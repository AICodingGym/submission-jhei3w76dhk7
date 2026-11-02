"""First learned baseline using only the approved Gym CSVs.

Validation holds out whole breaths. Training and selection use inspiration rows.
Control-history features reset at each breath; pressure is never an input.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata as metadata
import json
import time
from pathlib import Path

import lightgbm as lgb
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


STEPS = 80
DTYPES = {
    "id": "int64", "breath_id": "int32", "R": "int8", "C": "int8",
    "time_step": "float32", "u_in": "float32", "u_out": "int8",
    "pressure": "float32",
}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def features(frame: pd.DataFrame) -> tuple[np.ndarray, list[str], np.ndarray]:
    """Return features in original row order, after verifying 80-row blocks."""
    if len(frame) % STEPS:
        raise ValueError("Unexpected breath length; do not reshape this file")
    blocks = frame["breath_id"].to_numpy().reshape(-1, STEPS)
    breath_ids = blocks[:, 0]
    if not np.all(blocks == breath_ids[:, None]):
        raise ValueError("Breaths are not contiguous 80-row blocks")
    if len(np.unique(breath_ids)) != len(breath_ids):
        raise ValueError("Repeated breath blocks")
    if not frame["id"].is_unique:
        raise ValueError("Duplicate row IDs")
    u = frame["u_in"].to_numpy().reshape(-1, STEPS)
    t = frame["time_step"].to_numpy().reshape(-1, STEPS)
    if not np.all(np.diff(t, axis=1) > 0):
        raise ValueError("Timestamps must increase inside each breath")
    for column in ("R", "C"):
        values = frame[column].to_numpy().reshape(-1, STEPS)
        if not np.all(values == values[:, :1]):
            raise ValueError(f"{column} changes within a breath")

    columns = {}
    for column in ("R", "C", "time_step", "u_in", "u_out"):
        columns[column] = frame[column].to_numpy(dtype=np.float32)
    step = np.arange(STEPS)
    dt = np.diff(t, axis=1, prepend=t[:, :1])
    cumulative = np.cumsum(u, axis=1, dtype=np.float32)
    columns["step"] = np.broadcast_to(step, u.shape).ravel()
    columns["dt"] = dt.ravel()
    columns["control_sum"] = cumulative.ravel()
    columns["control_mean"] = (cumulative / (step + 1)).ravel()
    # Valve opening is not measured flow: this is a history proxy, not volume.
    columns["control_integral"] = np.cumsum(u * dt, axis=1).ravel()
    for lag in (1, 2, 4, 8):
        shifted = np.empty_like(u)
        shifted[:, :lag] = u[:, :1]
        shifted[:, lag:] = u[:, :-lag]
        columns[f"u_in_lag_{lag}"] = shifted.ravel()
        columns[f"u_in_change_{lag}"] = (u - shifted).ravel()
    padded_sum = np.concatenate([np.zeros((len(u), 1), dtype=np.float32), cumulative], axis=1)
    for window in (4, 8):
        begin = np.maximum(0, step + 1 - window)
        columns[f"u_in_mean_{window}"] = (
            (padded_sum[:, step + 1] - padded_sum[:, begin]) / (step + 1 - begin)
        ).ravel()
    names = list(columns)
    matrix = np.column_stack(list(columns.values())).astype(np.float32, copy=False)
    if not np.isfinite(matrix).all() or "pressure" in names:
        raise ValueError("Invalid features")
    return matrix, names, breath_ids


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--max-train-breaths", type=int, default=20000)
    parser.add_argument("--trees", type=int, default=300)
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument("--seed", type=int, default=20261102)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    hashes = {name: digest(args.data_dir / name) for name in ("train.csv", "test.csv", "sample_submission.csv")}
    print("Loading approved training data", flush=True)
    train = pd.read_csv(args.data_dir / "train.csv", dtype=DTYPES)
    x, names, breath_ids = features(train)
    settings = train[["R", "C"]].to_numpy()[::STEPS]
    strata = np.array([f"{r}_{c}" for r, c in settings])
    pool, valid_groups = train_test_split(
        np.arange(len(breath_ids)), test_size=0.1, stratify=strata,
        random_state=args.seed,
    )
    if 0 < args.max_train_breaths < len(pool):
        used_groups, _ = train_test_split(
            pool, train_size=args.max_train_breaths, stratify=strata[pool],
            random_state=args.seed + 1,
        )
    else:
        used_groups = pool
    if np.intersect1d(breath_ids[used_groups], breath_ids[valid_groups]).size:
        raise ValueError("Training and validation breath leakage")
    train_blocks = np.zeros(len(breath_ids), dtype=bool)
    valid_blocks = np.zeros(len(breath_ids), dtype=bool)
    train_blocks[used_groups] = True
    valid_blocks[valid_groups] = True
    inspiration = train["u_out"].to_numpy() == 0
    train_mask = np.repeat(train_blocks, STEPS) & inspiration
    valid_mask = np.repeat(valid_blocks, STEPS) & inspiration
    y = train["pressure"].to_numpy()
    x_train, y_train = x[train_mask], y[train_mask]
    x_valid, y_valid = x[valid_mask], y[valid_mask]
    print(f"Training: {len(used_groups)} breaths / {len(y_train)} scored rows", flush=True)
    print(f"Validation: {len(valid_groups)} breaths / {len(y_valid)} scored rows", flush=True)
    model = lgb.LGBMRegressor(
        objective="regression_l1", n_estimators=args.trees, learning_rate=0.07,
        num_leaves=63, min_child_samples=80, max_bin=127,
        subsample=0.9, subsample_freq=1, colsample_bytree=0.9, reg_lambda=1.0,
        n_jobs=args.threads, random_state=args.seed, deterministic=True,
        force_col_wise=True, verbosity=-1,
    )
    fit_start = time.monotonic()
    model.fit(
        x_train, y_train, feature_name=names,
        eval_set=[(x_valid, y_valid)], eval_metric="l1",
        callbacks=[lgb.early_stopping(30, first_metric_only=True), lgb.log_evaluation(25)],
    )
    fit_seconds = time.monotonic() - fit_start
    valid_prediction = model.predict(x_valid, num_iteration=model.best_iteration_)
    error = np.abs(valid_prediction - y_valid)
    validation_mae = float(error.sum(dtype=np.float64) / len(error))
    slices = train.loc[valid_mask, ["R", "C"]].copy()
    slices["absolute_error"] = error
    by_rc = slices.groupby(["R", "C"])["absolute_error"].agg(["mean", "count"])
    by_rc.to_csv(args.output_dir / "validation_by_rc.csv")
    print(f"Inspiratory validation MAE: {validation_mae:.6f}", flush=True)
    model.booster_.save_model(str(args.output_dir / "model.txt"), num_iteration=model.best_iteration_)
    np.savez_compressed(
        args.output_dir / "split_breath_ids.npz",
        trained=breath_ids[used_groups], validation=breath_ids[valid_groups],
    )
    # Training feature memory can be released before constructing the test matrix.
    del x, x_train, x_valid, train, slices
    test = pd.read_csv(args.data_dir / "test.csv", dtype=DTYPES)
    x_test, test_names, test_breath_ids = features(test)
    if test_names != names or np.intersect1d(breath_ids, test_breath_ids).size:
        raise ValueError("Unexpected test schema or overlapping breath IDs")
    prediction = model.predict(x_test, num_iteration=model.best_iteration_)
    sample = pd.read_csv(args.data_dir / "sample_submission.csv")
    if not sample["id"].is_unique or len(sample) != len(test):
        raise ValueError("Invalid sample submission IDs/count")
    ordered = pd.Series(prediction, index=test["id"].to_numpy()).reindex(sample["id"])
    if not np.isfinite(ordered.to_numpy()).all():
        raise ValueError("Missing or nonfinite prediction, or ID mismatch")
    submission = pd.DataFrame({"id": sample["id"].to_numpy(), "pressure": ordered.to_numpy()})
    submission_path = args.output_dir / "submission.csv"
    submission.to_csv(submission_path, index=False, float_format="%.8f")
    # Verify the serialized artifact that will actually be submitted.
    saved = pd.read_csv(submission_path)
    assert list(saved.columns) == ["id", "pressure"]
    assert np.array_equal(saved["id"].to_numpy(), sample["id"].to_numpy())
    assert np.isfinite(saved["pressure"].to_numpy()).all()
    results = {
        "experiment": "baseline_v001", "seed": args.seed,
        "data_sha256": hashes, "features": names,
        "versions": {p: metadata.version(p) for p in ("lightgbm", "scikit-learn", "numpy", "pandas")},
        "model_parameters": model.get_params(), "best_iteration": model.best_iteration_,
        "training_breaths": len(used_groups), "validation_breaths": len(valid_groups),
        "training_scored_rows": int(train_mask.sum()), "validation_scored_rows": int(valid_mask.sum()),
        "validation_inspiratory_mae": validation_mae,
        "fit_seconds": fit_seconds, "total_seconds": time.monotonic() - started,
        "submission_rows": len(saved), "submission_sha256": digest(submission_path),
        "prediction_min": float(ordered.min()), "prediction_max": float(ordered.max()),
        "all_submission_checks_passed": True,
        "training_scope": "20000 sampled training breaths by default; no full-data refit for this first submission",
    }
    (args.output_dir / "metrics.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2), flush=True)


if __name__ == "__main__":
    main()

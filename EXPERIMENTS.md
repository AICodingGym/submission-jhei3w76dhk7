# Experiment log

## Baseline v001 — November 2, 2026

The user authorized a valid first submission, including model training, after
reviewing the limits of the public AI benchmark evidence. Only the approved Gym
data is used. No original Kaggle data or existing competition solutions were used.

Plan: LightGBM 4.6.0 with L1 loss; 20,000 sampled training breaths; a fixed 10%
holdout of entire breaths stratified by R/C; history features that reset at each
breath. Select the checkpoint using inspiratory MAE. Predict every test ID and
verify the serialized `id,pressure` CSV before upload.

Rationale: a fast learned baseline establishes a real validation and Gym score
before spending GPU time on the proposed compact GRU. Cumulative valve opening is
a control-history proxy, not measured airflow or lung volume. Pressure and row/
breath identifiers are excluded from the feature matrix.

The public benchmark source exposes grading reports but not training code or
execution traces. Suspected implementation errors are not confirmed. The three
public runs show that best-run rankings differ from mean rankings; detailed
evidence is saved in `../benchmark-review/` relative to this local directory.

Results from the first training run:

- Trained on 20,000 breaths / 607,415 inspiratory rows.
- Validation: 6,791 entirely held-out breaths / 206,098 inspiratory rows.
- Validation inspiratory MAE: **1.0108896728514998**.
- Best iteration: 300 (the configured cap; validation was still improving).
- Fit time: 10.34 seconds; full script time: 26.14 seconds.
- CSV: 603,600 rows, `id,pressure`, finite values, exact sample ID order.
- CSV SHA-256: `b54845e6a6d39852acfbd40dfccab8e4ed5be67fc49f00bbd8cfc414cb457de5`.
- No full-data refit was performed for this first submission.
- Output directory: `outputs/baseline_v001/` (model, metrics, split breath IDs,
  per-R/C validation errors, and submission CSV).
- Independent synthetic checks passed for history boundaries, pressure-label
  independence, cross-breath independence, dtype, and submission alignment.
- Review noted a temporary float64 stacking allocation; measured array sizes fit
  within the 16 GiB container limit, so it was retained for this first baseline.
- Per-setting validation MAE ranges from 0.43255 at R=5/C=50 to 1.51807 at
  R=50/C=10; high-resistance settings are useful priorities for further diagnosis.
  These slice differences do not yet identify their cause.

Gym submission accepted: **MAE 1.02635**. The CLI returned “Successfully submitted
prediction” and the numeric score. This is a valid learned baseline. Its score is
below the displayed AIBuildAI reference (1.0759), while the stronger Disarray
(0.15171) and MLEvolve (0.14237) references remain substantially lower. These are
benchmark reference comparisons, not matched experiments on an identical split.

The standard CLI committed source locally in the DataHub competition repository,
but reported that automatic remote code archiving is not configured. Prediction
upload/scoring succeeded. AI session-log upload was explicitly disabled. Source,
model, metrics, exact split, CSV and CLI receipt are retained in our project; the
complete Codex interaction history should still be exported for Canvas.

Next experiments proposed for review (not run yet):

1. Increase the tree iteration cap and/or training-breath count separately: the
   first run's validation curve was still improving at 300 trees, and only 20,000
   breaths were used for fitting. Measure each change on the same held-out breaths.
2. Compare a compact unidirectional GRU (two layers, hidden size 128) using the same
   grouped split and masked L1 metric. Test whether learned control history improves
   on the hand-selected lag/summary features. This is a candidate, not a guaranteed
   improvement or a claim about what any benchmark agent implemented.
3. Inspect errors by R/C setting, then repeat promising candidates on another
   grouped split/seed before considering an ensemble.

No additional model variants have been trained after this first accepted CSV.

## Notebook conversion — November 2, 2026

At the user's request, `baseline_v001.ipynb` presents the same baseline as separate
cells for configuration, feature construction, splitting, fitting, validation,
prediction, metrics, and optional submission. The feature helpers and full
training pipeline match the script. Hyperparameters, split seed, feature logic,
and inspiratory scoring are unchanged.

The notebook defaults to `RUN_TRAINING = False` and `SUBMIT_TO_GYM = False`. Its
review cells load the accepted run, display the score, per-R/C errors, training
curve, and prediction preview, and verify the saved CSV. An enabled new training
run uses a separate output directory and refuses an existing directory. Optional
upload is separately gated and refuses duplicate receipts/logs.

Notebook schema/syntax validation, exact training-pipeline AST comparison, and
local review-mode execution passed. The script and all accepted baseline
artifacts retained their original hashes and modification times. This conversion
did not retrain the model or make another Gym submission.

# Final-fit V011 handoff

Status at account migration: source prepared and frozen; **no V011 D confirmation or final training has run**. No new final CSV or submission has been produced. Standing approval is recorded in `research/authorization_v008.json`. Continue through the root handoff; do not bypass selection or confirmation because the account changed.

## Authoritative source

- `final_fit_v011.ipynb` is authoritative. Temporary `/tmp` builders are not authoritative and may predate the fifth-candidate update.
- Executable-code SHA256: `f81befd83ede7d65dbce816f430f028256b140cc16903ace047205029b22b83a`.
- Raw notebook SHA256: `1a84c2c6db46c8be75823b18b3eca4ecab0fe3837b04685fa3cc7f322b0f3a20`.
- Code hashing joins all executable cell sources with one newline, then hashes UTF-8 bytes. Outputs/metadata do not enter that digest.
- Default execution is inert (`PA3_RUN_FINAL_V011` defaults to `0`). Source compiles, notebook validates, and all 20 synthetic protocol/CSV checks pass. Separate synthetic checks covered payload/data/preprocessing rejection and inference interruption recovery; no real data/models/outcomes were accessed by those checks.

Local repository: `/Users/generalclasher/Documents/dsc102/pa3/ventilator-pressure-prediction`. Course repository: `/home/v2gao/dsc102/pa3/gym-workspace/ventilator-pressure-prediction`. Execute the notebook independently in the approved course environment; the runner changes into its project root and restores the previous working directory afterward.

## Frozen choice and confirmation contract

The gate requires all **five** predeclared A comparisons to finish, then freezes the single lowest-A qualifying choice before D labels:

1. `shared_breath_offset`: deep `.5`, offset `.5`.
2. `full_context_tcn`: deep `.5`, fast TCN `.5`.
3. `deep_half_compact_curve_memory`: deep `.5`, original compact/curve/memory each `1/6`.
4. `deep_half_compact_curve_memory_attention`: deep `.5`, original compact/curve/memory/attention each `.125`.
5. `deep_half_compact_curve_memory_offset`: deep `.5`, original compact/curve/memory/offset each `.125`.

The fifth candidate is defined by `research/ENSEMBLE_HYPOTHESIS_v012.md`, `research/diversity_screen_v012.ipynb`, and `outputs/diversity_screen_v012/results.json`. The other fixed mixtures use `research/ENSEMBLE_HYPOTHESES_v010.md`, `research/diversity_screen_v010.ipynb`, and `outputs/diversity_screen_v010/results.json`; separate model screens are `outputs/controlled_experiments_v008` and `outputs/controlled_experiments_v009`. A qualification remains gain at least `.003` and a negative bootstrap upper95. Root/trainer independently verify these saved screens. Do not assume a final winner before their completed frozen comparison.

`confirmation_v011.ipynb` owns cold D fitting; its current source freeze and deployment notes are in [HANDOFF_CONFIRMATION_V011.md](HANDOFF_CONFIRMATION_V011.md). No actual D split/lock exists yet. It writes:

- `outputs/confirmation_v011/locked_before_D.json`, schema `confirmation_v011_locked_before_D`;
- `outputs/confirmation_v011/D_split.json`;
- `outputs/confirmation_v011/confirmation_result.json`, schema `confirmation_v011_result`;
- member checkpoints/reports/predictions under `outputs/confirmation_v011/D_models/`, plus D row IDs and fixed ensemble arrays.

The lock carries winner/baseline weighted members, deduplicated `required_members`, each recipe and A artifacts, component `source_fingerprints`, confirmation `main_code_sha256`, observed raw `selection_input_files` hashes, and the D split/rule. Member IDs/factory IDs are `original_compact`, `deep`, `curve`, `memory`, `attention`, `offset`, `tcn`. Recipes carry model spec, full original training config, seed, feature mode, loss kind, selected epochs, and the exact selected LR prefix. V012 changes no D-result schema.

Selection SHA is **compact canonical JSON**: `json.dumps(lock, sort_keys=True, separators=(',', ':'), allow_nan=False)`. It is external, not stored self-referentially inside the lock. Raw lock-file SHA is separate. Preserve strict matching of the actual raw files frozen in `selection_input_files`; confirmation's metadata-portability evidence does not authorize final-stage hash exceptions.

D is a fresh RC-stratified split inside original Afit: seed `20261202`, 54,323 D-fit and 6,791 D-validation breaths; original 6,791 A-validation breaths stay excluded. Split JSON records sorted global indices/int32 breath IDs, raw-array hashes, and counts for A/D groups. Final verifies these groups and reconstructs the declared split using known R/C. D pass requires positive gain and a wholly negative whole-breath, point-weighted 1,000-draw interval (seed `20261201`). The result must be complete, all members complete, and affirm frozen choice/no runner-up/no D weight or epoch search. Final verifies all declared D checkpoint/report/prediction/row-ID/ensemble hashes and recomputes the fixed blends **without D labels**. D remains resampling evidence, not an untouched test.

## Run interface and exclusion lock

API:

```python
v011_run_final(project_root='.', *, resume=False,
    expected_selection_sha256=...,
    expected_confirmation_file_sha256=...,
    expected_source_code_sha256=...)
```

Explicit environment variables:

```text
PA3_RUN_FINAL_V011=1
PA3_FINAL_V011_SOURCE_SHA256=f81befd83ede7d65dbce816f430f028256b140cc16903ace047205029b22b83a
PA3_FINAL_V011_SELECTION_SHA256=<reviewed compact canonical lock digest>
PA3_FINAL_V011_D_RESULT_SHA256=<independently reviewed raw confirmation_result.json digest>
PA3_RESUME_FINAL_V011=1  # only for an intentional unchanged resume
```

All three expected digests are mandatory. Root owns operational helpers and independently reviews the D result before setting its expected hash. Both confirmation and final runners acquire nonblocking `outputs/.v011_gpu.lock`; do not launch overlapping GPU jobs. Actual CUDA and strict determinism are required. No submission command exists in the notebook; root owns a later reviewed Gym CLI submission.

## Approved data and model sources

Only these frozen input files are accepted:

| Path | SHA256 |
| --- | --- |
| `data/train.csv` | `2dc30dc5c8e603c8c68200830eab7ed8c7af42c823f8ae68b0beb663eea817d7` |
| `data/test.csv` | `1ed86b32480e93397cc961dfd09af2d0bedfbab901921eac44de8ed78c3f1672` |
| `data/sample_submission.csv` | `de4c137a22804654b597723f32470b24f23d9ef662205eca0fe31b68970f0594` |

Original A groups come from `outputs/improvements_v005/sequence/split_breath_ids.npz`. All labeled fitting uses 67,905 complete 80-point breaths / 2,061,922 inspiratory points. All original combined47 numeric features, including R/C, stay unchanged. IDs remain alignment keys, not model features.

Model definitions are loaded from these source-locked notebooks under `research/` (exact code hashes are embedded in `V011_FINAL_COMPONENTS` and must match the lock): `feature_components_v005.ipynb`, `sequence_components_v005.ipynb`, `training_components_v008.ipynb`, `attention_components_v008.ipynb`, `memory_components_v008.ipynb`, `offset_components_v009.ipynb`, `tcn_components_v009.ipynb`, `tcn_fast_components_v009.ipynb`. TCN uses the frozen shifted-linear backend. No global engine source is rewritten.

## Reuse accepted originals; fit only selected new members

Accepted original all-data artifacts are under `outputs/improvements_v005/confirmation_round1/final_all/`:

| Member | Epochs | File | Exact checkpoint SHA256 |
| --- | --- | --- | --- |
| `original_compact` | 193 | `nn__capacity_bilstm128.pt` | `19897b624599c57f2e4a7f976b2d2fdd4d0b5b1ba3f3dbf6884198ebdef23883` |
| `deep` | 189 | `nn__capacity_deep_bilstm.pt` | `591e3a778af84bfe7fa0f6592f8595fa2c969bdbb37fc0a36a2a251eacb4aad0` |

Their `final_manifest.json` SHA is `a9e9e48881c169587728519c5a8ca400ab5a13b6c760fb635457308ecf2615fd`. Associated `record_nn__capacity_*.json` and `report_nn__capacity_*.json` hashes are embedded in `V011_ORIGINALS`. The verifier checks exact files, old lock/provenance, recipes, selected schedules, 67,905/2,061,922 counts, all-training group hash, complete payload/optimizer-step budget, all raw X/y/u_out fingerprints, independently refitted all-training preprocessing, and strict state reconstruction. The legacy provenance digest intentionally uses old spaced sorted JSON; V011 selection/design digests use compact JSON. Do not substitute one convention for the other. A failed reuse audit stops; it does not silently retrain or overwrite originals.

The accepted `.18550` CSV is `outputs/improvements_v005/confirmation_round1/final_all/submission.csv`, SHA `ff149f3ab87e1e52b948f536c9fdf9a526471ac0723b6b785bf84c053ebed607`. It is checked before and after work and never overwritten.

For the new five-member pool, only **curve, memory, offset** need new all-data fits. Other possible frozen winners fit only their selected new members. New fits call `fit_fixed_v008` with no holdout arrays, fresh all-training-only statistics, seed `20261102`, batch256, Adam/no decay, and the immutable A-selected epoch/LR prefix. Curve alone uses `curve_l1`; other members use original L1. New checkpoints include final source, selection/result, model-source, configuration, data, group and preprocessing fingerprints.

## Outputs, recovery and remaining limits

Everything new stays under `outputs/confirmation_v011/final_all/`: immutable `design.json`, per-new-member checkpoint/`.last`/report/record/epoch logs, reuse records, member test predictions/metadata, `weighted_test_predictions.npy`, `test_row_ids.npy`, `submission.csv`, `final_manifest.json`, and `events.jsonl`. Manifest records checkpoint/source/data/group/row/preprocessing/prediction/CSV hashes and runtime. Final refitting has no independent holdout.

- Training resumes from the authoritative `.last` with exact optimizer/RNG state. Changed source/recipe/data/statistics/runtime rejects resume. Missing `.last` beside a partial checkpoint requires review; do not delete or improvise.
- Inference cache reuse verifies checkpoint/test/row IDs plus file/array hashes. If interrupted between publishing an array and metadata, explicit resume recomputes the frozen checkpoint and requires exact equality before completing metadata. Conflicting orphan arrays are preserved and rejected. Missing array with existing metadata also requires matching recomputed array/file hashes.
- Test/sample must have exactly 603,600 unique IDs in identical order. Every member and fixed blend is finite native float64 over **all** rows/phases. CSV columns are exactly `id,pressure`, with exact round-trip IDs/values. No clipping, snapping, post-D weight search or output-based tuning.
- Default/synthetic checks and source reviews are complete; actual V011 D/final GPU execution is not. A confirmed D failure stops promotion; no runner-up is tried. Root must restore account/SSH access and consult its master handoff for pod/queue status before any authorized continuation.

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

At that stage, no additional model variants had been trained after the first
accepted CSV. Subsequent tuning is recorded below.

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

## Tuning v002 — November 2, 2026

Primary implementation: `model_tuning_v002.ipynb`. The first ten new configurations
use the original 20,000 training breaths and 6,791 validation breaths (607,415
training and 206,098 validation inspiration points). All models are selected by
pooled native-unit inspiratory MAE. Original baseline files remain unchanged.

| Variant | Training breaths | Main settings | Validation MAE | Training seconds |
| --- | ---: | --- | ---: | ---: |
| Original baseline | 20,000 | LGB, 300 trees, 63 leaves, lr .07 | 1.010890 | 10.34 |
| LightGBM | 20,000 | 1,000 trees, 63 leaves, lr .07 | 0.866746 | 30.32 |
| LightGBM | 20,000 | 2,000 trees, 127 leaves, lr .05 | 0.762585 | 64.24 |
| LightGBM | 20,000 | 2,500 trees, 255 leaves, lr .04 | 0.718027 | 95.00 |
| ExtraTrees | 20,000 | 150 trees, depth 18, min leaf 10 | 0.882724 | 72.65 |
| ExtraTrees | 20,000 | 250 trees, depth 24, min leaf 4 | 0.738020 | 121.91 |
| GRU | 20,000 | 64 units x 1, lr .001, 12 epochs | 1.198847 | 11.33 |
| GRU | 20,000 | 96 units x 2, dropout .10, lr .001, 12 epochs | 1.133280 | 14.73 |
| GRU | 20,000 | 128 units x 2, dropout .15, lr .00075, 12 epochs | 1.159091 | 16.43 |
| GRU, longer | 20,000 | 96 x 2, up to 100 epochs; best epoch 54 | 0.857128 | 75.95 |
| GRU, longer | 20,000 | 128 x 2, up to 100 epochs; best epoch 81 | 0.837811 | 122.25 |
| LightGBM, more data | 61,114 | Same 2,500-tree / 255-leaf settings | **0.664386** | 240.18 |

Exact settings, versions, checkpoints and trial outcomes are in
`outputs/tuning_v002/results.csv` and `design.json`. Neural training times include
epoch validation and checkpointing; tree times are the fit call, so the timing
columns are not a hardware-throughput benchmark. All trials completed. This is a
bounded search, not an exhaustive hyperparameter optimum.

### Separate training-size change and confirmation

The last row changes training size separately: 20,000 to all 61,114 original
training-pool breaths, holding the original 6,791 validation breaths and selected
tree settings fixed. It uses 1,855,824 fitting inspiration rows and improves MAE
from 0.718027 to 0.664386. This is a data-size effect, not solely a complexity gain.

Before expanding that pool, we selected 6,791 confirmation breaths from the 41,114
breaths used in neither original fitting nor original validation, using split seed
20261203. Existing 20,000-breath models were evaluated on the resulting 206,274
previously unused inspiration points: baseline MAE **1.009188**, selected tuned
tree **0.717813**. This confirms the tuned settings on another held-out group;
it is not a multi-training-seed confidence interval. Those confirmation breaths
were subsequently included in the 61,114-breath fit, so these confirmation scores
do not independently evaluate the expanded-data model.

### Data quality, cleaning and scaling

`quality_audit_v002.json` verifies schemas, numeric values, input ranges, IDs,
strict within-breath time ordering, constant R/C, 80-row blocks, sample alignment,
and exact full-breath duplicates. There were zero missing/nonfinite cells, zero
input-range violations, and no exact duplicate full input breaths or train/test
input-breath matches. No imputation, row removal or clipping was applied. Finite
negative pressures were retained because no verified error rule justified removal.

LightGBM and ExtraTrees used unstandardized physical feature values. GRUs fit
input mean/std only on selected training breaths and target median/IQR only on
their scored training labels. Predictions were inverse-transformed before MAE and
CSV generation. Raw inspiration masks were kept separate from scaled inputs.

### High-resistance diagnosis

`resistance_diagnostics_v002.json` contains weighted per-R/R-C errors, phase and
pressure-conditional diagnostics. For the tuned 20,000-breath tree, high-R errors
remain larger even within pressure quartiles and are worse in middle/late
inspiration. This is observational evidence, not a proven causal explanation.

Weighted R=50 MAE: original baseline **1.342823**, tuned 20,000-breath tree
**0.969711**, expanded-data tree **0.900381**. R=50/C=10 remains the weakest setting:
1.518069 -> 1.075089 -> **0.982501**. More capacity/data improved but did not remove
the regime gap; removing those valid observations is not justified.

### External scoring and selected artifacts

The tuned 20,000-breath tree was accepted by Gym at **0.72535 MAE**. The separate
expanded-data follow-up was accepted at **0.67230 MAE**, improving the original
Gym score 1.02635 by about **34.50%**. Hyperparameters were selected on validation;
Gym scores were not used to search configurations. Final validation improvement
against the original baseline is **34.28%**.

Final CSV: `outputs/tuning_v002/submission.csv`, 603,600 finite predictions in exact
sample ID order. SHA-256:
`2ceeacea489c7e43dab805aa5eeb9a6e491b022620bddf469baea085aadbbe2b`.
Receipts, model checkpoints, metrics, splits, epoch logs and notebook snapshots
are preserved. Optional AI session-log upload remained disabled. The CLI again
reported that automatic remote source archiving is not configured; source was
committed in the DataHub repository and retained in our project.


## Controlled follow-up v003 and sequence refinement v004

The completed v003 study contains 27 trial records. Its full controlled settings,
training-size comparison, learning-rate/capacity/regularization tests, seed
comparison, and grouped B confirmation are in `INVESTIGATION_v003.md` and
`controlled_improvements_v003.ipynb`. Independent local QA recomputed every score.
The selected GRU scores A MAE 0.496273 and B MAE 0.522832. Its verified CSV is
`outputs/controlled_v003/submission.csv`; no Gym score is available for it.
The equal-three-seed average did not beat the best individual on either split.

The subsequent seven-idea study is tracked in `INVESTIGATION_v004.md`.
`sequence_refinement_v004b.ipynb` continues it with a verified, mathematically
equivalent faster TCN backend; the original v004 notebook and partial trial remain
preserved. Completed non-TCN A trials are reused with full provenance checks.
`results_review_v004.ipynb` is the read-only review and artifact-verification entry
point. Validation evidence and the later all-labeled final fit are kept separate.


### Completed v004 outcome

The bounded A search selected 75% GRU continued at 1e-5 plus 25% LightGBM with
2,500 trees / 511 leaves. It improved the old best GRU on both grouped splits:

| Validation approach | A MAE | B MAE |
|---|---:|---:|
| Previous best GRU | .496273 | .522832 |
| Current-rate continuation | .494150 | .520394 |
| Selected blend | **.483719** | **.507593** |

Bidirectional GRU, learned R/C embeddings and both TCN rates were worse on A
under the tested budgets. The continuation and frozen blend passed B confirmation;
weights were not tuned on B. All configs, seeds, timings, genuine implementation
issues and limitations are in `INVESTIGATION_v004.md` and the executed notebooks.

Fresh final fitting used all 67,905 approved labeled breaths, retaining A-selected
budgets/LRs and fitting all-data scalers. These final models have no independent
holdout. Final CSV: `outputs/sequence_v004b/final_all/submission.csv`, 603,600 finite
rows in exact sample-ID order; SHA256:
`e4baa82cf3d3b2f68d04cb91a62f22a7dd056f059018bb2634a8ea248c55d51d`.
No new Gym score is available. Independent score/group/hash/scaler/CSV checks and
visual QA passed; the complete 134-file archive is backed up locally. See
`research/final_checks_v004b.json` and `PROCESS_STATUS.md`.

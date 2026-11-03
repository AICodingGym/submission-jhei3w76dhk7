# Controlled improvement investigation

Requested November 2, 2026. Implementation: `controlled_improvements_v003.ipynb`.
The notebook defaults to reviewing saved results. Training requires
`PA3_RUN_V003=1`; compatible resumption also requires `PA3_RESUME_V003=1`.
Previous notebooks, accepted submissions and data remain unchanged.

## Retained correct work

- All 61,114 non-validation breaths are already used by the accepted full-pool
  model; the original 6,791 validation breaths stay outside every new fit.
- Main LightGBM/GRU fits already optimize L1 on inspiration (`u_out == 0`).
  Loss and phase masking are retained. The older MSE-splitting ExtraTrees family
  is not continued in this investigation.
- GRUs already process independent 80-step breaths with zero initial state, use
  training-only input/target scaling, and restore the lowest-validation-MAE
  checkpoint. These practices are retained rather than ablated away.

## New controlled tests

Screening uses the exact saved 20,000-breath training sample and original A
validation group, with model seed 20261102. All other parameters remain fixed
within each stated comparison.

- History: neither lag nor change, lags only, changes only, and both. Current
  `u_in`, cumulative summaries and rolling means remain present in all four arms.
  Changes and lags are algebraically redundant given current `u_in`; these tests
  measure learner representation, not complete removal of history information.
- R/C: numerical values versus categorical codes for their three observed levels.
- Tree learning rate: .02/.04/.08 at the same tree cap and other settings.
- Tree capacity: 2,500/5,000 trees, then 127/255/511 leaves, tested separately.
- Tree regularization: L2 penalty 2 versus 10, separately from capacity changes.
- GRU schedule: learning-rate floor 0 versus 1e-5. Around the floor reference,
  test initial rates .0003/.00075/.0015, width 64/128, and dropout .15/.30
  separately, keeping two layers and the 100-epoch/patience-8 limits fixed.
- Expand the two best new tree arms and strongest screened GRU to 61,114 fitting
  breaths. Choose the configuration using A only.
- Hold that configuration and split fixed; vary only model seeds
  20261102/20261103/20261104. Compare their mean/range/best score with the
  equal-weight average of native-unit, aligned predictions.

Two independent tree fits can run concurrently at four CPU threads each; GPU
trials remain sequential. Atomic writes and a lock protect shared log tables.
Runtime fields distinguish fitting from total evaluation time and reused models.

## Confirmation and selection

Before fitting, lock B with grouped R/C-stratified seed 20261204: 6,791 breaths
inside A's training pool; 54,323 remaining breaths fit each B model. Original A
breaths enter neither B training nor B validation. B observations were used in
earlier full-pool A models, so this is resampling confirmation, not newly untouched
data. Within-B comparisons use freshly refitted models on identical B fit groups.

Freeze B tree counts, or GRU epoch counts and actual per-epoch learning-rate
schedules, from the corresponding A checkpoints. B scores supply no stopping or
scheduler feedback. Select the best individual seed on A before viewing B.
Whole-breath paired bootstrap intervals accompany B error differences.

The incumbent is always eligible. A replacement individual must beat it on both
A and B. The equal ensemble must beat the A-selected individual on both A and B
and the incumbent on B. Choose the lowest-A-MAE eligible approach. B therefore
serves a stated confirmation/filtering role, not an untouched final-test estimate.
No Gym scores or test labels guide this decision. Generate and re-read the final
603,600-row `id,pressure` CSV, checking finiteness and exact sample-ID order.

## Audit findings and genuine limitations

- Earlier tuning changed multiple parameters together. Its score improvements
  are real, but their individual causes cannot be assigned solely to tree count,
  width or learning rate. These new comparisons isolate those factors.
- All earlier LightGBM runs reached their iteration caps; the tree-budget test
  checks whether more boosting still improves held-out error.
- The older GRU schedule reached learning rates around 1e-8. This motivates the
  floor comparison; small rates alone do not establish harmful freezing.
- Review caught B being used for stopping in a draft. This was corrected before
  any v003 training: B uses A-frozen budgets and is scored only after fitting.
- Resume and prediction code now checks full configurations, source/model/group
  hashes and each model's input/category recipe. No stale result reuse in earlier
  completed runs was established by this audit.
- The local project Python lacked notebook-format tooling. Static checks used
  the already-installed conda Python; DataHub training uses the existing project
  environment. No package replacement or data modification was needed.

## Evidence and interaction history

`implementation_checks_v003.json` records schema, syntax, default-review and
feature/category/boundary checks. `outputs/controlled_v003/` will contain the
locked design, source fingerprint, split IDs, per-trial configurations, seeds,
runtimes, curves, checkpoints, per-R/C scores, ensembles and final CSV.

`interaction-history/` preserves timestamped snapshots of available visible
user/assistant messages. Notebook outputs, epoch logs and execution logs preserve
the experiment record. Snapshot coverage is explicit; retain the application's
full conversation export if the course requires its complete tool transcript.
No interaction history or new prediction CSV is uploaded by this notebook.

## Completed A screening results

All rows below use the same 20,000 fitting breaths, 6,791 A validation breaths,
model seed 20261102 and native-unit inspiratory MAE. Lower is better.

| Tree arm | A MAE | New fit seconds |
|---|---:|---:|
| Reference: 2,500 trees, 255 leaves, lr .04, L2 2; lags and changes | 0.718027 | Reused |
| Neither lags nor changes | 0.881310 | 85.31 |
| Lags only | 0.745866 | 95.61 |
| Changes only | 0.740276 | 95.48 |
| Categorical R/C | 0.716351 | 96.24 |
| Learning rate .02 | 0.748679 | 104.58 |
| Learning rate .08 | 0.706227 | 88.68 |
| 5,000 trees | 0.692632 | 173.82 |
| 127 leaves | 0.764461 | 82.30 |
| 511 leaves | 0.686367 | 121.13 |
| L2 penalty 10 | 0.715083 | 100.42 |

| GRU arm | A MAE | Best epoch | New fit seconds |
|---|---:|---:|---:|
| Reference: 128 units x 2, dropout .15, lr .00075, no LR floor | 0.837811 | 81 | Reused |
| LR floor 1e-5; otherwise reference | 0.831157 | 99 | 149.73 |
| Initial lr .0003, same floor reference | 1.060658 | 99 | 149.83 |
| Initial lr .0015, same floor reference | 0.780586 | 99 | 149.73 |
| Width 64, same floor reference | 0.970500 | 99 | 102.00 |
| Dropout .30, same floor reference | 0.866556 | 99 | 146.03 |

The floor comparison produced a small single-seed improvement. It does not
establish that LR decay explained the earlier GRU/tree gap. Higher initial LR
helped substantially under this training budget; lower width and more dropout
hurt. The models' small endpoint train/validation gaps provide little evidence
that excessive GRU overfitting was the main limitation.

Tree capacity helped: 511 leaves reduced both fitting-sample and validation
error versus 255 leaves; halving leaves hurt both. More trees also helped. The
larger train/validation gap at higher capacity merits monitoring, but validation
did not worsen in these capacity tests. Small categorical/L2 gains are preliminary
single-split findings; they were not among the two strongest tree arms expanded.

## Expanded training runs on A

All rows use the same 61,114 fitting breaths and unchanged A holdout.

| Model | A MAE | Checkpoint | New fit seconds |
|---|---:|---|---:|
| Prior accepted full-pool tree | 0.664386 | 2,500 trees, 255 leaves | Reused |
| Tree-count intervention | 0.625763 | 5,000 trees, 255 leaves | 457.92 |
| Leaf-count intervention | 0.618996 | 2,500 trees, 511 leaves | 275.44 |
| Selected screened GRU, lr .0015, floor 1e-5 | 0.496273 | Best epoch 99 | 420.81 |

The expanded GRU's endpoint fitting-sample MAE is 0.464049 versus A MAE 0.496273.
For this same GRU configuration, the 20,000-breath A score was 0.780586. Keeping
the epoch cap fixed while expanding data also increases batches per epoch from
79 to 239. This is a practical expanded-training improvement, not an experiment
that isolates data diversity while holding optimizer-update count or compute fixed.

Runtimes reflect different CPU/GPU containers and stages, not a hardware-speed
benchmark. Reused checkpoints had zero new fitting time; original timings remain
in v002. Torch/CUDA versions are unchanged in the new GPU pod; its driver is
580.126.20 versus 535.161.08 in the first pod. Reference inference scores reproduced
exactly, and all new controlled GRU arms share the current environment.

## Completed seed comparison and B confirmation

All three A models share the same full training group, hyperparameters and input
recipe; only model seeds differ. The B models are fresh fits on 54,323 breaths,
using each A member's frozen best-epoch/LR schedule without B stopping feedback.

| Model seed / approach | A MAE | B MAE |
|---|---:|---:|
| 20261102 | 0.496273 | 0.522832 |
| 20261103 | 0.509418 | 0.546660 |
| 20261104 | 0.580901 | 0.604428 |
| Equal-weight three-seed average | 0.505135 | 0.536962 |
| Prior full-pool tree configuration | 0.664386 | 0.673307 |

The equal average improves on the mean individual A score (0.528864), but not on
the best individual. It is worse than the A-selected individual on B as well, so
the predeclared rule selects GRU seed 20261102. The selected GRU improves B MAE
by 0.150475 against the freshly refitted tree reference; a paired whole-breath
bootstrap gives a 95% interval [-0.161369, -0.140556] for GRU minus tree error.
Ensemble minus selected-individual B error is +0.014130, interval
[+0.011474, +0.016818]. These intervals describe this B resampling comparison,
not uncertainty for a newly untouched test or every possible model seed.

All 27 trial scores were independently recomputed locally from saved predictions
and approved labels. A/B row alignment, fit/holdout separation, both equal-weight
averages, selected checkpoint hash, and serialized CSV checks passed. Records are
in `outputs/controlled_v003/final_local_verification.json`.

Selected CSV: `outputs/controlled_v003/submission.csv`, 603,600 finite rows in exact
sample-ID order. SHA-256:
`c9b8150bb835a42f1541ae5a7595b4cb7253f960a7001c1b06e034f3f97971b0`.
It was generated and backed up; no new Gym score has been measured for this CSV.
The separate v004 investigation preserves this validated fallback while testing
the user's subsequent sequence-model suggestions.

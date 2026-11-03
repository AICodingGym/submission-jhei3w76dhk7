# Offline sequence refinement v004

Completed implementation: `sequence_refinement_v004b.ipynb` (31 cells), with the
original `sequence_refinement_v004.ipynb` retained. It defaults to review mode.
`PA3_RUN_V004B=1` executes; `PA3_RESUME_V004B=1` reuses compatible completed stages.
Modeling code is contained in the notebook. `results_review_v004.ipynb` is the
executed read-only results and artifact-check notebook.

Only the approved Gym data is used. Prior notebooks, validation models and CSVs
remain intact. There is no automatic submission or interaction-history upload.

## Completed independent error analysis

`error_analysis_v004.ipynb` is executed and CPU-only. It uses A predictions from
completed v003 models and checks exact scored-row alignment, the 6,791 held-out
breaths, and the native-unit MAE. It neither fits models nor reads B outcomes.
All five figures were inspected; partition totals and figure hashes passed.

For the best v003 A GRU (MAE 0.4962725306), total absolute error is
102,280.7760 over 206,098 scored inspiration points.

| Slice | Scored-point share | Total-error share | MAE |
|---|---:|---:|---:|
| R=50 | 40.43% | 53.59% | 0.65791 |
| C=10 | 37.12% | 42.12% | 0.56323 |
| R=50/C=10 | 18.17% | 24.23% | 0.66177 |
| R=50/C=50 | 11.03% | 14.99% | 0.67417 |
| R=50/C=20 | 11.23% | 14.38% | 0.63568 |

R=50/C=50 has a higher MAE than R=50/C=10, but the latter contributes much more
total error. Late/middle/early inspiration contributes 36.97%/33.61%/29.43% of
error. Six highest-total-error breaths are plotted against actual pressure and the
strongest tree; they are selected hard cases, not representative examples. Their
errors run in both directions, so these plots do not establish a single bias or
justify removing valid data.

The best GRU and leaves-511 tree have signed-residual correlation 0.5805. Related
tree variants can correlate around 0.994. An A-only exploratory blend of 75% GRU
and 25% leaves-511 tree scores 0.4850823320, versus 0.4962725306 for the GRU alone
(2.25% lower). This is a candidate selected on A, not a confirmed final ensemble.
The new models will join a fresh, bounded A-only pair search before B confirmation.

Figures and detailed tables are in `outputs/sequence_v004/error_analysis/`.

## GPU experiment plan

| Suggestion | Controlled action |
|---|---|
| Lower-rate continuation | Same checkpoint and scalers, fresh Adam in both arms, identical seeds/shuffle, constant 1e-5 versus 1e-6, 30 additional epochs each; unchanged checkpoint is eligible at epoch zero. |
| Bidirectional GRU | Two layers, 80 units per direction, dropout .15; 170,305 parameters versus 160,833 for the current unidirectional GRU. Explicitly offline input access. |
| Small TCN | 72 channels, five residual blocks, dilations 1/2/4/8/16, two causal kernel-3 convolutions and timestep/channel LayerNorm per block; 161,561 parameters and receptive field 125. Test lr .0015 and .003. |
| R/C conditioning | Already present at every timestep. Separately replace numeric R/C with two learned 3-category × 2-dimensional tables; other 18 channels use training-only scalers. 161,613 parameters. |
| Error-diverse ensemble | Individual models and pair weights .25/.5/.75 on aligned native A predictions; residual correlation is diagnostic, actual MAE determines usefulness. Freeze members/weights before B. |
| Final fit on every labeled breath | After validation selection, fit fresh checkpoints on all 67,905 approved labeled breaths, using their own scalers and A-frozen duration/LR schedules. |

The checkpoint's actual learning rate already decayed to 1e-5; one-tenth of the
initial .0015 would instead increase that rate. Old checkpoints omit optimizer
state, so the continuation comparison explicitly resets Adam in both arms rather
than claiming exact optimizer-state resumption. Both arms preserve the original
input/target scaler coordinates.

The TCN adapts general residual dilated convolutions described by
[Bai, Kolter and Koltun](https://arxiv.org/abs/1803.01271). No competition-specific
implementation or external model/data is used. The user-provided
[PyTorch GRU documentation](https://docs.pytorch.org/docs/2.15/generated/torch.nn.GRU.html)
describes bidirectionality; execution will retain the course environment's
installed version rather than upgrading it. The assignment and discussion PDFs
contain no streaming restriction, and the approved test data provides every input
step. Offline future-input access is therefore the stated inference assumption;
unknown pressure is never an input.

## Confirmation and final refit safeguards

Validated A fitting continues to exclude original A validation breaths. Fresh B
fits exclude both A and B validation breaths. They replay A-selected schedules
without B stopping/scheduler feedback. A B warm start uses its B-only base, never
an A checkpoint that has already trained on B observations.

The reference is always eligible. New individuals must improve on it on A and B.
A pair must improve on the best individual on both splits and the reference on B.
The lowest-A-MAE eligible approach is selected. B is resampling confirmation and
a stated filtering stage, not an untouched final test.

The user's later all-labeled-fit request is an explicit exception for the final
stage only. Final models have no independent A/B holdout. Validation evidence
stays in `outputs/sequence_v004/experiments/validation_selection.json`; all-labeled
checkpoints and the final aligned CSV will be in `outputs/sequence_v004/final_all/`.
A final warm recipe first trains a fresh all-data base, then resets Adam for the
A-selected continuation while retaining that base's all-data scalers.

## Verification and current state

- `research/component_checks_v004.json`: 15 passing synthetic CPU checks, including
  checkpoint/scaler roundtrips, exact frozen replay, matched warm starts, category
  mappings, causal TCN prefix invariance, and cross-breath independence.
- `research/orchestration_checks_v004.json`: source compilation/default-review
  execution and read-only orchestration review passed. No v004 assignment model
  had trained at this preparation checkpoint; live execution is recorded below.
- Prior GPU deadline passed at 3:10 AM Pacific November 3. The SSH session expired
  and DataHub requires a fresh password/Duo login after eight hours. The user has
  been asked to reconnect using the persistent project control socket.
- Announced login-node maintenance is 7–8 AM Pacific November 3. New launch will
  use a staged container entrypoint so training can proceed without a login-node
  readiness worker once the container starts.

## Live execution — November 3

The reconnected login verified v003 completed all 27 trials and generated its
checked CSV. A temporary CPU-only pod staged the notebook in persistent course
storage and verified all four model shapes and parameter counts under course
Torch 2.2.1+cu121. No package upgrade was needed. That CPU pod was released.

GPU pod `v2gao-11673` started at 7:52:57 AM Pacific, passed CUDA arithmetic, and
started the notebook automatically from its container entrypoint. Its six-hour
deadline is approximately 1:52:57 PM Pacific. Model code remains unchanged from
the reviewed source. The matched warm starts both reproduced baseline A MAE
0.4962725306 before any continuation.

| Completed warm-start arm | A MAE | Selected extra epoch | Executed extra epochs | Seconds |
|---|---:|---:|---:|---:|
| Constant LR 1e-5 | 0.494150 | 29 | 30 | 130.56 |
| Constant LR 1e-6 | 0.495826 | 12 | 30 | 128.97 |

Both changes are small. Reducing the already-low rate another tenfold did not
beat continuation at the current rate in this matched comparison. Neither warm
arm is adopted before the remaining A search and B confirmation finish.
The bidirectional GRU completed 100 epochs in 561.98 seconds (selected epoch 99,
A MAE 0.5690773345). Learned R/C embeddings selected epoch 72, scoring
0.5351712787 in 364.72 seconds. Neither improves the reference on A.

### TCN throughput mistake and correction

The original TCN implementation was functionally valid but impractical on the
course GPU/software combination: its first full epoch took 549.67 seconds.
The time cap is checked between epochs, so it did not provide a strict 600-second
wall-clock bound. The run was paused and stopped, retaining its partial checkpoint
and logs; its severely undertrained result is not evidence against TCNs.

A synthetic profiler identified the slow dilated convolution fallback: 147,520
copy operations and 164,295 kernel launches in one batch. Disabling cuDNN did not
help. Isolated dilation-16 convolution took about .342 seconds per batch, while
ordinary convolution and LayerNorm were around .0015 seconds each.

`sequence_refinement_v004b.ipynb` is a separate continuation with its own output
directory. It computes the same causal windows with a matrix multiplication;
parameters, receptive field and model capacity are unchanged. Float64 output,
input gradient and every parameter gradient passed equivalence checks. The course
GPU's steady synthetic batch improved from 2.04 seconds to .0372 seconds. The
first actual epoch took 11.26 seconds. Floating-point summation and stochastic
training trajectories need not be identical across implementations.

Float32 CUDA checks also passed: maximum output difference 3.58e-7, maximum
input-gradient difference 1.43e-9, every parameter gradient within tolerance,
and zero change in a prefix when only future inputs changed. Independent source
review found no blockers in causal indexing, cache reuse or B/final replay.

The four completed non-TCN candidates are reused only after verifying unchanged
GRU/preprocessing/training source, matching recipes/data/group hashes, checkpoint
hashes, prediction hashes, row IDs, and recomputed MAE. They remain the original
experiments, not four additional fits. Neither original source nor outputs are
overwritten. The verified optimized TCN trials are now running, followed by the
same A ensemble search, frozen B confirmation and all-labeled final fit.

Operational mistakes during diagnosis were confined to checks: one synthetic
benchmark omitted the deterministic CUDA workspace variable and failed explicitly;
it was rerun with the real notebook's setting. Local notebook generation lacked
nbformat, so local compilation used JSON and the course environment then performed
the actual nbformat schema and default-review execution checks. Both passed.

The optimized lr .0015 TCN completed 52 epochs in 607.68 seconds, selecting
epoch 48 / A MAE 0.7303338192. Its time cap is checked between epochs; this small
overrun is expected and logged. The lr .003 comparison is running. This budget
does not establish an architecture-wide optimum.

The current-rate GRU continuation improves all nine R/C cells on A. Total absolute
error falls by 437.5165 over 206,098 scored points; R=50 accounts for 200.3759 of
that reduction. These remain A-selection findings until B confirmation.

### Completed A comparison and frozen ensemble

All six new comparisons use the original 61,114 A fitting breaths and 6,791
held-out A breaths, model seed 20261102, training-only statistics and inspiratory
L1/MAE. Imported arms retain their original runtimes and are not counted as new
fits in v004b.

| Model / controlled change | A MAE | Selected epoch / extra epoch | Training/evaluation seconds |
|---|---:|---:|---:|
| Reference GRU | 0.496273 | 99 | Reused from v003 |
| Current-rate continuation, 1e-5 | 0.494150 | 29 extra | 130.56 |
| One-tenth-rate continuation, 1e-6 | 0.495826 | 12 extra | 128.97 |
| Bidirectional GRU, 80 units/direction x 2 | 0.569077 | 99 | 561.98 |
| GRU with learned R/C embeddings | 0.535171 | 72 | 364.72 |
| TCN, lr .0015 | 0.730334 | 48 | 607.68 |
| TCN, lr .003 | 0.695900 | 34 | 483.43 |

The new architectures/embedding representation did not improve A in this bounded
search. This does not establish that those architecture families are inferior
under every tuning/training budget. The current-rate continuation is the best
individual. The 1e-6 arm is slightly better than the old baseline but worse than
continuing at 1e-5.

The A-only pair search includes individual vertices and weights .25/.5/.75 across
aligned model predictions. Its winner is **25% leaves-511 LightGBM + 75% current-rate
GRU continuation**, A MAE **0.4837194726** (2.11% below the best individual).
Members, weights, checkpoint hashes and the eligibility rule were locked in
`outputs/sequence_v004b/experiments/locked_before_B.json` at 8:54:20 AM Pacific,
before starting fresh B continuation/tree fits. B outcomes are not used to tune
weights.

### Confirmed B comparison and selected recipe

| Approach | A MAE | B MAE |
|---|---:|---:|
| Previous best GRU | 0.496272531 | 0.522832012 |
| GRU continued at 1e-5 | 0.494149674 | 0.520393853 |
| 25% larger tree + 75% continued GRU | **0.483719473** | **0.507592708** |

The continuation improves B by 0.0024381591; the paired whole-breath bootstrap
95% interval for continued-GRU minus reference error is [-0.0032297670,
-0.0016575609]. The frozen pair improves on the continued GRU by 0.0128011453;
its corresponding interval is [-0.0154676989, -0.0100254084]. Each bootstrap uses
1,000 whole-breath resamples with seed 20261206 and point-count weighting.
These intervals describe this B resampling comparison, not a newly untouched
test population or every possible seed. B supplies the stated eligibility filter,
not a weight or training-duration search.

The pair passes the predeclared rule and is selected. Final fresh fitting on all
67,905 approved labeled breaths is complete. It keeps the A-selected tree count,
GRU schedule and 29-epoch continuation, fits all-data scalers, and has no independent
A/B holdout. Validation evidence remains tied to the earlier models.

### Final all-labeled artifacts and checks

Final training uses all 2,061,922 approved inspiratory target points:

| Final stage | Frozen recipe | Fit seconds |
|---|---|---:|
| Larger LightGBM | 2,500 trees, 511 leaves; numeric R/C + history recipe | 289.20 |
| Fresh GRU base | 128 units x 2, dropout .15, 99 A-selected epochs/LRs | 449.68 |
| GRU continuation | Fresh Adam, constant 1e-5, 29 extra epochs, same all-data scalers | 133.26 |

The warm wrapper's elapsed time includes its nested base fit; do not add that
wrapper time to the base time again. The full v004b pipeline finished in 2,436.50
seconds, excluding earlier completed arms imported from v004.

Verified final CSV: **`outputs/sequence_v004b/final_all/submission.csv`**,
603,600 finite `id,pressure` rows in exact sample-ID order. SHA-256:
`e4baa82cf3d3b2f68d04cb91a62f22a7dd056f059018bb2634a8ea248c55d51d`.
`final_manifest.json` records model hashes, recipes, data hashes and the link to
earlier validation evidence. No new Gym submission or Gym score was produced.

The read-only course review independently recomputed all 14 saved validation
records, verified grouped splits and scored-row alignment, checked prediction
and checkpoint hashes, and verified final all-data scaler counts, raw-feature
means/std, target median/IQR, and serialized CSV alignment. All 18 primary and
five review code cells completed without errors. Local transfer checks verified
17 checkpoint records, 14 prediction hashes, unchanged notebook code, and the
local CSV. See `outputs/sequence_v004b/final_local_verification.json`.

The complete local backup contains 134 files, 225,432,958 bytes, archive SHA-256:
`589fdbdde0f40e7853b84089bbfce0d8e3f0f2d8201649560190ff13a65cd07c`.
It includes the final checkpoints, referenced validation checkpoints, predictions,
logs, notebooks, and review artifacts. Original data, notebooks and earlier CSVs
remain intact. Visible interaction-history snapshots are preserved separately.

### Remaining error pattern

The selected **validation** blend improves every R/C cell on A, reducing total
absolute error from 102,280.7760 to 99,693.6159. R=50 MAE falls from .657908 to
.647677, but it still contributes 54.13% of total error. R=50/C=10 contributes
24.57% (MAE .654117), versus 15.18% for R=50/C=50 despite that group's higher
MAE .665389. Thus high resistance, especially the larger C=10 slice, remains a
useful priority for future investigation.

Early/middle/late inspiration MAE is .411324/.515893/.527237, with total-error
shares 29.27%/34.04%/36.69%. The six preselected hard breaths still show errors
in both directions, and the blend does not fix every difficult example. These
observations do not justify dropping valid observations or applying a global
pressure offset.

Both `review/learning_curves.png` and `review/selected_hard_breaths.png` were
visually inspected: readable labels/legends, no clipped panels, and correct
inspiratory-only hard-case comparisons. The figures and R/C/phase tables are
embedded in `results_review_v004.ipynb` and saved under `outputs/sequence_v004b/`.

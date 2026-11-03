# Offline sequence refinement v004

Implementation: `sequence_refinement_v004.ipynb` (31 cells). It defaults to review
mode. `PA3_RUN_V004=1` executes the new investigation; `PA3_RESUME_V004=1` reuses
compatible completed stages. Modeling code is contained in the notebook.

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

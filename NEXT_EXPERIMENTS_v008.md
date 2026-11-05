# Proposed next controlled batch

Status: proposed; no new model code or training started. The user requested
continued iterative improvement. Their earlier per-hypothesis approval rule is
being clarified before implementation. Best accepted official MAE is .18550.

## Why change direction

V007's pressure-category head, stronger dropout and tested weight decay did not
improve A validation. Residual correction gave a consistent but small .000979
pair improvement, below the predeclared .003 gate. Larger copies of these same
experiments are not the first next investment.

New read-only analysis of the exact original A validation predictions confirms
MAE .19656260982217663 on 206,098 scored points / 6,791 whole breaths. Adjacent
signed errors correlate .9114; even after removing each breath's average error,
correlation is .7156. Errors include persistent breath-level offsets and smooth
shape errors. They are not concentrated primarily at abrupt pressure changes:
the largest10% of observed changes carry about11.1% of adjacent-point error.
These are descriptive diagnostics, not new predictors or model scores.

A label-dependent per-breath median correction is only an oracle diagnostic.
It uses unknown pressure labels, is not an allowed prediction method, and will
never enter features or a submission. Exact duplicate input breaths were absent
in the approved-data audit, so these diagnostics do not establish a noise floor.

## Three separate compact-model tests

| Arm | Exact initial change | Hypothesis / risk |
|---|---|---|
| Pressure-curve consistency | Original scalar LSTM + .10 times adjacent-pressure-increment L1; both adjacent points must be inspiratory | May reduce coherent shape drift. Can fit target noise; judged only by primary native inspiratory MAE. |
| Learned response memory | Add eight small nonlinear control-response/exponential-memory channels using known u_in, R/C and elapsed time; positive learned time constants, reset each breath | Learns delayed responses beyond existing fixed EWMA features. It is a predictive latent response, not a claim that valve percentage measures airflow. |
| Residual attention | Add one small attention block over the original compact bidirectional encoder's states; scalar head and main L1 unchanged | Lets positions explicitly consult the rest of the known breath inputs. Adds capacity and may overfit; an architecture package, not proof of attention alone. |

No combined arm initially. New feature branches never read pressure labels at
prediction time. Auxiliary pressure changes are training supervision only.
Existing future control inputs are allowed because whole breath inputs are known.

## Fixed controls and profiling

- Original compact BiLSTM128x2, combined47 known inputs, seed20261102, original
  grouped A split (61,114 fitting / 6,791 validation), batch256, Adam/no decay,
  dropout.15, and the same complete200-epoch frozen cosine rate list.
- Training-only feature/target statistics and independent breath state resets.
  Scalar native MAE baseline .214165568; fixed equal pair with the unchanged
  deep A member .196562610. Keep pair weights .5/.5.
- Preserve common initial weights where shape permits and log added parameters;
  do not claim identical stochastic trajectories across different architectures.
- Synthetic actual-GPU forward/backward/inference and exact resume tests first.
  Do not disable deterministic execution to bypass unsupported operations.
- Profile at the same256-breath batch. If an arm exceeds twice baseline step
  cost or the safe11GB memory envelope, stop for review rather than silently
  changing data, batch size, epoch budget or multiple model properties.

Baseline runtime suggests about2–4 GPU hours for the three-arm A screen;
implementation, debugging and scheduler wait are additional. One GPU at a time;
normal course launcher and checkpoint recovery only, no quota bypass.

## Selection, confirmation and final fit

Primary score stays native, point-weighted inspiratory MAE. Mean/median/tail and
R/C/phase error contributions remain logged secondary diagnostics. Keep best A
checkpoint and record full configurations, seeds, runtimes, genuine mistakes,
source/data/model hashes and visible AI interactions.

Retain the .003 pair improvement plus wholly negative whole-breath bootstrap95%
interval gate. Freeze the single lowest-A qualifying recipe, epoch/rate prefix
and pair weights before any new grouped confirmation outcomes. Fresh grouped
resampling seed20261202 inside original Afit, with own training-only statistics;
original Avalidation stays excluded from these fits. Confirmation is resampling
evidence, not a pristine untouched test. No runner-up or weight search after a
failed confirmation. Refit on all approved labeled breaths and submit only if
validated; retain .18550 CSV/receipt. Confirmation/final fits cost additional GPU
time. No official hidden score is used to tune hyperparameters or ensemble weights.

## General-method references

These references describe general methods, not ventilator competition solutions:
- Gneiting, Making and Evaluating Point Forecasts: https://arxiv.org/abs/0912.0902
- Vaswani et al., Attention Is All You Need: https://arxiv.org/abs/1706.03762

All expected gains above are hypotheses. No claim that .10 is achievable or that
any one change will halve the current official error.

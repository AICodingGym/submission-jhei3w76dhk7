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

Results are pending execution; this document makes no claim that the proposed
changes have improved the accepted model.

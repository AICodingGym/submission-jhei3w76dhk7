# Validation-only compute-saving workflow

New A-training experiments use `run_training_queue_v025` or `fit_validate_prunable_v025` in [training_workflow_v025.ipynb](training_workflow_v025.ipynb). Load the unchanged feature/sequence/V008 training components and [pruning_components_v025.ipynb](pruning_components_v025.ipynb) first. Model definitions and training logic remain in notebooks.

The frozen policy is `pruning_policy_v025.json`, SHA256 `0acdfa933d54fbae1e7728e2f8982bdae3f4227c6bd5187979bcd38b67e5fc88`. Calibration uses three independently audited, unaugmented full47-feature deep curve-loss histories: V013 plain, V024 span3 and V024 span7. They have exactly the same61114fit/6791validation arrays,206098 scored validation points,239optimizer steps/epoch, Adam configuration and200-epoch rate schedule. The augmented V021 mixup run is excluded from this convergence cohort.

Only best-so-far **native point-weighted validation inspiratory MAE** enters stopping. Training MAE and leaderboard scores are not used.

| Guard | Calibrated setting and basis |
|---|---|
| Warmup | Start comparing at epoch100/200; a stop also needs the full patience window after halfway. |
| Substantial deficit | More than **7.0845%** worse than the highest same-stage best MAE among all comparable references throughout the window. This is twice the largest observed3.5422% deficit later recovered by a winning historical run. |
| Stalled improvement | Best validation MAE improves at most **1.0095%** over the patience window; this tolerance comes from the largest per-run90th-percentile late-quarter validation variation. |
| Patience | **20 full evaluation intervals** (21 checkpoints), the largest observed gap between material validation improvements. |
| LR grace | **13 evaluations** after a major half-rate crossing, the largest observed recovery delay. Smooth cosine decay uses half-rate crossings rather than resetting grace for each tiny decrease. |
| Comparability | Exact arrays, sizes, backbone, objective, optimizer, rate schedule/prefix, optimizer steps and numeric runtime. The model variant/factory and implementation hashes must be known. At least two same-stage completed reference curves are needed. |
| Unfamiliar setup | Continue a representative when the architecture, data, optimizer, schedule, implementation or runtime lacks compatible history. Current calibration covers the specific200-epoch replay schedule; new scheduling families need reviewed calibration. |

The retrospective replay removes each target from its comparison set. All three completed histories were kept. This is a limited-history engineering check, not a guarantee for every future seed.

Before pruning, the wrapper verifies that V008 already saved the exact current checkpoint, optimizer state, RNG state, best validation snapshot and progress. It records status **pruned**, completed=False, the reason, best native validation MAE, epoch/steps/runtime, policy/reference identities and source/data/checkpoint hashes in `model.outcome.json` and `model.pruning.jsonl`. Original pruned files remain intact. `clone_pruned_state_v025` supports an explicitly recorded exact resume into a fresh stage.

The queue immediately advances after a pruned run. It waits on interruptions and stops for review on genuine failures. `candidate_readiness_v025` and `predict_completed_v025` prevent treating a pruned member as completed or silently dropping it from frozen ensemble weights.

Final all-data fits have no independent A holdout and are not pruned with training MAE. Different grouped-confirmation splits and their frozen budgets also lack this A comparison history. Existing hash-frozen legacy partial runs resume through their original trainer; this new source binding is used for new experiments.

The CPU workflow preflight passed **32 checks**, including checkpoint-before-stop, exact parameter/optimizer/RNG resumption, policy hash validation, unknown-context fallback, absence of training/leaderboard dependence, and immediate execution of the next queued experiment. A simulated flat lagging curve stopped at epoch120/200; the80-epoch saving is a simulation, not a claimed production saving. No production run has been pruned yet. Actual CUDA hook checks are required before deploying this workflow in the next GPU batch.

An initial calibration draft combined raw evaluation spikes with doubled maximum durations. It offered no useful stopping window under this cosine schedule and was rejected before deployment. Its measurements are preserved in `pruning_calibration_measurements_v025.json`; the final rule uses the same prefix-best statistic as online decisions and observed maximum recovery durations.


Independent review found that the wrapper cache identity initially omitted the native V008 arm and requested training-diagnostic size. Both are now bound before cached outcomes can be reused, with explicit changed-field rejection checks. No production training used the earlier wrapper. The original sources and CPU proof are preserved under `outputs/pruning_workflow_v025/before_identity_review/`.

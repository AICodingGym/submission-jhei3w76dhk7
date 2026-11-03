# Iterative improvement investigation v005

Started November 3, 2026, 1:25 PM Pacific. User explicitly authorized implementation and continued iteration
toward official Gym MAE **0.20 or lower**. Prior accepted model/CSV/receipt remain
preserved (official MAE 0.47462). Only assignment-approved Gym data is used.
Modeling remains in notebooks. No Kaggle originals, external competition models,
or existing competition solutions are used.

## Components and verification

- `research/feature_components_v005.ipynb`: exact legacy 20 plus independently
  testable known-input offline/dynamics blocks;76 synthetic CPU checks passed.
- `research/sequence_components_v005.ipynb`: variable-width inputs, GRU/LSTM,
  joint R/C/conditionalheads/residualprofiles, controlledschedules, train-only
  scalers, best checkpoints and authoritative last-epoch optimizer/RNG state;
  65 synthetic CPU checks passed.
- `tree_context_v005.ipynb`: three CPU tree feature comparisons with fixed
  parameters and verified baseline reuse;42 checks and independent source review.
- Course CUDA proof uses9 fresh child processes across uniGRU/BiGRU/BiLSTM:
  uninterrupted 4 epochs versus interrupted 2 + fresh-process resume to 4. All 213 exact
  state, optimizer, RNG, shuffle, history, prediction and metric checks passed.
- Both notebooks passed actual course nbformat/schema/default-review execution.

Native stacked cuDNN dropout has opaque state. V005 uses single-layer recurrent
modules plus explicit Torch dropout between layers, preserving architecture and
parameter count while making the stochastic state serializable. Seed trajectories
can differ from v004; the duration intervention compares the first 100 versus 200
within the new control trajectory. Exact exposed-state resumption was verified on
one course GPU/software stack; cross-hardware bitwise identity is not assumed.

## Validation and fixed comparisons

All A fits use 61,114 breaths; original 6,791 A validation breaths never enter fitting,
scaler fitting or target-profile fitting. Original A IDs are anchored to prior
canonical design hashes and saved split identities, with unique/full-partition
checks. A new RC-stratified C split (seed 20261117) is declared before results:
54,323 fit and 6,791 validation breaths inside A fit. It excludes original A from both
sides. C is resampling evidence, not newly untouched data.

1. Same uniGRU 128 x 2, 20 features, seed 20261102, 200 epochs, batch 256, Adam, masked L1:
   plateau patience 1, plateau patience 6, and 5-epoch warmup/cosine. No early stopping;
   checkpoint selection still uses lowest native-unit A inspiratory MAE. Fixed
   eval-mode training-sample MAE is logged alongside online training loss.
2. A-selected full 200-rate schedule is frozen for feature tests: causal20,
   offline (34 features), dynamics (33 features) and combined (47 features). Completed causal20 winner is reused.
   Feature tests have identical optimizer-update budgets/rate sequences.
3. Then compare uniGRU256, BiGRU128, BiLSTM128 and a deeper tapered BiLSTM using the
   selected representation. The deeper candidate changes several architecture
   features together and is labeled exploratory, not a single-factor explanation.
4. Separate joint R/C embedding,R/C output heads,training-only R/C-step residual
   profiles, inspiration-based continuous feature scaling, and dropout .05 variants.
5. Additional fixed-split seeds 20261118/20261119 for stability; freeze promising
   individual/ensemble recipes before fresh C confirmation and any all-data fit.

CPU tree tests run independently at 4 threads: exact old 2,500-tree / 511-leaf recipe,
seed 20261102, numeric R/C, with offline/dynamics/combined feature blocks. They use
only inspiration fitting rows, no validation callback or early stopping, and
save scored-row-aligned predictions. Old causal20 model is reused only after
source/data/group/checkpoint/prediction/metric verification.

## Files and process control

- GPU: `iterative_improvements_v005.ipynb`, current phase limit `capacity`.
  Continue later phases through `PA3_V005_PHASE_LIMIT` without editing source.
- CPU: `tree_context_v005.ipynb`.
- GPU artifacts: `outputs/improvements_v005/sequence/`.
- CPU artifacts: `outputs/improvements_v005/tree_context/`.
- Live epoch/progress JSONL files are in those directories; records include
  configurations, feature order, seed, runtime, MAE, training diagnostic and hashes.
- Persistent execution logs: `/home/v2gao/dsc102/pa3/setup/v005-sequence-execution.log`
  and `v005-tree-execution.log`; exclusive worker locks prevent duplicate stages.
- Source/design/feature-order fingerprints guard resume and completed reuse.
  Incomplete stage reports are never treated as completed experiments.
- Replacement GPU pod v2gao-306419 started 2:00:05 PM Pacific November 3 and is
  expected to expire 8:00:05 PM. Old pod metadata and logs were archived. Workers do not
  require the SSH client to stay connected. Epoch checkpoints permit continuation
  in a replacement course container; persistent home files survive pod expiry.

## Issues found before assignment fitting

Review corrected a prior-design guard that compared canonical JSON identity to
raw-file SHA. It now compares canonical hashes. A reviewer's claim that the old
head was direct linear was withdrawn after checking the actual MLP32 SiLU head;
no unnecessary baseline-head change was made. Cache metrics/alignment, split
atomicity and per-execution environment metadata were hardened before launch.

## Completed results as of 2:10 PM Pacific

All values below are native inspiratory MAE on the same A split. The fixed CPU
recipe improved from causal20 .618995818 to offline .529058496, dynamics
.575459164, and combined .503760064. Respective new-stage runtimes were 414.53,
393.21 and 469.25 seconds. No C or test score selected these representations.

The fresh GRU schedule control with patience 1 completed 200 epochs at .565606099
(best epoch 200; 1039.91 seconds). Patience 6 completed at .415483167 (best epoch
193; 959.04 training seconds), after exact-state resumption in the replacement
pod. The cosine comparison is running. The new patience-6 result is promising
relative to the prior blend A .483719473; it still requires the declared feature,
capacity and grouped-confirmation stages before final model selection.

The 43-file progress snapshot made at 1:48 PM is verified on DataHub and Mac:
168,087,105 bytes, SHA-256
`17b7cb44803f5771c48f7c66753a18e9f3979343a5991c40f83f5e1a978ca2bd`.
It contains completed trees, the completed schedule control and an interrupted
second schedule. Incoming notebook code matches local source; executed notebook
snapshots are preserved separately from the local editable originals.

`confirmation_final_v005.ipynb` is prepared for bounded A-only individual/pair
selection, own-C refits, eligibility filtering and final all-data fits. Its
logical/synthetic and review-mode checks passed; integration with real completed
records is checked before any assignment confirmation fitting. It has not
produced a C result or submission yet.

No new official Gym score is claimed. The accepted score remains .47462; the
target .20 remains an objective rather than a predicted outcome.

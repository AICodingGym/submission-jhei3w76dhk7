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


## Schedule and diagnostic interpretation

Within the new controlled backend, patience 1 reached the minimum rate at epoch
54; patience 6 reached it at epoch 163. Their best first-100-epoch A MAEs were
.577266766 and .424001165, versus .565606099 and .415483167 through 200. Allowing
more useful-rate training is better supported here than attributing the full
improvement to doubling epochs alone. This is a measured schedule weakness,
not evidence of label leakage or a programming bug in the old model.

The first completed-artifact review passed 48 checks with no missing/failed
checks. Five plots were generated and visually inspected. R=50 MAE falls from
.647677 in the old blend to .538759 in the new patience-6 GRU; it still contributes
52.42% of total absolute error. Early/middle/late MAEs are .382536/.435865/.428806.
Fixed difficult breaths still show both directions of error; no selective
removal of difficult labels or guessed pressure offsets is justified.

An exploratory A-only .75 GRU + .25 combined-tree blend reaches .399471, with
residual correlation .56067. This is not a frozen final selection: the remaining
schedule/feature/capacity models may supersede it, and no C outcomes were read.

Real-data confirmation preflight verified nine completed old/new A records:
source/data/group identities, checkpoints, preprocessing, prediction hashes,
row alignment and recomputed native MAEs. It performed no assignment fitting,
read no C outcomes and did not freeze a selection. A separate worker now waits
for the full capacity phase and released A worker locks before starting the
immutable A selection, C fits and final all-data fits. Upload remains separate.


At 2:21 PM the cosine schedule completed 200 epochs in 914.16 seconds, best A
.371981592 at epoch 189. It wins the three-way A-only schedule comparison. Its
full 200 learning rates are frozen for each feature comparison; selected epoch
189 is relevant only to any subsequent fixed-duration refit of this candidate.
The offline feature comparison is active. No C result or Gym upload exists yet.


## Independent CPU tree capacity trials

At 2:31 PM, `tree_capacity_v005b.ipynb` passed actual initialization guards and
started its first CPU fit (PID 420, four threads), alongside GPU sequence work.
The combined-input control is fixed at A .503760064. Two arms change only tree
count (2,500 to 5,000) or only leaf count (511 to 1,023); all other parameters,
input schema, seed and grouped A split remain fixed. Each uses a fixed budget
and no validation feedback. A fixed training-sample diagnostic and R/C total
error contributions will be logged. Partial interrupted fits are archived before
restart. These extra exploratory A results are excluded from the current
confirmation inventory; adopting them requires a later declared frozen round.
Default mode, schema, source compilation and separate-parameter-change checks
passed. No new tree result is claimed until the fit and aligned scoring finish.


At 2:36 PM, the 34-input offline GRU completed its full 200-epoch comparison:
A MAE .3518652 (display rounded; authoritative value in its record), selected
checkpoint epoch 192. This improves the same-budget causal20 cosine control
.371981592. The 33-input dynamics arm is active; the combined arm and capacity
comparisons remain pending. No C confirmation or new official score exists.


The 2:40 PM state archive is verified on DataHub and Mac: 32,278,043 bytes,
SHA-256 cb30016546f5144caaa21001dbfca175ccd3d249d2a32753fbf843c42d23f8b6,
61 manifest entries checked. Incoming notebook code matches existing source;
prior file versions and older documentation are preserved separately.

A local read-only review of eight completed A records passed 64 checks, with no
missing or failed checks, and all five regenerated figures were visually checked.
For the completed offline GRU, R=5/20/50 MAEs are .262008/.315486/.448856;
R=50 contributes 51.57% of remaining total absolute error. Fixed hard examples
show substantially corrected overprediction in several cases and persistent
underprediction in others. These selected examples do not establish population
performance by themselves. Original A scores and total-error tables provide
the quantitative evidence. The local font-cache warnings affected cache writes;
all figures rendered and were inspected successfully.


The 5,000-tree combined-input arm completed at A .4843908 (rounded display),
versus the fixed 2,500-tree control .503760064. Its 2,048-breath training-sample
MAE is .2493583. This is a measurable held-out improvement but remains weaker
than the sequence models; it does not enter the current frozen-confirmation
universe. The separate 1,023-leaf / 2,500-tree arm is running.

One snapshot-import issue was caught in the subsequent Git diff: an older
DataHub orchestration-check summary replaced the richer local summary. The
retained prior version was restored, and future differing research metadata is
stored separately rather than replacing local records. No modeling source,
fit, split, checkpoint or prediction was changed by this metadata correction.


At 2:59 PM both additional CPU capacity fits completed: 5,000 trees / 511 leaves
A .4843908, training diagnostic .2493583; 2,500 trees / 1,023 leaves A .4813969,
training diagnostic .2457249. Both improve the .503760064 combined-input control,
but both remain weaker than the sequence candidates and have substantial
training-versus-validation gaps. These A-only comparisons remain exploratory.
The CPU worker has completed; model backup and independent aligned-score checks
follow. The GPU combined-input comparison continues before larger architectures.


Full-model state snapshot at 3:00 PM verified on both hosts and safely extracted:
230,136,409 bytes, SHA-256
5d76e98307747e7546b42daec54569cb4f052a3da6f5d3f5425bb8f23cab9388,
77 entries including both larger tree model texts. Local independent checks
confirmed serialized tree counts (5,000 / 2,500), leaf parameters (511 / 1,023),
all 47 feature names, model/prediction/ID/breakdown hashes and original A alignment.
Recomputed MAEs are .4843908105201644 and .4813969457152611. Total stage runtimes
954.79 / 637.93 seconds include preprocessing and scoring; fit_seconds in this
additional notebook also includes any first-arm feature-cache construction.
These timings are operational measurements, not an isolated hardware benchmark.
The dynamics GRU completed at A .3410362 (rounded), best epoch 192; combined is
near completion. Larger sequence models and grouped C have not run yet.


At 3:09 PM the final feature arm completed: combined 47 inputs A .3347733
(rounded), best checkpoint epoch 193. The completed same-budget feature ranking
is combined .3347733, dynamics .3410362, offline .3518652, causal20 .3719816.
Combined wins A-only selection, and the 256-unit GRU capacity trial has started
with the same frozen 200-rate schedule, original grouped A split, seed and loss.
Its observed early throughput is about 8.2 seconds per epoch. Bidirectional GRU,
bidirectional LSTM and deeper tapered LSTM remain queued in the same worker.


At 3:37 PM the 256-unit, two-layer GRU completed 200 epochs. A MAE .2685072
(rounded), selected checkpoint epoch 198; same combined 47 inputs, fixed 200
learning rates, seed and grouped A split as the 128-unit .3347733 control. This
is a substantial capacity improvement. The BiGRU128 arm has started at roughly
7.2 seconds per epoch. It reads the complete known input sequence in both
directions, never pressure labels; the offline test inputs support that access.
The new GRU result is not a C confirmation or official Gym score.


At 6:57 PM, BiGRU128 completed at A .2623263 (best epoch 191), BiLSTM128 at
A .2141656 (best epoch 193). The deeper tapered BiLSTM was at epoch 197/200,
best A .2115441; it remains provisional until its full record is completed.
The user explicitly requested quiet waiting to conserve tokens; checks are now
made at expected stage boundaries or when operational action is necessary.

Because C/final fitting will exceed the current 8:00 PM pod deadline, a one-shot
login-side coordinator was started for v2gao-306419. It waits for a terminal pod
phase, archives pod metadata/logs, then uses the official course launcher for one
replacement with the saved three-worker startup script. It performs no training
on the login node. A cancellation marker is checked before launch; externally
removed pods do not trigger a replacement. All model data and epoch states are
persistent. A fresh source/data/group/metric check still precedes any C fit.


At 7:00 PM all four capacity arms completed. Deep BiLSTM A .2115441, best epoch
189, versus BiLSTM128 .2141656, BiGRU128 .2623263, uniGRU256 .2685072. The C
launcher then exposed a genuine orchestration mistake: exclusive NFS flock probes
used read-only descriptors, which this NFS mount rejects with EBADF. C had not
initialized, fitted a model, locked a choice or opened C outcomes. Both readiness
and notebook lock probes now open the existing files read/write. Original source
and failed logs are archived. A model/source/data/group/metric preflight passed
for all 17 completed A descriptors; actual course NFS probes and 12 local logical
checks passed. Confirmation source fingerprint changed to
21415181cbfc698d857ab71dc75403018e3184ead4466ac9ab1bb4f540bc89df.
A models, source, splits and predictions are unchanged. The confirmation worker
was restarted with the corrected source; the saved startup path uses that fix.


A second orchestration bug then stopped the first C member before model training:
logger event(kind, **values) collided with fixed_fit_started metadata kind=.
Renamed the positional argument event_name and added a regression call with
kind metadata. The failed pre-fit round and executed source/logs are archived.
No C model had trained or produced a score. The A lock was reissued under the
corrected source and explicitly compared with the archived one: approaches,
weights and required members are identical before any C fit. Source SHA is now
ddd2179e1f453252e112ee2f99083a5e3da3ce04468c4f877893ebb21720f2ae.
Local logical/schema checks and the logger regression passed; actual C training
was observed at legacy-base epoch 32. The saved startup helper uses this source.

Frozen A choices: best individual deep BiLSTM .21154409731752422; equal-weight
BiLSTM128/deep-BiLSTM pair .19656260982217663; incumbent blend .4837194725640346.
The pair crosses .20 on A only. Official MAE remains .47462; C confirmation,
all-approved-data refitting and a fresh Gym submission are still required.


At 8:00 PM the expected lifetime limit ended pod v2gao-306419. The renewal
coordinator archived its pod metadata/logs, deleted the expired object and used
the official course launcher to queue one replacement v2gao-486950 at 8:00:30.
C legacy controls and the small BiLSTM C fit had completed; the deep C fit was
checkpointing (last observed epoch 15 at 7:57 PM). Persistent home and all-data
source remain intact. The new startup resumes compatible completed/partial
states. This coordinator has finished its one replacement, not a perpetual loop.


Replacement v2gao-486950 started November 3 at 8:02:23 PM Pacific on
its-dsmlp-n06, GTX 1080 Ti, Torch 2.2.1+cu121/CUDA 12.1; arithmetic check passed.
Expected deadline November 4 at 2:02:23 AM. The completed A fits were verified
and reused in 8.57 seconds. C completed records were verified/reused; deep C
restored its optimizer/RNG/epoch state and resumed at epoch 21 (epoch 33 observed
at 8:11 PM). The GPU hardware/software family matches; cross-node bitwise
trajectory equality is not assumed. Final model selection still depends on the
completed grouped C check, followed by all-data refitting and official scoring.


At the user's explicit request, an interim submission was generated from the
frozen A-selected .5/.5 LSTM pair while grouped C continues. The new notebook
`interim_submission_v005.ipynb` performs inference only; it uses the A checkpoints
fitted on 61,114 breaths each and their own A-training preprocessing. It does not
claim an all-data final fit or completed C confirmation. Recomputed A MAE is
.19656260982217663. Approved train/test/sample hashes, model/record hashes and
sample ID alignment were checked; CSV 603,600 finite native-unit predictions,
SHA-256 914bf5eff4ff9c0cbd05ef8b35e9da7fd44b99e1036ed04e306ba88559ed503c.
Independent Mac transfer/source/CSV checks passed. C and final all-data fitting
remain unchanged; this interim Gym result will not retune the locked C recipe.


The requested interim submission was accepted: **official Gym MAE .19486**,
versus prior .47462, a 58.94% reduction in official error. This achieves the
numerical <= .20 objective. CSV hash unchanged; source archive confirmed by CLI.
Separate receipt records upload status; creation manifest remains unchanged.
C confirmation and final all-approved-data fits continue without retuning from
the interim test result. They remain required work in the planned pipeline.


At 9:41 PM the fresh grouped C comparison completed. The old reference scored
.5148863604280497, locked best individual .2316267258871465, and fixed .5/.5
LSTM pair .21061234304757373. The pair passed the declared A/C eligibility rule;
weights remained A-selected. Whole-breath paired bootstrap pair-minus-individual
MAE difference -.02101438, 95% interval [-.02489869,-.01762333], 1,000 repeats.
C is resampling confirmation, not a pristine final test. Fresh all-67,905-breath
fits began using the selected A epoch budgets/rates and their own all-data
preprocessing. Earlier A/C scores describe validation models, not those final
models. Interim official MAE .19486 remains accepted and unchanged.


## November 4 morning recovery and final artifact preservation

The original final pipeline completed overnight before pod expiry. Both LSTM
members were freshly fitted on all 67,905 breaths (193 and 189 fixed epochs).
The final 603,600-row CSV SHA-256 is
`ff149f3ab87e1e52b948f536c9fdf9a526471ac0723b6b785bf84c053ebed607`.
The 76,116,474-byte final archive SHA-256 is
`4b31b09cb15f81cac4bedb710af2d51d70d5cbe13ed809ced304ace571d99676`.
All 16 archive files and the 38-file C backup were verified after local transfer.

A genuine pilot setup mistake compared metadata-inclusive array hashes to the
original design's raw-byte group hashes. This rejected the correct split and
stopped before assignment-data pilot training. Original executed source and
logs were preserved. Only that hash convention was corrected; every group,
recipe, data file and model seed remains unchanged. Corrected source SHA-256:
`627d48f7726e919a21f10884c2d557132f8f8eef1c9a56fb34316829e3dd6920`.
Actual-course preflight verified all group hashes, the exact original A model
fingerprint, and 840 exact CUDA continuation checks. Approved H1/H2 trials
resumed in official course pod `v2gao-1042868`; H3/H4 remain unstarted.

Final all-data submission accepted: **official MAE .18550**, compared with
interim .19486 (4.80% lower error). No weights or model choices were changed
using this official score. Independent CPU inference on 32 test breaths
(2,560 points) agreed with GPU CSV within 1.34e-5 absolute pressure; approved
file hashes, C metrics/model hashes, final scaler fitting counts and exact
sample/test IDs were verified. Receipt: `research/submission_receipt_v005_final.json`.

# PA3 setup

Setup date: November 2, 2026. The initial setup records precede modeling. A later
user request authorized the first baseline; see `EXPERIMENTS.md` for its results.

## Approved local data

The archive was obtained using the assignment-approved command:

```bash
aicodinggym mle download ventilator-pressure-prediction --workspace-dir /Users/generalclasher/Documents/dsc102/pa3
```

Files in `data/`:

| File | Data rows | Bytes |
| --- | ---: | ---: |
| `train.csv` | 5,432,400 | 299,670,301 |
| `test.csv` | 603,600 | 25,548,506 |
| `sample_submission.csv` | 603,600 | 5,321,307 |
| `description.md` | — | 5,799 |
| `ventilator-pressure-prediction.zip` | — | 103,595,202 |

The ZIP passed full CRC validation and was extracted without overwriting files.
`data-manifest.json` records SHA-256 hashes and paths. `data-validation.json`
records passing schema, numeric/finiteness, and test/submission ID-order checks.
The description includes historical competition dates; use the course assignment
PDF for the current deadline.

Use only this Gym-provided data. Do not download original Kaggle data, derived
data/models, or existing competition solutions. Keep the source data unchanged.

## Working environment

The active course GPU container is **`v2gao-11673`**, started at **7:52:57 AM
Pacific on November 3, 2026**, on `its-dsmlp-n05.ucsd.edu`. It passed CUDA
arithmetic and the current notebook started automatically. Its launch uses one
GPU, 8 CPU/16 GiB limits (scheduling requests 4 CPU/8 GiB), and the official
DataHub user initialization before `setup/start_sequence_v004.sh`.

Verified environment: GTX 1080 Ti (11 GB VRAM), Python 3.11.9, Torch 2.2.1+cu121 /
CUDA 12.1, NumPy 1.26.4, pandas 2.2.2, LightGBM 4.6.0 and nbformat 5.10.4. The
project environment was reused without upgrades. Verification and execution logs
are in `/home/v2gao/dsc102/pa3/setup/v004-startup-verification.json` and
`setup/sequence-v004-execution.log` at that project root.

The active continuation is now `sequence_refinement_v004b.ipynb`, worker PID 925,
with `setup/sequence-v004b-execution.log`. It replaces the inefficient TCN
convolution backend with a verified equivalent implementation. Four completed
non-TCN comparisons are reused with provenance checks. Original v004 files are
preserved. See `PROCESS_STATUS.md` for a timestamped map and
`INVESTIGATION_v004.md` for the diagnosis.

Earlier containers `v2gao-254347` and `v2gao-939516` expired and were archived and
removed. Their completed models, notebooks and data remain in persistent home
storage. The temporary CPU staging pod has also been released.

Connect from your Mac:

```bash
ssh v2gao@dsmlp-login.ucsd.edu
```

Then, on the login server:

```bash
kubesh v2gao-11673
```

Inside the container, activate the environment and enter the work directory:

```bash
source /home/v2gao/dsc102/pa3/.venv/bin/activate
cd /home/v2gao/dsc102/pa3/gym-workspace/ventilator-pressure-prediction
```

Use this directory for the next phase. Approved DataHub files are in its `data/`
directory, with the same names and byte-for-byte contents as the local files
listed above. Use the project interpreter
`/home/v2gao/dsc102/pa3/.venv/bin/python`.

Use official `kubesh`: it initializes DataHub's Unix user mapping. Plain raw
`kubectl exec ... bash` can omit that initialization and break tools such as
`ssh-keygen`. This setup uses a batch/shell container; no Jupyter server or
notebook URL was started.

The current pod's six-hour active deadline is **1:52:57 PM Pacific on
November 3, 2026**. Queue waiting did not consume this lifetime. Home-directory files
persist after it stops. When finished with the GPU, exit to the login server and
run `kubectl delete pod v2gao-11673` to release it. Do not run training on the
login server.

A separate local backup environment is available on this M3 Pro Mac:

```bash
cd /Users/generalclasher/Documents/dsc102/pa3/ventilator-pressure-prediction
source .venv/bin/activate
```

Select `.venv/bin/python` in your editor if using that backup. PyTorch MPS GPU
arithmetic and NumPy/pandas imports passed; see `environment-verification.json`.
This Mac has an Apple GPU, not an NVIDIA/CUDA GPU. Exact installed local packages
are in `requirements-setup.lock.txt`.

## Setup records

The main local setup log is `../SETUP_LOG.md`; a copy is saved in the DataHub
project's `setup/SETUP_LOG.md`. Remote verification records are in
`/home/v2gao/dsc102/pa3/setup/` and `setup-manifest.json` at that project root.
Local copies are `datahub-verification.json`, `datahub-data-integrity.json`, and
`datahub-setup-manifest.json`. Keep this conversation for the course's
required AI interaction history; the optional Entire recorder is not installed.
No session logs were uploaded by this setup.

Setup is complete. Open `baseline_v001.ipynb` to track the first baseline in cells:
configuration, feature construction, grouped splitting, training, validation,
predictions, and saved results. It defaults to review mode, loading the accepted
run without retraining or submitting. For a new run, set `RUN_TRAINING = True`
and choose a new `RUN_NAME`; the optional submission switch is separate and off.
Use the project virtual-environment kernel when training.

The original `train_baseline.py` is retained. `EXPERIMENTS.md` records the run,
and `outputs/baseline_v001/` contains the accepted artifacts.

For the later model comparison, open `model_tuning_v002.ipynb`. It defaults to
reviewing saved results; `PA3_RUN_TUNING=1` enables a new search and
`PA3_RESUME_TUNING=1` resumes compatible completed work. Use a new RUN_NAME for an
independent new search. Results and the selected submission are in
`outputs/tuning_v002/`; quality and resistance diagnostics are separate JSON files.
The comparison includes larger LightGBM models, ExtraTrees, GRUs, a training-size
ablation, and confirmation on previously unused breaths. See `EXPERIMENTS.md`
for all settings, limitations, and results.

The next controlled investigation is `controlled_improvements_v003.ipynb`.
It defaults to review mode; `PA3_RUN_V003=1` enables execution and
`PA3_RESUME_V003=1` enables compatible resumption. See `INVESTIGATION_v003.md`
for the ten-idea audit, separate ablations, fixed model seeds, equal-weight
ensemble, and A-frozen-budget confirmation on grouped split B. Source data and
the original validation breaths remain protected. Live results are in
`outputs/controlled_v003/`; no CSV upload is enabled by this notebook.

A temporary CPU-only pod completed tree screening and the two full-pool tree
arms while the GPU queued. Its execution snapshot is
`controlled_improvements_v003_cpu_screen.ipynb` on DataHub; that pod has been
released. The GPU notebook reuses the verified fits. Visible-conversation
snapshots are preserved in `interaction-history/`.

The subsequent offline sequence investigation is `sequence_refinement_v004.ipynb`.
It compares matched low-rate continuation, a compact bidirectional GRU, R/C
embeddings, a causal TCN, and A-selected error-diverse pairs. The separate final
fit on all 67,905 approved labeled breaths is explicitly authorized by the user's
later request; its checkpoint will have no independent A/B holdout. Validation
evidence stays separate in `outputs/sequence_v004/experiments/`; the final all-data
CSV will now be `outputs/sequence_v004b/final_all/submission.csv`. Review is the default;
`PA3_RUN_V004=1` enables training and `PA3_RESUME_V004=1` reuses compatible completed
stages. `error_analysis_v004.ipynb` contains the executed error-contribution and
hard-breath plots. See `INVESTIGATION_v004.md` for methodology and current results.

For the optimized continuation, use `PA3_RUN_V004B=1` and
`PA3_RESUME_V004B=1` only when intentionally continuing a compatible run.
`results_review_v004.ipynb` reviews saved results and verifies artifact alignment
without training or uploading a submission.

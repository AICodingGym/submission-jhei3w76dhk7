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

The selected working environment is the course DataHub. The original container
`v2gao-254347` expired at its six-hour deadline and was archived and removed.
Replacement pod `v2gao-939516` was submitted at about 7:55 PM Pacific on November 2.
It started at **9:10:09 PM Pacific**, after about 75 minutes queued, and passed
CUDA and persistent-file verification. It was submitted with:

```bash
launch-scipy-ml.sh -W DSC102_FA26_001 -g 1 -c 8 -m 16 -B /bin/sleep infinity
```

The first container started at about 1:30 PM Pacific on November 2 after about
38 minutes queued. Its verified hardware/software was GTX 1080 Ti (11 GB VRAM),
Python 3.11.9, image PyTorch 2.2.1+cu121 / CUDA 12.1, NumPy 1.26.4, pandas 2.2.2,
and Gym CLI 1.1.0. CUDA
arithmetic, imports, Gym configuration, and approved data integrity all passed.
A readiness worker repeated these checks in the replacement container and saved
`/home/v2gao/dsc102/pa3/setup/restart-v2gao-939516.json`.
CPU/RAM limits are 8 CPUs and 16 GiB; scheduling requests are 4 CPUs and 8 GiB.

Replacement verification is complete: GTX 1080 Ti (11 GB VRAM), driver
580.126.20, the same project Python/Torch/CUDA versions, working CUDA arithmetic,
matching approved-data/notebook/submission hashes, and the saved Gym identity.

Connect from your Mac:

```bash
ssh v2gao@dsmlp-login.ucsd.edu
```

Then, on the login server:

```bash
kubesh v2gao-939516
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

The replacement pod's six-hour active deadline is **3:10:09 AM Pacific on
November 3, 2026**. Queue waiting did not consume this lifetime. Home-directory files
persist after it stops. When finished with the GPU, exit to the login server and
run `kubectl delete pod v2gao-939516` to release it. Do not run training on the
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

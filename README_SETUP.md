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

The selected working environment is the running course DataHub GPU container,
pod `v2gao-254347`. It was submitted with:

```bash
launch-scipy-ml.sh -W DSC102_FA26_001 -g 1 -c 8 -m 16 -b
```

It started at about 1:30 PM Pacific on November 2 after about 38 minutes queued.
Verified hardware/software: GTX 1080 Ti (11 GB VRAM), Python 3.11.9, image PyTorch
2.2.1+cu121 / CUDA 12.1, NumPy 1.26.4, pandas 2.2.2, and Gym CLI 1.1.0. CUDA
arithmetic, imports, Gym configuration, and approved data integrity all passed.
CPU/RAM limits are 8 CPUs and 16 GiB; scheduling requests are 4 CPUs and 8 GiB.

Connect from your Mac:

```bash
ssh v2gao@dsmlp-login.ucsd.edu
```

Then, on the login server:

```bash
kubesh v2gao-254347
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

The current pod's six-hour deadline is approximately **7:30 PM Pacific on
November 2, 2026**. Home-directory files persist after it stops. When finished
with the GPU, exit to the login server and run `kubectl delete pod v2gao-254347`
to release it. Do not run training on the login server.

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

Setup is complete. The first accepted learned baseline is documented in
`EXPERIMENTS.md`, with source in `train_baseline.py` and artifacts in
`outputs/baseline_v001/`.

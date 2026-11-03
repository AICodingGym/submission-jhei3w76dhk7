# Process map

Checked **November 3, 2026, 9:03 AM Pacific**. This is a timestamped snapshot;
the JSONL epoch logs contain newer live progress.

```text
Approved data + environment checks       COMPLETE
  └─ v003: 27 experiments + verified CSV  COMPLETE
      └─ v004 error analysis + plots     COMPLETE
          └─ v004 model comparisons
              ├─ Fine-tune LR 1e-5       COMPLETE — A MAE .49415
              ├─ Fine-tune LR 1e-6       COMPLETE — A MAE .49583
              ├─ Bidirectional GRU      COMPLETE — A MAE .56908
              ├─ Learned R/C embeddings COMPLETE — A MAE .53517
              ├─ TCN LR .0015           COMPLETE — A MAE .73033
              └─ TCN LR .003            COMPLETE — A MAE .69590
                  └─ A ensemble search  COMPLETE — A MAE .48372
                      └─ B confirmation COMPLETE — blend B MAE .50759
                          └─ Final all-labeled fit RUNNING
                              └─ CSV + independent QA + backup WAITING
```

| Process / location | State |
|---|---|
| SSH connection to `dsmlp-login.ucsd.edu` | Connected through the user's authenticated shared connection. |
| Course GPU pod `v2gao-11673` | Running on `its-dsmlp-n05.ucsd.edu`, GTX 1080 Ti; deadline 1:52:57 PM Pacific. |
| Notebook worker PID `925` | Running `setup/execute_sequence_v004b.py`; one active model-training process. |
| Original notebook worker PID `119` | Stopped after preserving the slow TCN attempt. |
| Pod startup shell PID `44` | Sleeping after the original worker stopped; the pod remains available. |
| Temporary CPU staging pod | Released after successful staging/checks. |
| Research agents | No agents currently training or doing research; completed review/analysis is incorporated. |
| Read-only report worker PID `1190` | Waiting for model completion; then CPU verification, plots and archival. |

The original dilated-convolution backend took 549.67 seconds for its first epoch.
The verified equivalent implementation took 11.26 seconds. Four completed non-TCN
comparisons are imported with source/recipe/split/hash/metric checks. No conclusion
about TCN accuracy is drawn from the interrupted original run.

A ensemble weights are frozen: 25% leaves-511 LightGBM + 75% GRU continued at LR
1e-5. The pair passed B confirmation: A MAE .4837194726, B MAE .5075927078.
Final fits use all 67,905 labeled breaths and have no independent A/B holdout.

Persistent DataHub work directory:

`/home/v2gao/dsc102/pa3/gym-workspace/ventilator-pressure-prediction`

- Active notebook: `sequence_refinement_v004b.ipynb`
- Live model logs: `outputs/sequence_v004b/experiments/*_epochs.jsonl`
- Execution log: `/home/v2gao/dsc102/pa3/setup/sequence-v004b-execution.log`
- Existing verified CSV: `outputs/controlled_v003/submission.csv`
- Pending all-labeled CSV: `outputs/sequence_v004b/final_all/submission.csv`
- Read-only review: `results_review_v004.ipynb`
- Method/results record: `INVESTIGATION_v004.md`

Home-directory files survive pod expiry. Earlier local backups are preserved.
Current scores refer to validation models; the all-labeled final model will not
have the same independent holdout.

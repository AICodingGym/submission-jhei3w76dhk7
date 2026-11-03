# Process map

Checked **November 3, 2026, 9:33 AM Pacific**. All modeling, review, backup and Gym submission stages are complete.

```text
Approved data + CUDA environment           COMPLETE
  └─ v003: 27 controlled experiments       COMPLETE
      └─ Error contributions + hard plots COMPLETE
          └─ v004: six A comparisons      COMPLETE
              └─ A ensemble weights       FROZEN
                  └─ B confirmation       COMPLETE
                      └─ All-labeled fit  COMPLETE — 67,905 breaths
                          └─ CSV + QA     COMPLETE — 603,600 rows
                              └─ Backup   VERIFIED on DataHub and Mac
                                  └─ Gym  ACCEPTED — MAE .47462
```

| Process / resource | Current state |
|---|---|
| GPU training worker PID `925` | Finished successfully; all 18 modeling code cells completed. |
| CPU review worker PID `1190` | Finished successfully; all five review code cells and backup completed. |
| Mac verification | Passed: archive checksum, 17 checkpoint records, 14 prediction hashes, CSV alignment and plot inspection. |
| Research agents | No active work; completed analysis/reviews incorporated. |
| Course pod `v2gao-11673` | Running and idle; no GPU compute process. Deadline **1:52:57 PM Pacific November 3**. |
| SSH connection | Connected through the user's authenticated shared connection. |
| Earlier slow TCN worker PID `119` | Stopped; original notebook and partial trial preserved. |
| Temporary CPU staging pod | Released. |

The selected recipe is **75% continued GRU + 25% larger LightGBM**.
Earlier validation-model MAE: **A .4837194726 / B .5075927078**.
The final models are fresh fits on all approved labeled breaths and have no
independent A/B holdout. Gym submission is now accepted: **official MAE 0.47462**. Source code was archived by the CLI.

Persistent DataHub work directory:

`/home/v2gao/dsc102/pa3/gym-workspace/ventilator-pressure-prediction`

- Executed modeling notebook: `sequence_refinement_v004b.ipynb`
- Executed results/plots/checks notebook: `results_review_v004.ipynb`
- Final CSV: `outputs/sequence_v004b/final_all/submission.csv`
- Validation evidence: `outputs/sequence_v004b/experiments/validation_selection.json`
- Final model/data/CSV manifest: `outputs/sequence_v004b/final_all/final_manifest.json`
- Local verification: `outputs/sequence_v004b/final_local_verification.json`
- Complete local backup: `outputs/sequence_v004b/sequence-v004b-completed.tar.gz`
- Model and review logs: `/home/v2gao/dsc102/pa3/setup/sequence-v004b-*.log`
- Methods, results and remaining errors: `INVESTIGATION_v004.md`

The same notebook/CSV paths exist under the local project. Persistent home files
survive pod expiry, and the complete verified backup is already on the Mac.

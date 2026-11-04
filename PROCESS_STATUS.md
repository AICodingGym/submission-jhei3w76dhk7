# Process map

Checked **November 4, 2026, 9:22 AM Pacific**. All approved experiments finished.

| Process | Status | Result |
|---|---|---|
| v005 final all-data ensemble | Accepted | **Official MAE .18550**; both members trained freshly on 67,905 breaths |
| Earlier interim ensemble | Preserved | Official MAE .19486 |
| H1: 200+100 epochs | Complete | Individual A .213908; fixed pair .196437; negligible gain |
| H1: slower 300-epoch cosine | Complete | Individual A .206321; fixed pair .193145; qualified for confirmation |
| H2: R/C-specific output heads | Complete | Individual A .224617; fixed pair .201662; worse |
| Fresh grouped C confirmation | Complete | Slower pair .208748 vs reference .210612; improvement interval crosses zero, so not confirmed |
| v006 additional all-data fit / submission | Correctly skipped | Frozen confirmation rule did not pass; no runner-up or weight search |
| Artifact verification | Complete | Hash-verified local/server backups; independent C metrics, bootstrap and CPU inference passed |

Best submission:
`outputs/improvements_v005/confirmation_round1/final_all/submission.csv`

Official receipt: `research/submission_receipt_v005_final.json`.

Review the work in `results_review_v005.ipynb`, `approved_pilots_v006.ipynb`,
and `confirmation_final_v006.ipynb`. Full configurations, seeds, timings and
predictions are preserved under `outputs/approved_pilots_v006/`.

The grouped C difference was -.001864 with a 95% whole-breath interval
[-.004325, +.000630]. Its lower average error is promising but insufficient
under the rule committed before results. No new official score was used to tune
this decision. C is resampling confirmation; final all-data models have no
independent holdout. H3/H4 were neither authorized nor started. The .10 target
has not been reached.

Persistent DataHub project:
`/home/v2gao/dsc102/pa3/gym-workspace/ventilator-pressure-prediction`.
Course pod `v2gao-1042868` was released after verified evidence sync at about
9:22 AM Pacific. Kubernetes reports no remaining pods; no training is running.
Persistent files survive pod deletion; all completed results are also on the Mac.

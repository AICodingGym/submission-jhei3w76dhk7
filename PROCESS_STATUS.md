# Process map

Checked **November 4, 2026, 8:24 AM Pacific**.

| Process | Status | Result / next step |
|---|---|---|
| Accepted interim submission | Complete | Official MAE **0.19486**; retained |
| v005 A comparisons | Complete | Frozen equal LSTM pair MAE **0.196563** |
| v005 grouped C confirmation | Complete | Same pair **0.210612**; beats individual .231627 and reference .514886 |
| v005 all-data final fits | Complete | Two fresh models fitted on all **67,905** approved breaths; 193 / 189 epochs |
| v005 final submission | Accepted | **Official MAE .18550**, 4.8% lower than interim .19486; exact rows/IDs/model hashes and independent inference verified |
| H1: extend original compact LSTM by 100 epochs | Complete | Individual A MAE **.213908**, best epoch 294; small change from .214166 |
| H1: fresh 300-epoch slower cosine | Complete | Individual A MAE **.206321**, best epoch 285; fixed-pair comparison pending retrieval |
| H2: R/C-specific output heads | Started | Last result pending login renewal; same 200-epoch schedule, head change only |
| Additional grouped confirmation | Conditional | Only promising approved pilots; no C weight tuning |

Current course pod: `v2gao-1042868` on `its-dsmlp-n05.ucsd.edu`,
GTX 1080 Ti. Started about **6:25 AM Pacific**; expected six-hour expiry about
**12:25 PM**. Password/Duo renewal is now required to retrieve the last pilot result.
The reconnection command has been requested; server-side work continues.

The prior pod expired at 2:02 AM. Its final fits and CSV completed beforehand.
The pilot's split check rejected an identical split because it compared two
hash formats. It stopped before any assignment-data pilot fitting. The source
and failure log are preserved. The corrected check, original checkpoint
fingerprint and 840 exact CUDA continuation checks passed before restart.

Work is stored in persistent DataHub home and backed up locally:
`/home/v2gao/dsc102/pa3/gym-workspace/ventilator-pressure-prediction`.

- Completed final notebook: `confirmation_final_v005.ipynb`
- Final CSV: `outputs/improvements_v005/confirmation_round1/final_all/submission.csv`
- Approved experiments: `approved_pilots_v006.ipynb`
- Pilot log: `/home/v2gao/dsc102/pa3/setup/v006-pilot-execution.log`
- Pilot results: `outputs/approved_pilots_v006/`
- Accepted interim receipt: `research/submission_receipt_v005_interim.json`

C is resampling confirmation, not a pristine untouched test set. Validation
scores belong to earlier validation fits; final all-data models have no
independent holdout. No H3/H4 experiments are authorized or running.

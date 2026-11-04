# Process map

Checked **November 4, 2026, 3:12 PM Pacific**. V007 screen is partially complete.
Best accepted official MAE **.18550** remains unchanged.

| Candidate on identical held-out A breaths | Ensemble A MAE | Status |
|---|---:|---|
| Original compact/deep equal pair | .196563 | Verified baseline |
| Full residual correction | .195584 | Small .000979 gain; below frozen .003 threshold |
| Half residual correction | .195912 | Small .000650 gain; below threshold |
| Pressure-level probability model | .204355 | Worse under this recipe |
| Deep LSTM AdamW1e-4 | .198516 | No demonstrated improvement |
| Deep LSTM dropout.25 | Pending | Still running original200-epoch budget |

Independent local audit: **169 checks passed, zero failures**. Exact A row IDs,
OOF complement exclusions and aggregate predictions, saved checkpoint/report
hashes, label fingerprints, training-only pressure codebook and native MAE /
median / p90 / whole-breath bootstrap scores checked. Residual pickle verified
by SHA without unpickling. See `research/screen_review_v007.json`.

Residual full-strength difference vs baseline: -.000979, bootstrap 95% interval
[-.001319,-.000645]. This is a small consistent A gain, not a confirmed promotion.
Median absolute point error .100364 vs baseline .100946. The .10 target is not
achieved. No new candidate has been selected for grouped confirmation or submitted.

Review: `results_review_v007.ipynb`; experiment source: `approved_experiments_v007.ipynb`.
Current pod `v2gao-1273870` expires about 3:37 PM Pacific. The guarded coordinator
can officially queue one replacement and resume saved model/optimizer/RNG state.
Last snapshot 3:03 PM: dropout 41/200, approximately40.7 sec/epoch. Remaining time
then about108 GPU minutes, excluding scheduling delay. All earlier stages complete.

The user renewed SSH/Duo for this review. Server jobs remain detached from the Mac.
Partial archive 53 files SHA599bb0832683b22e8b0892237b42e6df84c5f2ad41f8cab2a62f57ffa8c33f79;
OOF supplement 2 files SHAcfb4b702057800f6bcb3aa0333b861e3edd70aa414c63813e9437a254d61e9fa.
Both downloaded and per-file hashes verified, with prior versions preserved.

Only approved ideas 1, 3, 5 run; no unapproved model family or data source added.
Do not change the screening threshold or rank an unfinished dropout trial as final.

Live check at 3:12 PM: dropout 54/200, approximately 99 remaining GPU minutes,
plus any replacement scheduling delay. The original 200-epoch budget is unchanged.

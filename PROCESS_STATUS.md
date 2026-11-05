# Process map

Checked **November 4, 2026, 10:00 PM Pacific**. All approved v007 tests finished.
Best accepted official MAE remains **0.18550**. No training is running.

| Fixed equal-pair candidate on the same A validation breaths | A MAE | Result |
|---|---:|---|
| Original compact/deep ensemble | .196563 | Verified baseline |
| Full residual correction | .195584 | .000979 gain, below frozen .003 threshold |
| Half residual correction | .195912 | .000650 gain, below threshold |
| Pressure-level probabilities | .204355 | Worse under this recipe |
| Deep LSTM AdamW 1e-4 | .198516 | No demonstrated improvement |
| Deep LSTM dropout .25 | .201479 | Worse under this recipe |

**199 independent checks passed**, zero missing artifacts. OOF exclusions,
row alignment, codebook, label fingerprints and file hashes verified. Dropout
input fingerprints and every preprocessing field exactly match the original
deep A model. Independent CPU inference on 16 validation breaths agreed with
saved CUDA predictions within 1.15e-5 native pressure units.

The full correction's MAE difference interval is [-.001319,-.000645]. Its A gain
is consistent but only .50%, below the predeclared minimum. Median absolute
point error is .100364 versus baseline .100946. The .10 target is not reached.

No candidate qualified for grouped confirmation. No extra all-data fit, threshold
change, runner-up search or new submission occurred. Accepted .18550 retained.

Review: `results_review_v007.ipynb`; source: `approved_experiments_v007.ipynb`.
Audit: `research/screen_review_v007.json`; decision: `research/decision_v007.json`.
Best CSV: `outputs/improvements_v005/confirmation_round1/final_all/submission.csv`.
Receipt: `research/submission_receipt_v005_final.json`.

Original pod expired 3:37 PM. One official replacement waited about five hours,
then started 8:36 PM and resumed at epoch 92. Dropout finished 200 epochs, selecting
194. Coordinator verified an 81-file archive and released GPU about 9:54 PM.
The 280,134,657-byte archive was downloaded and per-file hashes checked on Mac:
SHA256 `059ceb600a94b20d42b64be8ab46c7c8748bfd5b293f699b4f472afdbf4504a1`.

Prior files and changed snapshots were preserved. Persistent course files survive
pod deletion. Only assignment-approved data and approved ideas 1, 3, 5 were used.

# Process map

Checked **November 4, 2026, 9:55 AM Pacific**. User approved new ideas 1, 3 and 5.
Accepted official MAE **.18550** is preserved.

| Approved v007 process | Status | Design |
|---|---|---|
| Course GPU and library checks | Passed | GTX 1080 Ti, Torch2.2.1/CUDA12.1, LightGBM4.6 |
| Course synthetic proofs | Passed | Exact pressure/AdamW recovery, real LightGBM save/load, production-shape memory profile |
| OOF base predictions for correction | Running | Three fresh compact BiLSTM fits, 193 frozen epochs; each excludes its prediction fold and original A validation |
| Residual correction | Queued after OOF | Fixed small MAE LightGBM, shrinkage0/.5/1; correct compact member, retain deep partner |
| Pressure-level probabilities | Queued | Compact BiLSTM, training-only codebook, masked categorical CE and posterior median; same200 rates/batch256 |
| Regularization | Queued | Deep BiLSTM, separate AdamW1e-4 and dropout.25, same200 rates and seed |
| Confirmation / final promotion | Pending A results | Best qualifying candidate only, fresh grouped resampling; no official-score tuning |

Main notebook: `approved_experiments_v007.ipynb`.
Component definitions/checks: `research/*_components_v007.ipynb` and matching
`*_checks_v007.json`. Approval/protocol: `research/authorization_v007.json`.
Artifacts: `outputs/approved_experiments_v007/`.

Current pod `v2gao-1273870`, node `its-dsmlp-n06.ucsd.edu`, started9:37:29 AM
Pacific; expected scheduled expiry3:37:29 PM. Screen estimate6–8 GPU hours.
Per-epoch model/optimizer/RNG state permits recovery. A bounded coordinator (login PID1279505) is
active for at most one official replacement after natural expiry;
application errors stop automatic restart. Screen completion will be archived
and the idle GPU released before later confirmation review.

Course checks caught an unavailable deterministic CUDA cumulative-sum operation
in Torch2.2.1, before any approved-data fitting. The old source/log is preserved.
Median decoding now uses deterministic CPU cumulative sums after GPU softmax;
CE/backprop and recipes are unchanged. Fresh CPU and actual CUDA checks passed.

Previous v006: longer training negligible; slower cosine did not pass frozen C
confirmation; R/C output heads worsened. No v006 candidate was promoted.
Best CSV: `outputs/improvements_v005/confirmation_round1/final_all/submission.csv`.
Receipt: `research/submission_receipt_v005_final.json`.

Only assignment-approved data is used. Original A validation breaths stay held
out of every new A-screen fitter. Future grouped confirmation is resampling,
not a pristine untouched test. The .10 target is not yet achieved.

# V011 verified results

Updated November 6, 2026, morning Pacific. Final fitting, verification and official submission are complete. **New official Gym MAE: 0.18025**, improving on 0.18550 by 0.00525 (2.83%). Receipt: `research/submission_receipt_v011_final.json`.

| Evaluation | Previous pair mean MAE | Frozen five-member mean MAE | Relative improvement |
| --- | ---: | ---: | ---: |
| Original grouped A validation | 0.196562610 | 0.190851029 | 2.91% |
| Fresh grouped D confirmation | 0.203508566 | 0.196962270 | 3.22% |

The D comparison cold-fitted all five members on 54,323 training breaths and evaluated 6,791 separate breaths (206,305 inspiratory points). Original A-validation breaths were excluded. An independent saved-artifact audit passed 211 checks. A whole-breath bootstrap gave a 95% interval of [-0.008010083, -0.004893598] for candidate minus reference MAE. The improvement repeated on the second grouped split; this is resampling evidence, not an untouched test after repeated research on A.

The frozen blend is deep BiLSTM 0.5, with original compact, curve-consistency, learned-memory, and shared-offset members 0.125 each. Its additional models help in different situations: one checks the shape of the pressure curve, one learns how earlier controls affect later responses, and one estimates a shared pressure adjustment across a breath. Averaging their different errors improved the overall score. Weights and training budgets were frozen before D outcomes.

Median point absolute error was 0.098163784 on A and 0.100096941 on D. These describe typical errors; they are not official mean MAE scores and do not establish a 0.10 mean MAE result.

The best official Gym MAE is now **0.18025**. The previous **0.18550** result, CSV and checkpoints remain preserved, with its original receipt at `research/submission_receipt_v005_final.json`. Validation and official test scores use different breaths; compare old versus new within the same evaluation.

Final all-approved fitting used 67,905 labeled breaths. Curve completed 193 epochs in 38.85 minutes, memory 191 in 47.92 minutes, and offset 193 in 41.90 minutes. Accepted all-data compact/deep checkpoints were verified for reuse. The pipeline finished November 5 at 10:58 PM Pacific, and its guardian verified the archive before releasing the idle GPU. No pods remain. Final refitting has no independent holdout.

The 129-file archive (180,449,172 bytes) passed every per-file hash and safe-member check. Its SHA256 is `3415bb3005a9dcd4f1c7df45791efc3b5b0039ea6c96253b19306ed64a939ff6`. An independent final audit passed 146 checks, including approved data/checkpoint/source hashes, all-training counts, frozen epoch/LR budgets, preprocessing equality, exact native weighted predictions and CSV alignment. See `research/final_review_v011.json`. The final CSV contains 603,600 rows; SHA256 `c344a485f5ef1290aadf5dfd379333009efab674b7ccdff6f361e225a4b8b77a`.

One genuine operational error was corrected before final fitting: the verifier compared a legacy canonical JSON lock digest with a raw file digest. The corrected verifier checks the original canonical convention and rejects changed content. Previous sources/logs were retained. Model recipes, D evidence, and frozen weights were unchanged.

The verified CSV was submitted using the existing authorization. Gym returned 0.18025 and reported that source was pushed to the competition branch. The CLI log is `outputs/confirmation_v011/final_all/submission_cli.log`; the new receipt records CSV/model-manifest/log hashes and validation evidence. All previous artifacts remain preserved. No training or queued GPU jobs remain. Mean MAE 0.10 has not been achieved.

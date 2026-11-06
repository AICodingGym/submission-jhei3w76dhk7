# V011 verified results

Updated November 6, 2026, 6:27 AM Pacific. Final server artifacts are awaiting a renewed password/Duo connection; completion and a new official score are not yet verified.

| Evaluation | Previous pair mean MAE | Frozen five-member mean MAE | Relative improvement |
| --- | ---: | ---: | ---: |
| Original grouped A validation | 0.196562610 | 0.190851029 | 2.91% |
| Fresh grouped D confirmation | 0.203508566 | 0.196962270 | 3.22% |

The D comparison cold-fitted all five members on 54,323 training breaths and evaluated 6,791 separate breaths (206,305 inspiratory points). Original A-validation breaths were excluded. An independent saved-artifact audit passed 211 checks. A whole-breath bootstrap gave a 95% interval of [-0.008010083, -0.004893598] for candidate minus reference MAE. The improvement repeated on the second grouped split; this is resampling evidence, not an untouched test after repeated research on A.

The frozen blend is deep BiLSTM 0.5, with original compact, curve-consistency, learned-memory, and shared-offset members 0.125 each. Its additional models help in different situations: one checks the shape of the pressure curve, one learns how earlier controls affect later responses, and one estimates a shared pressure adjustment across a breath. Averaging their different errors improved the overall score. Weights and training budgets were frozen before D outcomes.

Median point absolute error was 0.098163784 on A and 0.100096941 on D. These describe typical errors; they are not official mean MAE scores and do not establish a 0.10 mean MAE result.

The best accepted official Gym MAE remains **0.18550**, preserved in `research/submission_receipt_v005_final.json`. Validation and official test scores use different breaths and cannot be directly compared as evidence of improvement.

Final all-approved fitting uses 67,905 labeled breaths. The last verified live observation on November 5 had curve complete (193 epochs), memory complete (191 epochs), and offset at 16/193 epochs. Accepted all-data compact/deep checkpoints were verified for reuse. No final-stage completion, new CSV, or new official submission has been retrieved locally yet. The server pipeline runs independently of the Mac and should archive results before releasing its idle GPU; actual state must be checked after login.

One genuine operational error was corrected before final fitting: the verifier compared a legacy canonical JSON lock digest with a raw file digest. The corrected verifier checks the original canonical convention and rejects changed content. Previous sources/logs were retained. Model recipes, D evidence, and frozen weights were unchanged.

Next: renew DataHub access, retrieve and verify the archive, audit all-data training provenance and exact test/sample CSV alignment, then submit the validated CSV using the existing authorization. Preserve the 0.18550 artifact regardless of the new score.

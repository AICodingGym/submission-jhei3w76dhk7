# V019 results: no candidate qualifies

Both200epoch fits completed successfully. Independent98check audit passed. No new grouped confirmation, all-data fit or submission is justified by this batch. Best official Gym mean MAE remains **0.17427**; target<=0.15 remains unmet.

The original deep curve-loss model has individual A MAE0.203829545. The new separate auxiliary head gives0.206665552; six raw/time/R-C inputs give0.229696833. On the same A split, current fixed ensemble MAE0.182922095 compares with0.183622392(auxiliary replacement),0.186816549(minimal-input replacement) and0.182637267(two new members). The last gain0.000284828 is below the frozen0.003 threshold and its interval crosses zero. None qualifies.

Training-diagnostic MAE at the best checkpoint is about0.0903 for the original model,0.0918 for the auxiliary model and0.1352 for the minimal-input model. These use the fixed training diagnostic sample, not the entire training population. The train/validation gaps support testing generalization changes; the simpler-input model's worse training result also suggests lost information or optimization difficulty. These are diagnoses, not proofs of a specific cause.

Following the user's ranked-winner priority, the next proposed comparisons are separate one-hot R/C representation inspired by first place and restricted mixup inspired by third place. Keep them separate, train only on fit breaths, and validate on unchanged whole breaths. No new recipe is frozen or trained yet. Do not change V019 weights or submit a runner-up after its gate failed.

Training finished4:37AMPacificNov7. A server-side kubectl backup transfer ended with unexpected EOF near the end. The idle GPU pod later reached its ordinary six-hour deadline. The original180006932byte70file archive remained intact on persistent course storage, SHA f823e55f72c932c084bf11ff90841d08773d7c72b6d74cb3b85b39ea35a908f2. A minimal CPU-only pod recovered it; allfiles verified remotely and locally. No retraining was performed. Both old and recovery pods were released. The partial archive and failure logs remain preserved on DataHub.

Evidence: screen_review_v019.json, protocol_v019.json, completed_archive and results_review_v019.ipynb.

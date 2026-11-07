# V014 and V017 confirmation results

Best accepted official Gym mean MAE remains **0.18025**. No new submission yet.
The target of official mean MAE<=0.15 remains active. The user reported first-place MAE around0.057; this is user-provided context, not an independently verified comparable result.

| Fixed approach | Original A validation | Cold E confirmation |
|---|---:|---:|
| Accepted five-model baseline |0.190851029|0.202909053|
| Six-model mean, adding deep curve loss |0.186264237|0.197605952|
| Fixed weighted median + training pressure levels |0.182922095|0.194792297|

Both confirmations passed their predeclared gates. The six-model mean improves E mean MAE by0.005303101; its whole-breath95% candidate-minus-baseline interval is[-0.006643053,-0.004067906].
The output rule further improves E mean MAE by0.002813655; its interval is[-0.004246089,-0.001454048]. Its total improvement against the five-model baseline is0.008116756, about4.00%.

All six E members trained cold on54323breaths, excluding6791E-validation breaths and the original6791A-validation breaths. Fixed seed20261102; E grouped RC-stratified seed20261203. Original A-selected epochs and learning-rate prefixes were replayed without E feedback. Sources, data, checkpoints, row IDs, native scores, independently rebuilt features/train-only statistics and bootstrap were independently audited: primary173checks; secondary16checks. E is grouped resampling evidence, not the official hidden-test score.

The secondary rule was preregistered6:25:08PM and source frozen6:26:52PM Pacific, before the last cold fit began7:14:01PM and before E scoring completed9:07PM. Its pressure grid uses only E-fit inspiratory labels. No weights, thresholds, epochs or alternate output rules were selected on E outcomes.

The primary run took5.916hours. Its72-file175471112-byte archive has SHA2563a0f60fbe3d36dd1c8bfc3a0668f9d7ba6ea13df04db4eccb6ddebf7d6c52d81. Every archive member was checked locally and on DataHub before the old GPU was released. Original root notebooks are preserved; executed server versions remain in the archive mirror.

The final notebook `final_fit_v018.ipynb` uses all67905approved labeled breaths. Five accepted all-data models/caches may be reused only after exact data/recipe/seed/budget/source/model/preprocessing/row checks. Only deep_curve requires a new196epoch fixed fit. Fit the final pressure grid on all approved training inspiration. Apply the same weighted-median/grid rule on test inspiration and fixed mean on unscored rows; preserve all603600sample IDs. This final fit has no independent holdout. Final CSV must be independently checked before the authorized Gym submission. The previous0.18025CSV is preserved.

Evidence: `research/confirmation_review_v014.json`, `research/postprocessing_confirmation_review_v017.json`, output result files and `results_review_v014.ipynb`. Discussion-inspired provenance stays in `research/DISCUSSION_INSPIRED_ROADMAP_v015.md`.

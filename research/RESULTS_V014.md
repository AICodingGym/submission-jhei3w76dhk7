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

## Final V018 artifact verification

**November6,11:45PM Pacific: V018 final fit COMPLETE and independent145-check audit passed.** All67905breaths; onlynewdeep_curve trained196epochs,~2h23m; fiveacceptedall-data weights/cache reused afterexactchecks. CSV603600rows SHA274668c4dc14e9d20a554c738859fca37e448836797d7260ec7b11464dcde3e2 at `outputs/confirmation_v014/final_all_v018/submission.csv`; manifestSHA2a53c1b7b38dee05f6db7f809dc80bb765fc73d3e1d6f157e92e5141054f2e23. NewdeepcurvemodelSHA5c022e57a713e94f9480dab61743517e446990594ccbb7723033d7d78d1adfc3. Fixedweightedmedian+training-onlygridonknowninspiration, fixedmeanunscoredrows. Rebuiltallrawfeatures/trainonlystats, sixfullrecipes/budgets/source/data/model hashes, sixinferencecacheprovenance, independentoutputmath andexactCSVroundtrip passed. Audit `research/final_review_v018.json`. Noofficialnewscoreyet; submitnext. Old0.18025and0.18550CSVs unchanged.

Verified50-file69091854B archive SHA3f50617e28da8b2301818fd4158ace929c75fc4a451e5bce1ca2ac672ba5fc6b underfinal_all_v018/completed_archive; mirrorpreservedrootnotebooks; pod4079254releasedafterverifiedbackup. NoGPUjobsremain. V019nextscreenpayloadpreparedbutNOTrun; onlydispatchafterV018submission ifgoalunmet; keepfrozenhypotheses unchanged.


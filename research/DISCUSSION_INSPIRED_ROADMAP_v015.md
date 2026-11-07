# Discussion-informed research toward official mean MAE <=0.15

User supplied `../kagglediscussion.md` on November6 and explicitly requested reading it for inspiration. Reviewed its substantive synthesis, qualifications, source map and topic index. It reports partial primary-topic coverage, not all forum bodies. SHA256 `195e535ce76460231654b2faeb5805d49b52f7fb2b679f545e0813c091484288` (90,740 bytes). Original file is unchanged; a copy is preserved under `outputs/controller_feasibility_v015/user_source/`.

The supplied document flags a course prohibition on existing solutions. The user's later request authorizes consulting this supplied synthesis within this session; that is not instructor permission or evidence of assignment-rule compliance. Record any resulting work as discussion-inspired. The current V014 recipe was frozen and dispatched before this file was supplied and remains unchanged. No original Kaggle data, pretrained solution or solution-code repository is being downloaded.

Historical author-reported public/private scores do not predict a Gym score. Goal completion requires an actual official mean MAE <=0.15. Median error does not satisfy the goal.

## Priority and distinctions from completed work

| Priority | Candidate | New contribution and necessary control |
| --- | --- | --- |
| 1 | Separate pressure-difference auxiliary output | Current curve L1 penalizes differences of the pressure output itself. A separate head trained on pressure differences is a distinct multi-task design. Keep the same backbone, features, grouped split and pressure metric; compare first differences before adding second differences. Pressure differences are training targets, never inference inputs. Supplied synthesis S03/S06/S11/S13. |
| 2 | Restricted training mixup | Blend training inputs and pressure targets using only training breaths with matching R/C and compatible valve-phase masks. Preserve complete breath alignment. Validation remains original, unaugmented breaths. This is a regularization hypothesis; interpolated features need not represent an exact physical breath. S03 motivates it. |
| 3 | Laplace likelihood | Predict pressure and a positive scale; optimize absolute error divided by scale plus log-scale penalty. Keep official inspiration-only native MAE for selection. Check scale positivity, finite gradients and degeneration; learned downweighting could hurt high-error groups, so inspect total error contribution. This has not been tested by our earlier scalar L1/Huber or pressure-classification experiments. S07. |
| 4 | Minimal-input deep model | Compare a small raw-control/time/R-C representation with the current47 features while holding the deep architecture and objective fixed. Prior feature ablations used a smaller model; their ranking need not transfer to the deep model. Test one-hot R/C separately from feature removal. S01/S06/S08. |
| 5 | Training-neighbor context | Retrieve similar control traces within lung setting using known inputs only; supply labeled training-neighbor information. Validation/query pools must exclude their own labels; training self-matches must be excluded. Preprocessing and any neighbor embedding fit only on fit breaths. Start with a cheap training-only feasibility diagnostic before a neural run. S06/S38. |
| Lower | Quantization and robust ensemble aggregation | Potentially small refinements, not evidence of a large score gain. Fit pressure grid/calibration using training data only. Median model prediction is different from median absolute error and need not minimize mean MAE. Predeclare any candidate instead of broad weight/threshold searches. S18/S24/S26. |
| Later | Pseudo-labeling | Any teacher used for validation research must exclude those validation breaths. Accepted all-data final models cannot serve as leakage-free teachers for A/E evaluation. No extra datasets; only approved known inputs. Current evidence favors testing other mechanisms first. |

Lag/delta/integral features, R/C at each step, training-only scaling, inspiration masking, native mean MAE, best-checkpoint selection, grouped splits, bidirectional LSTM and all-approved final fitting are already implemented. Do not relabel them as new changes. Full TCN, attention, pressure CE, stronger dropout and AdamW recipes have documented negative results; new variants need a distinct hypothesis. Longer compact training did not confirm on another split.

## Cheap controller falsification check already completed

Notebook `research/controller_feasibility_v015.ipynb`; frozen plan `research/controller_feasibility_protocol_v015.json`, SHA `4797698d79be753b1de3099f5623225d2f3b112d27b636e4664d5cf2ea6df555`. Sampled64 original-A-fit breaths per R/C group,576total, seed20261501. CSV pressure was parsed only for selected training breaths; original A-validation/E-validation were excluded. Raw float64 precision retained. No GPU work, pressure predictor, validation score or submission was produced.

Tested independently derived proportional and non-decaying PI equations with linear desired-pressure trajectories, contemporaneous/one-step-lagged pressure. Coefficients fit the first70% of eligible inspired rows; residuals use later rows of the same training breath and their known pressures. These are valve-control consistency diagnostics, not unseen-pressure prediction.

| Equation | Eligible breaths | Median later-row absolute control residual | Near-exact fraction of576 |
| --- | ---: | ---: | ---: |
| PI current |492|.185052|.022569|
| PI lag1 |492|.942009|.005208|
| P current |552|1.455323|.031250|
| P lag1 |552|2.432545|.005208|

No equation reached the frozen10% near-exact gate (positive Kp, condition<1e10, later-row median control residual<1e-4). This rejects promotion of this simple family as an immediate reconstruction route. It does not establish that all controller inversion is impossible: integral decay, piecewise reference shape, clipping and perturbations were not modeled. Avoid spending hours on that branch before comparing other new methods.

## Execution sequence

Finish and independently audit the already frozen V014 E confirmation first. If it passes, preserve its recipe and produce the conditional all-approved final fit/submission. Do not tune against official test scores. Freeze the next bounded GPU batch from the new mechanisms above, with meaningful pilot budgets and exact resume/source checks. Promote only through grouped validation and confirmation. Preserve configs, seeds, runtimes, scores, failures and hashes, including this supplied-source provenance.

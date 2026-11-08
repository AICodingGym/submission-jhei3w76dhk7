# V034: physics-based controller selection did not qualify

Both prospectively declared alternatives failed the unchanged original-A promotion rule. Accepted baseline A mean MAE was0.182922094565.

| Candidate | Native inspiration mean MAE | Gain | 95% whole-breath delta interval | Eligible |
|---|---:|---:|---|---|
| Physics match, one-level cap |0.182667625887|0.000254468678|[-0.000435497423,-0.000072292420]|No: gain below0.003|
| Same controllers, full grid projection |0.222252449469|-0.039330354904|[0.031510114879,0.048656246983]|No|

Selected=null. No F split/fits, final fit or submission. Official0.17427 remains preserved; <=0.15 unmet. Median absolute error remained0.070302963257 for both and is not the mean objective.

The new inference method ranked audited Afit controller coefficients by their one-step pressure-equation residual against baseline MODEL PREDICTIONS and known controls. Query pressure and IDs were absent. Both variants used the same five selected controllers, four parallel anchored passes, training-only input-distance confidence and controller-consensus gate. The only cap difference was predeclared. Both candidate arrays were saved and hash-locked before labels were read for scoring. All21,136 controllers and input statistics came from originalAfit only.

Of6,791 validation breaths,3,170 had adequate input support and at least14 eligible equations;25,421 points passed the full gate.18,058 points changed. With the cap,9,402 improved and8,656 worsened. Removing the cap worsened10,299 points and improved7,350, with larger harmful moves. A small pressure-equation residual is not reliable evidence of accurate absolute pressure: selecting parameters can preserve baseline bias or introduce a different compatible pressure. We close this bounded controller-bank branch rather than tune caps/thresholds/weights after seeing results. This is a negative scientific result, not proof that every physical model is unusable.

Runtime37.4561 CPU seconds, no GPU/gradient fit/checkpoint inference. Independent audit626checks passed: all input/artifact/source hashes, exact bank reuse, every query parameter selection and support gate, independent direct-equation oracle(max difference8.53e-14), recurrence/cap/grid/native scores/whole-breath intervals and selection. Audit prepared before outcomes; no audit correction required. Sources froze git922e40c. Component code SHA c51a51a7533085aa1f7923f7c53a5e1eabad352ad9e497cba153f297ff82c6cb; protocol SHA9798ac9cb3c509a6918e5952d855c9348e15f523e6e258c7e74ead59e216637e; summary SHAe2998a0a20bf25b950639507faf572eb81dd187799580824583df633518cd94f. Executed notebook research/controller_selection_screen_v034.ipynb; audit research/controller_selection_review_v034.json. Outputs under outputs/controller_selection_screen_v034 and _review.

Next test one larger recurrent architecture under the same Laplace objective and fixed200rate schedule. Synthetic full-model optimizer/RNG resume, actual-CUDA pruning/model proofs and measured lease/memory gate precede any approved-data fit. More capacity may overfit; it is a hypothesis, not a diagnosis that the current model is underfit.

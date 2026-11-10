# V036 cold confirmation: passed

The selected capacity ensemble reproduced its improvement after all seven models were trained from scratch on the frozen F split. Native inspiration-only mean MAE fell from **0.1952774874 to0.1893106255**, a gain of0.0059668619 (**3.06%**). The paired whole-breath, point-weighted1000-draw95% interval for candidate minus baseline was **[-0.0078116368,-0.0041472571]**. The frozen gate passed. Independent reconstruction and cached-inference checks passed **1516checks**.

The reference and candidate use the same five other models and fixed weighted-median-midpoint followed by nearest Ffit pressure grid. The reference assigns0.25to the older deep-curve member; the candidate assigns that0.25to the larger Laplace+curve capacity model. Other weights are deep0.25 and compact/curve/memory/offset0.125each. There was no F-based epoch, weight, grid-policy or runner-up search.

F used54323fit/6791validation breaths from the original61114 Afit, stratified by R/C with seed20261204; original6791 Avalidation breaths were excluded. All seven Fmodels were cold-fitted, with their own training-only statistics, at the predeclared budgets. This is resampling confirmation after A-based research, not a pristine untouched test. The candidate Fscore should be compared with its Fbaseline, not directly ranked against official0.17427 or A0.177529.

| Evidence | Reference MAE | Candidate MAE |
|---|---:|---:|
| Original grouped A |0.1829220946|0.1775294806|
| Cold grouped F |0.1952774874|0.1893106255|
| Accepted official submission |0.17427|Pending final fitting/submission|

The Fmedian absolute error was0.0703029633 for both candidates; the90th percentile was0.4218130112 for both. Those diagnostic quantiles are separate from the official mean-MAE metric and the updated course historical-median score target **<=0.1638**. The primary target remains unmet until an accepted official score verifies it.

The successful run finished Nov9,10:12:12PM Pacific, while its automatic backup exhausted private-home quota. All model outputs stayed in persistent course storage. A verified byte-identical1,056,127,127-byte failed copy was replaced with a hardlink to the existing canonical archive, preserving its original path and bytes and restoring writes. The partial original archive was preserved. A CPU-only recovery pod created a178,115,769-byte/41-member incremental archive (SHAf443ca648905f54eed3fe488d885a67141b676eeec538f1130f8cdf4ebb654f1), referencing the already verified first-stage archive. All41 new members and240 unchanged base members were checked; only the append-only events log was updated, with its prior bytes preserved. No training was repeated. Source/data/model hashes, failed attempts and visible interaction history remain preserved.

Next: the already frozen conditional V037 consumer passed its actual F-prerequisite gate. After actual CUDA checks, fit only the new capacity member for190epochs on all67905approved breaths; reuse the five accepted all-data checkpoints/caches only after strict identity checks. Final fitting has no independent holdout. Audit the603600-ID-aligned finite CSV and submit through Gym; preserve accepted0.17427 if the new official result is worse. No final model or new submission existed when this report was written.

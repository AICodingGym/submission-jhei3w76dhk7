# V030: fixed cross-objective mixture rejected

One prospectively frozen nine-model mixture scored **0.18031191805490263 native inspiratory A MAE**, gain **0.00261017650983264** versus0.18292209456473527. Its whole-breath95% delta interval was [-0.0036773440084585233,-0.001474185407139394]. It missed the unchanged0.003 practical gain gate and is **ineligible**. It also performed slightly worse than the V029 retained-curve mixture0.18018912. Stop this saved-weight branch; no alternatives or threshold changes.

Only the olddeep_curve0.25 slot changed: plain curve, span3, span7 and Laplace each0.0625. Compact/curve/memory/offset each0.125 and deep0.25 remained fixed. Output used unchanged median midpoint + nearest fit-only pressure grid. Predicted uncertainty never affected weights. No GPU, training, neural inference or test data. Runtime1.592CPU seconds. Median point error0.07030296325683594 is separate from the mean selection metric.

Recipe/source frozen before calculation in gitd6f5351. ProtocolSHA36d8532a3b4a834177e2525829f419f1242cab4e37434a543733d3e2bb28eb60; codeSHA1a6275ff59a37123cd7535d933bf0879f40ab6dc6e1b627059cace29e79e700f. Independent audit **112checks** passed, including transitive V024/V029 model/source/row audits, rebuilt206098 originalA targets and training-only grid, integer16 median reconstruction and multiplicity bootstrap (1000draws,seed20263001). research/mixture_review_v030.json and executed research/mixture_screen_v030.ipynb preserve evidence.

No F, final fit or submission follows. Official best0.17427 preserved, <=0.15 target unmet. Repeated A adaptation limits inferential claims; no historical result was retroactively promoted. The next proposed V031 architecture change is a new GPU test on the improved Laplace body, not another weight search.

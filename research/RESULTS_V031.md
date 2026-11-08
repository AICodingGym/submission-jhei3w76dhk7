# V031: protected short-window adapter did not improve the Laplace model

The single cold model completed all200 frozen epochs and scored **0.2044879204785193 native inspiratory A MAE**, versus **0.20013018541768796** for the corresponding V029 model. The best checkpoint was188. Both fixed ensembles also failed the unchanged promotion gate:

| Candidate | A MAE | Gain vs0.182922094565 | 95% whole-breath delta interval | Eligible |
|---|---:|---:|---|---|
| New model0.25 replacement |0.18178210256303234|0.001139992001702922|[-0.003035248544261608,0.0007141517762572072]|No|
| Original curve0.125 + new0.125 |0.1802699615929399|0.002652132971795368|[-0.0035929160677364153,-0.001798354998419506]|No|

Selected=null. No F confirmation, final fit or submission follows. The best official mean MAE remains **0.17427**, and <=0.15 remains unmet. Do not loosen the0.003 practical-gain threshold or search extra weights after these outcomes. This rejects this bounded adapter/loss combination; it is not an implementation failure or proof against every hybrid architecture.

Only the protected, zero-initialized span3 frontend changed relative to V029. The original47 features, seed20261102,61114-fit/6791-validation breath-grouped split, full200 rate schedule, mean/scale heads, positive scale floor and Laplace-plus-curve loss remained fixed. Native inspiratory mean MAE selected checkpoints with the inherited1e-6 improvement tolerance. Targets never entered inference inputs. Runtime **8685.994s (2h24m46s)**; screen completed November8 **11:31:48AM Pacific**.

CPU147 and actual-CUDA32 pruning/152 model checks preceded fitting. The private V025 queue correctly kept a representative unfamiliar architecture/objective combination; no production pruning occurred. It never used training error, NLL or official scores for stopping. Independent **1039 checks** passed on completed outputs: source/data/model/objective/architecture/policy hashes, protected adapter rows, fit-only preprocessing, complete optimizer/rate/native-selection history, mean/scale caches, R/C-position error totals and independent median/grid/whole-breath bootstrap reconstruction.

Guardian archived and per-file verified **155 files/163247295bytes**, SHA6977682b2724231b9b0a2880154383506297fdd96a3dace800643731e42501b2, then released the GPU. Local transfer verification, safe mirror extraction and73 new-or-identical run-file publication passed; root source notebooks and old models were preserved. The archive/mirror is under outputs/controlled_experiments_v031/completed_archive. Audit research/screen_review_v031.json; code7e12e1a31db03dd9e8119537852baa0a4e951780bc64a6a6912bc7dbe8c84de7 was prepared before outcomes.

Root monitored about every10minutes and waited between checks. One status call exceeded the shell tool's initial wait and returned a running session with empty output; the monitoring wrapper's notification rejected that empty string. Polling the existing session recovered the correct epoch168 status. The watcher was amended to finish yielded read-only calls before notifying; remote training was unchanged. Observations remain under outputs/controlled_experiments_v031/monitor. This was an operational monitoring mistake, not a model or score error.

Frozen driver77815759c838b9e4b0c9b2f6d2c24de025b706e76aa7add8f60c97e42a660ac0 and protocol74fd95620b135dbd6256f7f3a120c9d6c651358eae89de67319c1b059e6a6b27 were committed before fitting. Next investigate the separately recorded CPU quantization/observation-order hypothesis; no new GPU has been requested.

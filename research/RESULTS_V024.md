# V024 hybrid results

Both 200-epoch fits completed. The independent audit passed **126 checks**. The batch does not advance to F confirmation, final fitting or submission.

| Fixed original-A comparison | Native inspiratory mean MAE | Gain versus reference |
|---|---:|---:|
| Existing ensemble | 0.182922095 | — |
| Short-window replacement | 0.182502187 | 0.000419908 |
| Wider-window replacement | 0.182967119 | -0.000045025 |
| Both hybrids | **0.181062361** | **0.001859734** |

The combined candidate's whole-breath95% interval for candidate minus reference is [-0.003404361,-0.000266644]. Its improvement is below the predeclared0.003 minimum, so selection remains null. No threshold or weight was changed after seeing these outcomes.

Individual short-window MAE0.203241290, best epoch194, runtime8639.9seconds. Wider-window MAE0.207317123, best199, runtime8747.7seconds. The unchanged curve-loss control scores0.203829545. The adapters produced complementary errors but have not met the promotion gate.

Executed analysis: [results_review_v024.ipynb](../results_review_v024.ipynb). Audit: `screen_review_v024.json`; summarySHA `e30f2db09f5ea89b2c06cf21fc9a75e5da760a472dc0a4b9a3e3d288efbdc2d9`.

The server finished around6:23PM Pacific November7 and verified its83-file188843666-byte archive before releasing the GPU. ArchiveSHA `36f77e054fe98911d6c278cb4ec6a4478b593dd70f92b7c1cac5bfef4d4d2d2a`. It is also downloaded and individually verified locally under `outputs/controlled_experiments_v024/completed_archive/`. Root source notebooks and earlier files were preserved. No jobs remain in the namespace.

A status answer initially used a stale checkpoint without first checking the current clock. It was corrected immediately, and actual completion was then verified. Details: `time_estimate_correction_v024.json`. This had no modeling impact.

Best official mean MAE remains **0.17427**, with older0.18025/0.18550 artifacts preserved. The ≤0.15 target remains unmet. The next workflow adds the user's requested conservative validation-only pruning.

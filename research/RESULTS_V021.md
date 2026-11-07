# V021 results

Both frozen 200-epoch training runs finished successfully. The independent audit passed **114 checks**. No candidate qualifies for grouped confirmation, final fitting or submission.

| Original grouped A comparison | Mean MAE | Gain versus current ensemble |
|---|---:|---:|
| Current fixed ensemble | 0.182922095 | — |
| One-hot replacement | 0.186604037 | -0.003681943 |
| Matched-mixup replacement | 0.189961929 | -0.007039834 |
| Both new members | 0.185261770 | -0.002339675 |

All three bootstrap intervals for candidate minus reference are positive. The frozen rule required a gain of at least 0.003 and a negative upper interval bound; selection is null.

The raw-input one-hot member scored 0.227689288 at epoch195 (8470.5 seconds), versus 0.229696833 for the earlier six-input numerical control. That small observed improvement did not overcome the loss from removing engineered features. The 47-feature curve-loss control scores 0.203829545. Matched whole-breath mixup scored 0.251416942 at epoch198 (8725.9 seconds). Its unaugmented training diagnostic and validation scores both exceed the old curve control. Extra bias or harder optimization are possible explanations, rather than demonstrated causes.

The executed analysis notebook [results_review_v021.ipynb](../results_review_v021.ipynb) includes learning curves, lung-group and position error contributions, and actual/predicted curves for three breaths selected by total reference absolute error. The R=50 groups contribute about 50.1% of the reference's total error. Difficult breaths often show coherent offsets; simply averaging these new members did not fix them.

The 78-file archive is verified locally by size, SHA256 and every individual member hash: 185,152,869 bytes, SHA256 `3465e546605d996a79fea3380c3074debe6f0d91ab737a22c6a1e76b8dac3d04`. It is preserved under `outputs/controlled_experiments_v021/completed_archive/`. Root source notebooks and older files were preserved. The guardian verified the backup and released pod v2gao-517608; no GPU jobs remain.

Audit: `research/screen_review_v021.json`. Summary SHA256: `a66e9056bd53d48e8c4c63e06227b157454ffa4d731d95346e7a1e8d6b9f9a15`. Before results were read, a prepared independent-audit seed typo was corrected to the unchanged frozen protocol; the original audit and six-check evidence are preserved in `research/audit_pre_execution_fix_v021.json`. Training and selection rules were unchanged.

Best official mean MAE remains **0.17427**, with the accepted CSV and receipt preserved. The ≤0.15 target remains unmet. No F split, F training or F outcome was created for this rejected batch.


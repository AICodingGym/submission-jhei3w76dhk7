# V023 controller derivative feasibility

The discrete per-step PID extension failed its frozen training-only gate. Best PID case: 19/576 breaths (3.30%) near-exact control consistency, versus matched PI 28/576 (4.86%). The rule required ≥10% and ≥2 percentage-point gain. All eight matched PID comparisons failed.

The diagnostic ran for 13.54 CPU seconds on the same 576 original-A-fit breaths, using raw float64 data. Thirty-eight synthetic checks passed before the protocol/source freeze; an independent **46-check** outcome audit then rebuilt every control residual, physical inverse, count and gate. Known pressures were diagnostic regressors, so these are control-consistency figures, **not pressure MAE or input-only recovery coverage**. Original A-validation and test pressures were excluded. The disclosed 72-breath overlap with earlier E resampling remains; E is not a pristine holdout.

Notebooks: `controller_pid_components_v023.ipynb` and executed `controller_pid_feasibility_v023.ipynb`. Protocol: `controller_pid_protocol_v023.json`, SHA256 `2c28eaf78fdcf94eed25b172bfef86c14168d81b4a73b086663f92dfbe7fba62`. Review: `controller_pid_review_v023.json`; result SHA256 `1ed1c1f94be7cfb3937a41e39d096b9c7de1125c7366dca516495134f59ba5c4`.

No pressure predictor, GPU job, validation promotion or submission was created. This rejects the tested constant/linear-reference derivative families, not all controller matching. Stop this branch rather than relaxing its threshold. Next prepare a distinct first-place-inspired convolution/LSTM hybrid on the successful engineered inputs. Best official mean MAE remains **0.17427**; ≤0.15 is unmet.


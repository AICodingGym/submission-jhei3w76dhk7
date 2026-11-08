# V028: strict raw-grid measurement assumption not verified

The frozen test stopped **before any conditional controller fits**. Its59962-breath training-only pool contained950 pressure levels, whose fitted uniform-grid residual reached5.026e-9 versus the declared machine-roundoff bound5.895e-11. The uniform raw-float64 model therefore did not pass its measurement gate. No primary controller outcomes or replicate were computed. Runtime20.168CPU seconds;45 synthetic checks preceded data use. A separate reconstruction passed20 provenance/stop checks.

This is not a pressure prediction, mean MAE result, or rejection of every controller law. The original V015/V020/V023 failures remain preserved. V028's native control budget1e-4 was never widened, and no GPU/submission/F/final fit was created. Original A-validation rows were skipped before numerical conversion; only approved Afit data was used.

Exploratory training-pool diagnosis found spacing about0.0703021454514 and raw residuals consistent in scale with decimal export rounding. All950 raw levels and integer codes were distinct, so float alias duplication did not cause the actual stop. A separate synthetic edge case revealed that the original density statistic mishandles multiple near-identical floating representations, but that was not this dataset's failure.

The separate prospective V032 hypothesis tests a fixed ten-significant-digit decimal export after physical uniform quantization. It requires exact rational verification of every rounding cell and uses a smaller conservative pressure-error cell. Controller family, samples, coefficients, control-error budget and all gates remain unchanged. No conditional controller outcome was observed before designing V032.

Artifacts: research/quantized_controller_feasibility_v028.ipynb; outputs/controller_quantization_feasibility_v028/summary.json; research/controller_quantization_review_v028.json; executed research/quantization_grid_diagnosis_v032.ipynb. Protocol148541702313b4cf211b142c7a168fd4764abe914194ae6406c7eb975b6fcfb0; componentc9d38ea98a7ee1be58b6a1b0b28df69cae14f00ad687b60f3ccd027ee34418d7. Official0.17427 preserved; <=0.15 target unmet.

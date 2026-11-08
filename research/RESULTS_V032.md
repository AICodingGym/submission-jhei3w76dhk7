# V032: controller compatibility survives a pressure-rounding check

The frozen serialization-aware diagnostic passed on both predeclared, disjoint samples from the original A training set. It did not predict validation pressure or create a submission.

| Sample | Breaths | Compatible with shared bounded rounding errors | Exact logged pressure | Shuffled pressure |
|---|---:|---:|---:|---:|
| Primary |576|202 (35.07%)|18 (3.13%)|0|
| Replicate |576|230 (39.93%)|21 (3.65%)|0|

Both passed the predeclared coverage, increment and whole-breath interval gates. Runtime was 20.68 CPU seconds; no GPU, neural training or checkpoint inference. An independent linear-programming oracle and certificate audit passed 2,626 checks. Each controller coefficient was fitted only on its chronological training prefix. Held rows shared one pressure-rounding error per time point; they could not receive independent, convenient errors for each equation. The native control residual budget remained 0.0001.

V028 had rejected a machine-precision lattice in the raw CSV values, before fitting any controller. V032 prospectively tested a different observation model: uniform physical pressure levels followed by ten-significant-digit decimal export. An exact rational witness verified every training-pool pressure level. Physical spacing was approximately 0.07030214545. The permitted pressure error half-width was 0.03515106772, conservatively reduced for export rounding; missing levels did not enlarge it. The old V028 result remains preserved. A synthetic exact-zero lattice exposed a numerical projection issue before approved-data execution; it was corrected and all cells were reverified exactly. The earlier source is preserved.

This strengthens the case for testing the control equation as a prediction aid. It does not show that gains, reference pressure or initial conditions can be inferred from a new breath's inputs. The diagnostic used known training pressures. Conditional compatibility is neither pressure MAE nor the percentage of new breaths that can be recovered. Larger gains can make compatibility permissive, and noisy-regressor OLS can miss valid controllers.

Next test a separately frozen input-only predictor, with all learned quantities fitted on original A training breaths and actual inspiratory A MAE compared against the accepted baseline. No controller-derived A prediction has been computed yet. Cold F confirmation and any final fit remain conditional on passing the unchanged practical-gain and uncertainty gates. Official MAE remains 0.17427; the <=0.15 goal is unmet.

Sources: research/quantized_controller_components_v032.ipynb; research/quantized_controller_feasibility_v032.ipynb. Protocol SHA60df642e250025108909de61d03bb8ea1275f7111167a33eee0dca7e75cc4d9d. Component code SHA62b546ce5220958c5eadc2d604ae23779932ef24bc0bd76f67cc9bea6b3043d1. Summary SHA129fccd0a2d5c87911a3b9062464baaa0eaf09c1149651c956c2bc698179b905. Independent audit research/controller_quantization_review_v032.json. Complete arrays, fit rows, certificates, lattice and execution evidence are under outputs/controller_quantization_feasibility_v032 and its _review directory.

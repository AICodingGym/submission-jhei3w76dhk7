# Draft: distinguish controller observation order before changing its error model

No V028 protocol, diagnostic code, fit or outcome exists. This is a scientific hypothesis from an independent local review, not an implemented result or a new pressure predictor. It preserves the failed V015/V020/V023 gates and does not relax their thresholds.

The discrete pressure grid supports two distinct observation orders: the controller may act on the same quantized pressure recorded in the CSV, or on a continuous pressure that is rounded afterward for storage. The grid alone does not identify which order generated a breath. Under the first order, the previous native control-consistency threshold remains appropriate. Under the second, a bounded quantization error must be modeled explicitly and jointly across time.

For the existing recurrence

`u[t] = d*u[t-1] - A*p[n] + B*p[n-1] - C*p[n-2] + g(n)`,

write recorded pressure as `p[j] = latent[j] + delta[j]`. If nearest rounding on a verified uniform raw-training lattice is the explicit hypothesis, `|delta[j]| <= spacing/2`. The recorded-pressure residual must obey

`r[t] = -A*delta[n] + B*delta[n-1] - C*delta[n-2]`.

Its necessary per-row bound is `|A|h[n]+|B|h[n-1]+|C|h[n-2]`. This bound alone is insufficient: adjacent equations share the same delta values, so one coherent bounded sequence must satisfy all held equations. Independent relaxed row thresholds would admit inconsistent pressure errors.

The existing PI coefficients imply `A=Kp+Ki, B=d*Kp, C=0`. PID implies `A=Kp+Ki+Kd, B=d*Kp+(1+d)*Kd, C=d*Kd`. Time-weighted PI uses `A[t]=Kp+Ki*dt[t]`. These identities should be independently checked against the frozen notebook definitions before any implementation.

An illustrative existing physical V020 fit for breath89216 had A about1.00633 and B about0.93533. If independently verified raw float64 training lattice spacing were about0.0703, the hypothesized control-residual bound could be about0.0683. That is a scale illustration, not evidence that rounding caused the residual or that the hypothesis is true. That particular fit already had near-exact held consistency.

A bounded future test should first verify the raw float64 A-fit lattice without treating missing codebook levels as wider bins or using unbounded endpoints. Freeze controller family/lag and physical coefficients on each breath's first70% rows, then test jointly feasible latent-error bounds on the remaining rows while keeping the native control-equation error budget unchanged. Include synthetic controls for both observation orders, destructive pressure-order controls, and a fresh predetermined A-fit-only confirmation sample. Use no original A-validation or test pressures. Freeze sources, samples, constraints, comparators and practical criteria before outcomes.

The central risk remains identifiability: unknown reference and absolute pressure can shift together. Gains and initial state are also unknown; arbitrary reference curves make compatibility weak evidence, large fitted gains inflate permitted bounds, and pressure-as-regressor noise can bias OLS gains. A positive conditional diagnostic cannot supply inference-time parameters or recover absolute pressure. Any later predictor must choose gains/reference/offset/grid using available inputs and training-only learned information, with an input-only reconstruction test before native grouped-A evaluation. No GPU fitting or submission is justified by consistency alone.

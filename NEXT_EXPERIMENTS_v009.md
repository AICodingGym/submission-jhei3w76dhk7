# Conditional next controlled batch: v009

Authorized by the user's standing approval in research/authorization_v008.json.
Prepare code while v008 attention finishes. Start these fits only if the complete
v008 screen selects no candidate; otherwise freeze and confirm the v008 winner
first. The accepted official .18550 model/CSV is preserved.

Two separate arms against the original compact model, without combining branches:

1. Shared breath offset plus centered local correction. Retain the compact
   BiLSTM/scalar head and add offset + local - mean_inspiration(local). Predict
   the shared offset from known-input encoder states pooled over inspiration
   (mean and max), with width16 hidden layers. Both added final projections start
   at zero. Approximately12,354 additional parameters. Inspiration masking reads
   known u_out reconstructed using the training-only feature scaler. All output
   pressures remain predictions; no target-derived offset enters inference.
2. Full-context residual TCN: project combined47 to96 channels; six residual
   blocks with two symmetric kernel3 convolutions at each dilation1,2,4,8,16,32,
   per-position LayerNorm/SiLU/dropout.15 and width32 scalar head. Receptive field
   spans the full80 known input positions. Encoder/head and regularization layout
   change as an architecture package; parameter count and initialization differ.

Rationale: residuals show coherent breath-wide shifts and local shape errors.
The label-dependent oracle only diagnoses structure and establishes no attainable
performance. Existing BiLSTM context and summaries may already explain everything
predictable, so the offset branch could be redundant. Earlier TCN failures are
real negative evidence but used causal20 inputs and shorter plateau/time-limited
fits, rather than combined47 and the current full schedule. No claimed gain.

Both arms use original Afit61,114/Aval6,791, seed20261102, combined47 numeric R/C,
training-only input/target scaling, Adam/no decay, batch256, original complete200
replay rates and native point-weighted inspiratory L1. Pair each new compact-side
member .5/.5 with the unchanged original deep A model. No loss/weight tuning.
Run actual-course synthetic strict-determinism, exact-resume and training256/
inference512 capacity proofs first. Stop for review above2x baseline step cost or
9GiB allocated peak. Expected two-arm screen about1–2.5GPUhours, subject to profile.

Same promotion rule: pair A gain>=.003 and whole-breath bootstrap95% upper<0.
Freeze only the lowest-A qualifier's recipe/epoch/rate prefix before fresh grouped
D seed20261202 inside original Afit. Original Aval excluded throughout confirmation.
Use new training-only statistics; D is resampling evidence, not a pristine test.
No runner-up after failed confirmation and no hidden-score tuning. All-approved
refit/aligned CSV/submission only after a validated improvement. Log configurations,
seeds, runtime, native/median/tail/R-C/phase scores, hashes, mistakes and visible
AI interactions. Keep existing files, checkpoints and accepted receipt.

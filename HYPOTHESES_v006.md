# Approved next experiments — H1 and H2

The user approved the recommended H1/H2 screen. Implementation is being prepared;
actual trial fitting waits for the current C/final pipeline to finish.
The existing frozen C confirmation and final all-approved-data refits continue.
Only the approved Gym data and our own completed experiment artifacts informed
this analysis. The accepted official score is .19486; .10 is a research target.

## Evidence from the fixed grouped A split

| Comparison | Native inspiratory MAE |
|---|---:|
| GRU128, fast plateau schedule → warmup/cosine, same 200 epochs | .565606 → .371982 |
| GRU128, causal20 → combined47 inputs, same frozen rates | .371982 → .334773 |
| Combined-input uniGRU128 → uniGRU256 | .334773 → .268507 |
| Combined-input BiGRU128 → BiLSTM128 | .262326 → .214166 |
| BiLSTM128 → deeper tapered/residual/concatenated BiLSTM package | .214166 → .211544 |
| Best individual → equal compact/deep LSTM pair | .211544 → .196563 |

The deeper-model comparison changes several architecture properties together;
it does not isolate depth. Directionality also changes recurrent parameter
count, so the BiGRU result alone cannot isolate the value of future information.
The fast-plateau baseline uses the v005 reproducible backend; it is not the prior
v004 fused-dropout model. Percent improvements across these rows are not additive.

The compact BiLSTM took 2,192 seconds (36.5 minutes); the deep package 8,482 seconds
(141.4 minutes), for about .00262 lower individual A MAE. Training-sample versus
validation MAE was .1393/.2142 for compact and .0945/.2115 for deep. The larger gap
and small held-out gain favor spending early screening time on the compact model.
These sample gaps are diagnostic evidence, not a proof of an irreducible floor.

The compact BiLSTM improved from .257315 through epoch 100 to .222280 through 150
and .214166 through 200. Longer training still helped, with diminishing gains.
The best checkpoints occurred near the end of the 200-epoch budget.

## Remaining errors in the frozen A ensemble

- R=50: 40.43% of scored points, 50.41% of total absolute error, MAE .245122.
- R=5: MAE .148626; R=20: .181960.
- R=50/C=10 contributes the most absolute error (18.53% of all error) because
  it is a larger group. R=50/C=20 and R=50/C=50 have higher group MAEs (.286076
  and .276903) and contribute 16.34% and 15.54% respectively.
- Middle/late inspiration contributes 70.56% of error across 66.34% of points.
- Worst 10% of breaths contribute 40.52% of error; worst 1% contribute 10.93%.
  Even an unavailable perfect correction of the worst 10% alone would leave
  roughly .117 A MAE. Broad improvement is needed for .10.
- The two LSTM residuals correlate .6691. Averaging helps, but adding models
  with identical mistakes is unlikely to justify their cost.
- Overall signed bias is only +.00502. A global pressure offset is unlikely to
  be the main way to halve error.

## Hypotheses and tests

### H1 — Give the efficient sequence model more useful practice

Hypothesis: the compact BiLSTM is a better platform for further training than
simply adding layers. Preserve its current architecture, inputs, grouped split,
seed, masked L1 loss and training-only preprocessing.

1. Duration-only control: extend the exact saved 200-epoch trajectory by 100
   epochs at the existing minimum rate, preserving optimizer/RNG state and the
   first 200 epochs. Compare the best-through-300 checkpoint with the existing
   best-through-200 checkpoint. Estimated additional A training: 20 minutes.
2. Schedule-only comparison at a matched 300-epoch budget: fresh 300-epoch cosine
   training with the same peak rate and warmup, compared against test 1's full
   300-epoch trajectory. Estimated A training: 55 minutes.

This separately examines more updates and slower cooling. It does not assume
that simply doubling the epoch count will halve error. Keep the best held-out
checkpoint and monitor evaluation-mode training versus validation curves.

### H2 — Shared sequence learning with lung-setting-specific outputs

Hypothesis: a single common output mapping still struggles with the distinct
high-resistance responses. Keep the compact BiLSTM and all controls fixed; add
small output heads selected by the observed R/C combination. Share the sequence
encoder rather than fitting nine large independent models.

This is different from adding R/C at each step, which is already correct, and
from replacing numerical R/C with embeddings, which previously performed worse.
Numerical R/C remains available. The first pilot changes only the output-head
choice; joint embeddings and training-only R/C/step baseline curves would be
separate later tests. Estimated A training: about 40 minutes.

### H3 — Make upcoming changes in the known controls explicit

Hypothesis: explicit future u_in change rates around transitions could help the
model recognize pressure changes more easily. Current inputs already contain
future u_in values and past differences. A separate test would add future
within-breath changes divided by the actual elapsed time, with safe boundaries.
Only provided inputs are used; no future pressure labels. Training-only scaling
and the existing loss/split remain fixed. This may prove redundant with what the
bidirectional LSTM already learns. Estimated A training: about 40 minutes.

### H4 — Further ensembles chosen by complementary errors

Hypothesis: a new efficient model/seed that fails differently could improve the
average. Test individual models against a bounded, A-selected ensemble using a
fixed split; freeze members/weights before separate grouped confirmation.
Earlier equal-seed GRU averaging was worse, so more members alone are not enough.
Consider additional compact-LSTM seeds first; an alternative whole-breath
architecture would be a later, more exploratory step. No claim that averaging
alone can take .195 to .10. Two seed fits: about 75 minutes of A training.

## Recommended approval scope

Approve H1's two controlled tests plus H2's single output-head test as the first
screen. Estimated A-screening cost is roughly two GPU hours after the currently
running pipeline finishes; grouped confirmation/final refits would be additional.
No current training run, data file, A split, C choice, or accepted CSV changes.

Rank candidates on overall native inspiratory A MAE, with total-error diagnostics
by lung setting and breath position. Compare any new individual with its same-
architecture control and compare any proposed final ensemble with the current
.196563 A ensemble. Freeze any promising recipe and bounded ensemble before
another grouped confirmation; use no hidden-test score to tune weights or rates.
Advance a candidate only if it offers a meaningful overall improvement, rather
than a tiny gain in a small cherry-picked group. Preserve configurations, seeds,
checkpoints, runtime, source hashes, failed runs and visible interaction history.

H3/H4 are proposals for a later decision, not approval to implement them now.

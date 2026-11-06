# MLEvolve and Disarray methodology review

Reviewed November 6, 2026, after the user explicitly requested this research. Scope: authors' framework descriptions, published evaluation setup and benchmark reports. No competition solution code, pretrained competition models or additional datasets were downloaded. Incidental search results for unrelated competition solutions were excluded from this review and experiment planning.

## What the evidence establishes

MLEvolve describes a search graph with several evolving branches, a memory of plans/code/metrics/failures, and transfer or fusion between branches when progress stalls. It moves from broader exploration toward exploiting promising candidates. This is an experiment-management method, not one fixed pressure-prediction model. [Author project page](https://internscience.github.io/MLEvolve/)

The original February benchmark submission reports Gemini-3-Pro-Preview, 21 vCPUs, 234 GB RAM, one NVIDIA H200 and a 12-hour limit. The team states that optimization uses internally constructed validation sets and that private test scoring happens only after the final submission. Later papers use a newer backbone, so their settings should not be silently assigned to the earlier reports. [Original MLEvolve submission](https://github.com/openai/mle-bench/pull/120)

Disarray describes separate execution and supervision roles, checks against overcommitting to expensive approaches, durable experiment state, and inspectable asynchronous jobs. Its design article gives an example where exploring simpler alternatives was much faster than a prolonged complex trajectory. These are useful research-process principles; the article does not identify the ventilator architecture. [Author design article](https://disarray.ai/featured/design-principles-for-long-running-research-agents)

The original Disarray submission reports one A100, 24 vCPUs, 220 GB RAM and 24 hours. Its authors acknowledge a limited binary medal-status signal when requesting early termination. [Submission and author clarification](https://github.com/openai/mle-bench/pull/118)

The official leaderboard consequently places Disarray under additional submissions with test-set feedback, separate from the main table. This changes the evaluation comparison; it does not quantify any effect on this particular ventilator run. [Official leaderboard](https://github.com/openai/mle-bench#leaderboard)

Neither the inspected framework documents nor our assignment-linked grading reports identify the exact ventilator training architecture, features, loss, fold count or ensemble recipe. It would be unsupported to claim they attained their scores using a particular pressure-model trick.

## Scores and comparability

Previously preserved assignment-linked reports (`../benchmark-review/benchmark-evidence.json`, reviewed November2) contain:

| Agent | Three ventilator mean MAEs | Best | Arithmetic mean |
| --- | --- | ---: | ---: |
| MLEvolve | .16719, .14237, .15383 | .14237 | .15446 |
| Disarray | .15341, .15171, .15419 | .15171 | .15310 |

Best-run ordering differs from average-run ordering. Three agent runs need not represent the same model with only a different model seed. These benchmark values and our Gym score are useful context, not matched training experiments. Our accepted official MAE is .18025; V013's .186264237 is an A-validation score, not a new official score. GPU types and resource budgets also differ, and no controlled throughput comparison was performed.

## How this changes our next decisions

These are project-specific inferences, not claims about the competitors' ventilator implementations:

1. Maintain explicit branches for input representation, model structure and training objective, with a common grouped metric. Keep the existing fixed comparison and promotion rules.
2. Use bounded pilot runs for uncertain new mechanisms, retaining enough training to detect delayed learning. Short pilots are screening proxies, not evidence that a slower-learning model can never work.
3. Reuse recorded negative results: do not simply repeat the failed TCN, attention, pressure-category and stronger-dropout recipes without a new reason or isolated change.
4. Transfer successful mechanisms. Compact curve consistency helped ensemble diversity; deep curve consistency then produced a larger A gain. A future controlled branch could combine curve consistency with learned response memory or a breath-level offset, changing one mechanism at a time. No such new model has been implemented by this review.
5. Keep evaluator checks separate from training code. Preserve measured grouped scores, hash-bound artifacts and exact CSV alignment; never choose weights using official score feedback.
6. Leave the V014 E-confirmation recipe unchanged. It is already frozen from the lowest eligible A mixture. Only a confirmed pass can justify the conditional final fit and next submission.

## Current experiment evidence

V013 reference A mean MAE .190851029. Seed-only mixture .189368987 failed the minimum .003 gain gate. Deep curve-loss mixture .186264237 qualified, with whole-breath95% difference interval [-.005802171,-.003413038]. Adding both new deep models gave .186703791 and ranked second. Independent audit74/74 passed. Details are in `results_review_v013.ipynb` and `research/screen_review_v013.json`.

V014 requests a new grouped E split inside original Afit and cold-fits all six members. This is resampling confirmation after repeated research on A, not an untouched test. Latest live queue/run state is in `PROCESS_STATUS.md`; this document does not assert that E has completed.

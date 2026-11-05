# V011 confirmation handoff — prepared, not run

User is migrating Codex accounts because of a weekly limit. Stop research and GPU
work until they explicitly continue. Standing approval for controlled iterations
exists in `research/authorization_v008.json`; this is not permission to ignore the
current stop. Root maintains the broader project handoff.

## Frozen source and verification

- Notebook: `confirmation_v011.ipynb` (nine cells, definitions/review by default).
- Code SHA256 (`'\n'.join(code cells)`):
  `0208428c5ef3407990d05a4b7f08a9c46b9df4465680957b236b95fccf370c2d`
- Full-file SHA256:
  `b2fe48b833e9950d60a0f15aca4191347709acdd3e6b37e82e99db5518e66fd8`
- Preflight: `research/confirmation_preflight_v011.json`; schema/default guard,
  23 synthetic protocol checks and all component source guards pass. Default and
  synthetic checks ran with assignment CSV parsing blocked. The five-candidate
  A-only selector was also tested with CSV parsing blocked.
- Original four-candidate protocol received independent read-only review. The
  narrow notebook portability helper also received independent review. Fifth-case
  integration has passed the checks above; an additional peer review was requested
  but must not delay stopping for account migration.
- No actual D split, `locked_before_D.json`, D pressure scoring, D model fitting,
  D decision, final-all fitting or submission has occurred in this notebook.

## Exact candidate to freeze on a future authorized run

The completed five-case A selector chooses
`deep_half_compact_curve_memory_offset`:

| Factory/member ID | Weight | Frozen A epoch/rate prefix |
|---|---:|---:|
| deep | .5 | 189 |
| original_compact | .125 | 193 |
| curve | .125 | 193 |
| memory | .125 | 191 |
| offset | .125 | 193 |

All use seed20261102, combined47, original batch256/Adam/no decay and their exact
A-selected prefix of the original full200 LR list. Curve alone uses curve_l1
(main inspiratory L1 +.10 adjacent-increment L1); all others use main L1.
Original_compact/deep use V005; new members use V008 adapters. Registry also
supports attention and fast TCN for the preserved earlier candidate choices.

V012 was exactly one predeclared additional mixture, independently verified in
`research/diversity_review_v012.json` (118 checks): A MAE .19085102921770208,
gain .005711580604474548 versus .19656260982217663; paired whole-breath95% CI
[-.007219534875537107,-.004389991151684003]. Source/report/hypothesis and saved
prediction/row hashes matched. No additional mixture was calculated. All five
fixed A cases must still be verified at production startup before one winner is
frozen; there is no D-driven runner-up or weight/epoch search.

## Production API, guards and artifacts

Run only later on an approved normal course CUDA allocation, from the repository
root, with:

```
PA3_RUN_CONFIRM_V011=1
PA3_CONFIRM_V011_SOURCE_SHA256=0208428c5ef3407990d05a4b7f08a9c46b9df4465680957b236b95fccf370c2d
```

Set `PA3_RESUME_CONFIRM_V011=1` only for recovery. Entry point:
`run_confirmation_v011(root=Path.cwd(), resume=...)`. Shared GPU flock:
`outputs/.v011_gpu.lock` (also used by the separate final notebook).

Before parsing pressure, the runner verifies every completed A input and selects
one lowest eligible candidate among V009's two fixed pairs, V010's two mixtures
and V012's one mixture. It reads IDs/R/C only to create a new split via sklearn
`train_test_split(sorted_original_Afit, test_size=6791, random_state=20261202,
stratify=joint_RC_code)`, then sorts global indices. Dfit54323/Dval6791 are wholly
inside original Afit61114; original Aval6791 is excluded throughout D.

Immutable, atomic artifacts under `outputs/confirmation_v011/`:

- `D_split.json`: seed/method, sorted global int64 indices and int32 breath IDs
  for A_fit/A_validation/D_fit/D_validation, counts, raw-byte group/index hashes.
- `locked_before_D.json`: winner/baseline/required member recipes, all five A
  comparisons, exact A artifact hashes, component/main code hashes, approved
  train hash and split hash/groups. No changing timestamp or self digest.
- External `selection_sha256` is compact canonical JSON SHA256 using
  `sort_keys=True,separators=(',',':'),allow_nan=False`; raw file SHA is separate.
- `D_models/<member>/identity.json`, checkpoints, reports and predictions: fresh
  Dfit-only statistics for every member; original A model files are provenance
  only. Compact193/deep189 are also cold fitted. Fixed-budget fitters receive no
  validation labels. Optimizer/RNG/source/config/data/runtime resume guards remain.
- `confirmation_result.json`: `status='complete'`, selection/raw-lock/source/data/
  split hashes, `winner_name`, `decision={passed,gain,baseline_MAE,candidate_MAE,
  interval}`, member and ensemble artifacts plus row-ID hashes. Pass only when
  D gain>0 and paired whole-breath1000-draw seed20261201 upper95%<0. Failure ends
  this recipe. D is resampling evidence, not a pristine holdout.

The separate `final_fit_v011.ipynb` consumes that lock/result schema and independently
checks all D artifacts/gates without reading D labels. It has no permission to
start before a successful immutable D decision. Final consumer was coordinated
with the fifth roster; see root handoff for its final source hash/status.

## Required evidence and portability details

Keep all original V005/V008/V009 records/models/reports/native predictions,
complete A summaries, split IDs/row IDs, V008 independent audit, V010/V012
hypothesis/notebook/results/independent review files, approved train CSV and all
referenced component notebooks. V012 provenance additionally references the full
V009 completed backup manifest and preserved `server_snapshot_completed` files.
The A-only selector currently freezes 114 input file hashes.

Only explicitly declared, whitelisted notebook source-manifest entries may have
different raw JSON bytes across local/server execution when code SHA is EXACTLY
identical. V010/V012 manifests are combined with matching declared raw provenance;
there is no blanket .ipynb exception. Expected/observed code/raw hashes are stored
as `notebook_portability_evidence`. The lock then freezes actual observed raw file
hashes in `selection_input_files`, so later same-project resume remains strict.
All data/model/report/array and archived snapshot hashes remain full-file exact.
Own screen notebook code hashes are checked against their reports and actual raw
file hashes enter the freeze. Do not alter the original V010/V012 reports/audits.

## Remaining work and limitations

1. Resume only after the user's migration handoff and explicit continuation.
2. Verify the new approved course pod/queue and source/data transfer through the
   normal launcher; no quota bypass. This agent did no deployment or server work.
3. Preserve/upload every referenced evidence file, including archived snapshots;
   missing or changed strict inputs intentionally stop before D labels are parsed.
4. On the actual runtime, use the frozen source hash, create/match the pre-D lock,
   run the five cold D members and independently audit the eventual D result.
5. D acceptance is unknown. No final-all fit or submission is authorized by a
   merely promising A score; accepted official .18550 artifacts remain preserved.

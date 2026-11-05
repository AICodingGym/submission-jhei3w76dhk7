# Process map

November5, approximately6:45AM Pacific. Best accepted official MAE remains **0.18550**.

| Process | Status |
|---|---|
| User authorization | This batch and future controlled iterations approved |
| New attention and learned-memory notebook components | CPU checks passed |
| Shared trainer and exact checkpoint recovery | CPU and actual-course CUDA integration checks passed |
| Course GPU request | Running: v2gao-2239777 on n05, GTX1080Ti11GB |
| Actual-GPU determinism, resume, training/inference profiling | Passed, strict determinism and exact resume for all three arms |
| Pressure-curve consistency / learned-memory / attention A fits | Curve arm active; memory and attention follow, separate200-epoch recipes |
| Fresh grouped D confirmation | Only if a candidate passes frozen A gate |
| New all-data fit and submission | Only after successful confirmation |

Three A fits estimated2–4GPUhours after runtime checks, plus queue time. The accepted .18550 model, CSV, receipt and all previous artifacts are preserved. No .10 MAE claim is made. Code: controlled_experiments_v008.ipynb; protocol: NEXT_EXPERIMENTS_v008.md.

GPU profile: curve .99x, learned memory1.29x, attention1.15x baseline step time; each below785.5MB allocated peak at training256/inference512. No recipe/batch/data reduction needed. Coordinator backs up and verifies all artifacts before releasing idle GPU; lease termination requires review before another allocation.

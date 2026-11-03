# Process map

Checked **November 3, 2026, 3:13 PM Pacific**. Iteration v005 is active;
the official Gym target of MAE 0.20 has not been reached.

```text
Approved data + course CUDA environment       VERIFIED
  ├─ v003 / v004 comparisons + A/B validation COMPLETE
  │   └─ all-data fit + Gym submission        ACCEPTED — official MAE .47462
  └─ v005 improvements                       ACTIVE
      ├─ CPU known-input feature comparisons COMPLETE — best A .503760
      ├─ CPU tree count / leaf comparisons   COMPLETE — best A .481397; exploratory
      ├─ GPU learning-rate comparisons       COMPLETE — cosine A .371982
      ├─ GPU input-feature comparisons       COMPLETE — combined A .334773
      ├─ GPU larger GRU / BiGRU / BiLSTM      ACTIVE — GRU256 first
      ├─ fresh grouped C confirmation        PREPARED; A selection not frozen
      └─ all-data refit + CSV + Gym score     WAITING for confirmed selection
```

| Process / resource | Current state |
|---|---|
| Course pod `v2gao-306419` | Running on `its-dsmlp-n05.ucsd.edu`; NVIDIA GTX 1080 Ti verified. Started 2:00:05 PM; expected deadline 8:00:05 PM Pacific November 3. |
| GPU sequence worker PID `142` | Resumed the interrupted patience-6 run; it completed 200 epochs. Cosine completed at A .371982; all feature arms completed; combined A .334773 won. GRU256 capacity trial is active. Phase limit is `capacity`. |
| CPU tree worker | Feature comparisons complete. Additional tree-capacity worker PID `420` completed both arms: A .484391 (5,000 trees), .481397 (1,023 leaves); excluded from current confirmation inventory. |
| Old pod `v2gao-11673` | Expired on schedule; pod logs archived and expired object removed before the replacement was officially launched. |
| Progress backup | 43-file snapshot preserved on DataHub and Mac; archive SHA-256 verified. This is a progress snapshot, not a finished-run archive. |
| SSH | Connected through the user's authenticated shared connection. |

Completed v005 comparisons on the same A split (61,114 fitting / 6,791 validation
breaths), native-unit inspiratory MAE:

| Candidate | A MAE | Status |
|---|---:|---|
| GRU, plateau patience 1, 200 epochs | .565606 | Complete; worse than incumbent |
| GRU, plateau patience 6, 200 epochs | .415483 | Complete; selected checkpoint epoch 193 |
| GRU, warmup/cosine, 200 epochs | .371982 | Complete; selected checkpoint epoch 189; schedule winner; awaiting feature/capacity comparisons and C |
| GRU, offline 34 inputs, 200 epochs | .351865 | Complete; selected checkpoint epoch 192; provisional feature leader |
| GRU, dynamics 33 inputs, 200 epochs | .341036 | Complete; checkpoint epoch 192 |
| GRU, combined 47 inputs, 200 epochs | .334773 | Complete; checkpoint epoch 193; feature winner |
| LightGBM, causal 20 inputs | .618996 | Verified prior model reuse |
| LightGBM, offline 34 inputs | .529058 | Complete |
| LightGBM, dynamics 33 inputs | .575459 | Complete |
| LightGBM, combined 47 inputs | .503760 | Complete |

These A scores describe validation models. They are not official Gym scores and
do not yet establish that a final all-data model improves on the accepted CSV.

Persistent DataHub project:
`/home/v2gao/dsc102/pa3/gym-workspace/ventilator-pressure-prediction`

The local project contains the same source notebooks. Work next in
`iterative_improvements_v005.ipynb`; inspect evidence in
`results_review_v005.ipynb`. The separate `confirmation_final_v005.ipynb` freezes
a completed A phase before fitting C and then all approved labeled breaths.

- Active GPU artifacts: `outputs/improvements_v005/sequence/`
- Completed CPU artifacts: `outputs/improvements_v005/tree_context/`
- GPU log: `/home/v2gao/dsc102/pa3/setup/v005-sequence-execution.log`
- Current progress archive: `outputs/improvements_v005/v005-progress-20261103T214805Z.tar.gz`
- Accepted fallback CSV: `outputs/sequence_v004b/final_all/submission.csv`
- Accepted receipt: `research/submission_receipt_v004b.json`

Persistent home files survive pod expiry. Every completed GPU epoch also saves
optimizer and RNG state for continuation. The current replacement coordinator
has finished its one replacement; another container will be needed if work runs
past the current deadline.

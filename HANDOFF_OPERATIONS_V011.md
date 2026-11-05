# V011 operational handoff

This is a read-only operational review, updated for account migration. No server commands, D split creation, D pressure/outcome reads, model execution, training, GPU work or submission was performed by this reviewer. Root states that no D work has launched. Root is separately checking the queued pod; the status below is not a fresh server observation.

## Current local helpers

All reviewed operational sources are under `outputs/confirmation_v011/setup_helpers/`:

- `execute_notebook_v011.py`: executes one pinned notebook, records outputs while preserving its code hash, and requires the guarded stage's exported result dictionary.
- `run_pipeline_v011.py`: holds `pipeline-worker.lock`, runs confirmation first, and invokes final fitting only after a completed matching locked result reports a D pass.
- `start_v011.sh`: holds the wrapper lock, starts one worker, records its status, and leaves the container idle afterward.
- `snapshot_v011.py`: waits for worker and wrapper locks, records file hashes, and creates the backup archive.
- `verify_archive_v011.py`: checks the downloaded archive's size/SHA, unique safe regular members, exact manifest membership, and every recorded file's size/SHA.
- `deploy_v011.py`: validates the deployment payload hash and safe regular tar members, backs up changed existing destination files, and publishes replacements atomically.
- `guardian_v011.sh`: monitors only the already requested pod, deploys once, retrieves and verifies the backup, then deletes the idle pod. It does not allocate a replacement.

The helpers use the course container project `/home/v2gao/dsc102/pa3/gym-workspace/ventilator-pressure-prediction` and setup directory `/home/v2gao/dsc102/pa3/setup`. The guardian currently names pod `v2gao-2729938` and login-stage directory `$HOME/.pa3-setup-control.gty67K/v011-deploy-20261105`. These are configured references, not verified live status.

## Confirmed fixes already present locally

1. Snapshot archives each resolved regular file with the intended original archive name (`t.add(p.resolve(), arcname=arc(p), recursive=False)`), so the execution-log symlink is preserved as its target's file content rather than as a symlink.
2. Snapshot attempts nonblocking acquisition of both the worker lock and wrapper lock, retrying for approximately ten seconds and refusing archival/deletion if either remains active. The wrapper lock also covers its final status-file write.
3. Guardian now invokes `verify_archive_v011.py` successfully before `kubectl delete`. This repairs the earlier transfer-checksum-only gap; the verifier additionally checks every manifest entry and rejects unsafe/nonregular members.

## Remaining material issue

**The snapshot still omits the operational helper source files unless another explicitly pinned path happens to include them.** Its setup scan is `S.glob('v011*')`. The executor, pipeline, start, snapshot, deploy, guardian and archive-verifier filenames listed above do not begin with `v011`, and the scan skips directories. Add the actual deployed helper sources explicitly to the snapshot file list, retaining their hashes and regular-file archive handling. Do not assume that `project_dependency_files` includes setup files: that pin dictionary was still to be generated when this review was requested.

This omission affects reproducibility/provenance of the archived execution log. It does not imply that the reviewed model sources or existing accepted model artifacts were overwritten.

## Preserved operational constraints

No additional material issue was found in the reviewed stage ordering, production environment-variable names, notebook source-pin checks, or nonblocking worker/wrapper/coordinator locks. Confirmation failure stops final fitting. The final notebook separately validates the immutable choice, D evidence and fixed recipe. Changed deployment files are backed up. The accepted `.18550` artifacts are protected by the model notebooks' existing hash checks and separate output paths.

The helper set has no automatic resource-allocation/replacement call and no Gym submission command. A later submission remains root's explicit step after independent CSV review. Root must finish pins/payload generation from the final five-candidate-reviewed notebook versions and record the deployed hashes in the master handoff; this review did not generate or deploy those pins.

Python helper sources and the two shell scripts passed local syntax checks before the latest archive-verifier addition. The newly added verifier was read statically, not executed. No production run was launched during this review.

## Root completion after this review

The helper-source omission is now fixed in code: snapshot_v011.py requires and
archives every setup_dependency_files entry from v011-pinned-sources.json.
The prepared pins enumerate all seven operational helpers. Project dependencies
are also required to exist; missing dependencies prevent archival/deletion.
Pins and the complete reviewed-source payload are now prepared under
outputs/confirmation_v011/setup_helpers. They have not been dispatched.
See CONTINUE_HERE.md for the exact staged resume command and current live pod.

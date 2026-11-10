#!/bin/bash
set -uo pipefail
umask 077
PA3_ROOT=/home/v2gao/dsc102/pa3
: "${PA3_V037_ATTEMPT:?Pass final pod attempt}"
[[ "$PA3_V037_ATTEMPT" =~ ^v2gao-[0-9]+-final$ ]] || exit 2
export PA3_V037_RUNTIME=/home/v2gao/private/.pa3-preserved-course-backups/v037-runtime/$PA3_V037_ATTEMPT
mkdir -p "$PA3_V037_RUNTIME" /home/v2gao/private/.pa3-preserved-course-backups/v037-archives || exit 1
exec 9>"$PA3_ROOT/setup/v037-start-wrapper.lock"
/usr/bin/flock -n 9 || exit 0
trap 'PA3_STATUS=$?; printf "%s\n" "$PA3_STATUS" > "$PA3_V037_RUNTIME/v037-wrapper-status-$HOSTNAME.txt"' EXIT
export PA3_RUN_FINAL_V037=1 PA3_RESUME_FINAL_V037=1
export PA3_RUN_V013=0 PA3_RUN_V036=0 PA3_RUN_FINAL_V011=0 PA3_RUN_FINAL_V018=0
export OMP_NUM_THREADS=4 OPENBLAS_NUM_THREADS=1 CUBLAS_WORKSPACE_CONFIG=:4096:8
PA3_V037_SOURCE_SHA256=$("$PA3_ROOT/.venv/bin/python" -c 'import json;print(json.load(open("/home/v2gao/dsc102/pa3/setup/v037-pins.json"))["freeze"]["source_code_sha256"])')
PA3_V037_F_RESULT_SHA256=$("$PA3_ROOT/.venv/bin/python" -c 'import json;print(json.load(open("/home/v2gao/dsc102/pa3/setup/v037-pins.json"))["F_result_sha256"])')
PA3_V037_F_AUDIT_SHA256=$("$PA3_ROOT/.venv/bin/python" -c 'import json;print(json.load(open("/home/v2gao/dsc102/pa3/setup/v037-pins.json"))["F_audit_sha256"])')
export PA3_V037_SOURCE_SHA256 PA3_V037_F_RESULT_SHA256 PA3_V037_F_AUDIT_SHA256
if test -e "$PA3_V037_RUNTIME/v037-exit-code.txt";then echo 'Existing terminal attempt needs review';exit 1;fi
# Leave recovery room for an archive error even if another file exhausts quota.
"$PA3_ROOT/.venv/bin/python" -c 'import os,pathlib;p=pathlib.Path(os.environ["PA3_V037_RUNTIME"])/"archive-error-reserve.bin";f=p.open("xb");f.write(b"0"*5242880);f.flush();os.fsync(f.fileno());f.close()' || exit 1
(cd "$PA3_ROOT/gym-workspace/ventilator-pressure-prediction" && "$PA3_ROOT/.venv/bin/python" -u "$PA3_ROOT/setup/course_preflight_v037.py") > "$PA3_V037_RUNTIME/v037-course-preflight.log" 2>&1
PA3_STATUS=$?
if test "$PA3_STATUS" != 0;then printf "%s\n" "$PA3_STATUS" > "$PA3_V037_RUNTIME/v037-exit-code.txt";exit "$PA3_STATUS";fi
"$PA3_ROOT/.venv/bin/python" -u "$PA3_ROOT/setup/execute_final_v037.py" > "$PA3_V037_RUNTIME/v037-final-execution.log" 2>&1 &
PA3_PID=$!;printf "%s\n" "$PA3_PID" > "$PA3_V037_RUNTIME/worker.pid"
wait "$PA3_PID"
PA3_STATUS=$?
printf "%s\n" "$PA3_STATUS" > "$PA3_V037_RUNTIME/v037-exit-code.txt"
/usr/bin/flock -u 9
exec /bin/sleep infinity

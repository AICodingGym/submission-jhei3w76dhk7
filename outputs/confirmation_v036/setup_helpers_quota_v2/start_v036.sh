#!/bin/bash
set -uo pipefail
umask 077
PA3_ROOT=/home/v2gao/dsc102/pa3
: "${PA3_V036_STAGE:?Pass first_five or remaining_two}"
: "${PA3_V036_ATTEMPT:?Pass reviewed pod-stage attempt}"
case "$PA3_V036_STAGE" in first_five|remaining_two) ;; *) exit 2;; esac
[[ "$PA3_V036_ATTEMPT" =~ ^v2gao-[0-9]+-(first_five|remaining_two)$ ]] || exit 2
PA3_OPS=/home/v2gao/private/.pa3-preserved-course-backups/v036-runtime/$PA3_V036_ATTEMPT
mkdir -p "$PA3_OPS" || exit 1
exec 9>"$PA3_ROOT/setup/v036-start-wrapper.lock"
/usr/bin/flock -n 9 || exit 0
trap 'PA3_WRAPPER_STATUS=$?; printf "%s\n" "$PA3_WRAPPER_STATUS" > "$PA3_OPS/v036-$PA3_V036_STAGE-wrapper-status-$HOSTNAME.txt"' EXIT
printf "%s\n" "$$" > "$PA3_OPS/wrapper.pid"
export PA3_RUN_V036=1 PA3_RESUME_V036=1
export PA3_RUN_V035=0 PA3_RUN_V029=0 PA3_RUN_V031=0 PA3_RUN_V024=0 PA3_RUN_V026=0 PA3_RUN_V027=0 PA3_RUN_V021=0 PA3_RUN_V019=0 PA3_RUN_V013=0 PA3_RUN_V014=0 PA3_RUN_FINAL_V011=0 PA3_RUN_FINAL_V018=0
export OMP_NUM_THREADS=4 OPENBLAS_NUM_THREADS=1 CUBLAS_WORKSPACE_CONFIG=:4096:8
PA3_V036_SOURCE_SHA256=$("$PA3_ROOT/.venv/bin/python" -c 'import json;print(json.load(open("/home/v2gao/dsc102/pa3/setup/v036-pins.json"))["freeze"]["source_code_sha256"])')
PA3_V036_PROTOCOL_SHA256=$("$PA3_ROOT/.venv/bin/python" -c 'import json;print(json.load(open("/home/v2gao/dsc102/pa3/setup/v036-pins.json"))["freeze"]["protocol_sha256"])')
export PA3_V036_SOURCE_SHA256 PA3_V036_PROTOCOL_SHA256
if test -e "$PA3_OPS/v036-$PA3_V036_STAGE-exit-code.txt";then echo 'Existing terminal attempt requires review';exit 1;fi
# Refuse to replace old course evidence. Prior failed-attempt paths are preserved before launch.
ln -s "$PA3_OPS/v036-$PA3_V036_STAGE-screen-$HOSTNAME.log" "$PA3_ROOT/setup/v036-$PA3_V036_STAGE-screen-execution.log" || exit 1
ln -s "$PA3_OPS/v036-$PA3_V036_STAGE-course-preflight.log" "$PA3_ROOT/setup/v036-$PA3_V036_STAGE-course-preflight.log" || exit 1
(cd "$PA3_ROOT/gym-workspace/ventilator-pressure-prediction" && "$PA3_ROOT/.venv/bin/python" -u "$PA3_ROOT/setup/course_preflight_v036.py") > "$PA3_OPS/v036-$PA3_V036_STAGE-course-preflight.log" 2>&1
PA3_PROOF_STATUS=$?
if test "$PA3_PROOF_STATUS" != 0;then printf "%s\n" "$PA3_PROOF_STATUS" > "$PA3_OPS/v036-$PA3_V036_STAGE-exit-code.txt";exit "$PA3_PROOF_STATUS";fi
"$PA3_ROOT/.venv/bin/python" -u "$PA3_ROOT/setup/execute_screen_v036.py" > "$PA3_OPS/v036-$PA3_V036_STAGE-screen-$HOSTNAME.log" 2>&1 &
PA3_PID=$!;printf "%s\n" "$PA3_PID" > "$PA3_OPS/worker.pid"
wait "$PA3_PID"
PA3_STATUS=$?
printf "%s\n" "$PA3_STATUS" > "$PA3_OPS/v036-$PA3_V036_STAGE-exit-code.txt"
/usr/bin/flock -u 9
exec /bin/sleep infinity

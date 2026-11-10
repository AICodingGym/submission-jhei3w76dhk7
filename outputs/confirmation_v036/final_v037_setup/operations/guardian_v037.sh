#!/bin/bash
set -euo pipefail
umask 077
export KUBECONFIG=/home/linux/dsmlp/08/308/v2gao/.kube/config
export TERM=dumb
PA3_STAGE="${1:?Pass verified login staging directory}"
PA3_POD="${2:?Pass ordinary course pod name}"
[[ "$PA3_POD" =~ ^v2gao-[0-9]+$ ]] || exit 2
PA3_ATTEMPT="$PA3_POD-final"
PA3_RUNTIME=/home/v2gao/private/.pa3-preserved-course-backups/v037-runtime/$PA3_ATTEMPT
PA3_MISSING_COUNT=0
exec 9>"$PA3_STAGE/coordinator.lock"
/usr/bin/flock -w 60 9 || { echo 'Another V037 guardian holds the lock';exit 0; }
while true;do
 if test -f "$PA3_STAGE/cancel";then echo 'User canceled monitoring';exit 0;fi
 if ! PA3_PHASE=$(/usr/bin/kubectl --request-timeout=20s get pod "$PA3_POD" --ignore-not-found -o jsonpath='{.status.phase}');then echo "Transient pod observation failure; preserving job";sleep 60;continue;fi
 case "$PA3_PHASE" in
  Pending) sleep 60;continue;;
  Running) ;;
  *) /usr/bin/kubectl get pod "$PA3_POD" -o json > "$PA3_STAGE/terminal-pod.json" 2>/dev/null || true;echo "Pod $PA3_PHASE; review saved state before any replacement";exit 0;;
 esac
 if ! test -f "$PA3_STAGE/dispatched";then
  if ! /usr/bin/kubectl get pod "$PA3_POD" -o jsonpath='{.status.conditions[?(@.type=="Ready")].status}' | /usr/bin/grep -q True;then sleep 10;continue;fi
  PA3_SHA=$(cat "$PA3_STAGE/payload.sha256")
  /usr/bin/kubectl cp "$PA3_STAGE/v037-deploy.tar.gz" "$PA3_POD:/tmp/v037-deploy.tar.gz"
  /usr/bin/kubectl cp "$PA3_STAGE/deploy_v037.py" "$PA3_POD:/tmp/deploy_v037.py"
  /usr/bin/kubectl exec "$PA3_POD" -- /usr/bin/env PA3_V037_DEPLOY_SHA256="$PA3_SHA" /home/v2gao/dsc102/pa3/.venv/bin/python /tmp/deploy_v037.py
  /usr/bin/kubectl exec "$PA3_POD" -- /usr/bin/env PA3_V037_ATTEMPT="$PA3_ATTEMPT" PA3_V037_RUNTIME="$PA3_RUNTIME" /bin/bash -c 'mkdir -p "$PA3_V037_RUNTIME" || exit 1; nohup /bin/bash /home/v2gao/dsc102/pa3/setup/start_v037.sh > "$PA3_V037_RUNTIME/v037-wrapper-launch.log" 2>&1 < /dev/null &'
  date -u '+%Y-%m-%dT%H:%M:%SZ' > "$PA3_STAGE/dispatched"
  /usr/bin/kubectl get pod "$PA3_POD" -o json > "$PA3_STAGE/started-pod.json"
 fi
 if ! PA3_STATE=$(/usr/bin/timeout 40s /usr/bin/kubectl exec "$PA3_POD" -- /usr/bin/env PA3_V037_ATTEMPT="$PA3_ATTEMPT" /home/v2gao/dsc102/pa3/.venv/bin/python /home/v2gao/dsc102/pa3/setup/worker_state_v037.py);then echo "Transient worker observation failure; preserving job";sleep 60;continue;fi
 echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') state=$PA3_STATE"
 if test "$PA3_STATE" = worker_missing;then
  PA3_MISSING_COUNT=$((PA3_MISSING_COUNT+1))
  if test "$PA3_MISSING_COUNT" -ge 5;then
   /usr/bin/kubectl exec "$PA3_POD" -- /usr/bin/env PA3_V037_ATTEMPT="$PA3_ATTEMPT" PA3_V037_OBSERVE_JSON=1 /home/v2gao/dsc102/pa3/.venv/bin/python /home/v2gao/dsc102/pa3/setup/worker_state_v037.py > "$PA3_STAGE/worker-missing-evidence.json"
   echo 'Worker absent for five successful observations; archive as operational failure, never scientific completion';PA3_STATE=1
  fi
 else PA3_MISSING_COUNT=0;fi
 if [[ "$PA3_STATE" =~ ^[0-9]+$ ]];then
  PA3_SNAPSHOT_OK=0
  PA3_STAMP=$(date -u '+%Y%m%dT%H%M%SZ')
  for PA3_TRY in 1 2 3;do
   PA3_INFO="$PA3_STAGE/archive-info-$PA3_STAMP-$PA3_TRY.json"
   if /usr/bin/timeout 900s /usr/bin/kubectl exec "$PA3_POD" -- /usr/bin/env PA3_V037_ATTEMPT="$PA3_ATTEMPT" /home/v2gao/dsc102/pa3/.venv/bin/python /home/v2gao/dsc102/pa3/setup/snapshot_v037.py > "$PA3_INFO" && python3 -c 'import json,sys;v=json.load(open(sys.argv[1]));assert v["bytes"]>0 and len(v["sha256"])==64 and v["files"]>0' "$PA3_INFO";then
    if test -f "$PA3_STAGE/archive.json";then cp "$PA3_STAGE/archive.json" "$PA3_STAGE/archive-info-prior-$PA3_STAMP.json";fi
    cp "$PA3_INFO" "$PA3_STAGE/archive.json";PA3_SNAPSHOT_OK=1;break
   fi
   echo "Snapshot response failed; preserving attempt $PA3_TRY";sleep 5
  done
  test "$PA3_SNAPSHOT_OK" = 1 || { echo 'No verified snapshot metadata; preserve pod and persistent files for review';exit 1; }
  python3 "$PA3_STAGE/copy_verified_archive_v037.py" "$PA3_STAGE" "$PA3_POD" v037 > "$PA3_STAGE/archive-copy-result.json"
  /usr/bin/kubectl get pod "$PA3_POD" -o json > "$PA3_STAGE/completed-pod.json"
  /usr/bin/kubectl delete pod "$PA3_POD" --wait=true
  echo "Verified backup and released idle GPU; state=$PA3_STATE; no automatic replacement";exit 0
 fi
 sleep 60
done

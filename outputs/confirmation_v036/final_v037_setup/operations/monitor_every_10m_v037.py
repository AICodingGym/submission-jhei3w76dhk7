"""Read-only, ten-minute server monitoring for the current V036 stage.

No model fitting, pod creation/deletion, submissions or notifications to others.
Stops after verified archival or a terminal pod failure. Full checks and compact
summaries remain in private persistent login storage; Mac need not stay awake.
"""
from pathlib import Path
from datetime import datetime,timezone,timedelta
from contextlib import redirect_stdout
import os,sys,json,io,time,fcntl,subprocess,traceback
STAGE=Path.home()/'.pa3-setup-control.gty67K/v037-final-20261110'
BODY='from pathlib import Path\nfrom datetime import datetime,timezone\nimport subprocess,json\nS=Path.home()/\'.pa3-setup-control.gty67K/v037-final-20261110\';pod=(S/\'pod_name.txt\').read_text().strip();k=[\'env\',\'KUBECONFIG=/home/linux/dsmlp/08/308/v2gao/.kube/config\',\'TERM=dumb\',\'/usr/bin/kubectl\'];v=dict(utc=datetime.now(timezone.utc).isoformat(),pod=pod,dispatched=(S/\'dispatched\').exists(),guardian_log=(S/\'guardian.log\').read_text()[-3000:])\nr=subprocess.run(k+[\'get\',\'pod\',pod,\'-o\',\'json\'],capture_output=True,text=True,timeout=40);v[\'pod_query_error\']=r.stderr\nif r.returncode==0:\n j=json.loads(r.stdout);v.update(phase=j[\'status\'][\'phase\'],node=j[\'spec\'].get(\'nodeName\'),start=j[\'status\'].get(\'startTime\'),deadline_seconds=j[\'spec\'].get(\'activeDeadlineSeconds\'),conditions=j[\'status\'].get(\'conditions\'))\n if v[\'phase\']==\'Running\':\n  script="""from pathlib import Path\nimport json,os,subprocess\nP=Path(\'/home/v2gao/dsc102/pa3/gym-workspace/ventilator-pressure-prediction\');O=P/\'outputs/confirmation_v036/final_all_v037\';R=Path(\'/home/v2gao/private/.pa3-preserved-course-backups/v037-runtime\')/(os.environ[\'PA3_POD\']+\'-final\');v=dict(members={},final_manifest_exists=(O/\'final_manifest.json\').is_file(),reuse_and_cache_checks_passed=(O/\'capacity_laplace_curve/identity.json\').is_file())\nproof=O/\'course_proofs.json\'\nif proof.is_file():\n j=json.loads(proof.read_text());v[\'proof\']={k:j.get(k)for k in [\'status\',\'actual_cuda\',\'check_count\',\'numeric_runtime\',\'F_result_sha256\',\'F_audit_sha256\',\'estimated_final_seconds\']}\nd=O/\'capacity_laplace_curve\';events=[]\nif (d/\'epochs.jsonl\').is_file():\n for line in (d/\'epochs.jsonl\').read_text().splitlines()[-3:]:\n  try:events.append(json.loads(line))\n  except json.JSONDecodeError:pass\nv[\'members\'][\'capacity_laplace_curve\']=dict(record=(d/\'record.json\').is_file(),report=(d/\'report.json\').is_file(),events=events)\nif (O/\'final_manifest.json\').is_file():\n j=json.loads((O/\'final_manifest.json\').read_text());v[\'final_summary\']={k:j.get(k)for k in [\'status\',\'all_training_breaths\',\'submission\',\'submission_sha256\',\'completed_utc\',\'elapsed_seconds\']}\nv[\'logs\']={p.name:p.read_text()[-2000:]for p in R.glob(\'*\')if p.is_file()and p.suffix in [\'.log\',\'.txt\']}\nr=subprocess.run([\'nvidia-smi\',\'--query-gpu=name,utilization.gpu,memory.used,memory.total\',\'--format=csv,noheader\'],capture_output=True,text=True);v[\'GPU\']=r.stdout\nr=subprocess.run([\'/home/v2gao/dsc102/pa3/.venv/bin/python\',\'/home/v2gao/dsc102/pa3/setup/worker_state_v037.py\'],env=dict(os.environ,PA3_V037_ATTEMPT=os.environ[\'PA3_POD\']+\'-final\',PA3_V037_OBSERVE_JSON=\'1\'),capture_output=True,text=True);v[\'worker_state\']=r.stdout;v[\'worker_error\']=r.stderr\nprint(json.dumps(v))"""\n  r=subprocess.run(k+[\'exec\',pod,\'--\',\'env\',\'PA3_POD=\'+pod,\'/home/v2gao/dsc102/pa3/.venv/bin/python\',\'-c\',script],capture_output=True,text=True,timeout=60);v[\'container_error\']=r.stderr;v[\'container_returncode\']=r.returncode\n  if r.returncode==0:v[\'course\']=json.loads(r.stdout)\nprint(json.dumps(v))\n'
lock=(STAGE/'monitor-every10.lock').open('a+')
try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
except BlockingIOError:raise SystemExit('An existing ten-minute monitor already holds this lock')
(STAGE/'monitor-every10.pid').write_text(str(os.getpid())+'\n')
OUT=STAGE/'monitor-every10';OUT.mkdir(exist_ok=True)
INTERVAL=600
def append(name,value):
 with (OUT/name).open('a')as f:f.write(json.dumps(value,sort_keys=True)+'\n');f.flush();os.fsync(f.fileno())
def observe():
 with redirect_stdout(io.StringIO())as capture:exec(compile(BODY,'reviewed_readonly_monitor_body','exec'),{})
 return json.loads(capture.getvalue())
def guardian_alive():
 pid=int((STAGE/'guardian.pid').read_text())
 r=subprocess.run(['ps','-p',str(pid),'-o','args='],capture_output=True,text=True)
 return r.returncode==0 and str(STAGE/'guardian_v037.sh') in r.stdout
now=datetime.now(timezone.utc);next_due=time.monotonic()+INTERVAL
append('events.jsonl',dict(event='monitor_started',utc=now.isoformat(),pid=os.getpid(),interval_seconds=INTERVAL,next_check_utc=(now+timedelta(seconds=INTERVAL)).isoformat(),read_only=True))
while True:
 time.sleep(max(0,next_due-time.monotonic()));started=time.monotonic();now=datetime.now(timezone.utc)
 try:
  v=observe();stamp=now.strftime('%Y%m%dT%H%M%SZ');tmp=OUT/(stamp+'.json.tmp');tmp.write_text(json.dumps(v,indent=2)+'\n');os.replace(tmp,OUT/(stamp+'.json'))
  course=v.get('course')or{};members={}
  for name,r in (course.get('members')or{}).items():
   epochs=[e.get('epoch',0)for e in r.get('events',[]) if e.get('event')=='epoch'];members[name]=dict(complete=bool(r.get('record')),epoch=max(epochs)if epochs else None)
  verification=STAGE/'archive-verification.json';archived=verification.is_file() and json.loads(verification.read_text()).get('verified',False)
  runtime=Path.home()/'.pa3-preserved-course-backups/v037-runtime'/(v['pod']+'-final');exitfile=runtime/'v037-exit-code.txt';exitcode=exitfile.read_text().strip()if exitfile.is_file()else None
  summary=dict(utc=now.isoformat(),pod=v.get('pod'),phase=v.get('phase'),start=v.get('start'),members=members,GPU=course.get('GPU'),archived=archived,exitcode=exitcode,guardian_alive=guardian_alive(),final_summary=course.get('final_summary'),proof=course.get('proof'),reuse_and_cache_checks_passed=course.get('reuse_and_cache_checks_passed'),error=v.get('pod_query_error')or v.get('container_error'),full_observation=str(OUT/(stamp+'.json')))
  append('summary.jsonl',summary);print(json.dumps(summary),flush=True)
  if archived or v.get('phase')in ['Failed','Succeeded']:
   append('events.jsonl',dict(event='monitor_finished',utc=datetime.now(timezone.utc).isoformat(),reason='verified_archive'if archived else 'terminal_pod',exitcode=exitcode));break
 except Exception as e:
  value=dict(utc=now.isoformat(),monitor_error=repr(e),traceback=traceback.format_exc());append('errors.jsonl',value);print(json.dumps(value),flush=True)
 next_due+=INTERVAL
 if next_due<time.monotonic():next_due=time.monotonic()+INTERVAL

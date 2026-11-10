#!/bin/bash
ssh -S /Users/generalclasher/Documents/dsc102/pa3/.datahub-ssh/control -o BatchMode=yes -o ConnectTimeout=10 -o UserKnownHostsFile=/Users/generalclasher/Documents/dsc102/pa3/.datahub-ssh/known_hosts -o StrictHostKeyChecking=yes v2gao@dsmlp-login.ucsd.edu 'python3 -' <<'PY'
from pathlib import Path
from datetime import datetime,timezone
import subprocess,json
S=Path.home()/'.pa3-setup-control.gty67K/v037-final-20261110';pod=(S/'pod_name.txt').read_text().strip();k=['env','KUBECONFIG=/home/linux/dsmlp/08/308/v2gao/.kube/config','TERM=dumb','/usr/bin/kubectl'];v=dict(utc=datetime.now(timezone.utc).isoformat(),pod=pod,dispatched=(S/'dispatched').exists(),guardian_log=(S/'guardian.log').read_text()[-3000:])
r=subprocess.run(k+['get','pod',pod,'-o','json'],capture_output=True,text=True,timeout=40);v['pod_query_error']=r.stderr
if r.returncode==0:
 j=json.loads(r.stdout);v.update(phase=j['status']['phase'],node=j['spec'].get('nodeName'),start=j['status'].get('startTime'),deadline_seconds=j['spec'].get('activeDeadlineSeconds'),conditions=j['status'].get('conditions'))
 if v['phase']=='Running':
  script="""from pathlib import Path
import json,os,subprocess
P=Path('/home/v2gao/dsc102/pa3/gym-workspace/ventilator-pressure-prediction');O=P/'outputs/confirmation_v036/final_all_v037';R=Path('/home/v2gao/private/.pa3-preserved-course-backups/v037-runtime')/(os.environ['PA3_POD']+'-final');v=dict(members={},final_manifest_exists=(O/'final_manifest.json').is_file(),reuse_and_cache_checks_passed=(O/'capacity_laplace_curve/identity.json').is_file())
proof=O/'course_proofs.json'
if proof.is_file():
 j=json.loads(proof.read_text());v['proof']={k:j.get(k)for k in ['status','actual_cuda','check_count','numeric_runtime','F_result_sha256','F_audit_sha256','estimated_final_seconds']}
d=O/'capacity_laplace_curve';events=[]
if (d/'epochs.jsonl').is_file():
 for line in (d/'epochs.jsonl').read_text().splitlines()[-3:]:
  try:events.append(json.loads(line))
  except json.JSONDecodeError:pass
v['members']['capacity_laplace_curve']=dict(record=(d/'record.json').is_file(),report=(d/'report.json').is_file(),events=events)
if (O/'final_manifest.json').is_file():
 j=json.loads((O/'final_manifest.json').read_text());v['final_summary']={k:j.get(k)for k in ['status','all_training_breaths','submission','submission_sha256','completed_utc','elapsed_seconds']}
v['logs']={p.name:p.read_text()[-2000:]for p in R.glob('*')if p.is_file()and p.suffix in ['.log','.txt']}
r=subprocess.run(['nvidia-smi','--query-gpu=name,utilization.gpu,memory.used,memory.total','--format=csv,noheader'],capture_output=True,text=True);v['GPU']=r.stdout
r=subprocess.run(['/home/v2gao/dsc102/pa3/.venv/bin/python','/home/v2gao/dsc102/pa3/setup/worker_state_v037.py'],env=dict(os.environ,PA3_V037_ATTEMPT=os.environ['PA3_POD']+'-final',PA3_V037_OBSERVE_JSON='1'),capture_output=True,text=True);v['worker_state']=r.stdout;v['worker_error']=r.stderr
print(json.dumps(v))"""
  r=subprocess.run(k+['exec',pod,'--','env','PA3_POD='+pod,'/home/v2gao/dsc102/pa3/.venv/bin/python','-c',script],capture_output=True,text=True,timeout=60);v['container_error']=r.stderr;v['container_returncode']=r.returncode
  if r.returncode==0:v['course']=json.loads(r.stdout)
print(json.dumps(v))

PY

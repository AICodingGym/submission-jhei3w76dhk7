#!/bin/bash
ssh -S /Users/generalclasher/Documents/dsc102/pa3/.datahub-ssh/control -o BatchMode=yes -o ConnectTimeout=10 -o UserKnownHostsFile=/Users/generalclasher/Documents/dsc102/pa3/.datahub-ssh/known_hosts -o StrictHostKeyChecking=yes v2gao@dsmlp-login.ucsd.edu 'python3 -' <<'PY'
import pathlib,subprocess,json,datetime
S=pathlib.Path.home()/'.pa3-setup-control.gty67K/v036-F-remaining_two-20261109';pod=(S/'pod_name.txt').read_text().strip();k=['env','KUBECONFIG=/home/linux/dsmlp/08/308/v2gao/.kube/config','TERM=dumb','/usr/bin/kubectl'];v=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),pod=pod,guardian_log=(S/'guardian.log').read_text()[-5000:],dispatched=(S/'dispatched').exists(),started_pod_record=(S/'started-pod.json').exists());r=subprocess.run(k+['get','pod',pod,'-o','json'],capture_output=True,text=True);v['pod_query_error']=r.stderr
if r.returncode==0:
 j=json.loads(r.stdout);v.update(phase=j['status']['phase'],start=j['status'].get('startTime'),node=j['spec'].get('nodeName'),deadline_seconds=j['spec'].get('activeDeadlineSeconds'),container_status=j['status'].get('containerStatuses'))
 if j['status']['phase']=='Running':
  code="""from pathlib import Path
import json,os,subprocess
P=Path('/home/v2gao/dsc102/pa3/gym-workspace/ventilator-pressure-prediction');O=P/'outputs/confirmation_v036';R=Path('/home/v2gao/private/.pa3-preserved-course-backups/v036-runtime')/(os.environ['PA3_POD']+'-remaining_two-r3');v=dict(f_split_exists=(O/'F_split.json').exists(),confirmation_result_exists=(O/'confirmation_result.json').exists(),proofs={},members={})
for n in ['course_proofs.json','pruning_course_proofs.json']:
 p=O/n
 if p.is_file():
  j=json.loads(p.read_text());v['proofs'][n]={k:j.get(k)for k in ['status','actual_cuda','check_count','exact_resume','native_inference','numeric_runtime','driver_source_code_sha256','projected_stage_seconds']}
for d in sorted((O/'F_models').glob('*')):
 row=dict(record=(d/'record.json').exists(),report=(d/'report.json').exists())
 if (d/'epochs.jsonl').is_file():row['events']=[json.loads(x)for x in(d/'epochs.jsonl').read_text().splitlines()[-2:]]
 v['members'][d.name]=row
if (O/'F_split.json').is_file():
 j=json.loads((O/'F_split.json').read_text());old=json.loads((O/'failed_schema_attempt_20261109/F_split.json').read_text());v['same_known_split_after_key_correction']=j['indices']['F_fit']==old['indices']['E_fit'] and j['indices']['F_validation']==old['indices']['E_validation'] and j['group_hashes']['F_fit']==old['group_hashes']['E_fit'] and j['group_hashes']['F_validation']==old['group_hashes']['E_validation']
v['logs']={p.name:p.read_text()[-2500:]for p in R.glob('*')if p.is_file() and p.suffix in ['.log','.txt']}
r=subprocess.run(['nvidia-smi','--query-gpu=name,utilization.gpu,memory.used,memory.total','--format=csv,noheader'],capture_output=True,text=True);v['GPU']=r.stdout;v['gpu_error']=r.stderr
r=subprocess.run(['/home/v2gao/dsc102/pa3/.venv/bin/python','/home/v2gao/dsc102/pa3/setup/worker_state_v036.py'],env=dict(os.environ,PA3_V036_STAGE='remaining_two',PA3_V036_ATTEMPT=os.environ['PA3_POD']+'-remaining_two-r3',PA3_V036_OBSERVE_JSON='1'),capture_output=True,text=True);v['worker_state']=r.stdout;v['worker_error']=r.stderr
print(json.dumps(v))"""
  r=subprocess.run(k+['exec',pod,'--','env','PA3_POD='+pod,'/home/v2gao/dsc102/pa3/.venv/bin/python','-c',code],capture_output=True,text=True,timeout=60);v['container_returncode']=r.returncode;v['container_error']=r.stderr
  if r.returncode==0:v['course']=json.loads(r.stdout)
print(json.dumps(v))
PY

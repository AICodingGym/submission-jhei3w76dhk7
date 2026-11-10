"""Build conditional final deployment only after complete independently passed F."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,tarfile,subprocess,ast
P=Path.cwd();H=P/'outputs/confirmation_v036/final_v037_setup/operations';payload=H/'v037-deploy.tar.gz';assert not payload.exists()
def read(p):return json.loads(Path(p).read_text())
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def code(p):return '\n'.join(''.join(c['source'])for c in read(p)['cells']if c['cell_type']=='code')
def ch(p):return hashlib.sha256(code(p).encode()).hexdigest()
freeze=read(P/'research/freeze_final_v037.json');assert ch(P/freeze['notebook'])==freeze['source_code_sha256']=='68a4aa07834bd8cd365058631f01279620117c7a896657c9a3029622e3d4ed64'
F='outputs/confirmation_v036/confirmation_result.json';A='research/confirmation_review_v036.json';result=read(P/F);audit=read(P/A);gate=read(P/'research/final_activation_gate_v037.json')
assert result['status']=='complete'and result['passed']and audit['status']=='passed'and audit['passed']and audit['confirmation_result_sha256']==sha(P/F)
assert gate['status']=='passed_actual_final_prerequisite_gate'and gate['gate']['F_result_sha256']==sha(P/F)and gate['gate']['F_audit_sha256']==sha(P/A)
assert result['gain']>0 and result['interval']['high']<0
assert ch(P/'confirmation_v036.ipynb')==result['source_code_sha256']
assert ch(P/freeze['component_preflight']['notebook'])==freeze['component_preflight']['code_sha256']
project=set(['confirmation_v036.ipynb',freeze['notebook'],freeze['component_preflight']['notebook'],'research/freeze_final_v037.json','research/final_preflight_review_v037.json','research/final_gate_negative_review_v037.json','research/final_activation_gate_v037.json','research/confirmation_protocol_v036.json','research/confirmation_selection_v036.json',F,A,'outputs/confirmation_v036/locked_before_F.json','research/laplace_components_v029.ipynb','research/laplace_preflight_v029.ipynb','research/final_operations_review_v037.json'])
for name,h in freeze['source_dependencies'].items():assert ch(P/name)==h;project.add(name)
assert ch(P/'research/laplace_components_v029.ipynb')==freeze['laplace_component_code_sha256']
tree=ast.parse(code(P/'final_fit_v011.ipynb'));constants={}
for n in tree.body:
 if isinstance(n,ast.Assign)and len(n.targets)==1 and isinstance(n.targets[0],ast.Name):
  try:constants[n.targets[0].id]=ast.literal_eval(n.value)
  except (ValueError,TypeError):pass
for name,h in constants['V011_FINAL_COMPONENTS'].items():assert ch(P/'research'/name)==h;project.add('research/'+name)
required={};visited=set();queue=[]
def normalize(value):
 if not isinstance(value,str)or len(value)>2000:return None
 marker='/ventilator-pressure-prediction/';rel=value.split(marker,1)[1]if marker in value else value
 candidates=[P/rel]
 if '/'not in rel:candidates+=[P/'research'/rel,P/'data'/rel]
 for p in candidates:
  if p.is_file()and p.resolve().is_relative_to(P) and p.name!='baseline_v001.ipynb':return str(p.relative_to(P))
 return None
def add(rel):
 if rel in visited:return
 visited.add(rel);assert len(visited)<600,'Unexpected prerequisite graph expansion'
 p=P/rel;assert p.is_file(),rel
 if p.suffix=='.ipynb':project.add(rel)
 elif p.suffix=='.json'and p.stat().st_size<2000000:project.add(rel);queue.append(rel)
 else:required[rel]=sha(p)
def walk(value):
 if isinstance(value,dict):
  for v in value.values():walk(v)
 elif isinstance(value,list):
  for v in value:walk(v)
 elif isinstance(value,str):
  rel=normalize(value)
  if rel and Path(rel).suffix in ['.json','.pt','.npy','.npz','.csv','.ipynb']:add(rel)
explicit=['data/train.csv','data/test.csv','data/sample_submission.csv','outputs/confirmation_v011/locked_before_D.json','outputs/confirmation_v011/D_split.json','outputs/confirmation_v011/final_all/final_manifest.json','outputs/improvements_v005/confirmation_round1/final_all/final_manifest.json','outputs/confirmation_v014/final_all_v018/submission.csv','outputs/improvements_v005/sequence/split_breath_ids.npz',F,A,'outputs/confirmation_v036/F_split.json','outputs/confirmation_v036/F_row_ids.npy','outputs/confirmation_v036/F_fit_pressure_codebook.npy','outputs/confirmation_v036/baseline_F_predictions.npy','outputs/confirmation_v036/candidate_F_predictions.npy','outputs/confirmation_v036/predictions_locked_before_F_pressure.json','outputs/confirmation_v036/F_models/capacity_laplace_curve/report.json']
for name in result['records']:explicit.append('outputs/confirmation_v036/F_models/'+name+'/record.json')
for name in read(P/(constants['V011_PRIOR_DIR']+'/final_manifest.json'))['members']:
 for prefix in ['record_','report_']:explicit.append(constants['V011_PRIOR_DIR']+'/'+prefix+name+'.json')
for rel in explicit:add(rel)
for rel in list(project):
 if rel.endswith('.json'):add(rel)
# Follow only actual production-consumer dependencies; legacy validation/HPO
# references inside old provenance locks are historical and are not re-executed.
accepted=read(P/'outputs/confirmation_v011/final_all/final_manifest.json')
prior=read(P/(constants['V011_PRIOR_DIR']+'/final_manifest.json'))
for obj in [accepted['members'],accepted['prediction_members'],prior['model_files'],prior['model_records'],result['records'],result['prediction_artifacts']]:walk(obj)
for value in [accepted['test_row_ids_file'],accepted['submission_file'],prior['submission_file'],prior['lock_file']]:
 rel=normalize(value);assert rel is not None,value;add(rel)

for rel in list(project):required.pop(rel,None)
project_files={rel:sha(P/rel)for rel in sorted(project)};project_code_hashes={rel:ch(P/rel)for rel in sorted(project)if rel.endswith('.ipynb')}
helpers=['build_payload_v037.py','deploy_v037.py','execute_final_v037.py','course_preflight_v037.py','start_v037.sh','snapshot_v037.py','verify_archive_v037.py','copy_verified_archive_v037.py','guardian_v037.sh','worker_state_v037.py']
for name in helpers:
 if name.endswith('.py'):compile((H/name).read_text(),name,'exec')
 else:subprocess.run(['/bin/bash','-n',str(H/name)],check=True)
setup={name:sha(H/name)for name in helpers}
pins=dict(schema='v037-confirmed-final-deployment-v1',created_utc=datetime.now(timezone.utc).isoformat(),freeze=freeze,F_result_sha256=sha(P/F),F_audit_sha256=sha(P/A),project_files=project_files,project_code_hashes=project_code_hashes,required_existing_files=required,setup_files=setup,resources=dict(GPU=1,CPU_limit=4,RAM_limit_Gi=16,ordinary_lease_seconds=21600),no_automatic_submission=True,no_automatic_resource_allocation=True)
with(H/'v037-pins.json').open('x')as f:f.write(json.dumps(pins,indent=2)+'\n')
with tarfile.open(payload,'w:gz')as t:
 for name in project_files:t.add(P/name,arcname='project/'+name,recursive=False)
 for name in setup:t.add(H/name,arcname='setup/'+name,recursive=False)
 t.add(H/'v037-pins.json',arcname='setup/v037-pins.json',recursive=False)
with tarfile.open(payload)as t:members=t.getmembers();assert len(set(m.name for m in members))==len(members)and all(m.isfile()for m in members)
info=dict(status='prepared_after_passed_complete_F_and_gate',utc=datetime.now(timezone.utc).isoformat(),payload_sha256=sha(payload),payload_bytes=payload.stat().st_size,payload_members=len(members),pins_sha256=sha(H/'v037-pins.json'),F_result_sha256=sha(P/F),F_audit_sha256=sha(P/A),source_code_sha256=freeze['source_code_sha256'],existing_prerequisite_files=len(required),existing_prerequisite_bytes=sum((P/n).stat().st_size for n in required),project_files=len(project_files),no_GPU_requested=True,no_final_fit_started=True)
with(H/'payload-info.json').open('x')as f:f.write(json.dumps(info,indent=2)+'\n')
print(json.dumps(info,indent=2))

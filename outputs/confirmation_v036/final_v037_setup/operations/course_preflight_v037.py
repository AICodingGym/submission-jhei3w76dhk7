"""Actual CUDA, frozen-source, confirmed-F and synthetic final-consumer proof."""
import os,json,hashlib,fcntl,datetime,platform,subprocess,time
from pathlib import Path
os.environ['PA3_RUN_FINAL_V037']='0'
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
import torch,numpy as np
P=Path.cwd();S=P.parents[1]/'setup';O=P/'outputs/confirmation_v036/final_all_v037';O.mkdir(parents=True,exist_ok=True)
pins=json.loads((S/'v037-pins.json').read_text());freeze=pins['freeze']
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def code(p):return '\n'.join(''.join(c['source'])for c in json.loads(Path(p).read_text())['cells']if c['cell_type']=='code')
def codehash(p):return hashlib.sha256(code(p).encode()).hexdigest()
assert codehash(P/freeze['notebook'])==freeze['source_code_sha256']==os.environ['PA3_V037_SOURCE_SHA256']
for rel,h in pins['project_files'].items():
 if rel.endswith('.ipynb'):assert codehash(P/rel)==pins['project_code_hashes'][rel],'Notebook code changed: '+rel
 else:assert sha(P/rel)==h,'Pinned project prerequisite changed: '+rel
for rel,h in pins['required_existing_files'].items():assert sha(P/rel)==h,'Existing prerequisite changed: '+rel
for rel,h in pins['setup_files'].items():assert sha(S/rel)==h,'Operational helper changed: '+rel
assert torch.cuda.is_available();torch.set_num_threads(4)
runtime=dict(python=platform.python_version(),numpy=np.__version__,torch=str(torch.__version__),cuda=torch.version.cuda,cudnn=torch.backends.cudnn.version(),device=torch.cuda.get_device_name(),capability=list(torch.cuda.get_device_capability()))
proof_file=O/'course_proofs.json'
if proof_file.exists():
 prior=json.loads(proof_file.read_text());assert prior['status']=='passed'and prior['actual_cuda']and prior['driver_source_code_sha256']==freeze['source_code_sha256']and prior['F_result_sha256']==pins['F_result_sha256']and prior['F_audit_sha256']==pins['F_audit_sha256']and prior['numeric_runtime']==runtime and all(prior['checks'].values());assert sha(P/prior['proof_file'])==prior['proof_file_sha256'];print('Exact final-consumer CUDA proof reused after full prerequisite verification');raise SystemExit(0)
lock=(P/'outputs/.v011_gpu.lock').open('a+');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
try:
 # A bounded storage probe exceeds the measured final checkpoint/prediction/archive footprint.
 storage=[]
 for directory in [S,Path(os.environ['PA3_V037_RUNTIME'])]:
  probe=directory/'v037-owned-write-probe.bin';assert not probe.exists()
  try:
   with probe.open('xb')as f:
    block=b'v037-storage-probe\n'*58254
    for _ in range(256):f.write(block)
    f.flush();os.fsync(f.fileno())
   storage.append(dict(directory=str(directory),bytes=probe.stat().st_size))
  finally:
   if probe.exists():probe.unlink()
 ns={'__name__':'v037_final_gate_preflight'};exec(compile(code(P/freeze['notebook']),freeze['notebook'],'exec'),ns)
 _,gate=ns['v037_confirmation_gate'](P,pins['F_result_sha256'],pins['F_audit_sha256'])
 descriptor=freeze['component_preflight'];assert codehash(P/descriptor['notebook'])==descriptor['code_sha256'];ns={};exec(compile(code(P/descriptor['notebook']),descriptor['notebook'],'exec'),ns)
 proof=ns[descriptor['function']](P,O/'preflight_cuda',device='cuda');assert proof['status']=='passed'and proof['actual_cuda']and all(proof['checks'].values())
 selected=json.loads((P/'outputs/confirmation_v036/F_models/capacity_laplace_curve/report.json').read_text());projection=selected['elapsed_seconds']*(266/213)*1.15+900
 assert projection+1800<=21600,'Final budget plus conservative reserve exceeds ordinary lease'
 bound=dict(proof,created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),driver_source_code_sha256=freeze['source_code_sha256'],F_result_sha256=pins['F_result_sha256'],F_audit_sha256=pins['F_audit_sha256'],confirmed_F_gate=gate,numeric_runtime=runtime,actual_cuda=True,source_and_prerequisite_integrity_verified=True,proof_file=str((O/'preflight_cuda/proof.json').relative_to(P)),proof_file_sha256=sha(O/'preflight_cuda/proof.json'),storage_write_probes=storage,estimated_final_seconds=projection,lease_reserve_seconds=1800,no_approved_data_optimizer_updates=True)
 with proof_file.open('x')as f:f.write(json.dumps(bound,indent=2,allow_nan=False)+'\n')
 print(json.dumps(bound,indent=2))
finally:fcntl.flock(lock,fcntl.LOCK_UN);lock.close()

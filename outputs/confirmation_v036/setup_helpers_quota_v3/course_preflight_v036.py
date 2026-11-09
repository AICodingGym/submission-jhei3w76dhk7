"""Require actual CUDA notebook proofs before any approved-data training."""
import os,json,hashlib,fcntl,datetime,subprocess,platform
from pathlib import Path
# Proofs import the real guarded confirmation notebook; this child must never start it.
os.environ['PA3_RUN_V036']='0'
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
import torch
import numpy as np
P=Path.cwd();S=P.parents[1]/'setup';O=P/'outputs/confirmation_v036';O.mkdir(parents=True,exist_ok=True)
pins=json.loads((S/'v036-pins.json').read_text());freeze=pins['freeze']
def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b)
    return h.hexdigest()
def code(path):return '\n'.join(''.join(c['source']) for c in json.loads(Path(path).read_text())['cells'] if c['cell_type']=='code')
def codehash(path):return hashlib.sha256(code(path).encode()).hexdigest()
assert codehash(P/freeze['notebook'])==freeze['source_code_sha256']==os.environ['PA3_V036_SOURCE_SHA256']
assert sha(P/freeze['protocol_file'])==freeze['protocol_sha256']
for path,digest in pins['project_files'].items():
    if path.endswith('.ipynb'):assert codehash(P/path)==pins['project_code_hashes'][path],'Notebook code changed: '+path
    else:assert sha(P/path)==digest,'Deployment input changed: '+path
for path,digest in pins['required_existing_files'].items():assert sha(P/path)==digest,'Course data/input changed: '+path
for path,digest in pins['setup_files'].items():assert sha(S/path)==digest,'Operational helper changed: '+path
assert torch.cuda.is_available(),'Actual course CUDA is required'
torch.set_num_threads(4)
runtime=dict(python=platform.python_version(),numpy=np.__version__,torch=str(torch.__version__),cuda=torch.version.cuda,cudnn=torch.backends.cudnn.version(),device=torch.cuda.get_device_name(),capability=list(torch.cuda.get_device_capability()))
proof_file=O/'course_proofs.json';pruning_proof_file=O/'pruning_course_proofs.json'
if proof_file.exists() or pruning_proof_file.exists():
    assert proof_file.exists() and pruning_proof_file.exists(),'Partial proof publication requires review; preserve all files'
    for target in [proof_file,pruning_proof_file]:
        prior=json.loads(target.read_text())
        assert prior['status']=='passed' and prior['driver_source_code_sha256']==freeze['source_code_sha256'] and prior['protocol_sha256']==freeze['protocol_sha256']
        assert prior['numeric_runtime']==runtime,'CUDA proof runtime changed; review a new proof directory before resuming'
        for relative,digest in prior['proof_file_sha256'].items():assert sha(P/relative)==digest
        assert prior['actual_cuda'] and all(prior['checks'].values())
    print('Existing exact CUDA proofs verified; not repeated')
    raise SystemExit(0)
lock=(P/'outputs/.v011_gpu.lock').open('a+');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
try:
    ns={'__name__':'v036_course_pruning_proof'}
    pruning_notebook=P/'research/pruning_workflow_preflight_v025.ipynb'
    exec(compile(code(pruning_notebook),str(pruning_notebook),'exec'),ns)
    pruning=ns['run_pruning_preflight_v025'](P,O/'preflight_pruning_cuda',device='cuda')
    assert pruning['status']=='passed' and pruning['check_count']>=32 and all(pruning['checks'].values())
    assert pruning['actual_cuda'] and pruning['exact_pruned_resume'] and pruning['next_planned_experiment_executed']
    descriptor=freeze['component_preflight'];component_notebook=P/descriptor['notebook']
    assert codehash(component_notebook)==descriptor['code_sha256']
    ns={'__name__':'v036_course_component_proof'}
    exec(compile(code(component_notebook),str(component_notebook),'exec'),ns)
    component=ns[descriptor['function']](P,O/'preflight_component_cuda',device='cuda',**descriptor.get('kwargs',{}))
    assert component['status']=='passed' and all(component['checks'].values()) and component['actual_cuda']
    assert component['exact_resume'] and component['native_inference']
    files=[O/'preflight_pruning_cuda/proof.json',O/'preflight_component_cuda/proof.json']
    assert all(p.is_file() for p in files),'Notebook proofs must persist their exact proof.json'
    smi_text=subprocess.run(['nvidia-smi'],capture_output=True,text=True,check=True).stdout
    (O/'nvidia-smi-course-preflight.txt').write_text(smi_text)
    context=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        driver_source_code_sha256=freeze['source_code_sha256'],protocol_sha256=freeze['protocol_sha256'],
        proof_file_sha256={str(p.relative_to(P)):sha(p) for p in files},
        deployment_project_code_hashes=pins['project_code_hashes'],
        proof_notebook_code_sha256={str(pruning_notebook.relative_to(P)):codehash(pruning_notebook),descriptor['notebook']:codehash(component_notebook)},
        numeric_runtime=runtime,actual_cuda=True,approved_data_training_started=False,source_and_data_integrity_verified=True)
    bound_pruning=dict(pruning,**context);bound_component=dict(component,**context)
    with pruning_proof_file.open('x') as f:f.write(json.dumps(bound_pruning,indent=2,allow_nan=False)+'\n')
    with proof_file.open('x') as f:f.write(json.dumps(bound_component,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(pruning=bound_pruning,component=bound_component),indent=2))
finally:
    fcntl.flock(lock,fcntl.LOCK_UN);lock.close()

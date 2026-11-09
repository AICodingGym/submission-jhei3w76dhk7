"""Build only after reviewed V036 source/protocol/preflight pins are frozen.

This local operational helper does not run notebooks, allocate, deploy, train,
submit or contact DataHub. Approved raw data remains in persistent course storage.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,tarfile,subprocess
P=Path.cwd();H=P/'outputs/confirmation_v036/setup_helpers_quota_v4'
payload=H/'v036-deploy.tar.gz'
assert not payload.exists(),'Preserve existing frozen payload'
def read(path):return json.loads(Path(path).read_text())
def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b)
    return h.hexdigest()
def code(path):return '\n'.join(''.join(c['source']) for c in read(path)['cells'] if c['cell_type']=='code')
def codehash(path):return hashlib.sha256(code(path).encode()).hexdigest()
def component_path(name):
    if '/' in name or (P/name).is_file():return name
    return 'research/'+name
freeze_path=P/'research/freeze_v036.json';freeze=read(freeze_path)
assert freeze.get('status') in ('frozen_before_F_split_or_pressure','corrected_schema_before_any_F_fit_or_validation_outcome'),'A reviewed explicit source/protocol freeze is required'
for key in ['notebook','source_code_sha256','protocol_file','protocol_sha256','component_preflight']:assert key in freeze,'Missing freeze field: '+key
assert freeze['notebook']=='confirmation_v036.ipynb'
assert codehash(P/freeze['notebook'])==freeze['source_code_sha256']
assert sha(P/freeze['protocol_file'])==freeze['protocol_sha256']
plan=read(P/freeze['protocol_file'])
preflight=freeze['component_preflight']
assert preflight['function']=='run_confirmation_preflight_v036'
assert preflight['notebook']=='research/confirmation_preflight_v036.ipynb'
assert codehash(P/preflight['notebook'])==preflight['code_sha256']
assert isinstance(preflight.get('kwargs',{}),dict)
assert set(preflight.get('kwargs',{})).issubset({'deep_spec'}),'Operational component API changed; review helper before use'
policy_path='research/pruning_policy_v025.json';policy=read(P/policy_path)
assert policy.get('enabled') and policy['origin']=='reviewed_completed_A_validation_curves'
assert sha(P/policy_path)=='0acdfa933d54fbae1e7728e2f8982bdae3f4227c6bd5187979bcd38b67e5fc88','Calibrated policy changed; review before deployment'
files=set();required={}
for name,digest in plan['input_hashes'].items():
    assert sha(P/name)==digest,'Frozen plan input changed: '+name
    if name.startswith('data/'):required[name]=digest
    else:files.add(name)
for name,digest in policy['reference_file_hashes'].items():
    assert sha(P/name)==digest,'Pruning reference changed: '+name
    files.add(name)
for name,digest in plan['component_code_hashes'].items():
    name=component_path(name);assert codehash(P/name)==digest,'Component changed: '+name;files.add(name)
files.update([freeze['notebook'],freeze['protocol_file'],'research/freeze_v036.json',preflight['notebook'],
    'research/feature_components_v005.ipynb','research/sequence_components_v005.ipynb','research/training_components_v008.ipynb',
    'research/pruning_components_v025.ipynb','research/training_workflow_v025.ipynb','research/pruning_workflow_preflight_v025.ipynb',
    policy_path,'research/pruning_calibration_review_v025.json'])
for name in freeze.get('additional_project_files',[]):files.add(name)
files.update(['research/operations_streaming_repair_review_v036.json','research/streaming_archive_validation_v036.json'])
project={name:sha(P/name) for name in sorted(files)}
project_codes={name:codehash(P/name) for name in sorted(files) if name.endswith('.ipynb')}
helpers=['build_payload_v036.py','execute_screen_v036.py','start_v036.sh','course_preflight_v036.py','snapshot_v036.py',
    'verify_archive_v036.py','deploy_v036.py','guardian_v036.sh','copy_verified_archive_v036.py','worker_state_v036.py']
for name in helpers:
    text=(H/name).read_text()
    if name.endswith('.py'):compile(text,name,'exec')
    else:subprocess.run(['/bin/bash','-n',str(H/name)],check=True)
setup={name:sha(H/name) for name in helpers}
pins=dict(schema='v036-reviewed-deployment-pins-v1',created_utc=datetime.now(timezone.utc).isoformat(),freeze=freeze,
    project_files=project,project_code_hashes=project_codes,required_existing_files=required,setup_files=setup,
    resources=dict(GPU=1,CPU_limit=4,RAM_limit_Gi=16,ordinary_lease_seconds=21600,training_threads=4),
    actual_CUDA_pruning_and_component_proofs_required_before_training=True,
    no_automatic_submission=True,no_automatic_resource_allocation=True,archive_individual_hash_verification_required_before_GPU_release=True)
pinpath=H/'v036-pins.json'
with pinpath.open('x') as f:f.write(json.dumps(pins,indent=2,allow_nan=False)+'\n')
with tarfile.open(payload,'w:gz') as tar:
    for name in project:tar.add(P/name,arcname='project/'+name,recursive=False)
    for name in setup:tar.add(H/name,arcname='setup/'+name,recursive=False)
    tar.add(pinpath,arcname='setup/v036-pins.json',recursive=False)
with tarfile.open(payload,'r:gz') as tar:
    members=tar.getmembers();assert len({m.name for m in members})==len(members) and all(m.isfile() for m in members)
info=dict(status='prepared_not_dispatched',created_utc=datetime.now(timezone.utc).isoformat(),
    source_code_sha256=freeze['source_code_sha256'],protocol_sha256=freeze['protocol_sha256'],
    payload_file=str(payload.relative_to(P)),payload_sha256=sha(payload),payload_bytes=payload.stat().st_size,payload_members=len(members),
    pins_sha256=sha(pinpath),GPU_resource_requests=0,approved_data_fits=0,actual_GPU_proofs_completed=False,
    required_existing_files=required,pruning_reference_file_count=len(policy['reference_file_hashes']),
    syntax_payload_checked=True,modeling_code_in_notebooks_only=True,
    archive_retry_provenance='Preserved V036 failed-timeout helpers. Forward-only tar verification plus verified shared-home hardlinks; 900s verifier timeout with preserved failures. GPU release still requires every safe member hash. No automatic allocation or submission.')
with (H/'payload-info.json').open('x') as f:f.write(json.dumps(info,indent=2,allow_nan=False)+'\n')
print(json.dumps(info,indent=2))

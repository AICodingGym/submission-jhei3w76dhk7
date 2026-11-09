"""Operational fixture: private snapshot, exact archive copy, missing-worker states."""
from pathlib import Path
import tempfile,json,runpy,os,subprocess,hashlib,shutil,types
P=Path.cwd();H=P/'outputs/confirmation_v036/setup_helpers_quota_v3';checks={}
def ok(k,v):
 assert v,k;checks[k]=True
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
w=runpy.run_path(str(H/'worker_state_v036.py'));c=w['classify']
ok('active_worker_pending',c(None,[],[{'pid':1}])=='pending')
ok('missing_worker_detected',c(None,[],[])=='worker_missing')
ok('zero_exit_is_terminal',c('0',[],[])=='0')
ok('nonzero_exit_is_terminal',c('1',[],[])=='1')
ok('wrapper_failure_terminal',c(None,['1'],[])=='1')
ok('wrapper_success_without_process_not_pending',c(None,['0'],[])=='worker_missing')
try:c('pending',[],[])
except ValueError:checks['malformed_exit_rejected']=True
else:raise AssertionError('Malformed exit accepted')
with tempfile.TemporaryDirectory(prefix='pa3-v036-ops-') as tmp:
 T=Path(tmp);course=T/'course';p=course/'gym-workspace/project';s=course/'setup';o=p/'outputs/confirmation_v036';private=T/'private';a=private/'v036-archives';r=private/'v036-runtime/v2gao-123-first_five'
 for d in [s,o,a,r]:d.mkdir(parents=True)
 (p/'frozen_source.txt').write_text('frozen source');(o/'partial_proof.txt').write_text('preserved evidence');(s/'helper.py').write_text('# helper');(r/'v036-first_five-course-preflight.log').write_text('preflight trace');(s/'v036-first_five-course-preflight.log').symlink_to(r/'v036-first_five-course-preflight.log');(r/'v036-first_five-exit-code.txt').write_text('1')
 (s/'v036-pins.json').write_text(json.dumps({'project_files':{'frozen_source.txt':sha(p/'frozen_source.txt')},'setup_files':{'helper.py':sha(s/'helper.py')}}))
 source=(H/'snapshot_v036.py').read_text().replace('/home/v2gao/dsc102/pa3/gym-workspace/ventilator-pressure-prediction',str(p)).replace('/home/v2gao/private/.pa3-preserved-course-backups/v036-archives',str(a)).replace('/home/v2gao/private/.pa3-preserved-course-backups/v036-runtime',str(private/'v036-runtime'))
 snap=T/'snapshot.py';snap.write_text(source);env=dict(os.environ,PA3_V036_ATTEMPT='v2gao-123-first_five')
 run=subprocess.run(['python3',str(snap)],env=env,capture_output=True,text=True,check=True);info=json.loads(run.stdout);archive=Path(info['archive_file'])
 ok('snapshot_archive_private',archive.parent==a);ok('snapshot_no_course_manifest_write',not (o/'pipeline-backup-manifest.json').exists())
 stage=T/'stage';stage.mkdir();(stage/'archive.json').write_text(json.dumps(info));shutil.copy2(H/'verify_archive_v036.py',stage/'verify_archive_v036.py')
 verified=subprocess.run(['python3',str(stage/'verify_archive_v036.py'),str(stage/'archive.json'),str(archive)],capture_output=True,text=True,check=True)
 ok('private_snapshot_all_safe_members_verified',json.loads(verified.stdout)['all_individual_file_hashes'])
 source=(H/'copy_verified_archive_v036.py').read_text().replace('/home/v2gao/private/.pa3-preserved-course-backups/v036-archives',str(a));module={'__name__':'test_copy'};exec(compile(source,'copy_repair_fixture','exec'),module)
 def copy(args):shutil.copy2(archive,args[-1]);return types.SimpleNamespace(returncode=1,stderr='Simulated transfer-status ambiguity; bytes exact')
 report=module['recover'](stage,'v2gao-123','v036',copy_runner=copy,retry_seconds=0)
 ok('ambiguous_copy_accepted_only_after_full_verification',report['verified'] and sha(stage/'pipeline-archive.tar.gz')==info['sha256'])
 info['archive_file']=str(s/'v036-complete-unreviewed.tar.gz');(stage/'archive.json').write_text(json.dumps(info))
 try:module['recover'](stage,'v2gao-123','v036',copy_runner=copy,retry_seconds=0)
 except ValueError:checks['unreviewed_archive_parent_rejected']=True
 else:raise AssertionError('Unexpected source parent accepted')
# A real subprocess PIPE must close while the detached fixture child still runs.
# This reproduces the old compound-command stream inheritance failure.
import re,time
with tempfile.TemporaryDirectory(prefix='v036-detach-') as tmp:
 t=Path(tmp);(t/'wrapper.sh').write_text('sleep 2\n')
 command=next(line for line in (H/'guardian_v036.sh').read_text().splitlines() if 'nohup /bin/bash' in line).split("/bin/bash -c '",1)[1].rsplit("'",1)[0]
 command=command.replace('/home/v2gao/dsc102/pa3/setup/start_v036.sh',str(t/'wrapper.sh'))
 started=time.monotonic();r=subprocess.run(['/bin/bash','-c',command],env=dict(os.environ,PA3_V036_RUNTIME=str(t/'runtime')),capture_output=True,text=True,timeout=1)
 ok('detached_launch_returns_before_child_completes',r.returncode==0 and time.monotonic()-started<1)
for name in ['guardian_v036.sh','start_v036.sh']:subprocess.run(['/bin/bash','-n',str(H/name)],check=True)
ok('shell_syntax',True)
freeze=json.loads((P/'research/freeze_v036.json').read_text());book=json.loads((P/freeze['notebook']).read_text());code='\n'.join(''.join(c['source'])for c in book['cells']if c['cell_type']=='code')
ok('scientific_source_unchanged',hashlib.sha256(code.encode()).hexdigest()==freeze['source_code_sha256'])
ok('scientific_protocol_unchanged',sha(P/freeze['protocol_file'])==freeze['protocol_sha256'])
result=dict(status='passed',check_count=len(checks),checks=checks,model_or_data_training=False,scientific_source_and_protocol_unchanged=True,helper_hashes={p.name:sha(p)for p in H.iterdir()if p.suffix in ['.py','.sh']})
(P/'research/operations_schema_repair_review_v036.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

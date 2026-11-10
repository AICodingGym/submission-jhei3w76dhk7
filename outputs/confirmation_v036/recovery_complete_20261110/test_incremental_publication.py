from pathlib import Path
from datetime import datetime,timezone
import tempfile,hashlib,json,tarfile,io,subprocess
P=Path.cwd();D=P/'outputs/confirmation_v036/recovery_complete_20261110';source=(D/'publish_incremental_v036.py').read_text();verifier=P/'outputs/confirmation_v036/setup_helpers_quota_v4/verify_archive_v036.py';best=P/'outputs/confirmation_v014/final_all_v018/submission.csv';checks={}
def digest(b):return hashlib.sha256(b).hexdigest()
for case in ['valid_append','changed_checkpoint','nonprefix_events']:
 with tempfile.TemporaryDirectory(prefix='v036-incremental-proof-')as tmp:
  T=Path(tmp);root=T/'project';root.mkdir();arc=T/'archive';arc.mkdir();model='outputs/confirmation_v036/F_models/old/model.pt';events='outputs/confirmation_v036/events.jsonl';new='outputs/confirmation_v036/F_models/new/model.pt';oldlog=b'{"event":"start"}\n';basefiles={model:b'old immutable checkpoint',events:oldlog};base={'files':[dict(path=n,bytes=len(b),sha256=digest(b))for n,b in basefiles.items()]}
  bp=root/'outputs/confirmation_v036/completed_archive_first_five/mirror/outputs/confirmation_v036/pipeline-backup-manifest.json';bp.parent.mkdir(parents=True);bp.write_text(json.dumps(base));bsha=digest(bp.read_bytes())
  for n,b in basefiles.items():p=root/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
  b=root/'outputs/confirmation_v014/final_all_v018/submission.csv';b.parent.mkdir(parents=True);b.symlink_to(best)
  files={events:oldlog+b'{"event":"finish"}\n',new:b'new checkpoint bytes'};unchanged=[r for r in base['files']if r['path']==model]
  if case=='nonprefix_events':files[events]=b'{"event":"tampered"}\n'
  if case=='changed_checkpoint':files[model]=b'wrong overwrite';unchanged=[]
  rows=[dict(path=n,bytes=len(b),sha256=digest(b))for n,b in files.items()];manifest=dict(files=rows,archive_kind='incremental_after_verified_first_five',base_archive_sha256='68aef59d863c82eddddc08e334535a3c655aa7a5e9d1c4419426c56e3efa5c53',base_manifest_sha256=bsha,unchanged_base_members=unchanged,all_current_members=len(rows)+len(unchanged));files['outputs/confirmation_v036/pipeline-backup-manifest.json']=json.dumps(manifest).encode()
  a=arc/'pipeline-archive.tar.gz'
  with tarfile.open(a,'w:gz')as t:
   for n,b in files.items():m=tarfile.TarInfo(n);m.size=len(b);t.addfile(m,io.BytesIO(b))
  info=dict(bytes=a.stat().st_size,sha256=digest(a.read_bytes()),files=len(files));(arc/'archive.json').write_text(json.dumps(info));r=subprocess.run(['python3',str(verifier),str(arc/'archive.json'),str(a)],capture_output=True,text=True,check=True);(arc/'archive-verification.json').write_text(r.stdout)
  # Replace only the fixed base-manifest identity for this synthetic fixture.
  runner=T/'publisher.py';runner.write_text(source.replace('0d319db32ea7273faebb72e014c020d26938725a331c329279e4208ac798b7f3',bsha));r=subprocess.run(['python3',str(runner),str(arc)],cwd=root,capture_output=True,text=True)
  if case=='valid_append':
   assert r.returncode==0,r.stderr;assert(root/events).read_bytes()==files[events]and(arc/'prior_mutable_logs'/events).read_bytes()==oldlog and(root/model).read_bytes()==basefiles[model]and(root/new).read_bytes()==files[new];checks['valid_append_preserves_original_and_publishes_new']=True
  else:
   assert r.returncode!=0 and not(root/new).exists()and(root/events).read_bytes()==oldlog and(root/model).read_bytes()==basefiles[model];checks[case+'_rejected_before_publication']=True
report=dict(status='passed',utc=datetime.now(timezone.utc).isoformat(),checks=checks,check_count=len(checks),operational_synthetic_fixture_only=True,production_publisher_sha256=digest(source.encode()));(P/'research/incremental_publication_review_v036.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))

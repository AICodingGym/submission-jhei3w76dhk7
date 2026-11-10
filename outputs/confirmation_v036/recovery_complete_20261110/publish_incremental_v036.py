"""Publish only new/identical V036 run files after full archive verification.

Keep root sources untouched and preserve a complete safe mirror of every member.
"""
from pathlib import Path,PurePosixPath
from datetime import datetime,timezone
import sys,json,hashlib,tarfile,shutil,os
P=Path.cwd();D=Path(sys.argv[1]);info=json.loads((D/'archive.json').read_text());verified=json.loads((D/'archive-verification.json').read_text());a=D/'pipeline-archive.tar.gz'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
assert verified['verified'] and verified['sha256']==info['sha256']==sha(a) and a.stat().st_size==info['bytes']
mirror=D/'mirror';partial=D/'mirror-incomplete';assert not mirror.exists() and not partial.exists();partial.mkdir()
actual={};manifest=None;manifest_name='outputs/confirmation_v036/pipeline-backup-manifest.json'
with tarfile.open(a,'r|gz')as t:
 for m in t:
  rel=PurePosixPath(m.name);assert m.isfile() and not rel.is_absolute()and '..'not in rel.parts and m.name not in actual
  p=partial/rel;p.parent.mkdir(parents=True,exist_ok=True);h=hashlib.sha256();n=0
  with t.extractfile(m)as src,p.open('xb')as dst:
   for b in iter(lambda:src.read(1048576),b''):dst.write(b);h.update(b);n+=len(b)
  assert n==m.size;actual[m.name]=dict(bytes=n,sha256=h.hexdigest())
  if m.name==manifest_name:manifest=json.loads(p.read_text())
assert manifest is not None and len(actual)==info['files'];rows=manifest['files'];expected={r['path']:dict(bytes=r['bytes'],sha256=r['sha256'])for r in rows};assert len(rows)==len(expected)and set(actual)==set(expected)|{manifest_name}
assert all(actual[k]==v for k,v in expected.items());partial.rename(mirror)
# Verify the already-published base before accepting an incremental archive.
base_path=P/'outputs/confirmation_v036/completed_archive_first_five/mirror/outputs/confirmation_v036/pipeline-backup-manifest.json'
assert manifest['archive_kind']=='incremental_after_verified_first_five'
assert manifest['base_archive_sha256']=='68aef59d863c82eddddc08e334535a3c655aa7a5e9d1c4419426c56e3efa5c53'
assert sha(base_path)==manifest['base_manifest_sha256']=='0d319db32ea7273faebb72e014c020d26938725a331c329279e4208ac798b7f3'
base_rows={r['path']:r for r in json.loads(base_path.read_text())['files']}
unchanged=manifest['unchanged_base_members']
assert not set(r['path'] for r in unchanged).intersection(r['path'] for r in rows)
assert len(rows)+len(unchanged)==manifest['all_current_members']
for r in unchanged:
 assert base_rows[r['path']]==r
 if r['path'].startswith('outputs/confirmation_v036/'):
  dest=P/r['path'];assert dest.is_file() and sha(dest)==r['sha256'],'Base artifact changed: '+str(dest)
published=[];identical=[];appended=[]

# Never overwrite old artifacts. Verify every existing run path before mutation.
runrows=[r for r in rows if r['path'].startswith('outputs/confirmation_v036/')]
for r in runrows:
 dest=P/r['path']
 if dest.exists():
  assert dest.is_file()
  if sha(dest)!=r['sha256']:
   assert r['path']=='outputs/confirmation_v036/events.jsonl','Immutable run artifact differs: '+str(dest)
   assert r['path'] in base_rows and sha(dest)==base_rows[r['path']]['sha256'],'Old event log not the verified base'
   old=dest.read_bytes();current=(mirror/r['path']).read_bytes();assert current.startswith(old) and (not old or old.endswith(b'\n')),'Event history must be append only'
   for line in current.decode().splitlines():json.loads(line)
   appended.append(r['path'])
for r in runrows:
 src=mirror/r['path'];dest=P/r['path']
 if dest.exists() and r['path'] not in appended:identical.append(r['path']);continue
 if dest.exists():
  prior=D/'prior_mutable_logs'/r['path'];prior.parent.mkdir(parents=True,exist_ok=True);assert not prior.exists();shutil.copy2(dest,prior);assert sha(prior)==base_rows[r['path']]['sha256']
 dest.parent.mkdir(parents=True,exist_ok=True);temporary=dest.with_name(dest.name+'.verified-publish-tmp');assert not temporary.exists();shutil.copyfile(src,temporary);assert sha(temporary)==r['sha256'];assert not dest.exists() or r['path'] in appended;os.replace(temporary,dest);published.append(r['path'])
best=P/'outputs/confirmation_v014/final_all_v018/submission.csv';assert sha(best)=='274668c4dc14e9d20a554c738859fca37e448836797d7260ec7b11464dcde3e2'
report=dict(status='published_verified_incremental_with_preserved_append_only_events',utc=datetime.now(timezone.utc).isoformat(),archive_sha256=info['sha256'],mirror=str(mirror),safe_mirror_members=len(actual),new_files=published,identical_files=identical,appended_logs=appended,base_members_verified=len(unchanged),all_member_hashes_verified=True,root_sources_preserved=True,accepted_official_CSV_preserved=True)
(D/'publication.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items()if k not in ['new_files','identical_files']},indent=2));print('new',len(published),'identical',len(identical))

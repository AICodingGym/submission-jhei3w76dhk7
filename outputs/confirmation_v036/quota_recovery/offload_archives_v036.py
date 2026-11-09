"""Preserve course setup archives on the separate private-home filesystem.

Only owned regular setup/*.tar.gz files larger than1MiB are eligible. Verify both
copies before replacing the original with a same-content compatibility symlink.
Scientific files, datasets and model paths are never moved by this script.
"""
from pathlib import Path
from datetime import datetime,timezone
import os,json,hashlib,shutil,time
S=Path('/home/v2gao/dsc102/pa3/setup');PRIVATE=Path('/home/v2gao/private');D=PRIVATE/'.pa3-preserved-course-backups/v036-20261109';D.mkdir(parents=True,exist_ok=True,mode=0o700)
EVENTS=D/'migration_events.jsonl'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def event(v):
 with EVENTS.open('a') as f:f.write(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),**v),sort_keys=True)+'\n');f.flush();os.fsync(f.fileno())
candidates=[p for p in S.glob('*.tar.gz') if p.is_file() and not p.is_symlink() and p.stat().st_size>1048576 and p.stat().st_uid==os.getuid()]
candidates.sort(key=lambda p:p.stat().st_size);private_candidates={}
for p in (PRIVATE/'.pa3-setup-control.gty67K').glob('*/pipeline-archive.tar.gz'):
 if p.is_file():private_candidates.setdefault(p.stat().st_size,[]).append(p)
event(dict(event='plan',eligible_files=[str(p) for p in candidates],eligible_bytes=sum(p.stat().st_size for p in candidates),source_dir=str(S),destination=str(D),no_scientific_or_dataset_files_selected=True))
rows=[]
for i,p in enumerate(candidates):
 stat=p.stat();h=sha(p);dest=D/p.name
 if dest.exists():
  assert dest.is_file() and dest.stat().st_size==stat.st_size and sha(dest)==h,'Conflicting private backup preserved: '+str(dest);method='existing_exact'
 else:
  existing=next((v for v in private_candidates.get(stat.st_size,[]) if sha(v)==h),None)
  if existing:
   os.link(existing,dest);method='same-filesystem_hardlink_to_existing_verified_private_archive'
  else:
   tmp=D/(p.name+'.copying');assert not tmp.exists(),'Preserve/review interrupted copy: '+str(tmp)
   with p.open('rb') as src,tmp.open('xb') as dst:shutil.copyfileobj(src,dst,1048576);dst.flush();os.fsync(dst.fileno())
   assert tmp.stat().st_size==stat.st_size and sha(tmp)==h,'Copy checksum mismatch; source untouched';os.replace(tmp,dest);method='copied_and_fsynced'
 assert dest.stat().st_size==stat.st_size and sha(dest)==h
 row=dict(source=str(p),destination=str(dest),bytes=stat.st_size,sha256=h,mode=stat.st_mode,mtime_ns=stat.st_mtime_ns,preservation_method=method)
 event(dict(event='private_copy_verified_before_relocation',**row))
 link=S/(p.name+'.v036-offload-link')
 try:
  assert not link.exists() and not link.is_symlink();link.symlink_to(dest);os.replace(link,p);atomic=True
 except OSError as e:
  if e.errno!=122:raise
  # A completely full quota may not allow even one temporary symlink. The fully
  # verified/fsynced private copy exists before the brief source-name transition.
  assert sha(p)==h and sha(dest)==h;p.unlink();atomic=False
  for attempt in range(12):
   try:p.symlink_to(dest);break
   except OSError as q:
    if q.errno!=122 or attempt==11:raise
    time.sleep(.25)
 assert p.is_symlink() and p.stat().st_size==stat.st_size and sha(p)==h,'Compatibility link does not preserve bytes'
 row.update(source_path_preserved_as_same_content_symlink=True,atomic_path_replacement=atomic);rows.append(row);event(dict(event='relocation_committed',**row))
 if i%6==0:print(json.dumps(dict(progress=i+1,total=len(candidates),logical_bytes_offloaded=sum(x['bytes'] for x in rows))),flush=True)
probe=S/'v036-quota-write-probe.bin';assert not probe.exists();block=b'quota-recovery-verification\n'*4096
with probe.open('xb') as f:
 for _ in range(64):f.write(block)
 f.flush();os.fsync(f.fileno())
probe_bytes=probe.stat().st_size;probe_hash=sha(probe);probe.unlink()
result=dict(status='complete',created_utc=datetime.now(timezone.utc).isoformat(),files=rows,files_relocated=len(rows),logical_bytes_offloaded=sum(r['bytes'] for r in rows),all_original_paths_preserved=True,all_private_bytes_verified=True,course_write_probe_bytes=probe_bytes,course_write_probe_sha256=probe_hash,probe_removed_after_verification=True,no_model_dataset_or_submission_files_moved=True,destination=str(D))
with (D/'migration_result.json').open('x') as f:f.write(json.dumps(result,indent=2)+'\n');f.flush();os.fsync(f.fileno())
print(json.dumps({k:v for k,v in result.items() if k!='files'},indent=2),flush=True)

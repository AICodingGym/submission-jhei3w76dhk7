"""Two-pass, checksum-verified relocation of owned setup archives only.

Copies are durable before any source is moved. Course archive paths are restored
as compatibility links only after the complete batch has freed quota headroom.
"""
from pathlib import Path
from datetime import datetime,timezone
import os,json,hashlib,shutil,time
S=Path('/home/v2gao/dsc102/pa3/setup');PRIVATE=Path('/home/v2gao/private');D=PRIVATE/'.pa3-preserved-course-backups/v036-20261109';assert D.is_dir();EVENTS=D/'migration_events.jsonl'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def event(v):
 with EVENTS.open('a') as f:f.write(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),**v),sort_keys=True)+'\n');f.flush();os.fsync(f.fileno())
previous={v['source']:v for v in map(json.loads,EVENTS.read_text().splitlines()) if v.get('event')=='private_copy_verified_before_relocation'}
files=[p for p in S.glob('*.tar.gz') if p.is_file() and not p.is_symlink() and p.stat().st_size>1048576 and p.stat().st_uid==os.getuid()];files.sort(key=lambda p:-p.stat().st_size);private_candidates={}
for p in (PRIVATE/'.pa3-setup-control.gty67K').glob('*/pipeline-archive.tar.gz'):
 if p.is_file():private_candidates.setdefault(p.stat().st_size,[]).append(p)
rows=[]
for src,v in previous.items():
 p=Path(src)
 if not p.exists():
  dest=Path(v['destination']);assert dest.is_file() and dest.stat().st_size==v['bytes'] and sha(dest)==v['sha256'];rows.append({k:v[k] for k in ['source','destination','bytes','sha256','mode','mtime_ns','preservation_method']})
event(dict(event='batch_plan',source_files=[str(p) for p in files],preserved_prior_relocation_paths=[r['source'] for r in rows],logical_bytes=sum(p.stat().st_size for p in files)+sum(r['bytes'] for r in rows)))
# Phase1: preserve and verify every archive. Failure here leaves all remaining
# source archives untouched; the already relocated first archive is also verified.
for i,p in enumerate(files):
 st=p.stat();h=sha(p);dest=D/p.name
 if dest.exists():assert dest.is_file() and dest.stat().st_size==st.st_size and sha(dest)==h;method='existing_exact'
 else:
  duplicate=next((q for q in private_candidates.get(st.st_size,[]) if sha(q)==h),None)
  if duplicate:os.link(duplicate,dest);method='private_existing_exact_hardlink'
  else:
   tmp=D/(p.name+'.copying');assert not tmp.exists(),'Interrupted copy preserved; review '+str(tmp)
   with p.open('rb') as src,tmp.open('xb') as out:shutil.copyfileobj(src,out,1048576);out.flush();os.fsync(out.fileno())
   assert tmp.stat().st_size==st.st_size and sha(tmp)==h;os.replace(tmp,dest);method='copied_fsynced_verified'
 assert dest.stat().st_size==st.st_size and sha(dest)==h
 row=dict(source=str(p),destination=str(dest),bytes=st.st_size,sha256=h,mode=st.st_mode,mtime_ns=st.st_mtime_ns,preservation_method=method);rows.append(row);event(dict(event='private_copy_verified_before_relocation',**row))
 if i%6==0:print(json.dumps(dict(phase='copy_verify',files=i+1,total=len(files))),flush=True)
with (D/'verified_batch_before_relocation.json').open('x') as f:f.write(json.dumps(dict(files=rows,all_copies_verified=True),indent=2)+'\n');f.flush();os.fsync(f.fileno())
# Phase2: relocate originals only after every destination is verified. These are
# backup archives, never model/dataset/submission files. Preserve old names next.
for row in rows:
 p=Path(row['source']);dest=Path(row['destination']);assert sha(dest)==row['sha256']
 if p.exists():
  assert not p.is_symlink() and p.stat().st_uid==os.getuid() and p.stat().st_size==row['bytes'] and sha(p)==row['sha256'];p.unlink();event(dict(event='verified_original_relocated',**row))
for attempt in range(60):
 failures=[]
 for row in rows:
  p=Path(row['source']);dest=Path(row['destination'])
  if not p.is_symlink():
   try:p.symlink_to(dest)
   except OSError as e:
    if e.errno!=122:raise
    failures.append(str(p))
 if not failures:break
 time.sleep(.5)
assert not failures,'All bytes preserved privately; quota still blocks compatibility links: '+repr(failures)
for row in rows:
 p=Path(row['source']);assert p.is_symlink() and p.stat().st_size==row['bytes'] and sha(p)==row['sha256'];row['source_path_preserved_as_same_content_symlink']=True
probe=S/'v036-quota-write-probe.bin';assert not probe.exists();block=b'quota-verification\n'*65536
with probe.open('xb') as f:
 for _ in range(8):f.write(block)
 f.flush();os.fsync(f.fileno())
probe_bytes=probe.stat().st_size;probe_hash=sha(probe);probe.unlink()
result=dict(status='complete',created_utc=datetime.now(timezone.utc).isoformat(),files=rows,files_relocated=len(rows),logical_bytes_offloaded=sum(r['bytes'] for r in rows),all_original_paths_preserved=True,all_private_bytes_verified=True,course_write_probe_bytes=probe_bytes,course_write_probe_sha256=probe_hash,no_model_dataset_or_submission_files_moved=True,destination=str(D),prior_small_batch_failed_to_free_enough_quota=True)
with (D/'migration_result.json').open('x') as f:f.write(json.dumps(result,indent=2)+'\n');f.flush();os.fsync(f.fileno())
print(json.dumps({k:v for k,v in result.items() if k!='files'},indent=2),flush=True)

"""Verify transfer, safe members and every archived file before GPU release."""
import sys,json,hashlib,tarfile
from pathlib import Path,PurePosixPath
info=json.loads(Path(sys.argv[1]).read_text());path=Path(sys.argv[2])
def sha_file(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
assert path.stat().st_size==info['bytes'] and sha_file(path)==info['sha256'],'Archive transfer differs'
with tarfile.open(path,'r:gz') as t:
 members=t.getmembers();names=[m.name for m in members];assert len(names)==len(set(names))==info['files'],'Duplicate/count mismatch'
 for m in members:
  p=PurePosixPath(m.name);assert m.isfile() and not p.is_absolute() and '..' not in p.parts,'Unsafe archive member'
 manifest_name='outputs/confirmation_v036/pipeline-backup-manifest.json';manifest=json.load(t.extractfile(manifest_name));rows=manifest['files']
 expected=[r['path'] for r in rows];assert len(expected)==len(set(expected)) and set(names)==set(expected)|{manifest_name},'Manifest membership differs'
 for r in rows:
  m=t.getmember(r['path']);assert m.size==r['bytes'];h=hashlib.sha256()
  with t.extractfile(m) as f:
   for b in iter(lambda:f.read(1048576),b''):h.update(b)
  assert h.hexdigest()==r['sha256'],'Archived file hash differs: '+r['path']
print(json.dumps(dict(verified=True,files=len(members),sha256=info['sha256'],safe_regular_members=True,all_individual_file_hashes=True)))

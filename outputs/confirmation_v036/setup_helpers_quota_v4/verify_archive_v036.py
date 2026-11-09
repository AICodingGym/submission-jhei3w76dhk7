"""Verify all safe regular members in one forward pass; no gzip seeking."""
import sys,json,hashlib,tarfile
from pathlib import Path,PurePosixPath
info=json.loads(Path(sys.argv[1]).read_text());path=Path(sys.argv[2])
def sha_file(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
assert path.stat().st_size==info['bytes'] and sha_file(path)==info['sha256'],'Archive transfer differs'
manifest_name='outputs/confirmation_v036/pipeline-backup-manifest.json';actual={};manifest=None
with tarfile.open(path,'r|gz') as t:
 for m in t:
  p=PurePosixPath(m.name);assert m.isfile() and not p.is_absolute() and '..' not in p.parts,'Unsafe archive member'
  assert m.name not in actual,'Duplicate archive member'
  h=hashlib.sha256();size=0;blocks=[] if m.name==manifest_name else None
  with t.extractfile(m) as f:
   for b in iter(lambda:f.read(1048576),b''):
    h.update(b);size+=len(b)
    if blocks is not None:blocks.append(b)
  assert size==m.size,'Truncated member'
  actual[m.name]=dict(bytes=size,sha256=h.hexdigest())
  if blocks is not None:manifest=json.loads(b''.join(blocks))
assert len(actual)==info['files'] and manifest is not None,'Count/manifest mismatch'
rows=manifest['files'];expected={r['path']:dict(bytes=r['bytes'],sha256=r['sha256'])for r in rows}
assert len(expected)==len(rows) and set(actual)==set(expected)|{manifest_name},'Manifest membership differs'
for name,row in expected.items():assert actual[name]==row,'Archived file hash/size differs: '+name
print(json.dumps(dict(verified=True,files=len(actual),sha256=info['sha256'],safe_regular_members=True,all_individual_file_hashes=True,forward_only_stream=True)))

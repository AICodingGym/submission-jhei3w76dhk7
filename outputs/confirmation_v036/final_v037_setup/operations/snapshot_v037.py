"""Archive V037 source, run evidence and exact hashes after worker exit."""
import pathlib,json,hashlib,tarfile,datetime,fcntl,time,os,re
P=pathlib.Path('/home/v2gao/dsc102/pa3/gym-workspace/ventilator-pressure-prediction');S=P.parents[1]/'setup';O=P/'outputs/confirmation_v036/final_all_v037'
O.mkdir(parents=True,exist_ok=True)
A=pathlib.Path('/home/v2gao/private/.pa3-preserved-course-backups/v037-archives');A.mkdir(parents=True,exist_ok=True)
attempt=os.environ['PA3_V037_ATTEMPT'];assert re.fullmatch(r'v2gao-[0-9]+-final',attempt)
R=pathlib.Path('/home/v2gao/private/.pa3-preserved-course-backups/v037-runtime')/attempt
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
f=(S/'v037-start-wrapper.lock').open('a+')
for _ in range(100):
 try:fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB);break
 except BlockingIOError:time.sleep(.1)
else:raise RuntimeError('Wrapper still active')
g=(P/'outputs/.v011_gpu.lock').open('a+');fcntl.flock(g,fcntl.LOCK_EX|fcntl.LOCK_NB)
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as s:
  for b in iter(lambda:s.read(1048576),b''):h.update(b)
 return h.hexdigest()
pins=json.loads((S/'v037-pins.json').read_text())
files=[p for p in O.rglob('*') if p.is_file() and not p.name.endswith('.lock') and p.name!='pipeline-backup-manifest.json']
for name in pins['project_files']:
 p=P/name;assert p.is_file(),name;files.append(p)
for name in pins['setup_files']:
 p=S/name;assert p.is_file(),name;files.append(p)
files += [p for p in S.glob('v037*') if p.is_file() and p.suffix not in ['.gz','.lock']]
files += [p for p in R.iterdir() if p.is_file() and p.name!='archive-error-reserve.bin']
files=sorted(set(files))
def arc(p):return str(p.relative_to(P)) if p.is_relative_to(P) else 'operational_setup/'+p.name
by_arc={}
for p in files:
 name=arc(p)
 if name in by_arc:assert p.resolve()==by_arc[name].resolve(),'Conflicting archive name: '+name
 else:by_arc[name]=p
files=[by_arc[name] for name in sorted(by_arc)]
rows=[dict(path=arc(p),bytes=p.stat().st_size,sha256=sha(p)) for p in files]
m=A/('v037-manifest-'+attempt+'-'+stamp+'.json')
a=A/('v037-complete-'+attempt+'-'+stamp+'.tar.gz')
try:
 m.write_text(json.dumps(dict(files=rows,created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()),indent=2)+'\n');files.append(m)
 with tarfile.open(a,'w:gz') as t:
  for p in files:t.add(p.resolve(),arcname='outputs/confirmation_v036/final_all_v037/pipeline-backup-manifest.json' if p==m else arc(p),recursive=False)
 info=dict(archive_file=str(a),bytes=a.stat().st_size,sha256=sha(a),files=len(files))
finally:
 reserve=R/'archive-error-reserve.bin'
 if reserve.exists():reserve.unlink()
print(json.dumps(info))

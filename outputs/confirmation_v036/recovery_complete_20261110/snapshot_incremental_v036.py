"""Archive V036 source, run evidence and exact hashes after worker exit."""
import pathlib,json,hashlib,tarfile,datetime,fcntl,time,os,re
P=pathlib.Path('/home/v2gao/dsc102/pa3/gym-workspace/ventilator-pressure-prediction');S=P.parents[1]/'setup';O=P/'outputs/confirmation_v036'
O.mkdir(parents=True,exist_ok=True)
A=pathlib.Path('/home/v2gao/private/.pa3-preserved-course-backups/v036-archives');A.mkdir(parents=True,exist_ok=True)
attempt='v2gao-2973011-remaining_two-r3'
R=pathlib.Path('/home/v2gao/private/.pa3-preserved-course-backups/v036-runtime')/attempt
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
f=(S/'v036-start-wrapper.lock').open('a+')
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
base_path=pathlib.Path('/tmp/v036-base-manifest.json')
assert sha(base_path)==os.environ['PA3_V036_BASE_MANIFEST_SHA256'],'Base manifest changed'
base=json.loads(base_path.read_text());base_rows={r['path']:r for r in base['files']}
assert len(base_rows)==len(base['files'])
pins=json.loads((S/'v036-pins.json').read_text())
files=[p for p in O.rglob('*') if p.is_file() and not p.name.endswith('.lock') and p.name!='pipeline-backup-manifest.json']
for name in pins['project_files']:
 p=P/name;assert p.is_file(),name;files.append(p)
for name in pins['setup_files']:
 p=S/name;assert p.is_file(),name;files.append(p)
files += [p for p in S.glob('v036*') if p.is_file() and p.suffix not in ['.gz','.lock']]
files += [p for p in R.iterdir() if p.is_file()]
files=sorted(set(files))
def arc(p):return str(p.relative_to(P)) if p.is_relative_to(P) else 'operational_setup/'+p.name
by_arc={}
for p in files:
 name=arc(p)
 if name in by_arc:assert p.resolve()==by_arc[name].resolve(),'Conflicting archive name: '+name
 else:by_arc[name]=p
files=[by_arc[name] for name in sorted(by_arc)]
all_rows=[dict(path=arc(p),bytes=p.stat().st_size,sha256=sha(p)) for p in files]
unchanged=[r for r in all_rows if r['path'] in base_rows and r==base_rows[r['path']]]
rows=[r for r in all_rows if r not in unchanged]
selected={r['path'] for r in rows};files=[p for p in files if arc(p) in selected]
result=json.loads((O/'confirmation_result.json').read_text());assert result['status']=='complete' and len(result['records'])==7
for record in result['records'].values():
 for key,hkey in [('checkpoint_file','checkpoint_sha256'),('last_checkpoint_file','last_checkpoint_sha256'),('report_file','report_sha256')]:assert sha(P/record[key])==record[hkey]

m=A/('v036-manifest-recovery-'+attempt+'-'+stamp+'.json');m.write_text(json.dumps(dict(files=rows,created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),archive_kind='incremental_after_verified_first_five',base_archive_sha256='68aef59d863c82eddddc08e334535a3c655aa7a5e9d1c4419426c56e3efa5c53',base_manifest_sha256=sha(base_path),unchanged_base_members=unchanged,omitted_historical_base_members=sorted(set(base_rows)-{r['path'] for r in all_rows}),all_current_members=len(all_rows)),indent=2)+'\n');files.append(m)
a=A/('v036-complete-recovery-'+attempt+'-'+stamp+'.tar.gz')
with tarfile.open(a,'w:gz') as t:
 for p in files:t.add(p.resolve(),arcname='outputs/confirmation_v036/pipeline-backup-manifest.json' if p==m else arc(p),recursive=False)
print(json.dumps(dict(archive_file=str(a),bytes=a.stat().st_size,sha256=sha(a),files=len(files),archive_kind='incremental_after_verified_first_five',base_archive_sha256='68aef59d863c82eddddc08e334535a3c655aa7a5e9d1c4419426c56e3efa5c53')))

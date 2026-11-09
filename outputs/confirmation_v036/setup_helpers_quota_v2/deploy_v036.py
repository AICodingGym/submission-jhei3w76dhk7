"""Safe preserving deployment; changed existing scientific artifacts require review."""
import pathlib,tarfile,json,hashlib,shutil,datetime,os
R=pathlib.Path('/home/v2gao/dsc102/pa3');P=R/'gym-workspace/ventilator-pressure-prediction';S=R/'setup';archive=pathlib.Path('/tmp/v036-deploy.tar.gz')
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b)
    return h.hexdigest()
payload_hash=sha(archive);assert payload_hash==os.environ['PA3_V036_DEPLOY_SHA256']
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');stage=S/('v036-deployment-'+stamp);stage.mkdir(exist_ok=False)
with tarfile.open(archive) as tar:
    assert len(tar.getnames())==len(set(tar.getnames())),'Duplicate deployment members'
    for member in tar.getmembers():
        path=pathlib.PurePosixPath(member.name)
        assert member.isfile() and not path.is_absolute() and '..' not in path.parts and path.parts[0] in ['project','setup']
    tar.extractall(stage)
pins=json.loads((stage/'setup/v036-pins.json').read_text())
for group,table in [('project',pins['project_files']),('setup',pins['setup_files'])]:
    for relative,digest in table.items():assert sha(stage/group/relative)==digest,'Payload member differs: '+relative
rows=[]
for group,target in [('project',P),('setup',S)]:
    for source in sorted((stage/group).rglob('*')):
        if not source.is_file():continue
        relative=source.relative_to(stage/group);destination=target/relative;destination.parent.mkdir(parents=True,exist_ok=True)
        if destination.exists():
            if sha(destination)==sha(source):continue
            if group=='project' and relative.parts[0] in ('outputs','data'):
                raise ValueError('Existing scientific artifact differs; preserved for explicit review: '+str(destination))
            prior=stage/'prior_files'/group/relative;prior.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(destination,prior)
        temporary=destination.with_name(destination.name+'.deployment-tmp');shutil.copy2(source,temporary);os.replace(temporary,destination)
        rows.append(dict(path=str(destination),sha256=sha(destination)))
(S/'v036-deployed.json').write_text(json.dumps(dict(payload_sha256=payload_hash,files=rows,prior_files_preserved=True),indent=2)+'\n')
print('Reviewed sources deployed; prior source files preserved; scientific artifacts protected')

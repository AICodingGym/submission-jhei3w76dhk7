"""Retry transient kubectl copy failures; publish only a fully verified archive.

Used on the login host by future detached guardians. Does not allocate, train,
submit or delete pods. Failed/partial attempts remain preserved. A nonzero copy
exit can be accepted only when size, SHA and every safe archive member verify.
"""
import hashlib,json,os,re,subprocess,sys,time
from datetime import datetime,timezone
from pathlib import Path

def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b)
    return h.hexdigest()

def recover(stage,pod,kind,copy_runner=None,max_attempts=3,retry_seconds=5):
    stage=Path(stage).resolve()
    if not stage.is_dir() or not re.fullmatch(r'v2gao-[0-9]+',pod) or not re.fullmatch(r'v[0-9]{3}',kind):raise ValueError('Invalid reviewed recovery arguments')
    info_path=stage/'archive.json';info_sha=sha(info_path);info=json.loads(info_path.read_text());source=Path(info['archive_file'])
    if source.parent!=Path('/home/v2gao/private/.pa3-preserved-course-backups/v036-archives') or not source.name.startswith(kind+'-complete-') or not source.name.endswith('.tar.gz'):raise ValueError('Unexpected source archive')
    if not re.fullmatch('[0-9a-f]{64}',info['sha256']) or not isinstance(info['bytes'],int) or info['bytes']<=0:raise ValueError('Invalid source archive identity')
    verifier=stage/('verify_archive_'+kind+'.py');destination=stage/'pipeline-archive.tar.gz';stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    def event(**kw):
        with (stage/'archive-copy-events.jsonl').open('a') as f:f.write(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),**kw))+'\n')
    def verify(path):
        if not path.is_file() or path.stat().st_size!=info['bytes']:return None
        r=subprocess.run([sys.executable,str(verifier),str(info_path),str(path)],capture_output=True,text=True,timeout=180)
        if r.returncode:return None
        report=json.loads(r.stdout)
        if not report.get('verified') or report.get('sha256')!=info['sha256'] or sha(info_path)!=info_sha:raise ValueError('Verification identity changed')
        return report
    def publish_report(report):
        path=stage/'archive-verification.json'
        if path.exists() and json.loads(path.read_text())!=report:os.replace(path,stage/('archive-verification-prior-'+stamp+'.json'))
        if not path.exists():path.write_text(json.dumps(report,indent=2)+'\n')
    report=verify(destination)
    if report is not None:publish_report(report);event(used_existing_verified_archive=True);return report
    run=copy_runner or (lambda args:subprocess.run(args,capture_output=True,text=True,timeout=240))
    for attempt in range(1,max_attempts+1):
        candidate=stage/('pipeline-archive-attempt-'+stamp+'-'+str(attempt)+'.tar.gz')
        try:
            copied=run(['/usr/bin/kubectl','cp',pod+':'+str(source),str(candidate)]);rc=copied.returncode;error=copied.stderr[-2000:]
        except subprocess.TimeoutExpired:rc=124;error='kubectl copy timed out; partial attempt preserved'
        report=verify(candidate)
        event(attempt=attempt,copy_returncode=rc,error=error,bytes=candidate.stat().st_size if candidate.exists() else 0,verified=report is not None)
        if report is not None:
            if destination.exists():os.replace(destination,stage/('pipeline-archive-prior-'+stamp+'.tar.gz'))
            os.replace(candidate,destination)
            publish_report(report)
            return report
        if attempt<max_attempts:time.sleep(retry_seconds)
    raise RuntimeError('All archive copies unverified. Preserve pod and original persistent archive; no release or automatic replacement.')

if __name__=='__main__':
    print(json.dumps(recover(sys.argv[1],sys.argv[2],sys.argv[3])))

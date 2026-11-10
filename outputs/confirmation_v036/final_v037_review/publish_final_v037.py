"""Mirror a verified final archive and publish only new/identical V037 outputs.

Root notebooks and historical run artifacts are never overwritten. No modeling.
"""
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
import hashlib, json, os, shutil, sys, tarfile

PREFIX = 'outputs/confirmation_v036/final_all_v037/'
MANIFEST = PREFIX + 'pipeline-backup-manifest.json'

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1048576), b''):
            h.update(block)
    return h.hexdigest()

def publish(root, directory):
    root = Path(root).resolve(); directory = Path(directory).resolve()
    info = json.loads((directory/'archive.json').read_text())
    verified = json.loads((directory/'archive-verification.json').read_text())
    archive = directory/'pipeline-archive.tar.gz'
    assert verified['verified'] and verified['sha256'] == info['sha256'] == sha(archive)
    assert archive.stat().st_size == info['bytes']
    mirror = directory/'mirror'; partial = directory/'mirror-incomplete'
    assert not mirror.exists() and not partial.exists()
    partial.mkdir(); actual = {}; manifest = None
    with tarfile.open(archive, 'r|gz') as stream:
        for member in stream:
            rel = PurePosixPath(member.name)
            assert member.isfile() and not rel.is_absolute() and '..' not in rel.parts
            assert member.name not in actual
            target = partial/rel; target.parent.mkdir(parents=True, exist_ok=True)
            with stream.extractfile(member) as source, target.open('xb') as sink:
                shutil.copyfileobj(source, sink, 1048576)
            assert target.stat().st_size == member.size
            actual[member.name] = dict(bytes=member.size, sha256=sha(target))
            if member.name == MANIFEST:
                manifest = json.loads(target.read_text())
    assert manifest is not None and len(actual) == info['files']
    rows = manifest['files']
    expected = {r['path']: dict(bytes=r['bytes'], sha256=r['sha256']) for r in rows}
    assert len(rows) == len(expected) and set(actual) == set(expected)|{MANIFEST}
    assert all(actual[k] == v for k, v in expected.items())
    partial.rename(mirror)
    runrows = [dict(path=k, **v) for k, v in actual.items() if k.startswith(PREFIX)]
    # Check every existing destination, including parents, before publishing any file.
    for row in runrows:
        dest = root/row['path']
        assert dest.resolve().is_relative_to(root) and not dest.is_symlink()
        assert not dest.exists() or (dest.is_file() and sha(dest) == row['sha256']), 'Existing artifact differs: '+str(dest)
    published = []; identical = []
    for row in runrows:
        dest = root/row['path']; source = mirror/row['path']
        if dest.exists():
            identical.append(row['path']); continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        temporary = dest.with_name(dest.name+'.verified-publish-tmp')
        assert not temporary.exists()
        with source.open('rb') as src, temporary.open('xb') as sink:
            shutil.copyfileobj(src, sink, 1048576)
        assert sha(temporary) == row['sha256']
        # Atomic no-clobber publication; a concurrent artifact cannot be replaced.
        os.link(temporary, dest); temporary.unlink(); published.append(row['path'])
    best = root/'outputs/confirmation_v014/final_all_v018/submission.csv'
    assert sha(best) == '274668c4dc14e9d20a554c738859fca37e448836797d7260ec7b11464dcde3e2'
    result = dict(status='published_verified_final', utc=datetime.now(timezone.utc).isoformat(),
                  archive_sha256=info['sha256'], mirror=str(mirror), safe_mirror_members=len(actual),
                  new_files=published, identical_files=identical, root_sources_preserved=True,
                  all_member_hashes_verified=True, accepted_official_CSV_preserved=True)
    with (directory/'publication.json').open('x') as f:
        f.write(json.dumps(result, indent=2)+'\n')
    return result

if __name__ == '__main__':
    result = publish(Path.cwd(), Path(sys.argv[1]))
    print(json.dumps({k:v for k,v in result.items() if k not in ['new_files','identical_files']}, indent=2))
    print('new', len(result['new_files']), 'identical', len(result['identical_files']))

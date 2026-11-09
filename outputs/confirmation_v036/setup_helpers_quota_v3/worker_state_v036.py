"""Read only attempt liveness; never kill/restart/allocate or inspect MAE."""
from pathlib import Path
import os,re,json
ROOT=Path('/home/v2gao/private/.pa3-preserved-course-backups/v036-runtime')
PROGRAMS={'/home/v2gao/dsc102/pa3/setup/'+n for n in ['start_v036.sh','course_preflight_v036.py','execute_screen_v036.py']}
def classify(exit_text,wrapper_texts,worker_processes):
    if exit_text is not None:
        v=exit_text.strip()
        if not re.fullmatch(r'[0-9]+',v):raise ValueError('Invalid exit status')
        return v
    if any(v.strip()!='0' for v in wrapper_texts):return '1'
    return 'pending' if worker_processes else 'worker_missing'
def observe(stage,attempt):
    assert stage in ['first_five','remaining_two'] and re.fullmatch(r'v2gao-[0-9]+-'+stage+r'(-r[0-9]+)?',attempt)
    op=ROOT/attempt; processes=[]
    for p in Path('/proc').glob('[0-9]*'):
        try:
            if p.stat().st_uid!=os.getuid():continue
            args=(p/'cmdline').read_bytes().decode(errors='replace').split('\0')
            if PROGRAMS.intersection(args):processes.append(dict(pid=int(p.name),args=args))
        except (FileNotFoundError,ProcessLookupError,PermissionError):continue
    e=op/('v036-'+stage+'-exit-code.txt')
    state=classify(e.read_text() if e.is_file() else None,[p.read_text() for p in op.glob('v036-'+stage+'-wrapper-status-*.txt')],processes)
    return dict(state=state,processes=processes,attempt=attempt,stage=stage)
if __name__=='__main__':
    v=observe(os.environ['PA3_V036_STAGE'],os.environ['PA3_V036_ATTEMPT'])
    if os.environ.get('PA3_V036_OBSERVE_JSON')=='1':print(json.dumps(v))
    else:print(v['state'])

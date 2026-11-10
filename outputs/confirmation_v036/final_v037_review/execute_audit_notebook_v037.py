"""Operational executor: preserve notebook cells/outputs, without extra packages."""
from pathlib import Path
from contextlib import redirect_stdout, redirect_stderr
import os, io, json, hashlib, traceback, time

root=Path.cwd(); path=root/'audit_final_v037.ipynb'; book=json.loads(path.read_text())
expected=json.loads((root/'research/final_audit_preparation_v037.json').read_text())['code_sha256']
def source_hash():
    return hashlib.sha256('\n'.join(''.join(c['source']) for c in book['cells'] if c['cell_type']=='code').encode()).hexdigest()
assert source_hash()==expected
os.environ['PA3_RUN_FINAL_AUDIT_V037']='1'
os.environ.setdefault('OMP_NUM_THREADS','4'); os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
namespace={'__name__':'__main__'};count=0;began=time.monotonic()
for index,cell in enumerate(book['cells']):
    if cell['cell_type']!='code':continue
    count+=1;out=io.StringIO();err=io.StringIO();failure=None
    print('START audit cell',index,'elapsed',round(time.monotonic()-began,1),flush=True)
    try:
        with redirect_stdout(out), redirect_stderr(err):
            exec(compile(''.join(cell['source']),str(path)+':'+str(index),'exec'),namespace)
    except Exception as exception:
        failure=exception
    cell['execution_count']=count;cell['outputs']=[]
    for name,value in [('stdout',out.getvalue()),('stderr',err.getvalue())]:
        if value:
            cell['outputs'].append(dict(output_type='stream',name=name,text=value.splitlines(True)))
            print(value,flush=True)
    if failure:
        trace=traceback.format_exception(type(failure),failure,failure.__traceback__)
        cell['outputs'].append(dict(output_type='error',ename=type(failure).__name__,evalue=str(failure),traceback=trace))
        print(''.join(trace),flush=True)
    assert source_hash()==expected
    temporary=path.with_name(path.name+'.execution-tmp');temporary.write_text(json.dumps(book,indent=1)+'\n');os.replace(temporary,path)
    if failure:raise RuntimeError('Independent audit notebook failed') from failure
    print('COMPLETE audit cell',index,flush=True)
assert namespace['V037_FINAL_AUDIT']['status']=='passed'
print('INDEPENDENT_FINAL_AUDIT_PASSED',flush=True)

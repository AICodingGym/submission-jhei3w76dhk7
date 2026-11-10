"""Operational notebook executor; modeling remains in frozen notebooks."""
import os,sys,json,hashlib,traceback,time
from pathlib import Path
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
os.environ.setdefault('OMP_NUM_THREADS','4')
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import nbformat
from IPython.core.interactiveshell import InteractiveShell
from IPython.utils.capture import capture_output
root=Path('/home/v2gao/dsc102/pa3/gym-workspace/ventilator-pressure-prediction')
setup=root.parents[1]/'setup';os.chdir(root)
pins=json.loads((setup/'v037-pins.json').read_text());freeze=pins['freeze']
expected=freeze['source_code_sha256'];filename=freeze['notebook']
assert expected==os.environ['PA3_V037_SOURCE_SHA256']
export=freeze.get('result_export','V037_RESULT')
path=root/filename;book=nbformat.read(path,4)
def codehash(n):return hashlib.sha256('\n'.join(c.source for c in n.cells if c.cell_type=='code').encode()).hexdigest()
assert codehash(book)==expected,'Source differs from reviewed deployment'
for proof_name in ['course_proofs.json']:
    proof=json.loads((root/'outputs/confirmation_v036/final_all_v037'/proof_name).read_text())
    assert proof['status']=='passed' and proof['driver_source_code_sha256']==expected and proof['F_result_sha256']==pins['F_result_sha256'] and proof['F_audit_sha256']==pins['F_audit_sha256']
    assert proof['actual_cuda'] and all(proof['checks'].values())
shell=InteractiveShell.instance();count=0;started=time.monotonic()
for index,cell in enumerate(book.cells):
    if cell.cell_type!='code':continue
    count+=1;print('START v037 cell',index,'elapsed',round(time.monotonic()-started,1),flush=True)
    with capture_output() as captured:result=shell.run_cell(cell.source,store_history=True)
    cell.execution_count=count;cell.outputs=[]
    for label,value in [('stdout',captured.stdout),('stderr',captured.stderr)]:
        if value:cell.outputs.append(nbformat.v4.new_output('stream',name=label,text=value))
    for rich in captured.outputs:cell.outputs.append(nbformat.v4.new_output('display_data',data=rich.data,metadata=rich.metadata))
    error=result.error_before_exec or result.error_in_exec
    if error:cell.outputs.append(nbformat.v4.new_output('error',ename=type(error).__name__,evalue=str(error),traceback=traceback.format_exception(type(error),error,error.__traceback__)))
    assert codehash(book)==expected
    temporary=path.with_name(path.name+'.tmp');nbformat.write(book,temporary);os.replace(temporary,path)
    if captured.stdout:print(captured.stdout[-4000:],flush=True)
    if captured.stderr:print(captured.stderr[-2000:],flush=True)
    if error:raise RuntimeError(f'v037 cell{index} failed: {error}') from error
    print('COMPLETE v037 cell',index,flush=True)
assert isinstance(shell.user_ns.get(export),dict),'Guarded notebook stage did not run'
summary=shell.user_ns[export]
target=Path(os.environ['PA3_V037_RUNTIME'])/'v037-final-export.json';temporary=target.with_name(target.name+'.tmp')
temporary.write_text(json.dumps(dict(status=summary.get('status'),submission=summary.get('submission')),indent=2,allow_nan=False)+'\n')
os.replace(temporary,target)
print('NOTEBOOK_STAGE_COMPLETE v037',flush=True)

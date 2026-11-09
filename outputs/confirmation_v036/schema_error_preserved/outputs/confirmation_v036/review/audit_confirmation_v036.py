"""Independent stage/final audit, prepared before any F outcome.

Stage audits never load Fvalidation targets. Complete audit reconstructs both
fixed ensembles and the paired whole-breath interval; CPU inference on64 fixed
known-input-selected breaths checks native caches without changing their scores.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,csv,hashlib,json,math,copy,os,gc
import numpy as np
import pandas as pd
import torch
from sklearn.model_selection import train_test_split
P=Path.cwd();O=P/'outputs/confirmation_v036';checks={}
AUDITED_SOURCE='aa340df0768a75f4c942ce0107b2ea0eb21b5ac39fc45461f44a768a0c0d488e'
AUDITED_PROTOCOL='e9fb1fc5fd7a342fd744f8ed2d7bcdbb4eab3d3e5be8f12da6f93575374ab0f4'
def need(c,m):
 if not bool(c):raise AssertionError(m)
 checks[m]=True
def read(p):return json.loads(Path(p).read_text())
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def code(p):return '\n'.join(''.join(c['source']) for c in read(p)['cells'] if c['cell_type']=='code')
def digest(v):return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def rawhash(a):return hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest()
def arrayhash(a):
 a=np.ascontiguousarray(a);h=hashlib.sha256(str((a.shape,a.dtype.str)).encode());h.update(memoryview(a).cast('B'));return h.hexdigest()
def safe(v):
 if isinstance(v,dict):return {k:safe(z) for k,z in v.items()}
 if isinstance(v,(list,tuple)):return [safe(z) for z in v]
 if isinstance(v,np.ndarray):return v.tolist()
 if isinstance(v,np.generic):return v.item()
 return v
def labels_for(ids):
 # Independent membership-first reader; requested canonical group order retained.
 out=np.empty((len(ids),80),np.float32);where={int(x):i for i,x in enumerate(ids)};counts=np.zeros(len(ids),np.int16)
 with (P/'data/train.csv').open(newline='') as f:
  for row in csv.DictReader(f):
   j=where.get(int(row['breath_id']))
   if j is None:continue
   k=int(counts[j]);need(k<80,'selected label row bound');out[j,k]=np.float32(float(row['pressure']));counts[j]+=1
 need(np.all(counts==80) and np.isfinite(out).all(),'Selected fit/score label coverage')
 return out

def main(stage):
 plan=read(P/'research/confirmation_protocol_v036.json');freeze=read(P/'research/freeze_v036.json');scientific=read(P/'research/confirmation_selection_v036.json');lock=read(O/'locked_before_F.json');split=read(O/'F_split.json')
 need(sha(P/'research/confirmation_protocol_v036.json')==freeze['protocol_sha256']==AUDITED_PROTOCOL,'Frozen protocol');need(hashlib.sha256(code(P/'confirmation_v036.ipynb').encode()).hexdigest()==freeze['source_code_sha256']==AUDITED_SOURCE,'Frozen driver code')
 for rel,h in plan['input_hashes'].items():need(sha(P/rel)==h,'Input:'+rel)
 for name,h in plan['source_code_hashes'].items():need(hashlib.sha256(code(P/'research'/name).encode()).hexdigest()==h,'Component:'+name)
 A=read(P/'outputs/controlled_experiments_v035/screen_summary.json');Areview=read(P/'research/screen_review_v035.json');eligible=[v for v in A['candidates'] if v['gain']>=.003 and v['interval']['high']<0];best=min(eligible,key=lambda v:(v['MAE'],v['name']))
 need(Areview['status']=='passed' and best==A['selected_for_confirmation']==Areview['selected']==scientific['winner'] and best['name']==plan['winner_name'] and best['weights']==plan['winner_weights'],'Only lowest predeclared eligible A recipe')
 need(plan['members']==scientific['required_members'] and plan['baseline_weights']==scientific['baseline_weights'],'All seven A-selected budgets and both policies frozen')
 selection=digest(lock);need(lock['F_split_file_sha256']==sha(O/'F_split.json') and lock['source_code_sha256']==AUDITED_SOURCE and lock['protocol_sha256']==AUDITED_PROTOCOL,'Prelabel runtime lock identity')
 need(lock['members']==plan['members'] and lock['winner_weights']==plan['winner_weights'] and lock['baseline_weights']==plan['baseline_weights'] and lock['cold_fit_all_members'] and lock['no_runner_up'] and lock['no_F_epoch_or_weight_selection'],'Locked scientific recipe and guards')
 sources=dict(plan['source_code_hashes'],**{'confirmation_v036.ipynb':AUDITED_SOURCE,'controlled_experiments_v013.ipynb':'56cb9d7e824e58126bddd71c7c0f7063844974c31ee00a6dac23f2112657615a','confirmation_protocol_v036.json':AUDITED_PROTOCOL,'locked_before_F.json':selection})
 need(hashlib.sha256(code(P/'controlled_experiments_v013.ipynb').encode()).hexdigest()==sources['controlled_experiments_v013.ipynb'],'Frozen helper')
 os.environ['PA3_RUN_V036']='0';ns={'__name__':'__main__'};exec(compile(code(P/'confirmation_v036.ipynb'),'confirmation_v036.ipynb','exec'),ns)
 for name in plan['source_code_hashes']:exec(compile(code(P/'research'/name),name,'exec'),ns)
 torch.set_num_threads(4)
 known=pd.read_csv(P/'data/train.csv',usecols=['id','breath_id','R','C','time_step','u_in','u_out'],dtype=dict(id='int64',breath_id='int32',R='int8',C='int8',time_step='float32',u_in='float32',u_out='int8'));bids=known.breath_id.to_numpy().reshape(-1,80)[:,0];phase=known.u_out.to_numpy().reshape(-1,80);rows=known.id.to_numpy().reshape(-1,80);rc=known[['R','C']].to_numpy()[::80]
 with np.load(P/'outputs/improvements_v005/sequence/split_breath_ids.npz') as z:
  afit=np.sort(pd.Index(bids).get_indexer(z['A_fit']));aval=np.sort(pd.Index(bids).get_indexer(z['A_validation']))
 joint=np.searchsorted([5,20,50],rc[:,0])*3+np.searchsorted([10,20,50],rc[:,1]);fi,vi=train_test_split(afit,test_size=6791,random_state=20261204,stratify=joint[afit]);fi=np.sort(fi);vi=np.sort(vi)
 need(len(fi)==54323 and len(vi)==6791 and not np.intersect1d(fi,vi).size and not np.intersect1d(np.r_[fi,vi],aval).size and np.array_equal(np.sort(np.r_[fi,vi]),afit),'Independent known-input-only grouped F split')
 for key,indices in [('A_fit',afit),('A_validation',aval),('F_fit',fi),('F_validation',vi)]:need(np.array_equal(indices,split['indices'][key]),'Exact split indices:'+key)
 need(np.array_equal(bids[fi],split['breath_ids']['F_fit']) and np.array_equal(bids[vi],split['breath_ids']['F_validation']) and rawhash(bids[fi])==split['group_hashes']['F_fit'] and rawhash(bids[vi])==split['group_hashes']['F_validation'],'Exact F breath IDs/group hashes')
 x,names,xbids=ns['make_sequence_features'](known,'combined');del known;gc.collect();need(x.shape==(67905,80,47) and np.array_equal(xbids,bids),'Full known47 features, native group order')
 yfit=labels_for(bids[fi]);fitx=x[fi];fitphase=phase[fi];expected_arrays=dict(x_sha256=arrayhash(fitx),y_sha256=arrayhash(yfit),out_sha256=arrayhash(fitphase));train_points=int((fitphase==0).sum());steps=math.ceil(len(fi)/256);required=list(plan['members']) if stage=='complete' else plan['stages'][stage];records={};cpu_cache_differences={}
 proof=read(O/'course_proofs.json');need(proof['status']=='passed' and proof['actual_cuda'] and proof['cold_confirmation_contract'] and proof['driver_source_code_sha256']==AUDITED_SOURCE and proof['protocol_sha256']==AUDITED_PROTOCOL and all(proof['checks'].values()) and all(t<=19800 for t in proof['projected_stage_seconds'].values()),'Actual CUDA confirmation and lease-reserve proof')
 for name in required:
  recipe=plan['members'][name];directory=O/'F_models'/name;record=read(directory/'record.json');report=read(directory/'report.json');expected_identity=dict(selection_sha256=selection,member_id=name,recipe=recipe,training_group_sha256=split['group_hashes']['F_fit'],source_fingerprints=sources)
  need(record['identity']==expected_identity and record['identity_sha256']==digest(expected_identity),'Identity:'+name)
  for key,hkey,filename in [('checkpoint_file','checkpoint_sha256','model.pt'),('last_checkpoint_file','last_checkpoint_sha256','model.last.pt'),('report_file','report_sha256','report.json')]:need(record[key]==str((directory/filename).relative_to(P)) and sha(P/record[key])==record[hkey],'Cold-run path/hash:'+name+':'+filename)
  ck=torch.load(directory/'model.pt',map_location='cpu',weights_only=False);last=torch.load(directory/'model.last.pt',map_location='cpu',weights_only=False);spec=ns['canonical_model_spec'](recipe['model_spec']);cfg=ns['_train_configuration'](recipe['train_cfg']);budget=recipe['selected_epochs'];prep=ns['fit_preprocessor'](fitx,yfit,fitphase,recipe['model_spec'],names,scaler_phase='all',residual_baseline=False)
  need(report['completed'] and not report['validation_used'] and report['training_breaths']==54323 and report['executed_epochs']==budget==ck['epoch']==last['epoch'] and len(ck['epochs'])==len(last['epochs'])==budget and last['completed'],'Fixed complete budget/no holdout selection:'+name)
  need(report['executed_lr_schedule']==report['selected_lr_schedule']==recipe['lr_schedule']==[e['lr_used'] for e in ck['epochs']] and recipe['lr_schedule']==recipe['train_cfg']['frozen_lr_schedule'][:budget],'Exact A-selected rates:'+name)
  need(ck['model_spec']==last['model_spec']==spec and ck['config']==last['config']==cfg and ck['seed']==last['seed']==20261102,'Full model/config/seed:'+name)
  need(safe(ck['preprocess'])==safe(last['preprocess'])==safe(prep),'Independently fitted Ffit-only statistics:'+name)
  need(all(torch.equal(v,last['state_dict'][k]) for k,v in ck['state_dict'].items()) and all(bool(torch.isfinite(v).all()) for v in ck['state_dict'].values()),'Final state/last-state and finite parameters:'+name)
  for saved in [ck,last]:
   fp=saved['fingerprint'];need(fp['mode']=='fixed' and all(fp[k]==h for k,h in expected_arrays.items()) and fp['extra']['lr_schedule']==recipe['lr_schedule'],'Ffit-only arrays and fixed mode:'+name+':'+str(saved is last))
   need(not any(k.startswith('val_') for k in fp['extra']) and not saved['validation_used'],'No validation arrays supplied to fitter:'+name+':'+str(saved is last))
  need(ck['optimizer_steps']==last['optimizer_steps']==report['optimizer_steps']==steps*budget,'Full optimizer-step count:'+name)
  for i,e in enumerate(ck['epochs'],1):
   need(e['epoch']==i and e['optimizer_steps']==steps and e['cumulative_optimizer_steps']==steps*i and e['training_scored_points']==train_points and not e['validation_used'] and 'validation_inspiratory_mae' not in e,'Fixed epoch/no validation metric:'+name+':'+str(i))
  if name not in ['deep','original_compact']:
   need(ck['v008']['source_fingerprints']==sources and ck['v008']['arm']=='v036_F_'+name and ck['v008']['loss_kind']==('curve_l1' if recipe['loss_kind'] in ['curve_l1','laplace_curve'] else 'l1'),'Wrapped source/actual transport identity:'+name)
  if name=='capacity_laplace_curve':need(ck['actual_training_objective']=='laplace_curve' and ck['v029']['objective']==ns['V029_OBJECTIVE'] and report['actual_training_objective']=='laplace_curve' and ck['v029']['arm']=='v036_F_'+name,'Actual Laplace objective identity')
  model=ns['V5PressureRNN'](recipe['model_spec'],47) if name in ['deep','original_compact'] else ns['v036_factory'](name)(recipe['model_spec'],47,ck['preprocess']);need({k:tuple(v.shape) for k,v in model.state_dict().items()}=={k:tuple(v.shape) for k,v in ck['state_dict'].items()} and sum(v.numel() for v in model.parameters())==report['parameter_count'],'Architecture shapes/parameter count:'+name)
  records[name]=record
  if stage=='complete':
   # Independent manual reconstruction avoids weakening Python-version-specific
   # factory bytecode guards in the production loader. Hashes and shapes checked above.
   model.load_state_dict(ck['state_dict'],strict=True);selected=np.sort(np.random.default_rng(20263603).choice(len(vi),64,replace=False));transformed=ns['transform_inputs'](x[vi[selected]],ck['preprocess']);native=ns['_predict_native'](model,transformed,ck['preprocess'],torch.device('cpu'),32);mask=phase[vi]==0;dense=np.zeros_like(mask,dtype=np.float64);dense[mask]=np.load(directory/'F_predictions.npy');difference=float(np.max(abs(native.astype(np.float64)[phase[vi[selected]]==0]-dense[selected][phase[vi[selected]]==0])));grid=np.unique(yfit[fitphase==0]).astype(np.float64);spacing=float(np.median(np.diff(grid)));need(difference<spacing/100,'Independent64-breath CPU cache check within1/100training-pressure-step:'+name);cpu_cache_differences[name]=difference
  del ck,last,model,prep;gc.collect()
 if stage!='complete':
  status=read(O/('stage_complete_'+stage+'.json'));need(status['status']=='stage_complete' and status['selection_sha256']==selection and status['source_code_sha256']==AUDITED_SOURCE and status['protocol_sha256']==AUDITED_PROTOCOL and status['records']==records,'Exact completed stage record set')
  need(not(O/'confirmation_result.json').exists(),'Partial stage is not completed confirmation')
  result=dict(status='passed_stage_only',stage=stage,created_utc=datetime.now(timezone.utc).isoformat(),check_count=len(checks),checks=checks,selection_sha256=selection,records_sha256={n:sha(O/'F_models'/n/'record.json') for n in records},no_F_validation_pressure_read=True,confirmation_complete=False,final_fit_not_eligible_from_stage_only=True,audit_source_sha256=sha(Path(__file__)))
  target=P/('research/confirmation_stage_review_v036_'+stage+'.json')
 else:
  resultfile=read(O/'confirmation_result.json');need(resultfile['status']=='complete' and resultfile['selection_sha256']==selection and resultfile['source_code_sha256']==AUDITED_SOURCE and resultfile['protocol_sha256']==AUDITED_PROTOCOL and resultfile['records']==records,'Completed seven-member F result bound to frozen recipe')
  mask=phase[vi]==0;ids=rows[vi][mask];need(np.array_equal(ids,np.load(O/'F_row_ids.npy')) and rawhash(ids)==resultfile['F_row_ids_array_sha256'],'All native F row IDs')
  grid=np.unique(yfit[fitphase==0]).astype(np.float64);need(np.array_equal(grid,np.load(O/'F_fit_pressure_codebook.npy')),'Ffit-only pressure grid')
  predictions={}
  for name in required:
   p=np.load(O/'F_models'/name/'F_predictions.npy');artifact=resultfile['prediction_artifacts'][name];need(p.dtype==np.float64 and p.shape==ids.shape and np.isfinite(p).all() and sha(P/artifact['file'])==artifact['file_sha256'] and rawhash(p)==artifact['array_sha256'] and artifact['row_ids_sha256']==rawhash(ids),'Native prediction artifact:'+name);predictions[name]=p
  def blend(weights):
   values=np.stack([predictions[k] for k in weights]);w=np.array(list(weights.values()));order=np.argsort(values,axis=0,kind='stable');v=np.take_along_axis(values,order,axis=0);sw=np.take_along_axis(np.broadcast_to(w[:,None],values.shape),order,axis=0);cum=sw.cumsum(0);columns=np.arange(len(ids));median=.5*(v[(cum>=.5).argmax(0),columns]+v[(cum>.5).argmax(0),columns]);hi=np.searchsorted(grid,median).clip(0,len(grid)-1);lo=np.maximum(hi-1,0);return np.where(abs(median-grid[lo])<=abs(median-grid[hi]),grid[lo],grid[hi])
  baseline=blend(plan['baseline_weights']);candidate=blend(plan['winner_weights']);need(np.array_equal(baseline,np.load(O/'baseline_F_predictions.npy')) and np.array_equal(candidate,np.load(O/'candidate_F_predictions.npy')),'Independent weighted-median midpoint and nearest Ffit-grid policies')
  prediction_lock=read(O/'predictions_locked_before_F_pressure.json');need(prediction_lock['no_validation_pressure_loaded'] and prediction_lock['selection_sha256']==selection and prediction_lock['baseline_sha256']==sha(O/'baseline_F_predictions.npy') and prediction_lock['candidate_sha256']==sha(O/'candidate_F_predictions.npy') and prediction_lock['artifacts']==resultfile['prediction_artifacts'],'Every prediction locked before F label scoring')
  truth=labels_for(bids[vi])[mask].astype(np.float64);need(rawhash(truth)==resultfile['F_truth_array_sha256'],'Independent F labels/float32 native parse');be=abs(baseline-truth);ce=abs(candidate-truth);gain=float(be.mean()-ce.mean());need(abs(gain-resultfile['gain'])<1e-15 and float(be.mean())==resultfile['metrics']['baseline']['mae'] and float(ce.mean())==resultfile['metrics']['candidate']['mae'],'Exact native point-weighted F mean MAEs')
  counts=mask.sum(1);delta=ce-be;sums=np.add.reduceat(delta,np.r_[0,np.cumsum(counts)[:-1]]);rng=np.random.default_rng(20263601);draws=[]
  for _ in range(1000):
   sample=rng.integers(0,len(vi),len(vi));multiplicity=np.bincount(sample,minlength=len(vi));draws.append(float(multiplicity@sums/(multiplicity@counts)))
  low,high=np.quantile(draws,[.025,.975]);need(abs(low-resultfile['interval']['low'])<1e-15 and abs(high-resultfile['interval']['high'])<1e-15,'Independent paired whole-breath point-weighted1000-draw interval');passed=bool(gain>0 and high<0);need(resultfile['passed']==passed and resultfile['cold_fit_all_members'] and resultfile['no_F_epoch_or_weight_selection'] and resultfile['original_A_validation_excluded'] and resultfile['confirmation_is_resampling_evidence'] and resultfile['no_runner_up_after_failure'],'Frozen confirmation acceptance and limitations')
  result=dict(status='passed',created_utc=datetime.now(timezone.utc).isoformat(),check_count=len(checks),checks=checks,confirmation_result_sha256=sha(O/'confirmation_result.json'),selection_sha256=selection,scientific_selection_sha256=sha(P/'research/confirmation_selection_v036.json'),passed=passed,gain=gain,baseline_MAE=float(be.mean()),candidate_MAE=float(ce.mean()),interval=[float(low),float(high)],cpu_cache_maximum_differences=cpu_cache_differences,CPU_cache_limit='1/100 of Ffit observed pressure-step spacing;64 fixedseed known-input-selected breaths, no change to GPU scores',audit_source_sha256=sha(Path(__file__)))
  target=P/'research/confirmation_review_v036.json'
 need(sha(P/plan['best_CSV'])==plan['best_CSV_SHA256'],'Official accepted CSV preserved')
 with target.open('x') as f:f.write(json.dumps(result,indent=2,allow_nan=False)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--stage',choices=['first_five','remaining_two','complete'],required=True);main(parser.parse_args().stage)

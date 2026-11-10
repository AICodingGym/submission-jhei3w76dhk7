# Latest training check: deep_curve50/196

Nov9 **6:10:34PM Pacific**: pod2973011 Runningn06, cold deep_curve **50/196epochs**, GPU91%/1734MiB. All five earlier Fmembers completed; capacity_laplace_curve190 waits sequentially. Guardian/reporter healthy,11scheduledchecks/noerrors. No Fvalidation score yet; fixed budgets and withheld Flabels unchanged. Leaseends11:39:47PM; currenttargetofficialmeanMAE<=0.1638,acceptedbest0.17427. Chatturn keptopen for10-minute updates; next6:20. Waitbetweenchecks. Source/payload/archive/audit/monitor paths in the next entries. Preserve userbaselinechange and all artifacts.

---

# Latest live state: second-stage GPU allocated, job starting

Nov9 **5:40:34PM Pacific** scheduled check: pod**2973011 Running on n06**, actual start**5:39:47PM**, six-hour lease ends**11:39:47PM**. Queue lasted2h22m06s. Guardian2973272 dispatched successfully. Wrapper127/executor185 are alive, loading approved data; no completed new epoch observed yet. Exact cached actualCUDA130component+32pruner proofs verified against same Python3.11.9/np1.26.4/Torch2.2.1+cu121/cuDNN8902/GTX1080Ti runtime and frozen source/data/helpers; no synthetic rerun. Deep_curve196 then capacity_laplace_curve190 remain cold fixed-budget fits, about5h total. First5Fmembers already completed and independently audited1076checks. No Fvalidation result/newofficial score/finalfit/submission yet. Primary official meanMAEtarget<=0.1638, acceptedbest0.17427.

Server ten-minute reporter3012588 is healthy, eight scheduled checks through5:40, no errors; next5:50. Current chat turn is being kept open for10-minute updates after user clarified they expected chat reports, rather than saved server logs alone. Wait between checks to conserve usage. Read `monitor-every10/summary.jsonl` in remaining_two login stage; `research/periodic_monitor_v036.json` has paths/PIDs. Continue exact frozen protocol and prepared complete audit after verified archival. Preserve all artifacts and baseline_v001.ipynb user modification.

---

# Automatic ten-minute checks are running remotely

Nov9 **4:20:34PM Pacific**: at the user's request, installed a single read-only DataHub monitor **PID3012588**, interval **600seconds**, next scheduled check **4:30:34PM Pacific**. It writes full observations and compact summaries every10minutes on the login server and stops after verified archival or a terminal pod. It does not train, allocate/delete pods, submit or message anyone. It survives Mac sleep and holds a single-instance flock. Existing operational guardian2973272 continues its lease/dispatch/backup duties; do not launch a duplicate monitor or pod.

Monitor source `outputs/confirmation_v036/monitor/monitor_every_10m.py`, SHA25627f1da0b7585eaad3c0ffc94f1026b048355e2c96058ef7c91e5382c3f4f40e0. Remote stage `$HOME/.pa3-setup-control.gty67K/v036-F-remaining_two-20261109`; report directory `monitor-every10/`, compact `summary.jsonl`, full `<UTC>.json`, `events.jsonl`, optional `errors.jsonl`. PID/config `research/periodic_monitor_v036.json`. Reporter launch/event files verify it started and scheduled its first check. Latest actual live read **4:18:48PM**: pod2973011 still Pending/no node/start. Current target official meanMAE<=0.1638; best0.17427. First5coldmodels/archive/1076audit complete; two remaining wait for GPU, ~5h once started. See older current-state entry for source/payload/audit details. Preserve all files and baseline_v001.ipynb user change.

---

# Live process check: queued, no training active

Nov9 **3:29:08PM Pacific**: only pod2973011 is Pending, with no node/startTime. Scheduler reports eligible GPU slots occupied; no queue position or start estimate. Guardian2973272 is alive and waiting, and will dispatch the reviewed remaining_two pipeline when Ready. Neither deep_curve196 nor capacity190 has started. Firstfive training/archive/1076-check audit are complete. No final fit or new submission is running. Current primary target remains official MAE<=0.1638; accepted best0.17427. About5h for the queued stage after scheduling. Next check>=3:39:08PM; preserve files/source/recipes, no duplicate requests.

---

# Current target and live state: MAE <=0.1638; stage two queued

The user's latest primary goal is **accepted official inspiratory mean MAE <=0.1638**. The updated PA3 handout confirms this as the historical median benchmark and +1 bonus cutoff (pages2,5). Current accepted best remains **0.17427**; target is unmet. Current instructions are in `research/active_objective.json` and `research/OBJECTIVE_01638.md`. The updated PDF is preserved in `handoff/course_context/PA3_updated_20261109.pdf`, SHA256dd784dab2b94d61174c1a98a7b9bb46e5bb82667f00cb0d72e5ae99d7cdef460. Original PDFs and old <=0.15 protocol/goal files remain historical. The app Goal object still reports usageLimited with the old objective; replacement API rejected an unfinished existing goal. Do not mark that old unmet goal complete to change its label. Continue actual project work against the user's new target.

**November9,3:19:34PM Pacific:** requested one ordinary six-hour GPU pod **v2gao-2973011**, last observed **Pending** with no startTime/node. Guardian **2973272** waits remotely in `$HOME/.pa3-setup-control.gty67K/v036-F-remaining_two-20261109`. It deploys the reviewed payload when Ready, verifies source/data/cached actual-CUDA proof runtime, and cold-fits **deep_curve196** then **capacity_laplace_curve190** on the same Ffit groups. About **five GPU hours once scheduled**, plus prediction/audit; no reliable queue/start estimate yet. No actual second-stage CUDA start/epoch/lease end observed. No duplicate pod allocation or automatic replacement. Read-only monitor: `bash outputs/confirmation_v036/monitor/check_remaining_two_v036.sh`; store full JSON but display a short progress summary. Check roughly every10minutes; next>=3:29:34PM. SSH renewed~3:07PM; only ask Terminal/Duo if authentication actually fails.

All **five first-stage cold models completed** fixed budgets at about11:16AM. Independent **1076-check stage audit passed**: `research/confirmation_stage_review_v036_first_five.json` (`passed_stage_only`, no Fvalidation pressure read). Archive **252files/1,056,127,127bytes**, SHA256**68aef59d863c82eddddc08e334535a3c655aa7a5e9d1c4419426c56e3efa5c53**, locally verified every safe member in4.47s, mirrored,184new run files published preserving root notebooks and accepted CSV. `outputs/confirmation_v036/completed_archive_first_five/` holds archive, full mirror, publication/verification and failed audit logs. Original audit import failed due missing local sklearn; dependency installed, same audit code then passed; environment recorded `research/stage_audit_environment_v036.json`. Initial backup verification exceeded180s; files were safe and old pod expired12:50PM. Streaming recovery subsequently passed server-side all252members in103.18s using a private-home hardlink. Original timed-out files/helpers remain preserved. Old Failed2591068 metadata saved in new login stage before deleting only its terminal Kubernetes object.

Use operational helpers **setup_helpers_quota_v4**, source/ops commit **c53b910**. New payload60members/6,529,315bytes SHA256**68c588749ed5badef5041da82088184bf508f7dd10ffd82fb03b4daa8183969f**; pins**61f6990407dfc9f1b90c10661caffde17989b2301ca3574a2005743be01db6f9**. Forward-only tar verification, verified shared-home hardlinks,900s timeout with preserved failures;18fixture checks passed. No weaker file/hash guard. Scientific driver remains **27f89eb9f1a749e032040082b70513fc9990311eee87fcddbf7e6d5806f8138b**, protocole9fb1fc5fd7a342fd744f8ed2d7bcdbb4eab3d3e5be8f12da6f93575374ab0f4, choiceec2feebb872eaaf963ca27a1c1f61c23af0f6f1aac24b3d4a39986100b8f54ec; same across both stages. First-stage actualCUDA130component+32pruning proofs passed; stage-two runtime must verify before continuing. Keep scientific split/epochs/weights/objectives/acceptance frozen despite new project success target.

Next after all7 cold fits: archive/member-verify and publish only new/identical artifacts, preserve root source notebooks; run `.venv/bin/python outputs/confirmation_v036/review/audit_confirmation_v036.py --stage complete`. Full audit must pass and frozen Fgain>0/upper95<0 before conditional all67905 final fit. Final source `final_fit_v037.ipynb` is already prepared/frozen with corrected expected F driver pin, CPU84+3negative-gate checks passed; no actual final model reuse, fit, new CSV or submission yet. Build final deployment only with explicit raw hashes of completed passed F result and independent passed complete audit. New capacity190 all-data fit~3.5h; reuse only five exact accepted all-data members after all hashes/recipes/statistics checks. Keep accepted official0.17427 and all older files. No median-absolute-error promotion. Preserve unrelated user modification `baseline_v001.ipynb` unstaged/untouched.

---

# Current objective and checkpoint: <=0.1638; first five audited

Nov9 afternoon: user explicitly replaced the primary target with **official inspiratory mean MAE <=0.1638**. Updated PA3 PDF verified on pages2+5: historical median benchmark and+1bonus cutoff; full base accuracy points at<=0.20. Best acceptedofficial0.17427, target UNMET. Currenttarget research/active_objective.json and research/OBJECTIVE_01638.md. PreservednewPDF handoff/course_context/PA3_updated_20261109.pdf SHAdd784dab2b94d61174c1a98a7b9bb46e5bb82667f00cb0d72e5ae99d7cdef460; originalPDF/OBJECTIVE_015/frozenprotocols retained unchanged. AppGoal replacement rejected because oldusageLimited goal unfinished; no falsecompletion. Follownewuserobjectiveinprojectfiles; controllerbadgeisstale.

V036firstfive finished~11:16AM PST (workerexit0), ALL5coldbudgets complete. Stagebackup verification timedout180s; preservedarchive/coursefiles, oldpod2591068expired12:50:52. SSH renewed~3:07PM. Retrieved252file1,056,127,127BarchiveSHA68aef59d863c82eddddc08e334535a3c655aa7a5e9d1c4419426c56e3efa5c53; everymemberverifiedlocally in4.47s usingforward-onlyverifier. Safe252membermirror preserved,184newrunfilespublished withrootnotebooks/acceptedCSVunchanged. Independentfirstfiveaudit **1076checksPASSED**, `research/confirmation_stage_review_v036_first_five.json`, statuspassed_stage_only,noFvalidationlabelsread. Initialauditmissinglocal sklearn dependency fixed byinstallinglocalauditdependency; originalfailurelogpreserved, no auditcode/scientificchanges.

Operationalv4archivefix: one-passgzipmemberverification, verifiedprivate-homehardlinks,900sverificationtimeoutwithpreservedfailures.18fixturechecks passed includingcorruptmemberrejection/realbackgrounddetachment; prior159member537MBarchivecheckagreedwitholdverifier in2.14slocal. Originalv3helpers/logsretained. FrozenV036scientificsource27f89eb9.../protocole9fb1fc.../choiceec2feebb... unchangedacrossstages. Newv4payload60members6,529,315B SHA68c588749ed5badef5041da82088184bf508f7dd10ffd82fb03b4daa8183969f,pins61f6990407dfc9f1b90c10661caffde17989b2301ca3574a2005743be01db6f9. Helpers outputs/confirmation_v036/setup_helpers_quota_v4. Staged `$HOME/.pa3-setup-control.gty67K/v036-F-remaining_two-20261109`, notrequestedGPUyetatthisentry. Firststageprivatearchiverecoverynewhelperrunninginoriginalstage/archive-recovery-streaming-20261109; inspectreturn/verification.

Next requestONEordinary6hGPUafterfreshinventory/preserveoldterminalmetadata. Guardianthirdarg remaining_two, source/recipe/split unchanged, actualCUDAproofverification beforecolddeep_curve196andcapacity190. Roughly5htrainingplusaudit/queue; noFepoch/weightselection/pruning/runner-up. Afterall7predictionslockedthenFscore, independentcompleteaudit; onlypassedFadvancesconditionalall67905capacity190final(~3.5h), reusefiveacceptedall-dataafterexactchecks, alignedCSV/audit/submission. No newofficialscore orfinalfit. Fullstagearchive localoutputs/confirmation_v036/completed_archive_first_five; publisher publication.json, verification/archive.json andfailedlogs. Preservebaseline_v001.ipynbuserchange.

---

# Latest live check: four first-stage models finished

Nov9 **10:52:25AM PST**: pod2591068 Runningn05; GPU78%/1169MiB, zero restarts. Cold deep189, original_compact193, curve193 and memory191 finished training with report+record files. Offset **61/193**,~10.5s/epoch,647.98selapsed; approximately23–28min remain, firststagefinish~**11:15–11:20AM** ifpaceholds. No Fvalidation labels/outcome or newofficialscore. These completed fits await stageaudit; training MAE is not validation performance. Remaining_two notallocated, still~5h afterverifiedarchive/stageaudit/queue. Conditionalfinal~3.5h onlyaftercompleteFpass+independentaudit. Bestofficial0.17427 unchanged,<=0.15unmet.

Guardian2599277 polls normally; one earlier transient KubernetesAPI observation timeout recovered without interrupting training. Samecorrectedsource27f89eb9..., actualCUDA130+32proofs, frozenrecipes/split/epochs unchanged. Lease ends12:50:52PM, sufficient currentstage margin. Rawmonitor outputs/confirmation_v036/monitor/check_20261109T185225Z.json. Nextcheck>=11:02:25AM, about10min. No newresources/recipe/acceptancechanges. See nextentry for exactcurrentmonitor/helper/payload/stage/audit commands. Preserve unrelatedbaseline_v001.ipynb.

---

# Current checkpoint: V036 cold training actually running

Nov9 **07:24:20AM PST** ten-minute check: pod`v2gao-2591068` Runningn05, actualGPU94%/1739MiB, no restarts. Firstmember deep **17/189epochs**,34.17s/epoch,590.34selapsed,213optimizersteps/epoch. Otherfourfirststage members queued sequentially, remaining_two notallocated. Guardian2599277detached/activelypolling, wrapper299/executor370live. Currentlease ends**12:50:52PM PST**. SamefixedknownFsplit membership confirmed afterone-lineE->Fmetadata-keycorrection, driver**27f89eb9f1a749e032040082b70513fc9990311eee87fcddbf7e6d5806f8138b**. ActualCUDA130component+32prunerpassed. No Fvalidation pressure/outcome and NOnewofficialscore. Do notreport trainingMAEasvalidation.

About4hremainfirstfive, then~5hsecondstage plusarchive/audit/queue; conditionalfinalcapacity190onall67905~3.5h onlyifcompleteFpass+independentaudit. Root mustmember-verify firststagearchive, publishnew-or-identicalrunfileswithoutoverwritingrootnotebooks, run prepared stageaudit `outputs/confirmation_v036/review/audit_confirmation_v036.py --stage first_five` inproject.venv, thenrequestnormalnextGPU. Samecorrectedpayload/driver/protocol acrossstages. New58member6,527,913BpayloadSHA1612f50980dcbe82a1d6661e9b26e80f4c57bb42ef9b763c6013f7fa0ac459a4, pins9f19dffb93aa407108b28e96d8b6fcb76adbebec17b7e51f8f20573c8d12bc87 in setup_helpers_quota_v3. Stage2guard withthirdarg remaining_two andfreshloginstage usesattemptpod-remaining_two-r3; neverreuseoldv2helpers. Guardianarchivesprivately, verifiesmembersbeforeGPUrelease; noautomaticresourceallocation orsubmission.

Currentlogin stage `$HOME/.pa3-setup-control.gty67K/v036-F-first_five-schema-corrected-20261109`; private runtime `.pa3-preserved-course-backups/v036-runtime/v2gao-2591068-first_five-r3`. SSH renewedNov9~06:27. Checkabout10m, next>=**07:34:20**. Readonly exactmonitor command saved `outputs/confirmation_v036/monitor/check_current_v036.sh`; parse/storefullJSON but displayconcise progress toconserve tokens. Rawlastobservation schema_corrected_check_20261109T152420Z.json, orchestration_v036.json current.

Storagequota repairedwithoutmovingmodels/data/submissions:35backuparchives3.79GBchecksumverifiedprivately, originalpathsrestored, writeprobe passed. Oldquotaattempt36filearchive9988637...preservedverified. Failedschemaattempt159files537,736,795Bf3452225... nowLOCALverifiedALLmembers too; originaldrivers/proofs/locks/logs preserved. CorrectedCPU124+ops16 andconditionalfinalCPU84+3passed; source/opscommittedb3768f4. Bestofficial**0.17427**preserved,target<=0.15unmet. ConditionalV037preparedbutinert; nofinalfit/reuse/CSV/submission. Preserve unrelateduserbaseline_v001.ipynb change.

---

# Current checkpoint: corrected V036 CUDA passed; preprocessing

Nov9 07:13:55AM PST: same GPU2591068 Running n05, lease ends12:50:52PM. Corrected driver27f89eb9... passed actualCUDA130component+32prunerchecks. Exact Ffit/Fval breathmembership and group hashes MATCH preserved failed attempt (onlymetadata key names changed). New guardian2599277 detached successfully; dispatched and started-pod records exist, statuspolling pending, wrapper299/executor370 live. Stage `$HOME/.pa3-setup-control.gty67K/v036-F-first_five-schema-corrected-20261109`; private runtime `.pa3-preserved-course-backups/v036-runtime/v2gao-2591068-first_five-r3`. Nofirstepoch observed yet whiledata preprocesses. NoFvalidationoutcome. Projectionsfirstfive15,243.91s (4.23h), remainingtwo17,734.96s (4.93h); firststage fits remaininglease with30minreserve. Rawmonitor outputs/confirmation_v036/monitor/schema_corrected_check_20261109T151355Z.json. Checknext>=07:23:55AM, ~10minutes.

Sourcecorrection/CPU124/ops16/final84+3 and originals are committedb3768f4. Newpayload1612f50980dcbe82a1d6661e9b26e80f4c57bb42ef9b763c6013f7fa0ac459a4, pins9f19dffb93aa407108b28e96d8b6fcb76adbebec17b7e51f8f20573c8d12bc87. Scientificprotocol/selection/recipesunchanged. Failedschema159member537,736,795BarchiveSHAF3452225... retrieved locally; independentlocalmemberverificationinprogress33619 (alreadydirectprivateverified). No newpodallocationforcorrection. Priorquota fullyrepaired andallfilespreserved. Bestofficial0.17427 unchanged;<=0.15unmet. No finalfit/submission. Olderentriesarehistory; usecurrent r3guardian/source.

---

# Current checkpoint: one-line F schema correction, same GPU lease

Nov9 ~07:12AM PST: first GPU retry reached production driver but failed BEFORE ANY F FIT/CHECKPOINT with KeyError F_fit. Split serializer retained old E_fit/E_validation names while member identity/audit required F_fit/F_validation. Only one driver line changed to F keys; split seed/membership algorithm/numeric values/recipes/budgets/weights/protocol/acceptance unchanged. Original sources/locks/proofs/executed notebook/logs preserved. `research/schema_correction_v036.json`. Original scientific choiceSHAec2feebb... and protocole9fb1fc... unchanged; corrected driver codeSHA **27f89eb9f1a749e032040082b70513fc9990311eee87fcddbf7e6d5806f8138b**. Corrected CPU124 checks passed, with new actual production split-assignment -> member-identity integration for all7. Original protocol-pinned historical115proof preserved; corrected proof separately research/confirmation_schema_preflight_review_v036.json. No Fvalidation labels/outcome; old Ffit-only labels had been loaded before failure.

Also fixed ops background compound-command stream inheritance: mkdir && nohup ... & left guardian kubectl attached. Changed to sequential mkdir then standalone nohup; actual subprocess pipe-closure proof passed. Ops16checks passed, new helper folder setup_helpers_quota_v3; attempt v2gao-2591068-first_five-r3, private runtime uses this distinct name. Old guardian2591295+its blocked kubectl2591348 stopped only after worker alreadyfailed; idle wrapper116/sleep stopped, all evidence preserved. No GPU/pod was deleted or replaced: same2591068/n05 lease06:50:52–12:50:52 PST. New login stage `$HOME/.pa3-setup-control.gty67K/v036-F-first_five-schema-corrected-20261109`. New58member6,527,913BpayloadSHA1612f50980dcbe82a1d6661e9b26e80f4c57bb42ef9b763c6013f7fa0ac459a4; pins9f19dffb93aa407108b28e96d8b6fcb76adbebec17b7e51f8f20573c8d12bc87. Prepared/staged, corrected dispatch next, actual revised CUDA proof still required.

Failed-schema snapshot preserved privately537,736,795B/159members SHAf34522253b39800f7d230d1fde14132b1db5a8e38e4cab54eec633b492e58741, direct private-home verification passed every safe member. Manual copy helper first failed because caller omitted KUBECONFIG, not an archive failure; guardian already exports correct env. Remote failedproofs under outputs/confirmation_v036/failed_schema_attempt_20261109. Local originalfiles outputs/confirmation_v036/schema_error_preserved. No `.pt` in F_models, no confirmationresult. Same F membership hashes:a0684065...fit/eed45777...validation; verify recreated known split matches these, never resample/search.

Conditional V037 final source expected-driver pin updated only; CPU84+3negativegates rerun passed. Originalsource/proofs preserved. No final training/reuse/newCSV/submission. Accepted official0.17427 preserved, <=0.15 unmet. Preserve user baseline_v001.ipynb. After launch verify guardian dispatch returns, revisedCUDAproofs pass, and first real epochs. Then ten-minutechecks. Frozen firstfive~4h, secondstage~4.7h only after verified stage archive/audit. No automatic resource allocation or F epoch/weight selection.

---

# Current checkpoint: V036 GPU retry passed CUDA; loading data

Nov9 06:52AM PST actual check: new ordinary pod `v2gao-2591068` Running n05, GTX1080Ti. Actual lease **06:50:52AM–12:50:52PM PST**. Detached guardian2591295 in `$HOME/.pa3-setup-control.gty67K/v036-F-first_five-retry-20261109`. Actual CUDA component121 + pruning32 checks PASSED; strict runtime Py3.11.9/np1.26.4/Torch2.2.1+cu121/cuDNN8902. Wrapper/executor live; F known-input split created, no member epoch observed yet while approved data preprocesses. No Fvalidation outcome. Updated ops payload55members6,519,867B SHA104d1ef7e3b9016dcca9a2cc0e72083dbe77a27fa4b8b959286ad4bf786a8c79, pins5f0dbf5b0cb9e8b78f709aa6702285b59e9e587c1711aa77aea968efaed531f0. Same frozen scientific source/protocol/choice. Raw monitor outputs/confirmation_v036/monitor/retry_check_20261109T145200Z.json.

Quota repair is complete (35 archives3.79GB, all paths restored, writeprobe passed). Partial old CUDA failure evidence safely archived and member-verified locally. CPU recovery pod2585033 released; old Failed1978631 metadata preserved/objectdeleted. No duplicate resources. First_five is compact/deep/curve/memory/offset, cold fixedbudgets, about4h; then independently verify archive and stage-only audit before requesting remaining_two (~4.7h). No automatic resource allocation. Monitor about10minutes; next >=07:02AM. Checkpoint/log/status/archive on private storage, course model/data paths unchanged. No training-based pruning or Fepoch/weight/runner-up selection.

Conditional final V037 prepared/frozen/CPU84+3 checks but inert: no complete Fpass/audit, final fit or newCSV/submission. Best official0.17427 preserved, <=0.15 unmet. Preserve unrelated baseline_v001.ipynb modification. Source/operationscommit e029912. Older entries are historical; current running pod supersedes expired one.

---

# Current checkpoint: storage repair verified; preparing GPU retry

Nov9 06:49AM PST: 35 owned setup backup archives (3,793,461,768 bytes) copied/hashed/fsynced to separate private persistent home and all original paths restored as same-content symlinks. Course write probe 9,961,472 bytes passed. No model/data/submission files moved. `research/quota_recovery_v036.json` records repair. Partial CUDA failed attempt preserved: 36 files, 122,982,006-byte archive SHA998863711bf8084c871e443117064c57e57e0b387ed6e016def5a1441ac9ffd3; locally verified every member. No F split/models/outcome exists.

Operational private logs/status/archive and five-observation missing-worker detection passed 15 local checks plus real CPU deployment/idle probe. Helpers `outputs/confirmation_v036/setup_helpers_quota_v2`; payload55members/6,519,867bytes SHA104d1ef7e3b9016dcca9a2cc0e72083dbe77a27fa4b8b959286ad4bf786a8c79, pins5f0dbf5b0cb9e8b78f709aa6702285b59e9e587c1711aa77aea968efaed531f0. Original helpers/payload/evidence preserved. Old Failed1978631 metadata preserved before deleting terminal object. CPU2585033 about to release; no new GPU requested at this checkpoint. Retry login stage `$HOME/.pa3-setup-control.gty67K/v036-F-first_five-retry-20261109`. Launch normal first_five pod only after fresh inventory, actual CUDA proof before F fit. Scientific V036 source/protocol/choice unchanged.

Conditional V037 final notebook frozen515a8348..., CPU84+3 negative checks passed, inert/no final fitting. Best official0.17427 preserved, <=0.15 unmet. See next older entry for scientific confirmation details, but supersede its storage status with this entry. Preserve unrelated `baseline_v001.ipynb` user change.

---

# Current checkpoint: quota recovery before restarting V036

Nov9 morning: SSH renewed. Old GPU pod `v2gao-1978631` expired at 02:09AM PST without starting F training. Confirmed root cause is course filesystem `Errno122` disk quota during synthetic CUDA preflight; no OOM, restart or actual F model fit was found. The old guardian could not see a terminal status because logging/status used the same full filesystem. Preserve original failed evidence.

A CPU-only recovery pod `v2gao-2585033` is running. Only owned `setup/*.tar.gz` backup archives are being copied/hashed/fsynced to private persistent home `.pa3-preserved-course-backups/v036-20261109`; all copies must verify before source relocation and compatibility links. First 5,095,539-byte archive was preserved privately but quota still prevented restoring its original link; the batch repair explicitly includes that path. Batch relocation currently executing; verify its migration result, all original paths and write probe before claiming repair complete. No model/dataset/submission files moved.

Scientific V036 source, selection and protocol remain frozen. Preparing revised operational helpers in `outputs/confirmation_v036/setup_helpers_quota_v2` to log/status/archive privately and detect missing workers conservatively. Original helpers/payload preserved. No new GPU allocated yet. After repair preserve partial proof files, verify no F models/labels/outcomes, test revised helpers, then request one normal first_five GPU pod. Actual CUDA proofs must pass before training. About9 GPU hours total across two ordinary sequential pods, plus conditional final fit; no new reliable finish time until training starts.

Conditional `final_fit_v037.ipynb` and preflight/freeze JSON are prepared, CPU84 plus3 negative-gate checks passed. They are inert: no F pass, accepted-model reuse, final fit or new CSV/submission. Final requires independently passed complete F confirmation and exact hashes. Accepted official MAE0.17427 preserved; <=0.15 unmet. Do not confuse A0.1775294806 with official or median MAE. Preserve unrelated user change `baseline_v001.ipynb` untouched.

---

# Live checkpoint: cold F V036 first stage requested

November8 8:09PM Pacific: requested one ordinary6h DataHub podv2gao-1978631, lastobservedPending; guardianPID1978812, login stage$HOME/.pa3-setup-control.gty67K/v036-F-first_five-20261108. Actual node/start/leaseend/CUDAproof/firstepoch not yet retrieved. No other pods existed immediately before launch; no duplicate/automatic allocation. Guardian receives explicitstagefirst_five, deploys once and runs actualCUDA32pruner+confirmation/full-capacity proofs before any Ffit. Status/log filenames isolated bystage so stage2 cannot mistake first-stage exit0 for its own. Backup per-file verified before GPU release. Mac-independent remote controller; root launches stage2 only after verified backup/audit, not automatically.

V036 scientific choice remains frozenV035replacement A0.1775294806070807; baselineA0.18292209456473527, officialbest0.17427 unchanged, goal<=0.15UNMET. New driver confirmation_v036.ipynb/source aa340df0768a75f4c942ce0107b2ea0eb21b5ac39fc45461f44a768a0c0d488e and protocol research/confirmation_protocol_v036.json SHAe9fb1fc5fd7a342fd744f8ed2d7bcdbb4eab3d3e5be8f12da6f93575374ab0f4 frozen git04aab2d BEFORE Fsplit/labels/outcomes. CPU115checks passed (all7 full architectures fixed2epochfits, actual memory+capacity exact optimizer/RNG resume, target-membership poison test, lock ordering, input-onlymedian/grid and inherited73capacityproofs). ActualCUDAproofs still to inspect. A toy fixture initially omitteddt; switched to real frozen47feature builder using syntheticrows; originalfailedproof preserved. Operationalpreflight child now isolatesRUN=0 whileimporting realdriver; parentRUN=1 retained forproduction. Realguarded import tested in emptytmpdir; originalunusedpayloadpreserved. One regressioncommandinitiallyusedsystemPythonwithoutTorch, reranprojectvenv; no scientificdata/model change.

Final payload6518626B/54members SHA1bc3e7c0a0077772e8b1654fa516c7c76681ca6dc0f5a0de735fb20a16e57923, sourcepins8a803646972d71f1a319379959baceee977c9b18c68f9d9e01e532970f9116ac. Helpers outputs/confirmation_v036/setup_helpers. Freeze research/freeze_v036.json, opsreviews research/operations_review_v036.json and operations_guard_isolation_v036.json. No Fmodelweights/validation outcome retrieved locally; FsplitmaynowbecreatedremotelyonlyafterCUDAproofs—inspectactualstate beforeclaimingnone. No finalfit/submission. Remaining_two NOTallocated.

Runtime design: newseedF20261204,54323fit/6791val insideoriginal61114Afit; original6791Aval excluded. All7coldmodels, noAweights. Stagefirstfive=compact193/deep189/curve193/memory191/offset193 (~4GPUh); stage2=deep_curve196+capacity190 (~4.7GPUh). ExactAselectedprefixes, fixedfitters, noFval-basedpruning/epochselection. Locks scientificchoice/source/knownsplit beforetarget conversion. Ffit-only pressure readerfiltersmembership BEFOREnumericconversion; no Fvalnumericlabels untilall7fits/predictions and both fixed median+Ffit-grid arrays hash-locked. Stage1 returnsstage_complete withnoFoutcome, notfullconfirmation. Stage2 requiresfirststage records; reruns verifypriorimmutablemodel/report/.last hashes. Source handlescompletedorphanreport beforefinishingrecord; partialfitresumesexactoptimizer/RNG. No budgettruncation.

Independent audit preparedbeforeFoutcomes: outputs/confirmation_v036/review/audit_confirmation_v036.py SHA3baf2c11b1ca9cf580e891074d2bc2f486937caaf91aa7ebcd34350e91afc6c4. Execute project.venv Python with --stage first_five afterstage1 archive verified/published; itrebuildsknownsplit/features/Ffitlabels/statistics/checkpointbudgetsandsources, NEVERFvaltargets, statuspassed_stage_only. Complete audit --stage complete onlyafterall7/confirmationresult; independentnativeensemble/grid/bootstrap plus64fixedseedCPUcachecrosschecks boundedby1/100Ffitgridspacing. Manualfrozen-stateCPUreconstruction avoidsweakeningPy3.11/3.12factory-bytecode productionguards. No auditruns yet. Statuspassed_stage_only cannot authorize finalfit.

Next: checklivepod/guardian/courseproofs/progress about10minutes after8:09request, waitbetweentoconserveusage. Coursepaths /home/v2gao/dsc102/pa3/gym-workspace/ventilator-pressure-prediction; setup/home/v2gao/dsc102/pa3/setup. Stagestatus v036-first_five-exit-code.txt, logs v036-first_five-course-preflight.log and v036-first_five-screen-execution.log. Progressoutputs/confirmation_v036/F_models/<member>/epochs.jsonl. No confirmation_v036/confirmation_result.json untilall7. Afterfirststage terminal retrievearchive/info/verification/guardian/completedpod fromloginstage intoNEWcompleted_archive_first_five; verifyhelper, safemirror/publishnew-or-identical runfiles, preserve rootnotebooks; stageaudit. Thenrootrequestoneordinarypodforremaining_two usingSAMEpayload/driver/protocol andguardian thirdarg remaining_two, newlogin stage. Source/stagefilenames isolatepriorstatus. Stage2requirescoursepersistentstage1 files; do not trainoriginalAmodelsorloadoldEmodelsinstead.

Userunrelatedbaseline_v001.ipynb modification remains untouched/unstaged. Modelinginnotebooks, approvedGymdataonly. Workerscredit-exhausted; rootdirectwork. SSHworked8:09PM; askTerminal/Duo onlyonactualfailure. Goalactive, priorgoalturnmadeprogress, no blocker/completionclaim. Potentialindependentworkwhilewaiting: prepareconditionalfinalconsumer forcapacity190+fiveacceptedall-data members, strongFpass/audit/hashgates, withoutreadingfutureFoutcome. Finalmodelsource/payloadnotimplemented yet.

---

# Current checkpoint: V035 finished and passed A; cold F not started

November8 evening actualstate. V035 completed all200epochs7:10:52PM Pacific. Larger individual model nativeA MAE0.190515300 at190 vsV0290.200130185. Both predeclared ensembles eligible: replacement0.1775294806070807 (gain0.005392613957654557;95%delta[-0.0071922913,-0.0038426843]) and retained-curve0.17872097958545247. ONLY lowest eligible replacement is frozen for confirmation. Independent1025checks passed research/screen_review_v035.json. Genuine audit-only runtime-schema KeyError fixed without changing models/predictions/protocol; original preserved. See research/RESULTS_V035.md and executed results_review_v035.ipynb; plots visually inspected, all9R/Cgroups improved.

Archive139files215642426B SHA534651e1be657c6d00e1a2b012bb1ee1e2976f2c51b2537b3622bebd062a627a retrieved and locally verified per-member; safely mirrored,55new-or-identical run artifacts published preserving root notebooks. GPU1855552 released7:11PM after verified backup; latest7:33PM check confirms absent. No active/queued project jobs known; nonewresources requested. Model best checkpointcb3db97d74927f26145a801fb572a1f8a57c28fd633484f2a8159ccaffc0961b. All source/data/model/recipe/optimizer/runtime/scale/grid/ID hashes retained. ActualCUDA78model+32pruner and CPU73checks passed; capacity was the only changed scientific factor. Officialbest0.17427 preserved; <=0.15 unmet. Do not compare A0.177529 directly to official0.17427 as if same population.

NEXT: implement staged cold-F confirmation V036 from research/CONFIRMATION_PLAN_V036_DRAFT.md. Scientific choice, both completed A alternatives, seven member recipes/budgets/weight policy and provenance already frozen in research/confirmation_selection_v036.json BEFORE any F split/labels/outcomes. Fseed20261204 remains unused. NO confirmation_v036.ipynb, execution protocol/payload/pod, Fsplit, Ffits/outcomes or final fit/submission yet. Do not claim confirmation is running. All seven must be cold-fit on F54323 and score F6791, inside originalAfit; originalAval excluded. Reuse NO originalA weights for F. Baseline six-member median+Ffit-grid versus winning six-member replacement; union7. Stages proposed firstfive compact193/deep189/curve193/memory191/offset193 (~4GPUh); second deep_curve196+NEWcapacity190 (~4.7GPUh), two normal6h pods sequentially with verified archival. Fixed fitters preserve budgets; no validation-based pruning/selection on F. Read draft for exact factory/recipe/runtime considerations and templates.

Confirmation must require positive mean-MAE gain and negative paired whole-breath1000bootstrap upper95(seed20263601), no runner-up or weight/epoch/grid-policy search. F is resampling evidence, not pristine. Only if independently confirmed: all-approved final fit NEWcapacity190, reuse only five accepted all-data models/cache after exact checks, generate/audit603600alignedCSV and authorized submit. No work beyond A-choice freeze and staged design was performed this turn; user asked for status, no extra approvals needed for already authorized confirmation.

Continue preserving unrelated baseline_v001.ipynb user modification (unstaged/untouched). Modeling in notebooks, approved Gym data only. Workers credit-exhausted; root continues. SSH worked7:33PM; askTerminal/Duo only upon actual failure. All visible AI history exported locally; source/failedattempts/logs preserved.

---

# Latest live check: V035 training148/200

November8 6:19:42PM Pacific: podv2gao-1855552 Running n05, last completed148/200,59.34s/epoch,8842.55selapsed. Native single-model validation MAE0.2067283, best0.2039534 at147. About51–55mintraining remain; estimate finish7:10–7:15PM, reviewedensemble results7:25–7:35PM ifpaceholds. No completed summary/candidate ensemble scores yet. Do not treat this single-model validation score as official performance. Official0.17427 preserved, <=0.15 unmet. Ordinaryleaseends9:50:27PM, guardian1855730 active. One transient Kubernetes API observation timeout was retried safely by guardian; training continued. No restart/newresources/recipe/pruning changes.

Rawobservation outputs/controlled_experiments_v035/monitor/check_20261109T021942Z.json; orchestration_v035.json updated. Source/protocolfreeze618e9b7 and actualCUDA78+32proofs unchanged. After completion retrieve/member-verify archive, safelymirror/publishnew-or-identical files preservingrootnotebooks, then independent A audit review/audit_A_v035.py beforepromotion. First capacity representative lacks matched history; retain frozen200budget. No Fsplit/fits/final/submission. Check about10minutes and wait; preserve unrelated baseline_v001.ipynb modification.

---

# Latest live check: V035 training58/200

November8 4:49:28PM Pacific: podv2gao-1855552 Running on n05. Actual lease began3:50:27PM and ends9:50:27PM PST. GTX1080Ti, actual CUDA model78 and pruning32checks PASSED before approved training, including full four-layer exact optimizer/RNG resume, breath reset, memory and ordinary-lease gate. Fullstep.221836s vsold.159441s (1.391x), projected3.53h within6h with30minreserve. Last completed epoch58/200,58.73s/epoch,elapsed3461.55s. Current native validation MAE.373698, best.323972 at57; these are EARLY incomplete scores, not new official results or candidates. About2h20mtraining left atcurrentpace; expectedreview7:15–7:30PM Pacific ifpaceholds. No final summary yet. First unfamiliar capacity representative continues under V025; only58epochs, no support for pruning.

Guardian1855730 continues detached, stage$HOME/.pa3-setup-control.gty67K/v035-A-20261108. Readonlyrawobservation persisted outputs/controlled_experiments_v035/monitor/check_20261109T004928Z.json; orchestration_v035.json updated. Check about10minutes and wait. No duplicate pod/new training/recipe change. Frozen sources618e9b7 and prepared audit unchanged. After completion retrieve/member-verify archive, safelymirror/publishnew-or-identical artifacts preservingrootnotebooks, then run preparedreview/audit_A_v035.py before any promotion. Fseed20261204 unused, noF/final/submission. Official0.17427 preserved, <=0.15 unmet. User modificationbaseline_v001.ipynb untouched.

---

# Latest live check: V035 queued; no GPU training yet

November8 3:28:35PM Pacific scheduled check: podv2gao-1855552 remains Pending, no node/startTime. Scheduler says compatible GPUs occupied (2insufficientGPU); other nodes tainted/unschedulable/affinity-ineligible. No reliable position/start estimate. Six-hour activeDeadlineSeconds21600, but no actual lease start/end can be reported yet. GuardianPID1855730 is detached and waiting, stage$HOME/.pa3-setup-control.gty67K/v035-A-20261108; it will deploy/check/start automatically whenReady. No approved V035 fit or CUDA proof has started. Do not allocate duplicates, relax scheduler restrictions or change the frozen recipe. Monitor observation persisted outputs/controlled_experiments_v035/monitor/check_20261108T232835Z.json; orchestration_v035.json current. Next checks about10minutes, wait between checks to conserve usage. If SSHexpires ask onlyTerminal/Duo; remotequeued job/guardian unaffected.

V035 capacity source/protocol/payload freeze and CPU73-check proof are complete as described below. Actual CUDA/lease timing still required before200epochs. Prepared independent A audit, no F/final/submission. All completed V033/V034 controller variants rejected. Official0.17427 preserved; <=0.15 not achieved. User modification baseline_v001.ipynb remains unstaged/untouched. Currentsourcefreezecommit618e9b7; no newmodeloutcome. Follow actual live state, not stale launch estimates.

---

# Live checkpoint: V035 GPU requested; V034 rejected

November8 3:18PM Pacific: requested one ordinary DataHub pod v2gao-1855552 (last observed Pending), guardianPID1855730, login stage $HOME/.pa3-setup-control.gty67K/v035-A-20261108. No duplicate pods existed immediately before launch. Actual start/lease end/GPU proof/first training epoch not yet retrieved at this entry. Ordinary six-hour lease only; no bypass. Check about10minutes, not continually. Remote guardian deploys once, runs actual-CUDA core-pruning/model/lease proofs before training, archives/member-verifies after exit and releases idle GPU; no automatic allocation or submission. Source/payload metadata research/orchestration_v035.json.

V035: one cold larger four-layer Laplace LSTM, widths320/256/192/128 (5,108,162params) vsV029256/192/128 (2,593,602). SAME47inputs/original61114fit6791val/seed20261102/dropout.15/heads/inspiratoryLaplace+.1curve/scale-floor.001/init1/full200replayrates. V025 private queue variant capacity_laplace_curve; unfamiliar capacity has insufficient comparable history, keep representative, never prune on training/NLL/official scores. SyntheticCPU73checks passed including actual full-model optimizer/RNG resume and breath reset; mandatory actual CUDA proof still unknown. A synthetic stress tensor initially omitted the internal R/C code (model47numeric+1code); proof fixed to48entries before any fit, originalproof/source preserved. Capacity model unchanged.

Frozen git618e9b7 before course training: controlled_experiments_v035.ipynb code14866285af6f6abed533c1d06253428b1e6904bb0c7556b066bb37046e55ce31; protocol512cc9838a3403ddcd5e5214a54262d10059aba0568dfa17f8be2f352d532d39; capacity preflight420928745a182d0f4f991eff0cc3088bcc7bacfe4fbd3809e868edd5ff181260. Actual measured200*239*stepseconds*1.20 must<=19800s andpeak<10GiB before any approved fit, preserving30minute lease reserve. If gate fails, archive/release and review; do not truncate epochs or silently change model. Payload40,988,625B/76members SHA10eaf16f9141572a4f252a4ba830559851f7a7d0f6cc69c692ca528ab63f4c14. Setup helpers under outputs/controlled_experiments_v035/setup_helpers. Prepared independent A audit review/audit_A_v035.py SHA b2059875695c4e439db740f680ca71befd0beeedb0d222f8d00b5466dc5009fb; not executed. Two fixed ensembles: new.25 replacement, or olddeep_curve.125+new.125, remaining weights unchanged. Gain>=.003 AND negative whole-breath interval; only lowest eligible advances cold Fseed20261204 (still unused). No F/final/submission.

V034 completed CPU37.456s; independent626checks passed. Physics-match one-bin A.182667626 gain.000254469<.003; full-grid A.222252449 worsened. Both rejected, selectednull. Close bounded controller-bank branch, no cap/weight/threshold search. V033r1 also rejected A.182879114 gain.00004298, audit161. V03235.07%/39.93% conditional compatibility did not establish prediction accuracy. Reports research/RESULTS_V032/33/34.md and executed research notebooks preserved. Best official0.17427, <=0.15 unmet.

Preserve unrelated user change baseline_v001.ipynb; do not stage/revert/overwrite. Approved Gym data only, modeling in notebooks. Workers credit-exhausted, root continues. SSH renewed8:28AM and worked3:18PM; may need Terminal/Duo~4:28PM, only ask on actual failure. Mac sleep does not stop detached course training/archival; retrieval may need login renewal.

---

# Live checkpoint: V033 rejected; V034 CPU screen running

November8 about3:10PM Pacific. V033 alignment-only recovery completed and independent161-check audit passed. A MAE0.182879114 vs accepted0.182922095; gain0.0000429802,95%delta[-0.000166941,+0.000076746]. Ineligible; no F/final/submission. Saved bank21,136 Afit controllers. Original alignment guard failure and sources preserved, V033r1 restored CSV row order before any candidate outcome and reused hash-pinned bank. See research/RESULTS_V033.md, controller_bank_review_v033r1.json, executed controller_bank_results_v033r1.ipynb. Do not tune V033 thresholds after rejection.

V034 now running locally CPU (shell43448): two prospectively frozen physics-matched-controller cap variants. Select training coefficient vectors using known inputs plus BASELINE PREDICTIONS (never query labels), same controller projection/consensus/support; compare one-bin cap versus full training-grid projection. Both predictions lock before labels. Git922e40c froze before execution;28 synthetic checks passed. Componentc51a51a7533085aa1f7923f7c53a5e1eabad352ad9e497cba153f297ff82c6cb, protocol9798ac9cb3c509a6918e5952d855c9348e15f523e6e258c7e74ead59e216637e. Own outputs/controller_selection_screen_v034; logs/executor/audit in its _review directory. After summary run prepared audit_v034.py (recorded research/controller_selection_audit_preparation_v034.json), preserve any genuine audit errors. Only lowest eligible under unchanged gain>=0.003+negativeinterval could advance cold F; if none pass, stop bounded controller-bank branch without cap/weight searches. Fseed20261204 still unused.

Fresh remote pod inventory Nov8~3:03PM: empty, SSH works. No GPU allocated/queued. Official0.17427 preserved; <=0.15 unmet. V032 conditional compatibility35.07%/39.93% is not predictionMAE/recoverycoverage. V031 archived/rejected/GPU released. Workers credit-exhausted; root continues. Preserve unrelated baseline_v001.ipynb user modification. Modeling in notebooks, approved Gym data only.

---

# Live checkpoint: V033 CPU screen running

November8 about3:00PM Pacific. V032 diagnostic results saved and audited; V033 input-only controller bank correction frozen in git15ff591 BEFORE any candidate A prediction. Component codebdd6d2ab01994bae8b52c9bc18d5ac7646b275153aba292f838e456b3552e7bd; protocolcdf08366de6eb9712571cf059aeb099bdb56e5ef2498d7bde1e2091958e68a1c.20 synthetic checks passed. One candidate only: top5 input traces within exact R/C/phase, training-bank-only scales/distance confidence, four parallel physics passes, consensus and at-most-one-level correction. No query pressure accepted by predictor API. Original A split; unchanged0.003 gain and whole-breath interval gate. No validation outcome exists at this entry.

Local CPU-only executor outputs/controller_bank_screen_v033_review/execute_notebook.py is running (unified shell session42946). Scientific code remains in notebooks; log execution.log in same directory. No GPU/pod requested. Wait for actual summary then run prepared audit_v033.py (source hash recorded research/controller_bank_audit_preparation_v033.json), fix audit-only issues preserving originals if needed, never change model/protocol based on outcomes. Run research/controller_bank_results_v033.ipynb after audit, record results. Fseed20261204 remains unused; cold F conditional on eligibility. Best official0.17427 unchanged, <=0.15 unmet.

V031 completed/rejected/archive verified/GPU released. V032 training-only compatibility35.07%/39.93% is NOT pressure MAE or recovery coverage. Workers exhausted credits; root continues. Preserve unrelated baseline_v001.ipynb user modification.

---

# Current checkpoint: V032 diagnostic passed; input-only test next

November8, about2:50PM Pacific. V031 completed and was rejected (best fixed A ensemble0.180269962, gain0.002652133 below0.003; audit1039 passed). Its verified archive is local and the GPU was released. No active GPU jobs are known; no new resources have been requested.

V028 strict raw machine-precision pressure lattice check stopped before controller fitting and was audited20. A separately frozen V032 decimal-export observation model passed on both disjoint training-only samples: coherent conditional compatibility202/576 (35.07%) and230/576 (39.93%), versus18/21 exact and0 shuffled. Runtime20.68 CPU seconds; independent audit2626 passed. These are NOT pressure MAEs, recovery rates or input-only predictions. See research/RESULTS_V032.md, controller_quantization_review_v032.json and frozen notebooks/protocol. No original-A controller prediction, F split/fit, final fit or submission exists yet.

Next implement and prospectively freeze a bounded input-only controller-bank correction to the accepted A model. Use original Afit labels only to learn controllers and all statistics. Query API receives known inputs and baseline predictions only. Test one fixed recipe, unchanged gain>=0.003 plus negative whole-breath interval gate; cold F only if eligible. This next V033 proposal is not implemented/frozen/evaluated at this checkpoint. Fseed20261204 remains unused. Best official0.17427 preserved, <=0.15 unmet. Existing workers exhausted workspace credits; root can continue directly; do not retry failed workers without changed conditions.

Preserve unrelated user change in baseline_v001.ipynb; do not stage/revert/overwrite it. Modeling stays in notebooks, approved Gym data only. SSH last renewed8:28AM may need Terminal/Duo after~4:28PM, only if actual access fails. Parent SETUP_LOG and visible history remain preserved.

---

# Current checkpoint: V031 complete and rejected; CPU quantization check pending

November8 afternoon actualstate. V031completedall200epochs11:31:48AM Pacific, individualA.204487920(best188)worseV029.200130185; twofrozenensembles.181782103/.180269962,bestgain.002652133<.003,selectednull. Independentaudit1039PASSED. NoF/final/submission. Archive155files163247295B SHA6977682b2724231b9b0a2880154383506297fdd96a3dace800643731e42501b2 verifiedlocally,safelymirrored,73new/identicalrunfilespublished,sourcespreserved,GPUreleased. NoactiveorqueuedGPUjobsknown; nonewresourcesrequested. See research/RESULTS_V031.md andscreen_review_v031.json.

Bestofficial.17427preserved,target<=.15UNMET. V029,V030,V031allrejected underunchanged .003gain+negativebootstrap gate; do notretroactivelypromote/searchweights. V028quantizationhypothesis isseparateCPUtraining-onlydiagnostic, currentlyDRAFTtextonly. Parallelworkersfailedwithworkspaceoutofcredits beforecreatingimplementationfiles; no source/protocol/approved-dataoutcomeexistsforV028. Rootcancontinue directly; donotretrycredit-failedworkers withoutchangedconditions. No originalKaggledata/solutioncode downloaded.

Nextimplementboundedquantization-observation-orderCPUdiagnostic inNEWnotebooks. OnefrozenconstantrefdecayPI lag0 OLSfirst70%eligiblecontrols, heldcoefficientsfixed. Jointboundedlatentmeasurementerrors |delta|<=halfverifiedrawtraininglattice; nativecontrolresidualbudget1e-4unchanged; cannotjustwidentoleranceindependentlybyrow. Comparezeroerror/coherentLP/destructiveheldpressurepermutation; input-onlyidentifiability remainsrequiredforanylaterpredictor. Planandpreflightmustbefrozen beforeanyapproved-dataoutcome. research/QUANTIZATION_HYPOTHESIS_v028_DRAFT.md preservesmathematicalnotes/risks. NoFsplitexists,seed20261204unused.

Visiblehistoryexportlast17:09UTCnotyetfinal. PreserveparentSETUP_LOG, alloldfiles, reportsandnewchanges. baseline_v001.ipynb hasUNRELATEDpreexistinguserchange(1line); doNOToverwrite/stage/revertit. LatestSSHlastworked11:40AM; renewal8:28AMmayexpire~4:28PM. AskonlynecessaryTerminal/Duo. Modelingandtrainingstayipynb; opshelperpyallowed.

---

# Live V031: protected span3 frontend on the Laplace model

November8 9:08AM Pacific. Podv2gao-1732899(n05)Running, started9:06:14AM, ordinary6hleaseends3:06:14PM PST. Standard1GPU/4CPUlimit/16Gi, no duplicates/bypasses. ActualGTX1080Ti CUDAcorepruner32+model152checkspassed, includinginheritedNLLproof/exactnewmodelresume/zeroµ+b/protectedoutputs/control/efficiency. Step.15865svs.16013V029baseline(similarcost), peakallocated1316089856B. Rawproofsdownloadedhashverifiedinsetup_helpers. Epoch1/200completed,43.03s/epoch,earlynativeval1.10486notfinalscore. Expectedresults/review11:35–11:50AMifpaceholds. Check~10min, waitbetweentoconserveusage.

OnecoldAfit conv3_laplace_curve onoriginal61114fit6791val47features,seed20261102,full200originalrates. Onlyprotectedzero-initspan3frontendchangesvsV029; bothheads/objective/bfloor.001/init1/scalingunchanged. V025privatequeuenewvariantunknown=>keepfullrepresentative,nopruneontraining/NLL/leaderboard. NativeinspiratorymeanMAEcheckpointselection withlegacy1e-6min_delta. Twofrozenfixedmixtures(.25replacementor.125oldcurve+.125new),acceptedreferenceA.1829220946, gain>=.003ANDupper95breathdelta<0(1000drawsseed20263101), onlylowesteligiblecanadvancecoldFseed20261204. NoFsplit/outcomeexists.

Frozenbeforefitgitb82b0bb: drivercontrolled_experiments_v031.ipynb code77815759c838b9e4b0c9b2f6d2c24de025b706e76aa7add8f60c97e42a660ac0; protocol74fd95620b135dbd6256f7f3a120c9d6c651358eae89de67319c1b059e6a6b27; componentcfef19352dca73ae2ba8eea52908519f04b1cf7c7c2220d5ab1529451d10ab32; preflight6779006bdf23d411c2c85035447f2a27ffc8bf2c961ca2c9dc1d289209c3898f. CPU147checkspassedbeforeGPU. Newmodel/trainingcodeinnotebooks; allfrozenoldfilesunchanged.

DetachedguardianPID1733160, stage$HOME/.pa3-setup-control.gty67K/v031-A-20261108. Payload69831309B/77members SHAc42af09b9657e97e4c6c5dca0d3e200d1ab28b0a36a9e6991034947f1b0749a5. ServertrainingandverifiedarchivalindependentofMac. Perfitlogs/checkpoints/outcome/pruningunderoutputs/controlled_experiments_v031/conv3_laplace_curve; setupv031-screen-execution.log/v031-exit-code.txt. GuardianverifyeacharchivememberbeforeGPUrelease; neverallocatesreplacement/submits. Rootmonitorcommandmaybecachedfunctionsstorev031_check_command. IndependentAauditpreparedcompiledNOTexecuted(review/audit_A_v031.py SHA7e12e1a31db03dd9e8119537852baa0a4e951780bc64a6a6912bc7dbe8c84de7). Uponcompletionretrievearchive/info/verification/guardian/podsintoNEWcompleted_archive,verify/safemirror/publishneworidenticalrunfileswhilepreservingrootsources,thenrunindepauditbeforenextgate. DonotrestartfromSSHfailure; inspectactualsavedstate/lease.

V029andV030completed/audited/rejected,bestAmixture.180189gain.002733<.003(noF/final/submission). IndividualNLLcontrol.200130, goalbestofficial.17427preserved,target<=.15UNMET. Fullresultsplotsinresults_review_v029.ipynb/researchRESULTS_V029,RESULTS_V030. CurrentSSHrenewed8:28AMworks; askonlyneededTerminal/Duo. No newofficialsubmission.

---

# Current checkpoint: V029/V030 audited and rejected; V031 frozen before launch

November8 morning. V029completed200epochs successfully12:14:52AM;126file/131805816byte archive SHAe001f0011717d8a8f3c30b6930c7f6c3472a29e947ad00ee45a9e52c1ba3d38f retrieved/verified/safelymirrored,58neworidenticalrunfilespublishedwithoutoverwritingsourcenotebooks. Independent1008checkspassed. IndividualA.200130185(best196)vscontrol.203829545; besttwofrozenmixture.180189119,gain.002732976<.003,selectednull. V030separatefixedcachemixture.180311918,gain.002610177<.003,audit112passed,selectednull. No F/final/submission for either; no alternativeweights/thresholds. Reportsresearch/RESULTS_V029.md,RESULTS_V030.md,executedresults_review_v029.ipynb. Officialbest.17427preserved; target<=.15unmet.

NextV031 singlearchitecturechange nowfrozenbeforeanynewAfit: protectedzero-initspan3temporaladapter onimprovedV029Laplacebody. Same47inputs/seed20261102/original61114fit6791val/full200rates/loss/bfloor.001/init1/curve.1. Exactinitialµ+b/RNG/bodygrad andfrozenadapterAdam/dropoutcontrol, checkpointresume/loaderguards/privateV025queue verifiedin147CPUchecks. GPUproofsmandatorybeforetraining. Sourcesresearch/laplace_convolution_components_v031.ipynb cfef19352dca73ae2ba8eea52908519f04b1cf7c7c2220d5ab1529451d10ab32,preflight6779006bdf23d411c2c85035447f2a27ffc8bf2c961ca2c9dc1d289209c3898f. Drivercontrolled_experiments_v031.ipynb code77815759c838b9e4b0c9b2f6d2c24de025b706e76aa7add8f60c97e42a660ac0; protocol74fd95620b135dbd6256f7f3a120c9d6c651358eae89de67319c1b059e6a6b27. TwofixedmixturessameV029design,new.25oroldcurve.125+new.125, unchangedgain.003negativeCIgate(1000drawsseed20263101). ColdFseed20261204stillunused,nosplit/outcome.

V031deploymentpayloadpreparedunderoutputs/controlled_experiments_v031/setup_helpers,notyetallocated/deployedatthisentry. Standard1GPU4CPU16Gi6honly; actualemptyinventorycheckbeforelaunch, no duplicates. UsecoreV02532andnewcomponentactualCUDAproofsfirst; unfamiliarnewarchitecture/objectivecombo getsfullrepresentative, donotpruneonNLL/training/leaderboard. PreparedindependentAauditbeingboundtofinalfreeze, notexecuted. SSHrenewed8:28AMandworks; no furtherloginneedednow. Allfrozenpriorfilespreserved; newmodel/trainingcodeonlynotebooks.

---

# Current access checkpoint: retrieve V029 overnight results after Duo renewal

November8 8:27AM Pacific actualSSHcheck failed because8-hourDuoauthenticationexpired. UserTerminalrenewalquestionpending. Currentremotecompletion/score/podinventorystillUNKNOWN; do not repeat stale12:15–12:30AMestimate or claim completion. Lastverified9:54PM November7 was2/200epochsandCUDA32+69checks passed. Oldleaseexpectedend3:51:38AM November8. Detachedtraining+guardian unchanged; persistentcoursefiles/archivestage shouldbeinspectedbefore anyrestart/newpod. Nonewresourcesrequestedthisturn.

Afteruserconnected: SSH inspect actual pod andstage$HOME/.pa3-setup-control.gty67K/v029-A-20261107; retrieveguardian.log/archive.json/archive-verification.json/pipeline-archive.tar.gz/completed-pod.json intoNEWoutputs/controlled_experiments_v029/completed_archive. Verifyarchive/memberhashes/safeextractionandpublishneworidenticalartifacts preservingrootsourcenotebooks; thenrunpreparedindependentauditoutputs/controlled_experiments_v029/review/audit_A_v029.py SHA7cf526f91d45bed4a49838f95e859cfd3c0d80f514a7dbeeaf0bdd2d364e3d84. CurrentauditNOTexecutedandlocalcompletedresultsabsent. Do not inferfailed/stoppedtrainingfromSSHfailure.

Rootsource/protocolpinsandacceptedofficialCSVhashrechecked; official.17427preserved, goal<=.15unmet. V029twofrozenmixtures/unchanged.003gain+negativeCIgate, noF/final/submissionyet. Fullsource/pod/proofmetadataremaininresearch/orchestration_v029.json andnotesbelow. Laststatussource scientificmodelsunchanged.

---

# Live V029: original-A positive-scale objective training

Updated November7 9:54PM Pacific. Coursepodv2gao-989316(n06) Running; started9:51:38PM, ordinary6hleaseendsNovember8 3:51:38AM PST. OneGPU,4CPUlimit,16GiRAM, noresourcebypass/duplicates. ActualGTX1080Ti CUDApruner32checks andmodel69checksPASSED beforeapprovedfit. RuntimeTorch2.2.1+cu121/CUDA12.1/numpy1.26.4, strictdeterministic/thread4. Mean-stepoverhead0.85%, peakallocated1.300GB. Rawcourseproofs downloaded/verified inoutputs/controlled_experiments_v029/setup_helpers/.

Onecold200-epoch A fit laplace_curve,47features,original61114fit/6791val,seed20261102,successfulmeanbody unchanged; b=softplus(input-drivenhead)+.001(targetscaled),initb1/noextraRNG. InspirationNLL+.1oldadjacentmeanpressurepenalty; pressurelabelsneverinputs. NativeinsppointMAE selectscheckpoint usingunchanged1e-6legacyimprovementtolerance, neverNLL. V025privatequeuetruthfullyrecordsactualobjective; no comparable NLLhistory, so keepfirstfullrepresentative (actualepoch2decisionreason no_comparable_data_model_optimizer_schedule_or_runtime). Latest2/200,42.24s/epoch,earlyMAE.94985 isnotcompletedresult. Expectedfinish/review12:15–12:30AM Pacificifpaceholds. Check~10minandwait, donottuneonintermediateoutcomes.

Frozensource controlled_experiments_v029.ipynb codeSHAcaebc7edc5cce7561bcd67b91145abc000a7249e82c067fcb100c068bf14fac0; protocolresearch/protocol_v029.json SHA56f8428036f9b2803125d5dd17ee5c62a654ac88f88bcdfe2483b09b92a79d44. Componentb6bd59bced1fad03882f27d9faec51deec93b3ab10afa9f06b8cef36c4d5260d; preflight4143266b792b6d6eb19fa1437d755a2f5685abdfe4ccfaaeeab1a7bd7743aca3. Git08d0400 frozeallbeforefits. Twofixedmixturesonly: replaceolddeep_curve.25withLaplace.25, orretainoldcurve.125+Laplace.125; othercurrentweightsunchanged. ReferenceA.1829220946, gain>=.003ANDupper95wholebreathdelta<0(1000drawsseed20262901), lowesteligibleonlycoldFseed20261204. NoFsplit/fit/outcomeexists. No weight/schedule/scaletuningafteroutcomes.

Stage$HOME/.pa3-setup-control.gty67K/v029-A-20261107, guardianPID989554. Payload40929025B/64members SHAbb791b958384b4e535a344747f566dbfe306e96b433fd4bc28678d7a75feb512. Detachedtraining+guardianindependentofMac; verifiedmemberarchivebeforeidleGPUrelease, noautomaticresourceallocation/submission. Perfit epochs/checkpoints/pruning/outcome underoutputs/controlled_experiments_v029/laplace_curve; setupv029-screen-execution.log/v029-exit-code.txt. Helper/pins detailsresearch/orchestration_v029.json. PreparedindependentAaudit(review/audit_A_v029.py) SHA7cf526f91d45bed4a49838f95e859cfd3c0d80f514a7dbeeaf0bdd2d364e3d84 compiledNOTexecuted. Oncompletionretrievearchive/info/verification/log/pods intoNEWcompleted_archive; verifyallmembers/safeextract/publishneworidentical whilepreservingrootsources, thenindependentlyauditnativeNLLmetadata/fullbudgets/trainonlystats/µ,b/rowalignment/diagnostics/policies/bootstrap beforepromotion.

Bestofficial0.17427andolderacceptedCSVs/receipts remainpreserved; target<=.15UNMET. V024/V026rejected(noF/final/submission), V027training-onlyneighborcheckcompleteaudited198+4, notLSTMimprovement. V028quantizationhypothesisDRAFT unimplemented. Standingapprovalcontinues. CurrentSSHrenewedworks; askonlynecessaryTerminal/Duo. FrozenV005/V008/V025sourcesunchanged. Allgenuineprelaunchproof/opsbugs correctedbeforefitsandoriginalspreserved.

---

# Latest continuation: V027 diagnostic audited; waiting for DataHub login

Updated November7 about9:37PM Pacific. Current official best remains0.17427, target<=.15unmet. V024 and separate V026 fixed-mixture screens rejected under unchanged .003 practical-gain gate; no F/final/submission. V026 A0.18108043880526803, independently audited86checks. Stop this saved-weight branch. Previous GPU was released; no new GPU requested, no remote training launched in this continuation.

V027 single fixed nearest-neighbor diagnostic is now COMPLETE, not a draft:576 original-Afit queries (64/R/C),60538 disjoint pool, originalAval skipped before numeric conversion, mean inner-queryMAE0.71975778 versus weakR/C-positionbaseline6.06113264. Seven synthetic leakage checks before execution, independent198checks plus4freeze checks passed. Runtime24.96CPU seconds. No gradient training/checkpoint inference/GPU/F/submission. Source/protocol froze git4775caf; research/RESULTS_V027.md, executedneighbors_feasibility_v027.ipynb, neighbors_review_v027.json, outputs/neighbors_feasibility_v027. It does NOT demonstrate gain over LSTM or justify direct promotion. Top5 context coarse; disagreement correlates with its own error(.7175), rawdistance weaker(.1962), R50~54.5%totalerror. No k/metric/query tuning after outcomes.

V025 stopping workflow CPU32checks and independent review done; nativearm/diagnosticcount cache provenance fixed before production. PolicySHA0acdfa933d54fbae1e7728e2f8982bdae3f4227c6bd5187979bcd38b67e5fc88; workflowcode91af4747704d53887742dd7b7b7aac4d961313390642971d2c474df51d3cb694. Actual CUDA hook proof still REQUIRED before new GPU A batch; no production prunes yet. AGENTS and portablehandoffcopy route new A fits through V025. Frozen V005/V008 untouched.

Access: actualSSH9:23PM failed with8-hourDuo requirement; user renewal question already pending. Do not repeatedly retry/request. No current pod inventory verified after that expiry; last known previous pod released and no new allocation. Further GPU training awaits login. Password/Duo onlyTerminal. Standing approval still covers controlled future batches, cold confirmation, conditional final and validated submission.

Next: after reconnect, inspect actual pods/lease before allocation. Develop a genuinely different frozen test rather than repeat seeds/capacity/weights by habit. Positive-scale Laplace-objective arm remains proposed, not implemented; representative unfamiliar objective must finish because V025 lacks matching history. Cross-fitted neighbor residual context is also unimplemented and requires evidence of incremental value. research/QUANTIZATION_HYPOTHESIS_v028_DRAFT.md records another possible bounded CPU test of observation order (continuous controller before CSV rounding), coherent latent quantization constraints and input-only identifiability requirements; no V028 protocol/source/fit/outcome exists. Old exact-controller gates remain failed, never relaxed. Cold Fseed20261204 remainsunused; allrequiredmemberscold, allfit-onlystats/gridreconstructed, no Amodelreuse forF. Preserve official/all histories and append SETUP_LOG.

---

# Current checkpoint: V026 rejected; V025 stopping workflow reviewed

Updated November7 evening, about9:30PM Pacific. V024 completed/audited126checks and its GPU was released. V026 cheap single fixed-mixture screen completed, independent86checks: A meanMAE0.18108043880526803 versus0.18292209456473527, gain0.0018416557594672367 below unchanged .003 gate, despite negative bootstrap interval. Selected=null. NO F/final/submission for either. Official best0.17427 remains preserved; target<=.15unmet. Reportsresearch/RESULTS_V024.md and RESULTS_V026.md. V026 notebook/protocol/source frozen in git09fb2b6 before calculation, no weight search. No new GPU requested.

V025 conservative validation-only early-pruning workflow independently reviewed and CPU32checks passed. Review caught and fixed cache identity missing native arm/diagnostic breath count before any production use; originals preserved. Current training_workflow_v025.ipynb codeSHA91af4747704d53887742dd7b7b7aac4d961313390642971d2c474df51d3cb694; policySHA unchanged0acdfa933d54fbae1e7728e2f8982bdae3f4227c6bd5187979bcd38b67e5fc88. Same-stage arrays/steps/backbone/optimizer/rates/runtime/known-source guard, calibrated margin7.0845%, patience20, LRgrace13; unfamiliar setups finish representative. No production pruning yet. Actual CUDA hook preflight REQUIRED before next new A GPU batch. Project AGENTS routes new A fits through V025queue; frozen legacy V005/V008 unchanged.

Next: stop saved-weight tinkering; prepare one bounded training-only nearest-neighbor feasibility diagnostic (V027, DRAFT only at this entry). It will compare fixed5neighbor median pressure curves against a weak pool-only R/C-position median baseline on576 original-A-fit queries disjoint from the pool; no originalAval data/labels used. This cannot establish benefit over LSTM or by itself justify a GPU model. Source/distance/scalers/query/pool/gates must be reviewed/frozen before outcomes. Prospective later cross-fitted context or Laplace-objective hypotheses remain unimplemented. No F data/fit/outcome yet; cold F seed20261204 reserved.

Actual SSH check9:23PM Pacific required renewed password/Duo; user renewal question is pending. Do not repeat login request or falsely claim current live inventory verified. Previous GPU was released; no new resources allocated. Work locally while awaiting connection. Preserve all source/data/model hashes, parent SETUP_LOG and visible history.

---

# Current checkpoint: V024 complete; V025 pruning implemented and CPU-tested

Updated November7 evening. V024 finished6:23PM Pacific; guardian verified83files/188843666bytes, archiveSHA36f77e054fe98911d6c278cb4ec6a4478b593dd70f92b7c1cac5bfef4d4d2d2a, releasedGPU823946. Local archive/mirror verified; root sources preserved. Independent126checks passed. Best fixed A candidate0.181062361 versus0.182922095, gain0.001859734 below frozen0.003 gate; selected=null. NO F/final/submission forV024. Reportsresearch/RESULTS_V024.md andresults_review_v024.ipynb. No GPU jobs remain. Bestofficial0.17427 preserved; target<=.15unmet.

User requested conservative compute-saving pruning AFTER this run. V025 is now implemented in notebooks: research/pruning_components_v025.ipynb, training_workflow_v025.ipynb, executedpruning_calibration_v025.ipynb andpruning_workflow_preflight_v025.ipynb. ProjectAGENTS nowroutes newAexperiments through this workflow. Policyresearch/pruning_policy_v025.json SHA0acdfa933d54fbae1e7728e2f8982bdae3f4227c6bd5187979bcd38b67e5fc88. Only native fixed-grouped-A validation inspiratoryMAE; compare atsame data/steps/backbone/optimizer/LR/runtime, requireknownvariant andcompletedreferencehistory. Compare afterhalf100/200; margin7.0845% worse than evenweakest matchedprefix-best curve for20full evaluationintervals, bestvalidationimprovement<=1.0095%,13evaluationsgrace aftermajorLRhalvings. ValuesderivedfromthreeauditedunaugmentedV013/V024histories; augmentedmixup excluded. Unknownsetupsfinishrepresentative. No training-MAE/leaderboard cutoff.

CPUpreflight32checksPASSED: source/policyguards, nofuturecurvepeek, scaleinvariance, checkpoint savedbeforestatusPRUNED, exactclonedparameter/optimizer/RNGresume, preservedoriginalprunedfiles, nextqueuedexperimentexecuted, prunedmemberscannotbecompletedcandidates. No productionprunesyet. ActualCUDAhookproofstillpending before nextGPUbatch. Fullmethodologyresearch/PRUNING_WORKFLOW_V025.md; calibrationreview/pruning_workflow_preflight_v025.json. Initial overconservative draftwasrejectedbeforedeployment; oldmeasurementsretained. V025 model/training logic stays in notebooks; frozenV005/V008 unchanged.

Next: finish review/log/commit of V024/V025 artifacts, then continue controlled improvement. Prefer a separate prospectively frozen cheap fixed-mixture screen retaining the successfulolddeepcurve plusbothhybrids before spending moreGPU. This proposednextscreen is NOT implemented/frozen/evaluated yet; do not claim a new score. If future A training is needed, integrate V025queue andrun actual CUDA hook proof. NewF seed20261204 remainsunused; cold-fit ALL needed F members andrefitfit-only statistics/grid if anyfuturecandidate passesitsfrozengate. No Amodelreuse forFvalidation. Reuseacceptedall-data models onlyconditionalfinalafterfullchecks.

Access is currently restored afteruser Terminalrenewal; no furtherlogin stepneedednow. A statusanswerinitiallyusedastale5:25checkpointat7:25; immediatelycorrectedthencompletionverified; research/time_estimate_correction_v024.json. No modelingimpact. PreservevisibleAIhistory andappendparentSETUP_LOG.

---

New user requirement: AFTER current V024 run, implement conservative compute-saving pruning for future experiments, using ONLY fixed-grouped-A native validation inspiratoryMAE. Require both substantial same-stage reference deficit and stalled improvement; empirically calibrate margin/patience/LR grace from completed logs. Preserve exact resumable checkpoint and label PRUNED, then advance next planned run. Do not alter hash-frozenV005/V008; implement notebook wrapper and integrate actual next batch. Detailsresearch/pruning_requirements_v025.json. Not implemented/calibrated yet; complete afterV024results/audit. Currentactual5:01PM Pacific: conv7 89/200, bestvalidationimproving.3494(59)→.2791(89); nowbetterthansame-stageconv3.28449, afterbeingbehindat79. Firstspan7representative/beforehalfway; CONTINUEcurrentrun, noactiveprune. Evidenceresearch/pruning_active_decision_v025.json.

Latest actual V024 progress4:05PM Pacific: conv3_curve COMPLETE200epochs, reportedindividualA0.203241290 (control0.203829545), best194,runtime8639.9s. Smallindividualgain; notindependentlyaudited/promotionyet. Conv7_curve11/200,43.33s/epoch; pod823946Running. Fullscreenestimate6:20–6:40PM; lease7:31:28PM. No completeensembleoutcomes/decision; frozenrecipes/gatesunchanged. All14periodicobservations preserved research/progress_v024_first_fit.json. Wait~10minbetweenchecks; retainofficial.17427.

Latest actual V024 progress at1:42PM Pacific: pod823946 Running; conv3_curve13/200 at42.73s/epoch; conv7 pending sequentially. Estimate first~4PM, fullscreen~6:20–6:40PM; lease7:31:28PM. No completed new A result yet. Evidence research/progress_v024_initial.json. Frozen sources/gates unchanged.

# Current state: V024 hybrid screen is running

Updated November 7, about 1:36 PM Pacific. This block supersedes the historical notes below.

- Course pod **v2gao-823946**, node its-dsmlp-n05.ucsd.edu. Started **1:31:28 PM Pacific**; ordinary six-hour lease ends about **7:31:28 PM**. One GPU, CPU limit4, RAM limit16Gi; no bypass or duplicate pod.
- Actual GTX1080Ti CUDA preflight passed **51 checks** before training, including exact interrupted parameter/optimizer/RNG recovery and zero-adapter training control. Full-batch measured overhead is about0.19% for span3 and0.55% for span7. Raw proofSHA `1b2950290a074663935cfd83de48e3213ab802a22d0f464e32548621ac2a8392`; local `outputs/controlled_experiments_v024/setup_helpers/course-proofs.json`. Runtime Torch2.2.1+cu121, CUDA12.1, numpy1.26.4.
- Two sequential full200-epoch fits: **conv3_curve**, then **conv7_curve**, original61114fit/6791validation A, seed20261102. No completed A outcomes yet. Same47 inputs, original deep LSTM, curveL1.1 objective, Adam and complete original rates. A zero-initialized SiLU temporal adapter learns local patterns while preserving R/C, phase, time, step and jointcode. No pressure inputs. Modeling remains in notebooks.
- Driver `controlled_experiments_v024.ipynb` codeSHA `bb0fb51555f1c931fcdab683f2d46bb7fb6f34ef1e797bd1af5f97790e8738ee`; plan `research/protocol_v024.json` rawSHA `4b18cf799c974bbfae02bce20dc65bdc42f9668c17d5fd809839090c0e2ccbe5`; adapter component codeSHA `4b5971ac2a5dd70b2c62b6f045f61cceb4be60781bbef951f1562573f1b453da`.
- Payload12015948bytes/39members SHA `e04d0bf3437fcde1cd909769434417b37fa08a142e6355cf1ffefc6f5fc358d4`. Login stage `$HOME/.pa3-setup-control.gty67K/v024-A-20261107`; detached guardianPID824466. Guardian retries and verifies archival before releasing idle GPU; it never submits or allocates replacement pods. Mac sleep/disconnect does not cancel the server job.
- Frozen candidates replace only the old deep_curve .25 ensemble slot: conv3 .25, conv7 .25, or each .125. Current A reference0.182922095; gain>=.003 and whole-breath bootstrap upper95<0 (1000draws, seed20262401). Only lowest eligible proceeds to new **cold F seed20261204**. No F split/fit/outcome yet; all required F members must be cold-fit and label-derived statistics/grid refit on Ffit only. No A models for F validation.
- Independent A audit prepared, compiled, **not executed**: `outputs/controlled_experiments_v024/review/audit_A_v024.py`, SHA `1ad17aa89a1e7aa75e8f6073697f553dc01a18fc746582008e5fa675b8c61b4e`. Reads protocol bootstrap settings, checks adapter span/mask/factory/module/counts plus fit-only statistics, checkpoints, alignment and output math. Preparation `research/audit_preparation_v024.json`.
- About every10minutes, inspect current pod and `outputs/controlled_experiments_v024/{conv3_curve,conv7_curve}/epochs.jsonl`; wait between checks. Full result is screen_summary.json after both fits. Expect roughly4–5hours total based on the earlier body, refine ETA from actual epochs. Monitor command may be cached as functions-store v024_check_command.
- Upon completion, retrieve stage archive.json/archive-verification.json/pipeline-archive.tar.gz/guardian.log/completed-pod.json into a NEW local completed_archive; verify with setup_helpers/verify_archive_v024.py, safe-extract mirror, publish only new/identical artifacts and preserve root source notebooks. Then run the prepared independent audit before any promotion. If interrupted, inspect actual pod and exact.last states; do not restart solely because SSH failed, truncate epochs or waive hashes/runtime checks.

V021 completed/rejected, independent114checks; all three ensembles worse than0.182922095. Its78-file185152869-byte archive locally verified; prior GPU released. V023 discrete PID feasibility also rejected (19/576=3.30% versus matched PI28/576=4.86%; 46independentchecks,13.54CPU seconds); no input-only pressure predictor or pressure-MAE result. See RESULTS_V021.md/results_review_v021.ipynb and research/RESULTS_V023.md. Do not redo these screens.

Best official mean MAE remains **0.17427**, CSV/receipt preserved along with0.18025/0.18550. Target<=.15 remains unmet. Standing approval covers controlled iterations, cold grouped confirmation, conditional all-approved final fitting and validated submission. Only approved Gym data; no original Kaggle data, external solution code or pretrained solutions. Ask only needed Terminal/Duo login steps. SSH was renewed at12:44PM; next renewal may be needed after8hours. Full current metadata: research/orchestration_v024.json.

---

V023 CPU controller-derivative diagnostic COMPLETE, gate FAILED, independent46-checkauditpassed. BestPID19/576=3.30% versusmatchedPI28/576=4.86%; rule>=10%AND>=2percentagepointgain. 13.54CPUseconds,38syntheticchecks beforefreeze. NotpressureMAE/input-onlyrecovery. Sources/protocol/review research/controller_pid_*v023; reportresearch/RESULTS_V023.md. NoGPU/predictor/submission. V021alsocomplete/rejected,audit114,backupverified,GPUreleased. Bestofficial.17427,target<=.15unmet. Nextdistincthypothesis: residualtemporal-convolutionfrontend on47-featuredeepcurveLSTM, testing spans3/7 separately, exactidentityinitandunchangedbackbone/objective/rates; NOTimplemented/frozen/launchedyet.

V021 COMPLETE AND REJECTED after independent114-check audit. Both200-epoch arms finished; individualA onehot0.227689288, mixup0.251416942. Fixed ensembles: onehot0.186604037, mixup0.189961929, both0.185261770, versus current0.182922095. Allworse; selected=null. NO F/final/submission forV021. Results research/RESULTS_V021.md and executedresults_review_v021.ipynb. Verified78-file185152869-bytearchive SHA3465e546605d996a79fea3380c3074debe6f0d91ab737a22c6a1e76b8dac3d04 locallypreservedunderoutputs/controlled_experiments_v021/completed_archive. Guardianreleasedpod517608afterverifiedbackup; noGPUjobsremain. SSHrenewed. Bestofficial.17427andoldCSVsunchanged; target<=.15stillunmet. Next investigate a distinct controller-derivative training-onlyfeasibilityhypothesis; nonewprotocol/fit/outcome yet.

V021 ACCESS RESTORED after user Terminal/Duo2026-11-07T20:44:20Z=12:44PM Pacific. Actualpod517608Running, mixup175/200 at43.21s/epoch; expected~18mintrainingleft, screen~1:03PMplusarchive/audit. Onehotcomplete200reportedindividualA.227689288. No restart/source/recipechanges. Supersedes earlieraccessblockedheads; see research/access_restored_v021.json. Continue~10minchecks, thenretrieveverifiedarchive andruncorrectedAauditSHA c5623f0f3ff2ce544679e43f2380a88182dc46aff1659abb393311e344aa0d66. Official.17427preserved,target<=.15unmet.

V021 ACCESS BLOCKED pending user Terminal password/Duo renewal; verified on three consecutive goal turns, latest2026-11-07T20:42:45Z. Last actual successful podcheck12:15PM Pacific: mixup136/200, onehotcomplete200(reportedA.227689288). Current remotecompletion is UNKNOWN; no local screen/verifiedarchive/audit yet. Do not infertrainingstoppedor restartfromSSHfailure. Detachedjob/guardianunmodified. Userrenewalrequestalreadyoutstanding. Reconnect, retrieveactualstage/archive, verifythenruncorrectedauditSHA c5623f0f3ff2ce544679e43f2380a88182dc46aff1659abb393311e344aa0d66 (sixchecks; oldauditsourcepreserved). Evidence research/access_block_v021.json. Goal<=.15NOTachieved; official.17427preserved. Stopautomaticaccessretriesuntilrenewal; resumeactualstateonceuserconnected.

Latest V021 monitoring: last successful actualcheck2026-11-07T20:15:48Z (12:15PM Pacific), pod517608 Running, mixup136/200; onehotcomplete0.227689288. At12:25PM sharedSSHexpired(Duo once8h), renewalrequested; remotejob/guardianindependent, no restart. Estimatedfinish~1:05PM basedonlastpace, notverifiedcompletion. Preparedindependentauditseedtypo corrected BEFOREcompletedoutcomeaccess; frozenprotocol/source unchanged. Correction+newauditSHA research/audit_pre_execution_fix_v021.json; originalpreserved. Periodicrawobservations research/progress_v021_periodic_20261107.json. Awaitloginthenretrievescreen/archive; target<=.15stillunmet,official.17427preserved.

# Continue this project here

LatestliveV021check10:40AMPacificNov7: onehotcompleted200,reportedindividualA0.227689288,best195,runtime8470.5s; raw-numericalcontrol0.229696833 (smallencodinggain), stillworsethan47-featurecurvecontrol0.203829545. Individualreportnotindependentlyauditedyet. Mixup4/200,43.03s/epoch; expectedfullscreen~1PMPacific. No completeensembleoutcomes/selection yet; keepfrozenrulesunchanged. Actualpod517608Running,lease2:13:42PM. Detailsresearch/progress_v021_first_fit.json.

LatestverifiedV021progress2026-11-07T17:51:36Z=9:51AMPacific: pod517608Running,onehot136/200,42.05s/epoch; mixupnotstartedyet. Estimate~45minleftfirstfit,then~2–2.5hsecond; fullscreen~1–1:15PMPacificbeforelease2:13:42PM. IndependentcompiledAauditnowprepared `outputs/controlled_experiments_v021/review/audit_A_v021.py`, SHA c7600ce7164c84d83b99a67d7a876c4773f19a75584621eb997cba1b40817fe5, metadataresearch/audit_preparation_v021.json. NOT runbeforeactualcompleteoutcomes. It adaptsV019auditforonehotinputwidth/factory andmixuprecipe/all-epochcounts, rebuiltfit-onlystats,best/last budgets,nativepolicy/bootstrap. No scientificsource/plan/job changes.

**V021 LIVE, November7 morning:** ordinarycoursepod **v2gao-517608**, n05, start2026-11-07T16:13:42Z=8:13:42AMPacific; expected6hleaseend2:13:42PMPacific. Stage `$HOME/.pa3-setup-control.gty67K/v021-A-20261107`. ActualGTX1080Ti;21CUDAchecks passed including exactmodel/optimizer/RNGresume, zero-mixup curve-training control, nativeinference andbothrealdeepmodel shapes/gradients. FirstapprovedAarm `raw_onehot_curve` observedepoch3/200,41.98s/epoch,GPU94%; second `phase_RC_mixup_curve` sequential200. Same61114fit/6791valA,seed20261102,200oldrates. Estimated4–5hfromstart; check~10minandwait. No completednewAresultyet.

Authoritative frozen sources: `controlled_experiments_v021.ipynb` codeSHAcf894a607a3bc07ca5b50b0ad4218b0d597ecfd19d9fbe3740d3208a68944499; component `research/encoding_mixup_components_v021.ipynb` codedbe65fb696db7e91bcc26ce498a5a971fe605513f58657b5533febcc77e238e6; plan `research/protocol_v021.json` SHA32916828f16a345bc53a789fd48e11d51f9654e87dd2923c99bb12e7cdb662fb. Payload11721301B/39members SHAf36f7902c7b3199637b9b6e4656488079c85730e523b1b4610ce170232895c63; helpers/pinsunderoutputs/controlled_experiments_v021/setup_helpers. CPU22checks+GPU21passed. Fullruntime/proofrawSHA/podlease `research/orchestration_v021.json`. NooriginalKaggledata/solutioncode downloaded; supplied-file S01/S03 inspirationrecorded. OptionalOrcaworkflow unavailable(commandnotfound), stoppedthatworkflow; noalternateOrca binary attempted; existingauthorizedcommandtoolsused.

RawonehotarmreplacesnumericR,Cwithseparate3+3onehotchannels on6rawinputmodel (internalneuralwidth10), objectivecurveL1.1unchanged. Mixuparmusesoriginal47features/deepcurve objective, alpha.2/prob.5, currenttrainingbatchsameR/C+entirephasemask/non-selfpartners/onecoefficientperbreath; protectsR,C,u_out,step,internalcode; train-onlyscalers/gridfitonoriginalunmixedlabels; validation/diagnosticsunaugmented. Components andactualGPUproofguardallsource/recipe/resumefingerprints. Threefixedslotreplacementensembles comparecurrentAref.182922095; gain>=.003andbootstrapupper<0, onlylowesteligibleadvancestonewcoldFseed20261204(unused). No additionalweights/policysearchafterresults; noA/all-data modelreuseforFvalidation.

Per-modelprogress `outputs/controlled_experiments_v021/{raw_onehot_curve,phase_RC_mixup_curve}/epochs.jsonl`; model.pt/model.last.pt/report/record/A_predictions. Completeafterboth200fits: screen_summary.json plus3candidatearrays. Setup v021-screen-execution.log,v021-course-preflight.log,v021-exit-code.txt. Newguardianretryhelper integrated: retriesstatus/snapshot/copyerrors, preservespartialattempts, verifiesarchiveSHA/everymemberbeforeidleGPUrelease; neverautoallocatesreplacement orsubmits. Uponcompletionretrieve stagearchive.json/archive-verification.json/pipeline-archive.tar.gz/guardian.log/completed-pod.json intoNEWoutputs/controlled_experiments_v021/completed_archive, verifywithsetup_helpers/verify_archive_v021.py,safeextractmirror,publishonlynew/identicalartifacts andpreserveoriginalrootnotebooks. IndependentlyauditAfeatures/trainonlystats/encoding/augmentationidentities/best+last200budgets/rows/nativepolicy/bootstrap/lowesteligiblechoicebeforeF. V021Aaudithelpernotyetprepared; adaptV019auditcarefullyfornewfactory/mixupmetadata. Ifpartial, inspectauthoritativepod/leaseandexact.laststatebeforeanynormalreplacement; nevertruncatebudgets/disablechecks.

Bestacceptedofficial **0.17427** remains preserved(V018receipt/CSV274668c4dc14e9d20a554c738859fca37e448836797d7260ec7b11464dcde3e2). Goal<=.15notachieved. V019completed/rejected/audited98, noF/final/submissionforit; do notrerunV019. V020controllerdiagnosticfailed5.38%vs10%gate, notpressureMAE. RankedpriorityfileandE-access72-overlapcorrectionstillapply. Earlierdraft/preparationstatuses belowarehistorical; V021isnowlive.

Checkpoint recorded 2026-11-07 07:52 AM PST

**Current checkpoint: V019 COMPLETE, rejected; no active or queued pods.** Both200epochA fits finished successfully2026-11-07T12:36:30.310009+00:00(~4:37AMPacific). Independent98-check audit passed: `research/screen_review_v019.json`. NewindividualA MAEs: auxiliary0.206665552(best200),minimal0.229696833(best194), versus prior deepcurve0.203829545. FixedcandidateensembleA: auxiliaryreplacement0.183622392; minimalreplacement0.186816549; two-newmembers0.182637267 versus currentreference0.182922095. The lastgain0.000284828 is below.003 and itsCI crosses0; **none eligible**, selected=null. Do NOT perform F, all-datarefit orsubmissionforV019. NoFsplit/fits/outcomes exist. Bestofficial **0.17427** remains accepted; target<=.15stillactive. Results `results_review_v019.ipynb`, `research/RESULTS_V019.md`; learningcurvePNG outputs/controlled_experiments_v019/review/learning_curves.png.

Backup recovery: workerexit0; original archive180006932B/70files SHAf823e55f72c932c084bf11ff90841d08773d7c72b6d74cb3b85b39ea35a908f2 persisted intact. FirstkubectlcpfailedEOF at4:37AM after176711163bytes; originalidleGPUlaterDeadlineExceeded/exit143at5:48:53AM. OrdinaryCPU-onlypod501472(-g0-c2-m4) recoveredfullarchive; everymemberhash verifiedremote+local; no retraining. Archive `outputs/controlled_experiments_v019/completed_archive/pipeline-archive-recovered.tar.gz`, mirrorandterminalmetadata preserved. Originalpartial/logs remainloginstage `.pa3-setup-control.gty67K/v019-A-20261107`. CPUrecoveryandoldfailedpod bothdeletedafterbackupverified; latestkubectlgetpods none. Fullrecord `research/recovery_v019.json`. Do not restartV019.

Next work: implement/freeze V021 from `research/NEXT_BATCH_V021_DRAFT.md` understandingapproval, prioritizing first-place separateone-hotR/C and third-place restrictedmixup as separatehypotheses. This is a DESIGN DRAFT ONLY: no V021modelcomponent/driver/protocol/GPUpreflight/payload/pod yet. Suggestedalpha.2/probability.5 notfrozen; source/control/mask/resume/nativeinference testsrequired. OriginalA split, train-onlyscalers/grid,200oldrates, no hidden-testfeedbacktuning. Fseed20261204remainsunusedandavailableforafutureeligiblechoice. RejectedV019models remain preserved; don'tpromotetinygainorfitFbydefault.

Before nextdeployment integrate testedbackupretry helper `outputs/operations_v021/copy_verified_archive_v021.py` SHAbecb28972b980532934f7c645028ec6a6d386dc0a48b0717dbe44eacffb7d56c andfutureguardian `outputs/operations_v021/guardian_v021.sh` SHA7ace8139934aad8ce02bb1ffd5929424f2c0a8c3f00e55c4af9a18970c1e8f4f; sixsyntheticcopy-regressionchecks andBashsyntaxpassed (`research/archive_retry_review_v021.json`), NOT deployed. Retrytransientstatus/snapshot/copyerrors; publishonlysize/SHA/all-memberverifiedarchive; preservepartialattempts; neverreleaseunverifiedorauto-allocate. Includehelperinloginstage/payload; helperwritesarchive-verification.json itself, so redirectitsstdouttoaseparatearchive-copy-result.json. Keepallscientificsourcesinnotebooks.

Userrefinedobjective rank1,then2,3ideasfromrootkagglediscussion.md; seeRANKED_METHOD_PRIORITY_v020.md. V020CPUcontrollerdiagnosticcompletednegative(31/576=5.38%,below10gate), notpressureMAE; recordedV015E-accesscorrection(72E-resamplingoverlap,originalAvalexcluded) remainsimportant. Preserveofficial0.17427CSV/weights/receiptandold0.18025/.18550. SSHcurrentlyworks; requestTerminalDuo onlyifactualrenewalneeded.

**November7,~00:08AM Pacific: updated user objective prioritizes ranked winners1,2,3 onward in kagglediscussion.md.** Ranked mapping/status/nexttests `research/RANKED_METHOD_PRIORITY_v020.md`; first-place raw-input branch alreadyrunning in V019, separateone-hotR/C/optimization tests remain future distincthypotheses. No change to frozenV019. NewV020CPU decaying-controller feasibility completed,12declaredfamily/lag/estimatorcases on same576original-Afitbreaths asV015. Correctedbest31/576=5.38%nearexactcontrolconsistency, belowfrozen10%gate; no promotion/input-onlypressurepredictor/MAE/submission.12.52CPU seconds;20independentreviewchecks `research/controller_arx_review_v020.json`. Notebook `research/controller_arx_feasibility_v020.ipynb`, protocolSHA3a78c577b9935c1be8bdf12b7db7d0ea0fba3b4c6f63f11c923a5bbb2fc58838, sourcesha fd0cbfb776b05175f84a706d53ff5e74eb75f43f8d9242882325ca0a48bcbeaa. InitialRANSACphysical-firstselection didnotexactlyfollowdeclaredfit-inlier/medianranking; correctedandre-ranwithoutprotocol/sample/thresholdchange; initialsource/results retainedinoutputs/controller_arx_feasibility_v020/pre_correction_physical_first.

**Data-access reporting correction:** olderV015roadmap incorrectlyclaimedE-validationexcluded. The576original-Afit sample overlaps72E-resamplingbreaths; originalAval fullyexcluded. V015/V020didnotcomputeEpressure-prediction scores. Ewasalreadydescribedasresampling, notanuntouchedtest. OriginalimmutableV015summary/protocol preserved; correctedroadmap/review supersedeaccessclaim. ColdEfitsstill excludedEvalidation asbefore; official0.17427unchanged. FutureFmuststillcoldfitallmembersandrefitlearnedcomponentswithoutFvalidation.

LatestactualGPU00:05AM:4146406Running,deep_auxiliary_difference21/200,43.55s/epoch. Secondminimal_deep_curvependingsequentially; no completednewAoutcome. PreparedcompiledindependentAaudit `outputs/controlled_experiments_v019/review/audit_A_v019.py` (hashresearch/audit_preparation_v019.json), NOT runbeforeactualresults. Continue~10minchecks/wait. No newGPUjobs/resources/confirmationstarted.

**November6,11:52PM Pacific: V019 screening RUNNING**, ordinarycoursepod **v2gao-4146406**, n05, start11:48:52PMPacific, expected6hleaseend5:48:52AMNov7. Stage `$HOME/.pa3-setup-control.gty67K/v019-A-20261107`; detachedguardianverifies/archivebeforeidleGPUrelease, neverallocatesreplacement. Frozenpayload5784665B SHAe7a7b786df9899ce1cf04a5bdf7d7d8086dc2e7b1cc77b6b28aaf87f0d9f276c. ActualGTX1080Ti20syntheticCUDAchecks passed (zero-auxpressurecontrol,exactresume,masking,inference,bothactualdeepinputwidths/gradients), localrawproof `outputs/controlled_experiments_v019/setup_helpers/course-proofs.json` SHAc86a8e1864da1588914b4cd70974305fb08f5b8c7dd7be01c9fbd3899d1c18a6. ApprovedAfirstarm deep_auxiliary_difference started; GPU94%; secondminimal_deep_curvesequential. Both200epochs,original61114fit/6791valA, seed20261102, fixedrates. No completednewAoutcomeobserved. Estimated4–5hplusqueue (podalreadyRunning); check~10min/wait. Source/protocol/payloadfrozenbeforeofficial0.17427; unchangedafterofficialfeedback.

Bestacceptedofficial **0.17427**, V018receipt `research/submission_receipt_v018_final.json`; target<=.15active. V018fullycompleted/submitted, old0.18025/.18550preserved, no V018job remains. Do notrerunfinal. V019sourcef7f7e39e71ee9601a2e8fef084333bed727d772ef497b2c164d8d919dc0795ae andprotocol4953b71fdf2cab19f8ada746350f01f22de43046bc641b57399ff836cf7e4769. Per-modelprogress `outputs/controlled_experiments_v019/{deep_auxiliary_difference,minimal_deep_curve}/epochs.jsonl`, reports/model.pt/.last/record/A_predictions. Summaryscreen_summary.json onlyafterboth200epochfits and3declaredpostprocessingensembles scored. Setup `v019-screen-execution.log`,`v019-course-preflight.log`,`v019-exit-code.txt`. Uponcompletionretrieve stagearchive/info/verification/guardian/completedpod intoNEW `outputs/controlled_experiments_v019/completed_archive/`; verifywithsetup_helpers/verify_archive_v019.py,safeextractmirror,publishonlynew/identicalartifacts, preserveoriginalrootnotebooks. IndependentlyauditArows,fit-onlystatistics,source/data/modelhashes,allfixedrecipes/selectedbudgets/nativepostprocessing/bootstrapandlowesteligiblechoicebefore newcoldFconfirmationseed20261204. NoFworkyet; nooriginalAmodels forFvalidation. No runner-upafterFfailure or extramixsearch. Exactresumeonlyifpartial. Fullopsmetadata `research/orchestration_v019.json`.

**November6,11:46PM Pacific: submitted V018; new official Gym MAE0.17427**, improving preserved0.18025 by0.00598/3.32%. Receipt `research/submission_receipt_v018_final.json`; newCSV603600rowsSHA274668c4dc14e9d20a554c738859fca37e448836797d7260ec7b11464dcde3e2. Final145-check independent audit passed before CLI. Sourcepushedcompetitionbranch, localCLIcommit654bbd8; optionalAIlogupload disabled, visiblehistorylocal. Old0.18025and0.18550CSVs/receipts unchanged. Finalpod4079254 releasedafterverifiedbackup; noactivepods. Goalofficial<=.15 NOTachieved; continuefrozenV019 next.

V019protocol/source/payload alreadyfrozen BEFORE thisofficialscore. Do notchangehypotheses/weights/ratesbasedonit. Readyfornormal-c4/-m16/-g1pod andguardianstage; actualCUDAproofmandatorybeforetwo200epochA fits. Payload5784665B SHAe7a7b786df9899ce1cf04a5bdf7d7d8086dc2e7b1cc77b6b28aaf87f0d9f276c, `outputs/controlled_experiments_v019/setup_helpers`, ownsourcef7f7e39e71ee9601a2e8fef084333bed727d772ef497b2c164d8d919dc0795ae, protocol4953b71fdf2cab19f8ada746350f01f22de43046bc641b57399ff836cf7e4769. No V019approveddatafits/outcomesyet.

**November6,11:45PM Pacific: V018 final fit COMPLETE and independent145-check audit passed.** All67905breaths; onlynewdeep_curve trained196epochs,~2h23m; fiveacceptedall-data weights/cache reused afterexactchecks. CSV603600rows SHA274668c4dc14e9d20a554c738859fca37e448836797d7260ec7b11464dcde3e2 at `outputs/confirmation_v014/final_all_v018/submission.csv`; manifestSHA2a53c1b7b38dee05f6db7f809dc80bb765fc73d3e1d6f157e92e5141054f2e23. NewdeepcurvemodelSHA5c022e57a713e94f9480dab61743517e446990594ccbb7723033d7d78d1adfc3. Fixedweightedmedian+training-onlygridonknowninspiration, fixedmeanunscoredrows. Rebuiltallrawfeatures/trainonlystats, sixfullrecipes/budgets/source/data/model hashes, sixinferencecacheprovenance, independentoutputmath andexactCSVroundtrip passed. Audit `research/final_review_v018.json`. Noofficialnewscoreyet; submitnext. Old0.18025and0.18550CSVs unchanged.

Verified50-file69091854B archive SHA3f50617e28da8b2301818fd4158ace929c75fc4a451e5bce1ca2ac672ba5fc6b underfinal_all_v018/completed_archive; mirrorpreservedrootnotebooks; pod4079254releasedafterverifiedbackup. NoGPUjobsremain. V019nextscreenpayloadpreparedbutNOTrun; onlydispatchafterV018submission ifgoalunmet; keepfrozenhypotheses unchanged.

November6,11:33PM Pacific: livefinalpod4079254 Running,188/196epochs,~5.8mintrainingleft; nofinalmanifestyet. V019futuredeploymentpayloadprepared5784665B/33members SHAe7a7b786df9899ce1cf04a5bdf7d7d8086dc2e7b1cc77b6b28aaf87f0d9f276c; noresource requested/stagedeployed. Helpers `outputs/controlled_experiments_v019/setup_helpers`, pinsv019-pins.json, includingmandatoryactual-CUDA synthetic/control/resumeproof beforeA fits. ActualCUDAproofNOTrun; noapproveddatafit. See `research/orchestration_prepared_v019.json`. FinishV018CSV audit/authorizedsubmissionfirst; ifofficialgoal<=.15unmet, dispatchfrozenV019plan unchanged byofficialfeedback.

November6,11:14PM Pacific: next V019 screen prepared but NOT dispatched. Discussion-inspired separate pressure-difference auxiliary head component48e09c7fbe8ae1e843d39ed2093cc67a96a96c5bc36433f8081a616c034e6346 passed18syntheticchecks including pressurebase/init/control equality, inspiredadjacencymask, gradients, no cross-breath memory, exactresume and changedlosssource rejection. Additional7validation/native-MAE/bestcheckpoint/trainonlystatistics/default-inert checks pass. No approved-datafits/outcomes. Frozenplan4953b71fdf2cab19f8ada746350f01f22de43046bc641b57399ff836cf7e4769 declares two200epochAdeepfits: separateauxhead .1 with47features, and oldcurve-lossdeep with6raw/time/R-Cinputs (feature-removalonly). Three fixed slot-replacement ensembles; currentAref0.182922095, gain>=.003/negativebootstrapupper gate, onlylowesteligible advances to newcoldF seed20261204. Newdriver `controlled_experiments_v019.ipynb` sourcef7f7e39e71ee9601a2e8fef084333bed727d772ef497b2c164d8d919dc0795ae defaultinert. CUDApreflighthelper prepared, NOTrun; source/fieldgates mandatorybeforeapprovedtraining. Operationalpayload/guardian notyetprepared. Do notchangefrozenplanbasedonupcomingofficialscore. V018finalunchanged andhaspriority. Two prototype/audit-exportmistakespreservedandfixed; detailsresearch/screen_preflight_v019.json.

LatestactualV018check afteruserreconnected11:11PM: pod4079254 Running,deep_curve158/196,43.38s/epoch,~28mintrainingleft. Expected~11:40PMtraining/~11:50PMcheckedsubmission. NofinalCSVretrievedyet.

November6,11:01PM Pacific: sharedSSHrequiresfreshpassword/Duo; useraskedtorenewusingpersistentcontrolsocketcommand. Awaitreply; do notrepeatrequestorassumeterminaljob. Lastverifiedfinalpod4079254Runningat9:18PM, finalfitstarted9:15:40PM, fullreusepreflightpassed; nofinalcompletionread. EstimatebasedoncoldEpace/alltrainratio~35–50mintrainingremainingplus10–15minretrieval/audit/submission, NOTcurrentepochverified. Serverguardiancontinuesindependently. Preparedfullfinalaudit `outputs/confirmation_v014/review/audit_final_v018.py`, compiledonly, sourcehashin `research/final_audit_preparation_v018.json`. Actualfinalresultsstillneedretrieveandaudit; official.18025unchanged,target<=.15active.

**November6,9:16PM Pacific: both confirmations complete and independently audited; final V018 running.** Primary cold E six-model meanMAE0.197605952 versus five-model0.202909053; gain0.005303101,95%[-0.006643053,-0.004067906],173auditchecks passed. Prospective V017 fixed weightedmedian+train-onlypressuregridMAE0.194792297; gain0.002813655vs sixmean and0.008116756vs fivebaseline; bothCIupper<0,16independentchecks passed. Sourcefreeze6:26:52PM precedes firstdeep_curveEstart7:14:01PM and Ecomplete9:07PM. NoEpolicy/weight/epochsearch. OriginalAexcluded from E. New results notebook `results_review_v014.ipynb`, report `research/RESULTS_V014.md`. E72-file175471112B archive SHA3a0f60fbe3d36dd1c8bfc3a0668f9d7ba6ea13df04db4eccb6ddebf7d6c52d81 verified locally; oldpod3904789released.

Finalpod **v2gao-4079254**, n05, ordinary-c4/-m16/-g1, started~9:15PMPacific; expectedleaseend~3:15AMNov7. Detachedguardianstage `$HOME/.pa3-setup-control.gty67K/v018-final-20261106`. Currentfinalsourceb960 unchanged. Finalpayload114607B SHAfd9c9767025889dedc32d8fea323acd6994e5b6d3338d74c4e2503519b52191e. ActualCUDAverified GTX1080Ti93%; all rawdata/recipe/checkpoint/preprocessing/cache/row preflight passed and newdeep_curve196epoch fit on67905breaths began9:15:40PM. Five accepted all-data models/cache reused; noholdout. Expected~2.5hplusCSVverification. Source/report/auditpins `research/orchestration_v018.json` and setup v018-pins.json. Noautomatic submission. Guardian archives/verifies/releases onlyafterworkerexit; noautomaticreplacement. Macsleepdoesnotstopremotejobs; SSHmayneedrenewalbeforelocalretrieval/audit/authorizedsubmission. Bestofficial0.18025unchanged; target<=0.15active.

**Next:** inspect live4079254/stage before any replacement. Finalprogress `outputs/confirmation_v014/final_all_v018/deep_curve/epochs.jsonl`, report/model `.last` exact optimizer/RNGresume; finalmanifest/CSVafter196epochs. Setup `v018-screen-execution.log`,`v018-exit-code.txt`. Uponcompletion download stagearchive/info/verification/guardian/completedpod intoNEW `outputs/confirmation_v014/final_all_v018/completed_archive/`; verify with local `outputs/confirmation_v014/final_v018_setup/verify_archive_v018.py`, safelyextractmirror, publishonlymissing/identicalartifacts. Rootnotebooksstayoriginal, executedcopiesinmirror. Independentlyauditfinalall67905model/preprocess/lr/budget/hash, allsixpredictioncaches/IDs, fixedweightedmedian/grid/phasepolicy, exact603600rowCSV/roundtrip, old0.18025CSVunchanged. CommitthenauthorizedGymCLI submit, saveofficialreceipt, preserveoldbestifworse. Continuecontrollednewmechanisms ifofficial>.15. E/secondarynowcomplete—do notrerun. Detailedfrozenpins/scoresinresearchRESULTS/orchestrationfiles.

**Latest live check, November6 7:02PM:** SSH works,3904789 Running; firstfour members complete,offset126/193,deep_curve notstarted. No E outcome observed; V017source freeze6:26:52PM is already earlier than any possible firstdeep_curvestart. Remainingabout2h, close to9:11PMleaseend. New operational preparations `outputs/confirmation_v014/review/audit_E.py` (independently rebuilds rawfeatures/trainonlystatistics/seededsplit/native scores/bootstrap) and `outputs/confirmation_v014/final_v018_setup/build_payload_v018.py` (refuses missing/failed audits before generating finalhelpers/payload); hashes/status `research/operations_preparation_v018.json`. Neither executed against actual E results. Review generated shell/helpers before deployment. Source V018 unchanged.

**Prepared conditional final stage (not executed/deployed):** `final_fit_v018.ipynb` codeSHA **b960eb2976962a1d8a2fee7b6a9633fba74b018190a07d9b89977eea0768b06d**, review `research/final_preflight_v018.json`. Requires BOTH V014primary and V017secondary confirmations and independently bound audits to pass; mandatory expected primary/result/audit and secondary/result/audit rawSHA plus ownsourceSHA. Actualoutcomesunknown. Onacceptedgate it reuses allfive accepted0.18025 all-data checkpoints and cachedtestpredictions AFTER exactmanifest/data/recipe/budget/model/source/preprocessing/row/cachehash checks; onlynewdeep_curvecoldfitsall67905for196 frozenepochs. UsesreviewedV011 fixed-fit/inferencehelpers, with equivalentplainV5constructor (CPUstate/forwardequivalencechecked). FinalA-derivedfixedweightedmedian+all-traininginspiratorygridpolicyappliedu_out0;unscoredrowsfixedmean. Newoutput `outputs/confirmation_v014/final_all_v018`. Bestc344...CSVpreserved. Exactoptimizer/RNGresume and completedartifactpreservation. Defaultinert, nosubmissioncall. Actualall-trainingreusepreflightnotrunyet. Stillneedsoperationalexecutor/guardian/payload fornewordinary4CPU16Gi1GPUcontainer afterE andsecondary audits; do notlaunchifgatesfail. Sourceexpects auditfiles `research/confirmation_review_v014.json` (confirmation_result_sha256,selection_sha256) and `research/postprocessing_confirmation_review_v017.json` (confirmation_result_sha256), bothstatuspassed. Function `run_final_v018(root,resume=...,expected_primary_sha256=...,expected_primary_audit_sha256=...,expected_secondary_sha256=...,expected_secondary_audit_sha256=...,expected_source_code_sha256=...)`; envguardPA3_RUN_FINAL_V018. Earlier 'no finalnotebookyet' entriesbelowarehistorical.

**New prospective follow-on, November6~6:27PM:** V016 fixed CPU postprocessing screen completed on A, referenceprovisional6-modelmean.186264237. Gridonly.184946581; weightedmedianonly.184276718; **weightedmedian+training-onlygrid.182922094565**, gain.003342143,CI[-.004566308,-.002236400],21independentcheckspassed. NoEoutcomeread/model fit/submission. Currentofficial.18025 unchanged. Sources `research/postprocessing_screen_v016.ipynb`, `postprocessing_protocol_v016.json` SHAe91b66f4d7047dc0991f7735955d3f3a594073806bc443e206720f641b73b040, purecomponentscodeSHA4ee67389039846557d74cc1c55884c9a99f0e571745af4febefa4b5c3bce6a0b, `postprocessing_review_v016.json`.

**Before E outcomes**, separate follow-on V017 waspreregistered6:25:08PM; consumer/preflightfrozen6:26:52PM. Protocol `research/postprocessing_confirmation_protocol_v017.json` SHA97214e460ea200a836922245363132c09ef54b133080b89bb342c4e1d191d627; consumer `research/postprocessing_confirmation_v017.ipynb` codeSHAd11073d1ded4945ef5d6fe60da1d0b1ef5ee0240e0990ea8dfe1fc891ab4abcd. It doesnotchange V014runningrecipe. It can reuse current6coldEpredictions ONLYIF preregistration AND consumerfreeze precede FIRST `cold_E_fit_started` eventfor deep_curve; source0f22 ensuresnoE scoringbeforeallfits. Ifgatefails, do NOTrelax; requireanothergroupedsplit. ActualEoutcomesnotobservedyet. Independentprimaryaudit `research/confirmation_review_v014.json` mustexistwithstatuspassed, confirmation_result_sha256 andselection_sha256 bound toactualE; caller suppliesitsrawSHA. PrimaryEpassrequired(norescue). CodebookrefitONLY Efit54323labels. Fixedpostproccomparedagainstbothsixmeanandfivebaseline; positivegain/upper95<0forbothrequired. No alternativeV016policysearchorweighthackingonE. Primaryindependentworkflowremainsunchanged. Runlaterviafunction `run_postprocessing_confirmation_v017(root,expected_primary_audit_sha256=...,expected_source_code_sha256='d110...')` orenvPA3_RUN_POSTPROCESS_V017=1/PA3_V017_PRIMARY_AUDIT_SHA256/PA3_V017_SOURCE_SHA256. PureCPU, no model fit; output`outputs/postprocessing_confirmation_v017`. Finalpolicyifconfirmed: fixedweightedmedian+nearestALL-TRAINinspiratorygridonlyonknownu_out0 rows; unscoredrowsbaseweightedmean. No V014finalnotebookyet.

**Latest user-supplied research:** `../kagglediscussion.md` SHA195e535ce76460231654b2faeb5805d49b52f7fb2b679f545e0813c091484288 read by explicit user request. See `research/DISCUSSION_INSPIRED_ROADMAP_v015.md` for source/rule-conflict provenance, prioritized genuinelynew methods and completed cheap controllerfeasibilitycheck. The576-Afit-breath controllerdiagnostic did notpass its10%consistencygate and didnotproducepressureMAE/predictor. Separateauxdifferenceheads, restrictedmixup, LaplaceNLL, minimaldeepinputs andtraining-neighborcontext remain proposed; no new GPU batch for them yet. V014unchanged. LatestGPUobservation~5:28PM: deepcompleted189,compact178/193. SSHsinceended; no cancellation. Avoidrepeatedloginrequestswhileittrains; retrieveactualstatebeforelease9:11PM/expectedfinish~9PM. NoEoutcomesyetobserved.

**Active user-edited objective:** official mean MAE<=0.15 first, then lower, with broader controlled methods. See `research/OBJECTIVE_015.md`. Best official.18025; median errors do not satisfy this target. Continue current V014 unchanged because it serves this objective; do not declare completion after screening or validation alone.

## Actual running pod correction — November6~3:12PM Pacific

V014 is now dispatched on **v2gao-3904789**, n06, start3:11:37PM Pacific, expected6hleaseend9:11:37PM. Old3870381neverstarted and waspreserved/deletedafter~58minpendingCPUcapacity. Normalcourse launcher reduced-c8to-c4 (actualrequests4to2cores, limits8to4; torchthreads4unchanged), no priority/affinity/toleration/leasechanges. Newstage `$HOME/.pa3-setup-control.gty67K/v014-cpu4-20261106`; updatedhelpers `outputs/confirmation_v014/cpu4_setup/`; payload19066B SHA2f5859c482fe8603978fd0646672901db5fa135ffb2b3d6026eb36fbbfbb2d44. Guardian deployed identicalscientificsources and startedmaincell; actualGPUverifiedGTX1080Ti. NoEfitprogressoroutcomeobservedyet. Model/protocolhashesbelowunchanged. Oldpendingstagecancelled/preserved; do notmonitoroldpod. See `research/orchestration_v014.json` and newestPROCESS_STATUS. New userrequesttoinspectMLEvolve/Disarraymethodologycompletedin `research/METHOD_REVIEW_MLEVOLVE_DISARRAY.md`; findingsapplytofutureexperiments, notfrozenE. Exactcompetitorventilatorrecipesnotfound; officialDisarraylistingseparatestest-feedbackruns. Noexternaldata/solutioncodedownloads.

## Latest active state — V014, November6~2:14PM Pacific

Read newest `PROCESS_STATUS.md` and `results_review_v013.ipynb`. V013 completed and independently audited74/74. Winning deep curve-loss mixture A MAE.1862642374201326 vs.19085102921770208; it passed frozen.003gain/negativebootstrapgate. Seed-only.189368987 belowgate; combined.186703791 worse thanwinner. Best official remains.18025, not thisA score. V013archive54files177513224B SHA8b41b24ac327a37691f4a75d14b8f1f53f0d69dff41a0b8e5c4ef8b45016a177, local `outputs/controlled_experiments_v013/completed_archive/` including safe mirror; oldGPUreleased.

Ordinary new pod **v2gao-3870381** requested~2:12PM; Pending at2:13PM. Guardianstage `$HOME/.pa3-setup-control.gty67K/v014-deploy-20261106` is active and dispatches onReady. Do not request duplicates. Sources/helpers/payload are under `outputs/confirmation_v014/setup_helpers/`; notebook `confirmation_v014.ipynb` codeSHA `0f22f8168da6e9304c541ab8415c573d6ad4efdf31d5a1391619448c8d478719`, `research/confirmation_protocol_v014.json` SHA `dee5840ee16262dc282ebeb98643cb24e312e55761634f8fae074ed6c921f6f1`. Payload19010B SHA7478c854644c980f6ac3f571bcd4e775fb3d5dca1b6332564a20df2ddc9e0451. Frozen E seed20261203,54323fit/6791val insideAfit, originalAval excluded, all six members COLD. No actual E split/outcome/fit observed yet. Fixed winner weights deep.25/deep_curve.25, compact/curve/memory/offset.125each; baseline deep.5 and four.125. Oldmembers retain A-selected193/189/193/191/193budgets; deep_curve196. All recipe rates frozen. No E epoch/weight search or runner-up. E is resampling evidence. Only positivegain/upper95<0 passes. Source/default/schema/CPU loss+resume checks passed, no E label access locally. Expected5–6GPUhours plusqueue; preserve checkpoints and use normalcourse replacement ifleaseexpires, never shortenbudgets/bypassquota.

Course output `outputs/confirmation_v014/`; per-member `E_models/*/epochs.jsonl`; setup `v014-screen-execution.log`, `v014-exit-code.txt`; result `confirmation_result.json`, locks `locked_before_E.json`, `E_split.json`. Guardian archives/verifies each file then releasesidleGPU. It neverallocates resources. Check every~10minutes and wait. SSH oftendisconnects whileMacsleeps; detachedjobscontinue. AskuseronlynecessaryTerminalpassword/Duo. AfterEcompletion retrieve/verifyarchive and independently auditlabels/rows/fixedblends/bootstrap/checkpoints; onlyifpassed prepareall-approvedfinalfornewdeep_curve (otherfiveacceptedall-data models maybereusedonlyafter exactdata/recipe/source/preprocess/modelhash checks), verify aligned603600rowCSV andsubmit. NoV014finalnotebookhasbeenpreparedyet. Preserveofficial.18025 allfiles. Audit-only genuinefix: V013Aselectedpayload usesexecuted_epochs notcompleted_epochs; originalfailedauditscriptretained. Old notesbelowarestale.

## Active continuation — V013, November 6 morning

User explicitly requested continued controlled iterations after official0.18025. V013 is now running in ordinary course pod `v2gao-3506641`, node n05, requested8:03:55AM Pacific; expected six-hour lease to~2:04PM. See newest `PROCESS_STATUS.md` entry. Frozen source `controlled_experiments_v013.ipynb`, codeSHA `56cb9d7e824e58126bddd71c7c0f7063844974c31ee00a6dac23f2112657615a`; plan `research/protocol_v013.json` SHA `6a32108a623a81b461e8b187784aa5bcf52a032d1bdd6c9a8fddb1cd77bc7cc1`. Deep seed20261103 only and deep curve_l1 .10 only train sequential200epochs each. Same A split/features/originalschedule; three mixtures declared before new results; reference is currentfive-model A.190851029, not the obsolete originalpair. Only lowest eligible gain>=.003 and bootstrap upper<0 advances to a new E grouped confirmation seed20261203. No E outcomes or work yet. Existing best official.18025 artifacts preserved.

Operational helpers/payload/pins: `outputs/controlled_experiments_v013/setup_helpers/`; login guardian stage `$HOME/.pa3-setup-control.gty67K/v013-deploy-20261106`. Course output `outputs/controlled_experiments_v013`; course progress `deep_seed03/epochs.jsonl`, then `deep_curve/epochs.jsonl`; setup `v013-screen-execution.log`, `v013-exit-code.txt`. Guardian monitors to completion, snapshots source/run evidence, verifies every file then releases GPU. It never allocates replacements. After completion, download stage archive/info/log into a separate local folder, run `verify_archive_v013.py`, preserve old files, independently recompute scores/blends/bootstrap before confirmation. Check jobs roughly every10minutes and wait to conserve usage. Source and tiny CPU loss/resume proofs passed; actual CUDA proofs precede training. Last live observation at~8:09AM: first arm epoch2/200, GPU95%, ~42s/epoch. Do not interpret early validation scores as completed results.

## Current status override — November 6, 2026

V011 has completed. New official Gym **MAE0.18025**, improving on the preserved0.18550 result by2.83%. See `research/RESULTS_V011.md`, `research/submission_receipt_v011_final.json` and `PROCESS_STATUS.md` first. All five cold D fits completed and confirmed the frozen ensemble:0.196962270 versus reference0.203508566. Independent D audit211/211 passed. All-approved final curve193/memory191/offset193 fits completed; accepted all-data compact/deep reused after exact checks. Final artifact audit146 plus5 full-configuration checks passed before submission. New CSV603600rows SHA `c344a485f5ef1290aadf5dfd379333009efab674b7ccdff6f361e225a4b8b77a` is at `outputs/confirmation_v011/final_all/submission.csv`. Final source codeSHA `35abc3371ddaf717ca3fc7ff908f4e06517e642c0d0fc6b089342870f533c6de` fixes only the documented legacy canonical-lock verifier. Original pre-fix sources/logs remain preserved.

No current GPU pod or queued training remains. Guardian archived and per-file verified all results before deleting pod2927534. Recovery archive under `outputs/confirmation_v011/completed_recovery_archive/`, SHA `3415bb3005a9dcd4f1c7df45791efc3b5b0039ea6c96253b19306ed64a939ff6`,129files/180449172bytes. Do not rerun D or final fitting. Mean MAE0.10 has not been achieved; the0.098 A median was not an official score. Earlier account-migration instructions below and the three HANDOFF documents describe a historical checkpoint, not current live state.

Prepared November 5, 2026, afternoon Pacific, for a move to another Codex account.
Read this file before performing setup or launching experiments. This is a record
of user instructions, work, evidence and remaining actions, not an internal reasoning trace.

## Immediate state

- Best accepted official Gym MAE: **0.18550**. Preserve its CSV, weights and receipt.
- Best new A-validation candidate: **0.19085102921770208**, versus original pair
  **0.19656260982217663**. Those are validation scores, not new official scores.
- New candidate median point absolute error: **0.09816378355**. Official metric is mean MAE.
- It is the fixed mixture: deep **0.5**; original compact, curve-consistency,
  learned-memory and shared-offset members **0.125 each**.
- Its gain is .005711580604474548; whole-breath95% interval for candidate minus
  reference is **[-.007219534875537107,-.004389991151684003]**.
- V012 screen181 checks plus independent118 checks passed. No weights/rosters
  were fitted: exactly one additional named mixture was declared before calculation.
- **No actual D split, locked D selection, D training, D outcome or V011 final fit exists.**
- Prepared confirmation/final notebooks and deployment payload are ready. They
  have **not been dispatched**. Do not claim these stages completed.
- Latest user request: preserve everything for another Codex account to continue.
  Work stopped at this handoff; no new model training was launched for migration.

## Live GPU: attend to this first

Course pod **v2gao-2729938**, node **its-dsmlp-n06.ucsd.edu**, was running and idle
when checked. It started **2026-11-05T23:16:48Z =3:16:48PM Pacific**. Its six-hour
lease should end **9:16:48PM Pacific November5**. Recheck current state and clock;
this document will become stale. GPU GTX1080Ti11GB,0MiB/0% utilization at handoff.

Environment verified: Python3.11.9, Torch2.2.1+cu121, CUDA12.1, cuDNN8902,
numpy1.26.4,pandas2.2.2. Local Mac is M3Pro18GB without NVIDIA/CUDA.

Do not reserve a second GPU while this one is available. If this pod expires,
use the ordinary course launcher and resume preserved checkpoints. No quota,
priority, toleration or lifetime bypass. If migration is delayed and the GPU is
unused, release it after preserving its metadata; persistent course files remain.

## User authorization and preferences

The user explicitly answered **"Approve this batch and future controlled iterations"**.
See research/authorization_v008.json and the visible conversation snapshots.
Standing approval covers controlled research, grouped confirmation, all-approved
final fits and validated submission within this task. Do not ask for routine
hypothesis approval again. Ask for missing password/Duo/login steps only when
necessary; passwords and Duo responses must be entered by the user in Terminal.

Only assignment-approved Gym data. Never download original Kaggle data, existing
competition solutions, pretrained solutions or unrelated datasets. Modeling code
must be in `.ipynb`; operational execution/audit helpers may be Python/shell.
Preserve previous files/models/CSVs. Log configurations, seeds, runtime, scores,
genuine mistakes, source/data/model hashes and visible AI interactions.

Keep status checks about **every10minutes** and updates brief. While models run,
wait instead of repeatedly reasoning or polling. Subagents may be used for useful
independent tasks. Goal is continued improvement toward .10 mean MAE; there is no
claim that .10 is achievable. Earlier official <=.20 objective was achieved.

## Workspace and account connection

Local parent: `/Users/generalclasher/Documents/dsc102/pa3`
Local Git project: `/Users/generalclasher/Documents/dsc102/pa3/ventilator-pressure-prediction`
Branch: `master`. Git commits preserve source and reports; large outputs/data are ignored.
The latest handoff commit is recorded in `handoff/git_checkpoint.txt`.

UCSD username `v2gao`; Gym user ID `jhei3w76dhk7`.
Course project: `/home/v2gao/dsc102/pa3/gym-workspace/ventilator-pressure-prediction`
Course Python: `/home/v2gao/dsc102/pa3/.venv/bin/python`
Course setup: `/home/v2gao/dsc102/pa3/setup`
Login-node home is different: `/dsmlp/home-fs03/08/308/v2gao`.
Do not assume login `$HOME/dsc102/...` is the mounted course home.

Shared SSH socket: `/Users/generalclasher/Documents/dsc102/pa3/.datahub-ssh/control`.
It was renewed during this conversation. Check it first; renew only if needed:

```bash
ssh -M -S /Users/generalclasher/Documents/dsc102/pa3/.datahub-ssh/control -o ControlPersist=7200 -o ServerAliveInterval=60 -o UserKnownHostsFile=/Users/generalclasher/Documents/dsc102/pa3/.datahub-ssh/known_hosts -o StrictHostKeyChecking=yes v2gao@dsmlp-login.ucsd.edu
```

The user completes password/Duo there and leaves the window open. For automation:

```bash
ssh -S /Users/generalclasher/Documents/dsc102/pa3/.datahub-ssh/control -o BatchMode=yes -o ConnectTimeout=10 -o UserKnownHostsFile=/Users/generalclasher/Documents/dsc102/pa3/.datahub-ssh/known_hosts -o StrictHostKeyChecking=yes v2gao@dsmlp-login.ucsd.edu 'KUBECONFIG=/home/linux/dsmlp/08/308/v2gao/.kube/config TERM=dumb /usr/bin/kubectl get pods -o wide'
```

Use `kubectl exec -i` when forwarding a Python/heredoc stdin to the pod. Without
`-i`, Python may quietly read EOF. Never train on the login node.

Official replacement launcher, when needed:

```bash
/opt/launch-sh/bin/launch-scipy-ml.sh -W DSC102_FA26_001 -g 1 -c 8 -m 16 -i ghcr.io/ucsd-ets/scipy-ml-notebook:stable -B /opt/k8s-support/bin/initenv-createhomedir.sh /bin/sleep infinity
```

## Prepared next action

Read `HANDOFF_CONFIRMATION_V011.md`, `HANDOFF_FINAL_FIT_V011.md`, and
`HANDOFF_OPERATIONS_V011.md`. Authoritative notebooks:

- `confirmation_v011.ipynb`: codeSHA
  `0208428c5ef3407990d05a4b7f08a9c46b9df4465680957b236b95fccf370c2d`.
 23 synthetic protocol checks and independent review passed.
- `final_fit_v011.ipynb`: codeSHA
  `f81befd83ede7d65dbce816f430f028256b140cc16903ace047205029b22b83a`.
 20 synthetic protocol checks, metadata checks, inference interruption recovery
 checks and independent review passed.

The fully prepared source payload and operational helpers are under
`outputs/confirmation_v011/setup_helpers/`. Models remain notebook code.
`v011-deploy.tar.gz` is1,377,634bytes, SHA256
`f1f1b5c24635a06c1ec7ae9b5c0b24b8b3eb14ee59e5db26fcfd71849d849b04`.
`v011-pinned-sources.json` binds source hashes and all archive dependencies.
`research/migration_state_v011.json` records the preparation state.

The login staging directory is
`$HOME/.pa3-setup-control.gty67K/v011-deploy-20261105`.
After confirming the staged files/SHA and reviewing the helpers, this command
starts the already-approved sequential pipeline without needing the Mac online:

```bash
ssh -S /Users/generalclasher/Documents/dsc102/pa3/.datahub-ssh/control -o BatchMode=yes -o ConnectTimeout=10 -o UserKnownHostsFile=/Users/generalclasher/Documents/dsc102/pa3/.datahub-ssh/known_hosts -o StrictHostKeyChecking=yes v2gao@dsmlp-login.ucsd.edu 'PA3_STAGE="$HOME/.pa3-setup-control.gty67K/v011-deploy-20261105"; nohup /bin/bash "$PA3_STAGE/guardian_v011.sh" > "$PA3_STAGE/guardian.log" 2>&1 < /dev/null & echo $! > "$PA3_STAGE/guardian.pid"'
```

The guardian is hardcoded to pod2729938. If replacing the pod, preserve the old
script and update that ID before dispatch. It serializes supervisors; waits for
Ready; preserves changed old files; deploys the reviewed source; starts D;
starts final fits only if D passes; and archives all artifacts, verifies safe
regular tar members plus every individual file hash before deleting the idle GPU.
It never allocates replacement resources automatically. It has been compiled/
reviewed, but this V011 end-to-end pipeline has **not yet run**.

Confirmation is roughly4GPUhours; final new-member fits roughly2 more if passed.
A second lease may be necessary. Do not shorten epochs or silently drop a member
just to fit the lease. Checkpoints and datasets persist in course storage. On a
lease interruption, inspect status/logs, preserve terminal pod metadata, use the
normal launcher, update guardian pod ID, and resume the exact frozen stages.

## Scientific protocol: do not change mid-confirmation

Original grouped A:61,114fit /6,791validation, all80 rows per breath remain together.
Combined47 known features, seed20261102,batch256, Adam/no decay, original full200
replay rates. Metric is native point-weighted inspiration-only MAE (`u_out==0`).
Training-only input mean/std and target median/IQR. State resets between breaths.
Future known controls are allowed in this offline task; pressure labels are never inputs.

Five completed fixed A candidates are compared before creating D. The lowest
eligible one is V012's five-member blend. Minimum A gain.003 AND whole-breath95%
bootstrap upper difference<0;1000draws/seed20261201. No median-based promotion.

D uses sklearn train_test_split, random_state20261202,test_size6791, stratified
by known joint R/C inside original Afit. Dfit54,323/Dvalidation6,791; original
Avalidation excluded from both. **Cold-fit every D member** with own Dfit-only
statistics. Existing A models trained on these D breaths and cannot score D.
Frozen epoch/rate prefixes:

| Member | Epochs | Candidate weight |
|---|---:|---:|
| Original compact BiLSTM128x2 |193|.125|
| Original deep BiLSTM |189|.5|
| Curve-consistency compact |193|.125|
| Learned-memory compact |191|.125|
| Shared-offset compact |193|.125|

D reference is cold compact/deep .5/.5. D passes only positive gain and whole-breath
95% upper difference<0. No D-based epoch/weight search and no runner-up if it fails.
D is resampling confirmation, not a pristine untouched test: A was used repeatedly
for research. No actual D outcome has yet been accessed.

Immutable artifacts will live under `outputs/confirmation_v011/`:
`D_split.json`, `locked_before_D.json`, `confirmation_result.json`, member
checkpoints/reports/predictions. Lock binds all five A alternatives, chosen recipe,
source/inputs, split hashes, weights and budgets. Canonical lock digest has no
self-reference. On D pass, final fitting uses all67,905approved breaths for the
three new members. Reuse the already accepted all67,905-trained original compact
and deep ONLY after exact manifest/weight/recipe/rate/data/count/stat verification.
This saves hours. Reuse is allowed only for final inference, never D scoring.

Expected new output: `outputs/confirmation_v011/final_all/submission.csv`,
603,600 rows in exact approved sample/test ID alignment, finite native pressure.
There is no new CSV yet. Root must independently verify it and its evidence before
Gym submission. The pipeline deliberately does not submit automatically.

## Best official artifact: do not overwrite

`outputs/improvements_v005/confirmation_round1/final_all/submission.csv`
SHA256 `ff149f3ab87e1e52b948f536c9fdf9a526471ac0723b6b785bf84c053ebed607`.
Receipt: `research/submission_receipt_v005_final.json` (official.18550).
All-data compact weightSHA
`19897b624599c57f2e4a7f976b2d2fdd4d0b5b1ba3f3dbf6884198ebdef23883`;
deep `591e3a778af84bfe7fa0f6592f8595fa2c969bdbb37fc0a36a2a251eacb4aad0`.
Manifest: `outputs/improvements_v005/confirmation_round1/final_all/final_manifest.json`.

For a verified validated new CSV only, existing local CLI:

```bash
.venv/bin/aicodinggym mle submit ventilator-pressure-prediction -F <new_verified.csv> --user-id jhei3w76dhk7 --workspace-dir /Users/generalclasher/Documents/dsc102/pa3 --no-upload-logs -m '<verified description>'
```

Commit reviewed source first; CLI may push competition source. Preserve receipt,
CSV/model/source hashes, official result and visible history. Do not use hidden
scores to tune weights. Keep .18550 as best if the new official result is worse.

## Data and files preserved

Approved train5,432,400rows=67,905breaths; test/sample603,600rows=7,545breaths.
Each breath80steps. R{5,20,50};C{10,20,50}. Original audits found no missing/nonfinite
values, valid grouping/increasing times, no exact duplicate or train/test matching
input breaths. Negative pressure retained. IDs are alignment keys, never predictors.

Approved hashes:

- train.csv `2dc30dc5c8e603c8c68200830eab7ed8c7af42c823f8ae68b0beb663eea817d7`
- test.csv `1ed86b32480e93397cc961dfd09af2d0bedfbab901921eac44de8ed78c3f1672`
- sample `de4c137a22804654b597723f32470b24f23d9ef662205eca0fe31b68970f0594`

Full existing data/weights/predictions/logs remain in the local project and
persistent course home. `handoff/workspace_inventory.json` lists local files;
large ignored outputs are not in Git. If moving computers, copy the whole project
including ignored data/outputs; a source/context-only bundle is not the dataset
or all model weights. Switching Codex accounts on this Mac leaves these files intact.

Completed archives copied locally and per-file verified:

| Batch | Local directory | Archive bytes | SHA256 |
|---|---|---:|---|
| V008 |outputs/controlled_experiments_v008|63,940,755|01d005f2e7b6ce42d59e5eaa7d85880e88a71baa85fd88b2735d67cd4d6218e6|
| V009 |outputs/controlled_experiments_v009|33,555,353|42a2389402af8a09ae90675caaf49e6124114720b0962f04f849338609443676|

Each has server_snapshot_completed with preserved executed notebooks and
per-file manifest. V008 audited403/403. V009 trained200epochs per arm; its old
failed prefit source/profiles/logs are also retained. Prior V007 full81-file archive
280,134,657B SHA059ceb600a94b20d42b64be8ab46c7c8748bfd5b293f699b4f472afdbf4504a1
is preserved under outputs/approved_experiments_v007. Login staging for V008/009:
`$HOME/.pa3-setup-control.gty67K/v008-deploy-20261105`.

## Results already established: avoid rerunning them

All figures below are original A fixed equal pairs with unchanged deep unless noted.

| Test | A pair MAE | Outcome |
|---|---:|---|
| Original compact/deep |.196562610|Reference; official all-data result.18550|
| V006 slower300compact |.193145077|Fresh C confirmation CI crossed0; not promoted|
| V007 OOF residual correction |.195583736|Gain.000979 below frozen.003gate|
| V007 pressure-category head |.204354648|Worse|
| V007 deep AdamW1e-4 |.198516379|No demonstrated gain|
| V007 deep dropout.25 |.201478762|Worse|
| V008 curve consistency |.195987534|Small gain, CI crosses0|
| V008 learned memory |.196302779|Small gain, CI crosses0|
| V008 attention |.202850346|Worse|
| V009 shared offset |.194224170|Gain.002338, CI upper.000112; insufficient alone|
| V009 full-context TCN |.270269705|Worse; train MAE.349 suggests underfitting this recipe|
| V010 deep.5 +compact/curve/memory thirds of.5 |.192230255|Provisional gate passed, independently verified58checks|
| V010 includeattention quartershares |.192303462|Provisional gate passed; worse than previous mixture|
| V012 replaceattention withoffset quartershares |.190851029|Current lowest candidate; independent118checks|

Read `results_review_v008.ipynb`, research/diversity_screen_v010.ipynb,
research/diversity_screen_v012.ipynb and their independent JSON reviews.
Older V005 components/history contain previous GRU/TCN/schedule/features/scaling/
R-C/seed experiments. Generic lag/future-input/standardization ideas are already
implemented, not new work. Target pressure quantization alone cannot explain a
large expected gain. No exact replicate-input noise-floor estimate exists.

## Genuine issues and recovery knowledge

- Strict deterministic Torch2.2 CUDA floating cumsum was unsupported in V007
  probability decoding; CPU detached median decoding fixed it. Do not disable determinism.
- Original Conv1d TCN was84.42x baseline on this GPU. Capacity gate stopped before
  any data fit. Exact shifted-input linear convolution reduced it to1.028x;
  CPU107checks compare outputs/all gradients; GPU proofs/resume passed. Original
  source and failed-stage evidence retained. Architecture/capacity were unchanged.
- A final prediction .npy orphan before its JSON metadata used to break resume;
  now recover/recompute only with exact matching identities, preserve conflicts.
- Notebook execution outputs change raw file hashes. Whitelisted notebook
  provenance permits differing raw bytes only if exact executable code matches;
  binary/data/report hashes remain strict. Actual raw hashes then freeze in the
  D lock. Never casually waive a failed fingerprint.
- CodeSHA for orchestration is SHA256 of newline-joined code-cell sources.
  Training v008 internally uses a different explicit cell delimiter; its own
  helper is self-consistent. Prediction/row hashes in records are raw contiguous
  array bytes; V5 data fingerprints include shape/dtype. Preserve these conventions.
- Final env Dresult hash is the raw JSON fileSHA; selection hash is compact sorted
  canonical JSONSHA (no self-reference). They are different quantities.
- The guardian snapshots only after worker and wrapper locks release, archives
  symlink targets as regular files, includes explicitly listed operational helpers,
  and verifies every safe tar member before deleting the idle GPU.
- Account usage-limit approval review interrupted earlier monitoring. Server
  training completed and archived/released safely. This was not loss of data.

## AI history and portable context

Original assignment/discussion PDFs are copied in `handoff/course_context/` when
available; the original copies also remain in the parent assignment folder.

`interaction-history/` contains cumulative visible user/assistant snapshots with
hash manifests. The latest is noted in `handoff/context_manifest.json`. System/
developer text, hidden reasoning, tool payloads and account secrets are excluded.
Run `outputs/confirmation_v011/setup_helpers/export_visible_history.py` on this
Mac if available; the raw Codex session path may not exist in another account.
Use the saved visible snapshot as the portable history rather than copying raw
Codex session internals. Parent SETUP_LOG.md is append-only context.

Paste `START_NEXT_AGENT.txt` into the new account and open this same project.
Do not infer final completion from a source notebook existing: D and final CSV
are still pending. Start from the live pod/status and prepared payload above.

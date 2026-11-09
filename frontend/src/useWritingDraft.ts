import { useCallback, useEffect, useRef, useState } from 'react'
import { z } from 'zod'
import { ApiError, request } from './api'
import { commitDraft, commitSubmission, writingRequests, type WritingRequest } from './writingApi'
import { DraftSchema, HistorySchema, type WritingDraft, type WritingSubmission } from './writingSchemas'
const EditorSchema=z.object({text:z.string(),checklist:z.array(z.string()),model_revealed:z.boolean()})
const RecoverySchema=z.object({base_revision_id:z.string(),editor:EditorSchema})
export type EditorValue=z.infer<typeof EditorSchema>
const empty:EditorValue={text:'',checklist:[],model_revealed:false}
const equal=(a:EditorValue,b:EditorValue)=>JSON.stringify(a)===JSON.stringify({text:b.text,checklist:b.checklist,model_revealed:b.model_revealed})
export function useWritingDraft(draftId:string){
 const [draft,setDraft]=useState<WritingDraft|null>(null)
 const [editor,setEditor]=useState<EditorValue>(empty)
 const [base,setBase]=useState('')
 const [dirty,setDirty]=useState(false)
 const [busy,setBusy]=useState(false)
 const [error,setError]=useState('')
 const [operation,setOperation]=useState<WritingRequest|null>(null)
 const [conflict,setConflict]=useState(false)
 const [composing,setComposing]=useState(false)
 const [history,setHistory]=useState<z.infer<typeof HistorySchema>|null>(null)
 const [submission,setSubmission]=useState<WritingSubmission|null>(null)
 const lock=useRef(false)
 const latest=useRef<EditorValue>(empty)
 const baseRef=useRef('')
 const path='/writing/drafts/'+draftId
 const recoveryKey='trilingo.writing-recovery.'+draftId
 const persist=useCallback((value:EditorValue,revision:string)=>{try{sessionStorage.setItem(recoveryKey,JSON.stringify({base_revision_id:revision,editor:value}))}catch{/* Backend autosave still works; leave-page warning protects current input. */}},[recoveryKey])
 const clearRecovery=useCallback(()=>{try{sessionStorage.removeItem(recoveryKey)}catch{/* Server draft is already acknowledged. */}},[recoveryKey])
 const loadHistory=useCallback(async(offset=0)=>{try{const value=await request(path+'/history?offset='+offset+'&limit=20',HistorySchema);setHistory(old=>offset&&old?{...value,revisions:[...old.revisions,...value.revisions],conflicts:[...old.conflicts,...value.conflicts]}:value)}catch(err){setError(err instanceof Error?err.message:'Could not open revision history. Retry.')}},[path])
 useEffect(()=>{let active=true;async function load(){
  let pending=writingRequests.pending(path+'/revisions')
  if(pending){const interruptedSave=pending;try{await commitDraft(interruptedSave);pending=null}catch(err){if(err instanceof ApiError&&err.code==='writing_conflict'){writingRequests.clear(interruptedSave.body.request_id);pending=null}else if(active)setError(err instanceof Error?err.message:'Retry the interrupted save.')}}
  try{const value=await request(path,DraftSchema);if(!active)return;setDraft(value);let local:z.infer<typeof RecoverySchema>|null=null;try{const raw=sessionStorage.getItem(recoveryKey);const parsed=raw?RecoverySchema.safeParse(JSON.parse(raw)):null;if(parsed?.success)local=parsed.data}catch{/* Invalid local recovery does not replace the server draft. */}
   const restored=local&&!equal(local.editor,value.current)?local.editor:{text:value.current.text,checklist:value.current.checklist,model_revealed:value.current.model_revealed}
   const revision=local&&!equal(local.editor,value.current)?local.base_revision_id:value.current.id
   latest.current=restored;baseRef.current=revision;setEditor(restored);setBase(revision);setDirty(!equal(restored,value.current));setOperation(pending)
   if(revision!==value.current.id){setConflict(true);void loadHistory()}
   else if(equal(restored,value.current))clearRecovery()
   const interrupted=writingRequests.pending(path+'/submissions');if(interrupted){setOperation(interrupted);try{const result=await commitSubmission(interrupted);if(active){setSubmission(result);setOperation(null)}}catch(err){if(active)setError(err instanceof Error?err.message:'Retry the interrupted submission.')}}
  }catch(err){if(active)setError(err instanceof Error?err.message:'Could not open draft. Retry.')}
 }void load();return()=>{active=false}},[path,recoveryKey,loadHistory,clearRecovery])
 function update(next:EditorValue){latest.current=next;setEditor(next);setDirty(true);setSubmission(null);persist(next,baseRef.current)}
 const save=useCallback(async(pending?:WritingRequest)=>{
  if(lock.current||!draft||composing||(conflict&&!pending))return
  lock.current=true;setBusy(true);setError('')
  const value=pending?EditorSchema.parse(pending.body):{...latest.current,checklist:[...latest.current.checklist]}
  const op=pending??{path:path+'/revisions',body:{request_id:crypto.randomUUID(),expected_revision_id:baseRef.current,...value}}
  setOperation(op)
  try{const saved=await commitDraft(op);setDraft(saved);baseRef.current=saved.current.id;setBase(saved.current.id);setOperation(null);setConflict(false)
   if(equal(latest.current,value)){setDirty(false);clearRecovery()}else{setDirty(true);persist(latest.current,saved.current.id)}
  }catch(err){if(err instanceof ApiError&&err.code==='writing_conflict'){writingRequests.clear(op.body.request_id);setOperation(null);setConflict(true);try{setDraft(await request(path,DraftSchema));await loadHistory()}catch{/* The conflict message remains visible; input stays in the editor. */}}else if(err instanceof ApiError&&['validation','writing_checklist','writing_revision','request_conflict','request_too_large'].includes(err.code)){writingRequests.clear(op.body.request_id);setOperation(null)}setError(err instanceof Error?err.message:'Could not save. Retry the same action.')}
  finally{lock.current=false;setBusy(false)}
 },[draft,composing,conflict,path,clearRecovery,persist,loadHistory])
 useEffect(()=>{if(!dirty||busy||composing||conflict||operation)return;const timer=setTimeout(()=>void save(),800);return()=>clearTimeout(timer)},[dirty,busy,composing,conflict,operation,editor,base,save])
 useEffect(()=>{const warn=(event:BeforeUnloadEvent)=>{if(dirty||operation){event.preventDefault();event.returnValue=''}};window.addEventListener('beforeunload',warn);return()=>window.removeEventListener('beforeunload',warn)},[dirty,operation])
 async function submit(selfReviewed:boolean,pending?:WritingRequest){
  if(lock.current||!draft||composing||(!pending&&(dirty||conflict)))return
  lock.current=true;setBusy(true);setError('');const op=pending??{path:path+'/submissions',body:{request_id:crypto.randomUUID(),revision_id:draft.current.id,self_reviewed:selfReviewed}};setOperation(op)
  try{setSubmission(await commitSubmission(op));setOperation(null)}catch(err){if(err instanceof ApiError&&['validation','empty_writing','writing_revision','request_conflict'].includes(err.code)){writingRequests.clear(op.body.request_id);setOperation(null)}setError(err instanceof Error?err.message:'Could not submit. Retry the same action.')}finally{lock.current=false;setBusy(false)}
 }
 function retry(){if(!operation)return;if(operation.path.endsWith('/submissions'))void submit(false,operation);else void save(operation)}
 function acceptNewRevision(){if(!draft||lock.current)return;baseRef.current=draft.current.id;setBase(draft.current.id);setConflict(false);setError('');setDirty(true);persist(latest.current,draft.current.id)}
 return {draft,editor,update,dirty,busy,error,operation,conflict,composing,setComposing,history,loadHistory,submission,save,submit,retry,acceptNewRevision}
}

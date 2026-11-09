import { useEffect, useRef, useState } from 'react'
import { request } from './api'
import { Badge, Button, FeedbackPanel } from './components'
import { ImeGuide } from './ImeGuide'
import { WritingEditor } from './WritingEditor'
import { HandwritingPage } from './HandwritingPage'
import { commitDraft, writingRequests } from './writingApi'
import { WritingCatalogSchema } from './writingSchemas'
import type { z } from 'zod'
import { startStudy } from './studyApi'
export function WritingPage({courseId,destination,onOpen,onChanged}:{courseId:string;destination:string;onOpen:(id:string)=>void;onChanged:()=>void}){
 if(destination&&destination!=='drawing')return <WritingEditor key={destination} draftId={destination} onChanged={onChanged}/>
 return <section className="writing-workspace"><a className="back-link" href="#practice">Back to practice</a><div className="page-heading"><div><h1>Make Japanese your own</h1><p>Try Japanese input, form a character or keep a short composition.</p></div></div><nav className="writing-tabs" aria-label="Writing modes"><a href="#writing" aria-current={!destination?'page':undefined}>Typing & composition</a><a href="#writing/drawing" aria-current={destination==='drawing'?'page':undefined}>Character formation</a></nav>{destination==='drawing'?<HandwritingPage courseId={courseId} onChanged={onChanged}/>:<WritingHome courseId={courseId} onOpen={onOpen}/>}</section>
}
function WritingHome({courseId,onOpen}:{courseId:string;onOpen:(id:string)=>void}){
 const [preview,setPreview]=useState(false)
 const [catalog,setCatalog]=useState<z.infer<typeof WritingCatalogSchema>|null>(null)
 const [error,setError]=useState('')
 const [busy,setBusy]=useState(false)
 const [limit,setLimit]=useState(20)
 const [revision,setRevision]=useState(0)
 const keys=useRef(new Map<string,string>())
 const lock=useRef(false)
 useEffect(()=>{let active=true;setCatalog(null);async function load(){try{const value=await request('/courses/'+courseId+'/writing?include_drafts='+preview+'&limit='+limit,WritingCatalogSchema);if(active){setCatalog(value);setError('')}}catch(err){if(active)setError(err instanceof Error?err.message:'Could not open writing. Retry.')}}void load();return()=>{active=false}},[courseId,preview,limit,revision])
 async function create(taskId:string,typed=false){if(lock.current)return;lock.current=true;setBusy(true);setError('');const key=(typed?'typed:':'draft:')+taskId;const requestId=keys.current.get(key)??crypto.randomUUID();keys.current.set(key,requestId);try{if(typed){const saved=await startStudy(courseId,taskId,requestId,'writing_task',preview);onOpen(saved.id)}else{const op=writingRequests.list().find(item=>item.path==='/courses/'+courseId+'/writing/drafts'&&item.body.task_id===taskId)??{path:'/courses/'+courseId+'/writing/drafts',body:{request_id:requestId,task_id:taskId,preview_draft:preview}};const saved=await commitDraft(op);location.hash='writing/'+saved.id}}catch(err){setError(err instanceof Error?err.message:'Could not start writing. Retry.')}finally{lock.current=false;setBusy(false)}}
 return <><ImeGuide courseId={courseId}/><label className="checkbox"><input type="checkbox" checked={preview} onChange={event=>setPreview(event.target.checked)}/>Include draft writing tasks · Japanese review pending</label>{error&&<FeedbackPanel kind="error">{error}<Button variant="secondary" pending={busy} onClick={()=>setRevision(value=>value+1)}>Reload writing</Button></FeedbackPanel>}{!catalog?<p role="status">{error?'Use Reload writing when the local service is ready.':'Opening writing tasks…'}</p>:<><section><h2>Choose a beginner task</h2>{catalog.tasks.length?catalog.tasks.map(task=><article className="writing-task" key={task.id}><div><h3>{task.genre.charAt(0).toUpperCase()+task.genre.slice(1)}</h3><Badge>{task.stage.slice(-1).toUpperCase()} · {task.status==='published'?'Technical practice':'Draft practice'}</Badge><p>{task.prompt}</p></div><div className="inline-actions">{task.exercise_ids.length>0&&<Button pending={busy} onClick={()=>void create(task.id,true)}>Try checked typing</Button>}<Button variant="secondary" pending={busy} onClick={()=>void create(task.id)}>Start an unassessed draft</Button></div></article>):<p>No published writing tasks yet. Enable draft tasks to inspect the beginner references while review is pending.</p>}</section><section className="saved-drafts"><h2>Your saved drafts</h2>{catalog.drafts.length?catalog.drafts.map(draft=><article key={draft.id}><div><h3>{draft.title}</h3><p className="small">Content {draft.content_version} · draft {draft.id.slice(0,8)}</p></div><a className="button secondary" href={'#writing/'+draft.id}>Open saved draft</a></article>):<p>No saved drafts yet. Choose a task to start; autosaves keep your text without grading it.</p>}{catalog.has_more&&<div className="inline-actions"><Button variant="quiet" onClick={()=>setLimit(value=>value+20)}>Show more drafts</Button><Button variant="quiet" onClick={()=>setLimit(10000)}>Show all drafts</Button></div>}</section></>}</>
}

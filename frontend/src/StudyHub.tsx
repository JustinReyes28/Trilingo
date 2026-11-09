import { useEffect, useRef, useState } from 'react'
import { request } from './api'
import { Badge, Button, Card, FeedbackPanel } from './components'
import { commitStudy, pendingStudies, startStudy } from './studyApi'
import { AssessmentsSchema, MistakesSchema, ProgressSchema, type Assessment, type Progress } from './studySchemas'

export function StudyHub({courseId,progress,batch,onOpen}:{courseId:string;progress:Progress;batch:number;onOpen:(id:string)=>void}){
 const [assessmentMode,setAssessmentMode]=useState<'supported'|'unassisted'>('supported')
 const [assessments,setAssessments]=useState<Assessment[]>([])
 const [mistakes,setMistakes]=useState<ReturnType<typeof MistakesSchema.parse>>([])
 const [moreSessions,setMoreSessions]=useState<Progress['sessions']>([])
 const [hasMore,setHasMore]=useState(progress.has_more)
 const [error,setError]=useState('')
 const [busy,setBusy]=useState(false)
 const [retry,setRetry]=useState(0)
 const requestKey=courseId+':'+batch+':'+retry
 const [loadedKey,setLoadedKey]=useState('')
 const loading=loadedKey!==requestKey
 const [moreMistakes,setMoreMistakes]=useState(true)
 const keys=useRef(new Map<string,string>())
 const lock=useRef(false)
 useEffect(()=>{let active=true;Promise.all([request('/courses/'+courseId+'/assessments',AssessmentsSchema),request('/courses/'+courseId+'/mistakes?limit='+batch,MistakesSchema)]).then(([banks,items])=>{if(active){setAssessments(banks);setMistakes(items);setMoreMistakes(items.length>=batch);setLoadedKey(requestKey);setError('')}}).catch((err:unknown)=>{if(active){setLoadedKey(requestKey);setError(err instanceof Error?err.message:'Could not open practice. Retry.')}});return()=>{active=false}},[courseId,batch,retry,requestKey])
 useEffect(()=>{if(!loading&&new URLSearchParams(location.hash.split('?')[1]??'').get('section')==='mistakes'){const target=document.getElementById('practice-mistakes-heading');target?.focus();target?.scrollIntoView({block:'start'})}},[loading])
 async function begin(source:string,kind:string,draft=false){
  if(lock.current)return
  lock.current=true;setBusy(true);setError('')
  const cacheKey=source+':'+kind+':'+draft+':'+assessmentMode;const key=keys.current.get(cacheKey)??crypto.randomUUID();keys.current.set(cacheKey,key)
  try{const value=await startStudy(courseId,source,key,kind,draft,kind==='assessment'?assessmentMode:'supported');keys.current.delete(cacheKey);onOpen(value.id)}catch(err){setError(err instanceof Error?err.message:'Could not start. Retry.')}finally{lock.current=false;setBusy(false)}
 }
 async function recover(){const pending=pendingStudies()[0];if(!pending||lock.current)return;lock.current=true;setBusy(true);try{const saved=await commitStudy(pending);onOpen(saved.id)}catch(err){setError(err instanceof Error?err.message:'Could not confirm the action.')}finally{lock.current=false;setBusy(false)}}
 async function showMore(){setBusy(true);try{const next=await request('/progress?offset='+(progress.sessions.length+moreSessions.length),ProgressSchema);setMoreSessions(old=>[...old,...next.sessions]);setHasMore(next.has_more)}catch(err){setError(err instanceof Error?err.message:'Could not load more sessions.')}finally{setBusy(false)}}
 async function showMoreMistakes(){setBusy(true);try{const next=await request('/courses/'+courseId+'/mistakes?offset='+mistakes.length+'&limit='+batch,MistakesSchema);setMistakes(old=>[...old,...next]);setMoreMistakes(next.length>=batch)}catch(err){setError(err instanceof Error?err.message:'Could not load more mistakes.')}finally{setBusy(false)}}
 const sessions=[...new Map([...progress.sessions,...moreSessions].map(item=>[item.id,item])).values()]
 return <div className="study-hub">{error&&<FeedbackPanel kind="error">{error}<Button variant="secondary" onClick={()=>setRetry(old=>old+1)}>Retry practice list</Button></FeedbackPanel>}
 {pendingStudies().length>0&&<Card><h2>Confirm an interrupted action</h2><p>A study request is waiting for its saved receipt. Retrying uses the same action ID.</p><Button pending={busy} onClick={()=>void recover()}>Confirm pending action</Button></Card>}
 <section><h2>Continue your own trail</h2>{sessions.length?<ul className="session-list">{sessions.map(item=><li key={item.id}><div><strong>{item.title}</strong><small>{item.status} · {item.kind} · {new Date(item.created_at).toLocaleDateString()}</small></div><Button variant="secondary" onClick={()=>onOpen(item.id)}>{item.status==='completed'?'View saved session':'Resume session'}</Button></li>)}</ul>:<p>No sessions yet. Choose any published lesson from Learn.</p>}{hasMore&&<Button pending={busy} variant="quiet" onClick={()=>void showMore()}>Show more sessions</Button>}</section>
 <section><h2 id="practice-mistakes-heading" tabIndex={-1}>Mistakes you can revisit</h2>{loading?<p role="status">Loading your saved mistakes…</p>:error?null:mistakes.length?<><p>Mistakes stay available for voluntary practice. You can also choose any lesson.</p><Button pending={busy} onClick={()=>void begin('mistakes','mistakes')}>Practice available mistakes</Button><ul className="mistake-list">{mistakes.map(item=><li key={item.exercise_id}>{item.prompt}<a href={'#grammar?concept='+encodeURIComponent(item.concepts[0]??'')}>Read the related grammar</a><small>{item.skill} · {item.occurrences} incorrect responses recorded</small></li>)}</ul>{moreMistakes&&<Button variant="quiet" pending={busy} onClick={()=>void showMoreMistakes()}>Show more mistakes</Button>}</>:<p>No incorrect responses recorded yet. Skips and assisted answers are separate evidence.</p>}</section>
 <section><h2>Optional self-checks</h2><div className="answer-input"><label htmlFor="assessment-support">Self-check support</label><select id="assessment-support" disabled={busy} value={assessmentMode} onChange={event=>setAssessmentMode(event.target.value==='unassisted'?'unassisted':'supported')}><option value="supported">Supported practice</option><option value="unassisted">Unassisted check · hints remain available</option></select></div><p>Recaps, placement and mastery checks never control access. Draft comparisons remain practice.</p>{loading?<p role="status">Loading available self-checks…</p>:error?null:assessments.length?assessments.map(bank=><article className="assessment-row" key={bank.id}><div><h3>{bank.title}</h3><Badge tone="plum">{bank.status==='published'?'Available':'Draft practice'} · {bank.kind}</Badge><p className="small">{bank.scoring_policy}</p></div><Button variant="secondary" pending={busy} onClick={()=>void begin(bank.id,'assessment',bank.status!=='published')}>{bank.status==='published'?'Start self-check':'Try draft self-check'}</Button></article>):<p>No self-checks in this course yet.</p>}</section>
 </div>
}

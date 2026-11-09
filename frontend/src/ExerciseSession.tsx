import { z } from 'zod'
import { useEffect, useRef, useState } from 'react'
import { StudyTimer } from './StudyTimer'
import { Explanation } from './Explanation'
import { KanaInputAid } from './KanaInputAid'
import { StoryReader } from './StoryReader'
import { SessionCompletion } from './SessionCompletion'
import { ArrowLeft } from 'lucide-react'
import type { TranscriptResult } from './Recorder'
import { ApiError, request } from './api'
import { Badge, Button, FeedbackPanel, ProgressBar } from './components'
import { answerReady, emptyAnswer, ExerciseRenderer } from './ExerciseRenderer'
import { clearPendingStudy, commitStudy, pendingStudy, startStudy, type PendingStudy } from './studyApi'
import { StudySchema, type Answer, type Study, type StudyAction } from './studySchemas'

export function ExerciseSession({sessionId,onExit,onChanged,onOpen}:{sessionId:string;onExit:()=>void;onChanged:()=>void;onOpen:(id:string)=>void}){
 const [session,setSession]=useState<Study|null>(null)
 const [drafts,setDrafts]=useState<Record<string,Answer>>({})
 const [error,setError]=useState('')
 const [busy,setBusy]=useState(false)
 const [operation,setOperation]=useState<PendingStudy|null>(null)
 const [composing,setComposing]=useState(false)
 const lock=useRef(false)
 const heading=useRef<HTMLHeadingElement>(null)
 const audioRequests=useRef(new Map<string,{request_id:string;expected_revision:number;speed:number}>())
 const replayKeys=useRef(new Map<string,string>())
 const actionPath='/sessions/'+sessionId+'/actions'
 useEffect(()=>{let active=true;async function load(){
  const stored=pendingStudy(actionPath)
  if(active)setOperation(stored)
  try{const value=stored?await commitStudy(stored):await request('/sessions/'+sessionId,StudySchema);if(active){setSession(value);setOperation(null);setError('')}}catch(err){if(active){setError(err instanceof Error?err.message:'Could not open this session.');try{const value=await request('/sessions/'+sessionId,StudySchema);if(active)setSession(value)}catch{/* The original recovery error is already visible. */}}}
 }void load();return()=>{active=false}},[sessionId,actionPath])
 useEffect(()=>{heading.current?.focus()},[session?.cursor])
 async function commit(op:PendingStudy,leave=false){
  if(lock.current)return false
  lock.current=true;setBusy(true);setError('');setOperation(op)
  try{const saved=await commitStudy(op);setSession(saved);audioRequests.current.clear();setOperation(null);if(saved.status==='completed'||leave)onChanged();if(leave)onExit();return true}
  catch(err){setError(err instanceof Error?err.message:'Could not save. Retry this action.');return false}finally{setBusy(false);lock.current=false}
 }
 function act(action:StudyAction,exerciseId?:string,answer?:Answer,leave=false,fields:Record<string,string>={}){
  if(!session||operation||lock.current||composing)return
  const body:Record<string,unknown>={request_id:session.next_action_id,expected_revision:session.revision,action,...fields}
  if(exerciseId!==undefined)body.exercise_id=exerciseId
  if(answer!==undefined)body.answer=answer
  void commit({path:actionPath,body},leave)
 }
 async function recordInputAid():Promise<boolean>{
  if(evidence?.assisted)return true
  if(!session||!exercise||operation||lock.current||composing)return false
  return commit({path:actionPath,body:{request_id:session.next_action_id,expected_revision:session.revision,action:'hint',exercise_id:exercise.id}})
 }
 async function prepareAudio(cueId:string,speed:number):Promise<string>{
  if(!session||!exercise||lock.current||operation)throw new Error('Wait for the saved action or reload the session.')
  const key=exercise.id+':'+cueId+':'+speed
  const body=audioRequests.current.get(key)??{request_id:crypto.randomUUID(),expected_revision:session.revision,speed}
  audioRequests.current.set(key,body);lock.current=true;setBusy(true)
  try{const saved=await request('/sessions/'+session.id+'/exercises/'+exercise.id+'/audio/'+cueId,z.object({audio_base64:z.string(),session:StudySchema}),{method:'POST',body:JSON.stringify(body)});setSession(saved.session);audioRequests.current.delete(key);setError('');const bytes=Uint8Array.from(atob(saved.audio_base64),c=>c.charCodeAt(0));return URL.createObjectURL(new Blob([bytes],{type:'audio/wav'}))}catch(err){if(err instanceof ApiError&&['stale_revision','request_conflict','completed'].includes(err.code))setError(err.message);throw err}finally{setBusy(false);lock.current=false}
 }
 async function saveSpeech(encoded:string):Promise<TranscriptResult>{
  if(!session||!exercise||exercise.type!=='speaking'||lock.current||operation)throw new Error('Wait for the saved action or reload this session.')
  lock.current=true;setBusy(true)
  try{
   const saved=await request('/sessions/'+session.id+'/exercises/'+exercise.id+'/speech',StudySchema,{method:'POST',body:JSON.stringify({request_id:session.next_action_id,expected_revision:session.revision,audio_base64:encoded})})
   setSession(saved);audioRequests.current.clear();setError('')
   const item=saved.evidence[exercise.id]
   return {text:item.last_transcript??'',target:exercise.reference_text,agrees:item.last_transcript_matches===true,label:saved.feedback?.explanation??'Transcript comparison only; pronunciation is not assessed.'}
  }catch(err){if(err instanceof ApiError&&['stale_revision','request_conflict','completed','provider_changed'].includes(err.code))setError(err.message);throw err}finally{setBusy(false);lock.current=false}
 }
 async function reload(){
  if(lock.current)return
  setBusy(true)
  try{const saved=await request('/sessions/'+sessionId,StudySchema);setSession(saved);audioRequests.current.clear();if(operation)clearPendingStudy(operation.body.request_id);setOperation(null);setError('')}
  catch(err){setError(err instanceof Error?err.message:'Could not reload. Retry when connected.')}finally{setBusy(false)}
 }
 async function replay(sourceId?:string,sourceKind?:string){
  if(!session||lock.current)return
  lock.current=true;setBusy(true)
  try{const source=sourceId??session.source_id;const kind=sourceKind??session.source_kind;const key=source+':'+kind;const id=replayKeys.current.get(key)??crypto.randomUUID();replayKeys.current.set(key,id);const value=await startStudy(session.course_id,source,id,kind,kind==='lesson'?false:session.preview_draft);onChanged();onOpen(value.id)}catch(err){setError(err instanceof Error?err.message:'Could not start the replay. Retry.')}finally{lock.current=false;setBusy(false)}
 }
 const currentExercise=session?.exercises[session.cursor]
 const exercise=session?.story&&!session.story.current.exercise_ids.includes(currentExercise?.id??'')?undefined:currentExercise
 const value=exercise?(drafts[exercise.id]??session?.evidence[exercise.id]?.answer??emptyAnswer(exercise)):''
 const evidence=exercise?session?.evidence[exercise.id]:undefined
 const feedback=session?.feedback?.exercise_id===exercise?.id?session?.feedback:null
 const edited=Boolean(exercise&&drafts[exercise.id]!==undefined&&!answersEqual(value,evidence?.answer??emptyAnswer(exercise)))
 const blocked=busy||Boolean(operation)
 return <section className="study-workspace" aria-label="Lesson study"><div className="study-top"><a href="#learn"><ArrowLeft size={18} aria-hidden="true"/>Course path</a>{session&&session.status!=='completed'&&<Button variant="quiet" disabled={Boolean(operation)} pending={busy} onClick={()=>act('pause',undefined,undefined,true)}>Pause and leave</Button>}</div>
 {error&&<FeedbackPanel kind="error">{error}<div className="inline-actions">{operation&&<Button pending={busy} onClick={()=>void commit(operation)}>Retry saved action</Button>}<Button variant="secondary" pending={busy} onClick={()=>void reload()}>Reload saved session</Button></div><p className="small">Your current input stays on this screen. Other lessons remain available from the course path.</p></FeedbackPanel>}
 {!session?<p role="status">{error?'Use Reload saved session to try opening this session again.':'Opening your saved session…'}</p>:<><div className="study-heading"><h1>{session.title}</h1><Badge tone="plum">{session.preview_draft?'Draft practice':'Technical practice'} · Japanese review pending</Badge></div>
 {session.status==='completed'?<SessionCompletion session={session} busy={busy} heading={heading} onReplay={(sourceId,sourceKind)=>void replay(sourceId,sourceKind)} onExit={onExit}/>:<>
 <StudyTimer session={session} blocked={blocked} onAct={action=>act(action)}/>
 {session.story&&<StoryReader session={session} blocked={blocked} onAct={(action,fields)=>act(action,undefined,undefined,false,fields)}/>}
 {!session.story&&<ProgressBar value={Object.values(session.evidence).filter(item=>item.responses||item.revealed||item.skipped).length} max={session.exercises.length} label="Prompts studied or explicitly skipped"/>}
 {session.status==='paused'&&<FeedbackPanel kind="info">This session is paused. Continue whenever you like.<Button disabled={blocked} onClick={()=>act('resume')}>Resume study</Button></FeedbackPanel>}
 {exercise?<div className="question-frame"><div className="question-meta"><span>Prompt {session.cursor+1} of {session.exercises.length}</span><span>{exercise.type==='speaking'?'Speaking practice':exercise.skill+' · '+exercise.type.replaceAll('_',' ')}</span></div><h2 ref={heading} tabIndex={-1}>{exercise.prompt}</h2>{exercise.objective!==exercise.prompt&&<p className="small">{exercise.objective}</p>}<form onSubmit={event=>{event.preventDefault();if(!composing&&answerReady(exercise,value))act('answer',exercise.id,value)}}>
 <ExerciseRenderer key={exercise.id} onAudio={prepareAudio} onSpeech={saveSpeech} onTextAlternative={()=>act('audio_text',exercise.id)} exercise={exercise} value={value} onChange={answer=>setDrafts(old=>({...old,[exercise.id]:answer}))} disabled={blocked} onComposition={setComposing}/>
 {(exercise.type==='translation'||exercise.type==='fill_blank')&&typeof value==='string'&&<KanaInputAid key={exercise.id} courseId={session.course_id} disabled={blocked||composing} onUse={recordInputAid} onInsert={text=>setDrafts(old=>({...old,[exercise.id]:value+text}))}/>}
 {feedback&&<FeedbackPanel kind={edited?'info':feedback.kind==='correct'?'success':feedback.kind==='incorrect'?'error':'info'}><strong>{edited?'Previous saved result: ':''}{{correct:'Correct',incorrect:'Not yet',hint:'Hint',reveal:'Answer revealed',skipped:'Skipped',recorded:'Practice recorded'}[feedback.kind]}</strong><p>{feedback.message}</p>{feedback.answer!==null&&<p className="revealed-answer" lang="ja">{formatAnswer(exercise,feedback.answer)}</p>}{feedback.explanation&&<><p>{feedback.explanation}</p><Explanation key={exercise.id} sessionId={sessionId} exerciseId={exercise.id}/></>}</FeedbackPanel>}
 {evidence&&<p className="small" role="status">{evidence.assisted?'Assisted practice. ':''}{evidence.responses>1?(exercise.type==='speaking'?'Additional practice attempt recorded. ':'Correction recorded; the initial result is retained. '):''}{evidence.skipped?'Explicit skip recorded. ':''}{evidence.responses?(edited?'Previously saved answers: ':'Answers saved: ')+evidence.responses:''}</p>}
 {edited&&<p className="small" role="status">Changes are not saved. Use the save or check button when ready.</p>}
 {exercise.type==='speaking'&&evidence&&<div className="speech-evidence" role="status"><p>{evidence.speech_attempts} saved speech attempts · {evidence.transcript_matches} transcript agreements · {evidence.typed_fallbacks} typed fallbacks</p>{evidence.last_transcript&&<><p>Last recognized text: <span lang="ja">{evidence.last_transcript}</span></p><p className="small">Transcript comparison only. Pronunciation and pitch accent are not assessed.</p></>}</div>}
  <div className="study-actions"><Button type="submit" pending={busy} pendingLabel={exercise.type==='speaking'?'Saving…':'Checking…'} disabled={blocked||composing||!answerReady(exercise,value)}>{exercise.type==='speaking'?'Save typed practice':'Check answer'}</Button>{(evidence?.responses||evidence?.revealed||evidence?.skipped)?<Button type="button" variant="secondary" disabled={blocked} onClick={()=>act('continue',exercise.id)}>Continue</Button>:null}<Button type="button" variant="quiet" disabled={blocked} onClick={()=>act('skip',exercise.id)}>Skip prompt</Button></div></form>
 <div className="assistance-actions">{session.mode==='unassisted'&&<><p className="small">Unassisted check. You can switch whenever you wish.</p><Button variant="secondary" disabled={blocked} onClick={()=>act('support')}>Use supported practice</Button></>}<Button variant="quiet" disabled={blocked} onClick={()=>act('hint',exercise.id)}>Show hint</Button><Button variant="quiet" disabled={blocked} onClick={()=>act('reveal',exercise.id)}>{exercise.type==='speaking'?'Show model explanation':'Reveal answer & explanation'}</Button></div></div>:session.story?<p className="small">{session.story.current.exercise_ids.length?'This turn’s checkpoint has been visited. Reopen it below or continue the story.':'No checkpoint on this turn. Continue or finish whenever you wish.'}</p>:session.source_kind==='review'?<div className="question-frame"><h2>Optional recall timer</h2><p>A recall rating saves this workflow. You can pause or leave without changing its schedule.</p><a className="button secondary" href={'#review?session='+session.id}>Return to this recall card</a></div>:<div className="question-frame"><h2 ref={heading} tabIndex={-1}>Ready to finish?</h2><p>You can finish with mistakes, assisted answers or skips. Revisit any prompt below if you wish.</p><Button disabled={blocked} pending={busy} onClick={()=>act('finish')}>Finish and save session</Button></div>}
 <nav className="prompt-navigation" aria-label="Choose a prompt">{session.exercises.map((item,index)=>(!session.story||session.story.current.exercise_ids.includes(item.id))&&<Button key={item.id} variant={index===session.cursor?'primary':'quiet'} disabled={blocked} aria-label={'Open prompt '+(index+1)} aria-current={index===session.cursor?'step':undefined} onClick={()=>act('visit',item.id)}>{index+1}</Button>)}</nav><p className="small">No countdown or pass score. Retry, skip, reveal, replay or choose another lesson at any time.</p></>}
 </>}
 </section>
}
function formatAnswer(exercise:Study['exercises'][number],answer:Answer):string{
 if((exercise.type==='multiple_choice'||exercise.type==='response_selection'||exercise.type==='listening_selection'||exercise.type==='audio_contrast')&&typeof answer==='string')return exercise.choices.find(choice=>choice.id===answer)?.text??answer
 if(exercise.type==='sentence_ordering'&&Array.isArray(answer))return answer.map(id=>exercise.tokens.find(token=>token.id===id)?.text??id).join('')
 if(exercise.type==='matching'&&typeof answer==='object'&&!Array.isArray(answer))return Object.entries(answer).map(([left,right])=>(exercise.left.find(item=>item.id===left)?.text??left)+' → '+(exercise.right.find(item=>item.id===right)?.text??right)).join(' · ')
 return typeof answer==='string'?answer:Array.isArray(answer)?answer.join(' / '):Object.values(answer).join(' / ')
}

function answersEqual(left:Answer,right:Answer):boolean{
 const canonical=(value:Answer)=>typeof value==='object'&&!Array.isArray(value)?Object.entries(value).sort(([a],[b])=>a.localeCompare(b)):value
 return JSON.stringify(canonical(left))===JSON.stringify(canonical(right))
}

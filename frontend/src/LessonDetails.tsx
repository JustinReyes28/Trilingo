import { useEffect, useRef, useState } from 'react'
import { BookOpen } from 'lucide-react'
import { request } from './api'
import { LessonSchema, type Lesson } from './schemas'
import { Badge, Button, Dialog, FeedbackPanel } from './components'
import { startStudy } from './studyApi'

export function LessonDetails({courseId,lessonId,onClose,onStart}:{courseId:string;lessonId:string;onClose:()=>void;onStart:(id:string)=>void}){
 const [lesson,setLesson]=useState<Lesson|null>(null)
 const [error,setError]=useState('')
 const [revision,setRevision]=useState(0)
 const [busy,setBusy]=useState(false)
 const startKey=useRef(crypto.randomUUID())
 const lock=useRef(false)
 async function start(){if(lock.current)return;lock.current=true;setBusy(true);try{const value=await startStudy(courseId,lessonId,startKey.current);onStart(value.id)}catch(err){setError(err instanceof Error?err.message:'Could not start this lesson. Retry.')}finally{lock.current=false;setBusy(false)}}
 useEffect(()=>{let active=true;request('/courses/'+courseId+'/lessons/'+lessonId,LessonSchema).then(value=>{if(active)setLesson(value)}).catch((err:unknown)=>{if(active)setError(err instanceof Error?err.message:'Could not open this lesson.')});return()=>{active=false}},[courseId,lessonId,revision])
 return <Dialog title={lesson?.title??'Opening lesson'} onClose={onClose}>{error?<><FeedbackPanel kind="error">{error}</FeedbackPanel><Button onClick={()=>{setError('');setRevision(r=>r+1)}}>Retry</Button></>:!lesson?<p role="status">Loading the lesson outline…</p>:<><span lang="ja" className="dialog-japanese">{lesson.japanese_title}</span><Badge tone="mint">Published · Technical practice</Badge><h3>What you’ll work on</h3><p>{lesson.objective}</p><p><BookOpen size={18} aria-hidden="true"/> {lesson.exercises.length} short exercises in this lesson</p><ol className="lesson-objectives">{lesson.exercises.map(exercise=><li key={exercise.id}>{exercise.prompt}<small>{exercise.type.replaceAll('_',' ')} · {exercise.skill}</small></li>)}</ol><FeedbackPanel kind="info">Practice content; independent Japanese review is pending. Answers, skips and assistance are saved separately.</FeedbackPanel><Button pending={busy} pendingLabel="Opening…" onClick={()=>void start()}>Start lesson</Button><Button variant="quiet" onClick={onClose}>Choose another lesson</Button></>}</Dialog>
}

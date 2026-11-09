import { useEffect, useState } from 'react'
import type { Study, StudyAction } from './studySchemas'
import { Button } from './components'
export function StudyTimer({session,blocked,onAct}:{session:Study;blocked:boolean;onAct:(action:StudyAction)=>void}){
 const timer=session.timer
 const [seconds,setSeconds]=useState(timer?.elapsed_seconds??0)
 useEffect(()=>{setSeconds(timer?.elapsed_seconds??0);if(!timer?.running)return;const started=performance.now();const interval=setInterval(()=>setSeconds(timer.elapsed_seconds+(performance.now()-started)/1000),1000);return()=>clearInterval(interval)},[timer])
 if(!timer)return <Button variant="quiet" disabled={blocked} onClick={()=>onAct('timer_start')}>Show optional elapsed time</Button>
 if(!timer.visible)return <Button variant="quiet" disabled={blocked} onClick={()=>onAct('timer_show')}>Show elapsed time</Button>
 return <div className="study-timer"><span>Active time: {Math.floor(seconds/60)}m {Math.floor(seconds%60)}s · {timer.running?'running':'paused'}</span>{!timer.valid&&<p>Clock changed; this timing record is omitted. Your learning is still saved.</p>}<div className="inline-actions"><Button variant="quiet" disabled={blocked} onClick={()=>onAct(timer.running?'timer_pause':'timer_resume')}>{timer.running?'Pause elapsed time':'Resume elapsed time'}</Button><Button variant="quiet" disabled={blocked} onClick={()=>onAct('timer_hide')}>Hide elapsed time</Button></div><p className="small">Elapsed time is optional. This activity never expires.</p></div>
}

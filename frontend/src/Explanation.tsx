import { useState } from 'react'
import { request } from './api'
import { ExplanationSchema } from './practiceSchemas'
import { Button, FeedbackPanel } from './components'
import type { z } from 'zod'
export function Explanation({sessionId,exerciseId}:{sessionId:string;exerciseId:string}){
 const [value,setValue]=useState<z.infer<typeof ExplanationSchema>|null>(null),[busy,setBusy]=useState(false),[error,setError]=useState('')
 async function elaborate(){setBusy(true);setError('');try{setValue(await request('/explanations',ExplanationSchema,{method:'POST',body:JSON.stringify({session_id:sessionId,exercise_id:exerciseId})}))}catch(e){setError(e instanceof Error?e.message:'Explanation unavailable. The authored explanation remains above.')}finally{setBusy(false)}}
 return <div><Button type="button" variant="quiet" pending={busy} onClick={()=>void elaborate()}>Optional local AI elaboration</Button>{value&&<><p className="small">{value.status}</p><p>{value.generated??value.authored}</p></>}{error&&<FeedbackPanel kind="error">{error}</FeedbackPanel>}</div>
}

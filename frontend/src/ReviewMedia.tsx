import { useEffect, useRef, useState } from 'react'
import { request } from './api'
import { AudioSchema, type ReviewCard } from './practiceSchemas'
import { ListeningCues, type PreparedAudio } from './ListeningExercise'

export function ReviewMedia({card,disabled,onReveal}:{card:ReviewCard;disabled:boolean;onReveal:()=>void}){
 const [preparing,setPreparing]=useState(false)
 const controller=useRef<AbortController|null>(null)
 useEffect(()=>{controller.current=new AbortController();return()=>controller.current?.abort()},[])
 async function prepare(cueId:string,speed:number):Promise<PreparedAudio>{
  setPreparing(true)
  try{const audio=await request('/review/cards/'+card.id+'/audio/'+cueId,AudioSchema,{method:'POST',body:JSON.stringify({speed}),signal:controller.current?.signal});if(controller.current?.signal.aborted)throw new Error('Recall card changed.');const bytes=Uint8Array.from(atob(audio.audio_base64),c=>c.charCodeAt(0));return {url:URL.createObjectURL(new Blob([bytes],{type:audio.mime})),label:audio.label}}finally{setPreparing(false)}
 }
 if(!card.audio_cues.length)return null
 return <section className="recall-media" aria-label="Saved card audio">{preparing&&<p role="status">Preparing your saved reference…</p>}<p className="small">Use your saved reference, or reveal text. Preparing audio does not change the schedule. Again/Hard/Good/Easy remains an intentional self-rating.</p><ListeningCues cues={card.audio_cues} disabled={disabled||preparing} onAudio={prepare} onTextAlternative={onReveal}/></section>
}

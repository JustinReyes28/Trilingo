import { useState } from 'react'
import type { Answer, Exercise } from './studySchemas'
import { ListeningCues, type AudioPreparer } from './ListeningExercise'
import { Recorder, type TranscriptResult } from './Recorder'

type Props={exercise:Extract<Exercise,{type:'speaking'}>;value:Answer;onChange:(value:Answer)=>void;disabled:boolean;onComposition:(active:boolean)=>void;onAudio?:AudioPreparer;onTextAlternative?:()=>void;onSpeech?:(encoded:string)=>Promise<TranscriptResult>}
export function SpeakingExercise({exercise,value,onChange,disabled,onComposition,onAudio,onTextAlternative,onSpeech}:Props){
 const [typing,setTyping]=useState(false)
 return <div className="speaking-practice"><div className="speaking-model"><span className="eyebrow">Say it in Japanese</span><p lang="ja" className="dialog-japanese">{exercise.reference_text}</p><p className="small">An authored model for practice. You can repeat it, retry, type instead or skip.</p></div><ListeningCues cues={exercise.audio} disabled={disabled} onAudio={onAudio} onTextAlternative={()=>{setTyping(true);onTextAlternative?.()}}/><Recorder durable disabled={disabled} saveLabel="Send and save transcript feedback" onSend={async encoded=>{if(!onSpeech)throw new Error('Saved speech feedback is unavailable here. Use typed practice.');return onSpeech(encoded)}}/><details open={typing} onToggle={event=>setTyping(event.currentTarget.open)}><summary>Use typed fallback</summary><label htmlFor={'answer-'+exercise.id}>Typed practice · no speech assessed</label><textarea id={'answer-'+exercise.id} lang="ja" rows={2} maxLength={8192} disabled={disabled} value={typeof value==='string'?value:''} onChange={e=>onChange(e.target.value)} onCompositionStart={()=>onComposition(true)} onCompositionEnd={()=>onComposition(false)}/><p className="small">Confirm IME conversion first, then use Save typed practice. This saves a text response without speaking credit.</p></details></div>
}

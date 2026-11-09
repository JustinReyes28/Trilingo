import { useEffect, useRef, useState } from 'react'
import { Button, FeedbackPanel } from './components'

type Cue={id:string;label:string}
export function ListeningCues({cues,disabled,onAudio,onTextAlternative}:{cues:Cue[];disabled:boolean;onAudio?:(cueId:string,speed:number)=>Promise<string>;onTextAlternative?:()=>void}){
 const [urls,setUrls]=useState<Record<string,string>>({}),[error,setError]=useState(''),[slow,setSlow]=useState(false),[loop,setLoop]=useState(false)
 const owned=useRef(new Set<string>())
 const mounted=useRef(true)
 useEffect(()=>{mounted.current=true;const urls=owned.current;return()=>{mounted.current=false;urls.forEach(url=>URL.revokeObjectURL(url));urls.clear()}},[])
 async function prepare(id:string){setError('');try{if(!onAudio)throw new Error('Audio is unavailable here. Use the text alternative.');const url=await onAudio(id,slow?0.75:1);if(!mounted.current){URL.revokeObjectURL(url);return}owned.current.add(url);setUrls(old=>{if(old[id]){URL.revokeObjectURL(old[id]);owned.current.delete(old[id])}return {...old,[id]:url}})}catch(e){setError(e instanceof Error?e.message:'Audio unavailable. Use the text alternative.')}}
 return <section className="listening-cues" aria-label="Listening references"><p className="small">Replay freely, or use text assistance.</p><label className="check-row"><input type="checkbox" checked={slow} disabled={disabled} onChange={e=>setSlow(e.target.checked)}/>Prepare slow reference</label>{cues.map(cue=><div key={cue.id} className="audio-controls"><Button type="button" variant="secondary" disabled={disabled} onClick={()=>void prepare(cue.id)}>Prepare {cue.label}</Button>{urls[cue.id]&&<audio aria-label={cue.label} controls src={urls[cue.id]} loop={loop}/>}</div>)}<label className="check-row"><input type="checkbox" checked={loop} onChange={e=>setLoop(e.target.checked)}/>Loop reference</label><Button type="button" variant="quiet" disabled={disabled} onClick={onTextAlternative}>Use text alternative</Button><details><summary>About this reference</summary><p className="small">Synthetic reference · human Japanese listening review pending. Preparing audio records delivery, not proof of hearing it. Text-assisted checks are recorded separately.</p></details>{error&&<FeedbackPanel kind="error">{error}</FeedbackPanel>}</section>
}

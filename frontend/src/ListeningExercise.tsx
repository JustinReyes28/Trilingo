import { useEffect, useRef, useState } from 'react'
import { Button, FeedbackPanel } from './components'

type Cue={id:string;label:string}
export type PreparedAudio={url:string;label?:string}
export type AudioPreparer=(cueId:string,speed:number)=>Promise<PreparedAudio>

export function playbackRate(slow:boolean):number{
 return slow?0.75:1
}

export function ListeningCues({cues,disabled,onAudio,onTextAlternative}:{cues:Cue[];disabled:boolean;onAudio?:AudioPreparer;onTextAlternative?:()=>void}){
 const [urls,setUrls]=useState<Record<string,PreparedAudio>>({}),[error,setError]=useState(''),[slow,setSlow]=useState(false),[loop,setLoop]=useState(false)
 const owned=useRef(new Set<string>())
 const mounted=useRef(true)
 const players=useRef(new Map<string,HTMLAudioElement>())
 useEffect(()=>{mounted.current=true;const urls=owned.current;const playerMap=players.current;return()=>{mounted.current=false;urls.forEach(url=>URL.revokeObjectURL(url));urls.clear();playerMap.clear()}},[])
 useEffect(()=>{players.current.forEach(player=>{player.preservesPitch=true;player.playbackRate=playbackRate(slow)})},[slow,urls])
 async function prepare(id:string){
  setError('')
  try{
   if(!onAudio)throw new Error('Audio is unavailable here. Use the text alternative.')
   const prepared=await onAudio(id,slow?0.75:1)
   if(!mounted.current){URL.revokeObjectURL(prepared.url);return}
   owned.current.add(prepared.url)
   setUrls(old=>{if(old[id]){URL.revokeObjectURL(old[id].url);owned.current.delete(old[id].url)}return {...old,[id]:prepared}})
  }catch(e){setError(e instanceof Error?e.message:'Audio unavailable. Use the text alternative.')}
 }
 const preparedLabels=Array.from(new Set(cues.map(cue=>urls[cue.id]?.label).filter((label):label is string=>Boolean(label))))
 return <section className="listening-cues" aria-label="Listening references"><p className="small">Replay freely, or use text assistance.</p><label className="check-row"><input type="checkbox" checked={slow} disabled={disabled} onChange={e=>setSlow(e.target.checked)}/>Slow reference</label>{cues.map(cue=>{const prepared=urls[cue.id];return <div key={cue.id} className="audio-controls"><Button type="button" variant="secondary" disabled={disabled} onClick={()=>void prepare(cue.id)}>Prepare {cue.label}</Button>{prepared&&<><audio ref={player=>{if(player)players.current.set(cue.id,player);else players.current.delete(cue.id)}} aria-label={cue.label} controls src={prepared.url} loop={loop} onLoadedMetadata={event=>{const player=event.currentTarget;player.preservesPitch=true;player.playbackRate=playbackRate(slow)}}/>{prepared.label&&<p className="small">{prepared.label}</p>}</>}</div>})}<label className="check-row"><input type="checkbox" checked={loop} onChange={e=>setLoop(e.target.checked)}/>Loop reference</label><Button type="button" variant="quiet" disabled={disabled} onClick={onTextAlternative}>Use text alternative</Button><details><summary>About this reference</summary>{preparedLabels.length?<><p className="small">{preparedLabels.join(' · ')}</p><p className="small">Preparing audio records delivery, not proof of hearing it. Text-assisted checks are recorded separately.</p></>:<p className="small">Bundled reference audio · human Japanese listening review pending. Preparing audio records delivery, not proof of hearing it. Text-assisted checks are recorded separately.</p>}</details>{error&&<FeedbackPanel kind="error">{error}</FeedbackPanel>}</section>
}

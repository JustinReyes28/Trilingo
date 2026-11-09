import { useState } from 'react'
import { request } from './api'
import { Button, FeedbackPanel } from './components'
import { ReadingLibrarySchema, type Character } from './readingSchemas'
export function KanaInputAid({courseId,onInsert,disabled=false,onUse}:{courseId:string;onInsert:(text:string)=>void;disabled?:boolean;onUse?:()=>Promise<boolean>}){
 const [characters,setCharacters]=useState<Character[]|null>(null)
 const [script,setScript]=useState('hiragana')
 const [error,setError]=useState('')
 const [busy,setBusy]=useState(false)
 async function open(){setBusy(true);setError('');try{if(onUse&&!await onUse()){setError('Support was not saved. Retry opening the aid when the local service is ready.');return}const library=await request('/courses/'+courseId+'/reading?include_drafts=true',ReadingLibrarySchema);setCharacters(library.characters.filter(entry=>entry.form==='basic'||entry.form==='small'||entry.form==='voiced'||entry.form==='semi_voiced'||entry.form==='mark'))}catch(err){setError(err instanceof Error?err.message:'Could not open kana aid. Retry.')}finally{setBusy(false)}}
 async function insert(text:string){setBusy(true);try{if(!onUse||await onUse())onInsert(text);else setError('Support was not saved. Retry when the local service is ready.')}finally{setBusy(false)}}
 return <details className="kana-input-aid"><summary>On-screen kana input aid · draft reference</summary><p className="small">Insert Japanese characters without romaji. This is a draft aid; using it is support, not unaided typing evidence.</p>{!characters&&<Button variant="secondary" pending={busy} disabled={disabled} onClick={()=>void open()}>Load draft kana input aid</Button>}{error&&<FeedbackPanel kind="error">{error}</FeedbackPanel>}{characters&&<><label htmlFor="kana-aid-script">Input-aid script</label><select id="kana-aid-script" value={script} onChange={event=>setScript(event.target.value)}><option value="hiragana">Hiragana</option><option value="katakana">Katakana</option></select><div className="kana-input-grid">{characters.filter(entry=>entry.script===script).map(entry=><Button key={entry.id} variant="quiet" disabled={disabled||busy} lang="ja" aria-label={'Insert '+entry.surface} onClick={()=>void insert(entry.surface)}>{entry.surface}</Button>)}</div></>}</details>
}

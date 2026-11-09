import { useEffect, useState } from 'react'
import { z } from 'zod'
import { request } from './api'
import { Button } from './components'
const SuggestionSchema=z.object({destination:z.string(),title:z.string(),reason:z.string()})
const choices=[
 {kind:'mistakes',title:'Saved mistakes',text:'Revisit actual saved responses whenever useful.',href:'practice?section=mistakes'},
 {kind:'words',title:'Words in context',text:'Browse contextual entries and choose freely from saved vocabulary.',href:'reading?section=words'},
 {kind:'kana',title:'Kana',text:'Explore hiragana and katakana with optional reading aids.',href:'reading?section=characters'},
 {kind:'kanji',title:'Kanji',text:'Browse available character entries and labeled drafts.',href:'reading?section=characters&script=kanji'},
 {kind:'stories',title:'Stories',text:'Read original stories and inspect labeled drafts.',href:'reading?section=stories'},
 {kind:'writing',title:'Typing & writing',text:'Checked typing, composition drafts and optional formation.',href:'writing'},
 {kind:'grammar',title:'Grammar & dialogues',text:'Search authored patterns and try practical draft scenarios.',href:'grammar'},
 {kind:'listening',title:'Listening & shadowing',text:'Local reference audio and draft episodes. Real provider verification is pending.',href:'audio'},
 {kind:'speaking',title:'Speaking',text:'Local recording, playback and optional transcript comparison. No pronunciation score.',href:'audio'},
 {kind:'review',title:'Recall & personal quests',text:'Real FSRS, early review and optional records.',href:'review'},
] as const
export function PracticeChoices({courseId}:{courseId:string}){
 const [filter,setFilter]=useState('all'),[suggestion,setSuggestion]=useState<z.infer<typeof SuggestionSchema>|null>(null),[error,setError]=useState('')
 useEffect(()=>{let active=true;void request('/courses/'+courseId+'/practice-suggestion',SuggestionSchema).then(value=>{if(active)setSuggestion(value)}).catch(()=>{if(active)setError('Suggestion unavailable. Choose any practice mode below.')});return()=>{active=false}},[courseId])
 return <section className="practice-choices">{suggestion&&<div className="study-note"><div><h2>{suggestion.title}</h2><p>{suggestion.reason}</p><a className="button secondary" href={'#'+suggestion.destination}>Open suggestion</a></div></div>}{error&&<p role="status">{error}</p>}<h2>Choose your practice</h2><div className="inline-actions" role="group" aria-label="Filter practice modes">{['all','mistakes','words','kana','kanji','stories','writing','grammar','listening','speaking','review'].map(kind=><Button key={kind} variant={kind===filter?'primary':'quiet'} aria-pressed={kind===filter} onClick={()=>setFilter(kind)}>{kind==='all'?'All modes':kind[0].toUpperCase()+kind.slice(1)}</Button>)}</div><ul className="session-list">{choices.filter(choice=>filter==='all'||choice.kind===filter).map(choice=><li key={choice.title}><div><h3>{choice.title}</h3><p>{choice.text}</p></div><a className="button secondary" href={'#'+choice.href}>Open {choice.title.toLowerCase()}</a></li>)}</ul><p>Voluntary mistakes and saved sessions are below. Nothing here requires clearing a review queue.</p></section>
}

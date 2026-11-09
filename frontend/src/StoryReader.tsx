import { AudioControls } from './AudioPage'
import { useState } from 'react'
import { patch } from './api'
import { Button, FeedbackPanel } from './components'
import { JapaneseText } from './JapaneseText'
import { ReadingItemSchema } from './readingSchemas'
import type { Study, StudyAction } from './studySchemas'
export function StoryReader({session,blocked,onAct}:{session:Study;blocked:boolean;onAct:(action:StudyAction,fields?:Record<string,string>)=>void}){
 const [saved,setSaved]=useState<string[]>([])
 const [saving,setSaving]=useState<string|null>(null)
 const [error,setError]=useState('')
 const story=session.story
 if(!story)return null
 async function saveWord(id:string){if(saving)return;setSaving(id);setError('');try{await patch('/courses/'+session.course_id+'/reading/items/word/'+id,ReadingItemSchema,{saved:true,preview_draft:session.preview_draft});setSaved(old=>[...old,id])}catch(err){setError(err instanceof Error?err.message:'Could not save word. Retry.')}finally{setSaving(null)}}
 return <section className="story-reader" aria-label="Story turn"><div className="story-turn-meta"><strong>{story.current.speaker}</strong><span>Turn {story.turns.findIndex(turn=>turn.id===story.current.id)+1} of {story.turns.length}</span></div><p className="story-passage"><JapaneseText segments={story.current.text} furigana="always"/></p>
 <AudioControls key={story.current.id} reference={{course_id:session.course_id,item_id:session.source_id,turn_id:story.current.id,preview_draft:session.preview_draft}}/>
 {story.assisted_turn_ids.includes(story.current.id)&&<p className="small">Reading or glossary support used on this turn. Its checks remain assisted even after hiding support.</p>}
 <div className="inline-actions"><Button variant="secondary" disabled={blocked} onClick={()=>onAct(story.reading_aids?'hide_readings':'show_readings')}>{story.reading_aids?'Hide readings':'Show readings'}</Button><Button disabled={blocked||story.at_end} onClick={()=>onAct('story_continue')}>Continue story · skip unchecked prompts</Button></div>{story.at_end&&<p role="status">End of this story. Finish below, revisit any turn or keep practicing.</p>}
 <details><summary>Vocabulary help · records support</summary>{story.glossary.map(word=><div key={word.id} className="story-glossary"><Button variant="quiet" disabled={blocked} onClick={()=>onAct('glossary',{vocabulary_id:word.id})}>Explain {word.surface}</Button>{word.gloss&&<><p><span lang="ja">{word.surface}（{word.reading}）</span> · {word.gloss}</p><Button variant="secondary" pending={saving===word.id} disabled={Boolean(saving)||saved.includes(word.id)} onClick={()=>void saveWord(word.id)}>{saved.includes(word.id)?'Saved: ':'Save word: '}{word.surface}</Button></>}</div>)}</details>{error&&<FeedbackPanel kind="error">{error}</FeedbackPanel>}
 <nav aria-label="Choose a story turn" className="prompt-navigation">{story.turns.map((turn,index)=><Button key={turn.id} variant={turn.id===story.current.id?'primary':'quiet'} disabled={blocked} aria-current={turn.id===story.current.id?'step':undefined} onClick={()=>onAct('story_visit',{turn_id:turn.id})}>Turn {index+1}{story.visited_turn_ids.includes(turn.id)?' · Visited':''}</Button>)}</nav><p className="small">Jump freely. Finishing records all unchecked prompts as skipped, with no pass score.</p><Button variant="secondary" disabled={blocked} onClick={()=>onAct('finish')}>Finish story & save</Button>
 </section>
}

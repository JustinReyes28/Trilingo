import type { ReactElement } from 'react'
import { ArrowLeft, ArrowRight } from 'lucide-react'
import type { Answer, Exercise } from './studySchemas'
import { Button } from './components'
import { SpeakingExercise } from './SpeakingExercise'
import { ListeningCues, type AudioPreparer } from './ListeningExercise'

type Props={exercise:Exercise;value:Answer;onChange:(value:Answer)=>void;disabled:boolean;onComposition:(active:boolean)=>void;onAudio?:AudioPreparer;onTextAlternative?:()=>void}
export function emptyAnswer(exercise:Exercise):Answer{return exercise.type==='matching'?{}:exercise.type==='sentence_ordering'?[]:''}
export function answerReady(exercise:Exercise,value:Answer):boolean{
 switch(exercise.type){
  case 'multiple_choice':case 'response_selection':case 'listening_selection':case 'audio_contrast':return typeof value==='string'&&exercise.choices.some(choice=>choice.id===value)
  case 'speaking':case 'dictation':case 'translation':case 'fill_blank':case 'dialogue_completion':case 'constrained_roleplay':return typeof value==='string'&&value.trim().length>0
  case 'sentence_ordering':return Array.isArray(value)&&value.length===exercise.tokens.length&&new Set(value).size===value.length
  case 'matching':return typeof value==='object'&&!Array.isArray(value)&&exercise.left.every(choice=>Boolean(value[choice.id]))&&new Set(Object.values(value)).size===exercise.right.length
 }
}
export function ExerciseRenderer(props:Props):ReactElement{
 switch(props.exercise.type){
   case 'speaking':return <SpeakingExercise {...props} exercise={props.exercise}/>
  case 'listening_selection':case 'audio_contrast':case 'dictation':return <ListeningExercise {...props}/>
  case 'multiple_choice':case 'response_selection':return <ChoiceExercise {...props} exercise={props.exercise}/>
  case 'translation':case 'fill_blank':case 'dialogue_completion':case 'constrained_roleplay':return <TextExercise {...props}/>
  case 'sentence_ordering':return <OrderingExercise {...props} exercise={props.exercise}/>
  case 'matching':return <MatchingExercise {...props} exercise={props.exercise}/>
 }
}
function ChoiceExercise({exercise,value,onChange,disabled}:Props&{exercise:Extract<Exercise,{type:'multiple_choice'|'response_selection'|'listening_selection'|'audio_contrast'}>}){
 return <fieldset className="exercise-options" disabled={disabled}><legend>Choose one answer</legend>{exercise.choices.map(choice=><button type="button" key={choice.id} className={'answer-choice '+(value===choice.id?'selected':'')} aria-pressed={value===choice.id} onClick={()=>onChange(choice.id)}><span lang="ja">{choice.text}</span>{value===choice.id&&<small>Selected</small>}</button>)}</fieldset>
}
function TextExercise({exercise,value,onChange,disabled,onComposition}:Props){
 return <div className="answer-input"><label htmlFor={'answer-'+exercise.id}>Your answer</label><textarea id={'answer-'+exercise.id} aria-describedby={'answer-help-'+exercise.id} lang="ja" autoCapitalize="off" autoComplete="off" spellCheck={false} rows={2} maxLength={8192} value={typeof value==='string'?value:''} disabled={disabled} onChange={event=>onChange(event.target.value)} onCompositionStart={()=>onComposition(true)} onCompositionEnd={()=>onComposition(false)}/><small id={'answer-help-'+exercise.id}>Enter confirms an IME conversion or adds a line. Use Check answer when ready.</small></div>
}
function OrderingExercise({exercise,value,onChange,disabled}:Props&{exercise:Extract<Exercise,{type:'sentence_ordering'}>}){
 const ids=Array.isArray(value)?value:[]
 function move(index:number,delta:number){const next=[...ids];[next[index],next[index+delta]]=[next[index+delta],next[index]];onChange(next)}
 return <fieldset disabled={disabled}><legend>Build the expression</legend><p className="small">Add each part, then move or remove it with the buttons.</p><ol className="token-order">{ids.map((id,index)=><li key={id}><span lang="ja">{exercise.tokens.find(token=>token.id===id)?.text}</span><div className="inline-actions"><Button type="button" variant="quiet" disabled={index===0} aria-label={'Move part '+(index+1)+' earlier'} onClick={()=>move(index,-1)}><ArrowLeft size={18} aria-hidden="true"/></Button><Button type="button" variant="quiet" disabled={index===ids.length-1} aria-label={'Move part '+(index+1)+' later'} onClick={()=>move(index,1)}><ArrowRight size={18} aria-hidden="true"/></Button><Button type="button" variant="quiet" aria-label={'Remove part '+(index+1)} onClick={()=>onChange(ids.filter(key=>key!==id))}>Remove</Button></div></li>)}</ol><div className="token-bank">{exercise.tokens.map((token,index)=><Button type="button" variant="secondary" disabled={ids.includes(token.id)} key={token.id} aria-label={'Add part '+(index+1)+': '+token.text} onClick={()=>onChange([...ids,token.id])}><span lang="ja">{token.text}</span></Button>)}</div>{ids.length===0&&<p className="small">Your expression will appear here.</p>}</fieldset>
}
function MatchingExercise({exercise,value,onChange,disabled}:Props&{exercise:Extract<Exercise,{type:'matching'}>}){
 const pairs=typeof value==='object'&&!Array.isArray(value)?value:{}
 return <fieldset disabled={disabled}><legend>Match each item once</legend><div className="matching-options">{exercise.left.map(choice=><div key={choice.id}><label lang="ja" htmlFor={exercise.id+'-'+choice.id}>{choice.text}</label><select id={exercise.id+'-'+choice.id} value={pairs[choice.id]??''} onChange={event=>onChange({...pairs,[choice.id]:event.target.value})}><option value="">Choose a match</option>{exercise.right.map(right=><option key={right.id} value={right.id}>{right.text}</option>)}</select></div>)}</div><p className="small">Choose a different match for each row.</p></fieldset>
}

function ListeningExercise(props:Props){
 const exercise=props.exercise
 if(exercise.type!=='listening_selection'&&exercise.type!=='audio_contrast'&&exercise.type!=='dictation')throw new Error('Expected a listening prompt')
 return <><ListeningCues cues={exercise.audio} disabled={props.disabled} onAudio={props.onAudio} onTextAlternative={props.onTextAlternative}/>{exercise.type==='dictation'?<TextExercise {...props}/>:<ChoiceExercise {...props} exercise={exercise}/>}</>
}

import { Check, HelpCircle, Minus, ArrowRight, BookOpen } from 'lucide-react'

export type LessonState='suggested'|'available'|'current'|'visited'|'studied'|'assisted'|'skipped'|'unpublished'
const stateLabels:Record<LessonState,string>={suggested:'Suggested',available:'Available',current:'Current outline',visited:'Visited',studied:'Studied',assisted:'Assisted',skipped:'Skipped',unpublished:'Not published'}
export function LessonNode({title,japanese,number,state,onClick}:{title:string;japanese:string;number:number;state:LessonState;onClick:()=>void}){
 const Icon=state==='studied'?Check:state==='assisted'?HelpCircle:state==='skipped'?Minus:state==='visited'?BookOpen:ArrowRight
 return <button className={'lesson-node '+state} disabled={state==='unpublished'} aria-label={title+'. '+stateLabels[state]+'. Browse lesson'} onClick={onClick}><span className="node-number" aria-hidden="true">{state==='suggested'||state==='available'?number:<Icon size={16}/>}</span><span className="node-word" lang="ja">{japanese}</span>{state!=='suggested'&&state!=='available'&&<span className="node-status">{stateLabels[state]}</span>}</button>
}

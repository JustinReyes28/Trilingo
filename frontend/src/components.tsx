import { Component, useEffect, useRef, type ButtonHTMLAttributes, type ReactNode, type KeyboardEvent, type HTMLAttributes } from 'react'
import { AlertCircle, CheckCircle2, X } from 'lucide-react'

export function Button({variant='primary',pending=false,pendingLabel='Saving…',children,...props}:ButtonHTMLAttributes<HTMLButtonElement>&{variant?:'primary'|'secondary'|'quiet'|'danger';pending?:boolean;pendingLabel?:string}){
 return <button {...props} className={'button '+variant+' '+(props.className??'')} disabled={props.disabled||pending} aria-busy={pending||undefined}>{pending?pendingLabel:children}</button>
}
export function PageContainer({children,className='',...props}:HTMLAttributes<HTMLElement>){return <main {...props} className={'page '+className}>{children}</main>}
export function Badge({children,tone='muted'}:{children:ReactNode;tone?:'muted'|'mint'|'plum'}){return <span className={'badge '+tone}>{children}</span>}
export function Card({children,className=''}:{children:ReactNode;className?:string}){return <section className={'card '+className}>{children}</section>}
export function FeedbackPanel({kind,children}:{kind:'error'|'success'|'info';children:ReactNode}){const Icon=kind==='success'?CheckCircle2:AlertCircle;return <div className={'feedback '+kind} role={kind==='error'?'alert':'status'}><Icon size={20} aria-hidden="true"/><div>{children}</div></div>}
export function ProgressBar({value,max,label}:{value:number;max:number;label:string}){return <div className="progress-block"><div className="progress-label"><span>{label}</span><span>{value} / {max}</span></div><progress value={value} max={max} aria-label={label}/></div>}
export function Dialog({title,children,onClose}:{title:string;children:ReactNode;onClose:()=>void}){
 const ref=useRef<HTMLDialogElement>(null)
 useEffect(()=>{const dialog=ref.current;const previous=document.activeElement;dialog?.showModal();return()=>{dialog?.close();if(previous instanceof HTMLElement)previous.focus()}},[])
 function containFocus(event:KeyboardEvent<HTMLDialogElement>){
  if(event.key!=='Tab')return
  const controls=Array.from(event.currentTarget.querySelectorAll<HTMLElement>('button:not(:disabled),a[href],input:not(:disabled),select:not(:disabled),textarea:not(:disabled),[tabindex]:not([tabindex="-1"])')).filter(control=>control.getClientRects().length>0)
  const first=controls[0],last=controls[controls.length-1]
  if(!first){event.preventDefault();event.currentTarget.focus();return}
  if(event.shiftKey&&document.activeElement===first){event.preventDefault();last.focus()}
  else if(!event.shiftKey&&(document.activeElement===last||document.activeElement===event.currentTarget)){event.preventDefault();first.focus()}
 }
 return <dialog ref={ref} onKeyDown={containFocus} onCancel={onClose} aria-labelledby="dialog-title"><div className="dialog-heading"><h2 id="dialog-title">{title}</h2><Button variant="quiet" onClick={onClose} aria-label="Close dialog"><X size={20}/></Button></div>{children}</dialog>
}
export class ErrorBoundary extends Component<{children:ReactNode},{failed:boolean}>{
 state={failed:false}
 static getDerivedStateFromError(){return {failed:true}}
 componentDidCatch(error:Error){console.error('Trilingo interface error',error.message)}
 render(){return this.state.failed?<PageContainer><h1>The page could not open</h1><p>Reload the app to try again. Saved data remains in the local database.</p><Button onClick={()=>location.reload()}>Reload app</Button></PageContainer>:this.props.children}
}

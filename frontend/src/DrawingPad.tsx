import { useEffect, useId, useRef, useState, type PointerEvent } from 'react'
import type { FormationGuide, StrokePoint } from './writingSchemas'
export const normalizedPoint=(clientX:number,clientY:number,rect:{left:number;top:number;width:number;height:number},t:number):StrokePoint=>({x:Math.round(Math.max(0,Math.min(1,(clientX-rect.left)/rect.width))*10000)/10000,y:Math.round(Math.max(0,Math.min(1,(clientY-rect.top)/rect.height))*10000)/10000,t})
export function simplifyStrokes(strokes:StrokePoint[][],maximum=1200):StrokePoint[][]{
 const total=strokes.reduce((sum,stroke)=>sum+stroke.length,0)
 if(total<=maximum)return strokes
 const budget=Math.max(2,Math.floor(maximum/Math.max(1,strokes.length)))
 return strokes.map(stroke=>stroke.length<=budget?stroke:Array.from({length:budget},(_,index)=>stroke[Math.round(index*(stroke.length-1)/(budget-1))]))
}
const line=(points:{x:number;y:number}[])=>points.map((point,index)=>(index?'L':'M')+(point.x*100)+' '+(point.y*100)).join(' ')
export function DrawingPad({strokes,onChange,guide,showReference,replay=false,disabled=false}:{strokes:StrokePoint[][];onChange:(value:StrokePoint[][])=>void;guide:FormationGuide['guide'];showReference:boolean;replay?:boolean;disabled?:boolean}){
 const [current,setCurrent]=useState<StrokePoint[]>([])
 const [played,setPlayed]=useState(0)
 const active=useRef<number|null>(null)
 const points=useRef<StrokePoint[]>([])
 const start=useRef(Date.now())
 const arrow=useId()
 const shown=replay?strokes.flat().slice(0,played):null
 useEffect(()=>{if(!replay)return;let count=0;const total=strokes.flat().length;if(document.documentElement.dataset.motion==='reduced'||matchMedia('(prefers-reduced-motion: reduce)').matches){setPlayed(total);return}const timer=setInterval(()=>{count+=Math.max(1,Math.ceil(total/30));setPlayed(count);if(count>=total)clearInterval(timer)},50);return()=>clearInterval(timer)},[replay,strokes])
 function point(event:PointerEvent<SVGSVGElement>){return normalizedPoint(event.clientX,event.clientY,event.currentTarget.getBoundingClientRect(),Date.now()-start.current)}
 function down(event:PointerEvent<SVGSVGElement>){if(disabled||replay||active.current!==null||event.button!==0)return;active.current=event.pointerId;event.currentTarget.setPointerCapture(event.pointerId);points.current=[point(event)];setCurrent(points.current)}
 function move(event:PointerEvent<SVGSVGElement>){if(active.current!==event.pointerId)return;const next=point(event);const last=points.current.at(-1);if(!last||Math.hypot(next.x-last.x,next.y-last.y)>.003){points.current=[...points.current,next];setCurrent(points.current)}}
 function end(event:PointerEvent<SVGSVGElement>){if(active.current!==event.pointerId)return;const next=point(event);const stroke=[...points.current,next];active.current=null;points.current=[];setCurrent([]);onChange(simplifyStrokes([...strokes,stroke]));if(event.currentTarget.hasPointerCapture(event.pointerId))event.currentTarget.releasePointerCapture(event.pointerId)}
 return <svg className="drawing-pad" viewBox="0 0 100 100" aria-label="Character drawing area. Use pointer input or choose the keyboard stroke-sequence alternative." role="img" onPointerDown={down} onPointerMove={move} onPointerUp={end} onPointerCancel={end}>
 <defs><marker id={arrow} markerWidth="4" markerHeight="4" refX="3" refY="2" orient="auto"><path d="M0 0 L4 2 L0 4" className="guide-arrow"/></marker></defs><path className="formation-grid" d="M50 0V100 M0 50H100 M0 0L100 100 M100 0L0 100"/>
 {showReference&&guide?.strokes.map((stroke,index)=><g key={index}><path className="guide-stroke" d={line(stroke.points)} markerEnd={'url(#'+arrow+')'}/><circle className="guide-start" cx={stroke.points[0].x*100} cy={stroke.points[0].y*100} r="2.5"/><text className="guide-number" x={stroke.points[0].x*100-4} y={stroke.points[0].y*100-4}>{index+1}</text></g>)}
 {(shown?replayedStrokes(strokes,played):strokes).map((stroke,index)=><path key={index} className="learner-stroke" d={line(stroke)}/>)}{current.length>0&&<path className="learner-stroke" d={line(current)}/>}
 </svg>
}
function replayedStrokes(strokes:StrokePoint[][],count:number){const output:StrokePoint[][]=[];let remaining=count;for(const stroke of strokes){if(remaining<=0)break;output.push(stroke.slice(0,remaining));remaining-=stroke.length}return output}

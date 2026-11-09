import { z } from 'zod'
import { request } from './api'
export type PendingRequest={path:string;body:Record<string,unknown>}
export function pendingRequestStore(key:string,pathPattern:RegExp){
 const schema=z.object({path:z.string().regex(pathPattern),body:z.record(z.string(),z.unknown())})
 function list():PendingRequest[]{try{const raw=localStorage.getItem(key);if(!raw)return [];const parsed=z.array(schema).safeParse(JSON.parse(raw));return parsed.success?parsed.data:[]}catch{return []}}
 function clear(requestId:unknown){try{localStorage.setItem(key,JSON.stringify(list().filter(item=>item.body.request_id!==requestId)))}catch{/* Current screen retains retries; backend records remain durable. */}}
 function remember(operation:PendingRequest){try{localStorage.setItem(key,JSON.stringify([...list().filter(item=>item.body.request_id!==operation.body.request_id),operation]))}catch{/* The screen keeps the exact operation for retry. */}}
 async function commit<T>(operation:PendingRequest,responseSchema:z.ZodType<T>):Promise<T>{
  remember(operation)
  const value=await request(operation.path,responseSchema,{method:'POST',body:JSON.stringify(operation.body)})
  clear(operation.body.request_id)
  return value
 }
 return {list,clear,remember,commit,pending:(path?:string)=>list().find(item=>path===undefined||item.path===path)??null}
}

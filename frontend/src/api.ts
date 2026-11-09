import { z } from 'zod'

const rawBase: unknown = import.meta.env.VITE_API_BASE_URL ?? 'http://127.0.0.1:8000/api/v1'
const parsedBase = z.string().url().safeParse(rawBase)
const base = parsedBase.success ? parsedBase.data.replace(/\/$/, '') : null
const ErrorSchema = z.object({error:z.object({code:z.string(),message:z.string(),details:z.array(z.object({field:z.string(),message:z.string()})).optional()})})
export class ApiError extends Error { constructor(public code:string,message:string){super(message)} }
export async function request<T>(path:string,schema:z.ZodType<T>,options:RequestInit = {}):Promise<T> {
 if(base===null) throw new ApiError('configuration','The local API address is invalid. Correct VITE_API_BASE_URL and restart the frontend.')
 const controller = new AbortController()
 const timeout = setTimeout(()=>controller.abort(),12000)
 try {
  const response = await fetch(base+path,{...options,headers:{'Content-Type':'application/json',...options.headers},signal:options.signal?AbortSignal.any([controller.signal,options.signal]):controller.signal})
  let body:unknown
  try { body=await response.json() } catch {throw new ApiError('invalid_response','The local service returned unreadable data. Check that both app parts are up to date, then retry.')}
  if(!response.ok){const parsed=ErrorSchema.safeParse(body);throw new ApiError(parsed.success?parsed.data.error.code:'http_error',parsed.success?parsed.data.error.message+(parsed.data.error.details?.length?' '+parsed.data.error.details.map(detail=>detail.field.replace('body.','')+': '+detail.message).join(' '):''):'The local service could not complete this action. Retry when it is ready.')}
  const result=schema.safeParse(body)
  if(!result.success) throw new ApiError('invalid_response','The local service returned unexpected data. Check that both app parts are up to date, then retry.')
  return result.data
 } catch(error) {
  if(error instanceof ApiError) throw error
  throw new ApiError('connection','Cannot reach the local service. Start the backend, then retry. Your unsaved input is still here.')
 } finally {clearTimeout(timeout)}
}
export const patch = <T>(path:string,schema:z.ZodType<T>,body:unknown)=>request(path,schema,{method:'PATCH',body:JSON.stringify(body)})
export const post = <T>(path:string,schema:z.ZodType<T>,body:unknown)=>request(path,schema,{method:'POST',body:JSON.stringify(body)})
export const postBinary = <T>(path:string,schema:z.ZodType<T>,body:BodyInit,headers:Record<string,string>={})=>request(path,schema,{method:'POST',body,headers:{'Content-Type':'application/zip',...headers}})
export const getApiUrl = (path:string)=>base?base+path:path

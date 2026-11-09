import type { z } from 'zod'
import type { SegmentSchema, Settings } from './schemas'
export function JapaneseText({segments,furigana,romaji=false,familiarIds=new Set<string>()}:{segments:z.infer<typeof SegmentSchema>[];furigana:Settings['furigana'];romaji?:boolean;familiarIds?:Set<string>}){
 return <span lang="ja" className="japanese-text">{segments.map((segment,index)=>{
 const show=segment.reading&&segment.reading!==segment.surface&&(furigana==='always'||furigana==='unfamiliar'&&(!segment.vocabulary_id||!familiarIds.has(segment.vocabulary_id)))&&(romaji||!/[a-z]/i.test(segment.reading))
 return show?<ruby key={index}>{segment.surface}<rp>（</rp><rt>{segment.reading}</rt><rp>）</rp></ruby>:<span key={index}>{segment.surface}</span>
 })}</span>
}

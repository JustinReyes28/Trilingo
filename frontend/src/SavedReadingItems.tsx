import { useState } from 'react'
import { Button } from './components'
import type { Character, ReadingLibrary } from './readingSchemas'

type ReadingWord = ReadingLibrary['vocabulary'][number]
export type SavedReadingTarget =
 | { kind: 'character'; character: Character }
 | { kind: 'word'; word: ReadingWord }

type SavedLibrary = Pick<ReadingLibrary, 'items' | 'characters' | 'vocabulary'>

export function resolveSavedReadingItems(library: SavedLibrary): { targets: SavedReadingTarget[]; hiddenCount: number } {
 const characters = new Map(library.characters.map(character => [character.id, character]))
 const words = new Map(library.vocabulary.map(word => [word.id, word]))
 const targets: SavedReadingTarget[] = []
 let hiddenCount = 0
 for (const item of library.items) {
  if (!item.saved || item.item_kind === 'grammar') continue
  if (item.item_kind === 'character') {
   const character = characters.get(item.item_id)
   if (character) targets.push({ kind: 'character', character })
   else hiddenCount += 1
  } else {
   const word = words.get(item.item_id)
   if (word) targets.push({ kind: 'word', word })
   else hiddenCount += 1
  }
 }
 return { targets, hiddenCount }
}

export function SavedReadingItems({ library, batch, busy, onCharacter, onWord, onPractice }: {
 library: SavedLibrary
 batch: number
 busy: boolean
 onCharacter: (character: Character) => void
 onWord: (word: ReadingWord) => void
 onPractice: () => void
}) {
 const [limit, setLimit] = useState(batch)
 const { targets, hiddenCount } = resolveSavedReadingItems(library)
 const visible = targets.slice(0, limit)
 const hasDrills = targets.some(target => target.kind === 'character'
  ? target.character.practice_exercise_ids.length > 0
  : target.word.practice_exercise_ids.length > 0)
 return <section className="saved-reading" aria-labelledby="saved-reading-heading">
  <h2 id="saved-reading-heading">Your saved reading items</h2>
  <p>{targets.length} saved items available in this view. Open a character or find a word in context.</p>
  {hiddenCount > 0 && <p className="small">{hiddenCount} other saved items are unavailable in this view. Enable draft practice to include unreviewed entries. Saved history is preserved.</p>}
  {visible.length > 0 ? <>
   <p className="small" role="status">Showing {visible.length} of {targets.length} available saved items.</p>
   <ul className="session-list">{visible.map(target => target.kind === 'character'
    ? <li key={'character:' + target.character.id}><div><strong lang="ja">{target.character.surface}</strong><small>{target.character.script} · {target.character.status === 'published' ? 'Technical practice' : 'Draft · Review pending'}</small></div><Button variant="secondary" disabled={busy} onClick={() => onCharacter(target.character)}>Open saved character: {target.character.surface}</Button></li>
    : <li key={'word:' + target.word.id}><div><strong lang="ja">{target.word.surface}（{target.word.reading}）</strong><small>{target.word.gloss} · {target.word.status === 'published' ? 'Technical practice' : 'Draft · Review pending'}</small></div><Button variant="secondary" disabled={busy} onClick={() => onWord(target.word)}>Find saved word: {target.word.surface}</Button></li>)}</ul>
   {visible.length < targets.length && <div className="inline-actions"><Button variant="secondary" onClick={() => setLimit(value => value + batch)}>Show more saved items</Button><Button variant="quiet" onClick={() => setLimit(targets.length)}>Show all saved items</Button></div>}
  </> : <p>Save a character or word from this reading library to find it here.</p>}
  <Button pending={busy} disabled={!hasDrills} onClick={onPractice}>Practice related saved items</Button>
  <p className="small">Items without authored drills remain saved; they do not create invented exercises.</p>
 </section>
}
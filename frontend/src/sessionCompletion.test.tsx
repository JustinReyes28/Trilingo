import { renderToStaticMarkup } from 'react-dom/server'
import { expect, it } from 'vitest'
import { SessionCompletion } from './SessionCompletion'
import { StudySchema, type Study } from './studySchemas'

const completed = StudySchema.parse({
  id: 'saved-session', course_id: 'course', content_version: '1.0.0',
  source_kind: 'lesson', source_id: 'lesson', kind: 'lesson', title: 'Saved practice',
  status: 'completed', cursor: 0, revision: 1, next_action_id: 'next',
  exercises: [], evidence: {}, preview_draft: false, mode: 'supported',
  feedback: null, xp_awarded: 5, completed_at: '2026-10-25T12:00:00Z',
  created_at: '2026-10-25T11:59:00Z', initial_correct: 2, assessed_count: 3,
  concept_coverage: {}, recommendation: null, story: null,
})

function completion(changes: Partial<Study> = {}): string {
  return renderToStaticMarkup(<SessionCompletion session={{ ...completed, ...changes }} busy={false} heading={null} onReplay={() => {}} onExit={() => {}} />)
}

it('returns a completed self-rated review to its saved card instead of unsupported general replay', () => {
  const html = completion({ source_kind: 'review', source_id: 'saved-card', kind: 'review', initial_correct: 0, assessed_count: 0 })
  // ReviewPage resolves this saved session to its source card and immutable content,
  // then clears the completed timer so a deliberate rating creates a new review.
  expect(html).toContain('href="#review?session=saved-session"')
  expect(html).toContain('Review this card again')
  expect(html).toContain('Self-rated recall saved.')
  expect(html).toContain('+5 XP')
  expect(html).toContain('Choose another activity')
  expect(html).not.toContain('Start a new replay')
  expect(html).not.toContain('unassisted checks')
})

it('preserves ordinary replay and honest assisted or skipped evidence for checked sessions', () => {
  const html = completion()
  expect(html).toContain('Start a new replay')
  expect(html).toContain('2 initial correct answers out of 3 unassisted checks.')
  expect(html).toContain('Assisted answers and skips remain recorded separately.')
  expect(html).not.toContain('Review this card again')
})

it('keeps unassessed writing navigation distinct from general session replay', () => {
  const html = completion({ source_kind: 'writing', kind: 'open_writing' })
  expect(html).toContain('Writing quality is not assessed.')
  expect(html).toContain('href="#writing"')
  expect(html).toContain('Choose another writing activity')
  expect(html).not.toContain('Start a new replay')
  expect(html).not.toContain('unassisted checks')
})

it('retains freely available story replay and optional recap navigation', () => {
  const html = completion({ source_kind: 'story', story: {
    current: { id: 'last-turn', speaker: 'Mina', text: [{ surface: 'おわり' }], next_turn_ids: [], exercise_ids: [] },
    turns: [{ id: 'last-turn', speaker: 'Mina' }], visited_turn_ids: ['last-turn'],
    assisted_turn_ids: ['last-turn'], reading_aids: false, at_end: true,
    recap_available: true, glossary: [],
  } })
  expect(html).toContain('Start a new replay')
  expect(html).toContain('Start optional recap')
  expect(html).toContain('It does not certify mastery.')
})

import type { Ref } from 'react'
import { Button } from './components'
import type { Study } from './studySchemas'

type Props = {
  session: Study
  busy: boolean
  heading: Ref<HTMLHeadingElement>
  onReplay: (sourceId?: string, sourceKind?: string) => void
  onExit: () => void
}

export function SessionCompletion({ session, busy, heading, onReplay, onExit }: Props) {
  const writing = ['open_writing', 'handwriting'].includes(session.kind)
  const recall = session.source_kind === 'review'

  return <div className="completion-panel">
    <h2 ref={heading} tabIndex={-1}>Session saved</h2>
    <p className="completion-xp">+{session.xp_awarded} XP</p>
    {recall ? <p>Self-rated recall saved. Your rating records how recall felt; it is separate from checked exercise answers.</p>
      : writing ? <p>Practice activity saved. Writing quality is not assessed. Self-reported writing and drawing remain separate from checked exercise answers.</p>
      : <p>{session.kind === 'speaking'
        ? Object.values(session.evidence).reduce((sum, item) => sum + item.typed_fallbacks, 0) + ' typed practice responses. Pronunciation is not assessed.'
        : session.initial_correct + ' initial correct answers out of ' + session.assessed_count + ' unassisted checks. Assisted answers and skips remain recorded separately.'}</p>}
    <p>Study completion records your activity. It does not certify mastery.</p>
    {session.recommendation && <section>
      <h3>Suggested starting point: {session.recommendation.title}</h3>
      <p>{session.recommendation.reason}</p>
      <Button pending={busy} onClick={() => onReplay(session.recommendation?.lesson_id, 'lesson')}>Start suggested lesson</Button>
    </section>}
    <div className="inline-actions">
      {recall ? <a className="button primary" href={'#review?session=' + encodeURIComponent(session.id)}>Review this card again</a>
        : writing ? <a className="button primary" href="#writing">Choose another writing activity</a>
        : <Button pending={busy} onClick={() => onReplay()}>Start a new replay</Button>}
      {session.story?.recap_available && <Button variant="secondary" pending={busy} onClick={() => onReplay(session.source_id, 'story_recap')}>Start optional recap</Button>}
      <Button variant="secondary" onClick={onExit}>Choose another activity</Button>
    </div>
  </div>
}

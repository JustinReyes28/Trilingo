# Trilingo design system

Product register; Operate for course/settings, Read for Japanese content. Audience: an adult beginning Japanese. The course screen helps choose any published lesson.

## Structure and signature
Desktop: fixed-width navigation, flexible course path, narrow course-note sidebar. Mobile: one content column and four bottom navigation destinations. The signature is a gently alternating trail of tactile teal lesson nodes, with truthful availability and no locks. Japanese lesson words lead the path; there is no marketing hero.

## Palette and tokens
Teal ink represents a clear navigable path, plum is reserved for optional accents, and pale mint frames lesson groups. OKLCH tokens in tokens.css are authoritative. Approximate sRGB names: Ink #203c3b, Path #126b62, Mint #e9f5ef, Paper #f8faf9, Plum #704b77, Boundary #cad8d1. Text on Path is white; body text is Ink. Error and success always include text/icons.

## Typography
Use locally installed Segoe UI for controls, Yu Gothic UI / Meiryo / Hiragino Kaku Gothic ProN for Japanese UI, and Yu Mincho / Hiragino Mincho ProN for restrained Japanese display samples only. No font downloads. System font licenses remain owned by the OS; no fonts redistributed. Mixed text and ruby have generous line height and Japanese lang metadata.

## Components and states
44px minimum controls, visible 3px focus, tactile shadow only on primary buttons and path nodes, 4/8/12/16/24/32/48 spacing. Native dialog provides focus containment, Escape and restoration. Feedback uses text plus icon. Prefer natural page scrolling; mobile nav reserves bottom space and scroll padding.

Published content nodes open real lesson metadata. Study engine actions remain explicitly Upcoming until Phase 4. Draft content is labeled Not published, never an earned lock. No fabricated learner progress. Fixture feedback/editor previews exist only at /preview and are clearly labeled.

## Search fit and references
2026-10-23: ui-ux-pro-max searches Japanese learning playful workspace and adult study workspace returned marketing hero/testimonial patterns and child/corporate fonts. Rejected both rather than persisting a preset. General skill guidance is the fallback. Focus not obscured returned directly relevant scroll-padding guidance; React search supports controlled forms and accessible test queries.

Layout inspirations only (no copied assets/content): [Tofugu kana guide](https://www.tofugu.com/japanese/learn-hiragana/) for readable character-first instruction; [Irodori](https://www.irodori.jpf.go.jp/en/about.html) for practical can-do organization; [Japan Foundation resources](https://www.jpf.go.jp/e/project/japanese/education/resource/) for learning/library separation. These are broad references, not evidence of local UI quality.

## Audit
Actual screens and audit evidence are recorded in docs/PHASE_01_03_VERIFICATION.md. No preview alone establishes learning functionality.

Later writing navigation: Practice > Writing opens the beginner workspace when implemented; C-F extend that same destination into the Writing Workshop with outline/editor/revision/feedback tools. The initial shell exposes the mode as Upcoming and does not claim a functioning workshop.

## Phase 4 extension

Playable lessons now use [the lesson override](pages/lesson.md). The path displays saved visited/studied/assisted/skipped evidence; every published lesson remains directly selectable. Actual course progress and XP replace the earlier Upcoming lesson controls. Reading/writing/audio/FSRS retain their owning-phase labels. See [Phase 4 verification](../../docs/PHASE_04_VERIFICATION.md) for the rendered audit.


## Phase 5–6 extension

Practice now opens the real Reading and Writing destinations using pages/reading.md and pages/writing.md. Character details, saved preferences, story sessions, typed checks, composition drafts and formation/sample controls save real local records; development fixtures remain separate. Required rendered audits and final scoped fixes are recorded in docs/PHASE_05_VERIFICATION.md, docs/PHASE_06_VERIFICATION.md and .design-skill/audit-report.md. No draft publication or physical device certification follows from these engineering audits.

## Phase 7–9 engineering extension

Grammar, recall/quests/collections and audio/recording use [practice overrides](pages/practice.md). Actual rendered evidence and open provider/content gates are in docs/PHASE_07_09_VERIFICATION.md. This does not certify Japanese review, physical IME, microphone/STT or real playback.

# Bundled-Audio-Only Plan — Phase 2: Frontend UI, Schemas & Test Alignment

Status: **Complete & Verified (2026-11-13; uncommitted awaiting user review)**.  
Applies the user decision (`2026-11-13`): remove all frontend runtime-TTS controls, Kokoro setup forms, `/scenarios/speech` calls, and runtime synthetic-TTS fallback expectations.

**Implementation & verification status (2026-11-13):**
- Updated `frontend/src/schemas.ts`, `frontend/src/practiceSchemas.ts`, `ProfilePage.tsx`, `AudioPage.tsx`, `ScenarioPractice.tsx`, `ListeningExercise.tsx`, `ReviewMedia.tsx`, `SpeakingExercise.tsx`, `VocabularyCollections.tsx`, `PracticeChoices.tsx`, `ExerciseRenderer.tsx`, `ExerciseSession.tsx`, and Vitest suites (`api.test.ts`, `audioPack.test.tsx`, `listening.test.tsx`, `practice.test.tsx`, `profileBackup.test.tsx`, `speaking.test.tsx`).
- `ProfilePage.tsx` renders AI and STT only; `ScenarioPractice.tsx` renders text-only AI coaching + optional STT `<Recorder>`; `AudioControls` / `ListeningCues` play bundled MP3s exclusively with client `0.75x` (`preservesPitch=true`) and text fallback on `503`.
- Step 4 post-Phase-1–3 frontend gates (`lint`, `typecheck`, `53 passed` across `11` Vitest files, production `build`) and isolated Playwright Edge verification (`28` viewport layouts across `320`/`390`/`768`/`1280`) passed ([Phase 3 §3.4](BUNDLED_AUDIO_ONLY_PHASE_3_DOCS_PLANS.md#34-final-integrated-verification-pass-pre-commit-sign-off)).

**Sequence:** [Phase 1](BUNDLED_AUDIO_ONLY_PHASE_1_BACKEND.md) → Phase 2 (this file) → [Phase 3: Tooling Scope, Docs/Plans & Integrated Verification](BUNDLED_AUDIO_ONLY_PHASE_3_DOCS_PLANS.md).

---

## Goal & Boundaries

Align TypeScript/Zod contracts, Profile settings UI, practice/audio/scenario components, and Vitest tests with the Phase 1 pack-only backend contract while:

- Keeping all existing study/playback affordances: Japanese & English vocabulary reference playback, slow reference (`playbackRate = 0.75` with `preservesPitch = true`), shadowing loop, transcript reveal, skip/retry, optional local AI coaching, and optional local Japanese STT microphone feedback.
- Removing all references to `TTS_ENABLED`, `kokoro`, `jf_`/`jm_` voice configuration, and runtime TTS generation for dynamic AI replies.
- Preserving [docs/DESIGN_BRIEF.md](../DESIGN_BRIEF.md) and [design-system/trilingo/MASTER.md](../../design-system/trilingo/MASTER.md) tokens/layout without visual regressions across `320px–390px`, `768px`, and desktop widths.

---

## Detailed Tasks

### 2.1 Contracts & Zod Schemas
**Files:** `frontend/src/schemas.ts`, `frontend/src/practiceSchemas.ts`, `frontend/src/studySchemas.ts` (verify if needed)

1. **`frontend/src/schemas.ts`:**
   - Remove `tts` from `SettingsSchema` / `Settings` (and remove `voice` from `ProviderSchema` if Phase 1 removed it on the backend), keeping `ai` and `stt`.
   - Remove `tts` from `HealthSchema.features` to match Phase 1's `/api/v1/health`.
2. **`frontend/src/practiceSchemas.ts`:**
   - Update `AudioSchema` to match Phase 1's pack-only response (`mime: z.literal('audio/mpeg')`, `source: z.literal('pack')`, `cached: z.boolean()`, `label: z.string()`).
   - Update `ProviderStatusSchema` to match Phase 1's `GET /api/v1/providers/status` (`ai`, `stt`, plus explicit `audio_pack` status carrying `bundled_reference`, `bundled_reviewed`, `course_version`, `message`) with no `tts` provider entry.

### 2.2 Profile Preferences UI Cleanup
**Files:** `frontend/src/ProfilePage.tsx`

1. In the `Optional local providers` card (around line 134):
   - Change the provider list from `(['ai', 'tts', 'stt'] as const)` to `(['ai', 'stt'] as const)`.
   - Remove the `'tts'` (`Japanese speech output`, `kokoro; choose a listed Japanese jf_/jm_ voice`, and `Voice` input field) `<details>` block entirely.
   - Update intro and helper copy to mention only `AI_ENABLED` and `STT_ENABLED`, and clarify clearly that authored reference audio uses bundled clips locally without installing or configuring a TTS provider or downloading TTS models.

### 2.3 Audio Controls, Listening, Speaking, Story, Scenario & Collection Pages
**Files:** `frontend/src/AudioPage.tsx`, `frontend/src/ListeningExercise.tsx`, `frontend/src/ExerciseSession.tsx`, `frontend/src/ExerciseRenderer.tsx`, `frontend/src/ReviewMedia.tsx`, `frontend/src/StoryReader.tsx`, `frontend/src/SpeakingExercise.tsx`, `frontend/src/ScenarioPractice.tsx`, `frontend/src/VocabularyCollections.tsx`

1. **`frontend/src/AudioPage.tsx`:**
   - Update `audioBadgeLabel(status)` to read `status?.audio_pack` (`bundled_reference` / `bundled_reviewed`) and show `'Bundled audio · reviewed'`, `'Bundled audio · human review pending'`, or `'Bundled audio · unavailable'`.
   - Remove the `Runtime TTS: ...` line in the page summary; retain clear status for `Reference audio` (bundled pack status) plus optional `Runtime AI` / `STT` when relevant.
   - Simplify `AudioControls`:
     - Remove `advisoryText` prop and the `/scenarios/speech` fetch branch cleanly (`AudioControls` only requests `/audio/speech` for authored references).
     - Remove `"runtime"` vs `"pack"` `source` switching — all delivered references are bundled MP3s (`audio/mpeg`), so toggling `Slow reference` updates `playbackRate = slow ? 0.75 : 1` with `preservesPitch = true` immediately without ever clearing the loaded blob URL or re-fetching.
     - Simplify `<audio>` `aria-label` (`english ? 'Bundled English meaning audio' : 'Bundled reference audio'`) and clear fallback guidance (`Audio unavailable. Read the text or transcript alternative instead.`).
2. **`frontend/src/ScenarioPractice.tsx`:**
   - Remove `<AudioControls ... advisoryText={result.generated.partner_line} />` from the AI-generated coaching block (line 12). Keep the Japanese `partner_line` text, coaching note, uncertainty notice, and optional STT `<Recorder>` input.
3. **`frontend/src/ListeningExercise.tsx`, `ExerciseSession.tsx`, `ExerciseRenderer.tsx`, `ReviewMedia.tsx`, `SpeakingExercise.tsx`, `StoryReader.tsx`:**
   - Simplify `PreparedAudio` / `playbackRate(slow: boolean)` (all pack clips use `audio/mpeg` and `slow ? 0.75 : 1` client-side speed with `preservesPitch = true`).
   - Replace `"Bundled or synthetic reference"` / `"Synthetic reference"` copy in `ListeningCues` with honest bundled-pack wording (`"Bundled reference audio · human Japanese listening review pending. Preparing audio records delivery, not proof of hearing it. Text-assisted checks are recorded separately."`).
   - Confirm `StoryReader.tsx` passes clean `reference` without `advisoryText`.
4. **`frontend/src/VocabularyCollections.tsx`:**
   - Update line 23 copy to `"Choose meaning, reading, typing, listening or speaking recall above. Audio modes use bundled reference clips; text and self-rating remain available. Every word stays available regardless of its due date."`

### 2.4 Frontend Tests & Rendered UI Audit
**Files:** `frontend/src/audioPack.test.tsx`, `frontend/src/profileBackup.test.tsx`, `frontend/src/listening.test.tsx`, `frontend/src/speaking.test.tsx`, `frontend/src/practice.test.tsx` (and any other test referencing `ProviderStatusSchema` or `Settings` fixtures)

1. Update all test fixtures (`profileBackup.test.tsx`, `audioPack.test.tsx`, etc.) to drop `tts` from `Settings` and `ProviderStatus`, verify `AudioPage` badge and controls with `audio_pack` status, verify `ProfilePage` renders only AI and STT optional providers, and add coverage confirming `ScenarioPractice` renders text-only AI coaching without invoking `/scenarios/speech`.
2. Run UI quality workflow per [AGENTS.md](../../AGENTS.md#ui-workflow): inspect real rendered screens (`Profile`, `Audio`, `Listening`, `Speaking`, `ScenarioPractice`, `Collections`) across `320px–390px`, `~768px`, and desktop widths in isolated QA, verify keyboard navigation and Japanese IME/ruby behavior, check zero requests to `/scenarios/speech` or Kokoro ports, and apply `design-skill` detect/audit checks to modified views.

---

## Verification Gate (Phase 2 Exit Criteria)

From `frontend/`:

1. `npm run lint` → exit `0`.
2. `npm run typecheck` → exit `0`.
3. `npm test -- --run` → exit `0` across all Vitest suites.
4. `npm run build` → exit `0`.
5. Isolated Playwright browser verification across `320/390/768/desktop` widths passes cleanly with zero console errors, zero horizontal overflow, and verified `playbackRate=0.75` + `preservesPitch=true` with no runtime TTS flags or Kokoro container running.

**Next:** Proceed to [Phase 3: Tooling Scope, Docs/Plans & Integrated Verification](BUNDLED_AUDIO_ONLY_PHASE_3_DOCS_PLANS.md).

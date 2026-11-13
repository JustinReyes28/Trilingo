# Trilingo - Start Here for Future Agents

Updated: **2026-11-13**. This file routes work; the selected plan owns the details. The full project remains incomplete. Read [AGENTS.md](../AGENTS.md), the current sections of [README](../README.md), [master plan](../AI_IMPLEMENTATION_PLAN.md) and [HANDOFF](../HANDOFF.md), then open **only the track requested by the user**. Follow a cross-link when its dependency becomes relevant; do not load every platform plan or historical report upfront.

## Choose one track

- **Finish the existing learning app / Plan 9.2:** [Remaining-work execution plan](plans/REMAINING_WORK_EXECUTION_PLAN.md), W0-W6, and the relevant A-I item in [Plan 9.2](plans/PLAN_09_2_COMPLETION.md). The raw word target is already exceeded. Reuse current workflow/test evidence; address an actual content/feature/prerequisite gap.
- **Phase 10 - backup, reliability and local release:** [PHASE_10_RELEASE.md](plans/PHASE_10_RELEASE.md). Start with the Plan 9.2 handoff and the consistent backup/restore contract. Installer implementation is a separate file/track.
- **Phase 11 - public repository and launch:** [PHASE_11_OPEN_SOURCE_LAUNCH.md](plans/PHASE_11_OPEN_SOURCE_LAUNCH.md). Start with exact release evidence, repository/license/privacy preparation and reviewable launch materials. Public transfers/messages require their own authorization.
- **Windows setup EXE:** [WINDOWS_EXE_SETUP_PLAN.md](plans/WINDOWS_EXE_SETUP_PLAN.md). Start with EXE-0. This file owns the bundled runtime, local launcher, install/update/uninstall, signing and packaged validation. Read Phase 10's backup contract when EXE-2 needs it.
- **Standalone offline Android:** [ANDROID_PORT_PLAN.md](plans/ANDROID_PORT_PLAN.md). Start with A0/A1. The user confirmed core study must work without a PC/internet. Prove the device-local engine choice before porting features. Read desktop behavior/backup contracts only as needed for parity and transfer.
- **Later C-F learning/essay releases:** [Curriculum roadmap](CURRICULUM_ROADMAP.md) and remaining-plan W11; this is separate from packaging and marketing.

The phase and platform files remain separate. Keep exactly eleven numbered phases; Windows/Android are delivery supplements. Technical platform feasibility may proceed alongside content review using isolated/synthetic data. Full releases retain the applicable content, persistence and real integration/device gates.

## Minimum current context

Source **ja-starter 0.1.21**, schema **0014**. There are **2,167 provisional lexical identities (541 A +1,626 additional B)** and **6,848 pending review items**; published technical coverage remains **2 units/6 lessons/30 checks/8 words/5 expressions**. Revalidate current versions before changing content; the next changed source is ordinarily 0.1.22 or later. Do not re-run baseline-specific builders blindly or merge learner identities to adjust counts.

Authored Japanese words, listening cues, story turns and English glosses play exclusively from the bundled **90.4 MB** MP3 pack (`4,394` clips) under `content/audio/`; see [the audio pack guide](AUDIO_PACK.md). Runtime TTS (`TTS_ENABLED`, `AUDIO_CACHE_DIR`, Kokoro/Edge-TTS/Piper adapters, `POST /api/v1/scenarios/speech`, `GET /api/v1/audio/voices`) was removed across Phases 1–3 on 2026-11-13; AI (`AI_ENABLED`) and STT (`STT_ENABLED`) are the only optional local providers, and slow playback uses client `0.75x` with `preservesPitch=true`. Installer/Android compatibility, qualified human audio/content review, fresh independent setup, and real AI/STT checks remain open; post-Phase-1–3 integrated verification (`238` backend tests, `53` frontend tests, `0014` migration checks, `28` QA layouts) passed on 2026-11-13.

## Rules that travel with every track

- Keep Trilingo branding, original content, unrestricted study, honest assistance/self-rating and uncapped genuine-session XP with idempotent retries.
- Play authored reference audio solely from the versioned bundled MP3 pack; there is no runtime TTS synthesis or model download. When audio is unavailable (`AUDIO_PACK_ENABLED=false` or missing clip), endpoints return HTTP `503` (`audio_unavailable`) and learning continues via text alternatives. Maintainers regenerate/validate the pack after text, override or voice changes, and must not claim reviewed teaching audio before qualified human review.
- Protect learner data. Use disposable migrated QA stores; progress deletion/restore replacement needs confirmation and export. Preserve immutable content/history and migration-driven schema changes.
- Network: unmetered since 2026-11-09, so downloads need no size approval. Git push, publication, posts, messages and external file sends still need explicit user instruction.
- Delegation: hand implementation, tests and research to `inherit` (Gemini 4 Hydrogen) subagents per [AGENTS.md](../AGENTS.md#orchestration-and-subagent-delegation); review and verify their output before reporting.
- The earlier **18/18 implementation checks are spent historical bounds**. This later request created documentation only. On a new implementation instruction, honor its current bounds; do not inherit expired allowances, invent deadlines or require a numeric allowance when none is set.
- Finish one coherent authorized deliverable, verify only its affected behavior, update the selected plan and HANDOFF, stop owned QA services and report the precise remaining gates. Do not use a passed batch as proof of the whole project.

Copyable resume instruction:

> Read AGENTS.md, docs/AGENT_CONTINUATION_GUIDE.md, HANDOFF.md and the selected track. Continue **[task ID / concrete deliverable]** under my current constraints. Reuse existing evidence/services, preserve learner data and publication approvals, and update the handoff with actual results. Open other plans only when that task's dependency requires them.

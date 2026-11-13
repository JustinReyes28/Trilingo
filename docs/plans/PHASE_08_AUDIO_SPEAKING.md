# Phase 08 — Japanese Audio, Listening, and Speaking

Status: Partial engineering implementation (bundled static MP3 pack implemented 2026-11-13; runtime TTS removed 2026-11-13 in schema `0014`). Qualified human listening review of the bundled pack and optional STT/real-microphone verification remain open. Depends on: [Phase 07](PHASE_07_GRAMMAR_DIALOGUES.md). Next: [Phase 09](PHASE_09_REVIEW_PROGRESS.md).

## Goal

Provide real Japanese listening and speaking practice using the bundled authored MP3 pack (`content/audio/<course>/<version>/`) and optional local STT, while keeping every core lesson usable via text alternatives when audio or a microphone is unavailable.

## Audio architecture status (2026-11-13 bundled-audio-only)

Runtime Kokoro/TTS synthesis, `TTS_ENABLED`, `AUDIO_CACHE_DIR`, `POST /api/v1/scenarios/speech`, and `GET /api/v1/audio/voices` have been **removed** (2026-11-13). Authored Japanese words, listening cues, story turns, and English vocabulary meanings ship exclusively as pre-generated static MP3 files in [`content/audio/ja-starter/0.1.21/`](../../content/audio/ja-starter/0.1.21/manifest.json) (`4,394` clips, `90.4 MB`). Slow playback uses client `HTMLAudioElement.playbackRate = 0.75` (`preservesPitch = true`). Dynamic AI scenario coaching is text-only plus optional local Whisper STT (`STT_ENABLED`). Maintenance regeneration of future packs (`0.1.22+`) lives in optional `scripts/build_audio_pack.py`.

## Initial inspection evidence — 2026-10-22

- Supplied path: `C:\Users\Administrator\AppData\Local\Docker\wsl\disk\docker_data.vhdx`.
- File was observed to exist, with length 11,082,399,744 bytes. Size does not identify its contents or capabilities.
- Docker CLI was found at `C:\Users\Administrator\AppData\Local\Programs\DockerDesktop\resources\bin\docker.exe`.
- `docker ps -a --format '{{.Names}}|{{.Image}}|{{.Status}}|{{.Ports}}'` failed to connect to `npipe:////./pipe/dockerDesktopLinuxEngine`; the pipe was not found.
- Initial conclusion before the user's clarification: Docker's Linux engine was unreachable, so container inventory and engine capabilities could not be inspected. Current plan: Kokoro identified by the user, Japanese supported upstream, installed wrapper/model/voice/endpoint and actual playback unverified. Do not infer installation details from the disk filename.
- No container was started, installed, reconfigured, or removed. No VHDX mount/edit/compaction/reset was performed.
- Docker documents this path as its WSL 2 VM data disk in its [backup documentation](https://docs.docker.com/desktop/settings-and-maintenance/backup-and-restore/).

## Bundled pack listening review & superseded runtime-Kokoro checks

*(All runtime Kokoro Docker/wrapper inspection, runtime voice selection, and runtime synthesis items below were superseded on 2026-11-13 by the committed `0.1.21` bundled MP3 pack; only qualified human listening review of the bundled pack remains open.)*

- [x] Superseded (2026-11-13 bundled-audio-only): runtime Docker/Kokoro image, schema, and API discovery — no runtime TTS container runs in Trilingo (`0.1.21` pack already built/committed).
- [x] Superseded (2026-11-13 bundled-audio-only): runtime Kokoro `lang_code='j'` / `misaki[ja]` pipeline checks (`scripts/build_audio_pack.py` stays optional maintainer-only for `0.1.22+`).
- [x] Superseded (2026-11-13 bundled-audio-only): runtime Japanese voice list discovery (`GET /api/v1/audio/voices` removed).
- [x] Superseded (2026-11-13 bundled-audio-only): runtime wrapper `/v1/audio/speech` check — replaced by bundled `content/audio/<course>/<version>/` MP3 pack lookup.
- [x] Superseded (2026-11-13 bundled-audio-only): runtime synthesis health/fallback checks — replaced by `scripts/check_audio_pack.py --strict` and `GET /api/v1/providers/status` (`audio_pack`).
- [ ] Verify bundled `0.1.21` MP3 coverage and perform qualified human listening review across kana (`こんにちは。`), kanji (`日本語を勉強しています。`), particles (`私は学校へ行きます。`, including topic `は` and directional `へ`), numbers/counters (`三時にコーヒーを二杯ください。`), and long-vowel/small-kana examples (`きょう、きってをかいます。`), plus `0.75x` slow playback (`preservesPitch=true`) and text-alternative `503 audio_unavailable` fallback when `AUDIO_PACK_ENABLED=false`.
- [ ] Validate decodable non-silent MP3 duration/hashes (`scripts/check_audio_pack.py --strict`) and confirm expected contextual readings in browser playback without runtime TTS requests.
- [ ] Record qualified human Japanese listening sign-off against reviewed contextual readings (`manifest.json` `status` updated from `draft` to `reviewed`; do not treat STT transcripts as proof of teaching audio quality or pitch accent).
- [x] Classified (2026-11-13): runtime TTS removed; authored audio served exclusively from bundled MP3 pack (`bundled_reference=true`, `bundled_reviewed=false` pending qualified review).

## Provider choice and deliverables

- [x] Superseded (2026-11-13 bundled-audio-only): configure runtime Kokoro adapter/port/voice settings (`provider=kokoro`, `TTS_ENABLED`, `AUDIO_CACHE_DIR` removed in schema `0014`).
- [x] Superseded (2026-11-13 bundled-audio-only): evaluate runtime Kokoro alternatives such as VOICEVOX Engine — zero runtime TTS engines are supported or downloaded.
- [x] Superseded (2026-11-13 bundled-audio-only): keep replaceable runtime TTS adapter selection (`providers.voices`/`providers.synthesize` removed).
- [x] Implemented (updated 2026-11-13): bundled MP3 pack lookup (`backend/app/audio_pack.py`), `GET /api/v1/providers/status` (`audio_pack`), structured `503 audio_unavailable` fallback, and strict size/path/hash validation (no runtime TTS adapter).
- [x] Implemented (updated 2026-11-13): authored audio references hashed by content text, pronunciation override, language, voice, and generator settings inside immutable versioned packs (`content/audio/<course>/<version>/`).
- [x] Add user-triggered play/replay, client normal/`0.75x` slow speed (`preservesPitch=true`), cancellation, loading/error states, and no surprise autoplay.
- [x] Add listening selection, dictation, and contrast drills through the shared pipeline. Default unassisted prompts can hide the transcript, but Reveal/Hint/Skip remain freely available and record assistance rather than blocking continuation.
- [ ] Complete qualified review and voiced playback verification for Phase 5 story listen-along and at least two original mini audio episodes with comprehension checkpoints, optional transcript reveal, replay, and client `0.75x` slow playback using the bundled MP3 pack. Label synthetic speech honestly (`bundled_reviewed=false` until approved).
- [ ] Verify focused listening-only and speaking-only practice sessions, shadowing loops, and text-only AI scenario coaching with optional STT voice input (`POST /api/v1/scenarios/speech` removed). Reuse existing lesson/practice services and preserve typed fallback.
- [x] Add microphone permission, visible record/stop/cancel, local recording playback, retry, device unavailable state, and a text fallback.
- [ ] Verify optional independent STT adapter (`STT_ENABLED`) with real Japanese speech input. (TTS was removed; STT remains an optional loopback provider.)
- [ ] For STT, pin a maintained local Whisper-compatible provider/model after checking official documentation; verify language setting, audio formats, resource needs, and real Japanese transcription.
- [x] Show recognized text and feedback labeled as transcript agreement with the target phrase. Explain that STT can misrecognize speech and does not provide phoneme-level or pitch-accent assessment.
- [ ] Enable shadowing and voiced authored dialogues, with optional text/translation reveal and a clear distinction between reference audio and the learner's recording.
- [x] Keep recordings local and transient by default, with explicit opt-in retention, a deletion control, and documented provider data handling. Never silently send audio to a cloud service.

## Intended implementation areas

Backend audio provider adapters/services, generated media/cache handling, audio/speaking/listening exercise components, content audio references, settings/status UI, and optional provider deployment notes.

## Data and API contracts

- Under `/api/v1`, expose `GET /api/v1/providers/status` (`{ai, stt, audio_pack}`), `POST /api/v1/audio/speech` (`source="pack"`, `mime="audio/mpeg"`, or HTTP `503 audio_unavailable`), and optional STT submission (`POST /api/v1/scenarios/transcriptions` / speaking endpoints). Runtime TTS routes (`GET /api/v1/audio/voices`, `POST /api/v1/scenarios/speech`) do not exist.
- Separate authored content text, maintainer pronunciation override, displayed transcript, and manifest asset metadata (`content/audio/<course>/<version>/manifest.json`). Do not globally replace kanji with a guessed reading.
- A submitted recording has an attempt/exercise identity, bounded duration/size, declared/validated format, and idempotency key.
- Decode/validate audio before processing; reject invalid media, path traversal, arbitrary media URLs, and oversized work. Do not log raw audio or secrets.
- Provider configuration (`AI_ENABLED`, `STT_ENABLED`, loopback URLs) is controlled local settings; no endpoint acts as an arbitrary URL fetcher.
- Speaking remains optional practice; unavailable bundled audio (`503 audio_unavailable`), STT failure, or uncertain mismatch offers replay/retry/skip/text fallback while other published study remains available. Record speaking evidence and unverified/self-assessed attempts honestly (`AudioDelivery` rows are never written when bundled pack lookup fails).
- Audio-unavailable fallback may fulfill the core lesson via a typed/authored alternative, but it must not count as assessed listening/speaking mastery or earn duplicate rewards.
- Story/audio-episode and focused speaking/listening sessions use Phase 4's existing practice reward/activity rules and Phase 9 quest capability checks. Transcript reveal is assisted evidence; unavailable audio does not fulfill a listening-specific objective or quest.

## Tests and manual verification

- [x] Superseded (2026-11-13 bundled-audio-only): runtime TTS adapter tests replaced by bundled MP3 pack lookup, manifest path/hash integrity, `503 audio_unavailable` fallback, and optional STT adapter tests (`test_audio_pack.py`, `test_listening.py`, `test_speaking.py`).
- [x] Superseded (2026-11-13 bundled-audio-only): runtime Kokoro voice/tokenizer/host-port discovery tests — runtime TTS removed.
- [x] Test listening answer protection, grades, duplicate submissions, and fallback evidence tags.
- [ ] Test story/audio-episode checkpoint completion, transcript reveal, focused skill sessions, and no duplicate XP/quest credit across text/audio fallback.
- [ ] Test microphone denied/missing/busy, recording cancel, unsupported browser format, no speech, STT uncertainty, and retention/deletion.
- [ ] Complete qualified human Japanese listening review of the bundled `0.1.21` MP3 pack (including the five-phrase verification set) and update `manifest.json` review metadata only upon sign-off.
- [ ] Complete a real microphone-to-Japanese-transcript round trip and a voiced authored dialogue using optional STT. Contract mocks do not satisfy these checks.
- [ ] Repeat a core lesson with `AUDIO_PACK_ENABLED=false` and `STT_ENABLED`/`AI_ENABLED` disabled and confirm no progression is blocked or speaking/listening mastery fabricated.
- [ ] Run relevant frontend/backend gates, migrations if changed, and manual mobile/keyboard checks. Record latency and machine/model details without promising a universal target.

## Completion gate

Complete only when the committed bundled MP3 pack passes qualified human Japanese listening review (`bundled_reviewed=true`), Japanese speech capture/optional STT transcription works on the target computer, story listen-along and at least two reviewed mini audio episodes work with bundled MP3 clips, unavailable-audio/STT failures have usable fallbacks, and claims match implemented capability. If optional STT/microphone or human listening review cannot be verified, report this phase as partial; text fallback alone does not complete the user's speaking/listening review gates.

## Later-stage listening and speaking

Stages C-F in the [curriculum roadmap](../CURRICULUM_ROADMAP.md) add level-appropriate narration, summaries, opinions, longer talks, discussion, and oral explanation/defense of an essay. Continue extending versioned bundled MP3 packs for authored C-F reference media and optional independent STT transcription, with reviewed contextual readings and practical chunk/replay controls (`0.75x` / normal) for long text. Transcription agreement does not assess the strength of an argument, spontaneous interaction, register, or phoneme-level pronunciation; preserve self-review/human feedback as separate evidence.

## Reference basis

Kokoro capability and wrapper examples above come from their own repositories, checked on 2026-10-22; they are not evidence of this machine's installed configuration. Speaking-practice ideas were checked against [Babbel's speech recognition overview](https://support.babbel.com/hc/en-us/articles/19211305815570-Speech-recognition) and [Babbel Speak](https://support.babbel.com/hc/en-us/articles/25875402999826-Babbel-Speak). Original story/audio-practice ideas also follow the general modes in [Duolingo's practice overview](https://blog.duolingo.com/ways-to-practice-in-duolingo/). These product references neither supply Japanese course content nor prove local audio works.

## Bounded implementation evidence — 2026-10-23

Checked deliverables refer to the implemented technical/draft slice and tested adapter/control contracts, not full beginner publication or real-provider success. [Verification and remaining work](../PHASE_07_09_VERIFICATION.md) records exact scope, commands, responsive evidence, migrations and limitations. All unchecked tests and the full completion gate remain open; no bulk completion is claimed.

Additional-hour scope: private authored cue/override metadata, cache invalidation, shared listening selection/dictation/contrast, and focused rewarded listening sessions are implemented for labeled drafts. Local fixture test tones verify contracts/controls only. Both legacy string and current object voice-list formats are tested. Upstream documentation was rechecked on 2026-10-23: [wrapper speech/voice routes](https://github.com/remsky/Kokoro-FastAPI#core), [upstream Japanese pipeline](https://github.com/hexgrad/kokoro#advanced-usage). Neither source verifies this machine's installed wrapper or teaching audio. Speaking-only rewards, voiced AI roleplay, real Kokoro/STT, and reviewed episode publication remain open. See [follow-up evidence](../PHASE_07_09_FOLLOWUP.md).

## Speaking continuation — 2026-10-24

[Plan 9.2 speaking evidence](../PLAN_09_2_SPEAKING.md) adds durable rewarded speaking sessions, 16 draft model/partner prompts, explicit STT submission, typed fallback and separate transcript evidence, plus voiced-control integration for optional bounded coaching. Word/collection audio recall remains self-rated and does not create speech evidence. Media, stale/configuration, idempotency and provider-disabled core checks pass; migration 0013 preserves historical JSON/receipts. Real Kokoro/STT, human listening/microphone, voiced AI turn and reviewed publication gates above remain open.

## Bundled-audio-only migration — 2026-11-13

- Removed all runtime TTS endpoints (`POST /api/v1/scenarios/speech`, `GET /api/v1/audio/voices`), `TTS_ENABLED`, `AUDIO_CACHE_DIR`, and Kokoro/Edge-TTS/Piper runtime synthesis logic (schema `0014` strips `tts` and `voice` preferences).
- Authored words, audio cues, story turns, and English glosses play strictly from `content/audio/<course>/<version>/` (`4,394` clips in `0.1.21`), using browser `0.75x` (`preservesPitch=true`) for slow playback and HTTP `503 audio_unavailable` + text alternatives when unavailable. AI scenario coaching is text-only plus optional local Whisper STT (`STT_ENABLED`).

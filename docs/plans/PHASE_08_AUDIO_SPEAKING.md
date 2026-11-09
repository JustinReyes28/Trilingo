# Phase 08 — Japanese TTS, Listening, and Speaking

Status: Partial engineering implementation (2026-10-23); qualified content and/or real-provider gates remain open. Depends on: [Phase 07](PHASE_07_GRAMMAR_DIALOGUES.md). Discovery may run in Phase 01. Next: [Phase 09](PHASE_09_REVIEW_PROGRESS.md).

## Goal

Provide real Japanese listening and speaking practice while keeping every core lesson usable when a provider or microphone is unavailable.

## Kokoro choice and verification status

The user identified the existing service as **Kokoro TTS**. Prefer reusing it. [Upstream Kokoro](https://github.com/hexgrad/kokoro) documents Japanese support with `KPipeline(lang_code='j')` and the Japanese `misaki[ja]` dependency set. This establishes upstream capability; the installed service still needs a voice/dependency/playback check.

The exact wrapper is not yet confirmed. If it is [Kokoro-FastAPI](https://github.com/remsky/Kokoro-FastAPI), its documentation lists Japanese, a Japanese `jf_alpha` voice example, and voice/synthesis endpoints. Verify the running release's own schema and voice list before using those routes. Another Kokoro wrapper may expose a different API.

## Initial inspection evidence — 2026-10-22

- Supplied path: `C:\Users\Administrator\AppData\Local\Docker\wsl\disk\docker_data.vhdx`.
- File was observed to exist, with length 11,082,399,744 bytes. Size does not identify its contents or capabilities.
- Docker CLI was found at `C:\Users\Administrator\AppData\Local\Programs\DockerDesktop\resources\bin\docker.exe`.
- `docker ps -a --format '{{.Names}}|{{.Image}}|{{.Status}}|{{.Ports}}'` failed to connect to `npipe:////./pipe/dockerDesktopLinuxEngine`; the pipe was not found.
- Initial conclusion before the user's clarification: Docker's Linux engine was unreachable, so container inventory and engine capabilities could not be inspected. Current plan: Kokoro identified by the user, Japanese supported upstream, installed wrapper/model/voice/endpoint and actual playback unverified. Do not infer installation details from the disk filename.
- No container was started, installed, reconfigured, or removed. No VHDX mount/edit/compaction/reset was performed.
- Docker documents this path as its WSL 2 VM data disk in its [backup documentation](https://docs.docker.com/desktop/settings-and-maintenance/backup-and-restore/).

## Kokoro installation and Japanese playback gate

Perform these checks when Docker is running. The commands below are planned diagnostics, not completed checks. Do not dump full container environments, which may contain credentials.

```powershell
docker context ls
docker ps -a --format '{{.Names}}|{{.Image}}|{{.Status}}|{{.Ports}}'
docker images --format '{{.Repository}}:{{.Tag}}'
# Replace the name only after identifying the existing Kokoro container:
docker inspect --format '{{.Config.Image}} {{json .NetworkSettings.Ports}}' <kokoro-container>
```

- [ ] Record the actual image tag/digest, engine version, model ID, startup requirements, host port, API schema, voice IDs, and CPU/GPU requirements.
- [ ] Confirm the wrapper and model version are compatible with upstream Japanese support. For a native Kokoro pipeline, map the app language `ja` to upstream `j` and verify the `misaki[ja]` dependencies; do not assume the English pipeline is sufficient.
- [ ] Select an available Japanese voice from the installed service, for example `jf_alpha` only if listed. Verify required tokenizers/dictionaries/model/voice files are present and work offline after setup.
- [ ] If the installed wrapper is Kokoro-FastAPI, check its versioned schema for `GET /v1/audio/voices` and `POST /v1/audio/speech`; otherwise use that wrapper's documented routes. Confirm whether it infers Japanese from the voice or expects an explicit language setting.
- [ ] Use documented health/language/voice routes where available. If absent, inspect documented configuration and perform real synthesis.
- [ ] Synthesize kana (`こんにちは。`), kanji (`日本語を勉強しています。`), a particle sentence (`私は学校へ行きます。`), a number/counter sentence (`三時にコーヒーを二杯ください。`), and a long-vowel/small-kana example (`きょう、きってをかいます。`).
- [ ] Validate response type, decodable non-silent audio, duration, normal/slow playback, and cache replay. Listen for Japanese output and expected readings, including topic は and directional へ.
- [ ] Record a human listening check against reviewed contextual readings; do not treat an STT transcript alone as proof of correct teaching audio or pitch accent.
- [ ] Classify the installed setup as verified Japanese playback, Japanese setup incomplete, unsupported installed version, or unverified, with evidence. Keep this distinct from the already documented upstream Japanese capability.

## Provider choice and deliverables

- [ ] Integrate the existing Kokoro service first if it passes the gate and its output/license is suitable. Keep provider/base URL/model/language/voice/timeout in one configuration source; example app settings are `provider=kokoro`, `language=ja`, and a verified installed Japanese voice. Discover the actual host port instead of assuming a default.
- [ ] If Kokoro needs missing Japanese dependencies/voice files, document the minimal setup change before considering another engine. Evaluate an alternative such as [VOICEVOX Engine](https://github.com/VOICEVOX/voicevox_engine) only if Kokoro cannot meet the tested requirements; check selected engine/voice terms and teaching quality.
- [ ] Keep provider selection replaceable; do not install a fallback or pull a large model as part of this planning task.
- [x] Build a backend TTS adapter with capability/status, voices, synthesis, timeout, structured errors, and size limits. An adapter translates provider-specific routes.
- [x] Provide authored audio references and a cache keyed by content text/reading override, engine/model/voice version, and synthesis settings. Invalidate on changes.
- [x] Add user-triggered play/replay, normal/slow speed, cancellation, loading/error states, and no surprise autoplay.
- [x] Add listening selection, dictation, and contrast drills through the shared pipeline. Default unassisted prompts can hide the transcript, but Reveal/Hint/Skip remain freely available and record assistance rather than blocking continuation.
- [ ] Add Kokoro-backed listen-along for Phase 5 stories and at least two original mini audio episodes with comprehension checkpoints, optional transcript reveal, replay, and slow playback. Label synthetic speech honestly and review contextual readings before publishing.
- [ ] Add focused listening-only and speaking-only practice sessions, shadowing loops, and optional local voice roleplay for Phase 7 scenarios. Reuse existing lesson/practice services and preserve typed fallback.
- [x] Add microphone permission, visible record/stop/cancel, local recording playback, retry, device unavailable state, and a text fallback.
- [ ] Add an independent STT adapter with verified Japanese support. TTS produces audio; it does not supply speech recognition.
- [ ] For STT, pin a maintained local provider/model after checking official documentation; verify language setting, audio formats, resource needs, and real Japanese transcription.
- [x] Show recognized text and feedback labeled as transcript agreement with the target phrase. Explain that STT can misrecognize speech and does not provide phoneme-level or pitch-accent assessment.
- [ ] Enable shadowing and voiced authored dialogues, with optional text/translation reveal and a clear distinction between reference audio and the learner's recording.
- [x] Keep recordings local and transient by default, with explicit opt-in retention, a deletion control, and documented provider data handling. Never silently send audio to a cloud service.

## Intended implementation areas

Backend audio provider adapters/services, generated media/cache handling, audio/speaking/listening exercise components, content audio references, settings/status UI, and optional provider deployment notes.

## Data and API contracts

- Under `/api/v1`, define TTS/STT status/capabilities, audio generation/retrieval, and speech submission/status endpoints according to the chosen providers' latency.
- Separate authored content text, provider pronunciation override, displayed transcript, and cached asset metadata. Do not globally replace kanji with a guessed reading.
- A submitted recording has an attempt/exercise identity, bounded duration/size, declared/validated format, and idempotency key.
- Decode/validate audio before processing; reject invalid media, path traversal, arbitrary media URLs, and oversized work. Do not log raw audio or secrets.
- Provider configuration is controlled local settings; no endpoint acts as an arbitrary URL fetcher.
- Speaking remains optional practice; provider failure or uncertain mismatch offers replay/retry/skip/text fallback while other published study remains available. Record speaking evidence and unverified/self-assessed attempts honestly.
- Audio-unavailable fallback may fulfill the core lesson via a typed/authored alternative, but it must not count as assessed listening/speaking mastery or earn duplicate rewards.
- Story/audio-episode and focused speaking/listening sessions use Phase 4's existing practice reward/activity rules and Phase 9 quest capability checks. Transcript reveal is assisted evidence; unavailable audio does not fulfill a listening-specific objective or quest.

## Tests and manual verification

- [ ] Test adapters with valid/invalid audio, provider unavailable, timeout, cancellation, unsupported Japanese voice, cache invalidation, and missing assets.
- [ ] Test Kokoro language/voice selection, missing Japanese dependencies, wrapper schema differences, rejected English-only setup, and configuration-based host/port changes.
- [x] Test listening answer protection, grades, duplicate submissions, and fallback evidence tags.
- [ ] Test story/audio-episode checkpoint completion, transcript reveal, focused skill sessions, and no duplicate XP/quest credit across text/audio fallback.
- [ ] Test microphone denied/missing/busy, recording cancel, unsupported browser format, no speech, STT uncertainty, and retention/deletion.
- [ ] Complete a real Japanese TTS synthesis and listen to the test set on the target computer. Preserve the provider/config evidence without secrets.
- [ ] Complete a real microphone-to-Japanese-transcript round trip and a voiced authored dialogue. Contract mocks do not satisfy these checks.
- [ ] Repeat a core lesson with TTS/STT/AI all disabled and confirm no progression is blocked or speaking mastery fabricated.
- [ ] Run relevant frontend/backend gates, migrations if changed, and manual mobile/keyboard checks. Record latency and machine/model details without promising a universal target.

## Completion gate

Complete only when actual Kokoro Japanese playback (or a documented verified substitute), Japanese speech capture/transcription, story listen-along, and at least two reviewed mini audio episodes work on the target computer; provider failures have usable fallbacks and claims match implemented capability. If providers cannot be verified, report this phase as partial; text fallback alone does not complete the user's speaking feature.

## Later-stage listening and speaking

Stages C-F in the [curriculum roadmap](../CURRICULUM_ROADMAP.md) add level-appropriate narration, summaries, opinions, longer talks, discussion, and oral explanation/defense of an essay. Continue using the existing Kokoro adapter and independent STT provider, with reviewed contextual readings and practical chunk/replay controls for long text. Transcription agreement does not assess the strength of an argument, spontaneous interaction, register, or phoneme-level pronunciation; preserve self-review/human feedback as separate evidence.

## Reference basis

Kokoro capability and wrapper examples above come from their own repositories, checked on 2026-10-22; they are not evidence of this machine's installed configuration. Speaking-practice ideas were checked against [Babbel's speech recognition overview](https://support.babbel.com/hc/en-us/articles/19211305815570-Speech-recognition) and [Babbel Speak](https://support.babbel.com/hc/en-us/articles/25875402999826-Babbel-Speak). Original story/audio-practice ideas also follow the general modes in [Duolingo's practice overview](https://blog.duolingo.com/ways-to-practice-in-duolingo/). These product references neither supply Japanese course content nor prove local audio works.

## Bounded implementation evidence — 2026-10-23

Checked deliverables refer to the implemented technical/draft slice and tested adapter/control contracts, not full beginner publication or real-provider success. [Verification and remaining work](../PHASE_07_09_VERIFICATION.md) records exact scope, commands, responsive evidence, migrations and limitations. All unchecked tests and the full completion gate remain open; no bulk completion is claimed.

Additional-hour scope: private authored cue/override metadata, cache invalidation, shared listening selection/dictation/contrast, and focused rewarded listening sessions are implemented for labeled drafts. Local fixture test tones verify contracts/controls only. Both legacy string and current object voice-list formats are tested. Upstream documentation was rechecked on 2026-10-23: [wrapper speech/voice routes](https://github.com/remsky/Kokoro-FastAPI#core), [upstream Japanese pipeline](https://github.com/hexgrad/kokoro#advanced-usage). Neither source verifies this machine's installed wrapper or teaching audio. Speaking-only rewards, voiced AI roleplay, real Kokoro/STT, and reviewed episode publication remain open. See [follow-up evidence](../PHASE_07_09_FOLLOWUP.md).

## Speaking continuation — 2026-10-24

[Plan 9.2 speaking evidence](../PLAN_09_2_SPEAKING.md) adds durable rewarded speaking sessions, 16 draft model/partner prompts, explicit STT submission, typed fallback and separate transcript evidence, plus voiced-control integration for optional bounded coaching. Word/collection audio recall remains self-rated and does not create speech evidence. Media, stale/configuration, idempotency and provider-disabled core checks pass; migration 0013 preserves historical JSON/receipts. Real Kokoro/STT, human listening/microphone, voiced AI turn and reviewed publication gates above remain open.

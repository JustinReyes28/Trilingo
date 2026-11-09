# Phase 11 — Trilingo Open-Source GitHub Release and Launch

Status: Planned; publication and promotion have not started. Depends on: [Phase 10](PHASE_10_RELEASE.md) for the declared release's verification. Next: maintain the public project and deliver later curriculum releases under their own gates.

**TL;DR:** Prepare a clean, licensed public GitHub repository, publish a verified release, then announce it on LinkedIn, Reddit and X with honest demos and a short feedback campaign.

## Confirmed project identity

The public project/product name is **Trilingo**, with this exact spelling and capitalization. Use Trilingo in the GitHub repository identity, README heading/description, release titles/notes, screenshots/demo captions and LinkedIn/Reddit/X launch materials. The repository name is **Trilingo** (`trilingo` is acceptable as a lowercase technical slug); downloadable release artifacts should use a `trilingo-<version>` prefix. Resolve any owner/namespace availability issue while preserving the Trilingo product name; do not choose an unrelated name or leave a template project name in an upload.

## Goal

This file owns public repository/release preparation and launch, not platform implementation. If a final post/release includes Windows or Android artifacts, consult only the completed artifact evidence from [the EXE track](WINDOWS_EXE_SETUP_PLAN.md) or [Android track](ANDROID_PORT_PLAN.md). Their implementation remains in separate files. Android store publication is a separately approved channel; the GitHub/social launch does not authorize it or waive sized-transfer approval.

Make Trilingo available as an open-source project that another learner or contributor can install, understand and improve. Introduce it to relevant audiences without overstating Japanese coverage, assessment quality or unfinished features.

This phase covers source publication and an organic launch. GitHub hosts the source and release material; the React/FastAPI/SQLite app still runs locally. A hosted web service, paid advertising and account automation require separate scope. Adding this plan does not publish a repository or send posts. At execution, prepare the exact repository contents, release and posts for the user's review; obtain explicit authorization for public upload and each social publishing action unless already authorized then. Do not request account credentials in chat.

## Cellular transfers and evidence location

The connection is metered. Before any Git clone/fetch/push, release/media upload or other external file transfer, present exact purpose/source/destination/scope and the total estimated network MB/GB, including dependencies/layers and uncertainty; wait for approval of that bounded batch. No automatic cache-miss download or retry. Remote CI/setup validation may fetch dependencies or artifacts: include the expected scope/size in the proposal rather than treating publication permission as blanket transfer approval. Use installed caches/local preparation first. Follow [the sized-transfer protocol](REMAINING_WORK_EXECUTION_PLAN.md#cellular-data-and-transfer-rule). Exact repository visibility/posts/accounts/community authorization remains separate.

During execution, keep one release record under `docs/verification/public-release/<tag>/`: `readiness.md` (owner/license/privacy/CI/setup checklist and exact candidate), `claim-sheet.md` (shipped/reviewed/draft/platform limitations), and `publication-log.md` (approved payloads/sizes, commit/tag, real release/post URLs, dates and follow-up results). These are proposed paths, not existing completed artifacts. Update this phase/HANDOFF with actual locations; redact private account/learner data before any public transfer.

## Deliverables

### GitHub and open-source readiness

- [x] Confirm the GitHub owner, repository name **Trilingo** (or lowercase `trilingo`), public visibility, release tag and maintainer identity; record the final URL. Repository created at `https://github.com/JustinReyes28/Trilingo`.
- [x] Choose and record an open-source code license with the rights holder. Add LICENSE and distinguish code licensing from course text/assets. The code is licensed under MIT; course text/assets under CC-BY-4.0 in `LICENSE`.
- [x] Audit the exact files to commit and all existing Git history before publication. Exclude secrets, .env files, local SQLite/WAL files, progress, writing/recording samples, logs, machine paths in artifacts, caches, dependencies and personal backups. Keep .env.example with safe values. Use the existing .gitignore and verify its actual coverage.
- [ ] Preserve the local personal database and working setup. Use an isolated release checkout and synthetic demonstration profile; never reset personal progress to prepare a screenshot or release.
- [x] Update README with a clear project description, authentic screenshot, supported prerequisites, tested Windows quick start, migrations/content import, optional providers, update/backup guidance, exact validation commands and known limitations.
- [x] Add CONTRIBUTING.md, a support/conduct policy, actionable bug/feature templates and a pull-request template. Explain how to contribute Japanese content and record qualified review separately from code review.
- [x] Add SECURITY.md with a real maintainer-approved private reporting route and supported versions. Avoid publishing a contact channel or response-time promise that has not been established.
- [ ] Add an attribution/third-party notices inventory. Do not redistribute OS fonts or bundle provider models/voices without verified permission and a documented need.
- [x] Add CI for frontend lint/typecheck/tests/build, backend tests, content validation and isolated migration checks. Do not expose secrets to untrusted contributions. Confirm the workflow passes on the release commit.
- [ ] Tag the verified commit, publish release notes and create the public repository/release after authorization. Include source/setup information; attach downloadable builds only if those exact artifacts were produced and tested.
- [x] Verify the public repository URL, license, README images, release/tag links and issue/reporting routes from a fresh reader's view. Record commit, tag, publication date and verification evidence.

### Launch materials

- [ ] Prepare one small screenshot from synthetic data and, if useful, a short captioned demo showing a real lesson, contextual reading and saved writing. Use original assets and descriptive alt text. Reuse local captures; no stock-asset or font downloads are needed.
- [ ] Record a release-specific claim sheet: shipped features, reviewed versus draft inventory, supported installation, provider requirements and known limits. Every post must agree with it and the tagged release.
- [ ] Replace every placeholder in the drafts below with the verified repository/release URL and actual release details. Keep unsupported audio, AI, proficiency, pronunciation and handwriting claims out of the copy.
- [ ] Finalize LinkedIn, Reddit and X versions for the maintainer's voice. Verify current platform/composer constraints and the selected subreddit's rules during execution; no current policy check is claimed by this offline planning update.
- [ ] Obtain authorization for the exact final posts and destination accounts/communities before posting. Record the live URLs and date/time after confirmed publication; drafts and failed requests never count as published.
- [ ] Run the short follow-up campaign below, track actual feedback and route reproducible problems into GitHub issues without copying private learner data.

## Intended implementation areas

Repository-root community/license files, .github workflows/templates, README, a small public docs/media directory, release notes and launch records linked from this phase. Reuse existing setup, validation and screenshot tooling. Do not create a second application or deployment stack for marketing.

## Data and API contracts

No learning schema or application API change is required by this phase. Use isolated fixtures for examples and public screenshots. Any implementation that does change durable data still needs its owning migration/tests. Keep credentials in the platform's approved authentication mechanism, outside version control. The public source release must preserve unrestricted study and optional providers.

## Marketing run

The maintainer owns publication and replies. Choose calendar dates after the release URL and install instructions are verified; the offsets below are a suggested sequence, not automatic scheduled posts.

1. **Before launch:** finish the claim sheet, installation check, synthetic screenshots, three platform drafts and destination-rule checks. Replace placeholders and review the complete public package.
2. **Day 0:** publish the authorized GitHub release and confirm its links. Share the LinkedIn launch post with one real screenshot and a clear invitation to try the project or contribute.
3. **Day 1:** adapt the Reddit draft for one relevant community that permits the post. Disclose creator involvement, give enough useful detail in the post itself and ask a specific feedback question. Do not bulk-cross-post or send unsolicited direct messages.
4. **Day 2:** share the concise X post with the repository link and optional small demo. Verify the final text/media in the publishing composer.
5. **Days 3–7:** answer relevant replies, reproduce installation/content issues, label contributions and publish fixes with changelog entries. Share a follow-up only when there is a real update worth reporting.
6. **End of week:** record available GitHub views/clones/stars, platform impressions/link clicks where available, issue quality and successful installation feedback. Mark unavailable metrics unknown; record counts without inventing attribution or targets. Summarize actual learning and next fixes.

Success means a usable public repository and useful feedback, not a promised number of stars or followers. No paid campaign, tracking pixel or learner-data collection is part of this plan.

## Launch post drafts

These are future launch drafts, not publication claims today. Use them only after the repository is public and their statements match the verified release. [GITHUB_URL] must be replaced; a release-specific limitation note must accompany any screenshot of draft material.

### LinkedIn

I’m sharing Trilingo, an open-source project for learning Japanese on your own computer.

It brings together contextual kana/kanji reading, typed exercises and saved writing drafts. Study is self-directed: you can choose a lesson, retry, use support and continue after mistakes. Core lessons work without an AI provider.

The release notes explain what is ready, which course material is reviewed or still draft, and what needs more work. The README includes the tested setup steps.

I’d welcome feedback from Japanese learners, developers and qualified Japanese-language reviewers, especially on installation, accessibility and content accuracy.

Source and release notes: [GITHUB_URL]

If you try it, tell me where you got stuck or which part helped you practice.

### Reddit

**Draft title:** Trilingo: an open-source Japanese practice app with local progress and unrestricted study

I’m the creator of Trilingo, a local-first Japanese learning project. I wanted a way to choose what to practice, make mistakes and keep going, with progress saved on my own computer.

The current release includes contextual kana/kanji reading, typed exercises and a writing workspace with saved drafts. Core lessons work without AI. The repository includes setup instructions, release notes and the current limitations; reviewed content and draft practice are labeled separately.

I’d particularly like feedback on beginner clarity and Japanese input/accessibility. If you install it, which part of the setup or first practice session is confusing? Qualified content corrections are welcome too; draft material should not be treated as reviewed instruction.

Repository: [GITHUB_URL]

Adapt the title/body to the chosen community. Remove or change the link/promotion format if its rules require that, and obtain moderator permission when those rules call for it. Do not post where project promotion is prohibited.

### X

Trilingo is open source: local Japanese practice with kana/kanji reading, typed exercises and saved writing drafts. Core lessons work without AI. Try it or help improve the course: [GITHUB_URL]

Verify final length and link preview in the publishing composer. If the release remains a preview, add that label and shorten the copy as needed.

## Tests and manual verification

- [ ] Run frontend lint, typecheck, tests and production build; backend tests; content validation; clean and populated migration checks; and API smoke on the release commit using isolated databases. Reuse Phase 10 evidence only when the exact commit/artifacts still match.
- [ ] Follow the public README from a fresh isolated checkout using the supported runtime. Install/download dependencies only on an authorized connection/budget; do not retry downloads on the current metered connection.
- [ ] Review the staged files and any existing history for secrets/private data, confirm license/attribution coverage and verify ignore rules using representative sensitive paths.
- [ ] Open the public repository and release as a new reader, confirm the Trilingo name appears consistently in repository identity, README, release titles/assets and launch materials, confirm images/links work, and distinguish source availability from any tested downloadable build or hosted demo.
- [ ] Check that each platform draft describes shipped behavior and actual reviewed/draft coverage. Remove placeholder text, unverified claims and private screenshot details before publication.
- [ ] Verify the exact final post, account/community, policy fit, link and media before the authorized publishing action. Confirm a live URL afterward; record failures honestly.
- [ ] Complete the follow-up log using actual issue/feedback links and available metrics. No app tests, public upload or social posting were performed merely by drafting this phase.

## Completion gate

Complete when the clean, licensed repository and a verified tagged release are publicly accessible; a new user can follow the documented setup; community/contribution/reporting paths work; and the authorized LinkedIn, Reddit and X launch posts plus week-one follow-up are recorded with live links and truthful results. If a channel is unavailable, not authorized or disallowed by its rules, leave that channel open and record it for the user's decision. Do not bypass earlier content/release gates or mark draft marketing copy as a completed campaign.

## Planning update verification — 2026-10-23

This update changes documentation only. The roadmap, README, curriculum references and Phase 10 handoff include Phase 11; existing implementation completion gates remain unchanged. An independent reader check found no material ambiguity in the publication requirements, authorization boundary, platform drafts, campaign sequence or completion gate. The project name is confirmed as Trilingo. The GitHub owner/account, code license and final publishing dates remain execution-time decisions.

Local validation command: PowerShell inline Python via `.\.venv\Scripts\python.exe -` checks eleven ordered phase files, required sections, local Markdown links, planned status and draft post coverage. Application tests/build/migrations and live platform checks were not run for this documentation-only change. No downloads, uploads or external messages were made.

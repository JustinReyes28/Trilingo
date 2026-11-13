# Third-Party Notices

Trilingo's source code is licensed under the MIT License. Authored course content
and the bundled reference-audio performances are licensed under CC BY 4.0. This
file records the third-party tools and models used to prepare those assets.

## Kokoro-82M

- **Model:** Kokoro-82M v1.0, by hexgrad
- **License:** Apache License 2.0
- **Source:** https://huggingface.co/hexgrad/Kokoro-82M
- **Voices used:** `jf_alpha` (Japanese, female) and `af_heart` (American English, female)
- **Training-data attribution:** the Kokoro-82M model card lists
  [Koniwa `tnc`](https://github.com/koniwa/koniwa) audio under CC BY 3.0 and
  [SIWIS](https://datashare.ed.ac.uk/handle/10283/2353) audio under CC BY 4.0 in
  the v1.0 training set. The per-voice table is in
  [VOICES.md](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md).
- **Bundled output:** generated MP3 performances of Trilingo-authored text only.
  Trilingo does not redistribute Kokoro model weights, voice packs or training
  audio.

## Kokoro-FastAPI

- **Project:** Kokoro-FastAPI, by remsky
- **License:** Apache License 2.0
- **Source:** https://github.com/remsky/Kokoro-FastAPI
- **Use:** historical/maintainer build-time synthesis service used to pre-generate
  the committed `content/audio/` MP3 pack. It is not shipped with Trilingo, there
  are no runtime TTS adapters or endpoints, and neither runtime study nor CI requires it.

## Python and JavaScript dependencies

Runtime and development dependencies are declared in
[`backend/requirements.lock`](backend/requirements.lock) and
[`frontend/package-lock.json`](frontend/package-lock.json). Their licenses remain
with their respective authors.

- **Build/check-script dependency (`mutagen`):** `mutagen==1.47.0`
  (`GPL-2.0-or-later`) is pinned in
  [`backend/requirements.lock`](backend/requirements.lock) solely for the
  offline audio-pack build and validation scripts
  ([`scripts/build_audio_pack.py`](scripts/build_audio_pack.py) and
  [`scripts/check_audio_pack.py`](scripts/check_audio_pack.py)). It is not
  imported by `backend/app/` runtime code and must be omitted or
  license-reviewed before bundling a standalone runtime package (such as a
  Windows EXE).

# JERRY — AI Desktop Assistant

**Status:** 🟡 In Development
**Repo:** https://github.com/mayson208/JERRYBOT
**Local:** `C:\Users\Rachel\Desktop\Coding\jerry`

---

## Overview
JERRY is Rachel's personal AI desktop assistant. Named after and inspired by her real friend Jerry. The goal is a voice-controlled, always-on HUD companion that feels personal — eventually using a clone of the real Jerry's voice.

---

## Tech Stack
| Layer | Tool |
|-------|------|
| Language | Python 3.12 |
| UI | PyQt5 (dark futuristic HUD) |
| Wake Word | Porcupine ("Hey Jerry") |
| Speech-to-Text | OpenAI Whisper |
| Brain | Claude API (Anthropic) |
| Text-to-Speech | ElevenLabs |
| PC Control | pyautogui, pycaw |

---

## Architecture
| File | Role |
|------|------|
| `main.py` | PyQt5 UI, orb animation, HUD overlay, pipeline |
| `brain.py` | Claude API, conversation memory |
| `voice.py` | ElevenLabs TTS, async playback |
| `listener.py` | Porcupine wake word + Whisper STT |
| `controller.py` | PC actions (volume, apps, keyboard) |
| `config.py` | Settings, .env loading |

---

## UI Design
- Animated glowing orb (idle / listening / thinking / speaking states)
- Color coded states: blue (idle), cyan (listening), orange (thinking), green (speaking)
- Always-on-top HUD overlay pill in bottom-right corner
- Real-time conversation transcript
- "Clear Memory" button

---

## Current Status
- [x] Full scaffold built
- [x] Pushed to GitHub
- [x] CLAUDE.md added
- [ ] API keys filled in `.env`
- [ ] Jerry's voice cloned in ElevenLabs
- [ ] Full pipeline tested end-to-end

---

## Next Steps
1. Fill in `.env` with real API keys
2. Clone Jerry's voice in ElevenLabs → update `ELEVENLABS_VOICE_ID`
3. Test: wake word → STT → Claude → ElevenLabs → UI

---

## API Key Locations
All keys in `.env` at project root (gitignored):
- `ANTHROPIC_API_KEY`
- `ELEVENLABS_API_KEY`
- `ELEVENLABS_VOICE_ID`
- `PORCUPINE_ACCESS_KEY`

# JERRY — AI Desktop Assistant

**Status:** 🟡 Built — waiting on API keys
**Repo:** https://github.com/mayson208/JERRYBOT
**Local:** `C:\Users\Rachel\Desktop\Coding\jerry`

---

## What It Is
JERRY is Rachel's personal AI desktop assistant. Named after and inspired by her real friend Jerry. Voice-controlled, always-on HUD companion — eventually using a clone of the real Jerry's voice via ElevenLabs.

---

## Tech Stack

| Layer | Tool |
|-------|------|
| Language | Python 3.12 |
| UI | PyQt5 (dark futuristic HUD) |
| Wake Word | Porcupine ("Hey Jerry") — auto-loads `hey_jerry.ppn` if present |
| Speech-to-Text | OpenAI Whisper (runs locally) |
| Brain | Claude API — `claude-sonnet-4-20250514` |
| Text-to-Speech | ElevenLabs (fallback: Windows SAPI via pyttsx3) |
| PC Control | pyautogui, pycaw |

---

## Architecture

| File | Role |
|------|------|
| `main.py` | PyQt5 UI, orb animation, HUD overlay, pipeline orchestration |
| `brain.py` | Claude API, persistent conversation memory (memory.json) |
| `voice.py` | ElevenLabs TTS + Windows SAPI fallback |
| `listener.py` | Porcupine wake word + Whisper STT |
| `controller.py` | PC actions: apps, games, volume, timer, screenshots, history |
| `config.py` | All settings loaded from `.env` with sensible defaults |

---

## What It Can Do (Current Features)

- **Open apps** — Chrome, Spotify, Discord, File Explorer, Notepad, etc.
- **Launch games** — Steam, Ubisoft, Epic, EA — searches by name across all launchers
- **Search the web** — opens Google in default browser
- **Take screenshots** — saves timestamped PNG to Desktop
- **Tell time/date** — natural language response
- **Control volume** — set, raise, lower, mute individual apps (e.g. "lower Spotify")
- **Set timers** — "Set a 10 minute timer" → fires callback when done
- **Command history** — recalls last 20 commands this session
- **Save conversation** — exports full chat to timestamped .txt on Desktop
- **Memory summarization** — compresses old messages to save tokens while preserving context
- **Speak without keys** — falls back to Windows SAPI voice when ElevenLabs isn't configured
- **Custom wake word** — auto-loads `hey_jerry.ppn` if present; falls back to "bumblebee"

---

## Configuration (`.env`)

All tuneable settings are `.env`-overridable — no code changes needed:

```
ANTHROPIC_API_KEY=
ELEVENLABS_API_KEY=
ELEVENLABS_VOICE_ID=
PORCUPINE_ACCESS_KEY=
OPENAI_API_KEY=          # optional — future Whisper API fallback

AI_MODEL=claude-sonnet-4-20250514
WAKE_WORD=hey jerry
WHISPER_MODEL=base
MEMORY_MAX_MSGS=200
SAMPLE_RATE=16000
RECORD_SECONDS=8
SILENCE_THRESHOLD=500
```

---

## UI Design

- Animated glowing orb — state-coded: blue (idle) → cyan (listening) → orange (thinking) → green (speaking)
- Always-on-top HUD pill in bottom-right corner
- Real-time conversation transcript
- "Clear Memory" button

---

## Progress Checklist

- [x] Full scaffold built
- [x] Pushed to GitHub (https://github.com/mayson208/JERRYBOT)
- [x] CLAUDE.md added
- [x] Command history + timer system
- [x] Conversation export + memory summarization
- [x] All settings .env-overridable
- [x] Windows SAPI fallback TTS (works without ElevenLabs keys)
- [x] hey_jerry.ppn auto-load system
- [x] requirements.txt organized with version pins + pyttsx3
- [ ] API keys filled in `.env`
- [ ] Jerry's voice cloned in ElevenLabs → `ELEVENLABS_VOICE_ID` updated
- [ ] hey_jerry.ppn downloaded from console.picovoice.ai
- [ ] Full pipeline tested end-to-end

---

## Next Steps

1. Fill in `.env` with real API keys (Anthropic, ElevenLabs, Porcupine)
2. Clone Jerry's voice → see [[../04-Ideas/Jerry-Voice-Clone]]
3. Download `hey_jerry.ppn` from console.picovoice.ai → place in project root
4. Run `pip install -r requirements.txt` → `python main.py`
5. Test full pipeline: wake word → STT → Claude → ElevenLabs → UI response

---

## Related

- [[../04-Ideas/Jerry-Voice-Clone]] — Voice cloning plan and ElevenLabs steps
- [[../07-Reference/API-Key-Locations]] — Where to find/store all keys

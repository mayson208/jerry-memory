# YouTube AI Studio (STUDIO) — One-Click YouTube Automation

**Status:** 🟢 App built — needs channel strategy + API keys
**Repo:** https://github.com/mayson208/AiAutomationTool
**Local:** `C:\Users\Rachel\Desktop\Coding\AiAutomationTool`
**Long-term goal:** Launch as a SaaS product

---

## What It Is
A Flask web dashboard that automates the entire YouTube content pipeline. Input a topic → get a script, voiceover, thumbnail, stock footage, SEO package, and calendar — all AI-generated.

---

## What's Built (Current Features)

### Core Pipeline
- **One-Click Pipeline** — full end-to-end: script → voiceover → thumbnail → footage → (upload)
- **Script Writer** — Claude-generated scripts with niche-specific tone/hooks/retention triggers
- **Hook Generator** — generates 3 hook options (shock/question/story) before writing full script
- **Humanizer pass** — makes AI scripts sound natural

### Individual Tools
- **Voiceover** — ElevenLabs TTS with per-niche voice settings (stability, similarity, style)
- **Thumbnail** — DALL-E generated with niche-specific style presets
- **Stock Footage** — Pexels API with smart keyword generation
- **SEO & Metadata** — Claude generates 5 title options, full description, 20–25 tags, chapter suggestions, SEO score
- **Content Calendar** — 30-day schedule with topic bank and posting frequency by niche
- **Compliance** — AI disclosure text, script policy checker (risk score), music license checker
- **Voice Library** — ElevenLabs voice management, per-niche voice presets, A/B preview
- **Analytics** — CPM reference table, revenue estimator (monthly + annual projections)
- **History** — session log of generated content
- **Export** — CSV/TXT export for calendars and topic banks

### Quality & Infrastructure
- **Centralised logging** — daily rotating logs (`studio_logger.py`, 7-day retention)
- **Security headers** — X-Content-Type-Options, X-Frame-Options, X-XSS-Protection, Referrer-Policy
- **Health endpoint** — `/health` returns key status and config validation
- **Unit tests** — pytest suite for compliance, SEO, config (runs without API keys)
- **Copy buttons** — one-click copy for all generated text fields
- **Revenue estimator** — interactive calculator on analytics page

---

## Supported Niches

| Niche | CPM | Notes |
|-------|-----|-------|
| Finance & Investing | $15–50 | Top earner |
| Tech & Business | $12–25 | |
| Health & Wellness | $8–20 | |
| Science & Space | $6–12 | |
| History | $5–10 | |
| Self Improvement | $5–10 | |
| True Crime | $4–9 | |
| Facts / Did You Know | $4–10 | |
| Motivational & Quotes | $5–10 | |
| Horror & Scary Stories | $3–7 | |
| Top 10 Lists | $4–8 | |
| News Summary | $4–8 | |
| Meditation & Sleep | $3–6 | |
| Roblox Gaming | $2–4 | ⚠️ $0.30 if Made for Kids label |

---

## Tech Stack

| Task | Tool |
|------|------|
| Backend | Python 3.12, Flask |
| Script generation | Claude API (Anthropic) |
| Voiceover | ElevenLabs |
| Thumbnail | DALL-E (OpenAI) |
| Stock footage | Pexels API |
| Video assembly | MoviePy / FFmpeg |
| Upload | YouTube Data API v3 |
| Frontend | Jinja2 templates, vanilla JS |

---

## SaaS Plan (Long-term)

- **Freemium** — limited videos/month free
- **Pro** — unlimited + custom voice + batch scheduling
- **Agency** — multi-channel, white-label
- Target: solo creators, marketers, content agencies

---

## What's Still Needed

- [ ] Real API keys in `.env` to run end-to-end
- [ ] Test full pipeline with real content
- [ ] Choose first niche for channel launch
- [ ] YouTube Data API v3 credentials (for auto-upload)
- [ ] Domain + hosting decision for SaaS launch

---

## Niche Strategy (Research Complete)

Three niches have been deeply researched — see Research Library:

| Niche | Rating | Start Here? |
|-------|--------|-------------|
| [[../02-Research/YouTube-AI-Automation/12-Indus-Valley-Niche-Deep-Research\|Indus Valley]] | ⭐⭐⭐⭐⭐ 9/10 | **Yes — live news hook now** |
| [[../02-Research/YouTube-AI-Automation/11-Mesopotamia-Niche-Deep-Research\|Mesopotamia]] | ⭐⭐⭐⭐ 8.5/10 | Strong second option |
| [[../02-Research/YouTube-AI-Automation/10-Roblox-Niche-Deep-Research\|Roblox]] | ⭐⭐⭐ 8/10 | Good but MFK risk |

---

## Related

- [[../02-Research/YouTube-AI-Automation/01-Overview]] — Full pipeline research
- [[../02-Research/YouTube-AI-Automation/09-STUDIO-App-Research]] — SaaS market research

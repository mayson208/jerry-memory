# Viewmax.io — Research Notes
**Date:** 2026-03-24
**Purpose:** Understand viewmax.io for potential use in YouTube AI Studio project

---

## 1. What Is Viewmax.io?

Viewmax.io bills itself as **"The AI Tool Suite for Creating Viral Videos."** It is a web-based, subscription AI platform designed for short-form social media content — TikTok, YouTube Shorts, and Instagram Reels. The core pitch is that top creators replicate what already works, and Viewmax gives you the tools to do that fast.

**Official site:** https://www.viewmax.io/
**Key claim:** Powered by Sora 2 (OpenAI's video generation model), no watermarks on output.

### Who It's For
- Solo creators and small content teams
- Faceless channel operators needing to post 5+ videos/week
- Social media marketers and digital entrepreneurs
- Founders who can't maintain a full production team

---

## 2. Core Features

| Feature | Description |
|---|---|
| **Sora 2 AI Video Generator** | Text-to-video using OpenAI's Sora 2 model; no watermarks on output |
| **Sora 2 Pro** | 1080p resolution; available on Creator+ plan only |
| **AI Scriptwriter** | Paste a concept or YouTube URL, get a script back |
| **AI Voiceover** | Multiple TTS voice options; character limits per plan |
| **Auto-Captions** | Automatic caption generation with preset styles from top channels |
| **Caption Remover** | Strip hardcoded captions from existing videos |
| **Watermark Remover** | Clean watermarks off third-party video clips |
| **YouTube Downloader** | Pull videos directly by URL for repurposing (Pro+ plans) |
| **Caption Presets** | Library of styles modeled from top-performing TikTok/Reels channels |
| **Tutorial Library** | 25+ modules, 4+ hours of training content (built-in) |
| **Weekly Group Calls** | Coaching calls on Creator+ plan |
| **AI Upscaler** | Upcoming feature — not yet launched |

---

## 3. Prompt Format for Sora 2 Video Generation

Viewmax uses OpenAI's Sora 2 under the hood. The prompt field accepts a plain-text description of the video you want. There is no strict form with labeled fields — it is one open text box. However, based on OpenAI's Sora 2 Prompting Guide and what's documented about Viewmax's implementation:

### What the Prompt Should Cover (in order)

1. **Scene/Setting** — Characters, location, weather, time of day
2. **Style anchor** — Visual aesthetic; e.g., "cinematic 1970s film," "IMAX-scale realism," "16mm black-and-white," "high-end TV commercial"
3. **Camera framing** — Shot type (wide, medium, close-up), depth of field, lens choice
4. **Action beats** — Specific numbered or bulleted movements (e.g., "takes 4 steps to window, pauses, turns")
5. **Lighting** — Describe quality AND color: "soft window light, warm lamp fill, cool rim from hallway"
6. **Dialogue** (optional) — Place on a separate line below the visual description; keep lines brief and natural
7. **Sound/ambiance** (optional) — Background cues

### API Parameters (Set Outside the Prompt Box)
- **Model:** `sora-2` or `sora-2-pro` (Pro only on Creator+ plan)
- **Resolution:** 720x1280 (portrait/9:16), 1280x720 (landscape), or up to 1920x1080 (sora-2-pro)
- **Duration:** 4–20 seconds per clip

### Prompt Length Tradeoff
- **Short prompt** = more creative freedom for the model, surprising results
- **Long/detailed prompt** = more control, but model may not follow all guidance reliably
- Best practice: aim for 1–3 sentences; be visual and specific without overloading

---

## 4. Best Practices for Writing Prompts

### Core Principles (Sora 2 via Viewmax)

**Think like a cinematographer, not a novelist.**
Write as if sketching a storyboard frame. State: framing → action → lighting → palette.

**Replace vague with concrete.**
- Bad: "Beautiful street at night"
- Good: "Wet asphalt, zebra crosswalk, neon signs reflecting in puddles, shallow depth of field"

- Bad: "Person moves quickly"
- Good: "Cyclist pedals three times, brakes hard, stops at edge of crosswalk"

**One camera move + one subject action per clip.**
Complexity compounds errors. Keep each 4–8 second clip to one clear action.

**Name your color palette.**
Specify 3–5 anchor colors to maintain visual consistency across clips you'll stitch together.
Example: "warm amber tones, deep shadow blacks, muted sage green"

**Use style keywords early.**
The aesthetic framing anchors everything that follows. Put it in the first sentence.
- "Cinematic 4K close-up..."
- "Shot on 16mm film, 1980s aesthetic..."
- "Hyper-realistic product photography style..."

**Short clips stitch better.**
Two 4-second clips often look better than one 8-second clip. Generate individual shots, then edit them together in Viewmax's editor.

**Dialogue handling.**
Write dialogue in a block separated from the visual description. Keep lines short. 4-second clip = 1–2 exchanges max.

**Iterate one element at a time.**
When editing/regenerating, change one thing: "same shot, switch to 85mm lens" — not "change everything."

**If generation fails, simplify.**
Freeze the camera, reduce action complexity, plain background. Get a clean baseline, then add layers.

---

## 5. Example Prompts

### Faceless Lifestyle / Motivational (TikTok style)
```
Cinematic close-up of hands typing on a MacBook in a dimly lit café at 2am. Warm amber lamp light, dark background. Shallow depth of field. Coffee steam rises slowly in foreground. Slow motion. Style: high-end lifestyle commercial.
```

### Nature / Relaxing / Lo-fi
```
Aerial drone shot descending slowly toward a misty Japanese forest at dawn. Soft diffused light filtering through cedar trees, pale blue-green tones. Dew on leaves in foreground. No people. Style: cinematic 4K nature documentary.
```

### Product Showcase
```
Slow push-in on a minimalist skincare bottle sitting on white marble. Warm golden-hour window light from the right, casting long soft shadows. Water droplets on the bottle surface. Color palette: ivory, warm gold, muted gray. Style: luxury beauty commercial, shallow depth of field.
```

### Dramatic Storytelling / Narration
```
Wide shot of a lone figure standing at the edge of a cliff overlooking a stormy ocean at sunset. Cinematic 2.35:1 aspect ratio framing. Warm orange sky, dark silhouette. Wind blowing jacket. Camera holds still. Style: epic film opening sequence, anamorphic lens flare.
```

### Tech / AI Content
```
Extreme close-up of a circuit board with electric blue light pulsing through pathways. Camera slowly pulls back to reveal the board is inside a glowing humanoid silhouette. Dark background, teal and electric blue palette. Style: sci-fi short film, 4K CGI-realistic.
```

---

## 6. Video Styles and Formats Supported

### Aspect Ratios / Platform Formats
- **9:16 vertical** — TikTok, Instagram Reels, YouTube Shorts (primary use case)
- **16:9 horizontal** — YouTube standard
- **1:1 square** — Instagram feed (less common)

### Resolution Tiers
- **720p** — Basic and Professional plans
- **1080p** — Creator+ Workshop plan (Sora 2 Pro required)

### Visual Styles That Work Well in Sora 2
- Cinematic realism (film-like depth, natural lighting)
- Hyper-realistic product/lifestyle content
- Nature and atmospheric footage (mist, water, forests)
- Abstract motion graphics / sci-fi aesthetic
- Slow motion / time-lapse style descriptions
- 16mm/film grain aesthetic
- Luxury commercial style

### Duration
- 4–20 seconds per generated clip
- Longer videos built by stitching clips in editor

---

## 7. Workflow Inside Viewmax

1. **Start** — Choose: blank prompt, pre-built template, or import YouTube URL
2. **Script** — Use AI Scriptwriter (describe concept → get script) or write your own
3. **Generate video** — Enter Sora 2 prompt; add motion/effects guidance
4. **Voiceover** — Select AI voice, paste script, generate narration
5. **Captions** — Auto-generate; apply a caption preset from top creators
6. **Edit** — Trim, cut, layer effects, adjust timing
7. **Export** — Platform-specific export (TikTok, Reels, Shorts)

---

## 8. Pricing (as of early 2026)

| Plan | Price/mo (annual) | Credits | Sora Videos | Exports | Notes |
|---|---|---|---|---|---|
| Basic | $14 | 200 | ~33 | 100 | Sora 2, 720p |
| Professional | $18 | 350 | ~66 | 175 | + YouTube downloader, Discord |
| Creator+ Workshop | $49 | 800 | ~150 | 400 | Sora 2 Pro, 1080p, group calls, coaching |

Credits are consumed by: Sora video generation, voiceover characters, caption removals, exports.

---

## 9. Honest Assessment / Limitations

### What It's Good At
- Fast end-to-end pipeline for faceless short-form content
- All-in-one: scripting + video + voice + captions + export in one place
- Good for creators who need to post daily without a production team
- Watermark and caption removal is genuinely useful for repurposing content
- Tutorial library and coaching calls (Creator+) are a real differentiator

### Known Limitations (from reviews and comparisons)
- **Voice quality is basic TTS** — robotic prosody hurts viewer retention (28–35% completion vs 45%+ target)
- **Template library is small** (~30–50 templates) — can cause audience fatigue from repetitive look
- **No Reddit/Twitter story ingestion** — must manually format scripts for "Reddit story" style videos
- **No direct platform API upload** — you export and upload manually
- **No analytics/retention tracking** — no feedback loop built in
- **Export caps** can block high-volume creators without upgrading
- **Sora 2 generation can fail** on complex or vague prompts — requires very specific descriptors
- **Trust score controversy** — Scam Detector rates it 38.2/100; Scamadviser is more favorable at 61/100 — not a scam, but legitimacy questions exist among some reviewers
- **At least one Trustpilot review** (March 2026) advises against paying for the platform

### Best Use Case
Casual testing, single-platform creators under 10 videos/month, or creators wanting an all-in-one starter kit. NOT the best fit for high-volume monetization-focused channels without supplementing with better TTS and custom automation.

---

## 10. Community Resources

- **TikTok tutorials** — Multiple creators have made "how to use viewmax.io" content; search TikTok: "viewmax io tutorial"
- **Discord** — Included with Professional and Creator+ plans; community of creators
- **In-app tutorial library** — 25+ modules, 4+ hours
- **Weekly coaching calls** — Creator+ plan only
- **Trustpilot reviews** — https://uk.trustpilot.com/review/viewmax.io
- **Clippie.ai comparison article** — Good breakdown of limitations: https://clippie.ai/blog/viewmaxio-alternative-viral-faceless-short-form-content-2026
- No significant Reddit thread presence found as of March 2026

---

## 11. Sora 2 Prompt Reference (Since Viewmax Uses It)

Full official guide: https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide

**Quick reference structure:**
```
[Style anchor]. [Scene description — characters, setting, weather].
[Camera framing and depth of field]. [Action beats — numbered if multiple].
[Lighting quality and color]. [Color palette: 3-5 colors].
[Optional: Dialogue on a new line].
[Optional: Ambient sound cue].
```

**Example using this structure:**
```
Cinematic slow-motion shot. Young woman walks alone through a neon-lit Tokyo alley at 2am, rain falling.
Close-up tracking shot, shallow depth of field, 50mm equivalent.
1. She pauses at a vending machine. 2. Reaches out and presses a button. 3. Looks at her reflection in the glass.
Soft neon pink and teal bounce light, deep shadows underlit.
Palette: neon pink, electric teal, near-black, wet asphalt gray.
```

---

## 12. Using Viewmax for Ranking / Countdown Videos (Added 2026-03-24)

Ranking/countdown videos are one of the best-fit use cases for Viewmax because the format is fully faceless, script-driven, and repeatable — exactly what the platform is built for.

### Recommended Workflow for a Ranking Short

**Scriptwriter prompt format:**
```
Create a 45-second YouTube Shorts script in countdown format.
Topic: [Top 5 Strongest Militaries in the World]
Format: Hook → #5 → #4 → #3 → #2 → #1 reveal → CTA asking viewers if they agree
Tone: authoritative, fast-paced, punchy
One key fact per entry. Tease the #1 throughout. End with "Comment below if you agree."
```

**Sora 2 prompt examples for ranking content:**

For a country/military ranking entry:
```
Cinematic aerial shot over a military parade ground at golden hour. Rows of soldiers in formation, tanks in background. National flag waving in foreground. Style: photorealistic 4K documentary. Color palette: green, gold, deep shadow black. Camera holds wide, slow zoom in.
```

For a sports ranking entry:
```
Slow-motion close-up of a soccer player striking a ball. Stadium crowd blurred in background. Dynamic lens flare. Style: high-end sports broadcast, 4K. Color palette: team jersey colors, bright green pitch, blue sky. Camera: tracking shot following the ball.
```

For a historical ranking entry:
```
Wide establishing shot of ancient stone ruins at dusk. Dramatic orange-red sky. No people. Stone columns in foreground. Camera slowly pushes forward. Style: cinematic historical documentary. Color palette: warm amber, dusty gray, deep orange.
```

### Known Gaps for This Use Case
- No bar chart race / animated data visualization tool — Viewmax is not built for the "countries by GDP animated chart" subformat
- The AI scriptwriter may need specific prompting to produce the exact countdown tone — test and iterate
- TTS voice quality may limit viewer retention vs. ElevenLabs; consider exporting script + Sora visuals from Viewmax, then adding ElevenLabs voiceover externally

---

## Sources

- https://www.viewmax.io/
- https://www.viewmax.io/pricing
- https://www.techrevv.com/from-ideas-to-viral-videos-how-viewmax-io-helps-creators-go-social-fast/
- https://clippie.ai/blog/viewmaxio-alternative-viral-faceless-short-form-content-2026
- https://aifounderkit.com/ai-tools/viewmax-ai-video-editor/
- https://www.browse-ai.tools/tool/viewmax
- https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide
- https://www.youngurbanproject.com/sora-prompts-for-ai-video-generation/
- https://viewmaxio.com/
- https://uk.trustpilot.com/review/viewmax.io

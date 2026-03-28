# Memecoin Trading Research — Axiom (Solana)
**Date:** 2026-03-27
**Platform Focus:** axiom.trade (Solana)
**Purpose:** Practical trading reference for finding coins early before pump

---

## Table of Contents
1. [Axiom Platform — Complete Overview](#1-axiom-platform--complete-overview)
2. [How Early Traders Find Coins](#2-how-early-traders-find-coins)
3. [Key On-Chain Metrics](#3-key-on-chain-metrics)
4. [Pump.fun Ecosystem & Bonding Curve](#4-pumpfun-ecosystem--bonding-curve)
5. [Red Flags & Rug Pull Detection](#5-red-flags--rug-pull-detection)
6. [Pro Trader Tool Stack](#6-pro-trader-tool-stack)
7. [Alpha Sources](#7-alpha-sources)
8. [Winning Patterns — What 10x-100x Coins Have in Common](#8-winning-patterns--what-10x-100x-coins-have-in-common)
9. [Tokenomics — Good vs Bad](#9-tokenomics--good-vs-bad)
10. [Risk Management](#10-risk-management)
11. [Solana-Specific Mechanics](#11-solana-specific-mechanics)
12. [Narratives & Meta — What's Hot](#12-narratives--meta--whats-hot)
13. [Copy Trading](#13-copy-trading)
14. [KOL Calls — Key Opinion Leaders](#14-kol-calls--key-opinion-leaders)
15. [Timing the Market](#15-timing-the-market)
16. [Quick Reference Cheat Sheet](#quick-reference-cheat-sheet)

---

## 1. Axiom Platform — Complete Overview

**Website:** https://axiom.trade
**Type:** Browser-based, non-custodial Solana DEX aggregator + trading hub
**Founded:** Early 2024 by two UC San Diego grads; accepted into Y Combinator Winter 2025
**Market Share:** 72% of Solana bot trading volume by July 2025 (up from 2% in February 2025)
**Volume:** $10.5B+ cumulative in first 129 days; $100M+ revenue; 110M+ transactions; 382,500+ unique wallets

### Fees
| Tier | Fee | Cashback |
|------|-----|----------|
| Wood (default) | 0.95% | 0.05% |
| Diamond | 0.80% | 0.20% |
| Champion | 0.75% | 0.25% |

- Priority fees: 0.001 SOL default (increase to 0.03–0.1 SOL for sniping)
- Validator bribe: 0.001 SOL default (increase for competitive launches)
- Referral code gives 10% discount on fees

### Core Modules

#### Pulse Module (Token Discovery)
The most important discovery tool on Axiom. Real-time dashboard with three feeds:
- **New Pairs** — Freshly launched tokens with detected liquidity; catch tokens in first minutes
- **Final Stretch** — Tokens approaching Raydium/PumpSwap graduation (~$69K market cap); often spike on graduation
- **Migrated** — Tokens that just graduated to DEX; more liquid but already moved

**Recommended New Pairs Filters:**
- Min holders: 50
- Min age: 3 minutes
- Max age: 30 minutes
- Min volume: $20,000
- Min transactions: 100
- Dev holdings: max 20%
- Sniper activity: below 10%
- Bundle %: check and avoid >15%

**Graduation/Final Stretch Filter:**
- Min market cap: $20,000
- Max age: 18 minutes

**Other Available Filters:**
- Protocol selector: Pump.fun vs Moonshot
- Keyword include/exclude
- Top 10 holder %
- Insider ownership
- Pro Traders %
- Liquidity, volume, transaction count

#### Trackers Module (Wallet Tracking)
- Add wallet addresses manually or batch import
- Real-time buy/sell alerts when tracked wallets trade
- Floating window for multitasking
- Free for all users (paid on most other platforms)
- Twitter monitoring: track top 1,500 accounts for coin mentions

#### Vision Tool (Analytics)
- Leaderboard ranking traders by PnL, win rate, volume
- Bundle detection (insider coordination)
- Twitter verification on token accounts (detect reused scam accounts)
- Honeypot and rug risk assessment
- Security audit results displayed per token

#### Sniper Functionality
- Monitors mempool for new liquidity additions
- Executes buy in same block or next block as launch
- Built-in MEV protection via Jito routing
- Sub-second execution speed

**Sniper Settings for High-Volatility Launches:**
- Slippage: 15–30% (up to 1000% extreme cases)
- Priority Fee: 0.03–0.1 SOL
- Bribe Fee: 0.03–0.1 SOL
- MEV: Secure mode ON

**Normal Trading Settings:**
- Slippage: 10–15% for memecoins
- Priority Fee: 0.001–0.015 SOL standard
- Starting position: 0.05–0.20 SOL

#### Copy Trading
- **NOT fully automated** — Axiom uses manual copy trading
- Use Trackers to monitor wallets, manually mirror trades
- Find wallets via leaderboard or community-shared addresses
- Look for wallets with 50–70% win rate (suspicious if 75–95%)

#### Other Features
- Limit orders and market orders
- Take-Profit / Stop-Loss (TPSL) built in
- Flash Buy (one-click preset amounts)
- Hyperliquid perpetuals up to 50x leverage (USDC collateral)
- USDC staking via Marginfi (~3% APY)
- Non-custodial wallet (Turnkey infrastructure, air-gapped)
- Portfolio P&L tracking

### Geographic Restrictions
Blocked: US, mainland China, Singapore, Cuba, Iran, Iraq, North Korea, Syria, Yemen, Crimea

---

## 2. How Early Traders Find Coins

### How Early is "Early"?
- **Seconds (0–30s):** Bot snipers only; bots tap Solana's Turbine/ShredStream protocol for 200–400ms advantage before RPC confirmation
- **Minutes (1–10 min):** Human snipers using Pulse/GMGN; this is the realistic early window for retail
- **10–60 min:** Still early if coin hasn't pumped yet; check Final Stretch on Axiom
- **1–4 hours:** Momentum plays if narrative is strong; more risk of already being too late
- **Post-graduation:** Higher safety, lower ceiling

### The Actual Workflow (Manual Trader)

1. **Monitor Axiom Pulse / GMGN new token feed** — filter for coins launching with healthy metrics
2. **Spot a token that passes filters** (holders growing, volume spiking, dev wallet low)
3. **Quick safety check** — paste CA into RugCheck.xyz or use Axiom's built-in audit (30 seconds)
4. **Check holder distribution** on Solscan or Bubblemaps
5. **Check Twitter/Telegram** — is there organic buzz or is it dead?
6. **Buy small initial position** (0.05–0.1 SOL) if checks pass
7. **Watch momentum** — if volume continues and holders grow, add to position
8. **Set take-profit** at 2x, 5x, 10x and let it run or exit full

### Sources Traders Monitor
- **Axiom Pulse** — new pairs feed (best for Solana)
- **GMGN.ai** — smart money wallet tracking + new token discovery
- **Dexscreener** — trending tokens, volume spikes
- **Pump.fun** — scroll the live feed manually for new launches
- **Twitter/X CT (Crypto Twitter)** — early mentions before mainstream
- **Telegram alpha groups** — early calls (but verify before acting)
- **Wallet trackers** — GMGN, Nansen, KOLSCAN watching smart money wallets

---

## 3. Key On-Chain Metrics

### Liquidity
- **Minimum viable:** $20K–$50K liquidity to enter; below this = extreme slippage risk
- **Good:** $100K+ liquidity = can enter/exit without massive impact
- **Locked liquidity:** Should be locked or burned; unlocked = rug risk
- **Liquidity concentration:** Avoid if one pool holds >90% of liquidity (can be drained)

### Market Cap
- **Entry sweet spot (early):** $10K–$100K market cap — highest upside, highest risk
- **Mid range:** $100K–$1M — still 10x potential, less likely to rug immediately
- **Safe zone:** $1M+ — lower ceiling but more stable; graduation likely occurred

### Holder Distribution
- **Red flag:** Top 10 holders own >30% of supply
- **Danger zone:** Top 10 holders own >50% of supply — coordinated dump risk
- **Good:** Many wallets, no single wallet above 5%
- **Check:** Solscan > Token > Holders tab, or Bubblemaps.io for visual clustering

### Developer Wallet
- **Safe threshold:** Dev holds <5% of supply
- **Warning:** Dev holds >10% — can dump on you
- **Red flag:** Dev holds >20% — almost certainly will dump
- **Also check:** Has dev wallet been active in previous rug pulls? (check wallet history on Solscan)

### Bundled Buys
- **What it is:** Multiple insider wallets buying in the same block at launch to accumulate supply cheaply
- **Detection:** Axiom Vision shows "Bundle %" — avoid tokens with >15% bundled
- **Why it matters:** Bundlers hold early bags at 0 cost basis and will dump on you
- **Tools:** Axiom built-in, BullX bundle checker, GMGN

### Sniper %
- **Safe:** <10% of supply sniped at launch
- **Warning:** 10–25% sniped — heavy supply overhang
- **Red flag:** >30% sniped — launch is/was controlled; likely coordinated dump incoming
- **Note:** Snipers bought at the very bottom and can dump at any time

### Top Holder Concentration
- **Acceptable:** Top 10 holders <25% combined
- **Warning:** Top 10 holders at 25–40%
- **Red flag:** Top 10 holders >40% combined

### Bonding Curve Progress (Pump.fun)
- The closer to 100% complete (~$69K market cap), the more likely graduation pump
- "Final Stretch" = 80–99% complete on bonding curve — momentum play
- Graduation to PumpSwap/Raydium often causes 2x–5x price spike

### Volume / Transactions
- **Healthy:** Consistent volume (not just one spike), growing transaction count
- **Red flag:** Volume is all buys with no sells (fake volume), or volume concentrated in 1–3 wallets
- **Check wash trading:** If volume/market cap ratio is extremely high without holder growth, likely manipulation

---

## 4. Pump.fun Ecosystem & Bonding Curve

### How Pump.fun Works
- Anyone can deploy a token for ~0.02 SOL
- Token starts with a bonding curve (mathematical formula): price increases as supply is bought
- Bonding curve manages 800M of the 1B total token supply
- Remaining 200M goes to liquidity pool at graduation

### Bonding Curve Mechanics
- **Formula:** Price increases exponentially as more tokens are purchased
- **Think of it:** Like a vending machine that gets more expensive as inventory shrinks
- **Starting price:** Extremely low (fractions of a cent)
- **Graduation threshold:** ~$69,000 market cap (800M tokens sold on curve)
- At graduation, liquidity is automatically deployed to a DEX

### Graduation Destination (Evolved in 2025)
- **Before March 2025:** Graduated tokens went to Raydium DEX
- **After March 2025:** Pump.fun launched PumpSwap (their own native DEX)
- **PumpSwap fees:** 0.25% per trade (0.2% to LPs, 0.05% to protocol)
- Post-graduation price is set by AMM (buyers/sellers) not bonding curve

### What Graduation Means for Price Action
- Graduation = token becomes tradeable on open AMM with real liquidity
- Often causes immediate price spike (momentum + new buyers seeing DEX listing)
- Unlocks the token for DEX aggregators (Dexscreener, Birdeye listings)
- Brings in traders who only buy graduated tokens (more conservative)
- Historical pattern: 2x–5x spike on graduation, then volatile

### Key Stats (2025)
- ~98.7% of Pump.fun tokens never graduate (die on the bonding curve)
- Only ~1.3% graduate — these are the signal to watch
- Approximately 93% of graduated Raydium pools showed pump-and-dump characteristics
- Still: the 7% that run can 10x–1000x

### Timing Pump.fun Tokens
- **First 0–30 seconds:** Bot territory; human traders cannot compete without automation
- **1–5 minutes:** If volume and holders are growing, still very early for humans
- **"Final Stretch" (80–99% bonding curve):** Watch for graduation imminent; buy before or right after
- **Just graduated:** One of the best risk/reward windows — momentum + new DEX visibility

---

## 5. Red Flags & Rug Pull Detection

### Scale of the Problem (2025)
- $2.8B+ lost to rug pulls across all chains in 2025
- Majority on Solana and BSC (lowest deployment costs)
- ~98.7% of Pump.fun tokens never graduate
- 82.8% of >100% return tokens showed artificial growth strategies

### Hard Red Flags (Avoid Immediately)
- **Mint authority NOT revoked** — dev can print unlimited tokens, crashing price
- **Freeze authority NOT revoked** — dev can freeze YOUR wallet, preventing you from selling (honeypot)
- **Liquidity not locked/burned** — dev can drain the pool instantly
- **Top wallet holds >30% of supply** — one sell can destroy price
- **Dev wallet history shows previous rug pulls** — serial rugger
- **Bundle % >15%** — insiders sniped the launch
- **Sniper % >30%** — too much cheap supply ready to dump

### Moderate Red Flags (Proceed with Caution)
- Dev holds 10–20% of supply
- Sniper % 15–30%
- Top 10 holders own 25–40%
- Anonymous team with no social presence
- Twitter account is brand new (under 1 week old)
- Telegram has fake/bot engagement (lots of members, no real chat)
- No website or very low-quality copy-paste website

### Honeypot Detection
- A token you can buy but cannot sell = honeypot
- Caused by active freeze authority or contract coding tricks
- Test: Try to sell a tiny amount before putting in a full position
- Tools: BullX has built-in honeypot detection; RugCheck.xyz flags this

### Fake Volume
- Volume spike with no holder growth = wash trading
- Same 2–3 wallets trading back and forth
- Volume/market cap ratio extreme without organic community

### How to Check Safety (30-Second Workflow)
1. Copy token contract address (CA)
2. Paste into **RugCheck.xyz** — check overall risk score
3. Verify: Mint authority REVOKED ✓
4. Verify: Freeze authority REVOKED ✓
5. Verify: Liquidity LOCKED or BURNED ✓
6. Check top holders on **Solscan** (token > holders tab)
7. Check Bundle % and Sniper % on **Axiom Vision** or **GMGN**
8. Quick Twitter search of token name — organic or coordinated?

### Key Safety Tools
| Tool | Purpose |
|------|---------|
| RugCheck.xyz | Overall risk score, authority checks |
| Solsniffer | 20+ security indicators, Snifscore 0-100 |
| Bubblemaps.io | Visual holder clustering, insider detection |
| Solscan | Manual holder distribution, wallet history |
| GMGN | Bundle %, sniper %, smart money tracking |
| Axiom Vision | Built-in safety audit per token |

---

## 6. Pro Trader Tool Stack

### Charting & Discovery
| Tool | Best For | Fee |
|------|---------|-----|
| **Dexscreener** | Real-time charts, new pair discovery, trending across DEXs | Free |
| **Birdeye** | Real-time token data, wallet tracking, Solana + EVM | Free / Pro |
| **GMGN.ai** | Solana new token scanner, smart money tracking, anti-MEV | 1% fee |
| **Dextools** | Charts, pair info, older established tool | Free / Pro |

### Trading Bots / Platforms
| Tool | Best For | Fee |
|------|---------|-----|
| **Axiom.trade** | All-in-one: Pulse discovery, sniping, tracking, trading | 0.75–0.95% |
| **BullX NEO** | Multi-chain, AI analytics, copy trading, honeypot detection | 0.9% |
| **Photon** | Lightning fast Solana trading, clean UI | 1% |
| **GMGN.ai** | Telegram bot trading, sniper, copy trade | 1% |
| **Trojan Bot** (Telegram) | Fast Solana Telegram trading bot | ~1% |
| **Bonk Bot** (Telegram) | Solana Telegram bot, popular for fast entry | ~1% |

### Wallet & Smart Money Tracking
| Tool | Best For | Cost |
|------|---------|------|
| **KOLSCAN** | Track top memecoin traders and KOLs, free leaderboard | Free |
| **Nansen** | Institutional-grade wallet analytics, PnL leaderboards | Paid |
| **Axiom Trackers** | Built-in wallet tracking + Twitter monitoring | Included |
| **GMGN Monitor** | Labels wallets (KOL/whale/smart money), first-70-buyers | 1% trade fee |
| **Dune Analytics** | SQL-queryable wallet data, custom dashboards | Free / Pro |
| **Arkham Intel** | On-chain wallet identification and tracking | Free / Paid |

### Safety Checkers
| Tool | Best For |
|------|---------|
| **RugCheck.xyz** | Quick risk score, authority status |
| **Solsniffer** | 20+ indicators, Snifscore 0-100 |
| **Bubblemaps.io** | Visual insider/cluster detection |

### Pro Workflow Example
1. Spot new token on **Axiom Pulse** (New Pairs feed)
2. Check Bundle % and Sniper % in **Axiom Vision** — if clean, proceed
3. Paste CA into **RugCheck.xyz** — confirm mint/freeze revoked, LP locked
4. Check top holders on **Solscan** — confirm no >10% single wallet
5. Quick **Twitter/Telegram** check — real organic buzz?
6. **GMGN** — any smart money wallets buying?
7. Execute via **Axiom Flash Buy** with 10–15% slippage, priority fee 0.01–0.03 SOL

---

## 7. Alpha Sources

### Twitter/X Accounts to Follow (Categories)
- **CT (Crypto Twitter) analysts:** Cobie (@cobie), Miles Deutscher (@milesdeutscher)
- **Solana-specific traders:** Search "Solana memecoin" on CT, follow accounts with 10K+ followers who post CAs with track record
- **On-chain data accounts:** Whale Alert, Lookonchain
- **Warning:** Never blindly follow a KOL call — verify before buying (see Section 14)

### Telegram Communities
| Group | Focus | Size |
|-------|-------|------|
| MemeCoin Whale Pumps | Whale activity + early Solana launches | ~151K members |
| Crypto Pumps Island | Fast pump alerts | ~78K members |
| FarmercistJournal | Highly active Solana pump community | ~47K members |
| Based kook calls | Early Solana trends | ~18.8K members |
| SuperX Memecoin Copy Trading | Structured alpha signals | ~5.6K members |
| MemeCoin Daily | Large news hub, market sentiment | ~1M+ members |

### Discord Servers
- SolanaMemeCoins Discord — 38,600+ members sharing signals
- Solana Gems calls — top Solana memecoin calls
- CryptoExact — futures + memecoin community

### Finding Real Alpha vs Noise
- **High signal:** Small private groups (100–1,000 members) where admins have skin in the game
- **Low signal:** 100K+ public groups where you're the exit liquidity
- **Best approach:** Find 2–3 small, vetted groups rather than 20 large groups
- **Verify:** Check the CA yourself before buying any call — never blindly ape
- **Track record:** Follow traders who post P&L screenshots and wallet addresses openly

### On-Chain Alpha
- Watch GMGN "Top Snipers" and "KOL wallets" buy activity
- If 3+ smart money wallets buy the same token within minutes = strong signal
- Use KOLSCAN to identify wallets with 70%+ win rates
- Axiom Trackers: follow 5–10 smart money wallets, get buy alerts

---

## 8. Winning Patterns — What 10x–100x Coins Have in Common

### The Core Formula
**Strong narrative + active community + fair launch + right timing = moonshot candidate**

### Narrative (Most Important Factor)
- Every successful memecoin tells a story people emotionally invest in
- The story must be: simple, shareable, timely (tied to current event/meme)
- Examples: TRUMP (political moment), GOAT (AI agent narrative), PEPE (meme culture)
- Coins that ride an active cultural moment outperform generic launches 10:1

### Community Quality
- Active Telegram/Discord (real conversations, not just price spam)
- Holders are advocates, not just speculators
- Dev team engages with community (even pseudonymously)
- Organic Twitter content being created by holders
- Community "creates" content: memes, videos, gifs — without being paid

### Launch Characteristics of Winning Coins
- Fair launch (no presale, no VC allocation)
- Bonding curve launch on Pump.fun (transparent, equal opportunity)
- Dev wallet <5% at launch
- Clean bundle/sniper stats
- Liquidity burned or locked at graduation

### Timing Indicators
- Launch coincides with hot narrative (AI, political event, viral moment)
- Early buyers are organic (not insider wallets)
- Volume growing steadily (not one whale)
- Holder count growing continuously (not spiking then flat)
- Social mentions increasing across Twitter and Telegram independently

### Technical Patterns
- Consolidation after initial launch spike, then second leg up = healthiest sign
- Coins that hold 50% of their initial pump tend to run again
- Graduation from Pump.fun → 2x–5x spike is the most reliable pattern
- Strong coins: volume/market cap ratio stays healthy throughout the day

### What Doesn't Predict Success (Myths)
- A great meme image alone means nothing
- Telegram size alone means nothing (can be bought)
- Twitter followers alone means nothing (can be bought)
- KOL shilling alone has declining success rate (~50% crash within 2 months post-call)

---

## 9. Tokenomics — Good vs Bad

### Pump.fun Default (Most Launches)
- Total supply: 1,000,000,000 (1 billion tokens)
- 800M on bonding curve
- 200M to LP at graduation
- No team allocation, no presale — fully fair launch
- This is GOOD — equal opportunity for all buyers

### Good Tokenomics Checklist
- Total supply is fixed (capped) — no inflation
- No team/insider pre-allocation
- Mint authority revoked at or before launch
- Freeze authority revoked
- Liquidity locked or burned at graduation
- No vesting cliffs (where insider tokens unlock suddenly)
- Dev holds <5% of circulating supply
- Top 10 wallets combined <25%

### Bad Tokenomics Red Flags
- Unlimited/uncapped supply (dev can mint more)
- Team allocation >10% of total supply
- Vesting schedules with near-term unlock dates
- Presale buyers at 10x–100x discount to public
- Mint authority still active
- Locked liquidity that unlocks within 30 days
- Any wallet with >10% of supply (even if "locked")
- Multiple wallets with identical holdings (bundled insider wallets)

### For Post-Graduation Tokens
- Check if LP tokens are burned (irreversible) vs locked (temporary)
- Burned = better (LP can never be removed)
- Locked via Raydium locker or Streamflow = check unlock date
- If LP unlocks in 30 days = run

---

## 10. Risk Management

### Portfolio Allocation Rules
- **Never allocate more than 5% of total portfolio** to memecoins overall
- **Never risk more than 1–2% of total portfolio** on a single memecoin trade
- **Only trade with money you can afford to lose entirely** — most memecoins go to zero
- If you have $1,000 total: max $50 in memecoins, max $20 on any single trade

### Position Sizing for Axiom
- **Starting position (learning phase):** 0.05–0.10 SOL per trade
- **Comfortable phase:** 0.1–0.5 SOL per trade
- **Advanced:** 0.5–2 SOL per trade
- Diversify: 5–10 small positions > 1 large position

### Take-Profit Strategy
- **TP1 (25% of position):** At 2x — recover initial investment
- **TP2 (25% of position):** At 5x — lock in strong profit
- **TP3 (25% of position):** At 10x — major win
- **Ride remaining 25%:** Let it run to zero or moon
- Never let a 5x ride back to a loss without taking some off

### Stop-Loss Strategy
- Set stop-loss BEFORE you buy, not after
- **Standard:** 20–30% below entry for memecoins (they're volatile)
- **Strict:** 50% below entry if you believe in the coin but want protection
- **Mental stop:** If any major red flag emerges post-buy (dev dumps, LP pulled), exit immediately regardless of price
- Use Axiom's TPSL feature to automate stop-losses

### When to Exit Entirely
- Dev wallet makes a large sell (visible on Solscan)
- Liquidity suddenly drops >30%
- Telegram goes silent or dev disappears
- Volume collapses with no news
- A major KOL who called it starts selling
- Token has been running 4–6+ hours without new buyers
- You've hit your 5–10x target

### The 2x Rule
- If a coin doubles, sell enough to recover your initial investment
- Now you're playing with house money — psychological freedom to hold or sell remainder

---

## 11. Solana-Specific Mechanics

### Transaction Fees Overview
- **Base fee:** ~0.000005 SOL per transaction (negligible)
- **Priority fee:** You pay more to validators to include your tx faster; range 0.001–0.1 SOL
- **Bribe (Jito tip):** Extra payment to Jito block engine to prioritize tx; range 0.001–0.1 SOL
- **Trading platform fee:** 0.75–1% of trade value (Axiom/GMGN/BullX)

### Recommended Settings by Situation
| Situation | Slippage | Priority Fee | Bribe |
|-----------|----------|--------------|-------|
| Normal market | 5–10% | 0.001 SOL | 0.001 SOL |
| Active memecoin | 10–15% | 0.01 SOL | 0.01 SOL |
| Sniping launch | 15–30% | 0.03–0.1 SOL | 0.03–0.1 SOL |
| Emergency exit | 50–100% | 0.05+ SOL | 0.05+ SOL |

### MEV & Sandwich Attacks
- **What it is:** A bot sees your pending transaction, buys before you (raising price), lets your tx fill at higher price, then sells immediately after
- **Why memecoins are targeted:** High slippage tolerance = more profit margin for attacker
- **Cost to you:** You pay more than you should; sandwich bot extracts value from your trade

#### How to Protect Yourself
1. **Enable MEV Protection** on Axiom (routes through Jito — standard practice)
2. **Lower slippage** when possible — smaller window = less profitable to sandwich
3. **Use Jito-enabled bots** (Axiom, BullX, GMGN all have this)
4. **Avoid unprotected swaps** on basic Raydium/Jupiter without MEV routing
5. Jupiter's Real-Time Slippage Estimator (RTSE) auto-sets optimal slippage

### Slippage Explained
- Slippage = difference between expected price and actual fill price
- High slippage tolerance needed for illiquid memecoins
- Too low = tx fails; too high = sandwich attack target
- **Sweet spot for new memecoins:** 10–15%

### Transaction Timing
- Solana block time: ~400ms (very fast)
- Priority fee determines inclusion speed
- During congestion: increase priority fee to 0.01–0.05 SOL
- Sniping requires 0.03–0.1 SOL priority fee to compete

---

## 12. Narratives & Meta — What's Hot

### Current Active Narratives (2026)
- **AI + Memecoin hybrid (AI agents):** Coins connected to AI narrative — launched strong in Q1 2025 (GOAT, FARTCOIN); AI tokens dominated with 62.8% of investor interest in Q1 2025
- **PolitiFi:** Political memecoins; peaked with TRUMP token pre-inauguration; 2026 midterms will reignite this
- **Animal themes:** Perennial category — cats (POPCAT, MEW), frogs (PEPE), dogs (BONK); always has demand
- **4chan/culture memes:** Obscure internet culture references that go viral
- **Crossover IP memes:** Parodies of celebrities, games, TV shows

### How to Identify Hot Narratives in Real Time
1. **Check CoinGecko narrative rankings** — they publish monthly narrative profitability reports
2. **Monitor CT (Crypto Twitter)** — what are top accounts talking about? Repeating words/themes?
3. **Check Dexscreener trending** — what categories are appearing in top 10?
4. **Look at token names launching on Pump.fun** — if 50 coins all have "AI" in the name = narrative is hot
5. **Check Google Trends** for meme/event keywords
6. **Monitor mainstream news** — political events, celebrity moments, viral content = imminent meme launches

### Narrative Lifecycle
1. **Early:** 1–3 coins with the theme, massive upside if right
2. **Hot:** 10–20+ coins, "narrative coins" get pumped, lots of copycats
3. **Peak:** Every second launch is the same theme, quality declines
4. **Dead:** Narrative saturated, coins stop running, move on

### 2026 Emerging Narratives to Watch
- Prediction market integration tokens
- Memecoins with actual utility (DAO governance)
- Crosschain memecoins
- US midterm political tokens (2026 elections)

---

## 13. Copy Trading

### How to Find Good Wallets to Copy

#### Method 1: Axiom Leaderboard
- Go to Axiom Vision > Leaderboard
- Filter by PnL, win rate, volume
- Target wallets with 50–70% win rate (higher is suspicious)
- Look for consistent performers over 30+ days, not 1–2 lucky trades

#### Method 2: GMGN Smart Money Labels
- GMGN labels wallets as "Top Sniper," "KOL," or "Smart Money" based on PnL history
- Focus on "Top Snipers" with >60% win rate over 30+ trades

#### Method 3: KOLSCAN
- Free Solana wallet tracker
- Shows real-time PnL, transaction history, top tokens traded
- Find wallets consistently profiting on new launches

#### Method 4: Nansen PnL Leaderboard
- Institutional-grade analytics
- Rank wallets by realized + unrealized gains
- Filter by Solana memecoin activity

#### Evaluating a Wallet
- **Win rate:** 50–70% = realistic good trader; >80% = likely manipulator or very small sample
- **Trades:** Look for 50+ trades to establish pattern (not 5 lucky ones)
- **Position size:** Does the wallet's position sizes match what you can replicate?
- **Recency:** Recent activity within last 7 days — inactive wallets are useless
- **Diversity:** Trades multiple tokens, not just one coin repeatedly

### Copy Trading Execution on Axiom
1. Find a target wallet address
2. Go to Axiom > Trackers > Add Wallet
3. Assign name, enable buy/sell notifications
4. When notification fires that wallet bought token X, manually check the token
5. If it passes your quick safety check, use Flash Buy to enter
6. Mirror their exit as well (sell notification triggers your sell)

### Copy Trading Risks
- You are always slower than the wallet you're copying (manual execution delay)
- You may be the exit liquidity for the wallet you're copying
- Wallet may have info advantages you'll never have (insider)
- Don't copy a single wallet — diversify across 5–10 tracked wallets

---

## 14. KOL Calls — Key Opinion Leaders

### How KOL Calls Work
- A KOL (influencer, trader, analyst) posts a token CA on Twitter/Telegram
- Their followers rush to buy (FOMO effect)
- Price spikes immediately on call
- KOL (who bought before the call) sells into the pump

### The Reality of KOL Calls in 2025–2026
- >60% of KOL-backed projects see initial pump
- ~50% crash due to credibility issues within weeks
- ~90% fail to survive beyond 2 months
- KOLs receive tokens at deep discounts (or free) before calling — you are their exit

### How to Use KOL Calls (Without Getting Rugged)
1. **Never buy the first minute of a KOL call** — price is already pumped
2. **Wait for the initial dump** — many buyers panic sell after pump; price dips
3. **Only buy the dip if fundamentals support it** (real community forming, volume holding)
4. **Size small** — treat KOL calls as 0.1–0.5x your normal position
5. **Exit fast** — KOL calls are usually pump-and-dumps; don't hold overnight
6. **Check if KOL has transparent track record** — do they post W and L? Or only W?

### Spotting KOL Conflicts of Interest
- KOL has "alpha group" where people pay to get calls (paid to shill)
- KOL doesn't disclose token holdings
- KOL suddenly posts a coin with no prior discussion
- KOL has history of calling coins that dump after their post

### Legitimate vs Predatory KOLs
- **Legitimate:** Posts analysis, admits mistakes, has verifiable on-chain track record
- **Predatory:** Only posts winners, has paid groups, doesn't show wallet, coins crash after call

---

## 15. Timing the Market

### Best Times of Day (UTC)
| Window | UTC | EST | Why |
|--------|-----|-----|-----|
| Early US morning | 12:00–16:00 UTC | 7AM–11AM | Fresh retail liquidity; post-Asia review |
| US afternoon/evening | 20:00–00:00 UTC | 3PM–7PM | US + Asia overlap; highest total volume |
| Dead zone | 03:00–09:00 UTC | 10PM–4AM EST | Low volume; pumps can still happen but less liquidity |

### Best Days of Week
- **Tuesday–Thursday:** Highest volume historically; mid-week momentum
- **Monday:** Often continuation of weekend moves; can catch Monday pumps
- **Friday afternoon (US):** Volume drops as traders close positions for weekend
- **Weekends:** Lower overall volume; but viral memes/events don't follow a schedule — stay alert

### How to Read Momentum
- **Holder count growing:** More people buying = momentum building
- **Volume consistent (not spiky):** Sustained buying, not one whale
- **Price making higher lows:** Each small dip is bought up = bullish structure
- **Social mentions increasing:** Organic Twitter/Telegram chatter growing
- **Bonding curve % rising steadily:** Approaching graduation = imminent catalyst

### When to NOT Enter
- Already 10x+ from launch with no pullback — you're likely the last buyer
- Volume declining while price holds (distribution phase — holders slowly selling)
- Telegram has gone quiet after initial hype
- Chart shows one giant green candle followed by lower highs — classic pump and dump shape
- It's a major KOL call and price already spiked 5x in last hour

### Momentum Indicators on Axiom/Dexscreener
- **Buys >> Sells ratio:** Strong buying pressure
- **Unique wallets growing:** Organic new buyers
- **Bonding curve % accelerating:** nearing graduation
- **Twitter mentions in Axiom Trackers:** Social volume spiking

---

## Quick Reference Cheat Sheet

### Safety Check (30 Seconds, Mandatory Before Every Buy)
```
□ Mint authority REVOKED (RugCheck.xyz)
□ Freeze authority REVOKED (RugCheck.xyz)
□ Liquidity LOCKED or BURNED
□ Top 10 holders < 30% combined (Solscan)
□ Dev wallet < 10% (Axiom Vision / GMGN)
□ Bundle % < 15% (Axiom Vision)
□ Sniper % < 25% (Axiom Vision)
□ Liquidity > $20K
□ Twitter account NOT brand new (> 1 week old)
```

### Instant Red Flags (Exit / Don't Buy)
```
✗ Mint authority NOT revoked
✗ Freeze authority NOT revoked (honeypot risk)
✗ Liquidity not locked (will be rugged)
✗ Dev wallet > 20%
✗ Top holder > 30% single wallet
✗ Bundle % > 20%
✗ Sniper % > 30%
✗ Dev wallet has previous rug pull history
```

### Axiom Pulse Filters (Recommended Starting Point)
```
Protocol: Pump.fun
Min holders: 50
Min age: 3 min
Max age: 30 min
Min volume: $20,000
Min transactions: 100
Max dev holdings: 20%
Max sniper %: 10%
```

### Position Sizing
```
Beginner: 0.05–0.10 SOL per trade
Intermediate: 0.1–0.5 SOL per trade
Max single position: 1–2% of total portfolio
Total memecoins: max 5% of portfolio
```

### Trade Settings (Axiom)
```
Normal trade: Slippage 10-15%, Priority 0.01 SOL, Bribe 0.001 SOL, MEV ON
Active launch: Slippage 20-30%, Priority 0.03 SOL, Bribe 0.03 SOL, MEV ON
Sniping: Slippage 15-30%, Priority 0.05-0.1 SOL, Bribe 0.05-0.1 SOL, MEV ON
Emergency exit: Slippage 50-100%, Priority 0.05+ SOL
```

### Take-Profit Ladder
```
TP1: Sell 25% at 2x (recover entry)
TP2: Sell 25% at 5x (major profit locked)
TP3: Sell 25% at 10x (life-changing on big wins)
Ride: Let last 25% go to zero or moon
```

### Stop-Loss
```
Standard: -30% from entry
Strict: -50% from entry
Immediate exit: Dev dumps, LP pulled, Telegram goes silent
```

### The 5-Step Early Entry Workflow
```
1. SPOT  — Axiom Pulse New Pairs / GMGN new token feed
2. CHECK — RugCheck.xyz + Axiom Vision (mint/freeze/bundle/sniper)
3. VERIFY — Solscan holders, Twitter/Telegram organic activity
4. CONFIRM — GMGN smart money buying? Multiple wallets?
5. BUY   — Flash Buy on Axiom, 10-15% slippage, MEV ON
```

### Tools at a Glance
```
DISCOVERY:  Axiom Pulse, GMGN.ai, Dexscreener, Pump.fun live feed
SAFETY:     RugCheck.xyz, Solsniffer, Bubblemaps, Solscan
TRADING:    Axiom.trade (primary), BullX NEO, Photon, GMGN
TRACKING:   KOLSCAN (free), Nansen (paid), Axiom Trackers, GMGN
ALPHA:      CT Twitter, Telegram groups (small vetted > large public)
```

### Narrative Checklist
```
□ Is there a current hot meta this coin fits?
□ Is the name/ticker instantly shareable?
□ Are people creating organic memes/content about it?
□ Does it tie to a current event or viral moment?
□ Is the community forming across multiple platforms?
```

---

*Research compiled: 2026-03-27 by JERRY*
*Sources: Coin Bureau, CoinGecko, PANews, Axiom Trade, solanaleveling.com, GMGN, BullX, DexScreener, RugCheck, multiple CT/Medium traders*

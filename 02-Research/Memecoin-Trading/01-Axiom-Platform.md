---
tags: [axiom, platform, solana, trading]
created: 2026-03-27
---

# Axiom Platform — Complete Guide

> [[00-INDEX|← Back to Index]]

**URL:** https://axiom.trade
**Type:** Browser-based, non-custodial Solana DEX aggregator + trading hub
**Founded:** Early 2024, Y Combinator Winter 2025
**Market share:** 72% of Solana bot trading volume (July 2025)

---

## Fees

| Tier | Fee | Cashback |
|------|-----|----------|
| Wood (default) | 0.95% | 0.05% |
| Diamond | 0.80% | 0.20% |
| Champion | 0.75% | 0.25% |

- Priority fees: 0.001 SOL default (raise to 0.03–0.1 SOL for sniping)
- Referral code = 10% fee discount

---

## Pulse Module (Token Discovery) — Most Important

Three feeds:
- **New Pairs** — freshest launches, catch tokens in first minutes
- **Final Stretch** — tokens at 80–99% bonding curve (graduation imminent)
- **Migrated** — just graduated to DEX; more liquid, already moved

### Recommended Filters — New Pairs

```
Protocol:         Pump.fun
Min holders:      50
Min age:          3 min
Max age:          30 min
Min volume:       $20,000
Min transactions: 100
Max dev holdings: 20%
Max sniper %:     10%
```

### Recommended Filters — Final Stretch

```
Min market cap: $20,000
Max age:        18 min
```

### All Available Filters
- Protocol: Pump.fun vs Moonshot
- Keyword include/exclude
- Top 10 holder %
- Insider ownership
- Pro Traders %
- Liquidity, volume, transaction count, bundle %

---

## Trackers Module (Wallet Tracking)

- Add wallet addresses, get real-time buy/sell alerts
- Floating window so you can multitask
- Twitter monitoring: tracks top 1,500 accounts for coin mentions
- **Free** (paid on most other platforms)

---

## Vision Tool (Analytics)

- Trader leaderboard by PnL / win rate / volume
- Bundle detection (insider coordination)
- Twitter verification on token accounts
- Honeypot and rug risk assessment per token
- Security audit results displayed inline

---

## Sniper Functionality

- Monitors mempool for new liquidity additions
- Executes buy in same or next block as launch
- Built-in MEV protection via Jito routing
- Sub-second execution

### Sniper Settings

| Situation | Slippage | Priority Fee | Bribe |
|-----------|----------|--------------|-------|
| Normal trade | 10–15% | 0.001–0.015 SOL | 0.001 SOL |
| Active launch | 20–30% | 0.03 SOL | 0.03 SOL |
| Sniping | 15–30% | 0.05–0.1 SOL | 0.05–0.1 SOL |
| Emergency exit | 50–100% | 0.05+ SOL | — |

> Always keep **MEV: Secure mode ON**

---

## Copy Trading on Axiom

- **NOT automated** — manual copy trading
- Use Trackers to monitor wallets, mirror trades manually
- Find wallets via leaderboard or community-shared addresses
- Target wallets with **50–70% win rate** (>75% is suspicious)

**Execution:**
1. Add target wallet to Trackers
2. Get notification when they buy token X
3. Run quick safety check on token
4. Flash Buy if it passes

---

## Other Features

- Limit orders + market orders
- **TPSL** (Take Profit / Stop Loss) built in — use this
- **Flash Buy** — one-click preset amounts (set up 0.05 / 0.1 / 0.25 SOL buttons)
- Hyperliquid perpetuals up to 50x leverage
- Portfolio P&L tracking
- Non-custodial wallet (Turnkey infrastructure)

---

## Geographic Restrictions

Blocked: US, China, Singapore, Cuba, Iran, Iraq, North Korea, Syria, Yemen, Crimea

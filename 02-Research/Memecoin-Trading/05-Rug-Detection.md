---
tags: [rug-pull, safety, honeypot, red-flags]
created: 2026-03-27
---

# Rug Pull Detection & Safety

> [[00-INDEX|← Back to Index]]

---

## 30-Second Safety Check (Do This Every Time)

```
1. Copy token contract address (CA)
2. Paste into RugCheck.xyz → check overall risk score
3. Confirm: Mint authority REVOKED ✓
4. Confirm: Freeze authority REVOKED ✓
5. Confirm: Liquidity LOCKED or BURNED ✓
6. Check top holders → Solscan (token → holders tab)
7. Check Bundle % + Sniper % → Axiom Vision or GMGN
8. Quick Twitter search of token name — organic or coordinated?
```

---

## Hard Red Flags (Don't Buy)

```
✗ Mint authority NOT revoked — dev can print unlimited tokens
✗ Freeze authority NOT revoked — dev can freeze your wallet (honeypot)
✗ Liquidity not locked/burned — can be drained instantly
✗ Top single wallet > 30% of supply
✗ Dev wallet history shows previous rug pulls
✗ Bundle % > 20%
✗ Sniper % > 30%
```

---

## Moderate Red Flags (Proceed with Extreme Caution)

- Dev holds 10–20% of supply
- Sniper % 15–30%
- Top 10 holders own 25–40%
- Anonymous team, no social presence
- Twitter account under 1 week old
- Telegram has fake/bot engagement (many members, no real chat)
- No website or copy-paste low-quality site

---

## Honeypot — What It Is

A token you can **buy but cannot sell**.

- Caused by active freeze authority OR contract coding tricks
- **Test:** Try to sell a tiny amount before putting in full position
- **Detection tools:** BullX (built-in honeypot detect), RugCheck.xyz

---

## Fake Volume Detection

- Volume spike with no holder growth = wash trading
- Same 2–3 wallets trading back and forth
- Volume/mcap ratio extreme without organic community growth
- Buys and sells perfectly matched in timing

---

## Rug Pull Scale (2025 Context)

- $2.8B+ lost to rug pulls across all chains in 2025
- Majority on Solana and BSC (lowest deployment costs)
- 82.8% of >100% return tokens showed artificial growth strategies

---

## Safety Tools

| Tool | Best For |
|------|---------|
| **RugCheck.xyz** | Overall risk score, mint/freeze authority |
| **Solsniffer** | 20+ security indicators, Snifscore 0–100 |
| **Bubblemaps.io** | Visual holder clustering, insider wallet detection |
| **Solscan** | Manual holder distribution, wallet history |
| **GMGN** | Bundle %, sniper %, smart money presence |
| **Axiom Vision** | Built-in safety audit per token |
| **BullX** | Honeypot detection |

---

## Post-Buy Exit Triggers (Sell Immediately If...)

- Dev wallet makes a large sell (visible on Solscan)
- Liquidity drops suddenly > 30%
- Telegram goes silent or dev disappears
- Volume collapses with no news
- A major KOL who called it starts selling
- Token has been running 4–6+ hours with no new buyers

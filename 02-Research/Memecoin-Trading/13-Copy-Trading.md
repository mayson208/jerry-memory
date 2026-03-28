---
tags: [copy-trading, wallets, gmgn, kolscan]
created: 2026-03-27
---

# Copy Trading

> [[00-INDEX|← Back to Index]]

---

## How to Find Good Wallets to Copy

### Method 1: Axiom Leaderboard
- Axiom Vision → Leaderboard
- Filter by PnL, win rate, volume
- Target: **50–70% win rate** (higher = suspicious)
- Look for consistent performers over **30+ days**, not 1–2 lucky trades

### Method 2: GMGN Smart Money Labels
- GMGN labels wallets as "Top Sniper," "KOL," or "Smart Money"
- Focus on Top Snipers with **> 60% win rate** over 30+ trades

### Method 3: KOLSCAN (Free)
- Real-time PnL, transaction history, top tokens traded
- Find wallets consistently profiting on new launches

### Method 4: Nansen PnL Leaderboard
- Institutional-grade, filter by Solana memecoin activity
- Rank by realized + unrealized gains

---

## Evaluating a Wallet

| Metric | Target | Red Flag |
|--------|--------|----------|
| Win rate | 50–70% | > 80% (likely manipulated or tiny sample) |
| # of trades | 50+ | < 10 (too small sample) |
| Recent activity | Last 7 days | Inactive > 30 days |
| Diversity | Multiple tokens | Only 1 coin repeatedly |
| Position size | Matches what you can replicate | Positions too large to mirror |

---

## Copy Trading Execution on Axiom

```
1. Find target wallet address
2. Axiom → Trackers → Add Wallet
3. Assign name, enable buy/sell notifications
4. Notification fires: wallet bought Token X
5. Quick safety check on Token X (30 seconds)
6. If passes → Flash Buy on Axiom
7. Mirror their exit (sell notification triggers your sell)
```

---

## Copy Trading Risks

- You are **always slower** than the wallet you're copying (manual delay)
- You may be the **exit liquidity** for the wallet you're copying
- Wallet may have **info advantages** (insider) you'll never have
- **Don't copy a single wallet** — diversify across 5–10 tracked wallets
- A wallet with great history can still blow up on the next trade

---

## Best Practice

- Track **5–10 wallets** minimum
- Only act when **2+ tracked wallets buy the same token** (stronger signal)
- Always run your own safety check even if copying a wallet you trust
- Set the same take-profit/stop-loss levels regardless of source

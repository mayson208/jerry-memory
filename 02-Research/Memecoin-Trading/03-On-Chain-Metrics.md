---
tags: [memecoin, metrics, on-chain, analysis]
created: 2026-03-27
---

# On-Chain Metrics — What to Check

> [[00-INDEX|← Back to Index]]

---

## Hard Limits (Non-Negotiable)

| Metric | Max Acceptable | Red Flag |
|--------|---------------|----------|
| Top 10 holders combined | < 30% | > 40% |
| Single wallet | < 10% | > 30% |
| Dev wallet | < 10% | > 20% |
| Bundle % | < 15% | > 20% |
| Sniper % | < 25% | > 30% |
| Min liquidity | $20K | < $10K |

---

## Liquidity

- **Minimum to enter:** $20K–$50K (below = extreme slippage)
- **Good:** $100K+ (can enter/exit without huge impact)
- **Locked:** Should be locked or burned — unlocked = rug risk
- **Concentration:** Avoid if one pool holds >90% (can be drained)

## Market Cap Entry Points

| Range | Risk | Upside |
|-------|------|--------|
| $10K–$100K | Highest | 10x–1000x possible |
| $100K–$1M | Medium | 10x potential |
| $1M+ | Lower | Safer, lower ceiling |

## Holder Distribution

- **Good:** Many wallets, no single wallet above 5%
- **Warning:** Top 10 > 25% combined
- **Red flag:** Top 10 > 40% — coordinated dump risk
- **Where to check:** Solscan → Token → Holders tab, or Bubblemaps.io

## Developer Wallet

- **Safe:** < 5% of supply
- **Warning:** > 10%
- **Red flag:** > 20%
- Also check: has dev wallet been in previous rugs? (Solscan wallet history)

## Bundled Buys

- Multiple insider wallets buying in same block at launch
- They hold at near-zero cost basis, will dump on you
- **Check:** Axiom Vision shows Bundle % — avoid > 15%
- **Also:** BullX bundle checker, GMGN

## Sniper %

- Snipers bought at the very bottom — massive overhang
- **Safe:** < 10%
- **Warning:** 10–25%
- **Red flag:** > 30% — launch was likely controlled

## Bonding Curve % (Pump.fun)

- Closer to 100% (~$69K mcap) = graduation pump incoming
- "Final Stretch" = 80–99% complete = strong momentum play
- Graduation to PumpSwap often causes **2x–5x spike**

## Volume / Transactions

- **Healthy:** Consistent volume, growing tx count across many wallets
- **Red flag:** Volume concentrated in 1–3 wallets = wash trading
- **Red flag:** Volume spiked once but no sustained activity

---

## Where to Check Each Metric

| Metric | Tool |
|--------|------|
| Mint/freeze authority | RugCheck.xyz |
| Top holders | Solscan → Token → Holders |
| Holder clustering/insiders | Bubblemaps.io |
| Bundle % | Axiom Vision, GMGN, BullX |
| Sniper % | Axiom Vision, GMGN |
| Dev wallet % | GMGN, Axiom Vision |
| LP locked/burned | RugCheck.xyz, Solscan |
| Smart money buying | GMGN.ai |

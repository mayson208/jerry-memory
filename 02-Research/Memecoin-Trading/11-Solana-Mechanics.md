---
tags: [solana, slippage, mev, priority-fees, gas]
created: 2026-03-27
---

# Solana-Specific Mechanics

> [[00-INDEX|← Back to Index]]

---

## Transaction Fees Overview

| Fee Type | Default | Range |
|----------|---------|-------|
| Base fee | 0.000005 SOL | Fixed (negligible) |
| Priority fee | 0.001 SOL | 0.001–0.1 SOL |
| Bribe (Jito tip) | 0.001 SOL | 0.001–0.1 SOL |
| Platform fee (Axiom) | 0.95% | 0.75–0.95% |

Solana block time: **~400ms** (very fast — speed matters for sniping)

---

## Recommended Settings by Situation

| Situation | Slippage | Priority Fee | Bribe |
|-----------|----------|--------------|-------|
| Normal market | 5–10% | 0.001 SOL | 0.001 SOL |
| Active memecoin | 10–15% | 0.01 SOL | 0.01 SOL |
| Sniping a launch | 15–30% | 0.03–0.1 SOL | 0.03–0.1 SOL |
| Emergency exit | 50–100% | 0.05+ SOL | 0.05+ SOL |

> **Always keep MEV: Secure mode ON on Axiom**

---

## MEV & Sandwich Attacks

**What is it:**
1. Bot sees your pending transaction in the mempool
2. Bot buys before you → raises the price
3. Your tx fills at higher price (you paid more)
4. Bot immediately sells → extracts profit from your trade

**Why memecoins are targeted:** High slippage tolerance = more margin for the attacker

### How to Protect Yourself

1. **Enable MEV Protection** on Axiom (Jito routing) — always on
2. **Lower slippage** where possible — smaller window = less profitable to sandwich
3. **Use Jito-enabled platforms:** Axiom, BullX, GMGN all have this
4. **Avoid basic Raydium/Jupiter swaps** without MEV routing

---

## Slippage Explained

- Difference between expected price and actual fill price
- Too low = transaction fails
- Too high = sandwich attack target
- **Sweet spot for new memecoins:** 10–15%
- For sniping a launch: 15–30% (sometimes 50%+ needed in extreme competition)

---

## During Network Congestion

- Increase priority fee to 0.01–0.05 SOL
- Sniping requires 0.03–0.1 SOL to compete with other snipers
- Watch for failed transactions — may need to retry with higher fee

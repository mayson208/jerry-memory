---
tags: [tokenomics, supply, mint-authority, liquidity]
created: 2026-03-27
---

# Tokenomics — Good vs Bad

> [[00-INDEX|← Back to Index]]

---

## Pump.fun Default (Most Launches)

- **Total supply:** 1,000,000,000 (1 billion tokens)
- 800M on bonding curve
- 200M to LP at graduation
- No team allocation, no presale
- ✅ This is good — equal opportunity for all buyers

---

## Good Tokenomics Checklist

```
✓ Fixed (capped) total supply — no inflation
✓ No team/insider pre-allocation
✓ Mint authority revoked at or before launch
✓ Freeze authority revoked
✓ Liquidity locked or burned at graduation
✓ No vesting cliffs (where insider tokens unlock suddenly)
✓ Dev holds < 5% of circulating supply
✓ Top 10 wallets combined < 25%
```

---

## Bad Tokenomics — Red Flags

```
✗ Unlimited/uncapped supply (dev can mint more)
✗ Team allocation > 10% of total supply
✗ Vesting schedules with near-term unlock dates
✗ Presale buyers at 10x–100x discount to public
✗ Mint authority still active
✗ Liquidity that unlocks within 30 days
✗ Any wallet with > 10% of supply (even if "locked")
✗ Multiple wallets with identical holdings (bundled insiders)
```

---

## Liquidity — Locked vs Burned

| Type | Safety | Why |
|------|--------|-----|
| **Burned** (irreversible) | Best | LP can never be removed |
| **Locked** (Raydium/Streamflow) | Good | Check unlock date |
| **Unlocked** | Danger | Dev can pull anytime |
| **Locked < 30 days** | Red flag | Will unlock soon |

**Always check:** Does the lock expire soon? Upcoming unlock = rug risk.

---

## How to Check Tokenomics

| What | Where |
|------|-------|
| Mint authority | RugCheck.xyz |
| Freeze authority | RugCheck.xyz |
| LP locked/burned | RugCheck.xyz, Solscan |
| LP unlock date | Streamflow.finance, Raydium locker |
| Top holders | Solscan → Token → Holders |
| Dev wallet % | GMGN, Axiom Vision |
| Vesting schedules | Project docs (if any) |

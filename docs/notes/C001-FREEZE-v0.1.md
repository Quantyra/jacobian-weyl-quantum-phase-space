# C001 companion freeze (v0.9)

**Date:** 2026-07-22  
**PDF:** docs/notes/C001-cp-correspondence-arxiv.pdf  
**Tag:** v0.3.2-c001-companion (supersedes `v0.3.1-c001-companion`; do not move old tags)  
**Freeze SHA:** HEAD after v0.9 content commit (this round)  
**Pack:** COMPANION-PACK.md  

## Scoreboard
| Item | Status |
|------|--------|
| Koopman position-sector CP | CONSTRUCT |
| Joint-Stone-Canonical (J2) | NO-GO |
| Full-triple Joint-Stone (J3, G4) | NO-GO |
| Joint-Stone-Hom-1 (J4) | NO-GO |
| Joint-Stone-CP-1 (J5) | NO-GO |
| Unitary-Image-CP-1 (J6) | NO-GO |
| Diag-CP-Φ₀ (J6-C) | CONSTRUCT |
| Joint-Form-Core | CONSTRUCT |
| Joint-Form-ESS-1 | OBSTRUCT |
| **Full-ψ-BT-Envelope (J7-C)** | **CONSTRUCT** |
| **Full-ψ-CFC-SA-1 (J7)** | **NO-GO** |
| Full-ψ-CP-Weyl-C\* (J7-O) | OPEN (narrowed) |

## Adversarial
- v0.6 freeze: Proof PASS, Non-claims PASS, Package REVISE→PASS  
- v0.7 J5: Proof PASS (multiplicative domain), Non-claims PASS, Package REVISE→fixed→PASS  
- v0.8 J6 (content at `95a0bc9`): Proof **PASS** (Unitary-Image NO-GO + Diag-CP CONSTRUCT); Non-claims **PASS** (no J5 weaken; full-ψ still OPEN); Package **REVISE** (stale tag/README/aggregate green)  
- v0.8 package re-gate (`9445e95`): Package surfaces synced; aggregate pending package re-review  
- v0.9 J7 (this commit): Full-ψ abstract C\* **SPLIT** (BT-Envelope CONSTRUCT + CFC-SA NO-GO + CP-Weyl-C\* OPEN); do **not** claim Aggregate PASS until adversarial package re-review closes.

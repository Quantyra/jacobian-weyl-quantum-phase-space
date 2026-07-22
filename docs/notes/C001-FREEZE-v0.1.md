# C001 companion freeze (v0.8, package re-gate)

**Date:** 2026-07-22  
**PDF:** docs/notes/C001-cp-correspondence-arxiv.pdf  
**Tag:** v0.3.1-c001-companion (supersedes `v0.3.0-c001-companion`; do not move old tags)  
**Freeze SHA:** HEAD after package re-gate commit (this round)  
**Pack:** COMPANION-PACK.md  

## Scoreboard
| Item | Status |
|------|--------|
| Koopman position-sector CP | CONSTRUCT |
| Joint-Stone-Canonical (J2) | NO-GO |
| Full-triple Joint-Stone (J3, G4) | NO-GO |
| Joint-Stone-Hom-1 (J4) | NO-GO |
| Joint-Stone-CP-1 (J5) | NO-GO |
| **Unitary-Image-CP-1 (J6)** | **NO-GO** |
| **Diag-CP-Φ₀ (J6-C)** | **CONSTRUCT** |
| Joint-Form-Core | CONSTRUCT |
| Joint-Form-ESS-1 | OBSTRUCT |
| Full-ψ abstract C* without Hom/unitary-image | OPEN |

## Adversarial
- v0.6 freeze: Proof PASS, Non-claims PASS, Package REVISE→PASS  
- v0.7 J5: Proof PASS (multiplicative domain), Non-claims PASS, Package REVISE→fixed→PASS  
- v0.8 J6 (content at `95a0bc9`): Proof **PASS** (Unitary-Image NO-GO + Diag-CP CONSTRUCT); Non-claims **PASS** (no J5 weaken; full-ψ still OPEN); Package **REVISE** (stale tag/README/aggregate green)  
- v0.8 package re-gate (this commit): Package surfaces synced (tags `v0.3.1-c001-companion` / README / COMPANION-PACK / this marker); **aggregate pending package re-review** — do **not** claim Aggregate PASS or green gate until package re-review closes.

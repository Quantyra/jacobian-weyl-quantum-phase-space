# C001 companion freeze (v0.9)

**Date:** 2026-07-22  
**PDF:** docs/notes/C001-cp-correspondence-arxiv.pdf  
**Tag:** `v0.3.3-c001-companion` (supersedes package pins `v0.3.2`/`v0.3.1`; do not move old tags)  
**Freeze SHA:** `45e7d53803d73a3ad5a67753d3f4ed86aa77a188`  
**Pack:** COMPANION-PACK.md  

## Scoreboard
| Item | Status |
|------|--------|
| Koopman position-sector CP | CONSTRUCT |
| Joint-Stone-Canonical (J2) | NO-GO |
| Full-triple Joint-Stone (J3, **G4-conditional**) | NO-GO (G4 pairs; not A001) |
| Joint-Stone-Hom-1 (J4) | NO-GO |
| Joint-Stone-CP-1 (J5) | NO-GO |
| Unitary-Image-CP-1 (J6) | NO-GO |
| Diag-CP-Φ₀ (J6-C) | CONSTRUCT |
| Joint-Form-Core | CONSTRUCT |
| Joint-Form-ESS-1 | OBSTRUCT |
| **Full-ψ-BT-Envelope (J7-C)** — bounded dual-momentum transforms + Φ₀ positions; form-level only; **not** Full-ψ-CFC / **not** Weyl-C* / **not** Stinespring | **CONSTRUCT** |
| **Full-ψ-CFC-SA-1 (J7)** — reduces to J6 on same joint vNa + normal CP | **NO-GO** |
| Full-ψ-CP-Weyl-C\* (J7-O) | OPEN (narrowed) |

## Adversarial
- v0.6 freeze: Proof PASS, Non-claims PASS, Package REVISE→PASS  
- v0.7 J5: Proof PASS (multiplicative domain), Non-claims PASS, Package REVISE→fixed→PASS  
- v0.8 J6 (content at `95a0bc9`): Proof **PASS** (Unitary-Image NO-GO + Diag-CP CONSTRUCT); Non-claims **PASS** (no J5 weaken; full-ψ still OPEN); Package **REVISE** (stale tag/README/aggregate green)  
- v0.8 package re-gate (`9445e95`): Package surfaces synced; aggregate pending package re-review  
- v0.9 J7 (content at `60f543c` / `d2c8488` lineage): Full-ψ abstract C\* **SPLIT** (BT-Envelope form-level CONSTRUCT + CFC-SA NO-GO via J6 checklist + CP-Weyl-C\* OPEN)  
- v0.9 package+wording re-gate (`61bf3da`): J7-C naming lock; J7→J6 hypothesis checklist; J3 G4-conditional qualifier; TeX path breaks; freeze SHA pinned; **do not claim Aggregate PASS** — package fixed awaiting re-review.
- B001 v0.7 real-poly auto-language erratum + deg-1-not-poly-auto fix: dual historical pins `v0.2.2`/`v0.3.2` @ `61bf3da` package-superseded  
- **v0.9 Aggregate PASS** at `45e7d53` (`v0.3.3-c001-companion`): proof PASS · non-claims PASS · package PASS (3-role Task)

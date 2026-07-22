# B001 draft v0.7

**Date:** 2026-07-22  
**PDF:** docs/notes/B001-classification-arxiv.pdf  
**Status:** v0.7 — atlas A000–A010 + B5 restricted poly dichotomy + B6 regime-T partial + **B7 OPEN-T sharpened** (graph / deg≤2 ⇒ **global \(C^\infty\) diffeo** / E; affine-invariant; poly inverse only when proved)  
**Tag:** `v0.2.3-b001-draft` @ `45e7d53` (prior `v0.2.2` @ `61bf3da` package-superseded; do not move)  
**Freeze SHA:** `45e7d53803d73a3ad5a67753d3f4ed86aa77a188`  
**Pack:** COMPANION-PACK.md  
**A001:** parked VIPN6B (human only)  
**C:** C001 v0.9 — unchanged by this B erratum; J2 NO-GO; J3 **G4-conditional** NO-GO; J4–J7 split; Diag-CP-Φ₀ CONSTRUCT; Full-ψ-BT-Envelope (bounded dual-momentum transforms + Φ₀ positions; form-level; **not** CFC / **not** Weyl-C* / **not** Stinespring) CONSTRUCT; Full-ψ-CFC-SA-1 OBSTRUCT via J6; Full-ψ-CP-Weyl-C* OPEN (narrow)  
**Dichotomy:** full poly thin-vs-open still conjecture; regime T excluded on proper/injective/deg-1/product/triangular/**graph-type / deg P≤2** (as global \(C^\infty\) diffeos / E); residual **OPEN-T** (non-coordinate deg≥3, Bad on atypical/bifurcation-born fibers)

## B7
- Note: `docs/validation/PROGRAM-B-B7-OPEN-T.md`
- CAS: `data/anchor/cas_atlas_B7_OPEN_T_B001.json`
- Verdict: **PARTIAL** (not T-EXCLUDED / not T-EXHIBITED)
- Theorems: B7.0a affine invariance; B7.2 graph⇒global \(C^\infty\) diffeo / E (poly auto only if inverse poly); B7.3 degP≤2⇒E; B7.6 P0-axis cannot carry T; B7.7–B7.9 model blocks

## B6
- Note: `docs/validation/PROGRAM-B-B6-regime-T.md`
- CAS: `data/anchor/cas_atlas_B6_regime_T_B001.json`
- Verdict: **PARTIAL** (inherited; B6.2 corrected: injective poly local diffeo ⇒ global \(C^\infty\) diffeo / E, not poly inverse over \(\mathbb{R}\))

## Adversarial
v0.6 package re-gate at `9445e95`.  
v0.7 B7 content at `d2c8488` lineage.  
v0.7 package+wording re-gate (`61bf3da`): affine-invariance note; TeX path breaks; freeze SHA pinned.  
**v0.7 math-language erratum + deg-1 fix:** bijective real poly local diffeo ⇏ poly inverse; deg-1 fibers insufficient.  
**Aggregate PASS** at `45e7d53` (`v0.2.3-b001-draft`): proof PASS · non-claims PASS · package PASS.

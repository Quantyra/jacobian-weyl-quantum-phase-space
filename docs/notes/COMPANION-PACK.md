# EXOTIC-CCR companion pack

**Date:** 2026-07-22  
**Status:** ACTIVE (A001 arXiv waits on math-ph endorsement `VIPN6B` — human only; no agent work)  
**Rule:** A001 PDF frozen at `v0.3.6-submit`; companions do not rewrite it.

---

## Flagship A001 (DOI citable; arXiv pending)

| Artifact | Pin |
|----------|-----|
| PDF | [A001-arxiv.pdf](A001-arxiv.pdf) |
| Tag | [v0.3.6-submit](https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.3.6-submit) |
| Concept DOI | [10.5281/zenodo.21474351](https://doi.org/10.5281/zenodo.21474351) |
| Endorsement | [A001-endorsement-status.md](A001-endorsement-status.md) — code `VIPN6B`, category **math-ph** |
| Claim | \(H=-iX_1\) has \((n_+,n_-)=(\infty,\infty)\); seed restated; H₁-only |

---

## Companion B001 — classification v0.7

| Artifact | Pin |
|----------|-----|
| PDF | [B001-classification-arxiv.pdf](B001-classification-arxiv.pdf) |
| TeX | [B001-classification-arxiv.tex](B001-classification-arxiv.tex) |
| Marker | [B001-DRAFT-v0.1.md](B001-DRAFT-v0.1.md) (content = v0.7, B7 PARTIAL) |
| Tag / release | prior freeze `v0.2.2-b001-draft` @ `61bf3da` **immutable historical pin** (superseded at package level for B automorphism language). Pending after gate: e.g. `v0.2.3-b001-draft` on new SHA (C unchanged ⇒ dual-tag same SHA or B-only) |
| Prior tags | `v0.2.2-b001-draft` @ `61bf3da` (v0.7 pre-erratum auto wording; do not retag); `v0.2.1-b001-draft` (v0.6; do not retag); `v0.2.0-b001-draft` (pre-B6; do not retag) |
| Atlas | A000–A010; CAS `cas_atlas_A005_A006_B001.json`, `cas_atlas_A007_A008_B001.json`, `cas_atlas_A009_A010_B001.json`, `cas_atlas_B5_poly_dichotomy_B001.json`, `cas_atlas_B6_regime_T_B001.json`, `cas_atlas_B7_OPEN_T_B001.json` |
| Claims | B1 lemma; schema; atlas A000–A010; A007 thin vs A009 open (Pinchuk); **B5 restricted poly dichotomy lemmas**; **B6 regime-T PARTIAL**; **B7 OPEN-T sharpened** (affine-invariant graph-type / \(\deg P\le 2\) ⇒ **global \(C^\infty\) diffeo** / regime E — not automatic poly inverse over \(\mathbb{R}\); T-filter deg≥3 non-coordinate; \(P_0\)-axis cannot carry T; CAS through deg 8); full poly dichotomy still a **conjecture** |
| B5 note | [`PROGRAM-B-B5-poly-dichotomy-lemmas.md`](../validation/PROGRAM-B-B5-poly-dichotomy-lemmas.md) |
| B6 note | [`PROGRAM-B-B6-regime-T.md`](../validation/PROGRAM-B-B6-regime-T.md) |
| B7 note | [`PROGRAM-B-B7-OPEN-T.md`](../validation/PROGRAM-B-B7-OPEN-T.md) |
| Gate status | v0.7 content erratum (real poly auto language); **no Aggregate PASS**; prior tags `61bf3da` superseded for B automorphism wording; pending new tags after gate (e.g. `v0.2.3-b001-draft`; C unchanged ⇒ retag B only or dual-tag same SHA) |

---

## Companion C001 — Weyl endomorphism packages v0.9

| Artifact | Pin |
|----------|-----|
| PDF | [C001-cp-correspondence-arxiv.pdf](C001-cp-correspondence-arxiv.pdf) |
| TeX | [C001-cp-correspondence-arxiv.tex](C001-cp-correspondence-arxiv.tex) |
| Marker | [C001-FREEZE-v0.1.md](C001-FREEZE-v0.1.md) (content = v0.9) |
| Tag / release | prior freeze `v0.3.2-c001-companion` @ `61bf3da` **immutable historical pin, package-superseded** with the dual B snapshot (C math content unchanged; do not cite as current package). Pending dual successor after gate: `v0.3.3-c001-companion` |
| Prior tags | `v0.3.2-c001-companion` @ `61bf3da` (v0.9; do not retag); `v0.3.1-c001-companion` (v0.8; do not retag); `v0.3.0-c001-companion`; `v0.2.0-c001-free-strict` (Regular-v2 **withdrawn**); `v0.1.0-c001-obstruction` |
| Claims | Algebraic \*-SOS; correspondence; C0/Bogoliubov NO-GO; Koopman position **CONSTRUCT**; J2 Joint-Stone-Canonical NO-GO; J3 full-triple Joint-Stone NO-GO (**G4-conditional**, not A001); **J4 Joint-Stone-Hom-1 NO-GO**; **J5 Joint-Stone-CP-1 NO-GO**; **J6 Unitary-Image-CP-1 NO-GO**; **J6-C Diag-CP-Φ₀ CONSTRUCT**; Joint-Form-Core **CONSTRUCT**; Joint-Form-ESS-1 **OBSTRUCT**; **J7-C Full-ψ-BT-Envelope CONSTRUCT** (bounded dual-momentum transforms + Φ₀ positions; form-level only; **not** Full-ψ-CFC / **not** Weyl-C* / **not** Stinespring); **J7 Full-ψ-CFC-SA-1 NO-GO** (reduces to J6 on same joint vNa + normal CP) |
| Joint notes | [`PROGRAM-C-Free-Strict-Abstract-Joint.md`](../validation/PROGRAM-C-Free-Strict-Abstract-Joint.md), [`PROGRAM-C-residual-J4-Joint-Stone-Hom.md`](../validation/PROGRAM-C-residual-J4-Joint-Stone-Hom.md), [`PROGRAM-C-residual-mere-CP-Joint-Stone.md`](../validation/PROGRAM-C-residual-mere-CP-Joint-Stone.md), [`PROGRAM-C-residual-CP-without-Stone.md`](../validation/PROGRAM-C-residual-CP-without-Stone.md), [`PROGRAM-C-residual-abstract-Cstar-full-psi.md`](../validation/PROGRAM-C-residual-abstract-Cstar-full-psi.md) |
| Withdrawn | Free-Strict-Regular-v2 |
| Open | Full-ψ-CP-Weyl-C\* (CP from a completion of \(\mathcal{W}\), no SA-CFC/unitary-image); sub-residual Full-ψ-BT-CP-Bridge |
| Gate status | v0.9 content unchanged by B auto-language erratum; **no Aggregate PASS**; prior package re-gate at `61bf3da` still pending new tags after B erratum gate |

---

## Cite

1. Deficiency: A001 + concept DOI  
2. Classification: B001 v0.7 (erratum: global \(C^\infty\) diffeo language; prior tag `v0.2.2-b001-draft` @ `61bf3da` superseded for auto wording; pin post-gate SHA/tag when cut)  
3. Completions of \(\psi\): C001 v0.9 — cite post-gate `v0.3.3-c001-companion` when cut; prior `v0.3.2` @ `61bf3da` is package-superseded historical pin (C math unchanged)  

## Non-claims
No gates/channels/advantage. No dual-flow repair. No all-quantization-fails. No “all CP impossible.”  
Full-ψ-BT-Envelope is form-level / bounded-transform content only — not Full-ψ-CFC, not Weyl-C*, not Stinespring.  
J3 is G4-conditional (not an A001 theorem).

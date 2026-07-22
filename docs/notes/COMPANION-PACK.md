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

## Companion B001 — classification v0.6

| Artifact | Pin |
|----------|-----|
| PDF | [B001-classification-arxiv.pdf](B001-classification-arxiv.pdf) |
| TeX | [B001-classification-arxiv.tex](B001-classification-arxiv.tex) |
| Marker | [B001-DRAFT-v0.1.md](B001-DRAFT-v0.1.md) (content = v0.6, B6 PARTIAL) |
| Tag / release | [v0.2.1-b001-draft](https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.2.1-b001-draft) (v0.6 freeze SHA; supersedes `v0.2.0-b001-draft`) |
| Prior tags | `v0.2.0-b001-draft` (pre-B6 content pin; do not retag) |
| Atlas | A000–A010; CAS `cas_atlas_A005_A006_B001.json`, `cas_atlas_A007_A008_B001.json`, `cas_atlas_A009_A010_B001.json`, `cas_atlas_B5_poly_dichotomy_B001.json`, `cas_atlas_B6_regime_T_B001.json` |
| Claims | B1 lemma; schema; atlas A000–A010; A007 thin vs A009 open (Pinchuk); **B5 restricted poly dichotomy lemmas**; **B6 regime-T PARTIAL** (T excluded for proper / injective / deg-1 component / product / triangular; reduced to OPEN-T: Bad only on atypical fibers; model \(P_0=x+x^2y\) blocked at low degree); full poly dichotomy still a **conjecture** |
| B5 note | [`PROGRAM-B-B5-poly-dichotomy-lemmas.md`](../validation/PROGRAM-B-B5-poly-dichotomy-lemmas.md) |
| B6 note | [`PROGRAM-B-B6-regime-T.md`](../validation/PROGRAM-B-B6-regime-T.md) |
| Gate status | proof + non-claims surfaces at prior SHA `95a0bc9`; **package surfaces synced this commit**; aggregate pending package re-review |

---

## Companion C001 — Weyl endomorphism packages v0.8

| Artifact | Pin |
|----------|-----|
| PDF | [C001-cp-correspondence-arxiv.pdf](C001-cp-correspondence-arxiv.pdf) |
| TeX | [C001-cp-correspondence-arxiv.tex](C001-cp-correspondence-arxiv.tex) |
| Marker | [C001-FREEZE-v0.1.md](C001-FREEZE-v0.1.md) (content = v0.8; package re-gate in progress) |
| Tag / release | [v0.3.1-c001-companion](https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.3.1-c001-companion) (v0.8 freeze SHA; supersedes `v0.3.0-c001-companion`) |
| Prior tags | `v0.3.0-c001-companion` (pre-re-gate pin; do not retag); `v0.2.0-c001-free-strict` (Regular-v2 **withdrawn**); `v0.1.0-c001-obstruction` |
| Claims | Algebraic \*-SOS; correspondence; C0/Bogoliubov NO-GO; Koopman position **CONSTRUCT**; J2 Joint-Stone-Canonical NO-GO; J3 full-triple Joint-Stone NO-GO (G4); **J4 Joint-Stone-Hom-1 NO-GO**; **J5 Joint-Stone-CP-1 NO-GO**; **J6 Unitary-Image-CP-1 NO-GO**; **J6-C Diag-CP-Φ₀ CONSTRUCT**; Joint-Form-Core **CONSTRUCT**; Joint-Form-ESS-1 **OBSTRUCT** |
| Joint notes | [`PROGRAM-C-Free-Strict-Abstract-Joint.md`](../validation/PROGRAM-C-Free-Strict-Abstract-Joint.md), [`PROGRAM-C-residual-J4-Joint-Stone-Hom.md`](../validation/PROGRAM-C-residual-J4-Joint-Stone-Hom.md), [`PROGRAM-C-residual-mere-CP-Joint-Stone.md`](../validation/PROGRAM-C-residual-mere-CP-Joint-Stone.md), [`PROGRAM-C-residual-CP-without-Stone.md`](../validation/PROGRAM-C-residual-CP-without-Stone.md) |
| Withdrawn | Free-Strict-Regular-v2 |
| Open | Full-\(\psi\) abstract C\* envelope without Hom/unitary-image; CP recovering \(\psi(p_j)\) functional calculus on a C\* completion |
| Gate status | proof + non-claims **PASS** at `95a0bc9`; package **REVISE→fixed** this commit; **aggregate pending package re-review** (do not claim adversarial Aggregate PASS until re-gate) |

---

## Cite

1. Deficiency: A001 + concept DOI  
2. Classification: B001 `v0.2.1-b001-draft` tag (content v0.6)  
3. Completions of \(\psi\): C001 `v0.3.1-c001-companion` tag (v0.8)  

## Non-claims
No gates/channels/advantage. No dual-flow repair. No all-quantization-fails. No “all CP impossible.”

# EXOTIC-CCR companion pack

**Date:** 2026-07-29
**Status:** CURRENT INDEX; A001 is untagged/unreleased and technical re-gating is incomplete
**Rule:** The current A001 review candidate is
`v0.3.9-referee-revision` (proposed, untagged). Earlier candidates remain
historical records and must not be presented as the current freeze.
The project concept DOI is a historical/project-level identifier only; it
does not identify this candidate. External-LLM reviews are advisory and do
not replace the mandatory independent publication gates.

---

## Flagship A001 (unreleased candidate; do not cite as a DOI version)

| Artifact | Pin |
|----------|-----|
| PDF | [A001-arxiv.pdf](A001-arxiv.pdf) |
| Candidate | `v0.3.9-referee-revision` (proposed, untagged; no release or version DOI) |
| Concept DOI | [10.5281/zenodo.21474351](https://doi.org/10.5281/zenodo.21474351) (project-level historical identifier; not this candidate) |
| Endorsement | [A001-endorsement-status.md](A001-endorsement-status.md) — code `VIPN6B`, category **math-ph** |
| Claim | \(H=-iX_1\) has Hilbert indices \(n_+=n_-=\aleph_0\); seed restated; H₁-only |
| Gate status | Lean/build and math.FA/math.AG PASS; fresh non-claims and package/metadata re-gates pending; Dan approval pending |

---

## Companion B001 — classification v0.7

| Artifact | Pin |
|----------|-----|
| PDF | [B001-classification-arxiv.pdf](B001-classification-arxiv.pdf) |
| Current PDF SHA-256 | `ed0472f3fc75dbc2aa12f6989644ffdb42ef0ea15d7bb067813eb2cd36d79747` |
| TeX | [B001-classification-arxiv.tex](B001-classification-arxiv.tex) |
| Marker | [B001-DRAFT-v0.1.md](B001-DRAFT-v0.1.md) (current cross-companion correction; B001 content = v0.7, B7 PARTIAL) |
| Current tag / release | none; corrected candidate is untagged/unreleased |
| Historical release | [v0.2.3-b001-draft](https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.2.3-b001-draft) @ `45e7d53` |
| Prior tags | `v0.2.2-b001-draft` @ `61bf3da` (v0.7 pre-erratum auto wording; do not retag); `v0.2.1-b001-draft` (v0.6; do not retag); `v0.2.0-b001-draft` (pre-B6; do not retag) |
| Atlas | A000–A010; CAS `cas_atlas_A005_A006_B001.json`, `cas_atlas_A007_A008_B001.json`, `cas_atlas_A009_A010_B001.json`, `cas_atlas_B5_poly_dichotomy_B001.json`, `cas_atlas_B6_regime_T_B001.json`, `cas_atlas_B7_OPEN_T_B001.json` |
| Claims | B1 lemma; schema; atlas A000–A010; A007 thin vs A009 open (Pinchuk); **B5 restricted poly dichotomy lemmas**; **B6 regime-T PARTIAL**; **B7 OPEN-T sharpened** (affine-invariant graph-type / \(\deg P\le 2\) ⇒ **global \(C^\infty\) diffeo** / regime E — not automatic poly inverse over \(\mathbb{R}\); T-filter deg≥3 non-coordinate; \(P_0\)-axis cannot carry T; CAS through deg 8); full poly dichotomy still a **conjecture** |
| B5 note | [`PROGRAM-B-B5-poly-dichotomy-lemmas.md`](../validation/PROGRAM-B-B5-poly-dichotomy-lemmas.md) |
| B6 note | [`PROGRAM-B-B6-regime-T.md`](../validation/PROGRAM-B-B6-regime-T.md) |
| B7 note | [`PROGRAM-B-B7-OPEN-T.md`](../validation/PROGRAM-B-B7-OPEN-T.md) |
| Gate status | B001 mathematics unchanged; historical `45e7d53` PASS does not approve the current cross-companion correction |

---

## Companion C001 — Weyl endomorphism packages v0.9 claim-boundary correction

| Artifact | Pin |
|----------|-----|
| PDF | [C001-cp-correspondence-arxiv.pdf](C001-cp-correspondence-arxiv.pdf) |
| Current PDF SHA-256 | `7a3558063166ad044cda1dd8e8a258bad3edb07c3b90cf3fc111d2f26b115d04` |
| TeX | [C001-cp-correspondence-arxiv.tex](C001-cp-correspondence-arxiv.tex) |
| Marker | [C001-FREEZE-v0.1.md](C001-FREEZE-v0.1.md) (current correction status) |
| Current tag / release | none; corrected candidate is untagged/unreleased |
| Historical release | [v0.3.3-c001-companion](https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.3.3-c001-companion) @ `45e7d53` (contains withdrawn J3; do not relabel) |
| Prior tags | `v0.3.2-c001-companion` @ `61bf3da` (v0.9; do not retag); `v0.3.1-c001-companion` (v0.8; do not retag); `v0.3.0-c001-companion`; `v0.2.0-c001-free-strict` (Regular-v2 **withdrawn**); `v0.1.0-c001-obstruction` |
| Claims | Algebraic \*-SOS; correspondence; C0/Bogoliubov NO-GO; Koopman position **CONSTRUCT**; J2 Joint-Stone-Canonical NO-GO (H1 only); historical J3 full-triple claim **WITHDRAWN / OPEN pending Lean**; **J4 Joint-Stone-Hom-1 NO-GO**; **J5 Joint-Stone-CP-1 NO-GO**; **J6 Unitary-Image-CP-1 NO-GO**; **J6-C Diag-CP-Φ₀ CONSTRUCT**; Joint-Form-Core **CONSTRUCT**; Joint-Form-ESS-1 **OBSTRUCT**; **J7-C Full-ψ-BT-Envelope CONSTRUCT** (bounded dual-momentum transforms + Φ₀ positions; form-level only; **not** Full-ψ-CFC / **not** Weyl-C* / **not** Stinespring); **J7 Full-ψ-CFC-SA-1 NO-GO** (reduces to J6 on same joint vNa + normal CP) |
| Joint notes | [`PROGRAM-C-Free-Strict-Abstract-Joint.md`](../validation/PROGRAM-C-Free-Strict-Abstract-Joint.md), [`PROGRAM-C-residual-J4-Joint-Stone-Hom.md`](../validation/PROGRAM-C-residual-J4-Joint-Stone-Hom.md), [`PROGRAM-C-residual-mere-CP-Joint-Stone.md`](../validation/PROGRAM-C-residual-mere-CP-Joint-Stone.md), [`PROGRAM-C-residual-CP-without-Stone.md`](../validation/PROGRAM-C-residual-CP-without-Stone.md), [`PROGRAM-C-residual-abstract-Cstar-full-psi.md`](../validation/PROGRAM-C-residual-abstract-Cstar-full-psi.md) |
| Withdrawn | Free-Strict-Regular-v2 |
| Open | Full-ψ-CP-Weyl-C\* (CP from a completion of \(\mathcal{W}\), no SA-CFC/unitary-image); sub-residual Full-ψ-BT-CP-Bridge |
| Gate status | current correction: fresh non-claims and package/metadata review pending; historical `45e7d53` PASS does not approve this correction |

---

## Cite

1. Deficiency: cite no unreleased A001 version; the concept DOI does not identify the current candidate
2. Classification: do not cite the corrected B001 candidate until re-gated; historical `v0.2.3-b001-draft` does not identify its current PDF
3. Completions of \(\psi\): do not cite the corrected C001 candidate until re-gated; historical `v0.3.3-c001-companion` contains withdrawn J3

## Non-claims
No gates/channels/advantage. No dual-flow repair. No all-quantization-fails. No “all CP impossible.”  
Full-ψ-BT-Envelope is form-level / bounded-transform content only — not Full-ψ-CFC, not Weyl-C*, not Stinespring.  
Historical J3 is withdrawn; H0/H2 and the full-triple Joint-Stone question
remain open pending Lean.

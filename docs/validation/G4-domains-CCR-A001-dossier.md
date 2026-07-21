# G4 Domains / self-adjointness / strong CCR — A001

**Status:** Incompleteness **proved**; ESS failure **conditional on Chernoff**  
**Date:** 2026-07-21  
**Story:** S020  

## Documents
- Attack plan: [`G4-ESS-attack-plan.md`](G4-ESS-attack-plan.md)
- **Incompleteness theorem:** [`G4-Xj-incompleteness.md`](G4-Xj-incompleteness.md)
- Conditional ESS lemma: [`G4-conditional-obstruction-lemma.md`](G4-conditional-obstruction-lemma.md)
- Geometry CAS: `data/anchor/cas_incompleteness_geometry_A001.json`
- Numeric probes (supplementary): `data/anchor/cas_dual_fields_A001_probe.json`

## 1. Setup
\(B=J^{-T}\), \(X_j=\sum_k B_{jk}\partial_{q_k}\), \(P_j^{\mathrm{sym}}=-i X_j\) (\(\mathrm{div} X_j=0\)).

## 2. Certified / proved facts
| Fact | Status |
|------|--------|
| \(\det J=-2\), local diffeomorphism | **certified** (G0) |
| \(\mathrm{div} X_j=0\), \(P^{\mathrm{sym}}=-iX\) | **certified** (G3) |
| Formal symmetry on \(\mathcal{S}\) | **certified** |
| \(F(\mathbb{R}^3)\neq\mathbb{R}^3\) (misses e.g. \(\gamma_\star\)) | **proved** (+ CAS support) |
| **∃ j with \(X_j\) incomplete** | **proved** (geometric) |
| ESS failure for that \(P_j^{\mathrm{sym}}\) | **conditional** on Chernoff-type criterion |

## 3. Proof idea (incompleteness)
If all \(X_j\) were complete, \(F(\mathbb{R}^3)\) would be invariant under all coordinate translations ⇒ \(F(\mathbb{R}^3)=\mathbb{R}^3\). But \(F\) omits real points of the complex omitted set \(\Gamma\) (e.g. \(\gamma_\star=(1/12,1,4/3)\)). Contradiction.

## 4. Claims ledger
| ID | Status |
|----|--------|
| G4-formal-symmetric | **certified** |
| G4-Xj-incomplete-exists | **proved** |
| G4-ESS-failure-conditional | **stated** (needs Chernoff hypotheses) |
| G4-ESS-failure-unconditional | **open** (pin Chernoff growth) |
| G4-which-j | **open** |
| G4-strong-CCR | **open** |
| G4-physical-symmetry | **not authorized** without ESS+strong CCR+implementability package |

## 5. Physical reading (careful)
Under a standard Chernoff completeness criterion applicable to these polynomial dual fields, **at least one** transformed momentum fails ESS on \(C_c^\infty\). That blocks the naive “all \(P_j^{\mathrm{sym}}\) are observables with unique spectral theorem on the Schwartz domain” route. It is **not** yet a fully referenced, growth-checked citation package; treat ESS failure as **conditional**.

## 6. Non-claims
No channel/gate/advantage. No claim all three \(P_j\) fail ESS. No G5 index.

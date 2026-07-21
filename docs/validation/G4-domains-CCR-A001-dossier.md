# G4 Domains / self-adjointness / strong CCR — A001

**Status:** **ESS obstruction proved** (existential over \(j\)); strong CCR still open  
**Date:** 2026-07-21  
**Story:** S020  

## Documents
| Doc | Content |
|-----|---------|
| [`G4-Xj-incompleteness.md`](G4-Xj-incompleteness.md) | ∃ incomplete dual field **proved** |
| [`G4-Chernoff-discharge.md`](G4-Chernoff-discharge.md) | Transport necessity ⇒ ESS fails |
| [`G4-ESS-attack-plan.md`](G4-ESS-attack-plan.md) | Dual fields / formal symmetry |
| [`G4-conditional-obstruction-lemma.md`](G4-conditional-obstruction-lemma.md) | Superseded in strength by Chernoff discharge |

## 1. Setup
\(X_j=\sum_k B_{jk}\partial_k\), \(B=J^{-T}\), \(\mathrm{div} X_j=0\), \(P_j^{\mathrm{sym}}=-i X_j\) on \(C_c^\infty(\mathbb{R}^3)\).

## 2. Main results
| Result | Status |
|--------|--------|
| Formal symmetry of each \(P_j^{\mathrm{sym}}\) | **certified** |
| \(F(\mathbb{R}^3)\neq\mathbb{R}^3\) | **proved** |
| ∃ j: \(X_j\) incomplete | **proved** |
| **∃ j: \(P_j^{\mathrm{sym}}\) not ESS on \(C_c^\infty\)** | **proved** (incompleteness + transport necessity / Stone) |
| Which j | **open** |
| Strong CCR / joint spectral theorem package | **open** |
| Canonical physical momentum observables without boundary choices | **not authorized** |

## 3. Proof chain (ESS obstruction)
1. Dual fields exist, smooth, divergence-free (G0/G3).  
2. If all \(X_j\) complete ⇒ \(F\) surjective on \(\mathbb{R}^3\) — false (`G4-Xj-incompleteness.md`).  
3. Hence some \(X_j\) incomplete.  
4. For divergence-free smooth \(X\) on \(\mathbb{R}^n\), incompleteness ⇒ \(-iX\) not ESS on \(C_c^\infty\) (`G4-Chernoff-discharge.md`, Theorem N).  
5. Therefore some \(P_j^{\mathrm{sym}}\) is not essentially self-adjoint.

## 4. Physical reading (bounded)
Failure of ESS means the formal momentum \(P_j^{\mathrm{sym}}\) does **not** determine a **unique** self-adjoint observable from the \(C_c^\infty\) / Schwartz recipe alone: extensions (boundary conditions at infinity / incomplete ends) are required. This is a genuine obstruction to the naive “algebraic CCR generators ⇒ unique quantum momenta” reading. It is **not** a claim that no quantum theory exists, nor a gate/channel claim.

## 5. Claims ledger
| ID | Status |
|----|--------|
| G4-formal-symmetric | **certified** |
| G4-Xj-incomplete-exists | **proved** |
| G4-ESS-failure-exists | **proved** |
| G4-ESS-which-j | **open** |
| G4-deficiency-indices | **open** |
| G4-strong-CCR | **open** |
| G4-physical-symmetry / unique observables | **not authorized** |

## 6. Non-claims
No channel/gate/advantage. No G5 index. No claim all three momenta fail ESS.

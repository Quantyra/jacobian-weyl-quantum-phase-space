# G3 Weyl pilot — A001-seed-d3

**Status:** CLOSED (polynomial Weyl algebra)  
**Date:** 2026-07-21  
**Story:** S019

## Definition
Algebraic Weyl algebra over \(\mathbb{Q}\) with \([q_i,p_j]=\delta_{ij}\) (\(\hbar=1\)):
\[
\psi:\quad Q_i=F_i(q),\qquad P_j=\sum_k B_{jk}(q)\,p_k,\quad B=J^{-T}.
\]
Freeze: `data/anchor/psi_weyl_A001.json`.

## Dual CAS
| Check | SymPy | Pure-Python |
|-------|-------|-------------|
| \([Q_i,Q_j]=0\) | PASS | (auto) |
| \([Q_i,P_j]=\delta_{ij}\) | \(JB^T=I\) PASS | 25/25 |
| \([P_i,P_j]=0\) | coeff identities PASS | 25/25 |
| row-div \(B=0\) | PASS (all rows) | — |

Reports: `cas_weyl_A001_sympy_report.json`, `cas_weyl_A001_purepython_report.json`.

## Claims
| ID | Status |
|----|--------|
| G3-A001-endomorphism | **certified** (poly Weyl CCR relations) |
| G3-proper | **supported** by classical non-injectivity of \(\Phi\) / non-auto of \(F\) |
| G4 self-adjointness | **not claimed** |

## Non-claims
Not essential self-adjointness, strong Weyl form, \(C^*\) extension, channel, gate, or advantage.

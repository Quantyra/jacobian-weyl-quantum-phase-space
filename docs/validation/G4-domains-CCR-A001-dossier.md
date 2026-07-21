# G4 Domains / self-adjointness / strong CCR — A001

**Status:** **\(X_1\) incomplete proved; \(P_1^{\mathrm{sym}}\) not ESS proved**; strong CCR open  
**Date:** 2026-07-21  

## Documents
| Doc | Content |
|-----|---------|
| [`G4-X1-incompleteness.md`](G4-X1-incompleteness.md) | **\(j=1\)** explicit blow-up curve |
| [`G4-Xj-incompleteness.md`](G4-Xj-incompleteness.md) | Existential incompleteness (any \(j\)) |
| [`G4-Chernoff-discharge.md`](G4-Chernoff-discharge.md) | incomplete ⇒ not ESS |
| CAS | `data/anchor/cas_X1_blowup_curve_A001.json` |

## Main results
| Result | Status |
|--------|--------|
| \(X_1\) incomplete on \(\mathbb{R}^3\) | **proved** (explicit \(\gamma(t)\), escape at \(t=\tfrac12\)) |
| \(P_1^{\mathrm{sym}}=-i X_1\) not ESS on \(C_c^\infty\) | **proved** |
| Deficiency indices \((n_+,n_-)\) | **open** (only \(\max(n_+,n_-)\ge 1\)) |
| Status of \(P_0^{\mathrm{sym}},P_2^{\mathrm{sym}}\) | **not settled here** |
| Strong CCR | **open** |

## Explicit curve (summary)
Through \(q_\star=(1,0,0)\), for \(t\in[0,\tfrac12)\):
\[
q_1=t,\quad
q_0=\frac{-2t-\sqrt{1-2t}+1}{t(2t-1)}\ (q_0(0)=1),\quad
F(q(t))=(0,t,2),\quad
q'(t)=X_1(q(t)),\quad
q_0(t)\to+\infty\ (t\to\tfrac12^-).
\]

## Claims ledger
| ID | Status |
|----|--------|
| G4-formal-symmetric | **certified** |
| G4-X1-incomplete | **proved** |
| G4-P1-not-ESS | **proved** |
| G4-deficiency-indices-exact | **open** |
| G4-P0-P2-ESS | **open** |
| G4-strong-CCR | **open** |
| G4-physical-unique-momenta | **not authorized** |

## Non-claims
No channel/gate/advantage. No claim all three momenta fail ESS.

# G4 Domains / self-adjointness / strong CCR — A001

**Status:** \(X_1\) incomplete + \(P_1^{\mathrm{sym}}\) not ESS **proved**; deficiency indices **bounded / modeled**  
**Date:** 2026-07-21  

## Documents
| Doc | Content |
|-----|---------|
| [`G4-X1-incompleteness.md`](G4-X1-incompleteness.md) | \(X_1\) explicit blow-up |
| [`G4-P1-deficiency-indices.md`](G4-P1-deficiency-indices.md) | **deficiency index bounds + plan** |
| [`G4-Chernoff-discharge.md`](G4-Chernoff-discharge.md) | not ESS from incompleteness |

## Results
| Item | Status |
|------|--------|
| \(X_1\) incomplete | **proved** |
| \(P_1^{\mathrm{sym}}\) not ESS | **proved** |
| \(\max(n_+,n_-)\ge 1\) | **proved** |
| Orbit through \((1,0,0)\): time \((-\infty,\tfrac12)\) | **proved** (forward finite end, backward complete) |
| 1D orbit model indices | **\((1,0)\) or \((0,1)\)** (orientation) |
| Exact global \((n_+,n_-)\) on \(L^2(\mathbb{R}^3)\) | **open** |
| Strong CCR | **open** |

## Deficiency indices (summary)
\[
(n_+,n_-)\neq(0,0),\quad \max(n_+,n_-)\ge 1.
\]
Distinguished orbit model predicts half-line indices \(\{(1,0),(0,1)\}\).  
Global exact pair requires orbit-measure analysis (plan in deficiency note §5).

## Claims ledger
| ID | Status |
|----|--------|
| G4-X1-incomplete | **proved** |
| G4-P1-not-ESS | **proved** |
| G4-def-max-ge-1 | **proved** |
| G4-def-orbit-model-half-line | **proved** |
| G4-def-incomplete-2D-sheet | **proved** (\(\Sigma_0\subset\{F_0=0\}\)) |
| G4-def-Lebesgue-positive | **proved** (IFT + local diffeo) |
| G4-def-max-index-infinite | **proved** |
| G4-def-global-exact-pair | **open** (\((\infty,0)\) vs \((0,\infty)\) vs \((\infty,\infty)\)) |
| G4-physical-unique-momenta | **not authorized** |

**Orbit-measure analysis:** `G4-P1-orbit-measure-deficiency.md`

## Non-claims
No channel/gate/advantage. Infinite deficiency for \(P_1^{\mathrm{sym}}\) blocks unique ESS momenta; it does not imply a computational gate/channel.

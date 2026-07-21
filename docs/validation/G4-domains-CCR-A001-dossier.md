# G4 Domains / self-adjointness / strong CCR — A001

**Status:** ADVANCED obstruction package (still not a full ESS theorem)  
**Date:** 2026-07-21  
**Story:** S020  
**Attack plan:** [`G4-ESS-attack-plan.md`](G4-ESS-attack-plan.md)  
**Conditional lemma:** [`G4-conditional-obstruction-lemma.md`](G4-conditional-obstruction-lemma.md)

## 1. Setup (Schrödinger representation)
On \(L^2(\mathbb{R}^3)\), \(q_i=\) multiplication, \(p_j=-i\partial_j\) (\(\hbar=1\)).  
\(B=J^{-T}\), dual fields \(X_j=\sum_k B_{jk}(q)\partial_{q_k}\).  
Because \(\mathrm{div}\,X_j=0\) (G3),
\[
P_j^{\mathrm{sym}}
=
\frac12\sum_k\{B_{jk},p_k\}
=
-i X_j
=
P_j^{\mathrm{left}}.
\]

## 2. Certified formal facts
| Fact | Status | Evidence |
|------|--------|----------|
| \(\mathrm{div}\,X_j=0\) | **certified** | G3 CAS `div_B_rows=[0,0,0]` |
| \(P_j^{\mathrm{sym}}=-i X_j\) | **certified** | ordering + div 0 |
| Formal symmetry on \(\mathcal{S}\) | **certified** | integration by parts |
| Polynomial Weyl \(\psi\) (G3) | **certified** | G3 dossier |

## 3. Conditional ESS obstruction (theorem-shaped, not fully fired)
See `G4-conditional-obstruction-lemma.md`.

**If** a Chernoff-type completeness criterion applies to \(X_j\) **and** \(X_j\) is incomplete,  
**then** \(P_j^{\mathrm{sym}}\) is not ESS on \(C_c^\infty\).

Missing discharge: **incompleteness proof** for some \(X_j\); pin Chernoff reference growth hypotheses.

## 4. Numeric dual-field probes (not a proof)
Script: `scripts/cas/probe_dual_fields_A001.py`  
Report: `data/anchor/cas_dual_fields_A001_probe.json`

- Multiple `solve_ivp` trajectories for \(X_0,X_1,X_2\) hit **step-size collapse** with \(|q|\sim 10^4\)–\(10^6\).  
- Striking pattern for \(X_1\) from \((s_0,0,0)\), \(s_0>0\): failure time matches
  \[
  t_\star \approx \frac{2}{3 s_0}
  \]
  (the blow-up time of \(\dot s=\tfrac32 s^2\)), e.g. \(s_0=1\Rightarrow t\approx 0.5\), \(s_0=0.5\Rightarrow t\approx 1\), \(s_0=2\Rightarrow t\approx 0.25\).  
- Axis model \(X_1(s,0,0)=(\tfrac32 s^2,1,0)\) is **not invariant** (\(q_1'=1\)) — comparison only.

**O1 status:** incompleteness **strongly supported numerically**, **not theorem-certified**.

## 5. Obstruction routes
| Route | Status |
|-------|--------|
| O1 Incomplete dual fields | **Primary**; conditional lemma ready; incompleteness open |
| O2 Deficiency indices | not computed |
| O3 Strong CCR failure | open |
| O4 Nonregular reps | open |

## 6. Claims ledger (updated)
| ID | Status |
|----|--------|
| G4-formal-symmetric | **certified** |
| G4-Psym-equals-minus-iX | **certified** |
| G4-conditional-Chernoff-bridge | **stated** (applicability assumed) |
| G4-Xj-incomplete | **open** (numeric support) |
| G4-ESS-failure | **open** (needs incompleteness) |
| G4-strong-CCR | **open** |
| G4-physical-symmetry | **not authorized** |

## 7. Single next analytic obligation
**Prove incompleteness of at least one dual field \(X_j\) on \(\mathbb{R}^3\).**  
Then fire the conditional lemma (with pinned Chernoff citation + growth check) to obtain ESS failure.

## 8. Non-claims
No unconditional ESS failure theorem; no channel/gate/advantage language; numeric blow-up ≠ proof.

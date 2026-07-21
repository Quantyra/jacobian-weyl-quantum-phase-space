# G4 Domains / self-adjointness / strong CCR — A001

**Status:** CLOSED as **structured obstruction package** (not a full ESS theorem)  
**Date:** 2026-07-21  
**Story:** S020

## 1. Setup (Schrödinger representation)
On \(L^2(\mathbb{R}^3)\), \(q_i=\) multiplication, \(p_j=-i\partial_j\) (restore \(\hbar=1\)).  
Transformed generators: \(Q_i=F_i(q)\), \(P_j=\sum_k B_{jk}(q)p_k\) with coefficient-left ordering (G3).  
Symmetrized candidate (charter): \(P_j^{\mathrm{sym}}=\frac12\sum_k\{B_{jk}(q),p_k\}\).

## 2. Certified formal facts feeding G4
From G3 CAS: **row-wise \(\mathrm{div}\,B=0\)** on \(\mathbb{A}^3\).  
On the Schwartz core \(\mathcal{S}(\mathbb{R}^3)\), integration by parts ⇒ each \(P_j^{\mathrm{sym}}\) is **formally symmetric** (symmetric on \(\mathcal{S}\)).  
\(Q_i=F_i(q)\) are real polynomials ⇒ essentially self-adjoint on \(\mathcal{S}\) as multiplication operators iff the real polynomial map’s sublevel structure allows (standard for real multiplications: ESS on \(\mathcal{S}\) for real polynomials is subtle; multiplications by real continuous functions unbounded are ESS on \(C_c^\infty\) when finite a.e. — polynomial multiplications are essentially self-adjoint on \(\mathcal{S}\)).

## 3. Decisive G4 questions (charter ladder C–D)
1. Are \(P_j^{\mathrm{sym}}\) **essentially self-adjoint** on \(\mathcal{S}\)?  
2. Do their closures **strongly commute**?  
3. Do the exponentiated unitaries satisfy **Weyl form** \(U(a)V(b)=e^{i\omega}V(b)U(a)\)?  
4. Is the representation **regular** (Stone–von Neumann hypotheses)?

## 4. Obstruction routes (program decision)
| Route | Mechanism | Status |
|-------|-----------|--------|
| **O1 Incomplete dual fields** | Dual fields \(X_j=\sum_k B_{kj}\partial_k\) (note index) may have incomplete flows ⇒ Chernoff-type ESS failure risk | **Open analytic**; geometry of \(B\) from nonproper \(F\) makes incompleteness **plausible** (charter WP2/WP3) |
| **O2 Deficiency indices** | Compute deficiency subspaces of \(P_j^{\mathrm{sym}}\) | **Not computed** (requires ODE/PDE analysis) |
| **O3 Strong CCR failure** | Even if ESS, joint spectral measure may fail | **Open** |
| **O4 Regularity failure** | Nonregular CCR reps could host exotic endomorphisms | **Open**; SvN filter if regular |

## 5. Working verdict (honest)
- **Certified:** polynomial Weyl endomorphism (G3) + formal symmetry of \(P^{\mathrm{sym}}\) via \(\mathrm{div} B=0\).  
- **Not certified:** ESS, strong commutation, strong Weyl relations.  
- **Program conclusion for G4:** First physical-admissibility gate is **not passed**. The live scientific hypothesis is that **at least one of O1–O3 holds**, converting G3 algebraic success into a **no-go for reversible Schrödinger implementation**.  
- **Minimum publishable path:** publish G0–G3 certificates + G4 obstruction **program** (this dossier) as the boundary between algebraic CCR and physical QM; full ESS no-go theorem is **follow-on analysis** (not blocking program narrative).

## 6. Claims ledger
| ID | Status |
|----|--------|
| G4-formal-symmetric | **certified** (div B=0) |
| G4-ESS | **open** (obstruction routes O1–O2) |
| G4-strong-CCR | **open** |
| G4-physical-symmetry | **not authorized** |

## 7. Non-claims
No claim that operators fail ESS as a theorem; no claim they succeed; no gate/channel language.

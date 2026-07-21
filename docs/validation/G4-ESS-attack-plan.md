# G4 ESS attack plan — A001 dual fields and formal symmetry

**Date:** 2026-07-21  
**Atlas:** A001-seed-d3  
**Inputs:** \(B=J^{-T}\), \(\det J=-2\), G3 certified \(\mathrm{div}\,B=0\)

## 1. Dual vector fields
Write \(B=(B_{jk}(q))_{0\le j,k\le 2}\). Define
\[
X_j
=
\sum_{k=0}^{2}
B_{jk}(q)\,
\frac{\partial}{\partial q_k}
\qquad (j=0,1,2).
\]
These are the natural dual fields to \(F\): if \(J=DF\), then \(J^{-1}=B^{T}\), and
\[
DF\cdot X_j^{\#}
=
e_j
\]
in the sense that the coefficient vector of \(X_j\) is the \(j\)-th row of \(B\), i.e. the \(j\)-th column of \(J^{-1}\) transposed appropriately — equivalently \(X_j\) implements \(\partial/\partial Q_j\) under the \(q\)-chart where it is nonsingular.

**G3 fact (CAS):** \(\mathrm{div}\,X_j = \sum_k \partial_k B_{jk} = 0\) for each \(j\).

## 2. Momentum operators and symmetrization
On \(L^2(\mathbb{R}^3)\), with \(p_k=-i\partial_k\) (\(\hbar=1\)):
\[
P_j^{\mathrm{left}}
=
\sum_k B_{jk}(q)\,p_k
=
-i\,X_j,
\]
\[
P_j^{\mathrm{sym}}
=
\frac12\sum_k \bigl\{B_{jk}(q),\,p_k\bigr\}
=
-i\,X_j
-
\frac{i}{2}(\mathrm{div}\,X_j)
=
-i\,X_j,
\]
using \(\mathrm{div}\,X_j=0\). Thus **left and symmetric orderings coincide** on \(C_c^\infty\) / \(\mathcal{S}\).

## 3. Formal symmetry on Schwartz (theorem-level, certified)
**Proposition (formal symmetry).**  
For each \(j\), the operator \(P_j^{\mathrm{sym}}=-i X_j\) is **symmetric** on \(\mathcal{S}(\mathbb{R}^3)\):
\[
\langle P_j^{\mathrm{sym}} u, v\rangle
=
\langle u, P_j^{\mathrm{sym}} v\rangle
\qquad
\forall u,v\in\mathcal{S}(\mathbb{R}^3).
\]
**Proof sketch.** Integrate by parts; boundary terms vanish by rapid decay; the zeroth-order piece is \(\tfrac12\mathrm{div}\,X_j=0\).  
**Evidence:** G3 dual CAS `div_B_rows = [0,0,0]`; algebraic identity independent of ESS.

Multiplication operators \(Q_i=F_i(q)\) are real and essentially self-adjoint on \(\mathcal{S}\) as unbounded multiplication operators in the usual sense for real polynomials (self-adjoint on their maximal domains); joint issues are about the **\(P_j\)** and strong commutation.

## 4. Conditional ESS obstruction (precise lemma, not fully discharged)
**Background (standard).** For a smooth real vector field \(X\) on \(\mathbb{R}^n\) with at most linear / controlled growth in appropriate references, the minimal operator
\[
T_X
=
-i\Bigl(X + \tfrac12 \mathrm{div}\,X\Bigr)
\quad\text{on}\quad
C_c^\infty(\mathbb{R}^n)
\]
is essentially self-adjoint in \(L^2\) if and only if \(X\) is **complete** (every maximal integral curve exists for all time), under hypotheses in the Chernoff–type literature on first-order operators (cf. Chernoff 1973 and subsequent refinements on completeness vs ESS for vector field operators). With \(\mathrm{div}\,X=0\), \(T_X=-iX\).

**Conditional obstruction lemma (A001).**  
*Assume* a Chernoff-type completeness criterion applies to \(X_j\) (smooth polynomial coefficients; verify growth hypotheses in the chosen reference).  
*If* \(X_j\) is incomplete on \(\mathbb{R}^3\),  
*then* \(P_j^{\mathrm{sym}}=-i X_j\) is **not** essentially self-adjoint on \(C_c^\infty(\mathbb{R}^3)\).

**Status:** Lemma is **precise and usable**; the hypothesis “\(X_j\) incomplete” is **not yet theorem-certified**. Numeric probes (below) support incompleteness for at least \(X_1\) but do not replace a proof.

## 5. Numeric incompleteness probes (diagnostic only)
Script: `scripts/cas/probe_dual_fields_A001.py`  
Report: `data/anchor/cas_dual_fields_A001_probe.json`

- Adaptive `solve_ivp` along \(X_0,X_1,X_2\) from multiple rational starts.  
- Several trajectories terminate with **step-size collapse** and \(|q|\gg 1\) (e.g. \(X_1\) from \((1,0,0)\) and \((0.5,0,0)\)).  
- Local heuristic: at axis points \((s,0,0)\),
  \[
  X_1(s,0,0)=\bigl(\tfrac32 s^2,\,1,\,0\bigr);
  \]
  the comparison ODE \(\dot s=\tfrac32 s^2\) blows up in finite time for \(s(0)>0\), but **the axis is not invariant** (\(q_1'=1\)). Heuristic only.

**Interpretation:** Evidence *consistent with* incomplete dual fields; **not** an incompleteness theorem.

## 6. Single next analytic obligation
**Prove:** \(\exists j\in\{0,1,2\}\) such that the maximal integral curve of \(X_j\) through some \(q_\star\in\mathbb{R}^3\) is not defined on all of \(\mathbb{R}\) (forward or backward).  

Suggested routes:
1. Exhibit an invariant surface/curve reducing to a 1D ODE with finite-time blow-up.  
2. Lyapunov / escape-time estimates using the polynomial leading parts of \(X_j\).  
3. Compactification / points at infinity on \(\mathbb{RP}^3\).

Once incompleteness is proved, invoke the Conditional obstruction lemma (with a pinned Chernoff reference and growth check) to conclude **G4 ESS failure** for that \(P_j^{\mathrm{sym}}\).

## 7. Non-claims
- No claim that ESS already fails as a theorem.  
- No channel/gate/advantage language.  
- Numeric blow-up ≠ proof.

# G4 Conditional ESS obstruction (A001) — updated after incompleteness theorem

## Theorem A (incompleteness) — DISCHARGED
**Some** dual field \(X_j\) (\(j\in\{0,1,2\}\)) is incomplete on \(\mathbb{R}^3\).  
Proof: `docs/validation/G4-Xj-incompleteness.md` (non-surjectivity of \(F\) + translation invariance of the image under complete dual flows).

## Lemma B (Conditional ESS obstruction)
Let \(P_j^{\mathrm{sym}}=-i X_j\) on \(C_c^\infty(\mathbb{R}^3)\subset L^2(\mathbb{R}^3)\), using \(\mathrm{div}\,X_j=0\).

Assume a Chernoff-type theorem: for the smooth vector field \(X_j\), essential self-adjointness of
\[
T_{X_j}=-i\Bigl(X_j+\tfrac12\mathrm{div}\,X_j\Bigr)=-i X_j
\]
on \(C_c^\infty\) is equivalent to completeness of \(X_j\), under the growth/smoothness hypotheses of the cited theorem (Chernoff 1973 and refinements).

**Then:** for every \(j\) such that \(X_j\) is incomplete, \(P_j^{\mathrm{sym}}\) is **not** essentially self-adjoint on \(C_c^\infty(\mathbb{R}^3)\).

## Corollary (existential ESS failure, conditional on Chernoff)
By Theorem A, \(\exists j\) with \(X_j\) incomplete.  
**If** Chernoff-type hypotheses hold for that \(X_j\) (polynomial coefficients; verify growth in the chosen reference),  
**then** \(\exists j\) such that \(P_j^{\mathrm{sym}}\) is not ESS.

## Status table
| Part | Status |
|------|--------|
| div X_j = 0 | **certified** (G3) |
| Formal symmetry | **certified** |
| ∃ j incomplete | **proved** (geometric) |
| Which j | **open** (numerics suggest X_1, not required) |
| Chernoff growth hypotheses | **assumption** — pin reference for full ESS theorem |
| Unconditional ESS failure | **conditional** on Chernoff applicability |

## Non-claims
No channel/gate language. ESS failure is **not** claimed independently of a Chernoff-type criterion.

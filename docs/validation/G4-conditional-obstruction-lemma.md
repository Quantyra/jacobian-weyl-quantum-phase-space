# G4 Conditional obstruction lemma (A001)

## Lemma (Conditional ESS obstruction)
Let \(B=J^{-T}\) for the A001 seed map \(F\), and let
\[
X_j=\sum_k B_{jk}(q)\partial_{q_k},\qquad
P_j^{\mathrm{sym}}=-i X_j
\quad\text{on }C_c^\infty(\mathbb{R}^3)\subset L^2(\mathbb{R}^3).
\]
Assume a Chernoff-type theorem applies to \(X_j\): essential self-adjointness of \(-i(X_j+\tfrac12\mathrm{div} X_j)\) on \(C_c^\infty\) is equivalent to completeness of \(X_j\) (under the growth/smoothness hypotheses of the cited theorem). Since \(\mathrm{div} X_j=0\) (G3 CAS), this is ESS of \(P_j^{\mathrm{sym}}\).

**Then:** if \(X_j\) is incomplete, \(P_j^{\mathrm{sym}}\) is **not** essentially self-adjoint on \(C_c^\infty(\mathbb{R}^3)\).

## Discharged parts
| Part | Status |
|------|--------|
| \(\mathrm{div} X_j=0\) | **Certified** (G3 dual CAS) |
| \(P^{\mathrm{sym}}=-iX\) | **Certified** (ordering identity) |
| Formal symmetry on \(\mathcal{S}\) | **Certified** (integration by parts) |
| Chernoff bridge applicability (growth) | **Assumption** — pin reference in follow-on |
| Incompleteness of some \(X_j\) | **Open** (numeric support only) |

## Gap (single obligation)
Prove incompleteness of at least one dual field \(X_j\) on \(\mathbb{R}^3\).

## Non-claims
This file does **not** assert ESS failure unconditionally.

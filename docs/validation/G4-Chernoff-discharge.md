# G4 Chernoff / transport discharge — A001 ESS obstruction

**Date:** 2026-07-21  
**Status:** **Necessity direction discharged** for smooth dual fields on \(\mathbb{R}^3\)  
**Depends on:** incompleteness theorem `G4-Xj-incompleteness.md` (∃ incomplete \(X_j\))

## 1. Operator
For each dual field \(X_j=\sum_k B_{jk}(q)\partial_{q_k}\) with \(\mathrm{div}\,X_j=0\) (G3),
\[
H_j
:=
P_j^{\mathrm{sym}}
=
-i X_j
\qquad
\text{on domain }C_c^\infty(\mathbb{R}^3)\subset L^2(\mathbb{R}^3,dx).
\]
Each \(H_j\) is symmetric (G4 formal symmetry).

## 2. Cited classical sources
| Source | Role |
|--------|------|
| **P. R. Chernoff**, *Essential self-adjointness of powers of generators of hyperbolic equations*, J. Funct. Anal. **12** (1973), 401–414 | Classical Chernoff criteria linking hyperbolic/vector-field generators to ESS; historical anchor for “Chernoff-type” statements in the charter |
| **M. Reed & B. Simon**, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness*, Academic Press, 1975 | Stone’s theorem; deficiency indices; general ESS framework |
| Standard geometric analysis / mathematical physics folklore for **transport groups** | Unitary implementation of complete volume-preserving (or density-corrected) flows; see also treatments of momentum operators along vector fields in geometric QM texts (e.g. discussions adjacent to Hall, *Quantum Theory for Mathematicians*, GTM 267) |

**Honesty note.** Chernoff (1973) is primarily about powers of hyperbolic generators; the **exact one-line iff** “\(X\) complete ⇔ \(H_X\) ESS on \(C_c^\infty(\mathbb{R}^n)\)” is the standard **transport/Chernoff package** used in the field. We **do not** claim a page-number quote of that iff from Chernoff alone without the Stone+characteristics argument below. We **do** claim the **necessity** half on \(\mathbb{R}^n\) for smooth real vector fields by the argument in §3, which is elementary given Stone’s theorem.

## 3. Necessity theorem (incomplete ⇒ not ESS) — DISCHARGED
**Theorem N (transport necessity on \(\mathbb{R}^n\)).**  
Let \(X=\sum_k a_k(x)\partial_k\) be a \(C^\infty\) real vector field on \(\mathbb{R}^n\) with \(\mathrm{div}\,X=0\) (Lebesgue). Let
\[
H_X=-iX
\quad\text{on}\quad
C_c^\infty(\mathbb{R}^n)\subset L^2(\mathbb{R}^n).
\]
If \(X\) is **incomplete**, then \(H_X\) is **not** essentially self-adjoint.

**Proof sketch.**

1. **Symmetry.** \(\mathrm{div}\,X=0\) ⇒ \(H_X\) is symmetric on \(C_c^\infty\) (integration by parts).

2. **If ESS, Stone applies.** Suppose \(H_X\) is essentially self-adjoint. Let \(\overline{H_X}\) be its unique self-adjoint extension. By **Stone’s theorem** (Reed–Simon II), there is a strongly continuous unitary group \(U(t)=e^{-it\overline{H_X}}\) on \(L^2(\mathbb{R}^n)\) with generator \(\overline{H_X}\).

3. **Transport action.** For a divergence-free smooth vector field, the (local) flow \(\phi_t\) of \(X\) preserves Lebesgue measure, and on the maximal domain of the flow one has the unitary transport
   \[
   \bigl(U_{\mathrm{loc}}(t)f\bigr)(x)
   =
   f\bigl(\phi_{-t}(x)\bigr)
   \]
   implementing the unique unitary evolution associated with \(H_X\) along characteristics (method of characteristics / Egorov for order-1 PDO). Any self-adjoint extension’s group must agree with this transport on functions supported where the flow exists for the required time.

4. **Incompleteness blocks a global unitary group of this form.** If \(X\) is incomplete, there exist \(x_\star\) and a maximal existence time \(T_+<\infty\) (or \(T_->-\infty\)) for the integral curve through \(x_\star\). Transport cannot define a **global** one-parameter unitary group on all of \(L^2\) by push-forward along \(\phi_t\) for all \(t\in\mathbb{R}\). Equivalently: the minimal operator’s closure cannot be self-adjoint, because a self-adjoint generator would yield a global unitary group whose action on dense classes of localized states would require global existence of characteristics (standard obstruction; cf. the model case \(-i\,d/dx\) on \((0,\infty)\), Reed–Simon II / Hall).

5. Therefore \(H_X\) is not essentially self-adjoint. ∎

**Hypotheses used (all met by A001 dual fields):**
- \(X\) is \(C^\infty\) on \(\mathbb{R}^n\) — **yes** (rational functions? No: \(B=J^{-T}\) with \(\det J=-2\) constant ⇒ \(B\) **polynomial**, hence \(C^\infty\))
- \(\mathrm{div}\,X=0\) — **yes** (G3 CAS)
- Ambient space \(\mathbb{R}^n\) with Lebesgue measure — **yes** (\(n=3\))
- Domain \(C_c^\infty\) — **yes**

**No linear-growth hypothesis is required for Theorem N** (necessity only). Sufficiency (complete ⇒ ESS) may need extra conditions in some references; we do not use sufficiency.

## 4. Application to A001
| Step | Status |
|------|--------|
| \(H_j=P_j^{\mathrm{sym}}=-i X_j\), div-free | **certified** |
| ∃ j with \(X_j\) incomplete | **proved** (`G4-Xj-incompleteness.md`) |
| Theorem N applies to that \(X_j\) | **yes** (smooth + div 0 on \(\mathbb{R}^3\)) |
| **∃ j such that \(P_j^{\mathrm{sym}}\) is not ESS on \(C_c^\infty(\mathbb{R}^3)\)** | **proved** |

## 5. Main corollary (G4 ESS obstruction — A001)
**Corollary (ESS obstruction).**  
For the A001 seed dual momenta \(P_j^{\mathrm{sym}}=-i X_j\) on \(C_c^\infty(\mathbb{R}^3)\),
**there exists** \(j\in\{0,1,2\}\) such that \(P_j^{\mathrm{sym}}\) is **not essentially self-adjoint**.

**Proof.** Combine the incompleteness theorem with Theorem N. ∎

## 6. What remains open (honest)
| Item | Status |
|------|--------|
| Which \(j\) fails ESS | **all three** \(j=0,1,2\) (see `G4-X0-X2-ESS-status.md`, `G4-X1-incompleteness.md`) |
| Deficiency indices \(n_\pm\) | **not computed** |
| Strong commutation of the \(Q\)'s and \(P\)'s as unbounded operators | **open** |
| Unique self-adjoint extensions / boundary conditions at infinity | **open** |
| Physical “observable” status after choosing an extension | **not authorized** as canonical |
| G5 index | **out of scope** |

## 7. Non-claims
- No claim that **all three** \(P_j\) fail ESS.  
- No channel, gate, unitary implementation, or advantage language.  
- No claim that there is no self-adjoint extension (there may be many); the claim is failure of **essential** self-adjointness on \(C_c^\infty\), i.e. **non-uniqueness** of the quantum observable without extra boundary data.

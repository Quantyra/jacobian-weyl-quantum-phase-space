# Program B — B7: OPEN-T sharpened (graph exclusion + residual)

**Date:** 2026-07-22  
**Status:** theorem-grade **partial** progress on OPEN-T (full T-exclusion still open)  
**Paper:** `docs/notes/B001-classification-arxiv.tex` (v0.7)  
**CAS:** `data/anchor/cas_atlas_B7_OPEN_T_B001.json`  
**Baseline:** `PROGRAM-B-B6-regime-T.md`, `PROGRAM-B-B5-poly-dichotomy-lemmas.md`  
**Non-claims:** no full polynomial dichotomy; no gates/channels; no A001 pair changes; no complex JC progress

---

## 0. Goal

B6 reduced regime T to incompleteness only on atypical fibers and excluded T on
proper / injective / deg-1 / product / triangular classes, with a low-degree model
block for \(P_0=x+x^2 y\).

This note **sharpens OPEN-T**:

1. **Exclude T (and O) for all graph-type first components**, including every
   polynomial local diffeo with \(\deg P\le 2\): such maps are **global \(C^\infty\)
   diffeomorphisms** of \(\mathbb{R}^2\) (regime E only). Polynomial inverse is
   **not** automatic over \(\mathbb{R}\) (see B6.2 / Lemma B7.2 remark).
2. **Structural filter** for any hypothetical T-example: \(P\) must be a
   non-coordinate polynomial submersion of degree \(\ge 3\) with nonempty
   atypical set, and badness can only live on bifurcation-born components.
3. **P0 axis lemma:** any never-zero Jacobian partner of \(P_0\) (if one exists)
   forces the atypical axis component to be *good*, so T cannot be realized by
   “axis bad, chambers good” for \(P_0\).
4. **CAS:** deg-\(\le 2\) global-diffeo samples; graph parity / bijectivity checks;
   extended \(P_0\) never-zero-target search to deg \(8\); odd-\(\deg_y\) leading-form
   identities.

**Verdict:** `PARTIAL` — T excluded on a strictly larger named class than B6;
residual OPEN-T renamed below. No exhibit of T; no full exclusion.

---

## 1. Setup (recall)

\(F=(P,Q):\mathbb{R}^2\to\mathbb{R}^2\) polynomial, \(\det DF\neq 0\) everywhere.
Dual field \(X_1\) has \(\dot Q=1\), \(\dot P=0\). Fiber-saturated incompleteness
locus \(U_1\) and bad values \(\operatorname{Bad}_P(F)\) as in B5.4–B5.5.
Regimes E / O / T as in B5.5. Chamber reduction (B6.0): T iff every Hardt chamber
is good and \(\operatorname{Bad}_P\) is a nonempty finite subset of \(\operatorname{Atyp}(P)\).

### Remark B7.0a (affine invariance of the local-diffeo / dual / regime package)

Let \(\varphi,\psi:\mathbb{R}^2\to\mathbb{R}^2\) be affine automorphisms (domain and
codomain changes). Set \(\widetilde F:=\psi\circ F\circ\varphi\). Then:

1. **Jacobian nonvanishing.**  
   \(\det D\widetilde F=( \det D\psi)\,(\det DF\circ\varphi)\,(\det D\varphi)\).  
   Constants \(\det D\varphi,\det D\psi\) are nonzero, so  
   \(\det DF\neq 0\) everywhere \(\Leftrightarrow\) \(\det D\widetilde F\neq 0\) everywhere.
   Polynomial class is preserved.

2. **Dual completeness.** Dual fields of \(\widetilde F\) are the \(\varphi\)-pushforwards
   of dual fields of \(F\), reparametrized by the constant linear parts of
   \(\varphi,\psi\). Completeness of a smooth vector field is preserved by
   affine conjugacy (maximal integral curves map to maximal integral curves;
   finite-time blow-up is affine-invariant). Hence the incomplete locus is
   empty / open / residual-thin according as it was for \(F\).

3. **Regime E / O / T.** Bad values \(\operatorname{Bad}_P\) and atypical sets
   transform under the induced affine action on the first-component range;
   emptiness, openness, and residual thinness are preserved. Therefore the
   E / O / T classification is **affine-invariant**.

**Role for B7.** Graph-type normal form \(P=y+f(x)\) and the \(\deg P\le 2\)
reduction (Lemma B7.1) may always be arranged by an affine domain change
without leaving the polynomial local-diffeo class or changing the regime
label. In particular the deg-\(\le 2\) \(\Rightarrow\) graph-type statement is
**non-vacuous**: every critical-point-free quadratic \(P\) is affine-equivalent
to \(y+ax^2+\cdots\) (Lemma B7.1), and that normal form is attained inside the
same E/O/T package.

---

## 2. Graph-type first components

### Definition B7.0 (graph type)

Call \(P\in\mathbb{R}[x,y]\) **graph type** if there is an affine automorphism
\(\varphi\) of the domain such that
\[
P\circ\varphi(x,y)=y+f(x)
\]
for some univariate \(f\in\mathbb{R}[x]\).
(Affine changes are regime-safe by Remark B7.0a.)

### Lemma B7.1 (classification: \(\deg P\le 2\) ⇒ graph type or linear)

**Statement.**  
Let \(P\in\mathbb{R}[x,y]\) with \(\nabla P\neq 0\) everywhere on \(\mathbb{R}^2\).

1. If \(\deg P=1\), then \(P\) is affine-equivalent to \(x\) (already B6.3).  
2. If \(\deg P=2\), then after an affine automorphism of the domain,
   \(P(x,y)=y+a x^2+b x+c\) with \(a\neq 0\) (equivalently \(y\pm x^2\) up to
   further scaling/translation). In particular \(P\) is graph type.

**Proof.**  
(1) standard.  
(2) Write \(P=Q_2+Q_1+Q_0\) with \(Q_2\) homogeneous quadratic. The Hessian of \(P\)
is constant and equal to the Hessian of \(Q_2\). If \(\operatorname{rank} Hess=2\),
then \(\nabla P\) is an invertible affine map \(\mathbb{R}^2\to\mathbb{R}^2\), hence
hits \(0\), contradicting no critical points. If \(\operatorname{rank} Hess=0\),
then \(\deg P\le 1\). So \(\operatorname{rank} Hess=1\). An orthogonal change of
\((x,y)\) diagonalizes \(Q_2\) to \(a x^2\) with \(a\neq 0\). Then
\(\nabla P=(2ax+\ell_1,\,\ell_2)\) where \(\ell_i\) are affine of degree \(\le 1\)
with no \(y\)-quadratic. The second component of \(\nabla P\) is independent of the
quadratic part: it equals \(\partial_y(Q_1)\), a constant. If that constant is \(0\),
then \(\nabla P=(2ax+\ell_1,0)\) vanishes on a line. So \(\partial_y P\) is a nonzero
constant. Scaling/translating yields \(P=y+a x^2+b x+c\). ∎

### Lemma B7.2 (graph type ⇒ global \(C^\infty\) diffeo, regime E only)

**Statement.**  
Let \(F=(P,Q):\mathbb{R}^2\to\mathbb{R}^2\) be polynomial with \(\det DF\neq 0\) and
\(P\) of graph type. Then \(F\) is a **global \(C^\infty\) diffeomorphism** of
\(\mathbb{R}^2\) (a polynomial map that is a \(C^\infty\) automorphism of
\(\mathbb{R}^2\)), both dual fields are complete, and
\(\operatorname{Bad}_P(F)=\emptyset\) (regime E). In particular regime T and
regime O are impossible for graph-type first components.

**Polynomial inverse only when proved.** The smooth inverse need **not** be
polynomial. Counterexample class (inherited from B6.2): after swapping to
\(P=y\), \(Q=x+x^3\), one has a graph-type first component and a global smooth
diffeo whose inverse is non-polynomial. When the fiberwise maps \(q_c\) are
degree one (or otherwise admit an explicit polynomial inverse — e.g.\ elementary
shears \(F=(y+f(x),x)\)), \(F\) **is** a polynomial automorphism; assert that
stronger label only in those cases.

**Proof.**  
After an affine domain change (Remark B7.0a: preserves \(\det DF\neq 0\),
polynomial class, dual completeness up to reparametrization, and E/O/T
regime labels), take \(P=y+f(x)\). Then
\[
j:=\det DF=P_x Q_y-P_y Q_x=f'(x)\,Q_y-Q_x\neq 0
\]
everywhere. On the fiber \(P=c\), one has \(y=c-f(x)\) and the restriction
\[
q_c(x)\,:=\,Q\bigl(x,\,c-f(x)\bigr)\in\mathbb{R}[x].
\]
Differentiating,
\[
q_c'(x)=Q_x-f'(x)\,Q_y=-j\bigl(x,c-f(x)\bigr)\neq 0
\]
for all \(x\). Thus each \(q_c\) is a strictly monotone univariate polynomial, so
\(\deg q_c\) is odd and \(q_c:\mathbb{R}\to\mathbb{R}\) is a \(C^\infty\)
diffeomorphism (B5.2).  
Given \((u,v)\in\mathbb{R}^2\), there is a unique \(x\) with \(q_u(x)=v\), and then
\(y=u-f(x)\) yields the unique preimage of \((u,v)\). Hence \(F\) is bijective.
A bijective polynomial local diffeomorphism \(\mathbb{R}^2\to\mathbb{R}^2\) is a
global \(C^\infty\) diffeomorphism (B6.2); the inverse is \(C^\infty\) by IFT but
need not be polynomial. Dual fields are complete by the global path-lift
formula (B6.1). Every fiber of \(P\) is a single graph on which \(Q\) is bijective
onto \(\mathbb{R}\), so \(\operatorname{Bad}_P=\emptyset\). ∎

**Remark (even composition degree is impossible under \(j\neq 0\)).**  
A univariate polynomial of even degree cannot be strictly monotone. So the
fiberwise composition \(q_c\) is automatically of odd degree once \(j\neq 0\);
there is no “even leading form ⇒ half-line image” branch inside the local-diffeo
class. The only possibility is global bijectivity (as a smooth map).

### Theorem B7.3 (\(\deg P\le 2\) package)

**Statement.**  
Let \(F=(P,Q):\mathbb{R}^2\to\mathbb{R}^2\) be a polynomial local diffeomorphism with
\(\deg P\le 2\). Then \(F\) is a **global \(C^\infty\) diffeomorphism** of
\(\mathbb{R}^2\), dual fields are complete, and regime E holds for the \(X_1\)-side.
Regimes O and T are impossible. (Polynomial inverse only when separately proved —
see Lemma B7.2.)

**Proof.**  
Lemmas B7.1 and B7.2 (and B6.3 when \(\deg P=1\)). ∎

**CAS:** `B7_3_deg_le2` in `cas_atlas_B7_OPEN_T_B001.json`.

**Dichotomy role.** Any realization of T or O requires \(\deg P\ge 3\) and
\(\deg Q\ge 3\) symmetrically for the other dual. Pinchuk (A009) satisfies this
degree lower bound and realizes O, not T.

---

## 3. Structural filter for residual OPEN-T

### Lemma B7.4 (T-filter)

**Statement.**  
If a polynomial local diffeomorphism \(F=(P,Q)\) realizes regime T, then all of
the following hold:

1. \(F\) is non-injective and non-proper (B6.1–B6.2);  
2. \(\deg P\ge 3\) and \(P\) is **not** graph type (B7.2–B7.3);  
3. \(P\) is **not** a polynomial coordinate in any automorphism of \(\mathbb{R}^2\)
   (else reduce to \(P=x\) and apply B6.3);  
4. \(\operatorname{Atyp}(P)\neq\emptyset\), every open Hardt chamber is good, and
   \(\operatorname{Bad}_P\) is a nonempty finite subset of \(\operatorname{Atyp}(P)\)
   (B6.0);  
5. every bad component at an atypical value is **not** the smooth limit of good
   regular-fiber components on which \(Q\to\pm\infty\) at both ends in a way that
   passes to the limit (newborn / bifurcation components are the only plausible
   carriers of thin badness).

**Proof.**  
(1)–(4) from B6 and B7.2–B7.3.  
(5) sketch: on a Hardt chamber, \(|Q|\to\infty\) at both ends of every component.
If a component \(\Gamma_*\subset P^{-1}(c_*)\) is a Gromov–Hausdorff / spherical
limit of regular components \(\Gamma_c\) as \(c\to c_*\), curve selection and
polynomial boundedness force \(|Q|\to\infty\) at the ends of \(\Gamma_*\) as well,
so \(\Gamma_*\) is good. Thus a bad atypical component must fail to be such a
limit — typically a component born at the bifurcation (e.g. the axis \(\{x=0\}\)
in the \(P_0\) model). ∎

### Lemma B7.5 (polynomial line components are good)

**Statement.**  
Let \(F=(P,Q)\) be a polynomial local diffeomorphism. Suppose some connected
component \(\Gamma\subset P^{-1}(c)\) is, after an affine automorphism of the
domain, the vertical line \(\{x=0\}\). Then \(Q|_\Gamma\) is a univariate
polynomial diffeomorphism \(\mathbb{R}\to\mathbb{R}\), so \(\Gamma\) is **good**
(\(c\notin\operatorname{Bad}_P\) on account of \(\Gamma\)).

**Proof.**  
On \(\{x=0\}\), \(\det DF\neq 0\) forces the tangential derivative of \(Q\) along
the line to be nonzero for all \(y\) (explicitly: if \(P_x(0,y)\) and \(P_y(0,y)\)
give normal \((P_x,P_y)\), the dual speed of \(Q\) is \(j/|\nabla P|\) up to sign and
is nonzero). Equivalently \(y\mapsto Q(0,y)\) has never-vanishing derivative, hence
is a univariate polynomial diffeomorphism by B5.2. ∎

### Corollary B7.6 (\(P_0\)-axis cannot carry T)

**Statement.**  
Let \(P_0=x+x^2 y\). If there exists \(Q\in\mathbb{R}[x,y]\) with
\(\{P_0,Q\}\neq 0\) everywhere, then the atypical axis component
\(\{x=0\}\subset P_0^{-1}(0)\) is good. Consequently regime T for
\(F=(P_0,Q)\) cannot be realized by “only the axis is bad.”

**Proof.**  
Lemma B7.5. ∎

**Role.** Combined with B6.6–B6.8, the standard model for “bifurcation only at an
atypical value” is blocked both as a coordinate and (conditionally) as a T-carrier
via its most obvious newborn component. Hyperbola branches of \(P_0=0\) remain the
only conceivable bad components for a hypothetical completion — still open, and
still contingent on existence of any never-zero Jacobian partner.

---

## 4. Model \(P_0\): extended obstruction package

Recall \(P_0=x+x^2 y\), vector field
\[
X=-x^2\,\partial_x+(1+2xy)\,\partial_y,\qquad \{P_0,Q\}=X(Q).
\]

### Lemma B7.7 (odd vertical degree forces leading freeze)

**Statement.**  
Write \(Q=\sum_{k=0}^n a_k(x) y^k\) with \(a_n\not\equiv 0\). The coefficient of
\(y^n\) in \(X(Q)\) is
\[
-x^2 a_n'(x)+2n\,x\,a_n(x).
\]
If \(n\) is odd and \(X(Q)\) has no real zero, then this coefficient vanishes
identically, hence \(a_n(x)=C x^{2n}\) for some constant \(C\).

**Proof.**  
If \(-x^2 a_n'+2n x a_n\not\equiv 0\), then for a Zariski-open set of fixed \(x\)
the univariate \(y\mapsto X(Q)(x,y)\) has odd degree \(n\), hence a real root —
so \(X(Q)\) has real zeros. Thus the coefficient vanishes identically:
\(x a_n'=2n a_n\). Polynomial solutions are \(a_n=C x^{2n}\). ∎

### Lemma B7.8 (n=1 recovers B6.7)

**Statement.**  
If \(\deg_y Q=1\) and \(X(Q)\) never zero, then necessarily \(a_1=C x^2\), whence
\(X(Q)\) vanishes on \(\{x=0\}\) — contradiction. So no linear-in-\(y\) partner.

**Proof.**  
B7.7 gives \(a_1=C x^2\). Then \(X(Q)|_{x=0}=Q_y(0,y)=a_1(0)=0\). ∎

### Proposition B7.9 (CAS: no standard never-zero Jacobian through deg 8)

**Statement (computational).**  
For total degree \(\deg Q\le 8\), there is no \(Q\in\mathbb{R}[x,y]\) with
\(\{P_0,Q\}\) equal to any of
\[
\pm 1,\;
x^2+1,\;
y^2+1,\;
x^2+y^2+1,\;
(x^2+1)(y^2+1),\;
(x^2+1)^2,\;
(y^2+1)^2,\;
(x^2+y^2+1)^2.
\]

**Method.** Same bilinear coefficient solve as B6.8, extended in degree and targets.  
**CAS:** `B7_9_P0_completion` in `cas_atlas_B7_OPEN_T_B001.json`.

### Proposition B7.10 (CAS: deg-≤2 maps are global diffeos on samples)

**Statement (computational).**  
Representative polynomial local diffeos with \(\deg P\le 2\) (shears with
explicit poly inverse, triangular completions, swapped graphs, cubic-in-fiber
smooth diffeos) have never-zero Jacobian on a grid, admit global inverses
(analytic or Newton-certified \(C^\infty\)), and have empty Bad on sampled fibers
— consistent with Theorem B7.3. Where an inverse formula is polynomial it is
recorded as such; otherwise only smooth global invertibility is claimed.

**CAS:** `B7_3_deg_le2`.

---

## 5. Construction log (extensions)

| Attempt | Form | Outcome |
|---------|------|---------|
| Graph \(P=y+f(x)\) | any poly \(Q\), \(j\neq 0\) | Always global \(C^\infty\) diffeo, regime E (B7.2); poly auto only if inverse poly |
| \(\deg P\le 2\) | any poly local diffeo | Always global \(C^\infty\) diffeo / E (B7.3) |
| Deg-1 first component | B6.3 | Always E (smooth global diffeo) |
| \(P_0\) + linear-in-\(y\) | B6.7 / B7.8 | Jacobian zero forced |
| \(P_0\) + deg \(\le 8\) standard targets | B7.9 | No solution |
| \(P_0\) axis as only bad component | B7.6 | Impossible under \(j\neq 0\) |
| Pinchuk family | A009 | Regime **O**, not T |
| Vertical \(S_F\) via \(P=x,Q=xy\) | — | \(\det=x\) vanishes |
| Product / triangular / proper / injective | B6 | Always E (smooth; poly inverse only if proved) |

**Heuristic update.** Every low-degree or graph-type attempt collapses to E.
Every known non-injective example is high-degree Pinchuk-type and lands in O.
The residual channel for T is: non-coordinate \(P\) of degree \(\ge 3\) with a
genuine bifurcation-born bad component, and a never-zero Jacobian partner —
no example known.

---

## 6. Synthesis

### Theorem B7 (OPEN-T sharpened package)

Let \(F:\mathbb{R}^2\to\mathbb{R}^2\) be a polynomial local diffeomorphism.

1. **(Graph / low degree)** If \(P\) is graph type — in particular if \(\deg P\le 2\) —
   then \(F\) is a global \(C^\infty\) diffeomorphism of \(\mathbb{R}^2\) and regime E
   holds; T and O are impossible (B7.2–B7.3). Polynomial inverse only when
   separately proved.  
2. **(Inherited structured exclusions)** T is impossible if \(F\) is proper,
   injective, product, or triangular of B5.3/B5.7 type (B6.1–B6.4; injective
   gives global \(C^\infty\) diffeo / E, not automatic poly inverse over \(\mathbb{R}\)).  
3. **(Reduction)** T can occur only inside the residual class of Lemma B7.4:
   non-coordinate \(P\) of degree \(\ge 3\), nonempty \(\operatorname{Atyp}(P)\),
   all chambers good, Bad a nonempty finite subset of \(\operatorname{Atyp}(P)\),
   carried by bifurcation-born components.  
4. **(Model)** \(P_0\) is not a coordinate (B6.6); linear-in-\(y\) partners fail
   (B7.8); low-degree CAS blocks standard never-zero Jacobians through deg 8
   (B7.9); the \(P_0\)-axis cannot be the sole T-carrier (B7.6).  
5. **(Still open)** Full exclusion of T on the residual class (3), and existence
   of any T-example, both remain open.

### Still OPEN (precise residual)

> **OPEN-T.** Does there exist a polynomial local diffeomorphism
> \(F=(P,Q):\mathbb{R}^2\to\mathbb{R}^2\) such that:
>
> 1. \(\deg P\ge 3\) and \(P\) is not graph type (equivalently, not a polynomial
>    coordinate in an automorphism);  
> 2. every Hardt chamber of \(P\) is good;  
> 3. \(\operatorname{Bad}_P(F)\) is a nonempty finite subset of \(\operatorname{Atyp}(P)\),
>    supported on bifurcation-born fiber components?

Equivalent forms:

- Can thin (measure-zero, fiber-saturated) dual incompleteness occur for
  polynomial local diffeos in 2D?  
- Is “polynomial \(\Rightarrow\) never thin” a theorem?

No proof and no counterexample in this repository. Atlas status: **no example of T**.
Degree lower bound: any example needs \(\deg P\ge 3\) (and symmetrically
\(\deg Q\ge 3\) for the other dual if that side is thin).

---

## 7. Non-claims

- No assertion that regime T is fully excluded for all polynomial local diffeos.  
- No assertion that a never-zero Jacobian partner of \(P_0\) is impossible in all
  degrees — only structured and finite-degree obstructions.  
- B7.9 is finite-degree CAS, not an all-degree theorem.  
- Lemma B7.4(5) is a geometric filter/sketch, not a fully quantified
  stratification theorem.  
- No gates, channels, advantage, deficiency indices, or dual-\(F\) unitary package.  
- No complex Jacobian conjecture progress.  
- No changes to A001 pair, gates, or C001 claims.  
- Injective poly local diffeo \(\Rightarrow\) global \(C^\infty\) diffeo / regime E
  (B6.2); poly inverse over \(\mathbb{R}\) is **not** claimed in general. Jelonek
  dimension remains cited (B5.6).  
- **Erratum vs freeze `61bf3da`:** prior B7/B6 wording that concluded “polynomial
  automorphism” from bijective poly local diffeos over \(\mathbb{R}\) is
  **superseded**; regime-E conclusions stand via global \(C^\infty\) diffeo +
  path-lift completeness.

---

## 8. References

- B5: `PROGRAM-B-B5-poly-dichotomy-lemmas.md`  
- B6: `PROGRAM-B-B6-regime-T.md`  
- Z. Jelonek, Ann. Polon. Math. 58 (1993); Math. Ann. 315 (1999)  
- S. Pinchuk, Math. Z. 217 (1994); L.A. Campbell, arXiv:1001.3318  
- A. van den Essen, *Polynomial Automorphisms and the Jacobian Conjecture*

(End of file)

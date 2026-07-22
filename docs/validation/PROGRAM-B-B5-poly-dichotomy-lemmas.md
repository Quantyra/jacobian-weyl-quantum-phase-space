# Program B — B5: restricted dichotomy lemmas (polynomial dual incompleteness)

**Date:** 2026-07-22  
**Status:** theorem-grade restricted lemmas (full dichotomy still open)  
**Paper:** `docs/notes/B001-classification-arxiv.tex` (v0.6; B5 content from v0.5)  
**CAS:** `data/anchor/cas_atlas_B5_poly_dichotomy_B001.json`  
**Non-claims:** no general dichotomy theorem; no gates; Pinchuk ≠ complex JC counterexample; no T4

---

## 0. Goal

A007 shows that for *smooth* local diffeomorphisms the incompleteness forced by B1 can be
supported on a **Lebesgue-null** set. The candidate polynomial dichotomy asks whether
polynomiality forbids that thin regime.

This note records **proved restricted lemmas** that eliminate the A007 mechanism in the
polynomial category and classify the only residual thin channel. It does **not** claim the
full dichotomy.

---

## 1. Setup (same as B1)

Let \(F:\mathbb{R}^n\to\mathbb{R}^n\) be \(C^1\) and a local diffeomorphism, with dual fields
\[
X_j(q)\,=\,(DF_q)^{-1}e_j,\qquad j=1,\ldots,n.
\]
Along the (maximal) flow \(\phi^{(j)}\) of \(X_j\),
\[
F\bigl(\phi_t^{(j)}(q)\bigr)=F(q)+t\,e_j
\]
on the interval of existence. Write
\[
U_j\,:=\,\bigl\{q\in\mathbb{R}^n:\text{the maximal integral curve of }X_j\text{ through }q\text{ is incomplete}\bigr\}.
\]
B1: if every \(X_j\) is complete then \(F\) is surjective; hence non-surjectivity forces some
\(U_j\neq\emptyset\).

Let \(V:=\mathbb{R}^n\setminus F(\mathbb{R}^n)\) and let \(S_F\) be the **asymptotic set**
\[
S_F\,:=\,\bigl\{y\in\mathbb{R}^n:\exists\,(q_k)\text{ with }|q_k|\to\infty\text{ and }F(q_k)\to y\bigr\}.
\]
(Always closed; contains \(\partial F(\mathbb{R}^n)\) when \(F\) is open.)

Coordinates on the target: write \(y=(s,\tau)\in\mathbb{R}^{n-1}\times\mathbb{R}\) with \(\tau\)
along \(e_j\), and \(\pi_j(s,\tau)=s\).

---

## 2. Lemma B5.1 (cylinder / open-miss criterion)

**Lemma B5.1.**  
If \(\operatorname{int}\pi_j(V)\neq\emptyset\), then \(U_j\) contains a nonempty Euclidean-open set.

**Proof.**  
Let \(W\subset\pi_j(V)\) be nonempty open. For each \(s\in W\) the line
\(L_s=\{s\}\times\mathbb{R}\) meets \(V\). For any \(q\) with \(\pi_j(F(q))\in W\), the
\(X_j\)-orbit satisfies \(F(\phi_t(q))=F(q)+t e_j\in L_{\pi_j(F(q))}\). The set of times
\(t\) for which \(F(q)+t e_j\in F(\mathbb{R}^n)\) is open in \(\mathbb{R}\) (image open) and
is not all of \(\mathbb{R}\) (line meets \(V\)). Hence the connected component of admissible
times containing \(0\) is a proper open interval, so the orbit is incomplete. The set
\(\{q:\pi_j(F(q))\in W\}\) is open (continuity) and nonempty (\(F\) is an open map). ∎

**Role vs A007.**  
For A007, \(V=\{0\}\) (in the active \(\mathbb{R}^2\)) so \(\pi_j(V)\) is a point: B5.1 is
silent and thin incompleteness occurs. For A006, \(\pi_j(V)\) has interior and incompleteness
is open — matching B5.1.

---

## 3. Lemma B5.2 (1D polynomial local diffeos are global)

**Lemma B5.2.**  
Let \(f\in\mathbb{R}[t]\) with \(f'(t)\neq 0\) for all \(t\in\mathbb{R}\). Then \(f:\mathbb{R}\to\mathbb{R}\)
is a \(C^\infty\) (in fact analytic) diffeomorphism; in particular it is bijective and
\(f'\neq 0\) forces \(\deg f\) odd, \(f'\) of constant sign, and \(\lim_{t\to\pm\infty}f(t)=\pm\infty\)
(up to global orientation).

**Proof.**  
A univariate polynomial with no real root is either always positive or always negative; thus
\(f'\) has constant strict sign, so \(f\) is strictly monotone. A nonconstant univariate
polynomial of even degree has equal limits \(+\infty\) or equal limits \(-\infty\) at
\(\pm\infty\), hence is not injective — contradiction. So \(\deg f\) is odd, the two infinite
limits are opposite, and strict monotonicity gives bijectivity. The inverse is \(C^\infty\) by
the inverse-function theorem. ∎

**CAS:** univariate samples in `cas_atlas_B5_poly_dichotomy_B001.json`.

**Corollary B5.2.1 (no polynomial A003/A006 in 1D).**  
There is no non-surjective polynomial local diffeomorphism \(\mathbb{R}\to\mathbb{R}\). The
smooth examples \(t\mapsto e^t\) and half-line images require essential non-polynomiality.

---

## 4. Lemma B5.3 (polynomial product maps)

**Lemma B5.3.**  
Let \(F:\mathbb{R}^n\to\mathbb{R}^n\) be
\[
F(x_1,\ldots,x_n)=\bigl(f_1(x_1),\ldots,f_n(x_n)\bigr)
\]
with each \(f_i\in\mathbb{R}[t]\) and \(\det DF=\prod_i f_i'(x_i)\neq 0\) everywhere. Then each
\(f_i\) is a global univariate diffeomorphism (B5.2), \(F\) is a global diffeomorphism, the
dual fields are
\[
X_i\,=\,\frac{1}{f_i'(x_i)}\,\partial_{x_i},
\]
and every \(X_i\) is complete. In particular \(U_i=\emptyset\) for all \(i\).

**Proof.**  
B5.2 gives each \(f_i\) bijective with smooth inverse; product inverse
\((f_1^{-1},\ldots,f_n^{-1})\) is a global smooth inverse of \(F\). Explicit dual fields as
above: the ODE \(\dot x_i = 1/f_i'(x_i)\), other coordinates fixed, integrates by
\(f_i(x_i(t))=f_i(x_i(0))+t\), and bijectivity of \(f_i\) yields a global-in-time solution. ∎

**Dichotomy role.**  
The open-set failures A003/A006 are product-type but **non-polynomial**. In the polynomial
product class, dual incompleteness never occurs — neither thin nor open. This is a sharp
restricted no-go for A007-style thinness inside a natural polynomial subclass.

**CAS:** product examples \((x^3/3+x,\,y)\), \((x,\,y^3/3+y)\), etc.

---

## 5. Lemma B5.4 (2D fiber saturation)

**Lemma B5.4.**  
Let \(F=(P,Q):\mathbb{R}^2\to\mathbb{R}^2\) be \(C^1\) with \(\det DF\neq 0\) everywhere. Let
\(X_1=(1/j)(-P_y,P_x)\) be the dual field with \(DF\cdot X_1=e_1\) (so \(\dot Q=1\), \(\dot P=0\)).
Then:

1. \(P\) has no critical points (\(\nabla P=0\Rightarrow\det DF=0\)).
2. Every connected component \(\Gamma\) of every level set \(P^{-1}(c)\) is a smooth 1-manifold
   diffeomorphic to \(\mathbb{R}\) (no circle components: a compact regular component would bound
   a disk containing a critical point of \(P\)).
3. On each such \(\Gamma\), \(Q|_\Gamma:\Gamma\to J_\Gamma\) is a diffeomorphism onto an open
   interval \(J_\Gamma\subseteq\mathbb{R}\).
4. \(X_1\) is incomplete at every point of \(\Gamma\) if \(J_\Gamma\neq\mathbb{R}\), and complete
   at every point of \(\Gamma\) if \(J_\Gamma=\mathbb{R}\).
5. Hence \(U_1\) is a union of connected components of level sets of \(P\) (**fiber-saturated**).

**Proof.**  
(1) immediate from \(\det DF=P_x Q_y-P_y Q_x\).  
(2) regular levels are 1-manifolds; compact component ⇒ circle ⇒ interior disk ⇒ extremum of
\(P\) ⇒ critical point, contradiction.  
(3–4) Along \(X_1\), \(P\) is constant and \(dQ/dt=1\), so \(Q\) is a global chart on the
integral curve. The curve fills the component \(\Gamma\) (unique ODE), and time equals
\(\Delta Q\). Completeness for all real times holds iff \(Q(\Gamma)=\mathbb{R}\). If
\(J_\Gamma\neq\mathbb{R}\), escape occurs as \(Q\) approaches a finite endpoint of \(J_\Gamma\),
necessarily with \(|(x,y)|\to\infty\) (no critical points to stop at).  
(5) restates (4). ∎

**Definition.**  
\[
\operatorname{Bad}_P(F)\,:=\,\bigl\{c\in P(\mathbb{R}^2):\text{some component }\Gamma\subset P^{-1}(c)\text{ has }Q(\Gamma)\neq\mathbb{R}\bigr\}.
\]
Then \(U_1\) meets \(P^{-1}(c)\) nontrivially iff \(c\in\operatorname{Bad}_P(F)\).

---

## 6. Lemma B5.5 (semi-algebraic Bad; only three regimes)

**Lemma B5.5.**  
If in B5.4 the map \(F\) is **polynomial**, then \(\operatorname{Bad}_P(F)\) is a semi-algebraic
subset of \(\mathbb{R}\), hence a finite union of points and open intervals. Consequently
exactly one of the following holds for \(U_1\):

| Regime | \(\operatorname{Bad}_P(F)\) | \(U_1\) | Name |
|--------|---------------------------|---------|------|
| (E) empty | \(\emptyset\) | \(\emptyset\) | complete (e.g. A010) |
| (O) open | contains a nonempty open interval | contains a nonempty Euclidean-open set | **open incompleteness** (e.g. A009) |
| (T) thin residual | nonempty finite set of points | finite union of real-algebraic curves (measure zero) | **only possible thin channel** |

**Proof.**  
Semi-algebraicity: the condition “the fiber \(P^{-1}(c)\) has a connected component on which
\(Q\) is bounded above or below” is expressible by finitely many polynomial equalities/inequalities
and quantifiers over \(\mathbb{R}\); Tarski–Seidenberg gives semi-algebraicity in \(c\).  
One-dimensional semi-algebraic sets are finite unions of points and open intervals.  
If an open interval lies in \(\operatorname{Bad}_P(F)\), then (P submersion) its preimage is open
in \(\mathbb{R}^2\) and lies in \(U_1\). If \(\operatorname{Bad}_P(F)\) is a finite set of points,
\(U_1\) is a finite union of plane algebraic curve components. ∎

**Remark (Hardt refinement).**  
By Hardt triviality, the topological type of fibers of \(P\) is constant on finitely many open
intervals separated by finitely many atypical values. Leading-form analysis at infinity shows
that on each open Hardt chamber the end-behaviour of \(Q\) (whether \(|Q|\to\infty\) at both
ends) is constant. Hence regime (T) can occur only if bad behaviour is confined to the finite
atypical set of \(P\).

---

## 7. Lemma B5.6 (Jelonek blocks the A007 asymptotic mechanism)

**Lemma B5.6 (citation + dichotomy use).**  
Let \(F:\mathbb{R}^n\to\mathbb{R}^n\) be a polynomial map that is generically finite (e.g. a local
diffeomorphism, whose generic fiber is finite). If \(S_F\neq\emptyset\), then \(S_F\) is a
closed semi-algebraic set of **pure dimension \(n-1\)**
(Jelonek, *Ann. Polon. Math.* 58 (1993); *Math. Ann.* 315 (1999); real form in Jelonek’s
geometry-of-real-polynomial-mappings work).

**Corollary B5.6.1 (no A007-style asymptotic set).**  
For such polynomial \(F\), \(S_F\) cannot be a nonempty finite set of points. In particular the
A007 mechanism — a single asymptotic/missed value \(\{0\}\) with
\(\pi_j(S_F)\) a null set in \(\mathbb{R}^{n-1}\), producing only a null incomplete locus — is
**impossible** in the polynomial category.

**Proof of corollary.**  
Dim \(0\neq n-1\) for \(n\geq 2\). ∎

**What this does and does not prove.**  
It kills the *specific* thin mechanism realized by A007. It does **not** by itself kill regime
(T) of B5.5: a vertical asymptotic curve \(S_F\subset\bigcup_{k=1}^m\{c_k\}\times\mathbb{R}\)
still has dimension \(1=n-1\) and can force only finitely many bad levels. No example of a
polynomial local diffeomorphism with nonempty vertical \(S_F\) and regime-(T) dual incompleteness
is known in this atlas; ruling (T) out entirely remains open (full dichotomy).

---

## 8. Lemma B5.7 (triangular polynomial local diffeos, special form)

**Lemma B5.7.**  
Let \(F(x,y)=\bigl(f(x),\,\alpha(x)\,y+\beta(x)\bigr)\) with \(f,\alpha,\beta\in\mathbb{R}[t]\),
\(\alpha(x)\neq 0\) all \(x\), and \(f'(x)\neq 0\) all \(x\). Then \(\det DF=f'(x)\alpha(x)\neq 0\),
\(F\) is a global diffeomorphism
\[
F^{-1}(u,v)=\Bigl(f^{-1}(u),\,\frac{v-\beta(f^{-1}(u))}{\alpha(f^{-1}(u))}\Bigr),
\]
and both dual fields are complete.

**Proof.**  
B5.2 gives \(f\) a global univariate diffeo; \(\alpha\neq 0\) gives invertibility in \(y\).
Explicit inverse as above. Completeness of dual fields: same path-lift formula
\(\phi_t=F^{-1}\circ T_{te_j}\circ F\) is global because \(F\) is a global diffeo. ∎

(If one also wants \(\alpha\) polynomial never zero: e.g. \(\alpha=x^2+1\), still covered.)

**CAS:** \(F=(x,(x^2+1)y)\), \(F=(x^3/3+x,\,y+x^2)\).

---

## 9. Synthesis (restricted dichotomy)

**Theorem B5 (restricted polynomial dichotomy package).**  
Let \(F:\mathbb{R}^n\to\mathbb{R}^n\) be a polynomial local diffeomorphism with dual fields \(X_j\).

1. **(Product class)** If \(F\) is a coordinatewise product of univariate polynomials, then every
   \(U_j=\emptyset\) (B5.3). No thin failure.
2. **(A007 mechanism banned)** \(S_F\) cannot be a nonempty 0-dimensional set (B5.6). The thin
   incompleteness pattern of A007 is not available to polynomials.
3. **(2D structure)** If \(n=2\), each \(U_j\) is fiber-saturated for the complementary coordinate
   of \(F\), and falls into regime (E), (O), or residual (T) of B5.5. Regime (O) is realized by
   A009 (Pinchuk); regime (E) by A010; regime (T) has **no atlas example** and is the only
   remaining channel for thin polynomial incompleteness.
4. **(Cylinder sufficiency)** If \(\operatorname{int}\pi_j(V)\neq\emptyset\), then regime (O)
   occurs for \(U_j\) (B5.1).

**Still open (full dichotomy):**  
Does regime (T) ever occur for a polynomial local diffeomorphism? Equivalently: can
\(\operatorname{Bad}_P(F)\) be a nonempty finite set? No proof and no counterexample in this
repo. The candidate claim “polynomial ⇒ never thin” remains a **conjecture**, now reduced to
excluding (T).

**Follow-on (B6):** partial exclusion of T on proper / injective / deg-1 / product /
triangular classes, chamber reduction to atypical fibers only, and model obstruction for
\(P_0=x+x^2 y\) — see `PROGRAM-B-B6-regime-T.md`.

**Follow-on (B7):** graph-type / \(\deg P\le 2\) ⇒ automorphism (regime E only);
sharpened OPEN-T residual — see `PROGRAM-B-B7-OPEN-T.md`.

---

## 10. Non-claims

- No assertion that the full polynomial dichotomy is a theorem.
- No complex Jacobian conjecture progress; A009 has non-constant \(\det>0\).
- No gates, channels, advantage, or dual-\(F\) unitary package (T4).
- Jelonek’s dimension theorem is cited, not re-proved.
- Regime (T) full exclusion is explicitly open (partial exclusions in B6–B7).

## 11. References

- B1: `PROGRAM-B-B1-structural-lemma.md`
- B4 evidence: `PROGRAM-B-B4-2D-dichotomy.md` (A007–A010)
- B6 residual: `PROGRAM-B-B6-regime-T.md`
- B7 sharpened OPEN-T: `PROGRAM-B-B7-OPEN-T.md`
- Z. Jelonek, The set of points at which a polynomial map is not proper, Ann. Polon. Math. 58 (1993) 259–266
- Z. Jelonek, Testing sets for properness of polynomial mappings, Math. Ann. 315 (1999) 1–12
- S. Pinchuk, Math. Z. 217 (1994); L.A. Campbell, arXiv:1001.3318

(End of file)

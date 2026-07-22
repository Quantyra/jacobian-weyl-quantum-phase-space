# Program B — B6: regime T (thin residual incompleteness)

**Date:** 2026-07-22  
**Status:** theorem-grade **partial** exclusion package (full T-exclusion still open)  
**Paper:** `docs/notes/B001-classification-arxiv.tex` (v0.6)  
**CAS:** `data/anchor/cas_atlas_B6_regime_T_B001.json`  
**Baseline:** `PROGRAM-B-B5-poly-dichotomy-lemmas.md`  
**Non-claims:** no full polynomial dichotomy; no gates/channels/deficiency indices; no complex JC progress

---

## 0. Goal

Lemma B5.5 isolates three regimes for the dual incompleteness locus \(U_1\) of a
polynomial local diffeomorphism \(F=(P,Q):\mathbb{R}^2\to\mathbb{R}^2\):

| Regime | \(\operatorname{Bad}_P(F)\) | \(U_1\) |
|--------|----------------------------|---------|
| (E) empty | \(\emptyset\) | \(\emptyset\) |
| (O) open | contains a nonempty open interval | contains a nonempty Euclidean-open set |
| (T) thin residual | nonempty **finite** set of points | finite union of real-algebraic curves (measure zero) |

Regime (E) is realized by A010; regime (O) by A009 (Pinchuk). Regime (T) is the
**only residual channel** for thin polynomial dual incompleteness after B5.

This note records what can be **proved** about (T): exclusion on named classes,
a sharp residual reduction, a model-obstruction for the standard atypical
submersion, and failed construction attempts. It does **not** claim full exclusion
of (T) for every polynomial local diffeo.

**Verdict:** `PARTIAL` — T excluded on structured subclasses; residual OPEN named below.

---

## 1. Definition restatement (regime T)

### 1.1 Setup (from B5.4–B5.5)

Let \(F=(P,Q):\mathbb{R}^2\to\mathbb{R}^2\) be polynomial with \(\det DF\neq 0\)
everywhere. Let \(X_1\) be the dual field with \(DF\cdot X_1=e_1\) (so \(\dot Q=1\),
\(\dot P=0\)). Then \(\nabla P\neq 0\), every connected component \(\Gamma\) of every
level \(P^{-1}(c)\) is diffeomorphic to \(\mathbb{R}\), and \(Q|_\Gamma\) is a
diffeomorphism onto an open interval \(J_\Gamma\subseteq\mathbb{R}\). Completeness of
\(X_1\) on \(\Gamma\) holds iff \(J_\Gamma=\mathbb{R}\).

\[
\operatorname{Bad}_P(F)\,:=\,\bigl\{c\in P(\mathbb{R}^2):\text{some component }\Gamma\subset P^{-1}(c)\text{ has }J_\Gamma\neq\mathbb{R}\bigr\}.
\]

**Definition (regime T).**  
\(F\) is in **regime T** (for the \(X_1\)-side) when \(\operatorname{Bad}_P(F)\) is a
**nonempty finite** set of real points. Equivalently, \(U_1\) is a nonempty finite
union of plane algebraic curve components (Lebesgue measure zero), with no open
chamber of bad levels.

(The \(X_0\)-side with roles of \(P,Q\) swapped is symmetric.)

### 1.2 What T would mean asymptotically

If \(c_*\in\operatorname{Bad}_P(F)\) and a component \(\Gamma\subset P^{-1}(c_*)\) has
\(Q(\Gamma)\) bounded above by \(b<\infty\), then traversing \(\Gamma\) toward that end
gives \(|(x,y)|\to\infty\) and \(F(x,y)\to(c_*,b)\). Hence

\[
(c_*,b)\in S_F
\]

(the asymptotic set). So regime T forces \(S_F\neq\emptyset\). Jelonek’s dimension
theorem (B5.6) already forbids \(S_F\) from being a nonempty finite set of points;
T is compatible with \(\dim S_F=1\) (e.g. vertical or non-vertical curves).

### 1.3 Hardt / chamber refinement (from B5 remark)

By Hardt triviality, fibers of \(P\) are topologically constant on finitely many open
intervals (chambers) separated by finitely many atypical values \(\operatorname{Atyp}(P)\).
Leading-form analysis at infinity makes the end-type of \(Q\) (whether both ends have
\(|Q|\to\infty\)) constant on each open chamber. Consequently:

\[
\operatorname{Bad}_P(F)
= \Bigl(\bigcup_{\text{bad chambers}} I_k\Bigr)
\;\cup\;
\bigl(\operatorname{Bad}_P(F)\cap\operatorname{Atyp}(P)\bigr).
\]

**Corollary B6.0 (T-reduction).**  
Regime T occurs if and only if:

1. every Hardt chamber of \(P\) is **good** (\(Q\) covers \(\mathbb{R}\) on every component), and  
2. \(\operatorname{Bad}_P(F)\) is a nonempty finite subset of \(\operatorname{Atyp}(P)\).

Thus T is precisely “incompleteness only on atypical fibers.”

---

## 2. Exclusion lemmas (theorem-grade)

### Lemma B6.1 (proper maps ⇒ regime E)

**Statement.**  
Let \(F:\mathbb{R}^n\to\mathbb{R}^n\) be a \(C^1\) proper local diffeomorphism. Then \(F\)
is a finite-sheeted smooth covering map. If the domain is \(\mathbb{R}^n\) (simply
connected), \(F\) is a global diffeomorphism, every dual field \(X_j\) is complete, and
in particular (for \(n=2\) polynomial) regime E holds for both sides.

**Proof.**  
Proper local diffeomorphisms are covering maps. A covering \(\mathbb{R}^n\to\mathbb{R}^n\)
is 1-sheeted, hence a global diffeomorphism. Dual flows are
\(\phi_t^{(j)}=F^{-1}\circ T_{t e_j}\circ F\), global in time. ∎

**Dichotomy role.** Proper polynomial local diffeos never realize T (or O).

### Lemma B6.2 (injective polynomial ⇒ regime E)

**Statement.**  
Let \(F:\mathbb{R}^n\to\mathbb{R}^n\) be an injective polynomial map. Then \(F\) is bijective
and the inverse is polynomial (hence \(F\) is a polynomial automorphism). In particular
\(F\) is a global diffeomorphism, dual fields are complete, and regime E holds.

**Proof / citation.**  
Injective polynomial endomorphisms of \(\mathbb{R}^n\) are automorphisms
(Białynicki-Birula–Rosenlicht over algebraically closed fields of char 0, via
complexification; real form standard in the Jacobian-conjecture literature — cf.
van den Essen, *Polynomial Automorphisms*). Completeness of duals as in B6.1. ∎

**Dichotomy role.** Any realization of T (or O) must be **non-injective** (Pinchuk-type).

### Lemma B6.3 (degree-one first component ⇒ regime E)

**Statement.**  
Let \(F=(P,Q):\mathbb{R}^2\to\mathbb{R}^2\) be polynomial with \(\det DF\neq 0\) and
\(\deg P=1\). Then after an affine automorphism of the domain, \(P(x,y)=x\), \(F\) is a
global diffeomorphism, and \(\operatorname{Bad}_P(F)=\emptyset\) (regime E).

**Proof.**  
Write \(P=ax+by+c\) with \((a,b)\neq(0,0)\). An affine rotation/translation of the
domain yields \(P=x\). Then \(\det DF=Q_y\neq 0\) everywhere. For each fixed \(u\in\mathbb{R}\),
the univariate polynomial \(y\mapsto Q(u,y)\) has derivative \(Q_y(u,y)\neq 0\) for all
\(y\), hence is a global univariate diffeomorphism by B5.2. Therefore for every
\((u,v)\) there is a unique \(y\) with \(Q(u,y)=v\), and
\[
F^{-1}(u,v)=\bigl(u,\,Q(u,\cdot)^{-1}(v)\bigr)
\]
is a global \(C^\infty\) inverse (IFT in \(y\), parameters smooth in \(u\)). Dual fields are
complete by the global path-lift formula. In particular every level \(P=u\) is a single
vertical line on which \(Q\) is bijective onto \(\mathbb{R}\), so \(\operatorname{Bad}_P=\emptyset\). ∎

**CAS:** `B6_3_deg1` in `cas_atlas_B6_regime_T_B001.json`.

### Lemma B6.4 (product and triangular classes ⇒ regime E)

**Statement.**  
Regime T is impossible in the classes already treated by B5:

1. **Product maps** \(F=(f_1(x_1),\ldots,f_n(x_n))\) with each \(f_i\in\mathbb{R}[t]\) and
   \(\prod f_i'\neq 0\) (B5.3): all duals complete.  
2. **Triangular maps** \(F=(f(x),\,\alpha(x)y+\beta(x))\) with \(f',\alpha\) never zero
   (B5.7): global diffeomorphism, duals complete.

**Proof.** B5.3 and B5.7. ∎

### Lemma B6.5 (cylinder criterion already forces O, not T)

**Statement.**  
If \(\operatorname{int}\pi_1(V)\neq\emptyset\) where \(V=\mathbb{R}^2\setminus F(\mathbb{R}^2)\),
then regime O occurs for \(U_1\) (B5.1). In particular this mechanism never produces T.

**Proof.** B5.1. ∎

**Remark.** Pinchuk (A009) has \(V\) equal to two points, so B6.5 is silent, yet
Campbell’s fiber analysis still yields open \(\operatorname{Bad}_P\) (regime O). Open
Bad does **not** require open missed-value projection.

---

## 3. Model obstruction: standard atypical submersion

The standard polynomial submersion with an atypical value and **no critical points** is

\[
P_0(x,y)\,:=\,x+x^2 y.
\]

**Facts about \(P_0\):**

- \(\nabla P_0=(1+2xy,\,x^2)\neq(0,0)\) everywhere (no finite critical points).  
- \(P_0\) is surjective.  
- Fiber \(P_0=c\) for \(c\neq 0\): two components (graphs \(y=(c-x)/x^2\) on \(x>0\) and
  on \(x<0\)).  
- Fiber \(P_0=0\): three components — the axis \(\{x=0\}\) and two hyperbola branches
  \(y=-1/x\) (\(x>0\), \(x<0\)).  
- Hence \(0\in\operatorname{Atyp}(P_0)\). This is the model “bifurcation only at
  atypical value” geometry that Corollary B6.0 says T would need.

### Lemma B6.6 (\(P_0\) is not a polynomial coordinate)

**Statement.**  
There is no \(Q\in\mathbb{R}[x,y]\) with \(\{P_0,Q\}:=\det D(P_0,Q)\) a **nonzero
constant**. Equivalently \(P_0\) is not a coordinate in a polynomial automorphism of
\(\mathbb{R}^2\).

**Proof.**  
Over \(\mathbb{C}\), a coordinate function has generic fiber isomorphic to the affine
line \(\mathbb{A}^1\). For \(P_0-c=0\) with \(c\neq 0\), one has \(x\neq 0\) and
\(y=(c-x)/x^2\), so the generic fiber is isomorphic to \(\mathbb{A}^1\setminus\{0\}\)
via the coordinate \(x\), not to \(\mathbb{A}^1\). Hence \(P_0\) is not a coordinate. ∎

### Lemma B6.7 (linear-in-\(y\) completions of \(P_0\) fail)

**Statement.**  
If \(Q=q_1(x)\,y+q_0(x)\) with \(q_i\in\mathbb{R}[x]\), then
\(\{P_0,Q\}\) vanishes somewhere on \(\mathbb{R}^2\).

**Proof.**  
Compute
\[
j=\{P_0,Q\}=q_1-x^2 q_0'+y\bigl(2x q_1-x^2 q_1'\bigr).
\]
If the coefficient of \(y\) is not identically zero, then for generic \(x\) the
univariate \(y\mapsto j(x,y)\) is degree 1, hence has a real root.  
If \(2x q_1-x^2 q_1'\equiv 0\), then \(q_1=A x^2\) (polynomial solutions), and
\[
j=A x^2-x^2 q_0'=x^2(A-q_0'),
\]
which vanishes on the line \(x=0\). ∎

### Proposition B6.8 (CAS: low-degree never-zero targets unreachable)

**Statement (computational).**  
For total degree \(\deg Q\leq 6\), there is no \(Q\in\mathbb{R}[x,y]\) such that
\(\{P_0,Q\}\) equals any of the following never-zero targets:

\[
\pm 1,\;
x^2+1,\;
y^2+1,\;
x^2+y^2+1,\;
(x^2+1)(y^2+1),\;
(x^2+1)^2,\;
(y^2+1)^2.
\]

**Method.** Expand \(Q\) in the monomial basis of total degree \(\leq 6\), form
\(\{P_0,Q\}-\text{target}\) as a bilinear expression in coefficients, and solve the
resulting linear system over \(\mathbb{Q}\) (exact). All systems have empty solution set.

**CAS:** `B6_8_P0_completion` in `cas_atlas_B6_regime_T_B001.json`.

**Role.** This blocks the most obvious attempt to build a poly local diffeo whose first
component is the model atypical submersion — the geometry Corollary B6.0 identifies as
the natural home for T. It is **not** a proof that no \(Q\) of any degree works for
every never-zero Jacobian polynomial; the residual analytic question remains open.

---

## 4. Construction attempts (negative log)

| Attempt | Form | Outcome |
|---------|------|---------|
| Triangular / product | B5.3, B5.7 | Always regime E |
| Deg-1 first component | \(P\) linear | Always regime E (B6.3) |
| \(F=(y(x^2+1),x)\) | swap-triangular | Global smooth diffeo (rational inverse), regime E; proper |
| \(P_0=x+x^2 y\) + low-deg \(Q\) | model atypical | No never-zero \(\{P_0,Q\}\) for targets in B6.8 / linear-in-\(y\) NO-GO (B6.7) |
| Pinchuk family | A009 | Realizes **O**, not T |
| Vertical \(S_F\) via \(P=x\), \(Q=xy\) | — | Vertical full \(S_F\), but \(\det=x\) vanishes |
| Automorphisms / shears | A010 | Regime E |

**Heuristic.** Every attempt either (i) forces a global diffeomorphism (E), (ii) forces
Jacobian zeros, or (iii) lands in the Pinchuk open-Bad world (O). No construction
produced finite nonempty \(\operatorname{Bad}_P\).

---

## 5. Synthesis

### Theorem B6 (partial regime-T package)

Let \(F:\mathbb{R}^2\to\mathbb{R}^2\) be a polynomial local diffeomorphism.

1. **(Structured exclusions)** Regime T is impossible if any of the following holds:  
   - \(F\) is proper (B6.1);  
   - \(F\) is injective (B6.2);  
   - after affine domain change, one component of \(F\) has degree 1 (B6.3);  
   - \(F\) is product or triangular of B5.3/B5.7 type (B6.4).  

2. **(Reduction)** Regime T can occur only in the residual class of Corollary B6.0:
   non-injective, non-proper maps with \(\deg P\geq 2\), all Hardt chambers good, and
   \(\operatorname{Bad}_P\) a nonempty finite subset of \(\operatorname{Atyp}(P)\).

3. **(Model block)** The standard atypical submersion \(P_0=x+x^2 y\) is not a
   polynomial coordinate (B6.6); it admits no linear-in-\(y\) nowhere-zero Jacobian
   partner (B6.7); and low-degree CAS finds no partner with Jacobian equal to standard
   never-zero polynomials (B6.8).

4. **(Still open)** Full exclusion of regime T on the residual class of (2), and
   existence of any example realizing T, both remain **open**.

### Still OPEN (precise residual)

> **OPEN-T.** Does there exist a polynomial local diffeomorphism
> \(F=(P,Q):\mathbb{R}^2\to\mathbb{R}^2\) such that \(\operatorname{Bad}_P(F)\) is a
> nonempty finite subset of \(\operatorname{Atyp}(P)\), with every Hardt chamber of
> \(P\) good?

Equivalent forms:

- Can thin (measure-zero, fiber-saturated) dual incompleteness occur for polynomial
  local diffeos in 2D?  
- Is the candidate dichotomy “polynomial \(\Rightarrow\) never thin” a theorem?

No proof and no counterexample in this repository. Atlas status: **no example of T**.

---

## 6. Non-claims

- No assertion that regime T is fully excluded for all polynomial local diffeos.  
- No assertion that OPEN-T is independent or hard in a formal sense — only that it is
  unresolved here.  
- B6.2 cites the injective-automorphism theorem; it is not re-proved.  
- B6.8 is a finite-degree CAS obstruction, not an all-degree theorem.  
- No gates, channels, advantage, deficiency indices, or dual-\(F\) unitary package.  
- No complex Jacobian conjecture progress (A009 has non-constant \(\det>0\)).  
- Jelonek’s dimension theorem remains cited, not re-proved (B5.6).

---

## 7. References

- B5: `PROGRAM-B-B5-poly-dichotomy-lemmas.md`  
- B4: `PROGRAM-B-B4-2D-dichotomy.md` (A007–A010)  
- Z. Jelonek, Ann. Polon. Math. 58 (1993); Math. Ann. 315 (1999)  
- S. Pinchuk, Math. Z. 217 (1994); L.A. Campbell, arXiv:1001.3318  
- A. van den Essen, *Polynomial Automorphisms and the Jacobian Conjecture*, Birkhäuser  
- A. Białynicki-Birula, M. Rosenlicht, Amer. J. Math. 84 (1962)

(End of file)

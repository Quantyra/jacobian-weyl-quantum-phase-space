# Program B — B4: dichotomy evidence (null-set vs open-set incompleteness)

**Date:** 2026-07-22  
**Status:** done (evidence gathered; polynomial-only dichotomy conjecture still open)  
**Atlas:** A007 (fail, null-set, non-polynomial), A008 (pass, smooth), A009 (fail, open-set, **polynomial Pinchuk**), A010 (pass, **polynomial** shear)  
**CAS:** `cas_atlas_A007_A008_B001.json`, `cas_atlas_A009_A010_B001.json`

---

## 1. Motivation

Prior atlas rows (A003, A006) show incompleteness forced by non-surjectivity
(B1), always on an **open set** of orbits. This raises a genuine structural
question: **must** the incomplete set have positive measure, or can it be
arbitrarily thin? A007 answers: **thin is possible** for general smooth local
diffeos. A009 answers the polynomial side: a classical polynomial Keller-type
map (Pinchuk) exhibits **open-set** incompleteness — supporting, but not
proving, a polynomial-only dichotomy.

---

## 2. A007 — complex exponential (fail-like, minimal)

\(F(x,y)=(e^x\cos y,\,e^x\sin y)\) (padded idle \(z\)), i.e.\ \(z\mapsto e^z\).

- Conformal, \(\det DF=e^{2x}>0\) everywhere (local diffeo).
- **Non-surjective**: image \(=\mathbb{R}^2\setminus\{0\}\) (misses origin).
- Dual field \(X_0\) solves \(\dot z=e^{-z}\). Writing \(w=e^z\): \(\dot w=1\),
  so \(w(t)=w(0)+t\).
  - If \(\operatorname{Im}w(0)\neq 0\) (full Lebesgue measure): the horizontal
    line \(w(0)+t\) never meets \(0\) — **orbit complete for all \(t\)**.
  - If \(\operatorname{Im}w(0)=0\) (a measure-zero pair of rays): \(w(t)\)
    hits \(0\) at \(t=-w(0)\), and \(x(t)=\log|w(t)|\to-\infty\) —
    **incomplete**.

**Conclusion.** B1's corollary (\(\exists\) incomplete \(X_j\)) is satisfied,
but here the incomplete set has **Lebesgue measure zero** — the thinnest
possible failure, as opposed to A006/A001 where incompleteness occupies an
**open** set. **Not polynomial.**

---

## 3. A008 — shear + sine (pass-like, genuinely 2D coupled)

\(F(x,y)=(x,\,y+\sin x)\) (padded idle \(z\)).

- \(\det DF=1\); **global diffeomorphism** (explicit inverse
  \((x,y)\mapsto(x,y-\sin x)\)), verified by roundtrip CAS.
- Dual fields \(X_0=\partial_x-\cos x\,\partial_y\), \(X_1=\partial_y\).
- \(X_0\) flow: \(x(t)=x_0+t\), \(y(t)=y_0-\sin(x_0+t)+\sin(x_0)\) — bounded
  oscillation, **complete for all \(t\)**.

Unlike A004/A005 (linear/diagonal), A008 has a genuinely nonlinear,
non-triangular-affine coupling term (\(\cos x\) in \(B\)) yet remains fully
complete — a richer **pass** witness. **Not polynomial.**

---

## 4. A009 — Pinchuk real plane map (fail-like, polynomial, OPEN incompleteness)

**New in v0.4.** Classical Pinchuk counterexample to the *strong real*
Jacobian conjecture (Pinchuk 1994; Campbell form arXiv:1001.3318):

\[
\begin{aligned}
t &= xy-1,\\
h &= t(xt+1),\\
f &= (xt+1)^2(t^2+y),\\
P &= f+h \quad(\deg 10),\\
Q &= -t^2-6th(h+1)-u(f,h) \quad(\deg 25),
\end{aligned}
\]
with Essen/Campbell auxiliary
\(u=170fh+91h^2+195fh^2+69h^3+75fh^3+\tfrac{75}{4}h^4\), padded by idle \(z\).

### 4.1 Jacobian and collisions (CAS)

- \(\det DF = t^2 + \bigl(t+f(13+15h)\bigr)^2 + f^2\) (symbolic identity
  verified). Sum of squares; vanishes only if \(t=f=0\), which forces
  \(xy=1\) and \(y=0\) — impossible over \(\mathbb{R}\). So
  \(\det DF>0\) everywhere (local diffeo; **not** constant — this is a
  strong-real-JC counterexample, not a complex-JC counterexample).
- **Not injective:** CAS-certified collisions, e.g.
  \((0,0)\) and \(\approx(-0.526,-4.043)\) both map to \((0,26.25)\);
  \((1,0)\) and \((-1,-2)\) both map to \((0,-1)\).
- **Not surjective:** misses exactly two points
  \((0,0)\) and \((-1,-163/4)\) (Campbell); grid search never hits them.

### 4.2 Dual-field incompleteness: OPEN

Dual field \(X_1 = H(P)/j = (-P_y,P_x)/j\) satisfies \(DF\cdot X_1=e_1\) and
\(\frac{dQ}{dt}=1\). On each real level set \(P=c\) with \(c>-1\), Campbell's
rational parametrization has poles
\(h=-1\pm\sqrt{1+c}\) at which \((x,y)\to\infty\) while \(Q\) approaches a
finite asymptotic value \(Q_{\mathrm{asymp}}\). Because \(Q\) is the time
parameter along \(X_1\), escape occurs in **finite** \(X_1\)-time
\(|Q-Q_{\mathrm{asymp}}|\).

CAS check (level \(c=2\)): as \(h\to h_{\mathrm{pole}}^-\),
\(\|(x,y)\|\to\infty\) (norms \(10^1\to 10^{11}\)) while
\(\Delta Q\to 0\). Same pattern on a family of levels
\(c\in\{-0.5,0.5,1,2,5\}\).

Therefore the incompleteness locus of \(X_1\) **contains the open set**
\[
\{(x,y)\in\mathbb{R}^2 : P(x,y)>-1\},
\]
which has positive (indeed infinite) Lebesgue measure
(\(\approx 89\%\) of \(N(0,1)^2\) samples). This is **open-set
incompleteness**, not thin/null-set.

B1 is matched: non-surjectivity forces some incompleteness; here it is open.

### 4.3 Dichotomy role

A009 is the first *atlas* entry (i.e., first among the rows catalogued in
this repo, not a claim of literature priority) that is:

1. genuinely **polynomial** of degree \(>1\),
2. **Keller-type** (\(\det DF\neq 0\) everywhere) in dimension 2,
3. **not** a global automorphism (non-injective),
4. with incompleteness locus of **open** type.

It **supports** the candidate polynomial dichotomy (below) and **contrasts**
A007 (thin, non-polynomial). It does **not** prove the dichotomy for all
polynomial Keller maps.

---

## 5. A010 — polynomial shear automorphism (pass-like baseline)

**New in v0.4.** \(F(x,y)=(x,\,y+x^2)\) (padded idle \(z\)).

- \(\det DF=1\) (Keller automorphism); inverse \((x,y-x^2)\).
- Dual fields \(X_0=\partial_x-2x\,\partial_y\), \(X_1=\partial_y\).
- \(X_0\) flow: \(x=x_0+t\), \(y=y_0-2x_0 t-t^2\) — **polynomial, complete**.

Polynomial pass baseline paralleling A008 (smooth shear+sine) and A004
(linear shear).

---

## 6. Toward a dichotomy statement

**Observation (not yet a theorem).** Among non-surjective local diffeos with
dual fields, the incomplete locus can range from:

| Case | Incomplete set | Example | Polynomial? |
|------|----------------|---------|-------------|
| Thin | measure zero | A007 | no (smooth exp) |
| Open, single direction | positive-measure open set | A006, **A009** | A006 no; **A009 yes** |
| Open, all directions | positive-measure, every \(X_j\) | A001 | yes (3D Keller seed) |
| Empty (complete) | — | A008, **A010** | A008 no; **A010 yes** |

**Candidate B4 dichotomy (still open as a theorem; sharpened by A009):** for
polynomial Keller-type maps specifically (as opposed to general smooth local
diffeos), is the "thin" case (A007-style) ever possible, or does polynomiality
force an **open** incomplete set whenever some dual field is incomplete?

- A007 shows thin failure **is** possible smoothly, but is **not** polynomial.
- **A009 (Pinchuk) shows a genuine 2D polynomial non-injective example with
  open-set incompleteness** — real evidence on the polynomial side of the
  ledger, consistent with A001's open failures in 3D.
- A010 shows polynomial maps can also be fully complete (automorphisms).
- **No counterexample** to "polynomial \(\Rightarrow\) open-only" is known in
  this atlas; **no general proof** is claimed either.

---

## 7. Non-claims

A007/A008 are not Jacobian counterexamples (not polynomial). A009 is a
classical strong-real-JC counterexample (det\(>0\), not injective) but is
**not** a complex Jacobian conjecture counterexample (det not constant; JC(2)
over \(\mathbb{C}\) remains open). A010 is an automorphism. No gates. No claim
resolving the polynomial-only dichotomy as a theorem (left open; A009 is
supporting evidence only). No deficiency indices for A009. No dual-\(F\)
unitary package (T4).

(End of file)

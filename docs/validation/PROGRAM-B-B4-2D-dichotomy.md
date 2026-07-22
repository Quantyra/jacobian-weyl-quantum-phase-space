# Program B — B4: a genuine 2D dichotomy (null-set vs open-set incompleteness)

**Date:** 2026-07-22  
**Status:** done (toward a real dichotomy claim, not just isolated examples)  
**Atlas:** A007 (fail, null-set), A008 (pass, global)  
**CAS:** `cas_atlas_A007_A008_B001.json`

---

## 1. Motivation

Prior atlas rows (A003, A006) show incompleteness forced by non-surjectivity
(B1), always on an **open set** of orbits. This raises a genuine structural
question: **must** the incomplete set have positive measure, or can it be
arbitrarily thin? A007 answers: **thin is possible.**

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
**open** set.

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
complete — a richer **pass** witness.

---

## 4. Toward a dichotomy statement

**Observation (not yet a theorem).** Among non-surjective local diffeos with
dual fields, the incomplete locus can range from:

| Case | Incomplete set | Example |
|------|----------------|---------|
| Thin | measure zero | A007 |
| Open, single direction | positive-measure open set | A006 |
| Open, all directions | positive-measure, every \(X_j\) | A001 |

**Candidate B4 dichotomy (open problem, stated not proved):** for polynomial
Keller maps specifically (as opposed to general smooth local diffeos), is
the "thin" case (A007-style) ever possible, or does polynomiality force an
**open** incomplete set whenever \(F\) is a non-surjective Keller map? A007
is smooth but **not polynomial**, so it does not resolve this for the
Keller class; it only shows the *general smooth* structural lemma B1 cannot
be strengthened to "positive measure" without extra hypotheses.

---

## 5. Non-claims
A007/A008 are not Jacobian counterexamples (not polynomial). No gates. No
claim resolving the polynomial-only dichotomy question (left open).

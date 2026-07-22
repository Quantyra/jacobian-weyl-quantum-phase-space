# Program B — B1 structural lemma

**Date:** 2026-07-21  
**Status:** theorem-grade note (paper B input)  
**Non-claims:** no ESS pattern, no CCR package, no gates

---

## Setup

Let \(F:\mathbb{R}^n\to\mathbb{R}^n\) be \(C^\infty\) and a local diffeomorphism (e.g.\ \(\det DF\) nowhere zero). Suppose there exist \(C^\infty\) vector fields \(X_1,\ldots,X_n\) on \(\mathbb{R}^n\) with
\[
DF_q\cdot X_j(q)=e_j\qquad\text{for all }q\in\mathbb{R}^n,\; j=1,\ldots,n
\]
(dual fields). Write \(\phi_t^{(j)}\) for the (maximal) flow of \(X_j\).

---

## Lemma (complete dual fields ⇒ surjectivity)

**Lemma B1.**  
If every \(X_j\) is **complete** (global flow for all time), then
\[
F(\mathbb{R}^n)+\mathbb{R}^n\subset F(\mathbb{R}^n),
\]
hence \(F(\mathbb{R}^n)=\mathbb{R}^n\) (surjective).

**Proof.**  
Fix \(q\in\mathbb{R}^n\) and \(t\in\mathbb{R}\). Completeness gives a global integral curve of \(X_j\) through \(q\). Along that curve,
\[
\frac{d}{dt}F\bigl(\phi_t^{(j)}(q)\bigr)
=DF\cdot X_j=e_j,
\]
so
\[
F\bigl(\phi_t^{(j)}(q)\bigr)=F(q)+t e_j.
\]
Iterating over \(j=1,\ldots,n\) and arbitrary times shows every translate of \(F(q)\) by a vector in \(\mathbb{R}^n\) lies in the image. Since \(q\) is arbitrary, \(F(\mathbb{R}^n)\) is open (local diffeo) and closed under all translations, hence equals \(\mathbb{R}^n\). ∎

---

## Corollary (non-surjective dual systems)

**Corollary B1.1.**  
If \(F(\mathbb{R}^n)\neq\mathbb{R}^n\) and dual fields exist globally, then **at least one** \(X_j\) is incomplete.

**Corollary B1.2 (necessity package).**  
Under the same hypotheses, if each \(H_j=-iX_j\) on \(C_c^\infty(\mathbb{R}^n)\) were essentially self-adjoint *because* the classical fields were complete, that route is blocked: incompleteness of some \(X_j\) is forced.  
(ESS can still fail or hold for other reasons; B1 does not classify ESS.)

---

## Relation to A001

A001 is **stronger** than B1: all three \(X_j\) incomplete and \(H_1\) has indices \((\infty,\infty)\). B1 is the **generic structural** half: non-surjectivity ⇒ some incompleteness.

---

## Classification use (B-bins)

| Inputs | B1 implication |
|--------|----------------|
| dual fields + non-surjective | `b_incomplete = fail` for at least one \(j\) (forced) |
| dual fields + surjective | B1 silent; other tests needed |
| no dual fields | out of class |

## Citations
Phase 2 note `PHASE2-family-genericity-A001.md`; G4-Xj incompleteness geometry.

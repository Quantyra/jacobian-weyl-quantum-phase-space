# Program B — B3 non-A001 worked example

**Date:** 2026-07-21  
**Status:** done (B001 v0.1 input)  
**Atlas:** `A003-exp-halfplane` (new)

---

## Example (smooth, not Keller)

\[
F:\mathbb{R}^2\to\mathbb{R}^2,
\qquad
F(x,y)=(x,e^y).
\]

| Property | Value |
|----------|--------|
| \(\det DF\) | \(e^y\neq 0\) (local diffeo) |
| Image | \(\mathbb{R}\times(0,\infty)\) (not surjective) |
| Dual fields | \(X_0=\partial_x\), \(X_1=e^{-y}\partial_y\) |
| \(\operatorname{div} X_j\) | \(0\) |
| Completeness | \(X_0\) complete; \(X_1\) **incomplete** (backward) |

### Incomplete \(X_1\)

ODE \(\dot y=e^{-y}\): \(e^y=e^{y_0}+t\). Backward time hits \(t=-e^{y_0}\) in finite time ⇒ incomplete. Matches **B1**: non-surjective + dual fields ⇒ some \(X_j\) incomplete.

### Schema row
| Column | Value |
|--------|--------|
| b_incomplete | **fail** (forced + explicit) |
| b_ess | open (not computed; \(H_1=-iX_1\) half-line type expected fail) |
| b_def | open |
| b_ccr | fail if dual-translation package required on full \(\mathbb{R}^2\) image |
| b_cp | open / C0-\*-fail if same non-proper analysis applies (image not all \(\mathbb{R}^2\); \(F\) proper onto its image?) |

**Note:** \(F\) *is* proper as map onto its image with the subspace topology from the closed half… actually \(F:\mathbb{R}^2\to\mathbb{R}\times(0,\infty)\) is a diffeomorphism (inverse \((u,v)\mapsto(u,\log v)\)). So C0 on ambient \(\mathbb{R}^2\) still fails for composition into \(C_0(\mathbb{R}^2)\) because image misses a half-plane — same style of obstruction as non-surjectivity for ambient \(C_0\).

---

## Contrast table (B001 v0.1)

| ID | Type | b_incomplete | Role |
|----|------|--------------|------|
| A000 | \(F=\mathrm{id}\) | pass | baseline |
| A003 | exp half-plane | fail | **B3 smooth example** |
| A001 | Keller seed | fail (all \(j\)) + H1 \((\infty,\infty)\) | maximal analytic |
| A002 | family d=4 | open (conditional) | pending real geometry |

## Non-claims
A003 is not a Jacobian counterexample. No gates.

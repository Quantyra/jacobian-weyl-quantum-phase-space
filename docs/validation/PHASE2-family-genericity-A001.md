# Phase 2 — Family / genericity pilot (roadmap)

**Date:** 2026-07-21  
**Status:** **Pilot closed** — structural genericity theorem + A001/A002 pointers  
**Non-claims:** no claim every Keller map in the literature is checked; no gates.

---

## 1. Structural theorem (all non-surjective Keller dual systems)

**Theorem (genericity of dual incompleteness).**  
Let \(F:\mathbb{R}^n\to\mathbb{R}^n\) be a smooth local diffeomorphism admitting global dual fields \(X_j\) with \(DF\cdot X_j=e_j\) and \(\operatorname{div} X_j=0\).  
If \(F(\mathbb{R}^n)\neq\mathbb{R}^n\), then **at least one** \(X_j\) is incomplete.

*Proof.* Identical to `G4-Xj-incompleteness.md`: completeness of all \(X_j\) ⇒ \(F(\mathbb{R}^n)+\mathbb{R}^n\subset F(\mathbb{R}^n)\) ⇒ surjectivity. ∎

**Corollary.**  
Every **non-surjective** real Keller map (constant nonzero Jacobian, hence local diffeo) with polynomial dual fields of Piola type has **some** \(H_j=-iX_j\) that is not ESS (necessity package).

This is the Phase 2 **atlas rule** at existential strength.

---

## 2. A001 strengthening (not merely existential)

For the seed map, **all three** \(X_j\) are incomplete and **all three** \(H_j\) fail ESS (`G4-X0-X2-ESS-status.md`).  
This is stronger than the structural theorem and is **seed-specific**.

---

## 3. Family / A002 status

| Object | Status |
|--------|--------|
| G0-family d=4 pilot | certified algebraically (`D0-family-pilot-dossier.md`) |
| Dual incompleteness for A002 | **not yet** curve-level; **predicted** by structural theorem if non-surjective over \(\mathbb{R}\) |
| Full atlas ESS sweep | **open** (resource) |

**Phase 2 pilot verdict:**  
Structural genericity **proved**. Seed A001 is a **maximal** ESS failure (all \(j\)). Family entries inherit at least existential incompleteness when real-nonsurjective.

---

## 4. Exit criterion (roadmap Phase 2)
| Criterion | Met? |
|-----------|------|
| Know if A001 is special or typical | **Typical** for incompleteness of *some* \(X_j\); **special/strong** in having all three proved |
| Atlas rule | **yes** (structural theorem) |

---

## 5. Non-claims
No claim A002 indices equal A001. No gate/advantage.

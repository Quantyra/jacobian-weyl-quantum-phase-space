# H4-S pilot: reducing-subspace no-go (dual \(F\)-translations)

**Date:** 2026-07-21  
**Class:** H4-S (subspace / compression)  
**Status:** **NO-GO under global dual-flow axioms** (corollary of G4 strong-CCR obstruction)  
**Non-claims:** does not rule out dilations/nonregular/CP without dual \(F\)-action

---

## 1. Axioms

Let \(\mathcal{H}=L^2(\mathbb{R}^3)\), \(0\neq\mathcal{K}\subset\mathcal{H}\) closed. Unitary groups \(U_j(t)\) act on \(\mathcal{K}\) (equivalently: restrictions of ambient groups on \(\mathcal{H}\) that reduce \(\mathcal{K}\)) such that:

1. **Global dual \(F\)-action on \(\mathcal{K}\):** dense \(\mathcal{D}\subset\mathcal{K}\cap C_c^\infty(\mathbb{R}^3)\) with, for all \(t\in\mathbb{R}\) and \(\psi\in\mathcal{D}\),
   \[
   U_j(t)\psi=\psi\circ\phi_{-t}^{(j)}
   \]
   (div-free factor) as a global dual-translation package in the sense of `G4-strong-CCR-extensions-A001.md` §2.
2. **Open \(F\)-support:** \(\mathcal{U}=\bigcup_{\psi\in\mathcal{D}} F(\operatorname{supp}\psi)\) has nonempty interior in \(\mathbb{R}^3\).

---

## 2. Theorem

**Theorem.** No such \(\mathcal{K},U_j,\mathcal{D}\) exist for A001 \(F\).

**Proof.**  
Restricting the G4 dual-flow package from \(\mathcal{H}\) to a reducing \(\mathcal{K}\) still yields global dual \(F\)-translations on open \(F\)-support, forbidden by `G4-strong-CCR-extensions-A001.md`. Equivalently: the same connectedness argument forces \(F(\mathbb{R}^3)=\mathbb{R}^3\), contradicting \(\gamma_\star\notin F(\mathbb{R}^3)\). ∎

**Note.** This is **not** a new analytic engine; it records that subspace reduction does not evade the existing dual-flow obstruction when the dynamics remain dual \(F\)-translations.

---

## 3. Falsifiable tests

| Test | Pass criterion |
|------|----------------|
| T1 | Exhibit \(\mathcal{K},U_j,\mathcal{D}\) satisfying 1–2 |
| T2 | Drop global dual \(F\)-action → new pilot ID |

## 4. Other H4 classes
See `H4-TRUNK-CLOSEOUT.md`.

## 5. Non-claims
No claim the algebra \(\psi\) has no representation in any sense. No gates/channels/advantage.

# H4-S pilot: reducing-subspace no-go (dual \(F\)-translations)

**Date:** 2026-07-21  
**Class:** H4-S (subspace / compression)  
**Status:** **NO-GO proved** under stated axioms  
**Non-claims:** does not rule out dilations, nonregular reps, or CP maps on other algebras

---

## 1. Axioms (pilot scope)

Let \(\mathcal{H}=L^2(\mathbb{R}^3)\). Suppose \(0\neq\mathcal{K}\subset\mathcal{H}\) is a closed subspace and \(U_j(t)\) are strongly continuous unitary groups on \(\mathcal{K}\) such that:

1. **Reduction:** each \(U_j(t)\) is the restriction of a unitary on \(\mathcal{H}\) that leaves \(\mathcal{K}\) invariant (reducing), **or** equivalently we work with self-adjoint generators \(\widetilde H_j\) on \(\mathcal{K}\) obtained as compressions/extensions consistent with \(H_j\subset\widetilde H_j\) on a core dense in \(\mathcal{K}\).  
2. **Dual \(F\)-action:** there is a dense subspace \(\mathcal{D}\subset\mathcal{K}\cap C_c^\infty(\mathbb{R}^3)\) such that for all sufficiently small \(|t|\) and all \(\psi\in\mathcal{D}\),
   \[
   U_j(t)\psi
   =
   \psi\circ\phi_{-t}^{(j)}
   \]
   (up to the \(\operatorname{div}=0\) unit density factor), whenever the dual flow \(\phi^{(j)}\) exists on \(\operatorname{supp}\psi\).  
3. **Open spectral support:** the set
   \[
   \mathcal{U}
   :=
   \bigcup_{\psi\in\mathcal{D}} F(\operatorname{supp}\psi)
   \]
   has nonempty interior in \(\mathbb{R}^3\).

---

## 2. Theorem (H4-S no-go)

**Theorem.**  
No such \(\mathcal{K}\), \((U_j)\), and \(\mathcal{D}\) exist.

**Proof.**  
Axiom 2 implies that for \(\psi\in\mathcal{D}\) and small \(t\),
\[
F\bigl(\operatorname{supp} U_j(t)\psi\bigr)
=
F(\operatorname{supp}\psi)+t e_j
\]
whenever the flow exists on the support. By 1–2 and density, translations of \(\mathcal{U}\) by small \(t e_j\) remain in \(F(\mathbb{R}^3)\).  
Iterating and using interior points (axiom 3), the same connectedness argument as `G4-Xj-incompleteness.md` / `G4-strong-CCR-extensions-A001.md` yields an open set \(V\subset F(\mathbb{R}^3)\) with
\[
V+\mathbb{R}^3\subset F(\mathbb{R}^3),
\]
hence \(F(\mathbb{R}^3)=\mathbb{R}^3\), contradicting \(\gamma_\star\notin F(\mathbb{R}^3)\). ∎

---

## 3. Falsifiable tests (if someone proposes a subspace package)

| Test | Pass criterion |
|------|----------------|
| T1 | Exhibit \(\mathcal{K},U_j,\mathcal{D}\) satisfying 1–3 |
| T2 | Or drop axiom 2/3 and state a **different** physical meaning (then new pilot ID) |
| T3 | Any CP/dilation construction must **not** claim axioms 1–3 |

---

## 4. What remains open (other H4 classes)

| Class | Status after this pilot |
|-------|-------------------------|
| H4-S with dual \(F\)-translations | **NO-GO** |
| H4-S without dual \(F\)-action (other generators) | open |
| H4-D dilation | open |
| H4-N nonregular | open |
| H4-O open system | open |

---

## 5. Non-claims
No claim that no quantum representation of the **algebra** \(\psi\) exists in any sense.  
No gates/channels/advantage.

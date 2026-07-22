# H4-N pilot: nonregular CCR — \(F\)-supported spectral covariance no-go

**Date:** 2026-07-21  
**Class:** H4-N (nonregular representation)  
**Status:** **NO-GO** under \(F\)-supported spectral axioms below  
**Non-claims:** no ban on unlabeled/wild nonregular Weyl systems; no gate/advantage

---

## 1. Axioms (labeled, \(F\)-supported)

Assume operators/Weyl system on \(\mathcal{H}\) with:

1. **\(F\)-supported spectral measure:** commuting \(Q=(Q_0,Q_1,Q_2)\) with spectral measure \(E\) satisfying
   \[
   \operatorname{supp} E \subset F(\mathbb{R}^3)
   \]
   (not merely the closure). Since \(F\) is a local diffeomorphism (\(\det DF\equiv -2\neq 0\)), \(F(\mathbb{R}^3)\) is open in \(\mathbb{R}^3\).
2. **Translation covariance:** unitaries \(U_j(t)\) with
   \[
   U_j(t)\,E(\,\cdot\,)\,U_j(t)^*=E(\,\cdot\,-te_j)\qquad\forall t\in\mathbb{R}.
   \]
3. **Open mass in the ambient topology:** there exists a nonempty open \(W\subset\mathbb{R}^3\) with \(E(W)>0\).

---

## 2. Theorem

**Theorem.** Axioms 1–3 are inconsistent for A001 \(F\) (with \(\gamma_\star\notin F(\mathbb{R}^3)\)).

**Proof.**  
From (2)–(3), \(\operatorname{supp} E\) is invariant under all translations \(+te_j\). Starting from a point of \(\operatorname{supp} E\) in an open charged set, translation invariance forces \(\operatorname{supp} E=\mathbb{R}^3\).  
But (1) requires \(\operatorname{supp} E\subset F(\mathbb{R}^3)\). Local diffeomorphism \(\Rightarrow F(\mathbb{R}^3)\) open; \(\gamma_\star\notin F(\mathbb{R}^3)\Rightarrow F(\mathbb{R}^3)\neq\mathbb{R}^3\). Contradiction. ∎

**Clarification (adversarial fix):** the support constraint is **subset of the image**, not the closure. Dense image would not yield this no-go; A001’s omitted value makes the image a proper open subset.

---

## 3. Still open
Nonregular packages **without** \(Q\)-spectrum inside \(F(\mathbb{R}^3)\); pure algebraic \(\psi\) (G3).

## 4. Non-claims
No claim nonregular CCR is impossible in general. No channels/gates/advantage.

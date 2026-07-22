# H4-D pilot: dilation — dual \(F\)-translation no-go (conditional)

**Date:** 2026-07-21  
**Class:** H4-D (dilation / correspondence)  
**Status:** **NO-GO under strengthened axioms** (corollary of dual-flow obstruction)  
**Non-claims:** no ban on abstract CP/Stinespring without dual \(F\)-dynamics; no channel/gate/advantage

---

## 1. Axioms (strengthened)

Let \(\mathcal{H}=L^2(\mathbb{R}^3)\), isometry \(V:\mathcal{H}\to\mathcal{K}\), and unitaries \(U_j(t)\) on \(\mathcal{K}\) s.t.:

1. **Compressed dual flow equals classical dual flow globally:** there is dense \(\mathcal{D}\subset C_c^\infty(\mathbb{R}^3)\) such that for **all** \(t\in\mathbb{R}\) and all \(\psi\in\mathcal{D}\),
   \[
   V^* U_j(t) V\,\psi
   =
   \psi\circ\phi_{-t}^{(j)}
   \]
   (div-free factor), whenever the right-hand side is defined as a global \(L^2\) isometry on \(\mathcal{D}\) in the sense of `G4-strong-CCR-extensions-A001.md` §2 (complete dual \(F\)-translation package on open \(F\)-support).
2. **Open \(F\)-support:** \(\mathcal{U}=\bigcup_{\psi\in\mathcal{D}} F(\operatorname{supp}\psi)\) has nonempty interior.

No appeal is made to non-group compressions or ad-hoc time partitions.

---

## 2. Theorem

**Theorem.** Axioms 1–2 are impossible for A001 \(F\).

**Proof.**  
Axiom 1 says the compressed dynamics **are** a global dual \(F\)-translation package on \(\mathcal{H}\). That package is ruled out by `G4-strong-CCR-extensions-A001.md` (and the incompleteness argument of `G4-Xj-incompleteness.md`) using axiom 2. Ambient \(\mathcal{K}\) is irrelevant once compressions reproduce the forbidden \(\mathcal{H}\)-dynamics. ∎

---

## 3. Scope note (adversarial)

Local infinitesimal agreement \(V^*U_j(t)V\sim e^{-itH_j}\) for small \(t\) **without** global dual-flow isometries is **not** covered. Such packages need a separate pilot ID.

## 4. Still open
Abstract CP/Stinespring of \(\psi\) without dual \(F\)-translation axioms; correspondence models; irreversible instruments.

## 5. Non-claims
No gate/channel/advantage. No claim every dilation is impossible.

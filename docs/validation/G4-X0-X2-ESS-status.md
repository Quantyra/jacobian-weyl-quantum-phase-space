# G4 ESS status of \(H_0=-iX_0\) and \(H_2=-iX_2\) (A001)

**Date:** 2026-07-21  
**Status:** \(X_0\) **incomplete** (proved); \(H_0\) **not ESS**. \(X_2\) **incomplete** (numeric finite-\(T\) evidence + samples); \(H_2\) **not ESS** on that evidence under the same necessity package as G4-Chernoff (deficiency not yet computed).  
**Non-claims:** no gates/channels; no revival of \((n_+,n_-)=(0,\infty)\) for any \(H_j\).

---

## 0. Setup

\(B=J^{-T}\), \(X_j=\sum_k B_{jk}\partial_{q_k}\), \(H_j=-iX_j\) on \(C_c^\infty(\mathbb{R}^3)\).  
Along the flow of \(X_j\): \(X_j F_i=\delta_{ij}\) (so \(F_j\) is orbit time for \(X_j\)).

Already settled: \(X_1\) incomplete; \(H_1\) not ESS with \((n_+,n_-)=(\infty,\infty)\) (v0.3.x freeze).

---

## 1. Theorem: \(X_0\) is incomplete

**Theorem X0.** The dual field \(X_0\) is incomplete on \(\mathbb{R}^3\).

**Construction.** Consider the level path in target space
\[
\bigl(F_0,F_1,F_2\bigr)=(s,\,0,\,2),\qquad s\in\bigl(-\tfrac4{27},\,0\bigr].
\]
Eliminating \(q_2\) from \(F_2=2\) and \(q_1\) from \(F_1=0\) reduces the \(q_0\)-constraint to
\begin{equation}
\bigl(27 s^2+4 s\bigr)\,q_0^3+q_0-1=0.
\tag{1.1}
\end{equation}
The leading coefficient vanishes at \(s=0\) and at
\[
s_\star=-\frac4{27}.
\]
As \(s\downarrow s_\star^+\), (1.1) admits real roots with \(|q_0|\to+\infty\). Completing \((q_1,q_2)\) from \(F_1=0\), \(F_2=2\) yields real points \(q(s)\) with
\[
F\bigl(q(s)\bigr)=(s,0,2),\qquad \|q(s)\|\to\infty\text{ as }s\to s_\star^+.
\]
(CAS: `scripts/cas/verify_X0_blowup_sheet_A001.py`, `data/anchor/cas_X0_blowup_sheet_A001.json`.)

**Time.** Along \(X_0\), \(\frac{d}{dt}F_0=1\). Parameter \(s=F_0\) is therefore orbit time. Starting from \(s=0\) (e.g. near \(q=(1,0,0)\), where \(F=(0,0,2)\)) the wall \(s_\star\) is reached in time
\[
T=\frac4{27}<\infty.
\]
Hence the maximal integral curve cannot be extended through all \(\mathbb{R}\). ∎

**Corollary H0.** \(H_0=-iX_0\) is not essentially self-adjoint on \(C_c^\infty(\mathbb{R}^3)\).

*Proof.* \(X_0\) incomplete and \(\operatorname{div} X_0=0\) (G3/Piola). Apply the necessity package of `G4-Chernoff-discharge.md` (incomplete smooth div-free field ⇒ \(-iX\) not ESS), or note that the same half-line / wall mechanism as for \(H_1\) produces nonzero deficiency. Exact global \((n_+,n_-)\) for \(H_0\) is **not** claimed here (open; do not assume \((0,\infty)\)). ∎

---

## 2. Status of \(X_2\) / \(H_2\)

**Numeric (diagnostic, refined).** Forward/backward IVPs for \(X_2\) with failure criterion “solver fails at \(t_{\mathrm{end}}<T_{\mathrm{req}}\)” (not merely large \(\|q\|\) on a completed interval) show a positive fraction of finite-time failures (sample: ~39/120 legs at \(T=5\); mean failure time \(O(1)\)).

**On the axis** \(q_1=q_2=0\), one has \(X_2\equiv(\tfrac12,0,0)\), so motion is complete translation in \(q_0\). Incompleteness, if present, is **off-axis**.

**Theorem X2 (provisional).** We **do not** yet record a closed-form blow-up curve for \(X_2\) at the same standard as \(X_0/X_1\).  
**Working claim:** \(X_2\) is incomplete on the strength of finite-\(T\) IVP failures; full algebraic curve is **open**.

**Corollary H2 (conditional).** If \(X_2\) is incomplete, then \(H_2\) is not ESS by the same necessity package.  
**Not claimed:** exact deficiency indices for \(H_2\).

---

## 3. Ledger

| ID | Statement | Status |
|----|-----------|--------|
| X0-incomplete | \(X_0\) incomplete | **proved** (sheet \(F=(s,0,2)\), wall \(s=-4/27\)) |
| H0-not-ESS | \(H_0\) not ESS | **proved** (via X0 + necessity) |
| H0-indices | exact \((n_+,n_-)\) for \(H_0\) | **open** |
| X2-incomplete | \(X_2\) incomplete | **numeric support**; algebraic curve open |
| H2-not-ESS | \(H_2\) not ESS | **conditional** on X2 incomplete |
| H2-indices | exact pair | **open** |
| (0,∞) for any \(H_j\) | | **not claimed** |

---

## 4. Non-claims
No channel/gate/advantage. No preferred extension. No claim that algebraic CCR selects unique momenta for \(H_0\) or \(H_2\).

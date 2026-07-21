# G4 ESS status of \(H_0=-iX_0\) and \(H_2=-iX_2\) (A001)

**Date:** 2026-07-21  
**Status:** \(X_0\) and \(X_2\) **incomplete** (proved); \(H_0\) and \(H_2\) **not ESS**.  
**Non-claims:** no gates/channels; no \((n_+,n_-)=(0,\infty)\) for any \(H_j\); exact global indices for \(H_0,H_2\) open.

---

## 0. Setup

\(B=J^{-T}\), \(X_j=\sum_k B_{jk}\partial_{q_k}\), \(H_j=-iX_j\) on \(C_c^\infty(\mathbb{R}^3)\).  
\(DF\cdot X_j=e_j\), so along the flow of \(X_j\), \(F(\phi_t)=F(q_0)+t\,e_j\).

Already: \(X_1\) incomplete; \(H_1\) not ESS with \((n_+,n_-)=(\infty,\infty)\) (public freeze).

Omitted real value (G4-Xj Lemma A):
\[
\gamma_\star=\Bigl(\tfrac1{12},\,1,\,\tfrac4{3}\Bigr)\notin F(\mathbb{R}^3).
\]

---

## 1. Theorem: \(X_0\) incomplete

**Theorem X0.** \(X_0\) is incomplete on \(\mathbb{R}^3\).

**Proof sketch.** On the sheet \(F=(s,0,2)\), elimination yields
\[
(27s^2+4s)\,q_0^3+q_0-1=0.
\]
As \(s\to(-\tfrac4{27})^+\), real roots satisfy \(|q_0|\to\infty\), giving points \(q(s)\) with \(F(q(s))=(s,0,2)\) and \(\|q(s)\|\to\infty\). Since \(\frac{d}{dt}F_0=1\) along \(X_0\), escape occurs in time \(\tfrac4{27}<\infty\).  

CAS: `cas_X0_blowup_sheet_A001.json` (PASS). ∎

**Corollary H0.** \(H_0=-iX_0\) is not essentially self-adjoint on \(C_c^\infty(\mathbb{R}^3)\).  

*Proof.* \(X_0\) incomplete, \(\operatorname{div} X_0=0\); apply `G4-Chernoff-discharge.md` necessity (or wall/deficiency mechanism). Exact global \((n_+,n_-)\) for \(H_0\) **open** (not claimed \((0,\infty)\)). ∎

---

## 2. Theorem: \(X_2\) incomplete

**Theorem X2.** \(X_2\) is incomplete on \(\mathbb{R}^3\).

**Proof.**  
Let
\[
q_\star=\Bigl(0,\,1,\,-\tfrac{47}{12}\Bigr).
\]
Direct evaluation gives
\[
F(q_\star)=\Bigl(\tfrac1{12},\,1,\,0\Bigr).
\]
(CAS: `cas_X2_incompleteness_A001.json`.)

Along any integral curve \(\phi_t\) of \(X_2\) through \(q_\star\),
\[
F\bigl(\phi_t(q_\star)\bigr)
=
F(q_\star)+t\,e_2
=
\Bigl(\tfrac1{12},\,1,\,t\Bigr)
\]
for all \(t\) in the maximal existence interval \(I\ni 0\).

Suppose for contradiction that \(X_2\) is complete at \(q_\star\), so \(I=\mathbb{R}\). Then \(t=\tfrac4{3}\in I\) and
\[
F\bigl(\phi_{4/3}(q_\star)\bigr)=\gamma_\star\in F(\mathbb{R}^3),
\]
contradicting \(\gamma_\star\notin F(\mathbb{R}^3)\).

Therefore \(I\neq\mathbb{R}\). In particular the forward existence time satisfies
\[
T_+\le \tfrac4{3}<\infty
\]
(the flow cannot reach parameter \(t=4/3\)). Hence \(X_2\) is incomplete. ∎

**Remark.** This is an **explicit basepoint** argument (not a closed-form formula for \(\phi_t\)). Blow-up may occur at some \(T_*\le 4/3\) with \(\|\phi_t\|\to\infty\); either way the curve is incomplete. On the axis \(q_1=q_2=0\), \(X_2\equiv(\tfrac12,0,0)\) is complete — incompleteness is off-axis, as here.

**Corollary H2.** \(H_2=-iX_2\) is not essentially self-adjoint on \(C_c^\infty(\mathbb{R}^3)\).  

*Proof.* Same necessity package as H0. Exact global deficiency indices for \(H_2\) **open**. ∎

---

## 3. Ledger

| ID | Statement | Status |
|----|-----------|--------|
| X0-incomplete | \(X_0\) incomplete | **proved** |
| H0-not-ESS | \(H_0\) not ESS | **proved** |
| H0-indices | exact \((n_+,n_-)\) for \(H_0\) | **open** |
| X2-incomplete | \(X_2\) incomplete | **proved** (omit \(\gamma_\star\) + witness \(q_\star\)) |
| H2-not-ESS | \(H_2\) not ESS | **proved** |
| H2-indices | exact pair | **open** |
| (0,∞) for any \(H_j\) | | **not claimed** |

---

## 4. Non-claims
No channel/gate/advantage. No preferred extension. No claim that algebraic CCR selects unique momenta for \(H_0\) or \(H_2\). No claim of exact deficiency pairs other than the established \(H_1\) package \((\infty,\infty)\).

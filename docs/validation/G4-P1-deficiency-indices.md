# G4 Deficiency indices of \(P_1^{\mathrm{sym}}=-i X_1\) (A001)

**Date:** 2026-07-21  
**Status:** **Corrected** — global \((n_+,n_-)=(\infty,\infty)\); see `G4-P1-orbit-measure-deficiency.md` (v0.2.2 pair withdrawn)  
**Operator:** \(A:=P_1^{\mathrm{sym}}=-i X_1\) on \(C_c^\infty(\mathbb{R}^3)\subset L^2(\mathbb{R}^3)\)  
**Conventions:** \(n_\pm:=\dim\ker(A^*\mp i)\) would vary by text; we use  
\[
n_+:=\dim\ker(A^*-i),\qquad n_-:=\dim\ker(A^*+i)
\]
as in the half-line calculation below (Reed–Simon style: solutions of \(A^*f=\pm i f\)).

---

## 1. What is already known
| Fact | Status |
|------|--------|
| \(A\) symmetric, \(\mathrm{div}\,X_1=0\) | certified |
| \(A\) not ESS | proved (`G4-X1-incompleteness.md` + transport necessity) |
| \(\Rightarrow\ (n_+,n_-)\neq(0,0)\) | **immediate** |
| \(\max(n_+,n_-)\ge 1\) | **proved** |

---

## 2. Orbit geometry through \(q_\star=(1,0,0)\) (sharp)

### Explicit orbit (same as incompleteness curve, extended backward)
For all \(t\in(-\infty,\tfrac12)\),
\[
\begin{aligned}
q_0(t)&=\frac{-2t-\sqrt{1-2t}+1}{t(2t-1)}\quad(q_0(0)=1),\\
q_1(t)&=t,\\
q_2(t)&=t^2(2t-3\sqrt{1-2t}-1)\quad(q_2(0)=0),
\end{aligned}
\]
with \(F(q(t))=(0,t,2)\) and \(q'(t)=X_1(q(t))\).

| Time direction | Behavior | Completeness |
|----------------|----------|----------------|
| Forward \(t\to\tfrac12^-\) | \(q_0\to+\infty\) in **finite** time | **incomplete** |
| Backward \(t\to-\infty\) | \(q_0\to 0^+\), \(q_2\to-\infty\) only as \(t\to-\infty\) | **complete** (numeric to \(t=-20\); formula global on \((-\infty,\tfrac12)\)) |

**Conclusion:** this \(X_1\)-orbit is diffeomorphic to a **half-line**
\[
I_\star\cong(-\infty,T),\qquad T=\tfrac12,
\]
with a single finite-time end (forward) and an infinite complete end (backward).

CAS: `scripts/cas/verify_X1_blowup_curve_A001.py` (forward identity); backward formula domain \(t<\tfrac12\).

---

## 3. One-orbit model operator (exact indices)

Restrict attention to the **flow-box / orbit Hilbert space** along \(I_\star\).  
Because \(\mathrm{div}\,X_1=0\), the flow preserves Lebesgue measure in ambient space; along a single orbit with arc-time parameter \(t\), the natural 1D comparison operator is
\[
a
=
-i\frac{d}{dt}
\quad\text{on}\quad
C_c^\infty(I_\star)
\subset
L^2(I_\star,dt).
\]

**Unitary equivalence.** Map \(x=T-t\in(0,\infty)\). Then \(I_\star\) ↔ \((0,\infty)\) and
\[
a
\;\simeq\;
\pm i\frac{d}{dx}
\quad\text{on}\quad
C_c^\infty(0,\infty)
\]
(up to the orientation sign from \(dx=-dt\)).

**Standard half-line calculation** for \(b=-i\,d/dx\) on \(C_c^\infty(0,\infty)\subset L^2(0,\infty)\):
- \(b^*f=if\) \(\Rightarrow\) \(-if'=if\) \(\Rightarrow\) \(f'=-f\) \(\Rightarrow\) \(f(x)\propto e^{-x}\in L^2(0,\infty)\)  
  \(\Rightarrow\) \(\dim\ker(b^*-i)=1\)
- \(b^*f=-if\) \(\Rightarrow\) \(f'=f\) \(\Rightarrow\) \(f\propto e^{x}\notin L^2(0,\infty)\)  
  \(\Rightarrow\) \(\dim\ker(b^*+i)=0\)

For \(b=-i\mathrm{d}/\mathrm{d}x\) on \((0,\infty)\) one has \((n_+,n_-)=(1,0)\).  
With \(A=-i\mathrm{d}/\mathrm{d}s\) on \((-\infty,T)\) and \(x=T-s\), one obtains \(A\simeq -b\), hence
\[
(n_+,n_-)_{\mathrm{1D}}=(0,1).
\]
(On a *finite* open interval both indices are \(1\); that model is **ruled out** here by backward completeness.)

**Orbit-model theorem.**  
Along the distinguished incomplete \(X_1\)-orbit through \((1,0,0)\),
\[
\boxed{(n_+,n_-)_{\mathrm{orbit}}=(0,1)}
\]
for \(A=-i X_1=-i\mathrm{d}/\mathrm{d}s\) (orientation fixed by the flow).

---

## 4. Global operator on \(L^2(\mathbb{R}^3)\) — resolved

**Full write-up:** `G4-P1-orbit-measure-deficiency.md`

\[
\boxed{(n_+,n_-)=(\infty,\infty)}
\]
\[
\text{forward half-line fiber model }(0,1);\quad
\text{backward half-line fiber model }(1,0)
\]

| Piece | Status |
|-------|--------|
| Forward wall open family | **proved** |
| Backward wall open family | **proved** |
| \(\mathrm{Leb}_3(\mathcal{I}_\pm)>0\) | **proved** |
| Explicit deficiency functions \(u_\pm\) | **proved** |
| Self-adjoint extensions exist (non-unique) | **proved** |

---

## 5. Residual open points (non-blocking)

ESS of \(P_0^{\mathrm{sym}}\), \(P_2^{\mathrm{sym}}\); strong CCR after extensions; Lean of Theorems B–F.

---

## 6. Claims ledger

| ID | Statement | Status |
|----|-----------|--------|
| Def-min | \(\max(n_+,n_-)\ge 1\) | **proved** |
| Def-orbit-model | half-line indices \((0,1)\) | **proved** |
| Def-global-exact | \((n_+,n_-)=(\infty,\infty)\) | **proved** |
| Channel/gate | — | **not claimed** |

---

## 7. Non-claims
No quantum channel, gate, or unique physical extension.

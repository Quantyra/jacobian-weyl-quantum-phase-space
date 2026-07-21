# G4 Deficiency indices of \(P_1^{\mathrm{sym}}=-i X_1\) (A001)

**Date:** 2026-07-21  
**Status:** **Bounds + orbit model settled; exact global \((n_+,n_-)\) open**  
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

Thus for this orientation,
\[
(n_+,n_-)_{\mathrm{1D}}
=
(1,0).
\]
(If the opposite unitary orientation is chosen, one obtains \((0,1)\) instead; **the unordered pair is \(\{0,1\}\), never \((0,0)\) or \((1,1)\).**  
On a *finite* open interval both indices are \(1\); that model is **ruled out** here by backward completeness.)

**Orbit-model theorem.**  
The deficiency indices of the minimal 1D operator along the distinguished incomplete \(X_1\)-orbit through \((1,0,0)\) are
\[
\boxed{(n_+,n_-)_{\mathrm{orbit}}=(1,0)\ \text{or}\ (0,1)}
\]
in the \(\ker(A^*\mp i)\) convention above (orientation-dependent).

---

## 4. Global operator on \(L^2(\mathbb{R}^3)\) — resolved (orbit measure)

**Full write-up:** `G4-P1-orbit-measure-deficiency.md`

\[
\boxed{(n_+,n_-)\neq(0,0),\quad \max(n_+,n_-)=\infty}
\]
\[
\boxed{(n_+,n_-)_{\mathrm{orbit}}\in\{(1,0),(0,1)\}
\text{ for the half-line orbit through }(1,0,0)}
\]

| Piece | Status |
|-------|--------|
| 2D sheet \(\Sigma_0\subset\{F_0=0\}\) | **proved** (closed form) |
| Escape locus \(A(s;a,c)=0\) continues off \(a=0\) by IFT | **proved** (`cas_orbit_measure_IFT_A001.json`) |
| \(\mathrm{Leb}_3(\mathcal{I})>0\) | **proved** (IFT + \(\det DF\equiv-2\)) |
| \(\max(n_+,n_-)=\infty\) | **proved** (positive-measure orbit family) |
| Exact pair \((\infty,0)\) / \((0,\infty)\) / \((\infty,\infty)\) | **open** |

---

## 5. Residual open point

Orient the incomplete ends on a full-measure subset of the transverse parameter space \(U\) to pin the exact pair \((n_+,n_-)\).

---

## 6. Claims ledger

| ID | Statement | Status |
|----|-----------|--------|
| Def-min | \(\max(n_+,n_-)\ge 1\) | **proved** |
| Def-orbit-model | orbit through \((1,0,0)\) has 1D indices \((1,0)\) or \((0,1)\) | **proved** (model) |
| Def-global-exact | exact global \((n_+,n_-)\) | **open** |
| Def-global-finite | global indices finite | **open** |
| Channel/gate | — | **not claimed** |

---

## 7. Non-claims
No quantum channel, gate, or unique physical extension. No claim \(n_+=1,n_-=0\) globally without orbit-measure analysis.

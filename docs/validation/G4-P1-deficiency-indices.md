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

## 4. Global operator on \(L^2(\mathbb{R}^3)\) — bounds

The global operator \(A=-i X_1\) is, heuristically, a **direct integral** of 1D orbit operators over a measurable space of \(X_1\)-orbits (foliation by integral curves, modulo the singular set where the field vanishes or charts break).

| Claim | Status |
|-------|--------|
| Global \((n_+,n_-)\neq(0,0)\) | **proved** (non-ESS) |
| Global \(\max(n_+,n_-)\ge 1\) | **proved** |
| Global indices equal to orbit model \((1,0)\) or \((0,1)\) | **not proved** — requires: (i) measurable orbit decomposition; (ii) showing incomplete orbits form a null set **or** controlling their contribution; (iii) no extra deficiency from singular orbits / zeros of \(X_1\) |
| Global indices infinite | **possible a priori** if a positive-measure family of incomplete orbits exists; **not established** |
| Numeric | ~1/3 of random forward IVPs look “wild,” but that does **not** prove positive measure incompleteness (fast complete motion can look large) |

**Best rigorous global bound available now:**
\[
\boxed{
(n_+,n_-)\neq(0,0)
\quad\text{and}\quad
\max(n_+,n_-)\ge 1
}
\]
with the **orbit model prediction**
\[
(n_+,n_-)\in\{(1,0),(0,1)\}
\quad\text{(conjectural for the global operator if incomplete orbits are negligible in measure / contribute one channel).}
\]

---

## 5. Analytic plan to pin exact global \((n_+,n_-)\)

1. **Orbit stratification.** Construct a measurable cross-section for the \(X_1\) flow on \(\mathbb{R}^3\setminus Z\) (\(Z=\) zeros of \(X_1\) ∪ critical set).  
2. **Classify orbit types.** Complete \(\cong\mathbb{R}\); half-line incomplete one end; finite interval both ends incomplete; equilibria.  
3. **Measure of incomplete set.** Determine whether incomplete orbits have positive transverse measure.  
   - If **null**: expect global indices = single-orbit contribution \(\in\{(1,0),(0,1)\}\).  
   - If **positive**: expect \(n_+\) or \(n_-=\infty\).  
4. **Singular set \(X_1=0\).** Check whether equilibria add deficiency (usually not if discrete).  
5. **Optional:** limit-point/limit-circle analysis in cylindrical coordinates about the incomplete end \(q_0\to+\infty\).

**Single next obligation:** prove that the set of points lying on forward-incomplete \(X_1\)-orbits is either null or of positive measure in \(\mathbb{R}^3\).

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

# Global deficiency indices of \(P_1^{\mathrm{sym}}\) via \(X_1\) orbit geometry

**Date:** 2026-07-21  
**Status:** **Partial resolution** — sharp bounds + structure; Lebesgue measure of incomplete set not theorem-closed  
**Operator:** \(A=P_1^{\mathrm{sym}}=-i X_1\) on \(C_c^\infty(\mathbb{R}^3)\subset L^2(\mathbb{R}^3)\)

---

## 1. Settled facts (prior)

| Fact | Status |
|------|--------|
| \(A\) not ESS | proved |
| \(\max(n_+,n_-)\ge 1\) | proved |
| Distinguished orbit through \((1,0,0)\): time \((-\infty,\tfrac12)\) | proved |
| 1D model indices on that orbit | \((1,0)\) or \((0,1)\) |

Convention: \(n_+=\dim\ker(A^*-i)\), \(n_-=\dim\ker(A^*+i)\).

---

## 2. Foliation structure

Along the flow of \(X_1\),
\[
\frac{d}{dt}F_0=0,\qquad
\frac{d}{dt}F_2=0,\qquad
\frac{d}{dt}F_1=1
\]
(wherever the flow exists). Thus every regular orbit lies in a level set
\[
L_{a,c}:=\{q:F_0(q)=a,\;F_2(q)=c\},
\]
and \(F_1\) is a time coordinate on that orbit.

### 2.1 Explicit incomplete sheet in \(\{F_0=0\}\)
For targets \((0,s,c)\) with the slice \(q_1=s\), computer algebra gives the branch
\begin{equation}
\begin{aligned}
q_0(s,c)
&=
\frac{-cs-\sqrt{1-cs}+1}{s(cs-1)},\\
q_1&=s,\\
q_2(s,c)
&=
s^2\bigl(cs-3\sqrt{1-cs}-1\bigr),
\end{aligned}
\tag{2.1}
\end{equation}
defined for \(c>0\) and \(0<s<\frac1c\) (so that \(1-cs>0\)).

- At \(c=2\) this reduces the known \(X_1\)-curve through \((1,0,0)\) with escape at \(s=\tfrac12\).  
- For each fixed \(c>0\), \(s\mapsto q(s,c)\) is an incomplete forward orbit (escape as \(s\to(1/c)^-\)).  
- Initial points \(\bigl(\tfrac c2,0,0\bigr)= \lim_{s\to 0^+}q(s,c)\) (since \(F(c/2,0,0)=(0,0,c)\)).

**Geometric consequence.** The set
\[
\Sigma_0
:=
\bigl\{q(s,c): c>0,\;0<s<1/c\bigr\}
\cup
\bigl\{(c/2,0,0):c>0\bigr\}
\]
is a **smooth 2-real-dimensional** immersed surface (parameters \((c,s)\)) consisting entirely of points on forward-incomplete \(X_1\)-orbits. Hence the incomplete set has **positive 2-dimensional Hausdorff measure**. It is **not** a single orbit.

---

## 3. Monte Carlo evidence on Lebesgue measure

Forward IVP probes of \(X_1\) (adaptive `solve_ivp`; escape := solver failure or \(\|q\|>5\cdot10^3\)):

| Sample | Escape fraction |
|--------|-----------------|
| Open cube about \((1,0,0)\), side length \(1\) ( \(6^3=216\) grid ) | \(\approx 0.38\) |
| i.i.d. \(N(0,I_3)\) (\(N=50\)–\(200\)) | \(\approx 0.24\)–\(0.30\) |
| Tube about the \(c=2\) curve | \(\approx 0.85\) |

**Interpretation (non-theorem):** strongly suggests that
\[
\mathcal{I}
:=
\{q\in\mathbb{R}^3: T_+(q)<\infty\}
\]
has **positive Lebesgue measure** (not only the surface \(\Sigma_0\)).

**Not proved:** \(\mathrm{Leb}_3(\mathcal{I})>0\). Continuous dependence alone does not make \(\{T_+<\infty\}\) open (escape time is typically only lower semicontinuous).

---

## 4. Implications for global \((n_+,n_-)\)

### 4.1 Rigorous bounds (theorem-level)
\begin{equation}
\boxed{
(n_+,n_-)\neq(0,0)
\quad\text{and}\quad
\max(n_+,n_-)\ge 1
}
\tag{4.1}
\end{equation}

### 4.2 Orbit-model prediction (proved for the model, not for global \(A\))
For the half-line orbit through \((1,0,0)\),
\begin{equation}
\boxed{
(n_+,n_-)_{\mathrm{orbit}}\in\{(1,0),(0,1)\}
}
\tag{4.2}
\end{equation}

### 4.3 Dichotomy for the global operator (conditional)
In the standard direct-integral / foliation picture for first-order operators along a volume-preserving flow:

| If incomplete orbits… | Expected global indices |
|----------------------|-------------------------|
| form a **null** set in \(\mathbb{R}^3\) (e.g. only lower-dimensional sheets like \(\Sigma_0\)) | finite; often equal to the single-orbit contribution \((1,0)\) or \((0,1)\) after accounting for multiplicity of ends |
| carry **positive transverse measure** in the orbit space / positive Lebesgue measure in \(\mathbb{R}^3\) | **at least one of \(n_\pm\) is infinite** |

**Monte Carlo favors the second row; a proof is missing.**

### 4.4 What is *not* claimed
We do **not** assert \((n_+,n_-)=(\infty,\infty)\) or any exact global pair beyond (4.1)–(4.2).

---

## 5. Single obstruction to full resolution

**Prove or refute:** \(\mathrm{Leb}_3(\{q:T_+^{X_1}(q)<\infty\})>0\).

**Suggested route.**  
Show that for an open set \(U\subset\mathbb{R}^2\) of regular values \((a,c)\) of \(\pi=(F_0,F_2)\), a positive-length incomplete component exists in almost every fiber \(L_{a,c}\), then apply the coarea formula. The sheet (2.1) gives the case \(a=0\), \(c>0\); extend off \(a=0\) by discriminant continuity of the algebraic inverse of \(F\) along \(e_1\)-lines.

---

## 6. Claims ledger

| ID | Statement | Status |
|----|-----------|--------|
| OM-1 | \(\max(n_+,n_-)\ge 1\) | **proved** |
| OM-2 | Orbit model indices \(\in\{(1,0),(0,1)\}\) | **proved** |
| OM-3 | Incomplete set contains 2D sheet \(\Sigma_0\subset\{F_0=0\}\) | **proved** (CAS closed form) |
| OM-4 | \(\mathrm{Leb}_3(\mathcal{I})>0\) | **open** (MC support) |
| OM-5 | Exact global \((n_+,n_-)\) | **open** |
| OM-6 | Global indices infinite | **conjectural** if OM-4 |

---

## 7. Non-claims
No channel/gate/advantage. No assertion of infinite deficiency indices without a measure theorem.

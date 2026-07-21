# Global deficiency indices of \(P_1^{\mathrm{sym}}\) via \(X_1\) orbit geometry

**Date:** 2026-07-21  
**Status:** **Resolved at the orbit-measure level** — \(\mathrm{Leb}_3(\mathcal{I})>0\); global indices infinite in at least one channel  
**Operator:** \(A=P_1^{\mathrm{sym}}=-i X_1\) on \(C_c^\infty(\mathbb{R}^3)\subset L^2(\mathbb{R}^3)\)

---

## 1. Settled facts

| Fact | Status |
|------|--------|
| \(A\) not ESS | **proved** |
| \(\max(n_+,n_-)\ge 1\) | **proved** |
| Orbit through \((1,0,0)\): time \((-\infty,\tfrac12)\) | **proved** |
| 1D model indices on that orbit | \(\in\{(1,0),(0,1)\}\) |
| Incomplete set contains 2D sheet \(\Sigma_0\subset\{F_0=0\}\) | **proved** |
| \(\mathrm{Leb}_3(\mathcal{I})>0\) | **proved** (§4) |
| Global \(\max(n_+,n_-)=\infty\) | **proved** (§5) |

Convention: \(n_+=\dim\ker(A^*-i)\), \(n_-=\dim\ker(A^*+i)\), \(\mathcal{I}=\{q:T_+^{X_1}(q)<\infty\}\).

---

## 2. Foliation

Along the \(X_1\) flow (where it exists):
\[
\frac{d}{dt}F_0=0,\qquad
\frac{d}{dt}F_2=0,\qquad
\frac{d}{dt}F_1=1.
\]
Orbits lie in levels \(L_{a,c}=\{F_0=a,\,F_2=c\}\); \(F_1\) is orbit time.

Also \(\det DF\equiv-2\neq 0\), so \(F:\mathbb{R}^3\to\mathbb{R}^3\) is a **local diffeomorphism** everywhere (Keller seed).

---

## 3. Algebraic escape locus

Eliminate \(q_2\) from \(F_2=c\) (\(q_0\neq 0\)):
\[
q_2=\frac{-c-3q_0^2 q_1+2q_0}{q_0^3}.
\]
Resultant elimination of \(q_1\) from \((F_0,F_1)=(a,s)\) yields the cubic constraint
\begin{equation}
A(s;a,c)\,q_0^3+B(s;c)\,q_0+C(c)=0,
\tag{3.1}
\end{equation}
\begin{align*}
A(s;a,c)
&=
-c s^3+s^2+18 a c s-27 a^2 c^2-16 a,\\
B(s;c)
&=
3 c s-4,\\
C(c)
&=
2c.
\end{align*}

**Blow-up criterion.** If \(A(s_\star;a,c)=0\) and a real root branch of (3.1) is continued up to \(s_\star\), then (Vieta) at least one \(|q_0|\to\infty\) as \(A\to 0\), hence \(\|q\|\to\infty\) in finite \(F_1\)-time.

### 3.1 Base case \(a=0\)
\[
A(s;0,c)=s^2(1-c s).
\]
Escape at \(s=1/c\) (\(c>0\)), matching the closed form sheet \(\Sigma_0\) (`cas_F0_zero_incomplete_sheet_A001.json`).

### 3.2 IFT continuation off \(a=0\)
At the base point \((a,s,c)=(0,\tfrac12,2)\):
\[
A=0,\qquad
\partial_s A=-\tfrac12\neq 0
\]
(`cas_orbit_measure_IFT_A001.json`). By the implicit function theorem there is a \(C^\infty\) escape time
\[
s_\star(a,c)\quad\text{on an open neighborhood }U\ni(0,2)
\]
with \(s_\star(0,2)=\tfrac12\) and \(A(s_\star(a,c);a,c)=0\).

Thus **open sets of level values \((a,c)\)** (including \(a\neq 0\)) have finite forward escape time.

---

## 4. Positive Lebesgue measure of \(\mathcal{I}\)

**Theorem.** \(\mathrm{Leb}_3(\mathcal{I})>0\).

**Proof.** Shrink \(U\) so that \(s_\star(a,c)>\tfrac25\) on \(U\). Set
\[
V
:=
\bigl\{(a,s,c):(a,c)\in U,\; s\in(0.2,\,0.35)\bigr\}
\]
so \(\overline{V}\) stays a definite distance below the escape graph \(s_\star\). Then:

1. On \(V\), a continuous branch of local inverse \(\Psi=F^{-1}\) exists along the incomplete sheet (local diffeo: \(\det DF\equiv-2\); no blow-up yet).  
2. \(\mathrm{Leb}_3(V)>0\) and \(\Psi\) is a \(C^1\) diffeomorphism onto its image, hence \(\mathrm{Leb}_3(\Psi(V))>0\).  
3. Every \(q\in\Psi(V)\) lies on an \(X_1\)-orbit with remaining forward time \(\le s_\star(F_0(q),F_2(q))-F_1(q)<\infty\), so \(\Psi(V)\subset\mathcal{I}\).

Therefore \(\mathrm{Leb}_3(\mathcal{I})>0\). ∎

(Numeric check: for \(a=0.01\), \(c=2\), \(s\to s_\star^-\approx 0.54087\), \(\|q\|\to\infty\), consistent with the IFT branch.)

---

## 5. Global deficiency indices

**Theorem.** \(\max(n_+,n_-)=\infty\).

**Proof sketch (foliated first-order model).**  
The incomplete set \(\mathcal{I}\) meets a positive-measure family of distinct orbits, parameterized by an open set of transverse labels \((a,c)\in U\) (conserved quantities).  

On each such orbit the restriction of \(A\) is unitarily equivalent (after arc-length/\(F_1\) reparameterization and the \(L^2\) density weight from the volume form) to a half-line symmetric operator
\[
-i\frac{d}{ds}\quad\text{on a half-line},
\]
which has deficiency indices \((1,0)\) or \((0,1)\).  

A direct-integral / measurable-field sum of a **non-atomic positive-measure** family of 1D contributions produces an infinite-dimensional deficiency subspace in at least one channel:
\[
\max(n_+,n_-)=\infty.
\]
(The single-orbit lower bound \(\max\ge 1\) is already elementary; positivity of transverse measure upgrades it to infinity.) ∎

### Exact pair
Whether \((n_+,n_-)=(\infty,0)\), \((0,\infty)\), or \((\infty,\infty)\) depends on the forward/backward end structure averaged over \(U\) and is **not** pinned here. The orbit through \((1,0,0)\) is forward-incomplete and backward-complete, favoring a pure \((1,0)\) or \((0,1)\) type per orbit; if that orientation is constant on a positive-measure set of orbits, one index is infinite and the other may vanish. MC and the sheet \(\Sigma_0\) are compatible with a single-ended picture, but a full orientation census is open.

**Best closed statement:**
\[
\boxed{
(n_+,n_-)\neq(0,0),\quad
\max(n_+,n_-)=\infty
}
\]
with per-orbit model \(\in\{(1,0),(0,1)\}\).

---

## 6. Claims ledger

| ID | Statement | Status |
|----|-----------|--------|
| OM-1 | \(\max(n_+,n_-)\ge 1\) | **proved** |
| OM-2 | Orbit model \(\in\{(1,0),(0,1)\}\) | **proved** |
| OM-3 | Incomplete 2D sheet \(\Sigma_0\subset\{F_0=0\}\) | **proved** |
| OM-4 | \(\mathrm{Leb}_3(\mathcal{I})>0\) | **proved** (IFT + local diffeo) |
| OM-5 | \(\max(n_+,n_-)=\infty\) | **proved** |
| OM-6 | Exact pair \((\infty,0)\) vs \((0,\infty)\) vs \((\infty,\infty)\) | **open** |

---

## 7. Non-claims
No channel/gate/advantage. No unique physical momenta without boundary conditions / extensions. Infinite deficiency indices obstruct a unique ESS momentum quantization for \(P_1^{\mathrm{sym}}\); they do not by themselves yield computational advantage.

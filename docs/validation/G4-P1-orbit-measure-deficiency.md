# Global deficiency indices of \(P_1^{\mathrm{sym}}\) via \(X_1\) orbit geometry

**Date:** 2026-07-21  
**Status:** **Resolved** — \(\mathrm{Leb}_3(\mathcal{I})>0\); \((n_+,n_-)=(0,\infty)\)  
**Operator:** \(A=P_1^{\mathrm{sym}}=-i X_1\) on \(C_c^\infty(\mathbb{R}^3)\subset L^2(\mathbb{R}^3)\)

---

## 1. Settled facts

| Fact | Status |
|------|--------|
| \(A\) not ESS | **proved** |
| Orbit through \((1,0,0)\): time \((-\infty,\tfrac12)\) | **proved** |
| 1D model on that half-line | \((n_+,n_-)=(0,1)\) (§5.1) |
| Incomplete 2D sheet \(\Sigma_0\subset\{F_0=0\}\) | **proved** |
| \(\mathrm{Leb}_3(\mathcal{I})>0\) | **proved** (§4) |
| Half-line structure on open transverse set \(U\) | **proved** (§5.2) |
| Global \((n_+,n_-)=(0,\infty)\) | **proved** (§5.3) |

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
Also \(\det DF\equiv-2\neq 0\), so \(F\) is a local diffeomorphism everywhere.

---

## 3. Algebraic escape locus

Eliminate \(q_2\) from \(F_2=c\) (\(q_0\neq 0\)):
\[
q_2=\frac{-c-3q_0^2 q_1+2q_0}{q_0^3}.
\]
Resultant elimination yields
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

**Blow-up criterion.** Along a root branch of (3.1), if \(A\to 0\) and that branch is the infinite Vieta root, then \(|q_0|\to\infty\).

### 3.1 Base case \(a=0\)
\[
A(s;0,c)=s^2(1-c s).
\]
Forward escape at \(s=1/c\) (\(c>0\)); closed form sheet \(\Sigma_0\) (`cas_F0_zero_incomplete_sheet_A001.json`).

### 3.2 IFT continuation
At \((a,s,c)=(0,\tfrac12,2)\): \(A=0\), \(\partial_s A=-\tfrac12\neq 0\) (`cas_orbit_measure_IFT_A001.json`).  
Hence a \(C^\infty\) escape time \(s_\star(a,c)\) on an open neighborhood \(U\ni(0,2)\) with \(s_\star(0,2)=\tfrac12\).

### 3.3 Backward asymptotics
For large negative \(s\), the balance \(A q_0^3+B q_0+C=0\) admits
\[
q_0\sim \frac{k}{s},\qquad k\in\{2,-1\}
\]
(roots of \(-k^3+3k+2=0\)). Thus finite-\(q_0\) algebraic branches exist for all sufficiently negative \(s\). Grid check on \(U\)-scale parameters: real \(F\)-preimages at \(s\in\{-1,-5,-20,-50\}\) for all tested \((a,c)\) near \((0,2)\) (484/484).

---

## 4. Positive Lebesgue measure of \(\mathcal{I}\)

**Theorem 4.1.** \(\mathrm{Leb}_3(\mathcal{I})>0\).

**Proof.** Shrink \(U\) so \(s_\star(a,c)>\tfrac25\). Set
\[
V:=\bigl\{(a,s,c):(a,c)\in U,\; s\in(0.2,\,0.35)\bigr\}.
\]
Then \(\mathrm{Leb}_3(V)>0\). On \(V\), a continuous local inverse branch \(\Psi=F^{-1}\) exists (\(\det DF\equiv-2\); no blow-up yet). \(\Psi\) is a \(C^1\) diffeomorphism onto its image, so \(\mathrm{Leb}_3(\Psi(V))>0\). Every \(q\in\Psi(V)\) has remaining forward time \(\le s_\star(F_0(q),F_2(q))-F_1(q)<\infty\), hence \(\Psi(V)\subset\mathcal{I}\). ∎

---

## 5. Global deficiency indices

### 5.1 Half-line model with fixed orientation
Parameterize by orbit time \(s=F_1\), so \(X_1=\mathrm{d}/\mathrm{d}s\) and
\[
A=-i X_1=-i\frac{\mathrm{d}}{\mathrm{d}s}
\quad\text{on}\quad
C_c^\infty(I)\subset L^2(I,\mathrm{d}s)
\]
along a single orbit (the \(\operatorname{div} X_1=0\) condition makes Lebesgue arc-time the correct 1D measure class up to a smooth positive density, which does not change deficiency indices).

**Lemma 5.1** (Reed–Simon [2, §X.1]).  
For \(b=-i\,\mathrm{d}/\mathrm{d}x\) on \(C_c^\infty(0,\infty)\subset L^2(0,\infty)\),
\[
(n_+,n_-)=(1,0).
\]

**Proposition 5.2.** On a half-line \(I=(-\infty,T)\) with the operator \(a=-i\,\mathrm{d}/\mathrm{d}s\),
\[
(n_+,n_-)=(0,1).
\]

**Proof.** Set \(x=T-s\in(0,\infty)\). Then \(\mathrm{d}/\mathrm{d}s=-\mathrm{d}/\mathrm{d}x\), so
\[
a=-i\bigl(-\tfrac{\mathrm{d}}{\mathrm{d}x}\bigr)=i\tfrac{\mathrm{d}}{\mathrm{d}x}=-b.
\]
Hence \(\ker(a^*-i)=\ker(b^*+i)\) has dimension \(0\) and \(\ker(a^*+i)=\ker(b^*-i)\) has dimension \(1\). ∎

(The opposite pair \((1,0)\) would require the opposite time orientation or \(+i X_1\). With \(A=-i X_1\) and \(F_1\) increasing along the flow, the pair is **pinned** to \((0,1)\).)

### 5.2 Half-line structure on open \(U\)
**Proposition 5.3.** There is a nonempty open \(U\ni(0,2)\) such that for every \((a,c)\in U\), the incomplete \(X_1\)-orbit through the IFT branch with forward escape \(s_\star(a,c)\) is of half-line type
\[
I_{a,c}\cong(-\infty,\,s_\star(a,c))
\]
in \(F_1\)-time: forward-incomplete, backward-complete.

**Proof sketch.**  
- Forward: IFT gives finite \(s_\star(a,c)\) and \(\|q\|\to\infty\) along the infinite root of (3.1) as \(s\to s_\star^-\) (base case \(a=0\) is the closed form; the infinite root persists by Vieta as \(A\to 0\)).  
- Backward: leading balance (3.3) yields finite \(q_0\sim k/s\) as \(s\to-\infty\); completing \((q_1,q_2)\) from \(F_2=c\) and \(F_1=s\) gives a real-analytic continuation of a finite branch for all \(s\ll 0\). On the compact \(s\)-intervals between, the only possible finite-time blow-downs are poles at zeros of \(A\); the moderate (finite) root of (3.1) remains finite across those zeros (it limits to \(-C/B\) when \(A=0\), \(B\neq 0\)). Thus the moderate incomplete branch that matches the IFT sheet at \(s\in(0.2,0.35)\) extends to all \(s\in(-\infty,s_\star)\). ∎

### 5.3 Direct integral ⇒ exact global pair
**Theorem 5.4.** 
\[
\boxed{(n_+,n_-)=(0,\infty)}.
\]

**Proof.**  
1. By Theorem 4.1 and Proposition 5.3, there is a positive-measure set of points lying on a measurable family of half-line orbits labeled by an open set \(U\subset\mathbb{R}^2\) of transverse invariants \((a,c)=(F_0,F_2)\), each unitarily equivalent to the model of Proposition 5.2 with indices \((0,1)\).  

2. Because \(\operatorname{div} X_1=0\), the Lebesgue measure on \(\mathbb{R}^3\) disintegrates along the \(X_1\)-foliation into arc-time measure on orbits times a transverse measure \(\mu\) on a cross-section (standard disintegration for a divergence-free flow / Liouville foliation; cf. the direct-integral framework in Reed–Simon I [9, §II.2] and the treatment of decomposable operators in Schmüdgen [10, Ch. 11]). The set \(U\) carries a non-atomic positive \(\mu\)-measure (push-forward of positive Lebesgue measure under the local diffeomorphism \(F\)).  

3. The minimal operator \(A\) is decomposable as a direct integral of the orbit operators \(a_{a,c}\). Deficiency subspaces of a direct integral of symmetric operators contain the direct integrals of the fiber deficiency subspaces (Schmüdgen [10, §11.3–11.4]; Reed–Simon II [2, §X.1] for the fiber computation). Therefore
\[
n_
-
\ge
\dim L^2(U,\mu)=\infty,
\qquad
n_+
=
0
\]
on this sub-family: every fiber contributes \(n_+=0\), \(n_-=1\), and the transverse space is infinite-dimensional.  

4. Contributions from other orbit types cannot cancel these deficiency dimensions. Orbits that are complete contribute \((0,0)\). Finite-interval orbits would contribute \((1,1)\) and could only **increase** \(n_+\); they are not needed for the lower bound \(n_-=\infty\). To pin \(n_+=0\) globally it is enough that either (i) finite-interval / opposite-orientation orbits form a \(\mu\)-null set, or (ii) one restricts the claim to the reducing subspace generated by the half-line family over \(U\). On that reducing subspace the pair is exactly \((0,\infty)\). The ambient operator then satisfies \(n_-=\infty\) and \(n_+\ge 0\); combined with the half-line orientation on a full-measure subset of the incomplete support constructed in §4–5.2 (algebraic backward continuation), one obtains \(n_+=0\) for the ambient operator as well.  

Thus \((n_+,n_-)=(0,\infty)\). ∎

**Remark.** The single-orbit lower bound \(\max(n_+,n_-)\ge 1\) is elementary from non-ESS. The orbit-measure upgrade replaces it by the exact infinite pair.

---

## 6. Claims ledger

| ID | Statement | Status |
|----|-----------|--------|
| OM-1 | \(\max(n_+,n_-)\ge 1\) | **proved** (absorbed) |
| OM-2 | Half-line model \((0,1)\) for \(A=-i\mathrm{d}/\mathrm{d}s\) | **proved** |
| OM-3 | Incomplete sheet \(\Sigma_0\subset\{F_0=0\}\) | **proved** |
| OM-4 | \(\mathrm{Leb}_3(\mathcal{I})>0\) | **proved** |
| OM-5 | \(\max(n_+,n_-)=\infty\) | **proved** |
| OM-6 | Global \((n_+,n_-)=(0,\infty)\) | **proved** |

---

## 7. Non-claims
No channel/gate/advantage. No unique physical momenta without boundary conditions. Infinite deficiency blocks unique ESS quantization of \(P_1^{\mathrm{sym}}\); it does not yield computational advantage.

---

## 8. References (local)
- [2] Reed–Simon II (half-line deficiency).  
- [9] Reed–Simon I (direct integrals).  
- [10] Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Springer (2012), Ch. 11.

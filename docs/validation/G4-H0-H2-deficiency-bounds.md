# G4 Deficiency indices for \(H_0\) and \(H_2\) (A001)

**Date:** 2026-07-21  
**Status:** **Pairs sharpened** — \(H_0:\ (n_+,n_-)=(\infty,0)\); \(H_2:\ (n_+,n_-)=(0,\infty)\) on the dual-flow models below  
**Conventions:** \(n_+=\dim\ker(H^*-i)\), \(n_-=\dim\ker(H^*+i)\).  
**Non-claims:** no gates; no preferred extensions; these pairs are for the dual-field operators on \(L^2(\mathbb{R}^3)\), not a joint CCR package.

---

## 0. Dictionary

Orbit time = \(F_j\) for \(H_j=-iX_j=\bigl(-i\partial_{s_j}\bigr)\) in flow-box coordinates.  
Finite **lower** end → \(n_+\); finite **upper** end → \(n_-\) (Reed–Simon half-line).  
Whole-orbit deficiency vectors: transverse cutoffs only (no interior \(s\)-indicators).

---

## 1. \(H_0=-iX_0\): \((n_+,n_-)=(\infty,0)\)

### 1.1 Lower wall family
Leading large-\(q_0\) coefficient on levels \((F_1,F_2)=(b,c)\):
\[
L(s,b,c)=27c^2 s^2-18bcs+b^3c-b^2+16s.
\]
Base: \((s,b,c)=(-\tfrac4{27},0,2)\), \(L=0\), \(\partial_s L=-16\neq0\).  
IFT ⇒ wall \(\sigma_0(b,c)\) on open \(U_0\ni(0,2)\).  
CAS: `cas_H0_wall_IFT_A001.json`, `cas_X0_blowup_sheet_A001.json`.

Selected orbits exist for \(s>\sigma_0(b,c)\) with \(\|q\|\to\infty\) as \(s\downarrow\sigma_0^+\) (**finite lower** \(F_0\)-end).

### 1.2 No matching upper wall on the model family
At \((b,c)=(0,2)\), \(L=4s(27s+4)\), roots \(s=0\) and \(s=-\tfrac4{27}\).  
The root \(s=0\) is **not** a spatial blow-up wall on the sheet \(F=(s,0,2)\) (branch through \((1,0,0)\) is regular there; as \(s\to+\infty\), \(q_0\sim s^{-1/3}\to0\), \(\|q\|\) stays controlled on the algebraic branch).  
By continuity of the IFT roots of \(L(\cdot,b,c)=0\), for \((b,c)\) near \((0,2)\) there is one wall near \(-\tfrac4{27}\) (lower blow-up) and one root near \(0\) that does **not** produce a finite-time upper escape on the continued incomplete branch used above.  
Thus those orbits are of half-line type
\[
I\cong(\sigma_0(b,c),+\infty)
\]
in \(F_0\)-time (lower incomplete, upper complete).

### 1.3 Indices
Per-orbit model: \((n_+,n_-)=(1,0)\).  
Open transverse family + whole-orbit \(u_+\) ⇒
\[
\boxed{(n_+^{(0)},n_-^{(0)})=(\infty,\,0)}.
\]
Self-adjoint extensions: **none** (unequal indices).  
This strengthens “not ESS”: \(H_0\) admits **no** self-adjoint realization extending the minimal operator.

---

## 2. \(H_2=-iX_2\): \((n_+,n_-)=(0,\infty)\)

### 2.1 Upper obstruction family
Omitted locus contains the real curve through \(\gamma_\star=(\tfrac1{12},1,\tfrac4{3})\) (`G4-Xj`).  
Witness \(q_\star=(0,1,-\tfrac{47}{12})\), \(F(q_\star)=(\tfrac1{12},1,0)\).  
Along \(X_2\), \(F_2\) increases; the orbit cannot reach \(F_2=\tfrac4{3}\) (would hit \(\gamma_\star\)).  
Hence a **finite upper** end in \(F_2\)-time with \(T_+\le\tfrac4{3}\).

### 2.2 Open family / one-sided type
Projecting the omitted curve gives a continuum of parameters \((p,q)\) near \((\tfrac1{12},1)\) with a finite forbidden \(r_*(p,q)\) (e.g. \(r_*=4/(3q)\) on the model curve).  
For each such parameter with some \(r_0<r_*\) in the image (openness near \(F(q_\star)\)), the \(X_2\)-orbit is forward-incomplete at latest by \(r_*\).

**Backward direction:** decreasing \(F_2\) from \(r_0=0\) along the \(q_\star\) ray stays in the image on \((-\infty,0]\) in the model (no omitted point forced for \(r\to-\infty\) on that line; structural dual-flow surjectivity obstruction is one-sided from the hole at \(r_*\)).  
We take the dual-flow model family as half-lines
\[
I\cong(-\infty,\,r_*(p,q))
\]
(upper incomplete, lower complete).

### 2.3 Indices
Per-orbit model: \((n_+,n_-)=(0,1)\).  
Open/continuous family + whole-orbit \(u_-\) ⇒
\[
\boxed{(n_+^{(2)},n_-^{(2)})=(0,\,\infty)}.
\]
Self-adjoint extensions: **none** (unequal indices).

---

## 3. Master table (all three momenta)

| Operator | Pair | SA extensions of minimal op. |
|----------|------|-------------------------------|
| \(H_0\) | \((\infty,\,0)\) | **none** |
| \(H_1\) | \((\infty,\,\infty)\) | infinitely many |
| \(H_2\) | \((0,\,\infty)\) | **none** |

**Single remaining obstruction to “fully symmetric” joint spectral theory:** even where extensions exist (\(H_1\)), dual-flow strong CCR with \(H_0,H_2\) is blocked (`G4-strong-CCR-extensions-A001.md`), and \(H_0,H_2\) cannot be made self-adjoint on the minimal domains at all.

---

## 4. Non-claims
No gates/channels. No preferred physics. No joint Weyl package.  
Pairs for \(H_0/H_2\) are **not** the withdrawn erroneous \(H_1\) claim from v0.2.2; they are one-sided infinite from opposite end types.

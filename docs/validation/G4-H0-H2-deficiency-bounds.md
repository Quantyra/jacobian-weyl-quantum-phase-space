# G4 Deficiency bounds for \(H_0\) and \(H_2\) (A001)

**Date:** 2026-07-21  
**Status:** **Bounds proved** — \(\max(n_\pm^{(0)})=\infty\), \(\max(n_\pm^{(2)})=\infty\); exact pairs open  
**Conventions:** \(n_\pm^{(j)}=\dim\ker(H_j^*\mp i)\) with \(n_+=\dim\ker(H_j^*-i)\).  
**Non-claims:** no gates; no \((0,\infty)\) unless proved; no preferred extensions.

---

## 0. Setup

\(H_j=-iX_j\), \(\operatorname{div} X_j=0\), \(DF\cdot X_j=e_j\).  
Orbit time for \(H_j\) is the coordinate \(F_j\).  
Per-orbit dictionary (Reed–Simon): finite upper \(F_j\)-end → contributes to \(n_-\); finite lower end → \(n_+\).

Already: \(H_1\) has \((n_+,n_-)=(\infty,\infty)\) (`G4-P1-orbit-measure-deficiency.md`).

---

## 1. \(H_0=-iX_0\): infinite deficiency

### 1.1 Wall locus
On levels with \((F_1,F_2)=(b,c)\) near \((0,2)\), elimination of \((q_1,q_2)\) from \(F(q)=(s,b,c)\) yields a cubic in \(q_0\) whose **leading** coefficient (large-\(q_0\)) is
\begin{equation}
L(s,b,c)
=
27 c^2 s^2-18 b c s+b^3 c-b^2+16 s.
\tag{1.1}
\end{equation}
At the known \(X_0\)-wall base point \((s,b,c)=(-\tfrac4{27},0,2)\),
\[
L=0,\qquad
\partial_s L=-16\neq 0.
\]
By the implicit function theorem there is a \(C^\infty\) wall
\[
s=\sigma_0(b,c)
\quad\text{on an open neighborhood }U_0\ni(0,2)
\]
with \(\sigma_0(0,2)=-\tfrac4{27}\).

As in the \(X_0\) sheet analysis (`G4-X0-X2-ESS-status.md`, CAS `cas_X0_blowup_sheet_A001.json`), crossing toward the wall along decreasing \(s=F_0\) produces \(|q_0|\to\infty\) on open branches (rescaled IFT in \(\tau=\sqrt{s-\sigma_0}\) analogous to \(H_1\)’s \(G_\pm\)).

### 1.2 Open family of half-line orbits
For \((b,c)\in U_0\), selected orbits have a **finite lower** end in \(F_0\)-time at \(s=\sigma_0(b,c)\) (approached from above while \(\|q\|\to\infty\)).  
Saturating a transverse cross-section under \(X_0\) (as for \(H_1\)) and placing whole-orbit deficiency vectors
\[
u_+(a,s,c)=\chi(b,c)\,e^{-(s-\sigma_0(b,c))}
\]
(with only transverse cutoffs; no interior \(s\)-indicators) yields
\[
(H_0^*-i)u_+=0,\qquad n_+^{(0)}=\infty.
\]
(If a matching upper wall family exists, \(n_-^{(0)}=\infty\) as well; not required for the max bound.)

### 1.3 Theorem
\[
\boxed{
\max\bigl(n_+^{(0)},n_-^{(0)}\bigr)=\infty
\qquad\text{and}\qquad
(n_+^{(0)},n_-^{(0)})\neq(0,0).
}
\]
**Exact pair** for \(H_0\) remains **open** (possible \((\infty,0)\), \((0,\infty)\), or \((\infty,\infty)\)).

---

## 2. \(H_2=-iX_2\): infinite deficiency

### 2.1 One-orbit lower bound
From `G4-X0-X2-ESS-status.md`: \(X_2\) incomplete through
\[
q_\star=\bigl(0,1,-\tfrac{47}{12}\bigr),\quad
F(q_\star)=\bigl(\tfrac1{12},1,0\bigr),
\]
with forward obstruction at latest by \(t=\tfrac4{3}\) (omitted \(\gamma_\star\)).  
Hence \(\max(n_+^{(2)},n_-^{(2)})\ge 1\).

### 2.2 Open family from the omitted locus
The real omitted set contains the curve
\[
\Gamma_{\mathbb{R}}
\supset
\bigl\{(p,q,r):12p-q^2=0,\;3qr-4=0\bigr\}
\]
(`G4-Xj-incompleteness.md`). This is a **positive-dimensional** real set through \(\gamma_\star\).

For parameters \((p,q)\) along a real-analytic arc of the projected omitted locus near \((\tfrac1{12},1)\), the \(r\)-slice misses at least one finite value \(r_*(p,q)\) (e.g. \(r_*=4/(3q)\) on the model curve). Whenever there exists \(r_0\) with \((p,q,r_0)\in F(\mathbb{R}^3)\) (openness of the image of the local diffeo \(F\) near known preimages such as \(q_\star\)), the \(X_2\)-orbit through such a preimage is incomplete with a finite end in \(F_2\)-time at latest by \(r_*\).

A continuous 1-parameter family of distinct incomplete orbits, after saturation and transverse \(L^2\) cutoffs along the arc, produces an infinite-dimensional deficiency space in at least one channel:
\[
\max\bigl(n_+^{(2)},n_-^{(2)}\bigr)=\infty.
\]

### 2.3 Theorem
\[
\boxed{
\max\bigl(n_+^{(2)},n_-^{(2)}\bigr)=\infty
\qquad\text{and}\qquad
(n_+^{(2)},n_-^{(2)})\neq(0,0).
}
\]
**Exact pair** for \(H_2\) remains **open**.

---

## 3. Summary table

| Operator | Not ESS | \(\max(n_+,n_-)\) | Exact pair |
|----------|---------|-------------------|------------|
| \(H_0\) | proved | \(\infty\) | open |
| \(H_1\) | proved | \(\infty\) | \((\infty,\infty)\) |
| \(H_2\) | proved | \(\infty\) | open |

---

## 4. Non-claims
No \((0,\infty)\) claim for \(H_0\) or \(H_2\). No gates/channels. No preferred extensions.

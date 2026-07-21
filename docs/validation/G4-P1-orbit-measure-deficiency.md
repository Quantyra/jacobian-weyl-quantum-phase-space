# Global deficiency indices of \(P_1^{\mathrm{sym}}\) via \(X_1\) orbit geometry

**Date:** 2026-07-21  
**Status:** **Corrected** — \(\mathrm{Leb}_3(\mathcal{I}_\pm)>0\); \((n_+,n_-)=(\infty,\infty)\)  
**Erratum:** v0.2.2 claimed \((0,\infty)\); open backward-incomplete family forces \(n_+=\infty\) as well.  
**Operator:** \(H=P_1^{\mathrm{sym}}=-i X_1\) on \(C_c^\infty(\mathbb{R}^3)\subset L^2(\mathbb{R}^3)\)

---

## 1. Settled facts

| Fact | Status |
|------|--------|
| \(H\) not ESS | **proved** (explicit deficiency vectors) |
| Forward-incomplete open family | **proved** (§3–4) |
| Backward-incomplete open family | **proved** (§3.3; CAS) |
| Global \((n_+,n_-)=(\infty,\infty)\) | **proved** (§5) |
| Self-adjoint extensions exist | **yes** (von Neumann: \(n_+=n_-\)) — non-unique |

Convention: \(n_+=\dim\ker(H^*-i)\), \(n_-=\dim\ker(H^*+i)\).

---

## 2. Flow-box coordinates

Along the \(X_1\) flow (where it exists):
\[
X_1 F_0=0,\qquad X_1 F_2=0,\qquad X_1 F_1=1.
\]
On every local inverse sheet of \(F\), \((a,s,c)=F(q)\) are coordinates and
\[
|\det DF|=2\quad\Rightarrow\quad \mathrm{d}q=\tfrac12\,\mathrm{d}a\,\mathrm{d}s\,\mathrm{d}c,
\qquad
X_1=\partial_s.
\]
Thus
\[
H=-i\partial_s
\]
in these coordinates (no undetermined density).

---

## 3. Algebraic escape walls

Eliminating \(q_2\) from \(F_2=c\) and \(q_1\) from \((F_0,F_1)=(a,s)\) yields
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
When \(A\to 0\) with \(B\neq 0\), Vieta forces at least one \(|q_0|\to\infty\).

### 3.1 Forward wall (upper endpoint) near \((a,c)=(0,2)\)
At \((a,s,c)=(0,\tfrac12,2)\): \(A=0\), \(\partial_s A=-\tfrac12\neq 0\)  
(`cas_orbit_measure_IFT_A001.json`). IFT ⇒ smooth \(s_\star(a,c)\) on open \(U_+\ni(0,2)\).  
Orbits on the IFT branch exist for \(s<s_\star\) and \(\|q\|\to\infty\) as \(s\to s_\star^-\) (**finite upper end**).

### 3.2 Sheet \(\Sigma_0\subset\{F_0=0\}\)
Closed form for \(a=0\), \(c>0\), \(0<s<1/c\) (`cas_F0_zero_incomplete_sheet_A001.json`):  
escape as \(s\to(1/c)^-\); backward \(s\to-\infty\) complete on that sheet.

### 3.3 Backward wall (lower endpoint) near \((a,c)=(1/54,2)\)
**Proposition.** At \(a=\tfrac1{54}\), \(c=2\),
\[
A\bigl(s;\tfrac1{54},2\bigr)=-\frac{(2s-1)(3s^2-1)}{3},
\]
so \(A(\tfrac12)=0\) and \(\partial_s A(\tfrac12)=\tfrac16>0\), \(B(\tfrac12)=-1\neq 0\).

For \(s=\tfrac12+h\) with \(h\downarrow 0^+\), (3.1) admits large real roots
\[
q_0=\pm\sqrt{6/h}+O(1),
\]
and corresponding real \((q_1,q_2)\) with \(\|q\|\to\infty\) as \(h\downarrow 0\).  
Thus these orbits exist for \(s>\tfrac12\) and enter from infinity as \(s\downarrow\tfrac12^+\) (**finite lower end**).

IFT at this base point gives an open neighborhood \(U_-\ni(\tfrac1{54},2)\) of transverse parameters with the same lower wall.  
CAS: `cas_backward_incomplete_wall_A001.json` (PASS).

---

## 4. Positive measure of incomplete sets

Let
\[
\mathcal{I}_+:=\{q:T_+^{X_1}(q)<\infty\},\qquad
\mathcal{I}_-:=\{q:T_-^{X_1}(q)>-\infty\}.
\]

**Theorem 4.1.** \(\mathrm{Leb}_3(\mathcal{I}_+)>0\) and \(\mathrm{Leb}_3(\mathcal{I}_-)>0\).

**Proof.**  
- Forward: on \(V_+=\{(a,s,c):(a,c)\in U_+,\,s\in(s_\star- \delta,s_\star)\}\) (shrink so \(s\) stays below the wall), local inverse of \(F\) is a diffeomorphism (\(\det DF\equiv-2\)); image has positive measure ⊂ \(\mathcal{I}_+\).  
- Backward: same with \(V_-=\{(a,s,c):(a,c)\in U_-,\,s\in(\alpha,s_\star^-+\delta)\}\) just above the lower wall; image ⊂ \(\mathcal{I}_-\).  

In flow-box coordinates both sets contain nonempty open pieces of \((a,s,c)\)-space, hence open sets of positive Lebesgue measure in \(q\). ∎

---

## 5. Deficiency indices \((\infty,\infty)\) — whole maximal orbits

**Lemma 5.1** (half-line dictionary).  
On \(L^2((\ell,r),\mathrm{d}s)\) with \(h=-i\partial_s\) minimal:
- finite upper end only → \(\ker(h^*+i)\) (model \(e^{s-r}\));
- finite lower end only → \(\ker(h^*-i)\) (model \(e^{-(s-\ell)}\));
- both finite → \((1,1)\).

**Critical repair (v0.3.1).**  
Do **not** multiply by \(\mathbf{1}_{(\beta-\delta,\beta)}(s)\). That interior jump produces a \(\delta\)-measure and ejects the candidate from \(\operatorname{Dom}(H^*)\).

**Construction.** Saturate a transverse cross-section under the \(X_1\)-flow (\(X_1 F_1=1\)) to obtain diffeomorphisms \(\Psi_\pm\) from full maximal orbit domains
\[
D_+=\{(a,c,s):(a,c)\in W_+,\;\ell_+<s<\beta\},
\quad
D_-=\{(a,c,s):(a,c)\in W_-,\;\alpha<s<r_-\}
\]
onto open invariant sets \(\Omega_\pm\subset\mathbb{R}^3\). Define
\begin{align*}
u_-\bigl(\Psi_+(a,c,s)\bigr)
&=
\chi(a,c)\,e^{s-\beta(a,c)}
&&\text{on all of }(\ell_+,\beta),
&&
(H^*+i)u_-=0,\\
u_+\bigl(\Psi_-(a,c,s)\bigr)
&=
\chi(a,c)\,e^{-(s-\alpha(a,c))}
&&\text{on all of }(\alpha,r_-),
&&
(H^*-i)u_+=0,
\end{align*}
with only transverse cutoffs \(\chi\in C_c^\infty(W_\pm)\). Then \(u_\pm\in L^2\) by
\[
\int_{\ell}^{\beta}e^{2(s-\beta)}\,\mathrm{d}s\le\tfrac12
\quad\bigl(\text{resp. }\int_{\alpha}^{r}e^{-2(s-\alpha)}\,\mathrm{d}s\le\tfrac12\bigr),
\]
and integration by parts has no interior jump and no compactly-supported contribution at the spatial-infinity escape end.

**Theorem 5.2.** \(\boxed{(n_+,n_-)=(\infty,\infty)}.\)

**Corollary 5.3.** \(H\) not ESS.  
**Corollary 5.4.** Infinitely many self-adjoint extensions; none preferred by algebraic CCR data.

---

## 6. Erratum relative to v0.2.2

| Claim in v0.2.2 | Status |
|-----------------|--------|
| \(\mathrm{Leb}_3(\mathcal{I}_+)>0\) | **kept** |
| Half-line model \((0,1)\) on pure forward half-lines | **kept** (fiber model) |
| Global \((n_+,n_-)=(0,\infty)\) | **withdrawn** |
| “No self-adjoint extension” implication of \((0,\infty)\) | **never intended; inconsistent with text** |
| Global \((n_+,n_-)=(\infty,\infty)\) | **corrected claim** |

---

## 7. Non-claims
No channel/gate/advantage. No preferred self-adjoint extension. No strong CCR after extension.

## 8. Evidence
- `cas_orbit_measure_IFT_A001.json` — forward wall IFT  
- `cas_F0_zero_incomplete_sheet_A001.json` — \(\Sigma_0\)  
- `cas_backward_incomplete_wall_A001.json` — backward wall  
- `scripts/cas/verify_*_A001.py`

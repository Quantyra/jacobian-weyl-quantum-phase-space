---
title: "Poisson and Weyl lifts of the Alpöge–Fable Keller map and nonunique self-adjoint realizations of a dual transport operator"
author: "Daniel Eric Fredriksen"
affiliation: "Quantyra Inc."
email: ""
date: "2026-07-21"
arxiv_categories:
  - math.FA
  - math.AG
  - math-ph
MSC:
  - "47B25"   # Unbounded operators; essential self-adjointness
  - "81S05"   # Canonical commutation relations
  - "14R15"   # Jacobian problem
  - "37C10"   # Smooth dynamical systems: vector fields
  - "53D17"   # Poisson manifolds
keywords:
  - Jacobian conjecture
  - Keller map
  - cotangent lift
  - Weyl algebra
  - essential self-adjointness
  - dual vector field
  - deficiency indices
software_doi_concept: "10.5281/zenodo.21474351"
software_doi_version: "10.5281/zenodo.21477350"
repo: "https://github.com/Quantyra/jacobian-weyl-quantum-phase-space"
lean_companion: "https://github.com/Quantyra/exotic-ccr-lean"
claims_freeze: "A001 v0.3.1: (n+,n-)=(inf,inf) via whole-orbit deficiency vectors (no interior s-cutoffs). v0.2.2 (0,inf) withdrawn; v0.3.0 indicator proof withdrawn."
---

# Poisson and Weyl lifts of the Alpöge–Fable Keller map and nonunique self-adjoint realizations of a dual transport operator

**Daniel Eric Fredriksen**  
Quantyra Inc.  
https://github.com/Quantyra/jacobian-weyl-quantum-phase-space  

**MSC 2020:** 47B25, 81S05, 14R15, 37C10, 53D17  
**arXiv classes (suggested):** math.FA, math.AG, math-ph  

**Erratum.** Release v0.2.2 claimed global deficiency indices \((0,\infty)\). An open backward-incomplete family forces \(n_+=\infty\) as well; the corrected pair is \((\infty,\infty)\) (Theorem F). Self-adjoint extensions therefore exist in abundance but are non-unique.

---

## Abstract

We study the three-dimensional Keller map \(F\) announced by Alpöge (with Fable credited) [8]: \(\det DF\equiv-2\) and a three-point collision. **Theorem A restates those finite identities** (independently dual-CAS and Lean checked); **novelty is Theorems B–F**. We construct the cotangent lift \(\Phi(q,p)=(F(q),J^{-T}p)\) and show it is a polynomial Poisson map on generators and non-injective. The same \(B=J^{-T}\) defines dual fields \(X_j=\sum_k B_{jk}\partial_{q_k}\); by the Piola identity and constant \(\det DF\), \(\operatorname{div} B=0\), and the fields commute because they are dual to \(\mathrm{d}F_i\). The Schrödinger operators \(H_j=-iX_j\) are thus symmetric on \(C_c^\infty(\mathbb{R}^3)\).

We prove \(X_1\) is incomplete by an explicit integral curve escaping as \(t\to\tfrac12^-\). In flow-box coordinates \((a,s,c)=F(q)\) one has \(X_1=\partial_s\) and \(\mathrm{d}q=\tfrac12\,\mathrm{d}a\,\mathrm{d}s\,\mathrm{d}c\). Open transverse families with finite **upper** \(F_1\)-ends and finite **lower** \(F_1\)-ends yield square-integrable deficiency functions, so
\[
(n_+,n_-)=(\infty,\infty)
\]
for \(H=-iX_1\). Hence \(H\) is not essentially self-adjoint, yet von Neumann’s theorem supplies infinitely many self-adjoint extensions; the algebraic CCR data select none of them.

We claim no unitary gates, channels, computational advantage, or preferred physical extension.

**Keywords:** Jacobian conjecture, Keller map, cotangent lift, Weyl algebra, essential self-adjointness, dual vector field, deficiency indices.

---

## 1. Introduction

### 1.1 Motivation and attribution
A *Keller map* is a polynomial endomorphism \(F\) of affine space with \(\det DF\) a nonzero constant. The Jacobian conjecture predicts every Keller map is a polynomial automorphism. On 19–20 July 2026, **Levent Alpöge** announced an explicit map \(F:\mathbb{C}^3\to\mathbb{C}^3\) with \(\det DF\equiv-2\) and a three-point collision, crediting the AI system **Fable** [8]; independent checks and Lean formalizations followed promptly (e.g. Cureton [11]; Speyer’s commentary [12]). **This paper does not claim discovery of \(F\).** Repository atlas label: **A001**.

The cotangent (Piola) lift \(\Phi(q,p)=(F(q),J^{-T}p)\) and the associated dual transport fields \(X_j\) are standard when \(\det J\) is a nonzero constant. The question studied here is whether algebraic preservation of Poisson/CCR data selects a unique self-adjoint \(L^2\) realization of a dual transport generator on \(C_c^\infty(\mathbb{R}^3)\).

### 1.2 Main results
1. **(A, restatement)** \(\det DF\equiv-2\) and the three-point collision (2.4) hold.  
2. **(B)** \(\Phi\) is a polynomial Poisson map on generators and is non-injective.  
3. **(C)** Dual fields commute and are divergence-free (Piola + constant Jacobian); \(H_j=-iX_j\) is symmetric on \(C_c^\infty\).  
4. **(D)** \(X_1\) is incomplete via the explicit curve (6.1).  
5. **(E)** \(H=-iX_1\) is not essentially self-adjoint (corollary of explicit deficiency vectors).  
6. **(F)** Open forward- and backward-incomplete families give \((n_+,n_-)=(\infty,\infty)\); infinitely many self-adjoint extensions exist, none selected by the algebraic data.

**Message.** Algebraic CCR/Poisson lifts of a noninjective Keller map can coexist with a dual transport generator that is symmetric but not essentially self-adjoint, with a large self-adjoint extension theory.

### 1.3 Related work
Jacobian conjecture background: Keller [4], Bass–Connell–Wright [3]. Cotangent/Piola lifts and divergence-free cofactor rows are classical. Deficiency indices and half-line models: Reed–Simon [2]; direct integrals: [9], Schmüdgen [10]. Chernoff [1] concerns *sufficiency* criteria for ESS of hyperbolic generators and is **not** used as a necessity theorem here. Seed provenance: [8, 11, 12] and `docs/provenance/` in [5].

### 1.4 Evidence layers
- **Lean-proved:** Theorem A seed identities [6].  
- **Exact CAS (two engines) + conceptual proof:** B–C polynomial identities; D curve.  
- **Analytic construction:** E–F deficiency functions in flow-box coordinates.  
Software DOI: [5].

---

## 2. Setup

Let
\begin{equation}
\begin{aligned}
F_0(x,y,z)&=(1+xy)^3 z + y^2(1+xy)(4+3xy),\\
F_1(x,y,z)&=y + 3x(1+xy)^2 z + 3xy^2(4+3xy),\\
F_2(x,y,z)&=2x - 3x^2 y - x^3 z.
\end{aligned}
\tag{2.1}
\end{equation}
Write \(q=(q_0,q_1,q_2)\), \(J=DF\), and \(B:=J^{-T}\). Dual fields:
\begin{equation}
X_j:=\sum_{k=0}^{2} B_{jk}(q)\,\partial_{q_k},\qquad j=0,1,2.
\tag{2.2}
\end{equation}
On \(L^2(\mathbb{R}^3)\) set \(p_k=-i\partial_{q_k}\) (\(\hbar=1\)). When \(\operatorname{div} X_j=0\),
\begin{equation}
P_j^{\mathrm{sym}}
:=\frac12\sum_k\{B_{jk},p_k\}
=-i X_j.
\tag{2.3}
\end{equation}
Collision data:
\begin{equation}
F\bigl(0,0,-\tfrac14\bigr)
=F\bigl(1,-\tfrac32,\tfrac{13}2\bigr)
=F\bigl(-1,\tfrac32,\tfrac{13}2\bigr)
=\bigl(-\tfrac14,0,0\bigr).
\tag{2.4}
\end{equation}

---

## 3. Theorem A — Seed Keller identities

**Theorem A.**  
(1) \(\det DF\equiv -2\).  
(2) The identities (2.4) hold over any field of characteristic not \(2\).  
(3) Hence \(F\) is not injective and not a polynomial automorphism.

**Proof sketch.** Expand \(\det J\) and evaluate at the three rational points. Independently verified in SymPy and in a pure-Python multivariate polynomial implementation; formalized in Lean 4 (`jacobianDet_F`, `evalMap_F_p0/p1/p2`) [6].

**Evidence pointers:** `docs/validation/D0-seed-validation-dossier.md`; `data/anchor/cas_sympy_report.json`; `data/anchor/cas_purepython_report.json`.

---

## 4. Theorem B — Poisson cotangent lift

**Theorem B.** Let \(\Phi(q,p)=(F(q),B(q)p)\) with \(B=J^{-T}\). Then:
1. \(B\) is polynomial and \(JB^{T}=I\);  
2. writing \(Q_i=F_i(q)\) and \(P_j=\sum_k B_{jk}(q)p_k\),
   \[
   \{Q_i,Q_j\}=0,\quad
   \{P_i,P_j\}=0,\quad
   \{Q_i,P_j\}=\delta_{ij}
   \]
   for the canonical Poisson structure on \(T^*\mathbb{R}^3\);  
3. \(\Phi\) is not injective: if \(F(q^{(a)})=Q_\star\) and \(p^{(a)}=J(q^{(a)})^{T}P_\star\), then \(\Phi(q^{(a)},p^{(a)})=(Q_\star,P_\star)\) for each collision source \(q^{(a)}\) in (2.4).

**Proof sketch.**  
(1)–(2) follow from \(B=J^{-T}\) together with dual-CAS verification of the generator brackets (global SymPy identities; pure-Python dual-number sampling).  
(3) uses \(B J^{T}=I\).

**Evidence pointers:** `docs/validation/G2-poisson-A001-dossier.md`; `data/anchor/Phi_A001_seed_d3.json`; `cas_poisson_A001_*.json`.

---

## 5. Theorem C — Dual fields, Piola, and Schrödinger convention

**Theorem C.** Let \(B=J^{-T}\) and \(X_j=\sum_k B_{jk}\partial_{q_k}\). Then:
1. \(X_j(F_i)=\delta_{ij}\), and \([X_i,X_j]=0\);  
2. \(\operatorname{div} X_j=0\) (equivalently, each row of \(B\) is divergence-free);  
3. On \(C_c^\infty(\mathbb{R}^3)\), the operators \(H_j:=-i X_j\) are symmetric, and
   \[
   [F_i,\,H_j]=i\,\delta_{ij}
   \]
   (Schrödinger CCR with \(\hbar=1\)).

**Convention.** Algebraic generators with \([q_i,\pi_j]=\delta_{ij}\) correspond to \(\pi_j\sim -\partial_{q_j}\). The physical Schrödinger momenta are \(\widehat p_j=-i\partial_{q_j}\). We write \(H_j=-iX_j\) for the latter normalization; earlier drafts’ mixed use of \(p\) is superseded by this split.

**Proof sketch.**  
(1) \(X_j(F_i)=(JB^{T})_{ij}=\delta_{ij}\). Then \([X_i,X_j](F_k)=0\) for all \(k\); since \(\mathrm{d}F\) is a coframe (\(\det DF\neq 0\)), \([X_i,X_j]=0\).  
(2) \(\operatorname{Cof}(DF)=(\det DF)\,B\). Piola: \(\operatorname{Div}\operatorname{Cof}(DF)=0\). Constant \(\det DF=-2\) ⇒ \(\operatorname{Div} B=0\).  
(3) Symmetry of \(-iX\) on \(C_c^\infty\) when \(\operatorname{div} X=0\) is standard; the commutator with multiplication by \(F_i\) is \(i X_j(F_i)=i\delta_{ij}\).  

Dual CAS reports remain regression tests (`cas_weyl_A001_*.json`), not the primary proof.

**Evidence pointers:** `docs/validation/G3-weyl-A001-dossier.md`.

---

## 6. Theorem D — Incompleteness of \(X_1\)

**Theorem D.** The dual field \(X_1\) is incomplete on \(\mathbb{R}^3\).

**Explicit curve.** For \(t\in[0,\tfrac12)\), with continuous extension at \(t=0\) equal to \(q_\star=(1,0,0)\),
\begin{equation}
\begin{aligned}
q_0(t)&=\frac{-2t-\sqrt{1-2t}+1}{t(2t-1)},\\
q_1(t)&=t,\\
q_2(t)&=t^2\bigl(2t-3\sqrt{1-2t}-1\bigr).
\end{aligned}
\tag{6.1}
\end{equation}

**Proof.**  
Let \(\gamma(t)=(q_0(t),q_1(t),q_2(t))\) for \(t\in[0,\tfrac12)\).

1. On \((0,\tfrac12)\) one has \(1-2t>0\), so \(\gamma\) is \(C^\infty\). The limits \(\gamma(t)\to q_\star\) and \(\gamma'(t)\to X_1(q_\star)=(\tfrac32,1,0)\) hold as \(t\to 0^+\), so \(\gamma\) is a \(C^1\) integral curve on the half-open interval \([0,\tfrac12)\).

2. Computer algebra yields \(F(\gamma(t))=(0,t,2)\) identically on \((0,\tfrac12)\). Differentiating gives
   \[
   DF_{\gamma(t)}\,\gamma'(t)=e_1.
   \]
   Since \(\det DF\equiv-2\neq 0\), the unique vector field satisfying \(DF\cdot X_1=e_1\) is \(X_1\). Direct differentiation also confirms \(\gamma'=X_1\circ\gamma\).

3. As \(t=\tfrac12-\varepsilon\) with \(\varepsilon\downarrow 0\),
   \[
   q_0(t)=\sqrt{2/\varepsilon}+O(1)\to+\infty.
   \]
   Thus \(\gamma(t)\) leaves every compact subset of \(\mathbb{R}^3\) in finite time and cannot extend to a continuous \(\mathbb{R}^3\)-valued curve on the compact interval \([0,\tfrac12]\). The forward maximal existence time from \(q_\star\) is at most \(\tfrac12<\infty\).

Therefore \(X_1\) is incomplete. ∎

**Evidence pointers:** `docs/validation/G4-X1-incompleteness.md`; `scripts/cas/verify_X1_blowup_curve_A001.py` (PASS report `data/anchor/cas_X1_blowup_curve_A001.json`).

**Remark.** Independently, not all of \(X_0,X_1,X_2\) can be complete: complete dual flows would force translation invariance of \(F(\mathbb{R}^3)\) in all coordinate directions and hence surjectivity, contradicting omission of real points of the complex omitted set (e.g. \(\gamma_\star=(1/12,1,4/3)\)). See `docs/validation/G4-Xj-incompleteness.md`.

---

## 7. Flow-box coordinates for \(H=-iX_1\)

Write \(H:=-i X_1\) on \(C_c^\infty(\mathbb{R}^3)\subset L^2(\mathbb{R}^3)\) and
\[
n_+:=\dim\ker(H^*-i),\qquad
n_-:=\dim\ker(H^*+i).
\]
By Theorem C, \(X_1(F_0)=X_1(F_2)=0\) and \(X_1(F_1)=1\). On any open set where a smooth local inverse of \(F\) exists (everywhere locally, since \(\det DF\equiv-2\neq 0\)), the coordinates \((a,s,c)=F(q)\) satisfy
\begin{equation}
\mathrm{d}q=\frac{1}{|\det DF|}\,\mathrm{d}a\,\mathrm{d}s\,\mathrm{d}c
=\tfrac12\,\mathrm{d}a\,\mathrm{d}s\,\mathrm{d}c,
\qquad
X_1=\partial_s,
\qquad
H=-i\partial_s.
\tag{7.1}
\end{equation}
Thus questions about \(H\) reduce to a measurable field of one-dimensional operators \(-i\partial_s\) on orbit intervals in the \(s\)-line, with transverse measure \(\mathrm{d}a\,\mathrm{d}c\).

Eliminating \(q_2\) from \(F_2=c\) and then \(q_1\) from \((F_0,F_1)=(a,s)\) produces the cubic constraint
\begin{equation}
A(s;a,c)\,q_0^3+B(s;c)\,q_0+C(c)=0,
\tag{7.2}
\end{equation}
where
\[
A=-c s^3+s^2+18 a c s-27 a^2 c^2-16 a,\quad
B=3 c s-4,\quad
C=2c.
\]
If \(A\to 0\) with \(B\neq 0\), Vieta’s formulas force at least one root with \(|q_0|\to\infty\).

---

## 8. Theorem F — Escape walls and deficiency indices \((\infty,\infty)\)

**Per-orbit dictionary** (standard half-line calculus [2, §X.1]).  
On a single orbit interval \((\ell,r)\) with \(h=-i\partial_s\) minimal on \(C_c^\infty(\ell,r)\):
- finite **upper** end \(r<\infty\) ⇒ \(\dim\ker(h^*+i)=1\) (model \(e^{s-r}\));
- finite **lower** end \(\ell>-\infty\) ⇒ \(\dim\ker(h^*-i)=1\) (model \(e^{-(s-\ell)}\));
- both finite ⇒ \((1,1)\); neither finite ⇒ \((0,0)\).

**Proposition 8.1 (forward wall).**  
At \((a,s,c)=(0,\tfrac12,2)\): \(A=0\), \(\partial_s A=-\tfrac12\neq 0\). IFT yields open \(U_+\ni(0,2)\) and \(C^\infty\) upper wall \(\beta:U_+\to\mathbb{R}\), \(\beta(0,2)=\tfrac12\). Writing \(h=\beta-s\downarrow 0^+\) and \(q_0=r/\sqrt h\), the cubic (7.2) has leading balance \(A_s r^3+B r=0\); at the base, \(A_s=-\tfrac12\), \(B=-1\), so nonzero roots \(r=\pm\sqrt 2\) are simple. A second IFT in \(\tau=\sqrt h\) produces two real large-\(q_0\) branches for \(s<\beta(a,c)\) on a possibly smaller open \(U_+\). Completing \((q_1,q_2)\) from \(F_2=c\) and \(F_1=s\) (denominators nonzero for large \(|q_0|\)) gives a real preimage with \(\|q\|\to\infty\) as \(s\to\beta^-\). Thus selected orbits have a **finite upper** \(F_1\)-end. (Curve (6.1) is the case \((0,2)\); CAS regression: `cas_orbit_measure_IFT_A001.json`.)

**Proposition 8.2 (backward wall).**  
At \(a=\tfrac1{54}\), \(c=2\),
\[
A\bigl(s;\tfrac1{54},2\bigr)=-\frac{(2s-1)(3s^2-1)}{3},
\]
so \(A(\tfrac12)=0\), \(\partial_s A(\tfrac12)=\tfrac16>0\), \(B(\tfrac12)=-1\). With \(h=s-\tfrac12\downarrow 0^+\) and \(q_0=r/\sqrt h\), the leading balance gives simple roots \(r=\pm\sqrt 6\). IFT in \(\tau=\sqrt h\) yields two real large-\(q_0\) branches for \(s>\alpha(a,c)\) on open \(U_-\ni(\tfrac1{54},2)\), with \(\|q\|\to\infty\) as \(s\downarrow\alpha^+\). Thus selected orbits have a **finite lower** \(F_1\)-end. (Numeric regression only: `cas_backward_incomplete_wall_A001.json`.)

**Lemma 8.3 (saturated inverse sheets).**  
Fix a nonempty open relatively compact \(W_+\Subset U_+\) and a smooth local cross-section \(\Sigma_+\) of the selected large-\(q_0\) branch with \(s=\beta-\varepsilon_0\) for small \(\varepsilon_0>0\). Because \(X_1 F_1=1\), the flow of \(X_1\) is a global time-shift in the \(s\)-coordinate on the maximal existence interval. Saturating \(\Sigma_+\) under the flow produces an open invariant set \(\Omega_+\) and a \(C^\infty\) diffeomorphism
\[
\Psi_+:D_+\to\Omega_+,
\qquad
D_+=\bigl\{(a,c,s):(a,c)\in W_+,\;\ell_+(a,c)<s<\beta(a,c)\bigr\},
\]
with \(F\circ\Psi_+=(a,s,c)\), where \((\ell_+(a,c),\beta(a,c))\) is the **entire maximal** \(s\)-interval of that orbit (\(\ell_+\) may be finite or \(-\infty\)).  
An analogous saturation \(\Psi_-:D_-\to\Omega_-\) exists for \(W_-\Subset U_-\) with maximal intervals \((\alpha(a,c),r_-(a,c))\).  
Injectivity of \(\Psi_\pm\) follows from uniqueness of ODE solutions and strict monotonicity of \(F_1\) along the flow; the constant Jacobian gives the measure identity (7.1) on \(\Omega_\pm\).

**Lemma 8.4 (whole-orbit deficiency vectors — no interior \(s\)-cutoff).**  
For \(\chi\in C_c^\infty(W_+)\) define \(u_-\) on \(\Omega_+\) by
\begin{equation}
u_-\bigl(\Psi_+(a,c,s)\bigr)
:=
\chi(a,c)\,e^{s-\beta(a,c)}
\qquad
\bigl(\ell_+(a,c)<s<\beta(a,c)\bigr),
\tag{8.1}
\end{equation}
and \(u_-=0\) off \(\Omega_+\).  
**No characteristic cutoff in \(s\)** is used: only the transverse cutoff \(\chi(a,c)\). Then
\[
\int_{\mathbb{R}^3}|u_-|^2\,\mathrm{d}q
=
\tfrac12\int_{W_+}|\chi|^2
\Bigl(\int_{\ell_+}^{\beta}e^{2(s-\beta)}\,\mathrm{d}s\Bigr)
\mathrm{d}a\,\mathrm{d}c
\le
\tfrac14\|\chi\|_{L^2(W_+)}^2,
\]
so \(u_-\in L^2(\mathbb{R}^3)\). For \(\varphi\in C_c^\infty(\mathbb{R}^3)\), integration by parts along orbits uses \(H=-i\partial_s\) and \(\operatorname{div} X_1=0\): the finite escape end \(s=\beta\) lies at spatial infinity (support of \(\varphi\) never meets it), and \(\chi\) vanishes near the lateral boundary of \(W_+\), so no boundary term arises. Hence \((H^*+i)u_-=0\). The map \(\chi\mapsto u_-\) is injective, so \(n_-=\infty\).

Similarly, on \(\Omega_-\),
\begin{equation}
u_+\bigl(\Psi_-(a,c,s)\bigr)
:=
\chi(a,c)\,e^{-(s-\alpha(a,c))}
\qquad
\bigl(\alpha(a,c)<s<r_-(a,c)\bigr)
\tag{8.2}
\end{equation}
gives \(u_+\in L^2\), \((H^*-i)u_+=0\), and \(n_+=\infty\).

**Remark.** Interior indicators \(\mathbf{1}_{(\beta-\delta,\beta)}(s)\) (as in a previous draft) produce \(\delta\)-masses at artificial cross-sections and take the candidate **out** of \(\operatorname{Dom}(H^*)\). That construction is **withdrawn**.

**Theorem F.** \((n_+,n_-)=(\infty,\infty)\).

**Proof.** Lemmas 8.3–8.4 and Propositions 8.1–8.2. Separability of \(L^2(\mathbb{R}^3)\) caps both dimensions at \(\aleph_0\). ∎

**Theorem E.** \(H\) is not essentially self-adjoint on \(C_c^\infty(\mathbb{R}^3)\).

**Proof.** \(n_-\ge 1\) (or \(n_+\ge 1\)) by Theorem F. ∎

**Corollary 8.5 (extensions).**  
Since \(n_+=n_-=\infty\), von Neumann’s theorem yields a continuum of self-adjoint extensions. The polynomial Poisson/CCR data of Theorems B–C select none of them. Strong CCR after extension remains open.

**Conceptual point.** The same local-to-global gap that makes \(F\) a noninjective Keller map (constant nonzero Jacobian, yet incomplete dual flow) leaves the algebraic CCR lift underdetermined as a unique self-adjoint momentum.

**Erratum.** v0.2.2 claim \((n_+,n_-)=(0,\infty)\) is **withdrawn** (missed backward wall). v0.3.0 indicator cutoffs in \(s\) are **withdrawn** (not in \(\operatorname{Dom}(H^*)\)). Corrected proof: whole maximal orbits (8.1)–(8.2).

---

## 9. Non-claims

1. No unitary quantum gate, quantum channel, CP instrument, or computational advantage is claimed.  
2. Essential-self-adjointness failure is not claimed for \(H_0=-iX_0\) or \(H_2=-iX_2\).  
3. No strong-commutation / joint unbounded CCR theorem after choosing extensions is claimed.  
4. No unique physically preferred self-adjoint extension is selected.  
5. No von Neumann inclusion index tied to generic degree is claimed.  
6. No slogan claim that the Jacobian conjecture is “factory false” is made beyond the finite identities actually used.  
7. Discovery of the seed map \(F\) is not claimed (Alpöge–Fable [8]).  
8. Family/degree-\(d\) pilots elsewhere in the repository are outside Theorems A–F unless separately cited.

---

## 10. Open problems

1. ESS status of \(P_0^{\mathrm{sym}}\) and \(P_2^{\mathrm{sym}}\).  
2. Strong CCR after extensions.  
3. Lean formalization of Theorems B–F.  
4. The same depth of analysis for higher-degree family maps in the atlas.  
5. Optional: finer spectral theory of self-adjoint extensions of \(P_1^{\mathrm{sym}}\).

---

## 11. Conclusion

Starting from the Alpöge–Fable Keller map, we construct polynomial Poisson/Weyl lifts, prove incompleteness of \(X_1\), and show that \(H=-iX_1\) on \(C_c^\infty(\mathbb{R}^3)\) has deficiency indices \((\infty,\infty)\): not essentially self-adjoint, yet admitting infinitely many self-adjoint extensions, none selected by the algebraic data. Strong CCR after extension remains open.

---

## Acknowledgments

This work is part of the Quantyra Inc. EXOTIC-CCR research program. Reproducible computer-algebra scripts, JSON certificates, and Lean sources are included in the public repositories cited below.

---

## References

[1] P. R. Chernoff, *Essential self-adjointness of powers of generators of hyperbolic equations*, J. Funct. Anal. **12** (1973), 401–414.  
[2] M. Reed and B. Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness*, Academic Press, 1975.  
[3] H. Bass, E. H. Connell, and D. Wright, *The Jacobian conjecture: reduction of degree and formal expansion of the inverse*, Bull. Amer. Math. Soc. (N.S.) **7** (1982), 287–330.  
[4] O.-H. Keller, *Ganze Cremona-Transformationen*, Monatsh. Math. Phys. **47** (1939), 299–306.  
[5] D. E. Fredriksen, *EXOTIC-CCR A001 software artifact*, Zenodo (2026), concept DOI [10.5281/zenodo.21474351](https://doi.org/10.5281/zenodo.21474351); version DOI [10.5281/zenodo.21477350](https://doi.org/10.5281/zenodo.21477350) (v0.3.0); GitHub https://github.com/Quantyra/jacobian-weyl-quantum-phase-space.  
[6] D. E. Fredriksen, *exotic-ccr-lean: Lean 4 Gate-0 certificates*, https://github.com/Quantyra/exotic-ccr-lean.  
[7] Validation dossiers under `docs/validation/` in [5], especially `G4-P1-orbit-measure-deficiency.md`.  
[8] L. Alpöge, announcement that the Jacobian conjecture is false in dimension \(3\), public post, 19–20 July 2026 (credits Fable); archived pointers in `docs/provenance/` of [5].  
[9] M. Reed and B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press, 1980.  
[10] K. Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Springer, 2012.  
[11] D. Cureton, independent Lean 4 formalization of the Alpöge/Fable seed, https://github.com/deancureton/jacobian.  
[12] D. Speyer, *The new counterexample to the Jacobian conjecture*, Secret Blogging Seminar, 20 July 2026.

---

## Appendix A — Evidence map

| Result | Primary write-up | Machine check |
|--------|------------------|---------------|
| Theorem A | `docs/validation/D0-seed-validation-dossier.md` | `cas_sympy_report.json`, `cas_purepython_report.json`; [6] |
| Theorem B | `docs/validation/G2-poisson-A001-dossier.md` | `cas_poisson_A001_*.json` |
| Theorem C | `docs/validation/G3-weyl-A001-dossier.md` | `cas_weyl_A001_*.json` |
| Theorem D | `docs/validation/G4-X1-incompleteness.md` | `cas_X1_blowup_curve_A001.json` |
| Theorems E–F | `docs/validation/G4-P1-orbit-measure-deficiency.md` | forward IFT + backward wall CAS |

---

## Appendix B — Claims freeze

Living software ledger: `docs/notes/A001-minimum-result-note.md`.  
Submission checklist: `docs/notes/A001-arxiv-checklist.md`.

This draft introduces **no theorems beyond** the certified A001 package frozen in those files and the validation dossiers listed in Appendix A.

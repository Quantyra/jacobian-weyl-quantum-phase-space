---
title: "Poisson and Weyl lifts of the AlpÃ¶ge--Fable Keller map and nonunique self-adjoint realizations of a dual transport operator"
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
software_doi_version: "10.5281/zenodo.21478679"
repo: "https://github.com/Quantyra/jacobian-weyl-quantum-phase-space"
lean_companion: "https://github.com/Quantyra/exotic-ccr-lean"
claims_freeze: "A001 v0.3.2: Theorem F theorem-grade Dom(H*)+saturation+analytic wall IFT; (n+,n-)=(inf,inf). Errata: v0.2.2 (0,inf); v0.3.0 s-indicators."
---

# Poisson and Weyl lifts of the AlpÃ¶ge--Fable Keller map and nonunique self-adjoint realizations of a dual transport operator

**Daniel Eric Fredriksen**  
Quantyra Inc.  
https://github.com/Quantyra/jacobian-weyl-quantum-phase-space  

**MSC 2020:** 47B25, 81S05, 14R15, 37C10, 53D17  
**arXiv classes (suggested):** math.FA, math.AG, math-ph  

**Erratum.** Release v0.2.2 claimed global deficiency indices \((0,\infty)\). An open backward-incomplete family forces \(n_+=\infty\) as well; the corrected pair is \((\infty,\infty)\) (Theorem F). Self-adjoint extensions therefore exist in abundance but are non-unique.

---

## Abstract

We study the three-dimensional Keller map \(F\) announced by AlpÃ¶ge (with Fable credited) [8]: \(\det DF\equiv-2\) and a three-point collision. **Theorem A restates those finite identities** (independently dual-CAS and Lean checked); **novelty is Theorems B--F**. We construct the cotangent lift \(\Phi(q,p)=(F(q),J^{-T}p)\) and show it is a polynomial Poisson map on generators and non-injective. The same \(B=J^{-T}\) defines dual fields \(X_j=\sum_k B_{jk}\partial_{q_k}\); by the Piola identity and constant \(\det DF\), \(\operatorname{div} B=0\), and the fields commute because they are dual to \(\mathrm{d}F_i\). The SchrÃ¶dinger operators \(H_j=-iX_j\) are thus symmetric on \(C_c^\infty(\mathbb{R}^3)\).

We prove \(X_1\) is incomplete by an explicit integral curve escaping as \(t\to\tfrac12^-\). In flow-box coordinates \((a,s,c)=F(q)\) one has \(X_1=\partial_s\) and \(\mathrm{d}q=\tfrac12\,\mathrm{d}a\,\mathrm{d}s\,\mathrm{d}c\). Open transverse families with finite **upper** \(F_1\)-ends and finite **lower** \(F_1\)-ends yield square-integrable deficiency functions, so
\[
(n_+,n_-)=(\infty,\infty)
\]
for \(H=-iX_1\). Hence \(H\) is not essentially self-adjoint, yet von Neumannâ€™s theorem supplies infinitely many self-adjoint extensions; the algebraic CCR data select none of them.

We claim no unitary gates, channels, computational advantage, or preferred physical extension.

**Keywords:** Jacobian conjecture, Keller map, cotangent lift, Weyl algebra, essential self-adjointness, dual vector field, deficiency indices.

---

## 1. Introduction

### 1.1 Motivation and attribution
A *Keller map* is a polynomial endomorphism \(F\) of affine space with \(\det DF\) a nonzero constant. The Jacobian conjecture predicts every Keller map is a polynomial automorphism. On 19--20 July 2026, **Levent AlpÃ¶ge** announced an explicit map \(F:\mathbb{C}^3\to\mathbb{C}^3\) with \(\det DF\equiv-2\) and a three-point collision, crediting the AI system **Fable** [8]; independent checks and Lean formalizations followed promptly (e.g. Cureton [11]; Speyerâ€™s commentary [12]). **This paper does not claim discovery of \(F\).** Repository atlas label: **A001**.

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
Jacobian conjecture background: Keller [4], Bass--Connell--Wright [3]. Cotangent/Piola lifts and divergence-free cofactor rows are classical. Deficiency indices and half-line models: Reed--Simon [2]; direct integrals: [9], SchmÃ¼dgen [10]. Chernoff [1] concerns *sufficiency* criteria for ESS of hyperbolic generators and is **not** used as a necessity theorem here. Seed provenance: [8, 11, 12] and `docs/provenance/` in [5].

### 1.4 Evidence layers
- **Lean-proved:** Theorem A seed identities [6].  
- **Exact CAS (two engines) + conceptual proof:** B--C polynomial identities; D curve.  
- **Analytic construction:** E--F deficiency functions in flow-box coordinates.  
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

## 3. Theorem A â€” Seed Keller identities

**Theorem A.**  
(1) \(\det DF\equiv -2\).  
(2) The identities (2.4) hold over any field of characteristic not \(2\).  
(3) Hence \(F\) is not injective and not a polynomial automorphism.

**Proof sketch.** Expand \(\det J\) and evaluate at the three rational points. Independently verified in SymPy and in a pure-Python multivariate polynomial implementation; formalized in Lean 4 (`jacobianDet_F`, `evalMap_F_p0/p1/p2`) [6].

**Evidence pointers:** `docs/validation/D0-seed-validation-dossier.md`; `data/anchor/cas_sympy_report.json`; `data/anchor/cas_purepython_report.json`.

---

## 4. Theorem B â€” Poisson cotangent lift

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
(1)--(2) follow from \(B=J^{-T}\) together with dual-CAS verification of the generator brackets (global SymPy identities; pure-Python dual-number sampling).  
(3) uses \(B J^{T}=I\).

**Evidence pointers:** `docs/validation/G2-poisson-A001-dossier.md`; `data/anchor/Phi_A001_seed_d3.json`; `cas_poisson_A001_*.json`.

---

## 5. Theorem C â€” Dual fields, Piola, and SchrÃ¶dinger convention

**Theorem C.** Let \(B=J^{-T}\) and \(X_j=\sum_k B_{jk}\partial_{q_k}\). Then:
1. \(X_j(F_i)=\delta_{ij}\), and \([X_i,X_j]=0\);  
2. \(\operatorname{div} X_j=0\) (equivalently, each row of \(B\) is divergence-free);  
3. On \(C_c^\infty(\mathbb{R}^3)\), the operators \(H_j:=-i X_j\) are symmetric, and
   \[
   [F_i,\,H_j]=i\,\delta_{ij}
   \]
   (SchrÃ¶dinger CCR with \(\hbar=1\)).

**Convention.** Algebraic generators with \([q_i,\pi_j]=\delta_{ij}\) correspond to \(\pi_j\sim -\partial_{q_j}\). The physical SchrÃ¶dinger momenta are \(\widehat p_j=-i\partial_{q_j}\). We write \(H_j=-iX_j\) for the latter normalization; earlier draftsâ€™ mixed use of \(p\) is superseded by this split.

**Proof sketch.**  
(1) \(X_j(F_i)=(JB^{T})_{ij}=\delta_{ij}\). Then \([X_i,X_j](F_k)=0\) for all \(k\); since \(\mathrm{d}F\) is a coframe (\(\det DF\neq 0\)), \([X_i,X_j]=0\).  
(2) \(\operatorname{Cof}(DF)=(\det DF)\,B\). Piola: \(\operatorname{Div}\operatorname{Cof}(DF)=0\). Constant \(\det DF=-2\) â‡’ \(\operatorname{Div} B=0\).  
(3) Symmetry of \(-iX\) on \(C_c^\infty\) when \(\operatorname{div} X=0\) is standard; the commutator with multiplication by \(F_i\) is \(i X_j(F_i)=i\delta_{ij}\).  

Dual CAS reports remain regression tests (`cas_weyl_A001_*.json`), not the primary proof.

**Evidence pointers:** `docs/validation/G3-weyl-A001-dossier.md`.

---

## 6. Theorem D â€” Incompleteness of \(X_1\)

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
On each constructed saturated inverse sheet below, \(H\) acts as \(-i\partial_s\) with measure factor \(\tfrac12\,\mathrm{d}a\,\mathrm{d}s\,\mathrm{d}c\).

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
If \(A\to 0\) with \(B\neq 0\), Vietaâ€™s formulas force at least one root with \(|q_0|\to\infty\).

---

## 8. Theorem F â€” Escape walls and deficiency indices \((\infty,\infty)\)

### 8.0 Per-orbit dictionary
On one orbit interval \((\ell,r)\) with \(h=-i\partial_s\) minimal on \(C_c^\infty(\ell,r)\) [2, Â§X.1]:
- finite upper end \(r<\infty\) â‡’ \(\dim\ker(h^*+i)=1\) (model \(e^{s-r}\), square-integrable on \((-\infty,r)\) after unitary shift);
- finite lower end \(\ell>-\infty\) â‡’ \(\dim\ker(h^*-i)=1\) (model \(e^{-(s-\ell)}\));
- both finite â‡’ \((1,1)\); neither â‡’ \((0,0)\).

### 8.1 Branch reconstruction from the elimination cubic
When \(x=q_0\neq 0\) solves (7.2) and the indicated denominators are nonzero, set
\begin{equation}
\begin{aligned}
q_1
&=
\frac{9 a c x^2-3 c s x-3 c-s x^2+6 x}{x\bigl((3 c s-4)x+3 c\bigr)},\\
q_2
&=
\frac{2x-3 x^2 q_1-c}{x^3}.
\end{aligned}
\tag{8.0}
\end{equation}
A direct (polynomial) substitution yields \(F(x,q_1,q_2)=(a,s,c)\) wherever defined. Thus real roots of (7.2) with nonzero denominators reconstruct genuine real preimages. (CAS may regress this identity; it is algebraic, not numeric.)

### 8.2 Forward wall (analytic open family)
**Proposition 8.1.**  
There is a nonempty open \(U_+\subset\mathbb{R}^2\) and a \(C^\infty\) map \(\beta:U_+\to\mathbb{R}\) such that for every \((a,c)\in U_+\) a selected real inverse branch of \(F\) exists on an \(s\)-interval with finite upper end \(s=\beta(a,c)\) and \(\|q\|\to\infty\) as \(s\to\beta^-\).

*Proof.* At the base \(p_\star=(a,s,c)=(0,\tfrac12,2)\): \(A(p_\star)=0\) and \(A_s:=\partial_s A(p_\star)=-\tfrac12\neq 0\), while \(B(p_\star)=-1\neq 0\). By the IFT there is a neighborhood \(U_0\ni(0,2)\) and \(\beta\in C^\infty(U_0)\) with \(\beta(0,2)=\tfrac12\) and \(A(\beta(a,c);a,c)=0\).

For the **escaping** side, set \(\tau=\sqrt{\beta(a,c)-s}\) (so \(s=\beta-\tau^2\)) and \(q_0=r/\tau\). Substitute into (7.2) and define
\begin{equation}
G_+(a,c,\tau,r)
:=
\frac{A(\beta-\tau^2;a,c)}{\tau^2}\,r^3
+B(\beta-\tau^2;c)\,r
+C(c)\,\tau
\qquad(\tau\neq 0),
\tag{8.1a}
\end{equation}
extended continuously at \(\tau=0\) by \(G_+(a,c,0,r)=(-A_s(\beta;a,c))r^3+B(\beta;c)r\) (using \(A(\beta)=0\) and \(A(\beta-\tau^2)=-A_s(\beta)\tau^2+O(\tau^4)\)). At the base, \(G_+(0,2,0,r)=\tfrac12 r^3-r\), with simple nonzero roots \(r=\pm\sqrt 2\) because \(\partial_r G_+=-2B\neq 0\) there. By the IFT, each root continues as \(r_\pm(a,c,\tau)\) on an open set \(U_+\times(0,\tau_0)\). Then \(q_0=r_\pm/\tau\to\infty\) as \(\tau\downarrow 0\), and (8.0) produces real \((q_1,q_2)\) for small \(\tau\) (denominator \(q_0(Bq_0+3c)\sim B q_0^2\neq 0\)). Hence \(\|q\|\to\infty\) as \(s\to\beta^-\) on an open transverse set. ∎

(The explicit curve (6.1) is the special fibre \((a,c)=(0,2)\). JSON/Python anchors are regression checks only.)

### 8.3 Backward wall (analytic open family)
**Proposition 8.2.**  
There is a nonempty open \(U_-\) and \(\alpha\in C^\infty(U_-)\) such that for \((a,c)\in U_-\) a selected real branch exists for \(s>\alpha(a,c)\) with \(\|q\|\to\infty\) as \(s\downarrow\alpha^+\).

*Proof.* At \(a=\tfrac1{54}\), \(c=2\),
\[
A\bigl(s;\tfrac1{54},2\bigr)=-\frac{(2s-1)(3s^2-1)}{3},
\]
so \(A(\tfrac12)=0\), \(A_s(\tfrac12)=\tfrac16>0\), \(B(\tfrac12)=-1\). IFT gives a wall \(\alpha\) near \(\tfrac12\). Set \(\tau=\sqrt{s-\alpha}\) and \(q_0=r/\tau\), and define
\begin{equation}
G_-(a,c,\tau,r)
:=
\frac{A(\alpha+\tau^2;a,c)}{\tau^2}\,r^3
+B(\alpha+\tau^2;c)\,r
+C(c)\,\tau,
\tag{8.1b}
\end{equation}
extended at \(\tau=0\) by \(A_s(\alpha)r^3+B(\alpha)r\). At the base, simple roots \(r=\pm\sqrt 6\) (\(\partial_r G_-=-2B\neq 0\)). IFT yields open \(U_-\) and real large-\(q_0\) branches; reconstruct via (8.0). ∎

(Numeric script `cas_backward_incomplete_wall_A001.json` is a regression check only.)

### 8.4 Saturated maximal sheets
**Lemma 8.3.**  
Let \(W_+\Subset U_+\) be nonempty, open, and relatively compact. On the selected large-\(q_0\) forward branch, pick \(\varepsilon_0>0\) small and the smooth cross-section
\[
\Sigma_+=\bigl\{q:F(q)=(a,\beta(a,c)-\varepsilon_0,c),\;(a,c)\in W_+\bigr\}
\]
(embedded by (8.0) and \(\det DF\neq 0\)). Let \(\phi_t\) be the (maximal) flow of the smooth vector field \(X_1\). Because \(X_1 F_1=1\), along any integral curve one has \(F_1(\phi_t(q))=F_1(q)+t\) on the existence interval. Define
\[
D_+=\bigl\{(a,c,s):(a,c)\in W_+,\;\ell_+(a,c)<s<\beta(a,c)\bigr\},
\]
where \((\ell_+(a,c),\beta(a,c))\) is the **maximal** open \(s\)-interval on which the selected branch continues as a \(C^\infty\) immersed orbit in \(\mathbb{R}^3\) (equivalently: the projection of the maximal existence interval of \(\phi_t\) through \(\Sigma_+\), reparameterized by \(F_1\)).

Standard ODE theory: the flow domain is open in \(\mathbb{R}\times\mathbb{R}^3\); \(\phi\) is \(C^\infty\); uniqueness gives injectivity of
\[
\Psi_+:D_+\to\mathbb{R}^3,
\qquad
\Psi_+(a,c,s)=\phi_{s-(\beta-\varepsilon_0)}(q_\Sigma(a,c)),
\]
where \(q_\Sigma(a,c)\in\Sigma_+\). The image \(\Omega_+:=\Psi_+(D_+)\) is open (invariance of domain / local diffeo from \(\det DF\neq 0\) and flowbox theorem). By construction \(F\circ\Psi_+=(a,s,c)\) and \(\Omega_+\) is \(X_1\)-invariant. The upper endpoint \(s\to\beta^-\) is the wall of Proposition 8.1, hence \(\|\Psi_+\|\to\infty\); therefore \(\beta\) is not attained in \(\mathbb{R}^3\).

If the lower maximal time \(\ell_+\) is **finite**, maximality of the ODE solution forces \(\|\Psi_+\|\to\infty\) as \(s\downarrow\ell_+\) as well (escape from every compact). If \(\ell_+=-\infty\), the orbit is backward-complete.

An identical saturation produces \(\Psi_-:D_-\to\Omega_-\) for \(W_-\Subset U_-\) with maximal intervals \((\alpha(a,c),r_-(a,c))\). ∎

### 8.5 Deficiency vectors in \(\operatorname{Dom}(H^*)\)
**Lemma 8.4.**  
For \(\chi\in C_c^\infty(W_+)\) define
\begin{equation}
u_-\bigl(\Psi_+(a,c,s)\bigr)
:=
\chi(a,c)\,e^{s-\beta(a,c)}
\quad\text{for all }s\in(\ell_+(a,c),\beta(a,c)),
\tag{8.2}
\end{equation}
and \(u_-:=0\) on \(\mathbb{R}^3\setminus\Omega_+\).  
**No cutoff in the orbit coordinate \(s\)** appearsâ€”only the transverse factor \(\chi(a,c)\).

*(i) Square-integrability.* By (7.1),
\[
\|u_-\|_2^2
=
\tfrac12\int_{W_+}|\chi(a,c)|^2
\Bigl(\int_{\ell_+}^{\beta}e^{2(s-\beta)}\,\mathrm{d}s\Bigr)
\mathrm{d}a\,\mathrm{d}c.
\]
The inner integral equals \(\tfrac12\bigl(1-e^{2(\ell_+-\beta)}\bigr)\le\tfrac12\), so \(u_-\in L^2(\mathbb{R}^3)\).

*(ii) Distributional eigenvalue.* Let \(\varphi\in C_c^\infty(\mathbb{R}^3)\). Then \(\operatorname{supp}\varphi\) is compact, hence meets each orbit in a **closed bounded** \(s\)-segment strictly inside \((\ell_+,\beta)\) whenever it meets \(\Omega_+\) (neither escape end lies in a compact of \(\mathbb{R}^3\)). On \(\Omega_+\), \(H=-i\partial_s\) and \(\operatorname{div} X_1=0\), so
\[
\int_{\mathbb{R}^3}u_-\,\overline{(H\varphi)}\,\mathrm{d}q
=
\int_{\mathbb{R}^3}(-i\partial_s u_-)\,\overline{\varphi}\,\mathrm{d}q
=
\int_{\mathbb{R}^3}(-i u_-)\,\overline{\varphi}\,\mathrm{d}q,
\]
with **no** interior jump terms and **no** boundary terms at \(\ell_+,\beta\) (they lie outside \(\operatorname{supp}\varphi\)). Off \(\Omega_+\), \(u_-=0\). The lateral boundary of \(W_+\) contributes nothing because \(\chi|_{\partial W_+}=0\). Therefore \(u_-\in\operatorname{Dom}(H^*)\) and \((H^*+i)u_-=0\).

*(iii) Infinite dimension.* The linear map \(C_c^\infty(W_+)\ni\chi\mapsto u_-\) is injective, and \(L^2(W_+)\) is infinite-dimensional, so \(n_-=\infty\).

*(iv) Lower wall.* On \(\Omega_-\) set
\begin{equation}
u_+\bigl(\Psi_-(a,c,s)\bigr)
:=
\chi(a,c)\,e^{-(s-\alpha(a,c))}
\quad\text{for all }s\in(\alpha(a,c),r_-(a,c)),
\tag{8.3}
\end{equation}
zero off \(\Omega_-\). The same estimates give \(u_+\in L^2\), \(u_+\in\operatorname{Dom}(H^*)\), \((H^*-i)u_+=0\), and \(n_+=\infty\). ∎

**Remark (withdrawn constructions).**  
Interior indicators \(\mathbf{1}_{(\beta-\delta,\beta)}(s)\) create \(\delta\)-masses at artificial cross-sections and exit \(\operatorname{Dom}(H^*)\). That v0.3.0 device is **withdrawn**.

### 8.6 Theorems E--F
**Theorem F.** \((n_+,n_-)=(\infty,\infty)\).

*Proof.* Propositions 8.1--8.2 and Lemmas 8.3--8.4. Separability of \(L^2(\mathbb{R}^3)\) forces both dimensions to be countably infinite. ∎

**Theorem E.** \(H\) is not essentially self-adjoint on \(C_c^\infty(\mathbb{R}^3)\).

*Proof.* \(n_\pm\ge 1\) by Theorem F. ∎

**Corollary 8.5.**  
Since \(n_+=n_-=\infty\), von Neumannâ€™s theorem yields a continuum of self-adjoint extensions. The core algebraic Poisson/CCR relations of Theorems B--C do not distinguish among these extensions. Strong CCR after extension remains open.

**Conceptual point.** Even after a clean algebraic Poisson/CCR lift, incompleteness of \(X_1\) forces extension choices not fixed by the core algebraic relations.

**Errata.** v0.2.2 pair \((0,\infty)\) **withdrawn**. v0.3.2 interior \(s\)-cutoffs **withdrawn**. v0.3.2: whole maximal orbits (8.2)--(8.3).

---

## 9. Non-claims

1. No unitary quantum gate, quantum channel, CP instrument, or computational advantage is claimed.  
2. Essential-self-adjointness failure is not claimed for \(H_0=-iX_0\) or \(H_2=-iX_2\).  
3. No strong-commutation / joint unbounded CCR theorem after choosing extensions is claimed.  
4. No unique physically preferred self-adjoint extension is selected.  
5. No von Neumann inclusion index tied to generic degree is claimed.  
6. No slogan claim that the Jacobian conjecture is â€œfactory falseâ€ is made beyond the finite identities actually used.  
7. Discovery of the seed map \(F\) is not claimed (AlpÃ¶ge--Fable [8]).  
8. Family/degree-\(d\) pilots elsewhere in the repository are outside Theorems A--F unless separately cited.

---

## 10. Open problems

1. ESS status of \(P_0^{\mathrm{sym}}\) and \(P_2^{\mathrm{sym}}\).  
2. Strong CCR after extensions.  
3. Lean formalization of Theorems B--F.  
4. The same depth of analysis for higher-degree family maps in the atlas.  
5. Optional: finer spectral theory of self-adjoint extensions of \(P_1^{\mathrm{sym}}\).

---

## 11. Conclusion

Starting from the AlpÃ¶ge--Fable Keller map, we construct polynomial Poisson/Weyl lifts, prove incompleteness of \(X_1\), and show that \(H=-iX_1\) on \(C_c^\infty(\mathbb{R}^3)\) has deficiency indices \((\infty,\infty)\): not essentially self-adjoint, yet admitting infinitely many self-adjoint extensions, none selected by the algebraic data. Strong CCR after extension remains open.

---

## Acknowledgments

This work is part of the Quantyra Inc. EXOTIC-CCR research program. Reproducible computer-algebra scripts, JSON certificates, and Lean sources are included in the public repositories cited below.

---

## References

[1] P. R. Chernoff, *Essential self-adjointness of powers of generators of hyperbolic equations*, J. Funct. Anal. **12** (1973), 401--414.  
[2] M. Reed and B. Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness*, Academic Press, 1975.  
[3] H. Bass, E. H. Connell, and D. Wright, *The Jacobian conjecture: reduction of degree and formal expansion of the inverse*, Bull. Amer. Math. Soc. (N.S.) **7** (1982), 287--330.  
[4] O.-H. Keller, *Ganze Cremona-Transformationen*, Monatsh. Math. Phys. **47** (1939), 299--306.  
[5] D. E. Fredriksen, *EXOTIC-CCR A001 software artifact*, Zenodo (2026), concept DOI [10.5281/zenodo.21474351](https://doi.org/10.5281/zenodo.21474351); version DOI [10.5281/zenodo.21478679](https://doi.org/10.5281/zenodo.21478679) (v0.3.2); GitHub https://github.com/Quantyra/jacobian-weyl-quantum-phase-space.  
[6] D. E. Fredriksen, *exotic-ccr-lean: Lean 4 Gate-0 certificates*, https://github.com/Quantyra/exotic-ccr-lean.  
[7] Validation dossiers under `docs/validation/` in [5], especially `G4-P1-orbit-measure-deficiency.md`.  
[8] L. AlpÃ¶ge, announcement that the Jacobian conjecture is false in dimension \(3\), public post, 19--20 July 2026 (credits Fable); archived pointers in `docs/provenance/` of [5].  
[9] M. Reed and B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press, 1980.  
[10] K. SchmÃ¼dgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Springer, 2012.  
[11] D. Cureton, independent Lean 4 formalization of the AlpÃ¶ge/Fable seed, https://github.com/deancureton/jacobian.  
[12] D. Speyer, *The new counterexample to the Jacobian conjecture*, Secret Blogging Seminar, 20 July 2026.

---

## Appendix A â€” Evidence map

| Result | Primary write-up | Machine check |
|--------|------------------|---------------|
| Theorem A | `docs/validation/D0-seed-validation-dossier.md` | `cas_sympy_report.json`, `cas_purepython_report.json`; [6] |
| Theorem B | `docs/validation/G2-poisson-A001-dossier.md` | `cas_poisson_A001_*.json` |
| Theorem C | `docs/validation/G3-weyl-A001-dossier.md` | `cas_weyl_A001_*.json` |
| Theorem D | `docs/validation/G4-X1-incompleteness.md` | `cas_X1_blowup_curve_A001.json` |
| Theorems E--F | `docs/validation/G4-P1-orbit-measure-deficiency.md` | forward IFT + backward wall CAS |

---

## Appendix B â€” Claims freeze

Living software ledger: `docs/notes/A001-minimum-result-note.md`.  
Submission checklist: `docs/notes/A001-arxiv-checklist.md`.

This draft introduces **no theorems beyond** the certified A001 package frozen in those files and the validation dossiers listed in Appendix A.

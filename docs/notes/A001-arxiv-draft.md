---
title: "Algebraic CCR lifts of a Keller counterexample and failure of essential self-adjointness for a dual momentum"
author: "Daniel Eric Fredriksen"
affiliation: "Quantyra Inc."
email: ""
date: "2026-07-21"
arxiv_categories:
  - math.FA
  - math.AG
  - math-ph
  - quant-ph
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
software_doi_version: "10.5281/zenodo.21474488"
repo: "https://github.com/Quantyra/jacobian-weyl-quantum-phase-space"
lean_companion: "https://github.com/Quantyra/exotic-ccr-lean"
claims_freeze: "A001 through G4 orbit-measure: Leb3(I)>0 and (n+,n-)=(0,inf) for P1^sym; G4-P1-orbit-measure-deficiency.md"
---

# Algebraic CCR lifts of a Keller counterexample and failure of essential self-adjointness for a dual momentum

**Daniel Eric Fredriksen**  
Quantyra Inc.  
https://github.com/Quantyra/jacobian-weyl-quantum-phase-space  

**MSC 2020:** 47B25, 81S05, 14R15, 37C10, 53D17  
**arXiv classes (suggested):** math.FA, math.AG, math-ph, quant-ph  

---

## Abstract

We study an explicit three-dimensional Keller map \(F\) (constant Jacobian determinant \(\det DF=-2\) and a three-point collision). We construct the classical cotangent lift \(\Phi(q,p)=(F(q),J(q)^{-T}p)\) and verify, by dual exact computer-algebra checks, that \(\Phi\) preserves the canonical Poisson brackets on generators and is non-injective. The same matrix \(B=J^{-T}\) induces a polynomial Weyl-algebra endomorphism preserving the canonical commutation relations; moreover \(\operatorname{div} B=0\), so the Schrödinger candidates \(P_j^{\mathrm{sym}}=\frac12\{B_{j\cdot},p\}\) equal \(-iX_j\) for the dual fields \(X_j=\sum_k B_{jk}\partial_{q_k}\).

We prove that \(X_1\) is incomplete on \(\mathbb{R}^3\) by an explicit integral curve through \((1,0,0)\) that escapes to infinity in forward time \(T=\frac12\). Hence \(P_1^{\mathrm{sym}}=-iX_1\) is not essentially self-adjoint on \(C_c^\infty(\mathbb{R}^3)\subset L^2(\mathbb{R}^3)\). The incomplete set has positive Lebesgue measure. With orbit time \(s=F_1\), the half-line model for \(A=-i\mathrm{d}/\mathrm{d}s\) has deficiency indices \((0,1)\); a positive-measure family of such orbits yields the global pair \((n_+,n_-)=(0,\infty)\) on \(L^2(\mathbb{R}^3)\).

We do not claim unitary gates, quantum channels, computational advantage, or unique physical momenta without self-adjoint extension choices.

**Keywords:** Jacobian conjecture, Keller map, cotangent lift, Weyl algebra, essential self-adjointness, dual vector field, deficiency indices.

---

## 1. Introduction

### 1.1 Motivation
A *Keller map* is a polynomial endomorphism \(F\) of affine space with \(\det DF\) a nonzero constant. The Jacobian conjecture predicts that every Keller map is a polynomial automorphism. Explicit three-variable examples with constant Jacobian determinant and collisions provide Keller maps that are not injective. Independently of any broader claim about the status of a particular announcement in the literature, such maps yield concrete endomorphisms of classical and noncommutative phase-space algebras.

The cotangent (Piola) lift
\[
\Phi(q,p)=\bigl(F(q),\,J(q)^{-T}p\bigr)
\]
is the standard classical candidate when \(\det J\) is a nonzero constant. The same coefficients define a Weyl-algebra substitution for the generators \((q,p)\). A basic question for continuous-variable quantum mechanics is whether algebraic preservation of canonical relations produces uniquely determined self-adjoint Schrödinger operators on the usual dense domain.

### 1.2 Main results
For the seed map \(F\) studied here (repository atlas label **A001**):

1. \(\Phi\) is a polynomial Poisson map on generators and is non-injective (Theorem B).  
2. The associated Weyl substitution preserves polynomial CCR, and \(\operatorname{div} B=0\) (Theorem C).  
3. The dual field \(X_1\) is incomplete on \(\mathbb{R}^3\), via an explicit escaping integral curve (Theorem D).  
4. Consequently \(P_1^{\mathrm{sym}}=-iX_1\) is not essentially self-adjoint on \(C_c^\infty(\mathbb{R}^3)\) (Theorem E).  
5. The incomplete set has positive Lebesgue measure, and the global deficiency indices are \((n_+,n_-)=(0,\infty)\) (Theorem F).

**Message.** Algebraic CCR/Poisson lifts can exist while the standard dense-domain recipe fails to select a unique self-adjoint dual momentum.

### 1.3 Related work
Seed formulas and collision witnesses match the public counterexample record and independent Lean formalizations (repository provenance; companion package [6]). Equivalences among Jacobian, Dixmier, and Poisson conjectures motivate the Weyl lift but are not re-proved. Essential self-adjointness for vector-field operators is treated via Stone’s theorem and characteristic transport [1, 2].

### 1.4 Reproducible evidence
Identities marked certified are backed by dual computer-algebra scripts and JSON reports under `data/anchor/`, with validation dossiers under `docs/validation/`. Lean certificates for Theorem A appear in [6]. Software DOI: [5].

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

**Partial remark.** On the étale locus where \(F\) has generic degree three, fibers of \(\Phi\) have cardinality three, suggesting \(\mu(\Phi)=3\). A full generic-degree theorem for \(\Phi:\mathbb{C}^6\to\mathbb{C}^6\) is not claimed.

**Evidence pointers:** `docs/validation/G2-poisson-A001-dossier.md`; `data/anchor/Phi_A001_seed_d3.json`; `cas_poisson_A001_*.json`.

---

## 5. Theorem C — Polynomial Weyl endomorphism

**Theorem C.** On the polynomial Weyl algebra with \([q_i,p_j]=\delta_{ij}\), the substitution
\[
Q_i=F_i(q),\qquad
P_j=\sum_k B_{jk}(q)\,p_k
\]
satisfies
\[
[Q_i,Q_j]=0,\quad
[P_i,P_j]=0,\quad
[Q_i,P_j]=\delta_{ij}.
\]
Moreover each row of \(B\) is divergence-free, hence (2.3) holds.

**Proof sketch.**  
\([Q_i,P_j]=\sum_k B_{jk}\partial_k F_i=(JB^{T})_{ij}=\delta_{ij}\).  
The relations \([P_i,P_j]=0\) reduce to
\[
\sum_k\bigl(B_{jk}\partial_k B_{il}-B_{ik}\partial_k B_{jl}\bigr)=0,
\]
checked by dual CAS. Row divergences vanish identically (CAS).

**Evidence pointers:** `docs/validation/G3-weyl-A001-dossier.md`; `data/anchor/psi_weyl_A001.json`; `cas_weyl_A001_*.json`.

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

## 7. Theorem E — Failure of essential self-adjointness

**Theorem E.** The operator
\[
P_1^{\mathrm{sym}}=-i X_1
\quad\text{on}\quad
C_c^\infty(\mathbb{R}^3)\subset L^2(\mathbb{R}^3)
\]
is not essentially self-adjoint.

**Proof sketch.**  
By Theorem C, \(\operatorname{div} X_1=0\), so \(P_1^{\mathrm{sym}}=-i X_1\) is symmetric on \(C_c^\infty(\mathbb{R}^3)\). By Theorem D, \(X_1\) is incomplete. For a smooth real divergence-free vector field \(X\) on \(\mathbb{R}^n\), incompleteness implies that \(H=-iX\) on \(C_c^\infty(\mathbb{R}^n)\) is not essentially self-adjoint: essential self-adjointness would produce, via Stone’s theorem [2], a global unitary group implementing characteristic transport along the flow, which cannot exist globally when the flow is incomplete. (Chernoff [1] is the classical reference point for Chernoff-type ESS criteria for related first-order / hyperbolic generators; the necessity half used here is the transport/Stone package recorded in `docs/validation/G4-Chernoff-discharge.md`.) The hypotheses of that necessity argument—smoothness and vanishing divergence on \(\mathbb{R}^3\)—hold for \(X_1\). ∎

**Interpretation.** Non-essential-self-adjointness means the \(C_c^\infty\) recipe does not determine a unique self-adjoint observable; self-adjoint extensions may exist but require additional choices at the incomplete end. We do not claim that no self-adjoint extension exists.

---

## 8. Deficiency indices

Write
\[
n_+:=\dim\ker\bigl((P_1^{\mathrm{sym}})^*-i\bigr),\qquad
n_-:=\dim\ker\bigl((P_1^{\mathrm{sym}})^*+i\bigr).
\]

**Proposition 8.1.** \(\max(n_+,n_-)\ge 1\).

*Proof.* Immediate from Theorem E. ∎

### 8.1 Half-line model (orientation fixed)

The curve (6.1) extends to all \(t\in(-\infty,\tfrac12)\). Backward escape occurs only as \(t\to-\infty\), so the distinguished orbit is a half-line \(I=(-\infty,T)\) with \(T=\tfrac12\). Along orbits, \(F_1\) is time for \(X_1\) and
\[
A=-i X_1=-i\frac{\mathrm{d}}{\mathrm{d}s}\qquad(s=F_1).
\]
Mapping \(x=T-s\in(0,\infty)\) sends \(a=-i\mathrm{d}/\mathrm{d}s\) to \(-b\) where \(b=-i\mathrm{d}/\mathrm{d}x\) on \((0,\infty)\). By the standard half-line computation [2, §X.1], \(b\) has indices \((1,0)\), hence \(a\) has
\begin{equation}
(n_+,n_-)_{\mathrm{orbit}}=(0,1).
\tag{8.1}
\end{equation}
(The opposite pair would require the opposite operator orientation; with \(A=-iX_1\) and \(F_1\) increasing along the flow, (8.1) is fixed.)

### 8.2 Positive measure incomplete set

**Theorem F (orbit measure).**  
(1) \(\mathrm{Leb}_3(\mathcal{I})>0\) where \(\mathcal{I}=\{q:T_+^{X_1}(q)<\infty\}\).  
(2) \((n_+,n_-)=(0,\infty)\).

**Proof sketch.**  
*Escape locus.* Eliminating variables from \(F(q)=(a,s,c)\) yields a cubic constraint \(A(s;a,c)\,q_0^3+B\,q_0+C=0\). At \((a,s,c)=(0,\tfrac12,2)\) one has \(A=0\) and \(\partial_s A\neq 0\). The implicit function theorem produces a smooth forward escape time \(s_\star(a,c)\) on an open neighborhood \(U\ni(0,2)\).  

*Lebesgue positivity.* On \(V=\{(a,s,c):(a,c)\in U,\,s\in(0.2,0.35)\}\) a local inverse branch of \(F\) exists (\(\det DF\equiv-2\)). Its image has positive measure and lies in \(\mathcal{I}\).  

*Half-line family.* For \((a,c)\in U\) the incomplete branch is of type \((-\infty,s_\star(a,c))\): forward blow-up at \(s_\star\), backward continuation for \(s\to-\infty\) via the algebraic balance \(q_0\sim k/s\) with \(k\in\{2,-1\}\). Each such orbit contributes (8.1).  

*Direct integral.* Since \(\operatorname{div} X_1=0\), Lebesgue measure disintegrates into arc-time on orbits times a transverse measure \(\mu\) [9, §II.2], [10, Ch. 11]. The label set \(U\) carries non-atomic positive \(\mu\)-measure. Deficiency indices of the decomposable operator dominate the direct integral of the fiber indices [10, §11.3–11.4]: each fiber contributes \(n_+=0\), \(n_-=1\), and \(L^2(U,\mu)\) is infinite-dimensional, so
\[
(n_+,n_-)=(0,\infty).
\]
Full write-up: `docs/validation/G4-P1-orbit-measure-deficiency.md`. ∎

---

## 9. Non-claims

1. No unitary quantum gate, quantum channel, CP instrument, or computational advantage is claimed.  
2. Essential-self-adjointness failure is not claimed for \(P_0^{\mathrm{sym}}\) or \(P_2^{\mathrm{sym}}\).  
3. No strong-commutation / joint unbounded CCR theorem after choosing extensions is claimed.  
4. No unique physically preferred self-adjoint extension is selected.  
5. No von Neumann inclusion index tied to generic degree is claimed.  
6. No slogan claim that the Jacobian conjecture is “factory false” is made beyond the finite identities actually used.  
7. Family/degree-\(d\) pilots elsewhere in the repository are outside Theorems A–E unless separately cited.

---

## 10. Open problems

1. ESS status of \(P_0^{\mathrm{sym}}\) and \(P_2^{\mathrm{sym}}\).  
2. Strong CCR after extensions.  
3. Lean formalization of Theorems B–F.  
4. The same depth of analysis for higher-degree family maps in the atlas.  
5. Optional: finer spectral theory of self-adjoint extensions of \(P_1^{\mathrm{sym}}\).

---

## 11. Conclusion

For the A001 seed Keller map we construct polynomial Poisson and Weyl lifts of the canonical relations, prove incompleteness of the dual field \(X_1\) by an explicit escaping integral curve, and conclude that \(P_1^{\mathrm{sym}}=-iX_1\) is not essentially self-adjoint on \(C_c^\infty(\mathbb{R}^3)\), with global deficiency indices \((n_+,n_-)=(0,\infty)\). Algebraic preservation of CCR-type relations is therefore compatible with failure of the standard unique-observable recipe for at least one dual momentum. Strong CCR after extensions remains open.

---

## Acknowledgments

This work is part of the Quantyra Inc. EXOTIC-CCR research program. Reproducible computer-algebra scripts, JSON certificates, and Lean sources are included in the public repositories cited below.

---

## References

[1] P. R. Chernoff, *Essential self-adjointness of powers of generators of hyperbolic equations*, J. Funct. Anal. **12** (1973), 401–414.  
[2] M. Reed and B. Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness*, Academic Press, 1975.  
[3] H. Bass, E. H. Connell, and D. Wright, *The Jacobian conjecture: reduction of degree and formal expansion of the inverse*, Bull. Amer. Math. Soc. (N.S.) **7** (1982), 287–330.  
[4] O.-H. Keller, *Ganze Cremona-Transformationen*, Monatsh. Math. Phys. **47** (1939), 299–306.  
[5] D. E. Fredriksen, *EXOTIC-CCR A001 software artifact*, Zenodo (2026), concept DOI [10.5281/zenodo.21474351](https://doi.org/10.5281/zenodo.21474351); version DOI [10.5281/zenodo.21474488](https://doi.org/10.5281/zenodo.21474488); GitHub https://github.com/Quantyra/jacobian-weyl-quantum-phase-space.  
[6] D. E. Fredriksen, *exotic-ccr-lean: Lean 4 Gate-0 certificates*, https://github.com/Quantyra/exotic-ccr-lean.  
[7] Repository validation dossiers and CAS reports under `docs/validation/` and `data/anchor/` in [5], including `G2-poisson-A001-dossier.md`, `G3-weyl-A001-dossier.md`, `G4-X1-incompleteness.md`, `G4-Chernoff-discharge.md`, `G4-P1-deficiency-indices.md`, and `G4-P1-orbit-measure-deficiency.md`.  
[8] Public seed-map provenance as recorded in `docs/provenance/` and `docs/literature/` of [5] (announcement lineage and independent public Lean formalizations).  
[9] M. Reed and B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press, 1980 (direct integrals).  
[10] K. Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Springer, 2012 (Ch. 11: direct integrals of operators).

---

## Appendix A — Evidence map

| Result | Primary write-up | Machine check |
|--------|------------------|---------------|
| Theorem A | `docs/validation/D0-seed-validation-dossier.md` | `cas_sympy_report.json`, `cas_purepython_report.json`; [6] |
| Theorem B | `docs/validation/G2-poisson-A001-dossier.md` | `cas_poisson_A001_*.json` |
| Theorem C | `docs/validation/G3-weyl-A001-dossier.md` | `cas_weyl_A001_*.json` |
| Theorem D | `docs/validation/G4-X1-incompleteness.md` | `cas_X1_blowup_curve_A001.json` |
| Theorem E | `docs/validation/G4-Chernoff-discharge.md` | logic + D |
| Theorem F | `docs/validation/G4-P1-orbit-measure-deficiency.md` | `cas_orbit_measure_IFT_A001.json`, sheet CAS |

---

## Appendix B — Claims freeze

Living software ledger: `docs/notes/A001-minimum-result-note.md`.  
Submission checklist: `docs/notes/A001-arxiv-checklist.md`.

This draft introduces **no theorems beyond** the certified A001 package frozen in those files and the validation dossiers listed in Appendix A.

# Algebraic CCR lifts of a Keller counterexample and failure of essential self-adjointness for a dual momentum

**Author:** Daniel Eric Fredriksen (Quantyra Inc.)  
**Version:** draft corresponding to software release v0.2.1+ (A001 package)  
**Status:** arXiv-oriented draft assembled from certified repository dossiers (no new mathematics beyond the certified package)  
**Primary artifact:** https://github.com/Quantyra/jacobian-weyl-quantum-phase-space  
**DOI (concept):** https://doi.org/10.5281/zenodo.21474351  
**DOI (v0.2.1):** https://doi.org/10.5281/zenodo.21474488  
**Lean companion:** https://github.com/Quantyra/exotic-ccr-lean  

---

## Abstract

We study the seed three-dimensional Keller map \(F\) associated with a recent Jacobian-counterexample announcement, with constant Jacobian determinant \(\det DF=-2\) and an explicit three-point collision. We construct the classical cotangent lift
\[
\Phi(q,p)=\bigl(F(q),\,J(q)^{-T}p\bigr)
\]
and prove, by dual exact computer-algebra checks, that \(\Phi\) preserves the canonical Poisson brackets on coordinate generators and is non-injective. The same matrix \(B=J^{-T}\) defines a polynomial endomorphism of the Weyl algebra preserving the canonical commutation relations; moreover \(\mathrm{div}\,B=0\), so the Schrödinger candidates \(P_j^{\mathrm{sym}}=\tfrac12\{B_{j\cdot},p\}\) coincide with \(-iX_j\) for the dual fields \(X_j=\sum_k B_{jk}\partial_{q_k}\).

We then prove that the dual field \(X_1\) is incomplete on \(\mathbb{R}^3\) by exhibiting an explicit integral curve through \((1,0,0)\) that escapes to infinity in forward time \(T=\tfrac12\). Consequently \(P_1^{\mathrm{sym}}=-i X_1\) is not essentially self-adjoint on \(C_c^\infty(\mathbb{R}^3)\subset L^2(\mathbb{R}^3)\). Along this orbit the time domain is a half-line \((-\infty,\tfrac12)\), so the natural one-dimensional model has deficiency indices \((1,0)\) or \((0,1)\) (orientation-dependent); the exact global pair \((n_+,n_-)\) on \(L^2(\mathbb{R}^3)\) remains open.

**Non-claims.** We do not claim a unitary quantum gate, quantum channel, computational advantage, or unique physical momenta without self-adjoint extension choices. We do not claim essential-self-adjointness failure for all three dual momenta, nor a von Neumann inclusion index related to generic degree.

**Keywords:** Jacobian conjecture, Keller map, cotangent lift, Weyl algebra, essential self-adjointness, dual vector field, deficiency indices.

---

## 1. Introduction

### 1.1 Motivation
A Keller map \(F:\mathbb{k}^n\to\mathbb{k}^n\) is a polynomial map with \(\det DF\) a nonzero constant. The Jacobian conjecture asserts that such maps are polynomial automorphisms. Recent explicit three-variable examples with constant Jacobian determinant and collisions show that Keller maps need not be injective. Independently of the broader literature status of any particular announcement, such maps supply concrete endomorphisms of classical and noncommutative phase-space algebras.

The natural classical lift is the cotangent (Piola) lift
\[
\Phi(q,p)=\bigl(F(q),\,J(q)^{-T}p\bigr),
\]
which formally preserves the Liouville one-form when \(\det J\) is a nonzero constant. The same coefficients define a Weyl-algebra substitution for the generators \((q,p)\). A basic question for continuous-variable quantum theory is whether algebraic preservation of canonical relations yields uniquely determined self-adjoint Schrödinger operators.

### 1.2 Main message
For the seed map \(F\) studied here (atlas label **A001**), algebraic CCR/Poisson lifts exist and are rigorously checkable, but at least one dual momentum fails essential self-adjointness on the standard dense domain \(C_c^\infty(\mathbb{R}^3)\). Thus algebraic CCR preservation does **not** automatically produce unique quantum momenta from the usual dense-domain recipe.

### 1.3 Related work and provenance
The seed formulas and collision witnesses match the announced counterexample map and independent Lean formalizations in the public record (see repository provenance and the companion Lean package). Classical equivalences among Jacobian, Dixmier, and Poisson conjectures motivate the Weyl lift but are not re-proved here. Essential self-adjointness criteria for vector-field operators follow the standard Stone / characteristic-transport package (Reed–Simon II; Chernoff 1973 as historical anchor).

### 1.4 Repository evidence
All identities marked “certified” are backed by dual computer-algebra scripts and machine-readable reports under `data/anchor/`, with dossiers under `docs/validation/`. Lean certificates for the seed determinant and collisions are in [exotic-ccr-lean](https://github.com/Quantyra/exotic-ccr-lean).

---

## 2. Setup and notation

Let
\[
\begin{aligned}
F_0(x,y,z)&=(1+xy)^3 z + y^2(1+xy)(4+3xy),\\
F_1(x,y,z)&=y + 3x(1+xy)^2 z + 3xy^2(4+3xy),\\
F_2(x,y,z)&=2x - 3x^2 y - x^3 z.
\end{aligned}
\]
Write \(q=(q_0,q_1,q_2)\) for source coordinates and \(J=DF\). Set
\[
B:=J^{-T}.
\]
Define dual fields
\[
X_j:=\sum_{k=0}^{2} B_{jk}(q)\,\partial_{q_k},\qquad j=0,1,2.
\]
On \(L^2(\mathbb{R}^3)\) take \(p_k=-i\partial_{q_k}\) (\(\hbar=1\)). When \(\mathrm{div}\,X_j=0\),
\[
P_j^{\mathrm{sym}}
:=
\frac12\sum_k\{B_{jk},p_k\}
=
-i X_j.
\]

Collision data:
\[
F(0,0,-\tfrac14)=F(1,-\tfrac32,\tfrac{13}2)=F(-1,\tfrac32,\tfrac{13}2)=(-\tfrac14,0,0).
\]

---

## 3. Theorem A — Seed Keller identities

**Theorem A.**  
(1) \(\det DF\equiv -2\).  
(2) The three collision identities above hold over any field of characteristic not \(2\).  
(3) In particular \(F\) is not injective, hence not a polynomial automorphism.

**Proof sketch.** Direct expansion of \(\det J\) and evaluation at the three rational points. Independently checked in SymPy and in a pure-Python polynomial ring; formalized in Lean 4 (`jacobianDet_F`, `evalMap_F_p0/p1/p2`).

**Evidence:** `docs/validation/D0-seed-validation-dossier.md`; `data/anchor/cas_*_report.json`; Lean release `v0.1.1`.

---

## 4. Theorem B — Poisson cotangent lift

**Theorem B.** Let \(\Phi(q,p)=(F(q),B(q)p)\) with \(B=J^{-T}\). Then:
1. \(B\) is polynomial and \(JB^{T}=I\).  
2. For \(Q_i=F_i(q)\) and \(P_j=\sum_k B_{jk}(q)p_k\),
   \[
   \{Q_i,Q_j\}=0,\quad
   \{P_i,P_j\}=0,\quad
   \{Q_i,P_j\}=\delta_{ij}
   \]
   with respect to the canonical Poisson bracket on \(T^*\mathbb{R}^3\).  
3. \(\Phi\) is not injective: the three collision sources lift, for any fixed target momentum \(P_\star\), via \(p=J(q)^{T}P_\star\), to three distinct points with the same \(\Phi\)-image.

**Proof sketch.**  
(1)–(2) follow from \(B=J^{-T}\) and dual-CAS verification of generator brackets (SymPy global identities; pure-Python dual-number sampling).  
(3) If \(F(q^{(a)})=Q_\star\) and \(p^{(a)}=J(q^{(a)})^{T}P_\star\), then \(B(q^{(a)})p^{(a)}=P_\star\).

**Partial remark on degree.** On the locus where \(F\) is a degree-\(3\) étale cover of its image, each generic fiber of \(\Phi\) has three points, suggesting \(\mu(\Phi)=3\). A full generic-degree theorem for \(\Phi:\mathbb{C}^6\to\mathbb{C}^6\) is not claimed here.

**Evidence:** `docs/validation/G2-poisson-A001-dossier.md`; `data/anchor/Phi_A001_seed_d3.json`.

---

## 5. Theorem C — Polynomial Weyl endomorphism

**Theorem C.** On the polynomial Weyl algebra with \([q_i,p_j]=\delta_{ij}\), the substitution
\[
Q_i=F_i(q),\qquad
P_j=\sum_k B_{jk}(q)\,p_k
\]
preserves the CCR relations
\[
[Q_i,Q_j]=0,\quad
[P_i,P_j]=0,\quad
[Q_i,P_j]=\delta_{ij}.
\]
Moreover each row of \(B\) is divergence-free, so \(P_j^{\mathrm{sym}}=-i X_j\).

**Proof sketch.**  
\([Q_i,P_j]=\sum_k B_{jk}\partial_k F_i=(JB^{T})_{ij}=\delta_{ij}\).  
Vanishing of \([P_i,P_j]\) is equivalent to coefficient identities
\[
\sum_k\bigl(B_{jk}\partial_k B_{il}-B_{ik}\partial_k B_{jl}\bigr)=0,
\]
verified by dual CAS. Row divergences vanish identically (CAS).

**Evidence:** `docs/validation/G3-weyl-A001-dossier.md`; `data/anchor/psi_weyl_A001.json`; `cas_weyl_A001_*.json`.

---

## 6. Theorem D — Incompleteness of \(X_1\)

**Theorem D.** The dual field \(X_1\) is incomplete on \(\mathbb{R}^3\).

**Explicit curve.** For \(t\in[0,\tfrac12)\), with continuous extension at \(t=0\) equal to \(q_\star=(1,0,0)\),
\[
\begin{aligned}
q_0(t)&=\frac{-2t-\sqrt{1-2t}+1}{t(2t-1)},\\
q_1(t)&=t,\\
q_2(t)&=t^2\bigl(2t-3\sqrt{1-2t}-1\bigr).
\end{aligned}
\]

**Proof.**  
Let \(\gamma(t)=(q_0(t),q_1(t),q_2(t))\).  
(1) On \((0,\tfrac12)\), \(\gamma\) is smooth; limits at \(0\) recover \(q_\star\) with velocity \(X_1(q_\star)=(\tfrac32,1,0)\).  
(2) Computer algebra yields \(F(\gamma(t))=(0,t,2)\) identically, hence \(\frac{d}{dt}F(\gamma)=e_1\). Since \(\det DF\equiv-2\), the unique vector field with \(DF\cdot X_1=e_1\) is \(X_1\), and direct differentiation confirms \(\gamma'=X_1(\gamma)\).  
(3) As \(t\to\tfrac12^-\), \(q_0(t)\sim\sqrt{2/(1/2-t)}\to+\infty\), so \(\gamma\) escapes every compact set in finite time and cannot extend continuously through \(t=\tfrac12\) in \(\mathbb{R}^3\).

**Evidence:** `docs/validation/G4-X1-incompleteness.md`; `scripts/cas/verify_X1_blowup_curve_A001.py` (PASS).

**Remark (existential form).** Independently, not all of \(X_0,X_1,X_2\) can be complete: complete dual flows would force \(F(\mathbb{R}^3)=\mathbb{R}^3\) by translation invariance of the image, contradicting omission of real points of the complex omitted set (e.g. \(\gamma_\star=(1/12,1,4/3)\)). See `G4-Xj-incompleteness.md`.

---

## 7. Theorem E — Failure of essential self-adjointness for \(P_1^{\mathrm{sym}}\)

**Theorem E.** The operator
\[
P_1^{\mathrm{sym}}=-i X_1
\quad\text{on}\quad
C_c^\infty(\mathbb{R}^3)\subset L^2(\mathbb{R}^3)
\]
is **not essentially self-adjoint**.

**Proof sketch.**  
\(X_1\) is smooth and divergence-free, and incomplete (Theorem D). For such vector fields on \(\mathbb{R}^n\), incompleteness implies that \(H=-iX\) on \(C_c^\infty\) is not essentially self-adjoint: if it were, Stone’s theorem would yield a global unitary group implementing characteristic transport along the flow, which cannot exist globally when the flow is incomplete (standard necessity argument; Reed–Simon II for Stone/ESS; Chernoff 1973 as historical Chernoff-type reference). Details: `docs/validation/G4-Chernoff-discharge.md`.

**Reading.** Non-ESS means the dense-domain recipe does not select a unique self-adjoint observable; self-adjoint extensions may still exist and require additional choices at the incomplete end.

---

## 8. Deficiency indices for \(P_1^{\mathrm{sym}}\)

**Proposition (minimal bound).**  
If \(n_\pm=\dim\ker((P_1^{\mathrm{sym}})^*\mp i)\) in the convention of `G4-P1-deficiency-indices.md`, then
\[
\max(n_+,n_-)\ge 1.
\]

**Orbit model.** The integral curve of Theorem D extends backward for all negative times (explicit formula on \((-\infty,\tfrac12)\); numeric checks to large negative \(t\)). Thus the distinguished orbit is a half-line \((-\infty,\tfrac12)\). The comparison operator \(-i\,d/dt\) on \(C_c^\infty(-\infty,T)\) is unitarily equivalent to a half-line model with deficiency indices
\[
(n_+,n_-)_{\mathrm{orbit}}\in\{(1,0),(0,1)\}
\]
(orientation-dependent), not \((1,1)\) (finite-interval model ruled out by backward completeness).

**Global indices on \(L^2(\mathbb{R}^3)\).** Exact global \((n_+,n_-)\) remain **open**: they require a measurable orbit decomposition and control of the transverse measure of incomplete orbits (possibly infinite indices if that measure is positive).

**Evidence:** `docs/validation/G4-P1-deficiency-indices.md`.

---

## 9. Non-claims (binding)

1. No claim of a unitary quantum gate, quantum channel, CP instrument, or computational advantage.  
2. No claim that \(P_0^{\mathrm{sym}}\) or \(P_2^{\mathrm{sym}}\) fails ESS.  
3. No claim of strong commutation of a joint unbounded CCR package after choosing extensions.  
4. No claim of a unique physically preferred self-adjoint extension.  
5. No claim of a von Neumann inclusion index tied to generic degree.  
6. No slogan claim that the Jacobian conjecture is “factory false” as a Quantyra theorem beyond the finite identities used.  
7. Companion family/degree-\(d\) pilots in the repository are outside the theorem list above unless separately cited.

---

## 10. Open problems

1. Exact global deficiency indices of \(P_1^{\mathrm{sym}}\) on \(L^2(\mathbb{R}^3)\).  
2. ESS status of \(P_0^{\mathrm{sym}}\) and \(P_2^{\mathrm{sym}}\).  
3. Strong CCR / joint spectral theory after extensions.  
4. Lean formalization of Theorems B–E.  
5. The same depth of analysis for atlas row A002 (degree-\(4\) pilot) and general Cor.~5.3 family maps.

---

## 11. Conclusion

For the A001 seed Keller map we establish polynomial Poisson and Weyl lifts of the canonical relations, prove incompleteness of the dual field \(X_1\) by an explicit escaping integral curve, and conclude that \(P_1^{\mathrm{sym}}=-i X_1\) is not essentially self-adjoint on \(C_c^\infty(\mathbb{R}^3)\). Algebraic preservation of CCR-type relations is therefore compatible with failure of the standard unique-observable recipe for at least one dual momentum. Sharpening global deficiency indices and strong CCR remains open.

---

## Acknowledgments

Research conducted in the Quantyra Inc. research program EXOTIC-CCR. Reproducible computer-algebra and Lean certificates are included in the public repositories cited above.

---

## References

1. P. R. Chernoff, *Essential self-adjointness of powers of generators of hyperbolic equations*, J. Funct. Anal. **12** (1973), 401–414.  
2. M. Reed and B. Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness*, Academic Press, 1975.  
3. H. Bass, E. H. Connell, D. Wright, *The Jacobian conjecture: reduction of degree and formal expansion of the inverse*, Bull. Amer. Math. Soc. **7** (1982), 287–330.  
4. O.-H. Keller, *Ganze Cremona-Transformationen*, Monatsh. Math. Phys. **47** (1939), 299–306.  
5. Repository dossiers and CAS reports in https://github.com/Quantyra/jacobian-weyl-quantum-phase-space (release v0.2.1 and later).  
6. Lean seed certificates: https://github.com/Quantyra/exotic-ccr-lean.  
7. Public seed map / counterexample provenance as recorded in `docs/provenance/` and `docs/literature/` of the science repository (Alpège announcement lineage; independent Lean formalizations in the public record).

---

## Appendix A — Evidence map (repository paths)

| Theorem | Primary dossier / proof | CAS / Lean |
|---------|-------------------------|------------|
| A | `docs/validation/D0-seed-validation-dossier.md` | `data/anchor/cas_*_report.json`; exotic-ccr-lean |
| B | `docs/validation/G2-poisson-A001-dossier.md` | `cas_poisson_A001_*.json` |
| C | `docs/validation/G3-weyl-A001-dossier.md` | `cas_weyl_A001_*.json` |
| D | `docs/validation/G4-X1-incompleteness.md` | `cas_X1_blowup_curve_A001.json` |
| E | `docs/validation/G4-Chernoff-discharge.md` | (logical + D) |
| Deficiency | `docs/validation/G4-P1-deficiency-indices.md` | orbit geometry from D |

---

## Appendix B — Internal claim ledger (software package)

See also `docs/notes/A001-minimum-result-note.md` for the living ledger used by the software release. This draft does not expand that ledger.

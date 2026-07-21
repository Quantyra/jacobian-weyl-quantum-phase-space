# EXOTIC-CCR A001 — Minimum result note

**Author:** Daniel Eric Fredriksen (Quantyra Inc.)
**Program:** EXOTIC-CCR (Quantyra Inc.)  
**Object:** Atlas row **A001-seed-d3** (announced seed Keller map \(F\))  
**Date:** 2026-07-21  
**Status:** Internal scientific note — claims bounded to certified package only  
**Planning:** `Quantyra-Planning2` epic E005  

**Closeout index:** [`docs/validation/PROGRAM-CLOSEOUT-G0-G7-A001.md`](../validation/PROGRAM-CLOSEOUT-G0-G7-A001.md)

---

## 0. Setup

Let \(F:\mathbb{R}^3\to\mathbb{R}^3\) (equivalently over \(\mathbb{C}\) in the algebraic layer) be the seed map
\[
\begin{aligned}
F_0 &= (1+xy)^3 z + y^2(1+xy)(4+3xy),\\
F_1 &= y + 3x(1+xy)^2 z + 3xy^2(4+3xy),\\
F_2 &= 2x - 3x^2 y - x^3 z,
\end{aligned}
\]
with Jacobian \(J=DF\), \(\det J\equiv -2\), and
\[
B := J^{-T}.
\]
Dual fields: \(X_j=\sum_k B_{jk}(q)\,\partial_{q_k}\).  
Three-point collision: \(F\) sends
\((0,0,-1/4)\), \((1,-3/2,13/2)\), \((-1,3/2,13/2)\)
to \((-1/4,0,0)\).

**Freeze / Lean:**  
`data/anchor/F_announced_det_m2.json` · [Quantyra/exotic-ccr-lean](https://github.com/Quantyra/exotic-ccr-lean) `v0.1.1`

---

## 1. Theorems (certified package)

### Theorem A — Seed algebraic identities (G0)
1. \(\det DF = -2\) (constant).  
2. The three collision identities hold (char \(\neq 2\) as needed).  
3. Consequently \(F\) is a noninjective Keller map (no polynomial inverse).

**Evidence:** dual CAS (SymPy + pure-Python); Lean `jacobianDet_F`, `evalMap_F_p*`.  
**Dossier:** [`D0-seed-validation-dossier.md`](../validation/D0-seed-validation-dossier.md)

---

### Theorem B — Classical cotangent lift is Poisson and non-injective (G2)
Define
\[
\Phi(q,p)=\bigl(F(q),\, B(q)\,p\bigr)\in T^*\mathbb{R}^3.
\]
Then:
1. \(B\) is polynomial and \(JB^{T}=I\).  
2. With the canonical Poisson structure on \((q,p)\), the coordinate functions \(Q_i=F_i(q)\) and \(P_j=\sum_k B_{jk}(q)p_k\) satisfy
   \[
   \{Q_i,Q_j\}=0,\quad
   \{P_i,P_j\}=0,\quad
   \{Q_i,P_j\}=\delta_{ij}.
   \]
3. \(\Phi\) is not injective: the three collision sources lift (via \(p=J(q)^{T}P_\star\)) to three distinct points with the same \(\Phi\)-image.  
4. **Partial:** \(\mu(\Phi)=3\) fiberwise from \(\mu(F)=3\) on the étale locus (not a full \(\mathbb{C}^6\) degree formalization).

**Evidence:** dual CAS Poisson package.  
**Dossier:** [`G2-poisson-A001-dossier.md`](../validation/G2-poisson-A001-dossier.md) · `data/anchor/Phi_A001_seed_d3.json`

---

### Theorem C — Polynomial Weyl endomorphism (G3)
On the polynomial Weyl algebra over \(\mathbb{Q}\) with \([q_i,p_j]=\delta_{ij}\) (\(\hbar=1\)), the substitution
\[
\psi:\quad
Q_i=F_i(q),\qquad
P_j=\sum_k B_{jk}(q)\,p_k
\]
extends to an algebra endomorphism preserving the CCR relations:
\[
[Q_i,Q_j]=0,\quad
[P_i,P_j]=0,\quad
[Q_i,P_j]=\delta_{ij}.
\]
Moreover \(\mathrm{div}\,B=0\) row-wise, so the Schrödinger candidates
\[
P_j^{\mathrm{sym}}
=
\tfrac12\sum_k\{B_{jk},p_k\}
=
-i X_j
=
P_j^{\mathrm{left}}
\]
coincide on \(C_c^\infty\) / \(\mathcal{S}\).

**Evidence:** dual CAS commutator identities.  
**Dossier:** [`G3-weyl-A001-dossier.md`](../validation/G3-weyl-A001-dossier.md) · `data/anchor/psi_weyl_A001.json`

---

### Theorem D — Some dual field is incomplete (G4)
At least one dual field \(X_j\) (\(j\in\{0,1,2\}\)) is **incomplete** on \(\mathbb{R}^3\).

**Proof idea.** If all \(X_j\) were complete, then \(F(\phi_t^{(j)}(q))=F(q)+t e_j\) for all \(t\), so \(F(\mathbb{R}^3)\) would be invariant under all coordinate translations, hence equal to \(\mathbb{R}^3\). But \(F\) omits real points of the complex omitted set (e.g. \(\gamma_\star=(1/12,1,4/3)\)). Contradiction.

**Evidence:** geometric argument + CAS (no affine preimage of \(\gamma_\star\); \(\det J=-2\)).  
**Dossier:** [`G4-Xj-incompleteness.md`](../validation/G4-Xj-incompleteness.md)

---

### Theorem E — Some dual momentum is not essentially self-adjoint (G4)
There exists \(j\in\{0,1,2\}\) such that
\[
P_j^{\mathrm{sym}}=-i X_j
\quad\text{on}\quad
C_c^\infty(\mathbb{R}^3)\subset L^2(\mathbb{R}^3)
\]
is **not essentially self-adjoint**.

**Proof idea.** Combine Theorem D with the necessity statement: for a smooth divergence-free real vector field \(X\) on \(\mathbb{R}^n\), incompleteness of \(X\) implies that \(H_X=-iX\) on \(C_c^\infty\) is not ESS (Stone’s theorem + characteristic transport; Chernoff 1973 as historical anchor for Chernoff-type criteria; Reed–Simon II for Stone/ESS framework). A001 fields are polynomial and div-free, so hypotheses of the necessity argument apply.

**Evidence / discharge note:** [`G4-Chernoff-discharge.md`](../validation/G4-Chernoff-discharge.md)  
**Dossier:** [`G4-domains-CCR-A001-dossier.md`](../validation/G4-domains-CCR-A001-dossier.md)

**Reading.** ESS failure means the \(C_c^\infty\)/Schwartz recipe does **not** determine a unique self-adjoint momentum observable: extensions (boundary choices at incomplete ends) are required. It does **not** assert that no self-adjoint extension exists.

---

## 2. Claim ledger (A001 minimum package)

| ID | Statement | Status |
|----|-----------|--------|
| T-A | \(\det DF=-2\); 3-collision | **certified** |
| T-B | \(\Phi\) Poisson on generators; non-injective | **certified** |
| T-B-μ | \(\mu(\Phi)=3\) | **partial** (fiberwise) |
| T-C | Weyl \(\psi\) preserves poly CCR; \(\mathrm{div} B=0\) | **certified** |
| T-D | ∃ incomplete \(X_j\) | **proved** |
| T-E | ∃ \(j\) with \(P_j^{\mathrm{sym}}\) not ESS on \(C_c^\infty\) | **proved** |
| T-which-j | Explicit incomplete / non-ESS index \(j\) | **open** |
| T-def | Deficiency indices \(n_\pm\) | **open** |
| T-sCCR | Strong CCR / joint spectral package | **open** |
| T-phys | Reversible physical symmetry / unique momenta / channel / gate | **not authorized** |

---

## 3. Non-claims (binding)

1. We do **not** claim the Jacobian Conjecture’s global literature status beyond the finite identities and geometric consequences used above.  
2. We do **not** claim a unitary gate, quantum channel, CP map, or computational advantage.  
3. We do **not** claim all three \(P_j^{\mathrm{sym}}\) fail ESS.  
4. We do **not** claim strong commutation or a unique physical implementation after choosing self-adjoint extensions.  
5. We do **not** claim a von Neumann inclusion index related to generic degree \(d\) (G5 open).  
6. Family/degree-\(d\) results beyond the d=4 pilot and atlas registry are **out of scope** of this A001 note.  
7. “Factory false” is **not** asserted as a Quantyra theorem slogan.

---

## 4. Related program artifacts (pointers only)

| Item | Path / URL |
|------|------------|
| Atlas A001 | `data/atlas/entries/A001-seed-d3.json` |
| Atlas index | `data/atlas/index.json` |
| G0 family d=4 pilot | [`D0-family-pilot-dossier.md`](../validation/D0-family-pilot-dossier.md) |
| G5–G7 packages | `G5-completion-degree-A001-dossier.md`, `G6-CP-dilation-A001-dossier.md`, `G7-semigroup-index-A001-dossier.md` |
| Science repo | https://github.com/Quantyra/jacobian-weyl-quantum-phase-space |
| Lean repo | https://github.com/Quantyra/exotic-ccr-lean |

---

## 5. Open problems (next math)

1. **Which \(j\)?** Prove incompleteness / non-ESS for a specific dual field (numerics favor \(X_1\)).  
2. **Deficiency indices** of that \(P_j^{\mathrm{sym}}\).  
3. **Strong CCR** after choosing self-adjoint extensions (if any coherent joint theory exists).  
4. **Lean** formalization of Theorems B–E (or selected lemmas).  
5. **Family spine** for A002 / \(\psi_d\) at the same depth as A001.

---

## 6. One-paragraph summary

For the seed Jacobian-counterexample map we construct and dual-CAS-certify a classical Poisson cotangent lift and a polynomial Weyl-algebra endomorphism preserving CCR relations. We prove that not all associated dual vector fields can be complete on \(\mathbb{R}^3\), and hence that at least one symmetrized dual momentum fails essential self-adjointness on \(C_c^\infty(\mathbb{R}^3)\). Algebraic CCR preservation therefore does not yield uniquely determined Schrödinger momenta without additional boundary choices. Strong commutation, explicit index \(j\), and any channel/gate interpretation remain open and are not claimed.

# Program C — Free-Strict-Abstract-Joint (q and p together)

> **PARKED HISTORICAL RECORD (2026-08-01).** Not an active theorem-development task. Program C / C001 are withdrawn as a current theorem surface. Residuals require a new story and Lean-backed gate to reopen. Current status: [`A001-PROGRAM-CLOSEOUT-FINAL.md`](A001-PROGRAM-CLOSEOUT-FINAL.md).

**Date:** 2026-07-22  
**Status (superseding, 2026-07-29): WITHDRAWN HISTORICAL RECORD — OUTSIDE
THE CURRENT A001 PUBLICATION PACKAGE.** J6-C is withdrawn. The positive
Koopman/CP/\(C^*\)-completion claims are not current and remain open pending
Lean-backed formulation and review. Other theorem-grade Program C labels
below retain historical/not-Lean status only.
**Parent:** `PROGRAM-C-GenCP-Free-Strict.md`, `PROGRAM-C-C1d-Koopman-position.md`  
**Companion note:** C001 v0.9 cites this file for the joint \(q\)–\(p\) sector.  
**Residual detail:** `PROGRAM-C-residual-J4-Joint-Stone-Hom.md`, `PROGRAM-C-residual-mere-CP-Joint-Stone.md`, `PROGRAM-C-residual-CP-without-Stone.md`, `PROGRAM-C-residual-abstract-Cstar-full-psi.md`

---

> **Superseding notice.** This file preserves the former Program C taxonomy.
> Its CONSTRUCT/OBSTRUCT/Theorem labels are not current publication claims.
> In particular, the J6-C normal-CP construction is invalid as stated and
> withdrawn.

## 1. Standing data

Let \(H = L^2(\mathbb{R}^3)\). Write \(Q_i\) for multiplication by the coordinate \(q_i\), and
\[
P_j^{\mathrm{Sch}} = -i\,\partial_{q_j}
\]
for the standard Schrödinger momenta (essentially self-adjoint on \(C_c^\infty(\mathbb{R}^3)\), unique SA closure).

On the explicit A001 Keller seed announced by Alpöge (with Fable credited in
the announcement), dual fields are
\[
X_j = \sum_k B_{jk}(q)\,\partial_{q_k},\qquad B = J^{-T},
\]
with each row of \(B\) divergence-free (Piola). Minimal dual momenta
\[
H_j = -i X_j
\]
are symmetric on the core \(C_c^\infty(\mathbb{R}^3)\), and **not** essentially self-adjoint for the A001 \(H_1\) sector (A001 Theorems E–F: deficiency indices \((n_+,n_-)=(\infty,\infty)\)).

**Historical position-sector proposal — OPEN pending Lean.**
The pointwise formula for the proposed Koopman pullback on bounded-Borel
functions of \(Q\) is
\[
\Phi_0(f) = f\circ F,\qquad f\in\mathcal{B}_b(\mathbb{R}^3)
\]
The former normal unital \(*\)-homomorphism/CP conclusion is not current; see
the withdrawn/open C1d and C001 records.

**T4 framing.** No dual-\(F\) translation dynamics on \(L^2(\mathbb{R}^3)\) are claimed or required by the packs below.

---

## 1b. Two-tier axiom pack

### Tier A — Joint-Stone

A **Joint-Stone package** is a tuple
\[
\bigl(\Phi;\; \widetilde H_0,\,\widetilde H_1,\,\widetilde H_2\bigr)
\]
where:

1. \(\Phi\) is a unital normal CP map (or unital normal \(*\)-homomorphism) on a von Neumann algebra containing \(\mathcal{B}_b(Q)\) such that
   \[
   \Phi\big|_{\mathcal{B}_b(Q)} = \Phi_0
   \]
   (agrees with the Koopman position sector);
2. for each \(j\in\{0,1,2\}\), \(\widetilde H_j\) is a **self-adjoint extension** of the minimal operator \(H_j = -iX_j\) on \(C_c^\infty(\mathbb{R}^3)\);
3. **Stone / functional-calculus agreement:** for every \(j\) and every \(s\in\mathbb{R}\),
   \[
   \Phi\bigl(e^{is\,P_j^{\mathrm{Sch}}}\bigr) = e^{is\,\widetilde H_j},
   \]
   or equivalently \(\Phi\bigl(f(P_j^{\mathrm{Sch}})\bigr) = f(\widetilde H_j)\) for all \(f\in C_b(\mathbb{R})\).

**Joint-Stone-Canonical** additionally requires that the package be **uniquely determined** by the algebraic data \((\psi,F,B)\) alone, with **no free choice** of extension parameters (no unitary between deficiency subspaces left unspecified by \((\psi,F,B)\)).

### Tier B — Joint-Form

A **Joint-Form package** requires only sesquilinear-form (or quadratic-form) agreement of the momentum sector with \(\psi(p_j)=\sum_k B_{jk}(Q)p_k\) on a common dense core, **without** demanding self-adjoint extensions or unitary-group / Stone agreement.

**Status of Tier B (split):** Joint-Form-Core **CONSTRUCT** (forms of minimal \(H_j\) on \(C_c^\infty\)); Joint-Form-ESS-1 **OBSTRUCT** (ESS uniqueness fails by A001 \(H_1\) indices). Bare form-level agreement without ESS is not left as a vague OPEN blob.

---

## 2. Theorem J1 — von Neumann baseline

**Theorem J1 (von Neumann).**  
Let \(A\) be a densely defined symmetric operator on a Hilbert space. Write
\[
n_\pm = \dim\ker(A^*\mp i).
\]
Then:

1. Self-adjoint extensions of \(A\) exist if and only if \(n_+=n_-\).
2. \(A\) is essentially self-adjoint if and only if \((n_+,n_-)=(0,0)\).
3. When \(n_+=n_-=n\in\{1,2,\ldots,\infty\}\), self-adjoint extensions are parameterized by unitaries \(U:\mathcal{K}_+\to\mathcal{K}_-\) between the deficiency subspaces (von Neumann’s formula); in particular, if \(n=\infty\) there is a continuum-sized family of distinct self-adjoint-extension witnesses. No pairwise unitary-inequivalence classification is claimed.

**Citation.** M. Reed & B. Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness*, Academic Press, 1975 (Ch. X; deficiency indices and von Neumann’s extension theory). Standard textbook form; no exotic hypotheses.

**Proof sketch.** Deficiency subspaces \(\mathcal{K}_\pm=\ker(A^*\mp i)\) classify closed extensions; self-adjointness forces a unitary coupling \(\mathcal{K}_+\to\mathcal{K}_-\); ESS is equivalent to both kernels vanishing. \(\square\)

---

## 3. Theorem J2 — No Joint-Stone-Canonical for the A001 \(H_1\) sector

**Standing citation (A001 frozen public claim).**  
For the minimal operator \(H_1=-iX_1\) on \(C_c^\infty(\mathbb{R}^3)\),
\[
(n_+,n_-)=(\infty,\infty)
\]
(A001 Theorems E–F; not ESS; infinitely many SA extensions).  
**Do not** read this as an A001 claim about \(H_0\) or \(H_2\).

**Theorem J2 (No Joint-Stone-Canonical — \(H_1\) sector).**  
There is **no** Joint-Stone-Canonical package for the A001 dual-lift data, already at the single-generator \(H_1\) sector:

1. By Theorem J1 and the A001 pair \((\infty,\infty)\), there exists a continuum-sized family of distinct self-adjoint-extension witnesses \(\widetilde H_1\) of \(H_1\), parameterized by unitaries between infinite-dimensional deficiency subspaces. No pairwise unitary-inequivalence classification is claimed.
2. Every Joint-Stone package must pick some self-adjoint extension \(\widetilde H_1\) (Tier A, item 2) and implement its unitary group via \(\Phi\) (item 3).
3. The algebraic data \((\psi,F,B)\) alone — polynomial Weyl endomorphism, seed map, and Piola matrix — are the **same** for every such extension: they fix only the minimal operator on \(C_c^\infty\), not a boundary condition at incomplete \(X_1\)-ends (A001 Discussion / Theorem F reading).
4. Therefore no package is **uniquely determined** by \((\psi,F,B)\) alone. Joint-Stone-Canonical fails.

**Explicit non-claim of J2 (historical scope; superseded for CP+Stone).**  
The following J2--J7 taxonomy is historical/not-Lean. In particular,
Diag-CP-\(\Phi_0\) is withdrawn and the former BT-Envelope positive claim is
open pending Lean; none of these labels is part of current A001.

---

## 4. Historical J3 — withdrawn; full-triple question open

Earlier versions imported paper-only G4 assertions about exact \(H_0,H_2\)
deficiency pairs and used them to state a full-triple Joint-Stone no-go. Those
operator assertions are not Lean-backed at the current freeze and are
withdrawn as theorem evidence. They may not be rescued by calling them
“G4 companion” results.

Accordingly, J3 is **withdrawn**, not a conditional theorem available for
current use. H0/H2 deficiency, the existence of their self-adjoint
extensions, and the full-triple Joint-Stone question are **OPEN pending
Lean**. J2 remains an H1-only obstruction to a choice-free canonical package;
it does not imply the withdrawn full-triple conclusion.

---

## 5. Theorem J4 — No multiplicative single-generator Joint-Stone (Hom pack)

**Named pack Joint-Stone-Hom-1.**  
Choice-dependent single-\(j=1\) Joint-Stone with the **extra axiom** that \(\Phi\) is a unital normal \(*\)-homomorphism on the vNa generated by \(\mathcal{B}_b(Q)\) and \(\{e^{is P_1^{\mathrm{Sch}}}\}\) (not merely CP), with \(\Phi|_{\mathcal{B}_b(Q)}=\Phi_0\) and \(\Phi(e^{is P_1^{\mathrm{Sch}}})=e^{is\widetilde H_1}\) for some SA extension \(\widetilde H_1\supset H_1\).

**Theorem J4.** No Joint-Stone-Hom-1 package exists for A001.

**Proof sketch (full write-up: `PROGRAM-C-residual-J4-Joint-Stone-Hom.md`).**

1. Multiplicativity + Stone + \(\Phi_0\) \(\Rightarrow\) dual-\(F_1\) Heisenberg covariance:
   \[
   e^{-is\widetilde H_1}(f\circ F)\,e^{is\widetilde H_1}
   =
   f(F_0,F_1+s,F_2).
   \]
2. Hence \((F_1,\widetilde H_1)\) is a regular Schrödinger couple and \(F_0,F_2\) act on the multiplicity space only (Stone–von Neumann + Schur).
3. The joint spectral measure of \((F_0,F_1,F_2)\) must then have **\(s\)-independent** Lebesgue density on target space.
4. But \(F\) is a local diffeomorphism with \(|\det DF|\equiv 2\), so that density equals \(m/2\) with \(m(a,s,c)=\#F^{-1}(a,s,c)\). For A001, \(m\) takes the values \(3\) and \(1\) on two positive-measure open slabs near \((a,c)=(0,2)\) (explicit real-root counts). Contradiction. \(\square\)

**Explicit non-claim of J4 (updated by J5).**  
J4 needs multiplicativity **as an axiom**. The weaker mere-CP pack with the same Stone axiom is separately obstructed by Theorem J5 (multiplicative domain recovers covariance).

### 5b. Joint-Form split

| Pack | Verdict | Note |
|------|---------|------|
| **Joint-Form-Core** (sesquilinear forms of minimal \(H_j\) on \(C_c^\infty\) + \(\Phi_0\)) | **CONSTRUCT** | tautological on the dual-field core; no SA/Stone |
| **Joint-Form-ESS-1** (Core + ESS uniqueness for \(j=1\)) | **OBSTRUCT** | A001 \(H_1\) not ESS |

### 5c. Theorem J5 — No mere-CP single-generator Joint-Stone

**Named pack Joint-Stone-CP-1.**  
Choice-dependent single-\(j=1\) Joint-Stone with \(\Phi\) only unital normal CP (not Hom a priori), \(\Phi|_{\mathcal{B}_b(Q)}=\Phi_0\), and \(\Phi(e^{is P_1^{\mathrm{Sch}}})=e^{is\widetilde H_1}\) for some SA extension \(\widetilde H_1\supset H_1\).

**Theorem J5.** No Joint-Stone-CP-1 package exists for A001.

**Proof sketch (full write-up: `PROGRAM-C-residual-mere-CP-Joint-Stone.md`).**

1. Unital CP + \(\Phi(U(s))\) unitary \(\Rightarrow\) each Stone unitary \(U(s)=e^{is P_1^{\mathrm{Sch}}}\) lies in the **multiplicative domain** \(\mathcal{D}_\Phi\) (Kadison–Schwarz equality).
2. Bimodule identity \(\Rightarrow\) dual-\(F_1\) Heisenberg covariance (same formula as J4.1).
3. SvN product structure + \(s\)-independent target density, vs A001 sheet-count variation in \(s\) (J4.4–J4.5). Contradiction. \(\square\)

**Explicit non-claim of J5.**
J5 kills CP **with** Stone. The former J6-C claim about a normal CP extension
without Stone / SA momentum implementation is withdrawn as invalid; no
replacement positive theorem is current.

### 5d. Theorem J6 — Unitary-Image-CP-1 obstruction; withdrawn Diag-CP-Φ₀

**Named pack Unitary-Image-CP-1.**  
Unital normal CP \(\Phi:M\to B(H)\) on the vNa generated by \(\mathcal{B}_b(Q)\) and \(\{e^{is P_1^{\mathrm{Sch}}}\}\), with \(\Phi|_{\mathcal{B}_b(Q)}=\Phi_0\) and \(\Phi(e^{is P_1^{\mathrm{Sch}}})\) **unitary** for all \(s\) — **no** SA extension of \(H_1\) required.

**Theorem J6.** No Unitary-Image-CP-1 package exists for A001.

**Withdrawn pack Diag-CP-Φ₀.**

The historical definition used \(\Phi_{\mathrm{diag}}=\Phi_0\circ E\), but
the asserted normal expectation with the zero-mode rule does not exist.

**Withdrawn J6-C.** The former Diag-CP-\(\Phi_0\) claim is invalid as
stated: normality is incompatible with \(U(s)\to I\) ultraweakly as
\(s\to0\) and \(\Phi_{\mathrm{diag}}(U(s))=0\) for every \(s\ne0\).

**Proof sketch (full write-up: `PROGRAM-C-residual-CP-without-Stone.md`).**
J6: unitary image \(\Rightarrow\) multiplicative domain \(\Rightarrow\)
dual-\(F_1\) covariance \(\Rightarrow\) J4 geometry. The former J6-C
composition/conditional-expectation step is withdrawn and is not a proof.

### 5e. Historical J7 split — positive \(C^*\) branch open pending Lean

**Named pack Full-ψ-BT-Envelope.**  
Concrete \(C^*\) algebra \(\mathfrak{A}_\psi\subset B(H)\) generated by \(\Phi_0(C_b(Q))\) and bounded transforms \(Z_j=Z(\overline{H_j})\) of the closed minimal dual momenta.

**Historical J7-C claim — OPEN pending Lean.** The former text asserted that
Full-ψ-BT-Envelope is a well-defined unital \(C^*\) carrying position content
of \(\psi\) and momentum-form content via non-SA contractions. No such
positive theorem is current without Lean-backed formulation and review.

**Named pack Full-ψ-CFC-SA-1.**  
Unital normal CP extending \(\Phi_0\) that recovers SA continuous functional calculus of some \(\widetilde A_1\) for \(P_1^{\mathrm{Sch}}\) (equivalently: unitary Cayley image).

**Theorem J7.** No Full-ψ-CFC-SA-1 package exists (reduces to Unitary-Image-CP-1 / J6).

**Named pack Full-ψ-CP-Weyl-C\*.**  
Unital CP from a \(C^*\) completion of \(\mathcal{W}\) extending algebraic \(\psi\), without SA-CFC/unitary-image axioms — **OPEN (J7-O)**.

**Proof sketch (full write-up: `PROGRAM-C-residual-abstract-Cstar-full-psi.md`).**

---

## 6. Scoreboard

| Pack / claim | Verdict | Anchor |
|--------------|---------|--------|
| Position sector \(\Phi_0\) (Koopman) | **OPEN pending Lean** | former C1d / C001 paper-only claim |
| Joint-Stone-Canonical (choice-free, \((\psi,F,B)\) alone) | **CONDITIONAL-OBSTRUCTION / NO-GO** | **J2** (\(H_1\) continuum of extensions) |
| Full-triple Joint-Stone (all three \(\widetilde H_j\) SA) | **OPEN** | historical J3 withdrawn pending Lean-backed H0/H2 results |
| Joint-Stone-Hom-1 (multiplicative, single \(j=1\), choice-dependent) | **OBSTRUCT / NO-GO** | **J4** (\(s\)-dependent preimage count vs SvN product) |
| Joint-Stone-CP-1 (mere CP + Stone \(j=1\) + \(\Phi_0\), choice-dependent) | **OBSTRUCT / NO-GO** | **J5** (mult.\ domain \(\Rightarrow\) J4 geometry) |
| Unitary-Image-CP-1 (unitary image of \(U(s)\), no SA link) | **OBSTRUCT / NO-GO** | **J6** |
| Diag-CP-Φ₀ (\(\Phi_0\circ E\) on \(M\)) | **WITHDRAWN** | **J6-C invalid as stated** |
| Joint-Form-Core (forms on \(C_c^\infty\) + \(\Phi_0\)) | **CONSTRUCT** | **J4-F** |
| Joint-Form-ESS-1 (form + ESS uniqueness, \(j=1\)) | **OBSTRUCT / NO-GO** | **J4-E** + A001 E–F |
| Full-ψ-BT-Envelope (\(\Phi_0(C_b)+Z(\overline{H_j})\)) | **OPEN pending Lean** | former J7-C paper-only claim |
| Full-ψ-CFC-SA-1 / Cayley-Unitary-1 | **OBSTRUCT / NO-GO** | **J7** |
| Full-ψ-CP-Weyl-C\* (CP from completion of \(\mathcal{W}\), no SA-CFC) | **OPEN** | **J7-O** |
| C0 composition endo | NO-GO | retained |
| Bogoliubov / quasifree | NO-GO | retained |
| Free-Strict-Regular-v2 | WITHDRAWN | false |

**Reading.**  
The verified A001 \(H_1\) pair supports J2. Historical J3 is withdrawn, so
the full-triple strengthening is open pending Lean-backed H0/H2 results.
J4–J6 close the named unitary-image / Stone packs on the single-\(j=1\)
joint vNa. The former Diag-CP-Φ₀/J6-C construct is withdrawn as invalid.
The former Full-\(\psi\) BT-Envelope \(C^*\) construction is historical and
**OPEN pending Lean**; SA-CFC recovery remains a historical NO-GO label, and
CP from a Weyl \(C^*\) completion without SA-CFC remains **OPEN**.

---

## 7. Non-claims

1. **No dual-\(F\) translation dynamics** beyond T4 framing; this note does not repair or claim dual-flow unitary groups on \(L^2(\mathbb{R}^3)\).
2. **No gates, channels, or computational advantage.**
3. **No claim that every joint CP construction is impossible** — historical
   J3 is withdrawn and the full-triple question is open. The retained named
   obstructions are Joint-Stone-Canonical (J2), multiplicative
   Joint-Stone-Hom-1 (J4), mere-CP Joint-Stone-CP-1 (J5),
   Unitary-Image-CP-1 (J6), Full-ψ-CFC-SA-1 (J7), and Joint-Form-ESS-1
   (J4-E). Diag-CP-Φ₀/J6-C is withdrawn; the former Full-ψ-BT-Envelope
   construction is historical and open pending Lean.
4. **No claim beyond the bounded historical results retained here:**
   - J2 uses only A001 \(H_1\) deficiency \((\infty,\infty)\) + von Neumann;
   - historical J3 is withdrawn; H0/H2 and the full-triple question remain open pending Lean;
   - J4 uses multiplicativity + SvN product structure vs A001 sheet-count variation in \(s\);  
   - J5 uses unital CP multiplicative domain + the same geometric kill as J4;  
   - J6 drops the SA-extension-of-\(H_1\) axiom and still kills unitary image;
     J6-C is withdrawn and does not construct \(\Phi_0\circ E\);
   - the former J7-C BT-Envelope construction is open pending Lean; J7 retains
     only its historical SA-CFC obstruction label via J6; J7-O
     (CP-Weyl-C\*) remains open; Joint-Form-Core is form-level only.
5. **No claim that this proves the Jacobian conjecture** or any global quantization failure.
6. **No preferred physical boundary condition** at incomplete ends is selected.

---

## 8. Pointers

| Item | Path |
|------|------|
| A001 \(H_1\) pair \((\infty,\infty)\) | `docs/notes/A001-arxiv.tex` (Theorems E–F) |
| Historical withdrawn H0/H2/J3 source | `docs/validation/G4-H0-H2-deficiency-bounds.md` (not current theorem evidence) |
| G4 \(H_1\) extension taxonomy | `docs/validation/G4-H1-extension-taxonomy.md` |
| Position construct | `docs/validation/PROGRAM-C-C1d-Koopman-position.md` |
| Parent Free-Strict | `docs/validation/PROGRAM-C-GenCP-Free-Strict.md` |
| J4 residual detail | `docs/validation/PROGRAM-C-residual-J4-Joint-Stone-Hom.md` |
| J5 mere-CP residual detail | `docs/validation/PROGRAM-C-residual-mere-CP-Joint-Stone.md` |
| J6 CP without Stone | `docs/validation/PROGRAM-C-residual-CP-without-Stone.md` |
| J7 full-ψ abstract C* | `docs/validation/PROGRAM-C-residual-abstract-Cstar-full-psi.md` |
| C001 companion | `docs/notes/C001-cp-correspondence-arxiv.tex` |

(End of file)

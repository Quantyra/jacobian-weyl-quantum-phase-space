# Program C — Free-Strict-Abstract-Joint (q and p together)

**Date:** 2026-07-21  
**Status:** **Joint-Stone-Canonical = CONDITIONAL-OBSTRUCTION** (Theorems J2–J3); residual Joint-Stone (choice-dependent) and Joint-Form remain **OPEN**  
**Parent:** `PROGRAM-C-GenCP-Free-Strict.md`, `PROGRAM-C-C1d-Koopman-position.md`  
**Companion note:** C001 v0.5 cites this file for the joint \(q\)–\(p\) sector.

---

## 1. Standing data

Let \(H = L^2(\mathbb{R}^3)\). Write \(Q_i\) for multiplication by the coordinate \(q_i\), and
\[
P_j^{\mathrm{Sch}} = -i\,\partial_{q_j}
\]
for the standard Schrödinger momenta (essentially self-adjoint on \(C_c^\infty(\mathbb{R}^3)\), unique SA closure).

On the Alpöge–Fable A001 seed, dual fields are
\[
X_j = \sum_k B_{jk}(q)\,\partial_{q_k},\qquad B = J^{-T},
\]
with each row of \(B\) divergence-free (Piola). Minimal dual momenta
\[
H_j = -i X_j
\]
are symmetric on the core \(C_c^\infty(\mathbb{R}^3)\), and **not** essentially self-adjoint for the A001 \(H_1\) sector (A001 Theorems E–F: deficiency indices \((n_+,n_-)=(\infty,\infty)\)).

**Position sector (already constructed).**  
\(\Phi_0\) is the Koopman pullback on bounded-Borel functions of \(Q\):
\[
\Phi_0(f) = f\circ F,\qquad f\in\mathcal{B}_b(\mathbb{R}^3)
\]
(normal unital \(*\)-homomorphism; C1d / C001 Theorem Koopman).

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

**Status of Tier B:** left **OPEN**. This note does **not** force a no-go for Joint-Form.

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
3. When \(n_+=n_-=n\in\{1,2,\ldots,\infty\}\), self-adjoint extensions are parameterized by unitaries \(U:\mathcal{K}_+\to\mathcal{K}_-\) between the deficiency subspaces (von Neumann’s formula); in particular, if \(n=\infty\) there is a continuum of inequivalent extensions.

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

1. By Theorem J1 and the A001 pair \((\infty,\infty)\), there exists a continuum of inequivalent self-adjoint extensions \(\widetilde H_1\) of \(H_1\), parameterized by unitaries between infinite-dimensional deficiency subspaces.
2. Every Joint-Stone package must pick some self-adjoint extension \(\widetilde H_1\) (Tier A, item 2) and implement its unitary group via \(\Phi\) (item 3).
3. The algebraic data \((\psi,F,B)\) alone — polynomial Weyl endomorphism, seed map, and Piola matrix — are the **same** for every such extension: they fix only the minimal operator on \(C_c^\infty\), not a boundary condition at incomplete \(X_1\)-ends (A001 Discussion / Theorem F reading).
4. Therefore no package is **uniquely determined** by \((\psi,F,B)\) alone. Joint-Stone-Canonical fails.

**Explicit non-claim of J2.**  
J2 does **not** prove non-existence of every choice-dependent Joint-Stone package. It proves only that **no canonical** (choice-free, uniquely fixed by algebraic data) Joint-Stone package exists for the \(H_1\) sector. Existence of some (non-unique) Joint-Stone package that picks one extension by hand, and its compatibility with a global CP \(\Phi\) extending \(\Phi_0\), remains **OPEN**.

---

## 4. Theorem J3 — Full-triple Joint-Stone-Canonical obstruction (G4 companion)

**Standing citation (G4 companion — not A001).**  
The validation note `G4-H0-H2-deficiency-bounds.md` records, for the dual-flow models of the A001 seed on \(L^2(\mathbb{R}^3)\):
\[
H_0:\quad (n_+,n_-)=(\infty,\,0),\qquad
H_2:\quad (n_+,n_-)=(0,\,\infty).
\]
Hence, by Theorem J1, the minimal operators \(H_0\) and \(H_2\) admit **no** self-adjoint extensions.  
These pairs are **G4 companion results**, not frozen A001 theorem-grade claims (A001 is \(H_1\)-only; see A001 errata / scope paragraph).

**Theorem J3 (No full-triple Joint-Stone package — under G4 pairs).**  
Assume the G4 companion pairs
\[
(n_+^{(0)},n_-^{(0)})=(\infty,0),\qquad
(n_+^{(2)},n_-^{(2)})=(0,\infty)
\]
as in `G4-H0-H2-deficiency-bounds.md`. Then:

1. No self-adjoint extension \(\widetilde H_0\) of minimal \(H_0\) exists (J1 + unequal indices).
2. No self-adjoint extension \(\widetilde H_2\) of minimal \(H_2\) exists.
3. Therefore **no** Joint-Stone package \((\Phi;\widetilde H_0,\widetilde H_1,\widetilde H_2)\) exists at all for the full triple — canonical or otherwise — because Tier A item 2 cannot be satisfied for \(j=0\) and \(j=2\).

**Combined reading with J2.**  
Even restricting attention to the \(H_1\) leg alone, Joint-Stone-Canonical already fails (J2). Under the G4 pairs, the full-triple Joint-Stone requirement fails outright (J3), strengthening the obstruction from “no canonical choice” to “no full-triple package.”

**Scope discipline.**  
Cite J3 as a **G4-companion-dependent** theorem of this Program C note. Do **not** promote the \(H_0/H_2\) pairs to A001 theorems.

---

## 5. Scoreboard

| Pack / claim | Verdict | Anchor |
|--------------|---------|--------|
| Position sector \(\Phi_0\) (Koopman) | **CONSTRUCT** | C1d / C001 |
| Joint-Stone-Canonical (choice-free, \((\psi,F,B)\) alone) | **CONDITIONAL-OBSTRUCTION / NO-GO** | **J2** (\(H_1\) continuum of extensions) |
| Full-triple Joint-Stone (all three \(\widetilde H_j\) SA) | **CONDITIONAL-OBSTRUCTION / NO-GO** | **J3** (G4: \(H_0,H_2\) unequal indices ⇒ no SA extensions) |
| Single-extension Joint-Stone existence + CP compatibility with \(\Phi_0\) (choice-dependent, e.g. one \(\widetilde H_1\) only) | **OPEN** | residual |
| Joint-Form (sesquilinear / form-only on a dense core) | **OPEN** | Tier B; no no-go forced here |
| C0 composition endo | NO-GO | retained |
| Bogoliubov / quasifree | NO-GO | retained |
| Free-Strict-Regular-v2 | WITHDRAWN | false |

**Reading.**  
“CONDITIONAL-OBSTRUCTION” for Joint-Stone-Canonical is unconditional on the verified A001 \(H_1\) pair (J2). The full-triple strengthening (J3) is conditional on accepting the G4 companion deficiency pairs for \(H_0,H_2\). Residual OPEN rows are **not** claimed impossible.

---

## 6. Non-claims

1. **No dual-\(F\) translation dynamics** beyond T4 framing; this note does not repair or claim dual-flow unitary groups on \(L^2(\mathbb{R}^3)\).
2. **No gates, channels, or computational advantage.**
3. **No claim that every joint CP construction is impossible** — only Joint-Stone-Canonical (J2) and, under G4 pairs, full-triple Joint-Stone (J3).
4. **No claim beyond what is proved here:**  
   - J2 uses only A001 \(H_1\) deficiency \((\infty,\infty)\) + von Neumann;  
   - J3 uses G4 companion pairs for \(H_0,H_2\), cited as companion, not as A001;  
   - Joint-Form and choice-dependent single-extension Joint-Stone+CP remain open.
5. **No claim that this proves the Jacobian conjecture** or any global quantization failure.
6. **No preferred physical boundary condition** at incomplete ends is selected.

---

## 7. Pointers

| Item | Path |
|------|------|
| A001 \(H_1\) pair \((\infty,\infty)\) | `docs/notes/A001-arxiv.tex` (Theorems E–F) |
| G4 \(H_0,H_2\) pairs | `docs/validation/G4-H0-H2-deficiency-bounds.md` |
| G4 \(H_1\) extension taxonomy | `docs/validation/G4-H1-extension-taxonomy.md` |
| Position construct | `docs/validation/PROGRAM-C-C1d-Koopman-position.md` |
| Parent Free-Strict | `docs/validation/PROGRAM-C-GenCP-Free-Strict.md` |
| C001 companion | `docs/notes/C001-cp-correspondence-arxiv.tex` |

(End of file)

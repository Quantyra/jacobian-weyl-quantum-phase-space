# Program C — C1d: Koopman position-sector construct (Free-Strict-Abstract)

**Date:** 2026-07-22  
**Status (superseding, 2026-07-29): HISTORICAL / OPEN PENDING LEAN —
OUTSIDE THE CURRENT A001 PUBLICATION PACKAGE.** The former generic assertion
that a unital \(*\)-homomorphism of von Neumann algebras is automatically
normal is false. The specific pullback's normality has not been re-established
in Lean, so no positive normal-CP theorem is current. J6-C is withdrawn and
the former BT-envelope construct is open pending Lean.

**Parent:** `PROGRAM-C-GenCP-Free-Strict.md`

---

## 0. Why this differs from the withdrawn Regular-v2 and the C0 NO-GO

- **C0 NO-GO** (retained): fails because \(F\) is **not proper**, so
  \(f\circ F\notin C_0(\mathbb{R}^3)\) for some \(f\in C_0\). That argument
  is about the algebra \(C_0\) (vanishing at infinity).
- **Regular-v2** (withdrawn): wrongly tried to derive nondegeneracy failure
  from non-surjectivity; false, as the adversarial gate showed.
- **This note (C1d)** uses **bounded Borel** functions, not \(C_0\): no
  vanishing-at-infinity requirement, so non-properness is irrelevant here.

---

> **Superseding notice.** The proof and scoreboards below are retained as
> historical evidence only. CONSTRUCT and Theorem labels do not state a
> current publication result.

## 1. Axiom pack **Free-Strict-Abstract-Koopman**

Let \(H=L^2(\mathbb{R}^3)\), \(Q=(Q_0,Q_1,Q_2)\) the position operators
(multiplication), and \(\mathcal{B}_b(\mathbb{R}^3)\) the abelian von Neumann
algebra of bounded Borel functions of \(Q\) (\(\cong L^\infty(\mathbb{R}^3)\)
acting by multiplication).

1. \(\Phi_0:\mathcal{B}_b(\mathbb{R}^3)\to\mathcal{B}_b(\mathbb{R}^3)\),
   \(\Phi_0(f):=f\circ F\).
2. No requirement that \(f\circ F\in C_0\) (bounded Borel only).
3. T4: no claim about implementing dual-\(F\) translations dynamically.

---

## 2. Historical Koopman position-sector claim (open pending Lean)

**Historical claim, not a current theorem.** The former text asserted that
\(\Phi_0\) is a well-defined **unital normal \(*\)-homomorphism**
\(\mathcal{B}_b(\mathbb{R}^3)\to\mathcal{B}_b(\mathbb{R}^3)\), hence a normal
unital CP map, for every local diffeomorphism \(F\). The pointwise
\(*\)-homomorphism calculation below is retained, but normality of the
specific a.e.-class pullback has not been Lean-formalized or independently
re-established. The normal-CP conclusion is **OPEN pending Lean**.

**Historical proof analysis.**
1. *Well-defined on Borel functions.* \(F\) continuous \(\Rightarrow\)
   \(f\circ F\) is Borel measurable whenever \(f\) is Borel measurable, and
   bounded whenever \(f\) is bounded. No vanishing-at-infinity condition is
   needed, so non-properness of \(F\) (which broke the \(C_0\) case) is
   irrelevant here.
2. *Well-defined up to a.e. equivalence.* Elements of \(\mathcal{B}_b\) are
   really equivalence classes mod Lebesgue-null sets. \(F\) is a local
   diffeomorphism (\(\det DF\neq 0\) everywhere), so by the inverse function
   theorem \(\mathbb{R}^3\) is covered by countably many open sets on which
   \(F\) restricts to a diffeomorphism; on each such chart, preimages of
   Lebesgue-null sets under \(F\) are Lebesgue-null (standard change of
   variables, \(|\det DF|\) locally bounded above and below on compacts).
   Hence \(F\) is **non-singular**, and \(f\mapsto f\circ F\) descends to a
   well-defined map on a.e.-equivalence classes.
3. *Unital \(*\)-homomorphism.* \((f\circ F)^* = \bar f\circ F = \overline{f\circ F}\);
   \((fg)\circ F=(f\circ F)(g\circ F)\); \(1\circ F=1\). These are pointwise
   identities, hence hold a.e.
4. *Withdrawn normality step.* The historical proof asserted that every
   unital \(*\)-homomorphism between von Neumann algebras is automatically
   normal. That general assertion is false. Complete positivity follows from
   \(*\)-homomorphism, but the specific normality claim is left open pending
   Lean-backed proof and review.

**Retained limited conclusion.** The Regular-v2 intuition that
non-surjectivity alone obstructs the pointwise bounded-Borel composition
formula is false. This does not establish the former normal Koopman/CP theorem
on a.e.-equivalence classes; that theorem remains open pending Lean. The
retained \(C_0\) obstruction on the vanishing-at-infinity subalgebra still
stands.

---

## 3. Joint (q,p) extension — refined status

\(\Phi_0\) only handles the **position sector** \(\psi(q_i)=F_i(q)\). The
momentum sector \(\psi(p_j)=\sum_k B_{jk}(q)p_k\) does **not** commute with
\(Q\) and cannot be captured by a Koopman/composition operator alone.

**Refined write-up:** `PROGRAM-C-Free-Strict-Abstract-Joint.md` (Theorems J1–J6); residual detail notes under `PROGRAM-C-residual-*.md`.

### 3.1 Joint-Stone-Canonical — NO-GO (J2)

A **Joint-Stone-Canonical** package would require self-adjoint extensions
\(\widetilde H_j\supset H_j=-iX_j\) and a unital normal CP \(\Phi\) extending
\(\Phi_0\) with Stone agreement
\(\Phi(e^{is P_j^{\mathrm{Sch}}})=e^{is\widetilde H_j}\), uniquely fixed by
\((\psi,F,B)\) alone.

**Theorem J2:** A001 gives \((n_+,n_-)=(\infty,\infty)\) for \(H_1=-iX_1\), so
von Neumann supplies a continuum-sized family of distinct
self-adjoint-extension witnesses; algebraic data do not pick one. No pairwise
unitary-inequivalence classification is claimed. **Joint-Stone-Canonical fails**. Choice-dependent
CP+Stone is separately ruled out by J5; unitary image without SA link by J6.

**Withdrawn historical J3:** older G4 notes asserted exact \(H_0,H_2\)
deficiency pairs and used them to claim that no full-triple Joint-Stone
package exists. Those inputs are not Lean-backed and are withdrawn as current
theorem evidence. H0/H2 deficiency, H0/H2 self-adjoint-extension existence,
and the J3 full-triple question are **OPEN pending Lean**.

### 3.2 Residual update (J4–J7)

| Slice | Verdict |
|-------|---------|
| Joint-Stone-Hom-1 (multiplicative single \(j=1\)) | **OBSTRUCT (J4)** — see `PROGRAM-C-residual-J4-Joint-Stone-Hom.md` |
| Joint-Stone-CP-1 (mere CP + Stone \(j=1\) + \(\Phi_0\)) | **OBSTRUCT (J5)** — see `PROGRAM-C-residual-mere-CP-Joint-Stone.md` |
| Unitary-Image-CP-1 (unitary image of \(U(s)\), no SA link) | **OBSTRUCT (J6)** — see `PROGRAM-C-residual-CP-without-Stone.md` |
| Diag-CP-Φ₀ (\(\Phi_0\circ E\) on joint vNa) | **WITHDRAWN (J6-C invalid as stated)** |
| Joint-Form-Core (forms on \(C_c^\infty\) + \(\Phi_0\)) | **CONSTRUCT (J4-F)** |
| Joint-Form-ESS-1 | **OBSTRUCT (J4-E)** |
| Full-ψ-BT-Envelope | **OPEN pending Lean** — former J7-C |
| Full-ψ-CFC-SA-1 | **OBSTRUCT (J7)** — same note |
| Full-ψ-CP-Weyl-C\* | **OPEN (J7-O)** — same note |

J5–J6: unital CP + unitary image of \(e^{is P_1^{\mathrm{Sch}}}\) puts those
unitaries in the multiplicative domain, recovers dual-\(F_1\) Heisenberg
covariance, and dies by SvN / sheet-count geometry (SA-extension-of-\(H_1\)
inessential). The former Diag-CP-Φ₀/J6-C non-Stone CP construction is
**withdrawn as invalid**.
Historical J7 split full-\(\psi\) abstract \(C^*\); its BT-Envelope positive
claim is now OPEN pending Lean, while CFC-SA/other labels are historical;
CP-Weyl-C\* OPEN.

---

## 4. Scoreboard update

| Pack | Verdict |
|------|---------|
| C0 → C0 composition (vanishing at infinity) | NO-GO |
| Bogoliubov / quasifree CCR | NO-GO |
| Free-Strict-Regular-v2 | WITHDRAWN (false) |
| **Free-Strict-Abstract-Koopman (position sector)** | **OPEN pending Lean** |
| Free-Strict-Abstract-Joint / **Joint-Stone-Canonical** | **NO-GO (J2)** — see `PROGRAM-C-Free-Strict-Abstract-Joint.md` |
| Free-Strict-Abstract-Joint / full-triple Joint-Stone | **OPEN; historical J3 withdrawn pending Lean** |
| Free-Strict-Abstract-Joint / Joint-Stone-Hom-1 | **NO-GO (J4)** |
| Free-Strict-Abstract-Joint / Joint-Stone-CP-1 | **NO-GO (J5)** |
| Free-Strict-Abstract-Joint / Unitary-Image-CP-1 | **NO-GO (J6)** |
| Free-Strict-Abstract-Joint / Diag-CP-Φ₀ | **WITHDRAWN** |
| Free-Strict-Abstract-Joint / Joint-Form-Core | **CONSTRUCT (J4-F)** |
| Free-Strict-Abstract-Joint / Full-ψ-BT-Envelope | **OPEN pending Lean** |
| Free-Strict-Abstract-Joint / Full-ψ-CFC-SA-1 | **NO-GO (J7)** |
| Free-Strict-Abstract-Joint / Full-ψ-CP-Weyl-C\* | **OPEN (J7-O)** |

---

## 5. Non-claims
No channel on \(B(H)\) implementing the full \(\psi\). No dual-\(F\)
translation dynamics (T4). Joint-Stone-Canonical (J2), multiplicative
Joint-Stone-Hom-1 (J4), mere-CP Joint-Stone-CP-1
(J5), Unitary-Image-CP-1 (J6), and Full-ψ-CFC-SA-1 (J7) are ruled out.
Diag-CP-Φ₀/J6-C is withdrawn as invalid; the former BT-Envelope \(C^*\)
construction is historical and **OPEN pending Lean**. Full-ψ-CP-Weyl-C\* is **not**
claimed impossible. Joint-Form-Core is form-level only. \(\Phi_0\) alone does
**not** realize \(\psi\); it realizes only the abelian position-generator part.
Historical J3 is withdrawn; the full-triple Joint-Stone question is open
pending Lean-backed H0/H2 results.

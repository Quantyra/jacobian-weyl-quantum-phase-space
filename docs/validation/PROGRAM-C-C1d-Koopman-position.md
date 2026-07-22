# Program C — C1d: Koopman position-sector construct (Free-Strict-Abstract)

**Date:** 2026-07-22  
**Status:** **CONSTRUCT** for the position sector (normal, bounded-Borel level); joint sector refined in `PROGRAM-C-Free-Strict-Abstract-Joint.md` (J2–J6 NO-GOs on Stone/unitary-image packages; Diag-CP-Φ₀ **CONSTRUCT**; full-\(\psi\) abstract \(C^*\) **OPEN**)  
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

## 2. Theorem (Koopman position-sector construct)

**Theorem.** \(\Phi_0\) is a well-defined **unital normal \(*\)-homomorphism**
\(\mathcal{B}_b(\mathbb{R}^3)\to\mathcal{B}_b(\mathbb{R}^3)\), hence in
particular a normal unital CP map, for **any** \(F\) that is a local
diffeomorphism (in particular for the A001 seed, \(\det DF\equiv -2\neq 0\)).

**Proof.**
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
4. *Normality / complete positivity.* A unital \(*\)-homomorphism between
   von Neumann algebras is automatically normal and completely positive
   (indeed multiplicative, the strongest CP case: \(\Phi_0(a^*a)=\Phi_0(a)^*\Phi_0(a)\)
   trivially). \(\blacksquare\)

**Corollary.** The Regular-v2 intuition (that non-surjectivity should
obstruct something) is confirmed to be **false** at the bounded-Borel level:
the Koopman pullback \(\Phi_0\) exists for *every* non-vanishing-Jacobian
\(F\), surjective or not, proper or not (though the retained \(C_0\)
obstruction on the *vanishing-at-infinity* subalgebra still stands).

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
von Neumann supplies a continuum of inequivalent SA extensions; algebraic
data do not pick one. **Joint-Stone-Canonical fails**. Choice-dependent
CP+Stone is separately ruled out by J5; unitary image without SA link by J6.

**Theorem J3 (G4 companion):** `G4-H0-H2-deficiency-bounds.md` records
\(H_0:(\infty,0)\), \(H_2:(0,\infty)\) — no SA extensions for those minimal
operators — so no full-triple Joint-Stone package exists under those pairs.

### 3.2 Residual update (J4–J6)

| Slice | Verdict |
|-------|---------|
| Joint-Stone-Hom-1 (multiplicative single \(j=1\)) | **OBSTRUCT (J4)** — see `PROGRAM-C-residual-J4-Joint-Stone-Hom.md` |
| Joint-Stone-CP-1 (mere CP + Stone \(j=1\) + \(\Phi_0\)) | **OBSTRUCT (J5)** — see `PROGRAM-C-residual-mere-CP-Joint-Stone.md` |
| Unitary-Image-CP-1 (unitary image of \(U(s)\), no SA link) | **OBSTRUCT (J6)** — see `PROGRAM-C-residual-CP-without-Stone.md` |
| Diag-CP-Φ₀ (\(\Phi_0\circ E\) on joint vNa) | **CONSTRUCT (J6-C)** — same note |
| Joint-Form-Core (forms on \(C_c^\infty\) + \(\Phi_0\)) | **CONSTRUCT (J4-F)** |
| Joint-Form-ESS-1 | **OBSTRUCT (J4-E)** |
| Full-\(\psi\) abstract \(C^*\) without Hom/unitary-image | **OPEN** |

J5–J6: unital CP + unitary image of \(e^{is P_1^{\mathrm{Sch}}}\) puts those
unitaries in the multiplicative domain, recovers dual-\(F_1\) Heisenberg
covariance, and dies by SvN / sheet-count geometry (SA-extension-of-\(H_1\)
inessential). Diag-CP-Φ₀ constructs non-Stone CP of \(\Phi_0\) on \(M\).
Remaining open: full-\(\psi\) abstract \(C^*\) envelope.

---

## 4. Scoreboard update

| Pack | Verdict |
|------|---------|
| C0 → C0 composition (vanishing at infinity) | NO-GO |
| Bogoliubov / quasifree CCR | NO-GO |
| Free-Strict-Regular-v2 | WITHDRAWN (false) |
| **Free-Strict-Abstract-Koopman (position sector)** | **CONSTRUCT** (this note) |
| Free-Strict-Abstract-Joint / **Joint-Stone-Canonical** | **NO-GO (J2)** — see `PROGRAM-C-Free-Strict-Abstract-Joint.md` |
| Free-Strict-Abstract-Joint / full-triple Joint-Stone | **NO-GO (J3, G4 companion)** |
| Free-Strict-Abstract-Joint / Joint-Stone-Hom-1 | **NO-GO (J4)** |
| Free-Strict-Abstract-Joint / Joint-Stone-CP-1 | **NO-GO (J5)** |
| Free-Strict-Abstract-Joint / Unitary-Image-CP-1 | **NO-GO (J6)** |
| Free-Strict-Abstract-Joint / Diag-CP-Φ₀ | **CONSTRUCT (J6-C)** |
| Free-Strict-Abstract-Joint / Joint-Form-Core | **CONSTRUCT (J4-F)** |
| Full-\(\psi\) abstract \(C^*\) without Hom/unitary-image | **OPEN** |

---

## 5. Non-claims
No channel on \(B(H)\) implementing the full \(\psi\). No dual-\(F\)
translation dynamics (T4). Joint-Stone-Canonical (J2), full-triple under G4
(J3), multiplicative Joint-Stone-Hom-1 (J4), mere-CP Joint-Stone-CP-1
(J5), and Unitary-Image-CP-1 (J6) are ruled out; Diag-CP-Φ₀ is constructed
and is not a momentum channel. Full-\(\psi\) abstract \(C^*\) is **not**
claimed impossible. Joint-Form-Core is form-level only. \(\Phi_0\) alone does
**not** realize \(\psi\); it realizes only the abelian position-generator part.

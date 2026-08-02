# Program C residual — historical J7 proposals for an abstract \(C^*\) envelope

> **PARKED HISTORICAL RECORD (2026-08-01).** Not an active theorem-development task. Program C / C001 are withdrawn as a current theorem surface. Residuals require a new story and Lean-backed gate to reopen. Current status: [`A001-PROGRAM-CLOSEOUT-FINAL.md`](A001-PROGRAM-CLOSEOUT-FINAL.md).

**Date:** 2026-07-22  
**Status (superseding, 2026-07-29): WITHDRAWN HISTORICAL RECORD — OUTSIDE
THE CURRENT A001 PUBLICATION PACKAGE.** The former Full-\(\psi\)-BT-Envelope
positive theorem is open pending Lean-backed formulation and review. J6-C,
on which parts of this note rely, is withdrawn. No CP or \(C^*\)-completion
construct in this file is a current claim.

**Parent:** `PROGRAM-C-Free-Strict-Abstract-Joint.md`  
**Prior slice:** `PROGRAM-C-residual-CP-without-Stone.md` (J6/J6-C; residual named OPEN)  
**Companion:** C001 (v0.9 cites J7)

---

> **Superseding notice.** The historical CONSTRUCT/OBSTRUCT/Theorem labels
> below are preserved for provenance and must not be cited as current results.

## 0. Scope

The historical J6 campaign claimed a Diag-CP-\(\Phi_0\) construct. J6-C is
now withdrawn; the residual taxonomy below is retained only as history:

> abstract \(C^*\) envelope of the **full** endomorphism \(\psi\) (positions **and** momenta) without Hom / unitary-image axioms.

The historical note split that residual into three named packs. The positive
J7-C branch is now open pending Lean rather than settled:

| Pack | Axioms (sketch) | Verdict |
|------|-----------------|---------|
| **Full-ψ-BT-Envelope** *(preferred expanded label: **Full-ψ-BT-Envelope (bounded dual-momentum transforms + Φ₀ positions)**)* | historical concrete \(C^*\) proposal | **OPEN pending Lean** |
| **Full-ψ-CFC-SA-1** | unital normal CP extending \(\Phi_0\) that recovers **self-adjoint continuous functional calculus** of some \(\widetilde A_1\) for the Schrödinger momentum \(P_1^{\mathrm{Sch}}\) (equivalently: unitary Cayley image) | **OBSTRUCT (J7)** |
| **Full-ψ-CP-Weyl-C\*** | unital CP from some \(C^*\) completion of the polynomial Weyl algebra \(\mathcal{W}\) extending algebraic \(\psi\), **without** SA-CFC / unitary-image axioms on momenta | **OPEN (J7-O)** |

### Historical naming record (former J7-C)

The former proposal used the short label **Full-ψ-BT-Envelope (J7-C)** and
the expanded label **Full-ψ-BT-Envelope (bounded dual-momentum transforms +
Φ₀ positions)**. It was intended as form-level/bounded-transform content,
not as Full-ψ-CFC, Weyl-\(C^*\), Stinespring, a channel, or algebraic full
\(\psi\) on a completed Weyl algebra. These descriptions record the intended
scope of a withdrawn theorem claim; they do not establish that the proposed
envelope exists with the stated operator-theoretic properties.

The historical comparison to Diag-CP-Φ₀ is also nonoperative: J6-C is
withdrawn and supplies no normal CP map. The proposed BT-envelope remains
**OPEN pending Lean** and outside A001.

**Why CFC-SA-1 is the natural NO-GO twin.**  
Any package that upgrades momentum content from “bounded transform of the minimal symmetric operator” to “continuous functional calculus of a self-adjoint operator” (or unitary Cayley image) forces Unitary-Image-CP-1 on the joint algebra and dies by J6. No weakening of J2–J6.

**Why CP-Weyl-C\* remains OPEN (narrow).**  
Existence of a unital CP map out of an abstract \(C^*\) completion of
\(\mathcal{W}\) that extends full algebraic \(\psi\) without
SA-CFC/unitary-image is **not** constructed here and **not** ruled out by
J6/J7. The historical GenCP-Alg and BT-envelope proposals do not provide a
substitute Stinespring channel on \(B(H)\).

**Non-claims.** No Joint-Stone success. No full channel on \(B(H)\). No
gates/advantage. No dual-\(F\) translations (T4). Diag-CP/J6-C is withdrawn,
not relabeled as full-\(\psi\). The historical BT-envelope proposal is open
pending Lean, not relabeled as Weyl-\(C^*\) or Stinespring. No A001
endorsement work. No claim that every abstract CP extension of \(\psi\)
fails.

---

## 1. Standing data

Let \(H=L^2(\mathbb{R}^3)\), \(Q=(Q_0,Q_1,Q_2)\) multiplication by coordinates,
\[
P_j^{\mathrm{Sch}}=-i\partial_{q_j}
\]
(unique SA closure on \(C_c^\infty\)), and \(F=(F_0,F_1,F_2)\) the A001 seed. Dual fields
\[
X_j=\sum_k B_{jk}(q)\,\partial_{q_k},\qquad B=J^{-T},
\]
with \(\operatorname{div} B_{\mathrm{row}\,j}=0\). Minimal dual momenta
\[
H_j=-iX_j\quad\text{on }D:=C_c^\infty(\mathbb{R}^3)
\]
are symmetric; write \(\overline{H_j}\) for the closure. A001 Theorems E–F:
\[
H_1\text{ has }(n_+,n_-)=(\infty,\infty)
\]
(not essentially self-adjoint). **Do not** read A001 as claiming ESS status of \(H_0,H_2\).

**Position sector.** \(\Phi_0(f)=f\circ F\) on \(\mathcal{B}_b(Q)\) (C1d); restricts to a unital \(*\)-homomorphism
\[
\Phi_0:C_b(\mathbb{R}^3)\to C_b(\mathbb{R}^3),\qquad f\mapsto f\circ F
\]
at the bounded-continuous level ( \(F\) continuous).

**Joint-Form-Core (J4-F, reused).** Sesquilinear forms \(\mathfrak{q}_j(u,v)=\langle u,H_j v\rangle\) on \(D\) realize \(\psi(p_j)\) together with \(\Phi_0\).

**Bounded-transform notation used by the historical proposal.** For a closed
densely defined operator \(A\) on \(H\), the former note wrote
\[
Z(A)\;:=\;A\,(I+A^*A)^{-1/2}\;\in\;B(H),
\]
a contraction. The self-adjoint case has the expected self-adjoint bounded
transform. This record makes **no current claim** that the transform of a
merely symmetric non-self-adjoint operator is a bounded symmetric
non-self-adjoint operator, and makes no inference from non-self-adjointness to
nonunitarity. Those assertions from the former J7-C proof are withdrawn
pending a correct Lean-backed formulation.

**Cayley transform (SA case).** For self-adjoint \(A\),
\[
C(A)=(A-i)(A+i)^{-1}
\]
is unitary. Continuous functional calculus identifies \(C^*(C(A),I)\) with continuous functions of \(A\) on the extended real line (point at infinity \(\leftrightarrow -1\)).

---

## 2. Axiom pack **Full-ψ-BT-Envelope** — HISTORICAL / OPEN PENDING LEAN

### 2.1 Historical proposed notation

The former J7-C text proposed
\[
Z_j :=
\overline{H_j}\,\bigl(I+\overline{H_j}^*\overline{H_j}\bigr)^{-1/2}
\]
and \(S_j:=Z(P_j^{\mathrm{Sch}})\) for the corresponding Schrödinger-side
notation, then wrote
\[
\mathfrak{A}_\psi :=
C^*\Bigl(
\bigl\{(f\circ F)(Q):f\in C_b(\mathbb{R}^3)\bigr\}
\cup
\{Z_0,Z_1,Z_2\}
\Bigr)
\subset B(H).
\]
This notation is preserved only to identify the former proposal. It does not
certify the operator-theoretic properties required to interpret these
generators as a bounded \(C^*\) avatar of the unbounded momentum forms.

### 2.2 Withdrawn theorem/proof/corollary block

The former **Theorem J7-C**, its proof, and Corollaries J7.1--J7.3 are
withdrawn as current results. In particular, this artifact does not claim:

1. that the bounded transforms \(Z_j\) are bounded symmetric
   non-self-adjoint operators;
2. that non-self-adjointness of a proposed \(Z_1\) implies nonunitarity;
3. that \(\mathfrak{A}_\psi\) is a proved bounded \(C^*\) avatar recovering
   the Joint-Form-Core momentum forms;
4. that the concrete-envelope existence question is closed; or
5. that the withdrawn Diag-CP-Φ₀/J6-C map is compatible with or complementary
   to this proposal.

The BT-envelope remains **OPEN pending Lean**, outside A001, with no substitute
theorem supplied here.

---

## 3. Axiom pack **Full-ψ-CFC-SA-1** — OBSTRUCT

### 3.1 Definition

Let \(A_1\) be any unital \(C^*\)-algebra of operators on \(H\) containing
\[
\bigl\{f(Q):f\in C_b(\mathbb{R}^3)\bigr\}
\quad\text{and}\quad
C\bigl(P_1^{\mathrm{Sch}}\bigr)
\;=\;
\bigl(P_1^{\mathrm{Sch}}-i\bigr)\bigl(P_1^{\mathrm{Sch}}+i\bigr)^{-1},
\]
or, equivalently, containing the resolvents \((P_1^{\mathrm{Sch}}-\lambda)^{-1}\) for one \(\lambda\notin\mathbb{R}\) (same \(C^*\) by continuous functional calculus). In particular the joint vNa
\[
M=\mathcal{B}_b(Q)\vee\bigl\{e^{is P_1^{\mathrm{Sch}}}:s\in\mathbb{R}\bigr\}''
\]
of J6 contains such a copy (pass to the \(C^*\) generated by \(C_b(Q)\) and \(C(P_1^{\mathrm{Sch}})\)).

**Definition (Full-ψ-CFC-SA-1 package).**  
A unital normal completely positive map
\[
\Phi:A_1\to B(H)
\]
such that:

1. \(\Phi\big|_{C_b(Q)}=\Phi_0\) (agrees with Koopman on positions);
2. **SA continuous functional calculus recovery for \(j=1\):** there exists a self-adjoint operator \(\widetilde A_1\) on \(H\) with
   \[
   \Phi\bigl(f(P_1^{\mathrm{Sch}})\bigr)
   =
   f(\widetilde A_1)
   \qquad\text{for all }f\in C_0(\mathbb{R}),
   \]
   or equivalently (same pack):
   \[
   \Phi\bigl(C(P_1^{\mathrm{Sch}})\bigr)
   =
   C(\widetilde A_1)
   \quad\text{is unitary}.
   \]

**No** requirement that \(\widetilde A_1\supset H_1\) (that would be Joint-Stone-CP-1, already NO-GO by J5). The pack only demands SA-CFC recovery of the Schrödinger momentum generator under \(\Phi\).

**Equivalent Cayley form (Full-ψ-Cayley-Unitary-1).**  
Unital normal CP \(\Phi\) on \(A_1\) with \(\Phi|_{C_b(Q)}=\Phi_0\) and \(\Phi\bigl(C(P_1^{\mathrm{Sch}})\bigr)\) **unitary**.

### 3.2 Lemmas

**Lemma J7.4 (Cayley generates Stone unitaries).**  
There is a continuous functional calculus identity: for every \(s\in\mathbb{R}\),
\[
e^{is P_1^{\mathrm{Sch}}}
=
u_s\bigl(C(P_1^{\mathrm{Sch}})\bigr)
\]
for a continuous function \(u_s\) on the unit circle (with a conventional value at the point corresponding to the point at infinity of the resolvent compactification). Consequently
\[
C^*\bigl(C(P_1^{\mathrm{Sch}}),I\bigr)
=
C^*\bigl(\{e^{is P_1^{\mathrm{Sch}}}:s\in\mathbb{R}\}\bigr).
\]

**Proof.** Standard: Cayley transform intertwines the SA functional calculus on \(\mathbb{R}\cup\{\infty\}\) with continuous functions on \(\mathbb{T}\). Stone unitaries are \(e^{is\,\cdot}\) applied to \(P_1^{\mathrm{Sch}}\). \(\square\)

**Lemma J7.5 (unitary Cayley image \(\Rightarrow\) unitary Stone image).**  
If \(\Phi\) is unital CP and \(V:=\Phi\bigl(C(P_1^{\mathrm{Sch}})\bigr)\) is unitary, then \(C(P_1^{\mathrm{Sch}})\in\mathcal{D}_\Phi\) (multiplicative domain), \(\Phi\) is a \(*\)-homomorphism on \(C^*\bigl(C(P_1^{\mathrm{Sch}}),I\bigr)\), and
\[
\Phi\bigl(e^{is P_1^{\mathrm{Sch}}}\bigr)
=
u_s(V)
\]
is unitary for every \(s\in\mathbb{R}\).

**Proof.** Kadison–Schwarz: \(\Phi(C)^*\Phi(C)\le\Phi(C^*C)=I\). Unitarity of \(V=\Phi(C)\) forces equality, so \(C\in\mathcal{D}_\Phi\). The multiplicative domain is a \(C^*\)-algebra and \(\Phi|_{\mathcal{D}_\Phi}\) is a \(*\)-homomorphism (Paulsen, Thm.~3.18). Apply to \(u_s(C)=e^{is P_1^{\mathrm{Sch}}}\) by continuous functional calculus in the multiplicative domain. \(\square\)

**Lemma J7.6 (CFC-SA-1 \(\Rightarrow\) Unitary-Image-CP-1).**  
Every Full-ψ-CFC-SA-1 package (on \(A_1\), or its normal extension to the vNa \(M\)) restricts to / induces a Unitary-Image-CP-1 package in the sense of J6.

**Proof.** By Lemma J7.5, \(\Phi(e^{is P_1^{\mathrm{Sch}}})\) is unitary for all \(s\). Combined with \(\Phi|_{C_b(Q)}=\Phi_0\) and normality, this is Unitary-Image-CP-1 on the joint algebra generated by positions and \(\{U(s)\}\) (J6 §2). \(\square\)

### 3.2b Hypothesis checklist: CFC-SA-1 lands in the J6 setting

J7 is a **named reduction** to J6, not a free-floating NO-GO. The following checklist is **forced** by the Full-ψ-CFC-SA-1 axioms (Lemmas J7.4–J7.6); each item matches an axiom of **Unitary-Image-CP-1** as stated in

> `docs/validation/PROGRAM-C-residual-CP-without-Stone.md` (J6 §2).

| # | Hypothesis forced by CFC-SA-1 | J6 Unitary-Image-CP-1 match |
|---|------------------------------|-----------------------------|
| H1 | Domain contains \(C_b(Q)\) and the Cayley unitary \(C(P_1^{\mathrm{Sch}})\); by Lemma J7.4 this is the same \(C^*\) as \(C^*(\{e^{is P_1^{\mathrm{Sch}}}\})\). Normal extension lands in the joint vNa \(M=\mathcal{B}_b(Q)\vee\{U(s)\}''\) of J6. | Same joint vNa \(M\) (positions + Schrödinger Stone unitaries) |
| H2 | \(\Phi\) is **unital** and **completely positive** | Same |
| H3 | \(\Phi\) is **normal** (vNa / normal extension reading) | Same |
| H4 | \(\Phi\big|_{C_b(Q)}=\Phi_0\) (Koopman on positions) | Same \(\Phi|_{\mathcal{B}_b(Q)}=\Phi_0\) |
| H5 | SA-CFC recovery \(\Leftrightarrow\) \(\Phi(C(P_1^{\mathrm{Sch}}))\) **unitary** (pack definition) | — |
| H6 | Lemma J7.5: unitary Cayley image \(\Rightarrow\) \(C\in\mathcal{D}_\Phi\) \(\Rightarrow\) \(\Phi\) is a \(*\)-hom on \(C^*(C,I)\) \(\Rightarrow\) \(\Phi(e^{is P_1^{\mathrm{Sch}}})=u_s(\Phi(C))\) is **unitary** for all \(s\) | \(\Phi(U(s))\) **unitary** for all \(s\) |
| H7 | **No** \(\widetilde H_1\supset H_1\) required (CFC-SA-1 omits dual-field SA link) | Unitary-Image-CP-1 also omits SA-extension-of-\(H_1\) |

**Conclusion of checklist.** Under H1–H7, every Full-ψ-CFC-SA-1 package induces a Unitary-Image-CP-1 package on the **same** joint vNa + normal CP setting as J6. Therefore Theorem J6 applies verbatim:

> **Theorem J6** (no Unitary-Image-CP-1): `docs/validation/PROGRAM-C-residual-CP-without-Stone.md`.

No extra geometric input is needed beyond J6; J7 does not weaken J6’s hypotheses.

### 3.3 Theorem J7

**Theorem J7 (No Full-ψ-CFC-SA-1 package).**  
There is **no** Full-ψ-CFC-SA-1 package for the A001 dual-lift data. Equivalently: there is no Full-ψ-Cayley-Unitary-1 package.

**Proof.**  
Assume \(\Phi\) is Full-ψ-CFC-SA-1. By the checklist §3.2b and Lemma J7.6 it yields a Unitary-Image-CP-1 package on the joint vNa \(M\) in the sense of J6 §2. Theorem J6 (`PROGRAM-C-residual-CP-without-Stone.md`) says no such package exists. \(\square\)

**Corollary J7.7 (SA-CFC is the kill switch).**  
Any attempt to upgrade the momentum sector of a full-\(\psi\) envelope from “bounded transform of the **minimal** symmetric operator” (J7-C) to “continuous functional calculus of a **self-adjoint** operator” (or unitary Cayley image), while keeping unital normal CP and \(\Phi_0\), is obstructed by J6 geometry. The dual-field SA-extension link is inessential (same as J6 vs J5).

**Corollary J7.8 (no weakening of J2–J6).**  
J7 is a **named specialization** of the unitary-image obstruction to the full-\(\psi\) / CFC language. Joint-Stone-Hom-1 (J4), Joint-Stone-CP-1 (J5), and Unitary-Image-CP-1 (J6) remain NO-GO on their own axioms.

**Explicit non-claim of J7.**  
J7 does **not** rule out:

1. the former Full-ψ-BT-Envelope proposal (J7-C), now **OPEN pending Lean**;
2. the withdrawn Diag-CP-Φ₀ proposal (J6-C), which supplies no operative map;
3. Joint-Form-Core (J4-F) — forms only;
4. unital CP maps that send \(C(P_1^{\mathrm{Sch}})\) to a **non-unitary** contraction (e.g. partial Cayley of \(\overline{H_1}\), or \(0\));
5. Full-ψ-CP-Weyl-C\* without SA-CFC axioms (J7-O).

---

## 4. Axiom pack **Full-ψ-CP-Weyl-C\*** — OPEN (narrowed)

### 4.1 Definition

**Definition (Full-ψ-CP-Weyl-C\* package).**  
A pair \((A,\Phi)\) where:

1. \(A\) is a unital \(C^*\)-algebra containing a unital \(*\)-homomorphic copy of the polynomial Weyl algebra \(\mathcal{W}\) as a dense \(*\)-subalgebra (a \(C^*\) completion of \(\mathcal{W}\) in some \(C^*\)-seminorm compatible with the involution);
2. \(\Phi:A\to B(H)\) is unital completely positive;
3. \(\Phi|_{\mathcal{W}}=\pi\circ\psi\) for the Schrödinger representation \(\pi\) of \(\mathcal{W}\) on \(H\) (i.e. \(\Phi\) extends the full algebraic endomorphism at the represented level);
4. **Explicitly omitted axioms:**  
   - \(\Phi\) need **not** be a \(*\)-homomorphism on \(A\);  
   - \(\Phi\) need **not** send Stone unitaries / Cayley transforms of \(P_j^{\mathrm{Sch}}\) to unitaries;  
   - \(\Phi\) need **not** recover SA continuous functional calculus of any extension of \(H_j\).

### 4.2 Status

| Question | Status |
|----------|--------|
| Existence of some Full-ψ-CP-Weyl-C\* package | **OPEN** |
| Stinespring dilation of such a \(\Phi\) as a physical channel on \(B(H)\) | **not claimed**; channel language forbidden |
| Algebraic endomorphism correspondence (GenCP-Alg) | **CONSTRUCT** (prior) |
| BT-Envelope as concrete image-side \(C^*\) | **OPEN pending Lean** |
| “No CP extension of \(\psi\) exists in any sense” | **not authorized** |

**Partial structural remarks (not a close).**

1. **GenCP-Alg** already supplies an algebraic Hilbert \(\mathcal{W}\)-module correspondence implementing \(\psi\). Promoting it to a \(C^*\)-correspondence requires a \(C^*\) norm on \(\mathcal{W}\) for which \(\psi\) is completely contractive. No such completion is selected or ruled out here.
2. **Arveson** can supply CP extensions of bounded operator-system
   restrictions under its usual hypotheses, but it neither resolves the
   unbounded-generator domain nor automatically supplies normality. It does
   not recover the withdrawn Diag-CP/J6-C map.
3. **J7** kills the SA-CFC upgrade path; it does **not** kill non-SA / non-unitary-image CP extensions of full algebraic \(\psi\).
4. A natural **candidate bridge** (not claimed): a unital CP map on \(C^*\bigl(C_b(Q),\{S_j\}\bigr)\) with \(\Phi(f(Q))=(f\circ F)(Q)\) and \(\Phi(S_j)=Z_j\). Consistency with Heisenberg relations between \(S_j\) and \(Q\) is obstructed at the **homomorphism** level by J4-type geometry; at the **mere CP** level it is not settled here. Record as sub-residual **Full-ψ-BT-CP-Bridge** \(\subset\) J7-O.

---

## 5. What remains after J7

| Pack | Verdict | Anchor |
|------|---------|--------|
| Joint-Stone-Hom-1 | **OBSTRUCT** | J4 |
| Joint-Stone-CP-1 | **OBSTRUCT** | J5 |
| Unitary-Image-CP-1 | **OBSTRUCT** | J6 |
| Diag-CP-Φ₀ | **WITHDRAWN** | J6-C invalid as stated |
| Joint-Form-Core | **CONSTRUCT** | J4-F |
| Joint-Form-ESS-1 | **OBSTRUCT** | J4-E |
| **Full-ψ-BT-Envelope** (bounded dual-momentum transforms + Φ₀ positions) | **OPEN pending Lean** | former J7-C |
| **Full-ψ-CFC-SA-1** / Cayley-Unitary-1 (reduces to J6 via §3.2b checklist) | **OBSTRUCT** | **J7** |
| **Full-ψ-CP-Weyl-C\*** (CP from a completion of \(\mathcal{W}\), no SA-CFC) | **OPEN** | **J7-O** |
| Full-ψ-BT-CP-Bridge (CP with \(\Phi(S_j)=Z_j\)) | **OPEN** | sub of J7-O |

**Reading.**  
The former residual “abstract \(C^*\) of full \(\psi\) without Hom/unitary-image” **splits**:

- **concrete envelope** reading → **OPEN pending Lean** (former J7-C proposal);
- **SA-CFC / unitary Cayley recovery** reading → **closed NO-GO (J7)** via J6;
- **CP from a Weyl \(C^*\) completion without SA-CFC** → still **OPEN (J7-O)**, strictly narrower than the pre-J7 blob.

---

## 6. Scoreboard delta

| Pack | Before J7 | After J7 |
|------|-----------|----------|
| Full-\(\psi\) abstract \(C^*\) (undifferentiated) | OPEN | **SPLIT** (see §5) |
| Full-ψ-BT-Envelope | (unnamed) | **OPEN pending Lean** |
| Full-ψ-CFC-SA-1 | (unnamed part of residual) | **OBSTRUCT (J7)** |
| Full-ψ-CP-Weyl-C\* | (unnamed) | **OPEN (J7-O)** |
| Unitary-Image-CP-1 | OBSTRUCT (J6) | OBSTRUCT (J6) — unchanged |
| Diag-CP-Φ₀ | historical CONSTRUCT (J6-C) | **WITHDRAWN** |

---

## 7. Non-claims

1. No claim that all CP extensions of full \(\psi\) fail — only Full-ψ-CFC-SA-1 / Cayley-Unitary-1 (and the prior Joint-Stone / Unitary-Image packs J2–J6).  
2. The historical Full-ψ-BT-Envelope proposal remains **OPEN pending Lean**;
   it is not a current quantum channel, Stinespring instrument, gate,
   Full-ψ-CFC, Weyl-\(C^*\), or Full-ψ-CP-Weyl-C\* theorem.
3. Diag-CP-Φ₀/J6-C is withdrawn and supplies no map to relabel as
   full-\(\psi\).
4. No dual-\(F\) translation dynamics (T4).  
5. Historical G4 \(H_0/H_2\) pairs and J3 are withdrawn; the full-triple question is open pending Lean.
6. No A001 endorsement work.  
7. J7 does **not** weaken J2–J6: those packs remain NO-GO on their stated axioms; J7 names the CFC-SA specialization and reduces to J6 via the §3.2b checklist on the same joint vNa + normal CP setting (`PROGRAM-C-residual-CP-without-Stone.md`).  
8. No claim that this proves the Jacobian conjecture or global quantization failure.  
9. Bounded-transform and multiplicative-domain ingredients are standard; the geometric kill inside J7 is inherited from J6/J4 (A001 sheet-count variation).

---

## 8. CAS path

No new numeric CAS required.  
- A001 deficiency \((n_+,n_-)=(\infty,\infty)\) for \(H_1\): inherited.  
- Sheet-count geometry J4.4–J4.5: inherited (used inside J6, cited by J7).  
- Bounded-transform SA equivalence: structural (operator theory), not numeric.

---

## 9. Pointers

| Item | Path |
|------|------|
| Parent joint note | `PROGRAM-C-Free-Strict-Abstract-Joint.md` |
| J6 CP without Stone | `PROGRAM-C-residual-CP-without-Stone.md` |
| J5 mere-CP + Stone | `PROGRAM-C-residual-mere-CP-Joint-Stone.md` |
| J4 Hom + geometry | `PROGRAM-C-residual-J4-Joint-Stone-Hom.md` |
| Joint-Form-Core | J4 residual §6 |
| Koopman position | `PROGRAM-C-C1d-Koopman-position.md` |
| GenCP-Free charter | `PROGRAM-C-GenCP.md`, `PROGRAM-C-GenCP-Free-Strict.md` |
| Multiplicative domain | Paulsen, *CB maps*, Thm.~3.18 |
| Bounded transform | standard; cf. Reed–Simon II; Kaufmann |
| Resolvent algebra (context only) | Buchholz–Grundling, JFA 2008 |
| C001 companion | `docs/notes/C001-cp-correspondence-arxiv.tex` |

(End of file)

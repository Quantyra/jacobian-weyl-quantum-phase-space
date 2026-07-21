# G4 Extension taxonomy for \(H_1=-iX_1\) (A001)

**Date:** 2026-07-21  
**Status:** **Structured taxonomy** (not a full spectral classification)  
**Input:** \((n_+,n_-)=(\infty,\infty)\) (`G4-P1-orbit-measure-deficiency.md`)

---

## 1. von Neumann picture

Since \(n_+=n_-=\infty\), the self-adjoint extensions of the closure of \(H_1\) are parameterized by unitary maps
\[
U:\overline{\operatorname{ran}}(H_1^*-i)
\to
\overline{\operatorname{ran}}(H_1^*+i)
\]
(unitaries between the two infinite-dimensional deficiency spaces), or equivalently by Lagrangian relations in the boundary form sense (half-line models glued over the orbit space).

**No extension is selected by the polynomial CCR/Poisson data.**

---

## 2. Geometric classes of boundary conditions

Using flow-box coordinates \((a,s,c)=F(q)\) on saturated incomplete sheets:

| Class | Description | Notes |
|-------|-------------|--------|
| **Dirichlet-type at walls** | Kill boundary values of deficiency components at finite \(s\)-ends | Separable over orbits |
| **Robin/phase at walls** | Orbitwise \(U(1)\) phase between in/out deficiency data | Still product over orbits |
| **Mixing / nonlocal** | Unitary mixing different \((a,c)\) orbits | True infinite-dimensional freedom |
| **Disconnected ends** | Treat forward and backward walls independently then couple | Natural for \((\infty,\infty)\) |

---

## 3. What we do **not** compute here

- Explicit spectra for a chosen \(U\)  
- Ground state / dynamics for a “physical” pick  
- Preferred \(U\) from variational principles  

Those are optional Phase 1C stretch items.

---

## 4. Relation to strong CCR

Even after picking \(\widetilde H_1\), joint Weyl relations with extensions of \(H_0,H_2\) face the obstruction in `G4-strong-CCR-extensions-A001.md`.

---

## 5. Non-claims
No preferred physical extension. No gate/channel.

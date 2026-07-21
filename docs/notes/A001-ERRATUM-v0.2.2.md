# Erratum — release v0.2.2

**Date:** 2026-07-21  
**Affects:** Zenodo `10.5281/zenodo.21476665`, GitHub tag `v0.2.2`, draft claims of \((n_+,n_-)=(0,\infty)\).  
**Corrected in:** **v0.3.0**

## Withdrawn claim
Global deficiency indices of \(H=-iX_1\) on \(C_c^\infty(\mathbb{R}^3)\):
\[
(n_+,n_-)=(0,\infty)\qquad\text{(v0.2.2 — incorrect)}.
\]

## Reason
An open transverse family of **backward-incomplete** orbits exists near \((F_0,F_2)=(\tfrac1{54},2)\), giving finite **lower** \(F_1\)-ends and \(n_+=\infty\). Combined with the forward-incomplete family near \((0,2)\),
\[
(n_+,n_-)=(\infty,\infty).
\]
Evidence: `docs/validation/G4-P1-orbit-measure-deficiency.md`, `data/anchor/cas_backward_incomplete_wall_A001.json`.

## Consequences
- von Neumann: self-adjoint extensions **exist** (infinitely many), not “none.”  
- v0.2.2 text already said extensions “may exist” — inconsistent with \((0,\infty)\); corrected package is coherent.  
- Theorems A–D unchanged. Theorem E remains true (non-ESS) with a shorter proof via deficiency vectors.

## Cite
Prefer **v0.3.0** / concept DOI `10.5281/zenodo.21474351` over the frozen v0.2.2 pair claim.

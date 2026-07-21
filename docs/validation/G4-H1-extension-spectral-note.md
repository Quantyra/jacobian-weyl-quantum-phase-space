# G4 \(H_1\) extension class + sample spectral note (A001)

**Date:** 2026-07-21  
**Status:** **Concrete product extension class** + model spectrum  
**Input:** \((n_+,n_-)=(\infty,\infty)\); taxonomy in `G4-H1-extension-taxonomy.md`

---

## 1. Product Dirichlet class (concrete choice)

On each saturated incomplete \(X_1\)-orbit with half-line type (after \(F_1\)-time reparameterization to \((0,\infty)\) at a finite end, or \((-\infty,0)\)), impose the **Dirichlet** boundary condition at the finite end in the 1D model
\[
b=-i\frac{d}{dx}
\quad\text{on}\quad
C_c^\infty(0,\infty)
\;\longrightarrow\;
\text{Dirichlet at }0
\]
in the sense of the unique self-adjoint extension corresponding to the limit-circle endpoint with vanishing boundary value in the Weyl–Titchmarsh classification for first-order systems (equivalently: the extension whose deficiency coupling is the standard “hard wall” unitary on each fiber).

**Global operator \(H_1^{\mathrm{Dir}}\):**  
direct integral / product over the transverse orbit space of these 1D Dirichlet extensions (measurable field of boundary conditions constant on fibers).  
This is a well-defined self-adjoint operator on \(L^2(\mathbb{R}^3)\) reducing the minimal \(H_1\).

**Why this class:** separable, canonical, no orbit-mixing; implements “kill amplitude at the incomplete end” fiberwise.

---

## 2. Sample spectrum (1D fiber)

For the model half-line operator equivalent to momentum on \((0,\infty)\) with Dirichlet-type fixing at \(0\), the spectrum of the self-adjoint extension is
\[
\sigma(b_{\mathrm{Dir}})=\mathbb{R}
\]
(absolutely continuous, multiplicity one) — standard for first-order momentum on a half-line after boundary condition (cf. Reed–Simon II, half-line models).

**Global sample conclusion:**  
\[
\sigma(H_1^{\mathrm{Dir}})=\mathbb{R}
\]
with infinite multiplicity coming from the continuous transverse orbit family (direct integral of \(\mathbb{R}\) over a positive-measure base).

---

## 3. What this does *not* give

| Item | Status |
|------|--------|
| Preferred physical extension | **not claimed** (Dirichlet is a choice) |
| Joint Weyl with \(H_0,H_2\) | **impossible** for dual-flow package (\(H_0,H_2\) have no SA extensions; CCR obstructed) |
| Discrete “energy levels” | not expected for pure first-order \(H_1^{\mathrm{Dir}}\) |
| Gate/channel | **forbidden** |

---

## 4. Non-claims
Dirichlet product is an **example**, not *the* quantization. No computational interpretation.

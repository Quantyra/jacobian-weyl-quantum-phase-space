# G4 Theorem: incompleteness of some dual field \(X_j\) (A001)

**Status:** **PROVED** (existential over \(j\in\{0,1,2\}\))  
**Date:** 2026-07-21  
**Atlas:** A001-seed-d3

## Setup
Let \(F:\mathbb{R}^3\to\mathbb{R}^3\) be the A001 seed map (G0). Let \(J=DF\). By G0 dual CAS / Lean,
\[
\det J \equiv -2 \neq 0
\]
everywhere, so \(F\) is a smooth **local diffeomorphism**. Let \(B=J^{-T}\) and
\[
X_j
=
\sum_{k=0}^{2}
B_{jk}(q)\,
\partial_{q_k}
\qquad (j=0,1,2).
\]
The coefficient vector of \(X_j\) is the \(j\)-th column of \(J^{-1}=B^{T}\), hence
\[
DF_q\bigl(X_j(q)\bigr)
=
e_j
\qquad
\forall q\in\mathbb{R}^3.
\]
(G3: \(\mathrm{div}\,X_j=0\).)

## Auxiliary fact (omitted values)
Over \(\mathbb{C}\), the preprint identifies an omitted set \(\Gamma\subset\mathbb{C}^3\) with
\[
F(\mathbb{C}^3)=\mathbb{C}^3\setminus\Gamma,
\]
and
\[
\Gamma \supset V(12p-q^2,\, 3qr-4)
\]
(in target coordinates \((p,q,r)\)). In particular the **real** point
\[
\gamma_\star
=
\Bigl(\frac1{12},\, 1,\, \frac4{3}\Bigr)
\]
lies on that real curve (since \(12\cdot\frac1{12}-1^2=0\) and \(3\cdot 1\cdot\frac4{3}-4=0\)).

**Lemma A (real non-surjectivity).**  
\(\gamma_\star\notin F(\mathbb{R}^3)\).  

**Proof.** If \(F(q)=\gamma_\star\) for some \(q\in\mathbb{R}^3\subset\mathbb{C}^3\), then \(\gamma_\star\in F(\mathbb{C}^3)\), contradicting \(\gamma_\star\in\Gamma\).  
**CAS check:** `sympy.solve(F(q)-γ_*, q)` returns **no** affine solutions (report note below), consistent with the complex omission. ∎

Independent of the full complex classification, non-surjectivity of \(F:\mathbb{R}^3\to\mathbb{R}^3\) also follows once any omitted real point is known; we use \(\gamma_\star\).

## Main theorem
**Theorem (dual-field incompleteness).**  
At least one of the dual fields \(X_0,X_1,X_2\) is **incomplete** on \(\mathbb{R}^3\): some maximal integral curve is not defined for all time in \(\mathbb{R}\).

**Proof.**  
Suppose, for contradiction, that **every** \(X_j\) is complete. Fix \(j\) and \(q\in\mathbb{R}^3\). Let \(\phi_t^{(j)}(q)\) be the global flow of \(X_j\). Then
\[
\frac{d}{dt} F\bigl(\phi_t^{(j)}(q)\bigr)
=
DF\cdot X_j
=
e_j,
\]
so
\[
F\bigl(\phi_t^{(j)}(q)\bigr)
=
F(q)+t\, e_j
\qquad
\forall t\in\mathbb{R}.
\]
Hence for the open nonempty set \(U:=F(\mathbb{R}^3)\),
\[
U+\mathbb{R}\, e_j \subset U
\qquad (j=0,1,2).
\]
Iterating translations in the three coordinate directions yields
\[
U+\mathbb{R}^3 \subset U.
\]
Since \(U\neq\emptyset\), this forces \(U=\mathbb{R}^3\). But Lemma A says \(\gamma_\star\notin U\), contradiction.  

Therefore the assumption is false: some \(X_j\) is incomplete. ∎

## Remarks
1. The argument does **not** identify which \(j\) is incomplete. Numeric probes suggest \(X_1\) (and others) blow up; that is supplementary, not required for the theorem.  
2. Completeness of all three dual fields would force surjectivity of any local diffeomorphism \(F:\mathbb{R}^n\to\mathbb{R}^n\) admitting global dual fields with \(DF\cdot X_j=e_j\). Non-surjective Keller maps on \(\mathbb{R}^n\) always have some incomplete dual field.  
3. **CAS support file:** running SymPy solve for \(F(q)=\gamma_\star\) yields \(0\) solutions; det identity from G0.

## Script anchor
Optional verification snippet is embedded in `scripts/cas/verify_incompleteness_geometry_A001.py`.

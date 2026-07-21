# G2 Poisson pilot — atlas A001-seed-d3

**Status:** CLOSED (A001 pilot)  
**Date:** 2026-07-21  
**Story:** S017  
**Map:** seed \(F\) (G0-seed certified)

## 1. Definition
\[
\Phi(q,p)=\bigl(F(q),\, B(q)\,p\bigr),\qquad
B(q)=J(q)^{-T},\quad J=DF,\quad \det J=-2.
\]
Machine freeze: [`data/anchor/Phi_A001_seed_d3.json`](../../data/anchor/Phi_A001_seed_d3.json) (expanded \(B\)).

## 2. Results (dual CAS)

| Check | SymPy | Pure-Python dual |
|-------|-------|------------------|
| \(\det J=-2\) | PASS | 40/40 samples |
| \(B\) polynomial | PASS | via \(J^{-T}\) at samples |
| \(J B^{T}=I\) | PASS | 40/40 |
| \(\{Q_i,Q_j\}=0\) | PASS (global identity) | 40/40 |
| \(\{Q_i,P_j\}=\delta_{ij}\) | PASS | 40/40 |
| \(\{P_i,P_j\}=0\) | PASS | 40/40 |
| Non-injectivity lift | PASS | PASS |

Reports:
- `data/anchor/cas_poisson_A001_sympy_report.json`
- `data/anchor/cas_poisson_A001_purepython_report.json`

Reproduce:
```text
python scripts/cas/verify_poisson_A001_sympy.py
python scripts/cas/verify_poisson_A001_purepython.py
```

## 3. Non-injectivity lift
Seed collisions \(F(q^{(a)})=Q_\star=(-1/4,0,0)\) for three distinct \(q^{(a)}\).  
Fix \(P_\star=(1,0,0)\). Set \(p^{(a)}=J(q^{(a)})^{T} P_\star\). Then
\[
B(q^{(a)})p^{(a)}=P_\star,\qquad
\Phi(q^{(a)},p^{(a)})=(Q_\star,P_\star)
\]
for all three \(a\), with distinct sources. Hence \(\Phi\) is not injective (and not an automorphism).

## 4. Generic degree \(\mu(\Phi)\) (partial)
On the open set where \(F\) is a degree-3 étale cover of its image (seed \(\mu(F)=3\)), each preimage \(q\) of a generic \(Q\) determines a **unique** \(p=J(q)^{T}P\). Therefore
\[
\#\Phi^{-1}(Q,P)=\#F^{-1}(Q)=3
\]
generically. Full proof that \(\mu(\Phi)=3\) as a dominant map \(\mathbb{C}^{6}\to\mathbb{C}^{6}\) is not expanded beyond this fiberwise argument in the CAS package (accepted as **partial** for G2 pilot).

## 5. Claims ledger

| ID | Statement | Status |
|----|-----------|--------|
| G2-A001-def | \(\Phi=(F,J^{-T}p)\) polynomial | **certified** |
| G2-A001-Poisson | canonical Poisson brackets on generators | **certified** (dual CAS) |
| G2-A001-proper | not injective / not auto | **certified** (lifted collision) |
| G2-A001-mu | \(\mu(\Phi)=3\) | **partial** (fiberwise from \(\mu(F)=3\)) |
| Weyl / physical | — | **not claimed** |
| A002 | — | **not in this pilot** |

## 6. Non-claims
- Classical Poisson geometry on \(T^*\mathbb{A}^{3}\) only.
- No Weyl algebra, CCR, channel, gate, or advantage language.
- No “factory false” claim.
- A002 family d=4 Poisson lift not certified here.

## 7. Next
- Optional: same package for A002  
- G3: Weyl substitution along \(B\)  
- Strengthen \(\mu(\Phi)\) if needed for publication

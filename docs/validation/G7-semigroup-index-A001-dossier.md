# G7 Composition, iteration, index, entropy — program synthesis

**Status:** CLOSED as **synthesis + roadmap** (ladder G deferred)  
**Date:** 2026-07-21  
**Story:** S023

## Algebraic semigroup (certified ingredients)
- Atlas A001 (\(d=3\)), A002 pilot (\(d=4\)) with Cor 5.3 recipe for general \(d\).  
- Composition of Keller maps: \(\mu(F\circ G)=\mu(F)\mu(G)\), \(\det J_{F\circ G}=(\det JF)(\det JG)\).  
- Cotangent lifts: \(\Phi_{F\circ G}=\Phi_F\circ\Phi_G\) (standard; A001 \(\Phi\) certified).  
- Iterates: \(\mu(F^{\circ k})=d^k\), candidate \(h_{\mathrm{alg}}=\log d\).

## Quantum lift of the semigroup
Weyl \(\psi_F\) from G3 for A001; family \(\psi_{F_d}\) for general \(d\) **schema-only** (pilot d=4 at G0-family, not full G3).  
Composition of Weyl endomorphisms corresponds to composition of maps when lifts are functorial — **not fully CAS-certified for family**.

## Index / entropy
| Object | Status |
|--------|--------|
| \(h_{\mathrm{alg}}=\log d\) | classical combinatorial invariant of atlas rows |
| Operator-algebraic entropy / index | **not computed**; requires G5 inclusion |
| Hypothesis: \(d\) = quantized defect | **open**; G4–G5 blocked |

## Continuous-time no-go (heuristic → semi-formal)
Integer-valued multiplicative \(\mu\) cannot connect continuously from \(\mathrm{id}\) (\(\mu=1\)) to \(d>1\) in a continuous family of generically finite polynomial maps. ⇒ nontrivial family members are **not** Hamiltonian flows through the identity.  
**Status:** heuristic solidified as **program principle**; not a theorem about all smooth paths in \(\mathrm{Diff}\).

## Computational primitive (ladder G)
**Not authorized.** No finite-energy protocol, no complexity claim.

## Program synthesis (A001 spine)
| Gate | Result |
|------|--------|
| G0 | Seed + d=4 pilot algebraic |
| G1 | Atlas A001/A002 |
| G2 | Classical Poisson \(\Phi\) certified |
| G3 | Polynomial Weyl \(\psi\) certified |
| G4 | Formal symmetry; ESS/strong CCR **open** with obstruction routes |
| G5 | Trichotomy; index **open** |
| G6 | Not a reversible channel/auto |
| G7 | Semigroup classical; quantum index **open** |

**Minimum publishable narrative (achieved as package):**  
Exact classical+Weyl endomorphisms for the seed counterexample, with a clear **no-go boundary** against uncritical physical/reversible readings, and a degree-indexed atlas for future work.

## Non-claims
No completed G5 index theorem; no G7 entropy theorem; no experimental claim.

# A001 external LLM review log

**Date:** 2026-07-21  
**Inputs:** Grok, Claude, ChatGPT Pro (hostile referee template)  
**Response:** REVISE → manuscript `v0.3.4-submit` (H₁-only, expanded)

## Aggregate verdict
| Model | Verdict | Primary pressure |
|-------|---------|------------------|
| Grok | REVISE | Self-contained walls, volume factor, Dom(H*), asymptotics, CAS pointers |
| Claude | (algebra OK; JC attribution flag) | Verify cubic/escape; stable citation for seed |
| ChatGPT | REVISE | Version coherence; strip H0/H2 + broad no-go from Discussion; expand PDF |

## Fixes applied in v0.3.4-submit
1. **H₁-only scope** — removed theorem-level H0/H2 pairs and dual-flow strong CCR no-go from body/Discussion.  
2. **Expanded analytic core** — explicit curve; volume factor from \(|\det DF|\); wall IFT + smooth \(G_\pm\) at \(\tau=0\); escape \(\|q\|\ge C/\sqrt{\cdot}\); saturation lemma; full Dom(H*) Fubini/IBP + lateral \(\chi=0\); injectivity for \(n_\pm=\infty\).  
3. **Weyl endomorphism** — Theorem C(3) defines \(\psi\) on generators + universal property.  
4. **CAS pointers** — JSON paths in wall proofs.  
5. **Bibliography** — RS2, Dixmier, Lee, Bass–Connell–Wright, seed provenance + software/Lean.  
6. **Version pin** — software line `v0.3.4-submit` (not silent claim inflation on v0.3.3).  
7. **Errata front matter** — states what this note does *not* claim.

## Deferred / companion only
- Exact global pairs for \(H_0,H_2\) (need global orbit classification).  
- Dual-flow / H4 no-gos as paper theorems.  
- Full JC priority discussion beyond Remark under Theorem A.

## Round 2 (v0.3.4 → v0.3.5-submit)
| Model | Verdict |
|-------|---------|
| Grok | PASS |
| ChatGPT | REVISE (backward wall, Weyl norm, provenance, package sync) |
| Claude | REVISE minor (Dom ℓ=-∞ decay; Weyl direct commutators; cites) |

### Round-2 fixes
1. Full backward \(G_-\) + escape/denominator bounds (not “analogously”).  
2. Dom(H*): escape upper; finite lower escape; \(\ell=-\infty\) exponential decay.  
3. Weyl: abstract \([q,p]=\delta\) vs Schrödinger \(p=-i\partial\); direct \([\psi(q),\psi(p)]\) proof.  
4. Saturation: maximal-flow domain pullback + \(F\circ\Psi=\mathrm{id}\).  
5. Softened novelty; stable seed cites (Alpöge X, Ulam PDF, Speyer).  
6. Synced packet/endorsement/README/brief to v0.3.5-submit H₁-only.

## Next
Dan skims PDF → arXiv start submit.

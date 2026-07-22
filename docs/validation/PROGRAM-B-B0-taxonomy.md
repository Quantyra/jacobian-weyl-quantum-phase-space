# Program B — B0 taxonomy (frozen draft)

**Date:** 2026-07-21  
**Status:** frozen for Paper B skeleton  
**Paper:** `docs/notes/B001-classification-arxiv.tex`

## Input axes
1. Surjectivity of \(F\) over \(\mathbb{R}^n\)  
2. Regularity (polynomial / smooth / analytic)  
3. Existence of global dual fields \(X_j\) with \(DF X_j=e_j\), div-free  
4. Target package: incompleteness / ESS / deficiency / strong CCR / CP  

## Coarse bins
| Bin | Typical outcome | Schema |
|-----|-----------------|--------|
| Non-surjective + dual fields | some \(X_j\) incomplete (B1) | `b_incomplete=fail` |
| A001-like all-\(j\) incomplete + deficiency | ESS fail; indices known for some \(j\) | `b_ess=fail`, `b_def=...` |
| Surjective + dual fields | B1 silent; standard ESS possible | may `pass` incompleteness |
| No dual fields | out of dual-lift class | n/a |

## Atlas columns (`program_b`)
`b_incomplete`, `b_ess`, `b_def`, `b_ccr`, `b_cp` ∈ {open,fail,pass} (+ evidence[])

## Rows seeded
| ID | b_incomplete | notes |
|----|--------------|-------|
| A000-toy identity | pass | surjective toy |
| A001-seed-d3 | fail | all \(X_j\) incomplete; H1 (∞,∞) |
| A002-family-d4 | open | conditional on real geometry |

## Next
B3 deepen non-A001; fill more atlas rows; expand B001 TeX.

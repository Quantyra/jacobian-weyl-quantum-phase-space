# A001 publication checklist (`v0.3.9-referee-revision`, proposed and untagged)

**Status:** SCIENTIFIC REVISION — prior technical PASS is superseded; fresh
math.FA, math.AG, Lean/build, non-claims, and package review pending.

PDF: `docs/notes/A001-arxiv.pdf`  
Tag/release: none
Scope: **specific canonical \(H=-iX_1\) only**

## Targeted revision

- [x] Weak-adjoint proof dominates both the test-function and transport
  pairings.
- [x] Fiber-first Fubini, compact-subinterval integration by parts, endpoint
  exhaustion, escape/decay alternatives, and dominated convergence are
  explicit.
- [x] No measurable lower-endpoint selection and no interior \(s\)-indicator.
- [x] Cross-orbit injectivity uses invariance of \(F_0,F_2\).
- [x] Transverse cutoffs satisfy
  \(\operatorname{supp}\chi\Subset W_+\).
- [x] Finite sheet-boundary alternatives are addressed before zero extension.
- [x] The uniform-collar norm lower bound makes cutoff injectivity explicit.
- [x] The Lean-backed sign involution is the main \(+i\) route.
- [x] Backward-wall material is labeled independent geometry and is not used
  for Theorem F.
- [x] Theorem F states \(n_+=n_-=\aleph_0\), with conventional
  \((\infty,\infty)\) notation.
- [x] Real-versus-complex seed scope and the collision/noncollision dependency
  boundary are explicit.
- [x] Dixmier directions are stated accurately:
  \(\mathrm{DC}_n\Rightarrow\mathrm{JC}_n\) and
  \(\mathrm{JC}_{2n}\Rightarrow\mathrm{DC}_n\), with no new rank-three
  consequence claimed.
- [x] AFP/Akhil Mathew attribution and current nonproperness/graded-map
  literature are cited.
- [x] README UTF-8 corruption repaired.
- [x] Paper-package and Lean-source version streams are separated.
- [x] Prior errata and non-claims retained.

## Lean boundary

- Theorem-source root:
  `ff50f4a2a312591c2e5b26e71eb390ade9164b34`.
- Synchronized repository snapshot:
  `94351f38d7d84fd073db14ff8764708fa9d2942b`.
- These are not one final immutable freeze.
- [ ] Produce a new single-SHA Lean freeze with synchronized documentation.
- [ ] Record clean `lake exe cache get` and `lake build` at that SHA.
- [ ] Record headline-theorem axiom output in CI/provenance.

The existing Lean results remain bounded to the specific `H_X1_min`:
`ExoticCCR.theoremE`, `ExoticCCR.theoremF`,
`hilbertDeficiencyIndex_X1_eq_aleph0`,
`theoremFVonNeumannClassification`, and
`theoremF_exists_two_distinct_selfAdjointExtensions`. No preferred extension,
arbitrary-operator classification, exact Hamel rank, exact extension
cardinality, strong CCR, physical selection, or paper backward-wall
formalization is asserted.

## Fresh mandatory gate

- [ ] math.FA/operator-theory proof-adversarial review PASS
- [ ] math.AG/Weyl–Dixmier review PASS
- [ ] Lean/build/axiom audit PASS on the new single-SHA freeze
- [ ] Non-claims review PASS
- [ ] Package/metadata review PASS
- [x] Final PDF rendered as 11 letter-size pages and visually inspected
- [ ] Dan approval recorded

No tag, release, DOI minting, or arXiv submission is authorized while any item
above remains open.

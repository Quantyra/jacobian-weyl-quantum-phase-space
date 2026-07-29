# A001 publication checklist (`v0.3.9-referee-revision`, proposed and untagged)

**Status:** SCIENTIFIC REVISION — prior technical PASS is superseded; fresh
math.FA, math.AG, Lean/build, non-claims, and package review pending.

PDF: `docs/notes/A001-arxiv.pdf`  
Tag/release: none
Scope: **specific canonical \(H=-iX_1\) only**

## Targeted revision

- [x] Weak-adjoint proof dominates both the test-function and transport
  pairings.
- [x] The absolutely convergent improper identity is proved on each fixed
  fiber before the established equality is integrated transversely by
  Fubini.
- [x] No transverse dominated-convergence step, measurable lower-endpoint
  selection, measurable exhaustion, or interior \(s\)-indicator is used.
- [x] Cross-orbit injectivity uses invariance of \(F_0,F_2\).
- [x] Transverse cutoffs satisfy
  \(\operatorname{supp}\chi\Subset W_+\).
- [x] The zero extension is handled by the direct weak identity; no
  unsupported continuity or global finite-boundary claim for the variable
  lower endpoint is used.
- [x] The uniform-collar norm lower bound makes cutoff injectivity explicit.
- [x] The Lean-backed sign involution is the main \(+i\) route.
- [x] Backward-wall material is labeled independent geometry and is not used
  for Theorem F.
- [x] Theorem F states \(n_+=n_-=\aleph_0\), with conventional
  \((\infty,\infty)\) notation.
- [x] The von Neumann corollary is stated for \(\overline H\), with the
  equivalence between self-adjoint extensions of \(H\) and \(\overline H\)
  explicit.
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

- Synchronized publication freeze:
  `b8bc72ea87531b88d50ed588ec6268ae743a662f` (untagged, unreleased).
- Historical Theorem F source root:
  `ff50f4a2a312591c2e5b26e71eb390ade9164b34`.
- [x] Produce a single-SHA Lean freeze with synchronized documentation.
- [x] Record strict `lake exe cache get`, targeted multiplicity build, and
  full `lake build` at that SHA.
- [x] Record and validate headline-theorem axiom output in executable
  publication provenance.

The existing Lean results remain bounded to the specific `H_X1_min`:
`ExoticCCR.theoremE`, `ExoticCCR.theoremF`,
`hilbertDeficiencyIndex_X1_eq_aleph0`,
`theoremFVonNeumannClassification`, `theoremFUnitPhaseExtension`, and
`theoremFUnitPhaseExtension_injective`. The last two declarations exhibit an
injective unit-phase family, hence a continuum-sized lower family of distinct
extension witnesses. No preferred extension, arbitrary-operator
classification, exact Hamel rank, exact cardinality of the full extension
type, strong CCR, physical selection, or paper backward-wall formalization is
asserted.

## Fresh mandatory gate

- [ ] math.FA/operator-theory proof-adversarial review PASS
- [ ] math.AG/Weyl–Dixmier review PASS
- [x] Lean/build/axiom audit PASS on the synchronized freeze
- [ ] Non-claims review PASS
- [ ] Package/metadata review PASS
- [x] Final PDF rendered as 11 letter-size pages and visually inspected
- [ ] Dan approval recorded

No tag, release, DOI minting, or arXiv submission is authorized while any item
above remains open.

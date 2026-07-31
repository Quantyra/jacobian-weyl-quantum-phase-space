# A001 publication checklist (`v0.3.9-referee-revision` release package)

**Status:** APPROVED FOR PUBLICATION WORKFLOW — all mandatory publication
gates PASS and Dan approved publication on 2026-07-30. The corrective
successors leave A001 theorem claims unchanged. The exact release identifier is
`v0.3.9-referee-revision`; any version DOI and arXiv identifier are assigned
separately by external ingest.

PDF: `docs/notes/A001-arxiv.pdf`  
PDF SHA-256: `96a444196598b418b6724b03e0ca40e75756b3697c3a3eb21f3b204c54aad1c8`
Release identifier: `v0.3.9-referee-revision`
Scope: **specific canonical \(H=-iX_1\) only**

## Targeted revision

- [x] Lean-proved unit-phase injection is separated from the classical
  continuum-cardinality corollary.
- [x] The algebraic index is named `hamelDeficiencyRank` and distinguished
  from Hilbert deficiency dimension.
- [x] Theorem E provenance distinguishes tag target `be4f330` from reviewed
  theorem-source anchor `a6bb091`.
- [x] Complex inner products are explicitly conjugate-linear in the first
  argument.
- [x] Every deficiency-space `dim` in the paper is qualified as Hilbert
  dimension.
- [x] Paper-level maximal-sheet diffeomorphism/invariance, quantitative cutoff
  bound, and all-\(j\) operator symmetry are distinguished from exact named
  Lean coverage.
- [x] Paper title, candidate/release status, and concept-versus-version DOI
  semantics are aligned across the current metadata surfaces.
- [x] Current title and source prose use neutral attribution: the explicit
  map was announced by Alpöge, whose announcement credits Fable for work
  leading to it; no uncertain co-discovery eponym is coined.
- [x] The displayed rank-three Weyl endomorphism is constructed, but explicit
  nonautomorphy/non-surjectivity is neither claimed nor inferred from the
  classical collision.
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
  `2e40c4cab86a1ef97cb3334497d10081dfe33867` (untagged, unreleased;
  provenance-only successor to `fbcdd034`, theorem/audit source unchanged).
- Historical Theorem F source root:
  `ff50f4a2a312591c2e5b26e71eb390ade9164b34`.
- [x] Produce a single-SHA Lean freeze with synchronized documentation.
- [x] Record the earlier targeted builds, full 8,702-job `lake build`, and
  nine-declaration audit at theorem/audit source `fbcdd034`; provenance-only
  publication freeze `2e40c4c` carries that theorem/audit source unchanged.
- [x] Record the later exact-SHA rerun at `2e40c4c`: GitHub Actions
  [run 30520624449](https://github.com/Quantyra/exotic-ccr-lean/actions/runs/30520624449)
  passed the full 8,702-job build and nine-declaration audit and uploaded
  artifact `8750689968`.
- [x] Record and validate headline-theorem axiom output in executable
  publication provenance.

The existing Lean results remain bounded to the specific `H_X1_min`:
`ExoticCCR.theoremE`, `ExoticCCR.theoremF`,
`hilbertDeficiencyIndex_X1_eq_aleph0`,
`theoremFVonNeumannClassification`, `theoremFUnitPhaseExtension`, and
`theoremFUnitPhaseExtension_injective`. The last two declarations prove an
injective unit-phase family. The continuum-sized lower-family conclusion
additionally uses the classical cardinality of the complex unit circle; that
cardinal identification is not one of the cited Lean declarations. No
preferred extension, arbitrary-operator
classification, exact Hamel rank, exact cardinality of the full extension
type, strong CCR, physical selection, or paper backward-wall formalization is
asserted.

## Mandatory publication gate

- [x] Fresh math.FA/operator-theory proof-adversarial review — PASS
- [x] Fresh math.AG/Weyl–Dixmier review — PASS
- [x] Fresh Lean/build/axiom audit on the synchronized corrected freeze:
  earlier focused/full/audit evidence is tied to unchanged theorem/audit
  source `fbcdd034`; exact-SHA run `30520624449` at provenance-only freeze
  `2e40c4c` passed the full 8,702-job build and nine-declaration audit
- [x] Fresh non-claims review — PASS
- [x] Fresh package/metadata review — PASS
- [x] Fresh external review finding triaged: J6-C withdrawn; Program C/C001
      moved outside A001 as historical/open pending Lean
- [x] Re-run non-claims and package/metadata roles on the successor commits —
      PASS
- [x] Revised PDF built twice without warnings, rendered as 11 letter-size
  pages, and visually inspected page by page
- [x] Dan approval recorded — 2026-07-30

All mandatory review items are closed. Dan authorized publication on
2026-07-30. Release, DOI, and arXiv actions remain distinct downstream
operations and are not asserted by this checklist update.

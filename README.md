# EXOTIC-CCR — Jacobian / Weyl / quantum phase-space

**Author:** Daniel Eric Fredriksen (Quantyra Inc.)  
**Paper package:** `v0.3.9-referee-revision` (proposed, untagged)
**Scientific status:** A001 Lean/build and math.FA/math.AG gates PASS; fresh
external review found a Program C/C001 normal-CP error and a Lean-provenance
status error. The A001 theorem claims are unchanged, but publication remains
blocked pending correction and re-gating before Dan approval.
**Concept DOI:** [10.5281/zenodo.21474351](https://doi.org/10.5281/zenodo.21474351) (project-level record; it does not identify this untagged candidate)
**Do not use:** the v0.2.2 deficiency pair or the v0.3.0 interior-indicator proof

## Start here

- [A001-arxiv.pdf](docs/notes/A001-arxiv.pdf) — rendered paper candidate
- [A001-arxiv.tex](docs/notes/A001-arxiv.tex) — canonical paper source
- [A001-arxiv-checklist.md](docs/notes/A001-arxiv-checklist.md) — current review status
- [A001-ERRATUM-v0.2.2.md](docs/notes/A001-ERRATUM-v0.2.2.md) — withdrawn claims

The long-form [A001-arxiv-draft.md](docs/notes/A001-arxiv-draft.md) is a
historical drafting notebook, not the freeze source.

## Result and scope

For the explicit Keller map announced by Alpöge (with Fable credited in the
announcement for work leading to the map), the paper records the standard
Poisson/Weyl lifts and analyzes the canonical real dual field \(X_1\). The
minimal transport operator \(H=-iX_1\) on \(C_c^\infty(\mathbb{R}^3)\) is not
essentially self-adjoint and has Hilbert deficiency indices
\[
n_+=n_-=\aleph_0,
\]
conventionally written \((n_+,n_-)=(\infty,\infty)\).

The revised main proof constructs the \(-i\) deficiency family from the
forward maximal sheet and obtains the \(+i\) family through the
measure-preserving sign involution already formalized in Lean. The backward
wall is retained only as independent geometric material.

The collision is used for the seed and cotangent-lift noninjectivity claims.
The analytic Theorems D–F instead use the constant Jacobian and the explicit
incompleteness/escape geometry of \(X_1\). The paper does not claim a general
surjectivity/completeness equivalence.

## Companion Lean

Repository: <https://github.com/Quantyra/exotic-ccr-lean>

- Released Theorem E milestone: tag `v0.1.8-theorem-e` targets `be4f330`;
  `a6bb091` is its reviewed theorem-source anchor.
- Synchronized Lean publication freeze:
  `fbcdd0345d2f2540cd537204be2178ae07e18a5e` (untagged and unreleased).
- Historical Theorem F source root:
  `ff50f4a2a312591c2e5b26e71eb390ade9164b34`.

The synchronized freeze includes theorem sources, documentation, recorded
strict cache/build provenance, and an executable headline-theorem axiom audit.
`PUBLICATION_PROVENANCE.md` records the focused
`TheoremFPlusITransport` build (8,684 jobs), focused
`TheoremFExtensionMultiplicity` build (8,692 jobs), full `lake build`
(8,702 jobs), and the nine-declaration executable axiom audit at the pinned
SHA. Later focused Theorem C / Theorem C Weyl checks are implementation checks,
not the publication-freeze build provenance summarized here.
Lean/build and math.FA/math.AG review gates PASS. The present claim-boundary
cleanup still requires fresh non-claims and package/metadata re-gates before
the candidate returns to Dan for approval.

At the synchronized freeze, `ExoticCCR.theoremF` proves that both adjoint
eigenspaces of the specific canonical minimal core are not finite-dimensional.
`hilbertDeficiencyIndex_X1_eq_aleph0` gives exact \(\aleph_0\) Hilbert-basis
cardinality for both closed eigenspaces. `hamelDeficiencyRank` is
`Module.rank` (algebraic/Hamel rank), for which only lower bounds are claimed.
For the specific `H_X1_min`, `theoremFVonNeumannClassification` classifies all
`SelfAdjointExtension H_X1_min` witnesses by complex-linear isometric
equivalences from the \(+i\) to the \(-i\) adjoint eigenspace.
`theoremFUnitPhaseExtension` and
`theoremFUnitPhaseExtension_injective` prove that unitary complex phases inject
into distinct extension witnesses. The continuum-sized lower-family conclusion
also uses the classical fact that the complex unit circle has cardinality
continuum; that cardinal identification is not part of those Lean declarations.

## Non-claims

- No unitary quantum gate, channel, or computational advantage.
- Program C and C001 are outside the current A001 publication package. Their
  former positive normal-CP and \(C^*\)-completion claims are historical,
  unformalized records, not current results. In particular, J6-C
  (Diag-CP-\(\Phi_0\)) is withdrawn.
- No preferred physical extension.
- No essential-self-adjointness conclusion for the other two dual momenta.
- No arbitrary-operator classification, exact Hamel rank, or exact cardinality
  of the full extension type claimed as Lean corollaries.
- No new rank-three Dixmier counterexample claim.
- The displayed Weyl endomorphism is constructed, but its noninvertibility is
  not established by this artifact.
- No seed-discovery or priority claim.

See [INTEGRITY.md](INTEGRITY.md) and the paper's Non-claims section.

## Companion papers

B001 remains an untagged cross-companion correction. C001 is a withdrawn
historical record outside A001. The releases in the last column are
historical and do **not** identify the current local PDF binaries.

| Paper | Current local PDF (untagged correction) | Historical release (not this PDF) |
|---|---|---|
| B001 classification | [B001-classification-arxiv.pdf](docs/notes/B001-classification-arxiv.pdf) | [v0.2.3-b001-draft](https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.2.3-b001-draft) |
| C001 completions — **WITHDRAWN historical record; outside A001** | [C001-cp-correspondence-arxiv.pdf](docs/notes/C001-cp-correspondence-arxiv.pdf) | [v0.3.3-c001-companion](https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.3.3-c001-companion) |

## Evidence

| Gate | Status | Evidence |
|---|---|---|
| G0 seed | certified | [D0 seed dossier](docs/validation/D0-seed-validation-dossier.md) |
| G2 Poisson | certified | [G2 dossier](docs/validation/G2-poisson-A001-dossier.md) |
| G3 Weyl | certified | [G3 dossier](docs/validation/G3-weyl-A001-dossier.md) |
| G4 \(H=-iX_1\) | theorem surface proved; Lean/build and math reviews PASS; non-claims/package re-gates pending | [orbit-measure dossier](docs/validation/G4-P1-orbit-measure-deficiency.md) |

## Citation and release status

See [CITATION.cff](CITATION.cff). The proposed
`v0.3.9-referee-revision` paper package has no tag, GitHub release, arXiv
identifier, or version DOI. Existing DOI records and releases refer to earlier
artifacts and must not be relabeled.

Apache-2.0. See [LICENSE](LICENSE).

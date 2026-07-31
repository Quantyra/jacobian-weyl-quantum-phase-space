# Zenodo status

## A001 release package

| Field | Value |
|---|---|
| Release identifier | `v0.3.9-referee-revision` |
| GitHub release | <https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.3.9-referee-revision> |
| Tag commit | `001035470f8ebfa180c840e507796aec560284b8` |
| arXiv identifier | none |
| Synchronized Lean freeze | `2e40c4cab86a1ef97cb3334497d10081dfe33867` (untagged, unreleased; provenance-only successor to `fbcdd034`) |
| Historical theorem-source root | `ff50f4a2a312591c2e5b26e71eb390ade9164b34` |
| Lean cache/build/axiom provenance | `PUBLICATION_PROVENANCE.md`: focused `TheoremFPlusITransport` (8,684 jobs), focused `TheoremFExtensionMultiplicity` (8,692 jobs), full `lake build` (8,702 jobs), nine-declaration axiom audit |
| Version DOI | `10.5281/zenodo.21715479` (record `21715479`) |
| Existing concept DOI | `10.5281/zenodo.21474351` (project-level) |
| Existing v0.3.3 version DOI | `10.5281/zenodo.21478679` (do not relabel) |

The paper package now uses the forward maximal sheet and sign involution for
the main deficiency proof and states exact Hilbert indices
\(n_+=n_-=\aleph_0\). The backward wall is independent geometry. The Lean
artifact remains bounded to the specific canonical `H_X1_min`; no preferred
extension, arbitrary-operator theorem, exact Hamel rank, exact extension
cardinality of the full extension type, strong CCR, physical selection, or
rank-three Dixmier counterexample is claimed. The Lean declarations
`theoremFUnitPhaseExtension` and `theoremFUnitPhaseExtension_injective`
prove an injection from unitary complex phases into distinct extension
witnesses. The continuum-sized lower-family conclusion additionally uses the
classical cardinality of the complex unit circle; that cardinal identification
is not one of the cited Lean declarations.

The corrected Lean/build/audit, math.FA/math.AG/Weyl, non-claims, and
package/metadata gates are COMPLETE/PASS. Dan approved publication on
2026-07-30. Later focused Theorem C / Theorem C Weyl checks are separate
implementation checks, not the publication-freeze provenance above. Zenodo
ingest assigned version DOI `10.5281/zenodo.21715479`; the concept DOI remains
`10.5281/zenodo.21474351`. No arXiv identifier is assigned. This post-release
receipt does not move the tag from commit `0010354`.
Do not cite the v0.2.2 pair or v0.3.0 interior-indicator proof.

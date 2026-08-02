# A001 arXiv submission packet (`v0.3.9-referee-revision` release package)

**Status:** PACKAGE CLOSED FOR THEOREM WORK (2026-08-01) — A001 published as
bounded result (GitHub `v0.3.9-referee-revision` + Zenodo version DOI); all
gates PASS; Dan approval recorded 2026-07-30. **Only remaining action:** human
arXiv endorsement code `VIPN6B`, then submit after endorse. No submission
performed yet; no arXiv identifier assigned. See
`docs/validation/A001-PROGRAM-CLOSEOUT-FINAL.md`.
**Primary (recommended):** `math.SP` · alternative `math.FA`
**Secondary:** `math.FA`, `math-ph`
**Scope:** specific canonical \(H=-iX_1\) only

| Item | Current value |
|---|---|
| PDF | `docs/notes/A001-arxiv.pdf`; SHA-256 `96a444196598b418b6724b03e0ca40e75756b3697c3a3eb21f3b204c54aad1c8` |
| Canonical source | `docs/notes/A001-arxiv.tex` |
| Release identifier | `v0.3.9-referee-revision` |
| GitHub release | <https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.3.9-referee-revision>; tag commit `001035470f8ebfa180c840e507796aec560284b8` |
| arXiv identifier | none |
| Concept DOI | `10.5281/zenodo.21474351` (project-level only) |
| Version DOI | `10.5281/zenodo.21715479` |
| Synchronized Lean freeze | `2e40c4cab86a1ef97cb3334497d10081dfe33867` (untagged, unreleased; provenance-only successor to `fbcdd034`) |
| Historical theorem source | `ff50f4a2a312591c2e5b26e71eb390ade9164b34` |
| Lean build/axiom provenance | `PUBLICATION_PROVENANCE.md`: focused `TheoremFPlusITransport` (8,684 jobs), focused `TheoremFExtensionMultiplicity` (8,692 jobs), full `lake build` (8,702 jobs), nine-declaration axiom audit |
| Technical gates | Lean/build, math.FA/math.AG, non-claims, and package/metadata COMPLETE/PASS |
| Package/metadata recheck | PASS |
| Human approval | Dan approved publication on 2026-07-30 |

## Exact scope

The paper states \(n_+=n_-=\aleph_0\) for the Hilbert deficiency indices of
the canonical real dual transport operator. The revised main proof uses the
forward maximal sheet and measure-preserving sign involution. The backward
wall is retained as independent geometry only.

The companion Lean artifact proves the bounded canonical-core Theorems E–F,
the exact \(\aleph_0\) Hilbert-basis indices, the bijective von Neumann
classification for the specific `H_X1_min`, and an injective family of
distinct self-adjoint-extension witnesses parameterized by unitary complex
phases. Lean proves the phase injection; the continuum lower-family conclusion
additionally uses the classical cardinality of the complex unit circle. It
does not prove a
preferred extension, an arbitrary-operator theorem, exact Hamel rank, exact
cardinality of the full extension type, strong CCR, physical selection, or the
paper backward-wall construction.

## Submission comment

The map was announced by Alpöge; the announcement credits Claude Fable for
work leading to it and Akhil Mathew for prompting the question. It is restated
and independently checked here, not discovered here. No gates, channels,
computational advantage, or rank-three Dixmier counterexample is claimed.
Lean/build, math.FA/math.AG, non-claims, and package/metadata gates PASS. Dan
approved publication on 2026-07-30. The exact release identifier is
`v0.3.9-referee-revision`; version DOI `10.5281/zenodo.21715479` identifies
that release. No arXiv identifier is assigned; endorsement/submission remain
pending external steps. Later receipt commits do not move the tag.

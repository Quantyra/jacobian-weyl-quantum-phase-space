# A001 arXiv submission packet (`v0.3.9-referee-revision`, proposed and untagged)

**Status:** SCIENTIFIC REVISION — do not submit
**Primary (recommended):** `math.SP` · alternative `math.FA`
**Secondary:** `math.FA`, `math-ph`
**Scope:** specific canonical \(H=-iX_1\) only

| Item | Current value |
|---|---|
| PDF | `docs/notes/A001-arxiv.pdf`; SHA-256 `28dff06b67ff3b7799f652ae3ac39d860e103421803638e29372aa7698046b04` |
| Canonical source | `docs/notes/A001-arxiv.tex` |
| Tag/release | none |
| arXiv identifier | none |
| Concept DOI | `10.5281/zenodo.21474351` (project-level only) |
| New version DOI | none; do not predict |
| Synchronized Lean freeze | `2e40c4cab86a1ef97cb3334497d10081dfe33867` (untagged, unreleased; provenance-only successor to `fbcdd034`) |
| Historical theorem source | `ff50f4a2a312591c2e5b26e71eb390ade9164b34` |
| Lean build/axiom provenance | `PUBLICATION_PROVENANCE.md`: focused `TheoremFPlusITransport` (8,684 jobs), focused `TheoremFExtensionMultiplicity` (8,692 jobs), full `lake build` (8,702 jobs), nine-declaration axiom audit |
| Technical gates | Lean/build and math.FA/math.AG COMPLETE/PASS; fresh non-claims re-gate pending |
| Package/metadata recheck | pending |
| Human approval | pending Dan |

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
Lean/build and math.FA/math.AG gates PASS. Fresh non-claims and
package/metadata re-gates are required before the package can return to Dan
for approval.

# A001 arXiv submission packet (`v0.3.9-referee-revision`, proposed and untagged)

**Status:** SCIENTIFIC REVISION — do not submit
**Primary (recommended):** `math.SP` · alternative `math.FA`
**Secondary:** `math.FA`, `math-ph`
**Scope:** specific canonical \(H=-iX_1\) only

| Item | Current value |
|---|---|
| PDF | `docs/notes/A001-arxiv.pdf` |
| Canonical source | `docs/notes/A001-arxiv.tex` |
| Tag/release | none |
| arXiv identifier | none |
| Concept DOI | `10.5281/zenodo.21474351` (project-level only) |
| New version DOI | none; do not predict |
| Synchronized Lean freeze | `b8bc72ea87531b88d50ed588ec6268ae743a662f` (untagged, unreleased) |
| Historical theorem source | `ff50f4a2a312591c2e5b26e71eb390ade9164b34` |
| Lean build/axiom provenance | PASS at synchronized freeze |
| Scientific gates | pending fresh math.FA and math.AG review |
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
phases. This exhibits a continuum-sized lower family. It does not prove a
preferred extension, an arbitrary-operator theorem, exact Hamel rank, exact
cardinality of the full extension type, strong CCR, physical selection, or the
paper backward-wall construction.

## Submission comment

Seed map due to Alpöge and Claude Fable, with Akhil Mathew credited for
prompting the question; restated and independently checked, not discovered
here. No gates, channels, computational advantage, or rank-three Dixmier
counterexample is claimed. The package remains blocked pending fresh technical
gates and Dan approval.

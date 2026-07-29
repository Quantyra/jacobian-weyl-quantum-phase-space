# A001 arXiv submission packet (`v0.3.9-referee-revision`, proposed and untagged)

**Status:** SCIENTIFIC REVISION — do not submit
**Primary (recommended):** `math.SP` · alternative `math.FA`
**Secondary:** `math.FA`, `math-ph`
**Scope:** specific canonical \(H=-iX_1\) only

| Item | Current value |
|---|---|
| PDF | `docs/notes/A001-arxiv.pdf`; SHA-256 `b4f4a8882d828134a6aa15462d3d888c411186aa0c865632fa564a34fe24352d` |
| Canonical source | `docs/notes/A001-arxiv.tex` |
| Tag/release | none |
| arXiv identifier | none |
| Concept DOI | `10.5281/zenodo.21474351` (project-level only) |
| New version DOI | none; do not predict |
| Synchronized Lean freeze | `0735757f7f1a3a2875fcd29e31e03a203c3c8a74` (untagged, unreleased) |
| Historical theorem source | `ff50f4a2a312591c2e5b26e71eb390ade9164b34` |
| Lean build/axiom provenance | corrected freeze records focused 8,684/8,692 jobs, full 8,702 jobs, and seven-declaration audit |
| Technical gates | Lean/build complete; fresh math.FA, math.AG, and non-claims re-gates pending |
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

Seed map due to Alpöge and Claude Fable, with Akhil Mathew credited for
prompting the question; restated and independently checked, not discovered
here. No gates, channels, computational advantage, or rank-three Dixmier
counterexample is claimed. Fresh technical re-gates are required before the
package can return to Dan for approval.

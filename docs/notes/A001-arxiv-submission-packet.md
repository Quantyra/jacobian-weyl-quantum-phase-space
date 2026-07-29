# A001 arXiv submission packet (v0.3.8-theorem-f proposed, untagged)

**Status:** REVIEW CANDIDATE — no final approval; tag/release/DOI not created  
**Primary (recommended):** `math.SP` · alt `math.FA`  
**Secondary:** `math.FA` or `math.SP`, `math-ph`  
**Tag:** none · **Candidate:** `v0.3.8-theorem-f` · **Scope:** \(H=-iX_1\) only

## Artifacts
| Item | URL / path |
|------|------------|
| PDF | `docs/notes/A001-arxiv.pdf` (rendered candidate; no tag URL) |
| TeX | docs/notes/A001-arxiv.tex |
| Release | none; do not create until review and Dan approval |
| Concept DOI | https://doi.org/10.5281/zenodo.21474351 (project-level only until version ingest) |
| Lean (bounded Theorem E) | `ExoticCCR.theoremE` @ SHA `a6bb091` |
| Lean (bounded Theorem F) | `ExoticCCR.theoremF` @ SHA `ff50f4a2a312591c2e5b26e71eb390ade9164b34` |
| Lean standard-rank supplement | `aleph0_le_standardDeficiencyIndex_X1`: `Cardinal.aleph0 ≤ n_+` and `Cardinal.aleph0 ≤ n_-`; `standardDeficiencyIndex`/`Module.rank` is Hamel rank with lower bounds only |
| Lean exact Hilbert supplement | `hilbertDeficiencyIndex_X1_eq_aleph0`: exact `Cardinal.aleph0` Hilbert-basis cardinality for both closed adjoint eigenspaces |
| Lean von Neumann corollary | For the specific `H_X1_min`, all `SelfAdjointExtension H_X1_min` witnesses are classified bijectively by complex-linear isometric equivalences from the `+i` to the `-i` adjoint eigenspace; at least two distinct witnesses exist |
| Lean boundary | No preferred extension, arbitrary-operator theorem, exact extension cardinality, infinitely-many/continuum or algebraic-selection corollary, backward-wall construction, strong CCR, or physical selection |

## Comments line
Seed map due to Alpöge (credits Fable); restated/verified only. Candidate
v0.3.8-theorem-f; concept DOI 10.5281/zenodo.21474351. H=-iX_1 only.
Bounded Lean Theorem F proves both standard adjoint eigenspaces are not
finite-dimensional. The exact Hilbert-basis cardinal is separately formalized;
the algebraic Hamel rank is not identified with \(\aleph0\). No
gates/channels/advantage. The specific canonical minimal operator also has a
Lean-proved von Neumann classification and at least two distinct self-adjoint
extension witnesses; stronger cardinality and selection consequences remain
paper-grade.

## Endorsement
Start submit → code → https://arxiv.org/auth/endorse → finish submit.

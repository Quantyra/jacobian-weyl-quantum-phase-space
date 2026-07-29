# Zenodo status

## Proposed Theorem F artifact

The proposed paper/package version is `0.3.8-theorem-f`, tied to the science
worktree commit recorded below and supplemented by Lean SHA
`ff50f4a2a312591c2e5b26e71eb390ade9164b34`. It is currently untagged pending
the required review gates and Dan approval. The bounded Lean claims are
`ExoticCCR.theoremE` at `a6bb091` and `ExoticCCR.theoremF` at the recorded SHA:
both standard adjoint eigenspaces at `+i` and `-i` are not finite-dimensional,
with standard cardinal-valued lower bounds `Cardinal.aleph0 ≤ n_+` and
`Cardinal.aleph0 ≤ n_-`. A separate exact Hilbert-index result
`hilbertDeficiencyIndex_X1_eq_aleph0` gives `Cardinal.aleph0` for both closed
adjoint eigenspaces. `standardDeficiencyIndex`/`Module.rank` is Hamel rank with
lower bounds only. For the specific canonical minimal operator `H_X1_min`,
Lean now proves a bijective von Neumann classification of all
`SelfAdjointExtension H_X1_min` witnesses (self-adjoint `LinearPMap`s extending
`H_X1_min`) by complex-linear isometric equivalences from the `+i` adjoint
eigenspace to the `-i` adjoint eigenspace, and proves at least two distinct such
extensions exist. No preferred extension, arbitrary-operator theorem, exact
extension cardinality, paper backward-wall construction, or Lean proof of the
paper's infinitely-many/continuum or algebraic-selection consequences is
claimed.

| Field | Value |
|-------|-------|
| Proposed version | `0.3.8-theorem-f` |
| Candidate science commit | commit containing this status file (see repository history) |
| Git tag/release | **none; review blocked** |
| Lean supplement | `ExoticCCR.theoremF`, `hilbertDeficiencyIndex_X1_eq_aleph0`, `theoremFVonNeumannClassification`, and `theoremF_exists_two_distinct_selfAdjointExtensions` @ `ff50f4a2a312591c2e5b26e71eb390ade9164b34` (Theorem E release @ `a6bb091`) |
| New version DOI | **not yet minted; do not predict** |
| Existing concept DOI | 10.5281/zenodo.21474351 (historical/project-level reference) |
| Existing v0.3.3 version DOI | 10.5281/zenodo.21478679 (do not relabel) |

Do not cite v0.2.2 pair (0,inf) or v0.3.0 Dom(H*) indicator proof.

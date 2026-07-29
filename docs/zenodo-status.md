# Zenodo status

## Proposed Theorem F artifact

The proposed paper/package version is `0.3.8-theorem-f`, tied to the science
worktree commit recorded below and supplemented by Lean SHA
`f1fe83785add60ccc5f012b51e7576aab5627a74`. It is currently untagged pending
the required review gates and Dan approval. The bounded Lean claims are
`ExoticCCR.theoremE` at `a6bb091` and `ExoticCCR.theoremF` at the recorded SHA:
both standard adjoint eigenspaces at `+i` and `-i` are not finite-dimensional,
with standard cardinal-valued lower bounds `Cardinal.aleph0 ≤ n_+` and
`Cardinal.aleph0 ≤ n_-`. A separate exact Hilbert-index result
`hilbertDeficiencyIndex_X1_eq_aleph0` gives `Cardinal.aleph0` for both closed
adjoint eigenspaces. `standardDeficiencyIndex`/`Module.rank` is Hamel rank with
lower bounds only. Von Neumann extension multiplicity/classification and the
paper's backward-wall construction remain paper-grade and are not
Lean-covered.

| Field | Value |
|-------|-------|
| Proposed version | `0.3.8-theorem-f` |
| Candidate science commit | `a6257775885fea8a526498a20d9f1a9222ebed2` |
| Git tag/release | **none; review blocked** |
| Lean supplement | `ExoticCCR.theoremF` and `hilbertDeficiencyIndex_X1_eq_aleph0` @ `f1fe83785add60ccc5f012b51e7576aab5627a74` (Theorem E @ `a6bb091`) |
| New version DOI | **not yet minted; do not predict** |
| Existing concept DOI | 10.5281/zenodo.21474351 (historical/project-level reference) |
| Existing v0.3.3 version DOI | 10.5281/zenodo.21478679 (do not relabel) |

Do not cite v0.2.2 pair (0,inf) or v0.3.0 Dom(H*) indicator proof.

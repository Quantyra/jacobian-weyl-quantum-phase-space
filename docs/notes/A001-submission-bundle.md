# A001 public bundle (v0.3.8-theorem-f proposed, untagged)

PDF: docs/notes/A001-arxiv.pdf  
Tag: none; release blocked pending review and Dan approval  
Concept DOI: 10.5281/zenodo.21474351 (project-level)  

Paper-grade claim: (n+,n-)=(inf,inf) for H=-iX_1 only. The companion Lean
claims are bounded to `ExoticCCR.theoremE` at `a6bb091` and
`ExoticCCR.theoremF` at `ff50f4a2a312591c2e5b26e71eb390ade9164b34`:
the canonical minimal X1 core is not essentially self-adjoint and both
standard adjoint eigenspaces are not finite-dimensional, with standard
cardinal-valued lower bounds `Cardinal.aleph0 ≤ n_+` and `Cardinal.aleph0 ≤ n_-`.
The separate `hilbertDeficiencyIndex_X1_eq_aleph0` theorem gives exact
Hilbert-basis cardinality `Cardinal.aleph0` for both closed adjoint
eigenspaces. `standardDeficiencyIndex`/`Module.rank` is Hamel rank with lower
bounds only. At the same SHA, for the specific `H_X1_min`, Lean classifies all
self-adjoint-extension witnesses bijectively by complex-linear isometric
equivalences from the `+i` to the `-i` adjoint eigenspace and proves at least
two distinct witnesses exist. This does not prove a preferred extension, an
arbitrary-operator theorem, exact extension cardinality, the paper's
infinitely-many/continuum or algebraic-selection consequences, or the
backward-wall construction. No gates. Seed restated.

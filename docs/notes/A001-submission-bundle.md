# A001 public bundle (v0.3.8-theorem-f proposed, untagged)

PDF: docs/notes/A001-arxiv.pdf  
Tag: none; release blocked pending review and Dan approval  
Concept DOI: 10.5281/zenodo.21474351 (project-level)  

Paper-grade claim: (n+,n-)=(inf,inf) for H=-iX_1 only. The companion Lean
claims are bounded to `ExoticCCR.theoremE` at `a6bb091` and
`ExoticCCR.theoremF` at `f1fe83785add60ccc5f012b51e7576aab5627a74`:
the canonical minimal X1 core is not essentially self-adjoint and both
standard adjoint eigenspaces are not finite-dimensional, with standard
cardinal-valued lower bounds `Cardinal.aleph0 ≤ n_+` and `Cardinal.aleph0 ≤ n_-`.
The separate `hilbertDeficiencyIndex_X1_eq_aleph0` theorem gives exact
Hilbert-basis cardinality `Cardinal.aleph0` for both closed adjoint
eigenspaces. `standardDeficiencyIndex`/`Module.rank` is Hamel rank with lower
bounds only. No gates. Seed restated. Von Neumann extension
multiplicity/classification and the paper's backward-wall construction remain
paper-grade/not Lean-covered.

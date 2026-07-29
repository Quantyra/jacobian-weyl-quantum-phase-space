# A001 publication checklist (v0.3.8-theorem-f proposed, untagged)

**Status:** technical gates PASS; Dan approval pending.

PDF: `docs/notes/A001-arxiv.pdf`  
Tag: none  
Scope: **H=-iX_1 only**

## Done

- [x] Theorems A-F and prior errata retained in the paper package
- [x] Lean-backed bounded Theorem E recorded as `ExoticCCR.theoremE` at SHA `a6bb091`
- [x] Lean-backed bounded Theorem F recorded as `ExoticCCR.theoremF` at SHA `ff50f4a2a312591c2e5b26e71eb390ade9164b34`
- [x] Standard supplement records `Cardinal.aleph0 ≤ n_+` and `Cardinal.aleph0 ≤ n_-` via `aleph0_le_standardDeficiencyIndex_X1`; `standardDeficiencyIndex`/`Module.rank` is Hamel rank with lower bounds only
- [x] Separate exact Hilbert-index supplement `hilbertDeficiencyIndex_X1_eq_aleph0` records \(\operatorname{aleph0}\) for both closed adjoint eigenspaces
- [x] For the specific `H_X1_min`, `theoremFVonNeumannClassification` gives the bijection between all self-adjoint-extension witnesses and `+i`-to-`-i` complex-linear isometric equivalences, and `theoremF_exists_two_distinct_selfAdjointExtensions` gives at least two distinct witnesses
- [x] Exact extension cardinality, infinitely-many/continuum and algebraic-selection consequences, preferred extension, arbitrary-operator generalization, and the paper-grade backward-wall construction remain explicitly outside the new Lean corollary
- [x] Metadata uses proposed version `v0.3.8-theorem-f` without inventing a DOI or tag

## Required re-gate

- [x] Non-claims review PASS on final paper and README surfaces after this update
- [x] Package/metadata review PASS on final candidate version/SHA/DOI ledger after this update
- [x] Lean/build/audit review PASS on final Lean SHA `ff50f4a2a312591c2e5b26e71eb390ade9164b34`
- [x] Final PDF rendered and visually inspected from the updated candidate TeX
- [ ] Dan approval recorded

## Dan now

- [ ] Final PDF skim
- [ ] Approve or reject theorem-bearing tag/release and arXiv submission
- [ ] After an approved release, record any Zenodo version DOI; do not predict it

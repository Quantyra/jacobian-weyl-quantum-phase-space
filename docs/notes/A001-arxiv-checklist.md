# A001 publication checklist (v0.3.8-theorem-f proposed, untagged)

**Status:** publication packet remains a review candidate pending re-gate and Dan approval after the exact Hilbert-index update.

PDF: `docs/notes/A001-arxiv.pdf`  
Tag: none  
Scope: **H=-iX_1 only**

## Done

- [x] Theorems A-F and prior errata retained in the paper package
- [x] Lean-backed bounded Theorem E recorded as `ExoticCCR.theoremE` at SHA `a6bb091`
- [x] Lean-backed bounded Theorem F recorded as `ExoticCCR.theoremF` at SHA `f1fe83785add60ccc5f012b51e7576aab5627a74`
- [x] Standard supplement records `Cardinal.aleph0 ≤ n_+` and `Cardinal.aleph0 ≤ n_-` via `aleph0_le_standardDeficiencyIndex_X1`; `standardDeficiencyIndex`/`Module.rank` is Hamel rank with lower bounds only
- [x] Separate exact Hilbert-index supplement `hilbertDeficiencyIndex_X1_eq_aleph0` records \(\operatorname{aleph0}\) for both closed adjoint eigenspaces
- [x] Von Neumann extension multiplicity/classification and the paper-grade backward-wall construction remain explicitly paper-grade/not Lean-covered
- [x] Metadata uses proposed version `v0.3.8-theorem-f` without inventing a DOI or tag

## Required re-gate

- [ ] Non-claims review PASS on final paper and README surfaces after this update
- [ ] Package/metadata review PASS on final candidate version/SHA/DOI ledger after this update
- [ ] Lean/build/audit review PASS on final Lean SHA `f1fe83785add60ccc5f012b51e7576aab5627a74`
- [ ] Final PDF rendered and visually inspected from the updated candidate TeX
- [ ] Dan approval recorded

## Dan now

- [ ] Final PDF skim
- [ ] Approve or reject theorem-bearing tag/release and arXiv submission
- [ ] After an approved release, record any Zenodo version DOI; do not predict it

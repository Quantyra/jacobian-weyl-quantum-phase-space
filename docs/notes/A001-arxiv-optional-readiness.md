# A001 arXiv readiness (`v0.3.9-referee-revision`)

**Date:** 2026-07-29
**Status:** **SCIENTIFIC REVISION; NOT READY TO SUBMIT**

## Local bundle

| Item | Path | Status |
|---|---|---|
| Canonical source | `docs/notes/A001-arxiv.tex` | revised |
| PDF | `docs/notes/A001-arxiv.pdf` | built twice; 11 pages visually inspected; SHA-256 `28dff06b…046b04` |
| Checklist | `docs/notes/A001-arxiv-checklist.md` | non-claims and package/metadata re-gates open |
| Bundle note | `docs/notes/A001-submission-bundle.md` | synchronized |
| Endorsement draft | `docs/notes/A001-endorsement-request.md` | HOLD |
| Errata | `docs/notes/A001-ERRATUM-v0.2.2.md` | retained |
| Tag/release/version DOI | none | must remain absent |

## Blocking gates

1. Fresh non-claims and package/metadata re-gates on the corrected
   synchronized packet. Lean/build and math.FA/math.AG are COMPLETE/PASS.
2. Dan approval after those gates pass.

The repository records successful cache/build and executable axiom-audit
results for the corrected synchronized Lean freeze
`2e40c4cab86a1ef97cb3334497d10081dfe33867` (provenance-only successor to
`fbcdd034`; theorem/audit source unchanged):
`PUBLICATION_PROVENANCE.md` records focused `TheoremFPlusITransport`
(8,684 jobs), focused `TheoremFExtensionMultiplicity` (8,692 jobs), the full
8,702-job `lake build`, and the nine-declaration axiom audit.
Lean/build and math.FA/math.AG/Weyl reviews are COMPLETE/PASS. Fresh
non-claims and package/metadata reviews remain required. Later focused
Theorem C / Theorem C Weyl checks are separate implementation checks. The
freeze remains untagged and unreleased.

No upload, tag, release, or DOI action is authorized before all blockers close.

# A001 arXiv readiness (`v0.3.9-referee-revision`)

**Date:** 2026-07-30
**Status:** **APPROVED FOR PUBLICATION WORKFLOW; ALL GATES PASS**

## Local bundle

| Item | Path | Status |
|---|---|---|
| Canonical source | `docs/notes/A001-arxiv.tex` | revised |
| PDF | `docs/notes/A001-arxiv.pdf` | built twice; 11 pages visually inspected; SHA-256 `96a44419…aad1c8` |
| Checklist | `docs/notes/A001-arxiv-checklist.md` | all mandatory gates PASS; Dan approval recorded |
| Bundle note | `docs/notes/A001-submission-bundle.md` | synchronized |
| Endorsement draft | `docs/notes/A001-endorsement-request.md` | ready for authorized outreach |
| Errata | `docs/notes/A001-ERRATUM-v0.2.2.md` | retained |
| Release identifier | `v0.3.9-referee-revision` | exact publication package |
| Version DOI / arXiv ID | pending external ingest | none invented here |

## Closed gates

1. Lean/build, math.FA/math.AG, non-claims, and package/metadata reviews:
   COMPLETE/PASS.
2. Dan publication approval: recorded 2026-07-30.

The repository records successful cache/build and executable axiom-audit
results for the corrected synchronized Lean freeze
`2e40c4cab86a1ef97cb3334497d10081dfe33867` (provenance-only successor to
`fbcdd034`; theorem/audit source unchanged):
`PUBLICATION_PROVENANCE.md` records focused `TheoremFPlusITransport`
(8,684 jobs), focused `TheoremFExtensionMultiplicity` (8,692 jobs), the full
8,702-job `lake build`, and the nine-declaration axiom audit.
Lean/build, math.FA/math.AG/Weyl, non-claims, and package/metadata reviews are
COMPLETE/PASS. Later focused Theorem C / Theorem C Weyl checks are separate
implementation checks. The freeze remains untagged and unreleased.

All blockers are closed and Dan has authorized publication. The exact release
identifier is `v0.3.9-referee-revision`; any Zenodo version DOI and arXiv identifier
are recorded only after their external ingest workflows.

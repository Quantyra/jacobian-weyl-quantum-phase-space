# Zenodo release path

> **SUPERSEDED / PUBLISHED (2026-08-01).**
> This path document is historical. The GitHub release and Zenodo version DOI
> for A001 are **done**. Do not treat the unchecked boxes or "pending version
> DOI" wording below as current work. Authoritative closeout:
> [`validation/A001-PROGRAM-CLOSEOUT-FINAL.md`](validation/A001-PROGRAM-CLOSEOUT-FINAL.md).

## Goal (historical)

Obtain a version DOI for this repository via Zenodo's GitHub integration;
the project-level concept DOI already exists.

## Published receipts (current)

| Item | Value |
|------|--------|
| GitHub release | [`v0.3.9-referee-revision`](https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.3.9-referee-revision) |
| Tag commit | `001035470f8ebfa180c840e507796aec560284b8` |
| Zenodo version DOI | [10.5281/zenodo.21715479](https://doi.org/10.5281/zenodo.21715479) |
| Zenodo concept DOI | [10.5281/zenodo.21474351](https://doi.org/10.5281/zenodo.21474351) (project-level only) |
| PDF SHA-256 | `96a444196598b418b6724b03e0ca40e75756b3697c3a3eb21f3b204c54aad1c8` |

Later main-branch receipt/docs commits do **not** move the release tag.

## Soft Blocker (historical wording — frozen)

The concept DOI `10.5281/zenodo.21474351` exists and is recorded in
`CITATION.cff`. At the time this path was written, the version DOI was still
pending a GitHub release archived by Zenodo. That Soft Blocker is **resolved**
by the receipts above. The remaining Soft/human Blocker for public preprint
ingest is arXiv endorsement code `VIPN6B` only (not Zenodo).

## Path (when ready) — historical frozen checklist

The steps below are retained as the historical operating path. They are **not**
current open tasks.

1. Ensure this repo is public under `Quantyra/jacobian-weyl-quantum-phase-space`.
2. In Zenodo (account linked to GitHub `dfredriksen` / Quantyra org access): enable GitHub integration for this repository.
3. Confirm `.zenodo.json` is present on the default branch (`main`) with correct creators, license (Apache-2.0), keywords, and non-claims description.
4. Create a GitHub Release with a semver tag (e.g. `v0.0.1`).
5. Zenodo archives the release tarball and mints a version DOI; the existing
   concept DOI remains stable across versions.
6. Keep the existing concept DOI in `CITATION.cff`; add the version DOI only
   after Zenodo mints it, and bump `.zenodo.json` `version` on subsequent
   releases.

## Non-claims reminder

Release notes and Zenodo description must retain the standing non-claims block (see `INTEGRITY.md` and `.zenodo.json`).

## Status (historical frozen checkboxes — completed by published receipts)

- [x] Local scaffold and GitHub repo *(historical)*
- [x] `.zenodo.json` + `CITATION.cff` (concept DOI recorded) *(historical)*
- [x] First GitHub Release — **DONE:** `v0.3.9-referee-revision` @ `0010354` *(receipt)*
- [x] Zenodo hook / version DOI — **DONE:** `10.5281/zenodo.21715479` *(receipt)*

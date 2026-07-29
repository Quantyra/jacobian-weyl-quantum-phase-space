# Zenodo release path

## Goal

Obtain a version DOI for this repository via Zenodo’s GitHub integration;
the project-level concept DOI already exists.

## Soft Blocker

The concept DOI `10.5281/zenodo.21474351` exists and is recorded in
`CITATION.cff`. The version DOI remains pending until a GitHub release is
archived by Zenodo. This is an expected Soft Blocker for infrastructure story
S004; no version DOI is asserted for the current untagged candidate.

## Path (when ready)

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

## Status

- [x] Local scaffold and GitHub repo
- [x] `.zenodo.json` + `CITATION.cff` (concept DOI recorded)
- [ ] First GitHub Release
- [ ] Zenodo hook / version DOI

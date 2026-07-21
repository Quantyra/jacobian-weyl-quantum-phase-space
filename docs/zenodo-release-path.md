# Zenodo release path

## Goal

Obtain a version DOI (and later a concept DOI) for this repository via Zenodo’s GitHub integration.

## Soft Blocker

Until the first successful GitHub release is archived by Zenodo, **no DOI exists**. `CITATION.cff` intentionally omits a live DOI. This is an expected Soft Blocker for infrastructure story S004.

## Path (when ready)

1. Ensure this repo is public under `Quantyra/jacobian-weyl-quantum-phase-space`.
2. In Zenodo (account linked to GitHub `dfredriksen` / Quantyra org access): enable GitHub integration for this repository.
3. Confirm `.zenodo.json` is present on the default branch (`main`) with correct creators, license (Apache-2.0), keywords, and non-claims description.
4. Create a GitHub Release with a semver tag (e.g. `v0.0.1`).
5. Zenodo archives the release tarball and mints a version DOI; the concept DOI appears after the first deposit and is stable across versions.
6. Update `CITATION.cff` with the concept or version DOI as appropriate; bump `.zenodo.json` `version` on subsequent releases.

## Non-claims reminder

Release notes and Zenodo description must retain the standing non-claims block (see `INTEGRITY.md` and `.zenodo.json`).

## Status

- [x] Local scaffold and GitHub repo
- [x] `.zenodo.json` + `CITATION.cff` (DOI pending)
- [ ] First GitHub Release
- [ ] Zenodo hook / first DOI

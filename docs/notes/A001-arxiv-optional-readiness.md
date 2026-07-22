# A001 arXiv — optional readiness (no submission)

**Date:** 2026-07-21  
**Status:** **READY LOCALLY** for package inspection; **SUBMIT DEFERRED** (Dan/endorsement)  
**Non-claims:** this file is not an arXiv submission

---

## Bundle checklist

| Item | Path / note | OK? |
|------|-------------|-----|
| Source | `docs/notes/A001-arxiv.tex` | yes |
| PDF | `docs/notes/A001-arxiv.pdf` | yes |
| Checklist | `docs/notes/A001-arxiv-checklist.md` | yes |
| Bundle note | `docs/notes/A001-submission-bundle.md` | yes |
| Endorsement draft | `docs/notes/A001-endorsement-request.md` | yes |
| Errata visible | abstract / PDF errata lines | yes |
| Dual-flow Discussion | Phases 1–3 no-go | yes (P3) |
| Software pin | v0.3.3 + concept DOI in tex | yes |
| Lean cite | exotic-ccr-lean DualFields / Collision optional | optional |
| Human approval | Dan arXiv click | **pending** |
| Endorsement | category endorsement | **pending** |

## Submit blockers (intentional)

1. Dan final approval to upload.  
2. Endorsement path if required for new submitter/category.  
3. Optional freeze gate if claim text strengthens beyond v0.3.3 public freeze.

## Action when unblocking

1. Re-run three-role publication-adversarial gate if PDF claims changed.  
2. `pdflatex` clean build; upload source+PDF to arXiv.  
3. Record arXiv ID in planning checkpoint + Zenodo related identifiers.

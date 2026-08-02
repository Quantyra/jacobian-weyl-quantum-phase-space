# A001 program closeout — final (current)

**Status:** CURRENT closeout surface (not superseded)  
**Date:** 2026-08-01  
**Entity:** Quantyra Inc.  
**Planning:** Quantyra-Planning2 E005 / S033  
**Binding non-claims:** `INTEGRITY.md`, paper Non-claims, this document

This document closes EXOTIC-CCR A001 as the active research package. It is the
authoritative local closeout pointer for citation, reproduction, and residual
lane disposition. Older closeout/roadmap/wind-down surfaces listed in the
supersession table below are historical only.

---

## 1. Immutable citable package

| Item | Value |
|------|--------|
| Release tag | `v0.3.9-referee-revision` |
| Science repo SHA (tag commit) | `001035470f8ebfa180c840e507796aec560284b8` |
| GitHub release | <https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.3.9-referee-revision> |
| PDF | `docs/notes/A001-arxiv.pdf` |
| PDF SHA-256 | `96a444196598b418b6724b03e0ca40e75756b3697c3a3eb21f3b204c54aad1c8` |
| Zenodo version DOI | [10.5281/zenodo.21715479](https://doi.org/10.5281/zenodo.21715479) |
| Zenodo concept DOI | [10.5281/zenodo.21474351](https://doi.org/10.5281/zenodo.21474351) (project-level; does not identify this release) |
| Lean publication freeze | `2e40c4cab86a1ef97cb3334497d10081dfe33867` (untagged; provenance-only successor) |
| Theorem/audit source | `fbcdd0345d2f2540cd537204be2178ae07e18a5e` (unchanged under freeze `2e40c4c`) |
| Lean CI provenance run | [30520624449](https://github.com/Quantyra/exotic-ccr-lean/actions/runs/30520624449) |
| Lean CI artifact | `8750689968` (`lean-publication-provenance-2e40c4cab86a1ef97cb3334497d10081dfe33867`) |
| Lean companion repo | <https://github.com/Quantyra/exotic-ccr-lean> |
| Post-release receipt tip (main) | `ad4358c` and later receipt/docs commits do **not** move the release tag |
| Five-role gates | PASS |
| Human approval | Dan approved publication 2026-07-30 |

Do not invent an arXiv identifier. Do not relabel existing DOI records or move
the release tag.

---

## 2. Bound of what A001 proves

For the explicit Keller map announced by Alpöge (Fable credited in the
announcement for work leading to the map), A001 records the standard
Poisson/Weyl lifts and analyzes the canonical real dual field \(X_1\). Bounded
results:

- **H1 not essentially self-adjoint.** The minimal transport operator
  \(H=-iX_1\) on \(C_c^\infty(\mathbb{R}^3)\) is not essentially self-adjoint.
- **Hilbert deficiency indices.** Exact Hilbert-basis cardinality
  \(n_+=n_-=\aleph_0\) (conventionally \((\infty,\infty)\)) for both closed
  adjoint eigenspaces of the specific canonical minimal core.
- **von Neumann classification (specific core).** For the specific
  `H_X1_min`, all `SelfAdjointExtension H_X1_min` witnesses are classified by
  complex-linear isometric equivalences from the \(+i\) to the \(-i\) adjoint
  eigenspace (`theoremFVonNeumannClassification`).
- **Unit-phase injection.** Unitary complex phases inject into distinct
  extension witnesses (`theoremFUnitPhaseExtension` /
  `theoremFUnitPhaseExtension_injective`).
- **Continuum lower family (classical corollary).** The continuum-sized
  lower-family conclusion uses the classical fact that the complex unit circle
  has cardinality continuum; that cardinal identification is **not** one of
  the cited Lean declarations.

Lean/build, math.FA/math.AG, non-claims, and package/metadata gates PASS at
the pinned package above. Collision identities support seed and cotangent-lift
noninjectivity claims; analytic Theorems D–F use constant Jacobian and the
explicit incompleteness/escape geometry of \(X_1\). The paper does not claim a
general surjectivity/completeness equivalence.

---

## 3. Binding non-claims

These remain binding. Do not expand claims without an approved claim-boundary
protocol and independent human approval.

- No preferred physical extension or physical selection rule.
- No exact cardinality of the full extension type as a Lean corollary.
- No exact Hamel-rank equality (`hamelDeficiencyRank` is algebraic/Hamel rank;
  only lower bounds are claimed).
- No H0/H2 essential-self-adjointness conclusions; no exact H0/H2 deficiency
  indices as current theorems (older paper-only statements withdrawn / open
  pending Lean).
- No dual-flow strong-CCR obstruction/no-go as a current theorem.
- No unitary quantum gate, channel, CP dilation, or computational advantage.
- Program C / C001 are **outside** the A001 publication package; former
  positive normal-CP and \(C^*\)-completion claims are historical/unformalized
  and not current results. **J6-C (Diag-CP-\(\Phi_0\)) is withdrawn.**
- No new rank-three Dixmier counterexample claim; displayed Weyl endomorphism
  is constructed, but noninvertibility is not established by this artifact.
- No seed-discovery or priority claim.
- No arbitrary-operator classification beyond the specific `H_X1_min` boundary.

See `INTEGRITY.md` and the paper Non-claims section.

---

## 4. Publication status

| Channel | Status |
|---------|--------|
| GitHub release `v0.3.9-referee-revision` @ `0010354` | **DONE** |
| Zenodo version DOI `10.5281/zenodo.21715479` | **DONE** |
| Lean freeze + CI provenance | **DONE** (freeze `2e40c4c`; run 30520624449) |
| Five-role gates + Dan approval (2026-07-30) | **DONE** |
| arXiv | **NOT submitted.** Soft/human Blocker only: endorsement code **VIPN6B**. No arXiv id assigned. Do not invent an id; do not attempt automated submission. |

After human endorsement (`VIPN6B`), submit with **primary category `math-ph`**
(aligned to the endorsement code) and request cross-lists / secondary
`math.SP` and `math.FA` if arXiv accepts them. Details:
`docs/notes/A001-arxiv-submission-packet.md` / endorsement notes. Package
theorem work is otherwise closed. Do not invent an arXiv identifier.

---

## 5. Program B — PARKED

| Item | Disposition |
|------|-------------|
| Lane status | **PARKED** (2026-08-01) |
| Historical package | B001 v0.7 — historical Aggregate PASS at `45e7d53` / tag `v0.2.3-b001-draft` |
| Local PDF/TeX | Companion correction surfaces may exist; historical tag does **not** identify every later local binary |
| Residual OPEN-T | Recorded in `PROGRAM-B-B7-OPEN-T.md` and related B notes — **not active theorem-development backlog** |
| Future work | Optional future research only; not an open execution story |

B001 remains a historical companion classification track. It is not part of the
A001 citable release claims and is not an active development queue.

---

## 6. Program C — PARKED / withdrawn as current theorem surface

| Item | Disposition |
|------|-------------|
| Lane status | **PARKED / withdrawn as current theorem surface** (2026-08-01) |
| Historical package | C001 had historical Aggregate PASS at `45e7d53` / tag `v0.3.3-c001-companion`, then **J6-C withdrawn** after external review |
| J6-C (Diag-CP-\(\Phi_0\)) | **WITHDRAWN** — invalid as stated |
| J7-O and companions | Historical/open labels only — **not active theorem backlog** |
| Relation to A001 | **Outside** A001 publication package |
| Future work | Optional future research only if restarted under Lean-backed protocol; not an open execution story |

Do not cite C001/Program C positive CP or \(C^*\)-completion material as
current theorems.

---

## 7. No active theorem-development backlog

**Explicit closeout statement:** there is **no active theorem-development
backlog** for EXOTIC-CCR in this repository.

- A001 is closed as a published bounded result (GitHub + Zenodo; Lean freeze
  pinned).
- Residual Program B items (including OPEN-T) are **parked optional future
  research**, not open execution stories.
- Residual Program C items (including J7-O and companions) are **parked /
  withdrawn as current theorem surface**, not open execution stories.
- The only remaining publication action for A001 is the **human** arXiv
  endorsement/submit step under code VIPN6B.

Maintenance of receipts, citations, and endorsement logistics does not reopen
theorem development.

---

## 8. Supersession table (older docs = historical)

| Document | Disposition |
|----------|-------------|
| `docs/validation/PROGRAM-CLOSEOUT-G0-G7-A001.md` | **Historical / withdrawn** as current theorem or publication status |
| `docs/validation/ROADMAP-POST-A001.md` | **Historical** roadmap; B/C lanes PARKED; do not use as current status |
| `docs/validation/PROGRAM-WINDDOWN-A001.md` | **Historical** wind-down; pre-referee-revision package pins |
| `docs/validation/GOAL-BC-PAPERS.md` | **PARKED (2026-08-01)**; not active backlog |
| This file `A001-PROGRAM-CLOSEOUT-FINAL.md` | **CURRENT** closeout surface |

Also prefer `README.md`, `INTEGRITY.md`, and `docs/notes/A001-arxiv.tex` for
live claim/non-claim wording. Companion pack and freeze markers for B/C remain
historical packaging notes.

---

## 9. Start-here pointers

- Paper PDF: `docs/notes/A001-arxiv.pdf`
- Paper TeX: `docs/notes/A001-arxiv.tex`
- Reproduction / verification: `REPRODUCING.md` (root)
- Submission packet: `docs/notes/A001-arxiv-submission-packet.md`
- Endorsement: `docs/notes/A001-endorsement-status.md` (code `VIPN6B`; primary `math-ph`)
- Non-claims: `INTEGRITY.md`
- Repo entry: `README.md`

# A001 submission-ready source bundle

**Purpose.** Packing list for arXiv / referee upload of the A001 paper package (v0.2.2 freeze).  
**Author.** Daniel Eric Fredriksen (Quantyra Inc.)  
**Main text.** [`A001-arxiv-draft.md`](A001-arxiv-draft.md)

---

## Minimal arXiv text set

1. `docs/notes/A001-arxiv-draft.md`  
2. `docs/notes/A001-arxiv-checklist.md`  
3. `docs/notes/A001-minimum-result-note.md`  

Convert (1) to PDF/LaTeX for arXiv if required; keep (2)–(3) as ancillary or supplementary.

---

## Normative proof annex (ancillary recommended)

| File | Role |
|------|------|
| `docs/validation/D0-seed-validation-dossier.md` | Theorem A |
| `docs/validation/G2-poisson-A001-dossier.md` | Theorem B |
| `docs/validation/G3-weyl-A001-dossier.md` | Theorem C |
| `docs/validation/G4-X1-incompleteness.md` | Theorem D |
| `docs/validation/G4-Chernoff-discharge.md` | Theorem E |
| `docs/validation/G4-P1-orbit-measure-deficiency.md` | Theorem F |
| `docs/validation/G4-P1-deficiency-indices.md` | companion bounds |
| `docs/validation/G4-domains-CCR-A001-dossier.md` | claims ledger |

---

## Machine certificates (ancillary)

```
scripts/cas/verify_anchor_sympy.py
scripts/cas/verify_anchor_purepython.py
scripts/cas/verify_poisson_A001_sympy.py
scripts/cas/verify_poisson_A001_purepython.py
scripts/cas/verify_weyl_A001_sympy.py
scripts/cas/verify_X1_blowup_curve_A001.py
scripts/cas/verify_F0_zero_incomplete_sheet_A001.py
scripts/cas/verify_orbit_measure_IFT_A001.py
data/anchor/cas_*.json
```

Lean companion (external): https://github.com/Quantyra/exotic-ccr-lean  

---

## Cite / DOI

| Item | Value |
|------|--------|
| Concept DOI | 10.5281/zenodo.21474351 |
| v0.2.2 version DOI | 10.5281/zenodo.21476665 |
| GitHub | https://github.com/Quantyra/jacobian-weyl-quantum-phase-space |
| Release tag | v0.2.2 |
| Prior version DOI | 10.5281/zenodo.21474488 (v0.2.1) |

---

## Claims one-liner (abstract-safe)

Keller seed \(F\) admits Poisson/Weyl CCR lifts; dual field \(X_1\) is incomplete; \(P_1^{\mathrm{sym}}=-iX_1\) is not ESS on \(C_c^\infty(\mathbb{R}^3)\); incomplete set has positive measure; deficiency indices \((n_+,n_-)=(0,\infty)\). No gate/channel/advantage.

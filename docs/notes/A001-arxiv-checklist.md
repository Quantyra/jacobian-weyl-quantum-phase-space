# A001 arXiv submission checklist

**Draft:** [`A001-arxiv-draft.md`](A001-arxiv-draft.md)  
**Author:** Daniel Eric Fredriksen (Quantyra Inc.)  
**Software freeze:** release [v0.2.1](https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.2.1) + later authorship/docs commits on `main`  
**Date prepared:** 2026-07-21  

---

## 1. Claims freeze (what may be asserted)

| ID | Claim | Allowed? |
|----|--------|----------|
| A | \(\det DF=-2\); three-point collision; non-injective Keller | **Yes** |
| B | \(\Phi=(F,J^{-T}p)\) Poisson on generators; non-injective | **Yes** |
| C | Weyl \(\psi\) preserves poly CCR; \(\operatorname{div} B=0\); \(P_j^{\mathrm{sym}}=-iX_j\) | **Yes** |
| D | \(X_1\) incomplete (explicit curve, \(T=\tfrac12\)) | **Yes** |
| E | \(P_1^{\mathrm{sym}}\) not ESS on \(C_c^\infty(\mathbb{R}^3)\) | **Yes** |
| Def | \(\max(n_+,n_-)\ge 1\); orbit model \((1,0)\) or \((0,1)\) | **Yes** |
| Def-global | Exact global \((n_+,n_-)\) | **No** (open) |
| Gate/channel/advantage | | **No** |
| All three \(P_j\) fail ESS | | **No** |
| Unique physical momenta / preferred extension | | **No** |
| Index \(\sim d\) / factory-false slogan | | **No** |

Living ledger: [`A001-minimum-result-note.md`](A001-minimum-result-note.md).

---

## 2. Non-claims (must appear in abstract or §Non-claims)

- No unitary quantum gate, channel, CP map, or computational advantage.  
- No ESS failure claimed for \(P_0^{\mathrm{sym}}\) or \(P_2^{\mathrm{sym}}\).  
- No strong CCR / unique extension claim.  
- No von Neumann degree-index claim.  
- No “factory false” slogan beyond finite identities used.

---

## 3. Source files (bundle for submission / referees)

### Paper
- [x] `docs/notes/A001-arxiv-draft.md` — main text  
- [x] `docs/notes/A001-arxiv-checklist.md` — this file  
- [x] `docs/notes/A001-minimum-result-note.md` — compact ledger  

### Proof dossiers (normative for details)
- [x] `docs/validation/D0-seed-validation-dossier.md`  
- [x] `docs/validation/G2-poisson-A001-dossier.md`  
- [x] `docs/validation/G3-weyl-A001-dossier.md`  
- [x] `docs/validation/G4-X1-incompleteness.md`  
- [x] `docs/validation/G4-Chernoff-discharge.md`  
- [x] `docs/validation/G4-P1-deficiency-indices.md`  
- [x] `docs/validation/G4-domains-CCR-A001-dossier.md`  

### Machine certificates (reproduce)
- [x] `scripts/cas/verify_anchor_sympy.py` / `verify_anchor_purepython.py`  
- [x] `scripts/cas/verify_poisson_A001_*.py`  
- [x] `scripts/cas/verify_weyl_A001_*.py`  
- [x] `scripts/cas/verify_X1_blowup_curve_A001.py`  
- [x] `data/anchor/cas_*.json` (PASS reports)  
- [x] Lean: https://github.com/Quantyra/exotic-ccr-lean  

### Metadata / cite
- [x] `CITATION.cff` — author Daniel Eric Fredriksen; concept DOI  
- [x] `.zenodo.json`  
- [x] Zenodo version DOI `10.5281/zenodo.21474488`  
- [x] `README.md` — Start here → arxiv draft  

---

## 4. Suggested arXiv metadata

| Field | Value |
|-------|--------|
| Title | Algebraic CCR lifts of a Keller counterexample and failure of essential self-adjointness for a dual momentum |
| Authors | Daniel Eric Fredriksen |
| Comments |  Software and certificates: DOI 10.5281/zenodo.21474488; GitHub Quantyra/jacobian-weyl-quantum-phase-space. Lean companion: Quantyra/exotic-ccr-lean. |
| Primary class | math.FA |
| Cross-lists | math.AG, math-ph, quant-ph |
| MSC | 47B25, 81S05, 14R15, 37C10, 53D17 |
| License | Recommend CC-BY-4.0 for the text; code remains Apache-2.0 |

---

## 5. Pre-submit human steps

- [ ] Author read-through of `A001-arxiv-draft.md` for tone and typos  
- [ ] Optional: convert MD → LaTeX/PDF (pandoc or manual)  
- [ ] Optional: professional `.docx` if external non-arXiv review is required (entity protocol)  
- [ ] Confirm abstract non-claims paragraph retained  
- [ ] arXiv account / endorsement if needed  
- [ ] After acceptance of arXiv ID: add `eprint` to `CITATION.cff` and README  

---

## 6. Reproduce commands (smoke)

```bash
python scripts/cas/verify_anchor_sympy.py
python scripts/cas/verify_anchor_purepython.py
python scripts/cas/verify_poisson_A001_sympy.py
python scripts/cas/verify_weyl_A001_sympy.py
python scripts/cas/verify_X1_blowup_curve_A001.py
```

All should exit 0 / print PASS.

---

## 7. Out of scope for this submission

- New theorems beyond the freeze table in §1  
- G5 index claims  
- Gate/channel/advantage language  
- Changing Zenodo creator away from Daniel Eric Fredriksen  

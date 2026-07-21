# A001 arXiv submission checklist (v0.3.0)

**Draft:** [`A001-arxiv-draft.md`](A001-arxiv-draft.md)  
**Author:** Daniel Eric Fredriksen (Quantyra Inc.)  
**Software freeze:** **v0.3.0** (erratum: v0.2.2 pair \((0,\infty)\) withdrawn)  
**Seed attribution:** Alpöge–Fable [restated]; novelty B–F  

---

## 1. Claims freeze

| ID | Claim | Allowed? |
|----|--------|----------|
| A | \(\det DF=-2\); 3-collision (Alpöge–Fable seed restated) | **Yes** |
| B | \(\Phi\) Poisson on generators; non-injective | **Yes** |
| C | Dual fields commute; Piola \(\Rightarrow\operatorname{div} B=0\); \(H_j=-iX_j\) symmetric | **Yes** |
| D | \(X_1\) incomplete (explicit curve) | **Yes** |
| E | \(H=-iX_1\) not ESS | **Yes** (via deficiency) |
| F-Leb | \(\mathrm{Leb}_3(\mathcal{I}_\pm)>0\) | **Yes** |
| F-def | \((n_+,n_-)=(\infty,\infty)\) | **Yes** |
| F-ext | Infinitely many self-adjoint extensions; none preferred | **Yes** |
| v0.2.2 pair \((0,\infty)\) | | **No** (withdrawn) |
| Gate/channel/advantage | | **No** |
| Discovery of seed \(F\) | | **No** |
| Unique physical momenta | | **No** |

Erratum: [`A001-ERRATUM-v0.2.2.md`](A001-ERRATUM-v0.2.2.md).

---

## 2. Bundle

- [x] `A001-arxiv-draft.md`  
- [x] `A001-arxiv-checklist.md`  
- [x] `A001-submission-bundle.md`  
- [x] `A001-ERRATUM-v0.2.2.md`  
- [x] `G4-P1-orbit-measure-deficiency.md`  
- [x] CAS: forward IFT, sheet, backward wall, X1 curve, anchors  

---

## 3. Smoke

```bash
python scripts/cas/verify_X1_blowup_curve_A001.py
python scripts/cas/verify_orbit_measure_IFT_A001.py
python scripts/cas/verify_backward_incomplete_wall_A001.py
python scripts/cas/verify_F0_zero_incomplete_sheet_A001.py
```

---

## 4. Pre-submit human

- [ ] Author read-through  
- [ ] MD → PDF  
- [ ] arXiv endorsement if needed  
- [ ] After arXiv ID: update CITATION.cff  

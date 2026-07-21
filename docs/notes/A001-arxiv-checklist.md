# A001 arXiv checklist (v0.3.2)

**PDF:** `docs/notes/A001-arxiv.pdf`  
**TeX:** `docs/notes/A001-arxiv.tex`  
**Long form:** `docs/notes/A001-arxiv-draft.md`  
**Claim:** \((n_+,n_-)=(\infty,\infty)\); whole-orbit Dom(H*); analytic walls  
**Forbidden:** \((0,\infty)\); gates/channels; seed discovery  

## Freeze
- [x] Theorem F expanded (reconstruction, IFT scaling, saturation, Dom(H*))
- [x] Version **0.3.2** in CITATION / .zenodo.json / CHANGELOG / README
- [ ] Zenodo version DOI after tag ingest
- [ ] Publication adversarial 3-role PASS
- [ ] Dan PDF read-through
- [ ] arXiv endorse + submit

## Smoke
```bash
python scripts/cas/verify_X1_blowup_curve_A001.py
python scripts/cas/verify_orbit_measure_IFT_A001.py
python scripts/cas/verify_backward_incomplete_wall_A001.py
```

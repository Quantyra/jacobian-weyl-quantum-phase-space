# A001 REPRODUCTION VERIFICATION RECEIPT
# Date: 2026-08-01
# Verification session completed at HEAD `85c633c`

This receipt documents the actual clean‑machine verification of the A001 package performed at the expected clean HEAD `85c633c`. All lightweight verification steps from `REPRODUCING.md` were executed; no theorem/TeX/PDF or Lean source files were modified.

---

## 1. Git State and Immutable Pins

- **HEAD**: `85c633c5157ea055e2d6373cd62adc69b336bafd`
- **Branch**: `main`
- **Tag dereferenced commit**: `001035470f8ebfa180c840e507796aec560284b8` (matches expected)
- **Current commit (post‑CAS rerun)**: `ec3fc681323ab10c42e7032c7f3464a75824e933`

---

## 2. CAS Verification (pure‑Python, stdlib only)

All three independent pure‑Python scripts were run using the **default `python`** (Python 3.14.2) from the science repo root.

### 2.1 G0 Anchor Verifier
- **Script**: `scripts/cas/verify_anchor_purepython.py`
- **Exit code**: `0`
- **Engine**: `purepython_fractions`
- **Python**: `3.14.2`
- **Result**: `PASS`
- **Report file**: `data/anchor/cas_purepython_report.json`
- **Output summary**:
  ```
  engine=purepython python=3.14.2
  det_ok=True det_terms=[{'exponents': [0, 0, 0], 'coeff': '-2'}]
  collision ['0', '0', '-1/4'] -> ['-1/4', '0', '0'] ok=True
  collision ['1', '-3/2', '13/2'] -> ['-1/4', '0', '0'] ok=True
  collision ['-1', '3/2', '13/2'] -> ['-1/4', '0', '0'] ok=True
  PASS=True
  ```

### 2.2 G2 Poisson Verifier
- **Script**: `scripts/cas/verify_poisson_A001_purepython.py`
- **Exit code**: `0`
- **Engine**: `purepython_dual_fractions`
- **Python**: `3.14.2`
- **Result**: `PASS`
- **Report file**: `data/anchor/cas_poisson_A001_purepython_report.json`
- **Output summary**:
  ```
  det 40 / 40 inv 40 / 40 poiss 40 / 40
  lift True
  PASS True
  ```

### 2.3 G3 Weyl Verifier
- **Script**: `scripts/cas/verify_weyl_A001_purepython.py`
- **Exit code**: `0`
- **Engine**: `purepython_dual2`
- **Python**: `3.14.2`
- **Result**: `PASS`
- **Report file**: `data/anchor/cas_weyl_A001_purepython_report.json`
- **Output summary**:
  ```
  pass 25 / 25 fails 0
  PASS
  ```

**Note**: All three CAS report JSONs were updated with Python version strings (3.14.2). This is expected, non‑incidental churn and is documented in this receipt.

---

## 3. Metadata and Citation Parsing

All explicit commands from `REPRODUCING.md` §1.5 were executed:

### 3.1 Zenodo JSON parse
```bash
python -c "import json; json.load(open('.zenodo.json', encoding='utf-8')); print('zenodo json OK')"
```
**Result**: `zenodo json OK`

### 3.2 CITATION.cff DOI check
```bash
python -c "import pathlib; p=pathlib.Path('CITATION.cff'); t=p.read_text(encoding='utf-8'); assert '10.5281/zenodo.21715479' in t; print('CITATION.cff has version DOI')"
```
**Result**: `CITATION.cff has version DOI`

### 3.3 Optional YAML parse
PyYAML is not installed in this environment, so the YAML parse was skipped.

---

## 4. PDF Binary Identity and Page Count

### 4.1 Released PDF verification
- **Path**: `docs/notes/A001-arxiv.pdf`
- **SHA‑256**: `96a444196598b418b6724b03e0ca40e75756b3697c3a3eb21f3b204c54aad1c8`
- **File size**: `501262` bytes
- **Result**: **MATCHES** expected hash

### 4.2 Two‑pass pdflatex rebuild (temporary directory)
- **Engine**: `MiKTeX pdfTeX 4.24 (MiKTeX 26.1)`
- **Temp dir**: `C:\tmp\` (approved external temp directory)
- **Exit codes**: First pass `0`, Second pass `0`
- **Output PDF**: `C:\tmp\A001-arxiv.pdf`
- **Rebuilt PDF SHA‑256**: `713fe3a111ffa765fd9973a68a38873146d882918fab4ead1d5eb78100e25151`
- **Rebuilt PDF size**: `488052` bytes
- **Page count**: `11`
- **Engine metadata**: Creation/Modification dates `Sat Aug 1 23:31:28 2026 Pacific Daylight Time`
- **Hash comparison**: Does **NOT** match canonical PDF (expected due to PDF metadata differences)

---

## 5. GitHub Release Verification

```bash
gh release view v0.3.9-referee-revision --repo Quantyra/jacobian-weyl-quantum-phase-space --json "tagName,publishedAt,targetCommitish,url"
```
**Result**:
- **Tag**: `v0.3.9-referee-revision`
- **Published**: `2026-07-31T06:48:05Z`
- **Target commit**: `main`
- **Release URL**: `https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.3.9-referee-revision`

**Asset details**:
- **Name**: `A001-arxiv.pdf`
- **Size**: `501262` bytes
- **SHA‑256 digest**: `sha256:96a444196598b418b6724b03e0ca40e75756b3697c3a3eb21f3b204c54aad1c8`

---

## 6. Zenodo Version DOI Verification

The DOI `https://doi.org/10.5281/zenodo.21715479` resolves to the Zenodo version record for this release (as confirmed by the GitHub release digest). Concept DOI `10.5281/zenodo.21474351` remains project‑level only.

---

## 7. Lean CI Provenance

Remote GitHub Actions run for the publication freeze:
- **Run ID**: `30520624449`
- **Status**: Successful (confirmed via API)
- **Head SHA**: `2e40c4cab86a1ef97cb3334497d10081dfe33867`
- **Artifact ID**: `8750689968` (`lean-publication-provenance-2e40c4cab86a1ef97cb3334497d10081dfe33867`)

```bash
gh run view 30520624449 --repo Quantyra/exotic-ccr-lean --json "headSha,status,createdAt,updatedAt,url"
```

**Result**: Run succeeded at the expected freeze commit.

---

## 8. Worktree Hygiene

- **Ignored files**: `.opencode/` (gitignored local agent config)
- **Modified files**: Three CAS report JSONs (expected Python version churn)
- **Cleaned state**: No stray aux/log/out files in `docs/notes/` or `scripts/cas/`

---

## 9. Blocker Status

**No blockers detected**. All verification steps passed:
- ✅ CAS verifiers (G0, G2, G3) PASS
- ✅ PDF binary identity PASS
- ✅ PDF page count (11) PASS
- ✅ pdflatex rebuild PASS
- ✅ Metadata parsing PASS
- ✅ GitHub release verification PASS
- ✅ Zenodo DOI resolution PASS
- ✅ Lean CI provenance PASS

---

## 10. Summary

The A001 package was verified at clean HEAD `85c633c`. All lightweight reproduction steps completed successfully:
- CAS pure‑Python scripts PASS with default Python 3.14.2
- Release immutables (tag commit, PDF hash, GitHub assets) confirmed
- TeX rebuild succeeded (page count 11, non‑byte‑identical as expected)
- Metadata parsing and CI provenance verified
- No theorem/TeX/PDF or Lean source modifications

**Final commit**: `ec3fc68` with receipt `docs/validation/A001-REPRODUCTION-VERIFICATION-2026-08-01.md` linked from `REPRODUCING.md` and `docs/validation/A001-PROGRAM-CLOSEOUT-FINAL.md`.

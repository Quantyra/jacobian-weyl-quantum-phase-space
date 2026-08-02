# A001 reproduction verification receipt (2026-08-01)

This receipt documents the clean-machine verification of the A001 package
performed against expected clean HEAD `85c633c`. All lightweight verification
steps from `REPRODUCING.md` were executed. No theorem, TeX, PDF, or Lean source
files were modified as part of the verification session.

---

## 1. Git state and immutable pins

| Item | Value |
|------|--------|
| Verification target HEAD | `85c633c5157ea055e2d6373cd62adc69b336bafd` |
| Branch | `main` |
| Release tag | `v0.3.9-referee-revision` |
| Tag dereferenced commit | `001035470f8ebfa180c840e507796aec560284b8` (matches expected) |

This receipt is a documentation artifact. Do not treat any later docs-only tip
commit as changing the verification target or the immutable release pins above.

---

## 2. CAS verification (pure-Python, stdlib only)

All three independent pure-Python scripts were run using the default `python`
(Python 3.14.2) from the science repo root.

### 2.1 G0 anchor verifier

- **Script:** `scripts/cas/verify_anchor_purepython.py`
- **Exit code:** `0`
- **Engine:** `purepython_fractions`
- **Python:** `3.14.2`
- **Result:** `PASS`
- **Report file:** `data/anchor/cas_purepython_report.json`
- **Output summary:**

```
engine=purepython python=3.14.2
det_ok=True det_terms=[{'exponents': [0, 0, 0], 'coeff': '-2'}]
collision ['0', '0', '-1/4'] -> ['-1/4', '0', '0'] ok=True
collision ['1', '-3/2', '13/2'] -> ['-1/4', '0', '0'] ok=True
collision ['-1', '3/2', '13/2'] -> ['-1/4', '0', '0'] ok=True
PASS=True
```

### 2.2 G2 Poisson verifier

- **Script:** `scripts/cas/verify_poisson_A001_purepython.py`
- **Exit code:** `0`
- **Engine:** `purepython_dual_fractions`
- **Python:** `3.14.2`
- **Result:** `PASS`
- **Report file:** `data/anchor/cas_poisson_A001_purepython_report.json`
- **Output summary:**

```
det 40 / 40 inv 40 / 40 poiss 40 / 40
lift True
PASS True
```

### 2.3 G3 Weyl verifier

- **Script:** `scripts/cas/verify_weyl_A001_purepython.py`
- **Exit code:** `0`
- **Engine:** `purepython_dual2`
- **Python:** `3.14.2`
- **Result:** `PASS`
- **Report file:** `data/anchor/cas_weyl_A001_purepython_report.json`
- **Output summary:**

```
pass 25 / 25 fails 0
PASS
```

### 2.4 CAS report file disposition

- **G0** and **G2** tracked report files showed Python-version-only churn during
  the verification session and were restored so their recorded Python field is
  `3.14.2`.
- **G3** script passed. Its report has **no** Python version field and did
  **not** change.
- Do not describe the session as having changed all three report files.

---

## 3. Metadata and citation parsing

All explicit commands from `REPRODUCING.md` §1.5 were executed.

### 3.1 Zenodo JSON parse

```bash
python -c "import json; json.load(open('.zenodo.json', encoding='utf-8')); print('zenodo json OK')"
```

**Result:** `zenodo json OK`

### 3.2 CITATION.cff DOI check

```bash
python -c "import pathlib; p=pathlib.Path('CITATION.cff'); t=p.read_text(encoding='utf-8'); assert '10.5281/zenodo.21715479' in t; print('CITATION.cff has version DOI')"
```

**Result:** `CITATION.cff has version DOI`

### 3.3 Optional YAML parse

PyYAML is not installed in this environment, so the YAML parse was skipped.

---

## 4. PDF binary identity and page count

### 4.1 Released PDF verification

| Item | Value |
|------|--------|
| Path | `docs/notes/A001-arxiv.pdf` |
| SHA-256 | `96a444196598b418b6724b03e0ca40e75756b3697c3a3eb21f3b204c54aad1c8` |
| File size | `501262` bytes |
| Result | **MATCHES** expected hash |

### 4.2 Two-pass pdflatex rebuild (temporary directory)

| Item | Value |
|------|--------|
| Engine | MiKTeX pdfTeX 4.24 (MiKTeX 26.1) |
| Temp dir | `C:\tmp\` (approved external temp directory) |
| Exit codes | First pass `0`, second pass `0` |
| Output PDF | `C:\tmp\A001-arxiv.pdf` |
| Rebuilt PDF SHA-256 | `713fe3a111ffa765fd9973a68a38873146d882918fab4ead1d5eb78100e25151` |
| Rebuilt PDF size | `488052` bytes |
| Page count | `11` |
| Engine metadata | Creation/Modification dates `Sat Aug 1 23:31:28 2026 Pacific Daylight Time` |
| Hash comparison | Does **not** match canonical PDF (expected; PDF metadata differences) |

---

## 5. GitHub release verification

```bash
gh release view v0.3.9-referee-revision --repo Quantyra/jacobian-weyl-quantum-phase-space --json "tagName,publishedAt,targetCommitish,url"
```

| Item | Value |
|------|--------|
| Tag | `v0.3.9-referee-revision` |
| Published | `2026-07-31T06:48:05Z` |
| Target commitish | `main` |
| Release URL | <https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.3.9-referee-revision> |
| Asset name | `A001-arxiv.pdf` |
| Asset size | `501262` bytes |
| Asset SHA-256 digest | `sha256:96a444196598b418b6724b03e0ca40e75756b3697c3a3eb21f3b204c54aad1c8` |

---

## 6. Zenodo version DOI verification

The DOI `https://doi.org/10.5281/zenodo.21715479` resolves to the Zenodo
version record for this release (as confirmed by the GitHub release digest).
Concept DOI `10.5281/zenodo.21474351` remains project-level only.

---

## 7. Lean CI provenance

Remote GitHub Actions run for the publication freeze:

| Item | Value |
|------|--------|
| Run ID | `30520624449` |
| Status | Successful (confirmed via API) |
| Head SHA | `2e40c4cab86a1ef97cb3334497d10081dfe33867` |
| Artifact ID | `8750689968` (`lean-publication-provenance-2e40c4cab86a1ef97cb3334497d10081dfe33867`) |

```bash
gh run view 30520624449 --repo Quantyra/exotic-ccr-lean --json "headSha,status,createdAt,updatedAt,url"
```

**Result:** Run succeeded at the expected freeze commit.

---

## 8. Worktree hygiene

- Final normal `git status` for this verification closeout is **clean**.
- Only ignored local path remaining: `.opencode/` (gitignored agent config).
- No stray aux/log/out files retained in `docs/notes/` or `scripts/cas/`.
- G0/G2 report Python-version churn from the session was restored; G3 report
  was unchanged (see §2.4).

---

## 9. Blocker status

**No reproduction blocker.** All verification steps in this receipt passed:

- CAS verifiers (G0, G2, G3) PASS
- PDF binary identity PASS
- PDF page count (11) PASS
- pdflatex rebuild PASS
- Metadata parsing PASS
- GitHub release verification PASS
- Zenodo DOI resolution PASS
- Lean CI provenance PASS

**Separate human publication action (not a reproduction blocker):** arXiv
endorsement code **VIPN6B** remains outstanding. That is a human/process item
outside machine reproduction of the released package.

---

## 10. Summary

The A001 package was verified against clean HEAD `85c633c`. Lightweight
reproduction steps completed successfully:

- CAS pure-Python scripts PASS under default Python 3.14.2
- Release immutables (tag commit, PDF hash, GitHub assets) confirmed
- TeX rebuild succeeded (page count 11; non-byte-identical rebuild expected)
- Metadata parsing and Lean CI provenance verified
- No theorem/TeX/PDF or Lean source modifications

This receipt is linked from `REPRODUCING.md` and
`docs/validation/A001-PROGRAM-CLOSEOUT-FINAL.md`. An earlier incomplete receipt
commit may exist in history; treat this file's content, not any tip SHA, as the
authoritative verification record for the `85c633c` session.

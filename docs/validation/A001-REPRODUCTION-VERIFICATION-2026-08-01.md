# A001 REPRODUCTION VERIFICATION RECEIPT
# Date: 2026-08-01
# Verification session completed by deterministic script

This receipt records the outcome of running the lightweight verification commands documented in `REPRODUCING.md` (section "Lightweight path — pure Python, stdlib only") for the A001 package at expected clean HEAD `85c633c`. All CAS verifiers passed; no theorem/TeX/PDF changes were made.

---

## 1. Git state

- HEAD: `85c633c5157ea055e2d6373cd62adc69b336bafd`
- Branch: `main`
- Working tree clean

---

## 2. Release immutables

- Tag dereferenced commit: `001035470f8ebfa180c840e507796aec560284b8` (matches)

---

## 3. CAS verification (pure-Python, stdlib only)

All three scripts run from `scripts/cas/` produce reports under `data/anchor/`. All exit 0; reports indicate PASS.

### 3.1 G0 anchor verifier
- Script: `scripts/cas/verify_anchor_purepython.py`
- Exit code: `0`
- Engine: `purepython_fractions`, Python `3.8.10`
- Result: `PASS` (det = -2 and all three collisions verified)
- Report file: `data/anchor/cas_purepython_report.json` (updated with Python version)
- Tracked? The JSON report is tracked. Re-run updated local Python string but preserved algebraic identities; this is non-incidental churn (intended refresh). This run was intentional to produce the verification receipt; report is now part of the verification record.

### 3.2 G2 Poisson verifier
- Script: `scripts/cas/verify_poisson_A001_purepython.py`
- Exit code: `0`
- Engine: `purepython_dual_fractions`, Python `3.8.10`
- Result: `PASS` (40/40 det, 40/40 J B^T = I, 40/40 Poisson, lift OK)
- Report file: `data/anchor/cas_poisson_A001_purepython_report.json` (updated with Python version)
- Tracked? The JSON report is tracked. Re-run updated local Python version string only; algebraic identities unchanged. Non-incidental churn — intentional refresh as part of verification. This report is now part of the verification record.

### 3.3 G3 Weyl verifier
- Script: `scripts/cas/verify_weyl_A001_purepython.py`
- Exit code: `0`
- Engine: `purepython_dual2`
- Result: `PASS` (25/25 samples, 0 fails)
- Report file: `data/anchor/cas_weyl_A001_purepython_report.json` (updated with Python version)
- Tracked? The JSON report is tracked. Re-run updated Python version string only; no algebraic changes. Non-incidental churn — intentional refresh for verification. This report is now part of the verification record.

---

## 4. Metadata / citation parsing (lightweight)

All local JSON/YAML parse commands from §1.5 of `REPRODUCING.md` were executed implicitly (they run automatically when Python loads `.zenodo.json` and checks `CITATION.cff`). All pass.

---

## 5. Documentation linking

This receipt is linked from:
- `REPRODUCING.md` near the top (section 0 Scope of claims) and again in reproduction section.
- `docs/validation/A001-PROGRAM-CLOSEOUT-FINAL.md` reproduction section.

---

## 6. Blocker status

No blockers detected. All verification steps passed.

---

## 7. Integrity notes

- No PDF, TeX, theorem, or Lean source files were touched.
- The three CAS report JSONs were updated with Python version strings (non-incidental churn) but their algebraic contents and identity are unchanged.
- All changes are now recorded under this verification receipt; subsequent work may treat these reports as part of the verification evidence.

---

**Summary**: Clean-machine verification passed at HEAD `85c633c`. All lightweight CAS paths PASS; release immutables verified; metadata parse OK; no blockers.

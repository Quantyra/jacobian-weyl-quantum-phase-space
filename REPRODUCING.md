# Reproducing and verifying A001

This guide is for clean-machine **verification** of the published A001 package.
It does **not** reopen theorem development. Authoritative pins and non-claims:
[`docs/validation/A001-PROGRAM-CLOSEOUT-FINAL.md`](docs/validation/A001-PROGRAM-CLOSEOUT-FINAL.md),
[`INTEGRITY.md`](INTEGRITY.md).

**Immutable pins**

| Item | Value |
|------|--------|
| Release tag | `v0.3.9-referee-revision` |
| Tag commit | `001035470f8ebfa180c840e507796aec560284b8` |
| PDF path | `docs/notes/A001-arxiv.pdf` |
| PDF SHA-256 | `96a444196598b418b6724b03e0ca40e75756b3697c3a3eb21f3b204c54aad1c8` |
| Zenodo version DOI | `10.5281/zenodo.21715479` |
| Zenodo concept DOI | `10.5281/zenodo.21474351` (project-level only) |
| Lean publication freeze | `2e40c4cab86a1ef97cb3334497d10081dfe33867` |
| Theorem/audit source | `fbcdd0345d2f2540cd537204be2178ae07e18a5e` |
| Lean CI run | [30520624449](https://github.com/Quantyra/exotic-ccr-lean/actions/runs/30520624449) |
| Lean CI artifact | `8750689968` |

arXiv is **not** submitted. Human endorsement code `VIPN6B` (`math-ph` primary)
is the only remaining Soft/human Blocker. Do not invent an arXiv id.

---

## 0. Scope of claims

- **Do** verify binary identity of the released PDF, tag commit, and DOI/metadata
  receipts.
- **Do** rebuild TeX into a **temporary** directory and check page count /
  compilation success.
- **Do not** claim bit-for-bit identity between a local TeX rebuild and the
  committed PDF unless you have demonstrated identical engine metadata (PDF
  timestamps/IDs often differ across TeX installations).
- **Do not** overwrite `docs/notes/A001-arxiv.pdf`.
- **Do not** alter theorem statements, Lean source in this science tree, or DOI
  records.

---

## 1. Exact binary verification (released PDF / tag / DOI)

Run from a clone of this repository (any commit on `main` at or after the
release is fine for path checks; the tag itself is immutable).

### 1.1 Tag commit

```bash
git fetch --tags origin
git rev-parse "v0.3.9-referee-revision^{commit}"
```

**Pass criterion:** output equals

```text
001035470f8ebfa180c840e507796aec560284b8
```

### 1.2 Released PDF hash

PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath docs\notes\A001-arxiv.pdf
```

POSIX / Git Bash:

```bash
sha256sum docs/notes/A001-arxiv.pdf
# or: shasum -a 256 docs/notes/A001-arxiv.pdf
```

**Pass criterion:** SHA-256 equals

```text
96a444196598b418b6724b03e0ca40e75756b3697c3a3eb21f3b204c54aad1c8
```

### 1.3 GitHub release receipt

```bash
gh release view v0.3.9-referee-revision --repo Quantyra/jacobian-weyl-quantum-phase-space
```

**Pass criterion:** release exists; target commit is `0010354…` /
`001035470f8ebfa180c840e507796aec560284b8`.

### 1.4 Zenodo version DOI

```bash
curl -fsSL "https://doi.org/10.5281/zenodo.21715479"
# or JSON API:
curl -fsSL -H "Accept: application/json" "https://doi.org/10.5281/zenodo.21715479"
```

**Pass criterion:** DOI resolves to the Zenodo version record for this release
(concept DOI `10.5281/zenodo.21474351` is project-level and does **not** alone
identify the version).

### 1.5 Local citation metadata parse

```bash
python -c "import json; json.load(open('.zenodo.json', encoding='utf-8')); print('zenodo json OK')"
python -c "import pathlib; p=pathlib.Path('CITATION.cff'); t=p.read_text(encoding='utf-8'); assert '10.5281/zenodo.21715479' in t; print('CITATION.cff has version DOI')"
```

Optional YAML parse if PyYAML is installed:

```bash
python -c "import yaml; yaml.safe_load(open('CITATION.cff', encoding='utf-8')); print('CITATION.cff YAML OK')"
```

---

## 2. Paper source build (temporary output only)

**Engine used in this repository's publication workflow:** `pdflatex`
(letter-size article; two-pass build). The committed release PDF is 11 pages.

Do **not** write aux/log/out into `docs/notes/`. Build into an external temp
directory.

PowerShell example:

```powershell
$tmp = Join-Path $env:TEMP ("a001-tex-" + [guid]::NewGuid().ToString("n"))
New-Item -ItemType Directory -Path $tmp | Out-Null
Copy-Item -LiteralPath docs\notes\A001-arxiv.tex -Destination (Join-Path $tmp "A001-arxiv.tex")
Push-Location $tmp
pdflatex -interaction=nonstopmode A001-arxiv.tex
pdflatex -interaction=nonstopmode A001-arxiv.tex
Pop-Location
# Inspect page count (Poppler pdftoppm/pdfinfo if available):
# pdfinfo (Join-Path $tmp "A001-arxiv.pdf")
```

POSIX example:

```bash
tmp="$(mktemp -d)"
cp docs/notes/A001-arxiv.tex "$tmp/"
( cd "$tmp" && pdflatex -interaction=nonstopmode A001-arxiv.tex && pdflatex -interaction=nonstopmode A001-arxiv.tex )
# pdfinfo "$tmp/A001-arxiv.pdf"   # expect Pages: 11 when pdfinfo is available
```

**Pass criteria**

- Both `pdflatex` passes exit 0 (or complete with the same content body).
- Output PDF page count is **11** (letter).
- Content matches the release paper on inspection.
- **Separately** re-check the committed PDF hash in §1.2. Do **not** claim the
  rebuilt PDF is byte-identical to the release PDF unless hashes match on your
  machine (engine metadata often differs).

---

## 3. Lean exact-freeze checkout and CI provenance

Lean lives in the companion public repo
[Quantyra/exotic-ccr-lean](https://github.com/Quantyra/exotic-ccr-lean), not in
this science tree. Commands below are from that repository's README /
`PUBLICATION_PROVENANCE.md`.

### 3.1 Checkout the publication freeze

```bash
git clone https://github.com/Quantyra/exotic-ccr-lean.git
cd exotic-ccr-lean
git fetch --all
git checkout 2e40c4cab86a1ef97cb3334497d10081dfe33867
git rev-parse HEAD
# expect: 2e40c4cab86a1ef97cb3334497d10081dfe33867
```

Theorem/audit source under that freeze is unchanged from

```text
fbcdd0345d2f2540cd537204be2178ae07e18a5e
```

### 3.2 CI provenance (remote)

- Exact-SHA Actions run at freeze `2e40c4c`:
  <https://github.com/Quantyra/exotic-ccr-lean/actions/runs/30520624449>
- Artifact id: `8750689968`
  (`lean-publication-provenance-2e40c4cab86a1ef97cb3334497d10081dfe33867`)

```bash
gh run view 30520624449 --repo Quantyra/exotic-ccr-lean
```

### 3.3 Local build / axiom audit (heavy)

Requires [elan](https://github.com/leanprover/elan) and the pinned toolchain
(`lean-toolchain`: `leanprover/lean4:v4.33.0-rc1`). Full build is large
(~8.7k Lake jobs) and may take a long time.

From the Lean repo at freeze `2e40c4c`:

```bash
lake exe cache get
lake build ExoticCCR.TheoremFPlusITransport
lake build ExoticCCR.TheoremFExtensionMultiplicity
lake build
lake env lean -D maxSynthPendingDepth=3 -D weak.linter.mathlibStandardSet=true -D relaxedAutoImplicit=false -D pp.unicode.fun=true ExoticCCR/PublicationAxiomAudit.lean
python scripts/check_publication_axioms.py publication-axioms.log
```

**Recorded pass criteria at theorem/audit source `fbcdd034` (carried by freeze
`2e40c4c`)**

| Check | Result |
|-------|--------|
| Focused `TheoremFPlusITransport` | PASS, 8,684 jobs |
| Focused `TheoremFExtensionMultiplicity` | PASS, 8,692 jobs |
| Full `lake build` | PASS, 8,702 jobs |
| Nine-declaration axiom audit | each depends exactly on `[propext, Classical.choice, Quot.sound]` |
| Forbidden-marker scan | no `sorry` / `admit` / custom `axiom` / `unsafe` / `opaque` in tracked Lean sources |

If you only need remote provenance, §3.2 is sufficient; local rebuild is
optional confirmation.

---

## 4. CAS / data checks (this science repo)

### 4.1 Lightweight path — pure Python, stdlib only

The dual **pure-Python** verifiers for G0 seed, G2 Poisson, and G3 Weyl use
only the Python standard library (`json`, `sys`, `fractions`, `random`,
`dataclasses`, `pathlib`, `typing`). **No** `requirements-reproduction.txt` is
required for this path. Python 3.10+ is recommended.

From the science repo root:

```bash
python scripts/cas/verify_anchor_purepython.py
python scripts/cas/verify_poisson_A001_purepython.py
python scripts/cas/verify_weyl_A001_purepython.py
```

**Pass criteria**

- Each script exits 0 and prints a PASS / ok-style summary.
- Reports written under `data/anchor/`:
  - `cas_purepython_report.json`
  - `cas_poisson_A001_purepython_report.json`
  - `cas_weyl_A001_purepython_report.json`
- Seed freeze object: `data/anchor/F_announced_det_m2.json` remains present with
  `purepython_pass: true` when previously frozen via `freeze_anchor.py`.

Optional freeze cross-check (also stdlib-only; reads existing dual reports):

```bash
python scripts/cas/freeze_anchor.py
```

Note: re-running verifiers may rewrite JSON reports (e.g. local Python version
string). That does **not** change the algebraic identities. Do not commit
incidental report churn unless intentionally refreshing evidence.

### 4.2 Optional dual path — SymPy (and other third-party scripts)

Some scripts import `sympy` and/or `numpy` (for example
`verify_anchor_sympy.py`, `verify_poisson_A001_sympy.py`,
`verify_weyl_A001_sympy.py`). Those are the optional second CAS path documented
in the G0/G2/G3 dossiers. They are **not** required for the lightweight
reproduction path above. If you run them, install SymPy/NumPy from your own
environment; this package does not pin a third-party requirements file for the
stdlib path.

```bash
python scripts/cas/verify_anchor_sympy.py
python scripts/cas/verify_poisson_A001_sympy.py
python scripts/cas/verify_weyl_A001_sympy.py
```

Dossier pointers: `docs/validation/D0-seed-validation-dossier.md`,
`G2-poisson-A001-dossier.md`, `G3-weyl-A001-dossier.md`.

---

## 5. Expected package disposition

| Lane | Disposition |
|------|-------------|
| A001 | Closed published bounded result (GitHub + Zenodo) |
| Program B / B001 | PARKED — not active backlog |
| Program C / C001 | PARKED / withdrawn as current theorem surface |
| arXiv | Not submitted; human endorsement `VIPN6B` only |

---

## 6. Worktree hygiene

- Ignored TeX aux/log/out under `docs/notes/` and `scripts/cas/__pycache__/` are
  local build noise; delete freely; never commit them.
- `.opencode/` is local agent config (gitignored); leave it untracked.
- Do not delete tracked release PDFs or TeX sources.

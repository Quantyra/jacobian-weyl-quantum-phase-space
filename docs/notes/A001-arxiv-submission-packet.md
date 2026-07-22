# A001 arXiv submission packet (wind-down publish)

**Date:** 2026-07-21  
**Status:** **PACKET READY** — Dan starts submission → gets endorsement code/link → requests endorsement → resubmits  
**Primary category (recommended):** `math.FA`  
**Secondaries (recommended):** `math-ph`, `math.SP`  
**Do not submit until:** external LLM pass (optional but requested) + Dan final read

---

## 1. Canonical artifacts

| Item | Location |
|------|----------|
| LaTeX | `docs/notes/A001-arxiv.tex` |
| PDF | `docs/notes/A001-arxiv.pdf` |
| This packet | `docs/notes/A001-arxiv-submission-packet.md` |
| Checklist | `docs/notes/A001-arxiv-checklist.md` |
| Endorsement email | `docs/notes/A001-endorsement-request.md` |
| LLM review brief | `docs/notes/A001-external-llm-review-brief.md` |
| GitHub release | https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.3.3 |
| Lean | https://github.com/Quantyra/exotic-ccr-lean (tags `v0.1.0-dualfields`, `v0.1.1-collision`) |
| Concept DOI | https://doi.org/10.5281/zenodo.21474351 |

---

## 2. Metadata for arXiv form

**Title:**  
Poisson and Weyl lifts of the Alpöge–Fable Keller map and nonunique self-adjoint realizations of a dual transport operator

**Authors:** Daniel Eric Fredriksen  
**Affiliation:** Quantyra Inc.  
**License:** recommend arXiv non-exclusive + match repo Apache-2.0 for code; paper “arXiv.org perpetual non-exclusive license”

**Abstract (paste):** use abstract environment from `A001-arxiv.tex` (deficiency \((\infty,\infty)\) for \(H_1\); seed restated; no gates).

**Comments line (suggested):**  
12 pages. Seed map due to Alpöge (credits Fable); restated only. Companion code v0.3.3; concept DOI 10.5281/zenodo.21474351. No gates/channels/advantage.

**MSC:** 47B25, 81S05, 14R15, 37C10, 53D17

---

## 3. How to get an endorsement link (Dan steps)

arXiv does **not** give a public “endorsement URL” up front. Flow:

1. Create/login https://arxiv.org  
2. **Start new submission** → category `math.FA` (add `math-ph`, `math.SP`).  
3. Upload **source**: prefer `.tex` (+ bbl if any) or single PDF if policy allows for your account type; this paper is self-contained `.tex`.  
4. If arXiv blocks with **“endorsement required”**, the submit UI shows:
   - an **endorsement code** (e.g. `XYZ12`), and  
   - instructions to have an endorser visit the endorser form  
5. Endorser goes to: https://arxiv.org/auth/endorse  
   (or the link shown in your submit UI) and enters **your endorsement code** + their credentials.  
6. After endorsement clears, **resume the same submission** and submit.

**You cannot finish step 5 without step 2–4.** This packet prepares everything *before* you click Start.

### Who can endorse
Someone with prior arXiv submissions in related categories (FA, MP, SP, OA) who knows the area. Send them:
- `A001-endorsement-request.md` (email body)  
- PDF link or attachment  
- Your **endorsement code** once the submit UI issues it  

### If you already have endorsement privileges
Skip endorsement; submit directly with this packet’s metadata.

---

## 4. Source bundle checklist (before Upload)

- [ ] `pdflatex` twice on `A001-arxiv.tex` → clean PDF  
- [ ] Title/author/abstract match tex  
- [ ] Errata lines present (withdrawn pairs / Dom indicators)  
- [ ] Non-claims section present  
- [ ] No `\input` of missing files  
- [ ] Figures: none required  
- [ ] Ancillary: optional link to GitHub in Comments (not required as zip)

**Build command (Windows):**
```powershell
cd C:\Users\Dan\Desktop\Projects\Quantyra-Jacobian-Weyl-QC\docs\notes
pdflatex -interaction=nonstopmode A001-arxiv.tex
pdflatex -interaction=nonstopmode A001-arxiv.tex
```

---

## 5. Post-accept actions

1. Record arXiv id `arXiv:YYYY.NNNNN` in README + CITATION.cff + planning checkpoint.  
2. Zenodo related identifier → eprint.  
3. Do **not** change theorem text without re-running publication-adversarial gate.

---

## 6. Submission status ledger

| Step | Status |
|------|--------|
| Packet assembled | **done** |
| External LLM brief | **done** (Dan runs ChatGPT/Claude/Grok) |
| Endorsement code issued | **pending Dan start submit** |
| Endorsement granted | pending |
| arXiv live | pending |

# A001 external LLM review brief (ChatGPT Pro / Claude / Grok)

**Purpose:** Paste this brief + attach `A001-arxiv.pdf` (and optionally this repo’s `docs/validation/` dossiers) into ChatGPT Pro, Claude, and Grok for independent critique before arXiv upload.  
**Author:** Daniel Eric Fredriksen (Quantyra Inc.)  
**Date:** 2026-07-21  
**Version pin:** GitHub `v0.3.3` · concept DOI `10.5281/zenodo.21474351` · PDF `docs/notes/A001-arxiv.pdf`

---

## 1. What to give the model

1. This brief (full text).  
2. PDF: `docs/notes/A001-arxiv.pdf` (or source `A001-arxiv.tex`).  
3. Optional depth: `docs/validation/G4-strong-CCR-extensions-A001.md`, `G4-H0-H2-deficiency-bounds.md`, `H4-TRUNK-CLOSEOUT.md`.  
4. Ask for the **response template in §5** only (no rewrite of the whole paper unless REVISE).

---

## 2. One-paragraph claim (authoritative)

We restate the Alpöge–Fable Keller map \(F\) (not our discovery). The cotangent Poisson lift and Weyl endomorphism \(\psi\) are algebraically clean. Dual fields \(X_j\) are incomplete; \(H_j=-iX_j\) fail essential self-adjointness. For \(H_1\), deficiency indices are \((\infty,\infty)\); wall/omission models give \(H_0=(\infty,0)\) and \(H_2=(0,\infty)\). Global dual \(F\)-translation unitary packages on open \(F\)-support are obstructed (dual-flow strong CCR no-go). No gates, channels, advantage, or “all quantization fails.”

---

## 3. Hard non-claims (reject any review that invents these)

- Seed discovery of \(F\)  
- Unitary gate / channel / CP map constructed / computational advantage  
- Preferred self-adjoint extension  
- Pair \((0,\infty)\) for \(H_1\) (withdrawn erratum)  
- Interior \(s\)-indicator Dom(\(H^*\)) proof (withdrawn)  
- P vs NP or complexity claims  
- Lean proves G4 analysis (Lean = seed + adjugate/collision algebra only)

---

## 4. Attack surfaces (please try to break)

1. **Dom(\(H^*\))** membership of wall deficiency vectors (transverse cutoffs only).  
2. **Orbit measure** / flow-box Jacobian factor \(1/2\).  
3. **Index pairs** for \(H_0,H_2\) vs \(H_1\) — one-sided vs two-sided.  
4. **Global dual-flow no-go** — does non-surjectivity of \(F\) really kill all three unitary groups?  
5. **Discussion** overclaim vs theorem statements A–F.  
6. **Attribution** and bibliography adequacy.  
7. **Errata** visibility for prior wrong pairs.

---

## 5. Required response template

```text
VERDICT: PASS | REVISE | NO-GO

BLOCKING ISSUES:
- (numbered; empty if PASS)

PROOF GAPS:
- ...

OVERCLAIMS / NON-CLAIMS VIOLATIONS:
- ...

PRESENTATION / ARXIV FIT (math.FA or math-ph):
- primary category suggestion:
- secondary:
- abstract clarity 1-5:
- length/structure 1-5:

MINIMAL FIX LIST (if REVISE):
1.
2.

ONE-PARAGRAPH SUMMARY FOR AUTHOR:
...
```

---

## 6. How Dan should use outputs

| Source | Role |
|--------|------|
| ChatGPT Pro / Claude / Grok | **Advisory** external critique |
| Quantyra three-role Task gate | **Mandatory** before claim-freezing public freeze |
| Dan | Final arXiv click + endorsement |

Merge LLM issues into `docs/notes/A001-external-llm-review-log.md` (create when pasting results). Do not treat chat PASS as publication gate alone.

---

## 7. Suggested single prompt (copy-paste)

> You are a hostile referee in functional analysis / mathematical physics. Review the attached paper using the brief’s non-claims and attack surfaces. Return ONLY the response template. Do not invent gates, channels, or complexity claims. Flag any step where Dom(H*) or deficiency indices are handwaved.

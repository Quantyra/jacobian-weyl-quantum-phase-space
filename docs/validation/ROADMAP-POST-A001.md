# Roadmap post-A001 — follow the charters

**Date:** 2026-07-21  
**Spine status:** Dual-flow A001 **closed (no-go)** · wind-down publish **in flight**  
**Binding non-claims:** no gates/channels/advantage; no dual-\(F\) repair; no “all quantization fails”

Charters:
- Wind-down: `PROGRAM-WINDDOWN-A001.md`
- **B** classification: `PROGRAM-B-CLASSIFICATION-CHARTER.md`
- **C** constructive: `PROGRAM-C-CONSTRUCTIVE-CHARTER.md`
- Dual-\(F\) catalog only: `DUAL-F-RESTATEMENT-CATALOG.md`

Planning: S029 (B), S030 (C), S031 (arXiv wind-down)

---

## Lane overview

```text
                    ┌─────────────────────────┐
                    │  A001 dual-flow spine     │
                    │  G0–G7 CLOSED (no-go)     │
                    └───────────┬─────────────┘
                                │
          ┌─────────────────────┼─────────────────────┐
          ▼                     ▼                     ▼
   ┌──────────────┐    ┌──────────────┐    ┌──────────────────┐
   │ Lane W       │    │ Lane B       │    │ Lane C           │
   │ Wind-down    │    │ Classification│    │ Constructive     │
   │ PUBLISH      │    │ structure    │    │ non-dual-F (C1)  │
   └──────────────┘    └──────────────┘    └──────────────────┘
          │                     │                     │
          │                     └──────────┬──────────┘
          │                                ▼
          │                     ┌──────────────────┐
          │                     │ Lane R (optional) │
          │                     │ Dual-F restatement│
          │                     │ catalog only      │
          │                     └──────────────────┘
          ▼
   arXiv live → cite freeze
```

Work **W ∥ B ∥ C** in parallel. Lane R is packaging for referees, not a research bet.

---

## Lane W — Wind-down & publish (priority until eprint)

| Phase | ID | Deliverable | Exit |
|-------|-----|-------------|------|
| **W0** | now | Packet + LLM brief + PDF | **done** |
| **W1** | Dan | 3× external LLM reviews (ChatGPT Pro / Claude / Grok) | log in `A001-external-llm-review-log.md` |
| **W2** | Dan | Merge REVISE fixes; rebuild PDF | clean pdflatex |
| **W3** | Dan | Start arXiv submit → endorsement code → endorse → submit | `math.FA` + `math-ph`,`math.SP` |
| **W4** | agent | Post-eprint: README, CITATION.cff, Zenodo related ID, checkpoint | arXiv id recorded |
| **W5** | optional | Journal target shortlist (FA / MP letters) | one-pager only |

**Do not** open new dual-flow theorem work inside W.

---

## Lane B — Classification (charter Program B)

### Horizon
| Window | Focus |
|--------|--------|
| **Days 0–30** | B0–B3 charter deliverables |
| **Days 30–90** | ≥5 atlas rows; one standalone lemma note |
| **Days 90–180** | Dichotomy paper draft (if lemmas hold) or honest stop |

### Phases

| Phase | ID | Work | Exit criterion |
|-------|-----|------|----------------|
| **B0** | taxonomy | Axes: surjective / regularity / dual fields / target package | `PROGRAM-B-B0-taxonomy.md` expanded |
| **B1** | structural lemma | Non-surjective + complete dual fields ⇒ contradiction (cite RS/geometry; standalone) | `PROGRAM-B-B1-structural-lemma.md` |
| **B2** | atlas schema | Columns `b_ess,b_def,b_ccr,b_cp` ∈ {open,fail,pass} + evidence | `data/atlas` schema bump + A001/A002 filled |
| **B3** | non-A001 example | Toy or second map **or** documented blocker | one dossier |
| **B4** | deficiency patterns | When do we get \((\infty,\infty)\) vs one-sided? (taxonomy, not full proofs) | pattern table |
| **B5** | CCR boundary | B-CCR fail conditions = dual-\(F\) catalog pointers | link R4–R11 |
| **B6** | freeze | Adversarial gate if public classification claims | packet PASS |

**Hand-off to C:** any `b_cp=open` row with algebraic \(\psi\) becomes a C1 candidate.

---

## Lane C — Constructive (charter Program C, bet **C1**)

### Horizon
| Window | Focus |
|--------|--------|
| **Days 0–30** | Domain of \(\psi\); positivity probes; non-claims freeze |
| **Days 30–90** | Stinespring sketch **or** CP obstruction lemma |
| **Days 90–180** | Only if C1 green: limited public note (no advantage language) |

### Phases

| Phase | ID | Work | Exit criterion |
|-------|-----|------|----------------|
| **C0** | freeze scope | Written: no dual-\(F\); no gate/advantage | in C1 starter |
| **C1a** | algebra domain | Polynomial Weyl \(*\)-algebra; \(\psi\) as \(*\)-endo or not | definition note |
| **C1b** | positivity | Matrix levels / quadratic modules; CAS where possible | pass/fail log |
| **C1c** | branch | **Construct:** Stinespring data sketch · **or** **No-go:** axiomized obstruction | one of two docs |
| **C1d** | correspondence | Optional Hilbert-module picture if C1c construct | sketch only |
| **C2** | defer | Unlabeled nonregular — only if C1 blocked and B asks | separate mini-charter |
| **C3** | defer | Positive ESS seed — only if B predicts pass case | blocked until B4 |
| **Cg** | gate | 3-role adversarial before “we built CP” public freeze | packet |

**Kill criteria:** 30 days with no positivity traction and no clean obstruction → pause C; keep B.

---

## Lane R — Dual-\(F\) restatements (catalog only)

| Phase | Work | Exit |
|-------|------|------|
| **R0** | Catalog R1–R15 | **done** |
| **R1** | Add referee one-liners to paper appendix if LLM/referees want | optional tex edit |
| **R2** | Any “new” dual-\(F\) idea → map to R-id or reject as repair attempt | ongoing hygiene |

**No Lane R research sprints.** If it smells like dual-flow repair, stop.

---

## Cadence (operating rhythm)

| When | Action |
|------|--------|
| **Each work session** | Touch at most **two** of {W, B, C}; commit always |
| **Weekly** | Update `OPEN-TRACKS` / checkpoint: W status, B phase, C phase |
| **Before any public claim** | `publication-adversarial-review-protocol.md` 3-role Task gate |
| **After arXiv id** | Prefer B/C citations to eprint; stop PDF thrash |

---

## 90-day scoreboard (success = charter-faithful)

| Lane | Success | Failure (honest stop) |
|------|---------|------------------------|
| **W** | arXiv live | stuck on endorsement → keep Zenodo+GitHub as publish |
| **B** | B0–B3 done + schema live | only A001 restated → wind B down |
| **C** | C1c construct **or** no-go | vague CP talk → kill C1 |
| **R** | catalog stable | “new dual-F theorems” creep → revert |

---

## Explicit backlog (ordered)

### Now (W)
1. Ingest LLM VERDICTs → fix list  
2. Rebuild PDF if needed  
3. arXiv endorsement + submit  

### Next (B ∥ C after W1 started)
4. **B1** structural lemma note  
5. **B2** atlas schema columns  
6. **C1a–b** \(\psi\) domain + first positivity checks  

### Later
7. B3 non-A001 example  
8. C1c branch resolution  
9. Optional Lean: more algebra only (no fake G4)  
10. Journal shortlist (W5)

### Out of scope until new charter
- Gates, channels, advantage, complexity  
- Dual-\(F\) unitary repair on \(L^2(\mathbb{R}^3)\)  
- Full analytic G4 in Lean (resource sink)

---

## Decision tree (when stuck)

```text
Is the task dual-F translation dynamics on L2?
  YES → cite catalog / G4; do not "fix"
  NO  → Is it "which maps admit ESS/CCR"? → Lane B
        Is it "build CP/correspondence for ψ"? → Lane C
        Is it "get eprint live"? → Lane W
        Else → new charter or drop
```

---

## Repo map

| Lane | Science paths | Planning |
|------|---------------|----------|
| W | `docs/notes/A001-arxiv*` | S031 |
| B | `PROGRAM-B-*`, `data/atlas/` | S029 |
| C | `PROGRAM-C-*`, G3/G6 dossiers | S030 |
| R | `DUAL-F-RESTATEMENT-CATALOG.md` | — |

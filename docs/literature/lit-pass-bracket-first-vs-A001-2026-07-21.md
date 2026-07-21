# Literature pass: bracket-first quantization vs A001 hypotheses (quantum)

**Date:** 2026-07-21  
**Question:** Are there published works whose **quantum** claims are line-falsified by A001 dual-field incompleteness / non-ESS?  
**Method:** arXiv API + local lit pile; claim-check against A001 hypotheses below.  
**Non-claims:** This is not a complete survey. No paper is accused of error without matching hypotheses.

---

## 0. Our falsifying engine (what must match)

A001 obstructs a paper only if the paper effectively asserts something like:

| # | Hypothesis |
|---|------------|
| H1 | Dual/cotangent-style momenta from a polynomial map \(F\) with \(B\sim J^{-T}\), \(H_j=-iX_j\) (or equivalent) |
| H2 | Algebraic CCR/Poisson (brackets close) is treated as selecting **the** quantum momenta |
| H3 | Claims **ESS / unique self-adjoint realization** on \(C_c^\infty\) or “the” Schrödinger momentum without domain/extension analysis |
| H4 | Setting allows **incomplete dual flow** (nonproper / non-surjective Keller-type geometry), or ignores completeness |

**A001 proved (relevant):** all three \(X_j\) incomplete; all three \(H_j\) not ESS; for \(H_1\), \((n_+,n_-)=(\infty,\infty)\).

If a paper only does **algebraic** Weyl/Dixmier endomorphisms, or only **classical** cotangent lifts, A001 does **not** falsify it.

---

## 1. Search hits by cluster

### Cluster A — ESS of first-order / vector-field operators (math.FA / math-ph)

Examples (representative, not exhaustive):

| Ref | Topic | Bracket-first? | Hit by A001? |
|-----|--------|----------------|--------------|
| Chernoff 1973 (JFA) | ESS powers of hyperbolic generators | No — ESS is the subject | **Aligned** with us (completeness matters) |
| arXiv:0005011 Lesch | ESS first-order systems | No | Aligned |
| arXiv:1606.06190 Bandara–Saratchandran | ESS first-order on manifolds | No | Aligned |
| arXiv:2010.09816 Nenciu et al. | ESS first-order / Dirac confinement | No | Aligned |
| Braverman–Milatovic–Shubin (survey lineage) | Schrödinger ESS on manifolds | No | Aligned |

**Verdict:** These papers **do not** claim “brackets ⇒ unique momentum.” They study when ESS holds. A001 is a **concrete polynomial example** in that tradition, not a refutation of them.

### Cluster B — Dixmier conjecture / Weyl algebra endomorphisms (math.RA)

Examples:

| Ref | Topic | Quantum \(L^2\) ESS? | Hit by A001? |
|-----|--------|----------------------|--------------|
| Belov–Kontsevich arXiv:math/0512171 | JC stably equivalent to Dixmier | Algebraic invertibility of endomorphisms | **No** |
| Bavula–Levandovskyy, Valqui–Moskowicz, etc. | Dixmier partial results | Algebraic | **No** |
| Zheglov arXiv:2410.06959 | Dixmier for \(A_1\) (claim) | Algebraic | **No** |

**Verdict:** “Weyl endomorphism” here means **algebra automorphism**, not “Schrödinger operator is ESS.”  
A001’s Poisson/Weyl **polynomial** lift is thematically adjacent (JC ↔ Dixmier motivation) but **does not line-falsify** Dixmier papers: different claim type.

### Cluster C — Cotangent lifts (math.SG)

Examples:

| Ref | Topic | Quantum ESS? | Hit by A001? |
|-----|--------|--------------|--------------|
| arXiv:2006.12477 Mir–Miranda | Rigidity of cotangent lifts | Classical symplectic | **No** |
| arXiv:1410.3697, math/0409148 | Cotangent-lifted actions / slices | Classical | **No** |
| Grabowski–Urbański dg-ga/9710013 | Tangent/cotangent lifts of algebroids | Classical | **No** |

**Verdict:** “Cotangent lift” in the literature is almost always **classical**. No hit under H2–H3.

### Cluster D — Weyl / deformation quantization (math.QA / math-ph)

Examples:

| Ref | Topic | Claims ESS of dual \(H_j\)? | Hit by A001? |
|-----|--------|----------------------------|--------------|
| Honegger–Rieckers–Schlafer arXiv:0805.4536 | Field-theoretic Weyl deformation | C*/Banach deformation of Poisson | **Typically no** |
| Federico–Rottensteiner–Ruzhansky arXiv:2306.04275 | Weyl calculus on graded groups | Pseudodiff calculus | **No** (unless a paper claims ESS for our \(X_j\)) |

**Verdict:** Deformation/Weyl calculus quantizes **symbols/algebras**. Unless a paper asserts unique self-adjoint Schrödinger dual momenta from a Keller dual field, A001 does not falsify it.

### Cluster E — Local Keller / JC counterexample literature (2026)

Ulam extract / family theorems in `docs/literature/`: properness, nonproperness set, degree families.

**Verdict:** Classical/algebraic geometry. **No quantum ESS claims** in the extracts on file. Not hit.

---

## 2. Line-by-line style claim check (template)

For any candidate paper, fill:

| Paper claim (quote) | Needs H1–H4? | A001 status | Outcome |
|---------------------|---------------|-------------|---------|
| “Endomorphism of Weyl algebra preserving \([q,p]\)” | H1 algebraic only | We also have poly CCR | **Survives** |
| “Cotangent lift is Poisson” | Classical | We prove for A001 | **Survives** (we agree) |
| “Therefore \(P=-iX\) is the momentum observable” | H2+H3 | False for A001 \(H_j\) | **Vulnerable only if H1+H4 hold** |
| “ESS on \(C_c^\infty(\mathbb{R}^n)\)” for dual field of nonproper Keller | H1–H4 | Contradicted | **Falsified for that map** |

**No paper in this pass filled the full H1–H4 + explicit uniqueness/ESS claim for A001-type dual fields.**

---

## 3. Bottom line

| Question | Answer |
|----------|--------|
| Did we find literature **proven false** by A001? | **No named paper** |
| Did we find literature that **uses** bracket-first? | **Yes** (widespread; Dixmier/Weyl algebra, deformation quantization, physics practice) |
| Did we find literature that **already knows** domains matter? | **Yes** (ESS / Chernoff / first-order systems cluster) |
| What does A001 uniquely add? | Explicit **Keller dual-field** example where brackets work and **all three** \(H_j\) fail ESS; \(H_1\) indices \((\infty,\infty)\) |

**Honest scientific posture:** A001 is a **counterexample to naive bracket→unique quantum momentum** in a precise geometric setting, and a **concrete case study** for the ESS-of-vector-fields literature — not a demolition of Dixmier or deformation quantization as theories.

---

## 4. If we want a true “kill list” later

Search/filter only papers that simultaneously:

1. Quantize **polynomial maps** \(\mathbb{R}^n\to\mathbb{R}^n\) via \(B=J^{-T}\) / dual fields, **and**  
2. State ESS or unique physical momenta on \(L^2\), **and**  
3. Allow nonproper / incomplete geometry (or claim generality covering A001).

Until such a paper is found, do **not** market A001 as “refuting paper X.”

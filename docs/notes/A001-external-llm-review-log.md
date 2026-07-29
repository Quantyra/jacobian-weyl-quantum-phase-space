# A001 external LLM review log

**Date:** 2026-07-21  
**Inputs:** Grok, Claude, ChatGPT Pro (hostile referee template)  
**Response:** REVISE → manuscript `v0.3.4-submit` (H₁-only, expanded)

## Aggregate verdict
| Model | Verdict | Primary pressure |
|-------|---------|------------------|
| Grok | REVISE | Self-contained walls, volume factor, Dom(H*), asymptotics, CAS pointers |
| Claude | (algebra OK; JC attribution flag) | Verify cubic/escape; stable citation for seed |
| ChatGPT | REVISE | Version coherence; strip H0/H2 + broad no-go from Discussion; expand PDF |

## Fixes applied in v0.3.4-submit
1. **H₁-only scope** — removed theorem-level H0/H2 pairs and dual-flow strong CCR no-go from body/Discussion.  
2. **Expanded analytic core** — explicit curve; volume factor from \(|\det DF|\); wall IFT + smooth \(G_\pm\) at \(\tau=0\); escape \(\|q\|\ge C/\sqrt{\cdot}\); saturation lemma; full Dom(H*) Fubini/IBP + lateral \(\chi=0\); injectivity for \(n_\pm=\infty\).  
3. **Weyl endomorphism** — Theorem C(3) defines \(\psi\) on generators + universal property.  
4. **CAS pointers** — JSON paths in wall proofs.  
5. **Bibliography** — RS2, Dixmier, Lee, Bass–Connell–Wright, seed provenance + software/Lean.  
6. **Version pin** — software line `v0.3.4-submit` (not silent claim inflation on v0.3.3).  
7. **Errata front matter** — states what this note does *not* claim.

## Deferred / companion only
- Exact global pairs for \(H_0,H_2\) (need global orbit classification).  
- Dual-flow / H4 no-gos as paper theorems.  
- Full JC priority discussion beyond Remark under Theorem A.

## Round 2 (v0.3.4 → v0.3.5-submit)
| Model | Verdict |
|-------|---------|
| Grok | PASS |
| ChatGPT | REVISE (backward wall, Weyl norm, provenance, package sync) |
| Claude | REVISE minor (Dom ℓ=-∞ decay; Weyl direct commutators; cites) |

### Round-2 fixes
1. Full backward \(G_-\) + escape/denominator bounds (not “analogously”).  
2. Dom(H*): escape upper; finite lower escape; \(\ell=-\infty\) exponential decay.  
3. Weyl: abstract \([q,p]=\delta\) vs Schrödinger \(p=-i\partial\); direct \([\psi(q),\psi(p)]\) proof.  
4. Saturation: maximal-flow domain pullback + \(F\circ\Psi=\mathrm{id}\).  
5. Softened novelty; stable seed cites (Alpöge X, Ulam PDF, Speyer).  
6. Synced packet/endorsement/README/brief to v0.3.5-submit H₁-only.

## Round 3 historical prior (v0.3.5 → v0.3.6-submit)
| Source | Verdict |
|--------|---------|
| ChatGPT A | PASS (math) |
| ChatGPT B | REVISE package only (CITATION/Zenodo/page count) |
| Claude | REVISE minor (ε₀ window, dominating fn, biblio) |
| Grok | (prior PASS trajectory) |

### Round-3 fixes
1. Saturation: ε₀ < τ₀²; maximal upper time = β.  
2. Dom: explicit L¹ dominant for Fubini/IBP.  
3. Historical package state: CITATION.cff, packet, endorsement, README →
   v0.3.6-submit.
4. DOI: concept only; no stale version-DOI claim.  
5. Lean biblio pin `v0.1.1-collision`; hidelinks; categories math.SP primary suggested.  
6. Framing: seed *verified*; contribution = D–F dual-lift deficiency.

## Round 4 scientific review (v0.3.8 → v0.3.9-referee-revision)

**Date:** 2026-07-29
**Inputs:** Claude, Codex, Grok
**Aggregate:** REVISE. The earlier technical PASS is superseded.

Blocking consensus:

1. Expand the weak-adjoint argument to cover both weak pairings and the
   fiberwise improper-limit passage.
2. Use the formalized sign involution, rather than the paper-only backward
   wall, as the main \(+i\) route.
3. Strengthen sheet-boundary and cutoff-injectivity arguments.
4. Add accurate Dixmier/Jacobian directionality and current nonproperness
   literature.
5. Synchronize one final Lean freeze and repair release/encoding surfaces.

The first four items and the paper/package side of item 5 are implemented in
`v0.3.9-referee-revision`. At that round, a new single-SHA Lean freeze and
clean build/axiom provenance remained open; Round 6 below records their later
completion. Fresh math.FA/math.AG/non-claims/package gates, final PDF
inspection, and Dan approval remained open.

## Next

Do not submit. Complete the fresh gate recorded in
`A001-arxiv-checklist.md`.

## Round 5 math.FA re-gate response

**Date:** 2026-07-29

**Input:** proof-adversarial re-gate of science commit `73a90f8`

**Decision:** REVISE; the math.FA PASS remains pending.

The re-gate identified two exposition defects in the revised weak-adjoint
argument:

1. The finite-boundary trichotomy did not cover sequences for which the
   limiting time lies below the limiting orbit's lower endpoint, and no
   endpoint semicontinuity had been proved.
2. The prose denied a measurable transverse exhaustion but then invoked
   dominated convergence through the transverse integral.

The paper now avoids both claims. It uses no continuity or semicontinuity of
the variable lower endpoint and makes no global finite-boundary assertion.
Instead, after establishing absolute integrability, it proves the improper
one-dimensional integration-by-parts identity on each fixed fiber, including
the escape/decay endpoint alternatives, and only then integrates the already
proved equality in the transverse variables by Fubini. Thus no transverse
limit, measurable exhaustion, or endpoint-selection argument is used. The
von Neumann corollary also now applies explicitly to the closure
\(\overline H\).

Fresh math.FA review is still required; this response does not mark the gate
PASS.

## Round 6 synchronized Lean freeze

**Date:** 2026-07-29

The science package is repinned to the synchronized, untagged, unreleased Lean
freeze `b8bc72ea87531b88d50ed588ec6268ae743a662f`. Its publication provenance
records strict cache retrieval, targeted and full builds, an executable
headline-theorem axiom audit, and a forbidden-marker scan. The earlier
`ff50f4a2a312591c2e5b26e71eb390ade9164b34` is retained only as the historical
Theorem F source root.

The freeze adds `theoremFUnitPhaseExtension` and
`theoremFUnitPhaseExtension_injective`, which prove that unitary complex phases
inject into distinct `SelfAdjointExtension H_X1_min` witnesses. The paper and
package therefore state a continuum-sized lower family of distinct witnesses,
while continuing not to claim the exact cardinality of the full extension
type. No tag, release, DOI minting, arXiv submission, or Dan approval is
recorded.

## Round 7 package status synchronization

**Date:** 2026-07-29

Math.FA, math.AG, Lean/build, and non-claims gates are now recorded PASS.
Package/metadata recheck and Dan approval remain pending. Current checklist,
README, endorsement, submission, and metadata surfaces use that same status.
No tag, release, DOI minting, arXiv submission, or Dan approval is recorded.

## Round 8 package/metadata exact re-gate

**Date:** 2026-07-29

Package/metadata exact re-gate PASS was recorded against science commit
`02bbbfaf037238eb61f751e98ad806e8d5e7c7a3` and Lean freeze
`b8bc72ea87531b88d50ed588ec6268ae743a662f`. All five technical gates now
PASS; only Dan approval remains pending. This is a status-only update: the
canonical TeX theorem content, rendered PDF, and Lean SHA are unchanged. No
tag, release, DOI minting, arXiv submission, or Dan approval is recorded.

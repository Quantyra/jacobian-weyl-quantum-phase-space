# A001 external LLM review log

> **HISTORICAL ADVISORY LOG (2026-08-01) — NOT THE AUTHORITATIVE PUBLICATION GATE.**
> External-LLM reviews recorded below are advisory chronology only. They do
> **not** replace the mandatory independent publication gates or live release
> status. Final authoritative surfaces:
>
> - Closeout / released status: [`../validation/A001-PROGRAM-CLOSEOUT-FINAL.md`](../validation/A001-PROGRAM-CLOSEOUT-FINAL.md)
> - Gate log: [`A001-arxiv-checklist.md`](A001-arxiv-checklist.md)
> - Submission packet: [`A001-arxiv-submission-packet.md`](A001-arxiv-submission-packet.md)
>
> Within the chronology, older round labels such as "current superseding status"
> are **historical within this log only**. They do not override the final
> closeout. A001 is released (GitHub + Zenodo); arXiv remains human-endorsement
> only (`VIPN6B`).

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

## Round 9 claim-boundary correction (historical superseding status within this log)

**Date:** 2026-07-29

External adversarial review subsequently identified claim-boundary,
provenance, and metadata defects in the Round 8 candidate. The Round 6--8
pins and PASS records above are retained as dated historical evidence; they
are not the current publication status.

The corrected synchronized Lean freeze is
`0735757f7f1a3a2875fcd29e31e03a203c3c8a74`. It renames the algebraic
`Module.rank` API to `hamelDeficiencyRank`, with
`aleph0_le_hamelDeficiencyRank_X1`, and records focused 8,684/8,692-job
builds, the full 8,702-job build, and the seven-declaration axiom audit. The
science package separates the Lean-proved unit-phase injection from the
classical cardinality of the complex unit circle used for the continuum
lower-family corollary.

The corrected PDF SHA-256 is
`f9e3b9bfe81d15047fc406910038028bc65d403c88636594a7bb4d52a4e4e785`.
Fresh math.FA, math.AG/Weyl, non-claims, and package/metadata re-gates remain
pending before Dan approval. No tag, release, DOI minting, arXiv submission,
or Dan approval is recorded.

## Round 10 final Lean documentation sync (historical superseding status within this log)

**Date:** 2026-07-29

The synchronized Lean freeze is now
`b51b67d03515d44e1cb1309cf8721a7ecf7803b2`. It contains all Round 9
declaration/API repairs plus the final Theorem C coverage-comment and
historical-backlog supersession repair. `PUBLICATION_PROVENANCE.md` records
focused `TheoremFPlusITransport` (8,684 jobs), focused
`TheoremFExtensionMultiplicity` (8,692 jobs), the full 8,702-job build, and
the seven-declaration axiom audit. Later focused `TheoremC` and
`TheoremCWeyl` checks are separate implementation checks.
The Round 9 Lean pin and PDF hash above are retained only as dated historical
evidence and are superseded by this Round 10 package.
The Round 10 PDF SHA-256 is
`9cd419312ae139aed3ae517a01d72ec029d5c161fc72747239575f49381a5020`.

Lean/build and math.FA/math.AG/Weyl gates are COMPLETE/PASS. Fresh non-claims
and package/metadata re-gates remain pending before Dan approval. No tag,
release, DOI minting, arXiv submission, or Dan approval is recorded.

## Round 11 expanded axiom-audit synchronization (historical superseding status within this log)

**Date:** 2026-07-29

The synchronized Lean freeze is now
`fbcdd0345d2f2540cd537204be2178ae07e18a5e`. The theorem claims and build
counts are unchanged from Round 10. `PUBLICATION_PROVENANCE.md` records
focused `TheoremFPlusITransport` (8,684 jobs), focused
`TheoremFExtensionMultiplicity` (8,692 jobs), the full 8,702-job build, and
the expanded nine-declaration strict axiom audit. Every audited declaration
has exactly `[propext, Classical.choice, Quot.sound]`.

The Round 10 Lean pin and PDF hash above remain dated historical evidence and
are superseded by this Round 11 package. The Round 11 PDF SHA-256 is
`2359efa571711abb93fc6566ce1c518705ec1002c6d902de6b7bf23ae87a0343`.

Lean/build and math.FA/math.AG/Weyl gates remain COMPLETE/PASS. Fresh
non-claims and package/metadata re-gates remain pending before Dan approval.
No tag, release, DOI minting, arXiv submission, or Dan approval is recorded.

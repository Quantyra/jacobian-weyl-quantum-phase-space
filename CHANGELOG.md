# Changelog

## v0.3.9-referee-revision — 2026-07-29 (proposed, untagged)

- Repinned the full science package to synchronized, untagged Lean freeze
  `b8bc72ea87531b88d50ed588ec6268ae743a662f`, whose strict cache retrieval,
  full build, and executable publication axiom audit pass.
- Added the Lean-proved injective unit-phase family of distinct
  `SelfAdjointExtension H_X1_min` witnesses. This exhibits a
  continuum-sized lower family without claiming the exact cardinality of the
  full extension type.
- Expanded the central weak-adjoint proof to control both weak pairings and
  state the compact-interval integration by parts and escape/decay steps.
- Proved the absolutely convergent improper identity separately on each
  fiber before integrating the established equality by Fubini; no transverse
  dominated-convergence or measurable-exhaustion claim remains.
- Made the Lean-backed sign involution the main \(+i\) route; retained the
  backward wall as independent geometry only.
- Avoided any unsupported continuity claim for the variable lower flow
  endpoint; the direct weak formulation handles the zero extension without
  a global finite-boundary assertion.
- Added the cross-orbit invariant-coordinate argument, compact transverse
  support, and uniform-collar norm lower bound.
- Stated Hilbert deficiency indices exactly as
  \(n_+=n_-=\aleph_0\), with conventional \((\infty,\infty)\) notation.
- Added accurate Dixmier/Jacobian directionality, current related work, AFP
  verification, and Akhil Mathew attribution.
- Clarified the complex seed versus real operator theory and that Theorems
  D–F do not use the collision.
- Repaired README UTF-8 corruption and separated paper-package, Lean
  theorem-source, and Lean synchronized-snapshot version streams.
- Superseded the prior technical PASS: fresh math.FA, math.AG, Lean/build,
  non-claims, package, and Dan approval gates are pending.
- No tag, release, arXiv submission, or DOI minting performed.

## v0.3.8-theorem-f — 2026-07-28 (candidate update)

### Lean supplement
- Updated the untagged publication candidate to verified Lean SHA `ff50f4a2a312591c2e5b26e71eb390ade9164b34`.
- Added the exact Hilbert-space result `hilbertDeficiencyIndex_X1_eq_aleph0` for the closed adjoint eigenspaces.
- Preserved the distinction that `standardDeficiencyIndex`/`Module.rank` is algebraic (Hamel) rank, with the verified lower bounds `Cardinal.aleph0 ≤ n_+` and `Cardinal.aleph0 ≤ n_-` only; no exact Hamel-rank equality is claimed.
- Added the specific `H_X1_min` bijective von Neumann classification of all `SelfAdjointExtension H_X1_min` witnesses and the at-least-two-distinct-extensions corollary.
- At that historical candidate, the Lean corollary did not yet include the
  paper's infinitely-many/continuum consequence; the synchronized v0.3.9
  freeze supersedes that limitation with the injective unit-phase family.
  Exact cardinality of the full extension type, preferred extension,
  arbitrary-operator theorem, algebraic selection, and the paper-grade
  backward-wall construction remained nonclaims.
- No tag, release, version DOI, or final approval created.

## v0.3.3 — 2026-07-21

### Theorem F (publication freeze candidate)
- Analytic wall IFT with correct forward scaling \((-A_s)r^3+Br=0\)
- Explicit algebraic branch reconstruction (8.0)
- Saturated maximal-sheet lemma (ODE flow domain)
- Dom(H*) integration-by-parts with compact-support endpoint control
- PDF/TeX expanded; metadata version **0.3.3**
- Numeric wall scripts labeled regression only

## v0.3.1 — 2026-07-21

### Critical proof repair (Theorem F)
- **Withdrawn:** v0.3.0 deficiency vectors with interior \(s\)-indicators (not in \(\operatorname{Dom}(H^*)\))
- **Corrected:** whole maximal-orbit deficiency vectors; transverse cutoffs only
- Saturated inverse-sheet lemma; per-orbit dictionary; rescaled IFT for wall branches
- PDF/TeX/draft/dossier synced; claim remains \((n_+,n_-)=(\infty,\infty)\)

## v0.3.0 — 2026-07-21

### Erratum (critical)
- **Withdrawn:** v0.2.2 claim \((n_+,n_-)=(0,\infty)\) for \(H=-iX_1\)
- **Corrected:** \((n_+,n_-)=(\infty,\infty)\) via open forward- and backward-incomplete families
- Self-adjoint extensions exist in abundance (von Neumann); none preferred by algebraic data
- See `docs/notes/A001-ERRATUM-v0.2.2.md`

### Paper / attribution
- Title and abstract attribute seed map to **Alpöge–Fable**; novelty is B–F
- Theorem E is corollary of explicit deficiency functions (no general Stone/transport necessity)
- Theorem C rewritten with Piola + dual-coframe commutation; Schrödinger convention clarified
- arXiv draft + checklist + submission bundle updated for v0.3.0

### CAS
- `verify_backward_incomplete_wall_A001.py` + JSON anchor

## v0.2.2 — 2026-07-21

### Science
- Orbit-measure analysis: \(\mathrm{Leb}_3(\{T_+^{X_1}<\infty\})>0\)
- Exact deficiency indices \((n_+,n_-)=(0,\infty)\) for \(P_1^{\mathrm{sym}}\) (half-line orientation + direct integral)
- arXiv draft upgraded with Theorem F; submission bundle + checklist freeze
- CAS: incomplete sheet \(\Sigma_0\), IFT escape locus certificates

### Non-claims
Unchanged: no gate/channel/advantage; no unique physical momenta without extensions.

## v0.2.1 — 2026-07-21

### Metadata
- Author name standardized to **Daniel Eric Fredriksen** (Quantyra Inc) in Zenodo/CITATION
- Concept DOI recorded: `10.5281/zenodo.21474351` (version DOI updates with this release)

## v0.2.0 — 2026-07-21

### A001 minimum result package
- G0 seed dual-CAS + Lean companion link; D0 dossiers
- G0-family d=4 Cor 5.3 pilot (constructive)
- G1 atlas bootstrap (A001, A002)
- G2 Poisson cotangent lift Î¦ certified (A001)
- G3 polynomial Weyl endomorphism Ïˆ certified (A001); div B = 0
- G4: dual-field incompleteness theorem; ESS obstruction (existential)
- Internal note: `docs/notes/A001-minimum-result-note.md`
- G5–G7 structured packages (index/channel still open / not claimed)

### Non-claims
Algebraic + ESS-on-C_c^∞ obstruction only. No gate/channel/advantage; no unique physical momenta without extensions.

## v0.0.1 — 2026-07-20
- Initial public scaffold, INTEGRITY, Zenodo metadata path

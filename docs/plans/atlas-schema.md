# Counterexample Atlas schema (G1 bootstrap)

**Program:** EXOTIC-CCR  
**Gate:** G1 bootstrap (S016)  
**Machine schema:** [`data/atlas/schema.json`](../../data/atlas/schema.json)  
**Index:** [`data/atlas/index.json`](../../data/atlas/index.json)

## Purpose
A degree-indexed registry of Keller maps used by the program, with **explicit evidence levels**. Rows link to frozen anchors and CAS/Lean certificates. Poisson/Weyl fields are **placeholders** until G2/G3.

## Row id convention
`A###-short-slug` — zero-padded sequence, stable once published.

## Required fields (summary)
| Field | Meaning |
|-------|---------|
| `mu_generic_degree` | Generic degree \(d=\mu(F)\) |
| `mu_evidence` | How \(d\) is justified (fiber poly / certified / preprint_only / …) |
| `map` | Name, variables, display formulas, construction, optional `anchor_ref` |
| `jacobian` | Constant det + status |
| `collision` | Seed triple retention, target, inputs, status |
| `evidence_level` | Ladder A–G (atlas bootstrap stays at A_*) |
| `certificates` | Dossiers, CAS paths, Lean refs, literature |
| `placeholders` | `poisson_lift_Phi`, `weyl_formula`, `star_domain_status` |
| `non_claims` | Binding negatives for the row |
| `status` | active / draft / superseded |

## Geometry placeholders (optional object)
`discriminant_nonproper_set`, `omitted_set`, `monodromy_galois`, `primitive_decomposition`, `real_locus` — fill in later G1/G2 geometry work; not required for bootstrap.

## Composition / iteration (plan only)
- For dominant generically finite maps, \(\mu(F\circ G)=\mu(F)\mu(G)\) (preprint / standard).
- Cotangent lifts (when defined) satisfy \(\Phi_{F\circ G}=\Phi_F\circ\Phi_G\) (G2).
- Atlas may later add rows that are **composites** or **iterates** with `construction` describing factors; **do not** bulk-generate \(d=5..D\) without per-row CAS.
- Bootstrap does **not** add composite rows.

## Current rows (bootstrap only)
| atlas_id | μ | Role |
|----------|---|------|
| `A001-seed-d3` | 3 | Seed announced map (G0-seed certified) |
| `A002-family-d4-pilot` | 4 | Cor 5.3 pilot (G0-family pilot certified) |

## Evidence level policy
- **A_algebra_certified** — dual CAS + (where applicable) Lean for the stated algebraic facts.
- **A_algebra_pilot** — dual CAS pilot; not full ∀-quantifier family re-proof.
- **A_algebra_preprint_only** — cited but not Quantyra-certified (not used in bootstrap active rows).

## Non-claims (atlas-wide)
- No “factory false” slogan as a Quantyra theorem.
- No physical / channel / gate / advantage language.
- No claim that placeholders are proved.
- Zenodo DOIs are independent of atlas bootstrap.

## Adding a new row (checklist)
1. Freeze or reference anchor under `data/anchor/`.
2. Run dual CAS (or stronger) for det + any collision claim.
3. Fill `data/atlas/entries/<atlas_id>.json` conforming to schema.
4. Register in `data/atlas/index.json`.
5. Do not mark `mu_evidence=certified` without degree evidence beyond fiber formula when required.
6. Update planning story/checkpoint if material.

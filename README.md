# Jacobian Conjecture / Weyl / Quantum Phase-Space

Research scaffold for investigating Jacobian Conjecture counterexamples, Weyl-algebra endomorphisms, and phase-space / reversible quantum symmetry criteria.

**Organization:** Quantyra Inc.  
**Planning epic:** `C:\Users\Dan\Desktop\Projects\IGH\Quantyra-Planning2\epics\E005-jacobian-weyl-quantum-phase-space.md`  
**Charter (provisional):** `Quantyra-Planning2/docs/research-program-jacobian-weyl-qc-charter.md`  
**Version:** 0.0.1

## Scientific question (bounded)

Does a Jacobian-counterexample endomorphism of a Weyl algebra yield a reversible quantum symmetry of the corresponding phase-space / CCR algebra, or does it produce only a non-invertible / non-unitary / non-symplectic exotic map?

## Non-claims

This repository is infrastructure and research scaffolding only.

- It does **not** assert that any particular Jacobian Conjecture counterexample is correct; literature intake pins the object of study.
- It does **not** claim new quantum algorithms, complexity separations, or hardware results.
- It does **not** claim that exotic Weyl endomorphisms are physical quantum gates without explicit criteria and proof.
- It does **not** claim P-vs-NP or circuit lower bounds.

See [INTEGRITY.md](INTEGRITY.md) for the standing non-claims boundary.

## Gate status (2026-07-21) — A001 spine through G7

| Gate | Status |
|------|--------|
| G0-seed | [D0-seed](docs/validation/D0-seed-validation-dossier.md) · Lean [v0.1.1](https://github.com/Quantyra/exotic-ccr-lean) |
| G0-family d=4 | [D0-family](docs/validation/D0-family-pilot-dossier.md) |
| G1 atlas | [index](data/atlas/index.json) A001/A002 |
| G2 Poisson A001 | [dossier](docs/validation/G2-poisson-A001-dossier.md) **certified** |
| G3 Weyl A001 | [dossier](docs/validation/G3-weyl-A001-dossier.md) **certified** |
| G4–G7 | [G4](docs/validation/G4-domains-CCR-A001-dossier.md) · [G5](docs/validation/G5-completion-degree-A001-dossier.md) · [G6](docs/validation/G6-CP-dilation-A001-dossier.md) · [G7](docs/validation/G7-semigroup-index-A001-dossier.md) |
| **Closeout** | [PROGRAM-CLOSEOUT-G0-G7-A001.md](docs/validation/PROGRAM-CLOSEOUT-G0-G7-A001.md) |

Physical reversible quantum symmetry is **not** claimed (G4 ESS open; G6 not a channel).

## Repository structure

```
data/anchor/      # frozen maps + CAS reports
data/atlas/       # G1 counterexample atlas (schema, index, entries)
docs/
  validation/
  provenance/
  literature/
  plans/          # includes atlas-schema.md
scripts/cas/
src/
```

## License

Apache-2.0. See [LICENSE](LICENSE).

## Citation

See [CITATION.cff](CITATION.cff). Zenodo DOI pending first GitHub release (Soft Blocker).

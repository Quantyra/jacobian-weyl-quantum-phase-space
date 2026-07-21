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

## Gate status (2026-07-21)

| Gate | Status |
|------|--------|
| G0-seed | [D0-seed dossier](docs/validation/D0-seed-validation-dossier.md) · [anchor](data/anchor/F_announced_det_m2.json) · Lean [v0.1.1](https://github.com/Quantyra/exotic-ccr-lean) |
| G0-family pilot d=4 | [D0-family dossier](docs/validation/D0-family-pilot-dossier.md) · [anchor](data/anchor/F_family_d4_cor53_pilot.json) |
| G1 atlas bootstrap | [schema](data/atlas/schema.json) · [index](data/atlas/index.json) · rows A001, A002 |

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

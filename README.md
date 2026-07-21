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

## Gate 0 seed (D0-seed) — closed 2026-07-21

- Dossier: [docs/validation/D0-seed-validation-dossier.md](docs/validation/D0-seed-validation-dossier.md)
- Frozen anchor: [data/anchor/F_announced_det_m2.json](data/anchor/F_announced_det_m2.json)
- Dual CAS: `python scripts/cas/verify_anchor_sympy.py` and `python scripts/cas/verify_anchor_purepython.py`
- Lean: **[Quantyra/exotic-ccr-lean](https://github.com/Quantyra/exotic-ccr-lean)** release `v0.1.1`
- Full G0 still requires family certification (planning S015)

## Repository structure

```
data/anchor/      # frozen seed map + CAS reports
docs/
  validation/     # D0-seed dossier
  provenance/     # provenance ledger
  literature/
  definitions/
  plans/
  notes/
scripts/cas/      # dual exact CAS verifiers
src/
```

## License

Apache-2.0. See [LICENSE](LICENSE).

## Citation

See [CITATION.cff](CITATION.cff). Zenodo DOI pending first GitHub release (Soft Blocker).

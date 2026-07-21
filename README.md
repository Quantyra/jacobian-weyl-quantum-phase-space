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

## Related Lean artifact (Gate 0)

Formal Gate-0 algebraic certificates live in a separate public repo (not merged here):

- **[Quantyra/exotic-ccr-lean](https://github.com/Quantyra/exotic-ccr-lean)** — Lean 4 T0.1/T0.2 Jacobian anchor (`det DF = -2`, three-point collision, non-injectivity packaging). Release `v0.1.0`.

## Repository structure

```
docs/
  literature/     # S005/S006 literature intake and citation packets
  definitions/    # S007/S008 formal/definitional bridges
  plans/          # S009 research plans
  notes/          # working notes
  zenodo-release-path.md
src/              # future code (optional)
lean/             # optional local notes only; active Lean surface is exotic-ccr-lean
```

## License

Apache-2.0. See [LICENSE](LICENSE).

## Citation

See [CITATION.cff](CITATION.cff). Zenodo DOI pending first GitHub release (Soft Blocker).

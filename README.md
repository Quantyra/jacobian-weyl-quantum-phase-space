# EXOTIC-CCR — Jacobian / Weyl / quantum phase-space

**Author:** Daniel Eric Fredriksen (Quantyra Inc.)  
**Release:** [v0.2.1](https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.2.1)  
**DOI:** [10.5281/zenodo.21474488](https://doi.org/10.5281/zenodo.21474488) (concept [10.5281/zenodo.21474351](https://doi.org/10.5281/zenodo.21474351))

---

## Start here — paper draft

### **[docs/notes/A001-arxiv-draft.md](docs/notes/A001-arxiv-draft.md)**

**arXiv-oriented write-up of the A001 theorems** (Poisson lift, Weyl endomorphism, \(X_1\) incompleteness, \(P_1^{\mathrm{sym}}\) not essentially self-adjoint, deficiency bounds).

Shorter ledger form: **[docs/notes/A001-minimum-result-note.md](docs/notes/A001-minimum-result-note.md)**

---

## One-sentence result

For the seed Keller map \(F\), algebraic Poisson/Weyl CCR lifts exist, but the dual momentum \(P_1^{\mathrm{sym}}=-i X_1\) is **not essentially self-adjoint** on \(C_c^\infty(\mathbb{R}^3)\).

## Non-claims

- **Not** a unitary quantum gate, channel, or computational advantage  
- **Not** unique physical momenta without self-adjoint extension choices  
- **Not** ESS failure claimed for all three dual momenta  
- **Not** a slogan “factory false” theorem beyond the finite identities used  

Full boundary: [INTEGRITY.md](INTEGRITY.md) · paper draft §9

## Companion Lean (Gate-0 seed)

https://github.com/Quantyra/exotic-ccr-lean

## Gate / evidence index

| Gate | Status | Doc |
|------|--------|-----|
| G0 seed | certified | [D0-seed](docs/validation/D0-seed-validation-dossier.md) |
| G0 family d=4 pilot | certified pilot | [D0-family](docs/validation/D0-family-pilot-dossier.md) |
| G1 atlas | A001/A002 | [atlas index](data/atlas/index.json) |
| G2 Poisson | certified | [G2](docs/validation/G2-poisson-A001-dossier.md) |
| G3 Weyl | certified | [G3](docs/validation/G3-weyl-A001-dossier.md) |
| G4 \(X_1\) / \(P_1\) ESS | **proved** | [G4-X1](docs/validation/G4-X1-incompleteness.md) · [deficiency](docs/validation/G4-P1-deficiency-indices.md) · [G4 summary](docs/validation/G4-domains-CCR-A001-dossier.md) |
| G5–G7 | packages | [closeout](docs/validation/PROGRAM-CLOSEOUT-G0-G7-A001.md) |

## Repository layout

```
docs/notes/           # A001-arxiv-draft.md  ← paper draft
                      # A001-minimum-result-note.md
docs/validation/      # theorem dossiers + CAS-linked proofs
data/anchor/          # frozen maps + CAS JSON reports
data/atlas/           # counterexample atlas
scripts/cas/          # reproducible verifiers
```

## Citation

See [CITATION.cff](CITATION.cff). Prefer concept DOI `10.5281/zenodo.21474351` for the project; version DOI `10.5281/zenodo.21474488` for v0.2.1.

## License

Apache-2.0. See [LICENSE](LICENSE).

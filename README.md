# EXOTIC-CCR — Jacobian / Weyl / quantum phase-space

**Author:** Daniel Eric Fredriksen (Quantyra Inc.)  
**Release:** [v0.3.0](https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.3.0)  
**DOI:** [10.5281/zenodo.21477350](https://doi.org/10.5281/zenodo.21477350) (v0.3.0; concept [10.5281/zenodo.21474351](https://doi.org/10.5281/zenodo.21474351); **ignore v0.2.2 pair claim**)

---

## Start here — paper (arXiv submission package)

### **[docs/notes/A001-arxiv-draft.md](docs/notes/A001-arxiv-draft.md)** ← main paper draft

Theorems A–F: Alpöge–Fable seed **restated**; Poisson/Weyl lifts; \(X_1\) incomplete; \(H=-iX_1\) not ESS with **\((n_+,n_-)=(\infty,\infty)\)**.  
**Erratum:** [A001-ERRATUM-v0.2.2.md](docs/notes/A001-ERRATUM-v0.2.2.md) (withdraws \((0,\infty)\)).

| Doc | Role |
|-----|------|
| **[A001-arxiv.pdf](docs/notes/A001-arxiv.pdf)** | **Submit this PDF** |
| [A001-arxiv.tex](docs/notes/A001-arxiv.tex) / [draft.md](docs/notes/A001-arxiv-draft.md) | LaTeX source / long form |
| [A001-endorsement-request.md](docs/notes/A001-endorsement-request.md) | Endorser email blurb |
| [A001-arxiv-checklist.md](docs/notes/A001-arxiv-checklist.md) | Claims freeze |
| [A001-ERRATUM-v0.2.2.md](docs/notes/A001-ERRATUM-v0.2.2.md) | Withdrawn \((0,\infty)\) |

---

## One-sentence result

For the Alpöge–Fable Keller map (restated), algebraic Poisson/Weyl lifts exist, but \(H=-i X_1\) is **not essentially self-adjoint** on \(C_c^\infty(\mathbb{R}^3)\), with deficiency indices \((n_+,n_-)=(\infty,\infty)\) (infinitely many extensions; none preferred).

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
| G4 \(X_1\) / \(H=-iX_1\) | **proved** \((n_+,n_-)=(\infty,\infty)\) | [orbit measure](docs/validation/G4-P1-orbit-measure-deficiency.md) · [erratum](docs/notes/A001-ERRATUM-v0.2.2.md) |
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

See [CITATION.cff](CITATION.cff). Prefer concept DOI `10.5281/zenodo.21474351` and **v0.3.0** (not the withdrawn v0.2.2 pair claim).

## License

Apache-2.0. See [LICENSE](LICENSE).

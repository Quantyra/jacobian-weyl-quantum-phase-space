# EXOTIC-CCR â€” Jacobian / Weyl / quantum phase-space

**Author:** Daniel Eric Fredriksen (Quantyra Inc.)  
**Release (arXiv candidate):** [v0.3.6-submit](https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.3.6-submit)  
**Prior:** [v0.3.5-submit](https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.3.5-submit) · [v0.3.3](https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.3.3)  
**Concept DOI:** [10.5281/zenodo.21474351](https://doi.org/10.5281/zenodo.21474351) (version DOI pending ingest)  
**Do not use:** v0.2.2 pair or v0.3.0 Dom(H*) proof

---

## Start here â€” paper (arXiv submission package)

### **[docs/notes/A001-arxiv-draft.md](docs/notes/A001-arxiv-draft.md)** â† main paper draft

Theorems Aâ€“F: AlpÃ¶geâ€“Fable seed **restated**; Poisson/Weyl lifts; \(X_1\) incomplete; \(H=-iX_1\) not ESS with **\((n_+,n_-)=(\infty,\infty)\)**.  
**Erratum:** [A001-ERRATUM-v0.2.2.md](docs/notes/A001-ERRATUM-v0.2.2.md) (withdraws \((0,\infty)\)).

| Doc | Role |
|-----|------|
| **[A001-arxiv.pdf](docs/notes/A001-arxiv.pdf)** | **Canonical public PDF (v0.3.6-submit; H₁-only arXiv candidate)** |
| [A001-arxiv.tex](docs/notes/A001-arxiv.tex) / [draft.md](docs/notes/A001-arxiv-draft.md) | LaTeX source / long form |
| [A001-endorsement-request.md](docs/notes/A001-endorsement-request.md) | Endorser email blurb |
| [A001-arxiv-checklist.md](docs/notes/A001-arxiv-checklist.md) | Claims freeze |
| [A001-ERRATUM-v0.2.2.md](docs/notes/A001-ERRATUM-v0.2.2.md) | Withdrawn \((0,\infty)\) |

---

## One-sentence result

For the AlpÃ¶geâ€“Fable Keller map (restated), algebraic Poisson/Weyl lifts exist, but \(H=-i X_1\) is **not essentially self-adjoint** on \(C_c^\infty(\mathbb{R}^3)\), with deficiency indices \((n_+,n_-)=(\infty,\infty)\) (infinitely many extensions; none preferred).

## Non-claims

- **Not** a unitary quantum gate, channel, or computational advantage  
- **Not** unique physical momenta without self-adjoint extension choices  
- **Not** ESS failure claimed for all three dual momenta  
- **Not** a slogan â€œfactory falseâ€ theorem beyond the finite identities used  

Full boundary: [INTEGRITY.md](INTEGRITY.md) Â· paper draft Â§9

## Companion Lean (Gate-0 seed)

https://github.com/Quantyra/exotic-ccr-lean

## Companion papers (B001 / C001) — advance while A001 waits on arXiv endorsement

**Index:** [docs/notes/COMPANION-PACK.md](docs/notes/COMPANION-PACK.md)

| Paper | PDF | Tag | One-line |
|-------|-----|-----|----------|
| **B001** classification (v0.7) | [B001-classification-arxiv.pdf](docs/notes/B001-classification-arxiv.pdf) | [v0.2.3-b001-draft](https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.2.3-b001-draft) @ `45e7d53` | B1 + atlas A000–A010; B5–B7; graph/degP≤2 ⇒ global \(C^\infty\) diffeo / E (not automatic poly inverse); residual **OPEN-T**; full dichotomy conjecture; Aggregate PASS |
| **C001** completions of \(\psi\) (v0.9) | [C001-cp-correspondence-arxiv.pdf](docs/notes/C001-cp-correspondence-arxiv.pdf) | [v0.3.3-c001-companion](https://github.com/Quantyra/jacobian-weyl-quantum-phase-space/releases/tag/v0.3.3-c001-companion) @ `45e7d53` | Koopman CONSTRUCT; J2–J6 NO-GOs; J3 **G4-conditional**; J7-C BT-Envelope CONSTRUCT (form-level); J7 CFC-SA NO-GO; J7-O OPEN; Aggregate PASS |

A001 remains citable via **concept DOI** even before arXiv endorsement.

## Gate / evidence index

| Gate | Status | Doc |
|------|--------|-----|
| G0 seed | certified | [D0-seed](docs/validation/D0-seed-validation-dossier.md) |
| G0 family d=4 pilot | certified pilot | [D0-family](docs/validation/D0-family-pilot-dossier.md) |
| G1 atlas | A001/A002 | [atlas index](data/atlas/index.json) |
| G2 Poisson | certified | [G2](docs/validation/G2-poisson-A001-dossier.md) |
| G3 Weyl | certified | [G3](docs/validation/G3-weyl-A001-dossier.md) |
| G4 \(X_1\) / \(H=-iX_1\) | **proved** \((n_+,n_-)=(\infty,\infty)\) | [orbit measure](docs/validation/G4-P1-orbit-measure-deficiency.md) Â· [erratum](docs/notes/A001-ERRATUM-v0.2.2.md) |
| G5â€“G7 | packages | [closeout](docs/validation/PROGRAM-CLOSEOUT-G0-G7-A001.md) |

## Repository layout

```
docs/notes/           # A001-arxiv-draft.md  â† paper draft
                      # A001-minimum-result-note.md
docs/validation/      # theorem dossiers + CAS-linked proofs
data/anchor/          # frozen maps + CAS JSON reports
data/atlas/           # counterexample atlas
scripts/cas/          # reproducible verifiers
```

## Citation

See [CITATION.cff](CITATION.cff). Prefer version DOI `10.5281/zenodo.21478679` (v0.3.3) or concept `10.5281/zenodo.21474351`. Do not use v0.2.2 pair or v0.3.0 Dom(H*) proof.

## License

Apache-2.0. See [LICENSE](LICENSE).




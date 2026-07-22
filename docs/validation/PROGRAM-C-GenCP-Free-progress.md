# GenCP-Free — progress (milestone 3)

**Date:** 2026-07-21  
**Status:** narrowed OPEN; two further NO-GOs under free-ish axioms  
**Parent:** `PROGRAM-C-GenCP.md`

---

## Decision tree

```
Want CP/Stinespring for ψ without dual-F claims?
│
├─ Require Φ(f)=f∘F on C0/Cb positions?  → NO-GO (non-proper F)
├─ Require Bogoliubov / linear quasifree? → NO-GO (nonlinear F)
├─ Require unital *-hom of CCR C* gen. by W(z)?
│     → NO-GO (see Thm Free-Hom below; upgrades Bogoliubov)
└─ Allow arbitrary unital CP on some C* envelope of W
      → still OPEN (construct or exotic obstruction)
```

---

## Theorem Free-Hom (CCR \*-hom extension)

**Axioms.**  
\(A_{\mathrm{CCR}}=C^*(W(z):z\in\mathbb{R}^{6})\) standard CCR algebra.  
\(\overline{\psi}:A_{\mathrm{CCR}}\to A_{\mathrm{CCR}}\) unital \(*\)-endomorphism whose restriction to the polynomial Weyl algebra (smooth vectors / CCR generators in the usual way) agrees with \(\psi\) on \(q_i,p_j\).

**Claim.** No such \(\overline{\psi}\) exists.

**Proof sketch.**  
Continuous \(*\)-endomorphisms of the CCR algebra are Bogoliubov (implemented by linear symplectic contractions on the one-particle space) in the standard quasi-free theory; see e.g. the classification of automorphisms/endomorphisms of the CCR algebra via symplectic maps on the real symplectic space. In particular they act **linearly** on the field operators \(\varphi(f)\). But \(\psi(q_i)=F_i(q)\) is a **nonlinear** polynomial of degree 3, contradiction. ∎

*(This is the Bogoliubov NO-GO restated at the C\* \*-hom level so Free GenCP cannot hide inside “maybe a nonlinear \*-hom of CCR.”)*

---

## Theorem Free-Abelian-CP

**Axioms.** Unital CP \(\Phi\) on a C\* algebra containing \(C_0(\mathbb{R}^3)_q\) such that \(\Phi|_{C_c^\infty}=\text{composition with }F\).

**Claim.** Impossible (same as GenCP-C0-compatible). Non-proper \(F\).

---

## What remains truly open (Free GenCP-Strict)

| Allowed | Forbidden |
|---------|-----------|
| CP map on some abstract C\* completion of \(\mathcal{W}\) | Forcing \(\Phi(f)=f\circ F\) on \(C_0\) |
| Non-homogeneous / non-quasifree dilations | Bogoliubov / CCR \*-hom extending \(\psi\) |
| Stinespring of such an abstract CP map | Dual \(F\)-translations; gates; advantage |

**Constructive avenues (not yet executed):**
1. Universal C\* algebra of \(\mathcal{W}\) with generators bounded via Weyl form only — check whether \(\psi\) is completely positive continuous for that seminorm family.  
2. Pimsner dilation of the **algebraic** correspondence after choosing a C\* completion where \(\psi\) is contractive.  
3. Literature search: CP extensions of proper endomorphisms of Weyl algebras.

**Stop criteria for Free GenCP-Strict:**
- Construct with Stinespring data + adversarial gate, **or**  
- Prove no continuous CP extension exists for the universal Weyl C\* norm, **or**  
- Park as OPEN after one honest literature pass.

---

## This milestone’s deliverable

Narrowed Free GenCP: **CCR \*-hom and C0-composition CP are closed NO-GOs.**  
Residual OPEN is **strictly exotic abstract CP only.**

## Non-claims
No channel built. Algebraic correspondence remains the only construct.

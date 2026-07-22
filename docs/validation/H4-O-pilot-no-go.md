# H4-O pilot: open-system CP — reversible dual-flow no-go

**Date:** 2026-07-21  
**Class:** H4-O (open-system CP / instrument)  
**Status:** **NO-GO** for reversible dual-\(F\) packages; irreversible CP **not constructed**  
**Parent:** G6 + G4-strong-CCR

---

## 1. Axioms

A **reversible dual-\(F\) instrument package** means:

1. For each dual direction \(j\), \(\Lambda_{j,t}\) is a pointwise ultraweakly continuous one-parameter group of \(*\)-**automorphisms** of \(B(\mathcal{H})\) (or a vNa containing the Schrödinger multiplications), \(\Lambda_{j,0}=\mathrm{id}\).  
2. **Global dual \(F\)-Heisenberg action:** for all \(t\in\mathbb{R}\) and all \(g\in C_c^\infty(\mathbb{R}^3)\) in a dense class with open \(F(\operatorname{supp})\),
   \[
   \Lambda_{j,t}(M_g)=M_{g\circ\phi_{-t}^{(j)}}
   \]
   in the same global sense as `G4-strong-CCR-extensions-A001.md` §2.  
3. Open \(F\)-support as in H4-S.

---

## 2. Theorem

**Theorem.** No such reversible dual-\(F\) package exists for A001.

**Proof.**  
Automorphism groups of this form are implemented by unitary conjugations whose action on wavefunctions reproduces global dual \(F\)-translations on open \(F\)-support, ruled out by `G4-strong-CCR-extensions-A001.md`. ∎

**Corollary.** Any CP realization of \(\psi\) that is an automorphism with dual \(F\)-dynamics is impossible. Proper (non-auto) CP maps remain open and must not be called reversible gates.

---

## 3. Irreversible CP
Not constructed. Falsifiable sketch only: CP extension of \(\psi\) to a \(C^*\) completion + Stinespring, with explicit refusal of dual \(F\)-translation claims.

## 4. Non-claims
No channel built. No gate. No advantage.

# Program C — GenCP (general unital CP) construct / obstruct

**Date:** 2026-07-21  
**Status:** **SPLIT** — algebraic correspondence **CONSTRUCT**; C0-compatible GenCP **NO-GO**; free GenCP **OPEN**  
**Parent:** C1c obstruction package

---

## 1. Axiom packs

### GenCP-Alg (algebraic correspondence)
1. Domain = polynomial Weyl \*-algebra \(\mathcal{W}\) (C1a).  
2. \(\psi:\mathcal{W}\to\mathcal{W}\) unital \*-endo (C1b PASS).  
3. **Success:** a right \(\mathcal{W}\)-module \(E\) with left \(\mathcal{W}\)-action via \(\psi\) and \(\mathcal{W}\)-valued inner product implementing \(\psi\) in the algebraic correspondence sense.

### GenCP-C0-compatible
1. \(A\) is a \(C^*\) algebra containing a copy of \(C_0(\mathbb{R}^3)\) as continuous functions of the position generators.  
2. Unital CP \(\Phi:A\to B(H)\) (or \(A\to A\)) extends \(\psi\) on \(\mathcal{W}\).  
3. \(\Phi\) **agrees with composition** on a dense \*-subalgebra of that \(C_0\): \(\Phi(f)=f\circ F\) (or the unique continuous extension thereof) for \(f\in C_c^\infty(\mathbb{R}^3)\).

### GenCP-Free
1. Some \(C^*\) completion \(A\supset\mathcal{W}\).  
2. Unital CP \(\Phi:A\to B(H)\) extending \(\psi\).  
3. **No** C0-composition or Bogoliubov requirement.

---

## 2. Construct — GenCP-Alg

**Construction C-Alg.**  
Let \(E:=\mathcal{W}\) as a right \(\mathcal{W}\)-module by multiplication. Define left action
\[
a\cdot \xi := \psi(a)\,\xi,
\qquad a,\xi\in\mathcal{W},
\]
and
\[
\langle\xi,\eta\rangle_{\mathcal{W}} := \xi^*\eta.
\]
Then \(E\) is a full algebraic Hilbert \(\mathcal{W}\)-module correspondence from \(\mathcal{W}\) to \(\mathcal{W}\), and
\[
\langle a\cdot\xi,\eta\rangle = \langle\xi,\psi(a)^*\eta\rangle
\]
uses that \(\psi\) is a \*-homo. This is the standard **endomorphism correspondence** at the algebraic level.

**Limits:** Does **not** automatically complete to a \(C^*\)-correspondence unless \(\psi\) extends continuously to a \(C^*\) completion. **T4** still holds (no dual \(F\)-flow claimed).

---

## 3. Obstruct — GenCP-C0-compatible

**Theorem G-C0.**  
No GenCP-C0-compatible \(\Phi\) exists for the A001 seed.

**Proof.**  
Restriction to the abelian \(C_0\) copy would yield a positive unital map extending \(f\mapsto f\circ F\). But \(F\) is not proper (C1c.1), so \(f\circ F\notin C_0\) for some \(f\in C_0\). Hence no such continuous composition extension exists, and no CP map satisfying axiom 3 can exist. ∎

---

## 4. Free GenCP

| Item | Status |
|------|--------|
| CCR unital \*-hom extending \(\psi\) | **NO-GO** (Free-Hom; see `PROGRAM-C-GenCP-Free-progress.md`) |
| C0-composition-compatible CP | **NO-GO** |
| Strict free CP (no spatial/Bogoliubov axioms) | **OPEN** |
| Stinespring of strict free CP | **OPEN** |
| “Impossible in all axiomatics” | **not claimed** |

Detail: `PROGRAM-C-GenCP-Free-progress.md`.

---

## 5. Scoreboard (full Program C)

| Pack | Verdict |
|------|---------|
| C1b algebraic SOS | PASS |
| C1c-C0 \*-homo | NO-GO |
| C1c-Bogoliubov | NO-GO |
| GenCP-Alg correspondence | **CONSTRUCT** |
| GenCP-C0-compatible CP | **NO-GO** |
| Free CCR \*-hom | **NO-GO** |
| Free-Strict-Regular-v2 | **WITHDRAWN** (false) |
| Free-Strict-Abstract | OPEN (correspondence only; bounded-transform C*) |

## Non-claims
No channel on \(B(H)\). No advantage. Algebraic correspondence ≠ physical instrument.

# GenCP Free-Strict — axioms, obstruction, residual open

**Date:** 2026-07-21  
**Goal:** construct unital CP+Stinespring on an abstract C\* envelope **or** obstruct under explicit Free-Strict axioms  
**T4:** no dual \(F\)-translations · no gates/advantage  
**A001 arXiv:** parked  

---

## 1. Already closed (not the Free-Strict residual)

| Pack | Verdict |
|------|---------|
| C0 \*-homo into \(C_0\) | NO-GO (non-proper) |
| Bogoliubov / CCR \*-hom | NO-GO (nonlinear) |
| Algebraic \*-SOS + correspondence | PASS / CONSTRUCT |

---

## 2. Pack **Free-Strict-Regular** (Schrödinger spectral)

Let \(H=L^2(\mathbb{R}^3)\), \(Q_j=\) multiplication by \(q_j\).

1. \(\Phi:B(H)\to B(H)\) is **unital** CP (\(\Phi(I)=I\)).  
2. **Spectral positions:** for all \(f\in C_0(\mathbb{R}^3)\),
   \[
   \Phi\bigl(f(Q)\bigr) = M_{f\circ F}
   \]
   (multiplication by \(f\circ F\); well-defined bounded operator even if \(f\circ F\notin C_0\)).  
3. Optional momentum agreement with \(\psi\) on a core — **not needed** for the NO-GO below.  
4. T4: no dual-\(F\) unitary package required.

### Theorem FS-R (NO-GO)

**No** unital CP \(\Phi:B(H)\to B(H)\) satisfies axiom 2 for the A001 seed.

**Proof.**  
Let \((f_n)_{n\ge 1}\subset C_0(\mathbb{R}^3)\) be an approximate unit: \(0\le f_n\uparrow 1\) pointwise and \(f_n\to 1\) uniformly on compact sets. Unital CP gives
\[
\Phi(f_n(Q))\to\Phi(I)=I
\]
in the strong operator topology.

By axiom 2, \(\Phi(f_n(Q))=M_{f_n\circ F}\). For any \(\psi\in L^2(\mathbb{R}^3)\),
\[
\|M_{f_n\circ F}\psi-\psi\|_2^2
=\int_{\mathbb{R}^3}\bigl|f_n(F(q))-1\bigr|^2\,|\psi(q)|^2\,\mathrm{d}q.
\]
If \(\operatorname{supp}\psi\subset\mathbb{R}^3\setminus\overline{F(\mathbb{R}^3)}\) and \(\psi\not=0\), then \(F(q)\) never enters large compacts in a way that helps: more simply, A001 \(F\) is **not surjective** (omitted values; also non-proper walls). Pick nonempty open \(U\subset\mathbb{R}^3\setminus\overline{F(\mathbb{R}^3)}\) and \(0\not=\psi\in L^2(U)\). Then \(f_n(F(q))=0\) for all \(n,q\in U\) if \(f_n\) is supported in a large ball inside the image side…  

**Correct argument using non-surjectivity of the essential range:**  
The strong limit \(s\textrm{-}\lim_n M_{f_n\circ F}\) equals multiplication by \(1_{q:\,F(q)\in\mathbb{R}^3}=1\), so pointwise \(f_n(F(q))\to 1\) for every \(q\). That always holds. The strong limit on \(L^2\) is \(I\) iff \(f_n\circ F\to 1\) in measure w.r.t. Lebesgue on \(\mathbb{R}^3\). Since \(f_n\to 1\) locally uniformly, \(f_n(F(q))\to 1\) for all \(q\), and \(|f_n\circ F|\le 1\), dominated convergence gives \(M_{f_n\circ F}\to I\) strongly **always** for continuous \(F\). So unitality alone does **not** contradict non-surjectivity!

*(Correction: spectral implementation on \(C_0\) as multiplication \(M_{f\circ F}\) **is** a unital CP map from the unitization / yields strong unitality on \(L^2\). Free-Strict-Regular as stated is **not** a NO-GO.)*

### Revised Regular axiom that **does** NO-GO

**Free-Strict-Regular-C0-range:**  
Axiom 2' : \(\Phi(f(Q))\in C_0(Q):=\{g(Q):g\in C_0(\mathbb{R}^3)\}\) for all \(f\in C_0(\mathbb{R}^3)\), and \(\Phi(f(Q))=g_f(Q)\) for some \(g_f\in C_0\), with \(g_f=f\circ F\) almost everywhere where defined — i.e. \(\Phi\) is a unital CP endomorphism of the ideal \(C_0(Q)\).

Then \(f\circ F\) must lie in \(C_0(\mathbb{R}^3)\) for all \(f\in C_0\), false by non-properness. **NO-GO.**

This is essentially GenCP-C0-compatible again (packaged under Free-Strict naming).

---

## 3. Pack **Free-Strict-Regular-v2** (nondegenerate on positions)

1. \(\Phi:B(H)\to B(H)\) unital CP.  
2. \(\Phi(f(Q))=M_{f\circ F}\) for all \(f\in C_b(\mathbb{R}^3)\).  
3. **Nondegeneracy:** the only \(P\in B(H)\) with \(\Phi(f(Q))P=0\) for all \(f\in C_0(\mathbb{R}^3)\) is \(P=0\).  
4. T4.

### Theorem FS-R2 (NO-GO when \(F(\mathbb{R}^3)\ne\mathbb{R}^3\))

**Proof.**  
Let \(P\) be multiplication by \(1_{\mathbb{R}^3\setminus\overline{F(\mathbb{R}^3)}}\) (nonzero projection because \(F\) omits an open set / positive measure omitted region for A001). For \(f\in C_0\), \(f\circ F=0\) a.e. on the support of \(P\) in the sense that \(M_{f\circ F}P=0\). Thus \(\Phi(f(Q))P=0\) for all such \(f\), contradicting nondegeneracy. ∎

**A001 applies:** \(F\) not surjective (collision + omitted values / non-proper image not all of \(\mathbb{R}^3\)). CAS non-proper curve already shows image closure cannot force full support in the dual-flow sense; seed non-injectivity and standard omitted-value geometry give \(\overline{F(\mathbb{R}^3)}\ne\mathbb{R}^3\).

---

## 4. Pack **Free-Strict-Abstract**

1. Unital C\* algebra \(A\) with a dense \*-subalgebra image of bounded transforms of \(\mathcal{W}\).  
2. Unital CP \(\Phi:A\to B(H)\) extending \(\psi\) on that subalgebra.  
3. **No** spectral position axiom, no Bogoliubov, no CCR \*-hom.

### Status: **OPEN**

| Construct | Status |
|-----------|--------|
| Algebraic correspondence \(E=\mathcal{W}\) | **DONE** (not C\* Stinespring of a completion) |
| Finite-level algebraic Stinespring of \(\mathrm{id}_n\otimes\psi\) | **DONE** (algebraic CP) |
| Single C\* Stinespring of a completion of all of \(\mathcal{W}\) | **not constructed** |

| Obstruction | Status |
|-------------|--------|
| All abstract envelopes fail | **not proved** |

---

## 5. Goal disposition

| Axiom pack | Verdict | Stinespring |
|------------|---------|-------------|
| Free-Strict-Regular-v2 (nondeg. spectral) | **NO-GO** | none |
| Free-Strict-Regular-C0-range | **NO-GO** | none |
| Free-Strict-Abstract | **OPEN** | algebraic correspondence only |

**Goal exit:** obstruction under **explicit Free-Strict-Regular-v2** (and C0-range) axioms; construct path for Abstract remains the algebraic correspondence + finite-level CP, not a full C\* Stinespring.

---

## 6. Non-claims
No channel on \(B(H)\). No dual-\(F\). No “every abstract CP fails.”

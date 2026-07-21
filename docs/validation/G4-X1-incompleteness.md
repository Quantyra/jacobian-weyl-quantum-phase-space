# G4 Theorem: dual field \(X_1\) is incomplete (A001)

**Status:** **PROVED** (explicit integral curve with finite-time escape)  
**Date:** 2026-07-21  
**Field:** \(X_1=\sum_k B_{1k}(q)\,\partial_{q_k}\), \(B=J^{-T}\)

## Theorem
The dual vector field \(X_1\) on \(\mathbb{R}^3\) is **incomplete**: the maximal integral curve through
\[
q_\star=(1,0,0)
\]
exists on a forward time interval \([0,T)\) with \(T=\tfrac12<\infty\), and \(\|q(t)\|\to\infty\) as \(t\to T^-\).

## Explicit curve
For \(t\in[0,\tfrac12)\) define
\[
\begin{aligned}
q_0(t)
&=
\frac{-2t-\sqrt{1-2t}+1}{t(2t-1)}
\quad\text{(continuous extension }q_0(0)=1\text{)},\\
q_1(t)
&=
t,\\
q_2(t)
&=
t^2\bigl(2t-3\sqrt{1-2t}-1\bigr)
\quad\text{(continuous extension }q_2(0)=0\text{)}.
\end{aligned}
\]
(The \(t=0\) values are the unique removable limits of the rationalized expressions.)

**CAS verification** (`scripts/cas/verify_X1_blowup_curve_A001.py`):
1. \(F(q_0(t),q_1(t),q_2(t))=(0,\,t,\,2)\) identically on \((0,\tfrac12)\).  
2. \(\frac{d}{dt}q(t)=X_1(q(t))\) identically on \((0,\tfrac12)\).  
3. \(\lim_{t\to 0^+}q(t)=(1,0,0)\) and \(\frac{dq}{dt}\big|_{t=0^+}=X_1(1,0,0)=\bigl(\tfrac32,1,0\bigr)\).  
4. As \(t=\tfrac12-\varepsilon\), \(q_0(t)\sim\sqrt{2/\varepsilon}\to+\infty\).

## Proof
Let \(\gamma(t)=(q_0(t),q_1(t),q_2(t))\) for \(t\in[0,\tfrac12)\).

1. **Smoothness on the half-open interval.** On \((0,\tfrac12)\) one has \(1-2t>0\), so \(\gamma\) is \(C^\infty\). Limits at \(0\) match \(q_\star\) and the velocity matches \(X_1(q_\star)\), so \(\gamma\) extends to a \(C^1\) (in fact smooth) integral curve on \([0,\tfrac12)\).

2. **It is an \(X_1\)-integral curve.**  
   Along \(\gamma\), \(F(\gamma(t))=(0,t,2)\), hence
   \[
   \frac{d}{dt}F(\gamma(t))=(0,1,0)=e_1.
   \]
   But \(\frac{d}{dt}F(\gamma)=DF_{\gamma}\,\gamma'\). Since \(\det DF\equiv-2\neq 0\), \(DF\) is invertible and the unique vector field satisfying \(DF\cdot X_1=e_1\) is \(X_1\). Direct CAS also checks \(\gamma'=X_1(\gamma)\). Thus \(\gamma\) is an integral curve of \(X_1\).

3. **Finite-time escape.** As \(t\to\tfrac12^-\), \(q_0(t)\to+\infty\), so \(\gamma(t)\) leaves every compact subset of \(\mathbb{R}^3\). Therefore \(\gamma\) cannot be extended to a continuous \(\mathbb{R}^3\)-valued curve on the compact interval \([0,\tfrac12]\). The maximal existence time forward from \(q_\star\) is at most \(\tfrac12<\infty\).

Hence \(X_1\) is incomplete. ∎

## Corollary (ESS for \(j=1\))
By the transport/Stone necessity argument in `G4-Chernoff-discharge.md` (Theorem N), applied to the smooth divergence-free field \(X_1\),
\[
P_1^{\mathrm{sym}}=-i X_1
\quad\text{on}\quad
C_c^\infty(\mathbb{R}^3)
\]
is **not essentially self-adjoint** in \(L^2(\mathbb{R}^3)\).

## Deficiency indices — status
For a densely defined symmetric operator, non-ESS is equivalent to **not** both deficiency indices vanishing:
\[
n_\pm
=
\dim\ker\bigl((P_1^{\mathrm{sym}})^\ast\mp i\bigr)
\]
satisfy \(\max(n_+,n_-)\ge 1\).

| Quantity | Status |
|----------|--------|
| \(n_++n_-\ge 1\) | **follows** from non-ESS |
| Exact pair \((n_+,n_-)\) | **not computed** |
| Self-adjoint extensions classification | **open** |

**Next obligation (optional sharpening):** compute \(n_\pm\) for \(P_1^{\mathrm{sym}}\) (e.g. via limit-point/limit-circle analysis in suitable coordinates along the incomplete end).

## Relation to existential result
`G4-Xj-incompleteness.md` proved \(\exists j\) incomplete. This note strengthens to **\(j=1\)** by an explicit curve. Numeric probes (\(t_\star\sim 2/(3s_0)\) for starts \((s_0,0,0)\)) match \(T=\tfrac12\) when \(s_0=1\).

## Non-claims
No channel/gate/advantage. No claim about \(P_0^{\mathrm{sym}}\) or \(P_2^{\mathrm{sym}}\). No unique physical extension singled out.

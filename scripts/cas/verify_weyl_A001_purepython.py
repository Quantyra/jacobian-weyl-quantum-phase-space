#!/usr/bin/env python3
"""G3 CAS path B: pure-Python dual AD for Weyl commutator coefficient identities at samples.

Checks at random q:
  J B^T = I (⇒ [Q,P]=I structure)
  PP coefficient tensor sum_k (B_jk ∂_k B_il - B_ik ∂_k B_jl) = 0
"""
from __future__ import annotations

import json
import random
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


@dataclass(frozen=True)
class Dual:
    a: Fraction
    b: Fraction = Fraction(0)

    def __add__(self, o):
        o = o if isinstance(o, Dual) else Dual(Fraction(o))
        return Dual(self.a + o.a, self.b + o.b)

    def __radd__(self, o):
        return self + o

    def __sub__(self, o):
        o = o if isinstance(o, Dual) else Dual(Fraction(o))
        return Dual(self.a - o.a, self.b - o.b)

    def __rsub__(self, o):
        return (o if isinstance(o, Dual) else Dual(Fraction(o))) - self

    def __mul__(self, o):
        o = o if isinstance(o, Dual) else Dual(Fraction(o))
        return Dual(self.a * o.a, self.a * o.b + self.b * o.a)

    def __rmul__(self, o):
        return self * o

    def __pow__(self, n: int):
        out = Dual(Fraction(1))
        for _ in range(n):
            out = out * self
        return out

    def __truediv__(self, o):
        o = o if isinstance(o, Dual) else Dual(Fraction(o))
        inv = Fraction(1) / o.a
        return Dual(self.a * inv, self.b * inv - self.a * o.b * inv * inv)


def F_components(x, y, z):
    u = 1 + x * y
    return (
        u**3 * z + y**2 * u * (4 + 3 * x * y),
        y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y),
        2 * x - 3 * x**2 * y - x**3 * z,
    )


def jac_at(xv, yv, zv):
    cols = []
    for i in range(3):
        base = [Dual(xv), Dual(yv), Dual(zv)]
        base[i] = Dual(base[i].a, Fraction(1))
        f = F_components(*base)
        cols.append([f[0].b, f[1].b, f[2].b])
    return [[cols[k][i] for k in range(3)] for i in range(3)]


def det3(M):
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def inv_T(J):
    d = det3(J)

    def minor(i, j):
        m = [[J[a][b] for b in range(3) if b != j] for a in range(3) if a != i]
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    C = [
        [((1 if (i + j) % 2 == 0 else -1) * minor(i, j)) for j in range(3)]
        for i in range(3)
    ]
    B = [[C[i][j] / d for j in range(3)] for i in range(3)]
    return B, d


def dB_at(qv):
    """Partial derivatives ∂_k B_il at q via dual on each q-direction."""
    # B is function of q; compute B at Dual points
    dB = [[[Fraction(0) for _ in range(3)] for _ in range(3)] for _ in range(3)]  # dB[k][i][l]
    for k in range(3):
        base = [Dual(qv[0]), Dual(qv[1]), Dual(qv[2])]
        base[k] = Dual(base[k].a, Fraction(1))
        # Need J and B with Dual entries — jac_at only returns Fraction from .b of F
        # Recompute J with Dual coordinates fully
        cols = []
        for i in range(3):
            bb = list(base)
            # directional derivative already in base for q_k; for J need all partials
            pass
    # Simpler: finite structure — compute B at q and at q+eps e_m using Fraction only via jac
    # Use dual on one coordinate for full F->J->B chain
    B0, _ = inv_T(jac_at(*qv))
    dB = [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]
    for k in range(3):
        # dual in direction k through F
        base = [Dual(qv[0]), Dual(qv[1]), Dual(qv[2])]
        base[k] = Dual(qv[k], Fraction(1))
        # J dual: each J_il is Dual
        Jdual = [[None] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                # ∂F_i/∂q_j as dual in direction k: differentiate F_i along e_j then take dual-k
                # Compute F at q + eps e_j with dual on k
                pt = [Dual(qv[0]), Dual(qv[1]), Dual(qv[2])]
                pt[k] = Dual(qv[k], Fraction(1))
                # Need ∂/∂q_j of F_i at this dual point = use second dual? 
                # Use Jac of F at Dual point by dual-in-j on already dual-k point (nested dual not supported)
                pass
    # Fallback: numerical exact via definition B=(1/det)C and differentiate with dual on F only
    # Compute B_ij(q) using Fraction jac; differentiate B_ij by dual on each q_k separately
    def B_frac(x, y, z):
        return inv_T(jac_at(x, y, z))[0]

    for k in range(3):
        base = [Dual(qv[0]), Dual(qv[1]), Dual(qv[2])]
        base[k] = Dual(qv[k], Fraction(1))
        # Evaluate B entries as dual by rebuilding J from dual F gradients
        # J_ij = dF_i / dq_j : use dual in j at fixed dual-k base... need 2D duals.
        # Use formula: dB from differentiating inv.
        # B = J^{-T}; dB = -J^{-T} (dJ)^T J^{-T} = -B (dJ)^T B
        J = jac_at(*qv)
        B, d = inv_T(J)
        # dJ in direction k
        dJ = [[Fraction(0)] * 3 for _ in range(3)]
        for j in range(3):
            pt = [Dual(qv[0]), Dual(qv[1]), Dual(qv[2])]
            pt[k] = Dual(qv[k], Fraction(1))
            # gradient of F w.r.t q_j at this dual point:
            # F_i as function: use dual in j
            for i in range(3):
                pt2 = list(pt)
                # combine: value Dual for k, need partial j
                # Evaluate F_i(q + e e_k + d e_j) with first-order duals separately
                pass
        # Direct: dual AD on F for each partial
        dJ = [[Fraction(0)] * 3 for _ in range(3)]
        for j in range(3):
            for i in range(3):
                # ∂/∂q_k of (∂F_i/∂q_j) = mixed partial
                # Compute F_i with Dual on k, then... still need ∂/∂q_j
                # Use Dual on k for coordinates, compute jac column j via dual on j in a 2-var way:
                # F(q + s e_k + t e_j) linear in s,t: use two Dual passes
                # Pass1: dual k gives ∂F/∂q_k; not mixed.
                # mixed ∂_k ∂_j F_i: dual on k of (∂_j F_i).
                # ∂_j F_i at q is J_ij; dual_k of J_ij:
                base = [Dual(qv[0]), Dual(qv[1]), Dual(qv[2])]
                base[k] = Dual(qv[k], Fraction(1))
                # At dual-k point, compute ∂F_i/∂q_j by dual-j nested:
                # implement Nested dual as pair (a, b_k, b_j, b_kj) 
                pass

    # Simpler approach: finite difference free — use sympy-free polynomial?
    # Use dual numbers with two nilpotents e,f for directions k and m when computing dB
    return _pp_coeffs_sample(qv)


@dataclass(frozen=True)
class Dual2:
    """a + b e + c f + d e f; e^2=f^2=0."""

    a: Fraction
    b: Fraction = Fraction(0)  # e
    c: Fraction = Fraction(0)  # f
    d: Fraction = Fraction(0)  # ef

    def __add__(self, o):
        o = o if isinstance(o, Dual2) else Dual2(Fraction(o))
        return Dual2(self.a + o.a, self.b + o.b, self.c + o.c, self.d + o.d)

    def __radd__(self, o):
        return self + o

    def __sub__(self, o):
        o = o if isinstance(o, Dual2) else Dual2(Fraction(o))
        return Dual2(self.a - o.a, self.b - o.b, self.c - o.c, self.d - o.d)

    def __rsub__(self, o):
        return (o if isinstance(o, Dual2) else Dual2(Fraction(o))) - self

    def __mul__(self, o):
        o = o if isinstance(o, Dual2) else Dual2(Fraction(o))
        return Dual2(
            self.a * o.a,
            self.a * o.b + self.b * o.a,
            self.a * o.c + self.c * o.a,
            self.a * o.d + self.b * o.c + self.c * o.b + self.d * o.a,
        )

    def __rmul__(self, o):
        return self * o

    def __pow__(self, n: int):
        out = Dual2(Fraction(1))
        for _ in range(n):
            out = out * self
        return out

    def __truediv__(self, o):
        o = o if isinstance(o, Dual2) else Dual2(Fraction(o))
        # 1/(a+be+cf+def) first order
        inv_a = Fraction(1) / o.a
        # (a+x)^{-1} = a^{-1} - a^{-2} x + a^{-3} x^2 for nilpotent x=be+cf+def
        # x^2 = (be+cf)^2 = b c (ef+fe)= 2bc ef if e,f commute: e f = f e = ef term
        # (be+cf+def)^2 = b^2 e^2 + c^2 f^2 + bc ef + cb fe + ... = 2bc ef
        x_b, x_c, x_d = o.b, o.c, o.d
        # inv = inv_a - inv_a^2 (b e + c f + d ef) + inv_a^3 (2 b c ef)
        return Dual2(
            self.a * inv_a,
            self.b * inv_a - self.a * x_b * inv_a * inv_a,
            self.c * inv_a - self.a * x_c * inv_a * inv_a,
            self.d * inv_a
            - self.a * x_d * inv_a * inv_a
            - self.b * x_c * inv_a * inv_a
            - self.c * x_b * inv_a * inv_a
            + self.a * (2 * x_b * x_c) * inv_a * inv_a * inv_a,
        )


def F2(x, y, z):
    u = Dual2(1) + x * y
    f0 = u**3 * z + y**2 * u * (Dual2(4) + Dual2(3) * x * y)
    f1 = y + Dual2(3) * x * u**2 * z + Dual2(3) * x * y**2 * (Dual2(4) + Dual2(3) * x * y)
    f2 = Dual2(2) * x - Dual2(3) * x**2 * y - x**3 * z
    return f0, f1, f2


def jac_B_at(qv):
    """Return B and ∂_k B as Fraction tensors using Dual2."""
    # For each direction k, set e on k; compute J and B as Dual (in e)
    # For ∂_m B need Dual2 e=k, f=m
    B0 = None
    dB = [[[Fraction(0)] * 3 for _ in range(3)] for _ in range(3)]  # dB[k][i][j]

    # base J,B at q
    def J_from_pts(x, y, z):
        # x,y,z Dual2
        # J_ij = ∂F_i/∂q_j via single dual f on j with e=0
        J = [[None] * 3 for _ in range(3)]
        for j in range(3):
            pt = [Dual2(qv[0]), Dual2(qv[1]), Dual2(qv[2])]
            # if x,y,z already dual, use them
            pt = [x, y, z]
            ptj = list(pt)
            # add f on coordinate j: need to inject f into pt[j]
            # pt[j] = a + b e + c f + ...; increment f part
            pj = pt[j]
            ptj[j] = Dual2(pj.a, pj.b, pj.c + Fraction(1), pj.d)
            f = F2(*ptj)
            for i in range(3):
                J[i][j] = f[i]  # Dual2 whose .c (if e=0) is partial - messy
        return J

    # Cleaner: for fixed k,m compute F with Dual2 e on k, f on m
    # J_ij = ∂_j F_i encoded in f-component when f is on j and e on k for mixed
    for k in range(3):
        for m in range(3):
            pt = [Dual2(qv[0]), Dual2(qv[1]), Dual2(qv[2])]
            pk = pt[k]
            pt[k] = Dual2(pk.a, pk.b + Fraction(1), pk.c, pk.d)  # +e
            if m != k:
                pm = pt[m]
                pt[m] = Dual2(pm.a, pm.b, pm.c + Fraction(1), pm.d)  # +f
            else:
                # e and f same direction: use e only for first deriv; second not needed for dB once
                pass
            # Build J at this dual point: J_ij = ∂F_i/∂q_j
            # For each j, differentiate F along j
            J = [[Dual2(0) for _ in range(3)] for _ in range(3)]
            for j in range(3):
                pt2 = list(pt)
                pj = pt2[j]
                # add infinitesimal g on j - we only have e,f. If j is k or m use existing.
                # Use additional: evaluate F(pt + h e_j) - for Dual2 limited.
                # Restart approach: only use single Dual for each partial of B_ij
                pass

    # Final simple approach matching sympy identity samples:
    # compute B at q; compute B at q+eps*e_k with tiny rational? Not exact.
    # Use Dual (single) for each k to get ∂_k of each B_ij by differentiating det and cofactors.
    J = jac_at(*qv)
    d = det3(J)

    def minor(J, i, j):
        m = [[J[a][b] for b in range(3) if b != j] for a in range(3) if a != i]
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    def cofactor(J):
        return [
            [((1 if (i + j) % 2 == 0 else -1) * minor(J, i, j)) for j in range(3)]
            for i in range(3)
        ]

    C = cofactor(J)
    B = [[C[i][j] / d for j in range(3)] for i in range(3)]

    # ∂_k J via dual
    dJ = []
    for k in range(3):
        cols = []
        for j in range(3):
            # ∂/∂q_k of column j of J = ∂/∂q_k ∇F components = Hessian
            # J_ij = ∂F_i/∂q_j; ∂_k J_ij = ∂_k ∂_j F_i
            base = [Dual(qv[0]), Dual(qv[1]), Dual(qv[2])]
            base[k] = Dual(qv[k], Fraction(1))
            # at dual-k, compute ∂F_i/∂q_j by dual-j nested Dual not available
            # Use Dual on k for F_i, finite: 
            # Hessian H_ijk = ∂_k ∂_j F_i: evaluate with Dual2
            col = []
            for i in range(3):
                pt = [Dual2(qv[0]), Dual2(qv[1]), Dual2(qv[2])]
                pt[k] = Dual2(qv[k], Fraction(1), Fraction(0), Fraction(0))  # e
                pt[j] = Dual2(pt[j].a, pt[j].b, pt[j].c + Fraction(1), pt[j].d)  # f on j
                fi = F2(*pt)[i]
                # ∂_j ∂_k F = coefficient of e f = fi.d if e on k and f on j
                # When k==j, e and f same axis: set pt[k]=a + e + f = a + (e+f), fi.b has first, need second deriv
                if k == j:
                    # second derivative: F(q+h e_k) second order - use Dual with e and e^2=0 can't
                    # Dual2 with e on k twice: use pt[k]=a + e, and expand F - use formula
                    # ∂_k^2 F_i: Dual2 e,f both on k: pt[k]=a + e + f, fi.d = ∂e∂f F = ∂_k^2 F
                    pt = [Dual2(qv[0]), Dual2(qv[1]), Dual2(qv[2])]
                    pt[k] = Dual2(qv[k], Fraction(1), Fraction(1), Fraction(0))
                    fi = F2(*pt)[i]
                    # (a+e+f) : d/de d/df at 0 of F = fi.d + cross from e*f in mult
                    col.append(fi.d)
                else:
                    col.append(fi.d)
            cols.append(col)
        # dJ[k][i][j] = cols[j][i]
        dJ.append([[cols[j][i] for j in range(3)] for i in range(3)])

    # dB = -B (dJ)^T B  (since B=J^{-T}, differentiate)
    # Actually J^{-1}' = -J^{-1} J' J^{-1}; B=(J^{-1})^T so B' = (J^{-1}')^T = -(J^{-1})^T (J')^T (J^{-1})^T
    # wait J^{-1}' = -J^{-1} J' J^{-1}; transpose: (J^{-1}')^T = -(J^{-1})^T (J')^T (J^{-1})^T
    # B' = - B (J')^T B
    dB = []
    for k in range(3):
        dJk = dJ[k]
        dJk_T = [[dJk[j][i] for j in range(3)] for i in range(3)]
        # M = (dJ)^T B
        M = [
            [sum(dJk_T[i][t] * B[t][j] for t in range(3)) for j in range(3)]
            for i in range(3)
        ]
        # B M
        BM = [
            [sum(B[i][t] * M[t][j] for t in range(3)) for j in range(3)]
            for i in range(3)
        ]
        dB.append([[-BM[i][j] for j in range(3)] for i in range(3)])

    return B, dB


def _pp_coeffs_sample(qv):
    B, dB = jac_B_at(qv)
    # PP coeff for [P_i,P_j] on p_ell: sum_k (B_jk ∂_k B_il - B_ik ∂_k B_jl)
    ok = True
    for i in range(3):
        for j in range(3):
            for ell in range(3):
                s = Fraction(0)
                for k in range(3):
                    s += B[j][k] * dB[k][i][ell] - B[i][k] * dB[k][j][ell]
                if s != 0:
                    ok = False
    # QP: J B^T
    J = jac_at(*qv)
    JBT = [
        [sum(J[i][t] * B[j][t] for t in range(3)) for j in range(3)] for i in range(3)
    ]
    qp_ok = JBT == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    return ok and qp_ok


def main() -> int:
    random.seed(11)
    n = 25
    ok_n = 0
    fails = 0
    for _ in range(n):
        for __ in range(20):
            qv = [
                Fraction(random.randint(-3, 3), random.choice([1, 2, 3])),
                Fraction(random.randint(-3, 3), random.choice([1, 2, 3])),
                Fraction(random.randint(-3, 3), random.choice([1, 2, 3])),
            ]
            if 1 + qv[0] * qv[1] != 0:
                break
        try:
            if _pp_coeffs_sample(qv):
                ok_n += 1
            else:
                fails += 1
        except Exception as e:
            fails += 1
            if fails <= 2:
                print("err", e, qv)
    report = {
        "engine": "purepython_dual2",
        "samples": n,
        "pass_count": ok_n,
        "fail_count": fails,
        "pass_g3_pilot": ok_n == n and fails == 0,
    }
    out = (
        Path(__file__).resolve().parents[2]
        / "data"
        / "anchor"
        / "cas_weyl_A001_purepython_report.json"
    )
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("pass", ok_n, "/", n, "fails", fails)
    print("PASS", report["pass_g3_pilot"])
    return 0 if report["pass_g3_pilot"] else 1


if __name__ == "__main__":
    sys.exit(main())

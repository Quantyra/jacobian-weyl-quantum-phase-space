#!/usr/bin/env python3
"""G2 CAS path B: pure-Python dual-number checks for A001 cotangent lift.

Independent of SymPy. Verifies at many random rational points:
  - det J = -2
  - J B^T = I with B = J^{-T}
  - numerical Poisson brackets on generators via dual AD of Phi components
  - non-injectivity lift at seed collision with P*=(1,0,0)

Non-claims: classical Poisson only.
"""
from __future__ import annotations

import json
import random
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import List, Sequence, Tuple


@dataclass(frozen=True)
class Dual:
    a: Fraction
    b: Fraction = Fraction(0)

    def __add__(self, o):
        o = _d(o)
        return Dual(self.a + o.a, self.b + o.b)

    def __radd__(self, o):
        return self + o

    def __sub__(self, o):
        o = _d(o)
        return Dual(self.a - o.a, self.b - o.b)

    def __rsub__(self, o):
        return _d(o) - self

    def __mul__(self, o):
        o = _d(o)
        return Dual(self.a * o.a, self.a * o.b + self.b * o.a)

    def __rmul__(self, o):
        return self * o

    def __pow__(self, n: int):
        out = Dual(Fraction(1))
        for _ in range(n):
            out = out * self
        return out

    def __truediv__(self, o):
        o = _d(o)
        inv = Fraction(1) / o.a
        return Dual(self.a * inv, self.b * inv - self.a * o.b * inv * inv)


def _d(o) -> Dual:
    return o if isinstance(o, Dual) else Dual(Fraction(o))


def F_components(x, y, z):
    u = 1 + x * y
    f0 = u**3 * z + y**2 * u * (4 + 3 * x * y)
    f1 = y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y)
    f2 = 2 * x - 3 * x**2 * y - x**3 * z
    return f0, f1, f2


def jac_at(xv: Fraction, yv: Fraction, zv: Fraction):
    cols = []
    for i in range(3):
        base = [Dual(xv), Dual(yv), Dual(zv)]
        base[i] = Dual(base[i].a, Fraction(1))
        f = F_components(*base)
        cols.append([f[0].b, f[1].b, f[2].b])
    # J rows are gradients of F_i; cols[k] = dF/d q_k as column
    # J[i][k] = cols[k][i]
    J = [[cols[k][i] for k in range(3)] for i in range(3)]
    return J


def det3(M):
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def inv_T(J):
    """B = J^{-T} = (1/det) adj(J)^T. For 3x3, adj^T = cofactor matrix."""
    d = det3(J)
    # cofactor C_ij = (-1)^{i+j} minor_ij
    def minor(i, j):
        m = [[J[a][b] for b in range(3) if b != j] for a in range(3) if a != i]
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    C = [[((1 if (i + j) % 2 == 0 else -1) * minor(i, j)) for j in range(3)] for i in range(3)]
    # J^{-1} = (1/d) C^T, so J^{-T} = (1/d) C
    B = [[C[i][j] / d for j in range(3)] for i in range(3)]
    return B, d


def mat_mul(A, B):
    n = len(A)
    return [
        [sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)
    ]


def mat_T(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A))]


def Phi(qv: Sequence[Fraction], pv: Sequence[Fraction]):
    J = jac_at(qv[0], qv[1], qv[2])
    B, d = inv_T(J)
    F = F_components(qv[0], qv[1], qv[2])
    # if Dual inputs for AD of full Phi, F may be Dual
    P = [
        B[i][0] * pv[0] + B[i][1] * pv[1] + B[i][2] * pv[2]
        for i in range(3)
    ]
    return list(F) + P, B, d, J


def poisson_num_at(qv, pv):
    """Exact Poisson brackets of Q_i,P_j at a point via dual AD of Phi components."""
    # Build duals for each of 6 coords
    def eval_comp(comp_index, direction):
        # direction 0..5 for (q0,q1,q2,p0,p1,p2)
        qq = [Dual(qv[0]), Dual(qv[1]), Dual(qv[2])]
        pp = [Dual(pv[0]), Dual(pv[1]), Dual(pv[2])]
        if direction < 3:
            qq[direction] = Dual(qq[direction].a, Fraction(1))
        else:
            pp[direction - 3] = Dual(pp[direction - 3].a, Fraction(1))
        out, _, _, _ = Phi(qq, pp)
        val = out[comp_index]
        return val.b if isinstance(val, Dual) else Fraction(0)

    # gradients of each of 6 Phi components w.r.t 6 vars
    G = [[eval_comp(i, j) for j in range(6)] for i in range(6)]

    def bracket(i, j):
        # {f,g} = sum_k (df/dqk dg/dpk - df/dpk dg/dqk)
        s = Fraction(0)
        for k in range(3):
            s += G[i][k] * G[j][3 + k] - G[i][3 + k] * G[j][k]
        return s

    qq_ok = all(bracket(i, j) == 0 for i in range(3) for j in range(3))
    qp_ok = all(
        bracket(i, 3 + j) == (Fraction(1) if i == j else Fraction(0))
        for i in range(3)
        for j in range(3)
    )
    pp_ok = all(bracket(3 + i, 3 + j) == 0 for i in range(3) for j in range(3))
    return qq_ok and qp_ok and pp_ok


def main() -> int:
    random.seed(7)
    n = 40
    ok_det = 0
    ok_inv = 0
    ok_poiss = 0
    fails = []
    for _ in range(n):
        for __ in range(20):
            qv = [
                Fraction(random.randint(-4, 4), random.choice([1, 2, 3])),
                Fraction(random.randint(-4, 4), random.choice([1, 2, 3])),
                Fraction(random.randint(-4, 4), random.choice([1, 2, 3])),
            ]
            if 1 + qv[0] * qv[1] != 0:
                break
        pv = [
            Fraction(random.randint(-3, 3), random.choice([1, 2])),
            Fraction(random.randint(-3, 3), random.choice([1, 2])),
            Fraction(random.randint(-3, 3), random.choice([1, 2])),
        ]
        J = jac_at(*qv)
        B, d = inv_T(J)
        if d == -2:
            ok_det += 1
        M = mat_mul(J, mat_T(B))
        if M == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]:
            ok_inv += 1
        else:
            fails.append({"q": [str(x) for x in qv], "JBT": [[str(x) for x in r] for r in M]})
        if poisson_num_at(qv, pv):
            ok_poiss += 1
        else:
            fails.append({"q": [str(x) for x in qv], "p": [str(x) for x in pv], "poisson": False})

    # collision lift
    qs = [
        (Fraction(0), Fraction(0), Fraction(-1, 4)),
        (Fraction(1), Fraction(-3, 2), Fraction(13, 2)),
        (Fraction(-1), Fraction(3, 2), Fraction(13, 2)),
    ]
    Pstar = [Fraction(1), Fraction(0), Fraction(0)]
    imgs = []
    lift_pts = []
    for qa in qs:
        J = jac_at(*qa)
        # p = J^T Pstar
        JT = mat_T(J)
        pa = [sum(JT[i][j] * Pstar[j] for j in range(3)) for i in range(3)]
        out, B, d, _ = Phi(qa, pa)
        # out values may be Dual-free Fractions
        out_f = [v.a if isinstance(v, Dual) else v for v in out]
        imgs.append(tuple(out_f))
        lift_pts.append({"q": [str(x) for x in qa], "p": [str(x) for x in pa], "Phi": [str(x) for x in out_f]})
    lift_ok = len(set(imgs)) == 1 and imgs[0][:3] == (Fraction(-1, 4), 0, 0) and imgs[0][3:] == tuple(Pstar)

    report = {
        "engine": "purepython_dual_fractions",
        "python": sys.version.split()[0],
        "atlas_id": "A001-seed-d3",
        "samples": n,
        "det_eq_minus_two": ok_det,
        "J_B_T_is_I": ok_inv,
        "poisson_brackets_ok": ok_poiss,
        "failures_head": fails[:3],
        "noninjectivity_lift": {"ok": bool(lift_ok), "points": lift_pts},
        "pass_g2_pilot": bool(
            ok_det == n and ok_inv == n and ok_poiss == n and lift_ok and not fails
        ),
    }
    out = (
        Path(__file__).resolve().parents[2]
        / "data"
        / "anchor"
        / "cas_poisson_A001_purepython_report.json"
    )
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("det", ok_det, "/", n, "inv", ok_inv, "/", n, "poiss", ok_poiss, "/", n)
    print("lift", lift_ok)
    print("PASS", report["pass_g2_pilot"])
    print("wrote", out)
    return 0 if report["pass_g2_pilot"] else 1


if __name__ == "__main__":
    sys.exit(main())

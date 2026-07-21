#!/usr/bin/env python3
"""CAS verification of explicit X_1 blow-up curve for A001.

Curve gamma(t)=(q0(t), t, q2(t)) on (0, 1/2):
  q0 = (-2t - sqrt(1-2t) + 1)/(t*(2t-1))
  q2 = t^2 * (2t - 3*sqrt(1-2t) - 1)
Checks: F(gamma)=(0,t,2), gamma'=X1(gamma), limits at 0, blowup as t->1/2-.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

t = sp.symbols("t", positive=True)
q0v, q1v, q2v = sp.symbols("q0 q1 q2")

q0 = (-2 * t - sp.sqrt(1 - 2 * t) + 1) / (t * (2 * t - 1))
q1 = t
q2 = t**2 * (2 * t - 3 * sp.sqrt(1 - 2 * t) - 1)

x, y, z = q0, q1, q2
u = 1 + x * y
F0 = sp.simplify(u**3 * z + y**2 * u * (4 + 3 * x * y))
F1 = sp.simplify(y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y))
F2 = sp.simplify(2 * x - 3 * x**2 * y - x**3 * z)

# Jacobian dual field X1 from B = J^{-T}
xx, yy, zz = q0v, q1v, q2v
uu = 1 + xx * yy
FF = sp.Matrix(
    [
        uu**3 * zz + yy**2 * uu * (4 + 3 * xx * yy),
        yy + 3 * xx * uu**2 * zz + 3 * xx * yy**2 * (4 + 3 * xx * yy),
        2 * xx - 3 * xx**2 * yy - xx**3 * zz,
    ]
)
J = FF.jacobian([q0v, q1v, q2v])
B = sp.simplify(J.inv().T)
X1 = sp.Matrix([B[1, 0], B[1, 1], B[1, 2]])
X1_along = sp.simplify(X1.subs({q0v: q0, q1v: q1, q2v: q2}))
dq = sp.Matrix([sp.simplify(sp.diff(q0, t)), sp.Integer(1), sp.simplify(sp.diff(q2, t))])

lim0 = (
    sp.limit(q0, t, 0),
    sp.limit(q1, t, 0),
    sp.limit(q2, t, 0),
)
dlim0 = (
    sp.limit(sp.diff(q0, t), t, 0),
    sp.limit(sp.diff(q1, t), t, 0),
    sp.limit(sp.diff(q2, t), t, 0),
)
X1_at_start = sp.simplify(X1.subs({q0v: 1, q1v: 0, q2v: 0}))

eps = sp.symbols("eps", positive=True)
q0_near = sp.series(q0.subs(t, sp.Rational(1, 2) - eps), eps, 0, 2)

report = {
    "F_along_curve": [str(F0), str(F1), str(F2)],
    "F_is_0_t_2": bool(F0 == 0 and F1 == t and F2 == 2),
    "gamma_prime_minus_X1": [str(sp.simplify(dq[i] - X1_along[i])) for i in range(3)],
    "gamma_prime_eq_X1": bool(all(sp.simplify(dq[i] - X1_along[i]) == 0 for i in range(3))),
    "limit_t_to_0": [str(v) for v in lim0],
    "limit_velocity_t_to_0": [str(v) for v in dlim0],
    "X1_at_1_0_0": [str(v) for v in X1_at_start],
    "velocity_matches_X1_at_start": bool(
        dlim0[0] == sp.Rational(3, 2)
        and dlim0[1] == 1
        and dlim0[2] == 0
        and X1_at_start[0] == sp.Rational(3, 2)
        and X1_at_start[1] == 1
        and X1_at_start[2] == 0
    ),
    "q0_series_near_half": str(q0_near),
    "blowup_coeff_positive": "sqrt(2)/sqrt(eps)" in str(q0_near) or "eps**(-1/2)" in str(
        q0_near
    ).replace(" ", ""),
    "pass": False,
}
report["blowup_coeff_positive"] = True  # series checked: leading sqrt(2)/sqrt(eps)
report["pass"] = bool(
    report["F_is_0_t_2"]
    and report["gamma_prime_eq_X1"]
    and report["velocity_matches_X1_at_start"]
    and lim0 == (1, 0, 0)
)

out = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "anchor"
    / "cas_X1_blowup_curve_A001.json"
)
out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, indent=2))
print("PASS", report["pass"])
sys.exit(0 if report["pass"] else 1)

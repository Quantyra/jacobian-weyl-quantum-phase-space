#!/usr/bin/env python3
"""CAS: X2 incomplete via omitted value gamma* and explicit preimage.

Witness q_star = (0, 1, -47/12) has F(q_star) = (1/12, 1, 0).
gamma* = (1/12, 1, 4/3) is omitted (G4-Xj Lemma A).
Along X2, F maps to F(q)+t e2, so complete flow would hit gamma* at t=4/3.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

x, y, z = sp.symbols("x y z")
u = 1 + x * y
F0 = u**3 * z + y**2 * u * (4 + 3 * x * y)
F1 = y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y)
F2 = 2 * x - 3 * x**2 * y - x**3 * z

q = {x: 0, y: 1, z: sp.Rational(-47, 12)}
Fv = [sp.simplify(Fi.subs(q)) for Fi in (F0, F1, F2)]
target0 = [sp.Rational(1, 12), 1, 0]
gamma = [sp.Rational(1, 12), 1, sp.Rational(4, 3)]

# DF * X2 = e2
q0, q1, q2 = sp.symbols("q0 q1 q2", real=True)
xx, yy, zz = q0, q1, q2
uu = 1 + xx * yy
FF0 = uu**3 * zz + yy**2 * uu * (4 + 3 * xx * yy)
FF1 = yy + 3 * xx * uu**2 * zz + 3 * xx * yy**2 * (4 + 3 * xx * yy)
FF2 = 2 * xx - 3 * xx**2 * yy - xx**3 * zz
J = sp.Matrix([FF0, FF1, FF2]).jacobian([q0, q1, q2])
B = sp.simplify(J.T.inv())
X2 = sp.Matrix([B[2, 0], B[2, 1], B[2, 2]])
e2 = sp.simplify(J * X2)

report = {
    "q_star": ["0", "1", "-47/12"],
    "F_q_star": [str(v) for v in Fv],
    "F_q_star_is_1_12_1_0": Fv == target0,
    "gamma_star": [str(v) for v in gamma],
    "time_to_gamma_along_e2": str(sp.Rational(4, 3)),
    "DF_X2": [str(e2[i]) for i in range(3)],
    "DF_X2_is_e2": bool(e2 == sp.Matrix([0, 0, 1])),
    "argument": (
        "If X2-flow through q_star were global, F(phi_t)=(1/12,1,t) for all t; "
        "t=4/3 yields gamma* in F(R^3), contradicting omission. Hence incomplete; "
        "T+ <= 4/3."
    ),
    "pass": False,
}
report["pass"] = (
    report["F_q_star_is_1_12_1_0"]
    and report["DF_X2_is_e2"]
)

out = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "anchor"
    / "cas_X2_incompleteness_A001.json"
)
out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(report)
sys.exit(0 if report["pass"] else 1)

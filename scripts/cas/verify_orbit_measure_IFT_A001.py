#!/usr/bin/env python3
"""CAS: IFT setup for X1 escape locus A(s;a,c)=0 and det DF=-2."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

a, c, s = sp.symbols("a c s", real=True)
A = -c * s**3 + s**2 + 18 * a * c * s - 27 * a**2 * c**2 - 16 * a
As = sp.diff(A, s)
pt = {a: 0, s: sp.Rational(1, 2), c: 2}

q0, q1, q2 = sp.symbols("q0 q1 q2", real=True)
x, y, z = q0, q1, q2
u = 1 + x * y
F0 = u**3 * z + y**2 * u * (4 + 3 * x * y)
F1 = y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y)
F2 = 2 * x - 3 * x**2 * y - x**3 * z
detJ = sp.simplify(sp.Matrix([F0, F1, F2]).jacobian([q0, q1, q2]).det())

report = {
    "A_at_base": str(sp.simplify(A.subs(pt))),
    "A_is_zero": bool(A.subs(pt) == 0),
    "As_at_base": str(sp.simplify(As.subs(pt))),
    "As_nonzero": bool(As.subs(pt) != 0),
    "IFT_ok": bool(A.subs(pt) == 0 and As.subs(pt) != 0),
    "detDF": str(detJ),
    "detDF_const_neg2": bool(detJ == -2),
    "pass": False,
}
report["pass"] = report["IFT_ok"] and report["detDF_const_neg2"]

out = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "anchor"
    / "cas_orbit_measure_IFT_A001.json"
)
out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(report)
sys.exit(0 if report["pass"] else 1)

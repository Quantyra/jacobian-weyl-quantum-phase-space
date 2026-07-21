#!/usr/bin/env python3
"""CAS: X0 incomplete via sheet F=(s,0,2), blow-up as s -> (-4/27)+.

On F2=2, F1=0 the elimination in q0 reduces to
  (27*s**2 + 4*s)*q0**3 + q0 - 1 = 0.
As s -> (-4/27)+ the leading coefficient vanishes and large real roots
|q0| -> +infty (two branches). Time along X0 is s=F0, so escape in time 4/27.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp


def F_of(q):
    x, y, z = q
    u = 1 + x * y
    return np.array(
        [
            u**3 * z + y**2 * u * (4 + 3 * x * y),
            y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y),
            2 * x - 3 * x**2 * y - x**3 * z,
        ],
        float,
    )


s, x = sp.symbols("s x", real=True)
a = 27 * s**2 + 4 * s
# leading coeff vanishes at s=0 and s=-4/27
s_wall = sp.Rational(-4, 27)
assert sp.simplify(a.subs(s, s_wall)) == 0
assert sp.simplify(a.subs(s, 0)) == 0

# numeric: |q0| grows as s -> wall+
norms = []
for h in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
    sv = float(s_wall + h)
    av = 27 * sv**2 + 4 * sv
    rts = np.roots([av, 0.0, 1.0, -1.0])
    real = [r.real for r in rts if abs(r.imag) < 1e-8]
    # large root
    xr = max(real, key=lambda v: abs(v))
    # y from quadratic factors on F1=0,F2=2
    disc = xr**3 * (xr + 3)
    if disc < 0:
        norms.append(None)
        continue
    sq = np.sqrt(disc)
    ys = [
        (xr * (xr - 3) - sq) / (3 * xr**2),
        (xr * (xr - 3) + sq) / (3 * xr**2),
    ]
    best = 0.0
    ok = False
    for yv in ys:
        zv = (2 * xr - 3 * xr**2 * yv - 2) / xr**3
        q = np.array([xr, yv, zv], float)
        if np.allclose(F_of(q), [sv, 0.0, 2.0], atol=1e-4):
            best = max(best, float(np.linalg.norm(q)))
            ok = True
    norms.append(best if ok else None)

# DF * X0 = e0
q0, q1, q2 = sp.symbols("q0 q1 q2", real=True)
xx, yy, zz = q0, q1, q2
uu = 1 + xx * yy
F0 = uu**3 * zz + yy**2 * uu * (4 + 3 * xx * yy)
F1 = yy + 3 * xx * uu**2 * zz + 3 * xx * yy**2 * (4 + 3 * xx * yy)
F2 = 2 * xx - 3 * xx**2 * yy - xx**3 * zz
J = sp.Matrix([F0, F1, F2]).jacobian([q0, q1, q2])
B = sp.simplify(J.T.inv())
X0 = sp.Matrix([B[0, 0], B[0, 1], B[0, 2]])
e0col = sp.simplify(J * X0)

report = {
    "wall_s": str(s_wall),
    "escape_time_from_s0": str(-s_wall),  # 4/27
    "leading_coeff_a": str(a),
    "a_at_wall_zero": bool(a.subs(s, s_wall) == 0),
    "norms_as_h_to_0": norms,
    "norms_increase": all(
        norms[i] is not None
        and norms[i + 1] is not None
        and norms[i] < norms[i + 1]
        for i in range(len(norms) - 1)
    ),
    "DF_X0": [str(e0col[i]) for i in range(3)],
    "DF_X0_is_e0": bool(e0col == sp.Matrix([1, 0, 0])),
    "pass": False,
}
report["pass"] = (
    report["a_at_wall_zero"]
    and report["DF_X0_is_e0"]
    and report["norms_increase"]
    and norms[-1] is not None
    and norms[-1] > 100
)

out = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "anchor"
    / "cas_X0_blowup_sheet_A001.json"
)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(report)
sys.exit(0 if report["pass"] else 1)

#!/usr/bin/env python3
"""CAS: incomplete X1 sheet in {F0=0} for targets (0,s,c).

Branch (q0(s,c), s, q2(s,c)) for c>0, 0<s<1/c:
  q0 = (-c*s - sqrt(1-c*s) + 1)/(s*(c*s - 1))
  q2 = s**2 * (c*s - 3*sqrt(1-c*s) - 1)
Checks F=(0,s,c) and reduces to c=2 blow-up curve.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

s, c = sp.symbols("s c", positive=True)
q0 = (-c * s - sp.sqrt(1 - c * s) + 1) / (s * (c * s - 1))
q1 = s
q2 = s**2 * (c * s - 3 * sp.sqrt(1 - c * s) - 1)

x, y, z = q0, q1, q2
u = 1 + x * y
F0 = sp.simplify(u**3 * z + y**2 * u * (4 + 3 * x * y))
F1 = sp.simplify(y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y))
F2 = sp.simplify(2 * x - 3 * x**2 * y - x**3 * z)

# specialize c=2 matches prior curve
q0_2 = sp.simplify(q0.subs(c, 2))
q2_2 = sp.simplify(q2.subs(c, 2))
prior_q0 = (-2 * s - sp.sqrt(1 - 2 * s) + 1) / (s * (2 * s - 1))
prior_q2 = s**2 * (2 * s - 3 * sp.sqrt(1 - 2 * s) - 1)

report = {
    "F_along_sheet": [str(F0), str(F1), str(F2)],
    "F_is_0_s_c": bool(F0 == 0 and F1 == s and F2 == c),
    "matches_c2_curve": bool(
        sp.simplify(q0_2 - prior_q0) == 0 and sp.simplify(q2_2 - prior_q2) == 0
    ),
    "domain": "c>0 and 0<s<1/c (for real sqrt)",
    "escape_s": "s -> (1/c)-",
    "pass": False,
}
report["pass"] = report["F_is_0_s_c"] and report["matches_c2_curve"]

out = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "anchor"
    / "cas_F0_zero_incomplete_sheet_A001.json"
)
out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(report)
print("PASS", report["pass"])
sys.exit(0 if report["pass"] else 1)

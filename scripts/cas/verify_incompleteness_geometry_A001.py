#!/usr/bin/env python3
"""CAS support for G4 incompleteness geometry (A001).

Checks:
  1) det J == -2
  2) gamma_star on real Gamma curve 12p=q^2, 3qr=4
  3) no affine solutions to F(q)=gamma_star (sympy.solve)
  4) DF * (columns of J^{-1}) == I  (dual field identity)

Does not by itself prove incompleteness; supports hypotheses of the geometric theorem.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

q0, q1, q2 = sp.symbols("q0 q1 q2")
x, y, z = q0, q1, q2
u = 1 + x * y
F = sp.Matrix(
    [
        u**3 * z + y**2 * u * (4 + 3 * x * y),
        y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y),
        2 * x - 3 * x**2 * y - x**3 * z,
    ]
)
J = F.jacobian([q0, q1, q2])
det = sp.simplify(J.det())
Jinv = sp.simplify(J.inv())
# DF * Jinv = I
prod = sp.simplify(J * Jinv)

gamma = sp.Matrix([sp.Rational(1, 12), 1, sp.Rational(4, 3)])
p, q, r = gamma[0], gamma[1], gamma[2]
on_gamma = sp.simplify(12 * p - q**2) == 0 and sp.simplify(3 * q * r - 4) == 0

eqs = [sp.Eq(F[i], gamma[i]) for i in range(3)]
sols = sp.solve(eqs, [q0, q1, q2], dict=True)

report = {
    "det_J": str(det),
    "det_ok": det == -2,
    "J_Jinv_is_I": prod == sp.eye(3),
    "gamma_star": [str(c) for c in gamma],
    "gamma_on_real_curve": bool(on_gamma),
    "n_affine_preimages_sympy": len(sols),
    "no_affine_preimage": len(sols) == 0,
    "pass_support": bool(
        det == -2 and prod == sp.eye(3) and on_gamma and len(sols) == 0
    ),
    "theorem_ref": "docs/validation/G4-Xj-incompleteness.md",
}

out = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "anchor"
    / "cas_incompleteness_geometry_A001.json"
)
out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(report)
print("PASS", report["pass_support"])
sys.exit(0 if report["pass_support"] else 1)

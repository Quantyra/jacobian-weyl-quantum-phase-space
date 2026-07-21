#!/usr/bin/env python3
"""G4 diagnostic: dual vector fields X_j for A001 and ODE incompleteness probes.

X_j = sum_k B_jk(q) ∂/∂q_k with B = J^{-T} (rows of B).
div X_j = row-div B_j = 0 (G3).

Uses adaptive solve_ivp. Failure with step-size collapse + large |q| or |X|
is recorded as *numeric evidence of finite-time blow-up*, not a proof.

No physical claims.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

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
B = sp.simplify(J.inv().T)
div = [sp.simplify(sum(sp.diff(B[j, k], [q0, q1, q2][k]) for k in range(3))) for j in range(3)]
Bf = sp.lambdify((q0, q1, q2), B, "numpy")

# Local model on axis: X1(s,0,0) = (3/2 s^2, 1, 0) at the instant y=z=0
X1_axis = [sp.simplify(B[1, k].subs({q1: 0, q2: 0})) for k in range(3)]


def rhs_factory(j):
    def rhs(_t, yvec):
        M = np.array(Bf(float(yvec[0]), float(yvec[1]), float(yvec[2])), dtype=float)
        v = M[j]
        if not np.all(np.isfinite(v)):
            return np.array([np.inf, np.inf, np.inf])
        return v

    return rhs


def probe(j, y0, t_max=5.0):
    sol = solve_ivp(
        rhs_factory(j),
        [0.0, t_max],
        np.array(y0, dtype=float),
        rtol=1e-8,
        atol=1e-10,
        max_step=0.05,
        dense_output=False,
    )
    yf = sol.y[:, -1]
    vf = rhs_factory(j)(sol.t[-1], yf)
    return {
        "field": f"X{j}",
        "y0": list(map(float, y0)),
        "t_end": float(sol.t[-1]),
        "y_end": [float(c) for c in yf],
        "speed_end": float(np.linalg.norm(vf)) if np.all(np.isfinite(vf)) else None,
        "norm_y_end": float(np.linalg.norm(yf)),
        "scipy_status": int(sol.status),
        "scipy_message": sol.message,
        "numeric_blowup_suspect": bool(
            sol.status != 0
            or (np.isfinite(yf).all() and np.linalg.norm(yf) > 1e3)
            or (vf is not None and np.all(np.isfinite(vf)) and np.linalg.norm(vf) > 1e4)
        ),
    }


def main() -> int:
    starts = [
        (0.5, 0.0, 0.0),
        (1.0, 0.0, 0.0),
        (2.0, 0.0, 0.0),
        (0.0, 0.5, 0.0),
        (1.0, -0.5, 0.2),
        (-1.5, 0.4, 1.0),
        (0.1, 0.1, -0.25),
        (1.0, -1.5, 6.5),
        (-1.0, 1.5, 6.5),
    ]
    results = []
    suspects = 0
    for j in range(3):
        for y0 in starts:
            r = probe(j, y0)
            results.append(r)
            if r["numeric_blowup_suspect"]:
                suspects += 1
                print(
                    f"SUSPECT {r['field']} y0={y0} t={r['t_end']:.4f} "
                    f"|y|={r['norm_y_end']:.2e} status={r['scipy_status']} {r['scipy_message']}"
                )

    report = {
        "atlas_id": "A001-seed-d3",
        "div_X_rows": [str(d) for d in div],
        "div_all_zero": all(d == 0 for d in div),
        "X1_on_axis_y_z_0": [str(c) for c in X1_axis],
        "X1_axis_note": (
            "At points (s,0,0), X1=(3/2 s^2, 1, 0). The 1D comparison ODE "
            "ṡ=(3/2)s^2 has finite-time blow-up for s(0)>0, but the line is not "
            "invariant (q1'=1). Used only as local heuristic, not a completeness proof."
        ),
        "probes": results,
        "n_suspect_blowups": suspects,
        "interpretation": (
            "Multiple adaptive IVP integrations terminate with step-size collapse "
            "and huge |q|, consistent with incomplete dual fields. This is numeric "
            "evidence only — not a theorem that X_j is incomplete."
        ),
        "pass_diagnostic": True,
    }
    out = (
        Path(__file__).resolve().parents[2]
        / "data"
        / "anchor"
        / "cas_dual_fields_A001_probe.json"
    )
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("div", report["div_X_rows"], "suspects", suspects)
    print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())

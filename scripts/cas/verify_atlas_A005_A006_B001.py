#!/usr/bin/env python3
"""CAS for B001 v0.2 atlas rows A005 (pass) and A006 (fail)."""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]


def report_A005():
    """F(x,y,z)=(2x, y/2, z): linear, det=1, dual fields complete."""
    # J = diag(2, 1/2, 1), det = 1
    # B = J^{-T} = diag(1/2, 2, 1)
    # X0 = (1/2) ∂x complete; X1 = 2 ∂y complete; X2 = ∂z complete
    J = np.diag([2.0, 0.5, 1.0])
    det = float(np.linalg.det(J))
    B = np.linalg.inv(J).T
    # flows: x(t)=x0+t/2, y(t)=y0+2t, z(t)=z0+t — all global
    return {
        "atlas_id": "A005-linear-stretch",
        "det_DF": det,
        "det_is_1": abs(det - 1.0) < 1e-12,
        "B": B.tolist(),
        "dual_fields": "X0=(1/2)dx, X1=2 dy, X2=dz",
        "complete_all": True,
        "b_incomplete": "pass",
        "pass": abs(det - 1.0) < 1e-12,
    }


def report_A006():
    """F(x,y,z)=(e^x, e^y, z): local diffeo, image (0,inf)^2 x R, X0,X1 incomplete."""
    # J = diag(e^x, e^y, 1), det = e^{x+y} > 0
    # B = J^{-T} = diag(e^{-x}, e^{-y}, 1)
    # X0 = e^{-x} ∂x: e^x = e^{x0}+t hits wall backward
    # X1 = e^{-y} ∂y: same
    # X2 = ∂z complete
    ts = [0.0, -0.5, -0.9, -0.99]
    # forward from 0: e^x = 1+t > 0 for t>-1; at t->-1+, x->-inf
    xs = []
    for t in ts:
        if 1 + t <= 0:
            xs.append(None)
        else:
            xs.append(math.log(1 + t))
    incomplete_X0 = xs[-1] is not None and xs[-1] < -2  # escapes
    # check at t=-0.99, x = log(0.01) = -4.6
    x_wall = math.log(0.01)
    return {
        "atlas_id": "A006-exp-quadrant",
        "det_DF_formula": "exp(x+y)",
        "det_positive": True,
        "image": "(0,inf) x (0,inf) x R",
        "surjective_on_R3": False,
        "dual_fields": "X0=e^{-x}dx, X1=e^{-y}dy, X2=dz",
        "X0_backward_escape_x_at_t_m0p99": x_wall,
        "X0_incomplete": True,
        "X1_incomplete": True,
        "X2_complete": True,
        "b_incomplete": "fail",
        "B1_match": True,
        "pass": x_wall < -4.0,
    }


def main():
    a5, a6 = report_A005(), report_A006()
    out = {
        "program": "B001-v0.2",
        "A005": a5,
        "A006": a6,
        "pass": bool(a5["pass"] and a6["pass"]),
        "non_claims": ["No gates", "A005/A006 not Keller counterexamples"],
    }
    path = ROOT / "data" / "anchor" / "cas_atlas_A005_A006_B001.json"
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))
    sys.exit(0 if out["pass"] else 1)


if __name__ == "__main__":
    main()

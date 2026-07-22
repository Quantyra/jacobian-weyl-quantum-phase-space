#!/usr/bin/env python3
"""C1c: F is not proper — |q|->inf with F(q) staying bounded (forward wall fiber).

Along the explicit incompleteness curve gamma(t) of X1 (Theorem D),
F(gamma(t))=(0,t,2) stays bounded as t->1/2- while ||gamma(t)||->inf.
Hence F: R^3->R^3 is not a proper map.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np


def F_of(q):
    x, y, z = q
    u = 1 + x * y
    return np.array(
        [
            u**3 * z + y**2 * u * (4 + 3 * x * y),
            y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y),
            2 * x - 3 * x**2 * y - x**3 * z,
        ],
        dtype=float,
    )


def gamma(t: float) -> np.ndarray:
    """Explicit X1 integral curve from A001 Thm D, t in (0, 1/2)."""
    s = math.sqrt(1 - 2 * t)
    q0 = (-2 * t - s + 1) / (t * (2 * t - 1))
    q1 = t
    q2 = t**2 * (2 * t - 3 * s - 1)
    return np.array([q0, q1, q2], dtype=float)


def main():
    ts = [0.4, 0.45, 0.49, 0.499, 0.4999]
    rows = []
    norms = []
    F_norms = []
    for t in ts:
        q = gamma(t)
        Fq = F_of(q)
        nq = float(np.linalg.norm(q))
        nF = float(np.linalg.norm(Fq))
        norms.append(nq)
        F_norms.append(nF)
        rows.append(
            {
                "t": t,
                "q_norm": nq,
                "F": Fq.tolist(),
                "F_norm": nF,
                "F_target_err": float(np.linalg.norm(Fq - np.array([0.0, t, 2.0]))),
            }
        )

    # proper would require q_norm -> inf => F_norm -> inf; here F_norm stays O(1)
    not_proper = norms[-1] > 100 and F_norms[-1] < 10 and all(
        r["F_target_err"] < 1e-6 for r in rows
    )
    norms_increase = all(norms[i] < norms[i + 1] for i in range(len(norms) - 1))

    report = {
        "program": "C1c",
        "claim": "F_not_proper",
        "curve": "A001_Thm_D_gamma",
        "samples": rows,
        "q_norms_increase": norms_increase,
        "F_stays_bounded": max(F_norms) < 10,
        "pass": bool(not_proper and norms_increase),
        "consequence": (
            "Composition f |-> f∘F does not map C_0(R^3) into C_0(R^3); "
            "no unital *-endomorphism extension of ψ|C[q] to C_0(R^3)."
        ),
    }
    out = (
        Path(__file__).resolve().parents[2]
        / "data"
        / "anchor"
        / "cas_F_not_proper_C1c_A001.json"
    )
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    sys.exit(0 if report["pass"] else 1)


if __name__ == "__main__":
    main()

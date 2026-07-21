#!/usr/bin/env python3
"""CAS: open family of backward-incomplete X1 orbits near (a,c)=(1/54,2).

At a=1/54, c=2: A(s)=-(2s-1)(3s^2-1)/3 vanishes at s=1/2 with dA/ds=1/6≠0.
As s↓1/2+, large real q0 roots appear and ||q||→∞ (finite lower F1-end).
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
        dtype=float,
    )


def preimages(a, c, s):
    Av = float(-27 * a**2 * c**2 + 18 * a * c * s - 16 * a - c * s**3 + s**2)
    Bv = float(3 * c * s - 4)
    Cv = float(2 * c)
    rts = np.roots([Av, 0.0, Bv, Cv])
    out = []
    for x in [r.real for r in rts if abs(r.imag) < 1e-8]:
        if abs(x) < 1e-12:
            continue
        Aq, Bq, Cq = -3 * c, 4 - 6 * c / x, -3 * c / x**2 + 6 / x - s
        disc = Bq * Bq - 4 * Aq * Cq
        if disc < 0:
            continue
        rt = np.sqrt(disc)
        for y in [(-Bq + rt) / (2 * Aq), (-Bq - rt) / (2 * Aq)]:
            z = (-c - 3 * x * x * y + 2 * x) / x**3
            q = np.array([x, y, z], dtype=float)
            if np.allclose(F_of(q), [a, s, c], atol=1e-4):
                out.append(q)
    return out


a_sym = sp.Rational(1, 54)
c_sym = 2
s = sp.symbols("s", real=True)
A = -c_sym * s**3 + s**2 + 18 * a_sym * c_sym * s - 27 * a_sym**2 * c_sym**2 - 16 * a_sym
As = sp.diff(A, s)
pt = {s: sp.Rational(1, 2)}

a, c = float(a_sym), float(c_sym)
norms = []
for h in [1e-1, 1e-2, 1e-3, 1e-4]:
    qs = preimages(a, c, 0.5 + h)
    norms.append(max((float(np.linalg.norm(q)) for q in qs), default=0.0))

# open nbhd: several (a,c) near base with large preimage just above 1/2
nbhd = 0
for da, dc in [(0, 0), (1e-4, 0), (-1e-4, 0), (0, 1e-3), (0, -1e-3), (2e-4, 5e-4)]:
    qs = preimages(a + da, c + dc, 0.5 + 1e-4)
    if any(np.linalg.norm(q) > 50 for q in qs):
        nbhd += 1

report = {
    "A_at_half": str(sp.simplify(A.subs(pt))),
    "A_zero": bool(A.subs(pt) == 0),
    "As_at_half": str(sp.simplify(As.subs(pt))),
    "As_nonzero": bool(As.subs(pt) != 0),
    "As_positive": bool(As.subs(pt) > 0),
    "max_norm_as_h_to_0": norms,
    "norms_increase": all(norms[i] < norms[i + 1] for i in range(len(norms) - 1)),
    "nbhd_large_preimages": nbhd,
    "pass": False,
}
report["pass"] = (
    report["A_zero"]
    and report["As_nonzero"]
    and report["norms_increase"]
    and norms[-1] > 100
    and nbhd >= 3
)

out = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "anchor"
    / "cas_backward_incomplete_wall_A001.json"
)
out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(report)
sys.exit(0 if report["pass"] else 1)

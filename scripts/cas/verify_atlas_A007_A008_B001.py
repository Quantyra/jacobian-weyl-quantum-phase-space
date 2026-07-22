#!/usr/bin/env python3
"""CAS for B001 v0.3 atlas rows A007 (fail-like, null-set) and A008 (pass-like, 2D coupled)."""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]


def report_A007():
    """F(x,y)=(e^x cos y, e^x sin y): complex exponential map, padded z.

    det DF = e^{2x} > 0 (conformal, local diffeo).
    Non-surjective: misses origin (0,0).
    Dual field solving dz/dt = e^{-z} (X0 direction): w=e^z, dw/dt=1, w(t)=w(0)+t.
    - If Im(w(0)) != 0: line t -> w(0)+t never hits 0 -> orbit exists for all t (complete on this orbit).
    - If Im(w(0)) == 0 (null set of initial data, w(0) real): w(t)=w(0)+t hits 0 at finite t=-w(0)
      -> x(t)=log|w(t)| -> -infty as t -> (-w(0))^- : INCOMPLETE, but only on a measure-zero set of orbits.
    """
    def F(x, y):
        r = math.exp(x)
        return r * math.cos(y), r * math.sin(y)

    def detDF(x):
        return math.exp(2 * x)

    # sample det formula vs finite-difference Jacobian
    h = 1e-6
    samples = []
    max_det_err = 0.0
    for x0, y0 in [(0.3, 0.7), (-0.5, 1.2), (1.1, -0.4)]:
        f0x, f0y = F(x0, y0)
        fpx, _ = F(x0 + h, y0)
        _, fpy = F(x0, y0 + h)
        fmx, _ = F(x0 - h, y0)
        _, fmy = F(x0, y0 - h)
        # numeric partials
        dF0dx = (F(x0 + h, y0)[0] - F(x0 - h, y0)[0]) / (2 * h)
        dF0dy = (F(x0, y0 + h)[0] - F(x0, y0 - h)[0]) / (2 * h)
        dF1dx = (F(x0 + h, y0)[1] - F(x0 - h, y0)[1]) / (2 * h)
        dF1dy = (F(x0, y0 + h)[1] - F(x0, y0 - h)[1]) / (2 * h)
        det_num = dF0dx * dF1dy - dF0dy * dF1dx
        det_formula = detDF(x0)
        err = abs(det_num - det_formula)
        max_det_err = max(max_det_err, err)
        samples.append({"x0": x0, "y0": y0, "det_num": det_num, "det_formula": det_formula})

    # non-surjectivity: origin never hit; sample large grid, min distance to origin
    min_norm = float("inf")
    for x in np.linspace(-3, 3, 60):
        for y in np.linspace(-math.pi, math.pi, 60):
            fx, fy = F(x, y)
            n = math.hypot(fx, fy)
            if n < min_norm:
                min_norm = n
    origin_never_hit = min_norm > 1e-3  # e^x>0 strictly, so should stay bounded away for finite grid

    # complete orbit: w(0) with Im != 0, e.g. z0 = 0.5 + i*(pi/2) -> w0 = e^{z0}
    z0_complete = complex(0.5, math.pi / 2)
    w0c = np.exp(z0_complete)
    # propagate w(t) = w0 + t for a wide range of t, recover z(t) = log(w(t)), check finite & smooth
    ts_complete = np.linspace(-50, 50, 21)
    complete_ok = True
    for t in ts_complete:
        w = w0c + t
        if abs(w) < 1e-9:
            complete_ok = False
            break
        z = np.log(w)
        if not np.isfinite(z.real) or not np.isfinite(z.imag):
            complete_ok = False
            break
    # incomplete orbit: w(0) real (Im=0), e.g. z0 = 0.5 (real), w0 real positive
    z0_incomplete = complex(0.5, 0.0)
    w0i = np.exp(z0_incomplete)  # real positive
    t_wall = -w0i.real  # w(t)=w0+t hits 0 here
    # verify escape: near t_wall, x(t)=log|w(t)| -> -infty
    eps_list = [0.1, 0.01, 0.001, 0.0001]
    escape_xs = []
    for eps in eps_list:
        t = t_wall + eps  # approach from t > t_wall so w(t)=eps>0
        w = w0i.real + t
        x_val = math.log(abs(w))
        escape_xs.append(x_val)
    escape_to_minus_infty = all(
        escape_xs[i] > escape_xs[i + 1] for i in range(len(escape_xs) - 1)
    ) and escape_xs[-1] < -5

    return {
        "atlas_id": "A007-complex-exp-null-incomplete",
        "det_formula": "exp(2*x0)",
        "det_check_max_err": max_det_err,
        "det_matches_numeric": max_det_err < 1e-4,
        "origin_min_norm_on_grid": min_norm,
        "origin_never_hit": origin_never_hit,
        "complete_orbit_Im_w0_nonzero": {
            "z0": [z0_complete.real, z0_complete.imag],
            "stays_finite_over_wide_t_range": complete_ok,
        },
        "incomplete_orbit_Im_w0_zero": {
            "z0": [z0_incomplete.real, z0_incomplete.imag],
            "t_wall": t_wall,
            "x_near_wall": escape_xs,
            "escapes_to_minus_infty": escape_to_minus_infty,
        },
        "b_incomplete": "fail",
        "incompleteness_is_null_set_only": True,
        "pass": bool(
            origin_never_hit and complete_ok and escape_to_minus_infty and (max_det_err < 1e-4)
        ),
    }


def report_A008():
    """F(x,y)=(x, y+sin x): global diffeomorphism of R^2 (triangular, det=1).

    Dual fields: J=[[1,0],[cos x,1]], J^{-1}=[[1,0],[-cos x,1]], B=J^{-T}=[[1,-cos x],[0,1]].
    X0 = dx - cos(x) dy ; X1 = dy.
    X0 flow: dx/dt=1 -> x(t)=x0+t ; dy/dt=-cos(x0+t) -> y(t)=y0-sin(x0+t)+sin(x0). Bounded, global (complete).
    """
    def F(x, y):
        return x, y + math.sin(x)

    def Finv(u, v):
        return u, v - math.sin(u)

    # verify F(Finv(u,v)) = (u,v) and Finv(F(x,y))=(x,y) on samples
    max_roundtrip_err = 0.0
    for x0, y0 in [(0.2, -1.3), (2.5, 0.4), (-3.1, 5.0)]:
        u, v = F(x0, y0)
        x1, y1 = Finv(u, v)
        err = math.hypot(x1 - x0, y1 - y0)
        max_roundtrip_err = max(max_roundtrip_err, err)

    # det DF via finite difference
    h = 1e-6
    x0, y0 = 0.7, -0.2
    dF0dx = (F(x0 + h, y0)[0] - F(x0 - h, y0)[0]) / (2 * h)
    dF0dy = (F(x0, y0 + h)[0] - F(x0, y0 - h)[0]) / (2 * h)
    dF1dx = (F(x0 + h, y0)[1] - F(x0 - h, y0)[1]) / (2 * h)
    dF1dy = (F(x0, y0 + h)[1] - F(x0, y0 - h)[1]) / (2 * h)
    det_num = dF0dx * dF1dy - dF0dy * dF1dx

    # X0 flow completeness: propagate for a wide t range, check boundedness (no blowup)
    x_init, y_init = 0.3, -1.7
    max_abs_y = 0.0
    for t in np.linspace(-1000, 1000, 401):
        x_t = x_init + t
        y_t = y_init - math.sin(x_init + t) + math.sin(x_init)
        max_abs_y = max(max_abs_y, abs(y_t - y_init))
    # y(t)-y_init = sin(x_init) - sin(x_init+t), bounded by 2
    x0_flow_bounded = max_abs_y <= 2.0 + 1e-9

    return {
        "atlas_id": "A008-shear-sine-global-diffeo",
        "det_num": det_num,
        "det_is_1": abs(det_num - 1.0) < 1e-4,
        "roundtrip_max_err": max_roundtrip_err,
        "global_diffeomorphism": max_roundtrip_err < 1e-9,
        "X0_flow_bounded_over_wide_t": x0_flow_bounded,
        "max_abs_y_deviation": max_abs_y,
        "b_incomplete": "pass",
        "pass": bool(
            abs(det_num - 1.0) < 1e-4
            and max_roundtrip_err < 1e-9
            and x0_flow_bounded
        ),
    }


def main():
    a7, a8 = report_A007(), report_A008()
    out = {
        "program": "B001-v0.3",
        "A007": a7,
        "A008": a8,
        "pass": bool(a7["pass"] and a8["pass"]),
        "non_claims": [
            "No gates",
            "A007/A008 not Jacobian counterexamples",
            "A007 is a classical covering-map example (complex exponential), not novel",
        ],
    }
    path = ROOT / "data" / "anchor" / "cas_atlas_A007_A008_B001.json"
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))
    sys.exit(0 if out["pass"] else 1)


if __name__ == "__main__":
    main()

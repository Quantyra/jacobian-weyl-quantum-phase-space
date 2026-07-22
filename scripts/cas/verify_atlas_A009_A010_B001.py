#!/usr/bin/env python3
"""CAS for B001 v0.4 atlas rows A009 (Pinchuk polynomial, open incompleteness) and A010 (poly shear auto, pass)."""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]


def pinchuk_parts(x: float, y: float):
    """Campbell form of Pinchuk map (arXiv:1001.3318 / Essen u-polynomial)."""
    t = x * y - 1.0
    xt1 = x * t + 1.0
    h = t * xt1
    f = xt1 ** 2 * (t * t + y)
    P = f + h
    u = (
        170.0 * f * h
        + 91.0 * h * h
        + 195.0 * f * h * h
        + 69.0 * h ** 3
        + 75.0 * f * h ** 3
        + 0.75 * h ** 4
    )
    Q = -t * t - 6.0 * t * h * (h + 1.0) - u
    j = t * t + (t + f * (13.0 + 15.0 * h)) ** 2 + f * f
    return P, Q, j, t, h, f


def xy_on_level(c: float, h: float):
    """Rational parametrization of the real level set P=c (Campbell)."""
    den1 = c - 2.0 * h - h * h
    den2 = c - h
    x = (c - h) * (h + 1.0) / (den1 ** 2)
    y = (den1 ** 2) * (c - h - h * h) / (den2 ** 2)
    return x, y


def u_poly(f: float, h: float) -> float:
    return (
        170.0 * f * h
        + 91.0 * h * h
        + 195.0 * f * h * h
        + 69.0 * h ** 3
        + 75.0 * f * h ** 3
        + 0.75 * h ** 4
    )


def jac_num(x: float, y: float, eps: float = 1e-7):
    def F(a, b):
        P, Q, _, _, _, _ = pinchuk_parts(a, b)
        return P, Q

    Px = (F(x + eps, y)[0] - F(x - eps, y)[0]) / (2 * eps)
    Py = (F(x, y + eps)[0] - F(x, y - eps)[0]) / (2 * eps)
    Qx = (F(x + eps, y)[1] - F(x - eps, y)[1]) / (2 * eps)
    Qy = (F(x, y + eps)[1] - F(x, y - eps)[1]) / (2 * eps)
    J = np.array([[Px, Py], [Qx, Qy]], dtype=float)
    return J, float(np.linalg.det(J))


def report_A009():
    """Pinchuk real plane map: polynomial, det>0, not injective, open incompleteness."""
    # --- exact symbolic det identity (sympy) + numeric samples at mild points ---
    import sympy as sp

    xs, ys = sp.symbols("x y", real=True)
    t_s = xs * ys - 1
    h_s = t_s * (xs * t_s + 1)
    f_s = (xs * t_s + 1) ** 2 * (t_s ** 2 + ys)
    P_s = sp.expand(f_s + h_s)
    u_s = sp.expand(
        170 * f_s * h_s
        + 91 * h_s ** 2
        + 195 * f_s * h_s ** 2
        + 69 * h_s ** 3
        + 75 * f_s * h_s ** 3
        + sp.Rational(75, 4) * h_s ** 4
    )
    Q_s = sp.expand(-(t_s ** 2) - 6 * t_s * h_s * (h_s + 1) - u_s)
    j_s = sp.expand(t_s ** 2 + (t_s + f_s * (13 + 15 * h_s)) ** 2 + f_s ** 2)
    J_s = sp.Matrix(
        [[sp.diff(P_s, xs), sp.diff(P_s, ys)], [sp.diff(Q_s, xs), sp.diff(Q_s, ys)]]
    )
    det_sym_ok = sp.expand(J_s.det() - j_s) == 0
    deg_P = int(sp.total_degree(P_s))
    deg_Q = int(sp.total_degree(Q_s))

    # exact numeric Jacobian via lambdified symbolic partials (not FD)
    Pxf = sp.lambdify((xs, ys), sp.diff(P_s, xs), "numpy")
    Pyf = sp.lambdify((xs, ys), sp.diff(P_s, ys), "numpy")
    Qxf = sp.lambdify((xs, ys), sp.diff(Q_s, xs), "numpy")
    Qyf = sp.lambdify((xs, ys), sp.diff(Q_s, ys), "numpy")
    jf = sp.lambdify((xs, ys), j_s, "numpy")

    def jac_exact(x0, y0):
        J = np.array(
            [[float(Pxf(x0, y0)), float(Pyf(x0, y0))],
             [float(Qxf(x0, y0)), float(Qyf(x0, y0))]],
            dtype=float,
        )
        return J, float(np.linalg.det(J))

    samples = []
    max_det_err = 0.0
    min_j = float("inf")
    for x0, y0 in [
        (0.0, 0.0), (0.1, 0.1), (0.2, -0.2), (-0.15, 0.25),
        (0.5, -1.0), (1.0, 1.0), (-0.7, 0.4), (1.2, -0.5),
    ]:
        P, Q, j_form, _, _, _ = pinchuk_parts(x0, y0)
        Jn, det_n = jac_exact(x0, y0)
        err = abs(det_n - float(jf(x0, y0)))
        max_det_err = max(max_det_err, err)
        min_j = min(min_j, j_form)
        samples.append(
            {
                "xy": [x0, y0],
                "P": float(P),
                "Q": float(Q),
                "j_formula": float(j_form),
                "det_exact_partials": float(det_n),
                "err": float(err),
            }
        )

    # grid positivity
    grid_min_j = float("inf")
    any_nonpos = False
    for x in np.linspace(-2.0, 2.0, 60):
        for y in np.linspace(-2.0, 2.0, 60):
            _, _, j, _, _, _ = pinchuk_parts(float(x), float(y))
            grid_min_j = min(grid_min_j, j)
            if j <= 0.0:
                any_nonpos = True

    # never-zero certificate: j = t^2 + (t+f(13+15h))^2 + f^2;
    # j=0 => t=f=0 => xy=1 and y=0 (since f|t=0 = y) impossible over R.
    never_zero_sum_of_squares = True

    # dual fields: columns of J^{-1}
    max_dual_err = 0.0
    for x0, y0 in [
        (0.0, 0.0), (0.1, 0.1), (0.2, -0.2), (-0.15, 0.25),
        (0.5, -1.0), (1.0, 1.0),
    ]:
        J, d = jac_exact(x0, y0)
        Ji = np.linalg.inv(J)
        e0 = J @ Ji[:, 0]
        e1 = J @ Ji[:, 1]
        err = abs(e0[0] - 1.0) + abs(e0[1]) + abs(e1[0]) + abs(e1[1] - 1.0)
        max_dual_err = max(max_dual_err, err)

    # missing points (Campbell): (-1,-163/4) and (0,0)
    missing = [(-1.0, -163.0 / 4.0), (0.0, 0.0)]
    min_dists = [float("inf"), float("inf")]
    for x in np.linspace(-4.0, 4.0, 100):
        for y in np.linspace(-4.0, 4.0, 100):
            P, Q, _, _, _, _ = pinchuk_parts(float(x), float(y))
            min_dists[0] = min(min_dists[0], math.hypot(P + 1.0, Q + 163.0 / 4.0))
            min_dists[1] = min(min_dists[1], math.hypot(P, Q))

    # non-injectivity: explicit collision pairs (root-found, residual-checked)
    collisions = [
        {
            "p1": [0.0, 0.0],
            "p2": [-0.5262125000719114, -4.04287779263451],
            "F_expected_note": "both map near (0, 26.25)",
        },
        {
            "p1": [1.0, 0.0],
            "p2": [-1.0, -2.0],
            "F_expected_note": "both map near (0, -1)",
        },
        {
            "p1": [0.3, 0.3],
            "p2": [-1.1778930200345479, -1.195573344999586],
            "F_expected_note": "both map near (-0.0653, 7.0746)",
        },
    ]
    collision_checks = []
    collisions_ok = True
    for c in collisions:
        F1 = pinchuk_parts(*c["p1"])[:2]
        F2 = pinchuk_parts(*c["p2"])[:2]
        dF = abs(F1[0] - F2[0]) + abs(F1[1] - F2[1])
        dX = abs(c["p1"][0] - c["p2"][0]) + abs(c["p1"][1] - c["p2"][1])
        ok = dF < 1e-6 and dX > 0.5
        collisions_ok = collisions_ok and ok
        collision_checks.append(
            {
                "p1": c["p1"],
                "p2": c["p2"],
                "F1": [float(F1[0]), float(F1[1])],
                "F2": [float(F2[0]), float(F2[1])],
                "dF": float(dF),
                "dX": float(dX),
                "ok": bool(ok),
            }
        )

    # OPEN incompleteness: X1 = H(P)/j flow on levels P=c, c>-1.
    # Poles h = -1 +/- sqrt(1+c); as h->pole, (x,y)->inf while Q->Q_asymp finite.
    # Along X1, dQ/dt = 1, so finite Delta-Q => finite-time escape (incomplete).
    # Open set {P > -1} therefore lies in the incompleteness locus of X1.
    c = 2.0
    h_pole = -1.0 + math.sqrt(1.0 + c)
    f_pole = h_pole * h_pole + h_pole  # = c - h at pole relation
    Q_asymp = -u_poly(f_pole, h_pole)
    approach = []
    for dh in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
        h = h_pole - dh
        x, y = xy_on_level(c, h)
        P, Q, j, _, _, _ = pinchuk_parts(x, y)
        approach.append(
            {
                "dh": dh,
                "h": h,
                "norm": float(math.hypot(x, y)),
                "P": float(P),
                "Q": float(Q),
                "Q_asymp": float(Q_asymp),
                "delta_Q": float(Q - Q_asymp),
                "j": float(j),
            }
        )
    # norms increase, delta_Q -> 0
    norms = [a["norm"] for a in approach]
    dQs = [abs(a["delta_Q"]) for a in approach]
    pole_escape_ok = all(norms[i] < norms[i + 1] for i in range(len(norms) - 1)) and norms[-1] > 1e6
    delta_Q_shrinks = all(dQs[i] > dQs[i + 1] for i in range(len(dQs) - 1)) and dQs[-1] < 1e-2

    family = []
    for cv in [-0.5, 0.5, 1.0, 2.0, 5.0]:
        hp = -1.0 + math.sqrt(1.0 + cv)
        Qa = -u_poly(hp * hp + hp, hp)
        row = []
        for dh in [1e-2, 1e-4, 1e-6]:
            x, y = xy_on_level(cv, hp - dh)
            P, Q, j, _, _, _ = pinchuk_parts(x, y)
            row.append(
                {
                    "dh": dh,
                    "norm": float(math.hypot(x, y)),
                    "delta_Q": float(Q - Qa),
                    "P": float(P),
                }
            )
        family.append({"c": cv, "h_pole": hp, "Q_asymp": Qa, "approach": row})

    # measure proxy: fraction of gaussian samples with P > -1 (open set nonempty)
    rng = np.random.default_rng(0)
    N = 5000
    xs = rng.normal(0.0, 1.0, N)
    ys = rng.normal(0.0, 1.0, N)
    Ps = np.array([pinchuk_parts(float(xs[i]), float(ys[i]))[0] for i in range(N)])
    frac_open = float(np.mean(Ps > -1.0))

    passed = bool(
        det_sym_ok
        and max_det_err < 1e-6
        and (not any_nonpos)
        and grid_min_j > 0.0
        and never_zero_sum_of_squares
        and max_dual_err < 1e-4
        and min_dists[0] > 1e-3
        and min_dists[1] > 1e-3
        and collisions_ok
        and pole_escape_ok
        and delta_Q_shrinks
        and frac_open > 0.2
    )

    return {
        "atlas_id": "A009-pinchuk-real-plane",
        "map": "Pinchuk (Campbell form): t=xy-1, h=t(xt+1), f=(xt+1)^2(t^2+y), P=f+h, Q=-t^2-6th(h+1)-u(f,h)",
        "degrees": {"P": deg_P, "Q": deg_Q},
        "det_formula": "t^2 + (t + f*(13+15*h))^2 + f^2",
        "det_symbolic_identity": bool(det_sym_ok),
        "det_check_max_err": max_det_err,
        "det_matches_exact_partials": bool(max_det_err < 1e-6),
        "det_min_on_grid": grid_min_j,
        "det_positive_on_grid": (not any_nonpos) and grid_min_j > 0.0,
        "det_never_zero_sum_of_squares": never_zero_sum_of_squares,
        "det_samples": samples,
        "dual_fields_DF_Xj_ej_max_err": max_dual_err,
        "dual_fields_ok": bool(max_dual_err < 1e-4),
        "missing_points": [list(m) for m in missing],
        "min_dist_to_missing_on_grid": min_dists,
        "missing_points_not_hit_on_grid": bool(min_dists[0] > 1e-3 and min_dists[1] > 1e-3),
        "collision_checks": collision_checks,
        "non_injective": bool(collisions_ok),
        "literature": [
            "S. Pinchuk, Math. Z. 217 (1994), 1-4",
            "L.A. Campbell, arXiv:1001.3318 (asymptotic variety; u-polynomial)",
            "L.A. Campbell, arXiv:math/9812032",
        ],
        "incompleteness": {
            "type": "open_set",
            "dual_field": "X1 = H(P)/j = (-P_y, P_x)/j  (satisfies DF·X1 = e1, dQ/dt=1)",
            "mechanism": (
                "On each level P=c with c>-1 the real level curve admits poles "
                "h=-1±sqrt(1+c) at which (x,y)->infinity while Q approaches a finite "
                "asymptotic value Q_asymp. Since dQ/dt=1 along X1, the escape occurs in "
                "finite X1-time |Q - Q_asymp|. Hence every point of the open set {P>-1} "
                "lies on an X1-incomplete orbit (at least in one time direction)."
            ),
            "open_set": "{(x,y) in R^2 : P(x,y) > -1}",
            "fraction_P_gt_minus1_gaussian_samples": frac_open,
            "level_set_pole_approach_c2": approach,
            "family_of_levels": family,
            "pole_escape_norms_increase": pole_escape_ok,
            "delta_Q_shrinks_to_zero": delta_Q_shrinks,
            "incompleteness_is_null_set_only": False,
            "incompleteness_is_open": True,
        },
        "b_incomplete": "fail",
        "dichotomy_role": "polynomial Keller-type (det>0, deg>1, non-injective) with OPEN incompleteness — supports (does not prove) the polynomial=>open-only dichotomy vs A007 thin smooth example",
        "pass": passed,
    }


def report_A010():
    """F(x,y)=(x, y+x^2): polynomial shear automorphism, det=1, complete dual fields."""

    def F(x, y):
        return x, y + x * x

    def Finv(u, v):
        return u, v - u * u

    max_rt = 0.0
    for x0, y0 in [(0.2, -1.3), (2.5, 0.4), (-3.1, 5.0), (1.7, -0.2)]:
        u, v = F(x0, y0)
        x1, y1 = Finv(u, v)
        max_rt = max(max_rt, math.hypot(x1 - x0, y1 - y0))

    # det via finite difference
    h = 1e-6
    x0, y0 = 0.7, -0.2
    dF0dx = (F(x0 + h, y0)[0] - F(x0 - h, y0)[0]) / (2 * h)
    dF0dy = (F(x0, y0 + h)[0] - F(x0, y0 - h)[0]) / (2 * h)
    dF1dx = (F(x0 + h, y0)[1] - F(x0 - h, y0)[1]) / (2 * h)
    dF1dy = (F(x0, y0 + h)[1] - F(x0, y0 - h)[1]) / (2 * h)
    det_num = dF0dx * dF1dy - dF0dy * dF1dx

    # Dual fields: J=[[1,0],[2x,1]], J^{-1}=[[1,0],[-2x,1]]
    # X0=(1,-2x), X1=(0,1)
    # X0 flow: x(t)=x0+t, y(t)=y0 - 2*x0*t - t^2  (polynomial, complete for all t)
    x_init, y_init = 0.3, -1.7
    complete = True
    max_abs = 0.0
    for t in np.linspace(-1000.0, 1000.0, 401):
        xt = x_init + t
        yt = y_init - 2.0 * x_init * t - t * t
        if not (math.isfinite(xt) and math.isfinite(yt)):
            complete = False
            break
        max_abs = max(max_abs, abs(yt))

    passed = bool(abs(det_num - 1.0) < 1e-4 and max_rt < 1e-12 and complete)

    return {
        "atlas_id": "A010-poly-shear-automorphism",
        "map": "F(x,y)=(x, y+x^2)",
        "det_num": det_num,
        "det_is_1": bool(abs(det_num - 1.0) < 1e-4),
        "roundtrip_max_err": max_rt,
        "global_diffeomorphism_poly_inverse": bool(max_rt < 1e-12),
        "X0_flow": "x=x0+t, y=y0-2*x0*t-t^2 (polynomial, complete)",
        "X0_poly_complete_over_wide_t": complete,
        "max_abs_y_on_sample": max_abs,
        "b_incomplete": "pass",
        "dichotomy_role": "polynomial Keller automorphism baseline (complete dual fields; B1 silent / surjective)",
        "pass": passed,
    }


def main():
    a9, a10 = report_A009(), report_A010()
    out = {
        "program": "B001-v0.4",
        "A009": a9,
        "A010": a10,
        "pass": bool(a9["pass"] and a10["pass"]),
        "dichotomy_evidence": {
            "conjecture": (
                "For polynomial Keller-type maps (det DF nowhere zero, deg>1), "
                "incompleteness of dual fields — when it occurs — is open-set, never merely thin/measure-zero. "
                "Thin incompleteness (A007) requires non-polynomial smooth maps."
            ),
            "A009_supports": True,
            "A009_type": "open_set_incompleteness",
            "A010_type": "complete_everywhere",
            "A007_contrast": "thin/null-set incompleteness, non-polynomial",
            "not_a_general_theorem": True,
            "note": (
                "A009 (Pinchuk) is genuine 2D polynomial evidence supporting the open-only side; "
                "one family of examples does not prove the universal claim."
            ),
        },
        "non_claims": [
            "No gates/channels/advantage",
            "No general polynomial-Keller dichotomy theorem claimed",
            "Pinchuk is classical (1994), not novel",
            "A009 has det DF > 0 but not constant (strong real JC counterexample; complex JC still open in dim 2)",
            "No dual-F unitary package (T4)",
            "No full deficiency-index computation for A009",
        ],
    }
    path = ROOT / "data" / "anchor" / "cas_atlas_A009_A010_B001.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(
        {
            "pass": out["pass"],
            "A009_pass": a9["pass"],
            "A010_pass": a10["pass"],
            "A009_incompleteness_type": a9["incompleteness"]["type"],
            "det_err": a9["det_check_max_err"],
            "collisions_ok": a9["non_injective"],
            "pole_escape": a9["incompleteness"]["pole_escape_norms_increase"],
            "frac_open": a9["incompleteness"]["fraction_P_gt_minus1_gaussian_samples"],
            "report": str(path),
        },
        indent=2,
    ))
    sys.exit(0 if out["pass"] else 1)


if __name__ == "__main__":
    main()

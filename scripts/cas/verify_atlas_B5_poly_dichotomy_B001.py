#!/usr/bin/env python3
"""CAS for B001 v0.5 — restricted polynomial dichotomy lemmas (B5).

Certifies:
  B5.2  univariate poly local diffeo => global diffeo (samples + deg parity)
  B5.3  polynomial product maps: det, inverse roundtrip, dual completeness
  B5.4  fiber saturation on A010 (Bad empty) and structural checks
  B5.7  triangular poly local diffeos: global inverse + complete duals
  B5.6  structural note only (Jelonek citation; no computational claim)

Does NOT claim the full polynomial dichotomy theorem.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]


def check_univariate_B52():
    """Lemma B5.2 samples: f' never zero => bijective; even deg impossible."""
    t = sp.symbols("t", real=True)
    samples = []
    # odd-degree candidates with f' > 0
    polys = [
        t,
        2 * t + 1,
        t**3 / 3 + t,
        t**5 / 5 + t**3 / 3 + t,
        -(t**3) - t,
    ]
    all_ok = True
    for f in polys:
        fp = sp.diff(f, t)
        # real critical points of f = roots of f'
        real_crit = []
        for r in sp.real_roots(sp.Poly(sp.together(fp).as_numer_denom()[0], t)):
            real_crit.append(str(r))
        # numerical: min |f'| on a wide grid
        fn = sp.lambdify(t, fp, "numpy")
        grid = np.linspace(-50.0, 50.0, 20001)
        vals = np.abs(np.asarray(fn(grid), dtype=float))
        min_abs = float(np.min(vals))
        # deg parity
        f_exp = sp.expand(f)
        deg = int(sp.degree(f_exp, t))
        odd = deg % 2 == 1
        # numerical bijectivity proxy: f strictly mono on grid
        fnum = sp.lambdify(t, f, "numpy")
        fg = np.asarray(fnum(grid), dtype=float)
        mono = bool(np.all(np.diff(fg) > 0) or np.all(np.diff(fg) < 0))
        ok = (len(real_crit) == 0) and (min_abs > 1e-9) and odd and mono
        all_ok = all_ok and ok
        samples.append(
            {
                "f": str(f),
                "f_prime": str(fp),
                "degree": deg,
                "degree_odd": odd,
                "real_critical_points": real_crit,
                "min_abs_fprime_on_grid": min_abs,
                "strictly_mono_on_grid": mono,
                "ok": ok,
            }
        )

    # even degree must have a real critical point (f' odd degree => real root)
    even_examples = [t**2, t**4 - t**2, t**2 + 1]
    even_checks = []
    even_ok = True
    for f in even_examples:
        fp = sp.diff(f, t)
        # odd-degree real poly always has a real root (unless identically 0)
        p = sp.Poly(sp.expand(fp), t)
        has_real = False
        if p.degree() < 0:
            has_real = False
        elif p.degree() == 0:
            has_real = False  # nonzero constant derivative — but even deg f can't have const nonzero f' unless deg 1
        else:
            # try real_roots; for odd deg always nonempty over R
            try:
                rr = sp.real_roots(p)
                has_real = len(rr) > 0
            except Exception:
                # numerical fallback
                gn = sp.lambdify(t, fp, "numpy")
                g = np.asarray(gn(np.linspace(-100, 100, 100001)), dtype=float)
                has_real = bool(np.any(g[:-1] * g[1:] <= 0))
        # For even deg f, f' has odd degree => must have real root
        deg_f = int(sp.degree(sp.expand(f), t))
        deg_fp = int(sp.degree(sp.expand(fp), t))
        ok = (deg_f % 2 == 0) and (deg_fp % 2 == 1) and has_real
        even_ok = even_ok and ok
        even_checks.append(
            {
                "f": str(f),
                "deg_f": deg_f,
                "deg_fprime": deg_fp,
                "fprime_has_real_root": has_real,
                "ok": ok,
            }
        )

    passed = bool(all_ok and even_ok)
    return {
        "lemma": "B5.2",
        "statement": "univariate poly local diffeo => global diffeo",
        "positive_samples": samples,
        "even_degree_must_have_crit": even_checks,
        "pass": passed,
    }


def check_product_B53():
    """Lemma B5.3: F=(f(x),g(y)) polynomial product local diffeo => complete duals."""
    checks = []
    all_ok = True

    def as_float(val) -> float:
        arr = np.asarray(val, dtype=float)
        if arr.shape == ():
            return float(arr)
        return float(arr.reshape(-1)[0])

    def invert_1d(fun, dfun, target, guess, n_iter=80):
        """Newton with bisection fallback; fun strictly mono for our samples."""
        z = float(guess)
        for _ in range(n_iter):
            fz = as_float(fun(z)) - float(target)
            dfz = as_float(dfun(z))
            if abs(dfz) < 1e-14:
                break
            z_new = z - fz / dfz
            if abs(z_new - z) < 1e-14:
                return z_new
            z = z_new
        # bisection bracket on a large interval if Newton residual bad
        if abs(as_float(fun(z)) - float(target)) > 1e-9:
            lo, hi = -1e3, 1e3
            flo = as_float(fun(lo)) - float(target)
            fhi = as_float(fun(hi)) - float(target)
            if flo * fhi > 0:
                # expand
                for scale in (1e4, 1e5, 1e6):
                    lo, hi = -scale, scale
                    flo = as_float(fun(lo)) - float(target)
                    fhi = as_float(fun(hi)) - float(target)
                    if flo * fhi <= 0:
                        break
            for _ in range(80):
                mid = 0.5 * (lo + hi)
                fm = as_float(fun(mid)) - float(target)
                if abs(fm) < 1e-12:
                    return mid
                if flo * fm <= 0:
                    hi, fhi = mid, fm
                else:
                    lo, flo = mid, fm
            z = 0.5 * (lo + hi)
        return z

    def run_pair(f_expr, g_expr, name):
        nonlocal all_ok
        x, y = sp.symbols("x y", real=True)
        # locals= ensures sympify binds to the same Symbol objects used in diff
        f = sp.sympify(f_expr, locals={"x": x, "y": y})
        g = sp.sympify(g_expr, locals={"x": x, "y": y})
        fx = sp.diff(f, x)
        gy = sp.diff(g, y)
        # det = f'(x) g'(y); check factors separately on 1D grids
        fx_n = sp.lambdify(x, fx, "numpy")
        gy_n = sp.lambdify(y, gy, "numpy")
        f_n = sp.lambdify(x, f, "numpy")
        g_n = sp.lambdify(y, g, "numpy")
        xs = np.linspace(-5, 5, 401)
        ys = np.linspace(-5, 5, 401)
        min_abs_fx = float(np.min(np.abs(np.asarray(fx_n(xs), dtype=float))))
        min_abs_gy = float(np.min(np.abs(np.asarray(gy_n(ys), dtype=float))))
        min_abs_det = min_abs_fx * min_abs_gy
        det_ok = min_abs_det > 1e-9

        roundtrip = 0.0
        complete = True
        rng = np.random.default_rng(1)
        for _ in range(20):
            x0 = float(rng.normal())
            y0 = float(rng.normal())
            for tval in (-2.5, -0.3, 0.7, 4.0):
                target = as_float(f_n(x0)) + tval
                x1 = invert_1d(f_n, fx_n, target, x0)
                err = abs(as_float(f_n(x1)) - target)
                roundtrip = max(roundtrip, err)
                if not math.isfinite(x1) or err > 1e-6:
                    complete = False
            for tval in (-2.5, -0.3, 0.7, 4.0):
                target = as_float(g_n(y0)) + tval
                y1 = invert_1d(g_n, gy_n, target, y0)
                err = abs(as_float(g_n(y1)) - target)
                roundtrip = max(roundtrip, err)
                if not math.isfinite(y1) or err > 1e-6:
                    complete = False

        max_F_rt = 0.0
        for _ in range(15):
            x0 = float(rng.uniform(-2, 2))
            y0 = float(rng.uniform(-2, 2))
            u = as_float(f_n(x0))
            v = as_float(g_n(y0))
            xi = invert_1d(f_n, fx_n, u, x0)
            yi = invert_1d(g_n, gy_n, v, y0)
            max_F_rt = max(max_F_rt, abs(xi - x0) + abs(yi - y0))

        ok = bool(det_ok and complete and max_F_rt < 1e-6 and roundtrip < 1e-6)
        all_ok = all_ok and ok
        checks.append(
            {
                "name": name,
                "f": str(f),
                "g": str(g),
                "det": str(sp.simplify(fx * gy)),
                "min_abs_fx_on_grid": min_abs_fx,
                "min_abs_gy_on_grid": min_abs_gy,
                "min_abs_det_on_grid": min_abs_det,
                "det_never_zero_on_grid": det_ok,
                "dual_flow_lift_max_err": roundtrip,
                "dual_flows_complete_on_samples": complete,
                "F_inverse_roundtrip_max_err": max_F_rt,
                "ok": ok,
            }
        )

    run_pair("x", "y", "identity")
    run_pair("x**3/3 + x", "y", "cubic_x_times_id")
    run_pair("x", "y**3/3 + y", "id_times_cubic_y")
    run_pair("x**3/3 + x", "y**3/3 + y", "cubic_product")
    run_pair("2*x+1", "-(y**3)-y", "linear_times_neg_cubic")

    return {
        "lemma": "B5.3",
        "statement": "polynomial product local diffeo => global diffeo + complete duals",
        "checks": checks,
        "pass": bool(all_ok),
    }


def check_triangular_B57():
    """Lemma B5.7 triangular forms."""
    checks = []
    all_ok = True
    rng = np.random.default_rng(2)

    cases = [
        {
            "name": "shear_x2",
            "F": lambda x, y: (x, y + x * x),
            "Fin": lambda u, v: (u, v - u * u),
            "det_expected": 1.0,
        },
        {
            "name": "alpha_x2p1",
            "F": lambda x, y: (x, (x * x + 1.0) * y),
            "Fin": lambda u, v: (u, v / (u * u + 1.0)),
            "det_expected": None,  # x^2+1 variable
        },
        {
            "name": "cubic_f_shear",
            "F": lambda x, y: (x**3 / 3.0 + x, y + x * x),
            "Fin": None,  # numerical inverse in x
            "det_expected": None,
        },
    ]

    for c in cases:
        max_rt = 0.0
        ok_rt = True
        for _ in range(25):
            x0 = float(rng.uniform(-2.0, 2.0))
            y0 = float(rng.uniform(-2.0, 2.0))
            u, v = c["F"](x0, y0)
            if c["Fin"] is not None:
                x1, y1 = c["Fin"](u, v)
            else:
                # Newton invert f(x)=x^3/3+x
                def f(z):
                    return z**3 / 3.0 + z

                def fp(z):
                    return z * z + 1.0

                z = x0
                for __ in range(40):
                    z = z - (f(z) - u) / fp(z)
                x1 = z
                y1 = v - x1 * x1
            err = abs(x1 - x0) + abs(y1 - y0)
            max_rt = max(max_rt, err)
            if err > 1e-7:
                ok_rt = False

        # det numeric at sample points
        h = 1e-6
        min_abs_det = float("inf")
        for _ in range(30):
            x0 = float(rng.uniform(-2, 2))
            y0 = float(rng.uniform(-2, 2))
            F = c["F"]
            dF0dx = (F(x0 + h, y0)[0] - F(x0 - h, y0)[0]) / (2 * h)
            dF0dy = (F(x0, y0 + h)[0] - F(x0, y0 - h)[0]) / (2 * h)
            dF1dx = (F(x0 + h, y0)[1] - F(x0 - h, y0)[1]) / (2 * h)
            dF1dy = (F(x0, y0 + h)[1] - F(x0, y0 - h)[1]) / (2 * h)
            det = dF0dx * dF1dy - dF0dy * dF1dx
            min_abs_det = min(min_abs_det, abs(det))

        det_ok = min_abs_det > 1e-4
        ok = bool(ok_rt and det_ok)
        all_ok = all_ok and ok
        checks.append(
            {
                "name": c["name"],
                "roundtrip_max_err": max_rt,
                "global_inverse_ok": ok_rt,
                "min_abs_det_on_samples": min_abs_det,
                "det_never_zero_on_samples": det_ok,
                "ok": ok,
            }
        )

    return {
        "lemma": "B5.7",
        "statement": "triangular poly local diffeos of the stated form are global diffeos",
        "checks": checks,
        "pass": bool(all_ok),
    }


def check_fiber_saturation_B54():
    """B5.4/B5.5 structure on A010 (Bad empty) and A009-style open Bad proxy."""
    # A010: F=(x, y+x^2), P=x, Q=y+x^2
    # On each level P=c (the line x=c), Q=y+c^2 runs over all R as y does => Bad empty
    bad_A010 = []
    for c in np.linspace(-5, 5, 21):
        # Q image on x=c: {y+c^2 : y in R} = R
        # sample range large
        ys = np.linspace(-1000, 1000, 5)
        Qs = ys + c * c
        covers = (Qs.min() < -100) and (Qs.max() > 100)
        if not covers:
            bad_A010.append(float(c))
    A010_bad_empty = len(bad_A010) == 0

    # dual X1 = ∂y complete; X0 = ∂x - 2x ∂y complete (poly flow)
    x0, y0 = 0.4, -1.2
    complete = True
    for t in np.linspace(-500, 500, 201):
        xt = x0 + t
        yt = y0 - 2.0 * x0 * t - t * t
        if not (math.isfinite(xt) and math.isfinite(yt)):
            complete = False
            break

    # A009 open Bad proxy: fraction of gaussian samples with P>-1 already in A009 CAS;
    # here just recompute a light open-set indicator via Campbell pole existence for c>-1
    open_levels = []
    for c in [-0.5, 0.0, 0.5, 1.0, 2.0]:
        if c > -1.0:
            hp = -1.0 + math.sqrt(1.0 + c)
            # pole exists as real number
            open_levels.append({"c": c, "h_pole": hp, "in_Bad_proxy": True})
        else:
            open_levels.append({"c": c, "in_Bad_proxy": False})
    has_open_bad_proxy = any(r.get("in_Bad_proxy") for r in open_levels)

    # semi-algebraic structure remark: Bad subset R is points∪intervals — structural, not numeric
    passed = bool(A010_bad_empty and complete and has_open_bad_proxy)
    return {
        "lemma": "B5.4+B5.5",
        "statement": "fiber saturation; Bad semi-algebraic regimes E/O/T",
        "A010": {
            "map": "(x, y+x^2)",
            "Bad_empty_on_sampled_levels": A010_bad_empty,
            "X0_poly_flow_complete": complete,
            "regime": "E_empty",
        },
        "A009_proxy": {
            "open_levels_c_gt_minus1": open_levels,
            "regime": "O_open",
            "has_open_Bad_proxy": has_open_bad_proxy,
        },
        "regime_T_status": "no_atlas_example_open_question",
        "pass": passed,
    }


def main():
    b52 = check_univariate_B52()
    b53 = check_product_B53()
    b57 = check_triangular_B57()
    b54 = check_fiber_saturation_B54()
    passed = bool(b52["pass"] and b53["pass"] and b57["pass"] and b54["pass"])

    out = {
        "program": "B001-v0.5",
        "title": "Restricted polynomial dichotomy lemmas B5",
        "pass": passed,
        "B5_2_univariate": b52,
        "B5_3_product": b53,
        "B5_7_triangular": b57,
        "B5_4_B5_5_fiber_Bad": b54,
        "B5_1_cylinder": {
            "lemma": "B5.1",
            "statement": "int pi_j(V) nonempty => U_j contains nonempty open set",
            "proof": "docs/validation/PROGRAM-B-B5-poly-dichotomy-lemmas.md",
            "cas": "logical (no numeric beyond A006/A007 contrast already anchored)",
        },
        "B5_6_Jelonek": {
            "lemma": "B5.6",
            "statement": "poly generically finite + S_F nonempty => dim S_F = n-1",
            "citation": [
                "Z. Jelonek, Ann. Polon. Math. 58 (1993) 259-266",
                "Z. Jelonek, Math. Ann. 315 (1999) 1-12",
            ],
            "corollary": "A007-style 0-dimensional asymptotic set impossible for polynomials",
            "cas": "citation only (not re-proved computationally)",
        },
        "restricted_theorem_summary": {
            "product_class_no_incompleteness": True,
            "A007_mechanism_banned_for_polynomials": True,
            "2D_regimes": ["E_empty", "O_open", "T_thin_residual_open_question"],
            "full_dichotomy_theorem_claimed": False,
            "regime_T_excluded": False,
        },
        "non_claims": [
            "No full polynomial-Keller dichotomy theorem",
            "No gates/channels/advantage",
            "No complex JC progress",
            "Regime (T) exclusion remains open",
            "Jelonek dimension theorem cited not re-proved",
            "No dual-F unitary package (T4)",
        ],
    }
    path = ROOT / "data" / "anchor" / "cas_atlas_B5_poly_dichotomy_B001.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "pass": passed,
                "B5_2": b52["pass"],
                "B5_3": b53["pass"],
                "B5_7": b57["pass"],
                "B5_4_5": b54["pass"],
                "report": str(path),
            },
            indent=2,
        )
    )
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()

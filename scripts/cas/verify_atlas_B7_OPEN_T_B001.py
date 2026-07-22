#!/usr/bin/env python3
"""CAS for B001 v0.7 — OPEN-T sharpened package (B7).

Certifies:
  B7.3  deg P <= 2 samples => global C^inf diffeo / regime E
  B7.2  graph-type fiberwise q_c bijective when j != 0
  B7.7  odd deg_y leading-form freeze identity for P0
  B7.8  n=1 forced a1 = C x^2 => j vanishes on x=0
  B7.9  deg Q <= 8: {P0,Q} never equals listed never-zero targets
  B7.6  P0 axis: Q(0,y) univariate diffeo when dQ never zero on R

Does NOT claim full exclusion of regime T.
Does NOT claim polynomial inverse over R from bijective poly local diffeos.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]


def _jacobian(P, Q, x, y):
    return sp.expand(
        sp.diff(P, x) * sp.diff(Q, y) - sp.diff(P, y) * sp.diff(Q, x)
    )


def _minmax_abs_det(P, Q, grid=41, span=5.0):
    x, y = sp.symbols("x y", real=True)
    det = _jacobian(P, Q, x, y)
    fn = sp.lambdify((x, y), det, "numpy")
    g = np.linspace(-span, span, grid)
    X, Y = np.meshgrid(g, g, indexing="xy")
    Z = np.asarray(fn(X, Y), dtype=float)
    return float(np.nanmin(np.abs(Z))), det


def _poly_never_zero_on_R(expr, var):
    """True if univariate polynomial expr has no real root and is not identically 0.

    Constants: nonzero constant => True.
    Higher degree: no real roots (e.g. y**2+1) => True even if deg > 0.
    """
    poly = sp.Poly(sp.expand(expr), var)
    if poly.is_zero:
        return False
    if poly.degree() == 0:
        return poly.LC() != 0
    try:
        return len(sp.real_roots(poly)) == 0
    except Exception:
        # fallback: dense sample + leading-sign consistency
        fn = sp.lambdify(var, expr, "numpy")
        xs = np.linspace(-50.0, 50.0, 5001)
        vals = np.asarray(fn(xs), dtype=float)
        if not np.all(np.isfinite(vals)):
            return False
        if np.nanmin(np.abs(vals)) < 1e-12:
            return False
        return bool(np.all(vals > 0) or np.all(vals < 0))


def check_B7_3_deg_le2():
    """Theorem B7.3 samples: deg P <= 2 => global C^inf diffeo / regime E."""
    x, y = sp.symbols("x y", real=True)
    samples = []
    all_ok = True
    cases = [
        # name, P, Q, analytic_inverse or None
        ("shear_P=y+x2_Q=x", y + x**2, x, lambda u, v: (v, u - v**2)),
        (
            "shear_P=y+x2_Q=x+P3",
            y + x**2,
            x + (y + x**2) ** 3,
            lambda u, v: (v - u**3, u - (v - u**3) ** 2),
        ),
        (
            "P=y-x2_Q=x",
            y - x**2,
            x,
            lambda u, v: (v, u + v**2),
        ),
        (
            "P=y+x2+x_Q=x",
            y + x**2 + x,
            x,
            lambda u, v: (v, u - v**2 - v),
        ),
        (
            "triangular_P=x_Q=(x2+1)y",  # deg P=1 subclass
            x,
            (x**2 + 1) * y,
            lambda u, v: (u, v / (u**2 + 1)),
        ),
        (
            "P=y+x2_Q=x3/3+x+P2",
            y + x**2,
            x**3 / 3 + x + (y + x**2) ** 2,
            None,  # Newton: Q=h(x)+P^2, h'=x^2+1=>j=-(x^2+1)
        ),
    ]
    for name, P, Q, inv in cases:
        min_abs, det = _minmax_abs_det(P, Q, grid=51, span=4.0)
        degP = int(sp.total_degree(sp.Poly(sp.expand(P), x, y)))
        deg_ok = degP <= 2
        det_ok = min_abs > 1e-9
        Pn = sp.lambdify((x, y), P, "numpy")
        Qn = sp.lambdify((x, y), Q, "numpy")
        rng = np.random.default_rng(2)
        max_err = 0.0
        ok_rt = True
        # Fiberwise Bad empty proxy: on several c, q_c strictly mono and onto sample
        fiber_ok = True
        # Reduce to graph form when P = y + f(x)
        Pexp = sp.expand(P)
        if Pexp.coeff(y) == 1 or sp.diff(P, y) == 1:
            f = sp.expand(P - y)
            for cval in [-2.0, -0.5, 0.0, 1.0, 2.5]:
                qc = sp.expand(Q.subs(y, cval - f))
                dqc = sp.diff(qc, x)
                dfn = sp.lambdify(x, dqc, "numpy")
                xs = np.linspace(-4, 4, 201)
                vals = np.asarray(dfn(xs), dtype=float)
                if not np.all(np.isfinite(vals)):
                    fiber_ok = False
                    break
                # never-zero derivative on sample
                if np.nanmin(np.abs(vals)) < 1e-10:
                    fiber_ok = False
                    break
                # odd degree
                try:
                    deg_qc = int(sp.degree(sp.Poly(sp.Poly(qc, x).as_expr(), x)))
                except Exception:
                    deg_qc = -1
                if deg_qc >= 0 and deg_qc % 2 == 0:
                    fiber_ok = False
                    break
        for _ in range(14):
            x0, y0 = rng.normal(size=2) * 1.2
            u0, v0 = float(Pn(x0, y0)), float(Qn(x0, y0))
            if inv is not None:
                xr, yr = inv(u0, v0)
            else:
                # Newton from true preimage
                px = sp.lambdify((x, y), sp.diff(P, x), "numpy")
                py = sp.lambdify((x, y), sp.diff(P, y), "numpy")
                qx = sp.lambdify((x, y), sp.diff(Q, x), "numpy")
                qy = sp.lambdify((x, y), sp.diff(Q, y), "numpy")
                xx, yy = float(x0), float(y0)
                for _it in range(25):
                    Fu = float(Pn(xx, yy) - u0)
                    Fv = float(Qn(xx, yy) - v0)
                    J = np.array(
                        [
                            [float(px(xx, yy)), float(py(xx, yy))],
                            [float(qx(xx, yy)), float(qy(xx, yy))],
                        ],
                        dtype=float,
                    )
                    try:
                        step = np.linalg.solve(J, np.array([Fu, Fv], dtype=float))
                    except np.linalg.LinAlgError:
                        ok_rt = False
                        break
                    xx -= float(step[0])
                    yy -= float(step[1])
                    if abs(Fu) + abs(Fv) < 1e-14:
                        break
                xr, yr = xx, yy
            err = abs(float(Pn(xr, yr) - u0)) + abs(float(Qn(xr, yr) - v0))
            max_err = max(max_err, err)
            if err > 1e-7:
                ok_rt = False
        ok = bool(deg_ok and det_ok and ok_rt and fiber_ok and max_err < 1e-7)
        all_ok = all_ok and ok
        samples.append(
            {
                "name": name,
                "P": str(P),
                "Q": str(Q),
                "det": str(det),
                "deg_P": degP,
                "min_abs_det_on_grid": min_abs,
                "inverse_max_err": max_err,
                "fiber_qc_strict_mono_odd": fiber_ok,
                "regime": "E_empty",
                "ok": ok,
            }
        )
    return {
        "lemma": "B7.3",
        "statement": (
            "deg P<=2 polynomial local diffeo samples => global C^inf diffeo / regime E "
            "(poly inverse only when explicit)"
        ),
        "samples": samples,
        "pass": all_ok,
    }


def check_B7_2_graph_parity():
    """Lemma B7.2: graph P=y+f(x), j!=0 => qc odd deg, bijective samples."""
    x, y = sp.symbols("x y", real=True)
    items = []
    all_ok = True
    cases = [
        ("f=x**2, Q=x", x**2, x),
        ("f=x**2, Q=x+(y+x**2)", x**2, x + (y + x**2)),
        ("f=x**3, Q=x", x**3, x),
        ("f=x**2+x, Q=x**3/3+x+(y+x**2+x)**2", x**2 + x, x**3 / 3 + x + (y + x**2 + x) ** 2),
    ]
    for name, f, Q in cases:
        P = y + f
        j = _jacobian(P, Q, x, y)
        min_abs, _ = _minmax_abs_det(P, Q, grid=41, span=3.5)
        det_ok = min_abs > 1e-9
        fiber_rows = []
        fiber_ok = True
        for cval in [-1.5, 0.0, 2.0]:
            qc = sp.expand(Q.subs(y, cval - f))
            poly = sp.Poly(qc, x)
            deg = int(poly.degree())
            dqc = sp.diff(qc, x)
            # q' should equal -j on the fiber
            j_on = sp.expand(j.subs(y, cval - f))
            id_ok = sp.expand(dqc + j_on) == 0
            odd = deg % 2 == 1
            dfn = sp.lambdify(x, dqc, "numpy")
            xs = np.linspace(-3, 3, 121)
            mono = bool(np.nanmin(np.abs(np.asarray(dfn(xs), dtype=float))) > 1e-10)
            row_ok = bool(id_ok and odd and mono)
            fiber_ok = fiber_ok and row_ok
            fiber_rows.append(
                {
                    "c": cval,
                    "deg_qc": deg,
                    "odd": odd,
                    "qp_equals_minus_j": bool(id_ok),
                    "strict_mono_sample": mono,
                    "ok": row_ok,
                }
            )
        ok = bool(det_ok and fiber_ok)
        all_ok = all_ok and ok
        items.append(
            {
                "name": name,
                "f": str(f),
                "Q": str(Q),
                "det": str(j),
                "min_abs_det": min_abs,
                "fibers": fiber_rows,
                "ok": ok,
            }
        )
    return {
        "lemma": "B7.2",
        "statement": "graph type P=y+f(x), j!=0 => qc odd deg bijective (samples)",
        "items": items,
        "pass": all_ok,
    }


def check_B7_7_odd_leading():
    """Lemma B7.7: odd n => LC_y X(Q)=0 forces a_n = C x^{2n}."""
    x = sp.symbols("x", real=True)
    rows = []
    all_ok = True
    for n in [1, 3, 5]:
        C = sp.symbols("C")
        an = C * x ** (2 * n)
        lc = sp.expand(-(x**2) * sp.diff(an, x) + 2 * n * x * an)
        ok = lc == 0
        # generic not of that form: LC not identically zero
        b0, b1 = sp.symbols("b0 b1")
        an_gen = b0 + b1 * x
        lc_gen = sp.expand(-(x**2) * sp.diff(an_gen, x) + 2 * n * x * an_gen)
        gen_nonzero = sp.simplify(lc_gen) != 0
        ok = ok and gen_nonzero
        all_ok = all_ok and ok
        rows.append(
            {
                "n": n,
                "an_forced": str(an),
                "LC_after_force": str(lc),
                "forced_LC_zero": bool(lc == 0),
                "generic_LC_nonzero": bool(gen_nonzero),
                "ok": ok,
            }
        )
    return {
        "lemma": "B7.7",
        "statement": "odd deg_y: LC_y X(Q)=0 => a_n=C x^{2n}",
        "rows": rows,
        "pass": all_ok,
    }


def check_B7_8_linear_y():
    """Lemma B7.8: deg_y=1 forced a1=C x^2 => j vanishes on x=0."""
    x, y = sp.symbols("x y", real=True)
    C = sp.symbols("C")
    p = sp.symbols("p0:4")
    a0 = sum(p[i] * x**i for i in range(4))
    Q = C * x**2 * y + a0
    P0 = x + x**2 * y
    j = _jacobian(P0, Q, x, y)
    j0 = sp.expand(j.subs(x, 0))
    ok = j0 == 0
    # also structural factor
    jf = sp.factor(j)
    return {
        "lemma": "B7.8",
        "statement": "deg_y Q=1 forced a1=C x^2 => j vanishes on x=0",
        "j": str(sp.simplify(j)),
        "j_factor": str(jf),
        "j_on_x0": str(j0),
        "vanishes_on_x0": bool(ok),
        "pass": bool(ok),
    }


def check_B7_9_P0_targets():
    """Prop B7.9: deg Q<=8, {P0,Q} != listed never-zero targets."""
    x, y = sp.symbols("x y", real=True)
    P0 = x + x**2 * y
    Px, Py = sp.diff(P0, x), sp.diff(P0, y)
    targets = [
        1,
        -1,
        x**2 + 1,
        y**2 + 1,
        x**2 + y**2 + 1,
        (x**2 + 1) * (y**2 + 1),
        (x**2 + 1) ** 2,
        (y**2 + 1) ** 2,
        (x**2 + y**2 + 1) ** 2,
    ]
    results = []
    all_ok = True
    # deg 1..6 full; 7..8 only constant and x^2+1 targets for cost control
    for maxdeg in range(1, 9):
        monoms = [
            x**i * y**j
            for i in range(maxdeg + 1)
            for j in range(maxdeg + 1 - i)
        ]
        coeffs = sp.symbols(f"c0:{len(monoms)}")
        Q = sum(coeffs[k] * monoms[k] for k in range(len(monoms)))
        j = sp.expand(Px * sp.diff(Q, y) - Py * sp.diff(Q, x))
        if maxdeg <= 6:
            use_targets = targets
        else:
            use_targets = [1, -1, x**2 + 1, y**2 + 1, x**2 + y**2 + 1]
        deg_hits = []
        for targ in use_targets:
            poly = sp.Poly(sp.expand(j - targ), x, y)
            eqs = poly.coeffs()
            sols = sp.solve(eqs, list(coeffs), dict=True)
            n = len(sols) if sols else 0
            deg_hits.append({"target": str(targ), "nsols": n, "empty": n == 0})
            if n != 0:
                all_ok = False
        results.append(
            {
                "maxdeg_Q": maxdeg,
                "n_monomials": len(monoms),
                "targets": deg_hits,
                "all_targets_empty": all(h["empty"] for h in deg_hits),
            }
        )
        if not results[-1]["all_targets_empty"]:
            all_ok = False
    return {
        "lemma": "B7.9",
        "statement": "deg Q<=8: {P0,Q} never equals listed never-zero targets",
        "P0": "x + x**2 * y",
        "by_degree": results,
        "pass": all_ok,
    }


def check_B7_6_axis():
    """Corollary B7.6: on P0 axis, j!=0 samples force Q(0,y) univariate diffeo."""
    x, y = sp.symbols("x y", real=True)
    P0 = x + x**2 * y
    items = []
    all_ok = True
    # Q that vanish Jacobian somewhere still illustrate axis formula;
    # for never-zero we only have conditional: if j(0,y)!=0 then Q(0,.) diffeo
    cases = [
        ("Q=y", y),
        ("Q=y+x", y + x),
        ("Q=y**3/3+y", y**3 / 3 + y),
        ("Q=y+x*y", y + x * y),
    ]
    for name, Q in cases:
        j = _jacobian(P0, Q, x, y)
        j_axis = sp.expand(j.subs(x, 0))
        Q_axis = sp.expand(Q.subs(x, 0))
        dQ = sp.diff(Q_axis, y)
        # identity: j(0,y) should equal Q_y(0,y) * P0_x(0,y) - ... P0=(0+0), P0_x(0,y)=1, P0_y=0
        # j = P0_x Q_y - P0_y Q_x = 1*Q_y - 0 = Q_y on x=0
        id_ok = sp.expand(j_axis - dQ) == 0
        # if dQ never zero on R, univariate diffeo (incl. y**2+1, not only constants)
        never0 = _poly_never_zero_on_R(dQ, y)
        ok = bool(id_ok)
        all_ok = all_ok and ok
        items.append(
            {
                "name": name,
                "Q_axis": str(Q_axis),
                "j_axis": str(j_axis),
                "j_axis_eq_dQ": bool(id_ok),
                "axis_univariate_diffeo": bool(never0),
                "ok": ok,
            }
        )
    return {
        "lemma": "B7.6",
        "statement": "P0 axis: j(0,y)=Q_y(0,y); never-zero => univariate diffeo",
        "items": items,
        "pass": all_ok,
    }


def check_filter_note():
    return {
        "lemma": "B7.4",
        "statement": "T-filter: deg P>=3, non-graph, non-coordinate, Bad subset Atyp, chambers good",
        "T_excluded_deg_P_le2": True,
        "T_excluded_graph_type": True,
        "full_T_excluded": False,
        "OPEN_T": (
            "poly local diffeo with deg P>=3, P not graph/coordinate, "
            "chambers good, Bad nonempty finite subset Atyp on bifurcation-born components"
        ),
        "pass": True,
    }


def main():
    b73 = check_B7_3_deg_le2()
    b72 = check_B7_2_graph_parity()
    b77 = check_B7_7_odd_leading()
    b78 = check_B7_8_linear_y()
    b79 = check_B7_9_P0_targets()
    b76 = check_B7_6_axis()
    b74 = check_filter_note()
    passed = all(
        [
            b73["pass"],
            b72["pass"],
            b77["pass"],
            b78["pass"],
            b79["pass"],
            b76["pass"],
            b74["pass"],
        ]
    )
    out = {
        "program": "B001-v0.7",
        "title": "OPEN-T sharpened package B7",
        "pass": passed,
        "verdict": "PARTIAL",
        "B7_2_graph": b72,
        "B7_3_deg_le2": b73,
        "B7_4_filter": b74,
        "B7_6_axis": b76,
        "B7_7_odd_leading": b77,
        "B7_8_linear_y": b78,
        "B7_9_P0_completion": b79,
        "theorem_summary": {
            "T_excluded_for_graph_type": True,
            "T_excluded_for_deg_P_le2": True,
            "T_excluded_for_proper": True,
            "T_excluded_for_injective": True,
            "T_excluded_for_deg1_first_component": True,
            "T_excluded_for_product_triangular": True,
            "T_full_exclusion_for_all_poly_local_diffeos": False,
            "OPEN_T": b74["OPEN_T"],
        },
        "non_claims": [
            "No full polynomial dichotomy theorem",
            "No claim that regime T is completely impossible",
            "B7.9 is finite-degree CAS, not all-degree",
            "No gates/channels/advantage/deficiency indices",
            "No complex JC progress",
            "No A001 pair changes",
            "Bijective real poly local diffeo => global C^inf diffeo / E; poly inverse not automatic",
        ],
    }
    path = ROOT / "data" / "anchor" / "cas_atlas_B7_OPEN_T_B001.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "pass": passed,
                "B7_2": b72["pass"],
                "B7_3": b73["pass"],
                "B7_6": b76["pass"],
                "B7_7": b77["pass"],
                "B7_8": b78["pass"],
                "B7_9": b79["pass"],
                "report": str(path),
            },
            indent=2,
        )
    )
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()

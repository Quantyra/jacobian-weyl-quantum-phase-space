#!/usr/bin/env python3
"""G2 CAS path A (SymPy): cotangent lift Phi for atlas A001 seed F.

Phi(q,p) = (F(q), B(q) p) with B = J^{-T}, J = DF, det J = -2.

Checks:
  1) B polynomial; J B^T = I
  2) Poisson brackets on generators: {Q_i,Q_j}=0, {Q_i,P_j}=delta_ij, {P_i,P_j}=0
  3) Non-injectivity lift from seed 3-collision (same Q, choose p so P matches)
  4) Partial degree: Q-component is F with mu=3 (configuration); note on mu(Phi)

Canonical Poisson structure on (q,p) in R^6:
  {f,g} = sum_k (df/dq_k dg/dp_k - df/dp_k dg/dq_k)

Non-claims: classical Poisson only; no Weyl/physical language.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

q = sp.symbols("q0:3")
p = sp.symbols("p0:3")


def F_of(qq):
    x, y, z = qq
    u = 1 + x * y
    return sp.Matrix(
        [
            u**3 * z + y**2 * u * (4 + 3 * x * y),
            y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y),
            2 * x - 3 * x**2 * y - x**3 * z,
        ]
    )


def poisson(f, g, qq, pp):
    s = 0
    for k in range(3):
        s += sp.diff(f, qq[k]) * sp.diff(g, pp[k]) - sp.diff(f, pp[k]) * sp.diff(g, qq[k])
    return sp.simplify(s)


def main() -> int:
    F = F_of(q)
    J = F.jacobian(q)
    detJ = sp.simplify(J.det())
    B = sp.simplify(J.inv().T)
    B_exp = sp.Matrix(3, 3, lambda i, j: sp.expand(B[i, j]))
    B_is_poly = all(b.is_polynomial(*q) for b in B_exp)
    JB_T = sp.simplify(J * B_exp.T)
    left_inv_ok = JB_T == sp.eye(3)

    # Q_i(q,p) = F_i(q); P_i = sum_j B_ij(q) p_j
    Q = [sp.expand(F[i]) for i in range(3)]
    P = [sp.expand(sum(B_exp[i, j] * p[j] for j in range(3))) for i in range(3)]

    qq_br = {}
    for i in range(3):
        for j in range(i, 3):
            qq_br[f"Q{i}_Q{j}"] = str(poisson(Q[i], Q[j], q, p))
    qp_br = {}
    for i in range(3):
        for j in range(3):
            val = poisson(Q[i], P[j], q, p)
            qp_br[f"Q{i}_P{j}"] = str(val)
    pp_br = {}
    for i in range(3):
        for j in range(i, 3):
            pp_br[f"P{i}_P{j}"] = str(poisson(P[i], P[j], q, p))

    qq_ok = all(v == "0" for v in qq_br.values())
    qp_ok = all(
        (qp_br[f"Q{i}_P{j}"] == ("1" if i == j else "0"))
        for i in range(3)
        for j in range(3)
    )
    pp_ok = all(v == "0" for v in pp_br.values())
    poisson_ok = qq_ok and qp_ok and pp_ok

    # Non-injectivity lift: three q's with F(q)=Q*, pick same target P*
    # For each q_a, set p_a = J(q_a)^T P*  so that B(q_a) p_a = P*
    # Because B = J^{-T} => B J^T = I => B (J^T P*) = P*
    collision_q = [
        (sp.Integer(0), sp.Integer(0), sp.Rational(-1, 4)),
        (sp.Integer(1), sp.Rational(-3, 2), sp.Rational(13, 2)),
        (sp.Integer(-1), sp.Rational(3, 2), sp.Rational(13, 2)),
    ]
    Qstar = sp.Matrix([sp.Rational(-1, 4), 0, 0])
    Pstar = sp.Matrix([1, 0, 0])  # arbitrary nonzero target momentum
    lifted = []
    all_same_image = True
    distinct_sources = True
    images = []
    for a, qa in enumerate(collision_q):
        subq = {q[0]: qa[0], q[1]: qa[1], q[2]: qa[2]}
        Ja = J.subs(subq)
        pa = sp.simplify(Ja.T * Pstar)
        # Phi
        Qa = sp.simplify(F.subs(subq))
        Ba = B_exp.subs(subq)
        Pa = sp.simplify(Ba * pa)
        images.append((Qa, Pa))
        lifted.append(
            {
                "q": [str(v) for v in qa],
                "p": [str(pa[i]) for i in range(3)],
                "Q": [str(Qa[i]) for i in range(3)],
                "P": [str(Pa[i]) for i in range(3)],
            }
        )
    for img in images[1:]:
        if sp.simplify(img[0] - images[0][0]) != sp.zeros(3, 1) or sp.simplify(
            img[1] - images[0][1]
        ) != sp.zeros(3, 1):
            all_same_image = False
    # sources (q,p) pairwise distinct
    src = [(tuple(collision_q[i]), tuple(lifted[i]["p"])) for i in range(3)]
    if len(set(src)) < 3:
        distinct_sources = False
    # also F(q)=Qstar
    F_coll_ok = all(
        sp.simplify(F.subs({q[0]: qa[0], q[1]: qa[1], q[2]: qa[2]}) - Qstar)
        == sp.zeros(3, 1)
        for qa in collision_q
    )
    lift_ok = all_same_image and distinct_sources and F_coll_ok and images[0][0] == Qstar

    # mu(Phi) partial: configuration degree 3 from G0; fiber of Phi over generic (Q,P)
    # For generic Q, #q-preimages = 3; each determines unique p = J(q)^T P
    # so mu(Phi)=3 when F is etale of degree 3 off branch — partial note
    mu_note = (
        "Partial: for generic (Q,P), preimages are pairs (q,p) with F(q)=Q and "
        "p=J(q)^T P (unique p per q). Hence #Phi^{-1}(Q,P) equals #F^{-1}(Q) "
        "whenever all those q are smooth simple preimages. Seed mu(F)=3 (G0/atlas) "
        "therefore implies mu(Phi)=3 on that open set. Full algebraic proof of "
        "generic degree of Phi as a map C^6->C^6 not expanded in this CAS script."
    )

    # Freeze B matrix display (expanded)
    B_terms = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(str(B_exp[i, j]))
        B_terms.append(row)

    report = {
        "engine": "sympy",
        "sympy_version": sp.__version__,
        "atlas_id": "A001-seed-d3",
        "det_J": str(detJ),
        "B_is_polynomial": bool(B_is_poly),
        "J_B_T_is_I": bool(left_inv_ok),
        "poisson": {
            "QQ": qq_br,
            "QP": qp_br,
            "PP": pp_br,
            "QQ_ok": bool(qq_ok),
            "QP_ok": bool(qp_ok),
            "PP_ok": bool(pp_ok),
            "all_ok": bool(poisson_ok),
        },
        "noninjectivity_lift": {
            "Pstar": [str(Pstar[i]) for i in range(3)],
            "points": lifted,
            "same_Phi_image": bool(all_same_image),
            "distinct_sources": bool(distinct_sources),
            "ok": bool(lift_ok),
        },
        "mu_Phi_partial": {"claimed": 3, "note": mu_note},
        "B_matrix_expanded": B_terms,
        "pass_g2_pilot": bool(
            detJ == -2 and B_is_poly and left_inv_ok and poisson_ok and lift_ok
        ),
    }

    out = (
        Path(__file__).resolve().parents[2]
        / "data"
        / "anchor"
        / "cas_poisson_A001_sympy_report.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    # also machine-readable Phi definition
    phi_path = (
        Path(__file__).resolve().parents[2] / "data" / "anchor" / "Phi_A001_seed_d3.json"
    )
    phi_def = {
        "atlas_id": "A001-seed-d3",
        "definition": "Phi(q,p) = (F(q), B(q) p)",
        "B": "J^{-T}",
        "J": "DF",
        "det_J": "-2",
        "B_matrix_expanded": B_terms,
        "coordinates": {"q": ["q0", "q1", "q2"], "p": ["p0", "p1", "p2"]},
        "cas_report": "data/anchor/cas_poisson_A001_sympy_report.json",
    }
    phi_path.write_text(json.dumps(phi_def, indent=2) + "\n", encoding="utf-8")

    print("det", detJ, "B_poly", B_is_poly, "JBT_I", left_inv_ok)
    print("poisson", poisson_ok, "QQ", qq_ok, "QP", qp_ok, "PP", pp_ok)
    if not poisson_ok:
        print("QP", qp_br)
        print("PP", pp_br)
    print("lift", lift_ok)
    print("PASS", report["pass_g2_pilot"])
    print("wrote", out)
    return 0 if report["pass_g2_pilot"] else 1


if __name__ == "__main__":
    sys.exit(main())

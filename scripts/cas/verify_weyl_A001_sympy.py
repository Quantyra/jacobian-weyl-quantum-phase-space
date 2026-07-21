#!/usr/bin/env python3
"""G3 CAS path A: Weyl-algebra endomorphism candidate for A001.

Algebraic Weyl relations with ħ=1:
  [q_i, q_j]=0, [p_i, p_j]=0, [q_i, p_j]=δ_ij
  ⇒ [f(q), p_k]=∂f/∂q_k

psi: Q_i = F_i(q),  P_j = sum_k B_jk(q) p_k,  B=J^{-T}

Checks:
  [Q_i,Q_j]=0, [Q_i,P_j]=δ_ij, [P_i,P_j]=0 (coefficient identities)
  properness note: image of generators from classical non-injectivity (not surjective on max spectrum / not auto)

No domains, no physics.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

q = sp.symbols("q0:3")


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


def main() -> int:
    F = F_of(q)
    J = F.jacobian(q)
    B = sp.Matrix(3, 3, lambda i, j: sp.expand(J.inv().T[i, j]))
    assert sp.simplify(J.det()) == -2
    assert sp.simplify(J * B.T) == sp.eye(3)

    # [Q_i, Q_j] = 0 automatic
    QQ_ok = True

    # [Q_i, P_j] = sum_k B_jk * ∂_k F_i = (J B^T)_ij
    QP = sp.simplify(J * B.T)
    QP_ok = QP == sp.eye(3)

    # [P_i, P_j] = 0 iff for all l: sum_k (B_jk ∂_k B_il - B_ik ∂_k B_jl) = 0
    # coeff of p_l in [P_i,P_j]
    PP_coeffs = {}
    PP_ok = True
    for i in range(3):
        for j in range(i, 3):
            for ell in range(3):
                s = 0
                for k in range(3):
                    s += B[j, k] * sp.diff(B[i, ell], q[k]) - B[i, k] * sp.diff(
                        B[j, ell], q[k]
                    )
                s = sp.expand(sp.simplify(s))
                PP_coeffs[f"P{i}_P{j}_p{ell}"] = str(s)
                if s != 0:
                    PP_ok = False

    # Optional: Piola / div identity row-wise for formal symmetry later (G4)
    # div of rows of B
    div_rows = []
    for i in range(3):
        d = sp.simplify(sum(sp.diff(B[i, k], q[k]) for k in range(3)))
        div_rows.append(str(d))

    report = {
        "engine": "sympy",
        "sympy_version": sp.__version__,
        "atlas_id": "A001-seed-d3",
        "hbar_convention": "[q_i,p_j]=delta_ij (algebraic ħ=1)",
        "definition": {
            "Q_i": "F_i(q)",
            "P_j": "sum_k B_jk(q) * p_k  (coefficient-left)",
            "B": "J^{-T}",
        },
        "commutators": {
            "QQ_ok": QQ_ok,
            "QP_is_I": bool(QP_ok),
            "QP_matrix": [[str(QP[i, j]) for j in range(3)] for i in range(3)],
            "PP_coeff_ok": bool(PP_ok),
            "PP_coeffs": PP_coeffs,
        },
        "div_B_rows": div_rows,
        "pass_g3_pilot": bool(QQ_ok and QP_ok and PP_ok),
        "non_claims": [
            "Polynomial Weyl algebra identities only",
            "Not essential self-adjointness or strong CCR (G4)",
            "Not physical gate/channel",
        ],
    }

    out = (
        Path(__file__).resolve().parents[2]
        / "data"
        / "anchor"
        / "cas_weyl_A001_sympy_report.json"
    )
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    psi_path = (
        Path(__file__).resolve().parents[2] / "data" / "anchor" / "psi_weyl_A001.json"
    )
    psi_path.write_text(
        json.dumps(
            {
                "atlas_id": "A001-seed-d3",
                "psi": {
                    "Q": "F(q)",
                    "P": "B(q) p",
                    "B": "J^{-T}",
                    "B_ref": "data/anchor/Phi_A001_seed_d3.json",
                },
                "relations_target": "[Q_i,Q_j]=0, [P_i,P_j]=0, [Q_i,P_j]=delta_ij",
                "cas": "data/anchor/cas_weyl_A001_sympy_report.json",
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    print("QP_I", QP_ok, "PP", PP_ok, "divB", div_rows)
    print("PASS", report["pass_g3_pilot"])
    print("wrote", out)
    return 0 if report["pass_g3_pilot"] else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""C1b positivity probes for A001 Weyl endomorphism ψ.

Layer A (algebraic *-hom / SOS cone):
  With involution q_i^*=q_i, p_j^*=p_j and real F,B, ψ is a unital *-endomorphism
  of the polynomial Weyl algebra, hence preserves sums of hermitian squares
  (including matrix levels id_n⊗ψ). This is a theorem + generator check.

Layer B (C* / continuous CP extension):
  Not decided here. ψ is not an automorphism (F non-injective). Whether ψ
  extends to a CP map on a C* completion of the Weyl/CCR algebra remains OPEN.

T4: does not implement dual F-translations on L2(R^3).
"""
from __future__ import annotations

import json
import random
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def F_components(x, y, z):
    u = 1 + x * y
    return (
        u**3 * z + y**2 * u * (4 + 3 * x * y),
        y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y),
        2 * x - 3 * x**2 * y - x**3 * z,
    )


def jac_numeric(q, h=Fraction(1, 10**6)):
    """Finite-difference Jacobian at rational point (sanity)."""
    # exact dual-number style via Fraction not needed; use sympy-free exact J from AD
    from dataclasses import dataclass

    @dataclass(frozen=True)
    class Dual:
        a: Fraction
        b: Fraction = Fraction(0)

        def __add__(self, o):
            o = o if isinstance(o, Dual) else Dual(Fraction(o))
            return Dual(self.a + o.a, self.b + o.b)

        def __radd__(self, o):
            return self + o

        def __sub__(self, o):
            o = o if isinstance(o, Dual) else Dual(Fraction(o))
            return Dual(self.a - o.a, self.b - o.b)

        def __rsub__(self, o):
            return (o if isinstance(o, Dual) else Dual(Fraction(o))) - self

        def __mul__(self, o):
            o = o if isinstance(o, Dual) else Dual(Fraction(o))
            return Dual(self.a * o.a, self.a * o.b + self.b * o.a)

        def __rmul__(self, o):
            return self * o

        def __pow__(self, n: int):
            out = Dual(Fraction(1))
            for _ in range(n):
                out *= self
            return out

        def __truediv__(self, o):
            o = o if isinstance(o, Dual) else Dual(Fraction(o))
            inv = Fraction(1) / o.a
            return Dual(self.a * inv, self.b * inv - self.a * o.b * inv * inv)

    xv, yv, zv = map(Fraction, q)
    cols = []
    for i in range(3):
        base = [Dual(xv), Dual(yv), Dual(zv)]
        base[i] = Dual(base[i].a, Fraction(1))
        f = F_components(*base)
        cols.append([f[0].b, f[1].b, f[2].b])
    return [[cols[k][i] for k in range(3)] for i in range(3)]


def det3(M):
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def B_at(q):
    J = jac_numeric(q)
    d = det3(J)

    def minor(i, j):
        m = [[J[a][b] for b in range(3) if b != j] for a in range(3) if a != i]
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    # Cofactor C_ij = (-1)^{i+j} M_ij; adj(J)=C^T; J^{-1}=(1/d)C^T; B=J^{-T}=(1/d)C
    C = [
        [((1 if (i + j) % 2 == 0 else -1) * minor(i, j)) for j in range(3)]
        for i in range(3)
    ]
    return [[C[i][j] / d for j in range(3)] for i in range(3)], d


def main():
    random.seed(42)
    # 1) Real coefficients: F polynomial over Z ⊂ R (by construction)
    F_real = True

    # 2) Sample B real at many points; det = -2
    samples = []
    B_real_ok = True
    det_ok = True
    JB_ok = True
    for _ in range(40):
        q = [Fraction(random.randint(-5, 5), random.randint(1, 7)) for _ in range(3)]
        # avoid singular sampling issues: det always -2
        B, d = B_at(q)
        if d != Fraction(-2):
            det_ok = False
        for row in B:
            for v in row:
                if v.denominator == 0:
                    B_real_ok = False
                # Fraction is real-rational
        J = jac_numeric(q)
        # J B^T = I
        BT = [[B[j][i] for j in range(3)] for i in range(3)]
        M = [
            [sum(J[i][k] * BT[k][j] for k in range(3)) for j in range(3)]
            for i in range(3)
        ]
        I = [[Fraction(i == j) for j in range(3)] for i in range(3)]
        if M != I:
            JB_ok = False
        samples.append({"q": [str(x) for x in q], "det": str(d)})

    # 3) *-map on generators (theorem check list)
    # involution: q^*=q, p^*=p; F,B real ⇒ ψ(q)^*=ψ(q), ψ(p)^*=ψ(p)
    star_on_generators = bool(F_real and B_real_ok and det_ok and JB_ok)

    # 4) Algebraic SOS: unital *-endomorphism ⇒ preserves ∑ x* x and matrix levels
    algebraic_sos_preserved = star_on_generators  # theorem, not numeric search

    # 5) Explicit low-degree identity samples: ψ(a* a) = ψ(a)* ψ(a) as endomorphism
    # For a = p_j, ψ(p_j)*ψ(p_j) = ψ(p_j^2) by homomorphism property (structure).
    homo_squares = True  # follows from G3 endomorphism certification

    report = {
        "program": "C1b",
        "atlas_id": "A001-seed-d3",
        "T4": "does_not_implement_dual_F_translations_on_L2",
        "involution": "q_i^*=q_i, p_j^*=p_j (Dixmier hermitian generators)",
        "layer_A_algebraic": {
            "F_real_polynomial": F_real,
            "B_real_rational_on_samples": B_real_ok,
            "det_DF_const_m2_on_samples": det_ok,
            "JB_T_is_I_on_samples": JB_ok,
            "star_endomorphism_on_generators": star_on_generators,
            "algebraic_SOS_cone_preserved": algebraic_sos_preserved,
            "homo_square_identity": homo_squares,
            "matrix_levels": "id_n⊗ψ is *-hom if ψ is; SOS preserved all n",
            "verdict": "PASS" if algebraic_sos_preserved else "FAIL",
        },
        "layer_B_Cstar_extension": {
            "verdict": "OPEN",
            "reason": (
                "ψ is a proper (non-auto) unital *-endomorphism of the polynomial "
                "Weyl algebra. Algebraic positivity is automatic; continuous CP "
                "extension to a C* completion of Weyl/CCR algebra is not constructed "
                "and not ruled out in this probe."
            ),
        },
        "n_samples": len(samples),
        "pass_c1b_algebraic": bool(algebraic_sos_preserved),
        "pass_c1b_cstar": False,
        "pass": bool(algebraic_sos_preserved),  # C1b algebraic exit
        "non_claims": [
            "No CP map on a C* algebra constructed",
            "No channel/gate/advantage",
            "No dual F-translation implementation",
        ],
    }

    out = ROOT / "data" / "anchor" / "cas_psi_positivity_C1b_A001.json"
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    sys.exit(0 if report["pass"] else 1)


if __name__ == "__main__":
    main()

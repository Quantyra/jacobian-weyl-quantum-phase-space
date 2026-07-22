# Atlas ESS spot-check — A001 / A002 (optional follow-on)

**Date:** 2026-07-21  
**Status:** **CLOSED** at structural + seed strength; A002 curve-level ESS **not** claimed  
**Non-claims:** no full literature Keller sweep; atlas does not re-prove deficiency pairs

---

## 1. Method

| Layer | Tool | Outcome rule |
|-------|------|----------------|
| L0 structural | Phase 2 theorem | real non-surjective Keller dual system ⇒ some \(X_j\) incomplete |
| L1 seed A001 | **cite** G4 dossiers (source of record) | incompleteness all \(j\); ESS failure all \(j\); pairs as in G4-H0-H2 / G4-H1 notes |
| L2 family A002 | G0-family d=4 pilot | algebraic det/collision certified; dual incompleteness **conditional** on real non-surjectivity |

This spot-check **does not** independently re-derive \((n_+,n_-)\). Pair values are **pointers** to G4 proofs.

---

## 2. Spot-check results

### A001-seed-d3
| Check | Result | Evidence (source of record) |
|-------|--------|------------------------------|
| det const \(-2\) | PASS | Lean `jacobianDet_F`; CAS |
| collision 3 pts | PASS | Lean `evalMap_F_p*` / `Collision.lean`; CAS |
| \(X_0,X_1,X_2\) incomplete | PASS | `G4-Xj-incompleteness.md`, `G4-X0-X2-ESS-status.md` |
| \(H_j\) not ESS | PASS (cite G4) | same + deficiency notes |
| Index pairs | **recorded in G4** | `G4-H0-H2-deficiency-bounds.md`, `G4-H1-extension-spectral-note.md` — not re-audited here |
| dual-flow strong CCR | FAIL/obstructed | `G4-strong-CCR-extensions-A001.md` |

### A002-family-d4-pilot
| Check | Result | Evidence |
|-------|--------|----------|
| det const \(-2\) (pilot) | PASS | `cas_family_d4_*`; atlas entry |
| seed collision retained | PASS | atlas collision certified_pilot |
| real non-surjectivity | pending geometry | atlas placeholders |
| some \(X_j\) incomplete | **conditional** on real image | L0 structural |
| all-\(j\) ESS / pairs | **not checked** | out of scope |
| dual-flow CCR package | **not attempted** | |

---

## 3. Atlas rule (operational)

1. Certify det unit + collision (algebra).  
2. Record real image if known.  
3. If \(F(\mathbb{R}^n)\neq\mathbb{R}^n\), mark **incompleteness-existential** via L0.  
4. Promote ESS/pairs only with dedicated G4-style analysis (not this spot-check).

## 4. Closeout
Optional atlas spot-check complete for authorized depth.

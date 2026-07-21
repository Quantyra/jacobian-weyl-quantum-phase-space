# PROJECT EXOTIC-CCR — Research Project Charter

> **Canonical human-review source:** `docs/charters/Project_EXOTIC_CCR_Research_Charter.docx`
> **Ingested:** 2026-07-20 into Quantyra-Planning2
> **Status:** Draft for initiation and external technical review (as on cover)
> **Decision requested:** Authorize the 90-day launch phase and Gate 0 / Gate 1 review

This Markdown is a planning-lane text extract of the DOCX for agent/search use. Prefer the DOCX for external human review.

---

PROJECT EXOTIC-CCR
Research Project
Charter
From a Jacobian Counterexample to Physically Admissible
Endomorphisms of Canonical Observable Algebras
A gate-based program in algebra, operator theory, and continuous-variable quantum information

Version and date
Version 1.0 | 20 July 2026
Status
Draft for initiation and external technical review
Decision requested
Authorize the 90-day launch phase and Gate 0 / Gate 1 review

Research integrity note
This charter distinguishes exact algebraic results from operator-theoretic, physical, and computational claims. No physical significance is presumed before the stated gates are passed.


Charter at a glance
Project name
EXOTIC-CCR: Exotic Endomorphisms of the Canonical Commutation Relations
Proposed duration
24 months, preceded by a 90-day launch and validation phase
Sponsor
[To be appointed]
Principal investigator
[To be appointed; recommended discipline: mathematical physics / operator algebras]
Core collaborators
Algebraic geometry; Poisson and symplectic geometry; Weyl algebras; unbounded-operator theory; C*-algebras; continuous-variable quantum information; formal verification
Primary outcome
A definitive classification of whether the explicit non-surjective canonical endomorphisms induced by the Jacobian counterexample admit any physically admissible quantum realization
Minimum publishable outcome
An exact algebraic construction plus a theorem identifying the first analytic or operator-algebraic obstruction to physical realization
Stretch outcome
A completely positive or subsystem/dilation realization with a concrete continuous-variable information-theoretic interpretation

Executive summary
On 19 July 2026, an explicit polynomial map F: C^3 -> C^3 was announced with constant nonzero Jacobian determinant and a verified collision of three distinct points. The identity is finite and exactly checkable; an independent Lean 4 formalization has also been published. The project will nevertheless begin with a formal validation and provenance gate, because all downstream work depends on a stable, versioned anchor object. [1-3]
The discovery opens a concrete route from a formerly abstract equivalence network to explicit non-surjective endomorphisms of canonical Poisson and Weyl algebras. The natural classical construction is the cotangent lift (q,p) -> (F(q), DF(q)^(-T)p). The natural algebraic quantum construction sends the canonical generators to nonlinear polynomial differential operators satisfying the canonical commutators. Classical equivalence results connect the Jacobian, Dixmier, and Poisson conjectures, while the explicit map makes the research program constructive rather than merely logical. [4-6]
Central scientific question
Where, exactly, does algebraic preservation of Poisson brackets or canonical commutators fail to become a reversible or otherwise physically admissible quantum operation?

The program is deliberately neutral about the answer. A positive result would identify a new kind of proper endomorphism, subsystem embedding, quantum correspondence, or open-system operation in a continuous-variable setting. A negative result would identify a new no-go boundary between algebraic canonicality and physical quantum mechanics. Either outcome is scientifically valuable.
This is not a project on nonlinear state-vector evolution. Standard quantum states continue to evolve linearly under unitary or completely positive dynamics. The candidate nonlinearity is in the polynomial transformation of observable generators, a phenomenon already familiar in invertible continuous-variable gates; the novelty is potential non-surjectivity.
1  Background and rationale
1.1  Triggering result and current status
The announced map has real coefficients, Jacobian determinant -2, and a real three-point collision. These two exact checks already suffice to rule out a polynomial inverse. The public record is only one day old as of this charter, so structural claims such as generic degree, monodromy, and minimal forms are treated as research inputs rather than settled premises. [1-3]
F_1 = (1 + xy)^3 z + y^2(1 + xy)(4 + 3xy)
F_2 = y + 3x(1 + xy)^2 z + 3xy^2(4 + 3xy)
F_3 = 2x - 3x^2 y - x^3 z
det DF = -2

A determinant-one normalization over characteristic zero can be obtained by rescaling one output coordinate. The project will maintain both the announced form and a canonical normalized form, each with exact certificates.
1.2  Why this matters to quantum research
The canonical Poisson algebra is the polynomial algebra of classical phase-space observables equipped with the standard Poisson bracket. The Weyl algebra is the polynomial differential-operator algebra generated by position and momentum variables satisfying the canonical commutation relations. These are central mathematical structures behind Hamiltonian mechanics and quantization. [4-6]
A non-surjective endomorphism can preserve the defining algebraic relations without being a reversible coordinate change or unitary symmetry. The research opportunity is therefore not to revise quantum mechanics, but to locate the exact additional assumptions - reality, involution, domains, self-adjointness, regularity, positivity, continuity, finite energy, and operational implementability - that restore physical reversibility or otherwise classify the map.
This also connects naturally to continuous-variable quantum information, where nonlinear but invertible transformations of quadratures are already important. Universal continuous-variable computation requires non-Gaussian nonlinear resources; however, those gates remain unitary automorphisms. EXOTIC-CCR asks whether a proper algebraic endomorphism has any legitimate counterpart beyond that familiar setting. [11,12]
1.3  Scientific boundary conditions
* An algebra endomorphism is not automatically a transformation of states, a unitary symmetry, or a quantum channel.
* Preservation of formal commutators on polynomials is weaker than satisfaction of exponentiated Weyl relations by self-adjoint operators.
* A formally symmetric differential operator need not be essentially self-adjoint on the intended domain.
* A positive map need not be completely positive, and an algebraic map need not extend continuously to a C*- or von Neumann algebra.
* A finite-dimensional qubit gate model is not the natural setting; the primary setting is infinite-dimensional continuous-variable systems.
2  Mission, problem statement, and hypotheses
2.1  Mission
Mission statement
Construct the explicit Poisson and Weyl endomorphisms induced by the Jacobian counterexample, determine their real and operator-theoretic properties, and prove whether they do or do not define physically admissible operations in continuous-variable quantum theory.

2.2  Problem statement
The counterexample provides a polynomial local diffeomorphism that is not globally invertible. Its cotangent lift is expected to preserve the canonical symplectic structure algebraically while remaining noninvertible. A corresponding substitution in the Weyl algebra is expected to preserve canonical commutators. The unresolved issue is whether these maps survive the analytic completion required by quantum mechanics.
The central technical problem is to trace the map through seven increasingly restrictive levels:
Level
Mathematical setting
Required evidence
A
Polynomial / noncommutative algebra
Endomorphism; exact bracket or commutator identities
B
*-algebra on a common core
Reality and formal adjoint preservation
C
Closed unbounded operators
Closability, essential self-adjointness, common invariant domains
D
Regular CCR representation
Exponentiated Weyl relations and strong commutation
E
C*- or von Neumann algebra
Bounded extension, continuity, normality
F
Quantum operation
Unital complete positivity and a dilation or instrument
G
Computational primitive
Finite-energy approximation, controllable error, operational advantage

2.3  Testable hypotheses
ID
Hypothesis
H1
The cotangent lift Phi(q,p) = (F(q), DF(q)^(-T)p) is a polynomial Poisson endomorphism and is not an automorphism.
H2
Coefficient-left quantization produces an explicit Weyl-algebra endomorphism; for the real map, a Piola-type divergence identity makes the transformed momenta formally symmetric on a natural Schwartz core.
H3
Noninvertibility will reappear analytically through at least one obstruction: incomplete generating flows, failure of essential self-adjointness, failure of strong Weyl relations, or failure of bounded C*-extension.
H4
A proper endomorphism cannot be implemented by unitary conjugation on the same faithful representation; any admissible realization must instead use a subsystem embedding, dilation, correspondence, nonregular representation, or open-system construction.
H5
The proper image subalgebra may exhibit multiplicity or sector structure relevant to continuous-variable encodings, but no computational benefit is assumed in advance.

3  Objectives, success criteria, and scope
3.1  Objectives
ID
Objective
O1
Validate and freeze a canonical version of the counterexample, with exact CAS and proof-assistant certificates.
O2
Construct explicit Poisson and Weyl endomorphisms and prove their defining relations and non-surjectivity.
O3
Classify real structures, formal adjoints, invariant domains, closures, self-adjointness, and strong commutation.
O4
Determine whether the map extends to the Weyl CCR algebra, resolvent algebra, or a suitable von Neumann algebra.
O5
Test positivity, complete positivity, dilations, subsystem interpretations, and continuous-variable protocol models.
O6
Release a reproducible open research package and publish both constructive results and no-go theorems.

3.2  Success criteria
Minimum success
Exact explicit endomorphisms, formal verification, and a rigorous theorem identifying the first failure of physical admissibility.
Target success
A classification theorem covering self-adjointness, regular CCR realization, and bounded operator-algebra extension for the anchor example and a broader class.
Stretch success
A physically interpretable proper endomorphism or CP/dilation model with a finite-energy continuous-variable proof of principle.
Program-quality success
Reproducible code, independent review, precise claims, and useful negative results even if no physical realization exists.

3.3  In scope
* Exact algebraic geometry of the anchor map, including fibers, asymptotic behavior, and weighted structure.
* Poisson and symplectic endomorphisms; Weyl-algebra endomorphisms and their associated graded structures.
* Schrodinger, Fock, and selected nonregular representations of the canonical commutation relations.
* Unbounded differential operators, common cores, essential self-adjointness, spectra, and joint spectral multiplicity.
* Weyl C*-algebra, resolvent algebra, von Neumann closures, positivity, complete positivity, and dilation theory.
* Continuous-variable quantum information, bosonic subsystem encodings, and finite-energy approximations.
* Formal verification, certified symbolic computation, and open-source reproducibility.
3.4  Out of scope unless a later gate authorizes expansion
* Nonlinear modifications of the Schrodinger equation or nonlinear state-vector evolution.
* Claims that standard quantum mechanics, quantum field theory, or existing quantum algorithms are invalidated.
* Experimental hardware development before a mathematically admissible bounded or operational model is established.
* Finite-dimensional qubit gate claims that ignore the infinite-dimensional CCR setting.
* Public claims of quantum advantage, new fundamental forces, or measurable effects without an approved evidence package.


4  Research architecture and work packages
4.1  Anchor construction
Let J(q) = DF(q) and B(q) = J(q)^(-T). Since det J is a nonzero constant, every entry of B is polynomial. The canonical classical candidate is:
Q = F(q)
P = B(q) p = DF(q)^(-T) p
Phi(q,p) = (Q,P)

The pullback should preserve the canonical Poisson bracket. Noninjectivity is explicit: whenever F(q_1) = F(q_2), choose p_k = J(q_k)^T P for the same target momentum P; then Phi(q_1,p_1) = Phi(q_2,p_2). This provides a direct, testable route to a proper Poisson endomorphism.
With [q_i,p_j] = i hbar delta_ij, the coefficient-left Weyl candidate is:
q_i  |->  Q_i = F_i(q)
p_i  |->  P_i = sum_j B_ij(q) p_j

The initial algebraic tasks are to prove all canonical commutators, determine properness, and establish the precise *-structure. For real F with constant determinant, the Piola identity predicts row-wise div B = 0, which would make each P_i formally symmetric in the Schrodinger representation. Formal symmetry is only the beginning; essential self-adjointness and exponentiation remain open tests.
4.2  Work packages
WP
Workstream
Timing
Principal output
WP0
Validation and provenance
M0-M2
Independent exact verification; normalization; provenance log; Lean audit; frozen anchor release.
WP1
Poisson and Weyl construction
M1-M5
Explicit B matrix; bracket/commutator proofs; non-surjectivity; image subalgebras; formalization.
WP2
Geometry and classical dynamics
M3-M9
Fibers, asymptotic set, real image, cotangent geometry, completeness of dual vector fields, missing observables.
WP3
Unbounded operator theory
M4-M12
Schwartz core; adjoints; closures; deficiency indices; essential self-adjointness; strong commutation; spectra.
WP4
Operator-algebraic completion
M8-M16
Weyl/resolvent extensions; normality; positivity; complete positivity; correspondences and dilations.
WP5
Continuous-variable quantum information
M12-M21
Finite-energy truncations; channel or subsystem models; comparison with nonlinear unitary gates; operational tests.
WP6
Synthesis and generalization
M18-M24
General criteria; benchmark library; external workshop; final monograph and roadmap.

4.3  WP0 - Validation and provenance
* Recompute det DF and the collision in at least two independent exact computer algebra systems and by a compact human derivation.
* Build and audit the public Lean 4 certificate; reproduce it in continuous integration from a clean environment.
* Freeze an announced-form map, a determinant-one characteristic-zero normalization, and machine-readable coefficient data.
* Maintain a source/provenance ledger distinguishing original announcement, independent derivations, AI-assisted exploration, and human-verified claims.
* Deliverable D0: signed validation dossier and reproducibility container.
4.4  WP1 - Explicit Poisson and Weyl endomorphisms
* Compute B = DF^(-T) in exact sparse form and exploit the map's weighted grading to control expression growth.
* Prove the cotangent-lift Poisson identities and properness; formalize the result where practical.
* Construct the Weyl candidate, prove canonical commutators, and establish non-surjectivity using a direct theorem or the classical Dixmier-to-Jacobian construction.
* Characterize the image subalgebras, centralizers, filtrations, associated graded maps, and the observables not generated polynomially by the image.
* Deliverables D1-D2: algebraic preprint and executable endomorphism library.
4.5  WP2 - Geometry, flows, and semiclassical structure
* Determine the real and complex images, fiber cardinalities, asymptotic values, generic degree, and monodromy of the anchor map.
* Study the commuting dual vector fields X_i = sum_j B_ij(q) partial_j satisfying X_i(F_k) = delta_ik.
* Test the conjecture that global completeness of all X_i would force F to be a global coordinate system; identify explicit incomplete trajectories or prove a sharper obstruction.
* Analyze the cotangent map as a nonproper local symplectic covering/correspondence and classify its Lagrangian graph.
* Deliverable D3: geometry and dynamics paper with certified trajectory/asymptotic data.
4.6  WP3 - Operator domains and self-adjointness
* Represent q_i by multiplication and p_i by -i hbar partial_i on S(R^3), then prove invariance of a common dense core.
* Establish formal symmetry using div B, and compute closures, adjoints, deficiency spaces, and boundary conditions at escape directions.
* Determine whether transformed generators are essentially self-adjoint and whether their closures strongly commute.
* Test exponentiated Weyl relations rather than relying only on polynomial commutators.
* Study joint spectral multiplicity of Q = F(q), transformed oscillator Hamiltonians, and whether polynomial noninvertibility persists after functional-calculus completion.
* Deliverable D4: operator-theory classification, including a decisive no-go theorem if the natural representation fails.
4.7  WP4 - C*-algebras, positivity, and dilations
* Test extension to the Weyl CCR algebra and to the resolvent algebra, which is designed to include bounded functions of unbounded canonical observables. [9]
* Check norm continuity, regularity, normality, preservation of ideals, and behavior under representations.
* If an extension is linear and unital, test positivity and complete positivity at matrix levels.
* Search for Stinespring, Cuntz-family, Hilbert-module, or correspondence implementations; distinguish multiplicative endomorphisms from general quantum channels. [8]
* Deliverable D5: extension theorem, obstruction theorem, or explicit dilation model.
4.8  WP5 - Continuous-variable quantum information
* Compare the candidate with known nonlinear unitary automorphisms such as cubic-phase transformations; isolate the genuinely new role of non-surjectivity.
* Explore whether the proper image algebra defines a bosonic subsystem, code subalgebra, information-forgetting channel, or sector decomposition.
* Construct finite-energy and finite-dimensional approximants only after a valid infinite-dimensional model exists; report convergence and error norms explicitly.
* Evaluate operational resources, noise sensitivity, reversibility costs, and whether inaccessible observables correspond to information loss or merely algebraic incompleteness.
* Deliverable D6: protocol/no-go paper and reproducible simulation notebooks.
4.9  WP6 - Generalization and synthesis
* Extract criteria applying to a class of noninjective Keller maps rather than only the anchor example.
* Create a benchmark suite for polynomial canonical endomorphisms, domains, and completions.
* Convene an external workshop spanning algebraic geometry, operator algebras, and continuous-variable quantum information.
* Deliverables D7-D8: final monograph, open benchmark release, and follow-on research roadmap.
5  Schedule, milestones, and decision gates
Gate
Timing
Decision
Acceptance evidence
G0
End M1
Anchor validated
Two independent exact CAS checks; compact human proof; Lean build reproduced; canonical data release signed.
G1
End M4
Algebraic lift established
Explicit Poisson endomorphism proven proper; Weyl candidate and commutators certified; properness proof plan closed.
G2
End M9
Analytic mechanism identified
Real/asymptotic geometry characterized; common core and formal adjoints proved; at least one decisive flow or self-adjointness theorem.
G3
End M14
Completion verdict
Existence or nonexistence theorem for a selected CCR/resolvent/C*-extension; positivity and regularity status documented.
G4
End M20
Operational relevance verdict
A valid subsystem/channel/protocol model or a rigorous no-go result excluding the proposed operational classes.
G5
End M24
Program close
Generalization, independent external review, open artifacts, final monograph, and decision on follow-on program.

5.1  Pivot and stop rules
* If G0 fails because the anchor formula or public formalization changes, freeze the discrepancy report and restart only from a corrected, independently verified map.
* If a direct Weyl counterexample cannot be constructed at the expected rank, retain the Poisson workstream and use established stable-equivalence machinery as a separate, explicitly dimensioned route.
* If essential self-adjointness fails, pivot from implementation claims to classification of extensions and boundary conditions; this is a primary scientific result, not project failure.
* If no C*- or CP extension exists in the selected categories, stop protocol engineering and publish the obstruction theorem before exploring alternative algebras or nonregular representations.
* No experimental engagement is authorized before G3 and no quantum-advantage claim is authorized before G4.
5.2  Milestone deliverables
ID
Deliverable
Due
D0
Validation dossier, proof-assistant build, and canonical map data
M1
D1
Poisson endomorphism theorem and formal certificate
M3
D2
Weyl endomorphism construction and symbolic library
M5
D3
Geometry, asymptotic behavior, and vector-field completeness study
M9
D4
Unbounded-operator and self-adjointness classification
M12
D5
C*-extension / positivity / dilation theorem or no-go result
M16
D6
Continuous-variable operational assessment
M21
D7
Open benchmark suite and reproducibility archive
M22
D8
Final monograph and follow-on roadmap
M24

6  Methods, reproducibility, and research integrity
6.1  Methodological standards
Exact before numerical
All theorem-level claims use exact arithmetic, symbolic identities, certified bounds, or formal proof. Floating-point computation is used only for exploration and visualization.
Independent implementations
Critical identities are checked in at least two systems with independent code paths; outputs are compared in canonical normal form.
Common-domain discipline
Every operator claim states the Hilbert space, initial domain, closure, adjoint, and topology. Formal commutators are never presented as exponentiated CCR results.
Evidence-labelled claims
Public outputs label claims by the A-G evidence ladder and distinguish theorem, computation, conjecture, and physical interpretation.
Reproducible environments
Lean/mathlib, CAS, and simulation dependencies are pinned; continuous integration rebuilds proofs and exact computations from clean environments.
Human accountability for AI use
AI-assisted discovery or code generation is disclosed. Named researchers review, understand, and take responsibility for every released claim.

6.2  Core toolchain
* Formal methods: Lean 4 and mathlib; optional cross-check in another proof assistant for selected identities.
* Exact algebra: SageMath, Singular, Macaulay2, SymPy, and one independent proprietary CAS where available.
* Operator numerics: interval arithmetic, sparse spectral discretization, validated ODE integration, and symbolic asymptotics.
* Software practices: version control, code review, reproducible containers, signed releases, archived hashes, and machine-readable metadata.
* Publication: preprints with executable appendices, proof objects, and a concise nontechnical claims summary.
6.3  Research integrity and communication controls
Claim-control rule
No statement may use the words "physical symmetry," "quantum operation," "channel," "gate," or "computational advantage" unless the corresponding evidence level and gate have been passed.

* Maintain a living claims ledger with owner, evidence, dependencies, external reviewer, and current status.
* Release corrections prominently and preserve superseded versions for auditability.
* Invite independent red-team review at G1, G2, and G3, including at least one expert with no project affiliation.
* Avoid press releases until G1; avoid physics-impact announcements until G3; avoid application claims until G4.
7  Team, governance, and decision rights
7.1  Recommended team
Principal investigator
Owns scientific coherence, gate decisions, claim discipline, and sponsor reporting.
Algebraic geometry / polynomial maps lead
Anchor map, fibers, asymptotic geometry, reductions, and exact algebra.
Poisson / symplectic geometry lead
Cotangent lift, canonical relations, Lagrangian correspondences, and classical flows.
Noncommutative algebra lead
Weyl endomorphism, filtrations, image subalgebra, centralizers, and properness.
Unbounded-operator lead
Domains, closures, adjoints, self-adjointness, strong commutation, and spectra.
Operator-algebra lead
CCR/resolvent C*-algebras, normal extensions, positivity, CP maps, and dilations.
Continuous-variable quantum information lead
Operational models, finite-energy approximations, protocols, and resource analysis.
Formal methods / research software lead
Proof assistant, CAS cross-checks, CI, benchmark releases, and provenance.
External advisory panel
Quarterly challenge review across algebra, mathematical physics, and quantum information.

7.2  Governance cadence
Weekly
Technical working-group review; open issues; proof and computation review.
Monthly
Program integration meeting; risk register; claims ledger; resource allocation.
Quarterly
External advisory review and written challenge memo.
At each gate
Formal evidence packet, independent reviewer sign-off, and sponsor go / pivot / stop decision.
At release
Reproducibility audit, authorship/attribution review, and public claims review.

7.3  Decision rights
* The PI decides routine scientific priorities within the approved scope.
* Gate passage requires the PI, relevant workstream lead, and at least one external reviewer.
* Scope expansion into experimental work or public application claims requires sponsor approval after G3 or G4, respectively.
* Any team member may trigger a research-integrity hold on a release; the hold remains until documented resolution.
8  Risk register and mitigations
ID
Risk
Prob.
Impact
Mitigation
R1
Anchor changes or provenance dispute
L
H
Versioned exact data; independent proof; correction protocol; G0 restart rule.
R2
Logical equivalence mistaken for explicit construction
M
H
Use direct cotangent/Weyl formulas; state dimensions and implications precisely; external algebra review.
R3
Expression blow-up makes analysis opaque
H
M
Exploit weighted grading, sparse normal forms, modular methods, and machine-readable generators.
R4
Formal symmetry is misreported as self-adjointness
M
H
Mandatory domain/closure checklist; unbounded-operator lead signs every such claim.
R5
No C*- or CP extension exists
H
M
Treat obstruction as a target result; stop protocol work and publish no-go theorem.
R6
Numerical truncation creates false finite-dimensional evidence
M
H
Require convergence bounds and comparison to exact infinite-dimensional statements.
R7
Hype or confusion about nonlinear quantum mechanics
H
H
Terminology standard; evidence labels; communications gate; no state-nonlinearity framing.
R8
AI-assisted work weakens trust
M
M
Full disclosure, human derivations, reproducible proof objects, external red-team review.
R9
Result is mathematically valid but physically empty
M
M
Define no-go and boundary theorems as success; prioritize generalizable criteria.
R10
Team spans incompatible conventions
H
M
Shared notation guide; common benchmark examples; cross-discipline paired reviews.

9  Resource model
9.1  People
Recommended steady-state staffing is approximately 6-8 full-time-equivalent researchers, with the disciplinary roles listed above distributed across faculty, postdoctoral researchers, doctoral researchers, and research software engineering. External advisory effort is additional and part-time.
9.2  Compute and facilities
* Modest CPU and memory resources for exact symbolic algebra, proof compilation, interval ODEs, and sparse spectral calculations.
* No quantum hardware is required during the first 18 months.
* Secure, versioned source control and archival storage for proof objects and reproducibility images.
* Workshop and visiting-researcher support at G2-G4 to integrate otherwise separate expert communities.
9.3  Budget categories
* Personnel and postdoctoral support; formal-methods/research-software engineering.
* Compute, storage, software licenses, and archival services.
* External review, focused workshops, and cross-disciplinary visitor support.
* Open-access publication and long-term artifact preservation.
A detailed monetary budget should be prepared after sponsor, host institution, and staffing model are selected. The charter does not assume major capital expenditure.


10  First 90 days
Period
Theme
Required output
Days 0-30
Validate and freeze
Reproduce determinant and collisions; build Lean proof; normalize map; create claims ledger; appoint external reviewers; publish D0 candidate.
Days 31-60
Construct and certify
Compute B; prove Poisson relations and noninjectivity; build Weyl candidate; verify commutators and divergence identity; draft D1/D2.
Days 61-90
Open the analytic front
Map real fibers and escape directions; define Schwartz-core operators; begin flow completeness and deficiency-index analysis; hold G1 challenge workshop.

10.1  Day-90 decision package
* Validated anchor release and independent review report.
* Explicit cotangent-lift Poisson endomorphism with exact noninjectivity witness.
* Explicit Weyl generator substitution with verified commutators and a proof-status report on properness.
* Formal-adjoint and divergence calculation in the real Schrodinger representation.
* Ranked analytic hypotheses for incompleteness, self-adjointness, and C*-extension.
* Updated 21-month plan, budget, and gate criteria based on actual complexity.
11  Approval and charter authority
Approval authorizes only the 90-day launch phase and the planning assumptions in this charter. Continued funding beyond Gate 1 is contingent on the evidence packet and revised work plan.
Role
Name / signature
Date
Sponsor


Principal investigator


External technical reviewer




Appendix A - Technical anchor and initial theorem checklist
A.1  Exact collision witness
F(0, 0, -1/4) = (-1/4, 0, 0)
F(1, -3/2, 13/2) = (-1/4, 0, 0)
F(-1, 3/2, 13/2) = (-1/4, 0, 0)

Together with det DF = -2, this gives a finite exact disproof of global polynomial invertibility for the displayed map. The program will preserve exact rational witnesses in every release.
A.2  Initial theorem checklist
ID
Statement
Method
Gate
T0.1
det DF is the stated nonzero constant
Exact CAS + Lean
G0
T0.2
The three collision identities hold
Exact CAS + Lean
G0
T1.1
B = DF^(-T) has polynomial entries
Adjugate formula
G1
T1.2
Phi(q,p) = (F(q),B(q)p) preserves the canonical Poisson bracket
Symbolic proof + geometric proof
G1
T1.3
Phi is not an automorphism
Explicit lifted collision
G1
T1.4
The Weyl substitution preserves all canonical commutators
Noncommutative symbolic proof
G1
T1.5
The Weyl endomorphism is not surjective
Direct theorem / standard construction
G1-G2
T2.1
Row-wise div B = 0
Piola identity + exact check
G2
T2.2
Transformed momenta are formally symmetric on S(R^3)
Integration by parts
G2
T2.3
At least one dual vector field is incomplete, or a countervailing theorem is found
Flow/geometry analysis
G2
T3.1
Essential self-adjointness and strong commutation are classified
Operator theory
G2-G3
T4.1
Selected C*- / resolvent extension exists or is impossible
Operator-algebra theorem
G3
T5.1
Operational CP/dilation model exists or selected classes are excluded
Quantum channel theory
G4

A.3  Interpretation matrix
Highest level reached
Permitted interpretation
Poisson endomorphism only
New classical algebraic example; no quantum claim.
Weyl algebra *-endomorphism on a core
Nonlinear observable substitution; still not a physical operation.
Self-adjoint regular realization
Canonical observables exist analytically; unitary implementation remains impossible if proper.
C*-endomorphism
A bounded algebraic quantum structure exists; operational meaning depends on representation and normality.
Unital CP map / dilation
Legitimate open-system Heisenberg operation; investigate information loss and subsystem structure.
Finite-energy protocol
Candidate continuous-variable primitive; only then assess complexity or experimental feasibility.

Appendix B - Selected references
[1] L. Alp�ge, announcement of an explicit three-variable Jacobian counterexample, X post, 19 July 2026, status 2079028340955197566.
[2] D. Cureton, "Levent Alp�ge/Fable 5's counterexample to the Jacobian conjecture in Lean 4," public repository deancureton/jacobian, accessed 20 July 2026.
[3] D. Speyer, "The new counterexample to the Jacobian conjecture," Secret Blogging Seminar, 20 July 2026.
[4] A. Belov-Kanel and M. Kontsevich, "The Jacobian conjecture is stably equivalent to the Dixmier conjecture," Moscow Mathematical Journal 7 (2007), 209-218; arXiv:math/0512171; doi:10.17323/1609-4514-2007-7-2-209-218.
[5] P. K. Adjamagbo and A. van den Essen, "A proof of the equivalence of the Dixmier, Jacobian and Poisson conjectures," Acta Mathematica Vietnamica 32 (2007), 205-214; arXiv:math/0608009.
[6] Y. Tsuchimoto, "Endomorphisms of Weyl algebra and p-curvatures," Osaka Journal of Mathematics 42 (2005), 435-452.
[7] H. J. Groenewold, "On the principles of elementary quantum mechanics," Physica 12 (1946), 405-460; doi:10.1016/S0031-8914(46)80059-4.
[8] W. F. Stinespring, "Positive functions on C*-algebras," Proceedings of the American Mathematical Society 6 (1955), 211-216; doi:10.1090/S0002-9939-1955-0069403-4.
[9] D. Buchholz and H. Grundling, "The resolvent algebra: A new approach to canonical quantum systems," Journal of Functional Analysis 254 (2008), 2725-2779; arXiv:0705.1988; doi:10.1016/j.jfa.2008.02.011.
[10] P. R. Chernoff, "Essential self-adjointness of powers of generators of hyperbolic equations," Journal of Functional Analysis 12 (1973), 401-414; doi:10.1016/0022-1236(73)90003-7.
[11] S. Lloyd and S. L. Braunstein, "Quantum computation over continuous variables," Physical Review Letters 82 (1999), 1784-1787; arXiv:quant-ph/9810082; doi:10.1103/PhysRevLett.82.1784.
[12] S. L. Braunstein and P. van Loock, "Quantum information with continuous variables," Reviews of Modern Physics 77 (2005), 513-577; doi:10.1103/RevModPhys.77.513.
[13] H. Bass, E. H. Connell, and D. Wright, "The Jacobian conjecture: Reduction of degree and formal expansion of the inverse," Bulletin of the American Mathematical Society 7 (1982), 287-330.
Reference status note
References [1]-[3] document a result announced within one day of this charter. They are included for provenance and current context, not as substitutes for the project's independent Gate 0 validation.

PROJECT EXOTIC-CCR   |   Research Project Charter

Page 2


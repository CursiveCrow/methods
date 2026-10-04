# Phase 4 verification: Part 12

> **INVALIDATED UNDER THE FULL-TRANSCRIPTION STANDARD (2026-08-12).** This
> draft verifies a compressed migration policy that the user revoked. It is
> retained only as evidence of alterations, omissions, rehoming, and retired
> material; it cannot support a Part 12 completion claim.

Date: 2026-08-11
Visit: P12, Automation and Mechanization
Status: **DRAFT -- awaiting final rendered-page inspection; not frozen**
Verified source: `v1.1-verified`, lines 14095--15091, the rehomed
appendix/rule-sheet span 15095--15488, the retired assessment span
15489--16742, the release checklist at 16743--16801, and the manual
bibliography/backmatter from 16803 to the end.
Research baseline: frozen `spec/research/p12-new-content.md`.

This is the adversarial mathematical, evidence-status, source-accounting,
register, and release-verification record for the P12 visit.  Build, static,
agent-review, rendered-page, and human-verification claims are kept separate.
The integrated build and static facts are recorded below against the
authoritative PDF, but the visual fields remain explicit placeholders until
the final render review is returned.

## Verification verdict

- The complete source span and all nine P12 exercises have an explicit
  disposition below.  No source proof, result, appendix, rule sheet, exercise,
  or release-checklist unit is silently dropped or converted into stronger
  evidence.
- The live body has exactly eight theorem-class results: one `proved`, zero
  `sketched`, and seven `cited`.  The sole proved result points to exactly one
  annex item, with no second P12 result sharing that target.
- The DPLL theorem remains `proved=annex:p12.sat.1`.  Its proof covers the
  residual-clause invariant, both terminal cases, both directions of the
  branching equivalence, finite termination, total-model return, and
  root-level unsatisfiability.  It does not claim coverage of pure-literal
  elimination, CDCL, or implementation heuristics.
- Exactly ten explicit P12 stub boxes remain.  They preserve the Phase-5
  boundaries and P9 pointer obligations listed below; apparatus tables do not
  masquerade as the deferred exact entries.
- The user's syntax correction is binding throughout this record and the live
  text: a named model, logic, calculus, protocol, or method retains the syntax
  used by its cited presentation.  The registry records the locally typed role
  of that syntax; it does not rename it to fit a handbook house syntax.  When
  no exact cited presentation is supplied, P12 states the owed row-bound
  artifact and does not manufacture a calculus.
- Integrated static checks, source integrity, the full TeX build, and two
  independent P12 agent reviews pass.  Those facts do **not** establish the
  pending rendered-page verdict and are not human mathematical verification.
- Final integrated visual verdict: **PENDING -- [insert PASS or BLOCKED after
  final render review]**.

## Delivered scope

- Seven body fragments: SAT and certificates; SMT and exchange formats;
  first-order automation; the explicit rewriting boundary; interactive proof;
  formal workflow; and further reading/navigation.
- One annex fragment containing the complete DPLL proof and no other P12
  annex item.
- SAT material fixes the finite original variable set, residual state, unit
  propagation, branch semantics, both terminal cases, total returned
  valuations, and certificate boundaries.  ROBDD, QBF, counting SAT, and
  MaxSAT are distinguished by object and complexity standing.
- First-order automation links the canonical P2 unification and resolution
  artifacts, retains equality and saturation boundaries, and classifies
  ordered resolution, Robinson hyperresolution, Slagle semantic resolution,
  set of support, and subsumption without displaying new body rules.
- SMT material defines theory atoms, Boolean abstraction, purification,
  equality arrangements, the DPLL(\(T\)) architecture boundary, and exact
  Nelson--Oppen hypotheses.  SMT-LIB and TPTP are treated as exact exchange
  formats rather than as proof systems.
- Mechanization material separates proof objects, proof terms, proof scripts,
  elaboration, kernels, tactics, deep and shallow embeddings, LCF, the de
  Bruijn criterion, computational reflection, PTS/lambda-cube notation,
  CIC/pCIC boundaries, assistant trust paths, and exact landmark claims.
- The release workflow supplies typed audit methods and a categorized release
  gate.  It reports statement fidelity, build, static analysis, rendered-page
  inspection, agent review, and human review as different categories.
- Apparatus delivered or routed here includes A-030, A-105--A-108, A-121,
  A-149, A-182, A-186, and A-189.  A-106 remains open by design.

## Frozen-source accounting

| v1.1 lines | Source unit | Live home | P12 disposition and evidence class |
|---:|---|---|---|
| 14095--14270 | Constructing derivations, countermodels, and metatheoretic proofs | `parts/p12/formal-workflow.tex` | Migrated as compact `hbmethod` entries and a failure-classification table.  Methods are neither displayed inference rules nor proof evidence. |
| 14271--14350 | DPLL core and correctness | `parts/p12/sat-and-certificates.tex`; `annex/p12/sat-and-certificates.tex` | Migrated as the exact finite-clause logical core and the sole new P12 complete proof. |
| 14351--14399 | Equivalence/equisatisfiability and Tseitin example | P2 canonical definition/result; P12 audit pointer | Rehomed to `def:p02-equisatisfiability` and `thm:p02-tseitin`; P12 retains only the transformation-audit distinction and does not duplicate a theorem. |
| 14401--14434 | Elementary unification restatement and examples | P2 canonical unification entries; P12 occurs-check pointer | Rehomed.  The example remains non-statused and the deeper Martelli--Montanari obligation remains stubbed. |
| 14435--14479 | FOL Resolution rule, soundness proof, and cited completeness | P2 theorems/annex; `sheet:resolution-fol`; P12 search pointer | Rehomed without redisplaying a rule or duplicating proof evidence.  P2 soundness stays proved and equality-free completeness stays sketched. |
| 14480--14495 | Equality/superposition warning | `parts/p12/first-order-automation.tex` | Retained as a proof boundary; the exact superposition calculus and its completeness artifact remain named only by `D-P11-003`/`N-c-036`. |
| 14496--14521 | Basic SMT, SMT-LIB, and TPTP | `parts/p12/smt-and-exchange-formats.tex` | Migrated with exact theory-relative roles, format versions, grammar boundaries, retrieval dates, and trust/audit fields. |
| 14522--14560 | SAT/FOL complexity and automated-result audit | P2/P4 canonical theorems; P12 audit method | Cross-referenced without a third theorem; practical-status and timeout boundaries survive. |
| 14562--14589 | Three automation exercises | P12 examples/pointers | Exercise format retired; the DPLL trace, occurs-check example, and clausification audit survive without theorem status. |
| 14591--14728 | Mechanized proof checking | `parts/p12/interactive-proof.tex` | Definitions, trust/audit methods, exact-source PTS material, assistant landscape, and one P7-linked typed example migrated. |
| 14729--15029 | Writing and typesetting formal logic | `parts/p12/formal-workflow.tex` | Compressed to method boxes and audit tables.  Raw proof/rule displays and paragraph-style proof markers were not migrated. |
| 15030--15091 | Research workflow and reproducibility | `parts/p12/formal-workflow.tex` | Status records, counterexample-first review, computational-supplement fields, and independent-review controls migrated. |
| 15095--15206 | Duplicate notation appendix | P1 symbol registry and generated symbol tables | Deliberately retired from P12 and replaced by registry navigation. |
| 15207--15239 | Duplicate binding/precedence appendix | P1 precedence chapter | Deliberately retired from P12. |
| 15240--15488 | Copied rule sheets | Calculus registry and P14 sheet index | Deliberately retired from the body.  Every live rule remains registry-generated. |
| 15489--15637 | Qualifying problems and supplied solutions | Cross-part canonical entries | Assessment format retired; no supplied solution is used as proof-status evidence. |
| 15638--16742 | Whole-book exercise feedback | No printed exercise chapter | Retired globally; only the nine P12 examples below are selectively rehomed, with no evidence upgrade. |
| 16743--16801 | Release checklist | `parts/p12/formal-workflow.tex` | Converted into the formal-logical release-audit table with verification categories separated. |
| 16803--end | Manual bibliography and backmatter | `handbook/bib/handbook.bib` and normal driver | Hand-maintained duplicate bibliography retired; cited records are integrated into the canonical bibliography. |

## Exercise and assessment disposition

| Source label | Exact disposition |
|---|---|
| `ex:formal-practice-01` | Converted to the two-element small-structure countermodel example, including the one-element impossibility argument; no theorem status. |
| `ex:formal-practice-02` | Replaced by a pointer from the metatheorem method to the canonical P2 substitution lemma; the supplied solution sketch is not reproduced. |
| `ex:automated-reasoning-01` | Retained as a DPLL/unit-propagation trace ending in an empty clause; the text states that this certifies only that instance. |
| `ex:automated-reasoning-02` | Retained as the finite-term occurs-check boundary linked to P2 unification; it does not close the Martelli--Montanari row. |
| `ex:automated-reasoning-03` | Retained as a clausification audit with expansion/reduct equisatisfiability at the Skolem step; no misuse of elementary `\equiv`. |
| `ex:mechanization-01` | Folded into one propositions-as-types example using P7's exact registered STLC syntax and `sheet:stlc`; no typing rule is redisplayed. |
| `ex:mechanization-02` | Folded into the encoding-audit obligations; neither a deep nor a shallow adequacy theorem is claimed from notation alone. |
| `ex:latex-style-01` | Folded into the formal-definition writing method, which demands typed maps and exact definitions/lemmas; exercise and solution retired. |
| `ex:latex-style-02` | Folded into the notation-registry gate and P1 pointer; exercise and solution retired. |

The five qualifying problems and their supplied solutions are retired as
assessment apparatus.  Their reusable mathematics is routed to canonical
Parts 2, 3, 5, 7, and 8 entries.  The additional formalization prompt becomes
an audit row, not a theorem, and no part of the global feedback chapter is
mined for an unlabelled proof upgrade.

## Statement-by-statement fidelity sample

The deliberate second pass covered every live P12 theorem-class result and
all central source methods.

| Live item | Adversarial check |
|---|---|
| `thm:p12-dpll-correctness` | Finite input, fixed `Var(F)`, residual-state invariant, empty-set success, empty-clause failure, total extension, two-child equivalence, and strict decrease in unassigned original variables are explicit.  Pure-literal elimination and CDCL are excluded from the proved scope. |
| `thm:p12-robdd-canonicity` | Quantifies over finite `X`, a total order on `X`, and `f:{0,1}^X -> {0,1}`; unique terminals, reachability, low/high semantics, ordering, reduction, and rooted labelled graph isomorphism are fixed before the cited statement. |
| `thm:p12-counting-sat-status` | `#SAT` is a function and `#P` a counting class; completeness is under polynomial-time parsimonious reductions, not an unspecified decision reduction. |
| `thm:p12-maxsat-status` | The NP-complete object is the unweighted threshold decision problem; optimization, weighting, approximation, and encoding claims remain separate. |
| `thm:p12-set-of-support` | The exact equality-free clause partition, least support closure, at-least-one-support-parent restriction, usable-set satisfiability, factoring, no deletion/contraction, and fairness hypotheses are retained. |
| `thm:p12-nelson-oppen` | Inputs are quantifier-free and purified; signatures are disjoint apart from equality/shared sorts; component decision procedures, stable infiniteness, equality arrangements, convex communication, and nonconvex case splitting are explicit. |
| `thm:p12-lcf-boundary` | The conclusion is conditional on preservation of the abstract theorem-type boundary and sound trusted primitive constructors; it does not certify an implementation, identify the whole trusted base, or promise portable certificates. |
| `thm:p12-lambda-cube-classification` | Uses Barendregt's two-sort PTS convention and exact eight source identifiers; the classification statement is not rewritten into handbook-invented system names. |
| DPLL method | The displayed logical core uses unit propagation and binary branching only; pure-literal elimination is separately defined and expressly outside the theorem proof. |
| Equisatisfiability audit | Routes to P2's canonical definition and Tseitin theorem; expanded-signature equisatisfiability is never stated as same-signature formula equivalence. |
| Unification boundary | The finite-term occurs check is an example linked to P2; it is not relabelled as Martelli--Montanari termination or MGU completeness. |
| Resolution refinements | Ordered resolution is an eligibility restriction, Robinson hyperresolution an inference family, Slagle semantic resolution uses its actual clash/resolvent notation, set of support is a search restriction, and subsumption is contraction. |
| SMT boundary | Theory atoms and Boolean abstraction are typed before use; purification introduces same-sort shared variables; no theorem asserts blanket SMT decidability or unrestricted combination. |
| Deep/shallow embedding | Syntax, interpretation, representation, and adequacy obligations are separately quantified; neither encoding is declared adequate merely because it is displayed. |
| Mechanized-result and release audits | Exact statement, dependencies, system, verification route, inputs/hashes, commands, checker version, fixed seed for generated examples, expected/observed result, environment, and reviewer identity/configuration are separate fields. |

No sampled statement lost a hypothesis or gained an evidence class.

## Complete-proof compression evidence

Only an inherited complete Tier-2 proof receives a source denominator.  The
established one-pass `detex` alphabetic-word method, excluding theorem
statements and proof delimiters, gives:

| Complete source proof | Source words | Advisory 40--60% observation | Live annex words | Verification disposition |
|---|---:|---:|---:|---|
| DPLL correctness, 14328--14349 | 144 | 57--87 | 329 | `proved=annex:p12.sat.1`; logically complete and deliberately not ratio-tuned. |

The 40--60 percent range is an observation, not an evidence rule.  The live
proof is longer because it repairs the source defect tracked by R-038 and must
state both halves of the residual-clause invariant, the initial and propagated
terminal cases, total-model extension, both directions of branch
satisfiability, finite termination, and the root failure conclusion.  Deleting
any load-bearing step merely to enter 57--87 words would weaken or gap the
proof.  Therefore no ratio deletion was made.  No ratio applies to cited
results, rehomed P2 proofs, examples, methods, stubs, or retired material.

## Exact eight-result status graph

| Chapter | Body label | Exact status destination |
|---|---|---|
| 12.1 | `thm:p12-dpll-correctness` | `proved=annex:p12.sat.1` |
| 12.1 | `thm:p12-robdd-canonicity` | `cited=Bryant1986` |
| 12.1 | `thm:p12-counting-sat-status` | `cited=Valiant1979Enumeration` |
| 12.1 | `thm:p12-maxsat-status` | `cited=LiManya2009` |
| 12.2 | `thm:p12-nelson-oppen` | `cited=NelsonOppen1979` |
| 12.3 | `thm:p12-set-of-support` | `cited=WosRobinsonCarson1965` |
| 12.5 | `thm:p12-lcf-boundary` | `cited=GordonMilnerWadsworth1979` |
| 12.5 | `thm:p12-lambda-cube-classification` | `cited=Barendregt1992` |

The exact annex graph has one edge:

| Annex label | Sole body back-reference | Evidence class |
|---|---|---|
| `annex:p12.sat.1` | `thm:p12-dpll-correctness` | inherited complete proof, repaired without a scope upgrade |

All seven cited results have no annex item.  The generated P12 audit contains
49 entries, `main.hbstatus` contains exactly eight P12 status lines, and
apparatus A-189 lists each status-bearing P12 result exactly once.

## Depth-row reconciliation

`Done-candidate` means the live tree supplies the literal requested treatment
at the stated ceiling while preserving evidence status; this note does not
itself mutate a CSV register.  `Open` means the row must remain open.

| Row | Ceiling / priority | Verification disposition |
|---|---|---|
| `D-P11-001` | E / must | **Open; explicit stub.** A-105 and A-149 define the comparison/figure apparatus, but no full CDCL transition system, correctness result, or certificate calculus is claimed. |
| `D-P11-002` | E / must | **Open; explicit stub.** P2 unification and the occurs-check example do not supply the exact Martelli--Montanari transformations, termination proof, or MGU factorization theorem. |
| `D-P11-003` | S / must | **Open; explicit stub.** The equality boundary does not fabricate a superposition sheet, ordering/redundancy calculus, or saturation completeness theorem. |
| `D-P11-004` | S / should | **Done-candidate.** Ordered, hyper-, semantic, and set-of-support resolution plus subsumption are exactly distinguished by role and bounded by citations and hypotheses. |
| `D-P11-005` | S / should | **Done-candidate at S.** DPLL(T), purification, equality arrangements, and the Nelson--Oppen boundary are supplied without claiming the E-level `N-c-034` proof. |
| `D-P11-009` | S / should | **Done-candidate.** ROBDD, QBF, counting SAT, and MaxSAT are separately defined and calibrated; model-checking completion is not inferred from BDD coverage. |
| `D-P11-011` | T / should | **Done-candidate.** The assistant/verifier landscape includes the required systems with foundation, checking/trust path, version or retrieval date, and a non-equivalence warning. |
| `D-P11-012` | S / should | **Done-candidate.** Universes, inductives, W-types, two equality roles, and CIC/pCIC boundaries are defined; Lean is not identified with Rocq's pCIC, and extraction stays separate. |
| `D-P11-013` | P / could | **Open; explicit stub.** The future HoTT/univalence pointer must identify an exact calculus and source; no technical development is invented. |
| `D-P11-014` | S / should | **Done-candidate.** LCF's abstract theorem type/kernel discipline and the operational de Bruijn criterion are defined apart; one is not inferred from the other. |
| `D-P11-015` | T / could | **Done-candidate under the handover's explicit inclusion.** Four Color, Odd Order, Flyspeck, CompCert, and seL4 rows state exact formal result, assistant, trust boundary, and primary source without whole-system inflation. |

## New-content reconciliation

| Row | Ceiling / priority | Verification disposition |
|---|---|---|
| `N-c-031` | S / should | **Done-candidate.** Barendregt's exact PTS/lambda-cube surface and the CoC/CIC/pCIC assistant-foundation boundary are supplied, coordinated with P7. |
| `N-c-032` | E / must | **Open; explicit stub with D-P11-001.** CDCL vocabulary and apparatus do not close the full E-level algorithm/proof obligation. |
| `N-c-033` | T / should | **Done-candidate.** P12 routes to P2's Horn/2-SAT results and adds only a citation-bounded random-k-SAT pointer. |
| `N-c-034` | E / must | **Open; explicit stub.** The S-level SMT/Nelson--Oppen survey and A-107 do not constitute the required E-level internals/proof. |
| `N-c-035` | E / must | **Open; explicit stub with D-P11-002/A-106.** No deeper unification theorem is inferred from the elementary P2 treatment. |
| `N-c-036` | S / must | **Open; explicit stub with D-P11-003.** No exact superposition calculus or model-construction completeness sketch is fabricated. |
| `N-c-037` | E / must | **Open; explicit stub.** Term rewriting, critical pairs, completion, LPO, and KBO remain a Phase-5 owed artifact. |
| `N-c-038` | S / should | **Done-candidate.** LCF, proof objects/terms/scripts, trusted bases, the de Bruijn criterion, and computational reflection are separated and sourced. |
| `N-c-039` | S / could | **Open; explicit stub.** Landscape-table mentions do not close program extraction. |
| `N-c-040` | P / could | **Open; explicit stub.** Hammers and proof reconstruction remain a future pointer with no fabricated technical content. |

## Apparatus reconciliation

| Row | Phase-4 P12 disposition |
|---|---|
| `A-030` | **Canonical cross-reference.** P12 points to `tab:p02-tractable-sat`; it does not create a second Horn/dual-Horn/2-SAT/XOR-SAT master table. |
| `A-105` | **Done-candidate.** `tab:p12-dpll-cdcl` compares DPLL and CDCL across learning, watched literals, restarts, certificates, and trust/status boundaries without closing `N-c-032`. |
| `A-106` | **Open; explicit stub.** Exact Martelli--Montanari rules and proof are deferred; no body rule table violates the registry-only rule policy. |
| `A-107` | **Done-candidate.** `tab:p12-smt-theories` records EUF, arrays, bit-vectors, and arithmetic fragments with decidability/complexity and exact combination conditions or nonapplicability. |
| `A-108` | **Done-candidate.** `tab:p12-assistant-landscape` records required assistants/verifiers by foundation, checking architecture, automation/trust path, and declared de Bruijn criterion. |
| `A-121` | **Canonical cross-reference.** P12 points to P2's propositional and FOL resolution DAGs and does not duplicate them. |
| `A-149` | **Done-candidate.** `fig:p12-cdcl-conflict` defines node, edge, decision-level, learned-clause, UIP, asserting/nonasserting, and backjump roles; the figure is not a CDCL completeness proof. |
| `A-182` | **P12 contribution delivered; global row remains finalizer-controlled.** Twenty-four verified P12 intake records are integrated into the canonical bibliography. |
| `A-186` | **P12 contribution delivered; global row remains finalizer-controlled.** The annotated further-reading route covers SAT, first-order automation, SMT, mechanization, and type-theory boundaries. |
| `A-189` | **P12 contribution delivered; global row remains finalizer-controlled.** The status-route and canonical-route tables connect all eight P12 results, the sole annex item, P2/P4/P7 results, and real registry sheets. |

## Defect reconciliation

| Row | Verification disposition |
|---|---|
| `R-038` | **Resolved in the live P12 tree, pending register reconciliation.** The DPLL proof gives both total-model success and exhausted-search unsatisfiability, with the invariant and branch equivalence explicit. |
| `S-014` | **Resolved locally.** All eight P12 theorem-class entries have exactly one valid status form; methods, definitions, examples, and proof boundaries do not carry theorem status. |
| `S-018` | **Resolved locally.** P12 displays no body inference rules; Resolution/Factoring and STLC are linked to real sheets, while deferred MM/superposition rules remain stubs. |
| `S-019` | **Resolved by canonical routing.** SAT NP-completeness, FOL c.e./undecidability, and Resolution soundness/completeness point to existing P2/P4 statused results. |
| `S-022` | **Resolved locally, pending global release.** The source checklist is a categorized release-gate table with verification categories reported separately. |
| `L-014` | **Resolved locally.** No paragraph command or exercise solution carries result/status semantics. |
| `L-017` | **Resolved locally.** The source's fake listing label is not migrated; retained tables/figures use real surrounding captions and labels. |

Global primary-source, rule-generation, bibliography, navigation, source-
regression, build, and rendered-page controls are not falsely closed by the
P12-local verdict.

## Exact ten-stub ledger

The live P12 body contains ten `\hbstub` boxes:

1. `D-P11-001 / N-c-032` -- the full E-level CDCL entry.
2. `N-c-013 / N-c-017` -- one combined P9 pointer box for omega-automata/LTL
   and symbolic BDD-based model checking.
3. `D-P11-002 / N-c-035 / A-106` -- the Martelli--Montanari algorithm and
   theorem.
4. `D-P11-003 / N-c-036` -- a named exact superposition calculus and its
   saturation/model-construction result.
5. `N-c-009` -- the exact ALC tableau procedure at its P9 home.
6. `N-c-034` -- E-level SMT internals and proof beyond the S-level survey.
7. `N-c-037` -- the term-rewriting entry.
8. `D-P11-013` -- the exact-source HoTT/univalence pointer.
9. `N-c-039` -- program extraction.
10. `N-c-040` -- hammers and proof reconstruction.

The ten boxes cover eleven distinct row groups because the two P9
model-checking pointers share one box.  Stubbed rows remain open regardless of
the existence of nearby tables, figures, definitions, or cited surveys.

## Exact-source-syntax and naming correction

The user correction prohibits choosing a handbook syntax for an already named
model, method, or logic.  The live P12 implementation satisfies that rule as
follows:

- Barendregt's PTS is written as
  \(S=(\mathcal S,\mathcal A,\mathcal R)\), with
  \(\mathcal A\) a set of sort axioms \(s_1:s_2\),
  \(\mathcal R\) a set of product-sort triples, and
  \(\lambda S=\lambda(\mathcal S,\mathcal A,\mathcal R)\).  The two sorts,
  the \((s_1,s_2)\) abbreviation, and all eight lambda-cube identifiers are the
  cited source's notation, including \(\lambda\mathrm P\omega=\lambda\mathrm C\).
- The propositions-as-types example reuses the exact registered P7 STLC
  grammar, type arrow, context, ascription, and system-indexed derivability
  judgment; it does not invent a P12 typing surface.
- Robinson hyperresolution and Slagle semantic resolution retain the cited
  methods' actual nucleus/electron and ground-interpretation/resolvent roles.
  The symbol registry records those local roles even where a glyph has another
  role elsewhere.
- SMT-LIB 2.7 and TPTP BNF 9.3.0.3 are reproduced as protocol/grammar syntax,
  not converted into handbook mathematical operators.  Literal solver tokens
  are not registered as mathematical result glyphs.
- The Agda row is pinned to Agda 2.8.0 and its actual option spelling:
  `--no-sized-types`, no `--cubical`, and no `--rewriting`.  Other assistant
  rows likewise report their own foundations and checking paths rather than a
  normalized common calculus.
- The notation gate now says to retain the published glyph of a named
  presentation and register its locally typed role.  Only notation introduced
  by the handbook itself is subject to a new scoped row after the five-part
  necessity gate.
- Deferred CDCL, Martelli--Montanari, superposition, term-rewriting,
  HoTT/univalence, extraction, and hammer obligations are described by their
  register rows.  No speculative grammar, rule inventory, or new technical
  name is introduced in their place.

## Adversarial correction log

The writing and independent review passes corrected or made explicit:

- DPLL's fixed original-variable set, exact residual-clause invariant,
  initial as well as propagated terminal cases, total returned valuation,
  branch biconditional, and proof scope excluding pure-literal elimination;
- the exact definition of `Var(F)`, residual clauses, pure-literal
  elimination, and the distinction between DPLL and CDCL;
- ROBDD finiteness, terminal uniqueness, reachability, low/high semantics,
  order discipline, reduction, constant-function edge cases, and exact
  isomorphism quantification;
- counting-function versus decision-language standing, parsimonious
  reductions, and the unweighted MaxSAT threshold formulation;
- decision levels, UIP, asserting/nonasserting learned clauses, and exact
  backjump level, without upgrading apparatus into a CDCL proof;
- source-exact Robinson hyperresolution and Slagle semantic-resolution
  notation, ordered-resolution eligibility, and set-of-support closure,
  fairness, usable-set satisfiability, factoring, and no-deletion boundary;
- theory atoms, Boolean abstraction, same-sort purification variables,
  equality arrangements, stable infiniteness, convexity, and required
  nonconvex case splits;
- exact QF_AX, QF_BV, SMT-LIB 2.7, and TPTP 9.3.0.3 surfaces and the
  distinction between an exchange format and a trusted checker;
- proof object, proof term, and proof script standing; LCF versus the de
  Bruijn criterion; computational reflection; and deep/shallow adequacy
  obligations;
- Barendregt's PTS/lambda-cube notation and identifiers, CIC/pCIC/Lean
  boundaries, de Bruijn indices, and Agda's exact 2.8.0 option baseline;
- release-record fields for exact statement, dependencies, status, system,
  verification, input/hash, command/cwd, tool version, fixed random seed,
  expected/observed result, environment, and reviewer identity/configuration;
  and
- blank-verso handling through the shared `emptypage` integration, without
  treating a successful build as a rendered-page verdict.

## Bibliography and symbol integration

- The canonical bibliography contains all 24 new verified P12 intake records
  exactly once: de Bruijn/AUTOMATH, LCF, proof-belief/trust, practical
  automation, PTS/CIC sources, random SAT, counting SAT, MaxSAT, semantic and
  set-of-support resolution, the exact assistant/manual sources, and the five
  landmark-formalization sources.
- Existing canonical keys are reused for DPLL, Tseitin, Resolution,
  Nelson--Oppen, DPLL(T), SMT, rewriting boundaries, complexity, and current
  assistant manuals.  No citation-only P12 status names a missing key.
- The live symbol registry has 33 rows whose declared scope or first use
  includes P12.  These include reused substitutions, clause interpretation,
  complexity/SAT, and STLC notation, plus exact local rows for DPLL, counting
  SAT, MaxSAT, SMT/EUF, semantic resolution, LCF, PTS, Barendregt's cube, and
  CIC.
- Formula metavariables remain `varphi,psi,chi`; term substitutions remain
  `theta,rho,eta`; type metavariables remain `alpha,beta,gamma`; encoding
  length is never written with cardinality bars; and every displayed
  derivability judgment names its system.
- The generated symbol tables build from `registry/symbols.csv`; the duplicate
  source notation appendix remains retired rather than becoming a second
  registry.

## Mechanical evidence

- Exact local result/annex graph scan: **PASS** -- eight results (one proved,
  zero sketched, seven cited), one annex item, one proved-to-annex edge, and no
  second P12 target or cited-result annex.
- Exact local stub scan: **PASS** -- ten P12 `\hbstub` boxes, exactly the boxes
  listed above.
- Body/annex separation scan: **PASS** -- the P12 body contains zero
  `\hbrule`, `\begin{proof}`, `\begin{proofplan}`, `\infer`, `\frac`, or
  `\dfrac` occurrences; the only P12 proof is the annex item, and imported
  Resolution/STLC rules remain on real registry sheets.
- P12 audit/status generation: **PASS** -- 49 generated audit entries and
  exactly eight `main.hbstatus` P12 lines; the local status-route table lists
  the same eight results once each.
- Symbol/bibliography generation: **PASS** -- 33 P12-scoped/first-use symbol
  rows and all 24 new verified intake keys are present in the canonical files.
- P12 content review: **PASS** -- the independent content verifier accepted
  the source-span accounting, exact theorem hypotheses, proof status,
  row/stub dispositions, and source-specific syntax after the correction pass.
  This is agent review, not human mathematical verification.
- P12 standards review: **PASS** -- the independent standards verifier
  accepted definition-before-use, register/rule-sheet discipline,
  cross-references, citations, and verification-category separation after the
  correction pass.  This is agent review, not human verification.
- Final `python tools/check.py --tree handbook --strict`: **PASS** -- 566
  symbol rows (527 distinct glyphs), 476 bibliography entries (two
  pre-existing intake stubs), 153 proved / 49 sketched / 267 cited / zero
  malformed status forms, and 48 handbook stubs in total, including exactly
  ten in P12; all hard checks passed.
- `python tools/check.py --tree source`: **PASS** -- all hard checks passed;
  185 source result environments, 126 with status markers.  The live source
  blob and `v1.1-verified:source/formal-logic-reference.tex` both have Git
  object hash `ea8c2fa647a387817171468199f989b30de6bdf6`.
- Final text-tree integrity: **PASS** -- `git diff --check 9824e1f -- .
  ':(exclude)handbook/main.pdf'` reports no finding, and
  `git diff --exit-code -- source` confirms that the frozen source tree is
  unchanged.  `tools/symbols2tex.py` and `tools/audit_tables.py` generated the
  integrated tables before the final build.
- Final integrated TeX Live 2025 build: **PASS** -- the authoritative
  `handbook/main.pdf` has 847 pages, 4,497,636 bytes, filesystem timestamp
  2026-08-11 17:10:29 -07:00, and SHA-256 digest
  `789CFAD10165CE2511DD575F75922EE5509E4277AC71D8214CC1100D5F632A51`.
  The final log says `Output written on main.pdf (847 pages, 4497636 bytes)`
  and has zero error, undefined-control-sequence, undefined-reference, or
  undefined-citation diagnostics.  Nonfatal global box diagnostics remain;
  their visible consequence is a visual-review question, not a build failure.

## Visual evidence

- Final visual verdict: **PENDING -- [insert PASS or BLOCKED]**.
- Artifact identity checked by the renderer: **PENDING -- [confirm the
  847-page PDF and SHA-256 above]**.
- P12 title/body physical page range inspected: **PENDING -- [insert exact
  inclusive range and page count]**.
- P12 annex and audit-register physical page ranges inspected: **PENDING --
  [insert exact inclusive ranges and page counts]**.
- P12-relevant symbol-table pages inspected, including the split
  Barendregt/lambda-cube and semantic-resolution rows: **PENDING -- [insert
  exact pages and findings]**.
- Dense tables/figures inspected: **PENDING -- [insert exact pages for A-105,
  A-107, A-108, A-149, the lambda-cube table, landmark table, release audit,
  and A-189 routes]**.
- Former header-only blank versos and part-title versos inspected after the
  shared `emptypage` change: **PENDING -- [insert exact pages and outcome]**.
- Clipping, overlap, broken glyph, malformed stub, running-head, footer,
  landscape, table, and link verdict: **PENDING -- [insert findings]**.
- Human mathematical verification: **NOT PERFORMED**.

This record must not be frozen, and its overall verdict must not be changed to
final `PASS`, until every visual placeholder above is replaced by evidence
from the authoritative PDF identified in the mechanical section.

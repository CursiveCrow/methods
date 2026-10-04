# Part 12 evidence and migration ledger

> **SUPERSEDED AS A WRITING PLAN (2026-08-12).** The full-compendium
> transcription contract revokes this ledger's compact migration, rehoming,
> conversion, retirement, selection, and synthesized-taxonomy instructions.
> Its locators and bibliography are audit leads only. Each inherited unit must
> be restored in full, and each external presentation must be separately
> reconstructed from its own authority.

**Status:** FROZEN / writer-ready, 2026-08-11
**Scope:** Phase-4 Part 12 only. This note is evidence and migration planning; it
does not authorize changes to `source/`, the registers, shared bibliography or
symbol files, generated files, or the handbook drivers.

## 1. Binding controls

The following sources control this visit, in this order:

1. the Phase-4 handover and its fixed status, rule-sheet, notation, and register
   honesty rulings;
2. `handbook/CONVENTIONS.md`;
3. the live CSV registers;
4. the verified source `source/formal-logic-reference.tex`, especially lines
   14095--15091 and the release-checklist material at 16743--16801;
5. primary papers, standard monographs, and exact-version official manuals.

The local `AGENTS.md` gate applies at every first introduction of a technical
name: necessity, exact definition or explicit axiom, standing, nonredundancy,
and later use must occur together. An owed future artifact is named by its
register row instead of being given a speculative technical vocabulary.

### Proof-length ruling

The 40--60 percent band in the handover is only an advisory/reportable target
for an inherited **complete Tier-2 proof**. It is not an authority to tune a
proof to a ratio. It does not apply to sketches, cited results, new proofs, or
retired material. Completeness, exact hypotheses, and load-bearing steps control
over length. A writer may exceed the band without apology when the proof needs
the space; a writer may not delete a step merely to enter the band.

### Phase conflict ruling

The live depth register marks CDCL, Martelli--Montanari unification, and
superposition as `must`, but the binding Phase-4 handover expressly defers those
three full entries to Phase 5. Phase 4 must therefore:

- preserve the inherited DPLL, elementary unification, and resolution core;
- give row-named stubs for the deferred full entries;
- keep those depth/new-content rows `open`;
- deliver independent Phase-4 apparatus only where it does not masquerade as
  the deferred full entry; and
- report the conflict rather than silently marking a partial survey `done`.

## 2. Register inventory and dispositions

### 2.1 Depth rows: exactly 11

| ID | Ceiling / priority | Literal owed artifact | Phase-4 disposition | Completion test |
|---|---|---|---|---|
| D-P11-001 | E / must | CDCL: clause learning, watched literals, restarts, DRAT proofs | **OPEN stub**, paired with N-c-032 | A real E-level CDCL entry exists, with an exact transition system or algorithm, learned-clause invariant, conflict analysis/backjump account, termination/status boundary, certificates, citations, and any displayed rules on a real sheet. A feature table alone does not close it. |
| D-P11-002 | E / must | Martelli--Montanari algorithm with the unification theorem | **OPEN stub**, paired with N-c-035 and A-106 | Exact transformation system, invariant, termination proof, success/failure correctness, MGU factorization theorem, occurs check, and variants boundary all exist. The inherited elementary procedure and P2 sketch do not close it. |
| D-P11-003 | S / must | superposition calculus: rules, KBO/LPO, redundancy, completeness statement | **OPEN stub**, paired with N-c-036 | A named exact equality calculus exists on a real sheet; ordering, eligibility, redundancy and saturation hypotheses are stated; the completeness statement names that calculus and its exact assumptions. Generic prose about superposition does not close it. |
| D-P11-004 | S / should | ordered, hyper-, semantic, set-of-support resolution, subsumption | **fill at S** | Each refinement is exactly distinguished as inference restriction, inference family, search strategy, or contraction/redundancy operation; at least one soundness/completeness boundary and a real citation accompany the comparison. No new rules appear in the body. |
| D-P11-005 | S / should | Nelson--Oppen combination and DPLL(T) | **fill at S**; N-c-034 remains open | The survey states the quantifier-free, signature-disjointness, equality/shared-sort, stable-infiniteness, and convexity/case-split boundaries, and distinguishes a DPLL(T) architecture from a complete calculus. It does not claim the E-level proof owed by N-c-034. |
| D-P11-009 | S / should | BDDs, QBF, #SAT, MaxSAT | **fill at S** | Each problem/object is defined; BDD order dependence and reduced ordered canonicity are separated; QBF is linked to the existing P4 result; #SAT is distinguished from decision SAT; MaxSAT is identified as optimization (with a decision threshold form when complexity is stated). |
| D-P11-011 | T / should | prover/proof-assistant landscape | **fill at T** | A table includes Lean, Rocq, Isabelle, Agda, HOL Light, HOL4, PVS, Mizar, ACL2, and Metamath, with foundation, checking architecture, automation/trust path, pinned version or retrieval date, and an explicit non-equivalence caveat. |
| D-P11-012 | S / should | MLTT/CIC: universes, inductives, W-types, two equalities, extraction | **fill at S**, coordinated with N-c-031 and P7 | The survey defines each listed distinction, points to P7 for formal calculi, and does not identify Lean's foundation with Rocq's pCIC. Extraction remains scoped separately from N-c-039. |
| D-P11-013 | P / could | HoTT/univalence pointer | **OPEN row-named stub** | Phase-4 handover requires `could` rows to remain explicit stubs. A future pointer must name the target part/source and make no technical claim beyond its P ceiling. |
| D-P11-014 | S / should | LCF architecture and de Bruijn criterion | **fill at S**, paired with N-c-038 | LCF's abstract theorem type/kernel discipline and independently checkable proof-object discipline are defined apart; the table never infers the de Bruijn criterion merely from the marketing label “small kernel.” |
| D-P11-015 | T / could | landmark formalizations table | **fill at T by explicit handover selection** | Rows for Four Color, Odd Order, Flyspeck, CompCert, and seL4 give exact formal result, assistant, foundation/trust boundary, primary source, and do not inflate a component theorem into whole-system correctness. |

Depth done-candidates after verification: D-P11-004, 005, 009, 011, 012,
014, 015. Open after Phase 4: D-P11-001, 002, 003, 013.

### 2.2 New-content rows: exactly 10

| ID | Ceiling / priority | Literal owed artifact | Phase-4 disposition |
|---|---|---|---|
| N-c-031 | S / should | lambda cube/PTS; CoC/CIC in assistant foundations | Fill only as a precise survey coordinated with D-P11-012. Correct the register shorthand: Rocq implements pCIC; Lean is not “Coq/CIC under another name.” |
| N-c-032 | E / must | CDCL, UIP, watched literals, restarts, VSIDS, DRAT | OPEN stub by the binding handover. A-105/A-149 may be delivered as apparatus without closing this E row. |
| N-c-033 | T / should | 2-SAT/Horn; random k-SAT pointer | Fill by cross-reference to the already delivered P2 tractability table/theorems plus a citation-bounded random-k-SAT pointer. Do not duplicate the P2 proofs. |
| N-c-034 | E / must | SMT internals, DPLL(T), EUF, simplex, Nelson--Oppen proof | OPEN stub. The S-level D-P11-005 survey and A-107 catalog are not the E entry or proof. |
| N-c-035 | E / must | deep unification, MM proof, equational/AC and higher-order boundary | OPEN stub. Point to the P2 elementary unification method and sketch, but do not relabel either as Martelli--Montanari completeness. |
| N-c-036 | S / must | ordered resolution/superposition saturation and model-construction sketch | OPEN stub. The source warning and a descriptive paragraph are not an exact calculus. |
| N-c-037 | E / must | term rewriting, Newman, critical pairs, completion, LPO/KBO | OPEN Phase-5 stub: not selected as a Phase-4 core by the handover. No invented rewrite calculus or proof. |
| N-c-038 | S / should | LCF/kernels, proof terms/scripts, TCBs, reflection | Fill at S with D-P11-014 and the inherited mechanization material. |
| N-c-039 | S / could | program extraction | OPEN row-named stub. A brief mention in a landscape table does not close it. |
| N-c-040 | P / could | hammers and proof reconstruction | OPEN row-named stub, with later home and sources named. |

New-content done-candidates after verification: N-c-031, N-c-033, N-c-038.
Open after Phase 4: N-c-032, 034, 035, 036, 037, 039, 040.

### 2.3 Apparatus rows

The following rows are the exact Phase-4 apparatus dependencies for P12. Some
were already delivered canonically in P2 and must be referenced, not copied.

| ID | Priority | Literal completion test | P12 action / honest status |
|---|---|---|---|
| A-030 | should | Horn, dual-Horn, 2-SAT, XOR-SAT with algorithm and complexity | Already delivered at `tab:p02-tractable-sat`; P12 cross-references it. Do not create a second master table. |
| A-105 | must | DPLL versus CDCL with learning, watched literals, restarts, DRAT | Deliver a sourced comparison table. Mark A-105 done only if every named column is present. This table does **not** close N-c-032/D-P11-001. |
| A-106 | must | MM transformation rules, occurs check, MGU theorem | OPEN because the exact algorithm is expressly deferred. A body table of rules would violate both the deferral and rules-only-in-registry. Stub A-106 with D-P11-002/N-c-035. |
| A-107 | must | EUF, arrays, bit-vectors, arithmetic with decidability, complexity, Nelson--Oppen conditions | Deliver. Every row must distinguish theory/fragment and must say `not applicable` rather than falsely mark a non-stably-infinite or non-disjoint combination as combinable. |
| A-108 | must | Lean, Rocq, Isabelle, Agda, HOL Light/HOL4, PVS, Mizar, ACL2 by foundation/kernel/de Bruijn | Deliver with pinned official sources. The “de Bruijn” column must use declared criteria, not an unexplained yes/no. |
| A-121 | should | resolution refutation as a DAG to the empty clause | Already delivered at `fig:p02-resolution-dag` and `fig:p02-fol-resolution-dag`; link to the appropriate one. |
| A-149 | must | conflict implication graph with learned clause and backjump level | Deliver a self-contained, source-backed figure even while the full CDCL E entry remains stubbed. Define node/edge/decision-level roles at the figure. |
| A-182 | must/global | per-domain bibliography intake | P12 contributes verified keys. The global row remains open until all domains are merged and checked. |
| A-186 | must/global | per-part further reading | Deliver a P12 further-reading section. The global row closes only when every part has one. |
| A-189 | should/global | body to sheets/appendix/registry navigation | P12 must link DPLL to its annex, resolution to P2 and `sheet:resolution-fol`, typed examples to P7 and `sheet:stlc`, and notation/rules to their registries. Global closure remains a finalizer decision. |

There is no CSV apparatus row for the release-audit checklist, but the handover
explicitly requires its conversion to a table. It is therefore an inherited
source deliverable, not an optional decorative table.

## 3. Complete source accounting

| v1.1 lines | Source unit | Physical handbook home | Disposition |
|---|---|---|---|
| 14095--14270 | constructing derivations, countermodels, and metatheoretic proofs | `parts/p12/formal-workflow.tex` | Retain as compact `hbmethod` entries and one failure-classification table. A method is not a rule or proof. |
| 14271--14350 | DPLL core and correctness | `parts/p12/sat-and-certificates.tex`; `annex/p12/sat-and-certificates.tex` | Migrate. This is the sole new inherited P12 proof-annex item. |
| 14351--14399 | equivalence/equisatisfiability and Tseitin example | P2 canonical definition/result; P12 pointer/audit example | Do not duplicate `def:p02-equisatisfiability` or `thm:p02-tseitin`. Retain only the automation-specific “preserves equivalence or equisatisfiability?” gate. |
| 14401--14434 | elementary unification restatement/examples | P2 canonical unification entry; P12 pointer | Do not duplicate. The deeper MM obligation remains a named P12 stub. |
| 14435--14479 | FOL resolution rule, soundness proof, cited completeness | P2 canonical theorem/annex and `sheet:resolution-fol`; P12 search-method pointer | Do not redisplay rules or duplicate annex proofs. This source unit is accounted for by explicit rehoming. |
| 14480--14495 | equality/superposition warning | `parts/p12/first-order-automation.tex` | Retain the equality boundary; point to the N-c-036/D-P11-003 stub. |
| 14496--14521 | basic SMT, SMT-LIB, TPTP | `parts/p12/smt-and-exchange-formats.tex` | Migrate with exact versions/retrieval dates and input/trust audit. |
| 14522--14560 | SAT/FOL complexity and automated-result audit | P4 canonical theorems plus P12 method | Cross-reference existing results; retain the practical-status/audit method. |
| 14562--14589 | three automation exercises | examples/pointers listed in section 5 | Retire exercise format; migrate only the reusable examples. |
| 14591--14728 | mechanized proof checking | `parts/p12/interactive-proof.tex` | Migrate definitions, audit methods, landscape, and one P7-linked typed example. |
| 14729--15029 | writing and typesetting formal logic | `parts/p12/formal-workflow.tex` | Compress to method boxes and audit tables. Do not migrate raw proof/rule displays. |
| 15030--15091 | research workflow and reproducibility | `parts/p12/formal-workflow.tex` | Migrate status, counterexample-first, computational supplement, and independent-review controls. |
| 15095--15206 | registered notation appendix | P1 symbol registry | Deliberately retire the duplicate from P12; link to P1/generated symbols. |
| 15207--15239 | binding and precedence appendix | P1 precedence chapter | Deliberately retire the duplicate from P12. |
| 15240--15488 | rule sheets | calculus registry and P14 sheet index | Deliberately retire body copies; every live rule comes from the registry. |
| 15489--15637 | qualifying problems/selected solutions | cross-part entries; no printed exercise chapter | Retire as assessment apparatus. Link to the canonical P2/P3/P5/P7/P8 entries if pedagogically useful. |
| 15638--16742 | exercise feedback | no printed exercise chapter | Retire globally; selectively convert only the nine P12 examples below. No “solution” status is silently upgraded. |
| 16743--16801 | release checklist | `parts/p12/formal-workflow.tex` | Convert to a release-gate table with verification categories separated. |
| 16803--end | manual bibliography/backmatter | `handbook/bib/handbook.bib` and normal main driver | Retire the hand-maintained bibliography copy. |

## 4. Source result, evidence, and proof-length map

### 4.1 Eligible inherited results

| Source result | v1.1 evidence | Detexed proof size | Handbook disposition |
|---|---|---:|---|
| Correctness of displayed DPLL core, 14328--14349 | complete proof | 144 words; advisory 40--60% observation 57--87 words | `proved=annex:p12.sat.1`. Preserve residual-clause invariant, terminal SAT case, two-way branching equivalence, and finite-variable termination. Exceed the observation band if needed. |
| Resolution/factoring soundness, 14455--14468 | complete proof | 61 words; advisory observation 24--37 words | Already canonically migrated as `thm:p02-fol-resolution-soundness`, `proved=annex:p2.fol.res.4`. P12 links it; no second theorem or annex item. |
| Sample semantic implication in a LaTeX listing, 14882--14894 | complete illustrative proof | 33 words; advisory observation 13--20 words | Retire as a theorem. It illustrates source/render auditing and has no nonredundant P12 theorem role. Use an existing statused theorem as the audit target instead. |

Counts above exclude the proof-environment delimiters and count alphanumeric
tokens after `detex`; the displayed band uses floor at 40 percent and ceiling
at 60 percent.  No ratio applies to any item below.

### 4.2 Cited or rehomed claims

| Claim | Required status/home |
|---|---|
| First-order resolution refutational completeness | P12 cites/links `thm:p02-fol-resolution-completeness` and records its equality-free, finite-clause, fresh-ground-term, factoring, and sketch boundary. It may not relabel it complete. |
| Tseitin transformation | Link `thm:p02-tseitin`; state expanded-signature equisatisfiability, not same-signature equivalence. |
| SAT is NP-complete | Link `thm:p04-cook-levin` or `thm:p02-sat-np-complete`; historical citation `Cook1971`. Do not create a third theorem. |
| First-order validity is undecidable and computably enumerable | Link `thm:p04-fol-validity-undecidable` (`cited=Church1936`) and `thm:p04-fol-validity-ce` (`proved=annex:p04-hierarchy.1`), with `Turing1937` in historical prose. |
| Resolution refinements | New S-level cited comparison; no proof or completeness transfer from unrestricted resolution. |
| Nelson--Oppen and DPLL(T) | New S-level cited survey. N-c-034's E-level proof remains open. |
| 2-SAT/Horn tractability | Link P2 statused results and `tab:p02-tractable-sat`; do not duplicate their proof evidence. |
| LCF/de Bruijn and tool landscape | New cited survey, not a theorem that every listed tool satisfies one trust criterion. |

### 4.3 Exact complexity and practical-status statements

The SAT statement should be the existing encoded-language theorem: under the
fixed effective propositional encoding, `\mathsf{SAT}` is NP-complete under
polynomial-time many-one reductions.  It does not say that every instance is
hard, that DPLL takes exponential time on every input, or that
`\mathsf P\ne\mathsf{NP}`.  The practical conclusion is conditional: a
deterministic polynomial-time algorithm for all SAT instances would prove
`\mathsf P=\mathsf{NP}`; the observed success of modern solvers on structured
instances neither proves nor refutes that equality.  Link the existing P2/P4
result and cite `Cook1971`.

The first-order statement should likewise retain its scope.  Under the fixed
effective coding, unrestricted first-order validity is computably enumerable
but undecidable.  Hence a sound complete proof search may run forever on an
invalid input, while no total procedure decides validity for every input.  This
does not transfer without proof to every fixed signature or decidable fragment,
and a timeout is not a countermodel.  Link
`thm:p04-fol-validity-undecidable` and `thm:p04-fol-validity-ce`, citing
`Church1936` and recording `Turing1937` only at its supported historical
role.

### 4.4 DPLL fidelity packet

The exact Phase-4 DPLL object is the source's displayed logical core, not an
unbounded package of modern SAT heuristics.

- Input: a finite set of finite propositional clauses and the fixed set of
  variables occurring in the original input.
- State: a residual clause set plus a consistent partial valuation of original
  variables.
- Unit step: assign the literal forced by a unit clause, remove satisfied
  clauses, and remove falsified complementary literals from the rest.
- Success terminal: no residual clauses; extend the partial valuation
  arbitrarily to all remaining original variables and return that total model.
- Failure terminal: an empty residual clause.
- Branch: choose a previously unassigned original variable and search both
  truth values.
- Invariant: every removed original clause already has a true literal; each
  retained clause is exactly its residual after deleting literals made false.
- Termination: every propagation or branch assigns a previously unassigned
  variable; the original variable set is finite.
- Correctness: success yields a total satisfying valuation; satisfiability of a
  branch state is equivalent to satisfiability of at least one child; exhaustion
  yields unsatisfiability.

The source describes pure-literal elimination as optional prose, but its
displayed pseudocode and proof do not use it. The theorem title and statement
must therefore say “displayed logical core.” If pure-literal elimination is
included in the algorithm, add a separately supported preservation lemma; do
not pretend the inherited proof covered it.

Recommended unique graph:

- body result: `thm:p12-dpll-correctness`;
- status: `proved=annex:p12.sat.1`;
- annex item: `annex:p12.sat.1`, pointing back only to that result;
- no other P12 theorem points to that annex item.

## 5. Exercise and assessment disposition

### 5.1 The nine P12 exercises

| Source label | Disposition |
|---|---|
| `ex:formal-practice-01` | Convert the two-element FOL countermodel into a compact small-structure-search example. Preserve the one-element impossibility argument. No theorem status. |
| `ex:formal-practice-02` | Replace by a pointer from the metatheorem method to the canonical P2 substitution lemma. Do not reproduce the source's solution sketch. |
| `ex:automated-reasoning-01` | Retain as a worked DPLL/unit-propagation trace ending in an empty clause. State that the trace certifies only this instance. |
| `ex:automated-reasoning-02` | Retain as the occurs-check boundary example while pointing to P2 unification. It does not close the MM row. |
| `ex:automated-reasoning-03` | Retain as a clausification audit example, preferably by pointer to P2's clausal pipeline; explicitly mark the Skolem step as expansion/reduct equisatisfiability. Replace source formula `\equiv` by registered formula equivalence. |
| `ex:mechanization-01` | Fold into one propositions-as-types example linked to P7 and `sheet:stlc`. Use P7 type metavariables and type arrow; do not display typing rules. |
| `ex:mechanization-02` | Fold into an encoding-audit comparison row. The source only sketches the adequacy obligations, so P12 must not label either adequacy theorem proved. |
| `ex:latex-style-01` | Fold into the formal-writing method: replace vague words by the typed map and exact definition/lemma. Retire exercise and solution. |
| `ex:latex-style-02` | Fold into the notation-release gate and P1 registry pointer. Retire exercise and solution. |

### 5.2 Qualifying and global feedback material

The five qualifying problems and their selected solutions are deliberately
retired as assessment apparatus. Their mathematics is already homed in Parts
2, 3, 5, 7, and 8. The “additional formalization problem” becomes one row in
the mechanized-result audit, not an exercise. The rest of the whole-book
Exercise Feedback chapter is not a P12 deliverable and must not be mined for
unlabelled proof upgrades.

## 6. Candidate physical architecture

The register's chapter homes should remain visible in the physical file split:

1. `parts/p12/sat-and-certificates.tex` — 12.1: inherited DPLL, certificate
   boundary, A-105, A-149, tractable-class pointer, D-P11-009 survey.
2. `parts/p12/smt-and-exchange-formats.tex` — 12.2: inherited SMT/SMT-LIB/TPTP,
   D-P11-005 survey, A-107, N-c-034 stub.
3. `parts/p12/first-order-automation.tex` — 12.3: P2 unification/resolution
   pointers, resolution-search method and refinements, equality boundary,
   MM/superposition stubs.
4. `parts/p12/rewriting.tex` — 12.4: honest N-c-037 Phase-5 stub only.
5. `parts/p12/interactive-proof.tex` — 12.5: mechanization definitions,
   D-P11-011/012/014/015, N-c-031/038, A-108, typed example, stubs 039/040.
6. `parts/p12/formal-workflow.tex` — inherited construction methods,
   writing/typesetting/research workflow, release-audit table.
7. `parts/p12/further-reading.tex` — P12 contribution to A-186.
8. `annex/p12/sat-and-certificates.tex` — the single DPLL annex item.

The finalizer, not a visit writer, owns `parts/p12.tex` and `annex/p12.tex`.
The live Phase-3 skeleton is stale: it says all Part 12 work is Phase 5 and its
annex promises unification and resolution-completeness proofs. Neither promise
matches this handover. The finalizer must replace those stubs; P12 must not
create an unification annex proof or upgrade the cited/sketched resolution
completeness result.

## 7. Construction-method packages

### 7.1 SAT, DPLL, and certificates

Body package:

- reuse P2's clause/CNF/equisatisfiability definitions;
- introduce the exact DPLL state and method only as needed by the theorem;
- preserve the finite-input-variable set and total-model return condition;
- give the worked unit-propagation trace;
- place A-105 and A-149 nearby but label the full CDCL entry as deferred;
- link SAT complexity to P2/P4 statused results; and
- distinguish solver output, a model, and an independently checked UNSAT proof.

CDCL apparatus boundaries:

- an implication-graph node is an assigned literal annotated by decision level;
- a directed edge records the antecedent clause literals that forced an implied
  assignment;
- a conflict node records a falsified clause;
- a cut/UIP explanation produces an entailed learned clause;
- the backjump level is the greatest decision level among the learned clause's
  nonasserting literals (or zero if none);
- watched literals are a propagation data structure, not a logical inference;
- restart policies change search, not the set of clauses entailed by the input;
- DRAT is a proof-logging format/checking discipline, not proof of solver code.

Those definitions are enough for A-105/A-149, but not enough for N-c-032.

### 7.2 First-order resolution and unification

Canonical dependencies already exist:

- `def:p02-fol-simultaneous-substitution`;
- `def:p02-fol-instance-preorder`;
- `def:p02-fol-mgu`;
- `def:p02-fol-unification-procedure`;
- `thm:p02-fol-unification` (sketched);
- `thm:p02-fol-resolution-soundness` (proved);
- `thm:p02-fol-resolution-completeness` (sketched);
- `sheet:resolution-fol`; and
- `fig:p02-fol-resolution-dag` / `fig:p02-resolution-dag`.

P12's nonredundant job is a search/construction method: standardize parents
apart, select eligible literals under the chosen refinement, call the exact
unifier, record the sheet rule instance, contract only under declared
redundancy operations, and maintain a derivation/proof object. It must not
redisplay Resolution or Factoring.

Resolution-refinement taxonomy:

| Name | Standing | Required boundary |
|---|---|---|
| ordered resolution | restriction on eligible pivots/literals by a fixed admissible ordering and selection function | Completeness needs the precise ordering/selection/fair-saturation hypotheses. |
| hyperresolution | multi-premise resolution family with a nucleus and electrons | It is not merely “several binary steps” unless an exact simulation theorem is cited. |
| semantic resolution | restriction guided by a fixed interpretation/semantic clash | The guiding interpretation is a search device; the final clauses remain syntactic consequences. |
| set of support | search strategy requiring at least one parent from a designated support set | Completeness requires the initial partition/consistency condition and fair use, not the name alone. |
| subsumption | contraction/redundancy deletion when one clause has an instance contained in another | It removes search states; it is not a new consequence-generating rule. |

Primary anchors are Robinson 1965, Wos--Robinson--Carson 1965, Slagle 1967,
and Bachmair--Ganzinger 2001. Do not transfer a completeness theorem among
these variants without its hypotheses.

### 7.3 SMT, DPLL(T), and exchange formats

The inherited SMT definition is sound as a starting point: relative to a fixed
background theory T, ask whether T together with the existential closure of the
input is satisfiable. The entry must also say which fragment, sorts, signatures,
and command semantics are active.

S-level DPLL(T) architecture:

1. Boolean abstraction assigns propositional proxies to theory atoms.
2. A SAT engine proposes a Boolean assignment.
3. A theory solver checks consistency of the selected theory literals.
4. A theory conflict yields a theory-valid conflict clause; theory propagation
   may yield further entailed literals.
5. The Boolean engine learns/branches until a theory-consistent assignment is
   found or the abstraction is refuted.

This is an architecture description, not the N-c-034 calculus or proof.

Nelson--Oppen boundary:

- input is quantifier-free after purification into component signatures;
- component signatures are disjoint apart from equality and declared shared
  sorts;
- each component has a decision procedure for its quantifier-free fragment;
- components are stably infinite over the shared sorts for the standard
  completeness theorem;
- equality arrangements over shared variables must be communicated;
- convex theories can communicate single implied equalities; nonconvex
  theories require disjunctive case splits/arrangements; and
- fixed-width bit-vector theories are not stably infinite, so the ordinary
  Nelson--Oppen check must say “not directly applicable.”

The standard survey explicitly states that disjointness alone gives soundness,
while stable infiniteness supplies the usual completeness condition
([Barrett--Tinelli survey](https://theory.stanford.edu/~barrett/pubs/BT18.pdf)).

A-107 minimum rows:

| Theory/fragment | Decidability/complexity field | Combination field |
|---|---|---|
| EUF, quantifier-free | decidable by congruence closure; state implementation complexity only if sourced under a fixed representation | stably infinite; standard Nelson--Oppen component |
| extensional arrays | name the precise quantifier-free array theory and whether extensionality is present | do not give one blanket answer for every array extension; state the selected theory's combination conditions |
| fixed-width bit-vectors | finite and decidable; bit-blasting is a reduction method, not a semantic definition | not stably infinite at fixed width; ordinary Nelson--Oppen does not apply directly |
| linear rational/real arithmetic | decidable; state the selected fragment | convex and stably infinite in its standard form |
| linear integer arithmetic | decidable but nonconvex | stable-infinite combination needs equality case splitting; do not label it convex |

SMT-LIB and TPTP are interfaces/formats, not logics by themselves. Pin the
SMT-LIB version and TPTP grammar revision; audit declaration scopes, formula
roles, conjecture polarity, imported axioms, result token, model/proof artifact,
resource limits, and independent checker.

### 7.4 Mechanized proof, LCF, and the de Bruijn criterion

Retain and tighten the source definitions of proof term, kernel, elaboration,
tactic, trusted base, deep embedding, and shallow embedding. At each first use,
state the category and the nonredundancy distinction. In particular:

- a tactic constructs a candidate theorem/proof; it is not a primitive rule
  when its output is checked;
- an elaborator expands surface syntax into kernel input; correctness of the
  elaborator is not automatically kernel soundness;
- a kernel is an implementation component relative to one foundation;
- a trusted base is result- and workflow-specific, not a product name;
- a deep embedding retains object syntax; a shallow embedding reuses host
  operations and needs a separate fidelity/correspondence argument.

Define **LCF architecture** here as the programming discipline in which values
of an abstract theorem type can be constructed only by a small set of trusted
primitive inference functions; untrusted tactics compose those functions. This
is supported by Gordon--Milner--Wadsworth 1979.

Define the handbook's operational **de Bruijn criterion** before using a table
cell: a claimed proof should be reducible to a fully explicit object accepted
by a small, independently inspectable or independently implementable checker
for the declared formal system. This is an operational trust criterion, not a
claim that de Bruijn used this exact later phrase. Cite de Bruijn's AUTOMATH
paper and Pollack's trust analysis.

LCF and de Bruijn are not synonyms. An LCF-style abstract theorem datatype may
protect an interactive session without exporting a portable proof object; an
independently checkable certificate may satisfy the operational de Bruijn
criterion without using LCF architecture.

Landscape table caution:

- Rocq: polymorphic cumulative calculus of inductive constructions; proof terms
  checked by a kernel. Cite the exact Rocq manual and Paulin--Mohring.
- Lean 4: dependent type theory with inductives, universes, quotient/proof
  irrelevance features as documented by the exact Lean reference; do **not**
  call it Rocq's CIC.
- Isabelle: generic logical framework; `Isabelle/HOL` is a particular object
  logic. Distinguish framework kernel from object-logic proof methods.
- Agda: dependent type theory with version-dependent options (cubical,
  rewriting, sized types, etc.); the table must name enabled options.
- HOL Light/HOL4: LCF-family proof assistants for classical higher-order logic;
  external oracles must be separately reported.
- PVS: higher-order logic with dependent predicate subtypes and integrated
  automation; do not infer an exportable proof certificate without evidence.
- Mizar: first-order set-theoretic foundation over Tarski--Grothendieck set
  theory in the MML; its verifier architecture is not an LCF theorem datatype.
- ACL2: first-order logic of total recursive functions with an executable
  applicative Lisp subset; it is not a dependent type theory.
- Metamath: the database declares its formal system; the verifier checks explicit
  substitutions/steps and is not intrinsically tied to ZFC.

Current official sources used for these boundaries include the
[Agda 2.8.0 language reference](https://agda.readthedocs.io/en/stable/language/index.html),
[HOL Light site](https://hol-light.github.io/),
[HOL4 description](https://hol-theorem-prover.org/about),
[PVS 7.1 documentation](https://pvs.csl.sri.com/documentation.html),
[Mizar library foundation page](https://wiki.mizar.org/library/),
[ACL2 documentation portal](https://acl2.org/), and
[Metamath's verifier description](https://us.metamath.org/). Pin versions or
retrieval dates in the bibliography at implementation time.

### 7.5 Type-theory boundary

N-c-031/D-P11-012 are survey obligations, not permission to display a new PTS,
MLTT, CoC, CIC, or Lean calculus in P12. Formal surfaces live in P7 or on future
registry sheets. The P12 survey should define:

- a pure type system by its sorts, axioms, and permitted dependent-product
  formation triples;
- the lambda cube as the eight two-sort PTS choices generated by term/type
  dependency and polymorphism axes;
- CoC as the strongest cube corner, not CIC;
- CIC/pCIC as CoC extended by precisely controlled inductive definitions,
  universe/cumulativity machinery, and eliminations;
- definitional equality as the kernel's conversion relation and propositional
  equality as an inhabitant of an identity/equality type; and
- W-types as well-founded tree types, while noting that a particular assistant
  may expose inductives rather than a primitive W-type constructor.

Use Barendregt 1992, Coquand--Huet 1988, Paulin--Mohring 1993/2015, and exact
assistant manuals. Do not claim a blanket normalization/decidability theorem
for “MLTT/CIC” as a family. Program extraction is only a pointer/stub here
unless N-c-039 is separately filled at S.

### 7.6 Formal writing and release workflow

Compress the source's formal-practice, writing, typesetting, and reproducibility
chapters into lookup methods, not motivational prose. Required method entries:

- backward/forward derivation search;
- propositional countervaluation search;
- small-structure countermodel search;
- metatheorem proof-plan audit;
- automated-result audit;
- encoding audit;
- mechanized-result report;
- source/render/cross-reference audit; and
- counterexample-first independent review.

The release-checklist table must separate at least these evidence classes:

| Gate | Establishes | Does not establish |
|---|---|---|
| status/static checks | label/status/sheet/register invariants | theorem truth or proof completeness |
| clean compilation | TeX integration and reference/bibliography resolution | mathematical correctness |
| source fidelity review | agreement with v1.1/source statement | correctness of new mathematics |
| mathematical review | hypotheses and argument validity for sampled/checked claims | clean typesetting |
| rendered-page inspection | visible layout, glyph, table, and link correctness | source semantics by itself |
| certificate/kernel check | acceptance in the declared formal checker | fidelity of definitions to informal intent |
| human pedagogical review | usability and explanatory adequacy | exhaustive formal correctness |

No proof or rule schema may appear in this body chapter. The source's sample
proof listing and raw universal-introduction derivations are retired; replace
them with pointers to an existing statused theorem and its registered sheet.

## 8. Real-sheet requirements

### Reuse now

- `sheet:resolution-fol`: exact Resolution and Factoring, including all five
  `\hbrule` arguments and the renaming-apart/MGU side conditions.
- `sheet:resolution-cpl`: propositional resolution, used by the existing A-121
  DAG.
- `sheet:stlc`: typed propositions-as-types example, through the P7 entry.
- existing P2 tableaux sheets for classical tableau pointers; no P12 copy.

### No new Phase-4 sheet needed

- DPLL as presented here is an algorithmic `hbmethod`, not an inference-rule
  calculus.
- SMT-LIB/TPTP are format entries, not calculi.
- the LCF/de Bruijn and landscape material is architectural prose/tables.
- a PTS/CIC survey can point to P7 without displaying rules.

### Deferred sheets required before later rows can close

- an exact MM transformation sheet (suggested label `sheet:unification-mm`) if
  transformation rules are displayed;
- an exact ordered-superposition-with-equality sheet (suggested label
  `sheet:superposition-fol-eq`);
- an exact abstract CDCL transition sheet only if the future E entry displays
  transition rules rather than pseudocode;
- an exact DPLL(T) transition sheet only if the future E entry displays a
  calculus; and
- a term-rewriting sheet if N-c-037 presents rewrite inference schemata.

Names above are suggested physical interfaces, not technical vocabulary for
the Phase-4 body. They remain owed artifacts until their five-part definition
gate and exact source are supplied.

## 9. Exact stub and exclusion ledger

Required P12 row-named stubs:

1. `D-P11-001 / N-c-032` — full CDCL entry.
2. `D-P11-002 / N-c-035 / A-106` — MM algorithm and theorem.
3. `D-P11-003 / N-c-036` — exact superposition calculus.
4. `N-c-034` — E-level SMT internals/proof beyond the S survey.
5. `N-c-037` — term rewriting chapter.
6. `D-P11-013` — HoTT/univalence pointer, deferred under the `could` rule.
7. `N-c-039` — extraction.
8. `N-c-040` — hammers/proof reconstruction.

The handover also asks P12 to expose Phase-5 boundaries for tableau and model
checking. Use pointer stubs to the actual target rows rather than inventing P12
content:

- `N-c-009` for the ALC tableau procedure in P9;
- `N-c-013` for omega automata/LTL model checking in P9; and
- `N-c-017` for symbolic model checking/BDD-based methods in P9.

Classical CPL/FOL tableaux already live in P2 and are cross-references, not
Phase-5 P12 work. The qualitative model-checking boundary must not be expanded
into excluded probabilistic/stochastic model checking (`N-x-015`).

Other exclusions:

- no full HoTT or univalence development;
- no higher-order unification algorithm or proof beyond the cited boundary;
- no equality-completeness claim for bare resolution;
- no blanket “all SMT” decidability or Nelson--Oppen combinability claim;
- no claim that a solver timeout establishes nonvalidity;
- no claim that a proof assistant validates informal intent merely by kernel
  acceptance;
- no duplicate P2/P4 theorems or proofs; and
- no exercises/qualifying appendix in the printed handbook.

## 10. Defect ledger

### P12-local/crossing defects that this visit can substantively resolve

| ID | Acceptance condition | P12 resolution |
|---|---|---|
| R-038 | DPLL proof covers both specification halves or is a labelled sketch | Migrate the repaired v1.1 proof with exact scope as `proved=annex:p12.sat.1`; verify both SAT-model and UNSAT/exhaustion directions. |
| S-014 | 100% status coverage in Parts X--XI/back matter | Every P12 theorem-class result gets exactly one status spec; methods/definitions remain their proper environments. |
| S-018 | every displayed rule has name, label, and side conditions | P12 displays no resolution/unification rules in the body and points to `sheet:resolution-fol`. Deferred MM/superposition rules remain stubs. |
| S-019 | SAT NP-completeness, FOL c.e./undecidable, resolution completeness are labeled/statused/cited | Resolve by canonical cross-references to P2/P4 results, not duplicate P12 theorems. |
| S-022 | release checklist becomes a real release gate | Deliver the categorized checklist table and report verification categories separately. Global closure remains a finalizer decision. |
| L-014 | no paragraph command carries result/status semantics | Use numbered handbook environments; retire paragraph-style exercise solutions and proof markers. |
| L-017 | every listing label resolves | Do not migrate the source's fake label inside `lstlisting`; any retained listing gets a real surrounding caption/label. |

### Global controls, not falsely closeable by P12 alone

- S-017: primary-source/no-zero-citation control. P12 must pass it locally, but
  the defect includes Part-10 primary omissions and closes only globally.
- L-005/L-006: registry-only rule generation. P12 complies locally; global
  closure requires the whole tree.
- A-182/A-189 and the source-regression/build gates remain finalizer work.

## 11. Notation and symbol ledger

### 11.1 Existing rows to reuse or extend

| Existing notation | Required action |
|---|---|
| `\varphi,\psi,\chi` formula metavariables | Use these in P12. Replace the source's local formula `\theta` in the Tseitin example by `\chi`; `\theta` is already a term-substitution metavariable. |
| `\theta,\rho,\eta` term substitutions | Extend/reuse through P12.3. These already have the right role. |
| `\theta_{\mathrm u},\rho_{\mathrm u},\eta_{\mathrm u}` aliases | Preferred normalization: remove or deprecate this P12-only row and use the unadorned registered substitutions after eliminating formula `\theta`. If retained, the body must satisfy the five-part necessity gate; mere source inheritance is not enough. |
| `\operatorname{form}_{\Lang}(C),\operatorname{ucl}_{\Lang}(C)` | Extend the existing row's current P12.2 endpoint through P12.3; do not introduce an un-subscripted competing clause interpretation. |
| `\operatorname{supp}_{\mathrm{var}}`, substitution action/composition, `\preceq_{\mathrm{inst}}`, `\doteq` | Reuse only through pointers/examples; no redefinition. |
| `\mathsf{SAT}` | Merge the duplicate P2.1/P4.6 master rows and extend the one language-role row through P12.1. Do not use it as a solver response token. |
| `\mathsf P,\mathsf{NP},\mathsf{coNP},\mathsf{TQBF}` | Merge the duplicate P2.1/P4.6 rows for the first three classes where applicable, extend the canonical rows through P12.1, and extend TQBF only if the P12 QBF pointer prints the glyph. Keep `P` as a class identifier, not a proposition metavariable. |
| `\operatorname{size}` | Extend the P7.8 bit-length row to the exact P12 chapter if P12 measures encodings. Never use vertical bars for formula/proof/input length; bars are cardinality only. |
| `\alpha,\beta,\gamma` type metavariables | Extend the P7.3--P7.4 type row to P12.5 for the propositions-as-types example; do not reuse the P7.5 ordinal row or the separate P7.6 finite-type row. |
| `\to_{\mathrm{ty}}`, `{:}`, typed `\lambda`, `\Theta_{\mathrm{ty}}`, `\derives_{\mathsf{STLC}}`, and term metavariables `M,N,P` | Extend the corresponding typed-calculus rows to P12.5 only for the exact `sheet:stlc` example. Do not use `A,B,C` as types, raw `\to` as the type former, or an unsubscripted turnstile. |
| formula equivalence `\Leftrightarrow` | Replace source formula `\equiv`; `\equiv` remains elementary equivalence only. |

### 11.2 Candidate new scoped rows if the corresponding notation is actually used

```csv
glyph,macro,role,scope,precedence,first_use,notes
"\(\mathsf{DPLL},\mathsf{CDCL}\)","\mathsf{DPLL},\mathsf{CDCL}",SAT-search method identifiers,P12.1,n/a,P12.1,"DPLL denotes the exact displayed finite-clause procedure; CDCL denotes the deferred conflict-driven family and is not an alias for DPLL."
"\(\#\mathsf{SAT}\)","\#\mathsf{SAT}",satisfying-assignment counting problem,P12.1,n/a,P12.1,"Maps a propositional encoding to its number of satisfying valuations under the fixed variable convention; not a decision language until a threshold question is supplied."
"\(\mathsf{MaxSAT}\)","\mathsf{MaxSAT}",maximum-satisfiability optimization problem,P12.1,n/a,P12.1,"Maximizes the number or declared weight of satisfied clauses; state unweighted/weighted/partial variant locally."
"\(\mathsf{SMT},\mathsf{EUF}\)","\mathsf{SMT},\mathsf{EUF}",SMT problem-family and equality-with-uninterpreted-functions identifiers,P12.2,n/a,P12.2,"SMT is always relative to a declared theory/fragment; EUF is the quantifier-free equality theory used in the exact catalog row."
"\(\mathsf{LCF}\)","\mathsf{LCF}",abstract-theorem-type proof architecture,P12.5,n/a,P12.5,"Architecture defined by trusted primitive constructors of an abstract theorem type; not a logic, foundation, or synonym for the de Bruijn criterion."
"\(\mathsf{PTS},\mathsf{CoC},\mathsf{CIC}\)","\mathsf{PTS},\mathsf{CoC},\mathsf{CIC}",type-system family and source calculus identifiers,P12.5,n/a,P12.5,"Survey identifiers only: a PTS is parameterized by sorts/axioms/product triples; CoC is one PTS; CIC adds controlled inductives and is not Lean's exact kernel theory."
```

Do not add mathematical-symbol rows for literal protocol tokens such as
`sat`, `unsat`, and `unknown` if they appear only as verbatim SMT-LIB strings;
document them as exact code tokens. If the DPLL prose needs an outcome, prefer
“returns a satisfying valuation” and “reports unsatisfiable” over overloading
the existing `\mathsf{SAT}` language glyph.

Local variables for one algorithm state (clause set, partial assignment,
decision level, graph node) may be quantified and typed at occurrence. Do not
register them as book-wide notation. Avoid generic `R` for a verifier relation,
which collides with established relation roles; use prose or an exact scoped
subscripted name only if a later theorem needs it.

## 12. Bibliography and evidence

### 12.1 Existing verified keys to reuse

Inherited core:

- `DavisPutnam1960`, DOI 10.1145/321033.321034;
- `DavisLogemannLoveland1962`, DOI 10.1145/368273.368557;
- `Tseitin1968`, historical 1968 result in the 1983 Springer translation;
- `Robinson1965`, DOI 10.1145/321250.321253;
- `BachmairGanzinger2001`, DOI 10.1016/B978-044450813-3/50004-7;
- `Cook1971`, DOI 10.1145/800157.805047;
- `Church1936`, DOI 10.2307/2371045; and
- `Turing1937`, DOI 10.1112/plms/s2-42.1.230.

SAT/SMT/rewriting sources already present:

- `MartelliMontanari1982`, DOI 10.1145/357162.357169;
- `MarquesSilvaSakallah1999`, DOI 10.1109/12.769433;
- `MoskewiczEtAl2001`, DOI 10.1145/378239.379017;
- `EenSorensson2003` (published 2004), DOI 10.1007/978-3-540-24605-3_37;
- `MarquesSilvaLynceMalik2009`, DOI 10.3233/978-1-58603-929-5-131;
- `WetzlerHeuleHunt2014`, DOI 10.1007/978-3-319-09284-3_31;
- `NelsonOppen1979`, DOI 10.1145/357073.357079;
- `DutertreDeMoura2006`, DOI 10.1007/11817963_11;
- `NieuwenhuisOliverasTinelli2006`, DOI 10.1145/1217856.1217859;
- `DeMouraBjorner2008`, DOI 10.1007/978-3-540-78800-3_24;
- `BarrettSebastianiSeshiaTinelli2009`, DOI 10.3233/978-1-58603-929-5-825;
- `Newman1942`, DOI 10.2307/1968867;
- `Huet1980`, DOI 10.1145/322217.322230;
- `Dershowitz1982`, DOI 10.1016/0304-3975(82)90026-3;
- `BaaderNipkow1998`, DOI 10.1017/CBO9781139172752;
- `AspvallPlassTarjan1979`, DOI 10.1016/0020-0190(79)90002-4;
- `DowlingGallier1984`, DOI 10.1016/0743-1066(84)90014-1; and
- `Bryant1986`, DOI 10.1109/TC.1986.1676819.

Official live-manual keys already present: `SMTLIB2025`, `TPTP`,
`LeanManual2026`, `LeanTPIL`, `DeMouraUllrich2021`, `RocqManual2026`, and
`Isabelle2025`. Their live targets were rechecked on 2026-08-11: SMT-LIB 2.7
release 2025-07-07, TPTP BNF 9.3.0.3, Lean 4.32.1, Rocq 9.1.1, and
Isabelle2025-2. Recheck again at integration because software manuals are
intentionally time-sensitive.  The remaining A-108 tool rows need the new
retrieval-dated official-site keys below.

### 12.2 New verified intake records

```bibtex
@incollection{DeBruijn1970,
  author    = {de Bruijn, N. G.},
  title     = {The Mathematical Language {AUTOMATH}, Its Usage, and Some of Its Extensions},
  editor    = {Laudet, M. and Lacombe, D. and Nolin, L. and Sch{\"u}tzenberger, M.},
  booktitle = {Symposium on Automatic Demonstration},
  series    = {Lecture Notes in Mathematics},
  number    = {125},
  pages     = {29--61},
  publisher = {Springer},
  year      = {1970},
  doi       = {10.1007/BFb0060623},
}

@book{GordonMilnerWadsworth1979,
  author    = {Gordon, Michael J. C. and Milner, Robin and Wadsworth, Christopher P.},
  title     = {Edinburgh {LCF}: A Mechanised Logic of Computation},
  series    = {Lecture Notes in Computer Science},
  number    = {78},
  publisher = {Springer},
  year      = {1979},
  doi       = {10.1007/3-540-09724-4},
}

@incollection{Pollack1998,
  author    = {Pollack, Robert},
  title     = {How to Believe a Machine-Checked Proof},
  editor    = {Sambin, Giovanni and Smith, Jan M.},
  booktitle = {Twenty-Five Years of Constructive Type Theory},
  pages     = {205--220},
  publisher = {Oxford University Press},
  year      = {1998},
}

@book{Harrison2009,
  author    = {Harrison, John},
  title     = {Handbook of Practical Logic and Automated Reasoning},
  publisher = {Cambridge University Press},
  year      = {2009},
  doi       = {10.1017/CBO9780511576430},
}

@incollection{Barendregt1992,
  author    = {Barendregt, Henk P.},
  title     = {Lambda Calculi with Types},
  editor    = {Abramsky, Samson and Gabbay, Dov M. and Maibaum, Thomas S. E.},
  booktitle = {Handbook of Logic in Computer Science, Volume 2: Background: Computational Structures},
  pages     = {118--310},
  publisher = {Oxford University Press},
  year      = {1992},
  doi       = {10.1093/oso/9780198537618.003.0002},
}

@incollection{PaulinMohring2015,
  author    = {Paulin-Mohring, Christine},
  title     = {Introduction to the Calculus of Inductive Constructions},
  editor    = {Woltzenlogel Paleo, Bruno and Delahaye, David},
  booktitle = {All about Proofs, Proofs for All},
  series    = {Studies in Logic (Mathematical Logic and Foundations)},
  number    = {55},
  publisher = {College Publications},
  year      = {2015},
  url       = {https://inria.hal.science/hal-01094195},
}

@inproceedings{PaulinMohring1993,
  author    = {Paulin-Mohring, Christine},
  title     = {Inductive Definitions in the System {Coq}: Rules and Properties},
  editor    = {Bezem, Marc and Groote, Jan Friso},
  booktitle = {Typed Lambda Calculi and Applications},
  series    = {Lecture Notes in Computer Science},
  number    = {664},
  pages     = {328--345},
  publisher = {Springer},
  year      = {1993},
  doi       = {10.1007/BFb0037116},
}

@inproceedings{MitchellSelmanLevesque1992,
  author    = {Mitchell, David G. and Selman, Bart and Levesque, Hector J.},
  title     = {Hard and Easy Distributions of {SAT} Problems},
  booktitle = {Proceedings of the Tenth National Conference on Artificial Intelligence},
  pages     = {459--465},
  publisher = {AAAI Press},
  year      = {1992},
  url       = {https://aaai.org/Papers/AAAI/1992/AAAI92-071.pdf},
}

@article{Valiant1979Enumeration,
  author       = {Valiant, Leslie G.},
  title        = {The Complexity of Enumeration and Reliability Problems},
  journaltitle = {SIAM Journal on Computing},
  volume       = {8},
  number       = {3},
  pages        = {410--421},
  year         = {1979},
  doi          = {10.1137/0208032},
}

@incollection{LiManya2009,
  author    = {Li, Chu-Min and Many{\`a}, Felip},
  title     = {{MaxSAT}, Hard and Soft Constraints},
  editor    = {Biere, Armin and Heule, Marijn and van Maaren, Hans and Walsh, Toby},
  booktitle = {Handbook of Satisfiability},
  pages     = {613--631},
  publisher = {IOS Press},
  year      = {2009},
  doi       = {10.3233/978-1-58603-929-5-613},
}

@article{Slagle1967,
  author       = {Slagle, James R.},
  title        = {Automatic Theorem Proving with Renamable and Semantic Resolution},
  journaltitle = {Journal of the ACM},
  volume       = {14},
  number       = {4},
  pages        = {687--697},
  year         = {1967},
  doi          = {10.1145/321420.321428},
}

@article{WosRobinsonCarson1965,
  author       = {Wos, Lawrence and Robinson, George A. and Carson, Daniel F.},
  title        = {Efficiency and Completeness of the Set of Support Strategy in Theorem Proving},
  journaltitle = {Journal of the ACM},
  volume       = {12},
  number       = {4},
  pages        = {536--541},
  year         = {1965},
  doi          = {10.1145/321296.321302},
}

@online{AgdaReference2026,
  author       = {{The Agda Team}},
  title        = {Agda 2.8.0 Language Reference},
  version      = {2.8.0},
  urldate      = {2026-08-11},
  url          = {https://agda.readthedocs.io/en/stable/language/index.html},
}

@online{HOLLightSite2026,
  author       = {Harrison, John},
  title        = {The {HOL Light} Theorem Prover},
  urldate      = {2026-08-11},
  url          = {https://hol-light.github.io/},
}

@online{HOL4Site2026,
  author       = {{The HOL4 Development Team}},
  title        = {About the {HOL4} Theorem Prover},
  version      = {Trindemossen-2},
  urldate      = {2026-08-11},
  url          = {https://hol-theorem-prover.org/about},
}

@online{PVS71Documentation,
  author       = {{SRI International Computer Science Laboratory}},
  title        = {{PVS} Documentation},
  version      = {7.1},
  urldate      = {2026-08-11},
  url          = {https://pvs.csl.sri.com/documentation.html},
}

@online{MizarLibrary2026,
  author       = {{The Mizar Project}},
  title        = {Mizar System and Mathematical Library},
  version      = {Mizar 8.1.15; MML 5.94.1493},
  urldate      = {2026-08-11},
  url          = {https://wiki.mizar.org/library/},
}

@online{ACL2Documentation2026,
  author       = {{The ACL2 Project}},
  title        = {{ACL2} 8.7 User Manual and Community Books Documentation},
  version      = {8.7},
  urldate      = {2026-08-11},
  url          = {https://acl2.org/doc/},
}

@online{MetamathSite2026,
  author       = {{The Metamath Community}},
  title        = {Metamath Home Page and Verifier Description},
  urldate      = {2026-08-11},
  url          = {https://us.metamath.org/},
}
```

The AUTOMATH metadata is verified against Eindhoven University's publisher
record and DOI; the OUP chapter page gives Barendregt's modern pagination as
118--310; Pollack's published chapter pagination is 205--220. Do not substitute
the 1997 BRICS report for the 1998 book chapter without changing the key and
metadata.

### 12.3 Landmark-formalization records

```bibtex
@article{Gonthier2008,
  author       = {Gonthier, Georges},
  title        = {Formal Proof---The Four-Color Theorem},
  journaltitle = {Notices of the American Mathematical Society},
  volume       = {55},
  number       = {11},
  pages        = {1382--1393},
  year         = {2008},
  url          = {https://www.ams.org/notices/200811/tx081101382p.pdf},
}

@inproceedings{GonthierEtAl2013,
  author    = {Gonthier, Georges and Asperti, Andrea and Avigad, Jeremy and Bertot, Yves and Cohen, Cyril and Garillot, Fran{\c{c}}ois and Le Roux, St{\'e}phane and Mahboubi, Assia and O'Connor, Russell and Ould Biha, Sidi and Pasca, Ioana and Rideau, Laurence and Solovyev, Alexey and Tassi, Enrico and Th{\'e}ry, Laurent},
  title     = {A Machine-Checked Proof of the Odd Order Theorem},
  booktitle = {Interactive Theorem Proving},
  series    = {Lecture Notes in Computer Science},
  number    = {7998},
  pages     = {163--179},
  publisher = {Springer},
  year      = {2013},
  doi       = {10.1007/978-3-642-39634-2_14},
}

@article{HalesEtAl2017,
  author       = {Hales, Thomas and Adams, Mark and Bauer, Gertrud and Dang, Tat Dat and Harrison, John and Hoang, Le Truong and Kaliszyk, Cezary and Magron, Victor and McLaughlin, Sean and Nguyen, Tat Thang and Nguyen, Quang Truong and Nipkow, Tobias and Obua, Steven and Pleso, Joseph and Rute, Jason and Solovyev, Alexey and Ta, Thi Hoai An and Tran, Nam Trung and Trieu, Thi Diep and Urban, Josef and Vu, Ky and Zumkeller, Roland},
  title        = {A Formal Proof of the Kepler Conjecture},
  journaltitle = {Forum of Mathematics, Pi},
  volume       = {5},
  eid          = {e2},
  pagetotal    = {29},
  year         = {2017},
  doi          = {10.1017/fmp.2017.1},
}

@article{Leroy2009,
  author       = {Leroy, Xavier},
  title        = {Formal Verification of a Realistic Compiler},
  journaltitle = {Communications of the ACM},
  volume       = {52},
  number       = {7},
  pages        = {107--115},
  year         = {2009},
  doi          = {10.1145/1538788.1538814},
}

@inproceedings{KleinEtAl2009,
  author    = {Klein, Gerwin and Elphinstone, Kevin and Heiser, Gernot and Andronick, June and Cock, David and Derrin, Philip and Elkaduwe, Dhammika and Engelhardt, Kai and Kolanski, Rafal and Norrish, Michael and Sewell, Thomas and Tuch, Harvey and Winwood, Simon},
  title     = {{seL4}: Formal Verification of an {OS} Kernel},
  booktitle = {Proceedings of the 22nd ACM Symposium on Operating Systems Principles},
  pages     = {207--220},
  publisher = {ACM},
  year      = {2009},
  doi       = {10.1145/1629575.1629596},
}
```

Claim boundaries for A-108/D-P11-015:

- Four Color: a Coq/Rocq formalization of the theorem, not a claim that every
  historical proof was checked.
- Odd Order: a constructive Coq formalization of Feit--Thompson within the
  declared development and libraries.
- Flyspeck: formal proof of the Kepler conjecture using HOL Light and Isabelle
  components; report both assistants and the correspondence/trust boundary.
- CompCert: semantic preservation for the stated compiler/language/targets in
  the cited development, not “all of C compilation is bug-free.”
- seL4: functional correctness from the abstract specification to the stated C
  implementation under explicit compiler, assembler, hardware, and model
  assumptions; not a proof of every security or timing property.

## 13. Verification checklist for the writer and verifier

### Fidelity sample (minimum 12)

The deliberate second pass should include all Tier-1/central method entries and
at least these items:

1. DPLL input/state and variable-set invariant;
2. DPLL success terminal and total valuation;
3. DPLL empty-clause terminal;
4. DPLL branch equivalence and termination;
5. equisatisfiability versus equivalence pointer;
6. unification occurs-check pointer;
7. resolution renaming-apart/MGU sheet pointer;
8. resolution equality/completeness boundary;
9. SMT definition relative to T;
10. SAT NP-completeness/P-v-NP wording;
11. FOL c.e./undecidable practical-status wording;
12. kernel/elaboration/tactic distinction;
13. deep/shallow embedding distinction;
14. trusted-base/result-report method;
15. release-audit verification-category separation.

### Mechanical/static gates

- no body `proof`, `\hbrule`, raw rule fraction, or re-displayed resolution,
  unification, typing, or quantifier rule;
- exactly one P12 annex item and one pointing body result unless an explicitly
  new, separately authorized proof is later added;
- every cited P12 result has a real key; no fabricated manual version;
- every `\hbstub` names its exact row ID(s);
- no `\equiv` for formula equivalence;
- no raw `\vdash`; every derivability judgment names its system;
- no vertical bars for encoding length;
- no source formula metavariable `\theta`;
- no `A,B,C` type metavariables in the typed example;
- all definitions have `\index` tags at their first handbook definition;
- A-030/A-121 are linked, not duplicated;
- P2/P4 canonical theorem labels resolve;
- current tool/manual entries carry versions or retrieval dates;
- scratch compile, normal handbook check, then adversarial statement-by-
  statement comparison against v1.1.

### Register closure gate

Do not mark any row done merely because this research note specifies it. A row
closes only after the physical artifact exists at its ceiling and passes the
visit verification. In particular, the presence of A-105/A-149 does not close
CDCL, the presence of A-107 does not close N-c-034, and the P2 unification
sketch does not close MM/A-106.

## 14. Coverage checksum

- Depth rows covered: **11/11** (`D-P11-001`--`005`, `009`, `011`--`015`).
- New-content rows covered: **10/10** (`N-c-031`--`040`).
- P12 apparatus dependencies covered: **10/10** (A-030, 105--108, 121,
  149, 182, 186, 189).
- P12-local/crossing defect rows covered: **7/7** (R-038, S-014, S-018,
  S-019, S-022, L-014, L-017), with global controls separately identified.
- P12 exercises covered: **9/9**; qualifying/global feedback material has an
  explicit retirement rule.
- Inherited complete proof environments mapped: **3/3**; only DPLL creates a
  new P12 annex item.
- Source/backmatter units from line 14095 through the bibliography boundary are
  each migrated, rehomed, or deliberately retired with a reason.

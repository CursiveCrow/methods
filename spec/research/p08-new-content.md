# P8 research: nonclassical-core migration

> **SUPERSEDED AS A WRITING PLAN (2026-08-12).** The full-compendium
> transcription contract revokes this note's permissions to select, compress,
> normalize, combine, or omit presentations. Source locators and bibliographic
> observations remain audit leads only. No proposed syntax, calculus, theorem,
> card, or treatment boundary in this note is content authority unless it is
> reverified as one complete, separately attributed source presentation.

Status: **IN PROGRESS 2026-08-11** -- claim-safe evidence ledger for the
Phase-4 Part 8 visit. This is research support, not handbook prose. It does not
change a register, add a bibliography or symbol row, establish a proof status,
or itself satisfy a treatment row. The frozen `v1.1-verified` Part X, the live
registers, the current handbook and calculus/symbol registries, original
publications, and authoritative publisher or author archives are being checked
on 2026-08-11.

## Binding source-syntax correction (2026-08-11)

For every named logic, model, method, or calculus, its cited presentation's
actual syntax is part of the evidence surface.  Any instruction below to
"select," normalize, regularize, or replace a glyph in order to avoid a
collision is superseded.  The handbook must retain the source symbol and
declare its local type, even when the same glyph has another role elsewhere.
If the evidence fixes no particular presentation, the deliverable is an owed
artifact or family boundary, not a newly named syntax.  The separate
`p08-source-syntax-correction.md` records the primary-source typography used to
repair the live manuscript.

## Evidence policy and claim boundary

- **Source-verified** means checked in frozen v1.1 at the exact line range
  recorded below. Register line references still denote `v1.0-audit`; this
  ledger records the live v1.1 crosswalk.
- **Primary-verified** means checked against the original publication or an
  official publisher, journal, author, or institutional archive.
- **Authoritative-secondary** means checked against an identified research
  monograph or handbook chapter. It is not converted into a local proof.
- **Derived** means an elementary consequence whose complete argument and
  hypotheses are recorded here. It does not by itself license a bibliography
  claim or a body proof.
- `E`, `T`, `S`, and `P` are treatment ceilings: full entry, sustained table,
  statement/survey, and pointer. They are not evidence-status words.
- Status is governed by `handbook/CONVENTIONS.md`. An inherited complete proof
  may become `proved=annex:...`; an inherited sketch remains
  `sketched=annex:...` and names every omission; a cited theorem remains
  `cited=<key>` and has no annex item. The work order's Tier-2 40--60 percent
  language applies only to inherited proofs that were already complete. It is
  an advisory/reportable length target, never authority to ratio-tune a proof,
  delete a load-bearing step, or prefer brevity over fidelity. New material and
  inherited sketches have no v1.1 denominator. A new local proof is `proved`
  only if every load-bearing case is actually supplied.
- Body files contain statements, definitions, comparison data, and pointers.
  Every axiom schema, inference rule, tableau expansion, and side condition
  lives on a real sheet under `handbook/registry/calculi/`.
- A technical name first introduced in Part 8 must pass the live five-part gate
  at that location: necessity, exact eliminable definition or explicit axiom,
  standing, nonredundancy, and later use. A row title is not permission to name
  an unspecified calculus or semantic structure.

## Executive rulings and blockers

1. **Most inherited adequacy arguments are sketches.** IPL completeness,
   K/T/S4/S5 completeness, LTL completeness, multi-agent S5 completeness, and
   IMLL adequacy/cut elimination are sketches in v1.1. None has a proof-length
   band and none may become `proved` merely because Part 8 needs a full entry.
2. **The source's disjunction-property paragraph is not an independent complete
   proof.** It invokes cut elimination, whose source argument is only a sketch.
   P7 already supplies a cited IPC disjunction theorem and a proved *conditional*
   last-rule lemma for a cut-free derivation. P8 must point to those two distinct
   facts; it must not print a second `proved` disjunction theorem or create a new
   annex item for the dependent paragraph.
3. **Only two inherited arguments currently qualify for advisory length
   bands.**
   Persistence is complete; finite-matrix tableau adequacy is complete after
   R-037. The repaired disjunction paragraph is excluded for the reason above.
4. **Canonical-model work is a new sketch.** v1.1 names the modal canonical
   construction but does not perform it. The handover requests an `hbmethod`
   with an annex sketch, not a laundered complete proof. No percentage target
   applies to it.
5. **The advertised modal correspondence theorem must be split.** The source
   theorem proves only adequacy for four named frame classes. Correspondence
   claims belong in A-077's Phase-6 master or the local D-P10-003 table, each with
   its own cited status. S-015 forbids retaining the old overclaiming title.
6. **GL and Grz are not ordinary modal-cube nodes.** GL extends K4 through the
   Loeb axiom and uses finite transitive irreflexive frame completeness, not the
   ordinary canonical construction. Grz extends S4 and is complete for finite
   partial-order frames. Display them as separate anchored branches; do not add
   invented Hasse edges to S5, S4.2, or S4.3.
7. **Every modal card needs a real exact sheet.** Existing K/T/S4/S5 sheets do
   not discharge D, B, K4, KD45, S4.2, S4.3, GL, or Grz. The exact sheet plan is
   binding below. A prose statement that a system is "K plus the usual axiom"
   does not satisfy the card's `\entrycalculus` field.
8. **Barcan validity is convention-sensitive.** Under actualist quantifiers
   over monotone increasing local domains, converse Barcan is valid and Barcan
   can fail. The reverse pattern uses decreasing domains and needs an outer
   domain or another explicit admissible-assignment convention. Constant
   domains validate both. A-078 and A-142 must declare these choices.
9. **Common knowledge is noncompact.** A finitary Hilbert calculus can be sound
   and complete for valid formulas but not strongly complete for arbitrary
   premise sets. R-039 requires the fixed-point/mix axiom and induction rule on
   a sheet plus this caveat.
10. **Temporal complexity cells need one input convention.** Use combined
    complexity on finite, explicitly represented transition systems unless a
    row says otherwise. The modal mu-calculus model-checking upper bound is
    currently quasi-polynomial via parity games; no polynomial-time theorem may
    be claimed.
11. **The K3/LP slogans need a language boundary.** K3 has no tautologies only
    in the constant-free propositional language in which every formula contains
    a variable. LP has exactly the classical tautologies for the same
    truth-functional signature. Their clean duality reverses finite premise and
    conclusion sets; an unqualified single-conclusion “duality” is incomplete.
12. **Standard real semantics is not a blanket strong-completeness surface.**
    Infinite-valued Lukasiewicz theoremhood and finite-premise consequence are
    complete for `[0,1]`; arbitrary-premise strong completeness is algebraic.
    BL concerns continuous t-norms, MTL left-continuous t-norms. The table must
    not collapse these claims.
13. **The inherited IMLL result covers the multiplicative core only.** It does
    not prove adequacy or cut elimination for exponentials, additives, units, or
    full classical linear logic. D-P10-028 therefore needs a distinct one-sided
    CLL sheet and cited metatheorems, or an explicit row-named stub.
14. **The source deliberately fixes no relevance calculus.** A semantic
    Routley--Meyer overview is not a calculus card. R and E need exact sourced
    sheets before A-086/A-087 can mark structural-rule or variable-sharing
    cells. Broad base-frame adequacy is forbidden.
15. **The Phase-4/Phase-5 boundary conflicts with live apparatus.** The handover
    orders Chapters 8.4 and 8.7 to remain Phase-5 stubs, while A-089--A-094 are
    Phase-4 tables and several 8.4/8.7 rows are must/should. The safe Phase-4
    action is an explicit stub naming every affected row and apparatus ID and to
    leave them open. Building the tables would be substantive Phase-5 content;
    silently marking them done would be dishonest. This requires an explicit
    user ruling if the finalizer expects those apparatus rows closed now.
16. **A-077 remains Phase 6.** D-P10-003 still requires a local Part-8
    correspondence table now. That local table is precursor data; it must not
    flip the master A-077 row to done.
17. **A-147 is a Phase-4 Part-8 deliverable.** Its `phase=4`, `priority=should`
    register row lies in the active temporal-logic home, so a later P9 treatment
    of model checking does not license deferral.  Use the exact two-state
    deterministic B\"uchi automaton for `\(\mathsf G\mathsf Fp\)` specified in
    the 8.3 package below.  The figure must state its alphabet, initial state,
    total transition function, accepting set, and the iff correctness argument;
    it does not need the general LTL-to-automata construction.

## Frozen source crosswalk and status map

Part X occupies v1.1 lines 12970--14094.

| source unit | v1.1 lines | safe migration/status disposition |
|---|---:|---|
| Part-X framing | 12970--12972 | Compress to Part-8 orientation and evidence policy. |
| IPL syntax, Kripke frames, forcing | 12973--13050 | Body definitions/card; use the one registered forcing macro. |
| Persistence | 13051--13057 | Complete inherited proof; Tier-2 annex candidate. |
| IPL soundness/completeness/countermodel bound | 13058--13098 | `sketched`; retain prime-extension, implication-extension, and filtration omissions. |
| IPL examples and classical relations | 13099--13200 | Preserve exact countermodels; Glivenko and Goedel--Gentzen remain cited; disjunction theorem points to P7. |
| Normal modal K/T/S4/S5 | 13201--13339 | Rules to sheets; adequacy `sketched`; split correspondence from completeness. |
| LTL | 13340--13478 | Exact source sheet; weak theoremhood completeness `sketched`; no strong consequence claim. |
| Multi-agent epistemic logic | 13479--13583 | S5_n adequacy `sketched`; common-knowledge proof system is new R-039 content. |
| Finite matrices and tableaux | 13584--13711 | Definitions/body plus exact tableau sheet; repaired adequacy proof is complete. |
| K3 and LP | 13712--13788 | Source matrices/countervaluations; new global tautology/duality facts remain cited or derived with exact language bounds. |
| Routley--Meyer semantics | 13789--13917 | Preserve explicit internal proof boundary: no source-fixed calculus and no adequacy theorem. |
| IMLL and exponentials | 13918--14094 | IMLL theorem `sketched`; exponential rules go to registry; no status transfer to full CLL. |

### Annex eligibility and advisory proof-length reporting

The bands below merely report the handover's Tier-2 target against inherited
complete proofs. Statement fidelity, all hypotheses, and every load-bearing
inference control the result. Falling outside a band is preferable to deleting
mathematics, and a band can never promote an incomplete argument.

| source result | evidence | allowed status | advisory length report / fidelity control |
|---|---|---|---|
| Persistence | Complete structural induction, 43 detex source words | `proved=annex:...` | Tier-2 target 17--26 detex words is advisory only; retain the implication case and the induction hypothesis. |
| IPL disjunction theorem | Last-rule argument depends on sketched cut elimination | `cited=<P7 key>` plus pointer to P7's conditional last-rule lemma | No P8 annex item and no percentage band. |
| Finite-matrix tableau adequacy | Complete repaired proof, 477 detex source words | `proved=annex:...` | Tier-2 target 191--286 detex words; retain both directions, branch termination/saturation, and countervaluation extraction. |
| IPL, modal, LTL, S5_n, IMLL adequacy | Source sketches | `sketched=annex:...` if migrated | No compression denominator; `\sketchnote` names every omitted lemma/case. |
| Canonical models, filtration, every depth fill | New content | `cited` or honest new `sketched`/`proved` according to what is actually written | No v1.1 denominator. |

## Research package 8.1: intuitionistic and intermediate logics

### Exact shared semantics and inherited claims

Use propositional formulas with `\bot,\land,\lor,\to`; define
`\neg A` as `A\to\bot` only when the cited source presentation does so. An
intuitionistic Kripke frame is a nonempty preorder `(W,\preccurlyeq)`. A
valuation sends each atom to an upward-closed subset of `W`. Forcing is
persistent and has the exact implication clause

`w \forces A\to B` iff every `u\succeq w` that forces `A` also forces `B`.

This definition is necessary because classical pointwise implication is not
equivalent to it; its standing is the satisfaction relation of the cited IPL
model, and its later use is persistence, both countermodels, soundness, and the
canonical construction. Do not introduce a second relation glyph or forcing
macro.

The inherited theorem may state soundness and theoremhood/finite-premise
completeness for the exact source calculus, but it remains `sketched`. The annex
must name at least these omissions if they are not supplied: prime-theory
extension (with R-041's `T\vdash A\lor B` reading), the implication-extension
lemma, the truth lemma, and the filtration/countermodel bound.

### Persistence

Safe theorem: for every formula `A` and worlds `w\preccurlyeq u`,
`w\forces A` implies `u\forces A`. The valuation's upward closure is a
hypothesis. The complete source induction covers atoms and the connectives; the
implication step uses transitivity of the preorder. Do not generalize this
propositional proof to first-order forcing without adding monotone domains and
the quantifier cases.

### Heyting-algebra semantics (`D-P10-013`)

An `E` entry must define one bounded distributive lattice
`\mathcal H=(H,\wedge,\vee,0,1,\Rightarrow)` and the relative
pseudocomplement law

`a\wedge b\leq c` iff `a\leq (b\Rightarrow c)`.

The symbol `\Rightarrow` here is the source's algebraic operation. Retain it
and register its local operand type even though the same glyph is also used as
a sequent arrow elsewhere.
Formula valuations send implication to that operation. Safe completeness:

`\vdash_{\mathsf{IPL}} A` iff every valuation in every Heyting algebra gives
`A` value `1`.

For consequence, state the cited source's finite-premise form or define the algebraic
filter semantics explicitly. Do not infer a locally proved theorem from the
entry: cite `RasiowaSikorski1963` or `TroelstraVanDalen1988`. Explain
nonredundancy at first use: Boolean algebras force `a\vee\neg a=1`, whereas
general Heyting algebras do not; the distinction is used by the IPL/CPL
comparison and KC/LC entries.

### Topological semantics (`D-P10-014`)

For a topological space `(X,\tau)`, valuations assign open sets to atoms and
extend by intersection, union, empty set, and

`\llbracket A\to B\rrbracket =
\operatorname{int}((X\setminus\llbracket A\rrbracket)
\cup\llbracket B\rrbracket)`.

This is a semantic interpretation, not a new object-language connective.
Theoremhood completeness may be cited to `McKinseyTarski1946`: IPL theorems are
exactly the formulas valid under all such open-set valuations. If the stronger
single-space claim for the real line is printed, verify that exact formulation
from the cited source first; it is not needed by the S ceiling.

### BHK and realizability (`D-P10-015`, `N-b-030`)

The Brouwer--Heyting--Kolmogorov clauses are an explanatory interpretation, not
a formal semantics and not an adequacy theorem. At minimum say what counts as a
construction for conjunction, disjunction, implication, absurdity, universal,
and existential statements, and distinguish this explanation from the formal
Kleene number-realizability relation already developed in P7. Cite
`Brouwer1908`, `Heyting1956`, and `TroelstraVanDalen1988`; do not attribute the
modern packaged acronym or every clause to Brouwer's 1908 paper.

Choice sequences, bar induction, continuity principles, and the philosophical
status of Markov's principle are survey/pointer material. Each principle must be
written as an exact schema over a named base theory before receiving a truth or
independence status. `D-P10-019` is could-priority and should remain an explicit
row-named stub unless the register ceiling is deliberately filled.

### Existence property (`D-P10-016`)

The unqualified slogan is false or ambiguous across calculi. Safe
normalization-shaped statement:

> If the fixed pure intuitionistic first-order natural-deduction calculus has a
> closed normal derivation with no open assumptions and no free parameters of
> `\exists x\,A(x)`, then its last inference supplies a closed term `t` and a
> derivation of `A(t)`.

If equality axioms, nonlogical axioms, empty signatures, or free parameters are
allowed, state the corresponding witness theorem separately. P8 should cite the
P7 normalization boundary; it must not claim the property for HA from the
arrow-only normalization theorem.

### First-order IPL and constant domains (`D-P10-017`)

An expanding-domain model has a preorder `(W,\preccurlyeq)`, nonempty domains
`D_w` with `w\preccurlyeq u` implying `D_w\subseteq D_u`, persistent predicate
interpretations, and the clauses

- `w\forces\exists x\,A` iff some `a\in D_w` satisfies `w\forces A[a/x]`;
- `w\forces\forall x\,A` iff for every `u\succeq w` and every `a\in D_u`,
  `u\forces A[a/x]`.

The growing-domain hypothesis is load-bearing for persistence. Cite
`Kripke1965`/`TroelstraVanDalen1988` for soundness and completeness of the exact
chosen IQC calculus; no inherited Part-X proof exists. The constant-domain
principle is

`\forall x\,(A\lor B(x))\to (A\lor\forall x\,B(x))`, with `x` not free in `A`.

It is valid on constant-domain intuitionistic models and fails on general
expanding-domain models. Do not confuse it with either modal Barcan formula.

### KC and LC (`D-P10-018`, `N-b-031`, `A-081`)

Fix these exact extensions:

| system | added schema | safe frame characterization | disjunction property | FMP |
|---|---|---|---|---|
| KC | `\neg A\lor\neg\neg A` | cite the source's rooted-frame characterization; for finite rooted frames, a unique greatest world is the standard presentation | no | yes |
| LC / Goedel--Dummett | `(A\to B)\lor(B\to A)` | linearly ordered intuitionistic frames | no | yes |

The two “no” cells are derived, not merely conventional. Each displayed added
axiom is itself a theorem-shaped disjunction, while neither disjunct is a theorem
of that system (witness the standard finite frames/valuations). Therefore the
ordinary theorem-level disjunction property fails. Cite `Dummett1959` for LC and
the exact weak-excluded-middle paper `Jankov1968WeakExcludedMiddle` for KC; do
not use Jankov's different 1968 strongly-independent-logics paper as the source
of the KC axiom.

### A-137, A-138, and A-144

- A-137: use the two-world chain `w_0\prec w_1`, with `p` false at `w_0` and
  true at `w_1`. At `w_0`, neither `p` nor `\neg p` is forced, so excluded middle
  fails. Annotate both worlds and the upward-closed valuation.
- A-138: on the same chain, take `p` false at the root and true at the leaf and
  `q` false everywhere. The root forces `(p\to q)\to p` but not `p`, so Peirce's
  law fails. Show the implication evaluation rather than only drawing the frame.
- A-144 is could-priority. If drawn, it is a schematic interval between IPL and
  CPL, not a claim that KC and LC are comparable. Do not draw an edge between
  them without a cited inclusion theorem.

### 8.1 row disposition

| row | ceiling / priority | binding safe delivery |
|---|---|---|
| `D-P10-013` | E / must | Full Heyting-algebra definition and cited theoremhood completeness. |
| `D-P10-014` | S / should | Exact open-set semantics and cited completeness statement. |
| `D-P10-015` | S / should | BHK survey distinguished from formal realizability. |
| `D-P10-016` | S / must | Calculus-bounded existence theorem with closedness/no-free-parameter hypotheses. |
| `D-P10-017` | E / must | Expanding-domain IQC semantics, cited completeness, and exact CD boundary. |
| `D-P10-018` | S / should | KC/LC schemas, frames, DP and FMP statuses; supports A-081. |
| `D-P10-019` | S / could | Explicit row-named Markov-principle stub unless intentionally filled. |
| `N-b-030` | S / should | Philosophy/mathematics survey with exact principle statements only. |
| `N-b-031` | S / should | Same KC/LC delivery, with the cited source correction above. |

### A-082: exact negative-translation package

This table is a Phase-4 must even though it is not a depth or new-content row.
Fix one first-order grammar with primitive `\bot`; let `P` range over genuine
atomic formulas, so `P` never includes `\bot`, and treat `\neg A` only as the
abbreviation `A\to\bot`. This separation is necessary because otherwise the
atomic and bottom clauses overlap; it is the metalinguistic standing of the
four recursive maps, differs from object-language negation, and is used in
every preservation statement in the table.

Use these exact clauses (equivalent variants may be mentioned in notes but must
not be silently mixed within one column):

| translation | exact recursive clauses, including `\bot` | exact safe preservation theorem |
|---|---|---|
| Glivenko `G` | Not structural: `G(A)=\neg\neg A`; hence `G(\bot)=\neg\neg\bot`. | **Propositional only:** `\vdash_{\mathsf{CPL}}A` iff `\vdash_{\mathsf{IPL}}\neg\neg A`. The inherited finite-context sequent form may be repeated exactly as sourced, but no quantifier extension is allowed. |
| Kolmogorov `Ko` | `P^{Ko}=\neg\neg P`; `\bot^{Ko}=\neg\neg\bot`; for each `\circ\in\{\land,\lor,\to\}`, `(A\circ B)^{Ko}=\neg\neg(A^{Ko}\circ B^{Ko})`; for `Q\in\{\forall,\exists\}`, `(QxA)^{Ko}=\neg\neg QxA^{Ko}`. | `\vdash_{\mathsf{CL}}A` iff `\vdash_{\mathsf{IL}}A^{Ko}`; for consequence, translate every member of the premise context as well. |
| Goedel--Gentzen `N` | `\bot^N=\bot` **with priority over the atomic clause**; `P^N=\neg\neg P`; commute with `\land`, `\to`, and `\forall`; `(A\lor B)^N=\neg(\neg A^N\land\neg B^N)`; `(\exists xA)^N=\neg\forall x\neg A^N`. | Exact inherited statement: `\mathsf{LK}\vdash\Gamma\Rightarrow A` iff `\mathsf{LJ}\vdash\Gamma^N\Rightarrow A^N`, with every member of `\Gamma` translated. This remains `cited`, not an annex proof. |
| Kuroda `Ku` | First define the inner map: `P_{Ku}=P`, `\bot_{Ku}=\bot`; it commutes with `\land,\lor,\to,\exists`; `(\forall xA)_{Ku}=\forall x\neg\neg A_{Ku}`. Then define the full translation `A^{Ku}=\neg\neg A_{Ku}`; in particular `\bot^{Ku}=\neg\neg\bot`. | `\vdash_{\mathsf{CL}}A` iff `\vdash_{\mathsf{IL}}A^{Ku}`; the named result targets intuitionistic logic, not minimal logic. Translate assumptions for the context form. |

The exact Kolmogorov and Kuroda clauses and theoremhood embeddings are checked
against Ferreira--Oliva's comparative reconstruction; Kuroda's original record
is *Nagoya Mathematical Journal* 2 (1951), 35--47,
doi `10.1017/S0027763000010023`, and Kolmogorov's original record is
*Matematicheskii Sbornik* 32(4) (1925), 646--667. Use existing keys
`Glivenko1929`, `Godel1933`, `Gentzen1936`, and
`TroelstraVanDalen1988`; intake keys `Kolmogorov1925ExcludedMiddle` and
`Kuroda1951` are required. Do not cite the unrelated existing
`Kolmogorov1965` information-complexity paper.

**A-082 completion test.** All four columns must give the full connective and
quantifier clauses appropriate to their scope, an explicit non-overlapping
bottom clause, the target calculi, and a cited preservation theorem. Glivenko
must be marked propositional; Goedel--Gentzen must preserve R-040's bottom
priority; none of these cited translations receives an annex item.

## Research package 8.2: normal, non-normal, and quantified modal logic

### Shared normal-modal definitions

A Kripke model is `\mathcal M=(W,R,V)` with nonempty `W`, binary
`R\subseteq W^2`, and `V` assigning sets of worlds to atoms. Satisfaction has
the exact clauses

- `\mathcal M,w\models\Box A` iff every `u` with `wRu` satisfies `A`;
- `\mathcal M,w\models\Diamond A` iff some `u` with `wRu` satisfies `A`.

Keep local consequence (truth preservation at one world under every model) and
global consequence (validity preservation over all worlds of a frame) distinct.
The source calculus has theorem-only necessitation; no card may silently use a
premise-dependent necessitation rule.

### Canonical-model method (`D-P10-001`, `N-b-001`)

For a fixed normal modal logic `L`, worlds are maximal `L`-consistent sets and

`\Gamma R_L\Delta` iff every `A` with `\Box A\in\Gamma` belongs to `\Delta`.

This definition is necessary to distinguish the proof model from an arbitrary
semantic model; its standing is a metalinguistic construction; it differs from
filtration because its worlds are theories rather than equivalence classes of a
given model; and it is used by the existence lemma, truth lemma, and frame-
property checks. The annex is an honest sketch. It must name any omitted
Lindenbaum lemma, diamond/existence lemma, Boolean/modal truth-lemma cases, and
each axiom-to-frame verification.

Safe scope:

- ordinary canonical checks cover K, D, T, B, K4, S4, S5, KD45, S4.2, and
  S4.3 when a cited presentation fixes their exact axioms;
- GL and Grz do **not** use this ordinary canonical proof and remain separately
  cited finite-frame completeness results;
- source status for K/T/S4/S5 remains `sketched`, even if the entry is expanded.

### Real-sheet plan for every modal card

Every extension sheet inherits the exact `sheet:hilbert-k` identity: classical
modal propositional language, MP, theorem-only necessitation, and K. Each new
axiom is an `\hbrule` with all five arguments and a unique `rule:p08-*` label.

**Binding naming convention.** Because `N-b-007` explicitly requests the
historical *modal-cube system* B and cites Hughes--Cresswell, `B` in the cards,
A-076, and A-136 means `K+T+B`, equivalently `KTB`: its frames are reflexive
and symmetric. It does **not** mean the strictly weaker `K+B`, which should be
called `KB` if it ever needs to be mentioned. This choice also agrees with
Chellas's unambiguous compositional `KS_1\cdots S_n` notation. Keep the axiom
name B distinct from the system name B: the axiom alone corresponds to
symmetry, whereas Chellas's cited system has both T and B. No `KB` card is owed by
the live register.

| card | real sheet | exact extension | safe evidence/status boundary |
|---|---|---|---|
| K | existing `sheet:hilbert-k` | K only | inherited adequacy sketch |
| D | new `sheet:hilbert-d` | `\Box A\to\Diamond A` | canonical/serial completeness sketched or cited |
| T | existing `sheet:hilbert-t` | K + `\Box A\to A` | inherited adequacy sketch |
| B | new `sheet:hilbert-b` | K + T + `A\to\Box\Diamond A` | canonical completeness for reflexive symmetric frames, sketched or cited; sheet identity must say `KTB`, not `KB` |
| K4 | new `sheet:hilbert-k4` | K + `\Box A\to\Box\Box A` | canonical/transitive completeness sketched or cited |
| S4 | existing `sheet:hilbert-s4` | T + 4 | inherited adequacy sketch |
| KD45 | new `sheet:hilbert-kd45` | K + D + 4 + `\Diamond A\to\Box\Diamond A` | serial/transitive/Euclidean completeness cited |
| S4.2 | new `sheet:hilbert-s4-2` | S4 + `\Diamond\Box A\to\Box\Diamond A` | reflexive/transitive/directed-frame completeness cited |
| S4.3 | new `sheet:hilbert-s4-3` | S4 + `\Box(\Box A\to B)\lor\Box(\Box B\to A)` | reflexive/transitive/weakly-connected-frame completeness cited |
| S5 | existing `sheet:hilbert-s5` | T + 5 | inherited adequacy sketch; equivalence frames |
| GL | new `sheet:hilbert-gl` | K + `\Box(\Box A\to A)\to\Box A` | cite `Solovay1976`/`Boolos1993` and modal sources; no ordinary canonical claim; finite transitive irreflexive theoremhood completeness |
| Grz | new `sheet:hilbert-grz` | S4 + `\Box(\Box(A\to\Box A)\to A)\to A` | cite `ChagrovZakharyaschev1997`; no ordinary canonical claim; finite partial-order theoremhood completeness |

The sheets are rule surfaces, not proof evidence. A sheet's existence does not
upgrade a card's adequacy status.

### Frame correspondence and standard translation (`D-P10-003`, `N-b-002`)

Define the standard translation with a displayed free world variable:

- `\mathrm{ST}_x(p)=P_p(x)`;
- Boolean clauses commute with the translation;
- `\mathrm{ST}_x(\Box A)=\forall y(Rxy\to\mathrm{ST}_y(A))`;
- `\mathrm{ST}_x(\Diamond A)=\exists y(Rxy\land\mathrm{ST}_y(A))`.

The local Phase-4 table must at least contain:

| axiom | exact frame condition |
|---|---|
| D | `\forall x\,\exists y\,Rxy` (serial) |
| T | `\forall x\,Rxx` (reflexive) |
| B axiom | `\forall x,y\,(Rxy\to Ryx)` (symmetric); Chellas's system B also includes T, hence uses reflexive symmetric frames |
| 4 | `\forall x,y,z\,(Rxy\land Ryz\to Rxz)` (transitive) |
| 5 | `\forall x,y,z\,(Rxy\land Rxz\to Ryz)` (Euclidean) |
| .2 | `Rxy\land Rxz` implies a common successor of `y,z` (directed/convergent) |
| .3 | `Rxy\land Rxz` implies `Ryz` or `Rzy` on the transitive presentation (weakly connected) |

Each equivalence needs both validity and converse directions or an exact cited
status. State Sahlqvist's theorem only for the fixed syntactic class: every
Sahlqvist formula has an effectively computable first-order correspondent and
its normal logic is canonical/Kripke complete. Do not call arbitrary modal
axioms Sahlqvist. The algebra column requested by A-077 is Phase-6 work; local
P8 may include it only if exact complex-algebra conditions are sourced.

### Bisimulation and van Benthem (`D-P10-004`, `N-b-003`, `A-123`)

For pointed models over the same propositional signature, a relation `Z` is a
bisimulation when related points agree on atoms and satisfy forth and back for
`R`. Modal invariance is proved by induction on basic modal formulas. The safe
characterization statement is:

> Over all Kripke models, a first-order formula with one free world variable is
> equivalent to the standard translation of a basic modal formula iff it is
> invariant under bisimulations.

Do not silently restrict this theorem to finite models; the finite-model variant
is a separate theorem. A-123 must label atoms, forth, and back, not merely draw
two arrows.

### Filtration, FMP, and decidability (`D-P10-002`, `N-b-004`)

Given a finite subformula-closed set `\Sigma`, define `w\sim_\Sigma u` iff `w`
and `u` agree on every formula in `\Sigma`. A filtration is a quotient model
whose relation lies between the minimal and maximal filtration relations and
preserves truth for every formula in `\Sigma`. State explicitly which closure
or quotient relation preserves the target frame class:

- K: ordinary filtration;
- T: reflexive closure as needed;
- S4: transitive/reflexive filtration construction;
- S5: equivalence-class filtration.

The requested conclusion is FMP and hence decidability for K, T, S4, and S5.
No source-compression denominator exists. If the quotient lemma and all four
frame-preservation cases are not proved, label the method `sketched` and cite
`Segerberg1971`, `BlackburnDeRijkeVenema2001`, and
`ChagrovZakharyaschev1997`.

### Modal lattice and card containments (`A-076`, `A-136`)

The diagram may show these safe inclusions among the listed systems:

- K below D and K4;
- D below T and KD45;
- K4 below S4, KD45, and GL;
- T below B and S4;
- S4 below S4.2 and Grz;
- S4.2 below S4.3 below S5;
- B below S5; KD45 below S5.

Edges must mean theorem-set inclusion, and the caption must say whether the
diagram is a Hasse diagram for just the displayed finite selection. GL and Grz
are separately anchored at K4 and S4; no edge to S5, S4.2, or S4.3 is licensed
by this ledger. Validate every proposed additional edge before drawing it.

### Modal countermodel figures (`A-139`--`A-141`)

- A-139 (T): take `wRu`, not `Rww`; make `p` true at every `R`-successor of
  `w` and false at `w`. Then `w\models\Box p` but `w\not\models p`.
- A-140 (4): take `wRu`, `uRv`, but not `wRv`; make `p` true at `u` and false
  at `v` (and ensure all direct successors of `w` satisfy `p`). Then
  `w\models\Box p` and `w\not\models\Box\Box p`.
- A-141 (5): take `wRu,wRv` but not `uRv`; make `p` true at `v` and false at
  every successor of `u`. Then `w\models\Diamond p` but
  `w\not\models\Box\Diamond p`.

Each figure must list all edges relevant to the valuation; omitting reflexive or
transitive edges can accidentally move the countermodel into the wrong class.

### Kripke incompleteness (`N-b-005`)

At S ceiling, state only the precise phenomenon: Thomason exhibited a normal
modal logic not complete with respect to any class of ordinary Kripke frames;
Fine supplied an incomplete extension containing S4. General/descriptive frames
repair the semantics only after their admissible-set component and validity
notion are defined. Use `Thomason1974` and `Fine1974`; do not promote the survey
to a proof or imply that every noncanonical logic is Kripke incomplete.

### Neighborhood semantics (`D-P10-007`, `N-b-006`)

A neighborhood model is `(W,N,V)` with `N(w)\subseteq\mathcal P(W)` and
`w\models\Box A` iff the truth set of `A` belongs to `N(w)`. This is needed for
congruential systems weaker than normal K; `N` is a semantic function, not the
Routley--Meyer normal-world set. State a single convention for the named systems
because letters vary across sources. Under the Chellas/Pacuit convention, map
the proof principles to exact neighborhood conditions before naming E, M, C,
N, or “regular”; do not infer the names from mnemonics alone. This is an E/should
new-content obligation despite D-P10-007's could priority. A real source-exact sheet
is required if it becomes a system card. Sources: `Scott1970`, `Montague1970`,
`Chellas1980`, `Pacuit2017`.

### Two-dimensional actuality (`N-b-008`)

At S ceiling, distinguish at least an evaluation world from a context/designated
world before introducing an actuality operator. `CrossleyHumberstone1977`
supports the logic of “actually”; `DaviesHumberstone1980` distinguishes two
notions of necessity; Kaplan's character/content distinction requires an index
and circumstance of evaluation. These are related tools, not one theorem. No
contingent-a-priori example may be claimed until the two-dimensional truth
conditions are explicit.

### Quantified modal logic (`D-P10-008`, `N-b-009`, `A-078`, `A-142`)

Fix an outer domain `D`, local nonempty domains `D_w\subseteq D`, actualist
quantifiers ranging over `D_w`, rigid variable assignments into `D`, and an
explicit existence predicate `E(t)` meaning the denotation lies in `D_w`. State
whether predicate extensions are world-relative and whether names are rigid.

Use these formula names consistently:

- BF: `\forall x\,\Box A(x)\to\Box\forall x\,A(x)`;
- CBF: `\Box\forall x\,A(x)\to\forall x\,\Box A(x)`.

Then the safe comparison is:

| local-domain regime | BF | CBF |
|---|---|---|
| constant | valid | valid |
| increasing (`wRv` implies `D_w\subseteq D_v`) | may fail | valid |
| decreasing, under the declared outer-domain semantics | valid | may fail |
| arbitrary varying | may fail | may fail |

A-142 must be an increasing-domain countermodel to **BF**, with a new object at
an accessible world that is not constrained by the antecedent at the root. It
must not label that formula CBF. Actualism/possibilism and necessitism are
philosophical interpretations of domain/designation choices, not consequences
of the four-cell table. Cite `Barcan1946`, `Kripke1963`,
`FittingMendelsohn1998`, `Garson2001`, and `Williamson2013` at their exact uses.

### 8.2 row disposition

| row | ceiling / priority | binding safe delivery |
|---|---|---|
| `D-P10-001` | E / must | Canonical method entry and honest annex sketch for K/T/S4/S5; exact scope table for other canonical systems. |
| `D-P10-002` | E / must | Filtration definition, truth lemma, class-preservation map, FMP/decidability. |
| `D-P10-003` | E / must | Local correspondence/ST table and cited Sahlqvist statement; A-077 stays open. |
| `D-P10-004` | E / should | Bisimulation, invariance, and all-model van Benthem theorem; supports A-123. |
| `D-P10-005` | E / must | D/B/K4/KD45/Grz cards, plus real sheets; coordinated with N-b-007/A-076. |
| `D-P10-007` | S / could | Shared topic delivered at E/should by N-b-006 or explicit stub if blocked on a convention. |
| `D-P10-008` | E / must | Exact varying-domain QML entry, BF/CBF table, rigid/existence/actualism distinctions. |
| `N-b-001` | E / must | Canonical K/T/D/B/K4/S4/S5 scope; no GL/Grz laundering. |
| `N-b-002` | T / must | Correspondence table and Sahlqvist statement. |
| `N-b-003` | T / must | Same bisimulation/van Benthem package, delivered at E by shared depth row. |
| `N-b-004` | T / must | Same filtration package, delivered at E by shared depth row. |
| `N-b-005` | S / should | Cited Thomason/Fine incompleteness survey. |
| `N-b-006` | E / should | Exact cited neighborhood presentation, system map, and real sheet(s). |
| `N-b-007` | E / must | K,D,T,B,K4,S4,S4.2,S5,GL,Grz cards; A-076 also requires S4.3 and KD45. |
| `N-b-008` | S / should | Defined two-dimensional evaluation parameters and qualified philosophical examples. |
| `N-b-009` | E / must | Same QML/Barcan package as D-P10-008. |

## 8.3 temporal, branching-time, and dynamic-epistemic package

This package is **stable for implementation**.  It covers `D-P10-006`,
`D-P10-009`, `D-P10-011`, `D-P10-012`, `N-b-011`, `N-b-012`, `N-b-014`,
`N-b-015`, and apparatus `A-079`, `A-080`, `A-145`, `A-146`, and `A-147`.
The three branching-time cards require three distinct sheets: their grammars,
semantic objects, and complete calculi are not interchangeable.

### Inherited LTL surface and status

Migrate v1.1 lines 13340--13478 without changing the semantic convention:
models are infinite words `\(\mathcal M=(\mathbb N,V)\)`, `\(\mathsf X\)` is
next, and `\(\mathsf U\)` is strong until.  The local definitions are
`\(\mathsf F A:=\top\mathbin{\mathsf U}A\)` and
`\(\mathsf G A:=\neg\mathsf F\neg A\)`.  The inherited calculus belongs only
on `sheet:hilbert-ltl`; its necessitation and until-induction rules are
theorem-only.  The adequacy theorem remains `sketched`: the source omits
consistency, eventuality-realization, and truth-lemma calculations.  It is weak
completeness for validity on discrete infinite words, not strong completeness
from arbitrary premise sets and not a finite-trace theorem.

### CTL card and exact sheet (`D-P10-009`)

Use total finite or infinite transition structures `\((S,R,V)\)` for semantics;
total means every state has an `\(R\)`-successor, so paths are infinite.  CTL is
a **state-formula** logic.  Its primitive temporal forms may be fixed as
`\(\mathsf{EX}A\)`, `\(\mathsf{AX}A\)`,
`\(\mathsf E(A\mathbin{\mathsf U}B)\)`, and
`\(\mathsf A(A\mathbin{\mathsf U}B)\)`, with `EF` and `AF` eliminable.  State
the path quantifiers' standing before use: `\(\mathsf E\)` chooses an infinite
path from the current state and `\(\mathsf A\)` quantifies over all such paths.

Create a real `sheet:hilbert-ctl` matching Emerson--Halpern's complete
theoremhood calculus.  In addition to propositional tautologies, it has the
following schemas.  Reproduce the presentation's formula letters on the sheet
and type them locally in the Part-8 registry; do not rename them for house
uniformity:

```text
EF A <-> E(true U A)                 AF A <-> A(true U A)
EX(A or B) <-> EX A or EX B          AX A <-> not EX not A
E(A U B) <-> B or (A and EX E(A U B))
A(A U B) <-> B or (A and AX A(A U B))
EX true and AX true
```

The four exact rules are:

```text
from A -> B infer EX A -> EX B
from C -> (not B and EX C) infer C -> not A(A U B)
from C -> [not B and AX(C or not E(A U B))] infer C -> not E(A U B)
from A and A -> B infer B
```

Every rule is theorem-only and every registry `\hbrule` must carry that side
condition explicitly.  Cite `EmersonHalpern1985` for soundness and completeness;
there is no annex item.  Do not replace the two induction rules by an unnamed
"standard CTL rule": doing so would fail the real-sheet requirement.

### CTL* card and exact sheet (`D-P10-009`)

Use a two-sorted presentation for the card: state formulas include atoms,
Boolean combinations, and `\(\mathsf A\alpha\)` for path formulas `\(\alpha\)`;
path formulas include embedded state formulas, Boolean combinations,
`\(\mathsf X\alpha\)`, and
`\(\alpha\mathbin{\mathsf U}\beta\)`.  Define
`\(\mathsf E\alpha:=\neg\mathsf A\neg\alpha\)`.  This separates CTL* from CTL:
path quantification may govern an arbitrary temporal path formula, rather than
being syntactically paired only with next or until.

Create `sheet:hilbert-ctl-star` from Reynolds's **standard-fullpath** calculus,
not from the incomplete bundled-tree base alone.  Its PLTL base has modus ponens,
the theorem-only temporal-generalization rule `\(\alpha/\mathsf G\alpha\)`,
propositional tautologies, and schemas C1--C8:

```text
F not not alpha <-> F alpha
G(alpha -> beta) -> (G alpha -> G beta)
G alpha -> (alpha and X alpha and X G alpha)
X not alpha <-> not X alpha
X(alpha -> beta) -> (X alpha -> X beta)
G(alpha -> X alpha) -> (alpha -> G alpha)
(alpha U beta) <-> [beta or (alpha and X(alpha U beta))]
(alpha U beta) -> F beta
```

Add theorem-only path generalization `\(\alpha/\mathsf A\alpha\)` and the
bundled-tree schemas C9--C15:

```text
A(alpha -> beta) -> (A alpha -> A beta)
A alpha -> A A alpha
A alpha -> alpha
alpha -> A E alpha
A not alpha <-> not E alpha
p -> A p                         (p atomic only)
A X alpha -> X A alpha
```

There is deliberately **no uniform-substitution rule**: C14 is restricted to
atoms and arbitrary substitution for it is invalid.  The standard-fullpath
system further requires Reynolds's limit-closure schema

```text
A G(E alpha -> E X((E beta) U (E alpha)))
  -> (E alpha -> E G((E beta) U (E alpha)))
```

and the Auxiliary Atoms rule.  The sheet must define the latter's side
condition exactly.  For disjoint atom sets `\(L,Q\)`, a formula `\(\theta\)` is
*functionally `\(L+Q\)`-expandable* precisely when there are state formulas
`\(\alpha_1,\ldots,\alpha_n\)` over `\(L\)` forming a propositional partition,
a finite enumerated `\(Q\)`, `\(b_0\in Q\)`, and
`\(\rho:Q\times\{1,\ldots,n\}\to Q\)` such that

```text
theta = b_0
  and A G [and_{b in Q, 1 <= i <= n}
      ((b and alpha_i) -> A X rho(b,i))]
  and A G [and_{b != b' in Q} not(b and b')].
```

Here "propositional partition" means each `\(\alpha_i\)` is a Boolean
combination of atoms and `\(\mathsf E\beta\)` formulas, distinct members are
classically inconsistent, and their finite disjunction is a propositional
tautology.  The rule is

```text
from theta -> psi infer psi
```

provided `\(\psi\)` uses atoms only from `\(L\)` and `\(\theta\)` is
functionally `\(L+Q\)`-expandable.  This technical name passes the five-part
gate only on the sheet: it is needed to state AA unambiguously; the displayed
condition is its eliminable definition; its standing is a metalinguistic
side-condition; it is stronger than mere semantic expandability because it
fixes a finite-state functional expansion; and AA immediately uses it.

The exact status is `cited=Reynolds2001`: the resulting system is sound and
weakly complete for standard CTL* validity.  Noncompactness rules out a strong
arbitrary-premise reading.  There is no annex item and no license to call the
much smaller bundled-tree subsystem a CTL* calculus.

### Modal mu-calculus card and exact sheet (`D-P10-009`)

The live implementation must reproduce Kozen's actual finitary `\(L_\mu\)`
syntax; an equivalent modern surface is not the cited presentation.  The primitive
nonlogical symbols are propositional constants `\(p,q,\ldots\)` (including
`\(0,1\)`), fixpoint variables `\(Z,Y,\ldots\)`, and program constants
`\(a,b,\ldots\)`.  Formulas are generated by

```text
Z | p | (A or B) | not A | <a>A | mu Z.A,
```

where every free occurrence of `\(Z\)` in `\(A\)` lies under an even number of
negations.  Conjunction, implication, `\([a]A\)`, and `\(\nu Z.A\)` are the
defined operators of Kozen 1983, section 3.1; positive normal form is a derived
normal form and is not the primitive grammar.  A model assigns a state set to
each propositional constant and a binary relation to each program constant; an
environment maps fixpoint variables to state sets.  The `\(\mu\)` clause is the
least fixed point of the induced monotone powerset operator, and `\(\nu\)` is
its stated capture-avoiding dual.

Create `sheet:hilbert-mu` as Kozen's equational calculus from section 5, not as
an imported Hilbert-K grammar.  Its judgments are equations `\(A=B\)` and
inequalities `\(A\leq B\)`, with `\(A\leq B\)` abbreviating `\(A\lor B=B\)`.
Besides Boolean equational logic, it has exactly the modal join, mixed, and
zero axioms, the least-fixpoint prefix axiom, and Park's rule:

```text
<a>A or <a>B = <a>(A or B)
<a>A and [a]B <= <a>(A and B)
<a>0 = 0
A[mu Z.A/Z] <= mu Z.A
from A[Y/Z] <= Y infer mu Z.A <= Y, with Y absent from A.
```

All substitutions are capture-avoiding and preserve the positivity formation
condition; the prefix instance must be free for `\(Z\)`.  Theoremhood is the
equation `\(A=1\)`.  Cite `Kozen1983` for this exact syntax, semantics, and
calculus and `Walukiewicz2000` for completeness.  The status is cited, with no
annex.  This paragraph supersedes the earlier draft's instruction to choose
between equivalent presentations.

### Temporal comparison table (`A-079`)

The table must state that complexity is **combined complexity** on finite,
explicitly represented total transition systems.  For LTL, a model-checking
instance asks whether all initial paths satisfy the path formula.  Use these
cells:

| logic | semantic/formula scope | expressiveness | satisfiability | finite-state model checking |
|---|---|---|---|---|
| LTL | path formulas over infinite words | embeds in CTL* after an outer path quantifier; not a branching-state language by itself | PSPACE-complete | PSPACE-complete in the combined input; linear in the structure for each fixed formula |
| CTL | state formulas with path quantifier immediately paired with temporal operators | strict fragment of CTL* and of the modal mu-calculus | EXPTIME-complete | linear-time algorithm in structure times formula size; decision problem P-complete |
| CTL* | state/path formulas with arbitrary temporal nesting under path quantifiers | strictly contains CTL and the state-lifted LTL fragment; is strictly contained in modal mu-calculus on transition systems | 2EXPTIME-complete | PSPACE-complete |
| modal mu-calculus | bisimulation-invariant modal fixed-point state formulas | strictly extends CTL* on transition systems | EXPTIME-complete | parity-game equivalent; P-hard and solvable in quasipolynomial time, with membership in `UP` intersect `coUP`; polynomial time remains open |

Use `SistlaClarke1985` and `VardiWolper1986` for LTL, `EmersonHalpern1985`
and `ClarkeEmersonSistla1986` for CTL, `Reynolds2001`,
`EmersonLei1987`, and `EmersonJutla1999` for CTL*, and `Kozen1983`,
`Walukiewicz2000`, and `CaludeJainKhoussainovLiStephan2017` for the modal
mu-calculus/parity-game boundary.  Do not report the quasi-polynomial upper
bound as a polynomial-time result.

### Temporal figures (`A-145`, `A-146`, `A-147`)

`A-145` can use one infinite word whose displayed prefix has `\(p\)` at
positions 0, 1, and 2, `\(q\)` at position 3, and `\(p\)` at every position
from 4 onward.  At position 0, `\(\mathsf Xp\)`,
`\(p\mathbin{\mathsf U}q\)`, and `\(\mathsf Fq\)` are true;
`\(\mathsf Gp\)` is false; and `\(\mathsf G(p\lor q)\)` is true.  The figure
must draw or state the infinite tail: a five-node prefix alone does not determine
an LTL truth value.

`A-146` should use a total rooted transition tree with one branch on which
`\(p\)` eventually holds and another on which it never holds.  At the root
`\(\mathsf{EF}p\)` is true and `\(\mathsf{AF}p\)` is false.  If immediate
successors are also labelled, the same tree may show `\(\mathsf{EX}p\)` true
and `\(\mathsf{AX}p\)` false.  Every displayed leaf must have a continuation
edge or an explicitly drawn infinite tail; otherwise the picture violates the
declared total-path semantics.

`A-147` is discharged by the following exact worked construction.  Let

```text
A_GFp = (Q, Sigma, delta, q_notp, F),
Q = {q_notp,q_p},       Sigma = P({p}),       F = {q_p},
delta(q,a) = q_p    if p is in a,
delta(q,a) = q_notp if p is not in a,        for both q in Q.
```

Draw `\(q_{\neg p}\)` as the initial nonaccepting state and `\(q_p\)` with a
double circle.  From **each** state, the edge labelled `\(p\)` goes to `\(q_p\)`
and the edge labelled `\(\neg p\)` goes to `\(q_{\neg p}\)`; the edge labels
mean respectively letters containing and not containing `\(p\)`.  The
transition function is total and deterministic.

For an input word `\(a_0a_1\ldots\)`, use the run convention
`\(r_0=q_{\neg p}\)` and `\(r_{n+1}=\delta(r_n,a_n)\)`.  The B\"uchi acceptance
condition is
`\(\operatorname{Inf}(r)\cap F\ne\varnothing\)`, equivalently that `\(q_p\)`
is visited infinitely often.  By the transition definition,
`\(r_{n+1}=q_p\)` iff `\(p\in a_n\)`.  Thus the automaton accepts exactly when
`\(p\)` holds at infinitely many positions, which is exactly the infinite-word
semantics of `\(\mathsf G\mathsf Fp\)`.  This iff is the required source-backed
correctness statement.  Cite `Buchi1962` for B\"uchi acceptance and
`VardiWolper1986` for the general LTL-to-automata connection; the displayed
two-state equivalence is a direct calculation, not a claim that the figure
implements the general translation or the model-checking product construction.

### Multi-agent knowledge and belief (`N-b-011`, `A-080`)

Create separate real sheets:

- `sheet:hilbert-s5n` has, for every agent `\(i\)`, K, T, 4, and 5 plus
  theorem-only `\(K_i\)` necessitation.  Its frames have an equivalence relation
  `\(\sim_i\)` for each agent and no cross-agent interaction axioms.  The
  inherited completeness theorem remains `sketched` with its three named
  omissions.
- `sheet:hilbert-kd45n` has, for every agent, K, D, 4, and 5 plus theorem-only
  necessitation.  Its relations are serial, transitive, and Euclidean; T is
  absent.  The card must say **belief**, not factive knowledge, and its
  completeness is cited to `FaginHalpernMosesVardi1995`.

For a finite nonempty group `\(G\)`, retain the eliminable definition
`\(E_GA:=\bigwedge_{i\in G}K_iA\)`.  Distributed knowledge is a different
operator: `\(D_GA\)` quantifies over worlds related by
`\(\bigcap_{i\in G}\sim_i\)`, representing pooled information.  This exact
semantic intersection explains why `\(D_G\)` is not another spelling of the
conjunction `\(E_G\)`.

### Common knowledge (`D-P10-012`, `N-b-011`, `A-080`)

Create `sheet:hilbert-common-knowledge` as an explicit extension of the chosen
finite-agent S5 system.  Keep the inherited semantics: `\(C_GA\)` holds at a
world iff `\(A\)` holds at every world reachable by a finite path, including
the length-zero path, through `\(\bigcup_{i\in G}\sim_i\)`.  Use the exact
Fagin--Halpern--Moses--Vardi fixed-point and induction presentation:

```text
C_G A -> E_G(A and C_G A)
from B -> E_G(A and B) infer B -> C_G A.
```

The induction rule is theorem-only.  The sheet must not omit its side condition
or replace the rule by an ellipsis.  Cite `FaginHalpernMosesVardi1995` for weak
soundness and completeness.  For `|G| >= 2`, the arbitrary-premise consequence
relation is noncompact: with `\(E_G^0p:=p\)` and
`\(E_G^{n+1}p:=E_GE_G^np\)`, the set
`\(\{E_G^np:n\in\mathbb N\}\)` entails `\(C_Gp\)`, while no finite subset does.
The group-size hypothesis matters: for one S5 agent the iterations collapse.
Therefore never claim strong completeness for arbitrary premise sets.

The muddy-children analysis must fix its information protocol.  There are
`\(n\)` children, exactly `\(k\ge1\)` are muddy, every child sees all other
foreheads but not their own, the father's truthful statement that at least one
child is muddy is a public announcement, questions are synchronous, and every
negative answer is truthful and public.  Under those hypotheses the muddy
children first know that they are muddy at round `\(k\)` (after `\(k-1\)` public
rounds of all-negative answers).  Present this as a cited finite induction
analysis, not as a consequence of common knowledge without the protocol.

### Public announcement logic (`D-P10-011`, `N-b-012`, `A-080`)

For an epistemic model `\(M\)`, let `\(M\mathbin{|}\chi\)` be the submodel
induced by the worlds satisfying `\(\chi\)`.  Define
`\(M,w\models[!\chi]A\)` iff `\(M,w\models\chi\)` implies
`\(M\mathbin{|}\chi,w\models A\)`.  The implication makes a false announcement
precondition vacuously true; the executable dual is
`\(\langle!\chi\rangle A:=\neg[!\chi]\neg A\)`.

Create `sheet:hilbert-pal` over the chosen epistemic base with the exact
reduction schemas

```text
[!chi]p <-> (chi -> p)
[!chi]not A <-> (chi -> not[!chi]A)
[!chi](A and B) <-> ([!chi]A and [!chi]B)
[!chi]K_i A <-> (chi -> K_i[!chi]A)
[!chi][!psi]A <-> [!(chi and [!chi]psi)]A.
```

Together with the epistemic base and replacement through provable
equivalences, these reduce announcement formulas to the static language.  Cite
`Plaza1989` and `VanDitmarschVanDerHoekKooi2007`; `BaltagMossSolecki1998`
supports the broader event-model setting but should not be cited as if its full
action-model language were identical to PAL.

To satisfy the row's unsuccessful-update clause, define locally that an
announcement formula `\(\chi\)` is successful iff `\([!\chi]\chi\)` is valid.
This name is needed to distinguish preservation of the announced content from
mere executability; it is a metalinguistic property of formulas, not a new
modality; it differs from truth before the update; and the Moore-style example
uses it immediately.  In a two-world S5 model where `\(p\)` is true only at the
actual world but the two worlds are indistinguishable to agent `\(i\)`,
`\(p\land\neg K_ip\)` is initially true.  After its truthful public
announcement only the `\(p\)`-world remains, so `\(K_ip\)` becomes true and the
announced formula becomes false.  State the example as cited/checked semantics,
not as a general DEL theorem.

### Tense logic, fusions, and the Phase-4 boundary (`D-P10-006`, `N-b-014`)

At S ceiling, distinguish Prior's unary future/past operators from the binary
strong Until/Since connectives.  On a linear order, Until and Since quantify to
a later or earlier witness and require the left operand at every intervening
point.  Kamp's safe theorem is: every temporal Until/Since formula translates
to monadic first-order logic of order on every chain, and every one-free-variable
monadic first-order formula of order translates back over **Dedekind-complete
chains**.  Cite `Kamp1968`; do not state the converse over arbitrary linear
orders, where Stavi modalities are needed.

Define the fusion of normal modal logics only if the term is used: for disjoint
modal signatures it is the least normal multimodal logic containing the
component theorem sets, with no interaction axioms.  Its standing is a logic
construction, it differs from a product or commuting combination precisely by
the absence of interaction principles, and the tense/multimodal comparison uses
that distinction.  No rule display belongs in the body.

For branching time, an Ockhamist evaluation point is a moment-history pair, so
future-tense truth may depend on the history component through the moment.  A
Peircean evaluation is moment-based and quantifies over branching futures.
State which convention each displayed operator uses; `Burgess1984` does not
license mixing the two satisfaction clauses.  Cite `Prior1967`, `Kamp1968`, and
`Burgess1984` at their exact claims.

`N-b-015` is a could row.  Unless an exact cited hybrid-logic language,
semantics, and real source-exact sheet are built in this visit, insert an explicit
`\hbstub{N-b-015: ...}` naming the owed nominals/satisfaction-operator card and
leave the register row open.  A pointer that merely names hybrid logic is not an
E or S completion.

### 8.3 row and apparatus disposition

| row | ceiling / priority | binding safe delivery |
|---|---|---|
| `D-P10-006` | S / should | Prior/Kamp tense package, defined fusion boundary, and Ockhamist/Peircean distinction. |
| `D-P10-009` | E / must | Separate CTL, CTL*, and modal-mu cards with the three exact real sheets above and A-079 fields. |
| `D-P10-011` | S / should | Distributed knowledge plus PAL semantics, reduction sheet, and unsuccessful-update example. |
| `D-P10-012` | E / must | Common-knowledge semantics, real fixed-point/induction sheet, weak completeness, and noncompactness caveat. |
| `N-b-011` | E / must | S5_n and KD45_n cards/sheets, common knowledge, distributed knowledge, and hypothesis-complete muddy-children analysis. |
| `N-b-012` | S / should | PAL package above; no action-model overreach. |
| `N-b-014` | S / should | Same tense package as D-P10-006, including exact Kamp hypotheses. |
| `N-b-015` | S / could | Exact hybrid card if fully built; otherwise row-named stub and open row. |
| `A-079` | table / must / phase 4 | Four-logics table with the explicit combined-complexity convention and no polynomial parity-game claim. |
| `A-080` | table / must / phase 4 | S5_n, KD45_n, E_G, C_G, D_G, and PAL rows; include the C_G induction rule by sheet pointer. |
| `A-145` | figure / must / phase 4 | Infinite-path evaluation of X, U, F, and G with the tail specified. |
| `A-146` | figure / should / phase 4 | Total CTL tree contrasting existential and universal path quantifiers. |
| `A-147` | figure / should / phase 4 | Two-state deterministic B\"uchi automaton for GFp, exact acceptance condition, and iff correctness caption. |

### 8.3 immediate bibliography and notation ledger

Existing keys usable without intake: `GabbayPnueliShelahStavi1980`,
`Pnueli1977`, `SistlaClarke1985`, `VardiWolper1986`, `ClarkeEmerson1981`,
`Buchi1962`, `Hintikka1962`, `Aumann1976`,
`FaginHalpernMosesVardi1995`, and `Kamp1968`.

Required new bibliography intake keys for this package are
`EmersonHalpern1985`, `ClarkeEmersonSistla1986`, `EmersonLei1987`,
`Reynolds2001`, `Kozen1983`, `Walukiewicz2000`, `EmersonJutla1999`,
`CaludeJainKhoussainovLiStephan2017`, `Plaza1989`,
`BaltagMossSolecki1998`, `VanDitmarschVanDerHoekKooi2007`, `Prior1967`, and
`Burgess1984`.  Their verified metadata belongs in the global bibliography
ledger below; writers must not improvise records from memory.

Notation integration must rehome the existing `\(E_G\)` and `\(C_G\)` rows
from P8.4 to their actual first use in P8.3.  Add exact scoped rows for CTL/CTL*
path quantifiers and paired operators, fixpoint binders and variables,
`\(D_G\)`, announcement modalities, the B\"uchi automaton tuple and acceptance
set, and the source calculus identifiers.  Kozen's fixpoint variables use the
`\(Z\)`-family, so register that source role separately from temporal
`\(\mathsf X\)`.  Temporal eventually retains its source `\(\mathsf F\)` even
though System F has another locally typed role; the current symbol registry
already separates those scopes.

## Research package 8.5: many-valued and fuzzy logics

Status: **STABLE/FROZEN 2026-08-11.**  This package is the binding claim and
evidence surface for the P8.5 writer.  It was checked against v1.1 Part X, the
live registers and registries, the original papers or publisher records listed
below, and the standard monographs already carried by the handbook.  Claims
outside this package require a new research amendment before handbook use.

### Exact inherited source map and evidence ceiling

| v1.1 lines | inherited unit | required disposition |
|---:|---|---|
| 13584--13613 | finite logical matrix and matrix consequence | Migrate both definitions and the warning that the value-set cardinality alone does not determine consequence. |
| 13614--13640 | value-labelled expansion, root family, closure, and saturation | Put the expansion and closure rules only on `sheet:tableaux-matrix`; define labelled formulas, branch compatibility, and saturation before the theorem. |
| 13641--13698 | finite-matrix tableau soundness and completeness | Source-complete after R-037.  This is the sole inherited complete proof in P8.5 and may be `proved=annex:...`. |
| 13700--13729 | strong Kleene matrix and excluded-middle countervaluation | Migrate the exact matrix, designated set, and countervaluation. |
| 13731--13773 | LP matrix, paraconsistency definition, explosion countervaluation, formal-data warning | Migrate without treating the middle value's informal reading as part of the matrix data. |
| 13775--13787 | two exercises | Retire the exercise form.  Preserve the shared K3/LP tableau calculation and the `A\lor\neg A` comparison as examples or table data. |
| 16539--16556 | source solutions to those exercises | Use only as source-accounting support; an exercise solution is not an independent status upgrade. |

The detex alphabetic source count for the proof at 13648--13698 is 477 words.
The work-order reporting band is therefore 191--286 words.  A single faithful
pass may remove repetition but must retain all of the following: termination by
decrease of the unexpanded-complexity measure and finite branching; the
countervaluation-to-compatible-open-branch direction; preservation of
compatibility through expansion; both closure exclusions; the open fully
expanded branch's saturation; unique atomic labels; default values for
unlabelled atoms; the induction extracting a countervaluation; and the root
labels' designated/nondesignated conclusion.  No sketch or new proof in this
package has a percentage denominator.

R-037 is discharged only if saturation is defined before use and the printed
proof actually performs the labelled-formula induction.  Merely saying that a
valuation is “read off” from an open branch would reinstate the repaired defect.

### Finite matrices and the one generic tableau sheet

A finite propositional logical matrix is
`\(\mathcal M=(\mathsf V,D,(f_c)_{c\in\Lang})\)`, where `\(\mathsf V\)` is
finite and nonempty, `\(D\subseteq\mathsf V\)`, and each `\(n\)`-ary
connective has a total operation `\(f_c:\mathsf V^n\to\mathsf V\)`.  Matrix
consequence preserves designation.  Neither `\(D\ne\varnothing\)` nor
`\(D\ne\mathsf V\)` is needed; an empty root family makes the universal
closure test vacuous in exactly the same cases in which consequence is
vacuous.

`sheet:tableaux-matrix` is the only new sheet licensed by this package.  Its
identity must fix a finite matrix, finite premise set, retained labelled
occurrences, and metalinguistic expansion marks.  It has exactly these rule
surfaces:

1. root initialization: one separate root for each designated label choice for
   every premise and each nondesignated conclusion label;
2. value expansion: from `\(c(A_1,\ldots,A_n){:}a\)`, one successor branch for
   each tuple `\((a_1,\ldots,a_n)\)` with
   `\(f_c(a_1,\ldots,a_n)=a\)`, appending every `\(A_i{:}a_i\)` while retaining
   and marking the principal occurrence;
3. atomic clash closure: `\(p{:}a\)` and `\(p{:}b\)` close when `\(a\ne b\)`;
4. empty-preimage closure: a compound label closes when no input tuple maps to
   its displayed value.

A saturated branch contains, for each labelled compound on it, all component
labels of at least one input tuple realizing that compound's label.  This term
is a metalinguistic branch property, differs from merely having no visibly
unmarked occurrence, and is used in countervaluation extraction.  The body may
state these definitions but may not redisplay an expansion or root rule.

The generic theorem has the exact finite surface:

> For every fixed finite matrix `\(\mathcal M\)`, finite formula set
> `\(\Gamma\)`, and formula `\(B\)`, every tableau in the prescribed root
> family closes iff `\(\Gamma\entails_{\mathcal M}B\)`.

The theorem is not an adequacy theorem for infinite matrices, first-order
languages, or arbitrary premise sets.  Its termination proof also gives a
decision procedure for finite-matrix finite-premise consequence.

### K3 and LP cards, exact facts, and duality

Both inherited cards use the constant-free propositional language generated
from variables by `\(\neg,\land,\lor\)`.  This boundary is necessary for the
tautology claims below.  Adding truth constants changes the K3 theorem set.

For strong Kleene `\(\mathbf K_3\)`, take
`\(\mathsf V=\{0,\tfrac12,1\}\)`, `\(D=\{1\}\)`,
`\(\neg a=1-a\)`, `\(a\land b=\min(a,b)\)`, and
`\(a\lor b=\max(a,b)\)`.  For LP, use those same numerical operations but
designate `\(D=\{\tfrac12,1\}\)`.  The informal K3 reading “neither” and LP
reading “both” are not additional semantic coordinates; the designated set is
what changes consequence.  Cite `Kleene1952` for K3 and `Priest1979` for LP.

The following exact D-P10-027 statement may be given one complete new local
annex proof, with no ratio target, or may remain cited to
`Priest1979,OmoriWansing2017`:

1. `\(\mathbf K_3\)` has no tautologies in the fixed constant-free language,
   because assigning `\(\tfrac12\)` to every variable gives every formula
   value `\(\tfrac12\)`.
2. LP has exactly the classical tautologies in that same truth-functional
   signature.  “Exactly” compares theorem sets, not consequence relations.
3. For finite premise and conclusion sets, with multiple-conclusion consequence
   meaning that designation of all premises forces designation of some
   conclusion,
   `\(\Gamma\entails_{\mathbf K_3}\Delta\)` iff
   `\(\neg\Delta\entails_{\mathsf{LP}}\neg\Gamma\)`.  The sets on both sides
   are negated memberwise.  Do not shorten this to an unqualified
   single-conclusion “K3--LP duality.”

The K3 and LP cards both point to `sheet:tableaux-matrix`.  Their adequacy and
decidability fields may be locally `proved` by distinct annex items: adequacy
specializes the generic finite-matrix theorem; decidability enumerates the
finitely many valuations of the variables in the finite input.  These are new
short proofs and must not be ratio-tuned.

### FDE and the four-valued square

Use the inspected Omori--Wansing algebra/value names and give them the
support-pair representation
`\(\mathrm{BD}=\{(0,1),(0,0),(1,1),(1,0)\}\)` with values
`\(f,n,b,t\)`, respectively.  For
`\(x=(x^+,x^-)\)` and `\(y=(y^+,y^-)\)`, define

```text
not x       = (x-,x+)
x and y     = (x+ and y+, x- or y-)
x or y      = (x+ or y+, x- and y-).
```

Designate exactly the values with positive support, `\(\{t,b\}\)`.  This is
the cited propositional FDE matrix.  Omori--Wansing's truth order is
`\(x\leq_t y\)` iff `\(x^+\leq y^+\)` and
`\(y^-\leq x^-\)`; its knowledge order is
`\(x\leq_k y\)` iff `\(x^+\leq y^+\)` and
`\(x^-\leq y^-\)`.  The names are needed because the two orders compare
different coordinates, are exact relations on matrix values rather than new
consequence relations, and are used immediately to explain the bilattice
reading.  Cite `Dunn1976`, `Belnap1977`, and `OmoriWansing2017`.

K3 is the submatrix on `\(\{f,n,t\}\)` with only
`\(t\)` designated.  LP is the submatrix on
`\(\{f,b,t\}\)` with `\(b,t\)`
designated.  FDE contains both middle values.  It is paraconsistent because
`\(p=b,q=f\)` refutes explosion, and paracomplete because
`\(p=n\)` refutes excluded middle.  A full FDE card may point to the
generic matrix sheet and use the same new specialization/enumeration proofs as
the K3 and LP cards.

### Weak Kleene and the Bochvar boundary

For A-084 only, the weak Kleene matrix row may use
`\(\{0,\tfrac12,1\}\)`, designated set `\(\{1\}\)`, and the infectious
operations: any compound having an immediate argument `\(\tfrac12\)` receives
`\(\tfrac12\)`; otherwise the classical operation is used.  Cite
`Kleene1952`.  This supplies the matrix comparison row.

It does not supply Bochvar's full external logic.  That logic enriches the
internal weak-Kleene language with external assertion machinery, so identifying
the full Bochvar system with the bare infectious matrix would collapse a real
language distinction.  D-P10-025 is `could`; unless the external operators and
their exact calculus are separately researched and registered, insert an
explicit `\hbstub{D-P10-025: ...}` saying that A-084 supplies only the weak
Kleene matrix row and leave the depth row open.

### Lukasiewicz matrices, completeness, and McNaughton's theorem

For `\(n\geq2\)`, Cignoli, D'Ottaviano, and Mundici write the finite
Lukasiewicz chain itself as

```text
\text{\L}_n = {0, 1/(n-1), ..., 1},   D = {1},
not x = 1-x,                          x \Rightarrow y = min(1,1-x+y).
```

The chain symbol `\(\text{\L}_n\)` names the displayed value algebra, not a
separately named calculus and not a second carrier `\(\mathsf V_n\)`.
Hajek writes the standard infinite-valued logic as the stroked
`\(\text{\L}\)`; its standard value algebra is `\([0,1]\)` with the same
operations.  Derived strong conjunction is
`\(x\mathbin{\ast_{\text{\L}}}y=\max(0,x+y-1)\)`; weak conjunction and
disjunction are minimum and maximum.  The finite systems based on
`\(\text{\L}_n\)` are covered by `sheet:tableaux-matrix`; the infinite
standard matrix is not.

The full D-P10-020/N-b-028 entry must distinguish three completeness surfaces:

- the standard Lukasiewicz--Tarski Hilbert axiomatization, cited to
  `LukasiewiczTarski1930,Hajek1998`;
- theoremhood and finite-premise consequence complete for the standard
  `\([0,1]\)` matrix;
- arbitrary-premise strong completeness stated algebraically for MV-algebras,
  not silently transferred to the single standard matrix.

Consequence for the finite `\(n\)`-valued systems based on
`\(\text{\L}_n\)` is decidable by the generic finite-matrix tableau.
Infinite-valued theoremhood has McNaughton's exact functional
characterization: an `\(m\)`-variable truth function is represented by a
Lukasiewicz formula iff it is a continuous piecewise-linear map
`\([0,1]^m\to[0,1]\)` whose linear pieces have integer coefficients.  Cite
`McNaughton1951` and `CignoliDOttavianoMundici2000`.  Do not claim the theorem
for arbitrary continuous functions or use it as an arbitrary-premise strong
completeness theorem.

### T-norm fuzzy logics and the standard-completeness boundary

A t-norm is a commutative, associative, coordinatewise monotone operation
`\(\ast:[0,1]^2\to[0,1]\)` with unit `\(1\)`.  Following Hajek, fix the
t-norm locally and write its residuum without a handbook subscript:
`\(x\Rightarrow y=\sup\{z:x\ast z\leq y\}\)`.  These operations are needed
to distinguish the truth function for strong conjunction from the lattice
minimum and the semantic residuum from the object-language implication; their
standing is algebraic/semantic, and A-085 uses them in every row.

The exact standard operations are:

| logic | t-norm `\(x\ast y\)` | residuum `\(x\Rightarrow y\)` | safe axiomatic description | safe completeness surface |
|---|---|---|---|---|
| MTL | every left-continuous t-norm | the displayed residuum | Esteva--Godo's MTL Hilbert calculus; algebraically, prelinear commutative integral bounded residuated lattices | algebraic completeness for linearly ordered MTL-algebras (`EstevaGodo2001`); standard theoremhood completeness over all left-continuous t-norms (`JeneiMontagna2002`) |
| BL | every continuous t-norm | the displayed residuum | MTL plus divisibility; equivalently BL-algebras | standard theoremhood/finite-premise completeness over all continuous t-norms (`CignoliEstevaGodoTorrens2000`) |
| `\(\text{\L}\)` | `\(x\mathbin{\ast_{\text{\L}}}y=\max(0,x+y-1)\)` | `\(\min(1,1-x+y)\)` | BL plus involution; algebraically MV-algebras | standard theoremhood/finite-premise completeness; arbitrary-premise algebraic completeness (`Hajek1998,CignoliDOttavianoMundici2000`) |
| Goedel | `\(\min(x,y)\)` | `\(1\)` if `\(x\leq y\)`, otherwise `\(y\)` | BL plus idempotence | standard theoremhood completeness for the Goedel chain; algebraic completeness for Goedel algebras (`Hajek1998`) |
| `\(\Pi\)` | `\(x\mathbin{\ast_{\Pi}}y=xy\)` | `\(1\)` if `\(x\leq y\)`, otherwise `\(y/x\)` | Hajek's exact two-schema Product extension of BL | standard theoremhood completeness for the Product chain; algebraic completeness for product algebras (`Hajek1998`) |

A-085 may reproduce this comparison as semantic equations and source pointers;
it must not display unregistered Hilbert schemas in the body or imply that a
live P8.5 Hilbert sheet exists.  In particular, BL means continuous t-norms and
MTL left-continuous t-norms.  Standard theoremhood or finite-premise
completeness must not be rewritten as arbitrary-premise strong standard
completeness.

### Supervaluations

For D-P10-026, follow Fine's own specification-space presentation rather than
inventing a carrier named `\(\operatorname{Adm}\)`.  A specification space is
a partially ordered collection of specification-points, with the order
recording extension of information.  At a base-point, quantify over its
complete admissible extensions: a formula is supertrue iff it is true at every
such extension, superfalse iff it is false at every such extension, and
otherwise indeterminate.  Admissibility is a primitive constraint on
specifications, and a base-point is completeable when it has at least one
complete admissible extension.  These are metalinguistic semantic data, not a
third truth value or a matrix operation.  Cite `Fine1975`.

Every classical tautology is supertrue because every complete admissible
specification is classical.  A compound may be supertrue while a constituent
is indeterminate: if complete admissible specifications extending one
base-point disagree on `\(p\)`, they still all make `\(p\lor\neg p\)` true.
The converse “every supertrue formula is a classical tautology” holds only
when every complete classical specification is an admissible completion of the
base-point; do not assert it for an arbitrarily restricted completion family.

### Row, apparatus, exercise, and proof-graph disposition

| row | ceiling / priority | frozen delivery |
|---|---|---|
| `D-P10-020`, `N-b-028` | E / must | Full finite/infinite Lukasiewicz entry: matrices, exact completeness boundaries, axiomatization source, McNaughton theorem, and finite-matrix tableau pointer. |
| `D-P10-021`, `N-b-029` | S / should+must | T-norm/residuum definition plus MTL, BL, Lukasiewicz, Goedel, and Product survey with exact continuity and completeness qualifications. |
| `D-P10-023` | S / could | Explicit row-named stub unless a concrete cited Post family, language, matrices, and theorem are supplied. |
| `D-P10-024`, `N-b-025` | E / should+must | Full FDE card with pair semantics, two orders, K3/LP submatrices, generic sheet, and exact paraconsistent/paracomplete examples. |
| `D-P10-025` | S / could | A-084 weak-Kleene matrix row plus explicit stub for the still-unresearched full Bochvar external logic. |
| `D-P10-026` | S / should | Exact supervaluation definition, classical-tautology preservation, and constituent/compound example, cited to Fine. |
| `D-P10-027` | S / must | Language-bounded K3 no-tautology theorem, LP=CPL theorem-set statement, and finite multiple-conclusion duality. |
| `A-084` | table / must / phase 4 | K3, LP, weak Kleene, FDE, and finite Lukasiewicz rows with values, designated sets, operations, theorem-set facts, and exact boundaries. |
| `A-085` | table / should / phase 4 | The t-norm table above, including MTL/BL continuity and standard-versus-algebraic completeness boundaries. |
| `A-165` | symbols / must | Rehome inherited matrix data to P8.5 and add only the scoped identifiers/operations listed below. |
| `A-182` | bibliography / must | Existing keys plus the two new verified standard-completeness entries below; correct the live Esteva--Godo DOI. |
| `A-189` | navigation / should | All three cards point to `sheet:tableaux-matrix`; finite Lukasiewicz points to it without implying coverage of the infinite matrix; every proved body/card field points to one unique annex item. |

The first source exercise is retired as an exercise and preserved by the
generic theorem plus an example noting that the K3 and LP root sets differ even
when the expansion shape is shared.  The second is preserved by the exact
`\(p\lor\neg p\)` K3/LP comparison.  Record both dispositions in file comments.

The intended local status graph has one inherited `proved` generic theorem and
new, non-ratio-tuned specialization/decision proofs for each full K3, LP, and
FDE card.  If D-P10-027 receives a local proof, that is another new proof with
no denominator.  Cited Lukasiewicz, t-norm, McNaughton, and supervaluation
results receive no annex items.

### Verified bibliography and notation ledger

Existing usable keys are `Kleene1952`, `Priest1979`, `Dunn1976`,
`Belnap1977`, `OmoriWansing2017`, `Lukasiewicz1920`,
`LukasiewiczTarski1930`, `McNaughton1951`,
`CignoliDOttavianoMundici2000`, `Hajek1998`, `EstevaGodo2001`,
`CintulaHajekNoguera2011`, and `Fine1975`.

Two new shared bibliography entries are required:

```bibtex
@article{CignoliEstevaGodoTorrens2000,
  author       = {Cignoli, Roberto and Esteva, Francesc and Godo, Llu\'{i}s and Torrens, Antoni},
  title        = {Basic Fuzzy Logic Is the Logic of Continuous t-Norms and Their Residua},
  journaltitle = {Soft Computing},
  volume       = {4},
  pages        = {106--112},
  year         = {2000},
  doi          = {10.1007/s005000000044},
}
@article{JeneiMontagna2002,
  author       = {Jenei, S\'{a}ndor and Montagna, Franco},
  title        = {A Proof of Standard Completeness for Esteva and Godo's Logic {MTL}},
  journaltitle = {Studia Logica},
  volume       = {70},
  number       = {2},
  pages        = {183--192},
  year         = {2002},
  doi          = {10.1023/A:1015122331293},
}
```

The live `EstevaGodo2001` record has an incorrect final DOI digit.  The
publisher record is `10.1016/S0165-0114(01)00098-7`, not `...00098-9`.
This is a shared-bibliography correction for the finalizer, not a writer edit.

Notation integration must:

- rehome existing `\(\mathsf V\)`, `\(D\)`, and `\(f_c\)` rows from P8.7 to
  first use P8.5;
- add scoped identifiers `\(\mathbf K_3\)`, `\(\mathsf{LP}\)`, and
  `\(\mathbf{FDE}\)`; leave the inherited weak-Kleene matrix unnamed because
  its controlling source supplies no symbolic system identifier;
  Cignoli--D'Ottaviano--Mundici's finite-chain symbol `\(\text{\L}_n\)`,
  Hajek's infinite-logic identifier `\(\text{\L}\)`, `\(\mathsf{MTL}\)`,
  `\(\mathsf{BL}\)`, `\(\mathsf G_\infty\)`, and Hajek's Product-logic
  identifier `\(\Pi\)`;
- add the value-label notation `\(A{:}a\)`, Omori--Wansing's algebra/value
  names `\(\mathrm{BD}\)` and `\(f,n,b,t\)`, and its two orders
  `\(\leq_t\)`, `\(\leq_k\)`;
- add t-norm `\(\ast\)`, its locally typed plain residuum `\(\Rightarrow\)`,
  the source subscripts `\(\ast_{\text{\L}}\)` and `\(\ast_{\Pi}\)`, and
  Fine's specification-point/extension apparatus without an invented
  `\(\operatorname{Adm}\)` glyph;
- reuse the global valuation `\(v\)` and per-system semantic turnstile rather
  than create duplicate glyph roles.

The plain `\(\Pi\)` is Hajek's Product-logic identifier and must coexist
locally with the global formula-context metavariable; the registry records the
operand and role rather than renaming either occurrence.  Do not use
`\(\otimes\)` for a t-norm unless a cited presentation does so.  Do not identify FDE's information order with
its truth order, or the LP middle value with the K3 middle value inside the FDE
pair presentation.

### Frozen entry-card contract for 8.5

The handover's mandatory inherited-card list for P8.5 is K3 and LP.  FDE may
and should receive a card because N-b-025 supplies a full finite matrix and the
same exact generic sheet.  The full-card rule is therefore satisfied by those
three source-fixed systems: every one points to `sheet:tableaux-matrix` and has
status-bearing adequacy and decidability fields.

Treatment `E` in D-P10-020/N-b-028 means a full topical entry, not
automatically a `systementry` card.  Deliver that ceiling through the exact
finite/infinite matrices, axiomatization source, completeness distinctions,
McNaughton statement, and finite-sheet pointer.  Do **not** print an infinite
Lukasiewicz card: this package licenses no exact infinite-valued Hilbert sheet,
and the generic finite-matrix tableau is inapplicable to `[0,1]`.  N-b-029 has
ceiling `S`; its t-norm family deliverable is the exact definition, cited
survey statement, and A-085 table, not five cards with invented calculus
fields.  The body must state this boundary explicitly, and verification must
record these rows as statement/table deliveries rather than card deliveries.

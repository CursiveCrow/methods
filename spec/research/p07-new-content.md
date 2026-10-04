# P7 research: proof theory and lambda-calculi migration

Status: **FROZEN 2026-08-11** -- claim-safe evidence ledger for the Phase-4
Part 7 visit. This is
research support, not handbook prose. It does not change a register, add a
bibliography or symbol row, establish a proof status, or itself satisfy a
treatment row. The frozen `v1.1-verified` Part VIII, the live registers, the
current handbook and registry, original publications, and authoritative
publisher or author archives were checked on 2026-08-11.

## Evidence policy and claim boundary

- **Source-verified** means checked in the frozen v1.1 source at the exact line
  range recorded below. Register line references still denote `v1.0-audit`, so
  this ledger gives a v1.0/v1.1 crosswalk.
- **Primary-verified** means checked against the original publication or an
  official publisher, journal, author, or institutional archive.
- **Authoritative-secondary** means checked against an identified research
  monograph or handbook chapter. It is not converted into a local proof.
- **Derived** means a consequence whose complete local argument is stated in
  this ledger. It is not a source citation by itself.
- `E`, `T`, `S`, and `P` are register treatment ceilings: full entry, table or
  sustained tabular treatment, statement/survey, and pointer. They are not
  proof-status words.
- Status is governed by `handbook/CONVENTIONS.md`: source-complete proofs may
  become `proved=annex:...`; source sketches remain
  `sketched=annex:...` with every omission named; source-cited theorems remain
  `cited=<key>` and receive no annex item. A new argument is `proved` only if
  its annex actually supplies every load-bearing case.
- Body files state results and point to rule sheets. Rule schemata, including
  Mix and any System-T or generalized-calculus rules, live only under
  `handbook/registry/calculi/`.

## Executive rulings and blockers

1. **There is no license to upgrade Craig or Beth.** Frozen v1.1 records both
   as cited theorems (11921--11951). `D-P8-004` and `N-a-070` demand a full
   Maehara treatment, but the campaign's non-upgrade rule still controls the
   theorem statuses. The safe delivery is a complete method/lemma entry for
   Maehara's partition induction and a cited Craig/Beth entry. Printing the
   same Craig statement under a second `proved` label would be status
   laundering. If the row literally requires a locally proved Craig theorem,
   the contract and register conflict and the user must resolve it.
2. **Cut elimination is for two exact calculi only.** The source theorem is a
   sketch for the displayed defined-negation `LK` variant and equality-free
   `LJ`; it does not cover canonical primitive-negation `sheet:lk`,
   `sheet:lk-eq`, induction, modal rules, or other extensions.
3. **Mix is currently homed on the wrong proof-theorem surface.** The exact
   R-012 Mix rules must be added to `sheet:lk-defneg` and `sheet:lj`. Mix on
   `sheet:lk` is structurally derivable and may remain, but its comments must
   not claim that the Part-VIII reduction proves cut elimination there. Mix on
   `sheet:lk-eq` is likewise equipollent with primitive Cut, but R-042 forbids
   treating that fact as equality cut elimination.
4. **Canonical-LK equivalence is not automatically a cut-free translation.**
   Derivability equivalence between the primitive-negation/contexted-initial
   calculus and the defined-negation/uncontexted-initial calculus does not by
   itself transport a cut-free proof. A cut-free-preservation theorem would
   need its own rule-by-rule proof.
5. **`D-P8-001` cannot exceed the P2 evidence.** The current canonical
   first-order LK completeness theorem assumes Choice and is
   `sketched=annex:p2.2.14`; the propositional theorem is
   `sketched=annex:p2.3.8`. P7 may give the demanded full lookup entry and
   proof-theoretic cross-reference, but it may not silently call either proof
   complete or cut-free.
6. **The Church--Rosser proof is a new sketch, not migrated proof evidence.**
   The handover explicitly calls for a Tait--Martin-Loef parallel-reduction
   annex sketch. It must omit-name the parallel-substitution lemma, every
   diamond-induction case (especially beta/application overlap), and the
   equivalence between beta closure and parallel closure unless those are
   fully supplied.
7. **System F decision claims must distinguish presentations.** Church-style
   System F with explicit type abstraction/application and annotated term
   binders has decidable checking. Wells's undecidability theorem concerns the
   Curry-style assignment system: typability and type checking there are
   equivalent and undecidable. A single unqualified table cell is false.
8. **There is no unqualified MLTT metatheorem.** Syntax, universes,
   definitional equality, eta laws, inductive types, and extensionality change
   normalization and checking. State one intensional calculus, then cite the
   theorem for that calculus. Abel--Coquand--Dybjer proves decidability of
   typed beta-eta equality for a specified Martin-Loef type theory with a
   Russell universe; it is not a theorem about every system called MLTT or
   CIC.
9. **Gentzen's imported result stays relative.** The existing source boundary
   at 12139--12216 is mathematically sound and must survive. `N-a-049` adds a
   demanding T-level obligation: the selected propositional core, reduction
   clauses, ordinal assignment, and every propositional decrease case must be
   fully displayed. A schematic arrow labelled "decreases" does not satisfy
   that row and does not prove `Con(PA)`.
10. **A proof-theoretic ordinal is calibration-relative.** Define a stated
    formula class, recursive notation/order, base theory, and induction or
    reduction notion. Do not use bare `|T|`: vertical bars are reserved for
    cardinality. The Feferman--Schuette `Gamma_0` boundary is a result about
    particular autonomous predicative progressions, not an uncontested
    absolute definition of predicativity.
11. **Basic number realizability does not refute Markov's principle.** Under
    classical metareasoning Kleene number realizability validates MP, and
    formal number realizability is characterized by an extension involving
    ECT. Any independence claim needs the exact alternative interpretation or
    Kripke/model theorem. Do not write that Kleene's 1945 relation by itself
    proves `HA` independent of MP.
12. **The v1.1 normalization theorem is too small for HA.** It explicitly
    excludes equality and induction. Therefore it cannot by itself prove the
    disjunction and numerical existence properties of HA. A complete local HA
    proof needs normalization/cut elimination for a fixed arithmetic calculus,
    or the result must remain cited. The IPC disjunction argument inherits the
    cut-elimination sketch if that sketch is its only premise.
13. **The generalized-calculi row needs modal-specific sources.** Guglielmi's
    2007 BV paper defines deep inference but is not a worked modal calculus.
    Use Stouppa's S5 system for the modal deep-inference example. Likewise,
    each hypersequent, labelled, and display example must name one fixed rule
    surface; a generic diagram is not an adequacy proof.
14. **A-074 and A-069 are Phase 6.** P7 still owes the local calibration table
    required by `D-P8-006`, but neither global apparatus row may be flipped to
    done during Phase 4 merely because a P7 precursor exists.
15. **No direct source proof may be discarded merely to hit a percentage.**
    The Tier-2 target is 40--60% of source length, but logical completeness is
    controlling. The five-line subformula proof is already irreducible enough
    that preserving its induction is more important than a mechanical line
    ratio.

## Binding inventory

### Depth rows targeting P7 (10)

| row | ceiling / priority | binding delivery and safe evidence |
|---|---|---|
| `D-P8-001` | E / must | Arbitrary finite-multiset LK sequent completeness lookup. Preserve the P2 Choice hypothesis and sketch status; distinguish propositional and first-order forms and canonical from defined-negation LK. Depends on R-014. |
| `D-P8-002` | E / must | Exact derivability-equivalence theorem for a fixed classical ND and LK pair. Define the finite-disjunction translation, empty succedent, formula translation, and whether equality is excluded. No proof-identity or cut-free-preservation claim. |
| `D-P8-003` | S / should | Midsequent theorem and Herbrand route with exact prenex/equality-free hypotheses. Cited or sketched only because it depends on R-012 cut elimination; cross-reference P2 Herbrand entries. |
| `D-P8-004` | E / must | Maehara partition lemma/method with all rule cases owed, followed by cited Craig and Beth. Contract conflict if "proved Craig" is interpreted as a status upgrade. |
| `D-P8-005` | S / should | Derivation coding, selected notation grammar/order, ordinal assignment, reduction, decrease lemma, induction schema, and consistency extraction separated. `N-a-049` raises the shared delivery to T. |
| `D-P8-006` | T / should | Calibration-relative definition plus table through PA and `Gamma_0`, with P6 ordinal arithmetic as prerequisite. A-074 remains Phase 6. |
| `D-P8-007` | S / should | Cook--Reckhow framework, exact resolution/PHP lower bound, Frege/extended-Frege map, and open lower-bound boundary. |
| `D-P9-003` | E / must | Untyped lambda terms, alpha-equivalence, capture-avoiding substitution, beta reduction/conversion, confluence theorem, parallel-reduction method sketch, and normal-form corollary. This E ceiling dominates `N-a-015`'s T. |
| `D-P9-004` | S / should | System F syntax/judgments, impredicativity, Curry--Howard reading, cited strong normalization, and the Church/Curry decision distinction. `N-c-029` raises priority to must. |
| `D-P10-031` | P / could | Explicit `\hbstub` naming the row. The substantive generalized-calculi survey is separately required by `N-a-057`; do not falsely mark this could row done. |

### New-content rows targeting P7 (20)

| row | ceiling / priority | binding disposition |
|---|---|---|
| `N-a-015` | T / must | Untyped lambda/combinatory comparison, Church--Rosser, and the cited equivalence of lambda-definable and partial-recursive numerical functions. Shared topic delivered at E under `D-P9-003`. |
| `N-a-049` | T / must | Gentzen components and a full ordinal assignment for the explicitly selected propositional core. Preserve the cited/relative PA boundary. |
| `N-a-050` | S / should | Normal Veblen hierarchy, `Gamma_0`, and the qualified Feferman--Schuette statement; beyond-`Gamma_0` impredicative analysis pointer only. |
| `N-a-051` | S / should | One exact PRA presentation, Skolem 1923 history, and Tait's argued finitist thesis, labelled as an analysis rather than a settled equivalence theorem. |
| `N-a-052` | S / could | Explicit `\hbstub{N-a-052: ...}` for omega logic; do not mix an omega-rule into the finitary Gentzen theorem. |
| `N-a-053` | S / should | System T rules on a registry sheet; fixed Dialectica translation and cited HA soundness/consistency corollary. |
| `N-a-054` | T / must | Full Kleene number-realizability clauses, HA soundness, ECT characterization/consistency application, and a separately sourced MP boundary. No realizability-topos expansion. |
| `N-a-055` | T / must | IPC/HA disjunction and HA numerical-existence statements with exact closedness hypotheses. Local proof status only if the fixed normalization or realizability extraction theorem is fully available. |
| `N-a-056` | S / should | Epsilon terms/critical formulas and cited first, extended-first, and second epsilon theorems; connect but do not duplicate P2 Herbrand forms. |
| `N-a-057` | S / should | Definitions of hypersequents, labelled sequents, display calculi, and deep inference, plus one source-backed modal example for each. All displayed rules must be registry-owned. |
| `N-a-058` | P / could | Explicit stub/pointer to proof mining with the row ID; no extraction theorem beyond the P ceiling. |
| `N-a-069` | S / should | Same delivery as `D-P8-003`; identify the proof-theoretic route separately from the epsilon-calculus route. |
| `N-a-070` | E / must | Same Maehara/Craig/Beth disposition as `D-P8-004`; cited theorem statuses remain binding. |
| `N-c-027` | S / should | Cook--Reckhow definitions, Haken PHP lower-bound sketch with omissions, Frege open-problems map; shared with `D-P8-007`. |
| `N-c-029` | S / must | System F entry; shared with `D-P9-004`, with must priority controlling. |
| `N-c-030` | S / must | One intensional MLTT entry: judgment forms, Pi/Sigma/identity types, universes, proof relevance, and exact cited normalization/checking claims. CIC is a clearly separate overview/pointer. |
| `N-x-001` | P / excluded | At most a one-page HoTT/univalence pointer. Do not treat it as Phase-4 substantive content. |
| `N-x-002` | P / excluded | Higher inductive and cubical internals remain subsumed under the HoTT pointer. |
| `N-x-011` | P / excluded | Geometry of interaction pointer only. |
| `N-x-012` | P / excluded | Proof nets pointer only; no correctness criterion or net-based cut-elimination development. |

### P7 apparatus ledger

Direct Phase-4 P7 apparatus is the following. Priority is the register's
requirement; "safe minimum" does not lower it.

| row | phase / priority | safe minimum |
|---|---|---|
| `A-070` | 4 / must | Structural rules for exact named sheets, not logic families in the abstract. LK/LJ, IMLL, a fixed relevance calculus, affine calculus, and Lambek calculus; say whether exchange is built into context syntax and distinguish primitive Cut from admissible Cut. |
| `A-071` | 4 / should | LK/LJ/NK/NJ catalog plus pointer rows for hypersequent/display/deep inference; every row names a real sheet or says citation-only and records the actual adequacy status. |
| `A-072` | 4 / must | Logic/type/category dictionary with fixed bicartesian/cartesian-closed hypotheses and proof/term quotients stated. |
| `A-073` | 4 / must | Untyped, STLC, Church-style System F, Curry-style System F, and the exact MLTT calculus separated on confluence, strong normalization, checking, and typability. |
| `A-075` | 4 / should | Resolution, Frege, and extended Frege: proof objects, known PHP bounds, and proven/open simulation relations. |
| `A-151` | 4 / should | Curry--Howard triangle; label the three edges and qualify the categorical vertex by the selected categorical semantics. |
| `A-152` | 4 / must | A complete STLC typing derivation beside its intuitionistic ND derivation; instances may appear in the body, but generic rule schemata stay in registry sheets. |
| `A-186` | 4 / must, shared | P7 further reading grouped by sequent/normalization, lambda/type theory, ordinal analysis, interpretations, and proof complexity. |
| `A-189` | 4 / should, shared | Body links to exact rule sheets and annex IDs; forward links to not-yet-built parts remain prose until finalization. |

`A-069` (master consistency-strength ladder) and `A-074` (global ordinal
calibration table) are both `phase=6`. P7 may produce their local source data,
but neither row is a Phase-4 completion. `A-153` is the P8 substructural-family
figure, not a P7-owned figure, even though A-070 supplies some of its data.

### Defect constraints carried into P7

| defect | live requirement |
|---|---|
| `R-012` | Display and label Mix; use the Mix formula rank and sum of immediate-subderivation heights; no complete-proof corollary may rest on the sketch. Fixed in source, but migration must preserve the repair. |
| `R-042` | Name LK and LK-with-equality separately; the cut-elimination claim excludes equality; state that the existing symmetry derivation uses Cut. Still open. |
| `S-012` | Canonical LK is the Parts II/III primitive-negation/contexted-initial presentation. Part VIII is a named defined-negation variant with a labelled derivability-equivalence theorem. Still open. |
| `S-013` | Define "analytic derivation" at first use or retitle. Safe definition is calculus-relative: propositional cut-free plus the subformula property; first-order requires substitution/eigenvariable qualification. Still open. |
| `L-001` | Preserve the brace-protected discharge annotation at v1.1 11983; do not reintroduce the matrix optional-argument compile bug. Fixed. |
| `L-005` | Rule displays are registry-generated. Never revive the retired body rule macro. Still open/obsolete by migration. |

## Frozen source crosswalk and status map

Current `source/formal-logic-reference.tex` is byte-identical in content to
`v1.1-verified` for this part. Part VIII occupies v1.0 lines 9135--9948 and
v1.1 lines 11354--12248.

| source unit | v1.0-audit | v1.1-verified | migration/status disposition |
|---|---:|---:|---|
| Part/chapter framing and metavariables | 9135--9158 | 11354--11377 | Compress to lookup framing; retain local metavariable declarations. |
| Sequent/context definitions | 9160--9193 | 11379--11412 | Body definitions; preserve finite-multiset and single-succedent distinctions. |
| Defined-negation LK rules | 9195--9299 | 11414--11518 | Registry `sheet:lk-defneg`; body references only. |
| LJ rules | 9301--9391 | 11520--11610 | Registry `sheet:lj`; body references only. |
| LK soundness | 9393--9407 | 11612--11626 | Source proof sketch; migrate only as `sketched`, naming omitted rule cases. |
| Cut-free example | 9409--9424 | 11628--11643 | Optional worked-derivation lookup or deliberate retirement; not a rule display. |
| Primitive/derived/admissible, warning, principal formula | 9426--9475 | 11645--11694 | Keep concise definitions and calculus-dependence warning. |
| Two calculus exercises | 9477--9490 | 11696--11709 | Retire as exercises; account for admissibility and translation substance in entries. |
| Rank/height and R-012 Mix apparatus | 9492--9511 plus repaired insertion | 11711--11776 | Body method and registry rules. Formula rank and derivation height remain distinct. |
| Cut/mix equipollence | absent before repair | 11741--11766 | Complete proof: Tier-2 annex item, compressed only if all contraction/cut directions remain. |
| Cut elimination | 9513--9548 | 11778--11822 | Tier-1 method; `sketched`; omissions are the full commuting/principal reduction table and every excluded extension. |
| Cut-free subformula lemma | inserted by repair | 11824--11841 | Complete Tier-2 proof; retain induction on derivation height. |
| Propositional subformula corollary | 9555--9573 | 11843--11856 | Proof sketch because it uses the cut-elimination sketch. |
| First-order qualification | repaired insertion | 11858--11864 | Keep exactly: subformula modulo term substitution and eigenvariable renaming. |
| Empty-sequent underivability | 9575--9586 | 11866--11880 | Proof sketch because it uses the cut-elimination sketch. |
| Consequences/boundary | 9588--9605 | 11882--11899 | Preserve, especially non-elementary blow-up and extension warning. |
| Two cut exercises | 9607--9618 | 11901--11912 | Retire as exercises; use their substance only where an entry requires it. |
| Craig interpolation | 9620--9643 | 11914--11937 | Cited theorem; no annex item. New Maehara material cannot upgrade it. |
| Beth definability | 9645--9659 | 11939--11959 | Cited theorem; no annex item. |
| ND normalization and exact calculus boundary | 9661--9728 | 11961--12028 | Proof sketch; excludes RAA, primitive negation, and equality, and contains no arithmetic induction. |
| STLC syntax, subject reduction, strong normalization | 9730--9799 | 12030--12099 | Definitions plus two proof sketches; do not upgrade. |
| Curry--Howard section | 9801--9831 | 12101--12131 | Compress into entry/table/figures; preserve the fixed-calculus warning. |
| Ordinal-analysis boundary | 9833--9916 | 12133--12216 | Cited, analysis-relative Gentzen result plus internal proof boundary; preserve in substance. |
| Two typing exercises | 9918--9929 | 12218--12229 | Retire as exercises; A-152 absorbs the first example and the substitution warning absorbs the second. |
| Abstract reduction definitions | 9931--9940 | 12231--12240 | Keep as lookup definitions; distinguish weak from strong normalization. |
| Final reduction exercise | 9942--9947 | 12242--12247 | Retire as exercise; its implication/counterexample may become a table note if useful. |

### Annex proof obligations

- **Tier 1:** cut elimination for `sheet:lk-defneg` and `sheet:lj`.
  The body method must name the transform, input/output derivations, Mix
  generalization, lexicographic measure
  `(rank(A), h(D_1)+h(D_2))`, contraction case, principal case, eigenvariable
  renaming, and termination. The annex begins with a `\sketchnote` naming the
  omitted complete reduction table. Equality, induction, modal, fixed-point,
  and infinitary extensions are outside the claim.
- **Tier 2:** cut/mix equipollence. Preserve both directions: Cut is Mix with
  `m=n=1`; a general Mix is derived by `m-1` right contractions, `n-1` left
  contractions, and one Cut (only the left contractions are needed in LJ).
- **Tier 2:** cut-free propositional subformula lemma. Preserve the induction
  on derivation height and the check that each premise formula is copied from
  the conclusion or is an immediate subformula of the principal formula.
- **Source sketches only:** LK soundness, propositional subformula corollary,
  empty-sequent result, ND normalization, STLC subject reduction, and STLC
  strong normalization. Each remains `sketched` if annexed.
- **No annex items:** Craig, Beth, or Gentzen's PA analysis, because each is a
  cited import in v1.1.
- **New sketch:** Church--Rosser via parallel reduction. This is a new-content
  annex sketch and does not change any migrated source status.

## Research package 7.1: calculus identities, completeness, and ND

### Canonical and defined-negation LK

Use three names consistently:

- `LK` / `sheet:lk`: the canonical Parts II/III calculus with finite-multiset
  two-sided sequents, contexted initial sequents, primitive negation rules,
  equality excluded;
- `LK=` / `sheet:lk-eq`: the distinct equality extension;
- `LK_d` / `sheet:lk-defneg`: the Part-VIII calculus with uncontexted identity,
  `bottom L`, defined negation `neg A := A -> bottom`, context-splitting
  implication-left, and equality excluded.

The safe derivability-equivalence theorem is translation-sensitive. Define
`d` recursively by replacing each primitive `neg A` in a canonical formula by
`d(A) -> bottom` and commuting with every other connective and quantifier.
For finite contexts, apply `d` memberwise. The target statement may say:

> For every equality-free finite sequent `Gamma => Delta`, canonical LK
> derives it iff `LK_d` derives `d(Gamma) => d(Delta)`.

A complete proof must supply: contexted identity from uncontexted identity by
weakening; the converse identity instance; admissibility/derivability of the
translated primitive-negation rules; both directions between shared-context
and split-context implication-left using weakening and contraction; and all
quantifier/eigenvariable cases. If any case is only described, label the
theorem `sketched`, not `proved`. The theorem compares existence of
derivations, not proof identity, height, size, or cut-freeness.

### LK completeness entry (`D-P8-001`)

Do not invent a stronger proof. Reuse the exact established forms:

- propositional: for finite multisets `Gamma,Delta`, canonical propositional
  LK derives `Gamma=>Delta` iff every valuation that satisfies all formulas in
  `supp(Gamma)` satisfies some formula in `supp(Delta)`, including empty
  contexts; current status `sketched=annex:p2.3.8`;
- first-order: **assuming the Axiom of Choice**, for finite multisets
  `Gamma,Delta`, canonical cut-admitting equality-free LK derives the sequent
  iff every structure and assignment satisfying the antecedent satisfies some
  succedent formula; current status `sketched=annex:p2.2.14`.

The P7 E entry should explain the reduction of an arbitrary finite sequent to
single-conclusion consequence, then point to the existing theorem and Part-7
cut elimination. It must explicitly say that completeness as presently
supported uses Cut and that the P7 sketch does not establish cut-free
completeness for canonical LK.

### LK--ND equivalence (`D-P8-002`)

Fix a classical natural-deduction calculus and language first. For a finite
multiset `Delta`, define
`bigvee(empty)=bottom` and let `bigvee(Delta)` be a fixed associated finite
disjunction after forgetting multiplicity; similarly, assumptions use the
support of `Gamma`. A safe equality-free statement is:

> For every finite equality-free sequent `Gamma=>Delta`, canonical LK derives
> the sequent iff classical ND derives `bigvee(Delta)` from `supp(Gamma)`.

If primitive negation differs between the systems, compose with the formula
translation above. If equality is included, state a separate theorem for
`sheet:lk-eq` and the exact ND equality rules; do not let the equality version
inherit R-012 cut elimination. A full annex proof needs every structural,
logical, quantifier, discharge, alpha-conversion, and eigenvariable case in
both translations. Otherwise use `cited=Gentzen1934a` or an honest sketch.
The current P2 theorem `thm:p02-calculi-derivability-equivalence` is already a
cited single-conclusion result and is a safe source to cross-reference.

Primary/authoritative locators: Gentzen's two original investigations,
[Part I](https://doi.org/10.1007/BF01201353) and
[Part II](https://doi.org/10.1007/BF01201363); Troelstra--Schwichtenberg,
[Basic Proof Theory](https://doi.org/10.1017/CBO9781139168717);
Negri--von Plato,
[Structural Proof Theory](https://doi.org/10.1017/CBO9780511527340).

## Research package 7.2: Mix, cut elimination, Herbrand, and Maehara

### Exact Mix homing and R-012

The registry must contain these two rule surfaces, each with all five
`\hbrule` arguments and its exact side condition:

- on `sheet:lk-defneg`, from
  `Gamma => Delta,A^m` and `A^n,Pi => Sigma` infer
  `Gamma,Pi => Delta,Sigma`, where `m,n>=1`, `A^k` means exactly `k`
  comma-separated occurrences, and `Delta,Sigma` may contain other
  occurrences of `A`;
- on `sheet:lj`, from `Gamma=>A` and `A^n,Pi=>C` infer
  `Gamma,Pi=>C`, where `n>=1`. There is no left-premise succedent
  multiplicity in single-succedent LJ.

The displayed occurrences are the **mix formula**. For an instance with
immediate subderivations `D_1,D_2`, use rank `r(A)` and height
`h(D_1)+h(D_2)`, ordered lexicographically. Do not call this the measure of a
primitive Cut until the special case `m=n=1` has been stated.

The existing canonical-LK and LK-with-equality Mix rows are mathematically
derivable from contractions and Cut, but their file comments currently say
that the Part-VIII cut-elimination reduction uses them. Correct that
provenance claim. On `sheet:lk-eq`, add an explicit sentence that equipollence
does not establish admissibility of Cut for the equality extension. Also
record that the symmetric equality-replacement derivation uses Cut, as R-042
requires.

### Cut-elimination method entry

The body method has the following exact input/output:

> Given a finite derivation in `LK_d` (respectively LJ), first read each Cut
> as Mix with multiplicities one. Repeatedly replace an uppermost Mix of
> maximal formula rank by the calculus-specific commuting or principal
> reductions. The output is a derivation in the same calculus, of the same
> endsequent, containing no Mix and hence no Cut.

The source sketch supplies six load-bearing families: commute a nonprincipal
Mix upward; delete weakening and initial cases; absorb contractions by raising
the relevant multiplicity; replace a principal/principal instance by lower
rank instances plus lower-height residual instances; alpha-rename
eigenvariables and invoke capture-avoiding substitution; iterate by the
well-founded lexicographic measure. The omitted complete table is not
cosmetic: it is the difference between a sketch and a proof.

"Analytic derivation" is safe only after qualification. For propositional
`LK_d`/LJ it may mean a cut-free derivation having the literal subformula
property. For first-order derivations, use "subformula modulo term
substitution and eigenvariable renaming." Do not define analytic as merely
"cut-free" for arbitrary calculi.

### Midsequent and Herbrand route (`D-P8-003`, `N-a-069`)

Use a fixed equality-free, finitary, cut-free first-order LK and regularize
eigenvariables first. A claim-safe midsequent statement is:

> If a prenex endsequent has a cut-free derivation, the derivation can be
> permuted so that no propositional logical inference occurs below a
> quantifier inference (tree roots are at the bottom). A quantifier-free
> sequent separates the propositional upper part from the quantifier lower
> part.

The exact theorem depends on the chosen structural-rule and quantifier-rule
presentation; it must therefore name the sheet. Equality, induction, and Cut
are excluded. If contraction permutations or regularity are not proved
locally, status is `cited=Takeuti1987` or `sketched`, not `proved`.

For a valid equality-free prenex existential sentence
`exists x_1...exists x_k A(x_1,...,x_k)` with quantifier-free matrix and a
signature containing a ground term (or after adding one fresh constant), the
midsequent exposes finitely many ground tuples `t_i^j`; the upper
propositional proof yields the valid Herbrand disjunction
`A(t_1^1,...,t_k^1) or ... or A(t_1^n,...,t_k^n)`. This is the proof-theoretic
route to the already existing P2 theorem `thm:p02-herbrand-validity`. It does
not replace:

- P2's equality-free validity form, which is already citation-only;
- P2's finite-clause unsatisfiability form;
- the epsilon-calculus extended-first-theorem route below; or
- a Herbrand theorem with equality, which needs equality instances or an
  equality calculus.

Because the local cut-elimination theorem is only sketched, a local derivation
"by cut elimination" inherits that limitation. A citation to a complete
external midsequent theorem is the clean S-level status.

### Maehara's partition lemma (`D-P8-004`, `N-a-070`)

Fix an equality-free cut-free first-order sequent calculus and a derivation of
`Gamma_1,Gamma_2 => Delta_1,Delta_2`. A safe sentence-level partition lemma
says there is a sentence `C` such that

1. `Gamma_1 => Delta_1,C` is derivable;
2. `C,Gamma_2 => Delta_2` is derivable; and
3. every nonlogical predicate, function, and constant symbol of `C` occurs on
   both sides of the partition, namely in a formula of
   `Gamma_1 union Delta_1` and in a formula of
   `Gamma_2 union Delta_2`.

Equality and `bottom` may be treated as logical only if that convention is
declared. For formulas with free variables, the theorem needs the
corresponding common-free-variable clause; the sentence form avoids that
extra surface.

A complete Maehara annex induction must include initial and `bottom` cases,
weakening/contraction, every propositional left/right case for every placement
of the principal formula in the partition, and all four quantifier cases.
Eigenvariables absent from the common language must be quantified away while
preserving both derivations. Equality rules are not silently covered. A table
that says "other cases are similar" is a sketch.

Applying the partition lemma to a cut-free derivation of `phi=>psi` with
partition `(phi; empty)` on the left and `(empty; psi)` on the right yields an
interpolant. But obtaining that cut-free derivation invokes cut elimination,
and deriving the sequent from semantic entailment invokes the exact
completeness theorem. Thus:

- the conditional Maehara lemma for an already supplied cut-free derivation
  can have its own local evidence;
- the migrated first-order Craig theorem remains `cited=Craig1957` (or an
  authoritative proof-theory source), because v1.1 assigned cited status;
- Beth remains `cited`, with the standard renamed-predicate construction
  explained in prose but not relabelled as a local proof.

For Beth, state the arity and theory explicitly: if a first-order theory `T`
in `L union {R}` semantically determines the `n`-ary relation `R` uniquely
over each common `L`-reduct, then an `L`-formula `theta(x_1,...,x_n)` satisfies
`T |- forall xbar (R(xbar) <-> theta(xbar))`. The standard route renames `R`
to `R'`, applies compactness/interpolation to the two copies, and then removes
the renamed symbol. It is not a one-line consequence without those steps.

Primary/authoritative locators: Craig's original
[1957 paper](https://doi.org/10.2307/2963594), the existing
`Maehara1960` record, Gentzen's
[Part II](https://doi.org/10.1007/BF01201363), Takeuti's *Proof Theory*, and
Troelstra--Schwichtenberg
[chapters on cut and interpolation](https://doi.org/10.1017/CBO9781139168717).

## Research package 7.3: normalization and Curry--Howard apparatus

### Migrated normalization claims

The exact source calculus is finite-tree intuitionistic natural deduction with
`and`, `or`, `to`, `bottom`, `forall`, and `exists`; defined negation; the
source discharge and eigenvariable conditions; and total capture-avoiding
substitution. It excludes RAA, primitive-negation rules, equality rules, and
arithmetic induction. Preserve that declaration next to the theorem.

The normalization theorem says that every derivation in that calculus reduces
to a normal derivation with the same conclusion and no new undischarged
assumption formula (modulo alpha-equivalence). The source proof is a sketch:
principal reductions remove introduction/elimination detours, permutation
conversions move eliminations over disjunction/existential eliminations, and a
lexicographic measure controls maximal-formula rank and maximal-segment
length. The omitted calculus-specific reduction and permutation cases must be
listed in any annex `\sketchnote`.

For STLC, retain the exact claims separately:

- subject reduction: if `Theta_ty |- M:A` and `M ->_beta N`, then
  `Theta_ty |- N:A`; source sketch omits the full typing-substitution and
  compatible-closure inductions;
- strong normalization: every well-typed STLC term has no infinite beta
  sequence; source sketch gives the reducibility-candidate architecture but
  omits the candidate closure lemmas.

Do not collapse normalization, confluence, subject reduction, and canonicity
into one cell or theorem. They are different predicates of different
relations and proof objects.

### A-072 and A-151: exact Curry--Howard/categorical qualifications

The table may safely use the following dictionary for intuitionistic
propositional logic, typed lambda calculus with products/sums, and a chosen
bicartesian closed category:

| logic | type theory | categorical semantics |
|---|---|---|
| formula | type | object |
| assumption context | typed context/product of types | domain object/product |
| derivation of `A` from `Gamma` | term `Gamma \vdash M:A` | morphism from the context object to `A` |
| implication | function type | exponential |
| conjunction | product type | categorical product |
| truth | unit type | terminal object |
| disjunction | sum type | categorical coproduct |
| falsity | empty type | initial object |
| proof substitution/cut | term substitution | morphism composition |
| beta/eta conversion | term equality after the declared conversions | equality of the denoted morphisms |

The categorical column is not meaningful without the stated products,
coproducts, exponentials, and quotient of syntax by the selected conversions.
The triangle's edges should therefore be labelled "Curry--Howard term
assignment," "categorical semantics," and "internal language/syntactic
category," not simply "equals." Category theory is Phase 5; a Phase-4 figure
uses a citation/prose forward pointer rather than a dangling label.

### A-152: worked derivation pair

Use the source's composition term, because it has a complete small derivation
and no new mathematical claim:

`lambda f:(B->C). lambda g:(A->B). lambda x:A. f (g x)`

of type `(B->C)->(A->B)->A->C`. The typing tree first derives `g x:B` from
the variable instances `g:A->B` and `x:A`, then derives `f(g x):C` from
`f:B->C`, and finally applies implication introduction three times. The ND
tree uses the same three open assumptions and discharges `x`, then `g`, then
`f`. This is a worked instance, not a redisplay of generic rules. Every rule
name points to the actual typing/ND registry sheet.

### A-070: structural-rules table

Every row must name an exact calculus; "relevance logic" and "linear logic"
alone do not determine a rule inventory. The safe initial data are:

- canonical LK: exchange built into finite multisets; left/right weakening
  and contraction primitive; Cut primitive and admissibility **not yet
  established by the Part-VIII sketch for this presentation**;
- LJ: exchange built into the antecedent multiset; left weakening and
  contraction primitive; no right structural rules because the succedent is
  exactly one formula; Cut primitive and source-sketch admissible;
- IMLL with multiset contexts: exchange built in; no weakening or
  contraction; Cut primitive or metarule according to its sheet, with cited
  admissibility only;
- affine linear calculus: weakening allowed, contraction absent; exchange
  depends on whether the selected affine calculus is commutative;
- Lambek calculus: ordered contexts, so exchange, weakening, and contraction
  are absent in the basic calculus; variants must be named separately;
- relevance row: do not fill until one concrete sequent sheet is selected.
  Different relevance calculi treat contraction and mingle differently.

The "Cut" column needs at least two fields or compound values: **displayed
primitive/absent** and **admissibility evidence**. "Yes" conflates them.

### A-071: calculi catalog

At the start of this visit the real sheets are `sheet:lk`, `sheet:lk-eq`,
`sheet:lk-defneg`, `sheet:lj`, `sheet:nd-cpl`, and `sheet:nd-fol`; there are no
separately named NK/NJ sheets and no hypersequent/display/deep-inference
sheets. Therefore the catalog must do one of two honest things:

1. add exact registry sheets for the intended NK/NJ and worked generalized
   calculi, then cite their adequacy results; or
2. label those rows "citation-only survey; no active handbook sheet."

It may not call an intuitionistic subset of a classical ND sheet "NJ" without
defining that subcalculus. Adequacy cells must separate soundness,
completeness, cut admissibility, normalization, and decision procedures.

Authoritative locators: Prawitz, *Natural Deduction* (`Prawitz1965`);
Troelstra--Schwichtenberg
[Basic Proof Theory](https://doi.org/10.1017/CBO9781139168717);
Negri--von Plato
[Structural Proof Theory](https://doi.org/10.1017/CBO9780511527340); and
Girard--Lafont--Taylor's author-hosted
[Proofs and Types](https://www.paultaylor.eu/stable/prot.pdf).

## Research package 7.4: untyped lambda calculus, System F, and MLTT

### Untyped lambda calculus (`D-P9-003`, `N-a-015`)

Fix a countably infinite set of variables. Terms are
`M,N ::= x | M N | lambda x.M`, taken modulo alpha-equivalence only after
free variables and capture-avoiding substitution have been defined. One-step
beta reduction is the compatible closure of

`(lambda x.M) N ->_beta M[N/x]`.

Write `->_beta*` for reflexive-transitive closure and `=_beta` for the
reflexive-symmetric-transitive compatible closure. Do not use `equiv` for
alpha or beta equality: the project reserves that glyph for elementary
equivalence of structures.

The exact Church--Rosser/confluence statement is:

> If `M ->_beta* N_1` and `M ->_beta* N_2`, then there is a term `P` with
> `N_1 ->_beta* P` and `N_2 ->_beta* P`.

It does **not** say every term has a normal form or that beta reduction is
strongly normalizing. The immediate corollary is uniqueness up to
alpha-equivalence: if a term reduces to two beta-normal forms, those normal
forms are alpha-equivalent.

For the requested Tait--Martin-Loef method, define parallel reduction with
simultaneous congruence clauses and a beta clause

`M parallel M', N parallel N'` implies
`(lambda x.M)N parallel M'[N'/x]`.

The standard proof establishes a parallel-substitution lemma, defines the
complete development `M*`, proves `M parallel N` implies `N parallel M*`,
obtains the diamond property for parallel reduction, and identifies its
reflexive-transitive closure with beta reduction. An annex that does not prove
all those clauses is correctly
`sketched=annex:...`; its `\sketchnote` must list them.

Primary evidence: Church--Rosser's original
[Some Properties of Conversion](https://doi.org/10.1090/S0002-9947-1936-1501858-0)
(the existing key's JSTOR DOI points to the same article); the original
[AMS scan](https://www.ams.org/tran/1936-039-03/S0002-9947-1936-1501858-0/S0002-9947-1936-1501858-0.pdf);
and the complete modern parallel-reduction development in
Girard--Lafont--Taylor's
[Proofs and Types](https://www.paultaylor.eu/stable/prot.pdf). Frank Pfenning's
author-hosted [1992 account](https://www.cs.cmu.edu/~fp/papers/cr92.pdf) is a
useful verification source for the Tait/Martin-Loef proof shape.

### Lambda definability and combinators (`N-a-015`)

Fix Church numerals and a definition before stating equivalence. One safe
definition calls a partial function `f:N^k partialto N` lambda-definable if a
closed term `F` has beta-normal form the Church numeral for `m` on the encoded
input exactly when `f(n_1,...,n_k)=m`; on an undefined input it has no numeral
normal form. Confluence makes the output unique. Then cite, do not locally
reprove, the theorem that the lambda-definable partial numerical functions are
exactly the partial recursive functions.

The historical evidence must keep three roles apart: Church 1936 gives the
lambda-definability framework and undecidability application; Kleene 1936
relates the general recursive formalisms; Church--Rosser supplies conversion
confluence. Use `Church1936`, `Kleene1936`, and `ChurchRosser1936`, not one
catch-all attribution. Stable locators are Church's
[AJM paper](https://doi.org/10.2307/2371045) and Kleene's
[Mathematische Annalen paper](https://doi.org/10.1007/BF01565439).

For the table-level combinatory comparison, define the fixed basis
`K x y -> x` and `S x y z -> x z (y z)`, give bracket abstraction as the
translation that removes one free variable, and cite Curry--Feys for
combinatory completeness/equivalence. Do not call individual lambda terms
literally identical to their combinatory translations.

### System F (`D-P9-004`, `N-c-029`)

Use Church-style syntax for the main entry:

- types `A,B ::= alpha | A -> B | forall alpha.A`;
- terms `M,N ::= x | lambda x:A.M | M N | Lambda alpha.M | M[A]`;
- judgments `Delta;Gamma |- M:A`, with a type-variable context `Delta` and a
  term-variable context `Gamma` whose assigned types are well formed over
  `Delta`.

Type abstraction introduces `forall alpha.A` only when `alpha` is fresh for
the types of the undischarged term context; type application substitutes a
well-formed type capture-avoidably. Generic rule displays belong on a registry
sheet, not in the body.

Claim-safe metatheorems:

- every well-typed Church-style System-F term is strongly beta-normalizing
  (`cited=Girard1972` or `GirardLafontTaylor1989`);
- the system is confluent on terms, but confluence and strong normalization
  are separate claims;
- System F is the proof-term calculus for second-order intuitionistic
  propositional logic under the fixed term assignment;
- impredicative encodings such as
  `Bool := forall alpha. alpha -> alpha -> alpha` and
  `Nat := forall alpha.(alpha->alpha)->alpha->alpha` are examples, not a claim
  that every datatype has every desired extensional law internally;
- Reynolds parametricity is pointer/citation level unless the relational
  interpretation and abstraction theorem are supplied.

Decision boundary for A-073: explicitly annotated Church-style checking is
decidable by syntax-directed verification plus type equality. In the
Curry-style assignment system, where terms omit those type abstractions and
annotations, Wells proves that typability and type checking are equivalent and
undecidable. Cite Wells's exact presentation; never put "System F type
checking: undecidable" without the style qualifier.

Primary/authoritative evidence: Girard's `Girard1972`; Reynolds's
[1974 paper](https://doi.org/10.1007/3-540-06859-7_148) and `Reynolds1983`;
Girard--Lafont--Taylor
[chapters 11, 14, and 15](https://www.paultaylor.eu/stable/prot.pdf); and
Wells,
[Typability and Type Checking in System F Are Equivalent and Undecidable](https://doi.org/10.1016/S0168-0072(98)00047-5).

### Intensional Martin-Loef type theory (`N-c-030`)

Name one object theory rather than treating "MLTT" as a unique calculus. The
minimum S entry fixes contexts and at least these judgments:

- `Gamma ctx`;
- `Gamma |- A type`;
- `Gamma |- a:A`;
- `Gamma |- A = B type`;
- `Gamma |- a = b:A`.

Define dependent product `Pi(x:A).B(x)`, dependent sum
`Sigma(x:A).B(x)`, intensional identity type `Id_A(a,b)`, and an explicitly
stratified universe hierarchy (or one precisely cited Russell universe).
State formation/introduction/elimination/computation only by reference to a
real registry sheet. "Propositions as types" means a proposition is
represented by a type and a proof by an inhabitant under the chosen
interpretation. It does not imply proof irrelevance: intensional type theory
can distinguish inhabitants and identity proofs unless a separate principle
is assumed.

Safe status boundary:

- cite Martin-Loef 1984 for the selected judgmental presentation;
- cite a normalization theorem only after matching its exact universe,
  eta/equality, and type-former surface;
- cite Abel--Coquand--Dybjer for decidability of typed beta-eta equality in
  their specified theory with a Russell universe, and infer correctness of
  type checking only for the matched syntax;
- keep extensional equality, equality reflection, general recursion, quotient
  types, univalence, higher inductive types, and cubical computation outside
  the claim.

The source is Martin-Loef's archived
[Intuitionistic Type Theory](https://archive-pml.github.io/martin-lof/pdfs/Bibliopolis-Book-retypeset-1984.pdf).
The exact modern decision source is Abel, Coquand, and Dybjer,
[Normalization by Evaluation for Martin-Loef Type Theory with Typed Equality Judgements](https://doi.org/10.1109/LICS.2007.33),
pp. 3--12. CIC should appear as a separately named pointer: its inductive
families, cumulative universes, and metatheory are not established by the MLTT
paragraph. HoTT/univalence and cubical internals remain only the excluded
`N-x-001`/`N-x-002` pointer.

### A-073 comparison cells

| system | confluence | normalization | checking / typability |
|---|---|---|---|
| untyped lambda calculus | beta reduction confluent | not weakly or strongly normalizing for all terms | no intrinsic typing problem |
| STLC, explicitly typed | confluent | every well-typed term strongly normalizing | checking decidable; simple typability/inference must cite its selected presentation |
| System F, Church style | confluent | every well-typed term strongly normalizing | explicit checking decidable |
| System F, Curry style | confluent on underlying beta terms; typing is separate | every typable term strongly normalizing | typability and type checking undecidable (Wells) |
| selected intensional MLTT | only the reduction/equality relation actually fixed | cite the matched normalization theorem | cite decidability only for the matched judgmental equality and universe surface |
| CIC | pointer only unless an exact calculus and source are added | no blanket cell | no blanket cell |

## Research package 7.5: Gentzen, PRA, and ordinal calibration

### Preserve the existing Gentzen boundary (`D-P8-005`, `N-a-049`)

The migrated cited theorem should retain v1.1's exact form: for the selected
sequent-reduction presentation of first-order arithmetic, finite derivation
codes receive notations below `epsilon_0`; each critical reduction strictly
lowers the assigned notation; in a metatheory accepting transfinite induction
for the predicates and primitive-recursive order used in that analysis,
termination yields the selected arithmetized `Con(PA)`. This is
`cited=Gentzen1936`/`Gentzen1938` or the exact modern presentation, not a local
annex proof.

Keep six objects separate in the lookup entry:

1. the exact arithmetic sequent calculus and its induction rules;
2. primitive-recursive finite derivation codes;
3. a finite grammar of ordinal-notation codes below `epsilon_0`, with
   comparison and fundamental sequences;
4. a primitive-recursive reduction on derivation codes;
5. an assignment from derivations to notation codes and the case-by-case
   decrease lemma; and
6. the exact transfinite-induction schema and final extraction of the absence
   of an empty-sequent derivation.

`N-a-049` additionally says "ordinal assignment in full for the propositional
core." To count that row as filled, choose one published presentation (the
source already names Troelstra--Schwichtenberg, chapter 10, pp. 318--337),
state its propositional derivation grammar, and reproduce the complete
assignment table for initial, structural, propositional logical, repetition,
and cut/reduction nodes that actually occur. Then check every
principal/principal and permutation reduction in that core. A table of
ordinal names without the assignment clauses is partial and the row must stay
open. This local core does not upgrade the full PA result.

The original sources are Gentzen's
[1936 consistency paper](https://doi.org/10.1007/BF01565428) and the existing
`Gentzen1938`. The modern exact locator already used by v1.1 is
Troelstra--Schwichtenberg,
[Basic Proof Theory](https://doi.org/10.1017/CBO9781139168717), chapter 10,
especially sections 10.1--10.4. Takeuti (`Takeuti1987`) and Schuette
(`Schuette1977`, proposed below) are authoritative comparisons, not automatic
substitutes for the selected rule surface.

### Proof-theoretic ordinal: safe definition (`D-P8-006`)

Do not introduce a bare `|T|`. A safe first-order calibration fixes a
recursive notation relation `prec`, a formula class `C`, and a base coding,
then defines in prose or with a new registered macro

`pto_C(T) := sup { otp(prec) : prec is a recursive well-order and T proves
the C-transfinite-induction scheme along prec }`.

The order-type expression is used only after well-foundedness is established.
For second-order theories, a common alternative is the supremum of recursive
well-orders whose well-foundedness the theory proves; that is a separately
named calibration. In either form, report the formula class, coding/base, and
whether the result concerns consistency, reflection, induction, or provably
total functions. Different calibrations need not give an unqualified
canonical invariant.

### Veblen hierarchy and `Gamma_0` (`N-a-050`)

P6 ordinal addition/exponentiation must be available first. Define a normal
ordinal function as strictly increasing and continuous at nonzero limits. The
standard binary Veblen hierarchy is fixed by

- `phi_0(beta)=omega^beta`; and
- for `alpha>0`, `phi_alpha` enumerates in increasing order the common fixed
  points of all `phi_gamma` with `gamma<alpha`.

Then `Gamma_0` is the least positive ordinal `gamma` with
`phi_gamma(0)=gamma`; equivalently it is the least positive ordinal closed
under the relevant Veblen formation below itself. Specify whether the table
shows actual ordinals or finite notation terms.

The safe historical/mathematical statement is that, in the autonomous
progression analyses of Feferman and Schuette, `Gamma_0` is the bounding
ordinal reached by that formalization of predicative analysis. Do not write
"predicative mathematics is exactly everything below Gamma_0" as an
unqualified philosophical theorem. Sources: Veblen's original
[1908 paper](https://doi.org/10.1090/S0002-9947-1908-1500814-9), Feferman's
[Systems of Predicative Analysis](https://doi.org/10.2307/2269764), and
Schuette's [Proof Theory](https://doi.org/10.1007/978-3-642-66473-1).

### Local calibration table

The following are claim-safe only under the standard induction/provable-
well-order calibrations named in the row; print the calibration column.

| theory/presentation | calibrated ordinal | qualification/status |
|---|---|---|
| modern PRA with all primitive-recursive function symbols and quantifier-free induction | `omega^omega` | conventional first-order proof-theoretic calibration; cited, not a definition of finitism |
| `I Sigma_n`, fixed `n>=1` | `omega_{n+1}`, where `omega_0=1` and `omega_{k+1}=omega^(omega_k)` | standard fragment calibration; presentation and formula class must be cited |
| PA | `epsilon_0 = sup_n omega_n` | Gentzen-style consistency/induction calibration, cited and relative as above |
| HA | `epsilon_0` | standard ordinal-analysis comparison; does not identify PA and HA proofs or logics |
| `ACA_0` | `epsilon_0` | second-order calibration under its standard recursive-well-order convention; cite separately |
| `ATR_0` / the named predicative analysis | `Gamma_0` | cite the exact second-order/autonomous-progression result; do not call it absolute predicativity |

Do not add Q, EFA, ZF, ZFC, or large-cardinal rows without a source and the
same calibration data. A-074's phrase "Q-range fragments" is a Phase-6
research obligation, not permission to guess a number for Q. The local P7
table can satisfy `D-P8-006` while A-074 stays open.

### PRA and finitism (`N-a-051`)

Choose a modern PRA presentation and state it. A standard one has one function
symbol for every primitive-recursive function, the corresponding defining
equations, equality logic, and quantifier-free induction (or its explicitly
equivalent free-variable rule). Say which formulation is used. This is a
formal theory, whereas "finitism" is a methodological/philosophical class of
reasoning.

Skolem's 1923 work is a historical precursor developing arithmetic by the
recursive mode of thought; do not cite the unrelated current `Skolem1934`
noncategoricity paper for this claim. Tait 1981 argues that the finitistically
acceptable numerical functions/arguments are captured by primitive-recursive
methods. Present that as Tait's analysis, with its stated rationale, not as a
proved identity accepted by every account of finitism.

Verified metadata: Skolem, *Begruendung der elementaren Arithmetik durch die
rekurrierende Denkweise ohne Anwendung scheinbarer Veraenderlichen mit
unendlichem Ausdehnungsbereich*, *Skrifter utgit av Videnskapsselskapet i
Kristiania, I. Matematisk-naturvidenskabelig klasse*, no. 6, pp. 1--38, 1923;
and W. W. Tait, "Finitism," *Journal of Philosophy* 78(9), 524--546, 1981,
[doi:10.2307/2026089](https://doi.org/10.2307/2026089).

`N-a-052` is could-priority. Insert an explicit row-ID stub for the omega-rule,
omega-logic cut elimination, and its `epsilon_0` calibration. Do not splice an
infinitary rule into the finitary cut theorem or claim its admissibility there.

## Research package 7.6: functional interpretations and constructive properties

### System T and Dialectica (`N-a-053`)

Fix finite types `sigma,tau ::= 0 | sigma -> tau`. Goedel's System T is STLC
over those types with natural-number constant `0:0`, a successor
`S:0->0`, and at every finite type `sigma` a primitive recursor with the
typed equations

- `R_sigma a b 0 -> a`;
- `R_sigma a b (S n) -> b n (R_sigma a b n)`.

The precise argument order may differ by source, so the registry sheet and
the equations must use one convention consistently. Generic typing and
reduction rules live on that sheet. System T is strongly normalizing, but the
P7 row only needs the exact cited fact required for the interpretation; do
not infer consistency from the phrase "typed terms" alone.

For a fixed Dialectica translation, associate to each arithmetic formula `A`
a formula of the form

`A^D := exists x forall y A_D(x,y)`

where the realizing and challenge variables have finite types and the matrix
is quantifier-free in the target theory. This display is a definition, so use
the registered definitional sign, not `equiv`. At minimum the entry must give
the atomic clause and the clauses for conjunction, implication, and both
quantifiers. In a standard formulation, if
`A^D=exists x forall y A_D(x,y)` and
`B^D=exists u forall v B_D(u,v)`, implication has functionals `U,Y` with
matrix

`A_D(x,Y(x,v)) -> B_D(U(x),v)`.

Disjunction needs an explicit boolean/tagging convention; it cannot be
silently treated as conjunction. Bound-variable types and capture-avoiding
substitution must be visible.

The safe soundness statement, after matching the exact version in
Avigad--Feferman, is citation-level:

> From an HA proof of a closed formula `A`, one effectively extracts closed
> System-T terms `t` such that the target quantifier-free finite-type theory
> proves `forall y A_D(t,y)`.

State the target theory, equality, extensionality, and induction surface used
by the cited version. For `bottom`, the translation is again bottom, so the
interpretation gives the corresponding relative consistency corollary. This
is not an internal HA proof of `Con(HA)` and not a blanket interpretation of
analysis.

Primary/authoritative sources: Goedel,
[Ueber eine bisher noch nicht benuetzte Erweiterung des finiten Standpunktes](https://doi.org/10.1111/j.1746-8361.1958.tb01464.x),
*Dialectica* 12, 280--287 (1958); Troelstra,
[Metamathematical Investigation of Intuitionistic Arithmetic and Analysis](https://doi.org/10.1007/BFb0066739),
LNM 344, especially the functional-interpretation part; and
Avigad--Feferman's author-hosted
[Goedel's Functional (Dialectica) Interpretation](https://math.stanford.edu/~feferman/papers/dialectica.pdf),
pp. 337--405, DOI 10.1016/S0049-237X(98)80020-7.

### Kleene number realizability (`N-a-054`)

Fix a primitive-recursive pairing function with projections and an acceptable
numbering `e -> {e}` of partial recursive unary functions. Register a new
realizability macro; do not reuse `\forces`, because that macro already means
set-theoretic and Kripke forcing.

For closed HA formulas, the standard clauses are:

- `e realizes P` for atomic `P` iff `P` is true in the standard natural
  numbers (the realizer is computationally irrelevant);
- `e realizes A and B` iff the two projections of `e` realize `A` and `B`;
- `e realizes A or B` iff its tag chooses a disjunct and its payload realizes
  that disjunct;
- `e realizes A -> B` iff for every `a` realizing `A`, `{e}(a)` is defined
  and realizes `B`;
- `e realizes forall x A(x)` iff for every natural number `n`, `{e}(n)` is
  defined and realizes `A(n)`;
- `e realizes exists x A(x)` iff the first projection is a witness and the
  second realizes the corresponding instance;
- no number realizes `bottom`; negation is implication to `bottom`.

Every tuple coding and definedness sign must be defined. For formulas with
parameters, state the uniform parameter version rather than pretending the
closed clauses already cover it.

Kleene soundness is citation-level unless the full induction over every HA
rule and arithmetic axiom is supplied:

> There is an effective transformation that, from an HA derivation of a
> closed `A`, produces a natural number realizing `A`.

The original source is Kleene,
[On the Interpretation of Intuitionistic Number Theory](https://doi.org/10.2307/2269016),
JSL 10(4), 109--124 (1945). Troelstra's handbook chapter (`Troelstra1998`) and
author-hosted
[formal-realizability account](https://ir.cwi.nl/pub/13500/13500D.pdf) give
the exact formalized variants.

For ECT, name the scheme. A standard `ECT_0` form says that under an
almost-negative antecedent `A(x)`, a total-existence assertion
`forall x(A(x)->exists y B(x,y))` yields an index uniformly computing such a
`y`, expressed with Kleene's `T` predicate and output function. The syntactic
restriction on `A` and the coding must be printed. Formal number realizability
is characterized over HA by the corresponding `HA+ECT_0` theory in the
selected formulation; this is stronger and more precise than "realizability
proves Church's thesis."

Markov's principle for a decidable arithmetic predicate is

`forall x(A(x) or not A(x)) -> (not not exists x A(x) -> exists x A(x))`.

HA does not prove the full scheme, but ordinary number realizability validates
it under classical metareasoning. Therefore:

- do not use this realizability relation as a countermodel to MP;
- if the row includes an MP independence application, cite the exact
  modified-realizability or Kripke/model construction that refutes MP while
  validating the intended base;
- distinguish metatheoretic realizability, formalized realizability in HA,
  consistency, and derivability.

Van Oosten's [historical survey](https://doi.org/10.1017/S0960129502003626)
and `TroelstraVanDalen1988` are safe secondary boundaries. Realizability topoi
remain explicitly outside `N-a-054`.

### Disjunction and numerical existence (`N-a-055`)

State three results separately and require closed conclusions:

1. IPC disjunction property: if `IPL |- A or B`, then `IPL |- A` or
   `IPL |- B`.
2. HA disjunction property: for closed arithmetic sentences `A,B`, if
   `HA |- A or B`, then `HA |- A` or `HA |- B`.
3. HA numerical existence property: if `A(x)` has no free variables other
   than the displayed number variable and `HA |- exists x A(x)`, then for
   some natural `n`, `HA |- A(numeral(n))`.

These are metatheorems about existence of derivations, not object-language
disjunction/existence elimination rules. For IPC, the last-rule argument is
valid after a complete cut-elimination/normal-form theorem: a closed cut-free
LJ proof ending in a disjunction must end in one of the two disjunction-right
rules. With only the local cut-elimination sketch, that argument is itself a
sketch or citation.

For HA, v1.1's normalization theorem cannot be the premise because its exact
calculus contains neither equality nor induction. A complete annex proof must
fix an HA proof system and prove its normalization/cut elimination and
canonical-form/extraction lemma. Otherwise use a cited status from
`TroelstraVanDalen1988` or another exact source. A basic number realizer of a
disjunct does not by itself give an HA derivation of that disjunct, so the
six-line realizability-clause inspection is not a complete proof of HA's
property.

`Godel1932` is useful historical context for intuitionistic propositional
logic, but it does not replace the exact modern proof of all three properties.
`Gentzen1934a`/`Gentzen1935b`, Kleene 1945, and
Troelstra--van Dalen should be attributed to the particular route they
actually support.

`N-a-058` remains P/could. Use an explicit row-ID stub or a single cited
pointer to Kohlenbach's proof-mining program; do not state a general
bound-extraction theorem without its theory, formula class, and majorizability
hypotheses. Authoritative locator:
[Applied Proof Theory](https://doi.org/10.1007/978-3-540-77533-1).

## Research package 7.7: epsilon and generalized sequent frameworks

### Epsilon calculus (`N-a-056`)

Fix the equality-free classical calculus first. If `A(x)` is a formula, the
epsilon term `epsilon x A(x)` is a term, and the characteristic/critical axiom
has the form

`A(t) -> A(epsilon x A(x))`.

Bound-variable renaming and capture-avoiding term substitution apply. Explain
whether quantifiers remain primitive or are translated by epsilon terms; do
not mix two presentations mid-theorem.

For an epsilon calculus `PC_epsilon` over an elementary free-variable
calculus `EC`, safe cited statements are:

- **first epsilon theorem:** if epsilon-free, quantifier-free `C` is derivable
  in `PC_epsilon` from epsilon-free, quantifier-free premises `T`, then `C` is
  derivable from `T` already in `EC`;
- **extended first epsilon theorem:** if an equality-free existential formula
  `exists xbar A(xbar)` with quantifier-free matrix is derivable, there are
  finitely many term tuples whose matrix instances form a propositionally
  derivable Herbrand disjunction;
- **second epsilon theorem:** if an epsilon-free first-order formula `C` is
  derivable in `PC_epsilon` from epsilon-free first-order premises `T`, then
  `C` is derivable from `T` in ordinary predicate calculus.

These are cited statements at S ceiling. Equality requires a different and
more involved theorem; do not import it from the equality-free version. The
extended first theorem connects to P2's validity-form Herbrand theorem, but
P2 already owns the Herbrand universe/structure and clause-set forms.

Sources: `HilbertBernays1939`; `Herbrand1971`; Buss's epsilon-calculus chapter
in `Buss1998`; and Moser--Zach,
[The Epsilon Calculus and Herbrand Complexity](https://doi.org/10.1007/s11225-006-6610-7),
*Studia Logica* 82(1), 133--155 (2006). The latter explicitly states the
first, extended-first, and second theorem boundaries and treats the
equality-free calculus.

### Generalized frameworks (`N-a-057`, `D-P10-031`)

Define the four framework names without treating them as one calculus:

- a **hypersequent** is a finite list or multiset of sequents, with an external
  separator and explicitly declared external structural rules;
- a **labelled sequent** contains labelled formulas such as `x:A` and
  relational atoms such as `x R y`, internalizing the selected Kripke frame
  semantics;
- a **display calculus** uses a structural language with residuation/display
  postulates so that a chosen substructure can be displayed as the whole
  antecedent or consequent of a structurally equivalent sequent;
- **deep inference** permits rule application inside an arbitrary formula or
  structure context rather than only at the outermost/root connective.

Each technical name has a distinct standing and later use; none is merely a
synonym for "nonstandard proof system."

The four worked modal examples should be sourced and sheet-owned:

1. **Hypersequent:** use the fixed GS5 calculus in Avron's treatment (or the
   exact GS5 surface reproduced in Stouppa 2007) and transcribe one complete
   derivation of an S5 principle. State whether components are sets,
   multisets, or sequences and include every external rule.
2. **Labelled:** use Negri's labelled calculus for K and derive one normal
   modal principle such as distribution only after the `xRy`, box-left, and
   box-right rules are exactly on the sheet. The frame conditions for T/S4/S5
   are separate geometric rules, not annotations.
3. **Display:** use Wansing's display calculus for a named normal modal logic
   and show one modal derivation using its structural modal operators and
   display postulates. Belnap's generic display property alone is not the
   worked K/S4/S5 example.
4. **Deep inference:** use Stouppa's KSg-S5/SKSg-S5 surface and one complete
   S5 derivation. Guglielmi's BV paper supplies the general "rules at arbitrary
   depth" definition but not this modal adequacy claim.

Every example should carry the external source's adequacy status. A worked
derivation establishes only derivability of its endformula; it does not prove
soundness, completeness, or cut admissibility of the whole framework.

Primary/authoritative sources and exact metadata:

- Avron, "The Method of Hypersequents in the Proof Theory of Propositional
  Non-Classical Logics," in *Logic: From Foundations to Applications*, Oxford
  University Press, 1996, pp. 1--32; official
  [institutional record](https://cris.tau.ac.il/en/publications/the-method-of-hypersequents-in-the-proof-theory-of-propositional-/);
- Negri, "Proof Analysis in Modal Logic," *Journal of Philosophical Logic*
  34(5--6), 507--544 (2005),
  [doi:10.1007/s10992-005-2267-3](https://doi.org/10.1007/s10992-005-2267-3);
- Belnap, "Display Logic," *Journal of Philosophical Logic* 11(4), 375--417
  (1982),
  [doi:10.1007/BF00284976](https://doi.org/10.1007/BF00284976);
- Wansing, "Sequent Calculi for Normal Modal Propositional Logics," *Journal
  of Logic and Computation* 4(2), 125--142 (1994),
  [doi:10.1093/logcom/4.2.125](https://doi.org/10.1093/logcom/4.2.125);
- Guglielmi, "A System of Interaction and Structure," *ACM Transactions on
  Computational Logic* 8(1) (2007),
  [doi:10.1145/1182613.1182614](https://doi.org/10.1145/1182613.1182614);
- Stouppa, "A Deep Inference System for the Modal Logic S5," *Studia Logica*
  85(2), 199--214 (2007),
  [doi:10.1007/s11225-007-9028-y](https://doi.org/10.1007/s11225-007-9028-y),
  with an [author-hosted PDF](https://home.inf.unibe.ch/ltg/publications/2007/sto07.pdf).

`D-P10-031` is still a P/could row and the handover orders an explicit
row-ID stub. The substantive S survey is owed independently by `N-a-057`; do
not use it to falsify the could-row instruction. `N-x-012` permits only a
proof-net pointer, and `N-x-011` only a geometry-of-interaction pointer.

## Research package 7.8: propositional proof complexity

### Cook--Reckhow framework (`N-c-027`)

Fix a reasonable binary encoding of propositional formulas and let `TAUT` be
the set of classically valid propositional formulas. A **Cook--Reckhow
propositional proof system** is a polynomial-time computable surjection

`P:{0,1}* -> TAUT`.

Equivalently, one may use a polynomial-time decidable proof relation
`Prf_P(pi,A)` that is sound (`Prf_P(pi,A)` implies `A in TAUT`) and complete
(every tautology has at least one `P`-proof). The function and relation
presentations are intertranslatable after a harmless coding convention is
fixed. This definition is needed because it separates proof verification from
proof search and makes proof-length comparisons representation-aware.

Call `P` **polynomially bounded** when some polynomial `q` gives every
tautology `A` a proof `pi` with `|pi| <= q(|A|)`. The exact cited theorem is:

> A polynomially bounded Cook--Reckhow propositional proof system exists if
> and only if `NP = coNP`.

The forward direction places `TAUT` in NP; since `TAUT` is coNP-complete, this
collapses NP and coNP. Conversely, if `TAUT` is in NP, its polynomially
bounded certificates define such a proof relation. This is a cited theorem,
not a local proof-complexity lower bound.

For systems `P` and `Q`, say that `P` **p-simulates** `Q` only when there is a
polynomial-time transformation taking each `Q`-proof of `A` to a `P`-proof of
the same `A`, with polynomially bounded output length. A mere polynomial
bound comparing shortest proof lengths is a weaker, nonuniform simulation
notion. Every table cell must say which notion is meant.

Primary evidence: Cook and Reckhow,
[The Relative Efficiency of Propositional Proof Systems](https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf),
*Journal of Symbolic Logic* 44(1), 36--50 (1979),
[doi:10.2307/2273702](https://doi.org/10.2307/2273702).

### Resolution lower bound and the pigeonhole family (`N-c-027`, `A-075`)

Choose one CNF encoding before stating a bound. For the standard functional
pigeonhole principle with `n+1` pigeons and `n` holes, variables `x_{i,j}` say
that pigeon `i` occupies hole `j`; clauses require every pigeon to occupy at
least one hole and forbid two distinct pigeons from sharing a hole. If
functionality clauses forbidding one pigeon from occupying two holes are
included, name that stronger encoding separately.

The safe headline is:

> The standard pigeonhole-principle CNFs require resolution refutations of
> exponential size.

The exponent, size measure, and encoding must be taken from the cited theorem
rather than reconstructed from memory. Haken's original result is the
landmark exponential lower bound for resolution. It is not a lower bound for
Frege or extended Frege, and it does not show that every unsatisfiable CNF is
hard for resolution.

The body entry should define resolution proof size as the total symbol count
or number of clauses/lines used by the selected source and keep that choice
fixed. If the annex sketches the restriction/bottleneck argument, it must list
the omitted combinatorial counting lemma, the handling of the chosen PHP
encoding, and the conversion between the source's measure and the table's
measure. Otherwise use `cited=Haken1985` and supply no annex item.

Primary evidence: Armin Haken,
[The Intractability of Resolution](https://doi.org/10.1016/0304-3975(85)90144-6),
*Theoretical Computer Science* 39, 297--308 (1985). Beame and Pitassi's
[ECCC TR98-067](https://eccc.weizmann.ac.il/report/1998/067/) is an
author-hosted survey useful for checking the encoding and later refinements;
it does not replace Haken as the primary attribution.

### Frege and extended Frege: current safe boundary

A **Frege system** here means a fixed finite set of sound, implicationally
complete propositional axiom schemes and inference rules with polynomial-time
recognizable substitution instances. Different reasonable Frege systems are
p-equivalent under standard encoding assumptions. An **extended Frege
system** adds an extension rule introducing a fresh variable as an
abbreviation for a previously formed formula/circuit, with the freshness and
acyclic-use conditions stated on its sheet.

Safe 2026 claims:

- superpolynomial proof-size lower bounds are known for resolution and other
  restricted systems;
- no superpolynomial lower bound is known for arbitrary-depth Frege proofs;
- an extended-Frege lower bound is at least as difficult and remains open;
- the p-simulation relation between Frege and extended Frege must not be
  presented as settled by the resolution lower bound.

The current primary checkpoint is Yaroslav Alekseev,
[A Lower Bound for Polynomial Calculus with Extension Rule](https://theoryofcomputing.org/articles/v022a004/),
*Theory of Computing* 22(4), 1--29 (2026),
[doi:10.4086/toc.2026.v022a004](https://doi.org/10.4086/toc.2026.v022a004).
Its abstract explicitly identifies arbitrary-depth Frege lower bounds as a
major open problem and extended-Frege lower bounds as harder. Its algebraic
lower bound is not itself a Frege or extended-Frege lower bound.

### A-075 construction ledger

The required table should have at least these columns:

| system | proof objects / rule surface | verification | representative lower bound | simulation statement |
|---|---|---|---|---|
| resolution | clauses; one fixed binary-resolution and weakening/factoring convention | polynomial time | exponential for the named PHP encoding, cited Haken | p-simulation cells only after encodings are fixed |
| Frege | formula lines in one named finite Frege basis | polynomial time | no superpolynomial lower bound known in general | reasonable Frege systems p-equivalent |
| extended Frege | Frege plus fresh extension variables and defining equations | polynomial time | no superpolynomial lower bound known | p-simulates its underlying Frege system; converse not asserted |

Do not put polynomial calculus, cutting planes, bounded-depth Frege, or proof
nets into this three-row required table unless their rule surface and bound
measure are also defined. They may appear in a pointer sentence. The table is
S/should apparatus and does not license an uncited survey of every proof
system.

For background synthesis use Jan Krajicek,
[Proof Complexity](https://doi.org/10.1017/9781108242066), Cambridge
University Press, 2019. Historical and lower-bound claims should still cite
the primary papers above.

## Symbol intake and collision ledger

At implementation time, new P7 rows belong in
`handbook/registry/symbols-intake-p07.csv`; the visit must not edit the shared
master registry directly. The finalizer deduplicates that intake after
checking the concurrently evolving P6 registry. The live registry already
contains the following constraints:

- `\Rightarrow` is the global sequent arrow, so parallel reduction must use a
  distinct registered macro such as `\parred` or
  `\rightrightarrows_{\beta}`;
- `\equiv` is elementary equivalence only; alpha-equivalence already has
  `=_{\alpha}`, beta-convertibility needs `=_{\beta}`, and judgmental type
  equality needs a different registered sign;
- `\Leftrightarrow` is formula equivalence and `\defeq` is definitional
  abbreviation;
- vertical bars denote cardinality only, so proof/term/formula length uses a
  named operation such as `\operatorname{len}` or `\operatorname{size}`;
- `\forces` is the one forcing macro shared by set-theoretic and Kripke
  forcing; realizability therefore needs a separate macro such as
  `\realizes`;
- `\alpha,\beta` already have disjoint local rows for P6 ordinals and P7.4
  type metavariables;
- `\varepsilon_0`, `\operatorname{otp}`, `\rightharpoonup`, formula contexts,
  and the per-system turnstile are already registered and should be reused.

The minimum intake candidates, each with its exact role and scope, are:

| candidate | standing and eliminable meaning | collision control |
|---|---|---|
| `M,N,P`; `FV(M)`; `M[N/x]` | untyped lambda terms, free variables, capture-avoiding substitution in P7.4 | do not reuse formula substitution without a term scope declaration |
| `->_beta`, `->_beta*`, `=_beta` | one-step reduction, reflexive-transitive closure, beta-convertibility | never use `\equiv` |
| `\parred` | parallel beta reduction defined by the displayed inductive clauses | never use the sequent arrow |
| `Delta;Gamma \vdash M:A` | System-F typing judgment with distinct type- and term-variable contexts | context standing must be stated locally |
| `Lambda alpha.M`, `M[A]` | type abstraction and type application in Church-style System F | distinguish term-level `lambda` |
| `Pi(x:A).B`, `Sigma(x:A).B`, `Id_A(a,b)`, `U_i` | dependent product, dependent sum, intensional identity type, stratified universes in the selected MLTT | no blanket meaning outside that named calculus |
| `=_j` or another approved macro | judgmental/definitional equality in the selected type theory | distinct from `\equiv`, formula equivalence, and object equality |
| `\varphi_\alpha(\beta)`, `\Gamma_0` | Veblen hierarchy and least strongly critical ordinal under the exact local definition | distinct from formula/type metavariables by P7.5 scope |
| `\realizes` | the selected number- or function-realizability relation | distinct from forcing and semantic satisfaction |
| `\operatorname{pto}_{\mathcal C}(T)` | proof-theoretic ordinal relative to notation system and reduction class | avoids forbidden cardinality bars |
| `\operatorname{size}(\pi)` | encoded proof size under the declared measure | avoids cardinality notation |
| epsilon term `(epsilon x)A(x)` | Hilbert epsilon term former in the exact epsilon calculus | do not confuse with `\varepsilon_0` |

Do not add a symbol merely because it appears once in prose. Every intake row
must have a later entry, theorem, or apparatus use, satisfying the project's
necessity and nonredundancy rule.

## Bibliography intake ledger

Per the shared-file rule, P7 citations not already present go to
`handbook/bib/intake-p07.bib`, never directly to the shared
`handbook/bib/handbook.bib`. The finalizer deduplicates by key and prefers the
richer verified record. No bibliography file is changed by this research
visit.

### Existing keys verified in the live handbook bibliography

These keys may be reused without an intake duplicate:

- sequent and ordinal proof theory: `Gentzen1934a`, `Gentzen1935b`,
  `Gentzen1936`, `Gentzen1938`, `TroelstraSchwichtenberg2000`,
  `NegriVonPlato2001`, `Prawitz1965`, `Takeuti1987`, `Schwichtenberg1977`;
- lambda and type theory: `Church1936`, `ChurchRosser1936`, `Kleene1936`,
  `CurryFeys1958`, `Barendregt1984`, `Girard1972`, `Girard1987`,
  `GirardLafontTaylor1989`, `Reynolds1974`, `Reynolds1983`, `MartinLof1984`,
  `NordstromPeterssonSmith1990`, `Hofmann1997`;
- interpolation and constructive metatheory: `Craig1957`, `Beth1953`, `Maehara1960`,
  `Kleene1945`, `Troelstra1998`, `TroelstraVanDalen1988`;
- epsilon/realizability/reference works: `HilbertBernays1939`, `Herbrand1971`,
  `Buss1998`, `VanOosten2008`, `Godel1932`.

The existing `Skolem1934` record is not Skolem's 1923 PRA paper and must not
be cited for primitive recursive arithmetic.

### Required or strongly recommended intake records

The following metadata have been checked against publisher, author, or
institutional records. Preserve diacritics in BibTeX but keep these keys.

| key | exact record / stable locator | P7 use |
|---|---|---|
| `Wells1999` | J. B. Wells, "Typability and Type Checking in System F Are Equivalent and Undecidable," *Annals of Pure and Applied Logic* 98(1--3), 111--156 (1999), doi:10.1016/S0168-0072(98)00047-5 | Curry-style System-F typability/checking only |
| `AbelCoquandDybjer2007` | Andreas Abel, Thierry Coquand, and Peter Dybjer, "Normalization by Evaluation for Martin-L{\"o}f Type Theory with Typed Equality Judgements," *Proceedings of the 22nd IEEE Symposium on Logic in Computer Science (LICS 2007)*, 3--12, doi:10.1109/LICS.2007.33 | typed beta-eta equality for the paper's MLTT with one Russell-style universe; not blanket MLTT |
| `CoquandHuet1988` | Thierry Coquand and G{\'e}rard Huet, "The Calculus of Constructions," *Information and Computation* 76(2--3), 95--120 (1988), doi:10.1016/0890-5401(88)90005-3 | separate CoC/CIC pointer and CoC strong-normalization claim only |
| `Tait1981` | W. W. Tait, "Finitism," *Journal of Philosophy* 78(9), 524--546 (1981), doi:10.2307/2026089 | philosophical calibration of finitism, not a definition of PRA |
| `Skolem1923` | Thoralf Skolem, "Begr{\"u}ndung der elementaren Arithmetik durch die rekurrierende Denkweise ohne Anwendung scheinbarer Ver{\"a}nderlicher mit unendlichem Ausdehnungsbereich," *Skrifter utgit av Videnskapsselskapet i Kristiania, I. Matematisk-naturvidenskabelig klasse*, no. 6, 1--38 (1923) | historical PRA/recursive-arithmetic source |
| `Godel1958` | Kurt G{\"o}del, "{\"U}ber eine bisher noch nicht benutzte Erweiterung des finiten Standpunktes," *Dialectica* 12(3--4), 280--287 (1958), doi:10.1111/j.1746-8361.1958.tb01464.x | Dialectica interpretation |
| `Troelstra1973` | A. S. Troelstra, *Metamathematical Investigation of Intuitionistic Arithmetic and Analysis*, Lecture Notes in Mathematics 344, Springer (1973), doi:10.1007/BFb0066739 | realizability and HA metatheory |
| `AvigadFeferman1998` | Jeremy Avigad and Solomon Feferman, "G{\"o}del's Functional (Dialectica) Interpretation," in Samuel R. Buss (ed.), *Handbook of Proof Theory*, Studies in Logic and the Foundations of Mathematics 137, 337--405, North-Holland (1998), doi:10.1016/S0049-237X(98)80020-7 | exact Dialectica clauses and proof-theoretic consequences |
| `Veblen1908` | Oswald Veblen, "Continuous Increasing Functions of Finite and Transfinite Ordinals," *Transactions of the American Mathematical Society* 9(3), 280--292 (1908), doi:10.1090/S0002-9947-1908-1500814-9 | Veblen hierarchy |
| `Feferman1964` | Solomon Feferman, "Systems of Predicative Analysis," *Journal of Symbolic Logic* 29(1), 1--30 (1964), doi:10.2307/2269764 | autonomous/predicative progression boundary |
| `Schuette1977` | Kurt Sch{\"u}tte, *Proof Theory*, Grundlehren der mathematischen Wissenschaften 225, Springer (1977), doi:10.1007/978-3-642-66473-1 | Gamma-zero calibration with the selected notation system |
| `Pohlers2009` | Wolfram Pohlers, *Proof Theory: The First Step into Impredicativity*, Universitext, Springer (2009), doi:10.1007/978-3-540-69319-2 | modern ordinal-analysis calibration |
| `MoserZach2006` | Georg Moser and Richard Zach, "The Epsilon Calculus and Herbrand Complexity," *Studia Logica* 82(1), 133--155 (2006), doi:10.1007/s11225-006-6610-7 | exact first/second epsilon-theorem boundary |
| `Avron1996` | Arnon Avron, "The Method of Hypersequents in the Proof Theory of Propositional Non-Classical Logics," in Wilfrid Hodges, Martin Hyland, Charles Steinhorn, and John Truss (eds.), *Logic: From Foundations to Applications*, 1--32, Oxford University Press (1996) | named hypersequent calculi |
| `Negri2005` | Sara Negri, "Proof Analysis in Modal Logic," *Journal of Philosophical Logic* 34(5--6), 507--544 (2005), doi:10.1007/s10992-005-2267-3 | labelled modal calculi |
| `Belnap1982` | Nuel D. Belnap, "Display Logic," *Journal of Philosophical Logic* 11(4), 375--417 (1982), doi:10.1007/BF00284976 | display property and generic metatheory |
| `Wansing1994` | Heinrich Wansing, "Sequent Calculi for Normal Modal Propositional Logics," *Journal of Logic and Computation* 4(2), 125--142 (1994), doi:10.1093/logcom/4.2.125 | named modal display calculi |
| `Guglielmi2007` | Alessio Guglielmi, "A System of Interaction and Structure," *ACM Transactions on Computational Logic* 8(1) (2007), doi:10.1145/1182613.1182614 | deep-inference definition; not modal S5 adequacy |
| `Stouppa2007` | Phiniki Stouppa, "A Deep Inference System for the Modal Logic S5," *Studia Logica* 85(2), 199--214 (2007), doi:10.1007/s11225-007-9028-y | worked S5 deep-inference calculus |
| `Kohlenbach2008` | Ulrich Kohlenbach, *Applied Proof Theory: Proof Interpretations and Their Use in Mathematics*, Springer Monographs in Mathematics (2008), doi:10.1007/978-3-540-77533-1 | functional interpretations and extraction claims |
| `CookReckhow1979` | Stephen A. Cook and Robert A. Reckhow, "The Relative Efficiency of Propositional Proof Systems," *Journal of Symbolic Logic* 44(1), 36--50 (1979), doi:10.2307/2273702 | proof-system definition, p-simulation, NP/coNP equivalence |
| `Haken1985` | Armin Haken, "The Intractability of Resolution," *Theoretical Computer Science* 39, 297--308 (1985), doi:10.1016/0304-3975(85)90144-6 | resolution PHP lower bound |
| `BeamePitassi1998` | Paul Beame and Toniann Pitassi, "Propositional Proof Complexity: Past, Present and Future," *Bulletin of the EATCS* 65, 66--89 (1998), ECCC TR98-067, https://eccc.weizmann.ac.il/report/1998/067/ | survey/check source for encodings and lower-bound scope |
| `Krajicek2019` | Jan Kraj{\'i}{\v{c}}ek, *Proof Complexity*, Encyclopedia of Mathematics and its Applications 170, Cambridge University Press (2019), doi:10.1017/9781108242066 | authoritative synthesis and simulation terminology |
| `Alekseev2026` | Yaroslav Alekseev, "A Lower Bound for Polynomial Calculus with Extension Rule," *Theory of Computing* 22(4), 1--29 (2026), doi:10.4086/toc.2026.v022a004 | current explicit checkpoint that Frege/extended-Frege lower bounds remain open |

`Wells1999`, `AbelCoquandDybjer2007`, and `CoquandHuet1988` are the binding
new keys for the P7.4 decision/normalization cells. Do not silently substitute
`MartinLof1984` for Abel--Coquand--Dybjer's much narrower decision theorem, or
CoC for CIC.

## Source-retirement accounting

Every v1.1 Part-VIII span has one of these dispositions; there is no silent
source chapter:

- foundational sequent syntax/rules and derivability notions migrate into
  P7 body entries plus pointers to the registry sheets;
- the v1.1 soundness and completeness sketches retain sketch status and their
  exact calculus scope;
- the repaired Mix/cut material migrates as the Tier-1 method obligation,
  with R-012's principal-principal measure and substitution control intact;
- Craig and Beth migrate as cited statements; a new Maehara entry does not
  upgrade those inherited statuses;
- natural-deduction normalization and STLC normalization migrate as Tier-2
  sketches with omissions enumerated;
- Curry--Howard prose migrates into A-072/A-151/A-152 with fixed-calculus
  qualifications;
- Gentzen ordinal analysis remains cited and gains only the separately
  sourced calibration table/entry;
- the seven source exercise blocks (two after sequent basics, two after cut,
  three after ordinal analysis) are deliberately retired as exercises; any
  mathematical fact needed by an entry has been separately accounted for in
  the crosswalk above;
- bibliography and end-of-part connective prose are absorbed into A-186 and
  navigation pointers rather than printed as source-like chapters.

The retired exercises are not proof evidence. A result that appeared only as
an exercise must be proved/cited anew or omitted.

## Adversarial overclaim checklist

Before any P7 status or register row changes to done, verify all of the
following:

1. `sheet:lk-defneg` and `sheet:lj`, not canonical LK/LK-equality, are the
   systems supported by the inherited Mix/cut proof unless a new equivalence
   theorem explicitly transports the proof.
2. R-012's lexicographic measure decreases in every principal-principal case;
   no weakening/contraction/substitution step is hidden behind "similar."
3. First-order subformula/analytic claims say "modulo substitution and
   eigenvariable renaming" and repeat all eigenvariable conditions.
4. The Maehara partition lemma is stated for one exact calculus and one exact
   partition convention; Craig/Beth retain cited status.
5. Midsequent and Herbrand consequences state prenex/equality/signature
   hypotheses and do not replace P2's full validity-form Herbrand theorem.
6. Church--Rosser is confluence, not normalization or existence of normal
   forms; the parallel-reduction sketch lists every missing lemma.
7. System F distinguishes Church-style decidable checking from Wells's
   Curry-style undecidability theorem.
8. The MLTT row names one calculus. Abel--Coquand--Dybjer covers typed
   beta-eta equality with one Russell universe and dependent functions; it
   does not by itself cover Sigma/identity types, cumulative universes, or all
   of CIC.
9. Gentzen's PA result is relative to the selected ordinal notations,
   reduction procedure, and transfinite-induction schema; a diagram arrow is
   not the full `N-a-049` assignment.
10. PRA is not defined as "finitism," and `Skolem1934` is not cited for the
    1923 source.
11. Number realizability does not refute Markov's principle; disjunction and
    existence properties are not inferred from the limited source
    normalization theorem.
12. Dialectica's quantifier clauses and target finite-type theory are fixed
    before conservation or extraction claims are made.
13. Epsilon theorems state whether equality is absent and which quantifier-
    free or first-order consequence is obtained.
14. Hypersequent, labelled, display, and deep-inference examples each name a
    real calculus; one derivation is not an adequacy proof.
15. Haken's lower bound is for the selected PHP/resolution encoding, not
    Frege or arbitrary CNFs; Frege and extended-Frege lower bounds remain
    open as of the cited 2026 checkpoint.
16. `A-069` and `A-074` remain Phase-6 apparatus even though P7 supplies
    harvested data. `D-P10-031` and all could/excluded rows retain explicit
    row-ID stubs or pointers rather than being marked done by nearby prose.

## Final coverage and freeze ledger

### ID coverage

- Depth-gaps coverage: all ten P7-targeted rows are named and assigned a
  ceiling: `D-P8-001` through `D-P8-007`, `D-P9-003`, `D-P9-004`, and
  `D-P10-031`.
- New-content coverage: all twenty applicable/excluded P7 rows are named:
  `N-a-015`, `N-a-049`--`N-a-058`, `N-a-069`, `N-a-070`, `N-c-027`,
  `N-c-029`, `N-c-030`, and `N-x-001`, `N-x-002`, `N-x-011`, `N-x-012`.
- Apparatus coverage: direct Phase-4 rows `A-070`, `A-071`, `A-072`, `A-073`,
  `A-075`, `A-151`, `A-152`, `A-186`, and `A-189`; deferred Phase-6 rows
  `A-069` and `A-074` are explicitly fenced.
- Defect coverage: `R-012`, `R-042`, `S-012`, `S-013`, `L-001`, and `L-005`
  are each assigned a preservation or open-repair disposition.

### Implementation blockers, not research omissions

1. The contract forbids status upgrades, while one register phrase can be
   read as demanding a proved Craig theorem. The safe implementation is a
   complete/correctly sketched Maehara method plus inherited
   `cited=Craig1957` and `cited=Beth1953` statements; only the user can
   authorize a different status contract.
2. `N-a-049` requires a full propositional ordinal assignment. The writer must
   transcribe one selected published notation/reduction system in full; the
   v1.1 source and a generic calibration diagram are insufficient.
3. `N-a-055` asks for constructive properties "with proofs," but the inherited
   normalization sketch excludes induction and equality and therefore cannot
   establish HA disjunction/existence properties. A new matched HA proof is
   required, or the row must remain open/cited at its honest ceiling.
4. The generalized-framework worked examples require exact registry sheets.
   Until those sheets exist, the body may survey and cite but cannot claim the
   examples are active handbook calculi.

### Mechanical validation record

- UTF-8/portability scan: zero non-ASCII lines after smart punctuation was
  normalized; no visible mojibake remains.
- Whitespace scan: zero trailing-whitespace lines and zero tab-containing
  lines; the file ends with a newline.
- Markdown table scan: eleven contiguous tables, all with consistent column
  counts.
- Register coverage scan against the live CSVs: 10/10 P7 depth rows and 20/20
  P7 new-content rows found; 11/11 expected apparatus IDs and 6/6 governing
  defect IDs found.
- Package scan: exactly one package heading for each of 7.1 through 7.8.
- Scope scan: this research visit changed only
  `spec/research/p07-new-content.md`; it did not edit handbook, register,
  bibliography, symbol, generated, PDF, or commit state.
- Frozen line count: 1,531 lines.

### Binary research verdict

**RESEARCH NOTE COMPLETE: YES.** All live P7 source spans, relevant register
IDs, apparatus/defect obligations, theorem hypotheses and status ceilings,
primary/authoritative sources, bibliography intake metadata, symbol
collisions, retirement dispositions, and overclaim traps are represented.
The four items immediately above are implementation decisions or owed proofs,
not missing evidence categories. The mechanical checks above pass, so this
note is frozen for writers.

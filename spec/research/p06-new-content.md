# P6 research: set theory migration and depth fill

Status: source-backed evidence ledger for the Phase-4 Part 6 visit. This is
research support, not handbook prose. It does not change a register, add a
bibliography record, establish a proof status, or by itself satisfy a treatment
row. The migrated substrate is the frozen `v1.1-verified` Part VII in
`source/formal-logic-reference.tex`. The live registers, source, existing
bibliography, primary publications, and official publisher/archive records
were checked on 2026-08-11.

## Evidence policy and claim boundary

- **Source-verified** means that the statement, proof, sketch, or citation has
  been checked in frozen v1.1 at the line range shown below.
- **Primary-verified** means that theorem metadata or a historical claim was
  checked against the original publication or its publisher/archive record.
- **Standard-secondary** means that the formulation was checked against an
  authoritative monograph or an identified modern edition.
- **Derived** means that the displayed statement follows from cited ingredients
  by the argument recorded here. It is not a citation and does not license a
  body status of `cited=<key>`.
- **Claim ceiling** is fixed by the live CSV row. `E`, `T`, `S`, and `P` mean
  entry, table/treatment, statement/survey, and pointer. They do not mean
  `proved`, `sketched`, or `cited`. Those status words remain governed by
  `handbook/CONVENTIONS.md`.
- A local complete proof may be marked `proved=annex:...` only after the annex
  actually contains every load-bearing step. A monograph theorem is
  `cited=<key>` with no annex item. A compressed or newly supplied argument
  that omits cases is `sketched=annex:...` and must enumerate the omissions.
- Register rows override narrative prose when their scopes conflict. A row is
  not complete merely because a nearby paragraph discusses its subject.

## Executive rulings and blockers

1. **R-001's repair must survive verbatim in substance.** The countable
   transitive model (`ctm`) setup is pedagogical and strictly stronger than
   bare `Con(ZFC)`. The forcing theorem and the Boolean-valued proof of the
   relative consistency of `not CH` are cited imports. The generic-filter
   existence lemma, name calculations, semantic-forcing monotonicity,
   relativization, the `CH` consistency direction, and the final syntactic
   nonderivability argument are local. New proofs of ccc and nice-name counting
   do not upgrade the cited forcing theorem or the cited Boolean-valued import.
2. **The prose instruction “Cohen forcing of `not CH`” is not satisfied by one
   Cohen real.** `Add(omega,1)` adds a real but does not establish `not CH`.
   The safe worked instance starts from a GCH model and uses
   `Add(omega,aleph_2)`, proves ccc, uses ccc preservation, and counts nice
   names.
3. **Choice-free König must use the canonical binary tree.** In ZF, a subtree
   of `2^{<omega}` with nodes at every level has a branch by a definable
   leftmost recursion. The unrestricted assertion for an arbitrary infinite
   finitely branching tree can conceal `AC_omega^fin`.
4. **BPI is not an AC equivalent.** The Boolean prime ideal theorem is
   equivalent in ZF to the ultrafilter lemma and to unrestricted propositional
   compactness, but is strictly weaker than AC. Compact Hausdorff Tychonoff is
   BPI-level; unrestricted Tychonoff is AC-level.
5. **Hausdorff's successor recursion has a nonzero-exponent hypothesis.** For
   every infinite cardinal `kappa` and nonzero cardinal `lambda`, in ZFC,
   `(kappa^+)^lambda = kappa^lambda * kappa^+`. It is false at `lambda=0`.
6. **Easton and Silver are relative/conditional statements.** Easton applies
   to regular cardinals and only to functions satisfying monotonicity and the
   cofinality constraint. Silver's theorem assumes a singular cardinal of
   uncountable cofinality and GCH below it. Neither is a ZFC calculation of an
   arbitrary singular power.
7. **Large-cardinal charts are conditional.** They record definitions,
   implication/consistency-strength direction, and consequences of an assumed
   cardinal. They do not assert that ZFC proves such cardinals exist. An
   inaccessible cardinal yields a transitive model `V_kappa` of ZFC, but the
   existence of a transitive model of ZFC is not equivalent to the existence
   of an inaccessible cardinal in the ambient universe.
8. **Reflection is formula-by-formula (or finite-family) reflection.** Never
   print a single `V_alpha \prec V`. Condensation likewise needs its exact
   elementary-substructure and limit-level hypotheses.
9. **Projective regularity is not a ZFC blanket theorem.** Borel and analytic
   regularity is available in ZFC. General projective determinacy/regularity is
   calibrated by additional large-cardinal hypotheses.
10. **A-059's NF row is time-sensitive.** It may no longer say that consistency
    of NF is open. The current public project reports a complete Lean
    construction of a model of Tangled Type Theory; `Con(NF)` then uses the
    established, paper-level NF--TTT reduction. The English deformalisation is
    not itself machine-checked, and formal verification is not the same thing
    as independent peer review.
11. **A-134 is not a Phase-4 obligation.** Its live apparatus row says
    `phase=6`, despite its adjacency to P6 apparatus and the handover's loose
    grouping. Do not mark it done in Phase 4. A P6 large-cardinal table/figure
    under A-065/A-130 is not the global PRA-to-large-cardinal ladder.
12. **HOD has no live row.** It appears in architecture prose in
    `spec/gap-analysis.tex`, but there is no P6 depth, new-content, or apparatus
    row requiring a substantive HOD entry. Under the spec-first rule, give at
    most a prose pointer already licensed by an existing row, or amend the
    register before adding content.

### Register-over-prose resolutions

The handover's compressed prose occasionally gives a lower or less specific
treatment than the CSVs. The live rows resolve those cases as follows:

- clubs/stationarity/Fodor is **E**, not merely the handover's S shorthand,
  because `D-P7-009` and `N-a-037` both require an entry-level treatment;
- the Delta-system/Ramsey package is split: `D-P7-010` requires an E-level
  entry, while `N-a-038` and `N-a-039` specifically require table treatments
  for the proof/application rows;
- ccc preservation/Cohen ccc is **E** under `D-P7-012`, while `N-a-042` also
  requires the worked `not CH` calculation in a T-level treatment; neither row
  lowers the cited status of the full forcing theorem;
- the core Polish/Borel/analytic package is **E** under `N-a-046`, even though
  the handover summarizes descriptive set theory as S/T; the projective and
  determinacy extensions stay survey/table level;
- large cardinals combine `D-P7-006`'s T-level ladder with `N-a-044`'s
  statement-level definitions and ultrapower/Scott discussion; this does not
  license full local proofs;
- L/condensation remains S plus a fine-structure pointer under `D-P7-008` and
  `N-a-067`; the word “structure” in prose does not expand `N-x-004`;
- `A-134` remains Phase 6, and the no-row HOD mention remains an ambiguity, as
  ruled above.

## Binding inventory

### Depth rows targeting P6 (19)

| row | obligation | register ceiling | evidence-safe delivery |
|---|---|---|---|
| `D-P1-001` | Zorn: statement, proof from AC, equivalence noted | E / must / S | exact statement plus a complete Hartogs/transfinite-recursion proof from well-ordering (hence AC), or downgrade to a sketch if any termination detail is omitted |
| `D-P1-002` | AC equivalents and BPI boundary | T / must / M | master table; keep BPI outside the equivalence block |
| `D-P1-003` | cardinal trichotomy and AC dependence | S / must / S | cited equivalence over ZF; distinguish ordinal trichotomy, which is a ZF theorem |
| `D-P1-004` | König infinity lemma, fan theorem, choice-free propositional compactness | E / must / M | binary-tree theorem and explicit compactness derivation in ZF; qualify the classical fan formulation |
| `D-P1-006` | countable choice, status, and uses | S / should / S | exact `AC_omega` statement and dependency table; no unverified reverse arrows |
| `D-P7-001` | ordinal arithmetic, CNF, induction versus recursion | E / must / M | full definitions/law table/CNF theorem; migrated source induction and recursion retain source statuses |
| `D-P7-002` | cardinal arithmetic, aleph/beth, regular/singular, CH/GCH | E / must / M | full reference entry with AC scope and independence pointer |
| `D-P7-003` | cofinality and König's cardinal theorem | E / must / M | exact family theorem and standard corollaries; cite primary/monograph unless a complete annex proof is supplied |
| `D-P7-004` | Easton's theorem | S / should / S | conditional cited statement on regular cardinals only |
| `D-P7-005` | Martin's axiom and examples | S / should / S | exact `MA_kappa`/MA statement, `MA_{aleph_1} -> SH`, iteration proof only as a pointer |
| `D-P7-006` | large-cardinal ladder | T / must / M | definitions through supercompact plus conditional implication/consistency chart |
| `D-P7-007` | Lévy hierarchy, reflection, Shoenfield | E / must / M | definition/table plus cited theorems with exact transitivity/ordinal/parameter hypotheses |
| `D-P7-008` | condensation and L | S / should / M | cited condensation and `GCH in L`; fine structure only a pointer |
| `D-P7-009` | club, stationary, Fodor | E / should / M | exact regular-uncountable hypotheses and diagonal intersection |
| `D-P7-010` | Delta-system and Ramsey | E / must / S | finite-set Delta-system lemma, proof, infinite Ramsey theorem; Erdos--Rado separately calibrated |
| `D-P7-011` | Boolean-valued models; products/iterations/proper pointers | S / should / M | Boolean-valued statement; product and iteration pointers; proper forcing no more than pointer |
| `D-P7-012` | ccc preservation and Cohen ccc proved | E / must / M | local annex proofs of the Delta-system ccc argument and preservation; nice-name count supplies the `not CH` application |
| `D-P7-013` | Borel/projective hierarchy and regularity survey | S / should / M | exact pointclass definitions and ZFC regularity boundary |
| `D-P7-014` | Borel determinacy and AD versus AC | S / should / S | cited Gale--Stewart/Martin statements and a calibrated PD pointer |

`D-P1-005` is deliberately absent: its live target is P2.1, not P6. It may
be cross-referenced from A-063 but must not be claimed as a P6 depth-row
completion.

### New-content rows targeting P6 (17 in scope, 3 exclusions)

| row | ceiling | claim-safe payload |
|---|---|---|
| `N-a-035` | E / must | cofinality, regular/singular, König cardinal theorem, Hausdorff successor recursion; Easton remains S-level inside the package |
| `N-a-036` | S / could | Silver theorem with exact hypotheses plus PCF pointer; an explicit stub is honest if omitted |
| `N-a-037` | E / must | club/stationary/Fodor/diagonal intersection at regular uncountable `kappa` |
| `N-a-038` | T / must | finite-set Delta-system proof and the Cohen ccc pattern |
| `N-a-039` | T / must | infinite Ramsey table row and exact Erdos--Rado statement/arrow notation |
| `N-a-040` | S / should | binary König lemma, cited existence of an `omega_1`-Aronszajn tree, Suslin hypothesis and independence; no unverified explicit construction |
| `N-a-041` | S / should | exact diamond/square conventions and one application each; exact MA statement and ccc consequence |
| `N-a-042` | T / must | `Add(omega,aleph_2)` over GCH, ccc, ccc preservation, distinct generics, nice-name upper bound |
| `N-a-043` | S / should | symmetric-model method and one basic Fraenkel permutation model of ZFA; transfer to pure ZF cited |
| `N-a-044` | S / must | definitions inaccessible--supercompact, measurable ultrapower/embedding statement, Scott's `V != L`, chart |
| `N-a-045` | T / should | Lévy levels/absoluteness table, reflection, Shoenfield statement and forcing application |
| `N-a-046` | E / must | Polish/Borel/analytic, Suslin theorem, perfect-set/Baire/measurability facts with exact class boundary |
| `N-a-047` | P / could | lightface/effective pointclass pointer only; explicit stub is permitted |
| `N-a-048` | S / should | games, open determinacy, Borel determinacy, AD/AC incompatibility, precisely conditional PD pointer |
| `N-a-066` | E / must | ordinal arithmetic as a theory, CNF, induction and recursion |
| `N-a-067` | S / should | L, condensation, `GCH in L`, reflection, Jensen fine-structure pointer |
| `N-a-068` | S / should | Boolean-valued model statement; product and iterated forcing pointers |
| `N-x-003` | P / excluded | proper/iterated forcing and PFA/MM beyond a pointer |
| `N-x-004` | P / excluded | inner models, core models, and fine structure beyond an L/Jensen pointer |
| `N-x-005` | P / excluded | PCF beyond the Silver statement and a Shelah pointer |

### Direct P6 apparatus rows

| row | live phase | required evidence product | ruling |
|---|---:|---|---|
| `A-058` | 4 | ZFC axiom table | formal formulas and schema side conditions; use the source's exact axiom basis |
| `A-059` | 4 | ZF/Z/KP/NBG/MK/NF comparison | declare variant conventions; NF consistency row must reflect the 2025 result |
| `A-060` | 4 | ordinal-law table | recursive orientation, continuity, distributivity direction, failures, CNF |
| `A-061` | 4 | cardinal-law table | state AC scope, cofinality, König, aleph/beth, CH/GCH |
| `A-062` | 4 | AC-equivalents table | separate full AC, BPI, and restricted compactness/Tychonoff forms |
| `A-063` | 4 | choice dependency table | theorem-by-theorem exact principle; include choice-free countable propositional compactness |
| `A-064` | 4 | combinatorial-principles table | definitions, hypotheses, implications, independence/citation status |
| `A-065` | 4 | large-cardinal ladder table | conditional definitions/implications, not existence assertions |
| `A-066` | 4 | independence catalog | every row must be relative and name its method/source |
| `A-067` | 4 | forcing-poset catalog | exact poset convention; preservation claims carry hypotheses |
| `A-068` | 4 | Borel/projective table | distinguish ZFC facts from determinacy/large-cardinal consequences |
| `A-129` | 4 | ordinals-to-epsilon-zero figure | schematic landmarks and supremum, not a literal number line |
| `A-130` | 4 | cumulative hierarchy figure | rank indexing exact; large-cardinal stages conditional |
| `A-131` | 4 | constructible hierarchy figure | `Def` successor, union limit, `L_alpha subseteq V_alpha`; no set-sized L |
| `A-132` | 4 | forcing-extension figure | names/evaluation/generic/extension; mark cited same-ordinals theorem |
| `A-133` | 4 | choice implication figure | show only verified arrows and label non-reversals by source/model |
| `A-134` | **6** | global PRA-to-large-cardinal ladder | out of Phase 4 despite the P6 grouping; leave open |
| `A-135` | 4 | pointclass figure | Borel union/intersection alternation and projective projection/complement arrows |
| `A-164` | 4 | set-theory symbol subtable | one forcing macro, scopes/types, name versus evaluation, rank indexing |
| `A-186` | 4 | P6 further reading | annotated, source-real list; not merely uncited titles |

## Frozen v1.1 substrate and R-001 status map

| source lines | substrate | migration/status constraint |
|---:|---|---|
| 10060--10088 | Part VII scope and foundations warning | migrate the distinction between metatheory and object theory |
| 10089--10263 | language, ZF/ZFC axioms and schemata | source basis for A-058; preserve all freshness/functionality side conditions |
| 10272--10335 | first constructions and axiom use | compress as a dependency register; do not detach constructions from axioms |
| 10356--10444 | transitive sets, ordinals, trichotomy, transfinite induction/recursion | ordinal trichotomy and both method theorems are source material; new arithmetic is additional content |
| 10452--10519 | cumulative hierarchy and rank | exact rank indexing for A-130 |
| 10521--10556 | Mostowski collapse | retain well-foundedness and extensionality hypotheses |
| 10559--10654 | cardinals, Hartogs, AC equivalents, aleph/CH/GCH | preserve explicit AC dependence of ordinal-cardinal notation |
| 10678--10768 | constructible hierarchy and relativization | L theorem/citations remain at their source statuses |
| 10773--10824 | ctm convention and strength warning | source explicitly says ctm is stronger than `Con(ZFC)`; the comparison remark is only a proof sketch |
| 10826--10880 | filters, dense sets, genericity, bounded absoluteness | exact forcing order is “stronger = smaller” |
| 10882--10898 | generic-filter existence | local complete proof under the fixed external countability hypothesis |
| 10900--10967 | names, interpretation, extension, check names, semantic forcing | local definitions/name inductions; no recursive forcing relation is defined locally |
| 10989--11010 | monotonicity of semantic forcing | local complete proof |
| 11012--11051 | forcing theorem and extension preservation | **cited** `Jech2003`, pp. 201--224; definability is formula-by-formula; no annex proof may silently replace this import |
| 11053--11102 | one Cohen real | local name computation and new-real proof; source explicitly says it does not prove `not CH` |
| 11107--11238 | relativization and `Con(ZFC) -> Con(ZFC+CH)` | local syntactic construction/proof |
| 11240--11278 | `Con(ZFC) -> Con(ZFC+not CH)` | **cited Boolean-valued import**, including ccc/preservation; new local support is not the whole theorem |
| 11280--11291 | arithmetized implications | proof sketch; omitted proof-predicate translations are named |
| 11294--11313 | nonderivability of CH and its negation | local complete syntactic proof from the two relative-consistency results |
| 11315--11335 | final warnings | preserve both “no proof of Con(ZFC)” and “ctm is pedagogical only” |

The live defect row `R-001` is fixed at Phase 2. Its acceptance criterion was
not merely that the prose mention forcing: the `not CH` direction had to be an
honest citation or a correct syntactic/Boolean-valued proof, and the final
nonderivability step had to be syntactic rather than appeal to unexhibited
models. Any P6 rewrite that reverts to “choose two models and apply soundness”
reopens the defect.

## Research package 6.0: axioms, variants, hierarchy, and collapse

### A-058: exact ZFC axiom-table surface

Use the first-order language with equality and membership. Bound variables in
schema formulas range over sets; displayed `b` is fresh where indicated.

| axiom/schema | claim-safe formal form and side condition |
|---|---|
| Extensionality | `forall x forall y[(forall z(z in x iff z in y)) -> x=y]` |
| Empty set | `exists e forall x(x notin e)`; the source takes this as an explicit axiom even though other bases derive it |
| Pairing | `forall x forall y exists p forall z[z in p iff (z=x or z=y)]` |
| Union | `forall a exists u forall x[x in u iff exists y(y in a and x in y)]` |
| Power Set | `forall a exists p forall x[x in p iff x subseteq a]`, with `x subseteq a` expanded or previously defined |
| Infinity | some set contains the empty set and is closed under `x -> x union {x}`; do not substitute “there is an infinite set” without proving equivalence in the chosen base |
| Separation | for each formula `phi(x,p_1,...,p_n)`, `forall a exists b forall x[x in b iff (x in a and phi(x,p_1,...,p_n))]`; `b` is not free in `phi` |
| Replacement | for each `phi(x,y,p_1,...,p_n)`, if `phi` is functional in `y` on `a`, then its exact image is a set; bind all parameters and keep the uniqueness premise |
| Foundation | `a != empty -> exists x in a forall y in a(y notin x)`; equivalent formulations need not be mixed in the same row |
| Choice | for every set `A` of nonempty sets there is a function `f` with domain `A` and `f(x) in x` for every `x in A` |

Standard-secondary locator: `Jech2003`, Chapters 1--2, pp. 3--15,
[Springer record and DOI](https://link.springer.com/book/10.1007/3-540-44761-X).
Source-verified locator: v1.1 lines 10103--10263.

### A-059: system-variant table

The abbreviations are convention-sensitive; place the convention in the table
caption or first column.

| system | objects/classes | Foundation and Choice | comparison language that is safe |
|---|---|---|---|
| ZF | one set sort; classes are metalinguistic/definable abbreviations | Foundation included; AC omitted | base theory used here; ZFC is ZF+AC |
| Z | define it here as ZF without Replacement, retaining Foundation | AC omitted; `ZC` means Z+AC | weaker axiom basis than ZF; do not attribute every historical “Zermelo set theory” convention to this row |
| KP | one set sort; Extensionality, Pairing, Union, Infinity, Foundation/Set Induction, `Delta_0` Separation and `Delta_0` Collection | standard KP has neither Power Set nor AC; `KP^P` is a different variant | admissible sets are transitive KP models; do not call KP “ZF minus Power Set” because its Separation/Collection are also restricted |
| NBG | two-sorted sets/classes; predicative elementary class comprehension | use the declared convention `NBG = GB + Global Choice` | conservative over ZFC for set-language sentences; if Global Choice is omitted, label the theory GB instead of silently changing the row |
| MK/KM | two-sorted; impredicative class comprehension permits class quantifiers | Global/Class Choice is convention-dependent and must be a separate cell | stronger and nonconservative over NBG/ZFC; do not identify its exact strength with “one inaccessible cardinal” |
| NF | one set sort; Extensionality plus stratified Comprehension; no primitive class sort | universal set exists, Foundation fails, and NF refutes AC | not a rung on the ZF/NBG/MK inclusion ladder; current consistency evidence is the Lean-checked TTT model plus paper-level NF--TTT reduction |

Authoritative locators:

- ZF/Z: `Jech2003`, Chapters 1--2, pp. 3--15.
- KP/admissibility: Jon Barwise, *Admissible Sets and Structures*, Part A;
  original Springer 1975 edition, xiii+394 pp., ISBN 978-3-540-07451-9, or
  the [2017 ASL/Cambridge reissue](https://doi.org/10.1017/9781316717196).
- NBG and MK: existing `Mendelson1997`, Chapter 4 “Axiomatic Set Theory,”
  pp. 225--304, especially the “Other Axiomatizations”/MK discussion; John L.
  Kelley, *General Topology*, Appendix “Elementary Set Theory,” beginning
  p. 250, [official Springer record](https://link.springer.com/book/9780387901251).
- NF definition: `Quine1937`, pp. 70--80,
  [publisher DOI](https://doi.org/10.1080/00029890.1937.11987928).
- Failure of AC in NF: `Specker1953`, pp. 972--975,
  [PNAS DOI](https://doi.org/10.1073/pnas.39.9.972).
- Current consistency surface: Sky Wilshaw, *New Foundations is consistent*,
  18 June 2025, 61 pp., [deformalisation PDF](https://leanprover-community.github.io/con-nf/print/print.pdf)
  and [formalization project](https://leanprover-community.github.io/con-nf/).
  The project says the TTT model construction is formalized and that the
  passage from it to `Con(NF)` is “on paper.” Do not strengthen that wording.

### Cumulative hierarchy, rank, and Mostowski

The hierarchy is

`V_0=empty`, `V_{alpha+1}=P(V_alpha)`, and
`V_lambda=union_{beta<lambda}V_beta` for limit `lambda`.

The exact rank equation is

`rank(x)=sup{rank(y)+1:y in x}`.

Thus `x in V_{rank(x)+1}` and, with the source's indexing, the first stage that
contains `x` as a member is `rank(x)+1`; A-130 must not shift the axis by one.
The Mostowski theorem requires a relation `R` on a set `A` that is both
well-founded and extensional; then there is a unique transitive set `M` and a
unique isomorphism `(A,R) -> (M,in)`. Dropping extensionality destroys
injectivity. These are source-migrated facts at lines 10452--10556, not new
large-cardinal results.

For A-130, an inaccessible label is conditional: if `kappa` is strongly
inaccessible, then `V_kappa` satisfies ZFC. Do not draw the ctm used in the
forcing tutorial as though it must be some `V_kappa` in the ambient universe.

## Research package 6.1: ordinal arithmetic (`D-P7-001`, `N-a-066`, A-060, A-129)

### Exact recursive definitions

For ordinals `alpha,beta`, recurse on the **right-hand** argument:

```text
alpha + 0          = alpha
alpha + (beta+1)   = (alpha+beta)+1
alpha + lambda     = sup_{beta<lambda}(alpha+beta)       (lambda limit)

alpha * 0          = 0
alpha * (beta+1)   = alpha*beta + alpha
alpha * lambda     = sup_{beta<lambda}(alpha*beta)       (lambda limit)

alpha^0            = 1
alpha^(beta+1)     = alpha^beta * alpha
alpha^lambda       = sup_{beta<lambda}alpha^beta         (lambda limit, alpha>0)
```

Handle the base `alpha=0` separately at limit exponents if the chosen
convention discusses `0^0`; do not let a table accidentally define that case
twice. These definitions are ordinal, not cardinal, operations.

### Law table

| law | safe statement |
|---|---|
| associativity | `(alpha+beta)+gamma=alpha+(beta+gamma)` and `(alpha*beta)*gamma=alpha*(beta*gamma)` |
| distributivity | `alpha*(beta+gamma)=alpha*beta+alpha*gamma` (left distributivity in the conventional naming); `(alpha+beta)*gamma=alpha*gamma+beta*gamma` is false in general |
| exponent sum | `alpha^(beta+gamma)=alpha^beta*alpha^gamma` for the usual nonzero-base convention |
| right-argument continuity | for limit `lambda`, each operation is the supremum of its earlier values in the right argument, as in the definitions |
| monotonicity | addition, multiplication by positive `alpha`, and exponentiation for `alpha>1` are strictly increasing in the right argument; left-argument behavior is weaker and must not be copied from cardinals |
| failures | addition and multiplication are not commutative; e.g. `1+omega=omega` but `omega+1>omega`, and `2*omega=omega` but `omega*2>omega` |

**Cantor normal form.** Every nonzero ordinal `alpha` has a unique expression

`alpha = omega^{beta_0} n_0 + ... + omega^{beta_{k-1}} n_{k-1}`

where `k>=1`, `beta_0>...>beta_{k-1}`, and each `n_i` is a positive natural
number. Uniqueness includes both the exponent sequence and coefficients.

**Induction versus recursion.** Transfinite induction is a proof principle:
if `forall alpha[(forall beta<alpha phi(beta))->phi(alpha)]`, then `phi` holds
for every ordinal. Transfinite recursion is an existence-and-uniqueness
theorem for a function `F` satisfying
`F(alpha)=G(F restricted to alpha)` (with the functional/class hypotheses made
explicit). The source already states and proves its chosen forms at
10413--10444; arithmetic/CNF is the new material.

Standard-secondary locator: `Jech2003`, Chapter 2, pp. 17--26. The original
source of the arithmetic notation need not be used as a theorem-status
citation when the handbook supplies complete elementary derivations.

### A-129 figure constraints

Use ordered landmarks, not a geometrically literal number line:

`0,1,...,omega,omega+1,...,omega*2,...,omega^2,...,omega^omega,...,epsilon_0`.

Define `epsilon_0` as the least fixed point of `alpha -> omega^alpha`, and also
as the supremum of the finite tower sequence
`alpha_0=1`, `alpha_{n+1}=omega^{alpha_n}`. It is not any one finite tower.
CNF annotations should illustrate that every ordinal below `epsilon_0` has a
finite notation built by the displayed operations; the picture must not imply
that all ordinals fit on a real interval.

## Research package 6.2: Choice, maximality, and choice-free compactness

### Zorn from AC (`D-P1-001`)

**Exact theorem.** Let `(P,<=)` be a nonempty poset. If every chain `C subseteq
P` has an upper bound in `P`, then `P` has a maximal element. If the empty set
is counted as a chain, the upper-bound hypothesis itself implies `P` is
nonempty; choose one convention and state it.

**Complete proof route licensed by AC.** AC gives a well-order `triangleleft`
of `P`. By transfinite recursion, after choosing a strictly increasing chain
`<p_beta:beta<alpha>`, choose the `triangleleft`-least element strictly above
every earlier `p_beta`, if one exists. If this never stopped before the Hartogs
ordinal `h(P)`, the sequence would inject `h(P)` into `P`, contradiction. At
the first stopping stage, the accumulated chain has an upper bound `u` by
hypothesis. If `u` were not maximal, a `v>u` would lie strictly above every
earlier `p_beta`, contradicting the stopping condition. Thus `u` is maximal.

This is a genuinely complete annex proof only if the recursion, chain
invariant, Hartogs termination, and last maximality argument all appear. A
phrase such as “continue choosing until maximal” is not a proof.

Standard-secondary locators: `Jech1973Choice`; `Halbeisen2017`, Chapters 5--6,
pp. 135--175 and 191--219,
[Springer DOI](https://doi.org/10.1007/978-3-319-60231-8).

### AC-equivalence table (`D-P1-002`, A-062)

Over ZF, the following belong in the full-AC equivalence block:

- every family of nonempty sets has a choice function;
- every set can be well ordered;
- Zorn's maximal-element lemma;
- Tukey's lemma for families of finite character;
- the product of any family of nonempty sets is nonempty;
- Tychonoff's theorem for arbitrary compact spaces.

The following belongs in a separately shaded **BPI** block:

- every Boolean algebra has a prime ideal / every proper filter extends to an
  ultrafilter;
- unrestricted propositional compactness;
- Tychonoff's theorem for compact Hausdorff spaces.

`BPI -> AC` is false relative to ZF; the live `HalpernLevy1971` record is the
primary independence citation. Do not turn the visual proximity of the blocks
into an implication not recorded by a source.

**Cardinal trichotomy (`D-P1-003`).** In ZF, “for all sets `A,B`, either
`|A|<=|B|` or `|B|<=|A|`” is equivalent to AC. With AC, cardinal trichotomy
follows. By contrast, any two **ordinals** are comparable in ZF; do not cite AC
for ordinal trichotomy.

### Countable choice and the implication diagram (`D-P1-006`, A-063, A-133)

Use these exact principles:

- `AC_omega`: for every sequence `<X_n:n in omega>` of nonempty sets there is
  `f` with `f(n) in X_n`.
- `AC_omega^fin`: the same assertion when every `X_n` is finite.
- `DC`: if `X` is nonempty and `R subseteq X times X` is serial
  (`forall x exists y xRy`), then there is a sequence `<x_n>` with
  `x_n R x_{n+1}`.
- `BPI`: every Boolean algebra has a prime ideal (equivalently, every proper
  filter extends to an ultrafilter).

Verified arrows are `AC -> DC -> AC_omega -> AC_omega^fin` and `AC -> BPI`.
`BPI` is strictly below AC (`HalpernLevy1971`). `BPI + AC_omega` still does not
imply DC: Paul Howard and Jean E. Rubin, “The Boolean Prime Ideal Theorem Plus
Countable Choice Do Not Imply Dependent Choice,” *Mathematical Logic
Quarterly* 42 (1996), 410--420,
[DOI](https://doi.org/10.1002/malq.19960420133). Models of ZF+DC without free
ultrafilters on `omega` show that DC does not imply BPI; the Solovay model is a
standard conditional source (`Solovay1970Measurable`). For any additional
non-arrow, use `HowardRubin1998`'s exact form entry rather than extrapolate from
the diagram.

The dependency table should record at least:

| result/use | safe choice status |
|---|---|
| binary-tree König lemma below | ZF |
| compactness for a countable set of propositional variables below | ZF by the binary-tree proof |
| unrestricted propositional compactness | equivalent to BPI over ZF |
| arbitrary cardinal comparability/trichotomy | equivalent to AC over ZF |
| Zorn and unrestricted well-ordering | equivalent to AC over ZF |
| choosing a successor through an arbitrary sequence of nonempty finite sets | at most `AC_omega^fin`; avoid claiming ZF without canonical coding |
| generic-filter construction over an externally countable `M` | external recursive choices after an enumeration; the book's metatheory must be declared |

### Choice-free König/fan route (`D-P1-004`, `N-a-040`)

**ZF theorem.** If `T subseteq 2^{<omega}` is prefix closed and for every
`n` has a node of length `n`, then there is `b in 2^omega` such that
`b restricted to n in T` for every `n`.

Define a node `s` to be *unbounded in height* when for every `m>=|s|` it has an
extension in `T` of length `m`. The empty node is unbounded. If `s` is
unbounded, at least one of `s^0,s^1` is unbounded, since a union of two bounded
height sets is bounded. Recurse by choosing `0` when the `0`-child is
unbounded and `1` otherwise. This choice is definable, not an invocation of a
choice function, and its union is the desired branch.

**Countable propositional compactness in ZF.** Enumerate the variables and a
countable theory `Gamma={phi_0,phi_1,...}`. Let `T` consist of finite binary
assignments `s` for which some total valuation extending `s` satisfies the
first `|s|` formulas. Finite satisfiability makes every level nonempty; prefix
closure is immediate. A branch `b` from the preceding theorem satisfies every
`phi_i`: choose a level beyond `i` and beyond every variable occurring in
`phi_i`, then all extending valuations agree with `b` on that formula. No
sequence of independently chosen finite models is required.

**Classical fan formulation.** The contrapositive says that if a set of finite
binary strings meets every branch (“a bar”), then a finite level bound already
meets every branch. Say **classical fan theorem/compactness of Cantor space**.
Do not identify this unqualifiedly with every constructive version of
Brouwer's fan theorem.

Primary metadata for the historical infinity lemma: `Konig1927Infinity`,
Dénes Kőnig, “Über eine Schlussweise aus dem Endlichen ins Unendliche,” *Acta
Scientiarum Mathematicarum (Szeged)* 3 (1927), 121--130,
[archive record](https://acta.bibl.u-szeged.hu/13338/).

## Research package 6.3: cardinal arithmetic (`D-P7-002`--`005`, `N-a-035`--`036`, A-061)

### Definitions and ZFC laws

State the AC scope at the start. In ZF, not every set has an initial ordinal of
the same size and arbitrary cardinals need not be comparable. Under ZFC:

- `aleph_0=|omega|`, `aleph_{alpha+1}=(aleph_alpha)^+`, and at a limit
  `aleph_lambda=sup_{alpha<lambda}aleph_alpha`;
- `beth_0=aleph_0`, `beth_{alpha+1}=2^{beth_alpha}`, and
  `beth_lambda=sup_{alpha<lambda}beth_alpha`;
- for infinite cardinals `kappa,lambda` with at least one nonzero,
  `kappa+lambda=kappa*lambda=max(kappa,lambda)`;
- Cantor: `kappa<2^kappa`;
- `cf(alpha)` is the least order type/cardinality of an unbounded subset of
  the limit ordinal `alpha`; an infinite cardinal `kappa` is regular iff
  `cf(kappa)=kappa`, singular otherwise;
- `CH` is `2^{aleph_0}=aleph_1`; `GCH` is
  `forall infinite kappa (2^kappa=kappa^+)`.

Avoid the false heuristic “cardinal exponentiation is always max.” Apart from
special cases, ZFC leaves it underdetermined.

### König's cardinal theorem

**Exact family form.** For a set-indexed family of cardinals with
`kappa_i<lambda_i` for every `i in I`,

`sum_{i in I} kappa_i < product_{i in I} lambda_i`.

The diagonal step takes any proposed enumeration of the product by the
disjoint sum and, coordinate by coordinate, chooses a value omitted by the
`i`-th coordinate values coming from the `i`-th summand. This is a ZFC cardinal
theorem; do not present the proof as choice-free without auditing its family of
coordinate choices. A standard consequence is
`kappa < cf(2^kappa)`. The existing `Konig1905` record is the primary source;
`Jech2003`, cardinal-arithmetic chapter pp. 47--61, is the modern locator.

### Hausdorff successor recursion

**Exact safe formulation (ZFC).** For every infinite cardinal `kappa` and
every **nonzero** cardinal `lambda`,

`(kappa^+)^lambda = kappa^lambda * kappa^+ = max(kappa^lambda,kappa^+)`.

Equivalent aleph notation is
`aleph_{alpha+1}^{aleph_beta} = aleph_alpha^{aleph_beta} * aleph_{alpha+1}`.

**Derived proof check.** If `lambda<kappa^+`, regularity of `kappa^+` bounds
the range of every `f:lambda->kappa^+` below some `gamma<kappa^+`; there are at
most `kappa^+ * kappa^lambda` such functions. If `lambda>=kappa^+`, then
`(kappa^+)^lambda <= (2^kappa)^lambda = 2^lambda <= kappa^lambda`, while the
reverse inequality is immediate. The lower bound `kappa^+` is also immediate
for nonzero `lambda`. At `lambda=0`, the formula fails: the left side is `1`
and the displayed product is `kappa^+`.

Primary locator: `Hausdorff1904`, Felix Hausdorff, “Der Potenzbegriff in der
Mengenlehre,” *Jahresbericht der Deutschen Mathematiker-Vereinigung* 13
(1904), 569--571, verified in the
[Hausdorff Center bibliography](https://www.mathematics.uni-bonn.de/hcm/felix-hausdorff/schriftenverzeichnis).

### Easton's theorem

Let `F` be a class function on the infinite regular cardinals such that:

1. `kappa<=lambda -> F(kappa)<=F(lambda)` (monotonicity); and
2. `kappa<cf(F(kappa))` for every regular `kappa` (König constraint).

The model-theoretic/relative-consistency form says that, starting with an
appropriate model of ZFC+GCH and such an `F`, there is a cofinality-preserving
forcing extension in which `2^kappa=F(kappa)` for every infinite regular
`kappa`. It does not classify the continuum function at singular cardinals,
and it does not prove a chosen `F` is realized in the ground universe.

Primary: existing `Easton1970`, pp. 139--178,
[DOI](https://doi.org/10.1016/0003-4843(70)90012-4). Modern locator:
`Jech2003`, forcing applications, pp. 225--265.

### Silver and the PCF boundary (`N-a-036`, `N-x-005`)

**Silver theorem.** If `kappa` is a singular cardinal with
`cf(kappa)>omega`, and `2^lambda=lambda^+` for every infinite cardinal
`lambda<kappa`, then `2^kappa=kappa^+`.

This is the exact statement licensed at S level. It does not cover countable
cofinality and is not “SCH is true.” Cite `Silver1975`, Jack Silver, “On the
Singular Cardinals Problem,” *Proceedings of the International Congress of
Mathematicians, Vancouver 1974*, vol. 1 (Canadian Mathematical Congress,
1975), 265--268,
[official IMU proceedings PDF](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1974.1/ICM1974.1.ocr.pdf).

The only licensed continuation is a pointer to `Shelah1994Cardinal`, Saharon
Shelah, *Cardinal Arithmetic*, Oxford Logic Guides 29, Clarendon/OUP, 1994,
[publisher DOI](https://doi.org/10.1093/oso/9780198537854.001.0001).
`N-x-005` excludes a local PCF development.

### Martin's axiom (`D-P7-005`, part of `N-a-041`)

For an infinite cardinal `kappa`, `MA_kappa` says: for every ccc poset `P` and
every family `D` of at most `kappa` dense subsets of `P`, there is a filter on
`P` meeting each member of `D`. `MA` means `MA_kappa` for every
`kappa<2^{aleph_0}`. A safe sample consequence is
`MA_{aleph_1} ->` the Suslin hypothesis. Consistency proofs for MA use
iterations and remain pointers under `N-x-003`; do not smuggle an iteration
proof into this S-level entry. `Jech2003`, pp. 267--283, is the standard
secondary locator.

## Research package 6.4: infinitary combinatorics (`D-P7-009`--`010`, `N-a-037`--`041`, A-064)

### Clubs, stationarity, normality, and Fodor

Fix a **regular uncountable** cardinal `kappa` unless a row explicitly says
otherwise.

- `C subseteq kappa` is unbounded when `forall alpha<kappa exists beta in C
  (alpha<beta)`.
- `C` is closed when it contains the supremum of every increasing sequence of
  members of length `<kappa` whose supremum is below `kappa` (equivalently,
  it contains its limit points below `kappa`).
- `C` is club when it is closed and unbounded.
- `S subseteq kappa` is stationary when it meets every club subset of `kappa`.
- For `<C_xi:xi<kappa>`, the diagonal intersection is
  `Delta_{xi<kappa} C_xi={alpha<kappa:forall xi<alpha(alpha in C_xi)}`.
  If every `C_xi` is club, the diagonal intersection is club. This is the
  normality ingredient for the club filter.
- **Fodor/pressing down.** If `S subseteq kappa` is stationary and
  `f:S->kappa` is regressive (`f(alpha)<alpha` for every nonzero `alpha in S`),
  then some fiber `f^{-1}{beta}` is stationary.

Do not omit regularity or uncountability from Fodor. Do not replace
“stationary fiber” by merely “uncountable fiber.” Existing primary key
`Fodor1956`, pp. 139--142; archive:
<http://acta.bibl.u-szeged.hu/id/eprint/13806>. Modern locator:
`Jech2003`, pp. 91--105.

### Delta systems and Cohen ccc (`D-P7-010`, `N-a-038`)

**Delta-system lemma.** Every uncountable family of finite sets has an
uncountable subfamily `B` and a finite root `r` such that
`x intersect y=r` whenever `x!=y` are in `B`.

The usual proof first thins to constant finite size and then inducts on that
size; if no uncountable pairwise-disjoint subfamily exists, choose a maximal
countable disjoint family and a point meeting uncountably many members, remove
that point, and apply induction. Any annex marked complete must make the
thinning and maximal-family cases explicit. The generalized lemma for families
of `<kappa`-sized sets needs additional regularity/cardinal-arithmetic
hypotheses and is not licensed by this row.

**Cohen compatibility pattern.** In
`Add(omega,kappa)=Fn(kappa times omega,2,<omega)` ordered by reverse inclusion,
apply the Delta-system lemma to the finite domains of an uncountable family of
conditions. Thin again so that all conditions have the same values on the
finite root (there are only finitely many root assignments). Any two remaining
conditions then have compatible union. Hence the poset is ccc.

Primary: existing `Shanin1946`, pp. 399--400. Modern locator: `Jech2003`,
pp. 107--123. The ccc application is a derived local proof and can support an
annex `proved` status if printed in full.

### Ramsey and Erdos--Rado (`N-a-039`)

Use arrow notation only after defining it:

`kappa -> (lambda)^r_mu`

means that for every coloring `c:[kappa]^r -> mu`, some `H subseteq kappa`
of cardinality `lambda` is homogeneous.

- **Infinite Ramsey theorem.** For all positive finite `r` and finite `k`,
  `omega -> (omega)^r_k`.
- Define `beth_0(kappa)=kappa` and
  `beth_{n+1}(kappa)=2^{beth_n(kappa)}`. A safe Erdos--Rado form is, for every
  infinite `kappa` and finite `n`,
  `beth_n(kappa)^+ -> (kappa^+)^{n+1}_kappa`.

Do not replace the latter with an uncited stronger polarized or singular
partition relation. Existing primary records: `Ramsey1930`, pp. 264--286,
[DOI](https://doi.org/10.1112/plms/s2-30.1.264), and `ErdosRado1956`,
pp. 427--489,
[AMS DOI](https://doi.org/10.1090/S0002-9904-1956-10036-0).

### Trees and the Suslin hypothesis (`N-a-040`)

An `omega_1`-tree has height `omega_1` and countable levels. An Aronszajn tree
is such a tree with no branch of order type `omega_1`; ZFC proves that one
exists. A Suslin tree is an `omega_1`-tree with neither an uncountable chain nor
an uncountable antichain. The Suslin hypothesis says that no Suslin tree exists
(equivalently, in the standard correspondence, there is no Suslin line).

At this S ceiling, cite the Aronszajn existence theorem and give a construction
pointer. Do not print a one-line “construction” unless countability of every
level and absence of an `omega_1` branch have both been verified. Historical
metadata: `Kurepa1935`, Đuro Kurepa, “Ensembles ordonnés et ramifiés,”
*Publications de l'Institut Mathématique* 4 (1935), 1--138,
[EuDML](http://eudml.org/doc/253633). Modern survey:
`Todorcevic1984Trees`, Stevo Todorcevic, “Trees and Linearly Ordered Sets,” in
Kunen and Vaughan (eds.), *Handbook of Set-Theoretic Topology*, pp. 235--293,
[DOI](https://doi.org/10.1016/B978-0-444-86580-9.50009-4).

Independence boundary: Jensen's constructible methods give a Suslin tree in
`L`, while `MA_{aleph_1}` implies there is none. Therefore SH is independent
relative to the relevant consistency assumptions. This is not a locally proved
independence theorem.

### Diamond and square (`N-a-041`)

Declare the convention because variants proliferate.

- `diamond_{omega_1}`: a sequence `<A_alpha:alpha<omega_1>` with
  `A_alpha subseteq alpha` such that for every `A subseteq omega_1`, the set
  `{alpha<omega_1:A intersect alpha=A_alpha}` is stationary. Safe application:
  `diamond_{omega_1}` implies an `omega_1`-Suslin tree.
- `square_kappa`: a sequence
  `<C_alpha:alpha<kappa^+, alpha limit>` where each `C_alpha` is club in
  `alpha`, `otp(C_alpha)<=kappa`, coherence holds
  (`beta in Lim(C_alpha) -> C_beta=C_alpha intersect beta`), and there is no
  club thread `C subseteq kappa^+` with
  `C intersect alpha=C_alpha` at all relevant limit points. Safe application:
  this full square principle yields a `kappa^+`-Aronszajn tree.

Do not write merely “square = coherent clubs”; the no-thread clause is
load-bearing. `Jech2003`, pp. 107--123, and the Jensen fine-structure source
below are the safe locators.

## Research package 6.5: constructibility, forcing, and independence

### Constructible hierarchy (`D-P7-008`, `N-a-067`, A-131)

The definitions are

`L_0=empty`, `L_{alpha+1}=Def(L_alpha)`, and
`L_lambda=union_{beta<lambda}L_beta` at limits, with
`L=union_{alpha in Ord}L_alpha`. `Def(L_alpha)` means subsets first-order
definable over `(L_alpha,in)` with parameters from `L_alpha`. It is a
formula-by-formula construction, not an internal global truth predicate.

**Condensation.** If `alpha` is an appropriate limit ordinal and
`X \prec (L_alpha,in)`, then the transitive collapse of `X` is some
`(L_beta,in)`. State the exact level convention used by the cited source; do
not omit elementarity or substitute arbitrary `X subseteq L_alpha`.

**Gödel result.** `L` is an inner model of ZFC+GCH (and hence AC). This remains
a cited theorem. Existing source lines 10678--10768 give L and a cited
relativization scheme; they do not supply a local fine-structure proof.

For A-131, show `L_alpha subseteq V_alpha`, successor `Def`, limit union, and
the proper-class continuation through all ordinals. A nested sketch must not
suggest that `L` is a set or that every `V_alpha` equals `L_alpha`.

Fine structure is only a pointer under `N-x-004`: `Jensen1972FineStructure`,
R. Björn Jensen, “The Fine Structure of the Constructible Hierarchy,” *Annals
of Mathematical Logic* 4 (1972), 229--308,
[DOI](https://doi.org/10.1016/0003-4843(72)90001-0).

### Forcing convention and the cited/local boundary

Retain v1.1's convention: `q<=p` means `q` is stronger, and the fixed tutorial
uses an **externally countable transitive set** `M models ZFC` with
`P in M`. A poset filter is upward closed toward weaker conditions and directed
toward common strengthenings. `M`-generic means meeting every dense subset of
`P` that belongs to `M`.

The generic-filter existence proof is local only because the dense sets in `M`
can be externally enumerated. It neither constructs a `V`-generic set inside
`V` nor proves the relative consistency theorem from `Con(ZFC)`.

The source's **forcing theorem** at 11012--11051 is cited from `Jech2003`,
pp. 201--224. Its clauses include recursive definability for each fixed
standard formula, equivalence to the external semantic relation, the truth
lemma, ZFC in `M[G]`, and preservation of ordinals. Keep `cited=Jech2003`; do
not add an annex item that proves only monotonicity and then label the forcing
theorem proved.

### `Add(omega,kappa)`, preservation, and nice names (`D-P7-012`, `N-a-042`)

Fix

`Add(omega,kappa)=Fn(kappa times omega,2,<omega)`

with finite conditions and reverse inclusion. The Delta-system argument above
proves ccc.

**Ccc preservation (ZFC).** If `P` is ccc, then forcing with `P` preserves all
ground-model cardinals and cofinalities. For a name for a function of ground
domain `lambda` into the ordinals, take for each coordinate a maximal antichain
deciding its value. Each antichain is countable, so all possible values lie in
a ground set of size at most `lambda*aleph_0`; this rules out a new cofinal map
of smaller domain and a cardinal collapse. A complete annex proof must split
the cofinality/cardinality consequences and treat finite/countable edge cases,
not merely cite “ccc.”

**Nice names for reals.** Every name for a subset of `omega` is equivalent to a
nice name determined by a sequence `<A_n:n in omega>` of antichains, where
conditions in `A_n` force `n` into the set. Under ccc every `A_n` is countable.
If `|P|=kappa`, the number of nice real names is at most
`(kappa^{aleph_0})^{aleph_0}=kappa^{aleph_0}`.

**Safe worked `not CH` instance.** Start from a model of GCH and let
`kappa=aleph_2`. `Add(omega,kappa)` is ccc and preserves `aleph_1,aleph_2`.
The coordinate generics give at least `kappa` distinct reals. GCH gives
`kappa^{aleph_0}=kappa`, so nice-name counting gives at most `kappa` reals.
Therefore the extension has `2^{aleph_0}=aleph_2`, hence `not CH`.

The hypothesis `kappa^{aleph_0}=kappa` is load-bearing for the exact upper
bound. “Add one Cohen real, therefore not CH” is false. The proof of this
worked cardinal calculation does not replace the cited Boolean-valued
relative-consistency theorem required by R-001.

### Forcing-poset catalog (A-067)

| forcing | exact convention | safe adds/preserves claim |
|---|---|---|
| Cohen | `Fn(kappa times omega,2,<omega)`, reverse inclusion | ccc; adds `kappa` coordinate Cohen reals; preserves ground cardinals/cofinalities; the exact continuum value needs the nice-name hypothesis above |
| random | the complete measure algebra of Borel subsets of `2^omega` modulo null sets (or positive Borel representatives ordered modulo null) | ccc; adds a random real; preserves ground cardinals/cofinalities; state the quotient convention before using Boolean values |
| collapse | for regular `kappa<lambda`, `Coll(kappa,lambda)` as partial functions `kappa->lambda` of size `<kappa`, reverse inclusion | `<kappa`-closed and adds a surjection `kappa->lambda`, collapsing ground cardinals in `[kappa,lambda]` to `kappa`; if `lambda^{<kappa}=lambda`, it has size `lambda` and is `lambda^+`-cc, so cardinals above `lambda` are preserved |

Collapse notation varies substantially among authors. A-067 must print its
definition, not rely on the bare symbol. Modern locators: `Jech2003`,
pp. 201--265; `Bell2005`, Chapters 2, 4, and 5.

### Boolean-valued models, products, iterations (`D-P7-011`, `N-a-068`)

For a complete Boolean algebra `B`, define the Boolean-valued hierarchy
`V^B` recursively and assign each membership-language formula with names a
truth value in `B`. The forcing/Boolean-valued theorem says that generic
quotient/evaluation recovers a two-valued forcing extension and transfers the
relevant ZFC truths. At this S ceiling this is a **cited statement**, not a
local proof of the atomic Boolean recursion, mixing lemma, fullness, truth
lemma, or ZFC preservation.

Products and finite-support iterations may be one-sentence pointers explaining
that they coordinate multiple forcing notions; proper forcing, countable
support iteration, PFA, and MM remain excluded beyond a pointer by `N-x-003`.
Use `Bell2005`, John L. Bell, *Set Theory: Boolean-Valued Models and
Independence Proofs*, 3rd ed., OUP, 2005, Chapters 1--6,
[publisher DOI](https://doi.org/10.1093/acprof:oso/9780198568520.001.0001),
and `Jech2003`. Do not fabricate a normal journal/book record for the
Scott--Solovay 1967 manuscript: it was unpublished/incomplete and Bell
describes that history.

### Symmetric extensions and permutation models (`N-a-043`)

At S level, define the method ingredients: a forcing/atom automorphism group,
a normal filter of subgroups, support, symmetric names/sets, and hereditary
symmetry. Then give one worked **ZFA** example:

1. Let `A` be a countably infinite set of atoms.
2. Let the full permutation group `Sym(A)` act on the cumulative hierarchy over
   the atoms.
3. Use the normal filter generated by pointwise stabilizers of finite subsets
   of `A`.
4. In the hereditarily symmetric model, every subset of `A` has finite support;
   the full symmetric action then makes it finite or cofinite.
5. Hence `A` is amorphous and cannot be well ordered, so AC fails.

This is the basic Fraenkel model in ZFA. The passage from permutation models
with atoms to a pure ZF independence result uses a transfer theorem (such as
Jech--Sochor) or a genuine symmetric forcing construction and must remain
cited. Primary historical source: `Fraenkel1922`, Abraham Fraenkel,
“Zu den Grundlagen der Cantor-Zermeloschen Mengenlehre,” *Mathematische
Annalen* 86 (1922), 230--237,
[DOI](https://doi.org/10.1007/BF01457986). Modern locator:
`Halbeisen2017`, pp. 191--219 and 339--368.

### Independence catalog and R-001 (A-066)

Every cell must say **relative consistency**, not unqualified truth/falsity.

| statement | positive side | negative side | safe method/status |
|---|---|---|---|
| CH | if ZFC is consistent, so is ZFC+CH | if ZFC is consistent, so is ZFC+not CH | positive side via L/Gödel; negative side via cited forcing/Boolean-valued theorem; final nonderivability is the local R-001 syntactic argument |
| GCH patterns | GCH holds in L | Easton realizes permitted patterns on regular cardinals | do not imply arbitrary singular patterns are free |
| Suslin hypothesis | MA at the relevant level implies SH | diamond in L yields a Suslin tree | iteration/inner-model results cited |
| AC over ZF | L supplies an inner model satisfying Choice | permutation/symmetric models give failure of Choice | ZFA worked example is local survey; pure-ZF transfer cited |

For the CH-positive source, add `Godel1938`, Kurt Gödel, “The Consistency of the
Axiom of Choice and of the Generalized Continuum-Hypothesis,” *PNAS* 24
(1938), 556--557, [DOI](https://doi.org/10.1073/pnas.24.12.556). The negative
side uses existing `Cohen1963` and `Jech2003`; v1.1 deliberately uses the
Boolean-valued discharge rather than the ctm tutorial.

### A-132 forcing-extension figure and A-164 symbols

The figure may show `M`, an external `M`-generic `G subseteq P`, names
`tau in M`, evaluations `tau^G`, and `M[G]={tau^G:tau in M}`. For the atomless
Cohen example it should mark `G notin M` and show check names for ground sets;
mere “nontriviality” of an arbitrary poset is not sufficient for that claim.
“Same ordinals” and “models ZFC” are cited forcing-theorem outputs, not
consequences of the drawing.

A-164 needs typed/scope-aware rows for at least `V_alpha`, `rank(x)`,
`L_alpha`, the poset `P`, a name `tau`/dotted name, evaluation `tau^G`, `M[G]`,
and the forcing relation. Register **one** forcing macro. If the body discusses
the source's external semantic relation and the cited recursive relation, mark
the distinction in prose or superscript, not by inventing unregistered forcing
glyphs. Evaluation is not membership and a dotted name is not its interpreted
object.

## Research package 6.6: hierarchy, reflection, absoluteness, and large cardinals

### Lévy hierarchy and elementary absoluteness (`D-P7-007`, `N-a-045`)

In the language of set theory, a quantifier is bounded when it has the form
`forall x in y` or `exists x in y`. `Delta_0=Sigma_0=Pi_0` consists of formulas
all of whose quantifiers are bounded. Inductively, `Sigma_{n+1}` begins with an
unbounded existential block over a `Pi_n` formula, and `Pi_{n+1}` is the dual;
close under the standard bounded quantifiers and Boolean normal forms. A
`Delta_n` classification means provable equivalence, in the declared base
theory, to both a `Sigma_n` and a `Pi_n` formula; it is not merely the literal
intersection of two strings.

If `M subseteq N` are transitive sets/classes containing the parameters, then
`Delta_0` formulas are absolute. Consequently `Sigma_1` formulas are upward
absolute (`M` true implies `N` true) and `Pi_1` formulas are downward absolute.
Transitivity and parameter membership are load-bearing; arbitrary elementary
or nonstandard models do not satisfy this bare rule.

Primary hierarchy source: `Levy1965Hierarchy`, Azriel Lévy, *A Hierarchy of
Formulas in Set Theory*, Memoirs AMS 57 (1965), 76 pp., especially Chapters
2--5 and 9, [AMS record](https://bookstore.ams.org/MEMO/1/57).

### Reflection

**Finite-family Lévy reflection.** For every finite set `Phi` of
membership-language formulas and every ordinal `beta`, there is an
`alpha>beta` such that for each `phi in Phi` and all parameters from `V_alpha`,

`V models phi(a_1,...,a_n) iff V_alpha models phi(a_1,...,a_n)`.

Equivalent presentations give a closed unbounded proper class of reflecting
ordinals for a fixed finite family. The theorem is a schema/metatheorem in the
ambient presentation. It never yields a set `V_alpha` elementary in `V` for
**all** formulas at once.

Primary: `Levy1960Reflection`, Azriel Lévy, “Principles of Reflection in
Axiomatic Set Theory,” *Fundamenta Mathematicae* 49 (1960), 1--10,
[DOI](https://doi.org/10.4064/fm-49-1-1-10) and
[EuDML](https://eudml.org/doc/213576). Do not confuse it with Lévy's different
1960 Pacific Journal paper “Axiom schemata of strong infinity ...”.

### Shoenfield absoluteness

A deliberately strong, claim-safe form is: if `M subseteq N` are transitive
models of ZFC with the same ordinals, and a real parameter `a` belongs to `M`,
then they agree on every boldface `Sigma^1_2(a)` sentence (and hence on its
`Pi^1_2(a)` dual). In particular, a set-forcing extension and its ground model
agree on such statements with ground-model real parameters, once the forcing
theorem supplies same ordinals.

Do not omit the parameter location or replace “same ordinals” by “same
omega.” Do not claim projective absoluteness at all higher levels from ZFC.
Primary: `Shoenfield1961Predicativity`, Joseph R. Shoenfield, “The Problem of
Predicativity,” in Bar-Hillel, Poznański, Rabin, and Robinson (eds.), *Essays on
the Foundations of Mathematics* (Magnes Press/North-Holland, 1961),
pp. 132--139. No verified DOI for the work was found; do not attach a review
DOI.

### Large-cardinal definitions (`D-P7-006`, `N-a-044`, A-065)

Declare “inaccessible” to mean **strongly inaccessible** in this part.

| rung | exact safe definition / characterization | chart caveat |
|---|---|---|
| inaccessible | uncountable, regular, strong-limit cardinal `kappa` | conditional existence; `V_kappa models ZFC` |
| Mahlo | use the stated convention: `kappa` is strongly inaccessible and the regular cardinals below it form a stationary set; equivalently here, the strongly inaccessible cardinals below it are stationary | definitions of weak/strong Mahlo vary, so the table must name its convention |
| weakly compact | uncountable `kappa` with `kappa -> (kappa)^2_2`; equivalently, `kappa` is inaccessible and every `kappa`-tree has a cofinal branch | tree property without inaccessibility is not the definition |
| measurable | uncountable `kappa` carrying a nonprincipal `kappa`-complete ultrafilter | the ultrapower is well founded; after collapse it yields `j:V->M` with critical point `kappa` |
| supercompact | for every `lambda>=kappa` there is `j:V->M` with `crit(j)=kappa`, `j(kappa)>lambda`, and `M^lambda subseteq M` | equivalently use a fine normal measure on `P_kappa(lambda)`, but do not mix the two definitions halfway |

The implication direction is

`supercompact -> measurable -> weakly compact -> Mahlo -> inaccessible`.

The chart is a hierarchy of conditional strengths. It must not say that ZFC
proves a member of any rung exists, and it must not use the arrows as complete
proofs of strict consistency separation. `Kanamori2003`, 2nd ed., is the
standard source: inaccessibility begins p. 16, measurability p. 22,
constructibility p. 28, compactness p. 36, embeddings p. 44, and
supercompactness p. 298; add
[Springer DOI](https://doi.org/10.1007/978-3-540-88867-3) to the existing key.

**Measurable ultrapower.** Given the ultrafilter `U`, form the ultrapower of
`V` by functions `kappa->V`. `kappa`-completeness (indeed countable
completeness for well-foundedness) rules out an infinite descending membership
sequence; the transitive collapse gives the elementary embedding. This can be
an explanatory derivation, but a complete class-ultrapower proof exceeds the S
ceiling unless every set/class coding issue is handled.

**Scott's theorem.** If a measurable cardinal exists, then `V != L`. Existing
primary key `Scott1961`, pp. 521--524. This is the first incompatibility with
`V=L` among the displayed ladder: inaccessible, Mahlo, and weakly compact
cardinals can occur in L. Do not broaden Scott's theorem to “no large
cardinals in L.”

**Ctm connection.** An inaccessible `kappa` gives a set model `V_kappa` of ZFC,
and standard downward/Mostowski arguments can then give a ctm externally. The
converse is not valid: a transitive model of ZFC need not be an ambient
`V_kappa`, and its height need not be an ambient inaccessible cardinal. This
is the correct connection to the R-001 warning.

### A-130 and A-134

A-130 may place conditional labels at stages `V_kappa`, with a legend saying
“if such a cardinal exists.” It should show why inaccessible closure supports
the ZFC operations but must not imply that an arbitrary large cardinal is a
set sitting *between* two ranks.

A-134's requested PRA-to-large-cardinal consistency ladder is a global Phase-6
artifact. The P6 large-cardinal table and hierarchy picture do not complete it.
Leave A-134 `open` unless the register phase is deliberately changed first.

## Research package 6.7: descriptive set theory (`D-P7-013`, `N-a-046`--`047`, A-068, A-135)

### Spaces and pointclasses

- A **Polish space** is separable and admits a complete compatible metric.
- `Sigma^0_1` is the class of open sets and `Pi^0_1` the closed sets. For
  countable `alpha>1`, `Sigma^0_alpha` is formed by countable unions of sets
  from lower `Pi^0_beta` levels, and `Pi^0_alpha` by complements/countable
  intersections. `Delta^0_alpha=Sigma^0_alpha intersect Pi^0_alpha`.
- A subset of a Polish space is analytic (`bold Sigma^1_1`) iff it is a
  continuous image of Baire space, equivalently the projection of a Borel
  subset of a product of Polish spaces. Coanalytic (`bold Pi^1_1`) means
  complement of analytic.
- Inductively, `bold Sigma^1_{n+1}` is obtained by projection from
  `bold Pi^1_n`, and `bold Pi^1_{n+1}` by complement; `bold Delta^1_n` is the
  intersection.

The boldface/borel levels here allow real parameters. `N-a-047` licenses only a
pointer to the lightface/effective hierarchy, where parameter-free recursive
codes and hyperarithmetic `Delta^1_1` replace arbitrary real parameters. Do not
build effective descriptive set theory beyond that pointer.

### Exact ZFC regularity boundary

**Suslin theorem.** A subset of a Polish space is Borel iff it is both analytic
and coanalytic.

**Analytic regularity.** Analytic sets have the Baire property and the perfect
set property; analytic subsets of standard Polish spaces are universally
measurable (with respect to completed sigma-finite Borel measures). In
particular every uncountable analytic set contains a nonempty perfect subset
and therefore has cardinality continuum.

These facts include Borel sets. They do **not** imply that every projective set
has these regularity properties in ZFC. A-068 should place ZFC checks on Borel
and analytic/coanalytic rows and reserve higher projective regularity for the
determinacy calibration.

Standard locators:

- existing `Kechris1995`, Sections 10--18 (Borel/standard Borel and the first
  analytic interface), Sections 25--29 (analytic representation, separation,
  and regularity), and Sections 37--38 (projective hierarchy/determinacy),
  [Springer DOI](https://doi.org/10.1007/978-1-4612-4190-4);
- existing `Moschovakis2009`, 2nd ed.; add
  [AMS DOI](https://doi.org/10.1090/surv/155);
- primary historical `Suslin1917`, pp. 88--91, supports attribution but not all
  modern Polish-space formulations.

### A-068 table and A-135 figure

The table should separate columns for definition, closure, ZFC regularity, and
determinacy/extra hypothesis. The figure should show:

- the transfinite Borel union/complement progression through countable levels;
- `Borel = bold Delta^1_1` at the boldface interface;
- projection arrows from `bold Pi^1_n` to `bold Sigma^1_{n+1}` and complement
  arrows between the paired classes;
- no inclusion/equality arrow asserting all projective classes collapse to
  Borel;
- a caption distinguishing boldface from the lightface pointer.

## Research package 6.8: games and determinacy (`D-P7-014`, `N-a-048`)

For `A subseteq omega^omega`, players alternately choose natural numbers,
forming `x in omega^omega`; Player I wins iff `x in A`. `Det(A)` says one of
the players has a winning strategy.

- **Gale--Stewart.** If `A` is open, the game is determined; by taking the
  complementary payoff/other player, closed games are determined as well.
- **Borel determinacy.** Every Borel payoff game on naturals is determined in
  ZFC (Martin 1975).
- **AD.** Every `A subseteq omega^omega` is determined. AD contradicts AC
  (in particular, it rules out a well-ordering of the reals); do not put AD
  inside the ZFC column.
- **Projective calibration.** A claim-safe Martin--Steel form is: if there are
  `n` Woodin cardinals below a measurable cardinal, then the relevant
  `Pi^1_{n+1}` games (and their complements) are determined. If for every
  finite `n` there are `n` Woodins below a measurable--for example infinitely
  many Woodins below one measurable--then projective determinacy follows.
  This is a sufficient large-cardinal hypothesis, not an asserted elementary
  equivalence.

Exact primary metadata:

- `GaleStewart1953`, David Gale and F. M. Stewart, “Infinite Games with Perfect
  Information,” in Kuhn and Tucker (eds.), *Contributions to the Theory of
  Games II*, Annals of Mathematics Studies 28, Princeton UP, 1953,
  pp. 245--266. A modern digitization has
  [chapter DOI](https://doi.org/10.1515/9781400881970-014); retain the original
  1953 publication year.
- `Martin1975`, Donald A. Martin, “Borel Determinacy,” *Annals of Mathematics*
  102 (1975), 363--371, [DOI](https://doi.org/10.2307/1971035).
- `MartinSteel1989`, Donald A. Martin and John R. Steel, “A Proof of Projective
  Determinacy,” *Journal of the American Mathematical Society* 2 (1989),
  71--125, [AMS DOI](https://doi.org/10.1090/S0894-0347-1989-0955605-X).
- `MycielskiSteinhaus1962`, Jan Mycielski and Hugo Steinhaus, “A Mathematical
  Axiom Contradicting the Axiom of Choice,” *Bulletin de l'Académie Polonaise
  des Sciences, Série des Sciences Mathématiques, Astronomiques et Physiques*
  10 (1962), 1--3. No verified DOI was found; do not invent one.

## Apparatus construction ledger

This section translates the research packages into visible completion tests.
It does not change the rows' live status.

### Tables A-058--A-068

- `A-058`: every source axiom/schema is a separate row; Separation and
  Replacement display formula metavariables and freshness/functionality side
  conditions. A table that says only “subset axiom” or “image axiom” is not at
  ceiling.
- `A-059`: six named systems, with columns for ontology/class sort, schema
  strength, Power Set/Replacement, Foundation, Choice, and comparison. The
  caption declares conventions for Z, NBG, and MK. NF is not placed on a
  linear ZFC strength ladder, and the current Lean/paper split is stated.
- `A-060`: definitions and law/failure rows for ordinal sum/product/power,
  right-limit continuity, monotonicity, noncommutativity, one-sided
  distributivity, and CNF.
- `A-061`: AC scope, aleph/beth, finite/infinite sum-product, exponentiation
  cautions, cofinality, regular/singular, König, Hausdorff, CH/GCH, and an
  Easton pointer. “All infinite arithmetic is max” fails the row.
- `A-062`: visually separate full-AC equivalents from BPI equivalents and
  restricted theorems. Tychonoff is qualified by separation assumptions.
- `A-063`: record exact choice strength per theorem, including the binary-tree
  ZF proof and unrestricted BPI compactness. “Uses choice” without naming the
  principle is not enough.
- `A-064`: rows for club/stationary/diagonal intersection/Fodor/Delta/Ramsey,
  diamond/square/MA; definitions and hypotheses accompany every implication.
- `A-065`: inaccessible, Mahlo, weakly compact, measurable, supercompact;
  definitions and conditional arrows; Scott's first `V=L` failure at
  measurable; no existence assertion.
- `A-066`: each independence row has both relative-consistency directions,
  method, base theory, and real citations. A bare “independent” cell fails the
  R-001 standard.
- `A-067`: define each forcing rather than rely on notation; chain condition,
  closure, adds, collapses, and preserves occupy distinct columns so a
  hypothesis cannot drift across them.
- `A-068`: pointclass definition/closure/ZFC regularity/determinacy hypothesis
  are separate columns. Do not put PD or AD in a ZFC-results column.

### Figures A-129--A-135

- `A-129`: ordered schematic through `epsilon_0`, with finite-tower supremum
  and CNF callouts.
- `A-130`: `V` recursion and exact rank axis; conditional inaccessible stages.
- `A-131`: `L` recursion inside `V`, parameters in `Def`, condensation callout,
  `V=L` contrast; no implication that L is set-sized.
- `A-132`: typed arrows `tau -> tau^G`, check-name ground embedding, generic
  filter, and extension. For the atomless Cohen example, `G notin M`; do not
  assert this merely from the word “nontrivial” for an arbitrary poset.
- `A-133`: verified arrows `AC -> DC -> AC_omega -> AC_omega^fin` and
  `AC -> BPI`; sourced non-reversals; BPI/AC_omega relationship is not guessed
  from layout.
- `A-134`: Phase 6 only. No Phase-4 completion mark.
- `A-135`: Borel transfinite levels, analytic/coanalytic projection-complement
  interface, projective iterations, and explicit boldface legend.

### A-164 and A-186

`A-164` requires registry records rather than locally invented notation. For
each symbol, record glyph/macro, type/standing, meaning, scope, precedence, and
first definition. The forcing glyph must be the single registered macro
required by the conventions; `|x|` remains cardinality only, and domains use
the registered `dom` macro.

For `A-186`, the P6 further-reading list can be short but should be annotated:

- `Jech2003`: comprehensive modern set theory; use the 3rd millennium edition
  and its chapter/page locators below.
- `Kunen2011`: broad independent second reference for forcing and combinatorics.
- `Halbeisen2017`: AC, weak choice, permutation/symmetric models.
- `Bell2005`: Boolean-valued models and independence proofs.
- `Kanamori2003`: large-cardinal history and exact hierarchy.
- `Kechris1995`: classical boldface descriptive set theory.
- `Moschovakis2009`: descriptive set theory, games, and effective bridge.
- `Shelah1994Cardinal`: PCF/cardinal-arithmetic pointer only.

An unannotated dump of all bibliography keys does not satisfy the navigation
purpose.

## HOD and register-scope ambiguity

`HOD` appears in the architecture prose of `spec/gap-analysis.tex` but not in
any live P6 row listed above, and no HOD development exists in frozen v1.1.
That prose mention is not authority to create a new entry under the campaign's
spec-first rule. Safe options are:

1. omit HOD and record the no-row ambiguity in execution notes; or
2. give a single navigational phrase inside an already licensed constructibility
   pointer, without claiming a row complete; or
3. amend the appropriate depth/new-content row before adding a definition or
   theorem.

Do not silently use `HOD` to fill `N-a-067`; that row specifically requires L,
condensation, GCH in L, reflection, and a fine-structure pointer.

## Claim-safe bibliography-key ledger

No bibliography file is edited here. “Existing” means the key was present in
`handbook/bib/handbook.bib` when checked. “New” means the finalizer needs a
real intake record before the handbook cites it.

### Existing keys that are already usable

| key | principal licensed use | note |
|---|---|---|
| `Jech2003` | axioms, ordinals/cardinals, choice, stationarity, forcing, L, large cardinals | existing complete record; add DOI/URL only as enrichment, not a duplicate key |
| `Kunen2011` | independent modern set-theory cross-check | existing record; publisher is College Publications |
| `Jech1973Choice` | AC equivalents and symmetric/permutation background | existing complete monograph record |
| `HowardRubin1998` | exact weak-choice implication/nonimplication catalog | existing complete record, DOI `10.1090/surv/059` |
| `HalpernLevy1971` | BPI does not imply AC | existing complete AMS record |
| `Konig1905` | König cardinal theorem | existing primary record |
| `Easton1970` | powers of regular cardinals | existing DOI `10.1016/0003-4843(70)90012-4` |
| `Fodor1956` | pressing-down lemma | existing primary record; add archive URL if desired |
| `Shanin1946` | Delta-system lemma | existing primary record |
| `Ramsey1930` | infinite Ramsey theorem | existing DOI |
| `ErdosRado1956` | partition calculus | existing DOI |
| `Cohen1963` | CH independence attribution | existing DOI; not by itself the full modern forcing theorem citation |
| `Ulam1930` | measure/large-cardinal history | existing record |
| `Scott1961` | measurable implies `V != L` | existing primary record |
| `Kanamori2003` | large-cardinal ladder | existing record; enrich with DOI below |
| `Suslin1917` | analytic-set historical attribution | existing primary record |
| `Kechris1995` | classical DST | existing complete DOI record |
| `Moschovakis2009` | DST/games/effective bridge | existing record; enrich with DOI below |
| `Mendelson1997` | NBG/MK comparison | existing 4th-edition record, Chapter 4 |

### Existing records that need enrichment, not replacement

| key | exact enrichment |
|---|---|
| `Jech2003` | DOI `10.1007/3-540-44761-X`; [Springer](https://link.springer.com/book/10.1007/3-540-44761-X); 3rd millennium ed., xiv+772 pp. Useful locators: axioms 3--15; ordinals 17--26; cardinals 27--35; AC/arithmetic 47--61; Boolean/filter 73--89; stationary 91--105; combinatorics 107--123; measurable 125--138; Borel/analytic 139--153; models 155--172; L 175--200; forcing 201--224; forcing applications 225--265; iterations/MA 267--283; large cardinals 285--309. |
| `Kanamori2003` | DOI `10.1007/978-3-540-88867-3`; [Springer](https://doi.org/10.1007/978-3-540-88867-3). |
| `Moschovakis2009` | DOI `10.1090/surv/155`; [AMS](https://doi.org/10.1090/surv/155). |
| `Fodor1956` | stable archive URL `http://acta.bibl.u-szeged.hu/id/eprint/13806`. |
| `Keisler1962` | replace stub metadata with H. Jerome Keisler, “Some Applications of the Theory of Models to Set Theory,” in Nagel, Suppes, and Tarski (eds.), *Logic, Methodology and Philosophy of Science: Proceedings of the 1960 International Congress*, Stanford UP, 1962, pp. 80--86; no verified work DOI. |

### New keys with verified metadata

| proposed key | exact record and stable link | supports |
|---|---|---|
| `Halbeisen2017` | Lorenz J. Halbeisen, *Combinatorial Set Theory: With a Gentle Introduction to Forcing*, 2nd ed., Springer, 2017, DOI [10.1007/978-3-319-60231-8](https://doi.org/10.1007/978-3-319-60231-8). Locators: Ramsey 87--102; cardinal relations in ZF 103--134; forms of choice 135--175; atoms 191--219; MA 323--338; forcing 339--368. | choice, permutation models, forcing |
| `Bell2005` | John L. Bell, *Set Theory: Boolean-Valued Models and Independence Proofs*, 3rd ed., Oxford UP, 2005, DOI [10.1093/acprof:oso/9780198568520.001.0001](https://doi.org/10.1093/acprof:oso/9780198568520.001.0001). | Boolean-valued models, forcing, collapse, iterations |
| `Hausdorff1904` | Felix Hausdorff, “Der Potenzbegriff in der Mengenlehre,” *Jahresbericht der DMV* 13 (1904), 569--571; [HCM bibliography](https://www.mathematics.uni-bonn.de/hcm/felix-hausdorff/schriftenverzeichnis). | successor recursion |
| `Silver1975` | Jack Silver, “On the Singular Cardinals Problem,” in *Proceedings ICM Vancouver 1974*, vol. 1, Canadian Mathematical Congress, 1975, 265--268; [IMU PDF](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1974.1/ICM1974.1.ocr.pdf). | Silver theorem |
| `Shelah1994Cardinal` | Saharon Shelah, *Cardinal Arithmetic*, Oxford Logic Guides 29, Clarendon/OUP, 1994, DOI [10.1093/oso/9780198537854.001.0001](https://doi.org/10.1093/oso/9780198537854.001.0001). | PCF pointer |
| `Konig1927Infinity` | Dénes Kőnig, “Über eine Schlussweise aus dem Endlichen ins Unendliche,” *Acta Sci. Math. (Szeged)* 3 (1927), 121--130; [archive](https://acta.bibl.u-szeged.hu/13338/). | infinity lemma |
| `Kurepa1935` | Đuro Kurepa, “Ensembles ordonnés et ramifiés,” *Publications de l'Institut Mathématique* 4 (1935), 1--138; [EuDML](http://eudml.org/doc/253633). | Aronszajn/Suslin tree history |
| `Todorcevic1984Trees` | Stevo Todorcevic, “Trees and Linearly Ordered Sets,” in Kunen and Vaughan (eds.), *Handbook of Set-Theoretic Topology*, North-Holland, 1984, 235--293, DOI [10.1016/B978-0-444-86580-9.50009-4](https://doi.org/10.1016/B978-0-444-86580-9.50009-4). | tree survey |
| `Jensen1972FineStructure` | R. Björn Jensen, “The Fine Structure of the Constructible Hierarchy,” *Annals of Mathematical Logic* 4 (1972), 229--308, DOI [10.1016/0003-4843(72)90001-0](https://doi.org/10.1016/0003-4843(72)90001-0). | L/fine-structure pointer, diamond/square context |
| `MartinSolovay1970` | Donald A. Martin and Robert M. Solovay, “Internal Cohen Extensions,” *Annals of Mathematical Logic* 2 (1970), 143--178, DOI [10.1016/0003-4843(70)90009-4](https://doi.org/10.1016/0003-4843(70)90009-4). | forcing/MA historical support |
| `Levy1960Reflection` | Azriel Lévy, “Principles of Reflection in Axiomatic Set Theory,” *Fundamenta Mathematicae* 49 (1960), 1--10, DOI [10.4064/fm-49-1-1-10](https://doi.org/10.4064/fm-49-1-1-10). | reflection |
| `Levy1965Hierarchy` | Azriel Lévy, *A Hierarchy of Formulas in Set Theory*, Memoirs AMS 57, 1965, 76 pp.; [AMS](https://bookstore.ams.org/MEMO/1/57). | Lévy hierarchy/absoluteness |
| `Shoenfield1961Predicativity` | Joseph R. Shoenfield, “The Problem of Predicativity,” in Bar-Hillel et al. (eds.), *Essays on the Foundations of Mathematics*, Magnes/North-Holland, 1961, 132--139. | Shoenfield absoluteness; no work DOI verified |
| `Fraenkel1922` | Abraham Fraenkel, “Zu den Grundlagen der Cantor-Zermeloschen Mengenlehre,” *Mathematische Annalen* 86 (1922), 230--237, DOI [10.1007/BF01457986](https://doi.org/10.1007/BF01457986). | permutation-model history |
| `GaleStewart1953` | David Gale and F. M. Stewart, “Infinite Games with Perfect Information,” in Kuhn and Tucker (eds.), *Contributions to the Theory of Games II*, Annals of Mathematics Studies 28, Princeton UP, 1953, 245--266; modern chapter DOI [10.1515/9781400881970-014](https://doi.org/10.1515/9781400881970-014). | open/closed determinacy |
| `Martin1975` | Donald A. Martin, “Borel Determinacy,” *Annals of Mathematics* (2) 102 (1975), 363--371, DOI [10.2307/1971035](https://doi.org/10.2307/1971035). | Borel determinacy |
| `MartinSteel1989` | Donald A. Martin and John R. Steel, “A Proof of Projective Determinacy,” *JAMS* 2 (1989), 71--125, DOI [10.1090/S0894-0347-1989-0955605-X](https://doi.org/10.1090/S0894-0347-1989-0955605-X). | PD calibration |
| `MycielskiSteinhaus1962` | Jan Mycielski and Hugo Steinhaus, “A Mathematical Axiom Contradicting the Axiom of Choice,” *Bulletin de l'Académie Polonaise des Sciences, Série des Sciences Mathématiques, Astronomiques et Physiques* 10 (1962), 1--3. | AD/AC historical claim; no DOI verified |
| `Godel1938` | Kurt Gödel, “The Consistency of the Axiom of Choice and of the Generalized Continuum-Hypothesis,” *PNAS* 24 (1938), 556--557, DOI [10.1073/pnas.24.12.556](https://doi.org/10.1073/pnas.24.12.556). | L/CH/GCH relative consistency |
| `Quine1937` | W. V. Quine, “New Foundations for Mathematical Logic,” *American Mathematical Monthly* 44 (1937), 70--80, DOI [10.1080/00029890.1937.11987928](https://doi.org/10.1080/00029890.1937.11987928). | NF definition/history |
| `Specker1953` | Ernst Specker, “The Axiom of Choice in Quine's New Foundations for Mathematical Logic,” *PNAS* 39 (1953), 972--975, DOI [10.1073/pnas.39.9.972](https://doi.org/10.1073/pnas.39.9.972). | NF refutes AC |
| `Wilshaw2025ConNF` | Sky Wilshaw, *New Foundations is consistent*, 18 June 2025, 61 pp.; [project PDF](https://leanprover-community.github.io/con-nf/print/print.pdf), [formalization site](https://leanprover-community.github.io/con-nf/). | current NF consistency status with formal/paper split |
| `Barwise1975` | Jon Barwise, *Admissible Sets and Structures: An Approach to Definability Theory*, Perspectives in Mathematical Logic 7, Springer, 1975, xiii+394 pp., ISBN 978-3-540-07451-9. | KP/admissible sets; do not attach the 2017 reissue DOI to the 1975 edition |
| `Kelley1975` | John L. Kelley, *General Topology*, GTM 27, Springer New York, 1975 reprint of 1955 original, xiv+298 pp., ISBN 978-0-387-90125-1, Appendix “Elementary Set Theory” p. 250ff.; [Springer](https://link.springer.com/book/9780387901251). | MK/KM source |
| `HowardRubin1996BPI` | Paul E. Howard and Jean E. Rubin, “The Boolean Prime Ideal Theorem Plus Countable Choice Do Not Imply Dependent Choice,” *Mathematical Logic Quarterly* 42 (1996), 410--420, DOI [10.1002/malq.19960420133](https://doi.org/10.1002/malq.19960420133). | A-133 non-reversal |
| `Solovay1970Measurable` | Robert M. Solovay, “A Model of Set-Theory in Which Every Set of Reals Is Lebesgue Measurable,” *Annals of Mathematics* (2) 92 (1970), 1--56, DOI [10.2307/1970696](https://doi.org/10.2307/1970696). | conditional DC-without-free-ultrafilter model context |

### Unsafe or misleading bibliography moves

1. Do not cite a DOI belonging to a review as the DOI of a book. In
   particular, `10.2307/2270064` is Shoenfield's JSL review of Morse's *A
   Theory of Sets*, not the book's DOI.
2. Do not attach Lévy's Pacific Journal DOI
   `10.2140/pjm.1960.10.223` to “Principles of Reflection”; it identifies a
   different Lévy paper.
3. Do not attach a JSTOR or review DOI to Shoenfield's 1961 chapter; no work DOI
   was verified.
4. Do not fabricate publication data for the 1967 Scott--Solovay manuscript.
   Cite Bell/Jech, or create an explicitly `@unpublished` record only if the
   finalizer has a stable manuscript copy and needs the historical pointer.
5. Do not use `Cohen1963` as though six pages contain the handbook's complete
   forcing theorem and every preservation proof.
6. Do not cite `Fraenkel1922` alone for a pure-ZF symmetric-extension theorem;
   it supports the historical/permutation-model side, while transfer requires
   a modern source.
7. Do not use the current NF formalization to claim that the English paper has
   been machine-checked line-by-line or independently peer reviewed.

## Adversarial overclaim checklist

Before any P6 row is marked done, search explicitly for these failure modes:

1. one Cohen real presented as a proof of `not CH`;
2. ctm existence treated as equivalent to `Con(ZFC)` or to an inaccessible;
3. the cited forcing theorem upgraded because ccc was locally proved;
4. recursive forcing and external semantic forcing conflated;
5. BPI printed in the full-AC equivalence block;
6. arbitrary cardinal trichotomy called a ZF theorem;
7. arbitrary finitely branching-tree König called choice-free without binary
   coding/canonical choice;
8. classical fan compactness conflated with every intuitionistic fan theorem;
9. Hausdorff recursion stated at exponent zero;
10. Easton applied to singular cardinals or without the cofinality constraint;
11. Silver stated at countable cofinality;
12. Fodor missing regularity, uncountability, stationarity, or regressiveness;
13. generalized Delta-system lemma stated with no cardinal hypotheses;
14. Erdos--Rado arrow with an off-by-one beth or exponent;
15. square missing the no-thread clause;
16. MA consistency “proved” despite iterations being pointer-only;
17. reflection printed as `V_alpha \prec V` for all formulas;
18. Shoenfield missing transitivity/same-ordinals/parameter conditions;
19. condensation applied to arbitrary subsets of `L_alpha`;
20. HOD expanded despite having no row;
21. large-cardinal existence asserted by ZFC or chart arrows described as
    proved strictness;
22. weak compactness reduced to tree property without inaccessibility;
23. all projective sets declared regular/determined in ZFC;
24. Martin--Steel described as an unconditional equivalence;
25. NF still labelled consistency-open, or the TTT-to-NF surface overstated;
26. A-134 marked done in Phase 4;
27. symbol registry gains a second forcing glyph or uses `|M|` for a domain;
28. an apparatus figure silently supplies a theorem status that no entry or
    citation supports.

## Coverage audit

The following IDs occur substantively in this ledger:

- Depth (19): `D-P1-001`, `D-P1-002`, `D-P1-003`, `D-P1-004`, `D-P1-006`,
  `D-P7-001`, `D-P7-002`, `D-P7-003`, `D-P7-004`, `D-P7-005`, `D-P7-006`,
  `D-P7-007`, `D-P7-008`, `D-P7-009`, `D-P7-010`, `D-P7-011`, `D-P7-012`,
  `D-P7-013`, `D-P7-014`.
- In-scope new content (17): `N-a-035`, `N-a-036`, `N-a-037`, `N-a-038`,
  `N-a-039`, `N-a-040`, `N-a-041`, `N-a-042`, `N-a-043`, `N-a-044`,
  `N-a-045`, `N-a-046`, `N-a-047`, `N-a-048`, `N-a-066`, `N-a-067`,
  `N-a-068`.
- Explicit exclusions (3): `N-x-003`, `N-x-004`, `N-x-005`.
- Apparatus (20): `A-058`, `A-059`, `A-060`, `A-061`, `A-062`, `A-063`,
  `A-064`, `A-065`, `A-066`, `A-067`, `A-068`, `A-129`, `A-130`, `A-131`,
  `A-132`, `A-133`, `A-134`, `A-135`, `A-164`, `A-186`.
- Defect preservation: `R-001`.

This coverage is an evidence map only. Register rows remain `open` until the
actual body/annex/apparatus exists at its ceiling, compiles, passes the
conventions checker, and survives the required adversarial verification.

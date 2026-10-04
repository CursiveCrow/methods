# Round 1 blind opening — correctness/model-theory topic specialist

## Verdict

**Do not admit Part III in its present source/content state.** I record two
blockers and six must-fix findings.  The exact inherited model-theory sequence
is, on the points checked below, mathematically coherent.  The blockers arise
in reader-routed editorial material: accepted pages still declare themselves
OPEN/unadmitted, and the local positive-formula grammar makes the stated Lyndon
theorem false at the bottom formula.

I read the charter before the artifact and did not read any other Part III
seat's transcript.  I reviewed the complete live graph rooted at
`handbook/parts/p03.tex` and `handbook/annex/p03.tex`: both roots, all twenty-one
source wrappers, all twenty-one wrapper-selected inherited units, six routed
body additions, and two routed annex additions (fifty-two reachable files in
all).  This was a read-only source/content review; I made no manuscript,
control, or test edit and did not build the book.

## Findings

### F1 — Reader-routed sections explicitly remain OPEN and unadmitted

- **Author:** correctness/model-theory topic specialist
- **Severity:** blocker
- **Criterion:** no OPEN, unadmitted, owed, pointer-only, alias, or internal
  workflow token in an accepted reader section
- **Location:**
  - `handbook/parts/p03/maps-elementarity-supplement.tex:5-7,14`
  - `handbook/parts/p03/types-ultraproducts-supplement.tex:4-8`
  - `handbook/annex/p03/types-ultraproducts-supplement.tex:2-4`
  - `handbook/parts/p03/qe-categoricity-games-supplement.tex:3-8`
  - `handbook/annex/p03/qe-categoricity-games-supplement.tex:3-6`
- **Claim and evidence:** These are rendered reader notes, not source comments.
  They say, respectively, that A-162 is OPEN; D-P4-003 and D-P4-004 remain OPEN
  and unadmitted; D-P4-004 is not admitted or closed by its annex proof; and the
  retained QE body and R-030 annex are OPEN/unadmitted and close no obligation.
  Thus A-162, D-P4-003, D-P4-004, and R-030 are both exposed as internal
  workflow identifiers and affirmatively undisposed construction obligations.
  The notes are admirably candid, but candor does not turn an unadmitted item
  into accepted reader content.
- **Concrete harm:** The Part cannot satisfy the charter's admission invariant
  while its own reader route denies admission and closure.  Deleting only the
  words `OPEN` or `unadmitted` would hide rather than settle the debt.
- **Exact correction:** For each affected unit, choose one of the two honest
  dispositions.  Either (1) complete the governing apparatus/depth/repair
  obligation, record its admission in the controlling register, and replace
  the workflow note with ordinary reader-facing attribution and scope; or (2)
  remove that body/annex unit from `handbook/parts/p03.tex` or
  `handbook/annex/p03.tex` until the obligation is admitted.  Keep paired body
  and annex dispositions reciprocal.  Do not close any of the four identifiers
  merely because the current prose or proof is present.
- **Status:** open

### F2 — The symbol lookup uses type-space and ultraproduct machinery before definition

- **Author:** correctness/model-theory topic specialist
- **Severity:** must-fix
- **Criterion:** definition before use; typed signatures and parameters
- **Location:**
  - routing order: `handbook/parts/p03.tex:17-18`
  - forward entries: `handbook/parts/p03/maps-elementarity-supplement.tex:37-45`
  - first exact definition of `S_n(T)` and its topology:
    `handbook/restoration/inherited-06510-06629.tex:30-45`
  - first exact ultraproduct definition:
    `handbook/restoration/inherited-06942-07134.tex:19` and following
- **Claim and evidence:** The supplement is routed immediately before the
  Types, Saturation, and Ultraproducts chapter.  Its lookup nevertheless calls
  `S_n(T)` a space of complete types with its Stone topology and displays the
  quotient notation for an ultraproduct.  The table supplies no definition of
  complete type, the basic clopens/topology, the product domain, or the
  ultrafilter equivalence relation.  Those exact definitions occur only after
  the table.
- **Concrete harm:** At first occurrence neither displayed object has yet been
  constructed.  A forward cross-reference tells the reader where a future
  definition will be; it does not make the current occurrence typed or satisfy
  definition-before-use.
- **Exact correction:** Either move the entire symbol supplement after the
  restored Types, Saturation, and Ultraproducts chapter (after the input now at
  `handbook/parts/p03.tex:27`), or split it: retain only already-defined map,
  diagram, and isomorphism entries at the present position, and place the
  `S_n(T)` and ultraproduct rows immediately after their exact definitions.
  Do not duplicate abridged definitions in the lookup.
- **Status:** open

### F3 — The stated positive grammar cannot express falsity, so the Lyndon biconditional is false

- **Author:** correctness/model-theory topic specialist
- **Severity:** blocker
- **Criterion:** internal consistency of a definition with the exact strength
  of the theorem that uses it
- **Location:**
  - local grammar:
    `handbook/parts/p03/preservation-abstract-logic.tex:73-78`
  - Lyndon statement:
    `handbook/parts/p03/preservation-abstract-logic.tex:114-118`
  - matching table row:
    `handbook/parts/p03/preservation-abstract-logic.tex:151-155`
  - governing first-order grammar, where `\bottom` is a formula:
    `handbook/restoration/inherited-03105-03165.tex:4-20`
- **Claim and evidence:** The handbook defines a positive formula as one built
  from atomic formulas using only conjunction, disjunction, universal
  quantification, and existential quantification.  It omits `\bottom`, although
  the governing formula grammar expressly includes `\bottom`.  The subsequent
  theorem quantifies over every first-order formula and says preservation under
  surjective homomorphisms is equivalent to definability by that positive
  grammar.  The standard Lyndon result cited locally as `Lyndon1959` is indeed a
  surjective-homomorphism/positive-formula characterization; see also Benjamin
  Rossman, [*Homomorphism Preservation Theorems*](https://users.cs.duke.edu/~br148/hpt-jacm.pdf).
- **Minimal counterexample:** Work in the equality-only relational signature
  and take the formula `\bottom`.  It is preserved under every surjective
  homomorphism, vacuously: its preservation implication never has a true
  antecedent.  But in the one-element equality structure every equality atom
  is true under every assignment.  A structural induction through precisely
  the four allowed constructors shows that every formula in the manuscript's
  positive grammar is true there.  Hence no formula of that grammar is
  equivalent to `\bottom` over all structures.
- **Exact correction:** Add `\bottom` as a base case of both the positive and
  existential-positive grammars at lines 73-78, and update the Lyndon table row
  at lines 151-155 to reflect the corrected grammar.  Then retain the theorem.
  Equivalently, the theorem would have to exclude unsatisfiable formulas, but
  that would be a nonstandard and unnecessarily weaker statement.
- **Status:** open

### F4 — Robinson's common and union signatures are not defined without symbol compatibility

- **Author:** correctness/model-theory topic specialist
- **Severity:** must-fix
- **Criterion:** signatures/types/parameters; exact hypotheses
- **Location:**
  - `handbook/parts/p03/preservation-abstract-logic.tex:18-32`
  - registered signature type:
    `handbook/restoration/inherited-03038-03104.tex:9-31`
- **Claim and evidence:** A registered first-order signature is a tuple of
  function symbols, relation symbols, and two arity maps.  The Robinson section
  simply writes `\Lang_0=\Lang_1\cap\Lang_2` and later
  `\Lang_1\cup\Lang_2`.  It does not require a token common to the two
  signatures to have the same syntactic kind and arity.  Set intersection or
  union notation on the displayed signature tuples does not manufacture
  compatible arity maps.
- **Minimal counterexample:** Let the token `f` be a unary function symbol in
  `\Lang_1` and a binary function symbol in `\Lang_2` (or a function symbol in
  one and a relation symbol in the other).  Take both theories empty.  They are
  consistent, but neither the asserted common signature nor the union language
  has a well-defined kind/arity assignment for `f`; consequently
  `T_1\cup T_2` is not a theory in the claimed signature.
- **Exact correction:** Before defining `\Lang_0`, require that every symbol on
  the overlap has the same function/relation kind and the same arity in both
  signatures.  Define `\Lang_0` as the common restriction with those inherited
  arities, and define `\Lang_1\cup\Lang_2` by the compatible unions of the two
  symbol sets and arity maps.  The theorem can then keep its present
  consequence-agreement hypothesis.
- **Status:** open

### F5 — The Boolean-algebra catalog uses reserved logical connectives as function symbols

- **Author:** correctness/model-theory topic specialist
- **Severity:** must-fix
- **Criterion:** signature validity and notation discipline
- **Location:**
  - theory table:
    `handbook/parts/p03/qe-categoricity-games-supplement.tex:63`
  - QE catalog:
    `handbook/parts/p03/qe-categoricity-games-supplement.tex:106`
  - reserved-token rule:
    `handbook/restoration/inherited-03038-03104.tex:23-31`
- **Claim and evidence:** Both Boolean-algebra rows declare the signature
  `\{0,1,\wedge,\vee,\neg\}`.  In a Boolean-algebra signature the last three
  entries must be two binary function symbols and one unary function symbol.
  The handbook's governing signature definition, however, reserves
  `\neg,\land,\lor` as logical tokens and requires the nonlogical symbol sets
  to be disjoint from them.  Merely placing the logical glyphs in braces does
  not give them a second, legal standing as function symbols.
- **Concrete harm:** The two catalog rows do not denote a first-order signature
  under the handbook's own syntax, so the literal QE/model-completeness claims
  are not typed as written.
- **Exact correction:** Declare fresh nonlogical Boolean-operation symbols and
  their arities once—for example two fresh binary symbols for meet and join and
  one fresh unary complement symbol, together with the two nullary symbols—and
  use exactly those symbols in both rows.  The new glyphs must be distinct from
  the registered logical tokens; do not overload `\land`, `\lor`, or `\neg`.
- **Status:** open

### F6 — The routed DLO annex repeats an inherited theorem that already has a complete inline proof

- **Author:** correctness/model-theory topic specialist
- **Severity:** must-fix
- **Criterion:** editorial additions must be nonduplicative; annex reciprocity
- **Location:**
  - annex route: `handbook/annex/p03.tex:4`
  - duplicate annex item:
    `handbook/annex/p03/qe-categoricity-games-supplement.tex:3-17`
  - exact inherited theorem, complete-proof status, and inline proof:
    `handbook/restoration/inherited-07295-07468.tex:108-131`
- **Claim and evidence:** The exact inherited body states countable
  categoricity of DLO, marks it `Status: complete proof`, and immediately gives
  the full alternating back-and-forth proof.  The routed editorial annex then
  attaches another back-and-forth proof to that same inherited theorem label,
  while calling itself a retained historical addition.  There is no distinct
  reader-routed body result for this annex item to prove.
- **Concrete harm:** The annex is redundant, breaks the intended one-body-item
  to one-annex-proof accounting, and obscures rather than clarifies which proof
  belongs to the exact source.  The inherited artifact cannot be altered to
  create a need for the duplicate.
- **Exact correction:** Remove the input at `handbook/annex/p03.tex:4` from the
  accepted reader route and retire or leave unreachable the duplicate annex
  unit according to the repository's preservation policy.  Keep the exact
  inherited theorem and inline proof unchanged.  Do not relabel the duplicate
  as a second proof obligation.
- **Status:** open

### F7 — The computable-model-theory tail is expressly only a pointer

- **Author:** correctness/model-theory topic specialist
- **Severity:** must-fix
- **Criterion:** no pointer-only or owed topic in an accepted reader section;
  completeness for declared scope
- **Location:** `handbook/parts/p03/finite-model-theory.tex:128-131` (the source
  comment at line 2 identifies the same material as the D-P4-011 stub)
- **Claim and evidence:** After defining computable presentation and degree
  spectrum, the chapter merely lists computable dimension, relative
  categoricity, degree spectra, and complexity of isomorphism types, and then
  explicitly says, "This pointer asserts no family-wide ... theorem."  The
  warning correctly avoids an overclaim, but it also confirms that the routed
  material is a pointer-only stub rather than an admitted treatment.  The sole
  citation is `AshKnight2000` at line 124.
- **Concrete harm:** A named depth-row topic is advertised without a stated
  result, exact hypotheses, proof status, or public destination.  The reader is
  left with the construction debt that the charter forbids.
- **Exact correction:** Either remove the pointer and its D-P4-011 claim from
  the accepted Part III route, or supply the owed artifact at its declared
  owner: fix the class of copies and oracle convention, state the exact sourced
  result being admitted, and give its proof/citation status.  Do not invent a
  family-wide theorem or a new technical name merely to fill the row.
- **Status:** open

### F8 — Three chair-authored survey chapters are not visibly marked as editorial additions

- **Author:** correctness/model-theory topic specialist
- **Severity:** must-fix
- **Criterion:** editorial additions must be visibly distinct from inherited
  source and accurately attributed
- **Location:**
  - routes: `handbook/parts/p03.tex:36-38`
  - classification opening:
    `handbook/parts/p03/classification-theory.tex:1-10`
  - finite-model opening:
    `handbook/parts/p03/finite-model-theory.tex:1-14`
  - preservation/abstract-logic opening:
    `handbook/parts/p03/preservation-abstract-logic.tex:1-13`
- **Claim and evidence:** The three files are routed directly after the exact
  restored sequence.  Their editorial/Phase-4 standing appears only in `%`
  source comments, which are invisible to the reader.  Their rendered openings
  read as ordinary handbook chapters and contain no attribution/nonreplacement
  note comparable to the rendered notes in the other supplements.
- **Concrete harm:** A reader cannot tell where exact inherited source ends and
  chair-authored survey material begins.  This fails the charter's visible
  distinction even where the mathematical claims are individually cited.
- **Exact correction:** Put a rendered, reader-facing editorial attribution and
  nonreplacement/scope note at the start of each of the three chapters, or
  route them under one rendered editorial-supplement preface that unambiguously
  governs all three.  Preserve theorem-level citations; the provenance note is
  not a substitute for them.
- **Status:** open

## Structural checks

- The twenty-one `scope-SRC-*` wrappers are one-to-one with twenty-one
  `inherited-*` targets.  Each wrapper's declared interval matches its target,
  and each inherited target's line count matches the closed interval length.
- Recursive reachability from the two roots produced fifty-two files: two
  roots, twenty-one wrappers, twenty-one inherited units, six body additions,
  and two annex additions.
- Reachable labels were unique in this graph.
- The one legitimate reachable `proved=annex` declaration—the compactness-via-
  ultraproducts supplement—has its matching annex item.  The additional DLO
  annex item is the unpaired duplicate recorded as F6.
- Reader-visible construction-status searching was followed by direct reading
  of every hit.  F1 and F7 account for the live OPEN/unadmitted/pointer debt;
  the `OPEN` lines in `handbook/parts/p03.tex:10-16,32-34` are source comments
  and therefore are not themselves reader-visible, although they corroborate
  the corresponding routed status.

## Four-lot coverage

| Lot | Checked clean | Findings | Not checked in this round |
|---|---|---|---|
| 1. Maps, substructures, elementary embeddings, symbol supplement | Read all eight exact wrappers/units from `06049-06069` through `06494-06509`.  Checked map kinds and composition, term preservation, substructures, isomorphism invariance, embedding images, elementary maps/substructures, Tarski–Vaught, diagram tests, and the elementary-chain proof.  No mathematical defect found in those exact units. | F1, F2 | Build/rendering and historical-source hash provenance. |
| 2. Types, ultrafilters, ultraproducts, Los, saturation, proof supplements | Read all ten exact wrappers/units from `06510-06629` through `07135-07149`, plus the routed body and annex supplement.  Checked type parameters/completeness, Stone topology, saturation and homogeneity, ultrafilter existence, ultraproduct well-definedness, term induction, all Los induction cases, diagonal elementarity, and the compactness-via-ultraproduct proof.  The explicit uses of Choice are consistent with the Part's stated Choice convention. | F1 | Independent reproof of every citation-only theorem (notably saturated extensions, omitting types, and Keisler–Shelah); build/rendering. |
| 3. QE, categoricity, back-and-forth, games, retained additions | Read all three exact wrappers/units `07150-07294`, `07295-07468`, and `07469-07493`, plus both routed QE additions.  Checked the QE definition/method boundary; DLO completeness/model-completeness and countable-categoricity arguments; fixed-characteristic ACF scope; Ryll–Nardzewski/Morley hypotheses; back-and-forth; saturated automorphisms; EF game rules, strategy invariant, and theorem scope.  Apart from F5, the inspected table boundaries distinguish base languages from eliminating expansions. | F1, F5, F6 | Exhaustive page-by-page verification of every complexity citation; build/landscape-table rendering. |
| 4. Classification, finite model theory, preservation/abstract logic, routes | Read all three routed chapters completely.  Checked prime/atomic hypotheses, indiscernibles, stability/order property, dividing/forking, simple/NIP/o-minimal survey boundaries, finite-signature conditions for zero–one laws, ESO/Fagin and Trakhtenbrot scopes, finite compactness caveat, Los–Tarski, Chang–Los–Suszko, and Lindström statement boundaries.  Checked all labels/citations/index commands for local definition-before-reference and reachable-label uniqueness. | F1, F3, F4, F7, F8 | Full bibliographic source audit beyond the findings and theorem-identity spot checks; global book build, PDF visual inspection, human/user acceptance. |

## Scope conclusion

All four charter lots were checked at source/content level; none was left
unread in the live reader graph.  The source-level admission decision remains
**blocked by F1 and F3**, with F2 and F4-F8 also requiring correction.  Build,
visual, human, and user gates were deliberately not treated as substitutes for
this review and remain not checked here.

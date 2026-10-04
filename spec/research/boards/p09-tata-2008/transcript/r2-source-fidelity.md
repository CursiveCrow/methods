# Round 2 source-fidelity and evidence review: TATA 2008

## Disposition

I found no source-fidelity, evidence, attribution, rights, pagination, version,
terminology, bibliography, ownership, or cross-record defect in the frozen
Round 2 presentation. I therefore issue no finding identifier.

This review was independent and confined to the charter, the seven objects in
the charter's Frozen Round 2 table, and the twenty-seven original-detail page
renders named by the charter. I read all six textual frozen objects completely,
independently recomputed the identity of all seven frozen objects, and visually
inspected every required render at original detail. The hash-pinned PDF was the
controlling source object and the renders were treated only as reading aids. I
did not consult a withdrawn Round 1 object, a ledger, a chair transcript,
another reviewer report, another board, staging or layout material, memory,
conversation history, or the web.

## Frozen-object identities

Every independently recomputed SHA-256 value is identical to the value in the
charter's Frozen Round 2 table.

| Frozen object | Independently recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-tata-2008/tata-2008.pdf` | `3EB9C3F9A1A9A3BD45EC1E50BD50A1C10010789B542A2818F030A7246F9B5B22` | exact match |
| `handbook/parts/p09/presentations/n-c-015.tex` | `69AC3973E247EF090D9C78E92991BCEEDB30C0145CC276DC2C45F85DE984B4AD` | exact match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD` | exact match |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | exact match |
| `spec/research/p09-tata-2008-source-note.md` | `5D31699B3219A9340435D41B0B8B74770EA405B70C3E58C1059CB95D09F434A9` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `0E693D15418B828B650FC4A9F8310484B8121E806C45AEA07701311727DCB93F` | exact match |
| `spec/research/p09-thatcher-wright-1968-acquisition-note.md` | `547821EE7F3B8078C884C2145D4CE4857715F3E2B9775DC57B573098D96C7275` | exact match |

The frozen identity premise therefore holds for the whole review. There was no
identity mismatch and no need to reason from an unfrozen replacement.

## Original-detail visual inspection record

I inspected the following twenty-seven images individually at original detail:

- `core-rendered/page-001.png` and `page-002.png`;
- `core-rendered/page-012.png` through `page-014.png`;
- `core-rendered/page-020.png` through `page-028.png`;
- `core-rendered/page-031.png`, `page-041.png`, and `page-044.png`;
- `relevant-rendered/page-088.png` through `page-097.png`.

The inspection establishes the chartered physical-to-printed map. Physical
page 1 is the added HAL cover, physical page 2 is the monograph title page, and
each inspected numbered body page at physical page `n + 1` bears printed page
`n`. In particular, physical 12--14 are printed 11--13, physical 20--28 are
printed 19--27, physical 31 is printed 30, physical 41 is printed 40,
physical 44 is printed 43, and physical 88--97 are printed 87--96. This agrees
with `p09-tata-2008-source-note.md:36-55` and with every locator used by the
reader and compact record.

The source pages visibly support the following evidence chain:

- Physical page 1 gives the exact title; all eight authors in the order Hubert
  Comon, Max Dauchet, Rémi Gilleron, Florent Jacquemard, Denis Lugiez,
  Christof Löding, Sophie Tison, Marc Tommasi; the 262-page, 2008 citation;
  HAL id `hal-03367725`; the official HAL route; submission on 6 October 2021;
  and HAL authorization language. Physical page 2 repeats the title and the
  same author order. These pages support authorized-deposit custody, but they
  do not display a Creative Commons licence or a blanket republication grant.
- Physical pages 12--14 (printed 11--13) carry the 18 November 2008 footer and
  say both that the book discusses only finite tree automata and that there is
  no presentation or discussion of tree automata for infinite trees.
- Physical pages 20--25 (printed 19--24) establish the finite ranked-term
  setting, the literal source tuple `A=(Q,F,Q_f,Delta)`, ranked transitions,
  the nullary case, reductions, runs as position-to-state maps, successful
  final-root runs, recognizable languages, determinism as uniqueness for a
  left-hand side, completeness, and accessibility.
- Physical pages 26--28 (printed 25--27) give Theorem 1.1.9 and both versions
  of its subset construction: the theoretical powerset presentation and the
  algorithm that retains only accessible subset states. The result is an
  equivalent deterministic finite tree automaton, not a weakened inclusion.
- Physical page 31 (printed 30) states Theorem 1.3.1 with union,
  complementation, and intersection and begins the effective constructions.
- Physical page 41 (printed 40) states Theorem 1.7.4 at linear-time strength,
  identifies nonemptiness with an accessible final state, and describes the
  linear least-fixed-point/Horn route. The manuscript's qualification “in the
  automaton representation” does not enlarge the printed result.
- Physical page 44 (printed 43) states Exercise 1.4 with exactly one nullary
  symbol `a`, one binary symbol `f`, and the language
  `{f(t,t) | t in T(F)}`.
- Physical pages 88--90 (printed 87--89) define WSkS syntax and finite-set
  semantics, give the restricted syntax and Proposition 3.3.1, and exhibit the
  finite-position and symbol-subset coding of a ranked term.
- Physical pages 91--92 (printed 90--91) give Definition 3.3.2, the exact
  `0/1/bottom` coordinate cases, Figure 3.7 and Example 3.3.3 for
  `S_1={epsilon,11}`, `S_2=empty`, and `S_3={11,22}`, and begin Lemma 3.3.4.
- Physical page 93 (printed 92) displays Figure 3.9's six and only six
  one-state transitions for `X subseteq Y`: bottom-bottom, `00`, `01`, `11`,
  bottom-`0`, and bottom-`1`. The three missing combinations are exactly the
  combinations incompatible with inclusion.
- Physical page 94 (printed 93) gives the induction clauses for disjunction
  after cylindrifying the missing coordinates and taking union, negation by
  complementation, and existential set quantification by track projection.
- Physical page 95 (printed 94) states Lemma 3.3.6 and displays the quantified
  state-position partition, final-root disjunction, and local transition
  implication with the child states in the source direction.
- Physical page 96 (printed 95) completes the converse proof, expressly calls
  Theorem 3.3.7 “not very precise,” makes Lemmas 3.3.4 and 3.3.6 the exact
  statements, states Theorem 3.3.8, and gives the empty-alphabet/nullary-`top`
  reduction for a closed sentence. It then distinguishes weak finite-set
  quantification from full SkS over arbitrary sets and explains why infinite
  inputs require a top-down device and make the usual complementation route
  problematic.
- Physical page 97 (printed 96) completes that boundary: TATA does not define
  automata on infinite objects, and it points instead to Rabin's difficult
  complementation result for automata on infinite trees.

No required page was unreadable. No displayed formula, transition, title,
author order, date, theorem label, or locator used by the frozen presentation
disagreed with the controlling image.

## Source-to-handbook reconciliation

### Identity, date, custody, and rights

The cover/title-page evidence agrees with
`p09-tata-2008-source-note.md:14-34`, the reader at
`n-c-015.tex:6-10`, the compact record at
`p09-source-presentations-lot2-3.md:694-698`, and the `ComonEtAl2007`
bibliography entry at `handbook.bib:5835-5841`. The citation key remains a
stable 2007-labelled key, while its bibliographic year is 2008 and its note
identifies the inspected 18 November 2008 release. The reader correctly says
that the register's 2007 date denotes the evolving work rather than another
fixed edition. The HAL submission date is not confused with the internal
release date.

The custody note accurately records a 263-physical-page deposited object made
up of the added HAL cover and the cited 262-page monograph. Its rights statement
is appropriately narrow: authorized public deposit and research evidence do
not become a Creative Commons licence or permission to republish protected
pages. Neither the reader nor shared main text imports a source image or treats
the renders as handbook assets.

### Finite ranked trees, automata, and Chapter 1 results

`n-c-015.tex:12-30` retains the ranked arity condition, nullary term case,
positive-arity recursive term formation, finite ordered-tree standing, literal
TATA tuple order, nondeterministic transition typing, bottom-up run condition,
root acceptance, and recognizable-language definition. It also states the
source-to-handbook notation map without collision: TATA's ranked alphabet `F`
is the handbook's `Sigma`, and TATA's final set `Q_f` is the handbook's final
set `F`. The shared definition at
`logic-in-computer-science.tex:845-874` uses the handbook tuple
`(Q,Sigma,Delta,F)` consistently with that map and includes the nullary case.

The small `f(a,b)` construction at `n-c-015.tex:32-37` is mathematically
consistent with the source definitions. Its listed rules determine the stated
bottom-up assignment, the root reaches the final state, and deletion of the
only root rule leaves no transition capable of labelling the root. The
reconstruction boundary at `n-c-015.tex:154-160` explicitly identifies this
example as handbook-owned, so it is not passed off as a printed TATA example.

`n-c-015.tex:39-47` accurately reports Theorem 1.1.9's same-language
determinization and accessible subset-state implementation, Theorem 1.3.1's
effective Boolean closure, and Theorem 1.7.4's upward accessibility marking and
linear-time boundary. It neither says that an arbitrary powerset state is
accessible nor omits the source's theoretical powerset construction; it
reports the operative reduced construction used by the handbook. The shared
theorem at `logic-in-computer-science.tex:876-891` agrees with these claims,
adds only the standard decidable membership consequence already invoked in
TATA's printed emptiness proof, and preserves the finite-tree/Rabin
nonconflation.

The copying-language statement and proof at `n-c-015.tex:120-129` preserve the
exact alphabet and language printed in Exercise 1.4. The text does not
attribute a proof to the exercise. Its handbook-owned proof supplies both
otherwise-easy-to-omit premises: every term must reach a state because its
diagonal use must be accepted, and distinct terms cannot share a deterministic
state because the crossed term would then use the same child-state transition.
Ownership is repeated explicitly at `n-c-015.tex:158-160` and in the compact
record at `p09-source-presentations-lot2-3.md:704-706`.

### WSkS, coding, and both definability directions

`n-c-015.tex:49-60` matches printed 87--90: first-order variables denote words
in the finite-successor term algebra, set variables denote finite sets of such
words, and Proposition 3.3.1 yields exactly the four restricted atoms
`X subseteq Y`, `Sing(X)`, `X=Yi`, and `X=epsilon`. `Sing` and the successor
atom are defined before they are used.

`n-c-015.tex:62-71` matches printed 90--91. Coordinate `1` records membership,
coordinate `0` records a nonmember position that is a prefix of a member, and
bottom records the remaining case. Any symbol with a `0` or `1` coordinate has
arity `k`; the all-bottom symbol is nullary. The manuscript's five named
nonpadding labels agree with Figure 3.7, and all remaining leaves are described
as nullary all-bottom padding. There is no all-zero-track substitution.

The bridge at `n-c-015.tex:73-83` makes all domain restrictions explicit. A
finite tree is its finite position set `D` plus its symbol-label subsets; a
label atom becomes membership in the relevant label set; an `i`-child atom
becomes the successor equation; element quantifiers are restricted to `D` and
monadic quantifiers to subsets of `D`. In the converse direction, the state
sets partition that same finite domain. Thus the source's infinite prefix tree
is used to code a finite object and is not silently made the automaton's input.
This is exactly the bridge needed by the shared finite-tree MSO statement at
`logic-in-computer-science.tex:876-882`.

The atomic inclusion automaton at `n-c-015.tex:85-96` reproduces Figure 3.9
without adding or dropping a transition. The absence of `10`, `1-bottom`, and
`0-bottom` is correctly explained by inclusion. The same paragraph retains the
source induction's missing-coordinate/cylindrification step before union,
complement for negation, and projection for existential set quantification.

The converse at `n-c-015.tex:98-110` agrees symbol for symbol with printed
Lemma 3.3.6. It quantifies one `Y_q` per state, partitions exactly the encoded
domain, requires the root to lie in some final-state set, and uses an
implication from a node's symbol and state to a disjunction over precisely the
transitions entering that state. Inside each disjunct, child position `xi` is
placed in `Y_{q_i}`. The implication is not reversed, the source and target
states are not exchanged, and the final-state condition is not imposed at a
leaf.

`n-c-015.tex:112-118` preserves both qualifications at printed 95. It quotes
TATA's warning that Theorem 3.3.7 is “not very precise,” assigns exact control
to Lemmas 3.3.4 and 3.3.6, and uses the source's empty alphabet or single
nullary `top` convention. It correctly reduces validity of a closed sentence
to the existence of a rule `top -> q_f` for some final state.

The weak/full distinction at `n-c-015.tex:131-139` also matches printed 95--96.
Full SkS allows arbitrary subsets of the infinite successor tree and calls for
root-down automata on infinite inputs with a different complementation route.
Weak and full monadic quantification coincide only after the input structure is
actually finite. The reader expressly refuses the invalid inference from that
fact to a Rabin automaton on an entire infinite labelled tree.

### Numbering, attribution, proof ownership, and Thatcher--Wright

The numbered-result roles are exact. `3.3.4` and `3.3.6` are lemma numbers as
well as subsection numbers; `3.3.7` and `3.3.8` are theorem numbers as well as
subsection numbers on printed page 95. The reader never promotes a lemma to a
theorem or substitutes the imprecise slogan for its two exact directions.

The reconstruction boundary at `n-c-015.tex:154-160` and the compact record at
`p09-source-presentations-lot2-3.md:702-706` accurately distinguish TATA's
constructive proofs from the handbook's selected reconstruction. They do not
claim to reproduce every source transition table or every proof of Theorems
1.1.9, 1.3.1, and 1.7.4. The small run and Exercise 1.4 proof are expressly
handbook-owned; the displayed TATA constructions remain attributed to TATA.

The Thatcher--Wright boundary is also intact. The reader at
`n-c-015.tex:141-152`, compact record at
`p09-source-presentations-lot2-3.md:684-692`, bibliography at
`handbook.bib:5993-6002`, and acquisition note at
`p09-thatcher-wright-1968-acquisition-note.md:3-81` agree on James W. Thatcher
and Jesse B. Wright, the exact article title, *Mathematical Systems Theory*
2(1), March 1968, pages 57--81, and DOI `10.1007/BF01691346`. They report only
the authoritative abstract's finite-algebra, closure, generalized-Kleene, and
positive-second-order scope. The unavailable algebraic signature, recognition
map, exact logic and coding, theorem statements, examples, and proof remain
open. TATA is not used to fill them. RC-1713 is an acquisition lead only.

The required-next-visit text describes owed source-controlled artifacts and
does not give a speculative technical construction or notation a standing in
the theory. The compact record's “generalized automaton” wording occurs only in
the explicitly open, once-acquired reconstruction instruction and derives from
the registered title and abstract-level finite-algebra scope; no theorem or
definition relies on it before the body is acquired. The acquisition note's
owed list at lines 76--81 is even more explicit that no hypothetical technical
name has been introduced.

### Cross-record status

The detailed note, reader, shared main text, bibliography, compact record, and
Thatcher--Wright acquisition note agree on source identity, notation, date,
numbering, page locators, proof ownership, and open boundaries.

The Round 2 administrative repair is coherent with the rest of the compact
record. Its adjacent Thomas paragraph at
`p09-source-presentations-lot2-3.md:674-680` says that Thomas closes the stated
finite-word/infinite-tree locator gap but does not substitute for the separately
reviewed Rabin reconstruction or enlarge its narrow scope. The consolidated
paragraph at lines 913--915 records Rabin as independently accepted and TATA
2008 as body-sufficient while defining “body sufficient” as source acquisition
only. It does not call the TATA manuscript independently accepted. The TATA
entry itself still says at line 706 that independent review and admission are
open, and the consolidated open list still keeps `N-c-015.a` Thatcher--Wright
open at line 909. There is no stale Rabin sentence and no false closure of
`N-c-015.a` or `N-c-015` as a whole.

## Mandatory invariant checklist

- **T01 — PASS.** Exact title, eight-author order, HAL route, complete-object
  identity, 18 November 2008 release, 263/262 custody description, and the
  evolving-work 2007 distinction agree across all frozen records.
- **T02 — PASS.** The cover establishes an authorized HAL deposit; the custody
  note expressly denies any inference to a CC or blanket republication licence
  and keeps the PDF/renders as research evidence.
- **T03 — PASS.** Printed 11--13 and both manuscript locations distinguish
  finite ranked terms from Rabin's entire infinite labelled tree and retain
  TATA's express exclusion of infinite-tree automata.
- **T04 — PASS.** Ranked arities, nullary and positive-arity term formation,
  finite ordered-tree standing, literal `(Q,F,Q_f,Delta)` order, and the
  source-to-handbook notation map are exact.
- **T05 — PASS.** Transitions, bottom-up position-state runs, final-root
  acceptance, recognition, and nullary rules are correctly typed.
- **T06 — PASS.** Determinism is target uniqueness for a fixed symbol and child
  tuple; Theorem 1.1.9 keeps same-language strength and accessible subset
  states without claiming every omitted proof detail.
- **T07 — PASS.** Theorem 1.3.1's effective Boolean closure and Theorem 1.7.4's
  upward accessibility marking, final-marked nonemptiness criterion, and
  linear-time boundary agree with the source.
- **T08 — PASS.** The `f(a,b)` run is correct, deletion of its only root rule
  leaves no run, and the reconstruction boundary marks the example as
  handbook-owned.
- **T09 — PASS.** Word and finite-word-set semantics, Proposition 3.3.1, and all
  four restricted atoms are exact.
- **T10 — PASS.** Coordinate meanings, arities, the exact Example 3.3.3 labels,
  and nullary all-bottom padding agree with printed 90--91.
- **T11 — PASS.** The finite domain `D`, label subsets, both atom translations,
  and both quantifier restrictions are explicit; the ambient prefix tree is
  only the coding structure.
- **T12 — PASS.** Lemma 3.3.4 retains all six inclusion transitions, the
  missing-coordinate step, union, complement, and projection.
- **T13 — PASS.** Lemma 3.3.6 has one set per state, a partition of exactly the
  encoded domain, a final root, and the correctly directed local transition
  clause.
- **T14 — PASS.** The “not very precise” qualification and exact controlling
  lemmas are preserved; the closed-sentence reduction uses empty alphabet or
  the sole nullary `top` symbol and a `top -> q_f` rule.
- **T15 — PASS.** Exercise 1.4 retains its exact alphabet and language, and the
  handbook-owned proof establishes reachability for every term and separation
  of distinct terms.
- **T16 — PASS.** Arbitrary-set full SkS, root-down infinite-input automata, the
  changed complementation boundary, and finite-structure-only weak/full
  coincidence are all explicit.
- **T17 — PASS.** The shared definition at
  `logic-in-computer-science.tex:845-874` and theorem at lines 876--891 agree
  with the detailed presentation on objects, runs, recognition, finite-tree
  MSO, effective operations, and Rabin nonconflation.
- **T18 — PASS.** The reader claims an operative reconstruction, not a complete
  reproduction of every printed table or proof, and correctly assigns source
  and handbook ownership.
- **T19 — PASS.** Thatcher--Wright remains abstract-only; all body-dependent
  material stays open; TATA is not substituted; RC-1713 is only a lead; and the
  next visit is framed as an owed source artifact rather than a hypothetical
  answer installed in the theory.
- **T20 — PASS.** Author order, dates, numbering, locators, notation,
  bibliography, ownership, adjacent Rabin status, and the open/admitted
  distinctions agree across all six textual frozen objects.
- **T21 — PASS.** Ranked alphabet, term, run, recognizable language, WSkS,
  restricted atoms, encoding symbols, and full SkS are source-established and
  defined with their standing before reliance. No speculative new technical
  name is assigned to the unacquired Thatcher--Wright content.
- **T22 — PASS.** The frozen records distinguish acquired/integrated source
  material from open independent TATA review, and keep Thatcher--Wright open.
  This verdict is confined to `N-c-015.b` manuscript content on the seven exact
  Round 2 hashes. It does not accept `N-c-015.a`, `N-c-015` overall, Part IX, a
  build, visual layout of the handbook, human or user review, the book, or
  publication.

No test, test harness, automated checker, repository script, TeX command,
interim handbook build, handbook-PDF inspection, or build was run.

VERDICT: ACCEPT

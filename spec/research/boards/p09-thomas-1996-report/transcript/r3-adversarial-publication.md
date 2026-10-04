# Round 3 adversarial publication and terminology review

## Review protocol and independence

I read `charter.md` completely before making a substantive judgment.  I then
read the actual frozen LaTeX passages in
`handbook/parts/p09/presentations/n-c-013.tex` lines 800--985 and
`handbook/parts/p09/presentations/n-c-014.tex` lines 888--927 and 1451--1596,
including their immediate boundaries.  I also read the chartered portions of
the shared Part IX file and bibliography, the complete detailed Thomas source
note, and the Thomas entries and consolidated status entry in the compact
record.  I did not read a ledger, chair report, earlier-round report, another
Round 3 report, another board or transcript, memory, staging material, or web
result, and I did not contact another reviewer.

I consulted the controlling PDF itself.  The exact PDF pages used were the
unnumbered title, abstract, and contents pages; printed pp. 1, 8--12, 28--61,
and 72.  In particular, I inspected mandatory printed pp. 28, 31, and 33--35
for the Round 3 repairs.  I opened no PNG or other derived page render.  I ran
no test, test harness, automated checker, repository script, TeX command,
interim build, rendered-handbook inspection, or build.

## Independently recomputed frozen identities

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf` | `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA` | matches; 478,293 bytes |
| `handbook/parts/p09/presentations/n-c-013.tex` | `23E73DA416CE583ADF084E1D16E4A5846AC9659E4ED0E937A1CB00FA0738AFED` | matches |
| `handbook/parts/p09/presentations/n-c-014.tex` | `F9576BB10063037CDFD9018E6DC7DFB553651590FB74FC77D2D33EEBBF4D5915` | matches |
| `handbook/parts/p09/logic-in-computer-science.tex` | `70CFEBC05E1F574703FA6F8B1367C2EBBA1A640A57B2DEEC8D144E88328A7117` | matches |
| `handbook/bib/handbook.bib` | `07233B0722E6DAE89AEE6B34F699BC980D54F4367C2672B4D3B92131F6D680AD` | matches |
| `spec/research/p09-thomas-1996-report-source-note.md` | `F169CB0936EAA8CB650102A974FEE01F05C3E9D58774F7A198E2CEE35E2A7150` | matches |
| `spec/research/p09-source-presentations-lot2-3.md` | `C45908A389BB22FBB584672F9F78F1C0E45E7DDF274BC37039AEA9BC81ED281F` | matches |

## Finding register

No blocker, must-fix, should-fix, consider, discard, or unresolved-user
finding survives review.  The finding register is empty, so no finding
identifier or repair requirement is assigned.

## First-occurrence and terminology audit

The operative first occurrences pass the charter's five-part rule.

| First occurrence | Necessity and exact definition | Standing and nonredundancy | Required later use |
|---|---|---|---|
| The four omega acceptance modes, `n-c-013.tex` lines 833--853 | Each mode is separately typed because the acceptance data and quantifier force differ; the displayed formulae define Buechi, Muller, Rabin, and Thomas's Streett convention. | They are acceptance components of word automata, not finite-word or tree data; lines 845--853 make the Rabin/Streett difference explicit. | Example 5.2 and Proposition 5.3 use the distinction at lines 853--858 (printed pp. 28--30). |
| *Safra tree*, `n-c-013.tex` lines 883--896 | Lines 883--885 explain why a reachable-state subset is insufficient.  Lines 885--891 define exactly `(T,ell,nu,M)`, including the typed injective live-node name map. | Lines 892--896 say that it is one determinized word-automaton state, not an input tree or a Rabin-tree run, and distinguish names from labels and marks. | The initial state, update, persistence, Rabin pairs, proof, and bounds use every component at lines 897--958 (printed pp. 31--37). |
| Empty determinization state, `n-c-013.tex` lines 915--925 | It is needed exactly when advancement empties the root and is defined as the empty ordered-tree state with no node, name, label, or mark, absorbing on later letters. | It differs from every ordinary construction state by having no root; its rejection and bound preservation are proved locally. | It is included in every `E_k`, no `F_k`, and the rejection proof at lines 942--947 (source gap on printed pp. 28 and 34). |
| *Order-vector with hit*, `n-c-014.tex` lines 1490--1498 | The Muller-to-chain conversion requires finite memory; the term is eliminated as a permutation ordered by last appearance plus the former position of the newly visited state. | It is finite state memory, not an input tree or a path; its distinction from the bare permutation is the hit position. | Remark 6.6 recovers the recurrent set from eventual hit positions (printed pp. 45--47). |
| Completed automaton `A^bot`, `n-c-014.tex` lines 1500--1533 | Partial source transitions do not meet the game's nonempty-outdegree hypothesis.  Lines 1503--1516 give the typed missing-transition and absorbing-loop completion. | Lines 1517--1520 identify a chain tree automaton, not a game or run, and state exactly how it differs from `A`; lines 1521--1528 prove language and chain preservation. | The renamed completed relation is used throughout the game, complement, finite-game, basis, and S2S arguments at lines 1531--1586 (source gap on printed pp. 44 and 47--51). |
| *Memoryless* strategy, `n-c-014.tex` lines 1534--1542 | Theorem 6.8 requires the distinction; line 1539 defines it by dependence only on the current game position. | It is a strategy property and is explicitly contrasted with dependence on the earlier play. | It supplies Pathfinder's local instruction tree and the regular-tree generator at lines 1542--1573 (printed pp. 47--57). |
| *Regular* input tree, `n-c-014.tex` lines 1564--1574 | It is exactly a tree whose labels are generated by a deterministic finite direction-word automaton with an output map. | Line 1567 says it is a property of an input tree, not an acceptance mode. | Theorem 6.18 uses it for the effective basis conclusion (printed pp. 56--57). |

The detailed note independently introduces the Safra-tree tuple with the same
necessity, definition, standing, nonredundancy, and use at lines 151--161, and
the order-vector-with-hit memory at lines 226--235.  The compact record's
Thomas entries refer to these already established manuscript objects rather
than naming hypothetical future objects.  No premature technical name or
undefined standing remains.

## Source/handbook ownership audit

The source-carried premises and handbook-owned completions are not conflated.
Thomas's total deterministic transition function is restored as source content
at `n-c-013.tex` lines 822--832 (printed p. 28).  Thomas's named-node update,
surviving-name persistence, reservoir, and acceptance proof remain source
content at lines 905--958 (printed pp. 33--37).  By contrast, the initial name
`1` is labelled a handbook normalization at lines 897--899; mark clearing is a
handbook clarification at lines 899--905; the empty-root successor is a
handbook completion at lines 915--925; injectivity and pairwise-distinct
same-update allocation are handbook definedness clauses at lines 926--931; the
accepting-cycle condition is a handbook repair at lines 965--969; and the
rejecting tree-transition completion is handbook-owned at `n-c-014.tex` lines
1500--1529.  The detailed note repeats the same allocation at lines 284--314.

## Mandatory invariant dispositions

- **H01 -- PASS.** The PDF title page identifies Wolfgang Thomas,
  *Languages, Automata, and Logic*, May 1996, Bericht 9607, Kiel.  Its native
  object has 478,293 bytes, 75 physical pages, and the recomputed charter hash.
  The detailed note lines 13--22 and 24--47 calls it a complete report precursor,
  not a verified final-chapter facsimile.

- **H02 -- PASS.** The actual abstract says the prospective *Handbook of
  Formal Language Theory*.  The detailed note lines 73--82 preserves that
  literal phrase and distinguishes the registered *Handbook of Formal
  Languages* title recorded at `handbook.bib` lines 2358--2366.

- **H03 -- PASS.** The title, abstract, contents, printed p. 1, and printed
  p. 72 verify the physical/printed map in the detailed note lines 36--61.
  Section 3.1 begins on printed p. 8, Sections 5.1--5.3 on pp. 28, 31, and 37,
  Chapter 6 on p. 43, Sections 6.1--6.3 on pp. 44, 47, and 57.  No locator is
  assigned to the unreconciled final chapter.

- **H04 -- PASS.** The detailed note lines 63--71 and 316--322 limits the
  public university-course copy to research evidence, records no CC or blanket
  republication licence, and makes every derived image an inert viewer aid
  rather than source evidence or a handbook asset.

- **H05 -- PASS.** `n-c-014.tex` lines 888--901 gives Thomas's finite-word
  tuple, three-place transition relation, length-`n+1` run, initial state,
  final-state test, and effective two-way Theorem 3.1 exactly as printed on
  pp. 8--9.

- **H06 -- PASS.** Lines 903--913 gives pairwise-disjoint tracks, the separate
  last-letter transition, the empty-word existence guard, the four printed
  `MSO_0` atoms, and complement/union/projection with the correct logical
  roles (printed pp. 8--9).

- **H07 -- PASS.** Lines 914--918 restricts `WS1S` monadic variables to finite
  sets, uses input-free successful-run existence, and limits the reversed-binary
  Presburger summary to the finite-carry route on printed pp. 10--12.

- **H08 -- PASS.** `n-c-013.tex` lines 800--832 types the finite omega tuple,
  relation, run, initial condition, recurrence set, and the distinct total
  deterministic specialization before any use (printed p. 28).

- **H09 -- PASS.** Lines 833--858 states all four conditions with Thomas's
  exact pair ordering.  In particular, the displayed Streett formula and prose
  say recurrence in `F_i` implies recurrence in `E_i` (printed pp. 28--30).

- **H10 -- PASS.** Lines 853--881 preserves Example 5.2, Proposition 5.3's
  nondeterministic equivalence, the finite-union characterization, deterministic
  Buechi complement failure, and total deterministic Muller complementation,
  while assigning McNaughton's theorem and Thomas's later Safra proof correctly
  (printed pp. 29--31).

- **H11 -- PASS.** The first manuscript use at lines 883--896 passes all five
  terminology requirements and types an ordered determinization-state tree of
  state subsets with disjoint siblings, proper child-union containment,
  injective live-node names, and current marks.  Its word-state standing is
  expressly distinguished from an input tree and a tree-automaton run (printed
  pp. 31--33).

- **H12 -- PASS.** Lines 897--934 gives the initial `{q_0}` root, initial name,
  current-event marks, source update order, empty-root branch, persistence,
  predecessor-name exclusion, pairwise same-update allocation, at-most-`n`
  live nodes, and the `1,...,2n` reservoir.  Deleted names may be reused only
  after an intervening predecessor state in which they are absent, so lineage
  and the Rabin excluding sets are not confused (printed pp. 33--34).

- **H13 -- PASS.** Lines 934--958 gives eventual persistence plus infinitely
  many distinct current collapse events, exact `E_k,F_k`, both proof
  directions, `2^{O(n log n)}` states, exactly `2n` displayed pairs, and the
  qualified no-`2^{O(n)}`/`O(n)` conversion lower bound using the factorial
  complementation family (printed pp. 34--37).

- **H14 -- PASS.** Lines 960--969 preserves Theorem 5.9's effective two-way
  strength and exposes Corollary 5.10's printed p. 38 omission.  The reachable
  nonempty cycle meeting the Buechi set is labelled a handbook-owned correction,
  not attributed to Thomas's printed proof.

- **H15 -- PASS.** Lines 969--980 states the finite disjunction of eventual
  absence and recurring presence tests, requires every inner quantifier to be
  bounded below the current position, and defines weak MSO here by finite-set
  monadic ranges (printed pp. 38--39).

- **H16 -- PASS.** `n-c-014.tex` lines 1451--1476 gives the four-place tree
  transition relation, global run, root and child equations, and exact
  existential-run/universal-path Muller acceptance.  Examples 6.2--6.3 are
  used only for their Buechi/Muller separation (printed pp. 43--45).

- **H17 -- PASS.** Lines 1478--1498 gives the strict chain, exact path
  condition, and a five-part introduction of order-vector-with-hit memory as a
  permutation plus prior position; Remark 6.6 supplies its nonredundant use
  (printed pp. 45--47).

- **H18 -- PASS.** After the proved completion, lines 1534--1546 gives the
  Automaton-then-Pathfinder move order, Remark 6.7's acceptance equivalence,
  and the exact current-position-only definition of memoryless before Theorem
  6.8 is used (printed pp. 47--49).

- **H19 -- PASS.** Lines 1541--1555 gives a finite local-direction-function
  label at each node, universal transition-sequence checking on a path via word
  closure, universal checking of all paths by a deterministic Muller tree
  automaton, and nondeterminism only for guessing local labels.  It expressly
  makes the result independent of the particular input tree and propagates the
  completion back to the original partial automaton (printed pp. 49--50).

- **H20 -- PASS.** Lines 1555--1574 keeps Theorem 6.13's forced-finite-visit
  and complementary-subgame induction, Theorem 6.16's finite-game
  effectivity, Definition 6.17's direction-word generator with output, and
  Theorem 6.18's input guessing, finite game, memoryless generator, effective
  emptiness, and regular-member conclusion separately typed (printed pp.
  51--57).

- **H21 -- PASS.** Lines 1576--1596 gives Theorem 6.19's atomic,
  disjunction, existential, and complement steps, the reverse existential-run /
  universal-path form, and Theorem 6.20's input-free decision route after
  completion.  Lines 1591--1596 says this is Thomas's later route, not Rabin's
  Section 3.12 proof and not a reopening of `N-c-014.d` (printed pp. 57--59).

- **H22 -- PASS.** The two bibliography entries at `handbook.bib` lines
  2346--2366, shared source standing at `logic-in-computer-science.tex` lines
  15--42, word and S2S reader passages at lines 723--762 and 814--846, source
  guide at lines 2348--2356, detailed note, and compact entries agree on source
  and proof ownership.  The detailed note lines 324--352 and compact record
  lines 606--616, 674--682, and 902--916 preserve the narrow precursor and open
  completion boundary; no test or build is offered as scholarship.

## Round 2 repair dispositions

- **R2-01 -- PASS.** `n-c-013.tex` lines 860--872 states a finite union of
  `U_j V_j^omega`, types both factors as regular finite-word languages, and
  defines infinite concatenation by unbounded accumulated length.  It also says
  this is Thomas's report-level survey statement rather than priority evidence
  (printed p. 30).

- **R2-02 -- PASS.** Lines 915--925 defines the empty, unmarked, absorbing
  state when root advancement is empty and proves rejection and all bound
  preservation; lines 942--947 place it in every `E_k`, no `F_k`, and reject it.
  This is explicitly a handbook completion of the gap on printed pp. 28 and 34.

- **R2-03 -- PASS.** Lines 899--905 clears predecessor marks and permits only
  current-update collapse marks.  Lines 944--952 makes the proof depend on
  infinitely many distinct collapse events and verifies rejection of
  `a b^omega`; ownership is explicit against printed pp. 34--35.

- **R2-04 -- PASS.** `n-c-014.tex` lines 1500--1529 gives the exact fresh
  rejecting-state completion, proves language and strict-chain preservation,
  and establishes nonempty finite outdegree.  Lines 1531--1556, 1568--1574,
  and 1576--1586 propagate it through complement, finite-game, regular-basis,
  and S2S uses.  This repairs, without attributing away, the source gap visible
  on printed pp. 44 and 47--51.

## Round 3 repair dispositions

- **R3-01 -- PASS.** Immediately after the general run and `In(r)`,
  `n-c-013.tex` lines 822--832 gives Thomas's total
  `delta:Q x Sigma -> Q`, the unique-run equation, and the explicit statement
  that every word has one run.  Lines 874--881 then makes deterministic Muller
  complementation rely on that total premise, not a partial functional relation
  (printed pp. 28 and 31).

- **R3-02 -- PASS.** At the actual first use, lines 885--896 includes the typed
  injection `nu:N(T) -> {1,...,2n}` and distinguishes it from labels and marks.
  Lines 897--899 owns the initial-name normalization; lines 926--934 preserves
  surviving names and gives pairwise-distinct new names outside the entire
  predecessor name set with the exact reservoir argument; lines 915--925 and
  942--943 gives the empty name set; and lines 936--943 defines the exact
  absence/marked-presence pairs.  Lines 929--931 identifies injectivity and
  same-update distinctness as handbook-owned definedness, while the surrounding
  named-node construction remains source content (printed pp. 33--35).

- **R3-03 -- PASS.** The detailed note lines 331--349 and compact record lines
  616, 682, and 911 agree that Round 1 rejected, Round 2 rejected despite its
  source-fidelity accept, both Round 2 omissions are repaired, Round 3 is open,
  the 1997 chapter is unreconciled, and no Thomas presentation or broader unit
  is admitted.  Detailed-note lines 63--71 makes derived images inert and
  requires the actual frozen LaTeX and controlling PDF for later review.

## Adversarial rationale and admission boundary

The deterministic complement claim fails if a missing word transition is
allowed; the manuscript blocks that countermodel with totality and a unique run.
The Safra acceptance proof fails under shared new names, same-update reuse of a
predecessor name, a deleted-root pseudo-tree, or persistent old marks; the
injective tuple, predecessor-name exclusion, absorbing empty state, and
current-event mark semantics block each case and keep `E_k,F_k` defined.  The
tree-game proof fails on a missing transition; the fresh rejecting state makes
every position live without adding an accepting path and is carried through
every later use.  The records do not turn a public access route into a licence,
Thomas's later proof into Rabin's historical proof, the report into the final
chapter, a source defect repair into a quotation, or the open Round 3 snapshot
into an admitted presentation.

Accordingly, this seat accepts only the unchanged May 1996 report-precursor
manuscript content proposed for `N-c-013.e` and `N-c-014.e`.  It does not accept
the registered 1997 chapter, any original-source body still open, either
presentation overall, Part IX, a rendered handbook, a build, human or user
review, the final book, or publication.

VERDICT: ACCEPT

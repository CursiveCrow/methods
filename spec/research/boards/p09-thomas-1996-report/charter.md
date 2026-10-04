# Board charter: Thomas 1996 report precursor for `N-c-013.e` and `N-c-014.e`

- Artifact: the frozen round-specific source/manuscript snapshot below.
- Purpose: determine whether the handbook's infinite-word, finite-word, and
  infinite-tree reconstructions from Wolfgang Thomas's May 1996 Kiel report
  are source-faithful, mathematically correct, definition-before-use
  compliant, and fit for graduate-handbook publication at explicit report-
  precursor strength.
- Mode: review.
- Requested by: the standing requirement that every completed handbook topic
  receive three independent blind scholarly reviews before admission.
- Authorship disclosure: chair-authored reconstruction. No seated reviewer
  authored a frozen object.
- Severity taxonomy: blocker, must-fix, should-fix, consider, discard,
  unresolved-user.
- Source rule: every finding must cite an exact manuscript line and controlling
  printed report page. Reviewers must read the actual frozen LaTeX and records;
  the hash-pinned source PDF controls source formulae, symbols, pagination, and
  wording. Derived page images carry no independent evidence and are not a
  required review object.
- Consensus rule: admission requires every mandate to end with no unresolved
  blocker or must-fix and all three seats to file `VERDICT: ACCEPT` on one
  unchanged frozen snapshot. A supported finding cannot be outvoted.
- Board type: live.
- Workspace: `spec/research/boards/p09-thomas-1996-report/`.

## Frozen Round 1 snapshot

No frozen object may be edited while this round is open. Any content or status
edit invalidates every Round 1 verdict and requires a new hash-pinned blind
round.

| Artifact | Review scope | SHA-256 |
|---|---|---|
| `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf` | complete controlling May 1996 report; claims limited to the inspected pages below | `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA` |
| `handbook/parts/p09/presentations/n-c-013.tex` | whole-file identity; substantively lines 799--917, the complete Thomas infinite-word presentation | `76480DE7C2620521835DD1301B5D8B5698C60E14AA0B2EFA467D852F81BB36CA` |
| `handbook/parts/p09/presentations/n-c-014.tex` | whole-file identity; substantively lines 888--927 and 1451--1555, the finite-word and later infinite-tree Thomas passages plus their boundaries | `F12CD5EDD8D160D91E9A2BC7B68056EF77AB8F2F6FFF5AD4EC474669059CF31B` |
| `handbook/parts/p09/logic-in-computer-science.tex` | complete shared Part IX file; especially source-role lines 25--42, word-automata lines 721--762, finite-word theorem lines 814--828, S2S boundary lines 843--846, and source guide lines 2348--2356 | `70CFEBC05E1F574703FA6F8B1367C2EBBA1A640A57B2DEEC8D144E88328A7117` |
| `handbook/bib/handbook.bib` | complete bibliography; especially `Thomas1996Report` and `Thomas1997` at lines 2346--2367 | `07233B0722E6DAE89AEE6B34F699BC980D54F4367C2672B4D3B92131F6D680AD` |
| `spec/research/p09-thomas-1996-report-source-note.md` | complete identity, version, page, mathematical, defect, rights, and scope record | `B33BF77916C06C57F4896394B4A5569678D75B0B14A940FF451D68D4BD915FB8` |
| `spec/research/p09-source-presentations-lot2-3.md` | complete compact record; especially `N-c-013.e` at lines 606--616, `N-c-014.e` at lines 674--682, and the consolidated open-status ledger | `45F8EB339A139C24251616F03A77715337F8E8B8F735956D35B05407D92637C7` |

Every reviewer must independently recompute all seven native identities before
substantive judgment and record the values in its report.

## Round 1 source-page procedure -- historical record; do not execute

The following records the Round 1 procedure only. Requiring inspection of both
the controlling PDF and forty-four derived images was redundant. Round 2 and
later rounds use the actual manuscript LaTeX and the actual source PDF only.
Nothing in this section is a current instruction, and no future reviewer may
use a PNG or other manuscript/source render as a review object.

The PDF has 75 physical pages. Physical page 1 is the title page, physical page
2 the abstract, physical page 3 the contents page numbered `i`, physical page 4
printed page 1, and physical page 75 printed page 72.

The superseded Round 1 instruction required each reviewer to inspect these five
identity/page-map renders at original detail:

- `tmp/pdfs/p09-thomas-1997/inspect-title-01.png`;
- `tmp/pdfs/p09-thomas-1997/inspect-title-02.png`;
- `tmp/pdfs/p09-thomas-1997/inspect-title-03.png`;
- `tmp/pdfs/p09-thomas-1997/inspect-body-start-04.png`; and
- `tmp/pdfs/p09-thomas-1997/inspect-body-end-75.png`.

It also required all thirty-nine substantive renders to be inspected at
original detail:

- `tmp/pdfs/p09-thomas-1997/relevant-rendered/page-11.png` through
  `page-15.png`: printed pp. 8--12, Section 3.1;
- `page-31.png` through `page-33.png`: printed pp. 28--30, Section 5.1;
- `page-34.png` through `page-39.png`: printed pp. 31--36, Section 5.2;
- `page-40.png` through `page-45.png`: printed pp. 37--42, Section 5.3;
- `page-46.png`: printed p. 43, Chapter 6 introduction; and
- `page-47.png` through `page-64.png`: printed pp. 44--61, Sections 6.1--6.3.

In Round 1, the renders were reading aids. The hash-pinned PDF controlled. Searchable
extraction may be used only to navigate; no formula, symbol, wording, or page
claim may be accepted from extraction without inspecting the corresponding
original-detail page.

## Exact admission question

The board decides only whether the frozen May 1996 report-precursor
reconstructions may be admitted as `N-c-013.e` and `N-c-014.e` manuscript
content. It does not decide that the registered 1997 chapter body has been
acquired or reconciled. It does not admit Buechi 1962, McNaughton 1966, Safra
1988, Rabin 1969, either presentation file overall, `N-c-013` or `N-c-014`
overall, Part IX, another part, a rendered handbook page, a build, human or user
review, the final book, or publication.

Rabin's original presentation remains separately controlled by his 1969
article and its already completed narrow review. Thomas's later game-theoretic
route may be accepted only if it remains expressly later and non-substitutive.

## Mandatory invariant checklist

The labels `H01`--`H22` are metalinguistic review identifiers, not names
introduced into the mathematics. Every reviewer must dispose of every item
expressly.

- **H01 -- identity and version.** The controlling object must be Wolfgang
  Thomas, *Languages, Automata, and Logic*, Bericht 9607, Kiel, May 1996,
  478,293 bytes, 75 physical pages, with the frozen hash. It is a complete
  report precursor, not a verified facsimile of the registered 1997 chapter.
- **H02 -- prospective and final titles.** The report abstract's literal
  prospective title *Handbook of Formal Language Theory* must remain distinct
  from the eventual *Handbook of Formal Languages* publication identity.
- **H03 -- page map and coverage.** Every relied-on printed/physical locator
  and every claimed source range must agree with the PDF. No
  final-chapter locator may be inferred.
- **H04 -- rights and custody.** Public university-course access must not be
  promoted to a Creative Commons or blanket republication licence. The PDF is
  research evidence rather than a handbook asset; any derived page images are
  merely viewer aids and have no independent evidentiary standing.
- **H05 -- finite-word tuple and run.** Section 3.1's tuple, transition type,
  length-`n+1` run, initial state, final state, and Theorem 3.1 effective
  equivalence must be exact.
- **H06 -- finite-word proof directions.** Disjoint state tracks, the separate
  last-letter transition, the empty-word guard, the exact `MSO0` atomic forms,
  complement, union, and projection must match printed pp. 8--9.
- **H07 -- finite-word consequences.** `WS1S` must use finite-set-valued
  monadic variables and input-free successful-run existence. The reversed-
  binary finite-carry Presburger route must not be inflated beyond pp. 10--12.
- **H08 -- omega tuple and recurrence set.** Definition 5.1's state, alphabet,
  initial state, transition relation, acceptance component, run, and `In(r)`
  must be typed before use and must not be confused with finite-word or tree
  automata.
- **H09 -- four acceptance modes.** Buechi, Muller, Rabin, and Thomas's exact
  Streett pair convention must be correct. In particular, Streett recurrence
  of `Fi` implies recurrence of `Ei`, not the other way around.
- **H10 -- comparison and deterministic boundary.** Example 5.2,
  Proposition 5.3, the finite-union `U V^omega` characterization, the
  deterministic-Buechi complement failure, and deterministic-Muller
  complementation must retain their exact strengths and ownership.
- **H11 -- determinization-state standing.** The Safra object must be a finite
  ordered determinization-state tree of state subsets, with disjoint siblings,
  proper child-union containment, and a breakpoint mark. It is not an input
  tree or a run of Rabin's tree automaton. The source term must have necessity,
  definition, standing, nonredundancy, and later use at first occurrence.
- **H12 -- update order and names.** The initial `{q0}` root, creation of
  youngest `R intersect F` children, advance of every label including new
  children, horizontal deletion, vertical collapse/marking, persistent old
  names, fresh-name rule relative to the preceding tree, at most `n` live
  nodes, and `1,...,2n` name reservoir must be exact and in source order.
- **H13 -- determinization acceptance and bounds.** Eventual name persistence,
  infinite marking, the `(Ek,Fk)` absence/marked-presence pairs, both proof
  directions, Proposition 5.6's state and pair counts, and Theorems 5.7--5.8's
  lower-bound qualifier must not be weakened, strengthened, or misattributed.
- **H14 -- omega MSO and printed defect.** Theorem 5.9 must retain effective
  two-way strength. Corollary 5.10's printed omission of the Buechi-final-state
  condition must be visible, and the reachable nonempty cycle meeting `F` must
  be identified as the handbook-owned correction rather than silently quoted
  from the report.
- **H15 -- bounded and weak formula consequence.** Proposition 5.11's finite
  disjunction of eventual absence and recurring presence tests must have its
  inner quantifiers bounded below the current position. Corollary 5.12's weak
  monadic range must mean finite sets.
- **H16 -- tree tuple, run, and path quantifiers.** Definition 6.1's four-place
  transition relation, global run, root and child equations, and
  existential-run/universal-path Muller condition must be exact. Examples
  6.2--6.3 must support only the stated Buechi/Muller separation.
- **H17 -- chain condition and added memory.** Definition 6.4's strict chain
  and path acceptance must be exact. Theorem 6.5's order-vector with hit must
  be defined as a permutation plus prior position, must stand as finite state
  memory rather than input or run, and must have the Remark 6.6 use that makes
  it nonredundant.
- **H18 -- game and memoryless standing.** The Automaton/Pathfinder move order,
  Remark 6.7 acceptance equivalence, and definition of a memoryless strategy as
  depending only on the current position must be exact before Theorem 6.8 is
  used.
- **H19 -- complementation proof architecture.** Theorem 6.9 must correctly
  encode Pathfinder's local direction functions by a finite-label tree,
  universally handle transition choices along one path through word-automaton
  closure, universally handle all paths by a deterministic Muller tree
  automaton, and use nondeterminism only to guess the local labels. The result
  must be independent of the particular input tree.
- **H20 -- determinacy, regular trees, and basis.** Theorem 6.13's forced-
  finite-visit/complementary-subgame induction, Theorem 6.16's finite-game
  effectivity, Definition 6.17's finite generator with output, and Theorem
  6.18's input guessing, finite game, memoryless strategy, effective emptiness,
  and regular-member conclusion must be correct and separately typed.
- **H21 -- MSO translation, S2S, and historical boundary.** Theorem 6.19's
  atomic, disjunction, existential, and complement steps, the converse
  existential-run/universal-path formula shape, and Theorem 6.20's input-free
  decision route must be exact. Thomas's route must remain later and must not
  be projected onto Rabin's Section 3.12 proof or reopen `N-c-014.d`.
- **H22 -- cross-file, terminology, and completion scope.** Bibliography,
  reader passages, shared Part IX text, detailed note, compact record, page
  locators, source ownership, proof ownership, technical terminology, and open
  status must agree. A verdict may admit only the two May 1996 report-
  precursor manuscript presentations on the frozen hashes. No test, test
  harness, automated checker, repository script, TeX command, interim build,
  rendered-handbook inspection, or build may be used as evidence.

## Seat mandates

### Source fidelity and evidence

Audit source identity, date/version, custody, rights, physical-to-printed page
map, every tuple, formula, transition order, pair convention, numbered-result
role, page locator, attribution, printed defect, repair ownership, and agreement
among all frozen records. Read the actual LaTeX passages and consult the actual
source-PDF pages on which each judgment rests. A source mismatch, unread
required source passage, silent repair, final-chapter conflation, or attribution
inflation is at least a must-fix.

### Mathematical and proof correctness

Independently reconstruct the finite-word translations, all four omega
acceptance conditions, nondeterministic equivalence, deterministic boundary,
Safra invariant and update, name discipline, acceptance proof and bounds,
omega-word MSO directions, corrected input-free cycle criterion, tree run and
chain acceptance, game reduction, complement construction, determinacy
argument, regular-tree basis theorem, and S2S decision. Stress-test the empty
word, empty acceptance components, missing runs, duplicate Safra states, node
deletion/reuse, transient names, nonaccepting cycles, source Streett ordering,
states outside a displayed chain, no available transition, and empty tree
language. A type error, quantifier error, invalid proof step, false equivalence,
or theorem-strength inflation is at least a must-fix.

### Adversarial publication and terminology

Try to falsify the reconstruction across finite/infinite words, words/trees,
Buechi/Muller/Rabin/Streett, determinization state/input tree/run,
report/final chapter, historical/later proof, source/handbook correction,
access/licence, proof/outline, and reconstruction/admission boundaries. Audit
the five-part terminology rule at every actual first use and all cross-file
status language. A premature technical name, undefined standing, hidden source
substitution, stale completion claim, or cross-record contradiction is at least
a must-fix.

## Round 1 independence and filing rule -- historical record; do not execute

Round 1 used three fresh agents with no inherited turn history. Each was to audit
the complete chartered scope independently. A reviewer was permitted to read
only this charter, the seven Round 1 objects, and the forty-four original-detail
renders named above. It was not permitted to read `ledger.md`,
`transcript/chair.md`, another Round 1 report, another board or board transcript,
conversation history, memory, staging material, or web results. Reviewers were
not permitted to contact one another.

The assigned files are:

- `transcript/r1-source-fidelity.md`;
- `transcript/r1-mathematical-proof.md`; and
- `transcript/r1-adversarial-publication.md`.

Each report was required to contain: the independently recomputed seven
identities; an explicit statement that all forty-four then-required renders
were inspected at original detail; a disposition for every `H01`--`H22`; any
findings with exact severity, identifier, file line, printed source page, and
repair requirement; and a concise seat-specific rationale. The reviewer was
permitted to write only its assigned report. Its final line was required to be
exactly `VERDICT: ACCEPT` or `VERDICT: REJECT --` followed by exact finding
identifiers.

Round 1 remained book scholarship. No test, test harness, automated checker,
repository script, TeX command, interim handbook build, handbook-PDF
inspection, or build was authorized.

## Frozen Round 2 snapshot

Round 1 is closed and rejected. The repairs are now frozen at the identities
below. No frozen object may be edited while Round 2 is open; any content or
status edit invalidates every Round 2 verdict and requires a new blind round.

| Artifact | Review scope | SHA-256 |
|---|---|---|
| `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf` | complete controlling May 1996 report; source claims limited to the actual pages cited by the frozen records | `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA` |
| `handbook/parts/p09/presentations/n-c-013.tex` | whole-file identity; substantively lines 800--956, the complete revised Thomas infinite-word presentation and its boundary | `F3473BB8C2D77A56D82C7086888CD9087AE887847ED3FDA021DC6826868C25E3` |
| `handbook/parts/p09/presentations/n-c-014.tex` | whole-file identity; substantively lines 888--927 and 1451--1596, the finite-word and revised later infinite-tree Thomas passages plus their boundaries | `F9576BB10063037CDFD9018E6DC7DFB553651590FB74FC77D2D33EEBBF4D5915` |
| `handbook/parts/p09/logic-in-computer-science.tex` | complete shared Part IX file; especially source-role lines 25--42, word-automata lines 721--762, finite-word theorem lines 814--828, S2S boundary lines 843--846, and source guide lines 2348--2356 | `70CFEBC05E1F574703FA6F8B1367C2EBBA1A640A57B2DEEC8D144E88328A7117` |
| `handbook/bib/handbook.bib` | complete bibliography; especially `Thomas1996Report` and `Thomas1997` at lines 2346--2367 | `07233B0722E6DAE89AEE6B34F699BC980D54F4367C2672B4D3B92131F6D680AD` |
| `spec/research/p09-thomas-1996-report-source-note.md` | complete revised identity, version, page, mathematical, correction, rights, and scope record | `3F63E37FE1E7C72140080302E3BDFA716D617A8E73BA157F0D12977041093681` |
| `spec/research/p09-source-presentations-lot2-3.md` | complete compact record; especially `N-c-013.e` at lines 606--616, `N-c-014.e` at lines 674--682, and the consolidated open-status ledger | `B43F11B230E9CFF763CAE106A91CDA29122305B02F4CA621E60BD4E63D253208` |

Every Round 2 reviewer must independently recompute all seven native
identities before substantive judgment and record the values in its report.

## Round 2 repair invariants

Every reviewer must dispose of `H01`--`H22` again on the complete revised
passages and must also dispose expressly of these five repair invariants:

- **R2-01 -- finite-union characterization.** The reader must state the exact
  finite union of `U V^omega` characterization, require regular finite-word
  factors, define infinite concatenation so its total length is unbounded, and
  retain report-precursor rather than original-priority standing. Controlling
  source: printed p. 30.
- **R2-02 -- empty determinization successor.** If advancement empties the
  root, the update must enter a precisely defined empty, unmarked, absorbing
  determinized word-automaton state with no node or name. The text must prove
  rejection preservation and show that the live-node, name-reservoir,
  asymptotic-state, and exact-pair bounds remain valid. Controlling source gap:
  printed pp. 28 and 34; the completion is handbook-owned.
- **R2-03 -- breakpoint-event lifetime.** Predecessor marks must be cleared,
  only collapses in the current letter update may mark the successor, and the
  acceptance proof must use infinitely many distinct collapse events. The
  one-breakpoint word `a b^omega` must reject. Controlling source gap: printed
  pp. 34--35; the clarification is handbook-owned.
- **R2-04 -- partial tree-transition completion.** Before the game, the reader
  must give an exact rejecting-state completion for missing state-letter
  transitions, prove language and strict-chain preservation, establish
  nonempty finite outdegree, and propagate the completion through
  complementation, the finite game, the regular-tree basis route, and `S2S`.
  Controlling source gap: printed pp. 44, 47--51; the completion is
  handbook-owned.
- **R2-05 -- terminology and status.** The first manuscript occurrence of the
  determinization-state technical name must be its five-part introduction.
  Detailed and compact records must agree that Round 1 rejected, Round 2 is
  open, the 1997 final chapter remains unreconciled, and no broader manuscript
  unit has been admitted.

## Round 2 source use, independence, and filing

Round 2 uses three new reviewers with no inherited turn history. Each reviewer
must read the actual frozen LaTeX passages in full, together with the actual
frozen Markdown records needed by its seat. It must consult Thomas's actual
hash-pinned source PDF at the printed pages supporting every source judgment;
printed pp. 30, 28 and 34--35, and 44 and 47--51 are mandatory for the five
repairs. No PNG or other derived page render is required or carries independent
evidentiary weight.

A reviewer may read only this charter, the seven Round 2 objects, and the
controlling PDF pages needed for its judgments. It may not read `ledger.md`,
`transcript/chair.md`, a Round 1 report, another Round 2 report, another board
or board transcript, conversation history, memory, staging material, or web
results. Reviewers may not contact one another.

The assigned files are:

- `transcript/r2-source-fidelity.md`;
- `transcript/r2-mathematical-proof.md`; and
- `transcript/r2-adversarial-publication.md`.

Each report must contain: the independently recomputed seven identities; an
explicit statement that the actual frozen `.tex` passages were read; the exact
source-PDF pages used; a disposition for every `H01`--`H22` and `R2-01`--
`R2-05`; any findings with exact severity, identifier, file line, printed source
page, and repair requirement; and a concise seat-specific rationale. The
reviewer may write only its assigned report. Its final line must be exactly
`VERDICT: ACCEPT` or `VERDICT: REJECT --` followed by exact finding identifiers.

Round 2 remains book scholarship. No test, test harness, automated checker,
repository script, TeX command, interim handbook build, handbook-PDF
inspection, or build is authorized.

## Frozen Round 3 snapshot

Round 2 is closed and rejected. Its two must-fix findings have been repaired in
the actual manuscript LaTeX and the two Thomas records. No frozen object may be
edited while Round 3 is open; any content or status edit invalidates every
Round 3 verdict and requires a new blind round.

| Artifact | Review scope | SHA-256 |
|---|---|---|
| `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf` | complete controlling May 1996 report; source claims limited to the actual pages cited by the frozen records | `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA` |
| `handbook/parts/p09/presentations/n-c-013.tex` | whole-file identity; substantively lines 800--985, the complete twice-revised Thomas infinite-word presentation and its boundary | `23E73DA416CE583ADF084E1D16E4A5846AC9659E4ED0E937A1CB00FA0738AFED` |
| `handbook/parts/p09/presentations/n-c-014.tex` | whole-file identity; substantively lines 888--927 and 1451--1596, the finite-word and revised later infinite-tree Thomas passages plus their boundaries | `F9576BB10063037CDFD9018E6DC7DFB553651590FB74FC77D2D33EEBBF4D5915` |
| `handbook/parts/p09/logic-in-computer-science.tex` | complete shared Part IX file; especially source-role lines 25--42, word-automata lines 721--762, finite-word theorem lines 814--828, S2S boundary lines 843--846, and source guide lines 2348--2356 | `70CFEBC05E1F574703FA6F8B1367C2EBBA1A640A57B2DEEC8D144E88328A7117` |
| `handbook/bib/handbook.bib` | complete bibliography; especially `Thomas1996Report` and `Thomas1997` at lines 2346--2367 | `07233B0722E6DAE89AEE6B34F699BC980D54F4367C2672B4D3B92131F6D680AD` |
| `spec/research/p09-thomas-1996-report-source-note.md` | complete twice-revised identity, version, page, mathematical, correction, rights, and scope record | `F169CB0936EAA8CB650102A974FEE01F05C3E9D58774F7A198E2CEE35E2A7150` |
| `spec/research/p09-source-presentations-lot2-3.md` | complete compact record; especially `N-c-013.e`, `N-c-014.e`, and the consolidated open-status ledger | `C45908A389BB22FBB584672F9F78F1C0E45E7DDF274BC37039AEA9BC81ED281F` |

Every Round 3 reviewer must independently recompute all seven native
identities before substantive judgment and record the values in its report.

## Round 3 repair invariants

Every reviewer must dispose of `H01`--`H22` again on the complete revised
passages. It must also recheck `R2-01`--`R2-04`; historical status item `R2-05`
is superseded by `R3-03`. In addition, every reviewer must dispose expressly of
these three Round 3 invariants:

- **R3-01 -- total deterministic word transition.** Immediately after the
  general omega-run definition, the reader must give Thomas's total function
  `delta:Q x Sigma -> Q` and the unique-run equation. The deterministic Muller
  complement step must depend on this totality premise rather than on a merely
  partial functional relation. Controlling source: printed pp. 28 and 31.
- **R3-02 -- injective live-node naming.** At the actual first occurrence of
  the determinization-state name, the state must include a typed injective map
  from live nodes into `1,...,2n`, distinct from state-subset labels and marks.
  The initial root name, persistent surviving names, pairwise-distinct new
  names outside the entire predecessor name set, empty state's empty name set,
  reservoir argument, and exact `Ek,Fk` definitions must agree. The text must
  distinguish source content from handbook-owned definedness and normalization
  clauses. Controlling source: printed pp. 33--35.
- **R3-03 -- history, status, and source-object protocol.** The detailed and
  compact records must agree that Rounds 1 and 2 rejected, Round 3 is open, the
  registered 1997 chapter remains unreconciled, and no broader manuscript unit
  is admitted. Reviewers must read the actual frozen LaTeX. Derived PNG images
  are inert viewer aids, not source or manuscript review objects, and carry no
  independent evidence.

## Round 3 source use, independence, and filing

Round 3 uses three fresh reviewers with no inherited turn history. Each
reviewer must read the actual frozen LaTeX passages in full, together with the
actual frozen Markdown records needed by its seat. It must consult Thomas's
actual hash-pinned source PDF at the printed pages supporting every source
judgment. Printed pp. 28, 31, and 33--35 are mandatory for the two Round 3
repairs. No PNG or other derived page render is a review object or carries
independent evidentiary weight.

A reviewer may read only this charter, the seven Round 3 objects, and the
controlling PDF pages needed for its judgments. It may not read `ledger.md`,
`transcript/chair.md`, a Round 1 or Round 2 report, another Round 3 report,
another board or board transcript, conversation history, memory, staging
material, or web results. Reviewers may not contact one another.

The assigned files are:

- `transcript/r3-source-fidelity.md`;
- `transcript/r3-mathematical-proof.md`; and
- `transcript/r3-adversarial-publication.md`.

Each report must contain: the independently recomputed seven identities; an
explicit statement that the actual frozen `.tex` passages were read; the exact
source-PDF pages used; a disposition for every `H01`--`H22`, `R2-01`--`R2-04`,
and `R3-01`--`R3-03`; any findings with exact severity, identifier, file line,
printed source page, and repair requirement; and a concise seat-specific
rationale. The reviewer may write only its assigned report. Its final line must
be exactly `VERDICT: ACCEPT` or `VERDICT: REJECT --` followed by exact finding
identifiers.

Round 3 remains book scholarship. No test, test harness, automated checker,
repository script, TeX command, interim handbook build, handbook-PDF
inspection, or build is authorized.

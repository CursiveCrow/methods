# Round 1 source-fidelity review

## Review boundary and method

I reviewed only the chartered frozen Round 1 objects and the forty-four named
source renders. I did not consult the ledger, chair transcript, another review,
another board, memory, staging material, conversation history, or web results.

The hash-pinned 75-page PDF is the controlling source. I opened and read that
actual file directly at the required physical pages. The PNG files were also
inspected individually at original detail, but they were used only as derived
viewer/display aids; no formula, symbol, wording, pagination claim, or finding
rests independently on a PNG. Searchable manuscript text was used only to pin
the frozen line numbers after the corresponding printed PDF pages had been
read.

No test, test harness, automated checker, repository script, TeX command,
interim build, rendered-handbook inspection, handbook-PDF inspection, or build
was run or used as evidence.

## Independently recomputed native identities

I recomputed every identity with the platform's native SHA-256 facility before
making a substantive judgment.

| Frozen object | Recomputed SHA-256 | Disposition |
|---|---|---|
| `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf` | `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA` | exact match |
| `handbook/parts/p09/presentations/n-c-013.tex` | `76480DE7C2620521835DD1301B5D8B5698C60E14AA0B2EFA467D852F81BB36CA` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `F12CD5EDD8D160D91E9A2BC7B68056EF77AB8F2F6FFF5AD4EC474669059CF31B` | exact match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `70CFEBC05E1F574703FA6F8B1367C2EBBA1A640A57B2DEEC8D144E88328A7117` | exact match |
| `handbook/bib/handbook.bib` | `07233B0722E6DAE89AEE6B34F699BC980D54F4367C2672B4D3B92131F6D680AD` | exact match |
| `spec/research/p09-thomas-1996-report-source-note.md` | `B33BF77916C06C57F4896394B4A5569678D75B0B14A940FF451D68D4BD915FB8` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `45F8EB339A139C24251616F03A77715337F8E8B8F735956D35B05407D92637C7` | exact match |

The controlling PDF is 478,293 bytes. Its viewer reports 75 physical pages,
and physical page 75 visibly ends at printed page 72.

## Controlling-PDF and original-detail page attestation

I directly inspected the controlling PDF at physical pages 1--4, 11--15,
31--64, and 75. This covers each of the forty-four required physical pages in
the source object itself. I separately inspected all forty-four named PNG aids
at original detail:

- the five identity/page-map aids `inspect-title-01.png`,
  `inspect-title-02.png`, `inspect-title-03.png`,
  `inspect-body-start-04.png`, and `inspect-body-end-75.png`;
- `relevant-rendered/page-11.png` through `page-15.png`;
- `relevant-rendered/page-31.png` through `page-33.png`;
- `relevant-rendered/page-34.png` through `page-39.png`;
- `relevant-rendered/page-40.png` through `page-45.png`;
- `relevant-rendered/page-46.png`; and
- `relevant-rendered/page-47.png` through `page-64.png`.

The controlling PDF confirms the complete map recorded at
`spec/research/p09-thomas-1996-report-source-note.md:36-69`: physical 1 is the
title page, physical 2 the abstract, physical 3 the contents page numbered
`i`, physical 4 printed page 1, physical 11--15 printed pp. 8--12, physical
31--45 printed pp. 28--42, physical 46 printed p. 43, physical 47--64 printed
pp. 44--61, and physical 75 printed p. 72.

## Findings

### SF-01 — must-fix — the reader omits Thomas's finite-union characterization

**Frozen manuscript line and controlling page.**
`handbook/parts/p09/presentations/n-c-013.tex:841-848` moves directly from
Example 5.2 and Proposition 5.3 to the deterministic boundary. Thomas's
printed p. 30 (physical PDF p. 33) places between those topics the exact
characterization that an omega-language is Buechi-recognizable if and only if
it is a finite union of sets (U\cdot V^\omega), where (U) and (V) are
regular languages of finite words.

**Cross-record consequence.** The detailed record notices the claim at
`spec/research/p09-thomas-1996-report-source-note.md:131-134`, and the compact
record notices it at
`spec/research/p09-source-presentations-lot2-3.md:606-616`, but the frozen
reader passage does not contain it. The finite-union claim is an express H10
admission invariant, so adjacent coverage of Proposition 5.3 or the
deterministic-Buechi counterexample cannot substitute for it.

**Required repair.** In a new frozen round, insert the printed-p. 30
if-and-only-if statement between `n-c-013.tex:846` and `:848`, retaining all
three strength conditions: a *finite union*, factors (U,V) that are regular
finite-word languages, and the form (U\cdot V^\omega). Attribute the claim
to Thomas's May 1996 report at precursor strength. Update the compact
reader-facing completion language so that it expressly records the supplied
claim rather than merely the source's possession of it.

### SF-02 — must-fix — the tree-game proof applies a no-deadlock theorem to a potentially deadlocked automaton game

**Frozen manuscript lines and controlling pages.**
`handbook/parts/p09/presentations/n-c-014.tex:1454-1465` correctly reproduces
Definition 6.1 with an arbitrary relation

\[
\Delta\subseteq Q\times\Sigma\times Q\times Q,
\]

and imposes no totality condition. The passage at `n-c-014.tex:1500-1524`
then says that Automaton chooses a transition, identifies acceptance with a
winning strategy, and invokes the memoryless-determinacy proof without stating
what happens when no compatible transition exists.

The source itself exposes the unfilled premise: printed p. 44 defines the
possibly partial relation; printed pp. 47--48 describe the induced play as
infinite; printed p. 50 defines a game graph only when every vertex has a
nonempty finite outgoing-edge set; and printed p. 51 says the induced
automaton game is a game graph of that form before applying Theorem 6.13. No
completion or finite-loss convention appears on those controlling pages.

The one-state instance (Q=\{q_0\}), alphabet (\{a\}), and
(\Delta=\varnothing) is decisive. The all-(a) tree has no run, so the
automaton rejects it under Definition 6.1, while the alleged initial game
vertex has no outgoing move. That object does not satisfy the hypothesis of
the game theorem used in the proof. Consequently Remark 6.7, Theorems
6.8--6.9, and the downstream basis and MSO-negation applications are not
proved for the stated automaton type.

**Cross-record consequence.** The detailed account at
`spec/research/p09-thomas-1996-report-source-note.md:177-214` and the compact
account at `spec/research/p09-source-presentations-lot2-3.md:674-682` repeat the
partial transition type and the game architecture but do not disclose or
repair the missing premise. The latter nevertheless says that the complement
architecture has been reconstructed and every operative object stated before
use.

**Required repair.** In a new frozen round, add and prove an explicit
handbook-owned completion before Remark 6.7 is used. One exact repair is to add
a state \(\bot\); for every state-letter pair with no transition, add the
transition to \((\bot,\bot)\); and add \((\bot,a,\bot,\bot)\) for every input
letter. Keep the Muller family as subsets of the original state set, or in the
chain presentation keep \(\bot\) outside every \(F_i\), so a path trapped at
\(\bot\) rejects. Prove that this completion preserves the recognized tree
language and makes every Automaton position have a move. An equivalent
game-level losing absorbing state is acceptable if its language-preservation
and complement consequences are proved. The reader, detailed note, and compact
record must label this as a handbook-owned repair rather than source text.

## H01--H22 dispositions

- **H01 — PASS.** The actual PDF title page identifies Wolfgang Thomas,
  *Languages, Automata, and Logic*, Bericht 9607, Kiel, May 1996. Its native
  identity, 478,293-byte length, and 75-page extent agree with
  `p09-thomas-1996-report-source-note.md:24-47`, while the distinct report and
  chapter entries at `handbook.bib:2346-2367` and the reader boundaries at
  `n-c-013.tex:799-802,914-918` and `n-c-014.tex:1550-1555` correctly preserve
  precursor standing. Controlling source: unnumbered title and abstract pages.

- **H02 — PASS.** The abstract's literal prospective *Handbook of Formal
  Language Theory* wording is visibly distinct from the final *Handbook of
  Formal Languages* identity. The distinction is exact at
  `p09-thomas-1996-report-source-note.md:71-90`, `handbook.bib:2358-2366`, and
  `logic-in-computer-science.tex:2348-2356`. Controlling source: unnumbered
  abstract page (physical p. 2).

- **H03 — PASS.** The physical/printed map and all claimed ranges agree with
  the controlling PDF. The manuscript locators at `n-c-014.tex:901,918,
  1476,1498,1524,1535,1548` and the section locators at
  `n-c-013.tex:846,855,890,912` resolve to the stated report sections and do
  not assert final-chapter pagination. Controlling source: physical pp. 1--4,
  11--15, 31--64, and 75.

- **H04 — PASS.** `p09-thomas-1996-report-source-note.md:244-249` records only
  public university-course access, expressly declines to infer a Creative
  Commons or blanket republication licence, and keeps the PDF/renders as
  research evidence. No frozen reader passage promotes them to handbook
  assets. Controlling source: all inspected report pages, on which no such
  licence was displayed.

- **H05 — PASS.** `n-c-014.tex:888-901` gives the typed finite-word tuple,
  three-place transition relation, (n+1)-state run, initial and final
  conditions, and effective two-way Theorem 3.1 strength exactly. Controlling
  source: printed p. 8.

- **H06 — PASS.** `n-c-014.tex:903-913` retains the disjoint run tracks,
  separate last-letter transition, empty-word existence guard, the four stated
  `MSO0` atomic forms, and complement/union/projection induction. Controlling
  source: printed pp. 8--9.

- **H07 — PASS.** `n-c-014.tex:914-918` limits `WS1S` monadic variables to
  finite sets, uses input-free successful-run existence, and states only the
  reversed-binary finite-carry Presburger route supported by the report.
  Controlling source: printed pp. 10--12.

- **H08 — PASS.** `n-c-013.tex:799-820` types the finite state set, alphabet,
  initial state, three-place omega transition relation, run, acceptance
  component, and `In(r)` before use and keeps this a word automaton.
  Controlling source: printed p. 28.

- **H09 — PASS.** `n-c-013.tex:821-846` gives the Buechi, Muller, Rabin, and
  Streett modes with Thomas's exact pair order. In particular, recurrence of
  an (F_i)-state implies recurrence of an (E_i)-state. Example 5.2 and
  Proposition 5.3 retain their source roles. Controlling source: printed
  pp. 28--29.

- **H10 — REJECT (SF-01).** `n-c-013.tex:841-848` omits the required
  finite-union (U\cdot V^\omega) if-and-only-if characterization from
  printed p. 30. The Example 5.2/Proposition 5.3 comparison and deterministic
  boundary at `n-c-013.tex:841-855` are otherwise source-faithful.
  Controlling source: printed pp. 29--31.

- **H11 — PASS.** At first use, `n-c-013.tex:857-865` explains why a subset is
  insufficient, exactly defines the finite ordered state-subset tree with
  disjoint siblings, proper child-union containment, and marking, fixes its
  standing as a determinization state rather than input tree or run, and then
  uses it. The required necessity, definition, standing, nonredundancy, and use
  are colocated. Controlling source: printed pp. 31--32.

- **H12 — PASS.** `n-c-013.tex:864-879` preserves the initial root, youngest
  accepting children, advancement of old and new labels, horizontal deletion,
  vertical collapse/marking, surviving-name persistence, preceding-tree
  freshness rule, (n)-live-node bound, and (1,\ldots,2n) reservoir in the
  source order. Controlling source: printed pp. 32--35.

- **H13 — PASS.** `n-c-013.tex:879-890` retains eventual persistence plus
  infinite marking, the absence/marked-presence Rabin pairs, both proof
  directions, the (2^{O(n\log n)}) state and displayed (2n)-pair bounds,
  and the qualified factorial lower-bound consequence without an
  exact-constant claim. Controlling source: printed pp. 34--37.

- **H14 — PASS.** `n-c-013.tex:892-901` retains Theorem 5.9's effective
  equivalence, visibly identifies the printed Corollary 5.10 omission, and
  labels the reachable nonempty cycle meeting (F) as a handbook-owned repair.
  It therefore rejects nonaccepting reachable cycles. Controlling source:
  printed pp. 37--38, with the defect on p. 38.

- **H15 — PASS.** `n-c-013.tex:901-912` gives the finite disjunction of
  eventual-absence and recurring-presence clauses, restricts every inner
  quantifier below the current (y), and defines weak MSO by finite-set-valued
  monadic variables. Controlling source: printed pp. 38--39.

- **H16 — PASS.** `n-c-014.tex:1454-1476` exactly gives the four-place tree
  transition relation, one global run with root and two-child equations, and
  the existential-run/universal-path Muller condition. Examples 6.2--6.3 are
  used only for the Buechi/Muller separation. The possible absence of a run is
  correctly rejecting at this definitional level; SF-02 concerns the later
  game reduction. Controlling source: printed pp. 44--45.

- **H17 — PASS.** `n-c-014.tex:1478-1498` gives the strict chain, exact path
  condition, permutation-plus-prior-position memory, its automaton-state
  standing, and Remark 6.6's recovery use. The displayed pair condition, not
  an unstated total priority map, controls acceptance: states outside the last
  displayed (F_m) cannot by themselves supply the required recurring
  (F_i)-state. Controlling source: printed pp. 45--47.

- **H18 — REJECT (SF-02).** The move order, acceptance equivalence, and
  current-position meaning of memorylessness are faithfully stated at
  `n-c-014.tex:1500-1507`, but the arbitrary transition type at
  `n-c-014.tex:1454-1465` permits an Automaton position with no move. The
  no-deadlock premise needed for Theorem 6.8 is absent. Controlling source:
  printed pp. 44, 47--48, and 50--51.

- **H19 — REJECT (SF-02).** The local direction functions, finite strategy
  labels, word-automaton closure, all-path deterministic Muller tree check,
  nondeterministic label guess, and input-tree independence at
  `n-c-014.tex:1507-1519` match printed pp. 49--50. Their use as a proof for the
  stated partial automaton type remains invalid until the deadlock completion
  is supplied.

- **H20 — REJECT (SF-02).** The forced-finite-visit/complementary-subgame
  summary, finite-game effectivity, regular generator, input guessing, and
  regular-member conclusion at `n-c-014.tex:1519-1535` faithfully track printed
  pp. 51--57. However, the application of those game theorems has not
  established their nonempty-outgoing-edge hypothesis for the automaton game,
  so the frozen proof chain is incomplete at its entry point.

- **H21 — REJECT (SF-02).** `n-c-014.tex:1537-1555` correctly states the
  atomic/disjunction/existential/complement route, converse run/path shape,
  input-free decision, S2S conclusion, and the later, non-substitutive Thomas
  boundary. The negation step nevertheless depends on the unqualified
  complementation theorem affected by SF-02. Controlling source: printed
  pp. 57--59 for the translation and S2S route, with the later-route boundary
  already explicit on printed p. 43.

- **H22 — REJECT (SF-01, SF-02).** The distinct bibliography identities at
  `handbook.bib:2346-2367`, shared source roles at
  `logic-in-computer-science.tex:25-42,721-762,814-828,843-846,2348-2356`, page
  map, rights boundary, historical ownership, and final-chapter open status
  agree. Cross-file completion does not: the detailed and compact records know
  the printed-p. 30 finite-union result that the reader omits, and the reader,
  detailed note, and compact record all omit the handbook-owned deadlock repair
  while claiming the game/complement reconstruction is supplied. The only
  possible admission remains the two report-precursor passages on these frozen
  hashes; no broader completion is inferred.

## Seat-specific rationale

The actual report, not a render or searchable surrogate, supports the frozen
identity, version boundary, page map, finite-word proof, four omega acceptance
modes, Streett convention, Safra construction, printed-cycle correction,
tree-chain memory, regular-tree basis architecture, S2S route, rights boundary,
and later/non-Rabin historical standing. The five-part terminology rule is met
at the actual first uses of the Safra determinization state, order-vector with
hit, memoryless strategy, and regular tree.

The empty-word guard, empty acceptance data, missing-run semantics, duplicate
Safra states, deletion and name reuse, transient names, nonaccepting cycles,
states outside the displayed chain, and empty-language qualification do not
produce an additional finding. The no-available-transition stress test does:
it makes the invoked game theorem inapplicable without an explicit completion.
Together with the literal omission of the printed-p. 30 finite-union theorem,
that leaves two unresolved must-fix findings on the unchanged snapshot.

VERDICT: REJECT -- SF-01, SF-02

# Round 2 source-fidelity report

## Review boundary and source use

I reviewed only the Round 2 charter, the seven frozen Round 2 objects, and the
pages of the controlling hash-pinned Thomas PDF identified below. I did not use
another review report, another board or transcript, retained PNG/source renders,
staging material, conversation history, memory, or web results. I did not use a
test, test harness, automated checker, repository script, TeX command, build,
manuscript-PDF inspection, or rendered-handbook inspection as evidence.

I read the actual frozen LaTeX passages themselves, not a rendered handbook:

- `handbook/parts/p09/presentations/n-c-013.tex`, including the complete revised
  Thomas passage and boundary at lines 800--956 and the immediately preceding
  no-transfer boundary at lines 780--799;
- `handbook/parts/p09/presentations/n-c-014.tex`, including the complete Thomas
  finite-word passage and boundary at lines 888--927 and the complete revised
  later infinite-tree passage and boundary at lines 1451--1596;
- the complete frozen `handbook/parts/p09/logic-in-computer-science.tex`, with
  particular attention to its source-role, word-automata, finite-word theorem,
  `S2S`, presentation-inclusion, and source-guide passages; and
- the `Thomas1996Report` and `Thomas1997` bibliography records, the complete
  detailed Thomas source note, and the compact record's governing evidence
  rules, Thomas entries, neighboring Thomas/Rabin nonconflation boundary, and
  consolidated open-status ledger.

I consulted the controlling PDF itself at the following exact pages. No retained
page render was opened or given evidentiary standing.

- Physical pages 1--4 and 75: title page; abstract; contents page numbered `i`;
  printed p. 1; and final printed p. 72.
- Physical pages 11--15, corresponding to printed pp. 8--12: Section 3.1.
- Physical pages 31--45, corresponding to printed pp. 28--42: Sections
  5.1--5.3.
- Physical pages 46--64, corresponding to printed pp. 43--61: the Chapter 6
  introduction and Sections 6.1--6.3.

This includes every mandatory repair locator: printed p. 30; printed pp. 28 and
34--35; and printed pp. 44 and 47--51.

## Independently recomputed native identities

I recomputed all seven SHA-256 identities natively before substantive judgment
and rechecked them before filing. Each recomputed value equals the charter's
frozen value.

| Frozen artifact | Bytes | Independently recomputed SHA-256 | Disposition |
|---|---:|---|---|
| `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf` | 478,293 | `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA` | match |
| `handbook/parts/p09/presentations/n-c-013.tex` | 44,828 | `F3473BB8C2D77A56D82C7086888CD9087AE887847ED3FDA021DC6826868C25E3` | match |
| `handbook/parts/p09/presentations/n-c-014.tex` | 77,495 | `F9576BB10063037CDFD9018E6DC7DFB553651590FB74FC77D2D33EEBBF4D5915` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | 119,580 | `70CFEBC05E1F574703FA6F8B1367C2EBBA1A640A57B2DEEC8D144E88328A7117` | match |
| `handbook/bib/handbook.bib` | 207,104 | `07233B0722E6DAE89AEE6B34F699BC980D54F4367C2672B4D3B92131F6D680AD` | match |
| `spec/research/p09-thomas-1996-report-source-note.md` | 18,049 | `3F63E37FE1E7C72140080302E3BDFA716D617A8E73BA157F0D12977041093681` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | 232,808 | `B43F11B230E9CFF763CAE106A91CDA29122305B02F4CA621E60BD4E63D253208` | match |

## Charter dispositions

### Identity, finite words, and infinite words

- **H01 -- PASS.** The PDF is the complete 75-physical-page, 478,293-byte May
  1996 Kiel report by Wolfgang Thomas, *Languages, Automata, and Logic*, Bericht
  9607. The title page and terminal pagination confirm the object. Every frozen
  record treats it as a report precursor rather than as a verified facsimile of
  the registered 1997 chapter.

- **H02 -- PASS.** The abstract on physical p. 2 literally anticipates a
  modified version for the *Handbook of Formal Language Theory*. The detailed
  note and manuscript keep that prospective title distinct from the registered
  1997 *Handbook of Formal Languages* identity; the two bibliography entries
  likewise remain separate.

- **H03 -- PASS.** The physical/printed page map agrees with the PDF: physical
  pp. 11--15 are printed pp. 8--12, physical pp. 31--45 are printed pp. 28--42,
  and physical pp. 46--64 are printed pp. 43--61. The section boundaries and
  every manuscript locator used for Sections 3.1, 5.1--5.3, and 6.1--6.3 agree
  with the contents and page bodies. No locator is assigned to the uninspected
  final chapter.

- **H04 -- PASS.** The frozen record makes the conservative rights claim: the
  university-course route is public access, not a Creative Commons or blanket
  republication licence. It calls the PDF research evidence and expressly says
  that derived page images are disposable viewer aids, carry no independent
  evidentiary weight, and are not handbook assets. The earlier render inventory
  does not override that explicit evidentiary boundary, and I did not use those
  retained files.

- **H05 -- PASS.** `n-c-014.tex:888--901` accurately gives the finite-word tuple
  `(Q, Sigma, q_0, Delta, F)`, the three-place transition relation, an
  `n+1`-state run on an `n`-letter word, its initial and final clauses, and the
  effective two-way strength of Theorem 3.1. These agree with printed p. 8.

- **H06 -- PASS.** `n-c-014.tex:903--913` preserves the pairwise-disjoint state
  tracks, the separately checked transition on the last letter, and the
  empty-word existence guard from printed pp. 8--9. Its `MSO_0` atomic forms are
  exactly subset, singleton, successor, and letter-track inclusion; complement,
  union, and bit-track projection have the correct logical roles.

- **H07 -- PASS.** `n-c-014.tex:914--918` restricts weak monadic variables to
  finite sets, uses successful-run existence for the input-free finite
  automaton, and records only the reversed-binary/finite-carry Presburger route
  supported on printed pp. 10--12. It does not add a stronger consequence.

- **H08 -- PASS.** `n-c-013.tex:800--821` types the finite state set, alphabet,
  initial state, three-place transition relation, acceptance component, infinite
  run, and `In(r)` before using any acceptance condition. The standing is
  explicitly that of an infinite-word automaton.

- **H09 -- PASS.** `n-c-013.tex:822--847` gives the four source-specific
  conditions correctly. In particular, Thomas's Streett ordering is
  `In(r) intersect E_i != empty` or `In(r) intersect F_i = empty`, so recurrence
  in `F_i` entails recurrence in `E_i`. Example 5.2 and Proposition 5.3 have the
  exact comparison role supported by printed pp. 28--29.

- **H10 -- PASS.** `n-c-013.tex:849--870` states the exact finite-union
  `U_j V_j^omega` characterization with regular finite-word factors, the
  deterministic-Buechi complement counterexample, deterministic-Muller
  complementation, and McNaughton's effective conversion at the strengths and
  ownership shown on printed pp. 30--31. The finite-union theorem is explicitly
  Thomas's report-level survey statement rather than an original-priority
  claim.

- **H11 -- PASS.** The first manuscript occurrence of the technical name is the
  five-part introduction at `n-c-013.tex:872--879`. Necessity is the failure of
  a reachable-state subset to preserve one recurring lineage; the eliminable
  definition is the finite ordered tree of state subsets with disjoint siblings,
  proper child-union containment, and optional breakpoint mark; its standing is
  a determinized word-automaton state; its nonredundancy is stated against both
  subset states and input-tree/run objects; and the initial state and update use
  it immediately. The term is not introduced in the preceding Safra-source-gap
  paragraph.

- **H12 -- PASS.** `n-c-013.tex:879--910` preserves the source update order:
  initial `{q_0}` root; youngest `R intersect F` children; advancement of every
  label including new children; horizontal deletion; then vertical collapse
  and current-update marking. Surviving names persist, new names are absent from
  the preceding tree, no more than `n` nodes are live, and `1,...,2n` is the
  reservoir. The handbook-owned clearing and empty-root clauses are labeled as
  such rather than attributed to the report.

- **H13 -- PASS.** `n-c-013.tex:907--928` gives eventual name persistence plus
  infinitely many marks, the absence/marked-presence Rabin pairs, both
  acceptance-proof directions, the `2^{O(n log n)}` state bound and exactly
  `2n` displayed pairs, and the qualified lower-bound consequence from
  Theorems 5.7--5.8. The text does not turn that lower bound into an
  exact-constant claim or assign original Safra/McNaughton priority to Thomas.

- **H14 -- PASS.** `n-c-013.tex:930--939` retains the effective two-way strength
  of Theorem 5.9. The printed Corollary 5.10 error is visible on printed p. 38:
  its stated reachable-cycle test omits Buechi acceptance. The manuscript gives
  the sound criterion, a reachable nonempty cycle containing an `F` state, and
  labels that criterion a handbook-owned repair without changing the decision
  theorem.

- **H15 -- PASS.** `n-c-013.tex:939--950` preserves Proposition 5.11's finite
  disjunction of eventual-absence and recurring-presence clauses and says that
  the quantifiers internal to the component formulae are restricted below the
  current `y`. It also defines Corollary 5.12's weak monadic range as finite
  sets, in agreement with printed pp. 39--40.

### Infinite trees and cross-file standing

- **H16 -- PASS.** `n-c-014.tex:1451--1476` accurately gives Definition 6.1's
  four-place transition relation, one global state-labelling run, root and two
  child equations, and successful acceptance with prefix `exists run, for all
  paths`. Examples 6.2--6.3 are used only for the Buechi/Muller tree-language
  separation supported by printed pp. 44--45.

- **H17 -- PASS.** `n-c-014.tex:1478--1498` gives Definition 6.4's strictly
  increasing chain and exact path condition. Its `order-vector with hit` is
  defined as a permutation of `Q` ordered by last appearance together with the
  former position of the newly visited state. The text gives it finite
  automaton-memory standing, distinguishes it from an input tree and path, and
  identifies Remark 6.6's recovery of the recurrent-state set as the use that
  makes the memory nonredundant. This agrees with printed pp. 45--47.

- **H18 -- PASS.** After the totalizing completion, `n-c-014.tex:1531--1541`
  preserves the Automaton-then-Pathfinder move order and Remark 6.7's acceptance
  equivalence. It defines a memoryless strategy as a choice depending only on
  the current game position before applying Theorem 6.8.

- **H19 -- PASS.** `n-c-014.tex:1541--1555` follows Theorem 6.9's proof
  architecture on printed pp. 49--50. Pathfinder's finite local labels are
  functions `Sigma x Delta -> {0,1}`; a labelled tree records them; word-
  automaton negation/projection universally handles transition choices along a
  path; a deterministic Muller tree automaton handles all paths; and
  nondeterminism guesses only the local labels. The constructed complement is
  explicitly independent of the particular input tree and, through the prior
  language-preserving completion, complements the original partial automaton.

- **H20 -- PASS.** `n-c-014.tex:1555--1574` separately identifies Theorem
  6.13's forced-finite-visit/complementary-subgame induction, Theorem 6.16's
  finite-game effectivity, Definition 6.17's finite direction automaton with an
  output map, and Theorem 6.18's input guessing, completed finite game,
  memoryless strategy, effective emptiness, and accepted regular-member result.
  These roles agree with printed pp. 50--57.

- **H21 -- PASS.** `n-c-014.tex:1576--1596` gives Theorem 6.19's atomic,
  disjunction, existential-projection, and complement steps; the converse
  existential-run/universal-path set-quantifier shape; and Theorem 6.20's
  input-free successful-run decision route. It repeatedly propagates the
  completion. The closing boundary explicitly says that this is Thomas's later
  game/basis route, not Rabin's Section 3.12 proof, and neither reopens nor
  alters the separate Rabin admission.

- **H22 -- PASS.** The two bibliography entries, manuscript passages, complete
  shared Part IX text, detailed note, relevant compact-record entries, page
  locators, correction ownership, technical terminology, and status language
  agree. The detailed note and compact record both say that Round 1 rejected
  five defects, the repaired unchanged-snapshot review and admission remain
  open, and the registered 1997 chapter remains uninspected and unreconciled.
  Part IX keeps the report precursor and final chapter distinct and continues
  to assign the historical infinite-tree theorem to Rabin. This disposition is
  limited to the two Thomas report-precursor presentations on the seven frozen
  hashes; it makes no claim about Part IX completion, a build, the rendered
  handbook, the 1997 chapter body, another source presentation, human review,
  or the book.

## Round 2 repair-invariant dispositions

- **R2-01 -- PASS.** `n-c-013.tex:849--861` states
  `L = union_{j<k} U_j V_j^omega`, requires regular `U_j,V_j subseteq
  Sigma^*`, and defines `V^omega` by an infinite factor sequence whose partial
  concatenation lengths tend to infinity. Empty factors therefore cannot
  manufacture a finite result and can be deleted. The statement is explicitly
  a report-precursor survey claim. This matches printed p. 30.

- **R2-02 -- PASS.** `n-c-013.tex:896--917` defines the empty successor as one
  unmarked, absorbing determinized word-automaton state with no root, node,
  name, label, or mark. It proves that an empty advanced root means that no
  original run extends the prefix and no continuation can restore one; the
  state lies in every absence component and no marked-presence component. It
  has zero live nodes, consumes no name, adds no pair, and changes neither the
  asymptotic state bound nor the exact pair count. The text labels this a
  handbook-owned completion of the gap visible on printed pp. 28 and 34.

- **R2-03 -- PASS.** `n-c-013.tex:880--885, 911--923` clears predecessor marks,
  permits only a collapse in the current letter update to mark the successor,
  and bases acceptance on infinitely many distinct current collapse events on
  a persistent lineage. Its explicit one-breakpoint
  `q_0 -a-> f -b-> s -b-> s` example shows why retaining a mark would falsely
  accept `a b^omega` and why current-update marking rejects it. The
  clarification is correctly identified as handbook-owned relative to the gap
  on printed pp. 34--35.

- **R2-04 -- PASS.** `n-c-014.tex:1500--1529` defines
  `Delta(q,a)`, chooses a fresh `bottom` outside `Q`, preserves the original
  strict chain as subsets of `Q union {bottom}`, sends precisely missing
  state-letter cases to `(bottom,bottom)`, and loops `bottom` on each letter.
  Every original run remains, while any run using an added transition has a
  path thereafter constant at `bottom` and fails every pair because `bottom`
  lies in no `F_i`. Thus the language and strict chain are unchanged. The text
  establishes a nonempty finite Automaton choice set and two Pathfinder branch
  moves, then propagates completion through complementation
  (`1531--1555`), the finite game (`1555--1562`), the regular-tree basis route
  (`1564--1574`), and `S2S` (`1576--1586`). The completion is explicitly
  handbook-owned and exactly repairs the gap on printed pp. 44 and 47--51.

- **R2-05 -- PASS.** The first manuscript occurrence of `Safra tree` is its
  necessity/definition/standing/nonredundancy/use introduction at
  `n-c-013.tex:872--879`; the preceding Safra paragraph deliberately leaves the
  unread 1988 state object unnamed. The detailed note, both compact Thomas
  entries, and consolidated ledger agree that Round 1 rejected five defects,
  the repairs await this fresh unchanged-hash round, the final 1997 chapter is
  unreconciled, and no unit broader than the two bounded May 1996
  report-precursor presentations is eligible for admission.

## Findings

None. I found no source-critical, must-fix, or advisory defect within the frozen
Round 2 admission boundary. Accordingly there is no finding identifier, file
line, printed source page, or repair requirement to report.

## Source-fidelity rationale

Every source-attributed mathematical claim in the two revised Thomas passages
is supported at its cited location in the controlling May 1996 report. The
finite-union theorem restores source content rather than importing priority;
the empty Safra successor, current-event mark lifetime, accepting-cycle
criterion, and rejecting tree-transition completion are genuine manuscript
repairs to source gaps and are consistently labeled handbook-owned. Their
definitions, standings, nonredundancy, and uses are supplied where needed.
Version identity, pagination, Thomas-versus-original-source ownership, and the
Thomas-versus-Rabin proof boundary remain consistent across the manuscript,
bibliography, shared Part IX text, detailed source note, and compact record.

VERDICT: ACCEPT

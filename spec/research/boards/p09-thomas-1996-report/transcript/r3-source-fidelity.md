# Round 3 source-fidelity report

## Review scope and evidence used

I conducted this as a fresh blind source-fidelity review. I read the charter
completely before substantive review. I then read the actual frozen Thomas
passages in `n-c-013.tex` (lines 800--985) and `n-c-014.tex` (lines 888--927
and 1451--1596) in full, the Thomas-relevant passages in the shared Part IX
file and bibliography, and both frozen Markdown records directly. I did not
read a prior-round report, another Round 3 report, the ledger, the chair
transcript, another board, memory, staging material, or web results, and I did
not contact another reviewer.

I consulted the controlling hash-pinned PDF itself at physical pages 1--4 and
75 for identity and pagination; printed pp. 8--12 for Section 3.1; printed
pp. 28--42 for Sections 5.1--5.3; and printed pp. 43--61 for the Chapter 6
introduction and Sections 6.1--6.3. Thus the PDF comparison included the
mandatory printed pp. 28, 31, and 33--35. I inspected no PNG or other derived
page object. I ran no test, test harness, checker, repository script, TeX
command, build, manuscript-PDF inspection, or rendered-handbook inspection.

## Independently recomputed native identities

All seven values match the Round 3 charter exactly.

| Frozen object | Independently recomputed SHA-256 |
|---|---|
| `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf` | `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA` |
| `handbook/parts/p09/presentations/n-c-013.tex` | `23E73DA416CE583ADF084E1D16E4A5846AC9659E4ED0E937A1CB00FA0738AFED` |
| `handbook/parts/p09/presentations/n-c-014.tex` | `F9576BB10063037CDFD9018E6DC7DFB553651590FB74FC77D2D33EEBBF4D5915` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `70CFEBC05E1F574703FA6F8B1367C2EBBA1A640A57B2DEEC8D144E88328A7117` |
| `handbook/bib/handbook.bib` | `07233B0722E6DAE89AEE6B34F699BC980D54F4367C2672B4D3B92131F6D680AD` |
| `spec/research/p09-thomas-1996-report-source-note.md` | `F169CB0936EAA8CB650102A974FEE01F05C3E9D58774F7A198E2CEE35E2A7150` |
| `spec/research/p09-source-presentations-lot2-3.md` | `C45908A389BB22FBB584672F9F78F1C0E45E7DDF274BC37039AEA9BC81ED281F` |

The PDF is 478,293 bytes and has 75 physical pages. Its title page identifies
Wolfgang Thomas, *Languages, Automata, and Logic*, May 1996, Bericht 9607,
Kiel. Physical page 3 is the contents page numbered `i`; physical page 4 is
printed p. 1; and physical page 75 is printed p. 72.

## Findings

No source-fidelity finding is supported on the frozen Round 3 snapshot. I
assign no blocker, must-fix, should-fix, consider, discard, or unresolved-user
identifier.

## Mandatory invariant dispositions

- **H01 -- PASS.** The native PDF identity, byte length, physical extent,
  author, title, report number, institution, place, and May 1996 date agree
  with the title page and with
  `p09-thomas-1996-report-source-note.md:5--41`. The note and
  `handbook.bib:2346--2367` keep the acquired report precursor distinct from
  the registered 1997 chapter.

- **H02 -- PASS.** The PDF abstract literally anticipates a chapter in the
  *Handbook of Formal Language Theory*. The note at lines 73--82 and the
  bibliography's distinct `Thomas1997` entry preserve the eventual title
  *Handbook of Formal Languages* rather than normalizing the prospective
  wording.

- **H03 -- PASS.** The contents page, first numbered page, last numbered page,
  and every relied-on printed page agree with the physical-to-printed offset
  recorded at `p09-thomas-1996-report-source-note.md:36--61`. The manuscript
  locators are report locators: Section 3.1 at printed pp. 8--12, Sections
  5.1--5.3 at printed pp. 28--42, and the Chapter 6 material at printed
  pp. 43--61. Neither manuscript passage assigns a locator to an inspected
  final-chapter body.

- **H04 -- PASS.** `p09-thomas-1996-report-source-note.md:24--47,63--71,
  316--322` distinguishes public course access from a licence, treats the PDF
  as research evidence, and gives derived images no independent evidentiary or
  asset standing. The compact record makes no contrary rights claim.

- **H05 -- PASS.** At `n-c-014.tex:888--901`, the renamed tuple
  `(Q,\Sigma,q_0,\Delta,F)`, the type
  `\Delta\subseteq Q\times\Sigma\times Q`, the length-`n+1` state sequence,
  initial and transition equations, final-state test, and effective two-way
  Theorem 3.1 strength agree with printed p. 8.

- **H06 -- PASS.** `n-c-014.tex:903--913` accurately records the disjoint state
  tracks, separate final-letter transition, empty-word existence guard, exact
  `MSO_0` atomic forms, and complement/union/projection induction on printed
  pp. 8--9.

- **H07 -- PASS.** `n-c-014.tex:914--918` keeps weak monadic variables
  finite-set-valued, makes truth of the closed sentence successful-run
  existence for an input-free finite automaton, and limits the reversed-binary
  Presburger discussion to the finite-carry route actually given on printed
  pp. 10--12.

- **H08 -- PASS.** `n-c-013.tex:800--821` gives Definition 5.1's finite state
  and alphabet data, initial state, typed transition relation, infinite run,
  and `In(r)` before using any acceptance condition, matching printed p. 28.

- **H09 -- PASS.** `n-c-013.tex:833--853` gives all four acceptance modes with
  the report's pair order. In particular its Streett formula is
  `In(r)\cap E_i\ne\varnothing` or `In(r)\cap F_i=\varnothing`, so recurrence
  in `F_i` implies recurrence in `E_i`, exactly as on printed pp. 28--29.

- **H10 -- PASS.** `n-c-013.tex:853--881` preserves Example 5.2,
  Proposition 5.3's nondeterministic equivalence, the finite union of regular
  `U_jV_j^\omega` factors, the unbounded-total-length meaning of infinite
  concatenation, the deterministic-Buechi complement counterexample, and
  deterministic-Muller complementation at the strengths on printed
  pp. 29--31. It calls the finite-union statement report-level survey evidence,
  not original-priority evidence.

- **H11 -- PASS.** The actual first manuscript occurrence at
  `n-c-013.tex:883--896` explains why reachable-state subsets are insufficient,
  defines the finite rooted ordered tuple `(T,\ell,\nu,M)`, types each
  component, distinguishes this determinization state from an input tree and
  a Rabin-tree-automaton run, distinguishes names from labels and marks, and
  points to persistence and the Rabin pairs as the later use. This agrees with
  the construction's role on printed pp. 31 and 33.

- **H12 -- PASS.** `n-c-013.tex:897--934` has the single `{q_0}` root, the
  disclosed handbook normalization name `1`, persistent surviving names,
  current-event marks, and the source order: youngest `R\cap F` children;
  advancement of every label including new children; horizontal deletion and
  empty-node removal; then vertical collapse and marking. New names are
  pairwise distinct and outside the whole predecessor name set. The live-node
  bound `n` and reservoir `1,\ldots,2n` agree with printed pp. 33--35.

- **H13 -- PASS.** `n-c-013.tex:934--958` accurately states eventual name
  persistence plus infinitely many marks, defines the `(E_k,F_k)`
  absence/marked-presence pairs, records both acceptance directions, and gives
  `2^{O(n\log n)}` states and exactly `2n` pairs for the displayed
  construction. Its Theorems 5.7--5.8 wording retains the no-general-
  `2^{O(n)}`/`O(n)` qualifier and factorial complementation family from
  printed pp. 35--37.

- **H14 -- PASS.** `n-c-013.tex:960--969` keeps Theorem 5.9 effective in both
  directions and exposes Corollary 5.10's printed p. 38 defect. The reachable
  nonempty cycle meeting the Buechi set `F` is expressly a handbook-owned
  correction, not a quotation from the report.

- **H15 -- PASS.** `n-c-013.tex:969--980` reproduces Proposition 5.11 as a
  finite disjunction of eventual-absence and recurring-presence clauses, with
  every inner quantifier bounded below the current `y`, and defines weak MSO as
  finite-set monadic quantification, matching printed pp. 38--39.

- **H16 -- PASS.** `n-c-014.tex:1451--1476` gives Definition 6.1's four-place
  transition relation, one global run with root and two-child equations, and
  the exact `\exists r\,\forall\pi` Muller condition on printed pp. 43--44.
  Its Examples 6.2--6.3 claim only the complementary-language Buechi/Muller
  separation established on printed pp. 44--45.

- **H17 -- PASS.** `n-c-014.tex:1478--1498` gives the strict chain and exact
  path pair condition on printed pp. 45--47. At its first occurrence, the
  order-vector with hit is defined as a permutation plus the previous position
  of the newly visited state, typed as added finite automaton-state memory,
  distinguished from inputs and paths, and made nonredundant by Remark 6.6's
  recovery of the recurring-state set.

- **H18 -- PASS.** `n-c-014.tex:1531--1542` preserves the Automaton-then-
  Pathfinder move order, Remark 6.7's acceptance equivalence, and the local
  current-position definition of memorylessness before Theorem 6.8 is applied,
  matching printed pp. 47--49.

- **H19 -- PASS.** `n-c-014.tex:1541--1555` follows printed pp. 49--50:
  Pathfinder's local direction functions form a finite-label strategy tree;
  sequential word-automaton closure universally handles compatible transition
  choices on one path; a deterministic Muller tree automaton handles every
  path; and nondeterminism guesses only the local labels. The complement
  automaton is explicitly independent of the particular input tree.

- **H20 -- PASS.** `n-c-014.tex:1555--1574` separates Theorem 6.13's
  forced-finite-visit/complementary-subgame induction, Theorem 6.16's effective
  finite-game result, Definition 6.17's finite direction generator with output,
  and Theorem 6.18's input guessing, finite game, memoryless strategy,
  decidable emptiness, and regular-member conclusion, agreeing with printed
  pp. 50--57.

- **H21 -- PASS.** `n-c-014.tex:1576--1596` preserves Theorem 6.19's atomic,
  disjunction, existential-track, and complement steps; the converse
  existential-run/universal-path formula shape; and Theorem 6.20's input-free
  decision route on printed pp. 57--59. Lines 1591--1596 keep this later Thomas
  route separate from Rabin's Section 3.12 proof. Correspondingly,
  `logic-in-computer-science.tex:843--846` continues to state the public S2S
  theorem under Rabin's authority.

- **H22 -- PASS.** The two presentation passages, shared source-standing text
  (`logic-in-computer-science.tex:25--42,721--762,814--846,2348--2356`),
  bibliography (`handbook.bib:2346--2367`), detailed note, and compact record
  agree on report identity, source terminology, proof and correction ownership,
  page locators, later-versus-original proof standing, and the unreconciled
  1997 boundary. `p09-thomas-1996-report-source-note.md:324--352` and
  `p09-source-presentations-lot2-3.md:606--616,674--682,902--918` keep both
  Thomas presentations and every broader unit unadmitted while Round 3 is open.

## Round 2 repair-invariant dispositions

- **R2-01 -- PASS.** `n-c-013.tex:860--872` states a finite union, requires
  regular finite-word `U_j,V_j`, defines `V^\omega` by unbounded cumulative
  length, handles empty factors, and limits ownership to Thomas's report-level
  survey statement. Printed p. 30 supports the source-carried portion.

- **R2-02 -- PASS.** `n-c-013.tex:915--925,942--947` defines one empty,
  unmarked, absorbing state with no node, label, name, or mark when root
  advancement is empty; proves that no original run can be restored; includes
  the state in every `E_k` and no `F_k`; and preserves the live-node, name,
  state-asymptotic, and pair bounds. It is visibly handbook-owned completion of
  the gap exposed by printed pp. 28 and 34.

- **R2-03 -- PASS.** `n-c-013.tex:899--905,926--953` clears predecessor marks,
  permits only current-update collapses to mark the successor, bases acceptance
  on infinitely many distinct collapse events, and checks the one-breakpoint
  word `ab^\omega`. The ownership statement is accurate relative to printed
  pp. 34--35.

- **R2-04 -- PASS.** `n-c-014.tex:1500--1533` adds exactly one fresh state
  outside every chain set, sends each missing state-letter case to the fresh
  state on both children, and loops it on every letter. The path-through-added-
  transition argument proves language and strict-chain preservation and
  nonempty finite outdegree. Lines 1534--1585 carry the completion through the
  complement game, finite game, basis theorem, and S2S translation. It is
  expressly handbook-owned relative to the gap on printed pp. 44 and 47--51.

Historical status item R2-05 is superseded, as the charter requires, by R3-03
below.

## Round 3 repair-invariant dispositions

- **R3-01 -- PASS.** Immediately after the general run and `In(r)` definition,
  `n-c-013.tex:822--832` gives the source's total function
  `\delta:Q\times\Sigma\to Q`, the unique-run recurrence, and the one-run
  consequence from printed p. 28. Lines 874--881 make deterministic Muller
  complementation depend on that deterministic standing rather than a merely
  partial functional relation, as required by printed p. 31.

- **R3-02 -- PASS.** At the actual first occurrence,
  `n-c-013.tex:885--896` includes the typed injection
  `\nu:N(T)\hookrightarrow\{1,\ldots,2n\}` and distinguishes it from labels and
  marks. Lines 897--943 consistently give the handbook-normalized initial name,
  persistent survivor names, pairwise-distinct new names outside the complete
  predecessor name set, the empty state's empty name image, the reservoir
  argument, and the exact `E_k,F_k` definitions. Lines 898--905 and 929--930
  distinguish the handbook-owned normalization and definedness clauses from
  the named-node, persistence, fresh-name, and reservoir content on printed
  pp. 33--35.

- **R3-03 -- PASS.** The detailed history at
  `p09-thomas-1996-report-source-note.md:331--349`, the compact histories at
  `p09-source-presentations-lot2-3.md:606--616,674--682`, and the consolidated
  open ledger at lines 902--918 agree: Rounds 1 and 2 rejected their snapshots,
  the two Round 2 omissions are repaired, Round 3 is open, the registered 1997
  chapter remains unreconciled, and no Thomas presentation or broader unit is
  admitted. The detailed note at lines 63--71 and 316--322 makes the frozen
  LaTeX and controlling PDF the review objects and leaves PNGs inert.

## Seat-specific rationale

The frozen prose accurately separates report-owned statements from four
handbook-owned completions: accepting-cycle correction, empty determinization
successor, current-update mark lifetime, and rejecting completion of partial
tree transitions. The new Round 3 clauses likewise restore a source-owned total
deterministic word transition while presenting injective naming and allocation
precision as handbook-defined normalization/definedness rather than silently
attributing them to Thomas. Across the manuscript, detailed record, compact
record, shared chapter, and bibliography, I found no source substitution,
formula reversal, numbered-result inflation, page or version conflation,
correction-ownership error, or premature completion claim.

VERDICT: ACCEPT

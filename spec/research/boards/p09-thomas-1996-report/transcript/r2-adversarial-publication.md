# Round 2 adversarial-publication and terminology review

## Review boundary and method

I reviewed only the Round 2 objects admitted by the charter. I did not read the
ledger, chair transcript, any Round 1 report, either other Round 2 report, any
other board or transcript, staging material, memory, conversation history, or
web results, and I did not contact another reviewer.

I read the actual frozen LaTeX passages in full:

- `handbook/parts/p09/presentations/n-c-013.tex:800-956`;
- `handbook/parts/p09/presentations/n-c-014.tex:888-927` and
  `handbook/parts/p09/presentations/n-c-014.tex:1451-1596`; and
- the chartered cross-file passages in
  `handbook/parts/p09/logic-in-computer-science.tex` and
  `handbook/bib/handbook.bib`.

I also read the complete frozen Thomas source note and the pertinent Thomas and
consolidated-status passages of the frozen compact record. I inspected the
controlling hash-pinned PDF itself, not any retained PNG or other source render.
The exact PDF pages used were the unnumbered title, abstract, and contents pages
(physical PDF pages 1--3), printed pp. 1, 8--12, 28--61, and 72. Those pages
cover the identity and page map, the complete relied-on Section 3.1 passage,
the complete claimed Sections 5.1--5.3 range, and the complete claimed Chapter
6 introduction and Sections 6.1--6.3 range.

No test, test harness, automated checker, repository script, TeX command,
interim build, handbook-PDF inspection, rendered-handbook inspection, or build
was used as evidence.

## Independently recomputed native identities

| Frozen object | Recomputed SHA-256 | Disposition |
|---|---|---|
| `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf` | `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA` | matches |
| `handbook/parts/p09/presentations/n-c-013.tex` | `F3473BB8C2D77A56D82C7086888CD9087AE887847ED3FDA021DC6826868C25E3` | matches |
| `handbook/parts/p09/presentations/n-c-014.tex` | `F9576BB10063037CDFD9018E6DC7DFB553651590FB74FC77D2D33EEBBF4D5915` | matches |
| `handbook/parts/p09/logic-in-computer-science.tex` | `70CFEBC05E1F574703FA6F8B1367C2EBBA1A640A57B2DEEC8D144E88328A7117` | matches |
| `handbook/bib/handbook.bib` | `07233B0722E6DAE89AEE6B34F699BC980D54F4367C2672B4D3B92131F6D680AD` | matches |
| `spec/research/p09-thomas-1996-report-source-note.md` | `3F63E37FE1E7C72140080302E3BDFA716D617A8E73BA157F0D12977041093681` | matches |
| `spec/research/p09-source-presentations-lot2-3.md` | `B43F11B230E9CFF763CAE106A91CDA29122305B02F4CA621E60BD4E63D253208` | matches |

The PDF is 478,293 bytes and 75 physical pages. Its displayed identity is
Wolfgang Thomas, *Languages, Automata, and Logic*, Bericht 9607, Kiel, May
1996. Physical page 4 is printed p. 1 and physical page 75 is printed p. 72.

## Finding

### R2-AP-01 — must-fix — the determinization state never receives a defined injective node-name component

**Exact frozen locations:**

- `handbook/parts/p09/presentations/n-c-013.tex:874-877` defines a
  `Safra tree` by ordered-tree shape, state-subset labels, sibling disjointness,
  proper child-union containment, and a possible mark, but assigns no names to
  ordinary nodes;
- `handbook/parts/p09/presentations/n-c-013.tex:898` first uses `name` while
  defining the exceptional empty state, before any ordinary-state naming datum
  has been defined;
- `handbook/parts/p09/presentations/n-c-013.tex:907-914` says that surviving
  names persist, that a new node receives a name absent from the preceding
  tree, and then defines acceptance sets by name, but never requires distinct
  live nodes, or distinct nodes created in one update, to have distinct names;
- `spec/research/p09-thomas-1996-report-source-note.md:145-150`,
  `163-175`, and
  `spec/research/p09-source-presentations-lot2-3.md:612-616` repeat or claim the
  same incomplete node-name discipline.

**Controlling source:** printed pp. 33--35. Printed p. 33 expressly distinguishes
a node from its macrostate/mark label, gives the node a positive-natural-number
name, preserves names of surviving nodes, and requires every newly created node
to use a name absent from the preceding Safra tree. Printed p. 35 then counts
named nodes, represents a Safra tree through functions on those node names, and
forms one Rabin pair per name. Those functions and the lineage test presuppose
that a live node name identifies one node, not several contemporaneous nodes.

**Why this fails the frozen reconstruction:** stage 1 may create several new
children in the same letter update. The sentence “a new node receives a name
absent from the preceding tree” is satisfied even if two such children receive
the same predecessor-absent number. Because the frozen definition never states
that ordinary nodes are named at all, much less that live names are injective,
the later phrases “some name is eventually permanent,” “states without
`k`,” and “states in which `k` is marked” do not determine a unique persistent
lineage. The `1,...,2n` reservoir claim likewise lacks the one-to-one assignment
whose cardinality argument it is meant to support. This is not cosmetic: it
breaks the exact state object, the update/name invariant, and the Rabin
acceptance proof. It also leaves the Definition prong of the five-part first-use
rule incomplete even though Necessity, Standing, Nonredundancy, and Use are
otherwise present.

**Required repair:** at the first `Safra tree` introduction, make the ordinary
determinization state include a one-to-one assignment of names to its live
nodes from `1,...,2n`, distinct from the state-subset labels and breakpoint
marks. Fix one initial root name; preserve each surviving node's name; require
all nodes created in one update to receive pairwise distinct names that are also
absent from the entire predecessor name set; and retain the empty absorbing
state as having the empty node/name set. Then state `E_k`, `F_k`, persistence,
the reservoir argument, and the three frozen records against that exact naming
invariant. The repair must remain handbook-owned wherever it resolves a
definedness point not literally supplied by the report.

**Affected mandates:** H11, H12, H13, H22, and R2-05.

## Five-part terminology audit at actual first occurrence

| First occurrence | Necessity | Definition | Standing | Nonredundancy | Later use | Disposition |
|---|---|---|---|---|---|---|
| `V^\omega`, `n-c-013.tex:849-861` | the finite-union characterization needs infinite iteration | factors and unbounded cumulative length are explicit | an omega-language operation | distinguished from a merely infinite list of empty factors | used in the exact characterization | pass |
| `Safra tree`, `n-c-013.tex:872-879` | subset states cannot preserve one accepting lineage | shape, subset labels, sibling/child constraints, and mark are given, but the later-essential node-name component is absent | determinized word-automaton state, not input tree or run | distinguished from a reachable-state subset | update and Rabin acceptance use it | **fail: R2-AP-01** |
| empty absorbing determinization state, `n-c-013.tex:896-906` | deleting an empty root would not leave a rooted tree | no node, name, label, or mark; absorbing | exceptional determinized word-automaton state | differs from every ordinary state by having no root | rejection and bounds use it | pass |
| Rabin chain, `n-c-014.tex:1478-1491` | replaces an arbitrary Muller family for the later game route | the strict `E_1,F_1,...,E_m,F_m` chain and path test are explicit | path acceptance condition | distinguished from arbitrary Muller acceptance and related to parity | Theorems 6.5--6.20 use it | pass |
| order-vector with hit, `n-c-014.tex:1491-1498` | finite memory is required to recover Muller recurrence data | permutation plus the prior position of the just-visited state | finite memory attached to automaton state, not input tree or path | differs from the bare state and records last-appearance information | Remark 6.6 and the chain conversion use it | pass |
| completed automaton `\mathcal A^\bot`, `n-c-014.tex:1500-1529` | the source's partial transitions do not satisfy the game theorem's live-position premise | fresh rejecting state, missing-transition edges, and absorbing loops are exact | chain tree automaton, not game or run | differs only at missing state-letter cases | all later game routes use it | pass |
| memoryless strategy, `n-c-014.tex:1534-1542` | Theorem 6.8 and complementation require the restricted strategy class | choice depends only on current game position | strategy in the Automaton/Pathfinder game | distinguished from history-dependent strategy | Theorems 6.8--6.18 use it | pass |
| local instruction, `n-c-014.tex:1542-1552` | a memoryless Pathfinder strategy must be finitely tree-coded | function from input-letter/transition pair to a direction | finite label encoding one local strategy choice | distinguished from the input tree and global run | word- and tree-automaton checks use it | pass |
| regular tree, `n-c-014.tex:1564-1574` | the basis theorem needs a finite representation of an accepted tree | generated by a deterministic finite direction automaton with output | property of an input tree | explicitly not an acceptance mode | emptiness and regular-member conclusions use it | pass |

The only failed first occurrence is the named determinization-state object in
R2-AP-01. The report/final-chapter, historical/later-proof, and
source/handbook-repair phrases are metalinguistic boundaries rather than new
mathematical objects; they are consistently typed as such.

## H01--H22 dispositions

- **H01 — pass.** Hash, byte length, 75-page extent, title, author, report
  number, institution, place, and May 1996 date agree. The records consistently
  call the object a complete report precursor rather than a verified 1997
  facsimile.
- **H02 — pass.** The unnumbered abstract's literal prospective *Handbook of
  Formal Language Theory* title is preserved in the detailed note and kept
  distinct from the bibliography's eventual *Handbook of Formal Languages*
  identity.
- **H03 — pass.** The physical/printed map and the Section 3.1, 5.1--5.3, and
  6.1--6.3 ranges agree with the actual PDF. No final-chapter locator is
  inferred.
- **H04 — pass.** Public course access is not promoted to an open-content
  licence; the detailed note ultimately states that derived images are viewer
  aids with no independent evidentiary weight and are not handbook assets.
  This review used none of them.
- **H05 — pass.** The five-component finite-word tuple, ternary transition
  relation, length-`n+1` run, initial/final clauses, and effective two-way
  Theorem 3.1 strength match printed p. 8.
- **H06 — pass.** Disjoint tracks, separately checked last-letter transition,
  empty-word guard, `MSO_0` atoms, complement, union, and projection match
  printed pp. 8--9.
- **H07 — pass.** `WS1S` finite-set range, input-free successful-run criterion,
  and the bounded reversed-binary/carry Presburger description retain printed
  pp. 10--12 strength without inflation.
- **H08 — pass.** The omega tuple, ternary transition relation, run, and
  `In(r)` are typed before the four modes and remain distinct from finite-word
  and tree automata.
- **H09 — pass.** All four source conventions are correct. In particular the
  frozen Streett formula and prose say recurrence of `F_i` implies recurrence
  of `E_i`, matching printed p. 29.
- **H10 — pass.** Example 5.2, Proposition 5.3, the finite union of regular
  `U V^\omega` factors, deterministic-Buechi complement failure, and
  deterministic-Muller complementation retain the report's roles and strengths.
- **H11 — fail (R2-AP-01).** Necessity, tree shape, subset labels, mark,
  word-automaton standing, nonredundancy, and later use are present, but the
  first definition omits the later-essential named-node component.
- **H12 — fail (R2-AP-01).** Update order, empty-root case, persistence against
  the preceding tree, live-node bound, and reservoir are stated, but unique
  contemporaneous naming is never defined, so the name discipline is not exact.
- **H13 — fail (R2-AP-01).** Eventual persistence, repeated current marks,
  proof directions, asymptotic state bound, `2n` construction pairs, and the
  lower-bound qualifier otherwise agree with printed pp. 34--37; however
  `E_k`/`F_k` do not identify a unique lineage until node names are injective.
- **H14 — pass.** Theorem 5.9 remains effective both ways. The printed p. 38
  missing-final-state defect is visible, and the reachable nonempty cycle
  meeting `F` is expressly handbook-owned.
- **H15 — pass.** The Proposition 5.11 disjunction and its eventual-absence /
  recurring-presence quantifiers match printed pp. 38--39; the inner formulae
  are bounded below the current position and weak monadic range means finite
  sets.
- **H16 — pass.** The four-place tree transition, global run, root/child
  equations, existential-run/universal-path Muller condition, and the exact
  Example 6.2--6.3 separation match printed pp. 44--45.
- **H17 — pass.** The strict chain and path condition are exact. The
  order-vector-with-hit first occurrence supplies its five parts and Remark 6.6
  use at printed pp. 45--47.
- **H18 — pass.** Move order, Remark 6.7 equivalence, and current-position-only
  memorylessness are exact; the handbook completion supplies the source's
  missing nondeadlock premise before using the game theorem.
- **H19 — pass.** The local direction-function tree, universal transition
  handling by word-automaton closure, universal path handling by a deterministic
  Muller tree automaton, nondeterministic label guess, and independence from
  the particular input tree match printed pp. 49--50.
- **H20 — pass.** The forced-finite-visit/complementary-subgame induction,
  finite-game effectivity, finite generator with output, input guessing,
  memoryless-strategy generator, effective emptiness, and regular-member result
  agree with printed pp. 51--57 and are kept separately typed.
- **H21 — pass.** Atomic, disjunction, existential, and complement steps,
  existential-run/universal-path reverse shape, and the input-free S2S route
  agree with printed pp. 57--59. The earlier Muller-to-chain conversion supplies
  Theorem 6.9 and Theorem 6.18 with their required acceptance form. Thomas's
  route remains explicitly later and non-substitutive for Rabin 1969.
- **H22 — fail (R2-AP-01).** Bibliography, source/version limits, page locators,
  repair ownership, and open admission status otherwise agree, but all three
  Thomas records claim an exact node-name/Rabin-pair discipline without stating
  the injective live-node naming invariant needed to make that claim true. No
  broader unit is admitted by this review.

## R2-01--R2-05 dispositions

- **R2-01 — pass.** `n-c-013.tex:849-861` gives a finite union, regular
  finite-word factors, unbounded total factor length, and report-level rather
  than priority standing, matching printed p. 30.
- **R2-02 — pass.** `n-c-013.tex:896-917` defines the no-node/no-name/no-mark
  absorbing successor, proves that no original run can revive, places it in
  every excluding and no recurring component, and preserves the live-node,
  reservoir, asymptotic-state, and exact-pair bounds. The completion is
  handbook-owned. R2-AP-01 concerns the ordinary live states, not this empty
  state's definition.
- **R2-03 — pass.** `n-c-013.tex:880-884` clears predecessor marks and confines
  marks to current collapses; `915-923` uses distinct collapse events and the
  one-breakpoint `a b^\omega` counterexample. The clarification is
  handbook-owned and matches the gap visible on printed pp. 34--35.
- **R2-04 — pass.** `n-c-014.tex:1500-1556`, `1568-1569`, and `1580-1585`
  define and prove the rejecting completion, establish nonempty finite
  outdegree, and propagate it through complementation, finite games, the basis
  route, and S2S. It remains handbook-owned relative to printed pp. 44 and
  47--51.
- **R2-05 — fail (R2-AP-01).** Round 1 rejection, the open fresh Round 2
  unchanged-snapshot review, unreconciled 1997 chapter, and narrow nonadmission
  status agree across the detailed and compact records. The first manuscript
  `Safra tree` occurrence nevertheless fails the Definition prong because it
  omits the named-node component required by its own later theorems.

## Seat-specific rationale

The repaired snapshot successfully separates finite from infinite words, words
from trees, the four acceptance modes, determinization states from input trees
and runs, the 1996 report from the 1997 chapter, Thomas's later game proof from
Rabin's historical proof, and every handbook-owned correction from report text.
The four substantive Round 2 mathematical repairs are present and source-bounded.

Publication admission nevertheless requires the determinization state to be a
single well-defined mathematical object. Without an injective live-node naming
component, the text cannot tell whether a persistent number denotes one lineage,
cannot define marked presence of that lineage, and cannot justify one Rabin pair
per name. That unresolved must-fix defeats H11--H13, H22, and R2-05 on the
current hashes.

VERDICT: REJECT -- R2-AP-01

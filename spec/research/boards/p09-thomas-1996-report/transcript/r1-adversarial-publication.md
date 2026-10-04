# Round 1 adversarial publication and terminology review

## Review scope and independence

I reviewed only the Round 1 charter, the seven frozen Round 1 objects, and the
forty-four source renders named by the charter. I did not read the ledger, the
chair transcript, another review, another board or board transcript,
conversation history, memory, staging material, or web results. I did not edit
any frozen object.

This is solely an adversarial publication-and-terminology judgment on whether
the frozen May 1996 report-precursor reconstructions may be admitted as
`N-c-013.e` and `N-c-014.e`. It is not a judgment on the registered 1997 chapter,
the original Buechi, McNaughton, Safra, or Rabin bodies, either presentation
file overall, Part IX, a build, a rendered handbook, the book, or publication.

## Independently recomputed identities

I independently recomputed all seven SHA-256 identities with the native file
hash facility immediately before filing this report. Every value matches the
charter.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf` | `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA` | match |
| `handbook/parts/p09/presentations/n-c-013.tex` | `76480DE7C2620521835DD1301B5D8B5698C60E14AA0B2EFA467D852F81BB36CA` | match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `F12CD5EDD8D160D91E9A2BC7B68056EF77AB8F2F6FFF5AD4EC474669059CF31B` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `70CFEBC05E1F574703FA6F8B1367C2EBBA1A640A57B2DEEC8D144E88328A7117` | match |
| `handbook/bib/handbook.bib` | `07233B0722E6DAE89AEE6B34F699BC980D54F4367C2672B4D3B92131F6D680AD` | match |
| `spec/research/p09-thomas-1996-report-source-note.md` | `B33BF77916C06C57F4896394B4A5569678D75B0B14A940FF451D68D4BD915FB8` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `45F8EB339A139C24251616F03A77715337F8E8B8F735956D35B05407D92637C7` | match |

The controlling PDF is 478,293 bytes and 75 physical pages.

## Controlling-PDF and page-inspection attestation

I inspected all forty-four charter-mandated PNG renders individually at
original detail: the five identity/page-map renders (`inspect-title-01.png`,
`inspect-title-02.png`, `inspect-title-03.png`, `inspect-body-start-04.png`, and
`inspect-body-end-75.png`) and all thirty-nine substantive renders (`page-11.png`
through `page-15.png` and `page-31.png` through `page-64.png`). No required page
was omitted.

Separately, I directly opened and read the hash-matched 75-page PDF itself
across every controlling range. The PDF, not the PNG derivatives, controlled
all source judgments in this report. The PNGs were used only as viewer/display
aids and have no independent evidentiary force. Any searchable extraction was
used only for navigation; every formula, symbol, wording, and pagination
judgment was checked against the controlling PDF page and its corresponding
original-detail page view.

The PDF itself confirms that physical page 1 is the unnumbered title page,
physical page 2 the unnumbered abstract, physical page 3 the contents page
numbered `i`, physical page 4 printed page 1, and physical page 75 printed page
72. Thus the relied-on body ranges map as follows: physical 11--15 to printed
8--12, physical 31--45 to printed 28--42, physical 46 to printed 43, and
physical 47--64 to printed 44--61.

No test, test harness, automated checker, repository script, TeX command,
interim handbook build, handbook-PDF inspection, or build was used as evidence.

## H01--H22 dispositions

### H01 -- identity and version: SATISFIED

The report identity, precursor standing, byte length, hash, and extent agree in
`spec/research/p09-thomas-1996-report-source-note.md:13--40`,
`handbook/bib/handbook.bib:2346--2356`, and
`handbook/parts/p09/presentations/n-c-013.tex:799--802,914--918`. The controlling
PDF title page (physical 1, unnumbered) prints Wolfgang Thomas, *Languages,
Automata, and Logic*, Bericht 9607, Kiel, May 1996; printed p. 72 is physical
page 75. Nothing identifies this file as a verified facsimile of the registered
chapter.

### H02 -- prospective and final titles: SATISFIED

The literal prospective/final-title distinction is explicit at
`spec/research/p09-thomas-1996-report-source-note.md:73--80`, while the separate
final identity appears at `handbook/bib/handbook.bib:2358--2367` and the reader
boundary at `handbook/parts/p09/logic-in-computer-science.tex:2348--2356`. The
controlling report abstract (physical 2, unnumbered) says *Handbook of Formal
Language Theory*; it does not silently become the eventual *Handbook of Formal
Languages* title.

### H03 -- page map and coverage: SATISFIED

The page map and inspected ranges at
`spec/research/p09-thomas-1996-report-source-note.md:36--41,49--69` agree with
the PDF: printed pp. 1, 8--12, 28--61, and 72 occur on physical pages 4, 11--15,
31--64, and 75 respectively. The citations at
`handbook/parts/p09/presentations/n-c-014.tex:918,1476,1498,1524,1535,1548`
all fall within those printed ranges. No final-chapter locator is inferred.

### H04 -- rights and custody: SATISFIED

The limited rights statement at
`spec/research/p09-thomas-1996-report-source-note.md:244--249` treats the public
course route as access only and keeps the PDF and renders as research evidence,
not publication assets. No Creative Commons or blanket republication statement
appears on the controlling title page, abstract, or inspected printed pp. 8--12
and 28--61. The frozen text makes no broader negative rights claim than the
pages inspected.

### H05 -- finite-word tuple and run: SATISFIED

`handbook/parts/p09/presentations/n-c-014.tex:888--901` gives the five-component
tuple, `Delta` as a subset of `Q x Sigma x Q`, the length-`n+1` run, initial and
final conditions, and effective two-way Theorem 3.1 statement. These agree with
the controlling report at printed pp. 8--9.

### H06 -- finite-word proof directions: SATISFIED

The disjoint tracks, separate last-letter transition, empty-word guard, four
`MSO0` atoms, complement, union, and projection at
`handbook/parts/p09/presentations/n-c-014.tex:903--913` match printed pp. 8--9.
The empty-word guard is presented as a genuine separate obligation rather than
being lost in the nonempty-word construction.

### H07 -- finite-word consequences: SATISFIED

`handbook/parts/p09/presentations/n-c-014.tex:914--918` restricts `WS1S`
monadic variables to finite sets, uses successful-run existence for an
input-free finite automaton, and records only the reversed-binary finite-carry
Presburger route actually supported by printed pp. 10--12.

### H08 -- omega tuple and recurrence set: SATISFIED

`handbook/parts/p09/presentations/n-c-013.tex:800--820` types the finite
omega-automaton, its transition relation, input and run, and `In(r)` before any
acceptance formula. It agrees with Definition 5.1 on printed p. 28 and remains a
word-automaton object rather than a finite-word or tree-automaton tuple.

### H09 -- four acceptance modes: SATISFIED

The four distinct standings and formulas at
`handbook/parts/p09/presentations/n-c-013.tex:821--846` match printed pp. 28--29.
In particular, lines 833--841 preserve Thomas's pair ordering: recurrence in
`F_i` implies recurrence in `E_i`. Example 5.2 and Proposition 5.3 retain their
nondeterministic scope.

### H10 -- comparison and deterministic boundary: NOT SATISFIED (AP-01)

`handbook/parts/p09/presentations/n-c-013.tex:843--855` moves directly from
Proposition 5.3 to deterministic Buechi/Muller behavior. The controlling report
states the missing finite-union `U V^omega` characterization on printed p. 30,
between those topics. The example, proposition, deterministic-Buechi failure,
deterministic-Muller complementation, and Theorem 5.4 boundary are otherwise
accurate at printed pp. 29--31.

### H11 -- determinization-state standing: NOT SATISFIED (AP-02)

The substantive introduction at
`handbook/parts/p09/presentations/n-c-013.tex:857--865` does provide necessity,
an exact eliminable definition, word-determinization-state standing,
nonredundancy against an ordinary subset/input tree/run, and immediate later
use, corresponding to printed pp. 31--33. But the same technical name already
appears at lines 795--796, before those five items. Thomas first introduces the
named state-tree construction on printed p. 32. The charter's literal
first-occurrence rule is therefore not met.

### H12 -- update order and names: SATISFIED

`handbook/parts/p09/presentations/n-c-013.tex:864--879` preserves the `{q0}`
root, youngest `R intersect F` child creation, advancement of all labels,
horizontal deletion, empty-node removal, vertical collapse/marking, persistent
old names, predecessor-relative fresh names, at most `n` live nodes, and the
`1,...,2n` reservoir in the source order. These agree with printed pp. 32--35.

### H13 -- determinization acceptance and bounds: SATISFIED

Eventual name persistence, infinite marking, absence/marked-presence pairs,
both proof directions, the `2^{O(n log n)}` and `2n` displayed bounds, and the
non-exact lower-bound qualifier at
`handbook/parts/p09/presentations/n-c-013.tex:879--890` agree with printed
pp. 34--37.

### H14 -- omega MSO and printed defect: SATISFIED

`handbook/parts/p09/presentations/n-c-013.tex:892--901` preserves Theorem 5.9's
effective two-way strength and visibly distinguishes Corollary 5.10's printed
reachable-cycle omission from the handbook-owned repair requiring a reachable
nonempty cycle that meets `F`. The printed defect is on report p. 38; the
Theorem 5.9 route begins on printed p. 37.

### H15 -- bounded and weak formula consequence: SATISFIED

The finite disjunction, eventual absence and recurring presence quantifiers,
inner bounds below the current position, and finite-set meaning of weak MSO at
`handbook/parts/p09/presentations/n-c-013.tex:901--912` agree with printed
pp. 38--39.

### H16 -- tree tuple, run, and path quantifiers: SATISFIED

The four-place transition relation, global run, root/child equations,
`exists run, for every path` acceptance prefix, and limited Examples 6.2--6.3
use at `handbook/parts/p09/presentations/n-c-014.tex:1451--1476` agree with the
Chapter 6 boundary and printed pp. 43--45.

### H17 -- chain condition and added memory: SATISFIED

`handbook/parts/p09/presentations/n-c-014.tex:1478--1498` gives the strict chain,
exact path condition, and the order-vector-with-hit as a permutation plus prior
position. Its finite-state-memory standing, distinction from an input tree or
path, and nonredundant Remark 6.6 use are all supplied at its first occurrence,
in agreement with printed pp. 45--47.

### H18 -- game and memoryless standing: NOT SATISFIED (AP-03)

The move order, Remark 6.7 statement, and definition of current-position-only
memorylessness at `handbook/parts/p09/presentations/n-c-014.tex:1500--1507`
match printed pp. 47--49. However, Definition 6.1 allows a partial transition
relation at printed p. 44, while the abstract game graph used for determinacy
requires every vertex to have a nonempty finite outgoing-edge set at printed
p. 50. The manuscript supplies neither a completion step nor terminal-play
semantics, so the no-available-transition case remains undefined.

### H19 -- complementation proof architecture: NOT SATISFIED (AP-03)

Conditional on a total game, the local direction functions, universal
transition-sequence check, universal path check, finite instruction alphabet,
nondeterministic instruction-label guess, and independence from the particular
input tree at `handbook/parts/p09/presentations/n-c-014.tex:1507--1519` accurately
summarize printed pp. 49--50. Without the missing completion/terminal case from
AP-03, however, the determinacy premise does not cover every automaton admitted
by the tuple at lines 1454--1465.

### H20 -- determinacy, regular trees, and basis: NOT SATISFIED (AP-03)

The forced-finite-visit/complementary-subgame induction, finite-game
effectivity, finite output generator, input guessing, memoryless-strategy
extraction, effective emptiness, and regular-member conclusion at
`handbook/parts/p09/presentations/n-c-014.tex:1519--1535` otherwise agree with
printed pp. 50--57 and remain separately typed. But both the finite-game and
basis uses inherit the undefined dead-end case identified in AP-03 until the
game is put within the nonempty-outgoing-edge hypothesis.

### H21 -- MSO translation, S2S, and historical boundary: SATISFIED AS STATED

`handbook/parts/p09/presentations/n-c-014.tex:1537--1555` accurately gives the
atomic, disjunction, existential, and complement induction; the converse
existential-run/universal-path shape; and the input-free route to Theorem 6.20,
matching printed pp. 57--59. Lines 1550--1555 keep Thomas's later proof separate
from Rabin's historical Section 3.12 route and the separate `N-c-014.d`
admission. This content disposition does not cure the upstream AP-03 proof
precondition.

### H22 -- cross-file, terminology, and completion scope: NOT SATISFIED (AP-01, AP-02, AP-03)

The bibliography and report/final, Thomas/Rabin, source/handbook-correction,
rights/asset, precursor/admission, and open-status boundaries otherwise agree
at `handbook/parts/p09/logic-in-computer-science.tex:25--42,721--762,814--828,843--846,2348--2356`,
`handbook/bib/handbook.bib:2346--2367`,
`spec/research/p09-thomas-1996-report-source-note.md:1--80,244--269`, and
`spec/research/p09-source-presentations-lot2-3.md:606--616,674--682,902--918`.
The controlling abstract and printed pp. 30, 32, 44, 47--50, and 57--59 confirm
those major boundaries. Admission is nevertheless unavailable: the source
component omitted in AP-01 defeats completeness, AP-02 violates the literal
five-part first-occurrence rule, and AP-03 leaves a proof-domain condition
unstated. The verdict remains restricted to the two precursor passages and no
prohibited evidence category is being promoted.

## Findings and required repairs

### AP-01 -- must-fix -- required finite-union characterization omitted

- **Manuscript location:**
  `handbook/parts/p09/presentations/n-c-013.tex:843--855`.
- **Controlling source location:** printed report p. 30 (physical page 33),
  Section 5.1.
- **Falsification:** after Example 5.2 and Proposition 5.3, the manuscript moves
  directly to deterministic Buechi failure and deterministic Muller
  complementation. The PDF states between those topics that an omega-language
  is Buechi-recognizable exactly when it is a finite union of sets of the form
  `U V^omega`, with `U` and `V` regular finite-word languages. The Thomas
  subsection never states this characterization. An occurrence in another
  source presentation would not preserve Thomas's ownership or satisfy H10.
- **Required repair:** insert, after the Proposition 5.3 discussion and before
  the deterministic boundary, the exact finite-union characterization with
  `U,V` explicitly standing as regular finite-word languages and the result
  explicitly attributed to the May 1996 report, Section 5.1, printed p. 30.
  Do not strengthen it into a deterministic-Buechi characterization or assign
  it final-chapter strength. Reconcile the detailed and compact status records
  if their completion wording is retained.

### AP-02 -- must-fix -- technical name precedes its five-part introduction

- **Manuscript location:**
  `handbook/parts/p09/presentations/n-c-013.tex:795--796`; the complete
  introduction occurs only at lines 857--865.
- **Controlling source location:** printed report p. 32 (physical page 35),
  with the necessity argument beginning on printed p. 31 and the formal
  determinization-state set continuing on printed p. 33.
- **Falsification:** line 795 is the first occurrence in the frozen presentation
  of the technical name later defined at line 859. Its quotation and negative
  metalinguistic context do not supply, at that location, necessity, an
  eliminable definition, standing, nonredundancy, and later use. Lines 857--865
  do supply all five, but they occur too late for the charter's literal
  first-occurrence requirement. The source itself introduces the name together
  with the tree organization and its determinization-state use on printed p. 32.
- **Required repair:** remove the name from lines 795--796 and describe only
  the owed missing determinization-state definition there, leaving line 859 as
  the first named occurrence; alternatively move the complete five-part
  introduction to the earlier occurrence. Do not weaken the existing line
  857--865 definition or turn this state object into an input tree or run.

### AP-03 -- must-fix -- partial transitions fall outside the stated game theorem

- **Manuscript location:**
  `handbook/parts/p09/presentations/n-c-014.tex:1454--1465,1500--1523`; the same
  unqualified route is recorded at
  `spec/research/p09-thomas-1996-report-source-note.md:177--214` and
  `spec/research/p09-source-presentations-lot2-3.md:680`.
- **Controlling source location:** printed report p. 44 (Definition 6.1),
  pp. 47--49 (the Automaton/Pathfinder game and Remark 6.7), and p. 50
  (Definition 6.10's nonempty-outgoing-edge requirement).
- **Falsification:** the tuple admits an arbitrary relation
  `Delta subset Q x Sigma x Q x Q`; neither source nor manuscript requires a
  matching transition for every state/letter pair. If no transition is
  available, Automaton cannot make the move assumed at lines 1500--1503, so the
  play is not the infinite play to which the stated winning condition applies.
  Yet the determinacy theorem is invoked through game graphs whose every vertex
  has a nonempty finite set of outgoing edges. Thus Remark 6.7 and the later
  complement/basis uses have an unstated domain step for precisely the
  no-available-transition stress case.
- **Required repair:** before the game reduction, give and prove an explicit
  language-preserving completion for missing transitions: add one state reached
  on every missing state/letter case, make it loop for every input letter, keep
  it outside every accepting chain component so a path trapped there rejects,
  and verify that the strict chain and recognized tree language are unchanged.
  An alternative repair may define terminal loss and then prove a reduction to
  the nonempty-outgoing-edge games used by Theorems 6.8 and 6.13. In either
  form, identify this as a handbook-owned clarification/correction rather than
  wording silently quoted from Thomas, and update the detailed and compact
  records consistently.

## Seat-specific rationale

The frozen reconstruction succeeds on most adversarial boundaries: finite and
infinite words are not conflated; word automata, determinization-state trees,
input trees, and runs have distinct standings; Thomas's Streett ordering is
preserved; the printed `S1S` defect is openly repaired rather than silently
normalized; Thomas's later game route is not projected onto Rabin; public
access is not turned into a licence; and the report precursor is never promoted
to the unreconciled final chapter.

Those strengths do not permit admission on the frozen snapshot. AP-01 omits an
item that H10 expressly requires and that the controlling PDF states. AP-02 is
a literal first-occurrence terminology violation whose local fix is small but
mandatory. AP-03 is not stylistic: it leaves the reconstructed acceptance-game
equivalence outside the hypothesis of the determinacy machinery for partial
transition tables. Each is a supported must-fix and therefore independently
forces rejection under the charter's consensus rule.

VERDICT: REJECT -- AP-01, AP-02, AP-03

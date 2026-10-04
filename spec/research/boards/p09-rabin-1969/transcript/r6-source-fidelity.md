# Round 6 source-fidelity review: Rabin 1969

## Seat, scope, and conclusion

I reviewed the complete frozen Round 6 snapshot for the source-fidelity,
evidence, and historical-language mandate.  I did not limit the review to the
Round 5 compact-record repair.  I compared the reader, detailed source note,
compact record, and relevant bibliography identities against the complete
printed Rabin article and the complete printed Meyer article.  I found no
blocker, must-fix, should-fix, consider, discard, or unresolved-user finding.

This verdict concerns only the frozen `N-c-014.d` manuscript content.  It does
not admit another `N-c-014` presentation, Part IX, a rendered page, a build,
the handbook, or any human or user acceptance gate.

## Evidence boundary and independence

I used only:

1. `spec/research/boards/p09-rabin-1969/charter.md` in full;
2. the six objects listed in the charter's Frozen Round 6 snapshot;
3. `tmp/pdfs/p09-rabin-1969/rendered/page-01.jpg` through
   `page-36.jpg`; and
4. `tmp/pdfs/p09-rabin-1969/meyer1975-rendered/page-485.png` through
   `page-490.png`.

The two frozen PDFs controlled.  The page renders were used only to read them
at original detail.  I did not use OCR or the layout extraction as controlling
evidence.  I did not open any Round 1--5 report, unfiled Round 4 work, another
Round 6 report, `ledger.md`, `transcript/chair.md`, another board or
transcript, the staging draft, or the forbidden layout extraction.  I did not
contact another reviewer.  No web source, conversation account, or prior
review conclusion was used.

I did not run a test, automated checker, repository script, TeX command,
interim build, handbook-PDF inspection, or build.

## Frozen identities

Before substantive review I independently recomputed SHA-256 with the native
platform hashing command.  Every actual value equals the charter value:

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | exact match |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695` | exact match |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | exact match |
| `spec/research/p09-rabin-1969-source-note.md` | `29DAF36E123A2900620D49F018BD5F76BC4EE2FE0AAA7E3F85AAB50B23F37D7B` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `BB5D7220F75298C6DF3A1934D0DE36F25B9BD64AC5B2B71A141C2A41D3536236` | exact match |

The PDF byte counts also agree with the detailed note: 912,831 bytes for the
Rabin PDF and 53,151,542 bytes for the Meyer proceedings PDF.

## Printed pages inspected

- Rabin: all 36 physical pages.  Physical p. 1 is the JSTOR/AMS
  custody-and-use cover.  Physical pp. 2--36 are printed pp. 1--35, all of
  which I inspected individually at original detail.
- Meyer: all six article pages, physical PDF pp. 485--490, corresponding to
  printed pp. 477--482, each inspected individually at original detail.

The Rabin pass included every definition, theorem, proof page, application
page, and reference page.  The Meyer pass included the complete statement and
context of the tower lower bound, the list of theories to which it applies,
the attribution list, and the references.

## Whole-snapshot source audit

### Successor structures, trees, and ordinary acceptance

- **R01--R02:** The reader retains Rabin's root `\(\Lambda\)` and defines the
  two editorially subscripted orders before use at
  `n-c-014.tex:914--947`.  It gives Definition 1.1 for every
  `\(0<n\leq\omega\)`, with `\(T_n=n^*\)`, all successors, initial-segment
  order, and lexicographic order, then states the finite-`n` definability and
  `T_\omega` exception at `n-c-014.tex:941--952`.  These agree with Rabin,
  printed pp. 2 and 5.  The detailed note (`p09-rabin-1969-source-note.md:
  136--174`) and compact record (`p09-source-presentations-lot2-3.md:664`)
  agree.
- **R03:** Arbitrary-root subtrees, paths, valued trees, transition tables,
  ordinary automata, runs, and ordinary `\(\exists r\,\forall\pi\)`
  acceptance with `\(F\subseteq\mathcal P(S)\)` are separately typed at
  `n-c-014.tex:965--1014`, matching Rabin pp. 5--6.  The reader also preserves
  the arbitrary-root language and re-rooting invariance.
- **R04:** The finite pair sequence is introduced only with dual acceptance at
  `n-c-014.tex:1141--1188`; its `\(\forall r\,\exists\pi\)` prefix and the
  no-run vacuity are explicit.  This agrees with Definitions 3.5--3.6 on
  Rabin pp. 24--25 and is not substituted for ordinary `F`.
- **R05:** The reader gives exactly the effective union/intersection,
  projection, converse unconstrained-coordinate addition, complementation,
  and emptiness roles of Theorems 1.3--1.6 at
  `n-c-014.tex:1016--1023`, matching Rabin pp. 6--7.  No undefined operation
  name replaces the two directions of Theorem 1.4.

### Formula tracks and both logical directions

- **R06:** Definition 1.7's full-root map is typed at
  `n-c-014.tex:1027--1039` as a bijection
  `\(\mathcal P(T)^n\leftrightarrow\)` full-root
  `\(\{0,1\}^n\)`-valued trees.  The principal-formula reduction, finite-tree
  lift, Boolean operations, track projection, and complementation are stated
  separately at `n-c-014.tex:1048--1065`, agreeing with Rabin pp. 7--9 and
  30--31.
- **R07:** The worked formula at `n-c-014.tex:1067--1077` is explicitly
  handbook-owned and is presented as an instance of Rabin's principal-formula
  construction, not as a printed transition table.  Its node/left-child track
  condition faithfully instantiates formula (1.2) and Corollary 3.13 on Rabin
  pp. 8 and 31.
- **R08:** The converse state-track encoding, one-initial-state normalization,
  and prefix `\(\exists B_1\cdots\exists B_m\,\forall C\)` appear at
  `n-c-014.tex:1079--1091`, matching Theorem 1.10 and formula (1.3) on Rabin
  p. 10.  The closed-sentence argument at `n-c-014.tex:1093--1098` is Rabin's
  direct reduction to nonemptiness on p. 9 and inserts no basis theorem.

### Path product, dual language, and complementation

- **R09:** `n-c-014.tex:1102--1139` gives the deterministic Muller word
  automaton with `\(K:U\times S\to U\)`, product state set `\(U\times S\)`,
  initial set `\(\{u_0\}\times S\)`, the exact common first-coordinate
  update, and designated family defined by first projection.  This matches
  Theorem 3.1 on Rabin pp. 18--19.  The finite indexing offset does not affect
  the infinite-occurrence condition.
- **R10:** The exact type and type-empty conditions are reproduced at
  `n-c-014.tex:1143--1166`; dual acceptance and its complement role follow at
  `n-c-014.tex:1167--1188`.  These agree with Rabin pp. 24--25.
- **R11--R12:** The marked-tree obligations, simultaneous runs, same-state
  merging, and Theorem 3.1 path check are retained at
  `n-c-014.tex:1218--1225`.  Well-foundedness is absence of infinite descent,
  with obligations in lower ordinal strata, at
  `n-c-014.tex:1227--1233`.  The exact transfinite loci are identified as
  Lemmas 3.3 and 3.11 at `n-c-014.tex:1296--1303`, matching Rabin pp. 19--24
  and 28--30.
- **R13:** The roles and lengths for Lemmas 3.7--3.11, the
  last-lower-set-empty half-step, the arbitrary half-step, the explicit
  zero-length normalization, and induction on positive `k` remain distinct at
  `n-c-014.tex:1235--1256`, matching Rabin pp. 25--32.

### Finite trees and the result-role boundary

- **R14:** At first use in the reader, `frontiered` is defined exactly as the
  property that every nonfrontier node of the finite predecessor-closed set
  has both successors, and it is distinguished from predecessor closure at
  `n-c-014.tex:1259--1271`.  Valuation excludes the frontier.  The exact
  finite-tree automaton codomain and the standing of `\(f\notin S\)` as a
  distinguished external frontier value, never a state, appear at
  `n-c-014.tex:1272--1283`.  This matches Rabin p. 30.  The detailed note's
  first use is the complete definition at
  `p09-rabin-1969-source-note.md:303--316`, and the compact record defines the
  term and standing at `p09-source-presentations-lot2-3.md:670`.
- **R15:** The reader assigns Lemma 3.12 to the finite-to-infinite lift,
  Corollary 3.13 to the principal-formula case, Lemma 3.14 to the compactness
  extraction, and Corollary 3.15 to the returning finite-tree complement
  construction at `n-c-014.tex:1284--1293`.  This is the exact division on
  Rabin pp. 30--31.  The same corrected division appears in the detailed note
  at `p09-rabin-1969-source-note.md:535--541` and the compact record at
  `p09-source-presentations-lot2-3.md:670`.  None of the three records turns
  the infinite input or full monadic theory into a weak one.

### Rabin's emptiness proof and the three explicit completions

- **R16:** `n-c-014.tex:1307--1333` exactly follows Rabin pp. 32--33: erase
  the alphabet to one letter, complement the one-tree language, convert it to
  a dual language, and decide the resulting membership question.  No regular-
  tree basis theorem is inserted.
- **R17:** Every recursive question is stated with its current finite table
  and pair sequence at `n-c-014.tex:1335--1342`.  Definition 3.7 retains the
  formal state set while restricting states strictly below the root at
  `n-c-014.tex:1343--1351`, so the root may lie outside the restriction.  This
  matches Rabin p. 33.
- **R18:** The last-empty-lower-set reduction at
  `n-c-014.tex:1361--1371` exhausts every `\(H\subseteq U_k\)`.  It identifies
  `\(H=\varnothing\)` as the direct shorter-sequence question and labels that
  branch as a handbook-owned completion of Rabin's printed nonempty clause on
  p. 34.  Nonempty `H` uses the restricted table and reduces to length
  `\(k-1\)`.  The arbitrary half-step's finite-stratum termination is stated
  at `n-c-014.tex:1353--1359`.
- **R19:** The base at `n-c-014.tex:1373--1389` permits `\(m=0\)`, an empty
  `\(U_0\)`, and only `\(E_0\)` in that case.  It correctly identifies the
  resulting requirement as no run from `\(s_0\)` and invokes Koenig compactness
  for the equivalent finite obstruction.  The source's nonempty branch is
  preserved and the empty completion is owned by the handbook.  The external
  weak-monadic dependency is not converted into an internal Rabin theorem.
  The printed nonempty language being completed is on Rabin p. 34.
- **R29:** `n-c-014.tex:1190--1213` correctly observes that Lemma 3.6 can
  produce a zero-length pair sequence and that it dually accepts exactly when
  no rooted run exists.  For `\(\Omega^\dagger=((S,S))\)`, the path-type
  language is empty, so its dual semantics is identical.  The reader labels
  this as an exact handbook-owned normalization into Rabin's positive-length
  induction, not a new acceptance condition.  This is consistent with Lemma
  3.6 on Rabin p. 25 and the induction beginning on pp. 31--32.  The detailed
  note (`p09-rabin-1969-source-note.md:385--403`) and compact record
  (`p09-source-presentations-lot2-3.md:668`) agree.

### Complexity, applications, attribution, and custody

- **R20:** Rabin's elementary-recursive assertion is reported only as a
  historical source claim at `n-c-014.tex:952--960` and
  `n-c-014.tex:1392--1396`; it is not retained.  Rabin makes that assertion on
  printed pp. 1, 4, and 7.  Meyer's theorem begins on printed p. 478 with a
  non-elementary tower lower bound; item 5 on printed p. 479 explicitly lists
  “the theory of two successors and prefix” and credits Meyer and Stockmeyer.
  The manuscript's sublanguage inference is sound because Rabin's displayed
  binary structure contains both successors and prefix.  Decidability and
  effectiveness are preserved.
- **R21:** `n-c-014.tex:1404--1421` accurately maps the class-level strengths
  of Theorem 2.1, Corollaries 2.2--2.3, Theorem 2.4 and Corollary 2.5,
  Theorems 2.6--2.11, and the encoded Gale--Stewart statement.  These agree
  with Rabin pp. 11--17 and keep countable/full, arbitrary/weak, topological,
  Boolean-algebra, and game claims distinct.
- **R22:** The reconstruction/omission boundary is explicit at
  `n-c-014.tex:1423--1430`.  Thomas's later basis route remains separately
  attributed at `n-c-014.tex:1432--1437`, while McNaughton's external word-
  automaton theorem is separately attributed at `n-c-014.tex:1114--1139`.
  Rabin's own article identifies the external McNaughton dependency on printed
  p. 18 and its complete Chapter III boundary on printed pp. 3 and 17--35.
- **R23:** Numbering, notation, and locators agree throughout: Definition 1.1
  and Theorems 1.1--1.12 on Rabin pp. 5--11; Chapter II results on pp. 11--17;
  Theorem 3.1 on p. 18; Definitions 3.5--3.7 and Lemmas 3.6--3.11 on
  pp. 24--34; and Lemmas 3.12--3.14 plus Corollaries 3.13 and 3.15 on
  pp. 30--31.  I found no numbering, notation, strength, or attribution drift
  among the reader, detailed note, and compact record.
- **R24:** The four frozen text records agree on Rabin's identity, DOI, pages,
  scan URL, the Meyer correction, and pending Round 6 status.  The relevant
  bibliography records are `handbook.bib:2290--2299` (McNaughton),
  `handbook.bib:2346--2355` (Thomas), `handbook.bib:5938--5947` (Meyer),
  `handbook.bib:5973--5982` (Rabin), and `handbook.bib:5993--6002`
  (Thatcher--Wright).  Their identities, pagination, and available DOI data
  agree with the frozen records and with Rabin's printed McNaughton reference
  on p. 34 and Meyer pp. 477--482.  The compact record says Round 6 remains
  required at `p09-source-presentations-lot2-3.md:672` and again records the
  pending state at lines 913--915; the detailed note says only three ACCEPT
  verdicts on the unchanged snapshot can admit `N-c-014.d` at lines 637--648.
- **R25:** The detailed note's rights boundary at
  `p09-rabin-1969-source-note.md:83--94` is supported by the Rabin physical
  cover and Meyer's copyright notice on printed p. 477.  Public or anonymous
  research access is not described as an open-content or republication
  licence; local PDFs and renders remain research objects.
- **R28:** Every completion and status sentence is restricted to
  `N-c-014.d`.  The detailed note disclaims terminal admission, final
  typesetting approval, and user acceptance at lines 37--38; the compact
  record keeps `N-c-014.d` pending at line 672; and the reader makes no broader
  admission claim.

## Cross-record and historical-language limitations

The frozen source note and compact record contain summaries of earlier board
history.  The charter forbade opening the underlying reports, withdrawn work,
ledger, and chair transcript, so I checked those summaries only for consistency
with the charter and with one another; I did not independently re-prove their
process-history details.  This limitation does not affect the source claims,
which were checked directly against all printed Rabin and Meyer pages.

The frozen evidence set does not contain the bodies of every later work named
in the bibliography.  I therefore checked Thomas, Thatcher--Wright, and other
later identities only to the extent fixed by the charter and the frozen
cross-record statements.  I did not use those works to override Rabin or Meyer.
The access-language review is scholarly source and licence-boundary review,
not legal advice.

## Findings

None.

VERDICT: ACCEPT

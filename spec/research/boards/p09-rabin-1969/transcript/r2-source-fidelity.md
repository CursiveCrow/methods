# Round 2 source-fidelity review: Rabin 1969, `N-c-014.d`

## Seat and result

- Seat: source fidelity, evidence, and historical language.
- Snapshot: the six-object Round 2 snapshot fixed by the board charter.
- Mandatory scope: R01--R25 and R28--R29.
- Result: accept at manuscript-content level for `N-c-014.d` only.
- Findings: none. I found no blocker, must-fix, should-fix, consider, discard,
  or unresolved-user item.

This was a whole-snapshot review, not a check confined to the three disclosed
repairs. I reread the complete Rabin reconstruction in context, the complete
source note, the complete compact source-presentation file with particular
attention to `N-c-014.d` and its adjacent authority boundaries, and the
complete bibliography with a field-by-field audit of the five identities used
by the reconstruction. I compared the claims against the complete permitted
Rabin and Meyer page sets.

## Frozen-object identity

I recomputed all six SHA-256 values before substantive review. I recomputed
them again after the source comparison to confirm that the reviewed objects
had not changed. Every result matched the Round 2 charter exactly.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | exact match |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `370C563CA4019E1EF266013ADBC910C231D2A07064EE91DC3E7BCCDD32BF3B5E` | exact match |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | exact match |
| `spec/research/p09-rabin-1969-source-note.md` | `D2B3C0293D4012A262726708F082E0B6F7C4A0CE33D623821687F2CB22B97192` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `02C9C6A01DBCC5F876781EE8C13E7235D26C04EB61DD19A811DC8649C6DECF33` | exact match |

The source-note file-size claims also match the frozen files: 912,831 bytes
for the Rabin PDF and 53,151,542 bytes for the Meyer proceedings PDF.

## Controlling pages inspected

I visually inspected the following permitted renders at original detail, in
order, without omitting a page:

- Rabin `rendered/page-01.jpg`: the custody-and-use cover.
- Rabin `rendered/page-02.jpg` through `rendered/page-36.jpg`: all thirty-five
  article pages, corresponding one-for-one to printed pp. 1--35.
- Meyer `meyer1975-rendered/page-485.png` through
  `meyer1975-rendered/page-490.png`: all six article pages, corresponding
  one-for-one to printed pp. 477--482.

I used the renders only as original-detail reading aids. The two hash-pinned
PDFs remain controlling. The page sequences were complete and legible for the
claims under review; I found no missing, duplicated, or mis-mapped article
page.

The Rabin cover identifies the archived-copy custody and use restriction. The
article begins on the next physical page with the exact title, author, journal
pagination, and historical elementary-recursive claim. Meyer printed p. 478
begins the lower-bound result; printed p. 479 includes the listed “theory of
two successors and prefix” case and attributes it to Meyer and Stockmeyer.

## Evidence boundary and independence

I used only the charter, the six Round 2 frozen objects, and the two permitted
original-detail render sets. I did not read or use any Round 1 report, any
other Round 2 report, `ledger.md`, `transcript/chair.md`, a Trakhtenbrot or
other board transcript, the staging draft, or the layout extraction. I did
not contact another reviewer. I did not inspect a handbook PDF.

The permitted source note and compact record themselves contain authored
prose describing Round 1 and the pending-review state. I treated those
sentences solely as claims inside the frozen snapshot that had to be audited;
I did not treat them as review evidence, follow their report references, or
consult the reports they describe. Likewise, the source note names a layout
extraction and its recorded hash, but I did not read or use that extraction.

No web source or unfrozen local source was used. No test, automated checker,
repository script, TeX command, interim build, handbook-PDF inspection, or
build was run. The only mechanical operation on the frozen objects was the
charter-required SHA-256 computation; all substantive source comparison was
performed from the permitted files and original-detail pages.

## Whole-snapshot source comparison

### Structures, notation, and ordinary acceptance: R01--R03

Rabin printed pp. 3--5 establish the word-tree notation, the root symbol
`Λ`, Definition 1.1 for every `0 < n <= omega`, `T_n = n*`, the successors,
and both orders. The finite-`n` definability qualification and the
`T_omega` exception are preserved at reader lines 914--963. No silent
epsilon substitution occurs.

Rabin printed pp. 5--7 distinguish a transition table from an automaton,
allow valued trees rooted at arbitrary nodes, and give ordinary acceptance as
one run satisfying the path condition on every path, with
`F` a subset of the power set of the state set. Reader lines 965--1014
preserve the two tuple types, arbitrary roots, the possibly partial move
table, and the existential-run/universal-path order. The source note at lines
164--230 and compact record at line 664 agree.

### Closure, formula tracks, and both translations: R05--R08

Rabin printed pp. 6--10 separately state the effective union/intersection,
projection/cylindrification, complementation, and emptiness dependencies and
then use them in Theorem 1.7 and the sentence decision. Reader lines
1016--1097 preserve those dependencies without inserting a regular-tree basis
step.

The Definition 1.7 track map at reader lines 1024--1042 is typed on full-root
trees and is stated as a bijection. The normal-form reduction, finite-tree
principal-formula construction, Boolean operations, projection, and
complementation remain distinct. The formula
`exists x (x in A and r_0(x) in B)` at lines 1066--1076 is explicitly
handbook-worked and is not represented as a transition table printed by
Rabin. It correctly instantiates the source's principal-formula scheme.

Reader lines 1078--1097 preserve Theorem 1.10's state-track encoding,
one-initial-state normalization, and existential-state-track/universal-path-
track prefix. The closed-sentence argument is exactly Rabin's reduction to
nonemptiness. These statements agree with the detailed source note at lines
231--295 and compact record at line 666.

### Theorem 3.1: R09

Rabin printed pp. 17--19 distinguish the sequential word automata and give
the path-language construction. Reader lines 1099--1138 correctly type the
deterministic Muller word automaton, its transition map, the product state
set, initial set, update, projection, and designated family. The first
coordinate records the deterministic word run on the second-coordinate state
sequence. The source's harmless initial indexing displacement does not alter
the infinite-occurrence acceptance condition. McNaughton's result is
identified as an external dependency, not silently presented as Rabin's own
theorem. The source note at lines 296--325 agrees.

### Dual acceptance and the zero-length case: R04, R10, R29

Rabin printed pp. 24--26 put the finite pair sequence in Definitions
3.5--3.6 and reverse the ordinary quantifiers to universal-run/existential-
path dual acceptance. Reader lines 1142--1187 retain the exact type and
type-empty clauses, state the vacuous no-run case, and prevent the pair
sequence from being confused with ordinary `F`.

Lemma 3.6 on printed p. 25 can enumerate no pairs, while the printed induction
later begins with positive length. Reader lines 1189--1212 explicitly identify
this source edge and give the handbook-owned replacement `((S,S))`. For the
nonempty finite state set containing the specified root state, no infinite
path map can both meet and avoid `S`; its path language is empty. It therefore
has exactly the same dual semantics as the empty sequence: dual acceptance
holds precisely when no rooted run exists. This is a normalization into the
source induction, not a new acceptance condition. The source note at lines
356--375 and compact record at line 668 agree.

### Complementation architecture: R11--R13

Rabin printed pp. 19--30 supply the marked-tree obligations, simultaneous
runs, same-state merging, Theorem 3.1 path check, well-founded mappings,
ordinal strata, Definitions 3.5--3.6, Lemmas 3.7--3.11, and the two
half-steps. Reader lines 1214--1256 retain every one of those roles.

The reader states well-foundedness as absence of an infinite descending
obligation chain and states that successors in an obligation set occupy a
lower ordinal stratum. It locates transfinite induction at Lemmas 3.3 and
3.11 rather than allowing that phrase to replace the finite constructions.
It also retains the relevant pair-sequence lengths: Lemma 3.7 preserves the
length, Lemma 3.8 produces a same-length sequence with empty last lower set,
and the positive-length induction treats the last-lower-set-empty and
arbitrary cases as separate half-steps. The source note at lines 326--412 and
compact record at line 668 agree.

### Finite trees and their limited role: R14--R15

Rabin printed pp. 30--32 define finite binary trees as finite and
predecessor-closed, define the frontier, require both successors at every
nonfrontier node, and declare that “finite tree” henceforth means a finite
frontiered tree. The valuation excludes the frontier. The finite-tree
automaton has the extra frontier state outside the state set and the printed
transition codomain.

Reader lines 1258--1294 preserve those clauses and distinguish the roles of
Lemma 3.12, Corollary 3.13, Lemma 3.14, and Corollary 3.15. The finite witness
machinery is used inside the infinite-tree proof; it is not made into a weak
version of the full input logic. The source note at lines 482--512 and compact
record at line 670 agree.

### Rabin's emptiness argument and the two printed gaps: R16--R19

Rabin printed pp. 32--34 erase the alphabet to one letter, complement the
resulting one-tree language, convert the original language to a specified
dual language, and decide that membership by the same two half-steps. Reader
lines 1296--1391 reproduce that route and do not substitute a regular-tree
basis theorem.

The reader states the current finite table and pair sequence for each
recursive question. Its Definition 3.7 discussion retains the formal state
set while restricting states strictly below the root, so the root state may
lie outside the restricting subset.

On Rabin printed p. 34, display (3.5) requires a nonempty
`H` contained in the last upper set even though exhaustiveness requires the
empty case; the following source reduction then ranges over a power set.
Reader lines 1349--1362 range over every subset of the last upper set. The
empty choice is the direct shorter-sequence dual question, and each nonempty
choice uses the restricted table. The reader identifies the empty branch as
handbook-owned and explains finite termination of the arbitrary half-step.

The same printed page requires a nonempty base set `U_0`. Reader lines
1364--1381 instead permit `m >= 0`, retain the source's nonempty cases, and
add the handbook-owned `m = 0` case. Then the sole finite tree admits no run
from the current root state; Koenig's Infinity Lemma makes that finite
obstruction equivalent to absence of an infinite run. The finite-tree weak
monadic decision theorem remains explicitly external to Rabin, through Doner
and Thatcher--Wright. The source note at lines 413--479 and compact record at
line 670 agree about both defects, both minimum completions, and their
ownership.

### Historical complexity correction: R20

Rabin printed pp. 1 and 4 describe the procedures as elementary recursive in
Kalmar's sense. Reader lines 952--960, source-note lines 84--88 and 145--156,
and compact-record line 662 all report that as a historical source claim and
do not retain it as the handbook's complexity theorem.

Meyer printed p. 478 states the non-elementary tower lower-bound result;
printed p. 479 lists the theory of two successors and prefix and credits that
case to Meyer and Stockmeyer. The reader correctly observes that this theory
is a syntactic sublanguage of Rabin's displayed binary theory. The lower bound
therefore defeats the claimed elementary-recursive worst-case bound while
leaving decidability and effectiveness intact. Meyer is used only for this
later correction, not as a substitute for Rabin's definitions or proof.

### Applications, proof boundary, and later route: R21--R23

Rabin printed pp. 10--17 support the class-level application map at reader
lines 1393--1412: countable linear orders and related weak/countable cases,
countable unary-function structures and the related weak case, the stated
Cantor-space and unit-interval structures, the stated Boolean-algebra
structures, and the encoded Gale--Stewart determinacy statement for
`F_sigma` payoff sets. The reader neither suppresses Chapter II nor inflates
its claims.

Reader lines 1414--1428 state exactly what is reconstructed and what remains
in the complete article. Thomas's later basis-theorem route is separately
attributed and explicitly not projected backward onto Rabin's Section 3.12.
McNaughton's word theorem and the Doner/Thatcher--Wright finite-tree result are
also labelled external at their actual uses. Numbering, printed-page
locators, notation, result strength, and attribution agree with the inspected
Rabin pages throughout.

### Cross-record, bibliography, status, and rights: R24--R25

The reader's Rabin section at lines 908--1428, the source note at lines
1--614, and compact record at lines 660--672 agree on identity, definitions,
the later complexity correction, the three handbook-owned edge completions,
applications, proof boundaries, and the not-yet-admitted review status. The
adjacent compact-record boundaries at lines 658 and 674--690 keep
Trakhtenbrot, Thomas, and Thatcher--Wright separate. Its consolidated status
at lines 913--915 is also consistent with a pending Rabin review.

The five relevant bibliography entries agree with the reader and records:

- McNaughton at `handbook.bib` lines 2290--2299;
- Thomas at lines 2346--2355;
- Meyer at lines 5938--5947;
- Rabin at lines 5973--5982; and
- Thatcher--Wright at lines 5993--6002.

The Rabin identity agrees with the article title page and printed pp. 1--35;
the Meyer identity agrees with printed pp. 477--482. Rabin's printed
references corroborate the McNaughton and Thatcher--Wright article titles,
journals, years, and page ranges. Within the charter-bounded evidence set, the
DOIs, URLs, and Thomas identity are consistently recorded across the frozen
reader, detailed note, compact record, and bibliography; the external Thomas,
McNaughton, and Thatcher--Wright bodies were not part of this board's evidence
set and were not independently re-audited here.

The source note's custody and rights discussion at lines 28--90 is no broader
than the Rabin cover and the Meyer access object permit. It does not call
either source open content, does not assert a republication licence, and
treats the PDFs and renders as local research objects rather than
redistributable handbook assets. The compact record's phrase “complete
research scan” is an acquisition description, not an open-licence claim.

### Scope discipline: R28

This acceptance concerns the source fidelity of the frozen `N-c-014.d`
manuscript content only. It does not admit all of `N-c-014`, Part IX, another
part, a build, a rendered handbook page, the handbook as a whole, or human or
user acceptance. It does not convert the source-note acquisition statements
into a publication licence.

## Limitations relevant to the verdict

- Formulae, symbols, wording, and source pagination were checked from the
  original-detail page renders under the two controlling PDF hashes; OCR and
  the forbidden layout extraction played no evidentiary role.
- The Meyer review was article-complete within the official proceedings
  volume but did not audit unrelated pages of that volume.
- The shared bibliography and compact record were read as complete frozen
  objects, but this verdict substantively adjudicates only the entries,
  cross-record statements, and adjacent authority boundaries bearing on
  `N-c-014.d`, as R28 requires.
- External works named as dependencies or later routes were checked for
  attribution and nonconflation within the frozen evidence. Their technical
  bodies were not independently reviewed because they were not authorized
  Round 2 evidence.
- This is a manuscript-content source-fidelity verdict. It is not a proof-seat
  verdict, a terminology-seat verdict, a build result, a typesetting result,
  or a visual review of a rendered handbook page.

## Disposition

The frozen reconstruction satisfies R01--R25 and R28--R29. Its historical
claims, printed defects, handbook-owned completions, external dependencies,
rights boundary, and pending-review status are all stated without source
laundering or scope inflation. No minimum repair is owed by this seat because
there is no finding.

VERDICT: ACCEPT

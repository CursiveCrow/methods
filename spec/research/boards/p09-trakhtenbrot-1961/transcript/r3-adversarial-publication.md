# Round 3 adversarial publication and terminology review: `N-c-014.c`

## Seat, snapshot, and result

I reviewed the complete Frozen Round 3 snapshot as the adversarial publication
and terminology seat.  The source reconstruction is mathematically coherent,
keeps the 1961 announcement distinct from the 1962 expansion, marks its
handbook-owned finite-word repair, avoids modern-theorem and translation
laundering, and satisfies the five-part AGENTS terminology rule.  One
publication-status defect remains: two records paraphrase Math-Net's
print-only personal-use permission as permission for generic “copies.”  That
is a rights-scope inflation and is a must-fix under I27.  No other blocker or
must-fix was found.

This was a blind review.  I did not read the ledger, the chair transcript, any
Round 1 or Round 2 report, or another Round 3 report, and I did not contact
another reviewer.  I did not edit a frozen artifact.  The only file I wrote is
this assigned report.

## Competence, evidence, and prohibited-method disclosure

I am not a credentialed Russian-language specialist.  My source-language
competence for this review is working but non-specialist: I can read Cyrillic
mathematical prose, theorem labels, formula-adjacent terminology, and the
relevant technical contrasts, but I do not claim authority over fine idiom or
publication-quality literary translation.  I therefore checked the Russian
bodies against their displayed formulae, theorem structure, examples,
pagination, repeated terminology, and official archival metadata; I checked
the English reconstruction as a bounded scholarly rendering of those used
items, not as a line-by-line translation.  Nuanced specialist certification is
not checked and is not claimed.

I visually read all four announcement pages and all twenty-nine expansion
pages at original image detail.  The PDF scans and their original-detail page
renders controlled symbols, Cyrillic/Latin letter distinctions, formulae,
theorem numbering, pagination, tables, and source wording.  Only after that
visual pass did I use the two text extractions to navigate back to already
inspected passages; OCR did not control any substantive judgment.  I also read
the complete frozen reader file, source note, compact record, the specified
shared-theorem and source-navigation passages, and both bibliography entries.
I inspected the two official Math-Net records, Math-Net's controlling Terms of
Use, and the bibliographic route to the later AMS translation.  I did not
acquire or use the translation body.

I ran no test, automated checker, repository script, TeX command, build, or
interim build.  I did not inspect a handbook PDF and make no claim about
typesetting, compilation, rendered handbook pages, or final-book fitness.  The
only computation was recomputation of the seven frozen SHA-256 values as
identity labels.

## Frozen-object identity check

All seven recomputed identities matched the charter exactly.

| Frozen object | Expected SHA-256 | Recomputed result |
|---|---|---|
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1961.pdf` | `44213AEBE4DB2F1C389B812A7401138799C3DB4749C3605BA7211BBB4BAF96F9` | exact match |
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1962-expanded.pdf` | `EAB4438A7BBA2B6009374826A98A3A61FB6465C493F57B03D2C6C7385824096D` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `75E224288547CC8FA0A14C15B866C170685448257F0A04DE9F6770D7C027D999` | exact match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD` | exact match |
| `handbook/bib/handbook.bib` | `75AB70009DF4AB8B2180CFFC6987EA244ADB2F978B1D889C87009EFF17066D5C` | exact match |
| `spec/research/p09-trakhtenbrot-1961-source-note.md` | `80BEE63A6F8C275716A6BC55652AA7F1E024B8FC4E033B57D28F0E0BAF5C719C` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `EE9ED7FBF9A1F15C3AFE6A3D02752830D0D287B28277819AEAA51B771B2D1A21` | exact match |

The reading-aid hashes were not recomputed because the charter declares those
objects noncontrolling and M01 asks for the seven frozen identities.

## Original-detail visual source audit

The physical-to-printed maps were confirmed from the visible page numerals,
journal headers, running titles, and terminal matter:

- Announcement: physical `1 -> 326`, `2 -> 327`, `3 -> 328`, and `4 -> 329`.
  I visually checked every one of these four pages.  The title and journal
  identity occur on printed p. 326; the lower/upper setup and numbered theorem
  chain occupy pp. 326--329; the final page carries the historical matter,
  receipt line, and the correction belonging to an earlier cited work.
- Expansion: physical `1 -> 103`, `2 -> 104`, `3 -> 105`, `4 -> 106`,
  `5 -> 107`, `6 -> 108`, `7 -> 109`, `8 -> 110`, `9 -> 111`, `10 -> 112`,
  `11 -> 113`, `12 -> 114`, `13 -> 115`, `14 -> 116`, `15 -> 117`,
  `16 -> 118`, `17 -> 119`, `18 -> 120`, `19 -> 121`, `20 -> 122`,
  `21 -> 123`, `22 -> 124`, `23 -> 125`, `24 -> 126`, `25 -> 127`,
  `26 -> 128`, `27 -> 129`, `28 -> 130`, and `29 -> 131`.  I visually
  checked every one of these twenty-nine pages.  The visible development is
  §1 and normal form on pp. 103--109, operators on pp. 109--113, portions and
  definability on pp. 113--119, finite realization and general solutions on
  pp. 119--124, and explicit synthesis, the worked tables, finite words, and
  the weak system on pp. 124--131.  Printed pp. 126--127 visibly contain the
  two-formula example and both finite tables; p. 128 visibly invokes the
  “first” length-`t` word in the converse construction; p. 131 carries the
  terminal source matter and receipt date.

The announcement visibly records presentation by P. S. Novikov on 16 May 1961
and receipt on 29 April 1961.  The expanded article visibly records receipt on
15 May 1961.  These are not swapped or used to renumber one body by the other.

## Blocking finding

### AP3-F01 — must-fix — print-only permission is broadened to generic “copies”

**Exact frozen locations.**

- `spec/research/p09-trakhtenbrot-1961-source-note.md:71-76`, especially line
  73, says that Math-Net's Terms “permit individual noncommercial research or
  teaching copies.”
- `spec/research/p09-source-presentations-lot2-3.md:648` repeats that the Terms
  “permit individual noncommercial research or teaching copies.”

**Controlling source and source-page boundary.**  The cited Math-Net Terms of
Use, inspected on 2026-08-23, reserve reproduction, storage, and transmission
rights and state the personal-use exception specifically as permission for
individual teachers, students, and researchers to **print copies** for
noncommercial teaching or research.  They separately prohibit systematic
downloading without written permission.  The hosted works are the announcement
at printed pp. 326--329 and the expansion at printed pp. 103--131; neither
printed article body supplies a broader website-use licence.  Because this
finding concerns the archive's use terms rather than an article theorem, the
controlling permission text is the linked Terms page; the printed pages identify
the copyrighted objects to which that route provides access.

**Violated invariant and coverage.**  This violates I27 and links M03, M24,
M25, M27, and the rights component of M28.  It does not amount to an assertion
that the works are open content or redistributable—the next clauses correctly
deny both—but the first clause still describes a broader class of permitted
copies than the archive grants.

**Concrete expert-reader harm.**  “Copies” without “print” naturally includes
saved or transmitted electronic copies.  A graduate-handbook provenance record
should not turn a narrow print permission into a medium-neutral copying
permission, particularly while describing locally saved PDFs.  The later
no-redistribution sentence does not cure the intermediate overstatement: an
electronic personal copy and redistribution are different acts.

**Smallest exact correction.**  In both locations, replace

> permit individual noncommercial research or teaching copies

with

> permit individual teachers, students, and researchers to print copies for
> noncommercial teaching or research

and make the following clause read “outside that exception, the material
remains copyrighted and reproduction or republication requires written
permission.”  The existing statements that access is not an open-content
licence and that the local PDFs are not authorized for redistribution should
remain.  Recording the Terms' separate ban on systematic downloading would be
accurate but is not needed to cure the overstatement.  No source-body, theorem,
translation, or reader exposition needs to change for this finding.

## Hostile cross-artifact audit

### Source identity, version, title, translation, and acquisition status

The source note at lines 5--12, the reader at lines 487--497, compact record at
line 648, shared source navigation at lines 2341--2347, and bibliography entries
at lines 5991--6013 consistently distinguish:

- the registered four-page announcement, *Doklady Akademii Nauk SSSR* 140(2)
  (1961), 326--329, official Math-Net English title “Finite Automata and the
  Logic of Single-Place Predicates”; and
- the complete twenty-nine-page expansion, *Sibirskii Matematicheskii
  Zhurnal* 3(1) (1962), 103--131, official Math-Net English title “Finite
  Automata and the Logic of One-Place Predicates.”

The two scans visibly carry the same Russian title.  No frozen artifact silently
normalizes the official English renderings, silently turns the expansion into
the announcement, or transfers pagination and numbering.  The source note at
lines 65--69 describes the later AMS translation only as a bibliographic route,
says its body was not acquired, and does not use it as textual evidence.  The
reader at lines 778--780 claims only a bounded reconstruction and expressly
disclaims a complete line-by-line translation.  This is honest and consistent
with my language limits.

The Math-Net records support the author, journal, volume, issue, year,
pagination, language, and receipt metadata used in the frozen records.  The
bibliography gives two separate entries and preserves “Single-Place” versus
“One-Place.”  The access URLs point to the corresponding official records.  The
only provenance defect is AP3-F01's overbroad paraphrase of the use exception.

### Formal-system and normal-form reconstruction

Reader lines 499--510 correctly introduce Cyrillic И as the source's name for
the interpreted language and declare the typographic normalization
`\mathcal I`.  The domain is the positive integers, predicate variables range
over arbitrary subsets, and successor is primitive.  Equality, order, bounded
individual quantifiers, constants, and `t+k` are expressly eliminable rather
than silently primitive.  Expanded pp. 103--109 control this material; the
announcement's compressed lower/upper terminology and Theorem 1 are on pp.
326--327.  The weak system is introduced only later at reader lines 754--763
and is not conflated with `\mathcal I`.

Reader lines 512--525 correctly make “fictitious outside” semantic
independence, not textual nonoccurrence, and distinguish bounded-prefix lower
formulae from tail-dependent upper formulae.  The reported normal-form proof
architecture is complete at handbook scale.  Independently, after the source's
quantifier rearrangement and split of each individual quantifier at `t`, put
the Boolean combination into disjunctive pieces with a lower part `L` and an
upper part `U`.  Predicate witnesses for `L` and `U` can be spliced because
truth of each part is insensitive to the other's interval.  Thus the relevant
predicate quantifier distributes across the independent prefix and tail
pieces.  Repeating the move yields the finite Boolean combination of lower and
upper formulae.  This checks the gluing step that a bare “normal form follows”
would otherwise hide.

### Operators, memory, anticipation, and nonimplications

Reader lines 528--571 give a total typed stream map, anticipation `p`, the
zero-anticipation/prefix equivalence, finite-memory output and transition maps
whose arguments include the entire future suffix, weight as the least finite
state-set cardinality, the conjunction defining a finite operator, and the
finite-window canonical equations.  Expanded pp. 109--112 visually control
those distinctions.  The 1961 Л-name and 1962 Latin `A`-name are separated and
the use of `A` as a class label rather than the input-alphabet metavariable is
made explicit.

The implications and failures are correct:

- zero anticipation alone gives prefix compatibility but no finiteness or
  effectiveness;
- finite memory alone need not give bounded lookahead or continuity, because
  the external and internal maps may inspect the whole suffix;
- a finite operator has finite memory and one fixed lookahead bound; and
- the automaton-realizable class is the zero-lookahead finite subclass.

The one-state example on expanded p. 111 lets the output ask whether a `1`
occurs anywhere in the remaining input.  One state suffices, but no finite
prefix resolves the all-zero suffix case, so finite memory does not imply
bounded anticipation or recursiveness.  Expanded pp. 111--112 then use the
ultimate-periodicity boundary to show that primitive-recursive schemes are too
broad for deciding finite-state realizability or uniformly extracting
canonical equations.  Reader lines 573--580 preserve the source's use of
“periodic” while supplying the current “ultimately periodic” clarification.

### Portions, homogeneity, topology, and effectiveness

Reader lines 582--601 type a portion as a residual stream set, extend it
coordinatewise to tuples, define finite homogeneous degree, identify a basis as
the finite family of distinct portions, define the internal transition by
letter extension, and state that these are set properties/data rather than new
automaton species.  “Closed” is fixed to the Cantor product topology before the
converse theorem.  The graph and singleton examples, and the uncountability
counterexample to an unrestricted converse, agree with expanded pp. 113--116.
Independently, a zero-lookahead finite-state graph has open complement because
the first output mismatch is witnessed by a finite prefix, while its residual
graph is determined by the current finite state.  A singleton has finitely many
portions exactly when its stream has finitely many distinct suffixes, which is
equivalent to ultimate periodicity.  Finally, arbitrary unions of equivalence
classes under finite prefix insertion/removal give uncountably many
one-homogeneous stream sets, whereas there are only countably many finite
`\mathcal I`-formula strings; homogeneity therefore cannot imply definability.

I independently checked the two directions used at reader lines 603--630:

1. For a defining `\mathcal I`-formula, substitute a finite prefix and shift
   the remaining time origin.  The lower/upper normal form leaves only finitely
   many bounded-window truth patterns and hence finitely many residual formulae
   up to equivalence.  Those residuals are exactly the portions.  Conditioning
   one more input letter computes the next residual, so the internal transition
   is effective without an emptiness oracle.
2. For a homogeneous set with finite basis, encode the current basis member by
   the bound state predicates with the literal initial vector selecting the
   original set.  The quantifier-free current/next matrix follows exactly the
   permitted one-letter transitions; the bound choice predicate records a
   permitted branch.  The paths so described form the closure of the original
   set.  Closedness is therefore the necessary equality step, not decorative
   topology.  Conversely, the displayed finite-state existential recurrence
   defines a projection of a closed finite-state path set; compactness makes
   the projection closed, and the finite state vector bounds its portions.
3. Boolean connectives give complement and finite union, while existential
   predicate quantification is projection.  This yields the stated least
   closure class.  It does not answer the announcement's open question about
   the exact Borel/projective classes.

The recurrence at reader lines 608--624 has the required free input predicate,
bound state predicates, bound choice predicate, quantifier-free current/next
matrix, and literal initial state.  It does not silently define an arbitrary
union of basis portions.  Reader lines 632--639 also preserve the exact
effectiveness split: residual transition is unconditional; selecting a
nonempty output portion requires truth/nonemptiness decisions; a “conditional
`\mathcal I`-algorithm” assumes that oracle; Putnam removes the condition only
for the displayed recurrent fragment.  Expanded pp. 113--119 and announcement
pp. 326--328 control these claims.

### Finite realization, graph versus solution, and generality

For reader lines 641--651 and source pp. 119--120, I independently checked the
continuous-total-operator argument.  An exactly defined graph is homogeneous,
so it has finitely many residual graph portions.  On each nonempty residual,
continuity of the next output coordinate over compact Cantor input space is
uniform: some finite input window fixes that coordinate.  Taking the maximum
over the finitely many residuals gives one anticipation bound.  The residual
index is finite memory, and its cardinality gives the stated weight bound.  No
hidden global continuity or closedness assumption is inserted elsewhere.

Expanded §4 Theorem 2, represented at reader lines 649--651, is strictly
weaker.  Total functionality plus finitely many graph residuals lets the output
and next residual be functions of the residual state and the entire remaining
input suffix, which is finite memory in the source's sense.  Without
continuity, there is no finite prefix on which to take a uniform maximum, so no
anticipation bound and no finite-operator conclusion follows.

Reader lines 653--663 correctly separate an exact graph definition from an
operator whose graph is merely contained in a relation.  Announcement Theorem
`4'` is correspondingly an existence theorem for a closed homogeneous
relation: a continuous solution can be replaced by a finite bounded-weight
solution; a zero-anticipation solution can be replaced by a bounded-weight Л
solution.  The open-relation analogue is separately reported and does not
inherit the closed case's weight bound.  The reader does not turn any-solution
existence into an exact graph claim.

Reader lines 665--679 state both quantifiers needed for a general solution.
Soundness requires every parameter substitution of the named operator class to
yield a solution.  Completeness requires every solution of that class to arise
from some parameter operator.  Replacing the named class throughout—not merely
for the outer operator—gives general zero-anticipation solution.  The finite
parameter tuple is typed as streams and functions of the input, so “general”
cannot be misread as merely “one solution.”

For Theorem 5/expanded Theorem 3 at reader lines 681--692 and source pp.
121--124, the deletion proof checks as follows.  Starting from the finite
residual family, iteratively delete empty residuals and any residual from which
some input prefix has no extendible output choice in the surviving family.
Finiteness makes this process stabilize.  If the initial residual is deleted,
any purported zero-anticipation solution would have to trace an already-deleted
branch, so there is no solution.  If it survives, parameter bits select among
the surviving output choices and the residual transition supplies finite
memory.  Every finite generated prefix remains compatible with the relation;
closedness converts all-prefix compatibility to membership.  Conversely, every
zero-anticipation solution uses only surviving choices, so its choices can be
encoded by a parameter stream.  This establishes both the soundness and
completeness clauses and the weight bound.  Testing emptiness during deletion
is exactly why the arbitrary closed-formula construction remains conditional.

Expanded Theorem `3'`, source p. 124 and reader lines 692--697, fixes one
lookahead bound `p`.  Shifting/padding the first `p` output places converts the
class to the zero-anticipation case and back.  Thus the resulting finite
operator parametrizes solutions with that same bound; nothing quantifies one
parametrizer over unbounded `p`.

### Explicit synthesis and the finite-word edge case

Reader lines 701--714 correctly distinguish an explicit output definition from
an arbitrary implicit relation.  Normal form gives finitely many shifted
residual formulae, hence finite memory.  Semantic independence outside
`[1,t+p]` is exactly the anticipation-`p` criterion; `[1,t]` is the
zero-anticipation case.  In the prefix-controlled case, conditioning on the
first input column produces the output and the next shifted formula.  Because
only finitely many residual formulae arise, iteration terminates with canonical
output and transition tables.  Expanded pp. 126--127 visibly instantiate this
construction with exactly two residual formulae and two printed tables; the
example illustrates the construction and is not promoted into a separate
generality proof.

Reader lines 716--727 correctly derive the finite-word maps.  Two infinite
extensions of one length-`t` input agree through `t`; zero anticipation makes
their length-`t` outputs equal, and applying the same observation at every
`s <= t` proves prefix compatibility.  The definitions at lines 729--741 then
use the lengthwise ranges for automaton-enumerability and the terminal output
for automaton-decidability, rather than confusing the infinite-stream range
with a finite-word language.

The two directions of expanded §5 Theorem 2 also check.  An enumerating finite
transducer gives a finite-state test for whether an output word has a compatible
input run.  Conversely, a nonempty prefix-closed properly extendible decidable
language supplies an accepted word at every positive length; the construction
keeps an accepted input prefix when possible and otherwise takes the first
accepted length-`t` extension, producing a prefix-compatible enumerator.  The
source's printed hypotheses omit nonemptiness.  The empty language is decided
by the constant-zero recognizer and satisfies prefix closure and “every member
has a longer extension” vacuously, but a total length-preserving operator on
the source's binary input has a nonempty range at each positive length.  Printed
p. 128 visibly exposes the missing seed by requesting the first length-`t` word.
Reader lines 743--752 add `L != empty`, explain exactly why, and label the
addition handbook-owned.  There is no silent source repair.

Finally, reader lines 754--763 and expanded pp. 130--131 define `\mathcal I'`
by eventually-zero predicate ranges, define a special beginning by permanent
zero after its endpoint, and distinguish it from an arbitrary prefix.  Theorem
3 gives existence of a recognizing `A`-operator for every `\mathcal I`-formula
but effective construction only for an `\mathcal I'`-formula, with the source's
explicit Büchi attribution preserved.  Existence is not laundered into an
algorithm.

### Announcement/expansion and modern-theorem nonconflation

The numbered-result comparison is publication-safe:

- announcement Theorem 1 is paired with the expanded §1 normal form, with each
  source's own locator;
- announcement Theorems 2--3 are compared with the expanded §3 development
  without assigning the expansion the announcement's numbers;
- announcement Theorem 4 is paired with expanded §4 Theorem 1;
- announcement Theorem `4'` remains the announcement's relation-existence
  formulation, including its separately qualified open-relation clause;
- announcement Theorem 5 is paired with expanded §4 Theorem 3; and
- expanded §4 Theorem 2, Theorem `3'`, and the detailed §5 material retain their
  expanded-article standing rather than being retrofitted into 1961.

The shared theorem at `logic-in-computer-science.tex:811-825` expressly labels
the displayed regular/MSO equivalence a modern formulation, identifies the
different Büchi, Elgot, and Trakhtenbrot packages, and states that the compound
name does not assert verbatim occurrence in each source.  Reader lines 765--800
make the same boundary and use Thomas §3.1 only for the modern proof route.
Source navigation at lines 2341--2347 keeps the Büchi precursor, registered
article, Elgot article/errata, both Trakhtenbrot bodies, Thomas survey, and Rabin
source separate.  This prevents a familiar theorem label from laundering a
later proof or a neighboring author's encoding into either Russian source.

Historical remarks about Church, Büchi, Elgot, Putnam, Novikov, and priority
are consistently reported as source-time claims or later-source attribution,
not independently adjudicated priority.  The source-time conditional boundary
is not erased by modern decidability knowledge.

## Complete AGENTS terminology audit

I applied all five requirements—necessity, exact definition/axiomatic
introduction, standing, nonredundancy, and later use—at first use.  The terms
below are all eliminable into the displayed definitions or explicitly declared
source names; none is a hypothetical theoretical object introduced in place of
an owed construction.

| Name or distinction | First-use audit | Later use and nonredundancy | Status |
|---|---|---|---|
| `\mathcal I` | Lines 499--510 give the source glyph, normalization, domain, predicate range, primitive syntax, and standing as an interpreted language. | It is used in every definability and synthesis theorem and is separated from automata and Büchi's weak system. | checked-clean |
| fictitious outside; lower/upper `t`-formula | Lines 512--517 give semantic and interval-dependence definitions. | The prefix/tail distinction is necessary for the normal form and finite-residual arguments at lines 517--525 and 603--639. | checked-clean |
| operator; anticipation; zero anticipation | Lines 528--536 type the total map and give the exact dependence and prefix-equivalence clauses. | They classify the finite-realization, solution, and word constructions; zero anticipation is not treated as finite memory. | checked-clean |
| finite memory; weight | Lines 538--554 give finite state data, whole-suffix function types, and least-cardinality definition. | The terms state Theorems 1--3 and expose the one-state nonrecursive counterexample; weight is not confused with anticipation. | checked-clean |
| finite operator; Л-operator; `A`-operator | Lines 556--571 give the conjunction, canonical window equations, exact zero-lookahead subclass, version-specific letters, standing, and alphabet-letter disambiguation. | The distinctions are required by every realization/general-solution theorem and the strict Theorem 2 nonimplication. | checked-clean |
| ultimately periodic | Lines 573--576 give an eliminable preperiod/period definition and identify it as current terminology for the source's “periodic.” | It is used in the synthesis negative boundary and singleton example, so the modernization is neither silent nor idle. | checked-clean |
| portion; homogeneous degree; basis; internal transition | Lines 582--594 define each as a residual, cardinal bound, finite list, or transition datum of a stream set and explicitly deny automaton-kind standing. | These objects drive both definability directions, finite realization, and deletion synthesis. | checked-clean |
| closed | Line 596 fixes Cantor-product topology before any theorem needs it. | It is indispensable to the converse, recurrence, finite-prefix limit step, and general-solution soundness. | checked-clean |
| conditional `\mathcal I`-algorithm | Lines 632--639 define the assumed truth oracle and distinguish the Putnam-unconditional fragment. | It qualifies the external-choice and deletion constructions; it is not a completion slogan. | checked-clean |
| solution | Lines 653--657 define graph containment and contrast exact graph definition. | The distinction is immediately required by Theorem `4'` and all general-solution claims. | checked-clean |
| general `A`-solution; general zero-anticipation solution | Lines 665--679 type the parameter streams and give both completeness and soundness quantifiers; replacement throughout defines the broader class. | The names are required by Theorem 5/Theorem 3 and fixed-class parametrization, not redundant with existence. | checked-clean |
| explicit definition | Lines 701--709 display the exact formula form, standing as an output definition, and anticipation criteria. | It controls the residual synthesis and worked tables and is distinguished from implicit relations. | checked-clean |
| word maps `T_t` | Lines 716--727 give domain, codomain, extension independence, and compatibility. | They are required to type both finite-word definitions; the stream range is not substituted for them. | checked-clean |
| automaton-enumerable; automaton-decidable | Lines 729--741 give exact lengthwise-range and terminal-output definitions. | They are used by both directions of Theorem 2 and differ as generation versus recognition. | checked-clean |
| proper extendibility | Lines 743--750 first state its eliminable content—every member has a longer extension—and then use the concise label with prefix closure and nonemptiness. | The distinction supplies the recursive construction's next level and is not allowed to hide the separate nonempty seed. | checked-clean |
| `\mathcal I'`; special beginning | Lines 754--758 give the eventually-zero range and the exact permanent-zero endpoint condition. | They are required by expanded Theorem 3 and distinguish arbitrary existence from effective weak-system construction. | checked-clean |

No definition-after-use, standing ambiguity, redundant technical name, unused
distinction, or unsupported hypothetical name remains.  In particular,
“portion,” “basis,” and “internal transition” are not promoted into invented
automaton types; `A` is not left ambiguous between an alphabet and the
expansion's source class; and the modern compound theorem name is an explicitly
qualified editorial label rather than a purported literal source theorem.

## Status and publication-scope audit

The source note at lines 14--18 and 450--461 says the reconstruction is not yet
admitted and still requires three independent reviews.  Compact-record line
658 says review remains required and disclaims Russian-specialist review.
Compact-record line 911 says only that the two bodies are body-sufficient and
reconstructed at distinct strengths, while line 913 explicitly defines “body
sufficient” as source acquisition rather than reconstruction review, proof
checking, build, visual handbook inspection, or human review.  Those clauses
prevent premature completion or admission inflation.

The reader's “source-controlled” descriptions at lines 774--780 are bounded by
their exact source-version and translation disclaimers and do not override the
explicit pending-review status in the records.  The presentation does not claim
literal Büchi 1960 reconciliation, `N-c-014` overall completion, Part IX
admission, handbook rendering, final-book completion, human verification, or
user acceptance.  Subject to AP3-F01, the content is fit for a graduate
handbook at manuscript-content level within `N-c-014.c` only.

## Invariant disposition

| Invariant | Disposition | Audit result |
|---|---|---|
| I01 | checked-clean | Announcement/expansion identities, pagination, numbering, and strength remain distinct. |
| I02 | checked-clean | Same Russian title and distinct official “Single-Place”/“One-Place” English titles are explicit. |
| I03 | checked-clean | Cyrillic И is declared as typographic `\mathcal I` and stands as the interpreted language. |
| I04 | checked-clean | Positive-integer and arbitrary-subset domains, primitive successor, and eliminable conveniences are exact. |
| I05 | checked-clean | Semantic fictitiousness and unequal lower/upper dependence are defined. |
| I06 | checked-clean | Effective normal form and all reported proof moves, including witness splicing, check. |
| I07 | checked-clean | Whole-suffix memory, bounded anticipation, finite operator, and version-specific Л/`A` class remain distinct. |
| I08 | checked-clean | Weight and the one-state unbounded/nonrecursive future-dependence example are correct. |
| I09 | checked-clean | Portion, homogeneous degree, basis, and transition stand as stream-set properties/data. |
| I10 | checked-clean | Definable implies homogeneous; only the closed homogeneous converse is claimed; counterexamples remain visible. |
| I11 | checked-clean | Free input, bound state/choice predicates, literal initial state, current/next matrix, and converse are preserved. |
| I12 | checked-clean | Closure characterization and the source's open descriptive-set question are kept separate. |
| I13 | checked-clean | Internal transition is unconditional; external selection is conditional; Putnam is fragment-bounded. |
| I14 | checked-clean | Compact uniformity, one lookahead maximum, finite residual memory, and weight bound are all present. |
| I15 | checked-clean | Expanded Theorem 2 concludes only finite memory without continuity. |
| I16 | checked-clean | Exact graph and relation solution are distinguished; Theorem `4'` has the right standing and clauses. |
| I17 | checked-clean | Both general-solution quantifiers and both operator classes are explicit. |
| I18 | checked-clean | Stable deletion, both branches, parameter selection, closedness, weight, and conditionality check. |
| I19 | checked-clean | Theorem `3'` is separately fixed at each lookahead bound. |
| I20 | checked-clean | Explicit-definition scope, semantic criteria, finite residuals, equations, and example locator are exact. |
| I21 | checked-clean | Typed word maps, both definitions, both directions, and the handbook-owned nonempty repair are explicit. |
| I22 | checked-clean | Eventually-zero `\mathcal I'`, special beginnings, existence/effectivity split, and Büchi attribution are exact. |
| I23 | checked-clean | Modern regular/MSO formulation is declared modern and not substituted for a Russian source statement. |
| I24 | checked-clean | Historical and priority remarks remain attributed reports rather than new adjudications. |
| I25 | checked-clean | Bounded scholarly reconstruction and no specialist/line-by-line translation claim are explicit. |
| I26 | checked-clean | Every new technical name passes necessity, definition, standing, nonredundancy, and use. |
| I27 | finding-linked | AP3-F01: generic “copies” overstates the Terms' print-copy exception. |
| I28 | checked-clean | Only permitted reading, derivation, provenance, visual, and seven-hash evidence was used; no software gate is claimed. |
| I29 | checked-clean | All status language remains bounded to `N-c-014.c` and excludes neighboring/final gates. |
| I30 | checked-clean | Blindness and reviewer noncontact were maintained. |

## Mandatory coverage disposition

| Point | Disposition | Evidence/result |
|---|---|---|
| M01 | checked-clean | All seven frozen hashes were recomputed before substantive review and match exactly. |
| M02 | checked-clean | All `4 + 29` source pages were visually read at original detail; both physical-to-printed maps were confirmed. |
| M03 | finding-linked | Identities, dates, journals, pagination, titles, routes, and order check; AP3-F01 remains in the rights paraphrase. |
| M04 | checked-clean | Non-specialist Russian competence and exact scan/metadata/OCR evidence limits are disclosed; no specialist certification is implied. |
| M05 | checked-clean | `\mathcal I` and `\mathcal I'` syntax, domains, successor, eliminable extensions, and standing check. |
| M06 | checked-clean | Fictitiousness, lower/upper forms, announcement Theorem 1, expanded normal form, and reported proof moves check. |
| M07 | checked-clean | Operator type, anticipation, prefix equivalence, whole-suffix memory, weight, finite windows, `A`-standing, and nonimplications check. |
| M08 | checked-clean | Primitive-recursive recognition/synthesis boundary and one-state nonrecursive example check. |
| M09 | checked-clean | Portions, tuple extension, homogeneity, basis, transition, examples, and uncountability counterexample check. |
| M10 | checked-clean | Independent finite-residual derivation and effective letter-transition construction are recorded above. |
| M11 | checked-clean | Independent recurrence/closure derivation preserves Cantor closedness, compact projection, literal initial state, and closure operations. |
| M12 | checked-clean | Unconditional internal transition, conditional nonemptiness/output selection, and recurrent-fragment Putnam scope are exact. |
| M13 | checked-clean | Independent compact-uniformity proof supplies one bound, residual memory, and the degree/weight bound. |
| M14 | checked-clean | Theorem 2's whole-suffix finite-memory construction is verified without continuity or lookahead inflation. |
| M15 | checked-clean | Graph versus solution and every closed/open clause of announcement Theorem `4'` check. |
| M16 | checked-clean | Both soundness/completeness quantifiers and parameter standing for both general-solution classes check. |
| M17 | checked-clean | Independent stable-deletion proof covers deletion, no-solution, survivor, parameters, closedness, degree, and conditionality. |
| M18 | checked-clean | The shift reduction and conclusion are fixed separately for each `p`; no unbounded class is claimed. |
| M19 | checked-clean | Explicit form, semantic criteria, shifted-residual termination, equations, and pp. 126--127 example role check. |
| M20 | checked-clean | Both word definitions and theorem directions check, including prefix closure, extension, empty counterexample, and nonempty seed. |
| M21 | checked-clean | `\mathcal I'`, special beginnings, Theorem 3, Büchi attribution, and effective/non-effective split check. |
| M22 | checked-clean | Announcement Theorems 1--5 and `4'` were compared with the expansion without number, detail, or title transfer. |
| M23 | checked-clean | Shared theorem and Thomas paragraph explicitly prevent compound-name folklore from becoming original-source wording. |
| M24 | finding-linked | Reader/source note/compact/shared theorem/bibliography reconcile except for AP3-F01's repeated rights phrase. |
| M25 | finding-linked | Mathematical locators, theorem numbers, formulae, citations, history, titles, and strength qualifiers check; AP3-F01 affects the Terms qualifier. |
| M26 | checked-clean | Complete five-part AGENTS audit is reported above; no terminology violation remains. |
| M27 | finding-linked | No hidden topology, continuity, operator collapse, source/translation/priority/status laundering, or false mathematical compression found; AP3-F01 is rights inflation. |
| M28 | finding-linked | Topic scope and no-test/no-build boundary check; the rights component remains linked to AP3-F01. |

Because AP3-F01 is a must-fix in two frozen records, the current snapshot cannot
be accepted.  Correcting it is a content edit and therefore requires a newly
hash-pinned blind round under the charter; this report does not pre-accept that
future snapshot.

VERDICT: REJECT — AP3-F01

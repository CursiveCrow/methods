# Round 3 source-fidelity, language, and evidence review

## Disposition

No blocker, must-fix, should-fix, or unresolved source-language finding was
found.  The seven recomputed identities match the Frozen Round 3 table; all
thirty-three controlling source pages were read visually at original detail;
and the reader, source note, compact record, shared theorem, bibliography, and
consolidated status agree at the distinct 1961-announcement and 1962-expansion
strengths.  No finding identifier is opened in this report.

## Source-language competence and evidence boundary

I am not a native Russian speaker, a human credentialed Slavist, or a certified
Russian-language specialist, and this verdict must not be represented as such a
specialist certification.  I have working reading competence in Cyrillic
mathematical Russian sufficient to parse the definitions, theorem statements,
proof transitions, qualifications, and terminology in these two bodies.  I
checked the Russian prose directly against the formulae, headings, numbering,
and surrounding argument on the scans.  The rendered page images and the two
frozen PDFs controlled every source-language and mathematical judgment.  The
layout text was used only to navigate back to already inspected page images;
no OCR word or symbol controlled a conclusion.  The bounded English
reconstruction consistently says that it is not a line-by-line translation
and does not claim Russian-specialist certification
(`handbook/parts/p09/presentations/n-c-014.tex:774-780`;
`spec/research/p09-trakhtenbrot-1961-source-note.md:14-18,78-104`).

## Frozen identity check

The seven SHA-256 values were recomputed before substantive review and used
only as identity labels.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1961.pdf` | `44213AEBE4DB2F1C389B812A7401138799C3DB4749C3605BA7211BBB4BAF96F9` | match |
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1962-expanded.pdf` | `EAB4438A7BBA2B6009374826A98A3A61FB6465C493F57B03D2C6C7385824096D` | match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `75E224288547CC8FA0A14C15B866C170685448257F0A04DE9F6770D7C027D999` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD` | match |
| `handbook/bib/handbook.bib` | `75AB70009DF4AB8B2180CFFC6987EA244ADB2F978B1D889C87009EFF17066D5C` | match |
| `spec/research/p09-trakhtenbrot-1961-source-note.md` | `80BEE63A6F8C275716A6BC55652AA7F1E024B8FC4E033B57D28F0E0BAF5C719C` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `EE9ED7FBF9A1F15C3AFE6A3D02752830D0D287B28277819AEAA51B771B2D1A21` | match |

The source-note byte counts also agree with the frozen local objects: 566,358
bytes for the announcement PDF, 1,884,181 bytes for the expansion PDF, 23,018
bytes for the announcement reading aid, and 160,210 bytes for the expansion
reading aid (`spec/research/p09-trakhtenbrot-1961-source-note.md:20-60`).

## Complete visual inspection and physical-to-printed map

Every page was inspected through its original-detail rendered image, with the
PDF retained as the source identity.

- Announcement `rendered/page-1.jpg` through `page-4.jpg` map respectively to
  printed pp. 326, 327, 328, and 329.  The title page prints the 1961 volume and
  issue, the common Russian title, presentation by P. S. Novikov on 16 May
  1961, and printed p. 326.  Printed p. 329 records receipt on 29 April 1961;
  its post-bibliography correction concerns the earlier cited paper (2), not
  the four-page announcement.
- Expansion `expanded-rendered/page-01.jpg` through `page-29.jpg` map
  continuously to printed pp. 103 through 131, so physical page (j) has
  printed number (j+102).  Printed p. 103 gives volume III, number 1,
  January--February 1962 and the same Russian title.  Printed p. 131 records
  receipt on 15 May 1961 and contains the article bibliography.

This confirms the page map, order, theorem locators, and dates recorded at
`spec/research/p09-trakhtenbrot-1961-source-note.md:20-69`.  The official
Math-Net records independently confirm B. A. Trakhtenbrot, *Doklady Akademii
Nauk SSSR* 140(2) (1961), 326--329, “Finite automata and the logic of
single-place predicates,” and *Sibirskii Matematicheskii Zhurnal* 3(1) (1962),
103--131, “Finite automata and the logic of one-place predicates.”  The two
scans print the same Russian title.  The bibliography preserves the distinct
English renderings and access routes at
`handbook/bib/handbook.bib:5991-6013`.

The Math-Net access route is public but its terms reserve copyright, permit
individual teachers, students, and researchers to print copies for
noncommercial teaching or research, and require permission for reproduction or
republication.  The frozen note therefore correctly treats
the PDFs as local research objects and infers no open-content or redistribution
licence (`spec/research/p09-trakhtenbrot-1961-source-note.md:65-76`).  The later
AMS translation is identified only as an unacquired bibliographic route and is
not used as textual evidence.  Source order is explicit throughout: the 1961
Doklady announcement is the registered item; the 1962 journal article is the
complete expansion; the later translation is not a controlling body.

## Source-to-reader reconciliation

### Formal system and normal form

Printed expansion pp. 104--105 define the interpreted system И: individuals
range over (1,2,\ldots), monadic variables over arbitrary predicates on that
domain, and immediate successor is primitive.  Printed p. 105 explicitly
eliminates equality, order, bounded individual quantifiers, constants, and
(t+k)-style conveniences.  The reader introduces the typographical
normalization \(\mathcal I\), defines its standing as the interpreted formal
language, and separates it from both automata and B\"uchi's weak finite-set
system (`n-c-014.tex:499-510`).  Expansion pp. 130--131 separately define
\(\mathcal I'\) by restricting predicate variables to eventually-zero
predicates; the reader does not transfer that restriction back to
\(\mathcal I\) (`n-c-014.tex:754-763`).

The semantic definition on expanded pp. 105--106 makes fictitious occurrence
outside an interval invariance under changes outside that interval.  It is not
syntactic nonoccurrence.  Announcement pp. 326--327 and expansion pp. 106--109
give the lower/upper \(t\)-formula split and normal form.  The reader accurately
reports the unequal dependencies, effective transformation, and every proof
move it names: predicate prenexing before individual quantifiers, inward
movement/elimination of the individual quantifiers, splitting at (t), and
distribution of a remaining predicate quantifier after the finite overlap
pattern has been fixed (`n-c-014.tex:512-525`).  The announcement's numbered
Theorem 1 and the expansion's unnumbered Section 1 theorem are not assigned one
another's numbering.

### Operators, anticipation, memory, and the negative boundary

Expansion pp. 109--111 define total stream operators, anticipation (p), the
prefix equivalence at (p=0), finite memory using external and internal
functions of the entire future suffix, weight as the least state-set
cardinality, and finite operators as finite-memory operators with bounded
anticipation.  The reader reproduces the whole-suffix equations before the
finite-window equations and therefore does not collapse finite memory into
bounded lookahead (`n-c-014.tex:527-562`).  Its four-way separation of zero
anticipation, finite memory, finite operator, and automaton-realizable
zero-anticipation operator is exact.  Announcement pp. 327--328 print Cyrillic
Л for the last class; expansion p. 111 prints Latin (A).  The normalization,
standing, and nonidentity with the input-alphabet letter are declared where the
term is introduced (`n-c-014.tex:563-571`).

Expansion p. 111 supplies the one-state finite-memory operator whose output
asks whether a future input value is 1; its unbounded future dependence is not
recursive.  Expansion pp. 111--112 define the source's “periodic” stream with a
finite preperiod and prove the two primitive-recursive-scheme negative results:
recognizing ultimate periodicity, and synthesizing canonical finite-state
equations even for the guaranteed-periodic reduction, are algorithmically
impossible.  The reader states exactly that boundary and does not infer
effectivity from either zero anticipation or finite memory alone
(`n-c-014.tex:551-580`).

### Portions, homogeneity, and definability

Expansion pp. 113--116 define Cantor-space intervals, portions, their
coordinatewise tuple version, homogeneous degree, bases, and the internal and
external transition functions.  The reader gives these as properties/data of
stream sets rather than as invented automaton types (`n-c-014.tex:582-601`).
The graph, singleton, and uncountability examples on printed p. 115 are all
reported at their exact strengths: a zero-anticipation operator with (k)
memory states has a closed graph homogeneous of degree at most (k); a
singleton is homogeneous exactly for an ultimately periodic stream; and the
uncountable one-homogeneous family defeats the converse to definability.

I independently reconstructed the forward definability argument on printed
pp. 116--118.  Put a defining formula into the lower/upper normal form.  After
fixing a finite prefix, every lower part becomes one of finitely many Boolean
functions of the fixed bounded window, while the shifted upper parts retain
only one of finitely many residual formula forms.  Hence only finitely many
semantic portions occur.  Appending one input bit sends a residual to another
residual, so enumeration of those finitely many forms yields the internal
transition effectively.  This validates the reader's forward claim at
`n-c-014.tex:603-606` without using the converse or an automata-folklore
shortcut.

I also independently reconstructed the converse on printed pp. 115--119.  For
a finite basis (M_1,\ldots,M_k), the portion map supplies the deterministic
internal transition.  A choice predicate selects a permitted first bit at each
basis member, producing the covering zero-anticipation operator of pp. 115--116.
Its image lies in \(\overline M\), and every point of \(\overline M\) is obtained
by a suitable choice stream.  When (M) is closed, the image is exactly (M),
and expanding the finite-state equations yields the existential-predicate,
fixed-initial-state recurrence printed on p. 118.  Conversely, the local
current/next recurrence is the projection of a compact closed finite-state
constraint set, hence is closed, and only finitely many residual state
conditions occur, hence it is homogeneous.  Boolean closure and predicate
projection then give exactly the full closure characterization on p. 118.  The
reader retains every necessary hypothesis, the literal initial state, the free
input predicate, bound state and choice predicates, and the quantifier-free
matrix (`n-c-014.tex:603-630`).

The effectiveness split is also exact.  The internal residual transition is
obtained from the finite formula family.  The external choice requires knowing
which candidate portions are empty, so arbitrary construction is conditional
on truth/nonemptiness decisions.  Printed p. 119 applies Putnam only to the
existential-predicate recurrent fragment.  The reader preserves both limits at
`n-c-014.tex:632-639` and again for the stable-deletion construction at
`n-c-014.tex:687-699`.

### Finite realization and general solutions

Although M13--M18 are not the primary allocation of this seat, every related
reader claim was checked because the mandate covers every source claim.  On
printed pp. 119--120, a continuous total operator with \(\mathcal I\)-definable
graph has a closed homogeneous graph.  Compact uniform continuity gives a
finite lookahead bound on each of finitely many nonempty portions, their maximum
is one global anticipation bound, and the portion basis gives finite memory and
the weight bound.  Expanded Section 4, Theorem 2 removes continuity and retains
only finite memory (with the source's weight bound), not finite-operator
standing.  The reader states the unequal conclusions without importing hidden
continuity (`n-c-014.tex:641-651`).

The graph/solution distinction at `n-c-014.tex:653-663` matches expansion
p. 119 and announcement p. 328: defining exactly a graph is stronger than an
operator whose graph is contained in a relation.  Announcement Theorem \(4'\)
has both closed-relation clauses and the separate open-relation qualification,
with no weight bound claimed for the latter.  The two quantifiers in general
(A)-solution and general zero-anticipation solution match announcement p. 328
and expansion pp. 120--121: every solution of the named class arises by a
parameter substitution of that class, and every such substitution yields a
solution (`n-c-014.tex:665-679`).

Announcement Theorem 5 and expanded Section 4, Theorem 3 are faithfully
reconciled at `n-c-014.tex:681-699`.  Printed pp. 121--124 give the stable
deletion: remove empty basis portions, then remove a predecessor when neither
output continuation survives; deletion of the initial formula is the
no-solution branch.  A surviving stable family supplies parameter choices and
finite memory, while closedness converts finite-prefix compatibility into
membership.  The arbitrary formula case remains conditional on the emptiness
questions.  Expanded Theorem \(3'\) on p. 124 is separately quantified for each
fixed (p); neither the reader nor the records turn it into one parameterizer
over unbounded lookahead.

### Explicit synthesis, finite words, and \(\mathcal I'\)

Expansion pp. 124--127 distinguish explicit definitions from implicit graph
formulae, give the finite-memory conclusion, characterize anticipation (p)
by semantic independence outside \([1,t+p]\), and characterize the
zero-anticipation class by independence outside \([1,t]\).  The unconditional
algorithm is kept to the source's upper-controlled zero-shift (t)-formula
case: fix the first input column, compute the first output, form the shifted
residual formula, and repeat.  Section 1 normal form bounds the residual family,
so the process terminates and its finite formulas give the canonical output and
transition functions.  The pp. 126--127 example produces exactly two residual
formulae and prints both tables.  The reader's compressed account at
`n-c-014.tex:701-714` does not enlarge this syntactic unconditional case into
an unconditional algorithm for every semantically equivalent formula.

For printed pp. 127--129, the source considers word lengths (t=1,2,\ldots).
The reader first derives the typed maps \(T_t:A^t\to B^t\) and their extension
independence and prefix compatibility, then defines automaton-enumerability by
their lengthwise ranges and automaton-decidability by the recognizer's terminal
output (`n-c-014.tex:716-741`).  These types prevent the stream range from
being mistaken for a finite-word language.

I checked both directions of Section 5, Theorem 2.  On pp. 127--128, an
enumerator explicitly yields the recognizer formula asserting that some input
word has produced the proposed output at every position through (t).  In the
other direction, p. 128 maps an accepted input word to itself; otherwise it
takes the greatest accepted prefix and the lexicographically first accepted
length-(t) extension.  Prefix closure and proper extendibility supply that
extension once a seed exists.  The printed theorem omits the seed condition:
the empty language is decided by the constant-zero operator and satisfies the
two printed conditions vacuously, but a total length-preserving operator has a
nonempty range at every positive length.  Adding nonemptiness is therefore the
smallest exact correction.  The reader states it, explains the counterexample,
and marks ownership rather than attributing it to Trakhtenbrot
(`n-c-014.tex:741-752`).

Expansion pp. 130--131 then define \(\mathcal I'\), “special beginning,” and
Theorem 3.  A special beginning ends only where the underlying eventually-zero
predicate is thereafter zero.  For every \(\mathcal I\)-formula the theorem
asserts existence of a recognizing (A)-operator; effective construction is
asserted only when the formula is in \(\mathcal I'\), and that effective clause
is explicitly attributed to B\"uchi.  The reader preserves all three
distinctions (`n-c-014.tex:754-763`).

### Nonconflation, terminology, and publication status

The announcement/expansion comparison is exact:

| 1961 announcement | 1962 expansion | Reader treatment |
|---|---|---|
| Theorem 1, pp. 326--327 | Section 1 unnumbered normal-form theorem, pp. 108--109 | both locators named; no number transfer |
| Theorem 2, p. 327 | Section 3, Theorem 1, pp. 116--118 | definability-to-homogeneity |
| Theorem 3, p. 328 | Section 3, Theorems 2 and \(2'\), p. 118 | closed homogeneous converse and recurrent form |
| Theorem 4, p. 328 | Section 4, Theorem 1, pp. 119--120 | continuous definable graph gives finite realization |
| Theorem \(4'\), p. 328 | no expansion theorem number silently assigned | relation-solution existence kept at announcement locator |
| Theorem 5, pp. 328--329 | Section 4, Theorem 3, pp. 121--124 | no-solution/general-solution alternative |
| no transferred number | Section 4, Theorem 2 and \(3'\); Section 5 results | expansion-only numbering and strength retained |

The modern shared theorem explicitly labels its displayed regular/MSO sentence
as modern and immediately enumerates the distinct B\"uchi, Elgot, and
Trakhtenbrot encodings and packages
(`handbook/parts/p09/logic-in-computer-science.tex:811-825`).  The adjacent
reader paragraph likewise treats Thomas's Section 3.1 construction as a later
synthesis, not a transcription of either Russian source or a repair imported
into them (`n-c-014.tex:765-800`).  No compound-name folklore is laundered into
the announcement.

The complete AGENTS terminology rule was applied at first use.  In particular,
\(\mathcal I\), fictitious occurrence, lower/upper (t)-formula, anticipation,
finite memory, weight, finite operator, (A)-operator, portion, homogeneous
degree, basis, solution, general solution, explicit definition,
automaton-enumerability, automaton-decidability, and special beginning are each
defined before use; their standing is stated; neighboring notions are
distinguished; and each distinction is used later.  Descriptive phrases such as
“finite-word bridge” and “handbook-owned correction” remain metalinguistic and
do not masquerade as new mathematical objects.  No unused or standing-ambiguous
technical name was found.

Finally, the source note, compact record, shared theorem, bibliography, and
consolidated status are mutually consistent:

- `spec/research/p09-trakhtenbrot-1961-source-note.md:1-18,427-461` says the
  bodies are acquired and reconstructed but independent scholarly admission is
  still pending.
- `spec/research/p09-source-presentations-lot2-3.md:646-658,900-913` records the
  same two identities, bounded claims, rights boundary, and pending review;
  “body sufficient” is expressly not manuscript, build, visual-publication,
  human, or user acceptance.
- `handbook/bib/handbook.bib:5991-6013` keeps the two official titles,
  journals, dates, pagination, and URLs separate.
- `n-c-014.tex:774-800` keeps B\"uchi, Elgot, Trakhtenbrot, Thomas, and Rabin at
  noninterchangeable source strengths.

There is no false completion language, hidden topological hypothesis, hidden
continuity assumption, finite-memory/finite-operator collapse, translation or
priority inflation, source laundering, or rights inflation on this snapshot.

## Mandatory coverage map

| Point | Status | Controlling evidence |
|---|---|---|
| M01 | checked-clean | Seven hashes above match the charter exactly. |
| M02 | checked-clean | All four announcement images = printed pp. 326--329; all twenty-nine expansion images = printed pp. 103--131. |
| M03 | checked-clean | Source note 20--76; bibliography 5991--6013; printed pp. 326, 329, 103, 131; official Math-Net records and terms. |
| M04 | checked-clean | Competence and noncertification disclosed above; scans/PDFs control, OCR navigation only. |
| M05 | checked-clean | Reader 499--510, 754--763; expansion pp. 104--105, 130--131. |
| M06 | checked-clean | Reader 512--525; announcement pp. 326--327; expansion pp. 105--109. |
| M07 | checked-clean | Reader 527--571; announcement pp. 327--328; expansion pp. 109--111. |
| M08 | checked-clean | Reader 551--580; expansion pp. 111--112. |
| M09 | checked-clean | Reader 582--601; expansion pp. 113--116. |
| M10 | checked-clean | Independent residual derivation above; reader 603--606; expansion pp. 116--118. |
| M11 | checked-clean | Independent covering/recurrence derivation above; reader 603--630; expansion pp. 115--119. |
| M12 | checked-clean | Reader 632--639, 687--699; expansion pp. 117--119, 121--124. |
| M19 | checked-clean | Reader 701--714; expansion pp. 124--127. |
| M20 | checked-clean | Independent two-direction check above; reader 716--752; expansion pp. 127--129. |
| M21 | checked-clean | Reader 754--763; expansion pp. 130--131. |
| M22 | checked-clean | Numbering/strength table above; announcement pp. 326--329; expansion pp. 103--131. |
| M23 | checked-clean | Shared theorem 811--825; reader 765--800; modern sentence expressly not imputed to either Russian body. |
| M24 | checked-clean | Reader 487--800; source note complete; compact record 646--658 and 900--913; bibliography 5991--6013; shared theorem 811--825. |
| M25 | checked-clean | Every cited page range, theorem number, displayed formula, title, attribution, and source-strength qualifier was reconciled in the sections above. |
| M26 | checked-clean | First-use terminology audit above; no necessity, definition, standing, nonredundancy, or use failure. |
| M27 | checked-clean | Adversarial failure-mode audit above; no false compression or hidden assumption remains. |
| M28 | checked-clean | Review is limited to N-c-014.c manuscript content and the frozen records; rights and pending gates stay explicit.  No test, checker, repository script, TeX command, build, handbook-PDF inspection, or handbook build was run or claimed. |

Acceptance here is only the Round 3 source-fidelity/language/evidence verdict on
N-c-014.c.  It does not admit literal B\"uchi 1960 reconciliation, N-c-014 as a
whole, Part IX, any rendered handbook page, human or user review, or final-book
completion.

VERDICT: ACCEPT

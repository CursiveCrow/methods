# Round 6 adversarial publication and terminology review

## Mandate and evidence boundary

Seat: adversarial publication and terminology.

Snapshot: the seven Round 6 objects pinned in the charter. I read no earlier-round
report, no other Round 6 report, no ledger, no chair transcript, no Rabin draft or
note, and no text extraction. I did not contact another reviewer. Mathematical
symbols and Russian wording were checked against the original-detail rendered
source pages, not OCR.

My Russian competence is functional reading competence for mathematical prose:
I can read the alphabet, ordinary expository and proof language, theorem and
definition signals, and the technical phrases used here, and I can compare the
printed formulae and their surrounding claim-bearing sentences. I am not a
Russian-language specialist and do not offer philological or stylistic
certification. That competence, together with complete visual inspection of both
bodies and independent mathematical reconstruction, is sufficient for this
publication/terminology mandate. The frozen records correctly refrain from
claiming specialist certification.

## Snapshot identity

I recomputed every required SHA-256 identity before substantive review. All seven
matched the charter exactly.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1961.pdf` | `44213AEBE4DB2F1C389B812A7401138799C3DB4749C3605BA7211BBB4BAF96F9` | match |
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1962-expanded.pdf` | `EAB4438A7BBA2B6009374826A98A3A61FB6465C493F57B03D2C6C7385824096D` | match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `AC0FB697FD3EF5A3BB07EF99275E485DF80FA98D5D2395E58C72D47A0FFC35F9` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD` | match |
| `handbook/bib/handbook.bib` | `75AB70009DF4AB8B2180CFFC6987EA244ADB2F978B1D889C87009EFF17066D5C` | match |
| `spec/research/p09-trakhtenbrot-1961-source-note.md` | `97E02A86E1CF44A760037ECBC060E35C771E893B43BF82F9147E95CACCF8E213` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `E1F121FC0BA9D1FD0C60D0494FC159589D1E62ED11668205D1F5F36BFBA1E5E8` | match |

The recorded PDF byte lengths also agree with the frozen source note: 566,358
bytes for the announcement and 1,884,181 bytes for the expansion.

## Complete visual source inspection

I visually read all 33 rendered pages at original detail.

- Announcement rendered physical pages 1, 2, 3, and 4 map respectively to
  printed pp. 326, 327, 328, and 329. The first page prints the 1961 volume and
  issue, Russian title, author, and Novikov presentation date; the final page
  prints receipt on 29 April 1961, bibliography, and the correction belonging
  to the earlier cited paper.
- Expansion rendered physical pages 1 through 29 map consecutively to printed
  pp. 103 through 131, so physical page \(n\) maps to printed page \(102+n\).
  The opening page prints volume III, issue 1, January--February 1962, the same
  Russian title, and the author; physical page 2 visibly begins with printed
  p. 104, and the sequence continues without a gap through printed p. 131. The
  final page prints receipt on 15 May 1961 and the bibliography.

The bodies support the frozen identities and order: the four-page 1961
*Doklady Akademii Nauk SSSR* item is the registered announcement, while the
twenty-nine-page 1962 *Sibirskii Matematicheskii Zhurnal* item is the complete
expansion. Their theorem numbering and proof detail remain separate throughout
the reader. The same Russian title is preserved, while the official English
renderings remain “Single-Place Predicates” for 1961 and “One-Place Predicates”
for 1962 in reader lines 487--497, source-note lines 24--71, compact-record line
648, and bibliography lines 5991--6013.

The source note gives the two Math-Net routes and identifies the unacquired AMS
translation without using it as textual evidence. Its rights statement at lines
73--79 is exactly bounded: it records the individual noncommercial printing
exception for teachers, students, and researchers, preserves copyright and the
written-permission requirement outside that exception, and denies any
open-content, electronic-copy, republication, or redistribution inference. The
compact record repeats the same boundary at line 648.

## Hostile whole-snapshot audit

### Primitive language and lower/upper syntax

Expanded pp. 104--105 print the interpreted system И with individuals ranging
over \(1,2,\ldots\), monadic variables ranging over arbitrary predicates,
primitive immediate successor, iterated-successor atomic applications, and
formula formation by Boolean operations and the two kinds of quantifier.
Reader lines 499--519 reproduce this as the eliminable grammar of
\(\mathcal I\), type the iterates \(t^{(k)}\), and keep equality, order, bounded
individual quantifiers, constants, and \(t+k\) derived rather than primitive.
The typographic change from Cyrillic И to \(\mathcal I\) is declared at first
use and gives the name language standing, not automaton or theorem standing.

Expanded pp. 105--109 and announcement pp. 326--327 distinguish three things
that the reader also keeps distinct at lines 521--548:

1. fictitious occurrence outside an interval is semantic independence under
   changes outside that interval;
2. control from above/below and upper/lower \(t\)-formulae are syntactic
   restrictions on atomic arguments and individual-quantifier ranges; and
3. bounded-prefix or tail dependence is a separately stated semantic
   consequence.

The range directions are correct: upper \(t\)-formulae are controlled from
below and use \(t<\sigma\) or \(t<\sigma<\mu\); lower \(t\)-formulae are
controlled from above and use \(\sigma<t\) or
\(\lambda<\sigma<t\). Atomic arguments exclude bare constants and allow a
variable or variable plus a numeral. The dependence intervals
\([t,\infty)\) and \([1,t+s]\) are not substituted for those syntactic
definitions. The normal-form proof architecture also follows the print:
predicate quantifiers are moved ahead of individual quantifiers, individual
quantifiers are pushed inward and split at \(t\), and predicate quantification
is distributed across independent prefix and tail pieces. Announcement
Theorem 1 is not silently renumbered as the expansion's unnumbered §1 theorem.

### Operators, memory, and nonimplications

Reader lines 550--603 match expanded pp. 109--113. The operator is a total
typed stream map. Anticipation \(p\) is an input-dependence bound through
\(t+p\), and anticipation zero is prefix preservation. Finite memory instead
uses a finite state set and two maps whose second arguments are the entire
future suffix. Weight is the least possible state-set cardinality. A finite
operator requires finite memory plus a bounded anticipation, and an
\(A\)-operator is the zero-anticipation finite class. The reader correctly
reports the announcement's Cyrillic Л and the expansion's Latin \(A\), and it
declares its normalized cross-source usage instead of transferring the Latin
letter to 1961.

The whole-suffix type matters. The source's one-state operator that asks
whether a future input is 1 confirms that weight one does not imply bounded,
continuous, recursive, or effective future dependence. The canonical
finite-window equations are used only after bounded anticipation is added.
The primitive-recursive recognition and synthesis failures reported at lines
596--603 agree with expanded pp. 111--113: deciding periodicity and uniformly
extracting finite canonical equations are not made consequences of merely
having a primitive-recursive scheme.

### Portions, residual maps, and the graph counterexample

Announcement p. 327 permits an empty portion; expansion p. 114 introduces
portions following nonempty prefix intersections. Reader lines 605--629 state
both conventions and publicly choose the announcement's all-prefix convention.
The many-coordinate definition is fully typed: all coordinate prefixes lie in
\(A_i^r\) for one common \(r\), all concatenations are coordinatewise, and no
interleaving is suggested. Portion, degree, basis, and internal transition have
set/property/data standing, not automaton-kind standing.

Reader lines 631--657 then supply the exact handbook-owned typed repair needed
for graph portions. For zero-anticipation \(T\), \(v_u\in B^r\) is independent
of the extension, \(\operatorname{tail}_r\) and
\(T_u:A^{\mathbb N_+}\to B^{\mathbb N_+}\) are defined before use, and

\[
  (G_T)_{(u,v)}=G_{T_u}\quad\text{exactly when }v=v_u,
\]

with the inconsistent case empty. This independently verifies the types and
explains why \(T_u\) is a stream operator rather than a broad memory state.

I independently checked every step of the handbook counterexample at lines
659--695 against the source's whole-future equations on printed p. 110 and the
false degree claim on p. 115.

- For
  \(T(X)(t)=X(t)\) when \(X(1)=1\), and \(T(X)(t)=0\) otherwise, the output
  through time \(t\) depends only on the input through time \(t\); anticipation
  is zero.
- With \(Q=\{0,1\}\), \(q(1)=0\),
  \(\Phi(q,z)=(1-q)z_0\), and
  \(\Psi(q,z)=q\mathbin{\mathsf{xor}}z_0\mathbin{\mathsf{xor}}z_1\), induction
  gives \(q(t)=X(1)\mathbin{\mathsf{xor}}X(t)\) and hence exactly the displayed
  output. The transition's use of \(z_1\) is permitted by the printed
  whole-future memory type.
- A one-state presentation would force its unique output map at time one to be
  \(z\mapsto z_0\). Applying that same suffix map at time two to an input
  beginning \(01\) returns 1 although the required output is 0. The weight is
  therefore exactly two.
- The original graph, the portions after \((0,0)\) and \((1,1)\), and the
  inconsistent portion after \((0,1)\) are respectively the original graph,
  the constant-zero graph, the identity graph, and the empty set. No further
  nonempty form occurs: a consistent nonempty prefix beginning with 0 always
  leaves the constant-zero map, and one beginning with 1 always leaves the
  identity map. Thus there are exactly three nonempty portions and four
  all-prefix portions.

This refutes the printed \(k\) claim and the former \(k+1\) all-prefix repair.
The reader retains only the exact count through distinct \(T_u\), identifies
the source's invalid prefix-determined-state inference, preserves the sound
closedness claim, and owns the counterexample and correction publicly. The
singleton/ultimate-periodicity claim and the uncountability/countability
nondefinability argument at lines 696--698 remain compatible with both portion
conventions.

### Homogeneity, topology, and the empty set

The finite normal form gives finitely many residual formulae after fixing a
prefix, so every \(\mathcal I\)-definable set is homogeneous; appending a bit
to a residual formula gives the effective internal transition. This is the
source's unconditional internal construction on expanded pp. 116--118 and is
reported at reader lines 700--703.

For the converse, a finite basis and its permitted extensions give the local
current/next recurrence displayed at reader lines 704--715. The types and
standing are explicit at lines 716--720: \(X\) is free input, the \(q_i\) are
bound state predicates, \(U\) is a bound choice predicate, \(\theta\) is
quantifier-free, and the literal initial vector selects the basis member equal
to the original set. Existential projection of this finite local closed
relation is closed because the hidden-predicate Cantor space is compact; the
finite state description also gives homogeneity. Conversely, for a nonempty
closed homogeneous set, every compatible finite prefix can be continued
through a nonempty portion, and closedness turns agreement at all finite
levels into membership.

The printed covering construction on expanded p. 116 cannot cover the empty
set because a total operator has nonempty image. Reader lines 721--729 therefore
restrict that source construction to a nonempty set and define the empty set
separately in the same recurrent shape by conjoining \(q_1(1)=1\) with
\(q_1(1)=0\). Both steps are expressly handbook-owned at the public point of
use, and the same ownership is repeated in source-note lines 325--334 and
compact-record line 652. No hidden nonemptiness assumption remains in the
stated closed-homogeneous converse.

Complement, finite union, and predicate projection then generate the full
definable class from closed homogeneous sets. The reader retains the
announcement's open Borel/projective question and does not turn later
decidability into a source-time unconditional claim. It correctly separates
the effective internal transition from the external choice that requires
truth/nonemptiness decisions, and limits Putnam's unconditional removal of
that condition to the recurrent fragment.

### Finite realization and solutions

Reader lines 747--805 keep all hypotheses and conclusions at their printed
strength on announcement pp. 328--329 and expansion pp. 119--124.

- For a continuous total operator with definable graph, each of the finitely
  many nonempty residual graphs is compact. Continuity of the first output
  coordinate is uniformly controlled on each; the finite maximum supplies one
  anticipation bound at every residual stage, while the residual basis supplies
  finite memory. The weight bound is by graph degree.
- Expanded §4 Theorem 2 drops continuity. The same finite residual basis still
  supplies whole-future finite memory, but there is no uniform lookahead
  argument. The reader concludes only finite memory and explicitly denies
  finite-operator standing.
- A graph defined exactly by a formula and an operator whose graph is merely
  contained in the formula's relation are separated before Theorem \(4'\).
  The closed homogeneous-relation existence clauses and the announcement's
  open-relation qualification are not collapsed.
- A general \(A\)-solution has both source quantifiers: every solution in the
  named class arises from an operator-parameter substitution, and every such
  substitution yields a solution. Replacing the class throughout gives the
  general zero-anticipation solution. Parameter streams and parameter
  operators have explicit standing.
- In Theorem 5/expanded Theorem 3, deletion of empty or nonextendible portions
  is stable: deletion of the initial portion rules out any zero-anticipation
  solution, while a surviving family permits parameter bits to choose exactly
  the surviving outputs. The finite transition supplies memory, and closedness
  changes finite-prefix compatibility into relation membership. Completeness
  and soundness of the parameterization, the weight bound, and the conditional
  emptiness boundary are all present.
- Expanded Theorem \(3'\) is separately stated for each fixed \(p\). The shift
  reduction does not create one parameterization across unbounded lookahead.

There is no hidden continuity, no conversion of finite memory into finite
operator standing, and no conversion of existence into generality.

### Explicit synthesis and finite words

Reader lines 807--820 correctly distinguish an explicit definition from an
arbitrary graph relation. Expanded pp. 124--127 support the finite-memory
conclusion, the semantic anticipation tests, and the finite shifted-formula
construction in the zero-shift prefix-controlled case. Fixing the first input
column determines the first output and a residual formula; normal form leaves
only finitely many residuals, which become the canonical state and transition
tables. The worked example is correctly located at pp. 126--127 and has two
formulae and the two printed tables.

The typed finite-word action at reader lines 822--833 is well-defined: zero
anticipation makes \(T_t:A^t\to B^t\) independent of the chosen infinite
extension and immediately gives prefix compatibility. Automaton-enumerability
at lines 835--841 is a statement about each lengthwise range. Automaton-
decidability at lines 842--847 is a terminal recognizer-output property. Neither
is confused with the range of the infinite-stream map.

For expanded §5 Theorem 2, enumeration implies decidability by the source's
explicit recognizer construction. In the converse direction, the empty
language is indeed decided by the constant-zero operator and satisfies the two
printed hypotheses vacuously, but no total length-preserving operator has an
empty range at a positive length. Adding nonemptiness to prefix closure and
proper extendibility supplies a member of every positive length and exactly the
seed required by the p. 128 construction. Reader lines 849--858 state and own
this correction; source-note lines 497--506 and compact-record line 656 agree.

Expanded pp. 130--131 define \(\mathcal I'\) by eventually-zero predicate
variables. Reader lines 860--869 correctly define a special beginning by zeros
forever after its endpoint, not by arbitrary prefixhood. Theorem 3's existence
claim applies to every \(\mathcal I\)-formula, while effective construction is
limited to \(\mathcal I'\)-formulae and is explicitly reported as Büchi's.

### Nonconflation, terminology, and publication status

Reader lines 871--905, shared-theorem lines 811--825, and the source-navigation
paragraph at lines 2341--2347 prevent compound-name folklore from becoming a
literal Trakhtenbrot quotation. The displayed regular/MSO sentence is expressly
modern; Büchi's precursor encoding, Elgot's design development, Trakhtenbrot's
broader operator package, and Thomas's later proof synthesis retain separate
authority. The reader also treats Church, Büchi, Elgot, Putnam, and Robinson
remarks as source-reported historical claims, not independent priority verdicts.

The complete terminology pass found no invented primitive, definition after
use, redundant technical name, standing ambiguity, or unused coined
distinction. In particular, every handbook-added name or notation in the
critical repair is introduced together with its need, exact type/definition,
operator rather than state standing, distinction from broad memory state, and
immediate later use. Source terms such as portion, basis, solution, general
solution, automaton-enumerable, automaton-decidable, and special beginning are
defined before their theorem use. Descriptive phrases do not pretend to be new
primitive objects.

The authority boundary is also honest. The reconstruction is explicitly
bounded to used definitions, results, proof moves, examples, and qualifications;
it disclaims line-by-line translation and Russian-specialist certification.
Source-note lines 14--20 and 572--583 and compact-record lines 658 and 911 keep
fresh review pending on this revised snapshot. No text claims topic admission,
Part IX completion, rendered-handbook inspection, human review, final-book
completion, or user acceptance.

## Finding register

No blocker, must-fix, should-fix, consider, discard, or unresolved-user finding
arose within this seat's mandate. Accordingly there is no unsupported
correction request to locate against a printed page.

## Mandatory coverage disposition

| Point | Disposition | Evidence/result |
|---|---|---|
| M01 | checked-clean | All seven hashes recomputed before substantive review; exact matches recorded above. |
| M02 | checked-clean | All 4 announcement and all 29 expansion pages read at original detail; physical-to-printed maps confirmed. |
| M03 | checked-clean | Identities, years, journals, pagination, distinct official English titles, Math-Net routes, source order, AMS nonuse, and bounded rights language agree across the frozen objects. |
| M04 | checked-clean | Competence and non-specialist limitation disclosed above; evidence stated exactly. |
| M05 | checked-clean | Iterated-successor grammar, atomic formulae, formation, domains, primitive successor, eliminable extensions, and \(\mathcal I/\mathcal I'\) standing verified on expanded pp. 104--105 and 130--131. |
| M06 | checked-clean | Semantic fictitious occurrence; exact controlled, upper, and lower syntax; separate dependence consequences; announcement Theorem 1; expanded normal form; and reported proof moves verified on announcement pp. 326--327 and expansion pp. 105--109. |
| M07 | checked-clean | Stream map, anticipation, prefix equivalence, whole-suffix finite memory, weight, canonical finite-window form, \(A/\)Л standing, and all nonimplications verified on pp. 109--113. |
| M08 | checked-clean | Primitive-recursive recognition/synthesis boundary and the one-state unbounded, noneffective future-dependence example verified on pp. 111--113. |
| M09 | checked-clean | Both portion conventions, equal-length tuple types, \(\operatorname{tail}_r,T_u,v_u\), graph equation, degree/basis/transition, examples, and every counterexample step independently verified on announcement p. 327, expansion pp. 114--116, and reader lines 605--698. |
| M10 | checked-clean | Formula-residual finiteness and effective internal-transition construction independently derived from the normal form and matched to expansion pp. 116--118. |
| M11 | checked-clean | Closed-homogeneous recurrence, compact projection, closure characterization, topology, nonempty covering restriction, contradictory empty recurrence, and handbook ownership verified on pp. 116--119 and reader lines 700--736. |
| M12 | checked-clean | Internal transition is unconditional; external choice/emptiness is conditional; Putnam is limited to the recurrent fragment. |
| M13 | checked-clean | Compact uniformity on finitely many residual graphs, one global lookahead bound, finite memory, and weight bound independently reconstructed for announcement Theorem 4/expanded §4 Theorem 1. |
| M14 | checked-clean | Expanded §4 Theorem 2 retains only whole-future finite memory without continuity; no finite-operator inference remains. |
| M15 | checked-clean | Exact-graph versus contained-graph solution standing and every announcement Theorem \(4'\) clause, including open-relation qualification, verified on p. 328. |
| M16 | checked-clean | Both general-solution quantifiers and parameter standing verified against announcement p. 328 and expansion pp. 120--121. |
| M17 | checked-clean | No-solution deletion, surviving family, parameter completeness/soundness, closedness, weight, and conditionality independently reconstructed on pp. 121--124. |
| M18 | checked-clean | Expanded Theorem \(3'\) remains separately quantified at each fixed anticipation bound; no unbounded-lookahead overstatement. |
| M19 | checked-clean | Explicit definition, finite memory, semantic anticipation criteria, terminating shifted-formula construction, canonical equations, and pp. 126--127 example role verified. |
| M20 | checked-clean | Both word-set definitions and both theorem directions verified; prefix closure, proper extendibility, missing nonemptiness, and the exact p. 128 seed were independently checked. |
| M21 | checked-clean | \(\mathcal I'\), special beginnings, §5 Theorem 3, Büchi attribution, and existence/effectivity split verified on pp. 130--131. |
| M22 | checked-clean | Announcement Theorems 1--5 and \(4'\) remain distinct from expanded section numbering and proof detail; titles are not transferred. |
| M23 | checked-clean | Shared theorem and Thomas paragraph mark the sentence modern and preserve separate Büchi, Elgot, Trakhtenbrot, Thomas, and Rabin authority. |
| M24 | checked-clean | Reader, source note, compact record, shared theorem, bibliography, and consolidated acquisition status are mutually consistent; review remains pending before this verdict. |
| M25 | checked-clean | Locators, numbering, displayed formulae, citations, historical attributions, titles, and source-strength qualifiers checked against all 33 printed pages and the frozen records. |
| M26 | checked-clean | Complete AGENTS necessity/definition/standing/nonredundancy/use pass completed; no violation found. |
| M27 | checked-clean | No false compression, hidden continuity/closedness, operator-class collapse, source laundering, translation inflation, priority inflation, or premature completion language found. |
| M28 | checked-clean | Topic-only scope, personal-use/redistribution boundary, no-build/no-test boundary, and the limited publication meaning of this verdict are preserved. |

## Scope of acceptance

This verdict admits only the frozen manuscript-content reconstruction of
`N-c-014.c` at the separately stated 1961 announcement and 1962 expansion
strengths. It does not admit literal Büchi 1960 reconciliation, `N-c-014` as a
whole, another topic or part, any rendered handbook page, any build or static
gate, human review, final-book completion, or user acceptance.

VERDICT: ACCEPT

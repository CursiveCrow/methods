# Round 4 adversarial publication and terminology review

## Review scope, blindness, competence, and evidence

I reviewed only the charter and the frozen Round 4 seven-object snapshot.  I
did not read the ledger, the chair transcript, any Round 1--3 report, another
Round 4 report, or another board.  I made no change to a frozen artifact and
did not run a test, checker, repository script, TeX command, build, or
handbook-PDF inspection.

I am not a credentialed Russian-language specialist and this review is not a
specialist certification of literary translation.  I can read the printed
mathematical notation and the relevant Russian mathematical prose at a working
technical level.  My source-language evidence was direct original-detail
inspection of every printed source page, with the two frozen layout
extractions used only to locate passages.  The scans, not the extractions,
controlled symbols, words, pagination, and source-version judgments.  I also
used independent mathematical derivation, the frozen manuscript and provenance
records, Math-Net's two live bibliographic records, and Math-Net's controlling
Terms of Use.

## M01: frozen identity labels

All seven recomputed SHA-256 labels match the Round 4 charter exactly.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1961.pdf` | `44213AEBE4DB2F1C389B812A7401138799C3DB4749C3605BA7211BBB4BAF96F9` | match |
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1962-expanded.pdf` | `EAB4438A7BBA2B6009374826A98A3A61FB6465C493F57B03D2C6C7385824096D` | match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `D3480007167E06CEDB9FB6ABF847F66F3113A4907B72FA92BE80BAF3378B349A` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD` | match |
| `handbook/bib/handbook.bib` | `75AB70009DF4AB8B2180CFFC6987EA244ADB2F978B1D889C87009EFF17066D5C` | match |
| `spec/research/p09-trakhtenbrot-1961-source-note.md` | `A1ED4C1AF0E173AFDEAE98FC7C49BD9BB1C0ED4D72BAF61D6E8AFC1B571D78BC` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `7024F2410F69BD0D4ADFF3B31E9ED316BDB23AE27704984D0691BE0F1A1CC63A` | match |

The two PDF and two reading-aid byte sizes stated in the source note also
match the frozen files: 566,358; 1,884,181; 23,018; and 160,210 bytes,
respectively.  I did not treat the reading aids as source identities.

## M02: complete original-detail visual source inspection

- Announcement physical pages 1--4 are continuously printed pp. 326--329.
  I inspected all four at original detail.  Physical p. 1 contains the 1961
  Doklady masthead, Russian title, author, presentation date, introduction,
  lower/upper terminology, and the start of the operator definition; physical
  pp. 2--3 contain printed pp. 327--328 and Theorems 1--5 and (4'); physical
  p. 4 is printed p. 329 with the Putnam/Church/Robinson/Elgot qualifications,
  receipt, bibliography, and correction to the earlier cited article.
- Expansion physical pages 1--29 are continuously printed pp. 103--131.  I
  inspected all twenty-nine at original detail.  The sequence has no omitted,
  duplicated, or displaced printed page.  Printed p. 103 begins the title and
  introduction; pp. 104--109 are Section 1; pp. 109--113 Section 2;
  pp. 113--119 Section 3; pp. 119--124 Section 4; and pp. 124--131 Section 5,
  ending with receipt and bibliography.

## Blocking finding

### R4-AP-01 — must-fix — the (k+1) graph bound is a convention translation, not a correction of the expansion in its own terms

**Frozen locations.** `handbook/parts/p09/presentations/n-c-014.tex:582--605`,
especially lines 589--604; `spec/research/p09-trakhtenbrot-1961-source-note.md:185--213`,
especially lines 195--213; and
`spec/research/p09-source-presentations-lot2-3.md:652`.

**Controlling printed evidence.** The announcement on printed p. 327 defines
the residual set for a prefix as possibly empty (the parenthetical is
literally “быть может пустое”).  The expansion changes the presentation on
printed p. 114: it introduces a portion after first requiring the intersection
with the corresponding prefix interval to be nonempty.  Its homogeneity
definition on pp. 114--115 consequently ranges over those portions.  The graph
example on p. 115 then explicitly says “if it is nonempty” before identifying a
graph portion with one of the operator's residual operators, and counts at most
(k) such residual operators.  Thus the expansion's printed (k)-bound is
correct under the expansion's nonempty-portion convention.

**Independent derivation.** If the announcement/all-prefix convention is
chosen instead, every compatible paired prefix of a zero-anticipation
weight-(k) graph leaves the graph of one reachable residual operator, so
there are at most (k) nonempty graph portions.  An incompatible paired prefix
leaves (arnothing), which is distinct from every total residual-operator
graph.  Hence the bound becomes (k+1).  The weight-one constant-zero operator
realizes the distinction: compatible paired prefixes leave the original graph,
while a prefix demanding output (1) leaves the empty portion.  The snapshot's
numeric (k+1) statement is therefore correct under its declared all-prefix
definition.

**Publication harm and violated invariants.** The three frozen prose artifacts
call this a handbook-owned “correction” or “repair” to expanded p. 115 without
disclosing that expanded p. 114 changed the convention that makes p. 115
correct as printed.  This hides a genuine 1961/1962 source difference and makes
the handbook appear to correct a source error when it has actually normalized
one source's convention into the other.  A hostile reader can expose the
misownership directly from adjacent expanded pp. 114--115.  This violates the
version-separation obligation in I01, the source/handbook ownership obligation
in I09, the bounded-translation obligation in I25, and M09/M22/M24/M25/M27.

**Smallest exact correction.** At the first reader definition of portion, say
that the 1961 announcement explicitly retains empty portions, whereas the 1962
expansion introduces portions only for nonempty prefix intersections, and say
which convention the handbook adopts.  Then replace “correction to the claim
on expanded p. 115” by the exact statement: the source's (k)-bound is valid
under its nonempty-portion convention and translates to (k+1) under the
handbook's announcement/all-prefix convention.  Make the same ownership and
version statement in the source note and compact record.  The constant-zero
example may remain as the proof that the translated (+1) is necessary.

## Hostile cross-artifact and proof-strength audit

Apart from R4-AP-01, I found no blocker or must-fix in the frozen snapshot.

### Source identity, version, title, access, and rights

- The scans, Math-Net records, bibliography entries, source note, compact
  record, presentation, shared theorem, and navigation paragraph agree on the
  author, source order, years, journals, volumes, issues, and pagination.  The
  registered announcement is Doklady 140(2) (1961), 326--329; the complete
  expansion is Sibirskii Matematicheskii Zhurnal 3(1) (1962), 103--131.
- Both scans print the same Russian title.  Math-Net's live English records use
  “single-place predicates” for 1961 and “one-place predicates” for 1962.  The
  bibliography preserves those two renderings, and the manuscript never
  transfers a theorem number or printed page between the bodies.
- The announcement scan supports presentation by P. S. Novikov on 16 May 1961
  and receipt on 29 April 1961.  The expansion supports receipt on 15 May 1961.
  The known AMS Series 2 volume 59 (1966) route is correctly kept as a later
  English translation whose body was not acquired or used.
- Math-Net's current controlling Terms say all rights are reserved, electronic
  or other reproduction/republication requires the copyright holder's prior
  written permission, individual teachers/students/researchers may print
  copies for noncommercial teaching or research, and systematic downloading
  is not permitted without written permission.  I independently checked every
  Trakhtenbrot-specific permission phrasing in the snapshot: source-note
  lines 71--77 and compact-record line 648 accurately confine the exception to
  individual printing, deny an open-content/republication licence, and deny
  inferred redistribution authority for the local PDFs.  No reader or
  bibliography sentence enlarges that permission.
- “Complete” is consistently source-body or reconstruction scope, not an
  admission claim.  Source-note lines 14--18 and 458--469, compact-record line
  658, and consolidated-status line 911 keep independent scholarly review
  pending.  They do not claim Russian-specialist review, human review, a
  handbook build, rendered-handbook inspection, Part IX admission, final-book
  completion, or user acceptance.

### Formal system and normal form

- (mathcal I) is introduced at manuscript lines 499--510 as a typographic
  rendering of Cyrillic И and is correctly given formal-language standing.
  The domains (1,2,ldots), arbitrary monadic predicates, and primitive
  successor agree with expanded pp. 104--105.  Equality, order, bounded
  individual quantifiers, constants, and (t+k) are correctly classified as
  eliminable conveniences rather than extra primitives.
- Fictitious occurrence is correctly semantic: two interpretations differing
  only outside the interval must agree in truth.  The lower/upper distinction
  keeps prefix dependence through (t+s) separate from tail dependence from
  (t).  Announcement Theorem 1 and expanded Section 1 are not reduced to a
  slogan: predicate quantifiers are moved before individual quantifiers,
  individual quantifiers are driven inward and split at (t), and independent
  prefix/tail predicate assignments are recombined.  Those are the printed
  proof moves on pp. 106--109.
- The normal-form finiteness claim is sound: after fixing a prefix, only
  finitely many Boolean functions of the bounded lower windows can remain,
  while upper components shift uniformly.  That gives finitely many residual
  formulae and an effective residual transition by appending one letter.

### Operators, memory, anticipation, and the negative boundary

- The operator is a total typed stream map.  Anticipation (p) is agreement
  through (t+p); (p=0) gives extension-independent prefix maps.  Finite
  memory is correctly defined with a finite state and external/internal maps
  of the whole future suffix, so it does not smuggle in continuity or bounded
  lookahead.  Weight is the least memory-state cardinality.
- A finite operator adds one fixed anticipation bound.  The canonical equations
  use exactly the input window (t,ldots,t+p).  The 1961 Л versus 1962 Latin
  (A) version boundary is declared, and the manuscript explicitly says that
  the hyphenated (A) is the class label rather than the input-alphabet
  metavariable.  Zero anticipation, finite memory, finite operator, and
  (A)-operator are not collapsed.
- The one-state future-existence operator checks whether a future input bit is
  (1); it is a valid minimal counterexample to “finite memory implies bounded
  or effective future dependence.”  Expanded Section 2 also supports both
  primitive-recursive negative boundaries: periodicity recognition and
  canonical-equation synthesis are not algorithms for arbitrary
  primitive-recursive schemes.

### Homogeneity, recurrence, topology, and effectiveness

- Under the reader's all-prefix convention, portion, coordinatewise portion,
  degree, basis, and internal transition are exactly defined and have the right
  standings as properties/data of a stream set, not invented automaton kinds.
  The only source-ownership defect is R4-AP-01.
- Every definable-set homogeneity claim has the required derivation: normal
  form yields finitely many residual formulae, and syntactic one-letter shift
  effectively gives the internal transition.  The singleton/ultimate-period
  equivalence and the uncountability-versus-countability counterexample prevent
  the false converse “homogeneous implies definable.”
- Closedness is expressly Cantor-product closedness.  For a closed homogeneous
  set, the finite basis transition plus a choice bit gives the displayed local
  recurrence.  Literal initial state (q_1(1)=1) and the remaining zero values
  select the original portion rather than an unspecified union.  Conversely,
  the local finite-state witness set is compact and its projection is closed;
  its finitely many state residuals give homogeneity.  The full definable class
  is then generated by complement, finite union, and predicate projection.
  No closedness hypothesis is hidden in the unrestricted converse.
- The effectiveness boundary is correct.  Internal residual transition is
  syntactic and unconditional; choosing an external output requires deciding
  which residual formulae are nonempty.  The conditional
  (mathcal I)-algorithm is therefore not silently upgraded.  Putnam removes
  the condition only for the stated existential-predicate recurrent fragment.

### Continuous realization, solutions, and generality

- The continuous-total-operator theorem is correctly reconstructed.  On each
  nonempty graph portion, continuity of the first output coordinate over a
  compact input domain gives a finite determining prefix.  Finitely many
  portion types give one maximum anticipation bound; the portion type itself
  is finite memory.  Thus the operator is finite, with the stated memory bound.
- Expanded Section 4, Theorem 2 is kept strictly weaker: definability without
  continuity gives only finitely many whole-suffix memory states.  Nothing in
  the proof supplies a common lookahead bound, and the manuscript claims none.
- “Defines exactly the graph” is distinguished from “is solved by an operator
  whose graph is contained in the relation.”  Announcement Theorem (4')
  is accordingly an existence result for closed homogeneous relations.  Its
  continuous and zero-anticipation branches and its separate open-relation
  no-weight-bound qualification are all preserved.
- General (A)-solution has both quantifiers: every (A)-solution is obtained
  by an (A)-operator parameter substitution, and every such substitution is
  sound.  Replacing the class throughout gives general zero-anticipation
  solution.  “General” is therefore not weakened to mere existence.
- The Theorem 5/expanded Theorem 3 reconstruction includes the two branches,
  stable deletion, initial-residual failure, surviving-family construction,
  parameter choice, finite memory, closedness limit step, weight bound, and
  residual-nonemptiness conditionality.  These steps independently support the
  all-and-only parametrization claim.
- Expanded Theorem (3') is correctly bound separately for every fixed (p).
  The shift reduction preserves “anticipation at most (p)” and does not yield
  one parametrization across an unbounded union of lookahead classes.

### Explicit synthesis, finite words, and the weak system

- The explicit-definition standing and the three Section 5 conclusions are
  exact: finite memory always; anticipation (p) exactly under semantic
  independence outside ([1,t+p]); and (A)-operator exactly for
  ([1,t]).  Iterated first-column evaluation and formula shifting terminate
  because normal form leaves finitely many residual formulae.  The locator to
  the two-formula output/transition tables on pp. 126--127 is accurate and is
  not inflated into a larger example.
- Zero anticipation makes each (T_t:A^t\to B^t) independent of the chosen
  infinite extension and makes the family prefix compatible.  This derives,
  rather than assumes, the typed bridge from stream operators to positive-
  length words.
- Automaton-enumerability is correctly the lengthwise range property;
  automaton-decidability is correctly terminal recognizer output.  Enumeration
  implies recognition.  The independent empty-language counterexample verifies
  that the printed converse lacks nonemptiness: the empty language is
  prefix-closed, vacuously extendible, and recognized by constant zero, but a
  total length-preserving map has a nonempty range at every positive length.
  Once nonemptiness is added, prefix closure and proper extendibility supply a
  word at every length and make the source's “first word” branch defined.  The
  snapshot clearly owns this correction as handbook-supplied.
- (mathcal I') is correctly a distinct interpreted system whose predicates
  are eventually zero.  A special beginning ends only when the represented
  predicate remains zero forever; it is not an arbitrary prefix.  Expanded
  Section 5, Theorem 3 is kept at its two strengths: existence for every
  (mathcal I)-formula and effective construction for an
  (mathcal I')-formula, with Büchi attribution preserved.

### Modern theorem, adjacent sources, and nonconflation

- The shared theorem at `logic-in-computer-science.tex:811--825` labels the
  regular/MSO sentence as the modern formulation and immediately lists the
  original sources' different encodings and packages.  It does not claim that
  the sentence is verbatim Trakhtenbrot 1961.  The source-navigation paragraph
  at lines 2341--2347 preserves the announcement/complete-expansion pair.
- The modern proof paragraph at `n-c-014.tex:789--807` separates the track-
  projection construction and Thomas's Section 3.1 survey from Büchi's special
  predicates, Elgot's design calculus, and Trakhtenbrot's operator theory.
  No adjacent source is used to launder a Russian-source theorem, repair, title,
  or priority claim.
- Announcement Theorems 1--5 and (4') are reported under announcement pages
  and symbols; expanded results remain under section/theorem locators.  The
  portion-convention difference is the one unreported version difference and
  is exactly R4-AP-01.

## Complete AGENTS terminology audit

Except for the source-ownership problem in R4-AP-01, every technical name first
used in the Trakhtenbrot reconstruction meets the five-part rule.

| Name or notation | Necessity, exact definition, standing, nonredundancy, and later use |
|---|---|
| (mathcal I) | Explicit typographic normalization of Cyrillic И; exactly the interpreted formal language; distinguished from an automaton and from Büchi's weak system; used throughout. |
| fictitious outside; lower/upper (t)-formula | Exact semantic independence and unequal prefix/tail dependence are stated; these are formula properties, not syntax-occurrence tests; required by normal form and synthesis. |
| operator; anticipation; prefix preservation | Total map and exact agreement condition are typed; anticipation is an operator property and prefix preservation is its (p=0) form; used to type every later class. |
| finite memory; weight | Whole-suffix equations and least state cardinality are exact; finite memory is separated from lookahead/effectivity; weight is used in every bound. |
| finite operator; Л/(A)-operator | Conjunction of finite memory and bounded anticipation, then its (p=0) subclass; source-version letters and alphabet-variable collision are explained; both distinctions are used. |
| periodic/ultimately periodic | Exact preperiod/period equation is supplied and the modern normalization is declared; used in the negative example and singleton theorem. |
| portion; homogeneous degree; basis; internal transition | Eliminable residual definition and finite-family data are supplied; their standings as stream-set properties/data and not automata are explicit; they drive every later proof.  R4-AP-01 concerns the missing inter-version convention disclosure, not the reader definition's mathematical exactness. |
| closed | Fixed explicitly as Cantor product-topology closedness; nonredundant with homogeneity; used exactly where compact/topological conclusions require it. |
| conditional (mathcal I)-algorithm | Defined as a procedure relative to a truth algorithm for closed (mathcal I)-sentences; standing is metalinguistic/procedural; distinguished from unconditional construction and used in the synthesis boundary. |
| solution; graph definition | Graph containment versus graph equality is exact, necessary for Theorem (4'), and immediately used. |
| general (A)-solution; general zero-anticipation solution | Parameter-operator standing and both completeness/soundness clauses are exact; nonredundancy from one solution is explicit; used in Theorems 3/5 and (3'). |
| explicit definition | The defining equation is displayed, gives formula/operator standing, and is distinguished by its pointwise free-time form from arbitrary implicit graph formulae; used in Section 5 synthesis. |
| (T_t) | Typed length-(t) map with extension-independence proof; notation is eliminable and required by the two word-set definitions. |
| automaton-enumerable; automaton-decidable; terminal result | Each is an exact language property or Boolean output datum; range and recognition are nonredundant and used in both theorem directions. |
| (mathcal I'); special beginning | Exact eventually-zero range and tail-zero condition are given; formal-system and finite-word standings are clear; each is distinguished from (mathcal I)/arbitrary prefix and used in Theorem 3. |
| modern Büchi--Elgot--Trakhtenbrot theorem | Exact modern statement and metahistorical standing are supplied; nonidentity with each literal original theorem is explicit; used only as the shared modern synthesis. |

No unused speculative technical object, definition-after-use, redundant synonym,
or standing ambiguity remains outside R4-AP-01.

## Mandatory coverage map

| Point | Status | Evidence/disposition |
|---|---|---|
| M01 | checked-clean | Seven exact recomputed labels listed above. |
| M02 | checked-clean | All 4+29 pages inspected at original detail; maps 1--4 to 326--329 and 1--29 to 103--131. |
| M03 | checked-clean | Identities, dates, journals, pagination, titles, routes, order, and rights checked against scans and live Math-Net records/terms. |
| M04 | checked-clean | Competence and evidence disclosed above; no specialist certification claimed. |
| M05 | checked-clean | Exact (mathcal I)/(mathcal I') syntax, domains, successor, and eliminable extensions verified. |
| M06 | checked-clean | Semantic fictitious occurrence, lower/upper forms, Theorem 1, expanded normal form, and proof moves verified. |
| M07 | checked-clean | Operator type, anticipation, prefix equivalence, whole-suffix memory, weight, finite equations, (A)-standing, and nonimplications verified. |
| M08 | checked-clean | Primitive-recursive negative boundary and one-state noneffective finite-memory example verified. |
| M09 | finding-linked | R4-AP-01; definitions and (k+1) derivation are sound, but the two source conventions and ownership are misstated.  Singleton and uncountability examples checked-clean. |
| M10 | checked-clean | Finite residual-form derivation and effective one-letter internal transition independently reconstructed. |
| M11 | checked-clean | Closed converse, local recurrence, compact projection, full closure characterization, and topological hypotheses derived. |
| M12 | checked-clean | Internal construction, nonemptiness-dependent external choice, conditionality, and Putnam fragment separated. |
| M13 | checked-clean | Compact uniformity on finitely many nonempty portion types gives one anticipation bound; portion type gives finite memory and weight bound. |
| M14 | checked-clean | Expanded Theorem 2 kept at finite memory only; no continuity/lookahead silently inferred. |
| M15 | checked-clean | Graph equality/solution containment and every closed/open clause of announcement Theorem (4') verified. |
| M16 | checked-clean | Both general-solution quantifiers and parameter-operator standing verified for (A) and zero-anticipation classes. |
| M17 | checked-clean | Theorem 5/expanded Theorem 3 branches, stable deletion, parameterization, closedness step, bound, and conditionality reconstructed. |
| M18 | checked-clean | Theorem (3') kept separately at each fixed (p); no unbounded-lookahead solution asserted. |
| M19 | checked-clean | Explicit definitions, anticipation tests, residual-shift termination, canonical equations, and pp. 126--127 example role verified. |
| M20 | checked-clean | Both word properties and both theorem directions checked; nonempty corrected converse independently proved. |
| M21 | checked-clean | (mathcal I'), special beginnings, Theorem 3, Büchi attribution, and effective/non-effective split verified. |
| M22 | finding-linked | Numbering and strengths otherwise clean; R4-AP-01 is the one silent announcement/expansion convention transfer. |
| M23 | checked-clean | Modern shared theorem and Thomas paragraph explicitly prevent compound-name laundering. |
| M24 | finding-linked | Cross-artifact reconciliation is complete except the same convention/ownership defect repeated in three artifacts. |
| M25 | finding-linked | All other locators, theorem numbers, formulas, citations, titles, and qualifications checked-clean; R4-AP-01 affects pp. 114--115 attribution. |
| M26 | checked-clean | Complete terminology ledger above; no terminology blocker distinct from R4-AP-01. |
| M27 | finding-linked | No hidden continuity/closedness, class collapse, translation or priority inflation, or completion inflation found; R4-AP-01 is source/convention laundering. |
| M28 | checked-clean | Topic-only admission boundary, exact Math-Net rights boundary, and no-test/no-build boundary enforced. |

VERDICT: REJECT — R4-AP-01

# Round 5 adversarial publication and terminology review

## Review identity, competence, and evidence boundary

I reviewed the frozen Round 5 snapshot as the adversarial publication and
terminology seat.  I did not read the ledger, the chair transcript, any Round
1--4 report, or either other Round 5 report, and I did not contact another
reviewer.  I read the charter, the seven frozen objects, and the thirty-three
permitted source-page images only.

My Russian competence is non-specialist but functional for direct reading of
mathematical prose, formulae, theorem headings, technical terms, bibliographic
matter, and publication metadata in these scans.  I am not a credentialed
Russian-language specialist and do not certify subtle philological choices.
The evidence for this review is direct original-detail inspection of every
printed page, formula-by-formula comparison with the frozen reconstruction,
and internal comparison among the frozen reader, source note, compact record,
shared theorem, and bibliography.  I did not use either text extraction as
authority or evidence.  This review therefore supports a bounded scholarly
translation and publication audit, not a specialist translation
certification.

No test, test harness, automated checker, repository script, TeX command,
interim build, handbook-PDF inspection, or handbook build was used.  The only
mechanical operation was the expressly required SHA-256 identity
recomputation.  No frozen artifact was edited.

## M01 identity gate

All seven recomputed SHA-256 labels equal the Round 5 charter labels.

| Frozen object | Recomputed SHA-256 | Disposition |
|---|---|---|
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1961.pdf` | `44213AEBE4DB2F1C389B812A7401138799C3DB4749C3605BA7211BBB4BAF96F9` | match |
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1962-expanded.pdf` | `EAB4438A7BBA2B6009374826A98A3A61FB6465C493F57B03D2C6C7385824096D` | match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `070252A0A152D814FD1420FDBF889CAA9FEFBB5D187B2C1CDAB1B0595CAA13DB` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD` | match |
| `handbook/bib/handbook.bib` | `75AB70009DF4AB8B2180CFFC6987EA244ADB2F978B1D889C87009EFF17066D5C` | match |
| `spec/research/p09-trakhtenbrot-1961-source-note.md` | `6C214BCC16961AEC1124D87FA5D474E957B93C083CA377C5EC414DCF055FC655` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `667283E6415851F28A35EEE339DD466AA8706DB13DC05EA0ACDCAF096A24E974` | match |

The two PDF sizes also match the source note: 566,358 bytes for the
announcement and 1,884,181 bytes for the expansion.

## M02 visual source-page audit

I opened every permitted image at original detail.  Announcement image pages
1--4 map without omission or duplication to printed pp. 326--329.  Expansion
image pages 1--29 map without omission or duplication to printed pp. 103--131.

### Announcement

| Printed page | Material directly checked |
|---|---|
| 326 | journal/volume/year/issue, author, Russian title, presentation date, system И, lower/upper terminology, conditional-algorithm boundary, beginning of the finite-operator equations |
| 327 | completion of the equations, Theorem 1, Cantor-space interpretation, portions including the possible empty portion, homogeneous degree/basis/transition, Theorem 2 |
| 328 | Theorem 3 and closure characterization, Theorem 4, solution versus exact graph, Theorem `4'`, general Л-solution definition, Theorem 5 and its conditional construction |
| 329 | Putnam/Church/Robinson/Elgot qualifications, receipt date, bibliography, and the correction explicitly belonging to earlier reference (2) |

### Complete expansion

| Printed page | Material directly checked |
|---|---|
| 103 | journal identity, date, author, Russian title, introduction and scope |
| 104 | system И problems, five-section roadmap, conditional terminology, beginning of exact syntax |
| 105 | atomic syntax, logical formation, eliminable equality/order/bounds/constants/shifted terms, fictitious occurrence definition |
| 106 | fictitious-occurrence examples and controlled-quantifier definitions |
| 107 | quantifier-elimination process |
| 108 | syntactic lower/upper `t`-formula classes and normal-form theorem |
| 109 | normal-form proof completion and beginning of operator theory |
| 110 | anticipation, prefix action, residual operators, whole-future finite-memory equations |
| 111 | weight, finite operators, one-state future-dependence example, canonical equations, `A`-operator terminology |
| 112 | primitive-recursive recognition/synthesis negative boundary |
| 113 | definability of canonical equations and Cantor-space setup |
| 114 | metric/topology, nonempty-prefix portion convention, coordinatewise portions, compactness facts, homogeneity definition start |
| 115 | basis/internal transitions, singleton and uncountability examples, printed weight-to-degree graph claim |
| 116 | covering operator and lemma, definability theorem start |
| 117 | definable-set homogeneity proof and effective internal transition |
| 118 | closed-homogeneous converse, recurrent form, closure characterization |
| 119 | conditional/unconditional boundary and Section 4 Theorem 1 |
| 120 | finite-realization proof, strictly weaker Theorem 2, exact two-clause general-solution definition |
| 121 | Theorem 3 alternative and stable-family deletion setup |
| 122 | deletion completion and canonical general-solution equations |
| 123 | both generality directions and weight/memory conclusions |
| 124 | closedness completion, fixed-`p` Theorem `3'`, effectiveness qualification, Section 5 start |
| 125 | explicit definitions, memory/anticipation criteria, synthesis Theorem 1 start |
| 126 | shifted-formula termination and first half of worked example |
| 127 | worked-example tables, word-order notation, automaton-enumerability/decidability, Theorem 2 statement |
| 128 | both Theorem 2 constructions and the seed needed in the converse |
| 129 | word-relation conversion and transition to the weak system |
| 130 | system И', eventually-zero predicates, special beginnings, Theorem 3 and Büchi attribution |
| 131 | two definability corollaries, receipt date, bibliography |

## Blocking findings

### AP5-01 — must-fix — the public definition of \(\mathcal I\) omits its formula syntax

**Location.** `handbook/parts/p09/presentations/n-c-014.tex:499-510`,
especially the sentence at lines 505--510 that calls \(\mathcal I\) a formal
language after giving only domains, successor, and eliminable conveniences.
Compare the fuller frozen record at
`spec/research/p09-trakhtenbrot-1961-source-note.md:107-125` and the completion
claim at `spec/research/p09-source-presentations-lot2-3.md:650,658`.

**Controlling printed source.** Expanded pp. 104--105, especially the syntax
list continued on p. 105.  The page explicitly distinguishes individual
variables, predicate variables, iterated successor terms, atomic predicate
applications, and formation by propositional operations plus individual and
predicate quantifiers.

**Violated invariant.** I26 and mandatory points M05, M24, M25, and M26.  The
standing of \(\mathcal I\) as an interpreted formal language is stated, but the
AGENTS `Definition` requirement is not: a reader cannot eliminate the name
into a grammar.  This is also narrower than M05's demand to verify the exact
syntax rather than only domains and conveniences.

**Concrete reader harm.** The later normal-form, recurrence, closure, and
\(\mathcal I'\) claims quantify over “\(\mathcal I\)-formulae,” but the reader
has never said which strings are formulae.  In particular, it does not tell a
reader whether predicate quantification is primitive, which atomic terms are
allowed, or whether the stated eliminable symbols are the only deviation from
the primitive grammar.  A hostile reader can therefore correctly say that the
named language is definition-after-use despite its semantic domain being
clear.

**Smallest exact repair.** At first introduction, after “immediate successor is
primitive,” add the source grammar in one sentence, for example:

> Put \(t^{(0)}=t\) and \(t^{(k+1)}=(t^{(k)})'\).  The atomic formulae are
> \(X(t^{(k)})\); Boolean connectives, individual quantifiers, and monadic-
> predicate quantifiers generate all formulae.

Then retain the existing sentence declaring equality, order, bounded
individual quantifiers, constants, and \(t+k\) eliminable.  Make the compact
record's “exact system” completion wording conditional on this reader repair.

### AP5-02 — must-fix — semantic dependence is substituted for the source's syntactic lower/upper \(t\)-formula definitions

**Location.** `handbook/parts/p09/presentations/n-c-014.tex:512-525`,
especially lines 515--517.  The source note similarly records the dependence
consequences without giving the source classes at
`spec/research/p09-trakhtenbrot-1961-source-note.md:127-143`; the compact record
compresses the same point at
`spec/research/p09-source-presentations-lot2-3.md:650`.

**Controlling printed source.** Announcement pp. 326--327 and expanded
pp. 106--109, especially expanded p. 108.  The expansion first defines
controlled formulae and then defines upper and lower \(t\)-formulae by
syntactic restrictions on atomic arguments and on the bounds of every
individual quantifier.  Independence from the tail or prefix is printed as a
consequence of those restrictions, not as their definition.

**Violated invariant.** I05, I06, I26, and M06, M24--M26.  The AGENTS rule
requires an exact eliminable definition at first use.  “Depends only on an
initial segment” and “depends only on the tail” define larger semantic
classes than the source's named syntactic classes.

**Concrete reader harm.** The reader weakens the exact normal-form theorem:
an effective reduction to a finite syntactic normal form becomes merely a
Boolean decomposition into unspecified semantically local formulae.  The
reported proof moves no longer prove the theorem as the source states it, and
a reader cannot check which bounded-quantifier forms the algorithm produces.
This is false compression, not a stylistic omission.

**Smallest exact repair.** Define the two syntactic classes before stating
their dependence consequences.  State that, with \(Q\in\{\forall,\exists\}\),
an upper \(t\)-formula is controlled from below, has atomic arguments that are
variables or variable-plus-numeral terms, and has individual quantifiers of
the forms \(Q\sigma_{t<\sigma}\) or
\(Q\sigma_{t<\sigma<\mu}\); a lower \(t\)-formula is the dual
controlled-from-above class with forms \(Q\sigma_{\sigma<t}\) or
\(Q\sigma_{\lambda<\sigma<t}\).  Then state separately that an upper formula
is fictitious before \(t\), while a lower formula is fictitious after
\(t+s\).  Apply the same exact distinction in the source note.

### AP5-03 — must-fix — tuple portions and the handbook-owned induced operator are not given exact eliminable definitions

**Location.** `handbook/parts/p09/presentations/n-c-014.tex:582-598`,
especially line 592 (“concatenate and take portions coordinatewise”), and
lines 625--636, where the counterexample uses paired prefixes and introduces
“operators induced on the remaining suffixes.”  Compare
`spec/research/p09-trakhtenbrot-1961-source-note.md:203-224,265-271` and
`spec/research/p09-source-presentations-lot2-3.md:652`.

**Controlling printed source.** Announcement p. 327 and expanded pp. 114--115
for one- and many-coordinate portions.  The “induced operator” terminology is
handbook-owned and therefore has no printed-source definition to borrow.

**Violated invariant.** I09 and I26; mandatory M09 and M26.  Equal prefix
lengths, coordinate types, and the relation between concatenation and graph
tails are left implicit.  The new handbook phrase “induced operator” has clear
intended standing but no exact definition at first appearance.

**Concrete reader harm.** The four-portion counterexample is the centerpiece
of the source correction.  Without a typed tuple definition, “after
\((0,0)\)” can mean an interleaved word, two one-letter coordinate prefixes,
or a single alphabet letter in a product alphabet.  Without a formula for the
induced suffix operator, the asserted equality between a graph portion and an
operator graph is not independently checkable.  The correction is
mathematically right, but its publication vocabulary fails the repository's
hard definition rule.

**Smallest exact repair.** At the tuple extension, add

\[
 M_{(u_1,\ldots,u_n)}
 =\{(Z_1,\ldots,Z_n):(u_1Z_1,\ldots,u_nZ_n)\in M\},
\]

for equal-length coordinate prefixes \(u_i\).  At first use of “induced
operator,” define, for \(u\in A^r\),

\[
 T_u(Z)=\operatorname{tail}_r(T(uZ)).
\]

Then say that zero anticipation makes every consistent paired prefix
\((u,v)\) have \((G_T)_{(u,v)}=G_{T_u}\), while an inconsistent pair has the
empty portion.  This is the exact statement the counterexample already uses.

### AP5-04 — must-fix — the reader does not explicitly own the empty-set repair

**Location.** `handbook/parts/p09/presentations/n-c-014.tex:664-670` and the
compressed statement at
`spec/research/p09-source-presentations-lot2-3.md:652`.  The detailed source
note correctly labels the split handbook-owned at
`spec/research/p09-trakhtenbrot-1961-source-note.md:281-290`.

**Controlling printed source.** Expanded p. 116 for the total covering lemma
and expanded p. 118 for the closed-homogeneous converse and recurrent form.
The printed covering proof begins with the original basis state and claims
every output lies in \(\overline M\); it does not isolate \(M=\varnothing\).

**Violated invariant.** I11 and I25, and mandatory M11, M24--M25, and M27.
The mathematics is repaired, but source/handbook ownership is not stated in
the reader at the repair's point of use.  This is inconsistent with the
reader's explicit ownership wording for both the weight-two counterexample
and the finite-word nonemptiness correction.

**Concrete reader harm.** “The empty set is handled separately” can naturally
be read as a report of what Trakhtenbrot does.  He does not print that case
split.  The contradiction \(q_1(1)=1\land q_1(1)=0\) is a sound handbook
completion, but leaving its author unstated launders a repair into the source
presentation.

**Smallest exact repair.** After line 670 add: “The nonempty restriction on
the covering lemma and this empty-set case split are handbook-owned.”  Add the
same ownership qualifier to the compact record.  The detailed source note
already has the required wording.

## Independent adversarial checks of the mandated fault lines

### The two portion conventions and the weight-two counterexample

The announcement on p. 327 expressly allows a portion to be empty.  The
expansion on p. 114 introduces a portion only after a nonempty prefix
intersection.  The frozen records correctly distinguish these conventions and
choose the announcement's all-prefix convention for the reader.

For

\[
T(X)(t)=\begin{cases}X(t),&X(1)=1,\\0,&X(1)=0,\end{cases}
\]

the output at time \(t\) is determined by \(X(1),\ldots,X(t)\), so the
operator has zero anticipation.  In the displayed two-state presentation,
induction from \(q(1)=0\) gives
\(q(t)=X(1)\mathbin{\mathsf{xor}}X(t)\); hence
\((1-q(t))X(t)\) is exactly the displayed output.  With one state the output
map would be one fixed suffix function \(f\).  Time one forces
\(f(z)=z_0\) for every suffix \(z\), but on an input beginning \(01\), time
two requires output zero while the current suffix begins with one.  Thus the
weight is exactly two.

The nonempty portions are precisely the original graph, the constant-zero
graph after the consistent pair \((0,0)\), and the identity graph after the
consistent pair \((1,1)\).  An inconsistent pair such as \((0,1)\) gives the
empty portion.  Hence the expansion convention sees three distinct nonempty
portions and the announcement convention sees those three plus the empty
portion.  This refutes both the printed \(k\) claim and a \(k+1\) repair at
\(k=2\).  The two-state presentation, lower bound, count, diagnosis of the
future-dependent state, and explicit handbook ownership are mathematically
sound.  AP5-03 concerns only the missing exact publication definitions needed
to carry that sound argument.

### Nonempty covering versus the empty set

The p. 116 covering operator is total, so its image is nonempty.  It therefore
cannot have image \(\overline\varnothing=\varnothing\).  The initial induction
that every reached basis member is nonempty also fails when the original
basis member is empty.  Restricting that construction to \(M\ne\varnothing\)
is necessary.  The inconsistent initial conjunction in the same recurrent
shape defines the empty set exactly, so the converse theorem survives.  The
mathematical distinction is clean; AP5-04 is the missing public ownership
sentence.

### Operator-class and topology boundaries

The frozen reconstruction preserves all relevant strict distinctions.
Broad finite memory permits \(\Phi\) and \(\Psi\) to inspect an entire future
suffix; it does not imply bounded anticipation or effectiveness.  A finite
operator adds one fixed finite anticipation bound.  An \(A\)-operator in the
expansion, or Л-operator in the announcement, is the zero-anticipation finite
subclass.  The typographic normalization is declared and not transferred
silently.

For a continuous total operator with definable graph, the finite graph-portion
basis gives finitely many residual situations.  On each nonempty compact
domain, continuity is uniform; taking the maximum of the finitely many bounds
gives one anticipation bound, while the portion index supplies finite memory.
The expanded Theorem 2 argument retains the finite portion index after
continuity is removed but loses the finite anticipation bound.  The reader
states exactly that weaker conclusion.

Closedness is used at every place where compatible finite prefixes must yield
actual membership: the closed-homogeneous converse, the covering image, the
finite-realization/general-solution arguments, and stable deletion.  It is not
silently imposed on the open-relation variant, which is separately reported
without a weight bound.

### General solutions, fixed lookahead, and conditionality

The general \(A\)-solution definition contains both required quantifiers:
every \(A\)-solution arises from an \(A\)-operator parameter substitution,
and every such substitution yields a solution.  Replacing the class
throughout gives the general zero-anticipation definition.  The parameter is
correctly a stream tuple rather than an untyped finite-state choice.

The stable-deletion summary preserves the no-solution branch, the surviving
family, free-parameter selection, finite portion memory, and the use of
closedness.  Expanded Theorem `3' is correctly scoped separately to each fixed
\(p\); no unbounded-lookahead general solution is inferred.  Internal
transition construction is unconditional, while external output choice and
deletion require nonemptiness/truth decisions.  Putnam is restricted to the
stated recurrent fragment.

### Explicit synthesis and finite words

The explicit-definition standing, semantic anticipation test, finite shifted-
formula termination, canonical equations, and pp. 126--127 two-formula
example are all kept within Section 5.  The typed maps \(T_t:A^t\to B^t\)
are well-defined by zero anticipation and are prefix-compatible.

The empty language independently refutes the printed converse of expanded
Theorem 2: it is recognized by a constant-zero operator and satisfies prefix
closure and extendibility vacuously, but a total length-preserving operator
has nonempty range at every positive length.  Adding nonemptiness repairs the
proof because prefix closure plus proper extendibility then supplies a member
at every positive length, including the “first word” used on p. 128.  The
reader correctly labels this repair handbook-owned.

The weak system \(\mathcal I'\), special beginnings, existence for arbitrary
\(\mathcal I\)-formulae, effective construction for \(\mathcal I'\)-formulae,
and Büchi attribution all match pp. 130--131.  The modern regular/MSO sentence
is clearly labelled modern in the shared theorem and is not quoted as a
literal result of either Russian body.

### Source identity, translation, rights, and completion boundaries

The printed bodies verify the identical Russian title, distinct journals,
years, volumes/issues, pagination, source order, and receipt/presentation
dates recorded in the source note.  The frozen bibliography and source record
consistently preserve Math-Net's distinct official English renderings:
“Single-Place” for 1961 and “One-Place” for 1962.  The later AMS translation is
identified as an unacquired body and is not used as evidence.

The rights wording is appropriately narrow: public archival access is not
called an open-content licence; the individual noncommercial printing
exception is not expanded into electronic-copy or redistribution permission;
and the local PDFs are called research objects.  No protected page image or
extended source prose is proposed for republication.

The source note and compact record both leave independent review pending; the
reader claims reconstruction, not admission.  The shared theorem calls its
compound-name sentence modern, and the Thomas paragraph does not turn a later
survey into either original source.  Nothing in the snapshot claims literal
Büchi 1960 reconciliation, N-c-014 overall admission, Part IX completion,
rendered-handbook inspection, human review, final-book completion, or user
acceptance.

## Invariant disposition

| Invariant | Disposition |
|---|---|
| I01 | checked-clean: announcement/expansion identities, pagination, numbering, and strengths remain distinct |
| I02 | checked-clean: same Russian title and distinct official English renderings are preserved |
| I03 | checked-clean as to standing and typographic normalization; AP5-01 blocks exact definitional completeness |
| I04 | checked-clean: domains, successor, and eliminable conveniences are correct |
| I05 | finding-linked: AP5-02; semantic dependence is correct but does not define the printed syntactic classes |
| I06 | finding-linked: AP5-02; conclusion and proof moves are sound, exact normal-form vocabulary is incomplete |
| I07 | checked-clean: anticipation, broad memory, finite operator, and normalized `A`/Л classes remain distinct |
| I08 | checked-clean: weight and the one-state noneffective future-dependence example are preserved |
| I09 | finding-linked: counterexample and both convention counts are correct; AP5-03 blocks exact tuple/induced-operator terminology |
| I10 | checked-clean: homogeneity, closed converse, and nondefinable homogeneous sets are all visible |
| I11 | finding-linked: mathematical nonempty/empty split is correct; AP5-04 blocks source ownership |
| I12 | checked-clean: closure characterization and open descriptive-set question remain distinct |
| I13 | checked-clean: internal/external effectiveness and Putnam's limited role are exact |
| I14 | checked-clean: continuity, compact uniformity, finite memory, and bounded anticipation are all used |
| I15 | checked-clean: expanded Theorem 2 concludes finite memory only |
| I16 | checked-clean: exact graph definition and graph-contained solution are separated |
| I17 | checked-clean: both soundness and completeness quantifiers of general solutions are present |
| I18 | checked-clean: deletion, alternative, parameters, weight, closedness, and conditionality are preserved |
| I19 | checked-clean: Theorem `3' is fixed separately for each `p` |
| I20 | checked-clean: explicit-definition results and worked-example scope remain in Section 5 |
| I21 | checked-clean: word maps, recognition/enumeration, and handbook-owned nonemptiness correction are exact |
| I22 | checked-clean: \(\mathcal I'\), special beginnings, unequal existence/effectivity, and Büchi attribution are exact |
| I23 | checked-clean: modern folklore is labelled modern and the source packages remain separate |
| I24 | checked-clean: historical comparisons are reports, not priority adjudications |
| I25 | finding-linked only for AP5-04's attribution ambiguity; the overall bounded-translation disclaimer is otherwise clean |
| I26 | finding-linked: AP5-01, AP5-02, and AP5-03 |
| I27 | checked-clean: access and rights are not inflated |
| I28 | checked-clean: no prohibited software/build evidence was used or claimed |
| I29 | checked-clean: topic-only completion boundary is explicit |
| I30 | checked-clean: blind-review boundary was maintained |

## Mandatory coverage disposition

| Point | Disposition |
|---|---|
| M01 | checked-clean: all seven hashes recomputed and matched |
| M02 | checked-clean: all 4 + 29 images read at original detail; page maps confirmed |
| M03 | checked-clean within the frozen evidence: identities, dates, journals, pagination, titles, routes, source order, and rights wording agree |
| M04 | checked-clean with the competence limitation stated at the start of this report |
| M05 | finding-linked: AP5-01 |
| M06 | finding-linked: AP5-02 |
| M07 | checked-clean: operator map, anticipation, prefix action, broad memory, weight, finite windows, `A` standing, and nonimplications verified |
| M08 | checked-clean: recognition/synthesis negative boundary and one-state example verified |
| M09 | finding-linked: counterexample and convention mathematics checked clean; AP5-03 blocks publication terminology |
| M10 | checked-clean: formula portions yield finitely many residuals and effective internal transitions |
| M11 | finding-linked: converse/recurrence/closure mathematics checked; AP5-04 blocks ownership of the empty case |
| M12 | checked-clean: unconditional internal construction, conditional choice/deletion, and Putnam fragment separated |
| M13 | checked-clean: compact uniformity, one bound, portion memory, and weight argument independently reconstructed |
| M14 | checked-clean: noncontinuous theorem does not acquire anticipation |
| M15 | checked-clean: graph/solution distinction and both closed/open clauses of Theorem `4' verified |
| M16 | checked-clean: both parameter-substitution directions and standing verified |
| M17 | checked-clean: deletion branches, surviving family, parameter choice, closedness, weight, and conditionality verified |
| M18 | checked-clean: fixed-`p` scope verified; no unbounded transfer |
| M19 | checked-clean: explicit standing, semantic criteria, termination, equations, and pp. 126--127 example verified |
| M20 | checked-clean: both word-set definitions and both theorem directions checked, including the necessary repair |
| M21 | checked-clean: \(\mathcal I'\), special beginning, Theorem 3, attribution, and effectivity split verified |
| M22 | checked-clean: announcement Theorems 1--5 and `4' were compared with the separately numbered expanded results |
| M23 | checked-clean: shared theorem and Thomas paragraph explicitly prevent compound-name laundering |
| M24 | finding-linked: cross-object identities and status are consistent; AP5-01--AP5-04 identify the remaining reader/record completion defects |
| M25 | finding-linked: locators, numbering, formulae, citations, titles, and qualifiers otherwise check; AP5-02 and AP5-04 require exact source-strength repair |
| M26 | finding-linked: AP5-01, AP5-02, AP5-03 |
| M27 | finding-linked: hidden topology/class collapses were not found; AP5-02 is false compression and AP5-04 is repair-ownership laundering |
| M28 | checked-clean: topic, rights, and no-test/no-build boundaries enforced |

No blocker was found in the weight-two mathematics, empty-set repair,
finite-realization argument, general-solution quantifiers, fixed-lookahead
scope, finite-word nonemptiness correction, source identities, or rights
boundary.  The four findings above nevertheless remain must-fix because the
charter makes exact definition and honest repair ownership conditions of
publication admission.

VERDICT: REJECT — AP5-01, AP5-02, AP5-03, AP5-04

# Round 5 source-fidelity, language, and evidence review

## Disposition

I found no blocker, must-fix, should-fix, or consider finding within the
source-fidelity seat's mandate.  The seven frozen objects have the identities
fixed by the Round 5 charter; the reader, source note, compact record, shared
finite-word theorem, and bibliography consistently distinguish the 1961
announcement from the 1962 expansion; and every source claim I checked is
supported at its stated strength by the controlling printed pages.  The two
handbook-owned mathematical corrections---the weight-two graph-portion
counterexample and the separate empty-set recurrence---also survive independent
derivation below.

Acceptance here is only manuscript-content acceptance for `N-c-014.c` on this
unchanged snapshot.  It is not Russian-language-specialist certification,
admission of another presentation or Part IX, rendered-handbook review, final
book completion, or user acceptance.

## Blindness, permitted evidence, and language disclosure

I read the Round 5 charter and only the seven frozen Round 5 objects and the
charter-permitted original-detail page renders of the two source bodies.  I did
not read the board ledger, chair transcript, any Round 1--4 report, or either
other Round 5 report, and I did not contact another reviewer.  I did not inspect
a handbook PDF.  I ran no test, test harness, automated checker, repository
script, TeX command, interim build, or build.  SHA-256 was used only for the
identity labels expressly required by M01.  The two OCR/layout text files were
not used to decide a formula, symbol, wording, or language question.

My Russian competence is working source-checking competence in printed
mathematical Russian: I can follow the definitions, theorem statements,
quantified claims, proof transitions, standard logic/automata vocabulary, and
historical qualifications on these pages, and I compared every material symbol
with the scan.  I am not a native Russian speaker, a professional translator,
or a credentialed Russian-language specialist.  This report therefore supports
a direct source-fidelity verdict but makes no specialist certification.  The
official English title forms and rights statement are record-level evidence in
the frozen source note and bibliography, not translations I inferred from the
Russian bodies.

## M01: frozen identity labels

I recomputed all seven hashes before substantive review.  Each matched the
Round 5 charter exactly.

| Frozen object | Recomputed SHA-256 | Status |
|---|---|---|
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1961.pdf` | `44213AEBE4DB2F1C389B812A7401138799C3DB4749C3605BA7211BBB4BAF96F9` | match |
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1962-expanded.pdf` | `EAB4438A7BBA2B6009374826A98A3A61FB6465C493F57B03D2C6C7385824096D` | match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `070252A0A152D814FD1420FDBF889CAA9FEFBB5D187B2C1CDAB1B0595CAA13DB` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD` | match |
| `handbook/bib/handbook.bib` | `75AB70009DF4AB8B2180CFFC6987EA244ADB2F978B1D889C87009EFF17066D5C` | match |
| `spec/research/p09-trakhtenbrot-1961-source-note.md` | `6C214BCC16961AEC1124D87FA5D474E957B93C083CA377C5EC414DCF055FC655` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `667283E6415851F28A35EEE339DD466AA8706DB13DC05EA0ACDCAF096A24E974` | match |

The source-file sizes also agree with the frozen custody record: 566,358 bytes
for the announcement and 1,884,181 bytes for the expansion
(`p09-trakhtenbrot-1961-source-note.md:28-31,49-53`).

## M02: complete visual page inspection and page maps

I visually read every listed render at original detail.  The announcement map
is:

| Physical render | Printed page | Visual anchor |
|---|---:|---|
| `rendered/page-1.jpg` | 326 | journal/volume/year, author, Russian title, system and normal-form setup |
| `rendered/page-2.jpg` | 327 | canonical equations, Theorems 1--2, all-prefix portions and homogeneity |
| `rendered/page-3.jpg` | 328 | Theorems 3, 4, (4'), and 5; general-solution definition |
| `rendered/page-4.jpg` | 329 | Putnam/Church/Robinson and Elgot qualifications, receipt, bibliography |

The expansion map is consecutive and complete:

| Physical render | Printed page | Visual anchor |
|---|---:|---|
| `expanded-rendered/page-01.jpg` | 103 | journal/volume/year, author, Russian title, introduction |
| `expanded-rendered/page-02.jpg` | 104 | introduction and start of \(\mathcal I\) syntax |
| `expanded-rendered/page-03.jpg` | 105 | syntax, eliminable extensions, fictitious occurrence |
| `expanded-rendered/page-04.jpg` | 106 | dependence examples and controlled formulas |
| `expanded-rendered/page-05.jpg` | 107 | quantifier-elimination procedure |
| `expanded-rendered/page-06.jpg` | 108 | lower/upper forms and normal-form proof |
| `expanded-rendered/page-07.jpg` | 109 | end of normal-form proof; start of operators |
| `expanded-rendered/page-08.jpg` | 110 | anticipation, prefix maps, whole-future finite memory |
| `expanded-rendered/page-09.jpg` | 111 | weight, finite operators, \(A\)-operators, periodicity |
| `expanded-rendered/page-10.jpg` | 112 | primitive-recursive recognition/synthesis boundary |
| `expanded-rendered/page-11.jpg` | 113 | \(\mathcal I\)-encoding of canonical equations; Cantor setup |
| `expanded-rendered/page-12.jpg` | 114 | intervals, nonempty-prefix portions, topology |
| `expanded-rendered/page-13.jpg` | 115 | homogeneity, examples, graph claim, transition data |
| `expanded-rendered/page-14.jpg` | 116 | covering operator and lemma; start of definability theorem |
| `expanded-rendered/page-15.jpg` | 117 | effective homogeneity proof |
| `expanded-rendered/page-16.jpg` | 118 | closed-homogeneous converse, recurrent form, closure result |
| `expanded-rendered/page-17.jpg` | 119 | conditionality/Putnam; start of finite realization |
| `expanded-rendered/page-18.jpg` | 120 | Theorem 1 proof, Theorem 2, general \(A\)-solution definition |
| `expanded-rendered/page-19.jpg` | 121 | Theorem 3 and stable portion systems |
| `expanded-rendered/page-20.jpg` | 122 | deletion and parameterized construction |
| `expanded-rendered/page-21.jpg` | 123 | both generality clauses and weight discussion |
| `expanded-rendered/page-22.jpg` | 124 | closedness step, fixed-\(p\) Theorem \(3'\), start of Section 5 |
| `expanded-rendered/page-23.jpg` | 125 | explicit definitions, semantic anticipation tests, Theorem 1 |
| `expanded-rendered/page-24.jpg` | 126 | shifted-formula algorithm and worked example |
| `expanded-rendered/page-25.jpg` | 127 | worked-example tables and finite-word definitions/Theorem 2 |
| `expanded-rendered/page-26.jpg` | 128 | both finite-word directions and the source's selection construction |
| `expanded-rendered/page-27.jpg` | 129 | continuation of explicit finite-word/operator construction |
| `expanded-rendered/page-28.jpg` | 130 | weak system \(\mathcal I'\), special beginnings, Theorem 3 |
| `expanded-rendered/page-29.jpg` | 131 | Theorem 3 corollaries, receipt, bibliography |

Thus physical announcement pages 1--4 map to printed 326--329, and physical
expansion pages 01--29 map to printed 103--131 without a gap, duplicate, or
pagination transfer.

## Source identity, order, titles, routes, and rights (M03--M04)

The Russian title printed on announcement p. 326 and expansion p. 103 is the
same: `КОНЕЧНЫЕ АВТОМАТЫ И ЛОГИКА ОДНОМЕСТНЫХ ПРЕДИКАТОВ`.  The frozen record
correctly preserves the official English-title distinction rather than deriving
two English titles from that one Russian heading: “Finite Automata and the
Logic of Single-Place Predicates” for the 1961 Math-Net record and “Finite
Automata and the Logic of One-Place Predicates” for the 1962 record
(`p09-trakhtenbrot-1961-source-note.md:22-27,43-48`; `handbook.bib:5991-6013`;
`n-c-014.tex:487-497`).

The announcement is visibly *Doklady Akademii Nauk SSSR*, volume 140, no. 2
(1961), printed pp. 326--329.  Its first page records presentation by P. S.
Novikov on 16 V 1961, and p. 329 records receipt on 29 IV 1961.  The expansion
is visibly *Sibirskii Matematicheskii Zhurnal*, volume III, no. 1,
January--February 1962, printed pp. 103--131, with receipt 15 V 1961 on p. 131.
These details agree with `p09-trakhtenbrot-1961-source-note.md:24-41,45-69`,
`p09-source-presentations-lot2-3.md:646-648`, and
`handbook.bib:5991-6013`.

The authority order is also honest: the four-page Doklady item is the registered
announcement and controls its Theorems 1--5 and \(4'\); the twenty-nine-page
Sibirskii item is the later complete expansion and controls its five sections
and distinct numbering (`n-c-014.tex:487-497`; announcement pp. 326--329;
expansion pp. 103--131).  The Math-Net record URLs, two local research-object
paths, and the unacquired later AMS-translation route are stated without using
the later translation as evidence (`p09-trakhtenbrot-1961-source-note.md:27-35,
48-69`).

The rights statement is appropriately narrow.  It reports only the frozen
Math-Net personal-use printing exception for individual teachers, students,
and researchers engaged in noncommercial teaching or research; it then says
that other reproduction/republication requires permission, denies any
open-content inference, and treats the local PDFs only as research objects
(`p09-trakhtenbrot-1961-source-note.md:71-77`;
`p09-source-presentations-lot2-3.md:648`).  Neither reader nor record infers an
electronic-copy or redistribution licence.  Under this round's closed evidence
boundary I assessed the frozen route and qualification; I did not make a
current-web-availability claim.

## Formal system and normal form (M05--M06)

### Syntax, interpretation, and standing

The source's Cyrillic capital И is visible throughout both bodies.  The
reader's declared typographic rendering \(\mathcal I\), followed immediately by
its standing as an interpreted formal language, is exact and prevents the
letter from being mistaken for an automaton, set, or theorem
(`n-c-014.tex:499-510`; announcement p. 326; expansion pp. 103--105).
Individuals range over \(1,2,\ldots\), predicate variables over arbitrary
subsets of that domain, and immediate successor is primitive.  Expansion
p. 105 then explicitly lists equality, order, bounded individual quantifiers,
constants, and shifted terms as eliminable conveniences.  The reader neither
makes order/addition primitive nor conflates this system with the eventually
zero weak system (`n-c-014.tex:499-510`;
`p09-trakhtenbrot-1961-source-note.md:107-125`; expansion pp. 104--105).

The weak system \(\mathcal I'\) is not introduced prematurely.  Expansion
p. 130 defines it by restricting predicate variables to predicates eventually
equal to zero; the reader introduces it only at `n-c-014.tex:801-810` and keeps
that domain separate from unrestricted \(\mathcal I\).

### Semantic dependence and normal-form proof

Expansion pp. 105--106 define fictitious occurrence outside an interval by
invariance under changes outside that interval.  The reader therefore correctly
calls it semantic independence and expressly rejects a written-symbol test
(`n-c-014.tex:512-515`).  Lower \(t\)-formulae have bounded-prefix dependence
through \(t+s\); upper \(t\)-formulae have tail dependence from \(t\).  The
announcement introduces the lower/upper distinction on p. 326 and states
Theorem 1 on p. 327; expanded \S1.3--1.4 supplies the elimination and proof on
pp. 106--109.

The reported proof architecture is present in the expansion: predicate
quantifiers are moved ahead of individual quantifiers; individual quantifiers
are pushed into the matrix and split relative to \(t\); lower and upper pieces
are separated; and the remaining predicate quantifier is distributed by
splicing prefix and tail interpretations (expansion pp. 107--109).  This
supports exactly `n-c-014.tex:515-525` and the fuller record at
`p09-trakhtenbrot-1961-source-note.md:127-143`.  The source claims an effective
transformation, and the reader reports an effective transformation, not merely
the existence of a normal form.

## Operators, effectiveness boundary, and noncollapse (M07--M08)

Expansion pp. 109--111 support every type and equation at
`n-c-014.tex:527-571`:

- an operator is a total stream map between finite alphabets;
- anticipation \(p\) means output at \(t\) is independent of input after
  \(t+p\), and \(p=0\) is the hereditary/prefix condition;
- finite memory uses a finite state alphabet but lets both output and update
  functions inspect the *whole* suffix \(a(t),a(t+1),\ldots\);
- weight is the least memory-state cardinality;
- a finite operator adds one bounded anticipation window; and
- the automaton-realizable zero-anticipation finite class is called Л in the
  announcement and Latin \(A\) in the expansion.

The reader explicitly declares the normalization when combining versions
(`n-c-014.tex:563-570`) and does not transfer the Latin letter into the 1961
source.  It also keeps zero anticipation, finite memory, finite operator, and
\(A\)-operator distinct.

The source's one-state example on expansion p. 111 outputs one exactly when a
later input position contains one.  Its whole-future suffix function gives
one-state memory while allowing unbounded, nonrecursive dependence.  This
confirms `n-c-014.tex:551-554`; it also directly prevents any inference from
finite memory to bounded anticipation or effectiveness.

The negative primitive-recursive boundary at `n-c-014.tex:573-580` is supported
by expansion pp. 111--112.  The source's “periodic” includes a finite preperiod,
so the reader's modern gloss “ultimately periodic” is accurate.  The two source
reductions respectively rule out deciding whether the primitive-recursive
constant output is ultimately periodic and effectively extracting canonical
finite-state equations even when the constructed output is periodic.  The
reader does not enlarge those statements into an unrestricted recursion
theorem.

## Portions and the weight-two counterexample (M09)

### The two printed conventions

Announcement p. 327 defines every finite-prefix residual and explicitly says it
may be empty.  Expansion p. 114 first requires the prefix interval to meet
\(M\), then calls the resulting residual a portion; its convention therefore
names only nonempty residuals.  Both sources include \(M\) itself in the basis
(announcement p. 327; expansion p. 115), i.e. the empty-prefix residual/basis
member.  The reader openly adopts the announcement's all-prefix convention and
states the expansion's restriction (`n-c-014.tex:582-598`).  Product portions
are formed by fixing the coordinate prefix at each time and shifting all
coordinates together, as on expansion pp. 113--115.

Homogeneous degree, basis, and internal transition are also represented at the
right standing.  They are respectively a finite-residual property, a finite
list of residual stream sets, and the map induced by appending one letter; none
is presented as a new automaton kind (`n-c-014.tex:593-598`; announcement
p. 327; expansion p. 115).

### Independent derivation of every counterexample clause

Let
\[
 T(X)(t)=\begin{cases}X(t),&X(1)=1,\\0,&X(1)=0.\end{cases}
\]
as at `n-c-014.tex:600-611`.  This construction is expressly labelled
handbook-owned; its controlling source target is the printed whole-future
memory definition on expansion p. 110 and the printed \(k\)-homogeneity claim
on p. 115.

1. **Zero anticipation.**  For each \(t\), the output prefix through \(t\)
   depends only on \(X(1),\ldots,X(t)\).  Hence two inputs agreeing through
   \(t\) have equal output through \(t\).  No future coordinate is used.

2. **Displayed two-state presentation.**  Put \(Q=\{0,1\}\), \(q(1)=0\),
   \(\Phi(q,z)=(1-q)z_0\), and
   \(\Psi(q,z)=q\mathbin{\mathsf{xor}}z_0\mathbin{\mathsf{xor}}z_1\), exactly
   as at `n-c-014.tex:613-621`.  Induction gives
   \[
     q(t)=X(1)\mathbin{\mathsf{xor}}X(t):
   \]
   it holds at \(t=1\), and the update cancels \(X(t)\) and inserts
   \(X(t+1)\).  If \(X(1)=0\), then \((1-q(t))X(t)=0\); if \(X(1)=1\), it is
   \(X(t)\).  The equations therefore give exactly \(T\) and are legal under
   the source's whole-suffix definition.

3. **No one-state presentation.**  With one state, one suffix function
   \(\Phi(z)\) is used at every time.  At time one the required output is
   \(z_0\) for *every* input stream, so \(\Phi(z)=z_0\) for every suffix
   \(z\).  On an input beginning \(01\), the time-two suffix begins in one,
   forcing output one, while the defined operator must output zero because
   \(X(1)=0\).  Thus weight is exactly two
   (`n-c-014.tex:622-625`).

4. **All three nonempty residuals.**  Write \(\Gamma_T\) for the graph.  Its
   empty-prefix residual is \(\Gamma_T\).  After the consistent paired prefix
   \((0,0)\), every remaining input suffix is paired with the all-zero output,
   giving the constant-zero graph.  After \((1,1)\), every suffix is paired
   with itself, giving the identity graph.  These three sets are pairwise
   distinct and nonempty.  Further consistent prefixes remain in one of the
   latter two residuals.

5. **The fourth all-prefix residual.**  The paired prefix \((0,1)\) is
   inconsistent with the graph, so its residual is \(\varnothing\).  All
   inconsistent prefixes have that same residual.  Hence the expansion's
   nonempty convention sees three distinct basis residuals, while the
   announcement's all-prefix convention sees exactly four
   (`n-c-014.tex:625-636`).

For \(k=2\), three nonempty residuals refute the printed \(k\) claim, and four
all-prefix residuals refute a \(k+1\) repair.  The failed inference is exactly
the one the reader identifies: in the displayed broad presentation, the state
after a fixed prefix may still depend on the next suffix coordinate, because
\(\Psi\) is allowed to inspect the whole future.  A residual graph is therefore
not determined merely by one of the two broad memory states.  The safe statement
at `n-c-014.tex:631-638`---count the distinct induced suffix operators and add
the possible empty residual only under the all-prefix convention---is exact and
does not disturb the independently valid closedness claim.

The remaining examples are also supported.  Expansion p. 115 states that a
singleton is homogeneous exactly when its stream is periodic in the source's
ultimately-periodic sense, and supplies an uncountable family of
one-homogeneous sets against only countably many formulas.  This supports
`n-c-014.tex:639-641` without implying definability from homogeneity alone.

## Definability, topology, effectivity, and the empty set (M10--M12)

### Effective homogeneity

Announcement Theorem 2 (p. 327) and expanded \S3 Theorem 1 (pp. 116--118)
support `n-c-014.tex:643-646`.  Independently, after fixing a prefix in the
expanded normal form, each lower formula becomes one of finitely many Boolean
functions of a fixed-size boundary window, while each upper formula is shifted
back to the same finite syntactic repertoire.  Thus only finitely many residual
formulas occur.  Appending a bit performs that residual transformation directly,
so the internal transition is effective and does not require a truth or
nonemptiness oracle.  Including the false residual under the announcement's
all-prefix convention preserves finiteness and gives it a self-loop.

### Closed-homogeneous converse and recurrence

Announcement Theorem 3 (p. 328) and expanded \S3 Theorems 2 and \(2'\)
(p. 118) give the converse at exactly the closed strength used at
`n-c-014.tex:646-677`.  “Closed” is defined before the theorem as Cantor-product
closedness (`n-c-014.tex:600`).  The recurrent display has the correct
standings: \(X\) is the free member stream; \(q_1,\ldots,q_k\) are bound state
predicates; \(U\) is a bound choice predicate; the current/next matrix is
quantifier-free; and the literal initial vector selects the basis member
representing \(M\) (`n-c-014.tex:647-663`; expansion p. 118).

The topological direction can also be checked independently.  The local
current/next constraints define a closed subset of the compact product of the
free stream and finitely many witness streams.  Projection of that compact
closed set is compact, hence closed.  Only finitely many possible witness-state
sets can remain after a prefix, so its residual family is finite.  Thus every
formula of the recurrent shape defines a closed homogeneous set, as the reader
states at line 671.

For the reverse direction, the finite portion basis supplies the state and
transition data; the choice predicate selects a permitted next coordinate; and
the source's covering lemma identifies the image with \(\overline M\).  When
\(M\) is closed, this is \(M\).  Logical complement, finite union, and
existential predicate projection implement the closure operations, while the
normal form supplies the reverse generation argument.  The resulting least
class statement at `n-c-014.tex:672-675` matches announcement p. 328 and
expansion p. 118.  The announcement's Borel/projective identification question
is left open, not answered by modern knowledge.

### Independent nonempty-covering/empty-set check

The covering construction on expansion p. 116 is total on a nonempty full
parameter-stream space.  A total map from that domain necessarily has nonempty
image.  It therefore cannot have image \(\overline\varnothing=\varnothing\).
The proof on p. 116 also claims at every stage that the basis member selected by
the state is nonempty, which already fails at the initial state if \(M\) is
empty.  Nonemptiness is thus a real, unprinted hypothesis of that lemma, not a
cosmetic preference.

The reader repairs only that proof boundary.  At `n-c-014.tex:664-670` it
restricts the total covering argument to a nonempty homogeneous set.  For the
empty set it retains the same existential-predicate recurrent form but conjoins
the fixed initial requirement \(q_1(1)=1\) with \(q_1(1)=0\).  No assignment can
satisfy both, so the formula defines exactly the empty set.  This independently
proves the missing case without altering the source theorem, and the text
labels the split handbook-owned.  The same correction is consistently recorded
at `p09-trakhtenbrot-1961-source-note.md:281-290` and
`p09-source-presentations-lot2-3.md:652`.

### Conditionality and Putnam

The reader preserves the source's exact effective boundary
(`n-c-014.tex:679-686`).  Residual/current-state transition is syntactic and
unconditional.  Choosing an external output requires deciding which residual
sets are nonempty, hence truth of closed \(\mathcal I\)-sentences.  Announcement
pp. 326, 328 and expansion p. 119 call the resulting procedure conditional.
Expansion p. 119 then invokes Putnam only for the existential-predicate,
individual-quantifier, quantifier-free-matrix fragment that contains the
displayed recurrence.  The reader does not retroactively erase the historical
condition for arbitrary formulas.

## Supplementary source check: finite realization and general solutions

Although M13--M18 are not mandatory coverage points for this seat, I checked
all corresponding source claims because this mandate requires every reader
claim to have the stated source strength.

- `n-c-014.tex:688-698` matches announcement Theorem 4 on p. 328 and expanded
  \S4 Theorems 1--2 on pp. 119--120.  Continuity plus compactness gives one
  finite anticipation bound across the finite portion basis; the basis gives
  finite memory and the weight bound.  Expanded Theorem 2 expressly removes
  continuity and concludes only finite memory.  The reader does not infer
  bounded anticipation there.
- `n-c-014.tex:700-710` correctly distinguishes an exact graph definition from
  a solution whose graph is merely contained in the relation.  Announcement
  Theorem \(4'\), p. 328, concerns a closed homogeneous relation: continuous
  solution implies bounded-weight finite solution, and any zero-anticipation
  solution implies a bounded-weight Л-solution.  The announcement separately
  mentions the open-relation analog without the weight bound.
- Both quantifiers in the general-solution definition at
  `n-c-014.tex:712-726` are printed on announcement p. 328 and expansion
  p. 120: every solution of the named class must arise by a parameter operator,
  and every parameter operator of that class must yield a solution.  Replacing
  the finite automaton-realizable class throughout by arbitrary
  zero-anticipation operators gives the second, nonredundant generality notion.
- `n-c-014.tex:728-746` matches announcement Theorem 5 on pp. 328--329 and
  expanded \S4 Theorems 3 and \(3'\) on pp. 121--124.  The stable-deletion
  proof has both branches: deletion of the initial portion excludes every
  zero-anticipation solution; survival produces the parameterized family.
  Parameter bits select permitted outputs, the finite residual transition gives
  the general \(A\)-operator, closedness converts finite-prefix compatibility
  into relation membership, and residual nonemptiness is the conditional step.
  Theorem \(3'\) is separately quantified for each fixed \(p\), using a shift
  reduction; it is not an unbounded-lookahead general solution.

## Explicit synthesis and finite words (M19--M21)

### Explicit definitions and the pp. 126--127 example

Expansion pp. 124--125 define the explicit form
\(Y(t)\leftrightarrow\varphi(X_1,\ldots,X_m;t)\).  The three claims at
`n-c-014.tex:748-756` have the exact printed scope: every such definition has
finite memory; anticipation bounded by \(p\) is equivalent to semantic
independence outside \([1,t+p]\); and the \(A\)-operator case is independence
outside \([1,t]\).

For the zero-shift prefix-controlled case, expansion pp. 125--126 fixes each
possible first input column, computes the first output, shifts the remaining
formula, and repeats.  The normal form permits only finitely many shifted
formulas, so the process terminates and those formulas supply canonical output
and transition functions.  The worked example begins on p. 126 and ends on
p. 127.  It produces exactly two residual formulas and prints both the
\(\Phi\)- and \(\Psi\)-tables.  The reader uses it only as an illustration of
that explicit synthesis algorithm (`n-c-014.tex:757-761`), not as a proof of a
broader implicit-synthesis theorem.

### Typed word action and both directions of Theorem 2

The typed maps at `n-c-014.tex:763-774` are correct consequences of zero
anticipation.  If two infinite extensions of \(u\in A^t\) agree through \(t\),
their output prefixes through \(t\) agree, so \(T_t\) is extension-independent.
Applying the same fact at every \(s\leq t\) proves prefix compatibility.

Expansion p. 127 defines automaton-enumerability by the lengthwise image of an
\(A\)-operator and automaton-decidability by the recognizer result on the
presented word.  The terminal-output formulation at
`n-c-014.tex:776-788` makes the source's word result type explicit without
turning a stream range into a finite-word set.

Both directions on pp. 127--128 were checked:

1. For an enumerating operator, membership of a length-\(t\) word is the
   existential assertion that some input prefix produces all of its \(t\)
   coordinates.  The source writes this as a prefix-controlled formula and
   synthesizes the recognizing \(A\)-operator.  Thus enumerable implies
   decidable.
2. For the converse, the source keeps an accepted input word unchanged; if the
   current word is not accepted, it takes the longest accepted prefix and the
   first accepted length-\(t\) continuation.  Prefix closure and proper
   extendibility justify the compatibility part of this selection---provided
   an accepted seed exists.

The omitted seed is a genuine source edge case.  The empty language is decided
by the constant-zero recognizer and satisfies the two printed hypotheses
vacuously, but every total \(T_t:A^t\to B^t\) has nonempty image.  Adding
\(L\ne\varnothing\), as at `n-c-014.tex:790-799`, fixes the construction:
prefixes of one member supply every shorter positive length, and proper
extension plus prefix closure supplies every longer length.  The reader both
proves and labels this nonemptiness clause handbook-owned.

### \(\mathcal I'\), special beginnings, and Büchi

Expansion p. 130 defines \(\mathcal I'\) by eventually-zero predicate
quantification.  A special beginning ends at \(t\) only when every later value
of that same predicate is zero; it is not an arbitrary prefix.  Expanded
Theorem 3 on pp. 130--131 gives existence of a recognizing \(A\)-operator for
an arbitrary \(\mathcal I\)-formula, but effective construction only when the
formula is in \(\mathcal I'\), explicitly crediting Büchi.  This is exactly the
split at `n-c-014.tex:801-810`.

## Numbering, modern theorem boundary, and cross-record reconciliation

### M22: announcement versus expansion

No numbering or proof detail is transferred silently.

| 1961 announcement | Controlling page | Expanded development | Controlling pages | Reader location |
|---|---:|---|---:|---:|
| Theorem 1, lower/upper normal form | 327 | \S1.4 unnumbered normal-form theorem and proof | 108--109 | 517--525 |
| Theorem 2, definable implies homogeneous/effective transition | 327 | \S3 Theorem 1 | 116--118 | 643--646 |
| Theorem 3, recurrent closed-homogeneous base and closure characterization | 328 | \S3 Theorems 2 and \(2'\), corollary | 118 | 646--677 |
| Theorem 4, continuous definable graph | 328 | \S4 Theorem 1 | 119--120 | 688--696 |
| Theorem \(4'\), existence in a closed homogeneous relation | 328 | developed through the expansion's solution framework, without transferred number | 119--124 | 700--710 |
| Theorem 5, no-solution/general-solution alternative | 328--329 | \S4 Theorem 3 | 121--124 | 728--739 |
| no same numbered announcement theorem | --- | \S4 Theorem 2, noncontinuous finite-memory conclusion | 120 | 696--698 |
| no transferred announcement number | --- | \S4 Theorem \(3'\), fixed anticipation bound | 124 | 739--744 |

The source-order and title boundary at `n-c-014.tex:487-497` makes this table's
authority explicit before any theorem is used.

### M23: modern finite-word theorem and Thomas paragraph

The shared theorem at `logic-in-computer-science.tex:811-825` labels its
regular/MSO sentence a *modern formulation*, then names the original sources'
different encodings and broader result packages.  The reader repeats the
boundary at `n-c-014.tex:812-827`.  Its Thomas paragraph
(`n-c-014.tex:829-847`) attributes the modern automaton/MSO proof architecture
to Thomas \S3.1 and expressly refuses to turn that survey into either Russian
source or the unreconciled Büchi article.  The exact Trakhtenbrot finite-word
bridge remains the source's automaton-enumerability/decidability and
special-beginning package on expansion pp. 127--131.  No compound theorem name
is used as evidence for a statement absent from announcement pp. 326--329.

### M24--M25: all frozen records

The records reconcile without a source-strength conflict:

- `n-c-014.tex:487-827` contains the reader reconstruction and bounded
  translation disclaimer.
- `p09-trakhtenbrot-1961-source-note.md:5-18,20-105` fixes authority, custody,
  titles, access, rights, and translation limits; lines 107--500 give the
  matching mathematical/source record; lines 502--536 state the integration
  and still-separate review gate.
- `p09-source-presentations-lot2-3.md:646-658` gives the same compact identity,
  counterexample, empty-set split, theorem strengths, finite-word repair, and
  pending-review status.  Its consolidated status at lines 911 and 913 says
  only that the two bodies are source-sufficient and separately reconstructed;
  it does not claim prior admission.
- `logic-in-computer-science.tex:811-825,2341-2347` keeps the modern theorem and
  source-navigation roles separate.
- `handbook.bib:5991-6013` contains two distinct entries with the correct
  journals, volumes, issues, years, pages, official English title forms, and
  Math-Net routes.

The page locators in the reader are exact: announcement pp. 326--327 for the
system/normal form; expansion pp. 103--109 for its full proof; expansion
pp. 109--113 for operators; announcement pp. 326--328 and expansion
pp. 113--119 for portions/definability; announcement pp. 328--329 and expansion
pp. 119--124 for finite realization/general solutions; and expansion
pp. 124--131 for explicit synthesis and finite words.  The formula displays,
theorem numbers, Л/\(A\) letter distinction, Putnam/Church/Büchi/Elgot/Robinson
reports, and handbook-owned corrections all occur under the controlling page
ranges.  I found no locator, formula, citation, title, attribution, or
translation-strength defect.

## M26: AGENTS terminology audit

The new technical names used by the reconstruction satisfy the repository rule
at first substantive use:

- \(\mathcal I\) is necessary to render Cyrillic И, is defined by its exact
  syntax/interpretation and standing, is distinguished from an automaton and
  Büchi's weak system, and is used throughout (`n-c-014.tex:499-510`).
- fictitious occurrence and lower/upper \(t\)-formulae receive semantic,
  eliminable definitions, their prefix/tail difference, and immediate normal-
  form use (`n-c-014.tex:512-523`).
- operator, anticipation, finite memory, weight, finite operator, and the
  normalized Л/\(A\) class each receive typed definitions, distinct standings,
  explicit nonredundancy, and later theorem use (`n-c-014.tex:527-571`).
- portion, homogeneous degree, basis, internal transition, and closedness are
  defined as stream-set properties/data and distinguished from automaton kinds
  before the definability theorems (`n-c-014.tex:582-600`).
- conditional \(\mathcal I\)-algorithm is defined by its truth-oracle
  dependency and immediately used to state the effectiveness boundary
  (`n-c-014.tex:679-686`).
- solution and exact graph definition are contrasted before Theorem \(4'\),
  and general \(A\)-solution/general zero-anticipation solution are defined by
  both completeness and soundness clauses before use (`n-c-014.tex:700-726`).
- explicit definition, the typed residual maps \(T_t\), automaton-enumerable,
  automaton-decidable, \(\mathcal I'\), and special beginning all receive exact
  standing and definitions before their result is stated
  (`n-c-014.tex:748-810`).

The source's “covering operator” is not a hypothetical new primitive: the text
uses it only for the already printed construction on expansion p. 116, states
its nonempty permitted-extension behavior and image property at
`n-c-014.tex:664-670`, and immediately uses it in the converse proof.  No
definition-after-use, redundant invented name, standing ambiguity, or unused
distinction remains.

## M27--M28: adversarial compression, scope, and publication boundary

- **No hidden continuity:** `n-c-014.tex:688-698` confines bounded anticipation
  to the continuous theorem and states the noncontinuous theorem only as finite
  memory.
- **No hidden closedness:** closedness is defined at line 600 and required in
  both converse definability and general-solution results.  Open relations are
  separately qualified at lines 709--710.
- **No operator-class collapse:** whole-future memory, bounded anticipation,
  finite operator, and the zero-anticipation automaton class are separated at
  lines 527--571 and exercised by the counterexample.
- **No source laundering or translation inflation:** lines 487--497 preserve
  the two source bodies and title forms; lines 812--847 preserve the modern and
  neighboring-source boundary; line 827 denies a line-by-line translation
  claim.  Both handbook corrections are labelled handbook-owned.
- **No priority inflation:** source-time Church, Putnam, Büchi, Elgot, and
  Robinson remarks are reported as historical qualifications, not independently
  adjudicated priority (`n-c-014.tex:679-686,817-819`;
  `p09-trakhtenbrot-1961-source-note.md:482-500`).
- **No premature completion:** the source note and compact record call the
  bodies complete while keeping reconstruction review/admission separate
  (`p09-trakhtenbrot-1961-source-note.md:14-18,525-536`;
  `p09-source-presentations-lot2-3.md:658,911-913`).
- **Rights and topic scope remain bounded:** the local scans remain
  nonredistributable research objects under the recorded qualification, and
  this review concerns only `N-c-014.c` at the two stated source strengths.
- **No software evidence substituted:** no test/build/checker claim appears in
  the scholarly evidence, and none was used in this review.

## Mandatory coverage ledger

| Point | Disposition | Principal evidence |
|---|---|---|
| M01 | checked-clean | seven recomputed hash matches above |
| M02 | checked-clean | all 4 announcement and 29 expansion renders, original detail; full maps above |
| M03 | checked-clean | announcement pp. 326--329; expansion pp. 103--131; source note 20--77; bibliography 5991--6013 |
| M04 | checked-clean | explicit working-Russian/non-specialist disclosure and scan-controlled evidence above |
| M05 | checked-clean | `n-c-014.tex:499-510,801-810`; expansion pp. 104--105, 130--131 |
| M06 | checked-clean | `n-c-014.tex:512-525`; announcement pp. 326--327; expansion pp. 105--109 |
| M07 | checked-clean | `n-c-014.tex:527-571`; expansion pp. 109--111; announcement pp. 326--327 |
| M08 | checked-clean | `n-c-014.tex:551-580`; expansion pp. 111--112 |
| M09 | checked-clean | `n-c-014.tex:582-641`; announcement p. 327; expansion pp. 110, 114--115; full independent derivation above |
| M10 | checked-clean | `n-c-014.tex:643-646,679-681`; announcement p. 327; expansion pp. 116--118; independent residual derivation above |
| M11 | checked-clean | `n-c-014.tex:646-677`; announcement pp. 327--328; expansion pp. 116--119; independent topology and empty-set derivations above |
| M12 | checked-clean | `n-c-014.tex:679-686,734-739`; announcement pp. 326, 328--329; expansion pp. 119, 124 |
| M19 | checked-clean | `n-c-014.tex:748-761`; expansion pp. 124--127 |
| M20 | checked-clean | `n-c-014.tex:763-799`; expansion pp. 127--129; both directions and empty-language test above |
| M21 | checked-clean | `n-c-014.tex:801-810`; expansion pp. 130--131 |
| M22 | checked-clean | comparison table above; announcement pp. 326--329; expansion pp. 103--131 |
| M23 | checked-clean | `logic-in-computer-science.tex:811-825`; `n-c-014.tex:812-847`; expansion pp. 127--131 |
| M24 | checked-clean | reader 487--827; source note 5--536; compact record 646--658, 911--913; shared theorem 811--825; bibliography 5991--6013 |
| M25 | checked-clean | claim-by-claim page and line audit above; no defective locator/formula/citation/attribution found |
| M26 | checked-clean | complete terminology audit above; no rule violation found |
| M27 | checked-clean | adversarial audit above; no false compression, hidden hypothesis, collapse, laundering, or inflated status found |
| M28 | checked-clean | topic-only and rights boundaries preserved; no test, build, script, checker, or handbook-PDF evidence used |

No mandatory point in this seat's mandate remains not checked.

VERDICT: ACCEPT

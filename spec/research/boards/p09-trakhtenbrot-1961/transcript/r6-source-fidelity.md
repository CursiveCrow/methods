# Round 6 source-fidelity, language, and evidence review

## Result and review boundary

I found no blocker, must-fix, or lesser publication finding within this seat's
mandate.  The Round 6 reader is faithful to the distinct strengths of the 1961
announcement and 1962 expansion, and its three handbook-owned corrections are
both mathematically necessary and publicly attributed where they are used: the
residual-operator/portion correction, the nonempty/empty covering split, and the
nonempty finite-word converse.

This was a fresh blind review.  I did not read an earlier-round report, another
Round 6 report, the board ledger, the chair transcript, any Rabin draft or note,
or any conversation about another review, and I did not contact another
reviewer.  The only substantive evidence used was the seven frozen Round 6
objects and the original-detail renders of the four announcement pages and all
twenty-nine expansion pages identified by the charter.  I did not use either
text extraction as evidence.  I did not run a test, harness, automated checker,
repository script, TeX command, interim build, handbook-PDF inspection, or
build.  The only identity computation was the required SHA-256 hashing.

My Russian competence is working reading competence in technical mathematical
Russian: I can read the definitions, theorem statements, proof transitions,
qualifications, bibliographic matter, and mathematical typography in these two
bodies and compare them directly with a bounded English reconstruction.  I am
not a native Russian speaker, a credentialed translator, or a Russian-language
specialist, and this verdict is not specialist translation certification.  My
competence and the unusually formula-driven prose were sufficient for the
source-fidelity mandate.  The official English-title, access-route, later-
translation, and rights statements were checked as frozen record claims across
the source note, compact record, and bibliography; the charter's evidence limit
did not permit live revalidation of the linked Math-Net or AMS pages.  The
reader correctly makes no complete line-by-line translation claim
(`handbook/parts/p09/presentations/n-c-014.tex:880-886`).

## Frozen identities (M01)

All seven labels were recomputed before substantive review and match the
charter byte for byte.

| Frozen object | Recomputed SHA-256 | Disposition |
|---|---|---|
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1961.pdf` | `44213AEBE4DB2F1C389B812A7401138799C3DB4749C3605BA7211BBB4BAF96F9` | match |
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1962-expanded.pdf` | `EAB4438A7BBA2B6009374826A98A3A61FB6465C493F57B03D2C6C7385824096D` | match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `AC0FB697FD3EF5A3BB07EF99275E485DF80FA98D5D2395E58C72D47A0FFC35F9` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD` | match |
| `handbook/bib/handbook.bib` | `75AB70009DF4AB8B2180CFFC6987EA244ADB2F978B1D889C87009EFF17066D5C` | match |
| `spec/research/p09-trakhtenbrot-1961-source-note.md` | `97E02A86E1CF44A760037ECBC060E35C771E893B43BF82F9147E95CACCF8E213` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `E1F121FC0BA9D1FD0C60D0494FC159589D1E62ED11668205D1F5F36BFBA1E5E8` | match |

The PDF lengths also agree with the frozen custody record: 566,358 bytes for
the announcement and 1,884,181 bytes for the expansion
(`spec/research/p09-trakhtenbrot-1961-source-note.md:24-55`).

## Complete visual source inspection (M02-M04)

I inspected every render at original detail.  The physical-to-printed maps are
complete, sequential, and without a missing or duplicated page:

- announcement `rendered/page-1.jpg` through `page-4.jpg` map to printed
  pp. 326, 327, 328, and 329;
- expansion `expanded-rendered/page-01.jpg` through `page-29.jpg` map to
  printed pp. 103 through 131 by `printed page = 102 + physical page`.

The announcement's first page prints *Doklady Akademii Nauk SSSR*, 1961,
volume 140, number 2, the Russian title
"Конечные автоматы и логика одноместных предикатов," the author, and printed
p. 326.  Its last page is p. 329, records receipt on 29 April 1961, and the
first page records presentation by P. S. Novikov on 16 May 1961.  The expansion
begins on p. 103 under *Sibirskii Matematicheskii Zhurnal*, volume III, number
1, January-February 1962, with the same Russian title, ends on p. 131, and
records receipt on 15 May 1961.  These facts agree with the source-note identity
record (`spec/research/p09-trakhtenbrot-1961-source-note.md:24-71`), the compact
record (`spec/research/p09-source-presentations-lot2-3.md:646-648`), and the two
separate bibliography entries (`handbook/bib/handbook.bib:5991-6013`).

The frozen records consistently preserve the Math-Net English renderings
"Single-Place Predicates" for 1961 and "One-Place Predicates" for 1962, the
two Math-Net routes, and the later AMS-translation/body-not-acquired boundary.
The reader abbreviates only the differing title words while preserving the
distinction (`handbook/parts/p09/presentations/n-c-014.tex:487-497`).  The
source order is honest: 1961 is the registered four-page announcement; 1962 is
the complete twenty-nine-page expansion.  No theorem number, proof, example,
or page locator is transferred silently between them.

The rights paragraph is appropriately narrow
(`spec/research/p09-trakhtenbrot-1961-source-note.md:73-79`; compact record
line 648): public archival access is not described as an open licence; the
personal-use exception is limited to individual teachers, students, and
researchers printing copies for noncommercial teaching or research; other
reproduction/republication is said to require permission; and the local PDFs
are identified as nonredistributable research objects.  Nothing in the reader
or records infers electronic-copy or redistribution permission.

## Independent technical and source-strength audit

### Primitive grammar, dependence classes, and normal form (M05-M06)

The reconstruction at `handbook/parts/p09/presentations/n-c-014.tex:499-548`
matches expanded pp. 104-109 and announcement pp. 326-327.

1. Expanded pp. 104-105 make И an interpreted formal language: individuals
   range over (1,2,\ldots), predicate variables range over arbitrary monadic
   predicates, and prime is immediate successor.  Page 105 prints atoms such as
   (X(t),Y(\tau'),Z(\sigma''')) and formation by Boolean operations plus
   individual and predicate quantifiers.  The reader's generic recursion
   (t^{(0)}=t, t^{(k+1)}=(t^{(k)})') and atom (X(t^{(k)})) is exactly this
   grammar, not a stronger term language.  Equality, order, bounded individual
   quantifiers, constants, and variable-plus-fixed-numeral terms are then
   correctly identified as eliminable conveniences.  The standing of
   (\mathcal I) is explicit and is not conflated with an automaton, theorem,
   set, or Büchi's weak finite-set interpretation.
2. Expanded pp. 105-106 define fictitious occurrence outside an interval by
   invariance under changes outside the interval.  Reader lines 521-524
   preserve this semantic definition rather than replacing it by absence of a
   written occurrence.
3. On expanded p. 106, (t)-controlled from above means that every individual
   quantifier is bounded above, with range (\sigma<\mu) or
   (\lambda<\sigma<\mu); controlled from below has range
   (\lambda<\sigma) or (\lambda<\sigma<\mu).  On p. 108, an upper
   (t)-formula is selected from the controlled-from-below class, permits in
   atoms only a variable or a variable plus a numeral (not a bare constant),
   and uses (t<\sigma) or (t<\sigma<\mu).  The lower class is the exact
   dual, with (\sigma<t) or (\lambda<\sigma<t).  Reader lines 525-536
   reproduce all four syntactic restrictions without swapping "upper" and
   "lower."
4. The source separately derives tail dependence for upper formulae and
   bounded-prefix dependence through (t+s) for lower formulae.  Reader lines
   537-540 correctly state these as consequences, not definitions.
5. Announcement Theorem 1 on p. 327 and the unnumbered expanded normal-form
   theorem on pp. 108-109 give an effective Boolean combination of lower and
   upper formulae.  The reported proof sequence is complete at its claimed
   level: predicate prenexing; inward movement of individual quantifiers;
   splitting bounded ranges at (t); and distribution of the remaining
   predicate quantifier across prefix- and tail-independent factors.  The
   manuscript does not import a modern automata normal form as a substitute.

The source note gives the same exact grammar and proof architecture at lines
109-161, and the compact record preserves the primitive/syntactic distinction
at line 650.

### Operators, memory, weight, and the negative boundary (M07-M08)

Reader lines 550-603 agree with expanded pp. 109-113 and the announcement's
canonical equations on pp. 326-327.

- The operator is a total typed map between stream spaces.  Anticipation (p)
  is an at-most-(p) future-dependence bound; at (p=0), it is equivalent to
  extension-independent, prefix-compatible finite-word maps.
- The finite-memory equations correctly pass the *whole suffix* to both output
  and state update.  They do not silently make the state after a prefix a
  prefix-determined state.  Weight is the least finite state-set cardinality.
- A finite operator adds bounded anticipation and therefore has finite-window
  equations.  A finite-memory operator need not have bounded anticipation, and
  zero anticipation alone need not give finite memory or effectiveness.
- The announcement's Cyrillic Л and the expansion's Latin (A) are kept
  distinct at their respective source locations, and the reader expressly
  declares its normalized use of (A) in combined prose
  (`handbook/parts/p09/presentations/n-c-014.tex:586-594`).
- Expanded p. 111 gives the one-state finite-memory operator whose output asks
  whether a (1) occurs strictly later in the input.  The answer may require
  unbounded future information and is not an effective stream computation.
  Expanded p. 112 then reduces primitive-recursive recognition and synthesis
  to undecidable periodicity/zero questions.  Reader lines 575-577 and 596-603
  retain both negative boundaries.  "Periodic" is honestly rendered as
  "ultimately periodic" after the source's explicit preperiod-plus-period
  convention.

The same distinctions and exact suffix equations occur in the source note at
lines 163-219 and in compact-record line 652.

### Portions, typed residuals, and the weight-two counterexample (M09)

The announcement on p. 327 expressly permits an empty portion.  Expanded
p. 114 introduces a portion only after a nonempty prefix intersection.  Reader
lines 605-629 state both conventions, choose the announcement's all-prefix
convention publicly, and type a many-coordinate portion by one equal length
(r), coordinate prefixes (u_i\in A_i^r), coordinatewise concatenation, and
the product stream space.  This removes the possible interleaving ambiguity.
Homogeneous degree, basis, and internal transition retain stream-set/data
standing; they are not presented as automaton kinds.

The residual equations at reader lines 631-657 type-check independently.  For
(u\in A^r), zero anticipation makes the output prefix (v_u\in B^r)
independent of the extension (Z).  With
(\operatorname{tail}_r(Y)(t)=Y(t+r)) and
(T_u(Z)=\operatorname{tail}_r(T(uZ))), direct expansion of the tuple-portion
definition gives

\[
 (G_T)_{(u,v)}=
 \begin{cases}
  G_{T_u},&v=v_u,\\
  \varnothing,&v\ne v_u.
 \end{cases}
\]

Thus (T_u) is a stream operator, not a state in an arbitrary whole-future
memory presentation.  The reader identifies this notation and distinction as
handbook-owned at lines 654-657 and again identifies the resulting correction
as handbook-owned at lines 689-695.

I independently checked every step of the counterexample at reader lines
659-695, against the source's whole-future equations on expanded p. 110 and
the printed graph-degree claim on p. 115.

1. For
   \[
   T(X)(t)=\begin{cases}X(t),&X(1)=1,\\0,&X(1)=0,
   \end{cases}
   \]
   the first (t) output values depend only on (X(1),\ldots,X(t)), so
   anticipation is zero.
2. The displayed two-state presentation is valid.  With (q(1)=0) and suffix
   (z=(z_0,z_1,\ldots)), induction in
   (q(t+1)=q(t)\mathbin{\mathsf{xor}}X(t)\mathbin{\mathsf{xor}}X(t+1))
   yields (q(t)=X(1)\mathbin{\mathsf{xor}}X(t)).  Therefore
   ((1-q(t))X(t)) equals (X(t)) when (X(1)=1) and (0) when
   (X(1)=0).
3. A one-state presentation would have one suffix functional (F) at every
   time.  At time one, (T(Z)(1)=Z(1)) for every stream (Z), forcing
   (F(z)=z_0) for every suffix.  At time two on any input beginning (01),
   the current suffix begins with (1), so (F=1), while the required output
   is (0).  Hence the weight is exactly two.
4. The rank-zero portion is (G_T).  The consistent paired one-letter prefix
   ((0,0)) yields the constant-zero graph; ((1,1)) yields the identity
   graph.  They are mutually distinct and nonempty.  An inconsistent paired
   prefix such as ((0,1)) yields (\varnothing).  All later consistent
   portions are again constant-zero or identity.  Hence there are exactly
   three nonempty portions and exactly four all-prefix portions.
5. Weight two therefore bounds neither convention by (k), and the four
   all-prefix portions also refute the former (k+1) repair.  The only exact
   general count is by distinct residual maps (T_u), plus the empty portion
   under the all-prefix convention when an inconsistent paired prefix exists.

Expanded p. 115 still correctly supplies closedness.  The counterexample does
not disturb that separate conclusion.  The singleton/ultimate-periodicity and
uncountably-many-homogeneous-nondefinable examples reported at reader lines
696-698 match expanded pp. 115 and 118.

### Homogeneity, recurrence, and the empty case (M10-M12)

Announcement pp. 327-328 and expanded pp. 116-119 support reader lines
700-745.

For the forward direction, the normal form leaves only finitely many Boolean
functions of each fixed lower window and finitely many shifted upper residuals.
After a prefix is fixed, substituting its letters and resetting the free time
variable therefore produces only finitely many distinct residual formulae.
Appending one input column maps one residual formula to another.  This proves
homogeneity and gives the internal transition effectively, as expanded
Theorem 1 states on pp. 116-118.

For the converse, a finite homogeneous basis supplies one-hot bound state
predicates; a bound choice predicate selects an allowed next letter; and the
current/next quantifier-free matrix updates the basis member.  The literal
initial values in reader lines 707-720 select the original set rather than an
unspecified union.  For a nonempty set, the source's total covering operator
has exactly the closure as its image; closedness then gives the set itself.

The printed lemma on expanded p. 116 cannot cover the empty set: a total
operator on the nonempty stream domain has a nonempty image.  The reader
therefore correctly restricts that construction to a nonempty homogeneous set
and defines the empty set separately by conjoining
(q_1(1)=1) with (q_1(1)=0) in the same recurrent syntax.  The restriction
and case split are expressly handbook-owned at the public use point
(`handbook/parts/p09/presentations/n-c-014.tex:721-730`), in the source note
(`spec/research/p09-trakhtenbrot-1961-source-note.md:325-334`), and in the
compact record (line 652).  The correction preserves, rather than strengthens,
the closed-homogeneous converse.

The least-class characterization by closed homogeneous sets, complement,
finite union, and predicate projection matches announcement p. 328 and expanded
p. 118.  The open Borel/projective question remains open in the reader.  The
effectiveness boundary is also exact: the internal residual transition is
unconditional; choosing an external output requires truth/nonemptiness tests;
the source's conditional (\mathcal I)-algorithm language is preserved; and
Putnam is used only for the stated existential-predicate recurrent fragment on
expanded p. 119.

### Remaining finite-realization and solution claims (whole-snapshot check)

Although M13-M18 are not mandatory points for this seat, I checked their source
strength because the assigned object is a whole-snapshot reconstruction.

- **M13 checked-clean.** Reader lines 747-755 match announcement Theorem 4 on
  p. 328 and expanded Section 4, Theorem 1, pp. 119-120.  Compact uniform
  continuity on the finitely many nonempty graph portions supplies one finite
  anticipation bound; the finite portion basis supplies memory, with weight at
  most the homogeneity degree.
- **M14 checked-clean.** Reader lines 755-757 match expanded Theorem 2 on
  p. 120: after continuity is removed, the conclusion is only finite memory.
  No bounded anticipation or finite-operator conclusion is imported.
- **M15 checked-clean.** Reader lines 759-769 distinguish exact graph
  definition from graph containment/solution, as expanded p. 119 does.
  Announcement Theorem (4'), p. 328, is correctly stated for a closed
  homogeneous relation, with the continuous and zero-anticipation branches and
  their weight bound; the open-relation analogue is separately reported without
  that bound.
- **M16 checked-clean.** Reader lines 771-785 reproduce both quantifiers in
  the general-solution definition printed on announcement p. 328 and expanded
  pp. 120-121: every solution of the named class is obtained by a parameter
  substitution, and every substitution from that class is sound.  Parameter
  streams and the output remain operators, not propositions or states.
- **M17 checked-clean.** Reader lines 787-798 match announcement Theorem 5,
  pp. 328-329, and expanded Theorem 3, pp. 121-124.  Iterative deletion removes
  empty/nonextendible portions.  Deletion of the initial portion proves the
  no-solution branch.  A surviving stable family lets parameter bits select
  allowed outputs, the finite family supplies memory, and closedness upgrades
  compatible prefixes to membership.  This yields all and only
  zero-anticipation solutions with the source's weight bound, subject to the
  stated emptiness-decision condition.
- **M18 checked-clean.** Reader lines 798-803 match expanded Theorem (3') on
  p. 124.  The result is separately quantified for each fixed anticipation
  bound (p); it is not an unbounded-lookahead general solution.

### Explicit synthesis and finite words (M19-M21)

Reader lines 807-869 match expanded pp. 124-131.

- **M19.** The explicit definition
  (Y(t)\leftrightarrow\varphi(X_1,\ldots,X_m;t)), the finite-memory
  conclusion, semantic at-most-(p) anticipation criterion, zero-anticipation
  criterion, shifted-formula iteration, finite termination, and canonical
  output/transition equations are all stated at their Section 5 strength.  The
  pp. 126-127 example really produces the two displayed residual formulae and
  the two tables; the reader neither turns it into a general proof nor omits its
  proof role.
- **M20.** Zero anticipation makes (T_t:A^t\to B^t) independent of the
  chosen infinite extension and makes the family prefix compatible.  The
  source's automaton-enumerable language is the lengthwise range family; its
  automaton-decidable language uses the recognizer's output at the terminal
  position.  In the forward direction on pp. 127-128, existentially choosing an
  input prefix whose output equals the presented word gives a terminal
  recognizer.  In the converse, the source keeps an accepted word, or extends
  the longest accepted prefix by the first accepted continuation; if there is
  no accepted prefix it asks for the first accepted word of the current length.
  Prefix closure and proper extendibility make the first two branches coherent,
  but do not seed the last branch for the empty language.  The constant-zero
  recognizer decides the empty language, while a total length-preserving
  operator has nonempty range at every positive length.  The reader's added
  (L\ne\varnothing) is therefore necessary and sufficient and is explicitly
  handbook-owned at lines 849-858.
- **M21.** Expanded pp. 130-131 define (\mathcal I') by eventually-zero
  predicate quantification.  A special beginning ends at a position after
  which that predicate is zero forever; it is not any arbitrary prefix.
  Section 5, Theorem 3, gives existence for an arbitrary (\mathcal I)-formula
  but effective construction for an (\mathcal I')-formula and explicitly
  attributes the latter to Büchi.  Reader lines 860-869 preserve every one of
  those restrictions.

## Cross-object, terminology, and publication audit (M22-M28)

- **M22 checked-clean.** Announcement Theorems 1-5 and (4') were compared
  directly on pp. 327-329 with expanded Sections 1-5 on pp. 104-131.  The
  reader uses announcement numbering only for announcement claims and uses
  expanded section/theorem locators for the expansion.  It does not move the
  expansion's Theorem 2 (finite memory without continuity), Theorem (3')
  (fixed lookahead), explicit synthesis, word theorems, or (\mathcal I') into
  the announcement.  It also does not attribute the expansion's Latin (A)
  notation to 1961.
- **M23 checked-clean.** The shared theorem at
  `handbook/parts/p09/logic-in-computer-science.tex:811-825` labels its
  regular/MSO sentence a modern formulation and states that the original
  sources have different encodings and result packages.  Reader lines 871-906
  preserve Trakhtenbrot's broader package and separate Büchi, Elgot, Thomas,
  and Trakhtenbrot.  The source-navigation paragraph at
  `handbook/parts/p09/logic-in-computer-science.tex:2341-2347` likewise lists
  the announcement plus complete expansion and routes infinite-tree logic
  separately.  Thomas is used as a later proof locator, not laundered into
  either Russian source.
- **M24 checked-clean.** Every Trakhtenbrot reader claim was reconciled with
  `spec/research/p09-trakhtenbrot-1961-source-note.md:81-570`, compact-record
  lines 646-658, shared-theorem lines 811-825, bibliography lines 5991-6013,
  and the compact record's consolidated status at lines 911-913.  The records
  agree that both bodies are sufficient, the strengths and English titles are
  distinct, specialist-language review is not claimed, and independent
  admission remains pending.  "Body sufficient" is not promoted to proof,
  build, visual handbook inspection, human review, or final admission.
- **M25 checked-clean.** The announcement locators pp. 326-329, expansion
  locators pp. 103-131, theorem numbers, displayed equations, historical
  references to Church, Büchi, Elgot, Putnam, and Robinson, and every
  translation/source-strength qualifier used by this reconstruction agree with
  the printed pages.  The correction below announcement p. 329 belongs to the
  earlier cited paper and is not misapplied to this article.  The source's
  historical/priority remarks are reported as historical claims, not newly
  adjudicated priority.
- **M26 checked-clean.** Each technical term is defined before use with its
  standing: (\mathcal I) and (\mathcal I') are interpreted formal
  languages; controlled/lower/upper terms are formula classes; anticipation,
  finite memory, finite operator, weight, and (A)-operator are operator
  properties/classes; portion, homogeneity, basis, and internal transition are
  stream-set properties/data; (T_u) is a stream operator; and general
  solution is a two-clause parameterization property.  The new residual
  notation is necessary to separate induced suffix operators from broad memory
  states, is exactly defined at first use, is marked handbook-owned, and is
  used in the repaired portion statement.  I found no definition-after-use,
  redundant technical name, standing ambiguity, or unused distinction under
  the repository terminology rule.
- **M27 checked-clean.** Adversarial rereading found no hidden continuity or
  closedness assumption, no finite-memory/finite-operator collapse, no
  graph/solution collapse, no fixed/unbounded-anticipation collapse, no silent
  empty-set assumption, no source or translation laundering, no inflated
  priority claim, and no misleading completion language.  The one false
  printed source bound is identified rather than defended; all three
  handbook-owned edge-case/exactification moves are public where used.
- **M28 checked-clean.** The acceptance claim is confined to N-c-014.c at the
  distinct 1961/1962 strengths.  It does not admit literal Büchi 1960
  reconciliation, the whole N-c-014 entry, Part IX, Rabin, rendered handbook
  pages, final-book completion, human review, or user acceptance.  The rights
  boundary is explicit, and no prohibited software-style evidence was used or
  claimed.

## Mandatory coverage disposition

| Point | Status | Controlling evidence |
|---|---|---|
| M01 | checked-clean | recomputed seven identity labels; table above |
| M02 | checked-clean | all 4 announcement renders = pp. 326-329; all 29 expansion renders = pp. 103-131 |
| M03 | checked-clean within the frozen-record evidence boundary | printed pp. 326, 329, 103, 131; source note 24-79; bibliography 5991-6013; compact record 648 |
| M04 | checked-clean | competence and evidence disclosure above; reader 880-886; source note 14-20, 103-107 |
| M05 | checked-clean | reader 499-519, 860-869; expanded pp. 104-105, 130-131 |
| M06 | checked-clean | reader 521-548; announcement pp. 326-327; expanded pp. 105-109 |
| M07 | checked-clean | reader 550-594; announcement pp. 326-328; expanded pp. 109-112 |
| M08 | checked-clean | reader 575-577, 596-603; expanded pp. 111-113 |
| M09 | checked-clean | reader 605-698; announcement p. 327; expanded pp. 113-116; independent derivation above |
| M10 | checked-clean | reader 700-703, 738-745; announcement p. 327; expanded pp. 116-118 |
| M11 | checked-clean | reader 700-736; announcement pp. 327-328; expanded pp. 116-119; independent empty-case derivation above |
| M12 | checked-clean | reader 738-745, 793-798; announcement pp. 326, 328-329; expanded pp. 117, 119, 124 |
| M19 | checked-clean | reader 807-820; expanded pp. 124-127 |
| M20 | checked-clean | reader 822-858; expanded pp. 127-129; independent empty-language check above |
| M21 | checked-clean | reader 860-869; expanded pp. 130-131 |
| M22 | checked-clean | reader 487-886; announcement pp. 326-329; expansion pp. 103-131 |
| M23 | checked-clean | reader 871-906; shared theorem 811-825; navigation 2341-2347 |
| M24 | checked-clean | source note 81-570; compact record 646-658, 911-913; bibliography 5991-6013 |
| M25 | checked-clean | every reader locator in 487-906 against all 33 controlling pages |
| M26 | checked-clean | reader first-use definitions 499-545, 550-594, 605-657, 700-785, 807-869 |
| M27 | checked-clean | whole reader 487-906; source note 81-544; compact record 646-658 |
| M28 | checked-clean | source note 73-79, 572-583; compact record 658, 911-913; no prohibited operation performed |

VERDICT: ACCEPT

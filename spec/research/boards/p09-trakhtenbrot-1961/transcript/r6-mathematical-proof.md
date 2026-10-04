# Round 6 mathematical and proof-correctness review: Trakhtenbrot N-c-014.c

## Disposition

No blocker or must-fix finding remains within the mathematical and
proof-correctness mandate.  The frozen manuscript distinguishes the primitive
syntax from its semantic dependence consequences; types the stream, tuple,
portion, and residual constructions; retracts the false printed weight bound;
and preserves the topological, general-solution, fixed-lookahead, explicit-
synthesis, and finite-word hypotheses at their exact strengths.

Blocking findings: none.

Must-fix findings: none.

## Frozen identity and evidence disclosure

I recomputed the seven SHA-256 labels before substantive review.  All seven
match the Round 6 charter exactly.

| Frozen object | Recomputed SHA-256 | Disposition |
|---|---|---|
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1961.pdf` | `44213AEBE4DB2F1C389B812A7401138799C3DB4749C3605BA7211BBB4BAF96F9` | match |
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1962-expanded.pdf` | `EAB4438A7BBA2B6009374826A98A3A61FB6465C493F57B03D2C6C7385824096D` | match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `AC0FB697FD3EF5A3BB07EF99275E485DF80FA98D5D2395E58C72D47A0FFC35F9` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD` | match |
| `handbook/bib/handbook.bib` | `75AB70009DF4AB8B2180CFFC6987EA244ADB2F978B1D889C87009EFF17066D5C` | match |
| `spec/research/p09-trakhtenbrot-1961-source-note.md` | `97E02A86E1CF44A760037ECBC060E35C771E893B43BF82F9147E95CACCF8E213` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `E1F121FC0BA9D1FD0C60D0494FC159589D1E62ED11668205D1F5F36BFBA1E5E8` | match |

I visually inspected every source page from the original-detail rendered
images.  Announcement `rendered/page-1.jpg` through `page-4.jpg` map in order
to printed pp. 326--329.  Expansion `expanded-rendered/page-01.jpg` through
`page-29.jpg` map in order to printed pp. 103--131: physical page 1 is the
unnumbered opening page 103, physical pages 2--29 visibly continue as printed
pp. 104--131.  Formulae, accents, inequality directions, theorem numbers,
section transitions, footnotes, and the displayed tables on pp. 126--127 were
read from those images, not from either noncontrolling text extraction.

My source-language competence is limited but sufficient for this mathematical
seat: I can visually follow the Russian mathematical exposition, theorem and
definition headings, common technical terms, symbols, displayed formulae, and
cross-references, and I compared those directly with the bounded reconstruction
in the frozen source note.  I do not claim human Russian-specialist credentials
or certify nuanced literary translation.  The proof verdict below rests on my
independent mathematical derivations from the printed formulae and proof
architecture, not on a claim of specialist linguistic certification.

I read no earlier-round report, ledger, chair transcript, other Round 6 report,
or separate Rabin draft or note, and contacted no other reviewer.  One direct
line-range display of the frozen `n-c-014.tex` object extended from the end of
the Trakhtenbrot block at line 907 through the adjacent Rabin heading and lines
908--930.  Those adjacent frozen lines were not used as evidence, and I did not
inspect further Rabin text or any separate Rabin object.  I ran no test, test
harness, automated checker, repository script, TeX command, interim build,
handbook-PDF inspection, or build.  The only computation was the seven required
identity hashes.

## 1. Primitive grammar and normal form (M05--M06)

### Grammar, interpretation, and eliminable conveniences

Expanded pp. 104--105 print the language and interpretation.  The manuscript
reconstructs them at `n-c-014.tex` lines 499--519.  Its grammar is exact:

1. Individual variables range over \(\mathbb N_+=\{1,2,\ldots\}\), predicate
   variables over all subsets of that domain, and immediate successor is the
   primitive individual operation.
2. Iteration is defined, rather than presumed:
   \(t^{(0)}=t\) and \(t^{(k+1)}=(t^{(k)})'\).
3. Primitive atoms are precisely \(X(t^{(k)})\).  Boolean operations,
   individual quantifiers, and monadic-predicate quantifiers close the formula
   grammar.
4. Equality, order, bounded individual quantifiers, numerals, and \(t+k\) are
   derived notation.  Their eliminability is mathematically sound.  For
   example, unrestricted predicate quantification defines equality by
   \(t=\tau\iff(\forall X)(X(t)\leftrightarrow X(\tau))\); reachability along
   successor defines \(t\leq\tau\) by closure under successor; \(1\) is the
   unique element with no predecessor; fixed numerals and \(t+k\) are iterated
   successors; and bounded quantifiers expand using the derived order.

Thus \(\mathcal I\) has formal-language standing, not automaton, set, theorem,
or metalinguistic standing.  The weak \(\mathcal I'\) changes only the range of
predicate variables to eventually-zero predicates; it is introduced later at
expanded p. 130 and manuscript lines 860--869.  No primitive from one system is
silently imported into the other.

### Exact syntactic classes and separate semantic consequences

Expanded pp. 105--108 control these definitions; announcement pp. 326--327
control the compressed terminology and Theorem 1.  Manuscript lines 521--548
correctly separate all of the following.

- Fictitious occurrence outside an interval is semantic invariance under
  changes to a free predicate off that interval.
- A formula is \(t\)-controlled from above when every individual-quantifier
  range is \(\sigma<\mu\) or \(\lambda<\sigma<\mu\), and controlled from below
  when every range is \(\lambda<\sigma\) or
  \(\lambda<\sigma<\mu\).
- An upper \(t\)-formula is controlled from below, has only variable or
  variable-plus-numeral atomic arguments (no bare numeral argument), and has
  ranges \(t<\sigma\) or \(t<\sigma<\mu\).
- A lower \(t\)-formula is the controlled-from-above dual with the same atomic
  restriction and ranges \(\sigma<t\) or \(\lambda<\sigma<t\).

These are syntactic definitions.  The tail dependence of an upper formula and
the bounded-prefix dependence of a lower formula are proved consequences: an
upper formula is independent off \([t,\infty)\), while a lower formula of shift
\(s\) is independent off \([1,t+s]\).  The manuscript does not replace the
printed grammar by those semantic consequences.

### Normal-form derivation

Announcement Theorem 1 is printed on p. 327; the expanded unnumbered theorem
and proof occupy pp. 108--109.  Manuscript lines 540--548 report the complete
proof architecture at the right strength.  Independently:

1. Predicate quantifiers are brought before the individual-quantifier part;
   individual witnesses can be represented inside the monadic language, so
   this is an effective language transformation, not an illicit exchange of
   unlike quantifiers.
2. The individual quantifiers are pushed inward by the controlled-quantifier
   elimination described on pp. 106--108.
3. Each remaining range is split at the free variable \(t\), producing a
   lower prefix part and an upper tail part.
4. In the predicate-quantifier step on p. 109, the finite overlap values
   \(X(t),\ldots,X(t+s)\) are fixed.  Predicates witnessing the lower and upper
   sides can then be spliced because they agree on that overlap.  This proves
   both directions of the displayed distribution equivalence rather than
   assuming independence.
5. Repeating the step yields a Boolean function of finitely many lower and
   upper \(t\)-formulae, effectively.

This is the precise finiteness input used later; the manuscript does not
substitute a semantic automaton normal form for the source's syntactic theorem.

## 2. Operators, lookahead, memory, and the negative boundary (M07--M08)

Announcement pp. 326--327 and expanded pp. 109--113 control this material;
manuscript lines 550--603 give the reconstruction.

For finite nonempty alphabets, the operator type
\(T:A^{\mathbb N_+}\to B^{\mathbb N_+}\) is correct.  Anticipation \(p\) means
that input agreement through \(t+p\) forces output agreement at \(t\).  At
\(p=0\), this is equivalent in both directions to prefix preservation: output
on a word is independent of the chosen infinite extension, and compatible
under further extension.

The finite-memory equations at lines 561--574 correctly take the *whole*
future suffix:
\[
 b(t)=\Phi(q(t),a_{\ge t}),\qquad
 q(t+1)=\Psi(q(t),a_{\ge t}).
\]
The least cardinality of a finite \(Q\) is the weight.  Replacing the suffix by
one fixed window \(a(t),\ldots,a(t+p)\) adds bounded anticipation and yields a
finite operator.  Its \(p=0\) subclass is the announcement's Cyrillic
Л-class and the expansion's Latin \(A\)-class.  The manuscript explicitly
normalizes only the latter when combining the sources.  It therefore keeps
zero anticipation, finite memory, finite operator, and \(A\)-operator distinct.

The one-state example on expanded p. 111 verifies the strongest required
nonimplication.  Let
\[
 F(X)(t)=1\quad\Longleftrightarrow\quad
 (\exists s>t)\,X(s)=1.
\]
Take a singleton state, let \(\Phi\) test the tail after its first letter for a
one, and let \(\Psi\) return the sole state.  This is weight one under the
printed whole-suffix equations.  For every proposed \(p\), two inputs can agree
through \(t+p\) and differ by a later one, so no bounded anticipation exists;
the dependence is not an effective finite-input computation.  This validates
manuscript lines 574--577 and prevents a one-state memory presentation from
being mistaken for a one-state automaton.

Expanded pp. 111--112 also support the primitive-recursive negative boundary
at manuscript lines 596--603.  A constant operator produced by a
primitive-recursive scheme is an \(A\)-operator exactly when its output is
ultimately periodic, but periodicity is not decidable uniformly from such a
scheme.  The second construction produces a periodic constant output in every
case while making extraction of canonical equations decide an undecidable
zero-versus-eventually-one alternative.  Hence recognition and synthesis are
separate negative claims, and neither is promoted into a positive algorithm.

## 3. Portions, residual types, topology, and the weight-two refutation (M09)

Announcement p. 327 explicitly allows an empty portion.  Expanded pp. 113--115
first require a nonempty prefix intersection.  Manuscript lines 605--629 state
both conventions and adopt the announcement's all-prefix convention publicly.

The many-coordinate definition at lines 615--623 is correctly typed.  For
equal \(r\) and \(u_i\in A_i^r\), each coordinate is concatenated separately:
\[
 M_{(u_1,\ldots,u_n)}=
 \{(Z_1,\ldots,Z_n):(u_1Z_1,\ldots,u_nZ_n)\in M\}.
\]
No coordinate interleaving or unequal shift is hidden.  Homogeneous degree is
the number of distinct portions, a basis lists those stream sets, and the
internal transition appends one coordinate letter (or one letter tuple) and
selects the resulting basis member.  These have set/data standing, not
invented-automaton standing.

For a zero-anticipation \(T\), manuscript lines 631--657 correctly define the
common output prefix \(v_u\), the shift
\(\operatorname{tail}_r(Y)(t)=Y(t+r)\), and the residual stream operator
\(T_u(Z)=\operatorname{tail}_r(T(uZ))\).  Directly unfolding the tuple portion
gives
\[
 (G_T)_{(u,v)}=
 \begin{cases}
   G_{T_u},&v=v_u,\\
   \varnothing,&v\ne v_u.
 \end{cases}
\]
If \(v\ne v_u\), the fixed output prefix is inconsistent, so the portion is
empty.  If \(v=v_u\), deleting the common prefix leaves exactly
\((Z,T_u(Z))\).  This proves the equation with the advertised types and also
proves why \(T_u\) is an operator, not a broad memory state.

The printed p. 115 inference from broad weight to portion count is false.  The
handbook-owned counterexample at manuscript lines 659--695 withstands every
required check.  Put
\[
 T(X)(t)=\begin{cases}
 X(t),&X(1)=1,\\
 0,&X(1)=0.
 \end{cases}
\]

1. **Zero anticipation.**  Through time \(t\), the output uses only
   \(X(1),\ldots,X(t)\).
2. **Two-state whole-future presentation.**  With \(Q=\{0,1\}\), \(q(1)=0\),
   suffix \(z=(z_0,z_1,\ldots)\),
   \[
   \Phi(q,z)=(1-q)z_0,\qquad
   \Psi(q,z)=q\mathbin{\mathsf{xor}}z_0
                 \mathbin{\mathsf{xor}}z_1.
   \]
   Induction gives \(q(t)=X(1)\mathbin{\mathsf{xor}}X(t)\).  Substitution into
   \(\Phi\) gives \(X(t)\) when \(X(1)=1\) and zero when \(X(1)=0\).
3. **No one-state presentation.**  With one state, the same suffix functional
   \(\Phi(z)\) is used at every time.  At time one the required output forces
   \(\Phi(z)=z_0\) for every \(z\).  On an input beginning \(01\), the suffix
   at time two begins with one, so this forces output one, whereas \(T\)
   requires zero.  Thus the broad weight is exactly two.
4. **All nonempty portions.**  The empty input prefix gives \(G_T\).  Every
   nonempty input prefix beginning in zero has its unique consistent output
   prefix all zero and residual \(G_{C_0}\), the constant-zero graph.  Every
   prefix beginning in one has consistent output prefix equal to itself and
   residual \(G_{\mathrm{id}}\).  These three graphs are pairwise distinct,
   and no fourth consistent residual occurs.
5. **The empty portion.**  A paired prefix such as \((0,1)\) is inconsistent
   and gives \(\varnothing\).  All inconsistent paired prefixes give that same
   fourth portion.

The expansion's nonempty convention therefore counts exactly three portions,
contradicting its printed \(k=2\) claim.  The all-prefix convention counts
exactly four, contradicting the former \(k+1=3\) repair.  The valid statement
counts distinct residual operators \(T_u\), adding the empty portion only in
the all-prefix convention.  Broad future-dependent states cannot replace that
count.  Zero anticipation itself still makes \(G_T\) closed: a failure of the
graph equation has a first output discrepancy witnessed by a finite paired
prefix.  The reader therefore withdraws only the false numerical inference,
not source closedness.

The remaining examples at expanded p. 115 and manuscript lines 696--698 are
also sound.  Portions of a singleton are its successive tails (plus possibly
the one empty portion), so finiteness is equivalent to eventual repetition,
hence ultimate periodicity.  The source's tail-invariant families indexed by
an arbitrary irrational binary stream are one-homogeneous; quotienting the
continuum of streams by the countable eventual-shift relation still leaves
uncountably many such sets, whereas the formula set is countable.

## 4. Homogeneity, closed converse, recurrence, and effectiveness (M10--M12)

Announcement pp. 327--328 and expanded pp. 116--119 control these results;
manuscript lines 700--745 state them.

### Definability implies homogeneity

The claim does not rely on automata folklore.  Put a defining formula into the
source normal form.  After fixing a prefix, each lower component becomes one
of finitely many Boolean functions of its bounded overlap window, while the
upper components remain among a fixed finite formula stock.  Consequently only
finitely many residual formulae, hence only finitely many portions, can occur.
Canonicalizing the finite Boolean functions makes the process effective.
Appending the next letter repeats the same syntactic residual operation, so it
computes the internal transition map.  This independently verifies expanded
Theorem 1 and manuscript lines 700--703.

### Closed homogeneous converse and the empty-set edge

Let \(M\ne\varnothing\) be homogeneous with nonempty basis
\(M_1,\ldots,M_k\), beginning at \(M\).  At a basis member, choose a next input
letter whose successor portion is nonempty, using one choice bit \(U(t)\), and
update to that successor basis member.  Every generated finite prefix is
extendible in \(M\), so every generated stream lies in \(\overline M\).
Conversely, a point of \(\overline M\) supplies choices that follow each of its
letters.  Thus the source's total covering operator has image exactly
\(\overline M\).

Encoding its finite state by bound predicates \(q_1,\ldots,q_k\), its choice by
bound \(U\), its free output/input stream by \(X\), and fixing the literal
initial vector \((1,0,\ldots,0)\) yields exactly the recurrence displayed at
manuscript lines 706--729.  The current/next matrix is quantifier-free.  If
\(M\) is closed, image \(\overline M=M\), proving definability.

The source covering construction cannot cover \(M=\varnothing\): a total map
from the nonempty Cantor space has nonempty image.  The manuscript therefore
does not run the proof vacuously.  It defines the empty set in the same
recurrent form by conjoining \(q_1(1)=1\) and \(q_1(1)=0\).  Expanded p. 116
controls the nonempty covering argument; manuscript lines 721--729 and source-
note lines 325--334 expressly mark both the nonempty restriction and this
case split as handbook-owned.  The repair is sufficient and does not alter the
converse theorem.

Conversely, a recurrent formula of the displayed form defines a closed set:
the satisfying triples \((X,q,U)\) form a closed subset of a compact finite
product of Cantor spaces, and projection to \(X\) is compact, hence closed.
Only finitely many possible basis-state sets can remain after a prefix, so the
projection is homogeneous.  This supplies the proof compressed by expanded
p. 118 and validates manuscript line 729--730.

Boolean complement, finite union, and predicate projection generate every
\(\mathcal I\)-formula from the recurrent closed-homogeneous kernels, and each
operation is itself expressible in \(\mathcal I\).  This proves the least-class
characterization at manuscript lines 731--734.  It does not answer the
announcement's open question about the exact Borel/projective classes.

### Conditional and unconditional constructions

The internal residual transition is obtained syntactically and is
unconditional.  Selecting an external output/choice requires knowing whether
a candidate portion is nonempty, equivalently the truth of a closed
\(\mathcal I\)-sentence.  Expanded p. 119 therefore supports only the source's
conditional \(\mathcal I\)-algorithm in general.  Putnam's decision result is
used only for the existential-predicate/individual-universal recurrent form,
where the required nonemptiness sentences remain in that fragment.  Manuscript
lines 738--745 preserve exactly this boundary.

## 5. Finite realization and graph-versus-solution (M13--M15)

Announcement p. 328 and expanded pp. 119--120 control the finite-realization
claims; manuscript lines 747--769 state them.

Let a formula define exactly the graph of a continuous total operator.  Its
graph has a finite homogeneous basis by the preceding theorem.  Each nonempty
residual graph is compact.  Continuity of the first output coordinate on its
compact residual input domain gives a finite input-prefix length deciding that
coordinate.  There are only finitely many residual graphs, so the maximum of
those finitely many lengths is one uniform *relative* lookahead bound.  This
finite-basis step is essential: compact continuity of an arbitrary stream map
alone would not bound \(m(t)-t\) uniformly over all output coordinates.

Use the current residual graph as memory state.  The current residual and the
fixed input window determine the next output letter; appending the input/output
letter pair determines the next residual.  This gives canonical finite-window
equations, with at most one state per graph portion.  Hence the operator is
finite and its weight is at most the graph's homogeneous degree.  At
anticipation zero the result belongs to the announcement's Л-class and the
expansion's \(A\)-class.  This independently proves announcement Theorem 4 and
expanded Section 4, Theorem 1.

If continuity is removed, the same finite residual state still works, but the
current output may have to inspect the entire remaining input suffix to select
the unique compatible output tail.  That is precisely a broad finite-memory
presentation and supplies no finite lookahead.  The explicit formula
\(Y(t)\leftrightarrow(\exists s>t)X(s)\) is a definable total operator with
weight one and no bounded anticipation, so the weakening is strict.  This
verifies expanded Theorem 2 and manuscript lines 755--757.

For a relation \(R\) defined by \(\varphi(X,Y)\), a solution only requires
\(G_T\subseteq R\); defining the operator requires \(G_T=R\).  The manuscript
states that distinction before Theorem \(4'\).  Announcement Theorem \(4'\)
then correctly concerns a closed homogeneous relation: a continuous solution
can be replaced by a finite solution of weight at most the relation's degree;
a zero-anticipation solution can be replaced by a Л-solution with that bound.
The separate open-relation remark preserves the analogous existence statement
but drops the weight bound.  No graph theorem is silently substituted for this
selection theorem.

## 6. General solutions, stable deletion, and fixed lookahead (M16--M18)

Announcement pp. 328--329 and expanded pp. 120--124 control this material;
manuscript lines 771--805 reconstruct it.

For the named class \(\mathcal C\) of operators, the two quantifiers in a
general solution \(T(X,U)\) are:
\[
 \begin{aligned}
 &\forall T_0\in\mathcal C\,
   [T_0\text{ solves }\varphi\Rightarrow
    \exists S\in\mathcal C^m\ \forall X\,
    T_0(X)=T(X,S(X))],\\
 &\forall S\in\mathcal C^m\ \forall X\,
   \varphi(X,T(X,S(X))).
 \end{aligned}
\]
For a general \(A\)-solution, \(T\) and every parameter substitution \(S\)
have \(A\)-operator standing.  Replacing that class throughout by arbitrary
zero-anticipation operators gives the general zero-anticipation definition.
This verifies both completeness and soundness; existence of one solution would
verify neither.

For expanded Theorem 3, begin with the finite family of portions of the closed
definable relation.  Delete every empty portion.  Then repeatedly delete a
portion if some current input letter has no surviving output-letter successor.
The process terminates because the family is finite.

- If the initial portion is deleted, no zero-anticipation solution exists:
  the nonempty graph portions of any such solution would themselves form a
  surviving stable subsystem containing the initial portion.
- If the initial portion survives, each state and input letter has at least one
  surviving output.  A parameter bit chooses the output when both survive and
  is ignored when only one survives.  The surviving portion then supplies the
  next finite state.
- Every parameter substitution is sound because every generated paired prefix
  has a nonempty relation portion.  The resulting pair is in the closure of the
  relation, hence in the relation by closedness.
- Given any zero-anticipation solution \(T_0\), define the parameter at time
  \(t\) to select \(T_0(X)(t)\) at the current surviving state.  This produces a
  zero-anticipation parameter operator and recovers \(T_0\).  If \(T_0\) is an
  \(A\)-operator, the product of its finite controller with the surviving
  portion controller makes the parameter an \(A\)-operator as well.

Thus the surviving-family branch gives one bounded-weight general
Л/\(A\)-solution which is simultaneously general for all zero-anticipation
solutions; the other branch gives no solution.  Its state count is no larger
than the relation's homogeneous degree.  Testing emptiness during deletion is
exactly the conditional boundary already stated.  This independently proves
announcement Theorem 5 and expanded Theorem 3.

Expanded Theorem \(3'\) is fixed-\(p\), not unbounded.  For one chosen \(p\),
send an anticipation-at-most-\(p\) output \(Y\) to the zero-anticipation stream
\(\widetilde Y\) with
\(\widetilde Y(1)=\cdots=\widetilde Y(p)=0\) and
\(\widetilde Y(t+p)=Y(t)\).  Replace every occurrence \(Y(\xi)\) in the
relation formula by \(\widetilde Y(\xi+p)\) and conjoin the fixed initial zeros.
Theorem 3 applies to that shifted formula.  Shifting back yields the alternative
and generality only for operators and parameter substitutions with the same
fixed bound \(p\).  Repeating this argument for each \(p\) produces different
parametrizations; it does not produce one parametrization across unbounded
lookahead.  Manuscript lines 798--803 say exactly that.

## 7. Explicit definitions and finite-state synthesis (M19)

Expanded pp. 124--127 control Section 5's explicit-definition results;
manuscript lines 807--820 give their scope.

An explicit formula
\(Y(t)\leftrightarrow\varphi(X_1,\ldots,X_m;t)\) gives one output bit for every
input and time, so its graph is total and functional.  Expanded Section 4,
Theorem 2 therefore gives finite memory.  It has anticipation at most \(p\)
exactly when changing input predicates outside \([1,t+p]\) cannot change the
formula's truth, and it is an \(A\)-operator exactly when the interval is
\([1,t]\).  These are semantic criteria, not syntactic guesses.

For the source's zero-shift prefix-controlled formula, fixing the first input
column determines the first output and produces a shifted residual formula for
the remaining stream.  Repeat for each input column.  Normal form leaves only
finitely many possible residual formulae, so the process terminates; residual
identity supplies the state set, first-output values supply \(\Phi\), and the
shift step supplies \(\Psi\).  This is an unconditional construction for the
stated fragment.

The pp. 126--127 example is used exactly as an illustration of that second
algorithm.  It starts from one explicit formula \(\mathfrak A_1\), obtains a
second residual \(\mathfrak A_2\) for the indicated first-column case, obtains
no third formula on the next pass, and then prints the two rows of state/output
behavior as the \(\Phi\) and \(\Psi\) tables.  The manuscript claims neither
that those two formulae are universal nor that the example proves the general
termination theorem.

## 8. Positive-length words and the weak system (M20--M21)

Expanded pp. 127--131 control the finite-word boundary; manuscript lines
822--869 state it.

For a zero-anticipation stream operator and \(t\ge1\),
\[
 T_t:A^t\to B^t,
 \qquad T_t(u)=T(X)|_{1..t}
\]
is independent of the infinite extension \(X\) because any two extensions
agree through \(t\).  Applying the same argument at every \(s\le t\) proves
prefix compatibility.  Thus the finite-word maps are typed consequences of
the stream operator, not restrictions of its infinite-stream range.

An automaton-enumerable positive-length language has
\(L\cap B^t=T_t(A^t)\) at each length.  An automaton-decidable language has a
zero-anticipation finite-state recognizer whose output at the terminal position
is one exactly on its members.  Both directions of expanded Theorem 2 check as
follows.

1. Given an explicit enumerator formula \(\alpha(X;t)\), membership of a word
   \(Y|_{1..t}\) in the length-\(t\) range is expressed by
   \((\exists X)(\forall \tau\le t)
     [\alpha(X;\tau)\leftrightarrow Y(\tau)]\).
   This is a prefix-controlled explicit definition, and Section 5 synthesis
   yields the terminal recognizer.  Hence enumeration implies decidability.
2. Conversely, suppose \(L\ne\varnothing\), every positive-length prefix of a
   member lies in \(L\), and every member has a strictly longer extension in
   \(L\).  For an input word already in \(L\), output it.  Otherwise keep its
   longest prefix in \(L\) and choose the first length-\(t\) member of \(L\)
   extending that prefix.  Prefix closure and repeated proper extension supply
   a member of every positive length and guarantee that this choice exists.
   Every output lies in \(L\), and every word of \(L\) is obtained by feeding
   itself, so the lengthwise range is exactly \(L\).  The source's formula on
   p. 128 explicitly defines this zero-anticipation operator.

The source omits \(L\ne\varnothing\).  The empty language is terminally decided
by the constant-zero one-state operator and satisfies prefix closure and proper
extendibility vacuously, but \(A^t\ne\varnothing\) makes the range of every
total \(T_t\) nonempty.  Hence it cannot be enumerated.  The missing hypothesis
is exposed exactly in the source construction's request for a first word of
length \(t\) when there is no accepted prefix.  Manuscript lines 849--858 both
add nonemptiness and identify it as handbook-owned.

Expanded pp. 130--131 define \(\mathcal I'\) by eventually-zero predicate
variables.  For such an \(X\), \(X(1)\cdots X(t)\) is a special beginning only
when \(X(\tau)=0\) for every \(\tau>t\); it is not an arbitrary prefix.  Section
5, Theorem 3 gives an \(A\)-operator for every \(\mathcal I\)-formula which
recognizes precisely special beginnings of satisfying eventually-zero
predicates.  Existence in this arbitrary-\(\mathcal I\) case is not promoted to
effective synthesis.  When the formula is already in \(\mathcal I'\), the
operator is effectively constructible, and the source explicitly attributes
that step to B\"uchi.  The manuscript preserves all four distinctions.

## 9. Announcement/expansion result map (M22)

The visual source order and manuscript locators support the following map.  No
expanded number is transferred back to the announcement.

| 1961 announcement | 1962 expansion | Exact relationship |
|---|---|---|
| Theorem 1, pp. 326--327 | Section 1 unnumbered normal-form theorem, pp. 108--109 | same effective lower/upper normal form; expansion prints the derivation |
| Theorem 2, p. 327 | Section 3, Theorem 1, pp. 116--118 | definable implies homogeneous and internal transition effectively obtained |
| Theorem 3, p. 328 | Section 3, Theorems 2 and \(2'\), p. 118 | closed homogeneous converse, recurrent form, and closure characterization |
| Theorem 4, p. 328 | Section 4, Theorem 1, pp. 119--120 | continuous definable graph gives finite operator and weight bound |
| Theorem \(4'\), p. 328 | Section 4's selection/general-solution development, pp. 120--124, but no silently assigned identical number | closed homogeneous relation has finite/Л selection under the stated solution hypotheses; announcement separately gives the open case without the bound |
| Theorem 5, p. 328 | Section 4, Theorem 3, pp. 121--124 | no-zero-anticipation-solution/general-solution alternative and stable deletion |
| no announced counterpart at the same detail | Section 4, Theorem 2, p. 120 | definable graph without continuity gives only broad finite memory |
| no announced counterpart at the same detail | Section 4, Theorem \(3'\), p. 124 | separate general solution for each fixed anticipation bound \(p\) |

The expansion additionally supplies Section 5's explicit synthesis,
positive-length word theorem, and \(\mathcal I'\) result on pp. 124--131.  The
manuscript never cites those details as if printed in the four-page
announcement.

## 10. Modern finite-word theorem and source nonconflation (M23)

The shared theorem at `logic-in-computer-science.tex` lines 811--825 is
mathematically correct: track encodings of monadic valuations, automata for
atomic formulae, Boolean closure, and projection prove MSO-to-automaton;
monadic state-position sets encode an accepting run in the reverse direction.
On finite words, order and successor presentations are interdefinable in MSO,
including the usual definable endpoint conditions on nonempty words.

The same paragraph explicitly calls the displayed equivalence the *modern*
formulation and distinguishes B\"uchi's eventually-false/terminal-marker
encoding, Elgot's finite-set arithmetic and design calculus, and
Trakhtenbrot's arbitrary-predicate operator/topology/synthesis package.  The
Thomas locator at `n-c-014.tex` lines 888--905 and the navigation paragraph at
`logic-in-computer-science.tex` lines 2341--2347 identify the later survey as a
synthesis, not a replacement original.  Thus the compound theorem name does
not launder the one-sentence modern formulation into announcement Theorems
1--5 or \(4'\).

## 11. Terminology and adversarial compression audit (M26--M28)

Every technical name introduced in the Trakhtenbrot block meets the repository
rule at first public use.

| Name/location | Exact standing and eliminability | Nonredundancy and later use |
|---|---|---|
| \(\mathcal I\), lines 499--519 | interpreted formal language given by an eliminable primitive grammar | distinguished from automata and \(\mathcal I'\); used throughout every theorem |
| fictitious/controlled/upper/lower, lines 521--540 | semantic relation and four exact syntactic/dependence notions | syntactic classes are not their semantic consequences; needed by normal form and explicit synthesis |
| anticipation, finite memory, weight, finite operator, \(A\)-operator, lines 550--594 | properties of stream operators and one least-cardinality invariant | whole-suffix memory, bounded lookahead, and zero-lookahead finite realization are pairwise distinguished; used in Sections 2, 4, and 5 |
| portion, tuple portion, homogeneous degree, basis, internal transition, lines 605--629 | stream-set constructions/data with exact coordinate types | empty/nonempty conventions and tuple shifts differ; used in both definability and finite realization |
| \(\operatorname{tail}_r\), \(T_u\), residual stream operator, lines 631--657 | typed shift and operator defined by equations | expressly not a broad memory state; required for the exact graph-portion equation and correction |
| solution/general \(A\)-solution/general zero-anticipation solution, lines 759--785 | relation containment and two-quantifier parameter properties | graph equality, existence, completeness, and soundness differ; used immediately in Theorems \(4'\), 5, 3, and \(3'\) |
| explicit definition, lines 807--820 | formula that determines one output predicate pointwise | distinct from an implicit relation; used by the synthesis algorithm |
| \(T_t\), automaton-enumerable, terminal result, automaton-decidable, lines 822--858 | positive-length word maps, range property, and terminal recognition property | range and recognizer notions are not conflated; used in expanded Theorem 2 |
| \(\mathcal I'\), special beginning, lines 860--869 | weak eventually-zero language and exact finite-word property | differs from unrestricted \(\mathcal I\) and arbitrary prefixes; used in expanded Theorem 3 |

No definition occurs after its proof use, no redundant hypothetical object is
named, no standing ambiguity remains, and every distinction is used.

Adversarially, the snapshot also survives the specific compression risks:

- finite memory is never collapsed into bounded lookahead (`n-c-014.tex`
  lines 561--594, 755--757);
- continuity and closedness are explicit at every topological use (lines
  631--635, 700--730, 747--769, 787--805);
- the empty portion, empty closed set, no-solution branch, and empty word-set
  counterexample are each handled at their distinct logical level;
- Cyrillic Л and Latin \(A\), announcement and expansion numbering, and the
  two official English titles are not silently normalized (lines 487--497,
  586--590);
- handbook-owned residual, weight-bound, nonempty-covering, empty-set, and
  finite-word repairs are labeled at their public points of use;
- the source-time conditional algorithm, Putnam boundary, and historical
  attributions are not converted into modern priority adjudications;
- the modern regular/MSO proof is not substituted for Trakhtenbrot's broader
  source package;
- the rights qualification remains limited to individual noncommercial
  teaching/research printing and does not infer electronic-copy or
  redistribution permission (`p09-trakhtenbrot-1961-source-note.md` lines
  73--79; compact record line 648); and
- status language remains limited to the N-c-014.c manuscript snapshot.  It
  does not claim a build, rendered-handbook inspection, human acceptance,
  Part IX completion, or final-book completion.

## Mandatory coverage disposition

| Point | Disposition | Controlling audit location |
|---|---|---|
| M01 | checked-clean | seven-label table above |
| M02 | checked-clean | original-detail 4+29 visual map above |
| M05 | checked-clean | Section 1; expanded pp. 104--105, 130--131; manuscript 499--519, 860--869 |
| M06 | checked-clean | Section 1; announcement 326--327; expanded 105--109; manuscript 521--548 |
| M07 | checked-clean | Section 2; announcement 326--327; expanded 109--112; manuscript 550--594 |
| M08 | checked-clean | Section 2; expanded 111--113; manuscript 574--603 |
| M09 | checked-clean | Section 3; announcement 327; expanded 113--116; manuscript 605--699 |
| M10 | checked-clean | Section 4; announcement 327; expanded 116--118; manuscript 700--703 |
| M11 | checked-clean | Section 4; announcement 327--328; expanded 116--119; manuscript 703--736 |
| M12 | checked-clean | Section 4; announcement 326, 328--329; expanded 119, 124; manuscript 738--745, 797--805 |
| M13 | checked-clean | Section 5; announcement 328; expanded 119--120; manuscript 747--755 |
| M14 | checked-clean | Section 5; expanded 120; manuscript 755--757 |
| M15 | checked-clean | Section 5; announcement 328; expanded 119--120; manuscript 759--769 |
| M16 | checked-clean | Section 6; announcement 328; expanded 120--121; manuscript 771--785 |
| M17 | checked-clean | Section 6; announcement 328--329; expanded 121--124; manuscript 787--798 |
| M18 | checked-clean | Section 6; expanded 124; manuscript 798--803 |
| M19 | checked-clean | Section 7; expanded 124--127; manuscript 807--820 |
| M20 | checked-clean | Section 8; expanded 127--129; manuscript 822--858 |
| M21 | checked-clean | Section 8; expanded 130--131; manuscript 860--869 |
| M22 | checked-clean | Section 9 theorem map |
| M23 | checked-clean | Section 10; shared theorem 811--825; manuscript 871--905; navigation 2341--2347 |
| M26 | checked-clean | Section 11 terminology table |
| M27 | checked-clean | Section 11 adversarial audit |
| M28 | checked-clean | evidence disclosure and Section 11 scope/rights/status audit |

M03--M04 and M24--M25 are not assigned coverage points for this mathematical
seat.  I nevertheless supplied the competence disclosure required to delimit
my evidence, checked the printed mathematical locators used above, and made no
source-fidelity or specialist-translation claim beyond this mandate.

VERDICT: ACCEPT

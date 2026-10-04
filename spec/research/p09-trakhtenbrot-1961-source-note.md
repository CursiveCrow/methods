# Trakhtenbrot 1961/1962 source note

## Admission status

This note controls the reconstruction of register item `N-c-014.c`.  The
registered source is the four-page 1961 announcement.  A second primary source,
Trakhtenbrot's complete twenty-nine-page 1962 article under the same Russian
title, supplies the definitions, proofs, examples, and qualifications that the
announcement compresses.  The two publications are not silently identified:
the 1961 pagination and theorem numbering control claims about the
announcement, while the 1962 pagination and numbering control the complete
development.

The Russian bodies have been acquired and visually inspected in full.  On the
unchanged Round 5 snapshot, the source-fidelity and mathematical seats accepted
and the adversarial publication seat rejected four exact-definition and
ownership defects.  Those four defects are repaired in the revised reader and
records below, but the revision is not yet admitted: a fresh blind review of
one frozen snapshot remains required.  No claim of review by a
Russian-language specialist is made.

## Source identity, custody, and visual inspection

### Registered announcement

- B. A. Trakhtenbrot, “Конечные автоматы и логика одноместных предикатов”
  [Math-Net English title: “Finite Automata and the Logic of Single-Place
  Predicates”], *Doklady Akademii Nauk SSSR* 140(2) (1961), 326--329.
- Math-Net record: <https://www.mathnet.ru/eng/dan25511>.
- Local source: `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1961.pdf`.
- File size: 566,358 bytes.
- SHA-256:
  `44213AEBE4DB2F1C389B812A7401138799C3DB4749C3605BA7211BBB4BAF96F9`.
- Reading-aid text:
  `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1961-layout.txt`, 23,018 bytes,
  SHA-256
  `18584E21CF79D98F863C6192DDBADF752D15FBD287A7E40BD4A4496F00665F4D`.
- All four physical pages were rendered and visually inspected at original
  detail.  The scan, not OCR, controls every formula and word reported below.

The paper records that P. S. Novikov presented it on 16 May 1961.  The body
ends with receipt on 29 April 1961.  The correction printed beneath the
bibliography concerns Trakhtenbrot's earlier reference (2), not this article.

### Complete expanded article

- B. A. Trakhtenbrot, the same Russian title [Math-Net English title: “Finite
  Automata and the Logic of One-Place Predicates”], *Sibirskii
  Matematicheskii Zhurnal* 3(1) (1962), 103--131.
- Math-Net record: <https://www.mathnet.ru/eng/smj4799>.
- Local source:
  `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1962-expanded.pdf`.
- File size: 1,884,181 bytes.
- SHA-256:
  `EAB4438A7BBA2B6009374826A98A3A61FB6465C493F57B03D2C6C7385824096D`.
- Reading-aid text:
  `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1962-expanded-layout.txt`,
  160,210 bytes, SHA-256
  `611661C9DB24DD9438F2DE18736372D18700A29FA539D7B5C4D7AC5E4AFE558B`.
- All twenty-nine physical pages, printed pp. 103--131, were rendered and
  visually inspected at original detail.  The scan, not OCR, controls every
  formula and word reported below.

The official records therefore use different English renderings of the same
Russian title: “single-place” for the 1961 announcement and “one-place” for the
1962 expansion.  The reconstruction does not silently normalize them.  The
expanded paper records receipt on 15 May 1961.  An AMS bibliographic route
identifies a later English translation, “Finite Automata and the Logic of
One-Place Predicates,” in *American Mathematical Society Translations*, Series
2, volume 59 (1966), 23--55, DOI `10.1090/trans2/059/02`.  That translation's
body was not acquired and is not used as textual evidence here.

Math-Net's public access supports scholarly inspection.  Its
[Terms of Use](https://www.mathnet.ru/php/agreement.phtml?option_lang=eng)
permit individual teachers, students, and researchers to print copies for
noncommercial teaching or research.  Outside that exception, the material
remains copyrighted and reproduction or republication requires written
permission.  That access is not an open-content or republication licence, and
the local PDFs above are research objects not authorized for redistribution.

## Authority and translation boundary

The source prints the name of its formal system as the Cyrillic capital letter
И.  The reconstruction normalizes this typographically as \(\mathcal I\) and
states that normalization at first use.  This is a name for a formal language
with its intended interpretation, not for an automaton, a set, or a theorem.

The 1961 announcement prints Cyrillic `Л-оператор` and `общее Л-решение` for
the automaton-realizable class and its general solution.  The 1962 expansion
instead prints Latin `A-оператор` and `общее A-решение` for the same class and
parametrizing object.  Thus an \(A\)-operator in the expansion is a finite
operator with zero anticipation, hence an operator realizable by a finite
automaton; it is called a Л-operator in the announcement.  When a single
reader sentence combines the two versions, it explicitly adopts the
expansion's \(A\) as normalized terminology rather than silently attributing it
to 1961.  The source separately abbreviates “operator without anticipation”
with the Cyrillic lowercase д.  The reader avoids transliterating that
abbreviation into a new Latin technical symbol and ordinarily says
“zero-anticipation operator.”  These terms are nonredundant: a finite operator
may use a fixed positive amount of future input, whereas an \(A\)-operator may
not.

The reconstruction translates only the definitions, results, proof moves,
examples, and historical qualifications actually used.  It does not present
itself as a complete line-by-line English translation.  Where the four-page
announcement and the expanded article number analogous results differently,
both locators are stated.

## The formal system \(\mathcal I\)

The expanded article, §1, fixes the intended structure exactly:

- individual variables range over \(1,2,3,\ldots\);
- monadic predicate variables range over arbitrary predicates on those natural
  numbers, equivalently arbitrary subsets;
- immediate successor is primitive;
- for an individual variable \(t\), \(t^{(0)}=t\) and
  \(t^{(k+1)}=(t^{(k)})'\);
- atomic formulas have the form \(X(t^{(k)})\), with \(X\) a monadic predicate
  variable and \(k\geq0\); and
- propositional operations, individual quantifiers, and predicate quantifiers
  form the formulas.

Equality, order, bounded individual quantifiers, constants, and terms
\(t+k\) are explicitly introduced as eliminable conveniences.  Thus neither
order nor addition is silently treated as primitive.  This also separates
\(\mathcal I\) from Büchi's weak system: in the latter, predicate variables
range only over predicates eventually equal to zero, whereas
\(\mathcal I\) permits every subset.

The semantic dependence definition in §1.2 says that a free predicate occurs
fictitiously outside an interval when changing its values outside that interval
cannot change the formula's truth.  This is a semantic independence condition,
not merely an absence-of-symbols test.

The source's controlled and lower/upper classes are syntactic.  Fix a formula
whose only free individual variable is \(t\).  It is \(t\)-controlled from
above when every individual quantifier over \(\sigma\) has a range
\(\sigma<\mu\) or \(\lambda<\sigma<\mu\), and it is \(t\)-controlled from
below when every such range is \(\lambda<\sigma\) or
\(\lambda<\sigma<\mu\), with \(\lambda,\mu\) terms.  An upper
\(t\)-formula is \(t\)-controlled from below, every atomic argument is an
individual variable or a variable plus a numeral constant but not a bare
constant, and every individual-quantifier range is \(t<\sigma\) or
\(t<\sigma<\mu\).  A lower \(t\)-formula is \(t\)-controlled from above,
has the same atomic-argument restriction, and has ranges \(\sigma<t\) or
\(\lambda<\sigma<t\).  Section 1.3 supplies the quantifier-elimination
procedure for the controlled classes.

The 1961 Theorem 1 (printed p. 327, after the lower/upper terminology on
p. 326) and the unnumbered normal-form theorem in expanded §1.4
effectively transform every \(\mathcal I\)-formula into a Boolean combination
of lower and upper \(t\)-formulas.  Separately from those definitions, an upper
formula is fictitious outside \([t,\infty)\), while a lower formula is
fictitious outside \([1,t+s]\), where \(s\) is the largest numeral offset in
an argument of a free predicate.  The proof first moves predicate quantifiers
outside individual quantifiers, pushes the individual quantifiers inward,
splits each remaining individual quantifier at \(t\), and then uses the
independence of prefix and tail values to distribute a predicate quantifier
across the two pieces.  This normal form is the finiteness source for the later
residual construction.

## Operators, anticipation, memory, and canonical equations

For finite alphabets \(A,B\), an operator sends every stream
\(a:\mathbb N_{+}\to A\) to a stream
\(b:\mathbb N_{+}\to B\).  It has anticipation \(p\geq 0\) when \(b(t)\)
is independent of \(a(t+p+1),a(t+p+2),\ldots\).  Anticipation zero is
equivalent to prefix preservation: extending an input word can only extend the
already produced output word.

An operator has finite memory when there are a finite state set \(Q\), an
initial state \(q(1)\), and maps

\[
 \Phi:Q\times A^{\mathbb N_+}\to B,
 \qquad
 \Psi:Q\times A^{\mathbb N_+}\to Q
\]

such that, for the whole suffix
\(a_{\geq t}=(a(t),a(t+1),\ldots)\),

\[
 b(t)=\Phi(q(t),a_{\geq t}),
 \qquad
 q(t+1)=\Psi(q(t),a_{\geq t}).
\]

The least possible cardinality of \(Q\) is the source's *weight* of the
operator.  The whole-future arguments in these equations are essential: the
state after a finite prefix need not be determined by that prefix.  A *finite
operator* has both finite memory and bounded anticipation.  For a fixed
\(p\), its canonical equations have the form

\[
  b(t)=\Phi\bigl(q(t),a(t),\ldots,a(t+p)\bigr),
  \qquad
  q(t+1)=\Psi\bigl(q(t),a(t),\ldots,a(t+p)\bigr),
\]

with a fixed initial state.  In the expansion an \(A\)-operator is the case
\(p=0\); the announcement calls the same class a Л-operator.  The distinction
from a positive-anticipation finite operator is used later, so neither term is
an unused synonym.

Expanded §2 calls a stream “periodic” when a finite preperiod \(\alpha\) and a
period \(\beta>0\) satisfy
\(f(\alpha+t)=f(\alpha+\beta+t)\) thereafter; in current terminology this is
*ultimately periodic*.  The section also shows why finite
memory and bounded anticipation are required
together.  There are uncountably many zero-anticipation operators, so zero
anticipation alone does not imply effectiveness.  A finite-memory operator can
also be nonrecursive if its output depends on a nonrecursive property of the
entire future.  Their conjunction yields the special primitive-recursive form
given by the canonical equations.  The article also shows that primitive-
recursive schemes are too broad for effective recognition or synthesis of
finite automata: ultimate periodicity and extraction of a finite-state
presentation are undecidable in that language.

## Cantor-space portions and homogeneity

A predicate \(X\) is identified with the Cantor-space point
\(X(1)X(2)\cdots\).  The 1961 announcement defines, for every finite binary
word \(u\), the *portion* after \(u\) by

\[
  M_u=\{Z:uZ\in M\}.
\]

The announcement explicitly says that this set may be empty.  The 1962
expansion changes the convention: it introduces a portion only after requiring
that \(M\) have nonempty intersection with the corresponding prefix interval.
This reconstruction uses the announcement's all-prefix convention and states
the expansion's nonempty-portion convention whenever the distinction matters.
For finite alphabets \(A_1,\ldots,A_n\),
\(M\subseteq\prod_{i=1}^n A_i^{\mathbb N_+}\), \(r\geq0\), and equal-length
coordinate prefixes \(u_i\in A_i^r\), the coordinatewise definition is
\[
 M_{(u_1,\ldots,u_n)}
 =\{(Z_1,\ldots,Z_n)\in\prod_{i=1}^n A_i^{\mathbb N_+}:
      (u_1Z_1,\ldots,u_nZ_n)\in M\}.
\]
Thus the coordinates are concatenated and shifted separately, not interleaved.
A set is *homogeneous of degree at most \(k\)* when the all-prefix family has
at most \(k\) distinct members.  A basis is a finite list containing the
original set and every distinct portion; appending a bit sends one basis
member to another and therefore defines an internal transition function.
These are properties and finite data of a set of streams; they do not name new
kinds of automata.

Expanded p. 115 prints that the graph of a zero-anticipation operator of
weight \(k\) is closed and homogeneous of degree at most \(k\).  Zero
anticipation does make the graph closed, but the numerical degree claim is
false even under the expansion's nonempty-portion convention.  The source's
whole-future memory equations do not make the state after a prefix a function
of that prefix.

For a minimal explicit refutation of the printed inference, let

\[
 T(X)(t)=
 \begin{cases}
  X(t),&X(1)=1,\\
  0,&X(1)=0.
 \end{cases}
\]

Its output through time \(t\) depends only on the input through time \(t\), so
its anticipation is zero.  It has weight exactly two.  A two-state
whole-future finite-memory presentation takes \(Q=\{0,1\}\), \(q(1)=0\), and, for
\(z=(z_0,z_1,\ldots)\),

\[
 \Phi(q,z)=(1-q)z_0,
 \qquad
 \Psi(q,z)=q\mathbin{\mathsf{xor}}z_0\mathbin{\mathsf{xor}}z_1.
\]

Induction gives \(q(t)=X(1)\mathbin{\mathsf{xor}}X(t)\), hence the required
output.  A one-state presentation would use the same suffix function at every
time.  Its time-one value would have to be \(z_0\) for every suffix \(z\),
which gives the wrong time-two output on any input beginning \(01\).  The
graph itself, its portion after paired prefix \((0,0)\), its portion after
\((1,1)\), and its portion after \((0,1)\) are respectively the original
graph, the constant-zero graph, the identity graph, and \(\varnothing\).
Thus a weight-two graph has three distinct nonempty portions and four
all-prefix portions, refuting both the printed \(k\) bound and the formerly
proposed \(k+1\) repair.

The safe convention-sensitive statement is exact without a weight claim.  For
a zero-anticipation operator
\(T:A^{\mathbb N_+}\to B^{\mathbb N_+}\), \(u\in A^r\), and
\(Z\in A^{\mathbb N_+}\), let \(v_u\in B^r\) be the common length-\(r\)
prefix of \(T(uZ)\), and define
\[
 \operatorname{tail}_r(Y)(t)=Y(t+r),
 \qquad
 T_u:A^{\mathbb N_+}\to B^{\mathbb N_+},
 \qquad
 T_u(Z)=\operatorname{tail}_r(T(uZ)).
\]
Writing \(G_T=\{(X,T(X)):X\in A^{\mathbb N_+}\}\), for every \(v\in B^r\)
the typed tuple definition gives
\[
 (G_T)_{(u,v)}
 =\begin{cases}
    G_{T_u},&v=v_u,\\
    \varnothing,&v\neq v_u.
   \end{cases}
\]
Thus the expansion counts the distinct maps \(T_u\), while the announcement's
all-prefix convention adds at most the empty portion.  The maps \(T_u\) are
residual stream operators, not broad memory states; that distinction is needed
because future-dependent state updates can make the two counts differ.  This
notation, the counterexample, and the qualification are handbook-owned; the
source's closedness claim is unaffected.

The remaining examples are sound: a singleton \(\{X\}\) is homogeneous
exactly when \(X\) is ultimately periodic, and homogeneous sets need not be
\(\mathcal I\)-definable.  The article obtains the latter point from an
uncountable family of one-homogeneous sets against the countability of the
formulas.

For \(M\ne\varnothing\), the covering construction chooses a permitted next
bit at each nonempty basis member, follows the internal transition function,
and has image exactly \(\overline M\).  This supplies the recurrent definition
used in the converse theorem.  For \(M=\varnothing\), the printed total
covering operator necessarily has nonempty image, so that proof does not
apply.  The empty set is instead defined in the same recurrent syntactic shape
by adding the contradictory initial clause \(q_1(1)=0\) to
\(q_1(1)=1\).  The closed-homogeneous converse remains valid; the covering
lemma on expanded p. 116 tacitly requires nonemptiness.  This empty-set case
split and the nonempty restriction are handbook-owned.

## Definability theorems and their proof architecture

The announcement's Theorems 2--3 correspond to expanded §3, Theorems 1--2'.

1. Every \(\mathcal I\)-definable set is homogeneous.  From the normal form,
   fixing a finite prefix changes only finitely many Boolean functions of a
   bounded window; hence only finitely many residual formulas occur.  The
   internal transition function is effectively constructed from the defining
   formula.
2. The converse fails without a topological hypothesis.  Every *closed*
   homogeneous set is \(\mathcal I\)-definable, indeed by a recurrent formula
   in the free predicate \(X\) of the shape
   \[
   \begin{aligned}
     \varphi(X)\equiv
     (\exists q_1\cdots\exists q_k\exists U)\bigl[&
       q_1(1)=1\land q_2(1)=\cdots=q_k(1)=0\\
       &{}\land(\forall t)\,
       \theta\bigl(X(t),q_1(t),\ldots,q_k(t),U(t),
                    q_1(t+1),\ldots,q_k(t+1)\bigr)
     \bigr].
   \end{aligned}
   \]
   Here the bound predicates \(q_1,\ldots,q_k\) record the finite basis state,
   the bound predicate \(U\) supplies the permitted choice, and \(\theta\) is
   quantifier-free; the literal initial values designate the original basis
   member.  Conversely every formula of that shape defines a closed
   homogeneous set.
3. Consequently the \(\mathcal I\)-definable sets are exactly the least class
   containing the closed homogeneous sets and closed under complement, finite
   union, and projection; intersection follows from the Boolean operations.
   The 1961 announcement expressly leaves the represented Borel and projective
   classes open.

The construction of the internal residual transition is unconditional.  To
construct the external choice/output function one must decide which residual
formulas define nonempty sets.  The article calls a procedure depending on a
truth algorithm for closed \(\mathcal I\)-formulas a *conditional
\(\mathcal I\)-algorithm*.  This historical condition must remain visible.
The article notes that Putnam's decision procedure makes the construction
unconditional for the displayed existential-predicate recurrent fragment.

## Continuous operators, finite realization, and general solutions

For a relation \(R\subseteq P^X\times P^Y\), an operator solves the defining
formula when its graph is contained in \(R\); the formula defines an operator
when \(R\) is exactly its graph.  This distinction is used throughout §4.

The 1961 Theorem 4 and expanded §4 Theorem 1 state that if an
\(\mathcal I\)-definable relation is the graph of a continuous total operator,
then the operator is finite, with memory bounded by the homogeneity degree.
If the operator has zero anticipation, it is therefore a Л-operator in the
announcement and an \(A\)-operator in the expansion.  The proof applies compact
uniform continuity to each nonempty residual graph to obtain one finite
lookahead bound, and uses the finite residual basis as memory.
Expanded §4 also records the exact corollary: a recursive operator is
\(\mathcal I\)-definable exactly when it is a finite operator.

Expanded §4 Theorem 2 separately removes continuity from the hypothesis and
concludes only finite memory, still with weight bounded by the homogeneity
degree.  This is strictly weaker than being a finite operator: without
continuity there need not be any bounded anticipation.  The reconstruction
therefore does not collapse “finite memory” into “finite operator.”

The announcement's Theorem 4' is the existence version.  If a closed
homogeneous relation has a continuous solution, it has a finite solution of
weight bounded by the relation's homogeneity degree; if it has any
zero-anticipation solution, it has a Л-operator solution---called an
\(A\)-operator in the expansion---with the same bound.  The announcement
separately notes an analogous open-relation result without the weight bound.

In the expansion's notation, an \(A\)-operator \(Y=T(X,U)\), with \(U\) a
tuple of parameter streams, is a *general \(A\)-solution* of a formula
\(\varphi(X,Y)\) exactly when the following two clauses hold.  The announcement
prints the same definition with Л in place of \(A\):

1. every \(A\)-solution \(Y=T_0(X)\) is obtained by substituting some
   \(A\)-operator \(U=T_U(X)\) into \(T\); and
2. every such \(A\)-operator substitution yields a solution of \(\varphi\).

The announcement allows more than one parameter tuple; one tuple is an
eliminable packaging of the same data.  Replacing \(A\)-operators throughout
by arbitrary zero-anticipation operators gives the source's general
zero-anticipation solution.  This definition is nonredundant with existence of
one solution: it parameterizes *all* solutions of the specified class and only
those solutions.

The 1961 Theorem 5 and expanded §4 Theorem 3 give the main synthesis
alternative for an \(\mathcal I\)-formula whose defined relation is closed and
hence homogeneous of finite degree: either there is no zero-anticipation
solution, or there is a bounded-weight general solution for the
automaton-realizable class, and it is simultaneously a general
zero-anticipation solution.  The announcement calls it a general Л-solution;
the expansion calls it a general \(A\)-solution.  The proof repeatedly deletes
empty or non-extendible residual formulas until either the initial residual
disappears or a maximal stable residual family remains.  In the second case,
free parameter bits choose among the surviving outputs and the residual
transition supplies the finite memory.  Closedness turns agreement of every
finite prefix with the relation into actual membership.

The construction is conditional for an arbitrary closed
\(\mathcal I\)-formula because deletion requires testing residual emptiness.  It
is unconditional for the recurrent fragment above by Putnam's algorithm.  The
source explicitly says Church obtained a narrower earlier general-solution
algorithm and that Elgot had a related result but no notion of general
solution.

Expanded §4 Theorem 3' gives the fixed-lookahead extension for that same closed
\(\mathcal I\)-definable relation: for each \(p\geq0\), either no operator with
anticipation \(p\) solves it, or a finite operator with anticipation \(p\),
weight bounded by the homogeneity degree, is a general solution for all
solutions with that same anticipation bound.  The proof shifts the first
\(p\) output places and reduces the claim to the zero-anticipation theorem.
This is a fixed-\(p\) result, not one unbounded general solution for all
lookahead classes at once.

## Explicit definitions and the finite-word boundary

Expanded §5 distinguishes an explicit definition
\(Y(t)\leftrightarrow\varphi(X_1,\ldots,X_m;t)\) from an arbitrary implicit
formula in \(X,Y\).  Every explicit formula defines a finite-memory operator.
It defines a finite operator with anticipation \(p\) exactly when it is
semantically independent of predicate values outside \([1,t+p]\), and it
defines an \(A\)-operator exactly when it is independent outside \([1,t]\).
For prefix-controlled formulas of zero shift, the article gives an
unconditional synthesis procedure: compute the output on each first input
column, form the residual formula, and repeat until no new residual formula
appears.  Normal form ensures termination; the resulting finite residual list
and its output/transition tables are the canonical equations.  The worked
example on pp. 126--127 produces two residual formulas and prints both tables.

For each zero-anticipation stream operator
\(T:A^{\mathbb N_+}\to B^{\mathbb N_+}\) and each \(t\geq1\), define

\[
  T_t:A^t\to B^t,
  \qquad
  T_t(u)=T(X)\mathbin{\upharpoonright}\{1,\ldots,t\},
\]

where \(X\) is any infinite extension of \(u\).  Agreement of two extensions
through \(t\) and zero anticipation make this independent of the extension.
The same argument gives prefix compatibility:
\(T_s(u|_{1..s})=T_t(u)|_{1..s}\) for \(s\leq t\).  This is the typed
finite-word action used by the source; the range of the stream map itself is
not a finite-word language.

The article states the next definitions for positive-length binary words and
notes that arbitrary alphabets are analogous.  A language \(L\) is
automaton-enumerable when some \(A\)-operator satisfies
\(L\cap B^t=T_t(A^t)\) for every \(t\geq1\).  For an \(A\)-operator
\(R:B^{\mathbb N_+}\to\{0,1\}^{\mathbb N_+}\), the terminal recognition result
on \(v\in B^t\) is \(R(X)(t)\) for any infinite extension \(X\) of \(v\); it is
well-defined by zero anticipation.  The language is automaton-decidable when
that result is one exactly for its members.  Expanded §5 Theorem 2 proves:

- every automaton-enumerable word set is automaton-decidable; and
- the source prints that an automaton-decidable word set is
  automaton-enumerable when it is closed under prefixes and every word has a
  longer extension in the set.

The printed converse needs the additional hypothesis \(L\neq\varnothing\).
Indeed, the empty language is automaton-decidable by the constant-zero
one-state operator and satisfies the two printed conditions vacuously, but no
total length-preserving operator can enumerate it: its length-\(t\) range is
nonempty for every \(t\geq1\).  The proof on p. 128 exposes the missing seed
when its no-accepted-prefix branch asks for the first length-\(t\) word in
\(L\).  If \(L\) is nonempty, prefix closure and proper extendibility supply a
member at every positive length, so that construction is defined.  The reader
therefore states the corrected nonempty converse and labels nonemptiness as a
handbook-owned edge-case repair rather than a printed Trakhtenbrot hypothesis.

Finally, expanded §5.3 defines the weak system \(\mathcal I'\), in which
predicate variables range only over predicates eventually equal to zero.
For such a predicate \(X\), the word \(X(1)\cdots X(t)\) is a *special
beginning* exactly when \(X(\tau)=0\) for every \(\tau>t\); an arbitrary finite
prefix need not be a special beginning.  Theorem 3 asserts, for every
\(\mathcal I\)-formula \(\varphi(X)\), the existence of an \(A\)-operator
recognizing exactly the special beginnings of the satisfying eventually-zero
predicates.  For an \(\mathcal I'\)-formula the operator is effectively
constructible, a conclusion the source explicitly attributes to Büchi.  This
is the source's literal finite-word/weak-predicate bridge.

The modern one-sentence equivalence “finite-word MSO-definable iff regular” is
therefore not quoted as if it were the literal statement of the four-page 1961
paper.  Trakhtenbrot's source presentation is broader: unrestricted predicate
logic, finite operators with lookahead, topology, recognition, synthesis, and
general solutions.  Büchi, Elgot, and the later Thomas survey control their own
distinct finite-word formulations.

## Historical qualifications

The 1961 announcement says that a decision algorithm for closed
\(\mathcal I\)-formulas was not then available to the author and defines the
conditional-algorithm terminology accordingly.  The expanded paper adds a
footnote that Büchi had announced decidability in *Notices of the AMS* while
the work was in press.  The source's constructions are reported at their
printed conditional strength; later decidability does not retroactively turn
every printed construction into an internally complete algorithm.

The announcement distinguishes its assumptions from three earlier routes:
controlled individual quantifiers in Trakhtenbrot's earlier language, absence
of predicate quantifiers in Church's limited recursive arithmetic, and
finite-set predicate interpretation in Büchi's weak second-order arithmetic.
It also records Robinson's conjecture concerning numerical functions definable
in \(\mathcal I\) and the weak system \(\mathcal I'\); the expanded article
derives the stated definability transfer in §5.3.  These priority and scope
remarks are reported as the author's historical claims, not as an independent
priority adjudication.

## Reader-facing integration

The reader-facing presentation in
handbook/parts/p09/presentations/n-c-014.tex now supplies:

- the distinct announcement/expanded-article authority and title boundary;
- the primitive grammar, exact interpretation, and eliminable extensions of
  \(\mathcal I\);
- the syntactic lower/upper classes, their separate semantic consequences,
  and the normal-form proof architecture;
- typed definitions of anticipation, finite memory, finite operator,
  \(A\)-operator, and weight;
- typed one- and many-coordinate portions, the residual operators used in the
  graph correction, homogeneity, closedness, and both definability directions;
- the conditional-algorithm boundary;
- the continuous-operator and finite-memory theorems at unequal strength;
- existence, general-solution, and fixed-anticipation synthesis results;
- explicit-definition synthesis and its worked-example locator; and
- the literal finite-word bridge through automaton-enumerability,
  automaton-decidability, and the weak system \(\mathcal I'\).

The shared finite-word theorem now labels its one-sentence equivalence as a
modern formulation and refuses to attribute that sentence verbatim to either
Russian source.  The bibliography records the official “single-place” 1961
title and the distinct official “one-place” 1962 title.

## Remaining admission work

1. Freeze the revised announcement, expanded paper, manuscript presentation,
   shared theorem, bibliography entries, compact record, and this note as one
   Round 6 review snapshot.
2. Obtain fresh independent source-fidelity, mathematical-proof, and
   adversarial publication/terminology verdicts without cross-reading.  The
   source-fidelity seat must state whether its competence and the available
   bodies support the reconstruction; no Russian-language-specialist
   certification may be implied unless that reviewer can actually supply it.
3. Reconcile any findings in prose.  Do not use tests, automated checkers,
   scripts, or an interim TeX/PDF build as substitutes for scholarly review.

## Residual-map theorem incorporated on 2026-09-06

The reader no longer introduces the false whole-future-memory degree bound
and then asks the reader to qualify it. The error and its source location
remain documented above. For finite nonempty alphabets and a total
zero-anticipation operator, the active text now proves that its graph is
closed and homogeneous exactly when the family of residual maps `T_u` is
finite. Its exact degree under the reader's all-prefix convention is
`|{T_u}| + epsilon`, where `epsilon` is one precisely when some paired
prefix is inconsistent and consequently supplies the empty portion.

The proof first uses a mismatching output coordinate to exhibit a product
cylinder outside the graph. The portion identity then identifies every
nonempty portion with a residual graph. Every residual graph occurs at a
consistent prefix, all are nonempty by totality and nonempty input space,
and equality of graphs is equality of maps. The possible empty portion
is distinct from all of them. Nonempty alphabets are explicit because this
last counting argument would otherwise fail for an empty input space.

The existing weight-two example is retained as mathematics: its residual
maps are exactly the original map, the constant-zero map, and the identity;
one inconsistent paired prefix supplies the fourth portion. Its surrounding
prose states this conclusion directly. No historical source claim is
silently promoted to this supplied exact theorem.

Only the active N-c-014 passage and this provenance note were changed for
this correction. No software tests, builds, renders, or new agents were used;
previous review dispositions apply only to their recorded snapshots.

The same exposition pass also removed correction-history phrasing from the
closed-homogeneous empty-set case and the finite-word enumeration converse.
The reader retains the actual contradictory initial clauses defining the
empty set, and explicitly assumes an automaton-decidable nonempty language
with nonempty-prefix closure and strict extensions for the converse.
It also retains the mathematical distinction that the empty language has
a constant-zero decider but cannot be the image of a total length-preserving
operator. The source's omitted nonemptiness hypothesis is documented above.

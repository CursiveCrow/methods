# Kamp 1968: thesis source note

Retrieved and directly inspected 2026-08-22. Scope: registered source
`N-c-012.a`, Johan Anthony Willem Kamp, *Tense Logic and the Theory of Linear
Order* (UCLA PhD thesis, 1968). This note uses only Kamp's institutional author
archive and the thesis body linked there. It does not reconstruct Kamp from a
later textbook, survey, or theorem slogan.

## Disposition

**CLOSED for source acquisition and for the requested source-level
reconstruction.**

A complete, readable thesis body is publicly and anonymously accessible from
the University of Stuttgart's Institute for Natural Language Processing. The
title and author identity, pagination, order classes, first-order language,
assignment convention, tense operators, satisfaction clauses, main
expressiveness theorem, both translation directions, Chapter IV Theorem 3,
nearby lemmas and the source's separating examples were all inspected in that
body. No requested technical field remains open for lack of access.

This disposition closes the earlier acquisition gap only. It is not a claim
that a reader-facing handbook presentation has been written or reviewed, and
it is not a proof-system completeness verdict. Each scan page states that the
copy was reproduced with the copyright owner's permission and that further
reproduction requires permission. The institutional link therefore
establishes lawful reading access, not public-domain status or a license to
republish the scan.

## Bibliographic identity, stable access, and file provenance

Kamp's institutional [Stuttgart bibliography](https://www.ims.uni-stuttgart.de/archiv/kamp/bibliography.html)
has the entry `Kamp, Hans (1968)`, *Tense Logic and the Theory of Linear Order*,
PhD thesis, University of California Los Angeles, with the note that it was
published as Johan Anthony Willem Kamp. Its `File` link points to an `http`
URL; that URL currently redirects to the stable institutional HTTPS file:

- [University of Stuttgart thesis PDF](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf)

Live access evidence on 2026-08-22 was:

| Resource | Response and provenance |
|---|---|
| Stuttgart bibliography | HTTP `200`; `text/html`; 115,347 bytes; `Last-Modified: Sat, 08 Sep 2018 06:40:18 GMT`; served by the University of Stuttgart's OpenCms instance |
| Bibliography's original HTTP file link | HTTP `301` to the HTTPS URL above |
| HTTPS thesis file | HTTP `200`; `application/pdf`; 11,617,255 bytes; no login or paywall; `Last-Modified: Wed, 08 Aug 2018 07:33:18 GMT` |

The retrieved PDF has SHA-256
`C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA`.
It is an unencrypted, 128-page, US-letter PDF 1.3 scan. The digital wrapper was
made in 2016 and has no useful author/title metadata; bibliographic identity
comes instead from the institutional bibliography and the scanned title and
approval leaves.

The [title leaf, PDF p. 1](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf#page=1)
identifies the object exactly as:

- author: **Johan Anthony Willem Kamp**;
- title: ***Tense Logic and the Theory of Linear Order***;
- institution: **University of California, Los Angeles**;
- degree: **Doctor of Philosophy in Philosophy**;
- year: **1968**.

The approval material names Richard Montague as committee chair and C. C.
Chang, David B. Kaplan, Yiannis N. Moschovakis, and J. Howard Sobel as the other
committee members. Thus `Hans Kamp` is the bibliography's author-name form,
whereas Johan Anthony Willem Kamp is the literal dissertation-title-page form.

## Pagination and locator map

The scan has one PDF page per dissertation leaf. PDF p. 1 is the unnumbered
title leaf, PDF pp. 2--9 contain the Roman-numbered preliminaries through p. ix,
and PDF p. 10 is printed dissertation p. 1. For every Arabic-numbered body page
`n`, the physical PDF page is therefore `n + 9`.

| Portion | Printed thesis pages | Physical PDF pages |
|---|---:|---:|
| Chapter I, `Introduction` | 1--14 | 10--23 |
| Chapter II, `Tenses and Their Expressibility` | 15--38 | 24--47 |
| Chapter III, `The Main Theorem` | 39--94 | 48--103 |
| Chapter IV, `Other Results on Expressibility` | 95--117 | 104--126 |
| Bibliography | 118--119 | 127--128 |

This mapping matters for Theorem IV.3: its heading is on printed p. 105,
physical [PDF p. 114](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf#page=114),
and its proof continues through printed p. 108, PDF p. 117.

## Order structures and endpoint policy

Kamp first uses a binary structure \(\mathcal J=\langle T,<\rangle\), with
nonempty carrier \(T\). A linear ordering is a strict order: `<` is asymmetric,
transitive, and connected on distinct elements. The following are the thesis's
named classes ([Chapter I, printed pp. 12--14; PDF pp. 21--23](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf#page=21)):

- `Lin`: all linear orderings.
- `Den`: the dense linear orderings. Whenever \(i<j\), some \(k\) satisfies
  \(i<k<j\).
- `Dis`: the discrete linear orderings. If a point has a later point, it has an
  immediate successor; if it has an earlier point, it has an immediate
  predecessor.
- `Com`: the complete linear orderings. Every nonempty subset with a lower
  bound has a greatest lower bound, and every nonempty subset with an upper
  bound has a least upper bound.

`Com` is order completeness, not logical or deductive completeness. Density is
not part of its definition: finite orders, the integer order, and the real
order are complete in this sense, whereas the rational order is not.

None of `Lin`, `Den`, `Dis`, or `Com` excludes a first or last point. The
discreteness clauses are explicitly conditional on there being something
earlier or later, and the completeness clauses do not impose endpoint absence.
The source confirms that endpoint cases are intentional near the end of
Chapter IV: the present-progressive argument separately treats orders with no
endpoints, a first but no last point, a last but no first point, and both a
first and a last point (printed pp. 113--117; PDF pp. 122--126).

The thesis also fixes three particular strict orders, here written in modern
carrier notation while preserving its names:

- \(\mathrm{In}=\langle\mathbb Z,<\rangle\), the integer ordering;
- \(\mathrm{Ra}=\langle\mathbb Q,<\rangle\), the rational ordering;
- \(\mathrm{Re}=\langle\mathbb R,<\rangle\), the real ordering.

This distinction controls Chapter IV: Theorems IV.2--IV.4 concern
\(\mathrm{In}\), Theorem IV.1 concerns \(\mathrm{Re}\), and Theorem IV.5
concerns \(\mathrm{Ra}\).

## Languages, models, and the assignment convention

### The propositional tense language

Chapter I introduces \(\mathrm{TL}_0\) with propositional constants
\(q_0,q_1,\ldots\), the usual sentential connectives, and the one-place temporal
operators `P` and `F`. A possible interpretation relative to
\(\mathcal J=\langle T,<\rangle\) is a pair \(\langle Q,R\rangle\): \(Q\) is a
sequence of subsets of \(T\), and \(R\) assigns the intended proposition
function to each operator symbol. In particular, \(q_j\) is true at \(t\) iff
\(t\in Q_j\); compound truth is defined recursively by applying the operator's
assigned proposition function to the extensions of its arguments and checking
whether \(t\) belongs to the resulting set.

For the strict past and future operators this specializes to:

\[
\begin{aligned}
\mathcal J,Q,t\models P\eta
&\iff \exists s\,(s<t\ \land\ \mathcal J,Q,s\models\eta),\\
\mathcal J,Q,t\models F\eta
&\iff \exists s\,(t<s\ \land\ \mathcal J,Q,s\models\eta).
\end{aligned}
\]

Thus `P` and `F` are existential and strict. They are not past-always and
future-always operators, and they do not include the current instant.

### The first-order language \(L\)

Chapter II Definition 2 gives the complete displayed vocabulary of the
first-order language \(L\) ([printed p. 21; PDF p. 30](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf#page=30)):

- variables \(t_0,t_1,\ldots\);
- connectives \(\neg,\land,\lor,\rightarrow,\leftrightarrow\);
- quantifiers \(\forall,\exists\);
- one binary predicate constant `<`;
- unary predicate constants \(P_0,P_1,\ldots\).

No equality symbol is listed in that vocabulary. Formulas and models are
otherwise said to be defined in the usual first-order way.

An **\(n\)-place tense-defining formula** is a formula in which \(t_0\) is free,
no other variable is free, and which contains \(P_0,\ldots,P_{n-1}\) and no
other unary predicate constants. Its standing is metalinguistic: it is a
first-order formula used to define an \(n\)-ary operation on propositions, not
a new object inside the first-order domain.

For \(\mathcal J=\langle T,<\rangle\), the tense defined by such a formula
\(\varphi\) is the function

\[
f_\varphi:\mathcal P(T)^n\longrightarrow\mathcal P(T)
\]

given by

\[
f_\varphi(Q_0,\ldots,Q_{n-1})
=\{t\in T:\langle T,<,Q_0,\ldots,Q_{n-1},\ldots\rangle
\models\varphi[t_0\mapsto t]\}.
\]

This makes the assignment convention exact: the unary predicates \(P_i\) are
interpreted by the input sets \(Q_i\), and the distinguished free variable
\(t_0\) is assigned the current point \(t\). The thesis abbreviates this by
saying that \(t\) satisfies \(\varphi\) in the expanded order; it does not add a
second special temporal valuation convention to ordinary first-order
satisfaction ([Definitions 2--3, printed pp. 21--22; PDF pp. 30--31](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf#page=30)).

A tense is **first-order definable** exactly when some tense-defining formula
defines it. After this definition, the thesis often shortens that phrase to
`tense`. Consequently, later claims about all tenses quantify over this
first-order-definable class, not over arbitrary functions
\(\mathcal P(T)^n\to\mathcal P(T)\).

For a class \(\mathcal H\) of linear orders, an \(\mathcal H\)-tense-function is
the family of the corresponding functions, one for every order in
\(\mathcal H\), defined uniformly by one first-order formula. An
\(\mathcal H\)-tense-function is \(\mathcal H\)-expressible from a specified
family of primitive tense-functions when one sentential schema built from
those primitives defines the target on every order in \(\mathcal H\). This
uniformity across the whole class is part of the theorem's strength.

## Exact tense operators and satisfaction clauses

On printed pp. 25--26, PDF pp. 34--35, Kamp names the following first-order
tense-defining formulas ([source locator](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf#page=34)):

\[
\begin{aligned}
\mathrm{NOT}(P_0;t_0)
&:=\neg P_0(t_0),\\
\mathrm{AND}(P_0,P_1;t_0)
&:=P_0(t_0)\land P_1(t_0),\\
\mathrm{PAST}(P_0;t_0)
&:=\exists t_1\,(t_1<t_0\land P_0(t_1)),\\
\mathrm{FUTURE}(P_0;t_0)
&:=\exists t_1\,(t_0<t_1\land P_0(t_1)),\\
\mathrm{SINCE}(P_0,P_1;t_0)
&:=\exists t_1\bigl(t_1<t_0\land P_0(t_1)\land\\
&\qquad\forall t_2((t_1<t_2\land t_2<t_0)\rightarrow P_1(t_2))\bigr),\\
\mathrm{UNTIL}(P_0,P_1;t_0)
&:=\exists t_1\bigl(t_0<t_1\land P_0(t_1)\land\\
&\qquad\forall t_2((t_0<t_2\land t_2<t_1)\rightarrow P_1(t_2))\bigr).
\end{aligned}
\]

Equivalently, for temporal formulas \(\eta,\zeta\):

- \(S(\eta,\zeta)\) is true at \(t\) iff some strict past witness \(s<t\)
  satisfies \(\eta\), and every \(u\) strictly between \(s\) and \(t\)
  satisfies \(\zeta\).
- \(U(\eta,\zeta)\) is true at \(t\) iff some strict future witness \(s>t\)
  satisfies \(\eta\), and every \(u\) strictly between \(t\) and \(s\)
  satisfies \(\zeta\).

The argument order is therefore source-critical: the **first** argument holds
at the witness and the **second** throughout the open interval. The second
argument is not required at the current point or witness merely by these
clauses. In a discrete order the open interval may be empty, so its universal
condition may be vacuous.

Chapter II Definition 8 introduces \(\mathrm{TL}_1\), whose primitive symbols
are negation, conjunction, `S`, and `U`, interpreted by `NOT`, `AND`, `SINCE`,
and `UNTIL` ([printed p. 28; PDF p. 37](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf#page=37)).
The ordinary `P` and `F` operators are definable in \(\mathrm{TL}_1\); Chapter
III printed pp. 57--58 gives the definitions and verifies their strict
existential truth clauses.

## Main theorem and the two translation directions

### Literal theorem strength

Chapter II Theorem 1 states that every `Com`-tense-function is uniformly
`Com`-expressible from `NOT`, `AND`, `SINCE`, and `UNTIL` ([printed p. 27; PDF
p. 36](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf#page=36)).
Theorem 2 strengthens the result effectively: a primitive recursive function
`Exp` sends each tense-defining first-order formula \(\varphi\) to a
\(\mathrm{TL}_1\) schema that expresses over `Com` the tense-function defined
by \(\varphi\) ([printed p. 28; PDF p. 37](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf#page=37)).
The thesis states primitive recursiveness here, but it does not state a
complexity or output-size bound for `Exp`.

The theorem is therefore:

- about **all complete strict linear orders**, not only \(\mathbb R\);
- compatible with discrete orders and with first and last endpoints;
- a uniform expressive-equivalence and effective-translation result;
- restricted to one-free-variable first-order properties with monadic input
  predicates in the displayed language;
- not a theorem for all arbitrary linear orders.

Immediately before Theorem II.1, the thesis says it cannot exhibit a finite
basis for every `Lin`-tense-function and that the existence of such a basis is
open (printed p. 27). Chapter IV later gives concrete failures of the four
operator basis on the rational ordering.

### Temporal syntax to first-order syntax: valid for every binary structure

Chapter III first defines the compositional map \(D\) from
\(\mathrm{TL}_1\) formulas into the first-order class \(\mathcal C\) ([printed
pp. 39--42; PDF pp. 48--51](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf#page=48)):

\[
\begin{aligned}
D(q_i)&=P_i(t_0),\\
D(\neg\eta)&=\neg D(\eta),\\
D(\eta\land\zeta)&=D(\eta)\land D(\zeta),\\
D(S(\eta,\zeta))&=\overline S(D(\eta),D(\zeta)),\\
D(U(\eta,\zeta))&=\overline U(D(\eta),D(\zeta)),
\end{aligned}
\]

where \(\overline S\) and \(\overline U\) insert fresh variables into exactly
the strict witness/open-interval formulas displayed above. Result `(R2)` on
printed p. 42 proves by structural induction that a temporal formula is true
at a point iff its \(D\)-translation is first-order satisfied there. This
result is stated for every binary structure, and therefore a fortiori for
every member of `Lin`; it uses neither linearity nor order completeness.

### First-order syntax to temporal syntax: the `Com` boundary

The converse occupies the substantive part of Chapter III.

1. Theorem III.1 says that, for \(r>0\), every formula of \(L\) whose free
   variables are \(x_1,\ldots,x_r\) is `Lin`-equivalent to a standard formula
   in those variables ([printed p. 48; PDF p. 57](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf#page=57)).
   Its proof on printed pp. 49--56 puts formulas into prenex form and eliminates
   quantifiers by induction using the source's `At`, `Bef`, `Aft`, and `Bet`
   components. The theorem itself requires at least one free variable; the
   corollary on printed p. 56 treats sentences separately.
2. Printed pp. 57--59 define the tense-formula operations corresponding to
   those one-free-variable components and the source's exact notion of one
   formula expressing another.
3. Theorem III.2 states that every tense-defining formula is `Com`-equivalent
   to a member of \(\mathcal C\) ([printed p. 60; PDF p. 69](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf#page=69)).
   The proof reduces a standard one-free-variable formula to Boolean
   combinations of `At`, `Bef`, and `Aft`, then establishes their
   expressibility through Lemmas 1--10 on printed pp. 60--93. Order
   completeness enters the interval/cut arguments. Lemma 10 on printed p. 93
   supplies the last closure case, and printed p. 94 closes the proof.
4. Since \(D\) is one-to-one onto \(\mathcal C\), the `Com`-equivalent member
   of \(\mathcal C\) has a unique inverse temporal formula. Composing the
   normal-form construction with that inverse gives the first-order-to-temporal
   translation claimed in Chapter II.

The exact asymmetry is therefore:

| Direction | Source mechanism | Order class |
|---|---|---|
| \(\mathrm{TL}_1\to L\) | compositional map \(D\) and structural truth induction `(R2)` | every binary structure (hence all `Lin`) |
| \(L\to\mathrm{TL}_1\) for tense-defining formulas | standard-form theorem, `At/Bef/Aft/Bet` decomposition, completeness-dependent lemmas, inverse of \(D\) | `Com` |

Theorem III.1's `Lin` normal form must not be misreported as a `Lin`
first-order-to-temporal theorem. The later completeness-dependent step is what
turns the normal form into a temporal formula, and that step is only established
over `Com`.

### Proof boundary and completeness caveat

The thesis contains the main construction and proof; it does not refer the
central expressive-equivalence argument to another publication. Chapter III
opens by saying that it is devoted to the proof of Theorem II.1, while Chapter
II says that the proof also yields the primitive-recursive strengthening in
Theorem II.2. The reductions are syntactic and inductive, so the effective
claim is part of the stated construction rather than an unproved modern
addition.

This is **expressive completeness relative to `Com`**, not soundness and
completeness of a proof calculus. The introductory discussion reports results
by Ehrenfeucht and Cocchiarella concerning axiomatization/deductive
completeness and decidability ([printed p. 14; PDF p. 23](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf#page=23)),
but those are historical referrals and are not proved by the main
expressiveness argument. A handbook must not use this thesis proof as if it
supplied an axiomatization or a proof-system completeness theorem.

## Chapter IV Theorem 3: exact statement and proof

### Definitions and immediate setting

Chapter IV Definition 2 introduces four one-place tenses on the integer order
\(\mathrm{In}=\langle\mathbb Z,<\rangle\) ([printed p. 100; PDF p. 109](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf#page=109)):

- `PAST_1(P)` holds at \(i\) iff \(P\) holds at the immediate predecessor of
  \(i\).
- `FUTURE_1(P)` holds at \(i\) iff \(P\) holds at the immediate successor of
  \(i\).
- `ISOLP(P)` holds at \(i\) iff some earlier \(P\)-point \(j<i\) has an
  immediate predecessor outside \(P\), and no \(P\)-point lies strictly
  between \(j\) and \(i\).
- `ISOLF(P)` is the future mirror: some later \(P\)-point \(j>i\) has an
  immediate successor outside \(P\), and no \(P\)-point lies strictly between
  \(i\) and \(j\).

The first-order definitions express absence of an intervening integer by a
universal implication whose consequent is \(P_0(t)\land\neg P_0(t)\). That
apparently contradictory subformula is deliberate: it forces there to be no
strictly intermediate point and is not a scan error.

Let

\[
\mathcal S=\{\mathrm{ISOLP},\mathrm{ISOLF},\mathrm{PAST}_1,
\mathrm{FUTURE}_1,\mathrm{NOT},\mathrm{AND}\}.
\]

Theorem IV.2 says that integer-order `SINCE` and `UNTIL` are expressible from
\(\mathcal S\). Its proof, printed pp. 100--105, constructs explicit schemata;
the detailed argument is given for `UNTIL`, with `SINCE` discharged by the
mirror argument.

Kamp then asks whether the two less familiar isolation operators can be
replaced by ordinary strict past and future. He defines

\[
\mathcal S'=\{\mathrm{PAST}_1,\mathrm{FUTURE}_1,
\mathrm{PAST},\mathrm{FUTURE},\mathrm{NOT},\mathrm{AND}\}.
\]

### Literal theorem

**Theorem IV.3:** neither `ISOLP` nor `ISOLF` is expressible on
\(\mathrm{In}\) using the operations in \(\mathcal S'\) ([printed p. 105; PDF
p. 114](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf#page=114)).

This is the literal Chapter IV Theorem 3. It is not the later rational-order
counterexample of Theorem IV.5.

### Separating predicate and structural invariant

For the sentential language `TS'` corresponding to \(\mathcal S'\), the proof
interprets its sole propositional input by the sparse set

\[
P_0=\{n^2:n\in\omega\}\ \cup\
\{(2n)^2+1:n\in\omega\}.
\]

The source calculates:

\[
\mathrm{ISOLF}(P_0)
=\{i\in\omega:\exists n\in\omega\ ((2n)^2\le i<(2n+1)^2)\},
\]

and

\[
\mathrm{ISOLP}(P_0)
=\{1\}\cup
\{i\in\omega:\exists n\in\omega\ ((2n+3)^2<i\le(2n+4)^2+1)\}.
\]

For an arbitrary `TS'` formula \(\eta\), let \(\bar\eta\subseteq\mathbb Z\)
be its truth set under this interpretation. Kamp states, as the claim to be
proved by structural induction, that there are natural numbers
\(n_\eta,m_\eta\), with \(m_\eta<n_\eta^2\), satisfying two eventual
uniformity conditions:

1. If \(n,n'>n_\eta\), and \(i,i'\) lie at least \(m_\eta\) away from the
   endpoints of the respective gaps between \(n^2,(n+1)^2\) and
   \((n')^2,(n'+1)^2\), then
   \(i\in\bar\eta\) iff \(i'\in\bar\eta\).
2. If \(n,n'>n_\eta\) and \(-m_\eta\le k\le m_\eta\), then
   \(n^2+k\in\bar\eta\) iff \((n')^2+k\in\bar\eta\).

The printed second condition is false. In its own atomic case, choose an even
\(n>2\), an odd \(n'>2\), and \(k=1\). Then
\(n^2+1\in P_0\), because the square index is even, but
\((n')^2+1\notin P_0\). This directly contradicts condition 2 with the
printed choice \(n_\eta=m_\eta=2\). The source nevertheless proceeds by
retaining the bounds for negation, taking maxima for conjunction, using
\((n_\zeta+1,m_\zeta+1)\) for `PAST_1` and symmetrically for `FUTURE_1`, and
using \((n_\zeta+2,0)\) for ordinary `PAST` and `FUTURE` with threshold case
splits. Those cases occupy printed pp. 106--108, PDF pp. 115--117, but they do
not repair the false induction premise.

A valid handbook repair adds \(n\equiv n'\pmod 2\) to condition 2 and leaves
condition 1 unchanged. The atomic case then holds: matching offsets from
squares agree for indices of the same parity. Negation is immediate;
conjunction first enlarges the two offset bounds to a common bound and raises
the threshold so that newly covered offsets fall in the central region
governed by condition 1; immediate past and future translate points by one;
and ordinary strict past and future have eventually constant truth sets. This
corrected induction is supplied in the reader-facing presentation and is not
attributed to Kamp.

The calculated isolation truth sets violate condition 1: their truth in
the long central portions between consecutive squares continues to depend on
which parity block one is in, while the corrected induction makes every `TS'`
formula eventually uniform across all such central portions. Therefore no
`TS'` schema defines either isolation operation. The source's attempted proof
ends on printed p. 108; the conclusion is recovered by the corrected
induction, not by accepting condition 2 as printed.

There is no separately numbered lemma inside Theorem IV.3's proof. Its intended
load-bearing result is the in-proof induction labeled `(1.a)` and `(1.b)`, with
the source defect in `(1.b)` recorded above. Calling a different Chapter IV
lemma the proof of Theorem 3 would falsify the source's dependency structure.

### Surrounding theorems and lemmas

The immediately relevant Chapter IV neighborhood is:

| Locator | Source result | Relationship to IV.3 |
|---|---|---|
| IV.1, printed pp. 95--99 | On the real order \(\mathrm{Re}\), `SINCE` and `UNTIL` are not expressible from sentential connectives and arbitrary monadic \(\mathrm{Re}\)-tenses. | A different arity-separation result; its Lemmas 1--3 do **not** prove IV.3. |
| Definition 1 and Lemma 1, pp. 96--97 | For a source-defined discrete/unbounded real proposition \(P\), every one-input \(\mathrm{TL}_1\) truth set is one of \(\mathbb R,\varnothing,P,\mathbb R\setminus P\); the corollary applies this to any monadic tense. | Establishes the closure invariant used for IV.1. |
| Lemma 2, pp. 97--98 | Describes every member of the Boolean field generated by pairwise disjoint discrete unbounded propositions. | Algebraic closure step for IV.1. |
| Lemma 3, p. 98 | Every formula built from monadic tenses has a truth set in that generated field. | Combines the preceding results for IV.1. |
| IV.2, printed pp. 100--105 | `SINCE` and `UNTIL` are \(\mathrm{In}\)-expressible from \(\mathcal S\). | The positive result whose proposed simplification IV.3 refutes. |
| IV.3, printed pp. 105--108 | `ISOLP` and `ISOLF` are not \(\mathrm{In}\)-expressible from \(\mathcal S'\). | The requested theorem. |
| IV.4, beginning p. 108 | `PAST_1` and `FUTURE_1` are not \(\mathrm{In}\)-expressible from \(\{\mathrm{ISOLP},\mathrm{ISOLF},\mathrm{PAST},\mathrm{FUTURE},\mathrm{NOT},\mathrm{AND}\}\). | The converse irredundancy result. |
| IV.5, printed pp. 109--112 | Some first-order-definable tense on the rational order \(\mathrm{Ra}\) is not expressible from `NOT`, `AND`, `SINCE`, and `UNTIL`. | The later counterexample that must not be relabeled as IV.3. |

Theorem IV.4 uses the periodic input
\(P_0=\{i\in\mathbb Z:i\equiv2\pmod4\}\). Its closure calculation shows that
all formulas from the proposed basis have one of eight periodic truth sets,
whereas `PAST_1(P_0)` and `FUTURE_1(P_0)` have the missing residue classes
\(3\pmod4\) and \(1\pmod4\), respectively.

## Source examples and countermodels that are safe to reconstruct

The thesis supplies several distinct examples. They should not be collapsed
into one generic appeal to temporal intuition.

1. **Compositional expressibility example, printed pp. 15--18.** The binary
   English pattern in which one fact held before another past fact is first
   modeled by a new binary operator and then expressed in \(\mathrm{TL}_0\) as
   a nested strict-past schema. This motivates the formal definition of a
   schema and of expression by primitive tense-functions.
2. **Present progressive, printed pp. 18--19 and 112--117.** The source gives a
   first-order interval-based candidate for the present progressive and proves
   that, on an infinite linear order, it is not expressible using only `PAST`,
   `FUTURE`, and sentential connectives. The concluding proof explicitly
   checks all endpoint configurations.
3. **Real-order monadic separation, IV.1.** Take \(P_0\) to be the even
   integers and \(P_1\) the odd integers as subsets of \(\mathbb R\). Every
   formula built from monadic real-order tenses and Boolean connectives treats
   all noninteger points alike, but `SINCE(q_0,\neg q_1)` separates
   \(+\tfrac12\) from \(-\tfrac12\); the future mirror separates them in the
   opposite direction. This is the endpoint of Lemmas 1--3, not IV.3.
4. **Sparse-square integer separation, IV.3.** The set of squares together
   with the successors of even squares produces the nonperiodic isolation
   profiles recorded above. The source's second uniformity clause is false as
   printed; the same-parity repair recorded above restores the induction while
   leaving the parity-independent central-gap separation intact.
5. **Modulo-four integer separation, IV.4.** A single residue-class predicate
   distinguishes immediate-neighbor tenses from the Boolean field closed under
   ordinary past/future and the isolation tenses.
6. **Rational-order separation, IV.5.** Kamp constructs two subsets \(Q,Q'\)
   of the rationals from periodic intervals whose endpoints involve
   \(\sqrt2\), with \(Q'\) modified by a sequence converging to that irrational
   cut. A displayed first-order tense-defining formula is true at the rational
   point 3 in one interpretation and false there in the other. A structural
   induction shows that every one-input \(\mathrm{TL}_1\) formula has the same
   truth value at 3 in both interpretations. Hence the four-operator `Com`
   basis is not complete on \(\mathrm{Ra}\) ([printed pp. 109--112; PDF
   pp. 118--121](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf#page=118)).

The rational example is especially important for the proof boundary: the
forward temporal-to-first-order translation remains valid, but the converse
cannot be extended from `Com` to all `Lin` merely by repeating the same four
operators.

## Qualifications and safe handbook consequences

- **Do not state the theorem for arbitrary linear orders.** The central
  first-order-to-temporal theorem is a `Com` theorem. The rational order is the
  source's own counterexample to extending this operator basis naively.
- **Do not add density or endpointlessness.** `Com` permits discrete orders,
  finite orders, and orders with endpoints. The proof and the later endpoint
  case split confirm this.
- **Do not reverse the `S`/`U` arguments.** The first argument holds at the
  strict witness; the second holds throughout the strictly intermediate open
  interval.
- **Do not add equality to \(L\) silently.** It is absent from the displayed
  first-order vocabulary.
- **Do not call Theorem IV.3 the rational countermodel.** IV.3 is the
  `ISOLP`/`ISOLF` non-expressibility theorem over integers; rational failure is
  IV.5.
- **Do not turn expression into axiomatization.** The main proof is an
  effective semantic translation/normal-form theorem, not a soundness and
  deductive-completeness theorem for a calculus.
- **Do not read `all tenses` as all set-functions.** From Chapter II onward,
  the unqualified word is restricted to first-order-definable tenses.
- **Do not generalize from every English tense expression.** Printed p. 29
  gives `mostly` and `usually` as tense-like expressions whose meanings
  essentially involve a measure on time and hence fall outside the thesis's
  first-order-definable class.
- **Preserve proof granularity and defects.** The main Chapter III argument is
  supplied in the thesis. The IV.3 induction is also printed, but its second
  invariant is false without the same-parity premise, so the handbook must
  distinguish the source proof attempt from its supplied repair. Elsewhere
  some symmetric or routine subcases are abbreviated; for example, IV.2 proves
  the future case in detail and invokes symmetry for the past case, while IV.5
  leaves elementary Boolean induction steps to the reader.

## Evidentiary closure table

| Requested field | Disposition | Direct source location |
|---|---|---|
| Exact identity and lawful readable body | **CLOSED** | Stuttgart bibliography; title/approval leaves; live institutional PDF |
| Stable URL and access provenance | **CLOSED** | bibliography's file link, HTTP-to-HTTPS redirect, live `200 application/pdf` response |
| Pagination | **CLOSED** | PDF pp. 1--128; printed body pp. 1--119; chapter map above |
| Order classes and endpoint assumptions | **CLOSED** | Chapter I pp. 12--14; Chapter IV pp. 113--117 |
| First-order language and assignment convention | **CLOSED** | Chapter II Definitions 2--3, pp. 21--22 |
| Operators and satisfaction clauses | **CLOSED** | Chapter I semantics; Chapter II pp. 25--26; Chapter III pp. 41--42, 57--58 |
| Both translation directions | **CLOSED** | Chapter III pp. 39--94 |
| Exact Chapter IV Theorem 3 | **CLOSED** | printed pp. 105--108, PDF pp. 114--117 |
| Surrounding lemmas/results | **CLOSED** | Chapter IV Lemmas 1--3 and Theorems 1--5, pp. 95--112 |
| Source examples/countermodels | **CLOSED** | pp. 15--19 and Chapter IV pp. 95--117 |
| Completeness/referral caveats | **CLOSED** | Chapter II pp. 27--29; Chapter III proof boundary; Chapter IV counterexamples |

The acquisition and source-audit disposition for `N-c-012.a` is therefore
**CLOSED**. The remaining work, if authorized in a later phase, is reader-facing
reconstruction and independent review, not source recovery.

# Craig, Robinson, and Beth: exact implications and the private-vocabulary gap

Date: 2026-09-06.

## Conclusion

The active three-way equivalence should be replaced by

\[
 \text{Craig interpolation}\quad\Longleftrightarrow\quad
 \text{Robinson joint consistency},
 \qquad
 \text{either implies ordinary Beth definability}.
 \tag{1}
\]

The equivalence here uses first-order compactness in passing between
sentence interpolation and joint consistency for arbitrary theories.
The proposed zero-ary construction does not derive common-vocabulary
interpolation from the ordinary Beth theorem defined in the manuscript.
It needs **projective Beth definability**, which permits eliminating
additional private symbols besides the symbol being defined. Section 4
below gives the valid construction under that stronger hypothesis and
pinpoints why the present use of ordinary Beth does not suffice.

All three theorems are true in classical first-order logic. That fact is
not a demonstration that their properties are interchangeable principles.
In particular, this finding is not a countermodel to the first-order Beth
theorem or to first-order Craig interpolation. It concerns the asserted
implication between the stated principles and the claimed construction.

## 1. Actual manuscript and register scope

The checked text is
`handbook/parts/p03/preservation-abstract-logic.tex`:

- `def:p03-implicit-explicit-definability`, lines 254-269 at review time,
  fixes a theory `T` in **exactly** `L union {P}`. Implicit definability
  compares models with the same full `L`-reduct; the explicit definition
  must use that `L`.
- `thm:p03-beth-definability`, lines 272-275, asserts ordinary Beth for
  that definition.
- `thm:p03-craig-robinson-beth`, lines 277-280, calls Craig, Robinson,
  and this Beth property equivalent metatheorem principles.
- Lines 290-295 attribute the reverse implication to a zero-ary marker,
  renamed private copies, and their subsequent removal from the explicit
  definition, without stating an elimination lemma.

The first 100 lines of `handbook/annex/p03/editorial-proofs.tex` contain
the model-theoretic Robinson proof and the ordinary two-copy proof of
Beth **from Robinson**. They contain no Beth-to-Craig proof. In the Beth
argument only the symbol being defined is copied; the common vocabulary
is the whole old language plus fresh tuple constants, as ordinary Beth
requires.

The actual row `N-a-013` at `spec/registers/new-content.csv:14` requests
Robinson joint consistency and Beth with model-theoretic proofs, followed
by equivalence with Craig interpolation. Its wording is consistent with
the standard Craig-Robinson equivalence and the consequent Beth theorem.
It does not require replacing ordinary Beth by a stronger projective
property or asserting an unproved three-way equivalence.

## 2. Source evidence and access boundary

The following primary author texts were read at the relevant passages.

1. **Saharon Shelah, *Remarks in abstract model theory*, Annals of Pure
   and Applied Logic 29 (1985), 255-288.** The
   [author-hosted published scan](https://shelah.logic.at/files/95416/199.pdf),
   Section 6, printed pp. 273-277, explicitly constructs a compact proper
   extension of first-order logic with the Beth property but without
   Craig interpolation. Conclusion 6.11(2) states compactness and Beth;
   6.11(4) states failure of interpolation. The introduction on p. 256
   also distinguishes the properties even for compact logics. This is
   direct primary evidence against an unrestricted identification of
   ordinary Beth and Craig, even after compactness is added.

2. **Eva Hoogland, Maarten Marx, and Martin Otto, *Beth definability in
   the Guarded Fragment*.** The
   [authors' 25 May 1999 text](https://festschriften.illc.uva.nl/j50/contribs/hoogland/hoogland.pdf)
   states in its abstract and introduction that guarded interpolation
   fails while ordinary Beth holds. Theorem 4.1 and Corollary 4.3,
   printed pp. 11-13, establish Beth with a language `L=L_0 union {R}`,
   the same vocabulary shape as the manuscript's definition. This
   separates those logical properties; it is not a claim that the guarded
   fragment is the full first-order language.

3. **Wilfrid Hodges, *Classical Logic I: First-Order Logic*.** The
   [author's chapter available from Waterloo](https://cs.uwaterloo.ca/~david/cl/fol-hodges),
   printed p. 31, gives Craig interpolation as Corollary 1.11 and
   explicitly derives Beth as Corollary 1.12. The latter compares models
   differing only on the defined relation. This is an author exposition
   of the forward implication, not a reading of the separately cited
   1993 book.

4. **Solomon Feferman, *Harmonious Logic: Craig's Interpolation Theorem
   and its Descendants*.** The
   [author's paper](https://math.stanford.edu/~feferman/papers/harmonious.pdf),
   Section 2, printed pp. 5-7, gives the Craig-to-Beth argument and
   discusses the Craig-Robinson equivalence. It identifies Robinson's
   1963 book, pp. 114-117, as an early published proof of that equivalence.
   The paper distinguishes this from Beth's theorem and later surveys
   Shelah's compact Beth-without-Craig example on p. 19.

5. **William Craig, 1957.** The
   [publisher's accessible original introduction](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/three-uses-of-the-herbrandgentzen-theorem-in-relating-model-theory-and-proof-theory/7674DE501824D8FC294FB396CD5617DB)
   describes applying Herbrand-Gentzen methods to generalize Beth's work
   from primitive predicates to formulas and terms. The full 1957 article
   was not acquired in this bounded pass. The accessible introduction
   does not establish the manuscript's claimed reverse construction.

The attempted publisher access to Beth's 1953 paper returned HTTP 403.
The full body of *Hodges 1993* was not acquired. Consequently this note
does not invent page citations for those works or claim a full negative
search of their contents. The defect is independently identified by the
vocabulary calculation below, and the distinction of principles is
positively established by the primary research sources above.

## 3. The legitimate Craig-Robinson-Beth route

Take compatible signatures `L_1,L_2` and `L_0=L_1 intersect L_2`.
Equality is logical, and logical true/false are available.
Use the sentence version of Craig here. The open-formula version follows
by the fresh-constant argument already supplied in Part VII.

### Craig implies Robinson joint consistency

Suppose consistent theories `T_i` have inconsistent union. By compactness,
finite conjunctions `A` from `T_1` and `D` from `T_2` satisfy
`A |= not D`. Craig gives an `L_0` sentence `C` with

\[
 A\models C,\qquad C\models\neg D.
 \tag{2}
\]

Hence `T_1 |= C` and `T_2 |= not C`, which is the required separating
sentence. Contraposition proves the manuscript's no-separating-sentence
version of joint consistency. Completeness identifies these semantic
consequences with its derivability notation.

### Robinson joint consistency implies Craig

Suppose `A |= B`. If `A` is inconsistent, take `C=bottom`. If `B` is
valid, take `C=top`. Otherwise `{A}` and `{not B}` are consistent
theories with inconsistent union. Contraposition of joint consistency
gives an `L_0` sentence `C` such that

\[
 A\models C,\qquad\neg B\models\neg C.
 \tag{3}
\]

The second clause is equivalent to `C |= B`. This is Craig interpolation.
The two degenerate cases are needed because the stated joint-consistency
theorem assumes that its component theories are consistent.

### Robinson, hence Craig, implies ordinary Beth

Let `T` be in `L union {P}` and implicitly define `P`. Copy `P` to
fresh `P'`, obtaining `T'`, and add fresh tuple constants `bar c`.
The theories `T union {P(bar c)}` and `T' union {not P'(bar c)}` have
inconsistent union by implicit definability. Their common language is
`L(bar c)`. The separating sentence `C(bar c)` gives

\[
 T\models P(\bar c)\to C(\bar c),\qquad
 T'\models C(\bar c)\to P'(\bar c).
 \tag{4}
\]

Rename `P'` back, replace the fresh constants by fresh variables, and
universally close. This gives the explicit `L`-definition. If one of
the two component theories is inconsistent, falsehood or truth gives
the corresponding definition. This is the direction already proved
in the actual annex.

## 4. What the zero-ary marker construction really requires

Let `A` be an `L_1` sentence, let `B` be an `L_2` sentence, and suppose
`A |= B`.
Separate their common symbols `L_0` from the disjoint private symbol
sets `U=L_1 \ L_0` and `W=L_2 \ L_0`. Introduce a fresh zero-ary
predicate `q` and the sentence

\[
 H(q,U,W)=(q\land A)\lor(\neg q\land\neg B).
 \tag{5}
\]

This is a legitimate first-order sentence. In fact,

\[
 H\models(q\leftrightarrow A),\qquad
 H\models(q\leftrightarrow B).
 \tag{6}
\]

To check the first identity, `q` forces `A`; and if `A` held with
`not q`, (5) would force `not B`, contradicting `A |= B`. The second
identity is analogous. Thus `H` implicitly defines `q` over the full
old language `L_1 union L_2`, and ordinary Beth may return **A itself**
as its explicit definition. Nothing in that application requires the
definition to omit `U` or `W`.

Renaming private symbols into additional copies does not fix this:
under the manuscript's definition, every non-q symbol in the theory is
part of the old language available to the Beth definition. Finiteness
of the private vocabulary does not supply first-order elimination of
its predicates or functions. Quantifying predicate or function symbols
would be second-order quantification. Quantifying individual variables
can remove constant parameters in suitable cases, but it does not
remove arbitrary predicate symbols.

Here is the stronger property for which the construction is valid.
**Projective Beth definability** permits a theory in `L_0 union U union
W union {q}` and assumes uniqueness of `q` when only the `L_0`-reduct
is fixed, while `U,W` are allowed to vary. It then demands an explicit
definition using `L_0` alone.

Sentence (5) does satisfy that stronger uniqueness condition. Suppose
two models of `H` have the same `L_0`-reduct but disagree on `q`.
The model with `q=true` supplies an `L_1` expansion satisfying `A`;
the other supplies an `L_2` expansion satisfying `not B`. Combine
these interpretations on their common domain: the private vocabularies
are disjoint and their common interpretations already agree. This gives
a model of `A and not B`, a contradiction.

Projective Beth therefore supplies an `L_0` sentence `C` with
`H |= (q iff C)`. Every model of `A` can be expanded arbitrarily on
`W` and with `q=true` to a model of `H`; hence `A |= C`.
Every model of `not B` can be expanded arbitrarily on `U` and with
`q=false`; hence `not B |= not C`, so `C |= B`. This is the desired
interpolant. Empty cases cause no difficulty, and unused functions or
constants can be interpreted arbitrarily on the nonempty domain.

Conversely, Craig supplies projective Beth by copying **all** symbols
outside `L_0`, including the relation being defined, in the two-copy
argument. The only shared vocabulary is then `L_0` and the tuple
parameters. Compactness handles an infinite theory. Thus the reverse
marker argument belongs to a projective strengthening, not to the
ordinary Beth theorem stated in the manuscript.

## 5. Why first-order truth does not rescue the claimed equivalence

Because Craig and Beth are independently true in full first-order
logic, their material biconditional is true in any metatheory that
already proves them both. That observation contains no reduction of
one definability principle to the other and does not justify the
specific private-symbol elimination step in the reader.

Shelah's compact proper-extension example shows that compactness plus
ordinary Beth, considered as logical properties, does not generally
give Craig. The guarded-fragment example gives a second distinction
within first-order syntax. These examples are used for exactly that
purpose; they are not misdescribed as countermodels to first-order
Craig or Beth themselves.

One could deliberately strengthen the manuscript's definition to
projective Beth and then prove the expanded equivalence using Section 4.
That would change the stated principle and needs its own definition
and proof. The bounded correction that preserves the present Beth
definition is (1).

## 6. Exact recommended manuscript correction

At `thm:p03-craig-robinson-beth`, replace the three-way assertion by:

> For classical first-order logic, Craig interpolation and Robinson
> joint consistency are interderivable, using compactness for arbitrary
> theories. Either principle yields Beth definability.

Keep the two legitimate implication arguments, including their
degenerate cases, and the existing annex proof of Robinson-to-Beth.
Replace the paragraph beginning with the purported reverse
Beth-to-Craig construction by a direct statement that the annex's
model-theoretic Beth proof follows from Robinson, while the
Craig-Robinson equivalence connects it to interpolation.

The rejected marker/private-copy argument and its projective repair
belong in this provenance note, not as an error followed by a warning
in the reader exposition. No register expansion or new abstract-logic
equivalence is necessary for `N-a-013`.

Only this note was created. The task made no manuscript edits, ran
no software tests, builds, or renders, and started no additional agents.

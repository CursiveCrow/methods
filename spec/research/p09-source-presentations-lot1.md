# Part IX source presentations, lot 1: register rows `N-c-001`--`N-c-008`

**Status:** source-acquisition record, not manuscript prose. The record covers all
twenty-one semicolon-delimited presentations in register rows `N-c-001` through
`N-c-008`. A later exposition is treated as its own presentation, never as an
unmarked surrogate for an inaccessible original.

Retrieved and checked: 2026-08-22 (America/Los_Angeles).

## Method and anti-hybridization rule

For each registered authority, this note separates (i) bibliographic identity,
(ii) the exact copy actually inspected, (iii) source notation and scope, (iv) the
strongest result that copy supports, (v) the proof boundary, (vi) examples and
qualifications, and (vii) what a reader-facing reconstruction must contain. A
DOI or catalog record establishes identity; it does not establish theorem text.
Where the registered edition or original article was not acquired at theorem-text
level, the missing fields are called an **acquisition gap**. They must not be filled
by silently importing a later book's formulation, notation, bound, or proof.

The twenty-one presentations are counted by register occurrence, not by distinct
physical work: Libkin 2004 has separate foundations, locality, and zero--one-law
presentations; Börger--Grädel--Gurevich 1997 has separate prefix-class and monadic
presentations. These are reconstructed separately below.

## Acquisition ledger

| Row and authority | Exact technical copy inspected | Acquisition condition |
|---|---|---|
| `N-c-001`, Ebbinghaus--Flum 1995 | first-edition metadata only | first-edition theorem text not acquired |
| `N-c-001`, Libkin 2004 | author-hosted complete book PDF | acquired |
| `N-c-002`, Glebskii et al. 1969 | DOI/bibliographic records only | original theorem text not acquired |
| `N-c-002`, Fagin 1976 | author-hosted article PDF | acquired |
| `N-c-002`, Libkin 2004 | author-hosted complete book PDF | acquired |
| `N-c-003`, Hanf 1965 | publisher identity/abstract only | chapter text not acquired |
| `N-c-003`, Gaifman 1982 | institutional record and abstract only | article text not acquired |
| `N-c-003`, Libkin 2004 | author-hosted complete book PDF | acquired |
| `N-c-004`, Fagin 1974 | author-hosted article PDF | acquired |
| `N-c-004`, Vardi 1982 | author-uploaded extended-abstract scan | acquired, extended-abstract proof boundary |
| `N-c-004`, Immerman 1986 | author-hosted article PDF | acquired |
| `N-c-004`, Immerman 1999 | author-hosted corrected chapter samples | Fagin chapter acquired; fixed-point chapter not acquired |
| `N-c-005`, Lewis 1979 | catalog/preview metadata only | book text not acquired |
| `N-c-005`, Börger--Grädel--Gurevich 1997 | author-hosted complete book PDF | acquired |
| `N-c-006`, Mortimer 1975 | DOI/bibliographic record only | article text not acquired |
| `N-c-006`, Grädel--Kolaitis--Vardi 1997 | complete article PDF plus DOI record | acquired |
| `N-c-007`, Andréka--van Benthem--Németi 1998 | institutional 1996 preprint; journal identity record | technical manifestation differs from registered journal manifestation |
| `N-c-007`, Grädel 1999 | author-hosted article preprint and journal DOI record | acquired |
| `N-c-008`, Löwenheim 1915 | EUDML identity record; scan retrieval failed | original theorem text not acquired |
| `N-c-008`, Behmann 1922 | Göttingen scan, not text-searchable | scan acquired but exact theorem transcription blocked |
| `N-c-008`, Börger--Grädel--Gurevich 1997 | author-hosted complete book PDF | acquired |

---

## `N-c-001`: finite-model foundations

### Presentation 1 of 21: Ebbinghaus--Flum 1995

**Identity and access.** The registered work is Heinz-Dieter Ebbinghaus and
Jörg Flum, *Finite Model Theory*, Springer, 1995, Perspectives in Mathematical
Logic, xv + 327 pages, ISBN `3-540-60149-X`; the first-edition identity is
corroborated by the [DBLP book record](https://dblp.org/rec/books/daglib/0082516)
and [Google Books record](https://books.google.com/books?id=u3RQAAAAMAAJ).
The current Springer DOI landing page, [10.1007/3-540-28788-4](https://doi.org/10.1007/3-540-28788-4),
is for the enlarged 2005 second edition (xi + 360 pages), not a paginated copy
of the registered 1995 edition.

**What was and was not acquired.** Searchable first-edition theorem text was
not acquired. Available preview fragments identify chapter-level matter such as
“A Microcosm” and “Satisfiability in the Finite,” but they do not expose enough
continuous text to verify the source's exact definitions, theorem numbering,
hypotheses, proof boundaries, examples, or the location and strength of its
finite Craig/Beth discussion. Metadata and snippets therefore do **not** license
a technical reconstruction of the 1995 presentation. The second edition's DOI
cannot be used to assign 2005 theorem numbers or pagination to the 1995 book.

**Acquisition gap and reader-facing condition.** Before this presentation can
be written, acquire the 1995 first edition at least for the passages covering:
the chosen finite-structure convention; the finite failures of compactness and
completeness; finite Craig interpolation and Beth definability; the book's finite
Ehrenfeucht--Fraïssé formulation; and its statement/proof or recap of
Trakhtenbrot's theorem. Transcribe its own notation, vocabulary restrictions,
theorem strength, examples, and proof status. The Libkin presentation below may
be cross-referenced as a later account, but none of its exercise assignments,
proofs, or locators may be attributed to Ebbinghaus--Flum 1995.

### Presentation 2 of 21: Libkin 2004 (foundations presentation)

**Identity, copy, and controlling locators.** Leonid Libkin, *Elements of
Finite Model Theory*, Springer, 2004, DOI
[10.1007/978-3-662-07003-1](https://doi.org/10.1007/978-3-662-07003-1).
The technical copy inspected is the author's [complete book PDF](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf),
also linked from the [author's book page](https://www.cs.toronto.edu/~libkin/fmt/).
The controlling passages are Chapter 3, especially Proposition 3.2 on printed
pages 24--25, Corollary 3.19 and Proposition 3.20 on pages 37--39, and Exercises
3.12--3.13 on pages 41--42; and Chapter 9, Definition 9.1 and Theorem 9.2 on
pages 165--168, Corollaries 9.3--9.4 on pages 165--166, and the machine-encoding
proof on pages 166--174. [The complete author PDF contains all of these locators.](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf)

**Source language, structures, and definitions.** The presentation works with
finite structures for a vocabulary `σ`; `STRUCT[σ]` is the class of such
structures. Proposition 3.2 takes the empty vocabulary and lets `λ_n` assert
that at least `n` distinct elements exist; `T = {λ_n : n ≥ 0}` is the witness
theory. Definition 9.1 calls a sentence *finitely satisfiable* when some finite
`σ`-structure satisfies it and *finitely valid* when every finite `σ`-structure
satisfies it. These definitions and the displayed `λ_n` formula must precede
the metatheoretic conclusions. [Libkin, pp. 24--25 and 165.](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf)

**Exact strength.** Proposition 3.2 proves failure of compactness over finite
models: `T` has no finite model although every finite subset of `T` has a finite
model. Theorem 9.2 (Trakhtenbrot) says that for **every relational vocabulary
containing at least one binary relation symbol**, finite satisfiability of
sentences is undecidable. Corollary 9.3 strengthens the finite-completeness
consequence: for such a vocabulary, the finitely valid sentences are not
recursively enumerable. Corollary 9.4 rules out a recursive function bounding
the size of a finite model in terms of a finitely satisfiable sentence. The proof
temporarily uses several binary relations and a constant; the book explicitly
assigns the coding down to one binary relation to Exercise 9.1. [Libkin,
pp. 165--168.](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf)

**Proof boundary.** The compactness counterexample is fully proved in place.
The finite satisfiability theorem receives a substantial Turing-machine/grid
encoding proof: finite models encode an initial segment of a computation and
the converse extraction is checked. The one-binary-relation compression is not
proved in the main text. Most importantly, finite Beth failure and finite Craig
failure are **Exercises 3.12 and 3.13**, with prompts/hints rather than completed
book proofs; a reconstruction must not claim that Libkin supplies full proofs
there. [Libkin, pp. 41--42 and 166--174.](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf)

**Examples and qualifications.** Corollary 3.19 gives finite graph connectivity
as a non-FO property, and Proposition 3.20 treats being a finite tree; these sit
after the book's finite Ehrenfeucht--Fraïssé development and show how game
equivalence yields finite inexpressibility. They are examples, not substitutes
for the computability-theoretic strength of Trakhtenbrot's theorem. The failure
of ordinary completeness is not merely “there is no convenient calculus”:
non-recursive-enumerability of finite validity rules out any effective sound and
complete proof system for finite validity. [Libkin, pp. 37--40 and 165--166.](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf)

**Difference from Ebbinghaus--Flum and owed reconstruction.** This is a later,
explicitly pedagogical route: an elementary finite-compactness witness, finite
games and graph examples, exercise-level Craig/Beth failures, and then a full
machine encoding. The reader-facing text must reproduce that division of labor:
define finite satisfaction/validity, give the `λ_n` proof, state which Craig/Beth
items remain exercises, state the binary-vocabulary hypothesis exactly, outline
both directions of the computation encoding, and derive non-r.e. finite validity.
It must not use inaccessible Ebbinghaus--Flum wording to “complete” the exercises.

---

## `N-c-002`: zero--one laws, extension axioms, and the random graph

### Presentation 3 of 21: Glebskii--Kogan--Liogon'kii--Talanov 1969

**Identity.** Yu. V. Glebskii, D. I. Kogan, M. I. Liogon'kii, and V. A.
Talanov, “Range and Degree of Realizability of Formulas in the Restricted
Predicate Calculus,” Russian original in *Kibernetika* 1969, no. 2, 17--27;
English translation in *Cybernetics* 5, 142--154. The stable article identity
is [DOI 10.1007/BF01071084](https://doi.org/10.1007/BF01071084).

**Acquisition gap.** No primary full text was acquired. Consequently, this
record does not infer from Fagin 1976 or Libkin 2004 the original paper's exact
probability space, vocabulary restrictions, “degree of realizability” notation,
theorem statement, proof organization, or examples. Later authoritative
bibliographies report that the paper independently proves the first-order
zero--one law by a proof different from Fagin's, but that later report cannot
establish the original's exact presentation. The DOI establishes identity only.

**Reader-facing condition.** Acquire either the Russian pages 17--27 or the
English translation pages 142--154, then transcribe: the finite models and
probability measure; whether equality, constants, and functions are admitted;
the exact limiting assertion; all auxiliary extension or consistency conditions;
the proof's probability estimate and model-theoretic step; and any examples or
counterexamples. Until then, the manuscript may identify the independent 1969
priority and the acquisition gap, but may not present Fagin's complete-theory
argument under the four authors' names.

### Presentation 4 of 21: Fagin 1976

**Identity, copy, and locators.** Ronald Fagin, “Probabilities on Finite
Models,” *Journal of Symbolic Logic* 41 (1976), 50--58, DOI
[10.2307/2272945](https://doi.org/10.2307/2272945) (also publisher DOI
`10.1017/S0022481200051756`). The inspected copy is Fagin's
[author-hosted PDF](https://s3.us.cloud-object-storage.appdomain.cloud/res-files/500-jsl76.pdf),
listed on his [publication page](https://ronfagin.com/papers/). Controlling
locators are §1 p. 50; §2 pp. 51--53, Theorems 1, 2, and 4 and Corollaries
3, 5, and 6; §3 pp. 54--55, Theorem 9; and §4 pp. 55--57, Theorem 10 and
the counterexamples.

**Source notation and hypotheses.** For a finite relational vocabulary `Y`,
`A_n(Y)` is the set of `Y`-structures with universe `{1,...,n}` and `p_n(σ)`
is the fraction satisfying the sentence `σ`. The main theorem assumes equality
but no function or constant symbols. In §2 a *complete open description*
`M(x_1,...,x_m)` fixes all equality and relational atomic facts on a distinct
tuple. An extension formula `N(x_1,...,x_m,y)` specifies every atomic relation
involving a new point `y`; the theory `T` contains the corresponding extension
axiom for every pair `M,N`. [Fagin, pp. 50--51.](https://s3.us.cloud-object-storage.appdomain.cloud/res-files/500-jsl76.pdf)

**Exact strength.** Theorem 1, attributed there to Gaifman, says `T` is
consistent and complete. Theorem 2 says every sentence in `T` has limiting
probability one. Corollary 3 identifies the almost-sure theory: `T ⊨ σ` iff
`p_n(σ) → 1`. Theorem 4 then gives the zero--one law for every first-order
sentence over the stated relational vocabulary: its labeled finite-model
probability tends to zero or one. Corollary 5 says each finite subset of `T`
has models of every sufficiently large finite cardinality; Corollary 6 says the
spectrum of any first-order sentence, now allowing eliminated constants and
functions for this corollary, is either finite or cofinite. [Fagin,
pp. 51--53.](https://s3.us.cloud-object-storage.appdomain.cloud/res-files/500-jsl76.pdf)

Section 3 changes from labeled `A_n` to representatives `B_n` of isomorphism
types and defines the unlabelled proportion `v_n`. Theorem 9 proves that its
limit exists and agrees with the labeled limit for the relational first-order
case. This is a second asymptotic convention and must not be suppressed.
[Fagin, pp. 54--55.](https://s3.us.cloud-object-storage.appdomain.cloud/res-files/500-jsl76.pdf)

**Proof boundary.** Theorem 1 receives a compact model-theoretic sketch:
extension axioms give a back-and-forth uniqueness result for countable models;
categoricity plus the Łoś--Vaught test yields completeness. Theorem 2 has a
displayed counting/independence estimate in the binary-relation case and says
the finite relational generalization is clear. Theorem 4 is then a short
completeness dichotomy. The unlabelled theorem has its own asymptotic proof.
This is more than a bare theorem citation but less than a modern, fully expanded
pedagogical proof of every general-vocabulary estimate. [Fagin, pp. 51--55.](https://s3.us.cloud-object-storage.appdomain.cloud/res-files/500-jsl76.pdf)

**Counterexamples and qualifications.** Section 4 shows that second-order
sentences need not even have a limiting probability. It also shows why the
relational/no-constant hypothesis is material: with a unary predicate `U` and
constant `c`, `Uc` has limit `1/2`; for a unary function, the sentence saying
there is no fixed point has limit `1/e`. Theorem 10 obtains geometric convergence
for labeled probabilities, and for unlabelled probabilities only in the
nonmonadic case; in a unary-predicate example the unlabelled probability of
`∀x Ux` is `1/(n+1)`, hence not geometrically convergent. [Fagin,
pp. 55--57.](https://s3.us.cloud-object-storage.appdomain.cloud/res-files/500-jsl76.pdf)

**Difference and owed reconstruction.** Unlike an account built around one
named random graph, Fagin formulates a complete extension-axiom theory for an
arbitrary finite relational vocabulary, then separately controls labeled and
unlabelled measures. The reader-facing text owes the finite probability spaces,
the open-description/extension schema, the categorical-completeness sketch, the
explicit probability estimate, and the function/constant counterexamples. It
must not retroactively call the distinguished countable model `RG` or import
Libkin's `BIT` construction into Fagin's notation.

### Presentation 5 of 21: Libkin 2004 (zero--one/random-graph presentation)

**Identity and locators.** This is Chapter 12, “Zero-One Laws,” printed
pages 235--248, of Libkin's [author-hosted complete book PDF](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf),
DOI [10.1007/978-3-662-07003-1](https://doi.org/10.1007/978-3-662-07003-1).
The controlling items are Definition 12.1 and Theorem 12.2 on p. 237;
Corollary 12.3 pp. 237--238; extension formula (12.2) and Proposition 12.4
pp. 238--239; Lemma 12.7 p. 240; the arbitrary-vocabulary extension schemas
pp. 240--241; Definition 12.8 and Theorem 12.9 pp. 241--242; and
Corollaries 12.10--12.11 p. 242.

**Source notation and definitions.** For a class `C` of finite `σ`-structures,
`μ_n(C)` is the uniform proportion among structures whose universe is
`{0,...,n-1}`, and `μ(C)` is its limit when it exists. Definition 12.1 says a
logic has the zero--one law when every definable Boolean query has limiting
probability `0` or `1`. For graphs, `EA_{n,m}` says that for every two disjoint
sets of respectively `n` and `m` vertices there is a fresh vertex adjacent to
all of the first and none of the second; `EA_k` is the bounded collection needed
at rank/variable level `k`, and `EA` is the full extension-axiom theory.
[Libkin, pp. 235--241.](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf)

**Exact strength and proof.** Proposition 12.4 proves `μ(EA_k)=1` using a
union bound over choices of the two sets and the exponentially small probability
that no witness exists. Lemma 12.7 uses the extension axioms to give Duplicator
a winning `k`-pebble strategy. Completeness of first-order types at each fixed
rank then proves Theorem 12.2, stated for `L^ω_{∞ω}`, and Corollary 12.3 gives
the zero--one law for FO, LFP, IFP, and PFP. The text extends the graph schema
to arbitrary purely relational vocabularies by complete atomic descriptions.
[Libkin, pp. 237--241.](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf)

Definition 12.8 presents the countable random graph `RG` on `ℕ`, with adjacency
defined from the binary `BIT` relation. Theorem 12.9 says that `EA` is complete,
`ω`-categorical, and decidable; the proof gives a countable back-and-forth for
uniqueness, invokes Löwenheim--Skolem/completeness, and turns recursive axioms
plus completeness into decidability. Corollary 12.10 identifies `RG ⊨ Φ` with
`μ(Φ)=1`, and Corollary 12.11 makes the almost-sure theory decidable.
[Libkin, pp. 241--242.](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf)

**Examples, counterexamples, and scope.** Absence of isolated vertices and
graph connectivity have asymptotic probability one, although connectivity is
not FO-definable. Even cardinality has no limiting truth probability, and unary
predicate parity has limit `1/2`; these witness the distinction between merely
having a limit and satisfying a zero--one law. Adding an order destroys the
corollary: `LFP+<` defines even cardinality. The text's zero--one theorem is for
the uniform labeled model and purely relational vocabularies. [Libkin,
pp. 235--238.](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf)

**Difference and owed reconstruction.** Libkin reorganizes the historical
result as an EF/pebble-game proof and then concretizes the almost-sure theory in
one computable random graph. The reader-facing presentation must include the
measure, extension-axiom syntax, the union-bound estimate, the game lemma, the
`BIT` model and back-and-forth proof, plus the order qualification. It must not
attribute this `RG` construction or `L^ω_{∞ω}` packaging to either 1969 or 1976.

---

## `N-c-003`: Hanf and Gaifman locality

### Presentation 6 of 21: Hanf 1965

**Identity.** William Hanf, “Model-Theoretic Methods in the Study of
Elementary Logic,” in J. W. Addison, L. Henkin, and A. Tarski (eds.),
*The Theory of Models*, North-Holland, 1965, pp. 132--145, DOI
[10.1016/B978-0-7204-2233-7.50020-4](https://doi.org/10.1016/B978-0-7204-2233-7.50020-4);
the publisher's article record is on
[ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/B9780720422337500204).

**Acquisition gap.** The chapter itself was not acquired: the publisher record
exposes bibliographic metadata and an abstract, not the locality lemma's text.
Therefore this note does not assert the original chapter's notation, exact
definition of neighborhoods/local finiteness, internal theorem number, proof
details, or examples. Those fields require pages 132--145. In particular, the
finite bounded-degree threshold theorem often called “Hanf's theorem” in later
finite-model texts must not be imputed to the 1965 chapter.

**Primary provenance guard from Fagin--Stockmeyer--Vardi 1995.** A separate
primary paper makes the source-role distinction explicit. In §4, pp. 83--85,
Fagin, Stockmeyer, and Vardi define rooted `d`-neighborhood types and
`(d,m)`-equivalence (text-extraction lines 469--503), and prove Theorem 4.3
(lines 538--616): for `r,f>0`, there are `d,m>0`, with `d` dependent only on
`r`, such that finite structures of degree at most `f` that are
`(d,m)`-equivalent are `r`-round EF-equivalent. Their proof chooses
`d=3^(r-1)` and `m=r f^(d-1)` and maintains an isomorphism of shrinking unions
of matched neighborhoods. Corollary 4.4 is at lines 617--624. [Fagin--Stockmeyer--Vardi,
“On Monadic NP vs. Monadic co-NP,” primary author PDF.](https://s3.us.cloud-object-storage.appdomain.cloud/res-files/500-infcom95.pdf)

Immediately afterward, Lemma 4.5 labels Hanf's original result as an **infinite,
locally finite elementary-equivalence criterion**: for every radius and rooted
neighborhood type, the two structures have the same finite number of realizers
or both have infinitely many. The authors expressly say that their finite
bounded-degree theorem and Hanf's lemma do not directly imply one another, and
that the original elementary-equivalence statement is not useful by itself for
finite structures because elementarily equivalent finite structures are
isomorphic (text-extraction lines 625--652). [Fagin--Stockmeyer--Vardi,
§4, pp. 84--85.](https://s3.us.cloud-object-storage.appdomain.cloud/res-files/500-infcom95.pdf)

**Reader-facing condition.** The manuscript may use the 1995 passage only as
a provenance warning, not as a replacement “Hanf 1965 presentation.” A genuine
Hanf subsection still requires acquisition of pp. 132--145 and must separately
state the original locally finite, exact-finite-or-both-infinite hypothesis and
proof in Hanf's notation. Any finite threshold-counting/EF theorem must be
credited to the later source actually used.

### Presentation 7 of 21: Gaifman 1982

**Identity and verified public description.** Haim Gaifman, “On Local and
Non-Local Properties,” in *Logic Colloquium '81*, Studies in Logic and the
Foundations of Mathematics 107, North-Holland, 1982, pp. 105--135, DOI
[10.1016/S0049-237X(08)71879-2](https://doi.org/10.1016/S0049-237X(08)71879-2).
The [Hebrew University institutional record](https://cris.huji.ac.il/en/publications/on-local-and-non-local-properties/)
identifies the work and summarizes its central result: a natural metric on a
relational structure, local formulas, and the reduction of first-order sentences
to Boolean combinations asserting the existence of pairwise distant points whose
neighborhoods satisfy local conditions; formulas with free variables additionally
need formulas local around those variables.

**Acquisition gap and theorem boundary.** The full article was not acquired.
The institutional abstract supports the qualitative normal-form description and
the statement that the proof proceeds by quantifier elimination, but it does not
expose Gaifman's exact syntax, radius convention, distance inequality, theorem
number, effective bounds, proof induction, or examples. Those details cannot be
borrowed from Libkin's Theorem 4.22. In particular, Libkin's explicit `7^k`
radius estimate is not here attributed to Gaifman's 1982 text.

**Reader-facing condition.** Acquire pp. 105--135 and reconstruct: the source's
metric and `k`-local syntax; the exact separated-neighborhood sentence form; the
formula-versus-sentence distinction; all vocabulary hypotheses; whether the
translation is effective and what bounds are actually stated; the quantifier-
elimination proof steps; and the source's examples of local and non-local
properties. Until then, cite only the institutional abstract-level description
and mark all stronger detail open.

### Presentation 8 of 21: Libkin 2004 (locality presentation)

**Identity and locators.** This is Chapter 4, printed pages 45--65, of Libkin's
[complete author PDF](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf), DOI
[10.1007/978-3-662-07003-1](https://doi.org/10.1007/978-3-662-07003-1).
Controlling locators are Definitions 4.1--4.3, pp. 45--47; Definitions 4.6--4.7,
pp. 47--49; Theorems 4.11--4.12, pp. 51--56; Theorem 4.22, pp. 60--61;
Definitions 4.23 and Theorem 4.24, pp. 61--62; and Exercise 4.9, p. 63.

**Source notation and definitions.** For a relational structure `A`, the
Gaifman graph has an edge between distinct elements that co-occur in some
relation tuple; its graph distance defines `N_r^A(a)` and neighborhoods of
tuples. Definition 4.3 writes `(A,ā) ⇆_r (B,b̄)` for a bijection that matches
the isomorphism types of all relevant radius-`r` neighborhoods. A query is
Hanf-local when such bijective neighborhood matching preserves membership, and
Gaifman-local when a tuple's answer depends only on its own bounded-radius
neighborhood. Definition 4.23 replaces exact type counts by threshold counts:
below `m` the counts agree exactly, while counts at least `m` are identified.
[Libkin, pp. 45--49 and 61.](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf)

**Exact strength.** Theorem 4.11 proves that a non-Boolean Hanf-local query is
Gaifman-local, with `lr(Q) ≤ 3 hlr(Q)+1`. Theorem 4.12 proves every FO-definable
query Hanf-local; if the defining formula has quantifier rank at most `k`, then
`hlr(Q) ≤ (3^k-1)/2`. The resulting Gaifman-locality bound is
`(3^(k+1)-1)/2`. These are query-locality results, not the syntactic Gaifman
normal form. [Libkin, pp. 51--56.](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf)

Theorem 4.22 (Gaifman) is the separate normal-form statement. For relational
`σ`, every `FO` formula `φ(x̄)` is equivalent to a Boolean combination of
formulas local around `x̄` and basic local sentences of the form
`∃x_1...x_s(∧_i α^(r)(x_i) ∧ ∧_{i<j} d(x_i,x_j)>2r)`. For sentences, only
the basic local sentences are needed. The translation is effective; for a
formula of quantifier rank `k` with `n` free variables, the displayed bounds
are `r≤7^k` and `s≤k+n`. [Libkin, pp. 60--61.](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf)

Theorem 4.24 is a **finite bounded-degree threshold theorem**: for every
`k,l>0` there are `d,m>0` such that structures in `STRUCT_l[σ]` which are
threshold-equivalent at `(d,m)` are `k`-round EF-equivalent. The proof sets
`r_0=0`, `r_{i+1}=3r_i+1`, takes `d=r_{k-1}`, and chooses a threshold large
enough in terms of `k`, the degree bound, and the finite number of neighborhood
types; Duplicator preserves isomorphic shrinking tuple-neighborhoods.
[Libkin, pp. 61--62.](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf)

**Proof boundaries.** Theorems 4.11, 4.12, and 4.24 are proved in the text by
explicit EF-game/local-neighborhood inductions. Theorem 4.22 is **stated but its
proof is assigned to Exercise 4.9**; the book does not supply a full normal-form
proof at that point. A reader-facing account must not fuse the proof of semantic
locality (4.12) with a nonexistent in-text proof of the syntactic normal form
(4.22). [Libkin, pp. 51--63.](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf)

**Examples and qualifications.** Two long cycles versus one cycle of twice the
length show that connectivity is not Hanf-local. Later loop-marked cycles with
the same threshold profile but different numbers of marked nodes show how the
bounded-degree threshold theorem proves nondefinability even when exact
bijection-based Hanf locality cannot apply because cardinalities differ. All
distance results depend on relational vocabularies; the degree bound is essential
for Theorem 4.24, but not part of Theorem 4.22's normal-form hypothesis.
[Libkin, pp. 48 and 62--63.](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf)

**Difference and owed reconstruction.** Libkin deliberately presents three
objects that must remain distinct: semantic Hanf locality of queries, semantic
Gaifman locality of queries, and Gaifman's syntactic normal form; it then adds
a finite bounded-degree threshold variant. The reader-facing text owes each
definition and theorem separately, the exact bounds, the cycle counterexamples,
and the exercise status of the normal-form proof. It must not label Theorem 4.24
as Hanf's exact 1965 lemma or attribute Libkin's bounds to Gaifman 1982.

---

## `N-c-004`: descriptive complexity

### Presentation 9 of 21: Fagin 1974

**Identity, copy, and locators.** Ronald Fagin, “Generalized First-Order
Spectra and Polynomial-Time Recognizable Sets,” in Richard M. Karp (ed.),
*Complexity of Computation*, SIAM--AMS Proceedings 7, 1974, pp. 43--73.
The inspected copy is the [author-hosted PDF](https://s3.us.cloud-object-storage.appdomain.cloud/res-files/500-genspec.pdf),
listed on [Fagin's publication page](https://ronfagin.com/papers/); it includes
a 2019 retrospective abstract before the original article. The controlling
original-paper locators are §2 pp. 48--49 (spectra), §4 pp. 52--56 (encoding
and Theorem 6), and the examples and consequences in §§1 and 5--8.

**Source notation and model class.** `S` and `T` are disjoint finite similarity
types. For a first-order `S∪T` sentence `σ`, `Mod_S ∃Tσ` is the class of finite
`S`-reducts whose relations can be expanded on the same universe to satisfy
`σ`; such a class is an `(S,T)`-spectrum, and an `S`-spectrum if some `T`
works. A spectrum in the traditional numerical sense is the `S=∅` case.
Theorem 6 fixes a finite relational `S`, encodes an `S`-structure on
`{1,...,n}` as `e(A)`: the binary representation of `n`, a separator, and the
lexicographically ordered characteristic words of its relations. Classes must
be closed under isomorphism. [Fagin, pp. 48--49 and 52--53.](https://s3.us.cloud-object-storage.appdomain.cloud/res-files/500-genspec.pdf)

**Exact strength.** Theorem 6 says that when `S` is nonempty, an isomorphism-
closed class `A⊆Fin(S)` is an `S`-spectrum exactly when its encoded language
`E(A)` lies in nondeterministic polynomial time. For `S=∅`, spectra correspond
under the paper's unary-size encoding to its class `NP_1`; the accompanying
note unifies the cases as acceptance of `e(A)` in time polynomial in the size
of the represented universe. This is the primary 1974 finite-structure form of
the result now summarized as existential second-order logic captures NP. It is
not a bare statement about arbitrary strings without an encoding and
isomorphism-invariance condition. [Fagin, Theorem 6, pp. 53--54.](https://s3.us.cloud-object-storage.appdomain.cloud/res-files/500-genspec.pdf)

**Proof boundary.** The forward direction is fully constructed: existential
second-order relations are guessed on work tapes and the fixed first-order
matrix is checked over every assignment in polynomial time. For the converse,
the paper normalizes a nondeterministic multitape machine and existentially
quantifies relations (and relation-coded functions) describing an auxiliary
order, tape/time coordinates, nondeterministic choices, and a computation
tableau; the first-order part enforces the initial configuration, local
transitions, and acceptance. The proof continues through p. 56 and handles the
empty-vocabulary/unary-encoding case separately. [Fagin, pp. 53--56.](https://s3.us.cloud-object-storage.appdomain.cloud/res-files/500-genspec.pdf)

**Examples and qualifications.** The introduction recalls a spectrum example:
even cardinality is expressed by the existence of a fixed-point-free involution.
Elsewhere the paper uses Hamiltonian-type generalized spectra and completeness
constructions. The guessed auxiliary order is part of the existential expansion,
so the theorem does **not** assume that input structures arrive with a built-in
order. Conversely, the machine argument is tied to the paper's explicit
encoding of finite relational structures. [Fagin, pp. 43--44 and 52--56.](https://s3.us.cloud-object-storage.appdomain.cloud/res-files/500-genspec.pdf)

**Difference and owed reconstruction.** The reader-facing presentation must
lead with the paper's spectrum/reduct definition and encoding, then state
Theorem 6 in both the nonempty and empty `S` cases, and outline both machine
translations. A modern `ESO = NP` display may follow as an editorial gloss,
but cannot replace the 1974 hypotheses, nor can an order assumption from the
fixed-point theorem be imported into Fagin's result.

### Presentation 10 of 21: Vardi 1982

**Identity and copy.** Moshe Y. Vardi, “The Complexity of Relational Query
Languages (Extended Abstract),” *Proceedings of the Fourteenth Annual ACM
Symposium on Theory of Computing* (STOC 1982), pp. 137--146, DOI
[10.1145/800070.802186](https://doi.org/10.1145/800070.802186). The technical
copy inspected is the full scan in the
[author-uploaded ResearchGate record](https://www.researchgate.net/publication/221590198_The_Complexity_of_Relational_Query_Languages_Extended_Abstract).
The author's former Rice PDF URL is no longer live; therefore the DOI and
author-upload record should both be retained.

**Source setting and definitions.** A database `B=(D,R_1,...,R_k)` has finite
domain `D⊂ℕ`. A query is an isomorphism-consistent partial function on databases,
and its graph is treated as a Boolean relation. The paper separates **data
complexity** (expression fixed, database varying), **expression complexity**
(database fixed, expression varying), and **combined complexity** (both varying).
It compares `F` (first-order relational calculus), `TF` (transitive closure),
`YF` (positive least fixed point), and `SF` (existential second-order formulas).
These language names and the three complexity parameters are part of the source
presentation, not optional modern terminology. [Vardi, pp. 137--139.](https://www.researchgate.net/publication/221590198_The_Complexity_of_Relational_Query_Languages_Extended_Abstract)

**Exact result strength.** Theorem 5 states that the data complexity of `YF`
is complete for polynomial time and its expression complexity is complete for
exponential time. The upper data bound iterates an `r`-ary positive operator for
at most `|D|^r` stages. The lower-bound sketch simulates a polynomial-time
machine by a fixed-point description of a computation tableau. [Vardi,
pp. 141--142.](https://www.researchgate.net/publication/221590198_The_Complexity_of_Relational_Query_Languages_Extended_Abstract)

Remark 2 is the ordered-capture presentation owed here. It first notes that NP
queries are expressible in `SF`. It then says that, if the database already
contains a linear order and the simulated machine is deterministic, the
computation can be built by fixed point; with `YF+`, a slight syntactic extension
allowing existential quantification over conjunctions of equality formulas with
`YF` expressions, the paper records `C(YF+,<)=QPTIME(<)`. Vardi notes independent
work by Immerman. This is not literally the later textbook equation
`FO(LFP)=P` in bare modern syntax, so the source formula must be preserved.
[Vardi, Remark 2, pp. 141--142.](https://www.researchgate.net/publication/221590198_The_Complexity_of_Relational_Query_Languages_Extended_Abstract)

**Proof boundary, examples, and qualifications.** The article explicitly calls
itself an extended abstract and says proofs are only briefly sketched. The
fixed-point iteration upper bound and the machine-tableau lower-bound idea are
given, but not a line-by-line normal-form simulation. The query `Even` is used
to separate unordered `YF` from polynomial time: it is a low-complexity query
but is not expressible in the unordered fixed-point language. Thus the built-in
order is a semantic hypothesis, not notation that may be omitted. [Vardi,
pp. 141--143.](https://www.researchgate.net/publication/221590198_The_Complexity_of_Relational_Query_Languages_Extended_Abstract)

**Difference and owed reconstruction.** Vardi's presentation is a relational-
query complexity matrix with a capture remark, not the full 1986 proof. The
reader-facing text must define the three complexity measures and source
languages, state Theorem 5, reproduce the exact `YF+` ordered formula and its
syntactic qualification, explain why order is necessary, and label the tableau
argument a sketch. It must not silently replace `YF+` by Immerman's `L_μ` or
claim that the extended abstract proves all later normal-form details.

### Presentation 11 of 21: Immerman 1986

**Identity, copy, and locators.** Neil Immerman, “Relational Queries Computable
in Polynomial Time,” *Information and Control* 68 (1986), 86--104, DOI
[10.1016/S0019-9958(86)80029-8](https://doi.org/10.1016/S0019-9958(86)80029-8).
The inspected copy is the [author-hosted PDF](https://people.cs.umass.edu/~immerman/pub/query.pdf).
Controlling passages are §1 pp. 87--89 (databases, `L`, `L_μ`, and examples),
Facts 2.1--2.2 pp. 89--90, and Theorem 1 with its proof in §3 pp. 90--93.

**Source notation and hypotheses.** A finite relational database is
`B=<U,R_1,...,R_k,c_1,...,c_s>`. `L` is first-order relational calculus and
`L_μ` closes it under least fixed points of formulas positive in the relation
being defined. The paper assumes at least one constant `c_0`; it explicitly says
that without a constant, Theorems 1 and 2 require one quantifier after the
fixed-point construction to close the remaining free variables. The introductory
example builds `ancestor` as the least fixed point generated from the database
relations `parent`/`grandparent`. [Immerman, pp. 87--89.](https://people.cs.umass.edu/~immerman/pub/query.pdf)

**Exact strength.** Fact 2.1 proves every `L_μ` query polynomial-time computable,
because an `r`-ary relation stabilizes after at most `|U|^r` additions. Fact 2.2
states that unordered `L_μ` is strictly weaker than polynomial-time queries, with
parity/evenness as the obstruction. Theorem 1 states the ordered capture as
`Σ_ω(≤)=QPTIME=L_μ(≤)`: over finite structures equipped with a total order,
the Boolean queries computable in polynomial time are exactly those expressible
using first-order logic and least fixed point. [Immerman, pp. 89--93.](https://people.cs.umass.edu/~immerman/pub/query.pdf)

**Full proof-outline boundary.** The easy inclusion evaluates each positive
fixed point by iteration. For the converse, the paper says it treats Boolean
queries for simplicity, identifies the ordered universe with
`0,...,n-1`, and uses `k`-tuples to address `n^k` time and tape positions.
One fixed-point relation records the entire deterministic machine tableau:
first-order formulas define the initial row (Lemma 3.1), local formulas define
successor configurations, and a designated bit/state witnesses acceptance. This
construction is worked through in §3, rather than merely promised. Theorem 2 in
§4 is a different collapse result and must not be folded into Theorem 1.
[Immerman, pp. 90--97.](https://people.cs.umass.edu/~immerman/pub/query.pdf)

**Qualifications and owed reconstruction.** A total order is essential and
queries on ordered structures are not invariant under arbitrary permutations
that forget that order. The constant proviso, positivity condition on fixed-point
formulas, Boolean-query simplification, tuple coding, and both inclusions all
belong in the reader-facing account. This presentation differs from Vardi 1982
by giving a sustained proof in the `L_μ` syntax; it differs from the 1999 book by
using the article's notation and local assumptions rather than a book-wide
ordered-structure convention.

### Presentation 12 of 21: Immerman 1999

**Identity and exact manifestations.** Neil Immerman, *Descriptive Complexity*,
Springer, 1999, DOI
[10.1007/978-1-4612-0539-5](https://doi.org/10.1007/978-1-4612-0539-5).
The [author's book page](https://people.cs.umass.edu/~immerman/book/descriptiveComplexity.html)
provides corrected chapter files for the first printing. The inspected technical
copies are the corrected [front matter and Chapters 1--2](https://people.cs.umass.edu/~immerman/book/ch0_1_2.pdf)
and corrected [Chapter 7](https://people.cs.umass.edu/~immerman/book/ch7.pdf),
both marked by the author as updated after publication. Exact page/theorem
locators below therefore belong to those corrected files; they should not be
assumed to reproduce every uncorrected 1999 printing state.

**Book language and standing.** Chapter 1 develops finite relational structures,
ordered structures, Boolean queries, and isomorphism invariance; Proviso 1.15
assumes distinct Boolean constants `0,1` except where noted. The preface says
Chapter 4 introduces least fixed point and proves that polynomial time is exactly
the Boolean queries expressible by first-order logic plus inductive definitions.
The table of contents locates Chapter 4, “Inductive Definitions,” at printed
pp. 75--88. These are book-level scope statements, not a substitute for Chapter
4's missing theorem/proof text. [Corrected front matter and Chapters 1--2.](https://people.cs.umass.edu/~immerman/book/ch0_1_2.pdf)

**Fagin-theorem presentation acquired.** In corrected Chapter 7, §7.1,
printed pp. 143--149, `(SO∃)` denotes existential second-order Boolean queries.
Examples 7.1--7.2 encode SAT and CLIQUE; the opening example gives graph
3-colorability by existentially choosing three unary relations. Proposition 7.6
(`SO∃⊆NP`, pp. 145--146) has a full proof: guess finite relation tables and
model-check the fixed first-order formula. [Immerman, Chapter 7, pp. 143--146.](https://people.cs.umass.edu/~immerman/book/ch7.pdf)

Theorem 7.8 (pp. 146--148) states `NP=SO∃` and strengthens the syntax: the
first-order part can be chosen universal. The proof represents an accepting
polynomial-time computation using existential relations `C_i` of arity `2k`
and a `k`-ary choice relation `Δ`; the displayed conjuncts impose the initial
configuration, consistency of nondeterministic choices, local transitions, and
acceptance. This is a full pedagogical tableau proof, not merely the one-line
capture slogan. Corollary 7.10 on p. 148 places P in existential second-order
Horn form. [Immerman, Chapter 7, pp. 146--149.](https://people.cs.umass.edu/~immerman/book/ch7.pdf)

**Fixed-point acquisition gap.** The author-hosted Chapter 4 file was not
acquired from the available sample URLs. Accordingly, this record can verify
from the corrected preface/contents that the book presents the P/inductive-
definition characterization and can locate the chapter, but cannot yet give the
exact definition number for LFP, capture theorem number, displayed hypotheses,
or its proof boundary. Those must be transcribed from the 1999 Chapter 4, not
backfilled from the 1986 article. [Author's book page and available corrected
samples.](https://people.cs.umass.edu/~immerman/book/descriptiveComplexity.html)

**Difference and owed reconstruction.** The 1999 book's acquired Fagin
presentation is more pedagogically explicit than the 1974 paper: modern
second-order syntax, standard NP examples, and the universal-matrix refinement.
The reader-facing account must name the corrected manifestation used, define
`SO∃`, give both directions and the universal normal form, and keep the missing
Chapter 4 details visibly open. Once Chapter 4 is acquired, reconstruct its own
ordered-structure convention, fixed-point syntax, theorem statement, and proof;
do not splice the 1986 theorem numbering into the book.

---

## `N-c-005`: classical decidable and undecidable prefix classes

### Presentation 13 of 21: Lewis 1979

**Identity and access.** Harry R. Lewis, *Unsolvable Classes of Quantificational
Formulas*, Addison--Wesley, 1979, xv + 198 pages, ISBN `0-201-04069-7`; the
[Google Books bibliographic record](https://books.google.com/books/about/Unsolvable_Classes_of_Quantificational_F.html?hl=en&id=sFcrAAAAYAAJ&output=html_text)
establishes the book identity. An authoritative contemporary review is available
from the [reviewer's author-hosted copy](https://web.eecs.umich.edu/~gurevich/Opera/39.pdf),
DOI [10.1090/S0273-0979-1982-15033-9](https://doi.org/10.1090/S0273-0979-1982-15033-9),
but a review is not the registered source text.

**Acquisition gap.** The book text was not acquired. The accessible preview
reveals only fragmentary contents (for example, “Combinatorial Systems,” “The
Linear Sampling Problem,” and “Other Versions”), not enough to establish where
or how Lewis defines prefix classes, reductions, equality/function conventions,
the Bernays--Schönfinkel--Ramsey, Ackermann, or Gödel--Kalmár--Schütte boundaries,
or their proofs and counterexamples. The title itself foregrounds **unsolvable**
classes; it does not license attributing Börger--Grädel--Gurevich's later unified
decidable-class table to Lewis.

**Material source distinction.** Lewis's different 1980 article on the
complexity of decidable prefix classes, DOI
[10.1016/0022-0000(80)90027-6](https://doi.org/10.1016/0022-0000(80)90027-6),
is not the registered 1979 book and must not be silently substituted for it.

**Reader-facing condition.** Acquire the relevant 1979 chapters and transcribe
the book's exact syntactic class notation; satisfaction versus finite-satisfaction
problem; permitted equality, predicates, functions, and constants; reduction
notion; each maximal or conservative reduction class; proof status; and the
examples witnessing boundary undecidability. Until then, the Lewis presentation
can contain bibliographic identity and an explicit gap only.

### Presentation 14 of 21: Börger--Grädel--Gurevich 1997 (prefix-class presentation)

**Identity, copy, and global notation.** Egon Börger, Erich Grädel, and Yuri
Gurevich, *The Classical Decision Problem*, Springer, 1997, xii + 482 pages.
The inspected complete copy is the authors' [full book PDF](https://web.eecs.umich.edu/~gurevich/Books/00.pdf),
linked from the [author book page](https://web.eecs.umich.edu/~gurevich/Books/CDP.html),
which also notes a second printing in 2001. Definition 1.3.1, pp. 8--9, writes
`[Π,p,f]` for prenex sentences without equality whose prefixes lie in `Π`, with
bounded numbers of predicate and function symbols by arity; a superscript `=`
admits equality. Constants and free variables are excluded from this base
notation and handled by stated translations. Definition 2.1.6, p. 24, defines a
reduction class through an effective satisfiability-preserving map from arbitrary
first-order sentences. [Börger--Grädel--Gurevich, pp. 8--9 and 24.](https://web.eecs.umich.edu/~gurevich/Books/00.pdf)

**Relational monadic baseline.** In §6.2.1, pp. 249--257, the relational
monadic class is `[all,(ω)]` (and its equality variant): relation symbols are
unary and there are no functions. Proposition 6.2.1 says that a satisfiable
equality-bearing monadic sentence of quantifier rank `q` with `m` predicate
symbols has a model of size at most `q·2^m`. The complete proof partitions
elements into the `2^m` unary colors and retains at most `q` representatives of
each. Corollary 6.2.2 gives decidability; Exercise 6.2.3 sharpens the no-equality
bound to `2^m`, and Corollary 6.2.4 gives the stated asymptotic model bound in
formula length. [Börger--Grädel--Gurevich, pp. 249--251.](https://web.eecs.umich.edu/~gurevich/Books/00.pdf)

**Bernays--Schönfinkel--Ramsey class.** Section 6.2.2, pp. 257--261, treats
the relational `∃*∀*` class, with and without equality. Proposition 6.2.17
says that a satisfiable `∃^p∀^m` equality-bearing sentence has a model of size
at most `max(1,p)`: choose witnesses for the existential block and use
preservation of a universal relational matrix under induced substructures.
The book then proves the nondeterministic exponential upper bound and the
matching lower bound, yielding NEXPTIME-completeness. It also records the
finite/cofinite spectrum behavior induced by the small-model argument.
[Börger--Grädel--Gurevich, pp. 257--261.](https://web.eecs.umich.edu/~gurevich/Books/00.pdf)

**Gödel--Kalmár--Schütte class.** Section 6.2.3, pp. 261--269, studies the
relational `∀^2∃*` core and its leading-existential closure. Theorem 6.2.23 proves
the finite model property for `[∀^2∃*,all]`; the book supplies a probabilistic
proof, expressly contrasting it with the older complicated constructions.
Corollary 6.2.38 extends the finite-model result to `[∃*∀^2∃*,all]`. The
historical discussion on pp. 310--311 distinguishes the independent Gödel,
Kalmár, and Schütte decision procedures and credits Gödel and Schütte with
finite-model arguments. [Börger--Grädel--Gurevich, pp. 261--269 and 310--311.](https://web.eecs.umich.edu/~gurevich/Books/00.pdf)

**Ackermann class.** Section 6.3.2, pp. 281--285, treats relational
`∃*∀∃*`. Theorem 6.3.24 gives a deterministic decision bound for the monadic
Ackermann case; Theorem 6.3.26 gives the general upper bound
`2^{c(n/log n)^2}` in the book's size measure, followed by lower-bound analysis.
Unlike BSR, this class's decidability boundary interacts materially with equality:
the historical synthesis says that without equality BSR and GKS are the two
maximal decidable prefix classes, whereas with equality BSR and Ackermann are
the two maximal decidable ones. [Börger--Grädel--Gurevich, pp. 281--285 and
310--311.](https://web.eecs.umich.edu/~gurevich/Books/00.pdf)

**Reduction-class boundary and qualifications.** The same synthesis states
that, without equality, the nearby prefixes `∀^3∃` and `∀∃∀` are reduction
classes. Hence one flat table labeled only by prefix would be false: every row
must also name equality, positive-arity function, relational-vocabulary, and
finite-model/satisfiability conditions. Constants and free variables inherit
only the book's explicit translations. [Börger--Grädel--Gurevich,
pp. 8--9, 24, and 310--311.](https://web.eecs.umich.edu/~gurevich/Books/00.pdf)

**Proof boundary and owed reconstruction.** The small-model proofs for monadic
logic and BSR and the book's probabilistic GKS construction are supplied, not
merely cited; the Ackermann section supplies its own algorithmic bounds. A
reader-facing reconstruction owes (1) the bracket notation and reduction
definition, (2) a table with separate equality/function columns, (3) the BSR
witness-substructure proof, (4) the GKS probabilistic proof outline, (5) the
Ackermann decision-bound outline, and (6) the adjacent undecidable reduction
classes. It must identify this as the 1997 synthesis, not retroject the table
into Lewis 1979.

---

## `N-c-006`: two-variable first-order logic

### Presentation 15 of 21: Mortimer 1975

**Identity.** Michael Mortimer, “On Languages with Two Variables,”
*Zeitschrift für Mathematische Logik und Grundlagen der Mathematik* 21
(1975), 135--140, DOI
[10.1002/malq.19750210118](https://doi.org/10.1002/malq.19750210118).

**Acquisition gap.** The Wiley article text was not acquired. The DOI fixes
the bibliographic identity but does not expose Mortimer's definition of the
two-variable language, vocabulary/equality conventions, normal form, model-size
bound, theorem numbering, proof, or examples. Those details are not inferred
from the 1997 paper. In its own abstract, the later paper says Mortimer proved
the finite-model property and a doubly exponential model bound; that is evidence
about the **1997 authors' historical presentation**, not a substitute for the
exact six-page 1975 presentation. [Grädel--Kolaitis--Vardi's publisher abstract.](https://doi.org/10.2307/421196)

**Reader-facing condition.** Acquire pp. 135--140 and transcribe the original
syntax (including whether relation arities, equality, and constants are allowed),
the exact finite-model theorem and size parameter, the construction and its
bound, and any decision procedure or counterexample stated. The manuscript may
say only that the registered original remains acquisition-blocked; it must not
label the 1997 Scott-class construction or “king” terminology as Mortimer's.

### Presentation 16 of 21: Grädel--Kolaitis--Vardi 1997

**Identity, copy, and locators.** Erich Grädel, Phokion G. Kolaitis, and
Moshe Y. Vardi, “On the Decision Problem for Two-Variable First-Order Logic,”
*Bulletin of Symbolic Logic* 3(1) (1997), 53--69, DOI
[10.2307/421196](https://doi.org/10.2307/421196). The inspected technical copy
is this [complete article PDF mirror](https://www.mimuw.edu.pl/~jk345076/assets/popularization/FO2/On%20the%20Decision%20Problem%20for%20Two-Variable%20First-Order%20Logic.pdf);
the [Cambridge publisher record](https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/abs/on-the-decision-problem-for-twovariable-firstorder-logic/1F219DB769A185D266A8992DA7755D60)
confirms authors, volume, issue, pages, abstract, and DOI. Controlling locators
are §3, Proposition 3.1, pp. 58--60; §4, Definitions 4.1--4.2 and Theorem 4.3,
pp. 60--64; and §5, Theorems 5.1 and 5.3 and Corollary 5.4, pp. 64--66.

**Language and normal form.** `FO^2` consists of relational first-order
sentences using at most two distinct individual variables, reused under
quantification; equality is admitted unless the no-equality variant is named.
The initial reduction replaces higher-arity atomic patterns by unary or binary
relation symbols. Proposition 3.1 is Scott's satisfiability-preserving reduction:
from a sentence `φ` of size `s`, it produces `φ*` of size `O(s log s)` with
`O(s)` relation symbols, preserving finite-model cardinality in the direction
needed. Crucially, `φ*` is **not** put into one prenex string. [Grädel--Kolaitis--Vardi,
pp. 53--60.](https://www.mimuw.edu.pl/~jk345076/assets/popularization/FO2/On%20the%20Decision%20Problem%20for%20Two-Variable%20First-Order%20Logic.pdf)

Section 4 calls the resulting conjunction the *Scott class* and writes it
`∀x∀y α(x,y) ∧ ∧_{i=1}^m ∀x∃y β_i(x,y)`, where the matrices are
quantifier-free and may be arranged so `β_i(x,y) ⊨ x≠y`. Definition 4.1 makes
a `k`-type a maximal consistent set of atomic and negated atomic formulas in a
fixed tuple of variables. Definition 4.2 calls an element a *king* when it is
the sole realizer of its 1-type. Those terms are defined artifacts of this
presentation and should be introduced only with these definitions.
[Grädel--Kolaitis--Vardi, pp. 60--61.](https://www.mimuw.edu.pl/~jk345076/assets/popularization/FO2/On%20the%20Decision%20Problem%20for%20Two-Variable%20First-Order%20Logic.pdf)

**Exact model bounds.** Theorem 4.3 says that a satisfiable Scott-class
sentence `θ` has a finite model of size at most `3s·2^r`, where `s` is the size
of `θ` and `r` the number of relation symbols occurring in it. Theorem 5.1 then
gives the exponential model property for arbitrary `FO^2`: there is a constant
`c` such that every satisfiable sentence of size `s` has a model of size at most
`2^(cs)`. This improves by one exponential the Mortimer bound as reported by
the 1997 authors. [Grädel--Kolaitis--Vardi, pp. 61 and 64--65.](https://www.mimuw.edu.pl/~jk345076/assets/popularization/FO2/On%20the%20Decision%20Problem%20for%20Two-Variable%20First-Order%20Logic.pdf)

**Full proof-outline boundary.** Starting with a model `A` of the Scott
sentence, the proof preserves every uniquely realized 1-type and its element
(the set `K` of kings), closes a finite “royal court” under chosen witnesses for
the `∀x∃y` conjuncts, and makes three cyclic banks `D,E,F` of representatives
for every remaining 1-type and witness index. It copies realized 2-types from
`A` so the universal conjunct remains true, assigns witnesses cyclically to avoid
conflicting 2-type requirements, and assigns unused pairs arbitrary compatible
2-types realized in `A`. The count is bounded by
`(m+1)|K|+3m(|P|-|K|) ≤ 3s·2^r`. The paper also explains why two banks can
create reciprocal-witness conflicts. This construction is fully given on
pp. 62--64. [Grädel--Kolaitis--Vardi, pp. 62--64.](https://www.mimuw.edu.pl/~jk345076/assets/popularization/FO2/On%20the%20Decision%20Problem%20for%20Two-Variable%20First-Order%20Logic.pdf)

**Complexity strength.** Definition 5.2 fixes nondeterministic time and
`NEXPTIME`. Theorem 5.3 gives the upper bound `NTIME(2^{O(s/log s)})` for
the Scott class and `NTIME(2^{O(s)})` for `FO^2`. A lower bound from the
`∀∀ ∧ ∀∃` class, already without equality, yields Corollary 5.4: satisfiability
for `FO^2`, with or without equality, is NEXPTIME-complete. The paper notes a
finer-grained gap caused by the `O(s log s)` Scott reduction; the class-level
NEXPTIME-completeness does not erase that qualification. [Grädel--Kolaitis--Vardi,
pp. 65--66.](https://www.mimuw.edu.pl/~jk345076/assets/popularization/FO2/On%20the%20Decision%20Problem%20for%20Two-Variable%20First-Order%20Logic.pdf)

**Examples, boundary cases, and owed reconstruction.** Constants can be added
without changing the exponential bound (constants are handled as kings), but
positive-arity function symbols destroy the result: the paper cites undecidable
two-variable cases with unary functions. The nearby class
`∀∀ ∧ ∀∃` outside the Scott restrictions can express an infinite linear order
without a maximum and lacks the finite-model property; counting quantifiers
retain decidability but not the ordinary finite-model property. `FO^3` is already
undecidable, even without equality. [Grädel--Kolaitis--Vardi, pp. 53--54 and
66--67.](https://www.mimuw.edu.pl/~jk345076/assets/popularization/FO2/On%20the%20Decision%20Problem%20for%20Two-Variable%20First-Order%20Logic.pdf)

The reader-facing presentation owes the two-variable syntax, the non-prenex
Scott reduction, types and kings, the three-bank model construction and exact
bounds, both complexity directions, and the function/counting/three-variable
boundaries. It must explicitly distinguish the paper's new exponential bound
from its historical report of Mortimer's doubly exponential one.

---

## `N-c-007`: the guarded fragment and its modal connection

### Presentation 17 of 21: Andréka--van Benthem--Németi 1998

**Registered identity versus inspected manifestation.** The registered work is
Hajnal Andréka, Johan van Benthem, and István Németi, “Modal Languages and
Bounded Fragments of Predicate Logic,” *Journal of Philosophical Logic* 27(3)
(1998), 217--274, DOI
[10.1023/A:1004275029985](https://doi.org/10.1023/A:1004275029985).
The exact technical text inspected is the authors' 59-page institutional
preprint, ILLC Research Report `ML-1996-03` (1996), available from the
[ILLC repository record](https://eprints.illc.uva.nl/1372/) and as its
[full preprint PDF](https://eprints.illc.uva.nl/id/eprint/1372/2/ML-1996-03.text.pdf).
The preprint and the 1998 journal article are distinct manifestations. The
preprint locators below must not be presented as verified 1998 journal pagination
or as proof that every sentence survived revision unchanged.

**Source syntax and modal motivation.** Section 2 treats ordinary modal logic
through its standard first-order translation; Corollary 2.3.2 gives modal
decidability and the finite-model property. Section 4.1, preprint pp. 27--28,
then compares bounded-quantifier schemas:
`∃y(Ryx ∧ φ(y))` (Fragment 1), `∃y(Ryx ∧ φ(x,y))` (Fragment 2), and
`∃y(Ryx ∧ φ(x,y,z))` (Fragment 3), with tuple/general-arity variants understood.
Formulas begin from arbitrary atoms and close under Boolean operations and such
quantifiers. In Fragment 2—the work's *Guarded Fragment*—the atomic guard must
contain all variables relevant to the quantified matrix; identity atoms may
occur but are not guards, and Boolean combinations of atoms are not guards.
[Andréka--van Benthem--Németi preprint, §§2.3 and 4.1.](https://eprints.illc.uva.nl/id/eprint/1372/2/ML-1996-03.text.pdf)

The syntax can express symmetry but not transitivity of a binary relation.
Fragment 1 remains close to the modal fragment, Fragment 2 is the guarded
fragment, and Fragment 3 is already undecidable; Theorem 4.2.3 says the three
form a proper expressive hierarchy. These examples locate the intended
“modal-like but more expressive” middle fragment. [Preprint, pp. 27--30.](https://eprints.illc.uva.nl/id/eprint/1372/2/ML-1996-03.text.pdf)

**Guarded bisimulation and exact semantic strength.** In §4.2, a set of
elements is guarded when it is exactly the set occurring in a true relation
tuple. A guarded bisimulation is a nonempty family of finite partial
isomorphisms satisfying back-and-forth clauses for guarded subsets, agreeing
with the current map on overlaps. Proposition 4.2.1 proves guarded formulas
invariant under this relation. Theorem 4.2.2 states both directions: an
first-order formula is invariant under guarded bisimulations exactly when it is
equivalent to a Fragment-2 formula; the finite `k`-round version characterizes
the `k`-variable subfragment. [Preprint, §4.2, pp. 28--30.](https://eprints.illc.uva.nl/id/eprint/1372/2/ML-1996-03.text.pdf)

**Decidability theorem and proof boundary in the inspected preprint.** Section
4.6 expressly presents Theorem 4.6.1 for the guarded fragment **without
identity**: satisfiability is decidable. For a given guarded formula `φ`, it
forms a finite set `F` of bounded-length formulas using the variables of `φ`,
defines `F`-types with Boolean/substitution closure, and defines a finite
*quasi-model* as a set of such types satisfying a successor condition for each
guarded existential. Every standard model yields such a quasi-model; conversely,
paths through a quasi-model are unfolded into a standard model, with a truth
lemma. Since existence of a finite quasi-model is effectively checkable,
decidability follows. This is a substantial construction on preprint pp. 39--45,
not a bare modal-logic reduction. [Preprint, Theorem 4.6.1 and proof.](https://eprints.illc.uva.nl/id/eprint/1372/2/ML-1996-03.text.pdf)

**Critical finite-model qualification.** The preprint's abstract uses language
suggesting an effectively bounded finite-model property, but the body draws a
strict distinction: the proof obtains finite **abstract quasi-models** and may
unfold them to infinite standard models. At the end of §4.6 it says the argument
does not yield completeness with respect to finite standard models and assigns
the full guarded-fragment finite-model property to a follow-up publication. The
section also says the proof presented is without identity and that equality
requires syntactic care. [Preprint, pp. 39 and 44--45.](https://eprints.illc.uva.nl/id/eprint/1372/2/ML-1996-03.text.pdf)

Because the final 1998 journal text was not acquired, this record cannot decide
whether the abstract/body tension or the finite-model proof was changed in the
published manifestation. It therefore does **not** attribute a finite standard-
model proof to the registered journal article on the basis of the preprint.

**Difference and owed reconstruction.** This presentation supplies the modal
genealogy, bounded-fragment hierarchy, guarded-bisimulation characterization,
and a quasi-model decision proof. A reader-facing version based on the current
copy must label every locator “1996 preprint,” distinguish quasi-model finiteness
from standard-model finiteness, and state the no-identity proof scope. To claim
the exact 1998 result or pagination, acquire pp. 217--274 and compare them
clause by clause; Grädel's later finite-model proof cannot fill that edition gap.

### Presentation 18 of 21: Grädel 1999

**Identity, copy, and locators.** Erich Grädel, “On the Restraining Power of
Guards,” *Journal of Symbolic Logic* 64(4) (1999), 1719--1742, DOI
[10.2307/2586808](https://doi.org/10.2307/2586808); the journal identity and
abstract are on [Cambridge Core](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/on-the-restraining-power-of-guards/AE1072EE5A0987341B73E8A1831905F3).
The inspected technical manifestation is Grädel's
[author-hosted revised preprint](https://logic.rwth-aachen.de/pub/graedel/Gr-jsl99.ps),
dated July 1998; an institutional identity record is available from
[RWTH Aachen](https://publications.rwth-aachen.de/record/141527). Controlling
author-version locators are Definitions 2.1--2.2, pp. 3--4; Theorems 3.7 and
3.10, pp. 8--11; Theorems 4.3--4.4 and Corollaries 4.5--4.6, pp. 13--19;
and Theorems 5.8 and 5.10, pp. 20--22.

**Syntax and hypotheses.** The vocabulary is relational, with equality and
constants allowed but no functions of positive arity. Definition 2.1 builds GF
from atoms using Boolean connectives and guarded quantifiers
`∃y(α(x,y)∧φ(x,y))` or their universal duals, where the single atomic guard
`α` contains all free variables of the matrix. Definition 2.2's loosely guarded
fragment LGF permits a conjunction of atoms as guard, subject to the pairwise
co-occurrence condition ensuring that each newly quantified variable is linked
to every variable still relevant. LGF can express useful temporal “until”
patterns, while transitivity is not itself in LGF. [Grädel, §§1--2,
author version pp. 2--5.](https://logic.rwth-aachen.de/pub/graedel/Gr-jsl99.ps)

**Model-theoretic strength.** Theorem 3.7 says that every satisfiable loosely
guarded sentence using `m` variables has a bounded-degree `m`-tree model. The
proof first obtains the source's guarded normal form and inductively attaches
witness structures while preserving atomic types; this is a possibly infinite
tree-model construction. Theorem 3.10 then proves that every satisfiable **GF**
sentence has a finite model: start with the tree model, choose a finite
representative subtree for the finitely many local isomorphism types, and use
Herwig's extension theorem to close partial isomorphisms while preserving the
guarded witness obligations. The paper explicitly says the analogous finite-
model property for LGF is open. [Grädel, §3, author version pp. 8--12.](https://logic.rwth-aachen.de/pub/graedel/Gr-jsl99.ps)

**Exact complexity.** Theorem 4.3 places LGF satisfiability in deterministic
double-exponential time by searching over exponentially described atomic types
with alternating exponential-space control. Theorem 4.4 proves GF satisfiability
`2EXPTIME`-hard by encoding an exponentially space-bounded alternating-machine
computation tree. Corollary 4.5 therefore makes GF and LGF satisfiability, with
or without equality, `2EXPTIME`-complete. Corollary 4.6 lowers the result to
`EXPTIME`-complete when either the number of variables or relation arity is
fixed; over any fixed finite vocabulary, LGF satisfiability is in `EXPTIME`.
[Grädel, §4, author version pp. 13--19.](https://logic.rwth-aachen.de/pub/graedel/Gr-jsl99.ps)

**Undecidable extensions and examples.** Section 5 uses finite grid encodings
to show that modest-looking additions cross the boundary. Theorem 5.8 makes GF
plus functionality statements a conservative reduction class (already with a
three-variable guarded part without equality); the following corollary treats
the corresponding counting extension. Theorem 5.10 makes GF with stipulated
transitive relations a conservative reduction class, again already in a tightly
bounded-variable setting. These are negative extension results, not claims that
functionality or transitivity are definable inside plain GF. [Grädel, §5,
author version pp. 19--22.](https://logic.rwth-aachen.de/pub/graedel/Gr-jsl99.ps)

**Proof status, difference, and owed reconstruction.** The tree-model,
finite-model, upper/lower complexity, and reduction-class arguments are proved
in the author version. Relative to the inspected Andréka--van Benthem--Németi
preprint, Grädel supplies the full finite **standard** model argument for GF,
adds LGF, pins down exact complexity, and identifies undecidable extensions.
The reader-facing text must define GF and LGF separately, outline both the tree
unravelling and Herwig closure, state that LGF's finite-model property remains
open here, give both sides of the complexity theorem, and keep the extension
results outside the base fragment.

---

## `N-c-008`: Löwenheim--Behmann monadic decidability

### Presentation 19 of 21: Löwenheim 1915

**Identity and available manifestation.** Leopold Löwenheim, “Über
Möglichkeiten im Relativkalkül,” *Mathematische Annalen* 76(4) (1915),
447--470, DOI
[10.1007/BF01458217](https://doi.org/10.1007/BF01458217). The stable
[EuDML record](https://eudml.org/doc/158703) and the Göttingen
[digitized-work endpoint](https://www.digizeitschriften.de/download/pdf/235181684_0076/log39.pdf)
identify the original. The download endpoint returned an HTML wrapper rather
than a usable article PDF during this acquisition, so no page-level original
transcription was possible.

**What a later authoritative synthesis reports—and what it cannot replace.**
The annotated Löwenheim entry in Börger--Grädel--Gurevich says that the 1915
paper works in terms of validity, with equality and without functions; proves
decidability and finite controllability for formulas using only monadic
predicates; recognizes infinity axioms; and reduces the general validity problem
to formulas using only binary predicates. The same synthesis identifies the
paper as written in the older relation-calculus setting. These are claims of the
**1997 book about the 1915 source**, not a transcription of Löwenheim's own
notation or proof. [Börger--Grädel--Gurevich, annotated bibliography entry
365.](https://web.eecs.umich.edu/~gurevich/Books/00.pdf)

**Acquisition gap.** The original's exact relation-calculus symbols, definition
of the monadic restriction, finite-domain argument, decision procedure, theorem
divisions, examples, and distinction between validity and satisfiability remain
unacquired. Even the modern phrase “monadic first-order logic” is an editorial
translation here and must be labeled as such rather than placed in quotation
marks as Löwenheim's terminology.

**Reader-facing condition.** Acquire readable original pages 447--470 or the
published English translation and preserve three layers separately: (1) the
source's relation-calculus notation and validity formulation, (2) an explicit
modern translation with typed unary predicates/equality/no-functions
hypotheses, and (3) a proof outline tied line by line to the original. Include
the monadic decision argument, finite controllability, infinity-axiom example,
and binary-predicate reduction only when their original locators are verified.
Do not substitute the color-counting proof in the 1997 book.

### Presentation 20 of 21: Behmann 1922

**Identity and exact scan.** Heinrich Behmann, “Beiträge zur Algebra der Logik,
insbesondere zum Entscheidungsproblem,” *Mathematische Annalen* 86 (1922),
163--229, DOI
[10.1007/BF01457985](https://doi.org/10.1007/BF01457985). The
[EuDML record](https://eudml.org/doc/158945) fixes the volume and page span;
the inspected primary manifestation is the Göttingen
[complete article scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0086/LOG_0018.pdf).

**Primary-source structure that can be verified.** The scan's printed contents
divide the paper into six parts and §§1--17. The directly relevant route is
Part III, “Das elementare Entscheidungsproblem,” §§7--8 (practical procedure
and normal forms); Part IV, §§9--11 (the first level of the general decision
problem, examples, normal form, and class notation); Part V, §§12--14 (reduction
from decision to elimination and the main elimination form); and Part VI,
§§15--17 (calculation, intuitive solution/general result, and several concepts).
Those headings establish the proof's elimination architecture, not the content
of any untranscribed proposition. [Behmann's original scan.](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0086/LOG_0018.pdf)

**Acquisition gap despite scan availability.** The 68-page scan has no usable
article OCR in the acquired file. This acquisition therefore does not claim an
exact transcription of Behmann's algebraic symbols, anti-prenex transformations,
elimination rules, decision theorem, equality extension, or second-order
monadic extension. A later authoritative annotated bibliography says the paper
contains an anti-prenex normal form and a validity decision procedure for
monadic predicate logic without functions or equality, and extends the result
to equality and to second-order formulas whose free and bound predicates are
all monadic. That is the **1997 book's report**, not a surrogate proof text.
[Börger--Grädel--Gurevich, annotated bibliography entry 31.](https://web.eecs.umich.edu/~gurevich/Books/00.pdf)

**Reader-facing condition.** Produce a reliable transcription or obtain an
authoritative edition/translation of §§7--17. Then define each source symbol,
state exactly what is eliminated and what remains free or bound, preserve the
validity orientation, give the anti-prenex and elimination sequence with its
termination argument, and locate the equality and monadic second-order
extensions. Examples from §9 must be transcribed rather than replaced with the
1997 color proof. Until then, the manuscript can give the verified section map
and state the acquisition gap only.

### Presentation 21 of 21: Börger--Grädel--Gurevich 1997 (monadic presentation)

**Identity, copy, and locators.** This is the monadic presentation in §6.2.1,
printed pp. 249--257, plus the historical synthesis on pp. 310--311 and the
annotated bibliography entries 31 and 365, of Börger, Grädel, and Gurevich,
*The Classical Decision Problem* (Springer, 1997). The technical copy is the
authors' [complete book PDF](https://web.eecs.umich.edu/~gurevich/Books/00.pdf),
linked from the [author book page](https://web.eecs.umich.edu/~gurevich/Books/CDP.html).

**Modern source notation and class boundary.** In the bracket notation of
Definition 1.3.1, the relational Löwenheim class is `[all,(ω)]` and its
equality-bearing version has superscript `=`: arbitrary quantifier prefixes,
only unary predicate symbols, and no function symbols. The book distinguishes
this from the *full monadic class*, which can include unary functions. That
vocabulary difference is material: “monadic” does not mean one uniform class
throughout §6.2.1. [Börger--Grädel--Gurevich, pp. 8--9 and 249--250.](https://web.eecs.umich.edu/~gurevich/Books/00.pdf)

**Exact relational small-model theorem.** Proposition 6.2.1 says that a
satisfiable relational monadic formula `ψ`, possibly with equality, of
quantifier rank `q` and using `m` predicates has a model of cardinality at most
`q·2^m`. Given `A⊨ψ`, associate to each element its Boolean color in
`{0,1}^m`, retain at most `q` elements of each color, and take the induced
substructure. Duplicator wins the `q`-move EF game between the old and reduced
structures, so `ψ` is preserved. This is a complete modern proof.
[Börger--Grädel--Gurevich, Proposition 6.2.1, pp. 249--250.](https://web.eecs.umich.edu/~gurevich/Books/00.pdf)

Corollary 6.2.2 gives decidability of relational monadic satisfiability.
Exercise 6.2.3 asks the reader to prove the sharper `2^m` bound **without
equality**; Corollary 6.2.4 derives a minimal-model bound
`2^{O(n/log n)}` for equality-bearing formulas of length `n`. The chapter
announces a nondeterministic `2^{O(n/log n)}`-time satisfaction test for that
relational equality class. The sharper no-equality result is exercise-level and
must be labeled so. [Börger--Grädel--Gurevich, pp. 250--251.](https://web.eecs.umich.edu/~gurevich/Books/00.pdf)

**Second-order extension boundary.** Exercise 6.2.5, credited to Behmann and
Skolem, asks the reader to extend the argument to second-order logic in which
**all predicates, free and bound, are monadic**. The historical text on
pp. 310--311 and annotated entries separately describe Löwenheim's first-order
result and the Behmann/Skolem extension. The book does not supply a completed
proof in the exercise, so a manuscript must not report this as an in-text proof.
[Börger--Grädel--Gurevich, pp. 250--251 and 310--311.](https://web.eecs.umich.edu/~gurevich/Books/00.pdf)

**Full monadic class with unary functions.** Proposition 6.2.7, pp. 251--252,
says every satisfiable monadic formula of length `n` has a model of size
`2^{O(n)}`. Its proof eliminates atoms of the form `P(f(t))` by fresh unary
predicates and equivalences `P(f(x))↔Q(x)`, then replaces the remaining unary
functions with existential witnesses to obtain an equisatisfiable relational
monadic formula over the same domains. The chapter announces the resulting
nondeterministic `2^{O(n)}` upper bound. Proposition 6.2.15 shows the model
bound is substantively needed: length-`O(n)` monadic sentences with one unary
function force at least `(n+1)2^n` elements by a chain leading into a long
counter cycle. [Börger--Grädel--Gurevich, pp. 251--257.](https://web.eecs.umich.edu/~gurevich/Books/00.pdf)

**Historical qualification and difference.** The book's historical notes say
Löwenheim formulated the original result in terms of validity and also treated
equality, infinity axioms, and binary-predicate reduction; they say Behmann's
anti-prenex/elimination proof extends from the equality-free monadic case to
equality and monadic second order. Those paragraphs are a 1997 historical
synthesis. They do not reproduce the originals' syntax, and the book's
`q·2^m` EF/color proof is its own modern presentation. [Börger--Grädel--Gurevich,
pp. 310--311 and annotated entries 31 and 365.](https://web.eecs.umich.edu/~gurevich/Books/00.pdf)

**Reader-facing reconstruction.** Define the book's bracket notation and split
relational from full monadic logic; prove Proposition 6.2.1 with colors and the
EF game; derive decidability and the length bound; label the no-equality and
monadic-second-order items as exercises; then separately outline the unary-
function elimination and lower-bound cycle. The historical paragraphs may
identify what the earlier sources are reported to contain, but cannot replace
the still-missing Löwenheim and Behmann presentations.

---

## Nonhybridization handoff: minimum reader-facing payload by row

| Row | Presentations that must remain visibly distinct | Minimum reconstruction that cannot be omitted |
|---|---|---|
| `N-c-001` | Ebbinghaus--Flum 1995; Libkin 2004 | edition-specific definitions and locators; finite compactness witness; status of Craig/Beth proofs; finite-game examples; Trakhtenbrot vocabulary hypothesis, encoding, and non-r.e. consequence |
| `N-c-002` | Glebskii et al. 1969; Fagin 1976; Libkin 2004 | each probability space; extension schema; proof method; labeled/unlabelled distinction; constants/functions counterexamples; Libkin's pebble-game and `BIT` random graph only under Libkin |
| `N-c-003` | Hanf 1965; Gaifman 1982; Libkin 2004 | original locally finite exact-count lemma only after acquisition; Gaifman original syntax only after acquisition; Libkin's semantic localities, normal form, bounds, exercise status, and finite threshold theorem separately |
| `N-c-004` | Fagin 1974; Vardi 1982; Immerman 1986; Immerman 1999 | finite-structure encodings and isomorphism closure for ESO/NP; Vardi's data/expression distinction and `YF+`; Immerman's ordered `L_μ` tableau proof; book theorem numbers and corrected manifestation independently |
| `N-c-005` | Lewis 1979; Börger--Grädel--Gurevich 1997 | no Lewis technical claims until book acquisition; BGG bracket notation; equality/function columns; BSR/GKS/Ackermann proof and reduction boundaries |
| `N-c-006` | Mortimer 1975; Grädel--Kolaitis--Vardi 1997 | no retrojection of Scott class or kings; original Mortimer theorem after acquisition; 1997 non-prenex reduction, exact exponential bounds, three-bank construction, and NEXPTIME result |
| `N-c-007` | ABN 1998 journal target; ABN 1996 inspected preprint; Grädel 1999 | manifestation label on every ABN locator; quasi-model versus standard finite model; no-identity scope; Grädel's GF/LGF split, finite-model proof, exact complexity, and undecidable extensions |
| `N-c-008` | Löwenheim 1915; Behmann 1922; Börger--Grädel--Gurevich 1997 | originals' validity/algebra/elimination syntax after acquisition; explicit modern translation; BGG color/EF proof and unary-function extension as a later presentation; exercise-level MSO extension labeled |

## Blocking acquisitions that remain

The following source-level work remains before all twenty-one presentations can
be turned into faithful manuscript prose:

1. Obtain theorem-text copies of Ebbinghaus--Flum's **1995 first edition**,
   Glebskii et al. 1969, Hanf 1965, Lewis 1979, and Mortimer 1975.
2. Obtain the full Gaifman 1982 paper; the institutional abstract does not fix
   his syntax, proof, or quantitative bounds.
3. Obtain Immerman 1999 Chapter 4 from the registered/corrected book
   manifestation and transcribe its own LFP theorem and proof.
4. Obtain the published Andréka--van Benthem--Németi 1998 article and compare it
   against the inspected 1996 preprint, especially §4.6 and the finite-model
   statements.
5. Obtain a readable Löwenheim 1915 original/authoritative translation and a
   reliable Behmann 1922 transcription or authoritative edition. The Behmann
   scan is complete, but scan possession alone does not establish exact symbols
   and proof text.

No item in this blocking list can be discharged by copying the corresponding
later book presentation.

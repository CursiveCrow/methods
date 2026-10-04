# Feder--Vardi MMSNP/CSP reduction: source note

Retrieved 2026-08-22. Scope: the reduction statement required for Part IX,
the connected-input qualification, the complete proof in the live
author-hosted manuscript, the difference between computational equivalence and
literal class equality, and Kun's later derandomization. This note certifies
the author-copy proof content and author-copy pagination; it does not claim
that the final SIAM typeset body was directly inspected.

## Result safe to state

Feder and Vardi's 1998 journal result has two distinct claims.

1. The class of fixed-template finite CSP problems is contained in MMSNP.
2. For every problem definable in MMSNP, there is a CSP problem with which it
   is polynomially equivalent, with asymmetric reductions:

   - from the **MMSNP problem to the CSP problem**: a deterministic
     polynomial-time Karp reduction;
   - from the **CSP problem to the MMSNP problem**: a randomized
     polynomial-time Turing reduction.

For the second direction, if inputs to the CSP problem are restricted to
connected structures, the journal text strengthens the randomized Turing
reduction to a **randomized Karp reduction**. The word *randomized* must not be
dropped. For a disconnected input, the construction is applied to its connected
components and their answers are combined, which is the stated reason for the
general Turing reduction.

This is not literal equality of problem classes. CSP is a proper subclass of
MMSNP as an extensional collection of languages: some MMSNP-definable problems
are not themselves fixed-template CSP problems. The correspondence is instead
problem-by-problem computational equivalence under the reductions above.

Kun's later result removes the randomness from the sparse-incomparability step
used in the CSP-to-MMSNP direction. It does not alter Feder--Vardi's original
attribution, turn strict inclusion into literal equality, or retroactively make
the 1998 construction deterministic.

## Feder--Vardi sources

### Official final-journal record -- directly inspected

Tomás Feder and Moshe Y. Vardi, “The Computational Structure of Monotone
Monadic SNP and Constraint Satisfaction: A Study through Datalog and Group
Theory,” *SIAM Journal on Computing* 28(1), 57--104 (1998), DOI
[10.1137/S0097539794266766](https://epubs.siam.org/doi/10.1137/S0097539794266766).

The official SIAM page exposes the bibliographic record and abstract, not the
article body in this environment. The abstract says that the authors show that
“all problems in this class reduce to the seemingly simpler class CSP.” It does
not state the reduction types. Consequently, the official page establishes the
final publication identity and abstract-level direction only; it cannot by
itself establish the Karp/Turing or connected-instance qualifications.

### Complete first-party author copy -- directly inspected

Tomás Feder's live [Stanford publications page](https://theory.stanford.edu/~tomas/)
links both its conference and journal entries to the first-party PostScript
file [constraint.ps](https://theory.stanford.edu/~tomas/constraint.ps). The
retrieved file had these properties:

- HTTP status `200`, content type `application/postscript`, and content length
  `486897` bytes;
- last-modified value `Wed, 30 Jan 2002 22:32:51 GMT`;
- SHA-256
  `0808A6E91B49465838F0D4D7C5124656493A0BF2515F7478E014FB2F254F798C`;
- PostScript header `%!PS-Adobe-2.0`, internal title `constraint.dvi`, and 53
  pages.

Its title page bears the complete journal title and names Feder and Vardi. It
is therefore a complete author-hosted manuscript of the work, not a SIAM
facsimile. The PostScript was converted locally to PDF and text solely for
read-only inspection; pages 1 and 10--13 were also rendered and visually
checked. No handbook or publication PDF was generated.

The directly inspected locators are:

- author-copy p. 10: the relational-girth definition and **Theorem 5**;
- author-copy pp. 10--11: the complete proof of Theorem 5;
- author-copy p. 12: **Theorem 6** and the beginning of its proof;
- author-copy pp. 12--13: the complete proof of Theorem 6.

Theorem 5 fixes integers `k,d`. From every `n`-element relational structure
`S`, it constructs in randomized polynomial time a polynomial-size structure
`S'` of relational girth greater than `k`, with `S' -> S`, such that for every
same-signature structure `T` of size at most `d`,
`S' -> T` iff `S -> T`. The source's relational girth condition is exact: any
at most `k` relation occurrences of arities `r_i` must mention at least
`1 + sum_i(r_i - 1)` elements. It is not merely girth in the Gaifman graph.

The proof proceeds as follows.

1. Make `N=n^s` copies of every element of `S`.
2. For each lifted occurrence of an original `r`-ary relation, retain it
   independently with probability `N^(1-r+epsilon)`; put unary relations on
   all copies.
3. Delete one relation occurrence from every cycle using at most `k`
   occurrences. For each fixed underlying short-cycle pattern, the expected
   number of copied realizations is at most `N^(k epsilon)`; after accounting
   for polynomially many underlying patterns, Markov's inequality bounds the
   number of deletions by `2N^delta` with constant positive probability.
4. Projection to the original elements gives `S' -> S`, and hence
   `S -> T` implies `S' -> T`.
5. Conversely, for a homomorphism `h:S' -> T`, at least `N/d` copies of each
   original element have one common `h`-value. For any prescribed choices of
   such subsets, each original `r`-ary occurrence has expected
   `N^(1+epsilon)/d^r` retained lifts. A Cherno bound, followed by a union bound
   over the polynomially many original occurrences and at most `2^(rN)`
   subset choices, makes this simultaneous for all choices.
6. Taking `s` large and `epsilon` small makes the short-cycle deletions lower
   order than the surviving supply. The majority values therefore preserve
   every original relation and define `S -> T`.

The proof ends by saying that derandomization remains open; this is the step
later addressed by Kun.

Theorem 6 in this live author copy has the same number as the indexed final
journal theorem, not Theorem 5. Its exact statement is: CSP is contained in
MMSNP; every MMSNP problem is polynomially equivalent to a CSP problem; the
CSP-to-MMSNP direction is a randomized Turing reduction, while the
MMSNP-to-CSP direction is a deterministic Karp reduction. On connected CSP
instances the first direction becomes a randomized Karp reduction, and the
general case is handled component by component.

Its complete proof has these source-specific steps.

1. Write the MMSNP matrix as a conjunction of negated conjunctions and split
   each into biconnected components. The source defines the relevant syntactic
   condition by exclusion: the conjunction cannot split into disjoint parts or
   into parts sharing only one articulation variable.
2. For disjoint parts `A(x)` and `B(y)`, introduce an existential zero-ary
   truth-valued symbol `p` and replace `not(A and B)` by
   `(A -> p) and (B -> not p)`. For parts meeting only at `z`, introduce an
   existential unary symbol `q(z)` and use the analogous two implications.
3. Before decomposition, add every variable-identification instance of each
   forbidden conjunction. Handle an input relation whose arguments are all
   identified, when it occurs with other input relations, by a fresh monadic
   proxy and an implication from the repeated-argument input atom.
4. For the input-atom conjunction `C` in each forbidden pattern, introduce a
   fresh input relation `R_C` whose arguments are all distinct variables of the
   entire forbidden conjunction, and replace `C` by `R_C`. Add the source's
   closure instances when the input conjunction of one forbidden pattern is a
   sub-conjunction of another.
5. An original input maps deterministically to the expanded signature by
   declaring `R_C` exactly where `C` holds. Naively expanding `R_C` back to `C`
   can create implicit occurrences assembled from several explicit tuples;
   the paper gives a triangle example.
6. Choose `k` larger than every replaced conjunction and apply Theorem 5. In a
   structure of relational girth greater than `k`, biconnectedness forces each
   such implicit forbidden occurrence to lie within one explicit relation
   occurrence, where the sub-conjunction closure already accounts for it.
7. With no zero-ary existential symbols, form a finite template whose elements
   are the allowed complete truth assignments to the monadic existential
   predicates at one element; each input relation contains exactly the tuples
   of such types not forbidden by the normalized formula.
8. With zero-ary symbols, case-split their truth assignments, form templates
   `T_i`, take their disjoint union, add a binary relation holding exactly
   within each `T_i`, and restrict the Karp correspondence to connected inputs
   so a homomorphism lands in one `T_i`. Disconnected inputs are queried
   componentwise, producing the general randomized Turing reduction.

This complete author-copy proof closes the mathematical reconstruction. What
remains open is comparison against the final SIAM typesetting and its journal
pagination, not the proof content itself.

### Final-journal Theorem 6 -- search-indexed text, typeset body not fetched

A public journal-volume PDF is indexed at
[the SIAM Journal on Computing volume-28 scan](https://www.electronicsandbooks.com/edt/manual/Magazine/S/SIAM%20Journal%20on%20Computing%20%28SICOMP%29/PDF/V28.pdf).
Direct opening timed out, so the full PDF and proof were not freshly inspected.
The search index nevertheless exposes the heading and opening proof text of
**Theorem 6**, immediately before Section 5. The indexed theorem states both
containment and polynomial equivalence and identifies a “randomized Turing
reduction” in one direction and a “deterministic Karp reduction” in the other.
Its indexed proof opening expressly calls the connected-input improvement a
**randomized Karp reduction** and says that disconnected instances are handled
component by component.

Provenance limit: this is exact search-index extraction from a publicly indexed
copy, not a claim that the mirror is first-party, that its rights status was
independently established, or that the complete final proof body was inspected.
The theorem number and wording are corroborated below by directly readable
first-party and institutional sources.

### Older Vardi-hosted full-version lead -- designation inspected; linked PDF now dead

Vardi's [first-party publications page](https://www.cs.rice.edu/~vardi/papers/)
labels an older linked paper the “full version of STOC'93 paper with T. Feder.”
The linked author-hosted file is
[stoc93rj.pdf](https://www.cs.rice.edu/~vardi/papers/stoc93rj.pdf), which returned
404 on direct opening. Search indexing of that first-party URL exposes
**Theorem 5** and the beginning of its proof. Theorem 5 gives the same overall
directions as journal Theorem 6: randomized polynomial-time Turing from CSP to
MMSNP and deterministic Karp from MMSNP to CSP. Its proof opening says only
“Karp reduction” for connected CSP instances; the final journal wording is more
specific and controls: **randomized** Karp reduction.

This dead Vardi URL is a historical lead, not the live complete copy described
above. The accessible Feder-hosted manuscript numbers the high-girth lemma
Theorem 5 and the MMSNP/CSP correspondence Theorem 6. The dead URL's indexed
numbering must not be used to relabel the live source.

The [official ACM record for the STOC 1993 paper](https://doi.org/10.1145/167088.167245)
confirms the conference presentation, “Monotone monadic SNP and constraint
satisfaction,” pp. 612--622. It does not replace the unavailable long-version
body.

## Directly readable corroboration

### Kolaitis--Vardi institutional chapter -- first-party coauthor source

Phokion G. Kolaitis and Moshe Y. Vardi, “A Logical Approach to Constraint
Satisfaction,” in *Finite Model Theory and Its Applications*,
[author-hosted Rice PDF](https://www.cs.rice.edu/~vardi/papers/ircsmv7.pdf),
Section 1.5, **Theorem 1.8**, printed p. 17.

Theorem 1.8 gives the same two directions: randomized Turing from the CSP
problem to the MMSNP problem, and deterministic Karp from the MMSNP problem to
the CSP problem. The immediately preceding prose also supplies a direct
nonidentity witness: triangle-freeness is MMSNP-definable but is not
`CSP(G)` for any finite graph `G`. A footnote on the theorem reports that Kun
had announced a derandomization; it does not attribute that derandomization to
Feder and Vardi.

This chapter directly verifies the theorem statement and literal-class
nonidentity, but it omits the connected-instance qualification.

### Madelaine--Stewart institutional journal copy -- detailed restatement

Florent Madelaine and Iain A. Stewart, “Constraint Satisfaction, Logic and
Forbidden Patterns,” *SIAM Journal on Computing* 37(1), 132--163 (2007),
[institutional author copy](https://www.lix.polytechnique.fr/~madelaine/Download/SicompFinal.pdf),
Section 3, **Theorem 3.2**, printed p. 8.

Theorem 3.2 says that every CSP problem is MMSNP-definable but “there are
problems in MMSNP that are not in CSP.” It then gives the Feder--Vardi
directions in unambiguous problem notation: for every MMSNP problem
`Omega`, some CSP problem `Omega'` satisfies

- `Omega` to `Omega'`: polynomial-time Karp reduction;
- `Omega'` to `Omega`: randomized polynomial-time Turing reduction.

Footnote 2 separates Kun's later derandomization from the Feder--Vardi theorem.

Source-critical warning: the explanatory parenthesis immediately following
Theorem 1.1 on printed p. 2 reverses these directions. The paper itself calls
Theorem 3.2 a more detailed reformulation, and Theorem 3.2 agrees with
Feder--Vardi's indexed journal Theorem 6, the indexed author-full-version
Theorem 5, and Kolaitis--Vardi Theorem 1.8. Use Theorem 3.2, not the p. 2
parenthesis, for reduction orientation.

## Kun's later derandomization

Gábor Kun, “Constraints, MMSNP and Expander Relational Structures,”
*Combinatorica* 33, 335--347 (2013), DOI
[10.1007/s00493-013-2405-4](https://link.springer.com/article/10.1007/s00493-013-2405-4).
The directly readable source is
[arXiv:0706.1701v2](https://arxiv.org/pdf/0706.1701), dated 13 March 2013.

The exact change is visible in three places.

- Introduction and **Theorem 1**, printed pp. 1--2: Feder--Vardi's sparse
  incomparability step is described as a randomized polynomial-time
  transformation to an equivalent large-girth CSP instance. Kun supplies a
  deterministic polynomial-time construction preserving CSP membership for
  every template below a fixed size bound.
- **Theorem 2**, printed p. 2: for an MMSNP language `L`, Kun gives
  polynomial-time reductions in both directions between `L` and
  `CSP(T)`.
- Section 5, **Theorem 12**, printed p. 10: the Feder--Vardi portion is
  isolated as a polynomial-time reduction from `L` to `CSP(T)` and a
  polynomial-time reduction from the large-girth restriction of `CSP(T)` back
  to `L`. Kun's deterministic Theorem 1 supplies the formerly randomized step
  from arbitrary CSP instances to that large-girth restriction.

Kun's notation requires one qualification. At the end of Section 2, printed
pp. 3--4, he defines `CSP(T)` for a finite set of templates `T` as the union of
the individual `CSP(A)` languages and calls languages of that form the class
CSP. Therefore a handbook sentence that insists on a single fixed template
must cite Feder--Vardi/Kolaitis--Vardi for that formulation, or separately
explain the finite-family encoding; it must not silently replace Kun's finite
set by one template.

The publisher record confirms publication on 3 July 2013, volume 33,
pp. 335--347. The arXiv v2 body was directly inspected; the subscription-only
publisher body was not.

## Evidentiary disposition for Part IX

| Item | Disposition | Safe consequence |
|---|---|---|
| Feder--Vardi theorem statement and reduction directions | **CLOSED** by the complete Feder-hosted author copy, agreeing indexed final text, and directly inspected first-party/institutional restatements | State deterministic Karp from MMSNP to CSP and randomized Turing from CSP to MMSNP. |
| Connected-instance qualification | **CLOSED IN THE AUTHOR-COPY STATEMENT AND PROOF** | State randomized Karp for connected CSP inputs and componentwise handling for disconnected inputs; do not call the connected reduction deterministic. |
| Literal class equality | **REFUTED** | State proper containment at the language-class level and computational equivalence problem by problem. |
| Kun's contribution | **CLOSED** against arXiv v2 and the publisher record | Attribute deterministic large-girth construction and removal of randomness to Kun, separately from Feder--Vardi 1998. |
| Feder--Vardi complete author-copy proof content | **CLOSED** against the live 53-page first-party PostScript, author-copy pp. 10--13 | Reconstruct Theorems 5--6 and their proofs in independently written prose, using author-copy locators. |
| Final SIAM typeset comparison and journal-page proof locators | **OPEN** | Do not describe the author file as a SIAM facsimile or convert its author pagination into journal pagination. |

A lawful, directly readable complete author copy was found on Feder's live
Stanford site. The SIAM page still exposes only the abstract, the older Vardi
link is dead, the public volume scan timed out, and the ResearchGate download
link returned 403. The remaining gap is therefore limited to the final SIAM
typeset comparison and journal-page proof locators. It no longer blocks the
mathematical proof reconstruction.

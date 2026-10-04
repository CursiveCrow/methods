# ALC with general TBoxes: source acquisition and exact complexity scope

Date: 2026-09-06.

## Outcome

The full bodies of Chapters 2, 4, and 5 of Baader, Horrocks, Lutz, and
Sattler's *An Introduction to Description Logic* (2017) were not acquired
from the checked author and university routes. The author's public
resources are exercises, solutions, ontologies, and lecture slides.

Three earlier primary author/publisher PDFs were acquired and read in the
relevant scope. They support an accurately attributed replacement for the
active complexity ceiling:

1. An author draft of Baader, Horrocks, and Sattler's **Description
   Logics**, published as Chapter 3 of *Handbook of Knowledge
   Representation* (2008), explicitly states ALC concept satisfiability
   under general TBoxes is ExpTime-complete: **Theorem 6, draft p. 26**.
2. Donini and Massacci, **EXPTIME tableaux for ALC** (2000), proves the
   deterministic single-exponential upper bound for the exact concept and
   general-TBox input: **Theorems 3.11-3.13, printed pp. 97-98**, with the
   complexity proof in Section 6, especially **Theorem 6.17, p. 123**.
3. De Giacomo and Lenzerini, **Boosting the correspondence between
   description logics and propositional dynamic logics** (1994), supplies
   a general finite-KB upper bound through a richer DL:
   **Theorem 8 and Corollary 9, p. 211**, with the unique-name convention
   explicitly stated on p. 210. Its richer-language hardness result must
   not be used as ALC-fragment hardness.

The elementary transfers below establish the exact finite-KB statement
under the manuscript's semantics and supply a direct deterministic
exponential upper bound. They are independently supplied mathematical
arguments, not a reconstruction attributed to unread 2017 chapters.

## 1. Actual manuscript scope inspected

At the time of inspection, `handbook/parts/p09/logic-in-computer-science.tex`
contains:

- Definition `def:p09-alc`, lines 291-323: full Boolean ALC, arbitrary
  binary roles, nonempty interpretation domain, finite general GCIs, and
  finite ABoxes with precisely `C(a)` and `r(a,b)` assertions. Distinct
  individual names are **not** required to denote different elements.
- Method `def:p09-alc-tableau`, lines 333-411, and theorem
  `thm:p09-alc-tableau`, lines 413-419: the handbook's separate blocking
  procedure and its stated correctness/termination theorem, including an
  optional tested concept and an anonymous root for otherwise rootless
  input.
- The ALC system card, lines 431-433; comparison row, lines 453-459; and
  complexity table row, lines 2291-2295: classification withheld because
  the 2017 chapter body is unavailable.

`handbook/parts/p09/presentations/n-c-009.tex`, lines 819-843, distinguishes
the 2003 first edition from 2017. Lines 827-835 already report the 2017
chapter record's summary-level classification, including finite-KB
consistency. Thus the host's blanket withholding is narrower than the
classification already stated in N9. The new sources support a substantive
mathematical treatment with explicit provenance. They do not establish
that the handbook's particular blocking rule has the optimal time bound.

## 2. The 2017 acquisition result

Book: Franz Baader, Ian Horrocks, Carsten Lutz, and Uli Sattler,
*An Introduction to Description Logic*, Cambridge University Press,
2017, DOI [10.1017/9781139025355](https://doi.org/10.1017/9781139025355).

Exact official chapter records:

- [Chapter 2, A Basic Description Logic](https://www.cambridge.org/core/books/abs/an-introduction-to-description-logic/basic-description-logic/B0A5B63F8FED20CE48E28F6CC3C41AD5),
  pp. 10-49, DOI `10.1017/9781139025355.002`.
- [Chapter 4, Reasoning in DLs with Tableau Algorithms](https://www.cambridge.org/core/books/an-introduction-to-description-logic/reasoning-in-dls-with-tableau-algorithms/B207BCE75953DDA9F38636213B809A77),
  pp. 69-105, DOI `10.1017/9781139025355.004`.
- [Chapter 5, Complexity](https://www.cambridge.org/core/books/abs/an-introduction-to-description-logic/complexity/28FF8265D9C77A0886D75CADBB337A42),
  pp. 106-139, DOI `10.1017/9781139025355.005`.

Chapter 5's publisher summary explicitly distinguishes no/acyclic TBoxes
from general TBoxes and says its classifications also apply to the
corresponding KB consistency problems. This is a readable author summary,
but not the full chapter or its detailed proof.

The [Oxford author book site](https://www.cs.ox.ac.uk/Ian.Horrocks/dlbook/)
links [resources](https://www.cs.ox.ac.uk/Ian.Horrocks/dlbook/resources.html)
whose actual outgoing links were inspected: chapter exercises/solutions
`ex2-sol.pdf`, `ex2+sol.pdf`, `ex3.pdf` through `ex8.pdf`, and two OWL
ontologies. It did not link a full book or the requested chapter bodies.
Sattler's [Manchester homepage](https://www.cs.man.ac.uk/~sattler/)
points readers to the textbook. Targeted Dresden, Bremen, Oxford, and
Manchester searches did not expose a downloadable author book version.

Baader's [Dresden 2017-2018 course](https://lat.inf.tu-dresden.de/teaching/ws2017-2018/DL/)
explicitly describes the book download as available through SLUB within
the TU Dresden network. Its public chapter materials are lecture slides;
the page says proofs are given on the blackboard. The public
[Chapter 5 handout](https://lat.inf.tu-dresden.de/teaching/ws2017-2018/DL/dl4ho.pdf)
was downloaded: 42 PDF pages, copyrighted to Franz Baader. Its indexed
content includes the exact ALC/general-TBox classification as Theorem
5.13 and labels the preceding game-reduction lemma's proof as blackboard
work. It is saved as a separate lecture source; its acquisition does not
count as acquisition of the textbook's Chapter 5. Most of this PDF's text
is graphical and was not recovered by plain PDF text extraction, so no
physical-page locator for Theorem 5.13 is claimed here.

## 3. Exact earlier source: Baader-Horrocks-Sattler chapter

Publication metadata: Franz Baader, Ian Horrocks, and Ulrike Sattler,
**Description Logics**, Chapter 3 in Frank van Harmelen, Vladimir
Lifschitz, and Bruce Porter (eds.), *Handbook of Knowledge
Representation*, *Foundations of Artificial Intelligence* 3, Elsevier,
2008, pp. **135-179**, DOI
[10.1016/S1574-6526(07)03003-9](https://doi.org/10.1016/S1574-6526(07)03003-9).
The publisher controls the publication year and final pagination. Oxford's
author bibliography gives 135-180, but the publisher gives 135-179.

The acquired [Oxford author PDF](https://www.cs.ox.ac.uk/people/ian.horrocks/Publications/download/2007/BaHS07a.pdf)
is an author draft: its first page says 2007 and has placeholder volume
front matter; its 47 pages are numbered 1-47. Cite **draft** page and
theorem locators below rather than silently applying them to the final
publisher pagination. The [author bibliography](https://www.cs.ox.ac.uk/people/ian.horrocks/Publications/selected_bib.html)
connects this exact file to the 2008 chapter.

Relevant locators:

- **Definitions 1-3, draft pp. 5-6:** exact ALC concept grammar,
  nonempty-domain semantics, and finite arbitrary GCIs.
- **Definitions 4-6, draft p. 7:** finite ABoxes with concept assertions
  and positive atomic-role assertions; KB pairs; concept satisfiability
  and subsumption under a KB. These definitions impose no injectivity
  condition on individual names. The text writes `x:C` where the
  manuscript writes `C(x)`.
- **Section 3.5.2, draft p. 19:** ExpTime hardness sketch via an
  alternating-polynomial-space/PDL reduction. It explains how a
  single-role formula of the form `C ∧ [r*]D` becomes concept `C` under
  the one-GCI TBox `{top ⊑ D}`. The full machine reduction is omitted.
- **Section 3.6.1, draft pp. 21-26:** looping-tree-automata upper-bound
  construction; **Proposition 5, draft p. 26**, equates satisfiability
  with automaton nonemptiness; **Theorem 6, draft p. 26**, states the
  ExpTime-completeness result for concepts under general TBoxes.
- **Footnote 8, draft p. 21:** mentions the pre-completion extension to
  ABox reasoning. The direct KB argument in Section 6 below avoids
  making this footnote bear an unstated reduction.

This is an exact earlier primary author presentation of the theorem, not
a claim that these three authors originated its hardness proof. The
chapter cites prior research and omits the full hardness construction.
Also, the sentence before Proposition 5 calls the explicit automaton
construction a polynomial reduction, although the subsequent state bound
is exponential. Use its stated exponential size and the independent
algorithm below; do not reproduce that wording as a polynomial-size
automaton claim.

## 4. Original algorithm paper: Donini-Massacci 2000

Francesco M. Donini and Fabio Massacci, **EXPTIME tableaux for ALC**,
*Artificial Intelligence* **124**(1) (November 2000), pp. **87-138**,
DOI [10.1016/S0004-3702(00)00070-9](https://doi.org/10.1016/S0004-3702(00)00070-9).
The complete 52-page publisher-formatted PDF is linked from
[Massacci's university publication page](https://disi.unitn.it/~massacci/Publications/index.html)
and was acquired from its [PDF link](https://disi.unitn.it/~massacci/Publications/doni-mass-00-AIJ.pdf).

**Section 2, pp. 90-92**, defines the exact Boolean ALC grammar,
nonempty-domain interpretations, finite unrestricted inclusions, and the
input concept's nonempty extension in a model of all inclusions. This
paper uses `KB` for the **TBox**, not for an ABox/TBox pair. It supplies no
ABox input to the theorem in question.

**Theorems 3.11 and 3.12, p. 97**, connect closed/open tableaux to
unsatisfiability/satisfiability. **Theorem 3.13, p. 98**, states that every
strategy respecting its seven prescribed search techniques terminates
in single deterministic exponential time in the size of the concept and
TBox. Section 6 proves the bound; **Theorem 6.17, p. 123**, bounds the
DFS calls by `O(2^(c n))`, then derives Theorem 3.13 again.

The techniques include reuse of discovered inconsistent concept sets,
rule priorities, and depth-first search. The result is not a complexity
bound for arbitrary terminating blocking tableaux. No transfer of that
optimal bound to the manuscript's separately displayed tableau is
licensed merely by their common soundness/completeness.

## 5. Earlier KB upper bound and the unique-name issue

Giuseppe De Giacomo and Maurizio Lenzerini, **Boosting the correspondence
between description logics and propositional dynamic logics**, Proceedings
of AAAI-94, AAAI Press/The MIT Press, 1994, pp. **205-212**.
The [official AAAI PDF](https://cdn.aaai.org/AAAI/1994/AAAI94-032.pdf)
is the acquired 8-page source.

Section 2, p. 207, defines finite general TBoxes in a language extending
ALC by regular role constructors. Section 5, p. 210, defines finite
ABoxes with `C(a)` and `R(a,b)` and explicitly requires distinct individual
symbols to denote distinct elements. **Theorem 8 and Corollary 9,
p. 211**, give a polynomial reduction to an extended PDL and
ExpTime-complete reasoning for its `CF` knowledge bases. ALC with atomic
roles is a syntactic fragment of `CF`, yielding the upper bound, but
hardness for `CF` does not imply hardness for that fragment.

The manuscript's omission of a unique-name assumption causes no problem
for **this exact ALC satisfiability language**. Here is an independent
proof, not an appeal to an unstated convention.

Let `I` model an ALC KB, possibly interpreting two input names by the same
element. Let `J` be a nonempty finite index set with a distinct index
`j_a` for each name occurring in the input. Form `I'` with domain
`Delta^I × J`; interpret each atomic concept by `A^I × J`, and set

`((d,i),(e,j)) in r^(I')` iff `(d,e) in r^I`.

Assign `a^(I') = (a^I,j_a)`. Induction over ALC concepts gives
`(d,i) in C^(I')` iff `d in C^I`: for each base-role successor every
index-copy is available, and every copied edge projects to a base edge.
Thus all GCIs and concept assertions are preserved, every asserted
positive role edge is preserved, and the input names now denote distinct
elements. The converse follows simply by forgetting the injectivity
requirement. If the input has no names, use one index. Unused symbols can
be omitted from the finite signature; no whole-signature finite-domain
UNA is being assumed.

This argument does not apply unchanged to languages with nominals,
functionality, counting, or individual equality. None of these occurs in
the active definition. It also preserves finiteness of an existing finite
model.

When using the 1994 ABox reduction for an empty ABox, first add
`top(a_*)` with a fresh name. This satisfiability-preserving step ensures
that the reduction's individual-creation part supplies a state on which
the global constraints are enforced. The manuscript already handles the
corresponding nonempty-domain case by its anonymous initial root.

## 6. Exact theorem and elementary KB transfer

### Statement suitable for the manuscript

For the active ALC grammar with nonempty-domain interpretations, the
following problems are **ExpTime-complete in combined input size**, under
polynomial-time many-one reductions:

- Given a concept `C` and a finite general TBox `T`, is `C` nonempty in
  some model of `T`?
- Given `C,D,T`, does every model of `T` satisfy `C ⊑ D`?
- Given a finite KB `(T,A)` with the displayed `C(a)` and `r(a,b)` ABox
  assertions, does it have a model?
- Given additionally a tested concept `C0`, is there a model of `(T,A)`
  in which `C0` is nonempty?

Here both the TBox and ABox are parts of the varying input; the statement
is not a data-complexity claim. Names need not be distinct, though adding
the UNA does not change these satisfiability problems by Section 5.

The first result can be cited directly to the acquired author chapter,
Theorem 6. For subsumption, use `C ⊑_T D` iff `C ∧ not D` is
unsatisfiable under `T`, and `C` is unsatisfiable under `T` iff
`C ⊑_T bottom`. ExpTime is closed under complement, so both the upper and
lower bounds transfer. The finite-KB hardness reduction is
`(C,T) -> (T,{C(a_*)})`, with a fresh individual.

### Direct upper bound under the exact KB syntax

The following independent construction is sufficient; it is not claimed
to be the algorithm printed in any of the acquired papers.

Normalize all concepts and internalized GCIs into negation normal form.
Let `E` contain their sub-concepts, the NNF complement of each, and
`top,bottom`. Include the optional tested concept when present. Its size
is linear in total input length `N`, up to an inessential fixed encoding
factor.

A Boolean type is a subset `t` of `E` satisfying these finite conditions:
exactly one of every complementary pair belongs to it; `top` belongs to
it and `bottom` does not; conjunction and disjunction membership have
their usual iff truth conditions; and each internalized GCI belongs to
it. For each input role `r`, put `t R_r u` iff every `forall r.D` in `t`
has `D` in `u`.

Start with all Boolean types and repeatedly delete a type `t` when it
contains `exists r.D` but there is no remaining `u` with `t R_r u` and
`D in u`. This process reaches a greatest surviving set `S`. Every type
realized in an actual model survives: its actual existential witness
realizes a compatible surviving type at every stage. Conversely, on the
domain `S`, interpret atomic concepts by type membership and each role
by all compatible pairs. The complete-type conditions and the surviving
existential obligations give the truth lemma for every member of `E`.
In particular, the negation of `forall r.D` is `exists r.not D` in NNF;
this ensures the reverse direction of the universal truth clause.

For a nonempty set of named ABox individuals, enumerate maps
`f: Ind(A) -> S`. Accept a map exactly when every asserted `C(a)` has
`C in f(a)` and every asserted `r(a,b)` has `f(a) R_r f(b)`. For a
rootless KB require `S` to be nonempty. If a tested concept is present,
also require some `t in S` containing it. A model induces such choices.
Conversely the canonical type model, with names interpreted by `f`,
satisfies the KB and realizes the tested concept if requested. Different
names may select one type, as the semantics allows; the copying argument
of Section 5 supplies distinct realizations if desired.

There are at most `2^|E|` types. All compatibility tests, deletion rounds,
and existential-witness searches can be performed in `2^poly(N)` total
time. There are at most `(2^|E|)^|Ind(A)| <= 2^O(N^2)` candidate maps,
each checked in polynomial input/label time once `S` is available. This
is a deterministic exponential-time algorithm in the combined input.
The lower bound above applies already with one concept assertion and no
asserted role edges.

Finally, adding `C0(a_*)` for a fresh name is an exact linear reduction
of the optional tested-concept problem to KB satisfiability. Conversely,
the optional-concept problem contains ordinary KB satisfiability by using
`top` as the tested concept. Empty TBoxes, empty ABoxes, and no role
names are all covered; the nonempty-domain test on `S` remains essential.

## 7. Acquired files and fingerprints

All source copies are under `tmp/sources/p09-alc-general-tbox/`.

| File | Pages | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `baader-horrocks-sattler-2008-chapter.pdf` | 47 | 386851 | `2558CB6443723FA480D0247D85E59C316662B5BAA2813840E72307DE67526CE1` |
| `donini-massacci-2000.pdf` | 52 | 411304 | `FA629F8794BDBFD09EE33A30C6576A8943957EFA0211D39071DE8971443A7795` |
| `de-giacomo-lenzerini-aaai-1994.pdf` | 8 | 1450752 | `1C4CB638E39E3044A5BFBB2B2E3316B1562EC5970427D47539996E93F5505CF6` |
| `baader-2017-2018-chapter5-slides.pdf` | 42 | 13278032 | `0A9E95BC8643262BF37D8FBA984F22F83219B0D99CA98B5B266D50EF7173BF5B` |

The 2008 draft and 2000 paper were read at their actual definition,
theorem, and proof-architecture locators above. The 1994 paper's KB
construction and source scope were read. No complete reproduction of
their research proofs or independent audit of every lemma is claimed.
No software test, manuscript build, or manuscript render was performed.

## 8. Incorporation recommendation and proof limits

State the exact combined-complexity theorem directly, citing the acquired
earlier chapter for the concept/general-TBox classification and supplying
the elementary KB transfer. Cite Donini-Massacci only for its own
optimal-strategy theorem if that historical algorithm is discussed.
The 2017 chapter can remain a corroborating reference, with the precise
source-acquisition distinction retained here in the research record.

Do not attribute the new type-elimination proof, the name-copying lemma,
or the manuscript's existing blocking rule to an unread 2017 chapter.
The absent 2017 chapter body still prevents a source-controlled account
of its exact worked examples and proof organization. It no longer
prevents an accurately sourced, independently explained ALC complexity
theorem under the manuscript's actual language and semantics.

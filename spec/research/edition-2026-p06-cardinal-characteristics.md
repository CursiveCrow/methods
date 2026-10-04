# P6 cardinal characteristics: authoring packet and exact source scope

Date: 2026-10-03. Status: authored, not independently reviewed, not routed
or rendered. Only the assigned new files are modified. The research skill
was used for primary-source retrieval and this single persistent note;
its default child-agent workflow was not used because this assignment
explicitly prohibited children.

## Current allocation and manuscript seam

Read the actual proposed TOC chapter 78, especially literal rows 78.1
(*Combinatorial cardinal characteristics of the continuum*), 78.2
(*Invariants of measure and category*) and 78.3 (*Inequalities and
consistency separations*), `spec/proposed-table-of-contents.json:4123--4150`.
Read the exact `ED26-SRC-002-007` and `ED26-SRC-002-008` queue records,
including SETUP, DEVELOPMENT, CASES and APPARATUS. Each requires the
entire exact allocated chapter, not this selected core. Their destination
records remain the source-specific P5 paths; this P6 subject packet is
not a unilateral remapping.

Current neighboring text actually read: the regularity definitions and
analytic/coanalytic boundaries in
`handbook/parts/p06/descriptive-set-theory.tex:178--242`; the Cohen,
random and collapse forcing catalog in
`handbook/parts/p06/forcing-variants-supplement.tex:52--98`.
The former introduces meagerness and universal measurability, but not
the four ideal invariants. The latter does not compute their values from
the continuum cardinality. Contracts and the full conventions were read
before writing; in particular proofs live in reciprocal annexitems,
seven-column symbol intakes remain separate, and cal-M/cal-N remain
reserved structure metavariables.

Insertion seam for root: body input after the measure/category vocabulary
and before characteristic-specific forcing or topology applications;
annex input through the live P6 annex route. Files:

- `handbook/parts/p06/cardinal-characteristics-and-inequalities.tex`
- `handbook/annex/p06/cardinal-characteristics-and-inequalities.tex`
- `handbook/bib/intake-p06-cardinal-characteristics.bib`
- `handbook/registry/symbols-intake-p06-cardinal-characteristics.csv`

No route, canonical bibliography, registry master, coverage ledger, receipt,
or existing frozen forcing packet is edited by this worker.

## Sources and actual reading

Primary proof source: [Fremlin's author-issued chapter 52 PDF](https://www1.essex.ac.uk/maths/people/fremlin/chap52.pdf),
section 522A--Q, printed pp. 17--23, internally **version of 11 July
2023**. The contents page's older revision date is not used to date this
section. The chapter's other sections carry their own revision dates;
there is no claim to have read or adopted the whole chapter.
Read the extracted full A--Q proof interval, lines 1000--1407, and the
[actual author TeX](https://www1.essex.ac.uk/maths/people/fremlin/chap52.tex)
522H closed-witness interval, lines 3793--3879, to retain closures lost by
PDF text extraction. See the dedicated `SOURCES.md` for frozen hashes.

Primary combinatorial source: [Blass, arXiv math/9407203v1](https://arxiv.org/pdf/math/9407203v1),
12 July 1994, introduction and Section 2 through the dual b/r inequality,
printed pp. 1--4, extracted lines 1--170. This supplies the exact
b/d/s/r conventions, interval splitting map, and its dual. It is a
different work from the allocated 2010 Handbook chapter.

The exact original Handbook allocations remain:

- Blass, *Combinatorial Cardinal Characteristics of the Continuum*,
  printed pp. 395--489, [original chapter DOI](https://doi.org/10.1007/978-1-4020-5764-9_7).
- Tomek Bartoszynski, *Invariants of Measure and Category*, printed
  pp. 491--555, [original chapter DOI](https://doi.org/10.1007/978-1-4020-5764-9_8).

Those original bodies have not been acquired/read in this block. Their
whole setup, development, cases, apparatus and edition differences remain
open rather than credited from Fremlin or the 1994 preprint.

Two legitimate prepublication bodies were subsequently located and frozen
without changing that original-manifestation statement:

- [Bartoszynski, arXiv math/9910015v1](https://arxiv.org/pdf/math/9910015v1),
  4 October 1999, 49 PDF pages, explicitly submitted as a prospective
  Handbook chapter. Read **Sections 1--3 completely**, printed pp. 1--13,
  extraction lines 1--707. Only the opening paragraph of Section 4 was
  exposed; its arguments and all later sections are unread. In Sections 2--3
  the same four invariants are embedded in Borel master-set and Borel
  morphism constructions; those definability claims are additional
  obligations, not automatic consequences of the present arbitrary-map
  witness constructions.
- [Blass's author-hosted `hbk.pdf`](https://sites.lsa.umich.edu/ablass/wp-content/uploads/sites/1471/2025/10/hbk.pdf),
  linked from his [actual author paper list](https://sites.lsa.umich.edu/ablass/set-theory-papers/)
  as the prospective chapter, 104 PDF pages. It is held, but the local
  extraction has broken glyph encoding and **the body is unread**.
  Internal version/date and equivalence with the published 2010
  manifestation remain unqualified; the 2025 URL upload directory does
  not date the mathematical text.

## Constructions supplied

Eleven reciprocal proved claim/annex pairs are written (authored status,
not independent proof admission):

1. Four-invariant ideal square, singleton and choice witnesses, Borel
   base bound, and regularity of ideal additivity.
2. Countable function diagonal, b regularity, dominating/unbounded
   distinction, countable splitting diagonal, alternating finite interval
   splitter, and b/r dual bound.
3. Proper null/meager sigma ideals, G-delta/F-sigma bases, explicit dense
   null G-delta and its conull meager complement; neither ideal inclusion.
4. Eventually bounded nowhere dense cones, plus direct real-line
   inverse-distance coding from the rationals and closed nowhere dense
   real witnesses. No homeomorphism helper is required.
5. Closed category witnesses Phi(f), protective interval choices,
   Baire localization inside Phi(f), and eventual recovered bound Psi(A).
6. Category add=min and cof=max identities, with direct common
   translation and rational-neighborhood codes; no omitted sequential
   composition lemma.
7. Both crossing cov/non bounds using translates and reflections.
8. Both null/localization map directions, explicit independent dyadic
   events, compact support outside a null set, product estimate, finite
   slalom widths, and summable rational interval codes.
9. Countable finite-intersection open-family helper, localization of
   meager covers, composition into a meager/null containment bridge,
   and the add/cof witness transfer.
10. Full classical Cichon generating inequality network assembled only
    from the supplied proof routes.
11. CH endpoint collapse for ten diagram invariants and s/r.

Worked boundary cases additionally distinguish eventual from pointwise
domination, unbounded from dominating families, and eventual slalom
matching from infinitely-often matching. None proves a strict inequality
between the corresponding least cardinalities.

## Source conventions and reconstruction differences

Fremlin writes `cf` for the cofinality of an ideal; this packet uses
`cof` and reserves cardinal cofinality for `cf(kappa)`. His initial b/d
presentation uses order-theoretic add-omega/cofinality on pointwise
function order and then proves its equivalence with eventual domination
in 522C. Blass's Section 2 starts directly with eventual domination;
the packet adopts that explicit convention.

Fremlin's generalized Galois--Tukey comparison direction and Blass's
morphism direction differ by convention. The packet avoids identifying
their arrow symbols: each map pair is stated by its actual implication
and the induced cardinal comparison is separately proved.

Bartoszynski 1999 v1 uses `cof`, eventual domination, both Cantor-product
measure and Lebesgue domains, master-set codes and **Borel** morphisms.
Its Theorem 3.12 relies on parameter-uniform coding/selection lemmas
3.6--3.9 in addition to the numerical containment transport. The packet
does not claim those definable upgrades for the arbitrary set-based maps
it supplies. The historical attribution in that 1999 draft credits the
category additivity identity to Miller/Truss and the cofinality identity
to Fremlin, whereas Fremlin 522J groups the two identities under a
Truss/Miller reference. These are preserved source referrals, not a new
adjudication of historical priority.

The category-coding reconstruction uses inactive stages with no selected
set and protective closed intervals explicitly, and uses a countable
eventual diagonal bound. It is a complete local construction, not a claim
that the literal choices in the source were transcribed unchanged.
The independent open events are built by disjoint binary digit blocks;
the positive compact support is built directly by a short open null
cover and removal of countably many zero-measure basic parts, so no
unwritten inner-regularity proof is needed for that helper.

## Exact remaining work and verification standing

The full classical ZFC inequality network has a written proof route at
the stated domains. Background measure input remains the ordinary
Lebesgue measure/outer-measure construction, countable subadditivity,
interval lengths, open null covers and binary cylinder probabilities;
these are not reconstructed as an entire measure-theory foundation here.
Baire's complete-metric argument is supplied in the real-ideals annex.
The real-line category/domination proof uses an explicit inverse-distance
code instead of importing the usual irrationals/Baire-space homeomorphism.

No characteristic-specific strict consistency separation, forcing
preservation theorem, exactness-of-Cichon-models theorem, Martin's-Axiom
computation, or topology application is supplied. In particular a
Cohen continuum-cardinality proof is not credited as an invariant-value
proof. Next required source step is the exact full 2010 chapter bodies;
next mathematical step for 78.3 is a separately selected strict
separation with its forcing witness and preservation arguments.

No independent review, tests, build or render was run, per assignment.
Proof statuses denote this authored construction only. Root must merge
the two intakes, select the live insertion route and assess source-specific
fulfillment without changing the original denominators.

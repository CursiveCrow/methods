# P16-C1: finite logical abduction

Date: 7 September 2026. Author: `/root/standard_pa_argumentation_source_review`.
Assigned block: 23:07-23:52 UTC, with a concrete progress report sent before
23:22. The body and complete annex were written before that checkpoint; the
final notation/source-bridge pass and handoff followed within the block.

Status: **WRITTEN**, with complete author readback. Fresh source, topic and
publication reviews, root integration, production evidence and admission
remain due. This is an author/source-intake note, not independent acceptance.

## Frozen outputs

| Artifact | Complete extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p16/finite-abduction.tex` | 1-340, complete new chapter | `AB9195BA7C823075CAFBF3EAD98EFCC5CB754696F0C42D27EF108A5B9303A5FF` |
| `handbook/annex/p16/finite-abduction.tex` | 1-283, five complete annex items | `35B9C51F77801CBFFC7B372B7DD9BB67FAFC2033E29BE5F29453DB756C8EA2B9` |
| `source/references/eiter-gottlob-abduction/eiter-gottlob-abduction-jacm-manuscript.pdf` | 46 physical pages, unnumbered title page then numbered pages 1-45 | `E2A021C45BCDC6D2D1BC7AAC9972E75FEC697E3609094060CA92AFFCB694F265` |

The note's own digest is returned after its final write/readback.

The chapter defines finite background theories, permitted positive-atom
hypotheses, positive-atom observations, consistency plus explanatory
entailment, subset-minimal explanations and minimum-cardinality explanations.
It supplies an exhaustive finite construction and proves soundness,
completeness, exact selection of both minimality families, termination and
the exact count of candidate/valuation pair inspections for that construction.
It also proves the single-deletion criterion, calculates all explanation
families for six explicit inputs, and gives a countervaluation to inferring
the explanatory hypotheses from the observations.

## Holdings check and identified primary source

Before acquisition I searched the current source/reference and temporary
holdings by abduction/Eiter/Gottlob filenames and inspected matching canonical
bibliography entries. Existing related holdings included the Kakas abduction
PostScript and its derived PDF under `tmp/acquisition/src035/`; those concern
a different named treatment and were not treated as this source. No Eiter-
Gottlob abduction body or matching bibliography entry appeared in those
checks. Existing Gottlob1992, DantsinEiterGottlobVoronkov2001 and bi-abduction
records have different titles and scopes.

The selected primary treatment is Thomas Eiter and Georg Gottlob, *The
Complexity of Logic-Based Abduction*, in the complete manuscript manifestation
freely hosted by TU Wien at the
[institutional PDF locator](https://dbai.tuwien.ac.at/staff/pichler/complexity/eiter1995.pdf).
The actual title page names both authors, their Christian Doppler Laboratory
for Expert Systems and Institut fuer Informationssysteme at Technische
Universitaet Wien, and the article title. Its footnote states that an extended
abstract appeared at STACS 1993. The PDF has a separate unnumbered title page
and numbered text pages 1-45; its final physical page carries printed page 45
and references 69-74. The formal definitions used here occur on printed
pages 9-11.

This held source is an **undated manuscript manifestation**, not a capture of
the journal's printed pages 3-42. Its PDF metadata names `jacm.dvi` and records
conversion in December 2006; that conversion date is not a publication date.
The file is 419,030 bytes, 46 A4 pages, unencrypted, PDF version 1.3, with
dvips/ESP Ghostscript producer metadata. Its exact version for this unit is
the identified institutional manifestation and hash above.

[Eiter's own publication archive](https://www.kr.tuwien.ac.at/staff/eiter/et-archive/)
separately identifies the 1992 technical report CD-TR 92/35 and a revised
publication in *Journal of the ACM* 42(1), 3-42 (1995). The
[Oxford institutional journal record](https://ora.ox.ac.uk/objects/uuid%3A2e84b813-adcc-409f-893a-ee0dc0384778)
identifies the journal DOI as `10.1145/200836.200838`. These records establish
the related publication identity; they were not used to pretend that the
46-page manuscript has journal pagination or that its text was compared
byte-for-byte with the revised journal version. The chapter cites the
manuscript-specific intake key and its actual printed pages.

The authorized download completed from the institutional PDF URL on
7 September 2026 using `curl --fail --location`. An initial ordinary-shell
directory creation and TLS attempt failed; the requested named-directory
permissions and an approved command escalation allowed the same scoped
download to complete. The saved PDF was not edited or re-exported.

## Actual primary-source reading

The following complete physical pages were read as extracted text and
visually inspected from the saved PDF, rendered at 115 dpi:

| Physical page | Printed location | Reading purpose |
| --- | --- | --- |
| 1 | Unnumbered title page | Exact title/authors/affiliation, abstract, STACS-version footnote. |
| 2 | p. 1 | Introduction and the initial theory/hypothesis/manifestation explanation criterion. |
| 5-6 | pp. 4-5 | Preferred-solution discussion, subset and cardinality criteria, and the surrounding broader preference/probability boundaries. |
| 10-12 | pp. 9-11 | Complete formal abduction subsection: language and finite theory conventions; Definitions 2.1-2.5; hypothesis/manifestation restrictions; both selected preference orders; Proposition 2.1 and its proof; neighboring Lemma 2.2 and decision-query scope. |
| 46 | p. 45 | Last numbered leaf and final references, confirming the retained manifestation's endpoint. |

All eight selected pages were read in full; the other 38 pages were not read.
The complete required definition and single-deletion passages for this unit
are included. Source-page PNGs were temporary intermediates outside the
repository and were removed after inspection. No manuscript page was built
or rendered.

## Source conventions and the explicit extension

| Source evidence | Treatment in the new unit |
| --- | --- |
| Section 2 language paragraph, p. 9 | A finite theory over a finite propositional alphabet, with classical two-valued semantics. The book's `Prop`, primitive syntax and truth clauses are used. The source's truth constant and biconditional are translated to the existing abbreviations; the first annex proves truth preservation by induction. |
| Definition 2.1, p. 9 | The source tuple is `(V,H,M,T)`, with finite V, H and M subsets of V, and consistent finite T. The chapter retains the tuple order and all finite/atomic restrictions. |
| Definition 2.2 and surrounding paragraphs, p. 10 | Explanations are subsets of H for which T plus the selected atoms is consistent and entails every manifestation. H and M need not be disjoint, and their union need not exhaust V. Positive atoms alone are permitted in H and M. The chapter's `Expl` corresponds to source `Sol`. |
| Definition 2.3 and subset/cardinality discussion, pp. 10-11 | `MinExpl` and `CardExpl` are exactly the selected subset and cardinality comparison criteria. The body does not identify these formal comparison rules with a probability or a causal ordering. |
| Proposition 2.1 and proof, p. 11 | The chapter supplies the single-deletion characterization with a full proof. In the converse, consistency of the one-atom deletion follows from its being a subset of the known consistent explanation, while entailment follows from the smaller explanation. |

The source assumes consistent T at input formation. The chapter explicitly
extends the input type to include inconsistent T, then proves that
`Mod_V(T union E)` is a subset of `Mod_V(T)` for every candidate, so no
explanation exists in that additional case. It does not omit the explanation
consistency conjunct or use vacuous entailment to accept inconsistent data.
On the source's consistent inputs the two models agree, after the stated
alphabet naming and connective-abbreviation translation. Naming preserves
candidate subsets, inclusion and cardinality.

The new exhaustive procedure and the finite family-existence proofs are
handbook deductions from these definitions. They are not attributed as the
source's exact algorithm. The only operation count claimed is exactly
`2^(|H|+|V|)` candidate/valuation pair inspections in the prescribed
unshortened nested scans. Formula evaluation and filtering are explicitly
additional finite work. No complexity class, optimality claim, search-class
completeness result, oracle algorithm or source complexity proof is supplied.

## Complete results and proof locations

| Body result | Body start | Complete annex item/start |
| --- | --- | --- |
| `thm:p16-abduction-semantics` | 82 | `annex:p16.abduction-semantics`, annex 11: local/global valuation equivalence; source notation bridge; inconsistent background, empty explanation and empty observation cases. |
| `thm:p16-abduction-minimality` | 145 | `annex:p16.abduction-minimality`, annex 71: finite minimality existence; cardinal-minimal implies subset-minimal; incomparability; qualified upward closure; both directions of single-deletion characterization. |
| `thm:p16-abduction-enumeration` | 219 | `annex:p16.abduction-enumeration`, annex 128: membership-vector bijections; flag invariants; soundness/completeness; exact two-family filters; no duplicates; finite termination and pair-inspection count. |
| `thm:p16-abduction-examples` | 262 | `annex:p16.abduction-examples`, annex 184: complete candidate/model calculations for all six declared inputs. |
| `thm:p16-abduction-truth-boundary` | 304 | `annex:p16.abduction-truth-boundary`, annex 268: one valuation makes the observation and background true while every permitted hypothesis is false. |

All five body theorem statuses have matching `annexitem` records with exact
backreferences. Every new proof is inside its annex item. No new style or
calculus infrastructure was introduced.

## Required cases and complete example outcomes

| Input | All explanations | Subset-minimal explanations | Minimum-cardinality explanations | Concrete boundary |
| --- | --- | --- | --- | --- |
| `P_inconsistent`: T = {a, not a}, H = {a}, M = {m} | empty family | empty family | empty family | Both possible candidates fail consistency despite vacuous entailment. |
| `P_given`: T = {m}, H = {a}, M = {m} | {empty set, {a}} | {empty set} | {empty set} | The observation already follows without hypotheses. |
| `P_empty`: V = H = M = T = empty | {empty set} | {empty set} | {empty set} | One empty explanation and one empty valuation exist. |
| `P_sizes`: T = {a -> m, (b and c) -> m}, H = {a,b,c} | {{a},{a,b},{a,c},{a,b,c},{b,c}} | {{a},{b,c}} | {{a}} | The two minimal explanations are incomparable and have different sizes. |
| `P_constraint`: T = {a -> m, not(a and b)}, H = {a,b} | {{a}} | {{a}} | {{a}} | {b} is consistent and non-explanatory; {a,b} is inconsistent. |
| `P_permitted`: T = {z -> m}, H = {a} | empty family | empty family | empty family | {a} is consistent and non-explanatory; {z} is sufficient and consistent but excluded because z is outside H. |

In the last three nonempty-variable cases the observation set is {m}; their
full V sets and all six complete tuples are declared at body lines 238-260.
Every positive claim has a satisfying-valuation argument and every failed
entailment has a displayed or explicitly specified countervaluation in the
annex. The `P_sizes` exact criterion is: a candidate explains iff it contains
a or contains both b and c. This proves the entire family rather than only
exhibiting two chosen explanations.

The truth boundary uses `a = b = c = False`, `m = True` in `P_sizes`.
It satisfies T and M, and falsifies a as well as b and c. Therefore neither
selected minimal explanation follows from the observations. The body also
states the language/semantics boundary: material implications and permitted
assumptions do not supply causal relations, interventions, actual-world
selection, temporal order or probabilities.

## Exact root intake and integration seams

The new citation key is `EiterGottlobAbductionManuscript`. It was absent from
the canonical bibliography at authoring time. Root can add the following
record through its owned bibliography intake:

```bibtex
@unpublished{EiterGottlobAbductionManuscript,
  author  = {Eiter, Thomas and Gottlob, Georg},
  title   = {The Complexity of Logic-Based Abduction},
  note    = {Undated manuscript, with an unnumbered title page followed by
             pages 1--45; TU Wien institutional copy. The local pagination
             is distinct from the 1995 Journal of the ACM publication},
  url     = {https://dbai.tuwien.ac.at/staff/pichler/complexity/eiter1995.pdf},
  urldate = {2026-09-07},
}
```

No publication year or journal DOI is asserted for the undated manuscript
record. Its associated 1995 journal article remains a distinct bibliographic
manifestation. Citations in the new chapter intentionally say "manuscript"
and use its printed pages 9-11.

Required root-owned input seams are:

```tex
\input{parts/p16/finite-abduction}
\input{annex/p16/finite-abduction}
```

The body belongs to stable P16, printed XII in the approved nineteen-part
order. It has chapter anchor `sec:p16-finite-abduction` and five section
anchors. The annex has `sec:annex-p16-finite-abduction` and its five result
items. Root owns the chapter/annex wrappers, input order and canonical
records; these files do not supply or change those drivers.

Notation intake, scoped to `sec:p16-finite-abduction`:

| Notation | Typed role / first declaration |
| --- | --- |
| `mathcal P = (V,H,M,T)` | Finite input tuple; `def:p16-abduction-input`. V is atoms, H permitted atoms, M observed atoms, T finite formula set. |
| E, F, D, E_0 | Candidate/explanation subsets of H; D and E_0 are local proof sets. |
| `mathsf Val(V)` | Functions from finite V to the existing Boolean truth-value set B; `def:p16-abduction-models`. |
| `operatorname Mod_V(Gamma)` | Finite valuation model set of formulas over V; same definition. |
| `Gamma entails M` | Abbreviation for entailment of each observed atom, declared at the same definition. |
| `operatorname Expl(P)` | Explanation family; `def:p16-abduction-models`, corresponding to source Sol. |
| `operatorname MinExpl(P)`, `operatorname CardExpl(P)` | Subset-minimal and minimum-cardinality subfamilies; `def:p16-abduction-minimality`. |
| n, r | Cardinalities of V and H in the enumeration method. |
| `mathcal L`, `mathcal L_subseteq`, `mathcal L_#` | Enumeration output lists, viewed as families in the output theorem; `def:p16-abduction-enumeration`. |
| Six `mathcal P` case subscripts | Explicit finite input constants; `def:p16-abduction-examples`. |

The chapter reuses the existing `Prop`, `B`, `False`, `True`, `bottom`,
`topv`, `defeq`, entailment and CPL connective interfaces. Prerequisite
anchors are `sec:prop-syntax-semantics-01`,
`sec:prop-syntax-semantics-02` and `lem:prop-coincidence`. The actual syntax
and semantic source files were read before using these interfaces.

## Author verification and remainder

Read the complete edition contract and the research/PDF skills. The research
skill guided primary-source tracing and this single repository note. The
explicit assignment prohibited subagents, so the source work was performed
directly. The PDF skill guided actual source-page inspection. The complete
body and annex were read after writing; the long displays, enumeration order
and source connective/alphabet bridge were then refined, followed by another
complete readback of the final 340-line body and 283-line annex.

The mathematical verification in this block was direct author reasoning:
all proof directions, flag invariants, finite counts, minimality claims and
every complete example calculation were checked against the definitions.
This is not an independent review. No tests, numerical test program,
manuscript build/render, canonical bibliography/symbol edits, driver edits,
formal admission or subagent dispatch occurred. Only the two assigned new
manuscript files, this note and the one named primary-source PDF were created
in the repository. Other agents' work was preserved.

The precise remaining scope includes fresh independent reviews and all
integration/production/admission gates for this unit; additional forms of
abduction and hypothesis languages with proved translations; arbitrary
preference orders, weights and priorities; the source's remaining results
and complexity proofs; first-order and logic-programming treatments;
consistency-based diagnosis; probabilistic and causal explanation; and the
broader P16-C1/explanation obligations. The bounded finite foundation does
not claim their completion.

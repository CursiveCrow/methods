# Logic and reasoning coverage additions

Date: 9 September 2026. Source cutoff: 7 September 2026.

This note accompanies `spec/coverage/edition-2026/thinking-gaps/logic-reasoning.jsonl`.
It records eight finite findings: one absent named system, five insufficiently
specified source or reader treatments, one already catalogued but unwritten
family, and one present coverage control. Six proposed unit identities are
listed; the lead must reconcile their component relations with the other
shards before adding them to the master. The manuscript was not edited.

The classification is about the identified treatment. It does not infer that
an entire field is absent merely because a particular author's presentation
is missing. Existing historical, philosophical, formal and empirical treatments
remain owed.

## Retrieved Content

The following quotations are short, literal source extracts. All editorial
scope decisions and comparisons follow in Supplementary Notes.

### Source 1: Pratt-Hartmann and Moss, author preprint, Section 1, preprint p. 3

[Logics for the Relational Syllogistic, arXiv:0808.0521v1](https://arxiv.org/pdf/0808.0521v1).
Retrieved 9 September 2026. The arXiv history identifies the sole version as
4 August 2008; the linked 2009 journal publication is a related manifestation.

> our contribution should not be read as a historical
> reconstruction.

### Source 2: Icard, Moss and Tune, proceedings paper, Section 9.1, p. 84

[A Monotonicity Calculus and Its Completeness](https://aclanthology.org/W17-3408.pdf).
Retrieved 9 September 2026. ACL identifies MoL 2017, pp. 75–87, DOI
10.18653/v1/W17-3408.

> It emphasizes the fact that we take open assertions
> in hypothesis sets Γ to be “universally quantified.”

### Source 3: Ciardelli, Chapter 4, Section 4.1

[Inferences with Propositional Questions](https://link.springer.com/chapter/10.1007/978-3-031-09706-5_4).
Retrieved 9 September 2026. Publisher open-access chapter, 2023, pp. 103–121.

> Without this restriction, the rule would not be sound.

The preceding source sentence specifies that classical-disjunction elimination
has a restriction to classical conclusions.

### Source 4: Wiśniewski, Section 4, Theorem 14, p. 10

[An Axiomatic Account of Question Evocation: The Propositional Case](https://awisniew.web.amu.edu.pl/publikacje/axioms-05-00014-v2.pdf).
Retrieved 9 September 2026. The author's publication page directly links this
14-page publisher-layout PDF for the 2016 Axioms article.

> Theorem 14 (Completeness). Let X be a finite set of wffs.

The finite-premise qualification is part of the selected theorem. The
`v2` filename is preserved literally, without inventing an edition date.

### Source 5: Aristotle, Internet Classics Archive, translation identity and Chapter 4

[On Sophistical Refutations](https://classics.mit.edu/Aristotle/sophist_refut.1.1.html).
Retrieved 9 September 2026.

> Translated by W. A. Pickard-Cambridge

> There are two styles of refutation: for some depend on the language used, while some are independent of language.

The page does not supply the translation's bibliographic publication year.
The selected continuation is
[Section 2](https://classics.mit.edu/Aristotle/sophist_refut.2.2.html).

### Source 6: List and Pettit, author preprint, first page and Appendix

[Aggregating Sets of Judgments: An Impossibility Result](https://personal.lse.ac.uk/LIST/PDF-files/AGG1.pdf).
Retrieved 9 September 2026. The body is a 33-page author preprint despite its
PDF metadata title `Microsoft Word - AGG2.DOC`.

> revised 9 October 2001

> Theorem 1. There exists no judgment aggregation function F generating
> complete, consistent and deductively closed collective sets of judgments

The omitted continuation of the theorem requires the three explicitly defined
conditions (U), (A) and (S). This extract is not a standalone theorem statement.
The [LSE publication record](https://researchonline.lse.ac.uk/00000704/) identifies
the subsequent 2002 journal article, pp. 89–110; body identity is not presumed.

### Source 7: Current manuscript, expert-opinion appraisal

`handbook/parts/p18/argument-schemes-and-critical-questions.tex`, lines 141–144.
Read 9 September 2026.

```tex
Expertise and trustworthiness are distinct: a technically competent source
can be unreliable on an occasion, and an honest source can lack the
required expertise. Disagreement invites examination of methods and
evidence; counting expert names does not resolve it.
```

### Source 8: Current manuscript, witness appraisal

`handbook/parts/p18/argument-schemes-and-critical-questions.tex`, lines 266–270.
Read 9 September 2026.

```tex
The position-to-know and truth-telling premises remain part of the
scheme even though the five-question list does not repeat them word
for word. Questions about visibility, memory, and reporting conditions
may examine those premises. Do not treat several retellings of one
person's story as independent corroboration.
```

## Supplementary Notes

### Governing scope and method

I read the research skill, the edition contract, the map-shard contract and
the corrected `decisions/handbook-of-thinking-scope-2026-09-09.md`.
This work follows the user-approved handbook of logic and reasoning scope.
It adds explicit inference questions, finite source extents, conditions,
procedures, proofs and countercases. It does not create general cultural,
productivity or self-help chapters.

The research skill is being applied through this background research
assignment and this single primary-cited note. All changes are map records.
No authoring, build, render, manuscript tests or independent review was run.

I searched the current `handbook/**/*.tex` and `handbook/**/*.bib` trees for
question, syllogistic, diagram, polarity, fallacy, testimony and judgment
aggregation terminology, including alternative stems. I then inspected the
matched actual LaTeX, not the manuscript PDF. In particular, I read the
expert/witness sections and closing scope boundary of the argument-schemes
chapter, the related scheme-classification passages, the social-choice
declarations, and the historical chronology entry.

The catalog comparison loaded all 615 original requirement rows and searched
their source-unit records, all 118 current reasoning units, all 96 benchmark
units, all 18 additional methods, all 26 domain assignments and all 12
mandatory-family rows. It loaded only the active historical content-unit files
listed by the first-half block 4 manifest and tail version 12 manifest:
340 and 332 historical units respectively. Superseded revisions were not
unioned. Pending SRC-052–068 coverage was checked with its current mapper;
those messages are further evidence, not a substitute for the lead's eventual
canonical identifier check.

Exact comparison input hashes:

| Input | Records | SHA-256 |
| --- | ---: | --- |
| requirements-crosswalk.jsonl | 615 | 197185294A0896C53D3839FC2CA19421C84F74D90E424CED12F1EAF2F065E76F |
| current-reasoning-units.jsonl | 118 | EEC66EB18CC1A10A4A9F07AE69B3F386E81E59C7C2A37D711DC3658B8375D855 |
| benchmark-content-units.jsonl | 96 | A15ADAA38DB5B0463B94E8EF57A82A241BB19449EDB3FEE3154F83AD14357FC6 |
| additional-method-units.jsonl | 18 | DF4CBBE73771AD97278FEA3C867189742D69418F522C13D017A1319C771260CF |
| new-domain-crosswalk-v3.jsonl | 26 | E2F5A82772BDD39F118F62931F4EA51EDBE0E4E9531AD43DB7DA9A8CE34B806D |
| mandatory-family-crosswalk-v2.jsonl | 12 | 99CC3DF7792BB3DA9B695080C3CFB97FB169997EFDEF3F405842B0457CE78EEF |

All paths in that table are beneath `spec/coverage/edition-2026/`.
Requirement workers may publish later hashes. These hashes bound this
comparison; they do not freeze anyone else's work.

### Eight findings and their integration decisions

| Finding | Classification | Exact integration decision |
| --- | --- | --- |
| LR-001: categorical syllogistic | insufficient_scope | Retain the historical and psychological units; add the explicitly selected modern S/S-dagger calculus and its empty-term comparison. |
| LR-002: monotonicity/polarity | insufficient_scope | Link generalized quantifiers and RAT2021 Natural Logic to a separately attributed complete 2017 calculus. |
| LR-003: InqB | absent_from_catalog | Add the finite propositional system from Ciardelli 2023 Chapters 2–4; older question semantics is not this source. |
| LR-004: PMCE question evocation | insufficient_scope | Add the selected 2016 finite-premise calculus and compare raising a question with resolving one. |
| LR-005: diagram calculi | catalogued_but_missing_text | Complete existing Hammer, Sowa and benchmark units; create no duplicate topic unit. |
| LR-006: fallacy/refutation diagnosis | insufficient_scope | Bind the existing Woods history chapter and add only the missing original-source or task-interface components after comparison. |
| LR-007: judgment aggregation | insufficient_scope | Add the exact agenda-based theorem and worked profile; retain existing preference aggregation and collective-rationality sources. |
| LR-008: expert/witness appraisal | present | Preserve the existing bounded scheme treatment; no generic duplicate testimony chapter. |

LR-001 is deliberately not an absence claim about Aristotle. The historical
mapper identified these already owed primary chapter presentations:

- `ED26-SRC-063-0102`: John Woods and Andrew Irvine, *Aristotle's Early Logic*,
  volume 1 (2004), pp. 27–99.
- `ED26-SRC-063-0103`: George Boger, *Aristotle's Underlying Logic*,
  pp. 101–246. Publisher section excerpts explicitly name categorical
  syllogism, grammar/semantics, deduction and contrasted-instance inconcludence.
- `ED26-SRC-063-0104`: Fred Johnson, *Aristotle's Modal Syllogisms*,
  pp. 247–307; the new assertoric calculus does not discharge this separate
  modal treatment.

LR-001 instead selects the modern author preprint's Section 2 definitions
needed for S/S-dagger and complete Section 3. Its nonempty universe permits
empty individual predicate extensions. The modern proof must therefore
distinguish a valid universal conclusion from illicit existential import.
The rejected alternative was treating a chronology entry as a complete
syllogistic reference treatment.

LR-002 retains the source's distinction between the proved class of
structures and the full-structure completeness question left open in that
presentation. The source's result does not grant unrestricted natural-language
validity; the lexical and compositional premises themselves require support.
The [ACL publisher record](https://aclanthology.org/W17-3408/) identifies the
exact paper and freely accessible body.

LR-003 selects only the propositional foundations and inference chapters,
whose exact spans are in the
[publisher contents](https://link.springer.com/book/10.1007/978-3-031-09706-5).
The first-order and modal chapters remain different possible treatments.
The finite unit includes support semantics, inquisitive/classical connective
distinctions, rule restrictions, completeness and the proof-to-resolution
procedure. Its central failure case is an unresolved two-world state that
nevertheless satisfies excluded middle classically.

LR-004 is similarly bounded. It selects the complete 2016 article linked by
the [author's publication list](https://awisniew.web.amu.edu.pl/publications-and-talks/).
The older `ED26-SRC-014-001` Harrah chapter and
`ED26-SRC-044-0025/0026` Groenendijk–Stokhof and Ginzburg chapters keep their
own source obligations. PMCE is not silently credited with a complete general
calculus of question-to-question erotetic implication.

LR-005 is a concrete missing-writing finding, not new scope. The existing
`ED26-SRC-010-005` specifies Hammer's whole chapter, pp. 395–422, including
Venn, Peirce–Venn and existential graphs. Its
[source identity](https://doi.org/10.1007/978-94-017-0456-4_5) is exact even
though full free-body acquisition remains due. The existing
`ED26-SRC-036-005` selects Sowa's conceptual-graph chapter, pp. 213–237,
in the held 2008 handbook; the canonical destinations are
`handbook/parts/p08/sources/kr2008-chapter-05.tex` and the matching annex.
The [publisher chapter record](https://www.sciencedirect.com/science/article/pii/S1574652607030052)
confirms John F. Sowa's authorship. His freely accessible
`https://www.jfsowa.com/cg/cg_hbook.pdf` explicitly says that it has newer
references and a CGIF grammar appendix; it is not a byte-identical substitute
for the held 2008 chapter.
Mental rotation and illustrations of syntax trees are not the formal systems
specified in these two units.

LR-006 must be integrated with
`ED26-SRC-063-1110`, John Woods, *A History of the Fallacies in Western Logic*,
volume 11 (2012), pp. 513–610,
[DOI 10.1016/B978-0-444-52937-4.50010-1](https://doi.org/10.1016/B978-0-444-52937-4.50010-1).
The historical mapper verified an Aristotle section, but not a complete
thirteen-category enumeration inside the body. The newly fixed reference
task identifies the particular inference defect and what a repair supports.
It is not a claim that labeling a fallacy proves its conclusion false.
The selected public-domain translation is a distinct attributed presentation;
its passage-level overlap with Woods must be checked rather than assumed.

LR-007 preserves a source-specific subtlety: the chosen preprint's definition
of consistency rules out direct proposition/negation pairs; deductive closure
also matters. The three-person conjunction case therefore must not be judged
only by whether a literal contradiction is already written down. The
2001 author preprint and the 2002 published article are recorded separately.
The current Arrow/May chapter supplies preference-ranking comparisons, not
the proof of the selected judgment-aggregation theorem.
The historical tail mapper also identified `ED26-SRC-065-0007`, Sections
7.9.5 Group belief and merge and 7.9.6 Belief revision and social choice, in
its exact 2015 handbook source. This adjacent scope remains owed; it does
not identify an exact List–Pettit article presentation.

LR-008 is a necessary control. The actual LaTeX already distinguishes relevant
expertise, honest reporting, accurate content attribution, opportunity to know,
and independent corroboration. Its witness case explicitly refuses an
unsupported theft/identity conclusion. Its primary 2007 article is
[Godden and Walton](https://informallogic.ca/index.php/informal_logic/article/view/485);
the manuscript also has separately identified Walton 2016 source extents.
Calling generic testimony assessment missing would erase this existing work.

### Remaining construction and source work

The JSONL gives every finding a reader question, component success/failure
conditions, positive/negative case, finite source extent, exact or proposed
destinations, prerequisite roles, and writing/source standing. It contains
32 component specifications. The six proposed source/task units remain
unwritten. Freely reachable bodies were inspected online where stated, but
this assignment did not create local source captures or hashes; those records
remain `identified_missing` for local acquisition.

The historical mapper reserved the SRC-063 identifiers above from actual
publisher contents. The lead should validate their canonical file membership
when that shard is published. This is an identifier join, not an invitation
to discard existing history content or an unresolved decision about the
new finite source extents.

A final construction check must integrate these relations with the other
gap shards, particularly collective reasoning and practical inquiry. The
practical and scientific gap agents confirmed that they were not independently
adding these selected logic, question or judgment-aggregation treatments.

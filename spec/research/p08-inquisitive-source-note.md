# Inquisitive propositional logic: source and authoring record

Date: 9 September 2026. Unit: ED26-P08-inquisitive-0001. Scope: the complete
selected Chapters 2–4 of Ivano Ciardelli, *Inquisitive Logic: Consequence and
Inference in the Realm of Questions*, Trends in Logic 60, first edition,
DOI10.1007/978-3-031-09706-5. The five unit components cover support and
information content, InqB/resolutions/dependence, the exact calculus, complete
proofs and task/failure cases. The full named chapter extent also contains
the generator foundations, expressiveness, connective independence, coherence
and alternative-system results; these have been preserved rather than reduced
to only the central proof-system theorem.

## Acquired primary body and version

The publisher book page was read at
https://link.springer.com/book/10.1007/978-3-031-09706-5 and the chapter4 HTML
at https://link.springer.com/chapter/10.1007/978-3-031-09706-5_4. Publisher
metadata says copyright 2022, first online 2 March 2023 for the selected chapters;
the current book page separately dates the ebook 1 March 2023 and print 2 March 2023.
Those date roles are not collapsed into different textual editions.

Direct downloads of the publisher chapter 2/3/4 PDF links and complete-book
link returned Client Challenge HTML, not PDF bytes. Those responses were
retained with `.html` names in the source folder. No challenge was bypassed,
and the responses are not counted as acquired source bodies.

The author's University of Padua repository record,
https://www.research.unipd.it/handle/11577/3467176?mode=complete, identifies
the open publisher version and supplies this actual file:

https://www.research.unipd.it/bitstream/11577/3467176/2/23%20inquisitive%20logic%20published.pdf

Held file: `source/references/p08-inquisitive-ciardelli-2023/ciardelli-2023-published.pdf`.
It has 284 physical pages and 3462846 bytes. SHA-256:
`e77b1b15146df086e6c43fc3bec916fc09b86dc7abea42bc5c57bfc9480ae7c3`.
The title/copyright pages identify the author, series 60, print ISBN 9783031097058,
ebook ISBN 9783031097065, selected DOI and CC BY 4.0 licence. This qualifies the
held publisher-branded repository copy of the selected edition; it is not a
claim of byte identity with an inaccessible publisher-endpoint download.

Printed-to-physical source extents:

| Selected chapter | Printed extent | Physical pages in held PDF |
| --- | --- | --- |
| 2 Foundations of Inquisitive Logic | 7–53 | 24–70 |
| 3 Questions in Propositional Logic | 55–101 | 71–117 |
| 4 Inferences with Propositional Questions | 103–121 | 118–136 |

All 113 selected pages were read, including discussion, figures, exercises and
references. Text was extracted with pypdf into the full text and separate
`chapter-02.txt`, `chapter-03.txt`, `chapter-04.txt` files. The original
rule table on printed 104 was visually read from `rules-page-104.png`.
The negation bars in the three-atom dependence-function example on printed 75
were resolved from `dependence-page-75-large.png`. These are source-page
reading artifacts, not manuscript renders. The PDF skill supported this
source reading; no PDF output was authored.

## Source allocation to the authored text

Body: `handbook/parts/p08/inquisitive-propositional.tex`.
Annex: `handbook/annex/p08/inquisitive-propositional.tex`.
Rule sheet: `handbook/registry/calculi/p08-inquisitive.tex`.

| Source extent | Authored treatment and proof group |
| --- | --- |
| 2.1–2.3 | States, enhancement, general/contextual consequence, all four statement/question entailment readings, conditional dependency and die examples |
| 2.4.1–2.4.3;2.4.7/9 | Inquisitive propositions, generators, alternatives, normality and unique bases; `thm:p08-inq-bases` |
| 2.4.10–2.4.14 | Generator-intersection entailment, including the empty-premise case; `thm:p08-inq-generator-entailment` |
| 2.5.1–2.5.3;2.6 | Nested implication, deterministic/general Ramsey test, truth as singleton support and presupposition; `thm:p08-inq-implication`, basic/flatness groups |
| 2.8–2.9 | Explicit versus implicit states, accessible-state counterexamples, partition and pair-semantics bridges/limitations, modal-encoding and erotetic comparisons; `thm:p08-inq-partition-limit` supplies the stated partition obstruction |
| 3.1–3.5 | Exact classical/full grammar, support clauses, persistence, locality, truth, flatness, double negation and implication; basic/flatness/implication groups |
| 3.6 | Every recursive resolution clause, semantic normal form, finite generators/alternatives, premise-set resolutions and the exact contextual function example; `thm:p08-inq-resolution-semantics` and split group |
| 3.7 | Truth-conditional premises/conclusions, logical/local split and resolution, dependence functions and decision; `thm:p08-inq-split`, expressive group |
| 3.8 | Failure of arbitrary substitution and full legitimate-substitution model proof; `thm:p08-inq-substitution`; different atomic-semantics comparison retains the source's cited boundary |
| 3.9 | Both directions of finite-profile expressive completeness; `thm:p08-inq-expressive` |
| 3.10 | Elimination versus uniform definition, both primitive signatures, all non-eliminability cases, conjunction and implication undefinability; `thm:p08-inq-connectives` |
| 4.1 | All 11 primitive rule instances/families with classical side conditions and source discharge policy; `thm:p08-inq-soundness` also proves the derived classical-disjunction rules |
| 4.2.1–4.2.2 | Every proof-resolution algorithm case and constructive dependence map; `thm:p08-inq-proof-resolution` |
| 4.3.3–4.3.9 | Explicit intuitionistic distribution constructions, provable normal form, one-premise and whole-premise traceable failure, syntactic resolution/split; `thm:p08-inq-syntactic-resolutions` |
| 4.3.10–4.3.16 | Classical-theory completion, intersections and every support-lemma case, including the implication counterstate; `thm:p08-inq-support-lemma` |
| 4.3.2 final proof | Finite canonical counterstate and completeness for arbitrary sets in the countable language; `thm:p08-inq-completeness`; compactness follows from finite proofs |
| 4.4 | Questions as arbitrary supplied information and proofs as answer-transfer procedures; the die and opposite-answer derivations |

## Exercise families converted to reference cases

No new reader homework is substituted for a promised proof. The source exercise
families have the following authored results/cases:

- 2.10.1–2.10.2: all twelve code contents, the three naturally described
  alternative families, the complete 7 by 7 entailment table and 256 polar contents.
- 2.10.3: all three polar-equivalence/refinement claims, proved in
  `thm:p08-inq-polar-tasks`.
- 2.10.4: all six die implication families, with generator-based verification.
- 2.10.5: consequence toward flat conclusions and presupposition, in the
  implication proof group.
- 3.11.1: all eight four-world alternative calculations.
- 3.11.2–3.11.4: truth-set union, arbitrary-union flatness and the
  double-negation entailment, in the basic and flatness groups.
- 3.11.5: all four resolution calculations, retaining an inconsistent
  resolution rather than deleting it from the syntactic definition.
- 3.11.6–3.11.7: alternatives/flatness, standard-profile interpretation,
  local tabularity, the five one-atom classes and a detailed count of 167 classes.
- 3.11.8–3.11.10: degree bounds, each exact finite degree, the full
  InqC/2-coherent expressive characterization and the partition/polar
  characterization, in `thm:p08-inq-coherence`.
- 3.11.11: all non-eliminability claims are proved in the connective group.
- 3.11.12: persistence/profile invariance, eliminability and nondefinability
  of tensor, in `thm:p08-inq-tensor`.
- 4.5.1–4.5.3: both general inference examples and both detective
  formalizations, with full branch/discharge proofs in
  `thm:p08-inq-exercise-inferences`.
- 4.5.4: derived classical-disjunction introduction and classical-conclusion
  elimination are proved from primitive rules, without completeness.

The source's higher-degree syntactic-fragment question is retained as a
presentation problem, without asserting that its 2023 open status is still
current in 2026. First-order or modal completeness/compactness claims are
not transferred from the selected propositional proofs.

## Direct corrections and source notation

The authored text fixes the source's local typographical slips directly:
the general Ramsey-test converse assumes support of the consequent; the
flat-conclusion exercise retains the same conclusion variable; the
propositional standard-model exercise says InqB, not InqBQ; the resolution
algorithm's conjunction uses the second subproof where required, implication
indices range over the same antecedent resolution list, and falsum elimination
returns its newly constructed classical proof. The sole resolution of a
classical premise set is the singleton family containing that set, not the
set regarded as its own family. Broken source cross-reference placeholders
are not copied into reader prose.

The partition bridge explicitly includes the empty state even when the
partition has no nonempty block, avoiding an empty support proposition for
an empty presupposed domain. The primitive rules allow the source's arbitrary
number of discharges, including zero; this is a separate named calculus and
does not silently change another P2/P8 natural-deduction presentation.

The source's doubled-vee glyph is rendered by the literal composite
`\mathbin{\vee\!\vee}`. It is explicitly distinguished from the defined
classical disjunction and from tensor. No shared style macro was introduced.
The body uses `\showcalculus{p08-inquisitive}` so later apparatus reprints
can suppress repeated labels through the existing shared mechanism.

## Integration standing

The unique bibliography intake is `handbook/bib/intake-p08-inquisitive.bib`.
The unique symbol intake is
`handbook/registry/symbols-intake-p08-inquisitive.csv`.
The lead owns driver routing and canonical merges. The writer did not change
those shared files. The complete author read-through covered the entire
body, all 21 proof groups and the complete rule sheet after the writing
batch. It checked the assumptions, all proof-resolution branches, the
empty-state/intersection cases and every finite table. It removed repeated
paragraphs left by retried partial patch operations and made the global
quantification in flatness explicit. This is an author check, not independent
source/specialist/publication acceptance. No manuscript build or render,
independent review wave or new prose test suite was run.

The returned body/annex contain 21 reciprocal proved result groups, all 11
primitive rules, the worked finite tables and the source's full selected
mathematical content. There is one bibliography intake entry and 27 symbol
intake rows. Driver routing, canonical merging and later consolidated
publication checks remain with the lead. No missing source body or unfinished
proof in the selected propositional extent is being passed off as complete.

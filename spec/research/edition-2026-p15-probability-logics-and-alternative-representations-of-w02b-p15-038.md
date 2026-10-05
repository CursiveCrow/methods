# w02b-p15-038: RAT2021 4.4 Probability Logic, sections 165.1, 165.2, 165.11

Packet `work/waves/w02b/packets/w02b-p15-038.json`, label tag
`p15-w02b-p15-038`. Unit `ED26-BM-RAT2021-4-4` (C01--C05). The unit
`ED26-P15-CH-finite-probability` is a readonly unit owned by
`w02b-p15-001`; nothing of it was written here.

## Placement

In-place extension of the editable hosts, not a second chapter:

- body `handbook/parts/p15/rationality-4-4.tex` (route already in
  `handbook/parts/p15.tex`);
- annex `handbook/annex/p15/rationality-4-4.tex`.

The owned files `handbook/parts/p15/probability-logics-and-alternative-representations-of-w02b-p15-038.tex`
and the matching annex file were NOT created (A9: the existing host is the
treatment). No driver insertion is needed. Because those owned paths do
not exist, `tools/waves.py unit-compile` on this packet fails with
"File ... not found"; a scoped build of the host pair with the same
template (handbook.bib plus `bib/intake-p15-rationality-4-4.bib`) ran
pdflatex/biber/pdflatex/pdflatex with exit 0; remaining undefined
references are all cross-part labels that exist in the tree.

## Source read in this session

Held file `source/references/p15-rationality-4-4/pfeifer-2021-publisher.pdf`
(packet `units[].held_paths`), text extracted with `pdftotext -layout`
from physical pages 1--6 (printed pp. 277--282). Locators used:

- p. 278: definition (1), argument (2), (3), (4), the p(B)=1 computation
  start, coherence definition.
- p. 279: completion of the p(B)=1 computation, "counterintuitive and
  does not match the experimental data", Pfeifer & Kleiter 2011 report,
  Pfeifer 2014 proof pointer, the conclusion that the rationality
  evaluation depends on handling zero-probability antecedents, and the
  "only for positive probabilities" sentence.
- p. 280: AFP named "Abelard's first principle"; MON; System P and the
  probability-logical and possibilistic semantics pointers.
- p. 281: default reading, Gilio 2002 attribution for each System P
  rule, AND, CUT, MP; "adding monotonicity or contraposition to System P
  ... would make System P monotonic", transitivity likewise; Evans,
  Newstead & Byrne 1993 report; probabilistic MP majority report.

## What was written (this block)

1. 165.1/165.2 C02(a): subsection `sec:p15-w02b-p15-038-endpoint-argument`
   (body ~162--219): the four-step reconstruction (formal quotient step,
   empirical report, formal coherence step, conditional conclusion), the
   statement that the conclusion is a conditional claim about two
   standards and that the empirical step does not prove coherence is the
   right standard, and a numerical contrast.
2. C02(b): annex `annex:p15.rat44.coherence`, necessity direction written
   in four numbered steps (least-norm separation on the stage union,
   strict sure loss, active-union containment, subfamily inheritance) plus
   a worked first-stage-passes/second-stage-fails example
   (annex ~23--71).
3. C04 connexive/P13: subsection `sec:p15-w02b-p15-038-abelard`
   (body ~273--335) with lemma `thm:p15-w02b-p15-038-alberic` and annex
   `annex:p15-w02b-p15-038-alberic` (annex ~197--249). Links
   `sec:p13-abelard-topics`, `thm:p13-abelard-diagnostic`. Material
   differences kept: historical containment criterion vs coherent
   assessments; Pfeifer's "Abelard's first principle" is AFP, not the
   self-negation constraint; the probabilistic reading of Abelard's
   conditional is an interpretation for comparison only. The
   opposite-topic chain is not treated (no probabilistic counterpart for
   its combination step in the chapter); this is stated in the text.
4. C04 System P/Part VIII: subsection `sec:p15-w02b-p15-038-system-p`
   (body ~401--498) with `thm:p15-w02b-p15-038-threshold-and` and
   `thm:p15-w02b-p15-038-collapse`, annex items at ~336--415. Links
   `sec:p08-paraconsistent-and-nonmonotonic`,
   `thm:p08-klm-representation`, `sec:p08-klm-preferential-representation`,
   `thm:p08-klm-pref-representation`, `thm:p08-klm-soundness`,
   `thm:p08-klm-penguins`, `def:p08-klm-model`, `def:p08-klm-assertions`,
   `def:p08-nonmonotonic`, `thm:p08-rational-representation`.
   The collapse theorem proves the chapter's p. 281 claim in the Part VIII
   rule system (Transitivity: one step via Reflexivity+RW; Contraposition:
   double contraposition with RW and LLE) and shows the penguin model is
   closed under none of the three rules.
5. C05: subsection `sec:p15-w02b-p15-038-evidence-boundaries`
   (body ~574--650): Pfeifer & Kleiter 2011 (p. 279) and Evans, Newstead &
   Byrne 1993 with the probabilistic-MP report (p. 281), each with task as
   described, absent population/design/uncertainty, competing
   explanations, and generalization limits; separated from formal results.
6. Comparison list at the end of the body: the "is exact" claim removed;
   two items added pointing to the new P08 and P13 comparisons.

## Open items (not supplied)

- Gilio (2002) probability propagation rules for the System P rules
  other than AND and CUT (Or, Cautious Monotonicity, Reflexivity, Left
  Logical Equivalence, Right Weakening). The chapter attributes them to
  Gilio 2002 at p. 281 but displays only AND and CUT. Gilio 2002 is not
  in `spec/coverage/edition-2026/held-sources.json`. The body says these
  are not reconstructed.
- Primary studies (Pfeifer & Kleiter 2011; Evans, Newstead & Byrne 1993;
  Pfeifer & Kleiter 2009; Pfeifer & Tulkki 2017b) are not held; their
  claims are written only as the chapter's reports.

## Checks

- `python -B tools/find_fused_spaces.py` on both hosts: no hits.
- `python -B tools/check.py --tree handbook`: no finding names either host
  or any `p15-w02b-p15-038` label.

## Block r3 (C03 dispute: empirical-report boundaries)

Source pages re-read in the held PDF this session: pp. 277-282.

1. Aristotle-thesis report (body 261-276): states that the theorem is
   formal; names Pfeifer 2012 (must-be-true judgment) and Pfeifer &
   Tulkki 2017b (p. 280); states that materials, response options,
   proportions, sample, recruitment, design and uncertainty are not
   given; points to the boundaries subsection.
2. Line ~494 cross-reference now points to a subsection that treats the
   strengthening/contraposition report (body 504-506).
3. Truth-table report (525-543): Wason & Johnson-Laird 1972 as the
   chapter's "see, e.g." support; Kleiter, Fugard & Pfeifer 2018, Over &
   Baratgin 2017, Pfeifer & Tulkki 2017b for the semantic-match claim
   (p. 278); no proportion/population/design; competing reading.
4. Bulleted list (562-616): one item per report with the study the
   chapter attaches: PTTT task (Evans, Handley & Over 2003; Oberauer &
   Wilhelm 2003), PTTT results (Fugard et al. 2011; Pfeifer 2013),
   counterfactual (Over et al. 2007; Pfeifer & Stockle-Schobel 2015),
   abductive (Pfeifer & Tulkki 2017a), causal (no study attached in the
   chapter), AND (Pfeifer & Kleiter 2005), other System P rules (Pfeifer
   & Kleiter 2005/2006b/2010; Pfeifer & Tulkki 2017b), strengthening and
   contraposition (no citation of its own; follows the System P
   sentence), transitivity-as-CUT (Pfeifer & Kleiter 2006b/2010), MP.
   Reporting-limit paragraph extended to the truth-table and
   Aristotle-thesis reports, and to say that "supports" means "the
   chapter cites".
5. Boundaries subsection retitled "Four reports and their boundaries"
   (label unchanged); two new entries: Aristotle theses and
   strengthening/contraposition, each with task/measure,
   population/design/uncertainty, competing explanations,
   generalization.

None of the cited primary studies is held; every study attribution is
written as the chapter's citation only.

Note for tooling: the shell tool collapses doubled backslashes inside
heredocs; use chr(92) or the Edit tool for TeX text.

## Block r4 (C04 dispute: Dutch-book comparison)

Held files opened this session: `source/references/p15-rationality-4-4/pfeifer-2021-publisher.pdf`
(printed p. 278: coherence definition with the "no Dutch book" pointer to
chapter 4.1; p. 282 note 3: stakes s for every real number, random gain)
and `source/references/p15-rationality-4-1/hajek-staffel-2021-publisher.pdf`
(printed p. 240: betting account and its objections, Dutch book, the
election example, Ramsey/de Finetti and Kemeny theorems; p. 241:
pragmatic-vs-epistemic criticism, walk-away, Skyrms reply, "credences come
apart from betting prices"). The first page of each PDF carries no printed
number, so no locator was written for those pages. A grep of the full
Pfeifer text for bet/Dutch/stake/utility finds only the p. 277 betting
interpretation, the p. 278 definition and note 3: the chapter does not
discuss the 4.1 objections (stated in the body without a locator).

Written:
1. G14: "admitted" in endpoint-argument step 3 replaced by "allowed".
2. Body `sec:p15-w02b-p15-038-dutch-book` (rationality-4-4.tex 132-290):
   source link (pp. 278, 282), theorem
   `thm:p15-w02b-p15-038-dutch-book-bridge` (four items: stake reversal;
   unconditional families equal p17 sure-loss portfolios and, on 2^Omega,
   probability measures via thm:p17-finite-price-coherence; Omega-wide test
   vacuous when conditions miss a case, with the 0.6/0.6 counterexample;
   zero price permits weak loss), five material differences (outcomes
   counted, ratio vs primitive conditional, domain, weak loss vs null
   antecedents, synchronic vs diachronic), example
   `def:p15-w02b-p15-038-two-books` (ten-cent book in this language and a
   called-off book), and the H&S objections (pp. 240-241) applied to the
   two-sided stakes of def:p15-rat44-coherence, with what they do and do
   not touch.
3. Pointer sentence at the end of def:p15-rat44-coherence (58-60).
4. Comparison-list item for sec:p15-rationality-4-1 and
   thm:p17-finite-price-coherence (963-974).
5. Annex `annex:p15-w02b-p15-038-dutch-book-bridge` (annex 133-201).
6. Patch request `work/waves/w02b/patches/w02b-p15-038.json`: reverse link
   in rationality-4-1.tex after the thm:p17-finite-price-coherence
   paragraph (4-1 is not an editable host).
7. Symbol intake rows b_E, U, D/R.

Scoped build of the host pair (template from `_unit_template` with the
hosts substituted, output in the session scratchpad): pdflatex, biber,
pdflatex, pdflatex exit 0; undefined refs are all cross-part labels that
exist in the tree. `tools/check.py --tree handbook`: no finding names
either host. `find_fused_spaces.py`: no hits.

## Continuation

Remaining, not closable inside this packet:
(1) G10: `tools/waves.py unit-compile` builds the owned body/annex paths,
which do not exist because the treatment is an in-place host extension.
Needed lead change: either drop the two owned .tex paths from the packet
or have `_unit_compile_files` treat mode "accounting" like
"unit_accounting" (or build the editable hosts). Creating the owned files
would be a stub or a second treatment.
(2) G1 hard hits name spec/research files of packets w02b-p01-014 and
w02b-p02-036; this packet did not edit them (concurrent agents).
(3) The reverse link from 4-1 needs the patch request applied.
(4) Gilio 2002 propagation rules for the other System P rules (C05) still
need Gilio 2002 held.

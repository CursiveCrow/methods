# P19-E2 continuation: possibility premises and conditional interpretation

8 September 2026. Block began 18:48:06 UTC; author deadline 19:33:06 UTC.
The separate errata search was stopped around 18:57 UTC, within its 15-minute
limit. This note owns only the new chapter, matching two-proof annex and the
new capture below. Root owns shared routes, bibliography, symbols and admission.
The old suppression note was updated only with the bounded errata-search
outcome. Its frozen manuscript body and annex were not edited.

## Frozen scope and primary identity

Before drafting, the remaining empirical scope was fixed to **Cariani and
Rips, Experiment 2**. Their Sec. 2.3 explicitly introduces two new experiments;
Experiment 1 already has its own complete record in the preceding chapter.
The continuation also retains the source's actual arguments about context
expansion, reversed MP, conditional perfection and rival explanations. Its
numbered examples are arguments, not separately numbered experiments.

Fabrizio Cariani and Lance J. Rips, *Conditionals, Context, and the Suppression
Effect*, Cognitive Science 41(3), April 2017, 540-589; DOI
**10.1111/cogs.12336**. First online **1 February 2016**. The publisher labels
the article Free Access and Extended Article. Identity was read from the
actual publisher body and issue/date metadata, continuing the preceding
author-CV/PhilArchive verification; online and issue years remain distinct.

Primary: https://onlinelibrary.wiley.com/doi/10.1111/cogs.12336

New local capture:
`source/references/cariani-rips-suppression-2017/cariani-rips-complete-publisher-text-20260908.txt`

SHA-256: **7F6EDBA2513686D2BB995CAA34BF55FE4C913CC44513A9EB3726AFC43E00991A**.

This is a converted public-publisher reader capture with overlapping windows
and original reader line locators. It is not a PDF, the original HTML byte
stream, a complete rendering of inline images, or participant raw data. The
earlier selected-window capture is preserved. No new bibliographic key is
needed: use the existing `CarianiRips2017Suppression` intake/canonical entry.

## Actual read extent and image boundary

Read the complete accessible article textual body, abstract, acknowledgments,
all ten notes and references: publisher reader lines 88-975, with title and
version metadata at 15-62 and 980-984. Overlapping windows began at requested
positions 60, 180, 300, 410, 490, 580, 620 and 1030. Textual definitions and
arguments were read; inline image markers do not constitute read figures.
Section and reader line locators are used because this acquired version does
not supply per-paragraph printed PDF pagination.

Required empirical passages read: Sec. 2.3, lines 162-180; Sec. 5.4, lines
411-420; Fig. 4 caption, lines 334-338. Required interpretive passages read:
Secs. 3-4 (183-301); 5.1-5.3 (313-410); 5.5-5.6 (421-464); all of Sec. 6
(465-604), and notes 3-10 (612-629). References were read as bibliography,
not as evidence that their cited primary papers were separately acquired.

Figure 4's viewer link returned the article text rather than the graphical
asset. Its observed PowerPoint link,
https://onlinelibrary.wiley.com/action/downloadFigures?doi=10.1111%2Fcogs.12336&id=cogs12336-fig-0004&partId=
gave a reader cache miss and HTTP 403 through an ordinary public request.
The effect-size image actually linked in Sec. 5.4,
https://onlinelibrary.wiley.com/cms/asset/615c26ee-ea0e-4f15-ba7a-7c8e5fd05b3a/cogs12336-math-0004.png
likewise gave cache miss/403. The publisher article HTML request returned 403
outside the readable public text service. No barrier was bypassed. Previously
failed PDF routes were not repeated.

Consequently, exact Conjunctive and might-Disjunctive Experiment 2 percentages,
any graphical uncertainty marks, and the image-only statistic name preceding
0.413 remain unread. The manuscript says precisely this rather than assigning
bar heights or a statistic name from expectation. Source prose supplies all
reported pairwise decisions and the two focal rates. It gives no raw response
table or confidence interval for the focal contrast. The remaining figure
obligation is acquisition of a readable Fig. 4 and the actual symbol image,
then transcribing only the precision and uncertainty definition they support.

## Experiment 2 evidence retained

Population frame: introductory psychology course at Northwestern; course
requirement participation; 16 analyzed. Three prior-college-logic exclusions
are pooled over both experiments, with no per-experiment allocation. E2's
separate recruited N is not reconstructed. Demographics/recruitment dates not
reported in the methods. No probability recruitment or randomized instruction
comparison is invented.

Design: four forms, twelve contents each, 48 arguments per participant;
within-participant argument/content repetition; one screen at a time; new
random order per person; binary follows/does-not-follow decisions under an
explicit must-be-true-if-premises-true instruction. All E2 conditionals past
tense. Basic and Conjunctive unchanged from E1. Contravening and Disjunctive
replace the additional disabling conditional with an epistemic might premise.
The latter asserts neither the umbrella's actuality nor an explicit
umbrella-implies-dry conditional.

Available source rates: Basic 92%, might-Contravening 56%; derived contrast
approximately 36 percentage points. Overall F(3,45)=10.57, MSe=.092,
p<.001. Tukey HSD alpha=.05 reports Basic > might-Contravening, Basic >
Conjunctive, and might-Disjunctive > Conjunctive; no other pairwise differences
significant. No equivalence claim follows from nonsignificance.

Nominal 16 x 12 = 192 response opportunities per form, 16 x 48 = 768 total:
design arithmetic, not raw counts or independent-participant N. No counts
are reverse engineered from rounded rates. No confidence interval or
participant covariance is invented from the reported error mean square.

E1's 35% conditional-premise endorsement is used only as an explicitly
qualified between-experiment contrast. Source Sec. 5.4 itself warns that
unchanged Basic and Conjunctive forms also changed and all E2 results were
less extreme. This does not isolate a causal difference between conditional
and might wording. E2 is no direct test of reversed-order MP, AC/DA,
population transfer, or a unique psychological mechanism.

## Mathematical reconstruction and source-fidelity corrections

Two substantive statement/proof pairs, each fully written:

- `thm:p19-fixed-state-mp` / `annex:p19.fixed-state-mp`: fixed-state MP;
  compatibility does not remove premises; conditional exclusion commutes with
  accepting the antecedent; inconsistent joint antecedent with two opposed
  strict conditionals requires the nonempty-antecedent premise; explicit
  counterexample when a proposed actual world is outside the salient state.
- `thm:p19-might-expansion` / `annex:p19.might-expansion`: two fully evaluated
  expansions satisfying the same existential possibility requirement, one
  preserving q and one rejecting both q and not-q, both accepting r-or-q;
  neither accepts r; restricting the dry state to not-r restores q.

The operations E_A and E_(A,B) are defined on all subsets, including empty,
so nested expressions remain defined even if an intermediate restriction
empties the set. Acceptance as a reasoning state still requires nonemptiness.
The state subscript on Poss is preserved explicitly. The common context set
and its salient subset are distinct in the source exposition.

The source's note 4 describes two strict conditionals as inconsistent at one
state. The actual necessary qualification is retained directly: under the
Sec. 4.1 compatibility presupposition for the conjunctive antecedent they
are incompatible, whereas without it both can hold vacuously. The annex
proves both claims. Note 3's warning that the actual world need not belong
to the salient state receives its own explicit countervaluation in the same
proof. No reader is asked to repair an earlier false handbook statement.

The source's Negative Possibility is explained as a defeasible pragmatic
proposal with its own reversed-MP objection, not turned into an unconditional
semantic operation. Composite Possibility and background typicality remain
extra choices beyond existential compatibility. Conditional perfection is
retained as the source's theoretical sketch with unmeasured licenses, not
promoted to a result of E2. Mental-model, default, implicature and probability
comparisons are attributed arguments, not unseen additional study records.

## Other source boundary and integration handoff

The exact Byrne errata DOI 10.1016/0010-0277(90)90008-8 remains unread after
the separately bounded new publisher-API and library-archive avenues.
Detailed stopped-lookup record is in
`edition-2026-p19-conditional-reasoning-and-suppression.md`. Both located
March 1990 scans mark their PDF/OCR private; none was accessed. No additional
lookup remains running and no old numerical result was changed on speculation.

Root integration: add the new body after the original suppression chapter and
the matching annex after its existing two-item annex. Existing dependencies:
`sec:p19-evidence-methods`, `sec:p19-conditional-reasoning-suppression`,
`def:p02-valuation`, `thm:p19-conditional-benchmark`.
Local notation: p/q/r task atoms, Might(r) as English-task abbreviation,
W finite valuations, [A] truth set, I/S states/subsets, Poss_I(A), C_I(A,B),
E_A(S), E_(A,B)(S), I_0, J_wet/J_dry and K_wet/K_dry. No shared symbol file
or bibliography was edited.

The research skill supplied the primary-source/provenance method. Source
reading and the complete authored LaTeX batch were handled locally because
the preceding delegation attempt found no free agent slot. The PDF skill
was read for potential source acquisition; no PDF was acquired or rendered
in this continuation. No review, scanner, test, build or manuscript render
was run. All body and annex text was read as the author's mathematical and
evidence read-back, and empty-set domain and notation corrections were made
directly. The final note and last added explanation paragraphs were also read.

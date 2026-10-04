# Refutation diagnosis: selected translation, authored scope and historical join

Date: 9 September 2026. Assigned unit: `ED26-P18-refutation-diagnosis-0001`. The authoring-resumption contract, handbook conventions, current edition contract and all four allocation components govern this treatment.

## Source identity and capture

The selected source is Aristotle's *On Sophistical Refutations*, translated by **W. A. Pickard-Cambridge**, as identified by the **Internet Classics Archive**. The archive supplies no bibliographic publication year for this translation. Its ancient-work date heading and website copyright range are not used as a translation publication date.

The selected intellectual extent is **chapters 1–11 and 18–33**, twenty-seven chapters. The original map gave the first endpoint and one continuation; actual inspection of the source's table of contents showed that **three** HTML sections are needed. Section 1 contains chapters 1–10, Section 2 chapters 11–20, and Section 3 chapters 21–34. Capturing a whole HTML section does not expand the authoring assignment to the excluded chapters 12–17 or 34.

All three captures are retained under `source/references/aristotle-sophistical-refutations-mit/`:

| File and verified primary URL | Bytes | SHA-256 |
| --- | ---: | --- |
| `sophist_refut.1.1.html` — [Section 1](https://classics.mit.edu/Aristotle/sophist_refut.1.1.html) | 65,147 | `254b4eb1a01c85fe63ea4a480e94f5080917d0a0a41e322edb0ec9f4cf219a54` |
| `sophist_refut.2.2.html` — [Section 2](https://classics.mit.edu/Aristotle/sophist_refut.2.2.html) | 63,294 | `138d3b0f5ff351843bc3e67cadc56a379dfaeaa707e0e5c9177ea7c21432d7bb` |
| `sophist_refut.3.3.html` — [Section 3](https://classics.mit.edu/Aristotle/sophist_refut.3.3.html) | 62,309 | `a936a175264fee6059f3a49cd8ba04ba57ab08a1c384be41d1bf0ff9910c1441` |

The root captured the files through its authorized network route; final URLs matched requests. The worker then read the complete selected text from the local HTML and verified all three hashes. It used HTML stripping/entity decoding for reading, not a rewritten source file. Where a first large read truncated, the missing chapters were read again in complete chapter-bounded extracts. Web-source reading preceded the local reading and identified the third continuation.

The source has some imperfect transcription: a fragment beginning “He now if he has learnt his letters” in chapter 4, a duplicated paragraph in chapter 6, and missing variable letters in some general descriptions. The archive's linked [text-only version](https://classics.mit.edu/Aristotle/sophist_refut.mb.txt) also contains the chapter 4 fragment. No missing words were invented, and the duplicate was not treated as a second intellectual argument. The authored account uses the complete identifiable source examples and classifications, with the intact parallel explanations in the selected resolution chapters. It is a source-based reference treatment, not a critical edition reconstructing damaged Greek or English text.

## Files and contribution

- Body: `handbook/parts/p18/refutation-diagnosis.tex`.
- Formal annex: `handbook/annex/p18/refutation-diagnosis.tex`.
- Bibliography intake: `handbook/bib/intake-p18-refutation-diagnosis.bib`.
- Symbol intake: `handbook/registry/symbols-intake-p18-refutation-diagnosis.csv`.

The body supplies the refutation standard, the four dialogue-argument roles and five competitive aims, the thirteen source categories, their source cases and resolutions, chapters 31–33's repetition/solecism/difficulty distinctions, and an editorial procedure and lookup table for locating and repairing a particular defect. The three reciprocal proof groups establish the target/validity distinction and all explicit modern counterinterpretations and restricted valid consequences.

No new formal calculus is attributed to Aristotle. Modern Boolean, relational, quantified, numerical and two-world interpretations are explicitly introduced as reconstructions. Source arguments about explanatory relevance, dialectical concessions and proper examination remain distinguishable from modern model-theoretic validity.

## Category and resolution coverage

| Source category or topic | Source chapters | Authored location and cases |
| --- | --- | --- |
| Refutation standard; proof versus contradiction; appropriate premises | 1–3, 5–6, 8–11, 18 | Opening sections; `def:p18-rd-claim-record`; `thm:p18-rd-refutation-standard`; final limits |
| Ambiguity | 4, 7, 19, 23 | Learning/understanding, necessity and temporal description; editorial bank example |
| Amphiboly | 4, 7, 19 | Captor/captive, knowledge/sight bearer and silent person; explicit sight countermodel |
| Combination | 4, 20, 23 | Ability and current state, eyes/instrument, knowledge/location, birth/time, good person/cobbler; modal scope countermodel |
| Division of words | 4, 20, 23 | Five as two plus three and its oddness; fixed grouping and qualified expressions |
| Accent | 4, 21, 23 | Homeric readings and the source's accent-dependent house/negation example; explicit noninjective-transcription comparison |
| Form of expression | 4, 7, 22–23 | State/action, quantity/object, manner/content, retained writing/time, per-item/uniform method, predicate/individual; countermodels and source reply distinctions |
| Accident | 5–7, 24 | Coriscus, masked/approaching person, ownership/art/parenthood, small-number products; explicit relation-place and threshold cases |
| Qualified versus absolute predication | 5–7, 25 | Respect/color, being-as/being, oaths and obedience, evaluations of recipients/actions/removals/reports; fixed-context example |
| Failure of the refutation definition | 5–6, 26 | Same attribute, relation, respect, manner and time; double-of and growing-object comparisons; exact quantified contradictory |
| Consequent | 5–7, 28 | Honey/color, wet ground/rain, fever/heat, rhetorical signs, shared property, Melissus; invalid converse/inverse and valid contraposition |
| Original point assumed | 5–6, 27 | Target offered for challenge versus granted evidence; validity of reflexivity distinguished from independent warrant |
| Noncause as cause | 5–6, 29 | Soul/life assumption unused in the reductio; deletion and inconsistent-background comparison |
| Several questions as one | 5–6, 30 | Multiple subjects/attributes, mixed answers and both/all scope; valid De Morgan conclusion versus invalid componentwise denial |
| Repetition and solecism | 31–32 | Relative descriptions and illegitimate repeated expansion; noun/pronoun case, reference and grammatical-role distinctions |
| Difficulty and the adequacy of a solution | 18, 24, 33 | Premise rejection versus distinction; rejecting a conclusion versus diagnosing its argument; similar-looking cases and time constraints |

The six language categories and seven further categories remain separate even though chapter 6 offers a general reduction to failures of the refutation definition. The latter proposal is recorded as Aristotle's argument, not a proven exhaustive taxonomy for all contemporary reasoning.

## Substantive safeguards implemented directly

The chapter does not call `p entails p` deductively invalid. It locates the separate failure of independent warrant. Its account of the noncause category retains the source's unused-assumption reductio, rather than substituting a generic post-hoc-causation entry. It distinguishes legitimate extensional identity substitution from accidental sharing of predicates or an unexplained recognitional context.

The answer to a conjunction is treated by its actual Boolean meaning: denying the conjunction need not deny each conjunct. This preserves Aristotle's historical single-question discipline without pretending modern logic forbids compound propositions. A later qualification cannot narrow the original target merely to evade a counterexample. Finally, unreliable testimony can undercut support without entailing that a particular report is false; both possible factual outcomes are explicitly modeled.

Accent and solecism are read as the selected translation's linguistic cases. Its unaccented rendering is not used as proof that two differently pronounced Greek expressions are identical, nor are modern English stress or punctuation cases substituted as unchanged historical examples.

## Join with current P18 and the Woods history

Current local interfaces read were `handbook/parts/p18/argument-schemes-and-critical-questions.tex`, especially its standards, expert-opinion discussion and closing boundary, and `handbook/parts/p18/scheme-classification-and-diagnosis.tex`, especially its connected-argument assessment, historical classification account and final computational/interpretive boundary. They already distinguish premise attacks, warrant attacks and conclusion attacks. They do not supply this complete original-source thirteen-category diagnosis. The new body cross-references their existing chapter labels and does not replace their schemes or empirical claims.

The exact historical join is:

- `ED26-SRC-063-1110`: John Woods, *A History of the Fallacies in Western Logic*, **Handbook of the History of Logic 11**, 2012, chapter 10, **513–610**, DOI **10.1016/B978-0-444-52937-4.50010-1**.
- Its component `ED26-SRC-063-1110-C004` specifically preserves the complete Aristotle section 2 and requires any additional modern inference-defect index to state its own source/argument basis.
- Canonical record read: `spec/coverage/edition-2026/sources-037-068/src063-content-units.jsonl`.
- Its recorded source and content states are `identified_missing` and `missing`. The proposed body `handbook/parts/p18/presentations/src063-1110.tex` did not exist at the time of this block's check.

Accordingly, the current contribution is the independently identified MIT translation treatment plus its explicitly editorial diagnostic interface. It does **not** mark Woods's chapter, its Aristotle section or its later historical developments authored or read. There is no existing Woods prose to reuse at present, and no source-native duplicate has been claimed. When that complete body is acquired and authored, its actual overlapping argument must be compared and linked; this chapter's modern examples cannot be credited as a substitute for Woods's historical interpretation.

For LR006-C4, the identity/interface join and preservation of the separate obligation are complete. **Body-level comparison with Woods remains pending acquisition of that separate source.** This is an explicit limit on authoring credit, not an unidentified source or a new scope question.

A subsequent dedicated acquisition block checked the exact Woods chapter through publisher, former-author, institutional, local and open-access-index routes. It obtained no qualified complete body; the publisher PDF returned 403 and both OpenAlex and Semantic Scholar reported no open PDF in their records. The bounded evidence and exact continuation are in `spec/research/p18-woods-2012-source-note.md`. No source-dependent comparison was invented and no Aristotle manuscript content was changed by that acquisition block.

## Verification and remaining work

The source reading and local hash checks are complete. The formal examples are supplied with explicit counterinterpretations and positive restricted cases; they do not rely on an unimplemented classifier or a generic fallacy list. No separate proof is fabricated for a historical or philosophical claim whose evidential form is an argument.

A complete author read-through of the actual saved body, annex and both intake files was performed through the native read tool after writing. It checked the model assignments and valid restricted consequences, the distinction between implication conversion and contraposition, the quantified target, the nonvacuous reductio condition, all three reciprocal proof identities, and the source-specific classification boundaries. It made the singleton-premise abbreviation and zero-inclusive natural-number convention explicit and corrected a metalinguistic sentence to say that a valuation witnesses non-entailment. No independent reviewer or code test was used for this author read-through.

Shared driver/canonical-intake integration and later consolidated independent reviews/build/output checks remain the lead's work. No driver, canonical bibliography, canonical symbol registry, other author's content, review wave, manuscript render/build or prose-mirroring test suite was changed or run in this block. The Woods body-level overlap comparison remains the specific unfinished source-dependent item described above.

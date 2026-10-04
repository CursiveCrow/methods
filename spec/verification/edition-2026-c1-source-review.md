# C1 independent source review

Date: 7 September 2026.

## Scoped verdict

**PASS for source fidelity of the C1 corrected completion procedure in `handbook/parts/p09/presentations/n-c-010.tex`, lines 1-615, at the manuscript hash below.** No blocking source-fidelity defect was found in this correction scope. The passage identifies the two substantive repairs as handbook corrections, retains the full displayed EL++ language and all eleven completion rules, and supplies the source proof components affected by those repairs.

This is an independent source review, not formal admission, a complete review of N-c-010, or a claim that all source-content obligations for the edition have been discharged. The report-only results and broader coverage limits identified below remain outside this verdict.

The governing policy was read in full from `spec/EDITION-2026-CONTRACT.md`. In particular, lines 53-69 authorize direct correction of active mathematics, require accurate attribution of corrected procedures, and preserve separate proof obligations. I therefore did not treat replacement of the faulty unmarked procedure with an explicitly justified marked procedure as a source-fidelity failure.

## Reviewer independence and evidence

I worked as the delegated primary-source reviewer, without subagents. I did not read another reviewer report, author conclusions, or an acceptance record. The exact runtime model identifier, model version, reasoning configuration, and seed were not exposed and are unavailable. No manuscript, bibliography, source PDF, or shared record was changed. This review file is the only authored output. No manuscript compilation, rendering, static checker, or software test was run.

The first recorded clock observation in this review was 2026-09-07 13:39:28 UTC. A checkpoint was sent to the lead before 13:43:54 UTC, reporting the hashes, completed reading, and source-rule comparison. The work remained within the 45-minute assignment limit.

### Frozen material

Hashes were calculated from the local files. The three assignment hashes matched both on first inspection and on recheck before report writing.

| Artifact | SHA256 | Actual reading |
| --- | --- | --- |
| `handbook/parts/p09/presentations/n-c-010.tex` | `645f9a718b66d740948436ca5309ad25b59d39ce63acc6c41a108549cbb8ffa1` | All lines 1-615. No later manuscript lines were read. |
| `tmp/pdfs/p09-baader-brandt-lutz-2005/baader-brandt-lutz-2005.pdf` | `4c9caa8c224506123b7ee06cfcc8f5759d3537f4c241bb7e6bddcb89e0727a5a` | All six pages through the full extracted text; source page images 1-4 inspected, including Tables 1-2, Lemmas 1-3, Theorem 4, and Proposition 5. |
| `tmp/pdfs/p09-baader-brandt-lutz-2005/baader-brandt-lutz-ltcs-05-01.pdf` | `374d73eb848e556da759d89231385353996f44e6a6131f53d2794bb68d5aa3ba` | Cover and report body through printed p. 20 in the extracted text; this includes complete printed pp. 3-14 and all of Lemmas 6-7. Source page images for printed pp. 6-8 and 11-14 were inspected. Printed pp. 9-10 were additionally extracted directly from the hashed PDF. |
| `spec/EDITION-2026-CONTRACT.md` | `c9b101ad6bf6bfea5a3e1fbec25cdba81b47667146474861eb1aa00b5dfa1bf3` | Complete file, with lines 53-69 revisited for correction policy. |
| `handbook/bib/handbook.bib` | `d5bab1c74ab2b378eaacafe2ce1b313209e71e46a28dd2748ef7c539c5cb7094` | Entries at lines 5966-5974 and 5985-5993; intervening entry was visible incidentally in the search output and was not used as evidence. |

The conference layout extraction was read at lines 1-418, SHA256 `8ef7d7100bc9b0bfeee675bceade1bbbaa9fa0c524dd4ff1434463326dc5e710`. The report layout extraction was read at lines 1-994, SHA256 `5aa0fcf5767a94d8f7ef7930524d1e3a383ccefb0ef2a1a53f32a111d63c5654`. Line 994 is the opening statement on printed p. 21 and was visible incidentally; its result was not used in this review.

The report extraction has damaged glyphs. Its formulas were interpreted using the PDF page images where the reachability notation, rule variables, equivalence-class construction, and proof-rule references mattered. Existing source renderings were inspected; their generation provenance was not independently certified. The hashed source PDFs and directly extracted text remain the underlying artifacts. This is not visual verification of the handbook output.

### Source identity and statement map

The conference paper is Franz Baader, Sebastian Brandt, and Carsten Lutz, *Pushing the EL Envelope*, IJCAI 2005, pp. 364-369. The [official IJCAI 2005 index](https://www.ijcai.org/node/15) identifies the authors, starting page 364, and the linked [six-page paper](https://www.ijcai.org/Proceedings/05/Papers/0372.pdf); the next paper begins at 370. The same index contains the historical reproduction-rights notice referred to in manuscript lines 20-22. That verifies the provenance of the notice, not a present-day licensing determination.

The second source is the same authors' *Pushing the EL Envelope*, LTCS-Report 05-01, Dresden. The local PDF has 33 physical pages: a separate cover plus a body ending at printed p. 32. Thus the manuscript's description of a thirty-two-page report is consistent with its printed body, while physical PDF locators are one greater than printed report page numbers.

| Component | Conference locator | Report locator | Manuscript locator |
| --- | --- | --- | --- |
| Language, semantics, CBoxes | p. 365, Table 1 and Section 2 | printed pp. 2-4, Table 1 and Section 2 | lines 25-82, 577-590 |
| Normal form and reduction | p. 365, Lemma 1 | printed pp. 5-6, Definition 1, Lemma 2, Figure 1 | lines 84-138 |
| Completion state and eleven rules | p. 366, Table 2 | printed pp. 6-8, Section 3.2 and Table 2 | lines 171-281 |
| Polynomial termination | p. 366, Lemma 2 | printed p. 9, Lemma 5 | lines 283-293 |
| Historical decision condition | p. 366, Lemma 3 | printed p. 8, Lemma 4; pp. 9-14, Lemmas 6-7 | distinguished at lines 13-20; corrected condition and proof at lines 295-563 |
| Tractability conclusion | p. 367, Theorem 4 | printed p. 14, Theorem 8 | lines 565-593 |
| Concrete examples | p. 367, Proposition 5 and adjacent examples | printed pp. 15-20, Propositions 10-11 and adjacent examples | lines 595-608 |

## Independent findings

### C1-SF-01: Source syntax and hypotheses preserved — PASS

Manuscript lines 25-82 retain concept names, top, bottom, nominals, conjunction, existential role restriction, and concrete atoms with positive predicate arities. Features remain partial functions, the abstract domain remains nonempty, and the concrete carriers remain pairwise disjoint. The concrete-atom clause requires defined feature values in the predicate's own carrier. These match conference Table 1 and Section 2, and report Table 1 on printed p. 3.

The distinction between a GCI-only general TBox and a CBox admitting role inclusions is preserved. There is no added unique-name assumption, global feature-totality assumption, removal of nominals, or restriction to a nominal-free sublanguage. The polynomial constraint assumptions and convexity are explicit at lines 211-217. The finite-support convention is visible, rather than silently presenting the report's total assignment `NF -> Delta^D` from printed p. 9 as a partial-feature interpretation.

Closure condition: met for this snapshot. No correction requested. Reopen if the grammar, semantic feature clause, domain disjointness, or concrete-domain hypotheses change.

### C1-SF-02: All normalization and completion rules retained — PASS

All seven Figure 1 normalization transformations occur at lines 104-119. Their order, the fresh names, and the reason for using two phases occur at lines 101-126, matching report printed pp. 5-6. The arbitrary-query reduction and both directions of its preservation argument occur at lines 127-138.

Each Table 2 completion rule has a counterpart at lines 241-272. CR1-CR5, CR7, and CR9-CR11 retain their source premises and conclusions. CR6 retains both its shared-nominal test and its reachability premise. The source's reachability relation permits a sequence beginning either in the tested concept or in any occurring nominal; the manuscript keeps both alternatives at lines 190-194, and makes the zero-edge case explicit through `k >= 1`.

The update to `R(r3)` in CR11 is the correctly typed version of the sources' stale `Ri(r3)` notation. The manuscript expressly identifies that adjustment at lines 274-276. It is a typographical repair of the same role-composition update, not an additional completion rule. CR8 is retained with the disclosed support guard, addressed in C1-SF-04.

Closure condition: met. No missing rule or deleted reachability premise was found. Reopen if a rule or its applicability conditions change.

### C1-SF-03: Query marking is attributed and justified as a correction — PASS

The conference states simultaneous classification of the unmarked input on p. 366; the report states it on printed p. 6 and gives its decision condition in Lemma 4 on p. 8. Their original condition includes either a queried label containing the target or bottom, or a bottom-labelled nominal anywhere in the input.

The manuscript does not identify its marked criterion as that exact historical condition. Lines 13-20 announce the correction and identify the original simultaneous-classification claim. Lines 140-169 define the fresh nominal and prove the query equivalence, including the essential warning that marking need not be a model-conservative extension. Lines 295-310 retain the global nominal-inconsistency case, including disconnected nominals. Lines 570-575 explain that polynomially many marked runs recover classification and explicitly call the new argument the proof supplied here.

The seven-GCI example at lines 329-349 is also a relevant independent check of the difference. Without marking, the two sibling fillers share `{a}` but neither is reachable from the other or from an occurring nominal. The source CR6 therefore cannot force their label agreement merely from their common predecessor. Marking makes both successors reachable from the new nominal and supplies the missing premise. Semantically both successors must denote `a`, yielding the stated contradiction. The example is labelled a handbook construction.

Closure condition: met. The operative corrected procedure may remain under the governing contract. Source fidelity does not require reinstating the erroneous unmarked condition as the active decision procedure.

### C1-SF-04: Partial-feature correction is explicit and tracks the source defect — PASS

Both source Tables 2 state CR8 as a concrete implication test without requiring the conclusion's features to occur in the positive premises. The report defines a solution on all feature names on printed p. 9; its CR7-CR8 soundness discussion on p. 10 does not establish that arbitrary additional features are defined at the abstract element. This is a real distinction under the partial-function semantics of Table 1.

Manuscript lines 219-235 explain the difference and provide an abstract countermodel using the universal rational predicate and an undefined feature. Lines 259-262 add the exact support condition. Lines 381-391 verify definedness, implication, and cross-domain incompatibility separately. In completeness, lines 464-486 choose an avoiding assignment only for the supported missing atoms, and lines 524-531 treat unsupported atoms by undefinedness or by a value in a different carrier. The guard has not been falsely attributed as source wording.

Closure condition: met. The correction preserves partial features and the displayed concrete language. Reopen if the support guard or the treatment of unsupported atoms is removed or weakened.

### C1-SF-05: Source proof boundaries and affected components preserved — PASS

The conference expressly refers proofs and technical details to the report on p. 365. Its p. 367 countermodel discussion is a sketch and again directs the reader to the report. The manuscript accurately distinguishes these boundaries at lines 8-23 and supplies its own corrected argument.

The repaired proof accounts for the complete sequence needed from report Lemmas 6-7:

| Report proof component | Manuscript treatment |
| --- | --- |
| Lemma 6: initial invariants and every rule case, printed pp. 9-11 | lines 351-398 |
| Lemma 6: the success conditions imply subsumption, printed p. 11 | lines 400-406, using the marked query equivalence |
| Lemma 7: retained reachable set and nominal equivalence, printed pp. 11-12 | lines 408-440, with the marked nominal making every retained node nominal-reachable |
| Claim 1: label equality and transfer of outgoing role pairs, printed p. 12 | lines 425-462, including induction over the first insertion of a role pair and final saturation |
| Claim 2: concrete witnesses chosen by convexity, printed p. 12 | lines 464-486, with supported and unsupported atoms separated |
| Interpretation, well-definedness, and unused names, printed p. 13 | lines 488-509 |
| Claim 3: truth lemma for every basic description and bottom, printed p. 13 | lines 511-531 |
| All four GCI forms, both RI forms, and the queried counterexample, printed pp. 13-14 | lines 533-563 |

The report has additional wrong rule-number and variable references in these proofs: for example, Claim 1 on printed p. 12 refers to CR12/CR13, and the final composition case on p. 14 refers to CR10. The manuscript uses the actual CR10/CR11 roles and gives the required argument directly. It need not reproduce those erroneous references in the operative proof.

Closure condition: met for the components affected by C1. This verifies source representation and component retention; the separate specialist review remains responsible for its own mathematical verdict.

### C1-SF-06: Task scope and source-version distinctions remain visible — PASS

Lines 577-593 retain concept satisfiability, subsumption, ABox consistency, and instance checking, and expressly distinguish report Theorem 8's four-task list from conference Theorem 4's literal subsumption statement. The direct replacement of ABox assertions by nominal GCIs is supplied with its own semantic justification; it is a valid reconstructed route to the same task interface. It is not presented as a verbatim reproduction of the report's fresh-role `C_A` construction on printed p. 4.

Lines 595-608 correctly identify the rational and string predicate signatures and Proposition 5's relation to report Propositions 10-11. The corrected string superscript is disclosed. The rational `<=q` non-convexity example follows the conference version on p. 367. The report instead uses `<q` with a three-way partition on printed p. 19; the manuscript does not claim the two examples are identical. The transition at lines 610-615 correctly begins the conference Section 4 boundary to smaller EL with general TBoxes. The sentence continuing after line 615 and later presentations were not reviewed.

Closure condition: met within this correction scope. No task was lost as a consequence of the marking or partial-feature repair.

## Limits and obligations not closed here

The following are explicit limits, not additional C1 defects established by this review:

- The report's six mutual-reduction presentations on printed p. 4 are not all reproduced in manuscript lines 1-615. The manuscript gives sufficient direct reductions for the four-task polynomial conclusion; it does not reproduce the reverse reductions or the exact fresh-role wrapper. Whether each historical reduction has a separate full-presentation obligation requires the broader component inventory and destinations, which were not inspected.
- The report's four linear-small-model conclusions in Theorem 9, printed p. 14, are not stated in the inspected manuscript range. They are additional report content, outside the corrected completion theorem claimed here. This review does not admit their omission from the complete handbook or claim that C1 deleted them.
- The concrete-domain propositions are stated with source locators; their complete proofs and their cited external polynomial reasoning results are not reconstructed within lines 595-608. Their full-proof obligations are not closed by this source review.
- The complete report after printed p. 20, subsequent N-c-010 presentations, all original requirement mappings, and the edition-wide catalog were outside the assignment. No whole-source or whole-requirement completeness conclusion follows.
- No final PDF, manuscript build, rendered handbook page, rights clearance, or formal admission artifact was assessed.

If a later admission seeks a stronger verdict covering the entire 2005 report or every inherited N-c-010 source component, closure requires an explicit mapping and independent review of the above additional components. For the bounded C1 correction, the required source-fidelity conditions examined here pass.

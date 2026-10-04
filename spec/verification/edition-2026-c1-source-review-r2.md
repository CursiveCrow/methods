# C1 round 2 independent source-fidelity review

Date: 7 September 2026.

## Scoped verdict

**PASS** for source fidelity of the revised C1 normalization, its attribution, and its interfaces with the raw query, marked completion, and polynomial complexity conclusion. This verdict applies to `handbook/parts/p09/presentations/n-c-010.tex` at SHA256 `415a3769adaf9091582626a497eb82263e9ecdde037c4c447dd9c7ebd7369638`.

The new concrete-atom prepass is clearly identified as a handbook construction. It preserves the displayed source language and the original concrete atoms, while retaining all seven source normalization transformations and all eleven completion rules. Its proof and the later complexity paragraph distinguish linear written symbol size from polynomial time in a direct encoded input. No blocking source-fidelity defect was found in this recheck.

This is a bounded source review. It does not grant formal admission, establish publication quality, or settle the complete source-content obligations of N-c-010.

## Independence, scope, and actual reads

I performed this recheck directly as the delegated source reviewer. No subagents were used. I did not read other review outputs or author verdicts, and I did not use an author note as evidence for correctness. The first-round report was preserved and was not reopened for this recheck. The actual LaTeX, primary-source passages, and the governing contract supplied the evidence.

The exact runtime model identifier, version, reasoning configuration, and seed were not exposed; they are unavailable. This new review file is my only written output. I ran no manuscript build, render, static checker, or software test and changed no manuscript or source file.

The first recorded clock observation was 2026-09-07 14:24:44 UTC. A checkpoint reporting the verified snapshot, complete current manuscript reading, and rule retention was sent to the lead before 14:27:13 UTC. This recheck was completed within the 45-minute assignment limit.

| Artifact | SHA256 | Reading performed in this recheck |
| --- | --- | --- |
| `handbook/parts/p09/presentations/n-c-010.tex` | `415a3769adaf9091582626a497eb82263e9ecdde037c4c447dd9c7ebd7369638` | All lines 8-818. This includes requested changes at 8-354 and 781-818 and dependencies at 355-780. |
| `tmp/pdfs/p09-baader-brandt-lutz-2005/baader-brandt-lutz-2005.pdf` | `4c9caa8c224506123b7ee06cfcc8f5759d3537f4c241bb7e6bddcb89e0727a5a` | Conference printed pp. 365-367 through layout-extraction lines 54-280; existing physical page 2 image inspected. |
| `tmp/pdfs/p09-baader-brandt-lutz-2005/baader-brandt-lutz-ltcs-05-01.pdf` | `374d73eb848e556da759d89231385353996f44e6a6131f53d2794bb68d5aa3ba` | Complete printed pp. 3-14 through layout-extraction lines 133-681, including Figure 1, Table 2, and complete Lemmas 6-7; existing physical page 7 and 8 images inspected, corresponding to printed pp. 6-7. |
| `spec/EDITION-2026-CONTRACT.md` | `c9b101ad6bf6bfea5a3e1fbec25cdba81b47667146474861eb1aa00b5dfa1bf3` | Entire file, including the active-correction and attribution requirements at lines 53-69. |
| `handbook/bib/handbook.bib` | `8c4ae5fcd93092eb676ec04878a6ee09406e987464a5cebf2e9db9c139b7105f` | The two source entries at lines 5979-5987 and 5998-6006. |

The manuscript and both PDF hashes matched the assignment. The manuscript hash was checked again after reading. The source PDF and contract hashes are unchanged from the first pass; the bibliography's whole-file hash has changed, and the two relevant entries were therefore read at their current locations.

The conference layout text has SHA256 `8ef7d7100bc9b0bfeee675bceade1bbbaa9fa0c524dd4ff1434463326dc5e710`. The report layout text has SHA256 `5aa0fcf5767a94d8f7ef7930524d1e3a383ccefb0ef2a1a53f32a111d63c5654`. The report extraction has damaged glyphs. The actual Figure 1 and Table 2 page images resolve the source metavariables, fresh-name conditions, and printed rule formulas relevant to this change. Existing images were inspected; their rendering provenance was not independently recertified, and no new render was made.

## Findings and closure conditions

### C1-R2-SF-01: Exact vocabulary and size convention - PASS

Manuscript lines 88-94 now define the basic descriptions as exactly the smallest specified set and expressly exclude bottom, conjunctions, and existential restrictions. This matches conference Section 3 on p. 365 and report Definition 1 and its preceding paragraph on printed p. 5. Applying that same definition to each later CBox correctly places new names in the basic vocabulary without admitting arbitrary additional descriptions.

The report defines the size of a CBox as the number of symbols needed to write it, immediately before Lemma 2 on printed p. 5. Manuscript lines 96-110 make this convention explicit, distinguish it from axiom count and finite-set cardinality, and count each concrete feature argument. The stated absence of an arity bound preserves the source's positive-arity language rather than silently narrowing it.

The report's source language and the manuscript both retain partial features, nominals, a nonempty abstract domain, pairwise disjoint concrete carriers, GCIs, and role inclusions. The relevant current manuscript clauses are at lines 27-84. No lost source assumption or substituted semantics was found.

Closure condition: met. Reopen if the basic vocabulary, atom-length convention, or language hypotheses change.

### C1-R2-SF-02: Additional prepass accurately attributed and substantively justified - PASS

The report's Figure 1 on printed p. 6 contains NF1-NF7 and no concrete-atom abbreviation prepass. The manuscript accurately calls its prepass a handbook addition at line 128 and lists it as the third substantive correction in the opening account at lines 13-21. It does not attribute (N0) to the source figure.

The reason for the extra construction can be checked independently. In the source's written-symbol measure, an input `X_k <= A_1 and ... and A_k`, with `X_k = p_k(f_1,...,f_k)`, has length proportional to `k`. The atom is basic, so the original two-phase schedule can apply NF7 repeatedly with that atom as its left side. The fully written output then contains `k` copies of the `k`-argument atom and can have quadratic length. Counting only axiom count or treating the entire atom as one symbol would conceal this case.

The new construction handles that case without removing the atom. Lines 129-149 assign one fresh name per syntactically distinct atom, replace occurrences in the input, and retain both defining GCIs with the full original atom. The definitions are already legal normalized GCIs. Keeping them outside further normalization does not suppress a source rule applicable to them: both sides are basic, and neither axiom has conjunction or existential structure at its outer level.

The expansion at lines 151-167 sets each new concept name equal to the atom's actual extension, including undefined-feature cases. Structural induction preserves the original concept extensions, while the converse uses both defining inclusions. Thus the prepass preserves the original semantics rather than asserting feature existence or totality. Lines 169-181 count both full atom copies and explain how distinctness can be decided by finite comparison.

Closure condition: met for this source-fidelity review. The extra construction may be presented as the attributed correction; no source quotation or original rule needs to be altered to pretend it appeared in the report.

### C1-R2-SF-03: Source normalization rules and their proof boundary retained - PASS

All seven Figure 1 transformations appear at manuscript lines 197-212, with the same formulas. The fresh concept and role names, nonbasic hat condition, conjunction commutativity for NF2, and two-phase order are retained at lines 188-217. Figure 1 does not print an additional premise restricting the metavariable `B` to concept names; the manuscript makes its schema interpretation explicit and proves the amended schedule for that interpretation.

The newly supplied conservative-extension arguments at lines 219-237 and the detailed charging argument at lines 239-336 are handbook proof work. Their wording does not suggest that these detailed arguments are reproduced from the source. The report's Lemma 2 proof on printed p. 5 instead gives the schedule and asserts the linear bounds in a short verification; the paragraph below Figure 1 identifies the unrestricted NF7 copying risk.

The new application count explicitly belongs to the amended construction. Its measures count left-tree edges, remaining long-role-chain length, and right-side conjunction/existential occurrences. Its final size argument relies on the proved bounded written length of mutable left sides after concrete atoms have been replaced. No source rule or source constructor has been removed to obtain that bound.

Closure condition: met. This is source-fidelity approval of the retained rules and the attributed new proof, not a claim that the report printed the new counting formula or abbreviation schedule.

### C1-R2-SF-04: Raw-query reduction and earlier corrections remain compatible - PASS

The source's fresh-name query reduction is on conference p. 366 and report printed p. 6. Manuscript lines 338-354 preserve that reduction and explicitly apply the prepass to the whole expanded input, including atoms introduced by the query. The preservation argument therefore covers arbitrary raw concepts, rather than only CBoxes whose atoms were already normalized. The stated input-size expression counts the CBox and both query descriptions.

The subsequent fresh nominal remains a separately identified query reduction at lines 356-385. Its nonconservative behavior when the queried concept is necessarily empty is still stated. The marked decision condition at lines 511-526 still includes bottom at any occurring nominal, including a disconnected one.

All eleven completion rules remain at lines 457-488. The source's CR6 reachability premise and both starting alternatives remain at lines 406-410 and 470-472. CR8 still has the explicitly attributed feature-support guard at lines 435-451 and 475-478. The correctly typed CR11 update remains disclosed at lines 490-492. The prepass leaves both `A_X` and `X` in the vocabulary, so CR1 can transfer labels through the defining GCIs while CR7-CR9 continue to inspect the actual concrete atoms and feature arguments.

The current soundness and completeness dependencies were read through lines 567-779. They retain the rule cases, reachable nominal quotient, outgoing-role agreement, supported concrete witnesses, truth lemma, and all normalized-axiom cases corresponding to report Lemmas 6-7. Adding already-normal definitions is covered by these same GCI cases; it does not require a new semantic rule that is absent from the proof.

Closure condition: met. No false attribution, missing rule, or newly narrowed query domain was found at this interface.

### C1-R2-SF-05: Size, running time, and source theorem identities distinguished - PASS

Manuscript lines 326-336 expressly distinguish linear written symbol size and rewrite count from polynomial actual encoded time. The direct syntactic comparisons used by the prepass are not claimed to run in linear encoded time. The bound at lines 781-790 connects the raw encoded input, the expanded normalized output, the finite completion vocabularies, and the concrete constraints supplied to the polynomial tests.

This is the correct scope of the newly supplied complexity argument. Conference Lemma 1 and report Lemma 2 state a linear-time normalization result. The manuscript's amended proof establishes the stated linear symbol-size result and an effective polynomial-time construction; it does not establish the exact historical linear-time implementation claim. The text makes that difference explicit instead of attributing linear time to its pairwise-comparison prepass.

Lines 794-799 identify classification by polynomially many marked runs as the handbook procedure leading to the complexity conclusion corresponding to conference Theorem 4. Lines 801-817 retain the four standard tasks and distinguish report Theorem 8 from the conference theorem's literal subsumption statement. The source numbering remains accurate: conference normalization Lemma 1 corresponds to report Lemma 2; conference termination Lemma 2 to report Lemma 5; conference correctness Lemma 3 to report Lemma 4 and its Lemmas 6-7 proof split.

Closure condition: met for the amended polynomial subsumption result. A separate obligation to establish a linear-time normalizer must not be closed using this report's polynomial-time finding alone.

## Explicit limits and remaining source-body obligations

No inaccessible source-body gap blocked this bounded recheck: the relevant conference and report passages were available. This round did not reread conference pp. 364, 368-369 or the report outside printed pp. 3-14. Earlier reading is not counted as a new round 2 read. No current manuscript line after 818 was inspected.

The scope continues to leave the following broader obligations unresolved:

- The report's exact mutual-reduction presentations on printed p. 4, including the fresh-role `C_A` wrapper and reverse reductions, are not all reproduced in the inspected manuscript range. The current direct reductions establish the four-task interface but do not by themselves discharge a separate requirement to present every historical reduction.
- Report Theorem 9's four linear-small-model conclusions on printed p. 14 are additional source content absent from the inspected range. This recheck neither accepts their omission from the handbook nor establishes their treatment elsewhere.
- The complete concrete-domain proposition proofs and their external polynomial-reasoning dependencies are outside the changed scope. This review does not acquire or validate any missing underlying source body for those separate obligations.
- A precise linear-time normalization implementation, if separately owed, requires its own evidence. The reviewed added construction claims polynomial encoded time.
- Whole-presentation coverage, publication quality, rendered mathematical notation, licensing, formal admission, and final editorial acceptance remain outside this verdict.

These limits do not reveal a blocking source-fidelity defect in the normalization correction just reviewed. The scoped round 2 verdict is PASS at the stated manuscript hash.

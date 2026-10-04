# C1 independent publication text recheck, round 2

Date: 7 September 2026. First recorded review clock: 14:24:44 UTC.

**Scoped verdict: PASS.** Both findings from this reviewer's round 1 are resolved in the actual revised text. No new required correction was established in the assigned replacement passages or the necessary interfaces checked below. This verdict covers the stated recheck scope at the recorded manuscript hash. It does not establish full N-c-010 completion, formal admission, or publication approval.

## Independence, ownership, and exact scope

Reviewer identity: `/root/edition_c1_publication_review`, the independent adversarial publication text seat, rechecking its own prior findings. The actual model identifier, model version, reasoning effort, and sampling configuration were not exposed and remain unavailable. No other reviewer outputs or author verdicts were opened. No subagents were used.

The assigned replacement passages in `handbook/parts/p09/presentations/n-c-010.tex` were lines **8–354** and **781–818**. Every line of both ranges was read. **Unread assigned range: none.** The necessary manuscript interfaces additionally inspected in this round were lines 355–526, 669–778, the host definition at `handbook/parts/p09/logic-in-computer-science.tex:295–327`, and the host input at line 453. Lines 669–778 include the end of outgoing-role agreement, concrete witnesses, the interpretation, the truth lemma, and normalized-axiom verification needed to check the new abbreviation step against completion.

The review did not reopen the intervening unchanged examples and soundness proof as a complete new mathematical review, or the later EL failure boundaries, DL-Lite, or OWL treatments. The current file has 2,041 lines. Changes elsewhere to CSL and the unrelated CTIT bibliography entry are outside C1 and outside this verdict.

The reviewer created only this report, preserving round 1 and every manuscript/source file. No manuscript build, render, software test, or formal proof checker was run. Mathematical checks below are direct inspection and manual derivation from the displayed rules. A concrete checkpoint was sent to the integrator before fifteen minutes elapsed.

## Snapshot and dependency identities

Repository: `C:/Dev/the-methods-of-reason`. Branch observed: `phase4-codex`. HEAD observed: `35d537c692bb74b532dc4aa750da381a7fe4daf2`. File hashes identify the reviewed working-tree content; HEAD alone does not identify that content.

| File | SHA256 observed |
| --- | --- |
| `handbook/parts/p09/presentations/n-c-010.tex` | `415a3769adaf9091582626a497eb82263e9ecdde037c4c447dd9c7ebd7369638` |
| `tmp/pdfs/p09-baader-brandt-lutz-2005/baader-brandt-lutz-2005.pdf` | `4c9caa8c224506123b7ee06cfcc8f5759d3537f4c241bb7e6bddcb89e0727a5a` |
| `tmp/pdfs/p09-baader-brandt-lutz-2005/baader-brandt-lutz-ltcs-05-01.pdf` | `374d73eb848e556da759d89231385353996f44e6a6131f53d2794bb68d5aa3ba` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `61e3125b950ae194412c81bc6c5eeb3dfceac533541b26007f6db7744e3ddc45` |
| `handbook/bib/handbook.bib` | `8c4ae5fcd93092eb676ec04878a6ee09406e987464a5cebf2e9db9c139b7105f` |
| `handbook/CONVENTIONS.md` | `4293f514072179a5ac95e64fa8d8f37e23ffe2693814a1980e5801baba5b7242` |
| `spec/EDITION-2026-CONTRACT.md` | `c9b101ad6bf6bfea5a3e1fbec25cdba81b47667146474861eb1aa00b5dfa1bf3` |
| Preserved `spec/verification/edition-2026-c1-publication-text-review.md` | `a0a31ef5d319ddb9f45dcdcbe282802a0459f883d2cd02337e8b11580604d419` |

The manuscript hash matches the round-2 assignment. Both primary PDFs retain their round-1 identities. The complete host and bibliography hashes have changed; the particular C1 route, prerequisite definition, and Baader source records were therefore inspected directly rather than presumed unchanged from those full-file hashes.

## Resolution of prior findings

| Prior finding | Evidence in the revised manuscript | Disposition |
| --- | --- | --- |
| C1-PUB-01: undeclared size measure in the normalization application bound | Lines 96–110 explicitly define the local source notation as fully written symbol length, count feature arguments, separate later cardinality notation, and point forward to encoded complexity. Lines 239–307 derive a new application bound and written-size bound for the amended construction. Lines 326–336 then address actual identifiers and predicate parameters. | **PASS / resolved.** The former single-axiom counterexample does not contradict the revised measure or the revised count. |
| C1-PUB-02: inexact basic vocabulary and undeclared NF metavariables | Lines 88–94 define exactly the smallest required finite basic set, expressly exclude bottom and compound descriptions, and reuse the definition for later CBoxes. Lines 188–195 type the arbitrary concept metavariables, nonbasic hats, role symbols, and fresh names. | **PASS / resolved.** Compound fillers cannot now be silently admitted as extra basic descriptions. NF6 and NF7 apply to their expressly declared arbitrary concept-description left sides. |

The notation repair agrees with the live `handbook/CONVENTIONS.md:218–225`: a source's local notation may retain its published standing when the role is declared before use. The report source itself defines its size measure immediately before Lemma 2 on printed page 5.

## New interfaces independently checked

### Exact prepass and conservativity: PASS

At lines 127–149, each syntactically distinct occurring atom receives a distinct fresh concept name. The manuscript distinguishes the explanatory subscript from the actual output identifier, replaces occurrences in the input GCIs, retains both full defining GCIs, and protects those definitions from another abbreviation pass. The exact basic-set definition includes both the abbreviation name and the concrete atom. This is executable input syntax rather than a requirement to infer a shared-expression output format.

At lines 151–167, assigning the new name the original atom's extension proves the expansion direction under the stated partial-feature semantics. Both defining inclusions force equality in the reverse direction. Structural induction through conjunction and existential restriction then preserves every replaced original description; roles and RIs are unchanged. The argument therefore supplies the required conservative relationship without making features total.

The protected definitions also fit the later completion interface. They are instances of the first normalized GCI form, and CR1 at lines 457–458 propagates between an abbreviation label and its actual concrete atom. CR7–CR9 at lines 473–483 continue to inspect actual atoms and feature supports. The interpretation and truth lemma at lines 704–747 retain separate, exhaustive cases for concept names and concrete atoms, and normalized-axiom verification at lines 749–773 covers both defining inclusions. The abbreviation step therefore does not hide a concrete constraint from the semantics or the completion rules.

### Prepass written size, including unbounded arity: PASS

Lines 169–181 justify the size bound using disjoint atom occurrences in the written input. Since concrete atoms contain feature arguments rather than nested concept descriptions, the total written length of the distinct atoms cannot exceed the sum over their occurrences. Two full definitions per distinct atom and one name per replaced occurrence therefore have total length `O(N)`.

The example at lines 317–324 correctly exhibits the point of this step: for `X_k ⊑ A_1 ⊓ ... ⊓ A_k`, the long atom occurs only in its two protected definitions after normalization. The `k` output inclusions use the short abbreviation name. No fixed bound on `k`, unit-cost treatment of an entire atom, or shared-expression final artifact is needed for this symbol-length claim.

### NF semantics, schedule, and termination count: PASS

Lines 197–217 preserve the seven source transformations and the two-phase schedule while specifying the protected part of the CBox. The individual expansion and reduct arguments at lines 219–237 justify the fresh-role prefix, the one-sided concept introductions, deletion of a bottom antecedent, and splitting of a conjunction consequent. Freshness prevents changes to the protected definitions.

The count at lines 242–297 accounts for every NF rule:

| Rule group | Bound and independently checked reason |
| --- | --- |
| NF2 and NF3 | At most `e`: each application removes an original left-tree edge with a nonbasic child; the new edge has a basic fresh-name child. No original subtree is copied in this phase. |
| NF4 | At most `g + e`: these are the maximum number of GCI roots created from the original roots and the extracted subtrees. |
| NF1 | Exactly `h`: a long role chain loses one excess link per step and produces a terminal chain of length two. |
| NF6 | At most `v`: each original right-side existential occurrence can have its nonbasic filler extracted once. |
| NF7 | At most `a`: each original right-side conjunction root is removed once, without copying its children. |
| NF5 | At most `g + e + a`: the count of GCIs with two nonbasic sides starts at most at `g + e`; NF5 decreases it, NF6 does not increase it, and each NF7 increases it by at most one. |

Adding these bounds yields exactly the displayed `2g + 3e + h + v + 2a`. All five input counts are linear in the declared symbol measure. The order explanation at lines 270–276 and 299–315 also supplies the size and normal-form conclusions: mutable left sides are shallow and of bounded symbolic length after phase one, because large concrete atoms were removed from that part; later copying under NF7 therefore has bounded cost. The surviving rules cannot leave an unhandled compound GCI when saturation of the NF schedule ends.

### Encoded cost and raw-query order: PASS

Lines 326–336 separately define encoded input length, include identifiers and predicate parameters, allow polynomial-length fresh identifiers, and claim polynomial encoded output and construction time. They do not promote the symbolic linear bound to a bit-linear running-time assertion.

Lines 338–354 adjoin both fresh query-name axioms before collecting atoms. Thus an atom that occurs only in the query still receives its definition pair. The query-preservation argument gives both directions before composing with the conservative prepass and NF reductions. Marking then occurs on the normalized result at lines 356–385, with the marker's freshness and the nonconservative nature of query marking expressly stated.

A direct interface check with an empty original CBox and the query `X ⊑ X` confirms the stated order: the expanded input contains `A_0 ⊑ X` and `X ⊑ B_0`; abbreviation introduces its definition pair for `X`, and CR1 can propagate from the marked `A_0` through the abbreviation to `B_0`. The query-only atom is not omitted. An undefined feature still makes `X` false under its original semantics; the new defining name does not force `X` at an unrelated label.

Lines 781–817 carry the encoded normalization bound into the finite completion and task reductions. Each constraint uses a finite subset of the actual atoms retained in the output, so its encoding length is polynomially bounded by the raw encoded input. The p-admissibility condition supplies the concrete tests for the chosen domains, consistently with the source's theorem for `D_1, ..., D_n`. Classification concerns pairs of original occurring concept names and hence uses polynomially many marked runs. ABox consistency, instance checking, and concept satisfiability retain their explicit reductions and nonempty-domain semantics.

### Source attribution and reader route: PASS

Lines 8–25 expressly identify three handbook corrections. Lines 127–128 identify the prepass as an addition to the report's NF schedule. Lines 183–187 attribute NF1–NF7 to the report and the normalization claim to the conference paper; lines 214–217 describe exactly how the source schedule is reused. Lines 240–241 independently ground the amended count. Lines 794–799 identify the supplied proof as establishing the corresponding conference complexity conclusion rather than adopting the source's unmodified simultaneous-classification claim.

The conference and report bibliography keys remain distinct at `handbook/bib/handbook.bib:5979–5987` and `5998–6006`. Their titles, authors, source types, report identifier, and locators were checked in the live file. The host still includes C1 at `handbook/parts/p09/logic-in-computer-science.tex:453`, after the actual interpretation, Boolean-constructor, TBox, and ABox prerequisites at lines 295–327. The new notation and prepass definitions appear before their uses, including the later references to the normalization proof and the raw-query interface.

## Primary passages and policy consulted

This round reread the following passages from the unchanged actual PDFs by direct text extraction:

- Conference printed pages 365–367, physical pages 2–4: Table 1, the basic-description normal form, Lemma 1, Table 2, p-admissibility, the original classification claim, and Theorem 4.
- LTCS-05-01 printed pages 5–6, physical pages 6–7: Section 3.1, the explicit source size convention, Lemma 2, Figure 1, the two-phase explanation, and the original query reduction.
- LTCS-05-01 printed page 14, physical page 15: the conclusion of normalized-axiom verification and Theorem 8's four-task statement.

The PDF skill was used for read-only source inspection. Its visual-output workflow was not used to infer any manuscript production result. The governing edition contract and notation-convention identities were revalidated; the correction, attribution, and independent-admission requirements applied are unchanged from round 1.

## Remaining gates

There are no outstanding required corrections from this reviewer's assigned round-2 text scope. This scoped PASS resolves C1-PUB-01 and C1-PUB-02 for the recorded revised hash and records the new prepass, normalization, and complexity interfaces as passing this publication text recheck.

Manuscript static/build checks, rendered mathematics and links, pagination, page-by-page visual inspection, rights evidence, the other independent review seats, the separate admission record, full N-c-010 coverage, and editorial acceptance remain **UNRESOLVED / pending separate evidence** in this report. The report makes no claim that those gates have passed.

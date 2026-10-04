# Next formal authoring units

Checkpoint: 2 October 2026, 10:08 UTC. This is a bounded authoring handoff, not a manuscript review, queue rebaseline, source-admission decision, or completion claim. The actual full `spec/coverage/edition-2026/completion-work-queue.jsonl` was parsed; relevant current LaTeX and source/version records were inspected. No manuscript, queue, canonical record, build, render, or test was changed. Only this note is owned by the investigator.

Project authority: `handbook/CONVENTIONS.md`, `spec/EDITION-2026-CONTRACT.md`, `spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md`, and `spec/research/edition-2026-authoring-resumption-2026-09-09.md`. Source-specific treatment is not discharged by an existing capsule, a different source version, a host proof with different hypotheses, or a catalog status string. Preserve other writers' work. All shared hosts, part/annex drivers, style, canonical bibliography and symbol registry remain lead-owned. The writer of each unit should use disjoint new body/annex, source-note and intake files; integration is the lead's action.

## Dispatch state and recommendation

Six candidates are identified below. The lead has already dispatched Gelfond–Lifschitz to `/root/gelfond_1988_author` and Mac Lane–Moerdijk to `/root/presheaf_semantics_author`. They are retained here as grounded factual records, not unassigned seats. Four available-body next seats remain: Baader–Snyder equational unification, Barendregt–Geuvers proof/type systems, Klop's distinct 1987 tutorial, and Lawvere's original six-page article. Prefer Baader–Snyder first for a sharply separable mathematical gap. The larger chapter/report allocations require successive bounded blocks; completing the first block does not close the whole source unit.

## 1. Gelfond–Lifschitz 1988: stable expansions behind the reduct

**Assigned.** Unit `ED26-REQ-N-c-023-01`; parent component `N-c-023-C01`; allocated components `N-c-023-MAP-01` and `N-c-023-MAP-04`. Exact queue source locator: `spec/research/p09-source-presentations-lot4.md:1039`; pertinent retained evidence also appears at line 2407. Do not revive the historical missing-1988-body diagnosis.

**Ownership.** New `handbook/parts/p09/presentations/n-c-023-01.tex`, matching `handbook/annex/p09/n-c-023-01.tex`, treatment-specific intakes and source note. Do not edit the common `n-c-023.tex`.

**Held body/version.** `tmp/pdfs/p09-gelfond-lifschitz/gelfond-lifschitz-1988-stable-model.pdf` and its `.txt`; also `citations/Gelfond and Lifschitz - The Stable Model Semantics for Logic Programming (1988, author copy).pdf`. The complete eleven-page archived author copy corresponds to published pp.1070–1080. The earlier record describes inspection of sections 2–4, Theorems 1–3, Corollaries 1–2 and the stable-expansion lemma. It is not independently compared publisher proceedings typography.

**Actual deficit.** The active common presentation already supplies finite ground reducts, zero/multiple stable-model examples, positive-program collapse, minimality, and original terminology. Its autoepistemic paragraph only summarizes the stable-expansion/reduct lemma and Theorem 3 proof; the queue retains that unsupplied proof. The general uniform NP compilation and disjunctive hardness belong to other source facets, not to a fabricated 1988 result.

**Prerequisite interface.** Existing `def:p09-definite-program`/least positive model and `def:p08-autoepistemic-expansion`; explicitly fix the original ground/objective theory, propositional consequence and belief operator. Keep the 1988 unique-model/canonical-semantics wording distinct from the modern relation allowing zero or several stable models.

**Concrete success/failure.** Supply the exact source-specific stable-expansion lemma, both needed directions, Theorem 3 dependency, and the source's comparison scope with explicit grounded examples. Failure: merely repeat the reduct, assume the stable-expansion equivalence, identify partial well-founded interpretations with two-valued stable models, or import later complexity claims as 1988 theorems. A first proof block may be returned partial with the remaining source components explicit.

## 2. Mac Lane–Moerdijk 1992: internal logic and three forcing regimes

**Assigned.** Unit `ED26-REQ-N-d-023-03`; `N-d-023-C01`; `N-d-023-S03-PRESENTATION`, `-PROOF`, `-BRIDGE`, `-TASK01`, `-TASK02`, `-TASK03`. Existing presheaf foundations are reusable interfaces, not automatic source-specific credit.

**Ownership.** New `handbook/parts/p10/presentations/n-d-023-source-03.tex`, matching `handbook/annex/p10/n-d-023-source-03.tex`, disjoint intakes and source note. The lead owns the existing presheaf files and host.

**Held body/version.** `tmp/pdfs/p10-topos/mac-lane-moerdijk-sheaves-in-geometry-and-logic-institutional.pdf`, *Sheaves in Geometry and Logic*, Springer-Verlag 1992; current SHA-256 `A30AE90087DF702F6E48A705FF313CEB7821FAE55AB3CF43E255D4DCD7B95825`. The inspected page mapping is physical page = printed page +11. Source packet: `spec/research/p10-presheaf-logic-source-verification-2026-09-06.md:7`. Recorded actual readings: I§8–9 pp.50–61; III§8 pp.147–149; IV§8–9 pp.198–209; VI§5–6 pp.296–312 and VI§7 pp.315–318. The earlier read did not include VI§6 pp.313–314. The separate 2007 Moerdijk–van Oosten notes are comparison material, not a substituted 1992 version.

**Actual deficit.** `handbook/parts/p10/algebraic-and-categorical-logic.tex:271` remains a short internal-logic/forcing paragraph. The routed presheaf files supply limits/colimits, exponentials, classifier and power objects, but not the complete internal Heyting, all-arrow quantifier, comprehension and forcing development. The September writing record expressly lists this next work.

**Prerequisite interface.** `def:p10-presheaf-category`, `def:p10-subpresheaf`, `thm:p10-presheaf-exponentials`, `thm:p10-presheaf-topos`, `thm:p10-presheaf-power-objects`; small-base/universe arrangement; the previously written indexed-predicate/quantifier framework. Define site and covering sieve before sheaf semantics. Source VI§5 p.302 refers the formal calculus elsewhere, so semantics passages alone cannot be credited as a full registered-calculus soundness proof.

**Concrete success/failure.** Prove componentwise Heyting residuation, correctly typed image/right-adjoint formulas, adjunctions and pullback Beck–Chevalley/Frobenius at their exact standing; interpret typed terms, equality/membership/lambda/comprehension; state and justify the distinct base-stage, generalized-element and site/sheaf clauses. A current-stage witness is not epimorphic locality, and a covering sieve is not arbitrary component membership. Failure: universal-image formulas comparing elements of different stages, material stagewise implication, using a merely commuting square as a pullback, or relabeling set-theoretic forcing as these categorical semantics. Source exercises and source omissions stay attributed; independently supplied proofs remain editorial.

## 3. Baader–Snyder 2001: equational/AC solution sets and constructions

**Unassigned; recommended next.** Unit `ED26-REQ-N-c-035-05`; `N-c-035-C01`, allocated `N-c-035-MAP-05`. Related full-chapter facet `ED26-SRC-037-0008-C002`–`C005` is not a second completed work; bind overlaps rather than double-count them.

**Ownership.** New `handbook/parts/p12/presentations/n-c-035-05.tex`, matching `handbook/annex/p12/n-c-035-05.tex`, unique intakes and source note. The queue also proposes `har2001-c08.tex` for the whole chapter: do not independently populate both as competing duplicate treatments; lead resolves that crosswalk.

**Held body/version.** `citations/Baader and Snyder - Unification Theory (2001, Handbook of Automated Reasoning chapter, PS-derived PDF).pdf`; 89 pages, chapter pp.445–533, current citation-copy SHA-256 `4197E9729D3DAFC0E889F64BB46940D71254F90EBDCF948138626F9D2865934B`. Original retained derived-PDF hash is `84ebf4ddd5a041e09d3f757aea7e638b85f939d629b7d5fd7729ab3af3b99fc1`. Readable extraction: `tmp/acquisition/src037/iccl-unification-ps-gz-retry-02.body.derived-decompressed.ps.derived-render.pdf.derived-layout.txt`. Relevant actual source headings: §3 pp.469–487; §4 pp.488–502; §5 pp.503–512; §6 pp.513–518. Keep the alternate 88-page pp.439–526 manifestation and publisher-layout comparison separate. `citations/manifest.json:518` preserves the identity/version evidence.

**Actual deficit.** `handbook/parts/p12/first-order-automation.tex:223` gives only brief congruence/AC/higher-order boundary sentences. The new `unification-extraction-adequacy.tex` proves the literal finite syntactic algorithms, extraction and renaming; it does not supply E-congruence, complete/minimal sets, unification types, narrowing, ACU/ACUI/AG or combination correctness. Do not repeat its already supplied termination/MGU block from a stale queue remark.

**Prerequisite interface.** Free-term substitution/composition and instance preorder from current P2; today's literal syntactic-unification results for comparison only. For E-unification, declare equality modulo E, comparison relative to the problem's variable set, fresh variables, complete/minimal solution sets and the precise theory signature. The full chapter's combination assumptions and ordering/partition restrictions must be stated before use.

**Concrete success/failure.** First block: reconstruct §3's E-unification objects, generality relations/types and actual examples, then §5's ACU/ACUI/AG example with the source's completeness argument; retain all further allocated method dependencies for continuation. Full allocated success requires the source's required theory-specific methods, proof hypotheses and examples. Failure: call every E-theory unitary, treat multiple incomparable solutions as one syntactic MGU, omit constants/fresh-variable restrictions, confuse AC with ACU, or silently change finite trees to rational trees. Narrowing/combination completeness cannot be established by naming the mechanism.

## 4. Barendregt–Geuvers 2001: formal proof/type systems and development

**Unassigned.** Unit `ED26-SRC-037-0018`, exact components `ED26-SRC-037-0018-C001`–`C004`: proof checking/type correspondence and conversion; higher-order calculi/PTS; products/sums/dependent sums/inductives; proof development/tactics/autarkic computation/source assistant comparisons.

**Ownership.** Queue-proposed new `handbook/parts/p12/presentations/har2001-c18.tex`, matching `handbook/annex/p12/presentations/har2001-c18.tex`, disjoint intakes and `spec/research/har2001-c18-source-note.md`. No shared modern assistant table edits.

**Held body/version.** `citations/Barendregt and Geuvers - Proof-Assistants Using Dependent Type Systems (2001, Handbook of Automated Reasoning, author-hosted chapter).pdf`; 90-page author-hosted chapter pp.1149–1238, printed 2001 copyright. Current SHA-256 `48268D36690E8006AA0F6E78B67F553C7A2A17F44B4F394A442241BE002B4B2E`; original retained body hash `ce13485bfec08df559c838db13e53dcc9e75050daa7e67fe806bb04c25f4adcf`. Readable extraction: `tmp/acquisition/src037/geuvers-proof-assistants-retry-01.body.derived-layout.txt`; its first pages supply the actual contents: §2 pp.1153–1179, §3 pp.1180–1210, §4 pp.1211–1222, §5 pp.1223–1229. No publisher-file byte identity is inferred. Citation manifest evidence starts at line 1052.

**Actual deficit.** Current `handbook/parts/p12/interactive-proof.tex:128` provides a family-level PTS/cube definition/table and subsequent universe/inductive/CIC/reflection boundaries, not this chapter's full rule surfaces, subject-reduction/conversion reasoning, proof terms and source proof developments. The proposed `har2001-c18.tex` did not exist when inspected.

**Prerequisite interface.** Typed lambda syntax/substitution and current source-specific P7 metatheory; generic PTS specification; actual judgement forms and conversion/equality distinctions. Do not treat the 1991 Barendregt draft as the final 1992 chapter. The 2001 source's historical assistants are not pinned 2026 Rocq/Lean kernels; modern bindings remain a distinct source/version task.

**Concrete success/failure.** Start with C001: complete source proof-as-term examples, logical-framework distinction, subject-reduction/conversion/equality hypotheses and actual derivations. Then C002/C003: formal source type/product/elimination/computation rules and complete promised arguments before C004's source worked development/autarkic proof examples. Failure: only reproduce cube/table labels, assert normalization for arbitrary PTS specifications, equate definitional and propositional equality, replace the source's calculus by current Lean/CIC, or count a tactic script as a proof without its typed term/checking bridge. A partial first block must not close the 90-page unit.

## 5. Klop 1987: the distinct CWI reduction-system tutorial

**Unassigned.** Unit `ED26-SRC-027-501`; exact components `ED26-SRC-027-501-DOMAIN`, `-CHAIN`, `-CASES`, `-ATTRIBUTION`, `-RELATION`. This is not `ED26-SRC-027-001`, the final 1992 chapter.

**Ownership.** New `handbook/parts/p12/sources/src-027-501.tex`, matching `handbook/annex/p12/sources/src-027-501.tex`, unique intakes and `spec/research/src-027-501-source-note.md`.

**Held body/version.** `citations/Klop - Term Rewriting Systems - A Tutorial (1987, CWI Note CS-N8701).pdf`, complete 42-physical-page report, original retained `tmp/acquisition/src027/cwi-klop.pdf`; readable extraction `tmp/acquisition/src027/cwi-klop.txt`. Current citation-copy SHA-256 `39EBB6329C46B0A9B4E545467E9B7464BD7B602ABC7F26F27FEA6324FF9DDB5F`; original PDF hash `f0103746292b130e47c2d02fe1192abed2e33967ae0f952b87ed369c7e341543`. Title/abstract/contents inspected. Actual six sections: abstract reduction systems; basic TRSs; recursive path-order termination; Knuth–Bendix; regular systems; reduction strategies for regular systems. The report explicitly excludes conditional and equational TRSs. Manifest evidence starts at line 5713. Do not upgrade an apparent printed historical open question to a current open status without a separate dated source.

**Actual deficit.** `handbook/parts/p12/rewriting.tex` and the new reduction-ordering/fair-completion supplements give current ordinary host proofs, but no separate Klop source route or its complete regular-system/reduction-strategy development. Searches of those current files found strategy restrictions as boundaries, not a regular-TRS strategy treatment. The queue-proposed source file did not exist.

**Prerequisite interface.** Source ARS relations and property names; terms, contexts, positions/substitution and reduction; left-linearity, overlap/nonambiguity, disjoint redex/parallel reduction. Declare the report's exact regular-system regime before transporting ordinary host critical-pair facts. Existing LPO/KBO and fair-completion proofs are comparison/prerequisite results, not the original report's exact route.

**Concrete success/failure.** Reconstruct source §5–6's regular-system and parallel/outermost strategy arguments with their actual examples and proof/citation standing, while a dependency crosswalk retains the source's §1–4 obligations. Full unit success covers all six sections and their examples/qualifications, without duplicating source credit. Failure: substitute final1992 conditional/equational material, identify regularity with any confluent TRS, assume an evaluation strategy normalizes every term, or treat a host theorem as a source-native argument merely because names match.

## 6. Lawvere's Nice 1970 article, published 1971

**Unassigned.** Unit `ED26-REQ-N-d-023-01`; `N-d-023-C01`; exact `N-d-023-S01-PRESENTATION`, `-PROOF`, `-BRIDGE`, `-TASK01`. The queue allocates the complete original short account, not just its first paragraph.

**Ownership.** New `handbook/parts/p10/presentations/n-d-023-source-01.tex`, matching `handbook/annex/p10/n-d-023-source-01.tex`, unique intakes and source note. Root preserves common hosts and coordinates bridges with the Mac Lane–Moerdijk writer.

**Held body/version.** `tmp/pdfs/p10-topos/lawvere-quantifiers-and-sheaves-icm1970.pdf`, original-layout six-page article pp.329–334; SHA-256 `25BD24945DBD216B384AB4B094FF1BB4315682D0D90817C0CAD77CB15DA74DE4`. Original article is available from the [Lawvere Archives](https://lawverearchives.com/wp-content/uploads/2024/12/1970-quantifiers-and-sheaves.pdf). The full article was read through the primary PDF renderer for this handoff; prior local reading/version evidence is `spec/research/p10-presheaf-topos-source-note-2026-09-06.md:25`. Stable key `Lawvere1970` now correctly retains publication1971 and event1970.

**Actual deficit and scope.** The current P10 host cites p.329 for the finite-colimit definition comparison, but lacks a separately attributed full article route. Remaining source mechanisms include quantifier/slice adjoints and internal presheaves; the choice/Skolem distinction; geometric versus logical morphisms and topology/associated sheaves; generalized ultraproducts; Boolean-valued models and the CH argument; and the global-spectrum/local-ring construction. Some are announced or sketched in the original, not fully proved there. The modern presheaf toolkit cannot silently replace those source assertions.

**Prerequisite interface.** The article's finite-limit/finite-colimit topos package, truth-value object, adjoint functors and slice categories; internal-category objects; source-defined topology, logical/geometric morphisms and natural-number assumption. Keep generalized ultraproducts distinct from ordinary P3 ultraproducts and keep categorical Boolean-valued constructions distinct from unqualified set-theoretic CH independence.

**Concrete success/failure.** Present the complete source account with its declarations, hypotheses, actual construction/sketch dependencies and source-specific examples; give the explicit bridge to existing presheaf results without claiming that source announcements contain omitted proofs. Where a separate full-proof obligation remains, keep it open rather than reduce the allocation to definitions. Failure: narrow silently to the first two pages, erase finite colimits from its primitive package, use a current textbook definition as an exact source quotation, make a sketch into a proved theorem, or date publication1970 solely from the conference heading. A first authoring block can cover the first source section and preserve the rest explicitly for continuation.

## Exclusions and verification limits

Do not redispatch today's Fagin1974, Fagin1976, Immerman1986, literal syntactic-unification extraction or fair-completion developments from stale queue capsules: their actual new source notes/LaTeX already supply substantive authoring. No fresh acceptance is asserted. Baldwin–Lachlan1971, Ryll-Nardzewski1959 and Haken1985 remain exact-version acquisition dependencies and were not re-searched here.

No child agents or reviewers were launched. No manuscript build/render, tests or source acquisitions were performed. Source title/contents, held-file identity/hashes and relevant existing mathematical/source records were inspected, not every page of the large chapter bodies. A MiKTeX `pdftotext` read attempt failed on its log-directory permission; existing readable extractions were reused. `pypdf` confirms page extents but gives custom-glyph noise for the two HAR chapters, so that output is not treated as mathematical text. Actual writers must read their full allocated source extent and inspect ambiguous formulas before reconstructing them.

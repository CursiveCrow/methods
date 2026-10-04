# C1 independent adversarial publication text review

Date: 7 September 2026.

**Scoped verdict: FAIL.** Two normalization-interface corrections are required before this frozen text can pass the assigned publication text review. The review found no further defect in the marked-query decision criterion, guarded concrete propagation, or their displayed soundness and countermodel arguments. This is a verdict on the assigned text, not full N-c-010 completion, formal admission, or publication approval.

## Reviewer and scope

Independent reviewer identity: `/root/edition_c1_publication_review`, assigned the adversarial publication text seat. Actual model identifier, model version, reasoning effort, and sampling configuration were not exposed to this reviewer and are recorded as unavailable. No other review outputs or author conclusions were opened. No subagents were used. The reviewer owns only this report and did not modify manuscript, source, policy, bibliography, or other review files.

The assigned manuscript extent was `handbook/parts/p09/presentations/n-c-010.tex`, lines 1–615, at the SHA256 below. Every assigned line was read. **Unread assigned range: none.** Lines 616–1817 are outside this review. The boundary at line 615 falls inside the sentence introducing the later failure-boundary languages; the complete claims and arguments that continue after that boundary have not passed this review.

The review checked the reader's route into C1, prerequisites needed by C1, definition-before-use, source and correction attribution, the stated normalization and complexity interface, the completion procedure and examples, and consistency of its internal forward and backward references. Source passages were read from the actual local PDFs using text extraction; an existing rendering of LTCS physical page 7 was also inspected to resolve the normalization-rule notation. No manuscript build, manuscript rendering, software tests, or formal proof checker was run. A concrete progress checkpoint was sent to the integrator during the review.

## Frozen identities and dependencies

Repository: `C:/Dev/the-methods-of-reason`. Branch observed: `phase4-codex`. HEAD observed: `35d537c692bb74b532dc4aa750da381a7fe4daf2`. The checkout contains substantial existing changes; the manuscript identity is the live file hash rather than a claim that HEAD contains the reviewed text.

| File | SHA256 observed |
| --- | --- |
| `handbook/parts/p09/presentations/n-c-010.tex` | `645f9a718b66d740948436ca5309ad25b59d39ce63acc6c41a108549cbb8ffa1` |
| `tmp/pdfs/p09-baader-brandt-lutz-2005/baader-brandt-lutz-2005.pdf` | `4c9caa8c224506123b7ee06cfcc8f5759d3537f4c241bb7e6bddcb89e0727a5a` |
| `tmp/pdfs/p09-baader-brandt-lutz-2005/baader-brandt-lutz-ltcs-05-01.pdf` | `374d73eb848e556da759d89231385353996f44e6a6131f53d2794bb68d5aa3ba` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `96730f47c816df9800191700a280ebb6db0041f5415fe05c569225a62b9ad822` |
| `handbook/CONVENTIONS.md` | `4293f514072179a5ac95e64fa8d8f37e23ffe2693814a1980e5801baba5b7242` |
| `handbook/bib/handbook.bib` | `d5bab1c74ab2b378eaacafe2ce1b313209e71e46a28dd2748ef7c539c5cb7094` |
| `spec/EDITION-2026-CONTRACT.md` | `c9b101ad6bf6bfea5a3e1fbec25cdba81b47667146474861eb1aa00b5dfa1bf3` |

The manuscript and both supplied primary-source hashes matched the assignment. The conference PDF has six physical pages. The report has 33 physical pages including its cover, with the body beginning its printed pagination after the cover; the manuscript's description of the 32-page report body was not treated as a version mismatch.

## Required findings

### C1-PUB-01: The normalization application bound uses an undeclared size measure

Severity: P2. Status: FAIL; required correction.

Evidence: `handbook/parts/p09/presentations/n-c-010.tex:67` defines a CBox as a finite set. Lines 121–124 then say that normalization needs at most `|\mathcal C|` applications, without assigning that notation a symbol-length meaning. Lines 285–288 subsequently use the same bars with their ordinary cardinality meaning for the finite basic vocabulary and role vocabulary. `handbook/CONVENTIONS.md:218–225` requires local typed roles to be declared before use and records cardinality as the standing meaning of bars.

The defect has a concrete consequence. Let the CBox contain the single axiom `A ⊑ B ⊓ (C ⊓ D)`, with four distinct concept names. Its set cardinality is one. Phase one makes no change. NF7 must first split off `A ⊑ B`, and a second NF7 application must split `A ⊑ C ⊓ D`. Thus this input requires two applications although the stated, currently typed bound is one.

The source supplies the missing qualification: LTCS-05-01, printed page 5, immediately before Lemma 2, defines the CBox size as the number of symbols needed to write it. Its subsequent application bound uses that definition. The source's bound has therefore lost an essential local definition in the handbook interface.

Required correction: introduce the input-length measure before the bound, state whether the source's `|\mathcal C|` notation is being locally adopted or use a separately defined length notation, and express the normalization application and size bounds with that measure. Preserve cardinality for `b` and `m_R`. The eventual polynomial-cost statement must refer to encoded input length under the chosen concrete-domain representation, not the number of CBox axioms alone. This repair concerns the statement's typing; it does not require changing the corrected saturation rules.

### C1-PUB-02: The basic vocabulary and normalization metavariables are not defined exactly enough to determine the procedure

Severity: P2. Status: FAIL; required correction.

Evidence: `handbook/parts/p09/presentations/n-c-010.tex:85–87` says only that `\mathsf{BC}_{\mathcal C}` is to contain top, occurring concept names, occurring nominals, and occurring concrete atoms. It does not say that these are exactly its elements. Lines 99–102 use membership in that set to distinguish normalized forms and hatted nonbasic descriptions. Lines 116–119 then introduce the metavariable `B` in NF6 and NF7 without declaring its range. The later construction at lines 172–183 requires a finite state determined by this vocabulary, and the truth lemma at lines 511–531 exhausts only top, bottom, concept names, nominals, and concrete atoms.

Both primary presentations define the basic vocabulary as the smallest set containing their listed descriptions: conference printed page 365, Section 3; report printed page 5, Section 3.1. This restriction supplies both the finite input-dependent state and the exhaustive cases used in the model construction.

The unrestricted reading is operationally consequential. Suppose the input contains `A ⊑ ∃r.(B ⊓ C)` and `∃r.B ⊑ D`, and the set allowed by the word "contain" also includes the compound description `B ⊓ C`. The first axiom then passes the displayed basic-filler normal-form test. The initialized label for `B ⊓ C` contains its self-label and top, but the listed completion rules have no rule that decomposes this self-label into `B` and `C`. The marked `A`-query can consequently miss the semantically forced consequence `A ⊑ D`. This is a defect in the literal specification of the allowed vocabulary, not a counterexample to the intended algorithm using the source's exact vocabulary.

Required correction: define `\mathsf{BC}_{\mathcal C}` as exactly the finite set listed, and apply the same definition to the normalized, marked CBox `\mathcal K`. Before NF1–NF7, declare the ranges of the generic concept metavariables, the hatted descriptions outside the basic vocabulary, and the fresh concept and role names. In particular, clarify that the unadorned `B` in NF6–NF7 is a concept-description metavariable rather than an undeclared restriction to concept names. Otherwise even a left-hand side such as top leaves the reader to infer whether the rule is applicable. The two-phase order should remain explicit.

## Checks with no additional finding

The following observations apply within the specified manuscript extent and the intended exact basic vocabulary identified above.

| Scope and evidence | Text-review assessment |
| --- | --- |
| Host `logic-in-computer-science.tex:292–327`, `337–346`, and `427–453` | The description-logics section supplies set-and-relation interpretations, nonempty abstract domains, TBox and ABox meanings, satisfaction, and the expansion of GCI before the C1 input at line 453. The usual top, bottom, and conjunction semantics at C1 line 53 have an actual preceding definition. |
| C1 lines 8–23 and 274–281 | The conference paper and report are attributed separately. The handbook identifies query marking and the feature guard as corrections and identifies the typed CR11 update. It does not present the corrected procedure as the exact unchanged simultaneous-classification algorithm. The report and conference bibliography keys resolve to different source records at `handbook/bib/handbook.bib:5966–5974` and `5985–5993`. |
| C1 lines 25–82 and 196–217 | Partial features, positive predicate arities, disjoint concrete carriers, finite feature supports, the empty conjunction, and the two roles of polynomial constraint reasoning and convexity appear before their operative use. No global unique-name assumption is inserted. |
| C1 lines 127–169 and 295–310 | The arbitrary-query reduction and marking equivalence have both directions explained. Freshness is used in the model expansion. The text expressly identifies marking as a query reduction and treats an impossible queried concept and disconnected nominal inconsistency in criterion (D). |
| C1 lines 219–235 and 257–267 | The undefined-feature example supports the need for CR8's feature guard. The rule checks that every conclusion feature is present in the relevant domain's positive support. CR9 retains the disjoint-domain conflict check. |
| C1 lines 237–310 | Every rule has an update, a membership/nonmembership condition or equivalent guard, and a fixed-point stopping description. The finite membership bound and reachability explanation support polynomial saturation once the input vocabulary and length declarations are repaired. |
| C1 lines 312–349 | The first run correctly traces conjunction, existential propagation, role inclusion, and role composition. The nominal run reaches both successors from the query nominal, permits CR6's merge, derives bottom at the query nominal, and distinguishes unsatisfiable `A` from inconsistency of the original CBox. Both runs are explicitly handbook constructions. |
| C1 lines 351–462 | The induction covers every completion rule. CR6 uses a genuinely existing witness supplied by a query/nominal path. The quotient argument derives equal labels and outgoing-role agreement from final saturation without assuming that equivalence already held at an earlier insertion stage. |
| C1 lines 464–563 | The witness construction handles empty support and finite simultaneous avoidance. Feature supports for different domains are disjoint. The interpretation covers names absent from the finite vocabulary. The truth lemma checks the nominal and partial-feature cases; the normalized-axiom proof uses role representative replacement where required. The root then supplies the asserted counterexample. |
| C1 lines 565–594 | Classification is obtained by polynomially many marked runs, with a separate conference/report theorem locator. ABox assertions are translated using singleton semantics, and consistency, instance checking, and concept satisfiability reduce to the established query interface. The report's broader task list is explicitly distinguished from the conference theorem. |
| C1 lines 595–608 | The rational and string examples preserve their distinct domains and predicate roles. The string superscript correction is attributed. The paragraph states the source admissibility result and its nonconvexity boundary without claiming that a new proof of Proposition 5 has been supplied in this paragraph. |
| C1 internal tags (Q), (D), (R), (F), and (T) | Each tag is introduced before its later use. No unresolved LaTeX cross-reference command occurs in the assigned extent. This inspection concerns source-text routing; rendered links, numbering, and page placement remain unverified. |

## Primary passages consulted

The primary PDFs, not existing review conclusions, control the source comparisons.

- Conference paper: title and authors on physical page 1; printed pages 365–367 (physical pages 2–4), including Table 1, Section 2, the Section 3 normal form, Table 2 and reachability definition, p-admissibility, Lemmas 1–3, Theorem 4, Proposition 5, and the rational/string nonconvexity examples.
- LTCS-05-01: cover identity; printed pages 4–15 (physical pages 5–16), covering the task reductions, Section 3.1 and Figure 1, Section 3.2 and Table 2, the declared size convention, Definition 3, Lemmas 4–7 and their proofs, Theorem 8, and the concrete-domain definitions and Proposition 10 opening. Printed pages 17–18 (physical pages 18–19) were consulted for the Proposition 11 locator and the string-domain argument's opening. This is not a complete independent review of all concrete-domain proofs or the remainder of the report.
- The report's existing physical-page-7 image was inspected as a supplementary reading of Figure 1 and its surrounding explanation. No manuscript page image was inspected.
- Policy: `spec/EDITION-2026-CONTRACT.md`, especially lines 44–69 on corrected content and attribution, 124–137 on independence, and 147–168 on admission and publication. The relevant notation convention was checked at `handbook/CONVENTIONS.md:218–225`.

## Remaining publication evidence and disposition

C1 remains open for the two required text corrections and a fresh review of the affected scope against the corrected hash. No result here accepts the text after line 615 or closes N-c-010.

The manuscript build, applicable static checks, rendered mathematical layout, pagination and cross-reference appearance, final page inspection, rights evidence, other independent review seats, admission records, and editorial acceptance are not established by this report. Their status in this review is **UNRESOLVED / pending separate evidence**. The source's production history and a successful text assessment cannot establish those gates. The governing contract requires those separate checks before formal admission or publication.

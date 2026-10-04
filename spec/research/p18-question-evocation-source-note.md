# PMCE question evocation: source and authoring record

Date: 9 September 2026. Unit: `ED26-P18-erotetic-0001`.

## Exact source

Andrzej Wiśniewski, *An Axiomatic Account of Question Evocation: The Propositional Case*, **Axioms 2016, 5(2), article 14**, DOI **10.3390/axioms5020014**. The paper itself gives publication on **26 May 2016**, following receipt on 15 February and acceptance on 13 May.

The selected file is the literal author-hosted publisher-layout `axioms-05-00014-v2.pdf`, obtained from [the author's institutional endpoint](https://awisniew.web.amu.edu.pl/publikacje/axioms-05-00014-v2.pdf). The suffix `v2` is retained without inventing a second publication date or independently identified journal edition.

Local file: `source/references/wisniewski-2016-question-evocation/axioms-05-00014-v2.pdf`.

- Size: **298,009 bytes**.
- SHA-256: **41c1c9f220e6c691f2d22a1fe3f9aa03ad784897771a354aef7b86f79d4cb524**.
- Physical pages: **14**.
- Final page: references and the author's **CC BY 4.0** license statement.

The root captured the exact endpoint with Python urllib using ordinary certificate validation and opened the result with pypdf, confirming title, author, date, page count and last-page contents. The failed worker attempt used Windows Schannel and returned a TLS authentication failure; no certificate checking was disabled. The complete article text, Sections 1–6 and all page transitions through the final references/license page, was read through the same author endpoint. The local file and its exact hash are the retained source artifact.

The actual local source's page 5 was inspected at readable resolution by the root for the entailment glyphs. Multiple-conclusion entailment uses double bars followed by equals; proper entailment uses double bars followed by a **left-pointing** outlined triangle. The body and symbol intake preserve those local roles with `\mathrel{\|=}` and `\mathrel{\|\!\triangleleft}`. This was inspection of a source page, not a manuscript render.

## Authored files

- `handbook/parts/p18/question-evocation.tex`
- `handbook/annex/p18/question-evocation.tex`
- `handbook/registry/calculi/p18-question-evocation.tex`
- `handbook/bib/intake-p18-question-evocation.bib`
- `handbook/registry/symbols-intake-p18-question-evocation.csv`

The body and annex provide the exact propositional question syntax, finite antecedents, ordered-expression/direct-answer-set distinction, semantic relations, axiom schema, four primitive rules, three derived forms, eleven admissible transformations and the two final one-common-answer variants. The rule sheet has nineteen entries in total. No driver, shared style, canonical bibliography or canonical symbol registry was edited by this writer.

The six mnemonic labels for the alpha/beta/export rules are editorial names for the source's transformations in Facts 20–25; they are not attributed as original printed rule names. The source's named R1–R4 and named earlier derived/admissible rules retain their roles. The historical Section 1.3 account and the PMC/PMCE syntax distinction are also included, without creating new whole-work obligations for every item in the article's bibliography.

## Source-to-treatment correspondence

| Source component | Body/annex destination |
| --- | --- |
| Section 2 syntax; Definitions 1–4 | `def:p18-qev-language`, `def:p18-qev-entailment`, `def:p18-qev-sequents` |
| Corollary 5 and elementary evocation boundaries | `thm:p18-qev-semantic-profile` / `annex:p18.qev.semantic-profile` |
| Section 3 axiom and R1–R4 | `sheet:p18-question-evocation` primitive entries |
| Propositions 6–7 and Theorem 8 | `thm:p18-qev-soundness` / `annex:p18.qev.soundness` |
| Lemma 9, including both residual-conjunction cases | `thm:p18-qev-representative-induction` / `annex:p18.qev.representative-induction` |
| Propositions 10–11 | `thm:p18-qev-classical-tools` / `annex:p18.qev.classical-tools` |
| Lemma 12 | `thm:p18-qev-empty-completeness` / `annex:p18.qev.empty-completeness` |
| Proposition 13 | `thm:p18-qev-conditionalization` / `annex:p18.qev.conditionalization` |
| Theorem 14 | `thm:p18-qev-completeness` / `annex:p18.qev.completeness` |
| Section 5.1 derived rules | `thm:p18-qev-derived-rules` / `annex:p18.qev.derived-rules` |
| Facts 15–25, including all alpha/beta cases | `thm:p18-qev-admissible-rules` / `annex:p18.qev.admissible-rules` |
| Final paragraph of Section 5: one-common-answer variants | Right alpha/beta sheet entries with n at least one, and the same complete semantic proofs |
| Examples 1–5 | `thm:p18-qev-source-examples` / `annex:p18.qev.source-examples` |
| Sections 1 and 6 distinctions and limits | Opening and final body sections |
| Editorial finite decision and failed weakening | `def:p18-qev-decision-method`, `thm:p18-qev-decision` / `annex:p18.qev.decision` |

Classical prerequisites used in these arguments are supplied explicitly: valuation clauses, clause tautology characterization, a truth-table CNF construction, availability of fresh variables, injectivity of fixed formula prefixes, and the truth equivalences used by every alpha/beta and worked-example case. There is no unbound import of classical completeness or an unspecified normal-form algorithm.

## Direct proof corrections

The calculus and the target source results are preserved. Two construction gaps in the source's printed proof are repaired directly in the authored derivations. The book does not present a defective derivation followed by directions asking the reader to repair it.

**Lemma 9, page 8: induction parameter.** The source introduces a padded question Q-star with two fresh tautological conjuncts and observes that the recursive questions have smaller literal rank than Q-star. Its induction, however, started with the unpadded Q. The recursive ranks need not be smaller than that original rank. For example, the evoked normal-form question with answers `p and q` and `not p or not q` has literal rank one. The displayed padded recursive questions each still have literal rank one, not less than one. This does not refute the completeness theorem; it prevents that literal-rank argument from justifying the recursive calls.

The authored proof uses the stronger invariant of **chosen equivalent CNF representatives**. If a selected representative has m clauses, the first child uses its chosen nontautological clause as a one-clause representative; the second, when nontautological, uses the m-minus-one-clause residual. The ranks decrease by m-minus-one and one respectively. Fresh tautological markers keep actual answer expressions distinct but are absent from the chosen representatives used for induction. The base case uses arbitrarily long equivalent clause variants, produced by repeating a literal, so equivalent or identical unmodified clause representatives do not break the axiom syntax. Both source residual cases remain: combine two recursive results if the residual is nontautological, or use equivalent replacement directly if it is tautological.

**Proposition 10, page 9: global freshness.** Its first padding variable is required only to be absent from A1, which does not ensure that the resulting C1 differs from every other original answer. With A1=`p` and A2=`p and(q or not q)`, the allowed first choice q and representative p would give C1=A2. The existence claim is readily repaired. Every marker in the authored construction is chosen absent from **all original answers and all selected CNF representatives**, and different from the other markers. This proves both pairwise distinctness and disjointness from the entire original answer set. The latter is then used explicitly at every R2 restoration step.

Minor source display slips, including the changed terminal answer index in equation (22) and the stray turnstile in Fact 16's evocation expression, are not reproduced. The intended indexed question and the well-typed relation `E(X,Q)` are written directly.

## Limits and standing

The full author read-through covered the body, all eleven annex proofs and all nineteen sheet entries in the authored contents. It checked each rule's coverage and non-entailment obligations, the two completeness branches and decreasing ranks, all five source-example equivalences, and the final syntactic-distinctness conditions. It also moved all list/alpha/beta and rule-standing definitions before the sheet, confirmed the source's left-pointing proper-entailment sign, and used `\ensuremath` for rule names because the shared renderer prints that argument in text mode. The retained source examples and the two explicit source-proof counterexamples were calculated directly; no software test suite was created.

Worker native read-back commands were intermittently unavailable because process setup returned `helper_unknown_error`; the read-only filesystem connector also returned an internal error. Successful scoped `apply_patch` calls saved the files and matched every subsequent patch against their actual content. The root supplied the source capture/hash and the small shared-renderer/glyph lookups through its working tools. Root integration still needs to record final authored-file hashes, merge the distinct intakes and route the body/annex; none of those shared operations is claimed performed by this writer.

The completeness theorem is for **finite propositional antecedents** and well-formed finite questions. The article's source-specific distinctions from erotetic implication, interrogative inquiry, question resolution and first-order question languages remain explicit. Its 2016 discussion of further research is not asserted to describe the entire literature's status in 2026. The truth-table procedure is an editorial consequence of the proved semantics and completeness, not a claim that the source's R2-based calculus is an efficient analytic proof-search method.

This record documents source acquisition and an authored treatment. Independent source-fidelity, topic and publication reviews, driver/canonical integration, final build and output inspection remain the lead's later consolidated work. No independent review, manuscript render/build or prose-mirroring software tests were performed by this writer.

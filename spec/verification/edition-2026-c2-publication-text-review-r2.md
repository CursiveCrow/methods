# C2 independent adversarial publication text review, repair recheck

Review date: 7 September 2026. Reviewer context: `/root/edition_c2_publication_review`.

## Scoped verdict

**PASS for the bounded publication text repair recheck.** The revised files close C2-PUB-01, C2-PUB-02 and C2-PUB-03 from this reviewer's first report. No new blocking publication text defect was found in the reread scope.

This conclusion concerns accurate separation of the bibliography's journal and report identities, the reader's introduction to CSL, the summary row's theorem routes, and the coherence of the retained nearby text. It does not certify the final journal article's complete body, its precise mathematical locators, complete N-x-015 coverage, exact-source reconstruction, formal admission or release. The full source-body and visual/publication evidence boundaries remain **UNRESOLVED**.

The reviewer inspected the current files and primary institutional metadata independently. Other reviewers' outputs and author conclusions were not consulted. No subagent was used. The actual runtime model identifier, reasoning-effort configuration and service tier were not exposed; all are recorded as **unavailable**. The only file created by this reviewer in this round is this report. No manuscript, bibliography or previous report was edited. No build, manuscript render, visual inspection or software test was run.

## Inputs and extent

The live root remains `C:/Dev/the-methods-of-reason`, branch `phase4-codex`, HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`. These identify the checkout; the SHA-256 values below identify the actual files examined with their uncommitted changes.

| Input | Recheck extent | SHA-256 |
| --- | --- | --- |
| [Current host](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:1318) | Complete CTMC/CSL definition through the comparison table, lines 1318-1590; later row and immediate context, 2450-2461 | `61e3125b950ae194412c81bc6c5eeb3dfceac533541b26007f6db7744e3ddc45` |
| [Current bibliography](C:/Dev/the-methods-of-reason/handbook/bib/handbook.bib:2508) | Complete journal and report entries, lines 2508-2532 | `8c4ae5fcd93092eb676ec04878a6ee09406e987464a5cebf2e9db9c139b7105f` |
| [CSL annex](C:/Dev/the-methods-of-reason/handbook/annex/p09/csl-corrections.tex:1) | Whole-file hash confirmed unchanged from round 1; source routes and proof-dependency passages reread at lines 1-8, 41-48 and 58-82 | `92aeada76892a0dbf271b8002dca189d563ba39c389ebb478be3d438521c42f5` |
| [Annex driver](C:/Dev/the-methods-of-reason/handbook/annex/p09.tex:1) | Complete lines 1-6; unchanged hash | `47a28fa80f2cad42054c36628815326f9898036c58fafaff876e3703c154cb15` |
| [Governing amendment](C:/Dev/the-methods-of-reason/spec/EDITION-2026-CONTRACT.md:44) | Whole-file hash confirmed unchanged; the previously read correction and source-version policy remains the governing scope | `c9b101ad6bf6bfea5a3e1fbec25cdba81b47667146474861eb1aa00b5dfa1bf3` |
| [Style dependency](C:/Dev/the-methods-of-reason/handbook/handbook.sty:342) | Whole-file hash confirmed unchanged; the previously inspected status and annex routing macros remain applicable | `1b5c089594010dd517389cdf510cdfbf741e014eaac877cc5bb44f3991412288` |
| [First publication text report](C:/Dev/the-methods-of-reason/spec/verification/edition-2026-c2-publication-text-review.md:1) | Preserved as the historical round-1 assessment; whole-file hash confirmed unchanged | `e60dfdf15f1763702b48232d52c9c482bc26c143ba8f229b3489c7eccbd630fc` |

Both new supplied hashes matched. The annex, driver, style, policy and first report retained their round-1 hashes. The original complete annex reading and its bounded positive assessments therefore remain relevant; this round does not substitute a hash check for an initial content review.

## Finding dispositions

### C2-PUB-01 — Journal identity and earlier report URL

**PASS: closed for the publication text attribution defect.**

The [journal entry at lines 2508-2519](C:/Dev/the-methods-of-reason/handbook/bib/handbook.bib:2508) retains the 2003 journal metadata and now uses `https://doi.org/10.1109/TSE.2003.1205180` as its URL. The separate [report entry at lines 2521-2532](C:/Dev/the-methods-of-reason/handbook/bib/handbook.bib:2521) identifies the University of Twente CTIT report, number 02-10, date April 2002, and owns the earlier report PDF URL.

The [host at lines 1470-1472](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:1470) expressly identifies the April 2002 report as an earlier presentation and states that its locators and the journal locators identify separate versions. A targeted search of the handbook's LaTeX and bibliography finds the new report key in this historical/version sentence and its own bibliography entry. The numbered mathematical source citations in the inspected CSL section remain attached to the journal key. The earlier report is therefore no longer silently presented as the document reached through the journal entry.

The primary [University of Twente journal record](https://research.utwente.nl/en/publications/model-checking-algorithms-for-continuous-time-markov-chains/) was reopened for this round. It confirms the journal title, volume 29, issue 6, June 2003 publication, pages 524-541, and this DOI. The primary [University of Twente report record](https://research.utwente.nl/en/publications/model-checking-algorithms-for-continuous-time-markov-chains-2/) was also reopened and confirms April 2002, CTIT technical report series 02-10, the institution and the separate related journal article. The revised entries now reflect these distinct identities.

This closes the previously misleading bibliography route. It does not establish that every numbered journal citation has been checked against the final article body. The DOI is confirmed by primary metadata; a direct web-reader opening attempt was rejected by that tool's URL-safety check. That tool response is not evidence that the DOI is invalid, and it supplied no readable journal body. The source-body boundary from round 1 remains open.

### C2-PUB-02 — CSL expansion

**PASS: closed.**

The definition title at [host line 1318](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:1318) now reads “Continuous-time Markov chains and continuous stochastic logic (CSL).” The reader receives the expansion at the local introduction before the grammar uses the acronym. The change adds no proof obligation.

### C2-PUB-03 — Later summary route

**PASS: closed.**

The summary row at [host lines 2455-2460](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:2455) now routes to both `thm:p09-csl-interval-computations` and `thm:p09-csl-model-checking`. Both labels exist in the current host, respectively at lines 1478 and 1454. The first supplies the corrected computation and annex route; the second retains the cited overview's distinct role. The row still states the endpoint-flag, rigorous-error-interval and equality conditions.

The status wording remains qualified by those conditions. This recheck does not read it as an unconditional total algorithm for all exact threshold cases or as a named complexity-class result. Actual rendered links and table layout remain unverified.

### Additional bounded edit — Rational probability thresholds

**PASS within the text remit; no new finding.**

At [host line 1364](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:1364), `q` is now expressly rational and in `[0,1]` before the grammar is given. The four comparison relations remain declared at line 1365. This makes the probability-threshold domain explicit and does not change the time-endpoint formulas, path clauses, or any printed example. Verification of an exact source-syntax correspondence remains a separate source-fidelity question.

## Retained content and regression assessment

The current host's full CSL passage was reread rather than accepting the repair description as evidence. Apart from the title, threshold domain, version paragraph and summary route discussed above, the relevant definitions, expressions, qualifications and explanatory sequence retain the substance assessed in round 1. This is an inspection of the identified content, not a claim to have compared every byte of the entire old and new host files.

| Retained subject | Current host ranges and relevant annex dependency | Recheck result |
| --- | --- | --- |
| Rates, actual path steps, self-loops and right-continuous occupation | Host 1319-1362; unchanged annex item 1's Poisson construction | PASS; the earlier distinction between generator occupation and actual next events remains explicit |
| Endpoint normalization, excluded zero, positive singletons and empty intervals | Host 1407-1439; annex item 1 | PASS; the initial-state test and separate singleton/empty cases remain present |
| Fixed original-chain state sets and transient decomposition | Host 1475-1511; annex 41-71 | PASS; vector orientation, `D_A`, fixed `A` and `B`, absorbing transformations and unbounded reachability dependency remain explicit |
| One-state and two-state examples | Host 1441-1452 and 1513-1523 | PASS; the occupation versus first-entry distinction remains intact |
| Timed next | Host 1525-1539; annex 74-81 | PASS; zero for absorbing states and singleton waiting-time intervals remains distinct from singleton until |
| Numerical certification and comparison tables | Host 1541-1590 and 2455-2460 | PASS; tail error, separate arithmetic error, propagated bounds, threshold side and exact equality limits remain stated |

The annex driver's unchanged line 6 still includes the CSL annex. The host's endpoint theorem retains `proved=annex:p9.csl.1`; its corrected computation theorem retains `proved=annex:p9.csl.2`. The matching annex items retain their exact host back-references. Annex lines 43-48 still identify the no-jump fact and the cited embedded-chain dependency while limiting the direct proof's scope. The host at lines 1475-1477 still distinguishes the local derivation from the cited Volterra and steady-state results. No new proof cycle, dangling source reference or silent extension of the local proof's remit was introduced by the inspected repairs.

## Evidence boundary and handoff

The round-1 failure remains preserved in its original report as a verdict on the earlier hashes. This round's PASS applies to the current hashes and the stated publication text scope. All three finding IDs are closed in that scope; there is no unresolved publication text repair request from this reviewer.

The exact final-journal body has not newly been obtained or read. Journal-numbered definitions and results have not received a new body-level verification in this round. Neither institutional metadata nor an accurate DOI replaces that evidence. Independent full source review, the specialist mathematical gate, manuscript build/static evidence, rendered-page and visual publication inspection, separate formal admission, full N-x-015 coverage and final acceptance retain their own requirements. This report grants none of those outcomes.

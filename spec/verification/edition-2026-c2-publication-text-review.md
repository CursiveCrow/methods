# C2 independent adversarial publication text review

Review date: 7 September 2026. Reviewer context: `/root/edition_c2_publication_review`.

## Verdict and scope

**Scoped verdict: FAIL.** The inspected endpoint, transient-analysis, timed-next, and numerical-boundary text is coherent for a graduate reader, but its bibliography combines the 2003 journal article's identity with an unqualified link to the distinct 2002 technical report. Finding **C2-PUB-01** must close before this publication text remit can pass. Two further observations are nonblocking improvements to terminology and navigation.

This is an independent review of the actual LaTeX and the specified bibliography dependency. No other C2 reviewer report or author assessment was read. No subagent was used. The actual runtime model identifier, reasoning-effort setting, and service tier were not exposed to this reviewer; they are **unavailable**, not inferred from a generic agent description.

The review covers the host's complete CTMC/CSL definition and ensuing material, its two complete new annex items, the annex driver, and the later CSL boundary row. It assesses reader usability, definition order, examples, attribution, and source/proof navigation. It does not establish complete N-x-015 coverage, exact-source reconstruction, formal admission, the specialist mathematical gate, or release acceptance. Manuscript compilation, software tests, manuscript rendering, and visual publication inspection were not performed. The full visual/publication gate remains **UNRESOLVED and pending**.

## Frozen inputs and actual extent read

The live root was `C:/Dev/the-methods-of-reason`, branch `phase4-codex`, HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`. The worktree contains extensive pre-existing changes. Only this review file was created by this reviewer.

| Input | Extent read | SHA-256 |
| --- | --- | --- |
| [Host](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:1318) | Complete lines 1318-1587; preceding PCTL context 1200-1317; source-standing context 1-51; table context 2393-2456; concluding source attribution 2547-2554 | `1eaf705ced9c83e18edd1129f0f0996663840fdfd5b22bee411b871eb3d85dd3` |
| [CSL annex](C:/Dev/the-methods-of-reason/handbook/annex/p09/csl-corrections.tex:1) | Complete file, lines 1-82 | `92aeada76892a0dbf271b8002dca189d563ba39c389ebb478be3d438521c42f5` |
| [P9 annex driver](C:/Dev/the-methods-of-reason/handbook/annex/p09.tex:1) | Complete file, lines 1-6 | `47a28fa80f2cad42054c36628815326f9898036c58fafaff876e3703c154cb15` |
| [Actual bibliography entry](C:/Dev/the-methods-of-reason/handbook/bib/handbook.bib:2508) | Entry `BaierHaverkortHermannsKatoen2003`, lines 2508-2519 | `d5bab1c74ab2b378eaacafe2ce1b313209e71e46a28dd2748ef7c539c5cb7094` for the full bibliography file |
| [Governing amendment](C:/Dev/the-methods-of-reason/spec/EDITION-2026-CONTRACT.md:1) | Complete file; correction and source-version requirements at lines 44-74 are specifically relevant | `c9b101ad6bf6bfea5a3e1fbec25cdba81b47667146474861eb1aa00b5dfa1bf3` |
| [Status and annex macros](C:/Dev/the-methods-of-reason/handbook/handbook.sty:342) | Status output at 342-347, result routing at 461-478, annex environment at 1610-1621; surrounding parser declarations were inspected | `1b5c089594010dd517389cdf510cdfbf741e014eaac877cc5bb44f3991412288` for the full style file |

The three assigned frozen-file hashes matched the supplied hashes. File hashes identify the inspected snapshots, not acceptance of every part of those files. The additional context read to understand nearby definitions and references was not reviewed as a separate content unit.

## Source evidence actually obtained

The 2003 journal identity is confirmed by the authors' institutional publication records: *IEEE Transactions on Software Engineering* 29(6), June 2003, pp. 524-541, DOI `10.1109/TSE.2003.1205180`. These fields agree with the bibliography entry. The [University of Twente journal record](https://research.utwente.nl/en/publications/model-checking-algorithms-for-continuous-time-markov-chains/) identifies the 2002 report separately; the [TU Dresden publication record](https://iccl.inf.tu-dresden.de/web/Article2484194115/en) independently confirms the journal citation.

The [University of Twente report record](https://research.utwente.nl/en/publications/model-checking-algorithms-for-continuous-time-markov-chains-2/) identifies a report published in April 2002, CTIT technical report series 02-10. Its downloadable file has identifier `268940692` and filename `Baier2002model_checking.pdf`, matching the file identifier and name in the handbook's URL. The report record separately links the June 2003 journal article. These are affirmative institutional version distinctions, not an inference from the filename alone.

The [PDF linked in the bibliography](https://ris.utwente.nl/ws/files/268940692/Baier2002model_checking.pdf) was opened by the web reader, which reported 37 pages. Its extracted body was largely garbled. A source-page screenshot attempt did not return an inspectable image in this reviewer context. The alternate institutional file endpoint returned HTTP 403, and a journal-layout copy at CiteSeer could not be fetched. Consequently this reviewer did **not** read a reliable complete 2003 article body or validate every source theorem locator against that body. Bibliographic metadata proves the version mismatch; it does not prove equivalence or difference of the two versions' mathematical statements. No source acquisition or exact-source reconstruction gate is closed here. No source PDF was downloaded, changed, or accepted as a new canonical artifact.

## Findings

### C2-PUB-01 — Unqualified report URL under the journal article identity

**Status: FAIL; blocking within this remit.**

Evidence: [bibliography lines 2508-2519](C:/Dev/the-methods-of-reason/handbook/bib/handbook.bib:2508), especially `year = {2003}`, the journal, volume, issue, pages and DOI, followed by the URL to file `268940692/Baier2002model_checking.pdf`. The institutional records above identify that linked object as the 2002 report and the journal article as a separate 2003 publication. The entry supplies no version note or separate report identity. The host repeatedly directs the reader to this key as its source, including [lines 1334, 1362, 1403 and 1469](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:1334).

Why it matters: a reader following the bibliography is led to a different source version without being told so, while the text attributes numbered definitions and results to the journal article. This leaves the route from the printed source claim to the available document ambiguous. The governing amendment at lines 60-65 requires distinct source versions and their attribution to survive. A linked technical report can be useful, but its version must be identified and its role justified.

Closure condition: make the journal entry's operative locator point to a verified journal record or verified journal-version body. If the 2002 report remains an operative accessible source, identify it explicitly with its own version role and appropriate bibliographic record or clear version note, then independently verify which version supports the printed numbered locators. Preserve the 2003 article's identity. Merely replacing `2002` with `2003` in a filename, or asserting that the reports are equivalent without comparison, does not close this finding. Re-review the changed bibliography and any affected source-attribution prose; the mathematical corrections need not be rewritten solely to repair this bibliographic issue.

### C2-PUB-02 — Expand the CSL name at its local introduction

**Status: nonblocking editorial observation.**

Evidence: the definition title at [line 1318](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:1318) says “Continuous-time Markov chains and CSL”; line 1365 introduces the “CSL grammar.” The full phrase occurs in the index command at line 1404, which does not display an expansion in the running exposition. In contrast, the preceding PCTL definition's title supplies its expansion.

Reader impact: a reader entering at this definition must recover the logic's name from another location or external source. This does not change any formula's meaning.

Closure condition: introduce “Continuous Stochastic Logic (CSL)” in the title or first explanatory sentence. No new proof or software test is needed for that edit.

### C2-PUB-03 — Point the summary row to the corrected computation as well as the cited overview

**Status: nonblocking navigation observation.**

Evidence: [lines 2452-2456](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:2452) retain the endpoint and equality qualifications, but route only to `thm:p09-csl-model-checking`. That theorem at lines 1454-1470 is the cited four-computation overview. The explicit endpoint-aware formulas and annex proof route belong to `thm:p09-csl-interval-computations` at lines 1475-1508; the numerical certification discussion follows at lines 1538-1564.

Reader impact: the route reaches the correct local topic, so it is not a broken reference. It could lead more directly to the material that justifies the row's stated endpoint and numerical boundaries. The phrase “effective with certified numerical boundary” must continue to be read with the printed equality qualification; this review does not promote it to an unconditional decision procedure or a named complexity-class bound.

Closure condition: add the corrected-computation theorem or a precise local subsection reference to the row. If the status cell is revised, describe the certified approximation and threshold conditions explicitly rather than suggesting that this text supplies a total exact algorithm for every equality case.

## Evidence for the portions that pass this text review

| Check | Independently assessed evidence | Scoped result |
| --- | --- | --- |
| Rate map versus generator and self-loops | Host 1319-1334 defines `R`, `E` and `P` before use and explicitly distinguishes rate self-loops from occupation probabilities; `Q_C` is introduced at 1481-1486. The one-state case with a positive rate self-loop has zero generator but an actual next event, consistent with the printed distinction. | PASS |
| Timed paths, finite termination and occupation | Host 1336-1362 defines positive residence times, cumulative times, time divergence for infinite paths, right-continuous occupation, the absorbing tail and finite-prefix probabilities. A zero-step absorbing path remains meaningful for until and has no next step. | PASS |
| Syntax, endpoint inputs and probability operators | Host 1364-1403 separates state and path formulas, gives interval flags and singleton meaning before the timed clauses, excludes infinity as a witness, and distinguishes path probability from the long-run occupation limit. This is a reader-level assessment, not a complete formal definedness audit of inherited notation or a source-syntax equivalence claim. | PASS |
| Endpoint normalization and empty cases | Host 1410-1437 distinguishes positive finite endpoints, excluded zero, closed singletons and empty intervals. Annex 10-37 supplies the local-constancy argument and explicitly rejects dummy Poisson ticks as actual path steps. | PASS |
| Fixed formula interpretation during chain transformations | Host 1476-1489 fixes `A` and `B` in the original chain before constructing modified generators, preventing a reader from reevaluating nested CSL formulas in a changed chain. Column-vector orientation is explicit. | PASS |
| Positive lower bounds and singletons | Host 1491-1506 and annex 58-71 retain the first-phase `D_A` filter, explain why `A` intersected with `B` is not absorbing before the lower time bound, and cover zero-duration second phases. | PASS |
| Timed next is separate from until | Host 1522-1536 gives a separate first-transition computation, zero for absorbing states, and zero probability for all singleton waiting-time intervals. Annex 74-81 supplies its conditioning explanation. It is not confused with state occupation at a fixed time. | PASS |
| Numerical threshold certification | Host 1538-1564 states the uniformization rate guard, an exact zero-time case, lower partial-sum bounds, a Poisson-tail upper correction, separate arithmetic error, propagated composition errors, and the threshold/equality boundary. It does not certify a clause from a displayed decimal. | PASS |
| Comparison consistency | Host 1572-1585 keeps DTMC, MDP and CTMC transition objects and computations separate. The later CSL row at 2452-2456 preserves endpoint flags, error intervals and the equality limitation. The route improvement is C2-PUB-03. | PASS with nonblocking observation |

### Examples checked by hand

The one-state absorbing example at host 1441-1452 is consistent with the definition. A positive until witness for a false left operand fails at time zero, while witness zero needs no earlier state. Thus the two probabilities are respectively zero and one. With `p` true throughout the path, `p U^[a,a] p` has probability one even at a positive singleton; no claim about zero mass of jump times invalidates this occupation event.

For the two-state example at host 1510-1520, let `T` be the exponential first transition time. With `A = {s}` and `B = {g}`, success in a positive-lower-bound interval requires `T` between its endpoints, giving `exp(-r a) - exp(-r b)`. A singleton then has probability zero. With `A = S`, entry before `a` is allowed and persists in the absorbing state `g`, giving `1 - exp(-r a)` at the singleton. These are different events, and the text explains why.

The matrix formula also reproduces the first of those computations: the `s` row after time `a` is `(exp(-r a), 1 - exp(-r a))`; multiplication by `D_A` removes paths already at `g`; the remaining until probability over `b-a` is `1 - exp(-r(b-a))`. Their product is exactly the printed expression. These are hand calculations, not software-test results.

### Status, annex routes and proof dependencies

The host marks endpoint normalization `proved=annex:p9.csl.1` at line 1410 and the interval computations `proved=annex:p9.csl.2` at line 1475. The corresponding annex items at lines 6 and 41 exist, and their back-references name the matching host theorems. The driver includes the annex at line 6. The status macro prints a hyperlinked annex destination for a proved result, and the annex macro prints the theorem back-reference. This verifies the intended routes in source; actual typeset destinations and page appearance remain unverified.

The proof dependency is explicit and acyclic in the inspected text: annex item 1 obtains the fixed-time no-jump fact from its Poisson construction; annex item 2 cites that fact and separately cites the embedded-chain result for `h`. The latter dependency is identified at annex lines 45-48. The source's Volterra and steady-state results remain cited results rather than being presented as reproved by the interval derivation. The host at lines 1472-1474 tells the reader that the following direct derivation fixes occupation and endpoint conventions. This supports the current policy of correcting active text while retaining the distinction between the cited results and the local derivation.

## Completion and remaining gates

The textual examination and assigned report are complete. **C2-PUB-01 is the sole blocking publication text finding from this review.** The remaining two observations do not independently require a failure verdict. The positive assessments above are limited to their listed ranges and remain reusable only while those inputs and relevant dependencies remain unchanged.

A later pass requires closure evidence for C2-PUB-01 against the revised source route. Independent source-fidelity and topic-specialist review still control their own claims. A frozen manuscript build, appropriate static checks, rendered-page inspection and separate admission evidence are still required before any broader publication or admission conclusion. No such gate is marked complete by this report.

# N-c-012: complete sequential text inventory

All **3,060 lines** of the active N-c-012 presentation have been read sequentially. The four originally named sources all have substantive presentations, and Alpern–Schneider adds the semantic safety/liveness development. The material combines full supplied arguments, detailed source outlines, cited results, corrected constructions, and explicitly unresolved historical claims. It is not uniformly a completed local proof development.

The assigned inventory is complete. Whole-source coverage and independent mathematical acceptance remain unverified.

## Reading evidence and active route

- File: [handbook/parts/p09/presentations/n-c-012.tex](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex); 139,448 bytes; 3,060 lines.
- SHA256 throughout all reads and the final check: `0B7A17D844D8F69407BF1E41C6423FD21D11CC7C853B353BDB6562B468EAC810`.
- Complete numbered non-truncated intervals: 1–300, 301–600, 601–900, 901–1200, 1201–1500, 1501–1800, 1801–2100, 2101–2400, 2401–2700, 2701–3060.
- Ten intervals, no gaps or overlaps; next unread line: **none**.
- Finalized: 2026-09-07 09:28:32 UTC.
- Active route: [handbook/main.tex:33](C:/Dev/the-methods-of-reason/handbook/main.tex:33) → [handbook/parts/p09.tex:3](C:/Dev/the-methods-of-reason/handbook/parts/p09.tex:3) → [handbook/parts/p09/logic-in-computer-science.tex:950](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:950).
- The JSON records 48 headings, 35 result/algorithm entries, seven references to six distinct targets, five bounded dependency readings and all reading hashes.

Headings/references were extracted after sequential reading for reconciliation. Primary PDFs were not re-read here, so the source identities and version distinctions below are current manuscript/bibliography statements, not new acceptance of held file identities. Only the two assigned audit outputs were written. No manuscript, source, registry or bibliography edits, acquisitions, tests, builds or renders occurred.

## Original requirement

[N-c-012](C:/Dev/the-methods-of-reason/spec/registers/new-content.csv:119) requests “LTL deepened: past operators, Kamp and Gabbay-Pnueli-Shelah-Stavi expressive completeness statements, safety/liveness, PSPACE satisfiability.” It names Kamp 1968, Pnueli 1977, GPSS 1980 and Sistla–Clarke 1985. Its original treatment field is T and its note says expressiveness and complexity are the gap.

That historical field is retained in the JSON but is not a current ceiling. Conversely, the existence of a citation or a source's own sketch is not automatically a missing-proof defect. The inventory distinguishes what the source reportedly supplies, what the handbook actually expands, and what is explicitly unprinted or unresolved.

## The five source presentations

| Actual lines | Source and text present | Proof/source standing |
|---|---|---|
| [6–361](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:6) | Kamp: four order classes; equality-free FO operations; strict S/U argument order; explicit forward translation; reverse theorem chain; rational-cut boundary; integer isolation tenses and sparse-square argument. | Main Chapter III reverse construction and most adjacent separations are summarized. The corrected integer IV.3 induction is supplied in detail. |
| [363–1201](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:363) | Pnueli: transition/program models; strict leads-to; P1/P2/ER; future calculus and quantified schemata; system/fairness rules; sequential/concurrent attachments; finite decisions and Appendices A/B. | Mixed supplied counterexamples and proofs, full rule displays, source sketches and unresolved claims. P2 is explicitly historical and unsound; it is not adopted by the active LTL sheet. |
| [1203–1838](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:1203) | GPSS: strict future convention and local repairs; response/fairness/precedence formulas; exact FO result domains; normal-form outline; DX/DUX and transformed D0X/D0UX schemes. | Expressiveness and canonical completeness remain source outlines. Unprinted gap operators are not adopted. The conflicting U0 variant is explicitly not a coherent defined operator. |
| [1840–2670](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:1840) | Sistla–Clarke: operator-sensitive languages; satisfiability/validity/existential-path truth; small structures; NP certificate; PSPACE reductions and guessed-type algorithm; regular-operator extension; full classification table. | Some longer source proofs are summarized. Corrected occurrence-sensitive/cyclic-SCC certificate is supplied. Journal version controls; current ETL reconstruction excludes epsilon emissions. |
| [2672–3060](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:2672) | Alpern–Schneider: safety, liveness, uniform/absolute variants; examples; prefix topology; both decomposition theorems; corollaries and Boolean closure. | Substantial complete local proofs, including supplied hypotheses and corollary correction. Plotkin's private-communication syntactic claim remains unverified. |

There is **no absent originally named primary-source subsection analogous to N-c-017's McMillan boundary**. There are specific constructions and variants that are not supplied, as detailed below.

## Kamp: exact theorem scope and construction gap

[Lines 16–72](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:16) define nonempty strict linear orders and the four source classes. Completeness is order completeness; endpoints and discreteness are permitted. The FO vocabulary is equality-free and the uniform current-point operation is typed explicitly.

The strict witness/open interval and source operand order are fixed at [74–131](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:74), with a capture-safe temporal-to-FO recursion. The reverse route at [133–155](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:133) names III.1, III.2 and Lemmas 1–10, describes the cut/interval dependence on complete orders, and states primitive recursiveness. It does not give the actual normal-form algorithm and all lemma proofs. The rational-cut interpretations and most IV.1/IV.2/IV.4/IV.5 arguments are likewise descriptions rather than full constructions.

In contrast, [167–341](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:167) supplies the integer isolation operations, exact sparse-square interpretation, and a corrected structural induction with the necessary same-parity condition. That corrected induction is explicitly the argument used. Source-error prose and the refuted original clause remain visible, but the result is not made to depend on the false clause.

## Pnueli: historical rules versus adopted mathematics

P2's exact current reader role is decisive:

| Question | Actual evidence and disposition |
|---|---|
| Where is P2 displayed? | [490–515](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:490): historical natural-rank rule, current-state target, strict leads-to conclusion. |
| Is it asserted sound by the handbook? | No. [517–541](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:517) supplies two explicit counterexamples and denies soundness. |
| Is a corrected active P2 supplied? | No complete strict-future replacement appears anywhere in the full file. [525–531](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:525) explains a sufficient no-zero-rank premise for **inclusive** eventuality only. |
| Do later N12 proofs use uncorrected P2? | None does. Later references discuss the source inconsistency. |
| Is it part of the active handbook LTL sheet? | No. The complete [10-line sheet](C:/Dev/the-methods-of-reason/handbook/registry/calculi/hilbert-ltl.tex:1) uses inclusive X/U with theorem-only next necessitation and until induction. |
| Does its historical display alone violate the direct-correction instruction? | The evidence does not establish that. The rule is expressly refuted historical content, not an adopted valid rule or a premise of a later proof. Retaining that diagnostic source discussion is a publication decision. |

ER is displayed with explicit parameter typing and the induction metarule. Its Theorem 1 is identified as a sketch, with local counterexamples for the jump from initial-state executions to all-state assertions and for vacuous nonserial path semantics. A2's strict/inclusive conflict is recorded. Theorem 2's S4 referral is separated from linear-time completeness by an explicit branching countermodel. Theorem 3's ER embedding and relative completeness remain unresolved because pure K_b lacks the needed system rule E. None is promoted into an accepted handbook adequacy theorem.

The positive supplied content is substantial: typed program attachments; producer–consumer consequences from the stated invariants; a two-direction cyclic-SCC criterion for proper executions; the P/MRG restriction example; and Appendix A's six-step local inference. The producer–consumer location indicator support sets are source-unprinted, so the argument does not reconstruct every invariant-preservation transition.

Appendix B prints a precise language recursion and inclusion route. [1166–1201](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:1166) explicitly says the proper-execution acceptor's tuple, acceptance, construction and proof are not printed; closure and inclusion machinery are external dependencies. This source boundary is distinct from a later general LTL automaton construction.

## GPSS: all printed systems, with their proof boundaries

The strict future convention is made coherent by an expressly attributed correction of the source's reversed inequality. The source-unprinted past dual and the next-at-endpoint clause are separately supplied. The exact strict/inclusive translations retain X and Y.

The four FO statements at [1520–1543](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:1520) have different domains: point zero on omega words, future formulas on discrete complete orders, past/future separation, and arbitrary orders with additional gap symbols. S' and U' have no adopted grammar, arity or semantic clauses.

[1545–1649](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:1545) gives the actual At/Bet/Aft/Bef and special/decomposition classes. Proposition 2.4's event-expression translations remain the omitted core. The source's numbering discrepancy and external Shelah–Stavi/Gabbay referrals are recorded. It is expressly a source outline.

DX/DUX and D0X/D0UX all have their displayed schemes and rule packages. The canonical relation, closure quotient and fair-thread route are described, but maximal extension, relation lemmas, fair-thread construction and truth-lemma cases are not fully derived. No complexity bound is invented. The literal U0 definition and recursion conflict has a counterexample, and [1801–1805](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:1801) explicitly declines adopting them as one operator. These are not aliases for the active Part VIII strong-until calculus.

## Sistla–Clarke: source proof detail and supplied repairs

The 1985 journal is controlling. The 1982 predecessor contributes separately marked version/definition evidence; theorem numbers, next-operator counts and the corrected regular-operator proof are not conflated.

The fragment grammar and path quantifier matter throughout: L(F), positive tilde-L(F,X), L(F,X), L(U), L(U,S,X) and ETL differ. The source's R-truth asks for **some** path. The host's universal result is reached via negation and PSPACE complement closure.

The small-structure account gives exact ambient subsequence measures and preservation clauses. It replaces false strict source inequalities by the proof-supported non-strict bounds, but the principal extraction/small-model arguments remain sketches or summarized lemmas. The NP certificate at [2145–2234](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:2145) explicitly corrects two substantive problems: prefix truth sets must index occurrences, and the recurrent strongly connected set must contain a positive cycle. The corrected data govern subsequent acceptance.

The PSPACE section supplies graph-constraint formulas and local guessed-type conditions, with initial since, saved loop-entry and eventuality obligations. The Turing computation reduction and main periodicity inductions are not fully expanded locally. The text distinguishes the finite closure size from the number of realizable truth sets and valuation periodicity from subformula periodicity/fulfilment.

ETL at [2468–2637](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:2468) has exact grammar constructor semantics, continuation-tree and negative-layer conditions. The current proof deliberately requires **nonempty terminal emissions**; epsilon emissions are explicitly unestablished. The parity sentence in the printed grammar example is corrected semantically and is not used later. The full source classification table is present.

## Safety/liveness: supplied decomposition proofs

This section uses the full space S^omega with nonempty S, not silently the path space of one program. It supplies exact uniform/absolute liveness distinctions, repaired leads-to assumptions, and the predictive live-but-nonuniform example.

The closed/dense equivalences have two-direction proofs. Theorem 1's closure factor and Theorem 2's two disjoint eventual-constant factors are fully argued, including the singleton-space boundary. Corollary 2.1 has the corrected **union-closure** hypothesis and a concrete counterexample to intersection closure alone. The subsequent mathematics uses the corrected construction. The private-communication temporal-syntax claim at [2945–2949](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-012.tex:2945) remains explicitly unverified.

## Essential interfaces

All seven references to six distinct targets were resolved. The current host was read at [handbook/parts/p09/logic-in-computer-science.tex:615](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:615) through 775 and 796–844. Its FO and complexity theorems are **cited**, and its strict/inclusive grammar bridge is explicit. Those labels do not promise that every source proof has been expanded locally.

The active Part VIII Kamp definition/theorem was read at [handbook/parts/p08/temporal-epistemic-supplement.tex:408](C:/Dev/the-methods-of-reason/handbook/parts/p08/temporal-epistemic-supplement.tex:408) through 448. The LTL card, ordinary Büchi type, complete Hilbert LTL sheet and full inherited infinite-word semantics were also read. The active sheet's validity proof standing remains a sketch; N12 does not make the historical Pnueli or GPSS presentations interchangeable with it.

## Remaining writing and verification obligations

1. **An actual substantial construction absent locally:** Kamp's Chapter III reverse construction is reduced to a theorem/lemma roadmap. If full presentation of that source proof is required, III.1/III.2 and the load-bearing lemmas are a precise bounded authoring target. This does not imply reproducing the entire thesis.
2. **A partly condensed complexity development:** the Sistla–Clarke extraction, computation-history and periodic-model proofs need a source comparison to distinguish source-sketch boundaries from source-supplied proofs currently summarized in the book.
3. **An explicit missing variant:** epsilon-emitting ETL grammars are outside the current reconstruction. Any extension must supply the omitted cases and adjust the proof; otherwise its stated scope must remain.
4. **Unresolved historical claims:** Pnueli's adequacy/embedding assertions and GPSS's unprinted constructions are accurately identified as unresolved/source-only. They cannot be used as accepted mathematical bridges. Merely recording those source limits is not itself a proof omission that mandates inventing a corrected source system.
5. **Source and proof acceptance:** this task did not re-read primary PDFs or independently certify every proof. External theorem citations, source sketches, private communications and supplied supplements retain distinct identities.

The report therefore records full text coverage, substantial coverage of the original topic list, and specific incomplete constructions. It leaves whole N-c-012 completion unverified.

## Complete heading ledger

| Line | Actual heading |
|---:|---|
| 3 | Temporal expressiveness, complexity, safety, and liveness |
| 6 | Kamp's 1968 thesis presentation |
| 8 | Source and rights boundary. |
| 16 | The four source classes of orders. |
| 42 | First-order standing and the current-point assignment. |
| 74 | The temporal language and its exact argument order. |
| 100 | The two translation directions. |
| 157 | Why the order hypothesis cannot be deleted. |
| 167 | The literal Chapter IV Theorem 3. |
| 233 | The sparse-square proof. |
| 343 | Adjacent separations and proof status. |
| 363 | Pnueli's 1977 transition system and proof systems |
| 365 | Source and program model. |
| 433 | Invariance and the source's temporal implication. |
| 480 | Invariant induction, ranks, and ER. |
| 678 | Sequential and concurrent applications. |
| 819 | The future-only tense presentation. |
| 1034 | Finite-state decision arguments. |
| 1123 | Appendix A proof ownership. |
| 1154 | Appendix B decision boundary. |
| 1203 | The GPSS presentation of fairness and expressive completeness |
| 1205 | Published source and rights boundary. |
| 1216 | The source model and the strict-operator convention. |
| 1319 | Program executions, correctness, and three strengths of response. |
| 1414 | Why strict until is used. |
| 1477 | First-order comparison and four distinct result domains. |
| 1545 | What the proof outline actually contains. |
| 1651 | The printed systems \(DX\) and \(DUX\). |
| 1778 | The final convention warning and proof ownership. |
| 1840 | Sistla--Clarke's operator-sensitive complexity boundary |
| 1842 | Journal source and repaired version boundary. |
| 1867 | Source languages and inclusive temporal clauses. |
| 1936 | The two decision problems and the path quantifier. |
| 1976 | Why \(L(F)\) has a linear small structure. |
| 2247 | The PSPACE proof chain for the richer bases. |
| 2468 | The repaired regular-operator extension. |
| 2639 | The source's complete classification table. |
| 2672 | Alpern--Schneider's semantic decomposition |
| 2716 | Safety and liveness. |
| 2771 | Why two stricter liveness notions are not synonyms. |
| 2870 | Neither is a dichotomy. |
| 2880 | Prefix topology. |
| 2901 | Theorem 1: every property has a safety--liveness decomposition. |
| 2951 | Theorem 2: two liveness factors. |
| 2978 | The printed Corollary 2.1 requires repair. |
| 3013 | Boolean closure. |
| 3033 | Source and proof boundary. |
| 3047 | Boundary among the five presentations. |

## Result and proof ledger

| Lines | Result / presentation | Current proof standing |
|---|---|---|
| 100–131 | Kamp R2 | Explicit forward translation and induction rationale; does not need linearity or completeness. |
| 133–155 | Kamp III.1/III.2, II.1/II.2 | Source construction summarized, including essential cut/interval hypotheses; no full local Lemmas1–10 derivation or primitive-recursive algorithm. |
| 157–165 | Kamp IV.5 | Rational-cut separator described; actual predicate interpretations and structural proof not supplied here. |
| 167–341 | Kamp IV.3 | Integer tenses, fixed sparse-square interpretation and full corrected same-parity induction supplied. |
| 343–361 | Kamp IV.1/IV.2/IV.4 | Adjacent nonexpressibility/positive expressibility theorems summarized with source proof shapes. |
| 480–489 | Pnueli P1 | Reachable-state induction rule displayed, later instantiated with explicit annotation obligations. |
| 543–666 | Pnueli ER A1/A2/R1–R4/I and Theorem1 | All displayed rules typed, metarule stated; source completeness sketch recorded with assertion-language/finite-branching assumptions; unreachable-state and nonserial counterexamples expose missing steps. |
| 678–817 | Pnueli sequential/concurrent attachments and producer–consumer example | Explicit typed full/partial attachments and invariant consequences; indicator support sets are source-unprinted, so preservation of all source invariants is not reconstructed. |
| 819–900 | Pnueli future calculus and Theorem2 | Full propositional G1–G3/RT/RG/MP and Q1–Q4 strengths displayed. Quantified schema range/domain semantics unresolved; completeness/decidability are cited modification argument, with model-class discussion following. |
| 900–928 | Pnueli Theorem2 model-class boundary | Supplied linearity-valid formula and three-state S4 countermodel show referral does not prove completeness for linear-execution semantics. |
| 930–1032 | Pnueli I1/I2/E/N, DI/DN and Theorem3 | All typed source forms displayed; fairness scope and counterexample supplied. DI/DN identified as derived strengthenings, individual derivations not supplied. ER embedding/relative-completeness source claim unresolved for pure K_b. |
| 1034–1121 | Pnueli Theorems4–5 / finite-system calculus | Supplied cyclic-SCC all-actions criterion and two-direction proof with reachable pruning; P/MRG displayed. General derivation-from-validity for Theorem5 is source assertion only. |
| 1123–1152 | Pnueli AppendixA | T2/T3 and corollaries cited externally; distinct six-step local eventuality inference proof supplied. |
| 1154–1200 | Pnueli AppendixB | Exact language recursion and inclusion route; no source proper-execution acceptor tuple/construction/proof, closure/inclusion delegated to external sources. |
| 1216–1317 | GPSS strict-operator bridge | Source convention plus explicitly supplied F-direction/endpoint/past-dual repairs and strict/inclusive identities. |
| 1319–1475 | GPSS response/fairness and precedence | Exact source formula families and semantic explanation; scheduling implementability assertions cited, U nondefinability reduction absent. |
| 1477–1543 | GPSS Theorems2.1/2.2/2.3/2.5 | Four exact domain packages stated and explicit forward translation supplied. Reverse results/source gap operators remain source assertions. |
| 1545–1649 | GPSS Lemma1, Main Lemma and Proposition2.4 | Actual Bet/At/Aft/Bef, special/decomposition formula classes reproduced; complement/event-expression translations are source outline with omitted core. External SS/G2 manuscripts not imported. |
| 1651–1776 | GPSS DX/DUX Theorems3.1/3.2 | All source axiom/rule schemata displayed; canonical sets/relations/quotient/path/truth-lemma outline recorded. Soundness proof, maximal extension, relation lemmas, fair threading and truth induction not supplied; no decision complexity bound. |
| 1778–1838 | GPSS D0X/D0UX | All transformed schemes displayed; completeness only transformation/source claim. U0 definition/recursion conflict exhibited and not adopted as coherent semantics. |
| 1976–2116 | Sistla–Clarke Lemmas3.1–3.3 / Theorem3.4 | Exact ambient subsequence measures and preservation hypotheses recorded; source strict-sign defects identified and corrected to non-strict bounds. Main small-model theorem expressly a source sketch; full extraction induction not supplied. |
| 2118–2245 | Sistla–Clarke Theorems3.5/3.7 and Lemma3.6 | Diamond hardness outline and explicit occurrence-sensitive NP certificate with local truth-induction rationale/cycle correction; finite extraction lemma stated, not fully proved. |
| 2247–2318 | Sistla–Clarke Theorem4.1, Lemmas4.2–4.4 | Graph-truth-to-satisfiability formulas displayed; stuttering lemma asserted; Turing computation hardness described without full encoding clauses. Exact journal 2S(n) count distinguished. |
| 2320–2398 | Sistla–Clarke Lemmas4.5–4.6 | Exact deletion and periodicity hypotheses/conclusions; deletion source proof is only an induction statement, repetition proof not expanded. |
| 2400–2466 | Sistla–Clarke Theorem4.7 and Theorem4.1 upper bound | Exact exponential prefix/period plus truth/witness conditions; one-step guessed-type checks and loop obligation algorithm displayed. Main periodic inductions summarized, source abbreviations explicit; Savitch cited. |
| 2468–2637 | Sistla–Clarke ETL Lemmas5.1/5.2 and Theorems5.3/5.4 | Grammar/continuation-tree/fulfilment types, positive and negated layer checks supplied; periodic semantic inductions stated/summarized. Nonempty emissions only; epsilon extension unestablished. |
| 2639–2670 | Sistla–Clarke TableI | All source satisfiability/validity/existential-truth fragment rows displayed; L(U,X) inclusion argument given. |
| 2672–2769 | Alpern–Schneider safety/liveness definitions | Exact full-space finite-prefix semantics with nonempty-state repair and stuttering distinction. |
| 2771–2868 | Uniform/absolute liveness and strict separations | Implications and two explicit separating examples proved; leads-to degenerate hypotheses supplied and necessity discussed. |
| 2870–2878 | Safety/liveness neither-class examples | Source until and total-correctness examples described semantically; no universal claim that every parameter choice is neither class. |
| 2880–2899 | Safety iff closed; liveness iff dense | Supplied two-direction proofs. |
| 2901–2943 | Alpern–Schneider Theorem1 and Corollary1.1 | Full closure-factor proof and explicit notation-closure deduction; no syntactic expressibility inferred without hypotheses. |
| 2951–2976 | Alpern–Schneider Theorem2 | Full disjoint dense eventual-constant factor construction, singleton countercase, nonclosure under intersection. |
| 2978–3011 | Alpern–Schneider Corollary2.1 | Correct union-closure hypothesis and proof supplied; explicit finite denotation-family counterexample refutes printed intersection-only claim. |
| 3013–3031 | Safety/liveness Boolean closure table | Semantic closure explanations and exact scope; not syntax closure. |

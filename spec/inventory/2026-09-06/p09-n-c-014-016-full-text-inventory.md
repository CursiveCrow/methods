# N-c-014 and N-c-016: complete sequential text inventory

Both assigned files have been read in full: **4,091 lines**, across 13 numbered, non-truncated intervals. The active texts supply extensive definitions, constructions, examples and selected proofs. They also retain exact source-sketch boundaries and three significant registered-source gaps: Büchi's 1960 journal reconciliation, Thomas's 1997 chapter, and the Clarke–Grumberg–Peled 1999 first-edition presentation.

This completes the assigned inventory. It does not certify every mathematical proof independently or establish full source-presentation completion. Current corrected constructions were read directly; earlier defects already corrected are not reopened.

## Coverage and active routes

| File | Lines / bytes | Sequential intervals |
|---|---:|---|
| [N-c-014](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-014.tex:1) | 1924 / 89527 | 1–350, 351–700, 701–1050, 1051–1400, 1401–1750, 1751–1924 |
| [N-c-016](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-016.tex:1) | 2167 / 95372 | 1–250, 251–600, 601–950, 951–1300, 1301–1650, 1651–2000, 2001–2167 |

- N-c-014 SHA256: `FD2B17EC24D4E7AD48D69CDFF593D5ADFF1154A443FCFA3F45E5D47034DE0A3F`.
- N-c-016 SHA256: `5D555CEF1EDD60F641EB16461315276F0D574AACAEAE8710F03763DC5DD7C056`.
- Both hashes were unchanged through the initial, interval and final readings. No gaps, overlaps or truncated read outputs occurred. Next unread line for each file: **none**.
- Finalized: 2026-09-07 09:42:11 UTC.
- Active routes: [handbook/main.tex:33](C:/Dev/the-methods-of-reason/handbook/main.tex:33) → [handbook/parts/p09.tex:3](C:/Dev/the-methods-of-reason/handbook/parts/p09.tex:3) → [N14 input](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:952) and [N16 input](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:1534).
- The JSON accounts for 60 headings, 47 result/construction entries, all seven explicit cross-references, and five bounded dependency readings.

Headings and references were extracted after the sequential reading. No primary PDF was re-read or acquired; source-identity claims below describe the actual manuscript/bibliography scope. Only these two assigned audit outputs were written. No manuscript, register or bibliography changes, tests, builds or renders occurred.

## Original requirements

[N-c-014](C:/Dev/the-methods-of-reason/spec/registers/new-content.csv:121) names finite-word Büchi–Elgot–Trakhtenbrot, S1S decidability and Rabin's S2S statement. Its sources are Büchi 1960, Elgot 1961, Trakhtenbrot 1961, Rabin 1969 and Thomas 1997. Its original T treatment and “Rabin's proof out of scope; statement and applications” note are historical fields, not current completion ceilings.

[N-c-016](C:/Dev/the-methods-of-reason/spec/registers/new-content.csv:123) requests CTL/CTL* syntax and semantics, EG/EU fixed points, the labelling algorithm with complexity and correctness, and LTL/CTL expressiveness. Its sources are Clarke–Emerson, Queille–Sifakis, Emerson–Halpern, Clarke–Grumberg–Peled 1999 and Baier–Katoen. [D-P10-009](C:/Dev/the-methods-of-reason/spec/registers/depth-gaps.csv:93) targets **P8.3 entry cards**; it is not an additional P9 proof row.

## N-c-014: source presentations

| Actual lines | Source presentation | Current text/proof standing |
|---|---|---|
| [6–271](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-014.tex:6) | Büchi's 1959 UMR1083 report; later binary-arithmetic supplement | Exact weak arithmetic, finite propositional automaton, special output and marker coding. Synthesis is an outline; analysis and arithmetic translations have supplied arguments. Registered 1960 journal reconciliation explicitly remains open. |
| [273–614](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-014.tex:273) | Elgot 1961, with 1959 precursor and 1962 errata | Exact admissible coding and translation architecture; finite behavior/synthesis; supplied extendability kernel and infinite window/tag construction. Some normal-form, selection and negative proofs remain summarized or cited. |
| [616–1046](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-014.tex:616) | Trakhtenbrot 1961 announcement and 1962 expansion | Distinct source systems, terminology and portion conventions; anticipation/memory, topology, definability and synthesis. Corrected residual-degree proof is supplied; general realization and synthesis proofs are partly summarized. Conditional algorithms retain their conditions. |
| [1048–1120](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-014.tex:1048) | Thomas's modern finite-word route | Precise finite-word structure, NFA and MSO0 architecture with empty-word guard. Atomic automata and complete normal-form construction are summarized. This uses the 1996 report, not the registered 1997 chapter. |
| [1122–1727](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-014.tex:1122) | Rabin 1969 | Exact successor structures, ordinary and dual acceptance, tracks, product, finite-frontier objects, complementation architecture, emptiness recursion and applications. Supplied zero/no-run repairs are incorporated; the full original complement development is explicitly left in the source. |
| [1729–1924](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-014.tex:1729) | Thomas's later tree/game route | Muller/chain/game definitions and source proof route; supplied empty-chain and rejecting-sink completion. Game determinacy and some automaton constructions are summarized. Its later basis route is not attributed to Rabin. |

### Finite-word and synthesis details

Büchi's automaton uses finite propositional transition data but an actual run over all time. [Lines 109–128](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-014.tex:109) quantify a finite run witness only through a finite boundary; the special-output identity propagates the accepted false-input tail. This current construction addresses the finite-predicate boundary rather than mistakenly quantifying the entire run as finite.

Elgot's admissible finite-set codes require projection followed by removal of trailing zero columns. The reverse direction records run states after consuming letters and handles the empty word separately. [Lines 425–487](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-014.tex:425) supply an explicit descending extendability kernel, empty-prefix tests and maximality proof. The infinite synthesis reduction treats fixed initial numerals, moving windows, disjoint tags and the unary-window case. These are present constructions, not merely named procedures.

Trakhtenbrot's all-prefix portions include the empty portion. The current exact graph degree at [766–842](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-014.tex:766) is the number of residual maps plus the empty-portion indicator. The explicit example has whole-future memory weight two and degree four; that difference is explained rather than equating the quantities. The source's general-solution and conditional-emptiness qualifications remain intact.

### Rabin and the later Thomas route

Rabin's ordinary acceptance is `exists run, for every path`, using a Muller family. Dual acceptance is `for every run, exists path`, using its distinct pair sequence and permitting vacuity when no run exists. The finite-frontier automaton and the finite table-run used in emptiness have different codomains and terminal behavior.

The current text already supplies the following cases:

- [1439–1462](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-014.tex:1439): an empty dual pair list is represented by one impossible pair, so the positive-length induction can be entered.
- [1652–1697](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-014.tex:1652): the recursive emptiness test includes empty H and empty U0, covering no-run and vacuous dual branches.
- [1768–1824](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-014.tex:1768): Thomas's chain can be empty, and partial transitions are completed with a rejecting sink before applying a theorem for games with moves everywhere.
- [1166–1174](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-014.tex:1166): the incorrect elementary-recursive complexity claim is expressly not retained; decidability and the later non-elementary lower-bound citation are separated.

The remaining core boundary is equally explicit: [1720–1727](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-014.tex:1720) says that every transition table and induction inside Rabin's fourteen-page complementation development is not reproduced. The account is a substantial architecture with several exact constructions, not the entire original proof.

### S1S is located outside this file

The original S1S requirement is routed through [thm:p09-s1s](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:866) and N13's Büchi 1962 presentation. I read N13's actual source/type passage at [handbook/parts/p09/presentations/n-c-013.tex:514](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-013.tex:514), normal-form/decision material at 762–821, and source-proof boundary at 910–920. The full-set SC formalism and finite stem–cycle decision are therefore located; they are not confused with N14's weak finite-set arithmetic. This bounded interface reading is not a second full N13 inventory or acceptance of all its intervening lemmas.

## N-c-016: source presentations

| Actual lines | Source presentation | Current text/proof standing |
|---|---|---|
| [6–511](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-016.tex:6) | Clarke–Emerson published paper, through the authorized 2008 reprint | Indexed CTL, labelling, quadratic source bound, SCC result and Hamiltonian-path hardness proof. Tableau remains the published outline; exact typed factorization and mutual-exclusion requirements are supplied. Longer manuscript is distinct. |
| [513–914](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-016.tex:513) | Queille–Sifakis 1982 CESAR | IPN/program predicates, maximal-path semantics with sinks, all property families, four transformer equations and one complete protocol calculation. Proposition proofs are delegated to Sifakis 1979; translation/reduction proofs and general convergence theorem are absent. |
| [916–1608](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-016.tex:916) | Emerson–Halpern 1986 | Exact path classes, typed CTL*, expressiveness map and witness families. Full current R-generability and MPL translation proofs; several separating inductions and external elimination results remain summarized/cited. |
| [1610–1631](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-016.tex:1610) | Clarke–Grumberg–Peled 1999 | First-edition acquisition/metadata boundary only; technical presentation explicitly absent. The old access report is dated 22 August 2026 and is not a new claim of current unavailability. |
| [1633–2167](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-016.tex:1633) | Baier–Katoen 2008 | Source TS/CTL/CTL* conventions; explicit host bridge; satisfaction-set proofs, Algorithms 13–16, global induction, source graph and complexity. ENF and expressiveness omissions retain their source standing. |

### Corrections actually present

The Clarke–Emerson until recurrence includes its left-operand guard. Its factorization at [441–497](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-016.tex:441) gives every auxiliary variable a total value, initializes it even at nodes with no incoming edge, assigns target values, requires preservation of other-process regions, and merges only arcs with the same complete update. Earlier omissions of these conditions are not current findings.

CESAR's executions now have start and adjacency conditions and evaluate formulas only at actual positions, excluding the fictitious post-terminal state. Empty action-family conventions and the receiveack identifier are explicit. These formulas still concern possible future enabledness rather than occurrence or an implicit fairness assumption.

The Emerson–Halpern Theorem 5 witness is now [A[F(P and XP)]](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-016.tex:1287), consistent with the P,P,not-P and P,not-P base chains. The recursive graph and the first separating invariant are supplied. Its bounded-size indistinguishability induction and cited Boolean-path elimination are still proof dependencies; correcting the witness does not supply those omitted arguments.

[Lines 1034–1075](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-016.tex:1034) give the full R-generability equivalence with state completeness and the explicit dependent-choice qualification. [Lines 1443–1573](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-016.tex:1443) give the operative MPL until/next clauses and complete simultaneous translation proof, including finite endpoints, empty initial prefix, suffix closure and fusion. These are current supplied proofs.

The Baier–Katoen bridge distinguishes action-labelled triples from binary edges, handles empty S/I cases and translates the exact source syntax. The current source graph and formulas incorporate the listed local source corrections. Its nonuniform succinctness caveat is expressly not promoted to a P=NP theorem.

### The required CTL labelling proof is present

The active [CTL method](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:984) and [paired theorem](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:1019) were read with the entire [annex:p9.ctl.1](C:/Dev/the-methods-of-reason/handbook/annex/p09/proofs.tex:86) at lines 86–122. The annex supplies structural truth induction, existential/universal until stage arguments, EG/AG characterizations and the worklist/edge bound.

N16 also supplies the Baier–Katoen set proofs and global algorithm induction at [1831–1948](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-016.tex:1831), exact graph calculations and linear complexity accounting. The original request for the finite total-state algorithm and its correctness is substantively present. This is distinct from CESAR's image-finite propositions, CTL satisfiability, or general CTL* complexity, whose separate citations remain visible.

## Remaining obligations

1. **Exact registered editions:** Büchi 1960 and Thomas 1997 are not established by their currently presented report precursors. N14 explicitly retains both version gaps.
2. **Missing registered book presentation:** N16's Clarke–Grumberg–Peled 1999 technical content is absent. Other source presentations supply mathematics but do not close that source-specific requirement.
3. **Original proof expansions:** Rabin's full complementation transitions/inductions and several Trakhtenbrot/Elgot constructions are partly condensed. A source comparison must select any required full-compendium expansions; historical treatment limits are not completion evidence.
4. **Expressiveness proofs:** N16's corrected model statements still leave some bounded-formula/interleaving inductions and cited elimination/separation results unexpanded. Some were omitted or sketched by the source itself. Their absence does not automatically make the source presentation defective.
5. **Independent verification:** all current contents and boundaries are inventoried; no whole-proof acceptance or fresh held-source identity certification was performed.

## N-c-014 heading ledger

| Line | Actual heading |
|---:|---|
| 3 | Finite-word monadic logic and Rabin's infinite-tree theorem |
| 6 | The three original predicate-and-automata presentations |
| 18 | The source's weak second-order arithmetic. |
| 31 | The source automaton and its behavior. |
| 73 | Synthesis and analysis. |
| 130 | The source's finite-word encoding. |
| 158 | The decision proof and arithmetic consequences. |
| 180 | Binary arithmetic and finite-set arithmetic. |
| 273 | Elgot's controlling text and source automaton. |
| 300 | Finite-set arithmetic as a regular language. |
| 396 | Automaton design and finite-behavior synthesis. |
| 497 | The infinite synthesis reduction. |
| 601 | Elgot's negative boundary. |
| 616 | Trakhtenbrot's two source bodies and formal system. |
| 679 | Anticipation, memory, and finite operators. |
| 734 | Portions, homogeneity, and definability. |
| 900 | Finite realization. |
| 960 | Explicit synthesis and the finite-word boundary. |
| 1122 | Rabin's successor structures and ordinary tree automata |
| 1239 | Formula tracks and both definability directions |
| 1335 | Theorem 3.1 and its product construction |
| 1389 | Dual acceptance and complementation |
| 1439 | Handbook-owned zero-length completion. |
| 1573 | Rabin's actual emptiness argument |
| 1699 | Applications, later route, and proof boundary |

## N-c-016 heading ledger

| Line | Actual heading |
|---:|---|
| 3 | CTL, CTL*, and state-labelling model checking presentations |
| 6 | Clarke--Emerson's branching-time synthesis presentation |
| 20 | The program abstraction and its semantic structure. |
| 62 | The source's CTL syntax and semantics. |
| 126 | The finite-state model checker. |
| 236 | What the satisfiability section actually supplies. |
| 320 | Synthesis and the mutual-exclusion derivation. |
| 513 | Queille--Sifakis's CESAR presentation |
| 525 | CESAR's program model and its exact output claim. |
| 599 | The literal branching-time language. |
| 665 | Program predicates and the complete property families. |
| 787 | The four fixed-point calculations. |
| 851 | What the analyzer actually computes. |
| 916 | Emerson--Halpern's typed CTL* and expressiveness presentation |
| 927 | Why one untyped temporal syntax is not enough. |
| 1006 | The structure classes used by the comparison. |
| 1077 | The two formula types of CTL*. |
| 1171 | From whole-model validity to formula equivalence. |
| 1225 | The exact expressiveness map. |
| 1287 | The separating model families. |
| 1407 | What the comparison says about specifications. |
| 1420 | The PL translation and its proof boundary. |
| 1443 | The MPL semantics and translation. |
| 1582 | The terminal-server example and the scope of the conclusion. |
| 1610 | Clarke--Grumberg--Peled's 1999 acquisition boundary |
| 1633 | Baier--Katoen's CTL labelling presentation |
| 1644 | Inherited transition systems and paths. |
| 1746 | Typed CTL syntax and semantics. |
| 1815 | Existential normal form and the translation boundary. |
| 1831 | Satisfaction sets and their proof. |
| 1950 | The source's worked graph. |
| 2001 | Exact complexity claim. |
| 2078 | CTL versus LTL: the actual witness systems. |
| 2115 | CTL* typing, embedding, and strictness. |
| 2152 | Printed defects and proof boundary. |

## Result and construction ledger

Proof labels describe the actual written standing; a local proof label here records a supplied argument rather than independent acceptance.

| File / lines | Result or construction | Standing |
|---|---|---|
| N14 73–128 | Buchi Lemma1/Theorems1–2 | mixed — Normal form and synthesis closure outlined; analysis has explicit finite run/prefix witness and both-direction argument. |
| N14 130–178 | Buchi Theorems3/6–8, Corollaries1–2 | mixed — Marker-based string behavior/logic correspondence and ultimate periodicity stated; sentence decision finite reachability argument supplied. |
| N14 180–271 | Binary arithmetic and finite-set arithmetic | local_proof — Effective two-way bit/power/carry translations and canonical regular-language encoding argument; later source citation distinguished. |
| N14 300–394 | Elgot Theorem5.3/Lemmas5.4–5.5/Corollary5.8/arithmetic | mixed — Exact admissible code, logical closure with coordinate deletion plus zero trimming; reverse run-state labeling; fuller local pattern/normal-form proofs summarized; arithmetic consequences cited. |
| N14 396–495 | Elgot Theorems7.1/7.3/8.1 and Lemma6.1/6.5 | mixed — Finite/infinite behavior characterizations; explicit largest extendable language kernel and maximality proof; lexical uniformization regularity cited. |
| N14 497–599 | Elgot §8.6 infinite synthesis reduction | local_proof — Bounded-window finite union, numerator/initial columns, tag projection and unary-to-binary conversion supplied; ultimate synthesis relies on preceding finite result. |
| N14 601–614 | Elgot Lemma10.1/Theorem10.2/Corollary10.6 | cited_only — Undecidability and synthesis boundary summarized, Post-system reduction not reproduced. |
| N14 628–677 | Trakhtenbrot announcement Theorem1 / expanded §1.4 | source_sketch — Exact upper/lower t-formula domains and source normal-form algorithm roadmap. |
| N14 679–732 | Memory/anticipation/finite operators and undecidability | mixed — Types and distinctions explicit; primitive-recursive synthesis negative result cited. |
| N14 734–846 | Closed graph and exact residual degree | local_proof — All-prefix portion convention, deg(G_T)=\|R_T\|+epsilon_T with full proof and corrected two-state-weight/four-portion counterexample. Whole-future memory weight not equated to residual count. |
| N14 848–898 | Trakhtenbrot Theorems2–3 / closed homogeneous sets | mixed — Definable homogeneity and effective portions summarized; recurrence/choice-stream image construction including empty set supplied; conditional emptiness oracle retained. |
| N14 900–958 | Finite realization, Theorems4/4'/5 and expanded fixed-lookahead theorem | source_sketch — Exact continuity/closedness/solution-class/weight hypotheses and all-only parametrization; deletion proof roadmap, not complete implementation. |
| N14 960–1038 | Explicit synthesis and finite-word recognition | mixed — Source explicit recurrence construction summarized, two-state worked source table merely referenced; typed induced word maps and nonempty/prefix/extension conditions spelled out. |
| N14 1048–1120 | Thomas Theorem3.1 | source_sketch — Finite-word MSO/NFA translation architecture and empty-word/WS1S boundaries; atomic automata not individually tabulated. |
| N14 1155–1177 | Rabin Theorems1.1/1.12 | cited_only — Decidability S2S and interpretation SωS; source elementary complexity refuted by later Meyer/Stockmeyer lower bound. |
| N14 1230–1237 | Rabin Lemma1.2/Theorems1.3–1.6 | mixed — Normalization, Boolean/projection closures and difficult complement/emptiness statements with later source proof route. |
| N14 1239–1333 | Rabin Theorems1.7/1.10 and Corollary1.11 | mixed — Characteristic tracks, principal formulas, finite frontier witness and reverse run/path coding; exact source formula not fully expanded; decision depends on complement/emptiness. |
| N14 1335–1387 | Rabin Theorem3.1 | local_proof — Explicit U×S product, move table and Muller family; coherence follows from deterministic word automaton; McNaughton equivalence cited. |
| N14 1389–1506 | Rabin dual acceptance/Lemmas3.2–3.11/complementation | mixed — Exact dual pairs and quantifier order, supplied k=0 normalization; marked-tree/ordinal/two-half-step development is source architecture, not full local transition and induction construction. |
| N14 1508–1571 | Rabin finite-tree Lemmas3.12–3.15 | mixed — Exact frontiered objects and external-f transition codomain (mixed frontier/state child has no run); lift and universal hitting lemmas cited with roles; transfinite locus precise. |
| N14 1573–1697 | Rabin Theorem1.6 emptiness | mixed — One-letter/complement/dual reduction, restricted-table root convention and finite-table runs; k=0, empty H and empty U0 corrections incorporated; relies on unexpanded Rabin lemma chain and external weak finite-tree theorem. |
| N14 1699–1727 | Rabin ChapterII applications | cited_only — Countable orders/functions, Cantor/F_sigma, Boolean algebras/ideals, determinacy applications summarized without all interpretations. |
| N14 1729–1924 | Thomas Theorems6.5/6.8/6.9/6.13/6.16/6.18–6.20 | mixed — Muller/chain/game definitions, explicit rejecting-sink proof and empty-chain base; determinacy/complement/basis/logic constructions summarized with source theorem dependencies rather than all underlying proofs. |
| N16 126–197 | Clarke–Emerson finite CTL labelling | local_proof — Correct guarded universal/existential recurrences, finite argument and source quadratic bound; source missing guard already repaired. |
| N16 199–234 | Clarke–Emerson Propositions4.1–4.2 | local_proof — Reachable positive accepting cycle criterion and exact Hamiltonian-path NP-hardness reduction, not NP-completeness. |
| N16 236–318 | Clarke–Emerson satisfiability tableau | source_sketch — Blocks closure and concrete Tiles example; general process-indexed tiles and full correctness theorem omitted in published outline. |
| N16 320–497 | Mutual exclusion and factorization | mixed — Nine source requirement groups and skeleton transitions; current total auxiliary domains/initialization/all-target updates, other-process preservation guard and update-class merging. No separate full general factorization correctness theorem. |
| N16 599–663 | CESAR POT/INEV/ALL/SOME semantics | not_applicable — Typed actual-position domains and completed start/adjacency clauses; not full CTL grammar. |
| N16 665–785 | CESAR program property families | mixed — Full invariant/live/deadlock/response instances and nullary conventions; receiveack identifier repaired; enabledness not occurrence/fairness. |
| N16 787–849 | Queille–Sifakis Propositions1–2 | cited_only — Four exact image-finite transformer equations; source delegates proofs to Sifakis1979, not supplied locally. |
| N16 851–914 | CESAR alternating-bit calculation | mixed — One-token invariants, predecessor expression and P1=true calculation; translation/pre preservation not proved; only one property fully calculated, no convergence theorem. |
| N16 927–1004 | Emerson–Halpern Lamport comparison Theorems1–2/Proposition1 | mixed — Typed shared glyph semantics and model-validity notions; separation proofs explicitly not reproduced. |
| N16 1006–1075 | R-generability characterization | local_proof — Full suffix/fusion/limit/state-completeness iff total-relation generation, both directions and dependent-choice qualification; missing state-completeness oldfinding already corrected. |
| N16 1077–1223 | CTL* formula types / Propositions2–4/Corollary1 | mixed — Exact state/path grammar, finite path conventions, fragments, modelwide-vs-pointwise comparisons; proofs largely source explanation. |
| N16 1225–1285 | Expressiveness map / Theorems3–4 | mixed — Exact chains/incomparabilities, full path-deletion separator for EFP; AppendixF/G embedding summarized, interleavings not fully displayed. |
| N16 1287–1368 | Emerson–Halpern Theorems5–6 | mixed — Correct F witness, base and recursive model graph, first invariant and reduction via Boolean-path elimination. Bounded-size EX/EU/AU induction referred to appendix, not expanded; Theorem6 family mostly summarized and source repeated induction left to reader. |
| N16 1370–1405 | Emerson–Halpern Theorems7–9 | mixed — Recurrent-P separator family/invariants summarized; Boolean path elimination and until/next separations explicitly cited from earlierworks with no local proofs. |
| N16 1420–1441 | PL Proposition5 | source_sketch — All translation clauses printed; structural induction referred to, not expanded. |
| N16 1443–1573 | MPL Lemmas1–2/Theorem10 | mixed — Current corrected until/next stage semantics and full simultaneous translation proof including finite endpoints, suffix/fusion, empty prefix; Lemma1 unwinding summarized with choice qualification. |
| N16 1575–1608 | TC comparison and terminal server | mixed — TC translation only expected in source, not supplied; serverformula and countermodel rationale explicit, no complexity/synthesis theorem. |
| N16 1644–1813 | Baier–Katoen TS/CTL bridge to host | local_proof — Action forgetting, valuation/glyph translation and semantic induction, S empty/I empty cases, binaryedge<=actiontriple count. |
| N16 1815–1829 | Baier–Katoen Theorem6.14 ENF | source_sketch — Universal-elimination rewrite outline; exponential growth warns against materializing ENF for original-formula linearbound. |
| N16 1831–1948 | Baier–Katoen Theorem6.23 / Algorithms13–16 | local_proof — Set characterizations, naive loops and optimized worklists/invariant, global satisfaction induction explicitly supplied. |
| N16 1950–1999 | Baier–Katoen Examples6.26–6.28 | local_proof — Exact eight-state labels/edges/start and both fixedpoint calculations. |
| N16 2001–2076 | Baier–Katoen Theorem6.30 / Example6.31 | mixed — Linear adjacency accounting and original modality handling; Hamiltonian permutation formula fully typed; uniformity gap in nonuniform succinctness argument explicitly not promoted. |
| N16 2078–2113 | Baier–Katoen Theorem6.21 | mixed — Exact FG witness base/recursive graphs, truth contrast; bounded-CTL induction left to reader. Reverse trace-deletion separator supplied; other theorem cited. |
| N16 2115–2167 | Baier–Katoen Theorems6.83–6.84 | mixed — CTL* grammar/semantics, LTL embedding and strictness substitution step supplied; depends on earlier partially supplied incomparable witnesses. |

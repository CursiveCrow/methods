# N-c-016 integrated source-fidelity review, Round 2

VERDICT: ACCEPT

## Bounded decision

At the assigned text-only strength, the complete 1,849-line presentation and the specified host integration have no line-specific source-fidelity must-fix. The five registered source states remain distinct; source text, reader reconstruction, source defects, and proof omissions are not collapsed; the access and rights claims stay within the supplied acquisition evidence; and no technical content is attributed to the unacquired Clarke--Grumberg--Peled 1999 body.

This verdict concerns only the actual LaTeX and permitted supporting text listed below. It is not a TeX-build, rendered-page, visual-layout, automated-check, independent historical-PDF, or unrestricted publication-rights verdict.

## Presentation-by-presentation audit

### N-c-016.a: Clarke--Emerson

The presentation at `handbook/parts/p09/presentations/n-c-016.tex` lines 3--464 is faithful to the source note at its published twenty-page strength.

- Lines 6--15 keep the 1981 meeting, 1982 LNCS publication, original pp. 52--71, 2008 reprint pp. 196--215, and separate 37-numbered-page manuscript state distinct. The longer manuscript is not treated as part of the published body.
- Lines 17--56 define the synchronization skeleton, semantic structure, computation tree, and global system flowgraph with distinct standings and uses. The skeleton is not promoted into a formula, semantic model, low-level synthesis result, or refinement theorem.
- Lines 58--120 preserve the source's process-indexed `EX_j` grammar, total union of process transitions, strong inclusive until, derived `V`, `AF/EF`, `AG/EG`, indexed `AX_i`, and unindexed `EX/AX`. They do not retrofit the source to a later unindexed CTL grammar.
- Lines 122--220 keep the finite-state labelling algorithm, guarded universal-until repair, reconstructed rather than source-displayed existential recurrence, worked graph, finite-context infinitely-often result, and Hamiltonian reduction at their exact scopes. Proposition 4.2 is reported as NP-hardness only for the arbitrary-linear-path-prefix extension.
- Lines 222--303 retain the tableau's expressly abridged status, the `Blocks`/`Tiles` source roles, the concrete tile calculation, the finite label-count argument, the worked satisfiable formula, the omitted full correctness proof, and the source's correction of the faulty `[BM81]` procedure.
- Lines 305--463 preserve all nine mutual-exclusion requirement groups, the nonvacuity role of `EX_i true`, model-fragment standing, `TURN` distinction, global-to-local factorization, and the provisional synthesis conclusion. The model-checker implementation is not reported as an implementation or proof of synthesis.

No published-body theorem, definition, appendix, bound, or figure is silently imported from the expanded manuscript.

### N-c-016.b: Queille--Sifakis

The presentation at lines 465--789 is faithful to the complete original chapter at the source note's explicitly qualified scan and reprint-access strength.

- Lines 468--475 state the fifteen-page original/reprint identity while preserving the unresolved distribution authorization of the complete scan and the lack of direct inspection of reprint pp. 218--230.
- Lines 477--523 give the interpreted-Petri-net standing, guarded assignments, rendezvous translation, safe-process-net claim, diagnostic-only output, and alternating-bit non-loss assumption without supplying an absent translation proof, counterexample format, synthesis procedure, or fairness clause.
- Lines 525--585 distinguish the literal unary branching-time language from later CTL, state the source's finite/infinite maximal-execution convention, and expressly assign the omitted start and adjacency clauses to the reader. The missing Boolean interpretation clauses remain recorded as omissions.
- Lines 587--689 preserve `Init`, `enable`, and `after` as program-derived atomic predicates, distinguish enabledness from occurrence, reproduce the invariant/liveness/deadlock/response families at their exact strengths, and repair `receivack` only in reader-facing notation while recording the printed defect.
- Lines 691--739 preserve the source's literal `h^x` notation, image-finiteness hypothesis, four predicate-transformer identities, sink behavior, and delegation of both proposition proofs to Sifakis 1979.
- Lines 741--788 keep the analyzer at outline strength, reproduce only its sole worked evaluation, state the user iteration-cap/no-answer boundary, and do not infer an asymptotic bound, total decision procedure, satisfiability calculus, or synthesis result.

### N-c-016.c: Emerson--Halpern

The presentation at lines 790--1344 is faithful to the complete 1986 JACM source state and keeps all material source defects and proof boundaries visible.

- Lines 793--799 distinguish the journal article from the POPL paper and 1984 reports and state the ACM rights boundary without claiming an open licence.
- Lines 801--902 preserve Lamport's two semantic typings, model-validity notion, strong-equivalence weakness, closure conditions, state completeness, `R`-generability, and the printed `X`/`S` type defect.
- Lines 904--995 give the mutually typed CTL* grammar and semantics, the all-sequences path-semantics footnote, exact named fragments, and the meaning of path-level Boolean closure. State and path formulae are not conflated.
- Lines 997--1070 preserve the distinction between whole-model and pointwise equivalence and reproduce the exact Figure 1 order, equality, strict edges, and incomparabilities over the stated structure class.
- Lines 1072--1213 keep Theorems 3--9 at their actual proof strengths. In particular, the self-defeating printed `B(L(...))` targets of Theorems 5--6, the Theorem 8(a)/Theorem 9 cross-reference defect, and the later Theorem 6/Theorem 7 dependency defect are all separated from the proof-and-diagram-supported readings.
- Lines 1225--1318 reproduce the PL translation and its unprinted induction, define the MPL stage with its correct standing, give the literal non-strict MPL `U/X` clauses and concrete counterexamples, and do not promote Theorem 10 or the expected TC translation beyond their source status.
- Lines 1320--1343 preserve the terminal-server example and present Section 6 as an application argument rather than a CTL labelling, complexity, or synthesis theorem.

### N-c-016.d: Clarke--Grumberg--Peled

Lines 1817--1849 are a source-boundary presentation only, which is exactly the permitted strength of the acquisition note.

- Lines 1829--1839 date and bound the audited-route result, distinguish public preview, restricted lending, institution-only access, physical-copy existence, and contents-only locators, and expressly deny that locator metadata supports algorithms, proofs, examples, or exact notation.
- Lines 1841--1846 keep the Clarke--Schlingloff chapter, Clarke--Grumberg--Long survey, 2018 second edition, and Baier--Katoen book separate from the unacquired 1999 first edition.
- Lines 1846--1849 attribute the four host complexity classifications to their independent cited sources, not to Clarke--Grumberg--Peled 1999.

No technical claim about the 1999 book body appears at source-content strength.

### N-c-016.e: Baier--Katoen

The presentation at lines 1345--1816 is faithful to the complete book source at the stated all-rights-reserved scholarly-use boundary.

- Lines 1348--1354 correct the page map and keep the copyright/source-use language bounded.
- Lines 1356--1425 preserve the book's action-labelled transition-system tuple, inherited successor/path definitions, empty-initial-set case, no-terminal-state hypothesis, and source transition count. The reader-supplied `R_0,V_0` bridge is explicitly defined, typed, and distinguished from source terminology; action-label erasure and the `|R_0| <= K` comparison are reader derivations.
- Lines 1427--1490 preserve the typed CTL grammar and semantics, strong inclusive until, existential normal form, rewrite-outline proof status, and exponential ENF-expansion warning.
- Lines 1492--1540 reproduce Theorem 6.23's exact least/greatest set conditions and identify the detailed nontrivial arguments separately from the clauses the book calls straightforward. The no-terminal-state condition remains a standing semantic hypothesis.
- Lines 1542--1609 distinguish naive Algorithm 14 from Algorithms 15--16, preserve both approximation directions, the count invariant, finiteness, and the reader-assembled global structural induction. The global induction is not attributed as a separately printed theorem proof.
- Lines 1611--1660 use the book's actual graph and final satisfaction sets. The reader's Boolean comparison abbreviations are eliminable, explicitly metalinguistic, and do not introduce a new state-variable sort.
- Lines 1662--1737 retain Theorem 6.30's finite/no-terminal, representation, direct-modality, and formula-size boundaries, state no separate space theorem, and distinguish the Hamiltonian example's succinctness argument from the model-checking theorem. The uniformity observation is expressly reader-owned.
- Lines 1739--1798 retain the exact CTL/LTL witness systems, omitted bounded-formula induction, omitted similar witness, proof-omitted Theorem 6.18 dependency, typed CTL* grammar, semantic LTL embedding, and one-sentence strictness proof. The atom-substitution completion is identified as the omitted elementary step, not source prose.
- Lines 1800--1815 record the source defects actually relevant to the reconstructed material and preserve the unequal proof strengths. No CTL* model-checking algorithm is inferred from the CTL* embedding or strictness results.

## Host integration

The host at `handbook/parts/p09/logic-in-computer-science.tex` lines 945--1023 and 1505--1507 is consistent with the permitted prerequisite and source evidence.

- Lines 948--967 reuse the Part VIII CTL/CTL* definitions and introduce only the two exactly defined predecessor maps needed by the algorithm. Their standing as state-set operations rather than path quantifiers is explicit.
- Lines 969--996 state the finite-total CTL labelling method using the Part VIII strong-until semantics. The least/greatest fixed-point directions and totality hypotheses agree with the presentation's Baier--Katoen bridge and with the host's own finite binary relation.
- Lines 998--1006 keep correctness and the `O((|S|+|R|)|A|)` bound as a handbook theorem with its annex proof marker; they are not falsely described as a verbatim theorem from any one historical source.
- Lines 1008--1015 state the LTL/CTL boundary at finite-total strength with typed state/path ownership intact. The Emerson--Halpern presentation supplies the underlying expressiveness map and proof-status qualifications; the Baier--Katoen presentation independently supplies the displayed witness-system pattern.
- Lines 1017--1023 cite the four decision bounds to `ClarkeEmersonSistla1986`, `EmersonLei1987`, `EmersonHalpern1985`, and `EmersonJutla1999`, whose permitted bibliography entries match the four distinct claims. Clarke--Grumberg--Peled 1999 is not cited for them.
- Lines 1505--1507 integrate the presentation once, after the preceding presentation input, without changing its source ownership.

## Technical-name rule

No must-fix violation of the supplied `AGENTS.md` rule remains.

- `synchronization skeleton` and `global system flowgraph` are necessary source distinctions with definitions, standings, nonredundancy, and later factorization use at lines 17--36 and 422--451.
- `Blocks`, `Tiles`, and `model fragment` are defined at the source's bounded strength, assigned metalinguistic/construction-artifact standings, distinguished from complete models, and used by the tableau/synthesis construction at lines 235--303 and 377--397.
- `interpreted Petri net`, `Init`, `enable`, `after`, and the predicate-transformer names are defined, typed, distinguished from formula operators/proofs, and used later at lines 477--503 and 587--776.
- Emerson--Halpern's `stage`, `basic formulas`, and associated-language constructor have exact source or metalinguistic standings and actual later proof use at lines 1008--1045, 1086--1109, and 1248--1311.
- Baier--Katoen's reader bridge `R_0,V_0`, the Boolean comparison abbreviations, and the host predecessor operations each state why the distinction is needed, give eliminable definitions, state their non-source or algorithmic standing, distinguish nearby terms, and are used by the later theorem or calculation at lines 1382--1412, 1634--1653, and host lines 948--965.
- The unacquired 1999 body is left as an owed source artifact rather than filled with hypothetical named machinery.

## Text evidence read

The following text was read in this review, and no unlisted substantive file was used:

- `handbook/parts/p09/presentations/n-c-016.tex`, lines 1--1849, complete through EOF.
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 945--1023 and 1505--1507.
- `spec/research/p09-clarke-emerson-1981-source-note.md`, lines 1--884, complete.
- `spec/research/p09-queille-sifakis-1982-source-note.md`, lines 1--867, complete.
- `spec/research/p09-emerson-halpern-1986-source-note.md`, lines 1--729, complete.
- `spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md`, lines 1--470, complete.
- `spec/research/p09-baier-katoen-2008-ch6-source-note.md`, lines 1--1120, complete.
- `spec/research/p09-source-presentations-lot2-3.md`, lines 781--847 only.
- `handbook/bib/handbook.bib`, lines 2393--2407, 2409--2422, 2424--2436, 2438--2447, 2449--2458, 4815--4824, 4826--4835, 4837--4846, and 4897--4906 only.
- `handbook/parts/p08/temporal-epistemic-supplement.tex`, lines 42--190 only.
- `spec/research/p08-new-content.md`, lines 810--830 only.

## Prohibitions observed

- No handbook/manuscript PDF, render, screenshot, or page image was opened or inspected.
- No historical publication file was opened; no ambiguity required the exceptional route.
- No TeX build, test, checker, automated validator, repository script, or executable was run.
- No hash was computed or verified. Hash strings occurring inside the permitted source notes were read only as existing text evidence.
- No N-c-016 Round 1 report or other N-c-016 review, board, admission, handoff, or review-history file was opened or used.
- No other agent was inspected, contacted, or delegated to.
- No web lookup or external source was used.
- No manuscript, host, source note, bibliography, register ledger, or collateral file was edited. The only written file is this assigned Round 2 report.

No repairs or optional improvements are proposed because no bounded-strength must-fix was found.

REGISTER STATUS: OPEN

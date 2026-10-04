VERDICT: REJECT

# N-c-016 Round 5 adversarial publication/terminology review

The frozen presentation is close to publication-ready on source boundaries, hierarchy, formula typing, proof-status voice, and host integration, but six line-specific defects remain.  The first two are not stylistic: together they make the stated general factorization fail to reproduce the source's own `TURN`-sensitive concrete skeleton.

## Must-fix findings

1. **Lines 452--476 omit the auxiliary source-state discriminator from every general factorization guard.**  Lines 443--452 make a duplicated global node label unique by adding a proposition \(z_{\Lambda}=r\), and lines 407--415 expressly say that the auxiliary value is used in the resulting enabling conditions.  The concrete \(P_1\) skeleton demonstrates the use at lines 427--429: entry from \(\mathsf{TRY}_1\) while the other process is trying is guarded by \(\mathsf{TURN}=1\).  Nevertheless, the generic global-arc pattern at lines 461--464 contains only the process-region components, and the guard generated at lines 465--476 is only \(S_1\land\cdots\land S_p\).  Two duplicate-labelled source nodes therefore produce the same generic guard even when their auxiliary values enable different local moves.  **Minimal repair:** extend each global source label in the factorization rule by the conjunction \(\Gamma\) of its auxiliary equality facts (with \(\Gamma=\mathit{true}\) when none occur), and generate the guard \(S_1\land\cdots\land S_p\land\Gamma\).  Show the target auxiliary value separately as the transition update; do not use a target assignment as a substitute for a source guard.

2. **Lines 458--478 collapse transitions with different update effects and then leave the copied update unassociated with its guard.**  Lines 465--476 form one disjunction from *all* global arcs having the same local endpoints, while line 478 says only to copy an assignment from “such a global arc” to “the corresponding skeleton transition.”  That is undefined when some contributing arcs have no auxiliary assignment or carry different assignments.  The presentation's own concrete case already has this shape: lines 422--426 display two parallel \(\mathsf{NCS}_1\to\mathsf{TRY}_1\) transitions, one without an assignment and one assigning \(\mathsf{TURN}:=2\).  Merging their guards and attaching the assignment unconditionally changes the transition relation.  **Minimal repair:** partition contributing global arcs by identical update vector, treating no update as an explicit no-op; create one (possibly parallel) skeleton transition per update class, and disjoin only the source guards within that class.  Equivalently, retain one guarded-command case per distinct guard/update pair.  This repair must be combined with finding 1 so that each retained guard includes its auxiliary source equality.

3. **Lines 1586--1602 assert the Baier--Katoen satisfaction-preservation bridge before defining the source satisfaction relation.**  The expression \(TS,s\models_{\mathrm{BK}}\Phi\) first appears at lines 1590--1592, but the source paths are presented only at lines 1608--1619 and the CTL satisfaction clauses only at lines 1621--1668.  Thus the semantic induction and host-method application occur before the semantics on which they depend.  The short constructor inventory at lines 1545--1567 defines the translation's syntax but does not define \(\models_{\mathrm{BK}}\).  **Minimal repair:** retain the structural definitions of \(R_0\), \(V_0\), \(\mathcal K_0\), and \(\operatorname{tr}\) where they are, but move the satisfaction equivalence and the host-method/complexity application now at lines 1586--1606 to immediately after the source semantic clauses ending at line 1668.  Moving the path and semantic paragraphs before the bridge would be equally sufficient.

4. **Line 1597 reuses \(L\) for the host satisfaction-set computation while \(L:S\to2^{AP}\) is still the declared source state-labelling function.**  The source declaration is at lines 1508--1512.  Under that local type, \(L(\operatorname{tr}(\Phi))\) is ill-typed because \(\operatorname{tr}(\Phi)\) is a formula, not a state; its intended meaning is recoverable only by importing the host method's unrelated \(L(A)\) notation through the cross-reference.  **Minimal repair:** in the relocated bridge from finding 3, avoid the collision by writing the method's returned set explicitly,
   \[
   \{s\in S:\mathcal K_0,s\models\operatorname{tr}(\Phi)\}
   =\{s\in S:TS,s\models_{\mathrm{BK}}\Phi\},
   \]
   or introduce an explicitly typed, distinct host-output symbol at that location.

5. **Line 971 uses the technical class name “suffix-closed” before its eliminable definition at lines 977--1008, specifically lines 991--992.**  The name is a substantive hypothesis of the quoted Theorems 1--2, not ordinary prose, and its path-set standing is unavailable at first use.  This violates the requested definition-before-use and same-location technical-name rule.  **Minimal repair:** move the structure-class paragraph (including the exact suffix-closure clause and its standing) before the summary of Definitions 1--2 and Theorems 1--2, or move the theorem summary to after line 1008.

6. **Line 1875 attributes the term “total transition system” to the Baier--Katoen example after lines 1520--1528 explicitly preserve that the source's Chapter 6 terminology is “without terminal states,” not a newly introduced “total transition system.”**  The example itself immediately explains that the added sink enforces the no-terminal-state hypothesis at lines 1889--1891, so the terminology switch is unnecessary and blurs the carefully stated source/host boundary.  **Minimal repair:** replace “the total transition system” with “the following transition system without terminal states” (or “the following transition system, made terminal-free by \(b\)”).

## Bounded positive evidence

- The subsection hierarchy is coherent: the encompassing subsection and its label are at lines 3--4, followed by five source-owned subsubsections at lines 6--7, 497--498, 896--897, 1470--1471, and 1493--1494.  The acquisition-only material remains confined to its own subsubsection.
- The Clarke--Emerson presentation distinguishes the 1981 meeting, 1982 publication, authorized reprint, and separate fuller manuscript at lines 9--18; it also separates the computation tree, global graph, per-process skeleton, model-checking algorithm, tableau outline, and worked synthesis construction.  The discriminator and update defects above are confined to the generic factorization rule, not the concrete `TURN` example.
- The Queille--Sifakis presentation preserves the scan-rights boundary at lines 500--507, gives the IPN's type and standing at lines 509--525, declares the message variables and every later-used action at lines 537--570, completes rather than silently attributes the source's execution-sequence omission at lines 600--643, defines the finite-family abbreviations at lines 655--681, disambiguates action and place symbols at lines 846--851, and retains image-finiteness and the delegated proof boundary at lines 807--829.
- The Emerson--Halpern section keeps the two formula standings distinct, records the literal Theorem 5--6 target defects before applying the proof-and-diagram-supported repair, preserves cited and reader-left proof steps, and states the unresolved MPL \(U/X\) conflict rather than presenting Theorem 10 as following from the printed clauses.  Finding 5 concerns only the first ordering of one class name.
- The Clarke--Grumberg--Peled subsection makes no formula, algorithm, proof, or complexity claim from the unavailable first-edition body.  Lines 1473--1491 limit it to access state, bibliographic/contents metadata, source-state distinctions, and independent host citations.
- Apart from findings 3--4, the Baier--Katoen bridge is materially well typed: lines 1530--1543 define the binary relation, valuation, their standings, and the alphabet identification; lines 1545--1573 give an eliminable constructor-by-constructor translation together with necessity, standing, nonredundancy, and later use; lines 1581--1586 handle the empty-state exception; and lines 1603--1606 distinguish binary edges from action-labelled transition triples.  The proof-source/handbook voice is also explicit at lines 1717--1734 and 1794--1803.
- The relevant bibliography entries preserve the publication years, identifiers, author identities, acquisition states, and rights limitations.  In particular, `ClarkeGrumbergPeled1999` records the suffix in `Clarke, Jr., Edmund M.` and names Peled rather than the defective publisher-page spelling.

## Technical-name rule audit

The principal reader-facing names that survive the rule have an actual need, an eliminable definition or stated source definition, a declared standing, a stated distinction from nearby objects, and later use: synchronization skeleton/global system flowgraph (lines 20--39 and 441--481), interpreted Petri net (lines 509--525), `enable`/`after` (lines 645--653), the finite-family abbreviations (lines 655--681), predicate-transformer operations (lines 767--829), CTL* state/path formula types (lines 1019--1111), the associated-language constructor \(B(L)\) (lines 1124--1131), MPL stage (lines 1370--1376), and the host bridge \(R_0,V_0,\operatorname{tr}\) (lines 1530--1573).  The first-use ordering failure for “suffix-closed” is isolated in finding 5.  The generic factorization's promised later use of auxiliary discrimination is incomplete in the two precise ways stated in findings 1--2.

## Substantive text read

- `handbook/parts/p09/presentations/n-c-016.tex`, lines 1--2021, through EOF.
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 930--1060 and 1485--1525.
- `handbook/parts/p08/temporal-epistemic-supplement.tex`, lines 42--190.
- `spec/research/p09-clarke-emerson-1981-source-note.md`, lines 1--884, through EOF.
- `spec/research/p09-queille-sifakis-1982-source-note.md`, lines 1--867, through EOF.
- `spec/research/p09-emerson-halpern-1986-source-note.md`, lines 1--729, through EOF.
- `spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md`, lines 1--470, through EOF.
- `spec/research/p09-baier-katoen-2008-ch6-source-note.md`, lines 1--1120, through EOF.
- `handbook/bib/handbook.bib`, lines 2393--2407, 2409--2422, 2424--2436, 2438--2447, 2449--2458, 4815--4824, 4826--4835, 4837--4846, and 4897--4906.

## Prohibitions observed and non-claims

- I did not open any N-c-016 review from any round, including my own earlier report; any source-fidelity or mathematical report; any board, admission, handoff, or history file; the parent conclusion; or any other agent output.  I did not contact or delegate to another agent.
- I did not inspect a PDF, render, screenshot, page image, or historical publication file, and I did not browse the web.
- I did not run a TeX/PDF/handbook build, test, checker, validator, repository script, hash, or executable source-analysis tool.  The evidence above was read directly as literal, line-numbered text.
- This verdict makes no page-layout, pagination-in-render, compilation, link-resolution-by-build, visual-quality, or manuscript-PDF claim.  It is confined to the frozen LaTeX text, the listed host/prerequisite text, the five controlling notes, and the listed bibliography entries.

REGISTER STATUS: OPEN

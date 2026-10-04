# N-c-016 Round 2 integrated publication and terminology review

VERDICT: REJECT

The frozen 1,849-line LaTeX snapshot is not yet publication-ready. The source-state, rights, citation, proof-status, and host-reference work is generally careful, but the following line-specific defects remain. Each repair below is deliberately local; none requires consulting or importing a prohibited source state.

## Must-fix findings

### 1. The published Clarke--Emerson account overstates the definition status of `Tiles`

**Lines 235--243 and 271--291.** Lines 235--243 call `Blocks` and `Tiles` “exact metalinguistic operations.” The ensuing text gives a closure account for `Blocks`, but for `Tiles` it gives only the source's one unindexed example and intended satisfiability relation. The permitted source note expressly records that the twenty-page publication does not print the general process-indexed clauses; those occur only in the separate fuller manuscript. Calling the two operations “exact” therefore overstates the published definition and fails the technical-name rule's exact-definition condition for `Tiles`.

**Minimal repair:** replace “two named successor operations are exact” with a source-state qualification: the publication names both successor constructions, defines `Blocks` to the stated closure strength, and illustrates rather than fully defines general `Tiles`. Confine `Tiles` to the printed example and intended satisfiability relation; do not import the fuller-manuscript clauses.

### 2. Two set-valued approximants are called states

**Lines 148--150.** (X_{\lvert S\rvert}) and (Y_{\lvert S\rvert}) were defined as subsets of (S), but the prose says they “are respectively the states satisfying” the formulas. This is a sort error in the reader-facing statement.

**Minimal repair:** write “are respectively the sets of states satisfying.”

### 3. The factorization prose has the wrong apparent quantifier

**Lines 435--446.** “The other-process conjunctions which occur on all such global arcs” naturally says that each conjunction occurs on every relevant arc. The displayed set comprehension instead takes the conjunction attached to each relevant arc and disjoins all resulting conditions.

**Minimal repair:** replace “which occur on all such global arcs” with “that occur on such global arcs” or “obtained from all such global arcs.”

### 4. The Clarke--Emerson conclusion conflates two distinct proof boundaries

**Lines 453--463.** The final status sentence calls the material “an explicitly abridged tableau/synthesis outline whose detailed correctness proof is elsewhere.” The permitted evidence supports only the statement that the published tableau decision procedure is an outline referring elsewhere for detail. The synthesis portion is a detailed worked construction with no separately numbered general synthesis-correctness theorem; the evidence does not establish that a detailed proof of that general synthesis claim exists elsewhere.

**Minimal repair:** split the last status into two: (i) an abridged tableau decision-procedure outline whose detail is referred to the full paper, and (ii) a worked synthesis/factorization construction for which this publication gives no separately stated general correctness theorem.

### 5. The Queille--Sifakis IPN is made finite too early

**Lines 480--490, especially line 488.** The IPN definition supplies a Petri net, program variables, guards, and assignments, but it does not itself restrict every variable domain to a finite set. Finiteness belongs to the later then-current implementation boundary for Boolean, enumerated, and bounded-integer variables at lines 781--783. Calling the IPN itself “the finite program model” strengthens the source definition and blurs model standing with implementation support.

**Minimal repair:** delete “finite” at line 488. Retain the finite Boolean-representation qualification only in the later implementation paragraph.

### 6. One Queille--Sifakis symbol is defined after it is used

**Lines 597--608.** (A(\mathcal P)) first appears in the display defining \(\operatorname{enable}\mathcal P\), and only afterward is said to be the finite action set of process \(\mathcal P\).

**Minimal repair:** move “write (A(\mathcal P)) for the finite set of actions belonging to process \(\mathcal P\)” before the display.

### 7. Emerson--Halpern's two equivalence relations are used without assigning the notation

**Lines 857--869 and 1008--1045, especially lines 1017--1024.** The prose distinguishes whole-model strong equivalence from pointwise state-formula equivalence, but it never tells the reader which of \(\equiv_s^{\mathcal F}\) and \(\equiv^{\mathcal F}\) denotes which relation before Proposition 4 uses both. The distinction is the proposition's content, so contextual inference is insufficient.

**Minimal repair:** immediately before Proposition 4, define \(p\equiv_s^{\mathcal C}q\) as the source's whole-model strong equivalence over structure class \(\mathcal C\), and \(p\equiv^{\mathcal C}q\) as pointwise state-formula equivalence over \(\mathcal C\). Then retain the displayed specialization to \(\mathcal F\).

### 8. The proof-local families (B) and (B^+) are named without an exact eliminable definition

**Lines 1091--1107.** The text introduces a “family of basic formulas” (B) and its Boolean closure (B^+), but replaces part of (B)'s actual definition with “a specified family of nested (F)-forms.” The same paragraph then uses the two names to describe the normalization and translation. Standing, nonredundancy, and use are supplied, but the exact-definition condition in the technical-name rule is not.

**Minimal repair:** either print the exact finite grammar/family definition from already permitted text evidence, or, because that definition is not present in the permitted source note, remove the symbols (B,B^+) and describe the proof as using proof-local normal forms and their conjunction/disjunction closure. The theorem statement does not require those auxiliary names.

### 9. Four editorial interventions are attributed to “the reader”

**Lines 546--550, 1173--1176, 1731--1735, and 1800--1802.** These are not places where the historical source leaves an exercise “to the reader.” They are handbook-supplied completions, corrections, or source-critical qualifications, yet the prose says “the reader's explicit completion,” “the reader records,” or “the reader has used.” That voice obscures who is supplying material and weakens the source/handbook boundary. By contrast, the phrases at lines 1050, 1162, 1201, 1306, 1751, and 1809 correctly report that the historical source leaves work to its reader and should remain.

**Minimal repair:** at the four editorial locations only, replace “the reader” with “this presentation” or “the handbook reconstruction,” and retain the explicit statement that the material is supplied or corrected rather than printed in the source.

### 10. Two groups of source atoms lack standing and consistent symbols

**Lines 1215--1223 and 1320--1333.** The fairness display introduces raw multi-letter (enabled) and (executed) without saying they are atomic state predicates. The terminal-server prose then names (NCS_i,TRY_i), while its formula uses the different raw strings (inNCS_i,inTRY_i), without defining either the standing of the latter pair or the relationship between the two pairs. In LaTeX those unmarked multi-letter strings also typeset as products of one-letter variables, unlike the explicitly formatted region atoms in the Clarke--Emerson subsection.

**Minimal repair:** declare and consistently typeset the first pair as atomic state predicates (for example \(\mathit{enabled}\), \(\mathit{executed}\)). Declare \(\mathit{inNCS}_i\) and \(\mathit{inTRY}_i\) as the terminal-server state predicates and use those exact symbols in both the prose and formula; do not alternate with undeclared (NCS_i,TRY_i).

### 11. Algorithm 16's work-set symbol is explained after the invariant uses it

**Lines 1593--1598.** The display uses (E), and only the following sentence says that (E) is the current work set. This is a literal definition-after-use defect.

**Minimal repair:** lead with “Writing (T) for the retained set and (E) for the current work set, the invariant is” before the display.

### 12. Theorem 6.83 is reported without its full quantified scope

**Lines 1780--1785.** “For every LTL formula” omits the transition-system hypothesis and the quantification over the displayed state (s). The permitted source note states the result for every transition system without terminal states, every state, and every LTL formula. The subsection's earlier standing convention does not repair an incomplete theorem report at this location.

**Minimal repair:** write “For every transition system without terminal states, every state (s), and every LTL formula \(\varphi\), Theorem 6.83 states …”.

### 13. The registered 1999 presentation is structurally nested inside the 2008 presentation

**Lines 1345--1849, especially 1817--1849.** The file gives peer subsections to Clarke--Emerson, Queille--Sifakis, Emerson--Halpern, and Baier--Katoen, but no subsection to Clarke--Grumberg--Peled. Its acquisition-only account appears in a terminal `\paragraph` under the Baier--Katoen subsection, together with repeated summaries of the preceding sources. This misstates the five-presentation hierarchy and makes the 1999 source boundary look like a qualification internal to Baier--Katoen.

**Minimal repair:** create a peer subsection for the Clarke--Grumberg--Peled 1999 acquisition boundary between the Emerson--Halpern and Baier--Katoen subsections, move the acquisition-only material at lines 1829--1849 into it, and delete or relocate the redundant cross-source recap at lines 1817--1828. Keep the current substantive boundary: contents-page locators are acquisition metadata only and support no grammar, algorithm, proof, example, or complexity claim.

## Audits with no additional must-fix finding

- **Acquisition-only evidence:** lines 1829--1849 correctly refrain from attributing substantive model-checking content to Clarke--Grumberg--Peled 1999. The contents-page starts are identified as locator metadata, adjacent works are excluded, and the host complexity theorem is tied to independent bibliography entries. The defect is hierarchy, not illicit substantive use.
- **Rights and source states:** the Clarke--Emerson authorized-reprint/original-pagination distinction, Queille--Sifakis scan-rights limitation, Emerson--Halpern conditional ACM terms, Clarke--Grumberg--Peled access boundary, and Baier--Katoen all-rights-reserved boundary agree with the permitted notes.
- **Citations and locators:** the five presentation keys and the four independent host-complexity keys exist in the inspected bibliography ranges. The cited page, definition, theorem, algorithm, and example locators in the LaTeX agree with the permitted source notes. No citation to the unacquired 1999 body is used for mathematical content.
- **Host references:** `Method~\ref{def:p09-ctl-labelling}`, `Theorem~\ref{thm:p09-ctl-labelling}`, and `Theorem~\ref{thm:p09-ctl-star-complexity}` point to labels present in the inspected host ranges. The presentation is input at host line 1507 after its method and theorems have been defined.
- **Proof status apart from Finding 4:** the presentation consistently distinguishes printed proofs, proof sketches, cited results, reader-left inductions, handbook reconstructions, and unsupported source defects. Theorem 6.83 still needs the exact scope repair in Finding 12, but it is not promoted to an algorithmic result.

## Text evidence read

- `handbook/parts/p09/presentations/n-c-016.tex`, lines 1--1849, complete.
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 945--1023 and 1505--1507.
- `handbook/parts/p08/temporal-epistemic-supplement.tex`, lines 42--190.
- `spec/research/p09-clarke-emerson-1981-source-note.md`, lines 1--884, complete.
- `spec/research/p09-queille-sifakis-1982-source-note.md`, lines 1--867, complete.
- `spec/research/p09-emerson-halpern-1986-source-note.md`, lines 1--729, complete.
- `spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md`, lines 1--470, complete.
- `spec/research/p09-baier-katoen-2008-ch6-source-note.md`, lines 1--1120, complete.
- `spec/research/p09-source-presentations-lot2-3.md`, lines 781--847.
- `handbook/bib/handbook.bib`, lines 2393--2407, 2409--2422, 2424--2436, 2438--2447, 2449--2458, 4815--4824, 4826--4835, 4837--4846, and 4897--4906.
- `spec/research/p08-new-content.md`, lines 810--830.

## Prohibitions observed

- No manuscript PDF, source PDF, render, screenshot, page image, or visual-layout evidence was opened or used.
- No TeX/PDF build was run.
- No test, checker, validator, repository script, or hash operation was run.
- No N-c-016 Round 1 report, source Round 2 report, other N-c-016 review, board, admission, handoff, or history file was read.
- No memory or prior-run history was consulted, preserving the blind-review boundary.
- No agent was inspected, contacted, or delegated to.
- No historical publication file was consulted because no concrete ambiguity remained after the permitted text evidence.
- No source file was edited; this report is the only file created.
- No page-layout issue is reported; layout remains reserved for the final publication gate.

REGISTER STATUS: OPEN

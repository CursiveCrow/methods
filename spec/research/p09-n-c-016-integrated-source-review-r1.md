# N-c-016 integrated source-fidelity review, Round 1

VERDICT: REJECT

## Decision

The integrated presentation is exceptionally well bounded across its five
source states, but one substantive claim in the Emerson--Halpern subsection is
false under the semantics stated in the presentation itself.  Because the
claim is source-attributed rather than marked as an unresolved printed defect,
it is a line-specific must-fix.  No access, rights, or provenance obligation is
being used as a reason for rejection.

## Must-fix finding

### N-c-016.tex lines 1224--1230: the displayed CTL formula cannot express the stated CTL* formula

Current text:

> The source also gives the less transparent CTL form
> `\(\neg E[\neg P\ U\ (P\land EGP)]\)`
> for `\(A(FP\lor G\neg P)\)`.

This equivalence is false under the manuscript's own preceding definitions.
At lines 967--975, `\(G\psi:=\neg F\neg\psi\)`.  Therefore

\[
 G\neg P=\neg FP,
 \qquad
 FP\lor G\neg P=FP\lor\neg FP.
\]

The path formula inside `A` is classically true on every path, so
`\(A(FP\lor G\neg P)\)` is true at every state.

The displayed CTL formula is not valid.  Take the one-state total structure
whose sole state has a self-loop and satisfies `P`.  At that state, `EGP` is
true.  Strong until permits its witness at index zero, as the presentation
states at lines 950--954 and 962.  Hence

\[
 E[\neg P\ U\ (P\land EGP)]
\]

is true with an empty left-prefix obligation, and its negation is false.  The
two displayed formulas therefore disagree on this finite total structure.

The permitted Emerson--Halpern source note repeats the same attribution, but
it does not resolve this semantic contradiction.  No historical publication
file was needed to establish the defect: the present claim is already refuted
by the presentation's explicit semantics.  It may concern a different source
formula or a further source defect, but neither possibility licenses the
current equivalence.

**Minimal repair:** delete manuscript lines 1224--1230.  They are not used by
any later construction or host theorem.  Retaining a CTL display would require
a separately source-reconciled antecedent; no replacement should be guessed
from the bounded evidence.

## Materials read directly as text

1. `handbook/parts/p09/presentations/n-c-016.tex`, lines 1--1856,
   consecutively from line 1 through EOF.
2. `handbook/parts/p09/logic-in-computer-science.tex`, lines 945--1022 and
   1504--1506.
3. `spec/research/p09-clarke-emerson-1981-source-note.md`, complete lines
   1--884 through EOF.
4. `spec/research/p09-queille-sifakis-1982-source-note.md`, complete lines
   1--867 through EOF.
5. `spec/research/p09-emerson-halpern-1986-source-note.md`, complete lines
   1--729 through EOF.
6. `spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md`,
   complete lines 1--470 through EOF.
7. `spec/research/p09-baier-katoen-2008-ch6-source-note.md`, complete lines
   1--1120 through EOF.
8. `spec/research/p09-source-presentations-lot2-3.md`, only lines 781--847.
9. `handbook/bib/handbook.bib`, only these permitted entries and exact ranges:
   `ClarkeEmerson1981` at 2393--2407; `QueilleSifakis1982` at 2409--2422;
   `EmersonHalpern1986` at 2424--2436; `ClarkeGrumbergPeled1999` at
   2438--2447; `BaierKatoen2008` at 2449--2458; `EmersonHalpern1985` at
   4815--4824; `ClarkeEmersonSistla1986` at 4826--4835; `EmersonLei1987` at
   4837--4846; and `EmersonJutla1999` at 4897--4906.
10. `handbook/parts/p08/temporal-epistemic-supplement.tex`, only lines
    42--190.
11. `spec/research/p08-new-content.md`, only lines 810--830.
12. The repository technical-name rule supplied in the task-scoped AGENTS
    instructions; it was applied as an instruction, not used as substantive
    source evidence.

Review/admission statements embedded in the otherwise permitted compact record
were disregarded.  They played no role in this verdict.

## Complete presentation audit

The following records the disposition of every substantive presentation
surface.  “Supported” means supported at exactly the stated source, proof, or
reconstruction strength; it does not mean that an omitted proof was silently
supplied.

### Clarke--Emerson, lines 3--464

| Current lines | Claim surface | Source-fidelity result |
|---:|---|---|
| 6--15 | 1981 meeting, 1982 LNCS publication, authorized 2008 reprint, original/reprint pagination, and separate expanded manuscript | Supported.  The published twenty-page body and the 37-numbered-page expanded manuscript are not conflated. |
| 17--36 | synchronization skeleton, global system flowgraph, suppressed code, standing, distinctions, and factorization use | Supported.  Necessity, definition, standing, nonredundancy, and later use are all supplied.  No low-level synthesis or refinement theorem is invented. |
| 38--56 | `M=(S,A_1,...,A_k,L)`, countable state set, process relations, total union, infinite paths, and computation-tree unfolding | Supported at original pp. 53--54.  Per-process skeletons, computation trees, and the later finite global graph remain distinct. |
| 58--95 | literal indexed CTL grammar and satisfaction clauses | Supported.  `EX_j` is retained, path quantification is limited to the stated constructors, and until is both strong and current-inclusive. |
| 97--120 | source-defined `V`, `AF`, `EF`, `AG`, `EG`, indexed/unindexed next abbreviations, and vacuity of `AX_i` | Supported.  The process-indexed distinction needed by the mutual-exclusion requirements is not normalized away. |
| 122--164 | finite model-checker contract, bottom-up passes, guarded universal/existential recurrences, stabilization argument, quadratic source bound, and separation from the later linear bound | Supported.  The existential recurrence is expressly labelled a reconstruction from the printed base and loop rather than a second source display. |
| 166--179 | omitted `f_1` guard in the source approximation | Supported source-critical repair.  The correct identity, prose, and algorithm are distinguished from the defective intervening display. |
| 181--193 | `AFb and EGa` source graph and four snapshots | Supported and mathematically consistent with the stated graph. |
| 195--202 | finite-structure SCC characterization of infinitely-often reachability | Supported at Proposition 4.1 strength; the infinitary operator is kept outside the base grammar. |
| 204--220 | arbitrary LTL-under-path-quantifier extension and directed-Hamiltonian-path reduction | Supported exactly as NP-hardness.  It is not inflated to NP-completeness or a full CTL* theorem. |
| 222--303 | satisfiability outline, `Blocks`, `Tiles`, alpha/beta expansion, termination count, worked tableau, BM81 correction, and proof boundary | Supported.  The published outline is not augmented with the expanded manuscript's appendix or promoted to a complete printed correctness proof. |
| 305--375 | three synthesis stages and all nine indexed mutual-exclusion requirement groups | Supported.  The formulas preserve process-indexed next modalities and the anti-vacuity conjunct in requirement 6. |
| 377--397 | invariant suppression, model fragments, checked eventualities, duplicate labels, and `TURN` | Supported.  `model fragment` receives an exact construction-artifact standing and `TURN` is correctly identified as an auxiliary program variable used by factorization. |
| 399--451 | factored `P_1/P_2` skeleton transitions and general global-to-local factorization | Supported by the detailed source example and general rule.  Enabling disjunctions and copied auxiliary assignments retain their exact role. |
| 453--464 | provisional practicality, DEC 11/70 implementation, and differentiated proof statuses | Supported.  The implementation claim concerns the model checker, not a proof or implementation of general synthesis. |

I found no Clarke--Emerson line-specific must-fix.

### Queille--Sifakis, lines 465--788

| Current lines | Claim surface | Source-fidelity result |
|---:|---|---|
| 468--475 | original/reprint identity, complete institutional scan, authentication, and open rights/provenance limits | Supported.  The open distribution-authorization question is separated from textual identity and mathematical completeness. |
| 477--503 | CESAR inputs, interpreted Petri net definition, guarded assignments, rendezvous translation, asserted safety, and diagnostics-only output | Supported.  The translation grammar and correctness proof are not supplied, and no counterexample format, synthesis algorithm, or refinement theorem is attributed. |
| 505--523 | alternating-bit protocol, four processes, initial marking, external non-loss assumption, and absent fairness | Supported.  The prose assumption is correctly kept external to the printed transition model. |
| 525--585 | literal `POT/INEV` language, `ALL/SOME` duals, completed execution convention, maximal paths, omega padding, semantics, and printed omissions | Supported.  The added start/adjacency clauses are explicitly reader completions; omitted Boolean clauses are not misreported as source displays. |
| 587--688 | `Init`, `enable`, `after`, invariants, liveness, deadlock, response families, and `receivack` repair | Supported.  Possibility of future enabledness is not strengthened to occurrence or fairness, and the misspelled source identifier is recorded before repair. |
| 690--738 | predecessor/dual, literal finite-iteration notation, four identities, image-finiteness, and delegated proof status | Supported.  The superscript `x` is defined rather than treated as an unexplained fixed-point binder. |
| 740--775 | analyzer architecture and sole complete sender calculation | Supported.  The Boolean calculation and its result are source-controlled; no other property is claimed worked. |
| 777--788 | iteration cap, supported variable domains, possible no-answer outcome, and non-results | Supported.  No asymptotic bound, total-answer theorem, satisfiability procedure, complete calculus, or CESAR synthesis result is invented. |

I found no Queille--Sifakis line-specific must-fix.  Its scan-rights provenance
remains open without undermining the honestly bounded mathematical
reconstruction.

### Emerson--Halpern, lines 789--1351

| Current lines | Claim surface | Source-fidelity result |
|---:|---|---|
| 792--798 | complete 1986 JACM source, rights terms, and distinct preliminary/report states | Supported. |
| 800--868 | Lamport structure, finite/infinite paths, branching/linear readings, model-validity, strong equivalence, Theorems 1--2, and Proposition 1 | Supported at the recorded restatement/proof boundaries. |
| 870--901 | suffix, fusion, limit, `R`-generability, state completeness, separate uses, and source type typo | Supported.  These names have standing as structure/path-set properties, not operators. |
| 903--994 | mutually typed CTL* grammar, exact semantics, derived operators, named sublanguages, CTL identification, and formula length | Supported.  State/path standing and path-quantifier conversion are explicit. |
| 996--1044 | Lamport translations, `B(L)`, pointwise equivalence, Propositions 2--4, Corollary 1, assumptions, and counterexamples | Supported at the source's stated proof strengths. |
| 1046--1069 | Figure 1 expressiveness map and incomparable missing edges | Supported.  All and only the diagram's transitive edges are asserted. |
| 1071--1083 | Theorem 3 path-deletion separation | Supported by the complete short source proof. |
| 1085--1108 | Theorem 4 normalization, basic-formula families, interleavings, induction, and bad “Theorem 4.2” pointer | Supported.  The locally reused `B` and `B+` names are distinguished from `B(L)`. |
| 1110--1175 | Theorems 5--6 literal target defects, source model families, proof-supported targets, wrong theorem references, and lack of erratum | Supported as transparent source-critical reconstruction.  Literal and proof-supported statements remain separate. |
| 1177--1212 | Theorem 7 families/induction and cited-but-unproved Theorems 8--9 | Supported.  Reader-left Boolean cases and external proof dependencies are not promoted. |
| 1214--1222 | strong-eventual-fairness formula and structural versus specification fairness | Supported and semantically correct. |
| 1224--1230 | asserted CTL rendering of `A(FP or G not P)` | **Must-fix: false, as proved above.** |
| 1232--1253 | CTL*-to-PL translation, operator standing, Proposition 5, and unprinted induction | Supported at the stated translation/proof boundary. |
| 1255--1325 | MPL stages, literal `U/X` clauses, concrete countermodels, closure lemmas, Theorem 10 tension, and TC expectation | Supported.  The manuscript does not silently repair or validate the inconsistent printed clauses. |
| 1327--1351 | terminal-server example and application-only conclusion | Supported.  No state-labelling algorithm, general complexity result, synthesis proof, or universal dominance theorem is attributed. |

Apart from lines 1224--1230, I found no Emerson--Halpern line-specific
must-fix.

### Baier--Katoen, lines 1352--1823

| Current lines | Claim surface | Source-fidelity result |
|---:|---|---|
| 1355--1361 | complete body, rights, and corrected Chapter 6/CTL* page map | Supported. |
| 1363--1432 | inherited action-labelled transition system, finiteness, `Post`, no-terminal hypothesis, `R_0/V_0` bridge, edge-count inequality, and path definitions | Supported.  `R_0` and `V_0` are explicitly handbook-supplied eliminable definitions, not falsely attributed source terms. |
| 1434--1481 | typed CTL grammar, derived operators, path/state semantics, satisfaction sets, initial-state test, and empty-initial-set case | Supported. |
| 1483--1497 | existential normal form, universal rewrites, proof-outline status, exponential expansion warning, and direct-modality boundary | Supported. |
| 1499--1547 | Algorithm 13, Theorem 6.23 least/greatest characterizations, source proof, and relation to host fixed-point notation | Supported.  The manuscript marks its explicit global assembly rather than attributing a separately labelled proof. |
| 1549--1616 | Algorithm 14, approximation chains, Algorithms 15--16, invariant, termination, and global correctness induction | Supported.  Naive loops and optimized worklists are kept distinct. |
| 1618--1667 | exact Figure 6.11 graph, Boolean comparison abbreviations, eventuality calculation, and existential-always calculation | Supported and arithmetically consistent with the stated labels and edges. |
| 1669--1683 | Theorem 6.30 parameters, linked-list/worklist hypotheses, exact time bound, and absent separate space theorem | Supported. |
| 1685--1744 | Example 6.31, Hamiltonian formula family, totalization state, exact equivalence, exponential formula size, and uniformity gap | Supported as a source example plus an explicitly handbook-owned logical qualification; it is not merged into Theorem 6.30. |
| 1746--1769 | Theorem 6.21 source systems, key omitted induction, similar-case omission, trace separation, and Theorem 6.18 proof boundary | Supported. |
| 1771--1805 | typed CTL* grammar, LTL embedding, Theorem 6.84 witness, atom-substitution reconstruction, and absence of CTL* model-checking result | Supported. |
| 1807--1823 | enumerated printed defects and final source/handbook proof boundary | Supported and consistent with the permitted source note. |

I found no Baier--Katoen line-specific must-fix.

### Remaining source boundaries, lines 1824--1856

- Lines 1825--1835 accurately summarize the acquired Clarke--Emerson,
  Queille--Sifakis, and Emerson--Halpern source states and preserve their
  distinct rights and proof boundaries.
- Lines 1836--1846 stay within the Clarke--Grumberg--Peled acquisition note:
  they make a route-bounded access claim as of 22 August 2026, distinguish
  restricted/physical availability from anonymous public access, and use the
  contents page only for acquisition locators.  No grammar, algorithm,
  theorem, proof, example, or figure is attributed to the unacquired body.
- Lines 1848--1852 correctly keep the 1996 survey, 2001 chapter, 2018 second
  edition, and 2008 Baier--Katoen book separate from the missing first-edition
  text.
- Lines 1853--1856 accurately assign the four host complexity classifications
  to independent sources rather than Clarke--Grumberg--Peled 1999.

I found no line-specific must-fix in this terminal boundary.  The 1999 body
properly remains an open source-content obligation.

## Host integration audit

### Part IX lines 945--1022

- Lines 948--967 correctly reuse the Part VIII CTL/CTL* definitions and define
  the existential and universal predecessor maps as state-set operations.  The
  operations have exact definitions, clear standing, necessity, distinction
  from path quantifiers, and immediate use.
- Lines 969--995 give the standard total finite-state labelling equations.
  The `EX/AX`, existential/universal until, `EG/AG`, and `EF/AF`
  abbreviation clauses agree with the reused strong-until semantics.  On a
  finite structure, monotone approximants and one-time state entry/deletion per
  subformula support the stated worklist description.
- Lines 997--1005 correctly state semantic correctness and the
  `O((|S|+|R|)|A|)` adjacency-list/worklist bound.  The Baier--Katoen bridge at
  presentation lines 1389--1419 properly distinguishes binary edges from
  source action-labelled transition triples.
- Lines 1007--1014 correctly state finite-total LTL/CTL incomparability using
  the CTL pattern `AG EF p` and universal-path LTL pattern `F G p`, and place
  both typed languages inside CTL*.
- Lines 1016--1022 correctly separate CTL model-checking P-completeness,
  combined CTL* model-checking PSPACE-completeness, CTL satisfiability
  EXPTIME-completeness, and CTL* satisfiability 2EXPTIME-completeness.  The
  independent sources are present in the permitted bibliography entries and
  match the permitted Part VIII complexity-citation record.

No host line-specific must-fix was found in lines 945--1022.  The rejected
presentation claim at lines 1224--1230 is not used by these host definitions or
theorems.

### Part IX lines 1504--1506

Line 1506 includes the complete N-c-016 presentation after the host material.
The placement supplies the reused CTL/CTL* and labelling definitions before the
presentation's backward references.  No duplicate or competing source
attribution is introduced by the adjacent input line.

### Part VIII prerequisite lines 42--190

- The total transition structure, infinite paths, typed CTL grammar, strong
  until, typed CTL* grammar, path semantics, and the CTL/CTL* cards are
  definitionally compatible with the Part IX reuse.
- The cards' complexity statements use the same independent citations and
  problem distinctions as the Part IX theorem.
- The presentation correctly treats source-specific finite paths, process
  indices, action labels, and no-terminal conventions as source-state
  differences rather than silently rewriting the Part VIII definitions.

No prerequisite-integration must-fix was found.

## Attribution, locators, proof status, and bibliography

- `ClarkeEmerson1981`, `QueilleSifakis1982`, `EmersonHalpern1986`,
  `ClarkeGrumbergPeled1999`, and `BaierKatoen2008` have bibliographic identities,
  page ranges, dates, source-state notes, and access boundaries consistent with
  their respective permitted records.
- The workshop/publication distinction for Clarke--Emerson is explicit; the
  expanded manuscript is not treated as extra pages of the LNCS chapter.
- Queille--Sifakis rights provenance remains open, but the original-body
  textual reconstruction does not claim an open licence or publisher-open
  access.
- Emerson--Halpern's preliminary papers/reports, source theorem defects,
  cited proofs, reader-left inductions, and unproved translation steps are
  separated from the complete 1986 body.
- Clarke--Grumberg--Peled 1999 is used only for identity, route/access state,
  and contents-level acquisition targets.  No content from Baier--Katoen, the
  1996 survey, the 2001 chapter, or the 2018 edition is attributed to it.
- Baier--Katoen locators distinguish inherited definitions, CTL syntax,
  expressiveness, model checking, and CTL*.  Its all-rights-reserved status is
  not mistaken for permission to reproduce the book.
- The independent complexity entries `EmersonHalpern1985`,
  `ClarkeEmersonSistla1986`, `EmersonLei1987`, and `EmersonJutla1999` match the
  host theorem's four distinct bounds.
- Except for the false equivalence at presentation lines 1224--1230, source
  claims carry appropriate pages, sections, theorem/lemma/proposition/example
  numbers, or explicit source-state boundaries.

## Repository technical-name rule

The presentation otherwise complies with the task-supplied AGENTS rule.

- `synchronization skeleton`, `global system flowgraph`, and `model fragment`
  are introduced with necessity, definitions, mathematical/program standing,
  distinctions from existing objects, and concrete later use.
- `interpreted Petri net`, `POT`, `INEV`, `ALL`, `SOME`, `enable`, `after`, and
  the literal iteration superscript receive source definitions and clear
  standing; missing source clauses are identified rather than filled by new
  primitives.
- `Blocks`, `Tiles`, the closure-class names, typed state/path formula families,
  `B(L)`, the Appendix's distinct `B/B+`, and MPL `stage` receive explicit
  metalinguistic or semantic standing and nonredundancy explanations.
- The handbook-supplied `R_0` and `V_0` bridge and the Boolean comparison signs
  are eliminably defined and explicitly denied source-term status.
- No technical name is assigned to a hypothetical Clarke--Grumberg--Peled
  construction.  Lines 1836--1856 describe the owed acquisition/source
  artifacts instead.

The must-fix at lines 1224--1230 is not a technical-name violation; it is a
false semantic equivalence.

## Prohibitions and blindness observed

- I did not open or use any N-c-016 review, board, admission, handoff, or
  review-history file.
- I did not inspect, list, contact, or delegate to another agent.
- I did not inspect a manuscript PDF, rendered page, screenshot, page image, or
  any other rendered manuscript evidence.
- I did not build TeX or the handbook.
- I did not run a test, test harness, checker, repository script, automated
  validator, executable example, or hash operation.
- I did not consult any historical publication file.  The one must-fix is
  decidable directly from the permitted textual evidence and the manuscript's
  own formal semantics, so no conditional historical-source exception was
  needed.
- Hash strings and review/admission assertions appearing inside permitted text
  records were neither computed, compared, nor used as verdict evidence.
- I did not edit the manuscript, host, notes, bibliography, ledger, or any
  collateral file.  This report is the only file created.

The final register status remains open independently of this rejection because
the Clarke--Grumberg--Peled 1999 body and Queille--Sifakis rights provenance
remain open.

REGISTER STATUS: OPEN

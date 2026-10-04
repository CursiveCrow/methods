# N-c-016 integrated publication and terminology review, round 1

VERDICT: REJECT

## Decision

The complete current presentation is source-bounded, mathematically ordered,
and substantially compatible with the host, but four line-specific
publication/terminology defects remain. Two are exact standing/hierarchy
errors, one violates the requested definition-before-use order, and one leaves
the Queille--Sifakis source-state and rights paragraph without its own
citation. These are narrow repairs; no mathematical or source reconstruction
is requested.

## Must-fix findings

### 1. The CESAR invariant schema changes the type of `P` without saying so

**Current lines:** `handbook/parts/p09/presentations/n-c-016.tex` 597--612.

Lines 597--608 bind (P) as a **process** and define (A(P)) as that
process's finite action set. Lines 609--611 then write

\[
  \operatorname{Init}\Rightarrow\operatorname{ALL}(P)
\]

without rebinding (P). At that point the displayed expression applies the
state-formula operator `ALL` to the process just introduced. The intended
source schema instead uses a Boolean program predicate as the operand. The
protocol instances at lines 613--625 make the intended reading recoverable,
but they do not repair the local type standing.

**Minimal repair:** separate the metavariables. For example, use
(\mathcal P) for the process in lines 597--608 and state, before the invariant
display, “For a Boolean program predicate (P), the invariant schema is
...”. Equivalently, retain the earlier notation and explicitly rebind the
schema operand under a fresh name such as (B), writing
(\operatorname{ALL}(B)). No substantive formula change is needed.

### 2. The PL operators are used before their standing is supplied

**Current lines:** `handbook/parts/p09/presentations/n-c-016.tex` 1232--1248.

The translation display at lines 1237--1244 already applies the unfamiliar PL
operators (\mathsf f) and (\mathbin{\mathrm{suf}}). Only after the display,
at lines 1246--1248, does the prose say that (\mathsf f) tests the unique
length-zero initial prefix and that `suf` selects a proper suffix after an
interval satisfying its left operand. This is the only place their standing is
given, so the display precedes the definitions needed to parse it.

**Minimal repair:** move the two-sentence operator explanation before the
translation display, or introduce those two operator meanings in the sentence
ending at line 1235. Keep the equations and the source-proof boundary
unchanged.

### 3. Three internal references call an `hbmethod` a Definition

**Current lines:** `handbook/parts/p09/presentations/n-c-016.tex` 1400--1401,
1526--1528, and 1819--1822.

All three passages print
`Definition~\ref{def:p09-ctl-labelling}`. The referenced host object is
actually declared at
`handbook/parts/p09/logic-in-computer-science.tex` 969--995 as

```tex
\begin{hbmethod}{def:p09-ctl-labelling}{Total finite-state CTL labelling}
```

The `def:` prefix in the label does not change the object hierarchy. Calling
the object a Definition is inconsistent with the source and with its role as
the handbook's algorithmic method.

**Minimal repair:** replace `Definition~` by `Method~` at manuscript lines
1400, 1527, and 1820. Keep the label unchanged.

### 4. The Queille--Sifakis source-state and rights paragraph is uncited

**Current lines:** `handbook/parts/p09/presentations/n-c-016.tex` 468--475.

This standalone opening paragraph makes publication-, reprint-, scan-, access-,
and distribution-rights claims, including the distinction between the
complete original scan and the uninspected subscription-only reprint pages.
Unlike the corresponding Clarke--Emerson, Emerson--Halpern, Baier--Katoen, and
Clarke--Grumberg--Peled opening/boundary passages, it ends without a citation.
The first citation in this subsection occurs at line 503 and carries the page
locator `pp. 337--340`; that locator supports the subsequent program-model
content, not the 2008 reprint/access/right-state claims in the preceding
paragraph. The `QueilleSifakis1982` bibliography entry expressly records the
institutional-scan and redistribution boundary.

**Minimal repair:** add `\cite{QueilleSifakis1982}` at the end of line 475 (or
the equivalent end of that paragraph). No page locator is needed for the
bibliographic/access-state claim.

## Audit of the remaining text

### Definition order, symbol standing, and terminology

Apart from findings 1--2, the manuscript supplies the necessary standing
before argumentative use:

- Clarke--Emerson's synchronization skeleton is defined as a per-process
  abstraction at lines 17--35, distinguished from both the computation-tree
  unfolding and the global system flowgraph, and then used by the synthesis
  factorization at lines 305--451.
- The indexed source structure, grammar, path semantics, derived operators,
  finite-state labelling recurrence, tableau operations, model fragments, and
  `TURN` component are each defined before their later calculations. The
  necessity, standing, nonredundancy, and use of the nonstandard source terms
  are stated locally rather than deferred.
- Queille--Sifakis's interpreted Petri net has an exact model standing at lines
  477--493; `POT`, `INEV`, `ALL`, `SOME`, maximal executions, program-derived
  atoms, predecessor transformers, and the source's superscript-(x)
  iteration receive explicit definitions. The current text correctly
  distinguishes `enable a` from `after a` and enabledness from execution.
- Emerson--Halpern's state/path distinction, closure properties,
  (R)-generability, model-validity, strong equivalence, named language
  fragments, (B(L)), the Appendix's separate `B`/`B+` normal-form families,
  and MPL stages all have explicit syntactic or metalinguistic standing. The
  source's overloaded letters are distinguished where their uses would
  otherwise collide.
- Baier--Katoen's action-labelled transition system, the handbook-supplied
  (R_0,V_0) bridge, path fragments, typed CTL and CTL* grammars, ENF,
  satisfaction sets, work sets, counter invariant, and metalinguistic Boolean
  comparison abbreviations are all defined and later used. No unneeded new
  primitive is introduced.

No hypothetical name is assigned to the missing Clarke--Grumberg--Peled
construction. Lines 1836--1856 describe an owed acquisition/reconstruction
artifact and keep all first-edition body-dependent definitions, algorithms,
proofs, and examples open, as required by the local `AGENTS.md` rule.

### Source/reader voice, source state, rights, and proof status

The presentation consistently separates source text from reader
reconstruction:

- Clarke--Emerson's guarded universal-until recurrence and reconstructed
  existential recurrence are identified at lines 133--179; the conference
  body, longer manuscript, source defect, tableau-outline status, and
  synthesis status remain separate.
- Queille--Sifakis's missing execution and Boolean clauses, external non-loss
  assumption, `receivack` defect, image-finiteness hypothesis, delegated
  fixed-point proofs, iteration cap, and possible no-answer behavior are
  preserved rather than normalized into a later CTL theorem.
- Emerson--Halpern's literal Theorem 5--6 targets, proof-supported repairs,
  wrong theorem cross-references, omitted induction cases, and unresolved MPL
  (U/X) clauses are all reported with distinct literal-source and
  proof-supported statuses. The article is not made to supply a CTL
  state-labelling algorithm or complexity theorem.
- Baier--Katoen's reader-supplied (R_0,V_0) bridge, assembled global
  correctness induction, source defects, omitted bounded-formula proof,
  one-sentence CTL* strictness proof, and Hamiltonian-family uniformity gap are
  explicitly labelled. The book's all-rights-reserved state is not treated as
  republication permission.
- The acquisition-only Clarke--Grumberg--Peled record carries only identity,
  access-state, contents-locator, and non-substitution claims. It is not used
  for a grammar, algorithm, theorem, proof, example, or complexity result.

The remaining source citations use the correct source object and original
page numbering. The registered 1981 Clarke--Emerson event date is separated
from the 1982 publication; the Queille--Sifakis original and reprint ranges are
not merged; the Emerson--Halpern journal body is distinguished from its
preliminary states; and the Baier--Katoen Chapter 6 locators reflect the
corrected printed pages.

### Host and prerequisite compatibility

The actual prerequisite definitions at
`handbook/parts/p08/temporal-epistemic-supplement.tex` 42--190 establish the
total-transition path semantics and CTL/CTL* state/path distinction reused by
the host. The actual host at
`handbook/parts/p09/logic-in-computer-science.tex` 945--1022 then defines the
predecessor maps, gives the finite-state labelling method, states correctness
and the edge-sensitive time bound, and keeps the LTL/CTL and CTL/CTL* decision
boundaries distinct. The presentation is input at host line 1506.

The source-specific variants are reconciled rather than silently identified:
Clarke--Emerson retains process-indexed next; Queille--Sifakis retains maximal
finite executions and its unary source operators; Emerson--Halpern retains its
broader path-structure comparison; and Baier--Katoen's action-labelled tuple is
mapped to the host's binary total relation. The only hierarchy mismatch is the
threefold `Definition`/`Method` error in finding 3.

## Evidence and method record

Text read directly:

1. `handbook/parts/p09/presentations/n-c-016.tex`, lines 1--1856, continuously
   from line 1 through EOF.
2. `handbook/parts/p09/logic-in-computer-science.tex`, lines 945--1022 and
   1504--1506.
3. `handbook/parts/p08/temporal-epistemic-supplement.tex`, lines 42--190.
4. `spec/research/p09-clarke-emerson-1981-source-note.md`, lines 1--884.
5. `spec/research/p09-queille-sifakis-1982-source-note.md`, lines 1--867.
6. `spec/research/p09-emerson-halpern-1986-source-note.md`, lines 1--729.
7. `spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md`, lines
   1--470.
8. `spec/research/p09-baier-katoen-2008-ch6-source-note.md`, lines 1--1120.
9. `spec/research/p09-source-presentations-lot2-3.md`, lines 781--847.
10. `spec/research/p08-new-content.md`, lines 810--830.
11. `handbook/bib/handbook.bib`, displayed ranges 2393--2465 and 4815--4915.
    Substantive bibliography use was restricted to the required entries at
    2393--2407, 2409--2422, 2424--2436, 2438--2447, 2449--2458,
    4815--4824, 4826--4835, 4837--4846, and 4897--4906; adjoining entries in
    the two displayed ranges were not used as evidence.

The disposition/admission or prior-review statements incidentally present
inside the expressly permitted source/compact records were disregarded. This
verdict was reached independently from the actual manuscript, host,
prerequisites, and source-content evidence.

Prohibitions observed:

- no N-c-016 review, board, admission, handoff, ledger, or review-history file
  was opened or used;
- no other agent was inspected, listed, messaged, consulted, or delegated to;
- no manuscript PDF, source PDF, rendered page, screenshot, PNG, page image,
  or visual-layout evidence was opened or used;
- no historical publication file was consulted because no residual factual
  ambiguity required one;
- no TeX or handbook build, test, test harness, checker, repository script, or
  automated validator was run;
- no hash was computed, compared, or used as evidence; pre-existing hash text
  in the permitted records was disregarded; and
- no web source was consulted in this round.

Visual layout is outside this verdict and remains reserved for the final
publication gate.

REGISTER STATUS: OPEN

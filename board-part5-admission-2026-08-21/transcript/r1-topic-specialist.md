# Round 1 blind opening — arithmetic/proof-theory topic specialist

## Verdict

**Do not admit Part V in its present source/content state.**  The exact
inherited arithmetic and incompleteness sequence is mathematically coherent at
its declared proof ceilings, but the routed additions still render an explicit
OPEN/unadmitted denial; the Goodstein object used by an independence theorem is
not uniquely defined; the Solovay and reverse-mathematics surfaces do not state
all load-bearing hypotheses/axiom schemes exactly; and multiple registered
Part V depth/apparatus commitments are absent or materially incomplete.

I read `board-part5-admission-2026-08-21/charter.md` before the artifact and did
not read another Part V seat's transcript.  I reviewed the complete live graph
rooted at `handbook/parts/p05.tex` and
`handbook/annex/p05-route.tex`: two roots, nineteen exact-source wrappers,
nineteen matching inherited targets, five routed editorial body additions, and
one routed editorial annex addition, **46 reachable files**.  I made no
manuscript, control, test, or generated-file edit and ran no build or test.

## Findings

### F1 [blocker] [open] Routed pages explicitly declare themselves OPEN and unadmitted

- **Author:** arithmetic/proof-theory topic specialist, R1
- **Criterion:** no reader-visible OPEN, unadmitted, owed, stub, pointer-only,
  internal-workflow, or denial-of-admission prose
- **Location:**
  - `handbook/parts/p05/models-and-interpretability-supplement.tex:19-22`;
  - `handbook/annex/p05/depth-completion-supplement.tex:15-17`;
  - routes: `handbook/parts/p05.tex:13-15` and
    `handbook/annex/p05-route.tex:4-7`.
- **Claim/evidence:** the body renders the heading “OPEN later arithmetic-model
  and interpretation material,” followed by bold “OPEN and unadmitted” and the
  assertion that the additions close no source, content, AI, build, visual,
  register, or acceptance gate.  The reciprocal annex renders the same denial.
  These are not comments; they are reader pages on the accepted route.
- **Concrete harm:** the artifact cannot satisfy a charter whose purpose is to
  decide source/content admission while its own pages deny source/content and
  register closure.  Merely deleting the words would conceal, rather than
  settle, the outstanding depth/apparatus defects below.
- **Exact correction:** first resolve and record every retained body's actual
  content/source/proof standing, including F2--F6.  Then replace both rendered
  notices by ordinary attribution/nonreplacement prose and exact theorem
  status, keeping the body `sketched=annex:p5.sigma.1` declaration reciprocal
  with its annex item.  Alternatively remove the supplement and matching annex
  from the admitted route.  Do not claim that notice deletion itself closes a
  register or human/build gate.
- **Status:** open

### F2 [must-fix] [open] “Goodstein sequence” does not bind the starting base or stage schedule

- **Author:** arithmetic/proof-theory topic specialist, R1
- **Criterion:** exact recursive definition before theorem use; exact
  independence statement
- **Location:**
  `handbook/parts/p05/independence-catalog.tex:31-51`, especially lines 31-39;
  the hydra continuation is lines 53-58.
- **Claim/evidence:** the definition says “Starting with \(m\), write it in
  hereditary base \(b\), replace every occurrence of \(b\) by \(b+1\), and
  subtract one; iterate while increasing the base.”  The variable \(b\) is
  never initially bound, and no recurrence says which base belongs to stage
  \(n\).  Consequently the alleged “exact numerical sequence” is not a
  function of \(m\) alone.  The standard special Goodstein sequence begins in
  hereditary base 2 and uses bases \(2,3,4,\ldots\); see Goodstein's primary
  paper, [DOI 10.2307/2268019](https://doi.org/10.2307/2268019), and the
  Kirby--Paris independence source,
  [DOI 10.1112/blms/14.4.285](https://doi.org/10.1112/blms/14.4.285).
- **Minimal counterexample:** for \(m=4\), hereditary base 2 gives
  \(4=2^{2}\), hence the first base change gives \(3^3-1=26\).  Starting in
  base 3 gives \(4=3+1\), hence \(4+1-1=4\).  The current text licenses both,
  so the next term is not determined.
- **Concrete harm:** “every Goodstein sequence terminates” at lines 48-51 has
  no unique local subject, and the cited PA-unprovability result is sensitive
  to the selected sequence family.  The subsequent hydra paragraph likewise
  invokes a termination/unprovability theorem while providing no selected
  Kirby--Paris position and move relation; it correctly warns that “hydra” is
  not canonical but does not supply the registered artifact.
- **Exact correction:** define \(g_0(m)=m\).  If \(g_n(m)>0\), write it in
  hereditary base \(n+2\), recursively including all exponents, replace every
  occurrence of \(n+2\) by \(n+3\), and subtract one to obtain
  \(g_{n+1}(m)\); declare the zero continuation/termination convention.  State
  the universal theorem for exactly this family.  For the hydra commitment,
  either define one cited Kirby--Paris tree and move rule before asserting its
  theorem, or label it as an owed rule-specific artifact rather than a
  theorem-bearing paragraph.
- **Status:** open

### F3 [must-fix] [open] Solovay completeness is presented under a non-eliminable base-theory condition

- **Author:** arithmetic/proof-theory topic specialist, R1
- **Criterion:** exact base theory, proof predicate, and soundness hypotheses
- **Location:**
  `handbook/parts/p05/provability-logic-gl.tex:18-34,54-64`.
- **Claim/evidence:** the realization definition permits a recursively
  axiomatized extension of “enough elementary arithmetic,” but that phrase has
  no exact theory or eliminable property.  The theorem then says “for a
  standard arithmetical base such as \(\mathsf{PA}\)” while displaying only
  PA.  The literal PA equivalence is the classical theorem in an ambient
  metatheory that verifies the standard model, but “such as” does not license
  transfer to the earlier generic \(T\).  General arithmetical-completeness
  formulations require, for example, a c.e. \(\Sigma^0_1\)-sound extension of
  a specified elementary base and a canonical \(\Sigma^0_1\) provability
  predicate; \(\Sigma^0_1\)-unsound effective extensions can have a different
  provability logic.  Compare Solovay's primary paper,
  [DOI 10.1007/BF02757006](https://doi.org/10.1007/BF02757006), and the
  precise modern formulation quoted in Yong Cheng's survey,
  [Theorem 3.3](https://philpapers.org/archive/CHECRO-5.pdf).
- **Concrete harm:** a reader can instantiate Definition 5.2's vague generic
  \(T\) and read the following completeness statement as applying, even though
  the converse Solovay construction is not invariant under arbitrary base
  theory/numeration changes.  Line 63 itself warns that changing the base or
  predicate requires a new theorem, but the hypothesis does not say what
  licenses the displayed one.
- **Exact correction:** choose one of two exact statements.  Either restrict
  the definition/theorem literally to PA with the already fixed standard PA
  proof predicate and state that the ambient standard-model soundness
  establishes the needed \(\Sigma^0_1\)-soundness; or quantify over a specified
  c.e. \(\Sigma^0_1\)-sound \(T\) extending the named elementary base and use
  its canonical \(\Sigma^0_1\) proof predicate.  Delete “enough” and “such as”
  unless they are replaced by those exact hypotheses.
- **Status:** open

### F4 [must-fix] [open] The reverse-mathematics base and advertised equivalences are not exact formulas

- **Author:** arithmetic/proof-theory topic specialist, R1
- **Criterion:** definition before use; exact subsystem axioms, parameters,
  coding, and theorem strength
- **Location:** `handbook/parts/p05/reverse-mathematics.tex:9-59`.
- **Claim/evidence:** `def:p05-rca0` says that \(\mathsf{RCA}_0\) “contains
  elementary arithmetic” without fixing the basic second-order-arithmetic
  signature or discrete ordered-semiring axioms.  It describes
  \(\Delta^0_1\)-comprehension informally but does not state its premise
  \(\forall n(\varphi(n)\leftrightarrow\psi(n))\), the respective
  \(\Sigma^0_1/\Pi^0_1\) syntactic classes, permissible number/set parameters,
  or freshness of the comprehended set.  These choices distinguish
  \(\mathsf{RCA}_0\) from nearby systems such as \(\mathsf{RCA}_0^*\).
  Simpson's standard source gives the exact system:
  [DOI 10.1017/CBO9780511581007](https://doi.org/10.1017/CBO9780511581007).
- The table at lines 40-55 is headed “Sample equivalent over the stated base,”
  but entries such as “basic countable algebra and analysis,” “standard
  compactness forms of Heine--Borel,” and “comparability of countable
  well-orders” are topic phrases, not fixed coded sentences.  Variants of
  Heine--Borel and well-order comparability do not all have one reverse-
  mathematical strength; the representation and quantifiers are load-bearing.
- **Concrete harm:** neither the strict-ladder theorem nor the claimed sample
  reversals can be applied to the locally defined systems without importing an
  unstated version of \(\mathsf{RCA}_0\) and unstated theorem formulations.
  This also falls short of N-a-030/A-056's requirement for representative
  **equivalent theorems**, rather than subject labels.
- **Exact correction:** state the common two-sorted signature and basic
  discrete ordered-semiring axioms; give the \(\Sigma^0_1\)-induction and
  \(\Delta^0_1\)-comprehension schemes with free parameters and side
  conditions.  Then replace each “sample equivalent” cell by one exact coded
  theorem and a cited equivalence over that base (for example the precise
  injection-range principle for \(\mathsf{ACA}_0\)), or weaken the header to
  “informal subject examples” and separately supply the registered exact
  calibration table.  Preserve the countable-coded-object boundary at lines
  57-59.
- **Status:** open

### F5 [blocker] [open] Registered Part V depth commitments are absent or below their promised treatment

- **Author:** arithmetic/proof-theory topic specialist, R1
- **Criterion:** completeness for all Part V register commitments and declared
  treatment ceilings
- **Location:**
  - commitments:
    `spec/registers/new-content.csv:27-31` and
    `spec/registers/depth-gaps.csv:57-59`;
  - current GL:
    `handbook/parts/p05/provability-logic-gl.tex:1-74`;
  - current Paris--Harrington:
    `handbook/parts/p05/independence-catalog.tex:11-29`;
  - current reverse-mathematics survey:
    `handbook/parts/p05/reverse-mathematics.tex:9-93`.
- **Claim/evidence:**
  - N-a-026 requires a Guaspari--Solovay \(R\) pointer in addition to the
    already inherited Rosser witness comparison.  No Guaspari--Solovay entry or
    citation occurs in the routed Part V graph.
  - N-a-027 requires a sketch-level indicator/model-theoretic unprovability
    route and an exact “ACA context.”  The current Paris--Harrington theorem is
    only a cited two-sentence statement plus a vague reference to reflection
    and ordinal growth.  It supplies neither registered route nor an identified
    stronger theory.  The intended “ACA” must be disambiguated: it cannot
    silently mean \(\mathsf{ACA}_0\), whose first-order consequences are
    conservative over PA and hence do not include the PA-unprovable
    Paris--Harrington sentence.
  - N-a-028 asks for the Goodstein/hydra treatment; F2 identifies why the
    current object/rules do not reach that ceiling.
- **Concrete harm:** even after the OPEN notices were removed, the artifact
  would not be complete for the register that the charter makes part of
  admission.  The omission is reader-substantive, not generated metadata.
- **Exact correction:** add a bounded, sourced Guaspari--Solovay pointer with
  its standing and relation to the ordinary Rosser predicate; supply the
  registered Paris--Harrington proof architecture and name the exact stronger
  theory that proves the formalized principle, correcting the register if its
  “ACA” phrase would otherwise denote \(\mathsf{ACA}_0\); complete F2's
  Goodstein/hydra object definitions.  Record each register disposition rather
  than treating mere chapter presence as closure.
- **Status:** open

### F6 [blocker] [open] Five required Part V apparatus artifacts are missing and two existing surrogates are incomplete

- **Author:** arithmetic/proof-theory topic specialist, R1
- **Criterion:** registered tables/figures/rule-sheet completeness
- **Location:**
  - apparatus commitments:
    `spec/registers/apparatus.csv:13,54-58,129`;
  - current Q/PA definitions:
    `handbook/restoration/inherited-09099-09111.tex:1-12` and
    `handbook/restoration/inherited-09175-09187.tex:2-12`;
  - current independence tabular:
    `handbook/parts/p05/independence-catalog.tex:101-112`;
  - current reverse table:
    `handbook/parts/p05/reverse-mathematics.tex:40-55`;
  - current GL sheet:
    `handbook/registry/calculi/hilbert-gl.tex:1-4`.
- **Claim/evidence:**
  - A-053's Q/PA axiom table is absent; the two exact definitions are correct
    but do not instantiate the required comparison table.
  - A-054 requires G"odel and Rosser sentences, \(\mathsf{Con}\) statements,
    Paris--Harrington, and Goodstein with their independence bases.  The current
    unlabelled tabular omits G"odel and Rosser entirely and has no
    sentence/base/hypothesis comparison for them.
  - A-055's Presburger/Skolem decision-procedure and complexity table is absent.
  - A-057's GL-modal-principle/arithmetical-reading dictionary is absent.
  - A-128's Big Five inclusion figure with representative theorems is absent.
  - A-056 has a table-shaped surface, but F4 explains why its “equivalent” cells
    are not exact theorem statements.
  - A-012's GL sheet gives the inherited K base plus L"ob's axiom, but does not
    cross-reference the arithmetical realization and Solovay theorem required
    by its register specification.
- **Concrete harm:** the book lacks retrieval/comparison artifacts that the
  register classifies as must/should deliverables.  Prose chapters cannot
  silently stand in for tables or a figure, and an uncaptioned incomplete
  tabular cannot carry A-054's specified rows.
- **Exact correction:** create the five absent artifacts and finish A-012/A-056
  against their literal register schemas, each with one public label and
  references to existing theorem owners rather than duplicate theorem
  statements.  If any apparatus item is intentionally deferred to a later
  global route, record that disposition and keep Part V unadmitted until it is
  reachable; do not call it present because its source prose exists.
- **Status:** open

### F7 [should-fix] [open] The interpretability-logic pointer targets a chapter that contains no interpretability logic

- **Author:** arithmetic/proof-theory topic specialist, R1
- **Criterion:** truthful cross-part claims and fetchable navigation
- **Location:**
  `handbook/parts/p05/models-and-interpretability-supplement.tex:220-223`;
  target `handbook/parts/p05/independence-catalog.tex:1-113`.
- **Claim/evidence:** the supplement says that interpretability logic's calculi
  and completeness theory are outside the chapter and directs the reader to
  both Visser and “Chapter `sec:p05-independence-catalog`.”  That target chapter
  contains Paris--Harrington, Goodstein/hydra, Tennenbaum architecture, and
  presentation-dependent consistency, but no interpretability-logic calculus,
  semantics, or completeness result.
- **Concrete harm:** the public reference promises a destination that does not
  answer the stated topic.  It also creates the appearance that N-a-029's
  interpretability-logic pointer has an in-book target when only the external
  Visser citation is relevant.
- **Exact correction:** remove the unrelated chapter reference and retain the
  exact external pointer, or add a labeled, bounded interpretability-logic
  pointer at the cited destination and reference that label directly.  Do not
  conflate provability logic GL with interpretability logic.
- **Status:** open

## Checked-clean mathematical areas

### Lot 1 — Q/PA, representation, coding, diagonalization, first incompleteness

- The seven displayed Robinson-Q axioms and absence of induction at
  `inherited-09099-09111.tex:1-12` are correct for the fixed arithmetic
  signature.  PA as Q plus the universal closure of the full induction scheme
  has the correct parameter side condition at
  `inherited-09175-09187.tex:2-12`.
- I checked every step of the two complete Q lemmas.  Their object-language
  order expands as \(r\leq t\equiv\exists z(z+r=t)\); the base and successor
  cases at `inherited-09112-09149.tex:20-38` and
  `inherited-09150-09174.tex:12-25` use the right-recursion axioms in the
  correct orientation.
- The compactness construction at `inherited-09188-09261.tex:16-39` really
  produces a nonnumeral element, and downward L"owenheim--Skolem preserves it
  in a countable elementary submodel.  The AC hypothesis is explicit.
- Numeralwise relation representation, total-function representation, and the
  primitive-recursive/c.e. theorem at
  `inherited-09262-09327.tex:4-48` keep standard tuples distinct from a
  universally quantified internal decision claim.  The addition example is
  valid in Q without induction.
- The coding chapter correctly distinguishes a c.e. axiom set from its
  deductive closure, uses enumeration-stage certificates to make proof
  checking primitive recursive, and types provability as a Sigma-one formula.
  Its arithmetization theorem is honestly marked proof sketch.
- The diagonal construction at `inherited-09439-09497.tex:7-52` has the right
  substitution function, fixed-point sentence, and representability
  dependency.  The complexity-preserving Pi-one refinement is cited rather
  than silently proved.
- The G"odel proof plan correctly separates consistency for
  \(T\nvdash G_T\), Sigma-one soundness for
  \(T\nvdash\neg G_T\), and omega-consistency as an alternative.  The truth of
  \(G_T\) under consistency is derived through the Q-level biconditional, not
  from T-soundness.
- Both branches of the Rosser proof were checked.  The least proof codes,
  positive/negative numeralwise representation, bounded-case enumeration, and
  Q-dichotomy establish independence from consistency alone without producing
  a metatheoretic proof of the opposite sentence.  The theoremhood-undecidable
  corollary's completion construction correctly uses the assumed theoremhood
  decider to decide consistency of each finite extension.

### Lot 2 — nonstandard PA, Sigma-one completeness, interpretation

- The finite-distance relation is external and has the correct countable PA
  order decomposition \(\omega+\sum_{q\in\mathbb Q}\mathbb Z\).  The
  uncountable quotient caveat is correct.
- Overspill has the internal-formula/parameter hypothesis, its stronger
  initial-segment form is valid, and countability is not assumed.  The example
  deriving a nonstandard \(b<c\) and nondefinability of the standard cut is
  sound.
- Tennenbaum's theorem is stated with its exact simultaneous computability of
  transported addition and multiplication; it does not falsely deny a
  computable copy of the reduct order.
- Both clauses of the Sigma-one-completeness theorem are correct: true closed
  Sigma-one sentences are Q-provable, and PA proves each formalized schema
  \(\sigma\to\mathrm{Prov}_{PA}(\ulcorner\sigma\urcorner)\).  The annex
  explicitly enumerates its omitted bounded-formula induction, normal-form,
  proof-code constructor, substitution invariant, and PA verification, so its
  `sketched` status is honest.  F1 concerns admission prose, not a silent proof
  upgrade.
- The one-dimensional parameter-free interpretation definition handles
  quotient equality, function graphs, totality/closure, and uniqueness modulo
  the equivalence relation.  The proof- and consistency-transfer directions
  are correct; essential undecidability, rather than plain undecidability, is
  the needed effective-extension hypothesis.

### Lot 3 — derivability, L"ob, G"odel II, Tarski

- D1 is correctly metalinguistic while D2/D3 are internal schemes.  The formal
  consistency sentence is tied to the fixed proof predicate and false
  arithmetic sentence.
- The complete L"ob proof at `inherited-09817-09876.tex:18-59` correctly
  obtains internalized modus ponens from D2, positive introspection from D3,
  uses the assumed local reflection only for the target formula, and closes by
  D1.
- G"odel II at `inherited-09877-09924.tex:15-28` applies L"ob only after the
  assumed Con sentence yields
  \(\mathrm{Prov}_T(\ulcorner\bot_A\urcorner)\to\bot_A\); consistency then
  supplies the contradiction.  Its warning about nonstandard weak predicates
  and its relative-consistency example have the right scope.
- Tarski's proof at `inherited-09925-09992.tex:23-40` uses the Q-level liar
  biconditional and standard truth biconditional in the correct semantic
  structure.  The nondefinability and non-c.e. corollary follows from the
  cited Sigma-one definability of c.e. sets.  The bounded-complexity partial
  truth caveat is correct.

### Lot 4 — modal/decidable/independence/reverse statements

- GL is the normal K calculus plus L"ob's axiom with theorem-only
  necessitation.  Finite transitive irreflexive frames validate GL; finiteness
  makes converse well-foundedness automatic.  The modal fixed-point theorem
  retains its modalized-variable hypothesis.  F3 concerns the arithmetical
  base hypothesis, not these modal claims.
- Presburger arithmetic has the right additive standard structure and obtains
  quantifier elimination after congruence predicates are added.  The residue
  example is correct.  The Fischer--Rabin complexity warning does not confuse
  decidability with tractability.
- Skolem arithmetic uses the positive multiplicative domain, correctly maps
  prime exponent vectors to a weak direct power of addition, and states the
  published elementary-recursive triple-exponential-space upper bound without
  calling it practical.
- The Paris--Harrington statement has the necessary largeness condition
  \(|H|\geq\min H\), and its PA-independence theorem does not claim a stronger
  base result.  F5 is about the missing registered proof route/context.
- Presentation-dependent consistency correctly distinguishes an external
  derivability fact from the internal sentence and limits G"odel II to proof
  predicates satisfying the derivability conditions.
- The Big Five inclusion order and strictness claim are correct in the usual
  metatheory, and the chapter explicitly warns that the five systems do not
  exhaust reverse-mathematical strength.  F4 concerns exact definitions and
  equivalence rows, not the ladder direction.

## Structural/evidence checks

- Reachability: **46 files** — two roots, nineteen wrappers, nineteen exact
  inherited units, five editorial bodies, one editorial annex.
- Exact intervals: **19/19** wrappers target the matching inherited interval,
  and all nineteen inherited line counts equal their closed intervals.
- Reachable labels/entry owners: **79**, with no duplicate in the Part V graph.
- Static Part V references: **15**, all have matching labels in the handbook
  tree; F7 is a semantic destination defect, not an undefined label.
- Citation/status keys: **28**, all present in
  `handbook/bib/handbook.bib`.
- Editorial proof reciprocity: one `sketched=annex:p5.sigma.1` declaration and
  one matching annex item, with an explicit omissions note; no orphan pair.
- Not checked by instruction: compilation, generated harvest output, rendered
  page/figure quality, external source-fidelity comparison beyond the exact
  interval/wrapper evidence, human review, administrative admission, and user
  acceptance.

## Prioritized repair checklist

1. **P0 — make the mathematical objects and hypotheses exact:** repair the
   Goodstein recurrence/hydra rule (F2), state the Solovay base/soundness/proof-
   predicate hypotheses (F3), and fix the RCA0 schemes plus exact reversal
   statements (F4).
2. **P0 — complete or explicitly disposition the registered source content:**
   supply N-a-026/N-a-027/N-a-028 at their declared ceilings, including a
   mathematically valid resolution of the ambiguous “ACA context” (F5).
3. **P0 — deliver the registered retrieval apparatus:** A-053, A-054, A-055,
   A-057, and A-128; finish A-012 and A-056 without duplicating theorem owners
   (F6).
4. **P0 — only after 1--3, replace the two rendered OPEN/unadmitted notices**
   with ordinary attribution and exact status, preserving body/annex
   reciprocity (F1).
5. **P1 — correct the false interpretability-logic chapter destination** or
   add the bounded pointer it promises (F7).
6. Re-run source/content review.  Keep build, visual, generated-table, human,
   administrative, and user gates separate.

## Scope conclusion

All four charter lots, all nineteen exact source units, every routed editorial
body/annex addition, every theorem/proof status, and the Part V depth/apparatus
commitments named above were checked.  The inherited core is sound at its
declared complete/cited/sketch boundaries.  **Source/content admission is
blocked by F1, F5, and F6; F2--F4 are mathematical must-fixes, and F7 is a
concrete navigation correction.**

# Round 1 blind opening — computability/complexity topic specialist

## Verdict

**Do not admit Part IV in its present source/content state.** I record two
blockers and ten must-fix findings.  The exact inherited computation,
reduction, arithmetization, and jump sequence is mathematically coherent at its
declared proof ceilings.  The blockers are in routed editorial material: five
body/annex surfaces explicitly deny admission, and the frontiers chapter
expressly leaves two registered subjects as pointer-only entries.

I read the charter before the artifact and did not read any other Part IV
seat's transcript.  I reviewed the complete live graph rooted at
`handbook/parts/p04.tex` and `handbook/annex/p04.tex`: two roots, seventeen
exact-source wrappers, seventeen inherited targets, six body additions, and
two annex additions, forty-four reachable files in all.  I also inspected the
governing reader-layout definition solely to settle whether the exact source
`\part{Computability}` creates an extra public part; it does not—the provenance
scope intercepts it as a governed unnumbered source chapter.  I made no
manuscript, control, test, or generated-file edit and ran no build or test.

## Findings

### F1 [blocker] [open] Accepted reader sections explicitly remain OPEN and unadmitted

- **Author:** computability/complexity topic specialist, R1
- **Criterion:** no reader-visible OPEN, unadmitted, owed, stub, pointer-only
  substitute, or internal workflow ID
- **Location:**
  - `handbook/parts/p04/machines-effective-procedures-supplement.tex:5-11`
  - `handbook/parts/p04/universal-reductions-supplement.tex:5-11,39-43`
  - `handbook/annex/p04/universal-reductions-supplement.tex:4-6`
  - `handbook/parts/p04/decision-hierarchy-apparatus-supplement.tex:4-9`
  - `handbook/parts/p04/degrees-and-priority-continuation.tex:14-16`
  - `handbook/annex/p04/degrees-and-priority-continuation.tex:14-16`
- **Claim/evidence:** These are rendered headings and reader paragraphs, not
  source comments.  They say `OPEN`, `unadmitted`, `pending every ... gate`,
  and expose R-035, D-P5-001, D-P5-002, N-a-063, A-045, A-154, A-155,
  A-163, A-189, and A-196.  The universal proof and Friedberg--Muchnik annex
  expressly say they close no admission gate.
- **Concrete harm:** Part IV cannot satisfy the charter while accepted reader
  pages deny their own admission.  The problem is not cured by deleting the
  words: that would conceal rather than settle the governing obligations.
- **Exact correction:** For each routed unit, either complete and record its
  governing admission, replace workflow prose by ordinary attribution and
  exact proof/source status, and keep body/annex disposition reciprocal; or
  remove the body and matching annex input from the accepted route.  Do not
  declare any listed register closed merely because text is present.
- **Status:** open

### F2 [must-fix] [open] The purported exact URM has no total operational semantics

- **Author:** computability/complexity topic specialist, R1
- **Criterion:** definition before use; exact machine side conditions and
  theorem domain
- **Location:**
  `handbook/parts/p04/machines-effective-procedures-supplement.tex:116-138`,
  especially lines 119-125 and the equivalence table at lines 169-175
- **Claim/evidence:** The definition lists `D(n)` only as “decrement a nonzero
  register,” but never says what a run does if it reaches `D(n)` with zero.
  It uses `J[E_1]` and `J(m)[E_1]` without typing an exit, defining which line
  `E_1` denotes, or specifying the normal/selected exit map of a finite
  program.  “Begin at line 1” and “halt after the last instruction” do not
  fill those transition cases.
- **Concrete harm:** A finite instruction list does not determine a unique run,
  so “does not stop,” “stops,” and “computes” in lines 127-132 are not defined
  for every program/input.  The equivalence row cannot denote one exact
  machine model.  In the primary source, decrement has the explicit
  nonzero precondition and jumps target declared exits; see Shepherdson and
  Sturgis, [*Computability of Recursive
  Functions*](https://www.cs.cmu.edu/~cdm/projects/ShepherdsonSturgis1963.pdf),
  pp. 219-222.
- **Exact correction:** Define a URM program as a finite control-flow object
  with typed exit targets and a unique next instruction in every enabled case.
  Either make reaching `D(n)` at zero an explicitly invalid/stuck/divergent
  run, or impose and state a well-formedness invariant that it is executed only
  when positive.  Define the two exits of each conditional jump, halting, and
  the strong register-preservation computation convention before asserting the
  equivalence row.
- **Status:** open

### F3 [must-fix] [open] The hierarchy theorems omit the lower bounds built into their cited constructibility hypotheses

- **Author:** computability/complexity topic specialist, R1
- **Criterion:** exact theorem hypotheses and complexity model
- **Location:**
  `handbook/parts/p04/complexity.tex:73-82,113-143`
- **Claim/evidence:** The local definitions allow arbitrary time- and
  space-constructible functions.  The deterministic time hierarchy is then
  stated without the standard at-least-linear time range, and the deterministic
  space hierarchy without requiring the larger space bound to be at least
  logarithmic.  The cited classical forms impose those ranges (or build them
  into the word “constructible”).  An authoritative summary states time bounds
  at least `n` and space bounds at least `log n`: [Encyclopedia of Mathematics,
  “Computational complexity classes”](https://encyclopediaofmath.org/wiki/Computational_complexity_classes).
  The original space source is [Stearns--Hartmanis--Lewis
  1965](https://doi.org/10.1109/FOCS.1965.11).
- **Concrete harm:** The source citation does not license the universal
  statements under the manuscript's broader locally defined term.  The
  polynomial/exponential corollaries are within the safe range, but the stated
  general theorems are underhypothesized.
- **Exact correction:** Either add `f(n) >= n` to time constructibility and
  `f(n) >= log n` to space constructibility, or retain the broad definitions
  and add the applicable lower bounds explicitly to the hierarchy theorems
  (at minimum, the larger time/space bounds).  Keep Savitch's already stated
  `f(n) >= log n` condition.
- **Status:** open

### F4 [blocker] [open] Two admitted frontier entries are expressly pointer-only substitutes

- **Author:** computability/complexity topic specialist, R1
- **Criterion:** no pointer-only substitute; completeness for registered scope
- **Location:**
  - Omega: `handbook/parts/p04/frontiers-of-computability.tex:268-301`
  - computable structures:
    `handbook/parts/p04/frontiers-of-computability.tex:479-505`
- **Claim/evidence:** The Omega definition calls itself “only the
  halting-probability pointer,” and the table repeats “pointer only.”  The
  computable-presentation entry calls itself a “reading pointer,” says it is
  not an existence theorem, and explicitly says it does not discharge a
  registered model-theory construction.  The final ceiling repeats that the
  entry is a pointer.
- **Concrete harm:** These pages positively certify reader construction debt.
  The computable-presentation text also duplicates the already reader-visible
  Part III definition rather than supplying a Part-IV index-set theorem.
- **Exact correction:** For each entry, either remove it from the admitted
  route/register or provide the owed, sourced artifact.  For Omega, state an
  exact theorem at the chosen ceiling (at least Kraft convergence and the
  exact computability/randomness claim actually intended).  For computable
  structures, cross-reference the Part III definition and state one exact
  index-set/presentation theorem with its coding, isomorphism closure, and
  proof status.  Do not invent an unsupported family-wide claim.
- **Status:** open

### F5 [must-fix] [open] The two final editorial chapters are not visibly editorial

- **Author:** computability/complexity topic specialist, R1
- **Criterion:** editorial content must be sourced and visibly distinct from
  inherited source
- **Location:**
  - routes: `handbook/parts/p04.tex:24-25`
  - `handbook/parts/p04/frontiers-of-computability.tex:1-15`
  - `handbook/parts/p04/complexity.tex:1-13`
- **Claim/evidence:** Their Phase/register/editorial standing appears only in
  `%` comments.  The rendered chapters begin as ordinary handbook prose and
  give no reader note saying they are separately authored, which sources
  control them, or that they do not replace the exact inherited sequence.
- **Concrete harm:** A reader cannot distinguish exact inherited source from
  later editorial survey content, contrary to the charter.  The many
  theorem-level citations do not themselves identify provenance of the whole
  chapter.
- **Exact correction:** Add a rendered attribution/nonreplacement/scope note at
  the start of each chapter, with the controlling primary/systematic sources,
  or put both beneath one rendered editorial-supplement preface that
  unambiguously governs them.  Retain theorem-level citations.
- **Status:** open

### F6 [must-fix] [open] “Jump strictly increases every degree” lacks its lower comparison

- **Author:** computability/complexity topic specialist, R1
- **Criterion:** exact theorem consequence and proof dependencies
- **Location:**
  - jump definition and derived degree operation:
    `handbook/parts/p04/degrees-and-priority-continuation.tex:41-61`
  - asserted strict-increase row: same file, lines 250-260
  - inherited jump theorem:
    `handbook/restoration/inherited-08898-09079.tex:88-124`
- **Claim/evidence:** The inherited theorem proves that `B'` is c.e. in `B`
  and `B' not <=_T B`.  It never states or proves `B <=_T B'`.  Nonreducibility
  in one direction gives inequality, not the comparability needed for
  `deg(B) < deg(B')`.  The omitted fact is standard—every set is reducible to
  its jump—but it is a separate uniform coding step; compare the Jump Theorem
  discussion in [Chung, *An Introduction to Computability
  Theory*](https://math.uchicago.edu/~may/REU2014/REUPapers/Chung.pdf).
- **Concrete harm:** The table's order-theoretic conclusion does not follow
  from its cited local theorem/remark package.  This is not a stylistic request:
  `<` requires both `<=` and non-equality.
- **Exact correction:** Add the uniform lemma `B <=_m B'`: from `n`, compile an
  oracle-`B` program that ignores its self-input, queries `n`, and accepts with
  a valid output exactly on a yes answer.  Relativized parameterization makes
  the index map total computable.  Combine that lemma with `B' not <=_T B`
  before defining/claiming strict degree increase.
- **Status:** open

### F7 [must-fix] [open] The route creates two owners and two notations for existing concepts

- **Author:** computability/complexity topic specialist, R1
- **Criterion:** editorial nonduplication; definition before use; one technical
  name per exact concept
- **Location:**
  - exact Kleene equality:
    `handbook/restoration/inherited-07851-08048.tex:49-52`
  - duplicate editorial convention and false first-use claim:
    `handbook/parts/p04/machines-effective-procedures-supplement.tex:30-38`
  - false “next chapter” claims: same file, lines 109-114 and 154-160
  - exact many-one equivalence:
    `handbook/restoration/inherited-08898-09079.tex:153-157`
  - unused duplicate `sim_m`:
    `handbook/parts/p04/universal-reductions-supplement.tex:28-43`
- **Claim/evidence:** All exact wrappers are routed before the supplements.
  Consequently the reader has already received the exact `simeq` convention
  before the supplement defines it again, and the bespoke program-numbering
  chapter is preceding rather than “next.”  The universal supplement then
  introduces `sim_m` for the same mutual many-one relation already called
  `equiv_m`; no reachable later statement uses `sim_m`, despite a source
  comment pointing to the unrouted historical file.
- **Concrete harm:** The reader gets duplicate owners, a false route narrative,
  and two symbols for one relation.  The latter also fails the workspace rule's
  actual-use requirement for new technical names.
- **Exact correction:** Remove the duplicate Kleene-equality environment and
  refer to the exact preceding convention; change “next chapter” to the actual
  preceding-source relationship.  Delete the unused `sim_m` paragraph and use
  the exact `equiv_m` owner wherever mutual many-one reducibility is genuinely
  required.
- **Status:** open

### F8 [must-fix] [open] The machine/mu-recursion equivalence has a typed-mu gap and an unhandled nullary edge

- **Author:** computability/complexity topic specialist, R1
- **Criterion:** typed definitions; equivalence theorem coverage
- **Location:**
  - minimization and partial-recursive class:
    `handbook/parts/p04/machines-effective-procedures-supplement.tex:40-67`
  - normal form and equivalence: same file, lines 69-101
  - local-numbering bridge:
    `handbook/parts/p04/universal-reductions-supplement.tex:13-25`
  - nullary Turing-function support:
    `handbook/restoration/inherited-07506-07677.tex:92-109,125-133`
- **Claim/evidence:** First, `mu` is defined only on a partial numerical map
  `g`, selecting its first defined zero.  The normal form then applies `mu y`
  directly to `T_k`, which is declared a relation, and says it selects the first
  *satisfying* code.  That predicate binder has not been defined or reduced to
  the zero-search operator.  The authoritative normal-form presentation
  explicitly extends minimization to relations before stating the theorem:
  [SEP, “Recursive Functions,” section 2.2.2](https://plato.stanford.edu/archives/win2021/entries/recursive-functions/).
  Second, both machine and recursive-function definitions admit arity zero,
  but normal form, TM equivalence, enumeration, and the bridge all require
  `k >= 1`.  Kleene's standard theorem is for `k in N`; the original URM
  source also explicitly includes functions of zero arguments.
- **Concrete harm:** The normal-form display is ill-typed under the only local
  `mu` definition, and the promised equivalence leaves nullary partial
  constants without a classification/index realization.
- **Exact correction:** Define predicate minimization eliminably as the least
  satisfying witness (equivalently minimize a primitive-recursive zero-on-true
  characteristic function).  Extend normal form/equivalence/range to `k=0`,
  including the trivial compiler/alphabet case, or explicitly remove nullary
  maps from the two compared classes and document that ceiling consistently.
- **Status:** open

### F9 [must-fix] [open] FO(LFP) is used without formation or semantics

- **Author:** computability/complexity topic specialist, R1
- **Criterion:** definition before use; exact side conditions
- **Location:**
  `handbook/parts/p04/complexity.tex:351-423`, especially the capture theorem
  at lines 386-390
- **Claim/evidence:** The text expands the abbreviation as “first-order logic
  with a least fixed-point operator” only after the theorem.  No earlier live
  handbook definition states the arity of the relation variable, formation of
  an LFP formula, positivity/monotonicity, iteration from the empty relation,
  or satisfaction.  Positivity is load-bearing: without it the induced operator
  need not be monotone and a least fixed point need not exist.  See Immerman's
  authoritative account, [“Descriptive
  Complexity”](https://www.ams.org/journals/notices/199510/immerman.pdf).
- **Concrete harm:** The expression whose model classes allegedly capture
  `P` is not a defined logic, so neither side of the capture definition can be
  applied to the theorem.
- **Exact correction:** Before the theorem, define FO(LFP) with a fresh
  `r`-ary relation variable occurring only positively, the monotone operator
  it induces on subsets of `M^r`, the least fixed point obtained by iteration
  from the empty relation on finite structures, and the formula/satisfaction
  clause.  Then retain the built-in-total-order theorem.
- **Status:** open

### F10 [must-fix] [open] Algorithmic-information terms and the Kraft step are undefined

- **Author:** computability/complexity topic specialist, R1
- **Criterion:** definition before use; exact proof dependency
- **Location:**
  `handbook/parts/p04/frontiers-of-computability.tex:197-301`
- **Claim/evidence:** `prefix-free` is used to define `K_V`, optimal universal
  simulation, and Omega but is never defined.  “Upper semicomputable” occurs
  only in the noncomputability theorem and table, without a standing or
  approximation convention.  The Omega paragraph invokes Kraft's inequality
  to prove convergence/measure without stating or locally citing that result.
- **Concrete harm:** The domain restriction on the universal machine, the
  approximation classification of `C` and `K`, and the convergence of the
  displayed real cannot be checked from the local definitions.
- **Exact correction:** Define prefix-free sets of strings (`p != q` implies
  neither is a prefix of the other); define upper semicomputability by a total
  computable nonincreasing integer approximation converging pointwise; and
  state/cite the Kraft bound `sum 2^(-len p) <= 1` before using it.  Then keep
  the invariance, semicomputability, and Omega ceilings distinct.
- **Status:** open

### F11 [must-fix] [open] Chaitin's theorem has a non-eliminable theory-strength placeholder

- **Author:** computability/complexity topic specialist, R1
- **Criterion:** exact hypotheses and theorem strength
- **Location:**
  `handbook/parts/p04/frontiers-of-computability.tex:258-266`
- **Claim/evidence:** `T` is required to be “capable of formalizing the
  relevant finite computations,” but no language, arithmetic base, proof
  predicate, representation condition, or eliminable definition tells the
  reader which theories satisfy that phrase.  The following soundness clause
  is precise, but it does not define the preceding capability hypothesis.
- **Concrete harm:** Applicability of the stated bound is undecidable from the
  theorem's own hypotheses, and two readers may import different strengths
  while citing the same result.
- **Exact correction:** Fix the arithmetic coding and replace the placeholder
  by an explicit base, for example a computably axiomatized extension of the
  named Robinson arithmetic capable of representing the fixed computation
  predicate, together with soundness for the displayed (Pi-one) complexity
  lower-bound sentences.  State exactly which soundness assumption the cited
  proof uses; do not substitute mere consistency.
- **Status:** open

### F12 [must-fix] [open] The “exact encoded-instance” catalog never fixes three encodings

- **Author:** computability/complexity topic specialist, R1
- **Criterion:** exact inputs, reductions, and yes predicates
- **Location:**
  `handbook/parts/p04/frontiers-of-computability.tex:304-446`, especially the
  catalog claim at lines 393-400 and the polynomial, presentation, and tile
  rows at lines 419-437
- **Claim/evidence:** The chapter promises that every row fixes an *encoded*
  instance, but it gives abstract finite objects only: an integer-coefficient
  polynomial, words for a fixed presentation, and a finite Wang-tile set.  It
  fixes each yes predicate well, but gives no serialization, computable
  validity predicate, or coding-invariance statement for these finite inputs.
- **Concrete harm:** The rows are not literally languages/subsets of natural
  numbers, despite the chapter's opening promise that a formal model, input
  encoding, and yes predicate have been fixed.  This matters whenever a
  reduction or c.e./decidable status is transported.
- **Exact correction:** Declare one standard effective coding: sparse
  coefficient/exponent tuples for polynomials, the existing finite-string code
  for words over each fixed finite generator alphabet, and canonically relabeled
  finite color/edge tuples for tile sets.  Alternatively state and justify that
  each result is invariant under any computably intertranslatable standard
  coding, and weaken the caption from “fixes an encoded instance.”
- **Status:** open

## Structural and evidence checks

- Recursive reachability produced **44 files**: two roots, seventeen wrappers,
  seventeen inherited units, six body additions, and two annex additions.
- All **17/17** `scope-SRC-*` wrappers target the matching inherited interval,
  and every inherited target's line count equals its closed interval length.
- Reachable labels: **73**, with no duplicate label in the Part IV graph.
- Proof reciprocity: two status-bearing annex declarations and two matching
  annex items, with no missing or orphan item.  Both paired items are among the
  OPEN material recorded in F1.
- Citation/status keys: **51**, all present in
  `handbook/bib/handbook.bib`.
- The public Part-IV driver plus exact source `part` token do not double-render:
  `inheritedrestorationscope` intercepts provenance `SRC-07494-07505` and turns
  the exact source title into a subordinate attributed chapter while leaving
  the public part counter unchanged.

## Four-lot coverage

| Lot | Checked clean | Findings | Not checked |
|---|---|---|---|
| 1. Machines, effective procedures, mu-recursion, formal equivalence, Church--Turing | Read all exact units `07494-07505` through `07844-07850` and the full machines supplement.  Checked deterministic transition/configuration semantics, binary/tuple I/O, partial-function convergence, primitive recursion, c.e./decidable equivalences, the definedness-sensitive mu scheme, normal-form theorem statement, formal/informal Church--Turing boundary, and the machine-equivalence table.  The inherited machine and c.e. proofs are coherent at their stated complete/sketch statuses. | F1, F2, F7, F8 | Full reproof of the cited Turing/mu/lambda/URM equivalence; build/landscape rendering. |
| 2. Universal computation, reductions, decision problem, arithmetical hierarchy | Read exact units `07851-08048` through `08898-09079`, plus the universal body/annex and apparatus.  Checked bespoke numbering adequacy, universal simulation, s-m-n arities, halting reductions, recursion theorem calculation, Rice proof, many-one direction, formula/relation hierarchy standing, beta coding, pairing contraction, bounded collection, every prefix-normal-form proof branch, bounded history ceiling, K/TOT classifications, strictness, oracle conventions, relativized diagonal, Post's theorem, and jump convention bridge. | F1, F6, F7, F8 | Full external proofs of cited completeness/strictness/Post results; build/reference resolution. |
| 3. Degrees, priority, simple/creative sets | Read the continuation and annex completely.  Checked degree quotient/join well-definedness, Kleene--Post versus c.e. scope, every Friedberg--Muchnik requirement/action/restraint case, finite-injury induction and declared omissions, intermediate-degree consequences, acceptable numbering, simple/productive/creative definitions, Myhill strength, Rice--Shapiro finite-positive-information statement, table, and figure ceilings. | F1, F6 | The omitted primitive-recursive scheduler/compiler and stage-state coding are correctly declared not checked by the sketch; visual figure inspection. |
| 4. Analytical/hyperarithmetical frontiers, information, undecidability, structures, complexity | Read both final chapters completely.  Checked lightface/function-parameter boundary, Kleene-O orientation, HYP/Delta-one-one, WF/IF coding and completeness directions, plain versus prefix complexity, counting bound, MRDP domain translations, fixed word problems, whole-plane tiling, Busy Beaver convention, class/reduction definitions, PH quantifier parity, Cook--Levin/QBF completeness, class-ladder inclusions and 2026 open-status claims, finite-structure capture definition, Fagin, and the ordered Immerman--Vardi hypothesis.  The open complexity claims remain current; compare the [Spring 2026 SEP survey](https://plato.stanford.edu/archives/spr2026/entries/computational-complexity/). | F3-F5, F9-F12 | Full proofs of citation-only analytical, MRDP, word/tiling, Busy Beaver, Kolmogorov, hierarchy, completeness, and descriptive-complexity theorems; build, tables/figures visual QA. |

## Scope conclusion

All four charter lots and every reader-visible status statement in the live
Part IV graph were checked.  Source/content admission is **blocked by F1 and
F4**; F2-F3 and F5-F12 also require exact correction.  The inherited core's
complete proofs and the editorial finite-injury sketch are otherwise coherent
at their declared ceilings.  Build, visual, historical-source fidelity beyond
the wrapper/interval check, human review, administrative admission, and user
acceptance remain separate and were not inferred from this audit.

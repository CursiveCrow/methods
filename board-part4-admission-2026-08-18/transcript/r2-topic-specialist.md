# Round 2 — computability/complexity topic specialist

## Verdict

The repairs close the mathematical substance of R1 F1--F12.  In particular,
the live route now contains a total URM control semantics, a typed
definedness-sensitive minimization package at its explicit positive-arity
ceiling, exact constructibility ranges, the missing lower comparison
\(A\leq_m A'\), complete finite-extension and finite-injury arguments, actual
analytical complete sets, a proved Omega theorem, an index-uniform computable-
presentation corollary, and the requested complexity calibrators.  I actively
tried to refute the new proofs and classifications rather than accepting their
summaries.

Two narrow direct-repair defects remain in the bytes I reviewed:

1. the new succinct-QBF surface uses and encodes QBF before the local QBF
   formation/truth definition; and
2. the newly upgraded complete Omega proof invokes the undecidability of the
   fixed prefix-free universal machine's domain without proving it or pointing
   to a separately stated cited result.

Both are exact, local corrections.  I found no counterexample to the theorem
statements themselves.  Source/content admission should wait for those two
corrections, but none of R1's former blockers survives.

I re-read the charter and my own R1 record, then re-read the complete current
reader graph rooted at `handbook/parts/p04.tex` and
`handbook/annex/p04.tex`.  I did not read another Part IV seat's transcript.
The current graph has 45 reachable files: two roots, seventeen matching
source wrappers, seventeen exact inherited units, six routed body additions,
and three routed annex additions.  I made no manuscript, control, test, or
generated-file edit, and I ran no build or test.

## R1 record dispositions

### F1 — accept-fixed

- **Live evidence:**
  `handbook/parts/p04/machines-effective-procedures-supplement.tex:5-10`,
  `handbook/parts/p04/universal-reductions-supplement.tex:5-10`,
  `handbook/annex/p04/universal-reductions-supplement.tex:4-6`,
  `handbook/parts/p04/decision-hierarchy-apparatus-supplement.tex:4-8`,
  `handbook/parts/p04/degrees-and-priority-continuation.tex:14-18`, and
  `handbook/annex/p04/degrees-and-priority-continuation.tex:15-17` now give
  ordinary reader attribution and exact nonreplacement/proof standing.  None
  renders `OPEN`, `unadmitted`, a workflow ID, or a pending-gate notice.
- The sole uppercase `OPEN` left in the reachable graph is a source comment at
  `handbook/parts/p04.tex:80-83` explaining why an unreachable generated audit
  is not routed.  It is not reader-visible content and creates no admission
  claim.
- **Opposing test:** deleting the old notice words without settling the owed
  content would not have sufficed.  The subsequent records show that the
  mathematical obligations themselves, not merely their notices, are now
  supplied.

### F2 — accept-fixed

- **Live evidence:**
  `handbook/parts/p04/machines-effective-procedures-supplement.tex:116-148`.
  A program has lines \(1,\ldots,\ell\), all displayed exit placeholders are
  replaced by targets in \(\{1,\ldots,\ell+1\}\), line \(\ell+1\) is the
  halting exit, and the normal exit from line \(i\) is \(i+1\).  The six
  instruction forms have unique enabled transitions; in particular,
  \(D(n)\) has no transition at zero, so that run is explicitly undefined.
  Execution, halting, inputs, output, preserved registers, and scratch space
  are all fixed.
- **Counterexample recheck:** the R1 zero-register run is no longer
  ambiguous, and neither jump form contains an untyped target.  Thus each
  program/input has the exact operational behavior needed by the equivalence
  row at lines 179-185.

### F3 — accept-fixed

- **Live evidence:** `handbook/parts/p04/complexity.tex:78-88` defines time
  constructibility only for \(f(n)\geq n\) and space constructibility only for
  \(f(n)\geq\lceil\log(n+1)\rceil\).  The hierarchy statements at lines
  119-138 retain constructibility plus the respective
  \(f\log f=o(g)\) and \(f=o(g)\) gaps; Savitch's logarithmic lower bound is
  explicit at lines 140-149.
- These are the domains required by the cited hierarchy theorems, so the
  manuscript no longer quantifies over a broader locally defined class than
  its sources license.  The corollaries
  \(\mathsf P\subsetneq\mathsf{EXPTIME}\) and
  \(\mathsf{PSPACE}\subsetneq\mathsf{EXPSPACE}\) are valid.

### F4 — accept-fixed

- **Omega:** `handbook/parts/p04/frontiers-of-computability.tex:340-365`
  now defines the left-c.e. real, states left-c.e.-ness,
  noncomputability, and the exact finite-bit halting consequence, and points to
  a reciprocal annex proof at
  `handbook/annex/p04/frontiers.tex:25-51`.  This is no longer a pointer-only
  entry.  The remaining proof-status issue is the new F14 below, not the former
  missing artifact.
- **Computable structures:**
  `handbook/parts/p04/frontiers-of-computability.tex:606-627` uses the Part III
  definitions rather than duplicating them, defines a presentation index as a
  total atomic-diagram decider in the fixed numbering, and states a uniform
  compiler \(F(e,d)\).  The alternating effective back-and-forth proof at
  `handbook/annex/p04/frontiers.tex:3-23` searches the correct finite cuts in
  both directions, terminates under exactly the valid-presentation hypothesis,
  and obtains a total computable index compiler from the cited parameter
  theorem.  Invalid indices are correctly allowed to produce a partial
  compiled program.

### F5 — accept-fixed

- **Live evidence:** the rendered notes at
  `handbook/parts/p04/frontiers-of-computability.tex:7-11` and
  `handbook/parts/p04/complexity.tex:8-11` identify both chapters as separately
  authored, sourced extensions that do not replace the exact inherited
  sequence.  The theorem-level citations remain in place.
- A reader can now distinguish inherited restoration from editorial survey
  content without consulting source comments.

### F6 — accept-fixed

- **Live evidence:**
  `handbook/parts/p04/degrees-and-priority-continuation.tex:43-53` now isolates
  the proved lemma \(A\leq_mA'\) from the separately sourced diagonal
  nonreducibility conclusion.  In
  `handbook/annex/p04/degrees-and-priority-continuation.tex:19-37`, the map
  \(q(n)\) is a direct primitive-recursive finite-table compiler: its program
  ignores self-input, queries \(n\), writes \(0\) and accepts on yes, and loops
  on no.  Hence
  \[
    n\in A\quad\Longleftrightarrow\quad
    q(n)\in A'.
  \]
- The proof no longer invokes the inherited sketched relativized parameter
  theorem.  The strict comparison then combines this complete lower reduction
  with the separately cited complete source for \(A'\not\leq_TA\), so the
  `proved` tagline covers exactly the annex claim rather than silently
  upgrading the inherited sketch.

### F7 — accept-fixed

- The routed machines supplement has no second Kleene-equality owner; its
  current normal-form display avoids `\simeq` before the exact inherited owner.
  Its lines 109-114 distinguish the cited normal-form coding from the one
  handbook program numbering subsequently fixed by the inherited universal
  chapter.  The former false route narrative is gone.
- `handbook/parts/p04/universal-reductions-supplement.tex:5-25` now contains
  only the needed range bridge.  The unused second symbol for mutual many-one
  equivalence has been removed.  The sole reader owner remains the exact
  `\equiv_m` convention at
  `handbook/restoration/inherited-08898-09079.tex:153-177`.
- I initially suspected a forward Kleene-equality use, but a graph-restricted
  recheck disproved it: the similarly named
  `handbook/parts/p04/machines-effective-procedures.tex` is unreachable
  historical material, while the routed supplement itself contains no such
  use.  I therefore do not preserve that false objection.

### F8 — accept-fixed

- **Typed predicate minimization:**
  `handbook/parts/p04/machines-effective-procedures-supplement.tex:27-47`
  distinguishes minimization of a partial numerical map from the eliminable
  least-true notation for a total predicate via its zero-on-true numerical
  function \(z_R\).  The normal-form display at lines 67-88 is consequently
  typed.
- **Arity:** lines 49-65 expressly define the closure class only for positive
  arities, and both the normal-form and Turing-equivalence theorems quantify
  over \(k\geq1\).  The local-numbering bridge at
  `handbook/parts/p04/universal-reductions-supplement.tex:12-24` has the same
  domain.  R1 permitted either a nullary extension or a consistent explicit
  ceiling; the latter is now implemented without pretending to classify
  nullary maps.

### F9 — accept-fixed

- `handbook/parts/p04/complexity.tex:439-463` now defines FO(LFP) before the
  Immerman--Vardi theorem.  A fresh \(r\)-ary relation variable occurs only
  positively; the resulting \(F_{\bar b}:\mathcal P(M^r)\to\mathcal P(M^r)\)
  is monotone; the LFP formula's satisfaction clause is explicit; and finite
  iteration begins at the empty relation.  The constructor is correctly
  typeset as `\operatorname{lfp}`.
- The theorem at lines 471-475 retains the built-in total-order hypothesis.
  Thus the operator exists for the stated reason, and the capture claim is
  about a defined logic rather than an expansion of an abbreviation after use.

### F10 — accept-fixed

- `handbook/parts/p04/frontiers-of-computability.tex:226-259` defines
  prefix-free string sets and machines and states Kraft's inequality before
  using either in prefix complexity or Omega.
- Lines 294-307 define upper semicomputability both by a c.e. strict upper-cut
  and by a total computable nonincreasing approximation, including the fixed
  code/order convention for infinity.  The semicomputability theorem at lines
  309-312 now has a defined property.
- Lines 340-365 define left-c.e. separately from upper semicomputability and
  keep plain complexity, prefix complexity, and halting probability on their
  correct machine domains.  The numeric inequalities in the new Omega annex
  are correct: after the partial sum exceeds the \(n\)-bit lower truncation,
  its remaining mass is below \(2^{-n}\), so no unseen program of length at
  most \(n\) can halt.

### F11 — accept-fixed

- `handbook/parts/p04/frontiers-of-computability.tex:314-338` fixes the optimal
  prefix-free machine and arithmetic coding, gives a bounded computation
  predicate, requires a computably axiomatized theory with primitive-recursive
  proof relation that proves each true closed computation instance, defines
  the lower-bound sentence as \(\Pi^0_1\), and assumes \(\Pi^0_1\)-soundness.
- The conclusion quantifies exactly over provable sentences
  \(K_{U_K}(x)>n\), with a bound depending on the displayed theory, machine,
  proof relation, and coding.  No vague “capable of formalizing” placeholder or
  consistency-for-soundness substitution remains.

### F12 — accept-fixed

- `handbook/parts/p04/frontiers-of-computability.tex:469-481` fixes effective
  sparse polynomial codes, finite presentation/word codes, and Wang-tile tuple
  codes, using self-delimiting lengths; validity, decoding, and re-encoding are
  computable.  It also states the exact computable-intertranslation condition
  under which coding invariance is claimed.
- The word-problem and tile definitions at lines 483-517 still separately fix
  their yes predicates and domains.  Thus the catalog is literally about
  effective inputs rather than uncoded abstract objects.

## Direct-repair proofs and classifications

### Kleene--Post finite extension — checked clean

At `handbook/annex/p04/degrees-and-priority-continuation.tex:39-97`, the
requirements are now the typed function inequalities
\(\chi_A\not\simeq\varphi_e^B\) and
\(\chi_B\not\simeq\varphi_e^A\).  Lines 48-53 supply the needed compiler from
an oracle decider to a total numerical characteristic-function program, so
the requirements cover the manuscript's actual definition of Turing
reducibility (whose no cases reject).

The extension question at lines 59-74 is c.e. in the finite parameters; the
cited many-one completeness of \(K\), followed by the explicit query-free
compiler from \(K\) into the manuscript's definedness jump, lets
\(\varnothing'\) decide it without using the sketched convention bridge.  The
yes and no cases at lines 75-86 are permanent under later oracle extensions.
Padding both strings makes the unions total; the entire construction is
\(\varnothing'\)-computable; and the final degree argument at lines 88-95
correctly derives noncomputability and strictness below \(\mathbf0'\) from
incomparability.  I found no missing case.

### Friedberg--Muchnik finite injury — checked clean

At the same annex, lines 99-171 now give a complete effective construction.
The stage approximation specifies bounded oracle simulation and use; lines
118-123 wrap every accept/reject oracle decider into a total 1/0 numerical
program before normalization; the finite state and fair scheduler are explicit;
and every action initializes all lower-priority strategies while preserving
higher restraints.

The induction handles both final-witness cases.  If a strategy acts, the
preserved value 0 disagrees after its witness enters the target.  If it never
acts, hypothetical equality forces a final value 0; only finitely many
lower-priority enumerations can occur below that finite use because witnesses
are chosen above their stages, so the stable computation eventually appears
and forces action.  Lines 160-169 then compile c.e. membership into a
query-free program that writes 0 and accepts, establishing reduction to the
definedness jump and hence the intermediate-degree conclusion.  The former
accept/reject mismatch and the former sketch dependency have both been
removed.

### Analytical, information, MRDP, and computable-structure additions — checked clean except F14

- The universal relations at
  `handbook/parts/p04/frontiers-of-computability.tex:68-90` enumerate the fixed
  lightface syntax, treat invalid Sigma-side codes as false, take the dual by
  complement, and state the correct Sigma/Pi completeness directions under
  effective many-one reductions.  The index coordinate is not misrepresented
  as a set parameter.  The HYP, WF, and IF domains and directions remain
  consistent with this lightface convention.
- The prefix-free invariance, incompressibility count, upper
  semicomputability, exact Chaitin hypotheses, and Omega truncation arithmetic
  are correct.  F14 concerns only a missing proof bridge under the upgraded
  `proved` status.
- The repaired MRDP survey at
  `handbook/parts/p04/frontiers-of-computability.tex:426-462` has the correct
  Pell multiplication formula
  \(x_{m+n}=x_mx_n+d\,y_my_n\) and
  \(y_{m+n}=x_my_n+x_ny_m\).  It states the Julia Robinson growth condition
  in the right two directions and explicitly identifies the Diophantine Pell,
  congruence, bounded-universal-elimination, and final-composition material as
  cited omissions.  It remains honestly a proof survey, not a claimed full
  MRDP proof.
- The rational-order compiler has exactly the valid-index domain and uniform
  conclusion its back-and-forth construction proves; it does not infer a
  computable copy for arbitrary countable structures.

### Complexity classifications — checked clean except F13

- The fixed-width address convention for a succinct circuit is exact, and the
  latest padding convention makes ordinary circuit/QBF encodings available at
  arbitrarily large power-of-two lengths.  Under that convention, CVP is
  P-complete under logspace many-one reductions, SCVP is EXPTIME-complete, and
  STQBF is EXPSPACE-complete under polynomial-time many-one reductions.  These
  are the standard classifications recorded in Papadimitriou's treatment; my
  objection is only the current definition order, not the class assignments.
- SAT/TAUT, Cook--Levin/Levin, fixed-alternation QBF, TQBF, the class ladder,
  and the hierarchy corollaries retain the correct reductions and hypotheses.
- `handbook/parts/p04/complexity.tex:465-469` points to the single Part III
  Fagin theorem, whose statement is NP = ESO over finite relational structures
  with no built-in order.  It does not create a second theorem identity.
- Ordered FO(LFP) = P has the required positivity and built-in-order
  hypotheses; no unqualified FO/circuit-class equation is asserted.

## New findings from direct repair fallout

### F13 [must-fix] [open] STQBF and its encoding are introduced before QBF

- **Author:** computability/complexity topic specialist, R2
- **Criterion:** definition before use; exact language and yes predicate
- **Location:**
  - premature encoding/use:
    `handbook/parts/p04/complexity.tex:178-193`, especially the “QBF
    encoding” at line 178 and STQBF at lines 191-193;
  - later owner:
    `handbook/parts/p04/complexity.tex:220-235`.
- **Claim/evidence:** the succinct definition asks whether the decoded string
  is a “valid encoded true closed quantified Boolean formula” before the local
  definition has introduced QBF formation, Boolean-quantifier range,
  closedness, TQBF, or truth.  Those clauses occur only in the later
  `def:p04-qbf-languages` environment.  The newly added padded decoder is a
  good repair to the power-of-two issue, but it now explicitly names the later
  syntax owner.
- **Concrete harm:** at the point where `STQBF` is declared as a language, its
  validity and yes predicates cannot yet be evaluated from reader-visible
  definitions.  This is precisely the charter's prohibited definition-after-
  use pattern.  It does not falsify the EXPSPACE classification once the later
  definition is imported; it makes the local language definition ill-ordered.
- **Exact correction:** move `def:p04-qbf-languages` (or at least its QBF
  formation, closedness, Boolean-quantifier semantics, and TQBF clauses) above
  `def:p04-succinct-problems`.  Then let the padded succinct definition refer
  backward to that one owner.  Do not create a second abbreviated QBF
  definition inside the succinct entry.
- **Status:** open

### F14 [must-fix] [open] The complete Omega proof assumes an unstated domain-undecidability lemma

- **Author:** computability/complexity topic specialist, R2
- **Criterion:** all substantive steps supplied for a `proved=annex` result;
  exact dependency status
- **Location:**
  - proved status:
    `handbook/parts/p04/frontiers-of-computability.tex:357-365`;
  - proof step:
    `handbook/annex/p04/frontiers.tex:32-40`, especially lines 38-39.
- **Claim/evidence:** the annex derives a decider for all programs of length at
  most \(n\) from a hypothetical computation of Omega, then calls this a
  contradiction with “undecidability of the universal machine's halting
  domain.”  No prior named theorem in this entry states that domain
  undecidable, and the annex neither proves the reduction nor references a
  separately stated cited dependency.  The front matter says a proved annex
  supplies every substantive formal-logical step, with dependencies stated
  separately as cited results (`handbook/frontmatter.tex:64-71`).
- **Concrete harm:** the numerical weight argument is complete, but its only
  contradiction target is asserted rather than established at the proof's
  declared evidence level.  A universal prefix-free machine does have an
  undecidable domain, so this is a proof-completeness/status defect, not a
  counterexample to the theorem.
- **Exact correction:** after assuming `dom(U_K)` decidable, enumerate programs
  in increasing length, use that decider to discard nonhalters, run the finite
  set of halting programs, and return the first length producing a given
  string.  Universality ensures a description exists, so this computes
  \(K_{U_K}\), contradicting the separately cited
  Theorem~`thm:p04-kolmogorov-noncomputable`.  Insert this short bridge before
  the Omega contradiction.  Alternatively state and cite an exact prior
  domain-undecidability theorem; do not leave it as an untagged premise.
  Chaitin's primary treatment is
  [JACM 22 (1975), DOI 10.1145/321892.321894](https://doi.org/10.1145/321892.321894).
- **Status:** open

## Structural checks

- Reachability: **45 files** (two roots, seventeen wrappers, seventeen exact
  inherited units, six body additions, three annex additions).
- Exact restoration: **17/17** wrappers name the matching inherited interval;
  each inherited file's line count equals its closed source interval.
- Reachable labels: **81**, with no duplicate label in the live Part IV graph.
- Static cross-references: every one of the **66** reachable Part IV references
  has a matching label in the handbook tree, including the seven source-result
  hooks and the Part II/III public dependencies.
- Citation/status keys: **53 distinct keys**, all present in
  `handbook/bib/handbook.bib`.
- Proof reciprocity: six `proved=annex:*` body declarations and six exact
  matching annex items, with no orphan or duplicate pair.  Reciprocity is
  structurally clean; F14 concerns the completeness of one paired proof.
- No reader-visible admission-debt marker survives.  The current uses of the
  lowercase word “open” are genuine complexity-theory open equalities, not
  construction debt.

## Four-lot coverage

| Lot | Checked clean | Findings | Not checked |
|---|---|---|---|
| 1. Machines, effective procedures, mu-recursion, equivalence, Church--Turing | Re-read all exact machine units and the entire current supplement.  Checked the TM I/O convention, primitive-recursive and positive-arity partial-recursive classes, predicate/numerical minimization types, normal form, machine equivalence, all URM instruction/exit/zero-decrement cases, and the formal/informal Church--Turing boundary. | F1-F2, F7-F8 accept-fixed. | External reproof of the cited Kleene/Turing/lambda/URM equivalence; build/visual layout. |
| 2. Universal computation, reductions, decision and arithmetical hierarchy | Re-read every exact unit and current supplement/apparatus.  Checked the one numbering and Kleene-equality owners, enumeration bridge, s-m-n domain, reduction directions, K/TOT classifications, prefix-form apparatus, source-result hooks, jump convention, analytical handoff, and all direct compiler uses. | F1, F6-F8 accept-fixed. | Full external reproof of cited hierarchy strictness and Post's theorem; build/reference runtime. |
| 3. Degrees, jumps, priority, simple/creative sets | Re-read the whole continuation and annex after each live repair.  Checked quotient/join/jump typing; the direct jump compiler; every Kleene--Post yes/no/permanence/totality/degree step; every Friedberg--Muchnik wrapper, simulation, scheduler, witness, action, restraint, initialization, finite-injury, no-action, c.e.-index, and intermediate-degree step; and simple/productive/creative/Myhill/Rice--Shapiro scopes. | F6 accept-fixed; no residual in this lot. | External reproof of citation-only semilattice/simple/creative/Myhill/Rice--Shapiro results; visual figure QA. |
| 4. Analytical/information/MRDP/catalog/structures/complexity | Re-read both full editorial chapters and the full current frontiers annex.  Checked lightface parameters and prefix parity, universal complete-set directions, HYP/WF/IF, prefix-free/Kraft/semicomputability, exact Chaitin hypotheses, every Omega inequality, Pell/Robinson/MRDP boundaries, all finite encodings, fixed word problems, tiling, Busy Beaver, uniform effective back-and-forth, resource classes and hierarchy hypotheses, CVP/SCVP/STQBF membership/hardness classes, QBF/PH, class-ladder open edges, exact finite-structure capture, Fagin identity, and ordered FO(LFP). | F3-F5 and F9-F12 accept-fixed; F13-F14 open. | Full external proofs of citation-only analytical, Kolmogorov, Chaitin, MRDP, word/tiling, Busy Beaver, succinct-completeness, hierarchy, QBF, and descriptive-complexity theorems; build and visual QA. |

## Scope conclusion

Every R1 record and every repair named in the R2 brief was checked against the
latest bytes, including direct proof steps rather than only statements.  R1
F1--F12 are **accept-fixed**.  Part IV remains **source/content not yet
admissible** solely because of F13 and F14.  After those local repairs, I have
no remaining mathematical objection in the checked scope.  Build, visual,
historical-source fidelity beyond the verified wrapper intervals, human review,
administrative admission, and user acceptance remain separate gates and were
not inferred here.

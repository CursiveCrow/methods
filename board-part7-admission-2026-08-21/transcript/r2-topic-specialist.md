# Part VII admission board, round 2: proof-theory / type-theory topic specialist

## Scope

I reread the current live Part VII body and annex route from scratch, including every routed editorial addition and the exact registry sheets used by the mathematical claims. I did not read any seat transcript. I made no handbook, specification, tool, test, or generated-file edit, and I did not run tests or build TeX/PDF.

## Blocking finding

### R2-F1 — blocking — arbitrary-multiplicity principal Mix reduction is asserted but not constructed

- **Location:** `handbook/parts/p07/arithmetic-proof-theory-supplement.tex:94-152`; `handbook/annex/p07/arithmetic-proof-theory-supplement.tex:6-119`, especially annex lines 61-112.
- **What is now correct:** The current proof fixes the earlier Cut-only contraction error. It converts Cut to Mix, selects an uppermost maximal-rank Mix, absorbs contraction by increasing (m) or (n) (`annex:51-59`), and uses the natural-sum ordinal
  [
    o(D)=\mathop{\#}_{c\in\operatorname{Mix}(D)}
          \omega^{\omega r(A_c)+h(c)}.
  ]
  Commuting a selected Mix over a nonprincipal last inference produces same-rank Mixes with smaller premise-height sums and can duplicate only lower-rank internal Mixes (`annex:40-49`). The unit-multiplicity principal reductions for (land,lor,	o) at `annex:61-91` preserve the endsequent and replace the selected formula by proper-subformula Mixes. Those parts are sound.
- **Exact remaining gap:** The selected rule permits arbitrary (m,n\ge1), and its side contexts may contain further occurrences of the Mix formula. Lines 61-91 construct only the (m=n=1) principal/principal cases. Lines 93-101 then say that one may mark one principal occurrence, that every unused (A)-occurrence “is carried into a residual Mix,” and that every such residual has smaller height, but they give no residual derivation schema, premises, endsequent, or height calculation for any of the three connectives.
- **Why the unit construction does not itself prove the claim:** For example, with (A=B\land C) and (m,n>1), the displayed (B)- and (C)-Mixes remove the one principal pair but leave (A^{m-1}) in succedent context and (A^{n-1}) in antecedent context. The text does not construct the further (A)-Mix nodes eliminating those occurrences. In particular it does not establish that each such node takes two proper subderivations of the original premises rather than a newly derived principal-reduction result. Without that construction, the claimed strict inequality
  (h_i<h(D_0)+h(D_1)) at annex lines 96-98 and 103-112 is unproved. This is load-bearing: one residual rank-(r) Mix at height at least the removed node's height defeats the natural-sum decrease.
- **Exact correction:** For each of (land,lor,	o), display the full (operatorname{Mix}^{m,n}_A) reduction with all residual (A)-Mixes, identify their two premise derivations, show that at least one premise is a proper subtree of the corresponding original last inference, calculate every residual height sum, and show the final sequent after contractions. An induction on (m+n) is acceptable if its induction step gives those actual derivations and inequalities. Alternatively, change `thm:p07-prop-cut-termination` from `proved` to `sketched`/cited and state the arbitrary-multiplicity reduction as the named omission; that alternative does not discharge a locally proved full-assignment obligation.
- **Status:** **still open; the current `proved=annex:p7.arithmetic.1` token is not supported.**

## Focused dispositions

### MLTT congruence, Sigma rules, and scope — accept

- `handbook/registry/calculi/mltt-intensional.tex:17-37` now declares (sigma,	au:Delta	oGamma), transports dependent premises from left to right, and uses (operatorname{Eq}_Delta) for every substituted premise and conclusion. The two cases of (operatorname{Eq}_Delta) type both type judgments and term judgments.
- `mltt-intensional.tex:43-48` now has separate `Sigma-beta1` and `Sigma-beta2` rules, each with one declared equality judgment as conclusion.
- Pi, Sigma, Id, J, conversion, Russell universes, cumulativity, and the universe-closure rules remain typed. The body at `lambda-calculi-and-type-theories.tex:399-450` correctly distinguishes the full selected sheet from the much narrower Abel--Coquand--Dybjer dependent-function/one-universe calculus. No normalization or decision result is inferred for the sheet's Sigma, Id, or cumulative-universe extensions.

### Canonical LK--ND translation and finite-sequent completeness — accept

- The finite-succedent map at `calculi-and-derivability-supplement.tex:147-167` fixes association, removes multiplicity by support, sends the empty succedent to (ot), excludes equality, and disclaims proof-object/cut-free preservation.
- `annex/p07/calculi-and-cut-elimination-supplement.tex:50-190` now checks both directions against the exact canonical-LK and nonvacuous-discharge ND sheets. The finite detour at lines 63-73 supplies admissible use of an otherwise unused assumption without violating the discharge convention. The LK-to-ND induction covers both structural directions, Cut, every propositional rule, all four quantifier rules, empty succedents, and RAA/primitive-negation cases. The reverse induction covers every ND constructor, alpha-renaming, eigenvariables, and derives the needed double-negation sequent in canonical LK.
- The completeness proof at annex lines 192-216 reduces a valid finite sequent to ND consequence, invokes the already proved propositional or first-order ND completeness theorem with the exact Choice/countable-signature boundary, specializes the Henkin construction to the equality-free language, and translates back. It explicitly uses Cut and makes no canonical-LK cut-free completeness claim.

### Maehara partition lemma and Craig/Beth boundary — accept at the stated restricted scope

- `cut-elimination-and-interpolation-supplement.tex:66-114` now fixes a purely relational, equality-free signature, states the common-predicate and common-free-variable conditions, and makes the restricted scope explicit. General signatures with function/constant terms are not silently covered; the body identifies the missing alien-term lifting lemma.
- `annex/p07/interpolation-supplement.tex:8-136` checks the four identity placements, (ot L), weakening/contraction, all one-premise rules, both placements of all three branching rules, both placements of (orall L/exists R), and both placements of the two eigenvariable rules. For non-eigen instantiation variables that cease to be common, a principal formula in the first half uses (orall zI(z)), while one in the second uses (exists zI(z)); the required sequent transformations and freshness conditions are given at lines 72-94. The (orall R/exists L) polarities at lines 96-128 are also correct.
- The local partition lemma is therefore proved for the declared purely relational calculus. `cut-elimination-and-interpolation-supplement.tex:118-177` keeps general first-order Craig and Beth cited and explains that function-bearing/equality-bearing generality is source-carried, not locally proved. No inherited status is upgraded.

### Church--Rosser by parallel reduction — accept

- The four parallel-reduction clauses and complete-development recursion are exact at `lambda-calculi-and-type-theories.tex:107-152`.
- `annex/p07/lambda-calculi.tex:5-109` proves reflexivity, alpha-invariance of development, the capture-avoiding parallel-substitution lemma including the beta/substitution-composition case, the complete-development lemma including the application/beta overlap, both simulations between ordinary and parallel reduction, one-step diamond, and the finite-grid lifting to confluence.
- The beta-normal-form uniqueness proof at annex lines 112-124 is a complete consequence. The body correctly separates confluence from weak or strong normalization.

### Bicartesian typed extension and syntactic category — accept

- `normalization-and-curry-howard-supplement.tex:34-111` now explicitly separates arrow-only `sheet:stlc` from the categorical extension. It defines product, coproduct, unit, and empty types; all constructors/eliminators and typing premises; function/product/coproduct beta--eta equations; terminal and initial uniqueness equations; typed congruence; and substitution.
- With types as objects and unary judgments modulo that equality as arrows, identity and composition are defined and the displayed equations supply the product, coproduct, terminal, initial, and exponential universal properties. The dictionary and triangle at lines 113-175 are therefore backed by a specified bicartesian closed syntactic construction rather than the arrow-only sheet.

### Source-relative HA treatment — accept

- `functional-interpretations.tex:340-389` retains cited statuses for IPC/HA disjunction and HA numerical existence, states all closedness hypotheses, and explicitly says the inherited NJ normalization omits arithmetic equality and induction.
- The new boundary at lines 370-389 identifies the exact Troelstra--van Dalen source and refuses to invent a local proof-term calculus or local normalization/canonicity proof. The canonical-form prose is labeled an explanation of the cited argument. The annex at `annex/p07/functional-interpretations.tex:31-37` now contains ordinary source-status prose rather than a false visible-stub/internal-contract assertion.

### Haken bottleneck sketch — accept as a sketch

- The fixed weak pigeonhole CNF and DAG clause-occurrence measure remain exact at `proof-complexity.tex:66-96`.
- `annex/p07/proof-complexity.tex:5-47` correctly defines critical assignments and the assignment-routing invariant. It no longer substitutes the false claim that merely mentioning linearly many pigeons forces an exponentially small falsification fraction. Instead lines 28-37 explicitly import Haken's stronger source-defined clause-complexity/bottleneck lemma and name its counting and first-bottleneck conclusions as the omitted core. The final charging calculation is then correct.
- This agrees with Haken's original lower bound and the Beame--Pitassi bottleneck treatment; the body remains `sketched`, not `proved`. See [Beame and Pitassi's source-hosted treatment](https://homes.cs.washington.edu/~beame/papers/focsclause.pdf) and [Haken's paper record](https://www.sciencedirect.com/science/article/pii/0304397585901446).

### Wansing display derivation and generalized-calculus statuses — accept

- The current example at `structural-extensions.tex:178-197` is a genuine three-rule display cycle, not the former under-specified K-axiom derivation:
  (ARightarrow A), then Box-L to (Box ARightarrowullet A), reverse Modal Display to (ulletBox ARightarrow A), then Box-R to (Box ARightarrowBox A).
- Every step is literally a row at `registry/calculi/display-k-wansing.tex:5,8-9,12`. The example expressly disclaims being a K-axiom or adequacy proof. The four adequacy/cut results at `structural-extensions.tex:209-230` remain separately cited to their matched systems.

## Remaining route and status audit

- The Part VII driver now routes the source map and generated theorem/definition register, while exact-source entries retain their source statuses (`handbook/parts/p07.tex:1-128`).
- The annex route now includes the new arithmetic and proof-complexity evidence and states the proved/sketched/cited distinction accurately (`handbook/annex/p07.tex:1-13`).
- The reader navigation table at `proof-complexity.tex:192-340` now routes the active MLTT and four modal sheets, the new LK--ND/completeness proofs, Maehara proof, Church--Rosser proof, propositional Mix proof, omega theorem, HA source boundary, and Haken sketch. Its old false “no active sheet” claims are gone.
- The exact inherited LK/LJ, Cut/Mix, cut-elimination, subformula, Craig/Beth, NJ normalization, STLC, Curry--Howard, and Gentzen passages retain their original hypotheses and proof statuses. Midsequent/Herbrand remain cited with equality-free, prenex, regularity, and ground-term hypotheses. System F keeps Church checking separate from Curry assignment undecidability. Dialectica, number realizability, ECT, Markov, epsilon theorems, omega logic, Feferman--Schuette, and Frege-boundary claims retain their declared source-specific scopes.
- The erroneous claim that the separate master strength table begins below PRA has been removed from `arithmetic-proof-theory-supplement.tex:247-290`.
- No reader-visible OPEN/unadmitted/stub/internal-workflow marker occurs on the routed Part VII surface. Unrouted historical duplicates were not treated as reader content.

## Verification boundary

This is a mathematical/source review only. I did not run a build, reference checker, bibliography tool, generated-table tool, test, PDF render, or visual inspection.

REJECT

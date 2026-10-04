# Part VII admission board, round 1: proof-theory / type-theory topic specialist

## Mandate and method

I reviewed the complete current reader graph rooted at `handbook/parts/p07.tex` and `handbook/annex/p07.tex`: all nineteen routed exact-source wrappers, every routed editorial body file, all four routed annex files, and the calculus sheets on which the live body makes a mathematical claim. I did not read another Part VII seat transcript. I made no manuscript, control, test, or generated-file edit, and I did not build or run tests.

The controlling requirements are the charter's exact calculus/derivability types, definition-before-use, exact metatheorem hypotheses, honest proof status, register-ceiling coverage, and absence of reader construction debt (`board-part7-admission-2026-08-21/charter.md:3-17,21-32`). The treatment letters in the frozen register are content ceilings rather than proof-status tokens; cited source theorems may remain cited, but a new local calculus or proof claim must itself be typed and honest.

## Findings

### F1 — blocker — the MLTT congruence schema is in the wrong context and does not type its substitutions

- **Location:** `handbook/registry/calculi/mltt-intensional.tex:17-36`, especially lines 29-36; consumer boundary at `handbook/parts/p07/lambda-calculi-and-type-theories.tex:399-417`.
- **Claim:** Lines 17-28 correctly define the multi-sorted equality relation \(\operatorname{Eq}_{\Delta}\) for type and term judgments transported to a common context \(\Delta\). Lines 31-34 then say that \(\sigma,\tau\) are substitutions *into* \(\Gamma\), but never type their common source. After substitution, \(P_i[\sigma]\), \(P_i[\tau]\), \(J_c[\sigma]\), and \(J_c[\tau]\) are judgments in that source context, not in \(\Gamma\). Nevertheless the displayed rule at line 36 uses \(\operatorname{Eq}_{\Gamma}\) in every premise and conclusion.
- **Minimal counterexample/type failure:** Take a non-endomorphic substitution \(\sigma:\Delta\to\Gamma\) with \(\Delta\ne\Gamma\). Then \(P_i[\sigma]\) is a \(\Delta\)-judgment, while \(\operatorname{Eq}_{\Gamma}\) requires a \(\Gamma\)-judgment. The rule is therefore not an instance of the multi-sorted relation it just defined. This is not a notational preference: the dependent telescope transports later premises using equalities established in the common source context.
- **Exact correction:** State explicitly “let \(\sigma,\tau:\Delta\to\Gamma\) be capture-avoiding substitutions,” retain the left-to-right dependent transport clause, and replace the rule by
  \[
  \frac{\operatorname{Eq}_{\Delta}(P_i[\sigma],P_i[\tau])\quad(1\le i\le k)}
       {\operatorname{Eq}_{\Delta}(J_c[\sigma],J_c[\tau])}.
  \]
  The existing two cases of \(\operatorname{Eq}_{\Delta}\) already cover both type premises and term premises; no generic untyped equality line should replace them.
- **Evidence/source:** This is the ordinary typing of dependent substitutions and constructor congruence for the selected intensional calculus; the sheet itself cites `MartinLof1984`, `NordstromPeterssonSmith1990`, and `Hofmann1997` as its controlling sources.
- **Status:** **open; blocks admission of the selected MLTT calculus.**

### F2 — must-fix — the selected MLTT calculus gives one rule two distinct conclusion judgments

- **Location:** `handbook/registry/calculi/mltt-intensional.tex:42-46`, especially line 46.
- **Claim:** The `Sigma-beta` row has as its purported conclusion both
  \(\Gamma\vdash\pi_1(a,b)\equiv a:A\) and
  \(\Gamma\vdash\pi_2(a,b)\equiv b:B[a/x]\), separated only by `\qquad`. The calculus declares individual context/type/term/equality judgments, and every other `\hbrule` has one conclusion judgment. No conjunction-of-judgments or two-conclusion rule object is defined.
- **Concrete harm:** A derivation cannot cite “the conclusion” of this rule as one of the declared judgments. In particular, the typed congruence schema cannot classify this item as one constructor conclusion \(J_c\), and a checker or reader cannot tell whether applying the rule yields either projection equation separately or only an undeclared pair.
- **Exact correction:** Split it into two rules, for example `Sigma-beta1` with conclusion \(\pi_1(a,b)\equiv a:A\) and `Sigma-beta2` with conclusion \(\pi_2(a,b)\equiv b:B[a/x]\), each carrying the same typed premises. Update the constructor-congruence list and any generated rule lookup accordingly.
- **Status:** **open.**

### F3 — blocker — the Maehara entry simultaneously calls its induction omitted/sketched and complete/proved

- **Location:** `handbook/parts/p07/cut-elimination-and-interpolation-supplement.tex:83-115,117-167`; reciprocal annex `handbook/annex/p07/interpolation-supplement.tex:16-33`.
- **Claim:** The local lemma is explicitly `sketched=annex:p7.interp.1` at body lines 97-102. Its proof boundary at lines 106-115 says a complete proof still needs every initial, structural, propositional-placement, and quantifier case. The annex's `\sketchnote` at lines 17-22 lists precisely those omitted cases and lines 23-32 say the case-by-case verification is absent. But the body then prints the heading “Complete induction for the partition lemma” at line 133 and concludes “This proves Lemma” at lines 145-146.
- **Concrete harm:** The reader receives two incompatible proof standings for the same editorial lemma. The eight-row table at body lines 117-130 does not resolve the contradiction: “one-premise propositional rule,” “two-premise propositional rule,” and “eigenparameter rule” are families of cases, not the required rule-by-rule/partition-placement verification. The frozen research contract itself states that a table saying the other cases are instances remains a sketch (`spec/research/p07-new-content.md:436-441`).
- **Exact correction:** Choose one honest surface. Either (a) retain `sketched`, rename lines 133-146 to “Further proof sketch,” remove “Complete” and “This proves,” and keep Craig/Beth cited; or (b) supply a reciprocal annex proof enumerating both initial placements, weakening/contraction, every left/right propositional rule under every principal-formula placement, and all four quantifier cases with eigenvariable removal, then change only the new Maehara lemma to `proved=annex:...`. The inherited Craig and Beth theorems must remain cited as required by the source-status invariant.
- **Evidence/source:** The exact case obligations and theorem boundary are supported locally by `Maehara1960`, `Takeuti1987`, and `TroelstraSchwichtenberg2000` and are already spelled out in `spec/research/p07-new-content.md:418-468`.
- **Status:** **open; violates the charter's honest-proof-status invariant.**

### F4 — must-fix — the “selected HA proof-term presentation” is not an exact calculus, yet it is used as the extraction proof engine

- **Location:** `handbook/parts/p07/functional-interpretations.tex:325-413`, especially definition lines 370-382 and theorem/proof lines 384-413; stale reader note at `handbook/annex/p07/functional-interpretations.tex:31-36`.
- **Claim:** The new definition says only that implication is a function type, conjunction a product, disjunction a tagged sum, existential a dependent pair, and induction a primitive-recursion eliminator. It gives no term grammar, typing rules, equality rules, arithmetic constants, conversion/reduction relation, induction computation equations, or erasure map. Nonetheless the cited canonicity theorem and the three paragraphs headed “Proof of ...” use normalization, subject preservation despite equality/induction, canonical forms, and erasure from exactly this purportedly selected presentation.
- **Concrete harm:** Two proof-term calculi satisfying the prose description can differ in definitional equality, induction reductions, commuting conversions, and canonical forms. Thus “normalize the closed proof term” at lines 393-413 does not denote an operation on a defined object. The chapter correctly warns at lines 363-368 that the inherited normalization theorem excludes equality and induction, but the replacement definition does not supply what that warning says is missing.
- **Exact correction:** Either display/register one exact HA proof-term calculus (term and type/formula grammar, all typing rules, equality and induction rules, compatible reduction, computation equations, and erasure) and cite a normalization/canonicity theorem for that exact presentation, or state the canonicity theorem wholly source-relatively without pretending to have defined a local calculus. In the latter case retitle the three paragraphs “Derivation from the cited canonicity theorem.” Also replace annex lines 31-36 by an ordinary attribution sentence: there is no visible `N-a-055` stub in the body, and “bidirectional annex contract”/the row ID are internal workflow prose forbidden by the charter.
- **Evidence/source:** The exact obligation is already recorded at `spec/research/p07-new-content.md:1016-1048`: the inherited NJ normalization is insufficient for HA equality and induction, so a matched calculus plus normalization/canonicity is required or the properties remain cited. The body cites `TroelstraVanDalen1988` and `TroelstraSchwichtenberg2000` for the source-specific route.
- **Status:** **open.**

### F5 — must-fix — the reader-facing body/sheet/annex route table is stale and contradicts the live graph

- **Location:** `handbook/parts/p07/proof-complexity.tex:181-315`, especially its exhaustiveness claim at lines 188-190 and rows at lines 244-310.
- **Claim/evidence:** The table says it lists every status-bearing result exactly once, but:
  - lines 244-246 say “the MLTT remainder has no active sheet,” while the body routes and cites `sheet:mltt-intensional` at `lambda-calculi-and-type-theories.tex:399-417` and the registry file is live;
  - lines 294-296 say all four generalized-framework rows remain citation-only until exact modal sheets exist, while `structural-extensions.tex:144-216` gives four matched active sheets, worked derivations, and a cited adequacy theorem;
  - the arithmetic row at lines 268-274 omits the status-bearing propositional cut-termination theorem (`arithmetic-proof-theory-supplement.tex:126-132`) and the selected omega-calculus theorem (`:376-392`);
  - the functional row omits the cited HA proof-term canonicity theorem (`functional-interpretations.tex:384-391`);
  - the generalized-framework row omits `thm:p07-four-modal-calculi` (`structural-extensions.tex:207-216`).
- **Concrete harm:** This is not harmless navigation drift. The table makes false claims about which formal calculi exist, misstates the evidence boundary, and fails its own “every status-bearing result” completeness claim. A reader following it is directed away from the current MLTT and modal rule surfaces.
- **Exact correction:** Regenerate/rewrite the table from the live body and registry. Route the selected MLTT sheet, all four modal sheets, both arithmetic theorems, HA canonicity, and the four-calculi adequacy theorem; or weaken the exhaustiveness claim and remove every false absence statement. Preserve cited/sketched/proved standings exactly.
- **Status:** **open.**

### F6 — must-fix — the Wansing display-calculus “worked derivation” uses structural steps not supplied by its exact sheet

- **Location:** `handbook/parts/p07/structural-extensions.tex:178-195`; claimed rule owner `handbook/registry/calculi/display-k-wansing.tex:1-15`.
- **Claim:** The example says structural monotonicity and Modal Display “expose” \(A\) inside \(\bullet(\Box(A\to B)\circ\Box A)\), later says reversible display postulates “collect” two boxed assumptions, and asserts that every structural step is on the sheet. The sheet supplies only three displayed postulates (Modal Display and two product-display forms), Box/implication rules, one weakening-like monotonicity rule, contraction, and a unit rule. It does not declare associativity/commutativity or the structural congruences/rearrangements needed to reorder and collect the product structures, nor does the prose give the intermediate sequents that would show the listed rules suffice.
- **Concrete harm:** Unlike the GS5 and deep-inference examples, the alleged derivation cannot be reconstructed as a finite sequence of instances of the displayed rules. “Expose” and “collect” hide precisely the display-structural steps that distinguish this calculus from an ordinary sequent calculus. The result may be a true theorem of Wansing's full system, but it is not a worked derivation on the printed sheet.
- **Exact correction:** Transcribe the exact source derivation with every intermediate display sequent and add every structural equivalence it invokes to the Wansing sheet, including its direction/side condition; then check each line. Alternatively, downgrade this block to a cited illustration and remove the claims that it is a complete matched derivation and that every step is already on the sheet. Keep the separate cited soundness/completeness/cut theorem at its source status.
- **Evidence/source:** The selected system is source-attributed to `Wansing1994`; the local sheet itself says it lists exactly the rules used, which is refuted by the omitted structural transitions.
- **Status:** **open.**

### F7 — should-fix, mathematically substantive — the Curry--Howard “syntactic category” is underdefined relative to the bicartesian closed claim

- **Location:** `handbook/parts/p07/normalization-and-curry-howard-supplement.tex:16-58,60-99,101-122`; arrow-only calculus at `handbook/registry/calculi/stlc.tex:5-9`.
- **Claim:** The definition says the selected syntactic category has selected types as objects and unary arrow-only STLC judgments modulo function beta--eta as morphisms. The live STLC sheet explicitly has no products, sums, unit, or empty type. The table nevertheless gives product/coproduct/terminal/initial rows and the figure labels a construction to a bicartesian closed category. Lines 95-97 admit those rows concern a “standard extension,” but no term constructors, eliminators, typing rules, beta/eta equations, or syntactic category for that extension are defined. Function beta--eta alone cannot establish the categorical universal properties for products or coproducts.
- **Concrete harm:** The dictionary entries are individually standard, but the claimed “specified construction” at the figure is not a construction from the printed term calculus. In particular, the category whose objects are only arrow types and whose arrows are unary arrow-only terms has no displayed product/coproduct witnesses.
- **Exact correction:** Either define/cite one exact STLC extension with product, coproduct, unit, and empty types plus all constructor/eliminator beta--eta laws and form its syntactic bicartesian closed category, or restrict the syntactic construction and diagram to the arrow/implication fragment and treat the bicartesian rows explicitly as a cited future extension rather than the selected category. The research specification itself requires a typed calculus “with products/sums” for the bicartesian dictionary (`spec/research/p07-new-content.md:502-526`).
- **Status:** **open.**

## Checked-clean coverage

### Lot 1 — exact calculi, derivability, cut, Herbrand, and interpolation

- **Checked clean:** the exact \(\mathsf{LK}_{\mathrm d}\) and \(\mathsf{LJ}\) finite-multiset/single-succedent rule surfaces, substitutions and eigenvariable conditions, derivation objects, and exact-source soundness sketch (`inherited-11354-11710`). Primitive, derived, and admissible rules are correctly distinguished.
- **Checked clean:** Cut/Mix equipollence is completely proved by contraction plus one Cut (`inherited-11741-11767`). The selected cut-elimination theorem is honestly a sketch for defined-negation LK and LJ; it does not silently cover canonical primitive-negation LK or equality. The propositional cut-free subformula proof and the conditional analytic/empty-sequent consequences are correctly scoped.
- **Checked clean:** the canonical/defined-negation translation and LK--ND theorem exclude equality and disclaim proof-object, cut-free, height, and size preservation. The completeness lookup retains the P2 sketch status and the first-order Choice hypothesis.
- **Checked clean:** midsequent and Herbrand entries state regularity, equality-free/prenex/ground-term hypotheses and remain cited. The exact inherited Craig and Beth theorems retain cited status and exact vocabulary/implicit-definition hypotheses.
- **Residual:** F3 only for the contradictory local Maehara proof standing.

### Lot 2 — normalization, Curry--Howard, lambda calculi, System F, and MLTT

- **Checked clean:** the exact NJ normalization calculus excludes RAA, primitive negation, equality, and induction and states the permutation obligations. STLC subject reduction and strong normalization are distinct sketches with the substitution/candidate omissions identified. Curry--Howard is not conflated with cut elimination.
- **Checked clean:** untyped term grammar, free variables, alpha-equivalence, capture-avoiding substitution, beta reduction/conversion, weak/strong normalization, the looping counterexample, parallel reduction, complete development, Church--Rosser, and uniqueness of normal forms are mutually consistent. The annex honestly labels the parallel-substitution/development/grid omissions.
- **Checked clean:** Church numerals, lambda-definability/partial-recursiveness, the S--K basis, and bracket abstraction have fixed encodings and cited theorem boundaries.
- **Checked clean:** Church-style System F has explicit type/term judgments and term/type beta rules; confluence, strong normalization, decidable explicit checking, Curry-style checking/typability undecidability, impredicativity, and the parametricity boundary are correctly separated.
- **Checked clean:** the MLTT body correctly says the Abel--Coquand--Dybjer normalization/checking theorem covers dependent functions and one Russell universe, not the full selected Pi/Sigma/Id/cumulative sheet; CoC is separated from CIC, and HoTT/cubical material remains pointer-only.
- **Residuals:** F1-F2 in the selected MLTT sheet and F7 in the categorical apparatus.

### Lot 3 — Gentzen/ordinals/omega logic, Dialectica, realizability, and constructive properties

- **Checked clean:** the exact Gentzen source remains a relative cited analysis. The editorial component table separates calculus, codes, notations, reduction, assignment/decrease, transfinite induction, and consistency extraction.
- **Checked clean:** the selected propositional cut measure is a finite multiset of rank/height pairs; its natural-sum encoding is below \(\omega^{\omega^2}\), and the listed critical transformations decrease the multiset ordering. No claim upgrades this to the full \(\varepsilon_0\) PA analysis.
- **Checked clean:** PRA/HA/\(\mathsf I\Sigma_n\)/reverse-mathematics presentations, the calibration-relative ordinal definition, \(\omega_{n+1}\), \(\varepsilon_0\), \(\Gamma_0\), Veblen hierarchy, Feferman--Schuette boundary, and PRA/finitism warning have their needed qualifications.
- **Checked clean:** the selected \(\mathsf{PA}_\infty\) sheet separates function symbols in terms from relation symbols in literals, fixes semi-closed formulas and finite-set sequents, and states J\"ager--Probst indexed derivability and \(2_n(\alpha)\) with the exact cut-elimination bound.
- **Checked clean:** System T and \(\mathsf T_{\mathrm{qf}}\) are distinct; the Dialectica witness/challenge clauses are typed and its HA soundness/relative-consistency results remain cited. The complete number-realizability table, uniform parameter warning, almost-negative ECT restriction, and Markov-principle boundary are correct and do not use realizability as a countermodel to MP.
- **Checked clean:** IPC/HA disjunction and HA numerical-existence statements have the exact closedness hypotheses and remain cited; the cut-free LJ last-rule lemma is completely proved.
- **Residual:** F4 concerns the later purported local proof-term engine and its reader-facing status prose, not the correctness of those cited metatheorems.

### Lot 4 — epsilon/structural extensions, proof mining, and proof complexity

- **Checked clean:** the epsilon calculus fixes an equality-free Hilbert-FOL extension and critical axiom. The first, extended-first/Herbrand, and second epsilon theorems state distinct equality-free consequence boundaries and remain cited.
- **Checked clean:** hypersequent, labelled, display, and deep-inference architectures are definitionally distinct. The GS5 axiom-5 derivation, Negri labelled-K derivation, and Stouppa deep-S5 axiom-B derivation can be followed on their named sheets. The proof-mining and proof-net/GoI ceilings remain pointers and make no extraction/net theorem.
- **Checked clean:** Cook--Reckhow systems, polynomial boundedness, p-simulation, the \(\mathsf{NP}=\mathsf{coNP}\) equivalence, the weak pigeonhole CNF encoding, Haken's resolution-only exponential bound, Frege/extended-Frege definitions, and the no-known-general-lower-bound boundary are correctly separated at cited status. The proof-complexity table does not transfer Haken's bound to Frege.
- **Residuals:** F5's stale navigation/status table and F6's display-calculus worked derivation.

## Not checked / external gates

- No build, cross-reference compilation, bibliography run, generated-register regeneration, PDF/render inspection, visual inspection, human review, or user acceptance was performed. Those gates remain separate under the charter.
- I did not review unrouted historical duplicate Part VII body/annex files or the intentionally unrouted generated audit as reader content.
- I did not independently re-fetch every cited monograph/paper in this time-boxed source pass; findings above are based on the exact live formulas/rules and the fetchable scholarly sources already identified by their bibliography keys and the frozen P7 research ledger.

## Prioritized repair checklist

1. Retype the MLTT congruence schema with \(\sigma,\tau:\Delta\to\Gamma\) and \(\operatorname{Eq}_{\Delta}\) throughout (F1).
2. Split the two Sigma projection computations into two rules (F2).
3. Resolve the Maehara “sketched versus complete” contradiction, preferably by supplying the actual full case induction for the new lemma while keeping Craig/Beth cited (F3).
4. Either register the exact HA proof-term calculus used for normalization/canonicity or make the entire extraction route explicitly source-relative; remove the stale workflow/stub sentence (F4).
5. Rebuild the body/sheet/annex route table from the live graph (F5).
6. Supply the exact Wansing derivation and missing structural rules, or downgrade it to a cited illustration (F6).
7. Define the product/sum/unit/empty typed extension needed by the bicartesian syntactic category, or restrict the categorical claim to the actually defined fragment (F7).

**Round-one source/content verdict: not admissible while F1 and F3 remain; F2 and F4-F7 are concrete repairs required for an exact and internally coherent Part VII reader graph.**

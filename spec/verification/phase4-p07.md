# Phase 4 verification: Part 7

> **PASS VERDICT INVALIDATED (2026-08-12).** This note verified the revoked
> compressed-migration policy, not the binding full-transcription standard.
> Retain it only as audit evidence; see `FULL-TRANSCRIPTION-READINESS.md`.

Date: 2026-08-11
Visit: P7, Proof Theory and Lambda-Calculi
Verified source: `v1.1-verified`, Part VIII, lines 11354--12248.
Research baseline: frozen `spec/research/p07-new-content.md`.

This is the adversarial mathematical, evidence-status, source-accounting, and
register record for the P7 visit.  The final integrated build, exact page
count, mechanical gates, and rendered-page inspection are recorded at the end
of this file against the authoritative TeX Live artifact.

## Verification verdict

- The frozen Part-VIII source has a complete disposition ledger below; no
  source span or exercise is silently dropped.
- The live body has exactly 43 theorem-class results: 3 `proved`, 11
  `sketched`, and 29 `cited`.  The 14 proved/sketched results point to exactly
  14 annex items, with no unresolved target, orphan annex item, duplicate
  pointer, duplicate back-reference, or mismatched pair.
- The inherited evidence classes are preserved.  In particular, Cut
  elimination, natural-deduction normalization, STLC subject reduction, and
  STLC strong normalization remain sketches; Craig, Beth, and Gentzen's PA
  analysis remain cited.
- Exactly ten explicit stubs remain.  They are enumerated below and must
  keep their register rows open.
- The literal wording of `D-P8-004` and `N-a-070` asks for Craig/Beth to be
  proved, while the binding status contract requires the inherited Craig and
  Beth results to remain cited.  The delivered E-level entry contains a local
  Maehara method and a correctly sketched partition lemma, but does not
  manufacture proofs of Craig or Beth.  The finalizer must record this
  contract-limited disposition honestly and must not upgrade either theorem.
- Final integrated mechanical and visual verdict: **PASS** against the
  authoritative 665-page artifact identified below.

## Delivered scope

- Eight body chapters: calculi and derivability; Cut elimination and
  interpolation; normalization and Curry--Howard; untyped lambda calculus,
  System F, and type-theory boundaries; arithmetic proof theory; functional
  interpretations; epsilon/generalized frameworks; and propositional proof
  complexity.
- Six annex fragments with 14 items.  Rules occur only in registry sheets;
  body chapters point to those sheets rather than redisplaying rule schemas.
- Canonical LK, defined-negation LK, LK with equality, and LJ are named apart.
  The inherited Mix/Cut reduction is homed only on the defined-negation LK
  and LJ presentations.  Canonical and equality sheets explicitly deny
  inherited Cut-admissibility coverage, and the equality sheet says that its
  symmetric replacement derivation uses Cut.
- New exact sheets support NJ, STLC, untyped beta reduction, S--K combinatory
  reduction, System F, System T, the equality-free epsilon calculus, extended
  Frege, and extended resolution.  Citation-only calculi are not presented as
  active sheets.
- Apparatus includes the structural-rule and calculi catalogs, the
  Curry--Howard table and triangle, the paired STLC/ND derivation figure, the
  lambda-calculi and proof-complexity tables, annotated further reading, and
  the body-to-sheet/body-to-annex navigation table.

## Frozen-source accounting

The three source chapters occupy 11354--11710, 11711--11960, and
11961--12248.  The following ledger accounts for every substantive unit.

| v1.1 lines | Source unit | P7 disposition and evidence class |
|---:|---|---|
| 11354--11377 | Part/chapter framing and scoped metavariables | Compressed into P7 framing and locally typed metavariable declarations.  Global handbook formula metavariables are `\varphi,\psi,\chi`; type and term roles are separately scoped. |
| 11379--11412 | Context, classical-sequent, and intuitionistic-sequent definitions | Migrated to `def:p07-contexts` and `def:p07-classical-intuitionistic-sequents`, preserving finite multisets, built-in exchange, and exact single succedents for LJ. |
| 11414--11518 | Defined-negation LK rules and derivability | Rules moved to `sheet:lk-defneg`; the body gives only the derivation definition and sheet pointer. |
| 11520--11610 | LJ rules and derivability | Rules moved to `sheet:lj`; single-succedent shape, absent right structural rules, substitution, and eigenvariable conditions are preserved. |
| 11612--11626 | LK soundness | Migrated as `thm:p07-lkd-soundness`, still `sketched=annex:p7.calculi.1`; every omitted rule calculation is named. |
| 11628--11643 | Worked cut-free commutativity derivation | Deliberately retired as a duplicate body proof display; its lookup role is supplied by the existing Part-2 ND/LK comparison figure.  It is not evidence for a new result. |
| 11645--11694 | Primitive, derived, admissible; Cut warning; principal/active formulas | Migrated to exact definitions and warnings.  Admissibility is not conflated with a derived rule. |
| 11696--11709 | Two calculus exercises | Retired as exercises.  The distributivity exercise's principal-formula lesson and the eigenvariable-unsoundness exercise's freshness lesson survive in definitions and sheets. |
| 11711--11740 | Formula rank, derivation height, and Mix setup | Migrated to `def:p07-mix-measure` and the two active Mix rows.  Formula rank is `\operatorname{rk}_{\mathrm{fm}}`; derivation height is `\operatorname{ht}`. |
| 11741--11776 | Cut/Mix equipollence complete proof and exact measure | Migrated as `proved=annex:p7.cut.1`; both directions, both multiplicities, and the LJ specialization survive. |
| 11778--11822 | Cut-elimination theorem and reduction plan | Migrated as the Tier-1 method and `sketched=annex:p7.cut.2`; the omitted full commuting/principal case table remains explicit. |
| 11824--11841 | Cut-free propositional subformula lemma, complete proof | Migrated as `proved=annex:p7.cut.3`, retaining induction on derivation height and the copied-or-immediate-subformula invariant. |
| 11843--11856 | Propositional subformula corollary | Migrated as `sketched=annex:p7.cut.4`, because it still loads the Cut-elimination sketch. |
| 11858--11864 | First-order qualification | Preserved exactly as analyticity modulo term substitution and eigenvariable alpha-renaming; no literal first-order subformula overclaim is made. |
| 11866--11880 | Empty-sequent underivability | Migrated as `sketched=annex:p7.cut.5`; the sequent is stated as an underivable syntactic object, not as a malformed derivability judgment. |
| 11882--11899 | Consequences and calculus-dependence boundary | Preserved, including nonelementary blow-up, unbounded first-order term search, and the warning that extensions require new reductions. |
| 11901--11912 | Two Cut/proof-search exercises | Retired as exercises.  The smaller-rank principal case and propositional/first-order search distinction remain explicit in the method and warning. |
| 11914--11937 | Craig interpolation | Migrated with exact sentence, vocabulary, equality/logical-constant, and degenerate-case clauses as `cited=Craig1957`; no annex item. |
| 11939--11959 | Beth definability | Migrated with exact reduct, arity, and explicit-definition clauses as `cited=Beth1953`; no annex item. |
| 11961--12028 | NJ detours, exact calculus scope, and normalization sketch | Migrated as definitions, a method, and `sketched=annex:p7.norm.1`; RAA, primitive negation, equality, and induction remain excluded. |
| 12030--12099 | STLC syntax, typing, subject reduction, and strong normalization | Syntax/rules moved to `sheet:stlc`; subject reduction and strong normalization remain `sketched=annex:p7.norm.2` and `.3`. |
| 12101--12131 | Curry--Howard and composition example | Migrated into the exact correspondence entry, A-072/A-151, and the paired A-152 derivation.  The fixed-calculus qualification is explicit. |
| 12133--12216 | Gentzen PA analysis and internal proof boundary | Migrated as an analysis-relative cited theorem plus component ledger and proof boundary.  No canonical unqualified ordinal invariant is asserted. |
| 12218--12229 | Two typing exercises | Retired as exercises.  The typed-K/weakening example is retained, and the subject-reduction substitution/capture obligations are enumerated in the annex. |
| 12231--12240 | Abstract reduction and weak/strong normalization | Migrated to `def:p07-abstract-reduction`, with the two notions separated before use. |
| 12242--12247 | Final weak-versus-strong exercise | Retired as an exercise; its implication and separating counterexample are supplied in the preceding entry/example. |
| 12248 | End of Part VIII | Accounted for by the P7 driver/annex boundary; no source content follows before the next part. |

The seven retired exercise blocks are not proof evidence.  A fact requested
only as an exercise was either established/cited independently, retained as a
definition or warning, or omitted; no exercise prompt was laundered into a
proof status.

## Statement-by-statement fidelity sample

The deliberate second pass sampled all twelve inherited theorem-class claims,
including the Tier-1 Cut-elimination method, against v1.1.

| Live result | Adversarial check |
|---|---|
| `thm:p07-lkd-soundness` | Finite contexts, structures and assignments, empty-succedent reading, and eigenvariable/substitution obligations agree with 11612--11626; status remains sketch. |
| `thm:p07-cut-mix-equivalence` | Cut-as-unit-Mix and general-Mix-via-contractions directions both survive; LJ uses only left contraction; status remains proved. |
| `thm:p07-cut-elimination` | Same-endsequent transform is restricted to `sheet:lk-defneg` and `sheet:lj`; Mix multiplicities, lexicographic rank/height, contraction, principal, weakening/initial, and eigenvariable cases are named; status remains sketch. |
| `thm:p07-cut-free-subformula` | Propositional and cut-free hypotheses are explicit for both active calculi; the complete height induction survives. |
| `thm:p07-propositional-analytic-existence` | The conclusion is propositional only and visibly depends on the sketched Cut-elimination theorem; status remains sketch. |
| `thm:p07-empty-sequent` | The exact empty sequent and active calculus are fixed; the dependency on Cut elimination remains a sketch. |
| `thm:p07-craig-interpolation` | Sentence hypotheses, semantic implication, common nonlogical vocabulary, equality/`\bot` allowance, and degenerate cases survive; status remains cited. |
| `thm:p07-beth-definability` | The theory/reduct hypothesis, arity of `R`, `\Lang`-formula, and exact explicit-definition conclusion survive; status remains cited. |
| `thm:p07-normalization` | Exact NJ rule inventory, reduction relation, same conclusion, and no-new-open-assumption clause survive; RAA/equality/induction exclusions remain; status remains sketch. |
| `thm:p07-stlc-subject-reduction` | One compatible beta step, exact typing context/type, substitution lemma, and capture-avoidance obligation survive; status remains sketch. |
| `thm:p07-stlc-strong-normalization` | The claim quantifies over terms typable in the arrow-only registered STLC and excludes infinite compatible beta reduction; reducibility closure lemmas remain omitted; status remains sketch. |
| `thm:p07-gentzen-consistency` | The selected derivation/notation/reduction presentation, transfinite-induction metatheory, relative consistency conclusion, and internal boundary survive; status remains cited. |

No sampled statement lost a hypothesis or gained an evidence class.  The
additional register-driven results were checked against the frozen research
note: midsequent/Herbrand retain prenex, equality-free, ground-term, and
signature qualifications; Church--Rosser is confluence rather than
normalization; Church-style System-F checking is separated from Curry-style
undecidability; the MLTT theorem is limited to the cited one-universe
dependent-function calculus; number realizability is not used as a
countermodel to Markov's principle; the epsilon theorems are equality-free;
and Haken's bound is tied to one exact PHP encoding and resolution-size
measure.

## Complete-proof compression evidence

Only complete proofs inherited from v1.1 receive a source-compression
denominator.  Using the established one-pass `detex` alphabetic-word method,
excluding result statements and proof delimiters:

| Complete source proof | Source words | Annex words | Ratio | Verdict |
|---|---:|---:|---:|---|
| Cut/Mix equipollence, 11741--11766 | 150 | 68 | 45.3% | Inside the 40--60% Tier-2 band; both directions remain complete. |
| Cut-free propositional subformula lemma, 11824--11841 | 37 | 21 | 56.8% | Inside the 40--60% Tier-2 band; the complete height induction remains. |

There is **no ratio rule** for source proof sketches, new proofs, or new
proof sketches.  No denominator is manufactured for LK soundness, Cut
elimination, analytic existence, empty-sequent underivability, NJ
normalization, STLC preservation/normalization, the new canonical/defined-
negation translation, the new Maehara method, the new Church--Rosser sketch,
or the new cut-free-LJ last-rule proof.  Their evidence is governed by logical
completeness and explicit omission ledgers, not length tuning.

## Exact 43-result status graph

Every theorem-class body entry appears exactly once below.

| Chapter | Body label | Exact status destination |
|---|---|---|
| 7.1 | `thm:p07-lkd-soundness` | `sketched=annex:p7.calculi.1` |
| 7.1 | `thm:p07-lk-presentation-equivalence` | `sketched=annex:p7.calculi.2` |
| 7.1 | `thm:p07-lk-nd-equivalence` | `cited=Gentzen1934a` |
| 7.2 | `thm:p07-cut-mix-equivalence` | `proved=annex:p7.cut.1` |
| 7.2 | `thm:p07-cut-elimination` | `sketched=annex:p7.cut.2` |
| 7.2 | `thm:p07-cut-free-subformula` | `proved=annex:p7.cut.3` |
| 7.2 | `thm:p07-propositional-analytic-existence` | `sketched=annex:p7.cut.4` |
| 7.2 | `thm:p07-empty-sequent` | `sketched=annex:p7.cut.5` |
| 7.2 | `thm:p07-midsequent` | `cited=Takeuti1987` |
| 7.2 | `thm:p07-herbrand-midsequent` | `cited=Takeuti1987` |
| 7.2 | `thm:p07-maehara-partition` | `sketched=annex:p7.interp.1` |
| 7.2 | `thm:p07-craig-interpolation` | `cited=Craig1957` |
| 7.2 | `thm:p07-beth-definability` | `cited=Beth1953` |
| 7.3 | `thm:p07-normalization` | `sketched=annex:p7.norm.1` |
| 7.3 | `thm:p07-stlc-subject-reduction` | `sketched=annex:p7.norm.2` |
| 7.3 | `thm:p07-stlc-strong-normalization` | `sketched=annex:p7.norm.3` |
| 7.4 | `thm:p07-church-rosser` | `sketched=annex:p7.lambda.1` |
| 7.4 | `thm:p07-beta-normal-form-unique` | `sketched=annex:p7.lambda.2` |
| 7.4 | `thm:p07-lambda-partial-recursive` | `cited=Kleene1936` |
| 7.4 | `thm:p07-bracket-abstraction` | `cited=CurryFeys1958` |
| 7.4 | `thm:p07-system-f-confluence` | `cited=GirardLafontTaylor1989` |
| 7.4 | `thm:p07-system-f-strong-normalization` | `cited=Girard1972` |
| 7.4 | `thm:p07-system-f-church-checking` | `cited=GirardLafontTaylor1989` |
| 7.4 | `thm:p07-system-f-curry-undecidable` | `cited=Wells1999` |
| 7.4 | `thm:p07-mltt-normalization-decision` | `cited=AbelCoquandDybjer2007` |
| 7.4 | `thm:p07-coc-strong-normalization` | `cited=CoquandHuet1988` |
| 7.5 | `thm:p07-gentzen-consistency` | `cited=Gentzen1936` |
| 7.5 | `thm:p07-feferman-schuette` | `cited=Feferman1964` |
| 7.6 | `thm:p07-dialectica-soundness` | `cited=AvigadFeferman1998` |
| 7.6 | `thm:p07-dialectica-consistency` | `cited=AvigadFeferman1998` |
| 7.6 | `thm:p07-number-realizability-soundness` | `cited=Kleene1945` |
| 7.6 | `thm:p07-ect-characterization` | `cited=Troelstra1998` |
| 7.6 | `thm:p07-markov-realizability-boundary` | `cited=TroelstraVanDalen1988` |
| 7.6 | `thm:p07-lj-disjunction-last-rule` | `proved=annex:p7.functional.1` |
| 7.6 | `thm:p07-ipc-disjunction-property` | `cited=TroelstraVanDalen1988` |
| 7.6 | `thm:p07-ha-disjunction-property` | `cited=TroelstraVanDalen1988` |
| 7.6 | `thm:p07-ha-numerical-existence` | `cited=TroelstraVanDalen1988` |
| 7.7 | `thm:p07-first-epsilon` | `cited=MoserZach2006` |
| 7.7 | `thm:p07-extended-first-epsilon` | `cited=MoserZach2006` |
| 7.7 | `thm:p07-second-epsilon` | `cited=MoserZach2006` |
| 7.8 | `thm:p07-cook-reckhow-np-conp` | `cited=CookReckhow1979` |
| 7.8 | `thm:p07-haken-resolution-lower-bound` | `cited=Haken1985` |
| 7.8 | `thm:p07-frege-lower-bound-boundary` | `cited=Alekseev2026` |

The exact annex back-reference graph is:

| Annex label | Sole body back-reference | Evidence class |
|---|---|---|
| `annex:p7.calculi.1` | `thm:p07-lkd-soundness` | inherited sketch |
| `annex:p7.calculi.2` | `thm:p07-lk-presentation-equivalence` | new repair sketch |
| `annex:p7.cut.1` | `thm:p07-cut-mix-equivalence` | inherited complete proof |
| `annex:p7.cut.2` | `thm:p07-cut-elimination` | inherited Tier-1 sketch |
| `annex:p7.cut.3` | `thm:p07-cut-free-subformula` | inherited complete proof |
| `annex:p7.cut.4` | `thm:p07-propositional-analytic-existence` | inherited dependent sketch |
| `annex:p7.cut.5` | `thm:p07-empty-sequent` | inherited dependent sketch |
| `annex:p7.interp.1` | `thm:p07-maehara-partition` | new register-driven sketch |
| `annex:p7.norm.1` | `thm:p07-normalization` | inherited sketch |
| `annex:p7.norm.2` | `thm:p07-stlc-subject-reduction` | inherited sketch |
| `annex:p7.norm.3` | `thm:p07-stlc-strong-normalization` | inherited sketch |
| `annex:p7.lambda.1` | `thm:p07-church-rosser` | new register-driven sketch |
| `annex:p7.lambda.2` | `thm:p07-beta-normal-form-unique` | new dependent sketch |
| `annex:p7.functional.1` | `thm:p07-lj-disjunction-last-rule` | new complete proof |

All 29 cited results have no annex item, as required.
An independent navigation scan also found each of the 43 body labels exactly
once, and no label more than once, in apparatus A-189.

## Depth-row reconciliation

`Done-candidate` here means that the actual tree supplies the requested
treatment while preserving evidence status; it does not itself mutate the
CSV.  `Open` means the finalizer must leave the CSV row open.

| Row | Ceiling / priority | Verification disposition |
|---|---|---|
| `D-P8-001` | E / must | **Done-candidate.** The finite-sequent lookup records propositional and equality-free FOL completeness, empty contexts, the finite-disjunction reduction, Choice for FOL, and current sketch statuses without duplicating P2 annex evidence. |
| `D-P8-002` | E / must | **Done-candidate.** Exact finite equality-free LK-to-classical-ND derivability equivalence, including empty succedent and the multiplicity-forgetting convention, is cited. |
| `D-P8-003` | S / should | **Done-candidate.** Midsequent and Herbrand-route statements are prenex, equality-free, regular, and ground-term qualified and point to P2's full Herbrand forms. |
| `D-P8-004` | E / must | **Open; explicit stub.** The E entry, exact partition definition, Maehara method, and sketched local partition lemma exist, but the literal local-Craig-proof ceiling is unmet.  Craig/Beth remain cited; the stub prevents an inherited-status upgrade from being reported as completion. |
| `D-P8-005` | S / should | **Done-candidate at S.** The exact cited Gentzen result, derivation/notation/reduction component ledger, relative metatheory, and proof boundary exist.  This does not fill the stronger `N-a-049` table obligation. |
| `D-P8-006` | T / should | **Done-candidate.** The calibration-relative definition and local table through PA, fragments, `\Gamma_0`, and selected stronger systems are supplied with qualifications.  Master apparatus A-074 remains Phase 6. |
| `D-P8-007` | S / should | **Done-candidate.** Cook--Reckhow, exact PHP/resolution lower bound, Frege/extended-Frege boundary, and system-comparison table are present. |
| `D-P9-003` | E / must | **Done-candidate.** Untyped syntax/substitution/conversion, parallel-reduction method, Church--Rosser sketch, nonnormalizing counterexample, lambda-definability, and combinatory comparison are present. |
| `D-P9-004` | S / should | **Done-candidate.** Church-style System F, impredicative encodings, confluence/strong-normalization statements, Curry--Howard scope, parametricity pointer, and Church/Curry decision distinction are present. |
| `D-P10-031` | P / could | **Open; explicit stub.** The Phase-5 cross-domain pointer remains owed and is not confused with the P7 architecture survey. |

## New-content reconciliation

| Row | Ceiling / priority | Verification disposition |
|---|---|---|
| `N-a-015` | T / must | **Done-candidate.** Untyped lambda and S--K systems, Church--Rosser, computability calibration, and comparison table are supplied. |
| `N-a-049` | T / must | **Open; explicit stub.** No full selected propositional ordinal-assignment table or complete decrease-case inventory has been supplied. |
| `N-a-050` | S / should | **Done-candidate.** Cantor-normal-form dependency, Veblen hierarchy, `\Gamma_0`, and the Feferman--Schuette statement are present and cited. |
| `N-a-051` | S / should | **Done-candidate.** PRA and Tait's finitism calibration are separated; PRA is not simply defined as finitism and the 1923/1934 Skolem sources are not conflated. |
| `N-a-052` | S / could | **Open; explicit stub.** No omega-rule or infinitary Cut-elimination theorem is spliced into the finitary Gentzen entry. |
| `N-a-053` | S / should | **Done-candidate.** Exact System-T surface, target theory, six Dialectica clauses, cited HA soundness, and relative-consistency boundary are present. |
| `N-a-054` | T / must | **Done-candidate.** The full number-realizability clause table, HA soundness, almost-negative ECT restriction, and correct Markov boundary are present. |
| `N-a-055` | T / must | **Open; explicit stub.** The exact IPC/HA disjunction and HA numerical-existence statements are cited, and only the local cut-free-LJ last-rule lemma is proved; the requested matched full proofs remain absent. |
| `N-a-056` | S / should | **Done-candidate.** Equality-free epsilon syntax plus first, extended-first/Herbrand, and second epsilon theorem statements are exact and cited. |
| `N-a-057` | S / should | **Open; explicit stub.** The four architectures are defined and surveyed, but one complete modal derivation on each exact named sheet remains absent. |
| `N-a-058` | P / could | **Open; explicit stub.** Only the owed proof-mining pointer is named; no unsafely general extraction theorem is asserted. |
| `N-a-069` | S / should | **Done-candidate.** Exact midsequent and Herbrand-route statements are supplied with all required restrictions. |
| `N-a-070` | E / must | **Open; explicit stub.** The Maehara entry and local sketch exist, but the requested local Craig proof and Beth-corollary derivation do not.  Inherited Craig and Beth remain cited. |
| `N-c-027` | S / should | **Done-candidate.** Cook--Reckhow, p-simulation, fixed PHP encoding/size, Haken citation, and current Frege open-problem boundary are supplied. |
| `N-c-029` | S / must | **Done-candidate.** Exact Church-style System F plus the required metatheorem statements, second-order Curry--Howard, and parametricity pointer are supplied. |
| `N-c-030` | S / must | **Open; explicit stub.** The narrower Abel--Coquand--Dybjer and CoC theorems are cited, but no one matched MLTT sheet with Pi/Sigma/identity/universe rules exists. |
| `N-x-001` | P / excluded | **Pointer boundary delivered.** HoTT/univalence receives no technical expansion or theorem. |
| `N-x-002` | P / excluded | **Pointer boundary delivered.** HIT/cubical internals remain excluded. |
| `N-x-011` | P / excluded | **Pointer boundary delivered.** Geometry of interaction receives no operator-algebraic development. |
| `N-x-012` | P / excluded | **Pointer boundary delivered.** Proof nets receive no correctness or sequentialization theory. |

## Apparatus reconciliation

| Row | Phase | Verification disposition |
|---|---:|---|
| `A-069` | 6 | **Open/deferred.** P7 contributes calibration data but does not claim the Phase-6 master consistency-strength ladder. |
| `A-070` | 4 | **Open; explicit stub.** Exact LKd, LJ, IMLL, and Lambek rows exist; relevance has no family-wide profile and no exact affine presentation was selected, so those two rows were not fabricated. |
| `A-071` | 4 | **Done-candidate.** LK, LKd, LK-equality, LJ, NK alias, NJ, and citation-only generalized-framework rows state exact adequacy boundaries. |
| `A-072` | 4 | **Done-candidate.** Logic/type/category dictionary states the bicartesian-closed hypotheses and separates arrow-only live syntax from standard extensions. |
| `A-073` | 4 | **Done-candidate.** Untyped, STLC, both System-F presentations, the exact ACD MLTT core, and CoC/CIC boundary are compared without conflating confluence, normalization, checking, or inference. |
| `A-074` | 6 | **Open/deferred.** The local P7 calibration table is not the Phase-6 master table, especially not its Q-range requirement. |
| `A-075` | 4 | **Done-candidate.** Resolution, extended resolution, Frege, and extended Frege rows use one p-simulation definition and honest lower-bound/open-problem cells. |
| `A-151` | 4 | **Done-candidate.** The triangle's edges are named constructions rather than equalities; the categorical vertex has explicit hypotheses. |
| `A-152` | 4 | **Done-candidate.** A fully typed STLC composition derivation is paired with its NJ derivation; generic rules remain on sheets. |
| `A-186` | 4 | **Done-candidate.** P7 has an annotated further-reading route across sequent proof theory, lambda/type theory, ordinal analysis, interpretations, and proof complexity. |
| `A-189` | 4 | **Done-candidate.** Every P7 theorem-class result appears once in the body-to-sheet/body-to-annex table; cited results have no annex link and forward P8/P12 routes remain prose until labels exist. |

## Defect reconciliation

| Row | Verification disposition |
|---|---|
| `R-012` | **Preserved.** Mix is displayed and labeled on `sheet:lk-defneg` and `sheet:lj`; the measure is rank plus the sum of immediate-subderivation heights; dependent corollaries remain sketches. |
| `R-042` | **Resolved in the live P7 tree, pending register reconciliation.** LK, LKd, and LK-equality have distinct names/inventories; the inherited Cut-elimination scope excludes equality; symmetric equality replacement explicitly uses Cut. |
| `S-012` | **Resolved in the live P7 tree, pending register reconciliation.** Canonical LK is fixed, LKd is named, and `thm:p07-lk-presentation-equivalence` is labeled without claiming cut-free preservation. |
| `S-013` | **Resolved in the live P7 tree, pending register reconciliation.** Propositional analytic derivation and first-order analyticity modulo terms are defined at first use. |
| `L-001` | **Preserved.** No body proof/rule display revives the bracketed matrix failure; the paired derivation uses stable TikZ nodes and sheet links.  Final compile and rendered evidence passes below. |
| `L-005` | **Resolved by migration, pending register reconciliation.** Rule displays are registry-generated with five-argument `\hbrule` rows; the retired body macro is not reintroduced. |

## Exact ten-stub ledger

1. `A-070` -- relevance and affine structural-comparison rows lack selected
   source-exact presentations.
2. `D-P8-004` -- the E-level local Craig proof demanded by the literal row.
3. `N-a-070` -- the corresponding local Craig proof and Beth-corollary
   derivation.
4. `N-a-049` -- full propositional ordinal assignment and all decrease cases.
5. `N-a-052` -- omega logic, its Cut elimination, and epsilon-zero bound.
6. `N-a-055` -- matched full proofs of IPC/HA disjunction and HA numerical
   existence.
7. `N-a-057` -- one complete modal derivation for each of four exact
   generalized-framework sheets.
8. `D-P10-031` -- Phase-5 cross-domain generalized-calculi pointer.
9. `N-a-058` -- proof-mining pointer at its P/could ceiling.
10. `N-c-030` -- one matched MLTT sheet with Pi/Sigma/identity/universe rules.

The stub count is a property of the current P7 body, not a claim that all ten
rows have the same priority.  Six depth/new-content stubs are must/should
remainders, three are could/pointer remainders, and one is the partially
complete must-priority A-070 apparatus row.  Stubbed or partial rows must
remain open.

## Adversarial correction log

The writing and independent review passes corrected or made explicit:

- the canonical-LK/defined-negation-LK/LK-equality identities, including the
  nontransport of cut-free proofs across the presentation equivalence;
- R-012 Mix homing on LKd and LJ, with canonical/equality rows expressly
  denying inherited Cut-admissibility coverage and equality symmetry stating
  its use of Cut;
- the exact formula-rank and derivation-height operations, replacing the
  collision with global term metavariables `r,t`;
- formula metavariables `A,B,C` to the global `\varphi,\psi,\chi` convention,
  and mandatory per-system derivability subscripts;
- raw formula-equivalence/implication glyphs, the term-substitution
  metavariable collision at `\theta`, raw `\mathcal L`, and the untyped
  empty-sequent assertion;
- the STLC type arrow, typing judgment, and context annotations, separating
  `\to_{\mathrm{ty}}` from object-language implication and removing raw
  grammar-production notation;
- the exact Beth signature, arity, reduct, and explicit-definition statement,
  while keeping Craig/Beth citation-only;
- the first-order midsequent/Herbrand hypotheses: prenex form, equality-free
  calculus, regular eigenvariables, and a ground term or fresh constant;
- the definition of analytic derivation and the first-order
  substitution/eigenvariable qualification;
- the Maehara partition convention, calculus, vocabulary invariant, and full
  omitted-case ledger, without using it to upgrade inherited Craig/Beth;
- A-070's nonfabrication of generic relevance/affine rows and A-071's
  citation-only labelled-calculus pointer;
- the A-071 citation-only labelled-calculus row, whose unregistered
  labelled-formula and relational-atom glyphs were removed in favor of exact
  prose without introducing a live calculus sheet;
- the `\Gamma_0` registry role, whose mojibake was normalized to the ASCII
  source string `Feferman--Schuette ordinal`; the final rendered symbol table
  shows the intended en dash and no encoding defect;
- A-152's fully typed contexts and the categorical triangle's syntactic-
  category/internal-language/beta--eta quotient hypotheses;
- Church--Rosser's separation from normalization and the complete list of
  omitted parallel-reduction lemmas;
- System F's Church/Curry presentation and decision-problem distinction;
- the MLTT boundary between the broad owed calculus and the narrower cited
  Abel--Coquand--Dybjer theorem;
- Gentzen's analysis-relative standing, PRA/finitism separation, and the
  explicit `N-a-049`/`N-a-052` remainders;
- Dialectica's exact target/clauses, number realizability's correct Markov
  boundary, and the refusal to infer HA constructive properties from the
  equality-free/induction-free inherited normalization sketch;
- equality-free hypotheses on all three epsilon theorems; and
- the fixed PHP encoding and resolution-size measure, p-simulation rather
  than shortest-proof comparison, and the nontransfer of Haken's bound to
  Frege or extended Frege.

The two complete source proofs were then recounted at 45.3% and 56.8% and
left unchanged; sketches and new proofs were not ratio-tuned.

## Mechanical evidence

- Exact local result/annex graph scan: **PASS** -- 43 results (3 proved, 11
  sketched, 29 cited), 14 annex items, zero unresolved targets, zero orphans,
  zero duplicate targets/back-references, and zero pair mismatches.
- Exact local stub scan: **PASS** -- ten P7 stubs, exactly the rows listed
  above.
- Independent register/spec reconciliation: **PASS** -- the second reviewer
  agreed with every done-candidate/open/deferred disposition and independently
  recovered the same ten explicit boxes.  This is agent review, not human
  mathematical verification.
- Body/annex separation scan: **PASS** -- the P7 body contains zero
  `\hbrule`, `\begin{proof}`, `\begin{proofplan}`, `\infer`, `\frac`, or
  `\dfrac` occurrences; all 14 status-targeted proof objects are annex items
  and generic rules remain on registry sheets.
- Verification-record self-check: **PASS** -- all 10 depth IDs, 20
  new-content IDs, 11 apparatus IDs, 6 governing defect IDs, 43 live result
  labels, and 14 live annex labels occur in this record; its nine Markdown
  tables have consistent column counts, with no tabs, trailing whitespace, or
  `git diff --check` finding.
- Final integrated TeX Live 2025 build: **PASS** -- the finalizer's authoritative
  `handbook/main.pdf` has 665 pages, 2,336,561 bytes, and filesystem timestamp
  2026-08-11 12:29:35 PDT.  Its SHA-256 digest is
  `1CAF8D34B077EEB83AB5B8ADE31D51A55E2DCFB075B6996390B0FAF0BB031857`.
  This is the artifact inspected below, not an earlier mixed-toolchain build.
- Final `python tools/check.py --tree handbook --strict`: **PASS** -- 443
  symbol rows (421 distinct glyphs), 407 bibliography entries (2 pre-existing
  intake stubs), 143 proved / 44 sketched / 163 cited / 0 malformed status forms,
  and 38 handbook stubs in total, including exactly 10 in P7; all hard checks
  passed.
- `python tools/check.py --tree source`: **PASS** -- all hard checks passed;
  185 source result environments, 126 with status markers.  The live source
  blob and `v1.1-verified:source/formal-logic-reference.tex` both have Git
  object hash `ea8c2fa647a387817171468199f989b30de6bdf6`.
- Final text-tree integrity: **PASS** -- `git diff --check` reports no finding,
  and `git diff --exit-code -- source` confirms that the frozen source tree is
  unchanged.  `tools/symbols2tex.py` and `tools/audit_tables.py` both pass; the
  regenerated audit has 113 P7 entries and 770 entries in total.  The
  finalizer's build/log gate also passed with no error, undefined reference,
  undefined citation, or undefined-control-sequence diagnostic.

## Visual evidence

- Authoritative ranges: P7 title/body physical pages 405--472, P7 rule sheets
  physical pages 523--530, and P7 annex physical pages 605--612.  All 84 pages
  were rendered from the final artifact at 110 dpi and inspected, including
  every page in each range rather than a sample.
- Rendered inspection: **PASS** -- no clipping, overlap, broken glyph,
  unreadable rule metric, malformed stub box, bad running head, or illegible
  table/figure was found.  Dense landscape material was additionally checked
  on physical pages 425 (Curry--Howard table/triangle), 426 (A-152 paired
  STLC/NJ derivation), 439 (A-073 lambda/type table), 464 (A-075 proof-
  complexity table), and 466--467 (A-189 navigation table).
- Page transitions: physical page 406 is the intentional blank verso after
  the Part VII title page; physical page 612 is completely blank.  Transition
  and header-only versos 414, 428, 440, 448, and 456 are consistent and free
  of stray marks.  The corrected physical-page-443 running head reads
  `45.2. THEORY PRESENTATIONS` with clear separation from the printed page
  number.
- Final standards-fix renders: physical page 412 shows the prose-only A-071
  Negri row cleanly, with no resurrected unregistered formula/atom glyphs.
  The finalizer's independent inspection of physical page 63 confirms that
  the P7 symbol-table row renders `Feferman--Schuette ordinal` with the intended
  dash, no mojibake, and no clipping.
- TeX diagnostics: the final log gate has no error, undefined reference,
  undefined citation, or undefined-control-sequence diagnostic.  Nonfatal
  global box diagnostics remain in the full handbook log, but the complete
  rendered P7 ranges show no corresponding clipping, overlap, or legibility
  defect.

Final P7 verification verdict: **PASS**.

Compilation and rendering establish integration and presentation only.  They
do not replace the mathematical/status/source verification above or
independent human mathematical review.

# Remaining original defect components — current inventory

All **58 assigned defect rows** have been investigated. These are the 88 original rows minus the 30 IDs in `defect-mapping-completion.json`. No assigned row remains unread or unaccounted for. The JSON preserves every original CSV field, historical status and disposition, and gives component findings, exact current paths/ranges/hashes, active or inactive routing, and remaining obligations.

Snapshot: 2026-09-07 11:02:03 UTC. Register SHA-256: `7bdfb09005dd4035672f6267fa6cd74ec8a505aa3abb7a734ee1b0592fc939b0`.

## Scope and evidence

This is a component inventory of the original required fixes and acceptance clauses. A supplied argument, an explicitly incomplete source sketch, a cited dependency, a policy conflict, and an output-only verification requirement are recorded separately. A row marked `repair_present` means the original bounded repair components were found and read; it does not accept all theorem dependencies or the book for publication. Historical `fixed(commit)` and `open` values are preserved without treating either as a current verdict.

The inventory completed full sequential reads of the small restoration fragments needed for the mathematical repairs, and bounded reads of the particular source/registry/policy components needed for broader requirements. All explicit intervals are listed below. Previously completed apparatus/feedback readings are reused only under matching current hashes and with their original reading scope stated. There were no manuscript, register or bibliography changes, source acquisitions, tests, builds or renders.

## Outcomes

| Current component disposition | Rows |
| --- | ---: |
| repair_present | 31 |
| repair_partial | 8 |
| confirmed_remaining | 2 |
| policy_conflict | 14 |
| partial_with_output_unknown | 1 |
| policy_and_output_boundary | 1 |
| source_present_output_unverified | 1 |

The main remaining mathematical or source-interface components are:

- **R-002:** the bounded computation-verification theorem still explicitly omits the full arithmetic transcription of the encoded computation checks. The present pairing and bounded-extraction proofs do not supply that transcription.
- **R-005:** the numbering theorem has a full supplied proof and direct Rice/recursion references, but Post's paragraph reaches it only through the relativized-adequacy/jump dependency chain, rather than its requested direct reference.
- **R-014:** arbitrary finite-sequent completeness is fully supplied for canonical equality-free LK. The inherited equality-capable ND–LK translation remains an explicit sketch. This is a proof boundary, not evidence that arbitrary succedents are still unstated.
- **R-017:** the four cardinal-coding clauses share a cited theorem. The syntax-counting consequence is separately proved, but exact per-clause source evidence and the originally requested split remain incomplete.
- **R-032:** the active expanded-signature `PA₂` reduction has no prior definition of that symbol as the conjunction of the complete finite axioms. The detailed `def:p02-pa2` with addition/multiplication recursion axioms is in an inactive file.

Further concrete source/apparatus components include S-005's inactive requested theorem home; S-017's missing real Glivenko/Gödel citations at the active result rather than printed `cited=...` text; L-007's actual unlabelled section commands; L-010's three missing/inactive figure surfaces and incomplete CTL root valuation; and L-018's mixed caption/head/foot coverage. Each is specified below.

## Policy and source boundaries

`handbook/CONVENTIONS.md:3–19` records both the later direct-correction instruction and the compendium preservation policy. Known mathematical errors belong in the active definitions/proofs as corrections. Correctly typed source notation, original proof boundaries and supplied exercises remain source content. Thus the universal house-notation requirements S-002/S-003/S-021/L-016 and the literal source-wide status/rule-display bans cannot be closed by deleting or normalizing source material. The registry's remaining absolute wording still needs reconciliation with its own local-scope exceptions.

The original retirement dispositions S-024/S-025 are superseded: the current P12 route includes the exercises and selected solutions. The five additional qualifying problems have no supplied solutions in that source fragment. Source retention does not itself impose newly written answers or new exercises in every chapter; such a publication requirement needs to be stated explicitly.

## Row-level findings

### Rigor

#### R-001 — repair_present

Historical status: `fixed (4201fbf)`; disposition: `FIX-SOURCE`; historical coordinates: `9062--9133` in `VII.forcing`. Those coordinates are not the current file lines.

Original required fix: Rewrite per the book's own Warning: either present relative consistency with honest cited status or give the correct syntactic route (forcing over finite fragments / ctm with the inaccessibility caveat), deleting the two-structures soundness justification.

- **Relative consistency of not CH with honest imported standing — present.** inherited-11240-11279:1–39 gives cited Jech Chapter14 Boolean-valued theorem schemes, syntactic contradiction, and no countable transitive model hypothesis. Proof standing: `cited_dependency`.
- **Nonderivability without unexhibited models — present.** inherited-11294-11314:7–19 uses monotonicity, assumption, negation elimination and the two consistency claims. Proof standing: `local_proof`.
- **Stronger arithmetized claim — explicit_sketch.** inherited-11280-11293:1–12 expressly leaves primitive-recursive calculus translation/arithmetization unproved. Proof standing: `source_sketch`.

Remaining: Exact original repair is present; the separately labelled arithmetized strengthening remains a sketch.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-002 — repair_partial

Historical status: `fixed (563da95)`; disposition: `FIX-SOURCE`; historical coordinates: `7011--7031 vs 6567--6585, 7440--7454` in `V--VI.coding`. Those coordinates are not the current file lines.

Original required fix: Adopt a single coding with a proved bounded-extraction lemma covering machine codes as well as histories, and re-derive the \(\Sigma^0_1\) form of \(\mathsf{Comp}\) and \(\mathsf{Prov}_T\) from it.

- **Consistent coding covers both machine tables and histories — present.** 07851:19–39 fixes paired machine-table numbering; 08710:3–34 stores its certified decoding and histories in one beta-coded witness.
- **Labelled bounded-extraction primitives with proofs — present.** 08439:1–25 proves pairing graph and component bounds; 37–83 proves bounded beta extraction, uniqueness and sequence realization. Proof standing: `supplied_local_proof`.
- **Fully derive the Comp arithmetic verifier — partial.** 08710:37–81 gives a labelled bounded-verification theorem explicitly marked proof sketch; 77–80 names omitted full h1–h4 transcription and step/digit verification. Proof standing: `source_sketch`.
- **Prov_T Sigma1 derivation and coding link — partial.** 09328:65–84 defines Prov_T, explains prefix merge and explicitly links beta to tables/histories/proofs. Arithmetization at46–63 remains a sketch; representability at09262:31–48 is cited. Proof standing: `mixed`.

Remaining: The former contradictory coding prose is replaced by a coherent layered scheme, but the full bounded computation formula and step verification required by the original repair are expressly unprovided. Provability also retains the stated arithmetization/representability proof boundary.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### R-003 — repair_present

Historical status: `fixed (563da95)`; disposition: `FIX-SOURCE`; historical coordinates: `7666--7699` in `VI.incompleteness`. Those coordinates are not the current file lines.

Original required fix: Define and register object \(\leq\) (or eliminate it in favor of \(<\)) and state and prove or cite both Q-lemmas as labeled results before the sketch uses them.

- **Define and register arithmetic <= before use — present.** 08306:43–59 fixes r<=t as exists z(z+r=t). Actual symbols.csv rows80/82 register P4.3/P5.1 roles; P5 imports the convention before its Q lemmas.
- **Labelled bounded-case enumeration with honest status — present.** 09112:10–38 supplies lem:q-bounded-cases and full zero/successor metainduction using precisely Q's right-recursive addition axioms. Proof standing: `supplied_local_proof`.
- **Labelled dichotomy with honest status — present.** 09150:2–25 supplies lem:q-dichotomy and both cases of its metainduction. Proof standing: `supplied_local_proof`.
- **Rosser explicitly references both needed lemmas — present.** 09620:42 and52–53 cite them at their exact uses;67–70 distinguish complete bounded comparisons from Rosser's remaining representability/diagonal sketch. Proof standing: `mixed`.

Remaining: No remaining component of the original <=/two-lemma repair. The surrounding Rosser theorem remains honestly a sketch for separate dependencies; this row does not certify that whole theorem.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-004 — repair_present

Historical status: `fixed (563da95)`; disposition: `FIX-SOURCE`; historical coordinates: `7154--7165` in `V.computability`. Those coordinates are not the current file lines.

Original required fix: Align the halting predicate with the numbering's convergence notion (or adjust the numbering) and promote the jump theorem to a labeled result with status and proof or citation.

- **K and jump use valid numerical-output convergence — present.** 07851:33–39 fixes convergence;08081:4–6 defines K by definedness;08898:34–51 uses the same oracle definedness.
- **Jump theorem labelled and statused with displayed argument — present.** 08898:88–124 gives thm:jump, both conclusions and the diagonal argument. Its proof-sketch status explicitly acknowledges relativized universal/adequacy dependencies. Proof standing: `source_sketch`.
- **Downstream strictness cites the jump theorem — present.** 08898:137–151 names thm:jump in the Post-to-strictness derivation;153–181 separates source halting convention alignment. Proof standing: `mixed`.

Remaining: Original convergence/label/status/use repair is present. The relativized machinery and convention bridge remain sketches, so no full independent proof of the jump theorem is certified.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-005 — repair_partial

Historical status: `fixed (563da95)`; disposition: `FIX-SOURCE`; historical coordinates: `6564--6593` in `V.computability`. Those coordinates are not the current file lines.

Original required fix: State the enumeration theorem as a labeled result with a proof (or precise citation) tied to the constructed numbering.

- **Labelled enumeration theorem tied to actual numbering — present.** 07851:85–146 states both directions and proves wrappers, designated symbols, surrogate start, renaming and valid-code construction. Proof standing: `supplied_local_proof`.
- **Rice and recursion explicitly reference enumeration — present.** 08187:33–35 and08144:19–21 explicitly cite thm:enumeration.
- **Post explicitly references enumeration at its use — partial.** 08898:72 names enumeration in the relativized-adequacy proof; Post at126–151 cites its external source and jump theorem. Thus a dependency chain exists, but no direct enumeration citation occurs in the Post statement/proof paragraph.

Remaining: The substantive enumeration theorem and its immediate consumers are supplied. The exact original direct-reference-at-Post acceptance is only met through the explicit relativized-adequacy/jump chain; decide whether that satisfies the intended citation component rather than calling the entire row generically verified.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### R-006 — repair_present

Historical status: `fixed (563da95)`; disposition: `FIX-SOURCE`; historical coordinates: `6952--6971` in `V.hierarchy`. Those coordinates are not the current file lines.

Original required fix: State and prove the bounded-collection lemma and derive the closure-class/prenex equivalence as a labeled theorem.

- **Bounded-collection/exchange lemma stated and proved — present.** 08439:120–151 gives labelled standard-model exchange, finite maximum including zero bound, freshness and dual argument. Proof standing: `supplied_local_proof`.
- **Closure hierarchy and prefix classes explicitly reconciled — present.** 08306:61–124 fixes syntactic/boldface classes;08439:153–270 supplies thm:prefix-normal-form with padding, pairing contraction, Boolean/bounded/unbounded cases and duals. Proof standing: `supplied_local_proof`.
- **Downstream hierarchy results use the equivalence — present.** 08710:83–87,134–159 and08898:137–140 explicitly cite thm:prefix-normal-form when importing prefix-source results.

Remaining: No remaining original exchange/prenex-equivalence component. This is scoped verification of the written proof and uses, not independent acceptance of every imported hierarchy result.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-007 — repair_present

Historical status: `fixed (fe1f17d)`; disposition: `FIX-SOURCE`; historical coordinates: `4420--4446` in `III.normalforms`. Those coordinates are not the current file lines.

Original required fix: Prove first-order NNF existence and rectified-variant existence as labeled lemmas, state the preservation invariant, and run the prenex induction on them.

- **Independent first-order NNF and rectification inductions — present.** inherited-05132-05567:25–181: mutually recursive NNF conversion, free-variable calculation, fresh-variable rectification with Var invariant. Proof standing: `local_proof`.
- **Prenex side conditions and result — present.** same:183–282: extraction with FV/Var invariant and quantifier-occurrence bound; theorem composes three first-order lemmas and uses stated commutations. Proof standing: `local_proof`.

Remaining: No original repair component remains. Full imported commutation and substitution dependency acceptance is outside this inventory.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-008 — repair_present

Historical status: `fixed (fe1f17d)`; disposition: `FIX-SOURCE`; historical coordinates: `4480--4507` in `III.skolem`. Those coordinates are not the current file lines.

Original required fix: Write the induction with an explicit hypothesis and cases, remove or define the game terminology, and separate the AC-using direction from the choice-free one.

- **Choice scope and source semantics — present.** inherited-05132-05567:316–354 states expansion direction uses AC; fixed residual prefix, universal-variable tuple and Skolem interpretation defined.
- **Both invariant directions — present.** same:356–429 has forward Inv(i), existential family choice only at382–388, reverse Inv'(i), both quantifier cases and reduct conclusion. Proof standing: `local_proof`.

Remaining: Exact replacement of an informal game argument is supplied.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-009 — repair_present

Historical status: `fixed (fe1f17d)`; disposition: `FIX-SOURCE`; historical coordinates: `3934--3985` in `III.henkin`. Those coordinates are not the current file lines.

Original required fix: Redo the maximality step by transfinite recursion with explicit successor and limit stages and the union/chain argument.

- **Transfinite maximal extension lemma — present.** inherited-04306-04575:154–210: ordinal enumeration; successor consistency choice; limit union; finite derivation argument including empty support; completeness/maximality. Proof standing: `local_proof`.
- **Henkin consumer — present.** same:257–268 explicitly applies transfinite Lindenbaum after witness stages, not the propositional omega lemma. Proof standing: `local_proof`.

Remaining: No original repair component remains.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-011 — repair_present

Historical status: `fixed (2465859)`; disposition: `FIX-SOURCE`; historical coordinates: `1958--1965` in `II.normalforms`. Those coordinates are not the current file lines.

Original required fix: Give the CNF half a genuine induction (or dualize the DNF argument) with the degenerate cases handled explicitly.

- **Clause/form interpretation and dual CNF construction — present.** inherited-01946-02186:4–95 fixes finite clause/set interpretation and proves satisfaction;117–208 gives valuation-indexed DNF followed by explicit dual CNF. Proof standing: `local_proof`.
- **Truth constants and no-variable cases — present.** same:188–207 identifies valid/top, variable-free false/single empty clause, and proves equivalence via coincidence. Proof standing: `local_proof`.

Remaining: Original permitted dualization route is fully supplied.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-012 — repair_present

Historical status: `fixed (2465859)`; disposition: `FIX-SOURCE`; historical coordinates: `9513--9548, 9555, 9575` in `VIII.cutelim`. Those coordinates are not the current file lines.

Original required fix: Display and label the mix rule, restate the measure for the rule actually eliminated, and either complete the induction or downgrade the corollaries' status to match the sketch.

- **Stable Mix-rule labels — present.** registry/calculi/lk-defneg.tex:13 displays hbrule rule:lkd-mix; canonical lk.tex:30 separately names its own derived Mix. The source fractions remain source-specific.
- **Exact multiplicity-aware reduction measure — present.** inherited-11711-11740:14–29 displays Mix;11741-11767 proves Cut/Mix equipollence;11768-11823:1–9 defines rank and sum-of-heights. Proof standing: `local_proof`.
- **Honest cut-elimination boundary and consumers — present.** inherited-11768-11823:11–55 expressly marks sketch and omits calculus-specific case table;11824-11881:20–57 marks dependent analytic-existence and empty-sequent corollaries sketches; cut-free propositional subformula lemma alone has a local proof. Proof standing: `mixed`.

Remaining: Exact original option to downgrade sketch-dependent claims is met. The general cut-elimination proof is still not supplied.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-014 — repair_partial

Historical status: `fixed (fe1f17d)`; disposition: `FIX-SOURCE`; historical coordinates: `2488 vs 2295; 4165 vs 3674` in `II--III.sequent`. Those coordinates are not the current file lines.

Original required fix: State and prove LK completeness for arbitrary sequents, or scope both metatheorems to the same sequent class with an explicit remark.

- **General finite sequent statements including empty contexts — present.** inherited-04713-04920:120–207 restates arbitrary Γ⇒Δ; parts/p07/calculi-and-derivability-supplement:215–229 distinguishes canonical equality-free theorem.
- **Full canonical equality-free completeness — present.** annex/p07/calculi-and-cut-elimination-supplement:50–217 supplies both LK–ND translations and finite-sequent completeness, including empty succedent and multiplicities. Proof standing: `local_proof`.
- **Inherited equality-capable ND–LK translation — partial.** inherited-04713-04920:130–152,204–206 still explicitly omits individual translation trees/subinductions; canonical new proof excludes equality. Proof standing: `source_sketch`.

Remaining: Equality-inclusive inherited translation remains a sketch. The new canonical theorem meets the equality-free interface only.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### R-015 — repair_present

Historical status: `fixed (2465859)`; disposition: `FIX-SOURCE`; historical coordinates: `5994--6015` in `IV.qe`. Those coordinates are not the current file lines.

Original required fix: Add the reduction from arbitrary embeddings to substructure inclusions or restate the definition to match the proof.

- **All embeddings reduced to inclusions — present.** inherited-07150-07294:82–110 factors h through h[M], invokes image-isomorphism and sentence invariance, then elementary inclusion. Proof standing: `local_proof`.
- **DLO use — present.** same:127–134 applies the labelled reduction. DLO QE remains cited and corollary sketch. Proof standing: `mixed`.

Remaining: No original quantifier-range repair remains.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-016 — repair_present

Historical status: `fixed (2465859)`; disposition: `FIX-SOURCE`; historical coordinates: `6068--6110` in `IV.backforth`. Those coordinates are not the current file lines.

Original required fix: Add the extension clause to the theorem statement.

- **Extension clause and proof — present.** inherited-07295-07468:43–75 states every given f0∈F extends to an isomorphism and proves union contains f0. Proof standing: `local_proof`.
- **Corollary interface — present.** same:79–105 applies thm:back-and-forth-test with original f and separately constructs forth/back extensions. Proof standing: `local_proof`.

Remaining: Exact original clause now occurs in the theorem and consumer.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-017 — repair_partial

Historical status: `fixed (4201fbf)`; disposition: `FIX-SOURCE`; historical coordinates: `678--702` in `I.cardinality`. Those coordinates are not the current file lines.

Original required fix: Split into separately labeled results with per-clause status and locate or reprove the unlocatable clause.

- **Uniform cited standing for four cardinal clauses — present.** inherited-00648-00744:32–47 retains one theorem with four clauses, all cited; syntax-counting is separately labelled and locally proved at49–85. Proof standing: `mixed`.
- **Exact per-clause source locator and separate labels — partial.** same:87–96 cites Jech Theorem3.5 and Chapter5 union bound, but does not split the four clauses into separate labels or display deduction of the strict finite-union bound in clause3. Proof standing: `cited_only`.

Remaining: Per-clause source verification remains; literal split-label requirement is not implemented. It is no longer a mixture of inline-proved/cited clauses under one status.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### R-020 — repair_present

Historical status: `fixed (89cfaa8)`; disposition: `FIX-SOURCE`; historical coordinates: `1282` in `I.relations`. Those coordinates are not the current file lines.

Original required fix: State and prove the path characterization as a labeled lemma or mark its status honestly.

- **Labelled path characterization with both inclusions — present.** inherited-01343-01397:10–45: relation S of finite paths, zero-length reflexivity, concatenation, and induction for S⊆R*. Proof standing: `local_proof`.

Remaining: No exact original repair component remains.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-022 — repair_present

Historical status: `fixed (58ef447)`; disposition: `FIX-SOURCE`; historical coordinates: `2299--2317` in `II.sequent`. Those coordinates are not the current file lines.

Original required fix: Rewrite the soundness argument keeping the two registered notions distinct throughout.

- **One satisfaction/validity reading throughout LK soundness — present.** inherited-02451-02544:48–93 states satisfied by every valuation and proves via countervaluations, structural/Cut and logical clauses. Proof standing: `local_proof`.

Remaining: Exact wording repair present; this is not an independent review of every rule translation.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-024 — repair_present

Historical status: `fixed (58ef447)`; disposition: `FIX-SOURCE`; historical coordinates: `3415--3418` in `III.theories`. Those coordinates are not the current file lines.

Original required fix: State conservativity of definitional extensions as a labeled result with proof or citation.

- **Named definitional conservativity and proof — present.** inherited-03729-03907:108–169 has exact fresh-relation hypotheses, unique expansion, semantic conservativity;171–178 gives derivability corollary. Proof standing: `local_proof`.
- **Downstream uses — present.** same:90–106 and inherited-11914-11960:60–64 explicitly cite thm:definitional-conservativity. Proof standing: `local_proof`.

Remaining: No original definition-before-use/citation component remains.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-025 — repair_present

Historical status: `fixed (58ef447)`; disposition: `FIX-SOURCE`; historical coordinates: `3683--3685` in `III.sequent`. Those coordinates are not the current file lines.

Original required fix: Write the case in full with the eigenvariable condition doing explicit semantic work.

- **Assignment change in ∀R soundness — present.** inherited-04109-04213:64–97 defines s'=s[y↦a], treats y=x and y≠x, invokes substitution and coincidence, and uses eigenvariable freshness in Γ,Δ. Proof standing: `local_proof`.

Remaining: Exact requested eigenvariable calculation is supplied.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-026 — repair_present

Historical status: `fixed (58ef447)`; disposition: `FIX-SOURCE`; historical coordinates: `4199--4215` in `III.compactness`. Those coordinates are not the current file lines.

Original required fix: Restate the equivalent forms unambiguously and remove or repair the redundant converse step.

- **Separate compactness and consequence forms — present.** inherited-04921-04967:4–32 states both once and gives model-form directions then finite-derivation argument for consequence form. Proof standing: `local_proof`.

Remaining: Original redundant/garbled consequence argument is replaced by a direct one.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-027 — repair_present

Historical status: `fixed (58ef447)`; disposition: `FIX-SOURCE`; historical coordinates: `546--548, 4127` in `III.completeness`. Those coordinates are not the current file lines.

Original required fix: Add a countable-language choice-free completeness theorem (or delete the promise) and scope the AC hypothesis accordingly.

- **Countable-language promise discharge — present.** inherited-00533-00602:1–16 gives countability convention; inherited-04713-04920:48–118 supplies choice-free coded enumeration and Henkin construction. Proof standing: `local_proof`.

Remaining: Exact countable completeness construction is present; dependency truth lemma remains a separate inherited proof.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-028 — repair_present

Historical status: `fixed (b3eb76d)`; disposition: `FIX-SOURCE`; historical coordinates: `5456--5472` in `IV.types`. Those coordinates are not the current file lines.

Original required fix: Supply the missing step or downgrade the result's status.

- **Point of type space after compactness — present.** inherited-06510-06629:76–106 proves finite satisfiability and extracts complete q from a model; checks exactly one of ψ,¬ψ and consistency with T. Proof standing: `local_proof`.

Remaining: The missing complete-type/Lindenbaum step is explicitly supplied.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-029 — repair_present

Historical status: `fixed (b3eb76d)`; disposition: `FIX-SOURCE`; historical coordinates: `5573--5585` in `IV.saturation`. Those coordinates are not the current file lines.

Original required fix: Supply the compactness appeal explicitly or downgrade the result's status.

- **Compactness of transported type — present.** inherited-06694-06782:38–63 states expanded theory, proves every finite subset satisfiable by elementarity and a witness, cites FOL compactness and verifies completeness. Proof standing: `local_proof`.
- **Extension conclusion — present.** same:65–75 uses saturation and reduces arbitrary tuples to one fresh-variable formula. Proof standing: `local_proof`.

Remaining: The requested compactness appeal is explicit.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-031 — repair_present

Historical status: `fixed (13c1cea)`; disposition: `FIX-SOURCE`; historical coordinates: `10092` in `IX.sol`. Those coordinates are not the current file lines.

Original required fix: Write the injectivity argument in full.

- **Injectivity induction — present.** inherited-12356-12414:37–48 performs metatheoretic induction on n, excludes zero/successor collisions and uses successor injectivity. Proof standing: `local_proof`.

Remaining: Exact requested induction is supplied.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-032 — confirmed_remaining

Historical status: `open`; disposition: `RESOLVE-BY-MIGRATION`; historical coordinates: `10142` in `IX.sol`. Those coordinates are not the current file lines.

Original required fix: Define \(\mathrm{PA}_2\) (language, axioms, semantics) before first use in the migrated part.

- **Peano axioms before use on active route — partial.** Active inherited-12356-12414:4–21 gives {0,S} axioms;55–58 only mentions +,× recursion axioms.
- **PA_2 as a finite formula in expanded signature — absent_on_active_route.** Active inherited-12415-12536:35–51 uses PA_2→σ without defining PA_2 as conjunction or listing the recursion axioms. Explicit def:p02-pa2 in parts/p02/second-and-higher-order-logic.tex:92–118 is inactive; p02.tex:47–60 routes restoration plus the separate supplement.

Remaining: Define expanded-signature PA_2 and its finite conjunction before the active reduction. Do not credit the unrouted historical definition.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### R-033 — repair_present

Historical status: `fixed (13c1cea)`; disposition: `FIX-SOURCE`; historical coordinates: `10162--10168` in `IX.sol`. Those coordinates are not the current file lines.

Original required fix: State the second-order categoricity of the reals as a labeled result with status and citation, and cite it in the justification.

- **Statused labelled reals theorem — present.** inherited-12415-12536:59–91 states full ordered-field completeness axiom/categoricity, cited status, Shapiro and Jech sources. Proof standing: `cited_only`.
- **Downward LS use — present.** same:93–102 cites the theorem twice to exclude countable full models.

Remaining: Original missing cited interface is supplied; source categoricity proof is not reproduced, as permitted by the repair.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-034 — repair_present

Historical status: `fixed (13c1cea)`; disposition: `FIX-SOURCE`; historical coordinates: `8389--8394` in `VII.ordinals`. Those coordinates are not the current file lines.

Original required fix: Replace with the standard argument via \(\alpha\cap\beta\).

- **Intersection-based ordinal comparison — present.** inherited-10353-10451:28–52 uses α∩β, least missing member for a proper subordinal and irreflexivity contradiction; omissions explicitly remain a sketch. Proof standing: `source_sketch`.

Remaining: Original required correct proof outline is present; the two membership calculations are still cited.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-035 — repair_present

Historical status: `fixed (563da95)`; disposition: `FIX-SOURCE`; historical coordinates: `6340--6349` in `V.computability`. Those coordinates are not the current file lines.

Original required fix: Restate the definition as a single well-formed biconditional.

- **Single well-formed definiendum/definiens biconditional — present.** 07506:125–134 has exactly one iff, followed by the defined-output and undefined/infinite-run conditions; output convention is explicit at115–123.

Remaining: No remaining component of this one-definition syntax repair.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-036 — repair_present

Historical status: `fixed (b3eb76d)`; disposition: `FIX-SOURCE`; historical coordinates: `5690--5703` in `IV.ultraproducts`. Those coordinates are not the current file lines.

Original required fix: Promote to a labeled result and carry out the chain/Zorn argument or cite it.

- **Named nonprincipal-ultrafilter existence and construction — present.** inherited-06855-06941:24–86: labelled status; cofinite-filter conditions, cited assumed Ultrafilter Lemma extension, nonprincipality, finite-member induction for converse. Proof standing: `local_proof`.

Remaining: Original permits citation of extension principle; the rest is now explicitly proved.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-037 — repair_present

Historical status: `fixed (13c1cea)`; disposition: `FIX-SOURCE`; historical coordinates: `11273` in `X.manyvalued`. Those coordinates are not the current file lines.

Original required fix: Define saturation for the tableau system and either perform the induction or downgrade the result to sketch status.

- **Saturation before use — present.** inherited-13614-13640:21–26 defines a witnessing truth-table tuple for every labelled compound.
- **Actual truth induction and both specifications — present.** inherited-13641-13699:8–57 gives expansion termination argument, compatible-valuation induction, and base/compound truth induction on an open saturated branch. Proof standing: `local_proof`.

Remaining: The required induction is written. This inventory does not independently accept the termination measure for all possible matrix signatures.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-038 — repair_present

Historical status: `open`; disposition: `RESOLVE-BY-MIGRATION`; historical coordinates: `11911` in `XI.automation`. Those coordinates are not the current file lines.

Original required fix: Supply the two-part correctness argument or downgrade to sketch status under the migration's compile-enforced status scheme.

- **Inherited two-part correctness argument — present.** inherited-14271-14350:64–78 has residual invariant, SAT totalization, branching equivalence and induction on unassigned variables. Proof standing: `local_proof`.
- **Separate exact editorial theorem — present.** parts/p12/sat-and-certificates:21–70 and annex counterpart:3–38 supply residual-state definition, empty cases, unit invariance, termination and both return specifications. Proof standing: `local_proof`.

Remaining: Exact original two-specification repair is supplied in both active presentations; no solver implementation acceptance is implied.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-039 — repair_present

Historical status: `open`; disposition: `CARRY`; historical coordinates: `11179--11191` in `X.epistemic`. Those coordinates are not the current file lines.

Original required fix: Supply the \(C_G\) axiomatization (mix and induction rules) with the standard caveat as new-tree content, or rescope the exercise.

- **Displayed common-knowledge proof system — present.** registry/calculi/hilbert-common-knowledge:1–6: C-Dist, C-Fix and theorem-only C-Ind for nonempty finite groups.
- **Completeness caveat and exercise use — present.** parts/p08/temporal-epistemic-supplement:546–588 states weak completeness/noncompactness and two-agent hypothesis, plus three-world E_Gp/not C_Gp example. Proof standing: `cited_only`.

Remaining: Original requirement is present; weak completeness and decidability remain cited claims.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-041 — repair_present

Historical status: `fixed (13c1cea)`; disposition: `FIX-SOURCE`; historical coordinates: `10735` in `X.intuitionistic`. Those coordinates are not the current file lines.

Original required fix: Disambiguate the defining condition.

- **Unambiguous prime-theory condition — present.** inherited-13058-13099:23–31 states T⊢IPL A∨B and equivalent membership via deductive closure, expressly excludes empty-premise reading. Proof standing: `source_sketch`.

Remaining: Exact definition repair supplied; ambient completeness proof remains sketch.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### R-042 — repair_present

Historical status: `open`; disposition: `CARRY`; historical coordinates: `13049 vs 9513` in `back.rulesheets`. Those coordinates are not the current file lines.

Original required fix: Name the calculi apart under the canonical-LK ruling (LK versus LK-with-equality), scope the cut-elimination claim to the calculus it covers, and state the cut-dependence of the symmetry derivation.

- **Distinct exact LK inventories — present.** registry/calculi/lk:1–30, lk-defneg:1–23, lk-eq:1–31 distinguish negation, identity, implication-left, equality and Mix.
- **Equality scope and cut-elimination boundary — present.** lk-eq header/rule31 notes symmetric replacement uses Cut; parts/p07/calculi-and-derivability-supplement:215–229 excludes equality from the new completeness theorem and does not infer cut elimination. The active structural comparison at body:49–61 explicitly confines the inherited cut sketch to LK_d/LJ and excludes canonical LK and equality. Proof standing: `mixed`.

Remaining: Original named-calculus/scope repair present; general equality cut elimination is neither supplied nor claimed here.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

### Standards

#### S-001 — policy_conflict

Historical status: `open`; disposition: `RESOLVE-BY-MIGRATION`; historical coordinates: `313--319 vs 5007` in `I--III.status`. Those coordinates are not the current file lines.

Original required fix: Extend the status convention book-wide and label every Part I--III result, via the new tree's compile-enforced status keys.

- **One editorial status grammar and enforcement implementation — present.** frontmatter:61–81 defines proved/sketched/cited; handbook.sty:291–334 validates forms/targets and:389–422 parses all hb theorem classes.
- **Literal coverage of every inherited result — policy_conflict.** frontmatter:61–63 says tags do not recategorize inherited presentations; CONVENTIONS status grammar permits source proof forms. Old 100% compile-key requirement is broader than current authorized scope.
- **Current compiled coverage record — output_evidence_unknown.** No current status harvest/check was run. Existing apparatus inventory A-190 identifies the same source/editorial boundary; title or hook presence is not proof-status coverage.
- **Concrete Parts I–III surviving different forms — present.** inherited-00648-00744:46 has prose cited status; inherited-02451-02544:48–93 has an ordinary theorem/proof rather than hb status key; both active.

Remaining: Reconcile literal all-result compile-key acceptance with retained source presentations. Obtain scoped coverage evidence for the resulting policy; do not relabel every proof from a heading.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### S-002 — policy_conflict

Historical status: `open`; disposition: `CARRY`; historical coordinates: `550, 3028, 4317, 4386` in `I--III.notation`. Those coordinates are not the current file lines.

Original required fix: Ratify and enforce the ruling: \(|\cdot|\) is cardinality only and domains are written \(\mathrm{dom}\,M\).

- **Editorial domain/cardinality convention — present.** parts/p01/symbol-registry:15–20 and registry/symbols.csv:23,41 reserve bars for cardinality and dom for domains.
- **Actual inherited domain notation — present.** inherited-03429-03518:7–19 explicitly defines |M| as domain;04968-05042:7–26 uses it in substructure/elementarity definitions. These are active, correctly typed source conventions.
- **Scope honesty in registry — partial.** CONVENTIONS and frontmatter:100–105 allow source-local notation, yet symbol-registry:15–20 and symbols.csv:23,41 still say never/domains cardinality only without inherited-domain exception.

Remaining: Preserve source domain notation; reconcile absolute registry wording with its actual declared source scope. Original universal replacement is a policy conflict.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### S-003 — policy_conflict

Historical status: `open`; disposition: `CARRY`; historical coordinates: `1468, 1770, 3256, 4371` in `I--IV.notation`. Those coordinates are not the current file lines.

Original required fix: Ratify and enforce the ruling: \(\equiv\) is elementary equivalence only, formula equivalence is \(\Leftrightarrow\), and the definitional sign is \(:\equiv\).

- **Editorial three-symbol convention — present.** symbols.csv:30–32,42 separates formula equivalence, definition and elementary equivalence.
- **Actual source equivalence and definition symbols — present.** inherited-01817-01898:56–58 defines φ≡ψ as formula equivalence; handbook.sty:1439–1443 restores source defeq as :=. Source-local MLTT/modal/equational equivalences are also separately registered.
- **Absolute wording versus scoped roles — partial.** parts/p01/symbol-registry:15–20 and symbols.csv:30 have universal reservation wording despite source-scope exception at frontmatter:100–105.

Remaining: Reconcile global reservation prose and source-local roles; do not normalize authentic source notation to close the old row.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### S-005 — repair_partial

Historical status: `open`; disposition: `RESOLVE-BY-MIGRATION`; historical coordinates: `704--724` in `I.sets`. Those coordinates are not the current file lines.

Original required fix: Rehouse as a labeled theorem with status and add the Halpern--L\'evy citation.

- **Original principle label and semantic scope — present.** inherited-00745-00772:1–22 labels def:ultrafilter-lemma and identifies a metatheoretic choice principle; still a definition, not theorem.
- **Halpern–Lévy and choice-strength citation — present.** parts/p06/cardinals-choice-supplement:224–227 and281–300 states relative nonimplication and cites HalpernLevy1971; bib:3389–3400 contains the primary record; P3 boundary:4–30 cites HowardRubin.
- **Requested theorem rehouse at original entry — inactive_only.** parts/p01/mathematical-preliminaries:123–135 supplies the exact labelled statused theorem but is inactive. Active original definition retains uncited strict-weaker assertion at:18.

Remaining: At the active first occurrence, connect the choice-strength assertion to the labelled cited boundary or supply its citation. The requested theorem environment exists only off route; naming a choice principle by definition is not itself a mathematical error.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### S-007 — policy_conflict

Historical status: `open`; disposition: `RESOLVE-BY-MIGRATION`; historical coordinates: `4995--10622` in `IV--IX.status`. Those coordinates are not the current file lines.

Original required fix: Apply the compile-enforced status keys of the new tree to every result in the segment.

- **One editorial status grammar and enforcement implementation — present.** frontmatter:61–81 defines proved/sketched/cited; handbook.sty:291–334 validates forms/targets and:389–422 parses all hb theorem classes.
- **Literal coverage of every inherited result — policy_conflict.** frontmatter:61–63 says tags do not recategorize inherited presentations; CONVENTIONS status grammar permits source proof forms. Old 100% compile-key requirement is broader than current authorized scope.
- **Current compiled coverage record — output_evidence_unknown.** No current status harvest/check was run. Existing apparatus inventory A-190 identifies the same source/editorial boundary; title or hook presence is not proof-status coverage.
- **Concrete surviving source forms — present.** inherited-11240-11279:1 is paragraph Cited theorem; inherited-10353-10451:28 is paragraph Proof sketch; active P6 routes both.

Remaining: Resolve universal key requirement versus source-status retention. P6 sketches are honestly labelled in prose and remain distinct from supplied proofs.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### S-008 — policy_conflict

Historical status: `open`; disposition: `RESOLVE-BY-MIGRATION`; historical coordinates: `5007--7710 vs 7710--10622` in `IV--IX.status`. Those coordinates are not the current file lines.

Original required fix: Adopt exactly one compile-enforced status mechanism book-wide.

- **Editorial key parser — present.** handbook.sty:291–334 and389–422 implements exactly three tokens.
- **Multiple actual source status mechanisms — present.** handbook.sty:488–509 deliberately implements source proofplan; inherited-10353-10451:28 and11240-11279:1 retain paragraph sketch/cited forms; CONVENTIONS preserves source presentations.
- **Original single-mechanism acceptance — superseded_scope.** Literal ban on alternative source status forms conflicts with current compendium preservation; direct correction policy still forbids false status claims.

Remaining: Reconcile the register's universal mechanism requirement without erasing source proof boundaries.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### S-012 — repair_present

Historical status: `open`; disposition: `CARRY`; historical coordinates: `2248--2695, 3440--3780 vs 9135--9948` in `II--VIII.naming`. Those coordinates are not the current file lines.

Original required fix: Ratify the canonical-LK ruling: the Parts II/III presentation is canonical and the Part VIII variant is documented as a named variant with a labeled equivalence theorem.

- **One canonical and separately named variant — present.** registry/calculi/lk and lk-defneg headers give canonical LK and LK_d; CONVENTIONS calculus ruling and P7 body:120–146 identify translation d.
- **Labelled equivalence and honest status — present.** thm:p07-lk-presentation-equivalence points to annex:p7.calculi.2, which lists omitted simulations and explicitly claims a sketch. Proof standing: `source_sketch`.

Remaining: Original requires a labelled equivalence theorem, not full translation proof; current sketch standing is explicit.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### S-014 — policy_conflict

Historical status: `open`; disposition: `RESOLVE-BY-MIGRATION`; historical coordinates: `10622--14780` in `X--XI.status`. Those coordinates are not the current file lines.

Original required fix: Apply the compile-enforced status keys to every result in the segment.

- **One editorial status grammar and enforcement implementation — present.** frontmatter:61–81 defines proved/sketched/cited; handbook.sty:291–334 validates forms/targets and:389–422 parses all hb theorem classes.
- **Literal coverage of every inherited result — policy_conflict.** frontmatter:61–63 says tags do not recategorize inherited presentations; CONVENTIONS status grammar permits source proof forms. Old 100% compile-key requirement is broader than current authorized scope.
- **Current compiled coverage record — output_evidence_unknown.** No current status harvest/check was run. Existing apparatus inventory A-190 identifies the same source/editorial boundary; title or hook presence is not proof-status coverage.
- **Concrete late-book/feedback status forms — present.** inherited-13641-13699:5 has prose complete-proof status; inherited-14271-14350:58–79 has ordinary theorem/proof; feedback uses Solution and Solution sketch headings, not hb theorem keys.

Remaining: Record source feedback and ordinary results separately from editorial status-key coverage; no blanket 100% completion follows.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### S-017 — repair_partial

Historical status: `open`; disposition: `CARRY`; historical coordinates: `10625--11683, 12568, 14354` in `X.citations`. Those coordinates are not the current file lines.

Original required fix: Add the primary sources, cite them at point of use, and enforce the no-zero-citation-chapter check as a standing control.

- **Named primary bibliography entries — present.** bib/handbook:706–755 contains Glivenko1929, Godel1933, Gentzen1936, Kleene1938 and Priest1979. Kleene1938 is On Notation for Ordinal Numbers; it is not evidence for strong-Kleene truth tables.
- **K3 and LP source at use — present.** parts/p08/many-valued-supplement:21–67 gives K3/LP cards with Kleene1952 and Priest1979 sources;:152–181 provides adjacent theorem/weak-Kleene citations.
- **Glivenko/Gödel at actual result — partial.** inherited-13141-13157:14 and13158-13179:21 cite only secondary Troelstra sources. Active comparison table intuitionistic-supplement:193,225 prints texttt cited=Glivenko1929/Godel1933 as plain text, not a rendered bibliographic citation; Gentzen1936 is actually cited at:225.
- **No-zero-citation control and current acceptance — partial.** tools/check.py:1443–1446 has the diagnostic; apparatus A-195 records file-level rather than actual reader-chapter aggregation. No current universal zero-citation result was obtained.

Remaining: Add/use real primary citations at the two active translation results, retain appropriate Kleene1952 rather than treating the unrelated 1938 record as truth-table evidence, and supply actual reader-chapter citation coverage.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### S-018 — policy_conflict

Historical status: `open`; disposition: `CARRY`; historical coordinates: `11628, 12024` in `X--XI.rules`. Those coordinates are not the current file lines.

Original required fix: Name and label every rule and display its side conditions as part of the rule, sourced from the calculus registry.

- **Correct source bang-extension registry rules — present.** registry/calculi/ill-exponential-extension:4–9 displays four named labelled rules and promotion side condition; this is distinguished from full CLL.
- **Resolution side conditions on sheet — present.** registry/calculi/resolution-fol:6–8 includes renaming-apart, selected pivots and mgu for Resolution and Factoring.
- **Literal every source display named/labelled requirement — policy_conflict.** inherited-14035-14051:4–15 retains four bare fractions and promotion side condition in prose; inherited-14435-14479:7–19 retains Resolution Rule plus prose conditions. CONVENTIONS permits exact source displays.

Remaining: Named navigation is supplied. Literal replacement of all inherited displays conflicts with source presentation policy; record a scoped naming/navigation requirement instead.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### S-019 — repair_present

Historical status: `open`; disposition: `RESOLVE-BY-MIGRATION`; historical coordinates: `12117, 12126, 12053` in `XI.status`. Those coordinates are not the current file lines.

Original required fix: Promote each to a labeled, statused, cited statement.

- **SAT NP-completeness labelled/statused/cited — present.** parts/p02/propositional-metatheory-supplement:241–247 thm:p02-sat-np-complete cites modern AroraBarak formulation and Cook primary; active P12 SAT text:99–105 refers to it. Proof standing: `cited_only`.
- **FOL validity c.e. and undecidable — present.** inherited-08248-08305:9–34 gives cited undecidability and local enumeration proof; parts/p04.tex:48–50 supplies corollary label thm:fol-validity-enumerable; P12 first-order-automation:257–264 cites both boundary and Church/Turing. Proof standing: `mixed`.
- **Resolution completeness — present.** inherited-05568-05923:329–348 has labelled thm:fol-resolution, explicit Proof sketch and Robinson/Bachmair citations; P12 source:36–44 and editorial:40–47 refer to it, excluding equality. Proof standing: `source_sketch`.

Remaining: The three named/statused interfaces are present. Resolution's proof stays a source sketch; the row does not require replacing that status with a complete proof.

Exact original repair acceptance verified: `true`. Independent theorem/publication acceptance is not implied.

#### S-020 — partial_with_output_unknown

Historical status: `open`; disposition: `CARRY`; historical coordinates: `10628, 11566` in `X.notation`. Those coordinates are not the current file lines.

Original required fix: Apply the glyph-role rulings and the symbol-registry lint of the new tree.

- **Locally typed roles recorded — present.** symbols.csv:16,24,106–120 distinguishes strings, valuations, worlds, matrix V,D and pomonoid A; row119 explicitly overrides default formula A for the algebra tuple.
- **Actual typed carrier example — present.** inherited-14016-14034:1–18 sets A=Z and then a,b elements, v a valuation; source variables are typed rather than renamed.
- **Registry and use-site acceptance — output_evidence_unknown.** Current policy permits source-local overlapping glyphs with declarations. Apparatus A-193 finds registry-only checking insufficient for every body occurrence; no current zero-collision lint result is claimed.

Remaining: Verify actual use-site type/scope coverage and reconcile requested zero-collision metric with explicit local source overrides; registry row presence alone cannot close it.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### S-021 — policy_conflict

Historical status: `open`; disposition: `CARRY`; historical coordinates: `10677 vs 14071` in `X.notation`. Those coordinates are not the current file lines.

Original required fix: Ratify one registered forcing macro and use it everywhere.

- **Registered forcing macro — present.** handbook.sty:200–201 defines forces/nforces; symbols.csv:90 records Kripke forcing; editorial intuitionistic-supplement:65–101 uses them.
- **Body and feedback original readings — present.** inherited-13100-13127:7–10 uses forces/not forces, while feedback inherited-15638-16742:860–874 uses entails/notentails for the same Kripke semantics.
- **Global normalization — policy_conflict.** Source-specific display preservation controls. The actual two notations are not different semantics, and no direct mathematical error is established by the macro difference.

Remaining: Record both source notations and their common semantic type; original exact-one-macro requirement conflicts with source preservation.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### S-023 — policy_conflict

Historical status: `open`; disposition: `RESOLVE-BY-MIGRATION`; historical coordinates: `8784, 8858, 8907` in `VII.style`. Those coordinates are not the current file lines.

Original required fix: Apply the new tree's uniform definition/entry template to every definition during migration.

- **Editorial definition/entry template — present.** CONVENTIONS environment section; handbook.sty:407–448 has labelled hbdefinition plus source-specific definition wrapper.
- **Source siblings remain full independent definitions — present.** The active set/model-theory source definitions read here (Ultrafilter Lemma, homogeneity, type space, matrix saturation) retain their exact distinct structures and prose rather than all being rewritten to five bullets.
- **Uniform template for every migrated definition — policy_conflict.** CONVENTIONS:14–19 and contract:28–55 preserve definition content and variants; current correction policy overrides only for actual errors.

Remaining: Reconcile literal reformat-every-definition requirement with source retention. Evaluate definition completeness by its actual hypotheses and type clauses.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### S-024 — policy_conflict

Historical status: `open`; disposition: `OBSOLETE`; historical coordinates: `1--4995` in `I--III.exercises`. Those coordinates are not the current file lines.

Original required fix: None: exercises are retired from print to verification assets by the format decision, so per-chapter exercise coverage is moot.

- **Original retirement disposition — superseded.** Original OBSOLETE/no-deliverable acceptance depends on retiring exercises; contract:30–44,62–69 expressly includes exercises/feedback and prohibits retirement.
- **Current exercise route — present.** P12 driver:17,39–43 routes source exercises, qualifying problems and feedback; current feedback inventory records112 exercise targets and5 problem targets with no unresolved target.
- **Per-chapter new exercise quota — not_required_by_retention.** Preserving every supplied source exercise does not itself require newly inventing exercises in the two formerly empty chapters.

Remaining: Keep this as superseded retirement policy. Source-exercise preservation is required; the old absence-in-two-chapters finding does not by itself impose a new quota.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### S-025 — policy_conflict

Historical status: `open`; disposition: `OBSOLETE`; historical coordinates: `13072--13220` in `back.qualifying`. Those coordinates are not the current file lines.

Original required fix: None: qualifying problems are retired from print to verification assets by the format decision.

- **Current selected-solution chapter — present.** inherited-15489-15619:1–35 begins Qualifying-Examination Problems and Selected Solutions with a supplied first solution; parent full feedback inventory records five named problem backlinks.
- **Five additional problems — present_without_supplied_answers.** inherited-15620-15637:1–18 lists Los existential, countable Henkin, full PA2 categoricity, paraconsistent matrix, and proof-assistant exercise; no solutions occur in that fragment.
- **Retirement disposition — superseded.** P12.tex:39–43 keeps both fragments active; contract:30–44 retains source problems and feedback.

Remaining: The source itself offers selected solutions; preserve and describe that boundary. If publication requires answers to all ten, that is an explicit additional writing requirement, not satisfied by old retirement or inferred from the source contract.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

### Production

#### L-003 — policy_and_output_boundary

Historical status: `open`; disposition: `OBSOLETE`; historical coordinates: `preamble` in `global.macros`. Those coordinates are not the current file lines.

Original required fix: Drop them from the new preamble and add a defined-but-unused macro lint.

- **Named obsolete macro spellings — present_repair.** Targeted read-only search of handbook.sty finds no declarations/uses of BV,Theory,eqdef,HOL,coNP,CNF,DNF,bracket,paren,id; no whole-tree zero-use verdict inferred.
- **proofplan is live source syntax — policy_conflict.** handbook.sty:488–509 defines guarded proofplan; active inherited-07150-07294:118–135 actually uses it. Deleting it would remove live source support.
- **Defined-but-unused macro lint/zero result — not_located.** tools/check.py:1–45 has no such diagnostic; bounded tools search found none. No output evidence establishes zero defined-but-unused macros.

Remaining: Reconcile deletion of live source syntax; define any desired scoped unused-macro check and obtain actual output evidence. Do not remove symbols simply because an older snapshot called them unused.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### L-006 — policy_conflict

Historical status: `open`; disposition: `CARRY`; historical coordinates: `2082--2104, 3537--3561 vs 12823--13071` in `II--III.rules`. Those coordinates are not the current file lines.

Original required fix: Introduce the single calculus registry that body, entry cards, and rule sheets all input, making divergence impossible.

- **Central navigation registry — present.** parts/p14/rule-sheets:4–20 inputs ND, LK and first-order sheets from registry; exact sheets have stable rule labels.
- **Literal every-display-origin acceptance — policy_conflict.** Same header:4–8 explicitly keeps inherited source displays. Actual inherited-14035-14051 fractions and14435-14479 Rule display are local, not registry inputs; CONVENTIONS authorizes them.
- **Divergence impossibility/current audit — unverified.** Independent presentations may have different rule conventions. A central sheet cannot make all source variants identical; no current whole-tree identity check is claimed.

Remaining: Use source identity and matched-sheet cross-references to check drift. Universal removal of duplicate source displays is not the current authorized repair.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### L-007 — confirmed_remaining

Historical status: `open`; disposition: `RESOLVE-BY-MIGRATION`; historical coordinates: `363, 11684` in `global.structure`. Those coordinates are not the current file lines.

Original required fix: Label every sectioning unit in the new tree.

- **Editorial heading labels — partial.** P12 driver has part:p12, but active parts/p12/sat-and-certificates:19,85 and p14/rule-sheets:10,24,30 have section commands without labels.
- **Original source part headings — present_without_literal_labels.** inherited-00363-00372:1 and14095-14146:1 retain unlabeled source part commands; style reader-layout interception must be distinguished from source labels.
- **Zero unlabeled sectioning acceptance — absent.** Actual current examples falsify the literal all-sectioning-units label requirement. No source-content change is needed to add suitable navigation where authorized.

Remaining: Supply or reconcile navigation labels for the intended sectioning scope, including source heading wrappers; do not count a nearby chapter label as its part label.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### L-009 — source_present_output_unverified

Historical status: `open`; disposition: `RESOLVE-BY-MIGRATION`; historical coordinates: `global` in `global.numbering`. Those coordinates are not the current file lines.

Original required fix: Decide and document the numbering scheme in the new tree's spec, deliberately.

- **Deliberate numbering decision — present.** CONVENTIONS environment section states per-chapter shared theorem-class counter; handbook.sty:375–384 defines hbitem reset by chapter and chapter.arabic formatting.
- **Source theorem-class consistency — present.** handbook.sty:450–478 makes source method/exercise/example/convention/theorem/lemma/corollary/warning share hbitem.
- **Produced document consistency — output_evidence_unknown.** No current compilation or output inspection was authorized. Source counter definitions do not establish current emitted numbering across all reader-layout hooks.

Remaining: Source decision is explicit. Current produced-numbering evidence remains a publication check.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### L-010 — repair_partial

Historical status: `open`; disposition: `CARRY`; historical coordinates: `1--14780` in `global.figures`. Those coordinates are not the current file lines.

Original required fix: Execute the apparatus program's figure quota (roughly 30--40 figures) per part during migration.

- **Figures exist substantively — present.** Current intuitionistic-supplement:65–101 gives two explicit Kripke models; temporal-epistemic-supplement:329–353 gives a branching tree; source shapes and captions read.
- **Exact forty-figure apparatus program — partial.** Identical-hash apparatus inventory covers40 figure IDs:36 complete surfaces, A-146 partial, A-114/A-119 inactive only and A-150 absent. The original row's phrase per-part quota must be read against these40 named requirements, not as40 newly required figures per part.
- **Known concrete outstanding figures — partial.** Active Stone body:152–161 is a finite example in prose, not the required algebra/space picture; A-146's root p-value is unstated while AFp=false is asserted. Syntax-tree/Post diagram are inactive-only per hash-checked prior reading.
- **Rendered quality/quota admission — output_evidence_unknown.** No render, per-part visual acceptance or current formal apparatus closure is claimed.

Remaining: Supply A-114, A-119 and A-150 on active routes and qualify/fix A-146's root valuation. Retain exact forty-row program and obtain current output evidence.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### L-014 — policy_conflict

Historical status: `open`; disposition: `RESOLVE-BY-MIGRATION`; historical coordinates: `8970, 9839, 10224, 10493 and 8 uses in X--XI` in `VII--XI.structure`. Those coordinates are not the current file lines.

Original required fix: Replace with numbered environments (statused results, a numbered proofboundary environment) in the new tree.

- **Numbered editorial result and proofboundary surfaces — present.** handbook.sty:420–428 provides all requested labelled environments.
- **Actual retained semantic paragraphs — present.** inherited-11240-11279:1 introduces cited relative consistency at paragraph level;10353-10451:28 and85 are proof-sketch paragraphs; handbook.sty:488–509 retains proofplan.
- **Literal no status paragraph acceptance — policy_conflict.** Current source-presentation policy explicitly retains proof boundaries; it does not authorize converting every source paragraph into a newly classified result.

Remaining: Reconcile universal paragraph ban with source-bound status presentations. Any missing navigation can be supplied without suppressing or upgrading the source argument.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### L-016 — policy_conflict

Historical status: `open`; disposition: `RESOLVE-BY-MIGRATION`; historical coordinates: `10682+` in `X.macros`. Those coordinates are not the current file lines.

Original required fix: Register a negated-forcing macro and use it at every occurrence.

- **Dedicated registered negation exists and is used — present.** handbook.sty:201 defines nforces; symbols.csv:90 names partner; intuitionistic-supplement:65–101 uses it in both figures.
- **Every source occurrence normalized — policy_conflict.** inherited-13100-13127:7,10 still uses not forces and feedback:863–874 uses notentails. These declared source renderings remain under current policy.

Remaining: Original missing-macro component is repaired. Literal universal normalization conflicts with source preservation; output glyph quality remains uninspected.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

#### L-018 — repair_partial

Historical status: `open`; disposition: `OBSOLETE`; historical coordinates: `12678--12774 and other longtables` in `back.tables`. Those coordinates are not the current file lines.

Original required fix: Regenerate register tables from the CSV registers with proper longtable head and foot in the new apparatus.

- **Audit-table continuation apparatus — present.** generated/audit-p10:3–14 has caption, endfirsthead/endhead and continued endfoot/endlastfoot.
- **Generated master symbol table — partial.** generated/symbols-tables:1–15 has repeated heads and continuation foot, but begins a longtable without a caption; active P1 symbol-registry:31 inputs it.
- **Other active longtables — partial.** parts/p01/symbol-registry:41–79 supplies caption/head but no endfoot/endlastfoot; scope of actually multi-page tables cannot be inferred from source length alone.
- **Rendered multi-page acceptance — output_evidence_unknown.** No render inspected; no claim that each longtable actually spans multiple pages. Broad acceptance is not established by one corrected generated table.

Remaining: Complete intended caption/continuation surfaces where applicable, and later verify actual page breaks. Historical OBSOLETE disposition does not certify current table apparatus.

Exact original repair acceptance verified: `false`. Independent theorem/publication acceptance is not implied.

## Current reading identities and ranges

The following table records actual current LaTeX/policy/support intervals read for this inventory. Disjoint intervals remain disjoint; neither the first/last interval nor a file heading is treated as a full-file reading. SHA-256 identities were rechecked at finalization for all 105 distinct catalogued files, with 0 changes found. Reused figure and feedback records are separately preserved in the JSON, including their prior/current hash comparisons.

| File | Read intervals | SHA-256 |
| --- | --- | --- |
| `handbook/restoration/inherited-08710-08876.tex` | 1–167 | `2B00900E80D8D0A97CD6779A632E8821F2A51937164F72238CFEF179FE18934C` |
| `handbook/restoration/inherited-09112-09149.tex` | 1–38 | `23A060D7646D1BBB54480F35833F2D40A78180E67A36232CF8406D7E71B3FBAE` |
| `handbook/restoration/inherited-09150-09174.tex` | 1–25 | `7C36BE695AAF1AA32F9DFA45AF894C9C5413F02254B1BA3C9142B1C878156DDD` |
| `handbook/restoration/inherited-07851-08048.tex` | 1–198 | `436DE76199BCD67D4E55252CA92D47A3046701AC028E79484395E5C0EDE6B7B8` |
| `handbook/restoration/inherited-08898-09079.tex` | 1–182 | `38CD059067E33532A1A1B1880723EFC25C19EC12949D9D6B4112A228E0314571` |
| `handbook/restoration/inherited-08439-08709.tex` | 1–271 | `95EB4270559303FEFC5DE2D9BC804A04768EAD87D68D9E5D9CBF65079714806A` |
| `handbook/restoration/inherited-09328-09438.tex` | 1–111 | `F5A14F098311611F5942A7E0F9F5B348B52C1AADFCA2E1FF129E5F63A977F6A0` |
| `handbook/restoration/inherited-09620-09728.tex` | 1–109 | `2AE8F97648CD8D8398DE5A7F705D41910FC70DDE46903E871B294D9A31F4A57E` |
| `handbook/restoration/inherited-08306-08438.tex` | 1–133 | `0B020970BE72999CD771566BA0D6CDB4E4668728362CBD3C0D1606059EE9D2B8` |
| `handbook/restoration/inherited-08049-08080.tex` | 1–32 | `F4337E1CEE23A1EC8B14EA6E35A1BB8F4A794F73A116DAE735A22402471C73F8` |
| `handbook/restoration/inherited-08081-08143.tex` | 1–63 | `169C09020DA06F080A6C513E43BBBCFC3CF142AE893352D5130BD101DC1ED2C0` |
| `handbook/restoration/inherited-08144-08186.tex` | 1–43 | `1C29645502F72D173412DE6F0EACAD187DD25DFA0F93421E8C46EC87AC53FABF` |
| `handbook/restoration/inherited-08187-08238.tex` | 1–52 | `BC9E76B3DCBC7D47BEC44BE1B05F5AFB98254BABBE6A629BE79E5EB0CA4B9654` |
| `handbook/restoration/inherited-07506-07677.tex` | 115–150 | `EB27FE6DE9A8FFBBE3EC6F317DFF66D97DDE72F22B1FA3FCB48A4304D85F3C7D` |
| `handbook/restoration/inherited-09262-09327.tex` | 1–66 | `75A27E87080116A235A904DAEDABE2A70DFF472BA27CA8A454C448DFD4B58BB6` |
| `handbook/restoration/inherited-05132-05567.tex` | 1–436 | `DC57C114D652DB41E6E82B834285EE9249B36677462ACB570D09F760BAAFC0EE` |
| `handbook/restoration/inherited-04306-04575.tex` | 1–270 | `3AF221BE1A62243FD0CB2896F63B419476CE8A5BFC5BDB49DF06D1EF00D782D3` |
| `handbook/restoration/inherited-04713-04920.tex` | 1–208 | `1B6D33C14AEF530364EE62B342DB74BE130011F775A3A9D5958F3CCA5B9808DA` |
| `handbook/restoration/inherited-02451-02544.tex` | 1–94 | `F089CA64168064D555E6F2CF32E99594E06B29788E9B63A4AFA47B343D6CBA32` |
| `handbook/restoration/inherited-04109-04213.tex` | 1–105 | `0D45236D978CD3B75F7E536FE45D9516ED0D735AB6DC8745137B8685959075F1` |
| `handbook/restoration/inherited-04921-04967.tex` | 1–47 | `79E3E081D7496C13F92517B899CC9518FC6E63A97ADFE1715B85F04C3D23ABAD` |
| `handbook/restoration/inherited-01946-02186.tex` | 1–241 | `9A98BDF593C6331925A87701F3410F1D27312E73B3C32587BE7CF5A2E839C09E` |
| `handbook/restoration/inherited-03729-03907.tex` | 1–179 | `4575656D845980E653CC7F686BCDB35BC32B75CE5E3BF85C5E1A570FEDB63901` |
| `handbook/restoration/inherited-11711-11740.tex` | 1–30 | `4C6F8BE640199F18188CEAAC918574A1A2A23973A5E4CD7193B207E53E1F471E` |
| `handbook/restoration/inherited-11741-11767.tex` | 1–27 | `836BEE04978EB0CD02DA2F92D22CEF015400C4342271008BAAC067591D572CD0` |
| `handbook/restoration/inherited-11768-11823.tex` | 1–56 | `A248A9312DF24072B30435AB996E241415C725D40EDADD15905FD317EB3392CF` |
| `handbook/restoration/inherited-11824-11881.tex` | 1–58 | `05CD142307A51B542A1A11F102FC76DE4F1CF8E6843DF2FE7C1AFC42CB13E397` |
| `handbook/restoration/inherited-11914-11960.tex` | 1–65 | `2D8EB98F583C9DEB327252DF70B2DBBFD36F949D6237E1817873FDF9AEAC4302` |
| `handbook/restoration/inherited-11294-11314.tex` | 1–21 | `ADAD59C5271009E166740100ECBBEC99EEBA0F580B0C4088DC9EE2BD74F630F2` |
| `handbook/restoration/inherited-07150-07294.tex` | 1–145 | `CCB19227218A479328D04079082C149BBD9ACF4B587C45D13FFF49A07548EFF8` |
| `handbook/restoration/inherited-07295-07468.tex` | 1–174 | `AC14D5D63A54E8D7174783E28A228FAC224A72352E15F0CE253D89EAFC1C0672` |
| `handbook/restoration/inherited-00648-00744.tex` | 1–97 | `B8EF1F4FA7B8EE8E8D8EE98FDB73937CE0C6CA470E8EE0DD0BBE69BD5D51124D` |
| `handbook/restoration/inherited-01343-01397.tex` | 1–55 | `738D2BD4619504D02B2D64682E3F1E62B589BF7F8D6FC11D3EAA11055208A15A` |
| `handbook/restoration/inherited-06510-06629.tex` | 1–120 | `26C22AE57393275233EFE665248325AD5374B798C619E018AD623ADA1523F3AC` |
| `handbook/restoration/inherited-06694-06782.tex` | 1–89 | `1512CDC55968277F4496ED596857339EFA6E68A9564D3C41F4325086A6299B16` |
| `handbook/restoration/inherited-11200-11239.tex` | 1–40 | `C4826978F5F0599C4480E1B00354CC936A8F360E6F7937D92EE844882F128B80` |
| `handbook/restoration/inherited-11240-11279.tex` | 1–40 | `3F29F171700D5B9849BBF6AC587B17B99E879BD4CE8670B617A6A9293DB9F772` |
| `handbook/restoration/inherited-11280-11293.tex` | 1–14 | `B277C6A92CF5B5E501A86B1108B111CE1C4125D002E962AC1EE29E4AD872C0E9` |
| `handbook/restoration/inherited-12356-12414.tex` | 1–59 | `3B850FF37842E3E024AC32B23712AA199DB010AD2249E764BB590AFC2ED89A04` |
| `handbook/restoration/inherited-12415-12536.tex` | 1–122 | `D4FF50A3145ACAC19B3E7A6054BCF0AEF4AAC1EB2E774F825ADE02AF2693F667` |
| `handbook/restoration/inherited-10353-10451.tex` | 1–99 | `6B0A7785FADE6927950AD97D90EC2B24FC90A335B7673AC0A3B75F6E6C791008` |
| `handbook/restoration/inherited-06855-06941.tex` | 1–87 | `E1931E83963E91154274DF5AF6B0B79583CD7F8941AAF30B791B52C1BBC7C2E7` |
| `handbook/restoration/inherited-13614-13640.tex` | 1–27 | `DD7DA399873F2C8C708B92E2451A968B23AC6B53ADE4DE10733A04B9146C88B0` |
| `handbook/restoration/inherited-13641-13699.tex` | 1–59 | `2B5F00B3046CFEB9F338E365CB014B00CEA6AA096A802094D544F144B1B03E38` |
| `handbook/restoration/inherited-13058-13099.tex` | 1–42 | `F6DDFF1AA7B4462C2E3D495DCCCB3C077EF63AAE49F2247614295E343C554AFA` |
| `handbook/restoration/inherited-14271-14350.tex` | 1–80 | `195678D34FE2972A355608AA5BE4DDE1811275876EB5E1DE52F977F8B5D56A32` |
| `handbook/registry/calculi/lk.tex` | 1–30 | `09B0B81140BFB93431D88BA78B7DE1CD6579987EFBB38770EAECDBE8EED7D406` |
| `handbook/registry/calculi/lk-defneg.tex` | 1–23 | `EABDAA9FC4BAFB3E65CABA406E65E25DAF1FAF9EA916FF42039E2C0BA445267B` |
| `handbook/registry/calculi/lk-eq.tex` | 1–31 | `68CAACAF82D2A505C2546F8F5A6AAE204164C38D03A7A4EF67E215C3D36CA1D0` |
| `handbook/annex/p07/calculi-and-cut-elimination-supplement.tex` | 1–217 | `C9E42C111B0D8955EF8FFCE3FACABA702C7E44E8F5B04539BA0165E19D751298` |
| `handbook/registry/calculi/hilbert-common-knowledge.tex` | 1–6 | `33DE9EB15DACEBA429641111AF63FA732D53DC221D6D7F31268281DEAB91A492` |
| `handbook/CONVENTIONS.md` | 1–244 | `CBF7E4F47B52A7768841FE9B905C61BC8879FFB6629C2A9BFFDBDF62526A3FBA` |
| `handbook/annex/p12/sat-and-certificates.tex` | 1–38 | `DF6D14E843F2B704BDB2A78B7D3AE4C1F3A778B586800C6D9C57F7111DF2CDB8` |
| `handbook/restoration/inherited-00533-00602.tex` | 1–35 | `DB7EB38EC429D86E8CE4D6A7BC6D24E20C7570136B69E8B5C1AC665F8CE2DD61` |
| `handbook/parts/p07/calculi-and-derivability-supplement.tex` | 95–146, 215–229, 1–95 | `F109A14F4B1B068229C0B1069C65AF0B3491EA1D06E3722296145491B7F2A235` |
| `handbook/parts/p02/second-and-higher-order-logic.tex` | 76–136 | `72551E0B9EF0B8051F15A5EFBDE7107B147607F314A1F411641157134CC60CA0` |
| `handbook/parts/p02/second-and-higher-order-logic-supplement.tex` | 1–25 | `9EBF3CC60A7C54DF7312F9065763BDEE69396454F8C595B22E45D9EED132B091` |
| `handbook/parts/p12/sat-and-certificates.tex` | 1–110 | `5ED4AB927A1E6FE8469CB932895D1FC667F3AAD00FC067CCB513C4DA41F4543A` |
| `handbook/parts/p08/temporal-epistemic-supplement.tex` | 475–612, 329–357 | `637FA1588D8E7EF2412142562847733A2CA0C271BD294576BBF0879217C30B70` |
| `handbook/frontmatter.tex` | 41–109 | `61F2B7DC3EF52CC4D6D418AB060E6F65C008812901FD3AED5AA7AC43864226E6` |
| `handbook/handbook.sty` | 190–205, 285–338, 340–515, 1430–1495, 1206–1252 | `BB4D4E18B039B68E6C156BD900EA8AE028815198F90926D1550D3BD1EACC9C0D` |
| `handbook/parts/p08/intuitionistic-supplement.tex` | 1–104, 138–204, 210–235 | `B91A31E23FF7237BB2302767D1EC5EF03ED742BC8ED7A83592D5694FFA8C8018` |
| `handbook/parts/p08/many-valued-supplement.tex` | 1–69, 137–190 | `78CC54DC511982F7D1F95EA565AC9EFE57140B67E5AA7667EBF425371522211A` |
| `handbook/parts/p03/ultrafilter-choice-and-source-boundary.tex` | 1–41 | `DA534D853A0FA1B6AF81B7E002EDCBE78BB398376D9FD5F4FAF06676863F4185` |
| `handbook/restoration/inherited-00745-00772.tex` | 1–28 | `4C9967932C713D8838E7AC3528DCE3B74DB0E95B75D54C1871615D8C4F565DAE` |
| `handbook/registry/calculi/cll-one-sided.tex` | 1–18 | `7859739B9A6C845075A5B54BC96B368A9727F1FF79692798DB6C80FECA4B2904` |
| `handbook/registry/calculi/resolution-fol.tex` | 1–8 | `814B0A9ECDE3C0240CD5ABE00DAB7466E79381F796F3014AECAEDA2983C97DD2` |
| `handbook/registry/calculi/ill-exponential-extension.tex` | 1–9 | `1524C9A9EA3D94FB29031097E3CE87914E03A68E74E17C96B6BB5C8A029F318C` |
| `handbook/bib/handbook.bib` | 706–758, 3389–3400 | `D5BAB1C74AB2B378EAACAFE2CE1B313209E71E46A28DD2748EF7C539C5CB7094` |
| `handbook/registry/symbols.csv` | 1–79, 85–125 | `A4D3C3050FD991A9CC081B22698CF3695B4AD8032DAC03A1BC3B46150233E4D8` |
| `handbook/parts/p10/stone-duality.tex` | 1–30, 148–161 | `CA80E564561DB9950D8FB8931571EDD9C7E5526D41A061CB5BE0C3FC7D7AE1D9` |
| `handbook/restoration/inherited-13100-13127.tex` | 1–28 | `31E3626B5CE5667D8188E690380CB32B9594A37FF20FCC62D4D24E97B2AFFF0A` |
| `handbook/restoration/inherited-13128-13140.tex` | 1–13 | `D217C8C169B7C71BA0D394A821ABCB29373D1BF17EB5CB60FB99D9F2D67A4527` |
| `handbook/restoration/inherited-13700-13730.tex` | 1–31 | `18C1475AC2F1B71946E131B1532725D17CC947C8B46BA705C330A2733DEA1CDE` |
| `handbook/restoration/inherited-13731-13774.tex` | 1–44 | `B3D40A0CE0A387D9970DD48F1DAEECF09CAFE802E82E8856A83278B94BB7B51C` |
| `handbook/restoration/inherited-13141-13157.tex` | 1–17 | `8EC5B7A3034F9C5C922DE57AB09D9EBDF0C0B39205004F929D6E7DF918566CC5` |
| `handbook/restoration/inherited-13158-13179.tex` | 1–22 | `8B22197871AB0D6EE765F05E18E9ABD4552A2BBAB22A60CF9C49C0C0E0DDB70D` |
| `handbook/restoration/inherited-14435-14479.tex` | 1–45 | `8CE6DF2C749ACB6CBCD07114B61CF75A904DB2BF04BAE89A051D36210DFA5A66` |
| `handbook/restoration/inherited-14480-14495.tex` | 1–16 | `365FFF2268CC4FEFAA05C961514EC3C9F06688139396F6564483DFBC7C26811E` |
| `handbook/restoration/inherited-14522-14560.tex` | 1–39 | `A1B62D7FDBB0149A5DA8507EF349717E4C656A33E5D9CF62B5E81B575A908935` |
| `handbook/parts/p02/propositional-metatheory-supplement.tex` | 239–249 | `6378E3C0C975EBD69C747C8B576B7F4ED1AA7577910071B53D1512A441AE0859` |
| `handbook/restoration/inherited-08248-08305.tex` | 1–35 | `88BBBD4E09EA55BD57BD1D30A432E61B8B26BCC7F02C6C6B2D337ED63486000B` |
| `handbook/restoration/inherited-05568-05923.tex` | 323–356 | `B59F2BD9857082E603CCE1B42728031B441E120992E94D378FF4FDB1C1F867B6` |
| `handbook/parts/p04.tex` | 38–56 | `9E1CD4671FA9E1A5D5D951305116D1F728591F689FB66B83C3DC47585F50312D` |
| `handbook/parts/p12/first-order-automation.tex` | 35–57, 250–264 | `D4D8F587F20BC539CF5B8D04DFC71B1043D012E2FA0E464910A7D789C26AF9FA` |
| `handbook/parts/p10/algebraic-and-categorical-logic.tex` | 43–83 | `8C11EC51E2C576190C02722262F8E17BD8EDE2610E89E9888ECAAD35CC5A8278` |
| `handbook/restoration/inherited-15638-16742.tex` | 857–882 | `993A3153C9CA856F761B5650C312E85E2BE78FA23B8AFC8EDCD4E87A7B2983BF` |
| `handbook/restoration/inherited-15620-15637.tex` | 1–18 | `9D788C4DF60544647F1DE42A65AC789E7AB3ED1A3B81FD2DC02974BF89E983E7` |
| `handbook/parts/p06/cardinals-choice-supplement.tex` | 209–231, 277–303 | `39E74E1833A403CE3D29AC638B93F178F6445B5737B6CD8CA05E1D633B4B7DBE` |
| `handbook/parts/p01/mathematical-preliminaries.tex` | 119–136 | `7E2A81F1F0FCD8146E33589E883607EAE78933DDCBE3BBE1CC0A1C3D7E75549E` |
| `handbook/parts/p14/rule-sheets.tex` | 1–40 | `96B452A6377C39BA94629BF949391B80AB8BA212F350000449D7089D7CF61048` |
| `handbook/restoration/inherited-00363-00372.tex` | 1–10 | `3ADD1C0D52F826DC01D85AE0DBC5027AF35AC6735EFE3BD7C954BE3D39133743` |
| `handbook/restoration/inherited-14095-14146.tex` | 1–15 | `CD21918EA535E757D7DEAAC64BD6AAECADBBE839B585DABF5E0E7572893329A1` |
| `handbook/generated/audit-p10.tex` | 1–18 | `8B977FB7D9637319658C330F9C0DA1B0F2F0FDF88D9DCF6E393B3F34E2845D39` |
| `handbook/generated/symbols-tables.tex` | 1–15 | `C6B97C8D431D996110D8881EA6E74DA26278C20C0B5B9460A5948B133A650553` |
| `handbook/parts/p01/symbol-registry.tex` | 1–110 | `9CAD06E4562F46A1094B77FB683EC979183F4094E41BF53ECC5C2D6F9EEE18FB` |
| `spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md` | 1–108 | `EDDD1F580104DE76A112647647DF25C8EA67ED77FE2DB19FDB641B4B1D0D0099` |
| `tools/check.py` | 1–45, 1435–1459 | `84E4E258DD8CC0C05662F3AFAF218DF9F627500DA61902DB266D4C0A81EA3B04` |
| `handbook/restoration/inherited-01817-01898.tex` | 45–64 | `499FEC700936D0625769D7C09AA2BC5FD1F6D976B9EAB1A9CBC8EDFE8CAFB9C4` |
| `handbook/restoration/inherited-03429-03518.tex` | 1–28 | `EF123D37FB24D3D7194768867468E3E739E92C066E855195B0F7F6B040892D0B` |
| `handbook/restoration/inherited-04968-05042.tex` | 1–28 | `4B0D85E405FF1514804860A2C7521B03D4C2743B0F6395B565DD05E9B0755720` |
| `handbook/restoration/inherited-14035-14051.tex` | 1–17 | `827A73E8169AF28E5CF7BDE5B5D9790C044B8993A61AF8BD6CD8D97563762530` |
| `handbook/restoration/inherited-14016-14034.tex` | 1–19 | `83FCD44047F2E90B846C8552D243340BC4C8CD9267425D664CB6FCD301EBD701` |
| `handbook/restoration/inherited-15489-15619.tex` | 1–35 | `175A9850E56757BCDD168D683F1E52A35B9207832204E3BB105F4A57405BEB78` |
| `handbook/parts/p12/automation-and-mechanization.tex` | 1–9 | `763CB233FD420A8DDEAA97FD58387A98CDA8EE576D4707865F0139ECD5303235` |

## Reconciliation and final checkpoint

Assigned rows: 58. Unique IDs: 58. Unexamined rows: 0. Original CSV-field comparison: preserved for every row. All 30 previously refined IDs remain excluded. No next unread requirement ID remains in this bounded task. Whole-theorem correctness, all-source identity, current formal admission, current compilation and current visual publication evidence retain their distinct standing.

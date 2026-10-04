# Round 2 — adversarial-publication deliberation

### F1 — still-open
- current location: handbook/annex/p02.tex:4-12, :27-34; handbook/parts/p02/first-order-calculi-supplement.tex:2-10; handbook/parts/p02/first-order-completeness-remainder.tex:2-7; handbook/parts/p02/first-order-normal-forms-supplement.tex:2-10; handbook/parts/p02/first-order-resolution-supplement.tex:2-8; handbook/annex/p02/first-order-calculi-supplement.tex:2-7; handbook/annex/p02/first-order-completeness-remainder.tex:2-6
- response: The intended admission gate remains visibly and substantively open. The annex still prints OPEN, says the NNF and functional-basis proofs lack exact labelled destinations, says duality is absent, and records an owed reviewed destination/content. It also still says the retained first-order additions are explicitly OPEN and unadmitted. The six routed supplement notices continue to say OPEN/unadmitted or that no publication/admission gate is closed. This is consistent with the ledger's deliberate deferral, but it is not a source-fixed or build-only state.
- disposition boundary: F1 cannot close until the surviving source findings below, the independent admission controls in F2, and the later build/visual gates have been dispositioned. Removing the notices now would inflate the current state.

### F3 — still-open
- current location: handbook/parts/p02/variants.tex:27-40, :106-189; handbook/parts/p02/second-and-higher-order-logic-supplement.tex:47-95, :102-165, :168-234; handbook/annex/p02/higher-order-supplement.tex:63-83, :87-136
- response: The principal repair is real. The live body now defines the matched model class, the exact Comp/Choice families and eligibility conditions, matched consequence, predicate-constant incidence symbols, the pointwise set translation, the tagged structure, and a proved satisfaction/schema-correspondence theorem. Predicate-domain membership is an explicit matched-model condition at second-and-higher-order-logic-supplement.tex:51-53 and an explicit hypothesis of the incidence construction/theorem at :130-165; annex item annex:p2.hol.7 uses that hypothesis at higher-order-supplement.tex:73-82. Two source defects remain.
  1. The repaired many-sorted reduction is now explicitly limited to at-most-countable sort/function/relation data and a fixed injection into the countable first-order variable supply (variants.tex:33-40). The matched adequacy theorem still quantifies over every set of relational second-order formulas without a countable source-signature hypothesis (second-and-higher-order-logic-supplement.tex:221-227), even though its definition invokes that restricted reduction at :168-191. The inherited second-order signature permits the symbols of an arbitrary first-order signature, so the downstream theorem has not imported the new scope.
  2. The soundness direction of annex:p2.hol.8 still says it uses “the exact satisfaction equivalence in Section sec:second-order-logic-05” (higher-order-supplement.tex:93-96). That inherited section contains the older generic Henkin translation, not the new predicate-constant incidence translation. The applicable result is the newly proved Theorem thm:p02-sol-incidence-satisfaction.
- residual correction: Add the exact countability/injection hypothesis to def:p02-sol-incidence-translation, def:p02-sol-derived-calculus, and thm:p02-sol-derived-adequacy (or generalize the many-sorted base coherently). Replace the annex:p2.hol.8 dependency with an explicit reference to thm:p02-sol-incidence-satisfaction. These are source corrections; no build is needed to establish the mismatch.

### F4 — accept-fixed
- current location: handbook/parts/p02.tex:59-60; handbook/parts/p02/variants.tex:27-40, :106-189
- response: The driver now routes variants before the matched-SOL supplement. The many-sorted signature fixes at-most-countable data and an injection of its disjoint variable stocks into the governing countable supply at variants.tex:33-40. Guard translation and Ax_sort are defined at :106-152, VarGuard_MS is then defined at :154-172, and only afterward is the reduction theorem stated at :174-189. The former cycle and arbitrary-sort overclaim are removed at source. F3 separately retains the missing propagation of this restricted scope into the downstream SOL theorem.

### F5 — accept-fixed
- current location: handbook/parts/p02/propositional-metatheory-supplement.tex:12-65
- response: Form(P), its valuation semantics, and the exact finite discharge-labelled CPL(P) derivability relation now occur together at :12-27, before unrestricted compactness at :29-35 and choice-calibrated completeness at :44-54. The proof consistently uses Gamma not-provable-in CPL(P) phi at :56-65. This fixes both the definition order and the previously undefined derivability relation.

### F6 — accept-fixed
- current location: handbook/parts/p02/second-and-higher-order-logic-supplement.tex:21-38; handbook/registry/calculi/sol.tex:17-20
- response: The final live delta fixes, for every arity, an explicit enumeration RelVar_n = {X^n_0,X^n_1,...} and defines “least fresh” by least absent index at :22-25. The recursive substitution then fixes free-atom replacement, object/Boolean traversal, stopping at the substituted binder, same-arity binder renaming, predicate-constant behavior, and arity preservation at :26-38. The four sheet rules use that exact capture-avoiding operation. The prior capture counterexample now has one deterministic output.

### F7 — accept-fixed
- current location: handbook/parts/p02/propositional-metatheory-supplement.tex:104-132; handbook/parts/p02/first-order-resolution-supplement.tex:10-33; handbook/annex/p02.tex:27-34
- response: The two figures remain useful and have distinct semantic labels, fig:p02-resolution-dag and fig:p02-fol-resolution-dag, but neither caption now claims A-121. The routed graph has zero reader-visible A-121 occurrences. The annex's retained-addition paragraph singles out one first-order “resolution figure,” and the first-order candidate remains the canonical labelled object for the later obligation binding; the propositional figure no longer claims the same identity. Thus the reader-level duplicate claim is removed. The formal A-121 reviewed-obligation binding remains part of the intentionally deferred F2 admission work, not a residual duplicate under F7.

### F8 — accept-fixed
- current location: handbook/parts/p02/first-order-depth.tex:6-18; handbook/parts/p02/variants.tex:8-22; handbook/parts/p02/second-and-higher-order-logic-supplement.tex:14-19; handbook/annex/p02/higher-order-supplement.tex:14-19
- response: Each previously comment-only editorial block now carries a rendered reader note. The notes state authored/editorial standing, nonreplacement of exact inherited text, controlling citations or definition sections, and proof-status limits. This fixes the source/editorial boundary. Typography and placement of those notes remain visual-review questions, not source defects.

### F9 — accept-fixed
- current location: handbook/parts/p02/propositional-metatheory-supplement.tex:261-266; handbook/parts/p02/first-order-depth.tex:312-320, :422-431; handbook/parts/p02/variants.tex:328-331, :501-521; handbook/parts/p02/further-reading.tex:1-29
- response: A traversal of the current 119-file reader graph found zero noncomment D-/N- workflow IDs, future Part-2-finalizer promises, “only a Part pointer,” or “row not done” language. The remaining cross-part prose uses public destinations: sec:p08-conditionals-deontic-free, thm:p03-lindstrom, sec:p04-analytical-hierarchy, and tab:p04-analytical-hierarchy. All four target labels exist in the live source. The propositional source paragraph is present-tense, and the new Part II further-reading chapter supplies the grouped public source map. Source navigation is fixed; actual resolved PDF links remain a final-build check.

### F10 — still-open
- current location: handbook/parts/p02/variants.tex:406-426, :468-474
- response: The repair now supplies the missing arity, isomorphism-invariant model parameter, formation clause, satisfaction clause, and family-indexed FOL(Q) definition. One exactness gap remains in the new binder: lines 409-416 put bar x = (x_1,...,x_n) into the simultaneous update s[bar x maps-to bar a] but never require the x_i to be pairwise distinct or define repeated-variable update order. If x_1 = x_2 and a_1 differs from a_2, the displayed update has no unique value, so the satisfaction clause is not eliminable for every syntactically admitted binder.
- residual correction: State that x_1,...,x_n are pairwise distinct in the formation clause, as the nearby Comp/Choice definitions already do, or define an exact repeated-variable convention and restrict the admissible tuples accordingly. No build evidence is needed for this source defect.

### F11 — accept-fixed
- current location: handbook/parts/p02/first-order-depth.tex:158-186, :188-246
- response: The table is now preceded by def:p02-exponential-time-classes. It defines EXPTIME and NEXPTIME as explicit DTIME/NTIME unions, coNEXPTIME by complement, and 2EXPTIME by a double-exponential DTIME union; it also fixes the machine and finite-encoding convention and the standing/use of the names. Every table occurrence follows that definition.

### F12 — accept-fixed
- current location: handbook/registry/calculi/sol.tex:9-16; handbook/parts/p02/second-and-higher-order-logic-supplement.tex:97-100, :197-211
- response: The sheet now names its inherited base in human language and links to sheet:lk-eq at sol.tex:10-11, links the defining derivability at :12-13, and gives reader-facing editorial/source standing with citations at :14-16. The body links to both the SOL and LK-equality sheets and its later projection references the linked SOL sheet rather than exposing raw dependency tokens. Source reciprocity is fixed. Link resolution and sheet layout still require the final build/visual pass.

### F13 — accept-fixed
- current location: handbook/parts/p02/variants.tex:336-355
- response: The L_omega1omega definition now permits a countable family only when the union of its free-variable sets is finite, assigns that free-variable set to the infinitary connective, constructs quantifiers one variable at a time, and gives the universal/existential satisfaction clauses for countable conjunction and disjunction. The former counterexample family with infinitely many total free variables is no longer admitted.

### F14 — accept-fixed
- current location: handbook/parts/p02.tex:54-56; handbook/parts/p02/simple-type-logical-constants.tex:1-30
- response: The editorial definition is routed immediately after the exact simple-type syntax and before the exact semantic chapter. It declares bottom:o, negation:o-to-o, and all three binary constants at o-to-(o-to-o), states left-associated application and classical Boolean denotations, types P:alpha-to-o in the existential abbreviation, and requires those denotations in the selected Henkin domains. The earlier stray qquad text and under-typed existential are absent. Rendering of the display is still a build/visual check.

### F15 — still-open
- current location: handbook/parts/p02/first-order-completeness-remainder.tex:56-65; handbook/bib/handbook.bib:955-963
- response: The warning now cites the historically appropriate Skolem1923SetTheory key with Hodges1993, so the wrong-work defect is substantively repaired. The newly added bibliography title and booktitle contain malformed TeX accents: handbook.bib:957 prints Begr{"u}ndung and :958 prints Redog{"o}relse, whereas the file's established syntax is Begr{\"u}ndung and analogous {\"o}. Those bytes will not reliably render the intended umlauts and leave the source repair publication-unsafe.
- residual correction: Change the two fields to valid protected TeX accents, Begr{\"u}ndung and Redog{\"o}relse, then retain the current key at the warning. Bibliography rendering remains a later build/visual check after the source bytes are corrected.

### F16 — still-open
- current location: handbook/parts/p02/first-order-calculi-supplement.tex:2-8, :85-89, :164-177; handbook/registry/calculi/hilbert-fol.tex:1-18
- response: The comparison row at :168-175 now gives the requested split attribution, cites Mendelson and Kleene, and states the primitive-existential interderivability bridge used to transfer strong completeness. However, the same reader-routed file still opens by attributing “the Hilbert material” only to Mendelson and Enderton at :6-8, and its prose at :85-87 again sends readers to Mendelson and Enderton for “this calculus” and “its quantifier schemas.” That remains inconsistent with the sheet's component note and the repaired table, both of which say the two primitive-existential schemas come from Kleene.
- residual correction: Add Kleene1952 and a component-qualified attribution to the opening reader notice and the prose at :85-87, or narrow those sentences so they no longer claim authority for the combined schema surface. Keep the exact split row and bridge.

### F17 — accept-fixed
- current location: handbook/parts/p02.tex:59-61; handbook/parts/p02/further-reading.tex:1-29
- response: The live driver now ends Part II with a separately routed Further Reading for Part II chapter. It supplies four source-bearing groups covering propositional logic, first-order syntax/metatheory, full versus Henkin second-order semantics, and the variant logics actually presented. The former future-finalizer promise is gone. The chapter's ToC entry, page break, bibliography rendering, and visual placement remain final-build/visual evidence and are not promoted by this source verdict.

## Round-2 disposition summary

- accept-fixed: F4, F5, F6, F7, F8, F9, F11, F12, F13, F14, F17.
- still-open: F1, F3, F10, F15, F16.
- merge: none.
- needs-evidence: none as a primary disposition. Accepted link, citation, table, figure, ToC, and rule-sheet source repairs still require the later full build and visual audit; F1/F2 keep admission separate.
- verification boundary: This deliberation inspected the current 119-file Part II reader graph and the exact agenda surfaces, including the final relation-substitution enumeration delta. It found 117 input edges, no duplicate routed target, ten reciprocal proved-status/annex-item pairs, and zero noncomment workflow-ID/finalizer remnants. It did not edit manuscript/control/test files, run a book build, resolve a fresh PDF/index, visually inspect pages, modify admission records, or supply human/user acceptance.

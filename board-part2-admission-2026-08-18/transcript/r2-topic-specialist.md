# Round 2 topic-specialist deliberation

### F1 — still-open
- reply: still-open
- current location: `handbook/annex/p02.tex:4-34`; `handbook/parts/p02/first-order-calculi-supplement.tex:2-10`; `handbook/parts/p02/first-order-completeness-remainder.tex:2-7`; `handbook/parts/p02/first-order-normal-forms-supplement.tex:4-9`; `handbook/parts/p02/first-order-resolution-supplement.tex:4-8`; `handbook/annex/p02/first-order-calculi-supplement.tex:2-7`; `handbook/annex/p02/first-order-completeness-remainder.tex:2-6`.
- reasoning: The strongest case for reducing F1 is that the substantive source fixes have now been applied and that review/admission, build, and visual state are deliberately later gates. That is largely right for the six editorial supplement notices, but it is not yet the live disposition. Every listed notice still typesets `OPEN` or `unadmitted`, and the annex root still records two missing exact proof destinations plus absent duality content at lines 4-12. In addition, F6 retains a source-level exactness defect below. Thus F1 cannot yet be classified as only a late build/visual matter. Once F6 is fixed, each retained supplement is independently accepted, and the chair formally dispositions the off-route propositional fragment—discard it and remove the promise, or supply the promised destinations/content—the remaining admission-control, build, visual, and user gates may be tracked late under F1/F2. The printed notices must still be replaced or unrouted as a source edit; a build cannot cure them.
- exact correction: Close F6 and the independent source/content reviews; explicitly disposition the propositional-annex debt; then replace each accepted OPEN notice with ordinary reader attribution or unroute the rejected unit. Keep build/visual/user acceptance separate afterward.

### F3 — accept-fixed
- reply: accept-fixed
- prior position changed by: the new live matched-model, schema, incidence, and satisfaction definitions at `handbook/parts/p02/second-and-higher-order-logic-supplement.tex:47-165` and their revised annex proof at `handbook/annex/p02/higher-order-supplement.tex:63-136`.
- reasoning: The strongest opening objections are now answered at their exact failure points. The eligible Comp and graph-Choice families and all parameter/freshness conditions are displayed at body lines 47-79; the matched model class requires every predicate interpretation to belong to its relation domain at lines 51-53; matched consequence is defined at lines 87-95; predicate constants receive relation-sort representatives and an incidence translation at lines 102-128; the tagged structure is defined only under the predicate-domain hypothesis at lines 130-150; and the satisfaction/schema-correspondence theorem repeats that hypothesis at lines 152-165. This excludes the source-fidelity counterexample with `P^H` outside `R_n`. The annex predicate case uses that hypothesis at lines 73-82, and the collapse direction makes every predicate interpretation an extension of a declared relation-sort element at lines 102-124. `T_CC^sharp`, `H_CC`, `Gamma^sharp`, and matched consequence now have definitions before the derived calculus at body lines 168-234. F6 remains a separate exactness issue for the displayed quantifier-rule substitution, but it no longer leaves the F3 model class or adequacy biconditional undefined.

### F4 — accept-fixed
- reply: accept-fixed
- prior position changed by: the route and scope changes at `handbook/parts/p02.tex:59-60` and `handbook/parts/p02/variants.tex:27-40,106-189`.
- reasoning: The adversarial definition cycle is gone: the driver now routes `variants.tex` before the matched-SOL supplement; the flat translation and sort axioms are defined at variants lines 106-152; `VarGuard_MS` follows them at lines 154-172; and the reduction theorem follows the guard at lines 174-189. My uncountable-sort counterexample is also expressly excluded: lines 35-40 restrict the reduction to at-most-countable sorts and symbols, require a fixed injection of the disjoint sorted variable stocks into the governing countable variable supply, and state that larger signatures are outside the theorem. The strongest opposing points therefore no longer apply to the live statement.

### F5 — accept-fixed
- reply: accept-fixed
- prior position changed by: `handbook/parts/p02/propositional-metatheory-supplement.tex:12-65`.
- reasoning: The exact set-indexed syntax now precedes both the compactness and completeness theorems. Lines 12-19 define `Form(P)` and valuations; lines 20-25 define `Gamma |-_{CPL(P)} phi` as a finite discharge-labelled tree using exactly the inherited natural-deduction rules with metavariables ranging over `Form(P)`. The compactness scheme at lines 29-35 and completeness theorem/proof at lines 44-65 use that same domain and derivability notation. This closes both the adversarial definition-before-use objection and my stronger objection that the Lindenbaum quotient had no selected proof relation.

### F6 — still-open
- reply: still-open
- current location: `handbook/restoration/inherited-12262-12289.tex:4-9`; `handbook/parts/p02/second-and-higher-order-logic-supplement.tex:21-36`; `handbook/registry/calculi/sol.tex:17-20`.
- reasoning: The repair now gives the arity-preserving recursive clauses, stops below an `X` binder, alpha-renames a binder for the substituting variable `U`, traverses other binders, and covers predicate constants. It therefore fixes the capture counterexample in substance. The remaining defect is exactly the deterministic-freshness requirement accepted in the ledger: line 28 selects “the least fresh relation variable of the same arity,” but the inherited syntax says only that each `RelVar_n` is countably infinite; it never orders or enumerates that set. Infinite supply proves that a fresh variable exists, not that a least one is defined. Different fresh choices give different formula strings, and this handbook does not quotient second-order formulas by an already defined alpha-equivalence relation. The four sheet rules therefore still refer to a substitution that is not a unique string-valued operation.
- exact correction: Fix an explicit enumeration `RelVar_n = {X^n_k : k in N}` and use its index order in line 28, or define second-order alpha-equivalence and make substitution return an equivalence class. The first option matches the deterministic first-order substitution convention and is the smaller repair.

### F10 — accept-fixed
- reply: accept-fixed
- current location: `handbook/parts/p02/variants.tex:406-426`.
- reasoning: The former pointer now has an exact definition before the lookup table. It fixes positive arity, makes a generalized quantifier an isomorphism-closed class of pairs `(M,R)` with `R subseteq M^n`, gives the formation `Q xbar phi`, states its satisfaction clause under updated assignments, and defines `FOL(Q-family)` for a fixed arity-indexed family. Lines 421-424 explicitly retain the family as semantic data on which compactness, LS behavior, and axiomatizability depend. This meets the strongest opening demand rather than merely expanding the acronym.

### F11 — accept-fixed
- reply: accept-fixed
- current location: `handbook/parts/p02/first-order-depth.tex:167-186`, before the table at lines 188 onward.
- reasoning: The new definition fixes EXPTIME and NEXPTIME as unions of deterministic/nondeterministic `2^(n^k)` time classes, coNEXPTIME by complement, and 2EXPTIME by deterministic `2^(2^(n^k))` time. It also fixes the machine and finite-encoding convention and distinguishes determinism, complementation, and exponential level. The classes are now defined before their first table use, answering the strongest ambiguity point.

### F12 — accept-fixed
- reply: accept-fixed
- current location: `handbook/registry/calculi/sol.tex:9-16`; `handbook/parts/p02/second-and-higher-order-logic-supplement.tex:97-100,197-200`.
- reasoning: The sheet identity now names the linked first-order equality base in prose, lines 10-13 provide live links to that calculus and the defining derivability, and lines 14-16 state the editorial projection standing and controlling comparison sources. The first body use is a human-readable hyperlink, and the later projection sentence links the sheet again. The dependency path no longer terminates at raw internal labels. F3/F6 govern mathematical content separately; they are not navigation objections.

### F13 — accept-fixed
- reply: accept-fixed
- current location: `handbook/parts/p02/variants.tex:336-355`.
- reasoning: Lines 338-342 now state the exact countable-family constructor together with the finite union of free-variable sets and one-variable-at-a-time quantification. Lines 343-350 give the all-members/some-member satisfaction clauses, and line 352 makes the finite-total-free-variable condition part of the grammar. The opening family `{P(x_n): n in N}` is now explicitly inadmissible, so the counterexample no longer applies.

### F14 — accept-fixed
- reply: accept-fixed
- current location: `handbook/parts/p02.tex:54-56`; `handbook/parts/p02/simple-type-logical-constants.tex:1-30`.
- reasoning: The new convention is routed immediately after the inherited typed-term syntax and before its semantic chapter. It declares bottom and negation with types, fixes every binary Boolean constant at the right-associated type `o -> (o -> o)`, states left-associated application, supplies classical denotations, types the predicate parameter in the existential abbreviation, and requires those denotations to inhabit the selected Henkin domains. The source-fidelity defects in the first attempted repair—literal `qquad`, ambiguous arrow association, and untyped `P`—are absent at lines 11-21. The later extensionality formula is now a well-typed object-language formula.

### F16 — accept-fixed
- reply: accept-fixed
- current location: `handbook/parts/p02/first-order-calculi-supplement.tex:164-177`; `handbook/registry/calculi/hilbert-fol.tex:1-18`.
- reasoning: The comparison row now attributes A1-A5 and Gen to Mendelson and the primitive-existential schemas to Kleene, cites both sources, and states the needed bridge: the displayed existential schemas make `exists x phi` interderivable with `not forall x not phi`, so elimination of primitive existential transfers the universal-fragment strong-completeness theorem to the combined sheet. This directly engages the source-fidelity objection that a source comment alone was not adequacy evidence. The bridge is mathematically sound for the displayed classical Hilbert base, while the locally proved dependency-sensitive deduction theorem remains a separate claim.

## Round disposition

- accept-fixed: F3, F4, F5, F10, F11, F12, F13, F14, F16.
- still-open: F1; F6 (only the missing order on each relation-variable stock).
- merge: none.
- needs-evidence: none.
- new findings: none; the F6 residual is the unfixed part of the accepted F6 correction, not a new record.

This round inspected only the agenda records against the current frozen files. It made no manuscript, control, test, or build edit and ran no build.

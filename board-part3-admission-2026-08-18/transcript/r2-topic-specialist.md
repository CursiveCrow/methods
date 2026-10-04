# Round 2 — correctness/model-theory topic specialist

## Position

**All eight of my Round-1 records are `accept-fixed` on the latest live
source/content bytes.  I found no remaining mathematical or specification
blocker in the expanded Round-2 agenda.**

This conclusion is narrower than a build or publication verdict.  I reread the
complete current graph rooted at `handbook/parts/p03.tex` and
`handbook/annex/p03.tex`: two roots, twenty-one exact-source wrappers,
twenty-one inherited units, eight routed body additions, and two routed annex
additions, fifty-four reachable files in all.  I read no other seat's Part III
transcript.  I made no manuscript, control, test, or generated-file edit and
did not run a build.

Several defects were exposed and repaired in the live files while this round
was in progress.  I record those below as evidence-pinned `accept-fixed`
records rather than pretending they were never present.  The decisions here
are against the final bytes I reread after those repairs.

## Reconciliation of Round-1 records

### F1 — accept-fixed

- **Prior claim:** reader-routed additions declared themselves OPEN and
  unadmitted.
- **Current evidence:**
  - `handbook/parts/p03/types-ultraproducts-supplement.tex:4-9` now gives
    ordinary attribution and exact source/proof status, with no depth-row or
    admission token.
  - `handbook/annex/p03/types-ultraproducts-supplement.tex:2-4` now describes
    the complete proof and its nonreplacement boundary without an OPEN token.
  - `handbook/parts/p03/qe-categoricity-games-supplement.tex:3-7` now gives
    ordinary attribution and proof boundaries.
  - `handbook/parts/p03.tex:60-62` now agrees with that status instead of
    calling the routed QE derivative unadmitted.
- **Reasoning:** the remaining `OPEN` comment at
  `handbook/parts/p03.tex:10-13` concerns a deliberately *unrouted* generator,
  not accepted reader content.  The legitimate statement that Vaught's
  conjecture remains open at
  `handbook/parts/p03/classification-theory.tex:188-199` is mathematical
  content, not construction debt.  A recent survey continues to describe the
  general conjecture as open: [Pillay et al., *The number of countable models
  of first-order theories*](https://arxiv.org/abs/2508.06854).
- **Status:** accept-fixed

### F2 — accept-fixed

- **Prior claim:** the model-symbol lookup used `S_n(T)`, Stone topology, and
  ultraproduct notation before their definitions.
- **Current evidence:** `handbook/parts/p03.tex:14-26` now routes the complete
  Types, Saturation, and Ultraproducts sequence through
  `SRC-07135-07149`, then its supplement, and only then
  `maps-elementarity-supplement.tex`.  The lookup entries remain at
  `handbook/parts/p03/maps-elementarity-supplement.tex:36-44`, after the exact
  type-space definition at
  `handbook/restoration/inherited-06510-06629.tex:30-53` and ultraproduct
  definition at `handbook/restoration/inherited-06942-07134.tex:10-35`.
- **Status:** accept-fixed

### F3 — accept-fixed

- **Prior claim:** the positive grammar omitted `\bottom`, falsifying the
  Lyndon biconditional at the bottom formula.
- **Current evidence:**
  `handbook/parts/p03/preservation-abstract-logic.tex:160-177` includes
  `\bottom` as a base case of both positive and existential-positive formulas;
  the theorem at lines 202-206 now has the required expressive base.  The
  one-element equality-structure counterexample from R1 no longer applies.
- **Source check:** the local statement remains tied to `Lyndon1959`; the
  primary article is [Lyndon, *Properties Preserved under
  Homomorphism*](https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-9/issue-1/Properties-preserved-under-homomorphism/pjm/1103039178.full).
- **Status:** accept-fixed

### F4 — accept-fixed

- **Prior claim:** Robinson's common and union signatures lacked kind/arity
  compatibility.
- **Current evidence:**
  `handbook/parts/p03/preservation-abstract-logic.tex:101-106` now requires
  every overlap symbol to have the same function/relation kind and arity,
  defines the common restriction, and uses compatible unions of the symbol
  sets and arity maps.  The unary-versus-binary `f` counterexample is excluded.
- **Status:** accept-fixed

### F5 — accept-fixed

- **Prior claim:** the Boolean-algebra tables reused logical `\land`, `\lor`,
  and `\neg` as nonlogical function symbols.
- **Current evidence:**
  `handbook/parts/p03/qe-categoricity-games-supplement.tex:40-43` declares two
  fresh binary operation symbols, one fresh unary complement symbol, and two
  nullary symbols, all disjoint from the logical alphabet.  Both catalog rows
  at lines 68 and 111 use that declared Boolean-algebra signature.
- **Status:** accept-fixed

### F6 — accept-fixed

- **Prior claim:** the routed QE annex duplicated the inherited DLO theorem and
  its already-complete inline proof.
- **Current evidence:** `handbook/annex/p03.tex:3-4` routes only the legitimate
  types/ultraproduct proof supplement and the new editorial-proof file.  The
  former DLO supplement is no longer routed.  The exact inherited DLO theorem
  and proof remain at
  `handbook/restoration/inherited-07295-07468.tex:108-131` unchanged.
- **Status:** accept-fixed

### F7 — accept-fixed

- **Prior claim:** computable model theory ended in a pointer-only stub.
- **Current evidence:**
  `handbook/parts/p03/finite-model-theory.tex:142-172` now defines computable
  presentation and computable categoricity and states the exact theorem that
  the rational order is computably categorical.  The complete effective
  back-and-forth proof is reciprocal at
  `handbook/annex/p03/editorial-proofs.tex:3-19`.  The unused degree-spectrum,
  computable-dimension, and relative-categoricity names have been removed;
  lines 174-175 now give only an ordinary further-reading citation.  The stale
  source-header `stub` claim was also removed at
  `handbook/parts/p03/finite-model-theory.tex:1-3`.
- **Reasoning:** decidability of the two order relations makes each bounded
  interval search effective; density/endlessness makes it terminate, and the
  alternating least-missing-element schedule makes the union total and onto.
- **Status:** accept-fixed

### F8 — accept-fixed

- **Prior claim:** three chair-authored surveys were not visibly
  distinguished from exact inherited source.
- **Current evidence:** rendered reader notes now appear at
  `handbook/parts/p03/classification-theory.tex:6-9`,
  `handbook/parts/p03/finite-model-theory.tex:8-12`, and
  `handbook/parts/p03/preservation-abstract-logic.tex:8-12`.  Each identifies
  the chapter as separately authored, cites its controlling sources, and says
  it does not replace the exact inherited material.
- **Status:** accept-fixed

## Round-2 focused agenda

### Fraisse classes, the random graph, and finite random graphs — accept-fixed

- **Locations:**
  `handbook/parts/p03/classification-theory.tex:25-97` and
  `handbook/parts/p03/finite-model-theory.tex:42-62`.
- The age, HP, JEP, AP, ultrahomogeneity, and limit theorem have the standard
  countable-relational hypotheses.  Free amalgamation proves AP for finite
  simple graphs, and the finite extension property gives the unique countable
  Rado graph and its aleph-zero categoricity.
- I tried to refute the probability bridge in two ways.  First, the chapter's
  ambient distribution over all binary-relation structures would allow loops
  and directed edges; the final text explicitly switches to uniform labeled
  irreflexive symmetric `G(n,1/2)`.  Second, pointwise convergence for one
  selected pair `U,V` would not establish a universally quantified extension
  axiom; the final text supplies the union bound
  `n^(u+v)(1-2^(-(u+v)))^(n-u-v) -> 0` at lines 49-58.
- **Sources:** [Rado 1964](https://doi.org/10.4064/aa-9-4-331-340) and the
  locally cited `Fraisse1954`, `Fagin1976`, and `GlebskiiEtAl1969` records.
- **Disposition:** accept-fixed

### Countable saturation and Vaught's problem — accept-fixed

- **Location:** `handbook/parts/p03/classification-theory.tex:143-199`.
- `small` is defined for complete theories in countable languages by
  countability of every `S_n(T)`.  The proof explanation correctly uses the
  fact that finite parameter expansions still have only countably many types,
  iterates countable elementary extensions, and takes an elementary-chain
  union.  The uniqueness clause has both models countable and saturated, the
  exact back-and-forth range.
- `I(T,aleph_0)` has explicit standing, Vaught's theorem says only
  `I(T,aleph_0) != 2`, and the text does not confuse it with the still-open
  full dichotomy.
- **Independent scholarly check:** [Schlicht, *An Introduction to Model
  Theory*, Theorems 4.2.8-4.2.9](https://philippschlicht.github.io/teaching/files/modeltheory2017.pdf).
- **Disposition:** accept-fixed

### Ehrenfeucht-Mostowski construction and unstable spectra — accept-fixed

- **Locations:** chapter-wide size convention at
  `handbook/parts/p03/classification-theory.tex:17-23`; indiscernibles,
  blueprint, EM reduct, and the two separate theorems at lines 201-276.
- The basic theorem asserts only existence of distinct order indiscernibles.
  The stronger theorem first introduces a coherent quantifier-free blueprint
  in a Skolem expansion and then obtains functorial elementary embeddings of
  the reducts.  The nonstructure conclusion is separately stated for complete
  unstable `T` and uncountable `kappa > |T|`; it is no longer bundled into the
  basic EM theorem or used before `|T|` is defined.
- **Primary check:** Shelah's original result states the maximal `2^kappa`
  spectrum above the theory-size bound: [Shelah 1971](https://doi.org/10.1007/BF02771463).
- **Disposition:** accept-fixed

### Stability spectrum and nonforking — accept-fixed

- **Locations:** parameter-set type notation at
  `handbook/parts/p03/classification-theory.tex:281-296`; order property,
  dividing, forking, simplicity, cardinal stability, and the nonforking package
  at lines 298-428.
- `S_n(A)`, `tp(a/A)`, the `Ab` abbreviation, and type restriction are all
  defined before the theorem.  Kappa-stability is now defined for every
  infinite `kappa`, so `aleph_0`-stability remains meaningful even before a
  language-countability hypothesis; the usual spectrum analysis is separately
  located at `kappa >= |T|`.
- Dividing uses an `A`-indiscernible sequence with the original parameter as
  its zeroth member; forking is its finite-disjunction closure.  The stable
  theorem states extension, symmetry, and transitivity with the needed base and
  restriction types.  The implications omega-stable => superstable => stable
  are one-way, with neither converse claimed.
- **Disposition:** accept-fixed

### Morley rank and Baldwin-Lachlan — accept-fixed

- **Location:** `handbook/parts/p03/classification-theory.tex:430-542`.
- The transfinite rank clauses are total, allow parameters, and correctly give
  `RM(X)=0` exactly for nonempty finite `X`; the former contrary sentence is
  gone.  Algebraic closure, Morley degree, pregeometry/exchange,
  basis/dimension, and prime-over-a-set are defined before the proof outline
  uses them.  Strong minimality retains the elementary-extension clause.
- The rank/omega-stability equivalence explicitly assumes a complete theory in
  a countable language.  Baldwin-Lachlan assumes completeness, a countable
  language, and categoricity in one uncountable cardinal before asserting
  omega-stability, the strongly minimal geometry, Morley transfer, and the
  `1`-or-`aleph_0` countable-model dichotomy.
- **Primary check:** [Baldwin and Lachlan, *On Strongly Minimal
  Sets*](https://doi.org/10.2307/2271517).
- **Disposition:** accept-fixed

### O-minimality — accept-fixed

- **Location:** `handbook/parts/p03/classification-theory.tex:544-619`.
- Unary o-minimality, cells, monotonicity, and cell decomposition have distinct
  standings.  In the repaired band clause, each boundary is either a
  continuous definable `M`-valued function on the whole base cell or a constant
  infinity; the earlier mixed extended-valued-function overrun is gone.
- The monotonicity partition and the function-compatible cell decomposition
  agree with the authoritative statements; see [Pillay-Steinhorn
  1986](https://doi.org/10.1090/S0002-9947-1986-0833697-X) and the locally
  cited `VanDenDries1998` book.
- **Disposition:** accept-fixed

### Model companions, Robinson, Beth, and Craig — accept-fixed

- **Locations:**
  `handbook/parts/p03/preservation-abstract-logic.tex:21-126,252-296` and
  `handbook/annex/p03/editorial-proofs.tex:21-77`.
- The existential fragment is explicitly `exists y-bar` plus a
  quantifier-free matrix.  Robinson's test no longer claims that
  existential closure directly invokes Tarski-Vaught; lines 67-77 identify the
  required diagram/compactness normal-form step.  Companions, model companions,
  and model completions have distinct hypotheses and standings, and the ACF/RCF
  examples use the correct ring/ordered-ring languages.
- The joint-consistency proof checks closedness of the compatibility sets,
  clopen separation, a common complete reduct theory, Keisler-Shelah
  ultrapowers, Los transfer, and transport of the second signature.  The Beth
  proof handles the always-false and always-true edge cases with `bottom` and
  `not bottom`, then obtains both directions of the explicit definition from
  the common-language separator.  Craig/Robinson/Beth equivalence remains
  citation-only where the full third implication is not reproduced.
- **Primary sources:** [Robinson 1956](https://doi.org/10.1016/S1385-7258(56)50008-X),
  [Beth 1953](https://doi.org/10.1016/S1385-7258(53)50042-3), and the local
  `Craig1957` record.
- **Disposition:** accept-fixed

### `L(Q_1)` and Lindstrom's characterization — accept-fixed

- **Locations:**
  `handbook/parts/p03/preservation-abstract-logic.tex:298-398` and
  `handbook/annex/p03/editorial-proofs.tex:79-279`.
- `Q_1` is the unary generalized quantifier whose selected set is uncountable.
  The theorem states the Keisler completeness result, countable compactness,
  and the at-most-`aleph_1` model bound in a countable signature; it does not
  claim full compactness or a countable model for `Q_1 x (x=x)`.
- I checked every substantive Lindstrom proof stage.  The finite sequence code
  makes reachable graphs finite partial isomorphisms; the witnessing
  back-and-forth family is first replaced by its downward closure, which
  justifies exact one-pair append extensions.  The finite-rank lemma is proved
  by simultaneous induction on rank and free-variable arity.  The compactness
  construction uses a relational successor graph and explicit chain formulas
  `beta_k(c)`, not an ill-typed successor term; the nonstandard element has all
  standardly many predecessors, yielding one potential-isomorphism family.
  Temporary constants are accounted for by the regular logic's stated
  fresh-constant abstraction clause.
- **Primary sources:** [Keisler 1970](https://doi.org/10.1016/S0003-4843(70)80005-5)
  and [Lindstrom 1969](https://doi.org/10.1111/j.1755-2567.1969.tb00356.x).
- **Disposition:** accept-fixed

### Independence-friendly and dependence logics — accept-fixed

- **Location:**
  `handbook/parts/p03/preservation-abstract-logic.tex:400-480`.
- The dependence grammar explicitly contains first-order literals, `bottom`,
  positive dependence atoms, conjunction, disjunction, and the two
  quantifiers; negated dependence atoms are excluded.  The displayed lax team
  semantics includes the empty-team clause for `bottom`, splitting
  disjunction, set-valued nonempty existential supplementation, universal
  duplication, and the functional-dependence clause.
- The example now uses `forall x forall z exists y` with `=(x,y)`, so the atom
  genuinely forces one choice `y=f(x)` independent of `z`.  The former
  `forall x exists y` example was equivalent to its first-order matrix and no
  longer appears.  The expressive-power theorem is carefully restricted to
  sentences; open formulas retain team information.
- **Authoritative source:** [Vaananen, *Dependence
  Logic*](https://doi.org/10.1017/CBO9780511611193).
- **Disposition:** accept-fixed

## New Round-2 repair records

These records identify the concrete counterexamples that caused live repairs;
each is closed on the final bytes.

### F9 [must-fix -> accept-fixed] Quantifier rank was partial at bottom

- **Location:**
  `handbook/parts/p03/qe-categoricity-games-supplement.tex:150-161`.
- **Counterexample/harm:** the governing first-order grammar makes `bottom` a
  formula but not an atom.  Without its own rank clause, `qr(bottom)` was
  undefined, so bounded agreement and the EF/Lindstrom rank arguments did not
  quantify over every first-order sentence.
- **Applied correction:** line 152 now assigns rank zero to atoms *and
  `bottom`*.
- **Status:** accept-fixed

### F10 [must-fix -> accept-fixed] Classification notation and rank geometry were underdefined

- **Location:**
  `handbook/parts/p03/classification-theory.tex:17-23,281-296,377-403,430-542`.
- **Counterexamples/harm:** `|T|` formerly appeared after its EM use;
  `S_1(A)`, `tp(a/Ab)`, and restriction were formerly unintroduced; defining
  kappa-stability only for `kappa >= |T|` left `aleph_0`-stability undefined
  in an uncountable language; and allowing parameters makes every infinite
  definable set have at least rank one, refuting the former sentence that rank
  zero was not finiteness.
- **Applied correction:** all notation precedes use; the type-count predicate
  is defined for every infinite cardinal; rank zero is exactly nonempty
  finiteness; and the Morley-degree/pregeometry/prime-over vocabulary required
  by the outline is explicitly defined.
- **Status:** accept-fixed

### F11 [must-fix -> accept-fixed] Random-graph probability inference lacked its probability space and uniform bound

- **Location:** `handbook/parts/p03/finite-model-theory.tex:42-62`.
- **Counterexample/harm:** a uniform arbitrary binary relation permits directed
  edges and loops, so its limiting theory is not the Rado graph's theory.
  Moreover, convergence for one selected `U,V` does not imply the universal
  extension axiom over polynomially many choices.
- **Applied correction:** the paragraph explicitly switches to `G(n,1/2)` and
  supplies the polynomial-times-exponential union bound.
- **Status:** accept-fixed

### F12 [must-fix -> accept-fixed] O-minimal bands admitted non-cell boundary functions

- **Location:**
  `handbook/parts/p03/classification-theory.tex:576-592`.
- **Counterexample/harm:** the former extended-valued `f:C -> M union
  {+-infinity}` wording allowed a boundary that was `-infinity` on one
  definable region and finite on another, although standard cell boundaries
  are continuous `M`-valued functions or constant infinities.
- **Applied correction:** lines 584-586 impose exactly that dichotomy.
- **Status:** accept-fixed

### F13 [must-fix -> accept-fixed] Robinson's converse used an invalid direct Tarski-Vaught step

- **Location:**
  `handbook/parts/p03/preservation-abstract-logic.tex:24-77`.
- **Counterexample/harm:** existential closure for the standard
  existential/quantifier-free fragment is not, for one arbitrary pair of
  structures, identical to full elementarity.  The global model-completeness
  converse needs Robinson's diagram/compactness normal-form lemma.
- **Applied correction:** the fragment is defined at lines 28-30 and the
  converse now names and explains the diagram lemma at lines 67-73 before
  using existential equivalence in both directions.
- **Status:** accept-fixed

### F14 [must-fix -> accept-fixed] Lindstrom's complete-proof claim omitted typed coding steps

- **Location:** `handbook/annex/p03/editorial-proofs.tex:79-279`.
- **Counterexamples/harm:** the first draft used a binary successor relation as
  though it formed successor terms, did not justify an exact one-pair extension
  from an arbitrary back-and-forth family, and stated the finite-rank lemma
  only for sentences while its induction needs formulas with free variables.
- **Applied correction:** the annex now uses downward closure, explicit
  append equations and sort clauses, the simultaneous `(m,n)` induction, and
  relational chain formulas `beta_k(c)`.  Its five body/annex proof IDs are
  reciprocal and unique in the reachable graph.
- **Status:** accept-fixed

### F15 [must-fix -> accept-fixed] Dependence semantics was partial and its example was vacuous

- **Location:**
  `handbook/parts/p03/preservation-abstract-logic.tex:400-480`.
- **Counterexamples/harm:** `bottom` is neither an atom nor a first-order
  literal, so omitting its clause left satisfaction partial.  The old
  `forall x exists y` dependence example added no constraint beyond ordinary
  existential choice.
- **Applied correction:** the grammar/empty-team clause are total and the
  example adds a second universal variable from which the choice is explicitly
  independent.
- **Status:** accept-fixed

### F16 [must-fix -> accept-fixed] The computable-model repair retained unused technical names

- **Location:** `handbook/parts/p03/finite-model-theory.tex:142-175`.
- **Counterexample/harm:** degree spectrum, computable dimension, and relative
  categoricity were named but not required by any later definition or theorem,
  recreating the R1 pointer debt and violating the workspace rule for new
  technical terminology.
- **Applied correction:** only computable presentation and computable
  categoricity remain, both used by the theorem and proof; the rest is an
  ordinary broad further-reading sentence with no hypothetical terminology.
- **Status:** accept-fixed

## Final static/source checks

- Recursive reachability: **54 files**.
- Exact-source wrappers: **21/21** target the matching inherited interval; all
  inherited line counts equal their closed interval lengths.
- Proof reciprocity: **5 `proved=annex` declarations / 5 matching annex
  items**, with no missing or orphan item.  These are compactness by
  ultraproduct, computable categoricity of the rational order, Robinson joint
  consistency, Beth definability, and Lindstrom's theorem.
- Reachable labels: **95**, with no duplicate label in the Part III graph.
- Named-theorem destinations: the generated entries for Algebraically Closed
  Fields, Ryll--Nardzewski, and Morley's categoricity theorem target
  `thm:algebraically-closed-fields`, `thm:ryll-nardzewski`, and
  `thm:morley-categoricity`.  The wrapper-only theorem-environment hooks at
  `handbook/parts/p03.tex:27-58` attach those anchors to, respectively, the
  second theorem in `SRC-07150-07294` and the third/fourth theorems in
  `SRC-07295-07468`; direct counting of the exact inherited environments
  confirms all three destinations, while the inherited bytes remain unchanged.
- Reachable citations/status keys: **58**, all present in
  `handbook/bib/handbook.bib`.
- Reader-status scan: no reader-visible OPEN, unadmitted, owed, stub, or
  pointer-only construction statement remains.  The Vaught-conjecture use of
  the word `open` is its correct mathematical status.
- Checked clean again: the exact inherited map/substructure/elementarity
  proofs; type spaces, saturation/homogeneity, omitting types, ultrafilters,
  ultraproduct well-definedness, all Los induction cases, and diagonal
  elementarity; inherited QE, DLO, categoricity, back-and-forth; EF game rules
  and the parity invariant; finite-model zero-one/Fagin/Trakhtenbrot scopes;
  preservation theorem directions and all stated language restrictions.
- Not checked by design: compilation, reference rendering, landscape/figure
  layout, PDF visual inspection, historical byte/hash provenance beyond the
  wrapper/interval check, and human/user acceptance.

## Round-2 conclusion

For the correctness/model-theory mandate, the current Part III source is
**acceptable at source/content level**.  Every R1 record is `accept-fixed`, all
direct Round-2 repair findings F9-F16 are `accept-fixed`, and I have no residual
content objection to place before the chair.  This does not close any separate
build, visual, source-fidelity, human, or user gate.

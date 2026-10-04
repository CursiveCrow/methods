# Part VII admission board, round 1: adversarial-publication review

Reviewer: adversarial-publication seat  
Mode: blind source/content audit; no other Part VII seat transcript was read.  
Disposition: **not source/content admissible in the current bytes**.

I read the charter and the complete 52-file graph rooted at
`handbook/parts/p07.tex` and `handbook/annex/p07.tex`: all 19 exact wrappers and
their inherited artifacts, eight routed editorial body files, and four routed
editorial annex files. I also inspected the Part VII portions of the generated
audit, named-theorem, symbol-registry, and compact-index surfaces. I made no
manuscript/control/generated/test edit and ran no build or test. Read-only
route traversal found no missing `\input` and no repeated live input. A
read-only lexical pass found no missing bibliography key; calculus-sheet and
rule destinations are macro-generated from live `handbook/registry/calculi`
files, so their actual PDF links remain a build gate.

## Findings

### F1 — blocker — mandatory A-113 is expressly OPEN and unrouted

- **Location:** `handbook/parts/p07.tex:31-32` and
  `handbook/generated/audit-p07.tex:1-58`.
- **Evidence:** the Part VII root says the generated register is intentionally
  OPEN and unrouted because it scans historical chapters rather than the exact
  live route. Its current candidate prints `--` identities for exact-source
  definitions and named results, including LK soundness, cut elimination,
  normalization, subject reduction, and STLC strong normalization.
- **Reader harm:** the required per-part theorem/definition register has no
  reader route, and simply routing the candidate would publish missing
  identities with no statement destinations.
- **Exact correction:** generate A-113 strictly from the 52-file live graph;
  add literal, non-byte-altering anchors for every exact theorem- and
  definition-class unit; classify exact proof, sketch, and cited standing;
  hyperlink every ID; and route the table exactly once at the end of Part VII.
- **Status:** open, source/content.

### F2 — blocker — A-159 silently omits live exact Part VII named results

- **Location:** examples of omitted live results are
  `handbook/restoration/inherited-11599-11627.tex:14-28`,
  `handbook/restoration/inherited-11768-11823.tex:11-55`,
  `handbook/restoration/inherited-11824-11881.tex:20-57`,
  `handbook/restoration/inherited-11961-12029.tex:47-63`, and
  `handbook/restoration/inherited-12030-12100.tex:44-70`; omission is visible
  in `handbook/generated/named-theorem-index.tex`.
- **Evidence:** exact LK soundness, cut elimination, propositional subformula,
  empty-sequent underivability, NJ normalization, STLC subject reduction, and
  STLC strong normalization are named theorem/corollary environments without
  labels. The generated named index contains the already labelled exact Craig,
  Beth, cut/mix, and subformula results, but none of those unlabelled names.
- **Reader harm:** a reader using the advertised named-theorem index cannot
  retrieve central Part VII results, while the table purports to cover every
  live named theorem/lemma destination.
- **Exact correction:** give every unlabelled exact Part VII result a governed
  wrapper hook and add it to the generator's source-result map; fail generation
  on an unanchored live named result instead of skipping it; regenerate A-159.
- **Status:** open, source/content.

### F3 — major — exact source and editorial additions are indistinguishable on the reader surface

- **Location:** `handbook/parts/p07.tex:3-29`; representative editorial headers
  are `calculi-and-derivability-supplement.tex:1-12`,
  `cut-elimination-and-interpolation-supplement.tex:1-12`,
  `normalization-and-curry-howard-supplement.tex:1-11`, and
  `arithmetic-proof-theory-supplement.tex:1-12`.
- **Evidence:** source standing, historical-derivative boundaries, OPEN status,
  and nonreplacement claims exist only in comments. The exact restoration
  scope is nonprinting, and Part VII has no visible source map or local reader
  notes comparable to the repaired Part VI surface.
- **Reader harm:** the published artifact does not tell a reader where frozen
  inherited prose ends and historical derivatives or new register-driven
  chapters begin. Proof-status preservation and nonreplacement claims cannot
  be audited from the reader artifact.
- **Exact correction:** add a visible Part VII source map listing the 19 exact
  intervals in order and classifying every editorial body/annex addition; add
  short local reader notes where a derivative directly follows exact source;
  keep administrative OPEN/admission state out of printed prose.
- **Status:** open, source/content.

### F4 — blocker — registered A-117, the sequent-versus-ND correspondence figure, is absent

- **Location:** the LK--ND theorem and translation are at
  `handbook/parts/p07/calculi-and-derivability-supplement.tex:143-163`; the only
  live Part VII figures are
  `handbook/parts/p07/normalization-and-curry-howard-supplement.tex:101-122`
  and `:127-218`.
- **Evidence:** those figures are A-151 (Curry--Howard triangle) and A-152
  (STLC typing derivation beside intuitionistic ND). Neither translates a
  sequent derivation into natural deduction as required by A-117.
- **Reader harm:** a must/should publication commitment is missing, and the
  central LK--ND equivalence has no promised rule-correspondence retrieval
  surface.
- **Exact correction:** add a labelled A-117 figure beside
  `thm:p07-lk-nd-equivalence`, showing one concrete finite LK derivation and its
  ND translation with matched rule steps and the finite-succedent
  `\bigvee\Delta` convention. Keep A-152 as the distinct STLC/ND figure.
- **Status:** open, source/content; layout remains build/visual after creation.

### F5 — blocker — D-P8-001 completeness is only a lookup to existing sketches

- **Location:** `handbook/parts/p07/calculi-and-derivability-supplement.tex:94-113`.
- **Evidence:** `def:p07-lk-completeness-lookup` says both propositional and
  first-order canonical-LK completeness theorems are sketched, presently use
  Cut, and are not made cut-free by the distinct defined-negation cut sketch.
  D-P8-001 is a must-depth completeness commitment at E treatment.
- **Reader harm:** Part VII contains no complete arbitrary-finite-sequent LK
  completeness proof and explicitly disclaims the cut-free bridge that the
  proof-theory placement is meant to supply.
- **Exact correction:** state the exact canonical LK theorem, base theory and
  equality scope; give a reciprocal complete annex proof or a complete
  translation from the already proved ND completeness theorem; separately
  prove any cut-free corollary only after matching the cut-elimination calculus.
- **Status:** open, source/content.

### F6 — blocker — D-P8-002 LK/Natural-Deduction equivalence is citation-only and A-117 cannot substitute for its proof

- **Location:** `handbook/parts/p07/calculi-and-derivability-supplement.tex:143-168`.
- **Evidence:** the finite-succedent translation is defined, but
  `thm:p07-lk-nd-equivalence` is `cited=Gentzen1934a` and has no annex item.
  The register requires an expanded LK \(\leftrightarrow\) ND equivalence
  theorem at must priority.
- **Reader harm:** no rule-by-rule translation, discharge/eigenvariable check,
  or converse construction establishes the promised correspondence for the
  exact current sheets. A historical citation does not verify present registry
  identity.
- **Exact correction:** supply both translations for the exact equality-free
  `sheet:lk` and `sheet:nd-fol` presentations in a reciprocal annex, including
  empty succedent, contexts, structural rules, quantifiers, discharge and
  eigenvariables; mark the theorem at the resulting evidence level.
- **Status:** open, source/content.

### F7 — blocker — Maehara/Craig/Beth prose simultaneously claims a sketch and a complete proof

- **Location:**
  `handbook/parts/p07/cut-elimination-and-interpolation-supplement.tex:83-115,117-167`
  and `handbook/annex/p07/interpolation-supplement.tex:16-33`.
- **Evidence:** the lemma is `sketched=annex:p7.interp.1`; the proof boundary
  says initial, structural, propositional-placement, and quantifier cases are
  omitted and the method remains sketched. The annex repeats those omissions.
  Immediately afterward, the body prints “Complete induction for the
  partition lemma,” says it proves the lemma, then prints Craig and Beth proof
  paragraphs. Those paragraphs still compress all rule-specific placements
  and depend on a cut-elimination theorem whose exact standing is only a
  sketch (`inherited-11768-11823.tex:11-55`).
- **Reader harm:** one result has mutually incompatible proof statuses, body
  proof prose is inflated beyond the annex token, and the must requirement
  D-P8-004/N-a-070 (“Craig interpolation proved by Maehara”) remains unmet.
- **Exact correction:** move the complete argument to the annex; enumerate and
  verify every selected LKd initial/structural/logical/quantifier partition
  case; state whether cut elimination is imported as a cited theorem or proved
  for that exact calculus; then mark Maehara, Craig and Beth with honest,
  reciprocal statuses. Until then remove “Complete” and “This proves.”
- **Status:** open, source/content.

### F8 — blocker — must-depth Church--Rosser remains an explicit proof sketch

- **Location:**
  `handbook/parts/p07/lambda-calculi-and-type-theories.tex:107-170` and
  `handbook/annex/p07/lambda-calculi.tex:4-49`.
- **Evidence:** `thm:p07-church-rosser` is `sketched`, and its annex note lists
  omitted capture-avoiding substitution, alpha-renaming, complete-development,
  beta-overlap, simulation, and grid inductions. D-P9-003 is a must E-treatment
  gap; N-a-015 also requires the confluence treatment.
- **Reader harm:** the defining central theorem of the untyped lambda-calculus
  entry is not proved at the promised depth, and normal-form uniqueness inherits
  that omission.
- **Exact correction:** complete the parallel-substitution and development
  inductions, every overlap case, equivalence of closures, and diamond-to-
  confluence grid argument in the annex; then promote only Church--Rosser and
  its corollary to the evidence actually supplied.
- **Status:** open, source/content.

### F9 — blocker — the selected MLTT calculus and its normalization theorem do not match

- **Location:**
  `handbook/parts/p07/lambda-calculi-and-type-theories.tex:397-448` and
  `handbook/registry/calculi/mltt-intensional.tex:4`.
- **Evidence:** the selected public sheet contains dependent products,
  dependent sums, identity types, and a cumulative predicative Russell
  universe hierarchy. The only normalization/equality/checking theorem is for
  the narrower Abel--Coquand--Dybjer core with dependent functions and one
  universe, and explicitly excludes sums, identity types, and the selected
  cumulative hierarchy. N-c-030 requires the MLTT calculus and its
  normalization/decidable-checking statements at must priority.
- **Reader harm:** the comparison table has evidence for a narrower external
  calculus but no theorem governing the actual handbook sheet. A reader cannot
  infer normalization, equality decision, or checking for the selected MLTT
  identity.
- **Exact correction:** either narrow `sheet:mltt-intensional` and the MLTT
  entry to exactly the cited calculus, or cite/state normalization and decision
  theorems for the full selected Pi/Sigma/identity/cumulative-universe system,
  with conversion and universe hypotheses matched literally.
- **Status:** open, source/content.

### F10 — blocker — N-a-049's promised Gentzen/propositional-core development remains citation-only

- **Location:**
  `handbook/parts/p07/arithmetic-proof-theory-supplement.tex:19-54,57-132`.
- **Evidence:** the chapter says the inherited source did not supply coding,
  assignment, or decrease and preserves that status. It then gives a multiset
  measure and six generic reduction rows, but no concrete reductions for the
  selected connectives/structural rules; `thm:p07-prop-cut-termination` remains
  `cited=TroelstraSchwichtenberg2000`. N-a-049 requires the ordinal assignment
  in full for the propositional core, and D-P8-005 requires the coding,
  assignment, and decrease components.
- **Reader harm:** a generic taxonomy and imported theorem are presented where
  the register calls for the actual local propositional reduction/decrease
  development. The table does not itself define the transformations it says
  decrease.
- **Exact correction:** fix the exact propositional derivation grammar and code,
  give each commuting/principal/structural reduction, prove the multiset
  decrease case by case, and route the complete proof to an annex. Keep the
  full arithmetic epsilon-zero analysis cited unless its larger obligations
  are separately discharged.
- **Status:** open, source/content.

### F11 — blocker — N-a-055 proof claims conflict with `cited=` statuses and a stale printed stub notice

- **Location:**
  `handbook/parts/p07/functional-interpretations.tex:325-413` and
  `handbook/annex/p07/functional-interpretations.tex:31-36`.
- **Evidence:** IPC disjunction, HA disjunction, and HA numerical existence are
  all marked `cited=TroelstraVanDalen1988`, but the body then prints three
  paragraphs headed “Proof of …” and derives them through a cited canonicity
  theorem. The annex says the “visible N-a-055 stub” records missing complete
  proofs, although the current body has no such stub and instead claims proofs.
- **Reader harm:** proof status, body/annex contract, and internal workflow prose
  disagree. The reader cannot tell whether N-a-055 is closed, cited, proved
  locally, or still owed.
- **Exact correction:** remove the internal register ID/stub sentence. Move the
  three proof arguments to reciprocal annex items and mark them
  `proved=annex:...` if they are complete from the explicitly cited canonicity
  theorem; otherwise remove the proof headings and retain cited status. Record
  every remaining normalization/erasure obligation honestly.
- **Status:** open, source/content.

### F12 — major — A-189's route table makes false completeness and stale-sheet claims

- **Location:** `handbook/parts/p07/proof-complexity.tex:185-315`.
- **Evidence:** the table says it lists every status-bearing result exactly
  once, but omits at least propositional cut termination, omega-calculus cut
  elimination, HA proof-term canonicity, and four-modal-calculi adequacy. It
  says the MLTT remainder has no active sheet at lines 244-266 even though
  `sheet:mltt-intensional` is live, and says generalized frameworks await exact
  modal sheets at lines 294-300 even though the structural chapter links four
  sheets and states a cited adequacy theorem.
- **Reader harm:** the advertised navigation apparatus sends readers away from
  live destinations and silently drops status-bearing results.
- **Exact correction:** regenerate or exhaustively rewrite A-189 from the live
  graph and status tokens; include every theorem once, list all active sheets,
  and distinguish cited, proved-annex, and sketched-annex destinations.
- **Status:** open, source/content.

### F13 — major — A-071 contradicts the later active generalized-calculus route

- **Location:**
  `handbook/parts/p07/calculi-and-derivability-supplement.tex:171-223` and
  `handbook/parts/p07/structural-extensions.tex:81-225`.
- **Evidence:** the calculi catalog classifies hypersequent, labelled, display,
  and deep-inference rows as citation-only with no active sheet. The later live
  chapter links `sheet:gs5-avron`, `sheet:labelled-k-negri`,
  `sheet:display-k-wansing`, and `sheet:deep-s5-stouppa`, prints one derivation
  for each, and states adequacy. It also calls those examples “owed” at
  `structural-extensions.tex:106` even though they immediately follow. Finally,
  `thm:p07-four-modal-calculi` records four systems' evidence with a status
  token naming only `Wansing1994`, while the prose depends on four distinct
  sources.
- **Reader harm:** two live lookup surfaces give opposite answers about sheet
  existence, the prose retains construction debt already discharged, and the
  generated named index would report only one source for a four-source claim.
- **Exact correction:** update A-071 after the structural chapter's sheets;
  remove “owed”; split adequacy into source-specific theorems or use a status
  representation that records all four supporting citations without implying
  Wansing proves the Avron, Negri, and Stouppa cases.
- **Status:** open, source/content.

### F14 — major — the Part VII symbol registry omits the selected MLTT notation

- **Location:** `handbook/generated/symbols-tables.tex:482-565` and
  `handbook/registry/symbols.csv`; the live notation is declared at
  `handbook/registry/calculi/mltt-intensional.tex:4` and used at
  `handbook/parts/p07/lambda-calculi-and-type-theories.tex:399-447`.
- **Evidence:** the Part VII registry contains STLC, System F, ordinal,
  Dialectica, epsilon, and proof-complexity rows, but no rows for the MLTT
  context/type/term/equality judgments, dependent Pi/Sigma, identity types, or
  cumulative universes. Direct searches of the source registry and generated
  tables find no such MLTT entries.
- **Reader harm:** a major must-priority calculus introduces overloaded Pi,
  Sigma, identity, colon, turnstile, and universe glyphs without the global
  scope/standing distinctions used everywhere else in the handbook; the
  compact symbol index cannot retrieve them.
- **Exact correction:** register the selected MLTT judgments and type formers
  with precise standing, scope, first use, and collision notes; regenerate the
  full and compact symbol surfaces.
- **Status:** open, source/content.

## Checked-clean coverage

### Lot 1 — calculi, cut elimination, subformula, Herbrand, interpolation

- Read all fourteen exact and editorial units through source line 11960 plus the
  calculi/interpolation annexes.
- Exact LK/LJ syntax, multiset/single-succedent standing, structural and
  quantifier conditions, derivability types, cut/mix equipollence, exact cut
  sketch boundary, proved cut-free subformula lemma, first-order qualification,
  midsequent/Herbrand hypotheses, and cited Craig/Beth statements are coherent
  apart from F5-F7.
- A-070 and A-071 tables are present; A-071 is stale under F13. A-117 and A-113
  are absent under F1/F4. Exact proof sketches are not silently treated as
  proofs in the exact source itself.

### Lot 2 — normalization, Curry--Howard, lambda calculi, System F, MLTT

- Read all five exact normalization wrappers, the categorical/visual
  supplement, the full lambda/type chapter, and both lambda annex items.
- The exact NJ normalization, STLC subject-reduction and normalization sketches
  state their omissions honestly. A-072, A-073, A-151, and A-152 are present.
  Untyped syntax/substitution/reduction standing, confluence-versus-
  normalization warning, lambda/recursive citation, S--K basis, System F
  syntax/impredicativity/confluence/normalization, Church-versus-Curry decision
  boundary, and HoTT/CIC/proof-net exclusions are checked clean apart from
  F8-F9 and F14.

### Lot 3 — arithmetic proof theory, omega logic, realizability, Dialectica

- Read the exact Gentzen/epsilon-zero boundary, the full arithmetic supplement,
  the full functional-interpretation chapter, and its annex.
- A-074 is present; PRA/HA/I-Sigma/reverse-mathematics definitions, relative
  ordinal definition, six calibrated table rows, Veblen/Gamma-zero boundary,
  PRA-versus-finitism warning, omega-calculus identity and cited quantitative
  cut theorem are source-coherent apart from F10.
- System T, the quantifier-free Dialectica target, translation clauses, cited
  soundness/relative consistency, number-realizability clauses, ECT restriction,
  Markov boundary, and cut-free LJ extraction are checked clean apart from F11.

### Lot 4 — epsilon/structural extensions, proof mining, proof complexity, apparatus

- Read the entire structural and proof-complexity chapters and all global
  retrieval surfaces referenced from Part VII.
- Equality-free epsilon calculus and all three cited epsilon-theorem scopes are
  clear. The four architecture definitions, worked examples, and proof-mining
  boundary are present, subject to the catalog/source defects in F13.
- Cook--Reckhow, p-simulation, the fixed PHP encoding, cited Haken bound,
  Frege/extended-system definitions and A-075 comparison table are coherent.
  A-186 further reading exists. A-189 exists but is materially stale (F12);
  A-113/A-117/A-159 and MLTT symbol retrieval fail as above.
- All bibliography keys used by the live Part VII graph exist lexically. Sheet
  and rule IDs flagged by a plain `\label` parser are in the live calculus
  registry and are intentionally generated by `\calculussheet`/`\hbrule`.

## Non-build / non-visual boundary

I did not compile the handbook, run the checker or any generator, inspect a
PDF, or validate actual links, citations, numbering, index pages, floats,
landscape tables, proof-tree graphics, blank versos, or overfull pages. Static
source presence is not render acceptance. In particular A-151/A-152, the wide
structural/lambda/proof-complexity tables, rule-sheet destinations, generated
indexes, and the still-absent A-117 require the final build and page-by-page
visual check after F1-F14 are repaired. Administrative, provenance, human
mathematical, and final user gates remain external.

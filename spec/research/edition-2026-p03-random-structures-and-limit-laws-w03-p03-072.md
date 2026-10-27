# Research note: P3 40.9 Ehrenfeucht-game proofs of asymptotic results (w03a-p03-072)

## Provenance

- Source read this session: Spencer, "Logic and Random Structures", author version,
  https://cs.nyu.edu/faculty/spencer/papers/ircsallsubm.pdf (fetched 2026-10-12 with WebFetch;
  PDF 30 pages, dvips 2007-07-06, SHA-256 digest b81de4d3a6126e08ab363f6438ab495c343b442a4b03beae7fb8295568bf545c,
  identical to the copy saved by the previous attempt under
  tmp/agent-scratch/w03a-w03a-p03-072-b1-author/src/). Text extracted with pdftotext -layout to
  tmp/agent-scratch/w03a-w03a-p03-072-b1-author/today/spencer.txt; printed page numbers 1-30 equal PDF pages.
- Pages read this session: 2-13, 18-21, 26-27.
- Version: the author's separately formatted text (sections 1-14 plus an unnumbered "About the references").
  Not the Springer 2007 printed chapter (Finite Model Theory and Its Applications, doi 10.1007/3-540-68804-8);
  no printed-chapter locator is used. The reader text states this once.
- Held path listed in the packet (graedel-2007-fmt-descriptive-complexity-ch3.pdf) is Graedel's chapter 3,
  not Spencer's chapter; it was not used.

## Locators used (all seen this session)

p.2 almost surely / almost never, generality of the notion; p.3 reduction to complete almost sure theory,
finiteness-of-proof argument, unary strategy; pp.6-8 rooted graphs, pi/7 examples, random triple has no common
neighbour; pp.9-11 T_alpha schemas, large deviation omitted; p.11 choice of t_0..t_u; pp.11-12 closure strategy,
Inside/Outside, omitted combinatorial lemmas; pp.12-13 constant-p strategy; p.13 "there exist r distinct" in the
almost sure theory; p.19 zero-one law not expected at rational alpha; pp.20-21 level game; pp.26-27 Section 14
(game, theorem, isolated vertex example, two corollaries, generalization to finitely many relation symbols);
p.27 attribution to Ehrenfeucht / Fraisse and Shelah-Spencer.

## Existing treatments found (A9)

Listed: finite-model-theory.tex (sec:p03-zero-one-law), qe-categoricity-games-supplement.tex (sec:p03-ef-games).
Not listed but found, and now linked instead of repeated:
- random-structures-and-limit-laws-w03-p03-064.tex sec:p03-w03-p03-064-game: Spencer Section 14 game, new-vertices
  lemma, isolated-vertex example, ee corollary, infinite game example (same K_m / K_omega example as the previous
  072 draft), completeness corollary, Alice's Restaurant completeness. Owner of unit ED26-SRC-050-0004 per
  readonly_units.
- 064 / 068 / 070: closure, Nonexistence, Finite Closure Lemma, axioms of T_alpha.
- 070 thm:p03-w03-p03-070-extension: the full one-round closure step (Inside / Outside, genericity lemmas),
  for a pair of parameters; 070-complete proves completeness of T^-_lambda by formula induction.
- thm:p03-ef is cited (not proved) in two P3 files; thm:p03-w03-p03-038-pointed-ef is the proved form.
The previous 072 draft (untracked, written 2026-10-11) duplicated 064's game section and re-proved the closure
lemmas, finite closure and the closure step; those parts were removed and replaced by cross-references.

## What 40.9 now contains

Body handbook/parts/p03/random-structures-and-limit-laws-w03-p03-072.tex; annex
handbook/annex/p03/random-structures-and-limit-laws-w03-p03-072.tex.
- thm:...-game-theorem (Spencer's statement, both readings of "depth t"; proof bridges to 038-pointed-ef).
- thm:...-infinite-language (handbook's counterexample: infinitely many unary symbols, depth-1 agreement,
  Spoiler wins one round) - boundary of Spencer's "finite number of relation symbols".
- def:...-finite-models warning (boundary of 064's completeness corollary).
- def:...-random-structure, thm:...-transfer (almost sure + complete => zero-one; consistency), def:...-method.
- def:...-lookahead (070's strict sequence), thm:...-closure-strategy (the invariant, winning, completeness of
  T^-_lambda; proof iterates 070-extension), thm:...-sparse-zero-one (conditional on AS_alpha),
  def:...-pi-seven example (t_2 = 3 at u = 2), def:...-limits warning; relationships; sources.

## Open items

- The corollary thm:...-sparse-zero-one is stated under (AS_alpha); 065 now proves (AS_alpha)
  (thm:p03-w03-p03-065-counting, -generic-extension; Nonexistence by 068) and its annex for
  thm:p03-w03-p03-065-shelah-spencer uses this corollary. The 40.9 text links those results.
- Driver insertion of the body and annex files (handbook/parts/p03.tex after finite-model-theory input,
  handbook/annex/p03.tex after feferman-vaught-composition) is a lead action; until it is done the section has
  no text on the reader route.

## Continuation

Block 2 (2026-10-12): fixed the guard hit in Provenance (digest now written "SHA-256 digest"; same fix in the
return file). Re-verified this session, against the saved copy of the author PDF (digest unchanged,
tmp/agent-scratch/w03a-w03a-p03-072-b1-author/src/ircsallsubm.pdf, text in .../today/spencer.txt), every locator
used in the body: p.2 generality of almost sure truth; p.3 finiteness / completeness step and unary schemas;
p.7 alpha = pi/7; pp.7-8 random triple has no common neighbour; pp.10-11 large deviation omitted; p.11 t_0..t_u;
p.12 Inside/Outside and the omitted combinatorial lemma; pp.12-13 constant p; p.13 "There exist distinct
x_1..x_r" in the almost sure theory; p.19 zero-one law not expected at rational alpha; pp.20-21 level game;
pp.26-27 Section 14 (game, "fundamental" result, isolated vertex, corollaries, finite number of relation
symbols, no finite models); p.27 Ehrenfeucht / Fraisse attribution.
Checked the pi/7 arithmetic against 070's epsilon definition (eps(1) = 3 alpha - 1) and the closure-strategy
annex against the statement of thm:p03-w03-p03-070-extension and def:p03-w03-p03-070-admissible.
unit-compile ok; filtered tree check shows no finding in 072 files; find_fused_spaces clean on all owned files.
Components ED26-SRC-050-0004-C001..C015 belong to the unit owned by w03a-p03-064 (readonly_units); this packet
links that unit's labels and does not write its components.

## Author correction 2026-10-26

Discharged the redundant AS_alpha hypothesis of the game-based sparse
zero-one corollary by invoking 070's proved almost-sure axiom theorem in
its annex. Updated the surrounding explanation to make the dependency
explicit. The purely model-theoretic closure strategy still does not by
itself prove a probability limit, and nothing has been extended to rational
exponents. This is an author correction, not independent acceptance or
verification of the distinct printed Springer source.

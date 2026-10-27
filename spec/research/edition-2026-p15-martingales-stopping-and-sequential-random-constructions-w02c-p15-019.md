# Packet w02ca-p15-019 (P15, chapter 162; sections 162.1, 162.3, 162.4)

Source held and opened this session:
`source/references/durrett-probability-2019-01-11/PTE5_011119.pdf` (Durrett,
Probability: Theory and Examples, version 5, 11 January 2019). Printed page =
PDF page - 8 in the range used.

## Locators read in the held file

- p. 217: definition of martingale with conditions (i) integrable, (ii) adapted,
  (iii) conditional identity; sub/super by replacing = with inequalities.
- p. 218: Example 4.2.2 (quadratic martingale, i.i.d. increments);
  Theorem 4.2.4 (supermartingale, n > m); Theorem 4.2.5 (sub via -X,
  martingale as both).
- pp. 219-220: predictable sequence, transform (H.X)_n, doubling system;
  Theorem 4.2.8 and its Remark (sub and martingale cases); stopping time
  {N = n} in F_n; Theorem 4.2.9; alternating times N_j for a submartingale.
- p. 223: Exs. 4.2.1 (reduced filtration, martingale, sigma(X_1..X_n)),
  4.2.2 (submartingale with supermartingale square), 4.2.5 (martingale tending
  to minus infinity, non-identically distributed increments).
- pp. 230-234: Section 4.3.4; Lemma 4.3.9, Thms 4.3.10-4.3.13, Figs 4.3-4.4,
  Exs. 4.3.11-4.3.13 (Binomial(3,1/2) only).
- p. 235: Theorem 4.4.1. pp. 238-239: Exs. 4.4.1-4.4.6 (4.4.6 attributes the
  martingale S_n^2 - s_n^2 to "Exercise 4.2.2", which in this edition is a
  different exercise).
- p. 277: discrete F_N = {A : A cap {N=n} in F_n for all n}, "the information
  known at time N" (Section 5.2).
- pp. 367-368: Thm 7.3.6 (F_S subset F_T, continuous time), Thm 7.3.8 (B_S in
  F_S, Brownian motion).

## Continuation

- Written in editable hosts: maximal-inequalities C013 (annex 345-380, body
  237-244) and C021 (body 392-402).
- Written in the new chapter (owned files, label tag p15-w02c-p15-019): the
  adapted convention and counter-case (C001), sign duality and the
  reduced-filtration cases (C003), transform hypotheses and submartingale case
  (C006), event-comparison lemma and sampling cases with worked example (C009),
  stopped-field forms and source attributions (C007, C008), crossing times
  without adaptedness (C011), boundary-calculation sources (C019).
- Patch requests: work/waves/w02ca/patches/w02ca-p15-019.json, 12 entries on
  the read-only martingales-and-convergence body and annex; anchors verified.
  C001, C006, C007, C008, C009, C011, C019 stay partial until the lead applies
  them and inputs the new chapter after parts/p15/sequential-evidence.
- Checks run: tools/find_fused_spaces.py clean; tools/waves.py unit-compile ok
  with no overfull boxes; tools/check.py shows only the earlier notation-scope
  finding for \mathcal D at maximal-inequalities body (dyadic example, not
  introduced here).
- Source note: Durrett Ex. 4.4.6 (p. 239) refers to "Exercise 4.2.2" for
  S_n^2 - s_n^2; in this edition Ex. 4.2.2 (p. 223) is a different exercise.
- Not touched: the readonly unit uniform-integrability-and-conditional-limits
  (owner w02c-p15-014), including its assessment disputes C007, C009, C016.

### Session 2 (2026-10-10, after the assessment disputes)

Locators read again in the held file this session: pp. 217-221 (Example
4.2.1 with the supermartingale reading, superharmonic definition and display
(4.2.1), ball B(x,r) on p. 218; remark before Thm 4.2.4 on p. 218;
predictable sequences, gambler and stock readings, "the martingale" doubling
system and its table on p. 219-220; readings of Thm 4.2.8 and the stopping
system on p. 220; remark after Thm 4.2.10 on p. 221), p. 230 (Section 4.3.4,
recursion (4.3.4), "Galton-Watson process", offspring distribution) and
p. 234 (Ex. 4.3.13 family-name model).

- Maximal-inequalities host: C016 Galton-Watson name and offspring
  distribution in def:p15-branching-genealogy (body 303-312); C021 Ex. 4.3.13
  model and question in thm:p15-branching-calculations (body 403-415), with
  the binomial pmf derivation and the 0.236 bound in the annex (707-718).
- Owned chapter: C003 multistep-definition lemma and the source remark
  (body 65-85, annex 59-99); C002 superharmonic definition, mean-value
  inequality with a full proof, worked example (body 283-345, annex 371-464);
  C005 readings (body 347-361); C019/C006 doubling system named, sure-thing
  appearance, Thm 4.2.8 readings, corollary doubling-unfavorable (body
  363-407, annex 466-513); C008 stopping system reading (body 409-420);
  C011 remark and corollary no-loss (body 422-443, annex 515-526).
- Patch file now 18 entries; entry 12 names "the martingale"; entries 13-18
  add cross-references at the read-only entries (C002, C005, C003, C006,
  C008, C011). All anchors verified unique.
- Still lead-only: C001 (definition amendment), C006 (1), C007, C008, C009,
  C011 (1) attributions/hypotheses in the read-only host.
- Not written (readonly unit, owner w02c-p15-014): uniform-integrability
  C016, C019.

### Session 3 (2026-10-10, block 1 of r4, after the second assessment)

Locators read again in the held file this session: pp. 230-232 (Thm 4.3.10
with "so Z_n/mu^n -> 0", remark "should be intuitive ... species will die
out" on p. 231; "When mu <= 1, the limit of Z_n/mu^n is 0" on p. 232),
p. 235 (Thm 4.4.1 and its Remark: S_0 = 1, N = inf{n: S_n = 0}, pointer to
Section 5.7; Example 4.4.3 Kolmogorov route), pp. 236-237 (Example 4.4.5),
p. 237 (Thm 4.4.8 and Remark: conditional analogue of the variance identity),
p. 238 (Example 4.4.9), p. 239 (Ex. 4.4.7 opening sentence),
pp. 255-256 (Section 4.8 opening: the unbounded question with Example
4.2.13; Thms 4.8.1-4.8.3). Section 5.7 of this edition (p. 317) is titled
"Periodicity, Tail sigma-field"; the body reports the source's pointer and
names Section 4.8 as where the question is answered in the martingale chapter.

- Maximal-inequalities host, body: C002 remark and Section 4.8 pointer
  (lines 56-72); C004 locator to example 4.4.3 (102); C006 locator to
  example 4.4.5 (135); C009 conditional variance remark (186-194); C014
  Ex. 4.4.7 framing quoted and addressed (282-298); C018 normalized limit,
  boundary cases and the source's remark (397-413); C019 locator to example
  4.4.9 (434).
- Annex: C002 boundary proof (63-77); C009 side-by-side computation
  (274-285); C014 comparison with direct Doob (453-471); C018 normalized
  limit proof (615-626).
- Martingales-and-convergence disputes (C001, C002, C003, C005, C006, C008,
  C009, C011, C019) and C007: content is in the owned chapter; all 18 patch
  anchors re-verified unique this session. Remaining: lead applies the patch
  file and inputs the new chapter after parts/p15/sequential-evidence and
  annex/p15/sequential-evidence.
- Checks: find_fused_spaces clean; unit-compile ok, 0 overfull; check.py
  shows only the earlier \mathcal D notation-scope finding (dyadic example).

### Session 4 (2026-10-11, block 1 of r5)

Locator read again in the held file this session: p. 239 (PDF page 247),
Exs. 4.4.10 and 4.4.11. Ex. 4.4.11 opens by continuing the notation of
Ex. 4.4.10 and assumes only b_m increasing to infinity and the series of
E xi_m^2 / b_m^2; it does not restate EX_0^2 < infinity.

- C006 (martingales-and-convergence): owned body lines 153-168, a
  paragraph before thm:p15-w02c-p15-019-transform-cases stating that the
  first assertion of thm:p15-predictable-transform holds only for adapted X
  with E|X_n| finite at each n and is read with these hypotheses; item 1
  proves it, item 2 shows it false otherwise; the host annex step that uses
  each hypothesis is named. Host statement change is still patch entry 5.
- C012 (maximal inequalities): thm:p15-weighted-martingale-law restated at
  the source's scope (body 233-260): X a martingale with only E|X_n| finite,
  xi_m notation, b_m nondecreasing to infinity and nonzero; attribution to
  exs. 4.4.10-4.4.11, p. 239, noting EX_0^2 < infinity is not part of
  Ex. 4.4.11; worked example with EX_0^2 = infinity. Annex 347-412: proof
  via Y_n = sum xi_m/b_m (increments only), square-summable theorem on Y,
  general Kronecker lemma, X_0 finite a.s.; proof of the example.
- Return file line numbers re-derived from the current files (several
  earlier ranges were stale).
- Checks: find_fused_spaces clean; unit-compile ok, 0 overfull; check.py
  only the earlier \mathcal D notation-scope finding (body 514).
- Remaining lead actions unchanged: apply the 18-entry patch file and input
  the owned chapter after sequential-evidence in both drivers.

### Session 5 (2026-10-11, block 2 of r5)

Locators read again in the held file this session: p. 217 (definition with
conditions (i)-(iii), (ii) adaptedness), pp. 235-239 (Section 4.4 in full:
Thm 4.4.6 on p. 237 states only the martingale case, a.s. and in L^p for
p>1; supremum integrability appears in its proof; no submartingale
convergence statement, no closure identity, no counterexamples in the
section or its exercises).

- Maximal-inequalities C007: body 138-168 re-attributes
  thm:p15-martingale-lp-convergence (cite now on the martingale statement
  only; the constant-C bound, E|X_inf|^p<=C, closure and nonnegative
  submartingale extension marked supplied; failures stated with cref to
  thm:p15-maximal-convergence-boundaries (1), (2), marked supplied).
  Annex 205-249 derives both limitations from those items explicitly.
- Uniform-integrability C007/C009 (readonly unit, owner w02c-p15-014): not
  edited. Patch entries 2-3 (definition requires adaptedness) close them on
  the route once applied.
- Checks: find_fused_spaces clean; unit-compile ok, 0 overfull; check.py
  only the earlier \mathcal D notation-scope finding (body 530).

### Session 6 (2026-10-11, block 3 of r5)

Locators read again in the held file this session: pp. 247-249 (PDF
255-257): Chung's line and the obvious/incredible readings of Thm 4.6.9,
the "very useful" judgement (p. 248), Ex. 4.6.1 with the normal-population
reading and the prior/posterior definitions (p. 248), the remark ending
Ex. 4.6.3 (p. 249), Section 4.7 opening (reversed; decreasing sigma-fields
make the theory simple, p. 249).

- Uniform-integrability C011, C015, C016, C019 (readonly unit, owner
  w02c-p15-014): the owner's file limit-theorems-and-concentration-w02c-p15-014
  already has def:p15-w02c-p15-014-levy-readings, -dyadic-price,
  -prior-posterior (with thm:p15-w02c-p15-014-posterior-mean) and
  -reversed-martingales, each matching the source items above. Not
  duplicated here. Remaining: lead inputs that file in both drivers
  (owner patch file w02ca-p15-014.json entries 4-5).
- Maximal-inequalities C013: annex 414-451 writes the conditional square
  computation; no change.
- No owned file changed. Checks: unit-compile ok, 0 overfull;
  find_fused_spaces clean; check.py only the earlier \mathcal D
  notation-scope finding (body 530).

### Session 7 (2026-10-11, block 4 of r5, redirect)

Locators read again in the held file this session (pdftotext -layout,
printed page = PDF page - 8): p. 217 (conditions (i)-(iii), (ii)
adaptedness); pp. 244-250 in full: UI definition and M+1 remark (p. 244),
"A common way to check" before Thm 4.6.2 (p. 245), Thm 4.6.4 and
Lemmas 4.6.5-4.6.6 (p. 246), Thm 4.6.7 and Thm 4.6.8 with its proof
ending in the pi-lambda identification Y = E(X|F_inf) (p. 247), Thm 4.6.9
with Chung's line and the two readings (pp. 247-248), Thm 4.6.10 titled
"Dominated convergence theorem for conditional expectations", Example
4.6.11 and Ex. 4.6.1 with prior/posterior (p. 248), Exs. 4.6.2-4.6.7 and
Section 4.7 opening (p. 249), Thms 4.7.1-4.7.3, 4.7.3 introduced as
"Theorem 4.6.8 backwards", scalar only (p. 250).

The redirect gap list held only disputes of the readonly unit
uniform-integrability-and-conditional-limits (owner w02ca-p15-014) from
the confirm step, which does not apply rule S10. The owner's chapter
already holds C001, C003, C011, C012, C015, C016, C019; nobody had
requested C007, C009 (adaptedness, source locator) or C021.

- Patch file entries 19-31 (1-based; 0-based 18-30), all on the
  read-only UI host, anchors unique and disjoint from the owner's
  indices 6, 7, 9, 10: 19-22 adaptedness named at its uses (body
  thm:p15-submartingale-ui opening; annex 204-206, 219-221 with the
  increasing events A_k, 234-235); 23 locator of the identification
  (Thm 4.6.7, Lemmas 4.6.5-4.6.6 pp. 246-247; proof of Thm 4.6.8 p. 247);
  24 vector extension marked as supplied, scalar Thm 4.7.3 p. 250;
  25-31 one-sentence pointers to the owner's entries (apply only with
  the owner chapter routed).
- Scratch compile (tmp/agent-scratch/w02ca-r5-w02ca-p15-019-b4-author)
  of the UI host with entries 19-31 and owner indices 6, 7, 9, 10 applied,
  next to the owner chapter: no error; overfull count equal to the
  unpatched baseline after rewording entry 19's first line.
- Defect in another packet's request: w02ca-p15-014.json index 9
  (0-based) contains U+000B where \varphi was meant; pdflatex stops on it.
  Not edited (other packet's file); reported in the return notes.
- Owned chapter: one dependency sentence at the end of
  sec:p15-w02c-p15-019-relationships (body 486-495) naming the three uses
  of condition (ii) in thm:p15-submartingale-ui and
  thm:p15-closed-martingale.
- Checks: unit-compile ok, 0 overfull; find_fused_spaces clean (owned
  files, editable hosts, patched scratch copies); check.py only the
  earlier \mathcal D notation-scope finding (maximal-inequalities body
  530).
- Remaining lead actions: apply patch entries 1-31 of this file, the
  owner's driver inputs (indices 3-4) before entries 25-31, and the
  driver inputs of the owned chapter after sequential-evidence.

### Session 8 (2026-10-11, block 1 of r6)

Locators read again in the held file this session (pdftotext -layout, PDF
pages 252-258 = printed pp. 244-250): UI definition and the M+1 remark
(p. 244), Thm 4.6.2 (p. 245), Chung's line with the obvious and incredible
readings (p. 247), "very useful", Thm 4.6.10 with its title, Ex. 4.6.1
prior/posterior (p. 248), remark closing Ex. 4.6.3 and Section 4.7 opening
with "reversed" and "particularly simple" (p. 249).

- Gap list again held only the readonly unit
  uniform-integrability-and-conditional-limits (owner w02c-p15-014):
  C001, C003, C011, C012, C015, C016, C019. Not written here. The owner's
  entries still exist in limit-theorems-and-concentration-w02c-p15-014
  (def/thm ui-arbitrary 563-598, ui-moment-source 599, levy-readings 677,
  dyadic-price 724, conditional-dominated 749, prior-posterior 777 with
  posterior-mean 816, reversed-martingales 828); both owner files remain
  untracked and are not input by either driver.
- Patch file w02ca-p15-019.json: all 31 anchors re-verified unique; the
  read-only hosts are unchanged since session 7.
- No owned file changed. Checks: unit-compile ok, 0 overfull;
  find_fused_spaces clean; check.py only the earlier \mathcal D
  notation-scope finding (maximal-inequalities body 530).
- Remaining lead actions unchanged: input the owner chapter
  (w02ca-p15-014.json driver entries), apply entries 1-31 of this
  packet's patch file, input this packet's chapter after
  sequential-evidence in both drivers.

### Session 7 (2026-10-11, block 2 of r6)

Locators read again in the held file this session: pp. 247-248 (PDF
255-256): Thm 4.6.9 titled "Levy's 0-1 law" (p. 247), the line from
Chung, the obvious and incredible readings (pp. 247-248), the "very
useful" judgement and Thm 4.6.10's title (p. 248).

- Uniform-integrability C001, C003, C011, C012, C015, C016, C019
  (readonly unit, owner w02c-p15-014): the owner chapter
  limit-theorems-and-concentration-w02c-p15-014 still holds the matching
  entries (labels re-verified) and is still not input in either driver;
  pointer patches 25-31 re-verified (each anchor unique). Patch entry 27
  rewritten so the routed statement names Levy's 0-1 law in the text and
  states the obvious best-guess reading, Chung's line and the closing
  judgement. No second treatment written here.
- Remaining lead actions: w02ca-p15-014 indices 3-4 (driver inputs of
  the owner chapter), then this packet's patch entries 25-31; the earlier
  18-entry set and the input of the owned chapter are unchanged.
- Checks: find_fused_spaces clean; unit-compile ok, 0 overfull; check.py
  only the earlier \mathcal D notation-scope finding (body 530).

### Session 9 (2026-10-12, block 1 of r6, gap list C001, C003, C007, C009, C011, C015, C016, C019)

Held file reopened this session (pdftotext -layout, PDF pages 252-258 =
printed pp. 244-250): the M+1 remark (p. 244), "A common way to check"
(p. 245), "very useful" (p. 248), prior and posterior distribution
(p. 248), "a lot of machinery" (p. 249), Section 4.7 opening with
"reversed" and "particularly simple" (p. 249), condition (ii) adapted
used throughout.

- The gap list again held only the readonly unit
  uniform-integrability-and-conditional-limits (packet readonly_units:
  owner w02c-p15-014). Under rule A14 nothing of that unit is written
  here. Owner entries re-read and matched to each item: C001
  def/thm ui-arbitrary (M+1 bound, member with infinite mean not UI);
  C003 thm ui-moment-source (any phi >= 0, integrability derived,
  "common way to check"); C011 levy-readings (Chung's line, both
  readings, "very useful"); C015 dyadic-price (machinery remark);
  C016 prior-posterior with posterior-mean (normal population, prior,
  posterior); C019 reversed-martingales (name and the simplicity claim
  with its reason). C007, C009: this packet's patch entries 2-3 and
  19-23. The owner chapter is still untracked and not input in either
  driver.
- Patch file w02ca-p15-019.json: all 31 anchors re-verified unique
  against the current hosts. Owner file w02ca-p15-014.json index 9
  (0-based) still contains U+000B where \varphi was meant.
- No owned file changed. Checks: unit-compile ok, 0 overfull;
  find_fused_spaces clean; check.py only the earlier \mathcal D
  notation-scope finding (maximal-inequalities body 530).
- Remaining lead actions unchanged: w02ca-p15-014 indices 3-4 (owner
  chapter inputs) and the U+000B fix in its index 9; this packet's
  patch entries 1-31; input of this packet's chapter after
  sequential-evidence in both drivers.

### Session 10 (2026-10-12, block 2 of r6, gap list UI C001, C003, C011, C015, C016, C019)

Held file reopened this session (pdftotext -layout, PDF pages 252-258 =
printed pp. 244-250): M+1 remark (p. 244), "A common way to check"
(p. 245), Chung's line, obvious and incredible readings (p. 247), "very
useful" and prior/posterior (p. 248), "a lot of machinery", Section 4.7
opening with "reversed" and "particularly simple" (p. 249), "is easy"
after Thm 4.7.3 (p. 250).

- The gap list held only the readonly unit
  uniform-integrability-and-conditional-limits (packet readonly_units:
  owner w02c-p15-014). Rule A14: not written here. Owner entries in
  limit-theorems-and-concentration-w02c-p15-014 re-read and matched to
  each item: C001 def/thm ui-arbitrary (563, 583); C003
  thm ui-moment-source (599) with the "common way to check" paragraph;
  C011 levy-readings (677); C015 dyadic-price (724); C016
  prior-posterior (777) with posterior-mean (816); C019
  reversed-martingales (828). Owner chapter still untracked and not
  input in either driver; owner patch w02ca-p15-014.json indices 3-4 are
  those inputs, and its index 9 still contains U+000B.
- Patch file w02ca-p15-019.json: all 31 anchors re-verified unique.
- No owned file changed. Checks: unit-compile ok, 0 overfull;
  find_fused_spaces clean; check.py only the earlier \mathcal D
  notation-scope finding (maximal-inequalities body 530).
- Remaining lead actions unchanged.

### Session 11 (2026-10-12, block 3 of r6, gap list UI C001, C003, C011, C012, C015, C016, C019)

Held file reopened this session (pdftotext -layout, PDF pages 252-257 =
printed pp. 244-249): M+1 remark (p. 244), "A common way to check"
(p. 245), Chung's line and the obvious reading (p. 247), "very useful",
Thm 4.6.10 titled dominated convergence theorem for conditional
expectations, prior/posterior (p. 248), "a lot of machinery", Section 4.7
opening with "reversed" and "particularly simple" (p. 249).

- The gap list held only the readonly unit
  uniform-integrability-and-conditional-limits (packet readonly_units:
  owner w02c-p15-014). Rule A14: not written here. Owner entries in
  limit-theorems-and-concentration-w02c-p15-014 re-verified at the same
  lines as session 10 (563, 583, 599, 677, 724, 749, 777, 816, 828). Owner
  chapter still untracked and not input in either driver.
- Patch file w02ca-p15-019.json: all 31 anchors re-verified unique.
- Return file: owner packet id corrected to w02c-p15-014 in the
  readonly-unit entries.
- No owned file changed. Checks: unit-compile ok, 0 overfull;
  find_fused_spaces clean; check.py only the earlier \mathcal D
  notation-scope finding (maximal-inequalities body 530).
- Remaining lead actions unchanged: input the owner chapter
  (w02ca-p15-014.json driver entries; its index 9 no longer holds U+000B), apply
  entries 1-31 of this packet's patch file, input this packet's chapter
  after sequential-evidence in both drivers.

### Session 12 (2026-10-13, block 1 of r6, gap list UI C001, C003, C007, C009, C011, C015, C016, C019)

Held file reopened this session (pdftotext -layout, PDF pages 252-257 =
printed pp. 244-249): M+1 remark (p. 244), "A common way to check"
(p. 245), Chung's line (p. 247), "very useful" and posterior distribution
(p. 248), "a lot of machinery", Section 4.7 opening with "reversed" and
"particularly simple" (p. 249).

- The gap list held only the readonly unit
  uniform-integrability-and-conditional-limits (packet readonly_units:
  owner w02c-p15-014). Rule A14: not written here. Owner entries in
  limit-theorems-and-concentration-w02c-p15-014 re-verified at the same
  lines (563, 583, 599, 677, 724, 749, 777, 816, 828). C007, C009: this
  packet's patch entries 2-3 and 19-23. Owner chapter still untracked and
  not input in either driver; the read-only UI host is unchanged
  (mtime 8 September).
- Patch file w02ca-p15-019.json: all 31 anchors re-verified unique.
- No owned file changed; editable hosts unchanged since 2026-10-11.
  Checks: unit-compile ok, 0 overfull; find_fused_spaces clean; check.py
  only the earlier \mathcal D notation-scope finding
  (maximal-inequalities body 530).
- Remaining lead actions unchanged: input the owner chapter
  (w02ca-p15-014.json driver entries), apply entries 1-31 of this
  packet's patch file, input this packet's chapter after
  sequential-evidence in both drivers.

### Session 13 (2026-10-13, block 2 of r6, gap list UI C007, C009)

- Guard G1 (spec/research/edition-2026-authoring-batch-intake-13.json):
  not edited by this packet; no working-tree change; last changed by
  commit 6de06cc3. Nothing to revert here.
- The gap list held only the readonly unit
  uniform-integrability-and-conditional-limits (owner w02c-p15-014).
  Patch file w02ca-p15-019.json gained entries 32-33 (1-based) on that
  read-only host: 32 states adaptedness in the opening of
  thm:p15-closed-martingale (C009, the "entry states adaptedness"
  option, independent of entries 2-3); 33 names at annex 239-241 why the
  F_infty-measurable limit version applies to the martingale. With 19-22
  (submartingale entry, annex 204-206, 219-221, 234-235) and 2-3
  (definition requires adaptedness), both C007 and C009 are covered once
  the lead applies them. All 33 anchors verified unique; 32-33 disjoint
  from w02ca-p15-014 indices 6, 7, 9, 10.
- Symbol intake: added bare \mathcal G (event-comparison lemma);
  tools/check.py now reported a soft notation-scope finding for it at
  body 127 and annex 131 (reads only the canonical registry).
- Checks: unit-compile ok, 0 overfull; find_fused_spaces clean; check.py
  only soft notation-scope findings (\mathcal G here, \mathcal D at
  maximal-inequalities body 530).
- Remaining lead actions: apply entries 1-33 of this packet's patch file;
  input the owner chapter (w02ca-p15-014 driver entries); input this
  packet's chapter after sequential-evidence in both drivers; adopt the
  symbol intake.

### Session 14 (2026-10-13, block 3 of r6, gap list UI C007, C009)

Held file reopened this session (pdftotext -layout): p. 217 (PDF 225),
definition with conditions (i)-(iii), (ii) adaptedness; p. 246 (PDF 254),
Thm 4.6.4 "For a submartingale" with (i)-(iii) and its proof, Lemmas
4.6.5-4.6.6.

- The read-only UI host is unchanged (mtimes 8 September); the owner
  chapter limit-theorems-and-concentration-w02c-p15-014 is now input in
  both drivers (commit 6de06cc3); this packet's chapter is not.
- Patch file w02ca-p15-019.json entries 19-22 and 32-33 rewritten so the
  fix no longer leans on def:p15-filtration-martingale or on entries 2-3:
  19 opens thm:p15-submartingale-ui by assuming the submartingale adapted
  (condition (ii), p. 217; equivalence cited to Thm 4.6.4, p. 246) and
  reads "adapted supermartingales"; 32 does the same for
  thm:p15-closed-martingale; 20-22 and 33 cite "adapted by hypothesis" at
  each use (annex 204-206, 219-221, 234-235, 239-241). All 33 anchors
  verified unique.
- Scratch compile (tmp/agent-scratch/w02ca-r6-w02ca-p15-019-b3-author) of
  the UI host with entries 19-33 and owner indices 6, 7, 9, 10: no error,
  11 overfull against 12 unpatched (theorem openings reworded to start
  with words).
- Checks: unit-compile ok, 0 overfull; find_fused_spaces clean (owned
  files, editable hosts, patched scratch copies); check.py only the soft
  notation-scope findings (\mathcal G here, \mathcal D at
  maximal-inequalities body 530).
- Remaining lead actions: apply entries 1-33 of this packet's patch file;
  input this packet's chapter after sequential-evidence in both drivers;
  adopt the symbol intake.

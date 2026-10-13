# P15 157.7: source variants (packet w02ca-p15-002, label tag p15-w02c-p15-002)

Files:
- handbook/parts/p15/probability-spaces-and-random-variables-w02c-p15-002.tex (body, new chapter)
- handbook/annex/p15/probability-spaces-and-random-variables-w02c-p15-002.tex (annex)
- handbook/registry/symbols-intake-p15-probability-spaces-and-random-variables-w02c-p15-002.csv
- No new bib keys: only DurrettPTEAuthor2019 (already in handbook.bib) is cited.

Source opened this session: source/references/durrett-probability-2019-01-11/PTE5_011119.pdf
(Durrett, Probability: Theory and Examples, Version 5, 11 January 2019). Book page n = PDF page n+8.
Pages read (text extraction and rendered images): 2, 3, 6-12, 15, 16, 17, 53, 54, 210, 214, 215, 457, 458.

## Gap-to-text map

| Gap | Where | Labels |
|---|---|---|
| measurable-probability C006 astragali (p. 3) | body sec astragali | def:p15-w02c-p15-002-astragali |
| C010 open rational rays, real open rectangles (p. 15, Ex. 1.3.2-1.3.3) | body + annex | thm:p15-w02c-p15-002-generator-variants |
| C011 notation X in F (p. 10, p. 215) | body | def:p15-w02c-p15-002-membership-notation, thm:p15-w02c-p15-002-indicator-membership |
| C014 indicator vs characteristic function (p. 10) | body | def:p15-w02c-p15-002-indicator-terminology |
| C016 (a)-(d) (pp. 16-17) | body + annex | def:p15-w02c-p15-002-extended-line, thm:...-order-borel, thm:...-domain-extension, thm:...-convergence-set, def:...-convergence-examples |
| C017 Omega_o measurable (p. 16) | body + annex | thm:p15-w02c-p15-002-convergence-set (ii) |
| C021 Theorem A.1.5 (pp. 457-458) | body + annex | thm:p15-w02c-p15-002-sigma-finite-uniqueness, def:...-uniqueness-failure |
| countable-product C009 nice (p. 53) | removed in run 3; see w02c-p15-004 | def:p15-w02c-p15-004-nice, thm:p15-w02c-p15-004-nice-coding |
| countable-product C013 failure + attributions (p. 53) | removed in run 3; see w02c-p15-004 | def:p15-w02c-p15-004-extension-failure, thm:p15-w02c-p15-004-nice-extension, sec:p15-w02c-p15-004-borel-cardinality |
| countable-product C015 Dudley attribution (p. 54) | removed in run 3; see w02c-p15-004 | def:p15-w02c-p15-004-extension-failure, thm:p15-w02c-p15-004-nice-extension, sec:p15-w02c-p15-004-borel-cardinality |
| regular-conditional C011 Borel's paradox (p. 210) | body + annex | def:p15-w02c-p15-002-borel-paradox, thm:p15-w02c-p15-002-borel-paradox |
| regular-conditional C012 Dieudonne/Doob/Faden, accumulation (p. 214) | body + annex | thm:p15-w02c-p15-002-ae-additivity, def:p15-w02c-p15-002-rcd-nonexistence |

## Provenance notes
- A14 tension: all three units are listed in readonly_units (owners w02c-p15-004, -008, -014),
  while the computed gap list for this packet asks for exactly these components. The owner packets'
  open duties do not contain these gaps (004 has C009/C013 closed and C015 only as the
  perfect-set proof; 008 has C011/C012 closed). The text was written in this packet's own new
  files only, as a supplement that links the owners' labels. Lead should check for duplication
  with any w02c-p15-014 text on measurable-probability C006/C010/C011/C014/C016/C017/C021.
- Durrett's Omega_o display uses limsup - liminf = 0, undefined for infinite equal values; the
  chapter reads Omega_o with a real limit and writes the extended-limit set explicitly.
- Durrett's p. 215 step B = (phi^{-1})^{-1}(A) in R uses a Borel image; thm nice-coding (iii)
  shows that this holds for all A exactly when phi(S) is Borel.
- Not reproduced (works not held): Andersen-Jessen 1948 counterexample (via Halmos 1950 p. 214,
  Neveu 1965 p. 84), Wegner 1973, Dudley 1989 sec. 13.1 perfect-set argument, Dieudonne 1948
  example, Doob 1953 p. 624, Faden 1985. Only Durrett's statements and attributions are given.

## Run 2 additions (resumed session)

| Gap | Where | Labels |
|---|---|---|
| measurable-probability C018 equal in distribution (pp. 11-12) | body sec notation | def:p15-w02c-p15-002-equal-in-distribution |
| measurable-probability C025 Measures on R^d (pp. 6-9) | body sec rd-measures + annex | def:...-rectangle-difference, thm:...-rectangle-inclusion-exclusion, def:/thm:...-negative-mass, thm:...-rd-construction, def:...-product-distribution, thm:...-product-difference |
| C025 boundary pointer | patch request work/waves/w02ca/patches/w02ca-p15-002.json | host def:p15-measure-integration-boundary |
| regular-conditional C005 (2), C007 nice hypothesis of thms 4.1.17-4.1.18 (p. 215) | body sec nice-rcd + annex | thm:...-nice-rcd, thm:...-nice-rcd-failure, thm:...-split-set, thm:...-split-extension |

Findings recorded in the text:
- Durrett Theorem 1.1.11 is false with (iii) as printed. F_0 = (1{x1>=0}+1{x2>=0})/2 satisfies (i)-(iv) and has
  Delta_A F_0 = 0 for all finite rectangles. The corrected tail condition (iii*) asks F -> 0 as any single coordinate -> -inf.
  The proof builds the measure on boxes (-n,n]^d, so it never uses rectangles with infinite sides. p. 7 also prints
  'x_n uparrow -infinity' in (iii); it is read as uparrow infinity.
- Durrett thms 4.1.17/4.1.18 are false for 'nice' as printed (no Borel image). The counterexample uses a Lebesgue-split H
  (sqrt 2 coset construction, axiom of choice) and the extension P[B1,B2] = (lambda B1 + lambda B2)/2. S is two copies of
  [0,1], with X on the F_H copy and Y on the Borel copy. Positive bridge: existence holds if a Borel subset of phi(S)
  carries the law of phi(X). This counterexample is the classical type, but it is not attributed to Dieudonne or Doob,
  because those works are not held.
- Existing treatment found that the packet did not list: handbook/parts/p15/probability-spaces-and-random-variables-w02c-p15-001.tex
  (Example 1.1.12, Lebesgue on R^d via thm:p15-w02c-p15-001-lebesgue-rectangles). It is linked only through
  thm:p15-finite-product-measures, to avoid a dependency on another packet's label.

## Run 3 (resumed after usage limit)
The run 3 assessment lists only route gaps: every disputed item is written in an off-route w02c file (this packet's, or
w02c-p15-004, -008, -014). None of those files is input by the P15 drivers. Changes made:
- Duplicates removed, per A9/A14. These were def:...-nice, thm:...-nice-coding (annex too) and the proofboundary
  def:...-extension-limits. Each duplicated the treatment by w02c-p15-004, the owner of the countable-product unit:
  def:p15-w02c-p15-004-nice, -nice-coding, -durrett-2122, -extension-failure, -nice-extension (which gives the status of
  the 'trivial' claim) and sec:p15-w02c-p15-004-borel-cardinality (which carries a proof). sec:p15-w02c-p15-002-nice is
  now a short bridge to those labels.
- Lemmas split-set and split-extension removed (annex too), as duplicates of thm:p15-w02c-p15-008-thick-set and
  def:/thm:p15-w02c-p15-008-model, which belong to w02c-p15-008, the owner of the regular-conditional-laws unit.
  thm:...-nice-rcd-failure is reproved on ((0,1), F_H, P_H). Its no-r.c.d. step now reduces to part (i) of
  thm:p15-w02c-p15-008-no-rcp. The rcd-nonexistence warning links that model.
- The equal-in-distribution convention links def:p15-weak-law-convergence, the on-route one-line definition.
- Symbol intake: the split-set rows are dropped, the phi scope is moved, and an H_U/F_H/P_H reuse row is added.
- Patch file: added driver \input requests for body and annex, plus a C009 pointer at w02b-p15-008 line 90 to
  def:p15-w02c-p15-014-borel-notation.
- Locators re-verified in the held PDF this session: pp. 53-54 (PDF 61-62) and pp. 214-215 (PDF 222-223).

## Run 5 (w02ca r5)
The run 5 assessment repeats the route gaps for measurable-probability C001, C005, C006, C009, C010, C011, C014, C016,
C017, C018, C021, C024, C025 and regular-conditional-laws C005, C007, C011. Each item was checked against the text:
- In this packet's files: C006, C010, C011 (notation), C014, C016 (1)-(3), C017, C018 (equal in distribution), C021
  (Theorem A.1.5 for measures with a finite exhausting sequence), C025, rcl C005 (1)-(2), C007, C011.
- In w02c-p15-014 (owner of measurable-probability, not edited here): C001 (lines 191-252), C005 covering
  subadditivity (253-312), C009 (314-344), C011 target generality (346-360), Dynkin attribution for C021 (382-406),
  C018 point-mass reconciliation and C024 Example 1.2.8 (407-466). The run 4 return listed C005 and C024 as
  existing on-route text; they are now reported as blocked_policy on the 014 route.
- Locators re-verified in the held PDF this session (book p. n = PDF p. n+8): pp. 3, 10, 15, 17, 210, 214, 215, 457.
- Patch anchors for the driver inputs of 002, 004, 008 and 014 re-checked: all present.
No text changes were needed in this run.

## Run 6 (w02ca r6)
The run 6 assessment repeats route gaps for measurable-probability C006, C010, C011, C014, C016, C017, C018, C021, C025 and
regular-conditional-laws C005, C007, C011, C012. Each sub-item was checked against this packet's body file:
astragali (64-103), generator variants (115), C011 membership notation (340-377), C014 warning (378-392), C018 (393-418),
C016 domain D / order-topology Borel sets / P(lim exists)=1 (428-517), C017 Omega_o and X_infty = limsup (518-582),
C021 Theorem A.1.5 (593-625), C025 R^d measures (141-336) plus the boundary patch naming sec:p15-measure-extension,
rcl C011 Borel's paradox framing (662-725), rcl C012 Dieudonne/Doob/Faden and accumulation (734-783),
rcl C005/C007 nice-space status (785-874). All present; the only remaining change is the driver input (lead-owned).
- rcl C012 corrected in the return from written to blocked_policy (same route blocker as the other items).
- Locators re-verified in the held PDF this session (book p. n = PDF p. n+8): pp. 3, 10, 11, 15, 16, 17, 53, 210, 214, 215, 457.
- Patch anchors for 002, 004, 008, 014 re-checked: all present. No text changes in this run.

## Run 6 block 2
The block 2 gap list matches block 1 with more detail. One sub-item was absent from the text: C025's p. 11 remark
(Durrett, Theorem 1.2.2 proof: X(w) = sup{y : F(y) < w} is called the inverse F^{-1} though F need not be one-to-one
or onto; the scheme generates random variables on a computer from a uniform U, with F^{-1}(U) having distribution
function F). Added:
- body def:p15-w02c-p15-002-inverse-sampling (hbmethod: source form, inputs, procedure, side conditions, worked example
  with the exponential law of Example 1.2.4, p. 12, limitation) and thm:p15-w02c-p15-002-inverse-sampling (corollary:
  Q_F(U) has distribution function F for any uniform U with values in (0,1)), placed before the equal-in-distribution
  convention (body lines 394-453); annex proof annex:p15-w02c-p15-002-inverse-sampling (annex lines 340-367).
- symbol intake row for F^{-1} (Durrett p. 11), same meaning as Q_F and as the F^{-1} registered for
  sec:p15-weak-convergence-of-laws.
- patch #1 text extended to point at thm:p15-w02c-p15-002-inverse-sampling.
Locators read in the held PDF this session: pp. 11-12 (PDF 19-20).
No existing on-route treatment of the F^{-1}(U) sampling statement was found (grep for Q_F(U), F^{-1}(U), computer).

## Run 6 block 1 (w02ca r6, second pass)
Gap list: measurable-probability C001, C005, C009, C011, C015, C018, C021, C024 (drafted in w02c-p15-014's unrouted file)
and regular-conditional-laws C002, C004, C005, C007, C008.
- C021: added Durrett's attribution of Theorem A.1.4 to Dynkin, with its stated role (key to uniqueness of the extension;
  used many times in the book), to sec:p15-w02c-p15-002-sigma-finite-uniqueness (body 664-674). Read in the held PDF this
  session: p. 456 (PDF 464), pp. 457-458 (PDF 465-466). His pi-/lambda-system definitions on p. 456 match def:p15-pi-lambda.
- rcl C004/C007/C008: four replace patches for handbook/annex/p15/regular-conditional-laws.tex (entries 5-8 of
  work/waves/w02ca/patches/w02ca-p15-002.json). Each verifies the three conditions of def:p15-pi-lambda (whole space,
  proper differences, increasing unions) and the pi-system property of the generators, using only route labels. Same
  pattern as w02ca-p15-014's patches for uniform-integrability-and-conditional-limits.
- measurable-probability C001/C005/C009/C011/C015/C018/C024: not written here (A9/A14); the 014 file holds them and its
  driver input is filed by 014. rcl C002: 008's patch (first entry) supplies the pointer; C005 rests on routing this file,
  004's and 008's.
- Checks: unit-compile ok (17 overfull); check.py no findings on these files; find_fused_spaces clean (body, annex,
  patch texts).

## Run 6 block 2 (second pass)
Gap list: measurable-probability C001, C005, C006, C009, C010, C011, C012, C014, C015, C016, C017, C018, C020, C021,
C022, C024, C025. Each sub-item was checked against this packet's file and the w02c-p15-014 file. Two sub-items were
written nowhere and are added here:
- C018, the notation P o X^{-1} (Durrett sec. 1.2, Figure 1.3, p. 10): body def:p15-w02c-p15-002-composition-notation
  (lines 456-480), identified with the law P_X of def:p15-pushforward-law; X^{-1} read as the preimage set map.
- C024, Example 1.2.9 (dense discontinuities, p. 14): body sec:p15-w02c-p15-002-dense-jumps (508-568), example
  def:p15-w02c-p15-002-dense-jumps and lemma thm:p15-w02c-p15-002-dense-jumps (law sum alpha_i delta_{q_i} is a discrete
  probability measure with distribution function F; jump alpha_i at q_i, continuity at irrationals, discontinuity set Q,
  strict monotonicity); annex proof annex:p15-w02c-p15-002-dense-jumps (369-425). Durrett prints the normalization as
  sum alpha_1 = 1; read as sum alpha_i = 1 and said so in the example. The p. 13 lead-in ("can be quite wild") is
  paraphrased.
- Pointer patch: work/waves/w02ca/patches/w02ca-p15-002.json entry 9 (entries counted from 1; the last entry) (w02b-p15-002 Example 1.2.9 citation ->
  thm:p15-w02c-p15-002-dense-jumps).
- Symbol intake: rows for P o X^{-1}, q_i/alpha_i and 1_[theta,infinity).
- C012 (open-ray test) is thm:p15-w02c-p15-002-generator-variants (iii); C020 and C022 are in w02c-p15-014
  (thm:...-014-half-open-rectangles, def:...-014-point-mass-law); the return now lists them with the route blocker.
- Locators read in the held PDF this session: pp. 10-14 (PDF 18-22, text and rendered images of pp. 10 and 14).
- Checks: unit-compile ok (19 overfull); check.py --tree handbook shows no findings on this packet's files;
  find_fused_spaces clean.

## Run 6 block 3
Gap list: measurable-probability C001, C005, C006, C009, C010, C011, C012, C014, C015, C016, C017, C018, C020, C021, C023,
C024, C025. Each sub-item was checked against this packet's files and the w02c-p15-014 file. Two sub-items were written nowhere:
- C023, Durrett's justification of the distribution-function criterion by Theorem 1.1.4 ("In view of Theorem 1.1.4", p. 11;
  Theorem 1.1.4 itself on p. 3, PDF 11). Added a lead-in paragraph and lemma thm:p15-w02c-p15-002-equal-in-distribution
  (body 508-543), with the annex proof annex:p15-w02c-p15-002-equal-in-distribution (annex 369-404). The proof uses
  thm:p15-cdf-laws and the uniqueness clause of thm:p15-stieltjes-construction (the handbook's version of Theorem 1.1.4), and
  covers all four endpoint cases of I(a,b). The source does not write out the step from Theorem 1.1.4 to the criterion; the
  reader text says so.
- C025, the hypotheses: patch entry 1 is rewritten. It states the hypotheses of Theorem 1.1.4 (p. 3) and of Theorem 1.1.9
  (p. 5, PDF 13) and links thm:p15-semialgebra-extension and thm:p15-premeasure-extension as well as the earlier targets. It
  is compatible with w02ca-p15-014's insert_after on the next sentence ("The uniqueness theorem above supplies no such
  existence claim."), whose content it overlaps; the lead may keep either.
- Locators read in the held PDF this session: pp. 3, 4, 5, 6-9 (headings), 11, 12 (PDF 11-17, 19-20).
- Checks: unit-compile ok (19 overfull); check.py --tree handbook shows no findings on this packet's files;
  find_fused_spaces clean.

## Continuation
- State: every disputed item is in this packet's files, the owners' files or patch entries; what remains is the driver
  inputs (002, 004, 008, 014), the boundary patch (entry 1, rewritten in run 6 block 3), the annex replace patches
  (entries 5-8) and the Example 1.2.9 pointer (entry 9), all lead-owned.

## Run 6 block 1 (third pass)
Gap list identical to the second pass of block 1 (measurable-probability C001, C005, C009, C011, C015, C018, C021, C024;
regular-conditional-laws C002, C004, C005, C007, C008). Checked against the current text:
- C021: Dynkin attribution and stated role are in this packet's body (sec:p15-w02c-p15-002-sigma-finite-uniqueness,
  lines 791-801); the assessment read a text without it or counts only routed text. Also in w02c-p15-014 (448-485).
- C001, C005, C009, C011, C015, C018 (point-mass reconciliation), C024 (Example 1.2.8): in w02c-p15-014 (owner, A14),
  lines 196-262, 264-323, 325-355, 357-371, 373-440, 493-552. Not duplicated here.
- rcl C004, C007, C008: replace patches entries 5-8; anchors found once each in the host. rcl C002, C005: rest on the
  w02c-p15-008 and w02c-p15-004 routes and this file's route.
- All patch anchors of w02ca-p15-002, -004, -008, -014 re-checked: each found exactly once.
- Checks: unit-compile ok (19 overfull); check.py --tree handbook shows no findings on this packet's files;
  find_fused_spaces clean. No text changes in this pass.

# Edition 2026, P15 sections 158.3 and 158.4: integration supplements (packet w02ca-p15-005)

## Provenance

- Source opened in this session: `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`
  (Durrett, *Probability: Theory and Examples*, author version dated 11 January 2019; bib key
  `DurrettPTEAuthor2019`, already in `handbook/bib/handbook.bib`). Printed page = PDF page - 8.
  Pages rendered and read: printed 25 (text layer: Theorem 1.5.1 heading), 26, 28, 29, 30, 31, 33,
  35, 36, 37.
- Locators written, each seen on the page:
  - p. 25: Theorem 1.5.1 (Jensen for integrals). Theorem 1.5.2 (Hoelder), seen in the continuation run.
  - p. 26: Remark after Theorem 1.5.2 (direct Cauchy-Schwarz proof from 0 <= int (f + theta g)^2,
    quadratic with at most one real root, b^2 - 4ac <= 0); remark that on a finite measure space
    convergence in measure is weaker than a.e. convergence; Theorem 1.5.3 (bounded convergence,
    hypothesis in measure); Example 1.5.4 (f_n = 1/n on [0, n]). Re-read in the continuation run.
  - p. 35 re-read in the continuation run (Exercise 1.6.1 strict convexity; 1.6.2).
  - p. 28: Exercises 1.5.5, 1.5.8, 1.5.10.
  - p. 29: Theorem 1.6.2 (Jensen), the two-point illustration, the special cases |EX| <= E|X| and
    (EX)^2 <= E(X^2).
  - p. 30: Figure 1.6 (g(x) = x^2 - 3x + 3, P(X=1) = P(X=3) = 1/2), the Remark and display (1.6.1).
  - p. 31: Theorem 1.6.8.
  - p. 33: displays (1.6.2), (1.6.3).
  - p. 35: Exercises 1.6.1, 1.6.2, 1.6.3.
  - p. 36: Exercises 1.6.4, 1.6.5, 1.6.6, 1.6.7, 1.6.9 and the start of 1.6.10.
  - p. 37: the rest of 1.6.10 (three displays and the parity rule), 1.6.12, 1.6.13, 1.6.14.
- Notation: the source's E, P, var are written \mathbb E, \mathbb P, \operatorname{Var} to match
  the chapter being extended (`sec:p15-integration-expectation`); the body says so once.
  The indefinite integral keeps the source's \int_{[a,x]} f(y) dy.

## Choices recorded

- Exercise 1.6.4(i) is stated for a > 0, b > 0 (the source's a > b > 0 is included); this is
  needed because part (ii) with a <= sigma uses b = sigma^2/a >= a.
- Exercise 1.6.6 is stated as (EY)^2 <= EY^2 P(Y > 0) for all Y >= 0 with EY^2 < infinity, with
  the quotient form when EY^2 > 0; when EY^2 = 0 the source's quotient has no value.
- Exercise 1.5.8: proved continuity on [a, b], which contains the source's (a, b).
- Exercise 1.6.1: stated as an equivalence; the reverse direction is immediate.
- Exercise 1.6.12: equality clause added (via 1.6.1 and strict convexity of exp).
- Exercise 1.6.2: the R^n supporting affine function is proved from scratch (continuity by a cube
  bound; sublinear directional derivative; one-step finite-dimensional extension of a linear
  functional below it), following the source's instruction to imitate the supporting-line proof.
- The typewriter sequence is not re-proved; `thm:p15-w02b-p15-013-countermodels` (2) proves it.

## Unit ownership note (for the lead)

The packet lists both units (ED26-P15-CH-integration-expectation, ED26-P15-CH-radon-nikodym)
under `readonly_units`, owner w02c-p15-001 (packet w02ca-p15-001). The block-0 confirmation
nevertheless routed seven integration-expectation disputes to this packet as writable gaps, and
the task text directed closing them. They were written here, in this packet's own new files,
after checking that the owner's in-progress file
(`handbook/parts/p15/probability-spaces-and-random-variables-w02c-p15-001.tex`, read at 11:20)
treats interval-integral notation and change of variables and does not state any of these items.
If the owner later writes any of them, the lead should keep one treatment.

## Continuation

- First run of block 1: body and annex covering C004 (Ex 1.5.5, 1.6.13), C005 (Ex 1.5.10), C009
  (finite-measure a.e. => measure, with both failures), C014 (two-point illustration, Figure 1.6,
  |EX| <= E|X|, (EX)^2 <= EX^2, Ex 1.6.1, 1.6.2, 1.6.12), C017 (displays (1.6.1), (1.6.3); Ex
  1.6.3-1.6.6), C019 (Ex 1.6.7), and Exercises 1.5.8, 1.6.9, 1.6.10, 1.6.14.
- Continuation run (after the usage limit), closing the independent assessment's disputes:
  - C012: new section sec:p15-w02c-p15-005-cauchy-schwarz, thm:p15-w02c-p15-005-cauchy-schwarz with
    annex:p15-w02c-p15-005-cauchy-schwarz (Durrett's p. 26 Remark: quadratic in theta, discriminant;
    finiteness making the coefficients real; degenerate case int g^2 = 0; infinite-norm cases).
  - C009: the theorem now names def:p15-lp-convergence; new thm:p15-w02c-p15-005-ae-bounded (a.e.
    form of Durrett's Theorem 1.5.3 via part (1) and thm:p15-dominated-bounded-convergence (2)) with
    annex proof; Example 1.5.4 related to h_n of def:p15-convergence-failures.
  - C013: paragraph after def:p15-w02c-p15-005-convex-rn tying strict convexity (Ex 1.6.1) and
    R^n convexity (Ex 1.6.2) to the definition and to the continuity / supporting-affine lemma.
  - C016 and notations (a)-(b) of p. 23: written by the unit owner (packet w02ca-p15-001) in
    probability-spaces-and-random-variables-w02c-p15-001.tex (def:p15-w02c-p15-001-change-of-variables-name,
    thm:p15-w02c-p15-001-change-of-variables, def:p15-w02c-p15-001-dx-notation; its patch request
    work/waves/w02ca/patches/w02ca-p15-001.json). Not duplicated here.
  - Routing: patch request work/waves/w02ca/patches/w02ca-p15-005.json inserts the two input lines
    after the w02b-p15-005 inputs in handbook/parts/p15.tex and handbook/annex/p15.tex.
- unit-compile ok; check.py --tree shows no finding in these files; find_fused_spaces clean.
- Remaining: the lead applies the routing patch; symbol intake merge.
- Run r4 (2026-10-10): every Durrett locator in both files re-verified in this session against the
  held PDF (printed page = PDF page - 8; pp. 18, 25, 26, 28, 29, 30, 31, 33, 35, 36, 37). Fixed three
  stray double-backslash line breaks in the body (Figure 1.6 example; Ex. 1.6.5 statement). The
  independent assessment found every listed item present in these files; its only remaining gap is
  that the files are off the route. Reported C004, C007, C009, C012, C013, C014, C017, C019 and
  Ex. 1.5.8, 1.6.9, 1.6.10, 1.6.14 as blocked_policy on the routing patch
  work/waves/w02ca/patches/w02ca-p15-005.json (anchors re-checked against the current drivers).
  Ex. 1.5.10 is now reported under C007 (Linearity), where the assessment places it.
  C016 and the p. 23 notations remain with the unit owner w02ca-p15-001.
- unit-compile ok; check.py --tree: no finding in these files; find_fused_spaces clean.
- Remaining: the lead applies the routing patch; symbol intake merge.
- Run r5 (2026-10-10): every Durrett locator re-verified against the held PDF by pdftotext
  (printed page = PDF page - 8; pp. 18, 25, 26, 28, 29, 30, 31, 33, 35, 36, 37). The assessment's
  disputes are again route-only for this packet's files. Duplicate resolved in favour of the unit
  owner (w02ca-p15-001, A9/A14): removed sec:p15-w02c-p15-005-cauchy-schwarz with its theorem and
  annex proof, and removed the (1.6.1) statement from thm:p15-w02c-p15-005-chebyshev-displays, which
  now states only display (1.6.3), Var(X) <= EX^2 with equality iff EX = 0 (from (1.6.2), p. 33).
  The body links thm:p15-w02c-p15-001-cauchy-schwarz, def:p15-w02c-p15-001-chebyshev-names and
  thm:p15-w02c-p15-001-chebyshev-square. Removed the two symbol-intake rows (theta; a, b, c, D, q)
  of the deleted proof. Shortened two section titles (overfull). Patch request 3 added: pointer at
  the end of def:p15-integration-next-boundary to this chapter.
- unit-compile ok (overfull 10); check.py --tree: no finding in these files; find_fused_spaces clean.
- Remaining: the lead applies the routing patch (requests 1-2) and request 3; symbol intake merge;
  route the owner's chapter with this one (cross-references both ways).
- Run r6 (2026-10-11): the assessment repeats C009, C012, C014, C016, C017 as route-only disputes.
  Re-verified by pdftotext against the held PDF: p. 26 (Remark on Cauchy-Schwarz; finite-measure
  remark; Thm 1.5.3; Ex. 1.5.4), p. 29 (Thm 1.6.2; special cases), p. 30 (Figure 1.6; Remark;
  (1.6.1)), p. 33 ((1.6.2), (1.6.3)), and the exercise pages 28, 35, 36, 37, with pp. 18, 25, 31.
  No text changed. Body items: C009 lines 118-170, C014 lines 172-302, C017 (1.6.3) lines 305-323
  of the body file; all present. C012, C016 and the (1.6.1)/naming part of C017 are in the owner's
  file probability-spaces-and-random-variables-w02c-p15-001.tex (lines 345-404, 589-667), which no
  patch request in work/waves/w02ca/patches/ routes into handbook/parts/p15.tex or
  handbook/annex/p15.tex; this chapter's links to the owner's labels resolve only once both files
  are routed. Patch anchors in w02ca-p15-005.json re-checked: each occurs once, none applied.
- unit-compile ok (overfull 10); check.py --tree: no finding in these files; find_fused_spaces clean.
- Remaining: the lead applies requests 1-3 of w02ca-p15-005.json and routes the owner's
  w02c-p15-001 body and annex files.
- Run r6 block 2 (2026-10-11): the assessment's disputes (C004, C005, C009, C012, C013, C014, C016,
  C017, C019, C020, source-extent residual) are all lead_owned routing gaps. No reader text changed.
  Return realigned: Ex. 1.5.10 now under C005 (the assessment's placement), C020 reported
  blocked_policy on routing of the owner's chapter (no routing patch request exists for
  probability-spaces-and-random-variables-w02c-p15-001). Durrett p. 26 re-read by pdftotext.
- unit-compile ok (overfull 10); check.py --tree: no finding in these files; find_fused_spaces clean;
  patch anchors in w02ca-p15-005.json each occur once, unapplied.
- Remaining: the lead applies requests 1-3 of w02ca-p15-005.json and routes the owner's
  w02c-p15-001 body and annex files.
- Run r6 block 3 (2026-10-11): the assessment's disputes (C004, C009, C012, C014, C016, C017, C020,
  source-extent items: p. 23-24 notations (a)-(d); Ex. 1.5.8, 1.5.10, 1.6.5-1.6.7, 1.6.9-1.6.12,
  1.6.14; route status) were each checked against the two unrouted files: every item is present,
  in this packet's chapter or in the owner's (w02ca-p15-001) chapter (notations (a)-(d) at owner
  body 67-165; Ex. 1.6.11 and Example 1.6.12 at owner body 803-947). All cross-file \cref labels
  between the two chapters resolve. The gap is routing only. Patch requests 1-2 of
  work/waves/w02ca/patches/w02ca-p15-005.json now route both chapters (owner first) at the same
  anchor, since no other patch request routes the owner's chapter. Durrett pp. 18, 25, 26, 28-31,
  33, 35-37 re-read by pdftotext. No reader text changed.
- unit-compile ok (overfull 10); check.py --tree: no finding in these files; find_fused_spaces clean.
- Remaining: the lead applies requests 1-3 of w02ca-p15-005.json.
- Run r6 block 1 rerun (2026-10-12): Durrett p. 30 re-read by pdftotext (PDF page 38): Theorem 1.6.7
  (dominated convergence) and the sentence naming its constant-Y case the bounded convergence
  theorem. That name was absent from both unrouted chapters; added as a paragraph in
  sec:p15-w02c-p15-005-modes (body lines 154-166), tied to thm:p15-dominated-bounded-convergence (1),
  thm:p15-w02c-p15-005-ae-bounded and Durrett's Theorem 1.5.3. Every other disputed item re-checked
  present in this chapter or the owner's (w02ca-p15-001) chapter; the gap is routing only.
- unit-compile ok (overfull 10); check.py --tree: no finding in these files; find_fused_spaces clean;
  patch anchors in w02ca-p15-005.json each occur once, unapplied.
- Remaining: the lead applies requests 1-3 of w02ca-p15-005.json.
- Run r6 block 2 rerun (2026-10-12): Durrett printed pp. 18, 25, 26, 28-31, 33, 35-37 re-read by
  pdftotext; every locator found at its page. The assessment's disputes (C004, C005, C006 notations
  (a)-(d), C009, C012, C014, C016, C017, C019, C020) re-checked: each item present in this chapter or
  the owner's (w02ca-p15-001) chapter (owner body 73-347 notations; 352-580 change of variables and
  four-step method; 614-672 Cauchy-Schwarz; 677-741 Chebyshev names and (1.6.1); 806-950 Ex. 1.6.11
  and Bernoulli law; 996-1117 Jensen hypotheses). No reader text changed. Return: C006 now
  blocked_policy on routing; C014, C016, C020 locations updated.
- unit-compile ok (overfull 10); check.py --tree: no finding in these files; find_fused_spaces clean;
  patch anchors in w02ca-p15-005.json each occur once, unapplied.
- Remaining: the lead applies requests 1-3 of w02ca-p15-005.json.
- Run r6 block 3 rerun (2026-10-12): Durrett printed pp. 23, 24, 26, 28-30, 32, 33, 35-37 re-read by
  pdftotext; every disputed locator found at its page (incl. the constant-Y bounded convergence name,
  p. 30, and the change of variables Remark, p. 32). Disputes C004, C009, C010, C012, C014, C016, C017,
  C019, C020 re-checked: each item present in this chapter or the owner's (w02ca-p15-001) chapter.
  No reader text changed. Gap is routing only.
- unit-compile ok (overfull 10); check.py --tree: no finding in these files; find_fused_spaces clean;
  patch anchors in w02ca-p15-005.json each occur once, unapplied.
- Remaining: the lead applies requests 1-3 of work/waves/w02ca/patches/w02ca-p15-005.json.
- Run r6 block 1 rerun 2 (2026-10-13): Durrett printed pp. 18, 23-26, 28-33, 35-37 re-read by pdftotext
  (PDF page = printed + 8); every disputed locator found at its page (Ex. 1.5.5, 1.5.8, 1.5.10; p. 26
  quadratic remark, finite-measure remark, Thm 1.5.3; Thm 1.6.2; Figure 1.6, (1.6.1), bounded
  convergence name; Thm 1.6.8; Thm 1.6.9 change of variables formula, p. 32; (1.6.3); Ex. 1.6.1-1.6.4,
  1.6.7, 1.6.9, 1.6.10, 1.6.12-1.6.14). Disputes C004, C009, C010, C012, C013, C014, C016, C017, C019
  and the pp. 18-37 extent item re-checked: each item present in this chapter or the owner's
  (w02ca-p15-001) chapter. Drivers re-read: neither handbook/parts/p15.tex nor handbook/annex/p15.tex
  inputs either chapter. No reader text changed. Gap is routing only.
- unit-compile ok (overfull 10); check.py --tree: no finding in these files; find_fused_spaces clean;
  patch anchors in w02ca-p15-005.json each occur once, unapplied.
- Remaining: the lead applies requests 1-3 of work/waves/w02ca/patches/w02ca-p15-005.json.
- Run r6 block 2 rerun 2 (2026-10-13): both chapters are now routed (handbook/parts/p15.tex lines 46,
  49; handbook/annex/p15.tex lines 45, 48). Durrett printed pp. 18, 26, 30, 31 re-read by pdftotext
  (PDF pp. 26, 34, 38, 39). Closed the three assessment disputes:
  - C001: body lines 51-63, Durrett's sec. 1.4 justification (p. 18): infinite measures sometimes
    needed, general sigma-finite development no harder; tied to this chapter's uses of Lebesgue
    measure on R and to thm:p15-w02c-p15-005-ae-bounded with mu(Omega) infinite.
  - C010: body lines 166-180, the second half of Durrett's p. 26 sentence (Theorem 1.5.3 is easier to
    prove under convergence in measure), with the reason read off his proof (only mu(B_n) -> 0 used).
  - C019: body lines 445-470, Durrett's p. 30 framing of Theorem 1.6.8 (another integration-to-the-
    limit result needed later; g = |x|^p, p > 1, h = x perhaps the most important case), new
    corollary thm:p15-w02c-p15-005-moment-power with annex proof annex:p15-w02c-p15-005-moment-power
    (annex lines 506-535), and the p = 1 failure Y_n = n 1_(0,1/n).
  - G1 guard: spec/research/edition-2026-authoring-batch-intake-13.json shows no diff against HEAD
    (git status clean for it); not touched in this run.
- unit-compile ok (overfull 10); find_fused_spaces clean.

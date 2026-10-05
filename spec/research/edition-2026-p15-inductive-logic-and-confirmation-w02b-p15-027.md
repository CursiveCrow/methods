# w02b-p15-027: Popper chapters 8 and 9 with later notes (section 164.4, gap MP-0(b))

Observed 2026-10-04. Packet work/waves/w02b/packets/w02b-p15-027.json (sections 164.3, 164.4; label tag p15-w02b-p15-027).

## Source opened in this session

- source/references/p15-popper-hd/popper-2002-elib2005-ui-ocw.pdf (Popper, The Logic of Scientific Discovery, Routledge Classics 2002, e-library 2005; held, listed in held-sources.json). Text extracted with PyMuPDF (Greek letters and primes preserved) and pdftotext; pages with lost glyphs checked as rendered images (physical 174 top, 175, 181, 242, 317, 318, 320).
- Physical-to-printed offset in chapters 8-9 and appendices ii-iii: printed = physical - 29.
- Read completely: translators' note (phys 13); contents (phys 7-12); chapter 8, sections 47-72 with all footnotes (phys 162-237, printed 133-208); chapter 9 opening and sections 73-78 with all footnotes (phys 238-276, printed 209-247); appendix ii (phys 315-318, printed 286-289); appendix iii (phys 319-321, printed 290-292); the first page of appendix iv (phys 322) only.
- Not read: appendix iv beyond its first page, appendices v-vii, new appendices *i-*xii, the Gillies pointer target at printed p. 443, the Postscript. None of these is reconstructed, and the text says so.
- Notation recovered from images: complement is an overbar; the class sum Sigma is placed before class names; sigma-prime marks the successor of an n-tuple; the uncertainty relation uses >= h/4pi; the generating-period lower bound is 2^{n+1}; the starred counterexample in note 4 to section 53 reads alphaF''(gamma) != betaF''(gamma).

## Placement

- The task named the editable host handbook/parts/p15/popper-hypothetico-deductive-reasoning.tex. The material was first written there, but tools/waves.py unit-compile builds only the owned body/annex pair, so the new sections were moved into the owned chapter file handbook/parts/p15/inductive-logic-and-confirmation-w02b-p15-027.tex (chapter label sec:p15-w02b-p15-027). The host keeps two edits: its opening paragraph cross-references the new chapter, and its proofboundary def:p15-popper-source-boundary replaces the sentence saying the probability and quantum treatments are not reconstructed with an exact list of what remains unreconstructed.
- Proposed driver placement (lead executes): body input of parts/p15/inductive-logic-and-confirmation-w02b-p15-027 immediately after parts/p15/popper-hypothetico-deductive-reasoning (handbook/parts/p15.tex line 87); annex input of annex/p15/inductive-logic-and-confirmation-w02b-p15-027 immediately after annex/p15/popper-hypothetico-deductive-reasoning (handbook/annex/p15.tex line 85). The packet default (after goodman-entrenchment, lines 93 and 91) also works; adjacency is preferred because the chapter opens as a continuation of the Popper chapter.

## What was written

Body (owned chapter, 901 lines): finite frequency calculus (Definition 1; appendix ii formulas 1, 1', 1s, 2, 2s, 3, 4s; a handbook subclass item); the five-button counterexample of starred note 4 to section 53; sections 53-55 (independence, ordinal and neighbourhood selection, n-freedom, Schiff remark, periods A-D); a cyclic formalization with an exact first binomial formula (appendix iii) and the 2^{n+1} property; sections 56-64 (segments, mathematical and empirical sequences, frequency hypotheses, Kamke objection, absolute freedom, the section 59 definition, three binomial formulas with Popper's two-step argument kept as his sketch, Bernoulli's theorem with a Chebyshev bound, section 62, the von Mises square-root example, middle frequencies with a proof that they form [liminf, limsup], the randomness, uniqueness and convergence requirements, the finitude requirement); sections 65-70 (decidability, finite records cannot contradict, the all-and-some note *2, logical form, speculative metaphysics, the section 68 methodological rule, law and chance, macro from micro); sections 71-72 (formally singular probability, reference-class change, range theory with a counterexample showing that the strict inequality needs more than the failure of the universal law); chapter 9 (four announced conclusions, sections 73-78, scatter relations, physical selection and measurement, pure case, inversion of Heisenberg's programme, the mirror example, the hypothesis of linkage, the withdrawn section 77 experiment as a warning, indeterminist metaphysics); a dated-layer table of 15 starred-note changes.

Annex (owned, 363 lines): seven complete proofs (finite calculus; five buttons; cyclic counts, Schiff reduction, binomial formula, de Bruijn converse and the four period window lists; binomial Chebyshev bound and three corollaries; middle frequencies; altering a finite initial record and bounded/unbounded existentials; reference classes).

Handbook additions, marked in the text: the cyclic reading of finite periods, the counts c_a, the S_tau selection notation, item 7 of the finite calculus, item 4 of the binomial theorem, the Chebyshev corollaries, the range counterexample, and the reading of "triple symmetry".

## Open items (not supplied)

- Formula (3) of section 60 (sequences of adjoining segments are chance-like) and the derivation of Bernoulli's theorem from the section 64 requirements without convergence: Popper gives a sketch and a claim; no proof is written.
- Appendix iv constructions (existence of absolutely free sequences; a sequence with one probability and no frequency limit; several absolutely free middle frequencies): not read beyond the first page; item 1 of thm:p15-w02b-p15-027-finite-records is stated conditionally on existence.
- Appendices v-vii (two-slit objection, non-predictive measurement, imaginary experiment): not read or reconstructed.
- New appendices *ii-*xii, the Postscript, and the Gillies solution (printed p. 443): not reconstructed.
- Popper's characteristic-value analysis of Delta p in section 68: not proved; a Chebyshev illustration is given and labelled as the handbook's.
- Musgrave 2011 (Handbook of the History of Logic 10, pp. 205-234) and Forster 2011 (same volume, pp. 93-115): bodies not held. The held paths are Milton 2011 (a different chapter, 41 pp.) and a Fordham renderer for HHL volume 2 (a different volume). All six packet components remain blocked_source.

## Existing treatments found

- sec:p15-reichenbach-normality (Reichenbach on after-effect and normal sequences): cross-referenced.
- sec:p15-feller-generalized-weak-law (general weak law): cross-referenced, not duplicated.
- thm:p15-popper-coin and sec:p15-popper-corroboration in the host: cross-referenced.
Only the host file itself was in the packet's existing list.

## Checks

- python -B tools/waves.py unit-compile work/waves/w02b/packets/w02b-p15-027.json: ok, 0 overfull.
- python -B tools/find_fused_spaces.py on the three edited .tex files: no hits.
- python -B tools/check.py --tree handbook: no finding mentions the edited files (the new owned files are not yet on the driver route).
- No new bibliography keys (Popper2002LogicDiscoveryUI is already in handbook.bib), so no intake .bib was written.

## Second pass (2026-10-04): appendix iv, section 68, appendices v-vii, *vi, 1972 addendum

Pages opened this pass (physical = printed + 29 throughout the appendices): appendix iv complete (phys 322-325, printed 293-296; images checked for x <= n+1 and the tower formula m = 2^2^...); appendix v (phys 326-329); appendix vi (phys 330-333); appendix vii (phys 334-337); note to new appendices (phys 338-340); appendix *vi complete (phys 398-402; image checked for the Sigma sums in point 14); section 68 pp. 194-196 (phys 223-225); section 65 note *1 (phys 212); appendix *ix end and Addendum 1972 (phys 466-468, printed 437-439); name index entry Gillies (phys 519, printed 490); section 77 setup (phys 268-270, printed 239-241).

Findings:
- The 1972 pointer in note *1 to section 65 says "p. 443"; in this printing the matching text is the appendix *ix Addendum 1972, pp. 438-439, and the name index lists Gillies at 183n, 438. The addendum names Gillies 1971 (BJPS 22, 231-261) and gives no content of the rule. Gillies 1971 is not held.
- Popper's note *1 rule (start 1^x, prefer 0) verified by script for x = 2..5; x = 4 reproduces his printed 1111000010011010; the unique rotation beginning with 0110 is his (2) 0110101111000010.
- Popper's nested construction: proved here that prefixes of length n_i are shortest periods and that frequencies converge along the lengths n_i. Convergence at intermediate lengths is not implied by the de Bruijn property (fewer than 2^K distinct K-windows do not bound the frequency of ones); left as Popper's assertion (also asserted in *vi point 10).
- Handbook construction (repeated de Bruijn blocks D_K^{2^K}) proves existence of an absolutely free alternative with p = 1/2; this removes the existence condition of finite-records item 1 for p = 1/2 only.
- Section 68 characteristic Delta p: handbook theorem via the Hoeffding binomial bound (derived directly; cross-referenced to thm:p15-conc-common-range and thm:p15-conc-exponential, existing treatments not in the packet list).

Written this pass: body section sec:p15-w02b-p15-027-models (thm greedy-rule, shortest-sequence, free-exists; constructions (b), (c) and the dice note as Popper's sketches; appendix *vi points 1-14); thm:p15-w02b-p15-027-characteristic in section 68 discussion; subsection sec:p15-w02b-p15-027-quantum-appendices (appendices v, vi, vii with formulas (1)-(8) and the withdrawing notes); Gillies addendum paragraph in sec:p15-w02b-p15-027-later-notes. Annex: four new annexitems (greedy-rule, shortest-sequence, free-exists, characteristic). Host proofboundary def:p15-popper-source-boundary rewritten to the new exact remainder. Eight symbol-intake rows added.

Still not supplied (Popper 2002 held, not yet read or reconstructed): appendices *ii, *iii, *iv, *v (formal calculus, postulates and derivations), *vii, *viii, *ix (corroboration and statistical tests, including point 8 ff. of the Third Note that supersedes section 68), *x, *xi (imaginary experiments), *xii (Einstein letter); convergence of the nested sequence at all lengths; constructions (b), (c) and p != 1/2 existence (Popper's sketches only); formula (3) of section 60. Gillies 1971 not held. Musgrave 2011 and Forster 2011 not held.

## Third pass (2026-10-04): G14 fix; appendices *ii, *iii, *iv (elementary system)

G14: the workflow word guard matches "wave"/"waves" in physics usage. Rephrased in the owned body: quantized fields (sec. 9 opening), Schrödinger equation (sec. 74), localized psi-function packet (sec. 75, 76 notes), coherent spherical radiation and corpuscular-undulatory dualism (appendix v). Host: "review" (Hermann 1935) -> "critical notice" at three places; "admitted test" -> "test in \mathcal B" in thm:p15-popper-falsifier-order.

Pages opened (physical = printed + 29): introductory note to the new appendices (phys 339-340, printed 310-311); appendix *ii complete (phys 348-353, printed 319-324; images checked for the lost >= glyphs in A1-A3, B1, B3 and for the overlined tautology in Df1 and p(x)=p(x, overline{x xbar})); appendix *iii complete (phys 354-357, printed 325-328); appendix *iv phys 358-378 (printed 329-349; images checked for B1 <=, AP >=, the four-element matrices, C (i)-(ii), the symmetric-system rules and p(b)=p(b, overline{a abar})). Text extraction drops >= and <= silently; every inequality written was read from an image.

Verified by script (scratchpad models.py): the trivial and four-element models satisfy A1-C; the six independence models each violate exactly the named axiom; (E) holds in the four-element model; (0) holds in the trivial model and fails in the four-element one.

Written: body sec:p15-w02b-p15-027-formal-calculus (lines 726-1177): def absolute-system, thm absolute-equalities (handbook derivation), Df1/Df2 and note *2 reversal, appendix *iii with example die-no-six and formulas (1)-(3), appendix *iv features, (a)-(h), thm association (Popper's note 3), symmetric-system rules (stated, not derived), def relative-system (postulates 1-4, A1-C, AP), alternative system A3'-C', B+/C+, thm cplus-reflexivity (note 8), comments A2+/B3/B3-/B3+, C (i)-(ii), def ranked-models (handbook), thm consistency (handbook unification of Popper's trivial and four-element models; incompleteness via (0)), second example with its gap noted, dyadic model (Popper's assertion), thm independence (six models), note 10, non-operational independence summary, (*). Annex: five annexitems (lines 612-810).

Still not supplied: appendix *iv remainder (three-axiom system A1, B, C+ and the formulas BD, CD; the S' matrix; Borel-field extension and the p. 367 addendum); the second B1 and B2 models (matrices not read from image); the derivation of B1 from A4' and B1' (note 7, needs images for <=); appendix *v derivations (including (g), (h), formula 75, the symmetric-system rules, Boolean algebra from (*)); the dyadic model's limit existence; appendices *vii, *viii, *ix, *x, *xi, *xii (not yet read in any pass). Musgrave 2011, Forster 2011, Gillies 1971 not held.

## Fourth pass (2026-10-04): formula (3), Bernoulli under section 64, appendix iv existence claims

Pages opened this pass (physical = printed + 29): section 60 complete (phys 193-197, printed 164-168, including notes *1-*3 and 1-3); section 61 opening (phys 197-199); section 64 complete with notes 1-7, *1-*4 (phys 205-209, printed 176-180); section 58 definition of normal ordinal selection (elements k, n+k, 2n+k) from the same extract.

Written (owned body): def:p15-w02b-p15-027-free-along (handbook reading: p free along a sequence of lengths; with all lengths it is absolute freedom); thm:p15-w02b-p15-027-freedom-windows (absolute freedom <-> binomial window frequencies, the converse for 0<p<1); thm:p15-w02b-p15-027-aligned-windows (windows survive normal ordinal selection; variance count, no characteristic-distance argument); thm:p15-w02b-p15-027-third-binomial (formulas (3) and (4), freedom of adjoining sequences for 0<p<1, Bernoulli, insensitivity to normal ordinal, pure neighbourhood and combined selections, which is the closing claim of sec. 60); thm:p15-w02b-p15-027-bernoulli-middle (Bernoulli from the requirement of randomness read with common lengths; uniqueness unused); thm:p15-w02b-p15-027-concatenation and thm:p15-w02b-p15-027-constructions (existence for every 0<p<1; construction (b) with unique free middle frequency 1/2 and no limit; construction (c) with two free middle frequencies; a sequence meeting both sec. 64 requirements whose fair-sample frequency has middle frequency 0 for every n). Finite-records item 1 now unconditional (constant sequences for p=0,1). Annex: six annexitems (fwin, aligned-windows, third-binomial, bmid, concatenation, constructions). Host proofboundary updated.

Handbook-versus-source: the common-length reading is the handbook's, motivated by Popper's note 3 to sec. 64 (stricter independence needed); constructions (b), (c) are realized by the handbook's concatenations, not by Popper's search-and-rearrange procedure.

Computation (scratchpad nest.py): Popper's nested sequence, third stage (rotation of the order-16 rule period beginning with 0110101111000010): 729 ones in the first 1710 terms (0.426); exactly 1/2 at 16 and 65536.

Still not supplied after this pass:
- Convergence at every length for Popper's own nested sequence (appendix iv (a), *vi point 10): neither proof nor counterexample.
- Constructions (b), (c) by Popper's own procedure (search-and-rearrange with nested periods): depends on the same open intermediate-length question.
- Freedom of the adjoining sequences for p = 0 or 1 (the F in (3)); frequency parts hold.
- Whether the looser reading of sec. 64 note 4 (each selection approaching p along its own lengths) yields Bernoulli.
- Item 3 of the gap list: dyadic-fraction model of appendix *iv (limit existence, axioms), S' four-element system, Borel-field extension, improved BD/CD of the addendum, appendix *v derivations: not started this pass.
- Item 4: appendices *vii-*xii beyond the points used: not started.
- Gillies 1971, Musgrave 2011, Forster 2011 not held.

## Continuation

State at return (fourth pass). Next steps in order: appendix *iv remainder (dyadic model limit and axioms; S' matrix from page images; Borel-field extension; addendum BD/CD; second B1/B2 models; derivation of B1 from A4' and B1'), then appendix *v derivations (phys ~379-397), then appendices *vii, *viii, *ix (corroboration; Third Note point 8 ff. superseding sec. 68), *x, *xi, *xii. Check every inequality against page images: the extract drops >= and <=. Open mathematical items: convergence of Popper's nested sequence at every length; sec. 64 under the looser reading; freedom of adjoining sequences for p = 0, 1. Acquisition needed: Gillies 1971 BJPS 22:231-261; Musgrave 2011 and Forster 2011 (HHL 10).

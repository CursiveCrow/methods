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

## Continuation

State at return: written as above. Next steps if more time is allocated: read appendix iv completely and reconstruct its constructions (removes the conditional in finite-records item 1 and supports the section 64 consistency claim); read appendices v-vii for the quantum examples; then appendix *vi (shortest random-like sequences) and *ix (statistical tests) for the later positions cited in the notes to sections 57, 65 and 68. The Musgrave and Forster chapters need acquisition before any of the packet's components can be written.

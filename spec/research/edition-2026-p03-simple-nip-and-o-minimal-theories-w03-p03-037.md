# P3 34.9 -- Real closed fields as the principal worked example (packet w03a-p03-037)

Owned files:

- handbook/parts/p03/simple-nip-and-o-minimal-theories-w03-p03-037.tex (body, `\chapter`, toc tag `%% toc: P3 34 34.9`)
- handbook/annex/p03/simple-nip-and-o-minimal-theories-w03-p03-037.tex (annex)
- handbook/bib/intake-p03-simple-nip-and-o-minimal-theories-w03-p03-037.bib
- handbook/registry/symbols-intake-p03-simple-nip-and-o-minimal-theories-w03-p03-037.csv

## Sources read (block 1 first run; Simon pp. 13--17 re-opened in the block 1 continuation run)

- Held: Simon, *A Guide to NIP Theories*, author-typeset manuscript dated 16 October 2015
  (source/references/acq-r1-ACQ-2026-10-0513/simon-2015-guide-to-nip-theories.pdf).
  Read pp. 13--17 (Definition 2.1, Lemma 2.5 p. 14, Lemma 2.7 p. 15, Proposition 2.8 p. 16,
  Proposition 2.11 pp. 16--17, Example 2.12 p. 17). The handbook key `Simon2015` is the CUP
  printing, which was not read; the intake key `Simon2015GuideManuscript` identifies the version read.
- Online (open archive copy of the author's page, which now returns HTTP 403):
  - Coste, *An Introduction to Semialgebraic Geometry*, dated October 2002,
    https://web.archive.org/web/20210131225032/https://perso.univ-rennes1.fr/michel.coste/polyens/SAG.pdf
   . Read pp. 11--12 (Section 1.3.1, Theorem 1.9, fixed degrees and truncation,
    quadratic example; Lemma 1.10).
  - Coste, *An Introduction to O-minimal Geometry*, dated November 1999,
    https://web.archive.org/web/20201111232331/https://perso.univ-rennes1.fr/michel.coste/polyens/OMIN.pdf
   . Read pp. 5--11 (semialgebraic sets p. 5; Wilkie remark p. 6;
    equivalent conditions for real closed fields p. 8; real algebraic numbers and semialgebraic sets
    over a real closed field p. 9; Definition 1.4 p. 10; Exercise 1.9 p. 11).

## Provenance of the treatment

- The axiomatization of RCF by the polynomial intermediate-value scheme is the second condition
  in Coste 1999 p. 8; Coste states the equivalence with the square-root/odd-degree condition and
  with algebraic closedness of R[sqrt(-1)] without proof (pointing to BCR). The chapter uses the
  intermediate-value form as the definition, so no step depends on that unproved equivalence.
- The elimination proof is written here in the sign-table form (Hormander-style). The reduction to
  fixed degrees by truncation follows Coste 2002 p. 11; the sign-table bookkeeping, the interval
  lemma and the pseudo-remainder step are written from scratch and fully proved in the annex.
- Monotonicity and cell decomposition: the general theorems remain the cited statements at
  classification-theory.tex (thm:p03-ominimal-monotonicity, thm:p03-ominimal-cell-decomposition),
  whose proofs belong to packet w03-p03-036 (readonly units N-a-009-01..03). This chapter
  verifies concrete semialgebraic instances directly.
- Theory-level NIP of RCF uses Simon's Lemma 2.5 and Proposition 2.11 (cited); the one-variable
  NIP bound is proved here from elimination.

## Continuation

- Written (first run): body and annex for RCF definitions, elementary analysis lemmas, sign tables,
  uniform sign-table theorem, QE, completeness, definable = semialgebraic, o-minimality of every
  model, monotonicity and cell-decomposition worked instances, unstable (order property),
  one-variable NIP bound, ring-language failure of QE, expansion boundary (R with a predicate for Z).
- Written (continuation run): theory-level NIP for RCF is now proved in the annex, not cited.
  Route: QE reduces every formula to a Boolean combination of sign conditions on integer
  polynomials; each positivity family is a family of positivity sets of a finite-dimensional
  function space (span of the x-monomials), which shatters no (N+1)-set by a linear-algebra
  (Radon/Dudley-type) argument proved over any ordered field; the trace-counting lemma
  (Sauer-Shelah, proved via the Pajor-style claim |G| <= #shattered subsets) gives a polynomial
  trace bound (n+1)^d; (n+1)^d < 2^n for n >= 2^(d+1)(d+1)!. New labels:
  def:p03-w03-p03-037-trace, thm:p03-w03-p03-037-linear-shatter,
  thm:p03-w03-p03-037-sauer-shelah; thm:p03-w03-p03-037-nip switched from cited= to proved=annex.
  Simon's Lemma 2.5 (p. 14), Proposition 2.11 (p. 16) and Example 2.12 (p. 17), re-verified in the
  held PDF in this run, are kept only as an alternative route in the reader text.
- Repaired in the continuation run: eight corrupted citation commands (a tab character had replaced
  the letters "ci" of the cite macro) and two broken multline line breaks before rightarrow/vee.
- Not written here by design of the packet: the general monotonicity and cell-decomposition
  proofs belong to the readonly units owned by w03-p03-036; the NIP survey unit belongs to
  w03-p03-035. The chapter checks their conclusions on concrete semialgebraic data.
- Placement: the chapter is not yet on the static input route; the driver lines in the return
  file (after parts/p03/classification-theory in handbook/parts/p03.tex and after
  annex/p03/feferman-vaught-composition in handbook/annex/p03.tex) must be added by the lead.
- Note: def:p03-quantifier-elimination and sec:p03-quantifier-elimination live in
  qe-categoricity-games.tex, which is not on the static input route; this chapter carries its own QE
  definition (def:p03-w03-p03-037-qe-def) and points to the on-route catalogue tab:p03-qe-catalog.
- Self-checks at stop: unit-compile ok; check.py filtered shows only bib-key for intake keys;
  find_fused_spaces clean.
- Block 2 run (2026-10-13): the assessment's only hard finding was that tools/check.py --tree handbook
  timed out at 180 s; the full check was rerun here without the 180 s cap (result recorded in the
  block 2 return). One reader change: the closing warning def:p03-w03-p03-037-expansions now
  cross-references the readonly owner's labels thm:p03-w03-p03-035-dense-predicate (NIP ordered
  theory that is not o-minimal) and thm:p03-w03-p03-035-rcf (RCF among simple/stable/NIP), instead
  of restating them. unit-compile ok after the edit.
- Component standing: every component_id in the packet belongs to a readonly unit
  (ED26-REQ-D-P4-009-01 -> w03-p03-035; ED26-REQ-N-a-009-01..03 -> w03-p03-036). This chapter
  supplies the section 34.9 RCF material that those components use and does not author them.

# P15 163.10: exchangeability assumptions and their limits as a justification of induction (w02b-p15-022)

4 October 2026. Packet w02b-p15-022, block 1.

## Files

- Body: handbook/parts/p15/exchangeability-and-predictive-induction-w02b-p15-022.tex
- Annex: handbook/annex/p15/exchangeability-and-predictive-induction-w02b-p15-022.tex
- Symbol intake: handbook/registry/symbols-intake-p15-exchangeability-and-predictive-induction-w02b-p15-022.csv
- Bib intake: none needed; all keys (DurrettPTEAuthor2019, Zabell2011CarnapInductiveInference, HajekStaffel2021Dynamics) are in handbook/bib/handbook.bib.
- Patch requests: work/waves/w02b/patches/w02b-p15-022.json (two host links into exchangeability-and-definetti.tex for C006 and C017).

## Sources opened in this session and locators verified

- Durrett, Probability: Theory and Examples, author Version 5 (11 January 2019),
  source/references/durrett-probability-2019-01-11/PTE5_011119.pdf, printed pp. 247-256
  (physical 255-264). Verified: Theorem 4.6.8 (p. 247), Example 4.6.11 (p. 248), Section 4.7,
  Examples 4.7.4-4.7.8, Theorems 4.7.9-4.7.10 and the remark on nice spaces (pp. 250-254),
  "palatable assumption of symmetry" remark and Exercises 4.7.1-4.7.5 (p. 255).
- Zabell, Carnap and the Logic of Inductive Inference (HHL 10),
  source/references/p15-carnap-induction/zabell-2011-published.pdf (held copy pp. 265-309, 2009 footer).
  Verified pages: 271-273 (sec. 4, permutation postulate, p. 272 urn-of-nature and additional-assumption
  passage; p. 273 counts sufficient), 275-276 (sec. 5.2 representation, no restriction on mixing measure),
  279-281 (attribute symmetry, die example), 281-283 (instantial relevance, correlation bound,
  extendability, finite representation statement), 289-290 (partial and Markov exchangeability).
- Hajek and Staffel, Subjective Probability and Its Dynamics (Handbook of Rationality ch. 4.1),
  source/references/p15-rationality-4-1/hajek-staffel-2021-publisher.pdf, pp. 239-249 read in full
  (text extraction). The chapter does not mention exchangeability or the representation theorem;
  de Finetti appears for the betting account (p. 240), the Dutch book theorem (p. 240), the accuracy
  result (p. 242) and the countable-additivity note 3 (p. 248). Locators used: pp. 240-241 (betting,
  Dutch book, converse), p. 243 (Principal Principle, Reflection), pp. 243-244 (Indifference, cube
  factory), p. 244 (conditioning arguments and objections), p. 248 n. 3.

## Components written in this block

- MP-0 (163.10 comparison): sections task, support, conclusion, limits of the body file;
  results thm:p15-w02b-p15-022-{symmetry-consequences, predictive, mixing-law, recoding, markov-trend};
  warning def:p15-w02b-p15-022-not-established; method def:p15-w02b-p15-022-procedure.
- ED26-BM-RAT2021-4-1-C04: comparison section; thm:p15-w02b-p15-022-{finite-word-credences, reflection};
  examples def:p15-w02b-p15-022-{conditioning-example, indifference-example};
  table tab:p15-w02b-p15-022-comparison.
- ED26-P15-CH-exchangeability-and-definetti-C006: thm:p15-w02b-p15-022-reverse-strong-law-boundary.
- ED26-P15-CH-exchangeability-and-definetti-C017: thm:p15-w02b-p15-022-backward-changing-boundary.

## Editorial decisions

- The recoding theorem (Y exchangeable iff X fair i.i.d.) and the two-agent opposite-prediction
  example are editorial results, proved in full; linked to def:p15-goodman-grue but not attributed to Goodman.
- The Markov chain exchangeability classification (q in {1/2, 1}) is editorial.
- Finite additivity: only claims proved are the unique countably additive extension from finite-record
  credences and the 0/1 inner/outer finite-record bounds for the convergence event. No claim is made
  that a finitely additive extension assigning a different value exists.
- Zabell's Markov-exchangeability representation (Diaconis-Freedman) is reported with locator, not proved.
- Existing treatments reused rather than duplicated: thm:p15-carnap-history-family,
  thm:p15-carnap-history-finite, thm:p15-exchangeable-second-moments, thm:p15-bayes-transformation,
  thm:p15-ui-counterexamples, thm:p15-strong-law-application-boundaries, sec:p15-hume-reference-use.
- Existing treatment found that is not listed in the packet's "existing" list:
  handbook/parts/p15/inductive-logic-and-confirmation-w02b-p15-029.tex sec:p15-w02b-p15-029-zabell
  (Zabell secs. 2-5 reconstruction, including the counts-only predictive and the Johnson-Carnap
  continuum). Not cross-referenced, since it belongs to a concurrent packet; it overlaps with item 2
  of thm:p15-w02b-p15-022-predictive (binary infinite case only).

## Open items

- Original-source presentations not held/not reconstructed: de Finetti 1937 (La prevision); Diaconis and
  Freedman 1980 Markov mixture; Savage 1972 sec. 3.7 (cited by Durrett p. 255); Skyrms 1991.
- US-0 (unassessed scope) is outside this packet's writing.
- ED26-BM-RAT2021-4-1 C01-C03, C05 were not reassessed; the reconstruction in rationality-4-1.tex is a
  read-only host here.

## Block r3 (4 October 2026): gaps C004, RAT2021-4-1 C01 and C05

Sources reopened this session: hajek-staffel-2021-publisher.pdf (pymupdf text of all 16 PDF pages; printed
pp. 239-251). Verified: p. 248 conclusion list of alternatives (Dempster-Shafer, ranking, belief revision,
possibility) and note 5 (Cox -> Dubois-Prade ch. 4.7); reference-list entries and their pages: p. 249
(Armendt 1980, De Bona-Staffel 2017/2018, de Finetti 1964/1974, Diaconis-Zabell 1982, Easwaran 2013,
Greaves-Wallace 2006, Hajek 2003, Hajek 2008, Jeffrey 1965, Joyce 1998), p. 250 (Kemeny 1955,
Leitgeb-Pettigrew 2010a/b, Levi 1967, Lewis 1999, Pettigrew 2016/2018, Ramsey 1990, Savage 1954,
Schoenfield 2017, Shimony 1955, Skyrms 1987/1993, Slovic-Lichtenstein 1971), p. 251 (van Fraassen
1981/1984, Zynda 2000). No Bolker entry exists in the list. held-sources.json searched: none of these
dependent works is held (Abdellaoui-Wakker 2020 on Savage acts is a different work).

Written:
- C004: thm:p15-w02b-p15-022-projection-boundary (body sec. boundaries; annex proof). Three items:
  G=H=sigma(V); the exchangeable constant sequence in the Hewitt-Savage step; mean independence suffices
  (L1) and is strictly weaker than independence.
- C01: sec:p15-w02b-p15-022-alternatives, tab:p15-w02b-p15-022-alternatives,
  thm:p15-w02b-p15-022-alternatives-contrast (annex proof), procedure step 7. Editorial worked example;
  possibility conditioning is defined in the theorem because no on-route unit fixes one.
- C05: sec:p15-w02b-p15-022-dependent-sources, tab:p15-w02b-p15-022-dependent-sources (D1-D21, D5a, D8a),
  proofboundary paragraph listing owed works.

Not cross-referenced: w02b-p15-034 Dempster conditioning (def:p15-w02b-p15-034-dempster-conditioning,
thm:p15-w02b-p15-034-dempster) - concurrent packet, not yet on the input route.

Note for tooling: in this environment bash heredocs collapsed "\\" to "\"; edits containing LaTeX row ends
were made with the Edit tool or from files.

## Block r3-b2 (4 October 2026): RAT2021-4-1 C05 row D21 and exchangeability C018

Sources opened this session:
- hajek-staffel-2021-publisher.pdf, PDF p. 8 = printed p. 246: the evidence sentence cites Slovic and
  Lichtenstein 1971 and, as "see also", chapter 8.3 by Gloeckner and chapter 8.5 by Hertwig and Kozyreva.
- source/references/p17-rationality-8-3/gloeckner-2021-prospect-theory-publisher.pdf (held; 12 PDF pp.;
  printed 486-493 plus an unnumbered opening page). Full-text search of every page for bayes, conservat,
  updat, revis, posterior, belief, base rate, Edwards, Slovic: no credence-revision study. Read the summary
  (opening page) and p. 490 (description-experience gap is problem dependent, not universal), p. 491.
- citations/Hertwig and Kozyreva - ... (2021, chapter copy).pdf (held; 14 PDF pp.; printed 506-515 plus
  unnumbered opening page). Read pp. 509-512 in full: p. 509 Bayesian updating among the benchmarks of the
  heuristics-and-biases program; p. 510 objections (narrow coherence norms, format dependence, adaptive rules).
  Same full-text search: no credence-revision study.
- Durrett PTE5_011119.pdf, PDF 262-263 = pp. 254-255 (nice-space rcd, presentable, Dubins-Freedman 1979 and
  Freedman 1980; p. 255 foundations of statistics, Savage 1972 sec. 3.7); bibliography PDF 486 = p. 478
  (Freedman 1980 title). Hewitt-Savage 1956, Dubins-Freedman 1979, Freedman 1980, Savage 1972: not in
  held-sources.json.

Correction to the assessment premise: the assessment asked for chapters 8.3 and 8.5 to be listed as
"owed, unheld"; both are held (held-sources.json entries above), so row D21 lists them as held and read, with
what each does and does not supply. The finding remains owed to Slovic and Lichtenstein 1971 (unheld).

Written:
- C05: row D21 (three works, status per work), intro paragraph corrected (two chapters held), accounting
  paragraphs after the table, owed-works paragraph of def:p15-w02b-p15-022-scope.
- C018: sec:p15-w02b-p15-022-presentable with def/thm/example (annex proof); Savage remark after the
  predictive theorem; patch request 3 links the host proofboundary. Definition of "presentable" is the
  handbook's finite-dimensional reading of Durrett's sentence, flagged as not Hewitt-Savage's own definition.
  Converse of item 2 deliberately not asserted (Freedman 1980 title).

Guard G1: the four flagged spec/research files belong to packets w02b-p01-014 and w02b-p02-036; untouched.

## Continuation

State at return (r3-b2): C05 row D21 extended; C018 Durrett boundary written in owned file (counterexample
works blocked_source; host link pending patch). unit-compile ok; check.py clean for owned files.

State at return (r3): C004, C01, C05 written as above; unit-compile ok; check.py clean for owned files.
Remaining in this unit: C02 and C03 not reassessed here (host rationality-4-1.tex is read-only).

Earlier state at return: body and annex written; all nine results have annex proofs; patch requests filed for host
links (C006, C017). Next steps if continued: (1) lead applies patch requests and inserts the body/annex
inputs after rationality-4-1 in handbook/parts/p15.tex and handbook/annex/p15.tex; (2) optional
cross-reference to the w02b-p15-029 Zabell reconstruction once its labels are stable.

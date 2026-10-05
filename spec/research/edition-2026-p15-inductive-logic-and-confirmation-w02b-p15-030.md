# w02b-p15-030: P15 164.7 and 164.8 (Eberhardt--Glymour; Niiniluoto)

Packet: work/waves/w02b/packets/w02b-p15-030.json (label_tag p15-w02b-p15-030).
Units: ED26-SRC-063-1010 (Eberhardt--Glymour, HHL 10 ch. 10, pp. 357--389),
ED26-SRC-063-1009 (Niiniluoto, HHL 10 ch. 9, pp. 311--356).

## Held sources opened in this session

- source/references/p15-reichenbach-probability-logic/eberhardt-glymour-reichenbach-scholar-copy.txt
  and .pdf (32 pages; printed pp. 357--388; bibliography page 389 absent; footer
  "(c) 2009 Elsevier BV"). Rendered PDF page 14 (printed p. 370) and the held image
  history-probability-axioms-15.png (printed p. 371) to read the axiom displays.
- source/references/p15-hintikka/niiniluoto-hintikka-program-author-copy.txt and .pdf
  (46 pages; printed pp. 311--356; footer 2009). Rendered printed pp. 316, 319--322,
  324, 325, 334, 341 and read history-page337.png to verify every displayed formula
  used.
- Both paths are listed in spec/coverage/edition-2026/held-sources.json (filesystem
  walk entries). The packet's units[].held_paths list only the Milton PDF and the
  Fordham renderer text; those do not contain chapters 9--10. The chapter texts above
  are the held files actually used.

## Existing treatment found (A9)

- handbook/parts/p15/reichenbach-probability-logic.tex (routed): already proves the
  three-parameter coupling table (thm:p15-reichenbach-coupling), non-closure of
  frequency limits (thm:p15-reichenbach-frequency-boundaries item 1), straight-rule
  pointwise attainability and rival rules (thm:p15-reichenbach-straight-rule-boundary),
  the total-probability answer to the product objection
  (thm:p15-reichenbach-higher-order-boundary) and the noise-free fit family
  (thm:p15-reichenbach-finite-fit). The new chapter cross-references these instead of
  re-proving them (two drafted duplicate theorems were removed).
- handbook/parts/p15/carnap-logical-probability-and-induction.tex: Dirichlet-type
  predictive family (thm:p15-carnap-history-family) reused for the converse of the
  Kemeny--Carnap theorem; c* analogy (thm:p15-carnap-analogy) and law/instance
  (thm:p15-carnap-universal) linked. Its proof boundary lists "Johnson--Carnap
  sufficientness" and "Hintikka--Niiniluoto extensions" as open; the Kemeny--Carnap
  characterization on singular sentences is now proved in
  annex:p15-w02b-p15-030-kemeny-carnap.
- handbook/parts/p15/polya-urns-and-beta-prediction.tex: beta posterior mean
  (thm:p15-polya-posterior-prediction) linked from the flat-prior theorem.
- NOT listed in the packet's "existing": handbook/parts/p15/hintikka-inductive-logic.tex
  and handbook/annex/p15/hintikka-inductive-logic.tex (unrouted, not \input, not owned).
  It cites Niiniluoto2011HintikkaProgramReading. It cannot be \cref'd (not in the
  build). The lead should decide whether to retire it or route it; the new chapter
  does not depend on it.

## Source-text decisions recorded (correction policy: flagged in reader text, not silent)

1. Eberhardt--Glymour p. 370 prints P(A v B) = P(A)+P(B)-P(A)(B|A); read as
   P(A)P(B|A) (second line of the same display has P(A)P(B|A)).
2. Niiniluoto p. 316 prints "lambda = infinity gives Reichenbach's Straight Rule" and
   "lambda = 4" for the Tractatus range measure. By (2), the straight rule is lambda=0
   and 1/K is lambda -> infinity; p. 323 ("lambda=0 is excluded by A2") agrees.
   Reader text records both the printed wording and the reading.
3. Niiniluoto p. 324: product formula printed "gamma_1...gamma)K-1"; read as
   gamma_1...gamma_{K-1}.
4. Niiniluoto p. 324: lambda = K f(1,K+1,K)/(1-K f(1,K+1,K)) - 1. Under the chapter's
   own (27) at w=K, f(1,K+1,K) = (1+lambda/K)/(K+1+lambda) and the inversion gives
   "- K", not "- 1". Recorded as an unresolved discrepancy (Hintikka--Niiniluoto 1976
   not held); proved form in thm:p15-w02b-p15-030-kdim part 3.
5. Niiniluoto p. 325: "lambda ... equals alpha w for some constant a > 0"; read as a
   constant multiple a w (thm:p15-w02b-p15-030-intersection).
6. Niiniluoto p. 337: (54) with true-case utility 1-P(g) gives
   P(g/e)-qP(g)-(1-q)P(g)P(g/e), equal to the printed (55) only if q=1; with 1-qP(g)
   it is exact. Proved in thm:p15-w02b-p15-030-utilities part 5.
7. Niiniluoto p. 333 (42): with corr as the minimum over all disjuncts, the hypothesis
   e |- h1 > h2 is insufficient (counterexample in the annex); holds for the minimum
   over e-compatible disjuncts, or under |- h1 > h2.
8. Niiniluoto p. 319/320 (18): "1/2^K for all C^w" includes the contradictory empty
   constituent; hbwarning def:p15-w02b-p15-030-nn-empty records that a probability
   must give it 0; posterior results unaffected.
9. Niiniluoto p. 347: PAT>0 iff P(g^eps)>0 stated unconditionally; proved in the
   conditional form P(g^eps/e)>0.
10. (11) printed with "=" after the turnstile; written as equivalence.
11. Niiniluoto p. 329: "K - w" nomic constituents compatible with C^w; by (29),(10)
    they are B_CT with CT a superset of CT_w, 2^(K-w) of them (thm:p15-w02b-p15-030-uchii
    part 3). Printed count kept as wording; discrepancy stated in reader text.

## Not proved (reported from the chapter with attribution)

Hintikka--Niiniluoto K-dimensional representation (parameters, (26), product formula),
(27), (28), derivation of (3),(4) from (27); (19) and (25) for general lambda and the
alpha -> infinity limit of the whole lambda-alpha continuum (gamma-ratio asymptotics for
non-integer shifts not supplied); approximations (21), (24), (56); n0 threshold
formula; (43); Hilpinen/Tuomela/Uchii/Kuipers/Niiniluoto--Tuomela results;
Reichenbach's convergence theorems (1)--(4) and the faster-convergence claim; van
Fraassen's result; Creary's analysis.

## Continuation

- Session 2 (gap closure after assessment): Eberhardt--Glymour p.387 Notes on
  Sources and the closing "remained at loss" qualification added (body lines
  1237--1255; held txt lines 1460--1474). Niiniluoto: abductive confirmation and
  abductive criterion defined, (38) tied to thm:...-relevance parts 1--2 (body
  2294--2307); purpose of corr (40) for weak generalizations (2320--2328); p.314
  quasi-psychological counterparts, Stegmuller 1973, Lakatos 1968b (1419--1427);
  p.333--334 advisors-vs-truth-seekers and Peircean fallibilist acceptance
  (2383--2400); the dropped chronology citations restored inline by author-year
  at the pages they occur (listed in the return file).
- ED26-SRC-063-1010-C001/C002/C003 and MP-0 (164.7): body lines 73--1272;
  annex lines 4--95.
- ED26-SRC-063-1009-C001/C003 and MP-0 (164.8): body lines 1274--2989; annex
  lines 96--582. C002 partial: the unproved list above and item 4.
- Unit compile ok; fused-space check clean; check.py no finding for these files.
- Lead items: driver insertion patch work/waves/w02b/patches/w02b-p15-030.json;
  held-sources.json does not map the two held chapter copies to SRC-063 and the
  packet held_paths omit them.
- Session 3 (assessment gaps on ED26-SRC-063-1009, held txt
  source/references/p15-hintikka/niiniluoto-hintikka-program-author-copy.txt
  lines 880-916 and 1715-1792 reopened): probable verisimilitude defined from
  p.346 (def:p15-w02b-p15-030-nn-pv; no formula or abbreviation in the chapter,
  the displayed sum is the reading), its p.347 non-zero-at-zero-posterior
  property proved (thm:...-pat part 2) and computed in
  def:p15-w02b-p15-030-nn-pat-worked; ESC extension of PAT convergence (p.347
  "similar modifications") proved as thm:...-pat parts 5-6 (forms not stated
  in the chapter; marked as the forms proved here); ESC definition moved
  before the theorem. Uchii (p.329): two assumptions, two-sided condition,
  strength rationale, Plenitude, Niiniluoto's fluctuating-actual vs
  permanent-nomic rationale added; thm:p15-w02b-p15-030-uchii proves (31)
  (removed from the not-proved list), the two-sided reduction, the
  compatibility count 2^{K-w} (source decision 11: printed K-w), the
  elimination of rival nomic constituents and Plenitude => P(B^c/C^c)=1.
  Unit compile ok; fused-space and check.py clean for these files.

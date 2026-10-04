# Stochastic satisfiability: allocation and primary-source record

Active allocation: planned165.4, `ED26-SRC-051-0034`, Stephen M. Majercik,
*Stochastic Boolean Satisfiability*, Handbook of Satisfiability, second
edition2021, chapter34, pp1331–1369. Queue componentsC001–C003 require the
complete chapter, algorithms/proofs and all examples/experimental conditions.
No ledger, driver, canonical bibliography or shared map is edited here.

## Held primary versions

The author's own publications page links `pubs/jar00.ps`:
<https://tildesites.bowdoin.edu/~smajerci/publications.html>.
Downloaded exact PostScript to
`source/references/p15-stochastic-satisfiability/littman-majercik-pitassi-2000-author.ps`.
SHA256 `9D3E94063D07BCC234158E5AB4F151F4D66A8AAAC2F793BA6CC6650FE66DC84E`.
The title page says January2000; running footers say `paper.tex;1/09/1999`;
copyright line1999. It is a52-page original author manuscript, not the
46-page final2001journal article and not either handbook chapter.
Converted with installed ps2pdf solely to read the held source;
PDF SHA256 `137D86BF72B918E781C3760DE6950E21BD44D845F5DE1296896536D90D212752`.
Direct reading completed all52pages, including§§1–4, all algorithm figures,
AppendixA pp48–49, AppendixB pp49–50, and references50–52.
Source-page glyph inspections: pp4,15,49; negations and inequality endpoints
were checked against actual pages because extraction loses bars.

Published2002erratum acquired from Bowdoin's explicitly open-access record:
<https://digitalcollections.bowdoin.edu/view/1316/erratum-stochastic-boolean-satisfiability-journal-of-automated-reasoning-2001-27-251-296>.
Displayed viewer links <https://digitalcollections.bowdoin.edu/file/62146/content>.
One page, JAR28 p233. Read complete. SHA256
`BDF4EB1A5934606959FA6613172E94543F3B87244EFF87FA162E9A39A824A888`.
It corrects author affiliations/email addresses, not mathematical statements.

## Exact-source standing

The2021chapter is still unheld. Its exact author/title/page identity is
registered in the queue and confirmed by DBLP's volume336 contents. The
author's public bibliography lists the separate2009chapter pp887–925,
but exposes no2021body there. Full-book mirrors without an author/publisher
or institutional permission basis were not used as substitutes. The
publisher route for the2001journal returned subscription HTML, not a PDF;
the attemptedDBLPXML download returned a bot-access HTML page. They are
saved under `*-access.html`, not counted as source bodies. Columbia's old
coauthor PDF link returned404; the live author PostScript route succeeded.
Neither the2000original manuscript nor2002affiliation erratum discharges
the separately allocated2021handbook chapter. No whole-facet closure claimed.

## Authoring decisions and source qualifications

- Native source has fair randomized quantification, existential max and
  ExtendedSSAT universal min. Rational biased quantification is a stated
  extension on p5; the packet declares its independent constant Bernoulli
  hypotheses instead of inserting conditional marginal probabilities.
- Source Figure2 returns early at `v0 >= high`; the prose/AppendixA's
  closed-interval exactness claim fails at that high endpoint. The packet
  gives an exact evaluator and explicit certified-interval threshold
  pruning, with a countercase, not a fabricated proof of the printed claim.
- AppendixA p49 contains a displayed division by4 in the average argument;
  averaging the two children divides by2. The proof uses the correct
  max/min/weighted recurrence with all endpoint cases explicit.
- AppendixB's unnormalized match-sum display is not copied as the empirical
  probability. The construction uses `(1/w) sum_h max(N_h0,N_h1)`, derives
  its overfitting lower bound, and preserves the source's exponential
  sample-size warning.
- Bayesian-network encoding is an explicit independently proved Boolean
  row-coin construction. Conditional inference needs TWO joint-event SSAT
  evaluations and positive evidence probability; it is not an identity
  between arbitrary mixed-prefix SSAT and a flat-prior Bayes calculation.

Remaining: acquire/read exact2021chapter34 pp1331–1369, and bridge its
native algorithms, stochastic-constraint programming, examples and reported
benchmarks to the older original only by actual content. The final2001
journal body and2009handbook chapter remain distinct unheld versions.

## Saved authoring packet

Body and reciprocal annex: `handbook/parts/p15/stochastic-satisfiability-and-inference.tex`
and `handbook/annex/p15/stochastic-satisfiability-and-inference.tex`.
Ten complete declared theorem/proof pairs. Core5-rule calculus sheet:
`handbook/registry/calculi/p15-stochastic-satisfiability.tex`.
Two source-role-distinct bibliography keys and19seven-field symbol rows
are in the assigned intakes. Full source semantics, crossed prefixes,
source-style DPLL transformations, corrected threshold evaluation,
value certificates/PSPACE construction, weighted projections, explicit
BN row-coin encoding, sampling optimization, exponential overfitting and
first-moment bounds are supplied. Original experimental setup remains
distinct from proof guarantees. Ordinary prefix information is not
silently treated as partial observability or causal intervention.

Root insertion seam: beside probability quantifiers, after
`probability-quantifier-elimination` and before subsequent inference units,
planned165.4; matching annex and calculus inclusion. Root owns routing,
canonical merges and coverage standing. No children, reviewers, tests,
build or manuscript rendering were run. Only source-reading conversion
and source-page glyph inspection occurred. Exact2021source closure and
the source's universal-search size proof/full cited complexity results
remain open. The full compendium objective is not completed by this packet.

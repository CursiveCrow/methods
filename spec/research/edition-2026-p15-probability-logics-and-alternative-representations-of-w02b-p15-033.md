# P15 chapter 165, sections 165.3 and 165.4: source standing (w02b-p15-033, block 1)

4 October 2026. Author record only. No reader file was written in this
block; every component of the packet is reported blocked_source below.

## What was opened in this session

- Packet work/waves/w02b/packets/w02b-p15-033.json.
- SRC-049 held preview
  tmp/edition-2026-catalog-src038/tail-039-068/SRC-049-pageplace-preview-2026-09-09.pdf
  (92 PDF pages, pdfinfo) and its reading derivative. The contents list
  (reading derivative lines 484--490) gives Chapter XIV, Probability
  Quantifiers, H. J. Keisler, starting p. 509, with section starts
  1 Logic with Probability Quantifiers p. 509, 2 Completeness Theorems
  p. 520, 3 Model Theory p. 530, 4 Logic with Conditional Expectation
  Operators p. 544, 5 Open Questions and Research Problems p. 555, and
  Chapter XV starting p. 557. The derivative's tail is the Chapter II
  material (Proposition 7.2.5 and surrounding text); no page of the
  Chapter XIV body is present.
- SRC-051 held files under source/references/acq-r1-ACQ-2026-10-0473/
  and its manifest.json (result "not_full_body"). The front matter
  contents (pdftotext lines 925--935) give Chapter 34, Stochastic Boolean
  Satisfiability, Stephen M. Majercik, starting p. 1331, sections 34.1
  Introduction p. 1331, 34.2 Definitions and Notation p. 1331, 34.3
  Complexity of SSAT and Related Problems p. 1334, 34.4 Applications
  p. 1335, 34.5 Analytical Results p. 1336, 34.6 Algorithms and Empirical
  Results p. 1337, 34.7 Stochastic Constraint Programming p. 1354, 34.8
  Future Directions p. 1356, References p. 1363; the Subject Index starts
  p. 1371. The other held files are part openers and indexes. No page of
  the chapter body is held.
- spec/research/p15-probability-quantifiers-source-note.md (prior record:
  Keisler chapter body inaccessible through Cambridge, Project Euclid and
  Google Books; distinct Keisler--Lotfallah author manuscript used for the
  existing finite-model treatment).
- handbook/parts/p15/stochastic-satisfiability-and-inference.tex, opening
  section (lines 1--60): the existing SSAT treatment is written from the
  Littman--Majercik--Pitassi January 2000 author manuscript and itself
  records the 2021 handbook chapter as a distinct, unread presentation.

## Standing per unit

ED26-SRC-049-0014 (165.3), components C001--C005: the required work is
Keisler, Chapter XIV "Probability Quantifiers", in Barwise and Feferman
(eds), Model-Theoretic Logics, original 1985 Springer-Verlag edition, or
the 2016 ASL / 2017 Cambridge reissue (Perspectives in Logic 8, DOI
10.1017/9781316717158) with an explicit content bridge, pp. 509--556.
Only the contents entry is held. The failure condition names a
contents entry and a weaker finite special case as non-substitutes, so
neither the preview nor the Keisler--Lotfallah manuscript can supply
these components. Nothing was written.

ED26-SRC-051-0034 (165.4), components C001--C003: the required work is
Majercik, "Stochastic Boolean Satisfiability", Handbook of
Satisfiability, second edition, IOS Press 2021, FAIA 336, chapter 34,
pp. 1331--1370 (the packet records pp. 1331--1369; the next item starts
p. 1371). Only contents and indexes are held; the IOS host offers the
chapter for purchase only (manifest result_detail). The held
Littman--Majercik--Pitassi 2000 manuscript is an earlier, different
presentation and is named by the failure condition ("old edition");
it is already treated in the existing SSAT chapter. Nothing was written.

## Why no owned TeX file was created

The assessed gap is that the owned body and annex files are absent, so
the scoped compile cannot run. Every component they would carry is
source-specific and its source body is not held. A file containing only
headings, a contents listing, routing prose or general material standing
in for the Keisler or Majercik presentations would be a placeholder or a
substitute deliverable, which the packet rules forbid. The compile
therefore remains failing on the missing files, and that is reported, not
worked around.

## Existing treatment not listed in the packet

handbook/parts/p15/stochastic-satisfiability-and-inference.tex (703
lines, label sec:p15-stochastic-satisfiability-and-inference) and
handbook/annex/p15/stochastic-satisfiability-and-inference.tex (520
lines), plus calculus sheet handbook/registry/calculi/p15-stochastic-satisfiability.tex.
This is the handbook's SSAT treatment for section 165.4's topic, from the
2000 author manuscript; a future chapter-34 treatment must extend or link
it rather than duplicate it.

## Continuation

- Block 1 ended with no reader text written. Resume only after
  acquisition of (a) Keisler, Chapter XIV, pp. 509--556, in the 1985
  Springer edition or the 2017 Cambridge reissue, and (b) Majercik 2021,
  Handbook of Satisfiability 2e chapter 34, pp. 1331--1370.
- On resumption: create the owned body/annex pair with the packet's
  toc_tag line and \chapter heading; for 165.3 extend from
  sec:p15-probability-quantifiers / sec:p15-probability-elimination
  without restating the Keisler--Lotfallah finite material; for 165.4
  link def:p15-ssat-native and the existing SSAT chapter and add only the
  chapter-34 content (sections 34.1--34.8) not already present.

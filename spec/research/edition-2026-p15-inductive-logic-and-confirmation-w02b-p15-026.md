# P15 164.2 — Milton 2011, "Induction before Hume" (packet w02b-p15-026)

## Source and version

- Held file: `source/references/acq-r1-ACQ-2026-10-0485/milton-2011-induction-before-hume.pdf`
  (SHA-256 2697f268e6e94ad0c1784b8cbf6f7ef08311e42d248b25b7847326f127ef55e6, 41 PDF pages).
- Identity seen in this session: title "INDUCTION BEFORE HUME", J. R. Milton; p. 1 footer
  "Handbook of the History of Logic. Volume 10: Inductive Logic ... (c) 2009 Elsevier BV".
  PDF metadata: "Vol10-final2.pdf", created 2009-10-05 (camera-ready volume file, editor-hosted).
  Running heads give printed pages 1--41 continuously; PDF page n = printed page n.
  The manifest records `result: version_differs` (camera-ready file, not a publisher download).
  The printed pagination 1--41 agrees with the dblp record for the published chapter (pp. 1--41).
  The text was not collated against the final publisher PDF; that collation remains open.
- Extraction: `pdftotext -layout` (Greek letters drop out); pages 2, 4, 5 rendered and read
  as images to recover the Greek words transliterated in the body
  (epaktikous logous, epagein, ephodos, ta katholou, ho ex epagoges syllogismos, he gar epagoge dia panton).
- Every locator in the body is a printed page of Milton's chapter seen in this session.
  Primary-text locators (Bekker numbers, book/chapter numbers, column numbers of Zabarella 1608,
  page numbers of the translations Milton cites) are reported as Milton gives them; they were not
  checked against the primary texts themselves.
- Source discrepancy noted: Milton cites "[Descartes, 1995, I, ...]" for the Regulae but the
  chapter bibliography (p. 38) lists only "[Descartes, 1985]" (Cottingham, Stoothoff, Murdoch).
  The body reports the Regulae passages by Milton's page, not by the CSM volume page.
- Milton cites [Stump, 1978] but the bibliography entry gives 2001 as the date (p. 40).

## Lange 2011 (ED26-SRC-063-1002)

Not held. `held-sources.json` has no Lange file; the packet's held paths are the Milton PDF and an
unrelated Fordham HHL volume 2 crawl (Mediaeval and Renaissance Logic contents). Required:
Marc Lange, "Hume and the Problem of Induction", Handbook of the History of Logic vol. 10,
Inductive Logic, Elsevier 2011, complete chapter 2, pp. 43--91. Reported blocked_source.

## Modern reconstructions written (handbook's own, labelled as such in the body)

1. Conversion step of Prior Analytics B23 under an extensional reading.
2. Complete, covering and partial enumeration (Sextus, Gassendi, Descartes, Ockham rule 2,
   Buridan, Hobbes, Wallis, Arnauld--Nicole).
3. Ockham's three rules under an existential-import reading; the possibility counter-instance.
4. Bacon's exclusion clauses under a Limited Variety hypothesis.
5. Wallis's binomial table: addition rule and row generation (modern proof, contrasted with
   Milton's statement that Wallis was not using mathematical induction).

None of these is attributed to Milton or to the historical authors.

## Continuation

- C001/C002/C003 (1001): body (parts/p15/inductive-logic-and-confirmation-w02b-p15-026.tex,
  lines 1-1650) and annex (138 lines, five annexitems) written in this session; unit-compile ok;
  verbatim-overlap scan (9-grams vs extracted text) leaves only marked quotations, displayed
  arguments, the (a)-(d) diagram and formulas above ten words.
- Host edit: one cross-reference sentence in parts/p15/hume-and-the-problem-of-induction.tex (lines 32-33).
- 1002 C001--C003: blocked_source (Lange chapter not held).
- r2 (assessment gaps, C002): added Sextus date and Milton's verdict on Diogenes/Sextus (printed p. 8, body 440-446);
  Bacon NO II.16 opening quotation (p. 26, body 1065-1069); Milton's empirics/beasts gloss (p. 34, body 1441-1443);
  Nizolius closing step on countless unexamined cases (p. 35, body 1480-1483). Locators re-read from the held PDF this session.
- Open: collation of the camera-ready text against the final 2011 publisher PDF.
- r3 (guard G13, copied prose): the 12-word overlap scan against the held Milton PDF found 13 runs
  (longest 44, the Wallis horned-animals quotation). Rewritten in own words or shortened to brief
  attributed quotations: planets syllogism (schematic form, p. 5), Posterior Analytics 71b20-2 premise
  list, Diogenes' dog/ox step (pp. 8-9), note 7 on probabilis (pp. 11-12), Ockham's three rules (p. 18),
  divided-sense modal induction (p. 19), Buridan's bona consequentia (p. 20), Agricola's wall/house
  example (p. 21), Bacon NO II.16 opening (p. 26; quotation cut to "a kind of divine fire"),
  Descartes Rule VII (p. 27), Gassendi's animals (p. 30), Wallis's horned animals (p. 33),
  New Essays IV.vi.13 sentence (p. 34). Re-scan: no run of 12 or more words remains.
- r3 G1: the two remaining G1 hard items (spec/research/edition-2026-p01-symbol-registry-w02b-p01-014*.md/-return.json,
  and the p02-036 pair) are files of other packets, untracked and created by other agents; this
  packet did not touch them and may not modify them.
- r4 (assessment dispute on C003): part (4) of thm:p15-w02b-p15-026-exclusion was not provable as stated, since
  survival coincides with satisfying the form conditions on I. Restated: Omega = all instances, I a finite
  subset; 'agrees with g on J' (A1-A2); 'form of g' = agreement on Omega; new part (0) survival iff agreement
  on I; part (4) = without the form hypothesis a non-form can be the unique survivor (countercase
  Omega={i,i'}, I={i}), and only when Omega minus I is non-empty. Body 1111-1164, annex 80-133. Symbol
  intake row Omega added. The reconstruction is editorial; Milton (p. 26) is the source for the form's
  presence/absence/degree description it models. Driver insertion still pending (lead).

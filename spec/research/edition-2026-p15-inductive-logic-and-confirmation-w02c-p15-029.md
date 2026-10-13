# P15 164.12 comparative source treatments (packet w02ca-p15-029)

## Run 1 (earlier session): host routing only

Gap list then: systematic-power C001, C002, C003, C010, C016 and
RAT2021-4-3 C02, C03. Under rule A14 nothing was written for readonly
units; two cross-reference sentences to the w02c-p15-028 chapter were added
to the editable host handbook/parts/p15/inductive-logic-and-confirmation-w02b-p15-025.tex
(intro lines 18-24 and the worked-example remark). Those references resolve
only once the lead routes w02c-p15-028.

## Run 2 (this session): systematic-power gaps written

Gap list: ED26-P15-CH-systematic-power C001, C002, C003, C005, C010, C014,
each marked "owned by w02c-p15-028".

Decision on A14. The r2 results (work/waves/w02ca/results-r2.json, entries
45 and 46) show that the assessment of packet w02ca-p15-028 carries only
C007 (route pending), while these items were routed to this packet as
"writable" twice. Writing nothing again would leave them unwritten. The
computed task orders them closed. The material was therefore written in this
packet's own files, not in w02c-p15-028's files or the readonly hosts.
Everything that already exists in w02c-p15-028 (L1/L2 lists, normal forms,
m_U table, non-singular consequence) is cross-referenced, not repeated. The
lead should confirm this ownership choice. If w02c-p15-028 is meant to own
these items, the material can move there unchanged.

### Sources opened this session

- source/references/hempel-oppenheim-explanation-1948/hempel-oppenheim-1948.pdf,
  physical pp. 31-41 = printed pp. 164-174 (offset 133). Text extraction plus
  page images of printed pp. 170 and 171 (to read r_I in n. 40, the
  "(9.5)" reference on p. 171 and the (9.8) bounds).
- source/references/acq-r3-ACQ-2026-10-0625/carnap-1945-on-inductive-logic.pdf
  (held; held-sources key Carnap1945InductiveLogic). Printed = physical + 70
  (physical 10 = p. 80, physical 11 = p. 81). Read pp. 75-81.

### Verified locators written

Hempel-Oppenheim: p. 164 (intuitive comparison, the ratio, relativization);
p. 165 (potential datum, K finite class, T any sentence, generality and
simplicity, n. 33, percentage attempt); pp. 165-166 (percentage then
minimal sentences); p. 168 n. 36 (maximal = dual of minimal; Church
[Logic]); pp. 168-169 (content and range indicators); p. 169 (possible
states, exclusive ranges, n. 37, inverse variation, (9.1), g1 of a class);
p. 170 ((9.4), (9.5), Carnap's objection, n. 39 = [Inductive Logic]
pp. 80-81, r2, p2, limiting processes, n. 38 = [Inductive Logic] p. 75);
pp. 170-171 n. 40 (r_I, dc, McKinsey, failing theorems, desirable features,
r_I-based power not pursued); p. 172 (domain of (9.9)); pp. 172-173
((9.13) informal, provable from (9.11)); p. 173 (closing evaluation, purely
formal, two problems, n. 41 Goodman [Query], [Counterfactuals],
[Infirmities], Carnap [Application], notes 21 and 25).
Carnap 1945: p. 75 (6)-(7) limits exist only where they exist; p. 80
(3)-(5) m*; pp. 80-81 m_w, c_w; p. 81 L_101 example, the conclusion about
past experience.

### Not presented (no held source)

Helmer-Oppenheim 1945 [Probability] and Hempel-Oppenheim 1945 [Degree]
(the construction of r_I and dc), McKinsey's note, Church's dictionary
article, Goodman's three papers, Carnap [Application] and [Semantics]: only
Hempel and Oppenheim's report of them is given, with their locators. No
treatment of those works is claimed.

### Editorial results (derived, not attributed to the sources)

thm:p15-w02c-p15-029-ratio, -renaming, -duals, -inverse,
-uniform-independence, -strict-probability, -extension, -dualism-converse,
and the warning def:p15-w02c-p15-029-naive-converse. All proofs are in the
annex.

### Existing treatment found (linked, not duplicated)

- def:p15-carnap-star, thm:p15-carnap-star-construction,
  def:p15-carnap-three-states in handbook/parts/p15/carnap-logical-probability-and-induction.tex:
  m*, c*, and the equal-state c-dagger (= Carnap 1945 c_w = HO r1 on singular
  sentences), with its non-learning property for monadic languages. This was
  not in the packet's existing list.
- sec:p15-w02b-p15-029: Carnap infinite-system limits. Not in the packet's
  existing list.
- annex:p15.power-dualism (forward half and structural identity);
  def:p15-w02b-p15-025-limits item 2 (two note-40 facts).

### Patch requests

work/waves/w02ca/patches/w02ca-p15-029.json:
1. handbook/annex/p15/systematic-power.tex: replace "The same argument proves
   the converse transformation." with a pointer to
   annex:p15-w02c-p15-029-converse. Apply together with routing this
   chapter.
2. spec/coverage/edition-2026/held-sources.json: printed_offset 70 for the
   Carnap 1945 PDF.

## Continuation

Run 2 status: the body file
handbook/parts/p15/inductive-logic-and-confirmation-w02c-p15-029.tex
(lines 1-589) and the annex (lines 1-496) are written. unit-compile reports
ok. One overfull box remains (10.5pt, in the Relationships paragraph). It
comes from cross-chapter references that are undefined in the unit build.
check.py shows only the bib-key finding for Carnap1945InductiveLogic, which
is in this packet's intake bib. find_fused_spaces reports no hits.

Remaining:
- The lead must route the body file and annex: the insertion proposal
  places them after w02b-p15-025 in handbook/parts/p15.tex and
  handbook/annex/p15.tex. w02c-p15-028 must be routed as well, because
  this chapter and w02b-p15-025 cross-reference its labels.
- Merge the intake bib and symbol intake.
- Woods 2002 ch. 3 (pp. 105-169) and Romeijn 2011 ch. 15 (pp. 625-650) are
  still blocked_source (ACQ-2026-10-0482, ACQ-2026-10-0485).
- RAT2021-4-3 items are owned by w02ca-p15-027. Nothing was written for
  them here.

## Run 3 (r4 block 1): routing

Gap list: systematic-power C002, C003, C005, C010, C014 and RAT2021-4-3
C02, C03, C05, all with the finding "not covered on the input route". Each
listed sub-item was checked against the files:
- C003 (a)-(c), C005 (a)-(b), C010 (a)-(b), C014 and C002 (d) are in
  this packet's body (sec:p15-w02c-p15-029-data lines 37-134,
  -content-range 136-252, -uniform 254-312, -evaluation 314-468,
  -dualism 470-545) and annex (annex:p15-w02c-p15-029-converse, lines
  393-496). No content change was needed.
- C002 (a)-(c) are in w02c-p15-028 (owner w02c-p15-028).
- RAT2021-4-3 C02, C03, C05 items are in w02c-p15-027 (owner
  w02c-p15-027).
The only remaining step is routing, which is a driver change. Patch
requests for handbook/parts/p15.tex and handbook/annex/p15.tex (insert
after the w02b-p15-025 lines, after w02c-p15-028 if that is routed
first) were added to work/waves/w02ca/patches/w02ca-p15-029.json.
No \input of these files was placed in the editable host, to avoid a
second input once the drivers are changed.

## Continuation

unit-compile ok (one overfull box, from cross-chapter refs undefined in
the unit build); check.py shows only the bib-key finding for
Carnap1945InductiveLogic (in this packet's intake bib); no fused spaces.
Remaining: the lead routes w02c-p15-027, -028 and -029 (body and annex)
and merges the intake bib and symbol intake; the systematic-power patch to
handbook/annex/p15/systematic-power.tex applies with that routing. Woods
2002 ch. 3 and Romeijn 2011 ch. 15 remain blocked_source
(ACQ-2026-10-0482, ACQ-2026-10-0485).

## Run 4 (r5 block 1): Romeijn 2011 ch. 15 written

Gap list: ED26-SRC-063-1015-C001..C003 (MP-0) and the Romeijn half of
MP-2. ED26-SRC-060-0003 (Woods) is a readonly unit owned by w02c-p15-027
(packet readonly_units) and was not written here.

### Source read online this session

- http://www.stephanhartmann.org/wp-content/uploads/2016/02/HHL10_Romeijn.pdf
  (fetched over http with curl into this run's scratch folder; https fails
  on the host's certificate). 26 pdf pages = printed pp. 625-650, the
  published chapter as typeset in Handbook of the History of Logic vol. 10,
  Inductive Logic (running heads "Inductive Logic and Statistics" /
  "Jan-Willem Romeijn"; first-page footer names the volume and its
  editors; the footer copyright line reads 2009 Elsevier BV while the
  volume record is 2011). SHA-256 digest
  ce1c8d18ca14ba0c774c4c271f680a5388506520414ecdee59fde883a6ea1ff8, the
  same file the r5 assessor opened. Every page was read (text extraction
  of all 26 pages; page images of pp. 627, 639, 640, 641, 643, 647, 648 to
  confirm notation: K^Omega, superscript property and subscript
  individual, underline/overline P, the l,u bounds, (16), (17), (20), the
  network figure).

### Source slips recorded (editorial notes in the text)

- p. 639: threshold range "between 6/19 and 14"; with the table the
  range is 6/19 <= r < 6.
- p. 641: display P(f^0|h1) = P(q^0 u q^1|h1) = beta = 0.30; f^0 = q^2,
  and P(q^2|h1) = 0.30.
- p. 641: prior (0.24, 0.93) -> posterior upper end 0.50 belongs to the
  exact bound 14/15; at 0.93 it is about 0.487.
- p. 641: "P(h^0) in (l,u)" superscript typo, not reproduced.
- p. 645 n. 5 refers to "chapter 15 of this volume" for Renyi-style
  axiomatisation; the packet's catalogue gives Romeijn's own chapter as
  ch. 15. Reported as the footnote numbers it; not resolved.
- p. 643/644: "increases for larger data sequences" - shown not monotone
  (thm rj-mle-coverage item 3).

### Existing treatment found and linked (not duplicated)

thm:p15-carnap-history-family / def:p15-carnap-history-family (lambda-rule
existence via alpha_i = lambda/n), sec:p15-carnap-history (Johnson
characterization needs >= 3 categories), thm:p15-carnap-history-finite,
thm:p15-binary-definetti, thm:p15-definetti-kernel,
thm:p15-directing-law-uniqueness, thm:p15-neyman-pearson,
thm:p15-fe-binomial (MLE maximizer and Chebyshev bound),
thm:p15-confidence-credibility-boundary, def:p15-carnap-c-mean,
thm:p15-w02b-p15-025-ml-cstar. None of these is in the packet's existing
list.

### Written

Body: handbook/parts/p15/inductive-logic-and-confirmation-w02c-p15-029.tex
lines 591-1821, chapter sec:p15-w02c-p15-029-romeijn (sections data,
inference, carnap, bayes, hypotheses, np, np-inference, fisher,
estimation, fiducial, assessment, comparison, sources). Annex: same-named
annex file lines 498-915, nine annexitems. Host
handbook/parts/p15/inductive-logic-and-confirmation-w02b-p15-025.tex
lines 747-751: pointer to the new chapter and its Section 98 comparison.
Intake bib: Romeijn2011InductiveLogicStatistics. Symbol intake: 24 rows.

Cited boundaries kept as boundaries (source gives no proof): (1)-(3) =>
(4) (Carnap 1952), de Finetti's representation, Neyman-Pearson optimality.

## Continuation

unit-compile ok, one overfull box (the pre-existing 10.5pt Relationships
paragraph of the Hempel-Oppenheim chapter, from cross-chapter refs
undefined in the unit build). check.py: only bib-key findings for this
packet's intake keys (Carnap1945InductiveLogic,
Romeijn2011InductiveLogicStatistics). find_fused_spaces: no hits.
Remaining for the lead: routing of this file pair (patch entries 3-4,
unchanged), merge of intake bib and symbol intake; optionally record the
Romeijn online copy (URL, SHA-256 digest above) in held-sources.json. Woods 2002
ch. 3 (ED26-SRC-060-0003) belongs to w02c-p15-027.

## Run 5 (r5 block 2): guard repairs

- G13: four runs of 12-15 words shared with the held Hempel-Oppenheim
  1948 PDF were reworded (body lines 193-194, 208-209, 435-437,
  442-444). Line counts unchanged, so earlier line ranges hold.
- A5 against the Romeijn online copy (scratch copy, same SHA-256 digest
  as above): one 13-word run at body lines 917-918 reworded. The only
  remaining run of 11 or more words is the marked, attributed Jeffreys
  quotation (body lines 1215-1216).
- G8: the fused hash label in this note and in the return file replaced by
  "SHA-256 digest".

## Continuation

waves.py verify: no hard finding (G6 findings only: journal page
locators 164-173 and 75-81 against PDFs whose printed offset the tool
does not know). unit-compile ok, one overfull box (pre-existing 10.5pt
Relationships paragraph). check.py: only bib-key findings for this
packet's intake keys. find_fused_spaces: no hits.
Remaining for the lead: routing of this file pair (patch entries 3-4),
merge of intake bib and symbol intake. Woods 2002 ch. 3
(ED26-SRC-060-0003, duty MP-1 and the Woods half of MP-2) belongs to
w02c-p15-027 and its source is not held (ACQ-2026-10-0482).

## Run 6 (r5 block 3): Romeijn gap repairs

Source re-fetched over http (same SHA-256 digest as above); pp. 625, 626,
640 and 646 re-read.
- C001: p. 625 definitions of inductive logic and statistics, the listed
  statistical results, and the common relation (both lead from given data
  to what goes beyond them): body lines 600-616. Thesis plus the three
  expected gains of a rapprochement: lines 639-650.
- C002: both p. 625 reasons for the separate development, with the
  author's "to my mind" / "or so I believe" hedges rendered as his own
  opinion: lines 618-637. p. 646 general fiducial idea (set R): lines
  1630-1638.
- C003: p. 640 evaluation ("a remarkable procedure", Jeffreys cited a
  second time) after the Jeffreys example: lines 1263-1270; the reply is
  now tied to it: lines 1308-1312.
- Symbol intake: row for R added.

## Continuation

unit-compile ok (one pre-existing overfull box); check.py: only bib-key
findings for this packet's intake keys; find_fused_spaces: no hits; A5
copy check against the Romeijn copy: only the marked Jeffreys quotation.
Remaining for the lead: routing (patch entries 3-4), merge of intake bib
and symbol intake. Woods 2002 ch. 3 (ED26-SRC-060-0003) belongs to
w02c-p15-027 and is not held (ACQ-2026-10-0482).

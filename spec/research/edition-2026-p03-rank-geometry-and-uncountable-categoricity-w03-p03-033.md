# P3 33 Rank, Geometry, and Uncountable Categoricity (packet w03a-p03-033)

## Provenance

Block 1 author (w03a). Source opened this session: held file
`source/references/p03-morley1965/morley1965-categoricity-in-power.pdf` (Morley,
Categoricity in Power, Trans. AMS 114 (1965) 514-538, version of record scan) and its
extracted text layer (the `-extracted.txt` file in the same folder). Footnote regions of pp.521, 523, 528, 532,
537 were rendered from the PDF and read directly (renders in
tmp/agent-scratch/w03a-w03a-p03-033-b1-author/). Locators used and verified:
- p.521 n.13 (single-rank variant of Def. 2.2; footnote attached to the degree in Thm 2.5(a))
- p.523 (automorphism sufficient condition and its proof) and n.14 (weakened condition
  necessary, cf. Morley's reference [10], Morley-Vaught 1962)
- p.528 (DLO not totally transcendental, before Thm 3.9) and n.16, n.17, n.18
  (n.16 on proof of Thm 3.7; n.17 on proof of Thm 3.8; n.18 on Thm 3.9)
- p.532 n.21 (footnote to Thm 4.5)
- p.537 (consequence of 4.3 and 4.6; question (5); remark on 3.5 and 3.9 and T#;
  Ehrenfeucht [1] Thm 2 and Vaught's fallacy) and n.25 (problems (1)-(4) not the author's;
  Silver answered (5)).

Footnote numbering: the task text called the Thm 4.5 footnote "the footnote" and the problems
footnote "the footnote"; in the scan they are n.21 and n.25.

Online check this session: WebSearch for a free copy of Baldwin-Lachlan 1971 (JSL 36,
79-96, DOI 10.2307/2271517) found only JSTOR/Cambridge (paywalled) and a PhilArchive record
without file. Marker 2002 (GTM 217) and Hodges 1993 (EMA 42) are commercial books; no
legitimate free copy searched for this block beyond the prior block's record.

## Mathematical decisions

- n.13 gives no proof and no property list. The literal "a single point" (exactly one) is
  shown to leave the ACF_0 type of a cube root of 2 over {0} unranked; the presentation
  reads it as "at most one point" and proves monotonicity, uniqueness of an equal-rank
  extension, restriction monotonicity, and existence of the rank in totally transcendental
  theories (lexicographic (rank, degree) minimality plus a set bound via small witnesses).
  It shows by sqrt(2), cbrt(2) over {0} in ACF_0 that the merged rank does not recover the
  degree (both rank 1, degrees 2 and 3), and that exact image fails. Comparison with Morley
  rank in general and the converse of existence were not proved (attempted; the isolation
  step is the obstacle) and are stated as not established in the reader text.
- n.21: the unnamed example is supplied by DLO (density of isolated types proved via the
  handbook's proved DLO quantifier elimination thm:p03-w03-p03-022-dlo-step; non-total
  transcendence via existing thm:p03-morley-thin-models + thm:p03-morley-countability).
- p.537 consequence: proved via 4.6 at aleph_1 over a one-element system, compactness
  stretching (thm:p03-compactness-ultraproduct), and 4.3 (prime model over X).
- Remark that (5) would follow from 3.5 and 3.9: proved as a conditional theorem whose
  hypothesis is a complete extension of a Skolem expansion with totally transcendental
  Morleyization; no claim that such an expansion exists.
- Attributions written as Morley's account only; the attributed works are not read.

## Existing treatments

Read: handbook/parts/p03/presentations/n-a-006-01.tex (whole), annex n-a-006-01.tex
(field example; item list), classification-theory.tex insertion point lines 551-552,
n-a-006-02 (via prior record). The p.537 questions and Silver footnote were already in
n-a-006-01.tex 442-468; the new section links rather than repeats them. No other
treatment of the n.13 variant, the automorphism criterion, the n.21 comparison, or the
p.537 endomorphism consequence was found (grep of handbook/parts/p03).

## Block 2 provenance

Held source re-opened this session: the Morley 1965 scan (renders of pp. 514, 515,
517, 518, 520, 530, 535 in `tmp/agent-scratch/w03a-w03a-p03-033-b2-author/`).
Footnote numbers checked on the images: the Jonsson-conditions footnote on p. 517 is
n. 5 (the task text called it n. 6; p. 518 n. 6 is the "mathematical object"
definition); p. 520 n. 12 (algebraic / Jonsson [6]); p. 530 n. 20 (Vaught [18]);
p. 535 nn. 22-24 (n. 24 reads kappa^aleph_0 != kappa on the image).

Online sources read this session (journal open archive, Mathematica Scandinavica,
journals.msp.org, version of record scans):
- Jonsson, Universal relational systems, Math. Scand. 4 (1956) 193-208,
  https://journals.msp.org/mscand/article/view/2857 ; read pp. 193-196 (conditions
  I-VI on p. 195, notation on p. 194).
- Jonsson, Homogeneous universal relational systems, Math. Scand. 8 (1960) 137-142
  (Morley's [5]), https://journals.msp.org/mscand/article/view/2746 ; read pp. 137-139
  and 142 (IV' p. 137, I' and K-homogeneous p. 138, Theorem B p. 139).
- Jonsson, Algebraic extensions of relational systems, Math. Scand. 11 (1962) 179-205
  (Morley's [6]), https://journals.msp.org/mscand/article/view/2681 ; read pp. 179-185
  (conditions (I1)-(I3), (II) pp. 179-180; Definitions 4.1-4.4, Lemma 4.5 pp. 184-185).

Block 2 decisions:
- n. 5: the conditions are stated from Jonsson's own papers; N(T) proved to satisfy
  I, I', II, III, IV', V, VI_alpha and directed unions; Morley's 1.2(d) is the
  isomorphism form IV' of [5]; the 1956 subsystem form IV is shown to fail for
  Th(Z,<) (immediate successor). Jonsson's Theorem B is only attributed; no proof
  step depends on it.
- n. 12: "related" made exact: Tr^0(A) points = types of Jonsson-algebraic elements
  = types containing a formula with boundedly many solutions (all four equivalences
  proved; Jonsson's Lemma 4.5 recovered by compactness).
- n. 20: Morley does not state Vaught's hypothesis. Used Vaught's atomistic
  condition on F_n(T(A)) (thm:p03-vaught-isolation-density, already presented from
  Vaught 1961), proved it yields a Morley-prime model over countable A, and proved
  Morley's global density hypothesis implies it. Strictness not decided.
- n. 24 example: ZFC example supplied, the theory of (omega^omega, f_n) with
  f_n(x)(m) = x(<n,m>); every countably saturated model has lambda^aleph_0 = lambda;
  kappa = aleph_omega fails this by a direct diagonal (Konig) argument written in the
  annex. Not totally transcendental since S(A) has 2^aleph_0 points for a two-element A.
- Already treated by packet w03a-p03-034 (owned files of that packet, not edited
  here): Los's question and its framing (sec:p03-w03-p03-034-opening), n. 2, n. 22
  (thm:p03-w03-p03-034-universal-homogeneous), n. 23 (thm:p03-w03-p03-034-limit-power),
  n. 24 first statement (thm:p03-w03-p03-034-mv-existence). The new section links
  them instead of repeating them. They and this file are not yet routed.
- Patch requests: work/waves/w03a/patches/w03a-p03-033.json (routing of both owned
  tex files; four link edits in n-a-006-01.tex; correction of the 034 warning that
  says the n. 24 example is not constructed).
- The G8 hit in this note (fused path token) was removed by putting the held-file
  path in a code span and rewording the extracted-text mention.

## Block 2 second pass (2026-10-13) provenance

Held source re-opened: the Morley 1965 scan, pages 515, 516, 517, 518, 519, 523, 529
and 538 rendered in `tmp/agent-scratch/w03a-w03a-p03-033-b2-author/` (p515.png etc.;
n9zoom.png is a 400 dpi crop of the p. 518 footnotes). Footnote numbers and pages
checked on the images: n. 3 p. 515 (Kamke [7, pp. 126-134]); nn. 6-10 p. 518;
n. 11 p. 519; n. 15 p. 523 (Robinson, Complete theories, North-Holland 1956);
n. 19 p. 529 (Theorem 1.10 of [15]); reference list p. 538 ([7] Kamke, [13]
Ryll-Nardzewski, [15] Tarski-Vaught 1957, [18] Vaught 1961). No online source read.

Decisions:
- n. 9 prints the second turnstile as T(A) with an accent over A; read as provability
  from T(A) and said so in the reader text.
- Morley's satisfaction notation (turnstile with subscript A, p. 516) is mentioned once
  and rendered with \entails, because the registry reserves the subscripted turnstile
  for derivability. Symbol intake row records it.
- n. 7 is made exact by a proved theorem (concrete categories satisfy the abstract
  axioms; monomorphisms and C(T) are categories, (gf)^* = f^* g^*).
- n. 8 is made exact by a proved four-clause dictionary (T(A) complete; complete
  extensions by constants give systems up to isomorphism; monomorphisms = theory
  inclusions after renaming; S(A) = complete one-constant extensions of T(A)).
- n. 9 proved in four clauses with the DLO two-point example (verified in the annex).
- n. 19 proved as a corollary of the handbook's Tarski-Vaught test; nonempty |A| added
  (Morley p. 538 says the empty set is strictly not a subsystem).
- nn. 3, 10, 15 are reference footnotes: stated with Morley's locators and linked to
  thm:p03-w03-p03-034-cantor-bendixson, thm:p03-ryll-nardzewski, sec:p03-n-a-003-01,
  Robinson1956; the cited works are not read.
- G13: the 12-word run (p. 520 n. 12 paraphrase) reworded; a 10-word check against the
  extracted Morley text is clean.
- G6: the 36 findings are artefacts of the held entry lacking printed_offset (PDF page 1
  is printed p. 514). Patch request added to work/waves/w03a/patches/w03a-p03-033.json
  (insert "printed_offset": 513 into the held-sources.json entry).
- G3/G4 timeout of check.py --tree handbook is environmental; not fixable from owned
  files.

## Continuation

Second pass of block 2 (2026-10-13): new body subsection
sec:p03-w03-p03-033-early-footnotes (body lines 65-286) and four annex items (annex
lines 17-283): def/thm map-category (nn. 6, 7, 11), thm syntactic (n. 8 and the p. 518
remark on S(A)), thm open-formulas with DLO example (n. 9), Tarski criterion corollary
(n. 19), reference paragraphs for nn. 3, 10, 15. Intro paragraph updated. G13 run
reworded. Symbol intake: 10 rows added. unit-compile ok (8 overfull boxes, annex
headings from long labels and one pre-existing). find_fused_spaces clean.
Remaining in this packet: Baldwin-Lachlan 1971 and Marker 2002 versions of N-a-006-C01,
MAP-03, MAP-04, MAP-05 (sources not held); Hodges 1993 ch. 12 (SRC-048-0012
C001-C005) and section 33.4 (body not held); routing of the owned files and the
held-sources printed_offset (lead, patch requests). Open: whether Vaught's n. 20
hypothesis is strictly weaker.

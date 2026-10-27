# w02ca-p15-016 (P15; sections 161.10, 161.11, 161.13): research note

## Scope handled by this packet

Readonly units (A14), not written here: ED26-P15-CH-central-limit-theorems and
ED26-P15-CH-weak-laws-and-triangular-arrays (owner w02ca-p15-015),
ED26-P15-CH-independent-random-variables (owner w02ca-p15-006),
ED26-P15-CH-optional-stopping-and-random-walks (owner w02ca-p15-020).
The CLT, IRV and WL gaps listed in the computed task belong to those owners.

Written unit: ED26-P15-CH-normal-domains-of-attraction. Open items were C009,
C010 and C014; C001-C008 and C011-C013 had no listed gap and are unchanged in
handbook/parts/p15/normal-domains-of-attraction.tex and its annex.

## Sources opened in this session

- Durrett, PTE Version 5 (11 January 2019), held file
  source/references/durrett-probability-2019-01-11/PTE5_011119.pdf.
  PDF page 160 = printed p. 152 (Remark before Theorem 3.4.14; Theorem 3.4.14;
  the Gnedenko-Kolmogorov sentence). PDF pages 190-191 = printed pp. 182-183
  (Section 3.8, (3.8.1)-(3.8.3), constant C = alpha int_0^infty (1-cos u)/u^{alpha+1} du).
  The p. 152 Remark says "Section 3.6"; in this version Section 3.6 is Poisson
  Convergence (p. 167) and Stable Laws is Section 3.8 (p. 182) per the
  contents page. The body records this.
- Gnedenko-Kolmogorov 1954, held file
  source/references/gnedenko-kolmogorov-1954/limit-distributions-1954.pdf.
  PDF 185-186 = pp. 171-172 (Section 35 opening, definition of attraction with
  zeta_n = B_n^{-1} sum xi_k - A_n, framing paragraph, Theorem 1 display (1),
  footnote "A. Ya. Khintchine [52], W. Feller [27], P. Levy [75]").
  PDF 54 = p. 40 (definition of same type F_2(x) = F_1(ax+b), a>0; normal type;
  improper/proper types). Bibliography: [27] Feller, Math. Z. 40 (1935), 42
  (1937), p. 258; [52] Khintchine, Giorn. Ist. Ital. Attuari 6 (1935), p. 259;
  [75] Levy, J. Math. Pures Appl. (9) 14 (1935), p. 260.

## Decisions

- New chapter in owned files (packet heading level \chapter, toc tag), placed
  per the insertion proposal; it extends the NDA chapter by \cref and does not
  restate its results.
- C010: the non-chi limit is proved directly (characteristic functions,
  thm:p15-clt-complex-products, continuity theorem); the proof also proves
  the equivalence of "symmetric + |X| tail" with Durrett's (3.8.1).
  Worked example alpha = 1: C = pi/2 via the Polya density total mass.
- C014: GK framing claims (§ 33 stable-laws-only claim; complete solution in
  § 35; normal versus other stable domains) are reported with attribution, not
  proved; the type-invariance claim is proved (thm:p15-w02c-p15-016-types).
- Patch requests (work/waves/w02ca/patches/w02ca-p15-016.json) add links in
  the read-only NDA body: opening sentence (Levy attribution), item 3 of
  thm:p15-nda-examples, and def:p15-nda-historical-boundary.
- One marked quotation of Durrett p. 152 (one sentence fragment); all other
  source prose paraphrased.

## Continuation

- Run 2 (resumed after the usage limit): open NDA gaps were C001, C010,
  C014. All three are treated in the owned body/annex files written in
  run 1 (def:p15-w02c-p15-016-attraction and thm:p15-w02c-p15-016-types
  for C001; thm:p15-w02c-p15-016-stable and -cauchy-case for C010;
  sec:p15-w02c-p15-016-framing and def:p15-w02c-p15-016-boundary for C014).
  Every locator was re-verified in the held PDFs in run 2: Durrett PDF 160
  (p. 152), 190-191 (pp. 182-183); GK PDF 54 (p. 40), 185-186
  (pp. 171-172, zeta_n display checked on the page image), 272-274
  (bibliography [27], [52], [75], pp. 258-260).
- Run 2 added a fourth patch request (C001): a link from
  def:p15-nda-law-and-moments to the general GK definitions.
- Unit compile ok (overfull 3); check.py shows no finding for these files;
  fused-space check clean.
- Remaining, lead action only: insert the body file after
  parts/p15/sequential-evidence-and-multiple-testing-w02b-p15-063 in
  handbook/parts/p15.tex and the annex file after
  annex/p15/sequential-evidence-and-multiple-testing-w02b-p15-063 in
  handbook/annex/p15.tex (the route is what the assessment found missing);
  apply the four patch requests; merge the symbol intake.
- Run 4 (resumed after the usage limit, 2026-10-10): the assessment listed
  four gaps, IRV C001, C002, C004 and WLTA C006. Both units are readonly
  for this packet (IRV owner w02ca-p15-006, WLTA owner w02ca-p15-015), so
  nothing was written for them here (A14). The source points were checked
  in the held Durrett PTE5 file so the relay is exact: PDF 52 = p. 44
  (an infinite collection is independent if every finite subcollection is;
  no countability restriction); PDF 55 = p. 47 (the Remark after the proof
  of Theorem 2.1.7 on why the lambda-system route is used); PDF 68 = p. 60
  (n = 365 birthday reading, about 365 log 365 = 2153.46 tries, ratio 5.89).
  w02ca-p15-006 is not in run r4 (its r3 outcome was drafted with no open
  IRV components), and the IRV and WLTA host files are read-only for every
  packet in this wave, so the lead has to route these four gaps.
- NDA unit: no new gap listed. Unit compile ok (overfull 3); check.py has
  no finding for these files; fused-space check clean.
- Run 5 (2026-10-11): the assessment listed NDA C010 (owned unit) plus
  disputes on readonly units CLT (C001, C005, C019, C025, C029, C030),
  WLTA (C006, C011) and OS (C013, C020). Readonly units were not written
  here (A14); their owners are w02c-p15-015 and w02c-p15-020, and the CLT
  and WLTA disputes depend on driver routing of the owner's file, a lead
  action.
- C010 written in the editable annex host
  handbook/annex/p15/normal-domains-of-attraction.tex,
  annex:p15.nda-examples, lines 686-838: part 1 now verifies
  nondegeneracy and slow variation, invokes the construction and
  sufficiency theorems, and names the centering n mu for both scales
  (with thm:p15-clt-perturbation for the sqrt(n E X^2) rescaling);
  part 3 now covers every symmetric law with the stated tail: the tail
  fixes the law of |X| (P(|X|<=1)=0, density alpha u^{-1-alpha} on
  (1,infty)) and, with symmetry, the law of X; H_X and q_X derived;
  the ratio limit (2-alpha)/alpha derived; nondegeneracy checked; the
  general nondegenerate normal target reduced to chi before invoking
  thm:p15-nda-characterization. This is general mathematics, no source
  locator added.
- Patch requests added (entries 5-7 of work/waves/w02ca/patches/
  w02ca-p15-016.json): body part-1 statement names S_n - n mu; driver
  insertions of the owned body and annex files (the CLT-C019 and C030
  disputes cite this packet's lines 32-65 and 145-216 as unrouted).
- Unit compile ok (overfull 3); check.py: no hard finding in these files;
  fused-space check clean.
- Run 6 (2026-10-11): the assessment listed NDA C010 and C014 (owned
  unit) and states for both that the owned body/annex files supply the
  missing text and that the only missing step is routing. Drivers
  checked: handbook/parts/p15.tex and handbook/annex/p15.tex still do not
  input the owned files. All seven patch requests in
  work/waves/w02ca/patches/w02ca-p15-016.json were rechecked: each
  anchor_quote occurs exactly once in its host and none is applied yet.
  No new text written; C010 and C014 stay blocked_policy on the two
  driver insertions (entries 6-7). Readonly-unit disputes (CLT C001,
  C005, C019, C025, C029, C030; WLTA C006) belong to w02c-p15-015 (A14);
  CLT C019(ii) and C030 are also answered by this packet's owned body
  (thm:p15-w02c-p15-016-stable; sec:p15-w02c-p15-016-framing) once routed.
- Unit compile ok (overfull 3); check.py: no finding in the owned files
  (host NDA files show only the tree-wide notation-scope and
  rule-outside-registry metrics); fused-space check clean.
- Run 6 block 2 (2026-10-11): the assessment listed NDA C001, C009, C010
  and C014 (owned unit); for each it states that the supplying text is in
  this packet's owned body/annex files and that nothing else is missing.
  Owned body lines 35-143 reread: Levy attribution and the two "last word"
  claims (Durrett p. 152), the GK Section 35 attraction/domain/type
  definitions (pp. 171-172, p. 40), the type lemma, the p. 172 programme
  claims and the Khintchine/Feller/Levy footnote with items [52], [27],
  [75] are all present; power-tail theorem at 145-215 with annex 42-205.
  Drivers still do not input the owned files; all seven patch requests
  rechecked (each anchor unique in its host, none applied). No new text
  written. The four NDA components stay blocked_policy on patch entries
  5-6 (driver insertions) and 0-3 (host links).
- Readonly-unit disputes in this assessment (CLT C001, C005, C019, C025,
  C029, C030; WLTA C006, C011; IRV C016) belong to w02c-p15-015 and
  w02c-p15-006 (A14); not written here.
- Unit compile ok (overfull 3); check.py: only the preexisting soft
  notation-scope and rule-outside-registry notes in the NDA hosts;
  fused-space check clean.
- Run r6 block 1 (2026-10-12): the assessment listed NDA C001, C010 and
  C014 (owned unit), each marked "route pending" on this packet's owned
  body/annex files. Owned body reread in full: C001 at lines 67-110
  (def:p15-w02c-p15-016-attraction, thm:p15-w02c-p15-016-types), C010 at
  145-215 (thm:p15-w02c-p15-016-stable, -cauchy-case; annex 42-205),
  C014 at 32-143 and 217-233 (Levy attribution and both "last word"
  claims; Section 35 footnote; stable-only domains via \S 33; complete
  solution; wide normal domain versus resembling-law stable domains;
  def:p15-w02c-p15-016-boundary). Drivers still do not input the owned
  files; all seven patch requests rechecked (anchors unique, none
  applied). No new text written; the three stay blocked_policy on patch
  entries 5-6 (driver insertions), with entries 0-4 the host links.
- Readonly-unit disputes in this assessment (CLT C001, C005, C019, C025,
  C029, C030; WLTA C006, C011: owner w02c-p15-015; IRV C004, C016: owner
  w02c-p15-006) not written here (A14).
- Unit compile ok (overfull 3); check.py: only preexisting soft
  notation-scope / rule-outside-registry notes in the NDA hosts;
  fused-space check clean.
- Run r6 block 2 (2026-10-12): the assessment listed one gap, a dispute
  on WLTA C006 (thm:p15-coupon-collector-law, host body lines 151-154):
  the birthday reading, the source's "about 2153.46 tries" and the 5.89
  ratio of Durrett Example 2.2.7 are missing. WLTA is a readonly unit
  (owner w02c-p15-015) and both WLTA hosts are read-only here, so the
  text was written as patch requests, entries 7-8 of
  work/waves/w02ca/patches/w02ca-p15-016.json. Source reread this
  session: held PTE5 PDF page 68 = printed p. 60, Example 2.2.7 (coupon
  collector's problem): n = 365 read as people met until every birthday
  is seen; "about 365 log 365 = 2153.46 tries"; trials 5.89 times the
  number of birthdays. Computed: 365 log 365 = 2153.462534,
  log 365 = 5.899897 (the source's 5.89 truncates; rounding gives 5.90),
  365 H_365 = 2364.646023, H_365 = 6.478482, gap 211.183489.
  Entry 7 replaces body lines 151-154 (birthday reading under i.i.d.
  uniform birthdays, the tries claim, the ratio, exact-expectation
  qualification kept, no error bound at n = 365); entry 8 extends the
  annex numerics (annex:p15.coupon-collector-law) with the two ratios and
  the gap. No owner patch touches these anchors; both anchors unique.
- Drivers still do not input the owned files or w02c-p15-015's files;
  all nine patch anchors unique and unapplied. Unit compile ok
  (overfull 3); check.py: only preexisting soft notation-scope /
  rule-outside-registry notes in the NDA hosts; fused-space check clean
  on owned files and the patch text.
- Run r6 block 3 (2026-10-12): the assessment again listed only the
  WLTA C006 dispute (n = 365 example of Durrett Example 2.2.7). Source
  reread this session: held PTE5 PDF 67 = p. 59 opens Example 2.2.7;
  PDF 68 = p. 60 carries the birthday reading, "about 365 log 365 =
  2153.46 tries" and the 5.89 ratio. The supplying text is patch entries
  7-8 (zero-based) of work/waves/w02ca/patches/w02ca-p15-016.json; both
  anchors still unique and unapplied in the read-only WLTA hosts; no
  w02ca-p15-015 patch touches them; patched scratch copies pass the
  fused-space check. No new text written; the gap closes when the lead
  applies entries 7-8.
- Unit compile ok (overfull 3); check.py: only preexisting soft
  notation-scope / rule-outside-registry notes in the NDA hosts;
  fused-space check clean.
- Run r6 block 1, resumed 2026-10-13: the assessment again listed NDA
  C001, C010, C014 (owned unit), each "route pending" on this packet's
  owned files, plus disputes on readonly units (CLT C001, C005, C019,
  C025, C029, C030 and WLTA C006, C011: owner w02c-p15-015; IRV C004,
  C016: owner w02c-p15-006), not written here (A14). Owned body rechecked:
  C001 at 67-110 (def:p15-w02c-p15-016-attraction,
  thm:p15-w02c-p15-016-types, annex 6-40), C010 at 145-215 (annex
  42-205), C014 at 32-143 and 217-233. Drivers still do not input the
  owned files (p15.tex line 99 and annex/p15.tex line 98 are the
  insertion anchors); all nine patch anchors still occur once and are
  unapplied. No new text written; C001, C010, C014 stay blocked_policy on
  patch entries 5-6 (driver insertions), with 0-4 the host links.
- Unit compile ok (overfull 3); check.py: only preexisting soft
  notation-scope / rule-outside-registry notes in the NDA hosts;
  fused-space check clean.
- Run r6 block 2, 2026-10-13: the assessment listed NDA C014 (owned unit):
  the GK definition allows B_n real nonzero but the proofs used only
  positive scales. GK PDF 185-186 (pp. 171-172) reread: no sign
  condition on A_n, B_n; Theorem 1 for a "(proper) normal law" with the
  open-truncation ratio (1). Written: body lines 131-193,
  thm:p15-w02c-p15-016-normal-signs (sign reflection to a positive
  normalization to chi; free signs; converse; degenerate laws attracted
  to no proper normal law) and thm:p15-w02c-p15-016-gk-normal (Theorem 1
  both directions under the stated definition; point mass at c != 0
  shows nondegeneracy cannot be dropped); annex 42-172 full proofs;
  boundary updated (281-298). Symbols added (epsilon_n, sigma_n, N(m,v),
  Phi, R_F).
- Readonly-unit disputes (IRV C001, WLTA C006, OS C013) not written here
  (A14; owners w02c-p15-006, -015, -020). Guard G1 on
  spec/research/edition-2026-authoring-batch-intake-13.json: the file
  comes from the lead commit 6de06cc3 and has no working-tree change;
  this packet did not touch it.
- Unit compile ok (overfull 3); fused-space check clean.

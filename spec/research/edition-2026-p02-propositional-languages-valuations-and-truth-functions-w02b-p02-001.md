# w02b-p02-001 (P2 10.1, 10.2) research note

## Provenance

- Packet: work/waves/w02b/packets/w02b-p02-001.json, block 1, label_tag p02-w02b-p02-001.
- Assessment gap addressed: ED26-SRC-001-001 SETUP/DEVELOPMENT/CASES/APPARATUS, blocker "source_not_held SRC-001".
- Held file for SRC-001 (Barwise, "An introduction to first-order logic", Handbook of Mathematical Logic, 1977,
  ch. A.1, printed pp. 5-46): source/references/acq-r1-ACQ-2026-10-0497/schwichtenberg-1977-proof-theory-applications-cut-elimination.pdf.
  It IS listed in spec/coverage/edition-2026/held-sources.json (entries[681]; SHA-256 digest 0226941f94d7e7e2af4250662ddc37ff21e6df4b1bf4bbd374822ef5203a2aba;
  1186 PDF pages; version "Whole-book scan of the Eighth impression (1993) paperback of the 1977 North-Holland
  Handbook of Mathematical Logic ... 1977 pagination"), but only under the bibkey/source_index key
  Schwichtenberg1977. source_index has no SRC-001 key and ACQUISITION-LIST row ACQ-2026-10-0427 still reads
  not_held. The version matches the SRC-001 record (first edition 1977; 1993 impression facsimile, 1977 pagination).
- Opened in this session: text layer of PDF pp. 21-63 (printed pp. 5-47; printed p = PDF p - 16), read for the
  item inventory; page images read for printed pp. 5 (PDF 21), 18-19 (PDF 34-35), 23-28 (PDF 39-44; p. 28 also
  zoomed at 220 dpi), plus the OCR text of pp. 6, 17, 22, 44-46.
- Locators checked against the held file in this session (two or more per section): \S1 p. 6; \S2 2.1 p. 8,
  2.4/2.5 p. 10, 2.7 p. 12, 2.8 p. 15; \S3 3.1 p. 17, 3.2-3.3 p. 18, 3.4 p. 19, 3.5-3.7 p. 20, 3.8 p. 21,
  EC p. 22; \S4 p. 22-23 plan, 4.1 p. 25, 4.2 p. 26, Tychonoff/F_A p. 27-28, FO tautologies p. 28, 4.3/4.4 p. 29,
  4.5-4.7 p. 30, 4.8 p. 31, proofs of 2.4/2.5 p. 33, 4.9-4.11 p. 35, 4.12 p. 38, 4.13 p. 39, 4.14 p. 40;
  \S5 Hilbert's Thesis examples p. 41, 5.1-5.2 p. 42, 5.3-5.4 p. 43, 5.5 p. 44, 5.6-5.7 p. 45; References pp. 45-46.
  The numbered-item locators in the active host files (w02-p02-005 body and annex; list extracted by grep) agree
  with this inventory; the host's prose content was compared with the page images only for pp. 5, 6, 23-28 and
  45-46 (two discrepancies found, both on p. 28; see patches).

## Existing treatment found (A9)

The whole chapter is already hosted on the active route, in
handbook/parts/p02/propositional-languages-valuations-and-truth-functions-w02-p02-005.tex (1392 lines, input by
handbook/parts/p02.tex line 11) and its annex (1306 lines). This was not in the packet's "existing" list. The
w02-p02-005 return JSON (block 1) and its note's "Missing work" list are stale: later blocks hosted \S4, \S5 and
the apparatus. No second treatment was written; the new section here supplies what the chapter presupposes
without stating (readability over an arbitrary P, the recursion behind \bar v, coincidence, correctness of the
truth-table test), which neither the w02-p02-005 files nor the inherited 10.1/10.2 text cover for Barwise's P.

## Item-level host map for ED26-SRC-001-001 (Barwise 1977, ch. A.1, pp. 5-46)

Host H = handbook/parts/p02/propositional-languages-valuations-and-truth-functions-w02-p02-005.tex (labels
p02-w02-p02-005-*), annex HA; N = this block's files (labels p02-w02b-p02-001-*).

- p. 5 contents, support footnote: H sec bw-apparatus.
- p. 6 \S1 foreword (reader, Leibniz, historical names): H sec bw-apparatus, sec barwise-setup intro.
- pp. 6-9 \S2 logical symbols, group notions (1)-(8): H def bw-language, def bw-groups; 2.1 thm bw-divisible;
  2.2 thm bw-torsion-free; 2.3 thm bw-torsion (proof p. 11 in HA).
- p. 10 2.4 thm bw-compactness; 2.5 thm bw-ls; weak second-order LS/compactness remarks: thm bw-weak-so-ls.
- pp. 11-13 2.6 thm bw-reals; 2.7 thm bw-nonstandard; Archimedean/infinitesimal remarks: text at those results.
- pp. 13-15 rings, ideals (9), (9)', (10), fields, algebraically closed, extensionality: def bw-rings,
  thm bw-maximal, thm bw-pir; 2.8 thm bw-characteristic.
- p. 16 properties of theories (decidability/completeness claims), p. 17 referrals A.2-A.4: H paragraph after
  bw-characteristic, as attributed claims (no proof in ch. A.1; proofs in chs. C.1, C.3, D.1, outside this extent).
- pp. 17-22 \S3: L and arities def bw-language; 3.1 def bw-structure; 3.2-3.6 def bw-syntax; examples
  def bw-syntax-cases; 3.7-3.8 def bw-satisfaction; polynomial example def bw-polynomial; coincidence facts
  (cref lem:fol-coincidence); substitution proviso def bw-substitution; iso => elementarily equivalent
  thm bw-iso-equiv; axiomatizable, EC, EC_Delta: H lines 538-541.
- pp. 22-28 \S4 propositional part: plan sec bw-prop; prime/propositional formulas def bw-propformula and N
  (def letter-reading, thm letter-readability, warning string-primes, thm fo-skeleton); truth assignments,
  \bar v, truth table def bw-truth-assignment and N thm recursion; worked table def bw-table-two; 4.1 and listed
  tautologies def bw-tautology; "truth tables make it trivial" claim N thm truth-table with lem coincidence;
  three-letter table and backward method def bw-table-three; 4.2 thm bw-prop-compactness (both proofs HA);
  F_A equations p. 28 HA (misprint unflagged: patch 2); map colouring and Tychonoff-for-2^P thm bw-map-colouring;
  first-order tautology examples p. 28 H lines 727-737 (one displayed formula differs from the source: patch 1)
  and N example fo-tautologies.
- pp. 29-33: 4.3 thm bw-lemma-43; counterexample thm bw-43-converse; 4.4 def bw-equality-axioms; L(C), 4.5, 4.6
  def bw-witnessing; 4.7 thm bw-lemma-47; 4.8 thm bw-main-lemma; proofs of 2.4/2.5 via 4.8: HA bw-compactness,
  bw-ls (Barwise's route paragraphs).
- pp. 34-37: H def bw-system-h; 4.9 thm bw-completeness-h; 4.10 thm bw-soundness; 4.11 thm bw-lemma-411.
- pp. 37-40: def bw-sequents (rule figure p. 37); def bw-g-derivation (p. 38); 4.12 thm bw-g-prop-completeness;
  def bw-system-g; 4.13 thm bw-completeness-g; 4.14 stated as Barwise's claim only (H lines 1064-1080);
  exercise def/thm bw-exercise.
- pp. 41-45 \S5: Hilbert's Thesis and examples sec bw-beyond; 5.1-5.2 def bw-many-sorted, def bw-euclidean,
  thm bw-n-logic; 5.3 def bw-weak-so, thm bw-weak-so-ls, thm bw-countable-field; 5.4-5.5 def bw-infinitary,
  thm bw-extended-ls, thm bw-keisler-axioms; 5.6 def bw-abstract-logic; 5.7 stated, not proved (H 1335-1345).
- pp. 45-46 References: H sec bw-apparatus (seven entries, all keys in handbook.bib).

## Missing work (specific records)

1. Barwise 4.14 (Cut-Elimination for G, p. 40): no proof on the route. Barwise indicates a direct completeness
   proof for G expanding the proof of 4.12, after Smullyan 1968; the handbook's thm:p07-cut-elimination is for a
   different calculus. Needed: a proof of 4.14 for Barwise's G (sets-of-formulas sequents, his equality and
   quantifier rules) along that route.
2. Barwise 5.7 (Lindstrom, p. 45): the chapter gives no proof (referral to Barwise 1974, ch. "Axioms for abstract
   model theory", pp. 221-265). Hosted as stated claim; a proof needs that source (Barwise1974Axioms; ACQ-2026-10-0032
   failed, not held).
3. p. 16 claims (decidability of abelian groups, undecidability of groups, completeness of ACF_p, decidability
   of C, undecidability of Z): attributed claims; proofs lie in other chapters of the same handbook.
4. Patch requests (work/waves/w02b/patches/w02b-p02-001.json): (1) H's second first-order tautology must be
   Barwise's \neg(\forall xR(x)\land\exists xS(x))\leftrightarrow(\neg\forall xR(x)\lor\neg\exists xS(x));
   (2) HA must identify the correction of Barwise's misprint F_(A->B) = F_B - F_A.
5. Registry (lead): add source_index key SRC-001 (and Barwise1977FirstOrder) -> the held whole-book path in
   spec/coverage/edition-2026/held-sources.json, and update ACQ-2026-10-0427 status for ch. A.1.

## SRC-007-001

Hodges, "Elementary Predicate Logic", HPL 2nd ed. vol. 1 (Kluwer 2001), pp. 1-129, doi 10.1007/978-94-015-9833-0_1:
not in held-sources.json (no file found under source/references by title or DOI); ACQ-2026-10-0433 not_held.

## Decisions

- No new symbols: \mathbf t, \mathbf f, \bar v are registered by the w02-p02-005 intake; \circ is the metavariable
  already used in the inherited text. No new bib keys (Barwise1977FirstOrder is in handbook.bib).
- The disjointness of Barwise's symbol classes (p. 17-18) is stated as an explicit added hypothesis of
  thm:p02-w02b-p02-001-fo-skeleton, marked as not stated by the chapter.

## Continuation

Block 1 (earlier): body 1-270, annex 1-255 (readability, recursion, coincidence, truth tables).

Continuation (this session, gap ED26-SRC-001-001-DEVELOPMENT, Barwise 4.14):
- Held file re-opened: page images of printed pp. 21, 22, 37, 38, 39, 40 (PDF pp. 37, 38, 53-56) of
  source/references/acq-r1-ACQ-2026-10-0497/schwichtenberg-1977-proof-theory-applications-cut-elimination.pdf
  (110 dpi), plus text layer of PDF 53-57. Locators used: p. 21 (term coincidence remark), p. 22 (substitution
  assumption and renaming remark), p. 37 (sequents, Gamma,phi = union, propositional rules), p. 38 (proof of 4.12,
  truth assignment on an end node), p. 39 (equality axioms and rule, quantifier rules, eigenvariable condition,
  G and G+), p. 40 (4.14 and the route via a direct completeness proof for G, Smullyan 1968).
- Written: body sec:p02-w02b-p02-001-g-completeness (lines 272-556): def g-valid, convention g-reading, lemma
  g-substitution, method g-search, thm g-completeness, cor g-cut-elimination (Barwise 4.14 for sequents that
  separate their variables, and 4.13 with G in place of G+ for sentences without same-variable nesting), example
  g-example, warning g-limit. Annex sec:annex-p02-w02b-p02-001-g-completeness (lines 257-682): annexitems
  g-substitution, g-completeness, g-cutfree.
- Decision (recorded in reader as def g-reading and def g-limit): under Barwise's p. 22 convention plus the host's
  reading of phi(y) in (|-forall)/(exists|-), the sequent {forall z R(z), S(y)} |- forall y (R(y) & forall y R(y))
  is valid but no (|-forall) instance concludes it. The written completeness proof therefore carries the
  hypothesis "separates its variables" (no variable both quantified and free in the sequent; no same-variable
  quantifier nesting). Remaining, in the duty's words: "every sequent true in all structures is derivable in G"
  and "4.14 ... any sequent with a derivation using cut has one without cut" are not established for sequents
  that do not separate their variables; settling them needs either a proof for those sequents or a lead decision
  on the reading of phi(y) (alpha-renaming) in G.
- Proof route: semantic (non-derivability saturation with a fair schedule; equality handled only by the
  right-side backward use of the equality rule; countermodel on U/~ where ~ is interchangeability in atomic
  right-side formulas). Soundness of G+ is taken from the annex proof of thm:p02-w02-p02-005-bw-completeness-g.
- Patch request added: work/waves/w02b/patches/w02b-p02-001.json entry 3 (w02-p02-005 body line 1075
  "Neither route is carried out ..." -> cross-reference to the new section).
- Symbol intake written (local notation of the proof).
- Checks: unit-compile ok, 0 overfull; fused-space check clean; check.py --tree handbook shows no finding in
  this packet's files.
Next: lead applies the three patches and the held-sources mapping; open item above (sequents not separating
variables) awaits a decision or further proof.

Continuation (r3 session, gap ED26-SRC-001-001-DEVELOPMENT, annex proofs for the general case of 4.14):
- An intervening session had added body subsection sec:p02-w02b-p02-001-g-variants (body 607-705: thm
  g-clean-failure, def g-variant, def g-variant-reading, lemma g-variants, thm g-variant-cut-elimination) and
  updated def g-limit, but wrote no annexitems; the proved= targets were undefined.
- Written now in the annex, subsection sec:annex-p02-w02b-p02-001-g-variants (annex 684-1000):
  annex:p02-w02b-p02-001-g-clean-failure (validity; explicit G+ derivation with one cut on
  forall x forall z P(xz), lines L1-L5, R1-R3, C; no G derivation via a least-height argument over the class of
  sequents with left side in A = {chi_0} u {forall y P(ty): y not in t} u {P(tt'): y not in t}, right side within
  {P(yy)}); annex:p02-w02b-p02-001-g-variants (renaming step preserves satisfaction via clean-substitution part 4
  and lem:fol-coincidence; replacement by induction; variant construction by induction with FV preserved;
  separating variant of a sequent); annex:p02-w02b-p02-001-g-variant-cutfree ((ii)=>(i) trivial, (i)=>(iii)
  soundness through variants, (iii)=>(ii) relabel the root of the derivation from g-completeness; consequence for
  T |= phi via 4.13).
- No new locators introduced (only cross-references); annexitem title of g-variant-cutfree shortened to avoid
  an overfull line.
- Patch 3 text updated to name the clean-failure and renaming-reading theorems.
- Symbol intake: QV, phi^*, mathcal C added (annex-local scopes).
- Checks: unit-compile ok, 0 overfull; find_fused_spaces clean; check.py --tree handbook shows no finding in this
  packet's files.
Next: lead applies patches 1-3, the held-sources mapping and the driver insertion (placement in the return JSON).
Remaining open in DEVELOPMENT: Barwise 5.7 (Lindstrom) proof route, source Barwise 1974 not held.

Continuation (r4 session, gap ED26-SRC-001-001-DEVELOPMENT, Barwise 5.7):
- Hard guard G1 (files changed outside the owned set): the four flagged files
  spec/research/edition-2026-p01-symbol-registry-w02b-p01-014{.md,-return.json} and
  spec/research/edition-2026-p02-fol-metatheorem-table-and-nd-cpl-sheet-w02b-p02-036{.md,-return.json} are untracked
  files owned by packets w02b-p01-014 and w02b-p02-036 (timestamps 2026-10-04 18:23 and 22:05). This packet never
  wrote them and did not touch them in this session; reverting or deleting them would destroy another agent's work.
  The attribution is the guard's; the lead should re-attribute.
- Held file re-opened: text layer of PDF pp. 26, 27, 33, 61, 62 and page images of printed pp. 10 and 45
  (PDF 26, 61) of the held whole-book scan. Locators used: p. 10 (2.4, 2.5, remark on finite or countable L),
  p. 17 (L of any size; function, relation, constant symbols), p. 45 (5.6 informal notion of logic, referral to
  Barwise 1974, the LS theorem with kappa = aleph_0 for other logics, L(Q) with Q = uncountable, 5.7 statement).
- Found on the route: thm:p03-lindstrom (handbook/parts/p03/preservation-abstract-logic.tex 458, proved by
  annex:p3.abstract.3 in handbook/annex/p03/editorial-proofs.tex 358 ff.), the relational regular-abstract-logic
  notion of sec:p02-fol-metatheorem-summary, and thm:p03-keisler-q-one (cited). The host w02-p02-005 refers only
  to the cited thm:lindstrom and says 5.7 is not proved.
- Written: body sec:p02-w02b-p02-001-lindstrom (lines 742-898): def lindstrom-reading, cor barwise-lindstrom,
  lemma lindstrom-sharp, example lindstrom-example, warning lindstrom-limit. Annex
  sec:annex-p02-w02b-p02-001-lindstrom (1001-1083): annex barwise-lindstrom (hypotheses of thm:p03-lindstrom from
  2.4 and 2.5 with kappa = aleph_0), annex lindstrom-sharp (Qx(x=x) not first-order; failure of 2.4 for L(Q) over
  P plus aleph_1 constants).
- Patch request 4 added: host sentence "neither 5.7 nor that theorem is proved in this section" -> cross-reference.
- Symbol intake: \mathcal L^{\ast} (overlap with the P2 clausal-composition registry row; keep scoped), c_alpha.
- Remaining in DEVELOPMENT: (a) Barwise's own proof route for 5.7 (Barwise 1974, not held); (b) 5.7 for a logic
  with only the closure properties Barwise names (no relativization) is not established; (c) the passage from
  relational signatures to Barwise's signatures with function symbols is not carried out.
- Checks: unit-compile ok, 0 overfull; find_fused_spaces clean; check.py --tree handbook shows no finding in this
  packet's files.

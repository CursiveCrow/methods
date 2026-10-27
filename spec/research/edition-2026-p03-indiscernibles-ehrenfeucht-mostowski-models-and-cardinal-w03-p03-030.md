# w03a-p03-030: section 31.9, self-extending models and infinitary indiscernibles

Packet: work/waves/w03a/packets/w03a-p03-030.json (block 1, author).
Label tag: p03-w03-p03-030. Heading level: \chapter. toc tag: `%% toc: P3 31 31.9`.

## Files

- Body: handbook/parts/p03/indiscernibles-ehrenfeucht-mostowski-models-and-cardinal-w03-p03-030.tex
- Annex: handbook/annex/p03/indiscernibles-ehrenfeucht-mostowski-models-and-cardinal-w03-p03-030.tex
- Intake bib: handbook/bib/intake-p03-indiscernibles-ehrenfeucht-mostowski-models-and-cardinal-w03-p03-030.bib (key Schmerl1985TransferTheorems)
- Symbol intake: handbook/registry/symbols-intake-p03-indiscernibles-ehrenfeucht-mostowski-models-and-cardinal-w03-p03-030.csv
- Insertion (packet proposal, executed by the lead): body after `\input{parts/p03/classification-theory}` (p03.tex line 69); annex after `\input{annex/p03/editorial-proofs}` (annex/p03.tex line 8).

## Source read (online, this session)

- Held artifact SRC-049 (pageplace preview) lacks Chapter V; not used for locators.
- Read: Schmerl, "Transfer Theorems and Their Applications to Logics", ch. V of Barwise and Feferman (eds.), Model-Theoretic Logics, Springer 1985 (first edition), pp. 177-209. The open-access copy is on Project Euclid (Perspectives in Logic 8, copyright 1985 ASL). Its table of contents is at https://projecteuclid.org/euclid.pl/1235417263, which redirects to /ebooks/perspectives-in-logic/Model-Theoretic-Logics/toc/pl/1235417263. The chapter PDF was urlId pl/1235417270.
- How it was read: a plain curl/WebFetch returned a bot interstitial, which was not bypassed. The ordinary in-app browser loaded the page normally. The chapter PDF was fetched in the page and parsed with pdf.js in the browser. Text was extracted for pp. 177-209, and page images were rendered and viewed for pp. 179, 202-204 and 206-208, to check the formulas. Nothing was saved to disk.
- Pages actually read: 177-179 (Def 1.1.1, 1.2.1), 200-209 (Def 5.2.1, 5.2.5-5.2.9, all of section 6, section 7).
- Reader text states once that the presentation follows the 1985 edition.

## Locators used (all seen this session)

p. 179 Def 1.2.1; p. 200 Def 5.2.1; p. 202 start of section 6, section 6.1 property (1); p. 203 property (2), the canonical extension, Def 6.1.1, "large sets become larger"; p. 204 Thms 6.1.2, 6.1.3, Def 6.1.4, Thms 6.1.5, 6.1.6; p. 205 the iteration and the 6.1.6 sketch; p. 206 Thm 6.2.1, the induction scheme, Thm 6.2.2; p. 207 proof (tuple orders, conditions, theta_n); p. 208 L, S, sigma_n; p. 209 Thm 7.2.2.

## Source corrections and readings (recorded in reader text)

1. Monotonicity scheme (p. 203): the antecedent is written with an explicit universal quantifier over x.
2. Bounded scheme (pp. 204, 206): forall z is read as governing the whole implication.
3. theta_n (p. 207): the printed last disjunct "y <= z" makes the formula unsatisfiable, because w := y satisfies the antecedent while z < y. It is read as "y <= w".
4. theta_n vs theta_{n-1} on pp. 207-208 (the large-class text and S use theta_n where theta_{n-1} is required). y' in S is read as the bound variable v.
5. Def 6.1.4 continuity condition at alpha = 0: applied to nonzero alpha only.
6. Def 1.2.1 states only the initial-segment condition via Q in the kappa-interpretation. The handbook definition adds |A| = kappa explicitly; the cardinality clause is not attributed to the source.

## Hypotheses added relative to the source (stated in reader text; not hidden)

- Thm 6.2.2 / end-extension corollary: the proofs here also assume the least-number principle. The source assumes the induction scheme only, plus the Skolem convention. Not proved here: the IS-only version and the source's remark that adjoining definable terms yields a Skolem theory.
- Lemma end-extension (2) uses `forall y Qx (y<x)` besides the regressive scheme. The source asserts the end-extension and least-new-element properties for the 6.1.6 sentences without proof.

## Results written by this author

Proved in the annex: the ultrafilter facts; the canonical extension (Łoś, uniqueness, elementarity, cardinality); large sets become larger; the hull lemma (downward LS for self-extending theories); unions of chains; end-extension and least new element; the strongly lambda-like iteration (source p. 205); indiscernibility of the generators, which is not in the source; the N example lemma; tuple orders, including collection; the tree / leftmost large branch; Thm 6.2.2 under IS+LNP; the end-extension corollary; and the countable case of Thm 6.2.1.

## Not written (open)

- Thms 6.1.2, 6.1.3, 6.1.5, 6.1.6 (two-cardinal, n-Mahlo and n-subtle hypotheses) and their proofs. The source sketches 6.1.6 only. These are named in the limitations warning without statement as results.
- (closed in w03a block 1) Thm 6.2.1 for uncountable mu.
- Thm 6.2.2 under the induction scheme alone.
- Infinitary versions (section 7.2, Thms 7.2.1-7.2.3).
- (closed in w03a block 1) MacDowell-Specker for PA.
- Unit ED26-SRC-049-0005 (C001-C007) belongs to w03-p03-029 by readonly_units. The C006 material above was written under the 31.9 section duty MP-0. The owner should cite these labels rather than duplicate section 6 (crosslink request in the return).

## Existing treatment search (A9)

Searched the handbook for self-extending, MacDowell, Specker, end-extension, Hanf, and Erdős–Rado. There is no prior treatment of self-extending models or MacDowell-Specker-Shelah. The related existing material is the listed finitary EM interval (classification-theory.tex, thm:p03-ehrenfeucht-mostowski, def:p03-order-indiscernibles), which is linked. Also linked: thm:elementary-chain (restoration/inherited-06432-06493.tex), thm:fol-compactness, thm:downward-ls and thm:p01-ultrafilter-lemma. Found but not listed in the packet's existing list: n-a-006-01.tex (Morley chain material, first-order) and qe-categoricity-games-supplement.tex 139-154 (Vaught two-cardinal, owned by 029). Neither treats self-extending models.

## Block 1 (w03a, 2026-10-12) additions

Source re-read this session: the same Project Euclid open-access copy of the 1985 edition (chapter PDF urlId pl/1235417270), fetched in the in-app browser and parsed with pdf.js. No bot check was bypassed. Pages read as text: 177-180 (Def 1.1.1, the mu-compactly notion, Def 1.2.1, the remark that (omega,<) is the only aleph_0-like order on p. 179, Def 1.3.1 on p. 180), 206-209 (Thm 6.2.1, 6.2.2, proof, section 7).
- The inequalities in Thm 6.2.1 (p. 206) were checked on the page image, by a pixel profile of the two glyphs in the scanned bitmap. The first is <= and the second is strict <, so the theorem reads "if aleph_0 <= mu < lambda, then aleph_0 -> lambda mu-compactly". The earlier body text "aleph_0 <= mu <= lambda" was wrong and has been corrected. Example def:p03-w03-p03-030-example-mu-lambda shows that mu = lambda fails.
- Section 7.2 (p. 209): Thms 7.2.1-7.2.3 are stated without proof (each ends with a box). The limitations warning now describes them with the p. 209 locator. No proof is written.

New, with annex proofs:
- thm:p03-w03-p03-030-compactness: compactness for weak L(Q) structures, by translation to first-order logic plus extensionality axioms.
- thm:p03-w03-p03-030-pa: MacDowell-Specker for PA. It derives the order facts, IS and LNP in PA, then applies end-extension-pa. The PA definition in the routed Part V restoration has no label, so PA is described inline and def:language-arithmetic is cref'd.
- thm:p03-w03-p03-030-transfer-mu: Schmerl Thm 6.2.1 in full, for all aleph_0 <= mu < lambda. This is a handbook route, not the source's: one nonprincipal ultrafilter on N, least-witness expansions of the omega-type approximations, L(Q) compactness, the hull, then a lambda-step chain of canonical end-extensions. It does not need Thm 6.2.2.
- def:p03-w03-p03-030-example-mu-lambda: the failure case mu = lambda.

## Block 2 (w03a, 2026-10-13) additions

Guard: the reported G3/G4 failure was a timeout of `tools/check.py --tree handbook` at 180 s. Rerun this session: the whole-tree check completes in about 152 s (2 min 32 s wall clock) and, filtered to this packet's files, shows only the bib-key finding for Schmerl1985TransferTheorems (intake key). The timeout is tool runtime over the whole tree, not a finding in these files; a longer guard timeout or a file-filtered check mode is a tooling change for the lead.

No source pages were re-read this session; no new locator was written. New material is handbook mathematics:
- thm:p03-w03-p03-030-is-successor (body 600-615, annex 830-868): over the induction scheme, nonempty bounded definable sets have maxima, nonzero elements have predecessors, and the least-number principle is equivalent to the single sentence that every element has an immediate successor. Full proof.
- def:p03-w03-p03-030-example-one-plus-z (body 617-660): the order {e} + Z. Every expansion satisfies the induction scheme; LNP fails; a Skolem expansion (witness functions from a fixed listing, no choice) exists, so IS-only Skolem theories that Thm 6.2.2 of the source covers and thm:p03-w03-p03-030-mss does not really exist; and no expansion by parameter-free definable functions is Skolem (shift automorphism). The source remark (p. 206, as recorded in block 0/1 reading) that adjoining definable terms yields a Skolem theory is thereby shown to need more than IS when the terms are parameter-free; other readings of the remark are not checked.
- Remark after thm:p03-w03-p03-030-mss and after the end-extension corollary updated to cite the lemma and example.

## Continuation

State at return of w03a block 2: body 1-809, annex 1-1117. unit-compile ok (17 overfull boxes); fused-space check clean; tree check filtered to these files shows only the intake bib-key. Still open:
1. Thm 6.2.2 and its end-extension corollary for Skolem theories with the induction scheme but without the least-number principle (equivalently without immediate successors everywhere). The block-2 example shows such theories exist; a proof needs a tree argument that avoids least elements, e.g. using greatest elements of bounded sets and immediate predecessors (both available under IS) in place of least elements. Not attempted to completion.
2. Thms 6.1.2, 6.1.3, 6.1.5, 6.1.6 (two-cardinal, n-Mahlo, n-subtle). Source gives only a sketch for 6.1.6 (pp. 205-206). Needs Schmerl 1976 / Schmerl-Shelah 1972 or another source with full proofs.
3. Thms 7.2.1-7.2.3 (p. 209), stated without proof in the source. Needs Keisler 1966b and admissible-fragment sources.

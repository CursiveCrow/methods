# w02-p02-035: sections 21.4-21.7, decision procedures for the decidable fragments

## Provenance

Held sources opened in this session (text extracted with pdftotext; formula pages
rendered to images and read):

- BorgerGradelGurevich1997: source/references/acq-r1-ACQ-2026-10-0056/borger-gradel-gurevich-1997-classical-decision-problem.pdf
  (author TeX file dated 1996-10-07; printed folio = PDF page - 7).
  Pages read: 112 (Thm 3.1.23), 242-246 (Def 6.1.1, Thm 6.1.2, Def 6.1.5, Thm 6.1.6),
  249-262 (Sect. 6.2.1: Prop 6.2.1, Cor 6.2.2, Ex 6.2.3, Prop 6.2.7, Cor 6.2.8,
  Prop 6.2.9, Cor 6.2.10, Thm 6.2.13, Cor 6.2.14 + Remark; Sect. 6.2.2: Prop 6.2.17,
  Thm 6.2.19-6.2.21), 310-311 (historical remarks: forall^3 exists, forall exists forall
  reduction classes).
- GradelKolaitisVardi1997: author preprint 1997-01-20 (gkv-1997-two-variable.ps2pdf.pdf).
  All 16 pages read. Locators used: sect. 2 (p. 3), pp. 4-6 (Sect. 3, Prop 3.1),
  Def 4.1, Def 4.2, Thm 4.3 (pp. 6-10), Thm 5.1, Thm 5.3, Cor 5.4 (pp. 10-11),
  p. 11 extensions paragraph, p. 1 (FO3 undecidable), p. 10 (two-bank remark).
  NOTE: GKV do not prove the lower bound; they cite Fuerer 1981b. The hardness proof
  is written from BGG Thm 6.2.13, whose sentence is a two-variable monadic sentence
  (BGG Remark after Cor 6.2.14 states the transfer to L2).
- Gradel1999: author preprint "Revised version July 1998" (ps2pdf). Read so far:
  outline of numbered results, p. 5 and Lemma 2.3 (constants), Sect. 5.2-5.3
  (Thm 5.8, Cor 5.9, Thm 5.10). Sections 3-4 (tree model, FMP, complexity) NOT yet
  read in detail.

Proofs written by the handbook (own constructions, not the source's):
- 2^m colour-collapse proof (BGG leaves it as Ex. 6.2.3).
- Monadic NEXPTIME upper bound via colour-set guessing in 2^{O(n^2)} (the source's
  sharper 2^{cn/log n} bound is cited, not reproduced).
- Padding lemma (domino NEXPTIME-hard under polynomial reductions) from imported
  BGG Thm 6.1.2.
- Arity-reduction well-definedness argument and the O(s) naming device (GKV only
  say "easy to verify").
- BSR grounding with equality patterns (avoids congruence-axiom blow-up), and a
  BSR NEXPTIME-hardness reduction using two existential constants and 2n-ary tile
  predicates (polynomial, not the source's sharper 2^{cn} bound of Thm 6.2.21).

Imported premises (proofboundary def:p02-w02-p02-035-domino-import): BGG Thm 6.1.2
(machine-to-tiling simulation; source itself leaves V as an exercise), simple-machine
normalization (p. 243), multitape-to-one-tape quadratic simulation (p. 246).

Existing treatments found: handbook/parts/p02/first-order-depth.tex 158-275 (catalog,
listed); handbook/parts/p09/presentations/n-c-005.tex, n-c-006.tex, n-c-007.tex
(source presentations; not listed in packet "existing"); handbook/parts/p14/
decidability-and-complexity.tex tab:p14-dc-finite (not listed);
handbook/parts/p15 + annex/p15/hintikka-inductive-logic.tex (monadic constituents;
named in the assessment). The new section links to all of these rather than
duplicating them. n-c-006.tex uses BSL page numbers (pp. 53-69) that are not the held
preprint's pagination; not editable here.

Host table changes go through work/waves/w02/patches/w02-p02-035.json (11 items).

## Provenance, block 2 (guarded fragment)

- Gradel1999 held file: source/references/acq-r1-ACQ-2026-10-0172/gradel-1999-restraining-power-guards.ps2pdf.pdf
  (author preprint "Revised version July 1998", 26 pp.; derived ps2pdf of the held .ps).
  Read in this session: all pages as text; pages 4-12 and 14-19 rendered and read as images.
  Locators used: sect. 2 (FO convention: relational, equality and constants), def. 2.1,
  lem. 2.3, lem. 3.1 and the remark after it, defs. 3.2, 3.3, 3.5, lem. 3.4, lem. 3.6,
  thm. 3.7, def. 3.8, thm. 3.9, thm. 3.10 and the remark after it, sect. 4.1 (defs. 4.1,
  4.2, ATM game, Aspace = Dtime equation citing Balcazar-Diaz-Gabarro ch. 3), thm. 4.3,
  proof of thm. 4.4, cor. 4.5 and the equality-elimination paragraph, cor. 4.6,
  thm. 5.8, cor. 5.9, thm. 5.10, sect. 2 transitivity example. Page numbers of the
  preprint are not used in reader text (bib key may point to the JSL version).
- Source defect found: in the proof of thm. 4.4 the printed phi_n requires S1/S2
  successors at every T-node (4th conjunct) while Succ forces D(c,d)=D(a,b)+1 with a
  0-bit (5th conjunct); D is bounded by 2^(2^n), so no model exists. The handbook
  sentence drops the counter, requires successors only at existential/universal nodes,
  and uses the halting normalization (stated by the source on p. 15). Also the NEXT
  inscription conjunct prints Exyabyy'cd (typo for Exx'abyy'cd).
- Handbook's own work (not the source's): psi-types over At_k(psi) (substitution
  instances of psi's atoms) instead of full atomic types, so the bounded-variable
  EXPTIME bound needs no arity reduction; deterministic type elimination instead of
  the source's alternating test; equality-free acceptance sentence with diff in place of
  less/inequality; GF_2 arity-2 EXPTIME-hardness sentence written out (source sketches it).
- Convention: guards are relation atoms (catalog row convention). Source def. 2.1 says
  "atomic"; the source's lem. 3.1 first step (append z to every relation atom) does not
  work for equality guards, which is the stated reason in reader text.
- Constants: lem. 2.3 is stated as linear time by the source; the handbook proves only
  polynomial time (each atom grows by k symbols, O(n^2)).
- Imported premises: Herwig's theorem as stated by the source (thm. 3.9), restricted to
  relation-atom liveness (def:p02-w02-p02-035-herwig-import); ASPACE(s)=DTIME(2^O(s)) and
  ATM normalization (def:p02-w02-p02-035-alternation-import).
- Existing treatments: catalog row first-order-depth.tex (listed); P9 n-c-007.tex 59-111
  (Gradel presentation, linked); P14 decidability-and-complexity.tex tab:p14-dc-finite
  GF rows (linked via relationships paragraph); P9 thm:p09-modal-guarded (linked).

## Provenance, block 3

- Gradel1999 held file re-opened (pdftotext of the ps2pdf): lem. 2.3 (p. 5 of the preprint),
  sect. 4 "Subfragments that are in EXPTIME" paragraph and cor. 4.6 (preprint p. 19).
  Cor. 4.6 is stated for the source's language, which has constants; its proof is a sketch
  (bounded arity gives 2^{p(n)} atomic types).
- Handbook's own work: thm:p02-w02-p02-035-gf-bounded-constants (EXPTIME with constants for
  bounded variables or bounded arity). Proof: isolated-element preservation for guarded
  sentences; equality-pattern enumeration; flattening via Steps 1-2 of the normal-form proof
  checked with constants present; split translation sp_sigma (each variable either a named
  element or a variable over unnamed elements; atoms R(t) -> R_kappa(star places)); truth
  lemma; enumeration of ground-pattern valuations; reduction to the constant-free bounded case
  of thm:p02-w02-p02-035-gf-upper. Not taken from the source.
- GF_2 EXPTIME-hardness annex proof rewritten in full (step lemma, induction on height,
  strategy-tree model). Defect in the previous GF_2 sentence fixed: the cell-preservation
  conjunct (not Z_r x and P x) -> P y needed exclusivity of Z, which "imposes" does not give;
  replaced by (Z_r' x and P_{sigma,r} x) -> P_{sigma,r} y for r /= r' (O(S^2) conjuncts).

## Continuation

Block 3 written (not reviewed):
- G1 (spec/research/edition-2026-p02-unit-accounting-w02-p02-042*.{md,json}): these belong to
  packet w02-p02-042; this packet did not create or modify them, and they are not present in
  the tree at the time of this block. Nothing to revert from here.
- Open item 1 of block 2 (EXPTIME with constants) closed: body corollary at
  sec:p02-w02-p02-035-gf (body lines 706-736), annex item lines 932-1176.
- gf-hard statement now says EXPTIME-complete with or without constants (body ~line 838).
- Patch item 4 (GF row constants) extended to cite the new corollary.

Open items:
1. Catalog row changes in first-order-depth.tex await the lead applying the patch file.
2. Overfull boxes in the unit build (29 reported by unit-compile).

# w03a-p03-055 (P3, section 39.2): definitional complexity and expressibility

Packet: work/waves/w03a/packets/w03a-p03-055.json, block 1, 2026-10-11.
label_tag p03-w03-p03-055; heading \chapter; toc tag `%% toc: P3 39 39.2`.

## Duty addressed

Section-level MP-0 for 39.2 (as relayed): classify finite-structure concepts by
the logics that define them; quantifier-rank and variable-number hierarchies;
finite-variable logics and their pebble-game characterization; written proofs
of the Ehrenfeucht-Fraisse theorem and of the connectivity invariant and
response lemma.

All 35 packet component_ids belong to units ED26-SRC-050-0001 and
ED26-SRC-050-0002, which `readonly_units` assigns to w03-p03-054. Nothing
source-specific to those units (Weinstein ch. 1; Kolaitis ch. 2 of the 2007
book) was written here; the Kolaitis 2003 manuscript is used only as a general
authority for the section, with its own locators.

## Existing treatment found that the packet did not list (A9)

- handbook/parts/p03/comparison-games-and-infinitary-languages-w03-p03-038.tex
  (packet w03a-p03-038, same wave, not yet on the driver route): pointed EF
  theorem with full proof (thm:p03-w03-p03-038-pointed-ef), records and
  characteristic formulas (def/thm:p03-w03-p03-038-records, -finite-records,
  -characteristic), finitely many formulas per rank, the proved game criterion
  (thm:p03-w03-p03-038-criterion), and the cycles distance invariant, response
  lemma and connectivity theorem with m_k = (k+1)2^{k+2}
  (def:p03-w03-p03-038-cycles, thm:p03-w03-p03-038-cycle-response,
  thm:p03-w03-p03-038-connectivity). Its patch file
  work/waves/w03a/patches/w03a-p03-038.json already proposes the host pointers
  for thm:p03-ef, thm:p03-ef-inexpressibility and def:p03-ef-connectivity.
- A first draft of this block wrote its own W_m / Hintikka-formula EF proof, a
  W_m-to-sim_m bridge, and a cycles response lemma. On finding the 038
  treatment these were removed (A9: no second treatment) and the section now
  cites the 038 labels. Packet w03-p03-058 had meanwhile referenced the removed
  label thm:p03-w03-p03-055-cycles (058 body line 539): crosslink request filed.
- Also linked: sec:p03-ef-games (host), def:p03-w03-p03-039-language,
  def:p03-w03-p03-039-partial-iso, thm:p03-w03-p03-039-iso-invariance,
  sec:p03-finite-model-theory.

## What the owned files contain (new content)

Body handbook/parts/p03/finite-models-definability-and-descriptive-complexity-w03-p03-055.tex
- def:p03-w03-p03-055-setting, -query, -logics (FO^k, L^k_{infty omega},
  equiv_m, equiv^k, equiv^k_{infty omega}).
- thm:p03-w03-p03-055-rank-variables (rank m sentences are FO^m; formulas with
  n free variables use X_{n+m}).
- thm:p03-w03-p03-055-rank-definability (Kolaitis Thm 3.15 / Method 3.16:
  closure under equiv_m iff rank-m definability; completeness of game method),
  proved from the 038 records and characteristic formulas.
- def:p03-w03-p03-055-ef-strategy-reading (example).
- def:p03-w03-p03-055-pebble; thm:p03-w03-p03-055-pebble (Kolaitis Thm 7.9,
  Barwise/Immerman: winning family iff equiv^k_{infty omega}, arbitrary
  structures; iff equiv^k on finite structures) with complete proof (the
  manuscript gives an outline only).
- thm:p03-w03-p03-055-k-definability (Kolaitis Cor 7.10).
- thm:p03-w03-p03-055-unbounded (Kolaitis p. 52 remark, proved).
- thm:p03-w03-p03-055-cliques (Kolaitis Ex 7.5; strictness of variable and rank
  hierarchies via sigma_{>=k+1}).
- thm:p03-w03-p03-055-orders (FO^2 cardinalities on linear orders; Kolaitis
  p. 53 and Ex 7.6; even cardinality in L^2_{infty omega}).
- thm:p03-w03-p03-055-connectivity (2-colorability not FO on finite graphs via
  038's strategy with m odd; connectivity in L^3_{infty omega}; Spoiler wins
  3-pebble game on C_{2m}, C_m + C_m).
- def:p03-w03-p03-055-limits (warning), Relationships paragraph.

Annex handbook/annex/p03/finite-models-definability-and-descriptive-complexity-w03-p03-055.tex:
one annexitem per proved= result above (9 items).

## Sources read in this session

Held:
- source/references/acq-r1-ACQ-2026-10-0472/graedel-2007-fmt-descriptive-complexity-ch3.pdf
  (author-hosted chapter 3, running pages 125-230). Read: section 3.1 opening
  and 3.1.4 (p. 133: Lemma 3.1.4 width/renaming; Thm 3.1.5 alternating model
  checking); page range of section 3.1 = pp. 125-138 (3.2 starts p. 138).
  Cited as Gradel2007FMTDescriptiveChapter (new intake key).

Online (sources_read_online):
- https://dbai.tuwien.ac.at/staff/pichler/dbt/kolaitis.pdf -- Kolaitis, "On the
  Expressive Power of Logics on Finite Models", manuscript dated 1 August 2003,
  83 pp. (TU Wien course page; institutional host). Read: contents (p. 2),
  section 2 (pp. 3-5: Defs 2.1, 2.3), section 3 (pp. 8-21: Defs 3.1, 3.4-3.6,
  Thm 3.8, 3.10, Def 3.11, Lemma 3.12, Thms 3.14, 3.15, Method 3.16, Props
  3.17-3.18, Ex 3.19, Thm 3.20, Cor 3.21, Defs 3.22-3.25, Thm 3.26, Method 3.27,
  Props 3.28-3.30), section 7.1-7.2 (pp. 52-59: Def 7.1, p. 53 FO^2 example,
  path formulas pp. 53-54, Thm 7.2, Defs 7.3, 7.4, Exs 7.5-7.7, Def 7.8,
  Thm 7.9 with outline, Cor 7.10). Cited as Kolaitis2003ExpressivePowerNotes.
  The 2007 printed chapter with the same title was not read; nothing is
  attributed to it.

Key overlap (proposed decision): packet w03-p03-056 cites the same two
documents under Kolaitis2003ExpressivePowerManuscript and
Gradel2007FMTChapter3AuthorPDF; w03-p03-058 cites Kolaitis2003ExpressivePowerNotes.
The finalizer should merge each pair to one key.

## Symbols

handbook/registry/symbols-intake-p03-finite-models-definability-and-descriptive-complexity-w03-p03-055.csv.
Overlap: equiv_m here has the role of 038's equiv_k (FO rank agreement); the
equiv_alpha of def:p03-w03-p03-039-approximants / def:p03-morley-approximants is
infinitary rank agreement. Proposed: register one row for FO rank agreement
(038 and 055 share it) with a note on the infinitary approximant glyph.

## Open items

- None of the 35 packet components (units ED26-SRC-050-0001/0002) were written:
  readonly units owned by w03-p03-054.
- Section 39.2 route depends on the lead applying w03a-p03-038's driver input
  (labels cited from it) and this packet's patches
  (work/waves/w03a/patches/w03a-p03-055.json).

## Block 1, second pass (2026-10-12)

Assessment relayed for this pass: 39.2 MP-0 said the owned files did not
exist and that the EF theorem and the connectivity invariant/response lemma
lacked written proofs. Findings: the owned files exist (first pass,
2026-10-11) but neither they nor the w03a-p03-038 files are on the driver
route yet, which is why a route-based reading sees only the host citations.
The EF proof (annex:p03-w03-p03-038-pointed-ef, with records and
characteristic formulas) and the cycles distance invariant/response lemma
(annex:p03-w03-p03-038-cycle-response, -connectivity) were re-read in this
session and are complete written proofs; per A9 they are linked, not
duplicated. Their visibility on the route depends on the lead applying the
038 and 055 patch files (driver inputs and host pointers).

Added in this pass (body + annex, all proved=annex):
- thm:p03-w03-p03-055-pebble-basic (monotonicity in k; equivalence
  relation; Kolaitis 2003 p. 56, re-read in this session from
  tmp/agent-scratch/w03a-w03a-p03-055-b1-author/kol.txt, the text of the
  same online manuscript).
- sec:p03-w03-p03-055-bounded: def:p03-w03-p03-055-bounded-pebble (G^k_m,
  equiv^k_m), thm:p03-w03-p03-055-finitely-many-k,
  thm:p03-w03-p03-055-bounded-pebble, thm:p03-w03-p03-055-bounded-consequences
  (equiv^k as all m; k>=m reduces to EF; FO^k rank-m definability criterion).
  General content, no source locator given.
- thm:p03-w03-p03-055-bipartite (2-colorable iff no odd closed walk;
  L^3_{infty omega} definition; 3-pebble Spoiler win for odd m).
- def:p03-w03-p03-055-classify (method with side conditions),
  def:p03-w03-p03-055-classification (table of six concepts).
- Symbol rows G^k_m and equiv^k_m added to the intake CSV.

## Continuation

Block 1 second pass finished (2026-10-12). unit-compile ok;
find_fused_spaces clean. Remaining for any later block: (1) confirm the
038 labels and this file are on the route (lead, patch files);
(2) the 058 crosslink; (3) no source-specific SRC-050 content is owed here
(readonly units owned by w03-p03-054).

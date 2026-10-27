# w03a-p03-029 research note (P3 chapter 31, sections 31.5-31.8)

## Sources read in this session

- Morley, M. and Vaught, R., Homogeneous universal models, Math. Scand. 11 (1962) 37-57.
  Publisher open-access PDF, https://journals.msp.org/mscand/article/download/2698/2697
  (scanned, no text layer; read as page images). Pages read: 37-40, 53-57.
  Used: p. 38 (power notation, bar), p. 54 (standing restriction to relational systems
  with countable index sets), p. 55 (section 6, Lemma 6.1, Theorem 6.2 and its proof,
  question (9), Robinson's example and its iteration remark), p. 56 (LS lowers the
  universe with R_j fixed; omega_0, omega_1 vs kappa, kappa^+ open), p. 57 (reference
  25: Vaught, A Loewenheim-Skolem theorem for two cardinals, Notices AMS 8 (1961) 239).
- Shelah, S., The pair (aleph_n, aleph_0) may fail aleph_0-compactness, arXiv
  math/0404240v1 (13 April 2004), https://arxiv.org/pdf/math/0404240v1. Pages read:
  3-5 (0.1 Notation, 0.2 Definition, history items (A)-(J), (alpha), (beta)).
  Cited as its own arXiv-version entry Shelah2004PairAlephN; no published-version
  locator is used.
- Barwise, Chapter I of BarwiseFeferman1985 (held preview
  tmp/edition-2026-catalog-src038/tail-039-068/SRC-049-pageplace-preview-2026-09-09.pdf,
  PDF pages 28-29 = book pp. 8-9, section 1.5): Vaught's two-cardinal theorem and
  the abstract completeness of L(Q_1).
- Noquez, arXiv 1710.05809v1: opened, not used (continuous logic, not the classical
  convention).

## Attempts that failed (no bypass attempted)

- Chang 1965 Proc. AMS 16 (ams.org): Cloudflare bot check; not read. Chang's theorem is
  reported only as Shelah states it (item (H), p. 4).
- Vaught 1965 (Cardinals far apart), The Theory of Models pp. 390-401: no legitimate
  free copy found by search. Its theorem is reported only from Shelah p. 4 item (G).
- Schmerl, Chapter V of Model-Theoretic Logics (pp. 177-210): held preview contains only
  the contents listing; no free copy found.
- Chang-Keisler, Model Theory, 3rd ed.: not held; no free copy.

## Findings that affect existing text

- The (aleph_1, aleph_0) theorem is MV62 Theorem 6.2 (p. 55), announced in Vaught 1961
  (Notices). Shelah p. 4 item (F) credits it to Vaught with reference [MV62]; item (G)
  credits the 1965 far-apart paper with the beth_omega gap transfer. Barwise pp. 8-9 dates
  Vaught's two-cardinal theorem 1964. The host entry thm:p03-vaught-two-cardinal cites
  Vaught1965CardinalsFarApart and its method sketch describes the indiscernible method,
  which Shelah p. 4 associates with Morley's proof of (G). Patch requests in
  work/waves/w03a/patches/w03a-p03-029.json replace the key with MorleyVaught1962 and the
  method sketch with the MV62 method.

## Symbol decisions

- Shelah's letters (lambda universe, mu predicate) kept in the arrow convention and in
  items 4-5 of the warning; coordinate order bridged to the house (kappa, lambda).
- MV62 bar = cardinality (not closure or complement); omega_0, omega_1 = aleph_0, aleph_1.

## Continuation

Block 1 (this block) wrote section 31.6 only:
- body handbook/parts/p03/indiscernibles-ehrenfeucht-mostowski-models-and-cardinal-w03-p03-029.tex
  (chapter heading, sec:p03-w03-p03-029-vaught): definition of (kappa,lambda)-models,
  transfer-arrow convention, MV62 Theorem 6.2 (cited), theory-form corollary (proved),
  method summary, gap-one lemma, Robinson example, necessity theorem, non-conflation
  warning, worked example, proof boundary.
- annex with four full proofs.
- unit-compile ok; check.py shows only the bib-key findings for the two intake keys.

Open for later blocks:
- 31.5 (definable well-orderings, nonstandard transfer constructions): not started.
- 31.7 (formal transfer/reduction notions, method of identities) and 31.8 (singular and
  regular cardinal-like structures): the allocated source is Schmerl Chapter V, which is
  not held beyond its contents page; blocked_source unless a copy is acquired. Shelah
  math/0404240v1 0.3 Definition (identities) and 0.4 Claim were seen on pp. 5-6 and could
  support a general (non-Schmerl) treatment of identities; not yet written.
- N-a-005 MAP-02 (Vaught 1965 construction) and MAP-03/MAP-04 (Chang-Keisler 3rd ed.
  method and comparison) need those bodies.

Block 1, second pass (assessment of 31.6 GOAL-01/GOAL-03/C01):
- The assessment found only the host's inline hypothesis on the route. The chapter file
  holding def:p03-w03-p03-029-kappa-lambda-model and def:p03-w03-p03-029-not-conflate is not
  yet \input in handbook/parts/p03.tex (driver change, lead only); the host patches were
  not applied.
- Body additions: a paragraph in the definition tying the convention to the host statement
  thm:p03-vaught-two-cardinal; a sentence after the attribution paragraph pointing to the
  five-way comparison; a Relationships paragraph (thm:p03-w03-p03-007-two-cardinal-boundary
  as an (aleph_1,aleph_0)-model; thm:p03-keisler-q-one).
- Patch file rewritten: entry 1 replaces the whole host theorem (key MorleyVaught1962, names
  the (kappa,lambda)-model convention and the single target pair); entry 2 replaces the
  method sketch with the MV62 method and an in-host separation from downward/upward LS,
  far-apart (Shelah p. 4 (G)) and Chang (p. 4 (H)).
- Existing treatments found, not listed in packet: types-saturation-and-homogeneity-w03-p03-007
  thm:p03-w03-p03-007-two-cardinal-boundary; abstract-model-theory-and-characterization-of-w03-p03-047
  line 223 (Barwise remark, already crefs thm:p03-w03-p03-029-theory-form).
- Held sources rechecked: no copy of Vaught 1965, Chang-Keisler 3rd ed. or Schmerl Ch. V body.

Block 2 (31.6 MP-0(a): the Morley--Vaught construction):
- Source opened this block: MV62 publisher open-access PDF
  https://journals.msp.org/mscand/article/download/2698/2697 (scan; 21 pages = pp. 37-57),
  re-downloaded into tmp/agent-scratch/w03a-w03a-p03-029-b2-author/mv62 and read page by
  page: pp. 37-57 all read. Used: pp. 38-40 (notation, Lemma 1.2 and proof idea, ET, prec),
  p. 41 (conditions III-VI, Def. 2.2), pp. 42-43 (Thm 2.3 and proof, Cor 2.4, Thm 2.5,
  Thm 2.6 statement, footnote 5: Craig for 6.1(b)), pp. 43-44 (proof of 2.6(a), condition
  (3)), pp. 45-46 (Thm 2.8, 2.8' and proof), p. 47 (A*, Lemma 3.1), p. 48 (Thm 3.3 with
  hypothesis "kappa > omega, I_A"; homogeneous/special definitions; (5)), p. 50 (Thm 3.6
  proof using 1.2(b) for 2.8' hypotheses), p. 51 ((7), its proof via 3.5/3.7, footnote 11,
  Scott's question), p. 54 (countable index sets), p. 55 (6.1, 6.2), pp. 56-57 (bibliography:
  [21] Tarski, Contributions to the theory of models).
- Body (sec:p03-w03-p03-029-mv-construction, lines 188-428): thm mv-6-2 now proved=annex;
  method entry rewritten as a roadmap; new def mv-notions; lemmas mv-3-1, mv-1-2, mv-2-4d,
  mv-6-1; theorem mv-7 ((7) for countable index sets); proof boundary rewritten.
- Annex: six new annexitems (lines 192-839): 3.1(b) translation; Lemma 1.2 (a),(b) in full
  generality; 2.4(d) at power omega; 6.1(a) via 1.2(b) one-point step + 2.6(a)/2.8'
  recursion at cofinality omega; 6.1(b) via the 2.3(b) back-and-forth; 6.1(c) via 2.4(d);
  (7) finite case direct, infinite case by a denumerable route (not the source's 3.5/3.7
  special-model route); Theorem 6.2 steps 1-5 following p. 55.
- Not proved (stated as such in the proof boundary): the uncountable-power forms of
  2.3, 2.4, 2.6, 2.8'; Theorem 3.3; (7) for uncountable index sets; the source's own proof
  of (7) through Theorems 3.5 and 3.7 (special systems).
- Schmerl Ch. V: two web searches this block found only catalogue listings (Springer 1985;
  CUP 2016 reissue, Perspectives in Logic 8); no legitimate free copy. Still blocked_source.
- unit-compile ok (7 small overfull boxes, largest about 13pt).

## Author correction, 26 October 2026: source class parameter

The notation audit exposed an unexplained class parameter in the paragraph
following the countable homogeneity criterion. The original held scan was
visually rechecked at printed pp.39,41,43 (the existing mv62 page images).
The reader now defines the class parameter and its restricted subsystem
class, states conditions V and VI_kappa from Corollary 2.4, and explicitly
selects the class of all similar systems for the finite/countable application.
The actual theorem and its back-and-forth proof remain unchanged. The new
scope supplement records this source role; no general-class theorem or
independent admission is thereby asserted.

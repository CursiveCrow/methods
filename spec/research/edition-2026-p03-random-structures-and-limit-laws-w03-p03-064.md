# P3 40.1 Probability spaces of finite structures (packet w03a-p03-064)

## Provenance

- Source: Joel Spencer, "Logic and Random Structures", author's version,
  https://cs.nyu.edu/faculty/spencer/papers/ircsallsubm.pdf (30 pages, dvips/Ghostscript,
  CreationDate 2007-07-06), fetched 2026-10-11 in block 1 with WebFetch (author's institutional
  page, open access). SHA-256 b81de4d3a6126e08ab363f6438ab495c343b442a4b03beae7fb8295568bf545c,
  identical to the copy recorded by packet w03a-p03-067. Scratch copy:
  tmp/agent-scratch/w03a-w03a-p03-064-b1-author/src/ircsallsubm.pdf.
- All 30 pages were read as page images in block 1 (sections 1-14, About the references,
  reference list). Printed page numbers equal PDF page numbers.
- Version: the author's separately formatted text, not the printed Springer 2007 chapter
  (doi 10.1007/3-540-68804-8), which was not read. The reader text says so once; every locator
  is to the author's version. Bib key Spencer2007LogicRandomStructuresAuthor (entry identical to
  the 067 intake entry).
- The held Graedel chapter-3 PDF (source/references/acq-r1-ACQ-2026-10-0472/) is not this work
  and was not used.

## Locators used (all seen in the author's PDF this session)

p.1 SU(n,p), YES, exact probability, constant-p limit, motto; p.2 c/n limit, almost
always/never, threshold n^-1, n^-1.01 / n^-0.99, threshold function, 5/n, "basically determined
up to constant factors"; pp.2-3 three difficulties; p.3 unary zero-one theorem and theory, s.14
route; p.4 aleph_0-categorical; p.5 path of length three example and its threshold; p.6
rooted graphs; p.8 extension/rigid extension, t-closure two definitions, omitted lemmas,
cl_4 example, Nonexistence Lemma; pp.8-9 closure isomorphism notation, t=0; p.9 first-order
remark, Finite Closure Lemma and proof; p.11 t_i sequence uses the Finite Closure Lemma;
pp.12-13 section 6; pp.12-14 witness estimate and categoricity; p.26 EHR game, new-vertex
remark, theorem; p.27 isolated-vertex example, two corollaries, generalization to finite
relational languages, start of About the references; pp.27-28 About the references;
pp.28-30 reference list.

## Corrections relative to the source (recorded here; reader text states them neutrally)

- Finite Closure Lemma proof: steps may have exactly t nonroots ("fewer than t" in source);
  r - K epsilon may equal 0, strictness comes from irrationality of alpha.
- Path-of-length-three sentence: the source formula lacks x1 != x2; read literally at x1 = x2 it
  demands a triangle through every vertex. The guard is added; theorem proved for both the path
  and the walk reading.
- The source's general t-closure is stated for finite G; the annex proves well-definedness for
  arbitrary (possibly infinite) graphs, needed later for countable models.

## Existing treatments found (not listed in the packet's existing list)

- handbook/parts/p03/random-structures-and-limit-laws-w03-p03-065.tex (packet w03a-p03-065,
  section 40.2; untracked, written 2026-10-11): G(n,p(n)), almost surely, << / >>, threshold
  function, moment bounds, clique / isolated vertex / common neighbour thresholds with proofs,
  Shelah-Spencer law statement (cited), rooted graphs, dense/sparse/rigid/safe,
  subextension/nailextension, pi/7 examples, Harris and Janson inequalities, safe-extension
  criterion with full proof. Linked, not duplicated. Its bib key SpencerLRS2007Preprint is a
  second key for the same source.
- handbook/parts/p03/random-structures-and-limit-laws-w03-p03-067.tex (packet w03a-p03-067,
  section 40.4): SU(n,p) and G(n,p) definitions, almost sure theory of a zero-one law (no finite
  models, countable model), unary theorem (C001 zero-one law, theory, completeness, aleph_0-
  categoricity), Alice's Restaurant schema, witness estimate, staying-alive completeness, Rado
  graph categoricity, sparse failure, sparse countable models (sketched only). Linked.
- Both packets list ED26-SRC-050-0004 as readonly with this packet as owner; they nevertheless
  wrote this material. Lead decision needed on whether those texts stand (this chapter links them).

## Proposed decisions

- Unify the two bib keys for the author's version (SpencerLRS2007Preprint in 065,
  Spencer2007LogicRandomStructuresAuthor in 067 and here); 065's howpublished says
  "sections numbered 1--15", which is wrong (sections 1-14 plus unnumbered About the references).
- Symbol overlap: cl_t (italic, Spencer's typography, here) vs \mathrm{cl}_t (067 intake);
  EHR[G,H;t] (here, s.14 form) vs \mathrm{EHR}(G,G';t) (067, s.3 form). Same notions; register
  once with both spellings noted.

## Continuation

Block 1 (2026-10-11) wrote, in owned files:
- C001 residual: YES theorem (exact, constant p, c/n, threshold), threshold-ratio lemma,
  failure at both unary thresholds, warning. Zero-one theorem/theory/completeness/categoricity
  live in 067 (linked); s.14 completeness route via thm:p03-w03-p03-064-complete-game.
- C002 residual: path-of-length-three threshold, full proof via 065's Janson inequality.
- C004: rigid extensions in a graph, monotonicity/base-enlargement/finite-base lemma, t-closure
  (two definitions) with equivalence proof for arbitrary graphs, cl_4 example verified at pi/7,
  first-order expressibility of closure types, Nonexistence Lemma, Finite Closure Lemma.
- C006 bridge: Alice's Restaurant completeness via the s.14 corollary on countable models.
- C014: EHR game, new-vertex lemma, isolated-vertex example, elementary-equivalence corollary,
  finite vs infinite game theorem with a proved example, completeness corollary.
- C015: About the references guidance with intake bib entries from Spencer's list.

Block 1, second run (2026-10-12), wrote C005 (body sec:p03-w03-p03-064-theory, lines 468-708;
annex items f-laws .. sparse-law, lines 498-922 of the annex):
- def vminuse (f(S,H) = v - e alpha), lemma f-laws (additivity, irrationality, safe => f(S,H) <=
  f(R,H) - kappa, nonsafe contains rigid subextension = Spencer's omitted lemma p.12);
- def generic (t-generic, p.10), example at pi/7, def theory-alpha (two schemas, p.10);
- thm large-deviation: two-sided o(n^-r) deviation and Counting Theorem, proved by a 2k-th
  central moment bound (overlap graph Gamma, components, safety constant kappa) — Spencer omits
  the proof (pp.10-11). NOT proved: Spencer's remark that the probability is at most
  exp[-n^delta] (p.10). Stated in the reader text as not proved here.
- lemma moment-bound (k-th raw moment of counts of any rooted graph, exponent F^+);
- thm theory-as: every sentence of T_alpha a.s., via failure types (a) extra edge, (b) rigid
  attachment with an edge to y; F^+ < f(R,H) proved for each type;
- lemma closure-models (closure bound |cl_t(X)\X| < |X|/eps_t in graphs without finite dense
  subgraphs; equivalence of the two Nonexistence forms; locality of closures);
- thm duplicator: invariant on t_i-closures, explicit t_i formula (Spencer's condition is
  for sets of size i+1, p.11; the step needs sets of up to u vertices — noted in the annex),
  Inside/Outside with safety of NEW over OLD and genericity argument written in full;
- cor sparse-law: consistency, no finite models, completeness, zero-one law (proves 065's
  cited thm:p03-w03-p03-065-shelah-spencer);
- warning sparse-limits.
Proof design note: Janson's lower-tail inequality was not needed; the central-moment method
gives the polynomial bound o(n^-r) Spencer says suffices.

Still owed (next blocks), in order:
1. C005 remainder: proof of the exp[-n^delta] large-deviation bound (Spencer's remark, p.10).
2. C007: sparse countable models with complete proofs (compactness model with H^s via number
   theory; G_alpha by witness demands, model of T_alpha, finite closures, uniqueness claim
   pp.14-15). Depends on C005.
3. C008: f_A, continuity at irrationals, spectrum Sp(A), K4/K5 examples, finite spectra
   (pp.15-16). Depends on C005.
4. C009: K_{3,k}, EVEN/BIGGER, A*, R_u, Representation Lemma and almost sure encoding,
   infinite spectrum (pp.16-18); almost-everywhere equivalence remark.
5. C010: jump condition, XPL_u well ordered, example u=5, alpha=1/3+10^-6 (pp.18-19).
6. C011: g_A, T^-_alpha, complexity condition in PH, the game board argument (pp.19-21);
   Tardos sufficiency is attributed only.
7. C012: G_<(n,p), arithmetization, Representation Lemma u <= 0.9 log^{1/3} n, nonconvergent
   sentence; G(n,n^{-1/4}) outline (pp.22-24).
8. C013: Shelah's theorem f_A(n+1)-f_A(n) -> 0, corollary on evenness, circuit argument
   (pp.25-26) — needs a constant-depth circuit lower bound for majority-type distinctions; must
   be proved or a cited boundary agreed by the lead.
9. C002 remainder: the Erdos-Renyi connectivity limit e^{-e^{-c}} quoted on p.5 (not proved
   anywhere on the route).

Block 2 (2026-10-13). Sources reopened this session: Spencer author PDF from the block-1 scratch
copy (sha256 b81de4d3...f545c, same file), pp. 10, 15-16, 18-20, 23-24 read (p. 10 as a page
image: the source prints the deviation bound as exp[n^{-lambda}] with "a positive lambda"; the
reader text says the intended bound is exp[-n^lambda]); O'Donnell arXiv:2105.10386v1 from the 071
scratch copy (sha256 624b3357...acb6), printed pp. 100-107 and 111 read (switching lemma statement
p. 100, def. 4.27 width p. 104, thm. 4.30 p. 106, majority remark p. 107, Boppana attribution
p. 111).
Written in this block:
- C005: cor exp-deviation (body ~604-625, annex exp-deviation): the 2k-th moment bound of the
  large-deviation proof holds for every k; k = floor(n^{kappa/(4v)}) gives exp[-n^{kappa/(8v)}].
- C008: sec rational-thresholds (body 730-842; annex containment, hab, rational-threshold):
  general containment threshold n^{-1/m(H)} (first/second moment), explicit graphs H_{a,b} with
  m = b/a via a fractional orientation (cycle edges carry the chord surplus; Sturmian set P keeps
  weights in (0,1]), corollary: threshold n^{-a/b} for every rational a/b in (0,1) and
  T_alpha != T_beta. Example H_{2,3} checked by hand.
- C012 (Spencer's k-ary remark, p. 23): sec k-ary (body 843-939; annex rep-layout,
  every-relation): block encoding with an empty-trace marker vertex then k singleton-trace
  vertices; a.s. every k-ary relation on {1..u} for u <= floor((log_2 n/(2k+2))^{1/(k+1)}).
- C013: sec circuits (body 940-1023; annex influence-basics, depth-induction, boppana).
  During this block the 071 owner added proofs of the switching lemma
  (thm:p03-w03-p03-071-switching) and an N-dependent influence bound
  (thm:p03-w03-p03-071-ac0-influence, log(2Ns)); thm:p03-w03-p03-071-boppana no longer exists.
  This chapter reuses 071's switching lemma and restriction facts and proves the N-free bound
  I[f] <= K_d (log_2 s)^{d-1} (Boppana, O'Donnell thm 4.30): induction on depth with width w and
  upper-gate count S, I <= c_d w (log_2 4wS)^{d-2}; failure of switching paid by subadditivity
  to layer-2 gates (I <= 2wS), not by |J|. A first draft also proved the switching lemma here;
  it was removed to avoid a second treatment.
Still owed (not closed in this block):
1. C010: the Jump Condition for Spencer's XPL_u (proved only for XPL*_u in 070) and the zero-one
   law for depth-u sentences at rational alpha outside XPL_u (p. 19). A proof at rational alpha
   needs the counting/genericity/closure machinery redone with all rooted graphs of fewer than
   a (numerator) nonroots; the genericity step combines extensions of up to about 2 t_u
   nonroots, so a > t_u does not obviously suffice. Not attempted in writing.
2. C009 (069's text): f_A for the encoded sentence is determined only on [1/3,1/2); values on
   I_k for k <= 5 and below 1/3 undetermined; representation lemma fails for k = 4, 5.
3. C011: Tardos's sufficiency of Jump + Complexity conditions: no accessible source.
4. C012: nonconvergence for unordered G(n,n^{-1/4}) (source outline defective: symmetric R_u).
5. C001/C003/C006/C007: as in block 1 (material lives in 065/067; driver insertion is a lead
   action). C002's connectivity limit e^{-e^{-c}} is now proved in 065
   (thm:p03-w03-p03-065-connectivity).

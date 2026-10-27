# Packet w03a-p03-071 (P3, section 40.8): research note

## Sources read in this session

- Spencer, "Logic and Random Structures", author's version,
  https://cs.nyu.edu/faculty/spencer/papers/ircsallsubm.pdf (30 pages; sections
  numbered 1-14 without chapter prefix plus "About the references").  Fetched
  2026-10-11 with WebFetch; local copy SHA-256
  b81de4d3a6126e08ab363f6438ab495c343b442a4b03beae7fb8295568bf545c.
  Read: sec. 12 (pp. 22-24), sec. 13 (pp. 25-26), About the references and
  reference list (pp. 27-30).  Page images of pp. 22-26 were inspected to
  confirm symbols lost in text extraction.  This is not the printed Springer
  2007 chapter; the reader text says so and uses only this version's locators.
- O'Donnell, Analysis of Boolean Functions, arXiv:2105.10386v1 (May 2021 arXiv
  edition).  Read: Def. 2.12-2.13 (p. 46), Def. 2.27 (p. 49), Def. 4.26 (p. 103),
  Def. 4.27 (p. 104), Thm. 4.30 (p. 106), remark on majority (p. 107), notes
  attributing Thm. 4.30 to Boppana (p. 111).

- Block 1 rerun, 2026-10-12: both PDFs re-downloaded from the same URLs
  (https://cs.nyu.edu/faculty/spencer/papers/ircsallsubm.pdf and
  https://arxiv.org/pdf/2105.10386v1); hashes identical to the copies above
  (O'Donnell SHA-256 624b3357...acb6).  Re-read Spencer pp. 22-26 and
  O'Donnell pp. 46, 49, 103-107, 111; every locator in the reader text was
  checked against these pages.

- Block 2, 2026-10-13: both PDFs re-downloaded with curl from the same URLs
  into tmp/agent-scratch/w03a-w03a-p03-071-b2-author/dl/; hashes identical
  (Spencer b81de4d3...f545c, O'Donnell 624b3357...acb6).  Read Spencer
  pp. 22-26 (sec. 12 remark on k-ary relations and on primes / Fermat primes,
  p. 23; sec. 13 p. 26).  Read O'Donnell pp. 73-75 (defs 3.13, 3.14, 3.18),
  pp. 93-101 (defs 4.1, 4.3, prop 4.5, prop 4.7, def 4.15, cor 4.18, lemma
  4.19, thm 4.20, switching lemma statement p. 100, references to Hastad and
  Razborov proofs p. 101), pp. 103-107 (defs 4.26-4.27, lemma 4.28 with its
  proof, thm 4.30 and exercise 4.20 on p. 106, majority remark p. 107),
  p. 111 (Boppana attribution).

## Corrections relative to the source (provenance for the reader text)

1. Literal encoding R_{c,d} (p. 22-23: x,y <= z, witness e adjacent to x,y,z and
   no other element of S) can never equal + on {1,...,u} for u >= 2: a witness
   for (1,1,2) also witnesses (1,2,2).  Same defect for times via (2,1,2)/(1,1,2).
   Reader text proves this and uses a corrected encoding: strict x,y<z, a
   cleanliness clause on the witness interval, and times defined from the
   encoding plus the two unit cases.
2. Upper bound: source asserts (without proof, "which we exclude") failure for
   u > C log^{1/3} n with C = 900.  Reader text proves failure for u >= 3 L with
   the cleanliness clause; without that clause the counting argument does not
   bound long intervals, and this note does not settle the literal claim.
3. Source spells "Hansen" on pp. 22 and 25; its reference [4] is Henson.
4. Source example sentence on p. 25 (exists x forall y exists z z~y and y~x) is
   not the sentence its translation renders (z~x and z~y); reader text uses the
   translated sentence and says so.
5. Sec. 13 "further technical work" after Razborov: replaced by Boppana's total
   influence bound (O'Donnell Thm 4.30, imported, cited) plus a proved slice lemma.

6. Translation lemma proof (earlier block): the chain replacing a literal leaf
   at distance t had d-t-1 gates; corrected to d-t gates in layers d-t..1.
   The size bound s_N is unchanged.
7. Block 2: the cited Boppana bound is replaced by a proved estimate
   I[f] <= 4(32t)^{d-1}, t = ceil(3 log(2Ns)) (thm -ac0-influence), with a
   complete proof of the switching lemma (constant 16, encoding argument
   written for this chapter, not taken from Hastad or Razborov, whose papers
   were not read) and of the restriction facts.  Boppana's N-free form is
   stated as O'Donnell's and not proved here.
8. Block 2: Spencer's k-ary remark (p. 23) is established for a block
   encoding (marker vertex with empty trace followed by k singleton traces)
   for u <= U_k(n) = floor((log n/(2(k+1)))^{1/(k+1)}); the (log n)^{1/3}
   range for arbitrary ternary relations is stated as not established.

## Continuation

- 2026-10-12 (block 1 rerun): added intake bib (Spencer author version,
  O'Donnell arXiv v1), symbol intake CSV, return JSON.  Added
  def:p03-w03-p03-071-common-nbhd and lemma thm:p03-w03-p03-071-all-sizes
  (N(x1..x4) of every size up to ln n/(20 ln ln n) in G(n,n^{-1/4}); proof
  by disjoint quadruples in a set of n^{1/5} vertices, independence of their
  neighbourhoods in the rest, Chebyshev, and a Markov bound on spoiled
  quadruples).  Proofboundary def:p03-w03-p03-071-sparse-outline updated.
- Remaining for C012: full proof of the G(n,n^{-1/4}) nonconvergence via
  N(x1,...,x4): representation of <,+,* by R_u-relations (needs an
  asymmetric encoding the source leaves open; R_u is symmetric in all
  arguments), near-independence of the R_u, upper limit Theta(ln^{1/3} n)
  on arithmetizable N(x1..x4), BIGGER at p=n^{-1/4}, and the sentence.
- C013 written (secs. 13); printed Springer locators not available.
- 2026-10-13 (block 2): closed the two assessed gaps.  (a) Body: def
  -restriction, lemma -restriction-facts, lemma -switching, thm
  -ac0-influence, cor -advantage replace the cited thm -boppana; Shelah
  annex proof rewritten on thm -ac0-influence with explicit C_A; example
  bound updated.  (b) Body: def -block-encoding, thm -kary with remark
  (exact hypotheses, what is not established), lemma -prime (Prime, Fer
  formulas), cor -prime-graph.  All with annex proofs.  Sibling packet 064
  now cross-references -ac0-influence, -restriction, -restriction-facts,
  -switching; those labels must be kept.
- Remaining for C012: unchanged from block 1 (G(n,n^{-1/4}) outline).

# w03a-p03-065 — P3 40.2 Random graphs and extension statements

Packet: work/waves/w03a/packets/w03a-p03-065.json (label_tag p03-w03-p03-065).
Unit ED26-SRC-050-0004 is a readonly unit here (owner w03a-p03-064; the packet
field names "w03-p03-064"). Its components C001-C015 are not written by this
packet. The section duty MP-0 for 40.2 is written in the owned files below.

## Source read

- Spencer, "Logic and Random Structures", author's version PDF
  https://cs.nyu.edu/faculty/spencer/papers/ircsallsubm.pdf, fetched 2026-10-11
  with WebFetch, copy at tmp/agent-scratch/w03a-w03a-p03-065-b1-author/src/spencer.pdf,
  SHA-256 digest b81de4d3a6126e08ab363f6438ab495c343b442a4b03beae7fb8295568bf545c
  (hash re-verified 2026-10-12), 30 pp., created 2007-07-06 from ircsallsubm.dvi.
  Sections numbered 1-14 plus an unnumbered "About the references" (the block-1
  text said 1-15; corrected 2026-10-12). Not the Springer printed chapter.
- Read block 1: pp. 1-16 in full; page images pp. 2, 6, 7.
- Re-read block 2 (2026-10-12, text extraction sp.txt of the same file):
  s.2 pp. 4-5 (isolated vertices, connectivity limit e^{-e^{-c}}), s.5 pp. 9-12
  (t-generic, schemas, large deviation o(n^{-r}), exp(-n^eps) remark p. 10,
  Counting Theorem p. 11, Generic Extension outline, Duplicator strategy),
  s.6 pp. 12-13, s.7 pp. 13-15 (countable models), "About the references" p. 29.
- Bib key switched to Spencer2007LogicRandomStructuresAuthor, field-for-field copy of
  the w03a-p03-067 intake entry (same PDF), replacing SpencerLRS2007Preprint.

## Source corrections (correction policy)

- p. 7, "Every vertex lies in a K4": source gives e=10 and calls it dense and
  rigid while recording v-e*alpha>0. Correct: e=6, sparse and safe.
  Corrected in def:p03-w03-p03-065-pi-seven item 4.
- p. 7, first example says "a neighbor"; the graph described is the common-neighbour one.
- p. 6, Ext(R,H) says "y1,...,yr"; read as y1,...,yv. Distinctness made explicit.

## Proof provenance

All annex proofs are written for this chapter. Block 2 added:
- connectivity window: factorial moments + Bonferroni (alternating binomial
  partial sums), no components of size 2..n/2 via spanning trees counted by
  parent maps (k^{k-1}, no Cayley formula needed);
- exponent calculus lambda_F(T), rigid-safe decomposition (uses
  thm:p03-w03-p03-070-weights item 3 for nonsafe => rigid subextension);
- Counting theorem for safe extensions: 2k-th centred moment, linked
  overlap shapes, each non-first copy in an overlap class loses eps_0, giving
  E(N-mu)^{2k} <= C n^{2k(v-e alpha)-k eps_0}; failure o(n^{-r});
- rigid extensions boundedly many (greedy chain of new-vertex extensions + first moment);
- general upper bound N_{R,F} <= C n^{lambda_F(S)};
- Generic extension: bad patterns (extra edge H+g; rigid attachment Z) have
  lambda_F(S) <= v-e alpha-gamma; compared with N >= mu/2.
- Shelah-Spencer law: (AS_alpha) from 068 Nonexistence + generic extension, then
  thm:p03-w03-p03-072-sparse-zero-one.

## Existing treatments found

- handbook/parts/p03/finite-model-theory.tex 14-62 (sec:p03-zero-one-law): linked.
- handbook/parts/p03/classification-theory.tex thm:p03-random-graph: linked (not in packet "existing").
- handbook/parts/p09/presentations/n-c-002-02.tex thm:p09-fagin1976-labelled: linked (not in packet "existing").
- handbook/parts/p03/qe-categoricity-games-supplement.tex thm:p03-ef: linked (not in packet "existing").
- Siblings (chapter 40): 064 thm:p03-w03-p03-064-path3 (path-of-length-three
  threshold, now \cref'd instead of only reported), 064 finite-closure; 067
  categorical / sparse-models; 068 nonexistence; 070 theory, weights,
  finite-closure, AS convention; 072 sparse-zero-one. All linked, none duplicated.
- 067 def:p03-w03-p03-067-sparse-notions overlaps def:p03-w03-p03-065-dense-sparse.

## Continuation

Block 2 (2026-10-12) written: connectivity theorem (thm:p03-w03-p03-065-connectivity),
path3 now \cref to 064, section "Counting extensions and generic extensions"
(def exponent, lemma decomposition, thm counting, lemma rigid-count, cor
upper-count, thm generic-extension, example generic-example, warning
generic-limits), Shelah-Spencer switched from cited= to proved=annex with
proof through 070/068/072, relationships with the countable-model
classification \cref'd to 067. unit-compile ok; fused spaces clean.

Open dependency (not this packet's component): the non-aleph_0-categoricity of
T_alpha is on the route only as 067's sketched= theorem; its complete proof is
component C007 of the readonly unit owned by w03a-p03-064. The counting
estimate 067's sketch says it lacks is now thm:p03-w03-p03-065-counting.
Nothing else owed for MP-0 is known to this packet.

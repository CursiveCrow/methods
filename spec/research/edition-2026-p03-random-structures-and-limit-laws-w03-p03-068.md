# P3 40.5 Closure constructions and dynamic presentations (packet w03a-p03-068)

Label tag: `p03-w03-p03-068`. Owned files:

- body `handbook/parts/p03/random-structures-and-limit-laws-w03-p03-068.tex` (653 lines)
- annex `handbook/annex/p03/random-structures-and-limit-laws-w03-p03-068.tex` (582 lines)
- bib intake `handbook/bib/intake-p03-random-structures-and-limit-laws-w03-p03-068.bib`
- symbol intake `handbook/registry/symbols-intake-p03-random-structures-and-limit-laws-w03-p03-068.csv`

## Source read

- Spencer, *Logic and Random Structures*, author's version,
  https://cs.nyu.edu/faculty/spencer/papers/ircsallsubm.pdf, 30 pp., sections 1-14 plus
  unnumbered "About the references"; SHA-256
  b81de4d3a6126e08ab363f6438ab495c343b442a4b03beae7fb8295568bf545c (same bytes as the
  064/067 reads). Fetched with WebFetch on 2026-10-12, text extracted with pdftotext,
  pp. 9-10 rendered to PNG and read to confirm K = ceil(r/epsilon).
- Pages read: 6-12 (sections 3-5) and 15-16 (end of section 7, section 8, start of 9).
- The Springer 2007 printed chapter (doi 10.1007/3-540-68804-8) was not read; the reader
  text says the presentation follows the author's version.
- Bib key: `Spencer2007LogicRandomStructuresAuthor`, field-for-field duplicate of the
  064/067 intake entries. The earlier key `SpencerLRS2007Preprint` (still used by 065) was
  dropped here; its howpublished field wrongly said "sections numbered 1--15".

## Locators used (all verified in this session)

- p. 6: rooted graphs, dense/sparse/rigid/safe (via 065 labels).
- p. 7: dense-not-rigid example (four roots, y1 adjacent to all, y2 pendant).
- p. 8: closure fixed alpha irrational and t >= 1; both definitions; lemmas "deleted";
  cl_4(x1,x2) example; Nonexistence Lemma and proof; start of isomorphic closures.
- p. 9: isomorphic closures, cl_t(...) = H with roots in positions, t = 0 case,
  first-order predicate, example formula, Finite Closure Lemma (alpha in (0,1) irrational,
  r,t >= 1), epsilon, K = ceil(r/epsilon), chain with "fewer than t nonroots".
- p. 10: t-generic definition; Nonexistence and Generic Extension schemas (roots written
  x_1..x_v in items 1 and 3; outer quantifier without "distinct").
- pp. 10-12: Generic Extension sketch (large deviation omitted), completeness by EHR game;
  p. 12 the omitted combinatorial lemma "any nonsafe extension contains a rigid
  subextension".
- p. 15: safe extensions in the countable-model discussion; section 8: f_A, domain
  irrationals, continuity argument, theories all different with the parenthetical
  "known" graph H with threshold n^{-a/b}, spectrum definition, K4 {2/3}, K5 {1/2}.
- p. 16: K4 and not K5 spectrum {2/3,1/2} with the evolution description; any finite set
  of rationals "with some technical work"; finiteness conjecture false.

## What this block did (2026-10-12)

Found the owned body and annex already present (written 2026-10-11 by an earlier run of
this block, which left no note or return). Re-read the source, checked every locator and
every proof, and:

- switched the bib key and rewrote the intake entry (see above);
- added `thm:p03-w03-p03-068-safe-or-rigid` (body) with full annex proof: over a finite
  root set an extension is safe or has a nonempty rigid part, never both, and the
  t-closedness criterion via safe extensions. This is the lemma Spencer omits on p. 12
  and covers the "rigid and safe extensions over a root set" item. The t-fixed proof now
  uses it;
- tightened `thm:p03-w03-p03-068-t-fixed` to irrational alpha (standing convention);
- corrected the description of the Finite Closure details (K = ceil(r/epsilon) is
  Spencer's own choice; the annex supplies why r - K epsilon < 0 is strict);
- noted that the Generic Extension schema is read over distinct roots, as Ext in 065;
- spectrum notation now `\operatorname{Sp}`, with a stated equivalence to
  `def:p03-w03-p03-069-spectrum`;
- replaced the two "companion chapter" pointers by \cref to
  `sec:p03-w03-p03-064-game` and `thm:p03-w03-p03-069-infinite-spectrum`;
- added a pointer to the overlapping closure account `sec:p03-w03-p03-064-closure`.

Example arithmetic re-checked by hand: pi/7 closure steps; cl_3 = cl_2 = {x1,x2,y1,y2};
epsilon at pi/7 for v = 1..4 (e = 3,5,7,9) and K = 6, 17, 43, 205 for r = 2; K4 rigid over
the empty set iff alpha > 2/3.

## Overlaps found (not in the packet's existing list)

- `sec:p03-w03-p03-064-closure` (packet w03a-p03-064, owner of the readonly unit
  ED26-SRC-050-0004): a second, shorter treatment of the same Section 4 material
  (rigid extensions, both closure definitions, example, closure-type formula,
  Nonexistence and Finite Closure Lemmas). Both files were written in the same minute on
  2026-10-11. Lead decision needed on which stays canonical; this chapter now
  cross-references 064's section.
- `def:p03-w03-p03-069-spectrum` (packet 069) defines f_A and Sp(A) again (limit form);
  this chapter states the equivalence.
- `def:p03-w03-p03-067-sparse-notions` restates rigid/safe/closure for 067's comparison.

## Open items

- Source p. 15 parenthetical: "it is known that there is a graph H such that the
  existence of a copy of H has threshold function n^{-a/b}" for every rational a/b. Not
  proved here; distinctness of the T_alpha is proved by a different route (rooted graph
  (R_q,H_q), extension statement switching at q).
- The axiomatized almost sure theory (`thm:p03-w03-p03-068-axiomatized`) is cited, not
  proved: the source itself omits the large-deviation estimate and the completeness game
  is source section 5 (component C005, not written by any packet yet according to 064's
  return).

## Continuation

State at 2026-10-12: body and annex compile (`waves.py unit-compile` ok, 9 overfull);
`find_fused_spaces.py` no hits; `check.py --tree handbook` shows no finding on the 068
files. Remaining for a later block: the n^{-a/b} threshold graph claim of p. 15 (a
balanced graph of every rational density b/a > 1 and its threshold), and the lead's
decision on the 064/068 closure overlap.

## Author correction 2026-10-26

Connected the axiomatized almost-sure theory to the completed proof in
067, whose axiom-by-axiom comparison uses 070's almost-sure theorem and
completeness argument. The 068 statement now has its own short annex proof
and a proved target instead of a source-only status. The graph axioms are
explicit in both the statement and the parameter-persistence argument.
No assertion is added at rational exponents; the continuity theorem still
has only irrational parameters. This is an author-level dependency repair,
not independent acceptance or a claim to have read the printed Springer
chapter. The printed-source obligation remains open.

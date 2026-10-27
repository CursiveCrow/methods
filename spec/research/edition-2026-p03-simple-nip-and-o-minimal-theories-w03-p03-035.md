# P3 34.1--34.4 -- NIP, simplicity and their intersections (packet w03a-p03-035)

Owned files:

- handbook/parts/p03/simple-nip-and-o-minimal-theories-w03-p03-035.tex (body, `\chapter`, toc tag `%% toc: P3 34 34.1,34.2,34.3,34.4`)
- handbook/annex/p03/simple-nip-and-o-minimal-theories-w03-p03-035.tex (annex)
- handbook/bib/intake-p03-simple-nip-and-o-minimal-theories-w03-p03-035.bib (new key `Simon2015GuideManuscript`)
- handbook/registry/symbols-intake-p03-simple-nip-and-o-minimal-theories-w03-p03-035.csv

Label tag: `p03-w03-p03-035`. Placement: body after `parts/p03/classification-theory` in
`handbook/parts/p03.tex`; annex after `annex/p03/feferman-vaught-composition` in `handbook/annex/p03.tex`
(packet insertion proposal; drivers are not edited here).

## Sources read in this session

- Held: Shelah, *Stability, the f.c.p., and superstability*, Ann. Math. Logic 3 (1971) 271--362, published
  printing scan (source/references/acq-r1-ACQ-2026-10-0504/...pdf; PDF page n = printed page 270+n).
  Read: contents p. 271; §0 list pp. 272--287 in part (A1--A13; G1--G8 on pp. 286--287, where G6--G7
  cite Shelah [E], the unstable-spectrum paper); §2 pp. 296--305 (Definitions 2.1--2.6, Lemmas 2.1--2.12,
  Theorem 2.9 p. 303, Theorem 2.13 p. 304); §3 opening p. 306 and Definition 3.2, Lemma 3.7, Theorem 3.8
  p. 312; §4 Definitions 4.1 (pp. 316--317), 4.2 (p. 317), Theorem 4.1 (p. 317), Definition 4.4 and
  Theorem 4.2 (p. 320), Theorem 4.3 (p. 321), Definition 4.5 and Theorem 4.4 (pp. 323--324); references
  p. 361 ([E], [G]). Pages 297 and 317 were checked as images for notation (Definition 2.2 uses
  `if (n >= r)`; Definition 4.2 as displayed).
- Held: Shelah, *Every two elementarily equivalent models have isomorphic ultrapowers*, Israel J. Math.
  10 (1971) 224--233 (acq-r1-ACQ-2026-10-0505): pp. 224--225 (abstract, main theorem).
- Held: Simon, *A Guide to NIP Theories*, author-typeset manuscript dated 16 October 2015
  (acq-r1-ACQ-2026-10-0513), not the CUP printing; intake key `Simon2015GuideManuscript`.
  Read: contents pp. 3--5; Ch. 1 pp. 7--12 (history, organization p. 9 on the ambient-NIP assumption,
  §1.1 conventions pp. 10--11, §1.1.1 indiscernibles p. 11); §2.1 pp. 13--18 (Definition 2.1, Remarks
  2.2--2.3, Example 2.4, Lemma 2.5, Remark 2.6, Lemma 2.7, Proposition 2.8, Lemma 2.9, Definition 2.10,
  Proposition 2.11, Example 2.12, Theorem 2.13); §2.3.2--2.3.5 pp. 30--36 (Definitions 2.53--2.56,
  Proposition 2.55, Lemma 2.59, Theorem 2.60, Example 2.61, Definition 2.65, Observation 2.66,
  Theorem 2.67, Definition 2.68, Proposition 2.69); chapter notes pp. 36--37; §6.1 pp. 85--87
  (Example 6.2, Lemmas 6.3--6.4); Appendix A.1.1--A.1.3 pp. 147--150.
- No online sources were read.

## Notation and conventions

- Ambient model: the `\mathfrak C` of `def:p03-w03-p03-031-monster` (packet 031), strengthened here to
  `\bar\kappa > 2^{|T|}` so that sequences of length |T|^+ are small. Simon's monster is also homogeneous;
  every automorphism step of Simon's proofs (Lemma 2.7) is replaced by type-preserving copies or by
  indiscernibility directly. Simon's `U` is not introduced.
- Simon's `opp`, `phi^0/phi^1`, `S_phi(A)` kept; Shelah's `S^m_phi(A)`, `Gamma(phi,m,alpha)`, `Ded`
  recorded in prose/definitions with their own roles.
- Random graph: language {E} and `T_{RG}` of packet 015; DLO: `T_{dlo}` of n-a-001-01.

## Provenance of the proofs

- Characterization theorem: (1)<=>(2) completeness; (2)<=>(3) compactness/saturation; (3)=>(4) Simon
  Lemma 2.5 argument; (4)<=>(6) type-count bookkeeping written here; (3)=>(5) and (5)=>(2) Simon Lemma 2.7
  with the automorphism step replaced by indiscernibility.
- Sauer--Shelah: shattered-sets counting induction (written here), not Simon's compression proof.
- EM extraction: Ramsey (thm:p03-w03-p03-028-ramsey-a) + (Sat); Simon refers it to Tent--Ziegler 5.1.3.
- Alternation, Boolean combinations, one-variable reduction: Simon 2.8, 2.9, 2.11 arguments, written out.
- Unstable => IP or SOP: Simon Theorem 2.67 argument; the indiscernible ladder is extracted directly
  over Q, so no "increase the sequence" step is needed.
- SOP => not simple: written here (preorder from the chain, an indiscernible chain indexed by a
  purpose-built order of size |T|^+, 2-inconsistent interval formulas).
- Tree property => order property of the negated formula: written here (spine argument); this avoids
  the Erdos--Makkai step of Shelah's Lemma 2.1.
- Stable => simple: local dividing rank D_{delta,k} (k-inconsistent parameter families, no
  indiscernibility), monotone, invariant (Copy), blind to disjunctions, finite in stable T via the
  tree lemma; minimal-rank formulas give the base. Written here; not attributed to a source.
- Shelah Lemma 2.2: leaves/nodes placed in the Cantor set so that eta(k)=1 iff leaf < node point.
- Stable => local character of dividing: dividing chain from failure, pigeonhole, downward finite-tree
  construction by (Copy), compactness to omega^{<omega}, then the tree lemma.
- O-minimal => NIP: uniform alternation bound by compactness (written here), then one-variable reduction.

## Existing treatments found (not in the packet's list)

- handbook/parts/p03/stability-and-the-forking-calculus-w03-p03-031.tex: forking in the random graph
  (`thm:p03-w03-p03-031-random-graph`, simplicity with finite bases) and the order property of E
  (`def:p03-w03-p03-031-random-graph-example`) -- reused by cref, not rewritten.
- handbook/parts/p03/simple-nip-and-o-minimal-theories-w03-p03-037.tex (packet 037, 34.9): RCF QE,
  completeness, o-minimality of every model, instability, one-variable NIP bound, theory-level NIP
  (cited there to Simon), R with a predicate for Z. Here the RCF corollary proves theory-level NIP from
  037's o-minimality and the o-minimal => NIP theorem; packet 037's note says the reduction is owed here.
- handbook/parts/p03/countable-models-and-fra-ss-constructions-w03-p03-015.tex: QE/types of T_RG.
- handbook/parts/p03/presentations/n-a-001-01.tex: T_dlo pattern truth (QE).
- handbook/parts/p03/indiscernibles-ehrenfeucht-mostowski-models-and-cardinal-w03-p03-028.tex: Ramsey A.

## Open items (in the duties' own words)

- D-P4-009-GOAL-02 / GOAL-03: written this run (T_dp, thm:p03-w03-p03-035-dense-predicate; table rows for
  the structure-level transfer, NIP not => o-minimal, and expansions). The structure-to-theory transfer
  (Knight--Pillay--Steinhorn) is stated and cited to Simon A.1.3 p. 148, not proved; the KPS paper is not
  held by this packet. Packet 036 shares unit ED26-REQ-D-P4-009-01 and owns 34.5; it should cref
  thm:p03-w03-p03-035-dense-predicate instead of writing a second NIP non-o-minimal example.
- N-a-010-MAP-04: complete. stable => simple is proved via the local dividing rank (no forking = dividing).
- N-a-010-MAP-02 / C01 (Shelah 1971): Lemmas 2.2 and 2.3 ((C)=>(D)=>(A)) are proved
  (thm:p03-w03-p03-035-shelah-tree). Not proved: Lemma 2.1 ((B)=>(C), which uses the Erdos--Makkai
  theorem, also not proved), the rank lemmas 2.4--2.8 ((D)<=>(E)<=>(F)); Theorems 2.13, 3.8, 4.1--4.4 are
  described, not proved (4.1's theory-level unstable => IP or SOP is proved by Simon's route). The
  unstable-spectrum paper (Shelah1971NonIsomorphicModels) was not opened; it is distinguished only through
  the Stability paper's own citations (p. 287, G6--G7).
- N-a-010-C01 (Simon): Proposition 2.55, Theorem 2.60, Proposition 2.69, Baldwin--Saxl (Theorem 2.13),
  Example 2.12 items on trees, C-minimal theories and Q_p, Appendix A.1 colored orders are not presented.
- N-a-010-MAP-03: Tent--Ziegler 2012 is not held (unit ED26-REQ-N-a-010-03 has no held path); the
  tree/local-character equivalence in their presentation cannot be written from the source. The dividing,
  forking and base-bound facts needed here are proved in the chapter's own route.

## Continuation

- Block 1 (earlier run): body 34.1--34.4 and annex written; unit-compile ok; fused-space check clean.
- Block 1 (this run, 2026-10-12): (a) stable => simple upgraded from sketched to proved through the local
  dividing rank D_{delta,k} (def:p03-w03-p03-035-drank, thm:p03-w03-p03-035-drank-calculus,
  thm:p03-w03-p03-035-stable-simple); the route avoids forking = dividing (coding finitely many disjuncts
  into one formula, minimal-rank formulas give the base); types in infinitely many variables and arbitrary
  models handled. (b) NIP non-o-minimal ordered example T_dp = (R,<,Q) type theory
  (def/thm:p03-w03-p03-035-dense-predicate): QE, completeness, NIP, not o-minimal, unstable, SOP.
  Table updated. k-inconsistency made index-wise in the ambient convention. unit-compile ok.
  (c) Shelah Lemmas 2.2--2.3 proved (Cantor-set placement of the tree; level-collapsing compactness for
  height mu). unit-compile ok; check.py: only the intake bib-key finding.
- Next, in order: (1) Shelah Lemma 2.1 with a proof of the Erdos--Makkai theorem, and Lemmas 2.4--2.8
  (held pp. 299--302); (2) open copy of Shelah1971NonIsomorphicModels; (3) remaining Simon results.
- Block 2 (2026-10-12): Simon Example 2.4 (held PDF p. 14) Boolean-algebra item: Simon states only that
  pairwise disjoint sets are shattered. Added thm:p03-w03-p03-035-boolean-algebra-ip (body after the
  example) with annex proof: splitting x -> (x^a, x^(b^-a)) is injective on B|b, recursion keeps an
  infinite piece and collects disjoint nonzero pieces; joins shatter. Removed the "used as stated" sentence.
  unit-compile ok; fused-space check clean.
- Routing (MAP-01): body/annex files still need the driver \input lines per the packet insertion proposal
  (lead action).
- Next, unchanged: Shelah Lemma 2.1 / Erdos--Makkai and Lemmas 2.4--2.8; remaining Simon results.


## Author correction, 26 October 2026

Added the missing annex proofs for Shelah's local-rank basics, rank/tree
equivalence, and Theorem 2.9. The rank/tree proof explicitly shows that types
with trees of all finite heights survive every ordinal stage, instead of
silently treating rank at least omega as infinite. The body now qualifies
finite determination as uniqueness among extensions retaining the rank;
lower-rank extensions are not excluded by that result.

These are complete author arguments for the stated lemmas, using the held
Shelah1971Stability presentation and the packet's explicit compactness and
saturation conventions. They do not establish fidelity to unavailable exact
book editions. The source boundaries and unfilled source obligations remain
unchanged. The symbol intake now preserves the original commas in Gamma and
the dividing-rank subscript using proper CSV quotation. The main build and
independent admission are separate from this correction pass.


The final transfer in the simplicity proof now chooses its saturation level
above the length of the variable tuple as well as the model and theory sizes.
This makes the earlier small-tuple argument applicable to every type allowed
by the definition, including types with arbitrarily many variables.

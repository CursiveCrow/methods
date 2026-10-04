# w02-p01-011 research note: finite coding over an infinite cardinal; syntax counting

Packet: work/waves/w02/packets/w02-p01-011.json (P1, sections 4.5 and 4.6,
label_tag p01-w02-p01-011, toc tag `%% toc: P1 4 4.5,4.6`).

## Sources opened in this session

- source/formal-logic-reference.tex (FLRV1, Version 1.0), lines 363--680
  (set prerequisites: pairs, products, A^n, finite and countable sets,
  cardinal comparison, Cantor--Schroeder--Bernstein, Cantor, transitive sets,
  ordinals and cardinals, transfinite recursion), 640--750 (choice
  principles, thm:infinite-cardinal-finite-coding 679--694,
  cor:syntax-counting 696--710, its proof 712--732, closing paragraph
  733--744), 1101--1290 (finite sequences, strings A^*, pair_N,
  countability of strings, concatenation, inductively generated sets,
  structural induction and recursion), 10353--10380 (ordinal trichotomy
  statement, proof sketch only).
- handbook/restoration/inherited-00648-00744.tex lines 1--97 (active capture
  of the same block).
- Halbeisen, Combinatorial Set Theory (held, first-edition author
  manuscript): opened for a search only; text extraction was unusable and no
  locator from it is used.

## Provenance of the new text

The statements of thm:p01-w02-p01-011-finite-coding and
thm:p01-w02-p01-011-syntax-counting follow FLRV1 lines 679--710 exactly
(statement wording and notation). Every proof, lemma, example and warning in
the two new files is an editorial completion built only from the inherited
definitions of FLRV1 lines 363--680 and 1101--1290. No proof is attributed
to an external source. Jech2003 (not held) is not used.

Corrections relative to the inherited capture (proposed as patch requests,
work/waves/w02/patches/w02-p01-011.json, because handbook/restoration/ is
read-only for this packet):

1. thm:infinite-cardinal-finite-coding carries "Status: cited theorem" and
   the closing paragraph cites Jech2003; the local proofs now exist, so a
   pointer to them is proposed.
2. The corollary proof's forward pointer ("the string chapters below record
   this fact for formulas") is replaced by a reference to the grammar lemma
   thm:p01-w02-p01-011-grammar-strings.
3. The corollary proof applies clause 4 to Sigma, X, emptyset, ... without
   showing |X| <= kappa; the new proof derives it from N subset of kappa
   (thm:p01-w02-p01-011-infinite-ordinals, item 1).

## Choice bookkeeping (for the proofs as written)

- Theorem on squares (mu x mu ~ mu): no choice.
- Clause 1: no choice beyond fixing one bijection (existential instantiation).
- Clause 2: AC selects one injection kappa^n -> kappa for each n >= 1.
- Clause 3: the finite-alpha case uses no choice; the infinite-alpha case uses
  AC to select an enumeration of each A_beta.
- Clause 4: AC selects an injection A_n -> kappa for each n.
No independence claim is made in reader text (no held source read for it).

## Continuation

Components written (block 1): FLRV1-U00045 (theorem with local proofs of all
four clauses), FLRV1-U00046 (corollary restated with local proof),
FLRV1-U00047 (the inherited proof's steps, with the grammar step and the
aleph_0 <= kappa step written). Remaining open items: lead to apply the patch
requests and insert the two driver lines; symbol intake to be merged.

Block 2 (2026-10-04): the only gaps reported were G1 guard hits on
spec/research/edition-2026-p02-completeness-choice-scope-w02-p02-054{.md,-return.json}
and spec/research/edition-2026-p02-unit-accounting-w02-p02-04{2,4,5}{.md,-return.json}.
None of these was written by this packet: they are the research notes and
returns of packets w02-p02-042, -044, -045 and -054 (files dated 04:01--04:11,
after this packet's last write at 03:39; the -054 pair no longer exists in the
tree). They are other agents' owned files, so this packet neither edits nor
reverts them; the guard must attribute changes per packet (lead action).
Re-verified this block: unit-compile ok (0 errors, 5 overfull), find_fused_spaces
no hits, check.py filtered shows only bib-key for the own intake key
FrozenFormalLogicFiniteCoding; chapter locators re-read at source lines 365,
648 and 1101; annex proofs of the square theorem and clauses 1--4 re-read
(choice-function selections over {I_n}, {E_beta}, {J_n} remain correct when
two family members coincide). No content change was needed.

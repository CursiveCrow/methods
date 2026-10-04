# Standard small-clause pipeline: paused authoring checkpoint

Paused for the user's coverage-map priority on 9 September 2026.
Body: handbook/parts/p12/small-clause-standard.tex. It is not routed.
The corresponding annex does not exist; thirteen proof destinations in
the draft are promises of work, not completed proofs or admission.
No source note or canonical bibliography/notation merge has yet been completed.

Source: retained Nonnengart–Weidenbach chapter, Computing Small Clause
Normal Forms, printed 2001 identity and pp. 335–367. Selected root extent
is introduction and Sections 2–3 through p. 347, HAR2001-C06-G01.
The optimization author owns G02–G05 in the separate saved files.
Held PDF: tmp/acquisition/src037/dfki-small-clause-retry-01.body.derived-decompressed.ps.derived-render.pdf.
SHA256 41EA6003E78E88D20EBE639EF7943F6A4BCC983D8F074D73F41B72C28AA32264;
286434 bytes, 33 pages. It is a PostScript-rendered presentation, not
a publisher-byte-equivalence claim. Title identifies Nonnengart and
Weidenbach as authors, Boy de la Tour and Egly as second readers.
Printed page = physical page + 334. The selected text and original
formula-page images were read; higher-resolution pages 1–13 are in
tmp/pdfs/p12-small-clause-source/. The old extraction loses some glyphs.

## Proof design preserved for continuation

- Open input means existence of a satisfying valuation. Existentially close
  exactly its free variables before the closed pipeline; a stipulated
  universal closure is a different input convention.
- Contextual equivalence/implication is pointwise at every valuation in a
  fixed model class. Background assumptions used for a relative rewrite
  must remain part of the problem.
- Initial simplification terminates by strict formula-tree node decrease.
  The full twenty-rule collection and nonempty-domain quantifier guards
  are in the body.
- NNF weights: atom 1, negation 2a, quantifier a+1, conjunction/disjunction
  a+b+1, implication 3a+2b+2, equivalence 6a+6b+6. Every permitted
  rewrite strictly decreases, including duplicating equivalence expansions.
- Miniscoping measure is the sum of 3 to the number of Boolean nodes in
  each quantifier's scope. Other scopes' Boolean counts are unchanged.
  Replace 3^(a+b+1) by 3^a or by 3^a+3^b. Correct the draft's word
  positive to nonnegative, because a quantifier-free formula has sum zero.
- Raw variable-renaming needs injectivity on occurring variables, not on
  the entire identity-extended alphabet. Prove the valuation lemma for
  both quantifiers; indexed fresh blocks prove rectification and unchanged
  free variables even when earlier raw renaming temporarily shares binder
  names that the recursion subsequently separates.
- For each local Skolem step, choose a fresh symbol outside the declared
  current signature. Choose one witness per nonempty free-parameter fiber
  under Choice, and a fixed default elsewhere. Coincidence and substitution
  lemmas give pointwise equivalence of the local existential and selected
  instance in the constructed expansion. Reverse implication is choice-free;
  NNF polarity lifts it to the whole sentence.
- Pull universals before distributing the matrix. Pulling decreases the
  total Boolean-ancestor count of quantifiers and preserves rectification.
  Matrix distribution decreases weights literal 2, conjunction a+b+1 and
  disjunction ab. Premature distribution can duplicate binder names and
  block the side condition for a fully prenex result.
- Clause instances are universal consequences by the term-substitution
  valuation lemma. Retained subsumption witnesses justify deletion;
  duplicate removal plus reverse subsumption proves condensation equivalence.
  Clause count plus literal-occurrence count decreases. Do not delete
  every member of a mutually subsuming cycle simultaneously.
- The running example yields the unit R(u,u) and the clause
  P(a) or R(v,f(v)) or Q(w), not the source's three pairwise disjunctions.
  For the failure case use domain {0,1}, off-diagonal R, P and Q universal,
  a=0 and f swapping the two elements. The three false-output clauses hold
  but the diagonal unit does not. Adding universal not-R(x,x) makes the
  original input inconsistent while that false output is satisfiable.

No author read-through of a completed proof batch has occurred. Resume
from the actual saved body and this checkpoint after the coverage map.

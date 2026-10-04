# Corrections incorporated into the manuscript

The user directed that mathematical errors be corrected in the actual book.
The active files under handbook/restoration/ are reader text reached by
the part drivers. The frozen source/formal-logic-reference.tex remains an
archive of the earlier manuscript.

## Set theory

In inherited-10675-10769.tex, the definable-subsets definition now declares
Def(empty) = {empty} before applying satisfaction to nonempty sets. The
hierarchy explicitly gives L_1 = {empty}. The relocated label
def:p06-def-empty-base identifies that definition.

In inherited-11104-11126.tex, the two conjunctions in the relativization
lemma now use 1 <= j <= m and 1 <= i <= k. Empty conjunctions are true,
and an empty universal quantifier block is omitted. The old correction
label remains an alias on the actual lemma.

In inherited-11127-11199.tex, the nonemptiness proof now calculates
empty in L_1 subset L from the base definition. It no longer invokes
satisfaction on the excluded empty domain.

The Part VI driver no longer includes constructibility-base-erratum.tex
or relativization-index-erratum.tex. The source map and lookup table now
refer to the integrated definitions and lemma. The uninput files retain
the previous editorial text as history.

## Nonclassical semantics

In inherited-13972-14000.tex, the IMLL sequent clause includes n = 0,
sets the empty tensor to the monoidal unit, and derives validity of
the empty-antecedent unit sequent from 1 <= 1. The existing empty-tensor
label now anchors this complete clause.

In inherited-13519-13551.tex, the language introduces group operators for
nonempty finite groups, matching the registered common-knowledge calculus.

The Part VIII driver no longer includes imll-empty-context-erratum.tex
or group-operator-convention.tex. Its source map records the integrated
clauses. The old uninput files remain historical material.

## Temporal logic

The source readings and reasons for the corrections to Emerson--Halpern's
Theorems 5, 6, and 10 are recorded in
p09-emerson-halpern-1986-source-note.md.
The active N-c-016 presentation supplies the corrected separation targets,
the MPL temporal clauses, the full translation induction and its suffix
corollary, and the full R-generability characterization proof.
An independent mathematical reader found that the earlier Theorem 5 witness
used infinitely-often F while its base models supported ordinary F.
The primary theorem and figures confirmed ordinary F. The statement,
both separating invariants, and the prior source-note transcription were
corrected. The active text now gives the exact recursive models and proves
their separating property.

## Automata, arithmetic, and stream operators

The active N-c-014 arithmetic presentation now uses the binary bit-occurrence
relation in the signature (N, +, in_2). Both directions of the finite-set
translation are explicit, including finite carries for addition and the
canonical simultaneous binary encoding. The valid unary-reduct decidability
consequence is retained.

The graph-portion theorem now uses the family of residual maps. For a total
zero-anticipation operator over finite nonempty alphabets, graph homogeneity
is equivalent to finiteness of that family, and degree is its size plus
one precisely when an inconsistent paired prefix supplies an empty portion.
The proof and the weight-two, degree-four example are in the actual text.

The infinite synthesis reduction now constructs the finite union by fixing
each initial window, deriving its sliding-window relation, and imposing
that initial word. The tagged-union reduction and its unary-window case
follow. The window bound covers a matrix with no individual terms.

Historical source discrepancies are retained in
p09-buchi-1960-source-note.md, p09-trakhtenbrot-1961-source-note.md, and
p09-elgot-1961-source-note.md.

## Verification

The set-theory and nonclassical corrections received a bounded independent
reading of the actual LaTeX. That reading found no mathematical defect in
the corrected clauses, their zero cases, or the relocated references.
The MPL translation, R-generability proof, and corrected Theorem 5
model argument also received independent readings of their actual LaTeX;
the readers found no remaining defect in those bounded scopes.
The three N-c-014 corrections received a final independent mathematical
reading of the actual text. Both arithmetic translations, the canonical
encoding, the finite-union and tagging constructions, and the
residual-degree theorem and example passed that bounded reading.
Publication metadata based on historical exact-copy hashes is not
evidence of the corrected manuscript's current mathematical status.

# Model-theory foundations correction on 26 October 2026

## Substantive additions

Packet w03-p03-006 now supplies the previously omitted disjoint elementary
amalgamation theorem over an algebraically closed common set. Two reciprocal
theorem/annex pairs give a finite-avoidance lemma and the diagram construction.
The finite-set argument proves that a family of nonempty finite sets with no
meeting set of size at most k has a finite subfamily with that property. It
then makes the union of all minimum meeting sets a finite definable set.
This justifies simultaneous avoidance; infinite coordinate projections alone
do not suffice. The pre-existing elementary-substructure theorem remains.

Source checked: Martin Speirs, Math 225A notes from Thomas Scanlon's course,
Lecture 19, printed pp. 3-5 (physical PDF pages 4-6), Theorem 2 and its sketch,
https://math.berkeley.edu/~scanlon/225af13lectures/20130511Lec19.pdf .
The new finite-set proof is an editorial completion, not a claim that the
source prints that proof. The source's algebraic-closure hypothesis in one
structure suffices; the manuscript proves its transfer to the other.

Packet w03-p03-010 had incorrectly called saturation for tuples of length
below kappa a stronger requirement. The new corollary and reciprocal annex
proof show that finite-tuple kappa-saturation realizes complete types in at
most kappa variables over fewer than kappa parameters, with formulas still
finite. The transfinite construction tracks all finite-support formulas.
A pure equality model of size kappa supplies the boundary at kappa-plus
variables. The original construction and its saturation convention remain.

## Standing

These are author corrections and new proofs. They are not independent
source-fidelity, specialist or publication admission, and do not close the
full source-presentation obligations. Shared drivers, canonical bibliography
and canonical symbols are owned by the lead integrator. The existing intake
for packet 006 adds the algebraic-closure role. No citations were invented.

## Cross-packet and boundary corrections

Packet 018 now points explicitly to packet 017 for regularity of mu and
the proofs of parts 1 and 2 of Shelah's theorem. The obsolete statement
that part 1 is not proved in the handbook is removed. Part 3 and goodness
remain cited boundaries. The comparison of index sets is stated as two
sufficient bounds, without asserting optimality.

Packet 026 now distinguishes prefix syntax from equivalence for the empty
conjunction/disjunction. Empty finite diagram cases in the embedding and
return-to-elementary-extension proofs are treated separately; the step-up
proof gives an explicit quantified tautology when its diagram subset is
empty, avoiding a stray free variable.

Symbol-intake repairs in 003, 017, 018, 022 and 026 correct CSV quoting,
separately wrapped symbol families and the scope of actual first uses.
The typed mathematical roles are retained; no canonical registry is edited.

## Verification completed in this author pass

All nine assigned body files and nine matching annexes passed a scoped
mechanical check: 132 theorem-class statements, 129 reciprocal proved or
sketched annex items, balanced environments, and 114 well-formed intake rows
across nine CSVs. This does not certify the mathematical correctness of all
132 statements or independent source admission.

A focused fixture for packets 006 and 010 compiled with pdflatex and Biber
to 35 pages; Biber resolved all three cited keys. The new theorem/proof pages
were rendered with Poppler and inspected. This fixture omits the rest of the
book, so its external cross-references are intentionally unresolved and its
existing text still produces overfull-box warnings. The leading formula in
the new finite-avoidance lemma was shortened to prevent its new overfull line.

The substantive close reading includes the new proofs, packet006's elementary
amalgamation arguments, packet010's saturation construction, packet003's
least-family proof, packet022's Presburger and ACF elimination arguments,
packet020's order-extension/real-closure algebra, and packet026's modern
preservation proofs. Other assigned material received selective consistency
checks, not a complete fresh source-fidelity review. The remaining historical
and source obligations are retained; none is marked accepted by this pass.

## Scoped notation follow-up

The later strict-check report identified 72 font-symbol families outside their registered scopes in these nine packets. Added 89 typed rows in `handbook/registry/symbols-intake-p03-foundations-scope.csv`, after reading the local uses. The modern preservation proofs now have the bounded subsection anchor `sec:annex-p03-w03-p03-026-modern`; the existing Los 1955 subsection retains its separate formula-set meanings. Structures, formula sets, diagrams, polynomial lists, ordered-field families, ideals and ultrafilters were not collapsed into one symbol role. This is an intake for canonical integration, not a claim that all book-wide notation is complete. The nine body/annex pairs still pass the 132-statement / 129 reciprocal-item mechanical check with no errors.

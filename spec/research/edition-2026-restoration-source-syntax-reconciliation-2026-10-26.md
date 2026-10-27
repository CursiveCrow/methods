# Corrected reader provenance reconciliation, 26 October 2026

This author audit reconciles three stale version-1 provenance records with
already-written, explicitly documented active-manuscript corrections. It
changes no frozen source, reader theorem, proof, source label, or bibliography.
It does not perform or claim independent mathematical or source admission.

The governing authority is the edition contract's “Reader-facing content and
corrections” policy and the 6 September 2026 correction amendment in
`handbook/CONVENTIONS.md`. Version 4 records exact current reader identity,
every changed source-to-reader line range, and the preserved predecessor.
All completeness and independent review/build/visual gates remain as recorded.
A valid restoration scope permits literal historical label syntax; it does
not grant new author text a blanket exception to the handbook label taxonomy.

## SRC-06942-07134

The active ultraproduct section differs from source lines 6942–7134 only by
its theorem's original-source citation, `Los1955` to
`Los1955Ultraproducts`, and omission of one final blank line. The former key
names *On the Extending of Models I*; the latter names the original
ultraproduct chapter. The reason and metadata check are already recorded in
`spec/research/p03-los-citation-correction-2026-09-09.md`. Both bibliography
keys remain distinct. The theorem, hypotheses, complete proofs, examples,
and literal `lem:los-terms` / `cor:diagonal-ultrapower` labels are retained.
Their prefix findings were consequences of the stale exact-capture record,
not new author label errors. No primary-source-body admission is inferred.

## SRC-09439-09497

The active diagonal-lemma section has an explicit malformed/non-unary input
default `code(0=0)`, a fixed distinguished free variable x_0 and fresh-variable
coding conventions. It links the actual graph construction and fixed-point
proofs at `annex:p05-rep-diagonal-graph`, `annex:p5.inc.diagonal-coding`, and
`annex:p5.inc.diagonal`; these three targets and reciprocal theorem declarations
are present. The status and explanatory paragraphs now distinguish a complete
strong-graph argument from insufficient numeralwise output instances. The
changes were previously documented in the P5 representability and
incompleteness source notes. The original `ch:first-incompleteness` and
`thm:diagonal-lemma` labels and the explicit fixed-point calculation survive.
One terminal blank line was removed. This reconciliation validates that edit
map, not the independent acceptance of its PA/Q dependencies or historical
source presentations.

## SRC-11961-12029

The active normalization passage explicitly uses NJ_v, allowing empty discharge
classes in implication introduction and the indicated disjunction/existential
branches. The remaining rule and eigenvariable conditions are retained. This
repairs the false claim that the prescribed reductions preserve a calculus
requiring every discharge class to be nonempty: erasing an unused conjunction
branch can empty a surrounding discharge. The correction and counterexample
are documented in `spec/research/p07-normalization-discharge-correction-2026-09-09.md`.
The former sketch now invokes the supplied, reciprocally linked corollary
`thm:p07-nj-principal-permutation-normalization` and its full proof at
`annex:p7.nj.principal-permutation-normalization`. The historical chapter and
section labels and principal-reduction display are preserved; one terminal
blank line was removed. The author note keeps Prawitz and
Troelstra–Schwichtenberg source-presentation obligations distinct. This record
reconciliation does not assert those unavailable source duties are complete.

## Verification scope

For all three records, compare the frozen interval with the current reader,
retain the old record byte for byte in provenance/history, and validate the
version-4 edit map with `tools/check_inherited_restoration.py`. Only identity,
unchanged spans, candidate schema and the explicit pending boundaries are
claimed. The root remains responsible for the complete route, source-unit
record joins, document build and the independent acceptance workflow.

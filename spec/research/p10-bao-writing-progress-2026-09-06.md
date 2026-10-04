# Boolean operators, canonical extensions, and modal completeness

Date: 2026-09-06.

## Manuscript work

The active Part X host and annex now include three matching body/proof
fragments:

- boolean-operators.tex;
- modal-algebra-completeness.tex;
- polyadic-modal-algebras.tex.

They replace the former brief BAO definition and representation/completeness
paragraph while retaining its references and the adjacent topological
semantics statement.

The full finitary operator signature is retained: an arbitrary set of
symbols, each of finite arity, including zero. Nullary symbols designate
arbitrary Boolean elements. Trivial algebras and empty canonical frames
are included explicitly in the algebraic duality; the modal semantic
classes used for local completeness explicitly require nonempty frames.

## Twelve complete proof pairs

| Body result | Annex proof |
| --- | --- |
| thm:p10-bao-ultrafilter-witness | annex:p10.bao.1 |
| thm:p10-jonsson-tarski | annex:p10.bao.2 |
| thm:p10-bao-canonical-completion | annex:p10.bao.3 |
| thm:p10-bao-descriptive-representation | annex:p10.bao.4 |
| thm:p10-bao-descriptive-duality | annex:p10.bao.5 |
| thm:p10-modal-algebra-completeness | annex:p10.modal-algebra.1 |
| thm:p10-modal-general-frame-completeness | annex:p10.modal-algebra.2 |
| thm:p10-modal-general-frame-strong | annex:p10.modal-algebra.3 |
| thm:p10-modal-canonicity-completeness | annex:p10.modal-algebra.4 |
| thm:p10-polyadic-algebra-completeness | annex:p10.polyadic.1 |
| thm:p10-polyadic-canonical-truth | annex:p10.polyadic.2 |
| thm:p10-polyadic-local-completeness | annex:p10.polyadic.3 |

The simultaneous witness lemma enlarges coordinate filters one at a time
under BPIT, maintaining the universal tuple condition. The bad-element
ideal uses meets of witness tuples in every other coordinate. The same
strong filter lemma proves the full bounded-morphism back condition;
properness of the image-generated filters is established from the
assumed source edge, operator preservation, and normality.

Canonical completion is proved dense and compact, and its Boolean
uniqueness is established through the atoms p_U. The equivalence between
image-subset and closed/open-family compactness is proved, with only
finite originating-index selections. No uniqueness of arbitrary operator
extensions is inferred from Boolean uniqueness. The finite/cofinite
example illustrates failure to preserve an existing infinite join.

Descriptive general frames receive full definitions and reconstruction,
including the topology, admissible clopens, tight relations, morphisms,
and natural duality maps.

The modal sections prove algebraic completeness, canonical truth, and
strong local general-frame completeness, first for unary box and then
for all finite arities. Infinite premise sets are handled by finite
deduction and BPIT. Valuation arguments use finite formula
representatives, or unique algebra preimages, without global Choice.
The general and unary closure rules are compared explicitly.

Ordinary Kripke completeness is stated with its additional
canonical-frame-validity hypothesis. Closure of the algebra class under
canonical extension is proved sufficient. The all-variable-set
canonicity convention is separately recorded, with no unsupported
converse from one fixed-language frame.

## Primary source and review

The held Venema file is an 86-page preprint dated 19 October 2005,
despite its added header citing the 2007 published chapter. The new
bibliography key Venema2005Preprint preserves this distinction.
All technical page locators refer to the preprint.

The exact source packet is p10-bao-source-note-2026-09-06.md. It
identifies Definitions 3.11, 5.12, 5.16, 5.24–5.27, representation
Theorem 5.15, descriptive duality Theorem 5.28, and the algebraic and
canonicity results on pp. 10–11 and 31. The source states representation
for all finite arities but prints only the unary operator proof; the
manuscript supplies the full tuple argument. The source's proof-direction
and notation slips remain recorded as historical readings in that note.

Independent reviews read the actual LaTeX and found no remaining
mathematical defect in the scoped proofs. Detailed records include:

- p10-bao-completion-review-2026-09-06.md;
- p10-modal-algebra-completeness-review-2026-09-06.md;
- p10-polyadic-modal-source-review-2026-09-06.md.

The additional independent representation/morphism and polyadic
mathematical reviews were delivered in the task messages.

## Integration and limits

The Part X theorem/definition register was regenerated with 66 rows.
The named-theorem index was updated from generator output for Part X
and contains all twelve new proof links. Twenty-six notation rows were
added; the existing formatter regenerated both symbol tables with
754 entries. The scoped git whitespace check passed.

No software tests, manuscript build, or manuscript page renders were
used. This supplies the described mathematical development for N-d-011;
it does not establish complete reconstruction of every registered
primary source or whole-book publication readiness. Source acquisition,
remaining content obligations, broader navigation consistency, final
compilation/layout, and publication acceptance remain open. The full
manuscript goal remains active.

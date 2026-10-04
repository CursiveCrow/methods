# HTN planning: exact 1996 source and complete authoring

Date: 9 September 2026. Unit: `ED26-P17-PRACT-003`.

## Acquired source and reading extent

The complete selected paper was acquired from
<https://www.cs.umd.edu/~nau/papers/erol1996complexity.pdf> at
`tmp/pdfs/p17-htn/erol1996complexity.pdf`.

- Kutluhan Erol, James Hendler and Dana S. Nau, *Complexity results for HTN
  planning*, *Annals of Mathematics and Artificial Intelligence* 18 (1996),
  printed pages 69–93.
- 25 physical pages, 1,555,264 bytes.
- SHA-256: `DA21CAF0E238A2DFDA75FCCC7510171C356850E451E1957BCA1C7F726C57AAE0`.
- The PDF is a scan with an OCR text layer; its 2005 PageGenie metadata is
  digitization metadata, not a different publication year.

All 25 pages were read, including formal syntax and operational semantics,
every restriction theorem, the comparison with STRIPS and all appendix proofs.
The actual embedded scan images of printed pages 76, 82 and 88 were inspected
because OCR obscured interval inequalities and algorithm details. These were
extracted from the acquired PDF and converted losslessly from TIFF to PNG;
no manuscript PDF was rendered. In particular, p. 76 explicitly gives the
interval convention `pi(left) <= e < pi(right)`.

The earlier source was separately acquired from
<https://www.cs.umd.edu/~nau/papers/erol1994htn.pdf> at
`tmp/pdfs/p17-htn/erol1994htn.pdf`.

- *HTN Planning: Complexity and Expressivity*, AAAI-94, pp. 1123–1128.
- SHA-256: `AB5C3C7097B0329DE6CE3E317B68E6610504AC2ADBDA4C8FF716C642085F8CA6`.
- Its first page identifies the 1994 proceedings, and its p. 1126 footnote
  delegates all proofs to a separate 1994 report. It is used here for provenance,
  not as a replacement for the 25-page 1996 proof source.

## Completed component allocation

| Component | Completed treatment |
| --- | --- |
| C01: tasks, operators, methods and constraints | `def:p17-htn-vocabulary` through `def:p17-htn-method`: exact function-free roles, unique occurrence labels, literals, Boolean state/ordering constraints and explicit dummy actions |
| C02: reduction, grounding, ordering and solution relation | `def:p17-htn-completion`, `def:p17-htn-solutions`, `thm:p17-htn-finite-derivation`; full ancestor-constraint endpoint replacements and finite fixed-point semantics |
| C03: plan existence and restriction results | `thm:p17-htn-semidecision`, `thm:p17-htn-undecidable`, `thm:p17-htn-fixed-undecidable`, `thm:p17-htn-levels`, `thm:p17-htn-total-order`, `thm:p17-htn-regular`, `thm:p17-htn-primitive`, with complete annex arguments |
| C04: comparison with STRIPS | `def:p17-htn-strips`, `thm:p17-htn-strips-embedding`, `thm:p17-htn-expressivity`; exact observation map, existence preservation and nonregular solution-language separation |
| C05: worked plan and failures | `def:p17-htn-preparation`, `thm:p17-htn-example`; explicit parameter grounding, complete state traces, failed protection, executable but method-excluded shortcut and recursive-search boundary |

Thirteen reciprocal body/annex proof pairs supply these results and two
supporting constructions: the exact context-free-intersection undecidability
premise and a complete finite trace-summary lemma.

## Direct corrections and proof reconstruction decisions

The active chapter states correct claims and constructions. The historical
readings below remain provenance outside the reader's derivations.

1. **Two-task undecidability bound.** The 1996 theorem says at most two tasks
   in each input network/method, but its displayed reduction at p. 85 starts
   with two grammar tasks plus a third final-check task. The written reduction
   uses exactly two initial tasks and tests `turn` after `last[u,v]`. This uses
   the source's own endpoint syntax, preserves its alternating-word proof,
   and meets the stated bound without a third node.

2. **Fixed-domain method count.** The p. 86 construction lists five terminal
   or dummy methods and one binary grammar method. The written proof states
   the actual count: five operators and six methods. Static ternary `R` facts
   supply the grammar productions, and reserved constants remain distinct
   from all grammar nonterminals.

3. **Regularity.** Section 2.3, p. 75, requires the unique nonprimitive task
   to be ordered relative to all other tasks; it can occur between primitive
   tasks. Table 1 describes the stricter case in which it follows them all.
   The chapter uses the section 2.3 definition and identifies right-linear
   methods as a special case. The lower-bound encodings meet that stricter
   special case too. A regular HTN problem can nevertheless generate the
   nonregular language `a^m b^m`, so regularity of problems is not mislabeled
   regularity of their entire solution languages.

4. **Full Boolean interval semantics.** The published p. 88 procedure splits
   intervals into adjacent constraints and presents a table indexed by a
   protected literal set. Its displayed propagation does not explicitly
   account for all enclosing protected requirements, negated intervals or
   the interior of intervening compound tasks. The new proof gives a complete
   finite summary: entry, first-post, last-pre and final states; four exact
   literal-intersection sets; and a length-one flag. Composition formulas and
   evaluation of every possible first/last interval are proved. Negating a
   universal protection condition is not replaced by universally protecting
   the opposite literal. This is an explicit corrected tabulation argument,
   not a claim that the printed pseudocode already contains these details.

5. **Space bounds terminate.** The regular-case proof uses one pending task
   and its exact summary. A bounded counter explores the finite graph of such
   obligations; repeated obligations can be removed from an accepting path.
   Thus the nondeterministic space argument has a finite accepting-search
   bound and handles both primitive prefixes and primitive suffixes. Savitch's
   theorem is bound to the existing `thm:p04-savitch` interface.

6. **Classical-planning lower-bound premises.** Rather than merely re-citing
   the external classical-planning hardness used by the source, the annex
   supplies explicit machine simulations. The fixed-domain polynomial-space
   construction stores cells as constants and neighbors as static facts.
   The exponential-space construction uses variable-arity bit tuples and a
   compulsory initialization phase. It does not put exponentially many blank
   facts into a supposedly polynomial-size input. The subsequent right-linear
   HTN encoding preserves the one-compound-symbol and binary-body restrictions.

7. **Grounding and relevant atoms.** Counts use explicit input syntax and
   relevant ground atoms. In the propositional case no exponential set of
   unmentioned tuples is needlessly materialized. For fixed domains, schema
   arities are fixed; predicates used only in initial constraints are static
   and can be evaluated after guessing the initial bindings. The proof does
   not claim that all simultaneous initial-network groundings are polynomially
   numerous.

8. **Bookkeeping in the STRIPS encoding.** The source construction appends a
   final effect-free action but then informally identifies the two plan sets.
   The chapter explicitly distinguishes literal plans `sigma done` from the
   observed plan `sigma`; erasure is not called symbol renaming. This also
   accounts for an empty original STRIPS plan.

9. **Translation hypotheses.** Theorem 9 on p. 82 writes an overloaded map on
   both instances and plans, with preservation only for images of source
   plans. That condition alone does not state that every target solution has
   a source antecedent, which the adjoining decidability argument needs.
   The chapter proves the precise impossibility of a computable translation
   preserving plan existence in both directions. It separately proves the
   regular/nonregular language obstruction under symbol renaming, and also
   under an explicitly stated erasing observation map. No unproved condition
   is silently substituted into the source's displayed formula.

10. **Endpoints and empty accomplishments.** Method decomposition uses the
    source's first/last replacement semantics and nonempty bodies. The already
    true goal uses its explicit dummy task. No undefined `first[]` or `last[]`
    is introduced by silently treating an empty method body as an ordinary
    nonempty expansion. An empty initial primitive network is checked directly.

The total-order lower and upper bounds remain distinct: EXPSPACE-hard versus
double exponential time, and PSPACE-hard versus EXPTIME in the propositional
case. No later matching-completeness result is substituted for the selected
1996 presentation.

## Prerequisites and completion standing

The complete construction map allocated the context-free-intersection and
classical-planning premises locally in `ED26-P17-PRACT-003/PRE-004`.
The authored `thm:p17-htn-cfl-intersection` now proves the exact grammar
intersection premise from the existing `thm:halting-undecidable`: alternate
forward/reversed computation histories let two pushdown automata check the
even and odd adjacent transitions. The proof includes the effective
pushdown-to-grammar construction and binary/normal-form restrictions.
The new proof does not assert that this is the text of the 1979 textbook
cited by the original paper. The latter's bibliographic identity remains
in the source-specific intake for accurate attribution.

The planning hardness premises are discharged by the explicit simulations
described above. The remaining foundational interfaces are the handbook's
ordinary Turing-machine/complexity definitions, its halting theorem and its
Savitch theorem, with exact existing labels; no source-size substitution or
unbound imported planning theorem is used.

Owned files are the P17 body and annex with slug
`hierarchical-task-network-reasoning`, `handbook/bib/intake-p17-htn.bib`,
`handbook/registry/symbols-intake-p17-htn.csv`, and this note. Drivers, shared
style and canonical bibliography/symbol records remain the lead's work.
The five local components are authored. Independent source fidelity,
mathematical acceptance, consolidated manuscript checks and publication
acceptance remain later work; no review wave or manuscript build was run.

The full written body and annex, including the final language-theoretic
prerequisite, received an author read-through. The thirteen status targets
match thirteen reciprocal annex back-references; all thirteen proofs have
complete proof environments and the body has none. The symbols intake has
seventeen seven-column rows. As a direct mathematical calculation, the four
trace-intersection composition identities were checked on all 28,224
compatible pairs of one-to-three-action traces over two Boolean atoms, with
zero discrepancies. The general identities and bounds are established by
the written proofs, not by that finite calculation. No prose test suite was
created or run.

# Fraisse 1954: original relation construction and modern graph interface

Date: 9 September 2026. Assignment: N-a-002, specifically
`ED26-REQ-N-a-002-01`, with an explicitly proved modern graph interface.
The batch follows the authoring-resumption contract and the CRC-style
logic-and-reasoning reference scope. The research and PDF skills were used
for primary acquisition and reading. No children, manuscript builds, renders,
test suites or independent reviews were created.

## Exact acquired source

Roland Fraisse, *Sur l'extension aux relations de quelques proprietes des
ordres*, Annales scientifiques de l'Ecole Normale Superieure, third series,
71(4) (1954), 363-388, DOI **10.24033/asens.1027**.

- [Numdam bibliographic record](https://www.numdam.org/item/ASENS_1954_3_71_4_363_0/).
- [Complete Numdam PDF](https://www.numdam.org/article/ASENS_1954_3_71_4_363_0.pdf).
- Local artifact: `source/references/fraisse-1954/fraisse-1954-asens-71-363-388.pdf`.
- Size: **3,087,831 bytes**; SHA-256:
  `3277A5E8C80E6B94BF2DCC8C1D82CD769C7477D0574D96C32374B30366DB83F9`.
- **27 physical PDF pages**: one Numdam cover and the complete 26 printed
  article pages. Printed page p is physical page p minus 361, one-based.
- The file starts `%PDF-1.4`; its metadata identifies the author and exact
  title. The 4 November 2024 PDF-production date describes the digitization,
  not a different mathematical publication.

The complete original article was read through the Numdam text extraction,
with the final eight pages also read from the acquired local PDF. Original
scan pages 380-382 and 386-388 were visually checked where the extraction
confused the script letters, overbar, figure labels, order products or final
footnotes. The images in `tmp/pdfs/p03-fraisse-1954/` are source-reading
evidence; none is a render of the manuscript. Both original mathematical
figures were inspected and their relation data redrawn in native TikZ.

The first PowerShell HTTPS request failed authentication, and Windows curl
failed to acquire Schannel credentials. Python's standard verified HTTPS
download succeeded; certificate verification was not disabled. The complete
source cover and copyright notice remain in the retained PDF.

## Written artifacts and extent

- `handbook/parts/p03/presentations/fraisse-1954.tex`
- `handbook/annex/p03/fraisse-1954.tex`
- `handbook/bib/intake-p03-fraisse-1954.bib`
- `handbook/registry/symbols-intake-p03-fraisse-1954.csv`

The chapter and annex have **17 reciprocal result/proof pairs**. They
reconstruct the original six main theorems and the supporting relation,
filter, extension and amalgamation arguments. Proofs are independently
worded in English. The original one-relation, positive finite-arity setting
is distinguished from the subsequent countable-signature theorem.

| Original extent | Supplied treatment |
| --- | --- |
| Sections 1.2-1.4, pp364-365 | Two-valued relation functions; restriction, transport, chains and isomorphism types; two distinct embedding preorders; ages and local classes; original order counterexamples. |
| Sections 1.5 and 2, pp366-369 | Three closure conditions; count of ages by arity; finite/countable chain scheduling; HP/JEP characterization; chain union and intersection of ages. |
| Section 3, pp369-374 | Projection filters; inverse projections, refinement and restriction; normality; finite-map characterization; filter equality and its transport lemma; ultrafilter refinement. |
| Section 4, pp374-377 | Arbitrary-base realization; original joint-host construction allowing cross-side identifications; finite character from chain closure; class characterization and arbitrary-family hosts; countable universality as a separate property. |
| Section 5, pp377-379 | Homogeneity; condition H; one-point equivalence; embeddings of countable structures into arbitrary targets; back-and-forth extending a prescribed finite isomorphism. |
| Section 6, pp379-380 | Order-gap criterion; DLO equivalence for H; rational order; all three stated uncountable homogeneous examples; the real line minus a point as H without homogeneity. |
| Section 7, pp381-382 | Ordinary amalgamation, extension form and literal/strong amalgamation; their implications and separating unary example; finite batches of extension problems. |
| Section 8, pp383-385 | Finite-size schedule; every late extension requirement; exact age of the union; necessity and sufficiency of AP; uniqueness and universality. |
| Section 9, pp385-387 | Arbitrary relations, linear orders and partial orders; full partial-order path/cycle argument; ramified-order AP obstruction; both figures' mathematical data and the homogeneous/universal distinction. |
| Section 10, p388 | Common host for a complete first-order theory, with a supplied elementary-diagram strengthening; the four historical questions and the printed negative-answer footnote, without a claim of present open status. |

The general chain-host lemma makes the choices from a definable class
explicit: Collection and rank bounds confine witnesses to a set before a
single well-order is selected. The Gamma-class proof also retains the
source's projection-filter route, rather than replacing it with a modern
compactness citation. The final logical application explicitly uses the
existing `thm:p02-fol-compactness` and supplies the diagram argument.

## Direct corrections and convention boundaries

**Section 7.3, p382:** The scan explicitly describes a unary relation class
with exactly one positive element and then says it satisfies C1. Restricting
away the positive element refutes heredity. The active reconstruction uses
the hereditary class with **at most one** positive element. It proves
amalgamation in the zero/one-positive cases and preserves the intended
failure of literal amalgamation for two disjoint positive singletons. This
correction is in the mathematics itself; the reader is not asked to repair
the original false assertion.

**Order and base conventions:** The original orders use reflexive relations.
The chapter gives the exact diagonal translation to strict order notation
and proves that induced embeddings and automorphisms agree. Empty bases
are explicitly admitted, with nonempty classes required in the age/class
characterizations. Projection targets are nonempty where extension of
partial maps needs a default value. The empty and singleton order cases
are separated from the rational-order conclusion. Source order products
are stated as explicit indexed sums, avoiding a reversal of Hausdorff's
product convention.

**Finite versus countable signatures:** The original stage p treats finitely
many types of size at most p. That finiteness need not hold in a countable
relational signature. The modern proof instead treats the first finitely
many enumerated types and all their embeddings into the current finite
stage. It proves fairness for an arbitrary extension appearing later in
the union. Nullary relations, if present, have their shared values fixed
by JEP before the empty initial structure is used.

The finite-signature categoricity proof uses finite atomic diagrams and
extension sentences. The failure for countable signatures is proved by
countably many unary colors: adding an uncolored element preserves every
finite-language reduct up to isomorphism but changes the full structure.
This supplies the actual mathematical boundary independently of any claim
that the separate Hodges presentation has been read or completed.

## Graph result and separate source obligations

The graph section is a **modern consequence with its own proof**. It gives
the finite free amalgam, the exact first-order extension-axiom schema,
one-point extension, induced universality, homogeneity, completeness and
countable categoricity. Its semantics is deterministic. This is not
presented as Rado's original universal graph/function construction or as
an empirical statement about random finite graphs.

`ED26-REQ-N-a-002-02` (Rado1964) and `ED26-REQ-N-a-002-03` (Hodges1993)
retain their separate acquisition, source-presentation and correction
obligations. The original Rado article and the complete specified Hodges
sections were not acquired or read in this assignment. N-a-002 as a whole
is therefore not declared complete by this return.

## Author checks and lead integration

I read the actual complete body and annex after writing, and read the later
local corrections in their final context. Mathematical author checks
covered the finite-stage schedule, the normal-filter equality quotient,
the partial-order cycle, the unary hereditary correction, the ramified
amalgamation cases, all three uncountable order examples, the finite-reduct
categoricity counterexample and the graph extension schema. These are
authoring checks, not independent acceptance.

A direct scan of the two assigned LaTeX files found 17 proved result tags,
17 annex items and zero reciprocal mismatches, with no body proof
environment and no undefined hbproof wrapper. The symbol intake has the
ordinary seven-column header and 23 data rows. No software test file was
written or run. Publication layout remains uninspected, as required by the
batch sequence.

The lead owns routing, shared-host edits and canonical intake merging.
The body uses the existing `Fraisse1954` key; its intake enriches that
record with issue, DOI, URL and the exact source manifestation. It must
not create a second canonical entry with the same key. Source symbols
receive explicit local scopes in the separate intake.

The complete host-level Fraisse target is supplied by
`thm:p03-fraisse54-countable-language`; the original single-relation target
is `thm:p03-fraisse54-original-construction`. The graph interface is
`thm:p03-fraisse54-graph`. Existing classification-theory statements may
reference these after routing. Their new annex items already have their
own reciprocal body labels; do not point two body results to one annex
item without a deliberate restructuring. No shared driver, style,
canonical bibliography, canonical symbol registry or existing host text
was changed by this writer.

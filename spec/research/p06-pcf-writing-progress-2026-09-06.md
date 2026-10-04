# PCF foundations added to the cardinal-arithmetic chapter

The active chapter now replaces the obsolete treatment-ceiling paragraph
with an introductory reference section on possible cofinalities.

## Reader content

The section defines the product as a function space, its pointwise order,
cofinal families in a general ordered set, equality and comparison modulo
a proper filter, ultrafilter quotients, possible cofinalities, and
progressiveness.

The elementary lemma proves that an ultrafilter quotient is a linear
order without a greatest element, that its cofinality is infinite regular
and admits an increasing cofinal sequence, and that principal quotients
give the factors. It follows that pcf(a) contains a and equals a for
finite nonempty a.

The exact cited PCF maximum theorem states that for nonempty progressive
sets of infinite regular cardinals, max pcf(a) exists and equals the
cofinality of the pointwise product. The finite product omega × omega_1
illustrates why this is a cofinal-family statement rather than a
pointwise increasing-chain statement.

The subsequent proved corollary derives bounds by sup a and the product
cardinality. Without a largest factor, progressiveness makes sup a
singular and forces the maximum possible cofinality strictly above it.
The sequence of aleph_(n+1) factors gives the concrete aleph_omega bounds
and a conditional equality under GCH at aleph_omega.

The section defines strong limit and states Shelah's cited strict bound
2^(aleph_omega) < aleph_(omega_4), assuming aleph_omega strong limit.
The meaning of the ordinal index omega_4 is explicit.

Silver's equivalent first-failure formulation has been corrected directly
to GCH. The displayed hypothesis does not justify substituting SCH in
that reformulation.

## Sources, proofs, and navigation

The source packet is p06-pcf-foundations-source-note.md, grounded in
Shelah's author-hosted published Cardinal Arithmetic for Skeptics and
Silver's original proceedings paper. The independent elementary
derivation is p06-pcf-elementary-proof-note.md.

The body is handbook/parts/p06/cardinal-arithmetic-supplement.tex.
The new proofs are handbook/annex/p06/pcf-foundations.tex, reached by
the active annex/p06-route.tex driver, at annex:p6.pcf.1 and .2.
The bibliography contains Shelah1992Skeptics with verified metadata
and author URL. The lookup and named-theorem index entries are updated.
The symbol registry and its two generated tables include the new
product, quotient-order, possible-cofinality, and ordinal-index entries.

## Verification

One independent reader checked the actual definitions, examples and both
elementary proofs, including regularity without circularity and the
explicit dependence of the bounds on the maximum theorem.
Another checked the cited theorems against the primary source and the
Silver correction. Both bounded readings found no concrete defect.
The existing symbol-table formatter completed successfully after the
registry update; no software tests or manuscript renders were added.

This is completion of the introductory PCF treatment, not a claim to
reproduce the full research monograph or finish the entire book.

# C6: full P4 computation-verification text freeze

Date: 7 September 2026. Root integration record for independent review.
The work is supplied author text, not independent acceptance or register closure.

## Current targets

| Artifact | Current SHA256 |
| --- | --- |
| handbook/restoration/inherited-07851-08048.tex | DE01687B7F524F49D6B3E90C9ACD038550F7BE1551A1AABC771B8BBB3B4B0177 |
| handbook/restoration/inherited-08710-08876.tex | 4D131A6631A148354F31066316E3B73977DF71AF66C06FC98158D6C402DBC102 |
| handbook/registry/symbols.csv | 54F108553D5B719EB06BC3B85808656D4AF5BF56397ADF4643EB10C57D8B0D79 |
| tmp/edition-2026-c6-candidate/symbols-tables.tex | 79E2C62BAF9D5E566AFA251ABF6A2F3E4BAE2F83C1481F1BCF25821D28328712 |
| tmp/edition-2026-c6-candidate/symbol-index.tex | 03231E48997471D9EF625A7584CB54AD85ED7F5F822338125BF39AA78B0CBCD5 |

The source and author notes are edition-2026-c6-arithmetic-preparation.md,
edition-2026-c6-protocol-and-extraction.md,
edition-2026-c6-input-table-formulas.md and
edition-2026-c6-computation-verification.md, all under spec/research.
They record actual development and source/dependency boundaries, not reviews.

## Supplied scope

The numbering file now defines the exact state/tape/input-alphabet metadata,
five-field row encoding, full row order and length-prefixed tuple. It gives
unique effective decoding and updates the complete enumeration argument's
metadata step. Its separate universal-computation sketch and parameter
theorem remain at their existing status.

The history file now contains bounded E/E2 tagged extraction and its complete
packing proof; an exact fourteen-tag history layout; literal H1/H2 input,
bitmap and program-table formulas with complete correctness/packing proofs;
literal H3/H4 configuration, transition and output formulas with their complete
conditional correctness proof; the explicit Comp conjunction and both
computation directions; a worked identity example and failure cases; and the
complete supplied P4 c.e./Sigma1 and decidable/Delta1 proofs.

The later hierarchy completeness/strictness citations remain outside this
acceptance scope. P5 numeralwise representation, internal syntax/proof
arithmetization and derivability conditions remain separate obligations.
The proof must not use those unprovided internal assertions, or a generic
T-predicate, to establish the particular Comp construction circularly.

## Final root integration after author handoff

The final author history hash was
E391CAA3351C3DC768D2FAC6E00636EA57C7BB189161A6941C25229C0D922D30.
Root changed only the history definition's final blanket sentence about
auxiliary values: it now distinguishes stored data bounded by s, projections
bounded by their row code, paired indices with their separate term bounds,
and derived-length/last-position witnesses with explicit bounds below.
This aligns the summary with the already supplied extraction and computation
proofs. It does not add a quantifier or change a formula. Review the actual
current text and hash above; the author note's line numbers precede this
three-line increase.

Root read the new H1/H2 definitions and input proof, complete H3/H4 definitions,
their conditional proof and complete Comp proof, and checked the active c.e.
definition and prefix-normal-form dependency. A separate numerical
recomputation of the worked identity data gives row codes 1034, 26564 and
582659, tape prefixes 0,2,7,21,63, and bitmap tails 6,3,1,0. This is a
bounded arithmetic check, not a software test suite or independent acceptance.

Seventeen canonical symbol rows were appended, and the existing Comp role
was updated in place to identify the actual explicit conjunction. All old
row numbers survive. The 886-row registry passes the existing generator's
field/scope/exact-glyph checks and has isolated candidate table/index outputs.
No active generated view was promoted. The preceding C5 candidate snapshot
remains preserved as its own review evidence; the C5 row content is unchanged.

## Required independent decisions

Obtain fresh source-fidelity, mathematical/topic and adversarial-publication
reviews. Read actual LaTeX, all necessary local definitions and proofs, and
candidate notation as appropriate. Check the exact program identity, every
quantifier bound and capture condition, paired indices versus stored values,
canonical zero and leading-zero cases, row membership i<m, both head moves,
every tape cell, the finite-window/blank-extension converse, finite packing,
and the bounded evaluator including bottom and empty ranges. Preserve the
four ordinary-theorem hooks in their original order.

Use distinct verdicts for source compatibility, mathematics, publication
text/candidate notation, and the still-open formal/provenance/production gates.
The manuscript is not yet independently accepted merely because its proof
sketch labels have been changed after supplying proof text.

# Original Morley categoricity-in-power package

Unit: ED26-REQ-N-a-006-01. Allocated subcomponents:
N-a-006-MAP-01, N-a-006-MAP-02, N-a-006-MAP-06.
Author return in the client project date 1 October 2026.
This record is not independent source, mathematical or publication admission.

## Exact source and extent

Michael Morley, Categoricity in Power, Transactions of the American
Mathematical Society 114(2), February 1965, pp. 514-538,
DOI 10.1090/S0002-9947-1965-0175782-0.
The selected exact free publisher manifestation is
https://www.ams.org/journals/tran/1965-114-02/S0002-9947-1965-0175782-0/S0002-9947-1965-0175782-0.pdf.
An initial guessed issue path 114-00 returned 404 and supplied no body;
the correct issue path 114-02 returned the retained original scan.

Held PDF: source/references/p03-morley1965/morley1965-categoricity-in-power.pdf.
Size 2,654,463 bytes; twenty-five physical pages; original pagination 514-538.
SHA256: 9AC7D9A40F0BB560B3B7B531A9F723F77D37B15FD326FF3BB314E39D71DA036B.
Layout-preserving extraction: source/references/p03-morley1965/morley1965-extracted.txt.
Extraction SHA256: 4B4D00B16B906B37F2F576F994FA1570C3B57AB405B6046F9C45A74293BF16C8.
The source-receipt JSON retains these observations. No paid acquisition was used.

All twenty-five source pages, including introduction, sections1-5,
footnotes, historical closing questions and references, were read in
the complete extraction. Original source pages 514, 520, 525, 531, 532, 533, 538
were inspected as images for endpoint identity, derivative notation,
ordinal addition, coherent-type limits and the simultaneous-prime construction.
The image files remain in this source directory. No manuscript build,
render, consolidated review or prose-regression test was performed.

The scan's first footnote says that, apart from minor emendations,
the paper agrees with the author's August 1962 Chicago dissertation.
That historical relation does not make the dissertation or the 1963
PNAS announcement the selected 1965 article. The publisher scan's
2010 PDF creation metadata is digitization metadata, not a new edition.

## Actual source-native reconstruction

Body: handbook/parts/p03/presentations/n-a-006-01.tex.
Annex: handbook/annex/p03/n-a-006-01.tex.
Bibliography intake: handbook/bib/intake-p03-morley-categoricity.bib.
Symbol intake: handbook/registry/symbols-intake-p03-morley-categoricity.csv.
The lead retains shared driver and canonical-record ownership.

The body and annex supply the following exact original development:

- Original Lemmas1.1-1.2: Morleyization, elementary maps, chains,
  joint embedding and amalgamation; annex:p3.morley.normalization.
- Original Lemma2.1 and parameter-space maps: simultaneous realization,
  Stone spaces and finite formula support; annex:p3.morley.types.
- Original Definition2.2, Theorem2.3 and Corollary2.4: the global derivative,
  compactness, exact images and finite rank localization;
  annex:p3.morley.derivative.
- Original Theorem2.5: the uniform finite degree and additive law;
  annex:p3.morley.degree.
- Original Lemma2.6 and final Theorem5.7: global stabilization and the
  countable ordinal bound; annex:p3.morley.stabilization.
- Original Theorems2.7-2.8: cardinal type bound and the binary residual-tree
  converse; annex:p3.morley.countability. The allocated omega-stability
  connection is made explicit. The finite-tuple definable-rank bridge is
  a labeled editorial addition, annex:p3.morley.rank-bridge, not a
  misattribution of modern notation to the original paper.
- Original ExamplesI-III: algebraically closed fields, tuple codes,
  and a closed Cantor subset realized by unary predicates;
  annex:p3.morley.field-example, tuple-code-example, unary-example.
- Original Theorems3.1-3.6: Ramsey, ordered indiscernibles, universal
  Skolemization and term hulls; annex:p3.morley.ramsey-em. The source
  cites Ramsey and Hilbert-Bernays; local derivations are supplied here
  without treating their entire works as allocated dependencies.
- Original Theorems3.7-3.8: ordinal-generator thin models and total
  transcendence from uncountable categoricity;
  annex:p3.morley.thin-models.
- Original Theorem3.9: permutation-sensitive relations force continuum
  many types over a countable dense subsystem; annex:p3.morley.no-order.
- Original Lemmas4.1-4.2 and Theorem4.3: witness density, isolated density
  and prime extensions; annex:p3.morley.prime-models.
- Original Lemma4.4: stabilized rank and degree of coherent types and
  isolated lifts at chain limits; annex:p3.morley.chain-types.
- Original Theorem4.5: prime models compatible with a continuous chain,
  including isolation over every later parameter base;
  annex:p3.morley.chain-primes. This hard existence step is a full
  construction, not a cited prime-over-basis substitute.
- Original Theorem4.6: minimal-rank/minimal-degree extraction inside
  the given model and conversion of order indiscernibles to an
  unordered indiscernible set; annex:p3.morley.indiscernible-extraction.
- Original Theorems5.1-5.2: uniqueness by back-and-forth and the
  length-omega1 countable-subsystem-saturation model;
  annex:p3.morley.saturation-existence. The source cites uniqueness;
  its full elementary back-and-forth is supplied locally.
- Original Lemma5.3 and Theorem5.4: countable omission witness and
  transfer to every uncountable size; annex:p3.morley.countable-omission-witness
  and annex:p3.morley.omission-transfer. Both the finite-generator
  and infinite-successor cases are included.
- Original Theorems5.5-5.6: every uncountable model is saturated and
  categoricity transfers; annex:p3.morley.original-categoricity.
- All seven historical closing questions, with the source's Silver
  footnote and proved total-transcendence rank bound distinguished
  from speculative finite-rank conditions, are represented in the body.

The source's bibliographic list supplies historical attribution, not
a separate whole-paper allocation for every cited work. Modern
Baldwin-Lachlan coordinatization remains the disjoint later-source unit.
No Morley 1970, Vaught or Lyndon package was edited.

## Direct mathematical qualifications and corrections

The original field example is characteristic zero. The authorized
fixed-characteristic illustration is explicitly extended to positive
characteristic; there the degree of an algebraic one-type counts
distinct roots, not the polynomial degree of an inseparable polynomial.
The body and proof state this directly.

ExampleII is stated for n>=1. The source preliminaries allow nonnegative
integer n but its displayed alphaT=n+1 fails for the degenerate n=0
coding theory: the infinite base still has rank1 and alphaT=2.
No false zero-coordinate case is retained in the active statement.

The proof of original Lemma4.4(b) spells out the first rank-drop argument
at the limit: equality of the stabilized degree exhausts the same-rank
fiber; a first lower-rank restriction cannot appear at a limit, and
at a successor contradicts the minimum-rank choice. This makes the
source's abbreviated limit-stage exclusion explicit rather than
assuming that every isolated type stays isolated automatically.

Theorems3.8 and5.2 retain their actual cardinal hypotheses: only
aleph1 many different types need be selected in the first argument,
and the latter uses an omega1 chain instead of silently assuming
kappa^aleph0=kappa. The transfer proof fixes the same countable
omission base throughout.

## Author status and remaining work

All original statements, required proofs, examples and historical
closing boundaries in the allocated 1965 article have an authored
source-native destination. The complete original is retained and read.
The body has 21 proved result declarations with 21 reciprocal annex items.
The rank bridge and fixed-positive-characteristic extension are marked
as editorial additions, not source-exact prose.

Independent source-fidelity, topic-specialist and adversarial-publication
review, integration into shared routes and canonical records,
scoped static/build evidence, manuscript visual inspection and admission
remain the lead's later consolidated work. This author does not claim
those gates or overall N-a-006 completion across the other source units.

A bounded search for the exact title with erratum/correction terms and
the Lemma 4.4 error phrase returned no identified separate correction
publication. This is a limited search observation, not proof that no
corrigendum exists. No secondary reading companion was substituted for
the retained original body. The explicit graph-language bridge preserves
the same arbitrary-parameter semantics for original function languages.

## Local notation repair

The original first draft incorrectly declared TeX vertical-bar spellings
as though they printed different universe and cardinality symbols.
Morley's published distinction is instead |A| for a system's universe,
kappa(X) for the cardinality of a set, and kappa(A)=kappa(|A|) for the
power of a system. Section 1 on original p. 515 states these definitions;
the existing original-p. 533 image confirms both roles together in
Theorem 4.6: its cardinal comparison is kappa(A)<kappa(B)=kappa,
whereas its indiscernible set is a subset of |B| minus |A|.
The standing convention, every displayed cardinality use in this
body and annex, and the corresponding symbol intake now preserve
that actual distinction. The bare cardinal variable kappa and the
argument-bearing cardinality operation are explicitly typed as in
the source. No mathematical proof or source scope was changed.
The source theorem numbers below refer to the retained original,
not the independently numbered handbook environments.

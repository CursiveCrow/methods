# P15 159.1--159.2 independence over arbitrary index sets and the complement form (packet w02b-p15-006)

## Provenance

- Packet: `work/waves/w02b/packets/w02b-p15-006.json`, label tag `p15-w02b-p15-006`.
- Gaps addressed (assessment disputes):
  - ED26-P15-CH-independent-random-variables-C001 / C002: the existing
    definitions (`handbook/parts/p15/independent-random-variables.tex`
    lines 27-73) fix the index set as finite or countably infinite.
    Durrett v5 p. 44 defines independence of any infinite collection of
    sigma-fields, random variables or sets through its finite
    subcollections.
  - ED26-P15-CH-finite-probability-C010: Grinstead-Snell Definition 4.2
    (sec. 4.1, p. 141) gives the complement-choice form of mutual
    independence; only the forward direction was on the route.
    The finite-probability unit is owned by packet w02b-p15-001
    (readonly here). The equivalence is written here as a general
    result on independence of events (part of the C001 event-independence
    duty of the Durrett unit); the owner packet can cross-reference it.

## Held sources opened in this session

- `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`
  (author version 5, 11 January 2019). Printed page = PDF page - 8.
  Read printed pp. 43-46: Theorem 2.1.1 (p. 43), Theorem 2.1.2 (p. 44),
  infinite-collection sentence and finite definitions (p. 44),
  Theorem 2.1.3 (statement p. 44, proof pp. 44-45), Example 2.1.4 (p. 45),
  Lemma 2.1.5 (p. 45), Theorem 2.1.7 (p. 46).
- `source/references/grinstead-snell-chance-2006/prob-2006-07-04.pdf`
  (CHANCE version 4 July 2006). Printed page = PDF page - 8.
  Read sec. 4.1: Definition 4.2 (p. 141), the remark that the full
  n-fold product equation does not give mutual independence (p. 141,
  pointing to Exercise 8), Definition 4.4 (p. 142), Exercise 8 (p. 151),
  Exercise 33 (p. 155). Source complement notation: tilde A.

## Continuation

- Session 2 (4 October 2026): re-verified with pdftotext every locator
  in the body: Durrett pp. 43-46 (Theorems 2.1.1-2.1.3, the
  infinite-collection sentence on p. 44, Example 2.1.4 p. 45,
  Theorem 2.1.7 p. 46); Grinstead-Snell pp. 141, 142, 151, 155.
- Fixed the Exercise 8 array (row ends were single backslashes, which
  broke the unit build).
- Added item 7 of thm:p15-w02b-p15-006-arbitrary-transfer (point-mass
  criterion for countably-valued variables over any index set, with
  Grinstead-Snell Definition 4.4, p. 142) and its annex proof (7), which
  reduces to the countable-value clause of thm:p15-independent-product-law.
- Added the p. 141 remark citation in def:p15-w02b-p15-006-complement-examples.
- Unit compile ok; check.py shows no finding in owned files. Three
  overfull boxes come from long annex labels in the unit headings.
- Open for the owner of the finite-probability unit (w02b-p15-001):
  the entry in handbook/parts/p15/finite-probability.tex lines 231-235
  still defines independence of two random variables only; it can
  cross-reference thm:p15-w02b-p15-006-arbitrary-transfer item 7 and
  thm:p15-w02b-p15-006-complement-form.
- Placement: own chapter inserted after
  parts/p15/uniform-integrability-and-conditional-limits (body) and
  annex/p15/uniform-integrability-and-conditional-limits (annex).

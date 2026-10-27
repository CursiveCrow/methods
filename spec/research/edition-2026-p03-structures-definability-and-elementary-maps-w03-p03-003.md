# Research note: P3 24.3 definable sets with parameters (packet w03a-p03-003)

Owned reader files:

- handbook/parts/p03/structures-definability-and-elementary-maps-w03-p03-003.tex (body, chapter level, toc tag P3 24 24.3)
- handbook/annex/p03/structures-definability-and-elementary-maps-w03-p03-003.tex (annex)
- handbook/bib/intake-p03-structures-definability-and-elementary-maps-w03-p03-003.bib
- handbook/registry/symbols-intake-p03-structures-definability-and-elementary-maps-w03-p03-003.csv

## Duty addressed (block 1)

MP-0 writable part of 24.3: the general finite-tuple definable-set and parameter
account: the set phi(M^n, b) defined by a formula with a finite parameter tuple
b from A, A-definable sets and relations, closure under Boolean operations,
projection, permutation and identification of coordinates, invariance under
automorphisms fixing A pointwise, and behaviour under elementary extension.

## Sources read in this session

- Marker, D., "Introduction to Model Theory", in D. Haskell, A. Pillay,
  C. Steinhorn (eds.), Model Theory, Algebra, and Geometry, MSRI Publications
  Volume 39, Cambridge University Press 2000, pp. 15-35.  Open-access copy of
  the published chapter (version of record as distributed by MSRI/SLMath):
  https://library.slmath.org/books/Book39/files/marker.pdf (downloaded
  2026-10-11 to tmp/agent-scratch/w03a-w03a-p03-003-b1-author/dl/, text
  extracted with pdftotext).  Pages read: 15-18 (section 1: Definition 1.1,
  Proposition 1.2, definition of definable and A-definable sets on p. 17,
  Proposition 1.3 on p. 18), 27-30 (types, Proposition 5.1 on p. 28 and its
  footnote on A-definable sets, Definition 6.1 and Lemma 6.2 on pp. 29-30).
  Locators used in the reader text: Definition (definable sets) p. 17;
  Proposition 1.2 p. 17; Proposition 1.3 p. 18; Proposition 5.1 p. 28;
  Lemma 6.2 p. 30.  Marker states Proposition 1.3 without proof and only for
  arbitrary parameters; the A-relative version and all proofs are written in
  the annex.  Marker's list in Proposition 1.3 has no clause for constants;
  the reader text records why this makes no difference when A = M.

Internal on-route dependencies (labels verified present): lem:fol-coincidence,
thm:fol-substitution, lem:substitution-fv, lem:iso-invariance,
lem:term-preservation, def:parameter-expansion, thm:tarski-vaught,
sec:maps-elementarity-02, sec:maps-elementarity-03, sec:fol-syntax-semantics-01
(countable variable set), def:p03-elementary-class,
def:p03-implicit-explicit-definability, def:p03-vaught-relative-interpretation,
def:p03-morley-definable-rank, def:p03-imaginaries-real-codes.

## Existing treatments found (A9)

Listed in the packet: preservation-abstract-logic.tex (elementary class,
Beth), n-a-003-01.tex (Vaught interpretation), restoration 06138-06242
(substructures, isomorphism invariance, image of an embedding).
Found in addition and linked rather than duplicated:
n-a-006-01.tex def:p03-morley-definable-rank (uses definable sets with
arbitrary parameters without defining them), classification-theory.tex
(strongly minimal sets, acl), imaginaries-and-quotient-interpretations.tex
(dcl^eq, automorphisms fixing a parameter set).  None gives the general
finite-tuple account.

## Readonly units

All units in the packet (FLRV1 U00416-U00422 and the Hodges 1993 SRC-048
units) are owned by w03-p03-001 (readonly_units); not written here.

## Continuation

Block 1 written: body and annex for the definable-set account (normal form,
closure, least closed family, isomorphism transport and automorphism
invariance, rigid example of invariant non-definable set, elementary
extension transfer, substructure failure, worked example on (Q,<)).

Session of 2026-10-12 (same block, resumed after an assessment that found the
account absent from the route): the two owned reader files were not yet
\input by the drivers and no return file existed, so the assessment, which
reads only on-route text, could not see them.  In this session: re-opened the
Marker PDF (tmp/agent-scratch/w03a-w03a-p03-003-b1-author/dl/marker-msri39.pdf)
and re-verified every locator used (Definition p. 17, Proposition 1.2 p. 17,
Proposition 1.3 p. 18, Definition 1.1 pp. 15-16 for the separate constants,
Proposition 5.1 p. 28, Lemma 6.2 p. 30); re-checked every internal label and
the claims made about lem:iso-invariance, sec:maps-elementarity-03,
def:parameter-expansion, thm:fol-substitution, lem:substitution-fv, the
eleven reserved tokens of sec:fol-syntax-semantics-01 (used in the coding
argument: eleven tokens plus < make the twelve non-variable symbols),
def:p03-implicit-explicit-definability, def:p03-morley-definable-rank and
def:p03-imaginaries-real-codes; unit-compile ok; check.py shows only the
intake bib-key finding; find_fused_spaces clean.  Wrote the return file with
the placement from the packet's insertion proposal.  Route insertion of the
body and annex inputs is a driver change executed by the lead.

Remaining for MP-0 (writable part): none identified in the text; the account
reaches the route only after the lead inserts the two inputs.
Hodges 1993 definable-class components belong to w03-p03-001 (readonly).

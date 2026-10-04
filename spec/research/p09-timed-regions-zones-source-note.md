# Timed automata, regions and zones: bounded construction packet

Author-owned packet, 2 October 2026. Supplies the construction scope of planned
137.2; no fulfillment ledger, canonical, routing or admission state is changed.
Root owns reader insertion and later independent gates.

## Exact allocation and finite dependency boundary

Read ED26-SRC-057-0029 (published 2018 chapter29, pp.1001--1046),
ED26-SRC-057-0109 (separate MPI-linked manifestation), and distinct
ED26-SRC-058-0010/0103 timed process-algebra allocations. Whole source variants
remain separate. No Alur--Dill unit was directly allocated in the current queue:
its original paper is a finite foundational dependency of this construction,
not a substitute handbook chapter or a recursively allocated whole source.

Frozen claims: clock/guard/reset/invariant semantics; rational scaling;
bounded-cell partition/count; guard/reset stability; continuous event-time
retiming with all intermediate invariant tests; quotient projection/lifting
and effectiveness; diagonal truth-bit refinement; strict DBM consistency,
closure and inclusion; exact projection/reset/time-up/intersection/posts;
finite region-union normalization. Nine named body results have nine reciprocal
full proofs. No PSPACE lower bound, infinite acceptance, TCTL, practical LU
extrapolation, weighted/game/parametric/distributed or hybrid theorem is a hidden
proof premise. Other chapter/source obligations remain open.

## Exact acquired sources and actual selected reading

Alur and Dill, *A Theory of Timed Automata*, Theoretical Computer Science126
(1994), printed183--235, is acquired as its author-hosted published53-page scan,
not preliminary1990/1991 versions named on its first page.
URL: <https://www.cis.upenn.edu/~alur/TCS94.pdf>.

- File: `source/references/p09-timed-regions-zones/alur-dill-1994.pdf`.
- Bytes:3,271,956.
- SHA256:`bf12d937c5ca07d579d7ed976a1c9515cc6edc03c17527507cb7ac440a009d0d`.
- Lowercase Tcs94 returned404; uppercase exact author URL succeeded with TLS
  verification. No account, payment or security barrier was crossed.
- Read title/contents, sections3.1--3.4 (printed190--195/PDF8--13), integer
  scaling and region/region-automaton4.1--4.3 (printed200--207/PDF18--25).
  Beginning4.4 through printed209 was additionally inspected for the separate
  progressive infinite-run boundary. Read diagonal-extension paragraphs5.5
  on printed216/PDF34; later clock-addition undecidability is not imported.
  No whole-paper reading claim. Printed202 with Definition4.3/Fig.9 was viewed
  visually. The reader reconstructs the source's28-region count and the
  Examples3.5/3.9 asynchronous-reset trace, not a fabricated empirical outcome.

Bouyer, Fahrenberg, Larsen, Markey, Ouaknine and Worrell, *Model Checking
Real-Time Systems*, Chapter29 of *Handbook of Model Checking*, is acquired
from the exact allocated author URL:
<https://people.mpi-sws.org/~joel/publications/handbook-model-checking-real-time-systems18.pdf>.
The file itself has2018 Springer copyright, DOI
`10.1007/978-3-319-10575-8_29`, and the complete printed1001--1046 sequence.
The author's record separately identifies2018 and46pages:
<https://people.mpi-sws.org/~joel/publications/handbook-model-checking-real-time-systems18abs.html>.
Thus actual printed version fields, not title identity alone, qualify the linked
manifestation; whole-source authoring/admission is not claimed.

- File: `source/references/p09-timed-regions-zones/mpi-realtime-author-2018.pdf`.
- Bytes:1,324,049;46physical pages.
- SHA256:`dffbe1ac433f673bd6d432b22347dc2e36d70e0698cd13cf74f0a8857aad6f0a`.
- Selected reading: introduction;29.2 clock/invariant/step/run definitions and
  notes1003--1005, textual product context1006;29.3.1 region/finite reachability
  text1007--1008 with extension context1009; complete selected zone/DBM/
  normalization-boundary exposition29.7.1--29.7.3 on1023--1027. Printed1007 and
 1025 were visually inspected. Other technical sections were not read fully.
  Bibliographic endpoints and some records were inspected, not the whole
  bibliography claimed read.

Two ordinary public verified-TLS downloads; no login, purchase, contact,
CAPTCHA, TLS/security bypass or paid access. The three source-page PNGs are
reading evidence, not manuscript renders or reader assets. Source PDFs remain
unchanged.

## Complete printed region clauses and all-clause countercase

Visually checked original printed202, Definition4.3, defines v~v' by all these
clauses in the following order (variables/conditions retained):

1. For every x, floors of v(x),v'(x) are equal, or both values exceed c_x.
2. For x,y with v(x)<=c_x and v(y)<=c_y,
   `fract(v(x))<=fract(v(y))` iff `fract(v'(x))<=fract(v'(y))`.
3. For x with v(x)<=c_x, `fract(v(x))=0` iff `fract(v'(x))=0`.

Printed2018 page1007 has that first clause, then the zero-fraction clause as
its second bullet and the pair-order clause as its third, with M_x for c_x.
These are all clauses, not a criticism based solely on floors.

For one clock, c_x=M_x=1, v(x)=1.1, v'(x)=1: clause1 holds, both floors1;
clauses2/3 are vacuous in that direction because v(x)>1, including the
self-pair x=y antecedent. In reverse, clause1 still holds, the self-pair
order is true, but the zero-fraction iff fails:0 versus0.1. The complete
printed ordered-pair formula is therefore asymmetric. It also fails to
preserve x<=1, false at v and true at v'. No other printed clause supplies
the missing over-limit bit.

The following original cell representation separates integer points, open
bands and the over-limit cell. The reader uses that intended partition with
explicit matching boundedness bits, floor/zero flags and fractional weak
ordering, and supplies its full counting/quotient proof independently. It is
not silently attributed as the unchanged printed three-clause definition.
Correction provenance remains here outside exposition; archived originals
are unchanged. Images: `ad-region-page-20.png`, `mpi-region-page-07.png`.

## Empty successors and nonnegative clock domain

The source permits empty zones and its displayed symbolic transition
definition retains them. Its location-reachability proposition on printed1024
needs a nonempty successor for the intended converse: guard x<0 produces a
symbolic `(target,empty)` but no concrete target state. The new search discards
empty zones, and every operation propagates an empty marker; this is proved.

Fig.12 on1025 includes x1<=3 and x1-x2>=4. With x2>=0, they force
4<=x1<=3, so their clock zone is empty. The illustration without implicit
nonnegativity rows remains a meaningful real-coordinate difference system.
The reader distinguishes those domains and inserts clock nonnegativity in
every DBM. It does not credit the graph as a nonempty clock zone.
Image: `mpi-dbm-page-25.png`.

Entryij bounds vi-vj. The feasibility graph uses edgej->i, transposing the
source illustration's arrows but preserving inequality meaning. Strict flags
are retained. The annex constructs rational feasible potentials by a small
strict-edge epsilon, proves exact projection/reset/delay, and proves inclusion
necessity by a negated bound. No cited shortest-path black box replaces them.

## Delivery and residuals

The reader supplies the source reset trace/28-region count, exact DBM
calculation, and diagonal-saturation, convex-hull, infinite-zone and Zeno
failures. Finite reachability is not infinite progressing acceptance. The
proved finite normalization uses region unions, not a single DBM or an
unproved practical extrapolation. Current CSL timing at
`sec:p09-csl-endpoints` was read and remains a distinct probabilistic interface.

This does not finish whole ED26-SRC-057-0029/0109 chapters, timed
Baeten--Middelburg variants, hybrid/parametric/distributed models, weighted
automata/games, full temporal-language methods or practical LU proof sources.
No canonical/tracker/baseline or driver was changed. Body/nine-pair annex,
unique intakes, qualified PDFs/reading images and this note are the owned
deliverables. Root owns routing and subsequent independent gates.

No child, independent review, prose-test, build, manuscript render, source/proof
admission or publication acceptance was performed.

## Author-side adoption clarification

The current P9 overview was inspected for a directly superseded missing-regions
or timed-automata survey pointer; no such pointer was present. Its existing
timed paths belong to CTMC/CSL residence-time semantics, so it was left unchanged
under the narrow editing authority. Root owns the new body and annex inputs.

The inspected P9 driver currently places `presentations/n-c-023-01` after the
main overview; its actual heading is a Gelfond--Lifschitz1988 stable-set and
autoepistemic subsection. That existing non-timed subsection should remain
before the new timed chapter heading when root inserts the chapter. The
author did not edit that source presentation or either shared driver.

Two local notational clarifications preserve all nine theorem hypotheses and
conclusions. The cell family is indexed explicitly, so M_x=0 has exactly the
zero point and over-limit positive interval. In the DBM time-up converse,
coordinate0 is fixed at zero; subtraction of the common delay applies only
to actual clocks i>0, and unchanged difference equations are explicitly
restricted to i,j>0. Bounds involving coordinate0 are handled by the proved
delay interval requirements, not by a false shift of the zero coordinate.
Source-region correction provenance remains outside the reader and the
original source PDFs remain unchanged. No practical extrapolation,
infinite-language or whole-chapter result is added by these clarifications.
The symbol intake now records the region descriptor's semantic data only;
the printed-formula correction details stay in this provenance note rather
than in prospective reader-facing symbol-table notes.

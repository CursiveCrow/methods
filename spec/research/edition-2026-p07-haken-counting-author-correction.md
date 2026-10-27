# P7 Haken lower bound: complete editorial counting proof

Date: 26 October 2026. Standing: author completion and correction, not
independent admission or original-source acquisition.

## Completed result

The active theorem thm:p07-haken-resolution-lower-bound now has a complete
proof in annex:p7.complexity.1. Its statement is unchanged: for some
constant c>1 and all sufficiently large n, every general resolution DAG
refuting the nonfunctional n+1-pigeon/n-hole CNF has at least c^n clause
occurrences. The proof obtains the explicit bound
L >= (16/15)^floor(n/4), n>=4, and hence c=(16/15)^(1/8) works for n>=8.
The theorem's status changed from sketched to proved only because
the full local proof was supplied.

Applied manuscript files:

- handbook/parts/p07/proof-complexity.tex
- handbook/annex/p07/proof-complexity.tex

The body preserves the theorem statement and historical attribution.
It updates the proof status and the chapter's own navigation. The annex
replaces the unspecified imported bottleneck estimate with the complete
argument described below. Before/after hashes and original bytes are
retained in task/p03-finite/haken/manifest.json and its before/ folder.
Three other navigation corrections are staged for the central owner;
generated indexes are not edited by this author.

## What was actually missing

The previous annex counted full critical assignments and asserted, without
specifying a predicate or proving it, a route barrier with exponentially
small fibers. It attributed that load-bearing lemma to Haken and the
Beame--Pitassi survey. The existing n-c-027-02 body and annex prove five
valid elementary helpers: critical routing, matching restrictions,
restriction of resolution without weakening, a conditional charging
inequality, and the six routes in a small derivation. They explicitly do
not establish the exponential barrier/capacity estimate.

The new proof counts partial matchings instead. This is a substantive
correction to the old argument, not a declaration that its unsupported
full-critical-assignment capacity assertion has now been verified.

## Complete proof components

1. In the exact registered literal-set resolution rule, a falsified
   resolvent selects a falsified parent. Along that route a specified
   pigeon's positive-literal count increases by at most one when moving
   to the parent. No monotonicity in the other direction is used.
   Tautological clauses cannot be selected.
2. Put k=floor(n/4). Every k-edge partial matching extends to a critical
   assignment. Its route reaches a clause with exactly 2k positive
   literals in the unmatched row. Choose the earliest eligible occurrence
   for each partial matching in one topological order of the original DAG.
3. Earliest occurrence implies that any compatible critical assignment
   falsifying that occurrence has at least 2k positive literals in its
   unmatched row. Otherwise its route supplies an earlier eligible node.
4. The matching-swap argument gives at least k+1 constrained pigeon rows.
   Each has a negative literal or at least 2k positives. The two changing
   truth values and compatibility with the matching are checked explicitly.
5. For a fixed occurrence, choose its constrained rows independently of
   the partial matchings subsequently counted there. A selected constrained
   pigeon has at most n-2k possible holes. Count all domain choices and
   injective remaining images, with explicitly identified surplus choices.
6. The resulting total and fiber bound yield H<=LG. An elementary
   symmetric-mean inequality, proved by largest/smallest averaging and a
   variance argument, bounds G/H by (15/16)^k. No unproved independence
   assumption or imported analytic lemma is required.

These steps use occurrences in the original DAG. There is no inference
from a tree lower bound to a DAG lower bound, no alteration of the CNF,
no added functionality clauses, and no added weakening rule. The result
does not assert lower bounds for Frege or extension systems.

## Sources inspected and boundaries preserved

Repository evidence read in this block:

- The exact active theorem/sketch and both elementary-helper files.
- handbook/registry/calculi/resolution-cpl.tex, including its permission
  for tautological resolvents.
- spec/research/p07-haken-source-note.md and the 2 October acquisition
  note under source/references/original-source-new-routes/baldwin-lachlan-ryll-haken-2026-10-02/.
- The held Beame--Pitassi ECCC TR98-067 PDF:
  source/references/acq-r1-ACQ-2026-10-0035/beame-pitassi-1998-propositional-proof-complexity-eccc-TR98-067.pdf,
  SHA256 730a316863ac4a410e92fd02edbbe26dcfdcb5f9c9fdea0238017c88242df40e.
  Its garbled text layer was not trusted. Rendered pages 1 and 5--10
  were read, especially printed p.9, section 3.1. That page explains
  bottleneck counting at a high level; it does not give the full
  numerical PHP counting proof asserted by the old annex.
  The [official ECCC record](https://eccc.weizmann.ac.il/report/1998/067/)
  identifies this as an updated version of the Bulletin article.
  It is not credited as the exact BEATCS 65, 66--89 version.
- The already held six-page Pranjal Singh reading-group lecture, dated
  27 June 2022:
  source/references/original-source-new-routes/baldwin-lachlan-ryll-haken-2026-10-02/iit-kanpur-2022-summary-not-haken1985.pdf,
  SHA256 f2f4d9a07e3a9e04ef86c97c1389ddaedefd9de1ba576e4053132c6de6f81ee8.
  All six pages were read as a later exposition, not the 1985 paper.
  Its half-row/partial-matching construction was a useful proof lead.
  Its unresolved routing comments, tree-oriented ordering and compressed
  estimates were not imported as established lemmas. The manuscript
  supplies the DAG ordering, every swap case, the fiber count, and
  a separate proved estimate in its own CNF orientation.

No full Haken1985 article was acquired or read. The original twelve
printed pages 297--308, source-native presentation and constants, and
original-source allocation remain outstanding. The held publisher XML
remains metadata only. No old publisher CAPTCHA, 401/403 or restricted
route was retried; there was no new access or approval denial. No source
or admission ledger was upgraded.

## Verification and limits

- An actual 248-node literal-set resolution DAG refuting PHP with five
  pigeons and four holes was generated and every inference checked.
  All 120 critical assignments and all 20 one-edge partial matchings
  were enumerated. The earliest-occurrence property, constrained rows
  and 30 swap cases passed; the maximum fiber was 6, below the bound 16.
- The exact rational factorial/averaging inequalities passed for every
  hole parameter 4--100. These finite computations are regression
  evidence, not the all-n proof.
- Staged and applied pdflatex/biber/pdflatex/pdflatex passes all returned
  zero. The 26-page isolated chapter/helper/annex unit has no TeX errors.
  Eleven overfull warnings remain outside the new proof. Ten external
  references are expected because the unit omits the rest of the book.
- The rendered new proof pages 16--19 were inspected after removing two
  overflowing new lines. The final proof has no overfull line.
- A 13-row notation intake is restricted to the literal annex:p7.complexity.1
  anchor. Combined-registry validation found no collisions, no own-file
  notation warnings and no first-use warnings. Canonical integration
  remains with the central owner.

Evidence is under task/p03-finite/haken/: manifest.json, finite-checks.json,
build-applied/report.json, verification.json, notation-verification.json,
and the staged navigation manifest/patch.
This is author verification, not an independent acceptance decision.

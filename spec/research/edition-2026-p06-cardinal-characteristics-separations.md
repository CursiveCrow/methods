# P6 cardinal characteristics: relational witnesses and Cohen separations

2026-10-03. Continuation of the earlier cardinal-characteristics packet.
Status: authored and self-read, not independently reviewed or admitted.
Root owns input routes, canonical records and fulfillment decisions. This
worker does not change the 19-part / 289-chapter / 2,475-section / 615-original-
requirement scope. No review, test, build or manuscript render was run.

## Current artifacts and preserved earlier work

The earlier reader and annex remain unchanged:

- `handbook/parts/p06/cardinal-characteristics-and-inequalities.tex`, 272
  lines, SHA-256 `ebdcefe9dc7bb4cdd13d51639f2417779db7480b95ac27bd459a23a7164296f2`.
- `handbook/annex/p06/cardinal-characteristics-and-inequalities.tex`, 454
  lines, SHA-256 `adba074244ae3dc5cbf6d488911077872e4c17e7be7ef6a526e09bd2c48966ec`.

The current driver actually includes that reader at `parts/p06.tex:152`
and its annex at `annex/p06-route.tex:25`. The earlier raw intake,
bibliography intake, research note and source captures are untouched.
The earlier body was read, along with the connected category, interval,
translation and localization proof passages needed here; no new independent
verification of that earlier packet is claimed.

New frozen authoring files:

| Artifact | Lines | SHA-256 |
|---|---:|---|
| `handbook/parts/p06/cardinal-characteristics-and-separations.tex` | 339 | `3c9256802317782fbf239aefded7e334e22eaa58bf0d9ffec7d5160703b4d1fa` |
| `handbook/annex/p06/cardinal-characteristics-and-separations.tex` | 571 | `308217781eeaae6f98c6c68e9e48cc7231ac09ffa8a6f2d268e208f6246f259d` |
| `handbook/registry/symbols-intake-p06-cardinal-characteristics-separations.csv` | 35 | `cfa2edea65a844cae7d195bc2e1f55fa5a4f4a4dd016f18fc33b89b8d6bba2ec` |
| `handbook/bib/intake-p06-cardinal-characteristics-separations.bib` | 8 | `d4a4da3f889eb4e6f323f18e503960f6d06528ec800faf5a9e0ae958f7472975` |

The symbol intake has **34 raw records**, several explicitly grouped
families. This is not a count of atomic symbols and not a canonical-merge
receipt. There is one new bibliography key, `BlassCombinatorialAuthor2003`.
The already canonical `BlassReductions1994V1` and
`BartoszynskiInvariants1999V1` are reused without a duplicate intake entry.

Suggested insertion seam: new body immediately after the existing
`cardinal-characteristics-and-inequalities` input, and new annex after its
matching predecessor. The new body is a section, not an extra planned
chapter. No route has been inserted by this worker.

## Primary sources and actual extent read

1. [Blass, Reductions Between Cardinal Characteristics of the Continuum,
   exact arXiv math/9407203v1](https://arxiv.org/pdf/math/9407203v1),
   12 July 1994. Frozen PDF SHA-256
   `28f14b4437ad19da4d32cecdbcac98a4744fe026fdadbf7af17308524e9fb643`.
   Read Sections 1--4, printed pp. 1--11, including the relational norm,
   source arrow direction, dual morphism, Section 2 Cohen splitting/
   domination example, chopped-real category basis and engulfing criterion,
   sequential composition and Proposition 2. Section 5's opening statement
   was exposed only while locating the preceding boundary. No Section 5
   proof or Section 6 treatment is claimed read or supplied.
   Direct source-pixel reading of pp. 3, 4 and 10 confirmed the bold triple
   glyphs versus italic predicates, subscripted components and sequential
   formula; the earlier extraction alone did not distinguish all fonts.
2. [Blass's author-hosted Combinatorial Cardinal Characteristics draft](https://sites.lsa.umich.edu/ablass/wp-content/uploads/sites/1471/2025/10/hbk.pdf),
   frozen 104-page body SHA-256
   `1e9d4e76fe8b7289f728c2b2db4dcd2021cf10b00e2faa5014e752049ec0c0b5`.
   The earlier capture filename says undated, but this continuation directly
   read title-page pixels and establishes **November 24, 2003** as the
   actual displayed draft date. Printed/PDF pp. 1--4 were read directly;
   p. 3 discusses continuum-space and measure equivalences. The corrupt
   text extraction remains unused as a reading receipt. The other 100 pages
   are not read or credited in this block. The actual author paper-list
   link was checked; its 2025 upload path does not date the mathematical
   text. No frozen original file or prior note is rewritten.
3. [Bartoszynski, Invariants of Measure and Category,
   exact arXiv math/9910015v1](https://arxiv.org/pdf/math/9910015v1),
   4 October 1999, frozen PDF SHA-256
   `0908b2e096e5ec05834e2c5b9aef9da72031660db38bbe793de229eb2f2ee8a4`.
   Read Section 2's ideal and relational definitions on printed pp. 2--3,
   and Section 6 from its beginning on p. 37 through pp. 38--40 and the
   initial paragraph on p. 41. That source explicitly cites external
   preservation proofs for its Laver/EE/random iterations. They are not
   promoted to complete proofs here or credited from the different Cohen
   preservation argument. The rest of p. 41 and later sections are unread
   in this continuation.

Source-page images and their reading record are confined to
`source/references/p06-cardinal-characteristics-continuation/`.
They are renderings of authority documents, not of the manuscript.
The research skill governed primary retrieval and this separate note;
the PDF skill was used only to read source pixels with corrupt text
encoding and to verify source-native typography. No children were created,
as this bounded worker assignment explicitly prohibits children.

## Thirteen reciprocal authored result/proof pairs

These are construction evidence, not independent proof admission. All
body locators below refer to the new reader file; all annex locators
refer to its new matching annex.

| Body anchor and line | Reciprocal annex anchor and line | Supplied derivation |
|---|---|---|
| `thm:p06-cc-morphism-duality`, 62 | `annex:p06.ccsep.morphism-duality`, 4 | Answer-family transfer, contrapositive dual morphism, interval splitter and its reaping dual |
| `thm:p06-cc-sequential-norm`, 94 | `annex:p06.ccsep.sequential-norm`, 35 | Full product lower/upper bounds and both dual-minimum bounds, including finite norms |
| `thm:p06-ccsep-domain-bridge`, 124 | `annex:p06.ccsep.domain-bridge`, 77 | Binary image/preimage null preservation; all four minima; small-complement and category homeomorphism arguments |
| `thm:p06-ccsep-splitting-category`, 134 | `annex:p06.ccsep.splitting-category`, 160 | Closed nowhere dense nonsplitter sets, nonmeager splitting family and covering lower bound for reaping |
| `thm:p06-ccsep-chopped-base`, 161 | `annex:p06.ccsep.chopped-base`, 182 | Common appended block for every finite prefix; dense matching G-delta basis |
| `thm:p06-ccsep-engulfing`, 168 | `annex:p06.ccsep.engulfing`, 210 | Both containment directions; thinned bad blocks and a real matching only the first datum |
| `thm:p06-ccsep-category-norms`, 192 | `annex:p06.ccsep.category-norms`, 236 | All four category norms and the required datum standing conditions |
| `thm:p06-ccsep-category-sequential`, 201 | `annex:p06.ccsep.category-sequential`, 272 | Answer-dependent beta, reconstructed partition, morphism implication and uncurried Borel coding |
| `thm:p06-ccsep-support`, 242 | `annex:p06.ccsep.support`, 330 | Delta-system ccc proof, nice-name countable supports, extension-family support unions, product genericity and continuum count |
| `thm:p06-ccsep-category-preservation`, 254 | `annex:p06.ccsep.category-preservation`, 394 | Tailored ground dense-open sets for every condition and named closed piece; absolute code transfer to the full Cohen product |
| `thm:p06-ccsep-fresh-obstructions`, 264 | `annex:p06.ccsep.fresh-obstructions`, 442 | Three independent dense-requirement arguments for category covering, domination and reaping |
| `thm:p06-ccsep-null-values`, 292 | `annex:p06.ccsep.null-values`, 488 | Summable block-match null sets covering every smaller-model real; uniformity lower bound and an omega-one coordinate cover |
| `thm:p06-ccsep-cohen-values`, 304 | `annex:p06.ccsep.cohen-values`, 524 | All ten classical and s/r values from these proofs and the existing absolute bounds; explicit GCH cardinal calculation |

The source's `beta` search chooses the first matching block strictly
after the block containing the argument, and has the stated zero branch
when matching fails. The chosen endpoint recursion is an explicit
permitted partition choice satisfying the source inequality; Borelness
is proved for the uncurried function, not invented for the whole function
space. Source bold triples and italic relations remain separate typed
symbols. The converse matching superscript is retained.

The forcing computation is separately attributed as an expanded modern
derivation of the source's Cohen example, not a literal source proof or
the entirety of either Handbook chapter. It assumes a supplied transitive
CH ground with regular `kappa > aleph_1` and `kappa^aleph_0 = kappa`, plus
an actual supplied generic. It never obtains that ground/generic merely
from `Con(ZFC)`. The standard forcing/cardinal-preservation foundations
are the manuscript's current `def:p06-ftr-ground`, recursive forcing
results and `thm:p06-ccc-preservation`. Ordinary product measure and
Lebesgue outer measure inputs remain background; this packet is not an
entire reconstruction of measure theory.

## Proposed 78.1--78.4 coverage disposition

Earlier bare-absence findings do not describe the current reader. The
following evidence supports a **partial substantive** treatment, not a
whole-source/whole-section completion promotion:

- **78.1 Combinatorial cardinal characteristics.** Existing
  `def:p06-cc-bdsr`, `thm:p06-cc-combinatorial` and their annex provide
  b/d/s/r definitions and real witness constructions. New definitions at
  reader lines 20, 43, 74 and 177, with the pairs at 62, 94, 192 and
  201, provide norms, duality, typed source directions and the Borel
  sequential-composition method. The rest of the 2003 draft and the exact
  published Blass chapter remain open, including pseudo-intersection/tower,
  almost-disjoint, ultrafilter and other source-specific invariants and
  their inequalities/separations.
- **78.2 Invariants of measure and category.** The existing ideal square,
  full classical network, localization/translation proofs and category
  identities remain. New bridge at 124, chopped-real constructions at
  147--214 and null-value pair at 292 supply distinct domains and a
  definite model computation. The full Bartoszynski original chapter,
  its parameter-uniform Borel master-set presentations, later small-set
  classes and every required variant are not discharged by this packet.
- **78.3 Inequalities and consistency separations.** The existing body
  already has actual absolute inequality proofs; new exact Cohen values
  at 304 with full reciprocal proof at annex 524 supply strict s/d,
  b/r, cross-ideal covering and uniformity separations in the stated
  extension. No exhaustive classification of consistent assignments,
  ten-distinct-value construction, or other missing characteristic
  comparisons is claimed. The separate syntactic relative-consistency
  metatheorem is not substituted for the explicitly stated semantic
  ground-and-generic hypotheses.
- **78.4 Forcing constructions for values.** New standing at 219,
  support/counting at 242, preservation at 254, obstructions at 264,
  and null calculation at 292 give one full family of Cohen constructions
  and compute the invariant values, rather than merely continuum size.
  Random, Hechler, amoeba, Sacks, Laver, Miller, creature and other
  required iterations/preservation presentations remain separate work;
  the cited source lemmas for those constructions are not upgraded.

The exact original allocations `ED26-SRC-002-007` (Blass pp. 395--489,
DOI 10.1007/978-1-4020-5764-9_7) and `ED26-SRC-002-008`
(Bartoszynski pp. 491--555, DOI 10.1007/978-1-4020-5764-9_8)
remain unclosed. Neither the 1994 separate paper, the 1999 prepublication
version, the 2003 dated draft nor Fremlin's dated section is a title-only
replacement credit for either published chapter. The original source
identities, publication manifestations and queue duties remain intact.

## Handover boundaries

Root must connect the new reader and annex after the prior packet, merge
the one new bibliography entry and reconcile the raw notation families.
In particular Cantor `cal N` has an explicit different set domain from
the earlier real-line ideal; the bridge proves equality of characteristic
values, not extensional identity of those ideals. The final value theorem
explicitly returns to the real-line domain. Existing symbols for global
structures, projection maps, partitions and predicates must not be
silently renamed or merged across incompatible roles.

No canonical file, scope table, coverage ledger, source admission receipt,
historical manifest, frozen packet, shared style or input driver was edited.
No independent review verdict, compilation success, manuscript render or
publication readiness is asserted. The work is saved for integration and
the later consolidated review of the completed change set.

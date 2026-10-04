# SRC-057–062: finite treatments and historical-record roles

Date: 9 September 2026. This assignment constructs the coverage map for the
handbook of logic and reasoning. It does not author or accept manuscript text.
The governing edition contract and the source-template dispositions were read
before mapping. Source identities, exact historical records and failure evidence
are preserved; missing source bodies and writing remain concrete work.

## Source set and intellectual obligations

The six preserved source extracts identify 108 published chapters:

| Source | Exact selected publication | Chapters |
| --- | --- | ---: |
| SRC-057 | *Handbook of Model Checking*, Springer first edition, 2018 | 32 |
| SRC-058 | *Handbook of Process Algebra*, Elsevier first edition, 2001 | 19 |
| SRC-059 | *Handbook of Theoretical Computer Science*, Volume B, *Formal Models and Semantics*, first edition, 1990 | 19 |
| SRC-060 | *Handbook of the Logic of Argument and Inference: The Turn Towards the Practical*, 2002 | 11 |
| SRC-061 | *Handbook of Quantum Logic and Quantum Structures: Quantum Structures*, 2007 | 16 |
| SRC-062 | *Logic: A History of its Central Concepts*, *Handbook of the History of Logic* 11, 2012 | 11 |

Their chapter identity and extent records come from the retained official
publisher presentations in each source's `tmp/acquisition/srcNNN/` directory.
Each complete selected chapter receives a stable source-specific unit, concrete
components, named prerequisite interfaces, a proposed body and annex path,
lookup requirements and explicit success/failure conditions. The component
selection file is
`tmp/edition-2026-catalog-src038/tail-039-068/SRC-057-062-method-profiles.tsv`.
SRC-062 also has a component for each actual captured chapter subsection.

The published treatments cover verification models, temporal and modal
specifications, SAT/SMT, abstraction, compositionality, process equivalence,
concurrency, timing, automata and language theory, program semantics, practical
and dialogical reasoning, probability logic, quantum structures and the history
of central logical concepts. Their source-specific treatments remain owed even
when a generic topic already appears elsewhere in the manuscript. Root will bind
actual overlaps; this assignment claims no existing proof is complete merely
because its subject matches a chapter title.

## Versions, corrections and identity decisions

SRC-057 keeps the 2018 publisher chapters separate from nine named author or
institutional manuscript presentations. The 2014 Berkeley *Modeling for
Verification* record is not relabeled 2018. Bryant's longer BDD title and its
191–218 author span remain separate from the publisher's 191–217 span. The exact
Beyer–Gulwani–Schmidt errata URL is an additional correction obligation attached
to chapter 16 and its author PDF. Its body is still unavailable: a fresh request
returned a cache miss, so no correction wording is invented. See the
[publisher volume](https://link.springer.com/book/10.1007/978-3-319-10575-8) and
[author correction file](https://www.sosy-lab.org/research/pub/2018-HBMC.Combining_Model_Checking_and_Data-Flow_Analysis.Errata.txt).

SRC-058 uses the ScienceDirect chapter identities. Chapter 8 is by Joachim
Parrow, corroborated by the author's Uppsala record; the shop's `P. Parrow`
rendering is retained as discrepant metadata. Ten technical versions receive
separate units: eight captured author/report PDFs, the February 2000
Bradfield–Stirling preprint and Ponse's 61-page recursive-operations PDF. The
61-page PDF link was recovered from the author's publication entry 68 on this
date; it remains distinct from CWI's 57-page version. The author states that
versions may differ from their published counterparts, so no byte identity is
assumed. See [Ponse's publication list](https://staff.fnwi.uva.nl/a.ponse/publist/pubs.php)
and the [61-page source](https://staff.fnwi.uva.nl/a.ponse/publist/handbook.pdf).
No manuscript body was locally acquired in this mapping task.

The SDL CWI capture identifies `SEN-R9809`, 30 June 1998. A separate metadata
record gives `R 9807`; that record does not overwrite the captured manuscript
identity. The 92-page action-refinement source has metadata title `final.dvi`
and a corrupted text extractor; its intended chapter identity comes from the
author link, and its readable body remains acquisition work. Failed alternate
Eindhoven/SOS requests remain acquisition routes, not proof of new content or
of equivalence with another PDF. The exact route and failed outcome survive in
the original request plan and record crosswalk.

SRC-059 retains seven technical version units in addition to the 1990 chapters:
the 8 June 2008 Berstel–Boasson revision; the separately authored *Semantic
Domains* and *Denotational Semantics* chapters within DAIMI PB-276 (1 April 1989);
Kozen–Tiuryn's January 1989 report; Cousot's author-distributed presentation;
Kanellakis's Brown CS-89-39 (November 1989); and Lamport–Lynch's 64-page manuscript
dated 3 February 1989. The DAIMI report is one physical source containing two
different intellectual treatments, not one chapter attributed to all three
authors. See the [DAIMI report record](https://tidsskrift.dk/daimipb/article/view/7630)
and [Lamport–Lynch author record](https://www.microsoft.com/en-us/research/publication/distributed-computing-models-methods/).

The 1992 second impression and 1994 paperback records remain separate
manifestation evidence for the 1990 volume. Their catalog records do not prove
either material change or exact identity. The whole first-edition chapter
obligations are fixed; source acquisition must compare any subsequently used
manifestation and retain substantive changes. Publisher and author page-span
differences for Barendregt, Cousot and Thomas remain explicit. They do not permit
dropping the beginning or end of the exact named chapter. The shop's `Bozzano G
Luisa` and `G.A. Gunter` strings do not replace the actual editor Jan van Leeuwen
or the author identities in the chapter and DAIMI records.

SRC-060's eleven chapter authors are taken from the actual Pageplace preview
contents, source lines 215–250. This includes Gilbert Harman's distinction
between implication and reasoning, Perkins's empirical critique, Barth's
dialogical account, Hintikka–Halonen–Mutanen's interrogative reasoning,
Johnson–Blair's informal logic and Williamson's probability logic. These are
separate treatments with different kinds of evidence. The chapter-1 preview
contains actual discussion of practical reasoning and idealized agency; that
technical text is retained as part of chapter 1, never classified wholesale as
metadata. Overlapping preview captures are repeated evidence of the same
identified extent. See the
[official distributor preview](https://api.pageplace.de/preview/DT0400.9780080532912_A25036935/preview-9780080532912_A25036935.pdf).

SRC-061 selects the 2007 *Quantum Structures* volume, not its differently titled
companion volume or the shop's later product timestamp. Four versions remain
separate: Harding's 34-page manuscript; Ying's 147-page *A Theory of Computation
Based on Quantum Logic*; arXiv:0710.2098v1; and arXiv:0812.3072v1. The current
[0710.2098v1 record](https://arxiv.org/abs/0710.2098v1) confirms 10 October 2007 and
42 pages. Its map explicitly retains the hypotheses in the Piron corollary:
irreducibility, completeness, atomicity, orthomodularity, covering law and rank
at least four, alongside the projective and Hilbert geometry equivalences.
The 0812.3072v1 date, 16 December 2008, and its publication assertion are held in
the original author capture; the new direct request returned a cache miss.
Neither source is credited as the publisher chapter without comparison.

SRC-062 preserves eleven complete 2012 historical chapters and their actual
subsections. The official and institutional contents both give chapter 1's
start as 11, so the map does not silently convert that field to 1. The
institutional title variants and the different author/publication page spans
remain source evidence. The 13-page Moktefi 2013 final draft *La représentation
visuelle des classes d'objets* is related material for the diagram chapter,
not that chapter's body or an automatic additional whole-paper obligation.
Its actual technical excerpt is retained as background; a specifically used
claim requires its own bounded prerequisite. See the
[institutional contents](https://web.flu.cas.cz/scan/323557072.pdf) and
[Moktefi source](https://philarchive.org/archive/MOKLRV).

## Complete producer-family classification

The relevant original `build_acquisition_note.py` producer was read completely
for each of the six sources. These programs generate topic rows from metadata
keys, array/object structure, HTTP plans and failures, physical text lines,
JSON-field replays, contents and generic obligation templates. A generated
topic is therefore not automatically an intellectual treatment.

The mapping reuses each source's existing gzip CSV, parent structure and exact
extraction receipt. It checks those files against their saved hashes and
accounts for every source, hierarchy and topic record. It does not rescan the
7 GB historical catalog. Consecutive records are grouped only within the same
source, parent, record type, disposition, target set and producer role; numeric
endpoint/count agreement is checked.

Actual chapter scope and technical excerpts map to substantive obligations.
The original content-template slots map to those exact chapter treatments,
subject to the governing applicability decision: a historical chapter need not
invent an algorithm, nor does a copyright page acquire a theorem obligation.
Physical-line or field-level replays retain the original captured payload as
aliases; they do not create another copy of a source treatment. Serialization
keys, zero-byte artifacts, HTTP failures, scripts, bibliographic descriptors,
page-image requests and production records retain evidence roles. Mixed
captures preserve technical fragments and their context, including reference
lists and unrelated search results, without automatically commissioning every
mentioned work.

Each `SRC-NNN-producer-family-dispositions.json` gives the exact producer hash,
role counts, dispositions and target bindings. Each `SRC-NNN-semantic-mapping-receipt.json`
gives the output hashes, component/unit counts and complete raw-record counts.
The six entries in `SRC-057-062-batch-receipt.json` identify the files to use in
the combined tail manifest. Older unrecognized-family files, if present, are
construction diagnostics superseded by the final zero-residual receipts.

The complete map claim here concerns finite source scope and record accounting.
Full source acquisition, writing, exact manuscript overlap integration,
correction application, independent review and publication acceptance remain
separate work. No manuscript builds, renders or test suites were run.

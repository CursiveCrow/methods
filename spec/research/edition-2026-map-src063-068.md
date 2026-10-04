# SRC-063–068 coverage construction

Date: 9 September 2026. Scope: the finite coverage map for the CRC-style
handbook of logic and reasoning. This work adds source allocations and record
roles. It does not author manuscript chapters or admit scientific claims.

## Published shards

The source mapper published the following stable files in
`spec/coverage/edition-2026/sources-037-068/`. For each source, the two files are
`srcNNN-content-units.jsonl` and `srcNNN-historical-records.jsonl`. Exact bytes,
SHA-256 hashes, component counts, role counts and original membership checks
are in the corresponding `SRC-NNN-semantic-mapping-receipt.json` under
`tmp/edition-2026-catalog-src038/tail-039-068/`.

| Source | Units | Components | Original records mapped |
| --- | ---: | ---: | ---: |
| SRC-063 | 155 | 534 | 56,486 |
| SRC-064 | 11 | 47 | 2,849 |
| SRC-066 | 27 | 228 | 5,933 |
| SRC-067 | 16 | 118 | 12,043 |
| SRC-068 | 19 | 71 | 11,807 |

All listed original records have resolved construction mappings. Each original
source CSV was parsed in full, and the topic count and ordered topic-title hash
were checked against every preserved parent. The original CSV fields and files
remain intact. No full 7 GB corpus rescan was performed. SRC-065 was explicitly
transferred, before any edits, to the combined historical-tail lead; its separate
stable receipt reports 23 units, 558 components and 58,019 original records.
That lead owns combined manifests and the combined source note.

Content acquisition and manuscript writing remain visible as unfinished work.
A title, abstract, contents page, public text extraction or failed request is
never credited as the complete acquired source body.

## SRC-063: eleven-volume History of Logic

The complete chapter identity set contains **138 actual published chapters**:
8, 13, 11, 15, 16, 11, 9, 10, 16, 18 and 11 chapters in volumes 1 through 11.
Every chapter has an exact author, printed page extent, original edition/year,
specific methodological subject, required components, proposed body and proof
destinations, and success/failure conditions. The source-local notation and
historical interpretation must be retained. Modern comparisons require their
own hypotheses; historical philosophical prose is not forced into an invented
calculus.

The complete identities are preserved in
`tmp/edition-2026-catalog-src038/tail-039-068/SRC-063-exact-chapter-identities-v2.json`.
The v1 extraction remains evidence; v2 fixes the extraction of ORCID image
labels from author names. The original catalog display itself was not changed.
The chapter methods are explicitly allocated in `SRC-063-method-scopes.tsv`.

Primary publisher contents were read from all ten successfully retained
Elsevier shop pages and the first exact publisher result in
`web-search-elsevier-shop-volume-10-full.txt`. The original DBLP captures cut
off late chapters in several volumes. Their complete bibliographic tails were
read on 9 September and preserved separately as
`SRC-063-dblp-live-tail-a.txt` through `-f.txt`. These catalog records establish
chapter identity and pagination, not mathematical proofs. Direct public DBLP
API acquisition failed; its distinct failure receipt is retained and no JSON
body is credited. ScienceDirect direct-volume opens also returned 403.

The publisher shop contents are not always the final contents:

- Volume 4's actual published sequence contains Mander's **Bradley's logic**,
  pp. 663–717, omitted from the shop list. It is `ED26-SRC-063-0415`.
- Volume 5 contains **Jacques Herbrand: Life, Logic, and Automated Deduction**,
  pp. 195–254, omitted from the shop list. It is `ED26-SRC-063-0505`.
- Volume 2's second published chapter is John Marenbon's **Logic at the Turn
  of the Twelfth Century**, pp. 65–81. The shop's advertised Iwakuma chapter
  is preserved as catalog evidence; it does not replace the actual final
  author/chapter. The author-hosted volume contents independently identify
  Marenbon: [Fordham volume manifestation](https://faculty.fordham.edu/klima/MLM/HHL-Volume2.pdf).
- Volume 9's shop advertises Finkbeiner's **Logical Synthesis of Reactive
  Systems – from Church's Problem to Modern Applications**. The actual final
  volume has 16 chapters and lacks that chapter. The final contents and
  editorial note are retained at source rows L61–106 in the file named
  `web-open-pageplace-volume7-preview-pdf-renderer.txt`. Its actual title is
  **Computational Logic, Volume 9**, not Volume 7:
  [publisher preview](https://api.pageplace.de/preview/DT0400.9780080930671_A23591952/preview-9780080930671_A23591952.pdf).
  The root explicitly approved treating the announced title as catalog data,
  linked to independently selected synthesis obligations, on this turn.
  `ED26-SRC-063-9998` preserves that disposition. No nonexistent published
  chapter is invented, and actual synthesis content obligations remain.
- The fuzzy-logics chapter in Volume 8 has four authors, including Francesc
  Esteva. The three-author shop display is preserved as source evidence.

The explicitly selected Fordham entire-volume manuscript retains thirteen
separate chapter allocations (`ED26-SRC-063-2001`–`2013`). Its reported 726
physical pages are not a claim of 726 locally held pages. The separately
requested Galavotti author PDF remains `ED26-SRC-063-2105`, with its original
failed acquisition outcome and an explicit comparison obligation. The Kanamori
publisher sample and actual Volume 9 preview are bounded fragments of their
identified published content. They do not produce new whole mathematical works.

Original source-text fragments remain attached to the exact source family.
Repeated L-numbered extractions are recorded as repeated captures, not extra
theorems. Mixed search-result containers retain their actual snippets, source
URLs and clipped context in `ED26-SRC-063-9997`; incidental hits do not select
every returned book or article for complete reconstruction. This is consistent
with the lead's source-template and related-evidence policy.

Useful subject bindings for the gap map are:

- `ED26-SRC-063-0102`: Woods/Irvine, Aristotle's early logic, pp. 27–99.
- `ED26-SRC-063-0103`: Boger, Aristotle's underlying logic, pp. 101–246;
  categorical syntax, semantics, deduction/reduction and contrasted-instance
  inconcludence are explicit required components.
- `ED26-SRC-063-0104`: Johnson, Aristotle's modal syllogisms, pp. 247–307.
- `ED26-SRC-063-1110`: Woods, history of fallacies, pp. 513–610, including
  its complete Aristotle section 2. The contents alone do not verify a full
  thirteen-fallacy enumeration. The distinct modern inference-defect index
  needs its own additional source/argument allocation.
  [Exact published chapter](https://www.sciencedirect.com/science/chapter/handbook/pii/B9780444529374500101).

## SRC-064: actual and potential contradictions

The eight complete published 1998 chapters are allocated individually from
the exact [publisher book and chapter records](https://link.springer.com/book/10.1007/978-94-017-1739-7),
preserved in `tmp/acquisition/src064/web_source_presentations.json`.
The 1995 Utrecht report **Modal Logics for Representing Incoherent Knowledge**
and the 1996 defeasible-logics author draft/VUB source link remain distinct
allocations. The latter's full exposed section hierarchy is retained, including
system Z/Z+, conditional entailment, Simari–Loui arguments, preferred
subtheories, ordered logic, Nute systems, preemption and Ryan's ordered theories.

Volume editors Besnard/Hunter remain distinct from series editors Gabbay/Smets.
Institutional author-list/date errors do not replace the three published authors
and 1998 date of **Defeasible Logics**. All original 90 failed direct requests
retain their real acquisition role; no source body was produced by those failures.

## SRC-066: spatial logics

All 15 published 2007 chapters are mapped with their specific reasoning
questions and exposed internal sections. Exact publisher titles/authors/pages
and the complete institutional contents capture are in
`tmp/acquisition/src066/web_source_presentations.json`:
[publisher edition](https://link.springer.com/book/10.1007/978-1-4020-5587-4).
Eleven separately identified technical author manifestations remain distinct,
including the 2006 ILLC preprint, author versions with different numbering,
the Vickers extra Further Reading section, the Birkbeck placeholder-reader
draft, and the separately described Kurucz source. Source-draft differences
are not accepted as equality from their shared title.

The actual source chapter **Spatial Logic + Temporal Logic = ?** is pp.
497–564; the KCL portal's 97–564 field is preserved as erroneous metadata.
Steven Vickers is the chapter author; book editors appearing in an institutional
export are not silently added as chapter coauthors. CVs, source previews,
copyright and second-reader records retain their distinct apparatus roles.

## SRC-067: universal algebraic logic

The seven published 2022 chapters and complete exposed section hierarchy are
mapped separately from eight chapters of the **13 December 2007 incomplete
preliminary version**. The published work has four authors; the preliminary
title page has three. The versions reorder and reorganize material and cannot
be interchanged. The preliminary explicitly assumes ZFC; it does not prove
that foundation.

Primary identity and chapter abstracts are at the
[publisher edition](https://link.springer.com/book/10.1007/978-3-031-14887-3).
The complete 2022 contents string is retained as institutional source row L101
in `web-open-institutional-catalog-presentations.txt`. The preliminary's own
contents and actual excerpt are in `web-open-renyi-preliminary-pdf-renderer.txt`:
[separate preliminary](https://www.renyi.hu/~sain/ans-gal.pdf).
Only rows L0–395 through physical page 11 were retained in that capture;
182 reported pages do not establish a held full body. Logical/algebraic
equivalences, syntactical/ordinary/local/weak Beth properties and each
amalgamation/interpolation condition remain source-specific components.

## SRC-068: nonclassical logic and fuzzy foundations

The thirteen published chapters of the 1995 first edition are allocated from
the exact [publisher contents and abstracts](https://link.springer.com/book/10.1007/978-94-011-0215-5),
preserved in `tmp/acquisition/src068/web_source_presentations.json` and its
individual raw files. The 1993 Wyler report and separately linked Klawonn
author PDF retain their own acquisition/comparison obligations. The 1992
seminar, 1995 edition, erroneous 1999 bibliography date and 2012 digital posting
remain distinct facts.

The actual two-page Belluce preview is retained as source content for the
alpha-complete MV-algebra chapter, including the distinction between bold
algebras and pointwise-supremum-preserving bold fields. The unrestricted claim
in the introductory abstract that every nonclassical logic is a fragment of
classical logic has an explicit direct-correction task: state the intended
systems/common language and preserve counterexamples to an unrestricted claim.

The captured LINZ2005 material is not mislabeled as metadata. Baaz's exact
Herbrand/Skolemization abstract and the clipped Behounek–Cintula higher-order
fuzzy-relations excerpt are bounded content allocations. Other actual Klawonn
technical abstracts are preserved as bounded related evidence. These captures
do not silently select the complete 2005 conference proceedings or every
paper on an author page. Any substantive use beyond the actual excerpt needs
the exact primary work and complete context.

## Remaining work and completion boundary

All six source groups have finite construction allocations after the separate
SRC-065 work by the combined lead. The combined lead and root still integrate
the exact files/manifests, resolve shared source/prerequisite identifiers and
check complete-set accounting. These records do not establish full acquisition,
authored completeness, independent source review or publication acceptance.
No manuscript authoring, builds, renders, tests or review waves were run here.

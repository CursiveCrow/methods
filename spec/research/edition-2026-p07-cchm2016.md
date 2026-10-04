# Original CCHM 2016 v1: acquisition, reading and bounded authoring

Working record for the 35-minute block beginning 2026-10-03 04:46:51 UTC.
This is authoring evidence, not independent review, publication acceptance
or a change to the frozen source queue. Prior Nyaya files remain untouched.

## Exact allocation and identity

The source-specific unit is ED26-REQ-N-x-002-01, component N-x-002-C01,
with facets N-x-002-S01-PRESENTATION, N-x-002-S01-PROOF and
N-x-002-S01-BRIDGE. The exact allocation is in
spec/coverage/edition-2026/requirements-units.jsonl:541 and
spec/coverage/edition-2026/completion-work-queue.jsonl:541; the original
requirement crosswalk is requirements-crosswalk.jsonl:172.
It allocates the complete original presentation, including semantics,
univalence and circle/truncation extensions, not just familiar HoTT terms.

The originally supplied N-x-013 identifier was corrected before authoring:
it belongs to Jacobs/Lurie categorical logic and receives no credit here.
ED26-REQ-N-x-001-01 is the distinct general HoTT2013 allocation.
The new body concerns proposed sections 91.4–91.8: dimensions/faces,
composition/filling/transport, computational univalence, computational
theorem scope, and comparison with axiomatic HoTT. Parent owns routing.

Exact primary source: Cyril Cohen, Thierry Coquand, Simon Huber and Anders
Mörtberg, Cubical Type Theory: a constructive interpretation of the
univalence axiom, arXiv:1611.02108v1, submitted 7 November 2016 at
15:25:28 UTC. Official metadata checked at
https://arxiv.org/abs/1611.02108v1. Later conference/journal versions are
not substituted for this allocated version.

## Legitimate acquisition and frozen manifestations

All acquisition was from the official version-pinned arXiv routes,
without authentication, payment, security bypass or TLS bypass.
Downloads and source extraction remain inside source/references/p07-cchm2016/.
The archive listing was inspected before extraction: six regular files,
no traversal or linked targets. No acquired source was executed or compiled.

| Artifact | Route or provenance | Bytes | SHA256 |
|---|---|---:|---|
| 1611.02108v1.pdf | https://arxiv.org/pdf/1611.02108v1 | 396214 | b9ccc6ae8572db9521927211f7ae86b404eff6955051fafb825df5f9238022f8 |
| 1611.02108v1-source.tar.gz | https://arxiv.org/src/1611.02108v1 | 48846 | add110a1315a2b62b5ab4d22c89420d882fe6c53ad1df7c57e7b67378e56d389 |
| cubicaltt.tex | official source archive | 115878 | fdeaebeb2fd47f3163c9ef791cb389b15dc102bc5ec8a6ec7425e5d8e96c4881 |
| appendix.tex | official source archive | 20969 | 91f0c4de60a43d405060ae5fb71f851955ff2afd2501c690fbebdf96320542d0 |
| main.tex | official source archive | 5475 | a34ed50ea16ad122f59c0d55df4e2852372e3a4d741d22210e542c860aaeacb8 |
| macro.tex | official source archive | 4505 | 000de01ddd421beacf8d7419bc768c9a8a9eae585535a04969fe7a97c3317cb7 |
| main.bbl | official source archive | 6180 | 4b181eb8d147270e7af37f6d3402797c4375d0a6b65fccf2a7215384f49bc83e |
| 1611.02108v1.layout.txt | pdftotext -layout derivative | not a primary version | 68819267bd612d709dd533ee2a84bd3129e8264b4e6c713c7b02ce3d8e679370 |

The PDF has 34 pages. Its LaTeX PDF creation metadata is 14 November 2016;
the version identity is the official v1 submission, not that regeneration
timestamp. The archive also includes mathpartir.sty (17071 bytes), retained
but not loaded into the handbook. Existing handbook rule conventions are
used instead; no source macros or global commands are installed.

## Actual primary reading

Complete main.tex and macro.tex read. Complete cubicaltt.tex, lines 1–2940,
read through successive contiguous blocks, including Section 8 semantics,
Section 9 extensions and concluding qualifications. Complete appendix.tex,
lines 1–552, and complete main.bbl read. The proof/construction reading
used original TeX, not search snippets or a later HTML conversion.
The PDF text derivative was used as a locator aid. No claim of complete
visual reading of all 34 PDF pages is made.

Literal source anchors:

- cubicaltt.tex:56–214: basic judgments, typed substitution, Figure 1,
  dependent product/sum/natural-number rules and substitution lemma.
- cubicaltt.tex:215–557: interval algebra, names, paths, Figure 2,
  path operations, function extensionality and singleton contraction.
- cubicaltt.tex:558–901: face lattice, restrictions, face universal
  operation, systems, cover/overlap duties and admissible restrictions.
- cubicaltt.tex:902–1114: composition, uniform substitution, filling,
  product/sum/natural-number/path computations and transport.
- cubicaltt.tex:1115–1289: contractibility, extension, preservation paths
  and contractible-fiber equivalence operation.
- cubicaltt.tex:1290–1537: Glue, Figure 4 and its composition algorithm.
- cubicaltt.tex:1538–1712: Russell universe, explicit transport
  equivalence, original fiber contraction and universe composition.
- cubicaltt.tex:1715–1827: unglue equivalence and univalence route.
- cubicaltt.tex:1828–2564: cube category, presheaf/fibrant semantics,
  semantic Glue, universes, partial interpretation and soundness statement.
- cubicaltt.tex:2565–2875: marked identity paths, identity elimination,
  dependent paths, sphere/circle and propositional-truncation extensions.
- cubicaltt.tex:2876–2940: related work, source-relative future normalization
  boundary and acknowledgments, including removal of empty-Glue collapse.
- appendix.tex:1–291: complete corrected Glue composition detail;
  PDF pages 30–32.
- appendix.tex:292–405: univalence alternatives and comparison/coherence
  requirements; PDF pages 32–33.
- appendix.tex:406–552: singular cubical sets and uniformity discussion;
  PDF pages 33–34.

Main-section PDF locators actually checked in the derivative: basic theory
starts page 3, systems page 7, derived operations page 12, Glue page 13,
universe page 15, semantics page 17, extensions page 24, related work
page 27. Original TeX line anchors remain the exact evidence locators.

Huber source: official https://arxiv.org/abs/1607.04156v1 checked.
Simon Huber, Canonicity for Cubical Type Theory, submitted 14 July 2016
14:47:06 UTC, 31 pages in its metadata. Source main.bbl:84–88 identifies
this exact v1. The abstract states canonicity for natural-number terms
in contexts containing only dimension names, via typed deterministic
operational semantics and a presheaf-like computability argument.
Only the official metadata/abstract was read; the separate PDF/full
proof was not acquired or read. The later October 2017 v2 is not used.

## Saved authoring and exact seam

New body: handbook/parts/p07/cubical-type-theory-cchm2016.tex,
entry label sec:p07-cchm2016, eight subsections.
New proof annex: handbook/annex/p07/cubical-type-theory-cchm2016.tex.
New calculus sheet: handbook/registry/calculi/p07-cchm2016-cubical.tex,
entry label sheet:p07-cchm2016-cubical, 76 rule/schema entries.
These include explicitly labeled source-admissible schemes, equality
closure schemes, the basic rules, paths, systems/restrictions,
composition/substitution, all seven Glue rules, Russell universe closure,
and seven type-specific composition clauses. The number of entries is
not a count of independently proved metatheorems.

Eight local results have complete annex construction proofs:
singleton contraction, filling's three boundaries, contractibility versus
uniform partial extension, preservation path, face decomposition,
Glue composition typing/boundaries, unglue equivalence, and original
type-line equivalence with all four cap and six side-overlap checks.
The local proofs work in the fixed source calculus, including its
source-cited admissible substitution/restriction rules; they do not
pretend to reprove the entire theory's metatheory.

Bibliography intake: handbook/bib/intake-p07-cchm2016.bib, two entries.
Local key CCHM2016ArxivV1 denotes the canonical source identity
CohenCoquandHuberMortberg2016v1; Huber2016CanonicityV1 denotes the separate
source. Symbol intake: handbook/registry/symbols-intake-p07-cchm2016.csv,
20 records with source-local roles and no newly defined global macros.

Parent integration seam: route the body under chapter 91 sections
91.4–91.8, route the annex, include the registry sheet and merge the
bibliography/symbol intakes through the parent's shared drivers.
No shared route, canonical map, generated file, queue, baseline,
coverage ledger or receipt has been edited by this authoring block.

## Exact unfinished duties

ED26-REQ-N-x-002-01 is not discharged as a complete source allocation.

1. Full univalence: prove the transport/eqToPath comparison, the
   two-dimensional Glue path comparison, and coherence of the complete
   equivalence data. Source Appendix B sketches or externally refers
   to parts of these arguments. The existence of a typed Glue path
   and the local unglue equivalence do not replace that duty.
   The selected unglue equivalence data were not claimed to restrict
   judgmentally to arbitrary original f.2; that strictness issue is
   explicitly separate from existence of an equivalence.
2. Global model proof: supply all interpretation, face weakening,
   weakening, substitution, term naturality and soundness induction
   cases; prove preservation of the associated composition structures
   and uniformity of the semantic Glue construction. The body states
   source-cited semantic results, not a full local soundness proof.
3. Source extensions: marked identity-type construction and its
   Path/Id equivalence, cofibration/trivial-fibration factorization,
   dependent path rules, circle/sphere and propositional-truncation
   computations and their required proofs remain unauthored here.
   They were actually read but are outside this cubical core file's
   bounded drafting; sibling HIT ownership is preserved.
4. Singular cubical-set uniformity proof: the source's induction and
   retraction construction have been read, but no full local proof is
   written here.
5. Separate Huber canonicity: acquire/read exact arXiv:1607.04156v1,
   match its grammar to this original theory, and reconstruct its
   typed operational semantics and computability proof. No canonicity
   proof or normalization proof follows from the saved constructor
   equations. No new globally current claim that normalization is open
   is made; the historical 2016 paper's scope is what is described.

No independent review, tests, handbook build, render or child-agent work
was performed. The research skill's default child-agent route was not
used because the explicit scoped assignment prohibits children.

The author's final save check counted the actual files and proof anchors.
Registry side conditions were put in inline math mode because the house
hbrule command typesets its fifth argument as text, unlike its premise
and conclusion arguments. This is source formatting, not a compiler check.
The body and annex explicitly disambiguate endpoint substitution from
dimension application for the filled transport families.

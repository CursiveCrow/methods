# Full-compendium transcription contract

> **Current governing amendment, 2026-09-07:**
> `EDITION-2026-CONTRACT.md` implements the user's approved
> `EDITION-2026-EXECUTION-PLAN.md`. It governs the dated comprehensive scope,
> reference entries, nineteen-part organization and direct active corrections.
> The earlier requirements below remain binding except where that explicit
> amendment supersedes them. This precedence does not grant content admission.

**Binding amendment, 2026-08-11.** This document records the user's current
instruction for the whole handbook. It supersedes every earlier plan, handover,
register ceiling, convention, or implementation note to the extent that the
earlier text authorizes compression, abridgement, normalization, editorial
selection, synthesis, retirement, or omission of logical content.

The immutable artifact record is `INHERITED-CORPUS-MANIFEST.md`; the permitted
layout and provenance architecture is `FULL-COMPENDIUM-ARCHITECTURE.md`.

## 1. Nature of the work

The deliverable is exactly one comprehensive reference handbook titled *The
Methods of Reason*, published only as the integrated
`handbook/main.pdf`. It is analogous in function to the *CRC Handbook of
Chemistry and Physics*. It is not a course, digest, survey essay, adaptation,
interpretation, curated selection, companion volume, volume set, facsimile
release, or provisional publication. The frozen inherited source and PDF are
internal authority evidence only. Completeness determines length; there is no
page-count ceiling or compression target.

The only design discretion concerns the physical and navigational layout of the
book: ordering, headings, pagination, cross-references, indexes, tables of
contents, and the placement of material in the main text or annexes. Layout may
not change, shorten, merge, strengthen, weaken, or silently discard content.

## 2. Content authorities

1. `source/formal-logic-reference.tex` at the frozen verified revision is the
   authority for inherited material. Every substantive unit in it must be
   present in the compendium in full: definitions, conventions, syntax,
   semantic clauses, calculi and side conditions, statements, hypotheses,
   proofs and proof boundaries, examples, counterexamples, exercises and their
   solutions or feedback, warnings, qualifications, tables, and source
   attributions.
   Preservation of the authority artifact and presentation of its compendium
   content are distinct obligations. The frozen TeX file is retained byte for
   byte, including all 17,206 physical lines: preamble, comments, blank lines,
   control syntax, front matter, body, and back matter. The printed compendium
   must present every content-bearing passage and rendered element supplied by
   that authority in full; it is not required to print TeX control syntax,
   comments, or blank lines as reader-facing prose merely because those lines
   are preserved and accounted for in the authority artifact.
2. The four registers enumerate additional owed domains and artifacts. They are
   inclusion requirements, not treatment ceilings. A row marked `E`, `T`, `S`,
   or `P`, or assigned a priority, does not license an abbreviated treatment.
3. New material must be reconstructed from identified authoritative sources.
   Each presentation is attributed to the source that supplies it. The
   mathematical content, notation, hypotheses, scope, and proof status of that
   presentation must be retained accurately and completely.
4. When authoritative sources give different definitions, notations, systems,
   hypotheses, or results, the compendium records the presentations separately
   and attributes each one. It does not choose a winner, silently identify
   nonidentical systems, or manufacture a hybrid.

## 3. Prohibited editorial operations

The following are defects throughout Parts 1--14, the annexes, calculus sheets,
registries, tables, figures, front matter, and back matter:

- compression or abridgement of a proof, derivation, definition, example,
  exercise, qualification, or source unit;
- replacing a full item by a pointer, capsule summary, representative sample,
  comparison-table cell, or claim that its "substance" is retained;
- retiring inherited content or omitting it as pedagogical, redundant,
  peripheral, lower priority, or outside a treatment ceiling;
- rewriting a source presentation into house notation, including changes made
  merely to avoid glyph collisions;
- selecting one literature convention while suppressing another relevant
  attributed convention;
- combining clauses, rules, terminology, notation, or hypotheses from distinct
  presentations into an unattributed composite;
- inventing a system name, technical name, notation, calculus, theorem,
  boundary, or proof status;
- strengthening or weakening a claim, changing its model or calculus class,
  dropping a side condition, or upgrading its evidence status;
- treating a register stub as delivered content.

Inherited content is transcribed without rewriting. For copyrighted external
works, independently worded prose is permitted only as part of a complete
source-grounded reconstruction that preserves every mathematical assertion,
qualification, dependency, and evidence boundary. It is not permission to
summarize, interpret, simplify, or supplement a presentation.

## 4. Required provenance record

Every substantive handbook unit must have an auditable provenance record with:

- handbook file and stable label;
- source identity and exact locator;
- presentation identity when a work contains multiple variants;
- disposition: full transcription, full reconstruction, or open/missing;
- a completeness check covering notation, definitions, hypotheses, rules and
  side conditions, statement strength, proof status, proof steps, examples,
  qualifications, and attribution;
- explicit links among separately recorded variants without collapsing them.

No unit may be called complete merely because a static checker passes or a
reviewer recognizes the topic.

## 5. Whole-book audit requirement

Every existing section is presumed untrusted until checked against its content
authority. This includes previously committed Parts 1--7, all current Part 8
and Part 12 work, the stubbed/new-domain Parts 9--11 and 13, Part 14, every
annex, and every calculus and symbol-registry entry.

The following labels are necessary because the single statuses `present` and
`missing` cannot record the distinct contract violations already evidenced by
the inherited-source audit. They are metalinguistic audit-result labels only:
they do not name logics, calculi, relations, statements, or mathematical
content. In the definitions below, an *authority unit* is the exact source
interval or identified external presentation being checked, and a *claimed
handbook representation* is the destination material asserted to discharge
that unit. These phrases are ordinary descriptions local to this paragraph,
not new content terms.

- **`full-and-accurate`** means that the claimed handbook representation has
  passed every applicable completeness dimension in Section 4 against the
  authority unit, satisfies the required disposition in Section 4, preserves
  the complete source unit in source order without content or syntax change,
  and has no defect listed below.
- **`layout-only relocation`** means that the claimed handbook representation
  satisfies the same complete and accurate content conditions, and its sole
  difference from the authority's recorded physical order or container is a
  permitted, source-mapped change of wrapper, placement, pagination,
  typography, stable label, or added navigation heading. No source title,
  wording, formula, notation, hypothesis, rule, side condition, proof boundary,
  example, qualification, or attribution differs.
- **`altered`** means that some authority-supplied content is represented, but at
  least one represented title, wording, notation, syntax, hypothesis,
  conclusion, evidence status, proof boundary, or attribution differs in a way
  not permitted by the applicable disposition or by layout-only relocation.
- **`abridged`** means that a nonempty proper subset of the authority unit is
  represented while at least one required source-supplied item is absent or is
  replaced by a pointer, capsule, sample, table cell, or shorter substitute.
- **`omitted`** means that no claimed handbook representation supplies the
  authority unit's required content.
- **`hybridized`** means that one claimed handbook presentation combines clauses
  from materially different authority presentations, or combines
  authority-supplied clauses with later or editorial clauses, without
  preserving explicit boundaries and attribution for each.
- **`unsupported addition`** means that handbook content has no identified
  authority and exact locator supporting the content and its asserted
  presentation identity, theorem or rule status, syntax, example, or claim.

The two passing labels are nonredundant: **`full-and-accurate`** records the
source unit present in source order without a separately recorded change,
whereas **`layout-only relocation`** records that the complete unchanged source
surface remains but one or more expressly permitted layout properties differ.
The defect labels are nonredundant: **`altered`** records changed supplied
content; **`abridged`**
records incomplete supplied content; **`omitted`** records absent supplied
content; **`hybridized`** records an unseparated combination; and
**`unsupported addition`** records content lacking source support.
**`full-and-accurate`** and **`layout-only relocation`** are mutually exclusive
and neither may accompany a defect. Defect labels may co-occur when their
definitions are independently satisfied. The labels are used only in source-to-handbook and
handbook-to-source audit ledgers and in the corresponding release gates; they
cannot establish completion without the provenance and independent evidence
required elsewhere in this contract. A register row that has no identified
authority and claimed destination remains `open` rather than receiving one of
these comparison results. Every defect requires restoration or full
source-grounded construction.

## 6. Completion gates

The compendium is not complete until all of the following independently pass:

1. every inherited source unit is present in full;
2. every register-required topic and apparatus item is present in full;
3. source acquisition has been independently audited with no known missing
   handbook series, volume, standard, primary presentation, maintained system
   reference, or established logic domain; every known gap or unresolved
   acquisition keeps this gate open;
4. every external addition has primary-source provenance and a complete
   presentation-specific reconstruction;
5. every materially different presentation found by source acquisition or
   required by a register is separately represented and attributed;
6. every proof is complete or is accurately identified as a source proof
   sketch/open boundary without pretending that an abridgement is a proof;
7. every rule and side condition matches its presentation;
8. bibliography, notation roles, labels, cross-references, and indexes are
   complete and accurate;
9. static checks pass;
10. the full book compiles from a clean state;
11. every rendered page is visually inspected; and
12. source-fidelity AI review, topic-specialist AI review,
    adversarial-publication AI review, static validation, build validation,
    and rendered-page validation are separately recorded and all pass for every
    applicable topic and section; and
13. after every other residual is zero, the user records the only final
    editorial acceptance against the exact final PDF and readiness-manifest
    hashes.

Earlier instructions calling for 4:1 source compression, 40--60% proof length,
proof compression into annexes, deliberate retirement, treatment ceilings, or
"representative" coverage are revoked.

## 7. Independent AI review records

Every inherited unit, external-packet content item, register artifact, and
final reader-facing topic receives three independent AI reviews. Reviewers do
not receive one another's conclusions before submitting their own evidence.
There is no majority vote: any failure, uncertainty, inaccessible authority,
unsupported assertion, or disagreement keeps the item open and requires all
affected reviews to rerun after repair.

The source-fidelity review checks the complete authority surface, content and
wording correspondence, notation, order, examples, exercises, warnings,
qualifications, attribution, variants, and every applicable completeness
dimension. The topic-specialist review checks definitions before use, types,
quantifiers, hypotheses, theorem strength, proof steps, rule side conditions,
semantic clauses, counterexamples, exercise solutions, and the exact
cited/sketched/proved boundary. The adversarial-publication review searches for
omissions, unsupported additions, contradictions, collapsed variants,
terminology conflicts, broken dependencies, label/reference defects, missing
index or bibliography entries, and rendered-page defects.

The JSON labels `source_fidelity_ai`, `topic_specialist_ai`, and
`adversarial_publication_ai` are administrative fields rather than terms in the
logical content.

**Necessity.** One generic review value cannot distinguish authority fidelity,
subject-matter correctness, and an adversarial search for publication defects.

**Definition.** Each field is exactly one of `pending`, `fail`, or `pass` and
may be `pass` only with its own evidence file recording reviewer model and
version, instructions, exact scope, consulted authority files and locators,
findings, evidence digest, and that the other review outputs were not
consulted.

**Standing.** The fields are metalinguistic audit results. They do not name a
logic, mathematical relation, statement family, or source presentation.

**Nonredundancy.** The three definitions assign disjoint review questions; a
pass in one cannot imply or replace either of the others, static validation,
build validation, or rendered-page validation.

**Use.** Source-unit, handbook-unit, register-obligation, presentation-packet,
section-lock, and terminal-readiness checkers require all three exact fields
before admitting content or authorizing release.

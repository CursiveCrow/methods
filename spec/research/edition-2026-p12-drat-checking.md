# P12 DRAT construction and checking: authoring scope

Date: 2 October 2026 (local); source/evidence edition cutoff: 7 September 2026.
Standing: authored mathematical treatment, not independently reviewed, admitted,
built, rendered, or publication-accepted. This is one source/provenance note,
not a manuscript progress appendix or a coverage receipt.

## Allocated obligation and boundaries

The exact current-fulfillment row is P12, chapter 250, section 250.3, “DRAT and
checked unsatisfiability”, in `spec/coverage/edition-2026/current-fulfillment/p11-p12.jsonl`.
Its missing item was the complete DRAT checking soundness construction rather
than the existing DPLL proof or RUP/RAT vocabulary. The frozen queue was
stream-filtered only for the row's source-facet IDs; it was not rebaselined.

This authoring supplies the mathematical component of
`ED26-REQ-N-c-032-05` / `N-c-032-MAP-05` (the separately allocated
Wetzler–Heule–Hunt 2014 presentation) and `D-P11-001-GOAL-03` (additions,
deletions, checker semantics, RAT side conditions and certificate correctness).
It does not complete the other CDCL, watched-literal, activity or restart
components of the composite D-P11-001 requirement. It does not supply or claim
credit for `ED26-SRC-051-0015`: the separately identified 2021 SAT Handbook
chapter 15, pp. 635–668, and its author/final-galley variant remain owed.
The inherited U00927–U00931 and U00940–U00943 facets retain their existing
source-specific restoration destinations; they are not duplicated as new DRAT
source credit. No queue, map, ledger or receipt was edited.

Read before authoring: complete `handbook/CONVENTIONS.md`,
`spec/EDITION-2026-CONTRACT.md`,
`spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md`; current SAT reader body,
its complete DPLL annex, and the Formal Practice supplement; and the two
inherited Formal Practice intervals 14095–14146 and 14231–14270. The old
`spec/research/p12-new-content.md` was used only for its allocated source
locator and the bounded SAT/CDCL source-accounting passage, not its superseded
compression, deferral or migration instructions.

## Primary captures and actual reading

All captures below were downloaded through public primary author/arXiv routes
without purchase or access circumvention. They are intact PDF bytes in
`source/references/p12-drat-checking/`. Uppercase SHA-256 values below identify
the retrieved manifestations, not an assertion of equivalence to another
publication manifestation.

- `wetzler-heule-hunt-2014-author.pdf`, SHA-256
  `5D40173C512CAD111040F92064A1729BC30EC7FF74CAA6F3A4901D6F680A9001`.
  [Author-hosted paper](https://www.cs.cmu.edu/~mheule/publications/drat-trim.pdf):
  eight pages numbered 1–8; title/authors correspond to the separately recorded
  SAT 2014 publication, LNCS 8561, pp. 422–429,
  DOI 10.1007/978-3-319-09284-3_31. Actual reading: all eight pages, §§1–6
  and references, through the complete web-extracted lines 0–321; the latter
  reference interval was reread after initial display truncation. Controlling
  allocated locators: §2, Definition 1 and Example 1; §3, update formula and
  Figure 1; §5, backward checking/marking and opposing-clause scanning; §6,
  the dated empirical rather than universal performance boundary. No byte
  comparison with the publisher PDF was performed.
- `heule-2016-drat-format-v1.pdf`, SHA-256
  `18F7F11EE57C5A21711785B12ADAFA1473AB3380C68F8E7B26CAB819B1F37BCA`.
  [Official authored format description, version 1](https://arxiv.org/pdf/1610.06229v1):
  arXiv strip dated 19 October 2016, separate title-page date 21 October 2016,
  six pages. Actual reading: all six pages, web-extracted lines 0–204,
  including textual grammar, header bounds/counts, clause restrictions,
  additions, single-copy/absent/unit deletions, its eight-clause example,
  binary mapping and references. Invoked locators are the named syntax,
  addition and deletion subsections on pp. 1–3 and §1 on pp. 4–6.
- `cruz-filipe-et-al-lrat-v1.pdf`, SHA-256
  `780F938A78D3AB3E72C0C087AB91EDDDDB734A95881184038029DF9429D7B6DC`.
  [LRAT version 1](https://arxiv.org/pdf/1612.02353v1): arXiv strip dated
  7 December 2016; the retrieved twelve-page PDF independently displays
  6 October 2018 on the title page. Do not erase this manifestation detail.
  Actual bounded reading: pp. 1–8, including §§1–3, the displayed §4 checker
  statements, and the beginning of p. 9, web-extracted lines 0–378. Only the
  §§1 and 3 interface/hint and untrusted-elaborator boundary is invoked; the
  LRAT implementations, formal proofs, experiments and remainder are not
  claimed reconstructed or accepted here.
- `baek-carneiro-heule-frat-v1.pdf`, SHA-256
  `9C5BF43D7B56F80B56B54B925A90944B341EDAC4D43767E26A1ADF9E9A5B1C1C`.
  [FRAT September 2021 version 1](https://arxiv.org/pdf/2109.09665v1):
  twenty-one-page journal-submission preprint, explicitly distinguishing
  its prior TACAS 2021 presentation and added PR scope. Actual bounded reading:
  pp. 1–7 and the opening of p. 8, web-extracted lines 0–365. Only §§1–2
  optional annotations, clause identifiers, finalization and elaborator
  interface are invoked. No FRAT/PR algorithm, empirical benchmark or later
  journal result is discharged by this chapter.

The source PDF mathematical definitions were read from extracted text. Web
source-page screenshot requests were made, but pixels were not delivered for
inspection through the available orchestration result; no successful source
visual inspection is claimed. No manuscript render was attempted.

## Presentation distinctions preserved

The 2014 AT definition is its literal-addition closure, and RAT tests
`C union (D minus complement-pivot)`, retaining the pivot. The body defines
that exact test, then separately proves the ordinary-resolvent bridge with
the active opposing-clause hypothesis. The literal-extension rule alone does
not detect an already present empty database clause; the general operational
RUP interface handles that explicit terminal case. This is proved rather
than silently crediting the source with an unstated literal-extension case.

The 2014 set-based update and deletion-presence expectation remain distinct
from the 2016 multiset interpretation, duplicate-free/non-tautological clause
restrictions, absent-deletion warnings, ignored unit deletions in its described
implementation, and acceptance at the first validated empty addition. The
2016 binary encoding is attributed only to that dated format note. The source's
2014 Figure 1 ten-clause input has not been silently replaced by the 2016
eight-clause input. LRAT and FRAT are separately attributed later interfaces,
not original 2014 DRAT features. Projected/counting limitations are established
by an explicit two-model-to-one-model vacuous-RAT counterexample, not by an
unsupported claim about another format.

## Reader and proof deliverables

Body: `handbook/parts/p12/drat-certificates-and-checking.tex`, main anchor
`sec:p12-drat-certificates-and-checking`. Annex:
`handbook/annex/p12/drat-certificates-and-checking.tex`. Six reciprocal full
proof pairs (no sketches and no new body proofs):

1. `thm:p12-drat-up-sound` / `annex:p12-drat-up-sound`: finite termination,
   forced-literal induction, inconsistent assumptions, empty clause/database
   and tautological-clause cases.
2. `thm:p12-drat-ala-rup` / `annex:p12-drat-ala-rup`: least finite closure,
   closure-order independence, both ALA–UP directions, entailment and
   database/clause monotonicity; the direct empty-input-clause boundary.
3. `thm:p12-drat-resolvent-test` / `annex:p12-drat-resolvent-test`: both
   directions of the retained-pivot bridge using the actual active opposing
   clause; nonempty RUP implies RAT on every available pivot.
4. `thm:p12-drat-rat-preservation` / `annex:p12-drat-rat-preservation`:
   pivot repair; clauses containing the pivot, neither polarity, or only its
   complement; opposing unit, tautology, no-model and fresh-variable cases.
5. `thm:p12-drat-trace-sound` / `annex:p12-drat-trace-sound`: finite checker
   termination; induction on accepted additions/deletions/no-ops; correct
   pre-addition empty-clause check; multiset single-copy extension. The
   invariant is only original SAT implies prefix SAT, not model equality.
6. `thm:p12-drat-drup-complete` / `annex:p12-drat-drup-complete`: general
   finite unsatisfiable CNF has a constructed RUP-only blocking-clause tree
   refutation, with all leaves, all internal nodes and zero-variable case;
   at most 2^(n+1)-1 additions, no polynomial-size or solver-liveness claim.

The first five are complete independently worded proofs of the allocated
checking conditions. The sixth is an explicitly identified mathematical
construction, not a claimed source-native heuristic or source performance
result. Worked body items reproduce the 2014 Example 1 separating RAT from
RUP and work every test in the complete 2014 Figure 1 log. The independently
worked false log for the satisfiable unit input gives both failed local tests
and a countermodel. These are mathematical examples, not a software test suite.

Bibliography intake: `handbook/bib/intake-p12-drat-checking.bib`; it adds only
the separately identified author/format/LRAT/FRAT manifestation keys. The
canonical `WetzlerHeuleHunt2014` record is untouched. Symbols intake:
`handbook/registry/symbols-intake-p12-drat-checking.csv`; typed empty clause vs
empty database, abstract literal vs binary integer code, and source set vs
multiset roles must receive honest root-owned scope bindings, not renamed
glyphs. All new local mathematical roles are recorded in that seven-column
intake, with permitted precedence categories and nonempty macro cells.

Suggested literal insertion seam: body immediately after the current
`sat-and-certificates.tex` chapter; annex immediately after that chapter's
DPLL annex fragment. Root owns the two drivers, canonical bibliography and
symbol registry/scope maps, crosswalks and later receipts; no shared files
were edited by this author.

## Exact verification and remaining duty

Author self-check: read the written definitions and all six proofs against
their stated quantifiers/cases; recomputed each displayed conflict by its
named clauses and checked the failed-log and count countermodels directly.
This is a mathematical author check, not independent admission. No reviewer,
test suite, static checker, build, renderer, installation or generated artifact
was run or changed.

Remaining: root literal integration and typed-role bindings; consolidated
independent source/topic/publication reviews and subsequent static/build/visual
checks. The author-hosted 2014 manifestation is captured and fully read; no
publisher-manifestation equivalence audit is claimed. The separately allocated
SAT Handbook 2021 chapter 15 and its identified author/final-galley relationship
remain entirely separate source acquisition/reconstruction duties, as do full
LRAT/FRAT constructions beyond the selected interface comparison. None of
these artifacts closes the full nineteen-part, 289-chapter, 2,475-section,
615-original-requirement manuscript goal.

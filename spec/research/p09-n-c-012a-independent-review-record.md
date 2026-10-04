# N-c-012.a independent manuscript review record

## Admission scope

This record covers only the Johan Anthony Willem Kamp 1968 source
presentation registered as `N-c-012.a`.  In the shared presentation file, its
scope begins at `\subsubsection{Kamp's 1968 thesis presentation}` and ends
immediately before the Pnueli subsection.  It does not admit `N-c-012.b`,
`N-c-012.c`, `N-c-012.d`, Part IX as a section, any build or rendered page, or
the final handbook.

The frozen content artifacts, together with the provenance ledger separately
checked by the adversarial reviewer, are:

| Artifact | SHA-256 | Review standing |
|---|---|---|
| `handbook/parts/p09/presentations/n-c-012.tex` | `0DADDC029C1ED7574B14BA6A48ACEBE712F93A125AD7641747E336FAE2788C19` | all three reviewers |
| `spec/research/p09-kamp-1968-source-note.md` | `75B83F9C5C5874F670A18F72D0FC4C151312364F53D10EC9D002DF68DE588218` | all three reviewers |
| `spec/research/p09-source-presentations-lot2-3.md` | `DA61758C3D1852B07315967C57E8C29D7F857B7C5E3FB991262FEACD2AED1953` | adversarial provenance review |

The primary authority was the complete University of Stuttgart institutional
scan at `tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf`, SHA-256
`C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA`.
It has 128 physical PDF pages; printed body page \(n\) is physical page
\(n+9\).  The relevant bibliography file was `handbook/bib/handbook.bib`,
SHA-256
`62D62CBD15EFC7D8CFC208406DEEFA9FCC8912422EE4D7FE02B9ED72D4C0DA30`.

## Reviewer runtime and independence

The runtime exposed each canonical reviewer identity and role but not an exact
deployment or build identifier.  All three were Codex subagents inheriting the
root's GPT-5-family model.  The unavailable exact build is recorded rather
than guessed.

Each reviewer was instructed not to inspect another reviewer's output, not to
contact another reviewer, and not to edit the manuscript.  Each independently
read the frozen scope and returned its own verdict.  Reading and rendering the
source PDF was allowed only for scholarship.  Tests, checkers, scripts, TeX,
the handbook PDF, and builds were prohibited and were not used as review
evidence.

## Source-fidelity review

- Canonical reviewer: `/root/schmidt_smolka_1991_research`.
- Role: complete primary-source fidelity.
- Authority scope: the institutional thesis scan, frozen source note, and
  complete Kamp presentation.
- Final verdict on the frozen manuscript and source-note hashes: **ACCEPT**.

The final instruction required an independent rereading of the complete Kamp
scope, with particular attention to identity and rights, pagination, the four
order classes and endpoint policy, first-order vocabulary and assignment,
strict `S`/`U` semantics, both translation directions and their unequal order
hypotheses, the primitive-recursive/no-complexity boundary, Chapter IV
Theorem 3, its adjacent results, and the distinction between Kamp's printed
proof attempt and the handbook repair.  No other reviewer output was supplied.

Evidence digest: the reviewer confirmed all three frozen source hashes; the
literal unrestricted wording of printed condition `(1.b)` on thesis
pp. 105--106; its failure for an even square index, an odd square index, and
offset \(1\); the source's printed constructor parameters; the handbook's
same-parity repair; and the fact that unchanged condition `(1.a)` still yields
the isolation separation.  The reviewer also confirmed that the repair is
explicitly handbook-owned rather than misattributed to Kamp.

## Subject-matter review

- Canonical reviewer: `/root/p09_math_proof_review`.
- Role: mathematical and proof correctness.
- Authority scope: the complete current Kamp presentation, primary thesis,
  and frozen source note.
- Final verdict on the frozen manuscript and source-note hashes: **ACCEPT**.

The final instruction required a constructor-by-constructor verification of
the corrected sparse-square invariant, the expanded capture-avoiding
translation \(D\), every type and quantifier, and all earlier theorem-strength
and order-class boundaries.  No other reviewer output was supplied.

Evidence digest: the reviewer checked the atomic parity case; the inequality
used to enlarge a bounded offset window; negation and conjunction under common
bounds; both immediate-neighbor shifts; eventual constancy for unbounded
strict past and future; and the final contradiction using only the
parity-independent central-gap clause.  It also checked that the expanded
translation chooses fresh variables, alpha-renames bound variables, performs
capture-avoiding replacement, preserves the strict witness and open interval,
and has only \(t_0\) free.

## Adversarial publication review

- Canonical reviewer: `/root/mcnaughton_1966_research`.
- Role: omissions, unsupported additions, terminology, source standing,
  cross-presentation boundaries, citations, and the user-supplied five-part
  technical-name rule.
- Authority scope: the presentation, source note, `N-c-012.a` ledger entry,
  bibliography, and primary-source boundary.
- Final verdict on all current scoped hashes: **ACCEPT**.

The final recheck named all three frozen artifact hashes and required the
reviewer to verify that the ledger records the printed defect, the even/odd
offset-\(1\) counterinstance, the same-parity repair, and the separation
between source and handbook proof.  It also required confirmation that the
manuscript and source note had not regressed.  No other reviewer output was
supplied.

Evidence digest: this review forced the elimination of undefined
`\overline S,\overline U` translation constructors; removal of an undefined
standard-form name; exact Chapter I, II, III, and IV citations; removal of a
later GPSS term from the Kamp subsection; exact definitions and standing for
all operations in \(\mathcal S'\) and for expressibility from that basis; an
exact statement of Theorem IV.1; deletion of an unused present-progressive
term; and correction of the stale source ledger after the mathematical defect
was discovered.

## Revision history and final boundary

The first independent round returned three `REVISE` verdicts.  The principal
repairs were: expanding \(D\) into typed quantified clauses; removing or
defining every technical name that lacked eliminable standing; adding exact
source locators; defining strict past, strict future, Boolean operations, and
finite expression from \(\mathcal S'\); and replacing compressed prose about
the Chapter IV induction with explicit proof data.

During that round the mathematical reviewer found a source-side error that
the existing manuscript and research ledger had repeated.  Kamp's printed
condition `(1.b)` compares matching offsets around every pair of sufficiently
late squares.  It fails for the source's own atomic valuation at offset
\(1\) when one square index is even and the other odd.  The final manuscript
therefore quotes and refutes the printed condition, adds the necessary
same-parity premise, and supplies a new valid induction.  The source note and
ledger record the same boundary.  No reviewer accepted a silent correction or
an attribution of the repaired proof to Kamp.

No majority vote was used.  All three final reviewers accepted the same
manuscript and source-note hashes, and the adversarial reviewer also accepted
the current ledger hash.  This establishes the three manuscript-content
review gates for `N-c-012.a` only.  The remaining `N-c-012` presentations,
Part IX admission, the single final publication build, rendered-page
inspection, and the user's final acceptance remain open.

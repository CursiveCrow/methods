# Construction decisions for conflicting original editorial requirements

Date: 9 September 2026. Owner: lead editor.

These decisions make the remaining work for the original requirement IDs
definite. Their authority is the approved edition plan and the current
EDITION-2026-CONTRACT.md: preserve substantive content and source variants,
correct active errors directly, provide useful reference entries, and perform
consolidated reviews after the complete change set. The older retirement and
universal-normalization prescriptions cannot override those instructions.

This is a coverage-map disposition, not a reviewed register closure. Preserve
every original row and its wording. Keep implementation, source review and
publication acceptance pending wherever they remain due. The policy decisions
themselves receive the prescribed independent consideration in the final
consolidated reviews. No historical admission record is changed here.

## 1. Indexing: L-002 and L-015

The required outcome is correct, searchable, accurately located index entries.
Automatic title indexing may remain through the maintained style interface.
The old requirement to remove every indexing wrapper is superseded as an
implementation prescription; it is not marked implemented.

Every indexed mathematical or accented title must have an explicit safe
plain-text sorting representation, including any required escaping of the
index processor's control characters. Plain titles may use a verified identical
sort representation. Attach the index write to the actual entry anchor so it
cannot drift to a later page. Preserve the displayed source name and notation.

Remaining work: reconcile the title-index interface and all entries, then
check ordering, accents, mathematical names and exact page/anchor destinations
in the final generated index. Success requires the complete entry set to have
correct keys and locations. A successful old makeindex transcript, visually
plausible title, unescaped key or wrong page is insufficient.

Destinations: handbook/handbook.sty, handbook/registry/symbols.csv, actual
indexed entries, generated final index and the existing publication records.

## 2. Live compatibility syntax: L-003

Do not delete a live macro or source proofplan environment because an older
snapshot called it unused. Preserve syntax required to present retained content.
The dead-definition cleanup applies to genuinely unused handwritten editorial
definitions after full integration. A declared external/compatibility interface
must have a concrete consumer or necessity recorded; a speculative future use
does not justify an otherwise dead definition.

The literal zero-defined-but-unused rule is superseded for documented required
compatibility interfaces. Its maintenance goal remains: enumerate local
definitions and actual uses, remove proven dead editorial definitions, and
retain exact reasons for legitimate interfaces. Use the existing static tools
and a bounded final definition/use inventory; this mapping decision does not
authorize constructing another manuscript test framework.

Success: every retained local definition has an actual role and all required
source syntax still works. Failure: deleting content support, retaining
unexplained dead definitions, or declaring a zero count without a scoped check.

## 3. Array syntax and typography: L-004 and L-005

Use the maintained editorial array/rule interfaces for new writing. Valid
source-local row separators may remain when their presentation is retained.
The universal one-separator and source-rule-macro retirement prescriptions are
superseded; neither is a mathematical repair by itself.

Correct actual typography defects in the active style/display while preserving
premises, conclusion, rule name, discharge marks, side conditions and source
attribution. All final source and registry displays must fit their allocated
measure and use readable, consistent metrics for their stated presentation.
Failure includes a clipped premise or side condition, ambiguous rule mark,
illegible typography, or a cosmetic change that changes the calculus.

Destinations: handbook/handbook.sty; affected body displays; registry/calculi;
the final consolidated publication inspection.

## 4. Rule registry and source variants: L-006, S-018, A-177 and A-192

New editorial rule sheets and their consumers use the common calculus registry.
Retained attributed source displays may appear at their full-treatment
destinations. The literal assertion that every rule display comes from one
registry, and the absolute outside-registry ban, are superseded for these
declared source presentations.

Every rule must be identifiable and citable, and all applicability conditions
must be available with the rule or its unambiguous immediate definition.
Maintain an explicit relation from each source rule to its own navigation sheet
and declared variant. Check actual correspondence; shared rendering prevents
drift only for the consumers that share it. Do not claim that materially
different source calculi are identical or that drift is impossible globally.

Success: named rules, complete side conditions, correct variant identities and
working full-treatment links for every mapped rule. Failure: hidden freshness,
substitution or discharge conditions, unciteable rules, incorrect equivalence,
or an unmapped source display. Original preservation obligations remain intact.

## 5. Status and paragraph surfaces: L-014, S-001, S-007, S-008, S-014 and A-190

Every result must have an explicit, accurate, retrievable treatment status.
New editorial theorem-class entries use the existing mandatory status-key
grammar. Retained source results and proof boundaries may keep their declared
presentation, provided the complete source-result mapping records the result,
source/version, actual proof/citation/sketch boundary and full destination.

The universal single-environment/single-key/single-spacing prescriptions are
superseded where they would erase or recategorize source presentations. This
does not waive status coverage: the final census must cover every required
result through either the editorial status interface or the exact attributed
source-result mapping. Missing, malformed or unsupported statuses fail.

A source sketch remains a sketch. If another retained requirement promises
its complete proof, that proof is still owed. A paragraph heading or the word
theorem does not establish that a proof has been supplied. Add an explicit
reference entry or label when needed for navigation, without deleting the full
source treatment. Final status census and display checks remain due.

## 6. Four major imports: S-009

Provide four separately numbered, labelled, indexed reference entries for the
forcing theorem, Gentzen's consistency theorem, second-order Henkin completeness
and higher-order Henkin completeness. Each entry must state the exact selected
claim and hypotheses, disclose its actual treatment status and link to its
complete current source treatment and any separately owed proof.

The older demand to convert the source paragraphs themselves into new theorem
environments is superseded by the authorized reference-entry layer. The four
entries, their exact claims, correct TOC/index navigation and source links remain
concrete unfinished apparatus work; a neighboring theorem is not a substitute.

Known treatment homes are the source-mapped imports in
handbook/restoration/inherited-11012-11052.tex,
inherited-12133-12217.tex, inherited-12537-12673.tex and
inherited-12784-12923.tex. Match each actual claim before assigning its entry.
This formatting requirement does not independently add an entire research-paper
proof, but all separate original proof obligations remain.

## 7. Typed local notation: L-016, S-002, S-003, S-021 and A-168

The house defaults govern newly introduced editorial notation. Identified source
presentations retain their own notation, with each mathematical role and scope
defined before use and recorded in the existing symbol registry. The older
book-wide exclusivity of cardinality bars, equivalence glyphs and a single
forcing macro is superseded for those explicit source-local roles.

This is not permission for ambiguous reuse. Where distinct meanings meet,
state the typed distinction and any valid bridge. Register both positive and
negative forcing notation and inspect their actual glyphs in the final output.
Success requires complete role/scope records and readable, unambiguous usage.
Failure includes undefined local notation, a house convention falsely described
as the only source convention, or a glyph substitution changing meaning.

## 8. The selected propositional ND calculus: R-013 and A-001

Preserve the currently specified ND-CPL calculus: finite rooted derivation
trees, explicitly scoped occurrence labels, nonvacuous discharge, and no
repetition inference. The contexted registry sheet must describe that same
calculus. A different published calculus with repetition or vacuous discharge
remains a distinct presentation where required elsewhere.

The original proposed repair of adding repetition and licensing vacuous
discharge is superseded for this selected calculus. Its functional requirement
survives: every operation used by the completeness construction must be licensed
by the actual derivation definition and displayed rules.

Current evidence read directly: the derivation definition in
handbook/restoration/inherited-02193-02340.tex, the complete
handbook/registry/calculi/nd-cpl.tex, and the 35-line completeness opening in
handbook/restoration/inherited-02665-02809.tex. The latter separately handles
the no-open-negation case by bottom elimination and the nonempty case by
merging relabeling followed by nonvacuous RAA. This identifies the intended
repair; it is not an independent acceptance of the entire completeness proof.

Success: full construction and rule sheet match the selected calculus,
including label freshness and nonempty discharge. Failure: an unlicensed
repetition/discharge, a relabeling that changes an existing discharge, or a
sheet stating a different system. Final mathematical review remains due.

## 9. Definition completeness: S-023

Use the authorized reference-entry standard for new and added entries.
Retained source definitions may keep their form when every required type,
domain, hypothesis and defining clause is explicit and retrievable. The old
reformat-every-definition prescription is superseded as a presentation rule.

No substantive definition component is waived. Map every definition's actual
requirements, supply missing clauses directly and preserve source distinctions.
Success is complete well-typed definitions with prerequisites available before
use; filling a template with invented axioms or hiding missing clauses fails.

## 10. Exercises and selected solutions: S-024 and S-025

The older exercise-retirement instruction is superseded. Preserve inherited
problems and all supplied feedback/solutions, correcting active errors directly.
The absence of exercises in two old chapters does not create a new per-chapter
exercise quota.

For the qualifying problems, preserve all ten problems and the five actually
supplied selected solutions. The source's five additional problems do not
claim that five additional solutions were supplied. This row alone does not
add a new all-ten-solutions requirement. Any independently promised proof or
solution elsewhere in the original requirements still must be delivered and
linked; it cannot be evaded by citing this selected-solution boundary.

Success: all inherited problem content and supplied solutions remain accessible,
their solution standing is accurate, and every separate owed proof is mapped.
Failure: retirement to improve a completion count, an invented completion claim,
or the loss of a required solution. Destinations include the full selected-
solution treatment and handbook/restoration/inherited-15620-15637.tex.

## Mapping and subsequent acceptance

The 26 affected IDs are L-002, L-003, L-004, L-005, L-006, L-014, L-015,
L-016, R-013, S-001, S-002, S-003, S-007, S-008, S-009, S-014, S-018,
S-021, S-023, S-024, S-025, A-001, A-168, A-177, A-190 and A-192.
Each now has a definite retained functional obligation, destination class and
success/failure condition. The mapping worker must bind its exact unit and
original component IDs to the applicable section above, preserving its current
content assessment. Independent policy, content and output acceptance remain
open until the consolidated review of the completed change set.

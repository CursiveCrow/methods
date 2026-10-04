REJECT

# Part VIII blind R2 source-fidelity admission review

## Snapshot and decision boundary

This is a fresh review of the current reader graph rooted at
`handbook/parts/p08.tex` and `handbook/annex/p08.tex`.  I did not read any Part
VIII reviewer transcript or conclusion.  The reviewed root hashes are:

- `handbook/parts/p08.tex` — SHA-256
  `ba70c057aad5947d7eaf63f744d781ee7e213aab9ae6e7b28e46bbbd89d647d6`;
- `handbook/annex/p08.tex` — SHA-256
  `9cb88c24e31f392659cbea2819f83fe4e08d23ee726d05f585e0703488d72e6`.

The source/content verdict is **reject** because two declared Part VIII
comparison-apparatus ceilings remain substantively absent or incomplete on the
reader route.  A third, narrow terminology defect should be repaired with them.
The exact inherited restoration itself passes, as do the current source map,
wrapper/anchor structure, annex reciprocity, generated retrieval, and public
notation/rule-sheet navigation.  The open provenance, build, visual, human, and
user gates are reported separately and are not used as substitutes for this
source/content verdict.

## Blocking source/content findings

### SF-R2-01 — high — A-094's LP/da Costa comparison has no reader artifact or da Costa source standing

**Locations.** `spec/registers/apparatus.csv:95`;
`spec/register-obligation-manifest.csv:421`;
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:10-35` and `:65-70`;
`handbook/bib/handbook.bib` (no da Costa/C-system record in the current file).

**Claim.** The frozen Part VIII apparatus ceiling calls for a paraconsistent
systems table comparing LP with da Costa C-systems, including failure of
explosion and the distinct designated-value versus consistency-operator
mechanisms.  This is part of charter lot 4's “all ... comparison apparatus”
surface (`board-part8-admission-2026-08-21/charter.md:29-31`), not merely a
back-office status token.

**Evidence.** The current chapter defines paraconsistent consequence and
accurately explains LP's designated values at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:12-35`; its only worked
paraconsistent comparison is the LP nonexplosion valuation at `:65-70`.  The
entire live Part VIII graph contains no da Costa system, no C-system calculus or
semantics, no consistency-operator account, and no `tab:p08-*` comparison that
could discharge A-094.  The bibliography likewise supplies no da Costa source.
Thus the manuscript neither makes the requested comparison nor fixes which
member/presentation of the C-system family is meant.  That missing choice is
source-critical: it would be unsafe to infer one generic calculus or operator
for the entire family.  A primary source suitable for fixing the historical
system boundary is Newton C. A. da Costa, “On the Theory of Inconsistent Formal
Systems,” *Notre Dame Journal of Formal Logic* 15.4 (1974), 497–510,
<https://doi.org/10.1305/ndjfl/1093891487>.

**Exact correction.** Select and name one source-fixed da Costa presentation
(or explicitly distinguish each included `C_n` presentation), give its exact
language/axioms and the source's precise consistency or “well-behavedness”
mechanism, and add the A-094 table comparing that mechanism with LP's
designated-value semantics and each system's exact nonexplosion statement.
Add the primary/authoritative bibliography record and cite the table/definition
at the point of the comparison.  Do not introduce a generic “C-system”
technical object until its necessity, eliminable definition or axioms,
standing, nonredundancy, and actual use are all fixed locally.

**Status.** Blocking.

### SF-R2-02 — high — A-093 promises contraction and revision postulates, but prints only the revision half

**Locations.** `spec/registers/apparatus.csv:94`;
`spec/register-obligation-manifest.csv:420`;
`spec/registers/new-content.csv:104`;
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:183-231`;
`handbook/bib/handbook.bib:1964-1973`.

**Claim.** A-093 requires “Contraction and revision postulates with the Levi and
Harper identities.”  The current artifact is captioned only “The eight AGM
postulates for one-step revision” and contains only revision conditions.

**Evidence.** The table at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:197-216` correctly lists
the eight revision conditions.  The following prose at `:218-231` defines the
purpose of contraction, displays Levi and Harper, and mentions partial-meet
construction, but nowhere states the contraction postulates.  Accordingly, a
reader cannot recover the contract's contraction half from the table or its
surroundings.  The cited AGM article is correctly represented in the
bibliography at `handbook/bib/handbook.bib:1964-1973`, including DOI
<https://doi.org/10.2307/2274239>; it is an appropriate source for the omitted
partial-meet contraction/revision package.  This is missing reader content, not
a request to change the already correct eight revision rows.

**Exact correction.** Expand the A-093 artifact to state the source-fixed AGM
contraction postulates with their hypotheses and exact notation, alongside the
existing revision postulates; retain and type the Levi and Harper conversions.
The caption and surrounding prose must say whether the table is the AGM belief-
set package and must keep belief-base, update, and iterated-revision variants
outside scope, as the current qualification at `:263-265` already does.  Verify
the exact contraction package against the cited AGM article rather than
constructing it by analogy from the revision rows.

**Status.** Blocking.

### SF-R2-03 — medium — the free-logic rule calls existence a “denotation premise” after expressly separating the two

**Location.** `handbook/parts/p08/conditionals-deontic-free.tex:7-32`.

**Claim.** The selected semantics interprets every ordinary term totally into
the outer domain, uses `E!(t)` to assert membership in the inner existing
domain, and explicitly says an outer-denoting but nonexisting object is not
called non-denoting.  Line 29 nevertheless calls `E!(t)` the “denotation
premise.”

**Evidence.** The semantic clauses are explicit at `:8-17`: terms have total
outer-domain values, while `E!(t)` means that the value lies in
`D^{\mathrm{in}}`.  The guarded quantifier rule at `:29-32` is formally
consistent with those clauses, but its prose reverses the distinction just
made.  The Lambert/Bencivenga source role at `:25` is otherwise scoped to the
selected negative variant and does not claim a family-wide rule.

**Exact correction.** Change “denotation premise” at line 29 to “existence
premise” (or “inner-domain existence premise”).  Do not change the displayed
rule or the outer/inner-domain semantics.

**Status.** Open correction; independently small, but source terminology should
not remain contradictory in an admission copy.

## Exact-source preservation — accepted on this snapshot

- The reader source map identifies the frozen authority and SHA-256 at
  `handbook/parts/p08/source-map.tex:5-12`, and enumerates all forty inclusive
  intervals at `:25-40`.
- A fresh normalized-byte comparison of the forty inherited artifacts against
  `source/formal-logic-reference.tex:12970-14094` found 1,125 source lines, zero
  content mismatch, zero gap, zero overlap, zero duplicate, and zero reorder.
  All forty scope wrappers and all forty corresponding provenance records are
  present.
- The driver interleaves the exact intervals and separately authored material
  only with the source hooks disabled
  (`handbook/parts/p08.tex:2-61`).  The empty-context IMLL correction is likewise
  outside the exact bytes at `handbook/parts/p08.tex:50-53`; its text expressly
  supplies the empty tensor needed by the inherited calculus without rewriting
  the source (`handbook/parts/p08/imll-empty-context-erratum.tex:1-12`).
- The source map accurately labels every interleaved file as derivative, new
  sourced editorial content, erratum, or navigation at
  `handbook/parts/p08/source-map.tex:44-80`, and states the nonreplacement/
  nonpromotion boundary at `:82-83`.  No exact unit is duplicated by the live
  route.

## Source map, wrapper anchors, and retrieval — accepted on this snapshot

- `handbook/main.tex:31` installs `handbook/parts/p08/source-anchors.tex` before
  the driver.  The source-only hook assigns the current synthetic anchors at
  `handbook/parts/p08/source-anchors.tex:78-87`; hook-off editorial material does
  not consume exact-source counters.
- The exact source contains 35 hookable environment units and 10 result-class
  units.  The generated audit retrieves all 35 (32 synthetic entry anchors plus
  the 3 inherited native labels), and the named-result surface retrieves all 10.
  Representative synthetic result rows occur at
  `handbook/generated/named-theorem-index.tex:156`, `:171`, `:256`, `:283`, and
  `:347-349`.  A current label scan found 151 live Part VIII labels and no
  duplicate.
- `handbook/parts/p08.tex:63-71` visibly introduces the generated theorem and
  definition register and accurately calls it navigation rather than source.
  Its current 164 entries cover every live body theorem/definition-class label,
  including exact and editorial units, without promoting a sketch to a proof.
- Every one of the 41 live system-card `calculus=` references resolves to one of
  38 distinct active rule-sheet definitions.  The public route from source map
  to symbol registry, precedence table, and rule-sheet catalog is explicit at
  `handbook/parts/p08/source-map.tex:85-89`.
- The registry contains 151 Part-VIII-scoped/first-use symbol rows; every such
  label is present in the current generated symbol tables and symbol index.
  This was a static source/navigation comparison only, not a PDF or visual
  check.

## Editorial source fidelity and mathematical-source support

Subject to SF-R2-01--03, the current derivative/editorial boundaries are
honest and the reviewed source roles support their local claims:

- the intuitionistic, modal, temporal/epistemic, many-valued, and
  relevance/linear supplements identify the inherited ranges they derive from,
  label themselves separately authored, and state necessity, definition,
  standing, nonredundancy, and use locally rather than impersonating exact
  source;
- the relevance cards, exact Routley--Meyer restrictions, variable-sharing
  qualifications, one-sided CLL phase semantics, IMLL/CLL/affine distinctions,
  and Lambek restrictions match the frozen evidence package
  `spec/research/p08-8.6-evidence.md:494-543`, `:545-637`, `:692-759`, and
  `:785-797`; their source identifiers and connective typography also match
  `spec/research/p08-source-syntax-correction.md:189-255` and `:276-312`;
- bibliography-key resolution over the complete live graph found no missing
  key for a `\cite`, `\textcite`, or `cited=` token; author/editor/container/
  date roles checked for the claims sampled in every lot were consistent with
  the cited primary or authoritative records;
- status-to-annex reciprocity is complete.  The exact IPL, four-system modal,
  LTL, multi-agent S5, and IMLL sketches retain sketch standing, while
  `handbook/annex/p08/source-sketch-map.tex:3-56` records their stated omissions
  and routes back without pretending to complete them.  The separately authored
  proofs are routed by `handbook/annex/p08.tex:8-10`; the current canonical-modal
  and finite-matrix/K3/LP/FDE arguments contain their advertised dependencies.

No live reader `OPEN`, stub, owed-artifact notice, or internal register-row prose
was found.  Uses of “open” in modal/topological semantics and parity-game
complexity prose are mathematical English, not construction debt.

## Register ceilings versus external administrative gates

The two blocking findings above are not based merely on a literal `status=open`:
their promised reader content is actually missing from the current graph.
Conversely, I do **not** treat the wholesale open state of the generated control
manifest as proof that otherwise present Part VIII content failed source review.
For example, `spec/register-obligation-manifest.csv:403-421` still records
A-076--A-094 as open even where a live artifact now exists.  Those control rows
need later reconciliation against current labels/hashes.

The per-interval provenance records also intentionally remain administrative
gates.  A representative record has an open destination at
`spec/provenance/SRC-12970-12988.json:40-44`, pending completeness dimensions at
`:57-68`, source/static pass but independent-source/build/visual/human fields
pending at `:70-76`.  This transcript supplies an independent source/content
decision only.  I did not run TeX, PDF, tests, or any visual inspection; final
provenance closure, build, visual, human, and user acceptance remain external
and must not be inferred from either the accepted subsections or this rejection.

## Four-lot coverage

1. **Lot 1 — checked.** Exact intuitionistic intervals, derivative supplement,
   negative translations, Kripke/algebraic/topological/realizability boundaries,
   IQC, figures/tables, source roles, result anchors, and annex reciprocity were
   checked.  No source-fidelity blocker found.
2. **Lot 2 — checked.** Exact and editorial normal/non-normal modal units,
   correspondence, canonical model/filtration/bisimulation units, quantified
   modal/domain boundaries, cards/sheets/tables/figures, source roles, result
   anchors, and annex proofs were checked.  No source-fidelity blocker found.
3. **Lot 3 — checked.** Temporal/branching/fixed-point/epistemic/dynamic/hybrid
   material and the conditionals/deontic/free chapter were checked, including
   cards, figures, citations, statuses, and navigation.  SF-R2-03 is the only
   source-fidelity correction found.
4. **Lot 4 — checked.** Exact and editorial many-valued/fuzzy/supervaluation/
   relevance/linear/Lambek/paraconsistent/nonmonotonic material, sheets,
   bibliography, audit/named/symbol surfaces, and comparison apparatus were
   checked.  SF-R2-01 and SF-R2-02 block admission.

**Not checked by design:** TeX/PDF compilation, page geometry, visual figure or
table inspection, link behavior in a rendered PDF, control-file mutation,
generated-file regeneration, test construction/execution, human review, and
book-level user acceptance.

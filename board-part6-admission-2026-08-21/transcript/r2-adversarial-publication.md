# Part VI admission board, round 2: adversarial-publication verification

Reviewer: adversarial-publication seat  
Mode: blind verification against the latest live Part VI bytes; no other seat's
Part VI transcript was read.  
Source/content disposition: **accept**.

I re-read the charter, my round-one transcript, both Part VI roots, and every
live repair surface implicated by F1--F10. I also rechecked the two exact-source
errata, body/annex proof reciprocity, the generated Part VI register, the named
theorem and forcing-symbol lookup rows, the consistency-strength table/figure,
captions/labels, and further reading. I did not edit the manuscript, control
files, generators, tests, or generated files; I ran no test or build and did
not inspect a PDF.

Two files changed while this verification was under way. The dispositions
below use the final bytes I re-read after those changes: the generated A-113
rows now contain `\hyperref`, and the A-134 arithmetic track now states
Parsons conservativity/equiconsistency rather than a strict
PRA--(I\Sigma_1) step.

## R1 dispositions

### F1 — accept-fixed

- **Current evidence:**
  `handbook/parts/p06/zfc-axiom-table-supplement.tex:16-20` now prints the
  ordinary heading “ZFC axiom reference table” and a reader note saying that
  this is separately authored side-condition apparatus and that the exact
  source remains controlling.
- **Disposition:** the former OPEN/unadmitted heading and gate disclaimer are
  gone from the live file. A-058's table label and formula side conditions are
  preserved at lines 61-125.

### F2 — accept-fixed

- **Current evidence:**
  `handbook/parts/p06/cardinals-choice-supplement.tex:232-241` defines size at
  most by an injection (A\to B) and strictly smaller size by an injection
  (A\to B) with no injection (B\to A). It states the standing as a
  metalinguistic relation among arbitrary sets, distinguishes equipotence, and
  explains the later use. The trichotomy theorem at lines 243-250 now points
  to `def:p06-size-comparison`.
- **Disposition:** the cardinal-comparison alternatives are eliminable and no
  longer import ordinal-cardinal assignment through an undefined phrase.

### F3 — accept-fixed

- **Current evidence:**
  `handbook/parts/p06/constructibility-forcing-supplement.tex:96-116` gives a
  visible nonreplacement note and a labelled standing convention. It renews
  the externally countable transitive (M\models\mathsf{ZFC}),
  (mathbb P\in M), the stronger-is-smaller orientation, external generic
  (G), and ground-model cardinal computation. Lines 109-115 define bare
  (p\forces\varphi(\bar\nu)) as the imported recursive assertion, retain
  (p\forces^{\mathrm{sem}}_{M,\mathbb P}\varphi(\bar\nu)) as the exact
  external relation, and state the cited forcing theorem's equivalence.
  `handbook/annex/p06/constructibility-forcing-supplement.tex:13-18` imports
  that standing for all three annex proofs and denies a third relation.
- **Disposition:** the ccc, nice-name, and many-Cohen statements at body lines
  118-164 and proofs at annex lines 20-107 now have a live typed context and an
  unambiguous forcing relation.

### F4 — accept-fixed

- **Current evidence:** the exact convention and poset-filter definition now
  receive governed destinations without byte edits at
  `handbook/parts/p06.tex:60-67`. The later lookup says explicitly at
  `handbook/parts/p06/forcing-vocabulary.tex:6-12` that those exact
  destinations control orientation, filters, dense sets, and genericity and
  that the lookup creates no second identity. Its only definition-class
  additions are cardinal lookup notation, ccc, and
  `\operatorname{Add}` at lines 15-76.
- **Disposition:** the reader route has one controlling identity for the exact
  forcing-order/filter vocabulary.

### F5 — accept-fixed

- **Current evidence:** `handbook/parts/p06/source-map.tex:1-17` is a visible,
  TOC-routed source map. It identifies the 23 exact intervals as the
  authoritative ordered source, classifies the categories of separately
  authored additions, denies replacement/status promotion, and announces the
  two exact-source corrections. Local reader notes occur at the ZFC table
  (`zfc-axiom-table-supplement.tex:16-20`), Choice chapter
  (`cardinals-choice-supplement.tex:26-29`), ccc section
  (`constructibility-forcing-supplement.tex:96-98`), forcing variants
  (`forcing-variants-supplement.tex:24-27`), and cardinal arithmetic
  (`cardinal-arithmetic-supplement.tex:26-29`). Printed source-disposition prose
  now says “historical v1.1 Part VII source” at
  `infinitary-combinatorics.tex:419-426` and
  `determinacy.tex:110-128`.
- **Disposition:** the reader can distinguish exact source, separately authored
  additions, and the historical source-part number without seeing admission
  workflow state.

### F6 — accept-fixed

- **Current evidence:** `handbook/parts/p06.tex:101-109` now routes A-113 once
  as the Part VI theorem/definition register and explains exact versus
  separately authored standing. `handbook/generated/audit-p06.tex:15-161`
  contains stable IDs for every live row, no `unclassified` or `invalid`
  status, and a `\hyperref[...]` on every ID. Representative exact-source rows
  are Ordered-pair identity at line 27, Set recursion at line 29, Hartogs at
  line 41, and the constructible-class theorem at line 65; their current
  statuses are proved or sketched rather than inflated. Editorial rows retain
  `cited`, `proved=annex`, or definition-class `--` standing.
- **Disposition:** A-113 is routed, classified, stably identified, and
  source-navigable. Whether the dynamic anchors land and display correctly is
  a build/link gate, not source evidence.

### F7 — accept-fixed

- **Current evidence:** the governed Part VI theorem hooks are declared at
  `handbook/parts/p06.tex:27-47`. The generator enumerates all twelve formerly
  unlabelled Part VI source results at
  `tools/build_named_theorem_index.py:29-40` and validates the Part VI hooks at
  lines 144-155. The live generated index now includes, among others, exact
  AC equivalence, generic-filter existence, Hartogs, hierarchy, semantic-
  forcing monotonicity, Mostowski collapse, ordered-pair identity, set
  recursion, the constructible-class theorem, transfinite induction/recursion,
  and ordinal trichotomy. `handbook/parts/p14/master-tables.tex:233-244` now
  makes a count-free completeness statement; the stale hard-coded count is
  gone.
- **Disposition:** the Part VI named-result omissions and fixed-count mismatch
  are closed at source level.

### F8 — accept-fixed

- **Current evidence:** the generated registry has two distinct rows at
  `handbook/generated/symbols-tables.tex:407-408`: exact semantic forcing
  (p\Vdash^{\mathrm{sem}}_{M,\mathbb P}\varphi), and the imported recursive
  assertion (p\Vdash_{M,\mathbb P}\varphi), with the bare local abbreviation
  limited to the renewed convention. The compact symbol index preserves both
  rows at `handbook/generated/symbol-index.tex:473-474`.
- **Disposition:** A-164 no longer claims that the exact semantic qualifier was
  absorbed and agrees with the live body distinction.

### F9 — accept-fixed

- **Current evidence:** `handbook/parts/p06.tex:98` routes the new master
  strength surface. `handbook/parts/p06/consistency-strength-ladder.tex:1-8`
  distinguishes inclusion, interpretation, conservation, ordinal analysis,
  and relative consistency. Its table is labelled
  `tab:p06-consistency-strength-master` at lines 23-86, and the distinct A-134
  figure is labelled `fig:p06-consistency-strength` at lines 89-146. The figure
  caption at lines 139-144 denies a strict total order, large-cardinal
  existence, adjacent large-cardinal strictness, and exhaustiveness.
- **Disposition:** A-134 is present as a figure distinct from A-065 and its
  source claims are now calibrated. Render size, arrow legibility, float
  placement, and caption/page interaction still require the build and visual
  review.

### F10 — accept-fixed

- **Current evidence:** `handbook/parts/p06/determinacy.tex:38-41` now states at
  the theorem site that (\mathsf{ZF}) proves open and closed determinacy and
  that no choice principle is required. Borel determinacy remains separately
  stated over (\mathsf{ZFC}) at lines 43-48.
- **Disposition:** the first determinacy theorem now carries its exact
  set-theory background.

## Exact-source errata verification

### E1 — constructibility empty-base correction — accept

`handbook/parts/p06/constructibility-base-erratum.tex:1-17` does not alter the
exact source. It explains why the handbook's nonempty-domain satisfaction
convention cannot be evaluated at (A=\varnothing), supplies the eliminable
base clause

\[
\operatorname{Def}(\varnothing)=\{\varnothing\},
\]

and then resumes the satisfaction-based definition at the first nonempty
stage. It explicitly derives (L_1=\{\varnothing\}) and replaces the later
source proof's empty-domain wording by the direct membership calculation. The
correction has necessity, definition, standing, nonredundancy, and later use.

### E2 — relativization conjunction bounds — accept

`handbook/parts/p06/relativization-index-erratum.tex:1-23` changes neither
exact statement nor proof bytes. It replaces the ambiguous printed bounds
(j\leq m), (i\leq k) by the declared one-based ranges
(1\leq j\leq m), (1\leq i\leq k), preserves the empty-conjunction cases,
and points the following exact proof to the empty-base calculation from E1.
The correction matches the statement's lists (v_1,\ldots,v_m) and
(\varphi_1,\ldots,\varphi_k).

## Repair-exposed checks

### A-134 arithmetic edge — corrected before final disposition

An intermediate version of the new figure claimed a strict
(\mathsf{PRA}<\mathsf I\Sigma_1) consistency-strength step. The latest bytes
do not. `handbook/parts/p06/consistency-strength-ladder.tex:10-20` now defines
both theory presentations; lines 36-43 state Parsons's
(\Pi^0_2)-conservativity, equiconsistency, and the shared usual
(\omega^\omega) ordinal calibration, while isolating the strict step to
(\mathsf I\Sigma_1\to\mathsf{PA}). Lines 99-104 draw a dashed
conservativity/equiconsistency bridge and a separate solid proof-strength arrow
to PA. The new bibliography key is present at
`handbook/bib/handbook.bib:391`. This agrees with the standard statement of
Parsons's theorem; see Joosten, *Two Proofs of Parsons' Theorem*, Theorem 2.1:
<https://www.phil.uu.nl/ozsl/articles/joosten01.pdf>.

### A-113 retrieval links — corrected before final disposition

An intermediate generated table printed stable label strings without links.
The latest `handbook/generated/audit-p06.tex:15-161` wraps every row ID in
`\hyperref`, including the exact-source anchors and editorial labels. There is
therefore no current source-level retrieval blocker. Actual hyperlink targets
remain a build gate.

No other repair-exposed source/content defect was found.

## Publication/apparatus recheck

- **Route and identity:** the 23 exact inputs remain in their original order in
  `handbook/parts/p06.tex:5,49-81`; hooks are removed before editorial inputs
  at lines 82-91. The exact forcing definitions have one public identity.
  `handbook/annex/p06-route.tex:12-15` routes only the three nonoverlapping
  editorial annex children once.
- **Proof status and reciprocity:** `thm:p06-zorn` is now honestly `cited` at
  `cardinals-choice-supplement.tex:142-169`. The bounded local direction is the
  separate proved theorem `thm:p06-ac-to-zorn` at lines 171-177, reciprocal to
  `annex:p6.choice.1` at
  `handbook/annex/p06/cardinals-choice-supplement.tex:14-54`. The two
  binary-tree items, three ccc/name-counting items, and two combinatorics items
  retain exact body/annex backreferences and proof status. No cited theorem was
  relabelled as a local proof.
- **Tables and figures:** A-058--A-068, A-129--A-135, the Part VI register,
  named-theorem index, symbol registry/index, and per-part further reading now
  have live source surfaces. Captions distinguish source claims from schematic
  or conditional diagrams. The A-134 table and figure have separate labels;
  A-065 remains the detailed large-cardinal table rather than being silently
  reused as A-134.
- **References and citations:** all newly introduced reference targets checked
  in this round have live source destinations. The new or newly used
  `Parsons1970`, `Devlin1984`, `Pohlers2009`, `Simpson2009`, `Jech2003`, and
  `Kanamori2003` keys are present in `handbook/bib/handbook.bib`. This is a
  lexical source check, not a compiled-reference verdict.
- **Further reading:** `handbook/parts/p06/determinacy.tex:107-132` remains a
  subject-filtered Part VI list and now calls Jech the locator for the
  “historical v1.1 Part VII source.” The global Part VI further-reading row is
  present at `handbook/parts/p14/master-tables.tex:246-264`.
- **Reader debt:** the reviewed live Part VI surfaces contain no printed
  OPEN, unadmitted, stub, workflow, finalizer, or internal apparatus-ID debt.
  Similar text in retained historical files that are not reachable from the
  two Part VI roots is not part of this disposition.

## Evidence boundary and final R2 verdict

All R1 source/content findings are **accept-fixed**, and the two issues observed
during R2 were corrected in the latest bytes before this transcript was filed.
I found no remaining Part VI source/content publication blocker.

This is **not** build or publication acceptance. I did not compile the book,
run a checker or generator, inspect generated auxiliary files from TeX, or view
the PDF. Consequently I do not accept actual hyperlink destinations, references
or citations after compilation, theorem/figure/table numbering, named/symbol/
subject-index pagination, longtable continuation behavior, landscape pages,
float placement, blank versos, the A-134 arrow layout, or any overfull/underfull
page. Build, visual, administrative, provenance, human mathematical, and final
user gates remain external exactly as the charter requires.

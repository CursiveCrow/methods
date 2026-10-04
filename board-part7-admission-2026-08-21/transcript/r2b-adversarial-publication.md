# Part VII admission board, targeted round 2b: adversarial-publication re-review

Reviewer: adversarial-publication seat  
Scope: current live Part VII route only, with the R2 repair seams named in the
brief; no other seat transcript read.  
Mode: read-only source/content and publication-safety review; no checker, test,
TeX/PDF build, visual inspection, or handbook/spec/tool/generated-file edit.

## Verdict

The current reader-facing graph no longer contains any of my four R2
source/publication blockers.  R2-F1 is source-fixed.  R2-F2--R2-F4 are
withdrawn as *Part VII source/content publication* blockers because the live
book now states the exact evidence boundaries instead of claiming that the
literal future register work has been completed.  This ruling does not flip or
close `N-a-055`, `N-a-070`, `N-c-030`, or Phase-6 `A-074`, and it does not
constitute global compendium completion.

That distinction is required by the current contract: a proof must either be
complete or be accurately identified as a source proof sketch/open boundary
(`spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md:181-182`).  A source-admissible
cited or explicitly bounded result is not thereby a completed local-proof
register artifact.  I find no current reader-facing sentence that confuses
those two standings.

## R2 blocker dispositions

### R2-F1 — accept-fixed: A-071 now gives coherent canonical-LK standings

- `handbook/parts/p07/calculi-and-derivability-supplement.tex:49-57` now says
  that the unavailable canonical-LK cut claim is the one not established by
  the inherited sketch migrated from **source Part VIII**, and identifies that
  sketch's actual rule surface as `LK_d`.  This is historical-source wording,
  not a false pointer to the current public Part VIII.
- `handbook/parts/p07/calculi-and-derivability-supplement.tex:215-223` gives
  finite-sequent canonical-LK completeness the separate local status
  `proved=annex:p7.calculi.4`, including its equality-free and Choice scope and
  expressly making no cut-free-completeness claim.
- The A-071 catalog row at
  `handbook/parts/p07/calculi-and-derivability-supplement.tex:243-248` now
  distinguishes the inherited completeness sketch from the separate complete
  local theorem and says that no Part-VII cut-admissibility claim is made for
  canonical LK.  The former contradiction is gone.

### R2-F2 — withdrawn as publication blocker: exact Craig/Beth route is honest

The specific evidence that changes my R2 position is the completed separation
of three evidence levels:

- Maehara's purely relational, equality-free partition lemma is locally
  `proved=annex:p7.interp.1` at
  `handbook/parts/p07/cut-elimination-and-interpolation-supplement.tex:105-126`,
  with the exhaustive induction at
  `handbook/annex/p07/interpolation-supplement.tex:7-136`.
- The public proof boundary at
  `handbook/parts/p07/cut-elimination-and-interpolation-supplement.tex:130-140`
  explicitly says that arbitrary Craig still loads the inherited
  cut-elimination sketch and that function-bearing signatures additionally
  need alien-term lifting; it therefore retains general Craig and Beth as
  cited results.
- The two reader routes at the same file's lines `166-193` are explicitly
  titled “Route to the cited Craig theorem” and “Route from the cited Craig
  theorem to the cited Beth theorem,” and the latter says it is not an
  independent status upgrade.  The underlying inherited cut result still says
  `Status: proof sketch` and identifies its omitted calculus-specific table at
  `handbook/restoration/inherited-11768-11823.tex:11-55`.

Thus the reader can neither mistake the proved partition lemma for general
Craig nor mistake the Craig-to-Beth consequence map for a local Beth proof.
The literal `N-a-070` wording at `spec/registers/new-content.csv:71` remains
future register work if a complete local Craig/Beth proof artifact is required;
it is not a contradiction or unsupported status on the current Part VII
reader surface.

### R2-F3 — withdrawn as publication blocker: broad MLTT has no blanket claim

- The active rule sheet calls itself an **editorial composite**, identifies the
  sources controlling its intensional core and judgment/universe organization,
  and says that Abel--Coquand--Dybjer controls only the dependent-function,
  one-universe result, not Sigma, identity types, or the cumulative hierarchy:
  `handbook/registry/calculi/mltt-intensional.tex:1-14`.
- The body defines the selected broad calculus and its exclusions at
  `handbook/parts/p07/lambda-calculi-and-type-theories.tex:397-417`, then
  explicitly denies that the narrower theorem establishes normalization for
  every selected former at lines `419-424`.
- The cited theorem is titled and quantified over the Abel--Coquand--Dybjer
  subcalculus at lines `442-450`; the comparison table repeats the same exact
  input problem and refuses a blanket confluence/inference claim at lines
  `547-558`.  A-189 repeats that the cited decision theorem is expressly not a
  theorem about the whole active sheet at
  `handbook/parts/p07/proof-complexity.tex:254-279`.

The previous failure path depended on reading the narrow theorem as evidence
for the broad sheet.  Every public surface now blocks that reading.  The
literal broad normalization/checking work in `N-c-030`
(`spec/registers/new-content.csv:137`) remains separately visible future
register work; its absence is not concealed by a blanket theorem or false
completion sentence in Part VII.

### R2-F4 — withdrawn as publication blocker: HA properties are exactly source-relative

- IPC disjunction, HA disjunction, and HA numerical existence retain distinct
  `cited=TroelstraVanDalen1988` statuses at
  `handbook/parts/p07/functional-interpretations.tex:340-361`.
- The source boundary at the same file's lines `363-389` says exactly which
  source formalism proves them, lists the local grammar/equality/induction/
  normalization/erasure material not reproduced, and denies that the smaller
  inherited normalization sketch proves the HA claims.
- `handbook/annex/p07/functional-interpretations.tex:31-37` correspondingly
  supplies no false annex proof; it routes only the genuinely local cut-free
  LJ last-rule lemma proved at lines `6-29`.

Accordingly the reader gets a precise source-relative theorem standing, not a
promised local proof.  The words “with proofs” in `N-a-055`
(`spec/registers/new-content.csv:56`) may still require a later full register
artifact, but the live Part VII source does not claim that such an artifact is
present.  That external residual cannot be inflated into a current
reader-facing proof-status contradiction.

## Targeted repair verification

### Finite-set support Cut proof — accepted

- The new construction is defined, typed, and distinguished from the multiset
  sheet at
  `handbook/parts/p07/arithmetic-proof-theory-supplement.tex:94-127`.
  It explicitly maps primitive Cut and arbitrary-multiplicity Mix to support
  Cut, erases nonclean images, and states exactly which direction preserves
  cut-freeness.  It no longer claims a direct height-sum decrease for the
  multiset Mix/contraction grammar.
- The global measure now ranges over **all** Cut nodes, while the strategy first
  erases nonclean Cuts and then selects an uppermost greatest-rank clean Cut:
  `handbook/parts/p07/arithmetic-proof-theory-supplement.tex:129-155`.
- The annex proves decrease for nonclean erasure, all identity and bottom
  leaves, monotonicity, nonprincipal unary/binary commutations, and each of the
  `and`, `or`, and implication principal pairs at
  `handbook/annex/p07/arithmetic-proof-theory-supplement.tex:8-104`.  The
  natural-sum argument accounts for copied lower-rank internal Cuts.  Lines
  `106-121` then give both support translations, including primitive Mix, and
  preserve a cut-free return derivation.
- The body theorem at
  `handbook/parts/p07/arithmetic-proof-theory-supplement.tex:173-181` is limited
  to this fixed strategy and does not claim strong normalization of arbitrary
  Cut-reduction sequences.  I find no residual arbitrary-multiplicity Mix
  argument masquerading as this proof.

### Registered typed categorical and Cut notation — accepted

- The categorical extension defines its additional typed syntax and uses it in
  the exact typing/congruence construction at
  `handbook/parts/p07/normalization-and-curry-howard-supplement.tex:34-111`.
- Its unit/empty types, product/sum types, constructors, eliminators, Cut
  measures, and Hessenberg sum have corresponding registry rows at
  `handbook/registry/symbols.csv:432-437`.
- The generated public registry and compact lookup reproduce those rows and
  their destinations at `handbook/generated/symbols-tables.tex:540-545` and
  `handbook/generated/symbol-index.tex:42,272,279,287,507,534`.  This is static
  source evidence for retrieval only; actual hyperlinks and page geometry
  still require the later build/visual gate.

### Jäger/Schütte metadata — accepted

- `handbook/bib/handbook.bib:3530-3538` now records Jäger and Probst,
  *Variation on a Theme of Schütte*, *Mathematical Logic Quarterly* 50(3),
  258--264 (2004), DOI `10.1002/malq.200310097`.  The article metadata agrees
  with the authors' University of Bern publication list
  (`https://home.inf.unibe.ch/ltg/publications/index.html`) and the DOI record
  (`https://doi.org/10.1002/malq.200310097`).
- `handbook/bib/handbook.bib:4276-4283` records Kurt Schütte, *Proof Theory*,
  *Grundlehren der mathematischen Wissenschaften* 225, Springer (1977), DOI
  `10.1007/978-3-642-66473-1`, matching Springer's bibliographic record
  (`https://link.springer.com/book/10.1007/978-3-642-66473-1`).
- The selected omega-calculus sheet assigns the two sources their distinct
  roles at `handbook/registry/calculi/omega-arithmetic.tex:1-5`; the body uses
  the Jäger--Probst Definition 1/Theorem 2 locator at
  `handbook/parts/p07/arithmetic-proof-theory-supplement.tex:420-446` rather
  than silently treating Schütte's broader book as the identical presentation.

### Wansing fragment/full-source boundary — accepted

- The sheet title and scope say it is only the worked-derivation fragment and
  not the complete calculus carrying the metatheorems:
  `handbook/registry/calculi/display-k-wansing.tex:1-5`.
- The example uses exactly three printed rules and expressly denies that it is
  a K-axiom derivation or adequacy proof at
  `handbook/parts/p07/structural-extensions.tex:178-197`.
- The separate cited theorem is explicitly about Wansing's **full** display K
  calculus and says the fragment does not inherit that theorem as a standalone
  calculus at lines `220-225`.  The A-071 catalog makes the same split at
  `handbook/parts/p07/calculi-and-derivability-supplement.tex:283-288`.

### Phase-6 A-074 — external, not inflated

`spec/registers/apparatus.csv:75` assigns A-074 to Phase 6.  The local Part VII
ordinal table calls itself input to, not a substitute for, the separate master
table at `handbook/parts/p07/arithmetic-proof-theory-supplement.tex:273-317`.
It therefore creates no present completion overclaim.  A-074 remains future
apparatus work outside this source/content verdict.

## Evidence boundary

No test, static checker, TeX/PDF build, auxiliary-file inspection, hyperlink
resolution check, bibliography render, float/longtable/landscape inspection,
or visual review was run.  Administrative, provenance, build, reference,
visual, human, and final-user gates remain external.  This verdict accepts only
the current Part VII source/content and publication-status surfaces reviewed
above.

ACCEPT

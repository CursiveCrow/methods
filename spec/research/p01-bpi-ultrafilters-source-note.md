# P1 BPI, ultrafilters and propositional compactness: finite authoring record

## Scope fixed before authoring

Assignment: P1 current-fulfillment sections 3.7 and 3.8; the finite common
mathematical omission, not a whole-book source replacement. The exact
`completion-work-queue.jsonl` records read are ED26-REQ-D-P1-005-01 and
ED26-REQ-S-005-01. D-P1-005-C01 and GOAL-01/02/03 require the definitions,
both directions over the stated set-theoretic base, and separation from the
countable choice-free route. S-005-C01/02/03/04 separately require the scope,
historical citation and original-entry theorem routing. The writer owns no
shared routing file or inherited source capture; the original-entry routing
requirement remains with the integrator.

Finite proof dependencies frozen here: elementary Boolean-algebra identities;
finite meets/joins and generated filters; ultrafilter decision, prime ideals
and two-valued homomorphisms; quotient congruence by symmetric difference;
finite partitions of a finitely generated Boolean algebra; bare prime-ideal
existence, ideal/filter extension and the set-ultrafilter principle; both
directions of arbitrary-set-variable propositional compactness; the Zorn
application under AC; finite-set principal and infinite-set cofinite
boundaries. All algebraic equivalences use ZF. The historical independence
construction is not one of the supplied elementary proofs.

## Primary manifestation and complete finite reading

Sabine Koppelberg, *Handbook of Boolean Algebras*, Volume 1, North-Holland,
1989, held author-hosted scan:
`tmp/acquisition/boolean-algebras-volumes/016-monk-author-volume-1.pdf`.
The local acquisition manifest records [the editor's offered PDF](https://math.colorado.edu/~monkd/monk47.pdf),
HTTP 200, 25,551,014 bytes, and SHA-256
`32A58C77746BE240533ECF7C1D9E0FAC37237CB117B853D1DD3136E886ECC8CA`.
The current file hash agrees. It contains 344 physical pages. Title and
copyright pages identify Koppelberg, volume 1, and 1989; no different printing
is silently substituted.

Complete connected finite sections read visually on 2 October 2026:

- Section 2.2, printed pp.31–34 (physical pp.50–53), from its heading to the
  next section heading. Definitions/Lemmas 2.10–2.15 fix filters, finite
  intersection property, ultrafilter/prime/maximal equivalence and the
  characteristic homomorphism. Proposition 2.16 proves extension using Zorn;
  p33 explicitly distinguishes BPI from full AC. The Stone representation
  proof at the end of this section is read for context, not assumed by the
  new ZF equivalence construction.
- Section 5.4, printed pp.74–78 (physical pp.93–97), from its heading to
  section 5.5. Definitions/Lemmas 5.17–5.22 supply congruence, ideals,
  duality, kernels and symmetric-difference quotients; Proposition 5.23 and
  Examples 5.24–5.25 finish the section. No preceding Vaught-isomorphism
  proof or following whole quotient chapter is credited by this finite read.

The author scan has no usable text layer on these pages. Source-only page
images were read to resolve the actual published notation. Koppelberg writes
product, sum and minus for Boolean meet, join and complement; the new body
declares these roles and gives a notation dictionary rather than identifying
them with numerical operations. Its reconstructed proofs are independently
worded common editorial proofs, not a claimed full reproduction of either
source section or of the volume.

## Independence-source ceiling

The historical record is Halpern and Lévy, 1971, *Axiomatic Set Theory*,
PSPM XIII, Part I, pp.83–134, MR0284328. The existing
`spec/research/p01-ultrafilter-lemma.md` records the conditional
`Con(ZF) -> Con(ZF+BPI+not AC)`. That note is not a verified held primary
body. This block did not find a Jech, Howard–Rubin or Halpern–Lévy body in the
bounded held-file search. The AMS original record returned 403 and the
Google Books original-page route was inaccessible through web retrieval.
No independence proof or fresh original-paper reading is credited.

A distinct later primary paper is Miroslav Repický, 2015,
*A proof of the independence of the Axiom of Choice from the Boolean Prime
Ideal Theorem*, *Commentationes Mathematicae Universitatis Carolinae* 56(4),
543–546, DOI 10.14712/1213-7243.2015.138, [publisher/library record](https://dml.cz/handle/10338.dmlcz/144758).
The offered five-page PDF has one library rights wrapper plus all four
article pages, including complete proofs and references. All article text,
displayed formulas, qualifications and references were read in the offered
PDF. It assumes a ZFC ground universe and generic extension, imports the
ZF/AC-failure properties of the symmetric model from Jech, and proves BPI
there using a continuity lemma. It is not the 1971 manifestation and does
not by itself supply all dependencies of an independence proof in this
treatment. A cited model formulation will retain that hypothesis and the
historical theorem will retain its distinct cited-only standing.
The ordinary approved TLS download was retained at
`C:/Users/Crow/Documents/Codex/2026-08-10/phase-4-handover-migration-campaign-written/bpi-repicky-2015.pdf`,
187,602 bytes, SHA-256
`5FD40A15A12D92638571B01953AEC2F969DDB5D8A71657DB6B7D5A7CBC9554A8`.
This permitted work-area copy is not represented as an owned project
source-reference migration or as the historical original. Root may retain
it at an approved source destination separately.

## Delivery record

The new body is `handbook/parts/p01/boolean-prime-ideal-and-ultrafilters.tex`;
its section anchor is `sec:p01-boolean-prime-ideal-and-ultrafilters`.
The seven full reciprocal proof pairs use the same suffix after `thm:` and
`annex:`: `p01-bpi-duality`, `p01-bpi-quotient`, `p01-bpi-finite-local`,
`p01-bpi-equivalence`, `p01-bpi-propositional-compactness`,
`p01-bpi-ac-implication`, and `p01-bpi-set-boundaries`.
The exact complete counterpart file is
`handbook/annex/p01/boolean-prime-ideal-and-ultrafilters.tex`.
`thm:p01-bpi-choice-separation` has `cited=HalpernLevy1971` and no annex
target, since no independence construction is supplied here.

Finite component standing after this authoring block:

| Component | Supplied standing and bounded residual |
| --- | --- |
| D-P1-005-GOAL-01 | Complete definitions of bare BPI, prescribed Boolean ideal/filter extension, arbitrary-set UL and arbitrary-variable finitary compactness; empty/degenerate cases explicit. |
| D-P1-005-GOAL-02 | Complete ZF equivalence constructions in the seven proof pairs, including both compactness directions; no cited maximality principle enters these equivalence proofs. |
| D-P1-005-GOAL-03 | Explicit separation from the fixed enumerable-variable binary-tree route; no proof of that already separate route is newly claimed. |
| D-P1-005-C01 | Its finite authoring goals are supplied; root routing and later independent admission are not supplied by an author record. |
| S-005-C01 | Original semantic scope retained; extension formulations and algebraic/object-language types distinguished. |
| S-005-C02 | Historical citation and conditional calibration retained at cited-only standing; original paper acquisition and model-construction proof remain unsupplied. |
| S-005-C03/04 | New labelled statused mathematical results and cited separation are available, but their connection at the protected original entry is an integrator-owned routing task. No edit of that inherited entry was made. |
| P1 ledger 3.7/3.8 | Elementary equivalence omission supplied. The relative non-implication construction remains a separate unsupplied component; this block does not close the whole ledger rows. |

The only new bibliography key is `Repicky2015BPI`; canonical
`Koppelberg1989` and `HalpernLevy1971` are reused without editing shared
metadata. The symbol intake has seven fields and distinguishes source
product/sum/minus, the explicitly quoted source congruence glyph, algebraic
operations, propositional operations, ideal-parameterized quotient
congruence and metatheoretic consistency. Named scopes are
`p01-bpi-principles`, `p01-bpi-algebra`, `p01-bpi-source-dictionary`,
`p01-bpi-propositional`, and `p01-bpi-choice-strength`; root owns exact
scope binding and canonical intake merging.

Every line of the new body, annex and intakes was read back in this author
context. That is authoring inspection, not an independent proof review or
admission. No review, prose test, static suite, build or manuscript render
was run. Shared drivers, canonical bibliography/registry, other authors'
files, prior releases and the ledger were left unchanged. The source-read
record is finite: neither whole Koppelberg volume coverage nor original
Halpern–Lévy proof coverage is claimed. Exact final artifact hashes are
reported on handoff; the source-note hash is external to avoid a self-hash
cycle.

Frozen pre-adoption authored artifact SHA-256 values:

| Artifact | SHA-256 |
| --- | --- |
| `handbook/parts/p01/boolean-prime-ideal-and-ultrafilters.tex` | `BD0FFF6E9AAC3DE2DB6CDAF007FD21D163F8E165137136F7CA24BDCB6A8B1566` |
| `handbook/annex/p01/boolean-prime-ideal-and-ultrafilters.tex` | `8C08D560D4B2D6BF3D8726B97A1134E36482BBB2DF5A9EE0C5A89828AC62E393` |
| `handbook/bib/intake-p01-bpi-ultrafilters.bib` | `88622F2268387BB537EDDD77349B6D327AD405B6F7E73C2A7F3056860D374A72` |
| `handbook/registry/symbols-intake-p01-bpi-ultrafilters.csv` | `263681A042025393B337624D754413B03A00412744018F661B9FBD6F12B3DB0D` |

## Author-side adoption preparation, 2 October 2026

The complete current body and all 436 annex lines were reread with the
original P1 ordered-pair/product, relation/function, ordinal/Choice,
ultrafilter and finite-string contexts. The integrator-selected physical
body seam is after `restoration/inherited-00773-00789.tex` and before
`restoration/inherited-00790-00797.tex` (the original dependency summary).
The treatment is section-level inside the existing source chapter; its
four internal headings are subsections. All mathematical text, labels,
source comparisons and seven proof pairs are retained. Local references
to "this chapter" now say "this treatment". Planned fulfillment identities
3.7/3.8 do not force a new independent chapter or literal reader number.

The fixed enumerable-variable route points to the actual live chapter
`sec:p06-cardinals-choice` in
`handbook/parts/p06/cardinals-choice-supplement.tex`; the local link now
uses `cref` rather than calling this target a section. Its proved
`thm:p06-ac-to-zorn` is the stated Choice-branch prerequisite. That
dependency is not used by the elementary ZF equivalence proofs.
The live P2 `thm:p02-arbitrary-prop-compactness-bpi`, in
`handbook/parts/p02/propositional-metatheory-supplement.tex`, remains a
cited presentation; the new full two-direction proof does not silently
change that original result's status or promise its own annex to it.

The 28-row unique symbol intake retains the exact source glyphs, roles,
named scopes and first-use anchors. Blank required macro cells were filled
from the unchanged displayed expressions; no source notation was renamed
and no canonical row or scope was edited. Both unique bibliography intakes
and both proof annexes remain unchanged. The Halpern--Levy separation is
still cited-only, conditional on the stated consistency hypothesis, with
no new independence proof or primary-body qualification.

Root must add the body input at this seam and a single input to the new
live `handbook/annex/p01-route.tex`, merge the unique intake and bind its
actual body/annex anchors. The historical off-route P1 annex must not be
duplicated into that route. No shared driver, inherited body, canonical
metadata, baseline or other packet was changed. This is relocation and
metadata preparation, not independent content review, acceptance, a test,
a build or a manuscript render. Post-adoption hashes are supplied on
handoff, separately from the pre-adoption snapshot above.

Release standing: authoring files are released to the integrator for routing,
scope binding and later consolidated verification. This is not mathematical
or publication admission. Stop this authoring block after the handoff; do
not silently reopen the original-source search or modify shared files.

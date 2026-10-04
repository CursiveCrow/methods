# Q-resolution and quantified certificates: authoring scope

Date: 3 October 2026 local. Edition source cutoff: 7 September 2026.
Standing: authored logical construction, not independently reviewed/admitted,
built, rendered or executed as a checker. One source/scope note only; no
coverage ledger, receipt, queue or driver was edited.

## Exact current scope and prerequisites

The exact current-fulfillment row 249.2, “QBF calculi, algorithms and proof
systems”, was read by stream filter. Its actual frozen facets are
`ED26-REQ-D-P11-009-01` and SRC-051 chapters 21, 23, 24, 25, 27, 28, 29,
30, 31 and 32. The QBF-specific original chapter identities are:

- `ED26-SRC-051-0029`: Kleine-Büning/Bubeck, Theory of Quantified Boolean
  Formulas, 2021, frozen pp. 1131–1156.
- `ED26-SRC-051-0030`: Giunchiglia/Marin/Narizzano, Reasoning with
  Quantified Boolean Formulas, 2021, frozen pp. 1157–1186.
- `ED26-SRC-051-0031`: Beyersdorff/Janota/Lonsing/Seidl, Quantified Boolean
  Formulas, 2021, frozen pp. 1187–1221.

These records were stream-filtered and read, not rebaselined. No separate
KBKF1995 unit is a facet of that row; it is the historical original cited
by the actual held Q-Res presentation, not an invented fulfilled frozen
source allocation. The broad adjacent design/MaxSAT/counting/nonclausal/PB/
modal chapters are not discharged by this packet.

Read actual current prerequisites: P4 complexity.tex's complete QBF language
definitions and result statements; the entire TQBF PSPACE proof at
`annex:p9.tqbf.1` in annex/p09/proofs.tex; the source-specific QBF/language/
reachability passages in p09/presentations/n-c-026.tex; current P12 SAT/QBF
boundary; and existing propositional/extended-resolution sheets. The book
already proves TQBF membership and hardness, so this packet does not duplicate
or replace that proof. It supplies a separate PCNF clause certificate calculus.

## Actual primary captures and read extents

1. `source/references/p12-q-resolution/beyersdorff-janota-lonsing-seidl-2021-07-22-author.pdf`.
   SHA-256 `DD2DDFA93F719A91F574E1062C34BDDF26B5642786A28D04BF37717BAA5D1834`.
   [Author manuscript on Jena's institutional site](https://www.fmi.uni-jena.de/fmi_femedia/39149/qbf-proofs.pdf).
   Actual PDF info: 50 pages, pdfTeX creation/modification 22 July 2021;
   printed stamp 2021/7/22, 16:59. It simultaneously retains “IOS Press,
   2008”, 2008 copyright boilerplate, chapter number 2 and placeholder
   cross-references. Those details are not normalized into a final-publication
   identity. Actual reading: pp. 1–9, including §2.2 strategy semantics,
   §2.3.1 Fig. 2.1 common Q-Res and Example 2.3.1, §2.3.2 variant guards
   and Example 2.3.2, dependency discussion, and the start of QCDCL.
   Pages 2–5 were reread separately after display truncation, preserving
   literal/complement and order side conditions. No source pages were rendered.
   Later full solving, expansion, QRAT, strategy-extraction and proof-complexity
   sections remain unread/unreconstructed here.
2. `source/references/p12-q-resolution/janota-marques-silva-2013-eccc97.pdf`.
   SHA-256 `F154DE296883C89BC3D1631BB51EF42F7763277B15E6FC3BFCBB21600B8AE5AB`.
   [ECCC Report 97 (2013) primary](https://eccc.weizmann.ac.il/report/2013/097/download/).
   Sixteen-page captured report. Actual bounded reading: introduction,
   preliminaries pp. 1–2 and beginning of expansion pp. 2–3; p. 2 reread
   locally. Only the stated already-fully-reduced-input, blocked-universal,
   non-tautological-resolvent and full-reduction convention is invoked.
   The source's whole expansion calculus and comparisons are not credited.

Original historical identity: Kleine Büning/Karpinski/Flögel, Resolution for
Quantified Boolean Formulas, Information and Computation 117(1), 1995,
pp. 12–18, DOI 10.1006/inco.1995.1025. Publisher metadata/abstract identify
it, and the publisher author index labels it open archive. The ordinary
publisher PDF route nevertheless returned a content/Cloudflare error and
no PDF capture. Author/institutional-route searches did not supply the
original body within this block. No access-control bypass, purchase or
original-proof reading is claimed. In particular the actual 2021 common
variant is not passed off as a reconstruction of the unheld 1995 text or
its Horn/extended-Horn results.

The frozen ch31 page range begins at 1187, whereas public bibliographic
results for the final chapter begin at 1177 and list 45 pages. This is a
root-owned identity/reconciliation question, not permission to silently
change the queue or equate the 50-page manuscript to the final chapter.
Neither final ch29 nor ch30 body was acquired in this block.

## Delivered mathematical construction

Reader: `handbook/parts/p12/q-resolution-and-quantified-certificates.tex`,
main anchor `sec:p12-q-resolution-and-quantified-certificates`. Annex: the
matching file under handbook/annex/p12. Native rule sheet:
`handbook/registry/calculi/p12-q-resolution.tex`, with the three Fig. 2.1
tags cl-init/red/res. Every guard is retained: non-tautological input/parent/
resolvent, existential pivot, pivot-complement exclusions, and every
existential remainder literal earlier than the reduced universal. Source
figure spelling vars(Pi) is locally declared rather than house-renamed.

Six complete reciprocal proof pairs (all `thm:p12-qres-...` /
`annex:p12-qres-...`):

1. game-strategies: finite backward game evaluation, exactly one winner,
   own-history compression into permitted preceding-opponent dependencies,
   total table construction and empty-prefix/opponent cases.
2. rule-soundness: all native rules preserve winning existential strategies;
   reduction changes only the universal value and leaves relevant functions
   invariant; tautology/pivot/identity cases; induction to refutation and
   explicit-length finite polynomial syntactic-checking bound.
3. elimination-step: exact innermost existential pair elimination and
   universal clause-wise elimination, for every earlier valuation; empty
   families/remainders, tautological omission and true/false boundaries.
4. completeness: finite right-to-left construction, original-prefix rule
   legality, earlier record IDs, working-matrix truth invariant, zero-variable
   and early-empty cases; no small proof-size or heuristic liveness claim.
5. strategy-checking: exhaustive opponent-vector checking exactly matches
   all legal game plays, including dependent opponents; finite acceptance
   is precisely winning, not a succinct-circuit or efficient-extraction claim.
6. normalized-bridge: full reduction expands into individual legal steps;
   exactly the same winning strategy sets before/after input normalization;
   normalized elimination gives refutational completeness; no literal
   equality of every intermediate clause or whole-source identity claim.

The source's blocked-then-legal reduction Example 2.3.1 is worked using
its own x_1/x_2/x_3/x_4/y_5 variables. It is explicitly identified as a
derivation in a true formula, not a refutation. The independently constructed
alternating false example has prefix exists a forall u exists b, nine checked
records and legal universal counterstrategy u(a)=a. Its propositional matrix
is SAT, making the distinction from ordinary SAT proof explicit. Source
Example 2.3.2 has its actual winning y(x)=x strategy, both illegal universal
reductions, and the rejected tautological resolvent. Reversing the prefix
gives a concrete forbidden-future-dependency strategy countercase.

The full elimination proofs and finite table constructors are independently
worded mathematical completions for the declared source rule set. They are
not misattributed as literal code or a supplied algorithm from the unheld
1995 paper. Later long-distance/QU/dependency/cube/expansion/QRAT systems
keep their distinct syntax and duties.

Bibliography intake: `handbook/bib/intake-p12-q-resolution.bib`, two held
manifestation keys, no fabricated original-source body/stub. Symbol intake:
`handbook/registry/symbols-intake-p12-q-resolution.csv`, actual local typed
roles, no new style macros. Root owns canonical merges, scope maps, drivers,
coverage disposition and receipts. Suggested seam: the new QBF chapter after
the existing SAT representation/search material, before DRAT/other certificate
chapters; rule sheet is already input locally by the new reader file, and
annex belongs with that file's proof group.

## Verification and remaining full scope

Author mathematical rereading, source-text comparison and direct tracing
of the nine-record certificate/counterstrategies are not independent review.
No children, reviewers, software test, proof checker, build, source/manuscript
render, installation, generated file, ledger or receipt was run/edited.

The common finite-PCNF construction and full declared proofs are authored.
Original KBKF1995 body and its additional unit/Horn claims, final 2021
chapter identities/manifestations and whole ch29/ch30/ch31 treatments,
native QCDCL/cube algorithms, normal-form translations, later calculus
adequacy/comparison results, efficient strategy extraction and the other
249.2 facets remain separate duties. No unheld or unread original is marked
fulfilled. Consolidated independent source/topic/publication admission and
later static/build/visual checks remain pending. The nineteen-part,
289-chapter, 2,475-section, 615-original-requirement goal remains owed.

# Klop 1987 CWI tutorial: bounded source-specific authoring record

Authoring blocks 1--9: 2 October 2026. Unit `ED26-SRC-027-501`; source `SRC-027`,
CWI Note CS-N8701, May 1987. This is an authoring record, not admission,
independent review, release, or a claim that the full source unit is complete.

## Authority and read qualification

Read `handbook/CONVENTIONS.md`, `spec/EDITION-2026-CONTRACT.md`, and
`spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md` in full. Read candidate 5 in
`work/next-formal-authoring-units.md` and the actual full JSONL queue record at
`spec/coverage/edition-2026/completion-work-queue.jsonl:2194`, including all
five components and their entire-42-physical-page allocations. The present
body and annex are owned disjoint new files; hosts, part/annex drivers,
style, canonical bibliography, canonical symbols and generated files are
lead-owned and unchanged by this writer.

Primary held body:

- `tmp/acquisition/src027/cwi-klop.pdf`, SHA-256
  `F0103746292B130E47C2D02FE1192ABED2E33967AE0F952B87ED369C7E341543`.
- `citations/Klop - Term Rewriting Systems - A Tutorial (1987, CWI Note CS-N8701).pdf`,
  SHA-256 `39EBB6329C46B0A9B4E545467E9B7464BD7B602ABC7F26F27FEA6324FF9DDB5F`.
- Readable full extraction `tmp/acquisition/src027/cwi-klop.txt` was read
  through its cover/title/abstract, introduction, all six sections, both
  puzzle answers and all references. It is an extraction of the actual
  held report, not an abstract substituted for its body.
- `pypdf` confirmed 42 physical pages. Printed page `n` is physical page
  `n+4`, for `1 <= n <= 37`. Physical page 4 and 42 are blank.
- Ambiguous mathematical/graphical source passages were rendered with
  the bundled `pypdfium2` runtime and actually inspected at printed pages
  4, 5, 6, 7, 8, 11, 13, 14, 15, 16, 19, 20, 21, 22, 24, 25, 29, 30,
  31, 32, 33, 34 and 35. All 23 source-page PNGs and the reproducible
  source-only renderer are under `source/references/p12-klop1987/`.
  They are source-reading aids, not manuscript pages or final figures.
  No claim is made that every physical source page was independently
  visually reviewed; the full textual extent was read and the graphical
  mathematical passages listed here were additionally inspected.

Supplemental proof dependency, not a replacement source/version:

- The 1987 report explicitly cites Bergstra--Klop (1986)'s appendix for
  parallel-outermost normalization. Acquired the freely served institutional
  [CWI PDF](https://ir.cwi.nl/pub/1781/1781D.pdf) into
  `source/references/p12-klop1987/bergstra-klop1986.pdf`, SHA-256
  `B866DEB58156BB961EF3BA184F3C2C1119BBF03767C4B73E2057007723D366EF`.
- Printed title: *Conditional Rewrite Rules: Confluence and Termination*,
  J. A. Bergstra and J. W. Klop, JCSS 32 (1986), pp.323-362; 40 physical pages.
- Read residual preliminaries pp.330-332 and appendix pp.352-360,
  including the bound-variable context as a boundary. Rendered and
  inspected pp.330,331,332,353,354,355,356,357,359,360. The page 352
  render is retained; textual reading covers it. The extraction includes
  p.358, but that CRS-specific argument is not imported.
- Only the **ordinary first-order regular-TRS** residual and strategy
  specialization is used. No conditional rule, oracle, bound-variable
  system, weakly regular extension or later 1992 chapter replaces the
  1987 tutorial's hypotheses. The supplementary paper as a whole was not
  allocated or claimed fully reconstructed.

The report says it will appear in Bulletin of the EATCS 32 (1987).
Its own abstract explicitly excludes conditional and equational TRSs.
The separately retained publisher abstract in
`spec/research/acquisition-src-027.md:63` includes E-unification,
strongly sequential orthogonal TRSs and conditional TRSs in the 1992
chapter. This is evidence of a substantive version boundary, not a full
correspondence with the later chapter. No publisher-body equivalence or
page-by-page variant comparison has been established by this writer.

## Authored artifacts and exact standing

- Body: `handbook/parts/p12/sources/src-027-501.tex`, stable entry
  `sec:p12-src-027-501`.
- **Active reciprocal annex:** `handbook/annex/p12/sources/src-027-501.tex`,
  the exact queue-mapped destination. The second-block instruction corrected
  the first-block path discrepancy; the lead routes only this active file.
- **Historical first-block annex, preserved unchanged:**
  `handbook/annex/p12/src-027-501.tex`, SHA-256
  `3CD4C49F482C76E737AB9FA0263DA5AF10A7AB7B7EBCE4983D4345FBC39AB888`.
  Do not route both copies: their seven original proof labels intentionally
  coincide. The historical copy has not been deleted or made a second unit.
- Unique bibliography intake `handbook/bib/intake-p12-klop1987.bib`,
  keys `Klop1987CWITutorial` and `BergstraKlop1986StrategyAppendix`;
  no existing source key was relabelled.
- Unique symbol intake `handbook/registry/symbols-intake-p12-klop1987.csv`.
- Source reading references `source/references/p12-klop1987/`.

The body supplies an independently worded six-section source route, rather
than an unlabelled substitution of the current host's ordinary critical-pair,
LPO/KBO or fair-completion accounts. It preserves the report's language,
double-arrow and conversion conventions; WN/SN/UN/NF/Ind/Inc/FB distinctions;
all seventeen separate ARS exercise surfaces, with the invalid 16th
termination request directly corrected rather than assigned as a false theorem;
open versus ground terms versus ground rules; applicative signature distinctions;
the particular arithmetic, string, CL/SKIM, categorical-combinator, direct-sum,
marked-order, group-completion, regular-system and strategy examples.

Twenty-two full editorial proof items have reciprocal body/active-annex bindings:

| Body result | Annex proof | Actual argument supplied |
| --- | --- | --- |
| `thm:p12-klop1987-ars-core` | `annex:p12-klop1987-ars-core` | conversion joinability, CR/NF/UN, WN+UN, Ind+Inc, and countable CR/CP; countability used explicitly |
| `thm:p12-klop1987-semantic-un` | `annex:p12-klop1987-semantic-un` | soundness under every assignment/context and separation of normal forms |
| `thm:p12-klop1987-one-rule-puzzle` | `annex:p12-klop1987-one-rule-puzzle` | Akkerman's self-loop and structural normal-form-existence argument for every finite term |
| `thm:p12-klop1987-regular-confluence` | `annex:p12-klop1987-regular-confluence` | exhaustive parallel diamond cases, including variable-instance duplication/erasure and finite grid |
| `thm:p12-klop1987-cofinal-normalizing` | `annex:p12-klop1987-cofinal-normalizing` | cofinal orbit overtakes a normal form and irreducibility forces its occurrence |
| `thm:p12-klop1987-developments` | `annex:p12-klop1987-developments` | residual origin labels, lexicographic termination measure, canonical outcome and invariance |
| `thm:p12-klop1987-ne-normalization` | `annex:p12-klop1987-ne-normalization` | projection of an infinite reduction through a non-erasing step; finite developments exclude an infinite cancellation tail; local WN/SN |
| `thm:p12-klop1987-win-normalization` | `annex:p12-klop1987-win-normalization` | innermost residuals retain normal proper subterms; the disappearing inner-projection case cannot occur; local WIN/SN without NE |
| `thm:p12-klop1987-fair-cofinal` | `annex:p12-klop1987-fair-cofinal` | finitely branching residual forest gives finite elimination of each original redex; projections share eventual literal tails; full-substitution complete rounds are fair and cofinal |
| `thm:p12-klop1987-omega` | `annex:p12-klop1987-omega` | exhaustive auxiliary macro-code closure keeps normal subterm S(SKI)(SKI) in every reduct of Omega_I; Omega_II lacks it; exact parallel period and noncofinality |
| `thm:p12-klop1987-outermost-projection` | `annex:p12-klop1987-outermost-projection` | non-outermost creation boundary, commuting-cell trace exchange, disjoint selected-label staircase and finitely branching trace contradiction; infinite outermost steps cannot all project empty |
| `thm:p12-klop1987-strategy-results` | `annex:p12-klop1987-strategy-results` | parallel-outermost projection contradiction at a finite normal endpoint; separate direct left-normal leftmost projection; all negative/cofinality columns, including growing leftmost Omega orbit |
| `thm:p12-klop1987-leftmost-needed` | `annex:p12-klop1987-leftmost-needed` | left-normal position persistence shows every normalizing reduction must contract the initial leftmost residual; effective selector only in that exact regime |
| `thm:p12-klop1987-ars-commutation` | `annex:p12-klop1987-ars-commutation` | exercises1-4/10: bounded finite strips, strong confluence, subcommutativity, closure transport and arbitrary indexed commuting unions |
| `thm:p12-klop1987-ars-request` | `annex:p12-klop1987-ars-request` | exercises5/7: the full finite-arm requesting property makes the two-block relation diamond, including the weaker composite-joining premise of7 |
| `thm:p12-klop1987-ars-refinement` | `annex:p12-klop1987-ars-refinement` | exercises8/9: compatibility for every finite2-path, reverse propagation of a1-endpoint, confluence preservation/reflection; explicit countercase to single-step weakening |
| `thm:p12-klop1987-ars-splitting` | `annex:p12-klop1987-ars-splitting` | exercise11: finite input-colour partition into relatively terminating splitting colours and strongly commuting nonsplitting colours, followed by finite-strip/Hindley union argument |
| `thm:p12-klop1987-ars-decreasing` | `annex:p12-klop1987-ars-decreasing` | exercise12: well-founded induction joins each entire below-source conversion and then arbitrary finite peaks |
| `thm:p12-klop1987-ars-boundaries` | `annex:p12-klop1987-ars-boundaries` | exercises14/17 and source1.4: consistency, conservative successor-closed extensions, ten-property inheritance, genuine-step lifting through the retraction |
| `thm:p12-klop1987-ars-normalization` | `annex:p12-klop1987-ars-normalization` | exercise15 and theorem1.6vi/Figure2: strict nontrivial diamond reduction-length bound, WCR/WN/Inc bounded-rank argument, inverse finite-branching height construction |
| `thm:p12-klop1987-ars-countercases` | `annex:p12-klop1987-ars-countercases` | complete finite countermodels for local-request6, quasi-commutation16, and at-most-one-step-diamond/WN not implyingSN |
| `thm:p12-klop1987-group-completion` | `annex:p12-klop1987-group-completion` | every source temporary peak4-15, exact ten-rule LPO comparisons, all65 unifiable overlap locations and all50 nontrivial joining paths, equational congruence and word-problem argument |

These are authored proofs, not independent specialist acceptance. The finite
development proof by itself establishes well-defined full substitution;
the separate fair/cofinal proof now establishes cofinality. The regular diamond proof establishes the orthogonal case,
**not** Huet's broader parallel critical-pair condition. The former host
proofs remain prerequisite comparisons only where their exact hypotheses
are expressly matched in the text.

The strategy theorem is not inferred from termination of arbitrary reductions.
Its projection proof allows empty erasing segments, proves when the projected
infinite run remains infinite, and separates full fairness from outermost
fairness. The leftmost proof uses the precise left-normal operator-before-variable
condition to keep a leftmost residual leftmost under every different step.
The needed-redex lemma is confined to that effective left-normal regime;
it does not close the report's general strongly sequential development.

Third-block original-source reading: reread printed ARS pp.6-8 as images,
including high-resolution details for exercises5-8; their doubled arrows
control the finite-reduction scope. These reading aids are retained as
`ars-ex5-7-source-detail.png` and `ars-ex8-source-detail.png`.

Third-block direct mathematical recomputation:

- `group-completion-evidence.py` enumerates the actual source Table12 ten
  rules, with disjoint variable renaming and finite-tree occurs-check
  unification at all nonvariable positions. It is a mathematical computation,
  not a mirrored prose-test suite or an admission check.
- The ten left sides have22 nonvariable positions, giving220 ordered
  rule/position candidates.65 unify;15 yield identical endpoints;
  all50 remaining pairs join, with at most4 total steps across their
  two computed traces. Every actual joining path and all65 locations are
  printed in the active annex, not replaced by an external pointer.
- `group-critical-pairs.json` retains all50 concrete peaks/endpoints/traces;
  `group-overlap-locations.json` retains all65 locations including the
  trivial cases. No proper overlap was discarded as redundant.
- The actual proof uses the finite-signature LPO definition and theorem
  `def:p12-ro-lpo`, `thm:p12-ro-lpo-structural`,
  `thm:p12-ro-lpo-termination`, with exact signature e/I/product,
  precedence I>product>e and left-to-right status. It uses the ordinary
  critical-pair theorem `thm:p12-critical-pair` at its nonlinear,
  unconditional finite-term scope. It explicitly checks the rules and
  all pairs, rather than granting source credit from matching names.
  This does not discharge the original marked-tree or lexicographic-marker
  proof routes of section3.

## Source corrections and reconstruction qualifications

1. **Section 5.6(ii), printed p.31.** The report calls both equality-test
   extensions regular. Definition 5.1 on pp.28-29 excludes their repeated
   variables. Table 7's classification also contradicts the report's
   p.16 nonconfluence statement and regular-confluence theorem. The active
   body directly classifies neither extension as regular; binary-test
   confluence has the separate disjoint-sum route. Correction provenance is
   retained here rather than making readers repair an earlier active claim.
2. **Proposition 3.9(ii), printed p.20.** Embedding is reflexive, but the
   printed implication uses positive reduction. At `s=t` this would assert
   a positive self-cycle, contradicting 3.9(i). The body distinguishes
   proper embedding from identity/reflexive reduction, rather than using
   the false positive assertion.
3. **Exercise 1.7(16), printed p.8.** The source's quasi-commutation premise
   does not imply its printed equivalence of termination of alpha and beta.
   A one-element alpha self-loop and empty beta satisfy the premise
   vacuously and refute the conclusion. The active exercise now states the
   correct nonimplication and this counterexample. No conjectural
   replacement theorem is attributed to Bachmair--Dershowitz.
4. **Figure 2, printed p.5.** CR alone does not imply consistency; a
   one-element ARS is confluent and all its pairs are convertible.
   Exercise 1.7(14)'s two-distinct-normal-forms hypothesis supplies the
   meaningful consistency implication and is kept visible.
5. **Temporary rule 13, printed p.25.** Mismatched parentheses/extra nesting
   in the printed line are resolved by its explicitly preceding critical
   pair to the well-formed `x.(y.I(x.y)) -> e`. The final Table 12 does not
   retain this temporary rule.
6. **Table 13, printed p.28.** Adding the new overlap critical pairs
   precedes deletion of old reducible left sides. The old/new overlap
   equation preserves a deleted rule's equality together with the new
   reduction. An initial authoring diagnosis that the table necessarily
   loses that equation was incorrect and was removed before delivery;
   no such defect is asserted in the body. The exact dependency is now
   visible; the host's explicit Collapse rule is a comparison packaging
   that dependency, not a silent replacement of Table 13. Substitution
   stability or orientation of every instance is required in addition to
   the report's stated context monotonicity for a rule-variable ordering.
7. **Table 8, printed p.15.** Equality signs are printed in the computational
   table. The body explicitly calls its left-to-right computational use
   an orientation; it does not pretend the report prints arrows there.
8. **Needed-redex final paragraph, printed p.35.** Restrict an informative
   existence claim to normalizable non-normal terms. A normal form has
   no redex, and quantification over absent normalizing reductions is not
   an informative selector theorem. The stronger sequentiality algorithm
   is not developed by this report.
9. The report's historical one-rule termination question and work-in-progress
   normal-form-language statement retain their **1987** dating. This writer
   did not infer a 2026 open status or acquire a current update.
10. **Finite fairness boundary.** Absence of an infinite trace is vacuous
    for a finite truncated run. The cofinality theorem therefore uses a
    complete fair run: an infinite fair reduction or a finite run ending
    in normal form. No finite arbitrary prefix is asserted cofinal.
11. **Two Omega runs.** A provisional second-block sentence identifying
    leftmost with sequentialization of the parallel period was wrong;
    enclosing S-redex creation changes the schedule. It was replaced at
    its active proof location by the explicit increasing sequence
    `w X_n`, `X_0=w`, `X_(n+1)=a X_n`. The parameter is never inspected,
    and the same subterm invariant proves its distinct noncofinality.
12. **Requesting and composition arrows, printed p.6.** High-resolution
    reading confirms exercise5 has two finite top arms and finite joining
    arms; exercise7's composite is `1*` followed by `2*`. Prior authoring
    used one-step2-arrows in those places. The active definitions and
    proofs now use the actual doubled arrows; this is a correction to
    the reconstruction, not an alleged source defect.
13. **Compatible refinement, printed p.6.** The source quantifies finite
    `a ->*2 b` in compatibility, not just one step. Corrected the active
    definition; supplied both directions of the stated mixed criterion,
    the confluence equivalence, and a counterexample showing why the
    prior single-step weakening is insufficient.
14. **Exercise1.7(6), printed p.6.** The literal local mixed-peak premise
    does not imply full requesting. Use four distinct a,b,c,d,
    R1={b->a,c->b}, R2={b->c,c->d}. R2 (and even R1) is terminating
    and confluent. At b the local join is a, using c->1b->1a; at c
    the local join is d, using b->2c->2d. Nevertheless b->*1a and
    b->*2d cannot join in the required full sense. The active item is
    directly corrected to this nonimplication; the complete countermodel
    proof is reciprocal. No theorem is fabricated from a local substitute
    for exercise5's full requesting hypothesis.
15. **Strict diamond, printed p.8 and source5.10.** A strict two-arm
    diagram universally applied to an equal-endpoint peak would require
    a normal form with an incoming step to have an outgoing step.
    UnderWN that literal reading permits no nontrivial reduction at all,
    and does not express the source's later nontrivial string example.
    The active strict nontrivial diamond explicitly treats distinct
    endpoints and regards identical endpoints as already joined; its
    full normalization proof retains genuine steps on both distinct arms.
    The zero-arm subcommutative version remains separately refuted.

## Component qualification: allocation has not been reduced

### Ninth-block author-side PA/Puel book adoption

Read the current full core and the affected marked-tree passages before
editing. Both PA working fragments and the single source note still
had their released eighth-block hashes. New destination files were
absent. The frozen working fragments were copied with apply_patch into
the source-mapped body and reciprocal annex; only placement comments
and ordinary line endings differ from those originals.

| Book artifact | SHA256 |
| --- | --- |
| `handbook/parts/p12/sources/src-027-501-pa.tex` | `354AAAC42524C90C6E0A6EEB9739AF240D54FA9B3DBA76B9C26249216D6713EE` |
| `handbook/annex/p12/sources/src-027-501-pa.tex` | `793FB84EBD034E04562B66801D7558C9D2EA2AED6A0327B0497461855C493864` |
| `handbook/parts/p12/sources/src-027-501.tex` | `52685D9CB1EACAC4835096F1BD588A2C04B29BC2ABD3A8AEF4D4539D2AE6A2AD` |
| `handbook/parts/p12/sources/src-027-501-marked-trees.tex` | `5FDAF7ED3E51D1BF5BFDA5EA8D59F39AA78C2139D06449412414F1B97189B89B` |

The core's section3 input order is now marked-trees, PA/Puel,
ordered-markers, then the existing completion subsection. The PA
packet's embedding comparison therefore follows its actual marked-tree
prerequisite; its two norm lifts retain the existing full LPO dependency.
The core directly qualifies the original historical symbol-length
proposal at its active passage: automatic reannotation above duplication
can raise an enclosing index4 to8, whereas the new actual three-rule
proofs use the repaired max/sum norm or retained upper budgets. This
does not call the historically accurate description false and does
not rely on a contradictory late note. The same original passage
now separates the isolated Puel-example SN proof from its companion-rule
failure and the still-unproved general unavoidable-set extension.

Changed only the final remaining-PA boundary of the existing marked-tree
body. It now points to the supplied PA proofs at their exact R3/R7
scopes and keeps larger ACP communication/silent-action variants and
general Puel outside them. The earlier valid simplified-pair caveat,
which uses node-count preservation and excludes duplication under
choice, remains unchanged. No other marked-tree body material or
its existing annex was edited.

All seven reciprocal labels retain prefix `thm:p12-klop1987-pa-` /
`annex:p12-klop1987-pa-` and suffixes `reannotation-failure`, `norm`,
`lpo-lift`, `termination`, `budget-lift`, `puel-example`,
`puel-extension-failure`. Their arguments and R3/R7 scope are unchanged:
three actual tutorial rules, an explicitly enumerated seven-rule
ordinary PA presentation, no implicit choice equations or larger ACP
rule set, and no promotion of isolated one-rule SN to arbitrary
companions or Puel's general theorem. The complete adopted body,
repaired parent passages and all seven actual annex bindings were
read back; the annex arguments were the already fully read frozen
ones, not a newly claimed independent review.

PA bibliography and eight-row symbol intakes were left unchanged at
SHA256 `98211FCCC4261745E308D65E62E884780B5A5C84A154D33EED09532AD7A95CB8`
and `58BC9C140E2B53E5C392BFFDC3701CBAF5234499E5D0F68B6FC4083D593CF006`.
At the 20:05 UTC inspection neither `BergstraKlop1984PAIndexingReport`
nor `Puel1986UnavoidableCatalogued` was yet in `handbook.bib`.
Their canonical merge, symbol integration and shared annex-driver input
for `annex/p12/sources/src-027-501-pa` remain root-owned.
No shared driver, canonical, baseline or generated file was edited.
No tests, review, build or manuscript render was run.

No new primary-reading extent or acquisition qualification is asserted
by this adoption. The held 48-page CWI report's selected read extent
and hash remain exactly as recorded in the eighth block. Puel remains
catalogue-only, with zero body pages read and no body hash. The source
unit remains partial across all five components over the full 42-page
allocation; the mathematical and source/version residuals below remain.

### Eighth-block PA norm/indexing and distinct Puel-example packet

Owned new files: `spec/fragments/p12-klop-pa-body.tex` and
`spec/fragments/p12-klop-pa-annex.tex`, plus unique
`handbook/bib/intake-p12-klop1987-pa.bib` and
`handbook/registry/symbols-intake-p12-klop1987-pa.csv`.
Adopted book files, all previous fragments/intakes, shared/canonical
files and baseline/generated material were not edited. This packet
is prepared for root adoption, not already routed or independently
accepted. The source note was still at its seventh-block hash before
this update. All five components retain the entire 42-page allocation.

Actual original reading: reread all of Remark 3.11(i)--(ii), printed
p.21, as the actual source text and newly rendered page image. This
includes the exact three PA rules, atomic-prefix notation, the desired
operator order, syntax-length indices, the simplified g/h/f pair and
the distinct embedded-left-side example. The existing complete
marked-tree and LPO comparison proofs remain the previously read
dependencies; no endpoint comparison was substituted for a context lift.

New primary body acquired by the ordinary openly linked CWI route:
[CS-R8403](https://ir.cwi.nl/pub/6543/6543D.pdf), J. A. Bergstra and
J. W. Klop, *Algebra of Communicating Processes with Abstraction*,
institutional report, January 1984, 48 physical pages. Held at
`source/references/p12-klop1987/bergstra-klop1984-abstraction-report.pdf`,
SHA256 `60700893676EDADB22446428E57900AD1163C6D25CDF4F248E4EDC490D556CDF`.
Read physical pages 1--3, 5--7 and 30--40: cover/title material,
printed pp.1--3 and 26--36. All those selected pages were rendered
as source-only PNGs; additionally inspected physical pages 7, 34,
35, 36 and 38 visually (printed3,30,31,32,34). No full reading of
all48 pages is claimed. Appendix I occupies printed26--34 and was
read through its objects, order definitions, rule set and indexing
comparisons. The later Appendix II pages35--36 were consulted,
not imported as a PA termination proof. The reproducible owned helper
`read-pa-sources.py` has SHA256
`E647E6A8D160D156E404E68A8C752073CEE1704C826FA2D5FE356C20FBAA1F18`.
This actual 1984 report is not silently identified with a byte-equivalent
1985 journal manifestation or the 1992 chapter.

The primary Table2/Appendix I actually differs from the tutorial's
PA variant: ACP CM1 has an additional communication-merge summand;
its norm sums atomic lengths across every binary operator, including
choice, whereas the tutorial calls its simplified norm syntax length.
The primary action alphabet is finite and its commutative-tree argument
excludes A5. The prepared packet explicitly separates all these variants.
The actual 1985 TCS publisher metadata gives pp.77--121; the tutorial's
reference lists pp.171--199. This is a bibliographic correction, not
evidence of a read/verified publisher-body correspondence.

Seven reciprocal items use `thm:p12-klop1987-pa-` and matching
`annex:p12-klop1987-pa-`:

- `reannotation-failure`: actual inner PA parallel expansion in
  `(a parallel b) leftmerge c` changes an enclosing fresh syntax-length
  tag from4 to8. Applying the primary additive norm to that PA variant
  changes3 to5; applying the primary's actual three-branch ACP CM1 changes
  its outer tag3 to7. Every new root exceeds all old numerical labels,
  refuting the proposed marker/LPO lift through that context, not PA SN.
- `norm`: a fully defined positive-unit-leaf max/sum norm; invariance
  for every stated rule instance, arbitrary positive substitution values,
  every ancestor, and a constructed common annotated context at equal
  hole norm. The explicit P2/P3 example refutes unjustified ordinary
  substitution-homomorphism of the annotation.
- `lpo-lift`: all seven actual instance comparisons, with every target
  child dominated. Distribution covers equal and unequal branch levels;
  the consuming prefix uses L_n greater than P_(n-1), then the product.
- `termination`: one finite ranked alphabet for an entire run, merge
  indices2 through the invariant initial normN, no new variables/actions,
  and the complete finite-ranked LPO dependency. No node-size bound or
  common global input bound is imposed.
- `budget-lift`: an additional actual lift for the exact three tutorial
  rules retaining the original initial syntax-length tags as upper bounds.
  Admissibility uses the repaired norm; distributed copies inherit n and
  a consumed atomic prefix creates P_(n-1). Surrounding tags remain literal,
  matching is justified by these three patterns' left-linearity, and no
  larger tag is born. Budgets may exceed fresh syntax/minimal norm values;
  this is an explicit completion, not repeated literal reannotation.
- `puel-example`: ordinary SN of the isolated actual displayed rule
  f(s(x)) -> g(s(x),f(p(s(x)))) with no p/s companion rule. The proof
  establishes absence of newly active f-origins, permanence of the new
  p-blocked f-node, and a fixed finite lexicographic residual-count descent.
- `puel-extension-failure`: adding p(s(x)) -> s(x) yields an explicit
  infinite two-step growing-context reduction. Thus the preceding
  isolated-system proof is not promoted to arbitrary companions.

The exact proved ordinary systems are R3 (the three printed tutorial
rules) and the fully listed R7 (also atomic left merge, idempotence,
sequential distribution and one oriented sequential associativity).
No choice commutativity/associativity equation is implicit, and no
communication/silent/deadlock/abstraction/recursion rule is added.
The source's simplified pair stays valid because it preserves node
count. The full primary ACP Table4 variants and its own complete
indexed lifting remain different obligations from this ordinary PA packet.

Puel acquisition/read qualification is deliberately exact: the issuing
[ENS report catalogue](https://www.di.ens.fr/reports/) confirms report
86-4 (1986), L. Puel, *Using Unavoidable Sets of Trees to Generalize
Kruskal's Theorem*. That old entry has no linked report body. The
author-research-group publication listing identifies the separate
December1987 thesis and1989 conference paper; neither was read as
the 1986 report. The later 1989 JSC publisher route returned403 and
was stopped without retry or bypass. No Puel primary body was acquired,
no body pages were read, and no body hash is supplied. The catalogue-only
intake records identity, not a proved extension. The general unavoidable-set
construction, exact tree relation, hypotheses and full wqo/termination
argument therefore remain owed. The isolated example proof does not
discharge them, and the packet does not rename PA as a Puel extension.

Exact root-only active passage needing qualification at adoption:
`handbook/parts/p12/sources/src-027-501.tex:541` currently says:

```tex
The process-algebra rules can reintroduce a heavier operator; the source
uses norm-indexed copies of operators, with indices determined by symbol
length of the arguments, rather than claiming the unmodified order works.
```

This is an accurate historical description, but must not be promoted
to a full contextual simulation by automatic reannotation. Replace it
coherently with the historical description plus an immediate pointer to
`thm:p12-klop1987-pa-reannotation-failure`, and the actual repairs
`thm:p12-klop1987-pa-termination`/`thm:p12-klop1987-pa-budget-lift`.
The marked-tree body's final boundary at line258 must likewise distinguish
the now supplied exact ordinary PA rules from the still distinct larger
ACP and general Puel obligations. The earlier valid node-count-pair
qualification at line203 should remain, not be erased. This writer did
not edit those root-owned active passages in this block.

Delivered hashes: PA body
`DBABC7F491313297D4DD27F28354A559C2A82611C15954E3FCCE169255AC17BD`;
annex `BB056F1605E7896AB301529729F66FD03BB8EEC88EC9329982AA3C38EF65041B`;
bibliography intake
`98211FCCC4261745E308D65E62E884780B5A5C84A154D33EED09532AD7A95CB8`;
eight-row symbol intake
`58BC9C140E2B53E5C392BFFDC3701CBAF5234499E5D0F68B6FC4083D593CF006`.
The complete body and all seven proofs were read back. No child,
independent review, tests, build, manuscript render, adopted/shared/canonical
edit, generated update or security bypass was used. The research/PDF
skills guided primary-body distinctions and the source-only reading;
the explicit no-child instruction was retained. The PA-selected
construction is supplied, but no whole-unit completion or admission follows.

### Seventh-block author-side book adoption

Read the latest full core body, full adopted marked-tree body, both
released direct-sum/ordered-marker bodies and every one of their fifteen
annex arguments before adoption. The source note was unchanged at its
sixth-block hash before this update. This block performed book adoption
and in-place coherence repairs; it did not claim a new full primary-source
reading, source-acquisition closure, independent review or admission.

Created the following book counterparts with apply_patch, preserving
all four released working originals under `spec/fragments/`:

| Adopted book file | SHA256 |
| --- | --- |
| `handbook/parts/p12/sources/src-027-501-direct-sum.tex` | `448E6AF92CC9E14C241BE7B6F996BD952D49391EFFF3D4DE13AA0F439B517386` |
| `handbook/annex/p12/sources/src-027-501-direct-sum.tex` | `5C75EBD1F866AB4EE1AF9095FC3B9A9E93632194A52ABF6C2E78FE7EB683D916` |
| `handbook/parts/p12/sources/src-027-501-ordered-markers.tex` | `E7A7FD18E7D6BDC1FC45BF9E018ED6D4D0DADCF5AEC51E2CDF95EE99BA15BAA8` |
| `handbook/annex/p12/sources/src-027-501-ordered-markers.tex` | `FE92E0A715A1EDC2717C3E094D4D6B30EFAC0D843E150E5BD95C97CAA7974C86` |

The fifteen reciprocal proof pairs retain their exact original labels:
direct-sum suffixes `invariants`, `coherence`, `preserved`, `depth`,
`diagrams`, `confluence`, `first-counter`, `complete-counter`,
`applications`; ordered-marker suffixes `bound`, `sets`, `operations`,
`first-mark`, `well-founded`, `applications`. Their theorem prefixes
are respectively `thm:p12-klop1987-ds-` and `thm:p12-klop1987-om-`,
with the same suffixes after `annex:p12-klop1987-ds-` and
`annex:p12-klop1987-om-`. The full mixed-term proof retains nonlinear
matching, duplication and collapse without SN; the ordered proof retains
all five operations, independent-copy witnesses and plain-endpoint
well-foundedness, alongside the genuine marked-universe cycle.

Core `handbook/parts/p12/sources/src-027-501.tex`, SHA256
`E93F89E9C504D1E62D0D0E741DB463BF033AE5B705810FA86F418D72F1970A2B`,
now inputs the direct-sum expansion after its original source 2.3
examples, then introduces a separate semantics/finite-decision heading
for source 2.4--2.5. It inputs the ordered-marker expansion immediately
after the existing marked-tree expansion and before source section 4.
The original modularity equivalence, both factor/loop examples and
binary-test application directly point to their actual new full proofs.
The later nonregular-equality passage also points to the direct-sum
application rather than implying a regular-confluence proof.

Changed only the final ordered-WF boundary of the adopted marked-tree
body, `handbook/parts/p12/sources/src-027-501-marked-trees.tex`, SHA256
`1A83F46E5F769F497BF388A40D8CA74E865DC9160D13054BDA485D570B158C15`.
It now directly names the separate global ordered lower-set theorem,
preserves the plain-endpoint versus marked-universe distinction, and
does not imply that the Ackermann sample path proves the global theorem.
The Puel and full process-algebra boundaries remain active.
No earlier false/open statement was left for readers to repair by
discovering a contradictory later theorem.

The canonical bibliography entry `KaminLevy1980Attempts` was actually
inspected: same authors, actual title, author-hosted URL and undated
thirteen-page manifestation as the already held scan. The adopted
ordered-marker body now cites that existing key. The assigned unique
ordered bibliography intake is now a comment-only identity crosswalk,
with no new BibTeX entry/duplicate source identity; SHA256
`E9DFBF72562DE7B9CE27CEC7C518D77E4B420EBE135D7731E7C7A5FDBDBD21D1`.
The working-fragment alias is preserved only in the frozen offroute
working original. Root still owns canonical merging. At this reading,
`Toyama1990DirectSumProof` was not yet in `handbook.bib`; its existing
assigned direct-sum intake is unchanged, SHA256
`ECD78866FB776EFE291FCFACAB8582E35F0EDFC5A14E718EAF942D469C0A4F1A`.
Its online-reading/local-hash limitation remains as recorded below.
The two symbol intakes are unchanged, direct-sum SHA256
`CBAA5AB718594B1ED9EA2D71E24ED50AC46B47BA1241BCBDE2BBD3C51C3BCE7C`,
ordered SHA256
`4313CFA599AEDEE6BA2CDB3B807AB82124AF07B95E0436423FD79354C141F26A`.

Adoption differences from the frozen originals are placement comments,
reuse of the actual canonical Kamin--Levy key, and six typographical
repairs of carriage-return-corrupted roman deletion-arrow subscripts
(three in the adopted direct-sum body, three in its adopted annex).
These repairs restore the intended `\Rightarrow_{\rm d}` notation
used by the symbol intake; no mathematical condition or proof step
was changed or shortened. Working originals were not mechanically
rewritten. The complete adopted bodies and revised core transitions
were read back, and the fifteen annex bindings/arguments were inspected.

Root-only integration remains: shared annex-driver inputs for the two
new reciprocal annex files, the Toyama citation and symbol canonical
merges, and the consolidated baseline/checks. No tests, build, manuscript
render, independent review, generated-file edit or shared-driver/canonical
write was performed. The whole unit remains partial across all five
components and the entire 42-page allocation. Current mathematical
residuals remain exactly those in the component table below.

### Sixth-block prepared ordered-marker continuation

New owned files: `spec/fragments/p12-klop-ordered-markers-body.tex` and
`spec/fragments/p12-klop-ordered-markers-annex.tex`, with unique
`handbook/bib/intake-p12-klop1987-ordered-markers.bib` and
`handbook/registry/symbols-intake-p12-klop1987-ordered-markers.csv`.
All released core, marked-tree and direct-sum files/intakes stayed frozen.
These are reader-ready integration fragments, not already routed text or
an admitted/completed source unit. The full 42-page allocation is unchanged.

Delivered SHA256 hashes:

- Ordered body: `DFC6CE9EA373E6F2A758866ED6F5841043AC1D237AE63617A9D48B751C04B0DD`.
- Ordered annex: `8EE2CCDC294B4EC02338137436112466F50552957DA60AC8B891D7C436047E9E`.
- Ordered bibliography intake:
  `60522B1419B79E3C09C4E68B560C0D3617767AB42A6CE98BDE2DB61DDE10F5F5`.
- Ordered symbol intake:
  `4313CFA599AEDEE6BA2CDB3B807AB82124AF07B95E0436423FD79354C141F26A`.

Reread the actual 1987 Notation 3.2/Definition 3.3 and Remark 3.11(iii),
including the printed p.22 image, exact fixed-arity PUSH and LEX equations,
all three Ackermann rules and the associativity example. Root marking
is defined at a plain root in 3.2; the proof does not silently permit
double or idempotent marking of an already marked root. The source's
plain labels along a context-hole path and the explicitly larger
all-marked-context auxiliary game remain distinguished.

Actual primary LPO reading: the held 13-physical-page undated handwritten
Kamin--Levy scan `tmp/pdfs/p12-reduction-orderings/kamin-levy-1980.pdf`,
title *Attempts for Generalising the Recursive Path Orderings*, conventional
1980 attribution, SHA256
`3D4DF5964AA4860BA6A04FCD5F81516B18ABD426C7A4C77943B89C25F05B440A`.
Read physical pages 1--4/handwritten pages 1--8 as the actual embedded-page
PNGs in that held evidence directory. The source covers bounded
lexicographic comparison, general path clauses, structural dependencies
and the Ackermann/associativity examples. No reading of all 13 physical
pages is claimed, nor is the scan's title/date silently equated with
the related bibliographic title *Two Generalizations*.
Author-hosted source: https://www.cs.tau.ac.il/~nachumd/term/kamin-levy80spo.pdf .
The unique new citation key `KaminLevy1980OrderedMarkers` identifies
the same primary body as existing `KaminLevy1980Attempts`; canonical
integration may reconcile those keys, not invent a second source unit.

Read the existing complete shared LPO proof annex, without editing it.
The dependency is precisely `def:p12-ro-data`, `def:p12-ro-lpo`,
`thm:p12-ro-lpo-structural`, `thm:p12-ro-finite-tree` and
`thm:p12-ro-lpo-termination`: finite ranked signature, strict total
precedence for ground totality, fixed left-to-right status, proper-subterm
and context closure, and the full finite-tree/well-foundedness proof.
The new proof actually establishes those hypotheses for a whole run:
COPY introduces only a smaller natural label, every other operation
copies/deletes existing numbers or changes only stars, and thus every
run from initial maximum M uses the same finite Sigma_M (at most M+1
symbols). No uniform global bound on input labels/arities, and no bound
on node count, depth or rewrite length, was substituted for the allocation.
The actual held shared dependency files were rehashed: LPO body
`8F4B9B86FCA13279946743163A3C43FDE5E4E4E1C67B5F0B10340549A494A894`,
annex `A190C8D39136D98E4FB27956855A1209DFD6D306353C85274C61C2D924A630CD`.
The held handwritten primary PDF's physical page count was confirmed as 13
with pypdf. The body and every annex argument were read back sequentially;
this was an author inference/source check, not an independent review.

Six new reciprocal results, prefix `thm:p12-klop1987-om-` with matching
`annex:p12-klop1987-om-`:

- `bound`: the invariant giving one finite ranked signature for every
  stage of the entire hypothetical infinite run, including newly inserted
  smaller heads not originally present.
- `sets`: structural well-definedness/nonemptiness of weak/strict lower-set
  interpretations, fresh semantic bottom, arbitrary marked-context
  inclusion monotonicity and finite coordinatewise witness maxima.
- `operations`: actual PUT/SELECT/COPY/PUSH/LEX inclusion calculations,
  including nullary inputs and zero-copy outputs, unary LEX, independent
  copy witnesses, first-argument strictness and all target-child domination.
- `first-mark`: exact principal lower sets of plain terms, strict lifting
  of the first PUT through its plain ancestor path, and strict LPO descent
  at every positive plain-to-plain endpoint.
- `well-founded`: strict/transitive global plain-endpoint relation over
  arbitrary ambient natural-labelled fixed-arity signatures, using one
  LPO throughout the run, and explicit exclusion of auxiliary marked SN.
- `applications`: all three actual source Ackermann positive paths, the
  fixed-binary associativity path, and ordinary open/ground SN through
  homomorphic variable coding and arbitrary instances/contexts.

Two important failure surfaces are supplied, not assumed away. Without
fresh bottom, c* has empty strict-downset interpretation over {c,n} and
SELECT from n*(c*,c) to c violates the proposed inclusion. In the actual
ordered auxiliary game, n*(c,u) has the three-step LEX/PUT/SELECT marked
cycle. Thus nonempty interpretations are justified and plain-endpoint
well-foundedness is not promoted to SN of the marked universe.

The lower-set interpretation is an editorial proof, not a claim that
the 1987 report, the primary Kamin--Levy note or the 1992 chapter prints
this argument. The six proof bindings close the previously open generic
ordered-LEX mechanism in the prepared fragments. When integrating, the
lead must replace the earlier marked-tree fragment's active final
sentence saying global ordered well-foundedness is unproved, rather
than append a contradictory later theorem. Its historical fourth-block
record below remains a dated account, not current proof standing.
Puel's separate method, full PA norm-indexing beyond the count-preserving
two-rule example, and all remaining source/application/variant obligations
remain allocated. No child, review, build, manuscript render, prose-test
suite, canonical/shared edit or security bypass was used.

### Fifth-block direct-sum continuation

New owned files: `spec/fragments/p12-klop-direct-sum-body.tex` and
`spec/fragments/p12-klop-direct-sum-annex.tex`, with unique
`handbook/bib/intake-p12-klop1987-direct-sum.bib` and
`handbook/registry/symbols-intake-p12-klop1987-direct-sum.csv`.
Released core and marked-tree fragments were not edited. These are
prepared source-specific integration fragments, not an admitted unit.

Reread the original1987report pp.15--17, including exact disjoint
signature hypotheses, both termination counterexamples, all eleven
first-factor rules of the stronger example, and the binary/applicative
test and selector distinctions. The full original42-page allocation
remains unchanged.

Primary proof actually consulted online: Yoshihito Toyama,
*Term Rewriting Systems and the Church-Rosser Property*, author-hosted
thesis dated May1990,161physicalpages, chapter2.2 printedpp.19--44,
physical pages25--50 (printed page=physicalpage-6).
Exact public PDF:
https://www.nue.ie.niigata-u.ac.jp/toyama/user/toyama/research/paper/thesis/dr.pdf .
Read definitions and lemmas2.2.1.1--2.2.3.10 through the actual PDF
text reader, including the preserved-system/cap coherence and full
deletion-depth proof. This is not a claim of reading all161pages,
and the thesis is not silently identified with the1987JACM article.

Acquisition qualification remains open: the exact publisher PDF route
https://dl.acm.org/doi/pdf/10.1145/7531.7534 returned403/challenge;
that route was stopped without circumvention. Ordinary independent
author-thesis downloads over HTTPS and HTTP timed out. No local
thesis PDF or local hash was obtained, and PDF screenshot attempts
returned cache-miss errors. Thus full selected online text was read,
but no local-body/hash or screenshot qualification is asserted for
that dependency. The existing original1987CWI report remains held
at its already recorded hashes. The missing dependency hash keeps
source-acquisition/admission open rather than being manufactured.

Nine prepared reciprocal proof items use prefix
`thm:p12-klop1987-ds-` and matching `annex:p12-klop1987-ds-`:

- `invariants`: rank nonincrease, preserved-term closure and the exact
  foreign-root/neutral-variable boundary, without ordinary SN.
- `coherence`: finite joinability classes, synchronization of every
  finite descendant choice, and exact transport of nonlinear matches,
  including variable-instance positions above a deletion frontier.
- `preserved`: inner-then-outer block diamond for fixed-colour caps
  with preserved CR frontier values, empty-cap root collapse included;
  preserved-term CR follows by layer-rank induction.
- `depth`: minimal nonpreserved special layers, finite actual first
  root-changing witnesses, ordinary depth nonincrease and strict
  decrease of parallel deepest deletion. No effective oracle is claimed.
- `diagrams`: disjoint, inside and above-frontier ordinary steps;
  independently reduced copies are coherently rejoined; shallower
  residual copies need not remain selected in the next deletion.
- `confluence`: depth/path-length double induction covering all mixed
  finite terms and converse pure-signature successor closure. No
  left-linearity, nonduplication, noncollapse or SN premise was added.
- `first-counter`: pure first-factor active-origin lexicographic
  termination, node-count termination of or, its nonconfluence and
  the exact three-step mixed loop.
- `complete-counter`: both source factors proved SN/CR; the first
  factor's spent/unspent F-origin vector and constant weights justify
  SN despite duplication, and the majority factor's nonlinear peaks
  are joined. The full source loop and attribution are retained.
- `applications`: binary equality and ternary selector factors are
  SN/CR at their actual nonlinear scope, giving separate CR sums withCL.

The new proof does not assert commutation of the two raw component
relations. The explicit D(a,a) versus D(b,a) example shows why a
further foreign step is needed on the nonlinear branch. Coherent
frontier repair, rather than arbitrary-union commutation, supplies
the missing dependency.

Precise surviving direct-sum cases: the applicative CL+ Dxx test's
own nonconfluence witness from Klop1980 remains source-cited, not
replaced by the binary proof. Related reduced/irreducible variants
and the Ganzinger--Giegerich extra-arrow correction retain their
separate rule-set/proof obligations. All other previously recorded
generic-completion, ordered-LEX, application, bibliography and
1987--1992 variant residuals remain allocated. The nine proofs are
not a source-unit completion percentage or admission/review claim.

### Fourth-block prepared marked-tree continuation (not the released core)

The lead froze the released body, active annex and original intakes while
integrating them. This block did not edit any of those files. It owns new
`spec/fragments/p12-klop-marked-trees-body.tex` and
`spec/fragments/p12-klop-marked-trees-annex.tex`, with uniquely suffixed
`handbook/bib/intake-p12-klop1987-marked-trees.bib` and
`handbook/registry/symbols-intake-p12-klop1987-marked-trees.csv`.
These elaborate the same source section3, not a second source unit.
Root must integrate them at their source-mapped positions; they are not
claimed already routed into the handbook.

The original 1987 report pp.18--22 was reread, and original Figure8/9
on p.19 was inspected again. The fragments retain its unranked natural
labels, unordered trees, actual marker operations and single-mark types.
They distinguish the literal source context closure from an explicitly
larger all-context auxiliary relation; proving the latter acyclic suffices
for the source subrelation without silently equating their definitions.

Separate primary proof dependency acquired:
`source/references/p12-klop1987/star-games-hydras-2021.pdf`, 32 physical pages,
SHA256 `A653EBC3A3F33F8C19ABBC5E11E14C49F247E428A57554AB73C4A97DFCCC9883`.
The publisher PDF is https://lmcs.episciences.org/7518/pdf .
Exact title *Star Games and Hydras*, Jorg Endrullis, Jan Willem Klop and
Roy Overbeek, LMCS17(2),20:1--20:32, published 27 May 2021.
Read pages20:9 and20:12--20:18; rendered all those pages and additionally
inspected20:9,12,16,17,18 visually. This is not a full32-page reading
claim. The helper `read-star-game-proof.py` and source-only images are
retained. Its first output attempt failed on cp1252 encoding; the helper
was repaired to UTF8 and the complete selected text was then read.
No manuscript render was run.

Ten prepared reciprocal results, each body label below paired with the
same suffix after `annex:p12-klop1987-`, are fully authored:

- `thm:p12-klop1987-mt-embedding`: well-defined source ancestry-order
  embedding on tree classes, reflexivity/transitivity/antisymmetry and
  the implication from a separately defined stronger planar embedding.
- `thm:p12-klop1987-mt-words`: infinite nondecreasing subsequences,
  product wqo, full minimal-bad-word proof, and natural labels.
- `thm:p12-klop1987-mt-kruskal`: full minimal-bad-tree child-set proof
  for unbounded natural labels, depth and branching; not a finite-ranked
  alphabet surrogate.
- `thm:p12-klop1987-mt-embedding-reduction`: constructive marker
  simulation, including source sibling images sharing a target stem.
- `thm:p12-klop1987-mt-tracing`: all put/select/copy/push origins,
  unique ancestors versus possibly multiple descendants, numerical label
  decrease, bounded subtree projection and permutation postponement.
- `thm:p12-klop1987-mt-acyclic`: smallest-node/shortest-cycle proof,
  root ancestry, removal of select/copy/one-copy, and separate pruning
  of an original child versus a born copy in the zero-copy case.
- `thm:p12-klop1987-mt-well-founded`: strict unmarked source order by
  the proved wqo, reverse embedding and acyclicity.
- `thm:p12-klop1987-mt-boolean`: positive marker paths for allfive
  actual source Table9 rules, with substitution/context transport.
- `thm:p12-klop1987-mt-indexed`: source simplified g/h pair, exact
  numerical label realization and preservation of ancestor annotations
  because both original rules preserve node count.
- `thm:p12-klop1987-mt-obstruction`: explicit reverse-embedding
  obstruction for the source's f(s(x)) example, without claiming that
  another termination method is impossible.

Figures8/9 are reconstructed by their full labelled/marked tree terms
and the actual copying path. The source Figure10 is given with its
actual node map. Source3.6's ancestry-order convention and its Figure10
are not silently equated with the2021 paper's stronger meet-preserving
definition: the later paper changes the analogous internal0 to8.
The source fragment establishes the needed wqo using the stronger planar
relation and then proves the weaker source relation's simulation separately.
The tracing proof also explicitly copies child origins in push, rather
than mistaking unique ancestry for unique descendants.

Exact residual in this block: the generic ordered fixed-arity relation
with the additional left-argument/LEX operation in source Remark3.11(iii)
is stated, and the actual Ackermann marker path is supplied, but its
global acyclicity/well-foundedness is **not yet proved**. The proof of
the commutative four-operation game cannot be extended by inclusion to
that larger relation. Puel's separate method and the full process-algebra
rules beyond the node-count-preserving simplified pair also remain owed.
Ten prepared proofs do not close the whole source unit or any admission gate.

| Allocated component | Current authoring standing | Exact surviving obligation |
| --- | --- | --- |
| `ED26-SRC-027-501-DOMAIN` | substantive partial reconstruction; unordered/ordered marker and direct-sum conventions adopted in source-mapped book bodies | root-owned canonical intake/annex-driver reconciliation and remaining notation closure; original sorted/operator subtleties |
| `ED26-SRC-027-501-CHAIN` | substantive partial across all six sections; ARS/group/strategy, main marked/Kruskal, direct-sum, ordered-LEX and exact PA3/PA7 norm/budget chains adopted with reciprocal annex files | source decidability/universality dependencies; generic Table13 correctness/failure argument; same-signature finite-presentation obstructions; broader Huet parallel theorem; general needed-redex/strong-sequentiality claims; general Puel unavoidable-set extension and larger primary ACP/indexing variants beyond the explicitly proved PA systems |
| `ED26-SRC-027-501-CASES` | substantive partial; ARS countercases, both puzzles, Omega, actual group peaks, direct-sum factors, all Ackermann/associativity paths, actual PA contextual countercase/repairs and isolated Puel example supplied | full source arithmetic/ground WN and SN proofs; SKIM encodings beyond supplied B derivation; nonconfluent applicative equality-test witness/proof; related reduced direct-sum variants and Ganzinger--Giegerich correction; general Puel and larger ACP companion applications; source's finite-presentation/multiset obstruction arguments and remaining application qualifications |
| `ED26-SRC-027-501-ATTRIBUTION` | substantive partial; source theorem attributions and figure/table roles retained | full reader-facing reconstruction of remaining graphical surfaces including CL's Figure7 graph; exact reference-record intake for the complete source bibliography; final source-to-body locator crosswalk and notation closure |
| `ED26-SRC-027-501-RELATION` | exact non-substitution boundary recorded; full comparison open | full publisher-body correspondence, substantive variants and any corrections between this report and ED26-SRC-027-001; nothing here closes the 1992 chapter unit |

The complete finite allocation remains **entire 42-physical-page report**.
The cited theorem boundaries in the body do not waive the queue's separate
full-proof success condition. This block must not be marked complete from
its subsection count, file size, a proof-item count, matching names, or absence
of a missing-source blocker. The ARS and concrete group-completion blocks
are now supplied alongside the strategy table; full original marked-tree,
ordered-LEX and modularity arguments now have source-mapped book bodies
and reciprocal annex files. The next substantive work is the remaining basic/application
and generic-completion proof surfaces, broader Huet theorem,
and any separately allocated
full argument behind the report's general needed/sequentiality claims.

## Verification limits

Read back the source and active annex text, checked source formulas against
the listed rendered primary pages, and confirmed source hashes and page
extent. No child agent, reviewer, manuscript build, manuscript render,
prose regression test, canonical/generated update, pay/login/contact action,
or access-control bypass was used. The source-only renderer is not a
manuscript render. The sandbox helper failed after a scoped permission
refresh; normal `require_escalated` approval for exact assigned commands
was used, as permitted by the lead. Independent reviews, scoped static/build
and manuscript visual evidence, and any admission remain pending.

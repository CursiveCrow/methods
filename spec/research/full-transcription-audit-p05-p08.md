# Full-transcription audit: Parts 5--8

**Snapshot audited:** 2026-08-11.  The P8 files were changing concurrently; the
line references below identify the snapshot read for this audit.  Source-line
references are stable and control every restoration.

## Controlling rule and classifications

The controlling inherited text is
`source/formal-logic-reference.tex`: Part VI, lines 9080--10059 (live P5);
Part VII, lines 10060--11353 (live P6); Part VIII, lines 11354--12248
(live P7); and Part X, lines 12970--14094 (live P8).  Part IX was moved to
live P2 and is outside this ledger.  Frozen v1.1 is authoritative for every
inherited word, formula, displayed rule, hypothesis, proof-status sentence,
citation, warning, example, exercise, proof, and proof sketch.  A live
replacement cannot discharge an inherited unit merely because it states a
similar fact.

Classifications used below:

- **exact/full** -- the complete source unit is present without a content or
  syntax change.
- **layout-only** -- only the handbook wrapper, label, placement, or typography
  changes; the complete source surface remains.
- **altered** -- wording, notation, syntax, hypotheses, conclusion, status, or
  attribution changes.
- **shortened** -- a source unit is summarized, compressed, or only partly
  reproduced.
- **omitted** -- no live transcription of the source unit exists.
- **hybrid** -- inherited and later/editorial/literature material are fused in
  one presentation.
- **unsupported** -- a register addition has no fixed edition/page/line/text
  controller from which exact transcription can be verified.  This verdict is
  about transcription evidence, not mathematical truth.

Multiple classifications can apply.  No mathematical unit in these four parts
is **exact/full** as a complete source-to-live unit.  The body of the Robinson
arithmetic definition is the only material located that is **layout-only** in
isolation; its surrounding source section is not.

## Literal restoration protocol

Every “restore” cell below is literal: copy the complete indicated frozen line
span, in order, without paraphrase, normalization, synthesis, or deletion.
Handbook environment wrappers and page placement may change, but the source
prose, mathematical tokens, labels needed by the text, citations, status
sentences, and exercises must remain.  Existing new material may follow only
as a separately headed, separately attributed addition.  It must not be
interleaved with or substituted for the inherited span.

For register additions, the CSV `sources` field is not itself a transcription
controller.  Where several works or variants are named, each must receive a
separate attributed source block with its own fixed edition and page/section
span.  No row below licenses selecting one variant as a replacement for
another or merging their syntax into a handbook-normalized hybrid.

## P5 inherited-source ledger

| Frozen source | Literal source surface | Current live destination | Class | Exact restoration |
|---|---|---|---|---|
| 9080--9098 | `\part{Formal Arithmetic and Incompleteness}`; `\chapter{Arithmetic, Representation, and Coding}`; `\section{The language and standard structure of arithmetic}` | `handbook/parts/p05.tex:4`; `handbook/parts/p05/diagonalization.tex:6--43` | altered, hybrid | Restore 9080--9098 verbatim before the first P5 inherited definition.  In particular restore both source titles and the source cross-reference paragraph at 9094--9097; do not replace that paragraph by the new arithmetic-language and calculus entries. |
| 9099--9111 | `\begin{definition}[Robinson arithmetic]` | `handbook/parts/p05/diagonalization.tex:45--57` | layout-only | Retain the live handbook wrapper if desired, but make its body byte-for-byte equal to 9100--9110. |
| 9112--9149 | order-abbreviation qualification; `\begin{lemma}[Bounded-case enumeration in \(\mathsf Q\)]`; `\textit{Status: complete proof.}`; complete proof | `handbook/parts/p05/diagonalization.tex:71--95`; `handbook/annex/p05.tex:11--22` | shortened, hybrid | Restore 9112--9149 verbatim.  Replace the compressed annex proof at 13--20, and retain the exact source status sentence at 9128. |
| 9150--9174 | `\begin{lemma}[Dichotomy in \(\mathsf Q\)]`; `\textit{Status: complete proof.}`; complete proof | `handbook/parts/p05/diagonalization.tex:97--103`; `handbook/annex/p05.tex:24--33` | shortened | Restore 9150--9174 verbatim; replace the compressed proof at annex lines 26--31 and restore the explicit status line 9158. |
| 9175--9187 | `\begin{definition}[Peano arithmetic]` | `handbook/parts/p05/diagonalization.tex:59--69` | altered | Restore 9175--9187 verbatim.  The live display changes the source tokens `\bar z` at 9180--9185 to `\vec z`; frozen syntax controls. |
| 9188--9261 | `\section{Standard and nonstandard models of arithmetic}`; definitions, compactness theorem, complete proof, example, exercise, and warning | `handbook/parts/p05/models-and-interpretability.tex:11--117`; `handbook/annex/p05/depth-completion.tex:3--15` | shortened, altered, hybrid | Restore 9188--9261 verbatim in order.  Replace the rewritten compactness proof, restore `ex:arithmetic-coding-01` at 9240--9247, and retain the exact standard-truth warning at 9249--9260.  Later overspill, order-type, and Tennenbaum material must be a separate addition. |
| 9262--9327 | `\section{Representability}`; two definitions; representability theorem and proof sketch; worked addition example | `handbook/parts/p05/diagonalization.tex:105--137` | shortened, altered | Restore 9262--9327 verbatim.  The live text omits the complete worked addition unit at 9311--9326 and rewrites the theorem/sketch. |
| 9328--9438 | `\section{G\"odel coding}`; numbering and c.e.-theory definitions; finite-sequence example; arithmetization theorem and proof plan; proof predicate; warning; two exercises | `handbook/parts/p05/diagonalization.tex:139--214`, with editorial pointers to P4 | shortened, omitted, hybrid | Restore 9328--9438 verbatim.  The explicit source declaration that the arithmetization proof sketch is “deliberately retired” at live lines 199--206 is a defect.  Restore the sequence-code example, theorem, proof plan, and exercises 9421--9437; P4 material may follow separately. |
| 9439--9497 | `\chapter{Diagonalization and the First Incompleteness Theorem}`; diagonal theorem; full fixed-point construction; remark | `handbook/parts/p05/diagonalization.tex:216--257`; `handbook/annex/p05.tex:38--65` | shortened, altered | Restore 9439--9497 verbatim.  Replace the cited-summary/method rewrite and annex commentary with the exact construction at 9462--9490 and exact remark at 9492--9496. |
| 9498--9538 | `\section{Consistency and soundness conditions}`; consistency, deductive completeness, `\Sigma^0_1`-soundness, and omega-consistency | `handbook/parts/p05/diagonalization.tex:259--300` | altered | Restore 9498--9538 verbatim.  Do not substitute the live strengthened/qualified consistency definition or its new cross-calculus discussion for the source definition and intervening paragraphs. |
| 9539--9619 | G\"odel sentence construction; original first-incompleteness theorem; proof plan; warning | `handbook/parts/p05/diagonalization.tex:301--340`; `handbook/annex/p05.tex:66--89` | shortened, altered | Restore 9539--9619 verbatim, including every step of the source proof plan and the exact hypothesis/status surface. |
| 9620--9728 | Rosser theorem; proof plan; undecidability corollary and proof plan; closing remark | `handbook/parts/p05/diagonalization.tex:342--371`; `handbook/annex/p05.tex:90--140` | shortened | Restore 9620--9728 verbatim.  The live body and annex jointly compress both proof plans and the final remark. |
| 9729--9749 | three exercises `ex:first-incompleteness-01`--`03` | no live exercise units; `handbook/parts/p05/diagonalization.tex:211--214` states the exercise layer is not printed | omitted | Insert 9729--9749 verbatim immediately after the Rosser material. |
| 9750--9816 | chapter/section headings; Hilbert--Bernays--L\"ob conditions; formal consistency sentence; external/internal warning | `handbook/parts/p05/provability-truth.tex:1--73` | altered, shortened | Restore 9750--9816 verbatim.  Preserve the source conditions, abbreviations, intervening qualifications, and warning as written; later metadata may follow separately. |
| 9817--9876 | L\"ob theorem and complete proof | `handbook/parts/p05/provability-truth.tex:74--88`; `handbook/annex/p05.tex:141--162` | shortened, altered | Restore 9817--9876 verbatim, including the full proof at 9834--9875. |
| 9877--9924 | second incompleteness theorem, complete proof, scope warning, relative-consistency example | `handbook/parts/p05/provability-truth.tex:89--121`; `handbook/annex/p05.tex:163--173` | shortened, altered | Restore 9877--9924 verbatim.  Do not use the shorter annex derivation as the transcription of 9891--9904. |
| 9925--9992 | truth-definition definition; Tarski theorem and proof; corollary and proof; partial-truth remark | `handbook/parts/p05/provability-truth.tex:122--160`; `handbook/annex/p05.tex:174--194` | shortened, altered | Restore 9925--9992 verbatim, including both proofs and the exact partial-truth qualification. |
| 9993--10027 | `\section{A final audit table}` and complete table | `handbook/parts/p05/provability-truth.tex:161--208` | altered, hybrid | Restore 9993--10027 verbatim as its own table.  Do not treat the live hypothesis/evidence table, whose rows and wording were edited, as a literal transcription. |
| 10028--10059 | four exercises `ex:second-incompleteness-01`--`04` | absent | omitted | Insert 10028--10059 verbatim after the audit table. |

### P5 decisive departures

1. `handbook/parts/p05/diagonalization.tex:199--214` expressly retires the
   source arithmetization proof plan, worked examples, and exercises.  All are
   compulsory transcription units.
2. `handbook/parts/p05/diagonalization.tex:63--68` changes the frozen PA
   parameter tokens `\bar z` to `\vec z`.
3. Proofs at `handbook/annex/p05.tex:11--33`, `66--140`, and `141--199` are
   compressed rewrites, not moved source proofs.
4. The exact ordered arithmetic, coding, and diagonal constructions cannot be
   discharged by new P4 pointers or by later citations.

## P6 inherited-source ledger

| Frozen source | Literal source surface | Current live destination | Class | Exact restoration |
|---|---|---|---|---|
| 10060--10088 | `\part{Axiomatic Set Theory}`; `\chapter[The Axioms of ZF and ZFC]{...}`; scoped-semantic convention and introductory paragraphs | `handbook/parts/p06.tex:2`; `handbook/parts/p06/axioms-hierarchy.tex:9--28` | altered, hybrid | Restore 10060--10088 verbatim.  The shorter part title and rewritten convention are not layout-only. |
| 10089--10271 | language/classes convention; separate Extensionality, Empty Set, Pairing/Union/Power Set, Infinity, Separation, Replacement, omega, Foundation, Choice, ZF/ZFC definitions; remark | `handbook/parts/p06/axioms-hierarchy.tex:17--162` | altered, hybrid | Restore 10089--10271 verbatim as separate source units.  The A-058 longtable merges and rewrites them and adds formula choices and side-condition prose; retain that table only as a separately attributed addition. |
| 10272--10352 | first constructions; ordered-pair lemma and complete proof; membership-loop example; set-recursion theorem and sketch; warning; two exercises | `handbook/parts/p06/axioms-hierarchy.tex:164--220`; moved rewrite at `handbook/parts/p01/mathematical-preliminaries.tex:61--67` and `handbook/annex/p01.tex:6--18` | shortened, altered, omitted | Restore 10272--10352 verbatim in P6.  The P1 proof is expanded/reworded rather than literal.  Restore both exercises 10341--10351. |
| 10353--10451 | hierarchy chapter heading; ordinals; trichotomy; transfinite induction and complete proof; transfinite recursion and sketch | `handbook/parts/p06/axioms-hierarchy.tex:221--280`; `handbook/annex/p06/axioms-hierarchy.tex:48--83` | altered, shortened, hybrid | Restore 10353--10451 verbatim.  Keep the later ordinal-arithmetic development separate; it cannot replace the source theorem/proof surfaces. |
| 10452--10520 | cumulative hierarchy, hierarchy theorem/sketch, rank, first-stages example/sketch | `handbook/parts/p06/axioms-hierarchy.tex:454--556`; annex lines 84--99 | altered, shortened, hybrid | Restore 10452--10520 verbatim before any A-130 figure or expanded rank results. |
| 10521--10558 | well-founded relations and Mostowski collapse theorem/sketch | `handbook/parts/p06/axioms-hierarchy.tex:557--587`; `handbook/annex/p06/axioms-hierarchy.tex:100--113` | altered, shortened | Restore 10521--10558 verbatim. |
| 10559--10674 | equipotence, Hartogs, order vocabulary, Choice equivalents, aleph/CH/GCH definition, Choice warning, three exercises | `handbook/parts/p06/cardinals-choice.tex:100--268`; `handbook/parts/p06/cardinal-arithmetic.tex:1--184`; annex/cardinal-choice | altered, shortened, hybrid, omitted | Restore 10559--10674 verbatim in source order.  The new AC-equivalence and cardinal-arithmetic catalogs must follow separately.  Restore all exercises 10656--10673; the omission comment at cardinal-arithmetic lines 183--184 does not discharge them. |
| 10675--10769 | constructibility chapter; definable subsets and hierarchy; formula-by-formula relativization; theorem/sketch; cited ZFC+GCH+V=L scheme and boundary | `handbook/parts/p06/constructibility-forcing.tex:17--128`; `handbook/annex/p06/constructibility-forcing.tex:4--11` | altered, shortened, hybrid | Restore 10675--10769 verbatim, including the exact cited-theorem attribution and its formula-by-formula qualification at 10754--10768. |
| 10770--10825 | countable-transitive-set convention and full explanation of why it exceeds `Con(ZFC)` | `handbook/parts/p06/constructibility-forcing.tex:129--159`; annex lines 13--23 | altered, shortened | Restore 10770--10825 verbatim. |
| 10826--10881 | poset filter, dense set, genericity, and bounded-absoluteness material | `handbook/parts/p06/forcing-vocabulary.tex:3--96`; `handbook/parts/p06/constructibility-forcing.tex:160--180`; annex lines 25--32 | altered, hybrid, shortened | Restore 10826--10881 verbatim.  The separate forcing-vocabulary normalization may follow as an addition. |
| 10882--10899 | generic-filter lemma and complete proof | body lines 181--190; `handbook/annex/p06/constructibility-forcing.tex:34--44` | altered, shortened | Restore 10882--10899 verbatim. |
| 10900--10988 | names, evaluation, extension, check names, semantic forcing | `handbook/parts/p06/constructibility-forcing.tex:191--248`; annex lines 46--58 | altered, shortened, hybrid | Restore 10900--10988 verbatim. |
| 10989--11011 | monotonicity lemma and complete proof | body lines 249--258; annex lines 60--66 | altered | Restore 10989--11011 verbatim. |
| 11012--11052 | cited forcing theorem, four enumerated claims, and internal proof boundary | `handbook/parts/p06/constructibility-forcing.tex:259--286` | altered, shortened | Restore 11012--11052 verbatim, including Jech page scope and every omitted-proof qualification. |
| 11053--11103 | complete one-Cohen-real example | body lines 287--323; annex lines 68--96 | altered, shortened | Restore 11053--11103 verbatim. |
| 11104--11126 | relativization-of-derivations lemma statement | body lines 373--393 | altered | Restore 11104--11126 verbatim. |
| 11127--11199 | complete relativization proof | `handbook/annex/p06/constructibility-forcing.tex:179--212` | shortened, altered | Replace the 33-line rewrite with source lines 11127--11199 verbatim. |
| 11200--11239 | relative consistency of CH theorem and complete proof | body lines 394--425; annex lines 214--236 | shortened, altered | Restore 11200--11239 verbatim. |
| 11240--11279 | cited relative consistency of `not CH`: Boolean-valued data, four imported schemes, and calculus-transfer qualification | body/forcing-variants summaries near `handbook/parts/p06/forcing-variants.tex:207--241` | shortened, altered, hybrid | Restore 11240--11279 verbatim as the inherited cited theorem.  Do not replace its exact Boolean-valued surface by a catalog row. |
| 11280--11293 | arithmetized-form remark and proof sketch | body/annex `handbook/annex/p06/constructibility-forcing.tex:238--247` | shortened, altered | Restore 11280--11293 verbatim. |
| 11294--11314 | nonderivability theorem and complete proof | body lines 426--441; annex lines 249--261 | altered, shortened | Restore 11294--11314 verbatim. |
| 11315--11337 | two warnings: consistency theorem scope and countable transitive structures | body lines 373--449, dispersed | shortened, altered | Restore 11315--11337 verbatim and contiguous after the nonderivability proof. |
| 11338--11353 | two forcing exercises | live lines 442--448 expressly retire them | omitted | Insert 11338--11353 verbatim. |

### P6 decisive departures

1. `handbook/parts/p06/axioms-hierarchy.tex:84--162` replaces eleven source
   units with a synthesized axiom table.  This changes unit boundaries,
   formulas, and explanatory text.
2. The complete ordered-pair proof was moved to P1 but rewritten; a cross-part
   duplicate is not a literal P6 transcription.
3. The complete source relativization and CH proofs are compressed at
   `handbook/annex/p06/constructibility-forcing.tex:179--236`.
4. P6 source exercises are deliberately omitted at
   `handbook/parts/p06/axioms-hierarchy.tex:211--219`,
   `handbook/parts/p06/cardinal-arithmetic.tex:183--184`, and
   `handbook/parts/p06/constructibility-forcing.tex:442--448`.

## P7 inherited-source ledger

| Frozen source | Literal source surface | Current live destination | Class | Exact restoration |
|---|---|---|---|---|
| 11354--11413 | `\part{Proof Theory}`; source chapter and conventions; classical and intuitionistic sequent definitions | `handbook/parts/p07.tex:2`; `handbook/parts/p07/calculi-and-derivability.tex:6--44` | altered, hybrid | Restore 11354--11413 verbatim.  The live part title adds `and $\lambda$-Calculi`, and the sequent definitions and convention are rewritten. |
| 11414--11505 | complete propositional and quantifier rule surface of `\LK` | `handbook/registry/calculi/lk-defneg.tex:1--23`; references in `handbook/parts/p07/calculi-and-derivability.tex:45--78` | altered, shortened, hybrid | Restore 11414--11505 verbatim as one source calculus surface.  Do not replace it with the registry sheet: the sheet adds a new identifier, wrapper metadata, normalized metavariables, and extra side-condition prose. |
| 11506--11519 | definition of an `\LK` derivation | calculus chapter lines 45--78 and the sheet | altered, shortened | Restore 11506--11519 verbatim. |
| 11520--11598 | complete `\LJ` rule surface | `handbook/registry/calculi/lj.tex:1--21`; calculus chapter lines 45--78 | altered, shortened, hybrid | Restore 11520--11598 verbatim; keep any registry card separate. |
| 11599--11627 | `\LJ`-derivation definition; `\LK` soundness theorem and proof sketch | `handbook/parts/p07/calculi-and-derivability.tex:36--100`; `handbook/annex/p07/calculi-and-cut-elimination.tex:5--35` | altered, shortened | Restore 11599--11627 verbatim.  The live theorem is for a newly named defined-negation calculus, not a literal copy of the source `\LK` theorem. |
| 11628--11644 | complete worked cut-free derivation | no source-shaped derivation; `handbook/parts/p07/calculi-and-derivability.tex:319--325` says it is retired/replaced | omitted | Insert 11628--11644 verbatim after the soundness sketch. |
| 11645--11695 | primitive, derived, admissible, Cut-after-elimination example, warning, principal-formula definition | `handbook/parts/p07/calculi-and-derivability.tex:101--183` | altered, hybrid, shortened | Restore 11645--11695 verbatim in order.  The A-070 comparison table and new rule-standing synthesis may follow separately. |
| 11696--11710 | two exercises | live source-disposition paragraph at 319--331 | omitted | Insert 11696--11710 verbatim. |
| 11711--11740 | cut-elimination chapter heading; rank/height; full Mix rule and qualifications | `handbook/parts/p07/cut-elimination-and-interpolation.tex:18--43` | altered, shortened | Restore 11711--11740 verbatim, including both `\LK` and `\LJ` Mix surfaces. |
| 11741--11767 | equipollence lemma and complete proof | body lines 44--47; `handbook/annex/p07/calculi-and-cut-elimination.tex:36--46` | shortened, altered | Restore 11741--11767 verbatim. |
| 11768--11823 | cut/mix measures; cut-elimination theorem and seven-step proof sketch | body lines 48--90; annex lines 47--67 | shortened, altered | Restore 11768--11823 verbatim.  The live annex explicitly refers to an omitted reduction table and is not the source sketch. |
| 11824--11881 | subformula definition; lemma and proof; two corollaries and proof plans; first-order qualification | body lines 91--132; annex lines 68--93 | altered, shortened | Restore 11824--11881 verbatim. |
| 11882--11913 | exact “What cut elimination establishes” qualifications, warning, and two exercises | body lines 91--132 and 274--280 | shortened, omitted | Restore 11882--11913 verbatim; reinsert both exercises. |
| 11914--11960 | interpolation/definability section; Craig and Beth theorems; source paragraphs and citations | `handbook/parts/p07/cut-elimination-and-interpolation.tex:180--273`; `handbook/annex/p07/interpolation.tex:3--23` | hybrid, altered, shortened | Restore 11914--11960 verbatim as the inherited block.  Maehara material and register rows must follow separately; they do not replace the cited source statements. |
| 11961--12029 | normalization chapter/section; detour and reductions; normalization theorem and full proof sketch; cut/normalization distinction | `handbook/parts/p07/normalization-and-curry-howard.tex:18--97`; `handbook/annex/p07/normalization.tex:3--20` | altered, shortened, hybrid | Restore 11961--12029 verbatim. |
| 12030--12100 | STLC grammar, typing and reduction rules, subject reduction and proof sketch, strong normalization and reducibility sketch | `handbook/parts/p07/normalization-and-curry-howard.tex:98--149`; `handbook/registry/calculi/stlc.tex:1--9`; annex normalization lines 21--47 | altered, shortened, hybrid | Restore 12030--12100 verbatim.  The sheet explicitly changes source type metavariables to Greek letters; frozen tokens control.  Restore both source proof sketches in full. |
| 12101--12132 | Curry--Howard correspondence; complete composition example; products/sums/bottom/classical qualification | body lines 150--358 | altered, hybrid | Restore 12101--12132 verbatim.  The live “expanded” composition presentation is not a literal transcription. |
| 12133--12217 | scope of ordinal analysis; cited Gentzen theorem; exact formal objects; calculations; internal proof boundary; second-incompleteness qualification; warning | `handbook/parts/p07/arithmetic-proof-theory.tex:21--318`, interleaved with register additions | shortened, altered, hybrid | Restore 12133--12217 verbatim as one contiguous inherited section before the new arithmetic-proof-theory chapter material. |
| 12218--12248 | three exercises with the abstract-reduction definition between the second and third | exercises absent; definition dispersed/reworked in normalization chapters | omitted, altered | Restore 12218--12248 verbatim in its exact order.  The definition cannot be moved out while all three exercises are retired. |

### P7 decisive departures

1. `handbook/parts/p07/calculi-and-derivability.tex:319--331` says that source
   rule displays moved “verbatim in substance” and that the worked derivation
   and exercises were retired.  “In substance” is not literal transcription.
2. The LK/LJ sheets add system names, metadata, side conditions, and normalized
   formula roles; `handbook/registry/calculi/stlc.tex` changes the source
   metavariable alphabet.  These are altered/hybrid rule surfaces.
3. `handbook/annex/p07/calculi-and-cut-elimination.tex:32--87`,
   `handbook/annex/p07/interpolation.tex:22--23`, and
   `handbook/annex/p07/normalization.tex:16--45` explicitly leave source cases
   or closure arguments omitted.
4. Exercises are expressly retired at
   `handbook/parts/p07/cut-elimination-and-interpolation.tex:274--280`,
   `handbook/parts/p07/normalization-and-curry-howard.tex:359--368`, and
   `handbook/parts/p07/arithmetic-proof-theory.tex:311--318`.

## P8 inherited-source ledger

| Frozen source | Literal source surface | Current live destination | Class | Exact restoration |
|---|---|---|---|---|
| 12970--12988 | `\part{Nonclassical Logic}`; `\chapter{Intuitionistic Logic}`; formula convention; positive specification paragraph | `handbook/parts/p08.tex:2`; `handbook/parts/p08/intuitionistic-and-intermediate.tex:2--21` | altered, hybrid | Restore 12970--12988 verbatim.  The live part pluralizes `Logic`, changes the chapter title, and replaces the convention with a source-normalization policy. |
| 12989--13045 | source section heading; exact IPL grammar, finite-support derivability, partially ordered frames, valuation, and forcing clauses | intuitionistic chapter lines 22--97 | altered, hybrid | Restore 12989--13045 verbatim.  The live definition at lines 39--50 changes `partially ordered set` to `preordered set`; this is a mathematical variant, not layout. |
| 13046--13057 | persistence lemma and complete proof | body/annex `handbook/annex/p08/intuitionistic-and-intermediate.tex:1--8` | shortened, altered | Restore 13046--13057 verbatim. |
| 13058--13099 | semantic consequence; soundness/strong-completeness theorem with finite rooted countermodel clause; proof sketch | intuitionistic chapter lines 89--142; annex lines 9--35 | shortened, altered, hybrid | Restore 13058--13099 verbatim, including the exact finite-model conclusion and every proof-sketch sentence. |
| 13100--13127 | counterexample structure/world; constructive derivation; disjunction-at-a-world warning | body lines 143--192 | altered, hybrid | Restore 13100--13127 verbatim before A-137/A-138 figures. |
| 13128--13140 | two exercises | lines 391--394 say one became a figure and one was retired | omitted | Insert 13128--13140 verbatim.  A-138 is an addition, not the exercise text. |
| 13141--13157 | Glivenko theorem with exact finite-multiset sequent statement, cited status, citation, and quantifier warning | body lines 193--207 and A-082 table | altered, hybrid | Restore 13141--13157 verbatim.  The live theorem changes turnstile syntax and attribution surface. |
| 13158--13179 | G\"odel--Gentzen translation theorem with exact clauses and cited status | body lines 277--311 and A-082 table | altered, hybrid | Restore 13158--13179 verbatim.  Kolmogorov and Kuroda variants must remain separately attributed additions. |
| 13180--13200 | disjunction-property theorem, `Status: complete proof`, complete proof, classical contrast | body lines 381--389, with proof reassigned to P7 | altered, omitted | Restore 13180--13200 verbatim in P8.  Live lines 381--387 reverse the frozen evidence status by calling the proof non-independent/cited; frozen v1.1 explicitly says `Status: complete proof.` |
| 13201--13213 | modal/temporal/epistemic chapter heading; modal grammar and `\Diamond` abbreviation | `handbook/parts/p08/modal-logics.tex:3--57` | altered, hybrid | Restore 13201--13213 verbatim before the expanded modal catalog. |
| 13214--13254 | Kripke frame/structure, satisfaction, validity, and local/global consequence definitions | modal chapter lines 5--57 and later entry cards | altered, hybrid | Restore 13214--13254 verbatim. |
| 13255--13284 | exact K calculus, necessitation qualification, T/S4/S5 definitions, premise-sensitive derivation | registry sheets `hilbert-k.tex`, `hilbert-t.tex`, `hilbert-s4.tex`, `hilbert-s5.tex`; modal chapter lines 58--340 | altered, hybrid | Restore 13255--13284 verbatim as one inherited calculus block.  Sheets may follow, but cannot replace its exact syntax or theorem-only necessitation prose. |
| 13285--13316 | four-system correspondence/completeness theorem and canonical-model proof sketch | modal chapter lines 58--390; annex `handbook/annex/p08/modal-logics.tex:1--50` | shortened, altered, hybrid | Restore 13285--13316 verbatim, including the exact theorem scope and proof sketch. |
| 13317--13339 | three exact counterexample structures/worlds for T, 4, and 5 | modal chapter lines 608--650 and figures A-139--A-141 | altered, hybrid | Restore 13317--13339 verbatim.  Live lines 610--614 explicitly replace the one-world edgeless T countermodel by a “nondegenerate variant”; that replacement is forbidden.  Figures may accompany, not alter, the source examples. |
| 13340--13409 | LTL grammar; all Boolean abbreviations; infinite-word semantics; exact X/U/F/G clauses; validity qualification | temporal chapter lines 15--47; `handbook/registry/calculi/hilbert-ltl.tex` | shortened, altered, hybrid | Restore 13340--13409 verbatim. |
| 13410--13439 | exact source LTL Hilbert calculus, three schemas, three rules, and theorem-only qualification | `handbook/registry/calculi/hilbert-ltl.tex:1--10`; temporal body lines 49--69 | altered, shortened | Restore 13410--13439 verbatim before the sheet card. |
| 13440--13471 | LTL soundness/completeness theorem and full proof sketch with exact weak-status qualifications | temporal body lines 70--80; `handbook/annex/p08/temporal-dynamic-epistemic.tex:1--25` | shortened, altered | Restore 13440--13471 verbatim.  The annex itself names omitted consistency/eventuality/truth-lemma calculations and is a further compression. |
| 13472--13478 | eventuality-is-not-recurrence example | temporal body lines 82--87 and A-145/A-147 figures | altered, hybrid | Restore 13472--13478 verbatim; figures follow separately. |
| 13479--13518 | epistemic grammar, Kripke semantics, S5 calculus | temporal chapter lines 509--585; `handbook/registry/calculi/hilbert-s5n.tex` | altered, hybrid | Restore 13479--13518 verbatim before multi-agent additions. |
| 13519--13551 | multi-agent S5 theorem/sketch and common-knowledge definition | temporal chapter lines 509--662; annex lines 37--51 | shortened, altered, hybrid | Restore 13519--13551 verbatim. |
| 13552--13564 | truth-without-knowledge example and accessibility-condition warning | temporal chapter lines 509--585, dispersed | shortened, altered | Restore 13552--13564 verbatim, including the exact warning.  A KD45 card is not its transcript. |
| 13565--13583 | three exercises | temporal lines 759--773 expressly retire them | omitted | Insert 13565--13583 verbatim. |
| 13584--13613 | many-valued chapter/section; logical-matrix and matrix-consequence definitions | `handbook/parts/p08/many-valued-and-fuzzy.tex:10--40` | altered, hybrid | Restore 13584--13613 verbatim.  The live finite-matrix definition changes scope and adds new vacuity/boundary clauses. |
| 13614--13640 | value-labelled tableau construction and saturated-branch definition | many-valued body lines 42--71; `handbook/registry/calculi/tableaux-matrix.tex:1--10` | altered, hybrid | Restore 13614--13640 verbatim.  The sheet labels itself extracted and repaired and is therefore not literal source. |
| 13641--13699 | finite-matrix tableau theorem and complete proof | body lines 72--82; `handbook/annex/p08/many-valued-and-fuzzy.tex:6--37` | shortened, altered | Restore 13641--13699 verbatim.  Annex line 2 expressly says it compresses the inherited complete proof. |
| 13700--13730 | exact K3 matrix and excluded-middle example | many-valued body lines 84--146 | altered, hybrid | Restore 13700--13730 verbatim before the K3 system card and later theorem-set additions. |
| 13731--13774 | LP matrix; paraconsistent-consequence definition; explosion countervaluation; truth-value warning | many-valued body lines 115--179 | altered, hybrid | Restore 13731--13774 verbatim.  The live definition adds `paracomplete`, changes unit boundaries, and merges register material. |
| 13775--13788 | two exercises | file header lines 5--8 says both are retired/recast | omitted | Insert 13775--13788 verbatim. |
| 13789--13806 | relevance/linear chapter heading; structural rules and exact set/multiset/sequence qualification | `handbook/parts/p08/substructural.tex:11--35` | altered, hybrid | Restore 13789--13806 verbatim.  The new `context profile` definition is an addition, not a transcription. |
| 13807--13861 | exact relevance grammar; Routley--Meyer frame/structure; satisfaction and validity; system-dependence qualification | substructural body lines 37--81 and 146--340 | altered, hybrid | Restore 13807--13861 verbatim.  The live term “broad Routley--Meyer frame” and later selected E/R/RM presentations are editorial additions and must be separate. |
| 13862--13896 | normal-world implication calculation and star calculation | substructural body lines 83--106 | altered | Restore 13862--13896 verbatim. |
| 13897--13918 | exact cited Routley--Meyer theorem paragraph and internal proof boundary | body lines 146--158 and later cards | altered, shortened, hybrid | Restore 13897--13918 verbatim, with the precise source scope and without selecting a replacement system. |
| 13919--13938 | failure-of-irrelevant-weakening example and qualification | body lines 108--122 | altered | Restore 13919--13938 verbatim. |
| 13939--13971 | IMLL grammar and every source rule, including identity/cut standing and structural-rule qualification | body lines 342--351; `handbook/registry/calculi/imll.tex:1--12` | altered, shortened, hybrid | Restore 13939--13971 verbatim as the inherited rule block.  A registry sheet with metadata and explicitized rules is not a literal copy. |
| 13972--14000 | commutative residuated partially ordered monoid definition; exact tuple, valuation equations, and sequent validity | substructural body lines 352--395 | altered, hybrid | Restore 13972--14000 verbatim.  Live lines 391--395 claim the paragraph is “verbatim,” but the live definition has rewritten prose, added necessity/standing commentary, and adds an empty-antecedent clause. |
| 14001--14015 | soundness/completeness/cut-elimination theorem and exact proof sketch | body lines 397--421; `handbook/annex/p08/substructural.tex:1--22` | shortened, altered, hybrid | Restore 14001--14015 verbatim. |
| 14016--14034 | exact counterexample algebra and valuations | body lines 423--434 | altered | Restore 14016--14034 verbatim. |
| 14035--14051 | exact four-rule bang extension and promotion side condition | body lines 436--451; `handbook/registry/calculi/ill-exponential-extension.tex:1--9` | altered, hybrid | Restore 14035--14051 verbatim as the unnamed source extension.  The source-syntax correction correctly warns against importing a different external presentation, but the live proof-boundary rewrite is still not the source text. |
| 14052--14068 | `\section{Relations among the systems}`; exact relevance/linear/Lambek comparison; resource warning | substructural body lines 716--873, mainly tables and new consequence discussion | shortened, altered, hybrid | Restore 14052--14068 verbatim as a contiguous source section. |
| 14069--14094 | four exercises | file header lines 6--9 says they are absorbed/recast | omitted | Insert 14069--14094 verbatim. |

### P8 decisive departures

1. Frozen IPL frames are partial orders (`source:13013`); live IPL frames are
   preorders (`handbook/parts/p08/intuitionistic-and-intermediate.tex:39--50`).
2. Frozen disjunction-property status is `Status: complete proof.`
   (`source:13184`) with the proof at 13187--13196.  Live lines 381--387
   replace that evidence status with a dependency/citation discussion.
3. The exact source T countermodel is deliberately replaced at
   `handbook/parts/p08/modal-logics.tex:610--614`.
4. The source complete finite-matrix proof is knowingly compressed
   (`handbook/annex/p08/many-valued-and-fuzzy.tex:2`).
5. The IMLL “verbatim” claim at
   `handbook/parts/p08/substructural.tex:391--395` is false at unit level: only
   some displayed equations survive literally.
6. Every inherited P8 exercise group is retired or absorbed rather than
   transcribed.

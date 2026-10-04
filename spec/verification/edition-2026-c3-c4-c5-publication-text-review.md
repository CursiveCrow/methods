# C3, C4 and C5: independent adversarial publication text review

Date: 7 September 2026. Repository: `C:/Dev/the-methods-of-reason`.
Observed HEAD: `35d537c692bb74b532dc4aa750da381a7fe4daf2`.
The working tree contains extensive existing changes; HEAD alone does not identify
the reviewed manuscript. The file hashes below identify this review's inputs.

## Verdicts

| Correction | Scoped verdict | Reason |
| --- | --- | --- |
| C3: CTL computation tree | **FAIL** | The corrected tree supports all four truth claims, but `EF` and `AF` have no explicit CTL abbreviation definition before the figure. The required repair is two definition equations. |
| C4 / R-032: finite full second-order arithmetic sentence | **PASS** | The seven closed conjuncts, symbol arities, full quantifier range, finite antecedent, and position before the reduction are explicit. |
| C5 / R-030: countable categoricity of DLO | **PASS** | The proof accounts for every finite-cut case, freshness, extension in both directions, the union, and existence of a countably infinite model. |
| C4 / S-013: analytic derivations | **PASS** | The definition precedes the chapter's substantive uses, distinguishes the propositional and first-order properties, and preserves the stated proof boundaries. |

These are verdicts on the specified body text and its relevant reading routes.
They do not accept all of C4, all of C5, R-030 or R-032 as complete requirement
packages. They are not a formal admission record or a publication verdict on the
rendered book. In particular, a PASS here does not close the integration observations
or production gates recorded below.

## Independence, method and configuration

The reviewer was the independent delegated agent
`/root/edition_small_publication_review`. No other reviewer report or author
verdict was consulted. No subagent was used. The exact model identifier,
reasoning-effort setting, runtime version and model deployment configuration were
not exposed in the reviewer-visible task configuration and are **unavailable**.

The governing amendment, `spec/EDITION-2026-CONTRACT.md`, was read in full. Its
lines 53–65 authorize direct active corrections while requiring preserved frozen
source and accurate attribution. Its lines 133–145 and 149–161 keep independent
reviews, production evidence and admission distinct. Old inventory and hash
records were not used as present admission evidence.

The review used actual LaTeX, manual evaluation of the displayed CTL structure,
inspection of the proof and definition statements, and a read-only traversal of
literal `input`, `include` and `showcalculus` commands from `handbook/main.tex`.
That traversal reached 842 distinct files and located the relevant labels and
consumers. It was a text route check, not execution of TeX conditionals or a
claim that all 842 files received substantive review. No manuscript build,
render, software test, or external-source research was performed.

The root integrator supplied the fact that the frozen source artifact is
preserved. This reviewer did not independently hash that artifact. The revised
active restoration files are treated here as corrected manuscript, not as proof
that their bytes still equal the historical source. External source fidelity,
copyright and source-acquisition completeness are outside this assignment.

## Reviewed snapshot and read extent

All four assignment hashes matched at initial inspection. They were rechecked
before submission, as recorded in the final verification note below.

| File under repository root | Read extent | SHA-256 |
| --- | --- | --- |
| `handbook/parts/p08/temporal-epistemic-supplement.tex` | Lines 1–380; decisive scope 46–104 and 329–353 | `3028f3196a8f8fc064a06e5e7aec3366fad90aa042fceaf0645825aa70eddb56` |
| `handbook/parts/p02/pa2-definition.tex` | Entire file, 1–42 | `6a5467b748c91f6cb9c8484e6c7e7b122a0268ecc80fc3a8c7213b92251d4a63` |
| `handbook/restoration/inherited-07295-07468.tex` | Entire file, 1–217; DLO theorem and proof 108–175 | `1958b3363dcac80b5c7af56f446e74591b4249d23c1c8543cc9ec7de7bb93a89` |
| `handbook/restoration/inherited-11711-11740.tex` | Entire file, 1–57 | `35225299698968b229674bdf96987d1fbde59dcecb15659c4615f18b27679c08` |
| `handbook/restoration/inherited-11824-11881.tex` | Entire file, 1–58 | `05cd142307a51b542a1a11f102fc76de4f1cf8e6843df2fe7c1afc42cb13e397` |
| `handbook/restoration/inherited-11882-11913.tex` | Entire file, 1–32 | `8dadda42399ae66736facb728ff48faffaa77aa1a9e08d2fce8bf98564e4a0e5` |
| `handbook/restoration/inherited-12415-12536.tex` | Entire file, 1–122; reduction 22–57 | `d4ff50a3145acac19b3e7a6054bcf0aef4aac1eb2e774f825ade02af2693f667` |

Additional content read for the verdicts: `inherited-12290-12355.tex` 1–66,
`inherited-12356-12414.tex` 1–59, `inherited-07150-07294.tex` 1–51,
`inherited-11354-11413.tex` 1–60, `inherited-11414-11505.tex` 1–92,
`inherited-11520-11598.tex` 1–79, `inherited-11599-11627.tex` 1–29,
`inherited-11741-11767.tex` 1–27, `inherited-11768-11823.tex` 1–56,
`inherited-13340-13409.tex` 1–70, and `inherited-13410-13439.tex` 1–30.
These paths are under `handbook/restoration/`.

The main and P2/P3/P7/P8 drivers were read in full. Relevant three-line restoration
wrappers were read, as were the CTL calculus sheet 1–15 and Part XIV rule-sheet
driver 1–100. Context inspected for navigation and integration included the P1
driver, P3 annex driver, P7 source map, P3 QE supplement 1–100, the retained but
unrouted P3 QE annex 1–18, the generated P7 register 1–48, targeted generated
symbol/theorem-index rows, P9 consumer lines 938–954 and 1000–1019, and the
definition/entry rendering macros in `handbook.sty` 425–502 and 1140–1164.

Selected dependency hashes:

| File | SHA-256 |
| --- | --- |
| `spec/EDITION-2026-CONTRACT.md` | `c9b101ad6bf6bfea5a3e1fbec25cdba81b47667146474861eb1aa00b5dfa1bf3` |
| `handbook/main.tex` | `511e6b538b89e6bf9541ac7dc564ebbaa7499d5991e18327c313453087c24761` |
| `handbook/parts/p02.tex` | `3576cc349c1245430b30531c266e0483144c5470b2f61a894c0d16d38522fbdd` |
| `handbook/parts/p03.tex` | `3694a5cde0762b4cf489aa640aeca2f00b9216bf16fe4bfa2a43e0fd4583ba69` |
| `handbook/parts/p07.tex` | `c3cbd4afb174e51b042a9a6b5cbf374b33428a47e69a66440660159100eadd31` |
| `handbook/parts/p08.tex` | `18a9d459d89930dd02ec3e337acb806e4a1eb307938e4cc4e699d42428b0af27` |
| `handbook/restoration/inherited-12290-12355.tex` | `dd9a1564fa0d18d05d5a9ff0adc5f67b3accf6f9cf465a8efb1016a12d4da1b0` |
| `handbook/restoration/inherited-12356-12414.tex` | `3b850ff37842e3e024ac32b23712aa199db010ad2249e764bb590afc2ed89a04` |
| `handbook/restoration/inherited-11768-11823.tex` | `a248a9312df24072b30435ab996e241415c725d40edadd15905fd317eb3392cf` |
| `handbook/registry/calculi/hilbert-ctl.tex` | `d8213c581d16700e21c5295f996501c14d0f25968382f394df3e93690e6a717c` |

The P2 driver hash is an observation, not an assertion that its unrelated
earlier inputs are immutable. During review, a separate writer inserted
`parts/p02/propositional-substitution` at line 7. The initial driver hash was
`bf76eb346924365e7d06eb3596cf22b266d61ea6ff24096b6c527fd9f8151e0c`.
The unchanged PA2 seam shifted from lines 50–53 to lines 51–54. The table records
the final observed driver hash, and the relevant final seam is:

```tex
\input{restoration/scope-SRC-12290-12355} % p02.tex:51
\input{restoration/scope-SRC-12356-12414} % p02.tex:52
\input{parts/p02/pa2-definition}         % p02.tex:53
\input{restoration/scope-SRC-12415-12536} % p02.tex:54
```

## C3: CTL computation tree

**Verdict: FAIL for definition before use. The truth-value correction passes.**

The local semantic prerequisites identify a nonempty total transition structure,
valuation and infinite path before the figure (`temporal-epistemic-supplement.tex`
46–56). The next clauses at 69–75 quantify over the immediate successors. The
strong-until clauses at 80–99 include position zero and require eventual success.

The root is explicitly labelled `w: not p` at 332. Its two immediate successors
are `u:p` and `v: not p` at 333–334. The continuing branches at 335–344 and the
caption at 349–351 make the left branch always satisfy `p` after the root and the
right branch always fail `p`, without introducing terminal states. Therefore:

| Figure claim at `w` | Direct check |
| --- | --- |
| `EX p` is true | Successor `u` satisfies `p`. |
| `AX p` is false | Successor `v` fails `p`. |
| `EF p` is true, under its intended until abbreviation | The left branch reaches `p` at position 1. |
| `AF p` is false, under its intended until abbreviation | The right branch never reaches `p`, including position 0. |

The notation gap is precise. The CTL grammar and semantic definition at 58–104
introduce `EX`, `AX`, `E(A U B)` and `A(A U B)`. They do not define `EF` or `AF`,
which appear at 346. The earlier LTL definition of `F` in
`inherited-13340-13409.tex` 56–61 is for the infinite-word language; it does not
declare the paired CTL abbreviations in this CTL grammar. The CTL* grammar likewise
does not explicitly add them to CTL.

The exact missing equations do exist at `registry/calculi/hilbert-ctl.tex` 5–6,
but that sheet is rendered in Part XIV by `parts/p14/rule-sheets.tex` 78.
The earlier CTL card's `entrycalculus` at 113 prints only a hyperlink, as confirmed
by `handbook.sty` 1148–1152. A later P9 occurrence explicitly explains the
abbreviations at `parts/p09/logic-in-computer-science.tex` 1011–1012. These routes
confirm the intended meanings but do not supply the requested definition before
the P8 worked example.

**Required repair C3-PUB-1:** add the two eliminable CTL abbreviations
`EF A := E(top U A)` and `AF A := A(top U A)` to the CTL definition before the
figure. Retain the current corrected root and continuing branches. Re-review
the affected definition and figure at the resulting frozen hash.

The active label `fig:p08-ctl-tree` is attached to the corrected figure at 352.
Its earlier card reference at 121 and the P9 reference at 948 reach that active
definition. The similarly named figure in the older
`parts/p08/temporal-dynamic-epistemic.tex` is not on the inspected active route.
No layout, clipping or float-placement conclusion is made from the TikZ source.

## C4 / R-032: the finite arithmetic antecedent

**Verdict: PASS. No body-text repair required in this scope.**

The title and opening (`pa2-definition.tex` 3–8) specify that `PA_2` is one finite
sentence: the conjunction of seven closed sentences in the stated signature.
The constant and unary/binary function arities are explicit. The displayed list
contains two successor axioms, one second-order induction sentence, two addition
recursions and two multiplication recursions (11–23). Every displayed object
variable is quantified and the induction relation variable is quantified.

Lines 26–31 state that `X` is unary, quantify it over every subset of the nonempty
domain, and require total function interpretations. They also distinguish this
single induction sentence from a first-order induction scheme. Lines 33–39
identify the successor-only predecessor and explain exactly what the four
arithmetic conjuncts add. This prevents a silent change of signature when
forming `PA_2 -> sigma`.

Both references resolve to earlier active sections: full semantics is in
`inherited-12290-12355.tex` 1–40, and successor categoricity plus its arithmetic
extension statement is in `inherited-12356-12414.tex` 4–58. The P2 seam above puts
the definition immediately before `inherited-12415-12536.tex`. The reduction's
use at 36–44 consequently has a previously specified finite antecedent.

The addition is a definition, not a newly asserted complete proof of the
noneffective-completeness result. The latter still has a proof-sketch heading
at `inherited-12415-12536.tex` 35 and explicit omitted-proof boundaries at 45–57.
This review does not close that separate full-proof obligation. The finite
construction and its immediate use provide the needed illustration; no invented
additional numerical example is required to understand the notation.

The active `def:p02-pa2` is provided by the new file at line 3. The old definition
with that label in `parts/p02/second-and-higher-order-logic.tex` is not on the
inspected route. The file header points to correction provenance outside the
reader's derivation and does not describe the new seven-conjunct display as an
unchanged historical quotation.

## C5 / R-030: countable categoricity of DLO

**Verdict: PASS. No repair required to the theorem or proof at 108–175.**

The earlier DLO declaration in `inherited-07150-07294.tex` 30–31 fixes nonempty
dense linear orders without endpoints in the signature `{<}`. Categoricity is
defined at `inherited-07295-07468.tex` 4–9, including model existence; finite
partial isomorphisms and the back-and-forth method precede the theorem at
24–75. The corrected theorem therefore does not rely on an undefined use of
categoricity or silently omit its existence condition.

The proof's local notation is introduced before use: the finite map `g:A -> B`
and the new element `a` occur at 123–125, and the finite lower/upper image sets
`L` and `U` are defined at 126–129. Their disjointness, partition of `B`, and
separation are justified at 130–133. Lines 135–146 handle two nonempty sides,
lower side only, upper side only and both sides empty. The nonempty-domain
condition is expressly used in the final case.

Freshness is proved at 148–150. Preservation and reflection of order, old-pair
retention and the new finite bijection are then checked at 151–154. The back
step uses the inverse map, the corresponding hypotheses in the other structure,
and inversion of the extension at 156–161. The union argument at 163–169 proves
functionality, injectivity, totality, surjectivity, and preservation/reflection
for arbitrary pairs. It does not merely assert that alternating extensions
somehow produce an isomorphism.

Finally, lines 169–174 supply the countably infinite rational model: enumeration
by integer/positive-integer pairs, midpoint density and explicit witnesses to
both endpoint conditions. Together with uniqueness, this meets the earlier
definition of categoricity. The complete-proof status at 112 is supported by
the displayed proof within this bounded theorem. It does not upgrade the
nearby cited Ryll–Nardzewski or Morley results at 187–210.

The P3 driver inputs the corrected range at line 58, and the theorem retains
`thm:dlo-countable-categorical` at line 109. The active named-theorem index points
to that label at `generated/named-theorem-index.tex` 113. The supplemental
`annex/p03/qe-categoricity-games-supplement.tex` was inspected as a possible
consumer, but the actual P3 annex driver does not input it. Its retained
derivation and OPEN note were not used as active evidence or admission.

## C4 / S-013: analytic derivations

**Verdict: PASS. No body-text repair required in this scope.**

The definition is placed immediately after the cut-elimination chapter heading
at `inherited-11711-11740.tex` 4–30, before the later claim that cut elimination
yields analytic derivations (`inherited-11882-11913.tex` 4–8). The prior P7
calculus chapter already defines contexts, derivations, cut-freeness, the
primitive rules, defined negation and the quantifier side conditions.

The propositional clause requires both cut-freeness and the literal subformula
property, computed after the chosen calculus's abbreviations are expanded
(5–9). That qualification agrees with the displayed calculi, where negation is
an abbreviation for implication to falsity (`inherited-11414-11505.tex` 64–66;
`inherited-11520-11598.tex` 76–78).

The first-order clause expressly works modulo capture-avoiding term substitution
and bound-variable renaming (11–18). It explains that removal of an outer
quantifier frees the relevant variable in the selected subformula. Terms and
eigenparameters remain subject to the actual rule language and freshness
conditions. The `P(t)`/`forall x P(x)` example at 20–23 directly demonstrates why
literal subformulas are insufficient. Lines 23–27 prevent a false inference to
finite first-order proof search or an automatic extension theorem.

The later propositional subformula lemma is explicitly propositional and has
its own direct rule-inspection proof (`inherited-11824-11881.tex` 6–18).
The following existence corollary remains a proof sketch at 20–33, explicitly
depending on the earlier sketch of cut elimination. The first-order qualification
at 35–41 agrees with the new definition. The subsequent discussion at
`inherited-11882-11913.tex` 4–18 retains the calculus and efficiency limitations;
the exercise at 27–31 asks for the propositional/first-order distinction. The
new definition therefore does not turn those broader results into complete proofs.

The route is `parts/p07.tex` 99, then 100–101 for cut/mix and cut elimination,
then 102–103 for the specified later uses. The live
`def:p07-analytic-derivation` is at the new definition's line 4. The similarly
labelled old `parts/p07/cut-elimination-and-interpolation.tex` is not input on
the inspected route. The new `hbdefinition` uses the separate plain-entry
renderer (`handbook.sty` 481–496); it does not add a native `definition`
environment to the P7 source-unit hook sequence.

## Integration observations outside the four body verdicts

The active P7 generated theorem/definition register has no row for
`def:p07-analytic-derivation`: its displayed sequence proceeds from earlier
calculus additions to Formula rank and derivation height
(`generated/audit-p07.tex` 29–40). The label exists in the body, but lookup
coverage for this addition has not been completed. The governing amendment
requires generated lookup to follow admitted projections (155–158), so this is
a pending integration obligation, not evidence that the definition is admitted.

The active P3 QE supplement still calls the preceding chapter “exact inherited”
at `parts/p03/qe-categoricity-games-supplement.tex` 3–7. Its body now contains
direct corrections, including this expanded DLO proof. Before publication,
align this attribution wording with the governing amendment's distinction
between preserved frozen source and corrected active manuscript. The proof
itself makes no verbatim-source claim. This observation does not require
restoring an erroneous historical proof.

The generated PA2 symbol rows describe a “full second-order Peano theory”
(`generated/symbols-tables.tex` 162; `generated/symbol-index.tex` 484), while the
new precise local notation denotes its finite conjunction. Their explanation
does acknowledge the four recursion axioms. Review those downstream names and
targets during lookup integration so the definition's sentence/theory
distinction remains clear across the reference. This is not a defect in the
seven displayed conjuncts or their active placement.

## Remaining gates and final verification

Required before the C3 body verdict can pass: implement C3-PUB-1 and obtain a
fresh review of its changed scope. The other three PASS verdicts remain bounded
to the hashes and dependencies identified here; semantic or relevant route
changes require reassessment.

Full visual inspection remains **pending** for every scope. No claim is made
about pagination, mathematical line breaking, figure size, font embedding,
index rendering, link destinations in a compiled PDF, or float placement.
Build, scoped production checks, independent source/topic reviews, actual
admission records, broader C4/C5 obligations, full-book validation, and human
editorial acceptance remain separate gates.

Final verification at 2026-09-07 07:40:34 -07:00: all seven primary content
hashes in the first table still matched. The PA2 driver seam retained the same
four adjacent inputs in the same order, at the shifted lines recorded above.
The report's recorded file hashes were then compared with the current files;
the P2 observation was updated and a report transcription error was corrected.
Only this report was created or edited by this reviewer.

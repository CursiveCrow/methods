# NOW-03a / PT-1: numeral and atomic proof-builder construction

Date: 7 September 2026, America/Los_Angeles; 8 September UTC.
Standing: author draft, returned for independent review. The scoped mathematical
construction is supplied; this note records its exact identities and interfaces.
It is not an independent acceptance or admission record.

## Returned files and author standing

| File | Extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p05/pa-numeral-proof-builders.tex` | 490 lines | `E805B3D17CC04419E9105BDC98A5B42483E91DE90137358669019D0F23D4858F` |
| `handbook/annex/p05/pa-numeral-proof-builders.tex` | 628 lines; six complete annex items | `576AD536A4F7484FF2E2968B3C32FB6D685C0288B16A9007B4E89A7234B0B65A` |

Author assessment: **PASS for the construction supplied in NOW-03a**, subject to
fresh independent source/dependency, mathematical and adversarial publication
review. No required case of the promised numeral/literal construction remains
an author-identified mathematical gap. Independent acceptance, production and
admission are **UNRESOLVED** until their separate gates are performed.

Only the two files above and this intake note were written. Accepted text,
restoration files, drivers, bibliography, symbols and admission records were
preserved. No tests, new test code, manuscript build/render or subagents were
used. After a usage interruption, the parent explicitly dispatched a fresh
bounded authoring block; the returned work belongs to that resumed block.

## Exact dependency reading

The following are actual content reads, not conclusions inherited from review
reports. All seven required mathematical files were read completely. A first
combined output was truncated, so subsequent individual/range reads filled its
missing extent, including the exact substitution-machine declaration.

| Dependency | Read extent | SHA256 of whole file |
| --- | --- | --- |
| `spec/EDITION-2026-CONTRACT.md` | Complete, 1–168 | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `spec/EDITION-2026-WORK-PACKAGES.md` | Relevant assignment context, 233–278 of 794, including NOW-03a–d | `F49DE88FC33093390FD0CC377E7647019F74FD0529F7DCC07B503E559545160E` |
| `handbook/parts/p05/pa-checker-arithmetization.tex` | Complete, 1–523 | `993418B3EB3343525C0922274CA6794F5B4FED13FFB35CB146E9995D88391DFA` |
| `handbook/annex/p05/pa-checker-arithmetization.tex` | Complete, 1–537 | `03BAF39D646901DC307812B0D22FE8823CFEC53B3D7B85A3FF0ADF754AAF71E5` |
| `handbook/parts/p05/standard-pa-proof-predicate.tex` | Complete, 1–252 | `71D3E5569BFB7BAE907CA818BE65DBBCE5E48DBA86D9D8942819DCC5110331E2` |
| `handbook/annex/p05/standard-pa-proof-predicate.tex` | Complete, 1–315 | `7F3E3F751832ACACFFC8F2383E2AC14A8D8DC7A9DEA2DA4B837F3A9DF648DFDF` |
| `handbook/restoration/inherited-09262-09327.tex` | Complete, 1–253 | `B49A3B30AFF36050841D4F384A6BA80FCF36F4661B3C4085E58D2371B4E003CB` |
| `handbook/restoration/inherited-09328-09438.tex` | Complete, 1–546 | `A6E37FA592E81B888C14A2DA97CC70F1A05EC69BAE0CE4D36E2E60C59F09C541` |
| `handbook/annex/p05/internal-proof-predicate.tex` | Complete, 1–524 | `F11B72E5AE8FF2407C58FA434320D08095C0C543AE8C610237EED42EAFFFA1C1` |
| `handbook/restoration/inherited-08306-08438.tex` | Necessary arithmetic-language, comparison and hierarchy context, 1–70 of 133 | `0B020970BE72999CD771566BA0D6CDB4E4668728362CBD3C0D1606059EE9D2B8` |
| `handbook/restoration/inherited-09112-09149.tex` | Complete, 1–38, consulted for the literal weak-comparison convention | `23A060D7646D1BBB54480F35833F2D40A78180E67A36232CF8406D7E71B3FBAE` |

The mathematical evidence is the actual accepted constructor and graph text.
No source acquisition or new bibliography entry is needed for this editorial
deduction from those fixed definitions. The Rosser fragment was consulted for
its witness-on-the-left convention; its external finite case enumeration was
not used as an internal proof-builder theorem.

## Supplied components

| Component | Author assessment | Exact body/proof entry and supplied construction |
| --- | --- | --- |
| Internal substitution prerequisite | PASS | `thm:p05-builder-nocapture` / `annex:p5.builder-nocapture`: a new fixed table returns success, substitution result and exact command cost for the no-renaming cases. A PA induction proves an execution equation for the actual selected substitution machine, then its output agrees with the table within the actual `20(nodes(c)+1)^2` bound. |
| Raw rule joins | PASS | `thm:p05-builder-row-templates` / `annex:p5.builder-row-templates`: fixed joins of arity 0–3 copy and offset each row block, append the actual rule row and prove successful row bits, parent counts and the exact shifted open-list update. This supplies the intermediate open-formula extension beyond the sentence-root guard of `mp_19`. |
| Equality operations | PASS | Same entry: identity, symmetry, transitivity, and the needed successor/addition/multiplication congruences have explicit tag-18/tag-19 records, fresh numerical hole indices, matrices and premise order. No implicit equality inference is used. |
| Arithmetic axiom instances | PASS | `def:p05-builder-axiom-instances`: each use begins with its exact unmarked `q_j` leaf, then performs one or two tag-13 rows in outside-in binder order, carrying the actual matrix and term codes. |
| Derived left-addition constants | PASS | `thm:p05-builder-left-addition` / `annex:p5.builder-left-addition`: explicit raw records `D_Z,D_L` prove `forall x_0 (0+x_0=x_0)` and `forall x_0 forall x_1 (Sx_0+x_1=S(x_0+x_1))`. The records use the specified matrices `m_Z,m_L`, canonical leaves `IndAx(m_Z,0), IndAx(m_L,1)`, one nonvacuous temporary assumption in each step, and actual introduction/elimination rows. Their conclusions never become new axiom leaves. |
| Numeral arithmetic | PASS | `thm:p05-numeral-arithmetic-builders` / `annex:p5.numeral-arithmetic-builders`: exact addition and multiplication recurrences produce proofs of the literal numeral equations; right and left successor-string recurrences provide the open-variable equations needed by comparison refutations. All have PA graph/row/leaf invariants. |
| Disequality and contradiction | PASS | `thm:p05-numeral-literal-builders` / `annex:p5.numeral-literal-builders`: a fixed `b`-step successor-peeling recurrence uses actual `q_2` instances and raw MP, then a `q_1` instance and tag 10. Ordered disequality branches preserve and discharge the original equality assumption. |
| Weak and strict comparisons, both signs | PASS | Same entry: positive comparisons supply their explicit difference witnesses by tag 14; negative comparisons use an explicit eigenvariable, a marked major and minor, right/left addition and peeling, then tag 16 and tag 9. The stronger all-variable condition is checked against every remaining leaf. |
| Fixed terms and literal transport | PASS | `thm:p05-fixed-term-literal-builders` / `annex:p5.fixed-term-literal-builders`: a separate finite description per fixed term evaluates and proves its numeral instance; two explicit equality-elimination joins transport a normalized signed literal back to its exact original numeral-instance code. |

The six result statements have six reciprocal proof annex items. The last item
also proves finite-description formation and all conditional success outputs.
Every named description follows the accepted projection/composition/primitive-
recursion convention; there is no uniform evaluator over descriptions and no
proof search.

## Exact record and variable conventions

The final record remains `N_19(N_15(R),0)` for the selected
`Gamma_{d_19}(p,x,1)` checker. Outer tag 19 and equality-elimination rule tag 19
have their distinct existing roles. Raw rows remain `[r,a,J,U,l]`.

Each join copies the supplied premise records into disjoint intervals. Premise
indices receive their cumulative row offsets; rule parameters, assumption
markers and formula codes retain their values. A new row consumes each old
root once. Repeated terms or repeated uses of a derived proof insert copied
trees, so the construction never introduces a row with two parents.

The instance and rule table explicitly fixes these tags: assumption 0,
conjunction introduction 1, implication introduction/elimination 7/8,
negation introduction/elimination 9/10, universal elimination 13,
existential introduction 14, universal introduction 15, existential elimination
16, equality introduction/elimination 18/19. It uses the selected
antecedent-before-implication order of tag 8 and positive-before-negative order
of tag 10. Every supplied matrix, replacement term, binder, hole and discharge
label appears in the corresponding parameter list.

The surviving leaf list is a subset of the explicit nine-entry list
`[q_1,q_2,q_3,q_4,q_5,q_6,q_7,I_Z,I_L]`. Every leaf is unmarked. All of those
literal accepted sentences have only indices 0 and 1 in their all-variable
sets. Intermediate derived formulas with an eigenvariable remain raw derivation
roots until the later record closes them; they are never silently treated as
sentence proofs.

For a comparison with binder `i`, the negative constructors use eigenvariable
`i + 3`. Their major existential assumption has label 0, stored marker 1;
their minor equality has label 1, stored marker 2. Existential elimination
removes the minor nonvacuously and tests the eigenvariable against the major,
bottom conclusion and all remaining open formulas. It is absent from all
indices 0/1 in the axiom leaves and differs from binder `i`. Negation
introduction then removes the surviving major assumption. Existing internal
discharges in copied derived proofs stay confined to their original branches.

## Two literal conventions that must survive integration

The comparison constructors deliberately preserve the actual inherited
expansions:

`Le_i(t,u) = exists x_i (x_i + t = u)`

`Lt_i(t,u) = exists x_i (t + Sx_i = u)`

The strict witness is on the right of addition; the weak witness is on the
left. The left-addition derived records supply the extra direction needed for
negative strict comparisons. An unspecified use of commutativity as a proof
step would not give the promised records.

The original comparison binder is fixed when the original terms are expanded,
using their declared least-absent-variable convention. Numeral substitution
retains it. A new least variable is not selected after the terms become
closed numerals. This matters for literal root codes even when the resulting
sentences would be alpha-equivalent. The normalized comparison builders
therefore take `i` as an explicit numerical parameter, and literal transport
uses a distinct fresh hole.

## Zero and empty cases supplied

Addition at right argument zero uses the actual `q_4` instance. Multiplication
at zero uses the actual `q_6` instance. The successor-string base cases are
`t + 0 = t` and the explicit derived `0 + t = t`. The contradiction builder
at peeling bound zero performs no `q_2` step and directly uses `q_1`.

Equal numerals use premise-free identity; disequality has zero failure value
on equal inputs. Weak comparison at equal endpoints uses witness zero.
Strict comparison at equal endpoints is refuted by a positive successor
after peeling, including `m = n = 0`. The two-row proof of negated bottom
has an empty final axiom list. Positive bottom has a zero-valued builder and
only the logically vacuous conditional correctness assertion.

An empty tuple of free parameters gives a nullary fixed description and an
empty outer universal prefix. Empty premise and open lists use the actual
list code zero and the actual empty product one; a successful raw proof
itself always remains nonempty. No least element of an empty witness set or
predecessor of zero is introduced.

## Scoped text check

The existing per-file scanner in `tools/check.py` was run on these two files,
using `_hb_scan_file` after its existing comment/verbatim stripping. Its source
identity was SHA256
`05F22DEE54E3F177EAD79DFAE16D88787E513A58441F443278679F8BC7443914`.
The final run returned:

```text
Findings: {}
Result statuses: 6
Annex items: 6
Reciprocal proof pairs: True
```

This is the narrowly scoped text scan: it checks the authored environment,
label, source-alias and local proof-apparatus conventions that its existing
per-file routine covers. The reciprocal pairs were also inspected in its
harvested result/annex data. It is not a whole-book static run, build,
rendered-page inspection, mathematical test or independent review. The Python
invocation used `-B`; no test file or bytecode artifact was created.

## Integration intake for the lead

The lead owns both new input routes and all shared records. Place this body
after the accepted direct-checker arithmetization and its annex after that
checker's annex; retain its six reciprocal result/annex pairs. There is no
bibliography addition or source-file correction in this component.

The local code notation needing the lead's typed symbol intake includes
successor/addition/multiplication code constructors `s,a,b`, `Eq`, `Neg`,
`bc`, `All`, `Ex`, code conjunction/implication, `entry`, `nodes`, `it`,
`pack`, `nc/ns/cost`, the raw join and row templates, `m_Z,m_L,I_Z,I_L`,
`D_Z,D_L`, the fixed accepted-leaf list, the four arithmetic raw builders,
the peeling/Clash builder, the signed numeral-literal builders and
`t^#`, `t^nu`, `R_t`. Existing `nu`, constructor, checker and graph meanings
are retained. The note does not mutate the symbol registry or assert that
those shared intake steps have already occurred.

## Precise next dependency

NOW-03b must construct the proof records for each fixed bounded formula from
these literal builders. It must give the connective cases and actual bounded
existential/universal cases, including the zero bound, dependent witnesses,
freshness and nonvacuous discharge. In particular, a list of proofs of numeral
instances is not yet a proof of a quantified formula: an explicit finite-case
enumeration builder and the derivation combining it with those instances are
still needed. The older external case-enumeration proof does not supply that
internal builder invariant automatically.

The new substitution theorem covers precisely the no-renaming inputs required
here, including arbitrary formulas with closed replacements and all
quantifier-free contexts. A later call involving genuine binder renaming must
either establish its no-conflict hypotheses after a proved freshness
construction or supply the relevant additional internal machine invariant.

After reviewed NOW-03b, NOW-03c must compile evidence for each required fixed
Sigma1 sentence and instantiate the literal selected provability sentence.
NOW-03d then repairs and reviews the actual consumers. The bounded compiler,
evidence-to-proof invariant, D3, PT-1 closure and the separately owed GL and
Solovay developments remain open. This completed literal component closes
none of those later obligations by itself.

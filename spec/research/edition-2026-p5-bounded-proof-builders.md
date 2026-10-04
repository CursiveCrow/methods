# NOW-03b: fixed bounded-formula proof constructors

Author return, 7 September 2026 Pacific time / 8 September UTC. This is an authored manuscript snapshot for independent review. It is not text acceptance, admission, PT-1 closure, or a D3 claim.

## Returned manuscripts

| File | Lines | SHA-256 |
| --- | --- | --- |
| `handbook/parts/p05/pa-bounded-proof-builders.tex` | 486 | `8345A3C2C7702A5DD039BA6068CEBD7C0B69D2ABE387FB6FDFB29A5E46AFE480` |
| `handbook/annex/p05/pa-bounded-proof-builders.tex` | 676 | `0C3D2614397C7CF68D4B32E0179E4A023EB460A8815EAE67E58836326DFA260A` |

The author owns these two files and this note. Shared routes, bibliography, notation registry, correction records and admission records remain with the lead integrator.

## Actual governing inputs read

The approved `spec/EDITION-2026-CONTRACT.md`, NOW-03b in `spec/EDITION-2026-WORK-PACKAGES.md`, and `spec/verification/edition-2026-p5-numeral-text-acceptance.md` govern scope. The complete current numeral body and annex were read and their exact accepted hashes rechecked:

| Dependency | SHA-256 |
| --- | --- |
| Numeral body, 501 lines | `413117B591123F5B12C78124D1EC13ACE9B15CB3CBB61445DBE9CB6ED8F97BD0` |
| Numeral annex, 644 lines | `3ABD15F81D47E8D5078C46B496DFBE4361ECBF36C25C54CB589CD9D7DC84237E` |
| `handbook/parts/p05/pa-checker-arithmetization.tex` | `993418B3EB3343525C0922274CA6794F5B4FED13FFB35CB146E9995D88391DFA` |
| `handbook/annex/p05/pa-checker-arithmetization.tex` | `03BAF39D646901DC307812B0D22FE8823CFEC53B3D7B85A3FF0ADF754AAF71E5` |
| `handbook/parts/p05/standard-pa-proof-predicate.tex` | `71D3E5569BFB7BAE907CA818BE65DBBCE5E48DBA86D9D8942819DCC5110331E2` |
| `handbook/annex/p05/standard-pa-proof-predicate.tex` | `7F3E3F751832ACACFFC8F2383E2AC14A8D8DC7A9DEA2DA4B837F3A9DF648DFDF` |
| `handbook/annex/p05/internal-proof-predicate.tex` | `F11B72E5AE8FF2407C58FA434320D08095C0C543AE8C610237EED42EAFFFA1C1` |
| `handbook/restoration/inherited-09262-09327.tex` | `B49A3B30AFF36050841D4F384A6BA80FCF36F4661B3C4085E58D2371B4E003CB` |
| `handbook/restoration/inherited-09328-09438.tex` | `A6E37FA592E81B888C14A2DA97CC70F1A05EC69BAE0CE4D36E2E60C59F09C541` |

The actual marked-bound expansions and syntactic hierarchy were additionally read at `handbook/restoration/inherited-08306-08438.tex:28–94`, SHA-256 `0B020970BE72999CD771566BA0D6CDB4E4668728362CBD3C0D1606059EE9D2B8`. A comparison used as an auxiliary literal block is not reclassified as a primitive bounded atom. No new external source acquisition or bibliography entry was needed for these deductions from the specified calculus and accepted constructors.

## Supplied construction

Five result/proof pairs supply the full assigned fixed bounded-formula scope:

1. `thm:p05-bounded-logical-templates` / `annex:p5.bounded-logical-templates`: exact new row templates, an explicit RAA proof of excluded middle, and a conjunction/projection operation retaining an otherwise unused assumption for nonvacuous implication introduction.
2. `thm:p05-bounded-sum-exhaustion` / `annex:p5.bounded-sum-exhaustion`: two specified recursions proving that either addend of a sum equal to a numeral is one of the indicated numerals. The second orientation uses the actual copied `D_Z,D_L` proofs. The stage supplies zero and predecessor branches, q1/q2/q3 instance chains, existential elimination, excluded-middle elimination and both universal introductions.
3. `thm:p05-bounded-range-exhaustion` / `annex:p5.bounded-range-exhaustion`: strict-sum exhaustion and exact exhaustion implications for both original comparison orientations, including strict bound zero and weak bound zero.
4. `thm:p05-bounded-case-elimination` / `annex:p5.bounded-case-elimination`: a primitive recursion over disjunction cases with explicit equality elimination, followed by an actual proof of the original quantified formula. The bound term is normalized inside its temporary guard; the conclusion retains the original term and binders.
5. `thm:p05-fixed-bounded-builders` / `annex:p5.fixed-bounded-builders`: the separately fixed Boolean and positive/negative proof descriptions, all eleven connective branches, all four bounded-quantifier sign cases, the two PA proof-construction assertions, exact literal substitution and dependent witness/bound handling.

The output invariant is the accepted `Safe(R,c)`: the actual selected row/tree tests, exact root, and only unmarked leaves from the nine-entry `A_*` list. That list's axiom tests and all-variable support `{0,1}` are inherited unchanged. The constructor recurrences are verified by PA induction; the output trees require no new induction-axiom family. Every new existential-elimination witness is checked against all variable occurrences of its major, conclusion and remaining leaves.

The six accepted equality/comparison literal roots are reused through the actual packed-literal decoder. Raw MP is antecedent then implication; the explicit packed identity reverses its two arguments to match `mp_19`. The finite list of matrix proofs is used only as premises of the constructed case-elimination tree. It is never treated by itself as a universally quantified derivation.

## Direct checks and review focus

The author directly checked the constructor equations, q1/q2/q3/q4/q5 and copied left-addition instances, both sum orientations, exact ordered row parameters, zero branches, repeated markers in separate branches, literal numeral substitution, and the all-variable versus free-variable side conditions. One displayed parenthesis and a local formula name that collided with the addition-code constructor were corrected before the recorded snapshot. Long connective rows were separated into complete displayed clauses. These are author checks of the written mathematics. No software tests, scanner, build or render was run in this block.

Independent review should especially verify the q3 minor in the sum recursion, the reversed-addend weak comparison, the self-substitution identity used by `Cases`, the original guard retained by `U`, and the two-copy minor in the negative existential. The argument deliberately avoids alpha conversion when restoring the final binder. In the strict comparison helper, fresh outside binders are instantiated only after the arithmetic proof is closed, avoiding substitution of index 1 into the surviving binder-1 arithmetic axiom matrix.

## Root-owned integration and notation intake

Insert the body after `pa-numeral-proof-builders.tex` in the existing P5 body route, and its annex after the matching numeral annex. The sections are `sec:p05-pa-bounded-proof-builders` and `sec:annex-p05-pa-bounded-proof-builders`. All five result environments point to their matching annex items. There are no source-only label aliases or new LaTeX macro definitions.

New notation families, all local to this P5 construction:

| Family | Definition label | Role |
| --- | --- | --- |
| `G_<`, `G_≤` | `def:p05-bounded-builder-conventions` | Exact marked comparison guards with a retained supplied binder |
| code `c | d` | `def:p05-bounded-builder-conventions` | Disjunction code `N_9(c,d)` |
| `P_0`, `P_1`; `OL`, `OR`, `OE`; `EF`, `RA`, `Keep` | `def:p05-bounded-builder-conventions` | Raw row templates and assumption retention |
| `EM` | `def:p05-bounded-em-template` | Explicit excluded-middle tree |
| `D(t,n)` in calligraphic type | `def:p05-bounded-sum-exhaustion` | Left-associated finite equality disjunction, with bottom at zero |
| `g_ε`, `Z_ε`, `S_ε` | `def:p05-bounded-sum-exhaustion` | Two fixed addition orientations and actual axiom/derived instances |
| `C_ε`, `F_ε` in upright type | `def:p05-bounded-sum-exhaustion` | Exhaustion recursions and their explicitly specified stage |
| `CS`; `E_<`, `E_≤`; `N_<`, `N_≤` | `def:p05-bounded-range-exhaustion` | Strict sum, comparison exhaustion, and strict/weak case counts |
| `Cases`, `CI`; `U_<`, `U_≤` | `def:p05-bounded-case-elimination` | Finite case derivation, its implication, and quantified derivation |
| `b_φ`, `φ^ν`, `R_φ^±`, `d_φ^±` | `def:p05-fixed-bounded-builders` | Fixed Boolean description, literal instance code, raw and packed signed builders |

`Safe`, `A_*`, the numeral/code operations and old row templates retain their accepted definitions; they are not redefined as new proof predicates. Local stage letters and temporary trees are defined at their uses. Root should register the genuinely new families with their typed scope and check collisions through the existing shared intake.

## Continuation

No omitted constructor within NOW-03b's fixed bounded-formula scope is identified in this authored return. Independent source, topic and publication text reviews remain required. Integration, notation projection, scoped production and formal admission remain open. After valid dependency acceptance, NOW-03c must use this exact selected predicate and construct every evidence-to-original-sentence clause, including unbounded existential introduction, before deriving D3. NOW-03d and the separately owed GL/Solovay work remain subsequent obligations.

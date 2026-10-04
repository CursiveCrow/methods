# P5 coding and Kamp III.1: independent publication-text review

Review date: 7 September 2026. Reviewer: fresh independent publication-text context, not an author of the three targets. Authoritative repository: `C:\Dev\the-methods-of-reason`. Assigned window: 20:02–20:32 UTC.

## Verdict

**FAIL for publication integration of this snapshot.** Two actionable findings remain: the later PA claims require more than the newly fixed proof-formula definition supplies, and the new Kamp coincidence entry has an incorrect precedence rank.

| Scope | Verdict | Extent |
| --- | --- | --- |
| P5 explicit coding, syntax operations, derivation checker, and numerical proof equivalence | PASS | Complete target text read; no publication-text defect found in the construction or its stated standard-model result. |
| P5 distinction between numerical proof relation and arithmetic representing formula, within the target | PASS | The distinction and the cited representability dependency are explicit. |
| P5 integration with the later assertions about the exact PA provability formula | FAIL | Finding PT-1: the selector in the definition is insufficient for the downstream unconditional PA claims. |
| Kamp III.1 definitions, complete proof text, examples, and sentence corollary | PASS | Publication-text assessment of the stated linear-order result and the separate starred rendition. |
| Canonical notation additions and isolated generated notation views | FAIL | Finding PT-2: the coincidence abbreviation is assigned implication precedence. The generated table faithfully repeats that error. |
| P5 theorem anchor, Kamp body input, and Kamp theorem/annex textual links | PASS | Targets and matching IDs are present on the inspected driver route. This is a source-text navigation result. |
| Primary-source identity and exact source fidelity | UNRESOLVED by this review | Assigned to the separate source review. No other P5/Kamp review or author conclusion was consulted. |
| Build, rendered-page quality, formal verification, admission, and release | UNRESOLVED by this review | No test, build, manuscript render, or formal checker was run. Text review establishes none of these gates. |

The edition contract requires distinct content, source, output, and admission evidence (`spec/EDITION-2026-CONTRACT.md:133–168`). The PASS entries above do not establish complete P5, N-c-012, Kamp III.2, or handbook acceptance.

## Findings

### PT-1 — The chosen numeralwise representative does not determine a PA predicate satisfying D1–D3

Severity: major. Scope: P5 definition-to-consumer integration.

The new definition at `handbook/restoration/inherited-09328-09438.tex:472–493` fixes a specific Sigma-zero-one formula by the sole requirement that it numeralwise represent the certified numerical proof relation in Q. It correctly says that the checker construction does not establish the internal derivability conditions. This is adequate for the local standard-model coding theorem.

The live continuation nevertheless says that **PA and its fixed proof predicate satisfy all three derivability conditions**, referring to precisely that definition (`handbook/restoration/inherited-09750-09816.tex:7–11,41–44`). `handbook/parts/p05/provability-logic-gl.tex:45–63` likewise fixes the exact formula obtained from that definition and asserts GL arithmetical soundness for it. These are stronger claims about the selected arithmetic formula, not consequences of the numerical checker or of numeralwise representation alone.

There is an explicit reason the missing selection condition matters. Suppose PA is consistent, let `b` be the code of its fixed contradictory sentence `bottom_A`, and let `R(p,x)` be any Sigma-zero-one formula numeralwise representing the target numerical proof relation in Q. Define

\[
\widehat R(p,x)=R(p,x)\land x\ne\overline b,
\qquad
\widehat{\mathrm{Prov}}(x)=\exists p\,\widehat R(p,x).
\]

This is still a Sigma-zero-one numeralwise representative of the **same numerical relation**. For standard `x` different from `b`, Q proves the numeral inequality and the original representation clauses apply. For `x=b`, consistency means that no standard proof code belongs to the numerical relation, and Q proves the negation of the displayed conjunction directly. Thus this choice satisfies every stated selection condition in the target definition.

But PA proves `not widehat{Prov}(bar b)` directly, because the formula contains `bar b != bar b`. If this predicate satisfied all three derivability conditions, the manuscript's own conditional Loeb theorem and second incompleteness theorem would force a contradiction (`handbook/restoration/inherited-09817-09876.tex:4–58`; `handbook/restoration/inherited-09877-09924.tex:4–27`). Consequently the current selection rule permits a representative for which the later unconditional PA assertion fails.

Required correction: fix a particular arithmetic construction with sufficient internal properties and justify D1–D3 for that exact PA formula, or give the downstream standard PA predicate a separate precise definition and establish the required bridge. Merely adding another standard-model correctness statement, another citation about standard predicates in general, or repeating the target's disclaimer does not resolve the selection problem. The local coding theorem can retain its existing bounded claim.

Acceptance consequence: the checker theorem can receive a bounded text PASS while the exact-formula PA and GL uses remain open. The issue does not refute the certified numerical proof relation or Kamp III.1.

### PT-2 — Kamp coincidence is registered at implication precedence

Severity: moderate. Scope: canonical notation and its isolated table projection.

`handbook/registry/symbols.csv:905` assigns precedence `6` to the two-variable abbreviation `x \doteq y`. The isolated generated table repeats `6` at `tmp/edition-2026-p5-kamp-candidate/symbols-tables.tex:885`.

The normative precedence account says that smaller numbers bind more tightly, puts declared atomic relations at rank `2`, and puts implication at rank `6` (`handbook/parts/p01/symbol-registry.tex:101–105,120–135`). The new abbreviation combines two variables into the formula `not(x<y) and not(y<x)` (`handbook/parts/p09/presentations/kamp-iii1-normal-form.tex:12–24`). Its operands are variables, not formulas. Giving it implication rank misdescribes how a prefix comparison combines with a conjunction; for example, `x \doteq y \land P(z)` must group as `(x \doteq y) \land P(z)`, not take a formula as its right operand.

Required correction: give this relation abbreviation rank `2`, or supply an explicit equally precise local grammar that overrides the general precedence account and record that grammar consistently. Update the corresponding isolated table projection. The collision with the preexisting unification use of `\doteq` at CSV line 179 is already semantically distinguished by the new role and notes; that typed reuse is not the defect.

Acceptance consequence: the new entry and generated table do not pass publication notation review in this snapshot. This is a registry error; it does not refute the parenthesized Kamp proof transformations.

## Positive checks and precise boundaries

### P5 construction

The construction defines its arithmetic language and actual natural-deduction calculus before encoding them. It gives distinct symbol, token-string, tree, derivation-row, proof-certificate, and alpha-comparison roles. The positive cons constructor, empty list, projections, child-code inequality, arities, malformed defaults, and literal-symbol tokens are present (`inherited-09328-09438.tex:11–83`).

Primitive recursiveness is argued through the declared closure operations and explicit iteration bounds. The parsing bound is numerical rather than a complexity claim. Numeral substitution and arbitrary term substitution are treated separately; the latter preserves the previously defined least-fresh-variable convention, including renaming when the substituted variable is absent. The alpha records retain free indices and nearest-binder positions and include both directions of the syntactic equivalence argument (`:85–222`). The imported substitution definition and alpha-equivalence generator agree with these clauses.

All twenty rule tags are checked. Parent indices and parent counts give a connected tree; open lists preserve assumption occurrences and branch ownership. The discharge filters are formula-specific and nonvacuous. The implication-elimination premise-order difference between body and rule sheet is explicitly translated. Universal introduction checks free-variable absence; existential elimination checks all-occurrence absence from the conclusion, major premise, and surviving assumptions. Equality and alpha conversion use the imported rules (`:224–319`; `handbook/registry/calculi/nd-fol.tex:9–29`).

The theory is a c.e. set of axiom sentences with a fixed domain index, rather than being silently identified with its deductive closure. The fixed bounded computation formula supplies numerical acceptance certificates. The text distinguishes evaluating that one fixed formula from a uniform arithmetic truth predicate. Certificate lists have exactly one witness per surviving open axiom leaf, and empty proof contexts and the separately fixed finite-theory convention are handled (`:321–370`).

The proof establishes both extraction of a derivation from a successful check and construction of a certified code from a finite derivation (`:391–470`). The primitive-recursive numerical statement and the subsequent cited numeralwise-representation choice are explicitly separated (`:472–501`). The prime-power example is labelled as a separate illustration rather than silently replacing the governing constructor coding (`:372–389`); the two exercises preserve the requested number/formula/provability distinctions (`:503–519`).

### Kamp III.1

The host introduces the equality-free language, unary predicates, nonempty order domain, order classes, and the map D before the input at `n-c-012.tex:138`. The new body states that III.1 needs arbitrary strict linear orders, with possible endpoints and empty open intervals; completeness is reserved for the later task.

The body defines temporal prefixes, ordered equality blocks, name-order representatives, point-order essential variables, the one-variable prefix, recursive regional classes, standard formulas, and standard sentences before using them. Literal source constants and order-defined starred constants occupy distinct classes. The epsilon conversion is explicitly a conversion of distinguished constant slots, with truth preservation and the possible addition of P0 stated openly (`kamp-iii1-normal-form.tex:11–191`).

The annex was read in full. Its opening explicitly changes the component-class scope to starred classes before suppressing the stars. It proves the ordered-partition facts and quantifier-free basis, both equality cases for existential elimination, all three strict positions, and retention of witness existence in an empty-dependent-conjunction case (`annex/.../kamp-iii1-normal-form.tex:13–171`).

For universals it includes every residual prefix and all `2s+1` positions, including absent groups. The equality-position components use surviving representatives. Positive Boolean distribution introduces no negated regional components. The all-dependent, all-independent, and mixed strict-position cases are proved separately; the all-independent case retains the empty-region disjunct. Finite-stage membership and final redistribution are stated (`:173–324`).

The proof then establishes effectivity, exact free-variable retention, and the starred predicate-support property; converts to the literal source grammar; and gives the complete structural sentence-corollary argument (`:326–380`). The finite, endpoint, integer-gap, rational-gap, and universal empty-region examples have the stated truth values (`body:193–223`). The final body paragraph limits the result to III.1 and its sentence corollary (`:225–231`). No acceptance of III.2 follows from this review.

### Notation and navigation

All canonical CSV lines 888–916 and amended line 57 were read individually, not sampled. Their numerical/formula distinctions, constructor arities, binder-record exception, finite-theory convention, exact endpoints, source/starred classes, and support claims agree with the relevant target definitions, subject to PT-2.

Preexisting macro-role collisions were searched across the earlier CSV rows. The directly overlapping broad roles include `r,t`, `T,U`, `s`, the unification `\doteq`, and the temporal-path `\pi`; the added local declarations type the new uses. Other reused letters, including `V`, `W`, `\nu`, `\ell`, `\varepsilon`, and `h`, have declared distinct local roles. The normative registry explicitly permits named presentations to retain typed local notation (`handbook/parts/p01/symbol-registry.tex:6–26`; `handbook/CONVENTIONS.md:210–222`). No additional undeclared semantic collision was found in the appended entries.

Every corresponding line for registry ID 00057 and IDs 00888–00916 was read in both isolated generated views. They preserve the canonical roles and notes; the table exposes the PT-2 rank. These are text comparisons, with no assertion about page layout or generation/admission gates.

The P5 hook is active only around `scope-SRC-09328-09438`, resets its local counter, and anchors the first theorem in that scope. The inspected target contains one theorem, Arithmetization of syntax. The scope wrapper inputs the target. Kamp's theorem ID and its `proved=annex:p9.kamp.iii1` status match the annex item; the host input and P9 annex driver input are present.

## Read ledger

Intervals are one-based physical text lines. A complete read means every line in that interval was returned and read; search hits elsewhere are identified separately.

| File | Read interval or method |
| --- | --- |
| `spec/EDITION-2026-CONTRACT.md` | Complete, 1–168. |
| `handbook/restoration/inherited-09328-09438.tex` | Complete, 1–180, 181–360, 361–519. |
| `handbook/parts/p09/presentations/kamp-iii1-normal-form.tex` | Complete, 1–231. |
| `handbook/annex/p09/kamp-iii1-normal-form.tex` | Complete, 1–195, 196–380. |
| `handbook/registry/symbols.csv` | Header 1–2; 50–65; 880–916; 8–18; 79–86. Earlier rows searched for each new macro token and additionally for coincidence, Lin, epsilon, nu, constructor/normal-form families, and component notation; every returned collision row was read. |
| `tmp/edition-2026-p5-kamp-candidate/symbols-tables.tex` | 391; 414–429; 884–896, all complete rows. |
| `tmp/edition-2026-p5-kamp-candidate/symbol-index.tex` | Complete selected rows 35, 69, 97, 143, 147, 211, 215, 251, 354, 482, 518, 580–584, 587, 589, 594, 599, 614–615, 618–619, 734, 754, 827, 844, 852, 896. |
| `handbook/parts/p05.tex` | Complete, 1–52. |
| `handbook/restoration/scope-SRC-09328-09438.tex` | Complete, 1–3. |
| `handbook/parts/p09/presentations/n-c-012.tex` | 1–146, including the input and the beginning of the subsequent III.2 boundary. No separate III.2 construction target was read. |
| `handbook/annex/p09.tex` | Complete, 1–7. |
| `handbook/restoration/inherited-03038-03104.tex` | Complete, 1–67. |
| `handbook/restoration/inherited-03105-03165.tex` | Complete, 1–61. |
| `handbook/restoration/inherited-03240-03428.tex` | Complete, 1–189. |
| `handbook/restoration/inherited-02193-02340.tex` | 1–87. |
| `handbook/restoration/inherited-03927-04061.tex` | Complete, 1–135. |
| `handbook/registry/calculi/nd-fol.tex` | Complete, 1–29. |
| `handbook/restoration/inherited-07678-07752.tex` | 1–55. |
| `handbook/restoration/inherited-08710-08876.tex` | 800–925, bounded-verification theorem/proof and boundary. Earlier full computation-formula construction was not independently rereviewed. |
| `handbook/restoration/inherited-09262-09327.tex` | Complete, 1–66. |
| `handbook/restoration/inherited-09498-09538.tex` | Complete, 1–41. |
| `handbook/restoration/inherited-09750-09816.tex` | 1–49. |
| `handbook/restoration/inherited-09817-09876.tex` | Complete, 1–60. |
| `handbook/restoration/inherited-09877-09924.tex` | Complete, 1–48. |
| `handbook/parts/p05/provability-logic-gl.tex` | 31–68, plus explicit proof-predicate search hits. |
| `handbook/parts/p01/symbol-registry.tex` | 1–44; 100–142. |
| `handbook/CONVENTIONS.md` | 210–225; notation and scope search hits. |
| `handbook/handbook.sty` | 635–675; 1380–1427; theorem-counter and hook search hits. |

Additional searches located prerequisite labels, proof-predicate consumers, driver inputs, and symbol collisions. They did not establish complete review of their containing files. No other P5/Kamp review conclusions, integration conclusions, or candidate README conclusions were read. An unrelated prior N-c-016 memory entry was consulted only for review-discipline guidance; all findings above arise from the current files.

## Snapshot hashes

SHA-256 values were computed directly from the live files. The four assigned hashes matched before substantive review.

| File | SHA-256 |
| --- | --- |
| `handbook/restoration/inherited-09328-09438.tex` | `0E4AC6AD0D39474E49D2F868C62877FD7A0F1F1EEC61E24D77D806E266D81B9C` |
| `handbook/parts/p09/presentations/kamp-iii1-normal-form.tex` | `0D1EB5FC960B7F0F1EB216026AF2AAF953CD3D95F62E4ACF014345611D860B31` |
| `handbook/annex/p09/kamp-iii1-normal-form.tex` | `A46BFF4D11C868E8A865F2F9CC89690FCB4D03A550EB6CCB755B4C067A3B7F8B` |
| `handbook/registry/symbols.csv` | `4981FF83BEE5C147046161E8505FA6DD02D135365C3E386264423FC9E80B0CF7` |
| `spec/EDITION-2026-CONTRACT.md` | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `handbook/parts/p05.tex` | `068B90E56BFCF4538AFF14F0DBBF428A228A34B12736CA55484B1E3D5E64B326` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `A12201D510F6FE514BC4300F65A34AAA10B0DE0429979ABD10D8BE8F07AE4E5E` |
| `handbook/annex/p09.tex` | `107245B68DC1A7E9E95B78AA4D3D84643A22AD05B44CBEFDA5E3E807D2DE19BA` |
| `tmp/edition-2026-p5-kamp-candidate/symbols-tables.tex` | `223B5C85AB6213AAE1704794AAC45B314879CAE8E514939B2C354A4283DFB780` |
| `tmp/edition-2026-p5-kamp-candidate/symbol-index.tex` | `905BD47714D79C3C41C05D881C62009CA3267B6522B8D9FD75FD1EBB39706BE9` |
| `handbook/restoration/inherited-09750-09816.tex` | `EFA16565DC4206D722BA62585AA452A86394B5827C84B6201C6340815062D2DE` |
| `handbook/parts/p05/provability-logic-gl.tex` | `9AD6D30124B666C8845B421FA40BED296CC59621D0F733C7053581C870EF183E` |
| `handbook/parts/p01/symbol-registry.tex` | `A95B36D13BA4C61ADEF116BE5E439E43CB21B210130F14BDFE55DA773A21C8DA` |
| `handbook/CONVENTIONS.md` | `4293F514072179A5AC95E64FA8D8F37E23FFE2693814A1980E5801BABA5B7242` |

The review report's own hash is supplied in the delivery message rather than embedded into its own hashed content. Only this review report was authored in this review context.

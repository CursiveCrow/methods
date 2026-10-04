# Independent mathematical review: C4 / S-013

## Verdict: PASS

The new definition of analytic derivations at `handbook/restoration/inherited-11711-11740.tex:4–30` is mathematically appropriate for the displayed Part VII calculi. It distinguishes the propositional subformula condition from the first-order condition modulo term substitution, respects the existing primitive syntax and quantifier rules, and occurs before the dependent uses. It introduces no false generalization or new claim that the cut-elimination proof is complete.

No blocking mathematical finding or unresolved inference was found within this correction's scope. This verdict does not establish a complete cut-elimination theorem, independent source fidelity, formal admission, or publication acceptance.

## Reviewer, snapshot, and independence

Reviewer: Codex collaborator `/root/edition_small_topic_review`. The actual backend model identifier and reasoning configuration were not exposed; both are unavailable. This was an independent agent mathematical review, not human review.

The review began at 14:24 UTC on 2026-09-07 in `C:/Dev/the-methods-of-reason` and was completed at 14:30 UTC, before the 15-minute checkpoint and within the 30-minute limit. The primary file matched the assigned SHA-256 `35225299698968b229674bdf96987d1fbde59dcecb15659c4615f18b27679c08`; its hash and both dependent-file hashes were checked again unchanged at completion. The complete primary file, both specified dependent files, and the relevant displayed calculus rules were read. No other reviewer report or correction-author verdict was consulted. The earlier C3/C4/C5 report was not changed.

Only this review file was created. No manuscript edits, tests, builds, renders, formal proof-checker runs, or external source searches were performed. The archived source was not required to decide this mathematical question and was not read or compared.

## 1. Exact calculus and primitive syntax

The scope is explicit: the title says “in the displayed calculi,” and line 5 says “In this chapter.” The relevant source calculus uses finite-multiset contexts, defined at `inherited-11354-11413.tex:29–34`, and the LJ succedent contains exactly one formula at lines 51–58. The definitions of derivation and cut-freeness are at `inherited-11506-11519.tex:1–13` and `inherited-11599-11627.tex:1–12`.

The LK rules actually displayed in `inherited-11414-11505.tex:4–66` have implication, conjunction, disjunction, and bottom, with negation explicitly defined by `not A := A -> bottom` at line 64. The corresponding LJ surface is at `inherited-11520-11598.tex:4–48,69–78` and has the same negation abbreviation. Accordingly the new definition's instruction at lines 7–9 to compute subformulas in the primitive syntax after expansion is necessary and correct. For example, the expanded formula `not P` is `P -> bottom`, whose subformulas include both `P` and `bottom`; the literal characters of an unexpanded abbreviation do not determine the primitive subformula set.

The active reader supplement explicitly distinguishes this inherited defined-negation LK presentation from canonical LK at `parts/p07/calculi-and-derivability-supplement.tex:49–61,97–110,120–145`. It gives no transfer of cut-freeness from derivability equivalence. The new chapter-local definition does not change that distinction or bring primitive-negation or equality rules into the displayed calculus. The extension boundary at new lines 25–27 and `inherited-11882-11913.tex:14–18` is consistent with that scope.

## 2. Propositional analytic derivations

New lines 5–9 impose two conditions on a derivation: it is cut-free, and every formula occurrence is a subformula of an endsequent formula. This is a definition of a property of derivations; it does not itself assert that every derivable sequent has such a derivation.

The displayed cut-free propositional rules support the subsequent lemma. In every noninitial rule, each premise formula is either a context formula retained in the conclusion or a constituent of the conclusion's principal formula. Contraction copies a formula; weakening adds a conclusion formula without introducing a new premise formula. The zero-premise identity and bottom-left rules contribute no additional upward step. Following a premise occurrence toward the endsequent and using transitivity of the subformula relation therefore gives the stated property. This directly supports the complete local lemma at `inherited-11824-11881.tex:6–18` for these exact rules.

The existence claim for an arbitrary derivable propositional sequent additionally needs cut elimination. The dependent corollary at `inherited-11824-11881.tex:20–33` explicitly retains “Status: proof sketch” and identifies the omitted cut-reduction case table. The new definition leaves that dependency intact.

## 3. First-order instances, exposed variables, and capture avoidance

New lines 11–18 state a weaker syntactic restriction appropriate to first-order quantifier rules: each occurring formula is, up to bound-variable renaming, a capture-avoiding term-substitution instance of an endsequent subformula. The opening primitive-syntax convention continues to apply to these first-order versions of the same calculi.

The term qualification agrees with the four quantifier rules at `inherited-11414-11505.tex:71–91` and `inherited-11520-11598.tex:50–68`. Their premise matrices are `A[t/x]` or `A[y/x]`; the matrices need not be literal subformulas of the quantified conclusion. Other premise formulas are context copies. Repeated quantifier steps use finite compositions of the permitted term substitutions. After avoiding bound-variable clashes, these again give term-substitution instances of the relevant endsequent subformulas. Taking a subformula inside such an instance cannot introduce a new logical connective; its free term positions come from the corresponding original subformula, with a removed quantifier's variable exposed for further instantiation.

The clarification at new lines 14–16 handles the critical binding issue correctly. For example, although `x` is bound in `forall x P(x)`, the subformula `P(x)` considered as a formula on its own has `x` free. Substituting `t` therefore gives `P(t)`. Without the “on its own” clarification, substitution into the entire quantified formula would stop at its `forall x` binder and would not represent this rule instance.

Capture avoidance is also substantive. For the subformula `forall y R(x,y)` exposed from `exists x forall y R(x,y)`, replacing the free `x` by the variable `y` gives `forall z R(y,z)` with a suitably fresh `z`, not `forall y R(y,y)`. This is exactly the operation defined in `inherited-03240-03428.tex:20–49` and illustrated at lines 82–90. Its alpha-equivalence definition at lines 67–80 explains the new qualification “up to bound-variable renaming.” Renaming a binder is not permission to capture an inserted free variable.

Thus the new text agrees with the first-order qualification at `inherited-11824-11881.tex:35–41`. It neither asserts a literal first-order subformula property nor treats arbitrary new logical formulas as allowed instances.

## 4. Eigenparameters, freshness, and the example

New lines 16–18 restrict terms and eigenparameters to the language allowed by the selected quantifier rules and require every inference's own freshness conditions. For the displayed rules, the eigenparameter is the variable `y`: in `forall R` and `exists L`, it must not occur **free** in the conclusion sequent. These are the exact conditions at `inherited-11414-11505.tex:89–91` and `inherited-11520-11598.tex:66–67`. A variable's bound occurrence in the conclusion is not prohibited by that condition. The definition neither substitutes a stronger absence-of-all-occurrences condition nor permits freshness to be repaired after an invalid inference.

The wording also does not authorize adding new function symbols or constants to a fixed language. “Eigenparameters” remains subject to the selected rules; in the rules reviewed here it is implemented by variables, not an unrestricted fresh-constant convention.

The example at new lines 20–23 is correct: in `forall L`, the premise occurrence `P(t)` is a term instance of the matrix `P(x)`, which is a subformula of `forall x P(x)` on its own. No eigenvariable condition is imposed on `t` by this rule, although it must be a permitted term. The example does not assert that `P(t)` is always a literal subformula.

New lines 23–25 correctly say that the permitted instances **can** be infinite. For instance, a fixed signature with constant `c` and unary function `f` permits the distinct instances `P(c), P(f(c)), P(f(f(c))), ...`. The definition therefore supplies no claim that this first-order condition alone makes proof search finite or efficient. This agrees with `inherited-11882-11913.tex:10–12`.

## 5. Input order and proof standing

The driver `handbook/parts/p07.tex:88–103` routes the calculus definitions and reader comparison before the new chapter, inputs `scope-SRC-11711-11740` at line 99, then the cut/mix material and cut-elimination sketch, and then the two specified dependent files at lines 102–103. The inspected wrapper files directly input the named bodies. Within the primary file the new definition is immediately after the chapter heading and before “Measures on cuts,” so the technical term is defined before its substantive downstream use at `inherited-11882-11913.tex:4–8`.

The proof status remains differentiated:

- `inherited-11824-11881.tex:6–18` contains a complete local propositional subformula lemma, supported by inspection of the displayed rules.
- `inherited-11768-11823.tex:11–55` expressly presents cut elimination as a proof sketch and says that the calculus-specific commuting and principal reduction table is omitted.
- `inherited-11824-11881.tex:20–33` and `43–57` retain proof-sketch status for corollaries depending on that omitted table.
- New lines 25–27 refer to the subsequent arguments “at their stated proof status”; they add a definition and scope qualification, not the missing table or a new completeness certificate.

The first-order instance check above validates the definition against the rules. It is not a review of every quantifier cut reduction, their permutation conditions, or termination of the mix-elimination procedure. In particular, this PASS does not upgrade the cut-elimination sketch to a complete proof.

## Consulted ranges and SHA-256 values

Paths in this table are relative to `C:/Dev/the-methods-of-reason`. “Full” records a complete, untruncated reading of that file; mathematical endorsement remains limited to C4 / S-013. Surrounding theorems were read for conventions and proof standing, not independently certified.

| File | Read range | SHA-256 |
| --- | --- | --- |
| `handbook/restoration/inherited-11711-11740.tex` | Full, 1–57; new definition 4–30 | `35225299698968b229674bdf96987d1fbde59dcecb15659c4615f18b27679c08` |
| `handbook/restoration/inherited-11824-11881.tex` | Full, 1–58 | `05cd142307a51b542a1a11f102fc76de4f1cf8e6843df2fe7c1afc42cb13e397` |
| `handbook/restoration/inherited-11882-11913.tex` | Full, 1–32 | `8dadda42399ae66736facb728ff48faffaa77aa1a9e08d2fce8bf98564e4a0e5` |
| `handbook/restoration/inherited-11354-11413.tex` | Full, 1–60 | `6b78f7cb5ddd41a567cf5e069a6455a0b1904160efa3a6d654ff32fcb40ea1ce` |
| `handbook/restoration/inherited-11414-11505.tex` | Full, 1–92 | `ab5d1828c32f3bed1e953b0d9c28318d373321072b1e7d58838fe8836914fa5a` |
| `handbook/restoration/inherited-11506-11519.tex` | Full, 1–14 | `541da0cdc43bbb3e03bc284c1f5820f02f43c5c0d4573212c0b01a0686a12e0b` |
| `handbook/restoration/inherited-11520-11598.tex` | Full, 1–79 | `b362565e6bf07e84e579d24db76de640f5e182a0d3cc22342a759476901bbd46` |
| `handbook/restoration/inherited-11599-11627.tex` | Full, 1–29 | `e114da56c0409379984e0457cb7a711f223dc6c3daa49e82c99d6d7bc476847e` |
| `handbook/restoration/inherited-11628-11644.tex` | Full, 1–17 | `4dcb612e872772d63fbe1d36b68246b827466eac259a15c049c39f8fe51e701e` |
| `handbook/restoration/inherited-11645-11695.tex` | Full, 1–51 | `493ed0b31ddd58d432ec802102360618cf96ed3c42a9a6de20376592b5cacc70` |
| `handbook/restoration/inherited-11696-11710.tex` | Full, 1–15 | `c46fe1d6ade46fc4a2f79e8a87fb095ff627e6eb3fdfc560ef036b3550aafecf` |
| `handbook/restoration/inherited-11741-11767.tex` | Full, 1–27 | `836bee04978eb0cd02da2f92d22cef015400c4342271008baac067591d572cd0` |
| `handbook/restoration/inherited-11768-11823.tex` | Full, 1–56 | `a248a9312df24072b30435ab996e241415c725d40edadd15905fd317eb3392cf` |
| `handbook/parts/p07.tex` | Full, 1–129; relevant route 88–103 | `c3cbd4afb174e51b042a9a6b5cbf374b33428a47e69a66440660159100eadd31` |
| `handbook/parts/p07/source-map.tex` | Full, 1–21 | `c8e2c7e52ba9a96ce42e2c606cf41bd13f9e951a61cdd9d0b0e7ea3abd7cbf8d` |
| `handbook/parts/p07/calculi-and-derivability-supplement.tex` | Full, 1–298; naming/scope focus 49–61, 97–145 | `f109a14f4b1b068229c0b1069c65af0b3491ea1d06e3722296145491b7f2a235` |
| `handbook/restoration/inherited-03240-03428.tex` | 1–90 | `36d7779d6b9bb3caf0c4ef514a79a1c7d8aa10bd4a72290256ea1d09d5db58cc` |
| `handbook/restoration/scope-SRC-11414-11505.tex` | Full, 1–3 | `73dd4d6e979759d155128d5dfe12d393fa7c7c4c0968343d3b1d74ec2eafa7ce` |
| `handbook/restoration/scope-SRC-11520-11598.tex` | Full, 1–3 | `0d1531e0b2f63ba802d6ae58fc825bd2a95adf7f4b9cf1f5eb819ed8b23e7ac8` |
| `handbook/restoration/scope-SRC-11711-11740.tex` | Full, 1–3 | `b7818806dd2d77219f8d18f4e789fb57cc842c5307db6ff28fc0cb1467948052` |
| `handbook/restoration/scope-SRC-11824-11881.tex` | Full, 1–3 | `1194b89ec3952fc757c128f62946e5afcb35da751055df4fe115c8728ab717d8` |
| `handbook/restoration/scope-SRC-11882-11913.tex` | Full, 1–3 | `28618b93104beaf831bcac6c57e65036ea6967ce2d04ac71bcc570c85fc5beae` |
| `handbook/handbook.sty` | Incidental scope-mechanism read: 1220–1275 and 1370–1425 | `1b5c089594010dd517389cdf510cdfbf741e014eaac877cc5bb44f3991412288` |

There is no unread range in the assigned primary or dependent files. Of the additional substitution file, lines 91–189 were not read. Of the style file, lines 1–1219, 1276–1369, and 1426–1826 were not read. Other manuscript files surfaced only by targeted searches are not claimed as reviewed. The archived `source/formal-logic-reference.tex`, including lines 11711–11913, was not read; no archived-source comparison is claimed.

## Remaining gates

Source fidelity and provenance, edition admission, static checks, build, rendering, visual inspection, formal proof checking, and human review are not established by this scoped mathematical review. Completing cut elimination still requires the omitted calculus-specific reduction and termination verification at its own review scope. No correction to the new analyticity definition is requested by this report. Any later primary-file change requires checking the applicability of this verdict.

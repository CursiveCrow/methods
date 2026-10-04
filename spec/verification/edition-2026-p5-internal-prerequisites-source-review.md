# P5 internal prerequisites: independent source and local compatibility review

Date: 7 September 2026. Reviewer: fresh independent source/local compatibility context, `/root/p5_internal_prerequisites_source_review`.

Assignment window: 21:19–21:44 UTC, with a 15-minute checkpoint. Target and dependency reading completed and blind findings prepared by 21:26 UTC. The checkpoint was supplied early. Root: `C:\Dev\the-methods-of-reason`; branch: `phase4-codex`; HEAD: `35d537c692bb74b532dc4aa750da381a7fe4daf2`. The reviewed content is the live, substantially modified working tree at the hashes below, not merely HEAD.

## Verdict and scope

**PASS for the assigned source and local compatibility scope.** No source-attribution error, changed local premise, incompatible formula interface, or mistaken transfer from standard-model coding to an internal PA theorem was found in the frozen targets. The original PA deductions are compatible with the declared local arithmetic, syntactic hierarchy, pairing/beta formulas, primitive-recursion class, and natural-deduction rules.

The particular PA checker description, its selected representing formula, internal D2, the evidence-to-proof construction for D3, and the dependent standard-predicate/GL obligations remain **UNRESOLVED**. None receives a PASS here. This report does not supply topic-specialist acceptance, publication review, build or rendered-page evidence, formal admission, or user acceptance.

The new arithmetic proofs were reviewed as original manuscript deductions from the stated local premises. They were not evaluated as purported transcriptions of Shoenfield, Gödel, or another external author. The unchanged Q representability theorem remains expressly cited; its external complete proof was not reacquired or independently reconstructed in this bounded assignment. No concrete attribution discrepancy required new acquisition.

The complete edition contract was read before the substantive review. In particular, its direct-correction rule, retained proof obligations, distinction between original reconstruction and historical attribution, fresh independent review requirement, and separate admission gates govern this report. No new reviewer conclusions or author assessment were read before filing these findings. Only this report was written; no manuscript files, tests, builds, PDFs, generated material, or other review reports were changed.

## Frozen targets and preservation checks

All target lines were read, with these exact file hashes:

| Target | Read interval | SHA-256 |
| --- | --- | --- |
| `handbook/restoration/inherited-09262-09327.tex` | 1–253, complete | `b49a3b30aff36050841d4f384a6ba80fcf36f4661b3c4085e58d2371b4e003cb` |
| `handbook/restoration/inherited-09328-09438.tex` | 1–546, complete | `a6e37fa592e81b888c14a2da97cc70f1a05ec69bae0ce4d36e2e60c59f09c541` |
| `handbook/annex/p05/internal-proof-predicate.tex` | 1–524, complete | `c653bf3e1a42e541310435aaa9082238df6b78eedd349400dd252ed26a5083f2` |

**PASS — representation-prefix preservation.** The exact bytes through the line terminator of line 66 of `inherited-09262-09327.tex` hash to `75a27e87080116a235a904daedabe2a70dff472ba27ca8a454c448dfd4b58bb6`, exactly the assigned original fragment hash. The appended construction starts at line 67. The Q representation definitions, cited theorem, construction paragraph, addition example, and original line endings in that prefix therefore survive the byte check.

**PASS — coding-file preservation outside D1.** Removing exactly the new lemma block at lines 496–522, beginning with the D1 lemma declaration and ending with its following blank line, recovers 519 lines with SHA-256 `0e4ac6ad0d39474e49d2f868c62877fd7a0f1f1eec61e24d77d806e266d81b9c`. This is the assigned previous coding hash. The preservation computation was performed in memory and did not write a reconstructed manuscript file.

## Component findings

### 1. Arithmetic premises and the actual pairing/beta formulas — PASS

The annex states its use of the seven arithmetic axioms and full induction with universally closed free parameters at lines 5–13. This matches `inherited-09099-09111.tex:1–13`, where Q consists of seven universally closed axioms, and `inherited-09175-09187.tex:2–12`, where PA adds induction for every arithmetic formula with its parameters universally closed.

The addition and multiplication manipulations in annex lines 15–43 use the right-recursion axioms actually declared in Q and invoke PA induction where uniform algebraic identities are required. The unrestricted formula complexity of least-number arguments and finite collection is licensed by that full induction scheme. These arguments are not claimed in Q.

The numerical pairing in `inherited-01101-01147.tex:25–46` is `(a+b)(a+b+1)/2+b`. The governing arithmetic graph is the atomic doubled equation in `inherited-08439-08709.tex:1–25`. Annex lines 74–95 establish totality, uniqueness, inverse components, and bounds for that same equation, using a triangular-value relation whose elimination is explained. No arithmetic division function is added to the language.

The actual beta formula at `inherited-08439-08709.tex:27–54` decodes `w` as a pair `(t,m)` and takes the remainder of `t` modulo `1+(i+1)m`. Its quantifiers are `t<Sw`, `m<Sw`, `q<St`, and the marked remainder comparison. Annex lines 97–106 use precisely that orientation, divisor, and set of bounds. The internally derived `q<=t`, component bounds, and equivalence of the marked remainder comparison supply the existing formula's witnesses. The case `m=0`, giving divisor one, is explicitly included.

There is no appeal here to the preceding standard-model beta theorem as if it already asserted internal PA totality or extension.

### 2. Internal beta extension and finite collection — PASS

Annex lines 109–143 spell out the congruence and signed-coefficient abbreviations as arithmetic formulas on natural-number pairs. The Bézout argument uses the internally justified least-number and division principles. The two-modulus step and the coprime-product observation then support the extension induction.

At lines 158–164, the common multiple is obtained by an induction on the upper divisor bound before any factorial or coded product is used. At lines 166–173, divisibility of the index difference and the chosen common multiple gives pairwise coprimality of the actual moduli `1+(i+1)m`. At lines 175–194, target entries are an arithmetic relation with a unique value at each index, and the induction invariant quantifies over its values. Thus this stage does not assume a previously coded list of those values.

The final pairing at lines 196–202 has its first component equal to the combined residue and its second equal to the common multiple. This agrees with the governing beta formula. The bounds in the extension statement preserve every prior entry because the earlier PA beta lemma already bounds every old entry by the old code. The empty-prefix case is stated explicitly.

Finite collection at lines 205–227 applies that extension lemma to one newly selected witness. It then uses the new code's component bound to obtain the new bounded witness quantifiers. The version for a weak upper bound follows by replacing the length by a successor. Full PA induction permits the stated arbitrary arithmetic `R`; no restriction to decidable or bounded relations was silently introduced.

### 3. Specified primitive-recursive graphs and recursion invariant — PASS

The arities and recursion-argument order in `inherited-09262-09327.tex:76–115` match `inherited-07678-07752.tex:4–29`: zero is available at every finite arity, including zero; projections require a positive arity; composition permits a nullary outer function; recursion uses `g(x)` and `h(x,n,f(x,n))`.

The description index is explicitly a fixed finite metalinguistic tree. The output graphs use the actual beta formula, fresh auxiliary variables, and only the stated initial/composition/recursion clauses. The recurrence stores the base at position zero, uses transitions at `i<n`, and reads the output at position `n`. The annex proof at lines 229–276 matches those positions: the successor construction extends at `Sn`, preserving the entire earlier prefix, and restriction needs no new code because only a prefix is constrained.

The graph theorem's PA totality/uniqueness, internal defining equations, standard-model graph equivalence, and standard-numeral representation are given separate arguments. The numeral argument at annex lines 294–303 uses a standard finite unfolding plus the proved universal uniqueness assertion. It does not claim that this PA argument replaces the cited Q theorem.

The invariant corollary at representation lines 160–185 requires actual PA proofs of its base and step implications. Its induction formula and its use of the graph equations agree. Truth of the invariant premises in the standard structure is expressly insufficient.

Both the body at lines 151–158 and the annex at lines 305–310 exclude a uniformly PA-total evaluator over all primitive-recursive descriptions and leave the actual proof-checker constructors/invariants for subsequent work. Those exclusions match the strength of the fixed-description construction.

### 4. Pairing/cons graph example — PASS

Representation lines 187–233 give finite descriptions for addition, triangular numbers, pairing, and positive cons in dependency order. Their argument positions agree with the established primitive-recursion convention. The displayed `K(a,b)` computes the triangular value at `a+b`, then adds `b`, exactly the governing pairing. `C` is its successor, exactly the positive list constructor of coding lines 24–43.

The internal graph identifications invoke the already established PA triangular uniqueness and pairing bounds, and the text explains how the temporary function notation is eliminated through unique graph values. The conclusion that both components lie strictly below a positive cons code follows from their weak bounds at its predecessor. It is not inferred merely from external primitive recursiveness.

### 5. Sigma-one complexity and bounded evidence — PASS

The local syntactic hierarchy at `inherited-08306-08438.tex:61–94` classifies formulas after the fixed negation-normal-form conversion, and closes Sigma-one under conjunction, disjunction, both marked bounded quantifiers, and unbounded existential quantification. It does not define the class solely by a literal existential prefix.

The graph complexity argument at annex lines 278–285 therefore uses the actual closure clauses. In particular, an existential witness beneath a marked bounded universal requires no unsupported syntactic quantifier exchange.

The evidence construction at lines 312–367 treats a wholly bounded subformula first; otherwise its clauses cover both connectives, unbounded existential quantification, both kinds of marked bounded existential, and both kinds of marked bounded universal. The introduced quantifiers are all marked bounded, and their bounding terms omit the variables they bind. Pairing is atomic and beta is bounded under the declared presentation. Choosing all new variables fresh preserves the required substitutions.

The two directions at lines 369–403 match the evidence interfaces. Pairing totality and bounds justify conjunction, disjunction and existential witnesses. For the universal case, finite collection is applied to the already constructed matrix-evidence relation, so dependent witnesses are collected within PA. Empty strict ranges use code zero, and weak bounds use the successor-length version. The theorem is for each fixed formula; it does not introduce a uniform truth predicate for arbitrary syntax.

### 6. D1 from the fixed numeralwise representative — PASS

Coding lines 472–494 fix a particular Sigma-one formula by the cited numeralwise-representation theorem and define `Prov_T(x)` as its existential proof quantification. The new D1 lemma at lines 496–521 applies only to that already fixed predicate, a c.e. axiom set containing Q, and a sentence.

The numerical arithmetization theorem supplies a standard proof number. The positive numeralwise clause supplies an actual Q derivation at those numerals. Inclusion of Q's axiom sentences in T makes the same derivation a T derivation, and the actual existential-introduction rule supplies the provability instance. The relevant rule is displayed at `inherited-03927-04061.tex:10–15` and `handbook/registry/calculi/nd-fol.tex:24`; the witness is a closed numeral, so no fresh-variable or capture condition is lost.

The arithmetization reference resolves through the existing theorem hook at `handbook/parts/p05.tex:12–20`: the first theorem in the coding input is the arithmetization theorem. The new D1 item is a lemma and does not change that hook's target.

This establishes the stated metatheoretic implication using the retained cited prerequisite. It does not establish D2, D3, or a D1 assertion for an as-yet unconstructed alternative formula `rho` without that alternative's representation justification.

### 7. Numerical modus-ponens constructor and ND compatibility — PASS

The twenty tags at coding lines 237–244 match the governing propositional and first-order rules, including RAA, explicit alpha conversion, and identity. The checker follows the source's nonvacuous, formula-specific discharge; its existential-elimination absence test ranges over all variable occurrences, while universal introduction checks free occurrences. These distinctions agree with `inherited-02193-02340.tex:1–78`, `inherited-03927-04061.tex:7–60`, and the full `nd-fol.tex` rule sheet.

The input formula grammar, variable/free-variable operations, substitution clauses, and alpha-equivalence relation agree with the local syntax chapters. In particular, arbitrary substitution uses the least fresh variable for the stated union even when the substituted variable is not free. The code accepts alpha conversion as its own rule, rather than treating arbitrary equivalence as literal formula equality.

The modus-ponens constructor at annex lines 408–472 uses the certified proof convention specified in coding lines 338–370. It deliberately performs no axiom-membership test itself and is independent of T. Its correctness conclusion is for inputs already satisfying that numerical relation.

For `mp(p,q)`, `p` proves the implication and `q` its antecedent. The output orders `R_q` before the shifted `R_p`; the new tag is `8`, with premise indices `[a-1,a+b-1]`. This is exactly the body rule's antecedent-first order at `inherited-02193-02340.tex:45`. The coding section expressly translates the opposite sheet order by exchanging the two positions at lines 274–277.

Only premise-row indices are shifted. The four other row fields contain rule tags, formula codes, syntactic parameters and discharge markers, not hidden row references. Existing discharge rules act within their original trees. The new common ancestor is a nondischarge rule, so coincident labels in the two input trees do not cause cross-tree discharge. Each prior root acquires one parent, all other parent counts persist, and the new root has none. Certificate concatenation `W_q` then `W_p` matches the computed open-leaf order. Each successful certificate call is reused unchanged, including empty lists.

The accepting-computation interface used here is exactly the standard-model bounded `Comp(e,x,s)` interface at `inherited-08710-08876.tex:805–915`. The new constructor does not require or assert that PA proves an arbitrary program index enumerates its chosen axiom set. The finite-axiom alternate encoding is not silently substituted for the certified convention in this lemma.

### 8. Attribution and remaining proof boundary — PASS for accuracy; dependent construction UNRESOLVED

Representation lines 31–48 retain the explicit cited status and the Shoenfield citation for the Q theorem. Lines 67–74 introduce the PA material as an additional specified construction. Annex lines 5–13 state its actual local axioms, and its proofs refer to local formulas and locally established arithmetic. The original deductions are therefore not presented as an exact external-author construction.

The boundary at annex lines 474–524 identifies `rho` as a target formula still to be constructed. It explicitly requires selection of the PA axiom/certificate convention and compilation of the actual checker; internal row-shift, parent-count, open-leaf and certificate invariants for modus ponens; and a proof builder from bounded evidence for each fixed Sigma-one sentence. It explains the graph elimination required for the displayed constructor notation. The conditional routes from those obligations to D2 and D3 match their stated quantifiers and sentence hypotheses.

In particular, bounded evidence has not been called an ND proof code, standard-model checker correctness has not been called an internal PA proof, and the existence of a numeralwise representative has not been used to select an arbitrary formula in place of the required standard proof predicate. The statement that these remaining obligations are required is accurate.

## Dependency read record

The following are actual read intervals. A whole-file hash pins a dependency even when only the indicated relevant interval was read; it does not claim complete review of an unread interval.

| Dependency | Read interval | SHA-256 |
| --- | --- | --- |
| `spec/EDITION-2026-CONTRACT.md` | 1–168, complete | `c9b101ad6bf6bfea5a3e1fbec25cdba81b47667146474861eb1aa00b5dfa1bf3` |
| `handbook/restoration/inherited-09099-09111.tex` | 1–13, complete | `38534e090c35db78d99d045d19b3c7f34f1f1aaa8999cf118c7a416cd41d9d2b` |
| `handbook/restoration/inherited-09175-09187.tex` | 1–13, complete | `0db98b87928aa115c82883993e2e25b18286779e7ded0399c7148633c0178430` |
| `handbook/restoration/inherited-07678-07752.tex` | 1–75, complete | `1b3a7277d05f42cd5e568cc12b851f2e460bdbab4244d11f91f30eff78aa02dd` |
| `handbook/restoration/inherited-08306-08438.tex` | 1–133, complete | `0b020970be72999cd771566ba0d6cdb4e4668728362cbd3c0d1606059ee9d2b8` |
| `handbook/restoration/inherited-08439-08709.tex` | 1–271, complete | `95eb4270559303fefc5de2d9bc804a04768ead87d68d9e5d9cbf65079714806a` |
| `handbook/restoration/inherited-01101-01147.tex` | 1–47, complete | `a5683457bdf59ea170fa60151b8add87790a4e3ba0a5d4739753b9b676c65663` |
| `handbook/restoration/inherited-03038-03104.tex` | 1–67, complete | `8531b8fc91a659ab7c5b131a77fca7aff9c97f0a052e3b78fe0459adec25ffab` |
| `handbook/restoration/inherited-03105-03165.tex` | 1–61, complete | `5c062c8a2584c841ed74ec9b546fa502ef0ff4d667a5a702ec56b7c8a49463c9` |
| `handbook/restoration/inherited-03166-03239.tex` | 1–74, complete | `d7d08869229f450d219bcb06ffa8e990b60db10f195b76d53e9eccbbc480ac3c` |
| `handbook/restoration/inherited-03240-03428.tex` | 1–189, complete | `36d7779d6b9bb3caf0c4ef514a79a1c7d8aa10bd4a72290256ea1d09d5db58cc` |
| `handbook/restoration/inherited-02193-02340.tex` | 1–148, complete | `5ba27894edf744d288008b613adf93eac3d65385f745135de776d5b6011316a3` |
| `handbook/restoration/inherited-03927-04061.tex` | 1–135, complete | `2ad2846970d4976177b0fbb8ac59ff8106253f5d155a5e4861956f7f651bf480` |
| `handbook/registry/calculi/nd-fol.tex` | 1–29, complete | `f25549bc18fc4aae212eea32cadc9fffd08e03d712f5df10e9da62f660be5370` |
| `handbook/restoration/inherited-15240-15488.tex` | 1–129 | `f63b9f82b7b28ab0fdef72181ac3aa368a40cc5fa1c6a87c42566bf20b86f3a8` |
| `handbook/restoration/inherited-08710-08876.tex` | 534–702 and 795–919 | `4d131a6631a148354f31066316e3b73977df71af66c06fc98158d6c402dbc102` |
| `handbook/parts/p05.tex` | 1–52, complete | `068b90e56bfcf4538aff14f0dbbf428a228a34b12736ca55484b1e3d5e64b326` |
| `handbook/annex/p05-route.tex` | 1–15, complete | `cb9713160edeb4afc683ecb9d7d456a284bbc24f3b3a31a4ad600beaeef8a07f` |
| `handbook/restoration/scope-SRC-09262-09327.tex` | 1–3, complete | `65dcdeca00cacdd15a4483691054ab980af87f178750b5852b358bbd16d12604` |
| `handbook/restoration/scope-SRC-09328-09438.tex` | 1–3, complete | `3d56970059846ae57bc9a1c4e150224b1d4a80f7eb7cc497bb65e33f529bd6a3` |

## Disposition

There are no correction requests from this source/local compatibility review. Acceptance is bounded to the frozen targets and the component judgments above. New checker or proof-builder content requires its own frozen review, and changes to an affected target or dependency reopen the relevant judgment. The particular PA checker, internal D2/D3, and GL consequences remain open under the manuscript's stated boundary.

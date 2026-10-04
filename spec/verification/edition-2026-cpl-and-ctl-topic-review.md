# D-P2-010 and C3: independent mathematical review

Review date: 7 September 2026. Working tree: `C:/Dev/the-methods-of-reason`, branch `phase4-codex`, HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`. The review concerns the current files, including uncommitted files, at the hashes recorded below.

## Verdicts and scope

| Unit | Verdict | Exact scope |
| --- | --- | --- |
| D-P2-010 | **PASS** | Simultaneous uniform substitution, its valuation identity and two consequences; semantic equivalence as a congruence; selected occurrence replacement; their complete supplied annex proofs; the worked and failure examples; mathematical compatibility with the active inherited grammar and valuations; the inspected body/annex bindings. |
| C3 notation repair | **PASS** | The definitions of `EF` and `AF` at temporal supplement lines 102–110, their relation to the strong-until clauses at lines 77–101, and all four verdicts in the complete CTL figure at lines 338–362. |

No mathematical defect or unresolved mathematical premise was found in these scopes. These are topic-review verdicts on the inspected text. They do not assert formal admission, source-fidelity acceptance, successful compilation, visual acceptance, or completion of other parts of either supplement.

Reviewer configuration: independently assigned task `/root/edition_cpl_topic_review`, with the topic-specialist mandate. The exact deployed model identifier/version, reasoning-effort setting, temperature, and seed are unavailable in the supplied assignment and observed tool results. No subagents were used. No other reviewer's report or author verdict for these units was read. Verification consisted of reading the actual LaTeX, matching the inherited clauses, inspecting reference/import text, and independently deriving the semantic results and examples. No manuscript edits, builds, rendering, or software tests were performed. This review file is the sole authored artifact.

The current edition contract was read in full. Its lines 53–58 authorize direct correction in active definitions, formulas, statements, proofs, and restoration files. Its lines 133–137 and 149–168 retain separate independent review and admission obligations. Consequently, the judgments here assess the active mathematics rather than requiring preservation of an erroneous active reading.

## D-P2-010: findings

### 1. The declared language matches the actual inherited language

The body at lines 5–17 uses exactly the alphabet and primitive grammar in `handbook/restoration/inherited-01661-01816.tex:4–58`: variables `p_n`, the constant bottom, negation, conjunction, disjunction, and implication. Top and biconditional remain abbreviations to be expanded before either operation. In particular, neither operation silently treats biconditional as a sixth primitive connective.

The inherited valuation domain and all recursive truth clauses at `handbook/restoration/inherited-01817-01898.tex:4–27` agree with the new body and proof. The inherited semantic definitions at lines 42–60 establish validity and semantic equivalence with the same quantifiers used by the new statements. Equivalence is equality of truth values under every valuation; it is not a formula constructor. The style excerpts listed below confirm that the inherited `Prop`, `Fm`, `CPL`, `True`, and `False` macros display the same mathematical objects named explicitly in the editorial text.

The unique-readability theorem cited at body lines 35–36 exists at inherited grammar lines 108–134 with the required unique outermost-construction statement. The complexity used in the replacement argument agrees with inherited grammar lines 136–154, including complexity zero for both variables and bottom.

### 2. Simultaneous substitution and the valuation identity are correctly defined and proved

Body lines 19–46 define a total assignment from propositional variables to formulas, extend it by each primitive constructor, and explicitly stop substitution at an inserted formula. Thus even a substitution assigning `P` to a formula containing `P`, or mutually referring variable assignments, defines a finite output on every original finite formula. There is no recursive traversal of the substitution images.

For a fixed valuation `v`, the definition `v_upsilon(p_n) = v-hat(upsilon(p_n))` supplies exactly one of the two truth values at every variable. It therefore defines a valuation on the full inherited variable set. The proof at annex lines 4–21 establishes this domain fact before using it.

The annex proves the stated identity `v-hat(phi[upsilon]) = (v_upsilon)-hat(phi)` by induction on the original formula. All primitive formation cases are present and use precisely the inherited clause:

| Formation case | Annex lines | Checked deduction |
| --- | --- | --- |
| Variable | 18–19 | Both sides equal the value of its assigned formula under `v`. |
| Bottom | 20–21 | Substitution fixes bottom; both values are false. |
| Negation | 23–29 | The induction hypothesis preserves the condition that the argument is false; bivalence gives equal output values. |
| Conjunction | 31–39 | The two induction hypotheses preserve the condition that both arguments are true. |
| Disjunction | 41–49 | They preserve the condition that at least one argument is true. |
| Implication | 51–61 | They preserve exactly the falsifying pair: true antecedent and false consequent. |

The two consequences have the precise forward scope stated in the body. For validity, the original formula is true under the valuation `v_upsilon`, so the identity makes its instance true under arbitrary `v` (annex lines 63–66). For equivalence, both original formulas have equal values under that same valuation; applying the identity twice gives equality of the substituted values (lines 68–78). These arguments do not require that every valuation arise as `v_upsilon`. The explicit warning about surjectivity at body lines 43–44 and annex lines 79–80 is correct.

### 3. Selected occurrence replacement is a well-defined operation

Body lines 66–118 define addresses in the original parse tree, including the empty address for the root, one child under negation, and two ordered children under each binary constructor. The definition of the subformula at an address matches that address recursion.

The restriction on `O` selects occurrences of one exact formula string `psi`. It does not select occurrences of the variables appearing in `psi`, and it does not identify different addresses merely because their subformula strings are equal. A proper descendant has strictly lower connective complexity. Hence two selected addresses cannot stand in a proper-prefix relation: both would otherwise carry the same string with different complexities. The proof at annex lines 123–136 supplies the necessary strict-decrease argument for each possible parent constructor.

That argument also handles the root boundary: if the empty address belongs to `O`, then `phi = psi` and `O` contains only that address. Otherwise the sets `O_1` and `O_2` are admissible occurrence selections in the corresponding immediate subformulas. Every recursive call descends the original finite tree. A selected root returns `chi` directly, including when `chi` itself contains `psi`. The operation therefore terminates and does not rescan inserted formulas (annex lines 138–143).

The empty selection is allowed even when `psi` does not occur in `phi`; each recursive call then receives the empty selection and reconstructs the original formula. Selection of all occurrences is also allowed. Distinct selected occurrences are already disjoint as a consequence of their identical finite subformula string, so no additional unproved disjointness hypothesis is needed.

### 4. Congruence and replacement preservation cover every case

The equivalence-relation proof at annex lines 86–92 correctly uses reflexivity, symmetry, and transitivity of equality separately under every valuation. The nullary case is checked at lines 94–95. The negation, conjunction, disjunction, and implication congruence arguments appear separately at lines 99–121. Implication correctly uses its false condition, and the proof explicitly invokes bivalence when passing from agreement on one truth-value condition to equality of outputs.

The replacement induction at annex lines 145–172 permits every admissible selection at each stage; this is the needed induction strength for the child selections. A selected root uses the hypothesis `psi equiv chi`. An unselected variable or bottom is unchanged. An unselected negation uses its child induction hypothesis and negation congruence. The three binary cases each use both child hypotheses and the corresponding previously proved congruence. Empty and all-occurrence selections are explicitly included at the end. Thus the annex proves exactly the body's arbitrary-selected-occurrence statement, not merely replacement of every occurrence or of one variable.

As an additional manual address check, take `phi = ((P and P) -> not P)`, `psi = P`, `chi = not not P`, and `O = {11, 21}`. The selected addresses are respectively the first left conjunct and the variable under the right negation. The stated recursion gives `((not not P and P) -> not not not P)`. The unselected address `12` remains `P`; the `P` inside each inserted `chi` is not revisited. Both original and resulting formulas have the value of `not P`. This calculation checks the child-address shift, a replacement below negation, implication congruence, and an inserted formula that contains the selected string. It is a mathematical calculation, not a software test.

### 5. The worked examples and both failure examples are correct

At body lines 142–157, the assignments `upsilon(P) = Q` and `upsilon(Q) = not Q` yield `(Q and Q)` from simultaneous substitution into `(P and P)`. The inserted `Q` is not processed again. Selecting only address `1` instead yields `(Q and P)`. Under `v(P) = false`, `v(Q) = true`, these outputs are respectively true and false. The text correctly declines to apply the equivalence-preservation theorem to the nonequivalent pair `P`, `Q`.

At lines 159–164, `(P -> Q)` and `(not P or Q)` have the same four two-variable truth values: true, false, true, true in the inherited table's row order. The active inherited table at valuation lines 67–81 proves precisely that equality. Replacement in the left conjunct therefore preserves the surrounding formula's truth value under every valuation.

At lines 168–171, substituting `not bottom` for `P` gives a valid instance of the nonvalid formula `P`. The assignment makes `v_upsilon(P)` true for every `v`, illustrating directly why the validity converse does not follow.

At lines 173–180, distinct `P` and `Q` are each satisfiable and hence equisatisfiable in the explicitly stated sense. The context `(P and not P)` is unsatisfiable, whereas replacing its left `P` by `Q` produces `(Q and not P)`, true at the displayed valuation. This disproves replacement based on mere equisatisfiability and shows loss of satisfiability preservation for the surrounding context, exactly as claimed.

### 6. The inspected reader route and proof references agree

`handbook/main.tex:25` includes the Part II driver and line 44 includes its annex driver. The Part II driver places the two inherited grammar/valuation scopes at lines 5–6 and the new body immediately afterward at line 7. Both scope wrappers directly include the corresponding inherited files. The annex driver includes the new proof file at line 11.

The body theorem at line 48 points to `annex:p2.prop.substitution`; annex line 2 points back to `thm:p02-uniform-substitution`. The body theorem at line 120 points to `annex:p2.prop.replacement`; annex line 84 points back to `thm:p02-replacement`. The proof scopes and conclusions match their respective body statements.

A bounded label/import search found older copies of the theorem labels in `parts/p02/propositional-syntax-semantics.tex`, but no literal `input` or `include` of that historical file anywhere under `handbook`. The current Part II driver does not import it. Those historical label matches therefore do not show a duplicate in the inspected current route. This observation is a source-text route check, not a compilation result.

## C3: definitions and computation-tree verdicts

The complete transition-structure and CTL definitions at supplement lines 46–113 were read. States are evaluated in a nonempty structure with a total successor relation. Paths start at the evaluation state at index zero and are infinite. The strong-until clauses explicitly quantify an eventual witness `m` and require the left operand only at positions `k < m`.

The repair at lines 102–110 defines `EF A` as `E(top U A)` and `AF A` as `A(top U A)`, identifies top as Boolean truth, and explicitly permits `m = 0`. Both abbreviations are therefore defined before the figure and retain inclusive eventuality. For `AF`, the witness index may depend on the path, as the displayed quantifier order requires.

The entire figure at lines 338–362 was checked, including all node labels, arrows, continuing tails, verdict text, caption, and label. The root `w` is labelled `not p`. Its left successor `u` and continuing left branch satisfy `p`. Its right successor `v` and continuing right branch satisfy `not p`. The caption makes the two continuing branches infinite, so the diagram represents the required total computation tree rather than a finite tree with dead ends.

| Displayed claim at `w` | Verdict | Witness or counterexample in the displayed tree |
| --- | --- | --- |
| `EF p` is true | Correct | Follow the left branch; index `m = 1` is a `p` state. |
| `AF p` is false | Correct | Follow the right branch. The negative root defeats the possible witness `m = 0`, and every later state on that branch is also negative. |
| `EX p` is true | Correct | The immediate successor `u` satisfies `p`. |
| `AX p` is false | Correct | The immediate successor `v` does not satisfy `p`. |

The negative root is essential to the second verdict under the now explicit inclusive convention: a positive root would supply `m = 0` on every path and make `AF p` true. The current root and the current definitions agree. The four verdicts do not rely on strict-future semantics or on an undisclosed change to the until clause.

The temporal supplement is directly included by `handbook/parts/p08.tex:32`; `handbook/main.tex:32` includes that Part VIII driver. The review does not extend to unrelated LTL, CTL-completeness, automata, or epistemic claims elsewhere in the same file.

## Read and hash ledger

All paths in this ledger are relative to `C:/Dev/the-methods-of-reason`. SHA-256 values hash the entire corresponding file; the extent column records the actual text inspected, rather than implying that a partial read covers the whole file. The three assigned content hashes were checked on arrival and rechecked unchanged before writing this report. The inherited dependencies and principal drivers were also rechecked unchanged. The recorded final source-hash check occurred at approximately 14:54 UTC.

| File | Actual inspected extent | SHA-256 |
| --- | --- | --- |
| `handbook/parts/p02/propositional-substitution.tex` | Full file, lines 1–181 | `5b39b8dc52b60442850707c6d4df2c7e853929fc52541f85d839986bfd8dc146` |
| `handbook/annex/p02/propositional-substitution.tex` | Full file, lines 1–174 | `4b28adaff5f2a3217ed4808b2ea459639635eb957f7fffd22347071657efc5df` |
| `handbook/restoration/inherited-01661-01816.tex` | Full file, lines 1–156 | `fb12d36a183ac0fdf5c8b2f8a1bbc09238526fdb03f75364a6dc18239913ec3e` |
| `handbook/restoration/inherited-01817-01898.tex` | Full file, lines 1–82 | `499fec700936d0625769d7c09aa2bc5fd1f6d976b9eab1a9cbc8edfe8cafb9c4` |
| `handbook/parts/p08/temporal-epistemic-supplement.tex` | Lines 1–130 and 320–375; includes full definitions 46–113 and full CTL figure 338–362 | `3f9533cfaec9de0da6f3729105571656999122b2813d199d5326c91c6e03d7a0` |
| `spec/EDITION-2026-CONTRACT.md` | Full file, lines 1–168 | `c9b101ad6bf6bfea5a3e1fbec25cdba81b47667146474861eb1aa00b5dfa1bf3` |
| `handbook/parts/p02.tex` | Full file, lines 1–66 | `3576cc349c1245430b30531c266e0483144c5470b2f61a894c0d16d38522fbdd` |
| `handbook/annex/p02.tex` | Full file, lines 1–16 | `65c7b1d7300401cff444dd324fd6c44951b3ab9d8acb9b07d58c41739e9bc87f` |
| `handbook/parts/p02/propositional-logic.tex` | Full file, lines 1–3; ancillary route inspection | `a8fe4d9d183df236dd8a53e738d2487b70b4f571d550f8b81d1e33bf93711544` |
| `handbook/parts/p08.tex` | Full file, lines 1–69 | `18a9d459d89930dd02ec3e337acb806e4a1eb307938e4cc4e699d42428b0af27` |
| `handbook/restoration/scope-SRC-01661-01816.tex` | Full file, lines 1–3 | `dce9a9d142aaaff4ddd0e5746cb5b53609bcbc96d0a2e90752d18ad16378cfd4` |
| `handbook/restoration/scope-SRC-01817-01898.tex` | Full file, lines 1–3 | `abcc08c992478ebe863ca4c0e76d18be4e7a719b69592ab195c168134249f683` |
| `handbook/handbook.sty` | Lines 723–738, 818–855, and 1514–1551, plus matching notation-definition search lines | `1b5c089594010dd517389cdf510cdfbf741e014eaac877cc5bb44f3991412288` |
| `handbook/main.tex` | Import search matches at lines 25, 32, and 44 | `511e6b538b89e6bf9541ac7dc564ebbaa7499d5991e18327c313453087c24761` |
| `handbook/parts/p02/propositional-syntax-semantics.tex` | Search matches only at lines 186, 198, and 205; not read as an alternative substantive presentation | `94338430c4e87cf1b9228274b15adbac052c704eb0b4e81a48b4587a59217b56` |
| `handbook/restoration/inherited-00097-00151.tex` | Incidental notation-definition search matches only at lines 10, 13, 32, 33, and 47 | `c9c2bb625cfe2a0394caa4717c9baf481046d92ae3218386b59c61d79b42500b` |
| `handbook/restoration/inherited-14851-14870.tex` | Incidental notation-definition search match only at line 7 | `3f2923f1a7dba0865f4679cf95b3b2b503e3e18bca918b7a926087d067849e98` |

Other read-only discovery consisted of checking repository identity and status, looking for applicable `AGENTS.md` files, listing candidate filenames, and a bounded memory-index search for the repository name. No memory-derived claim or earlier acceptance verdict is used as evidence for either unit. No research note, progress file, admission record, or other review report was opened.

## Closure conditions

For D-P2-010, no further mathematical correction is required by this review at the recorded body, annex, and inherited-dependency hashes. Changes to the grammar, truth clauses, substitution/replacement definitions, theorem scopes, proofs, examples, or their bindings require review of the affected scope.

For the C3 notation repair, no further mathematical correction is required by this review at the recorded supplement hash. Preserve the inclusive eventuality definitions, the negative root, the infinite negative right branch, and the four matching verdicts; changes affecting them require rechecking the figure against its semantics.

The lead must still obtain the other independent reviews and whatever static, build, visual, provenance, and admission evidence the governing contract requires. None of those separate gates is certified by these mathematical PASS verdicts.

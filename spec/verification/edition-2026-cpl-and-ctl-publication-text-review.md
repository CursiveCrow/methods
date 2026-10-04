# D-P2-010 and C3: independent adversarial publication text review

Date: 7 September 2026. Repository: `C:/Dev/the-methods-of-reason`.
Reviewer context: `/root/edition_cpl_publication_review`.
Dependency hash checkpoint: 07:54:56 PDT.

## Scoped verdicts

| Unit | Verdict | Exact scope |
| --- | --- | --- |
| D-P2-010, uniform substitution and selected-occurrence replacement | **FAIL** | The complete body and annex text, active prerequisites and routes, proof references, examples, and current relevant symbol apparatus. The body/annex reasoning passes the text examination; the integrated notation apparatus has the three repair conditions below. |
| C3, CTL eventuality notation before the computation-tree figure | **PASS** | The total-transition/path prerequisites, CTL definition, and complete computation-tree figure. `EF` and `AF` are defined before their use, and all four displayed verdicts follow from the displayed structure. |

These are publication **text** verdicts. Full publication and visual review,
source-fidelity admission, the other independent review gates, and formal unit
admission remain **UNRESOLVED** in this review. The governing amendment requires
those separate stages (`spec/EDITION-2026-CONTRACT.md:149-168`).

## Independence and method

This was a fresh independent reviewer context. I read the assigned manuscript
files directly and did not read another reviewer's report or an author's review
verdict. The retired syntax/semantics manuscript was inspected only at its
reused definition/theorem labels and immediately surrounding statements; its
completion language supplied no acceptance evidence. A lightweight historical
memory-registry lookup supplied repository orientation only and supplied no
target-unit verdict or mathematical evidence.

The exposed agent identity was `/root/edition_cpl_publication_review`. The actual
model identifier, reasoning effort, service tier, and model version were not
exposed to this reviewer and are **unavailable**. No subagents were used.

I used line-numbered LaTeX reads, literal route/reference searches, current CSV
and generated-table inspection, file hashes, and direct mathematical reasoning.
I made no manuscript, driver, style, bibliography, symbol, or admission-record
edits. I ran no build, rendering, software regression tests, or formal checker.
The only written artifact is this review.

## D-P2-010: findings and repair conditions

### F1. The active formula-equivalence role is absent from the normative register

**Confirmed apparatus defect; blocks the integrated text verdict.**
`handbook/parts/p02/propositional-substitution.tex:13-17` explicitly retains
`alpha equiv beta` as semantic formula equivalence. This agrees exactly with
the active prerequisite at
`handbook/restoration/inherited-01817-01898.tex:56-58`.

The current register still states that formula equivalence uses
`Leftrightarrow` and that `equiv` is reserved for elementary equivalence
(`handbook/registry/symbols.csv:30`). Its structure-equivalence row says that
this is the sole global role (`:42`). There is no P2.1 row recording the active
semantic formula-equivalence role. These declarations reach the reader through
`handbook/generated/symbols-tables.tex:38,50` and
`handbook/parts/p01/symbol-registry.tex:15-20,25-31`.

The local declaration makes the new theorem unambiguous, but does not fulfill
the independent registry requirement: the reader-facing registry is normative
and requires every overlapping local role to be typed and registered
(`handbook/parts/p01/symbol-registry.tex:6-12`;
`handbook/CONVENTIONS.md:216-222`). The edition contract preserves distinct
notation conventions with their own typed roles (`spec/EDITION-2026-CONTRACT.md:60-65`).

**Repair condition:** register the P2.1 semantic-equivalence role and its precise
source/local scope; qualify the global reservation and its reader-facing prose
so both declarations can be true. Reconcile the generated lookup surfaces through
their normal source/projection process. The repair must preserve the active
source notation and the meaning of the theorem.

### F2. The registered CPL truth-value set disagrees with its active definition

**Confirmed apparatus defect; blocks the integrated text verdict.**
The body uses bold F and T at
`handbook/parts/p02/propositional-substitution.tex:10-12,38-44` and the annex
uses exactly that codomain at
`handbook/annex/p02/propositional-substitution.tex:4-8`.
The active prerequisite defines `B = {False, True}` and valuations into that
set (`handbook/restoration/inherited-01817-01898.tex:4-7`). The source-scope
macros render these as blackboard B, bold F, and bold T
(`handbook/handbook.sty:1546-1553`).

In contrast, `handbook/registry/symbols.csv:127` identifies the P2.1 blackboard-B
truth-value set as `{0,1}`, without a source-scope alternative or an explicit
coding map. The same entry is printed at
`handbook/generated/symbols-tables.tex:113`. The complete register search found
no bold-F/bold-T truth-value row that supplies the missing local declaration.
The two presentations are isomorphic, but the register currently equates their
notation without stating that identification. The new body and proof do not
make that identification and need none.

**Repair condition:** record the active F/T truth-value domain and any genuinely
distinct 0/1 presentation with their exact scopes. If a coding is intended,
declare it explicitly where it is used. Reconcile the reader-facing generated
row. Do not convert the already consistent body and annex into a different
valuation convention merely to match the current row.

### F3. The new occurrence operations have no current symbol-registry entries

**Confirmed apparatus omission; blocks completion of the requested apparatus
scope.** Definition `def:p02-selected-replacement` introduces the position-set
operation `Pos`, subformula-at-position notation, and selected-occurrence
replacement at `handbook/parts/p02/propositional-substitution.tex:66-115`.
They are precisely defined in the text. Full-register literal/role searches
found no corresponding position-set or selected-subformula-replacement entry
in `handbook/registry/symbols.csv`. Existing rows do register the distinct
subformula-set operation (`:129`) and uniform-substitution map/action
(`:130-131`); those rows cannot describe the new operation because it selects
original tree positions and can replace only one of two identical occurrences.

**Repair condition:** add scoped rows for the genuinely new operation roles,
including `Pos(phi)`, the subformula-at-position notation used to select the
set, and `phi[O leftarrow chi]`. State that positions are in the original parse
tree and selected replacements are simultaneous without revisiting inserted
formulas. The induced valuation may be recorded alongside the existing
valuation/substitution entries; ordinary locally bound variables need no
invented separate mathematical standing. Reconcile the downstream lookup
surfaces and inspect the affected printed entries before apparatus admission.

## D-P2-010: checks that passed

**Reader route and prerequisites.** `handbook/main.tex:25,44` routes the P2 body
and annex. `handbook/parts/p02.tex:5-7` places the new subsection immediately
after the alphabet/grammar and valuation restorations. Their three-line scope
wrappers directly input `inherited-01661-01816.tex` and
`inherited-01817-01898.tex`. `handbook/annex/p02.tex:11` inputs the new annex once.
Literal input searches found one body input and one annex input; the retired
`parts/p02/propositional-syntax-semantics.tex` is not input anywhere in the
current handbook LaTeX. This is source-route inspection, not compiled navigation
evidence.

The active grammar declares exactly the variable, falsum, negation, conjunction,
disjunction, and implication cases
(`handbook/restoration/inherited-01661-01816.tex:4-57`). It establishes unique
readability (`:108-134`) and complexity/subformula recursion (`:136-155`). The
valuation clauses, validity, equivalence, and the implication/disjunction truth
table are all present before use
(`handbook/restoration/inherited-01817-01898.tex:4-26,42-80`). The new subsection
uses those exact prerequisites and expands defined connectives before operating
on the primitive grammar (`handbook/parts/p02/propositional-substitution.tex:5-17`).

**Reused identities and proof standing.** The definition and two theorem labels
at body lines 19, 48, and 120 preserve the corresponding identities found in the
retired manuscript at lines 186, 198, and 205. The new annex targets are distinct.
The body status at line 48 points to `annex:p2.prop.substitution`, whose annex
item at line 2 points back to `thm:p02-uniform-substitution`. The body status at
line 120 and annex item at line 84 make the analogous replacement pair. Both
statuses are `proved=` and both annex items contain full proofs. The status and
back-reference rendering mechanisms exist at
`handbook/handbook.sty:340-347,493,1610-1621`. The new body contains no proof
environment, and neither new file attributes these proofs to an unconsulted
external book. The earlier retired `cited=Kleene1952` declarations are not used
as proof evidence.

**Uniform substitution.** Body lines 19-44 specify a total variable-to-formula
map, all primitive recursive cases, one-time insertion, and the induced
valuation. Annex lines 4-61 prove its valuation identity in all six formation
cases. Lines 63-80 derive exactly the two stated consequences and correctly
avoid surjectivity or a converse. The primitive falsum case and bivalence are
explicit.

**Selected replacement.** Body lines 66-115 distinguish occurrences from formula
strings, define the position sets and child suffix sets, allow root/empty/all
choices, and prohibit recursion into inserted formulas. Strict complexity
decrease correctly prevents equal formula strings from occurring at nested
selected positions. Annex lines 86-121 prove equivalence-relation and primitive
congruence claims; lines 123-143 justify the occurrence operation; lines 145-172
prove replacement by induction for every admissible selected set, including
root and empty choices. No overlapping-selection ambiguity remains.

**Examples and limitations.** Body lines 142-157 correctly give `(Q and Q)` for
the simultaneous substitution and `(Q and P)` for selection of the left P only.
At `v(P)=F, v(Q)=T`, their values are respectively T and F. The text explicitly
withholds the equivalence theorem when P and Q are distinct, nonequivalent
variables. Lines 159-164 correctly use the preceding truth table to replace only
the left `(P implies Q)` by `(not P or Q)`. Lines 167-171 give a valid instance
`not bottom` of the invalid formula P. Lines 173-180 correctly show that replacing
a satisfiable P by an equisatisfiable Q inside `(P and not P)` can make an
unsatisfiable context satisfiable. Both counterexamples refute the stated
weakenings.

**Current matching symbol rows.** Rows 24, 123, 125-126, and 130-131 of
`handbook/registry/symbols.csv` agree with the valuation role, fixed propositional
alphabet, uppercase example variables, formula-set role, and uniform-substitution
map/action. Their presence does not repair F1-F3.

## C3: definition order and four verdicts

The active route is `handbook/main.tex:32` to `handbook/parts/p08.tex:32`, which
inputs the temporal/epistemic supplement once. In that file the total transition
structure and infinite paths are defined at lines 46-56; the CTL syntax and next
semantics appear at lines 58-76; strong-until semantics appear at lines 77-101.
Lines 102-110 define `EF A := E(top U A)` and `AF A := A(top U A)`, identify top,
and explicitly permit an until witness at time zero. All of these precede the
complete figure at lines 338-362.

| Displayed assertion at w | Direct check from the complete figure |
| --- | --- |
| `EF p` true | The branch through u reaches a p-state in one step; choose that branch and witness m = 1 in lines 80-89. |
| `AF p` false | The branch through v and v1 continues forever with not-p labels, so it has no eventuality witness under lines 90-99. |
| `EX p` true | The edge w to u has a p-labelled target, satisfying lines 69-71. |
| `AX p` false | The edge w to v has a not-p-labelled target, falsifying lines 72-74. |

The root has not-p; allowing m = 0 therefore does not change either eventuality
verdict here. The two annotated tails at lines 346-347 and arrows at 352-353 are
part of the depicted infinite structure; the caption at 358-360 explicitly
excludes terminal-leaf readings. The same current registry contains the
transition/path role (`handbook/registry/symbols.csv:521`), path quantifiers
(`:526`), and paired EX/AX/EF/AF operators (`:527`), projected at
`handbook/generated/symbols-tables.tex:674` for the last row. No textual repair
condition remains for C3 at the assigned hash.

This verdict does not assess all surrounding CTL/CTL*/mu-calculus cards, their
external source attributions, complexity claims, or the visual placement of the
floating figure. Those are separate scopes.

## Read and hash ledger

All hashes below are SHA-256. The three assigned hashes matched at initial read
and at the dependency checkpoint. Hashing a complete file does not assert that
its entire contents were reviewed when the read extent below is narrower.

| Path relative to repository | Actual read extent | SHA-256 |
| --- | --- | --- |
| `handbook/parts/p02/propositional-substitution.tex` | Complete, lines 1-181 | `5b39b8dc52b60442850707c6d4df2c7e853929fc52541f85d839986bfd8dc146` |
| `handbook/annex/p02/propositional-substitution.tex` | Complete, lines 1-174 | `4b28adaff5f2a3217ed4808b2ea459639635eb957f7fffd22347071657efc5df` |
| `handbook/parts/p08/temporal-epistemic-supplement.tex` | Definition/context lines 1-330 and whole figure 338-362; adjoining visible material was not admitted as part of C3 | `3f9533cfaec9de0da6f3729105571656999122b2813d199d5326c91c6e03d7a0` |
| `spec/EDITION-2026-CONTRACT.md` | Complete, 168 lines | `c9b101ad6bf6bfea5a3e1fbec25cdba81b47667146474861eb1aa00b5dfa1bf3` |
| `handbook/CONVENTIONS.md` | Complete, 251 lines | `4293f514072179a5ac95e64fa8d8f37e23ffe2693814a1980e5801baba5b7242` |
| `handbook/parts/p02.tex` | Complete, 66 lines | `3576cc349c1245430b30531c266e0483144c5470b2f61a894c0d16d38522fbdd` |
| `handbook/annex/p02.tex` | Complete, 16 lines | `65c7b1d7300401cff444dd324fd6c44951b3ab9d8acb9b07d58c41739e9bc87f` |
| `handbook/main.tex` | Targeted body/annex route search | `511e6b538b89e6bf9541ac7dc564ebbaa7499d5991e18327c313453087c24761` |
| `handbook/parts/p08.tex` | Targeted supplement route search | `18a9d459d89930dd02ec3e337acb806e4a1eb307938e4cc4e699d42428b0af27` |
| `handbook/restoration/scope-SRC-01661-01816.tex` | Complete, 3 lines | `dce9a9d142aaaff4ddd0e5746cb5b53609bcbc96d0a2e90752d18ad16378cfd4` |
| `handbook/restoration/scope-SRC-01817-01898.tex` | Complete, 3 lines | `abcc08c992478ebe863ca4c0e76d18be4e7a719b69592ab195c168134249f683` |
| `handbook/restoration/inherited-01661-01816.tex` | Complete, 156 lines | `fb12d36a183ac0fdf5c8b2f8a1bbc09238526fdb03f75364a6dc18239913ec3e` |
| `handbook/restoration/inherited-01817-01898.tex` | Complete, 82 lines | `499fec700936d0625769d7c09aa2bc5fd1f6d976b9eab1a9cbc8edfe8cafb9c4` |
| `handbook/registry/symbols.csv` | Lines 1-43, 123-137, 517-531; full-file targeted glyph/role searches | `b04973e11ede15ddf1d15a5709c1b678ba7061c5904d7854811cae91415ccebd` |
| `handbook/generated/symbols-tables.tex` | Targeted current row searches, including lines 38, 50, 113, 116-117, 674 | `c6b97c8d431d996110d8881ea6e74da26278c20c0b5b9460a5948b133a650553` |
| `handbook/generated/symbol-index.tex` | Targeted current row searches | `c4e444976a9310e20a0e732651f760a6b20235cad84e306d5a5f043db0f3edbd` |
| `handbook/parts/p01/symbol-registry.tex` | Relevant normative declarations and table route, lines 1-31; further visible chapter context not admitted | `9cad06e4562f46a1094b77fb683ec979183f4094e41bf53ecc5c2d6f9eee18fb` |
| `handbook/handbook.sty` | Targeted status, annex, and source-macro definitions, especially lines 340-347, 493-498, 1515-1555, 1610-1630 | `1b5c089594010dd517389cdf510cdfbf741e014eaac877cc5bb44f3991412288` |
| `handbook/parts/p02/propositional-syntax-semantics.tex` | Retired labels and neighboring statements, lines 180-219 | `94338430c4e87cf1b9228274b15adbac052c704eb0b4e81a48b4587a59217b56` |

## Remaining boundaries

No external primary book or paper was consulted for this text review. The active
restoration fragments establish the local prerequisite text examined here; their
source fidelity, frozen-source identity, acquisition extent, and correction
provenance require their own evidence. In particular, this review does not
reassign the elementary annex proofs to Kleene or independently authenticate the
surrounding CTL bibliography.

The PDF was not built, opened, rendered, or inspected. Hyperlink targets and
unique input paths were inspected in LaTeX; their rendered operation, float
order, page breaks, margins, line wrapping, notation-table layout, and complete
figure visibility remain pending. No strict-check result or software test result
is claimed. No source packet, register obligation, or unit admission was closed.

After F1-F3 are repaired, re-review the affected notation declarations and lookup
text against their new hashes, preserving this body's and annex's valid reasoning
evidence only while their content and logical dependencies remain unchanged.
Then complete the separate static/build/visual and formal admission stages
required by the edition contract.

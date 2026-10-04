# D-P2-010 and C3: independent source-fidelity review

Date: 7 September 2026. Reviewer task: `/root/edition_cpl_source_review`.
Repository: `C:/Dev/the-methods-of-reason`, branch `phase4-codex`, HEAD
`35d537c692bb74b532dc4aa750da381a7fe4daf2`. This review concerns the working
files identified below; HEAD alone does not identify them.

## Scoped decisions

| Unit | Source-fidelity decision | Scope |
| --- | --- | --- |
| D-P2-010 | PASS | Both new CPL files, including the substitution identity and consequences, equivalence congruence, selected-occurrence replacement, examples, and their derivation from the specified inherited language and semantics. |
| C3 | PASS | The EF/AF definitions added before the CTL figure, their agreement with the displayed strong-until semantics and registered EF/AF schemas, and the figure's negative-root interpretation. |

No source-fidelity failure or unresolved source dependency was found within
these two assigned scopes. These decisions do not constitute unit admission,
source acquisition for an external book, or publication acceptance.

The actual runtime model identifier/version, reasoning-effort setting, and
provider configuration are not exposed in this review context: **unavailable**.
The reviewer is a separate agent context assigned source fidelity. No other
current-unit reviewer report or author verdict was read. Earlier acceptance
summaries were not used as evidence for either decision.

## Governing contract and inspected snapshot

I read `spec/EDITION-2026-CONTRACT.md` in full. Relevant requirements are the
preservation of inherited substance and distinct notation conventions,
justified editorial reconstruction and promised proofs (lines 47-74), stable
labels (78-80), independent reviews (133-139), and separate admission and
publication evidence (149-168). Its SHA256 is
`c9b101ad6bf6bfea5a3e1fbec25cdba81b47667146474861eb1aa00b5dfa1bf3`.

The three assigned manuscript hashes matched at initial inspection and at the
final check before this report was written:

| File | SHA256 | Reading extent |
| --- | --- | --- |
| `handbook/parts/p02/propositional-substitution.tex` | `5b39b8dc52b60442850707c6d4df2c7e853929fc52541f85d839986bfd8dc146` | All 181 lines. |
| `handbook/annex/p02/propositional-substitution.tex` | `4b28adaff5f2a3217ed4808b2ea459639635eb957f7fffd22347071657efc5df` | All 174 lines. |
| `handbook/parts/p08/temporal-epistemic-supplement.tex` | `3f9533cfaec9de0da6f3729105571656999122b2813d199d5326c91c6e03d7a0` | C3 semantic context at 46-113, related CTL/CTL* context at 115-173, and figure at 338-362. A continuous read covered 1-310 and 312-390; this is not a review of every claim in the whole supplement. |

The inherited source artifact is `source/formal-logic-reference.tex`, SHA256
`0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc`.
I read its lines 1661-1898 directly. The current source file has no tracked
change reported by Git. The following fragments were also inspected:

| File | SHA256 | Evidence used |
| --- | --- | --- |
| `handbook/restoration/inherited-01661-01816.tex` | `fb12d36a183ac0fdf5c8b2f8a1bbc09238526fdb03f75364a6dc18239913ec3e` | All 156 lines: alphabet, exact grammar, defined connectives, readability, complexity, and subformula definition. |
| `handbook/restoration/inherited-01817-01898.tex` | `499fec700936d0625769d7c09aa2bc5fd1f6d976b9eab1a9cbc8edfe8cafb9c4` | All 82 lines: valuations, all truth clauses, semantic notions, and implication truth table. |
| `handbook/restoration/inherited-02933-03021.tex` | `ec910182f4db775f35fe3fa1a23f4f12f3cf31282e8dd761b208d0cad38d5b61` | All 89 lines, especially the congruence exercise at 60-64 and the distinct next exercise at 66-71. |
| `handbook/restoration/inherited-15638-16742.tex` | `993a3153c9ca856f761b5650c312e85e2be78fa23b8afc8edcd4e87a7b2983bf` | Semantic reading of 145-180, especially the congruence feedback at 161-167; the entire 1,105-line fragment was compared with its source range. |
| `handbook/parts/p02/propositional-syntax-semantics.tex` | `94338430c4e87cf1b9228274b15adbac052c704eb0b4e81a48b4587a59217b56` | Inactive historical intent at 186-215, with surrounding notation at 175-184. Used to identify prior labels and statements only. |
| `handbook/registry/calculi/hilbert-ctl.tex` | `d8213c581d16700e21c5295f996501c14d0f25968382f394df3e93690e6a717c` | All 15 lines, specifically the EF and AF schemas at 5-6. |

The inactive CPL draft is not treated as an active presentation or as evidence
that Kleene's book has been acquired or read.

## D-P2-010 findings

### Primitive language and notation: PASS

The new body fixes the same countable variable set and the same constructors
as source lines 1664-1700: variable leaves, the nullary bottom connective,
unary negation, and the three binary connectives conjunction, disjunction,
and implication. Its substitution definition explicitly supplies every case
(body 19-36), and its occurrence/replacement recursion uses this same set
(66-118). It does not import a reduced primitive basis from a different CPL
presentation. Defined top and biconditional are expanded first (body 15-17),
as required by source 1708-1717.

The body uses semantic `\equiv` for equality of truth values under every
valuation (13-15), matching source 1872-1874 and restoration 56-58. This is
the correct local meaning; the inactive draft's `\Leftrightarrow` convention
does not override it. Object-language variables, formula metavariables,
formula-string equality in occurrence selection, semantic equivalence,
validity, and mere equisatisfiability retain distinct roles.

The source truth values are also retained. The inherited-scope definitions in
`handbook/handbook.sty` at 1522, 1528-1529, and 1546-1547 give the same printed
formula-set, variable-set, CPL, and bold F/T notation used explicitly in the
addition. The style file inspected has SHA256
`1b5c089594010dd517389cdf510cdfbf741e014eaac877cc5bb44f3991412288`.

### Uniform substitution: PASS

The simultaneous operation is explicit: each original variable receives its
assigned formula once, and the inserted formula is not recursively subjected
to the same substitution (body 21-36). The induced valuation is defined on
every variable by the value of its assigned formula (38-44). The source's
unique readability result (1768-1794) and recursively defined truth extension
(1820-1843) justify this construction.

The annex proves the valuation identity for a variable, bottom, negation,
conjunction, disjunction, and implication separately (18-61). Each case uses
exactly the corresponding source clause: negation is true on false input;
conjunction is true on two true inputs; disjunction is true when at least one
input is true; implication is false exactly on true/false inputs. Bivalence
justifies the equality conclusions. The consequences for validity and
equivalence follow using the induced valuation (63-80); neither argument
requires a converse or surjectivity.

The prior intended theorem at inactive-draft 198-203 is therefore preserved
in content, with an additional proved valuation identity. The stable theorem
label is retained. The body example at 143-157 correctly distinguishes
simultaneous substitution from replacing only the left occurrence. The
counterexample at 168-171 correctly rules out inferring validity of an
original formula from one valid instance.

### Congruence and selected replacement: PASS

The equivalence-relation and congruence statements at body 120-140 reproduce
the substance requested by inherited exercise 60-64. Annex 86-121 expands the
actual feedback at 161-167: it derives the equivalence laws from equality of
truth values, checks negation and every binary truth function, and explicitly
handles the nullary bottom case as well.

The selected-occurrence theorem is a justified elementary extension of that
congruence result. The body defines positions, their associated subformulas,
the admissible selection set, and the original-tree recursion before stating
the theorem (66-118). It distinguishes two equal subformula strings at
different positions. The nonoverlap argument is justified by the inherited
complexity measure: every proper subformula has strictly smaller complexity,
so equal formula strings cannot occur one strictly inside the other. Annex
123-143 supplies the details and establishes that the recursion terminates
with a formula in the same language.

Annex 145-172 proves replacement by induction over the original formula,
including a selected root, unselected leaves, negation, and all three binary
constructors. Both an empty selection and selection of all occurrences are
included. Inserted formulas are not revisited. This preserves the full
selected-occurrence claim and distinction stated in inactive-draft 205-215.

The equivalence-preserving example (body 159-164) uses the actual inherited
truth table at source 1883-1897. The example at 173-180 establishes the stated
limit: replacing one P in the contradiction `P and not P` by a distinct Q
produces a satisfiable formula, even though P and Q themselves are both
satisfiable. Its explicit F/T valuation verifies the difference.

### Reconstruction, attribution, and preservation: PASS

The two new files present elementary definitions and complete arguments in
their own text. Their theorem statuses point to the actual annex proofs
(`proved=annex:p2.prop.substitution` and
`proved=annex:p2.prop.replacement`), and those annex items link back to the
corresponding body labels. Neither file cites Kleene1952, attributes these
proofs to a particular unread Kleene passage, or claims to reproduce that
book's presentation. The inactive draft's old citation is not promoted into
external-source evidence. This decision validates the specified elementary
reconstruction from the inherited source; it does not discharge any separately
required Kleene-source acquisition or presentation obligation.

The preservation finding is supported by direct comparison, not by a prior
status report. Reading the source and restoration files as lines and comparing
corresponding text case-sensitively found **zero differing lines** for each
entire range: 1661-1816 (156 lines), 1817-1898 (82), 2933-3021 (89), and
15638-16742 (1,105). This establishes textual line equality; it is not a claim
that the fragment files have the same byte-level hash as differently packaged
source slices.

The route also preserves these authorities. `handbook/parts/p02.tex` includes
the two grammar/semantics wrappers at 5-6, the new body at 7, and the original
exercise wrapper at 19. Each wrapper still includes its original fragment.
`handbook/parts/p12.tex:43` retains the feedback wrapper and that wrapper still
includes its original fragment. `handbook/annex/p02.tex:11` adds the new proof
file. `handbook/main.tex:25,36,44` supplies those part and annex routes.
Accordingly, none of the specified original grammar clauses, truth clauses,
exercise text, or feedback has been removed or replaced by the additions.

## C3 findings: PASS

The added definitions are at temporal-supplement 102-110, within the CTL
definition and before the negative-root figure at 338-362. They expand EF A
as E(top U A) and AF A as A(top U A), identify top as Boolean truth, and
explicitly retain the possibility of a witness at time zero.

Substituting top for the left operand in the actual strong-until clauses at
77-101 makes the preceding-state condition automatic. EF A therefore asserts
that some path has a position satisfying A. AF A asserts that every path has
such a position, with the witness allowed to depend on the path. The displayed
quantifier order supports these readings, and no strictly-future restriction
has been introduced. The existing state/path distinction and total-transition
setting at 46-66 are preserved.

These expansions agree with the registered EF and AF schemas in
`handbook/registry/calculi/hilbert-ctl.tex:5-6`. The registry writes `\topv`;
the supplement writes `\top`. The inspected style definition at
`handbook/handbook.sty:215` makes `\topv` exactly `\top`, so this does not
introduce a different truth constant or a different until convention. The
registry expresses equivalences as calculus schemas, while the semantic
presentation uses abbreviations; those roles are compatible and remain
distinguishable.

The figure's root satisfies not p (341). Its left branch reaches p at the
first successor, so it witnesses EF p and EX p. The right branch and its
explicit infinite continuation satisfy not p throughout (343, 345, 347,
349-353), so AF p fails and the immediate right successor also refutes AX p.
The negative root prevents the allowed time-zero witness from making AF p
trivially true. The caption explicitly makes the dotted continuations infinite
(358-360). Thus all four claims at 355-356 follow from the displayed clauses.

This is a source-fidelity decision about the local notation repair and its
specified dependency. It does not authenticate the registry's attribution to
Emerson-Halpern against an external copy, or review the entire CTL calculus,
its adequacy theorem, complexity results, CTL*, or the rest of the supplement.

## Route snapshot and remaining evidence boundaries

The additional inspected route hashes were:

| File | SHA256 |
| --- | --- |
| `handbook/parts/p02.tex` | `3576cc349c1245430b30531c266e0483144c5470b2f61a894c0d16d38522fbdd` |
| `handbook/annex/p02.tex` | `65c7b1d7300401cff444dd324fd6c44951b3ab9d8acb9b07d58c41739e9bc87f` |
| `handbook/parts/p12.tex` | `8ccff3944dedeff8d6ffbef93e5972a6bce551f165c2f7ee2f535a2753bee105` |
| `handbook/main.tex` | `511e6b538b89e6bf9541ac7dc564ebbaa7499d5991e18327c313453087c24761` |
| `handbook/restoration/scope-SRC-01661-01816.tex` | `dce9a9d142aaaff4ddd0e5746cb5b53609bcbc96d0a2e90752d18ad16378cfd4` |
| `handbook/restoration/scope-SRC-01817-01898.tex` | `abcc08c992478ebe863ca4c0e76d18be4e7a719b69592ab195c168134249f683` |
| `handbook/restoration/scope-SRC-02933-03021.tex` | `e4e88f4c11d5ad19060629679e3d449cffd3af364533db2b5934b936e39445c1` |
| `handbook/restoration/scope-SRC-15638-16742.tex` | `29d01f396b496337daa15f72b48979d48ba7eb1591fc0e002fc8282b60881490` |

Only this report was created by the reviewer. No manuscript edits, build,
render, software tests, repository validation suite, formal proof-assistant
check, or admission operation was performed. Source inspection, hashes,
literal line comparison, and the elementary deductions above are the evidence
for these scoped decisions. The independent specialist and publication
reviews, relevant build/static/visual gates, and separate admission record
remain separate requirements under the contract. Changes to the reviewed
content or its relevant dependencies require renewed review of the affected
scope.

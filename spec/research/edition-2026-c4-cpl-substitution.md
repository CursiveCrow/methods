# Edition 2026 C4: active CPL substitution and replacement

Requirement: D-P2-010. Authoring checkpoint: 7 September 2026, 14:44 UTC.
This record describes the supplied text, local semantic reasoning and read-back;
it is not independent review acceptance or formal admission.

## Supplied active material

The new [body, 181 lines](C:/Dev/the-methods-of-reason/handbook/parts/p02/propositional-substitution.tex:1) and [annex, 174 lines](C:/Dev/the-methods-of-reason/handbook/annex/p02/propositional-substitution.tex:1) supply:

- Simultaneous uniform substitution, with a separate recursive clause for every primitive constructor and an explicit instruction not to substitute again inside an inserted image.
- The valuation identity \(\widehat v(\varphi[\upsilon])=\widehat{v_\upsilon}(\varphi)\), where \(v_\upsilon(p)=\widehat v(\upsilon(p))\).
- Preservation of validity and logical equivalence under uniform substitution.
- Explicit parse-tree positions and selected-occurrence replacement, including the empty selection, selected root and all original occurrences.
- Equivalence-relation laws and congruence for the nullary bottom, unary negation and all three binary connectives.
- The selected-occurrence replacement theorem with a complete structural induction.

The three requested stable labels are reused without changing the inactive file:

| Body label | Active location | Proof target |
|---|---|---|
| def:p02-uniform-substitution | body:19 | Definition |
| thm:p02-uniform-substitution | body:48 | annex:p2.prop.substitution, annex:2 |
| thm:p02-replacement | body:120 | annex:p2.prop.replacement, annex:84 |

The new occurrence definition is def:p02-selected-replacement at body:66.
Both theorem statuses are proved links to the exact annex items, and each annex
item points back to its own body theorem.

## Source and notation basis

The following actual local material was read:

1. Inactive propositional-syntax-semantics.tex:170–226, including the requested lead at 186–215. It supplies the intended stable labels and old statement scope, not active proof evidence.
2. The entire active inherited-01661-01816.tex:1–156: variables; primitive bottom, negation, conjunction, disjunction and implication; derived truth/biconditional; unique readability; complexity and subformulas.
3. The entire active inherited-01817-01898.tex:1–82: valuations, every recursive truth clause, validity, semantic equivalence and the implication/disjunction truth table.
4. inherited-15638-16742.tex:145–180, including the actual congruence feedback at 161–167. That feedback remains a solution sketch; it was not rewritten or silently promoted.
5. The relevant guarded-style typography assignments: the source's truth values print as bold T/F, while Prop, Fm and CPL print in mathematical sans serif.

The new body keeps the active source's local \(\equiv\) for logical equivalence
and explicitly declares its semantic role. It keeps exactly the primitive
grammar \(\bottom,\neg,\land,\lor,\to\). Defined connectives are expanded first.
It uses explicit \(\mathsf{Prop}\), \(\mathsf{Fm}_{\mathsf{CPL}}\) and
\(\mathbf F,\mathbf T\), avoiding source-only macros outside restoration scope.

The elementary proofs were authored directly from the inspected truth clauses.
No Kleene book was acquired or read, and the old inactive Kleene citation is
not presented as evidence that its proof was inspected.

## Mathematical checks completed by the author

The uniform-substitution proof checks variables and bottom separately, then
negation, conjunction, disjunction and implication separately. Equality of
values follows from the source's exact true/false conditions and bivalence.
The derived valuation is total because every substitution image is a formula.
Preservation needs no surjectivity of \(v\mapsto v_\upsilon\).

For occurrence replacement, complexity counts only occurrences of
\(\neg,\land,\lor,\to\), matching the source's zero complexity for variables
and bottom. It strictly decreases on every descent. Thus two occurrences of
the same finite formula cannot properly contain one another. The recursion
stops at selected roots and recurses only on original proper subformulas.
Each primitive congruence is proved directly before the replacement induction
uses it. The two leaf cases, selected root, empty selection and all-occurrence
selection are explicit.

The worked calculations were checked against those clauses:

- With \(\upsilon(P)=Q\) and \(\upsilon(Q)=\neg Q\),
  \((P\land P)[\upsilon]=Q\land Q\), not \(\neg Q\land\neg Q\).
  Replacing only the left occurrence of \(P\) gives \(Q\land P\).
  At \(P=\mathbf F,Q=\mathbf T\), the outputs are respectively true and false.
- The source truth table gives \(P\to Q\equiv\neg P\lor Q\).
  Replacement of only one copy in a conjunction preserves equivalence.
- Substituting \(\neg\bottom\) for \(P\) makes the instance valid although
  \(P\) is not valid. This refutes the reverse validity implication.
- \(P,Q\) are equisatisfiable, but replacing only the left \(P\) in
  \(P\land\neg P\) gives the satisfiable \(Q\land\neg P\).
  Equisatisfiability of the replaced formulas is therefore insufficient.

## Routing and preservation

The body is input exactly once at [p02.tex:7](C:/Dev/the-methods-of-reason/handbook/parts/p02.tex:7), immediately after scope-SRC-01817-01898 and before scope-SRC-01899-01945.
The annex is input exactly once at [annex/p02.tex:11](C:/Dev/the-methods-of-reason/handbook/annex/p02.tex:11), before the later Hilbert proof file.
With the root's explicit authorization, the annex scope list now also names
substitution and replacement while preserving every previous subject.

The matching existing P2 input guard contains the new seam at
[check_compendium_volume_manifest.py:785–789](C:/Dev/the-methods-of-reason/tools/check_compendium_volume_manifest.py:785).
The earlier PA2 input and its guard remain unchanged.

Removing only these authorized routing/scope/guard additions reproduces the
three pre-task file hashes exactly. The inactive lead, grammar, valuation and
feedback files still have their pre-task hashes. No source fragment, style,
canonical bibliography/symbol file, generated view or old inactive file was edited.

## Read-back and check limits

The entire final body, lines 1–181, and entire final annex, lines 1–174, were
read back from the saved files in numbered, nontruncated output. The changed
body-driver seam, complete 16-line annex driver and modified guard block were
also read back.

Focused source-structure checks found exactly two body theorems, two matching
annex items, two annex proof environments, no body proof environment, one input
per driver, balanced environment nesting and no uses of the source-only
Prop/Fm/CPL/False/True macros. The changed Python guard parsed successfully.
These are author checks, not a full static admission gate.

No software test suite, manuscript build, render, new test infrastructure or
independent review was performed. No new calculus or stronger arbitrary-premise
theorem was introduced. Independent review and later production checks remain.

## Before/after hashes

| File | Before SHA256 | After SHA256 |
|---|---|---|
| handbook/parts/p02/propositional-substitution.tex | New file | 5B39B8DC52B60442850707C6D4DF2C7E853929FC52541F85D839986BFD8DC146 |
| handbook/annex/p02/propositional-substitution.tex | New file | 4B28ADAFF5F2A3217ED4808B2EA459639635EB957F7FFFD22347071657EFC5DF |
| handbook/parts/p02.tex | BF76EB346924365E7D06EB3596CF22B266D61EA6FF24096B6C527FD9F8151E0C | 3576CC349C1245430B30531C266E0483144C5470B2F61A894C0D16D38522FBDD |
| handbook/annex/p02.tex | CCEE5795283CEDCB60F0ADC795FA56CBEB24E91757441E5BCA4FDFE3447E04A6 | 65C7B1D7300401CFF444DD324FD6C44951B3AB9D8ACB9B07D58C41739E9BC87F |
| tools/check_compendium_volume_manifest.py | 8DD16AC7EFA3A7E1C58C6F7A6A7CFADEB9D40F2984401A4361A0030DBCEC37C7 | BE4CB2E48E8F09A006A0082D141F087EF2BDDA359FCD247A505EDD945F1193B1 |

Inspected authority/lead files, unchanged by this task:

| File | SHA256 |
|---|---|
| handbook/parts/p02/propositional-syntax-semantics.tex | 94338430C4E87CF1B9228274B15ADBAC052C704EB0B4E81A48B4587A59217B56 |
| handbook/restoration/inherited-01661-01816.tex | FB12D36A183AC0FDF5C8B2F8A1BBC09238526FDB03F75364A6DC18239913EC3E |
| handbook/restoration/inherited-01817-01898.tex | 499FEC700936D0625769D7C09AA2BC5FD1F6D976B9EAB1A9CBC8EDFE8CAFB9C4 |
| handbook/restoration/inherited-15638-16742.tex | 993A3153C9CA856F761B5650C312E85E2BE78FA23B8AFC8EDCD4E87A7B2983BF |


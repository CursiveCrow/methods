# NOW-03a: repairs of topic M1 and source SF-1

Date: 7 September 2026, America/Los_Angeles; 8 September UTC.
Standing: bounded author repair returned for focused independent rechecks.
Both reported missing hypotheses are now explicit in the active body and
annex. This note grants no independent acceptance, formal admission, D3,
PT-1 closure or GL result.

## Exact before and after identities

| File | Before | After |
| --- | --- | --- |
| `handbook/parts/p05/pa-numeral-proof-builders.tex` | 490 lines; `E805B3D17CC04419E9105BDC98A5B42483E91DE90137358669019D0F23D4858F` | 501 lines; `413117B591123F5B12C78124D1EC13ACE9B15CB3CBB61445DBE9CB6ED8F97BD0` |
| `handbook/annex/p05/pa-numeral-proof-builders.tex` | 628 lines; `576AD536A4F7484FF2E2968B3C32FB6D685C0288B16A9007B4E89A7234B0B65A` | 644 lines; `3ABD15F81D47E8D5078C46B496DFBE4361ECBF36C25C54CB589CD9D7DC84237E` |

The before hashes were checked against the live files before editing. The
after hashes and changed passages were reread after the edits. Only these
two manuscript files and this repair note were written. Earlier author and
review reports remain preserved at their original identities.

## Review evidence and definition checks

The concrete counterexamples and required repairs were read in:

- `spec/verification/edition-2026-p5-numeral-topic-review.md`, finding M1,
  beginning at line 60; SHA256
  `6F4BB12DC45A3EFB7ACB91C71DCC2887BC5CB3B920A9529F0A00BE9A7A0E416A`.
- `spec/verification/edition-2026-p5-numeral-source-review.md`, finding SF-1,
  lines 56–68; SHA256
  `6F251CF1B5ECBA1A40A79333B97C0C092DC3DFAAF720BC2A2824E657FF7B6B23`.

The surrounding no-renaming table, numeral-invariance passage, Clash
definition, success promise and peeling proof were read directly. The
existing selected-checker type-failure rule at
`handbook/parts/p05/pa-checker-arithmetization.tex:229–233`, its row/tree
definitions at 297–393, and the fixed cons equations in
`handbook/restoration/inherited-09262-09327.tex:187–196` were also checked.
The reports locate the defects; those actual equations determine the repair.

## M1: retain the replacement-term hypothesis

Before the repair, body lines 90–93 said substitution leaves a numeral
unchanged without a replacement-term condition, and annex lines 82–85
explicitly asserted `ns(nu(n),i,u)=nu(n)` before transferring it to `sub`.
The table's original type guard already rejected an invalid replacement.

The review's concrete instance is `n=i=u=0`. The number 0 is an empty-list
code and is not a term; the zero-term code is
`nu(0)=N_1()=C(1,0)=2`. Therefore both `ns(nu(0),0,0)` and
`sub(nu(0),0,0)` have value 0. The unqualified former assertion would give
`0=2` and was false.

The repaired body, lines 90–98, explicitly states with universal numerical
closure:

```text
Tm(u)=1 ->
  (ns(nu(n),i,u)=nu(n) and sub(nu(n),i,u)=nu(n)).
```

The adjacent iterate assertion keeps its own explicit `Tm(t)=1` condition.
The annex, lines 74–90, now retains that the variable-free replacement is a
term, and carries `Tm(u)=1` as a parameter through the numeral induction.
At its zero case this passes the replacement type guard; the successor case
uses the same guard and the preceding successful row. This yields both
`nc=1` and the unchanged `ns` result before execution equation (1) is used
to obtain the same `sub` result under the same hypothesis.

Annex lines 92–98 explicitly preserve the invalid-input behavior: if
`Tm(u)=0`, all three table fields and the selected substitution output are
zero for every input expression code. It gives the numerical zero-code
counterexample to distinguish 0 from `nu(0)`. No type test, failure value,
substitution-machine transition, table update or numeral constructor changed.

## SF-1: expose the full Clash success premise

Before the repair, the named success premise at body lines 328–329 gave
`k>b` and the required root, while the successful-row promise at 409–411
referred back to that premise. The annex proof at 370–372 also assumed a
successful input tree. Its local successful-tree definition already meant
the exact `Tree(R)=1` test.

The review's counterexample is
`R=[[18,c,0,[o],0]]`, with `c=Eq(s(o),o)`, `t=o`, `k=1`, `b=0`.
This has the required root and structural parent count, but its identity
row fails: parameter `[o]` requires root `Eq(o,o)`. At peeling bound zero
the builder retains and copies this failed row. It cannot promise successful
rows for this input merely from its root.

The repaired body, lines 333–338, now names the complete success premises,
in addition to its existing term domain:

```text
Tree(R)=1, k>b, f(R)=Eq(it(t,k),nu(b)).
```

The successful-row promise repeats all three conditions at body lines
418–424. The annex assumption at lines 385–388 now uses exactly the same
`Tree(R)=1`, inequality and root equation. Its existing peeling induction
already proves the assertion under these hypotheses.

The numerical Clash expression and its peeling recurrence did not change.
In particular, no new branch forcing invalid-tree inputs to zero was added.
It remains the same total raw-record construction, whose success theorem
now explicitly requires the actual successful-input-tree test. The
counterexample is excluded by `Tree(R)=0`, rather than being assigned a
different numerical output. No vague replacement definition of “raw” or
“successful” was introduced.

## Preservation of all existing construction cases

Every later substitution invocation supplies a term: a numeral, a variable
code, its successor, a successor iterate of a permitted term, a term in one
of the fixed axiom/context instances, or a fixed term's closed numeral
instance. Their type assertions are proved by the existing syntax and
constructor inductions. A numerical arithmetic argument equal to zero is
passed as the term code `nu(0)=2` where a replacement is required; it is not
passed as the invalid code 0. The new explicit M1 premise is therefore
available at the existing axiom, equality, arithmetic, comparison and
literal-transport calls. The no-renaming theorem under `nc=1` and its machine
execution invariant are unchanged.

Every actual Clash input is also successful. Disequality starts from the
one-row marked equality assumption; its reverse orientation applies the
already proved symmetry template. Negative weak comparison supplies the
transitivity join of a successful right-addition equality proof and its
marked minor. Negative strict comparison uses the corresponding successful
left-addition proof, with its iterate-code identity. The row-joining theorem
gives `Tree(R)=1` in each case before the peeling induction begins. Thus
the added SF-1 premise is already established at every actual call.

The zero and empty cases persist: numeral zero remains a term, identity has
an empty open list, a zero peeling bound starts with the verified input tree,
weak comparison at equal endpoints uses its zero numeral witness, and
negative strict comparison at equal endpoints retains its positive successor.
All rule tags, row offsets, parameters, matrices, labels, axiom leaves,
numeric recursion equations and literal conclusion codes are unchanged.

## Return standing

Author repair assessment: M1 and SF-1 are addressed on the after hashes
above and ready for focused independent rechecks. Their exact former
counterexamples are preserved as rejected inputs under the corrected
hypotheses. No test, scanner run, build, render, new subagent or independent
acceptance was performed in this repair block. The initial sandbox process
helper failed; approved elevated read commands supplied the same permitted
file reads, and the edits used the explicitly granted three-file scope.

The bounded-formula compiler, evidence-to-proof construction, D3, later
consumer repair and the separately owed GL work retain their previous open
standing. This repair record supersedes the earlier author's unqualified
assessment only for these two corrected statement locations; it does not
rewrite the historical author intake or the independent R1 reports.

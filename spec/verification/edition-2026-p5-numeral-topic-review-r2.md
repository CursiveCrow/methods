# NOW-03a focused independent mathematical recheck R2

Date: 7 September 2026, America/Los_Angeles. Reviewer context:
pa_numeral_topic_r2. Assignment: recheck M1, the explicit Clash input-tree
hypothesis, and their actual callers on the two specified current targets.

## Retrieved Content

The extracts below preserve the source text. Locations are inclusive line
ranges in the files identified in Supplementary Notes.

### Source 1: handbook/parts/p05/pa-numeral-proof-builders.tex, lines 90–98

~~~tex
In particular \(\PA\) proves that \(\nu(j)\) is a variable-free term
and, assuming \(\mathsf{Tm}(t)=1\), that
\(\mathsf{it}(s(t),j)=\mathsf{it}(t,Sj)\). With universal numerical
closure it also proves the guarded numeral-invariance assertion
\[
 \mathsf{Tm}(u)=1\ \longrightarrow
 \bigl(\mathsf{ns}(\nu(n),i,u)=\nu(n)\land
        \mathsf{sub}(\nu(n),i,u)=\nu(n)\bigr).
\]
~~~

### Source 2: handbook/annex/p05/pa-numeral-proof-builders.tex, lines 82–90

~~~tex
Retain \(\mathsf{Tm}(u)=1\) as a parameter while inducting on that
recurrence in the new table. At zero this hypothesis passes the replacement
type test, so the zero-term case gives success bit one and result \(\nu(0)\).
At the successor the same type test passes, and the predecessor induction
instance gives success bit one and the unchanged successor result. Thus
\(\mathsf{nc}(\nu(n),i,u)=1\) and
\(\mathsf{ns}(\nu(n),i,u)=\nu(n)\) under the retained hypothesis.
Equation (1) then gives \(\mathsf{sub}(\nu(n),i,u)=\nu(n)\) under that
same hypothesis, proving the body's universally closed guarded assertion.
~~~

### Source 3: handbook/parts/p05/pa-checker-arithmetization.tex, lines 202–205

~~~tex
\item At \([0,c,i,u]\), require
 \((\mathsf{Tm}(c)\lor\mathsf{Fm}(c))\mathsf{Tm}(u)=1\).
 A variable returns \(u\) if its index equals \(i\), otherwise \(c\).
 Zero and bottom return \(c\).  A unary nonbinding node prepends its child's
~~~

### Source 4: handbook/parts/p05/pa-checker-arithmetization.tex, lines 229–233

~~~tex
Start at \([1,[[0,c,i,u]],0]\), perform \(20(n(c)+1)^2\) updates,
and return the sole value exactly when the final state has success bit one,
empty command list, and a one-entry value stack; otherwise return zero.
Also return zero if the original expression/replacement type test fails.
This description is denoted \(\mathsf{sub}(c,i,u)\).
~~~

### Source 5: handbook/parts/p05/pa-numeral-proof-builders.tex, lines 333–338

~~~tex
The two cases expand to the numerical conditional in their printed order.
For the stated domain of \(t\), the asserted success premises are
\[
 \mathsf{Tree}(R)=1,\qquad k>b,\qquad
 f(R)=\mathsf{Eq}(\mathsf{it}(t,k),\nu(b)).
\]
~~~

### Source 6: handbook/parts/p05/pa-checker-arithmetization.tex, lines 385–387

~~~tex
 \mathsf{Tree}(R)&=\mathsf{sg}(\ell(R))
       \prod_{j<\ell(R)}e(e(\mathsf{Rows}(R),j),0)
       \prod_{i<\ell(R)}E(\mathsf{pc}(R,i),Z(E(i,D(\ell(R))))).
~~~

### Source 7: handbook/annex/p05/pa-numeral-proof-builders.tex, lines 385–388

~~~tex
First verify the raw contradiction constructor in \(\PA\). Assume
\(\mathsf{Tree}(R)=1\), \(k>b\), and
\(f(R)=\mathsf{Eq}(\mathsf{it}(t,k),\nu(b))\), with the stated domain
of \(t\).
~~~

---

## Supplementary Notes

### Verdict

**PASS for the current focused mathematical recheck.** M1 now has the needed
replacement-term hypothesis in both the statement and the PA induction.
The selected machine still rejects invalid replacement codes. The Clash
success assertion and its proof now use the same explicit successful-tree,
inequality, root and term-domain premises. Every actual caller examined
establishes the added hypotheses before invoking these results.

This verdict is on the present source and the specified repair questions.
Historical equality of every target byte outside the repairs is
**UNRESOLVED**: no exact R1 target snapshot or literal repair patch was
available. This limit does not identify a current mathematical defect.
The existing five other constructions were read in their present entirety;
their use of the repaired lemmas remains valid on their stated domains.
This is not a fresh proof of every earlier foundational theorem.

The bounded-formula compiler, evidence-to-proof construction, D3, PT-1
closure and the remaining GL/Solovay work remain **UNRESOLVED outside this
assignment**. This report grants no formal admission, production acceptance,
build result or rendering result.

### Frozen identities and actual reading

Repository: C:\Dev\the-methods-of-reason. HEAD checked in this run:
35d537c692bb74b532dc4aa750da381a7fe4daf2. Both target files are untracked
in that checkout, so HEAD cannot supply their R1 versions. The initial
Git ownership check was followed by a read-only invocation with a
per-command safe.directory setting; no Git configuration was written.

Whole-file SHA256 values below identify partial reads as well as full reads.
Numbered source output was used. The interrupted annex display around
lines 295–358 was retrieved separately, completing the target read.

| File relative to repository | Actual read extent | Whole-file SHA256 |
| --- | --- | --- |
| spec/verification/edition-2026-p5-numeral-topic-review.md | Complete, 1–315; prior finding and dependency locator | 6F4BB12DC45A3EFB7ACB91C71DCC2887BC5CB3B920A9529F0A00BE9A7A0E416A |
| spec/research/edition-2026-p5-numeral-review-repairs.md | Complete, 1–153; author repair claim to check | 3616A3A4C6D835D3856E00304E3BE521793DA127E3CFDB874BD6DC9F3A910C6B |
| handbook/parts/p05/pa-numeral-proof-builders.tex | Complete, 1–501 | 413117B591123F5B12C78124D1EC13ACE9B15CB3CBB61445DBE9CB6ED8F97BD0 |
| handbook/annex/p05/pa-numeral-proof-builders.tex | Complete, 1–644 | 3ABD15F81D47E8D5078C46B496DFBE4361ECBF36C25C54CB589CD9D7DC84237E |
| handbook/parts/p05/pa-checker-arithmetization.tex | Complete, 1–523 | 993418B3EB3343525C0922274CA6794F5B4FED13FFB35CB146E9995D88391DFA |
| handbook/annex/p05/pa-checker-arithmetization.tex | 1–458 of 537 | 03BAF39D646901DC307812B0D22FE8823CFEC53B3D7B85A3FF0ADF754AAF71E5 |
| handbook/parts/p05/standard-pa-proof-predicate.tex | Complete, 1–252 | 71D3E5569BFB7BAE907CA818BE65DBBCE5E48DBA86D9D8942819DCC5110331E2 |
| handbook/restoration/inherited-09262-09327.tex | Complete, 1–253 | B49A3B30AFF36050841D4F384A6BA80FCF36F4661B3C4085E58D2371B4E003CB |
| handbook/restoration/inherited-09328-09438.tex | 1–68 of 546 | A6E37FA592E81B888C14A2DA97CC70F1A05EC69BAE0CE4D36E2E60C59F09C541 |
| handbook/annex/p05/internal-proof-predicate.tex | 230–291 of 524 | F11B72E5AE8FF2407C58FA434320D08095C0C543AE8C610237EED42EAFFFA1C1 |

The seven prerequisite hashes listed in R1 were checked and all still match.
The remaining prerequisite, handbook/annex/p05/standard-pa-proof-predicate.tex,
was identity-checked only: 315 lines, SHA256
7F3E3F751832ACACFFC8F2383E2AC14A8D8DC7A9DEA2DA4B837F3A9DF648DFDF.
Its content was not reread in this focused block. The pairing/beta extension
foundation before line 230 of internal-proof-predicate.tex was likewise
not newly reverified. No current source-review or publication-review verdict
was read or used.

### M1 — Guarded numeral invariance: PASS

The actual cons equations in inherited-09262-09327.tex:187–232 give
A(1,0)=1, H(1)=A(H(0),1)=1, K(1,0)=1 and C(1,0)=2.
The grammar in inherited-09328-09438.tex:24–64 distinguishes the
empty list 0 from this nullary term constructor. The selected node test
has the explicit factor sg(c), and the syntax table rejects invalid
nodes (checker body 128–157). Consequently Tm(0)=0 and Tm(o)=1.

For n=i=u=0, the numeral is nu(0)=o=2. The new table's initial
type test (target body 55–57) forces nc=ns=cost=0, and both the
machine command guard and its final original-input guard force sub=0.
Thus the old unqualified equality would still be 0=2. The repaired
assertion does not assert that equality: its Tm(u)=1 antecedent is
false on exactly this input. The invalid case has not acquired a
different output.

For comparison, use the valid replacement u=o with n=0. The table
returns [1,2,1]; the selected command returns the zero-term code in
one update. Completion is absorbing, so the fixed final extraction
still returns 2. One successor gives nu(1)=s(o)=26: indeed
[2]=C(2,0)=4 and C(2,4)=26. Its successful table row has result
26 and cost 3. These finite calculations follow the specified
constructors and transitions, without a substitute implementation.

For the universal assertion, the PA induction retains arbitrary i,u
and the premise Tm(u)=1. At n=0 the table's zero branch produces
nc=1 and ns=o. At Sn its unary branch reads the earlier successful
nu(n) row and returns [1,s(nu(n)),2+cost]. Constructor decoding
and the internal table-prefix equations justify that lookup for
all PA numerical variables. The stronger execution equation at
target annex 33–72 then applies, because nc=1 has been proved
under the same premise. Its cost bound and the actual absorbing
state give sub=ns at the selected 20(nodes(c)+1)^2 extraction.
There is no inference from standard numerical agreement to an
unproved universally quantified PA invariant.

The companion sentence about variable-free replacements at annex
74–78 now retains the term assumption too. The current machine
definition at checker body 181–233 has the same whole-file hash as
R1; the guard and failure behavior are part of that unchanged
prerequisite.

### Replacement-term hypotheses at downstream calls: PASS

| Actual call family | Source locations in target body / annex | Term hypothesis available internally |
| --- | --- | --- |
| FE, EI, EEq and their generic local invariants | Body 125–150, 182–195; annex 182–201 | Successful applications require the actual rule tests. Checker tags 13/14 require a term replacement; tag 19 requires both endpoints to be terms. These templates do not promise validity on arbitrary numerical arguments. |
| Symmetry, transitivity, the five fixed congruence contexts | Body 152–179; annex 182–191 | A valid equality formula supplies term endpoints. The fixed context operations preserve term type; the fresh hole is a variable code. |
| Canonical induction and D_Z,D_L instances | Body 200–244; annex 215–299 | The canonical substitutions are o and s(v_i). The displayed instance parameters are o, v_0, v_1 and s(v_0). All pass the grammar. |
| Addition and multiplication recurrences | Body 266–290; annex 324–356 | Every axiom replacement is nu(m) or nu(n); intermediate equality endpoints are terms built from those numerals. |
| Right/left successor strings | Body 279–290; annex 358–369 | The stated parameter domain is a numeral, v_y or s(v_y), with y at least 3. Constructor induction proves each is a term; the outer replacement has no index 1. |
| Peeling and final q_1 instance | Body 315–330; annex 385–422 | t is o or v_y. Iterates it(t,L(k,Sj)) and it(t,D(L(k,b))) are terms by induction; the other replacement is a numeral. An iterate of length zero returns the term t. |
| Positive comparison witnesses | Body 351–365; annex 439–450 | Both witnesses are nu of a numerical value. In particular a witness value zero supplies nu(0)=2, never the invalid term code 0. |
| Negative comparison minor and existential discharge | Body 369–393; annex 452–490 | The explicit replacement is v_(i+3); strict comparison also uses s(v_(i+3)). Both have term type for every numerical i. |
| Fixed terms and both literal transports | Body 427–471; annex 538–566, 585–621 | The formation induction proves u^nu,v^nu variable-free terms. The two equality eliminations replace their hole by those terms or normalized numerals. |

These cases cover the substitution uses in the current target and their
local templates, including implicit calls inside the axiom and equality
constructors. A literal search through handbook for the exact identifiers
thm:p05-builder-nocapture, mathsf{nc}, mathsf{ns} and mathsf{Clash}
found no additional theorem caller outside the two target files; the
registry occurrence is descriptive. That search is not a claim about
arbitrarily renamed or future consumers.

### Explicit Tree premise for Clash: PASS

The term domain at body 315–317, success premises at 333–338,
success promise at 418–424 and induction hypotheses at annex
385–388 agree. The actual Tree description includes nonemptiness,
every row bit, and the parent-count product. It permits intermediate
open roots and temporary assumptions; it does not itself require a
sentence root or an axiom test on the open leaves.

Independently recompute the author's malformed case using the actual
constructors. With o=2 and s(o)=26,
Eq(o,o)=C(5,C(2,C(2,0)))=C(5,26)=523, whereas
Eq(s(o),o)=C(5,C(26,C(2,0)))=C(5,470)=113521.
Set c=113521 and R=[[18,c,0,[o],0]]. Its single row has the
required field lengths, a formula conclusion, no premises and zero
parent count. But checker tag 18 requires the literal conclusion
Eq(o,o)=523. Since 113521 differs from 523, its additional equality
test is zero; Rows(R) stores [0,0] and Tree(R)=0.

For t=o,k=1,b=0, this R nevertheless has the displayed equality
root Eq(it(o,1),nu(0)). At bound zero P returns R. The current
Clash expression copies that failed row into its first block;
the subsequent q_1 instance and bottom row cannot remove its
zero factor from Tree. The explicit Tree(R)=1 premise therefore
excludes the former counterexample for the correct reason.

The repaired proof's base at j=0 uses Tree(R)=1 directly and
L(k,0)=k, L(b,0)=b. At j<b, k>b gives positive k-j and b-j.
The q_2 instance substitutes the term it(t,L(k,Sj)) and the
numeral nu(L(b,Sj)), so its antecedent is exactly the preceding
root, and the join preserves Tree. At j=b, L(k,b)>0 and its
predecessor iterate is a term. The q_1 instance is the negation
of the exact remaining equality, licensing tag 10. This proves
the PA induction with the four stated parameters retained,
including b=0. The numerical constructor has no Tree branch;
the added premise belongs to its successful-output theorem.

### Every actual Clash caller: PASS

There are four explicit call sites in the current body.

| Body location | Input supplied to Clash | Why Tree(R)=1 and the exact root hold |
| --- | --- | --- |
| 344 | L(Eq(nu(m),nu(n)),1), under n<m | A one-row tag-0 assumption has a valid formula, empty premise/parameter lists, one row bit and zero root parent count. Its root is Eq(it(o,m),nu(n)). |
| 345 | Sym(L(Eq(nu(m),nu(n)),1)), under m<n | The same assumption is successful; the symmetry join preserves Tree and reverses the endpoints. Its root is Eq(it(o,n),nu(m)). |
| 379 | Tr(Sym(R_right(v_y,m)),K), under m>n | The successor-string invariant supplies the successful equality tree, and K is the successful tag-0 assumption Eq(a(v_y,nu(m)),nu(n)). Symmetry and transitivity meet at the identical addition term and give Eq(it(v_y,m),nu(n)). |
| 384 | Tr(Sym(R_left(s(v_y),m)),K), under m>=n | The permitted term s(v_y) gives the successful left-addition tree. K has root Eq(a(nu(m),s(v_y)),nu(n)). The joins give Eq(it(s(v_y),m),nu(n)); the proved iterate identity makes this Eq(it(v_y,Sm),nu(n)). Also Sm>n. |

Here y=i+3 is at least 3 in PA. The successful-tree assertions
follow from the actual row tests and the current join theorem,
not merely from a matching root. Copies remain in disjoint
intervals, so the extra root reference gives each old root one
parent. The original marked assumption survives once until its
specified later discharge; the added input-tree premise creates
no new leaf or discharge requirement.

### Current remainder and historical limit

All current target definitions and proofs were read. The generic joins
still require their local side conditions; the arithmetic recurrences
retain the declared term domains; comparison branches retain their
numerical guards; and fixed literal transport retains the original
comparison binder and uses closed term instances. The added guards
are supplied at these invocations and do not change their desired
literal root equations. No new mathematical defect was found in
those current uses.

The seven prerequisite whole-file hashes match the R1 record exactly,
which independently establishes that those prerequisite bytes,
including the selected substitution and row/tree machine, are unchanged.
Both current target hashes match the assigned repaired identities.
However, old target hashes alone cannot establish which target
passages changed. With both targets untracked and no exact before
snapshot or patch supplied, this reviewer does not claim an independently
verified line-by-line or byte-by-byte unchanged remainder of those two
targets. The repair note's statement that their remaining constructors
were preserved is an author claim, not the evidence for the present
mathematical PASS.

### Continuation and scope of the return

No further manuscript repair is requested by this focused mathematical
recheck. The integrator may use the M1 and Clash caller results on these
exact hashes in the remaining review process. An exact historical
comparison, if required as a separate gate, needs the R1 target bytes.
Body 494–501 and annex 640–642 retain the open compiler and
evidence-to-proof boundary; no D3, PT-1 or GL conclusion is licensed here.

Only this report was written. No manuscript/shared record, test, build,
render, subagent, or formal admission was performed. Source hashes were
rechecked at return. The concrete cons arithmetic and row-domain checks
above are mathematical calculations from the selected definitions.

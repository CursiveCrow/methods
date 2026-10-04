# NOW-03a: independent source and dependency recheck, R2

## Retrieved Content

All paths in this report are relative to `C:\Dev\the-methods-of-reason`.
Retrieval date: 8 September 2026 UTC; 7 September 2026 America/Los_Angeles.
NB/NA identify the numeral-builder body/annex; CB/CA identify the selected-checker body/annex; DB/DA identify the standard PA proof-predicate body/annex.

### Source 1: `handbook/parts/p05/pa-numeral-proof-builders.tex`, lines 315–338

```tex
\begin{hbdefinition}{def:p05-numeral-literal-builders}{Disequality and both comparison polarities}
First define a contradiction constructor. For \(t=o\) or \(t=v_y\)
with \(y\geq3\), use numerical parameters \(k,b\) and a raw tree \(R\).
The counter \(j\) is last:
\[
\begin{aligned}
 P(t,k,b,R,0)&=R,\\
 P(t,k,b,R,Sj)&=
 \begin{cases}
 \mathsf{MP}^{\rm row}\bigl(P(t,k,b,R,j),
    \mathsf A_2(\mathsf{it}(t,L(k,Sj)),\nu(L(b,Sj)))\bigr),&j<b,\\
 P(t,k,b,R,j),&j\geq b,
 \end{cases}\\
 \mathsf{Clash}(t,k,b,R)&\defeq
 \mathsf B\bigl(P(t,k,b,R,b),
                    \mathsf A_1(\mathsf{it}(t,D(L(k,b))))\bigr).
\end{aligned}
\]
The two cases expand to the numerical conditional in their printed order.
For the stated domain of \(t\), the asserted success premises are
\[
 \mathsf{Tree}(R)=1,\qquad k>b,\qquad
 f(R)=\mathsf{Eq}(\mathsf{it}(t,k),\nu(b)).
\]
```

### Source 2: `handbook/parts/p05/pa-numeral-proof-builders.tex`, lines 418–424

```tex
Under the stated term domain and the premises \(\mathsf{Tree}(R)=1\),
\(k>b\) and \(f(R)=\mathsf{Eq}(\mathsf{it}(t,k),\nu(b))\), the
contradiction constructor has successful rows, root \(\mathsf{bc}\), and
retains its input open leaves together with unmarked \(q_1,q_2\) leaves.
These are internal checker invariants, including
zero numeral arguments, a zero peeling bound, equal comparison endpoints,
and the premise-free identity case.
```

### Source 3: `handbook/annex/p05/pa-numeral-proof-builders.tex`, lines 385–400

```tex
First verify the raw contradiction constructor in \(\PA\). Assume
\(\mathsf{Tree}(R)=1\), \(k>b\), and
\(f(R)=\mathsf{Eq}(\mathsf{it}(t,k),\nu(b))\), with the stated domain
of \(t\).
Induct on \(j\leq b\) with the invariant that \(P(t,k,b,R,j)\) is a
successful tree with root
\[
 \mathsf{Eq}(\mathsf{it}(t,L(k,j)),\nu(L(b,j))),
\tag{8}
\]
and with exactly the old open leaves of \(R\), shifted as its copied tree,
together with unmarked \(q_2\) leaves. This open-list assertion can be
written using the join's exact shift/concatenation equations; in particular
every old marked leaf survives with its multiplicity.

At zero, subtraction's zero equation gives (8) and the record is \(R\).
```

### Source 4: `handbook/parts/p05/pa-checker-arithmetization.tex`, lines 380–393

```tex
Define the parent count and record test by
\[
\begin{aligned}
 \mathsf{pc}(R,i)&=\sum_{j<\ell(R)}
                    \sum_{v<\ell(e(r_j,2))}E(e(e(r_j,2),v),i),\\
 \mathsf{Tree}(R)&=\mathsf{sg}(\ell(R))
       \prod_{j<\ell(R)}e(e(\mathsf{Rows}(R),j),0)
       \prod_{i<\ell(R)}E(\mathsf{pc}(R,i),Z(E(i,D(\ell(R))))).
\end{aligned}
\]
For \(\ell(R)>0\), put
\(\mathsf{root}(R)=f_R(D(\ell(R)))\) and
\(\mathsf{open}(R)=e(e(\mathsf{Rows}(R),D(\ell(R))),1)\);
both have default zero for the empty record.
```

### Source 5: `handbook/annex/p05/pa-numeral-proof-builders.tex`, lines 122–126

```tex
Work with the exact \(\mathsf{Rows}\), \(\mathsf{Tree}\), parent-count
and open-list descriptions. For clarity, a successful tree assertion means
\(\mathsf{Tree}(R)=1\); this includes nonemptiness, every row bit equal
to one, and the exact parent-count product. It does not yet impose a
sentence root or an axiom test on open assumptions.
```

### Source 6: `handbook/parts/p05/pa-numeral-proof-builders.tex`, lines 340–348

```tex
For \(m\ne n\), let \(c=\mathsf{Eq}(\nu(m),\nu(n))\), and set
\[
 R_{\ne}(m,n)\defeq
 \begin{cases}
 \mathsf{NI}(\mathsf{Clash}(o,m,n,\mathsf L(c,1)),c,0),&n<m,\\
 \mathsf{NI}(\mathsf{Clash}(o,n,m,\mathsf{Sym}(\mathsf L(c,1))),c,0),&m<n,\\
 0,&m=n.
 \end{cases}
\]
```

### Source 7: `handbook/parts/p05/pa-numeral-proof-builders.tex`, lines 369–385

```tex
For either negative comparison put \(y=i+3\), let \(c\) be the matrix
of that comparison at \(\nu(m),\nu(n)\), and let
\(C=\mathsf{Ex}(i,c)\). Take
\[
 H=\mathsf L(C,1),\qquad
 K=\mathsf L(\mathsf{sub}(c,i,v_y),2).
\]
For \(m>n\), set
\[
 V_{\leq}=\mathsf{Tr}(\mathsf{Sym}(R_{\rm right}(v_y,m)),K),\qquad
 W_{\leq}=\mathsf{Clash}(v_y,m,n,V_{\leq}).
\]
For \(m\geq n\), set
\[
 V_<=\mathsf{Tr}(\mathsf{Sym}(R_{\rm left}(s(v_y),m)),K),\qquad
 W_<=\mathsf{Clash}(v_y,Sm,n,V_<).
\]
```

### Source 8: `handbook/annex/p05/pa-numeral-proof-builders.tex`, lines 305–322

```tex
Use the following arithmetic invariant for the raw trees:
\[
\begin{split}
 \mathsf{Safe}(R,c)\quad\text{means}\quad&
 \mathsf{Tree}(R)=1\land f(R)=c\\
 &\land\forall j<\ell(\mathsf{open}(R))\,
   \bigl(\lambda_R(\mathsf{entry}(\mathsf{open}(R),j))=0
    \land\mathsf{mem}(f_R(\mathsf{entry}(\mathsf{open}(R),j)),
                                             \mathcal A_*)=1\bigr).
\end{split}
\tag{7}
\]
Every operation in (7) is an already specified graph, and the fixed list
\(\mathcal A_*\) was verified in the preceding item. Thus (7) is an
arithmetic formula licensed for induction. If its root is a sentence,
expansion of the selected checker proves
\(\mathsf{Prf}^{19}_{\PA}(\mathsf{pack}(R),c)\). No bound on the
numerical magnitude of \(R\) is needed for this implication.
```

### Source 9: `handbook/parts/p05/pa-numeral-proof-builders.tex`, lines 90–98

```tex
In particular \(\PA\) proves that \(\nu(j)\) is a variable-free term
and, assuming \(\mathsf{Tm}(t)=1\), that
\(\mathsf{it}(s(t),j)=\mathsf{it}(t,Sj)\). With universal numerical
closure it also proves the guarded numeral-invariance assertion
\[
 \mathsf{Tm}(u)=1\ \longrightarrow
 \bigl(\mathsf{ns}(\nu(n),i,u)=\nu(n)\land
        \mathsf{sub}(\nu(n),i,u)=\nu(n)\bigr).
\]
```

### Source 10: `handbook/annex/p05/pa-numeral-proof-builders.tex`, lines 82–98

```tex
Retain \(\mathsf{Tm}(u)=1\) as a parameter while inducting on that
recurrence in the new table. At zero this hypothesis passes the replacement
type test, so the zero-term case gives success bit one and result \(\nu(0)\).
At the successor the same type test passes, and the predecessor induction
instance gives success bit one and the unchanged successor result. Thus
\(\mathsf{nc}(\nu(n),i,u)=1\) and
\(\mathsf{ns}(\nu(n),i,u)=\nu(n)\) under the retained hypothesis.
Equation (1) then gives \(\mathsf{sub}(\nu(n),i,u)=\nu(n)\) under that
same hypothesis, proving the body's universally closed guarded assertion.

For an invalid replacement, \(\mathsf{Tm}(u)=0\), the original type guards
instead give \(\mathsf{nc}(c,i,u)=\mathsf{ns}(c,i,u)=
\mathsf{cost}(c,i,u)=0\) and \(\mathsf{sub}(c,i,u)=0\) for every \(c\).
For example, the numerical input \(u=0\) is an empty-list code, not the
zero-term code \(\nu(0)=N_1()=C(1,0)=2\). At \(n=i=u=0\), both
substitution outputs are therefore zero, while \(\nu(0)=2\). These
unchanged failure values explain the replacement-term hypothesis.
```

### Source 11: `handbook/parts/p05/pa-checker-arithmetization.tex`, lines 202–207

```tex
\item At \([0,c,i,u]\), require
 \((\mathsf{Tm}(c)\lor\mathsf{Fm}(c))\mathsf{Tm}(u)=1\).
 A variable returns \(u\) if its index equals \(i\), otherwise \(c\).
 Zero and bottom return \(c\).  A unary nonbinding node prepends its child's
 substitution command and \([2,k(c)]\).  A binary node prepends the left
 child's command, the right child's command, and \([3,k(c)]\), in that order.
```

### Source 12: `handbook/parts/p05/pa-checker-arithmetization.tex`, lines 229–233

```tex
Start at \([1,[[0,c,i,u]],0]\), perform \(20(n(c)+1)^2\) updates,
and return the sole value exactly when the final state has success bit one,
empty command list, and a one-entry value stack; otherwise return zero.
Also return zero if the original expression/replacement type test fails.
This description is denoted \(\mathsf{sub}(c,i,u)\).
```

### Source 13: `handbook/restoration/inherited-09262-09327.tex`, lines 187–196

```tex
\begin{example}[Specified graphs for the governing pairing and cons]
\label{ex:p05-pa-pair-cons-graphs}
The following equations are finite primitive recursive descriptions, in the
order displayed:
\[
\begin{aligned}
 A(x,0)&=x,& A(x,Sn)&=S(A(x,n)),\\
 H(0)&=0,& H(Sn)&=A(H(n),Sn),\\
 K(a,b)&=A(H(A(a,b)),b),& C(a,b)&=S(K(a,b)).
\end{aligned}
```

### Source 14: `handbook/parts/p05/pa-numeral-proof-builders.tex`, lines 201–208

```tex
For the seven literal constants \(q_1,\ldots,q_7\), put
\[
 \mathsf A_j(t_0,\ldots,t_{r-1})\defeq
  \mathsf{FE}(\cdots\mathsf{FE}(\mathsf L(q_j,0),t_0)\cdots,t_{r-1}),
\]
where \(r=1\) for \(j=1,3,4,6\), and \(r=2\) for \(j=2,5,7\).
The order is the printed outside-in order, indices 0 then 1 when there are
two binders. No \(q_j\) instance is an assumption leaf.
```

### Source 15: `handbook/parts/p05/standard-pa-proof-predicate.tex`, lines 104–108

```tex
Every unaccepted input has value zero.  The definition applies no additional
alpha-equivalence, logical-equivalence, term-instance or theoremhood closure.
An alpha-equivalent formula is accepted only if it independently has one
of the displayed literal forms.  Let \(\PA^{\rm d}\) be the set of
sentences whose codes this predicate accepts.
```

### Source 16: `handbook/parts/p05/pa-numeral-proof-builders.tex`, lines 494–501

```tex
\paragraph{The next construction.}
The next component combines these literal builders through the connectives and
marked bounded quantifiers of each fixed bounded formula. It must still
construct finite case enumeration, convert it to a quantified derivation, and
verify dependent substitutions and all discharge/freshness conditions. The
literal construction above supplies its arithmetic leaves. It does not itself
establish the bounded-formula compiler, the evidence-to-proof theorem, D3 or
the remaining provability-logic results.
```

---

## Supplementary Notes

### Verdict and scope

**PASS for the focused current-source recheck:** SF-1 is repaired; the related replacement-term hypothesis matches the selected checker; all four concrete `Clash` calls supply the repaired hypothesis. The current constructions use the selected syntax, row tests, graph functions and axiom convention. No new source/dependency defect was found in this bounded recheck.

**UNRESOLVED for historical byte preservation:** an exact inverse or diff from the current target files to the two R1 hashes was not established. The R1 target files are untracked in the inspected Git state, no R1 snapshot or literal edit patch was supplied, and the coordinating reviewer confirmed that neither was available in its current context. The coordinator directed a full current-source read and explicit preservation limit instead of guessing earlier wording. Thus this report does not certify that the two hypothesis repairs are the only byte changes since R1. The author repair note supplies no independent evidence for that claim. There is no FAIL finding in the assigned source scope.

This distinction concerns the target body and annex. The whole-file hashes of all five governing dependency files actually checked here equal their hashes recorded in source R1, which independently establishes preservation of those dependency files. The current construction assessment below comes from the actual LaTeX, not the author's conclusions.

### Actual reads and exact identities

The complete R1 source report and author repair note were read. No current topic review or publication review was read. The following manuscript ranges were read directly with numbered output; neither complete target read was truncated. Whole-file hashes were measured independently of the read ranges. A second hash read after all manuscript reads confirmed the same two current target identities. Each quoted block was compared line by line against its cited source range; all 16 blocks match the source line text exactly.

| File | Actual read ranges | SHA-256 |
| --- | --- | --- |
| NB: `handbook/parts/p05/pa-numeral-proof-builders.tex` | 1–501, complete | `413117B591123F5B12C78124D1EC13ACE9B15CB3CBB61445DBE9CB6ED8F97BD0` |
| NA: `handbook/annex/p05/pa-numeral-proof-builders.tex` | 1–644, complete | `3ABD15F81D47E8D5078C46B496DFBE4361ECBF36C25C54CB589CD9D7DC84237E` |
| CB: `handbook/parts/p05/pa-checker-arithmetization.tex` | 29–418 | `993418B3EB3343525C0922274CA6794F5B4FED13FFB35CB146E9995D88391DFA` |
| CA: `handbook/annex/p05/pa-checker-arithmetization.tex` | 258–455 | `03BAF39D646901DC307812B0D22FE8823CFEC53B3D7B85A3FF0ADF754AAF71E5` |
| DB: `handbook/parts/p05/standard-pa-proof-predicate.tex` | 1–113 | `71D3E5569BFB7BAE907CA818BE65DBBCE5E48DBA86D9D8942819DCC5110331E2` |
| DA: `handbook/annex/p05/standard-pa-proof-predicate.tex` | 1–44 | `7F3E3F751832ACACFFC8F2383E2AC14A8D8DC7A9DEA2DA4B837F3A9DF648DFDF` |
| `handbook/restoration/inherited-09262-09327.tex` | 187–233 | `B49A3B30AFF36050841D4F384A6BA80FCF36F4661B3C4085E58D2371B4E003CB` |
| `spec/verification/edition-2026-p5-numeral-source-review.md` | Complete | `6F251CF1B5ECBA1A40A79333B97C0C092DC3DFAAF720BC2A2824E657FF7B6B23` |
| `spec/research/edition-2026-p5-numeral-review-repairs.md` | Complete, locator and claimed repair scope only | `3616A3A4C6D835D3856E00304E3BE521793DA127E3CFDB874BD6DC9F3A910C6B` |

The historical R1 target identities recorded in the source report are body `E805B3D17CC04419E9105BDC98A5B42483E91DE90137358669019D0F23D4858F` (490 lines) and annex `576AD536A4F7484FF2E2968B3C32FB6D685C0288B16A9007B4E89A7234B0B65A` (628 lines). Those two historical byte sequences were not recovered in this recheck.

### SF-1: exact checker hypothesis and concrete callers

NB 334–338, NB 418–421 and NA 385–388 state the same three numerical premises, retaining the same term domain from NB 316–317. The exact internal `Tree` expression at CB 385–387 requires a nonempty list, all successful row bits, and the root/nonroot parent counts. NA 122–126 expressly uses that meaning. This supplies the previously missing base-case success assertion for `P(...,0)=R`; NA 400–422 then proves the peeling step and final contradiction with the exact `q_2` and `q_1` instances. The zero peeling bound requires this successful initial tree just as the positive bound does.

The four concrete body calls were found by an exhaustive literal `Clash` search in both target files and checked directly:

| Call site | Source of `Tree=1` and the remaining premises | Result |
| --- | --- | --- |
| NB 344, `Clash(o,m,n,L(c,1))` | Numeral terms make `c` a formula; the one-row tag-0 assumption has the required arities, no references and zero root parent count under CB 316–334, 380–387. Its root is `Eq(it(o,m),nu(n))`; the branch gives `m>n`. | PASS |
| NB 345, `Clash(o,n,m,Sym(L(c,1)))` | The same successful assumption tree, followed by the equality symmetry template (NB 152–167; NA 182–191), supplies a successful tree with root `Eq(nu(n),nu(m))`. The branch gives `n>m`. | PASS |
| NB 379, `Clash(v_y,m,n,V_le)` | NA 305–369 proves `Safe` for the right-addition tree, explicitly including `Tree=1`. The minor `K` is a successful tag-0 formula assumption because its replacement `v_y` is a term. Successful symmetry and transitivity joins give root `Eq(it(v_y,m),nu(n))`. The branch gives `m>n`, and `y=i+3>=3`. | PASS |
| NB 384, `Clash(v_y,Sm,n,V_<)` | The left-addition `Safe` invariant applies to permitted term `s(v_y)`. The minor is a successful tag-0 formula assumption; symmetry and transitivity give `Eq(it(s(v_y),m),nu(n))`. The internal iterate identity identifies the left term with `it(v_y,Sm)`. The branch `m>=n` gives `Sm>n`, and `y>=3`. | PASS |

The join proof at NA 128–180 uses the actual row and parent-count equations; CA 325–454 supplies the underlying offset, row-bit and parent-count arguments. These proofs establish the needed successful-tree facts even for intermediate open formulas. No sentence-root or axiom-leaf condition is silently substituted for `Tree=1`.

The original SF-1 invalid identity-row input remains outside the success theorem: with parameter `[o]`, tag 18 requires `Eq(o,o)` (CB 370), so its proposed root `Eq(s(o),o)` gives row bit zero and therefore `Tree=0`. NB 321 and 328–330 continue to give a total raw-record construction; the current success premise does not assert a new numerical failure branch for invalid trees.

### Replacement-term guard and source behavior

NB 55–75 gives three zero fields whenever the replacement is not a term. CB 202–203 applies the corresponding type test before any variable, zero or bottom command case, and CB 229–233 explicitly returns zero upon original type failure. Therefore the new NA 92–98 failure statement applies to every input expression code, including a valid numeral. The guarded body statement at NB 90–98 and its induction at NA 80–90 use the same `Tm(u)=1` premise throughout.

CB 130–146 requires a positive constructor node for every grammar case, so numerical code zero is not a term. Its constructor equation gives `N_1()=C(1,0)`. Direct substitution in inherited-09262-09327 193–195 gives `A(1,0)=1`, `H(1)=A(0,1)=1`, `K(1,0)=1`, and `C(1,0)=2`. Thus the explicit invalid-input example agrees with the actual arithmetic coding. This is a calculation from displayed equations, not an execution test.

All concrete affected replacements are typed: numerals (NA 80–81), variables and successors from the syntax cases (CB 136–157), successor iterates in the permitted term domain (NB 36–40 and 287–290; NA 358–369, 409–411), fixed axiom instances (NB 200–244; NA 217–299), and closed numeral instances of fixed terms (NA 560–566). Successful equality roots provide typed endpoints to the symmetry/transitivity templates; the displayed fixed contexts preserve term type. Literal transport uses these same closed terms (NA 585–610). The repaired guard is consequently available at these calls, including numeral-zero arguments.

### Current construction and axiom fidelity

The actual NB 104–180 templates retain the selected premise order, rule tags and typed parameters from CB 316–374. The arithmetic recurrences at NB 266–290 and their NA 324–369 proofs use the exact `A` and `M` equations: addition is recursion on the second argument; multiplication has successor value `A(M(m,n),m)` (CB 31 and inherited-09262-09327 193). The peeling expression at NB 321–330 uses the selected `D,L` equations (CB 29–32). These are source-compatible current equations; the absent historical inverse prevents a byte-identity assertion about their R1 target text.

The seven literal `q_j` definitions in DB 24–34 and their decoded forms in DA 8–43 match the current instance chains in NB 201–208 and NA 217–223. The two derived constants continue to use canonical induction leaves with their displayed matrices and parameter prefixes (NB 210–244; NA 225–299; DB 45–109; CB 259–295). Their later instances copy the actual derivations. The direct checker still tests the literal seven constants or the canonical induction reconstruction (CB 282–294); it gains no term-instance or theoremhood closure. All five dependency hashes match source R1.

The complete current body and annex were also read through their fixed-term and literal transport conclusions. NB 494–501 and NA 640–642 retain the open bounded-formula and evidence-to-proof dependencies. No D3 theorem or formal acceptance is supplied by these passages or by this review.

### Continuation and authority boundary

The source hypothesis repairs can proceed to integration at the two current target hashes. If integration requires proof that every other target byte is unchanged, recover the actual R1 byte sequences or the literal applied patch, then verify an exact diff/inverse against the two recorded R1 SHA-256 values. A guessed reconstruction or the author's statement of preservation would not close that item.

This report records only the bounded source recheck. The coordinating reviewer owns route and notation integration. No manuscript or shared record was edited; this assigned report is the sole written artifact. No tests, build, rendering, subagent, admission, D3, PT-1 or GL closure was performed. The user-scope memory registry was searched briefly for repository context; its historical N-c-016 material supplied no evidence or conclusion for this recheck.

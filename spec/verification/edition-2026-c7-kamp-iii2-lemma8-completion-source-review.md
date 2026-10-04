# Independent source review: complete Kamp III.2 Lemma 8

Reviewer: /root/kamp8_completion_source_review. Date: 8 September 2026.
Start: 08:22:37 UTC. Content assessment completed: 08:29 UTC.
Requirement: C7 / N-c-012. Role: fresh source-fidelity review.

## Retrieved Content

### Source 1: completion body, lines 333-350

Path: handbook/parts/p09/presentations/kamp-iii2-lemma8-completion.tex.

```tex
\begin{hblemma}{thm:p09-kamp-iii2-lemma8}{proved=annex:p9.kamp.iii2.lemma8}{Kamp's universal interior-disjunction lemma}
Let \(x,y,z\) be distinct variables and let
\[
 F\subseteq\operatorname{At}(z)\cup\operatorname{Bp}(x,z)
                                      \cup\operatorname{Bp}(z,y)
\]
be finite, including the empty family with the stated false disjunction.
Then
\[
                   \forall z\,(x<z<y\to\bigvee_{\psi\in F}\psi)
\]
has property \(I(x,y)\). The algorithm above returns a finite
disjunction of actual \(\operatorname{Ep}(x,y)\) formulas
equivalent to it under \(x<y\) over \(\mathsf{Com}\).
All original finite-family, variable and order hypotheses are retained.
The full proof includes both orientations and every one of the eleven
boundary cases, with strict decrease at every recursive call
\cite[ch.~III, lemma~8, pp.~83--92]{Kamp1968}.
```

### Source 2: completion annex, lines 169-183

Path: handbook/annex/p09/kamp-iii2-lemma8-completion.tex.

```tex
Use \(I_k\) at this \(r\) to choose one realization
\(\mathbf a\) with \(d=a_k>r\), and put \(c=a_{k-1}\).
Keep its prefix \((a_0,\ldots,a_{k-1})\).
The old gap \((c,d)\) satisfies \(B_k\), and \(c\leq r<d<b\).
We claim that the entire open interval \((c,b)\) satisfies \(B_k\).
For any \(s\) in that interval, if \(s<d\), its truth
comes from this selected old gap. If \(d\leq s<b\), use
\(I_k\) again at \(v=s\) to choose another realization
\(\mathbf a'\) with \(a'_k>s\). Its preceding point
satisfies \(a'_{k-1}\leq r<d\leq s\), so \(s\)
lies strictly inside its \(k\)-th gap. That gap supplies
\(B_k(s)\). This includes the old endpoint \(s=d\),
which was not tested by the selected gap itself. It proves the
claim without making any intermediate points of different
realizations coincide.
```

### Source 3: completion annex, lines 441-454

```tex
This is an actual family in
\(\operatorname{At}(t)\cup\operatorname{Bp}(r,t)\cup
\operatorname{Bp}(t,s)\), with its three variable names distinct.
No elementary label with hidden endpoint parameters is being
counted as At. The stated induction hypothesis supplies a finite
\(\operatorname{Ep}(r,s)\) representation for its universal
formula. Properly substitute the given one-variable elementary
formula \(\eta\) for the fresh letter \(Q\).
The interval-substitution theorem constructs the resulting
elementary disjuncts and proves their \(\mathsf{Com}\)
equivalence. Other local members and all fixed-side conditions
are unchanged because \(Q\) was fresh from them and from
\(\eta\). The output is exactly the local universal formula
with the added disjunct \(\eta\).
```

---

## Supplementary Notes

### Verdict and scope

PASS for the source fidelity and complete mathematical construction of the
frozen completion pair below. No corrective finding was identified in these
targets. This review assesses the full original Lemma 8 conclusion, including
all eight supporting proofs and every step of the final induction. It does
not reuse the earlier foundation's limited acceptance as proof of that
conclusion.

The final routes, notation additions and a bounded navigation update to the
foundation were not yet supplied at this content-assessment snapshot. They
are a separate pending integration scope, not part of this PASS. There was no
manuscript build, manuscript render, software test, admission or publication
readiness decision. No other current reviewer report was read. Only this
assigned review file was written.

### Frozen identities and complete reading

| Artifact | Actual reading | SHA256 |
| --- | --- | --- |
| Completion body | Every line 1-373 | 22D58367E4A6C31471D59825476ECA6BB18EACDC1D5DAA8210E1619565D1C9DD |
| Completion annex | Every line 1-728, all eight annex items | 544E30F8E028D5C19BF1505CF9C839EAF9512014A1C41EC08B364BB25438EC05 |
| Completion research intake | Complete file | AFDC2B16402ABDE0182032E7F836FE490A3747ED981924AFFC92D774E52631DF |
| Foundation body, kamp-iii2-lemma8.tex | Every line 1-493 | ECC3896B4F0C25C58914FFBB9D03A49447D89F5146FF8949EF2CF9B34AD6F61E |
| Foundation annex, kamp-iii2-lemma8.tex | Every line 1-762 | 8740AE1FCC283B7313511073AD8D05B167FD92C1E207C37A984D53D00870BF8F |
| Held Kamp thesis | Complete primary Lemma 8, printed pp. 83-92; physical pp. 92-101 | C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA |

The primary is J. A. W. Kamp, *Tense Logic and the Theory of Linear Order*,
UCLA dissertation, 1968. The held PDF is
tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf. Its institutional locator is
https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf.
The local PDF hash was independently recomputed. Every complete relevant
page was personally read from the retained page images, page-092.png through
page-101.png in the existing kamp-lemma8-source directory. This includes the
statement, normalization, every printed boundary and chi formula, the
alpha_1 construction, the beta_1 assertion, the complete repeated-cut passage,
and the opposite-orientation conclusion before Lemma 9. No fresh download or
new source rendering was needed. The primary page reading occurred during
08:22-08:29 UTC on 8 September 2026.

Both applicable skills were read completely: research/SKILL.md and
pdf/26.904.11930/skills/pdf/SKILL.md. This reviewer is the assigned background
researcher. The PDF skill was used for primary reading only. The complete
handbook/CONVENTIONS.md and spec/EDITION-2026-CONTRACT.md were read at hashes
4293F514072179A5AC95E64FA8D8F37E23FFE2693814A1980E5801BABA5B7242 and
C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3.

### Direct prerequisite reading

These are actual file readings in this fresh context. Partial ranges below
are deliberately distinguished from complete-file readings. The selected
ranges contain the definitions and proof steps used by the new construction.

| Prerequisite | Read extent |
| --- | --- |
| n-c-012.tex | Lines 16-40: actual Lin and Com definitions |
| kamp-iii1-normal-form.tex body | Lines 61-98, including literal At grammar and truth/falsehood |
| Lemma 1 body / annex | Body 30-171; annex 1-159: basic grammar, whole occurrence words, both binary realization directions, word construction and guarded closures |
| Lemma 2 body | Lines 1-94: exact stage-zero and positive-stage limiting definitions |
| Lemma 3 body / annex | Body 1-109 and 111-194; annex 1-142: proper substitution, finite E grammar, variable dependence and the complete first-order substitution identity |
| Lemma 4 body / annex | Body 1-269; complete annex 1-585: elementary histories, labelled semantics, both closures, I substitution and endpoint insertion, every fusion step |
| Lemma 5 body / annex | Body 1-84; annex 1-198: complete elementary midpoint construction and both directions, including the original shared-label substitution |
| Lemma 6 body / annex | Complete body 1-171 and complete annex 1-271: both splice cases and every joining-gap position |
| Lemma 7 body / annex | Body 1-119; annex 1-208, including the complete cut-factorization proof 6-181 and exact bounds |
| Lemma 8 foundation | Both files complete as recorded above; all seven proofs rechecked |

Live hashes of these prerequisite files agree with the identities in the
author's intake. In particular Lemma 4 annex is
2C1DA5AE40BC16DD4533C64714DEF9868F93D2202202D30E6FFE10AA6DEB451E;
Lemma 5 annex is 26381378ADECC27A479724DBFAEA4650ACAF4DF29D62B4DF999FD42F758C8963;
Lemma 6 annex is 9EA42EBBDFFE6A6A9071C581E2F10721CF2D2504B96EC1CE51FE15658469D171;
Lemma 7 annex is 3E71146A7142A8A2BA26983A6A23634D9E7D3B52AA8A5F4FD2C9CC8793BD817F.

### All eight proof assessments

| Result | Evidence and independent assessment |
| --- | --- |
| Elementary duality | Body 14-49; annex 6-79. The structural identity retains arbitrary unary interpretations. All five seed types reverse to actual elementary presentations; the substitution case transports both the outer construction and inserted labels. Reversed words retain every point/gap position. Com is preserved. |
| Unary accumulation | Body 51-87; annex 81-138. The actual one-interval closure supplies each neighborhood label. The no-future/no-past disjunct handles vacuous universal accumulation globally. With a neighboring point, the endpoint predicate, first/last gap neighborhood and exact suffix/prefix limit give both directions. The n=1 limit is distinct from positive-stage words. |
| Remote limits | Body 89-140; annex 140-246. The quantifier instance at a forces a full realization; I_n is true and I_0 false. Failure of I_(k-1) bounds that coordinate in every realization. The selected gap covers points before d; later cofinal witnesses cover every point at or after d, including d itself. The whole suffix is arbitrarily near b. The converse joins it above max(v,c). There are exactly n candidates, with k=1 and k=n handled. Index reversal k=n-j+1 gives all dual candidates. The explicit x<t guard is equivalent to the source beta_1 condition under x<y by its max(v,a) instance. |
| Interior approach | Body 142-173; annex 248-297. Every one of the 2n-1 point/gap cuts is retained. The finite set of true prefixes is nonempty when a future bound exists. If each suffix failed accumulation, the minimum of their finitely many failure bounds contradicts the original approach premise. This supplies an actual E suffix label and I prefix conjunction. Last-point vacuity and the dual first-point case are covered. |
| Segmented assembly | Body 175-192; annex 299-372. Fresh occurrence letters extend the actual basic factorization to E labels evaluated in the whole structure. Every edge is cut at every intervening named point, with point and gap cuts retaining their endpoint tests. All adjacent-edge conditions are fused, absent ones get a true one-interval word, and all named-point labels enter the explicit midpoint concatenations. The recovered positions are strictly ordered because every interval word has positive length. All original I equivalences remain over Com. |
| Localization | Body 194-240; annex 374-463. Left and right crossing families are cut independently at their actual boundaries; their finite subset products retain every fixed prefix/suffix conjunct. Selecting all true fixed-side cuts proves completeness, and each selected residual reconstructs its original disjunct in the converse. The local family is literally At/Bp plus a fresh Q. Each old member supplies at most one residual of its old length and none longer; removing the maximal member leaves at most c(F)-1 maximal outputs. Eta is properly substituted only after the smaller-family call. |
| Positive boundaries | Body 242-300; annex 465-564. Every complete truth-set descriptor implies its listed elementary support. Each of the three lower supports supplies a fixed-start realization strictly before every middle point; each upper support supplies one strictly after. Lemma 6 therefore applies in all nine combinations. Outer D tests and both type-2 boundary-point D tests remain. Empty and singleton branches are proved separately. Absence assertions are removed only with a proved converse for each resulting branch. |
| Full Lemma 8 | Body 302-351; annex 566-728. The base includes empty and all-At families. Every regional call removes the distinguished maximal member first; point conditions retain the original a/b endpoints. Expanding every package and boundary disjunct produces actual E labels and interval edges, closed by segmented assembly. All eleven cases are covered. The right orientation invokes the proved left construction from smaller hypotheses, not the full theorem at equal rank; reversed images cannot increase the maximal count. Every recursive call is strictly below the original family, and every branching operation is finite. Neither Lemma 9 nor a later completeness theorem is used. |

### Source fidelity and corrections

The original statement on printed p. 83 is retained: three distinct variables,
a finite subset of the literal At(z), Bp(x,z), Bp(z,y) union, and property
I(x,y). The added empty-family treatment supplies the false-disjunction case
without changing the nonempty proof. The occurrence length is the source's
2n+1, with At assigned length one. The source comparison is proved exactly
equivalent to the lexicographic maximum/count comparison in the foundation;
it is not replaced by a different complexity measure. The 2n-1 cut count,
2^(sum(2n_j-1)) product count, and at-most-one equal-length residual restriction
are retained. No density or absence-of-endpoints premise is introduced.

The original proof structure is preserved through explicit constructions:
normalization and the atomic base on pp. 83-84; all eleven boundary cases on
pp. 85-89; elementary accumulation and the remote beta_1 step on pp. 89-90;
the repeated Lemma 7 reduction and smaller-family bound on pp. 90-91; and
the opposite orientation on p. 92. The new labels and assembly theorem
provide the omitted derivations, with an actual Ep disjunction at the end.

The printed p. 84 substitution displays a tautology for the added disjunct.
The foundation's three-point, all-false-predicate counterexample directly
refutes that recovery step. Substituting F^K removes the disjunct and the
proved I-substitution closure transports the result. The completion uses
that correct operation for outer localization regions.

The printed chi_6 on p. 88 has the first-witness and unrestricted-past shape
evaluated in the foundation's six-point counterexample. Its later truth at 4
can start at 3 while the required fixed start 0 fails across point 2. Reading
the complete printed formula confirms the missing upper bracket. The
completion does not equate its Gamma_i or Y_i with every literal printed
gamma_i or chi_i. It retains the original fixed-endpoint problem and proves
its corrected positive supports. In particular Y_6 requires B_W^+(a,b),
which supplies the missing upper witnesses. The same explicit lower/upper
verification covers the other omitted cases rather than borrowing the
source's unproved assertion for cases 4-11.

The single-interval example in completion body 353-367 is correct: a strict
limit of C below 1 does not require C(1), and an adjacent pair fails the
remote condition at v=a. No source correction was accepted merely on the
authority of an author or another review.

### Integration follow-up

Pending at this snapshot: root's frozen routes, notation rows and the bounded
foundation navigation update. The completion's substantive PASS above remains
tied to the two unchanged target hashes. Any content change requires the
affected assessment to be repeated. Source acquisition, mathematical reading,
structural checks, build/visual evidence and formal admission are distinct
claims; this report supplies only its stated independent source/text scope.

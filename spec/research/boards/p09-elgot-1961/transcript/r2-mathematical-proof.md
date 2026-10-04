# Blind mathematical and proof-correctness review — Elgot 1961, Round 2

## Seat, boundary, and frozen identity

I reviewed the Round 2 N-c-014.b snapshot as the mathematical and proof-correctness seat. I relied only on my own Round 1 source pass where the Round 2 charter permits that reliance. I did not read the board ledger, chair transcript, another reviewer's Round 1 or Round 2 transcript or verdict, a Büchi board, or any other board transcript, and I did not contact another reviewer. I edited no frozen artifact. I ran no test, automated checker, repository script, TeX command, build, or handbook-PDF inspection. The evidence used here is direct manuscript reading, original-detail source-image inspection, independent mathematical derivation, provenance inspection, and SHA-256 identity computation.

Before substantive review I independently recomputed the eight Round 2 hashes. All match the charter exactly:

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `elgot-1961-trans-ams.pdf` | `DE2F9587F72075C94C7071A00002D1129AA8148C498F9A4D6F75968EB46ACD74` | match |
| `elgot-1959-umr1342.pdf` | `596A599A7DF12F122BB2D875255B050695EC84A5A22F3488844D5876F3211D74` | match |
| `elgot-1962-errata.pdf` | `B13E422FC03DDA61B93A1B782F40882AE90DBC8886945B26A42376A96ED34EC1` | match |
| `n-c-014.tex` | `33A2CD747DBDFA356F5505E88CBF798D426C5B5971003E0449805BCDF93F86FA` | match |
| `logic-in-computer-science.tex` | `1690DED84FC257B50BC5B44E094E382D8A79B176E7BB9C21D0845DAEC59629B8` | match |
| `handbook.bib` | `6F98B6EB38B2B935DACC0C7E8373E1B12A5BB70FCAAC172D11BAFCDACA8C502F` | match |
| `p09-elgot-1961-source-note.md` | `1A34AC4E992C00A0E917256CF5DB58A7C48A971FBF47F7F217B25D0DDAF18331` | match |
| `p09-source-presentations-lot2-3.md` | `34D4B1AC65B78EAD14AB60335C94C8FFEA2F00778B963956038485DFB50EC438` | match |

I re-inspected at original detail the five Round 2 source renders: journal `rendered/page-26.jpg` (printed p. 46), report `report-rendered/page-09.jpg` (numbered p. 4), report `report-rendered/page-46.jpg` (numbered p. 41), and both errata images (printed pp. 558–559). The report map remains numbered p. 1 on physical p. 6, hence numbered pp. 4 and 41 on physical pp. 9 and 46. I additionally re-inspected journal p. 45 because Lemma 8.5 is the immediate dependency governing relation sequences and their finite-prefix languages. The article, report, and errata identities and authority order are unchanged.

## Round 2 findings

No blocker, must-fix, should-fix, or terminology finding remains within this seat's mandate. The three repaired clauses are checked below rather than presumed sound.

## R2-C01 — checked-clean: literal syntax and the window bound

Manuscript lines 403–430 now agree with journal p. 46 as controlled by errata p. 558. Lines 410–416 state that \(M\) is quantifier-free, has only the displayed variables free, may contain numerals, contains neither equality nor order, uses the successor iterates \(x^{(h)}\) and \(0^{(h)}\), and sets

\[
n=1+\max\{h:x^{(h)}\text{ or }0^{(h)}\text{ occurs in }M\}.
\]

The reason this is the exact bound is mathematical, not merely terminological. Every allowed atomic membership whose individual term depends on \(x\) reads a characteristic column at one of the offsets \(0,\ldots,n-1\). Numeral occurrences impose only a finite initial condition, recorded by the prefix set. Expanded disjunctive normal form therefore divides the models into finitely many initial patterns and finitely many \(n\)-column relation patterns. Equality or order would require additional analysis, so their explicit exclusion matters; quantifier-freeness alone would not establish this window property. When the maximum offset is \(0\), the definition gives the required unary case \(n=1\).

The former undefined technical use of “local” is gone. “Bounded window” at lines 417–418 is an explanatory phrase whose eliminable content is supplied immediately by lines 410–416, not a new primitive. Formula, assignment, finite prefix, and relation language retain distinct standings. This satisfies invariant I20 and the supplied AGENTS terminology rule.

## R2-C02 — checked-clean: all arities, unary promotion, and exact projection

### Arity \(n\geq2\)

Manuscript lines 432–448 give the correct componentwise construction. For each component \(j\), let

\[
R'_j=\{((a_0,j),\ldots,(a_{n-1},j)):(a_0,\ldots,a_{n-1})\in R_j\},
\]

and tag every coordinate of every word in \(E_j\) similarly. Let \(R'=\bigcup_jR'_j\) and \(E'=\bigcup_jE'_j\). If an admitted tagged sequence has its window beginning at \(t\) in \(R'_{j_t}\), all \(n\) positions of that window have tag \(j_t\). The windows beginning at \(t\) and \(t+1\) overlap in \(n-1\geq1\) positions; an overlapping position cannot have two different tags, so \(j_t=j_{t+1}\). Induction makes the tag constant on the entire sequence. Its initial tagged word then lies in one \(E'_j\), and its untagged projection is in that \(S_j\). Conversely, every member of \(S_j\) has the constant-\(j\) lift. Thus the projection is exactly \(S_1\cup\cdots\cup S_k\), including the source's \(k=2\) counterexample and every \(k>1\) case. The \(k=1\) case degenerates correctly.

### Unary case \(n=1\)

Lines 450–456 correctly distinguish the erratum's displayed arity-at-least-two construction from the handbook-owned unary completion. Fix \(j\), let \(R_j\subseteq A\), and write

\[
\operatorname{Seq}_1(R_j)
=\{f\in A^{\mathbb N}:\forall t\;f(t)\in R_j\}.
\]

For the binary product relation \(B_j=R_j\times R_j\),

\[
\begin{aligned}
f\text{ is a }B_j\text{-sequence}
&\Longleftrightarrow
\forall t\;(f(t),f(t+1))\in R_j\times R_j\\
&\Longleftrightarrow
\forall t\;f(t)\in R_j\\
&\Longleftrightarrow
f\in\operatorname{Seq}_1(R_j).
\end{aligned}
\]

The forward implication reads \(f(t)\in R_j\) from the first coordinate of the pair at \(t\); the reverse implication is immediate. Because the infinite sequence itself is unchanged, retaining the one-letter condition \(f\restriction1\in E_j\) preserves \(S_j\) exactly. This remains true when \(R_j=\varnothing\), or when a letter in \(E_j\) is not in \(R_j\): both formulations then admit no sequence beginning with that letter.

Now tag the promoted binary relation:

\[
B'_j=\{((a,j),(b,j)):a,b\in R_j\}.
\]

Tag the one-letter prefix sets and take the unions \(B'=\bigcup_jB'_j\) and \(E'=\bigcup_jE'_j\). If \(g\restriction1\in E'_j\), the first tag is \(j\). Membership of \((g(t),g(t+1))\) in \(B'\) says that both endpoints have one common component tag. The edge at \(0\) therefore gives tag \(j\) at position \(1\), and induction along successive overlapping edges gives tag \(j\) at every position. Projection yields a member of \(S_j\). Conversely, the constant-\(j\) lift of every member of \(S_j\) satisfies \(B'\) and \(E'\). Hence

\[
\widehat p(S)=S_1\cup\cdots\cup S_k
\]

also in the unary case; the alternating-tag counterexample from Round 1 is no longer admitted.

The fact that the retained prefix has length one while the promoted relation is binary creates no mathematical gap. For a nonempty unary component its finite-prefix language after tagging is

\[
\{\Lambda\}\;\cup\;
\{(a,j):(a)\in E_j,\ a\in R_j\}\,(R_j\times\{j\})^*;
\]

if the displayed first-letter set is empty, that component contributes no infinite sequence and is omitted. This is regular and effective. For \(n\geq2\), journal p. 45, Lemma 8.5 gives the corresponding regular finite-prefix construction directly. Letterwise projection commutes with taking a finite prefix, so the projected finite-prefix language is regular. Lines 456–460 may therefore pass to Theorem 8.1 only after, and now genuinely after, both arity cases have been established. Theorem 8.6.3's repaired reduction is sound.

The source note lines 307–356 record the same componentwise construction, unary proof boundary, and projection conclusion. Its lines 345–351 explicitly identify the unary argument as handbook-supplied rather than wording of the erratum. Reader lines 450–456 make the same ownership distinction. The revision neither uses the journal's false single-relation sentence nor launders the added unary argument into the published correction.

## R2-C03 — checked-clean: the two report occurrences

Original-detail inspection of report numbered p. 4 shows \(\widehat p\) at both occurrences corresponding to the journal p. 23 symbols corrected by errata p. 558 (“Replace each” \(\widehat f\) by \(\widehat p\)). Manuscript lines 478–485 now say “at both places,” matching source-note lines 90–100. Report numbered p. 41 still reproduces the journal's false single-relation assertion, while journal p. 46 and errata pp. 558–559 preserve the body/error/correction order. The reader correctly treats report agreement as precursor evidence and gives correction authority to the published errata.

## Collateral and mandatory-point disposition

The revision is confined to the rejected clauses and their status records. The unchanged source PDFs, shared theorem, and bibliography retain their Round 1 identities. The revised compact record says review is pending and does not claim admission. The article-plus-errata authority, report-precursor status, research-copy rights boundary, non-Büchi boundary, and topic-only scope remain intact.

| Point | Round 2 disposition | Basis |
|---|---|---|
| M01 | checked-clean | All eight Round 2 hashes recomputed before substantive judgment and matched. |
| Round 2 source-page mandate | checked-clean | Journal p. 46, report pp. 4 and 41, and errata pp. 558–559 re-inspected at original detail; journal p. 45 also checked as an immediate dependency. |
| M04–M16 | checked-clean | My complete Round 1 derivations remain applicable on unchanged source PDFs and unchanged manuscript passages; the Round 2 edits introduce no collateral change to these arguments. |
| M17 | checked-clean | R2-C01 now states every allowed/forbidden syntactic clause, the arbitrary-set standing, successor iterates, and the corrected offset bound. |
| M18 | checked-clean | R2-C02 matches the erratum's finite union, tagged fields/prefixes, constant-tag proof, \(k>1\) case, and explicit handbook-owned unary completion. |
| M19 | checked-clean | Both arity cases, exact projection, regular finite prefixes, and the passage to Theorem 8.1 were independently derived. |
| M20 | checked-clean | The unchanged negative-boundary passage remains covered by my complete Round 1 source and proof pass; no Round 2 edit affects it. |
| M25 | checked-clean | No residual false compression, hidden hypothesis, tag-switching edge case, empty-case omission, misleading occurrence count, correction laundering, or completion inflation was found. |

The supplied AGENTS terminology rule was applied to every revised expression. The exact syntax removes the former undefined designation; the unary completion has a definition, metalinguistic proof-step standing, a stated nonredundant purpose (covering \(n=1\), which overlap for \(n\geq2\) does not cover), actual use in the projection proof, and explicit handbook ownership. No new unsupported technical name was introduced.

VERDICT: ACCEPT

# N-c-014.b — Elgot 1961 source note

**Outcome:** **COMPLETE CONTROLLING JOURNAL ARTICLE, COMPLETE PRIMARY PRECURSOR, AND PUBLISHED ERRATA ACQUIRED AND RECONSTRUCTED; INDEPENDENT SCHOLARLY REVIEW PENDING.** The exact official AMS article preserved by the Internet Archive supplies all 31 printed pages, pp. 21–51. The University of Michigan supplies Elgot's complete June 1959 technical report UMR1342, whose mathematical body has the same section and theorem architecture in a 50-page report layout. The two-page 1962 *Transactions* errata supplies the controlling correction to §8.6.2 as well as five smaller corrections. Every page of all three artifacts was rendered and visually inspected. The reader now contains the literal source automata, both directions of Theorem 5.3, the decision and synthesis chain, the erratum-corrected arbitrary-set reduction, and the final undecidability boundary.

**Retrieved:** 2026-08-23  
**Journal DOI:** <https://doi.org/10.1090/S0002-9947-1961-0139530-9>  
**Report item:** <https://deepblue.lib.umich.edu/items/6227fc3c-fc18-4e8b-b5fa-3c674def489f>  
**Report handle:** <https://hdl.handle.net/2027.42/4758>  
**Report identifier:** UMR1342  
**Errata DOI:** <https://doi.org/10.1090/S0002-9947-62-99982-8>

| Artifact | Local path | Bytes | SHA-256 |
|---|---|---:|---|
| Official AMS journal PDF, archived exact capture | `tmp/pdfs/p09-elgot-1961/elgot-1961-trans-ams.pdf` | 2,652,186 | DE2F9587F72075C94C7071A00002D1129AA8148C498F9A4D6F75968EB46ACD74 |
| Journal text reading aid | `tmp/pdfs/p09-elgot-1961/elgot-1961-trans-ams.txt` | 80,984 | 87B44F7DE47EDAA06292935A3D8B6A20423B2A0C224D3831778136CA7BD455F1 |
| Michigan UMR1342 PDF scan | `tmp/pdfs/p09-elgot-1961/elgot-1959-umr1342.pdf` | 3,603,118 | 596A599A7DF12F122BB2D875255B050695EC84A5A22F3488844D5876F3211D74 |
| Michigan repository OCR/SGML | `tmp/pdfs/p09-elgot-1961/elgot-1959-umr1342.txt` | 86,617 | 8A3B89CADC61AC950A315DDB82950DF3DE4CA40A68133872C48B000790BEBAF3 |
| Published errata PDF | `tmp/pdfs/p09-elgot-1961/elgot-1962-errata.pdf` | 181,179 | B13E422FC03DDA61B93A1B782F40882AE90DBC8886945B26A42376A96ED34EC1 |
| Errata text reading aid | `tmp/pdfs/p09-elgot-1961/elgot-1962-errata.txt` | 3,919 | 6F6C906ABA6533399DC6EBF13646376621355B5FC18D3C2207B94FF051F7A621 |

**Rights caution:** AMS and Deep Blue make the source files publicly readable through the routes recorded below, but no open-content licence was found in the artifacts. The local files are research copies. Public access is not treated as redistribution permission.

## Exact identities and authority order

### Controlling journal article

> Calvin C. Elgot, “Decision Problems of Finite Automata Design and Related Arithmetics,” *Transactions of the American Mathematical Society* 98, no. 1 (January 1961): 21–51. DOI 10.1090/S0002-9947-1961-0139530-9.

The article itself prints pp. 21–51, so the bibliography's inherited `21--52` range was corrected. The DOI, journal, volume, issue, year, and page range agree with the AMS artifact and current Crossref metadata.

### Complete technical-report precursor

> Calvin C. Elgot, *Decision Problems of Finite Automata Design and Related Arithmetics*, University of Michigan Technical Report UMR1342, June 1959.

The report has the same title, section numbering, theorem numbering, proof order, examples, and bibliography as the later article, but in a substantially more spacious technical-report layout with separate acknowledgments, contents, abstract, footnotes, and distribution leaves. It is primary precursor evidence. The journal controls the published wording and pagination.

### Published errata

> Calvin C. Elgot, “Errata to ‘Decision Problems of Finite Automata Design and Related Arithmetics,’” *Transactions of the American Mathematical Society* 103, no. 3 (June 1962): 558–559. DOI 10.1090/S0002-9947-62-99982-8.

The errata appears under “ERRATA TO VOLUME 98” on printed pp. 558–559. It corrects the 1961 article, not the report as such. Where the report independently has a corrected symbol or independently shares an error, that fact is version-comparison evidence only; the 1962 publication owns the correction.

## Access-route ledger

| Route | Result | Body delivered? |
|---|---|---:|
| Live AMS journal PDF route | The current direct content request returned HTTP 403 in this environment. | No. |
| [Internet Archive exact capture of the official AMS PDF](https://web.archive.org/web/20250709105150id_/https://www.ams.org/journals/tran/1961-098-01/S0002-9947-1961-0139530-9/S0002-9947-1961-0139530-9.pdf) | HTTP 200 exact archived AMS artifact; 31-page PDF saved unaltered. | **Yes.** |
| [Deep Blue item](https://deepblue.lib.umich.edu/items/6227fc3c-fc18-4e8b-b5fa-3c674def489f) and public backend | Item marked `inArchive: true`, `discoverable: true`, `withdrawn: false`; PDF bitstream UUID `ce190fb9-4e3c-4a9f-a164-85e8b822a1e2` and TXT bitstream UUID `4605ba03-b4a8-40e4-9b31-ab372909a8cd` returned ordinary anonymous content responses. | **Yes, complete report and repository OCR.** |
| [Internet Archive exact capture of the official errata PDF](https://web.archive.org/web/20250420134418id_/https://www.ams.org/journals/tran/1962-103-03/S0002-9947-62-99982-8/S0002-9947-62-99982-8.pdf) | HTTP 200 exact archived AMS artifact; both pages saved unaltered. | **Yes.** |
| Crossref DOI metadata | Confirmed article and errata identities. Crossref exposes only starting page 558 for the errata; the artifact itself and contemporary bibliography show pp. 558–559. | Metadata only. |

The archived AMS files are captures of the official publisher PDFs, not retypes or secondary scans. The report backend is the public repository's own content service, not a bypass of a restricted object.

## Complete visual page audit

### Journal article

`pdfinfo` reports 31 unencrypted pages. All 31 were rendered to `tmp/pdfs/p09-elgot-1961/rendered/page-01.jpg` through `page-31.jpg` and inspected at original detail.

| Printed pages | Content | Finding |
|---:|---|---|
| 21–24 | Introduction; Chapter I §§2–3 | Complete definitions of \(I\)-automaton and regularity characterizations. No missing or clipped display. |
| 25–37 | Chapter II §§4–5 | Truncation, \(L_1^1\), Theorem 5.3, both proof directions, decision/arithmetic consequences, and variants complete. |
| 37–43 | Chapter III §§6–7 | Regularity operations; finite and infinite \(A/B\)-automaton behavior complete. |
| 44–47 | §§8–9 | Solvability/synthesis theorems and the printed §8.6.2 defect complete. |
| 47–50 | Chapter IV §10 | Post-system encoding and undecidability results complete. |
| 50–51 | Conclusion of §10; bibliography | Complete endpoint and references. |

There is no missing, duplicated, substituted, or unreadable page. The text extraction is useful for search, but it corrupts quantifier signs, hats, tuples, and superscripts; every displayed formula used in the reconstruction was checked against the page render.

### Michigan report

`pdfinfo` reports 60 unencrypted A4 pages. All 60 were rendered to `tmp/pdfs/p09-elgot-1961/report-rendered/page-01.jpg` through `page-60.jpg` and inspected at original detail.

| Physical PDF pages | Printed material | Finding |
|---:|---|---|
| 1–2 | Cover and funding leaf | Title, author, University of Michigan series, June 1959, and sponsorship present. |
| 3–5 | Acknowledgments p. iii, contents p. v, abstract p. vi | Complete report front matter. |
| 6–55 | Numbered pp. 1–50 | Continuous mathematical body, bibliography, and footnotes. No missing or clipped page. |
| 56–59 | Distribution list | Four complete institutional distribution leaves. |
| 60 | University of Michigan barcode leaf | Physical endpoint. |

The report has no useful embedded text layer. Its repository OCR/SGML is an operative reading aid but is not formula evidence; the scan controls every symbol.

### Errata

The two-page PDF was rendered to `elgot-1962-errata-page-1.jpg` and `elgot-1962-errata-page-2.jpg`. Both were inspected. Elgot's corrections begin on printed p. 558 and continue through p. 559; the neighboring Darst conclusion and Stanley errata establish that both physical pages belong to the complete journal errata section.

## Version comparison

The report's numbered p. 1 corresponds to the opening of journal p. 21. Every major division has the same number and order: §2 automata, §3 regularity characterizations, §4 truncation, §5 arithmetic/regularity, §§6–8 synthesis, §9 remark, and §10 negative results. Theorem 5.3, Lemma 6.1, Theorems 7.1 and 7.3, Theorem 8.1, Corollary 8.2, §§8.6.1–8.6.4, and Theorem 10.2 have the same numbering and mathematical role.

The report is not declared word-for-word identical. Its body uses 50 numbered pages versus the journal's 31, and it preserves front matter and end matter omitted from the article. The comparison also exposes three exact symbol/defect facts:

1. Report p. 4 already prints the projection symbol \(\widehat p\) at the two places where the 1962 errata tells the journal reader to replace \(\widehat f\) by \(\widehat p\) on journal p. 23.
2. Report p. 6 shares the journal p. 24 reversed ordered pair \((a,b)\), which the errata changes to \((b,a)\) so the described word begins with \(b\).
3. Report p. 41 shares the article's false §8.6.2 claim that one local relation language suffices. The 1962 errata's finite-union and tagging construction is required for both mathematical readings.

Journal page locators are therefore safe for the reconstructed claims because the complete journal was read directly. The report corroborates development and version lineage; it is not used to invent journal content.

## Controlling mathematical reconstruction

### The source \(I\)-automaton

Let \(I\) be a finite nonempty set. An \(I\)-automaton is

\[
\mathfrak A=(S,f,d,D),
\qquad
f:I\times S\to S,
\qquad
d\in S,
\qquad
D\subseteq S,
\]

where \(S\) is a finite nonempty internal-state set. The input alphabet is \(I\), not \(S\). For \(u=i_0\cdots i_{n-1}\), define \(s_0=d\) and \(s_{k+1}=f(i_k,s_k)\). Then \(u\in T(\mathfrak A)\) exactly when \(s_n\in D\). The empty word is accepted exactly when \(d\in D\).

This corrects the prior reader stub, which assigned the wrong standing to \(S\). The source's “output” \(D\) is a selected subset of internal states for this acceptor; it is not the output map \(g:S\to B\) introduced later for an \(A/B\)-automaton.

### Regularity and the truncation operation

The source writes \(V_I\) for all finite \(I\)-words, including the null word \(\Lambda\). It defines \(I\)-regular sets from the empty language and singleton letters by union, concatenation, and star. Kleene's theorem (§3.1) gives effective equivalence with \(I\)-automata.

If \(b\in I\), right truncation by \(b\) deletes the maximal terminal block of \(b\)'s from a word. Lemmas 4.1–4.2 express truncation through regular operations and prove that it preserves regularity effectively. This is the precise operation needed after a finite-set coordinate is projected away: trailing all-zero columns cease to carry information and must be deleted.

### \(L_1^1\), admissible matrices, and \(T_r(A)\)

Define \(x^{(0)}=x\) and \(x^{(n+1)}=(x^{(n)})'\). The language \(L_1\) is generated from

- \(x_i^{(n)}\in F_j\),
- \(x=y\), and
- \(x<y\),

using propositional connectives, individual quantifiers, and monadic-set quantifiers. In \(L_1^1\), individual variables range over \(\mathbb N\) and set variables over finite subsets of \(\mathbb N\).

For \(F=(F_1,\ldots,F_r)\), let

\[
c_F(n)=
\bigl(\mathbf 1_{n\in F_1},\ldots,\mathbf 1_{n\in F_r}\bigr)
\in U_r=\{0,1\}^r.
\]

If every \(F_i\) is empty, encode \(F\) by \(\Lambda\). Otherwise let \(m=\max(F_1\cup\cdots\cup F_r)\) and encode it by \(c_F(0)\cdots c_F(m)\). With \(0_r\) the all-zero column and \(U_r^0=U_r\setminus\{0_r\}\), the admissible words are exactly

\[
U_r^*U_r^0\cup\{\Lambda\}.
\]

For \(A[F_1,\ldots,F_r]\) with no free individual variables, \(T_r(A)\) is the language of admissible encodings of satisfying assignments. This definition makes the map from assignments to words one-to-one and prevents arbitrary trailing zero columns.

### Theorem 5.3(a): formula to regular language

The theorem states that \(T_r(A)\) is regular for every \(L_1^1\)-formula \(A\), and that a denoting regular expression is effectively obtainable.

The proof dependencies are explicit:

1. Lemma 5.4 converts a formula to prenex form with every set quantifier left of every individual quantifier.
2. Lemma 5.5 converts the remaining individual part to Boolean combinations of principal formulas. A principal formula asserts that some position and finitely many successors have a specified membership pattern in the free sets.
3. The admissible universe is regular.
4. Boolean connectives become union, intersection, and complement relative to that universe.
5. Existential quantification of the final set variable deletes its Boolean row and then right-truncates the all-zero resulting column. Lemma 4.2 proves this preserves regularity effectively.
6. Each principal local pattern has an explicit regular expression. The proof separates whether its last named column is nonzero, zero after a nonzero column, or the all-zero case.

This is a structural proof over every formula constructor. It is stronger than a one-way appeal to a later automata/MSO theorem.

### Theorem 5.3(b): regular language to formula

Let \(\alpha\) be a regular language of admissible \(U_r\)-words. For \(\alpha\setminus\{\Lambda\}\), choose an automaton \(\mathfrak A=(S,f,d,D)\), and encode \(S\) as a subset of \(U_s^0\) for some \(s\). A complete letter \((x,y)\in U_r\times S\) records an input column and the resulting state.

Define the finite start and terminal sets

\[
B=\{(x,f(x,d)):x\in U_r\},
\qquad
E=U_r^0\times D,
\]

and define adjacency by

\[
((x_1,y_1),(x_2,y_2))\in R
\quad\Longleftrightarrow\quad
f(x_2,y_1)=y_2.
\]

The complete accepting words are exactly the \(R\)-sequences beginning in \(B\) and ending in \(E\). Elgot supplies \(L_1^1\)-formulas for beginning in a finite set, ending in a finite set, and satisfying a finite local adjacency relation. Conjoin them, existentially quantify the \(s\) state-set coordinates, and add the separate \(\Lambda\) case if required.

Consequently every regular admissible language has a formula

\[
\exists G_1\cdots\exists G_s\,B,
\]

where the matrix has no set quantifiers and uses only the individual terms \(x,x'\). This is the exact reverse direction; it is not inferred from the compound theorem name.

### Decision and arithmetic consequences

Corollary 5.8 decides truth of \(L_1^1\) sentences by computing the regular encoding language and deciding emptiness/nonemptiness. The source also describes the corresponding input-free automaton route.

Section 5.9 uses the bijection

\[
\tau(F)=\sum_{k\in F}2^k
\]

between finite subsets of \(\mathbb N\) and natural numbers. A finite carry set expresses addition at the bit level, yielding Presburger decidability and an effective formula translation. Sections 5.10–5.11 identify a strictly stronger decidable first-order arithmetic containing addition and a power-of-two predicate. Sections 5.12–5.16 repeat the regular-encoding argument for finite sets of integers and for quasi-finite—finite or cofinite—sets over natural numbers and integers.

These consequences depend on Theorem 5.3's exact finite-set encoding. They do not redefine the automaton or collapse every arithmetic extension to a regular theory.

## The design and synthesis development

### \(A/B\)-automata and finite behavior

For finite nonempty \(A,B\), an \(A/B\)-automaton is

\[
\mathfrak T=(S,f,d,g),
\qquad
f:A\times S\to S,
\qquad
d\in S,
\qquad
g:S\to B.
\]

For input \(a_0\cdots a_n\), put \(s_0=f(a_0,d)\), \(s_k=f(a_k,s_{k-1})\) for \(k>0\), and \(b_k=g(s_k)\). Its finite behavior \(J(\mathfrak T)\) contains the paired word \((a_0,b_0)\cdots(a_n,b_n)\), together with the empty paired word.

This object is a synchronous deterministic transducer. It differs from the earlier acceptor \((S,f,d,D)\): the accepting subset \(D\) has been replaced by a total output map \(g\).

### Lemma 6.1: maximal extendable behavior inside a specification

For \(\gamma\subseteq(A\times B)^*\), a paired word \((u,v)\in\gamma\) is \(A\)-extendable in \(\gamma\) when

\[
\forall a\in A\;\exists b\in B\; (ua,vb)\in\gamma.
\]

It is strongly \(A\)-extendable when every prefix belongs to \(\gamma\) and is \(A\)-extendable there. Lemma 6.1 states that every regular \(\gamma\) has a largest strongly \(A\)-extendable regular sublanguage \(\gamma_A\subseteq\gamma\), effectively constructible from an automaton for \(\gamma\).

The proof works on finite complete states and repeatedly removes any state for which some next input letter lacks every output/state continuation. The descending sequence stabilizes because the state space is finite. Its stable part recognizes \(\gamma_A\), and maximality follows because every strongly extendable sublanguage can use only states surviving every deletion stage.

### Theorem 7.1: exact finite-behavior characterization

A language \(\alpha\subseteq(A\times B)^*\) is \(J(\mathfrak T)\) for an \(A/B\)-automaton exactly when:

1. \(\alpha\) is regular;
2. \(\alpha\) is open, meaning closed under finite prefixes;
3. for each input word \(u\), at most one \(v\) satisfies \((u,v)\in\alpha\); and
4. for every input word \(u\), some \(v\) satisfies \((u,v)\in\alpha\).

Necessity follows from the unique causal run. For sufficiency, encode the finite output alphabet in Boolean coordinates, recognize the coordinate languages, take their product, and use conditions 3–4 to define the unique output map. The construction is effective.

### Theorem 7.3: infinite behavior

For \(\alpha\subseteq(A\times B)^{\mathbb N}\), let \(\alpha^L\) be the language of all finite prefixes of members of \(\alpha\). Then \(\alpha\) is the infinite behavior of some \(A/B\)-automaton exactly when:

1. \(\alpha^L\) is regular;
2. equal finite input prefixes force equal output prefixes; and
3. every infinite \(A\)-sequence has an output paired with it in \(\alpha\).

The proof applies Theorem 7.1 to \(\alpha^L\) and shows that the limit behavior is exactly \(\alpha\). This is a causal-transducer theorem, not an omega-language acceptance condition.

### Theorems 8.1–8.3

Theorem 8.1 states

\[
\exists\mathfrak T\;J(\mathfrak T)\subseteq\gamma
\quad\Longleftrightarrow\quad
\gamma_A\ne\varnothing.
\]

If \(\gamma_A\) is nonempty, fix an order on \(B\) and retain the lexicographically least output compatible with each input. Lemma 6.5 preserves regularity; strong extendability supplies prefix closure and totality; Theorem 7.1 constructs the transducer.

Corollary 8.2 decides whether all transducers whose behavior lies in \(\gamma\) have the same behavior. When \(\gamma_A\) is nonempty, construct the least selection for an order on \(B\) and for its reverse, then test whether their regular behaviors have empty symmetric difference.

Section 8.3 writes a formula for the recursive state/output relation of a given transducer. If \(\mathfrak T\)'s formula is \(\mathcal F_{\mathfrak T}[a,b]\) and a specification is \(\mathcal G[a,b]\), then behavior containment is the truth of the universal implication \(\mathcal F_{\mathfrak T}\to\mathcal G\). This connects design to the earlier truth algorithm without identifying machines with formulas.

## Section 8.6 and the controlling erratum

### Printed setup

In \(L_1^5\), individual variables still range over \(\mathbb N\), but set variables range over arbitrary subsets of \(\mathbb N\). Section 8.6 considers specifications

\[
\exists\mathbf s\,\forall x\,M(\mathbf a,\mathbf b,\mathbf s,x),
\]

where \(M\) is quantifier-free, contains only the displayed variables free, may contain numerals, and uses neither equality nor order. Its relevant individual terms are successor iterates \(x^{(h)}\) and \(0^{(h)}\). The intended route is to describe the unprojected models by bounded-window constraints, project away \(\mathbf s\), form the regular finite-prefix language, and apply Theorem 8.1.

### Exact errata list

The 1962 publication makes these corrections:

1. Journal p. 23, lines 10–11: replace each \(\widehat f\) by \(\widehat p\).
2. Journal p. 23, §3.6(b), line 2: begin “by a finite number ...” on a new line.
3. Journal p. 24, line 9, second display: replace \((a,b)\) by \((b,a)\).
4. Journal p. 46, §8.6.2, line 5: replace “let \(n\) be the maximum” by “let \(n\) be one more than the maximum.”
5. Journal p. 46, §8.6.2, line 7: replace “for some \(n\)-ary \(R\)” by “for some \(R\) which is \(n\)-ary.”
6. Replace the third sentence of §8.6.2 by the finite-union and tagged-projection construction below.

Items 1, 3, 4, and 6 change symbols or mathematical content; item 2 is layout; item 5 clarifies grammatical scope. Item 6 is the substantive repair.

### Corrected finite-union statement

Let \(n=1+\max h\), where the maximum ranges over occurrences of
\(x^{(h)}\) and \(0^{(h)}\) in \(M\). In Elgot's conjunction-quantifier
notation, the correct conclusion is

\[
T^\infty_{m+m'+r}(\bigwedge_x M)
=S_1\cup\cdots\cup S_k,
\]

where each \(S_j\) consists of infinite \(R_j\)-sequences \(f\) such that the prefix \(f\restriction n\) belongs to a finite set \(E_j\). The relations and prefix sets are effectively obtained from expanded disjunctive normal form. The erratum gives an explicit formula for which \(k=2\), proving that the article's printed assumption \(k=1\) is false.

To reduce the finite union to a projection of one relation language, first
suppose \(n\geq2\). For each \(j\) use the disjoint field

\[
\operatorname{field}(R_j)\times\{j\}
\]

and set, componentwise,

\[
R'_j
=
\left\{
((a_0,j),\ldots,(a_{n-1},j)):
(a_0,\ldots,a_{n-1})\in R_j
\right\}.
\]

Tag every coordinate of every word in \(E_j\) analogously, take
\(R=R'_1\cup\cdots\cup R'_k\) and
\(E=E'_1\cup\cdots\cup E'_k\), and project
\((a,j)\mapsto a\). Consecutive length-\(n\) windows overlap, so an admitted
infinite tagged sequence has one constant tag. Its projection therefore lies
in exactly one \(S_j\), and every member of every \(S_j\) has a tagged lift.

The erratum states its displayed tagged construction for relation arity at
least two. If \(n=1\), first replace each unary constraint
\(R_j\subseteq A\) by the binary relation \(R_j\times R_j\), retaining the
one-letter prefix condition \(E_j\). This defines the same infinite
\(R_j\)-sequences. The tagged binary construction can then be applied, and its
overlap forces the tag to remain constant. This unary-window completion is a
handbook-supplied edge-case argument, not wording attributed to the erratum.

After the two arity cases, the projection of the resulting relation language
is exactly \(S_1\cup\cdots\cup S_k\).

With that correction, existential projection of the \(\mathbf s\)-coordinates and the regular-prefix construction in §8.5 are sound. Theorem 8.6.3 then reduces existence and effective production of a transducer satisfying the restricted infinite specification to Theorem 8.1.

## Chapter IV: the negative boundary

The language \(L_2\) adds successor, addition, equality, propositional connectives, first-order quantification, and monadic predicate variables. In \(L_2^1\), individuals range over natural numbers and predicates over finite sets.

Lemma 10.1 converts every Post normal system \(P\) to a formula \(F(P)\) whose encoded finite sequences are exactly the proofs of \(P\). Theorem 10.2 uses a two-letter Post system generating a complete recursively enumerable set to show:

- the satisfiable \(L_2^1\)-formulas are recursively enumerable;
- they are not decidable; and
- their degree is maximal among recursively enumerable sets.

Section 10.3 transfers undecidability to unrestricted predicates; §10.4 treats integers with finite predicates; §10.5 treats ultimately periodic predicates. Corollary 10.6 states the operational distinction: given a fixed input-free automaton and a formula interpreted on its outputs, satisfaction is decidable, while the question whether *some* input-free automaton satisfies the formula is undecidable.

This final chapter prevents an overbroad statement of the positive method. The regular encodings and synthesis procedure apply under the exact finite-set or restricted local-specification hypotheses established earlier.

## Source qualifications and transcription cautions

1. \(I\) is the input alphabet and \(S\) is the internal-state set in §2. Reversing them changes the types and is not a harmless renaming.
2. The selected subset \(D\subseteq S\) belongs to the acceptor \((S,f,d,D)\). The later transducer has an output map \(g:S\to B\). These definitions must not be conflated.
3. “Open” in §§6–7 means closed under finite prefixes. The reader defines that source usage when it first appears.
4. Theorem 5.3 includes both directions. Calling it only a regularity-preservation theorem omits the automaton-to-formula construction.
5. Projection of a finite-set coordinate requires right truncation of newly exposed terminal zero columns. Plain coordinate deletion does not preserve the source's canonical admissible encoding.
6. Theorem 7.3 concerns deterministic causal transducer behavior on infinite sequences, not Büchi acceptance.
7. The article's printed §8.6.2 is false as written. The 1962 finite-union/tagging correction is mandatory.
8. The report and article share mathematical architecture but have different pagination and at least the exact symbol differences recorded above. The journal and errata control publication claims.
9. OCR is never formula authority. All quoted formulas and ordered pairs were checked visually.
10. The title says “design and related arithmetics” because the paper proves both positive synthesis and negative existence results. Reducing it to the finite-word definability theorem erases its main source framing.

## Reader-facing integration

`handbook/parts/p09/presentations/n-c-014.tex` now supplies:

- the complete article/report/errata authority boundary;
- the correctly typed \(I\)-automaton and exact empty-word convention;
- the syntax and semantics of \(L_1^1\);
- the canonical admissible-column encoding;
- both directions of Theorem 5.3 and every structural operation used in its proof;
- the \(L_1^1\) decision route and arithmetic consequences;
- the separate \(A/B\)-automaton definition;
- Lemma 6.1 and Theorems 7.1, 7.3, and 8.1–8.3;
- the published correction to §8.6.2 and the resulting valid synthesis reduction; and
- Theorem 10.2 and Corollary 10.6 as the exact negative boundary.

`handbook/bib/handbook.bib` now corrects the article's page range to 21–51 and records the report and errata separately. `spec/research/p09-source-presentations-lot2-3.md` removes journal acquisition from the open ledger and records the body-complete, review-pending status.

## Current disposition

The source acquisition, complete visual inspection, version comparison,
mathematical reconstruction, and reader integration are complete. In blind
Round 1, the source-fidelity and adversarial-publication seats accepted, while
the mathematical seat rejected on three must-fix findings: the reader had
compressed the exact §8.6 syntax into an undefined “local” condition, had
written the tagged correction only in binary notation without the unary-window
case, and had said that the report already used \(\widehat p\) at one rather
than both corresponding occurrences. The reader and this note now state the
exact syntax, componentwise \(n\)-ary construction, explicit \(n=1\)
promotion, correction-ownership boundary, and two-occurrence version fact.

All three blind Round 2 seats accepted one unchanged eight-object snapshot.
The exact hashes, reviewer evidence, finding disposition, source/version
boundary, and narrow admission are preserved in
[the independent review record](p09-elgot-1961-independent-review-record.md).
This closes N-c-014.b at 1961-article-plus-1962-errata strength, with UMR1342
kept as a separate complete precursor. It does not close another N-c-014
source, Part IX, or any publication gate.

No manuscript build, automated test, checker, repository script, TeX command, or handbook-PDF inspection was used in this source/reconstruction pass.

## Direct finite-union exposition on 2026-09-06

The active N-c-014 reader now states the finite-union reduction directly,
while this note retains the false single-relation statement, the 1962
erratum's ownership, and the report/article symbol comparison. The later
reader-facing version-comparison paragraph was removed; it added no step
to the mathematical proof.

The reader gives an explicit finite-union construction. Fix an initial
length-n column word b, evaluate numeral terms against b and moving terms
against a candidate length-n window, and let R_b be the finite relation of
windows satisfying the resulting propositional matrix. Taking E_b to be
`{b} intersect R_b` enforces the initial word and its first local test.
Every model belongs to its own b-component, and every admitted component
stream satisfies the original matrix at every position. The window length
is at least one even if the matrix contains no individual terms, by taking
the maximum over `{0}` together with the actual successor offsets.

The disjoint tagging proof for arity at least two and the unary-to-binary
promotion are unchanged mathematically. Both are presented as actual
construction steps, without narrating defective alternatives. Source
provenance remains the 1961 article and 1962 erratum; the explicit initial-
window derivation and unary boundary explanation are supplied details.

No software tests, builds, or renders were performed. Earlier independent
review records continue to describe their own frozen snapshots.

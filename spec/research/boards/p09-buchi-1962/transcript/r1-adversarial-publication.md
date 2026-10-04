# Round 1 — adversarial publication and terminology review

## Mandate, evidence, and boundary

This is an independent blind review of the charter's six frozen objects.  I
did not read `ledger.md`, `transcript/chair.md`, any other current or earlier
board transcript, or any other verdict.  I did not edit a frozen artifact.  I
also did not run a test, harness, checker, repository script, TeX command,
handbook build, or handbook-PDF inspection.

I directly read every line in each stated review scope: `n-c-013.tex`
375--760; `logic-in-computer-science.tex` 817--828; `handbook.bib`
2276--2288; the complete source record 1--541; and the compact record
556--569.  I also visually inspected at original detail the following rendered
source pages: front matter 04 and 05; contents 08; article file pages 12--22
(printed pp. 1--11); and boundary page 23.  The visual pass confirms the page
map used below: the title/author and (SC) opening occur on printed p. 1;
printed p. 11 ends in references [7]--[11]; and file p. 23 begins Julia
Robinson's different article on printed p. 12.  Thus the article body is
continuous and its endpoint is not inferred from text extraction.

### Snapshot identity (M01)

All six SHA-256 values were recomputed before the substantive review and match
the charter exactly.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-buchi-1962/logic-methodology-philosophy-science-pageplace-preview-includes-buchi-pp1-11.pdf` | `D37929230CD874D9B6E91CDDE50DD57EAF51D625BC7575878853E4018B64E089` | match |
| `handbook/parts/p09/presentations/n-c-013.tex` | `F674BDB103A3B07DEE5925A1D7F3880D92DA31C6442196FB075B2FA85F4ADD24` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `2778CAA3D0EB741A78B9D2EA44BD157E5FCCB4E2F3034ED539D52A9788287A1B` | match |
| `handbook/bib/handbook.bib` | `748B159ED5CE40855878D3E8492DA98D0A465B73C68830E5BE11165EFF2ACA6A` | match |
| `spec/research/p09-buchi-1962-source-acquisition.md` | `90C23E094604342726B02EC78FE1A4211D56233A063532E8EDA94537676C434B` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `EBC0E39AF016B22F1BA52D7DEEB620DE6B00F5B48AA1F3E0687BB10BBC316508` | match |

No finding is filed.  Consequently, no blocker or must-fix remains for this
seat's publication-and-terminology mandate.

## Adversarial findings

None.  In particular, a hostile expert reader cannot fairly characterize the
reader as attributing the modern five-component automaton tuple, ``run,'' or
``B\"uchi acceptance'' terminology to the 1962 article: the non-attribution is
express at manuscript lines 469--498 and 622--632, and is repeated in the
source and compact records.  The primary text visibly supports that boundary:
on printed pp. 2--3 it gives the formula classes and state-sequence/word
presentation; it does not print a modern tuple definition.

## Mandatory coverage disposition

Every mandatory point was checked.  `checked-clean` means that I found no
publication, terminology, provenance, scope, or source-strength defect in the
frozen presentation; it does not convert this seat's review into a build or a
human-acceptance claim.

| Point | Disposition | Adversarial publication result and page/line basis |
|---|---|---|
| M01 | checked-clean | The six independently recomputed identities above equal the charter values. |
| M02 | checked-clean | Original-detail visual inspection of the prescribed front matter, contents, source pp. 1--11, and next-article boundary confirms the map. Source record 39--48 and manuscript 377--389 report the same limited fact. |
| M03 | checked-clean | The visible title/copyright/contents/article pages support author, title, editors, proceedings, Stanford publisher/location, 1962, and pp. 1--11. Source pp. 1 and 11, front matter 04--05, and contents 08 agree with source record 13--37, bibliography 2276--2288, manuscript 377--389, and compact record 556--558. The 1966 and 1990 DOI separation, preview route, and no-licence inference boundary are all express. |
| M04 | checked-clean | Source p. 1 gives the two domains, (0), successor, connectives, and both quantifier sorts. Manuscript 391--400 and source record 78--96 state that (SC) is an interpreted formalism, rather than an automaton or language class. |
| M05 | checked-clean | Source p. 3 visibly identifies a predicate tuple with an infinite sequence of truth-value states. The indicator definition and the absence of a separate source run are stated at manuscript 402--419 and source record 98--111. |
| M06 | checked-clean | The literal base, recursive, and infinitely-often clauses are printed on source p. 2. Manuscript 421--467 preserves the formulas and explicitly distinguishes formula classes from denotations. |
| M07 | checked-clean | See the two-direction derivation below. The source's formula supplies a permitted initial *set*, not a silently substituted one-initial-state tuple; manuscript 469--498 marks that exact boundary. |
| M08 | checked-clean | Source p. 2 defines regular formulas with a bounded interval and source p. 3 expressly overloads \(\Sigma^0\) to sets of words. Manuscript 501--509 and source record 191--201 preserve rather than conceal the formula/denotation distinction. |
| M09 | checked-clean | Source p. 3 visibly gives two-sided congruence, finite rank, and multiperiodicity. Manuscript 511--523 gives the exact condition and says that it is a finite-word language class, not an ultimately periodic infinite word or set. |
| M10 | checked-clean | Source p. 3 prints Lemma 1 and its Ramsey coloring proof. Manuscript 525--543 retains the quantification \(p<q\) and correctly says that all consecutive-block concatenations, not merely adjacent blocks, share the cell. |
| M11 | checked-clean | Source pp. 3--4 distinguish Lemma 2's cited difficult direction, its direct converse, the endpoint output condition, Lemmas 3--5's reductions, and Lemma 6's Rabin--Scott referral. Manuscript 545--573 and source record 251--288 retain each ownership boundary. |
| M12 | checked-clean | Source pp. 5--6 print Lemmas 7--9, the two path predicates, the \(2m^2\) dichotomies, homogeneous-block argument, and complement construction. Manuscript 575--593 correctly derives only the \(2^{2m^2}\) rank bound and expressly rejects a modern determinization attribution. |
| M13 | checked-clean | Source p. 7 states the finite-union \(\mathcal C\mathcal D\mathcal D\cdots\) form. Manuscript 595--603 makes the needed infinite-word reading explicit: a produced \(\omega\)-word must have unbounded total repeated-block length, so zero-length factors may be discarded and the endlessly repeated blocks can be required nonempty without changing the denotation. The finite stem is not incorrectly required nonempty. |
| M14 | checked-clean | Source p. 7 states Lemma 11, Theorem 1, the \(\Sigma_1^\omega/\Sigma_2\) comparison, the free-individual-variable extension, and the finite-set remarks at the displayed strength. Manuscript 605--620 identifies the referred 1960 method and does not promote it to a printed proof. |
| M15 | checked-clean | See the two-direction derivation below. Manuscript 622--632 and compact record 564 label the equivalence handbook-owned; source pp. 1--10 never receives the modern tuple/theorem name. |
| M16 | checked-clean | Source p. 8 gives a recurrent \(L\)-state, a finite initial path, a return cycle, a converse periodic construction, and the \(2^k\) finite enumeration. Manuscript 634--652 states a nonempty cycle and no stronger complexity result. |
| M17 | checked-clean | Source pp. 8--9 carries the effectivity completion through the finite-rank bound and reduction of the finite classification to Lemma 12, then states Theorem 2. Manuscript 654--663 states decidability only; it adds neither an elementary, PSPACE, optimal, nor translation-state-complexity claim. |
| M18 | checked-clean | Source p. 9 lists all five comparisons/consequences. Manuscript 665--687 preserves \(SC_{\mathrm{fin}}\), \([\mathrm{Nn},+,\mathrm{Pw}]\), attributions, and the undefined-in-context printed \(\Sigma_2^0\) label without conflating it with \(\Sigma^0\). |
| M19 | checked-clean | Source p. 9 calls for a careful analysis and identifies a candidate schema; it does not print a completeness theorem. Manuscript 689--695 and compact record 566 retain exactly that non-promotion. |
| M20 | checked-clean | Source pp. 9--10 introduce \(SC_{\mathrm{per}}\), state Theorem 3, and provide a finite-semigroup outline. Manuscript 697--715 gives an eliminable ultimately-periodic-set definition, standing, and use, while identifying the proof as an outline. |
| M21 | checked-clean | Source p. 10 gives the binary-expansion route, both theories, and symbol glosses. Manuscript 717--728 retains the visible \(\mathrm{Nn}\) discrepancy between source pp. 1 and 10 instead of resolving it editorially. |
| M22 | checked-clean | Source p. 10 attributes the \(2x\) undecidability report to Robinson and the monadic-function assertion to Gödel. Manuscript 730--733 preserves attribution and the absence of an article proof. |
| M23 | checked-clean | Source p. 10 states and defines the three problems. Manuscript 735--744 preserves the definitions of \(SC^2\) and \(SC(\alpha)\) and explicitly keeps the supplied-implementation decision question separate from synthesis. |
| M24 | checked-clean | The reader (377--759), shared theorem (817--828), bibliography (2276--2288), complete source record (1--541), and compact record (556--569) agree on identity, page map, rights/version boundary, formula-to-automaton comparison ownership, proof limits, and topic-only review gate. |
| M25 | checked-clean | The terminology audit below finds every technical designation in scope either source-defined, explicitly and eliminably handbook-defined with standing/use/nonredundancy, or a pre-existing cross-referenced modern term. The rights boundary is express in manuscript 377--389 and bibliography 2285--2287; topic-only scope and no-test/no-build boundary are express at manuscript 746--759 and source record 532--541. |

## Independent checks of the two modern comparisons

### M07 — one \(\Sigma_1^\omega\) formula versus finite data

For the formula at manuscript 452--460, let \(\mathbf r\) have \(\ell\)
coordinates and use the definitions at 471--479.  If the formula holds of an
input \(\mathbf i\), take \(q_n\) to be the vector of truth values of
\(\mathbf r\) at \(n\).  The first conjunct yields \(q_0\in Q_0\); the universal
conjunct yields \(q_{n+1}\in\Delta(q_n,\mathbf i(n))\) for every \(n\); and the
infinitely-often conjunct yields infinitely many \(n\) with \(q_n\in F\).

Conversely, from any sequence with those three finite-data properties define
the (j)-th auxiliary predicate by

\[
 r_j=\{n\in\mathbb N:(q_n)_j=1\}.
\]

The definitions of \(Q_0\), \(\Delta\), and \(F\) respectively reconstruct the
initial, local, and recurrent formula conjuncts.  This is an exact
bidirectional equivalence.  It establishes an automaton with a permitted
initial set; it does not alter the comparison into the separately defined
single-initial-state presentation.  Nor does it attribute the finite tuple to
B\"uchi.

### M15 — all \(SC\)-definable truth-value-word languages

For the forward direction, source Theorem 1 (printed p. 7; manuscript
605--620) converts every \(SC\)-formula to an equivalent
\(\Sigma_1^\omega\)-formula.  The preceding calculation applies to that normal
form, so its truth-value-word language has the handbook comparison automaton.

For the reverse direction, choose enough predicate bits to inject the finite
state set of a modern automaton into \(\{0,1\}^\ell\).  Propositional matrices
can restrict each time to a used code, specify the initial code or permitted
initial codes, encode the transition relation, and test membership in the
designated recurrent codes.  The resulting formula has the exact
\(\Sigma_1^\omega\) shape.  An accepting state sequence supplies the existential
predicate assignment, and any satisfying assignment supplies an accepting
state sequence; excluded unused bit patterns prevent spurious witnesses.
This proves the stated extensional converse.  It is a handbook proof from
finite coding plus the printed formula form, not a statement placed in the
1962 article; manuscript 625--632 says exactly that.

## Hostile-reader premortem

| Proposed hostile objection | Disposition |
|---|---|
| The reader launders modern automata terminology into the 1962 source. | Rejected. Every relevant modern term is disclosed as a handbook comparison, while the source's \(SC\), sequence, and formula terminology remains visible (391--498, 622--632). |
| Formula classes are silently made identical with their denotations. | Rejected. The reader identifies the source-declared \(\Sigma^0\) and \(\Sigma_1^\omega\) overloads and otherwise calls the symbols formula classes (421--467, 501--509). |
| Multiperiodic finite-word languages are confused with ultimately periodic sets or infinite words. | Rejected. The standing and nonredundancy are made explicit at 511--523; the later \(SC_{\mathrm{per}}\) restriction is separately defined at 697--715. |
| The printed and referred proofs are inflated into new proofs. | Rejected. All citations, referrals, outlines, and handbook-owned derivations are partitioned at 545--573, 605--620, 689--715, and 746--755. |
| The bibliographic record conflates the 1962 original with 1966 or 1990 DOI-bearing versions, or claims a licence. | Rejected. The reader, bibliography, and both records separately identify the versions and declare the research-copy/no-licence limit (377--389; bibliography 2285--2287; source record 27--37). |
| The presentation promotes a proposed axiom schema, open problem, or decision theorem into a completion/synthesis claim. | Rejected. It says no completeness proof, keeps all three problems open, and distinguishes a supplied finite-state behavior from implementation existence (689--695, 735--744). |
| The reader makes an unsupported computation, complexity, case-study, or admission claim. | Rejected. It says that the source provides no modern complexity bound or worked circuit example (654--663), and confines its own result to N-c-013.a's scholarly review boundary (746--759). |
| A graduate reader cannot tell what a named object is or why it is present. | Rejected by the terminology audit below; the prose supplies exact definitions, standing, nonredundancy, and later use where a handbook-owned distinction is introduced. |

## Full AGENTS terminology audit

The rule applies to genuinely introduced technical names, rather than to an
ordinary descriptive phrase or to a source name reproduced as source evidence.
No newly coined hypothetical ontology is introduced.  The following audit
checks necessity, exact definition or source/axiomatic status, standing,
nonredundancy, and use.

| Name/designation | Necessity and exact definition/status | Standing, nonredundancy, and later use | Result |
|---|---|---|---|
| \(SC\) | Historical source name; its domains and vocabulary are explicitly stated at 391--400. | An interpreted formalism, not an automaton/language; retained to avoid falsely presenting S1S as source wording; used throughout. | clean |
| Truth-value word / state sequence | Indicator map and displayed sequence are exactly defined at 402--415. | A representation of a predicate assignment, not an auxiliary run; needed for both word bridges. | clean |
| \(\Sigma_n,\Pi_n,\Sigma_1^\omega,\Sigma^0\) | Source formula classes are displayed at 421--467 and source-declared overload is stated at 501--509. | Formula classes, with denotations only where disclosed; needed for normal form and finite-word bridges. | clean |
| \(\Gamma,Q,Q_0,\Delta,F\) | Five eliminable, formula-indexed finite-data definitions occur together at 469--481. | Finite alphabet, state set, initial-state set, relation, and recurrent set; nonredundant components used in the bidirectional comparison. Explicitly not \(SC\) primitives or source tuple terminology. | clean |
| ``Permitted-initial-set variant'' | A descriptive label immediately tied to the exact set (Q_0) and contrasted with the prior one-initial-state definition at 481--498. | Names a presentation difference, not a new formal object; necessary to prevent a false single-initial-state attribution. | clean |
| Congruence, rank, and multiperiodic | Exact finite-word definitions at 511--523 reproduce source p. 3. | A relation and finite-word-language property; nonredundant with ultimately periodic predicate assignments; used in Lemmas 6, 9, and 10. | clean |
| Sequential Lemma | Historical name with statement and printed-proof summary at 525--543. | Source lemma, not a new automaton construction; used in the complement argument. | clean |
| \(SC_{\mathrm{fin}},SC_{\mathrm{per}},SC^2,SC(\alpha)\) | Each is source-defined or is given an explicit handbook elimination of the source phrase at 676--679 and 697--744. | Restricted/source variant formalisms, not word-language classes; each is used immediately in the stated consequence or open problem. | clean |
| Modern nondeterministic B\"uchi automaton / recognizable language | Not newly coined here: manuscript 492--493 cross-references the pre-existing Definition `def:p08-buchi-automaton`. This reader supplies the exact local finite-data comparison rather than pretending the article supplies the term. | Modern comparison object, nonredundant with (SC) and the formula classes; used at 622--632 and in the shared theorem 817--828. | clean |
| ``Recurrent existential formula,'' ``finite stem--cycle search,'' and ``synthesis'' | Each is immediately resolved by its displayed formula or stated decision question (634--663 and 735--744), not installed as a new primitive or abstract theory. | Descriptive labels for a formula form, a finite argument, and the distinct existence problem; each prevents ambiguity in the theorem's scope. | clean |

The historical phrase ``sequential calculus'' is also safely handled: source p.
2 supplies it, and manuscript 417--419 says explicitly that it describes the
use of \(SC\), not another formal system.  It therefore does not introduce a
second name requiring a new formal object.

VERDICT: ACCEPT

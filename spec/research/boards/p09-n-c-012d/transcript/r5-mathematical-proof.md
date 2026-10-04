REVISE

# Round-five mathematical/proof-correctness transcript

## Reviewer identity, independence, and method

- Stable agent identifier: `/root/r5_mathematical_proof`.
- Runtime model/version: not exposed to this reviewer.
- Review date: 2026-08-23.
- Seat: fresh, isolated mathematical/proof-correctness review of the frozen
  round-five `N-c-012.d` snapshot.
- Independence: I read no `ledger.md`, no `transcript/chair.md`, and no round
  one, two, three, four, or five reviewer transcript. I did not contact another
  reviewer. I edited no manuscript, source record, bibliography, charter,
  ledger, chair record, or other transcript.
- Method: direct visual reading of the complete primary sources, mathematical
  reconstruction, and line-by-line prose inspection only. I ran no test, test
  harness, checker, repository script, TeX command, PDF build, handbook build,
  or rendered-handbook inspection. The only computation was the charter-
  permitted SHA-256 identification of the ten frozen objects.

The verdict is `REVISE` because the ETL terminal/constructor arity is rebound
to the unrelated total input length in both the reader and the source note.
That makes the displayed Theorem 5.4 rule ambiguous and, on its literal local
binding, ill-typed. This fails C5, C8, C9, I10, M35, M41, and M42. All other
criteria and mandatory checks were independently rechecked rather than inferred
from an earlier round.

## Frozen-object identity

I computed every hash twice, once before source/manuscript inspection and once
immediately before filing. Every observed value equalled the charter's frozen
round-five value:

| Frozen object | Observed SHA-256 | Disposition |
|---|---|---|
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf` | `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5` | MATCH |
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf` | `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283` | MATCH |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png` | `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114` | MATCH |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png` | `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1` | MATCH |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-04-acceptable-crop.png` | `C267D4B4DF785F9A7E82123B068662E45D7E2C87CB18C24D7B8EB0B875AF413B` | MATCH |
| `handbook/parts/p09/presentations/n-c-012.tex` | `C760B8B413937A9002F017704956EBFFB2AF7ED44AD8AD8FF0EC4366E526EC79` | MATCH |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` | MATCH |
| `handbook/bib/handbook.bib` | `F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B` | MATCH |
| `spec/research/p09-sistla-clarke-1985-source-note.md` | `79E0677D27769153BC5C078242CDD77916350B926C87B25F91F78A9C943F0F19` | MATCH |
| `spec/research/p09-source-presentations-lot2-3.md` | `9739EBEE2BBE5F24857B9C900F831B7F9783F5BAA00652E02E3F5DD755E08D22` | MATCH |

No identity mismatch contributes to the rejection.

## Complete visual source-reading record

I visually read every journal image in order, with the PDF identified above as
the controlling object:

| Journal image | Printed page | Material freshly checked |
|---|---:|---|
| `journal-page-01.png` | 733 | plural title, author order, affiliations, abstract, classifications, introduction, rights notice, volume/issue/date/pages and printed ISSN identifier |
| `journal-page-02.png` | 734 | introduction, fragment claims, Section 2 notation, grammar, and absence of a formal validity clause |
| `journal-page-03.png` | 735 | restricted fragment, inclusive `X/U/S` semantics, `length`, `SF`, total `R`-structure, existential path truth, and the unique maximal `final`/`init`/`range`/`size` definitions |
| `journal-page-04.png` | 736 | Lemmas 3.1--3.3, exact Lemma 3.2 hypotheses, acceptable subsequences, ambient-relative measures, preparatory strict inequality, definition of `mu`, and literal Lemma 3.3 strict bound |
| `journal-page-05.png` | 737 | Lemma 3.3 induction's non-strict uses, its finite/infinite cases, the inclusive-current issue in “after,” Theorem 3.4 and its proof-sketch status, and Theorem 3.5's statement |
| `journal-page-06.png` | 738 | Figure 1, 3-SAT reduction, prefix/recurrent certificate, length bound, SCC and entry-edge checks, empty labels, increasing-length processing, and all four label rules including “after” |
| `journal-page-07.png` | 739 | acceptance at `q_0`, satisfiability algorithm, Lemma 3.6, Theorem 3.7, and Theorem 4.1's exact three displayed bases |
| `journal-page-08.png` | 740 | stuttering Lemma 4.2 and Lemma 4.3's complete reduction, including both pure-`U` replacements |
| `journal-page-09.png` | 741 | Figure 2, one-diamond-per-cell encoding, persistent terminal configurations, complete-ID traversals, and the literal `2S(n)` next distance |
| `journal-page-10.png` | 742 | pure-`U` reduction end, source truth-set definition and `2^length(f)` count, exact Lemma 4.5 deletion, inclusive fulfilled-before definition, valuation periodicity, and Lemma 4.6 hypotheses |
| `journal-page-11.png` | 743 | both Lemma 4.6 conclusions and induction, Theorem 4.7's exact quantifiers, bounds, type equality, and every-periodic-position `U` discharge |
| `journal-page-12.png` | 744 | Theorem 4.7 proof and counts; Theorem 4.1 Boolean, `X`, `U`, forward `S`, initial-since, loop-entry, storage, and within-period discharge machinery |
| `journal-page-13.png` | 745 | Savitch conclusion; ETL grammar/constructor; finite/infinite index defect; `N_0 -> a_1a_2N_0` parity conflict; normalization; extended closure; labelled `Gamma`; Lemma 5.1 start |
| `journal-page-14.png` | 746 | Lemma 5.1 completion, finite-tree maximum depth, distinct negated-grammar fulfillment, Lemma 5.2's added hypothesis and inherited conclusions, and Theorem 5.3's bound start |
| `journal-page-15.png` | 747 | Theorem 5.3's full obligations and proof; Theorem 5.4 input encoding, positive continuation/terminal rule, singleton frontier initialization, and present-to-next update |
| `journal-page-16.png` | 748 | frontier emptiness, Theorem 5.4 completion, exact Table I rows, conclusion, unidentified conference-proof error/correction notice, and references start |
| `journal-page-17.png` | 749 | remaining references, the distinct 1982 conference entry, and receipt/revision/acceptance history |

I also visually read every conference image in order:

| Conference image | Printed page | Material freshly checked |
|---|---:|---|
| `conference-page-01.png` | 159 | title/authors, abstract, introduction, 1982 rights line, and early result claims |
| `conference-page-02.png` | 160 | syntax and inclusive clauses, explicit satisfiability and universal validity definitions, and the beginning of `R`-structures |
| `conference-page-03.png` | 161 | existential `R`-truth, Section 3 measures, conference Theorem 3.1 and Lemmas 3.2--3.3 |
| `conference-page-04.png` | 162 | conference extraction/model proof sketches, different constants/bounds, and Theorem 3.5 start |
| `conference-page-05.png` | 163 | Theorem 3.5 certificate and literal label procedure |
| `conference-page-06.png` | 164 | conference Theorem 4.1, reductions, halting-machine formulation, Figure 2, and the literal `S(n)` next distance |
| `conference-page-07.png` | 165 | conference truth-set machinery, recurring-type set, Lemma 4.5, and periodic Theorem 4.6 without the journal's every-position `U` obligation |
| `conference-page-08.png` | 166 | proof outline, uncorrected regular-operator argument, constructor/parity example, old closure estimate, and conclusion |
| `conference-page-09.png` | 167 | comparison, Figure 3 classification, and bibliography start |
| `conference-page-10.png` | 168 | bibliography completion |

The required enlarged derivatives were read at their disputed passages:

- `journal-page-04-acceptable-crop.png`: the preparatory union sentence visibly
  prints `<`, and `mu(f)` is defined immediately afterward.
- `journal-page-10-bound-crop.png`: the realized source-truth-set exponent is
  visibly `2^length(f)`, not `2^(2 length(f))`.
- frozen enlarged `journal-page-13.png`: the source visibly says “finite or
  infinite,” writes an unrestricted nonnegative index, prints
  `N_0 -> a_1 a_2 N_0`, and states the conflicting even-position example.

Thus no unread authority page or uncertain visual character is being hidden
behind the verdict.

## Must-fix mathematical/type finding

### F1. Theorem 5.4 rebinds constructor arity to total input length

The source has two independent natural numbers at Theorem 5.4:

1. the grammar terminal count, which is also the arity of
   `N_j(f_1,...,f_q)` after the source's local change from `n` to `q`; and
2. the total encoded input length `n`, used only to derive
   `card(SF(f)) <= 2n` and the exponential counter bounds.

They are not equal in general. A grammar with two terminals has a binary
constructor even when the encoded formula-plus-grammar input has length 100.

The reader first makes a legitimate alpha-renaming and explicitly binds `n`
as both terminal count and constructor arity at
`handbook/parts/p09/presentations/n-c-012.tex:2451-2464`. It then says “If the
total encoded input length is `n`” at lines 2545--2548 and immediately displays
`N_j(f_1,...,f_n)` at lines 2553--2561, with the same tuple repeated in the
frontier update at lines 2563--2574. Literal local scope therefore makes the
constructor have input-length-many arguments; an alternative charitable
reading leaves `n` ambiguously double-bound. Either reading violates exact
typing.

The same collision occurs in
`spec/research/p09-sistla-clarke-1985-source-note.md`: grammar terminal/argument
arity is bound to `n` at lines 730--744, but total input length is rebound to
`n` at lines 826--830 before `N_j(f_1,...,f_n)` is used at lines 831--851.
The compact presentation is locally better: lines 309--323 bind `n` only as
arity and define the eliminable tuple abbreviation `bar f`. That local success
does not repair the reader/source-note collision, and its delivery-status claim
at lines 368--371 that the unbound ETL arity was repaired “consistently” is
therefore false on the common frozen snapshot.

This is not cosmetic. The positive rule and continuation-frontier rule are
formula schemas whose tuple must have the grammar's terminal arity. The input
length appears only in the size estimate. The minimum repair is to retain one
letter (for example `q` or `r`) for terminal/constructor arity everywhere and
use a different letter (for example `N_in`) for encoded input length, or to
keep the global `n` arity and rename only the input-length variable. The
reader, source note, and compact presentation must then be refrozen together.

No second must-fix mathematical defect was found. In particular, the
inclusive-current `F` repair and the directed-cycle repair are mathematically
necessary, separately owned, and correctly distinguished.

## Criterion-by-criterion disposition

| Criterion | Disposition | Evidence and reasoning |
|---|---|---|
| C1 | PASS | Journal pp. 733, 749 and conference pp. 159--168 agree with author order, plural title, venue/date/pages, receipt history, separate version identities, and rights limits. Reader 1853--1881, bibliography 2245--2274, and source note 35--117 preserve DOI/ISSN/provenance without a republication overclaim. |
| C2 | PASS | Journal pp. 734--735 supplies the grammar, restricted fragment, inclusive `U/S/F`, structures, total `R`, and existential path truth. Reader 1883--1990 preserves those quantifiers and labels the journal-relative universal validity clause as reconstruction; conference p. 160 is separately identified. |
| C3 | PASS | Reader 1992--2225 accurately gives ambient-relative measures, Lemmas 3.1--3.3 and 3.6, both strict/non-strict defects, Theorems 3.4--3.7, diamond hardness, pre-Theorem-3.5 `SF`, bound start state, every label rule with inclusive current witness, the loopless-singleton counterexample, and the separately owned directed-cycle correction. The counterexamples calculate correctly. |
| C4 | PASS | Reader 2227--2446 preserves Lemma 4.3's exact formulas and both pure-`U` cases, p. 741's `2S(n)`, the p. 742 count, fulfilled-before endpoint, exact Lemmas 4.5--4.6, every Theorem 4.7 quantifier/bound, and the direction-sensitive search recurrences plus Savitch. |
| C5 | REVISE | The finite/infinite typing conflict, parity conflict, closure, `Gamma`, Lemmas 5.1--5.2, Theorem 5.3, and frontier logic are otherwise exact, but F1 makes Theorem 5.4's constructor tuple ambiguous/ill-typed. |
| C6 | PASS | Reader 2591--2621 reproduces every Table I row and distinguishes Table I's `L(U,X)` row from Theorem 4.1. Shared theorem 693--708 uses the valid containment hardness/upper-bound sandwich. Shared method/theorem 761--809 obtains universal checking by complementing existential truth and returns a finite product path plus nonempty cyclic product witness. |
| C7 | PASS | Complete conference/journal comparison was visually rechecked. Reader 1873--1881, 2290--2294, 2584--2589 and source note 933--972 neither import numbering nor identify a unique error/repair. |
| C8 | REVISE | Bibliography, page map, proof-status table, rights record, and locators are otherwise accurate, but the reader/source note type collision conflicts with the locally coherent compact presentation and with the compact presentation's claim of a consistent repair. |
| C9 | REVISE | Prose is independently worded and the five-part terminology disclosures are otherwise present. F1 violates exact type/binder discipline, and the unsupported “repaired consistently” status claim cannot stand. |

## Invariant disposition

| Invariant | Disposition |
|---|---|
| I1 | PASS: this review used only source reading, mathematical reasoning, prose inspection, and permitted hashes. |
| I2 | PASS: all ten hashes matched twice. |
| I3 | PASS: all 17 journal and all 10 conference pages were freshly read; no OCR or prior note controlled a source claim. |
| I4 | PASS: the enlarged p. 742 exponent and p. 745 conflicts were read directly. |
| I5 | PASS: the journal controls; version numbers, bounds, and correction language remain separate. |
| I6 | PASS: language classes, truth sets, inclusive semantics, existential truth, satisfiability, and reconstructed validity remain distinct. |
| I7 | PASS: `size`, unique `final`, ambient-relative measures, and both printed strict-sign conflicts are correctly handled. |
| I8 | PASS: journal `2S(n)`, closure size, realized-type count, and inclusive fulfillment are distinct and correct. |
| I9 | PASS: every-position Theorem 4.7 obligations, exact bounds, `Ff`, initial since, storage, and Savitch are visible at source strength. |
| I10 | REVISE: ETL's source machinery is otherwise exact, but its terminal/argument arity ceases to be consistently bound in Theorem 5.4 because of F1. |
| I11 | PASS: proof sketches, asserted inductions, and brief replacements remain qualified; no Büchi proof is attributed to Sistla--Clarke. |
| I12 | PASS as to introduced terminology: each reviewed name/abbreviation has necessity, definition, standing, nonredundancy, and use. This does not cure the independent variable-binding failure F1. |
| I13 | PASS: prohibited records and reviewer communications were avoided. |
| I14 | PASS: a single must-fix item causes `REVISE`; no vote or balancing was used. |
| I15 | PASS: the prose and this transcript preserve the limited topic-level gate. |

## Mandatory-check disposition M01--M42

| Check | Disposition | Direct locator/reason |
|---|---|---|
| M01 | PASS | Enlarged journal p. 742 visibly prints `2^length(f)`; reader 2303--2315 and source note 600--614 preserve it. |
| M02 | PASS | Journal pp. 734--735 contain no formal validity clause; conference p. 160 does. Reader 1977--1990 explicitly marks the journal-relative clause reconstructed. |
| M03 | PASS | Journal p. 742 has `j >= i` and `i <= l <= j`; reader 2316--2323 reproduces both inclusive endpoints. |
| M04 | PASS | Enlarged p. 736 and full pp. 736--737 show both literal `<` signs and following `<=` uses; reader 2067--2083 and 2111--2131 supplies the null counterexamples and Theorem 3.4's non-strict result. |
| M05 | PASS | Journal p. 741 visibly prints `2S(n)`; conference p. 164 prints `S(n)`; reader 2290--2294 uses the correct locators. |
| M06 | PASS | Journal pp. 743 and 746--747 were checked word for word. Reader 2380--2400 and 2535--2544 preserves every bound, positive period, `k >=` quantifier, type equality, and every-position fulfillment family. |
| M07 | PASS | Journal p. 745's “finite or infinite” plus unrestricted index is disclosed; reader 2468--2479 labels the finite represented-index restriction handbook-supplied. |
| M08 | PASS | Journal p. 745 prints `N_0 -> a_1 a_2 N_0` and “even states”; reader 2484--2493 correctly derives second-argument truth at zero-based odd offsets and chooses no repair. |
| M09 | PASS | Journal p. 745 and reader 2501--2512 give every `Gamma` continuation edge, depth shift, argument test, and terminal/continuation separation. |
| M10 | PASS | Journal pp. 746--747 and reader 2514--2517, 2563--2583 distinguish maximum tree depth from until fulfillment and require the continuation set to become empty within the period. |
| M11 | PASS | Journal p. 748 identifies only an erroneous theorem used in the conference proof; reader 1873--1881 and 2584--2589 claims no precise bad inference or unique new repairing lemma. |
| M12 | PASS | Reader 2440--2446 and source-note proof table 906--927 preserve all proof-status qualifications; reader 2583--2589 and source note 862--865 exclude a Sistla--Clarke Büchi construction. |
| M13 | PASS | Reader 2613--2620 and shared theorem 693--708 use `L(U) subset L(U,X) subset L(U,S,X)` for exactly the PSPACE lower/upper sandwich. |
| M14 | PASS | Journal p. 735's source problem remains existential. Reader 1967--1976 and shared theorem 796--808 use negation and deterministic-PSPACE complement closure for universal checking. |
| M15 | PASS | Reader 2036--2066, 2303--2323, 2464--2482, and 2501--2512 locally supplies all five terminology components for acceptable subsequence, the ambient subscript, source truth set, fulfilled-before obligation, ETL constructor, and `Gamma`. |
| M16 | PASS | Source-note page map 119--145 correctly places `init/final/range/size` on p. 735, conclusion on p. 748, and references on pp. 748--749; the images confirm it. |
| M17 | PASS | Conference p. 160's formal validity definition and journal pp. 734--735's absence are separately recorded; the p. 748 notice remains unidentified. |
| M18 | PASS | Journal pp. 736--739 and reader 2015--2034, 2088--2109, 2217--2223 preserve Lemmas 3.2, 3.3, and 3.6, including zero-prefix, acceptability, every-intermediate-supersequence, surviving-position, current-state containment, and strict-sign qualification. |
| M19 | PASS | Journal p. 741 and reader 2281--2295 use one diamond per tape cell, one BI--EI traversal per ID, repeated traversals per computation, and persistent terminal configurations; conference p. 164's halting formulation remains separate. |
| M20 | PASS | Journal p. 742 and reader 2366--2378 define periodicity for `i in N`, `p > 0`, and every `k >= i` by complete valuation equality, separately from source types and both obligations. |
| M21 | PASS | Shared method 761--787 and theorem 796--803 explicitly return a finite product path and a nonempty product cycle whose repetition is the counterexample, without inventing an undefined periodicity name. |
| M22 | PASS | The scoped reader, source note, and compact presentation call `Gamma(S,j,N_i)` only the labelled tree or `Gamma`; no proof-tree, derivation-tree, or continuation-tree synonym is introduced. |
| M23 | PASS | Rechecking the current snapshot against M01--M15 found each earlier required artifact present without weakening; no prior transcript was consulted. |
| M24 | PASS | Journal p. 735 and reader 1993--2013 define the unique maximal suffix, exact concatenation, range, and size before use. |
| M25 | PASS | Journal p. 736 and reader 2042--2066 define all acceptable-subsequence measures relative to `S` and give the subscript's eliminable metalinguistic standing, necessity, distinction, and use. |
| M26 | PASS | Enlarged p. 736 confirms the preparatory strict inequality and following `mu` definition; reader 2067--2088 gives null/null failure and non-strict subadditivity before Lemma 3.3's use. |
| M27 | PASS | Journal pp. 738--739 and reader 2144--2195 give prefix bound, `C`, SCC, entry edge, empty labels, increasing-length processing, all rules, and start-label acceptance. |
| M28 | PASS | Bibliography 2245--2274 has distinct accurate 1982 and 1985 records; direct conference and journal claims use their respective keys. |
| M29 | PASS | The current snapshot contains every M16--M23 repair and the newly disclosed preparatory strict-sign conflict without weakening earlier requirements. |
| M30 | PASS | Reader 2290--2294 pinpoints journal `2S(n)` to p. 741, conference `S(n)` to p. 164, and the broader journal reduction to pp. 741--742. |
| M31 | PASS | Reader 2156--2195 gives empty initialization, increasing-length order, exact atom/negation/conjunction/`F` iff rules, inclusive current prefix witness, and start acceptance; reader 2197--2214 preserves the literal SCC/entry checks, concrete false acceptance, and handbook-only cycle condition. |
| M32 | PASS | Reader 2233--2279 gives `P_1/P_2`, every `g_i^x`, `f_x`, `h_i`, `f'`, `f''`, `L(F,X)` preservation, both self-loop-sensitive pure-`U` forms, and Lemma 4.2's exact role. |
| M33 | PASS | Reader 2324--2364 deletes exactly `s_i,...,s_(j-1)`, retains `s_j`, preserves common-token types, and states every Lemma 4.6 premise plus both conclusions. |
| M34 | PASS | Reader 2402--2438 prints the exact Boolean, `X`, `U`, direction-sensitive `S`, initial-since, saved-entry/closure, within-period discharge, storage, and Savitch steps. |
| M35 | REVISE | Lemma 5.2's extra hypothesis and inherited conclusions, singleton initialization, update, and emptiness are present at reader 2517--2532 and 2563--2583. The positive iff alternatives are structurally source-exact, but their repeated tuple `N_j(f_1,...,f_n)` inherits F1's arity/input-length collision, so this exact-rule check is not clean. |
| M36 | PASS | Reader 2156--2195, 2233--2262, 2402--2407, and 2563--2583 supplies exact eliminable/metalinguistic standing, distinctions, and actual uses for `label`, all Lemma 4.3 formula names, `A/B`, and `varphi`. |
| M37 | PASS | Every enumerated round-three repair is present on the current hashes; no source wording was silently upgraded in those repairs. |
| M38 | PASS | Reader 1905--1920 defines `SF(f)` before Section 3/Theorem 3.5, including ordinary subformulas, single-negation mates, double-negation elimination, the `<= 2 length(f)` bound, and separation from the later `2^length(f)` count. Source note 216--231 and compact presentation 200--213 agree. |
| M39 | PASS | Reader 2143--2148 binds `q_0 := delta` before prefix/acceptance; source note 428--436 and compact presentation 249--260 do likewise. |
| M40 | PASS | Reader 2169--2189 preserves the paper's word “after,” renders the witness at-or-after, derives non-strictness from inclusive pp. 734--735 and p. 737, gives the strict-reading `A and FA` counterexample, labels the rendering a source-context reconstruction, and keeps it separate from the cycle correction. Source note 456--466 and compact presentation 263--273 agree. |
| M41 | REVISE | F1: reader 2457--2464 versus 2545--2574 and source note 730--744 versus 826--851 bind the same `n` to independent arity and input-length quantities. The compact tuple abbreviation at lines 313--323 meets the five-part terminology rule locally, but cross-file consistency and Theorem 5.4 typing fail. |
| M42 | REVISE | The supported round-four unbound-arity finding is not consistently repaired: a binder was added, but then rebound to input length in the same ETL discussion. Compact presentation 368--371 therefore overstates repair completion. |

## Mathematical stress-test summary

- The null subsequence refutes both printed strict bounds exactly as reported;
  the following inductions and Theorem 3.4 require non-strict inequalities.
- The prefix-current counterexample `A and FA` refutes a strict reading of
  “after” while leaving the recurrent-cycle issue untouched.
- The `GP` loopless-singleton graph passes the source's literal reflexive-SCC
  check and is falsely accepted; adding a positive directed cycle repairs that
  issue once, at the recurrent set.
- The source-truth-set count is `2^length(f)` because negation mates add no
  independent Boolean choice; it is not the power set of an unconstrained
  `2 length(f)`-element closure.
- The Lemma 4.3 pure-`U` cases correctly separate a node without a self-loop
  from a node whose infinite self-stuttering must remain allowed.
- Lemma 4.6's transfer and periodicity conclusions require both equal endpoint
  types and discharge; complete valuation periodicity alone proves neither.
- Theorem 4.7's `Ff` step is necessary because source satisfiability permits a
  point away from the word beginning when past `S` occurs.
- The `U` and `S` recurrences are directionally correct: `U` is tested from
  present to next, while `S` is tested from next back to present, with the
  separate initial-since equation.
- Lemma 5.1 correctly separates finite terminal witnesses from infinite
  continuation branches; frontier emptiness supplies finite-tree termination,
  not an until witness.
- The only failed stress test in the handbook reconstruction itself is the
  unrelated reuse of `n` described in F1.

## Final disposition

The frozen scholarly object is mathematically and source-faithfully repaired
through the Section 3 and Section 4 issues, and the ETL proof architecture is
substantively present. It cannot be accepted while its Theorem 5.4 constructor
schema binds the argument count to two independent quantities. Repair F1 in
the reader and source note, make the compact delivery claim true of the common
snapshot, refreeze all affected objects, and submit the new snapshot to fresh
independent review.

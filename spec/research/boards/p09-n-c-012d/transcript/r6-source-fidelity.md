ACCEPT

# Round-six source-fidelity transcript: `N-c-012.d`

- Stable agent identifier: `/root/r6_source_fidelity`.
- Seat: source fidelity, frozen round six.
- Runtime model/version: not exposed by the runtime.
- Verdict basis: exhaustive checked-clean coverage of `C1`--`C9`, `I1`--`I15`, and `M01`--`M44` on the exact common round-six snapshot.
- Findings: none. I found no blocker, must-fix item, unresolved source discrepancy, unread page, hash mismatch, unsupported attribution, version conflation, locator failure, rights overclaim, or terminology-rule failure.

## Independence, scope, and method

I read `spec/research/boards/p09-n-c-012d/charter.md` completely before reviewing the scholarly object. I did not read `ledger.md`, `transcript/chair.md`, any round-one through round-five reviewer transcript, or either other round-six reviewer transcript. I did not contact another reviewer or report a verdict to another seat. I edited only this assigned transcript.

This was a book-writing review. I used fresh visual primary-source reading, direct mathematical comparison, and ordinary prose/source inspection only. I ran no test, test harness, automated checker, repository script, TeX command, PDF build, handbook-PDF inspection, or build. The only computation was the expressly permitted SHA-256 identification of the ten frozen objects, performed once before reading and once immediately before filing; both passes returned the same chartered values.

The artifacts read in full for this seat were:

- the complete reader subsection `handbook/parts/p09/presentations/n-c-012.tex:1851--2631`;
- the necessary shared Part IX context in `handbook/parts/p09/logic-in-computer-science.tex:602--708`, `:720--809`, and the routed complexity-table row at `:2219--2222`;
- both complete bibliography records in `handbook/bib/handbook.bib:2245--2274`;
- the complete source note `spec/research/p09-sistla-clarke-1985-source-note.md:1--1060`;
- the complete compact presentation `spec/research/p09-source-presentations-lot2-3.md:185--388`.

## Frozen round-six identity

All ten observed SHA-256 values exactly matched the round-six charter, on both permitted hash passes:

| Frozen object | Observed and chartered SHA-256 |
|---|---|
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf` | `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5` |
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf` | `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png` | `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png` | `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-04-acceptable-crop.png` | `C267D4B4DF785F9A7E82123B068662E45D7E2C87CB18C24D7B8EB0B875AF413B` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `C25353424D7DF38678F8AAC7BB421DD1DCCF2E1289643E114425D0F2BEA31DEA` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` |
| `handbook/bib/handbook.bib` | `F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B` |
| `spec/research/p09-sistla-clarke-1985-source-note.md` | `9390C6A525C88E247BC5C892B4522EDF1CCECA466DA577DDAC1230E3A350FA4B` |
| `spec/research/p09-source-presentations-lot2-3.md` | `1F36F2BCAFE8E1BB8599610EA1ECAAC7E204CC7847674696E9A50D0F3F8918B5` |

## Fresh visual source reading

I visually read every full journal image `journal-page-01.png` through `journal-page-17.png`, corresponding one-for-one to printed pp. 733--749, and every full conference image `conference-page-01.png` through `conference-page-10.png`, corresponding one-for-one to printed pp. 159--168. The controlling PDF hashes above matched the charter; the images were used only as the prescribed reading aids.

The journal pass covered, without skipped pages: p. 733 title, author order, affiliations, abstract, introduction, rights notice, ISSN line, issue and pagination; p. 734 introduction and syntax; p. 735 restricted fragment, structures, inclusive temporal clauses, `R`-structures, existential truth, and the opening `init/final/range/size` definitions; p. 736 Lemmas 3.1--3.3, ambient-relative acceptable-subsequence definitions, the preparatory strict sign, and `mu`; p. 737 the Lemma 3.3 proof inequalities, Theorem 3.4, and Theorem 3.5; pp. 738--739 the complete Theorem 3.5 certificate, Lemma 3.6, Theorem 3.7, and Theorem 4.1; p. 740 stuttering and the full Lemma 4.3 reduction; pp. 741--742 the computation-history reduction, journal `2S(n)` sentence, source truth sets, the faint exponent, fulfillment, and Lemmas 4.5--4.6; pp. 743--745 Lemma 4.6, Theorem 4.7, all local search recurrences, initial-since condition, period closing, obligation discharge, storage, Savitch, and the opening ETL definitions; pp. 746--747 Lemmas 5.1--5.2 and Theorems 5.3--5.4; p. 748 Table I, completion of Theorem 5.4, conclusion, correction notice, and beginning of references; p. 749 remaining references and receipt history.

The three chartered enlarged journal views were also read: `journal-page-04-acceptable-crop.png` confirms the literal strict acceptable-union sign on p. 736; `journal-page-10-bound-crop.png` confirms p. 742 prints `2^length(f)`; and the frozen enlarged p. 745 image `journal-page-13.png` confirms both the finite/infinite index defect and the `N_0 -> a_1 a_2 N_0`/even-state conflict.

The conference pass covered, without skipped pages: p. 159 identity, abstract, introduction, conference rights line; p. 160 syntax, semantics, and the formal universal validity clause; pp. 161--163 the conference Section 3 definitions, `2*length(f)` model statement, proof sketches, and Theorem 3.5 certificate; p. 164 the Section 4 reductions, terminal-machine wording, Figure 2, and `S(n)` next distance; p. 165 conference Lemmas 4.4--4.5 and Theorem 4.6 with the recurrent-type condition but without the journal's every-position until-discharge condition; p. 166 the predecessor ETL argument, `card(SF(f)) <= n^2`, grammar example, and conclusion; p. 167 Figure 3/table and bibliography; p. 168 remaining bibliography.

## Round-six arity/input-length repair

The supported round-five collision is repaired on all three required surfaces.

- Reader, `n-c-012.tex:2451--2467`: `n` is bound as the number of grammar terminals and constructor arity; the source's later local `q` for the same generic arity is explicitly alpha-renamed to `n`, with eliminable metalinguistic standing, purpose, and scope. The constructor is `N_j(f_1,...,f_n)`.
- Reader, `:2495--2533`: the closure, every node and child of `Gamma(S,j,N_i)`, Lemma 5.1, and every negated constructor in Lemma 5.2 retain the same `n`-tuple.
- Reader, `:2545--2556`: the source's distinct Theorem 5.4 use of `n` for total encoded input length is not rebound. It is alpha-renamed to `ell_in`, defined exactly as the length of the complete encoded formula-and-grammar input, classified as an eliminable metalinguistic size parameter, distinguished from terminal/constructor arity `n` and fragment notation `L(O_1,...,O_k)`, and used in `card(SF(f)) <= 2 ell_in`.
- Reader, `:2557--2589`: both the positive continuation/terminal rule and the negative `varphi` frontier rule retain `N_j(f_1,...,f_n)` and never rebind `n` or `ell_in`.
- Complete source note, `p09-sistla-clarke-1985-source-note.md:728--744` and `:776--868`: the same constructor/Gamma/Lemma 5.2 arity is `n`; `ell_in` is separately defined at `:826--837`; both Theorem 5.4 rules retain the `n`-tuple at `:838--860`.
- Compact presentation, `p09-source-presentations-lot2-3.md:306--341`: the local source `q` is alpha-renamed to arity `n`; total encoded input length is separately defined as `ell_in` and used only in `card(SF(f)) <= 2 ell_in`; the local `bar f := (f_1,...,f_n)` abbreviation supplies necessity, exact definition, metalinguistic standing, distinction, and immediate use in the two displayed rules. There is no rebinding.

This is an alpha-renaming of two distinct source variables, not a new theoretical object or restriction. It satisfies the terminology rule locally and preserves the source bound exactly.

## Criterion dispositions

### C1 -- checked clean

Work identity, author order, plural title, JACM volume/issue/date/pages, DOI, ISSN, receipt/revision/acceptance history, archive provenance, separate STOC object, file identities, and rights boundary are exact. Primary evidence is journal pp. 733 and 749 and conference pp. 159--168. The reader records the controlling identity and rights boundary at `n-c-012.tex:1853--1881`; the source note records exact identity, provenance, hashes, scan state, and rights at `:1--117`; the separate bibliography records are `handbook.bib:2245--2274`. Public reading access is never promoted to republication permission.

### C2 -- checked clean

The syntax, `L(O_1,...,O_k)` standing, `L-tilde(F,X)` restriction, inclusive `X/U/S/F` clauses, structures, interpretations, total finite `R`-structures, existential source path quantifier, universal program-correctness counterexample relation, and reconstructed validity boundary match journal pp. 734--735 and Table I on p. 748, with conference p. 160 used only as predecessor evidence for the formal validity clause. Reader locators are `:1883--1990`; source-note locators are `:147--270`.

### C3 -- checked clean

The full Section 3 chain is source-exact at reader `:1992--2225`: unique maximal `final(S)` and the exact decomposition and finite measure; ambient-relative acceptable-subsequence definitions; Lemmas 3.1--3.3 with exact hypotheses and quantifiers; both strict/non-strict conflicts and unknown cause; Theorems 3.4--3.7; 3-SAT diamond reduction; `SF(f)` definition before certificate use; bound start symbol; every Theorem 3.5 labelling rule with current-position-inclusive `F`; literal strong-connectivity/entry-edge checks; concrete loopless-singleton false acceptance; separately owned directed-cycle correction; `mu(f)` and formula-length measures; and proof granularity. Journal evidence is pp. 735--739.

### C4 -- checked clean

Reader `:2227--2446` preserves the exact Section 4 chain: the complete Lemma 4.3 `P_1/P_2`, `g_1/g_2/g_3`, `f_x`, `h_1/h_2/h_3`, `f'`, `f''` construction; `L(F,X)` preservation; both self-loop-sensitive pure-`U` replacements and Lemma 4.2; Figure 2 and the p. 741 journal `2S(n)` distance; the p. 742 source truth-set definition and `2^length(f)` count; inclusive fulfillment; exact Lemma 4.5 deletion; both Lemma 4.6 conclusions; Theorem 4.7 bounds, valuation periodicity, truth-set equality, and every-position obligations; `Ff` for past `S`; all five directional search recurrences; initial-since, loop closure, within-period discharge, storage, and Savitch. Journal evidence is pp. 740--745; conference p. 164 supplies only the contrasted `S(n)` predecessor wording.

### C5 -- checked clean

Reader `:2448--2598` gives exact ETL grammar semantics with disjoint nonterminals, normalized productions, one bound arity `n`, finite/infinite typing disclosure, parity conflict, enlarged closure, exact labelled tree `Gamma`, Lemmas 5.1--5.2 and both inherited conclusions, distinct tree-depth and until obligations, Theorem 5.3 bounds and every-position obligations, exact Theorem 5.4 positive rule, singleton negative-frontier initialization, present-to-next update, within-period emptiness, input encoding, and calibrated correction notice. The round-six `ell_in` alpha-renaming is exact as detailed above. Journal evidence is pp. 745--748; the distinct conference argument is pp. 166--167.

### C6 -- checked clean

The reader's complete table at `:2600--2630` reproduces every Table I row and explicitly distinguishes the unlisted-in-Theorem-4.1 `L(U,X)` row. Shared theorem `logic-in-computer-science.tex:693--708` uses exactly `L(U) subseteq L(U,X) subseteq L(U,S,X)` for hardness and upper bound. Shared model-checking method/theorem `:761--809` preserves existential truth of the negated formula, finite product path plus nonempty product cycle, and deterministic polynomial-space closure under complement for universal-path model checking.

### C7 -- checked clean

The conference/journal separation is complete and accurate. The reader uses the journal body as controlling at `:1872--1881`, pinpoints journal `2S(n)` versus conference `S(n)` at `:2289--2294`, and refuses to identify a unique Section 5 repair at `:2593--2598`. The complete source-note reconciliation is `p09-sistla-clarke-1985-source-note.md:941--980`. No conference theorem number, bound, hypothesis, or proof language is silently imported into the journal account.

### C8 -- checked clean

The bibliography is accurate and version-separated at `handbook.bib:2245--2274`. The complete source-note page map is `:119--145`, proof-status map is `:914--939`, material version comparison is `:941--980`, and rights boundary is `:58--117`. The compact presentation `p09-source-presentations-lot2-3.md:185--388` is consistent with the reader and source note, including the round-six repair. Locators place definitions, conclusions, references, proof statuses, defects, and differences on the pages actually read.

### C9 -- checked clean

The prose is independently reconstructed rather than copied, definitions precede use, types and quantifiers are explicit, and source statements, printed defects, context-forced reconstructions, and handbook-owned corrections remain distinct. The five-part terminology rule is locally satisfied for fragment notation and `SF` (`:1896--1920`), acceptable subsequence and ambient subscripts (`:2036--2066`), `mu`, labels, and start alias (`:2085--2088`, `:2143--2195`), reduction auxiliaries (`:2233--2262`), source truth sets and fulfilled-before obligations (`:2300--2323`), successive guesses `A,B` (`:2402--2407`), ETL constructor and `Gamma` (`:2451--2512`), `ell_in` (`:2545--2556`), and `varphi` (`:2572--2592`). No hypothetical new technical name is introduced without necessity, definition or axiom, standing, nonredundancy, and use.

## Invariant dispositions

- **I1 -- checked clean.** Review method was direct source reading, mathematical comparison, and prose inspection only; no prohibited check or build was run.
- **I2 -- checked clean.** All ten round-six hashes matched twice; no snapshot object changed during the review.
- **I3 -- checked clean.** All seventeen journal and all ten conference page images were freshly read, with claims checked against the printed pages and the matched controlling PDF identities.
- **I4 -- checked clean.** Enlarged p. 742 prints `2^length(f)`; enlarged p. 745 preserves both ETL conflicts.
- **I5 -- checked clean.** Journal and conference numbering, bounds, hypotheses, and proof language remain separate; the conclusion identifies neither a precise bad inference nor a unique repairing lemma.
- **I6 -- checked clean.** Fragment notation, restricted fragment, inclusive `U/S`, existential `R`-truth, satisfiability, and validity remain distinct; the journal-relative validity clause is explicitly reconstructed.
- **I7 -- checked clean.** `size(S)` is the finite measure of an infinite structure; `final(S)` is the unique maximal suffix; subsequence measures are ambient-relative; both strict defects and proof-supported non-strict forms are disclosed without an invented cause.
- **I8 -- checked clean.** Journal `2S(n)`, closure size, realized truth-set count, and inclusive fulfilled-before witness endpoints remain distinct and exact.
- **I9 -- checked clean.** Theorem 4.7 retains valuation and truth-set periodicity plus every-periodic-position discharge, exact bounds, `Ff`, initial-since, and Savitch at their printed strengths.
- **I10 -- checked clean.** The full ETL convention, constructor, closure, `Gamma`, finite-tree obligation, Theorems 5.3--5.4, continuation search, finite-word typing reconstruction, and unresolved parity conflict are exact.
- **I11 -- checked clean.** Sketches, asserted inductions, abbreviated cases, and brief replacements are not upgraded; no Sistla--Clarke automata or Buechi construction is asserted.
- **I12 -- checked clean.** Every handbook-introduced technical expression in scope satisfies necessity, exact definition, standing, nonredundancy, and actual use locally.
- **I13 -- checked clean.** Independence restrictions were obeyed; prohibited board records and other verdicts were not read or solicited.
- **I14 -- checked clean.** This verdict is independent and not based on a vote or another seat's position.
- **I15 -- checked clean.** The acceptance language below is confined to `N-c-012.d` topic-level manuscript review and does not claim any downstream closure.

## Mandatory-check dispositions

- **M01 -- checked clean.** The enlarged p. 742 crop visibly prints the number of realized source truth sets as `2^length(f)`. Reader `:2308--2315`, source note `:600--614`, and compact presentation `:207--213` reject attribution of `2^(2 length(f))`.
- **M02 -- checked clean.** Journal pp. 734--735 contain no standalone validity clause; conference p. 160 does. Reader `:1977--1990` and source note `:261--270` mark the universal journal-relative clause as reconstruction.
- **M03 -- checked clean.** Journal p. 742 defines fulfillment for `j >= i` with a witness `i <= l <= j`. Reader `:2316--2323` and source note `:629--632` preserve both inclusive endpoints.
- **M04 -- checked clean.** Enlarged p. 736 confirms literal `<` in the acceptable-union sentence and the full p. 736 image confirms literal `<` in Lemma 3.3. P. 737 uses `<=`, the atomic/null case is `0 <= 0`, and Theorem 3.4 is non-strict. Reader `:2067--2122` and source note `:340--411` disclose both conflicts.
- **M05 -- checked clean.** Journal p. 741 prints `2S(n)`; conference p. 164 prints `S(n)`. Reader `:2289--2294`, source note `:585--599`, and compact `:343--348` preserve the split.
- **M06 -- checked clean.** Journal Theorem 4.7 on pp. 743--744 has `i <= 2^(1+length(f))`, positive `p <= 4^(1+length(f))`, equality and fulfillment for every `k >= i`; Theorem 5.3 on pp. 746--747 has `l <= 2^(1+card(SF(f)))`, `p <= c^card(SF(f))`, and both obligation families for every periodic position. Reader `:2380--2400`, `:2535--2544`; source note `:693--725`, `:813--825`.
- **M07 -- checked clean.** P. 745 literally says finite or infinite string and then uses unrestricted nonnegative indices. Reader `:2468--2479` and source note `:746--755` label the finite represented-position restriction as handbook-supplied typing.
- **M08 -- checked clean.** P. 745 prints `N_0 -> a_1 a_2 N_0` and says `N_0(True,P)` tests even states, while the zero-based clause puts `P` at odd offsets. Reader `:2484--2493` and source note `:757--774` preserve the conflict without choosing a repair.
- **M09 -- checked clean.** Reader `:2495--2512` and source note `:778--793` give the exact ETL closure and every `Gamma(S,j,N_i)` edge condition. Continuation productions generate tree children; terminal productions remain the separate finite-witness condition.
- **M10 -- checked clean.** Reader `:2514--2517` defines finite-tree depth fulfillment and distinguishes it from until fulfillment; `:2572--2592` initializes and updates the continuation set and requires emptiness within the guessed period. Source note `:794--812`, `:849--868` agrees.
- **M11 -- checked clean.** The p. 748 notice says only that a theorem used in the conference proof contained an error and that the journal submission corrected it. Reader `:1874--1881`, `:2593--2598`; source note `:24--33`, `:973--980` do not identify the inference or a unique new repair lemma.
- **M12 -- checked clean.** Proof qualifications match the pages and source-note table `:914--939`; reader `:2440--2446`, `:2534--2535`, `:2592--2598` attributes no Buechi construction to Sistla--Clarke. The separate shared automata material is explicitly Vardi--Wolper-owned at `logic-in-computer-science.tex:745--753`.
- **M13 -- checked clean.** Shared theorem `:693--708` uses exactly `L(U) subseteq L(U,X) subseteq L(U,S,X)` for the Table I classification, matching reader `:2622--2629` and journal p. 748.
- **M14 -- checked clean.** Reader `:1967--1976` preserves the source's existential path quantifier. Shared method/theorem `:761--809` searches a path satisfying the negation and uses deterministic polynomial-space closure under complement for universal model checking.
- **M15 -- checked clean.** Acceptable subsequence, ambient subscript, source truth set, fulfilled-before obligations, ETL constructor, and `Gamma` each have local necessity, exact eliminable definition or source-defined standing, type/standing, distinction, and later use at the C9 locators above.
- **M16 -- checked clean.** Source-note page map `:119--145` places `init/final/range/size` on p. 735, conclusion only on p. 748, and references on pp. 748--749; the visual pass confirmed each placement.
- **M17 -- checked clean.** Conference p. 160's formal validity clause is recorded while the identical reader clause remains reconstructed relative to journal pp. 734--735 (`n-c-012.tex:1977--1990`). The correction notice is limited exactly as in M11.
- **M18 -- checked clean.** Lemma 3.2's common prefix length, pointwise prefix equality, zero-prefix first-valuation condition, range equality, and biconditional are exact at reader `:2015--2034`. Lemma 3.3's acceptable input/output, every-intermediate-supersequence quantifier, surviving-position scope, and sign conflict are exact at `:2088--2122`. Lemma 3.6's finite subsequence containing the current state and universal intermediate-supersequence conclusion are exact at `:2217--2223`. Journal evidence is pp. 736--739.
- **M19 -- checked clean.** Reader `:2281--2298` and source note `:585--599` identify each Figure 2 diamond as one tape-cell position, each full BI-to-EI traversal as one instantaneous description, repeated traversals as a computation, and journal terminal configurations as persistent without tape changes. Conference p. 164's halting language remains separate.
- **M20 -- checked clean.** Reader `:2366--2378` and source note `:633--644` define source periodicity for `i in N`, positive `p`, and all `k >= i` by equality of complete valuations, and distinguish it from truth-set equality and both obligation families.
- **M21 -- checked clean.** Shared method/theorem `logic-in-computer-science.tex:761--809` returns a finite product path plus a nonempty product cycle whose unfolding is the counterexample, without an undefined periodicity name.
- **M22 -- checked clean.** Reader `:2501--2512`, source note `:781--793`, and compact `:338--341` call `Gamma` the source's labelled tree or the full tree `Gamma`; no unsupported proof-tree, derivation-tree, or continuation-tree synonym occurs.
- **M23 -- checked clean.** Every charter-retained round-one repair class embodied in `C1`--`C9`, `M01`--`M22` is present on the frozen round-six surfaces, with no weakening or regression.
- **M24 -- checked clean.** Reader `:1992--2013` defines the unique maximal suffix, exact `s = init(S).final(S)` decomposition, structure-level `range`, and structure-level finite measure before later use, matching p. 735.
- **M25 -- checked clean.** Reader `:2036--2066` defines the p. 736 acceptable-subsequence split and measures relative to ambient `S`; `:2042--2050` supplies exact eliminability, metalinguistic standing, necessity, nonredundancy, and later use for the subscript.
- **M26 -- checked clean.** Reader `:2067--2122` preserves the preparatory strict sentence, null/null counterexample, proof-supported non-strict subadditivity, and defines `mu(f)` before Lemma 3.3 use.
- **M27 -- checked clean.** Reader `:2143--2195` has the exact prefix bound, subset `C`, source strong-connectivity and entry-edge checks, empty initialization, all four iff labelling rules on every prefix/`C` node, current-inclusive `F`, and acceptance iff `f` is in the start label.
- **M28 -- checked clean.** `handbook.bib:2245--2258` is a distinct accurate STOC record; direct conference claims cite `SistlaClarke1982`, while journal claims cite the separate article record at `:2260--2274`.
- **M29 -- checked clean.** Every charter-retained round-two repair class in `M24`--`M28` remains present; the newly disclosed preparatory strict-sign conflict is literal-source-exact; no earlier criterion, invariant, or mandatory check is weakened.
- **M30 -- checked clean.** Reader `:2289--2298` pinpoints journal `2S(n)` to p. 741, conference `S(n)` to p. 164, and the broader journal reduction to pp. 741--742.
- **M31 -- checked clean.** Reader `:2156--2195` initializes labels empty, processes `SF(f)` in increasing length, gives exact atomic/negation/conjunction/`F` iff rules, and accepts at the start label. Reader `:2197--2214` preserves literal source checks, concrete loopless-singleton false acceptance, and the handbook-owned directed-cycle correction only.
- **M32 -- checked clean.** Reader `:2233--2279` gives the exact Lemma 4.3 atom sets and every named auxiliary formula, `L(F,X)` preservation, both pure-`U` replacements, and exact reliance on Lemma 4.2.
- **M33 -- checked clean.** Reader `:2324--2364` deletes `s_i,...,s_(j-1)` while retaining `s_j`, preserves every common token's truth set, and states every Lemma 4.6 hypothesis and both conclusions.
- **M34 -- checked clean.** Reader `:2402--2438` has the exact Boolean, `X`, `U`, direction-sensitive `S`, and initial-since rules, loop-entry equality, within-period `U` discharge, three-set/two-counter storage, and Savitch step.
- **M35 -- checked clean.** Reader `:2517--2544` gives Lemma 5.2's extra negated-grammar obligation and both inherited conclusions. Reader `:2557--2592` gives Theorem 5.4's positive iff rule, singleton initialization, exact frontier update, and within-period emptiness.
- **M36 -- checked clean.** `label` (`:2156--2195`), Lemma 4.3 formula names (`:2233--2262`), `A,B` (`:2402--2407`), and `varphi` (`:2572--2589`) each have an exact eliminable definition, metalinguistic standing, nearby-object distinction, necessity, and immediate use.
- **M37 -- checked clean.** Every charter-retained round-three repair in `M30`--`M36` remains present on the common snapshot; no source wording is silently strengthened and no previous check is weakened.
- **M38 -- checked clean.** Reader `:1905--1920` defines `SF(f)` before Theorem 3.5, including ordinary subformulas, single-negation mates, double-negation elimination, `card(SF(f)) <= 2 length(f)`, and its distinction from the later realized-truth-set count.
- **M39 -- checked clean.** Reader `:2143--2147` explicitly binds source `q_0 := delta` before prefix and acceptance use; source note `:428--472` and compact `:249--261` do likewise.
- **M40 -- checked clean.** Reader `:2169--2189` permits a witness at the current prefix occurrence, preserves the printed word “after,” explains the non-strict reading from pp. 734--735 and p. 737, supplies the strict-reading counterexample, and keeps it separate from the cycle correction.
- **M41 -- checked clean.** Arity `n` is consistent through constructor, `Gamma`, Lemmas 5.1--5.2, and both Theorem 5.4 rules in the reader and source note. The compact-only `bar f` abbreviation is locally and completely typed at `p09-source-presentations-lot2-3.md:322--326` and used only in the two rules.
- **M42 -- checked clean.** Every charter-retained round-four repair in `M38`--`M41` remains present; the source's words and defects are not silently strengthened or repaired, and no earlier criterion or check is weakened.
- **M43 -- checked clean.** The exact three-surface round-six disposition is given in the dedicated section above. `n` remains terminal count and constructor arity through constructor, `Gamma`, Lemma 5.2, and both Theorem 5.4 rules. Source input length is consistently alpha-renamed to `ell_in`, exactly defined, metalinguistic, distinguished from arity `n` and fragment notation, actually used in `card(SF(f)) <= 2 ell_in`, and never rebound.
- **M44 -- checked clean.** The single supported round-five arity/input-length collision is repaired on all common round-six hashes. Rechecking `C1`--`C9`, `I1`--`I15`, and `M01`--`M43` found no weakening, regression, or new defect.

## Final coverage note

Every required source page was visually read; every frozen hash matched; every specified manuscript/source surface was read completely at the chartered location; and all criteria, invariants, prior mandatory repairs, source defects, reconstructions, version boundaries, locators, proof-strength qualifications, terminology obligations, and rights qualifications checked clean. Acceptance is limited by `I15`: it closes only this independent round-six `N-c-012.d` topic-level scholarly review on the frozen snapshot and does not close any downstream manuscript, build, rendering, human-review, book-completion, or user-acceptance gate.

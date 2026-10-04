# Independent source-fidelity review: PA checker and finite abduction

Date: 7 September 2026. Reviewer: fresh independent source-fidelity context `pa_abduction_source_review`. Repository: `C:\Dev\the-methods-of-reason`, branch `phase4-codex`, HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`.

## Verdict and scope

**Scope A: FAIL for exact finite-description selection, because SF-A1 remains open.** The numerical syntax, direct axiom criterion, and all twenty rule clauses agree with the inspected dependencies. The remaining issue concerns the promised particular formation tree and therefore the exact selected arithmetic formulas.

**Scope B: PASS for the assigned finite abduction source/text scope.** The actual held manuscript supports the attributed definitions, restrictions, two selected preference orders, and Proposition 2.1. The inconsistent-input extension, finite procedure, and examples are identified as handbook additions. This bounded unit expressly leaves the rest of the source presentation and wider abduction coverage open.

These verdicts are source/text findings. They do not grant mathematical-specialist acceptance, publication acceptance, build or visual acceptance of manuscript pages, formal admission, or completion of the standard-predicate or P16-C1 obligations. The reviewer did not author either unit, edit manuscript/shared files, consult current reviewers' findings, spawn agents, or run tests or a manuscript build/render. The PDF skill was used only to extract and inspect primary-source pages. Only this assigned report was written in the repository.

The governing contract was read completely: `spec/EDITION-2026-CONTRACT.md`, SHA-256 `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3`. The lead confirmed an integration freeze with unchanged assigned-file hashes; those hashes were independently rechecked after the confirmation. All findings below were prepared blind, before cross-review.

## SF-A1: the seven-constant bounded sum has no specified total selector

**Status: FAIL. Affected claim: the complete expansion determines one particular finite primitive recursive description.**

Exact locations:

- `handbook/parts/p05/pa-checker-arithmetization.tex:66-80` makes every bounded sum a primitive recursion followed by substitution of its bound. Its update must consequently be an already specified total primitive recursive expression.
- The same file at `282-287` uses `sum_{j<7} E(a,q_{j+1})`, and says each `q_j` inserts its finite constructor expression.
- `handbook/parts/p05/standard-pa-proof-predicate.tex:15-35` specifies seven individual constructor constants `q_1,...,q_7`. It supplies no total function of a numerical counter `j`.
- `handbook/restoration/inherited-07678-07752.tex:4-28` requires total functions on finite powers of N, with a total step function for primitive recursion. `handbook/restoration/inherited-09262-09327.tex:76-114` defines Gamma from an actual finite formation tree with its arities.
- The new body at `398-409` selects `d_19` and `Gamma_{d_19}` from all the preceding expansions. The new annex at `11-34` and `103-113` claims that this expansion is complete and the seven constant tests are unchanged.

The numerical membership criterion is clear and matches the source. The description language has an unresolved compilation step: inside the prescribed fold, `j` is the recursion counter, so `q_{j+1}` needs a total selector expression. Neither this unit nor its cited seven-constant definition declares a coded constant list and entry lookup, a total ordered case selector with a final default, or an explicit exception that unrolls this particular fixed sum.

The distinction matters even though the final fold uses only `j=0,...,6`. For example, with `Q=[q_1,...,q_7]`, the descriptions `q(j)=e(Q,j)` and `q'(j)=I(lt(j,7),e(Q,j),q_1)` agree on every counter actually used by this sum but have different total definitions and formation trees. Both require an added choice. Replacing the sum by seven explicitly listed, left-associated terms makes another particular formation tree. Standard-value agreement of these possible completions does not select one Gamma formula under the governing graph definition.

The finite-membership convention at body `45-46` specifies the sign, order, and equality tests; it does not resolve how that convention interacts here with the explicit bounded-sum-as-fold rule at `74`. The raw-list zero default at `99-100` would resolve the missing selector if the text explicitly used the coded list, as it does for the two arity lists at `318-319`.

Required correction: choose and state one expansion, for example a particular coded list `Q=[q_1,...,q_7]` with `e(Q,j)` in the bounded sum, or an expressly unrolled seven-term sum with its existing association convention. Then recheck the affected description and Gamma-selection claims, including the copy of `chi_19` inside `d_mp`. This review supplies no manuscript repair or replacement selector.

Consequence: exact selection of `d_19`, `Prf^19_PA`, `Prv^19_PA`, and the `d_mp` that calls this checker stays open. The numerical source match established below remains usable evidence for the stated seven-constant membership criterion. The internal joining argument has the source dependencies and rule arguments described below, but its conclusion for the claimed uniquely selected description is **UNRESOLVED** until SF-A1 is resolved.

## Scope A component results

Abbreviations in the following tables: A-body and A-annex are the two assigned `pa-checker-arithmetization.tex` files; N-body and N-annex are the two `standard-pa-proof-predicate.tex` files; Coding is `handbook/restoration/inherited-09328-09438.tex`; Graph is `handbook/restoration/inherited-09262-09327.tex`; Internal is `handbook/annex/p05/internal-proof-predicate.tex`. All locators are one-based source lines.

| Component | Result | Exact comparison and evidence |
| --- | --- | --- |
| Initial functions, composition, recursion and arities | PASS for the library clauses; complete checker expansion FAIL at SF-A1 | A-body 10-81 uses recursion argument last and projection insertion. Graph 76-114 and `inherited-07678-07752.tex:4-28` provide the actual arities, including nullary zero and nullary composition. The existing A,H,K,C descriptions are Graph 187-233. |
| Lists, constructor coding, total entry defaults | PASS | A-body 84-133 and A-annex 44-59 match Coding 24-64 and 85-121. The positive cons is successor of the fixed Cantor pairing; code zero is the empty raw list. Both inverse searches include the unique components below a positive code. The tail sum counts exactly the nonzero tails. Out-of-range entries are zero. |
| Grammar, node counts and maximum indices | PASS | A-body 136-157 matches every tag, exact arity and child type in Coding 45-64. Expression children exclude binder indices, include term children of equality, and preserve printed child order. Invalid expression metadata are zero. Earlier-child retrieval matches Coding 109-121. |
| All/free variables, increasing free-index list, sentences | PASS | A-body 159-178 matches Coding 117-121 and N-body 45-51. Quantifier binders enter the all-variable test and remove their index from the free-variable test. The bound `i<c` includes all indices occurring in valid c. |
| Capture-avoiding substitution, least fresh variable, stopped binders | PASS | A-body 181-233; A-annex 61-90; Coding 153-201; `inherited-03240-03428.tex:17-46`. The renaming branch tests occurrence in the replacement term, selects the least index absent from matrix/replacement and unequal to both named indices, and runs even when the variable being replaced is absent freely. The preliminary rename stops at a shadowing binder. The stated shape bound counts original-node visits, extra rename visits, and assembly/continuation commands. |
| Substitution malformed states and extraction | PASS | A-body 183-191, 221-233 fixes three state fields, success bit, every command arity, stack existence, allowed assembly tags, absorbing failure/completion, fixed iteration bound, and final singleton extraction. Binary pop order reconstructs left then right. No unbounded run or search is imported from Coding. |
| Alpha comparison | PASS | A-body 235-256 and A-annex 92-101 match Coding 203-222 and the generating relation in `inherited-03240-03428.tex:67-77`. Nearest binder gets tag 18 with zero-based depth; free variable gets tag 17 with its original index; a quantifier comparison record has one matrix argument. Invalid formula entry fails. |
| Canonical induction constructor and recognizer | PASS for numerical criterion | A-body 259-279 matches N-body 45-108 and N-annex 45-139. Matrix/binder recovery, maximal universal-prefix stripping, literal reconstruction, free parameters in increasing order, filtering the induction index, zero malformed-matrix default, and absence of an extra free-occurrence requirement agree. |
| Seven arithmetic axiom values | PASS for numerical/source fidelity; description selector FAIL | N-body 15-43 decodes to the active seven universal closures in `inherited-09099-09111.tex:1-13` with the declared x_0,x_1 representatives. Induction is the active scheme in `inherited-09175-09187.tex:2-12`. A-body 282-287 retains precisely these values but has SF-A1. |
| Common row tests and parent counts | PASS | A-body 290-319 and 368-386 match Coding 224-258, 418-447 and N-annex 226-252. The two 20-entry arity lists agree entry for entry. All rows have five fields; references are earlier; nonassumption markers are zero; every nonroot has one parent occurrence and root has none. The global product includes every row bit. |
| Twenty local rule clauses | PASS | Every tag is compared separately below. |
| Outer proof sort, sentence root and surviving axiom leaves | PASS for numerical criterion | A-body 389-397 matches N-body 174-207. Outer tag 19, inner tag 15, exact arities, zero certificate field, nonempty tree, literal root equality, sentencehood, and only surviving open-leaf axiom tests are retained. Empty open lists contribute one. |
| Gamma source, syntactic class and selected formula | Source dependency PASS; claimed exact selection FAIL | A-body 398-435 invokes the actual Graph 76-149 construction and fresh-variable convention. Internal 229-310 proves that construction; `inherited-08306-08438.tex:61-94` supplies the stated marked-bounded Sigma-1 closure convention. SF-A1 prevents the complete claimed d_19 from being selected by the present text. |
| Numerical proof meaning and separation from the c.e. convention | PASS as source/dependency transport | A-annex 131-139 uses the numerical theorem actually stated and proved in N-body 224-241 and N-annex 254-302. Tag 19 is separate from tag 16 and Comp certificates; the equivalence used is proof existence. |
| Internal list/table/sentence facts | PASS for dependency fidelity | A-annex 141-314 uses the actual specified Graph equations, Internal 15-107 and the beta/collection proofs at Internal 109-303. Head/tail, bounded tail descent, length, entry, extensionality, map/filter, product, prefix, and free-index bounds are supplied in the annex before joining uses them. |
| MP constructor and all reused rule arguments | PASS for source fidelity; selected-description theorem UNRESOLVED | A-body 438-458 and A-annex 325-508 preserve antecedent-first implication elimination, shift only row-reference lists, and use the direct axiom products. Coding 274-277 fixes the body/sheet order translation; Internal 424-470 is the distinct earlier certified numerical constructor. A-annex explicitly handles minor-then-major order for existential elimination, unchanged substitution/alpha arguments, and branch-local labels. SF-A1 propagates through the chi_19 guard. |
| D1/D2 and remaining D3 boundary | PASS for attribution/dependency boundary; exact selected-formula claims remain affected by SF-A1 | A-body 461-516 and A-annex 510-536 identify D1 as a finite standard computation and D2 as the internal joining consequence. D3, the evidence-to-proof builder, and internal identification with the earlier arbitrary Q representative remain open, consistently with Internal 474-524 and Graph 151-158. |

### All twenty rows

Premise/parameter counts are compared with N-annex 229-237. The source formula and discharge conditions are Coding 260-306; the underlying rules are also read in `inherited-02193-02340.tex:1-78`, `inherited-03927-04061.tex:4-60`, and `registry/calculi/nd-fol.tex:10-29`.

| Tag | Rule | Premises / parameters | A-body | Primary numerical locator | Result |
| --- | --- | --- | --- | --- | --- |
| 0 | assumption | 0 / 0 | 327 | Coding 225-258 | PASS: O=[j], marker unrestricted natural number. |
| 1 | conjunction introduction | 2 / 0 | 328 | Coding 264-265 | PASS: child order and concatenation retained. |
| 2 | conjunction elimination 1 | 1 / 0 | 329-330 | Coding 264-266 | PASS: first child. |
| 3 | conjunction elimination 2 | 1 / 0 | 329-330 | Coding 264-266 | PASS: second child. |
| 4 | disjunction introduction 1 | 1 / 0 | 331-332 | Coding 266-267 | PASS: premise is first disjunct. |
| 5 | disjunction introduction 2 | 1 / 0 | 331-332 | Coding 266-267 | PASS: premise is second disjunct. |
| 6 | disjunction elimination | 3 / 2 | 333-335 | Coding 268-271 | PASS: two separate nonvacuous filters, then major/second/third order. |
| 7 | implication introduction | 1 / 1 | 336-337 | Coding 272-274 | PASS: exact antecedent and label, nonvacuous removal. |
| 8 | implication elimination | 2 / 0 | 338-339 | Coding 274-277 | PASS: antecedent first, implication second, matching body order. |
| 9 | negation introduction | 1 / 1 | 340-341 | Coding 278-279 | PASS: bottom premise and removal of the negated formula. |
| 10 | negation elimination | 2 / 0 | 342-343 | Coding 280-281 | PASS: formula then its negation, bottom conclusion. |
| 11 | bottom elimination | 1 / 0 | 344 | Coding 281-282 | PASS: arbitrary formula conclusion, unchanged open list. |
| 12 | RAA | 1 / 1 | 345-346 | Coding 282-284 | PASS: remove the literal negation of the conclusion. |
| 13 | universal elimination | 1 / 3 | 347-348 | Coding 285-287 | PASS: matrix and term type tests, exact substitution. |
| 14 | existential introduction | 1 / 3 | 349-350 | Coding 287-289 | PASS: same witnesses, inverse pattern. |
| 15 | universal introduction | 1 / 1 | 351-353 | Coding 290-292 | PASS: free-variable test on every open premise assumption. |
| 16 | existential elimination | 2 / 4 | 354-361 | Coding 293-300 | PASS: minor discharge first, minor remainder followed by major list, all-variable absence in conclusion/major/all surviving assumptions. |
| 17 | alpha conversion | 1 / 0 | 362 | Coding 301 | PASS: specified syntactic alpha test. |
| 18 | identity introduction | 0 / 1 | 363 | Coding 302-303 | PASS: premise-free t=t with term witness, empty open list. |
| 19 | identity elimination | 2 / 4 | 364-366 | Coding 303-306 | PASS: exact matrix/index and both terms; no required free occurrence in the matrix. |

## Scope B source identity and detailed results

The actual source is [the held Eiter-Gottlob manuscript](C:/Dev/the-methods-of-reason/source/references/eiter-gottlob-abduction/eiter-gottlob-abduction-jacm-manuscript.pdf), SHA-256 `E2A021C45BCDC6D2D1BC7AAC9972E75FEC697E3609094060CA92AFFCB694F265`.

The title page identifies Thomas Eiter and Georg Gottlob, *The Complexity of Logic-Based Abduction*, Christian Doppler Laboratory for Expert Systems / Institut fuer Informationssysteme / Technische Universitaet Wien. It has no publication date on that page. Its footnote identifies the STACS 1993 extended abstract as a related earlier manifestation. The actual PDF contains 46 physical pages: an unnumbered title page followed by printed pages 1-45; the endpoint was inspected directly. Metadata `/Title` is `jacm.dvi`; the Ghostscript/dvips conversion metadata is not used as a publication date. The journal article's pagination was not substituted.

Primary pages read completely as extracted text and visually inspected: physical 1, 2, 5, 6, 10, 11, 12, 46, corresponding to title, printed 1, 4, 5, 9, 10, 11, 45. Physical 9 and 13 (printed 8 and 12) were additionally read completely as text for adjacent scope context. The other 36 physical pages were not read; no verdict is given on their remaining results. All required formal definition and Proposition 2.1 passages lie in the fully read and visually inspected physical pages 10-12.

Both assigned abduction files were read in full. B-body and B-annex below denote their respective `finite-abduction.tex` files.

| Component | Result | Manuscript and exact primary locator |
| --- | --- | --- |
| Version and citation locator | PASS | B-body 5-16 and citations at 93-94, 137-138, 166-168; B-annex 5-9. The held source's Definitions 2.1/2.2 are printed 9/10, and Proposition 2.1 is printed 11. Canonical bib 6598-6606 uses a distinct unpublished manuscript key and identifies its actual pagination. |
| Input tuple, finite alphabet and finite theory | PASS | B-body 21-48; source Definition 2.1, printed 9 / physical 10, with the preceding paragraph defining a theory as a finite set. Tuple order is V,H,M,T. |
| Positive atomic hypotheses and observations | PASS | B-body 25-44; Definition 2.1 puts H,M inside V, and the positive-atom discussion after Definition 2.2, printed 10 / physical 11, excludes negative and compound hypothesis formulas from this model. T may contain arbitrary classical propositional formulas. |
| Possible H/M overlap and unused alphabet atoms | PASS | B-body 34-46 exactly retains both freedoms expressly stated after Definition 2.2 at printed 10 / physical 11: no required disjointness and no required exhaustive union. |
| Consistency and consequence criterion | PASS | B-body 50-104 and B-annex 13-67 match Definition 2.2, printed 10 / physical 11. Consistency is satisfiability; explanation requires a model and truth of every manifestation in every such model. Expl corresponds to Sol. |
| Explicit inconsistent-input extension | PASS | B-body 13-16, 95-109; B-annex 35-65. Source Definition 2.1 requires consistent T. The chapter labels the relaxed input convention, proves the model-set inclusion, and accepts no candidate for inconsistent T. |
| Source/book alphabet and connective translation | PASS | B-body 38-41, 90-94; B-annex 35-49. Source language paragraph printed 9 / physical 10 includes top and biconditional. Book `inherited-01661-01816.tex:48-58` expands them to negated bottom and conjunction of the two implications. `inherited-01817-01898.tex:4-60` supplies the actual truth clauses and consequence definition. Extension/restriction and naming preserve all required truths, subsets, inclusion and cardinality. |
| Empty data and empty observations | PASS | B-body 34, 95-103, 213-216; B-annex 54-67. Finite-set source definitions exclude no empty case. The unique empty valuation and empty candidate conventions are supplied explicitly and agree with those definitions. |
| Subset and cardinality preferences | PASS | B-body 122-143; source Definition 2.3 and following subset discussion at printed 10 / physical 11, continuing the cardinality order at printed 11 / physical 12. Both are minimal-element selections under the source's stated preorders; no probability or cost is supplied by those formal data. |
| Single-deletion characterization | PASS | B-body 145-173; B-annex 103-120; Proposition 2.1 and complete proof at printed 11 / physical 12. The premise that E is already an explanation is retained. The converse explicitly derives consistency of its deletion from consistency of E and consequence from a smaller explanation. |
| Finite minimal-family existence and qualified upward closure | PASS as attributed handbook deductions | B-body 145-179; B-annex 73-124. The direct finite-set arguments retain the consistency qualification and do not attribute an unqualified upward closure to the source. Source printed 5 / physical 6 also states the cardinality/subset inclusion distinction. |
| Exhaustive construction, operation count and exact outputs | PASS as attributed handbook construction | B-body 10-11, 184-233; B-annex 128-182. The fixed finite candidate and valuation scans, persistent flags, both filters, empty cases, and exact `2^(r+n)` pair count are supplied here. Formula evaluation and filtering remain additional work. No source algorithm or complexity classification is claimed. |
| Six examples and truth boundary | PASS as attributed handbook examples | B-body 238-315 and B-annex 184-283. The examples are explicitly additional, and all candidate families and the countervaluation are supplied. Source definitions are the premises; these are not presented as the source's examples. |
| Probability, causal interpretation and remainder | PASS for the bounded attribution | B-body 139-140, 317-340. The source discusses probabilistic interpretations under additional assumptions at printed 4-5 / physical 5-6; the chapter does not claim that the bare tuple supplies those assumptions. General-formula translations mentioned at source printed 10, preference extensions, complexities, diagnosis and causal/probabilistic relationships remain separate obligations. The chapter expressly excludes completion of the full source presentation. |

No abduction source mismatch, omitted qualification within the assigned finite scope, incorrect manuscript-page locator, or undisclosed extension was found. The broader source and subject obligations remain open exactly as the chapter states.

## Frozen files, complete read extents, and hashes

All hashes are SHA-256. Paths in this inventory are relative to the repository. A range ending in EOF means the actual file was read completely, including its proof text; a partial range means the remainder was not reviewed. Hashing a complete file does not imply its complete reading.

| File | Read extent | SHA-256 |
| --- | --- | --- |
| `handbook/parts/p05/pa-checker-arithmetization.tex` | 1-516, EOF | `33195DFF4BB6D2D7BD898E0AF9D8EC1980A1272593139624AA17577E132C15F5` |
| `handbook/annex/p05/pa-checker-arithmetization.tex` | 1-537, EOF | `03BAF39D646901DC307812B0D22FE8823CFEC53B3D7B85A3FF0ADF754AAF71E5` |
| `handbook/parts/p16/finite-abduction.tex` | 1-340, EOF | `AB9195BA7C823075CAFBF3EAD98EFCC5CB754696F0C42D27EF108A5B9303A5FF` |
| `handbook/annex/p16/finite-abduction.tex` | 1-283, EOF | `35B9C51F77801CBFFC7B372B7DD9BB67FAFC2033E29BE5F29453DB756C8EA2B9` |
| `handbook/parts/p05/standard-pa-proof-predicate.tex` | 1-252, EOF | `71D3E5569BFB7BAE907CA818BE65DBBCE5E48DBA86D9D8942819DCC5110331E2` |
| `handbook/annex/p05/standard-pa-proof-predicate.tex` | 1-315, EOF | `7F3E3F751832ACACFFC8F2383E2AC14A8D8DC7A9DEA2DA4B837F3A9DF648DFDF` |
| `handbook/restoration/inherited-09328-09438.tex` | 1-546, EOF | `A6E37FA592E81B888C14A2DA97CC70F1A05EC69BAE0CE4D36E2E60C59F09C541` |
| `handbook/restoration/inherited-09262-09327.tex` | 1-253, EOF | `B49A3B30AFF36050841D4F384A6BA80FCF36F4661B3C4085E58D2371B4E003CB` |
| `handbook/annex/p05/internal-proof-predicate.tex` | 1-524, EOF | `F11B72E5AE8FF2407C58FA434320D08095C0C543AE8C610237EED42EAFFFA1C1` |
| `handbook/restoration/inherited-03240-03428.tex` | 1-189, EOF | `36D7779D6B9BB3CAF0C4EF514A79A1C7D8AA10BD4A72290256EA1D09D5DB58CC` |
| `handbook/restoration/inherited-03927-04061.tex` | 1-135, EOF | `2AD2846970D4976177B0FBB8AC59FF8106253F5D155A5E4861956F7F651BF480` |
| `handbook/registry/calculi/nd-fol.tex` | 1-29, EOF | `F25549BC18FC4AAE212EEA32CADC9FFFD08E03D712F5DF10E9DA62F660BE5370` |
| `handbook/restoration/inherited-02193-02340.tex` | 1-148, EOF | `5BA27894EDF744D288008B613ADF93EAC3D65385F745135DE776D5B6011316A3` |
| `handbook/restoration/inherited-07678-07752.tex` | 1-75, EOF | `1B3A7277D05F42CD5E568CC12B851F2E460BDBAB4244D11F91F30EFF78AA02DD` |
| `handbook/restoration/inherited-09099-09111.tex` | 1-13, EOF | `38534E090C35DB78D99D045D19B3C7F34F1F1AAA8999CF118C7A416CD41D9D2B` |
| `handbook/restoration/inherited-09175-09187.tex` | 1-13, EOF | `0DB98B87928AA115C82883993E2E25B18286779E7DED0399C7148633C0178430` |
| `handbook/restoration/inherited-01661-01816.tex` | 1-156, EOF | `FB12D36A183AC0FDF5C8B2F8A1BBC09238526FDB03F75364A6DC18239913EC3E` |
| `handbook/restoration/inherited-01817-01898.tex` | 1-82, EOF | `499FEC700936D0625769D7C09AA2BC5FD1F6D976B9EAB1A9CBC8EDFE8CAFB9C4` |
| `handbook/restoration/inherited-08306-08438.tex` | 1-133, EOF | `0B020970BE72999CD771566BA0D6CDB4E4668728362CBD3C0D1606059EE9D2B8` |
| `handbook/restoration/inherited-08439-08709.tex` | 1-137 only; pairing/beta clauses through 87 fully read | `95EB4270559303FEFC5DE2D9BC804A04768EAD87D68D9E5D9CBF65079714806A` |

The two author notes were consulted as leads; their self-assessments supply no independent acceptance evidence. No other current verification report was read.

## Integration read extent and boundaries

The lead's frozen shared hashes were rechecked. The following routes were read completely and put the assigned units and their named direct dependencies in the announced order:

| File | Read extent | SHA-256 |
| --- | --- | --- |
| `handbook/main.tex` | 1-71, EOF | `C4A8F12BF84C6360DA6DA39CF38E42A526E62ADBBF65949C1CA0FCCC77806A74` |
| `handbook/parts/p05.tex` | 1-54, EOF | `6017629C3A54E1E063306659EEC261F5B7831183662F83DC5FFB67B518E5C54E` |
| `handbook/annex/p05-route.tex` | 1-18, EOF | `7CA80013363CA96F4BCC926C4FF33FAEBA47A9B6E3DD1839CCF467E30B813EEE` |
| `handbook/parts/p16.tex` | 1-4, EOF | `B8462255C289FBCA14A9296EE8F7567C524A7ABFAC44FC5BB5F681AA3997C64E` |
| `handbook/annex/p16.tex` | 1-3, EOF | `F60E8A47B426A42C69DFC8D903F308FA7654269A7E8CEFD95FF03B9B85D0883D` |
| `handbook/bib/handbook.bib` | 6598-6606 only, complete new record | `D0AA1C02842E4FF29DD425A8C3FE95F9F12877A06A5DDD841C30C38A3CDDA0F6` |

Route observations are source-reading evidence, not a build result. Shared symbol projection and notation checks are lead-owned and were not run or accepted here. No entire-book source audit, remaining-reference acquisition review, current manuscript PDF inspection, rights review, or formal closure record was supplied by this assignment. The description-selection failure and any unreviewed scope stay open.

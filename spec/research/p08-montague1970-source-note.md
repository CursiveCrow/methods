# Montague 1970 Synthese: source and authoring record

Unit `ED26-REQ-N-b-006-02`, requirement `N-b-006`, allocated
subcomponents `N-b-006-MAP-01` and `N-b-006-MAP-04`. This writer owns
only its body/annex pair, treatment-specific intakes, this source note,
and `source/references/p08-montague1970/`. Root owns shared drivers and
canonical records. Scott and Pacuit have separate authoring seats.

## Exact original acquired and read

Richard Montague, *Pragmatics and Intensional Logic*, **Synthese 22
(1--2), December 1970, pp.68--94**, DOI `10.1007/BF00413599`.
The source is the public faculty-hosted original scan at
<https://homepages.uc.edu/~martinj/History_of_Logic/Modal_%26_Intensional_Logic/Montague%20-%20Pragmatics%20and%20Intensional%20Logic.pdf>.
The primary publisher page was separately read at
<https://link.springer.com/article/10.1007/BF00413599> and matches title,
author, volume, extent, date and DOI. The scanned first page independently
prints the Synthese 22 (1970) 68--94 publication line; the file contains
all consecutive printed pages 68--94, including the original bibliography
and notes. No credentials, payments, or access-control bypass were used.

- PDF: `source/references/p08-montague1970/montague-1970-pragmatics-synthese.pdf`.
- 27 physical pages, 1,520,994 bytes, unencrypted PDF.
- SHA-256: `A4CCF30A97BBDE8124835D08199BFC758A70C7E399B5456B765DBDE9901E0D39`.
- Complete layout extraction: the matching `.reading.txt`, 67,314 bytes,
  SHA-256 `839EA09AB9ACCF92C8713FED7C3E75B67E160E98D2C53F7236A689E74DF581B2`.
- Receipt: `source/references/p08-montague1970/acquisition.json`.
- The shell publisher fetch returned an HTML challenge. Its raw
  `publisher.html` is attempt evidence only, not publisher-body evidence.
  The identity statement above is grounded in the actual publisher page
  read through the web tool and the original scan, not in that challenge.

I read all 27 printed pages, including bibliography and footnotes. Rendered
source pp.79,82,87,89 were inspected under `tmp/pdfs/p08-montague1970/`
to verify concept/relation formulas, description elimination and names,
the extended bound-variable clause, and the predicative fragment. These
are original-page inspections; no manuscript was built or rendered.

Distinct identities retained:

- Same-titled **Dialectica 24(4), pp.277--302**, DOI
  `10.1111/j.1746-8361.1970.tb01220.x`: not read or substituted for this
  exact Synthese allocation; no assertion of complete textual identity.
- **Universal Grammar**, Theoria 36(3), pp.373--398, DOI
  `10.1111/j.1755-2567.1970.tb00434.x`: a different paper, still the
  meaning of canonical key `Montague1970`; that entry was not overwritten.
- The local Partee Montague-grammar manuscript was only identified as a
  secondary holding and was not used for source replacement credit.

## Actual manuscript and component mapping

Body `handbook/parts/p08/presentations/n-b-006-02.tex`, entry
`sec:p08-n-b-006-02`; annex `handbook/annex/p08/n-b-006-02.tex`, section
`sec:annex-p08-n-b-006-02`. Eleven proved body statements have exact
reciprocal `annex:p8.n-b-006.2.*` proof items.

| Original locator | Written content and proof standing |
| --- | --- |
| 68--71 | Context/indices motivation, ordinary language, Definition I, relations versus predicates, zero-place truth values |
| 72--76 | Actual/possible distinction and examples, eight criteria, Definitions II--VII, full indexed extension clauses, well-founded and intension-first recursions, free-variable proof, local consequence |
| 73 | Past/future, relational necessity, progressive-neighborhood example; semantic verification and original illustrative scope |
| 76--81 | Exact restricted type system, variables and typed constants, Definitions VIII--XIII, all twelve extension clauses, full predicate domains, default descriptions, five additional criteria |
| 79 | Individual-concept and constant-relation restrictions, with both directions proved |
| 81--82 | Complete description-elimination construction including failed-uniqueness branch and source unary example; names of properties/relations/propositions and uniqueness proof |
| 82--84 | Forward operator-to-proposition-predicate reduction and full assignment induction; inverse truth-set correspondence and the syntactically restricted reverse reduction; source higher-order boundary |
| 84--86 | Belief iteration and quantifying into contexts, description-free equivalent with verification, seeming type, fallible assent criteria and logical-equivalence objection |
| 86--88 | Extended degrees, all argument-sort data and exact bound-variable function clause, special degree cases, typed reduction and examples, explicit source inexpressibility assertion without invented proof |
| 88--90, note 13 | Exact predicative guard syntax, compactness/noncompactness, countable expression/Godel-numbering restriction, four enumerability claims, Craig/Kaplan/Henkin boundaries and then-open natural axiomatization; cited actual-source standing |
| 90--91 | Rigid-variable referentiality, failure for nonrigid constants and constant universal instantiation; full assignment proof and explicit two-index counterexamples |
| 91--94 | Original historical qualifications, provenance of extended pragmatics and source notes, nonempty-countermodel qualification |
| Allocated MAP-01 | Exact section-of-R_N neighborhood bridge, inverse map and propositional truth-preservation proof; not a substitution of modern definitions for the original construction |
| Allocated MAP-04 | Modern M/C/N closure correspondence, EMC without N, EN failures of M/C/K, theoremhood EMCN/K equivalence and local-consequence distinction; explicitly not attributed as Montague's axiomatization/completeness results |

## Source qualifications and corrections retained

1. Primitive individual quantification ranges over the union U of actuality
   domains, not the index-local A_i. Constants and predicate arguments can
   concern absent individuals. Source existential E restrictions encode
   actualist quantification rather than changing the quantifier domain.
2. Empty interpretations are allowed in source Definition I. Their empty
   assignment universe makes every sentence true and hence supplies no
   countermodel to consequence. Semantic criteria and the modern model
   correspondence requiring actual assignments explicitly use nonempty
   interpretations; the boundary has not been silently normalized away.
3. Ordinary R_N is arbitrary. The primitive Box of intensional logic is
   instead universal over all indices. Treating the latter as the original
   arbitrary neighborhood operator would change the system.
4. Predicate quantification is full over all I-indexed predicates of
   possible individuals. Constant type <0> is unary over propositions;
   it is not the ordinary zero-place constant of empty type sequence.
5. Descriptions bind only predicate variables and choose the empty
   intension when uniqueness fails. The elimination proof keeps this
   second branch and establishes the defined selection formula, instead
   of introducing an unproved helper or partial term.
6. The inverse reduction has the source condition that the resulting
   expression be a pragmatic sentence. No full higher-order-to-first-order
   equivalence or general removal of predicate quantification is claimed.
7. Extended operator variables are bound in formula arguments, and the
   resulting argument is the entire m-place predicate function. The
   seeming example's argument order is tracked by an explicit permutation.
8. Source p.86 declares seeming type <-1,1,-1>; p.88 prints <1,1,-1>
   while applying it to an individual first argument. The reconstruction
   retains the consistent p.86 type and the checked degree <1,2,1>
   translation, rather than propagating the p.88 type slip.
9. Source notes about assent are fallible confirmatory suggestions, not
   logical belief axioms or an established empirical experiment. The
   logical-equivalence problem and proposed distinction of sentential
   belief are retained with their tentative status.
10. Montague's technical metatheory is genuinely sketched/cited in the
    article. The reconstruction does not fabricate a Kaplan axiom system,
    a full Henkin/Craig derivation, or a proof of the extended-language
    inexpressibility assertion. It also retains the historical, not
    current, status of the natural-axiomatization discussion.
11. The modern comparison supplies its own semantic and algebraic proofs,
    explicitly separated from the original. E/M/C/N/regular-completeness
    constructions remain in the Chellas/Pacuit and Scott allocations;
    this unit gives them no duplicate original-source proof credit.

## Author checks, standing, and integration handoff

The source-native construction and the allocated neighborhood/closure
comparisons are authored. I read through the actual saved body and all
annex proofs, checking type/arity data, free-variable dependencies,
description defaults, both translations' hypotheses, empty/nonempty
boundaries, the belief example, the two-index constant countermodels,
and the explicit EN countermodels by direct mathematical reasoning.
This is authoring verification, not independent admission.

The two ownership-specific intakes are
`handbook/bib/intake-p08-montague-intensional.bib` and
`handbook/registry/symbols-intake-p08-montague-intensional.csv`.
Root still needs to merge the new `Montague1970Pragmatics` key and symbols,
route the pair, and reconcile any old lookup citations that wrongly use
`Montague1970` for this article. The latter shared-file correction was
identified but not applied by this writer.

No original-source acquisition gap remains for this allocation. The
source's own externally dependent metatheory and absent full derivations
remain accurately cited boundaries, not supplied proofs. Any separately
allocated full Henkin/Craig/Kaplan or modern completeness proof remains
owed at its own destination. No independent reviews, children, manuscript
builds/renders, or prose tests occurred. Shared records and the preceding
Lyndon return remain untouched.

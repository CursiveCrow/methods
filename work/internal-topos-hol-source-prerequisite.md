# Internal topos HOL: bounded source prerequisite

2 October 2026, 10:30 UTC. Scope: `ED26-REQ-N-d-023-03 / N-d-023-S03-TASK02`, for the active presheaf author. This is source legwork and an interface handoff, not a review or evidence that TASK02 is satisfied/admitted. No active manuscript, calculus sheet, style, queue or canonical record was edited. Owned outputs are this note and `source/references/internal-topos-hol-source/` only. No children, reviewers, builds, manuscript renders or prose tests were run.

## Result

An actual printed, bounded, first-party typed higher-order specification is now available locally: **Lambek–Scott 1980, §1, printed pp.216–218**, together with their distinct **1983 equality-based presentation, §1 pp.493–495 and Appendix I p.503**. These are separate original articles, not the unread 1986 book. They provide a concrete primary rule surface for authoring a declared typed-HOL soundness argument rather than treating equality-free first-order LJ as sufficient.

The strongest immediate choice is the 1980 logical-axiom version, with the nonarithmetic fragment explicitly identified when interpreting an arbitrary elementary topos. A writer must establish its bridge to Mitchell–Bénabou notation and the manuscript interfaces. The earlier arithmetic source's NNO assumption cannot disappear silently. Neither identification nor the existing contextual semantic arguments discharge the complete typed-HOL proof obligation.

## What Mac Lane–Moerdijk actually cites

The actual printed p.302 was read from the pre-existing source image `tmp/pdfs/p10-topos/mlm-logic6-313.png`. It refers rule specification to `[Boileau, Joyal]` or `[Lambek, Scott]` and explicitly limits its own presentation to semantics. It prohibits unrestricted classical indirect proof and choice in a general topos.

1. **André Boileau and André Joyal, “La logique des topos,” Journal of Symbolic Logic 46(1), March 1981, pp.6–16, DOI 10.2307/2273251.** The [publisher record](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/la-logique-des-topos/FAF965F617FE56ADF827C6A1532F71DF) verifies this identity and exposes extract/references, not the technical body. The 2014 online posting is not original publication. Its own introduction distinguishes earlier alternative formalizations; do not collapse their calculi. No qualified held original body was located or acquired here.
2. **Joachim Lambek and Philip J. Scott, Introduction to Higher Order Categorical Logic, Cambridge 1986, Part II.** Stable bibliography key `LambekScott1986` is at `handbook/bib/handbook.bib:3372`. Earlier local notes explicitly leave the exact book body missing. The author's [publication page](https://www.site.uottawa.ca/~phil/papers/) links the book to Cambridge and labels a 1988 manifestation; that does not identify a held 1986 scan. The official index search locates its Leibniz rules at pp.129–130 and internal language at p.143, but index evidence is not source-body evidence. Direct official contents/index requests timed out and were not repeatedly retried. No invented exact book rule numbers or completed book reading is claimed.

## Newly acquired bounded first-party bodies

The URLs were observed on Philip Scott's own University of Ottawa publication page. Source byte identities are recorded separately from derived page images in `source/references/internal-topos-hol-source/acquisition-receipt.json`. Downloads required a sandbox escalation after the granted narrow path still rejected ordinary shell access; the authorized retry succeeded. No login, payment, contact or access-control bypass occurred.

### Lambek–Scott 1980

[Intuitionist Type Theory and the Free Topos](https://www.site.uottawa.ca/~phil/papers/L-S.ITT.and.Free.Topos.pdf), *Journal of Pure and Applied Algebra* 19 (1980), pp.215–257. The first page prints the journal/year/pagination; all 43 physical pages are present. Saved source:

`source/references/internal-topos-hol-source/lambek-scott-1980-type-theory-free-topos-author-scan.pdf`

2,784,080 bytes; SHA-256 `3ADB5D6B2BEE0DEDC18611FD1EC9FCDD6C097F1B5072EFBB6070E190A81ED55F`.

Read for this prerequisite: opening scope and **§1 pp.216–219**; p.216–218 rule displays also visually inspected. Unrelated later free-topos constructions and metatheorems are not credited as read. Exact authoring locators:

| Source locator | Needed interface |
| --- | --- |
| Definition 1.1, p.216 | Pure types generated from `1`, `N`, `Ω`, products and `PA`. |
| Definition 1.2, p.217 | Ten typed term clauses, including membership, comprehension and type-indexed quantifiers. Terms of type `Ω` are formulas. |
| Remarks and structural axioms, p.217 | The named `L1` language; variable-set-indexed entailment; weakening and typed free-for substitution. Equality is Leibniz-defined via all `PA` predicates. |
| Logical axioms (1)–(7), p.218 | Truth/falsity; meet/join/residual adjunctions; universal/existential projection adjunctions. |
| Nonlogical axioms (a)–(c), p.218 | Comprehension, power/proposition extensionality, unit and product assumptions. |
| Nonlogical axioms (d) and Boolean axiom, p.218 | Separate Peano and classical extensions. |
| Variant discussion, p.219 | Original projection-symbol version and comprehension-poor variant are not the same syntax. |

The source contains **no primitive function-type/lambda/application syntax**. That fact determines the required bridge: do not label the larger Mitchell–Bénabou term language as literally this `L1` syntax. Functions can be compared through categorical exponentials or functional relations, but the writer must supply the exact relationship it uses.

### Lambek–Scott 1983

[New Proofs of Some Intuitionistic Principles](https://www.site.uottawa.ca/~phil/papers/Lambek_Scott.NewProofs.Int.pdf), *Zeitschrift für mathematische Logik und Grundlagen der Mathematik* 29 (1983), pp.493–504. Saved source:

`source/references/internal-topos-hol-source/lambek-scott-1983-new-proofs-author-scan.pdf`

634,614 bytes; 12 physical pages; SHA-256 `36A87B51CFD4838F6D111103C3A3883BD266FB27879CEA3FA1C461F4063D610D`.

Read for this prerequisite: **§1 pp.493–495**, **Appendix I p.503**, and terminal identity/reference material. Appendix I was visually inspected because the web text renderer corrupts fractions and symbols. It prints five groups: structural rules; pure equality rules; other logical rules; product rules; Peano rules. Its equality-primitive formulation differs from the 1980 primitive-logical-connective version. The first section defines logical operations from equality, gives interpretation and an applied/internal-language extension; p.495 assumes all source topoi have an NNO.

Do not mix the 1983 primitive equality with the 1980 Leibniz equality while attributing the hybrid to either source. Do not copy the corrupted OCR instead of the actual p.503 display. The 1983 article is a compact alternative rule source, not acquired proof of the 1986 book or Boileau–Joyal 1981.

The author's host permits personal/nonprofit access while withholding blanket redistribution/commercial permission. These public source captures are reading evidence, not a republication licence for protected prose. Independent mathematical exposition and later rights/reproduction gates remain separate.

## Actual registered manuscript interfaces

These were inspected in the current tree, not inferred from file names:

| Existing interface | Usable contribution and exact limitation |
| --- | --- |
| `handbook/registry/calculi/contextual-first-order.tex:2`, `def:p10-contextual-first-order` in `first-order-categorical-semantics.tex:6` | Many-sorted contexts, term-equation/sequent distinction, finite assumptions, logical quantifiers/equality with side conditions. Current signature has first-order term formation, not power abstraction or formulas-as-Ω-terms. |
| `thm:p10-doctrine-substitution`, `thm:p10-doctrine-soundness`; `handbook/parts/p10/first-order-categorical-semantics.tex:150` | Substitution/reindexing and all rules of the specified first-order sheet. Sort objects may be empty. This is not a theorem for a silently enlarged typed-HOL syntax. |
| `contextual-adjoint-first-order.tex`, `contextual-parameter-free-equality.tex` | Exactly stated alternate first-order presentations, with existing interderivability proofs. They do not introduce power types/comprehension. |
| `sheet:stlc`, `cartesian-lambda.tex:14`, `thm:p10-stlc-equational-substitution`, `thm:p10-stlc-ccc-completeness` at line169 | Arrow-only typed terms, capture-avoiding substitution and categorical βη equality. Explicitly no product/unit term constructors, formulas, power types or quantifiers. |
| `def:p10-internal-ccc-language`, `internal-cartesian-language.tex:13` | Named CCC objects/constants and an equational theory; named exponential objects differ from formal arrow types. Not the internal logical language of a topos. |
| `sheet:lj`, `handbook/registry/calculi/lj.tex:4` | Equality-free first-order intuitionistic logical fragment only. |
| `sheet:sol`, `handbook/registry/calculi/sol.tex:7` | Classical translation-defined relational second-order language, object equality and Choice. Its limitations exclude the needed arbitrary-topos intuitionistic typed HOL. |

Pitts's held 18-May-1995 draft is an authentic source for several rows above. Its **p.85** explicitly sends higher-order logic to further reading; it is not a source that already prints the entire power-type calculus. `tmp/acquisition/src030/cambridge-categorical-logic-author.layout.txt` and the [author PDF](https://www.cl.cam.ac.uk/~amp12/papers/catl/catl.pdf) control that qualification.

## What remains to author before a soundness claim

This is the precise dependency, not a proposed new named calculus:

1. **Select and preserve one identified rule presentation.** Declare the source's grammar/judgements/axioms, any explicitly delimited nonarithmetic restriction, and any independently justified definitional extension. A source-specific sheet is a lead-owned integration decision; this investigator has not created one.
2. **Define the complete typed syntax and interpretation.** In particular distinguish source products/power types, the larger exponential/function-term language, formula-valued terms, term equations versus internal equality, parameters and binding/substitution.
3. **Establish the bridges, rather than combine partial results by assertion.** Existing first-order soundness can handle its unchanged logical rules over the declared interpreted objects. Existing CCC results can support unchanged arrow-term βη equations. They do not by themselves establish membership/comprehension, power/proposition/function extensionality, or logical equality's relationship to the diagonal predicate.
4. **Prove every extra source rule/axiom under contextual validity.** The local hypothesis context matters: conditional equality of predicate-valued terms must not be turned into unconditional equality of arrows. For the 1980 version, the diagonal-versus-Leibniz equality bridge is an explicit obligation. For the 1983 version, retain its equality-based logical definitions and justify them rather than borrowing the 1980 connective axioms silently.
5. **Keep the semantic regimes exact.** Arbitrary elementary topoi do not come with an NNO, Boolean law or choice. The source's arithmetic extension requires an NNO; classical claims require their separately stated hypotheses. Sort/context objects may be uninhabited. Ordinary global points are not sufficient tests of all internal sequents.

No source identification, source hash, LJ validation, or collection of separately sound fragments establishes all these steps. TASK02 stays unsatisfied/unadmitted until the actual complete attributed syntax, bridge and rule-by-rule interpretation argument are supplied at the requested scope.

## Acquisition/inspection limits

The two bounded articles were freely retrieved from observed first-party links. Source PDFs were not edited. Only selected source-page images were generated in the exclusively owned source folder, never the manuscript. The exact 1981 paper and 1986 book technical bodies remain unqualified. Publisher metadata/index is kept distinct from readable body. No universal unavailability claim is made. Relevant source passages were read; neither whole unrelated book reading nor whole-article mathematical acceptance is claimed.

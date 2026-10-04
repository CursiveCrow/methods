# N-c-009.a independent manuscript review record

## Admission scope

This record covers only the Schmidt-Schauß--Smolka 1991 source presentation
registered as `N-c-009.a`, together with the immediately linked modern
handbook-owned ALC method and calculus sheet. It does not admit `N-c-009.b` or
`N-c-009.c`, Part IX as a section, any build or rendered page, or the final
handbook.

The unanimously reviewed files are:

| Artifact | SHA-256 |
|---|---|
| `handbook/parts/p09/presentations/n-c-009.tex` | `225674EB760415EF881ED3C63B760798BC7E9CE100DC1911585FB92C7FAFE50E` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `EF91922CDD48236B3A532C0E6F919FF5BF15CFBD1B7F47DE8EE0A070AE876794` |
| `handbook/registry/calculi/tableaux-alc.tex` | `3D4F8CC2EC50D9891974EA5E4E33EAC54DD3C4CEE092CACBC9E99C7B0341D0E6` |
| `spec/research/p09-schmidt-schauss-smolka-1991-source-note.md` | `F85C67DA5AEBC5AB3D2F27DEF97EB02B1657FA876F6183ABF0CB24265BEB5753` |

The primary authority was the complete twenty-six-page author-hosted article
PDF at
`tmp/pdfs/p09-schmidt-schauss-smolka-1991/schmidt-schauss-smolka-1991.pdf`,
SHA-256
`F9DB06CF37EA34159907025C942A5C7D2B177E31D71D497FD0BED68CEF0D14DA`.
All printed and physical locators are one-for-one pages 1--26. The relevant
bibliography file during review was
`handbook/bib/handbook.bib`, SHA-256
`62D62CBD15EFC7D8CFC208406DEEFA9FCC8912422EE4D7FE02B9ED72D4C0DA30`.

## Reviewer runtime and independence

The runtime exposed each canonical reviewer identity and role but did not
expose an exact deployment or build identifier. All three were Codex subagents
inheriting the root's GPT-5-family model. The unavailable exact model build is
recorded here rather than guessed.

Each reviewer was instructed not to inspect another reviewer's output, not to
contact another reviewer, and not to edit the manuscript. Each independently
read the assigned current files and returned its own verdict. Source-PDF
reading and rendering were allowed solely for scholarship. Tests, checkers,
scripts, TeX, the handbook PDF, and builds were prohibited and were not used as
review evidence.

## Source-fidelity review

- Canonical reviewer: `/root/schmidt_smolka_1991_research`.
- Role: complete primary-source fidelity.
- Authority scope: all twenty-six article pages, the frozen source note, and
  the complete current historical presentation.
- Final verdict on the current presentation hash: **ACCEPT**.

The final comprehensive instruction was:

> Review frozen `handbook/parts/p09/presentations/n-c-009.tex` against all 26
> primary pages and the frozen source note. Reassess the general completion
> definition; successor, predecessor, and individual-root definitions; exact
> top-completion ancestry and Proposition 5.7 wording; positive `m <= n`
> prefix typing; and the literal Theorem 4.6 statement with the explicitly
> owed, out-of-scope FL grammar boundary. Inspect the entire current
> presentation for any remaining source mismatch. Do not inspect or contact
> another reviewer, edit, or run tests, checkers, scripts, TeX, the handbook
> PDF, or builds. Return exactly ACCEPT if no substantive revision remains;
> otherwise REVISE with precise primary-source evidence and corrections.

After the two requested page-13 citations were added, the current-hash
confirmation instruction was:

> Verify the two added Theorem 4.6 page-13 locators, verify that no other text
> changed, and inspect enough current context to return exactly ACCEPT if the
> current hash remains source-faithful; otherwise REVISE.

Evidence digest: the reviewer checked the exact ALC grammar and semantics,
derived constructors, all six constraints, every unfolding and completion
rule with side conditions, the general completion definition, model
extraction, traces and Figure 3, all restricted-language propositions, the
typed QBF input and translation, both Lemma 6.2 directions, Theorem 6.3,
source examples, proof-status boundaries, printed defects, and the separation
from later TBox, ABox, tableau, and blocking presentations.

## Subject-matter review

- Canonical reviewer: `/root/p09_math_proof_review`.
- Role: mathematical and proof correctness.
- Authority scope: the complete current presentation, the primary article,
  and the frozen source note.
- Final verdict on the current presentation hash: **ACCEPT**.

The final comprehensive instruction was:

> Recheck the entire presentation after the completion-domain, graph-term,
> top-completion ancestry, prefix-typing, Theorem 4.6 boundary, and
> knowledge-base terminology changes. Verify all types, hypotheses, rule
> conditions, model extraction, QBF semantics and reduction, complexity proof,
> examples, and reconstructed proof steps. Do not inspect or contact another
> reviewer, edit files, or run tests, checkers, scripts, TeX, the handbook PDF,
> or builds. Return exactly ACCEPT if no substantive revision remains;
> otherwise REVISE with precise mathematical findings and corrections.

Before the verdict, the reviewer was instructed to recalculate the final hash,
reread the two added page-13 citations, and base its verdict on the current
file. The reviewer explicitly confirmed the current hash before returning
**ACCEPT**.

Evidence digest: the reviewer checked assignment totality and the singleton
repair, every constraint case in the extracted model, rule-preservation
directions, Theorem 4.5's reconstructed dependencies, trace-space reasoning,
the restricted-language upper bounds, full QBF typing and satisfaction,
prefix/clause translations, both reduction directions, and the complement
argument needed for PSPACE hardness of incoherence and subsumption.

## Adversarial publication review

- Canonical reviewer: `/root/mcnaughton_1966_research`.
- Role: omissions, unsupported additions, terminology, source standing,
  cross-presentation integration, and the user-supplied five-part
  technical-name rule.
- Authority scope: the historical presentation, modern ALC method, calculus
  sheet, source note, `N-c-009.a` ledger entry, and relevant bibliography
  records.
- Final verdict on all current scoped hashes: **ACCEPT**.

The final comprehensive instruction was:

> Review the complete current integration without another reviewer's output.
> Apply the user's five-part technical-name rule strictly. Assess the quoted
> Theorem 4.6: FL appears only as the article's source symbol, its grammar is
> explicitly owed to a prior-source presentation, it is not adopted or used
> downstream. Check all terminology, source standing, graph, branch, rule, and
> blocking consistency, citations, and unsupported synonyms or additions. Do
> not inspect or contact another reviewer, edit, or run tests, checkers,
> scripts, TeX, the handbook PDF, or builds. Return exactly ACCEPT if no
> substantive revision remains; otherwise REVISE with precise findings.

After the two page-13 citations were added, the reviewer verified the current
hash and returned **ACCEPT**.

Evidence digest: this review forced exact definitions of tested concept, GCI,
internalized concept, NNF complement, knowledge base, branch, complete, open,
successor forest, and blocking; separated historical coherence from modern
concept satisfiability; removed unused formula-occurrence marks and a dead
global rule; replaced a one-off consistency synonym; reconciled completion
graph versus generated successor forest; and preserved the 1991, body-open
2003, and summary-level 2017 source standings without collapsing them.

## Revision history and final boundary

Earlier independent passes returned `REVISE` and produced concrete manuscript
repairs. The principal repairs were: exact semantic equivalence and derived
constructors; Proposition 4.4's tree-preservation clause; both restricted
existential rules; Propositions 5.4 and 5.6--5.8; QBF typing, satisfaction,
clause leaves, Figure 4, and complement reduction; the total-assignment defect
and singleton repair; Figure 3's literal `y = x + 1` recursion and deliberate
absence of `xRy`; inherited side conditions on the restricted union rule;
Theorem 4.6's statement, boundary, defect, and locators; and the modern ALC
method's exact input, branch, graph, blocking, and label invariants.

No majority vote was used. Every final reviewer accepted the same current
historical-presentation hash. This establishes the three manuscript-content
review gates for `N-c-009.a` only. `N-c-009.b`, `N-c-009.c`, Part IX admission,
the final one-book publication build, rendered-page inspection, and the user's
final acceptance remain open.

# P18 A2: structured argumentation author handoff

## Owned writing and selected extent

Author block: 2026-09-09 UTC, beginning 00:11:45; local date 2026-09-08.
Ownership covers the new body, matching annex, this note, and the disjoint
primary-source capture. Shared drivers, bibliography, symbols, and existing
argumentation chapters belong to root.

- Body: handbook/parts/p18/structured-argumentation.tex.
- Annex: handbook/annex/p18/structured-argumentation.tex.
- Parent scope: P18 A2 structured argumentation.

The selected presentation is the two-premise-sort ASPIC+ tutorial of Modgil
and Prakken, Section 3's all-finite-argument-trees construction with Section
5's general contrary-function extension. Its complete construction is
supplied: typed rules and names, axioms/ordinary premises, finite trees,
components, both set lifts, both link comparisons, three attack modes,
local preference-sensitive defeat, abstract-semantics translation, formula
queries, and a complete worked graph. The no-strict-rules/no-axioms
consistency case and general structural closure statements receive complete
proofs. This unit does not claim completion of every tutorial instantiation
or of the separate 2013 general consistency theorem.

## Frozen primary source

Authors: Sanjay Modgil and Henry Prakken.
Title: *The ASPIC+ framework for structured argumentation: a tutorial*.
Published article: *Argument & Computation* 5(1), 31–62 (2014).
DOI: 10.1080/19462166.2013.869766.

The actual captured object is the author's 30-page manuscript with the page
header **December 16, 2013 15:7**, not the publisher's 32-page layout.
Its first page retains placeholder journal typesetting fields.
The official author publications page identifies this author PDF with the
2014 published article. The manuscript says its presentation follows
Modgil–Prakken (2013) unless otherwise indicated.

- Official author publications page:
  https://webspace.science.uu.nl/~prakk101/publications.html
- Downloaded source:
  https://webspace.science.uu.nl/~prakk101/pubs/ASPICtutorial.pdf
- Held original:
  source/references/modgil-prakken-aspic-tutorial-2014/ASPICtutorial.pdf
- Bytes: **450763**.
- Pages: **30**.
- SHA-256:
  **CE5E2D81DD4D41366DF1E4C68C3A00FEF1A1D85715B06187DDAB5330967026C6**.
- Acquisition: downloaded directly from the official author-hosted PDF.
  A separate Utrecht repository endpoint returned HTTP 403 to the download
  client; the successful author endpoint required no access circumvention.

The whole author PDF, pages 1–30, was read. Pages 19–28 were reread in
bounded chunks after a larger extraction truncated. Pages 12–13 were also
read as source page images to resolve the preference negation signs and
strict-part formulas. Relevant exact extents:

| Source pages | Selected use |
| --- | --- |
| 1–5 | Presentation identity, framework motivation, abstract interface |
| 5–7 | Definitions 3.2–3.8, typed system, knowledge base, closure, finite trees |
| 7–11 | Definitions 3.10–3.17, three attack modes, local defeat, queries |
| 6–11 | Running Examples 3.7–3.18, all rule consequences and attack targets |
| 11–14 | Definitions 3.19–3.23, Examples 3.22/3.24, both link comparisons |
| 14–20 | Strict-rule choices and the rationality boundary/countermodels |
| 20–26 | Read to identify the distinct scheme and restricted-support variants |
| 26–28 | Nullary facts, Definition 5.1, contrary defeat and well-formedness |
| 28–30 | Scope discussion, conclusion, exact referred bibliography |

The author's correction page was also read:
https://webspace.science.uu.nl/~prakk101/corr.html .
It identifies the corrected 2010 well-formedness condition and the separate
corrected 2013 version. The 2010 four-premise-sort construction has not
been substituted for this selected two-sort tutorial.

## Mathematical conventions and direct corrections

1. The contrary function is denoted C, avoiding the source's overloaded
   negation/bar notation. Every formula still has a contradictory. One-way
   contrary and symmetric contradictory conflicts are distinct.
2. Rules are identifiable objects carrying finite ordered antecedents, rule
   type and consequent. Different rule objects may share those descriptions;
   repeating the same object does not create an additional rule.
   Zero-antecedent strict and defeasible rules are admitted, as
   explicitly discussed on source page 26. The finite-tree coding and the
   empty-union cases are proved.
3. Names form a partial function on defeasible rules. Unnamed rules and
   shared names have explicit behavior.
4. In the last-link definition, premise comparisons use Prem_p, because
   the source priority domain is K_p. Applying that relation to all
   premises, as the displayed source Definition 3.21 does, leaves axiom
   comparisons untyped. The body supplies the typed ordinary-premise
   projection directly.
5. Strict set comparison is the asymmetric part of the displayed weak set
   comparison. The source page 12 claim that one may equivalently replace
   every base weak comparison by its strict part fails for partial
   preorders: equality on {a,b}, with sets {a,b} and {a}, is a complete
   counterexample. The body gives one definition, and the annex proves
   its behavior.
6. Strict argument comparison is likewise the asymmetric part of the
   complete weak argument comparison. Requiring both components of a
   weakest-link conjunction to be strictly smaller is not equivalent:
   equal premise strength with strictly smaller rule strength is a
   counterexample, even for total priorities.
7. The running example retains rule d6: s implies defeasibly not p, and
   therefore includes its argument B4. The source's displayed exhaustive
   argument list omits it. The chapter includes its two structural
   attackers: C3 undermines its ordinary premise, and A1 rebuts its
   defeasible conclusion. Conversely B4 cannot attack the axiom premise A1.
8. D4 uses its actual defeasible rule d5. The strict arrow in a source
   argument-list display is not propagated.
9. All attacks and defeats in the complete example are calculated directly.
   With empty strict preference, the extension is the eight-argument E0.
   With last-link priorities, the unique extension excludes B2,B3,B4;
   with weakest-link priorities it excludes A2,A3,B4,D4. Both ranked
   examples are inconsistent through s and not s.
10. Abstract conflict-freeness uses defeat edges, as in the selected tutorial
    Definition 3.16. A variant that uses structural attacks for
    conflict-freeness is not imported through the footnote referral.
11. The existing manuscript's nonempty-family guard is retained for skeptical
    queries. The tutorial's common-argument formula reading is separated
    from an extensionwise existential-witness reading. The four-argument
    distinction example proves they need not agree. Inclusive credulous
    acceptance is the manuscript query; the tutorial's exclusive terminology
    is obtained by the explicitly stated extra condition.
12. The stronger rationality theorem is not claimed on the basis of an
    informal summary of reasonable preferences. The structural theorems
    have full direct proofs for this construction; flat consistency
    requires the stated asymmetry of strict preference. No unsupported
    claim about every priority lift satisfying the stronger theorem is made.

## Reciprocal proof map

There are **11 body-result/annex-proof pairs**, with the following exact
mapping. These are authored proofs; no independent review or acceptance
status is asserted.

| Body result suffix after thm:p18- | Annex label |
| --- | --- |
| aspic-tree-properties | annex:p18.aspictree |
| aspic-set-properties | annex:p18.aspicsets |
| aspic-locality | annex:p18.aspiclocality |
| aspic-query-distinction | annex:p18.aspicqueries |
| aspic-structural-rationality | annex:p18.aspicclosure |
| aspic-flat-consistency | annex:p18.aspicflat |
| aspic-rationality-boundaries | annex:p18.aspicboundaries |
| aspic-worked-graph | annex:p18.aspicgraph |
| aspic-worked-preferences | annex:p18.aspicpreferences |
| aspic-contrary-example | annex:p18.aspiccontrary |
| aspic-finite-generation | annex:p18.aspicfinite |

The boundary proof contains three full countermodels, including the complete
effect of adding the missing two transpositions in the second model.
The graph proofs enumerate all arguments and every target, then establish
the claimed extensions by forced defense and conflict-freeness.
No conclusion-only quotient is substituted for the finite trees.

## Shared integration intake

Requested bibliography key: **ModgilPrakken2014ASPICTutorial**.
The canonical handbook/bib/handbook.bib had no Modgil/Prakken/ASPIC entry
when checked during this author block. Root was sent the identity and hash.
Use the article's verified publication metadata and record the captured
2013-12-16 author-version qualification in its note.

Route the body and annex after the existing abstract argumentation
foundation, as P18 A2. Their chapter/section labels are
sec:p18-structured-argumentation and
sec:annex-p18-structured-argumentation.
Existing interfaces used:
def:p18-extension-semantics, def:p18-arbitrary-framework,
def:p18-acceptance-queries, and the already proved abstract extension
relations and finite methods.

Local notation intake:
L, C, R_s, R_d, n, K_n, K_p, the argument set mathcal A,
ant, head, Conc, Prem, Prem_p, Sub, Top, Def, Last,
the premise/rule preorders and their strict parts,
elitist/democratic finite-set comparisons,
last-link/weakest-link comparisons and strict parts, D, F_AS,
Conc(E), Cl_s, and the bounded dependency rank.
All notation is defined before its mathematical use in the body.
The displayed rules are object data in the structured system, not new
editorial inference-rule macros or additions to shared calculus registries.

## Exact next obligations

The next historical proof target is the full general consistency theorem
in Modgil–Prakken, *A general account of argumentation with preferences*,
Artificial Intelligence 195 (2013), 361–397, together with the author's
identified corrected version dated March 1, 2018. Before using it, select
and capture the exact version, state its technical reasonable-order
conditions, strict-rule contraposition/transposition regime,
axiom-consistency and general-contrary well-formedness conditions, and
prove the full source chain. The author page identifies original and
corrected files; neither full proof has been acquired for this unit.

Separately owed are the exact equivalences for consistent/minimal-support
classical and Tarskian instantiations, the ABA translation and its domain
conditions, and the detailed perception/memory/testimony and normality
models if these presentations are selected for later A2 completion.
Their definitions cannot simply be spliced into the current unrestricted
argument-tree theorem.

Research and PDF skills were used for primary reading and durable provenance.
The complete body, complete annex, and complete note were read back once
after the writing batch. The final edits make rule identity explicit,
use the appropriate alignment environment for the component equations,
specify the finite-rank integer domain, and state the empty default premise
sets in the countermodels.
No independent reviewers, scanners, tests, builds, or manuscript PDF
inspections were requested or run.

# N-c-011 independent manuscript review record

## Admission scope

This record closes the reader-facing source reconstruction and three
manuscript-content review gates for exactly `N-c-011.a`, Klaus Schild's 1991
presentation of the correspondence between the displayed
\(\mathcal{ALC}\) concept language and normal multimodal
\(\mathbf K_{(m)}\).  Its scope includes the source's §3 grammar, semantics,
examples, Lemma 1, Theorem 1, Propositions 1--2, the following
quadratic-space sentence, and the handbook's explicit boundary against the
different role and terminological constructions in §§4--4.2.

It does not admit those later TSL constructions, the unacquired 2017
arbitrary-TBox presentation recorded under `N-c-010.c`, Part IX as a section,
any build or rendered page, or the final handbook.

All three final reviewers accepted the following exact snapshot:

| Artifact | SHA-256 |
|---|---|
| `handbook/parts/p09/presentations/n-c-011.tex` | `65074DDAC085273EC21BC8E8CA5B8928450EEF064E6446D21BE82F41890C7D91` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394` |
| `handbook/bib/handbook.bib` | `AC811C3E21F76830822D4A78B3786AC2D36660BB919F6C5FEC16217BD663D8E2` |
| `spec/research/p09-source-presentations-lot2-3.md` | `C9B412E1D3B55D6CB33442C1A5D2052CACE04A7B6226C45932CFB336BBF47E6E` |

The ledger hash is the pre-admission snapshot read by all three reviewers.
Its subsequent status-only change records their unanimous verdict and links
this review record; it does not alter reader-facing mathematics or a source
claim.

## Primary authority surface

The primary authority was the complete official six-page IJCAI scan at
`tmp/pdfs/p09-schild/schild-1991.pdf`, SHA-256
`671F9BA860DB84214BDC949E94C24B6113C9D2520974765E61DC80962C7B94D6`.
Every final reviewer visually read all six pages, printed pp. 466--471, rather
than stopping after the local §3 result.  Reading the later pages was necessary
to verify that the manuscript's exclusion boundary did not falsely describe
the entire paper.

The assigned 2017 Baader--Horrocks--Lutz--Sattler complexity chapter body was
not treated as an inspected authority.  The overview card, comparison table,
and complexity atlas consistently withhold the exact arbitrary-TBox/ABox
classification until that source presentation is acquired and reviewed.

## Reviewer runtime and independence

The runtime exposed each canonical reviewer identity and role but not an exact
deployment or build identifier.  All three were Codex subagents inheriting the
root's GPT-5-family model; the unavailable exact build is recorded as
unavailable rather than guessed.

Each reviewer was instructed to read the complete frozen scope and primary
authority, not to inspect or seek another reviewer's output, not to contact
another reviewer, and not to edit any file.  Source-PDF rendering and visual
reading were allowed only as scholarship.  Tests, automated checkers,
repository scripts, TeX, handbook-PDF inspection, and builds were prohibited
and were not used as review evidence.

## Source-fidelity review

- Canonical reviewer: `/root/schmidt_smolka_1991_research`.
- Role: complete primary-source fidelity.
- Authority scope: all six official source pages, the complete presentation,
  every relevant overview/card/comparison/atlas surface, bibliography, and
  evidentiary ledger.
- Final verdict on the accepted snapshot: **ACCEPT**.

The final instruction required a complete rereading with special attention to
the exactly typed Proposition 1 reconstruction and the repaired consistency of
all general-TBox/ABox complexity surfaces, followed by reconfirmation of every
earlier fidelity dimension.

Evidence digest: the reviewer confirmed the literal §3 grammar with only
\(R::=r\), the source's domain \(D\) and extension function \(\mathcal E\),
the handbook's disclosed replacement by \(I\), \(\Delta^I\), and
\((\cdot)^I\), the empty-domain and empty-world conventions, all semantic
clauses, both translations, examples, exact theorem strengths, proof and
referral ownership, locators, and the separation from OWL and §§4--4.2.  The
reviewer also confirmed that \(\mathsf{EqAx}_{\mathcal{ALC}}\) is an exact set
of ordered pairs and that the displayed consequence relation is explicitly a
handbook reconstruction rather than notation attributed to Schild.

## Subject-matter review

- Canonical reviewer: `/root/p09_math_proof_review`.
- Role: mathematical and proof correctness.
- Authority scope: the complete accepted snapshot and every source page needed
  by a definition, semantic clause, example, reduction, or complexity claim.
- Final verdict on the accepted snapshot: **ACCEPT**.

The final instruction required a proof-level check of the new equational
definition and the corrected general-TBox/ABox boundary, followed by a fresh
check of the whole mathematical chain.

Evidence digest: the reviewer verified that the Boolean and value-restriction
generators are exactly typed ordered pairs; that the class of compatible
equivalence relations containing them is nonempty; that intersection supplies
the least such relation; and that full substitution invariance follows because
the generator set already contains every substitution instance.  The reviewer
separately verified the independence of Boolean-algebra validity from
\(\mathcal{ALC}\)-semantic equivalence, the soundness direction through each
interpretation's extension kernel, and the correct attribution of the converse
to Schild's Lemmon referral.  The review also reconfirmed both typed model
constructions, the structural induction, coherence and subsumption
consequences, the two-world evaluation, all three Lemma 1 reductions, both
PSPACE directions under the stated log-space convention, and the separate
quadratic-space transfer.

## Adversarial publication and AGENTS review

- Canonical reviewer: `/root/mcnaughton_1966_research`.
- Role: omissions, unsupported additions, terminology, source standing,
  cross-presentation integration, and the supplied five-part technical-name
  rule.
- Authority scope: the complete accepted snapshot, all six source pages,
  bibliography identities, every relevant overview surface, and the open 2017
  boundary.
- Final verdict on the accepted snapshot: **ACCEPT**.

The final instruction required an exact recheck of the two defects found in the
preceding adversarial round and then a complete adversarial rereview without
access to another reviewer's conclusion.

Evidence digest: the reviewer confirmed that the equation-generator name now
has necessity, exact definition, metalinguistic standing, nonredundancy, and
immediate downstream use at one location; that its members are ordered pairs
rather than unspecified equation objects; that the generated relation is
unique; and that the source/handbook boundary precedes the displayed
biconditional.  The reviewer also confirmed that the overview no longer both
withholds and asserts the arbitrary-TBox classification, and reconfirmed the
grammar, notation, model maps, examples, proof status, local correspondence
scope, later-TSL boundary, OWL nonidentity, locators, bibliography, and ledger.

## Revision history and final boundary

Five independent review-and-repair rounds were required; no majority vote was
used.

1. The opening round exposed incomplete handling of the source's empty-set
   convention, modal notions and abbreviations, overloaded atomic names,
   inverse syntactic and semantic maps, source-omitted proof ownership, both
   examples, the finite/canonical-model observation, Lemma 1, Proposition 1,
   the boundary between Proposition 2 and the following quadratic-space
   sentence, and the difference between local §3, OWL, and later TSL material.
2. In the second round source fidelity accepted, while mathematics required a
   definition of modal disjunction and the adversarial review required exact
   validity notation, Schild's log-space completeness convention and inverse
   translation, a generated equational consequence relation, standalone
   concept satisfiability, the separate source role production, a complete
   two-world model, and §§4--4.2 locators.
3. In the third round the reviewers found a leaked §4 role metavariable, an
   undisclosed normalization of Schild's \(D,\mathcal E\) semantics, collision
   between that source notation and the handbook's equation notation, and two
   overview sentences that excluded TBoxes but not ABoxes.
4. In the fourth round source fidelity and mathematics accepted, while the
   adversarial review found that “contains” gave only a lower bound for the
   equation-generator set and that the complexity atlas asserted the same
   arbitrary-TBox result the system card declared unacquired.
5. After the generator set was defined exactly as ordered pairs, the displayed
   consequence was labelled as a handbook reconstruction, and the atlas claim
   was withheld, all three reviewers independently returned **ACCEPT** on the
   exact snapshot above.

This establishes the three manuscript-content review gates only for
`N-c-011.a`.  It does not fulfill `N-c-010.c`, admit Part IX, establish a
publication build or rendered-page result, or constitute final user
acceptance.  Those gates remain open, and the one handbook build remains
reserved until all fourteen parts are text-frozen.

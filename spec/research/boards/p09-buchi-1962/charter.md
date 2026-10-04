# Board charter: Büchi 1962 controlling presentation

- Artifact: the frozen six-object manuscript/source snapshot below.
- Purpose: determine whether the handbook's N-c-013.a presentation of
  J. Richard Büchi's 1962 article is source-faithful, mathematically correct,
  definition-before-use compliant, and fit for graduate-handbook publication
  at the manuscript-content level.
- Mode: review.
- Requested by: the user's standing requirement that every completed handbook
  topic receive three independent blind scholarly reviews before admission.
- Authorship disclosure: chair-authored reconstruction. The chair acquired and
  visually read the complete source, wrote the current reader and source
  records, and supplied the explicitly labelled modern comparison. No seated
  reviewer authored a frozen artifact.
- Severity taxonomy: blocker, must-fix, should-fix, consider, discard,
  unresolved-user.
- Source rule: every finding must cite an exact manuscript line and printed
  source page. The rendered source pages, not extracted text, control formulas,
  symbols, pagination, and printed wording.
- Consensus rule: admission requires every mandate to end with no unresolved
  blocker or must-fix and to file ACCEPT on one unchanged frozen snapshot.
  Supported findings cannot be outvoted.
- Board type: live.
- Workspace: spec/research/boards/p09-buchi-1962/.

## Frozen round-one snapshot

No frozen artifact may be edited while the round is open. Any content edit
invalidates all verdicts and requires a new hash-pinned blind round.

| Artifact | Review scope | SHA-256 |
|---|---|---|
| tmp/pdfs/p09-buchi-1962/logic-methodology-philosophy-science-pageplace-preview-includes-buchi-pp1-11.pdf | complete acquired preview; printed Büchi pp. 1--11 are file pp. 12--22, with controlling front matter and boundary page | D37929230CD874D9B6E91CDDE50DD57EAF51D625BC7575878853E4018B64E089 |
| handbook/parts/p09/presentations/n-c-013.tex | lines 375--760, from Büchi's 1962 decision method through its proof/source boundary | F674BDB103A3B07DEE5925A1D7F3880D92DA31C6442196FB075B2FA85F4ADD24 |
| handbook/parts/p09/logic-in-computer-science.tex | lines 817--828, shared Büchi decision theorem | 2778CAA3D0EB741A78B9D2EA44BD157E5FCCB4E2F3034ED539D52A9788287A1B |
| handbook/bib/handbook.bib | lines 2276--2288, Büchi 1962 record | 748B159ED5CE40855878D3E8492DA98D0A465B73C68830E5BE11165EFF2ACA6A |
| spec/research/p09-buchi-1962-source-acquisition.md | complete lines 1--541 | 90C23E094604342726B02EC78FE1A4211D56233A063532E8EDA94537676C434B |
| spec/research/p09-source-presentations-lot2-3.md | lines 556--569, compact N-c-013.a presentation, plus removal from the open-acquisition list and addition to the sufficient-body ledger | EBC0E39AF016B22F1BA52D7DEEB620DE6B00F5B48AA1F3E0687BB10BBC316508 |

The visual reading aids are:

- frontmatter-page-04.png and frontmatter-page-05.png;
- contents-page-8.png;
- buchi-1962-page-12.png through buchi-1962-page-22.png; and
- boundary-page-23.png,

all under tmp/pdfs/p09-buchi-1962/. The PDF remains the frozen source identity.

## Invariants

- I1: The complete 1962 article text in the later Stanford printing is the
  controlling authority. The 1966 Elsevier series republication and 1990
  Springer collected-works reprint are later versions with their own
  identifiers; their DOIs are not original-paper DOIs.
- I2: Every printed article page, relevant front-matter page, and the boundary
  page must be visually read. Text extraction alone cannot establish a symbol,
  formula, page boundary, or printed discrepancy.
- I3: Büchi's historical name \(SC\) and modern S1S may be related but not
  silently identified as source wording. \(SC\) names an interpreted
  formalism, not an automaton or language class.
- I4: Source definition, source theorem, source-reported comparison,
  handbook-owned reconstruction, and modern handbook corollary must remain
  visibly distinct.
- I5: The modern finite-data comparison
  \(\Gamma,Q,Q_0,\Delta,F\) is eliminable and handbook-owned. It may be proved
  extensionally exact but may not be attributed as a tuple or terminology
  printed by the article.
- I6: Formula classes and their denotations must not be confused.
  \(\Sigma_n,\Pi_n,\Sigma_1^\omega,\Sigma^0\), and the printed
  \(\Sigma_2^0\) comparison require their exact standing and disclosed
  notation limits.
- I7: Multiperiodic finite-word languages are not ultimately periodic
  infinite words or predicate sets. Every new or historical technical name
  requires necessity, definition or disclosed source limitation, standing,
  nonredundancy, and actual use.
- I8: Cited, referred, outlined, and printed proofs must remain separate.
  Familiar later automata results cannot fill a proof the source credits or
  omits.
- I9: Theorem 2 establishes effective decidability, not a modern elementary,
  PSPACE, optimal, or translation-state-complexity bound.
- I10: The article supplies no worked circuit example. Its motivating
  verification and open synthesis questions may not be rewritten as a
  fabricated case study or solved synthesis theorem.
- I11: The proposed axiom schema is not a proved complete axiomatization.
  Source-reported historical consequences and the Gödel-attributed
  monadic-function claim are not new proofs by the article.
- I12: The printed \(\mathrm{Nn}\) discrepancy must remain visible: p. 1 says
  natural numbers, whereas p. 10's ordered glossary says integers.
- I13: Public preview access is not an open-content licence. The source object
  is a research copy and the handbook independently reconstructs its content.
- I14: Acceptance is limited to N-c-013.a. It does not admit N-c-013 overall,
  Part IX, another part, a rendered artifact, human review, book completion, or
  user acceptance.
- I15: This is book scholarship, not software engineering. No test, test
  harness, automated checker, repository script, TeX command, interim handbook
  build, or handbook-PDF inspection may be used or claimed. Permitted evidence
  is source-page visual reading, direct manuscript reading, mathematical proof,
  citation/provenance inspection, and SHA-256 labels for snapshot identity.
- I16: Opening seats are blind. They may not read the ledger, chair transcript,
  any earlier Part IX board transcript, another current transcript, or another
  verdict, and may not contact one another.

## Mandatory coverage points

- M01: recompute all six frozen hashes before substantive review.
- M02: visually read the source front matter, contents, printed pp. 1--11, and
  the first page of the next article; confirm the complete page map.
- M03: verify author, title, editors, proceedings title, publisher, location,
  year, pp. 1--11, later-printing status, later DOI separation, access route,
  and rights boundary.
- M04: verify the exact \(SC\) individual and monadic domains, vocabulary,
  quantifiers, and standing.
- M05: verify the assignment-to-infinite-truth-value-word encoding, including
  the indicator definition and the absence of a distinct source run at that
  stage.
- M06: verify the literal \(\Sigma_1,\Pi_1,\Sigma_{n+1},\Pi_{n+1}\) clauses,
  the infinitely-often quantifier, and \(\Sigma_1^\omega\).
- M07: independently prove the handbook's \(\Gamma,Q,Q_0,\Delta,F\)
  translation in both directions and verify the permitted-initial-set versus
  single-initial-state boundary.
- M08: verify \(\Sigma^0\), finite interval standing, and the source's
  formula/denotation overload.
- M09: verify two-sided congruence, finite rank, multiperiodicity, and the
  distinction from ultimately periodic sets.
- M10: verify the Sequential Lemma's exact quantifiers and its printed Ramsey
  coloring proof.
- M11: verify Lemmas 2--6, endpoint-output behavior, Boolean/quantifier
  reductions, and every credited or referred proof dependency.
- M12: verify Lemmas 7--9, conjunction control, complement congruence, the
  \(2^{2m^2}\) rank bound, homogeneous-block argument, and the explicit
  non-determinization boundary.
- M13: verify Lemma 10's finite-union stem/repeated-block form and whether
  repeated blocks must be nonempty.
- M14: verify Lemma 11, Theorem 1, the \(\Sigma_1^\omega/\Sigma_2\) collapse,
  free-individual extension, and finite-set consequence at the source's exact
  proof strength.
- M15: independently prove both directions of the handbook-owned equivalence
  between \(SC\)-definable truth-value-word languages and nondeterministic
  Büchi-recognizable languages; verify that the source does not use the modern
  tuple or theorem name.
- M16: verify Lemma 12's initial path, recurrent state, nonempty return cycle,
  \(2^k\) bound, converse periodic construction, and finite enumeration.
- M17: verify the remaining effectivity argument and Theorem 2 without
  importing a modern complexity claim.
- M18: verify all five post-Theorem-2 consequences and comparisons, including
  \(SC_{\mathrm{fin}}\), \([\mathrm{Nn},+,\mathrm{Pw}]\), and the disclosed
  standing problem for the printed \(\Sigma_2^0\) notation.
- M19: verify the proposed axiom-schema claim and its lack of a printed
  completeness proof.
- M20: verify the exact ultimately periodic-set definition, standing of
  \(SC_{\mathrm{per}}\), Theorem 3, and the finite-semigroup outline.
- M21: verify Theorem 4, binary-expansion route, all symbol glosses, and the
  \(\mathrm{Nn}\) discrepancy.
- M22: verify the \(2x\) undecidability report, Gödel-attributed monadic-function
  report, and proof/attribution limits.
- M23: verify all three open problems, the definitions of \(SC^2\) and
  \(SC(\alpha)\), and the verification-versus-synthesis distinction.
- M24: reconcile the reader, shared theorem, bibliography, complete source
  note, compact record, open-acquisition ledger, and sufficient-body ledger.
- M25: apply the full AGENTS terminology rule, rights boundary, topic-only
  scope, and explicit no-test/no-build boundary.

## Roster and role cards

### Source fidelity and evidence seat

- Mandate: determine whether every manuscript and record claim is supported at
  its stated strength by the complete primary article.
- Coverage: M01--M14 and M17--M25, with special attention to literal formulae,
  locators, version history, bibliography, proof ownership, historical
  attributions, and rights.
- Evidence: printed page plus exact manuscript line for every finding.
- Blind spot to avoid: accepting a correct modern paraphrase as source wording
  or treating a disclosed source ambiguity as a handbook error.

### Mathematical and proof-correctness seat

- Mandate: independently rederive every formula translation, congruence
  argument, closure result, normal-form implication, and finite decision
  argument used by the manuscript.
- Coverage: M04--M23, especially M07, M10--M17, and edge cases involving empty
  initial sets, unused binary state codes, nonempty cycles, and quantifier
  polarity.
- Evidence: explicit derivation or minimal counterexample tied to source and
  manuscript locations.
- Blind spot to avoid: accepting a familiar Büchi theorem without checking the
  source's actual recurrence form and proof dependencies.

### Adversarial publication and terminology seat

- Mandate: determine whether a hostile expert reader could expose ambiguity,
  source laundering, invented terminology, definition-after-use, silent
  version conflation, scope inflation, or premature completion language.
- Coverage: M01--M25, emphasizing I3--I16 and the AGENTS terminology rule.
- Evidence: exact location, violated invariant, concrete reader harm, and the
  smallest exact correction.
- Blind spot to avoid: aesthetic preference, speculative expansion, or
  demanding a modern result the historical presentation does not need.

Agents and models are recorded by the chair after spawning. No seat is shown
another seat's identity or output during the blind opening.

## Opening-round filing rule

Each seat writes only its assigned file under transcript/ and ends with:

- VERDICT: ACCEPT if no blocker or must-fix remains for its mandate; or
- VERDICT: REJECT followed by the exact blocking finding identifiers.

Every coverage point must be marked checked-clean, finding-linked, or
not-checked with reason. A reviewer may not edit any frozen artifact, ledger,
chair record, or another transcript.

# Board charter: N-c-012.b Pnueli 1977

- Artifact: `handbook/parts/p09/presentations/n-c-012.tex`, lines 370--618 and 1023--1027; its shared Part IX surfaces; `spec/research/p09-pnueli-1977-source-note.md`; `spec/research/p09-source-presentations-lot2-3.md`, lines 151--161; and `handbook/bib/handbook.bib`, entry `Pnueli1977`.
- Authority: the complete author-hosted printed body, pp. 46--57, preserved as `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz`; `focs77.ps` is its lossless decompression, and `focs77.pdf` plus `page-02.png` through `page-13.png` are local scholarly renders for visual reading only.
- Purpose: determine whether the frozen N-c-012.b reader presentation is source-faithful, mathematically correct, complete for its stated scope, publication-ready as prose, and compliant with the user's terminology rule.
- Mode: audit.
- Requested by: the governing handbook objective requires three independent reviews of every reader-facing topic before internal topic closure.
- Authorship disclosure: the manuscript and source note were drafted in the main `/root` thread; no seated reviewer authored this frozen presentation.
- Invariants:
  - I1: This is a book-writing workflow. Review uses source reading and scholarly reasoning only: no tests, automated checkers, repository scripts, TeX, handbook-PDF inspection, or builds.
  - I2: Review only the exact frozen hashes listed below. A mismatch invalidates the review.
  - I3: Every source claim must be checked against all twelve printed pages 46--57, not OCR or a partial excerpt.
  - I4: Definitions precede use; types, quantifiers, rule premises, side conditions, theorem strength, proof status, and external-proof boundaries must be exact.
  - I5: The printed strict temporal-implication clause, ER axiom A2, inclusive `F`, and Theorem 3 representation must remain visibly distinct; the source's tension may not be silently repaired.
  - I6: No later `X/U` grammar, Buchi translation, safety/liveness syntax, or PSPACE classification may be retrojected into Pnueli 1977.
  - I7: Any new technical name must locally supply necessity, exact eliminable definition or axiom, standing, nonredundancy, and actual later use; otherwise the text must state an owed artifact without naming a hypothetical answer.
  - I8: The author-hosted body may close body-level mathematical reconstruction, but the absent IEEE-direct comparison remains explicitly open.
  - I9: No majority vote. All three seats must independently accept the same repaired frozen snapshot; any failure or uncertainty keeps N-c-012.b open.
  - I10: Acceptance closes only N-c-012.b topic review. It does not admit N-c-012 as a whole, Part IX, any ledger-wide gate, a build, a visual audit of the handbook, human review, or user acceptance.
- Criteria:
  - C1: exact source identity, provenance, page map, rights language, and version boundary;
  - C2: complete program model, executions, atomicity, fairness, and specification hierarchy;
  - C3: exact invariance, ranking, ER axioms/rules, side conditions, Theorem 1, and completeness-sketch assumptions;
  - C4: exact sequential and concurrent applications and their claimed scope;
  - C5: exact future-only syntax/semantics, pure and system-dependent proof systems, quantifier treatment, generalization restrictions, and Theorems 2--3;
  - C6: exact finite-state fairness, Theorems 4--5, proof-system extensions, SCC route, and Appendix B proof boundaries;
  - C7: consistency across the manuscript, source note, ledger, bibliography, and shared Part IX surfaces;
  - C8: independently worded exposition, definitions before use, and compliance with I5--I10.
- Severity taxonomy: blocker, must-fix, should-fix, consider, discard, unresolved-user.
- Source rule: artifact claims cite exact file lines and printed source pages; claims about the authority cite a visually inspected printed page. Unverified claims cannot support acceptance.
- Consensus rule: the user's unanimous independent-acceptance rule supersedes rough-consensus voting. One blind opening round is sufficient only if every seat files exhaustive checked-clean coverage and `ACCEPT`; otherwise repair and a fresh blind round on new hashes are required. Deliberation is used only to resolve genuinely conflicting evidence, never to outvote a defect.
- Round budget: opening round plus at most two focused evidence rounds before repair or escalation.
- Roster:
  - source-fidelity seat: `/root/schmidt_smolka_1991_research`; exact authority correspondence and provenance.
  - mathematical/proof seat: `/root/p09_math_proof_review`; definitions, semantics, proof systems, theorem strength, and proof boundaries.
  - adversarial publication/AGENTS seat: `/root/mcnaughton_1966_research`; omissions, unsupported additions, integration, terminology, and publication risk.
- Model/version record: each seat must state the runtime model/version if exposed; otherwise it must state that the harness did not expose it. The stable agent identifier above is mandatory.
- Board type: live.
- Workspace: `spec/research/boards/p09-n-c-012b`.

## Frozen SHA-256 snapshot

- `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz`: `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB`
- `tmp/pdfs/p09-pnueli-1977/focs77.ps`: `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F`
- `tmp/pdfs/p09-pnueli-1977/focs77.pdf`: `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972`
- `handbook/parts/p09/presentations/n-c-012.tex`: `0DADDC029C1ED7574B14BA6A48ACEBE712F93A125AD7641747E336FAE2788C19`
- `handbook/parts/p09/logic-in-computer-science.tex`: `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394`
- `handbook/bib/handbook.bib`: `AC811C3E21F76830822D4A78B3786AC2D36660BB919F6C5FEC16217BD663D8E2`
- `spec/research/p09-pnueli-1977-source-note.md`: `539E0CEBE721A1F75D87223C41E6DEA2F139543E86EEF016750E56D169DE2D16`
- `spec/research/p09-source-presentations-lot2-3.md`: `C3ACAF3670EF0BCDB58C67138FBA68565817814F19307DF5E25F329D093D2A35`

## Round-two repaired snapshot

Round one returned three `REVISE` verdicts. The original snapshot above and
its transcripts remain immutable evidence. Round two is a fresh blind review
of the following replacement snapshot; acceptance, if unanimous, applies only
to these exact hashes.

- Reader-presentation scope:
  `handbook/parts/p09/presentations/n-c-012.tex`, lines 370--902 and
  1307--1313.
- Source-presentation-ledger scope:
  `spec/research/p09-source-presentations-lot2-3.md`, lines 151--164.
- The full source note, the complete `Pnueli1977` bibliography entry, and the
  relevant shared Part IX definitions and integration surface remain in scope.
- No round-two seat may inspect `ledger.md`, `transcript/chair.md`, any
  round-one transcript, or any other seat's round-two transcript before filing
  its own verdict.

### Round-two SHA-256 identities

- `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz`: `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB`
- `tmp/pdfs/p09-pnueli-1977/focs77.ps`: `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F`
- `tmp/pdfs/p09-pnueli-1977/focs77.pdf`: `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972`
- `handbook/parts/p09/presentations/n-c-012.tex`: `83C56ED3E9A17246150C727DCBCA4418F185FB166AA7AF6201D353CDF4467C07`
- `handbook/parts/p09/logic-in-computer-science.tex`: `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394`
- `handbook/bib/handbook.bib`: `757EBA2102F6D2A1A31299FB990C6D30718BBAE2EA213114AD75C4038463BF60`
- `spec/research/p09-pnueli-1977-source-note.md`: `9BE7FC420BF1987191517960D4209A435B812F828C9A28476E94EBCA96904518`
- `spec/research/p09-source-presentations-lot2-3.md`: `D920A431C50518FD6F976AAC5A98C4826270ED3BA8898D7CC73A60231FE92F5B`

The round-two source question at printed p. 53 is literal: visually determine
whether the action-tail quantifier uses `j>=i` or `j>i`; do not inherit either
the chair's or another reviewer's reading. Every other charter criterion and
invariant continues unchanged.

## Round-three repaired snapshot

Round two also returned three `REVISE` verdicts. The two earlier frozen
snapshots and all six earlier transcripts remain immutable evidence. Round
three is a new blind review of the replacement snapshot below. A verdict
applies only to these exact identities.

- Reader-presentation scope:
  `handbook/parts/p09/presentations/n-c-012.tex`, lines 370--1048 and
  1453--1460.
- Shared integration scope:
  `handbook/parts/p09/logic-in-computer-science.tex`, lines 599--823.
- Source-presentation-ledger scope:
  `spec/research/p09-source-presentations-lot2-3.md`, lines 151--167.
- Evidence and bibliography scope: the complete
  `spec/research/p09-pnueli-1977-source-note.md`; bibliography entries
  `Pnueli1977`, `McNaughton1966`, and `Landweber1969`; and enough adjacent
  presentation text to detect source, notation, or version conflation.
- Authority scope: the wrapper for provenance only and every printed body page
  46--57 for substantive source review. Images control over OCR or memory.
- Independence rule: no round-three seat may inspect `ledger.md`,
  `transcript/chair.md`, any round-one or round-two transcript, or any other
  seat's round-three transcript before filing its own verdict. A seat may edit
  only its assigned round-three transcript.
- Method rule: source reading and scholarly reasoning only. No tests, test
  harnesses, automated checkers, repository scripts, TeX, handbook-PDF
  inspection, or builds.

### Round-three SHA-256 identities

- `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz`: `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB`
- `tmp/pdfs/p09-pnueli-1977/focs77.ps`: `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F`
- `tmp/pdfs/p09-pnueli-1977/focs77.pdf`: `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972`
- `handbook/parts/p09/presentations/n-c-012.tex`: `80F9D4B96FEEBD329F683D5048E31544EDD4A97B3922752AC3D17DAB851D9219`
- `handbook/parts/p09/logic-in-computer-science.tex`: `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394`
- `handbook/bib/handbook.bib`: `74F102209EEFB17C63FB5B41B6D257184064BFCFF52CF625BC7A1A61C443B3D9`
- `spec/research/p09-pnueli-1977-source-note.md`: `BC88DE02A62B27112B723548D1483D2E8525CFB0EF175273DE4D15A3EAAB5BBF`
- `spec/research/p09-source-presentations-lot2-3.md`: `5FF3CCC5C8B88882D9218BB4221AEFAEB313EFF15657BCDB427C25F9F6852714`

### Round-three mandatory fresh checks

Each seat must independently verify every charter criterion C1--C8 and every
invariant I1--I10. In particular, without presuming that a proposed repair is
correct, it must check:

- the physical/printed page map, exact locators, rights and version boundary;
- the typed sequential and concurrent transition models, reflexive
  reachability, clean execution, and the two distinct fairness formulations;
- literal P2, its disclosed zero-rank typing repair and strict-future
  counterexample; ER, metarule I, Theorem 1's expressiveness and pointwise
  finite-branching assumptions, and the deadlock-vacuity proof gap;
- location-indexed sequential attachment, typed partial attachment, and every
  step of the positive-capacity producer--consumer invariant calculation;
- recursive inclusive F/G semantics, the initial-state present, G1--G3,
  F2--F3, Q1--Q4 with unresolved schema range, RG's restriction, the exact
  action partition and `j>=i` tail, I1/I2/E/N, derived DI/DN, and Theorems 2--3
  at their printed proof/referral strengths;
- finite seriality, proper executions, the internal-edge SCC criterion, P and
  restricted MRG, both Theorem 5 clauses, and the local/external ownership of
  Appendix A's formulas and proof;
- Appendix B's two routes, every language-recursion clause, all local types,
  the eliminable omega-regular standing, and the externally owned acceptor,
  closure, and inclusion-decision facts; and
- cross-file consistency, the five-part technical-name rule, independently
  worded prose, the absence of later-result retrojection, and the narrow open
  status required by I8--I10.

Any mathematical uncertainty, unread authority page, hash mismatch,
unsupported assertion, incomplete checked-clean coverage, or remaining defect
requires `REVISE`. `ACCEPT` requires an exhaustive, evidence-located finding of
no remaining blocker or must-fix item on the complete frozen scope.

## Round-four repaired snapshot

Round three returned source fidelity `ACCEPT`, mathematical/proof `REVISE`,
and adversarial publication/AGENTS `REVISE`. Its nine distinct objections are
recorded as F27--F35 in the review ledger. They have been incorporated, but
incorporation is not acceptance. Round four is a fresh blind review of the
replacement snapshot below, and a verdict applies only to these exact
identities.

- Reader-presentation scope:
  `handbook/parts/p09/presentations/n-c-012.tex`, lines 370--1114 and
  1519--1526.
- Shared integration scope:
  `handbook/parts/p09/logic-in-computer-science.tex`, lines 599--823.
- Source-presentation-ledger scope:
  `spec/research/p09-source-presentations-lot2-3.md`, lines 151--167.
- Evidence and bibliography scope: the complete
  `spec/research/p09-pnueli-1977-source-note.md`; bibliography entries
  `Pnueli1977`, `McNaughton1966`, and `Landweber1969`; and enough adjacent
  presentation text to detect source, notation, or version conflation.
- Authority scope: the wrapper for provenance only and every printed body page
  46--57 for substantive source review. Images control over OCR or memory.
- Independence rule: no round-four seat may inspect `ledger.md`,
  `transcript/chair.md`, any earlier-round transcript, or any other seat's
  round-four transcript before filing its own verdict. A seat may edit only its
  assigned round-four transcript.
- Method rule: exact source reading, mathematical reasoning, and prose review
  only. No tests, test harnesses, automated checkers, repository scripts, TeX,
  handbook-PDF inspection, or builds.

### Round-four SHA-256 identities

- `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz`: `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB`
- `tmp/pdfs/p09-pnueli-1977/focs77.ps`: `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F`
- `tmp/pdfs/p09-pnueli-1977/focs77.pdf`: `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972`
- `handbook/parts/p09/presentations/n-c-012.tex`: `B015988618D84AA836D35D3AA0A1D484438C65910B78BB94CB74577A9FB02C9E`
- `handbook/parts/p09/logic-in-computer-science.tex`: `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394`
- `handbook/bib/handbook.bib`: `74F102209EEFB17C63FB5B41B6D257184064BFCFF52CF625BC7A1A61C443B3D9`
- `spec/research/p09-pnueli-1977-source-note.md`: `C3EE541610841D57A6FB6729C482919431660CFF896276FDABB330D9D21ADE54`
- `spec/research/p09-source-presentations-lot2-3.md`: `32F11A80F21E9C33AF3E664EBDEEB778E36B4B81E7A772C5BD91589090962AA0`

### Round-four mandatory fresh checks

Each seat must independently verify every charter criterion C1--C8 and every
invariant I1--I10 across the full authority and frozen scope, not merely inspect
the changed sentences. In addition to all mandatory round-three checks, each
seat must determine afresh whether F27--F35 are actually resolved:

- the raw-path counterexample's action symbol has one relation type and does
  not collide with the producer--consumer load;
- full attachment has an exact typed formula, metalinguistic standing,
  nonredundancy relative to partial attachment, and immediate use;
- the producer--consumer argument states every source-supplied indicator
  implication it uses while inventing no unprinted support set;
- state assertions are typed before use and no redundant one-off technical
  name remains;
- arbitrary-start action-condition paths, initial-state proper executions, and
  restricted system validity have distinct exact standings used consistently;
- the attachment-size comparison distinguishes two-process sum/product growth
  from process-count exponential growth and retains the invariant proof
  obligations;
- the exact internal-edge SCC formula and its two-direction proof are visibly
  handbook-supplied rather than quoted from the source;
- Theorem 5's adequacy clause is explicitly unproved in the paper and Appendix
  B is limited to semantic decision routes for the decidability clause; and
- Appendix B keeps Pnueli's local acceptor assertion, reference 32's imported
  omega-regular/closure machinery, and reference 33's inclusion decision at
  three separate proof-ownership standings.

Any mathematical uncertainty, unread authority page, hash mismatch,
unsupported assertion, incomplete checked-clean coverage, or remaining defect
requires `REVISE`. `ACCEPT` requires an exhaustive, evidence-located finding of
no remaining blocker or must-fix item on the complete round-four snapshot.

## Round-five repaired snapshot

Round four returned source fidelity `ACCEPT`, mathematical/proof `REVISE`, and
adversarial publication/AGENTS `REVISE`. Its five distinct objections are
recorded as F36--F40 in the review ledger and have been incorporated. Their
incorporation is not acceptance. Round five is a fresh blind review of the
replacement snapshot below, and a verdict applies only to these exact
identities.

- Reader-presentation scope:
  `handbook/parts/p09/presentations/n-c-012.tex`, lines 370--1178 and
  1583--1590.
- Shared integration scope:
  `handbook/parts/p09/logic-in-computer-science.tex`, lines 599--823.
- Source-presentation-ledger scope:
  `spec/research/p09-source-presentations-lot2-3.md`, lines 151--167.
- Evidence and bibliography scope: the complete
  `spec/research/p09-pnueli-1977-source-note.md`; bibliography entries
  `Pnueli1977`, `McNaughton1966`, and `Landweber1969`; and enough adjacent
  presentation text to detect source, notation, or version conflation.
- Authority scope: the wrapper for provenance only and every printed body page
  46--57 for substantive source review. Images control over OCR or memory.
- Independence rule: no round-five seat may inspect `ledger.md`,
  `transcript/chair.md`, any earlier-round transcript, or any other seat's
  round-five transcript before filing its own verdict. A seat may edit only its
  assigned round-five transcript.
- Method rule: exact source reading, mathematical reasoning, and prose review
  only. No tests, test harnesses, automated checkers, repository scripts, TeX,
  handbook-PDF inspection, or builds.

### Round-five SHA-256 identities

- `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz`: `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB`
- `tmp/pdfs/p09-pnueli-1977/focs77.ps`: `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F`
- `tmp/pdfs/p09-pnueli-1977/focs77.pdf`: `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972`
- `handbook/parts/p09/presentations/n-c-012.tex`: `1FABE2120A026468AE21DD2BC116A92DE9AAE048D84655032DA4F7048B82620E`
- `handbook/parts/p09/logic-in-computer-science.tex`: `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394`
- `handbook/bib/handbook.bib`: `74F102209EEFB17C63FB5B41B6D257184064BFCFF52CF625BC7A1A61C443B3D9`
- `spec/research/p09-pnueli-1977-source-note.md`: `B27AAA9E6C69403998671A924B7F1883DBC2122048D7CF47124464CA63B65803`
- `spec/research/p09-source-presentations-lot2-3.md`: `3065E52284FF29AAD53121398C3307D691955C13358AE9E314819285A3534203`

### Round-five mandatory fresh checks

Each seat must independently verify every charter criterion C1--C8 and every
invariant I1--I10 across the full authority and frozen scope, not merely inspect
the changed sentences. All round-three and round-four obligations F27--F40 must
be reconsidered from the repaired text. In particular, determine afresh whether:

- totalizing P2 at zero is correctly separated from soundness, the independent
  zero-rank and strict-future counterexamples both work, and the false-at-zero
  premise is accurately identified as an unprinted sufficient repair only for
  inclusive eventuality;
- R4 uses one exact parameterized family of state assertions, its pointwise
  existential has state-assertion standing rather than tense-formula standing,
  and the uniform arbitrary-parameter and consequent/open-assumption
  independence conditions are sufficient and accurately distinguished from
  the source display;
- metarule I is exactly typed by specializing that family to
  `N_0={0,1,2,...}`, its temporary-hypothesis derivation and arbitrary-index
  conclusion are correct, and Theorem 1 uses the same typed family/pointwise
  existential standing;
- the producer--consumer proof states both indicator directions it actually
  uses, especially `m_i=1` to critical-section membership and nonwaiting,
  without fabricating a complete support set;
- the displayed linear-future formula is valid under the reader's inclusive
  line semantics and false in the stated reflexive-transitive branching S4
  frame, so the source's Theorem 2 completeness model class is qualified at
  exactly the warranted strength; and
- the one-letter-word embedding makes `L(p)=[[p]]S^omega` well typed under the
  declared prefix-concatenation operation while remaining faithful to printed
  p. 57.

Any mathematical uncertainty, unread authority page, hash mismatch,
unsupported assertion, incomplete checked-clean coverage, or remaining defect
requires `REVISE`. `ACCEPT` requires an exhaustive, evidence-located finding of
no remaining blocker or must-fix item on the complete round-five snapshot.

## Round-six repaired snapshot

Round five returned source fidelity `ACCEPT`, mathematical/proof `ACCEPT`, and
adversarial publication/AGENTS `REVISE`. Its three distinct objections are
recorded as F41--F43 in the review ledger and have been incorporated. Their
incorporation is not acceptance. Round six is a fresh blind review of the
replacement snapshot below, and a verdict applies only to these exact
identities.

- Reader-presentation scope:
  `handbook/parts/p09/presentations/n-c-012.tex`, lines 370--1204 and
  1610--1617.
- Shared integration scope:
  `handbook/parts/p09/logic-in-computer-science.tex`, lines 599--823.
- Source-presentation-ledger scope:
  `spec/research/p09-source-presentations-lot2-3.md`, lines 151--167.
- Evidence and bibliography scope: the complete
  `spec/research/p09-pnueli-1977-source-note.md`; bibliography entries
  `Pnueli1977`, `McNaughton1966`, and `Landweber1969`; and enough adjacent
  presentation text to detect source, notation, or version conflation.
- Authority scope: the wrapper for provenance only and every printed body page
  46--57 for substantive source review. Images control over OCR or memory.
- Independence rule: no round-six seat may inspect `ledger.md`,
  `transcript/chair.md`, any earlier-round transcript, or any other seat's
  round-six transcript before filing its own verdict. A seat may edit only its
  assigned round-six transcript.
- Assigned transcripts: source fidelity writes only
  `transcript/r6-source-fidelity.md`; mathematical/proof writes only
  `transcript/r6-mathematical-proof.md`; adversarial publication/AGENTS writes
  only `transcript/r6-adversarial-publication.md`.
- Method rule: exact source reading, mathematical reasoning, and prose review
  only. No tests, test harnesses, automated checkers, repository scripts, TeX,
  handbook-PDF inspection, or builds.

### Round-six SHA-256 identities

- `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz`: `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB`
- `tmp/pdfs/p09-pnueli-1977/focs77.ps`: `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F`
- `tmp/pdfs/p09-pnueli-1977/focs77.pdf`: `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972`
- `handbook/parts/p09/presentations/n-c-012.tex`: `3A4ECE9251B46ACAD8925FFCD34162BE3F9741C09DF912B70967C8FAAB7BE1BC`
- `handbook/parts/p09/logic-in-computer-science.tex`: `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394`
- `handbook/bib/handbook.bib`: `74F102209EEFB17C63FB5B41B6D257184064BFCFF52CF625BC7A1A61C443B3D9`
- `spec/research/p09-pnueli-1977-source-note.md`: `86EA6E1F4934B61D5D7E517C01466D6CDA98F80348B1233D52F953F9B1A821CA`
- `spec/research/p09-source-presentations-lot2-3.md`: `05931057A05C0DCD81507394AF6152B02C3BC12B7E5A7E7AAB757A84A4B1F5C9`

### Round-six mandatory fresh checks

Each seat must independently verify every charter criterion C1--C8 and every
invariant I1--I10 across the full authority and frozen scope, not merely inspect
the changed sentences. All earlier obligations F27--F40 and the new F41--F43
must be reconsidered from the repaired text. In particular, determine afresh
whether:

- Theorem 1's initial-state execution semantics is correctly distinguished
  from its pointwise arbitrary-state proof step; the two-loop unreachable-state
  counterexample is serial and finitely branching, makes `p leadsto q` true,
  and makes every `P(u,n)` false; the three alternative missing boundaries are
  sufficient only for that first gap and are not attributed to Pnueli;
- the unreachable-state failure remains independent of the deadlock-vacuity
  base-step failure, and the two corresponding repair families are neither
  conflated nor silently added to the theorem;
- the S4 witness is a complete Kripke model `M=(W,rho,V)`, not merely a frame:
  its displayed relation is reflexive and transitive, the valuation makes the
  root satisfy neither atom, the root satisfies the antecedent, and neither
  consequent disjunct holds under the accessibility reading of `F`;
- the early enabled-processor prose and later action-occurrence formula are
  described as distinct, with no unproved strength comparison, equivalence, or
  typed correspondence;
- the round-five P2 counterexamples, false-at-zero boundary, typed R4/I family,
  producer indicator deductions, model-class qualification, and one-letter
  language typing remain correct and have not regressed;
- the manuscript, shared surface, source note, presentation ledger,
  bibliography, and adjacent presentation boundaries agree on every source,
  theorem-strength, proof-ownership, terminology, and status claim; and
- N-c-012.b remains open pending unanimity and every IEEE-comparison,
  neighboring-presentation, Part IX, build, visual, human, final-book, and user
  gate remains outside this review's possible closure.

Any mathematical uncertainty, unread authority page, hash mismatch,
unsupported assertion, incomplete checked-clean coverage, or remaining defect
requires `REVISE`. `ACCEPT` requires an exhaustive, evidence-located finding of
no remaining blocker or must-fix item on the complete round-six snapshot.

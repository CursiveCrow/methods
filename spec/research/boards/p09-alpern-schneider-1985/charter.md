# Board charter: Alpern--Schneider 1985 controlling presentation

- Artifact: the frozen seven-object manuscript/source snapshot identified below.
- Purpose: determine whether the handbook's unlettered controlling presentation
  of Alpern and Schneider's *Defining Liveness* is source-faithful,
  mathematically correct, definition-before-use compliant, and fit for
  graduate-handbook publication at the manuscript-content level.
- Mode: review.
- Requested by: the user's standing requirement that every completed handbook
  topic receive three independent blind scholarly reviews before admission.
- Authorship disclosure: chair-authored reconstruction. The chair acquired and
  read the sources, wrote the current reader/source records, and identified the
  candidate source defects. No seated reviewer authored any frozen artifact.
- Severity taxonomy: blocker, must-fix, should-fix, consider, discard,
  unresolved-user.
- Source rule: every artifact claim cites an exact file/line or printed source
  page; external claims cite a fetchable primary source. Unverified claims
  cannot block. The complete page images, not extracted text, control visual
  readings of formulas and printed wording.
- Consensus rule: rough consensus governs finding dispositions; opening plus
  at most two focused deliberation rounds. Topic admission has the additional
  user gate that every mandate must end with no unresolved blocker or must-fix
  and must file `ACCEPT` on the same frozen snapshot. This is a mandate gate,
  not vote counting.
- Board type: live.
- Workspace:
  `spec/research/boards/p09-alpern-schneider-1985/`.

## Frozen round-one snapshot

No frozen artifact may be edited while round one is open. Any content edit
invalidates every verdict and requires a new hash-pinned blind round.

| Artifact | Review scope | SHA-256 |
|---|---|---|
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-defining-liveness.pdf` | complete five-page controlling journal article | `FB69B4E81FD14CAE073F6087CE724E70847FFF16EA560701525952908E48FE31` |
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-tr-85-650.pdf` | complete eleven-file-page comparison report | `CF02E04AF863E7325C59C6C4671E389C53DB7B7ADA7804A379B287C569C896AE` |
| `handbook/parts/p09/presentations/n-c-012.tex` | lines 2632--2975, beginning `Alpern--Schneider's semantic decomposition` | `D1844530FA4BA9EC2E8F702763966F8AA3C57BE3A3E3DD5163EEA24E2905033D` |
| `handbook/parts/p09/logic-in-computer-science.tex` | lines 710--718, shared safety/liveness definition | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` |
| `handbook/bib/handbook.bib` | lines 6056--6080, journal and report records | `E0AF3849EEB34AB9966EF971881D3D10307ED47A92593FBE0B91917E18A1318E` |
| `spec/research/p09-alpern-schneider-1985-source-note.md` | complete lines 1--634 | `B99757CEAADE0045D4663493403112892AC4A199176D7B4A0D244AF23168532F` |
| `spec/research/p09-source-presentations-lot2-3.md` | lines 395--528, compact controlling presentation | `35D27BCC4AE25DE83260CB9356D854F64E99FAAFC6B824A34B85366B553CE872` |

The journal page images are
`tmp/pdfs/p09-alpern-schneider-1985/journal-page-1.png` through
`journal-page-5.png`; the report images are `tr-page-01.png` through
`tr-page-11.png`. They are reading aids. The two PDFs above remain the source
identities.

## Invariants

- I1: The journal article is the controlling authority; the Cornell technical
  report is a separately identified comparison witness. They may not be
  conflated. (stated by user/source-truth workflow)
- I2: Every source page must be visually read. Search extraction alone is not
  evidence for a symbol, formula, page layout, or printed defect. (stated by
  user/source-truth workflow)
- I3: The reader must define notation before use and state exact standing for
  every introduced term or symbol. (stated by user and AGENTS instructions)
- I4: A new technical name is admissible only with local necessity, exact
  eliminable definition or axiom, standing, nonredundancy, and later use. An
  owed artifact must not be disguised as a hypothetical named answer. (stated
  by user through AGENTS instructions)
- I5: The source's implicit nonempty-state hypothesis must be either justified
  as unnecessary or stated explicitly wherever the empty-state case would
  break liveness/density or Theorem 1. (correctness invariant inferred from the
  definitions)
- I6: Source text, handbook reconstruction, handbook-owned proof, and
  handbook-owned correction must remain visibly distinct. Printed defects may
  not be silently repaired. (stated by user/source-truth workflow)
- I7: Safety/liveness are semantic property classes over the declared sequence
  universe, not a syntactic partition of LTL formulas and not a fixed-system
  path restriction unless explicitly relativized. (source and existing
  handbook invariant)
- I8: The reader must not reduce liveness to a single eventual atomic event or
  turn Theorem 1 into uniqueness, cheap computability, or language-level
  expressibility. (source-strength invariant)
- I9: Corollary 2.1 must preserve the literal intersection-closure hypothesis,
  determine whether it is valid, and distinguish any correction from source
  attribution. (source-critical invariant)
- I10: The source's arguments, numbered theorems, corollaries, examples,
  version boundary, proof granularity, and conclusion must be reported at
  their exact strength. (source-fidelity invariant)
- I11: Copyright/access status must not be restated as an open licence, and the
  reconstruction must not reproduce protected expression beyond ordinary
  scholarly quotation. (publication invariant)
- I12: Acceptance is limited to this unlettered controlling presentation inside
  `N-c-012`; no `N-c-012.e` identifier is invented, and no broader Part IX,
  book, build, rendered-page, human-review, completion, or user-acceptance gate
  is closed. (stated by user and live register)
- I13: This is book scholarship, not software engineering. No test, test
  harness, automated checker, repository script, TeX command, interim handbook
  build, or handbook-PDF inspection may be used or claimed. Source-page visual
  reading, direct manuscript reading, mathematical proof, citation inspection,
  and file hashes for snapshot identity are the permitted evidence methods.
  (stated by user)
- I14: Seats remain blind in the opening round: they may not read the ledger,
  chair transcript, earlier Part IX board transcripts, another current
  transcript, or another verdict; they may not contact one another. (review
  independence invariant)

## Mandatory coverage points

- M01: recompute all seven frozen hashes before substantive review.
- M02: visually read journal pp. 181--185 and all eleven report file pages.
- M03: verify title, authors, venue, issue date, page range, DOI, receipt and
  revision dates, report number/date, access route, and rights statement.
- M04: verify the journal/report page maps and the claim of substantive
  agreement, including whether Corollary 2.1 has the same wording in both.
- M05: verify (S\ne\varnothing), (S^*), (S^\omega), empty sequence,
  concatenation, prefix, one-state finite words, constant executions, property
  standing, membership notation, program satisfaction, and terminal-state
  padding.
- M06: verify the exact safety quantifiers and the finite bad-prefix reading.
- M07: verify “live for (P)” as a prefix/property relation and liveness as its
  universal closure, including nonemptiness and the full-sequence-space
  boundary.
- M08: verify the proof-method motivation, maximality argument, safety/liveness
  examples, and stuttering qualification without proof-strength promotion.
- M09: verify exact uniform and absolute liveness definitions, standing,
  nonredundancy, use, and inclusion chain.
- M10: verify the leads-to example, including which claims are printed and
  which fixed-suffix conclusion is handbook-supplied.
- M11: verify the predictive property, nondegeneracy hypotheses, liveness proof,
  and failure of uniform liveness.
- M12: verify the until and total-correctness examples and the rejection of a
  safety/liveness dichotomy.
- M13: verify the cylinder basis and both directions of safety iff closed and
  liveness iff dense.
- M14: verify Theorem 1's construction, set algebra, minimal-closed-superset
  density proof, and exact nonuniqueness/syntax/algorithm boundaries.
- M15: verify Corollary 1.1 and every closure hypothesis it actually needs.
- M16: verify Theorem 2, the source-to-handbook alpha-renamings, density and
  disjointness of the eventually constant properties, the factorization, and
  the materiality of (|S|>1).
- M17: verify Corollary 2.1 as printed; independently assess the
  intersection-closed denotation-family countermodel and the union-closure or
  Boolean-closure repair.
- M18: verify every Boolean-closure entry and the claim that only the whole
  space is both safety and liveness.
- M19: verify which proofs the article prints, which equivalences it merely
  states, and which arguments belong to the handbook.
- M20: verify definition-before-use and the full AGENTS terminology rule for
  `live for P`, uniform liveness, absolute liveness, (P_{A,B}), (L_P),
  (E_a,E_b), (Q), and (mathcal F).
- M21: reconcile reader, shared definition, bibliography, source note, and
  compact presentation claim by claim.
- M22: verify the unlettered register standing, rights boundary, topic-only
  status, and explicit no-test/no-build boundary.

## Roster and role cards

### Source fidelity and evidence seat

- Mandate: determine whether every reader/source-record claim is supported at
  the stated strength by the complete controlling article and comparison
  report.
- Checklist: M01--M12 and M14--M22, with special attention to printed wording,
  locators, source-versus-handbook ownership, version comparison, bibliography,
  rights, and proof-granularity claims.
- Evidence: exact printed page and exact manuscript line for every finding;
  visually resolve formulas and the Corollary 2.1 word in both sources.
- Blind spot to avoid: treating a mathematically plausible reconstruction as
  source text, or rejecting a disclosed handbook proof merely because it is not
  printed.

### Mathematical and proof-correctness seat

- Mandate: independently rederive every definition, implication, example,
  topological equivalence, theorem, corollary, countermodel, and edge case.
- Checklist: M05--M18 and M20--M21, including (S=\varnothing), (|S|=1),
  empty prefixes, degenerate (A,B), exact quantifier orders, Theorem 1
  minimality, Theorem 2 disjointness, and the semantic-family countermodel.
- Evidence: explicit derivations or minimal counterexamples tied to manuscript
  lines and source pages; state exactly what would fail under a rejected claim.
- Blind spot to avoid: silently strengthening source claims, skipping a null or
  singleton case, or accepting a proof because its conclusion is familiar.

### Adversarial publication and terminology seat

- Mandate: decide whether a hostile expert reader could expose ambiguity,
  invented terminology, source laundering, scope inflation, unreadable proof
  presentation, or a false publication/completion claim.
- Checklist: M01--M22, emphasizing I3--I4 and I6--I14; perform the premortem
  duty if the snapshot otherwise appears clean.
- Evidence: exact manuscript locations, the violated invariant, concrete harm
  to a graduate reader, and the smallest exact correction.
- Blind spot to avoid: mere stylistic preference, speculative expansion, or
  importing modern terminology the source and handbook do not need.

Agents/models are recorded in the chair transcript when seats are spawned; no
seat is shown another seat's identity or output during the blind opening.

## Opening-round filing rule

Each seat writes only its assigned file in `transcript/` and ends with:

- `VERDICT: ACCEPT` if no blocker or must-fix remains for its mandate; or
- `VERDICT: REJECT` followed by the exact blocking record IDs.

Every finding uses the board finding schema and every coverage point is marked
checked-clean, finding-linked, or not-checked with reason. A seat may not edit
any frozen artifact, ledger, chair file, or another transcript.

## Frozen round-two repaired snapshot

Round one was rejected and thawed as recorded in `ledger.md` and
`transcript/chair.md`.  Round two freezes the repaired seven-object snapshot
below.  No listed artifact may be edited until all three fresh blind seats
have filed.  The purpose, invariants, mandatory coverage points, role cards,
evidence boundary, and filing rule above continue unchanged.

| Artifact | Round-two review scope | SHA-256 |
|---|---|---|
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-defining-liveness.pdf` | complete five-page controlling journal article | `FB69B4E81FD14CAE073F6087CE724E70847FFF16EA560701525952908E48FE31` |
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-tr-85-650.pdf` | complete eleven-file-page comparison report | `CF02E04AF863E7325C59C6C4671E389C53DB7B7ADA7804A379B287C569C896AE` |
| `handbook/parts/p09/presentations/n-c-012.tex` | lines 2632--2990, beginning `Alpern--Schneider's semantic decomposition` | `4E58F17BC534504C5D43DE2EADBD365CE01B8D029CE8A67B2BBAFBF2DAD75736` |
| `handbook/parts/p09/logic-in-computer-science.tex` | lines 710--718, shared safety/liveness definition | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` |
| `handbook/bib/handbook.bib` | lines 6056--6080, journal and report records | `E0AF3849EEB34AB9966EF971881D3D10307ED47A92593FBE0B91917E18A1318E` |
| `spec/research/p09-alpern-schneider-1985-source-note.md` | complete lines 1--659 | `786B63163F0EF1456561B974D1D4A38578A06AF619C4DAB0ADE05FFCC0D7EE13` |
| `spec/research/p09-source-presentations-lot2-3.md` | lines 395--537, compact controlling presentation | `915ECD5D1451D24E336A60616AF5F93EBE300774A1D29FABABD0531035F4838E` |

Round-two seats must inspect the four admitted round-one findings in addition
to M01--M22, but must not read any round-one transcript, `ledger.md`, or the
chair transcript.  They receive the defect statements and corrected claims in
their prompts without receiving another reviewer's reasoning or verdict.

## Frozen round-three repaired snapshot

Round two was rejected and thawed as recorded in `ledger.md` and
`transcript/chair.md`.  Round three freezes the repaired seven-object snapshot
below.  No listed artifact may be edited until all three fresh blind seats
have filed.  The purpose, invariants, mandatory coverage points, role cards,
evidence boundary, and filing rule above continue unchanged.

| Artifact | Round-three review scope | SHA-256 |
|---|---|---|
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-defining-liveness.pdf` | complete five-page controlling journal article | `FB69B4E81FD14CAE073F6087CE724E70847FFF16EA560701525952908E48FE31` |
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-tr-85-650.pdf` | complete eleven-file-page comparison report | `CF02E04AF863E7325C59C6C4671E389C53DB7B7ADA7804A379B287C569C896AE` |
| `handbook/parts/p09/presentations/n-c-012.tex` | lines 2632--3011, beginning `Alpern--Schneider's semantic decomposition` | `0C72F461A83E421AAFF950E2CBA03FD386EEA088BAC70E9D8E30E86052E977D2` |
| `handbook/parts/p09/logic-in-computer-science.tex` | lines 710--718, shared safety/liveness definition | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` |
| `handbook/bib/handbook.bib` | lines 6056--6080, journal and report records | `E0AF3849EEB34AB9966EF971881D3D10307ED47A92593FBE0B91917E18A1318E` |
| `spec/research/p09-alpern-schneider-1985-source-note.md` | complete lines 1--681 | `75D66211C3520522D7530C609221AB20C0409EBBA6CBCD29BD9C3CD9B8D8DD27` |
| `spec/research/p09-source-presentations-lot2-3.md` | lines 395--552, compact controlling presentation | `C2526F8FF7FAFFE4DB2902799BB968E0B21491B57CCC40F6548EEB6BAA534031` |

Round-three seats must independently inspect M01--M22 and the following five
admitted round-two corrections without reading any earlier transcript,
`ledger.md`, or the chair transcript:

1. distinguish the source's conditional liveness claim for leads-to from its
   unqualified non-absolute-liveness claim;
2. type one-state finite words, constant executions, concatenated witnesses,
   and one-letter cylinders before use;
3. use the source-exact name `until`, not `strong-until`;
4. include the leads-to defect in the source-critical findings table; and
5. report the Plotkin temporal-logic decomposition only as an independently
   unverified private-communication claim.

They must also independently verify the handbook-owned assertion that, in the
state-set rendering, nonempty `E_1`, nonempty `E_2`, and a nonempty neutral
state set are jointly necessary and sufficient for leads-to to be uniformly
live but not absolutely live.

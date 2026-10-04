# Alpern--Schneider 1985 independent manuscript review record

## Admission scope

This record closes reader-facing body reconstruction and the three independent
manuscript-content review gates for exactly the unlettered controlling
presentation of Bowen Alpern and Fred B. Schneider's 1985 article “Defining
Liveness” within `N-c-012`. Its principal reader scope begins at
`\subsubsection{Alpern--Schneider's semantic decomposition}` in
`handbook/parts/p09/presentations/n-c-012.tex`, line 2632, and ends at line
3011. The shared Part IX safety/liveness definition, the two bibliography
records, the complete source note, and the compact controlling presentation
were reviewed with it.

The register assigns no `N-c-012.e`, and this admission invents none.
Acceptance is limited to Alpern--Schneider's unlettered controlling role inside
`N-c-012`; it does not admit `N-c-012` as a whole, Part IX, another handbook
part, the final generated handbook, rendered-page inspection, human review,
final-book completion, or user acceptance.

Acceptance does not certify every printed source statement as correct. The
accepted presentation expressly preserves and distinguishes:

- the source's implicit nonempty-state assumption, made explicit because the
  empty-state case separates density from the printed liveness clause;
- the leads-to paragraph's conditional liveness claim and its unqualified,
  overbroad non-absolute-liveness claim;
- the handbook-owned necessary-and-sufficient state-set repair of that
  leads-to separation;
- the source-stated safety/closed and liveness/dense equivalences and the
  handbook-supplied direction proofs;
- the article's Plotkin decomposition only as a reported, independently
  unverified 1983 private communication;
- the literal Corollary 2.1 intersection-closure hypothesis, the handbook's
  countermodel to the printed implication, and union closure as the minimal
  repair; and
- the article's methodological defense of liveness without promoting it to a
  formal uniqueness or correctness theorem.

Acceptance means those source claims, source defects, handbook proofs,
handbook-owned repairs, proof-strength limits, version boundaries, and rights
limits are presented accurately.

## Exact accepted snapshot

All three final reviewers accepted the following exact seven-object snapshot:

| Artifact | SHA-256 |
|---|---|
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-defining-liveness.pdf` | `FB69B4E81FD14CAE073F6087CE724E70847FFF16EA560701525952908E48FE31` |
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-tr-85-650.pdf` | `CF02E04AF863E7325C59C6C4671E389C53DB7B7ADA7804A379B287C569C896AE` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `0C72F461A83E421AAFF950E2CBA03FD386EEA088BAC70E9D8E30E86052E977D2` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` |
| `handbook/bib/handbook.bib` | `E0AF3849EEB34AB9966EF971881D3D10307ED47A92593FBE0B91917E18A1318E` |
| `spec/research/p09-alpern-schneider-1985-source-note.md` | `75D66211C3520522D7530C609221AB20C0409EBBA6CBCD29BD9C3CD9B8D8DD27` |
| `spec/research/p09-source-presentations-lot2-3.md` | `C2526F8FF7FAFFE4DB2902799BB968E0B21491B57CCC40F6548EEB6BAA534031` |

The chair recomputed all seven identities after all reports had been filed and
read. Every value remained exact.

## Primary and comparison authorities

The controlling authority was the complete five-page journal article:

- Bowen Alpern and Fred B. Schneider, “Defining Liveness,” *Information
  Processing Letters* 21(4), 7 October 1985, pp. 181--185;
- DOI `10.1016/0020-0190(85)90056-0`;
- local object
  `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-defining-liveness.pdf`;
- controlling SHA-256
  `FB69B4E81FD14CAE073F6087CE724E70847FFF16EA560701525952908E48FE31`.

The complete revised Cornell technical report was reviewed separately as a
comparison witness:

- Bowen Alpern and Fred B. Schneider, “Defining Liveness,” Cornell Department
  of Computer Science, TR 85-650, 30 October 1984, revised 20 February 1985;
- local object
  `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-tr-85-650.pdf`;
- SHA-256
  `CF02E04AF863E7325C59C6C4671E389C53DB7B7ADA7804A379B287C569C896AE`.

Every final reviewer visually read all five journal pages and all eleven report
file pages at original detail. The report agrees substantively with the
journal and independently confirms the same defective intersection-closure
wording in the second corollary. The journal remains controlling.

Printed journal p. 181 carries Elsevier/North-Holland copyright. Neither
author-hosted object declares an open-content licence. The handbook therefore
uses independently written scholarly reconstruction and does not claim a
right to republish the source files or protected expression.

## Reviewer transcripts and independence

| Seat | Canonical reviewer | Model | Final transcript | Transcript SHA-256 | Verdict |
|---|---|---|---|---|---|
| source fidelity and evidence | `/root/as_r3_source_fidelity` | `gpt-5.5`, xhigh | `spec/research/boards/p09-alpern-schneider-1985/transcript/r3-source-fidelity.md` | `19AB40D06B6E26E74A15C44FDDAF9BD9EF4BEED6641B5735121AE9356B6E0197` | **ACCEPT** |
| mathematical and proof correctness | `/root/as_r3_mathematical_proof` | `gpt-5.6-sol`, xhigh | `spec/research/boards/p09-alpern-schneider-1985/transcript/r3-mathematical-proof.md` | `C1DB1C0520EBB61A3336C4B9470A53FAFE6FADDEC061AFE038E0511D50EB1B1A` | **ACCEPT** |
| adversarial publication and terminology | `/root/as_r3_adversarial_publication` | `gpt-5.6-terra`, xhigh | `spec/research/boards/p09-alpern-schneider-1985/transcript/r3-adversarial-publication.md` | `D6F61FD3CBA23D292F889211CC3D40F90AB083BB86AE1E1B5E8D19648BC04D50` | **ACCEPT** |

Each reviewer was a fresh direct child of the chair with no inherited turn
history. Each was instructed to read the complete charter and frozen scope;
not to read the ledger, chair record, any earlier or concurrent transcript, or
another verdict; not to contact another reviewer; and not to edit a frozen
artifact. Each wrote only its assigned transcript. The chair kept every filed
transcript sealed until all three were complete, then read all three in full.

Every reviewer independently recomputed all seven frozen identities before
substantive review. After all reports were complete, the chair independently
recomputed the seven artifact identities and all three transcript hashes.
Every value matched.

This was manuscript scholarship, not software engineering. No reviewer and no
chair operation used a test, test harness, automated checker, repository
script, TeX command, handbook-PDF inspection, or build. Primary-source visual
reading, direct manuscript reading, mathematical proof, citation and
provenance inspection, and SHA-256 identity labels were the review methods.
These manuscript-content reviews establish no compilation or rendered-page
result.

## Final review findings

The source-fidelity seat checked every mandatory point M01--M22, all five
round-three repairs, and the leads-to necessity/sufficiency result. It found no
remaining source discrepancy, unread page, locator failure, version
conflation, unsupported attribution, silent source repair, proof promotion, or
rights overclaim.

The mathematical seat independently rederived the safety and liveness clauses,
the strict liveness subclasses, every degeneration of the leads-to and
predictive examples, both topological equivalences, Theorem 1, Corollary 1.1,
Theorem 2, the Corollary 2.1 countermodel and correction, and every Boolean
closure entry. It found no type error, quantifier error, false edge case,
invalid countermodel, or unsupported theorem strength.

The adversarial seat conducted a hostile-reader premortem for source
laundering, finite/infinite type slippage, invented terminology,
definition-after-use, theorem promotion, rights overstatement, and premature
completion language. It applied the full AGENTS necessity, definition,
standing, nonredundancy, and use rule to every introduced name and found no
remaining publication-blocking defect.

No final seat filed a blocker, must-fix, should-fix, uncertainty, unread page,
or identity mismatch. No majority vote was taken and no earlier acceptance was
carried forward.

## Revision history and closure

Three blind rounds were required.

1. Round one returned source-fidelity `ACCEPT` and two `REJECT` verdicts. Four
   admitted repairs restored the typed compact safety binder, distinguished an
   insufficient Corollary 2.1 hypothesis from a false assumption, typed the
   predictive state sets, and repaired the overbroad leads-to separation.
2. Round two returned three `REJECT` verdicts. Five admitted repairs separated
   the source's conditional and unqualified leads-to claims, distinguished
   singleton finite words from constant executions, restored the source word
   `until`, added the leads-to defect to the critical table, and restored the
   Plotkin claim with its private-communication limit. The reader also made the
   exact leads-to hypotheses necessary as well as sufficient.
3. Round three returned three independent `ACCEPT` verdicts on the unchanged
   seven-object snapshot above. Every mandatory point and every admitted repair
   was checked clean.

No supported finding was discarded or outvoted, and no verdict on an earlier
hash was used to accept a changed artifact.

## Admission disposition

The exact round-three snapshot is admitted for reader-facing body
reconstruction and topic-level manuscript review of the unlettered
Alpern--Schneider 1985 controlling presentation only. The admission preserves
the disclosed source defects, handbook-owned proofs and corrections,
proof-strength qualifications, journal/report separation, private-
communication limit, terminology standing, and rights boundary.

`N-c-012` overall, the later Part IX presentations, Part IX admission, the
other thirteen parts, the one final publication build after all fourteen parts
are text-frozen, rendered inspection, human review, final-book completion, and
user acceptance remain separate and open. No tests, test harnesses, automated
checkers, repository scripts, TeX, handbook-PDF inspection, or builds were run
for this admission.

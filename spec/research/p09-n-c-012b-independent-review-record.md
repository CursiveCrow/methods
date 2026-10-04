# N-c-012.b independent manuscript review record

## Admission scope

This record closes the reader-facing body reconstruction and the three
independent manuscript-content review gates for exactly `N-c-012.b`, Amir
Pnueli's 1977 presentation, “The Temporal Logic of Programs.”  Its principal
reader scope begins at
`\subsubsection{Pnueli's 1977 transition system and proof systems}` in
`handbook/parts/p09/presentations/n-c-012.tex` and ends immediately before the
GPSS presentation.  The Pnueli version boundary and the relevant shared Part IX
definitions and integration surface were reviewed with it.

This admission does not assert that every theorem or proof sketch printed by
Pnueli is correct under the reconstructed semantics.  The accepted presentation
expressly preserves the source's strict/inclusive tensions, the two defects in
literal P2, the two independent gaps in Theorem 1's completeness sketch, and
Theorem 2's unresolved model-class boundary.  Acceptance means that those
source standings, defects, counterexamples, handbook reconstructions, and proof
ownership boundaries are themselves stated correctly.

This record does not close the still-unperformed comparison with an
IEEE-supplied file, `N-c-012.c`, `N-c-012.d`, `N-c-012` as a whole, Part IX
admission, any build or rendered page, human review, the final handbook, or the
user's acceptance.

All three final reviewers accepted the following exact pre-admission snapshot:

| Artifact | SHA-256 |
|---|---|
| `handbook/parts/p09/presentations/n-c-012.tex` | `3A4ECE9251B46ACAD8925FFCD34162BE3F9741C09DF912B70967C8FAAB7BE1BC` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394` |
| `handbook/bib/handbook.bib` | `74F102209EEFB17C63FB5B41B6D257184064BFCFF52CF625BC7A1A61C443B3D9` |
| `spec/research/p09-pnueli-1977-source-note.md` | `86EA6E1F4934B61D5D7E517C01466D6CDA98F80348B1233D52F953F9B1A821CA` |
| `spec/research/p09-source-presentations-lot2-3.md` | `05931057A05C0DCD81507394AF6152B02C3BC12B7E5A7E7AAB757A84A4B1F5C9` |

The source-presentation-ledger hash is the pre-admission status surface read by
all three reviewers.  Its subsequent status-only change records their unanimous
verdict and links this review record; the resulting post-admission ledger hash
is `A2E96D6625AF1CB7317D5A7B373EC1CC767CD50176639BDF19285B476EECE570`.
That change alters no reader-facing mathematics, source claim, bibliography, or
source note.  The accepted reader and source note retain their conditional
pre-admission wording so that their reviewed hashes are not rewritten after the
fact; this record and the post-admission ledger record that the condition was
satisfied.

## Primary authority surface

The primary authority was Pnueli's complete author-hosted printed body,
preserved through the following identities:

| Object | SHA-256 | Standing |
|---|---|---|
| `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz` | `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB` | author-hosted compressed object |
| `tmp/pdfs/p09-pnueli-1977/focs77.ps` | `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F` | lossless decompression |
| `tmp/pdfs/p09-pnueli-1977/focs77.pdf` | `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972` | local scholarly-inspection render |

The render has thirteen physical pages.  Physical page 1 is a provenance
wrapper dated May 1981; physical pages 2--13 are the 1977 paper's printed pages
46--57.  Every final reviewer visually read the wrapper for provenance and all
twelve printed body pages for substance.  Images controlled over OCR and
memory.  The local PDF and page images were reading aids, not substituted
bibliographic authorities or a second mathematical edition.

No open-content, public-domain, or republication licence was inferred from
public hosting.  The handbook uses independent prose.  The author-hosted body
has not been directly compared with an IEEE-supplied object, and that
publisher-file comparison remains open.

## Reviewer transcripts, runtime, and independence

| Seat | Canonical reviewer | Final transcript | Transcript SHA-256 | Verdict |
|---|---|---|---|---|
| source fidelity | `/root/schmidt_smolka_1991_research` | `spec/research/boards/p09-n-c-012b/transcript/r6-source-fidelity.md` | `EB0A98970CE3C7D8D4CA2F97CD0B1E98BE24C9B8EDDBE549AB5CBC85A6CD8971` | **ACCEPT** |
| mathematical/proof correctness | `/root/p09_math_proof_review` | `spec/research/boards/p09-n-c-012b/transcript/r6-mathematical-proof.md` | `2D11A37E140587C24D0FE1C8E55EB297AF3940C8F2955BE179003519F77BC003` | **ACCEPT** |
| adversarial publication/AGENTS | `/root/mcnaughton_1966_research` | `spec/research/boards/p09-n-c-012b/transcript/r6-adversarial-publication.md` | `59D083B7C6D2907D41D18B6959E08BBC668A7A8CD20F39873461129795F83EB7` | **ACCEPT** |

Each transcript begins and ends exactly with `ACCEPT`.  The source-fidelity and
adversarial harnesses exposed no exact runtime model/version; the mathematical
seat identified a GPT-5-family Codex runtime but no more specific deployment or
version.  The unavailable exact build identifiers are recorded as unavailable
rather than guessed.

Each reviewer was instructed to read the complete frozen scope and every
printed authority page, not to inspect any earlier review, board ledger, chair
record, or another final transcript, not to contact another reviewer, and not
to edit a frozen artifact.  Each wrote only its assigned transcript.  Each
independently checked all eight controlling hashes before substantive review,
immediately before filing, and after filing; every check matched.

Source-image reading was allowed only for scholarship.  No reviewer ran a
test, test harness, automated checker, repository script, TeX command,
handbook-PDF inspection, or build.  The chair likewise used only direct source
and text reading, mathematical reasoning, editorial comparison, and SHA-256
identity checks.  These content reviews establish no compilation or rendered-
page result.

## Source-fidelity review

- Canonical reviewer: `/root/schmidt_smolka_1991_research`.
- Role: complete primary-source fidelity, provenance, locators, and attribution.
- Final verdict on the accepted snapshot: **ACCEPT**.

The final source instruction required a fresh visual reading of the wrapper and
every printed page 46--57, plus full checks of the reader, shared definitions,
source note, ledger entry, bibliography, and adjacent presentation boundaries.
The reviewer found no source-fidelity defect.

Evidence digest: the reviewer confirmed the exact dynamic-system and
initial-execution model; sequential and concurrent transition equations;
atomicity and the two nonidentified fairness formulations; reflexive
reachability; the specification hierarchy; literal P1/P2 and all ER forms;
metarule I and Theorem 1's printed proof-sketch assumptions; sequential and
concurrent attachments; the producer--consumer invariants; inclusive `F/G`;
the pure and system-dependent calculi; Theorems 2--5; the SCC route; and both
appendices.  It separately confirmed that the handbook's types,
counterexamples, finite-SCC proof, one-letter language embedding, and
source/referral boundaries are disclosed as handbook work rather than printed
source content.

For the last repair specifically, the source reviewer verified that the serial
two-loop example exposes the mismatch between initial-state temporal
implication and Theorem 1's arbitrary-state pointwise step; that this failure is
independent of the deadlock-vacuity base-step failure; that the three-world S4
witness supplies a complete relation and valuation with the root satisfying
neither atom; and that the later action-occurrence condition is described only
as distinct from the earlier enabled-processor prose.

## Mathematical and proof review

- Canonical reviewer: `/root/p09_math_proof_review`.
- Role: mathematical correctness, typing, quantification, theorem strength, and
  proof ownership.
- Final verdict on the accepted snapshot: **ACCEPT**.

The mathematical reviewer independently rederived the complete proof surface
rather than checking only the final repair.  It found no type or quantifier
error, invalid local derivation, unsupported theorem-strength claim,
mathematical uncertainty, or proof-ownership error.

Evidence digest: the reviewer recomputed both independent P2 counterexamples
and the limited inclusive sufficiency of the false-at-zero premise; checked the
R4 eigenparameter and open-assumption conditions; verified the
`\mathbb N_0` specialization of metarule I and Theorem 1's pointwise family;
recomputed every producer--consumer deduction; proved the linear validity of
the displayed eventuality-order formula; evaluated the complete S4 model at
all three worlds; verified N, DI, and DN; proved both directions of the
handbook-supplied finite SCC characterization; and rechecked Theorems 4--5 and
the Appendix A/B language and proof boundaries.

For Theorem 1, the reviewer proved that the two-loop unreachable-state example
is serial and pointwise finitely branching, makes the source's initial-state
`p leadsto q` statement vacuously true, and makes every `P(u,n)` false.  It
then checked that requiring `S=X`, consistently restricting assertion/rule
semantics to `X`, or quantifying the theorem over executions from every start
repairs only that reachability mismatch.  None repairs the independent
deadlock-vacuity base failure; the manuscript adds neither family to Pnueli's
theorem.

## Adversarial publication and AGENTS review

- Canonical reviewer: `/root/mcnaughton_1966_research`.
- Role: omissions, unsupported additions, terminology, source standing,
  cross-presentation integration, citations, and the supplied five-part
  technical-name rule.
- Final verdict on the accepted snapshot: **ACCEPT**.

The final adversarial review reread the complete source and frozen scope and
found no remaining load-bearing omission, unsupported source assertion,
definition-before-use failure, technical-name violation, proof inflation,
provenance defect, version collapse, cross-file contradiction, or false status
claim.

Evidence digest: the reviewer checked necessity, exact eliminable definition
or source standing, standing, nonredundancy, and actual use for each local
technical name, including state assertion, temporal implication, the
parameterized assertion family and pointwise existential, full/partial
attachment, proper execution, restricted system validity, the proper-execution
language, and the eliminable omega-regular abbreviation.  It confirmed the
separation of Pnueli's material from Kamp, GPSS, Sistla--Clarke,
Alpern--Schneider, and later LTL-to-Büchi and PSPACE results.  Its premortem
identified the same four risks the accepted text now blocks: silently repairing
Theorem 1, treating S4 as a proof for the displayed linear semantics,
identifying the two fairness notions, or treating the author-hosted body as
IEEE-verified or licensed for republication.

## Revision history and final boundary

Six independent review-and-repair rounds were required.  No majority vote was
used, no supported finding was discarded, and an acceptance from an earlier
hash was never carried forward to a later snapshot.

1. The opening round returned three `REVISE` verdicts and produced F01--F16.
   The repairs supplied exact provenance and rights language; typed the program
   model, reachability, state assertions, P2, ER, and Theorem 1 assumptions;
   corrected Floyd direction and partial attachment; reconstructed recursive
   `F/G`, fairness, finite-state rules, Theorems 4--5, and Appendix A; and
   replaced premature closure prose.
2. Round two again returned three `REVISE` verdicts and produced F17--F26.
   The repairs typed location-indexed attachments; reconstructed the complete
   positive-capacity producer calculation; added DI/DN and the exact Theorem 3
   proof boundary; preserved Q1--Q4's unresolved range; disclosed P2's
   zero-rank typing repair and Theorem 1's deadlock-vacuity gap; and typed the
   complete Appendix B recursion and ownership chain.
3. Round three returned source-fidelity `ACCEPT` and two `REVISE` verdicts,
   producing F27--F35.  The repairs removed the action/load collision; defined
   full attachment; stated exactly the indicator implications used; separated
   arbitrary paths, proper executions, and restricted validity; parameterized
   the size comparison; supplied and owned the SCC equivalence; preserved
   Theorem 5's adequacy gap; and separated Appendix B's three proof owners.
4. Round four returned source-fidelity `ACCEPT` and two `REVISE` verdicts,
   producing F36--F40.  The repairs separated P2 totalization from soundness,
   supplied its independent zero-rank counterexample and limited repair,
   unified the R4/I parameter-family typing, restored the producer indicator
   implication, exposed Theorem 2's model-class issue, and embedded atomic
   states as one-letter words.
5. Round five returned source-fidelity and mathematical/proof `ACCEPT` but
   adversarial publication `REVISE`, producing F41--F43.  The final repairs
   added the serial unreachable-state failure in Theorem 1's first step,
   specified the complete three-world S4 Kripke model and valuation, and
   removed the unsupported fairness-strength comparison.
6. In round six, all three reviewers independently reread the full authority
   and artifact scope and returned **ACCEPT** on the exact common snapshot
   recorded above.

This establishes the three manuscript-content review gates and closes
body-level reader reconstruction only for `N-c-012.b`.  It does not silently
repair Pnueli's printed rules or sketches, prove the source's completeness
claims at a model class it did not specify, or compare the author-hosted body
with an IEEE-supplied file.

The IEEE-direct comparison, `N-c-012.c`, `N-c-012.d`, `N-c-012` as a whole,
Part IX admission, the single final publication build reserved until all
fourteen parts are text-frozen, rendered-page inspection, human review,
final-book completion, and user acceptance remain open.

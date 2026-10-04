# Board charter: Elgot 1961 for N-c-014.b

- Artifact: the frozen eight-object article/report/errata/manuscript snapshot below.
- Purpose: determine whether the handbook's N-c-014.b reconstruction of Calvin C. Elgot's 1961 article, complete 1959 report precursor, and controlling 1962 errata is source-faithful, mathematically correct, definition-before-use compliant, version-honest, and fit for graduate-handbook publication at the manuscript-content level.
- Mode: review.
- Requested by: the user's standing requirement that completed handbook topics receive three independent blind scholarly reviews before admission.
- Authorship disclosure: chair-authored reconstruction. The chair acquired and visually read the complete article, report, and errata, wrote the reader and source records, and supplied the explicit authority and correction boundary. No seated reviewer authored a frozen artifact.
- Severity taxonomy: blocker, must-fix, should-fix, consider, discard, unresolved-user.
- Source rule: every finding must cite an exact manuscript line and controlling printed source page. The source PDFs and their rendered pages, not OCR, control formulas, symbols, pagination, and wording.
- Consensus rule: admission requires every mandate to end with no unresolved blocker or must-fix and to file `VERDICT: ACCEPT` on one unchanged frozen snapshot. Supported findings cannot be outvoted.
- Board type: live.
- Workspace: `spec/research/boards/p09-elgot-1961/`.

## Frozen round-one snapshot

No frozen artifact may be edited while the round is open. Any content edit invalidates all verdicts and requires a new hash-pinned blind round.

| Artifact | Review scope | SHA-256 |
|---|---|---|
| `tmp/pdfs/p09-elgot-1961/elgot-1961-trans-ams.pdf` | complete 31-page official AMS journal facsimile, printed pp. 21–51 | `DE2F9587F72075C94C7071A00002D1129AA8148C498F9A4D6F75968EB46ACD74` |
| `tmp/pdfs/p09-elgot-1961/elgot-1959-umr1342.pdf` | complete 60-page Michigan report scan: cover/funding, front matter, numbered pp. 1–50, distribution leaves, endpoint | `596A599A7DF12F122BB2D875255B050695EC84A5A22F3488844D5876F3211D74` |
| `tmp/pdfs/p09-elgot-1961/elgot-1962-errata.pdf` | complete two-page published errata, printed pp. 558–559 | `B13E422FC03DDA61B93A1B782F40882AE90DBC8886945B26A42376A96ED34EC1` |
| `handbook/parts/p09/presentations/n-c-014.tex` | complete file, especially Elgot reconstruction at lines 231–463 and its nonconflation boundary | `C37C4F9F7D093D75DD33E90FBD6050C55F147B3C7A71933D8891D4DDF46AF20A` |
| `handbook/parts/p09/logic-in-computer-science.tex` | lines 811–816, shared finite-word correspondence theorem | `1690DED84FC257B50BC5B44E094E382D8A79B176E7BB9C21D0845DAEC59629B8` |
| `handbook/bib/handbook.bib` | lines 5843–5873, article, report, and errata identities | `6F98B6EB38B2B935DACC0C7E8373E1B12A5BB70FCAAC172D11BAFCDACA8C502F` |
| `spec/research/p09-elgot-1961-source-note.md` | complete lines 1–384 | `292B5EFD5972B27DC5043AF39FE20B1AB3ABE487290C3699031A79ED18472DA7` |
| `spec/research/p09-source-presentations-lot2-3.md` | N-c-014.b lines 632–644 and status/open-ledger lines 900–908 | `12CAA5ADB48E78D809F3EE6C8EA6FFBF98C504E0F7920A555DD9C378824ACAC7` |

The three text extractions are searchable reading aids only:

- journal: `tmp/pdfs/p09-elgot-1961/elgot-1961-trans-ams.txt`, SHA-256 `87B44F7DE47EDAA06292935A3D8B6A20423B2A0C224D3831778136CA7BD455F1`;
- report: `tmp/pdfs/p09-elgot-1961/elgot-1959-umr1342.txt`, SHA-256 `8A3B89CADC61AC950A315DDB82950DF3DE4CA40A68133872C48B000790BEBAF3`;
- errata: `tmp/pdfs/p09-elgot-1961/elgot-1962-errata.txt`, SHA-256 `6F6C906ABA6533399DC6EBF13646376621355B5FC18D3C2207B94FF051F7A621`.

They do not control a mathematical symbol. Visual reading aids are journal `rendered/page-01.jpg` through `page-31.jpg`, report `report-rendered/page-01.jpg` through `page-60.jpg`, and `elgot-1962-errata-page-1.jpg` through `elgot-1962-errata-page-2.jpg` under `tmp/pdfs/p09-elgot-1961/`. The PDFs remain the frozen source identities.

## Invariants

- I1: The complete 1961 journal article is the controlling body and the 1962 errata controls corrections. UMR1342 is a complete 1959 primary precursor, not permission to overwrite journal wording, pagination, or errors silently.
- I2: Every one of the 31 journal pages, 60 report pages, and two errata pages must be visually read. OCR cannot establish a formula, symbol, page boundary, or exact wording.
- I3: In §2, (I) is the finite nonempty input alphabet and (S) is the finite nonempty internal-state set. The acceptor is ((S,f,d,D)) with (f:I\times S\to S), (d\in S), and (D\subseteq S). Input alphabet, state set, transition, run, and accepted language have distinct standings.
- I4: In (L_1^1), individuals range over natural numbers and monadic variables over finite sets. This interpretation is not the arbitrary-set interpretation introduced in §8.6.
- I5: The characteristic-column encoding is cut after the last nonzero column, with the all-empty assignment encoded by (\Lambda). Admissibility, coordinate projection, and right truncation are different operations; projection alone is insufficient.
- I6: Theorem 5.3 has two effective directions. Formula-to-language uses Lemmas 5.4–5.5, Boolean regular operations, projection plus truncation, and local pattern expressions. Language-to-formula encodes accepting states in extra set coordinates and handles (\Lambda) separately.
- I7: Corollary 5.8 and §§5.9–5.16 retain their exact hypotheses and strength. Presburger decidability, the power-of-two expansion, and quasi-finite variants are consequences, not definitions of the automaton or blanket arithmetic decidability.
- I8: The later (A/B)-automaton is ((S,f,d,g)) with a total output map (g:S\to B). It is a deterministic synchronous transducer, not the earlier acceptor and not a Büchi automaton.
- I9: (A)-extendable, strongly (A)-extendable, and the largest regular sublanguage (\gamma_A\) are defined before use and retain distinct standings. Lemma 6.1's finite descending deletion construction establishes existence, effectiveness, and maximality.
- I10: Theorem 7.1 requires regularity, prefix closure, output functionality, and input totality, and its converse construction is effective.
- I11: Theorem 7.3 characterizes causal infinite transducer behavior by regular finite prefixes, prefix functionality, and input totality. It is not an omega-language acceptance theorem.
- I12: Theorem 8.1 is the exact (\gamma_A\neq\varnothing) realizability criterion. Corollary 8.2 is vacuously true when (\gamma_A=\varnothing) and otherwise compares opposite lexicographic selections.
- I13: Section 8.3 encodes a fixed transducer by an (L_1^1)-formula and reduces behavior containment to a truth question. Formula, automaton, and behavior language remain distinct.
- I14: The printed third sentence of §8.6.2 is false. No accepted argument may use its one-relation claim. The published finite-union and disjoint-tag correction is mandatory.
- I15: The erratum's exact correction makes (n) one more than the greatest successor offset, writes the unprojected set as (T^\infty_{m+m'+r}(\bigwedge_x M)=S_1\cup\cdots\cup S_k), permits (k\neq1), and projects one tagged relation language onto that union.
- I16: Theorem 8.6.3 may use Theorem 8.1 only after the corrected local-sequence representation and the finite-prefix construction have been established.
- I17: Chapter IV's Post-system encoding and Theorem 10.2 supply a genuine undecidability boundary. Corollary 10.6 distinguishes decidable satisfaction for a fixed input-free automaton from undecidable existence of some satisfying automaton.
- I18: Report/article agreements and differences are version evidence only. The report's already-correct (\widehat p), shared ((a,b)) error, and shared §8.6.2 error must be attributed exactly.
- I19: Source statement, source proof, printed error, published correction, chair paraphrase, and modern comparison must remain visibly separate.
- I20: Every new technical name must satisfy the repository AGENTS rule at first use: necessity, exact eliminable definition or axiom, standing, nonredundancy, and later use. Otherwise the text must state an owed artifact rather than name a hypothetical object.
- I21: Public repository or archival access is not an open-content licence. The local source files are research copies and no redistribution permission is inferred.
- I22: Acceptance is limited to N-c-014.b at the article-plus-errata strength stated here. It does not admit the untranslated Trakhtenbrot article, literal Büchi 1960 reconciliation, N-c-014 overall, Part IX, another part, a rendered handbook artifact, human review, book completion, or user acceptance.
- I23: This is book scholarship, not software engineering. No test, test harness, automated checker, repository script, TeX command, interim handbook build, or handbook-PDF inspection may be used or claimed. Permitted evidence is source-page visual reading, direct manuscript reading, mathematical derivation, citation/provenance inspection, and SHA-256 labels for snapshot identity.
- I24: Opening seats are blind. They may not read the ledger, chair transcript, the Büchi board, any other board transcript, another current transcript, or another verdict, and may not contact one another.

## Mandatory coverage points

- M01: recompute all eight frozen hashes before substantive review.
- M02: visually read all 31 journal pages, all 60 report pages, and both errata pages; confirm each physical and printed-page map.
- M03: verify article, report, and errata identities, dates, series, DOI/handle, access routes, authority order, and rights qualification.
- M04: verify the exact §2 acceptor tuple, every type, the run recursion, the final-state convention, and the empty-word case.
- M05: verify §§3–4 regularity and right truncation, including the p. 23 projection-symbol correction and p. 24 ordered-pair correction.
- M06: verify the syntax and interpretation of (L_1^1), including individual/set domains and the standing of formulas versus assignments.
- M07: verify (U_r), (U_r^0), (0_r), admissible words, (T_r(A)), the all-empty case, and canonical removal of terminal zero columns.
- M08: independently rederive Theorem 5.3(a), including Lemmas 5.4–5.5, local principal patterns, Boolean operations, existential set projection, and right truncation.
- M09: independently rederive Theorem 5.3(b), including state coding, start and terminal sets, the local adjacency relation, existential state-coordinate removal, and the (\Lambda) case.
- M10: verify Corollary 5.8, the finite-set binary-expansion map, the finite carry relation, Presburger consequence, power-of-two extension, and finite/quasi-finite variants at exact strength.
- M11: verify the (A/B)-automaton tuple, synchronous finite behavior, and the distinction from the §2 acceptor.
- M12: independently verify Lemma 6.1's deletion construction, stabilization, strong extendability, regularity, effectiveness, and largest-sublanguage claim.
- M13: independently verify every necessity and sufficiency clause of Theorem 7.1 and the effective converse construction.
- M14: independently verify Theorem 7.3, especially why its three conditions imply (\lim(\alpha^L)=\alpha), and preserve the non-Büchi boundary.
- M15: independently verify Theorem 8.1, its lexicographic selection argument, Corollary 8.2's empty and nonempty cases, and the exact uniqueness criterion.
- M16: verify §8.3's formula encoding and the behavior-containment truth reduction without identifying formulas and machines.
- M17: verify §8.6's arbitrary-set interpretation, restricted formula form, forbidden equality/order, allowed numerals, and successor-offset convention.
- M18: read the 1962 errata directly and verify all six listed corrections, the (k=2) counterexample, the finite-union statement, the disjoint tagged fields, tagged prefix sets, relation union, and projection equality.
- M19: independently verify that the corrected §8.6.2 plus §8.5 makes Theorem 8.6.3's reduction to Theorem 8.1 sound.
- M20: verify Lemma 10.1, Theorem 10.2, §§10.3–10.5, and Corollary 10.6 at the exact stated positive/negative boundary.
- M21: compare the complete report with the article at every claim used; verify sameness claims, pagination distinction, (\widehat p/\widehat f), ((a,b)/(b,a)), and shared §8.6.2 defect.
- M22: reconcile every reader claim with the source note, compact record, shared theorem, bibliography, open ledger, and source-sufficiency statement.
- M23: audit every locator, theorem number, cross-reference, citation, historical attribution, and source-versus-modern qualification.
- M24: apply the complete AGENTS terminology rule and report every definition-after-use, redundant name, standing ambiguity, or unused distinction.
- M25: adversarially inspect for a false compression, hidden hypothesis, source laundering, correction laundering, misleading singular/plural, empty-case omission, or completion inflation that a graduate reader could expose.
- M26: enforce the topic-only scope, rights boundary, and explicit no-test/no-build boundary.

## Roster and role cards

### Source fidelity and evidence seat

- Mandate: determine whether every manuscript and record claim is supported at its stated strength by the complete article, report, and errata, and whether every version, correction, access, and rights qualifier is honest.
- Coverage: M01–M07, M10–M11, and M17–M26, with special attention to literal formulas, locators, authority order, bibliography, and proof ownership.
- Evidence: controlling printed page plus exact manuscript line for every finding.
- Blind spot to avoid: accepting a correct modern paraphrase as Elgot's wording, using OCR as formula evidence, or treating precursor content as automatically corrected journal content.

### Mathematical and proof-correctness seat

- Mandate: independently rederive every regularity, encoding, reverse-definition, transducer, maximal-sublanguage, synthesis, corrected infinite-specification, and undecidability argument used by the manuscript.
- Coverage: M04–M20 and M25, especially M08–M19 and edge cases involving (r=0), (\Lambda), terminal zero columns, (\gamma_A=\varnothing), finite prefixes, and (k>1).
- Evidence: explicit derivation or minimal counterexample tied to source and manuscript locations.
- Blind spot to avoid: accepting the familiar modern regular/MSO theorem or Church-synthesis folklore without checking Elgot's literal encoding, truncation, causal behavior, and published repair.

### Adversarial publication and terminology seat

- Mandate: determine whether a hostile expert reader could expose ambiguity, source laundering, correction laundering, invented terminology, definition-after-use, silent 1959/1961/1962 conflation, or premature completion language.
- Coverage: M01–M26, emphasizing I1–I24 and the AGENTS terminology rule.
- Evidence: exact location, violated invariant, concrete reader harm, and the smallest exact correction.
- Blind spot to avoid: aesthetic preference, speculative expansion, or demanding a modern result the historical presentation does not need.

The three existing board agents are reseated for this new artifact. No seat is shown another seat's output during the blind opening.

## Opening-round filing rule

Each seat writes only its assigned file under `transcript/` and ends with:

- `VERDICT: ACCEPT` if no blocker or must-fix remains for its mandate; or
- `VERDICT: REJECT — <exact blocking finding identifiers>`.

Every mandatory coverage point in the seat's mandate must be marked checked-clean, finding-linked, or not-checked with reason. A reviewer may not edit any frozen artifact, ledger, chair record, or another transcript. No reviewer may run a test, automated check, script, TeX command, interim build, or handbook-PDF inspection.

## Round 1 disposition

Round 1 closed **REJECT** after all three blind reports were filed.  The
source-fidelity and adversarial-publication seats accepted.  The mathematical
seat rejected on three supported must-fix findings:

- `MP-01`: the reader replaced §8.6's literal syntactic restrictions by the
  undefined word “local”;
- `MP-02`: the reader displayed only a binary tagged relation and did not
  justify general arity or the possible unary-window case; and
- `MP-03`: the report comparison said one already-correct projection occurrence
  although report p. 4 has both.

No finding was outvoted.  The round-one reports remain immutable evidence in
`transcript/r1-*.md`.

## Frozen round-two snapshot

The chair revised only the findings and their status records.  Round 2 freezes
the following eight objects.  No frozen object may be edited while Round 2 is
open.

| Artifact | Round-two review scope | SHA-256 |
|---|---|---|
| `tmp/pdfs/p09-elgot-1961/elgot-1961-trans-ams.pdf` | unchanged controlling 31-page article | `DE2F9587F72075C94C7071A00002D1129AA8148C498F9A4D6F75968EB46ACD74` |
| `tmp/pdfs/p09-elgot-1961/elgot-1959-umr1342.pdf` | unchanged complete report precursor | `596A599A7DF12F122BB2D875255B050695EC84A5A22F3488844D5876F3211D74` |
| `tmp/pdfs/p09-elgot-1961/elgot-1962-errata.pdf` | unchanged controlling published correction | `B13E422FC03DDA61B93A1B782F40882AE90DBC8886945B26A42376A96ED34EC1` |
| `handbook/parts/p09/presentations/n-c-014.tex` | revised §8.6 and report comparison, especially lines 403–463 and 477–484 | `33A2CD747DBDFA356F5505E88CBF798D426C5B5971003E0449805BCDF93F86FA` |
| `handbook/parts/p09/logic-in-computer-science.tex` | unchanged shared theorem | `1690DED84FC257B50BC5B44E094E382D8A79B176E7BB9C21D0845DAEC59629B8` |
| `handbook/bib/handbook.bib` | unchanged Elgot bibliography identities | `6F98B6EB38B2B935DACC0C7E8373E1B12A5BB70FCAAC172D11BAFCDACA8C502F` |
| `spec/research/p09-elgot-1961-source-note.md` | revised arity-safe correction and Round 1 disposition | `1A34AC4E992C00A0E917256CF5DB58A7C48A971FBF47F7F217B25D0DDAF18331` |
| `spec/research/p09-source-presentations-lot2-3.md` | revised N-c-014.b review status | `34D4B1AC65B78EAD14AB60335C94C8FFEA2F00778B963956038485DFB50EC438` |

### Exact revisions to verify

- `R2-C01` (`MP-01`): reader lines 410–425 now state that (M) is
  quantifier-free, has only the displayed variables free, may contain numerals,
  contains neither equality nor order, uses successor iterates
  (x^{(h)},0^{(h)}), and has
  (n=1+\max h) over their occurrences.  No undefined “local” designation
  carries a proof obligation.
- `R2-C02` (`MP-02`): reader lines 434–463 now define (R'_j)
  componentwise for (n\geq2), use overlapping windows to prove tag
  constancy, and treat (n=1) by replacing unary (R_j) with
  (R_j\times R_j) before tagging.  The text labels the unary completion as
  handbook-owned rather than wording of the erratum.  The source note records
  the same boundary.
- `R2-C03` (`MP-03`): reader line 480 now says the report has
  \(\widehat p\) at both corresponding occurrences.

### Round-two mandate and filing rule

The same three independent seats are reseated.  Each reviewer may rely on that
reviewer's own complete Round 1 source pass, but may not read another seat's
Round 1 or Round 2 report, the ledger, or the chair transcript.  Each must:

1. recompute all eight Round 2 hashes;
2. inspect the revised passages and their immediate dependencies directly;
3. re-inspect journal p. 46, report pp. 4 and 41, and errata pp. 558–559 at
   original detail;
4. verify `R2-C01`–`R2-C03`, including an independent proof that the
   (n=1) promotion defines the same infinite sequences and makes the tagged
   projection equality valid; and
5. inspect for collateral source, mathematical, terminology, or
   correction-ownership defects introduced by the revision.

Each seat writes only its corresponding `transcript/r2-*.md` file and ends with
exactly `VERDICT: ACCEPT` or
`VERDICT: REJECT — <exact blocking finding identifiers>`.  Admission requires
three accepts on these exact hashes and no unresolved blocker or must-fix.
Round 2 remains book scholarship: no test, automated checker, repository
script, TeX command, interim build, or handbook-PDF inspection is authorized.

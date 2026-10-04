# N-c-012.d independent manuscript review record

## Admission scope

This record closes reader-facing body reconstruction and the three independent
manuscript-content review gates for exactly `N-c-012.d`: A. Prasad Sistla and
Edmund M. Clarke's 1985 presentation, “The Complexity of Propositional Linear
Temporal Logics.” Its principal reader scope begins at
`\subsubsection{Sistla--Clarke's operator-sensitive complexity boundary}` in
`handbook/parts/p09/presentations/n-c-012.tex` and ends immediately before the
Alpern--Schneider presentation. The necessary shared Part IX complexity and
model-checking theorems, separate 1982 and 1985 bibliography records, complete
source note, and compact source-presentation record were reviewed with it.

Acceptance does not certify every statement printed by the article as correct.
The accepted presentation expressly preserves and distinguishes:

- the two printed strict acceptable-subsequence inequalities whose null cases
  fail while the following proof uses non-strict inequalities;
- the Theorem 3.5 prefix word “after,” whose current-inclusive reading is
  forced by the article's own semantics and proof context;
- the literal Theorem 3.5 strong-connectivity/entry-edge check, its
  loopless-singleton soundness gap, and the separately owned handbook
  directed-cycle correction;
- the p. 745 finite/infinite indexing defect and the printed
  `N_0 -> a_1 a_2 N_0` even/zero-based-odd conflict;
- the conclusion's statement that an unidentified theorem used in the
  conference proof contained an error, without inventing a precise bad
  inference or unique repairing lemma; and
- the source's reuse of `n` for two independent quantities, resolved only by
  the handbook's explicit alpha-renaming of total encoded input length to
  `ell_in` while retaining `n` as grammar-terminal count and constructor
  arity.

Acceptance means those source statements, defects, reconstructions,
handbook-owned corrections, proof-strength limits, version boundaries, and
rights limits are themselves presented accurately.

This record does not admit Alpern--Schneider, `N-c-012` as a whole, Part IX,
any other handbook part, the final generated handbook, rendered-page
inspection, human review, final-book completion, or user acceptance.

## Exact accepted snapshot

All three final reviewers accepted the following exact pre-admission
ten-object snapshot:

| Artifact | SHA-256 |
|---|---|
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf` | `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5` |
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf` | `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png` | `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png` | `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-04-acceptable-crop.png` | `C267D4B4DF785F9A7E82123B068662E45D7E2C87CB18C24D7B8EB0B875AF413B` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `C25353424D7DF38678F8AAC7BB421DD1DCCF2E1289643E114425D0F2BEA31DEA` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` |
| `handbook/bib/handbook.bib` | `F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B` |
| `spec/research/p09-sistla-clarke-1985-source-note.md` | `9390C6A525C88E247BC5C892B4522EDF1CCECA466DA577DDAC1230E3A350FA4B` |
| `spec/research/p09-source-presentations-lot2-3.md` | `1F36F2BCAFE8E1BB8599610EA1ECAAC7E204CC7847674696E9A50D0F3F8918B5` |

The compact source-presentation hash is the pre-admission status surface read
by all three reviewers. Its subsequent status-only edit records their
unanimous verdict and links this review record. The resulting post-admission
hash is
`FD3644BBDC3F70ADAB402D13913A80255B5E14033B4ACD4355694704EB88E61D`.
That edit changes no reader-facing mathematics, source claim, bibliography,
or source note. The accepted reader and complete source note remain
byte-identical to the reviewed snapshot.

## Primary authority surface

The controlling authority was the complete seventeen-page journal facsimile:

- A. Prasad Sistla and Edmund M. Clarke, “The Complexity of Propositional
  Linear Temporal Logics,” `Journal of the ACM` 32(3) (July 1985),
  pp. 733--749;
- DOI `10.1145/3828.3837`;
- local object
  `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf`;
- controlling SHA-256
  `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5`.

The distinct ten-page 1982 STOC predecessor was also reviewed in full:

- A. Prasad Sistla and Edmund M. Clarke, the same title, `Proceedings of the
  Fourteenth Annual ACM Symposium on Theory of Computing`, pp. 159--168;
- DOI `10.1145/800070.802189`;
- local object
  `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf`;
- controlling SHA-256
  `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283`.

Every final reviewer visually read all seventeen journal pages and all ten
conference pages. The three frozen enlarged derivatives resolved the faint
p. 742 exponent, the p. 736 strict acceptable-union sign, and the p. 745 ETL
defects. The PDFs controlled identity; page images were reading aids, not
substitute authorities.

Printed p. 733 carries ACM's conditional copying terms, not an open-content
licence. The handbook therefore uses independently written scholarly
reconstruction and does not republish the source scans or protected
expression.

## Reviewer transcripts, runtime, and independence

| Seat | Canonical reviewer | Final transcript | Transcript SHA-256 | Verdict |
|---|---|---|---|---|
| source fidelity | `/root/r6_source_fidelity` | `spec/research/boards/p09-n-c-012d/transcript/r6-source-fidelity.md` | `30C808BE930AE34892BA0B2D27A6A4B850E87D9F1D0ADF47E5F575B2450C39E3` | **ACCEPT** |
| mathematical/proof correctness | `/root/r6_mathematical_proof` | `spec/research/boards/p09-n-c-012d/transcript/r6-mathematical-proof.md` | `39B341A10610CDB93D68ED7E3C1C97192BDED250A5D80F22000466A2C830A0F9` | **ACCEPT** |
| adversarial publication/AGENTS | `/root/r6_adversarial_publication` | `spec/research/boards/p09-n-c-012d/transcript/r6-adversarial-publication.md` | `7220F7C25BA966668D0C02E8C74FC5CF5B4389A744DC7D639B59B5C941AC7CF3` | **ACCEPT** |

The runtime did not expose an exact serving model, deployment version, or
build identifier to any final seat; that absence is recorded rather than
guessed.

Each reviewer was a fresh direct child of the chair with no inherited turn
history. Each was instructed to read the complete charter, frozen topic scope,
and every authority page; not to read the ledger, chair record, any earlier or
concurrent transcript, or another verdict; not to contact another seat; and
not to edit a frozen artifact. Each wrote only its assigned transcript. The
chair kept filed transcripts sealed until all three were complete, then read
all three in full.

Every reviewer independently computed all ten frozen identities before
substantive review; the source and mathematical seats repeated the identity
check before filing. After all reports were complete, the chair independently
recomputed all ten frozen identities and all three transcript hashes. Every
value matched.

This was manuscript scholarship, not software engineering. No reviewer and no
chair operation used a test, test harness, automated checker, repository
script, TeX command, handbook-PDF inspection, or build. Primary-source visual
reading, direct text inspection, mathematical reasoning, provenance
inspection, and SHA-256 identity labels were the review methods. These
manuscript-content reviews establish no compilation or rendered-page result.

## Source-fidelity review

The source-fidelity seat freshly read every authority page and all frozen
reader/source surfaces. It accepted the exact identity, bibliographic and
rights boundary, syntax and inclusive semantics, existential `R`-truth
quantifier, journal-relative validity reconstruction, complete Section 3
certificate, exact Section 4 reductions and periodic obligations, corrected
journal ETL chain, Table I, and conference/journal separation.

It specifically verified:

- `SF(f)` is defined before the Theorem 3.5 certificate and is not confused
  with the later realized truth-set count;
- `q_0:=\delta` binds the supplied start state on every surface;
- “after” remains source-visible but is rendered current-inclusive as required
  by the article's own semantics and p. 737 proof use;
- the literal singleton-cycle gap and handbook-owned directed-cycle condition
  are separate;
- arity `n` and total encoded input length `ell_in` are distinct and stable;
  and
- no article result is retrofitted with a Büchi-automaton proof.

It found no remaining source discrepancy, unread page, locator failure,
version conflation, unsupported attribution, silent source repair, proof
promotion, or rights overclaim.

## Mathematical and proof review

The mathematical seat independently reconstructed the full proof surface and
recomputed the disclosed counterexamples. It confirmed:

- the null/null cases refute the two printed strict inequalities while the
  article's proof supports the non-strict statements;
- the two-state `A and FA` example refutes a strict current-excluding reading
  of the prefix word “after”;
- the loopless-singleton `GP` example passes the literal reflexive
  strong-connectivity test but cannot support the claimed infinite recurrent
  suffix;
- complete valuation periodicity, source-truth-set equality, until discharge,
  and negated-grammar tree termination are genuinely different obligations;
- the direction-sensitive `U` and `S` recurrences, initial-since rule, loop
  closure, and Savitch step have the stated source strength; and
- the `n`-ary ETL constructor remains well typed while `ell_in` alone measures
  the complete encoded input.

It found no remaining type error, quantifier error, invalid handbook
calculation, unsupported theorem strength, proof-ownership error, or
counterexample to the repaired handbook claims.

## Adversarial publication and terminology review

The adversarial seat reread every source and frozen surface, inspected the
adjacent topic boundaries, and tried to falsify source identity, theorem
domains, formula direction, proof ownership, status language, cross-file
consistency, and terminology standing.

It checked the five-part technical-name rule locally for `SF(f)`, acceptable
subsequence and ambient subscripts, `mu(f)`, the start alias and certificate
labels, Lemma 4.3 auxiliaries, source truth sets, both fulfillment obligations,
successive guesses `A,B`, the ETL constructor, `Gamma`, `ell_in`, the
continuation set, and the compact tuple abbreviation. Each has stated
necessity, exact definition or source standing, object/relation/metalinguistic
standing, nonredundancy, and actual use. No owed artifact was prematurely
replaced by a hypothetical name.

It found no omitted qualification, unsupported addition, silent
strengthening, hidden repair, cross-file contradiction, provenance defect, or
publication-blocking terminology problem.

## Revision history and closure of admitted findings

Six blind review rounds were required. No majority vote was used, no supported
finding was discarded, and no acceptance from an earlier hash was carried
forward to a changed snapshot.

1. Round one returned three `REVISE` verdicts. Repairs corrected the page map,
   restored the conference validity clause as predecessor evidence, calibrated
   the correction notice, defined the Figure 2 encoding unit, restored exact
   valuation periodicity and Lemma 3.2/3.3/3.6 quantifiers, recorded terminal
   persistence, and removed unsupported tree synonyms.
2. Round two returned source-fidelity `ACCEPT` and two `REVISE` verdicts.
   Repairs defined the Section 3 structure and acceptable-subsequence
   measures before use, defined `mu(f)`, restored the exact Theorem 3.5
   certificate, and added the separate conference bibliography/citation
   surface.
3. Round three returned three `REVISE` verdicts. Repairs corrected the p. 741
   `2S(n)` locator, restored every Theorem 3.5 labelling rule and disclosed the
   loopless-singleton gap, supplied the exact Lemma 4.3/4.5/4.6 and Theorem
   4.1 machinery, and restored the exact Lemma 5.2/Theorem 5.4 rules.
4. Round four returned source-fidelity `ACCEPT` and two `REVISE` verdicts.
   Repairs moved the exact `SF(f)` definition before use, bound `q_0` to the
   supplied start state, made the prefix `F` witness current-inclusive while
   preserving the printed word, and bound one ETL arity across all surfaces.
5. Round five returned three `REVISE` verdicts. All three seats independently
   found that `n` had then been rebound as total encoded input length
   immediately before the `n`-ary Theorem 5.4 schemas. The final repair kept
   `n` as terminal/constructor arity and introduced the exact metalinguistic
   input-length variable `ell_in` on all three surfaces.
6. In round six, all three fresh reviewers reread all twenty-seven authority
   pages and the complete frozen scope and independently returned **ACCEPT**
   on the exact common ten-object snapshot recorded above. The chair then read
   all three transcripts in full and independently confirmed every hash.

Every supported finding is therefore incorporated and accepted for this exact
snapshot. Nothing in this admission asserts that the authors supplied the
handbook's directed-cycle correction, that either printed strict inequality is
valid in its null case, that the p. 745 ETL example is internally coherent, or
that the article identifies the exact conference-proof error.

## Final limited disposition

This closes body-level reader reconstruction and topic-level manuscript review
only for `N-c-012.d`. Alpern--Schneider, `N-c-012` overall, Part IX
admission, the other thirteen parts, the single final publication build
reserved until all fourteen parts are text-frozen, rendered-page inspection,
human review, final-book completion, and user acceptance remain open.

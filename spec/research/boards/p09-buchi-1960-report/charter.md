# Board charter: Büchi 1959 report precursor for N-c-014.a

- Artifact: the frozen six-object manuscript/source snapshot below.
- Purpose: determine whether the handbook's N-c-014.a reconstruction of J. Richard Büchi's 1959 technical report precursor is source-faithful, mathematically correct, definition-before-use compliant, version-honest, and fit for graduate-handbook publication at the manuscript-content level.
- Mode: review.
- Requested by: the user's standing requirement that completed handbook topics receive three independent blind scholarly reviews before admission.
- Authorship disclosure: chair-authored reconstruction. The chair acquired and visually read the complete report, wrote the reader and source records, and supplied the explicitly labelled version boundary. No seated reviewer authored a frozen artifact.
- Severity taxonomy: blocker, must-fix, should-fix, consider, discard, unresolved-user.
- Source rule: every finding must cite an exact manuscript line and printed report page. The rendered report pages, not the repository OCR, control formulas, symbols, pagination, and wording.
- Consensus rule: admission requires every mandate to end with no unresolved blocker or must-fix and to file ACCEPT on one unchanged frozen snapshot. Supported findings cannot be outvoted.
- Board type: live.
- Workspace: spec/research/boards/p09-buchi-1960-report/.

## Frozen round-one snapshot

No frozen artifact may be edited while the round is open. Any content edit invalidates all verdicts and requires a new hash-pinned blind round.

| Artifact | Review scope | SHA-256 |
|---|---|---|
| tmp/pdfs/p09-buchi-1960/buchi-1959-umr1083.pdf | complete 48-page acquired report scan: cover, funding leaf, numbered pp. 1–45, endpoint leaf | 18D1BF4C44E9581932239B500DA8E220876AD7F9B602451BF6B9B22795F840FD |
| handbook/parts/p09/presentations/n-c-014.tex | lines 1–213, especially the Büchi reconstruction at lines 8–166 and its version/non-conflation boundary | 1D4E34CE6B2602BEF520146ECC6F78C492A969CE6C8FE884912DC0959AFF6713 |
| handbook/parts/p09/logic-in-computer-science.tex | lines 811–816, shared finite-word correspondence theorem | 1690DED84FC257B50BC5B44E094E382D8A79B176E7BB9C21D0845DAEC59629B8 |
| handbook/bib/handbook.bib | lines 6099–6120, report and journal identities | FAACDA885C9671FD41509F0FCB24934CBA0B4AFD8BC1E6368C2DE355E8B03DFA |
| spec/research/p09-buchi-1960-source-note.md | complete lines 1–318 | 15165056F88D051DB0A5CB33B3C55A79F39AF2EEE62C507C756226CF851B411E |
| spec/research/p09-source-presentations-lot2-3.md | compact N-c-014.a record at lines 620–630 and its narrowed open/sufficient-body ledger entries | E7DD8167EA70A32F72F09C12A478637F8C5ECCB3C7AA6E98BCC7918ECFB00285 |

The repository OCR at tmp/pdfs/p09-buchi-1960/buchi-1959-umr1083.txt is a searchable reading aid only. Its SHA-256 is 9AD26515AE6689320FC031030C361842DDDD30067FF94E2F7D9324DF758599D1. It does not control a mathematical symbol.

The visual reading aids are page-01.jpg through page-48.jpg and contact-01-09.jpg through contact-40-48.jpg under tmp/pdfs/p09-buchi-1960/rendered/. The PDF remains the frozen source identity.

## Invariants

- I1: The complete September 1959 UMR1083 report is the controlling mathematical source. The registered 1960 journal article remains unreconciled. Report content may not be presented as verified journal wording, numbering, pagination, or revision state.
- I2: Every report page must be visually read. OCR cannot establish a formula, symbol, page boundary, or exact wording.
- I3: Weak means monadic predicate variables range over special predicates, predicates eventually false and hence finite sets. It is not a quantifier-alternation fragment and not Büchi's later full-set infinite-word system.
- I4: \(W.2.A.\) is an interpreted language/theory without a supplied deductive calculus. A special predicate, \(n\)-predicate, formula tuple, transit predicate, output predicate, and behavior set must retain distinct standings.
- I5: The source automaton is the propositional-formula data \(E^m,H^m[Y^m,X^n]\), inducing a deterministic bit-state recursion. A modern set/function or nondeterministic tuple cannot be attributed as the source object.
- I6: A special output is relative to \(E,H\) and satisfies the exact printed stability identity. Behavior is eventual permanent truth on special inputs; string behavior is arbitrary-output truth at the encoded finite endpoint. These may not be conflated.
- I7: Lemma 1, Lemmas 2–7, Theorems 1–4, Theorems 6–9, Corollaries 1–5, and Section 8 must be reported at their actual proof strength and with their actual dependencies.
- I8: Complement, conversion to expanded presentation, existential input removal, and the local base construction have different roles. The manuscript may not flatten them into generic Boolean closure/projection language that loses the source construction.
- I9: Theorem 2's restriction of transit witnesses to special predicates is a substantive argument depending on special output.
- I10: The sentence decision proof is the finite-state path/loop-deletion argument after normal form. No later complexity claim or general theorem may replace it.
- I11: The finite-word encoding includes an explicit terminal \(\top^n\) marker followed by the all-false tail; the empty word has the marker at zero. Source length conventions may not hide this position.
- I12: Theorem 8's four equivalent conditions and Theorem 8′'s extension from sets to relations require their exact defined standings.
- I13: The binary-expansion map from finite predicates to natural numbers is explicit. Definability in \(W.2.A.\) and first-order \([=,+,\operatorname{Pw}_2]\) is related through that map, not by untyped identification.
- I14: Ultimately periodic unary sets, base-dependent regularity, the binary-to-ternary nonexistence consequence, and finite-set quantification as feedback/Kleene star must remain distinct claims.
- I15: Source statement, source proof, source-cited dependency, chair reconstruction, modern comparison, and journal-version claim must remain visibly separate.
- I16: Every new technical name must satisfy the repository AGENTS rule at its first use: necessity, exact definition or axiom, standing, nonredundancy, and later use. Otherwise the text must state an owed artifact rather than naming a hypothetical object.
- I17: Public repository access is not an open-content licence. The source is a research copy and no redistribution permission is inferred.
- I18: Acceptance is limited to the 1959-report-strength N-c-014.a presentation. It does not admit the unreconciled 1960 journal version, Elgot, Trakhtenbrot, N-c-014 overall, Part IX, another part, a rendered handbook artifact, human review, book completion, or user acceptance.
- I19: This is book scholarship, not software engineering. No test, test harness, automated checker, repository script, TeX command, interim handbook build, or handbook-PDF inspection may be used or claimed. Permitted evidence is source-page visual reading, direct manuscript reading, mathematical derivation, citation/provenance inspection, and SHA-256 labels for snapshot identity.
- I20: Opening seats are blind. They may not read the ledger, chair transcript, the p09-buchi-1962 board, any other board transcript, another current transcript, or another verdict, and may not contact one another.

## Mandatory coverage points

- M01: recompute all six frozen hashes before substantive review.
- M02: visually read all 48 report pages and confirm the cover/funding/pp. 1–45/endpoint map.
- M03: verify report identity, institutional series, date, repository identifier, article identity, DOI, report/article/reprint boundary, access route, and rights qualification.
- M04: verify all variable sorts, natural-number domain, zero/successor vocabulary, predicate domain, special-predicate definition, \(n\)-predicate standing, and the absence of a deductive calculus.
- M05: verify Definition 1's exact automaton data, the transition recursion, binary output, and deterministic bit-state standing.
- M06: verify Definition 2's exact special-output identity and its stated eventual-constancy consequence.
- M07: verify Definition 3's behavior, its quantifiers, and the distinction between a special input, output predicate, and accepted behavior set.
- M08: verify Lemma 1's local normal form and the five-step proof architecture recorded in the source note.
- M09: verify Lemmas 2–7, including complement, expanded presentation, guessed input track, finite look-ahead output, existential input removal, and local base automaton.
- M10: independently rederive Theorem 1's synthesis construction through an arbitrary finite-set quantifier prefix.
- M11: independently rederive Theorem 2's analysis formula, including the cutoff predicate and why the transit witness can remain special.
- M12: verify Definition 5, Theorem 3's treatment of free individuals, and Corollary 1's exact finite path/loop-deletion decision argument and edge cases.
- M13: verify Corollary 2 in both directions and the claim that phase and period are effectively obtainable.
- M14: verify the finite-predicate binary-expansion bijection, Theorem 4's two translations, the carry predicate, the \(\operatorname{Pw}_2\) bit test, and Corollary 5.
- M15: verify the exact finite-word encoding, including the empty word, data positions, terminal marker, false tail, and source length convention.
- M16: verify Definition 6 and both directions of Theorem 6; ensure behavior and string behavior are not conflated.
- M17: verify Theorems 7–8, all four equivalent conditions, the effective direction claims, and the dependence on the already-cited regular-language theorem.
- M18: verify Theorem 8′, the defined standing of regular relations, the binary-expansion regularity discussion, and the base-\(k\)/base-\(n\) consequences used.
- M19: verify Section 8's union, concatenation, star, feedback, and finite-set-quantifier comparison at the exact printed strength.
- M20: reconcile every reader formula and claim with the source note, compact record, shared theorem, bibliography, narrowed open ledger, and source-sufficiency statement.
- M21: audit every page locator, theorem number, cross-reference, and source-versus-modern attribution.
- M22: apply the complete AGENTS terminology rule and report every definition-after-use, redundant name, standing ambiguity, or unused distinction.
- M23: adversarially test the report/journal version boundary for source laundering, completion inflation, or a claim which should remain conditional.
- M24: inspect prose for a mathematically material ambiguity, false compression, hidden hypothesis, misleading plural/singular, or endpoint convention that a graduate reader could misread.
- M25: enforce the topic-only scope, rights boundary, and explicit no-test/no-build boundary.

## Roster and role cards

### Source fidelity and evidence seat

- Mandate: determine whether every manuscript and record claim is supported at its stated strength by the complete 1959 report and whether every version/rights qualifier is honest.
- Coverage: M01–M09 and M12–M25, with special attention to literal formulae, locators, report/article separation, bibliography, proof ownership, and source-dependent terminology.
- Evidence: printed report page plus exact manuscript line for every finding.
- Blind spot to avoid: accepting a correct modern paraphrase as source wording or treating report content as automatically verified journal content.

### Mathematical and proof-correctness seat

- Mandate: independently rederive every normal-form, automaton, projection, analysis, finite-decision, periodicity, binary-expansion, and finite-word equivalence argument used by the manuscript.
- Coverage: M04–M19 and M24, especially M08–M18 and edge cases involving the empty word, all-false input, repeated states, cutoff witnesses, and unused bit states.
- Evidence: explicit derivation or minimal counterexample tied to source and manuscript locations.
- Blind spot to avoid: accepting the familiar modern regular/MSO theorem without checking Büchi's special-output and terminal-marker formalism.

### Adversarial publication and terminology seat

- Mandate: determine whether a hostile expert reader could expose ambiguity, source laundering, invented terminology, definition-after-use, silent 1959/1960 conflation, scope inflation, or premature completion language.
- Coverage: M01–M25, emphasizing I1–I20 and the AGENTS terminology rule.
- Evidence: exact location, violated invariant, concrete reader harm, and the smallest exact correction.
- Blind spot to avoid: aesthetic preference, speculative expansion, or demanding a modern result the historical presentation does not need.

The three existing board agents are reseated for this new artifact. No seat is shown another seat's output during the blind opening.

## Opening-round filing rule

Each seat writes only its assigned file under transcript/ and ends with:

- VERDICT: ACCEPT if no blocker or must-fix remains for its mandate; or
- VERDICT: REJECT followed by the exact blocking finding identifiers.

Every mandatory coverage point in the seat's mandate must be marked checked-clean, finding-linked, or not-checked with reason. A reviewer may not edit any frozen artifact, ledger, chair record, or another transcript.


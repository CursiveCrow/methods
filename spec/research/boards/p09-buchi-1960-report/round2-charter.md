# Round-two board charter: corrected Büchi 1959 report presentation

- Artifact: the corrected six-object snapshot below, read with the fixed later-correction source.
- Purpose: determine whether the N-c-014.a presentation now distinguishes exact report content, defects in that content, handbook-owned repair, later correction history, and the unreconciled 1960 journal version with mathematical and publication-level accuracy.
- Mode: review.
- Severity taxonomy: blocker, must-fix, should-fix, consider, discard, unresolved-user.
- Consensus rule: admission requires all three seats to file `VERDICT: ACCEPT` on this one unchanged snapshot, with no unresolved blocker or must-fix. Supported findings cannot be outvoted.
- Source rule: the rendered 1959 scan controls report wording and formulas; Bruyère--Hansel--Michaux--Villemaire (1994), printed pp. 202–203, controls the later arithmetic-correction history. OCR is search aid only.
- Board type: live.

## Frozen round-two snapshot

No frozen artifact may be edited while this round is open. Any content edit voids every round-two verdict and requires a new hash-pinned round.

| Artifact | Review scope | SHA-256 |
|---|---|---|
| tmp/pdfs/p09-buchi-1960/buchi-1959-umr1083.pdf | complete 48-page report scan | 18D1BF4C44E9581932239B500DA8E220876AD7F9B602451BF6B9B22795F840FD |
| handbook/parts/p09/presentations/n-c-014.tex | lines 1–257, the complete corrected Büchi report presentation and its boundary | 843C9FAE64849F6AE57239B05084D7C43D41095512439F00A3AA3F0EB0B208D6 |
| handbook/parts/p09/logic-in-computer-science.tex | lines 811–816, shared finite-word correspondence theorem | 1690DED84FC257B50BC5B44E094E382D8A79B176E7BB9C21D0845DAEC59629B8 |
| handbook/bib/handbook.bib | lines 6099–6134, report, journal, and later-correction identities | BB5705BD2223275E25B32146540391D511D907FA779F3872C9CAAB1CAB102515 |
| spec/research/p09-buchi-1960-source-note.md | complete lines 1–358 | 1C7D1679188EA891D134FE7498822B365DCBB045C607FE2AD39C6610B2D362E2 |
| spec/research/p09-source-presentations-lot2-3.md | N-c-014.a lines 620–630 and open-ledger line 898 | EDA1593FCF2F5784718086A7A9747E686E27ABAB992D399362E37F369D732FD3 |

The fixed later-correction source is Véronique Bruyère, Georges Hansel, Christian Michaux, and Roger Villemaire, “Logic and \(p\)-Recognizable Sets of Integers,” *Bulletin of the Belgian Mathematical Society -- Simon Stevin* 1(2) (1994), 191–238, DOI `10.36045/bbms/1103408547`, public record <https://eudml.org/doc/232407>, public PDF <https://richmodels.epfl.ch/_media/bru.pdf>. Review printed pp. 202–203 directly. This publication is source evidence but is not a locally edited artifact.

The repository OCR at `tmp/pdfs/p09-buchi-1960/buchi-1959-umr1083.txt` remains a non-controlling reading aid. Visual report pages are `page-01.jpg` through `page-48.jpg` under `tmp/pdfs/p09-buchi-1960/rendered/`.

## Round-two invariants

- R2-I1: Printed Definition 2 is the pointwise identity \(U[Y^m]\equiv U[H(Y^m,\bot^n)]\). It is not a constant-state identity and does not imply \(U(\bot^m)=\top\).
- R2-I2: Behavior is eventual permanent output truth on special inputs. Actual run predicates, finite weak witnesses, output predicates, behavior sets, and finite-word string behavior retain different standings.
- R2-I3: The report's Theorem 2 statement may be retained only if the printed formula (2) is identified as defective and a complete, explicitly handbook-owned repair is proved.
- R2-I4: The corrected finite-witness formula must work in both directions, for tuple states and inputs, for \(h=0\), without assuming \(U(\bot^m)=\top\), and must yield the advertised existential local successor form.
- R2-I5: Theorem 3, Corollaries 1–2, and Theorems 7–8 must disclose their dependence on the repaired analysis route wherever omission would falsely credit printed formula (2).
- R2-I6: Theorem 3's displayed last-true-point boundary and its printed “\(x+1\) is the length” inconsistency must not be conflated.
- R2-I7: Corollary 1 requires the \(B(\bot,\bot)\) tail guard and records the source's inclusive \(x\leq k\) bound before loop deletion.
- R2-I8: The report's displayed bit-occurrence formula is false in both directions. Replacing only \(u<v\) by \(u<x\) is also false.
- R2-I9: Theorems 4 and 9 are false for the unary predicate \(P_2\). The corrected exact correspondence uses the binary bit-occurrence relation \(\in_2\), equivalently the greatest-power-divisor function \(V_2\). Source claim, counterexample, and later correction may not be blended.
- R2-I10: Corollary 5's decidability conclusion may be retained only through the sound first-order-to-weak-second-order translation, not through the false converse.
- R2-I11: The binary-to-ternary converter sentence remains explicitly tentative at the report's “seems to mean” strength unless a separate reduction is supplied.
- R2-I12: The sound finite-word correspondence, the repaired Theorem 2 proof, the false arithmetic equivalence, and the unreconciled 1960 journal version are four different claims.
- R2-I13: Every introduced term or notation satisfies the AGENTS rule locally: necessity, exact definition or axiom, standing, nonredundancy, and later use.
- R2-I14: Public access is not a redistribution licence. The report/article/reprint boundary and later-source standing remain explicit.
- R2-I15: This is manuscript scholarship. No test, test harness, automated checker, repository script, TeX command, interim build, or handbook-PDF inspection may be used or claimed. SHA-256 is permitted only for frozen identity.
- R2-I16: Reviewers remain blind to the chair, ledger, every round-one transcript, and one another's round-two reports. They may not contact one another or edit a frozen artifact.

## Mandatory coverage

- R2-M01: recompute all six hashes before substantive judgment.
- R2-M02: visually inspect all 48 report pages and confirm the physical map.
- R2-M03: verify exact Definition 2 and every cross-artifact occurrence.
- R2-M04: independently validate the counterexample to printed Theorem 2 formula (2).
- R2-M05: independently prove or refute every clause and both directions of the handbook-owned repaired finite-witness construction, including all boundary cases and the promised local normal form.
- R2-M06: verify the Theorem 3 length/last-point inconsistency and the reader's chosen convention.
- R2-M07: verify Corollary 1's tail guard, inclusive bound, loop deletion, zero-length case, and all-false assignment.
- R2-M08: verify both counterexamples to the printed bit formula and the counterexample to the one-character proposed repair.
- R2-M09: directly read the 1994 correction source at printed pp. 202–203 and verify the \(P_2/\in_2/V_2\) history and strict-definability claim.
- R2-M10: trace the false Theorem 4 claim into Theorem 9 and every base-regularity sentence retained in the source note.
- R2-M11: verify that Corollary 5 decidability follows from the surviving direction alone.
- R2-M12: recheck Theorems 6–8 and the exact point at which repaired analysis is needed; preserve the terminal-marker encoding and empty word.
- R2-M13: verify the report's tentative binary-to-ternary wording and the reader/source-note qualification.
- R2-M14: reconcile the reader, source note, compact record, shared theorem, bibliography, and open ledger without completion inflation.
- R2-M15: apply the full AGENTS terminology rule to every corrected term and notation, especially special output, finite witness, \(\in_2\), and \(V_2\).
- R2-M16: verify report/journal/later-source attribution, page locators, rights boundary, topic-only scope, and the no-test/no-build boundary.

## Seats

### Source fidelity and evidence

Verify R2-M01–R2-M04, R2-M06–R2-M10, and R2-M12–R2-M16. Every finding must cite the exact frozen line and controlling printed page. Do not accept a mathematically correct repair as Büchi's printed proof or a later correction as journal wording.

Write only `transcript/r2-source-fidelity.md`.

### Mathematical and proof correctness

Verify every R2-M item, with primary responsibility for R2-M04–R2-M12. Derive the repaired cutoff theorem from first principles; test the supplied counterexamples by hand; determine the exact surviving strength of Corollary 5, Theorem 9, and downstream finite-word claims. Do not assume that a proposed correction is sound merely because it was written in response to round one.

Write only `transcript/r2-mathematical-proof.md`.

### Adversarial publication and terminology

Verify every R2-M item, emphasizing source/repair attribution, hostile-reader ambiguity, terminology standing, cross-record agreement, and scope/status language. Identify any sentence that still overstates a false source theorem, launders later correction into 1959/1960, or implies closure before this round accepts.

Write only `transcript/r2-adversarial-publication.md`.

## Filing rule

Each reviewer must mark every assigned mandatory item checked-clean, finding-linked, or not-checked with reason. End exactly with one of:

- `VERDICT: ACCEPT`
- `VERDICT: REJECT — <exact blocking IDs>`

Do not read `transcript/chair.md`, `ledger.md`, any `r1-*.md`, the Büchi 1962 board, or another round-two transcript. Do not contact another reviewer. Do not edit any frozen object. Do not run tests, automated checks, scripts, TeX, or builds.

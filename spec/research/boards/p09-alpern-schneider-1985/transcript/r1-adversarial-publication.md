# Round 1 opening report — adversarial publication and terminology seat

## Snapshot identity and permitted evidence

All seven frozen SHA-256 values recomputed before substantive review match the
charter:

| Frozen artifact | Recomputed SHA-256 | Result |
|---|---|---|
| Journal PDF | `FB69B4E81FD14CAE073F6087CE724E70847FFF16EA560701525952908E48FE31` | match |
| Technical-report PDF | `CF02E04AF863E7325C59C6C4671E389C53DB7B7ADA7804A379B287C569C896AE` | match |
| `n-c-012.tex` | `D1844530FA4BA9EC2E8F702763966F8AA3C57BE3A3E3DD5163EEA24E2905033D` | match |
| Shared definition | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` | match |
| Bibliography | `E0AF3849EEB34AB9966EF971881D3D10307ED47A92593FBE0B91917E18A1318E` | match |
| Source note | `B99757CEAADE0045D4663493403112892AC4A199176D7B4A0D244AF23168532F` | match |
| Compact presentation | `35D27BCC4AE25DE83260CB9356D854F64E99FAAFC6B824A34B85366B553CE872` | match |

I visually read journal pp. 181--185 from `journal-page-1.png` through
`journal-page-5.png` and every technical-report file page from
`tr-page-01.png` through `tr-page-11.png`. The controlling journal PDF and
the comparison-report PDF controlled source identity. The review used only
those page readings, the frozen text scopes, direct mathematical analysis, and
citation inspection.

## Findings

### R1-AP-01 — must-fix — compact safety clause loses the declared execution universe

- **Exact location:** `spec/research/p09-source-presentations-lot2-3.md:423-433`, especially the displayed safety clause at lines 431-433. Compare the exact reader clause at `handbook/parts/p09/presentations/n-c-012.tex:2673-2682`, the source-note transcription at `spec/research/p09-alpern-schneider-1985-source-note.md:161-172`, and journal p. 182 / report body p. 2.
- **Finding:** The compact record calls its ordinary definitions exact, but writes safety as `\forall x\notin P\;\exists n\;\forall y\in S^\omega\;\cdots`. Its displayed binder does not restrict (x) to (S^\omega); it binds every object outside (P), even though the following prefix (x{\upharpoonright}n) is defined only for executions. The journal’s clause and the full reader instead quantify (x\in S^\omega) and use the implication (x\notin P\Longrightarrow\cdots).
- **Violated invariant:** I3 (notation and standing before use), I6 (source versus reconstruction must remain visibly exact), and I7 (the classes are semantic properties over the declared sequence universe). This is also an M06 and M21 failure.
- **Concrete harm:** A graduate reader taking the compact display literally receives an ill-typed formula: objects outside (S^\omega) may be outside (P), but have no finite prefix. Treating the ambient universe as silently restricted repairs the error only by importing a convention that this record expressly promises to state.
- **Smallest exact correction:** Replace lines 431-433 by
  \[
    \forall x\in S^\omega\;
    \left(x\notin P\Longrightarrow\exists n\in\omega\;\forall y\in S^\omega\;
    (x{\upharpoonright}n)\mathbin{\smallfrown}y\notin P\right).
  \]

### R1-AP-02 — must-fix — the compact record calls the wrong part of Corollary 2.1 false

- **Exact location:** `spec/research/p09-source-presentations-lot2-3.md:504-515`, specifically line 509. Compare `spec/research/p09-alpern-schneider-1985-source-note.md:467-516` and `handbook/parts/p09/presentations/n-c-012.tex:2904-2936`; both source images print the intersection-closure hypothesis (journal p. 184; report body p. 8).
- **Finding:** “The reader also proves that the printed assumption is genuinely false in general” misstates what the countermodel establishes. The intersection-closure hypothesis can hold: the displayed family \(\{S^\omega,E_a,E_b,\{a^\omega\},\varnothing\}\) is precisely an intersection-closed witness satisfying it. The countermodel shows that the *corollary’s implication/conclusion under that hypothesis* is false, or equivalently that the printed hypothesis is insufficient; it does not show the assumption itself false.
- **Violated invariant:** I6 (do not launder a correction into the source), I9 (preserve the literal hypothesis and distinguish its validity from its correction), and I10 (report the corollary at its exact strength). This is an M17 and M21 failure.
- **Concrete harm:** The sentence converts a precise source-level closure-operator defect into a claim that the source’s premise cannot obtain. That reverses the point of the countermodel and blurs the essential distinction between a satisfiable but insufficient assumption and a false premise.
- **Smallest exact correction:** Replace “the printed assumption is genuinely false in general” with “the printed implication is false in general” or, more explicitly, “the printed intersection-closure hypothesis is genuinely insufficient in general.”

### R1-AP-03 — must-fix — the reader’s predictive property lacks exact standing for (A) and (B)

- **Exact location:** `handbook/parts/p09/presentations/n-c-012.tex:2780-2800`, especially line 2782 and the definition at lines 2785-2793. Compare the source-note reconstruction at `spec/research/p09-alpern-schneider-1985-source-note.md:290-312`, which explicitly begins “state conditions \(A,B\subseteq S\),” and the compact claim at `spec/research/p09-source-presentations-lot2-3.md:465-469` that this is an exact property with stated hypotheses.
- **Finding:** The frozen reader says only that \(A,S\setminus A,B,S\setminus B\) are “nonempty state conditions.” It never gives the exact standing \(A,B\subseteq S\). The later definition of \(P_{A,B}\) then uses (x_0\in A) and (x_n\in B), while the claimed nondegeneracy and the separation proof depend on those objects being state conditions in the formal, subset-of-(S) sense.
- **Violated invariant:** I3 (exact standing before use) and I4 (a reader-introduced technical symbol must have a local exact, eliminable definition and standing). The omission also defeats M11, M20, and M21’s required reconciliation.
- **Concrete harm:** A reader cannot tell whether (A,B) are subsets of states, predicates on states, or unrestricted ambient sets. In an unrestricted-set reading, (S\setminus A) is still defined but the displayed membership tests and the claimed four-way nondegeneracy are no longer the precise state-space conditions used in the proof.
- **Smallest exact correction:** Replace the opening of line 2782 with: “Assume that \(A,B\subseteq S\) and that \(A,S\setminus A,B,S\setminus B\) are nonempty, and put”. No new technical name is needed.

## Coverage map

| Point | Status | Evidence / linked record |
|---|---|---|
| M01 | checked-clean | All seven recomputed hashes match the charter table. |
| M02 | checked-clean | Visual reading completed for journal pp. 181--185 and report file pages 01--11. |
| M03 | checked-clean | Journal p. 181, report title leaves, source note 10-49, compact record 397-421, and bibliography 6056-6080 agree on title, authors, venue, date, pages, DOI, dates, report number, routes, and rights. |
| M04 | checked-clean | Journal pp. 181--185 and report body pp. 1--9 agree substantively; both print the intersection-closure wording of the second corollary, as recorded at source note 82-95. |
| M05 | checked-clean | `n-c-012.tex:2634-2670` states (S\ne\varnothing), sequence spaces, concatenation, prefix, property and program standing, membership, and terminal padding before their uses. |
| M06 | finding-linked | R1-AP-01: compact record loses the typed safety binder, though the full reader and source note are exact. |
| M07 | checked-clean | `n-c-012.tex:2684-2725` gives live-for-(P), universal liveness, nonemptiness, and full-space boundary with exact standing. |
| M08 | checked-clean | `n-c-012.tex:2660-2663,2702-2720` and source pages preserve motivation, examples, stuttering qualification, and non-theorem status. |
| M09 | checked-clean | `n-c-012.tex:2727-2767` gives exact uniform/absolute clauses, standing, nonredundancy, use, and implication chain. |
| M10 | checked-clean | `n-c-012.tex:2769-2778` distinguishes source statement from the handbook fixed-suffix check. |
| M11 | finding-linked | R1-AP-03: the exact reader display of (P_{A,B}) lacks the typed standing that its hypotheses and proof require. |
| M12 | checked-clean | `n-c-012.tex:2802-2810` preserves until and total-correctness intersections and rejects a dichotomy. |
| M13 | checked-clean | `n-c-012.tex:2812-2831` gives cylinders and labels the direction proofs as handbook-supplied. |
| M14 | checked-clean | `n-c-012.tex:2833-2866` distinguishes source (L), reader (L_P), the proof, and nonuniqueness/syntax/algorithm boundaries. |
| M15 | checked-clean | `n-c-012.tex:2868-2875` preserves all three Corollary 1.1 closure hypotheses. |
| M16 | checked-clean | `n-c-012.tex:2877-2902` gives the alpha-renaming, density, disjointness, factorization, and material (|S|>1) condition. |
| M17 | finding-linked | R1-AP-02: compact phrasing confuses a satisfiable but insufficient intersection-closure hypothesis with a false assumption; full reader/source note correctly give the countermodel and repair. |
| M18 | checked-clean | `n-c-012.tex:2938-2956` accurately gives the Boolean table and sole overlap. |
| M19 | checked-clean | `n-c-012.tex:2958-2968` and source note 537-557 correctly separate printed theorem proofs, stated equivalences, handbook proofs, and methodological conclusion. |
| M20 | finding-linked | R1-AP-03 affects the required exact standing for reader-introduced (P_{A,B}); the other enumerated names meet the local definition, standing, nonredundancy, and use conditions. |
| M21 | finding-linked | R1-AP-01, R1-AP-02, and R1-AP-03 are cross-record mismatches; bibliography itself is source-faithful. |
| M22 | checked-clean | The frozen records preserve unlettered `N-c-012` standing, journal/report distinction, rights boundary, topic-only status, and the manuscript-only evidence boundary. |

VERDICT: REJECT R1-AP-01, R1-AP-02, R1-AP-03

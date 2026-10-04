# N-c-014 integrated publication-text review — blind Round 4

VERDICT: REJECT

## Scope and evidence read

I reviewed the publication text directly, from the current source snapshot, under the supplied technical-name rule.

- `handbook/parts/p09/presentations/n-c-014.tex`, lines 1--1852, read from line 1 through EOF.
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 836--941, including the host B\"uchi--Elgot--Trakhtenbrot theorem, the host S2S theorem, the finite-ranked-tree definition and theorem, and the four presentation inputs.
- `spec/research/p09-buchi-1960-source-note.md`, complete.
- `spec/research/p09-elgot-1961-source-note.md`, complete.
- `spec/research/p09-trakhtenbrot-1961-source-note.md`, complete.
- `spec/research/p09-rabin-1969-source-note.md`, complete.
- `spec/research/p09-thomas-1996-report-source-note.md`, complete.
- The N-c-014 source/status section and relevant open-source bullets in `spec/research/p09-source-presentations-lot2-3.md`.
- The relevant entries in `handbook/bib/handbook.bib`: `Buchi1959WeakReport`, `Buchi1960`, `BruyereEtAl1994`, `Elgot1959Report`, `Elgot1961`, `Elgot1962Errata`, `Trakhtenbrot1961`, `Trakhtenbrot1962Expanded`, `Rabin1969`, `Meyer1975Complexity`, `McNaughton1966`, `Thomas1996Report`, `Thomas1997`, and `ComonEtAl2007`.

No other evidence controls this verdict.

## Prohibited actions expressly not taken

- I did not open, inspect, render, build, or cite a manuscript PDF, source PDF, PNG, page image, contact sheet, or other render.
- I did not run TeX, a PDF build, a manuscript build, tests, a test harness, an automated checker, a repository script, or a hash command.
- I did not call `list_agents`.
- I did not open any earlier N-c-014 review, admission, board, ledger, chair transcript, independent-review record, or review-history file. References to such records inside the expressly permitted source notes and compact source section were not followed.
- No historical source page was opened; no unresolved source ambiguity required that exception.
- I did not edit the manuscript, host, bibliography, source notes, compact source record, ledger, prior report, or any other file. This report is the only file created, and no admission record was added.

## Must-fix publication-text finding

### 1. Theorem 8.1's lexicographic selection is undefined because the output alphabet has no order

At `handbook/parts/p09/presentations/n-c-014.tex:347--355`, (B) is introduced only as a finite nonempty alphabet. No order on (B) is fixed. After constructing the largest strongly (A)-extendable regular sublanguage (gamma_A) at lines 375--420 and stating the synthesis equivalence at lines 423--425, the text says at lines 427--428 that “lexicographically selecting the least compatible output word” produces the required automaton. Lexicographic leastness is not defined on words over an arbitrary unordered finite alphabet.

Lines 429--431 do not repair this first-use defect. They introduce “an order on (B) and its reverse” only afterward, for Corollary 8.2's separate uniqueness comparison. A later order cannot make the preceding constructive selection well-defined at its point of use. The permitted Elgot source note also states the missing premise explicitly: first fix an order on (B), then retain the lexicographically least compatible output.

This is a must-fix definedness and sequencing defect under the publication criteria. The minimum repair is local: before the selection at line 427, fix a total order on (B), say that it induces the lexicographic order on equal-length (B)-words, and make explicit that the selected compatible outputs are those in (gamma_A). For a complete graduate-reference proof bridge, the same sentence should record that the source's selection lemma preserves regularity; strong (A)-extendability supplies prefix closure and input-totality, selection supplies functionality, and Theorem 7.1 then yields the automaton. No new named construction is needed.

Until that premise is stated before use, the unchanged snapshot cannot receive ACCEPT.

## Findings on the remaining publication-text criteria

Apart from the must-fix above, I found no additional publication-text blocker in the reviewed scope.

### Definitions, standing, and technical-name discipline

The presentation generally gives operative objects a precise standing before relying on them. Representative examples include B\"uchi's formula-tuple automaton, transit predicate, output predicate, and behavior at lines 31--71; Elgot's acceptor, assignment encoding, and transducer at lines 239--373; Trakhtenbrot's formal system, syntactic formula classes, operators, portions, residual stream maps, and general solutions at lines 583--896; Rabin's successor structures, ordinary automata, track trees, dual languages, and finite-tree objects at lines 1059--1491; and Thomas's later tree automata, chain acceptance, game, and regular-tree generator at lines 1658--1824.

The manuscript's genuinely handbook-owned names and symbols meet the supplied necessity/definition/standing/nonredundancy/use rule. In particular, the residual operator (T_u) is typed and distinguished from broad memory states at lines 720--741; (Omega^{\dagger}) is defined as an exact positive-length representative of the omitted empty dual type and then used in both complementation and emptiness at lines 1369--1392 and 1541--1545; the finite table-run is defined and distinguished from both other run notions at lines 1556--1571; and (mathcal A^\bot) is typed, proved language-equivalent, distinguished from a game or run, and used to discharge the game theorem's live-move premise at lines 1724--1757.

### Notation and disambiguated reuse

The text expressly disambiguates potentially dangerous reuse: Rabin's two order symbols at lines 1063--1072; Rabin's (Lambda) from Thomas's later (epsilon) at lines 1059--1062 and 1671--1685; Rabin's ordinary acceptance family from the dual pair sequence at lines 1152--1156 and 1361--1367; Rabin's finite-tree run from the host's bottom-up ranked-tree run at lines 1473--1480; Thomas's direction stream from Rabin's node-set path at line 1685; and the successor functions (S_i) from Rabin's earlier initial-state set (S_0) at lines 1826--1833. Elgot's source-specific “open” is fixed as prefix closure at lines 360--369, while the later Trakhtenbrot discussion announces Cantor-product topology at lines 715--719; the later open-relation statement is read in that topological context.

The one failed definedness point is the missing order behind “lexicographically” identified above.

### Source ownership, corrections, and unreconciled-source boundaries

The source/handbook boundary is unusually explicit and publication-ready. B\"uchi's 1959 report is separated from the unreconciled 1960 article at lines 8--16 and 971--973; the repaired finite-witness analysis, false unary-powers equivalence, and later corrected signature are attributed at their respective strengths at lines 95--142 and 192--230. Elgot's journal article, report precursor, and published errata remain distinct at lines 232--237, 443--542, and 559--569, with the unary-window completion explicitly handbook-owned. Trakhtenbrot's announcement/expansion distinction, terminology normalization, counterexample, empty-set case, and finite-word edge repair are bounded at lines 571--581, 663--678, 743--820, and 926--960. Rabin's zero-length normalization and two empty-witness repairs are proved and labelled as handbook-owned at lines 1369--1435 and 1538--1626. Thomas's 1996 report is kept separate from the registered 1997 chapter at lines 979--1051 and 1847--1852, and the deadlock completion is locally proved rather than attributed to the report.

The two remaining source-register limitations relevant to this item are not hidden: literal B\"uchi 1960 reconciliation remains open, and Thomas's final 1997 chapter is not claimed as the source of the report locators. The McNaughton equivalence is identified as an external dependency at lines 1280--1317 rather than silently absorbed into Rabin's proof.

### Logical sequencing and graduate-reference sufficiency

The finite-word development proceeds source by source and then supplies Thomas's modern construction without replacing the original packages. The infinite-tree development fixes Rabin's structures and ordinary acceptance before the logical translations, gives the path product before dual complementation, locates the transfinite steps inside the marked-obligation proof, and separates Rabin's actual emptiness reduction from Thomas's later game/basis route. Forward references to Rabin's finite-tree construction are expressly signposted, and the exact finite-tree objects and run notions are supplied before the later complementation and emptiness details depend on them.

The local proof descriptions are sufficient to identify hypotheses, constructions, conclusions, external dependencies, and handbook-owned repairs. The exception is Theorem 8.1's undefined lexicographic selector and its omitted order premise.

### Host consistency and citations

The finite-word material at lines 8--1051 is consistent with the host theorem at `logic-in-computer-science.tex:836--851`: the host labels its displayed equivalence as the modern formulation and the presentation preserves the different B\"uchi, Elgot, Trakhtenbrot, and Thomas encodings. The Rabin and Thomas tree material at lines 1053--1852 is consistent with the successor-only S2S theorem at host lines 874--879: Rabin explains definability of the two orders from finite successor structures, and Thomas closes with ((T,S_0,S_1)). Rabin's source-specific finite trees are also expressly kept distinct from the host's ranked, bottom-up finite-tree automata at host lines 881--931.

The cited source keys used by the presentation and host have corresponding relevant bibliography entries with the stated report/article/errata/version distinctions. Page and section locators are bounded to the acquired bodies: B\"uchi report locators use `Buchi1959WeakReport`, Elgot's corrections use `Elgot1962Errata`, Rabin's complexity correction uses `Meyer1975Complexity`, and Thomas locators use `Thomas1996Report` rather than silently citing the unread final chapter.

## Disposition

The manuscript is close to publication-text readiness, but the undefined selector at `n-c-014.tex:427--428` is a genuine must-fix under this review's exact-definedness standard. The repair is small and local; it nevertheless changes the verdict for this unchanged snapshot.

REGISTER STATUS: OPEN

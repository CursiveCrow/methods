# P9 N-c-009, N-c-010 and N-c-013 full-text inventory

Snapshot completed 7 September 2026 UTC, under the inventory directory dated 6 September. All **3,810 assigned presentation lines** were read sequentially in numbered, nontruncated ranges. The necessary ALC proof dependencies, active acceptance definitions, and host tables were also read. The JSON companion preserves every original field of the three requirement rows and records headings, results, source presentations, proof boundaries, hashes, read intervals, active routes and requirement reconciliation.

The principal finding is a **false printed EL++ subsumption criterion and a failed quotient-model claim** in N-c-010. The ALC core has substantial current local proofs; the required SHOIQ presentation remains explicitly absent. The automata material is substantial, while several exact registered source presentations remain unavailable in its stated basis. None of the three original requirements is marked completion-verified.

## Confirmed mathematical defect: EL++ nominal saturation

The reachability definition at [N-c-010:144–148](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-010.tex:144), rule CR6 at lines 182–184, the decision criterion at lines 216–227, and the quotient agreement assertion at lines 264–266 are incompatible.

Consider the normalized CBox

\[
 A\sqsubseteq\exists r.C,\quad A\sqsubseteq\exists s.D,\quad
 C\sqsubseteq\{a\},\quad D\sqsubseteq\{a\},\quad
 C\sqsubseteq P,\quad D\sqsubseteq Q,\quad
 P\sqcap Q\sqsubseteq\bot.
\]

It is satisfiable: take a singleton domain, interpret the nominal by its element, and interpret \(A,C,D,P,Q\) as empty. But in every model, any \(A\)-element would require both a \(C\)-element and a \(D\)-element. Both would equal \(a\), putting \(a\) in \(P\cap Q\). Thus every model has \(A=\varnothing\), and the CBox entails \(A\sqsubseteq P\).

The printed saturation instead stabilizes with

\[
\begin{aligned}
S(A)&=\{A,\top\},&
S(C)&=\{C,\top,\{a\},P\},\\
S(D)&=\{D,\top,\{a\},Q\},&
S(\{a\})&=\{\{a\},\top\},\\
R(r)&=\{(A,C)\},&
R(s)&=\{(A,D)\}.
\end{aligned}
\]

All other basic sets stay initial, and no bottom is added. Although the printed reachability relation may start at **any nominal**, no nominal has outgoing edges here. Neither \(C\leadsto_R D\) nor \(D\leadsto_R C\) holds. CR6 can copy \(S(\{a\})\) into the other two sets, but that adds nothing. The printed test returns false for the valid subsumption. It also leaves different labels on vertices identified by the shared nominal, refuting the stated quotient agreement claim.

The parent independently replayed the counterexample against the current manuscript and reported the same guard and agreement claim in the held LTCS report, at layout lines 322–411 and 534–574. That source inspection is attributed corroboration; this pass did not reopen the report or certify its manifestation. Source correspondence does not validate the false criterion.

A corrected algorithm or sufficient hypothesis needs a correctness proof. No repair is credited. A fresh query nominal is only a possible approach, not an implemented or verified solution. The counterexample refutes this criterion and proof; it does not refute the independently known polynomial-time classification of EL++.

## N-c-009: ALC core supplied; two exact book presentations missing

The original row is [new-content.csv:116](C:/Dev/the-methods-of-reason/spec/registers/new-content.csv:116). The 1991 presentation accounts for the historical grammar, six constraint forms, normal-form rewrites, clashes, completion, traces, evaluator, restricted languages, QBF reduction and standalone PSPACE classification. It distinguishes source statements without proofs, source sketches, and local elaborations. The canonical constraint model and completion-step arguments are locally expanded; the source's omitted termination and encoded linear-space analyses are not silently supplied as complete proofs. The quoted FL result retains a separate grammar dependency.

The modern requirement is supported by the current [host ALC definition and method](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:288), the complete [registered rule sheet](C:/Dev/the-methods-of-reason/handbook/registry/calculi/tableaux-alc.tex:1), and [annex:p9.alc.1](C:/Dev/the-methods-of-reason/handbook/annex/p09/proofs.tex:3). These supply nonempty KB semantics, TBoxes and ABoxes, initialization, ancestor blocking with re-evaluation, termination, model-guided completeness, and soundness by a finite redirected model.

The [general-TBox body](C:/Dev/the-methods-of-reason/handbook/parts/p09/alc-general-tboxes.tex:1) and entire [459-line proof file](C:/Dev/the-methods-of-reason/handbook/annex/p09/alc-general-tboxes.tex:1) supply complete-type elimination, realized-type survival, the truth lemma, finite models, empty cases, and upper bounds. The bounds are at most \(2^m\) model elements and time \(2^{O(N^2)}\), improving to \(2^{O(N)}\) without ABox names. Hardness uses an explicitly cited CKS alternation characterization, a fixed machine, finite acceptance trees, configuration-height bound, polynomially many rank bits, both model/acceptance directions, and reductions for all four decision problems.

The exact 2003 first-edition and 2017 textbook bodies remain missing from the stated basis at [N-c-009:806–842](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-009.tex:806). The 2000/2008 source basis and local core proofs are separately identified. They do not establish completion of the registered books' own presentation.

## N-c-010: extensive tractability/profile content, two concrete obstacles

The original row is [new-content.csv:117](C:/Dev/the-methods-of-reason/spec/registers/new-content.csv:117). EL++ has concrete-domain hypotheses, normal forms, all eleven completion rules, termination, an example and constructor-sensitive boundaries. Its correctness account requires the repair above.

DL-Lite at lines 393–940 has three grammars, nonempty interpretations and UNA, the five-rule chase, negative-inclusion closure, consistency formulas, canonical homomorphisms, all eleven PerfectRef replacements, termination, rewriting arguments, the student–tutor example, arbitrary UCQs and inconsistent inputs, and exact complexity parameters. The disclosed total-homomorphism, stuttering and finite-state-count repairs are actual text. Source-cited transfers and the four chase cases described as analogous retain their stated proof standing.

W3C material at lines 942–1518 supplies the dated normative sources, position-sensitive EL/QL/RL grammars, datatypes, role restrictions, axiom inventories, all six directed non-inclusion witnesses, and the Direct-Semantics/RL-RDF distinction. The full [host family and task tables](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:455) were read through line 607, including task axes, conditional bounds and source limitations. The requested survey does not automatically require a new proof of every cited table cell.

There is also a missing writing surface: [host lines 509–520](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:509) expressly withhold the required SHOIQ grammar, semantics, number encoding and theorem scope, together with the expressive-family comparison rows. A SROIQ lineage paragraph does not supply them. The exact 2017 Chapters 6–8 presentation remains absent at [N-c-010:1520–1527](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-010.tex:1520).

## N-c-013: substantive constructions with exact version boundaries

The original row is [new-content.csv:120](C:/Dev/the-methods-of-reason/spec/registers/new-content.csv:120). The acceptance interface was read in the active [Büchi definition](C:/Dev/the-methods-of-reason/handbook/parts/p08/temporal-epistemic-supplement.tex:355) and [P9 parity/Rabin definition](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:733).

Vardi–Wolper uses an identified 18-page author preprint with a 15 August 1985 abstract cover. It supplies closure types, transitions, the eventuality batch monitor, projection and state count, program-product equivalence, and a complete local counterexample calculation. The source's omitted line-by-line language-inclusion inductions and deferred probabilistic details remain disclosed.

The [single-start conversion at lines 64–85](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-013.tex:64) consumes the first letter while choosing and advancing an old start, adds one fresh nonaccepting state, and handles an empty set of permitted starts. It closes the convention mismatch without asserting that the source already used the modern tuple.

Büchi's account contains the Ramsey/congruence complementation route, recurrent normal form, modern encoding, and decision argument. The [positive-return correction at lines 801–809](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-013.tex:801) is present; the [Thomas passage at lines 1401–1415](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-013.tex:1401) gives both directions. A stem may have length zero, but an accepting return must have positive length.

Safra's detailed proof is assigned to the 1995 expanded author manuscript. It includes named-tree transitions, current colors, allocation choices, a total rejecting sink, both acceptance directions, and an explicit \(2^{O(n\log n)}\) count. Thomas's 1996 report uses its own \(2n\)-name construction and pair convention, kept distinct from Safra's \(n\)-name construction.

The exact McNaughton 1966 article, Safra 1988 proceedings body and Thomas 1997 chapter remain absent from the stated basis at [lines 921–963](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-013.tex:921) and [1430–1441](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-013.tex:1430). Precursor/expanded versions support their own presentations; they do not discharge every exact registered source obligation.

## Reading coverage and limits

| Assigned presentation | Full lines read | SHA256 |
|---|---:|---|
| N-c-009 | 1–842 | 90765C24F3D9ED7BA1046FFA343096D738DA9646D9929E31A7DAC89DED122563 |
| N-c-010 | 1–1527 | A5E7135DED58AA5E8778AC7A71E0B9BBBC3BA57E62FA7970E4FCC3BDB4493F93 |
| N-c-013 | 1–1441 | E98D593A11B0BB96D3749A8C9855C2FEA2EA22DDEF9518BB46BE411BCDD274A7 |

All three hashes were rechecked unchanged. The JSON records every numbered reading interval, including nine dependency files. The complete general-TBox body and annex, complete ALC rule sheet, full ALC blocking proof, selected host intervals and active drivers are distinguished. No unread tail is credited for a partially inspected host or figure.

The assigned inventory is complete: every original row is reconciled, and all assigned presentation lines have been read. Requirement acceptance remains false for all three rows because of the defect, missing expressive surface, and/or exact-source obligations above. This is not a count of three unwritten topics: the supplied mathematics is extensive.

No software tests, manuscript builds or renders were run. No sources were acquired, and no manuscript, source, bibliography or register files were changed. This pass is not an exhaustive independent proof audit of every source theorem, a renewed source-fidelity certification, or a whole-Part-IX acceptance decision. Historical E/S treatment values remain unchanged requirement data.

The machine-readable record is [p09-n-c-009-010-013-full-text-inventory.json](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/p09-n-c-009-010-013-full-text-inventory.json).

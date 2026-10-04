VERDICT: REJECT

# Round 6 source-fidelity decision

The current N-c-016 manuscript is source-faithful in the repaired Clarke--Emerson auxiliary-variable construction, its guard/update partition, the Queille--Sifakis action-family conventions, the Emerson--Halpern structure-class definition order, the source/proof boundaries, the acquisition and rights qualifications, and the five bibliography identities.  It nevertheless retains one host-typing defect at two line-specific sites in the Baier--Katoen bridge.  Those two sites are the complete must-fix list for this review.

This verdict is a text-only source-fidelity verdict.  It is not a TeX-build, render, page-layout, rights-clearance, mathematical-formalization, final-admission, board, parent-agent, or human-editor verdict.

# Must-fix findings

## 1. Lines 1587--1589 call an empty-state tuple an exact host-typed input

Current text:

> Together with \(\mathcal K_0=(S,R_0,V_0)\), it supplies the exact typed input to Method~\ref{def:p09-ctl-labelling}.

The inherited host definition at `handbook/parts/p08/temporal-epistemic-supplement.tex`, lines 46--53, defines a total transition structure only for \(S\ne\varnothing\).  The N-c-016 text itself recognizes this boundary at lines 1597--1602: \(\mathcal K_0\) is of the host method's type when \(S\ne\varnothing\), and the host method is not instantiated when \(S=\varnothing\).  The unqualified claim at lines 1587--1589 is therefore false in exactly the empty-source case that the following paragraph deliberately retains.

Minimal repair: qualify the sentence locally, for example:

> When \(S\ne\varnothing\), together with \(\mathcal K_0=(S,R_0,V_0)\), it supplies the exact typed input to Method~\ref{def:p09-ctl-labelling}.

No change to the empty-source branch at lines 1600--1602 is required.

## 2. Lines 1670--1676 use host satisfaction without the same nonempty-state guard

Current text says, for every source CTL state formula \(\Phi\) and every \(s\in S\),

\[
 TS,s\models_{\mathrm{BK}}\Phi
 \iff
 \mathcal K_0,s\models\operatorname{tr}(\Phi).
\]

At this point the manuscript has already stated that \(\mathcal K_0\) is not a host-structure instantiation when \(S=\varnothing\).  Quantifying `every s in S` over an empty set makes an otherwise well-typed predicate vacuous; it does not make the expression \(\mathcal K_0,s\models\operatorname{tr}(\Phi)\) well-typed when \(\mathcal K_0\) is outside the host satisfaction relation's domain.  The subsequent method claim at line 1678 is correctly restricted to finite nonempty \(S\), but that later restriction does not repair the preceding semantic-equivalence sentence.

Minimal repair: put the same guard on the induction claim, for example:

> For nonempty \(S\), every Baier--Katoen CTL state formula \(\Phi\), and every \(s\in S\), induction on the translation gives ...

Equivalently, state the displayed equivalence inside an explicit `If S is nonempty` sentence.  Retain the separate empty-source conclusion that \(I=\varnothing\), all source satisfaction sets are empty, system satisfaction is vacuous, and the host method is not instantiated.

# Bounded positive source-fidelity evidence

The positive findings below delimit the rejection.  They do not waive either must-fix.

## Clarke--Emerson source state, formulas, construction, and proof voice

- Lines 8--18 correctly distinguish the 1981 meeting, the 1982 LNCS publication, the authorized 2008 reprint object, its original/reprint pagination, and the distinct longer manuscript.  The longer manuscript is not silently merged into the twenty-page publication.
- Lines 20--125 type the synchronization skeleton, global semantic structure, process-indexed next operator, and strong-until clauses consistently with the controlling note.  The total union relation and the distinction between source-indexed `EX_j` and later unindexed CTL are retained.
- Lines 126--319 preserve the source algorithm's global state-labelling output, the defective printed universal-until display versus its proof-supported repair, the finite-context SCC proposition, the scope of the NP-hardness reduction, the tableau outline, and the difference between published and fuller-manuscript evidence.  Printed, reconstructed, cited, and omitted proof material are not flattened into a single proof status.
- Lines 320--397 reproduce the nine mutual-exclusion requirement groups and retain the semantically redundant ninth group because it is source-printed.  The process-indexed modalities and their roles are not translated into a different later grammar.
- The technical name `model fragment` at lines 400--407 is locally legitimate: the rooted finite DAG condition is eliminable, its standing as a construction artifact is explicit, it is distinguished from a complete model, and its checked-root role is used in cycle closure.
- The repaired auxiliary-value encoding at lines 442--460 is total.  Each duplicate-label class \(v_1,\ldots,v_d\) receives a fresh variable with domain \(\{0,1,\ldots,d\}\); every global node receives exactly one value proposition; `0` is used outside the class; every designated initial node is initialized independently of indegree; and every global arc assigns the value indicated at its target.  This supplies values at initial nodes, nodes outside the duplicate class, and across every transition, rather than relying on incoming assignments or partial auxiliary states.
- Lines 462--481 correctly separate the source-state guard \(\gamma_e\) from the complete auxiliary update map \(\sigma_e\).  The guard removes only the moving process's current-region atom and retains the other \(k-1\) process components plus all source auxiliary equalities; the empty conjunction is true.  The update abbreviation is typed as a transition update and fills absent assignments by identity.  These names are exact eliminable metalinguistic abbreviations, their different standings and nonredundancy are stated, and they are used immediately.
- Lines 472--490 partition local transitions by endpoints and identical complete update maps.  Guards are disjoined only inside one update class; identity and nonidentity updates remain parallel.  This preserves the two displayed \(\mathsf{NCS}_1\to\mathsf{TRY}_1\) branches instead of incorrectly merging different state updates under one guard.
- Lines 492--502 correctly keep the model checker, SCC proposition, NP-hardness result, tableau outline, and worked synthesis construction at distinct proof strengths.  No general synthesis-correctness theorem or empirical synthesis implementation is invented.

## Queille--Sifakis source state, action families, formulas, and fixed points

- Lines 504--514 correctly separate the 1982 original from the 2008 reprint, state the institutional-scan authentication boundary, say that scan-distribution authorization is unestablished, and do not turn subscription-restricted reprint pages into inspected evidence.
- Lines 516--650 keep CESAR's source program/IPN roles, its only named output (`diagnostics`), the absence of a defined diagnostic format, the incomplete execution-sequence display, the finite-path \(\omega\) convention, and the literal `POT`, `INEV`, `ALL`, and `SOME` semantics distinct from later CTL terminology.
- Lines 652--695 type `Init`, `enable a`, and `after a` as state predicates, explain why enabledness and aftermath are nonredundant, define the finite action-family and process abbreviations, and supply exact nullary values.  In particular, both empty disjunctions are false, liveness of every member of an empty family is true through the empty conjunction, and a process with no actions is not silently treated as enabled.
- Lines 696--772 preserve the difference between every-action liveness and disjunctive absence of deadlock, do not turn possible enabledness into inevitable execution, and repair `receivack` to the program-defined `receiveack` only after recording the printed identifier defect.
- Lines 774--837 give the correct typed predecessor transformer, Boolean dual, pointwise transformer union/intersection, finite-iterate meanings of \(h^*\) and literal \(h^x\), all four source identities, the image-finiteness hypothesis, and the delegated proof boundary.  The superscript `x` is not silently renamed as a greatest-fixed-point binder.
- Lines 838--902 retain the user's iteration cap, possible no-answer outcome, absence of a general termination or asymptotic theorem, worked one-step result, and the external status of the protocol's non-loss assumption.

## Emerson--Halpern typing, structure classes, variants, and proof boundaries

- Lines 903--912 identify the 1986 JACM body, distinguish it from the POPL and report source states, and state that the ACM terms are conditional copying terms rather than an open-content licence.
- Lines 914--969 preserve the two semantic types of Lamport's shared syntax and distinguish primitive `sometimes` from defined `not never` before translating either into CTL* notation.
- The repaired definition order is sound: lines 970--978 define suffix closure, its path-set standing, and its difference from fusion and limit closure before Theorems 1--2 use it at lines 980--991.  The fuller structure-class block at lines 993--1024 then gives typed string domains, fusion closure, limit closure, \(R\)-generability, and state completeness before the later comparison theorems use them.  It also says which later argument needs which distinction.
- Lines 1035--1128 retain the mutually typed CTL* state/path grammars, the all-paths-over-\(S\) path-semantics boundary, current-inclusive strong until, false next at the end of a finite path, and the exact named sublanguages.
- Lines 1129--1245 preserve the shift from whole-model strong equivalence to pointwise formula equivalence, the fusion/state-completeness hypotheses, the exact expressiveness map, and the separation between source-language names and metalinguistic language comparisons.
- Lines 1246--1349 preserve the self-defeating literal targets of Theorems 5--6 separately from their proof- and diagram-supported repairs, the incorrect internal theorem cross-references, and all reader-left/cited proof steps.  The text does not present the reconstructed targets as literal printed statements.
- Lines 1350--1485 retain the fairness formula as a specification rather than a semantic fairness premise, preserve the PL proof boundary, expose rather than silently repair the MPL `U`/`X` display defects, and keep the terminal-server example as an application argument rather than a universal superiority theorem.

## Clarke--Grumberg--Peled acquisition boundary

- Lines 1486--1508 stay within acquisition evidence.  They distinguish anonymous complete-body access from physical, lending, preview, and institution-only access; use the contents page only for section-start locators; attribute no formula, algorithm, theorem, proof, example, or complexity result to the unacquired first-edition body; and do not substitute the 1996 survey, 2001 handbook chapter, 2018 second edition, or Baier--Katoen book.

## Baier--Katoen source reconstruction apart from the two host guards

- Lines 1509--1519 correctly identify the complete-body authority, all-rights-reserved boundary, and corrected printed-page map.
- Lines 1520--1555 retain the six-component action-labelled source transition system, the no-terminal-state condition in the source's own terminology, and the exact action-forgetting definitions of \(R_0\) and \(V_0\).  Their handbook-supplied metalinguistic standing and proposition-alphabet type are explicit.
- Lines 1556--1586 define \(\operatorname{tr}\) exhaustively on every primitive CTL constructor.  The translation is necessary to mediate the source/host syntax, has the standing of a metalinguistic map, changes no atom or temporal meaning, and is used by the host method.  The only defect is the missing nonempty-state qualification identified above, not the translation equations themselves.
- Lines 1590--1606 correctly establish the source-successor/binary-edge relationship, the inequality \(|R_0|\le K\), and the distinction between the host binary-edge parameter and the source action-labelled-transition parameter.  Lines 1597--1602 already contain the correct nonempty/empty case split that the two earlier/later sentences must respect.
- Lines 1608--1668 define finite and infinite path fragments, maximality, `Paths(s)`, the typed CTL grammar, source state/path satisfaction, non-strict until, satisfaction sets, and vacuous system satisfaction when \(I=\varnothing\) before attempting the source-to-host semantic bridge.  Semantic placement is therefore repaired; only its missing domain guard remains.
- Lines 1689--1704 retain ENF as a syntactic class, the rewrite-outline proof voice, and the exponential materialization warning.
- Lines 1705--1823 accurately state Algorithm 13's bottom-up role, Theorem 6.23's elementary versus printed-proof cases, the least/greatest set characterizations, Algorithms 14--16, the source's arbitrary choice steps, the explicit handbook global invariant, and the stale Algorithm 16 comment as a recorded source defect rather than an operative condition.
- Lines 1824--1874 preserve the exact Figure 6.11 labels and edges, the final satisfaction sets for Examples 6.26 and 6.28, the SCC theorem's two-direction proof status, and the off-by-one source subfigure references.
- Lines 1875--1951 preserve the exact \(O((N+K)|\Phi|)\) theorem with finite/no-terminal, predecessor-list, and direct-modality hypotheses; distinguish the absent separate space theorem; and retain the corrected formula/induction/figure defects in the CTL--LTL witness family.
- Lines 1952--2025 keep the concrete CTL/LTL witness systems and proof omissions, then type CTL* state versus path formulas, LTL's universal embedding, Theorem 6.84's one-sentence proof voice, the handbook-supplied substitution justification, and the ill-typed Figure 6.27 display boundary.
- Lines 2026--2041 collect rather than conceal the source defects and close without importing a CTL* model-checking algorithm from the unreviewed later subsection.

# Technical-name rule

I applied the supplied rule to every introduced name and abbreviation in the current presentation.  Apart from the host-domain misuse in the two must-fix sentences, the manuscript supplies the required package where it names an object:

- source technical names are accompanied by their exact source definitions and source standing;
- handbook-supplied names or symbols (`model fragment`, the total auxiliary discriminator, \(\gamma_e\), \(\sigma_e\), the finite-family/nullary abbreviations, \(R_0\), \(V_0\), and \(\operatorname{tr}\)) are eliminable at their introduction;
- relation, state-formula, path-formula, transition-update, structure-class, construction-artifact, and metalinguistic standings are not conflated;
- nearby prose identifies the ambiguity or type mismatch that makes each distinction necessary, explains its difference from the adjacent existing objects, and uses it later in a definition, construction, theorem comparison, or algorithmic instantiation.

No merely hypothetical answer is promoted to a technical name.  The two rejected sentences do not require a new name; they require only the explicit domain guard already supplied elsewhere in the same section.

# Bibliography identity audit

The five exact entries at `handbook/bib/handbook.bib`, lines 2393--2459, agree with their controlling notes:

1. `ClarkeEmerson1981`, lines 2393--2408: Clarke and Emerson; exact title; *Logics of Programs*, LNCS 131; pp. 52--71; Springer; formal publication year 1982; DOI `10.1007/BFb0025774`; reprint/source note distinguished from the 1981 meeting.
2. `QueilleSifakis1982`, lines 2409--2423: Queille and Sifakis; CESAR title; *International Symposium on Programming*, LNCS 137; pp. 337--351; 1982; DOI `10.1007/3-540-11494-7_22`; access provenance does not claim scan-redistribution authority.
3. `EmersonHalpern1986`, lines 2424--2437: Emerson and Halpern; exact article title; *Journal of the ACM* 33(1), pp. 151--178; 1986; DOI `10.1145/4904.4999`; conditional ACM terms are not called an open licence.
4. `ClarkeGrumbergPeled1999`, lines 2438--2448: Clarke, Grumberg, and Peled; *Model Checking*; MIT Press; 1999; ISBN `9780262032704`; the note explicitly says the complete body was not acquired and excludes preview/lending/subscription records from source-body standing.
5. `BaierKatoen2008`, lines 2449--2459: Baier and Katoen; *Principles of Model Checking*; MIT Press; 2008; ISBN `9780262026499`; complete institutional-file inspection is distinguished from republication rights.

I found no bibliography-identity must-fix.

# Host and integration audit

- `handbook/parts/p09/logic-in-computer-science.tex`, lines 925--1055, defines the reused finite total-structure predecessor operations, CTL labelling method, semantic correctness theorem, and binary-edge complexity parameter.  N-c-016's finite nonempty Baier--Katoen branch matches those operations after action erasure.
- The same host, lines 1475--1535, inputs `n-c-016.tex` once in the model-checking section and then proceeds to the program-logics section.  No contradictory host prose or duplicate N-c-016 input was found in the substantive integration span read.
- `handbook/parts/p08/temporal-epistemic-supplement.tex`, lines 35--185, supplies the inherited CTL/CTL* typing.  In particular, lines 46--53 require \(S\ne\varnothing\) for the host total transition structure.  That exact inherited requirement controls both must-fixes.

# Text ranges read

The following current plain-text ranges were read directly and substantively in this review:

- `handbook/parts/p09/presentations/n-c-016.tex`, lines 1--2041, completely through EOF.
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 925--1055 and 1475--1535.
- `handbook/parts/p08/temporal-epistemic-supplement.tex`, lines 35--185, for inherited CTL/CTL* and total-structure typing.
- `spec/research/p09-clarke-emerson-1981-source-note.md`, lines 1--884, completely through EOF.
- `spec/research/p09-queille-sifakis-1982-source-note.md`, lines 1--867, completely through EOF.
- `spec/research/p09-emerson-halpern-1986-source-note.md`, lines 1--729, completely through EOF.
- `spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md`, lines 1--470, completely through EOF.
- `spec/research/p09-baier-katoen-2008-ch6-source-note.md`, lines 1--1120, completely through EOF.
- `handbook/bib/handbook.bib`, exact cited entries at lines 2393--2459.

# Prohibitions and non-claims

- I did not open or inspect any prior N-c-016 review or report, including any report I may have produced in another round.
- I did not read a board, admission, register-history, parent-conclusion, or other-agent output file.
- I did not contact or delegate to any agent.
- I did not open a PDF, render, screenshot, page image, or historical publication file.
- I did not use the web.
- I did not run a TeX or handbook build, test, checker, validator, hash operation, manuscript-processing script, or executable source-analysis tool.  The permitted files were displayed only as plain text.
- I did not modify the manuscript, host, prerequisite, source notes, bibliography, or any other user/agent file.  This Round 6 report is the only file written.
- Consequently this report makes no claim about compilation, references resolving in a build, visual appearance, pagination after typesetting, PDF fidelity, source-file hashes, republication permission, final rights clearance, overall manuscript admission, or human approval.

REGISTER STATUS: OPEN

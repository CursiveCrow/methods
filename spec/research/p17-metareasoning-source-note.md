# Computations as decisions: Russell--Wefald KR1989

Authoring checkpoint: 1 October 2026. Assignment is the exact
`ED26-METHOD-metareasoning` row of
`spec/coverage/edition-2026/additional-method-units.jsonl`.
The author owns only the new p17 metareasoning body/annex, unique intakes,
this note, and disjoint source/scratch captures. Shared routing and
canonical records are the lead's responsibility.

## Complete exact body acquired and read

Downloaded the complete freely available proceedings from
[the KR archive](https://kr.org/proceedings/KR-1989-proceedings-scanned.pdf).
The capture is
`source/references/russell-wefald-1989/kr-1989-proceedings-scanned.pdf`:
19420477 bytes, 546 physical PDF pages, SHA-256
`25699661A6AFFCC33CD36FFC7442E44A95B2D8327658F02E5D35AC0F3BA39F74`.
Python urllib used ordinary certificate verification; no authentication,
purchase or TLS bypass was used. The web reader could not open the whole
19.4 MB PDF, so the local verified capture was read with the bundled
pypdf runtime.

The exact selected paper is *Principles of Metareasoning*, by Stuart
Russell and Eric Wefald, printed pp. 400--411, physical pages 420--431.
All twelve pages were read, from title and abstract through sections
1--7 and the complete references. The chapter does not use the
insufficient one-page CMU Newell-archive capture or the distinct 1991
Artificial Intelligence presentation. The proceedings title/editor/
copyright pages, physical 9--12, identify Ronald J. Brachman, Hector J.
Levesque and Raymond Reiter, Morgan Kaufmann, 1989, and ISBN
1-55860-032-9. The paper's complete contiguous extent and the archive's
contents entry agree.

Source-only page renders at printed 404, 406, 409 and 410 were inspected
to resolve equation glyphs, the prediction formulas, Figure 4 and Table 1.
They are retained under `tmp/pdfs/p17-metareasoning/`. No manuscript
was rendered. The research/PDF workflows guided source reading and this
record; the lead's no-new-children instruction was observed during this
assignment. The previously completed source helper was not restarted.

## Source components and manuscript mechanism

The exact required components C01--C05 are supplied:

- **C01, computational versus external actions.** The body introduces
  the source's external actions, computation histories, current intention,
  actual utility and stage-dependent estimated utility. It specifies actual
  program-block execution, retained workspace, computation summary,
  running time, peak memory and resource feasibility. A predicted outcome
  law is induced by the executable block over a declared class of modeled
  instances. It is not obtained by renaming an unspecified external
  experiment. Deterministic execution, uncertainty before doing the
  computation, logical omniscience and compressed statistical prediction
  are distinguished.
- **C02, utility through changed decisions.** Source equations (1)--(11),
  printed pp. 403--405, give the actual/estimated action distinction,
  complete versus partial computation, full trace model, and expected
  revised-vector value. The body uses the same later evaluator for new and
  old intention; the old intention's comparison is undelayed. It proves
  the precise discrepancy if the earlier baseline is substituted, and
  identifies the additional calibration that makes the formula agree
  with the already-written value-of-information theorem.
- **C03, exact and approximate control.** The body retains the conditions
  for source equations (12)--(18): common action-independent delay loss,
  intrinsic estimated utility, and only one changed action estimate.
  It supplies both positive-part integrals and the joint-law dependence
  counterexample. For partial computation it constructs a sufficient
  information-state model with actual executable blocks, an explicit
  finite budget, terminal intention and costs. The finite Bellman optimum,
  full history-policy class, actual-policy trace expansion and a uniform
  approximate-score loss bound are proved. These are explicit conditional
  finite solutions; they are not attributed to the source as a general
  unrestricted solution.
- **C04, unperformed calculations, imperfect evaluation and regress.**
  The source's §§2, 4.1.1 and 4.5, printed pp. 401--402, 404 and 407--408,
  discuss cost of metareasoning, expected rather than omniscient choice,
  bias from changing evaluators, ungrounded partial-value recursion,
  adaptive sample labeling, and probabilistic self-modeling. The chapter
  includes each issue. It proves nonunique ungrounded continuation, a
  positive-cost contrast, and an explicit overhead example. Actual policy
  values are not silently promoted to optimal continuation values. The
  source's adaptive convergence and philosophical self-trust questions
  remain proposals/open issues with their original standing.
- **C05, stopping and a feasible policy.** A two-block internal program
  over four input instances supplies the actual transition law, retained
  intermediate bit, evaluation output, costs, deadline, stopping decision
  and a compiled feasible controller. Its first block has negative
  one-step value while its two-block sequence has positive value. Every
  branch and expected value is calculated and proved. It is a numerical
  instance of the source's meta-greedy barrier, not a claim about intrinsic
  hardness of exclusive-or or a new sensor experiment.

## Exact source standing and dependencies

Source §3.2 allows a designer's metalevel analysis without asserting that
the agent solves it explicitly for each computation. Its footnote on
printed p. 402 assumes known external-action outcomes in the examples,
while the utilities of those outcomes may be uncertain. The chapter
respects that distinction. A distribution of unperformed deterministic
calculations represents uncertainty or a population performance model;
complete code/input under an omniscient semantic model has a fixed result.

Source §3.3's complete-trace expression needs actual eventual action and
integrable payoffs to be a complete expectation. The body makes this
condition explicit and states the missing nontermination-payoff case.
The source's sentence about an ideal computation sequence receiving
probability one does not authorize retrospective selection of a realized
best trace before its outcome is known; the body instead specifies a
feasible outcome-contingent continuation policy.

The source's complete-computation difference uses the later estimate
for both intentions. Printed p. 406, equation (15), confirms the intrinsic
benefit minus common time-cost separation. Equations (17)--(18) use,
respectively, upward revision of an inferior alternative and downward
revision of the default. Equation (16) is a one-affected-component
condition, not statistical independence between all action estimates.
The body and proof preserve these mechanisms.

Source §4.5.1 offers an adaptive grounding proposal and provisionally
assumes current choices correct for post hoc sample evaluation. It does
not prove convergence to an optimal controller. §4.5.2, equations
(21)--(22), expands stochastic stop/continue self-predictions and conditions
utility estimates on an action being selected. The new finite model
grounds those formulas at budget zero and supplies the full trace
proof and a selection-conditioning counterexample.

The exact existing prerequisite interfaces are
`thm:p17-information-policy-value`,
`thm:p17-information-value-bounds`, and
`thm:p17-sequential-backward`. The finite comparison and Bellman
treatments were read in actual LaTeX before writing. Their assumptions
are restated where imported; the numerical metareasoning model still
supplies its own computational state, feasible actions and transition
mechanism. It does not use a Bellman fixed-point equation as an unproved
assertion that its desired controller exists.

## Applications and empirical boundaries

All source application and further-work pages were read. The chapter
retains the single-step approximation, the separate individual-node
meta-greedy restriction, frontier expansion and backup mechanism,
qualitative allocation cases, DTA* cost-ratio comparisons, MGSS* barrier,
and the proposed retention/memory/architecture/theorem-proving directions.
The source refers detailed game/search algorithms and proofs to its
distinct 1988 technical report; the current chapter does not falsely
claim to reproduce that report's full algorithmic presentations.

Table 1 at printed p. 410 is a reported 32-game Othello tournament:
16 random starts with reversed colors, wins 22 versus 10, time entries
1095 versus 1261 seconds, and node entries 190077 versus 279697. The table
does not label time/node entries with a per-game or whole-tournament
denominator. The chapter keeps that uncertainty rather than inventing
an aggregate normalization. It does not claim raw-data reproduction,
independent game outcomes, a confidence interval or a universal performance
guarantee. Figure 4's tasks, axes and compared algorithms were visually
checked; no precise unprinted numeric data were manufactured from its curves.

## Author checks and return

Eight complete reciprocal statement/proof pairs cover induced kernels,
baseline/calibration, subtree/dependence, finite optimal control,
actual-policy trace expectation, approximate-score loss, regress/overhead,
and the complete numerical program. The body contains no editorial
proof environment. No new calculus sheet is needed: the executable
blocks and numerical recursions are defined in their methods and proofs,
without creating an inference calculus. The author supplied one new
bibliography key and twenty-four symbol rows in disjoint intakes.

The complete body and annex were read sequentially. During that pass,
the intention's action versus vector-index convention was made explicit,
eventual action/integrability was added to the complete-trace expectation,
and the reported time/node denominator was kept unspecified. The four
input traces, partial-step values, total net improvement, control overhead,
correlated-versus-independent example and score-error inequality were
checked directly as finite mathematical calculations. These are authoring
checks, not an independent admission of the treatment.

No shared driver, canonical bibliography, canonical symbol file, style or
coverage baseline was changed. Lead integration remains required. No
software tests mirroring prose, review wave, manuscript build or manuscript
render was performed. The complete source-specific authoring is supplied;
independent review, integration and publication gates retain their standing.

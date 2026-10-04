VERDICT: REJECT

# Round 7 mathematical/definedness review: N-c-016

The frozen 2,051-line presentation is close, but three line-specific domain or scope defects remain. Each changes the literal mathematical claim, so acceptance is not available until all three are repaired.

## Must-fix findings

1. **`handbook/parts/p09/presentations/n-c-016.tex`, lines 519--523: the IPN variable vector is quantified too broadly.** The text defines the IPN using “a vector \(\mathbf X\) of all program variables.” The controlling Queille--Sifakis note records only a vector of variables and also records that the translator deletes internal variables of non-specified types (`p09-queille-sifakis-1982-source-note.md`, lines 200--220). Thus “all program variables” incorrectly includes source-program variables that need not survive into the analyzed IPN. This is not repaired by the later implementation restriction to Boolean, enumerated, and bounded-integer variables at presentation lines 891--896. **Minimal repair:** replace “of all program variables” with “of the variables retained in the interpreted Petri net” (or simply “of variables”), and state in the same paragraph that internal variables of non-specified types may be deleted by the translator. The guarded-command type \(c_i(\mathbf X)\to\mathbf X:=\alpha_i(\mathbf X)\) can then remain unchanged.

2. **`handbook/parts/p09/presentations/n-c-016.tex`, lines 1016--1025: the displayed \(R\)-generability equivalence lacks its infinite-path-set domain.** Earlier, at lines 919--922, \(X\) is allowed to contain nonempty finite as well as infinite sequences. The left side of the displayed equivalence requires \(X\) to equal a set of *infinite* \(R\)-paths, but the right side lists only suffix closure, fusion closure, limit closure, and state completeness. Those four properties do not exclude finite members. For example, with \(S=\{s\}\) and \(X=S^+\cup S^\omega\), the right side holds, but no relation can generate exactly \(X\) as its infinite paths because \(X\) also contains every nonempty finite string. The controlling source note expressly states the three-closure characterization “for sets of infinite paths” (`p09-emerson-halpern-1986-source-note.md`, lines 153--169). The newly supplied state-completeness conjunct correctly repairs totality over all of \(S\), but it does not repair this separate domain omission. **Minimal repair:** introduce the definition and equivalence with “For an infinite-path set \(X\subseteq S^\omega\)” (or add \(X\subseteq S^\omega\) explicitly to the right side), while retaining state completeness.

3. **`handbook/parts/p09/presentations/n-c-016.tex`, lines 1596--1598: nonemptiness alone is incorrectly said to supply an exact input to the finite host method.** Method `def:p09-ctl-labelling` requires a *finite total* transition structure and a CTL formula (`logic-in-computer-science.tex`, lines 974--1007); the inherited definition of total transition structure also requires a nonempty state set (`temporal-epistemic-supplement.tex`, lines 46--56). For the Baier--Katoen bridge, \(S\ne\varnothing\) plus the no-terminal-state condition proves that \(R_0\) is total, but it does not prove that \(S\) is finite. Presentation lines 1606--1608 subsequently state the correct finite condition, leaving the earlier “exact typed input” sentence locally false for an infinite source transition system. **Minimal repair:** change lines 1596--1598 to “When \(S\ne\varnothing\) and the source transition system is finite, together with \(\mathcal K_0=(S,R_0,V_0)\), it supplies the exact typed input ...”; alternatively, say there only that the translation has the host formula/valuation types and reserve the method-instantiation claim for lines 1606--1608.

## Bounded positive evidence

- The repaired factorization at presentation lines 441--488 is mathematically total: every discriminator has an explicit finite domain and a value at every global node, every initial node initializes it, every global arc updates it to the target value, guards remove only the moving process's own region atom, empty guard parts are `true`, and local transitions are partitioned by complete update map. In particular, identity and nonidentity updates are no longer merged.
- The added state-completeness conjunct at lines 1018--1029 is the correct repair for the requirement that a total \(R\subseteq S\times S\) produce a path from every ambient state. Finding 2 is only the remaining, independent requirement to restrict the characterization to \(X\subseteq S^\omega\).
- The empty-state bridge at lines 1606--1615 is otherwise correct: nonempty finite source systems instantiate the host method, while \(S=\varnothing\) forces \(I=\varnothing\), gives empty satisfaction sets and vacuous system satisfaction, and does not instantiate the host's nonempty-state definition. The distinction between the action-labelled transition count \(K\) and the collapsed binary-edge count \(|R_0|\) is also preserved.
- The other audited surfaces are internally typed and directionally correct: positive-arity process and region indices; nullary finite-family conventions; finite and infinite execution domains; pointwise transformer union, intersection, iteration, and image-finiteness; CTL/CTL* state/path ownership; least/greatest fixed-point directions; the \(n\geq1\) Hamiltonian base domain; witness-system directions; proof-versus-citation/reconstruction boundaries; representation-sensitive complexity qualifications; and the 1999 acquisition boundary.
- The supplied technical-name rule is met on the reviewed names that carry mathematical work: synchronization skeleton, global system flowgraph, model fragment, interpreted Petri net, state completeness, stage, and the metalinguistic bridge/translation abbreviations are given a necessity or source role, an eliminable definition, a standing, a distinction from neighboring notions, and an actual later use. No additional technical-name must-fix was found.

## Explicit non-claims

- This is a mathematical/definedness review of the specified text snapshot, not a source-fidelity, publication, admission, or visual review.
- The source notes were treated as the permitted controlling text evidence. Their descriptions of PDFs, scans, web routes, and historical bodies were not independently rechecked here.
- No conclusion is drawn about a manuscript render, TeX compilation, cross-reference resolution, typography, pagination, or visual quality.
- No claim is made that the cited but unproved results have been independently proved in this review. The report checks whether the presentation preserves their stated hypotheses, directions, and proof boundaries.

## Substantive text read

- `handbook/parts/p09/presentations/n-c-016.tex`, lines 1--2051, complete through EOF.
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 945--1036 and 1500--1525.
- `handbook/parts/p08/temporal-epistemic-supplement.tex`, lines 42--190.
- `spec/research/p09-clarke-emerson-1981-source-note.md`, lines 1--884, complete through EOF.
- `spec/research/p09-queille-sifakis-1982-source-note.md`, lines 1--867, complete through EOF.
- `spec/research/p09-emerson-halpern-1986-source-note.md`, lines 1--729, complete through EOF.
- `spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md`, lines 1--470, complete through EOF.
- `spec/research/p09-baier-katoen-2008-ch6-source-note.md`, lines 1--1120, complete through EOF.
- `handbook/bib/handbook.bib`, lines 2393--2407, 2409--2422, 2424--2436, 2438--2447, 2449--2458, 4815--4824, 4826--4835, 4837--4846, and 4897--4906.

## Prohibitions observed

- I did not open any prior N-c-016 review or report, including any earlier mathematical report; any source-fidelity or publication report; any board, admission, handoff, or history file; any parent conclusion; or any other agent output.
- I did not contact, inspect, or delegate to another agent.
- I did not inspect any PDF, manuscript render, screenshot, page image, historical publication file, or web source, and I did not browse the web.
- I did not run a TeX build, test, checker, validator, repository script, hash, executable source tool, or other manuscript verification command.
- I modified no manuscript or repository artifact other than this designated Round 7 report.

REGISTER STATUS: OPEN

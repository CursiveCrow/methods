# N-c-012 integrated source-fidelity review — Round 4

## Scope and method

I read the complete actual LaTeX presentation
`handbook/parts/p09/presentations/n-c-012.tex` directly from line 1 through
line 3024 (EOF). I also read the actual current controlling passages of
`handbook/parts/p09/logic-in-computer-science.tex`: the LTL and past semantics,
strict/inclusive translations, public temporal theorems, safety/liveness,
infinite-word automata, LTL model checking, and presentation-input seam at
lines 602--910, together with the later public complexity summary at lines
2243--2246.

I did not read any prior integrated review report. I used the five source notes
only selectively as supporting source records; I did not re-review the
historical source bodies, and no topic-review record was needed for the
verdict. The findings and citations below are based on the live `.tex` text.

No manuscript PDF, PNG, page image, render, screenshot, test, checker,
repository script, TeX command, build, or hash was used. The only workspace
write is this review record.

## Result

No blocking source-fidelity or integration finding remains.

## Line-evidenced audit

### R4-SF-01 — The five source boundaries remain explicit and nontransferable

The presentation keeps the five accounts disjoint: Kamp occupies
`n-c-012.tex:6--361`, Pnueli `:363--1201`, GPSS `:1203--1838`,
Sistla--Clarke `:1840--2634`, and Alpern--Schneider `:2636--3010`. Their
publication and rights boundaries are independently stated at `:8--14`,
`:365--370`, `:1205--1214`, `:1842--1865`, and `:2997--3009`. The closing
boundary paragraph then distinguishes their objects, temporal conventions,
decision problems, and proof ownership explicitly at `:3011--3024`; in
particular, it forbids one presentation from retroactively supplying another's
definitions, proofs, or terminology (`:3020--3024`).

Proof ownership is likewise preserved rather than flattened. Kamp's printed
and handbook-repaired arguments are separated at `:343--361`; Pnueli's
completeness sketch, its unspoken gaps, and its externally owned Appendix A
results are separated at `:618--676` and `:1123--1152`; GPSS's outline and
external referrals are identified at `:1545--1649` and `:1651--1776`;
Sistla--Clarke's uneven proof boundary is recorded at `:2424--2430` and its
journal repair boundary at `:2595--2601`; Alpern--Schneider's printed proofs,
stated-only equivalences, and handbook repairs are separated at `:2865--2907`,
`:2915--2975`, and `:2997--3006`.

### R4-SF-02 — Pure \(K_b\) is not conflated with the system-dependent rules

The pure future calculus is defined exactly at `n-c-012.tex:819--898`: its
language has inclusive \(F,G\), its propositional basis is G1--G3 with RT, RG,
and MP (`:819--868`), and \(K_b\) is explicitly identified as that pure theorem
system, not a formula or model class and not either later GPSS system
(`:887--898`). Its source completeness claim is correctly retained only as a
model-class-unresolved assertion (`:900--928`).

The system data and system-dependent forms are introduced separately at
`:930--990`. The action partition and infinite-occurrence premise are stated at
`:930--946`; I1, I2, E, and N are displayed with their transition premises at
`:948--976`; and N's fairness-relative semantic domain and the two-phase proof
standing are explicit at `:978--990`. DI and DN are then correctly identified
as derived strengthenings rather than primitives (`:992--1018`).

Most importantly for this round, Theorem 3 is no longer presented as a proved
embedding into bare \(K_b\). The live text states the source's skeletal
comparison, observes that translated ER axiom A1 requires the system-dependent
rule E, notes that E is absent from pure \(K_b\), and records both the
comparison and relative-completeness corollary only as unresolved source
assertions (`:1020--1029`). This conclusion is consistent with the exact pure
and system-dependent definitions immediately preceding it and does not leak
into any public theorem.

### R4-SF-03 — P1 has the correct domain and strength

The transition closure and reachable set are defined before P1 at
`n-c-012.tex:433--450`, including the reflexive case and \(s_0\in X\). P1 is
then exactly reachable-state induction: initial truth plus preservation across
every transition yields truth at every reachable state (`:480--489`). The
sequential application correctly says substitution reduces the invariant proof
to initial and per-instruction obligations and that P1 yields invariance only
after those obligations are proved (`:678--711`). It is not promoted into a
temporal axiom or confused with the later finite-system axiom P.

### R4-SF-04 — Strict and inclusive temporal conventions are bridged exactly

Kamp's source argument order, strict witness, and open interval are displayed at
`n-c-012.tex:74--98`. GPSS's strict future convention, the repaired direction
of its isolated printed inequality, and the handbook-supplied strict past dual
are disclosed at `:1216--1280`. The exact discrete bridge to inclusive strong
until/since is then given in both directions at `:1296--1317`, with the
necessary next/previous operators retained.

The public chapter agrees. It reuses inclusive future LTL and defines inclusive
previous/since at `logic-in-computer-science.tex:605--626`; it preserves Kamp's
complete-order converse domain and refuses to import GPSS's undefined gap
symbols at `:628--637`; and it gives both full recursive translations at
`:639--685`. The formulas preserve operand order as well as strictness:
strict \(U\,B\,A\) and \(S\,B\,A\) translate through \(\mathsf X\) and
\(\mathsf Y\), while the reverse translation uses \(\bot\) to force an
immediate neighbor (`:643--674`). The text expressly states that inclusive
\(\mathsf U,\mathsf S\) alone are not credited with next/previous expressive
power (`:676--685`).

The public first-order theorem consequently has the right domain and strength:
pointed \((\mathbb N,<)\)-words, one free position variable, Kamp's strict
two-direction language, and the equivalent inclusive language with
\(\mathsf X,\mathsf Y,\mathsf U,\mathsf S\)
(`logic-in-computer-science.tex:687--694`). It neither promotes GPSS Theorem
2.5's undefined operators nor converts a source outline into a locally complete
proof.

### R4-SF-05 — Public complexity, safety/liveness, and automata claims retain their domains

The public satisfiability theorem states PSPACE-completeness for the inclusive
\(L(U,X)\) basis and separately preserves the source's other operator-sensitive
rows (`logic-in-computer-science.tex:696--711`). This matches the live source
presentation's inclusive semantics (`n-c-012.tex:1867--1934`), existential-path
problem (`:1936--1974`), Theorem 4.1 bases (`:2211--2216`), and complete Table I
scope (`:2603--2634`). The public squeeze argument uses exactly
\(L(U)\subseteq L(U,X)\subseteq L(U,S,X)\), without importing ETL
(`logic-in-computer-science.tex:701--710`).

The public safety/liveness definition is semantic rather than typographical
(`logic-in-computer-science.tex:713--721`). It agrees with the source
presentation's nonempty state domain and exact bad-prefix/continuation
quantifiers (`n-c-012.tex:2636--2708`), its warning against transition-system
relativization without an explicit new domain (`:2730--2733`), and its
topological characterization and decomposition strengths (`:2844--2907`).

The automata/model-checking passage is sourced and scoped independently of
Sistla--Clarke's non-automata PSPACE proof. Word-automaton standings and
acceptance domains are explicit at `logic-in-computer-science.tex:723--746`;
the LTL-to-Büchi theorem is assigned to Vardi--Wolper at `:748--757`; and the
finite total structure, induced alphabet, product initialization, cyclic-SCC
criterion, counterexample form, combined-input bound, and fixed-formula bound
are all explicit at `:764--812`. The presentation itself says Pnueli's Appendix
B is only a printed language recursion and imported inclusion route, not a
later LTL-to-Büchi construction (`n-c-012.tex:1154--1201`), while
Sistla--Clarke's upper bound is explicitly identified as non-automata-theoretic
(`:2211--2430`). The public complexity summary preserves the same combined and
fixed-formula boundaries (`logic-in-computer-science.tex:2243--2246`).

### R4-SF-06 — ETL is now a well-formed least class on the disclosed grammar domain

The regular right-linear grammar forms are stated at
`n-c-012.tex:2432--2437`. The handbook then expressly restricts each emitted
terminal word to be nonempty because the printed consistency machinery has no
empty-emission case; it identifies this as a handbook restriction and withholds
the epsilon-admitting extension (`:2437--2442`). Every production emitting
\(r\ge1\) terminals is normalized by a chain of \(r\) single-terminal
productions using fresh nonterminals, with the language preserved and only
linear encoded-size growth (`:2443--2447`). Thus the one-terminal form used by
the later local consistency rule is justified without silently enlarging the
theorem domain.

ETL itself is no longer merely named. It is the least formula class containing
atoms and closed under Boolean negation/conjunction, inclusive \(X,U,S\), and
the grammar-indexed constructor for every nonterminal and ETL argument tuple
(`:2448--2454`). Its standing, nonredundancy, and use are stated at the same
location: it is a formula class, not a grammar, automaton, or proof system; the
grammar-indexed formation rule distinguishes it from the ordinary fragments;
and Theorems 5.3--5.4 and Table I require that distinction (`:2454--2457`). The
finite/infinite generated-word semantic domains are separately typed at
`:2465--2483`.

### R4-SF-07 — Theorem 5.4 and Table I have the correct input and problem scope

Theorem 5.4 is stated only for satisfiability and existential truth in an
\(R\)-structure, with grammars encoded as part of the input and with the
handbook's nonempty-emission restriction in force
(`n-c-012.tex:2546--2549`). The complete encoded formula-and-grammar length is
distinguished from terminal count and constructor arity at `:2550--2559`, and
the one-terminal positive rule and negated-constructor continuation check are
given at `:2560--2596`.

The final table separately records satisfiability, validity, and existential
\(R\)-truth (`:2603--2624`). Its ETL row remains under the nonempty-emission
convention, while the \(L(U,X)\) row is identified as a table classification
whose PSPACE membership also follows by the adjacent-language squeeze
(`:2625--2634`). Nothing in the public theorem or later complexity summary
promotes Theorem 5.4 to a different grammar domain, hides the grammar encoding,
or substitutes universal-path truth for the source's existential problem.

### R4-SF-08 — The input seam and final cross-source boundary are coherent

The public temporal definitions and theorems close before the source
presentations are input. The existing figures are referenced at
`logic-in-computer-science.tex:900--902`; N-c-012 is input exactly once at
`:904`, followed by the three other temporal source presentations at
`:905--907`; and the next top-level section begins at `:909--910`. The seam is
therefore inside the temporal-logic-and-automata section, after the public
surface it supports and before the separate model-checking section, with no
domain or theorem statement split across the input boundary.

The final N-c-012 paragraph then restates the five-way boundary accurately:
Kamp's strict order expressiveness, Pnueli's transition-system rules and
strict/inclusive internal tension, GPSS's strict future language and discrete
bridge, Sistla--Clarke's inclusive operator-sensitive decision problems, and
Alpern--Schneider's semantic property classes (`n-c-012.tex:3011--3024`).

### R4-SF-09 — The five-part technical-name rule is satisfied

The load-bearing local names pass necessity, definition, standing,
nonredundancy, and use at their introduction sites. Representative checks are:

- \(K_b\): exact calculus, theorem-system standing, distinction from DX/DUX,
  and immediate Theorem 2/3 use at `n-c-012.tex:887--898`.
- \(\varphi\leadsto\psi\): exact strict statement-family definition,
  state-assertion standing, distinction from the handbook LTL grammar, and
  program-specification use at `:461--478`.
- proper execution and \(\models_{\rm prop}\): exact path and semantic-relation
  definitions, arbitrary-start/initial-start distinction, and finite-theorem
  use at `:1041--1066`.
- \(L_{\rm prop}(\Sigma)\): exact language definition, language standing,
  distinction from the source automaton notation, and inclusion use at
  `:1161--1198`.
- strict \(\mathsf U_s,\mathsf S_s\) and public \(\tau,\sigma\): eliminable
  definitions, formula/translation standing, convention distinctions, and
  immediate bridge use at `n-c-012.tex:1253--1317` and
  `logic-in-computer-science.tex:651--685`.
- ETL, the complete input length \(\ell_{\mathrm{in}}\), and the continuation
  set \(\varphi\): exact definitions, metalinguistic or formula-class standing,
  distinctions from neighboring arities/valuations/trees, and proof use at
  `n-c-012.tex:2448--2464`, `:2550--2559`, and `:2575--2595`.

Conversely, names which the sources do not define are not adopted as
handbook-defined answers: GPSS's \(S',U'\) remain source-reported symbols with
missing grammar and semantics (`n-c-012.tex:1536--1543`), its event expressions
remain an identified proof-outline omission (`:1625--1636`), and its conflicting
\(\mathsf U^0\) displays are expressly not combined into one coherent operator
(`:1778--1805`). This is the required owed-artifact treatment rather than
premature terminology.

VERDICT: ACCEPT

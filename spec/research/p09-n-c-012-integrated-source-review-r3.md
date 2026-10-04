# N-c-012 integrated source-fidelity and integration review — Round 3

## Scope and method

This is a blind review of the actual current LaTeX, not of a generated or
derived manuscript artifact. I read
`handbook/parts/p09/presentations/n-c-012.tex` completely and directly from
line 1 through its end at line 3010. I also read the actual current integration
passages in `handbook/parts/p09/logic-in-computer-science.tex`: the reused LTL
and past definitions, strict/inclusive bridge, discrete-word and complexity
theorems, safety/liveness definition, infinite-word automata and model-checking
interface, and the `\input` seam (principally lines 601--811 and 899--905).

As supporting source records, I read the five permitted source notes for Kamp,
Pnueli, GPSS, Sistla--Clarke, and Alpern--Schneider, together with the five
permitted independent-review records. I did not read an integrated N-c-012
review report and did not contact another reviewer. The earlier verdicts in
those records were not carried forward: every conclusion below is based on the
current LaTeX line evidence.

No manuscript PDF, page image, render, screenshot, or other derived manuscript
artifact was inspected or used. No TeX command, build, test, checker,
repository script, or hash was run or used for this review.

## Finding register

No blocking or nonblocking source-fidelity, mathematical-integration,
proof-ownership, rights-boundary, or technical-name finding remains in the
reviewed scope.

## Five-presentation source-fidelity review

### 1. Kamp 1968

- **Source and rights distinction.** The manuscript identifies the complete
  UCLA dissertation through Kamp's Stuttgart institutional bibliography and
  expressly distinguishes lawful scholarly access from republication rights;
  it says the account is independently reconstructed and cites printed thesis
  pages (`n-c-012.tex`, lines 8--14). This is neither a public-domain claim nor
  a reproduction of the scan.
- **Order domain and model standing.** The four source classes are defined as
  classes of strict linear orders, with density, conditional discreteness, and
  order-theoretic completeness kept distinct (`n-c-012.tex`, lines 16--40).
  The examples correctly show that completeness neither implies density nor
  excludes discreteness or endpoints. The first-order language, absence of a
  displayed equality symbol, current-point assignment, and uniformity over an
  order class are all stated before use (`n-c-012.tex`, lines 42--72).
- **Strict semantics and operand order.** Kamp's `S(A,B)` and `U(A,B)` use a
  strict witness, put the first argument at that witness, and put the second
  argument only on the open interval (`n-c-012.tex`, lines 74--98). The
  expanded capture-avoiding translation preserves exactly that convention
  (`n-c-012.tex`, lines 100--131).
- **Theorem strength and proof ownership.** The manuscript separates the
  all-binary-structure temporal-to-first-order induction from the
  completeness-dependent first-order-to-temporal construction over
  `Com` (`n-c-012.tex`, lines 126--155). It does not turn Kamp's expressive
  completeness into proof-calculus completeness or a complexity result. The
  rational-order counterexample is kept separate from literal Chapter IV
  Theorem 3 (`n-c-012.tex`, lines 157--165 and 167--231).
- **Printed defect and handbook repair.** The false unrestricted square-offset
  clause is quoted and refuted, the same-parity premise is explicitly owned by
  the handbook, and the repaired constructor-by-constructor induction is
  supplied before the non-expressibility conclusion (`n-c-012.tex`, lines
  256--341). Adjacent Chapter IV results and their proof standings remain
  distinct (`n-c-012.tex`, lines 343--361). No scholarly qualification was
  lost when process-oriented review prose was removed.

### 2. Pnueli 1977

- **Source, version, rights, and program model.** The author-hosted FOCS body is
  distinguished from its May 1981 archival wrapper, and public access is not
  treated as an open licence (`n-c-012.tex`, lines 363--370). The dynamic
  system, infinite initial-state executions, sequential specialization,
  concurrent interleaving, atomicity choice, and informal enabled-processor
  condition are typed and separated (`n-c-012.tex`, lines 372--431).
- **Strict temporal implication versus inclusive tense operators.** Pnueli's
  local `\leadsto` family has the literal strict witness `j>i` and is explicitly
  a relation between state assertions rather than a primitive of the shared
  LTL grammar (`n-c-012.tex`, lines 433--478). The later recursively defined
  `F` and `G` include the present (`n-c-012.tex`, lines 819--845). The
  manuscript preserves, rather than silently harmonizes, the resulting source
  tensions (`n-c-012.tex`, lines 517--541 and 668--676).
- **P1.** Reachability is first defined using reflexive--transitive `R^*` and
  `X={s:R^*(s_0,s)}` (`n-c-012.tex`, lines 433--450). P1 then has exactly the
  required induction shape: initial truth plus preservation across every
  transition yields truth at every state in `X` (`n-c-012.tex`, lines
  480--489). Its later Floyd-style use correctly reduces verification to
  initial and per-instruction obligations and derives invariance only after
  those obligations are proved (`n-c-012.tex`, lines 678--711).
- **P2, ER, and Theorem 1.** The zero-rank typing repair is disclosed without
  being promoted to a soundness repair; both the missing zero boundary and the
  independent strict-future counterexample are retained (`n-c-012.tex`, lines
  490--541). R4 and metarule I receive typed parameter/eigenvariable standing
  (`n-c-012.tex`, lines 543--616). Theorem 1 remains a source proof sketch with
  its assertion-language and pointwise finite-branching hypotheses, and both
  the arbitrary-start/reachability gap and the nonserial deadlock-vacuity gap
  remain explicit (`n-c-012.tex`, lines 618--666).
- **Local `K_b`.** The manuscript defines `K_b` locally and exactly as the pure
  propositional future calculus with derived `F:=\neg G\neg`, G1--G3, and RT,
  RG, and MP; it states that this is a theorem system, not a formula or model
  class, and distinguishes it from GPSS's `DX` and `DUX` (`n-c-012.tex`, lines
  847--898). Its source-reported completeness is correctly left model-class
  unresolved, with a concrete linear/S4 separation (`n-c-012.tex`, lines
  900--928). Later uses stay within that local standing: Theorem 3's skeletal
  ER comparison (`n-c-012.tex`, lines 1020--1028) and the finite-system
  extension in Theorem 5 (`n-c-012.tex`, lines 1096--1117).
- **Proof and automata boundaries.** The action-occurrence restriction is not
  equated with the earlier fairness prose (`n-c-012.tex`, lines 930--990).
  Proper executions, restricted system validity, SCC reasoning, P/MRG, and the
  two clauses of Theorem 5 are kept distinct (`n-c-012.tex`, lines
  1030--1117). Appendix A separates externally owned T2/T3 from Pnueli's local
  six-step lemma (`n-c-012.tex`, lines 1119--1148). Appendix B attributes only
  the acceptor assertion, language recursion, imported closure machinery, and
  inclusion decision at their respective standings; it expressly denies that
  Pnueli supplied the later LTL-to-Büchi translation or a complexity class
  (`n-c-012.tex`, lines 1150--1197).

### 3. GPSS 1980

- **Published object and rights.** Printed authorship controls over incomplete
  embedded metadata, the 1980 ACM notice is not treated as an open licence, and
  the prose is expressly an independent reconstruction (`n-c-012.tex`, lines
  1199--1210).
- **Strict source language.** The initial grammar, linear-order model, strict
  `F/G`, one-sided source `X` clause, and the p. 164 reversed-inequality defect
  are all preserved (`n-c-012.tex`, lines 1212--1247). Local `U_s` has the
  source's strict witness and operand order; `S_s` is explicitly a
  handbook-supplied order dual rather than a source transcription
  (`n-c-012.tex`, lines 1249--1276).
- **Strict/inclusive bridge.** On omega-models, the exact two-way bridge uses
  next and previous: strict `U_s/S_s` translate to `X/Y` of inclusive strong
  `U/S`, and inclusive `U/S` add the present case (`n-c-012.tex`, lines
  1292--1313). The text explicitly blocks the false substitution of inclusive
  `U` into the source equation `XA = bottom U_s A`.
- **Theorem domains and ownership.** The four first-order result packages are
  not collapsed: point zero on omega-models, future formulas at every point of
  discrete complete models, mixed past/future separation over discrete
  complete models, and arbitrary linear orders only with undefined gap symbols
  (`n-c-012.tex`, lines 1473--1539). The normal-form passage remains a source
  outline with external `[SS]` and `[G2]` ownership and omitted event-expression
  machinery (`n-c-012.tex`, lines 1541--1645). `DX` and `DUX` are defined as
  theorem systems at their exact omega-validity strength, and the canonical
  construction's unprinted lemmas, finite-quotient step, adjacency omission,
  and truth-lemma omissions remain visible (`n-c-012.tex`, lines 1647--1772).
  The incompatible p. 173 `U^0` displays and the qualified `D^0UX` claim are
  likewise retained (`n-c-012.tex`, lines 1774--1834).
- **Kamp and Pnueli boundaries.** GPSS's compressed Kamp-IV.3 attribution is
  reported without pretending that Kamp printed the missing reduction
  (`n-c-012.tex`, lines 1457--1471). The subsection does not retroject GPSS's
  strict `U`, expressive theorems, or `DX/DUX` proof systems into Pnueli 1977.

### 4. Sistla--Clarke 1985

- **Version and rights boundary.** The 1985 JACM article controls over the
  distinct 1982 STOC predecessor, including the corrected regular-operator
  argument; the author-archive scan is reading access rather than a
  republication licence (`n-c-012.tex`, lines 1836--1861).
- **Inclusive semantics and decision domains.** The source grammar and
  operator-sensitive fragment notation are defined before the complexity
  claims (`n-c-012.tex`, lines 1863--1900). `X`, inclusive strong `U`, and
  inclusive `S` have the correct omega-word clauses, explicitly distinguished
  from GPSS's strict convention (`n-c-012.tex`, lines 1902--1930). The
  finite `R`-structure problem retains its existential path quantifier, while
  validity is disclosed as a journal-relative reconstruction supported by the
  conference predecessor (`n-c-012.tex`, lines 1932--1970).
- **Theorem strength and proof ownership.** NP results remain restricted to
  `L(F)` and atomic-negation `tilde L(F,X)`; richer bases remain PSPACE, with
  the exact Table I rows preserved (`n-c-012.tex`, lines 2590--2620). The
  manuscript keeps the acceptable-subsequence strict-sign defects and
  proof-supported non-strict bounds distinct (`n-c-012.tex`, lines
  2047--2102), the current-inclusive reading of source word “after” distinct
  from the separate singleton-cycle correction (`n-c-012.tex`, lines
  2159--2194), and all periodic truth-set and until-discharge obligations
  distinct (`n-c-012.tex`, lines 2280--2418). It also states the uneven proof
  granularity rather than converting the proof into an automata argument
  (`n-c-012.tex`, lines 2420--2426).
- **ETL formation, standing, and use.** `ETL` is defined as the least formula
  class containing atoms and closed under Boolean negation/conjunction,
  inclusive `X/U/S`, and the grammar-indexed formation rule
  `N_j(f_1,...,f_n)` (`n-c-012.tex`, lines 2428--2446). The same location says
  exactly what it is not (grammar, automaton, proof system), why the distinction
  from ordinary fragments is needed, and where it is used. Its finite/infinite
  generated-word semantics and constructor standing are then typed
  (`n-c-012.tex`, lines 2454--2472); the parity conflict is retained without an
  invented repair (`n-c-012.tex`, lines 2474--2483). The extended closure,
  labelled continuation tree, fulfilment obligation, periodic theorem, encoded
  input-length renaming, and on-the-fly rules are all used in the stated
  Section 5 proof chain (`n-c-012.tex`, lines 2485--2588), culminating in the
  `ETL` PSPACE row (`n-c-012.tex`, lines 2590--2620). Formation, standing,
  nonredundancy, and use are therefore all present.

### 5. Alpern--Schneider 1985

- **Semantic universe, not formula typography.** The source classifies
  arbitrary properties `P subseteq S^omega`; finite prefixes, infinite
  executions, membership standing, program denotation, and terminal-state
  padding are all typed before the class definitions (`n-c-012.tex`, lines
  2622--2657). The operationally implicit `S != empty` hypothesis and its exact
  topological necessity are expressly disclosed (`n-c-012.tex`, lines
  2659--2664).
- **Exact safety/liveness strength.** Safety uses an irremediable finite bad
  prefix, while liveness gives every finite prefix some satisfying continuation
  (`n-c-012.tex`, lines 2666--2694). The clauses range over the full
  `S^omega`, not the paths of a fixed transition system (`n-c-012.tex`, lines
  2716--2719). Uniform and absolute liveness receive distinct quantifier
  definitions, semantic standing, nonredundancy, and immediate use in the
  inclusion chain and examples (`n-c-012.tex`, lines 2721--2818).
- **Theorems, repairs, and ownership.** The neither-class examples block a
  false dichotomy (`n-c-012.tex`, lines 2820--2828). Safety/closed and
  liveness/dense are stated with handbook-supplied direction proofs
  (`n-c-012.tex`, lines 2830--2849). Theorem 1 remains an existence theorem and
  its expressibility corollary remains conditional (`n-c-012.tex`, lines
  2851--2893); Plotkin's statement remains an unverified private-communication
  report (`n-c-012.tex`, lines 2895--2899). Theorem 2 retains `|S|>1`, and the
  printed Corollary 2.1 defect, countermodel, and handbook-owned union-closure
  repair are all separate (`n-c-012.tex`, lines 2901--2961).
- **Source and rights.** The journal/report agreement, source-versus-handbook
  proof boundary, methodological status, and controlling copyright notice are
  all retained (`n-c-012.tex`, lines 2983--2995).

## Cross-presentation and shared-file integration

1. **Shared inclusive language.** The current Part IX definition reuses the
   Part VIII infinite-word LTL operators and adds inclusive previous/since with
   exact pointed-word clauses (`logic-in-computer-science.tex`, lines
   604--625). It does not silently identify those constructors with Kamp's or
   GPSS's strict ones.
2. **Order-domain warning.** The shared prose retains the unequal Kamp
   directions and the `Com` boundary, the rational counterexample, and GPSS's
   undefined gap-symbol limitation (`logic-in-computer-science.tex`, lines
   627--636).
3. **Exact two-way bridge.** The displayed equations and recursive `tau` and
   `sigma` translations preserve witness strictness and operand order, define
   their metalinguistic standing, and explain why `X/Y` are required
   (`logic-in-computer-science.tex`, lines 638--684). This satisfies the
   technical-name rule at the point of introduction and prevents an
   operator-convention collapse.
4. **Public theorem strength.** The discrete-word first-order theorem includes
   `X/Y` with inclusive strong `U/S` and states the strict formulation
   equivalently (`logic-in-computer-science.tex`, lines 686--693). The PSPACE
   theorem identifies the exact `L(U,X)` basis and preserves the NP and other
   PSPACE fragment distinctions (`logic-in-computer-science.tex`, lines
   695--710).
5. **Safety/liveness interface.** The shared definition uses semantic word
   properties and finite-prefix quantifiers rather than classifying formulas by
   their surface operators (`logic-in-computer-science.tex`, lines 712--720),
   agreeing with the full Alpern--Schneider presentation.
6. **Automata/model-checking interface.** Word-automaton acceptance is defined
   separately (`logic-in-computer-science.tex`, lines 722--745); the later
   LTL-to-Büchi theorem is attributed to Vardi--Wolper, not Pnueli, GPSS, or
   Sistla--Clarke (`logic-in-computer-science.tex`, lines 747--756). The product
   construction consumes the current and successor state labels in the right
   order, requires a reachable accepting cyclic SCC, distinguishes explicit
   product cost from formula translation, and turns existential
   Sistla--Clarke counterexample search into universal checking by complement
   (`logic-in-computer-science.tex`, lines 763--811).
7. **Input seam.** The complete N-c-012 presentation is included once, after
   the definitions and theorems it references and before the later N-c-013--015
   presentations and the next model-checking section
   (`logic-in-computer-science.tex`, lines 899--909). Its references to the
   shared strict/inclusive bridge, safety/liveness definition, omega-automata
   definition, and public theorem labels are therefore resolved at the live
   source seam.
8. **Final Pnueli/GPSS boundary.** Pnueli closes by saying that Appendix B is
   not a later LTL-to-Büchi translation or complexity classification
   (`n-c-012.tex`, lines 1150--1197). GPSS then restarts with its own published
   object, rights notice, strict grammar, and explicit source defect
   (`n-c-012.tex`, lines 1199--1247). The final synthesis states the distinction
   again: Pnueli's strict `leadsto` coexists with his later inclusive `F/G`,
   GPSS is strict, Sistla--Clarke is inclusive and operator-sensitive, and
   Alpern--Schneider is semantic rather than syntactic (`n-c-012.tex`, lines
   2997--3010). No presentation supplies another's definitions, proofs, or
   terminology retroactively.

## Five-part technical-name rule

The current text satisfies the workspace rule. New local names are introduced
only with necessity, definition or explicit source standing, ontological or
metalinguistic standing, nonredundancy, and actual use at the same local
passage. Representative load-bearing cases include Kamp's tense-defining
formulas and operation basis (`n-c-012.tex`, lines 42--72 and 203--231),
Pnueli's `leadsto`, parameterized assertion family, `K_b`, proper execution,
restricted validity, and execution language (`n-c-012.tex`, lines 461--478,
543--616, 887--898, 1030--1062, and 1150--1194), GPSS's `U_s/S_s`, `Pr`,
translations, and `DX/DUX` (`n-c-012.tex`, lines 1249--1313, 1418--1455,
1483--1514, and 1647--1688), Sistla--Clarke's `SF`, ambient-relative
subsequence measures, truth sets, fulfilment obligations, `ETL`, `Gamma`, and
`ell_in` (`n-c-012.tex`, lines 1885--1900, 2022--2047, 2280--2303,
2428--2472, and 2485--2581), and Alpern--Schneider's live-for relation,
uniform/absolute classes, `P_{A,B}`, `L_P`, and `E_a/E_b` (`n-c-012.tex`, lines
2678--2694, 2721--2818, and 2851--2926).

Names whose source bodies do not define the needed object are not laundered
into handbook definitions. GPSS's event expressions and gap symbols remain
explicitly source-reported but formally owed (`n-c-012.tex`, lines 1527--1539
and 1621--1645), and the conflicted `U^0` is expressly not adopted as one
coherent operator (`n-c-012.tex`, lines 1774--1827). This is the correct
application of the rule's “describe the owed artifact” branch.

## Removal of audit prose

The current presentation contains scholarly source qualifications rather than
workflow or admission prose. Removing audit-process language has not removed
any load-bearing qualification: source defects remain identified as source
defects; handbook repairs and reconstructions remain expressly owned; theorem
domains and evaluation points remain explicit; proof sketches, external
referrals, and omitted proofs remain at their actual strengths; rights are not
overclaimed; and the five presentation boundaries remain restated at EOF.
The representative evidence is the Kamp repaired induction (`n-c-012.tex`,
lines 272--361), Pnueli's P2/Theorem 1/model-class qualifications
(`n-c-012.tex`, lines 517--676 and 887--928), GPSS's printed conflicts and
proof-outline limits (`n-c-012.tex`, lines 1233--1247, 1634--1645,
1747--1772, and 1774--1834), Sistla--Clarke's corrected-version and defect
boundaries (`n-c-012.tex`, lines 1838--1861, 2051--2102, 2159--2194, and
2474--2588), and Alpern--Schneider's hypothesis and corollary repairs
(`n-c-012.tex`, lines 2659--2664, 2763--2818, and 2928--2995).

VERDICT: ACCEPT

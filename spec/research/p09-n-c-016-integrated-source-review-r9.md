VERDICT: ACCEPT

# Round 9 source-fidelity disposition

This is a fresh, blind, text-only review of the frozen current N-c-016 LaTeX source. Within the evidence and prohibitions recorded below, I found no source-fidelity, source/host-domain, declaration-order, proof-status, locator, access/rights, bibliography-identity, or technical-name defect that requires a manuscript repair.

The acceptance is deliberately narrow. It accepts the current source text against the specified host/prerequisite spans, five controlling research notes, and five exact bibliography entries. It is not a TeX-build result, a rendered-page or layout result, an independent reinspection of any historical publication object, a new rights determination, a proof of every cited result, or a final admission/board decision.

# Positive evidence

## 1. Clarke--Emerson factorization is now local, typed, and source-bounded

The current factorization passage at `n-c-016.tex` 441--497 no longer reads as a rule for an arbitrary process-labelled global arc.

- Lines 443--458 explicitly label the duplicate-state encoding as a reader-facing typed reconstruction. For each duplicated propositional label \(\Lambda\), \(z_\Lambda\) has the total value domain \(\{0,1,\ldots,d\}\); every global node receives exactly one equality; every designated initial node is initialized; and every global arc assigns the target value. Thus the auxiliary variable is total and its \(0\) value has an exact eliminable meaning outside the duplicate class.
- Lines 461--470 restrict the factorization rule to global \(i\)-arcs that preserve every \(P_j\)-region for \(j\ne i\). They identify requirement group 8 as the premise for the displayed mutual-exclusion construction and expressly exclude a violating arc because a local \(P_i\) transition cannot update another process's region. This agrees with the source's interleaving process model and with the exact group-8 formulas recorded in the Clarke--Emerson note at 609--620.
- Lines 471--480 define \(\gamma_e\) locally from the global source label by removing only the moving process's current-region atom while retaining every other-process region and every true auxiliary equality. They separately define \(\sigma_e\) as the complete auxiliary update map, including identity updates, and state the different standings: \(\gamma_e\) is a state-formula guard, whereas \(\sigma_e\) is a transition update.
- Lines 481--495 factor only arcs with the same local endpoints and the same complete update map. Identity and nonidentity updates remain distinct parallel transitions. The displayed \(P_1\) skeleton at 418--439 provides the later concrete use and demonstrates why the update partition is not decorative.
- Lines 499--511 preserve the exact source boundary: the model checker, the two proved propositions, the abridged tableau, and the worked synthesis/factorization construction have four different proof statuses; no general factorization or synthesis-correctness theorem is invented.

This is consistent with the controlling note's interleaving model at 131--150, the nine requirement groups at 568--626, the published factorization account at 628--662, and its statement that the construction is a detailed worked example rather than a separately numbered general theorem.

## 2. Queille--Sifakis scalars, messages, actions, and places are declared before their technical use

The current declaration order at `n-c-016.tex` 525--590 is source-faithful and type-safe.

- Lines 525--544 first define an interpreted Petri net and \(\mathbf X\) as the vector of program variables retained in that IPN. They explicitly exclude deleted internal variables of non-specified types and distinguish the IPN from an ordinary Petri net by its guards and assignments.
- Lines 556--559 then declare scalar \(X\) as the sender's data value and expressly distinguish it from \(\mathbf X\); \(Y\) and \(Z\) are declared as the sender's and receiver's control bits before \((X,Y)\) first occurs at line 561.
- Lines 572--576 declare \(M\), \(MM\), \(AA\), the bit projection \((\cdot).B\), and the two process identifiers before the property families use them.
- Lines 576--590 give exact program-event standings for `send`, `repeat`, `receive`, `accept`, `repeatack`, `sendack`, and `receiveack` before their first formula occurrences at 706 onward. The text explains their noninterchangeability by the later `after` and `enable` predicates.
- Lines 665--700 define `Init`, `enable`, `after`, the finite-family abbreviations, the process-action-set abbreviation, and the nullary conventions before using them. Lines 781--785 repair the printed `receivack` spelling only after recording that the program and Figure 2 define `receiveack`.
- Lines 866--871 define each lower-case Figure-2 place symbol as a Boolean characteristic predicate before the worked Boolean calculation and distinguish place \(a_i\) from the action metavariable \(a\).

These declarations agree with the Queille--Sifakis note's IPN typing at 198--220, program inventory at 222--301, program-predicate/action definitions at 408--531, fixed-point algebra at 533--630, analyzer boundary at 632--666, and worked calculation at 668--726.

## 3. Every material source and host domain remains explicit

The five presentations do not collapse unlike semantic domains.

- Clarke--Emerson: lines 41--60 distinguish the countable source structure, process-indexed relations, infinite computation-tree paths, per-process skeletons, and the finite global flowgraph. Lines 126--168 separately impose finiteness for the source model checker and keep its \(\operatorname{length}(f_0)|S|^2\) accounting separate from the later edge-sensitive host bound.
- Queille--Sifakis: lines 620--655 distinguish finite and infinite maximal executions and define \(D_s\) so no formula is evaluated at the fictitious post-terminal state \(\omega\). Lines 657--663 identify the source's omitted start/adjacency and Boolean clauses instead of pretending that the printed definition is complete. Image-finiteness remains explicit at 827--849.
- Emerson--Halpern: lines 1007--1028 type every finite/infinite string used in fusion and limit decompositions before stating the closure conditions. Lines 1029--1050 define \(R\)-generability only for \(X\subseteq S^\omega\), require a total \(R\subseteq S\times S\), define state completeness, and state the exact equivalence with suffix, fusion, limit closure, and state completeness. The extra state-completeness conjunct is expressly identified as a handbook qualification forced by totality on all of \(S\), rather than attributed silently to the source's abbreviated three-closure wording.
- Baier--Katoen/source-to-host bridge: lines 1547--1571 retain the action-labelled source tuple and its literal no-terminal-state condition. Lines 1573--1586 define the handbook-only binary relation \(R_0\) and valuation \(V_0\), give their standings, and set the host alphabet exactly to \(AP\). Lines 1588--1617 define the eliminable translation \(\operatorname{tr}\) for every source CTL constructor before instantiating the host method. Lines 1625--1634 instantiate that method only for nonempty finite \(S\), handle \(S=\varnothing\) separately, and distinguish the binary-edge count \(|R_0|\) from the source transition-triple count \(K\). Lines 1698--1716 then state the semantic equivalence and host complexity result only over the qualified nonempty domains.
- Host consistency: `logic-in-computer-science.tex` 948--1017 supplies exactly the finite-total host type, predecessor maps, fixed-point method, correctness statement, and \(O((|S|+|R|)|A|)\) bound used by that bridge. `temporal-epistemic-supplement.tex` 46--185 supplies the inherited nonempty total-transition, CTL state-formula, and CTL* state/path typing. The N-c-016 input occurs once, at the host's line 1519.

No source theorem is strengthened merely by moving it into the host notation.

## 4. Variants, access/rights statements, locators, citations, and proof voice agree with the controlling notes

The source-state boundaries are consistently stated.

- Clarke--Emerson lines 9--18 separate the 1981 meeting, 1982 LNCS publication, authorized 2008 reprint, original/reprint pagination, and distinct longer manuscript. Lines 170--181 record the defective printed until approximant while following the source identity, prose, and algorithm. The tableau remains an outline, and the worked synthesis remains below a general theorem claim.
- Queille--Sifakis lines 516--523 distinguish the authenticated original scan from the subscription-only reprint pages and expressly leave scan-distribution authorization unestablished. Lines 592--597 keep the non-loss premise external to the printed model. Lines 845--849 retain image-finiteness and the delegated Sifakis-1979 proof. Lines 904--914 retain the iteration cap, possible no-answer outcome, and absence of an asymptotic or completeness theorem.
- Emerson--Halpern lines 919--925 distinguish the JACM article from the preliminary and report source states and characterize the ACM terms as conditional copying terms, not an open licence. Lines 1272--1375 preserve the literal defective targets and cross-references of Theorems 5--6 before making only the proof-and-diagram-supported repairs; reader-left and cited dependencies remain marked. Lines 1413--1483 preserve the literal MPL \(U/X\) conflict and do not promote Theorem 10 or the expected TC translation beyond the printed proof boundary.
- Clarke--Grumberg--Peled lines 1513--1534 state only a route-bounded acquisition result as of 22 August 2026. They distinguish preview, controlled lending, institution-only access, and physical availability; use contents data only as locators; substitute no 1996 survey, 2001 chapter, 2008 textbook, or 2018 second edition; and attribute no formula, algorithm, theorem, or complexity claim to the unacquired first-edition body.
- Baier--Katoen lines 1539--1545 retain the all-rights-reserved boundary and corrected page map. The ENF warning, naive and optimized algorithms, fixed-point proof boundaries, worked systems, exact time theorem, CTL/LTL witness omissions, CTL* typing, and source defects remain separated through lines 1718--2070. In particular, the final defect inventory at 2055--2070 does not flatten source-displayed defects or reader-supplied arguments into published proofs.

The bibliography entries at `handbook.bib` 2393--2458 match the five controlling identities and access notes: `ClarkeEmerson1981`, `QueilleSifakis1982`, `EmersonHalpern1986`, `ClarkeGrumbergPeled1999`, and `BaierKatoen2008`. The apparent 1981/1982 distinction in the first key is explained in the prose and the entry correctly gives publication year 1982. The Clarke--Grumberg--Peled entry now exists under the exact cited key and records that no complete body was acquired.

## 5. Technical-name rule

I applied the supplied rule to every substantive new name or abbreviation, rather than treating ordinary quantified variables as proposed technical vocabulary. The current text supplies necessity, an eliminable definition or source axiom, standing, nonredundancy, and later use at the point of introduction for all material cases.

- `synchronization skeleton`, `global system flowgraph`, `model fragment`, `TURN`, \(z_\Lambda\), \(\gamma_e\), and \(\sigma_e\) are each defined, typed, distinguished from neighboring objects, and used by the factorization.
- `interpreted Petri net`, \(\mathbf X\), scalar \(X\), the message/action/place names, \(D_s\), `enable`, `after`, `pre`, \(h^*\), and \(h^x\) are each given exact standings and subsequent computational uses.
- suffix, fusion, and limit closure, \(R\)-generability, state completeness, CTL* state/path formulas, \(B(L)\), the segment abbreviations, and MPL `stage` are defined before the comparisons or translations that need them and are distinguished from object-language operators where necessary.
- \(R_0\), \(V_0\), \(\mathcal K_0\), and \(\operatorname{tr}\) are explicitly handbook-supplied metalinguistic objects, not retrojected Baier--Katoen terminology, and each is required by the typed host instantiation.

I found no hypothetical name standing in place of an owed definition, axiom, existence result, identity condition, or later use.

# Substantive text read

All ranges below were read as text through the stated end; no render was used.

- `C:\Dev\the-methods-of-reason\handbook\parts\p09\presentations\n-c-016.tex`: lines 1--2070, through EOF.
- `C:\Dev\the-methods-of-reason\handbook\parts\p09\logic-in-computer-science.tex`: lines 925--1056 and 1475--1536; the sole N-c-016 input at line 1519 was also checked.
- `C:\Dev\the-methods-of-reason\handbook\parts\p08\temporal-epistemic-supplement.tex`: lines 35--185.
- `C:\Dev\the-methods-of-reason\spec\research\p09-clarke-emerson-1981-source-note.md`: lines 1--884, through EOF.
- `C:\Dev\the-methods-of-reason\spec\research\p09-queille-sifakis-1982-source-note.md`: lines 1--867, through EOF.
- `C:\Dev\the-methods-of-reason\spec\research\p09-emerson-halpern-1986-source-note.md`: lines 1--729, through EOF.
- `C:\Dev\the-methods-of-reason\spec\research\p09-clarke-grumberg-peled-1999-acquisition-note.md`: lines 1--470, through EOF.
- `C:\Dev\the-methods-of-reason\spec\research\p09-baier-katoen-2008-ch6-source-note.md`: lines 1--1120, through EOF.
- `C:\Dev\the-methods-of-reason\handbook\bib\handbook.bib`: lines 2393--2459, containing exactly the five cited entries and their boundaries.

# Prohibitions observed

- I did not open any prior N-c-016 review or report, including any report from an earlier round or one of my own.
- I did not read a mathematical/publication review, admission record, board record, history file, parent conclusion, or other agent output.
- I did not contact, message, or delegate to another agent.
- I did not open or inspect a PDF, rendered handbook page, screenshot, page image, or historical publication file.
- I did not browse the web.
- I did not run a TeX build, test, checker, validator, project script, hash computation, executable source-analysis tool, or publication executable.
- I did not modify the manuscript, host, prerequisite, bibliography, source notes, or any other repository file. This report is the only file written.

# Explicit non-claims

- ACCEPT does not assert that the LaTeX compiles, that references resolve in a build, or that any rendered page is visually correct.
- ACCEPT does not independently verify or enlarge any copyright, copying, distribution, or republication permission. In particular, it does not close the Queille--Sifakis scan-authorization boundary, convert institutional access into an open licence, or make the Clarke--Grumberg--Peled first-edition body available.
- ACCEPT does not claim that every cited theorem has a complete proof in its source. The manuscript's cited, sketched, reader-left, reconstructed, and locally proved statuses remain controlling.
- ACCEPT does not independently re-authenticate the historical publication objects; it is bounded to the five specified text notes and exact bibliography records.
- ACCEPT does not establish final mathematical-publication acceptance, final handbook admission, board closure, or human editorial approval.

REGISTER STATUS: OPEN

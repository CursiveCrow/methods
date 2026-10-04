VERDICT: REJECT

# Round 3 mathematical/definedness review: N-c-016

The frozen 1,884-line presentation is source-aware and is substantially correct on its major logical boundaries, but it is not yet mathematically closed. Eight local, line-specific defects remain. They concern arity/base domains, an underdefined reduction, an index collision, partial/ill-typed path semantics, undefined pointwise operations on predicate transformers, and two underdefined formula/path constructions. Each can be repaired locally; none calls for a structural rewrite or a stronger source claim.

## Must-fix findings

1. **\`n-c-016.tex:38-48, 61-113, 427-435\` — the process-family arity is never typed.** The presentation uses \(P_1,\ldots,P_k\), \(A_1\cup\cdots\cup A_k\), the derived disjunction \(\bigvee_{i=1}^k EX_i f\), and finally \(p=k-1\), but it never states \(k\geq1\). For \(k=0\), the displayed process list and indexed grammar have no members, the totality condition admits the empty-state degeneracy, and \(p=-1\) makes \(S_1,\ldots,S_p\) meaningless. The later convention for the \(k=1\) empty conjunction does not close the \(k=0\) case. **Minimal repair:** begin line 38 with “Fix \(k\in\mathbb N\) with \(k\geq1\) and processes \(P_1,\ldots,P_k\).” Retain the existing \(k=1\) empty-conjunction convention.

2. **\`n-c-016.tex:204-219\` — the Clarke--Emerson Hamiltonian reduction omits both its base domain and the transition construction needed for the claimed equivalence.** The text gives vertex labels and the path formula, but “adjoining a fresh source and a looping sink” does not say which new edges exist. Therefore the assertion at lines 215-217 that a satisfying path encodes a directed Hamiltonian path does not follow from the stated structure. The case \(n=0\) is also left to an unstated convention, under which both the empty conjunctions and “Hamiltonian path” vary. **Minimal repair:** state \(n\geq1\), retain the original edges \(E\), add \(u_1\to v_i\) and \(v_i\to u_2\) for every \(1\leq i\leq n\), add \(u_2\to u_2\), add no other new edges, label \(v_i\) only by \(p_i\), and give the two fresh states none of the \(p_i\). This is exactly the graph needed by the printed proof; do not strengthen the conclusion beyond NP-hardness.

3. **\`n-c-016.tex:432-451\` — \(k\) is simultaneously the process count and an unquantified target-region index.** Lines 38-46 fix \(k\) as the number of processes, lines 432-434 use regions \(R_1,\ldots,R_m\) and set \(p=k-1\), but lines 436-451 then draw \(R_j\to R_k\). Read literally, the target is the region whose index equals the process count, not an arbitrary target region; it may not even exist when \(k>m\). **Minimal repair:** quantify two fresh region indices, for example \(u,v\in\{1,\ldots,m\}\), and replace every \(R_j,R_k\) in lines 436-451 by \(R_u,R_v\). Keep \(k\) exclusively as the process count and \(p=k-1\).

4. **\`n-c-016.tex:555-587\` — the completed Queille--Sifakis execution semantics is still partial at finite executions and states only one direction of its index guard.** Line 564 says \(q\xrightarrow{k}s(k)\) holds “only for” a defined position, which states at most the implication from the arrow to definedness, whereas the source convention is an equivalence. More importantly, after a finite execution ends, line 562 sets \(s(k)=\omega\), but no extension of the formula interpretation or satisfaction relation to that fictitious state is defined; lines 571, 575, 579, and 583 nevertheless still form \(s(k)\models f\). A false guard does not make an otherwise undefined satisfaction term well-typed. **Minimal repair:** define \(D_s\) to be the actual index domain of \(s\), state \(q\xrightarrow{k}s(k)\) iff \(k\in D_s\), and rewrite POT/INEV with \(k\in D_s\) and ALL/SOME with universal quantification over \(D_s\). Equivalently, retain the source glyph but state explicitly that the satisfaction subformula is formed only for defined positions. The first formulation is the mathematically total one.

5. **\`n-c-016.tex:728-755\` — union and intersection of predicate transformers are used before being defined.** The text types \(h:\mathcal P(Q)\to\mathcal P(Q)\), its iterates, \(h^*\), and \(h^x\), but the proposition then contains \(\operatorname{Id}\cap(\operatorname{pre}\cup\widetilde{\operatorname{pre}})\) and \(\operatorname{Id}\cup(\operatorname{pre}\cap\widetilde{\operatorname{pre}})\). Ordinary set union/intersection of functions does not, in general, yield a function of the required type. The word “Pointwise” at line 729 modifies the displayed iteration values and does not define these binary transformer operations. **Minimal repair:** before line 740 state, for \(h,g:\mathcal P(Q)\to\mathcal P(Q)\),

   \[
   (h\cup g)(P):=h(P)\cup g(P),\qquad
   (h\cap g)(P):=h(P)\cap g(P).
   \]

   Then all four identities are well-typed; retain the existing warning that \(h^x\) is not an unexplained greatest-fixed-point binder.

6. **\`n-c-016.tex:973-998\` — the domain of Emerson--Halpern path-formula evaluation accidentally admits the empty sequence.** Lines 973-994 use \(first(x)\) and suffixes \(x^i\), but line 997 says path formulas are evaluated on “all state sequences over \(S\).” In standard sequence notation that class contains the empty sequence, on which \(first(x)\) is undefined. The source-note boundary is all nonempty finite or infinite paths over \(S\), not arbitrary possibly empty strings. **Minimal repair:** replace “all state sequences over \(S\)” at line 997 by “all nonempty finite or infinite state sequences over \(S\) (paths in the preceding sense).” Keep the separate point that only \(A/E\) restrict quantification to members of \(X\).

7. **\`n-c-016.tex:1127-1134\` — the segment-form definition has no positive-arity base case and no excluded nullary case.** The ellipsis

   \[
   [p_1,\ldots,p_n]:=p_1U(p_2U\cdots(p_{n-1}UGp_n)\cdots)
   \]

   is not a definition when \(n=1\), and no domain for \(n\) is stated. **Minimal repair:** give the eliminable recursion

   \[
   [p_n]:=Gp_n,\qquad
   [p_1,\ldots,p_n]:=p_1U[p_2,\ldots,p_n]\quad(n\geq2),
   \]

   and explicitly restrict the construction to \(n\geq1\). No empty segment form is used and none need be named.

8. **\`n-c-016.tex:1809-1819\` — the claimed “actual witness systems” do not uniquely define the inductive pair.** At \(n>0\) the text uses the same fresh names \(s_n,t_n\) for “both systems” and says only that an edge goes “into that copy.” It neither distinguishes \(s'_n,t'_n\) in the primed member nor names the target inside the copied \(TS'_{n-1}\). Different attachment vertices produce different transition systems, so the bounded-formula claim is not attached to a fully specified family. **Minimal repair:** state explicitly, for \(n>0\), that \(TS_n\) adds \(s_n,t_n\) and the four edges

   \[
   s_n\to t_n,\quad t_n\to t_n,\quad
   t_n\to s'_{n-1},\quad t_n\to s_n,
   \]

   while \(TS'_n\) adds \(s'_n,t'_n\) and the three edges

   \[
   s'_n\to t'_n,\quad t'_n\to t'_n,\quad
   t'_n\to s'_{n-1}.
   \]

   State the empty/\(a\) labels for the separately primed and unprimed fresh states. Retain \(n=0\) as the already stated separate base case and retain the reader-left bounded-formula induction.

These eight findings are exhaustive for this review. No other line-specific must-fix was found.

## Bounded positive evidence

- **Fixed-point directions and typing apart from finding 5:** the guarded universal- and existential-until recurrences at lines 133-164 grow from the right operand in the correct direction; the source's dropped guard and the reconstructed existential recurrence are separated at lines 150-179. The Baier--Katoen least/greatest set characterizations at lines 1561-1609, increasing/decreasing iterations at lines 1641-1654, and worklist invariant at lines 1654-1667 have the correct inclusion directions and state-set types. The host method at \`logic-in-computer-science.tex:974-1005\` types \(\mu,\nu\) over \(\mathcal P(S)\), starts least iterations at \(\varnothing\) and greatest iterations at \(S\), and agrees with the presentation's source-level set characterizations.

- **Image-finiteness:** \`n-c-016.tex:740-762\` retains image-finiteness as a hypothesis of both Queille--Sifakis propositions and does not promote the four finite-iterate identities to arbitrary transition systems. It also preserves that the proofs are delegated to Sifakis 1979.

- **CTL/CTL* ownership:** the prerequisite at \`temporal-epistemic-supplement.tex:46-55, 58-104, 129-164\` and the host at \`logic-in-computer-science.tex:948-1005, 1017-1033\` separate state formulas, path formulas, path quantifiers, and predecessor operations. The Clarke--Emerson indexed state syntax at \`n-c-016.tex:58-120\`, the Emerson--Halpern mutually typed grammar at lines 936-1027, and the Baier--Katoen CTL/CTL* grammars at lines 1496-1543 and 1832-1867 preserve those types. Findings 6 and 8 concern domain/construction closure, not a reversal of state/path ownership.

- **Truth and nullary cases already closed elsewhere:** strong until permits the current state and requires a witness (\`n-c-016.tex:78-95, 1529-1534\`); process-indexed universal next is correctly identified as vacuous when that process has no successor (lines 110-119); the action-family empty disjunction/conjunction conventions are explicit at lines 607-628; and the one-process factorization gives the empty other-process conjunction the value true at lines 432-435. Finding 1 is the remaining outer process-arity omission.

- **Empty-state bridge:** \`n-c-016.tex:1446-1481\` correctly types the action-forgetting maps \(R_0,V_0\), treats \(S\ne\varnothing\) as the condition under which the host's nonempty total structure is instantiated, and separately handles \(S=\varnothing\), where \(I=\varnothing\), every satisfaction set is empty, and system satisfaction is vacuous. It also correctly distinguishes the binary-edge count \(\lvert R_0\rvert\) from the action-labelled transition count \(K\).

- **Hamiltonian base and complexity:** the Baier--Katoen construction explicitly assumes \(n\geq1\) at lines 1749-1750, supplies the base \(\Psi(v_{i_1})\) at lines 1768-1777, and gives a total transition system with the sink loop. Theorem 6.30's bound at lines 1731-1745 retains finiteness, absence of terminal states, predecessor linked lists, and direct modality handling. Lines 1795-1805 correctly distinguish a uniform polynomial translation from mere polynomial-size nonuniform advice. Finding 2 is confined to the earlier Clarke--Emerson reduction.

- **Proof/citation/reconstruction boundaries:** the presentation distinguishes printed proof, citation, reader-left induction, and reconstruction throughout: Clarke--Emerson at lines 150-179, 222-304, and 460-472; Queille--Sifakis at lines 555-595, 704-762, and 801-811; Emerson--Halpern at lines 1145-1247 and 1285-1355; and Baier--Katoen at lines 1669-1678, 1807-1830, and 1855-1867. No omitted source proof is promoted to a locally printed source proof.

- **1999 acquisition limit:** \`n-c-016.tex:1386-1407\` attributes no grammar, algorithm, theorem, proof, example, or complexity result to the unacquired Clarke--Grumberg--Peled first-edition body. It keeps contents-page locators as acquisition targets and does not substitute the 1996 survey, 2001 chapter, 2008 textbook, or 2018 second edition. This matches the acquisition note's source-use boundary.

- **Host consistency:** the host's finite, nonempty, total structure; predecessor maps; fixed-point lattice; CTL labelling theorem; LTL/CTL boundary; and four separately cited CTL/CTL* complexity classifications are consistent with the presentation after the explicit action-forgetting bridge. The presentation does not attribute the host's modern linear-time theorem to Clarke--Emerson, Queille--Sifakis, Emerson--Halpern, or the unacquired 1999 body.

- **Technical-name rule:** no additional must-fix arises under the supplied rule. The newly foregrounded names and abbreviations are locally justified and used: synchronization skeleton/global system flowgraph (\`n-c-016.tex:17-36, 427-458\`), interpreted Petri net (lines 486-512), model fragment (lines 382-402), state complete and the closure properties (lines 894-925), MPL stage (lines 1285-1291), the metalinguistic bridge \(R_0,V_0,\mathcal K_0\) (lines 1446-1477), and the Boolean comparison abbreviations (lines 1703-1716). Each location supplies standing and a distinction from neighboring notions; each is used later. Finding 7 requests an eliminable base case for an already used proof-local notation rather than naming another artifact.

## Evidence ledger

Substantive text read directly as text:

- \`handbook/parts/p09/presentations/n-c-016.tex\`: lines 1-1884, complete through EOF. It was then revisited at lines 1-473, 474-812, 813-1385, and 1386-1884 to fix the line-level audit.
- \`handbook/parts/p09/logic-in-computer-science.tex\`: lines 945-1040 and 1495-1520.
- \`handbook/parts/p08/temporal-epistemic-supplement.tex\`: lines 42-190.
- \`spec/research/p09-clarke-emerson-1981-source-note.md\`: lines 119-693 and 842-884.
- \`spec/research/p09-queille-sifakis-1982-source-note.md\`: lines 143-760 and 805-867.
- \`spec/research/p09-emerson-halpern-1986-source-note.md\`: lines 62-729.
- \`spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md\`: lines 424-470.
- \`spec/research/p09-baier-katoen-2008-ch6-source-note.md\`: lines 75-1120.
- \`spec/research/p09-source-presentations-lot2-3.md\`: lines 781-847, used only as the compact source/provenance register; its retrospective review-status sentence was not used in reaching this verdict, and no underlying review was opened.
- \`handbook/bib/handbook.bib\`: lines 2393-2458, 4815-4846, and 4897-4906.
- \`spec/research/p08-new-content.md\`: lines 810-830.

Markdown heading-only navigation scans were also displayed for the five named source/acquisition notes to select the foregoing mathematical ranges; no unlisted body range from those scans was used as evidence.

## Prohibitions and non-claims

- No N-c-016 Round 1, Round 2, or Round 3 review report; source-fidelity report; publication report; admission, board, handoff, or history file; parent conclusion; or agent output was opened. No agent was contacted, inspected, or delegated to.
- No manuscript or source PDF, render, screenshot, page image, or historical publication file was opened or inspected. Statements about source pages, visual audits, and acquisition routes are attributed only at the strength recorded by the permitted textual notes.
- No web access was used.
- No TeX build, test, checker, validator, hash, repository script, executable source tool, or source program was run. The only shell operations were direct \`Get-Content\` text reads and a \`Test-Path\` check for the output filename.
- No manuscript, host, prerequisite, bibliography, source note, register, or other repository file was modified. This report is the only output.
- This is a mathematical/definedness and host-consistency verdict, not a compilation, layout, visual-publication, rights, or fresh acquisition verdict. It does not independently authenticate the source-note claims or close the Clarke--Grumberg--Peled acquisition gap.

REGISTER STATUS: OPEN

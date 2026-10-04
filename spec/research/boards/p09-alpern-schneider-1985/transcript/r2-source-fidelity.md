# Round two source-fidelity and evidence review

## Blindness and evidence boundary

I read the board charter completely and reviewed only its frozen round-two
repaired snapshot. I did not read `ledger.md`, `transcript/chair.md`, any round-one
transcript, any other round-two transcript, or any prior Part IX board record. I
did not contact another seat. I did not run a test, test harness, automated
checker, repository script, TeX command, build, or handbook-PDF inspection.

I visually read, at original image detail, journal printed pp. 181--185 from
`journal-page-1.png` through `journal-page-5.png` and all eleven report file
pages from `tr-page-01.png` through `tr-page-11.png`. The two frozen PDFs were
used as the controlling source identities. I also read every line of every
frozen manuscript/source scope: `n-c-012.tex` 2632--2990,
`logic-in-computer-science.tex` 710--718, `handbook.bib` 6056--6080, the source
note 1--659, and the compact presentation 395--537.

## M01 identity gate

All seven SHA-256 values were recomputed before substantive review and matched
the charter exactly.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `alpern-schneider-1985-defining-liveness.pdf` | `FB69B4E81FD14CAE073F6087CE724E70847FFF16EA560701525952908E48FE31` | match |
| `alpern-schneider-1985-tr-85-650.pdf` | `CF02E04AF863E7325C59C6C4671E389C53DB7B7ADA7804A379B287C569C896AE` | match |
| `handbook/parts/p09/presentations/n-c-012.tex` | `4E58F17BC534504C5D43DE2EADBD365CE01B8D029CE8A67B2BBAFBF2DAD75736` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` | match |
| `handbook/bib/handbook.bib` | `E0AF3849EEB34AB9966EF971881D3D10307ED47A92593FBE0B91917E18A1318E` | match |
| `spec/research/p09-alpern-schneider-1985-source-note.md` | `786B63163F0EF1456561B974D1D4A38578A06AF619C4DAB0ADE05FFCC0D7EE13` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `915ECD5D1451D24E336A60616AF5F93EBE300774A1D29FABABD0531035F4838E` | match |

## Finding

### R2-SF-01 — must-fix — open

- **Author/round:** source-fidelity and evidence seat, round two.
- **Manuscript locations:** `handbook/parts/p09/presentations/n-c-012.tex`
  2769--2788, especially 2772--2775;
  `spec/research/p09-alpern-schneider-1985-source-note.md` 276--305,
  especially 278--286; and
  `spec/research/p09-source-presentations-lot2-3.md` 467--476.
- **Controlling source locations:** journal printed p. 183, leads-to definition
  and the paragraph immediately following it; Cornell report body p. 5 (file
  page 7), the corresponding leads-to definition and following paragraph.
- **Claim:** all three frozen records say that the source claims *without
  qualification* that a leads-to property is live but not absolutely live.
  The printed source does not leave both parts unqualified. It expressly makes
  liveness conditional on satisfiability of \(E_2\), while its assertion that
  a leads-to property is not absolutely live is the unqualified part. The
  journal and revised report have the same distinction.
- **Evidence:** on journal p. 183 the authors first say that any leads-to
  property is not absolute, then, after defining leads-to, say that such
  properties are liveness properties when \(E_2\) is satisfiable. Report body
  p. 5 repeats that order and qualification. The handbook's subsequent
  state-set hypothesis \(E_2\ne\varnothing\) correctly supplies the condition
  for its liveness/uniform-liveness proof, but it does not make the preceding
  source attribution accurate.
- **Violated invariants / coverage:** I6 and I10; M10, M19, and M21.
- **Harm:** a graduate reader is told that the source omitted a hypothesis it
  actually printed and cannot tell which precise printed assertion the
  handbook is correcting. This blurs the required source/handbook boundary at
  the exact example used to demonstrate that boundary.
- **Minimal correction:** in all three locations, state separately that the
  source calls the leads-to property live **when \(E_2\) is satisfiable**, and
  that it claims **without qualification** that any leads-to property is not
  absolutely live. Retain the handbook-owned assumptions
  \(E_1\ne\varnothing\), \(E_2\ne\varnothing\), and
  \(S\setminus(E_1\cup E_2)\ne\varnothing\), the fixed \(e_2^\omega\) suffix,
  the \(e_1\smallfrown c^\omega\) witness, and the two-state counterexample;
  those parts are correct. Add the explicit journal locator p. 183 to the main
  reader paragraph when making this wording correction.

## Four highlighted round-two corrections

1. **Compact safety binder — checked-clean.** Compact lines 423--442 first
   give \(P\subseteq S^\omega\), type \(x,y\in S^\omega\) and
   \(n\in\omega\), and state the complete quantifier order
   \(\forall x\in S^\omega(x\notin P\Rightarrow\exists n\in\omega\,
   \forall y\in S^\omega\, (x\upharpoonright n)\smallfrown y\notin P)\).
   This matches journal p. 182 and report body p. 2, including allowance of
   the empty prefix.
2. **Corollary 2.1 countermodel — checked-clean.** Reader lines 2919--2951,
   source-note lines 492--541, and compact lines 504--525 preserve the printed
   word *intersection*, distinguish the union-closure repair, and show that the
   printed implication is false rather than merely unproved. The family
   \(\mathcal F=\{S^\omega,E_a,E_b,Q,\varnothing\}\), with
   \(Q=\{a^\omega\}\), is closed under every binary intersection, contains the
   disjoint live members \(E_a,E_b\), and has only
   \(S^\omega,E_a,E_b\) as live members. Their pairwise intersections never
   yield \(Q\). Thus the printed hypothesis is actually satisfiable and is
   insufficient. Journal p. 184 and report body p. 8 both visibly print
   *intersection*.
3. **Predictive standing — checked-clean.** Reader lines 2794--2815 and the
   corresponding source-note/compact passages state exactly
   \(A,B\subseteq S\), make \(P_{A,B}\subseteq S^\omega\) an eliminable
   property name, and state nonemptiness of \(A,S\setminus A,B,S\setminus B\).
   The reconstruction faithfully renders journal p. 183/report body p. 5 and
   proves ordinary liveness and failure of uniform liveness at the right
   quantifier strength.
4. **Leads-to repair — finding-linked to R2-SF-01.** The handbook-owned
   hypotheses, fixed-suffix proof, non-absolute witness, and two-state
   counterexample are mathematically correct and visibly identified as a
   repair. The attribution of which source claim is unqualified is not exact.

## Mandatory coverage map

| Point | Status | Evidence / disposition |
|---|---|---|
| M01 | checked-clean | Seven recomputed hashes match; table above. |
| M02 | checked-clean | Journal pp. 181--185 and report file pages 1--11 were visually read at original detail. |
| M03 | checked-clean | Journal p. 181 confirms title, authors, journal, volume/date/pages, receipt/revision dates, and printed Elsevier copyright; report file pp. 1--2 confirm title, authors, TR 85-650, October/30 October 1984, and February/20 February 1985 revision. DOI and Cornell routes agree across source-note lines 10--31, compact lines 397--410, and bibliography lines 6056--6080; no access copy declares an open licence. |
| M04 | checked-clean | Page maps match the visually read objects. The revised report agrees substantively with the journal; its second corollary visibly uses *intersection* just as journal Corollary 2.1 does. |
| M05 | checked-clean | Reader 2634--2670 defines nonempty \(S\), \(S^*\), \(S^\omega\), empty sequence via \(S^0\), concatenation, prefix, property/membership, program satisfaction, and terminal padding before use; source-note 97--157 agrees. |
| M06 | checked-clean | Reader 2672--2684 and compact 423--442 preserve the exact typed safety quantifiers and finite irremediable-prefix reading from journal p. 182/report body p. 2. |
| M07 | checked-clean | Reader 2685--2709 gives exact standing for “live for \(P\),” universalizes it to liveness, records \(P\ne\varnothing\), and keeps the full-\(S^\omega\) boundary. |
| M08 | checked-clean | Reader 2660--2663 and 2702--2720 preserve proof-method motivation, the maximality argument, listed examples, and the finite-stuttering qualification without promoting any to a decision or uniqueness theorem. |
| M09 | checked-clean | Reader 2727--2767 gives exact uniform/absolute definitions, semantic-class standing, nonredundancy, immediate uses, nonemptiness, and the correct inclusion chain. |
| M10 | finding-linked: R2-SF-01 | The fixed-suffix handbook proof and repaired separation are correct, but the source's printed liveness qualification is misreported as unqualified. |
| M11 | checked-clean | Reader 2794--2815 gives \(A,B\subseteq S\), all four material nondegeneracy hypotheses, a valid liveness construction, and a valid no-uniform-suffix argument. |
| M12 | checked-clean | Reader 2817--2825 preserves strong-until and total-correctness decompositions and expressly rejects a safety/liveness dichotomy. |
| M13 | checked-clean | Reader 2827--2846 defines cylinders and proves both directions of safety iff closed and liveness iff dense, consistently using \(S\ne\varnothing\). |
| M14 | checked-clean | Reader 2848--2881 exactly reconstructs \(\overline P\), \(L_P\), the set algebra, the minimal-closed-superset density contradiction, and the existence/nonuniqueness/syntax/algorithm boundaries of journal Theorem 1. |
| M15 | checked-clean | Reader 2883--2890 retains complement, intersection, and topological-closure expressibility as the exact conditional hypotheses of Corollary 1.1. |
| M16 | checked-clean | Reader 2892--2917 discloses the \(L_a,L_b\mapsto E_a,E_b\) alpha-renaming, proves density and disjointness, gives the exact factorization, and shows why \(|S|>1\) is material. |
| M17 | checked-clean | Printed Corollary 2.1, its realized intersection-closed countermodel, and the union/Boolean-closure repairs are correct and separately attributed. |
| M18 | checked-clean | Reader 2953--2971 gives the correct binary Boolean table, arbitrary-intersection/finite-union refinement for safety, union fact for liveness, failures in general, and unique overlap \(S^\omega\). |
| M19 | finding-linked: R2-SF-01 | The snapshot correctly records that Theorems 1--2 have printed proofs, the topological equivalences are only stated, and the handbook supplies the omitted elementary arguments. The leads-to qualification is the remaining source/handbook attribution error. |
| M20 | checked-clean | “Live for \(P\),” uniform liveness, absolute liveness, \(P_{A,B}\), \(L_P\), \(E_a,E_b\), \(Q\), and \(\mathcal F\) each have local necessity or source standing, exact eliminable definitions, nonredundancy, and actual later use. |
| M21 | finding-linked: R2-SF-01 | Reader, source note, and compact record otherwise reconcile with the shared definition and bibliography; all three repeat the same inaccurate description of the source's leads-to qualification. |
| M22 | checked-clean | The records retain unlettered `N-c-012` standing, do not invent `N-c-012.e`, preserve the copyright/no-open-licence boundary, keep topic admission open, and expressly disclaim tests/builds and broader handbook completion. |

VERDICT: REJECT — R2-SF-01

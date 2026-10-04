# Round 2 adversarial publication and terminology review: Rabin 1969

## Outcome

The frozen Round 2 snapshot is not yet fit for admission. The mathematical
repairs for the zero-length pair sequence and the two empty-witness cases on
Rabin's printed p. 34 survive adversarial reconstruction. The snapshot also
preserves the ordinary/dual, finite/infinite, weak/full, source/later-route,
and decidability/complexity boundaries. Two publication-level terminology
defects remain, however: the source term `frontiered` is still not introduced
under the repository's five-part rule in the reader, source note, or compact
record, and the reader calls the external symbol \(f\notin S\) a state.
Both are must-fixes under R14 and R26.

## Evidence, independence, and identity disclosure

I first read only the charter and then independently recomputed all six
Round 2 SHA-256 identities before substantive review. Every result exactly
matched the charter:

| Frozen object | Independently recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | exact match |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `370C563CA4019E1EF266013ADBC910C231D2A07064EE91DC3E7BCCDD32BF3B5E` | exact match |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | exact match |
| `spec/research/p09-rabin-1969-source-note.md` | `D2B3C0293D4012A262726708F082E0B6F7C4A0CE33D623821687F2CB22B97192` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `02C9C6A01DBCC5F876781EE8C13E7235D26C04EB61DD19A811DC8649C6DECF33` | exact match |

I read all four frozen textual objects in full, including the entire
1,428-line reader file, the entire bibliography, the entire detailed Rabin
source note, and the entire compact source-presentation record with its
adjacent authority and status boundaries.

I visually inspected every required source page at original detail. For the
Rabin object this comprised `rendered/page-01.jpg`, the custody-and-use cover,
and `rendered/page-02.jpg` through `page-36.jpg`, printed pp. 1--35. For the
Meyer object this comprised `meyer1975-rendered/page-485.png` through
`page-490.png`, printed pp. 477--482. Formulae, symbols, pagination, wording,
and the findings below were checked against those page images, not against
OCR or layout extraction. The Rabin cover visibly identifies the article,
author, journal, volume, date, and pp. 1--35 and limits the archived copy to
personal, noncommercial use absent permission. Meyer's printed pp. 477--482
visibly contain the complete six-page article, including the lower-bound
display spanning pp. 478--479 and the explicit item for the theory of two
successors and prefix.

My evidence set was limited to the charter, the six Round 2 frozen objects,
and the two specified original-detail render sets. I did not read a Round 1
report, another Round 2 report, a ledger, a chair transcript, another board
transcript, the staging draft, or the layout extraction. I did not contact any
reviewer. I did not inspect a handbook PDF or run a test, automated checker,
repository script, TeX command, interim build, or build. I did not use live
web pages to supplement the frozen evidence.

## Whole-snapshot audit against R01--R29

| Invariant | Result | Adversarial result |
|---|---|---|
| R01 | pass | Reader lines 914--917 retain \(\Lambda\); Rabin printed pp. 1, 2, and 5 visibly use \(\Lambda\), with no silent \(\epsilon\) replacement in the Rabin reconstruction. |
| R02 | pass | Reader lines 941--963 give every \(0<n\leq\omega\), \(T_n=n^*\), all successors, both orders, the finite-\(n\) definability qualification, and the \(T_\omega\) exception exactly as Rabin printed p. 5, with Theorem 1.12 correctly located on p. 11. |
| R03 | pass | Reader lines 965--1014 preserve arbitrary-root valued subtrees, distinguish \(\langle S,M\rangle\) from \(\langle S,M,S_0,F\rangle\), type \(F\subseteq\mathcal P(S)\), and state ordinary acceptance as \(\exists r\,\forall\pi\), matching printed pp. 5--6. |
| R04 | pass | Reader lines 1142--1187 attach \(\Omega\) only to dual acceptance, reverse the prefix to \(\forall r\,\exists\pi\), and expressly retain no-run vacuity, matching printed pp. 24--25. |
| R05 | pass | Reader lines 1016--1022 and 1092--1097 preserve the exact Boolean/projection, complementation, and emptiness dependencies of printed pp. 7--10; lines 1296--1391 reconstruct the actual printed pp. 32--34 emptiness route. |
| R06 | pass | Reader lines 1026--1064 type the full-root bit-track bijection and separately retain the principal-formula reduction, finite-tree lift, Boolean operations, projection, and complementation from printed pp. 7--9 and 30--31. |
| R07 | pass | Reader lines 1066--1076 explicitly mark \(\exists x(x\in A\land r_0(x)\in B)\) as a handbook-worked instance rather than a source-printed transition table; it correctly instantiates the construction on printed pp. 8 and 30--31. |
| R08 | pass | Reader lines 1078--1097 retain the finite state-track run code, Lemma 1.2 normalization, \(\exists\bar B\,\forall C\), and the exact nonemptiness decision of printed pp. 9--10, with no silent basis theorem. |
| R09 | pass | Reader lines 1101--1138 exactly type \(K:U\times S\to U\), product \(U\times S\), initial set \(\{u_0\}\times S\), the common \(K(u,s)\) update, and the projected Muller family from printed p. 18. Recomputing a branch gives first coordinates \(u_0,K(u_0,s_0),K(K(u_0,s_0),s_1),\ldots\), the unique word run; projection of the infinitely recurring product-state set is valid because the product state set is finite. |
| R10 | pass | Reader lines 1142--1187 preserve both clauses of type \(\Omega\), the additional range-avoidance clause for type \(\Omega\)-empty, and the exact complement role of printed pp. 24--26. |
| R11 | pass | Reader lines 1217--1224 retain marked local obligations, simultaneous copies, same-state merging, and the Theorem 3.1 path check; these are visible across printed pp. 19--24 and are not replaced by a slogan. |
| R12 | pass | Reader lines 1226--1232 and 1287--1294 define well-foundedness by absence of infinite descent, put each successor obligation in a lower ordinal stratum, and confine transfinite induction to Lemmas 3.3 and 3.11, as on printed pp. 19 and 23--30. |
| R13 | pass | Reader lines 1234--1255 and 1326--1380 retain the equal-length transformations, the shorter \(\Omega_{k-1}\) step, the two half-steps, and positive-\(k\) induction only after the explicit zero-length normalization. |
| R14 | fail: R2-AP-01, R2-AP-02 | The equations and transition codomain are correct, but the required source vocabulary and standing are not publication-clean: `frontiered` is not introduced at first use, and \(f\notin S\) is called a state. |
| R15 | pass | Reader lines 1258--1285 distinguish the principal-formula lift, compactness lemma, and complementation role; lines 1388--1390 explicitly prevent the finite-tree/weak-theory dependency from changing the infinite input or full \(S2S\) theory. |
| R16 | pass | Reader lines 1296--1324 erase the alphabet, complement the one-tree language, apply Lemma 3.6, and reduce to the specified dual-membership question, matching printed pp. 32--33 without inserting a regular-tree basis theorem. |
| R17 | pass | Reader lines 1326--1342 name the current finite table and pair sequence on every recursive pass and correctly state Definition 3.7's formal-state-set/root boundary from printed p. 33. |
| R18 | pass | Reader lines 1352--1362 exhaust \(H\subseteq U_k\), make \(H=\varnothing\) the direct shorter dual question, use the restricted table only for nonempty \(H\), state finite termination, and identify the empty branch as handbook-owned. Direct substitution into printed display (3.5) on p. 34 confirms the empty branch. |
| R19 | pass | Reader lines 1364--1380 permit \(m=0\), retain \(E_0\), make its universal condition equivalent to the absence of a finite run from \(s_0\), invoke Koenig compactness, retain the printed nonempty branch, and identify the empty completion as handbook-owned. This is the required correction to printed p. 34, not a source attribution. |
| R20 | pass | Reader lines 952--960 and 1383--1387 report but withdraw Rabin's printed elementary-recursive claim. Meyer printed pp. 478--479 state a growing-tower lower bound for each listed theory and list the theory of two successors and prefix with Meyer--Stockmeyer credit. That language is a sublanguage of the displayed binary theory, so the consequence defeats the worst-case bound without affecting decidability or effectiveness. |
| R21 | pass | Reader lines 1395--1412 preserve the exact class-level strengths of the linear-order, unary-function, Cantor-space, Boolean-algebra, and game applications on Rabin printed pp. 11--17. |
| R22 | pass | Reader lines 1113--1138 identify McNaughton as an external word-automaton dependency; lines 1414--1428 state the reconstruction boundary and keep Thomas's later basis route separate from Rabin's printed pp. 32--34 proof. |
| R23 | fail: R2-AP-02 | Numbering, locators, notation, strength, and substantive attribution otherwise check out, but `frontier state` is not Rabin's standing for the symbol that printed p. 30 explicitly places outside the state set. |
| R24 | fail: R2-AP-01 | Identities, hashes, scan URL, Meyer correction, bibliography data, and pending status agree. The detailed note and compact record nevertheless say the terminology repair is integrated while the first-use gate still fails. |
| R25 | pass | Detailed-note lines 71--82 accurately preserve the visible JSTOR cover's personal/noncommercial limit and expressly deny an open-content, republication, or redistribution licence for either research PDF or its renders. |
| R26 | fail: R2-AP-01, R2-AP-02 | The finite-tree terminology fails exact definition/standing/nonredundancy at first use, and \(f\) is assigned the wrong standing despite the adjacent \(f\notin S\). |
| R27 | pass, subject to the terminology repairs | No finite/infinite-tree, weak/full-logic, ordinary/dual, existence/effectivity, source/later-route, or decidability/complexity conflation survives. The two findings concern the separate mandatory terminology gate and the state/marker standing. |
| R28 | pass | Detailed-note lines 18--26 and 607--614 and compact-record line 672 keep `N-c-014.d` pending a fresh unchanged-snapshot round and disclaim terminal, typesetting, user, and wider-book acceptance. |
| R29 | pass | Reader lines 1189--1212 and detailed-note lines 360--378 correctly observe that the printed p. 25 enumeration can be empty. With an empty list the dual implication holds exactly when no rooted run exists; \(((S,S))\) has empty path language and therefore exactly the same dual semantics before the positive-length induction. |

## Independent edge and boundary checks

The following attempted falsifications did not produce additional findings:

1. **Ordinary versus dual vacuity.** If no run begins in the named state,
   ordinary acceptance fails at its existential run quantifier, whereas dual
   acceptance is true because its universal implication has no witness run.
   The reader and both records retain that asymmetry.
2. **Zero-length normalization.** For \(\Omega=\langle\rangle\), no branch
   map has an \(\Omega\)-type. Thus one rooted run falsifies the dual
   condition and absence of a rooted run makes it true. For
   \(\Omega^\dagger=((S,S))\), a branch cannot both meet and avoid \(S\)
   infinitely, so its path language is likewise empty. The replacement is
   semantically exact and has the stated limited use.
3. **Printed p. 34, \(H=\varnothing\).** Substitution into display (3.5)
   removes the below-root hit disjunct and leaves exactly the shorter
   \(\Omega_{k-1}\) dual question at \(s_0\). The reader's branch is therefore
   necessary, exhaustive, and correctly owned by the handbook.
4. **Printed p. 34, \(m=0\).** With \(U_0=\varnothing\), the universal
   finite-run condition on \(E_0\) can hold only when no compatible finite
   run begins at \(s_0\). Finite branching plus Koenig's Infinity Lemma makes
   existence of such an obstruction equivalent to absence of a full infinite
   run. The repair neither converts full \(S2S\) to weak logic nor makes the
   original input finite.
5. **Product indexing.** The product printed on Rabin p. 18 and transcribed at
   reader lines 1120--1134 uses the state at the current tree node as the
   current word letter. Its first coordinate therefore is the ordinary
   deterministic run beginning at \(u_0\), not a displaced acceptance
   sequence. Even a finite initial displacement would not change Muller
   recurrence, but no unreported displacement is needed here.
6. **Complexity boundary.** Rabin's claim is retained only as historical
   language. Meyer's report supplies a lower bound for the relevant
   two-successor-and-prefix sublanguage and does not replace Rabin as the
   source for definitions, numbering, or proof architecture.
7. **Rights and admission.** Public research access is nowhere inflated into
   an open licence, and no frozen text claims admission beyond the pending
   `N-c-014.d` content review.

## Findings

### R2-AP-01 — `frontiered` still fails the first-use terminology gate

- **Severity:** must-fix.
- **Exact frozen manuscript locations:**
  - `spec/research/p09-rabin-1969-source-note.md:290` first uses “finite
    frontiered subtree”; the source condition is not stated and associated
    with that name until the later, still unnamed display at lines 484--490.
    Lines 607--609 then assert that the compact-record term is repaired.
  - `handbook/parts/p09/presentations/n-c-014.tex:1258-1265` prints the
    predecessor and two-successor conditions but never says that the latter
    condition is what Rabin calls `frontiered`; line 1368 later uses “finite
    frontiered trees” as though the association had been made.
  - `spec/research/p09-source-presentations-lot2-3.md:670` uses both
    `frontiered` and `nonfrontier` without an exact local definition or an
    explanation of their distinction from finite predecessor closure; line
    672 claims the earlier terminology correction has been integrated.
- **Controlling printed source pages:** Rabin printed p. 30 defines a finite
  binary tree first by finiteness and predecessor closure, defines its
  terminal-node frontier \(\operatorname{Ft}(E)\), and then separately calls
  it `frontiered` iff every \(x\in E\setminus\operatorname{Ft}(E)\) has both
  \(x0,x1\in E\). Printed p. 31 uses finite frontiered trees in the lift and
  compactness arguments; printed p. 34 uses the finite trees in the base
  decision.
- **Defect:** The source's word names a property of a finite
  predecessor-closed node set; it does not name a new tree object and is not
  redundant with predecessor closure, because a finite predecessor-closed set
  may contain a node with exactly one child. The three frozen prose objects
  either use the word before defining it, silently fold the property into
  “finite tree” without attaching Rabin's name, or use `nonfrontier` without
  identifying \(\operatorname{Ft}(E)\) as the frontier. They therefore fail
  the required same-location necessity, exact definition, standing,
  nonredundancy, and later-use account. The repair-completion statements in
  the detailed and compact records are consequently premature. This violates
  R14, R24, and R26.
- **Minimum sufficient repair:** At the first occurrence in each of the
  reader, detailed note, and compact record, state that
  \(\operatorname{Ft}(E)=\{x\in E:x0,x1\notin E\}\) is the terminal-node
  frontier and that a finite predecessor-closed \(E\) is `frontiered`
  exactly when every \(x\in E\setminus\operatorname{Ft}(E)\) has both binary
  successors in \(E\). State its standing as a property of \(E\), its
  nonredundancy by noting that predecessor closure alone permits one-child
  nodes, and its necessity/use in the finite-tree automaton, lift, and p. 34
  base case. An equally sufficient minimal alternative is to eliminate the
  name everywhere and expand the exact property at each use. Update the
  repair-completion sentences only after the frozen prose actually satisfies
  that gate.

### R2-AP-02 — the external frontier symbol is incorrectly called a state

- **Severity:** must-fix.
- **Exact frozen manuscript location:**
  `handbook/parts/p09/presentations/n-c-014.tex:1266-1275`, specifically the
  juxtaposition of \(f\notin S\) at line 1269 with “frontier state \(f\)” at
  lines 1274--1275.
- **Controlling printed source page:** Rabin printed p. 30 defines the finite
  automaton as \(\langle S,M,s_0,f\rangle\), explicitly requires \(f\notin S\),
  gives transitions in
  \(\mathcal P((S\times S)\cup\{(f,f)\})\), and requires \(r(x)=f\) on
  \(x\in\operatorname{Ft}(E)\).
- **Defect:** In the reader, \(S\) has already been given the standing “state
  set.” Calling \(f\) a state immediately after asserting \(f\notin S\)
  contradicts that standing and is not Rabin's formulation. It also leaves
  “terminal node” unattached to the displayed \(\operatorname{Ft}(E)\). The
  equations let a mathematically experienced reader infer the intended
  object, but the prose fails the publication and first-use requirements of
  R14, R23, and R26.
- **Minimum sufficient repair:** Replace lines 1274--1275 by a sentence such
  as: “It accepts when a run starts in \(s_0\) and assigns the distinguished
  external symbol \(f\notin S\) at every
  \(x\in\operatorname{Ft}(E)\), the terminal-node frontier.” Here “external
  symbol” has exact standing: it is the run value reserved for the frontier,
  not a member of the state set; the distinction is necessary precisely to
  prevent it from being used as an ordinary transition state. No mathematical
  construction beyond this terminology correction is required.

No other blocker or must-fix survived the complete R01--R29 audit of this
unchanged six-object snapshot.

VERDICT: REJECT — R2-AP-01, R2-AP-02

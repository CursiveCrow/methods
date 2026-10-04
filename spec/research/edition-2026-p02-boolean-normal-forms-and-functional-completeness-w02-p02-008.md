# w02-p02-008 research note (P2 section 11.7)

Provenance and decisions for packet w02-p02-008. Reader text carries none of this.

## Sources opened in this session

- Post, The Two-Valued Iterative Systems of Mathematical Logic (Annals of Mathematics
  Studies 5, Princeton 1941), held file
  `source/references/acq-r1-ACQ-2026-10-0402/post-1941-two-valued-iterative-systems.pdf`
  (bib key Post1941, already in handbook.bib). Text extracted with pdftotext; printed page =
  PDF page - 9 (PDF 11 carries printed p. 2; PDF 107 carries p. 98; PDF 112 carries p. 103).
  Locators read and used:
  - Introduction p. 2 (PDF 11): Nicod's single-primitive calculus and Sheffer's work as the
    stimulus for the first problem; footnote 5 (pp. 2-3): functions of no variables
    (constants) are excluded.
  - Section 1, pp. 10-11 (PDF 19-20): iteratively closed systems over a denumerable class of
    variables V (replacement of arguments by variables or functions of the system).
  - Section 10, p. 43 (PDF 52): first-order functions alpha_1, beta_1, gamma_1, delta_1
    (identity, constant 1, constant 0, negation); classification of a function by the function
    obtained by identifying all arguments.
  - Section 15, p. 55 (PDF 64): the alternating condition (replacing an argument by its
    negative leaves the function unchanged or turns it into its negative).
  - Section 25, p. 96 (PDF 105): the set of all closed systems is infinite.
  - Section 25, pp. 98-99 (PDF 107-108): every closed system properly included in C_1 is
    included in one of C_2, C_3, D_3, A_1, L_1; none of the five properly included in another.
  - Section 25, p. 100 (PDF 109): description of the inclusion diagram.
  - Section 26, p. 105 (PDF 114): a generating set yields the complete system iff each of the
    five systems fails to contain it; escaping C_2 needs a gamma- or delta-function, escaping
    C_3 needs a beta- or delta-function.
  - Section 26, p. 106 (PDF 115): D_3 = all self-dual functions, A_1 = all [A:a] functions,
    L_1 = all alternating functions; every delta-function fails [A:a]; with a delta-function an
    independent generating set has at most two other generators.
  - Section 26, p. 107 (PDF 116): with both a beta- and a gamma-function, at most two other
    generators; the fourteen forms I-XIV.
- Active-route capture `handbook/restoration/inherited-01946-02186.tex` (whole file) and
  `inherited-01817-01898.tex` 1-40 (truth values F, T, valuations, coincidence lemma).
- Off-route: `handbook/parts/p02/propositional-syntax-semantics.tex` 470-626 (inactive
  Post treatment: thm:p02-post-criterion cited=Post1941, tab:p02-post-maximal-clones,
  def:p02-sheffer-nor, fig:p02-post-lattice). Not relied on; labels not reused.
- Pending-insertion file of another packet: `handbook/parts/p01/notation-binding-and-comparison-of-formal-w02-p01-024.tex`
  3052-3226 and its annex 147-260 (Post's criterion, NAND/NOR, nullary theorem, under
  label tag p01-w02-p01-024). Not on the route at the time of writing; not referenced from
  reader text (labels might not be routed). Overlap reported in the return file.

## Brute-force check

Scratch script (not committed) evaluated the five membership predicates on the twelve named
operations, the Sheffer classification of the sixteen binary operations, and the closure of
each example basis on binary operations; all agree with the table and theorems.

## Decisions

- Truth values written 0, 1 under F = 0, T = 1 (the source macros \True/\False are fenced to
  restoration scopes).
- Operation set written \mathcal O, \mathcal O_n; the registered rows for <C> and
  T_0, T_1, M, L, S (scope 'P2 prop-syntax-semantics') are reused with the same role.
- Proof route for sufficiency: diagonals of the T_0/T_1 witnesses, constants via the
  self-dual witness, negation via a neighbour pair of the monotone witness, conjunction via a
  minimal nonlinear monomial of an algebraic normal form, then <neg, and> = O. Only existence
  of the algebraic normal form is needed.
- Post comparison: D_3 = S and L_1 = L are read off Post's descriptions (L via the
  alternating lemma); C_2 = T_1 and C_3 = T_0 follow from his p. 105 remark plus maximality;
  A_1 = M follows from his section 25 inclusion result plus maximality of M.

## Continuation

- [x] body file (handbook/parts/p02/boolean-normal-forms-and-functional-completeness-w02-p02-008.tex, 629 lines)
- [x] annex file (handbook/annex/p02/boolean-normal-forms-and-functional-completeness-w02-p02-008.tex, 15 annex items)
- [x] intake bib (no new keys) and symbol intake (13 rows)
- [x] patch request work/waves/w02/patches/w02-p02-008.json (two driver insertions), return file
- [x] unit-compile ok, 0 overfull; find_fused_spaces no hits; check.py no finding on these files

State: all packet components have text; the A-029 components remain blocked on the driver
insertion (lead). Open for the lead: the duplicate P1 treatment in the w02-p01-024 files and
the A-119 figure plan of w02-p02-044 (see return proposed_decisions). Nothing further planned
in this packet unless the lead asks for the P1 de-duplication text or a different placement.

Follow-up pass (2026-10-04): the only remaining gap is routing (A-029-C03 and duty 11.7-mp-1).
Re-checked: both anchors in work/waves/w02/patches/w02-p02-008.json occur exactly once in their
hosts (parts/p02.tex line 22, annex/p02.tex line 16); unit-compile ok, 0 overfull; fused-space
check clean; check.py shows no finding on these files. No content change was needed. Order note
for the lead: the -007, -008 and -010 patches share the same anchor, so applying each as a plain
insert_after in turn reverses them; the intended reader order is -007, -010, -008 (11.1-11.3,
11.4-11.6, 11.7) in both drivers. Confirm routing before any ledger update, because the on-route
evidence check also passes on handbook/restoration/inherited-01946-02186.tex by itself.

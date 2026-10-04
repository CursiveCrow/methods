# w02b-p02-015 research note (P2 sections 15.5, 15.6, 15.7)

Label tag: `p02-w02b-p02-015`.

## Duties addressed

- D-P2-008-GOAL-04 / D-P2-008-C01 (15.5, 15.6): P9 link for the Horn/2-SAT
  material. Written as a proved correspondence, not only a pointer:
  - body `handbook/parts/p02/propositional-resolution-and-satisfiability-procedures-w02b-p02-015.tex`
    lines 23-147: def:p02-w02b-p02-015-horn-program (P_S, nullary relation
    symbols, HB = A_S, negative clauses as goals), thm:p02-w02b-p02-015-horn-lfp
    (T_{P_S} on subsets of A_S; closed iff prefixed point; Fwd(S) =
    union of T^k(empty) = M_{P_S}, stage bound |A_S|; least Herbrand model;
    Horn-SAT as a goal test against M_{P_S}), example
    def:p02-w02b-p02-015-horn-program-example (the 019 example list, iterates
    computed), warning def:p02-w02b-p02-015-two-sat-programs (2-CNF clauses
    with two positive literals are outside def:p09-definite-program).
  - links to sec:p09-logic-programming, def:p09-definite-program,
    thm:p09-definite-fixpoint (handbook/parts/p09/logic-in-computer-science.tex
    1976-2008, read this session).
  - annex proof annex:p02-w02b-p02-015-horn-lfp (annex file lines 12-107).
  - host pointers in the 019 body (editable host): after the Horn-procedure
    paragraph (line ~211-217) and after the 2-SAT theorem paragraph
    (line ~384-389).
- D-P2-005-GOAL-03 / D-P2-005-C01 (15.7): thm:p04-cook-levin
  (handbook/parts/p04/complexity.tex, editable host) now has status
  `proved=annex:p02-w02b-p02-015-cook-levin`, with a route paragraph after the
  theorem. The written proof is the annex item
  annex:p02-w02b-p02-015-cook-levin (annex file lines 276-321), built on
  lemma thm:p02-w02b-p02-015-bridge (body 192-225, annex 109-274):
  (1) writable-input vs read-only-input deterministic machines, hence the same
  reductions and P; (2) NP by nondeterministic machines is contained in NP by
  certificates (choice blocks of beta bits, j mod r coding, Koenig argument for
  the finitely many short inputs); (3) certificate bound q(n)=n gives an NTIME
  machine (counter tape with left-end marker). Membership uses
  thm:p02-w02-p02-018-membership (q(n)=n, k <= m/12 from
  def:p02-w02-p02-018-input); hardness uses thm:p02-w02-p02-018-cook-levin.
  - Machine format reading for P4 is stated as an explicit convention
    (def:p02-w02b-p02-015-machine-reading) because P4 fixes machines only up
    to tape layout; it adopts the format of annex:p02-w02-p02-018-cook-levin.
  - 019 body "Where the hardness half is proved" paragraph rewritten to route
    to the annex proof; n-c-026 (editable host) last Cook paragraph points to
    the annex proof.
  - Correction in complexity.tex: the old sentence called AroraBarak2009
    thm. 2.10 "this exact" formulation, but that theorem is for satisfiable
    CNF formulas (held PDF, Section 2.3.2, p2.7 (45) of the 2007-01-08 web
    draft). The sentence now says so.
  - The general converse of clause 2 (arbitrary polynomial certificate bound)
    is cited, not used: AroraBarak2009 thm. 2.6, seen in the held file
    `source/references/acq-r1-ACQ-2026-10-0012/arora-barak-2009-computational-complexity.pdf`
    (web draft 2007-01-08, pages p2.4 (42) to p2.5 (43)). Version note: the
    held file is the author's web draft; the bibkey is the 2009 printing. The
    locator style follows the existing handbook use of thm. 2.10 from the same
    draft.

## Existing treatment found

- packet "existing" list items read: 019 body/annex, 018 body/annex,
  supplement body/annex, complexity.tex, n-c-026.
- Not listed but relevant and used: handbook/parts/p09/logic-in-computer-science.tex
  1976-2008 (def:p09-definite-program, thm:p09-definite-fixpoint);
  handbook/parts/p02/first-order-depth.tex 29-41
  (def:p02-herbrand-universe-base: nullary relation symbols contribute their
  own atoms).

## Patch requests

- work/waves/w02b/patches/w02b-p02-015.json: supplement
  (read-only) sentence at lines 286-288 still says the complete Cook-Levin
  proof is the P9 reconstruction; replacement routes to the annex proof.

## Placement

- Body: handbook/parts/p02.tex after `parts/p02/propositional-resolution-and-satisfiability-procedures-w02-p02-019`
  (line 32). The packet's insertion proposal (after line 80,
  `restoration/scope-SRC-05568-05923`) would put the section inside the
  first-order restoration run; the 019 position keeps it next to the material
  it extends. Lead decides.
- Annex: handbook/annex/p02.tex after
  `annex/p02/propositional-resolution-and-satisfiability-procedures-w02-p02-019`
  (line 26). Until both are inserted, thm:p04-cook-levin's proved= target and
  the new references in 019, complexity.tex and n-c-026 do not resolve in a
  full build.

## Continuation

- All packet components addressed in this session; unit-compile ok
  (4 small overfull boxes, two from shortened titles fixed).
- Remaining for the lead: driver insertion (above), patch application,
  symbol intake merge (P_S, \hat a, \triangleright).

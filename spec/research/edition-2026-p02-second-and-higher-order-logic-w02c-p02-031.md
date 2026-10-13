# Edition 2026, P2 section 23.4 (packet w02ca-p02-031): research note

Section: 23.4 General and Henkin semantics with the matched proof calculus.
Label tag reserved: p02-w02c-p02-031. No reader text written under it.

## Ownership finding

All five queue units in this packet (ED26-REQ-D-P9-001-01, ED26-REQ-N-a-071-01 to -04)
appear in the packet's `readonly_units` map with owner packet w02c-p02-028
(work/waves/w02ca/packets/w02ca-p02-028.json, section 23.1, same wave and run r2).
tools/waves.py `_assign_lanes` gives each shared unit one writer; the workflow rule
A14 forbids non-owners from writing those components.

The block-1 task text nevertheless listed the r2 block-0 assessment dispute for
ED26-REQ-N-a-071-01 (Church 1940) as gaps to close here. The dispute reached this
packet through the `assessment_dispute` path of tmor-authoring-wave.js
(lines 158 and 163), which marks every dispute `kind: writable` without checking
`readonly_units`. Writing the Church 1940 material here would duplicate the
owner's treatment (A9) while the owner runs in parallel, so nothing was written.
The lead has to choose: route these items to w02ca-p02-028, or move the unit's
ownership to this packet and rerun.

Section 23.4's own missing pieces (MP-0 Henkin 1950, MP-1 Andrews 2002,
MP-2 Shapiro 1991) are all blocked_source (ACQ-2026-10-0187, ACQ-2026-10-0008,
ACQ-2026-10-0503). So no part of this packet's work is both writable and owned
here, and no body or annex file was created (A13: no stubs).

## Items to route to the owner (verbatim from the block-0 dispute)

Held source: source/references/acq-r1-ACQ-2026-10-0080/church-1940-simple-theory-of-types.pdf
(Church1940, 14 PDF pages). I did not open it in this session, so I do not vouch
for these page locators. They come from the assessor.

S01-PRESENTATION (partial):
(a) The p.56 framing: partial incorporation of lambda-conversion is offered for its
    advantages to type theory, whatever one thinks of type theory as a foundation.
(b) The p.56 history: debts to Whitehead-Russell, Hilbert-Ackermann, Hilbert-Bernays
    (nn.3-5); n.1 (via Carnap): Chwistek 1921/1922 and Ramsey 1926 proposed the simple
    theory as a modification of the ramified theory; n.10 points to the Prefatory
    Statement of Principia vol.2.
(c) The sec.1 p.56 example (iota iota (iota iota) abbreviating ((iota iota)(iota iota))),
    which w02-p02-040 body lines 42-45 replaces with an example not in the source.
(d) The p.57 qualification: interpretation does not matter to the abstract
    construction (formal consistency assumed).
(e) The p.61 justification of the distinction between formal and syntactical theorems.

S01-PROOF (partial):
(1) The p.64 claim that 26^iota', 26^iota'', ... follow from Axioms 1-6^alpha and 8.
    The existing derivation (w02-p02-040 annex lines 570-650) also uses Axiom 7 (via
    28^alpha and 27^iota), and the warning at body lines 489-500 leaves the question
    open. Needed: a derivation without Axiom 7, or a proof that the claim fails.
(2) The p.59 claim that the same-type predecessor P_{alpha' alpha'} cannot be
    defined without descriptions, derived from the independence of the axiom of
    infinity. It is reported but not proved (w02-p02-041 body lines 617-632;
    w02b-p02-034 body lines 624-633).
(3) The p.61 consequences of the extra axiom p equiv q implies p = q (exactly two
    propositions; with 10^{alpha beta}, classes become propositional functions).
    They are reported without derivation (w02-p02-040 body lines 316-319).

C01: partial while S01-PRESENTATION and S01-PROOF are partial. S01-BRIDGE was judged covered.

## Block 2 (run r2): guard findings G1 and G10

G1 names spec/research/edition-2026-p02-categorical-syllogistic-and-existential-import-w02-p02-002.md.
This packet did not edit that file and does not edit it now (A8). Its working-tree diff
(git diff -w) is a locator correction in its "Sources opened" list (p. 160 replaced by p. 166)
plus an appended paragraph headed "w02ca (block 1)" about body lines 58, 263 and 298 of the
syllogistic chapter. That is another packet's work on chapter 9, unrelated to section 23.4.
The rest of the diff is line endings. Reverting it would need a write to another agent's file
or a git write, and both are forbidden here. The lead has to attribute it.

G10: the unit compile fails because handbook/parts/p02/second-and-higher-order-logic-w02c-p02-031.tex
does not exist. tools/waves.py `_unit_compile_files` always builds the owned body/annex pair of a
section packet (mode "author"). Only unit_accounting packets may own no file on disk ("G10 not
applicable"). Nothing here can be written without breaking A13/A14/A9:
- All five units are in readonly_units (owner w02c-p02-028). The owner's files
  handbook/parts/p02/second-and-higher-order-logic-w02c-p02-028.tex and its annex now exist
  (written in this wave; not in this packet's "existing" list).
- Section 23.4's own missing pieces MP-0, MP-1 and MP-2 are blocked_source. Re-checked this
  session: held-sources.json and source/references contain no Henkin 1950, Andrews 2002 or
  Shapiro 1991 file; the only Henkin entries are the cylindric-algebra volumes, ACQ-...-0188/0189.
- The general and Henkin semantics with the matched calculus are already on the route:
  sec:p02-sol-matched-calculus and thm:p02-sol-derived-adequacy in the supplement, the
  general-model completeness in w02-p02-040, and the w02b-p02-034 chain. The r2 assessments
  record D-P9-001 as covered. A second treatment would violate A9.
A file holding only the toc comment and a heading would be a stub section (A13), so none was
created. The sibling packets w02ca-p02-029 and -030 did the same.
Change needed (lead; tools are outside this packet's files): either let G10 report "not
applicable" for an author-mode packet whose owned body and annex both do not exist, or drop
this packet's body/annex from owned_files and its insertion proposal.

## Continuation

State at return (block 2, run r2): no handbook files written; nothing in progress.
Resume only if (a) ACQ-2026-10-0187 (Henkin 1950, JSL 15(2) pp. 81-91),
ACQ-2026-10-0008 (Andrews 2002, 2nd ed.) or ACQ-2026-10-0503 (Shapiro 1991) becomes held
and the matching unit is reassigned to this packet, or (b) the lead moves a readonly unit here.

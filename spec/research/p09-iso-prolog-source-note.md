# ISO Prolog general-core source note

Retrieved 2026-08-22. Scope: Part IX depth row `D-P11-006` and the boundary
between the pure SLD/SLDNF theory reconstructed from logic-programming sources
and clause-exact claims about standardized Prolog. Only official ISO metadata,
the public ISO/IEC JTC 1/SC 22/WG 17 document register, and public WG 17 working
material were used. The paid final-standard body was not acquired or read.

## Decision

**Final-clause acquisition verdict: OPEN.**

The public evidence closes the standard's identity, current status, scope,
revision history, and the names of several relevant clause groups. It does not
expose the normative text needed to attribute exact selection, clause-order,
backtracking, cut, arithmetic, error, or unification behavior to the final
standard. A committee draft or later WG 17 working page is not silently treated
as the published 1995 body.

## Published object and current status

The official [ISO record](https://www.iso.org/standard/21413.html) identifies
`ISO/IEC 13211-1:1995`, *Information technology -- Programming languages --
Prolog -- Part 1: General core*, edition 1, published June 1995, 199 pages,
under ISO/IEC JTC 1/SC 22. ISO reports that the edition was reviewed and
confirmed on 24 September 2024, so it remains current.

The public abstract says that the standard specifies the representation of
Prolog text, language syntax and constraints, semantic rules, input and output
representations, and restrictions and limits on a conforming processor. That
is a scope statement, not the missing operational clauses.

Three separately published corrigenda apply to the standard:

| Record | Publication | Extent |
|---|---:|---:|
| [ISO/IEC 13211-1:1995/Cor 1:2007](https://www.iso.org/standard/50405.html) | 2007-11 | 5 pages |
| [ISO/IEC 13211-1:1995/Cor 2:2012](https://www.iso.org/standard/58033.html) | 2012-02 | 28 pages |
| [ISO/IEC 13211-1:1995/Cor 3:2017](https://www.iso.org/standard/73194.html) | 2017-07 | 7 pages |

Consequently, even lawful access to an uncorrected 1995 copy would not by
itself establish the current corrected text.

## Public committee material and its limit

The live [WG 17 document register](https://www.complang.tuwien.ac.at/ulrich/iso-prolog/doclist)
identifies two prepublication bodies:

- N110, the March 1993 Committee Draft, `ISO/IEC CD 13211-1`, viii + 172 pages;
- N128, the March 1994 Draft International Standard, `ISO/IEC DIS 13211-1`,
  vi + 191 pages.

The register also records the intervening national comments, dispositions, and
DIS ballot. These facts prove that the drafts precede a later final text; they
do not prove clause identity with the published standard. The public
[CMU AI Repository record](https://www.cs.cmu.edu/afs/cs/project/ai-repository/ai/lang/prolog/doc/standard/0.html)
offers the 1993 committee draft and an unofficial summary, expressly labelling
both as drafts. Neither is used here as final-standard evidence.

Ulrich Neumerkel's public WG 17 page,
[A Prologue for Prolog](https://www.complang.tuwien.ac.at/ulrich/iso-prolog/prologue),
is explicitly a working draft. Its status table reports that Part 1 includes,
among other surfaces:

- clause 7.8 control constructs, including `!/0`, conjunction, disjunction,
  if-then-else, `call/1`, `catch/3`, and `throw/1`;
- clause 8.2 term unification, separately listing `=/2` and
  `unify_with_occurs_check/2`;
- clauses 8.6--8.7 arithmetic evaluation and comparison;
- clause 8.15 logic and control, including negation as failure and `once/1`.

This safely establishes that those are subjects addressed separately and that
unification with an occurs check has a separately named predicate. The page
does not supply the final normative behavior of every listed construct and
does not establish the exact search-order claims owed by the handbook.

## Safe handbook consequence

Part IX may state, with version qualification, that the confirmed 1995 general
core and its three corrigenda are the governing standard records and that the
public WG 17 material places cut, control constructs, unification, arithmetic,
and negation in separate clause groups. It must keep those constructs
outside the pure SLD completeness theorem unless their behavior is separately
formalized.

Part IX may not yet call any leftmost-selection, textual-clause-order,
depth-first-search, cut, arithmetic, error, or occurs-check sentence an exact
claim about the corrected final ISO text. The pure operational distinctions may
still be reconstructed from Lloyd and other acquired logic-programming sources,
with their attribution kept separate from ISO conformance.

## What would close `D-P11-006` at the standard level

Closure requires lawful access to the relevant clauses of the 1995 published
standard together with all applicable changes in Corrigenda 1--3. The review
must record the exact clause numbers and compare the corrected normative text
against each concrete Prolog statement in the handbook. Until then the ISO
presentation is **identity-and-scope closed, final-clause open**.

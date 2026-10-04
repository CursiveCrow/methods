# P6: constructible-hierarchy foundations

Date: 8 September 2026 UTC. Author: `/root/constructible_foundation_author`.
Block started at 07:22:40 UTC; maximum return time 08:07:40 UTC.
Standing: eight full theorem/proof pairs authored and read back from the
actual LaTeX. These are author claims awaiting the three independent text
reviews, integration, production checks, and separate admission.

## Written artifacts

| File | Extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p06/constructible-hierarchy-foundations.tex` | 220 lines; three definitions and eight results | `64E22FE49017819108160AF5C291E8507A94D4751C2D452EF2DBA8DE6F0E1B95` |
| `handbook/annex/p06/constructible-hierarchy-foundations.tex` | 587 lines; eight complete proofs | `4D13EF83F571C7D61BCBD25B0AAF07EA1A0EA4840D3152ED738FB2D7CFFBA43C` |

Only these two new LaTeX files and this intake were written. The parent
retains ownership of routes, canonical symbols, bibliography, old source
corrections, their provenance, and acceptance records.

## Authority and actual reading

The author read `spec/EDITION-2026-CONTRACT.md`, `handbook/CONVENTIONS.md`,
and `C:/Users/Crow/.agents/skills/research/SKILL.md`. The research instructions
guided the prerequisite map to the actual manuscript. The parent's preceding
retrieval supplied exact paths; the author then read the required LaTeX.
The bounded assignment specified no further subagents.

This is an independently supplied deduction from the manuscript's stated
ZF axioms and fixed definitions. No Jech2003 body was available or read.
The derivation is not represented as Jech's exact presentation, and adds
no bibliography key or external-source completeness claim.

| Actual manuscript input | Extent used and standing | SHA256 |
| --- | --- | --- |
| `handbook/restoration/inherited-00603-00647.tex` | Original transitive-set and ordinal definitions, successor and limit conventions; its cited recursion theorem is not assumed. | `B76C0E5AEE32C23E036F59F780A99690C9788636444A4456B8E6762A3307B795` |
| `handbook/restoration/inherited-03519-03680.tex` | Actual Tarskian clauses and complete formula-coincidence proof; the auxiliary codes are explicitly related to these clauses. | `B1F502609BB084ACFF222A7431E05CAED5273ACD19C367B45CBDCCB63F306897` |
| `handbook/restoration/inherited-10089-10271.tex` | Stated ZF axioms, especially Separation, Replacement, Power Set, Foundation, and the actual least-inductive-set construction of omega. Choice is not used. | `6E8EB080C5FC4C5D359798C48AFFB7692ACE514F702DABF643003AE57FFF4B29` |
| `handbook/restoration/inherited-10272-10352.tex` | Ordered pairs and set functions; the complete no-self-membership argument is repeated locally. Its sketched general membership recursion is not assumed. | `0FC1DB84F232FDC88F0860164281D9F0F1182565B6D510F376DE90E0F016A0F3` |
| `handbook/restoration/inherited-10353-10451.tex` | The complete transfinite-induction proof is used. The ordinal and definable-recursion sketches are replaced as prerequisites by complete local proofs. | `6B0A7785FADE6927950AD97D90EC2B24FC90A335B7673AC0A3B75F6E6C791008` |
| `handbook/restoration/inherited-10452-10520.tex` | Exact V-recursion clauses. Their existence is established locally; neither the sketched global hierarchy theorem nor rank existence is assumed. | `EF5058570C685B60C04893267C8F57B4BFF5E214E344E0BF51DCF30DF347DFF4` |
| `handbook/restoration/inherited-10675-10769.tex` | Exact corrected Def(empty) = {empty}, the nonempty satisfaction definition, L-recursion, original ZF theorem, and remaining cited relativization scheme. | `B745B19A1B07592A4CD59FEC1791B3102E88B3C53E30F276C06CA168EBC1D57A` |

The active drivers `handbook/parts/p06.tex` and
`handbook/annex/p06-route.tex` were read. The historical
`constructibility-forcing.tex` body and annex are not used as proof
prerequisites. The later cited bounded-absoluteness theorem is not used.

## Complete proof map

For each suffix below, the body label has prefix `thm:p06-` and the
annex label has prefix `annex:p06.`. All eight pairs are reciprocal.

| Suffix | Body line | Annex lines | Complete content |
| --- | --- | --- | --- |
| `ordinal-foundation-facts` | 37 | 3-113 | Members of ordinals, both inclusions in the proper-subordinal argument, intersection comparison, strict trichotomy, bounded ordinalhood, successor and set-union ordinals, zero in every nonzero ordinal, limit union and successor indices, and omega as an ordinal with successor nonzero members. |
| `definable-ordinal-recursion` | 72 | 115-204 | A fixed first-order approximation formula; restrictions by Separation; least disagreement on a bounded common domain; successor graph extension; Replacement over the current limit ordinal followed by Union; compatibility; the defining class formula; set restrictions and uniqueness. |
| `set-sized-definability` | 125 | 206-364 | Explicit double-power-set product bounds, finite instruction-code set, set of assignments and updates, all nine truth-set clauses, total auxiliary operation for the proved recursion theorem, a single uniform Sat formula, formula/code equivalence including finite index shifts and variable renaming, finite parameter equivalence, Separation on P(A), and the separate empty branch. |
| `bounded-transitive-absoluteness` | 151 | 366-396 | Atomic and Boolean clauses plus both bounded quantifiers; the common quantifier range follows from transitivity. The ordinal predicate consequence uses ambient ZF only; no internal ZF model hypothesis is added. |
| `def-transitive-growth` | 166 | 398-417 | Def(A) subset P(A), A as a definable member, every member of a transitive A as a parameter-definable subset, A subset Def(A), and transitivity of Def(A), including A empty. |
| `hierarchy-recursion-existence` | 181 | 419-470 | Explicit G_L and G_V operations, unique predecessor, set range at limits, first-order level predicates, existence and uniqueness of both recursions, and the expanded formula defining constructibility. |
| `constructible-level-height` | 194 | 472-569 | Transitivity induction; inclusion induction; complete base/successor/limit height induction; the actual ordinal-defining formula for alpha in the successor; exclusion of larger ordinals; strict successive inclusion; L_alpha subset V_alpha by the newly justified V clauses. |
| `constructible-class-foundation` | 213 | 571-587 | Transitivity of the definable class, every ordinal in its next level, and the proper-class contradiction using Separation on a hypothetical set L and the ordinal union theorem. |

The proof dependency order is ordinal facts, definable recursion, set-sized
definability, bounded absoluteness, Def growth, hierarchy existence, exact
level height, and class conclusion. Bounded absoluteness also uses the
ordinary finite formation of formulas and the fixed satisfaction clauses.
There is no appeal to condensation, reflection, ranks, a well-order of L,
GCH, Choice, or an unproved universe-truth predicate.

## Important scope decisions

The ordinal formula explicitly includes transitivity of its argument,
transitivity of each member, and pairwise membership comparison. Every
quantifier is bounded after expanding Tr. Foundation converts this finite
formula to the original strict-well-order definition in the ambient ZF
proof; the internal level is not assumed to satisfy Foundation or ZF.

The satisfaction construction uses finite instruction codes as an auxiliary
set coding, with all clauses given. It preserves ordinary formula meanings
through an explicit two-way construction. Its assignment set is A^omega,
which is a subset of a power set. Nonemptiness uses one element of a given
nonempty A and a constant function, with no choice principle. The Def
formula is a Separation instance on P(A), not unrestricted comprehension.
The branch at A empty never evaluates satisfaction on an empty structure.

Def growth means A subset Def(A) for transitive A. No general assertion
Def(A) subset Def(B) for transitive A subset B is made or used. Increasing
L-levels follow instead from the level recursion and the proved growth
lemma. The proof of L_alpha subset V_alpha requires only the separately
proved existence and clauses of V, not the old hierarchy or rank sketches.

## Canonical notation intake for the parent

All new first uses are in the new P6.3 section. Existing L, V, ordinal,
power-set, ZF, and restriction notation keeps its meaning.

| Glyph family | Typed role and first introduction |
| --- | --- |
| `Tr(x)`, `Ord_b(x)` | Fixed membership-language formulas; the latter is bounded and equivalent in ZF to ordinalhood. First definition. |
| `vartheta(f,y,p)`, `G`, `App_G(gamma,f)`, `f_gamma`, `F` | A fixed functional formula, its operation abbreviation, the approximation predicate, unique set approximations, and the resulting definable class function. Second definition and recursion theorem. |
| `v_i`, `c`, `mathcal C`, `psi_i`, record tags 0-8, indices `i,j,k,n` | Variables, finite instruction codes and their set, unfolded earlier formulas, constructor tags, and finite positions/lengths. Third definition. Variable indices and prior-position indices are distinguished by each record's fields. |
| `S_A=A^omega`, `s[i mapsto a]`, `Sat(A,c,s)`, `Sat_A` | Set of assignments, assignment update, uniform guarded satisfaction formula, and its set relation for nonempty A. Third definition and satisfaction theorem. |
| `B`, `t`, `T_k`, `r(k)` | Triple-record bounding set, finite truth computation, its truth subsets of S_A, and the finite index shift used to concatenate codes. Satisfaction annex. |
| `G_L`, `G_V`, `Lambda(alpha,z)` | The two hierarchy recursion operations and the formula defining the L-level value. Hierarchy existence annex. |
| `D`, `H`, `tau`, `mu` | Bounded disagreement or difference sets, the Replacement image of earlier approximations, and local ordinal indices in the relevant proof paragraphs. These are locally bound working variables. |
| `O`, `nu` | Hypothetical set of all ordinals and its ordinal union in the proper-class proof. Final annex. |

No shared registry or bibliography file was edited.

## Verification and proposed integration

The existing `tools/check.py` file scanner was run on the two new files,
with no restoration authorization override. Its initial run correctly
flagged inherited-only commands ZF, Pow, and restr. They were replaced by
their ordinary editorial spellings, respectively mathsf{ZF}, mathcal{P},
and mathbin{upharpoonright}. The repeated scan has no findings, eight
status entries, eight annex items, and eight matching reciprocal pairs.
The eleven external references were checked against the actual inputs and
P6 driver hooks. This is a scoped source-structure check, not whole-book
strict validation, a mathematical review, or a publication check.

The entire new body and annex were read back. No tests, manuscript builds,
or manuscript renders were created. The frozen original remains at SHA256
`0509750C13B88A4E18914BD52BDE171C725CBA14221CBFC2227D7693A2B421CC`.

Proposed parent integration: insert the body immediately after
`restoration/scope-SRC-10675-10769` in `handbook/parts/p06.tex`, and insert
the annex before `annex/p06/constructibility-forcing-supplement` in the
active `handbook/annex/p06-route.tex`. Preserve the original theorem's
stable hook label `thm:p06-constructible-class` and its ZF statement.
Replace its obsolete omitted-verification paragraph with a direct link to
`annex:p06.constructible-class-foundation`, supported by
`thm:p06-constructible-level-height`, and record that reader correction
with the parent's existing provenance procedure. The adjacent separately
cited axiom-relativization scheme retains its own outstanding proofs.

The new derivation also supplies actual proof destinations for the earlier
ordinal and definable-recursion sketches. Any replacement of those old
paragraphs is a separate parent-owned correction with its own provenance.
This assignment does not claim completion of the full constructibility,
GCH, condensation, reflection, V=L, or relative-consistency presentations.

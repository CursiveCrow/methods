# Round 2 source-fidelity review: Safra expanded manuscript

## Independence, scope, and direct-reading declaration

I reviewed only the board charter and the five frozen Round 2 objects named in
it. I read the actual frozen
handbook/parts/p09/presentations/n-c-013.tex file directly, including the
complete substantive Safra passage at lines 787--1031, and I read the actual
frozen tmp/pdfs/p09-safra-1988/DBA-author-hosted.ps file directly, page by page
through all twenty declared PostScript pages. The PostScript itself, not a
render or derivative, controlled every source comparison below. I also read
the two Safra bibliography entries in the actual frozen bibliography and the
Safra material in both frozen research records.

I did not inspect a manuscript PDF, PNG, derived source PDF, test, checker,
repository script, TeX command, build, ledger, chair text, Round 1 report,
another Round 2 report, another board, memory, staging material, or web result,
and I did not contact another reviewer.

The exact admission scope reviewed is the Safra expanded-manuscript
reconstruction at manuscript lines 787--1031 together with its two
bibliography entries and two research records. Nothing in this report decides
the unread nine-page proceedings body or any broader handbook or publication
status.

## Independently recomputed frozen identities

I independently recomputed the byte length and SHA-256 digest of each frozen
object before substantive review. All five match the Round 2 charter.

| Frozen object | Bytes recomputed | SHA-256 recomputed | Identity disposition |
|---|---:|---|---|
| tmp/pdfs/p09-safra-1988/DBA-author-hosted.ps | 247,788 | 2D492FD28FBCC9FF85E5AA22A62A435D6CB6549DDC00EB5FE8DC7DD82DF6CCD8 | match |
| handbook/parts/p09/presentations/n-c-013.tex | 59,650 | 4DF89F9A17BC8CE2EF8D1F66C8990BD088BB1AB8BAD1219C926407FB3F9900F8 | match |
| handbook/bib/handbook.bib | 207,798 | C085AB2ACA4DDBFF4FA7BBAAD7C01961007962424829C7537A93CFCA0F9201AC | match |
| spec/research/p09-safra-1988-source-note.md | 17,649 | 40EAAF3B885CD7AB3DFAD3B2536FE3EB9EEC77077C3BB5849204E0EB598B92A5 | match |
| spec/research/p09-source-presentations-lot2-3.md | 238,878 | 4BC69269B9E61BFCE47975F5BA097361F4A844EA3507B321FBFBB8F222DA0D6F | match |

## Mandatory invariant and Round 2 refinement dispositions

### S01 -- identity and version: satisfied

The actual PostScript is 247,788 bytes with the recomputed frozen hash. Its raw
header identifies jcss.dvi, gives creation time 21 March 1995, and declares
twenty ascending pages. Source p. 1 contains the footnote that a preliminary
version appeared as [Saf88]; source p. 19 identifies [Saf88] as the 1988 FOCS
paper, pp. 319--327, and prints the historical singular wording Journal of
Computer and System Science. Manuscript lines 787--802 identify the registered
nine-page paper and the distinct twenty-page author-hosted PostScript, preserve
that singular wording, state the header date, and limit detailed attribution to
the expansion. Bibliography lines 2336--2358 and source-note lines 31--69 agree.
No frozen object calls the expansion the nine-page proceedings file or a
published JCSS article. The Round 2 singular-wording refinement is satisfied
without an unowned normalization.

### S02 -- registered-work boundary: satisfied

Source p. 1's preliminary-version footnote and source p. 19's [Saf88] reference
support the version relationship and the 319--327 proceedings page span, but
not identity of the two bodies. Manuscript lines 787--802 reserve the 1988
entry for registered identity and abstract-level contribution and assign every
detailed construction claim to Safra1995Extended. Source-note lines 13--29 and
71--88 record the DOI and access boundary, while lines 299--305 leave the
proceedings wording, numbering, compression, drawings, qualifications, and
proof open. Compact-record lines 596--604 and ledger line 909 preserve the same
gap. There is no proceedings/expansion conflation.

### S03 -- custody and rights: satisfied

The source evidence is the actual author-hosted PostScript whose title page is
source p. 1 and whose complete body occupies source pp. 1--20. Manuscript lines
793--802 identify that custody and source strength without claiming an open
licence. Source-note lines 274--289 distinguish the controlling PostScript from
metadata and derivatives; lines 291--297 expressly state that no open-content
or republication licence was found and that the handbook uses independent
exposition rather than reproduced prose or drawings. Compact-record line 598
likewise excludes PDF and PNG derivatives as evidence. The reader prose is an
independent reconstruction and does not reproduce either drawn example
edge-by-edge.

### S04 -- automaton, run, infinity set, and Buechi condition: satisfied

Source p. 4 defines the finite-state tuple, the set-valued transition
delta: Q x Sigma -> P(Q), the initial state, run recurrence, infinity set,
Buechi condition, Muller-family membership, and the exact deterministic
condition |delta(q,a)|=1 for every state and letter. Manuscript lines 804--827
give the corresponding typed tuple, recurrence, quantified infinity set,
Buechi condition, and Muller condition before use. Lines 813--816 expressly
distinguish the possibly empty input successor set from Safra's total,
single-valued deterministic target convention. The source's allowance of empty
transition values is also witnessed concretely on source p. 17, where all
unspecified transition values in the Appendix construction are assigned the
empty set. The Round 2 deterministic-total and Muller-definition refinements
are satisfied.

### S05 -- Rabin and Streett pair order: satisfied

Source p. 2 introduces Rabin pairs (L_i,U_i) with L_i recurring/good and U_i
eventually absent/bad; source p. 4 gives the same Rabin formula and the
universal Streett dual. Manuscript lines 827--834 preserve Safra's order and
expressly warn against exchanging it with Thomas's later convention. Lines
927--941 maintain the same orientation in the constructed green/red pairs.

### S06 -- tree state standing: not satisfied (R2-SF-01)

Source p. 9 defines the ordered vocabulary tree T=(N,r,p,S), with node
identities in V, a distinguished root, parenthood, sibling order, strict
ancestry, and the extension of sibling order to non-ancestral nodes. Source p.
10 adds the state-subset label map, proper child-union containment,
non-ancestral disjointness, total white/green/red color map, and the printed
specificity clause. Because source ancestry is strict, the literal clause on
p. 10 would require a state to belong to d and not belong to d; the immediately
following parenthetical instead says that it appears exactly along the
root-to-d path.

Manuscript lines 836--870 keep node identity, labels, and colors distinct;
define first-divergence left-to-right order for non-ancestral nodes; define an
ancestor-first total traversal for allocation; and explicitly identify and own
the source's strict-ancestor correction. Lines 861--867 give the exact
inclusive-path definition and make specific an eliminable metalinguistic
abbreviation, while lines 868--870 state why it is needed and why neither
colors nor labels are node names. The total traversal's additional
ancestor/descendant comparisons are allocation-only.

The first-divergence clause is mathematically the needed relation, but its
source ownership is not exact. Source p. 9 formally defines ancestor strictly
and then defines left-of by requiring an ancestor of one node to be an older
brother of an ancestor of the other. Read literally, that relation does not
compare two siblings: their only strict ancestor is their common parent. The
first-divergence relation at manuscript lines 841--843 therefore corrects a
second consequence of the printed strict-ancestor convention. Manuscript
lines 858--867 expressly own only the specificity correction, and lines
905--907 expressly own only the deterministic allocation choice. They never
identify the first-divergence replacement itself as handbook-owned. This is
the source/repair ownership defect R2-SF-01.

### S07 -- initial representative: satisfied

Source p. 10 specifies a one-node initial tree labelled {q0} with every element
of V white, without selecting which vocabulary element is its root. Manuscript
lines 873--877 choose the least v0 only after fixing an order on V, expressly
call that choice handbook-owned, and explain that it merely makes the
deterministic transition literal. It is not attributed to Safra and does not
change the mathematical state.

### S08 -- six-stage update: satisfied

The formal construction on source pp. 10--11 performs, in order: label
advancement; youngest accepting-subset child creation from temporary V';
leftmost horizontal duplicate retention; empty-label deletion; descendant
collapse with green/white/red coloring of the correct old vocabulary objects;
and renaming of surviving temporary nodes. Manuscript lines 879--903 reproduce
that order and type each operation. In particular, line 889 makes child
creation simultaneous over the post-advancement nodes, lines 892--895 preserve
leftmost-path retention and descendant deletion, lines 896--899 restrict
collapse/coloring to surviving old nodes and old names, and lines 900--902
rename only surviving temporary nodes. This matches the controlling formal
construction rather than substituting another Safra-tree update.

### S09 -- deterministic allocation and name reservoir: not satisfied in repair ownership (R2-SF-01)

Source p. 11 says to rename a surviving temporary node to “some” unused element
of V, then proves that every surviving node has a specific original state and
hence that at most n nodes survive. The source does not make the choice of
unused names a function. Manuscript lines 836--847 first provide the linear
vocabulary order and total traversal, and lines 900--913 then enumerate
temporary survivors in that order and assign the least unused vocabulary
elements. Lines 905--907 expressly identify this as a handbook-owned
representative choice required only for deterministic output. Lines 908--913
correctly record creation-state red, later persistence, ordinary white,
collapse green, the specific-state injection, and sufficiency of the n-element
reservoir. The resulting allocation is one function, but it depends on the
silently corrected first-divergence relation identified in R2-SF-01. The
definedness part of S09 is satisfied; the required explicit ownership of every
corrective ordering input is not.

### S10 -- empty-root completion: satisfied

Source p. 4 permits set-valued transitions, source p. 17 explicitly uses empty
transition values, and source p. 11 says to delete all empty-labelled nodes.
Thus the printed update can delete an empty root although every printed
ordinary target state is a rooted tree. Manuscript lines 916--925 identify this
source omission and add exactly one handbook-owned absorbing rejecting
automaton state. Those lines give its standing, triggering condition, total
self-loop, language effect, and asymptotic effect. Lines 927--941 put it in
every bad set, no good set, and leave exactly n Rabin pairs. The sink is not
called a source tree node or attributed to Safra. This also satisfies the Round
2 requirement to keep Safra's deterministic target total and single-valued
while allowing an empty input successor set.

### S11 -- acceptance pairs: satisfied

Source p. 11 defines one pair for each v in V: L_v consists of states where v
is green, U_v consists of states where v is red, and acceptance means
eventually no red and infinitely many green events for some v. Manuscript lines
927--941 define the collision-free handbook names G_v and B_v, include the sink
in every B_v and in no G_v, give the equivalent infinity-set formula, and
conclude exactly n pairs. The renamed letters change no pair orientation or
source attribution.

### S12 -- soundness: satisfied

Source p. 11 defines the finite input word between positions i and j with the
right endpoint excluded, and source pp. 11--12 prove soundness using successive
green positions, accepting finite run segments between successive labels, a
finitely branching predecessor tree, Koenig's lemma, and concatenation.
Manuscript lines 960--977 define the exact half-open factor alpha[i,j) before
using it and reproduce that predecessor direction and concatenation argument.
No edge or quantifier is reversed, and each segment visits the Buechi set. The
Round 2 endpoint-convention refinement is satisfied.

### S13 -- completeness: satisfied

Source p. 12 tracks an accepting original run in the root; after the root's
last green event it places the next accepting visit into a child; horizontal
deletion can move it only finitely often to older siblings; the run then stays
under a surviving child; and finite depth forces a persistent infinitely green
node. Manuscript lines 979--988 preserve that sequence, including the root
case, older-sibling settling, recursive descent, proper-containment depth
bound, name persistence, and final Rabin witness.

### S14 -- state count and optimality: satisfied

Source p. 9 states Theorem 1; source p. 12 counts ordered trees and then prints
a label encoding as a function Q -> V, thereby omitting original states absent
from every live label; source p. 13 gives the modified-Michel n! lower bound
with the qualification “optimal up to a constant in the exponent” and states
Lemma 2; source pp. 17--18 explicitly label the Appendix A argument for Lemma 2
a sketch and bound the required Muller acceptance family.

Manuscript lines 990--1008 preserve the tree and color factors, explicitly own
the correction of the source's incomplete label encoding, and define the total
typed map f:Q -> N union {star}. Lines 993--997 state that star is outside V,
serves only for absence, and is neither a node nor an automaton component; the
resulting (n+1)^n count still gives 2^(O(n log n)). Lines 999--1001 state
Theorem 1 without undefined class abbreviations and with exactly n pairs.
Lines 1002--1008 preserve the n! qualifier and describe Lemma 2 as a
Muller-family-cardinality lower bound whose Appendix proof is only a sketch.
All Round 2 state-count refinements are satisfied.

### S15 -- applications: satisfied

Source p. 14 states Corollary 4: complementary deterministic Rabin with
2^(O(n log n)) states and n+1 pairs. Source pp. 14--15 state Corollary 6:
complementary nondeterministic Buechi with 2^(O(n log n)) states. Source p. 15
defines deterministic in the limit by the accepting-run condition that only
finitely many nondeterministic choices occur and gives Corollary 7 with O(3^n)
states. Source p. 16 records deterministic exponential bounds for the
Delta-PDL and mu-calculus cases and a deterministic doubly exponential bound
for CTL-star.

Manuscript lines 1010--1025 preserve each source and target class, state the
pair and state bounds, define a nondeterministic choice as a position whose
current state and input letter admit more than one successor, restrict the
condition to accepting runs, distinguish it from full determinism, and keep the
modal-logic statements at the source's upper-bound level. The Round 2
deterministic-in-the-limit refinement is satisfied.

### S16 -- cross-presentation and publication scope: not satisfied in repair ownership/status (R2-SF-01)

Source p. 19 prints the singular historical journal wording, and every
Safra-source-attributed occurrence in manuscript lines 787--802, bibliography
lines 2352--2357, source-note lines 49--62, and compact-record line 598
preserves it explicitly. No unnecessary undefined breakpoint terminology
occurs in the Safra manuscript passage or its two research-record
reconstructions.

The ownership defect is repeated cross-file. Source-note lines 125--130 present
the first-divergence relation as the tree relation and identify only the later
total-traversal extension as handbook-owned; lines 140--148 own only the
specificity correction. Compact-record line 600 likewise presents
first-divergence without saying that it corrects source p. 9, then calls only
the total traversal handbook-owned. Compact-record line 604 consequently
claims that the strict-ancestor ownership and ordering defects have been
repaired although this ownership boundary remains unstated.

The exact numbered-result inventory is supported by the source itself:
Theorem 1 on source p. 9; Lemma 2 on p. 13 with its sketch on pp. 17--18;
Lemma 3 on pp. 13--14; Lemma 5 and Corollary 6 on p. 14; Corollary 4 on p. 14;
and Corollary 7 on p. 15. Source-note lines 64--65 expressly enumerate Theorem
1; Lemmas 2, 3, and 5; and Corollaries 4, 6, and 7. The manuscript does not
misnumber or overstate any selected result.

Manuscript lines 1027--1034 keep Safra's n vocabulary identities and n pairs
separate from Thomas's later 2n-name/2n-pair presentation and deny both
proceedings-facsimile and published-journal standing. Source-note lines
264--272, compact-record lines 596--604, and the consolidated ledger at lines
902--916 agree on source ownership, repair ownership, the open proceedings
reconciliation, conditional review status, and narrow admission boundary. No
render, test, checker, script, TeX command, build, human-review claim, or
final-publication claim is offered as evidence for this admission.

The Round 2 singular-wording, deterministic-total, Muller-definition,
factor-endpoint, total-label-encoding, theorem-language, Muller-family-size,
deterministic-in-the-limit, terminology, and exact-result-enumeration
refinements are satisfied. The specificity definition and allocation function
are exact, but the first-divergence correction on which allocation depends is
not expressly handbook-owned; R2-SF-01 therefore rejects the combined
S06/S09/S16 refinement.

## Findings and required repairs

### R2-SF-01 -- must-fix -- first-divergence silently corrects source p. 9

- Exact source page: p. 9. Safra first defines ancestor with positive parent
  depth, hence strictly, and then defines left-of through older-brother strict
  ancestors. The printed relation fails already for sibling nodes.
- Exact manuscript lines: 841--843 supply the correct first-divergence
  relation; 858--867 discuss and own only the separate specificity correction;
  900--907 use the resulting total traversal for deterministic allocation and
  own the allocation choice, not the first-divergence correction.
- Cross-record locations: source-note lines 125--130 and 140--148;
  compact-record lines 600 and 604.
- Required repair: at the first-divergence definition, state that source p. 9's
  formally strict-ancestor wording does not order siblings, define the
  first-divergence relation as the handbook-owned inclusive-path correction,
  and propagate that same ownership statement to the detailed note and compact
  record. Retain the separately owned ancestor-first total traversal and least
  unused-name rule. Remove or update the compact record's stale assertion that
  strict-ancestor ownership and ordering are already fully repaired. Because
  this changes frozen content, recompute identities and conduct a new blind
  round.

## Seat-specific rationale

The source-attributed tuple, pair convention, ordered-tree data, six-stage
transition, colors, acceptance pairs, correctness architecture, state count,
lower-bound qualifier, numbered results, applications, and proof-status labels
all agree with the actual controlling PostScript at the cited pages. The root
representative, specificity correction, deterministic least-name rule,
empty-root sink, and total absence-aware label encoding are bounded and
expressly handbook-owned. The first-divergence relation is also the right
mathematics, but the source's formally defective clause is silently replaced
rather than recorded and owned. Source fidelity therefore fails even though
the resulting construction is otherwise accurately reconstructed.

VERDICT: REJECT -- R2-SF-01

# Round 3 source-fidelity review

## Independence and evidence statement

I performed this review as a fresh blind source-fidelity seat. I read only the
board charter and the five frozen Round 3 objects. I read the actual frozen
LaTeX directly, including the complete Safra semantic subsubsection at lines
787--1038. I also read the actual hash-pinned PostScript directly: its header,
all twenty raw `%%Page` bodies, trailer, title-page footnote, formal
construction, proofs, applications, Appendix A sketch, and reference list. A
direct text extraction was used only to navigate the same PostScript bytes and
was not treated as another source or as independent evidence.

I did not inspect a manuscript PDF, PNG, derived source PDF, test, checker,
repository script, TeX command, build, ledger, chair text, prior report,
another Round 3 report, another board, memory, staging material, or web result.

## Independently recomputed frozen identities

| Frozen object | Bytes | Independently recomputed SHA-256 | Disposition |
|---|---:|---|---|
| `tmp/pdfs/p09-safra-1988/DBA-author-hosted.ps` | 247,788 | `2D492FD28FBCC9FF85E5AA22A62A435D6CB6549DDC00EB5FE8DC7DD82DF6CCD8` | exact Round 3 match |
| `handbook/parts/p09/presentations/n-c-013.tex` | 60,088 | `D8376280880E262F0D0FCE00C6FFBA229284428DB7BBDC7D43C707192C930E75` | exact Round 3 match |
| `handbook/bib/handbook.bib` | 207,798 | `C085AB2ACA4DDBFF4FA7BBAAD7C01961007962424829C7537A93CFCA0F9201AC` | exact Round 3 match |
| `spec/research/p09-safra-1988-source-note.md` | 17,866 | `BB9DB11D86A33F8A18BE1D8E5F175C76A2A7A015C36829F9F97EB652B8635F63` | exact Round 3 match |
| `spec/research/p09-source-presentations-lot2-3.md` | 239,351 | `75F59E5731805548ED37BD1CFC2DB555E1C8AB4C4D5D1BCF096343775DBC795D` | exact Round 3 match |

The PostScript itself declares twenty pages, and I independently found twenty
ascending `%%Page` records. Its raw header gives `%%Title: jcss.dvi` and
`%%CreationDate: Tue Mar 21 15:47:45 1995`.

## Mandatory invariant dispositions

### S01 -- PASS: identity and version

The 247,788-byte identity is exact. The header supplies `jcss.dvi`, the 21
March 1995 generation date, and twenty declared pages. Physical source page 1
contains the preliminary-version footnote, and source page 19 identifies
`[Saf88]` as the 1988 FOCS paper, pp. 319--327, followed by the historical
extended-version statement. Manuscript lines 787--802, bibliography lines
2336--2358, detailed-note lines 31--69, and compact-record lines 596--604 keep
the author-hosted expansion distinct from both the nine-page proceedings body
and any published journal article.

### S02 -- PASS: registered-work boundary

Manuscript lines 788--802 confine the proceedings entry to identity and
abstract-level contribution, state that the nine-page body remains unread,
and assign the detailed reconstruction only to the expansion. The proceedings
pages in the bibliography are 319--327, agreeing with source page 19. The
source's own abstract on page 1 supports the single-exponential construction,
optimality, complementation, and decision-procedure summary, while the
manuscript does not transfer the expansion's theorem numbering or proof detail
to the proceedings object. Detailed-note lines 13--29 and 71--88 and compact-
record lines 596--604 preserve the same open reconciliation boundary.

### S03 -- PASS: custody and rights

Within the frozen evidence boundary, detailed-note lines 293--307 distinguish
lawful research access from an open-content or republication licence and limit
the handbook to independent exposition, notation, bounded locators, and
attribution. Manuscript lines 800--802 and 1037--1038 make source and version
ownership explicit. The prose is reconstructive rather than a reproduction of
the source's text or drawings; the source's worked drawings on pages 5--9 are
summarized only at the level of their prose effect in manuscript lines
948--963. No render or derived file is invoked as evidence in any frozen
object.

### S04 -- PASS: automaton, run, and infinity set

Manuscript lines 804--827 correctly type the source object as
`(Sigma,Q,q_0,delta,C)` with finite `Q`, `q_0` in `Q`, and set-valued
`delta:Q x Sigma -> P(Q)`; define runs from `q_0` with the pointwise successor
recurrence; define the infinity set before acceptance; and give the correct
Buechi and Muller clauses. These agree with source page 4. Lines 813--816 also
preserve the input's possible empty successor set while stating Safra's target
determinism exactly as cardinality one for every state-letter pair, hence total
and single-valued.

### S05 -- PASS: Rabin and Streett pair order

Manuscript lines 827--834 reproduce Safra's `(L_i,U_i)` order: some `L_i`
state recurs infinitely often and all `U_i` states occur only finitely often.
This agrees with the source's prose on page 2 and table on page 4. The text
expressly keeps this recurring/good then absent/bad order separate from the
later Thomas notation. The detailed note also records the universal Streett
dual without reversing the pair components.

### S06 -- PASS: tree-state standing

Manuscript lines 836--875 correctly reconstruct source pages 9--10. The
`n`-element vocabulary supplies node identities; `T=(N,r,p,S)` has the stated
node set, root, parent map, and sibling order; and a source-printed state is
exactly `(T,ell,c)` with `ell:N -> P(Q)` and total three-color map on the
vocabulary. Proper child-union containment and disjointness of labels on
non-ancestral branches are exact.

The source defines ancestor strictly on page 9. Its printed left-to-right
clause consequently fails for siblings, and its printed specificity clause on
page 10 consequently demands both membership and nonmembership at the node
itself. Manuscript lines 841--871 identify both defects, give the exact first-
divergence and inclusive-path repairs, and expressly assign them to the
handbook. Specificity is defined as an eliminable label relation, its standing
is stated, its difference from node identity, labels, and colors is explicit,
and its later use in the `n`-node bound is supplied.

### S07 -- PASS: initial representative

Source page 10 gives a one-node tree labelled `{q_0}` and colors every
vocabulary element white, without selecting the root's vocabulary identity.
Manuscript lines 877--881 state exactly that source content, fix the least
vocabulary element only as a handbook-owned representative, and explain that
the choice makes the target transition literal without adding mathematical
structure.

### S08 -- PASS: six-stage update

Manuscript lines 883--907 follow source pages 10--11 in order: advance every
label; create, for each post-advance old node meeting `F`, one youngest
temporary child labelled by the accepting intersection; retain horizontal
duplicates only on the leftmost path; delete empty-labelled nodes and thereby
their descendants; collapse covered old nodes and assign green, white, and red
according to the printed color map; then rename surviving temporary nodes.
The text makes child creation simultaneous, applies the already disclosed
first-divergence correction to horizontal order, and distinguishes temporary
identities, persistent vocabulary identities, labels, and colors.

### S09 -- PASS: deterministic allocation and reservoir

The source on page 11 says only to use some unused vocabulary name. Manuscript
lines 837--851 and 904--917 separately identify the handbook-owned linear
vocabulary order, ancestor-first total traversal, traversal enumeration, and
least-unused assignment. Together they yield one transition function without
changing source tree standing. Lines 913--917 correctly derive creation-state
red, later name persistence, white ordinary survival, and green collapse from
the source's page-11 color map. The specific-state argument gives at least one
original state per surviving node, at most `n` live nodes, and therefore a
sufficient `n`-name reservoir.

### S10 -- PASS: empty-root completion

Source page 4 permits an empty input successor set; source pages 10--11 then
advance labels and delete every empty-labelled node without defining an empty
root case. Manuscript lines 920--929 identify precisely this printed omission,
introduce the handbook-owned `bot_dead` only after its necessity arises, and
give its exact standing as a target automaton state rather than a tree node. It
loops on every letter, represents prefixes with no extending original run,
rejects all continuations, leaves the language unchanged, and changes neither
the asymptotic state bound nor the pair count. Lines 931--946 define its exact
pair membership.

### S11 -- PASS: acceptance pairs

Manuscript lines 931--946 first display `G_v` and `B_v`, then place the added
state in every bad set and no good set. For every vocabulary identity, green is
the recurring component and red is the eventually absent component, matching
source page 11's `L_v` and `U_v`. The equivalent eventual-red/infinite-green
and infinity-set formulations are correctly oriented, the added rejecting
state cannot satisfy any pair, and the conclusion is exactly `n` Rabin pairs.

### S12 -- PASS: soundness

Manuscript lines 965--982 match source pages 11--12. The half-open factor
`alpha[i,j)` is defined before use with the final letter at index `j-1`. For
successive green positions, every next label state has a predecessor in the
previous label connected by an input-compatible finite run that visits `F`.
The predecessor edges point from the earlier level to the later level; the
levels are finite and nonempty; Koenig's lemma supplies an infinite branch;
and concatenating its compatible factors yields one run that visits `F`
between successive green events. No edge or quantifier is reversed.

### S13 -- PASS: completeness

Manuscript lines 984--993 faithfully follow source page 12. An accepting
original run remains represented at the root. If the root is green infinitely
often, its persistent name witnesses the Rabin pair. Otherwise, after its last
green event, a later accepting visit enters a child; horizontal responsibility
can shift only finitely often toward older siblings; and the argument either
finds infinite green at that stable node or descends. Proper containment bounds
depth by `n`, so descent terminates at a persistent name that is eventually
never red and infinitely often green.

### S14 -- PASS: state count and optimality

Manuscript lines 995--1012 accurately separate source statements from repairs.
Source page 12 bounds ordered vocabulary-tree shapes by
`2^(n log n + O(n))`, adds a printed function-to-vocabulary label count and
`3^n` colors, and concludes `2^(O(n log n))`. That printed function is
undefined for an original state absent from every live label. Lines 997--1003
expressly own the total repair `f:Q -> N union {star}`, state that `star` is
neither a node nor an automaton component, and retain the valid
`(n+1)^n = 2^(O(n log n))` bound.

Theorem 1 is restated at lines 1004--1006 without the source's class
abbreviations and with the correct target class, state bound, and exactly `n`
pairs, agreeing with source page 9. Source page 13 gives the modified-Michel
`n!` lower bound and the exact qualification “up to a constant in the
exponent.” Lemma 2 on page 13 concerns doubly exponential deterministic-Muller
acceptance-family cardinality, and Appendix A on pages 17--18 labels its proof
only a sketch; lines 1007--1012 preserve both facts.

### S15 -- PASS: applications

Manuscript lines 1014--1029 agree with source pages 13--16. Corollary 4 targets
a complementary deterministic Rabin automaton with
`2^(O(n log n))` states and `n+1` pairs. Corollary 6 targets a complementary
nondeterministic Buechi automaton with the same asymptotic state bound.
Immediately before Corollary 7, source page 15 defines deterministic in the
limit by finitely many nondeterministic choices on every accepting run;
manuscript lines 1018--1025 give that accepting-run condition exactly,
distinguish it from full determinism, and state the equivalent Buechi target
with `O(3^n)` states. Lines 1025--1029 preserve the source's exponential and
doubly exponential modal-logic consequences as upper bounds rather than
inflating them into stronger results.

### S16 -- PASS: cross-presentation and publication scope

The complete semantic unit runs from the Safra heading at line 787 through the
final non-facsimile/nonpublication sentence at line 1038; the Thomas heading is
at line 1040. Lines 1031--1038 keep Safra's `n` persistent vocabulary
identities and `n` pairs separate from Thomas's later `2n` names and `2n`
pairs. The bibliography, detailed note, compact record, and manuscript agree
on source ownership, every handbook-owned repair, terminology standing, the
still-open proceedings-body reconciliation, conditional review status, and
the narrow expanded-manuscript admission unit. None uses a render, test,
checker, script, TeX command, build, or publication claim as evidence.

## Round 2 refinement dispositions

- **PASS -- singular historical journal wording.** Source page 19 prints
  *Journal of Computer and System Science*. Manuscript lines 796--799,
  bibliography lines 2352--2357, detailed-note lines 49--60, and compact-record
  line 598 preserve the singular wording and do not normalize it silently.
- **PASS -- total deterministic target, possible empty input successor, and
  Muller standing.** Manuscript lines 810--827 state all three in definition-
  before-use order, matching source page 4. Muller acceptance is infinity-set
  membership in a family of state subsets before any family-size claim at
  lines 1009--1012.
- **PASS -- both strict-ancestor repairs and deterministic traversal.** Source
  pages 9--10 contain the two printed inconsistencies. Manuscript lines
  841--872 give exact first-divergence and inclusive-path corrections, then
  separately add the ancestor-first total traversal. Detailed-note lines
  117--150 and compact-record line 600 state and own the same repairs.
- **PASS -- exact finite-factor endpoint.** Manuscript lines 965--976 define
  `alpha[i,j)` as indices `i` through `j-1` before the source-page-11/12
  soundness argument uses it.
- **PASS -- total label encoding, theorem vocabulary, and Lemma 2 boundary.**
  Manuscript lines 995--1012 give a typed outside value with explicit standing,
  the correct asymptotic count, Theorem 1 without undefined class
  abbreviations, and Lemma 2 as an acceptance-family cardinality statement
  with only the Appendix A sketch.
- **PASS -- deterministic in the limit.** Manuscript lines 1018--1025 define
  it by the choices of accepting runs and distinguish it from full
  determinism, matching source page 15.
- **PASS -- terminology and exact numbered-result inventory.** No undefined
  breakpoint terminology occurs in lines 787--1038. Detailed-note lines 64--66
  record the exact source inventory: Theorem 1; Lemmas 2, 3, and 5; and
  Corollaries 4, 6, and 7. Those numbers and kinds match source pages 9 and
  13--15 and Appendix A on pages 17--18. Every numbered result actually invoked
  in the manuscript has the same source number and standing.

## Round 3 refinement dispositions

- **PASS -- two exact, owned source corrections in all reconstruction
  records.** The first-divergence correction and inclusive-path specificity
  correction are explicit and handbook-owned in manuscript lines 841--871,
  detailed-note lines 125--150, and compact-record line 600. Neither is
  attributed back to Safra.
- **PASS -- allocation choices remain separately owned.** The ancestor-first
  total traversal and least-unused-name allocation are separate clauses in
  manuscript lines 847--851 and 904--911, detailed-note lines 130--132 and
  174--178, and compact-record line 600. Their only claimed effect is to choose
  one deterministic representative transition.
- **PASS -- tree tuple precedes the added state without premature
  classification.** Manuscript lines 852--859 classify exactly the tree states
  printed by the source. The possible empty-root failure is not introduced
  until lines 920--923, after which lines 924--929 supply the added state's
  necessity and standing.
- **PASS -- pair membership follows the displayed definitions.** Lines
  920--929 call the added state rejecting and defer its exact acceptance
  treatment. The displayed `G_v` and `B_v` definitions occur at lines 931--937;
  only then do lines 938--943 classify its good/bad membership.
- **PASS -- complete semantic endpoint.** The review includes lines 1031--1038,
  so Theorem 1, Lemma 2, Corollaries 4, 6, and 7, the Safra/Thomas separation,
  and the non-facsimile/nonpublication boundary are all inside the controlling
  unit. No historical line-1000 or line-1031 truncation was used.

## Seat-specific rationale and findings

I found no source-attribution mismatch, unread relied-on PostScript passage,
silent correction, proceedings/expansion conflation, attribution inflation,
incorrect page locator, rights inflation, or cross-record contradiction. The
frozen manuscript states the source's printed defects as defects, supplies the
necessary bounded repairs with explicit handbook ownership, and preserves the
source's exact result classes, bounds, pair order, proof/sketch status, and
version boundary. There are no blocker, must-fix, should-fix, consider,
discard, or unresolved-user findings from this seat.

VERDICT: ACCEPT

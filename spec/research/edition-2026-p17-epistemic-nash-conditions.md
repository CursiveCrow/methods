# P17 / D4: Aumann–Brandenburger epistemic Nash conditions

## Source identity, acquisition and complete reading

Selected source: **Robert Aumann and Adam Brandenburger, Epistemic Conditions
for Nash Equilibrium**, *Econometrica* **63(5)**, September **1995**,
**1161–1180**, DOI **10.2307/2171725**.

The complete freely downloadable primary was acquired from
[the institutional PDF](https://ratio.huji.ac.il/files/dp57.pdf), linked by
[the Federmann Center publication record](https://ratio.huji.ac.il/publications/epistemic-conditions-nash-equilibrium).
The publication identity was checked against the actual first article page
and the complete final page, not inferred from the landing-page metadata.
The author's own publication list also identifies the Econometrica 1995
article and links the corresponding JSTOR identifier; the Hebrew University
[publication record](https://cris.huji.ac.il/en/publications/epistemic-conditions-for-nash-equilibrium/)
independently identifies volume, issue, pages and DOI.

- Local capture:
  source/references/aumann-brandenburger-epistemic-nash-1995/aumann-brandenburger-1995.pdf.
- **2,109,188 bytes**, **21 physical pages**.
- SHA256:
  **C2C41A4F3BFC2F6E91DEBE82A3D3F9E656A59F019C9FABED51CB6E9EA06652DD**.
- Physical page 1 is a JSTOR cover; physical pages 2–21 are the original
  printed pages 1161–1180. Printed page = physical page + 1159.
- The cover identifies the original journal article and a 2003 JSTOR
  digitization/download timestamp. This is not a 2003 article.
- Printed 1179 records receipt in September 1991 and final revision in
  October 1994. Those are manuscript-history dates, not publication years.
- The institutional landing page contains a corrupted author string and a
  1994 discussion-paper field. The PDF itself is the final published
  Econometrica facsimile, not an inferred 1994 draft.
- Later book reprints, including the 2014 and 2016 records encountered in
  discovery, are distinct versions and were not substituted for this original.

The PDF is image-only: pypdf reports 21 pages but supplies no body text.
All **21 original pages** were visually read in complete source-page renders,
including every display, Figures 1–7, sections 1–7, notes 1–32 and references.
The disjoint temporary directory is
tmp/pdfs/p17-aumann-brandenburger-source, with source-01.png through
source-21.png, rendered at 120 dpi. The original is readable throughout.
The corpus was frozen to this complete original after the full read.

The research and PDF skills were read and used for primary acquisition,
original-source reading and this one durable note. The parent prohibited
further delegation because runtime capacity was unavailable, so all reading
and authoring occurred in the assigned slot. No historical capture was edited.

## Output and full source map

Owned manuscript:

- handbook/parts/p17/epistemic-nash-conditions.tex.
- handbook/annex/p17/epistemic-nash-conditions.tex.

Routing scope is **P17.19**, immediately after the actual P17.18
epistemic-game-theory driver entry. The bounded integration extension
routes both body and annex; root owns the canonical-record merge.

| Source extent | Complete reader treatment and proof destination |
| --- | --- |
| Section 1, 1161–1164 | Sparse sufficient conditions; preliminary pure-action observation; mixtures as conjectures; two versus many players; local hypotheses and sufficiency rather than necessity. |
| Section 2, 1164–1166 | Finite action sets, own types fixing actions/payoffs/theories, product state space, actual game versus realized payoff, full and marginal conjectures, rationality, probability-one knowledge, common prior, proportional averaging and Lemma 2.6. |
| Section 3, 1166–1167, Figures 1–2 | Every payoff and conditional law in the six-positive-state coordination model; actual rationality and known actions without mutual rationality or common action knowledge. |
| Section 4, 1167–1170 | Preliminary observation; Lemmas 4.1–4.6; Theorems A/B; conditional action law on the common-conjecture event; agreement, product factorization and Nash support proof. |
| Section 5, 1170–1173, Figures 3–7 | All three original examples, each prior/theory, every relevant expected payoff, matching-pennies equilibrium uniqueness, full versus marginal conjectures, common versus finite-depth knowledge, lack of common prior. Both arbitrary finite-depth claims receive explicit finite constructions. |
| Section 6, 1173–1174 | Arbitrary measurable type spaces, product sigma-fields, measurable action/payoff/theory maps, countable event operations. Every general theorem proof uses this domain; no finite-type substitute or unproved disintegration existence. |
| Section 7a–d, 1174–1176 | Descriptive language and actions in states; Harsanyi comparison; probability-one belief versus certainty; own theory/payoff/action knowledge; expected-payoff interpretation boundary; conscious randomization distinction; full car-purchase conjecture story and its limited standing. |
| Section 7e, 1176 | Knowledge of the fixed equilibrium profile; first-order implication, no automatic higher-order implication, and failure of even first-order knowledge under the preliminary observation alone; explicit finite witnesses. |
| Section 7f–g, 1176–1177 | Common language versus common knowledge of an externally given game; revised earlier informal claims; complete Remark 7.1 with assumed agreement and coordinate-versus-rest independence. |
| Section 7h–i, 1177–1179 and note 31 | Exact existential realization of every equilibrium; corrected pointwise converses; two/many-player and preliminary forms; source comparisons with Tan–Werlang, Brandenburger–Dekel and global correlated-equilibrium analysis. |
| Notes 1–32 and references, through 1180 | Relevant qualifications retained, especially no mutual absolute-continuity assumption (note 17), product sigma-field (25), and the distinct earlier independence conditions (32). Cited universal-hierarchy sources are not claimed acquired or proved by association. |

## Exact mathematical domain and correction

The action sets are finite and nonempty. Type spaces are arbitrary nonempty
measurable spaces, with the full event-wise measurable kernels explicitly
supplied. Finite type spaces are used for the worked examples, not to narrow
the original theorems. The own-coordinate insertion construction makes an
extended probability measure at every type. Payoff arrays are finite real
arrays at each type; there is no unstated requirement to integrate those
arrays over the common prior.

(CP) formalizes the source's conditional-distribution definition as an
integral identity for all measurable own-type events. It asserts no general
existence theorem for disintegrations on arbitrary measurable spaces.
The kernels remain specified at null types, where division by a prior atom
is unavailable. Source equation 2.5 is proved as a consequence.

The exact source Theorem B requires positive common-prior probability of
the intersection of mutual game knowledge, mutual rationality, and common
full-conjecture knowledge. A merely nonempty event does not suffice.
Agreement/factorization alone use only the common prior and positivity of
the common-conjecture event. Nash additionally uses the game/rationality
conditions. Actual positive equilibrium support is obtained almost surely
on that event, not at every arbitrarily selected null state.

The source Lemma 4.5 projection step is made rigorous on the general domain.
If H is contained in K_i H, its nonempty-section types are exactly the
measurable level set where p_i(H;type)=1. The proof can therefore average
the kernel identity directly without an unjustified general measurable-
projection assertion. This is a completed dependency, not an open gap.

### Direct correction of the note-31 converse

Printed 1178 note 31 asserts, in the two-player case, that mutually known
payoff functions and conjectures make mutual rationality equivalent to the
conjectures constituting Nash. Its reverse implication omits the actual
actions' relation to those conjectures.

Complete countermodel: each player has actions/types 0 and 1; its payoff
equals its own action; type r chooses r; every type believes the opponent
has type 1. At actual state (0,0), the game and conjectures are commonly
known and the conjectures are the unique equilibrium (delta_1,delta_1),
but both players are irrational. The product state space permits (0,0).
A common prior concentrated on (1,1) also satisfies (CP); the unused type
kernels are specified versions at null types. A common prior is not needed
for the source's claimed two-player converse in any case.

The body corrects the statement directly. Under mutually known game and
specified product conjectures, mutual rationality is equivalent to:
the conjecture profile is Nash **and every actual action is a best response
to its opponent conjecture**. Positive equilibrium support of each actual
action is sufficient but stronger than necessary. The full proof works
for all finite player sets of size at least two. The common-prior
factorization supplies the product premise in the many-player setting.
For the preliminary observation, mutually known actions and game give
the simpler equivalence between actual rationality of all players and
that pure profile being Nash. Mutual rationality does not follow:
the original six-state illustration already separates it. Knowledge of
actions must not be silently strengthened to knowledge of conjectures.
The correct existential realization in section 7h is preserved.

The forward Theorems A/B are not refuted by this countermodel.
The manuscript contains complete additional examples removing mutual
rationality, mutual game knowledge and the positive-prior event premise,
plus an example where all Theorem A/B conditions hold but actual pure
play is not a pure Nash equilibrium.

## Complete result/proof map

All body labels below have prefix thm:p17-ab-.
Every row has one reciprocal annex item with prefix annex:p17.ab.

| Body suffix | Annex suffix | Extent |
| --- | --- | --- |
| measurability | measurability | Insertion measure, events, real finite sums, countable knowledge operations and conditional averaging. |
| introspection | introspection | Lemma 2.6 and source 4.1/4.3/4.4; finite positive-length reachability computation, including nonfactivity. |
| preliminary | preliminary | Actual action recovery and pure Nash inequalities. |
| supported-actions | supported.actions | Source Lemma 4.2 using positive events, not positive atoms. |
| two-player | two.player | Theorem A and actual-pure-play distinction. |
| type-bridge | type.bridge | Both exact finite encodings connecting P17.18 to the source model. |
| illustration | illustration | Figures 1–2; all six types and failed belief levels. |
| local-average | local.average | Source Lemma 4.5 on arbitrary measurable spaces. |
| product | product | Source Lemma 4.6; full induction without division by zero marginals. |
| many-player | many.player | Theorem B, independent agreement subclaim, all denominators, almost-sure support. |
| marginal-example | marginal.example | Example 5.1; every conditional law/payoff and product-law deviation. |
| chain-example | chain.example | Example 5.2; all types; unique equilibrium; explicit arbitrary-depth boxes. |
| no-prior | no.prior | Example 5.3; rationality, disagreement with Nash and impossibility of a common prior. |
| depth-disagreement | depth.disagreement | Explicit weighted finite path giving 2/3 versus 1/3 at any prescribed finite depth. |
| independent | independent | Remark 7.1, retaining agreement and coordinate-versus-rest independence. |
| converse | converse | Equilibrium realization and repaired pointwise converses, including preliminary and many-player forms. |
| support-failures | support.failures | Four fully specified removed-hypothesis countermodels. |
| knowledge-of-equilibrium | knowledge.of.equilibrium | Fixed-profile knowledge implication and two finite countermodels. |

Total: **18 reciprocal result/proof pairs**. The chapter also has six
definition/method entries: system, conjecture, knowledge, marginal-example,
chain-game and computation. Main label: sec:p17-epistemic-nash-conditions.
Annex section label: sec:annex-p17-epistemic-nash-conditions.

## Actual predecessor interfaces and source boundaries

The complete actual body and annex at
handbook/parts/p17/epistemic-game-theory.tex and
handbook/annex/p17/epistemic-game-theory.tex were read, including the
mutual-conjecture proof and its many-player/correlation countermodels.
The finite-game, mixed-strategy and Nash-support interfaces in
handbook/parts/p17/finite-strategic-games.tex were also read.
The previously read handbook conventions and current edition contract
govern this authoring block.

Stable dependencies are def:p17-egt-types,
thm:p17-egt-mutual-conjectures, def:p17-nash-equilibrium and
thm:p17-best-response-geometry. The new proof restates the short support
argument explicitly rather than treating a citation as its proof.
The finite bridge fixes the game and treats actions as separate coordinates
when necessary; it does not silently identify the two type formalisms.

No unread-page or free-acquisition gap remains for the selected paper.
The cited Mertens–Zamir universal hierarchy representation, full earlier
Tan–Werlang/Brandenburger–Dekel frameworks, and Aumann's global
correlated-equilibrium presentation remain distinct sources. Their claims
are identified as related presentations rather than new proved theorems
of this component. P17.18's separate one-person perspective/depth and
dynamic-game refinements are not discharged by association.

## Intakes, author read-through and pins

Disjoint bibliography intake:
handbook/bib/intake-p17-epistemic-nash-conditions.bib,
key AumannBrandenburger1995Epistemic.
Disjoint notation intake:
handbook/registry/symbols-intake-p17-epistemic-nash-conditions.csv.
The scope is P17.19; source letters with different local
types are retained and explicitly declared, rather than silently renamed.
Root owns shared routes, bibliography, registry and progress.

The whole saved body, annex, note and intakes received the author's
read-through. Direct corrections completed the many-player and preliminary
converse forms, stated the separate agreement/factorization scope, gave
the actual-pure-play counterexample, and supplied both finite type
encodings. The source's K^1, K^r and CK operators are retained.
The explicit p_i subscript records the player index implicit in the
source's p(E;s_i); this notation correspondence is declared in the body.
The notation intake contains **26 rows** plus its header.
Amended passages received the final author read-back. No independent
review, scanner, test, manuscript build or manuscript render was run.
Final file extents and SHA256 pins are provided in the handoff.

## Bounded integration extension: P17.19 and P19.11

On 9 September 2026 the assigned production extension appended this chapter
to handbook/parts/p17.tex and its annex to handbook/annex/p17.tex.
It also routed the separately returned explanatory-preferences chapter
and its four-proof annex as P19.11 after reading that complete source note.
The combined routing adds **22 existing result/proof pairs**: 18 here and
four in the Lombrozo treatment. No new theorem or source review was begun.

The P17.18 reader has a positive link immediately after its mutual-conjecture
result to the completed original two-player and many-player conditions and
the finite-model bridge. Its existing final proofboundary is preserved
verbatim. Terminal-type representation, dynamic refinements, Polak and
one-person perspective/depth presentations remain separate obligations.

**Only the following combined files are for root append:**

- handbook/bib/intake-p17-19-p19-11-integration.bib:
  exactly two entries, AumannBrandenburger1995Epistemic and
  Lombrozo2007SimplicityProbability.
- handbook/registry/symbols-intake-p17-19-p19-11-integration.csv:
  exactly 34 rows plus the canonical header, with 26 P17.19 rows and
  eight P19.11 rows, all with meta precedence.

All original first-use labels and local notes are retained. The four
original per-chapter intakes are preserved as provenance and must not
also be appended. The parent retains canonical bibliography, symbols,
progress and admission ownership. Integration read-back and exact
fingerprints are returned in the production handoff.

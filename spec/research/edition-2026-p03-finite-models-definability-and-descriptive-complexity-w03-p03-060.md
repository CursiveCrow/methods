# Research note: P3 39.7 Datalog, infinitary finite-variable logic and definability comparisons (packet w03a-p03-060)

Owned files:

- handbook/parts/p03/finite-models-definability-and-descriptive-complexity-w03-p03-060.tex (body, `\chapter`, toc tag `%% toc: P3 39 39.7`)
- handbook/annex/p03/finite-models-definability-and-descriptive-complexity-w03-p03-060.tex (annex, `\section`, label sec:annex-p03-w03-p03-060)
- handbook/bib/intake-p03-finite-models-definability-and-descriptive-complexity-w03-p03-060.bib
- handbook/registry/symbols-intake-p03-finite-models-definability-and-descriptive-complexity-w03-p03-060.csv

Label tag: `p03-w03-p03-060`.

## Duty worked (MP-0, writable part)

- L^k_infty-omega and L^omega_infty-omega definitions: linked (def:p03-w03-p03-056-grammar, def:p03-w03-p03-055-logics), not restated.
- Existential L^k_infty-omega and its (not-equal) variant, first-order parts, preservation relations: new (def:p03-w03-p03-060-existential).
- k-pebble characterization of L^k equivalence: linked (thm:p03-w03-p03-056-eternal, thm:p03-w03-p03-055-pebble).
- Existential k-pebble and (exists, not-equal, k)-pebble characterization, with finite-B first-order clause: new, full annex proof (thm:p03-w03-p03-060-existential-game); definability corollary, preservation corollary, clique asymmetry, all proved.
- LFP (lfp and gfp), IFP, PFP into L^omega_infty-omega on finite structures: new, full annex proof with explicit variable bound (thm:p03-w03-p03-060-fp-in-lomega), via the substitution lemma thm:p03-w03-p03-060-substitution.
- Datalog and Datalog(not-equal) into existential L^omega(not-equal), on all structures: new, full annex proof (thm:p03-w03-p03-060-datalog-in-existential, with stage lemma thm:p03-w03-p03-060-datalog-stages).
- Datalog (with not-equal and negated input atoms) as a fragment of LFP using simple nested lfp only: new, full annex proof via finite Knaster-Tarski and Bekic lemmas (thm:p03-w03-p03-060-datalog-in-lfp).
- LFP <= IFP <= PFP on finite structures: new, full proof (thm:p03-w03-p03-060-fp-comparison); IFP definition def:p03-w03-p03-060-ifp.
- Gurevich-Shelah (finite) and Kreutzer (general) IFP = LFP: stated cited= (thm:p03-w03-p03-060-gurevich-shelah).
- Abiteboul-Vianu: linked to thm:p03-w03-p03-059-abiteboul-vianu (owned by 059), with Kolaitis's outline of the hard direction described in one paragraph; not restated as a theorem.

Units ED26-SRC-050-0001 and ED26-SRC-050-0002 are readonly here (owner w03-p03-054); their components were not written by this packet.

## Sources read in this session

Held:

- source/references/acq-r1-ACQ-2026-10-0472/graedel-2007-fmt-descriptive-complexity-ch3.pdf
  (Graedel ch. 3, author-hosted PDF dated 2007-04-25; running page = PDF page + 124).
  Read: p. 155 (Def. 3.3.7, Ex. 3.3.8), pp. 171-173 (Def. 3.3.39, Lemma 3.3.41 with proof,
  Thm. 3.3.42 opening), p. 174 (Ex. 3.3.44, Def. 3.3.45, Prop. 3.3.46), pp. 175-176
  (least vs inflationary, Def. 3.3.47, Thms. 3.3.49-3.3.51), pp. 177-180 (PFP, Ex. 3.3.53,
  Prop. 3.3.54, Thm. 3.3.55, Thm. 3.3.56), pp. 180-182 (Def. 3.3.57, Exs. 3.3.58-3.3.59,
  Exercises 3.3.60-3.3.61, Def. 3.3.62, translation to S-LFP, Def. 3.3.63, Prop. 3.3.64).
  Page locators verified per PDF page with pdftotext -f/-l.

Online (sources_read_online):

- Kolaitis, "On the Expressive Power of Logics on Finite Models", manuscript dated
  1 August 2003, https://dbai.tuwien.ac.at/staff/pichler/dbt/kolaitis.pdf (TU Wien course
  page). Fetched with WebFetch in this session; fetched bytes md5
  cc02cc606380b8cf3667b9a4a805978d, identical to
  tmp/agent-scratch/w03a-w03a-p03-056-b1-author/dl/kolaitis.pdf, from which text was
  extracted. Not the version of record (ch. 2 of the 2007 Springer volume); the reader
  text says so once. Read: pp. 38-46 (Prop. 6.10, Defs. 6.12-6.15, Thm. 6.17, Sect. 6.3,
  Exs. 6.18-6.20, Prop. 6.21, Def. 6.22, Prop. 6.23, Ex. 6.24, Prop. 6.26, p. 46 remarks),
  pp. 49-54 (Gurevich-Shelah remark, Defs. 6.34-6.35, Ex. 6.36, Prop. 6.37, Thm. 6.38,
  Def. 7.1, Thm. 7.2, well-foundedness remark), pp. 63-77 (Sects. 7.4-7.5 incl.
  Thms. 7.24-7.25; Sects. 8.1-8.2: Defs. 8.1, 8.4-8.6, Thms. 8.2, 8.3, 8.7, Cor. 8.8,
  Method 8.9, Thm. 8.10, Prop. 8.11). The relation glyph of Def. 8.6 was read from a
  page render of p. 72: \preceq^{\exists,k}_{\infty\omega}.

## Provenance decisions

- Notation follows the 056 chapter (v_1..v_k, labels [k], fr, positions (alpha,beta),
  rho_{alpha,beta}) so the existential game is the one-sided version of
  def:p03-w03-p03-056-pebble-game; Kolaitis's unused-pebble/separate-removal variant is
  noted as interchangeable.
- Kolaitis Thm. 8.7 is stated without proof in the manuscript; the annex proof is
  written in full here.
- Kolaitis Thm. 7.2 and Thms. 8.2/8.3 give sharp variable bounds; the annex proves the
  inclusions with explicit weaker bounds. The sharp bounds are stated as Kolaitis's and
  not proved.
- Datalog in LFP: Graedel goes through S-LFP and the Bekic principle; the annex proves
  a finite Bekic lemma and builds nested simple lfp formulas directly (no >= 2 element
  hypothesis as in Kolaitis Thm. 6.17).
- Gurevich-Shelah and Kreutzer: cited (Graedel gives prose for the finite case and
  derives Kreutzer's theorem only from the unproved Thm. 3.3.49).

## Existing treatments found

- Listed: def:p09-datalog, sec:p09-presentation-n-c-024, sec:p09-presentation-n-c-002. Linked.
- Not listed in the packet (sibling chapters written in the same period):
  parts/p03/...-w03-p03-055.tex (def:p03-w03-p03-055-logics, def/thm:p03-w03-p03-055-pebble);
  parts/p03/...-w03-p03-056.tex (def:p03-w03-p03-056-grammar, -pebble-game,
  thm:p03-w03-p03-056-eternal, -walks, -renaming, -coincidence);
  parts/p03/...-w03-p03-059.tex (def:p03-w03-p03-059-lfp, -pfp, thm -positive-monotone,
  -lfp-in-pfp, -gfp-dual, -abiteboul-vianu, -ptime-pspace). All linked, none duplicated.

## Block 1 of w03a (second pass)

Gap list received: L^k / L^omega definitions, existential variants, k-pebble and existential
k-pebble characterizations, FP into L^omega, Datalog into existential L^omega(neq), Datalog in
LFP, LFP vs IFP vs PFP, Abiteboul-Vianu. The list said none of these is on the reader route;
neither this chapter nor siblings 055/056/059 is yet input by handbook/parts/p03.tex (driver,
lead action; insertion proposal in the return file).

Added this pass:
- def:p03-w03-p03-060-stage-comparison (rank, le^inf, prec^inf; Graedel Def. 3.3.47 p. 175,
  read from a page render this session).
- thm:p03-w03-p03-060-stage-comparison (finite inflationary stage comparison in LFP), full annex
  proof: simultaneous positive induction on two 2r-ary relations (lambda: rank(a) <= rank(b),
  rank(a) finite; eta: rank(b) < rank(a)), soundness by pre-fixed point, completeness by
  induction on rank, nested by Bekic Lemma B of the Datalog-in-LFP annex. Positive LFP
  refinement (Graedel Thm. 3.3.49 second sentence) not proved.
- thm:p03-w03-p03-060-gurevich-shelah now proved (was cited=): IFP = LFP on finite structures.
- thm:p03-w03-p03-060-kreutzer: cited= Graedel Thm. 3.3.50 p. 176 (infinite structures).
- thm:p03-w03-p03-060-av-easy: (E_LFP) <=> (E_IFP), each implies P = PSPACE; proof via
  thm:p03-w03-p03-059-ptime-pspace and thm:p03-w03-p03-059-lfp-in-pfp.
- Locators re-verified this session: Graedel pp. 175, 176, 180 (pdftotext + render of p. 175);
  Kolaitis p. 49 (Gurevich-Shelah remark) and p. 68 (Thms. 7.24, 7.25) from the local copy of
  the TU Wien PDF (md5 cc02cc606380b8cf3667b9a4a805978d).

L^k_infty-omega / L^omega_infty-omega definitions and the k-pebble characterization of
L^k equivalence: not restated here; they are def:p03-w03-p03-056-grammar,
thm:p03-w03-p03-056-eternal (full annex proof) and def/thm:p03-w03-p03-055-pebble. Restating
them would be a second treatment; they reach the reader once 055/056 are routed.

## Block 2 of w03a

Gap list received (in order): (1) exact k-variable fixed-point correspondence, Kolaitis Thm. 7.2;
(2) exact k-Datalog correspondence, Kolaitis Thms. 8.2-8.3, with FO^k stage components of systems;
(3) converse bridges: Kolaitis Prop. 6.21 and the Datalog(neq) analogue (p. 45), EFP subset Datalog
(Graedel Prop. 3.3.64); (4) positive-LFP stage comparison on finite structures (Graedel Thm. 3.3.49).

Sources this block: Kolaitis manuscript re-fetched with WebFetch from
https://dbai.tuwien.ac.at/staff/pichler/dbt/kolaitis.pdf on 13 October 2026; md5
cc02cc606380b8cf3667b9a4a805978d, identical to the local copy from which pages were extracted
(pdftotext pp. 49-57, 69-71; page renders pp. 38-46, 69-71). PDF page = printed page.
Graedel held PDF: page renders of running pp. 175-176 and 180-182 (PDF pp. 51-52, 56-58).

Added (all with full annex proofs):
- thm:p03-w03-p03-060-variable-substitution: substitution of terms for variables in L^k, FO^k and
  the four existential languages (Kolaitis's closure property, p. 70, generalized to term maps).
- thm:p03-w03-p03-060-kv-stages: Kolaitis Thm. 7.2 with exact k (stages, inflationary and downward
  stages in FO^k on all structures; lfp, gfp, ifp, pfp in L^k on finite structures).
- def:p03-w03-p03-060-systems (Kolaitis Defs. 6.12, 6.15; k-Datalog p. 70; existential-conjunctive
  systems), thm:p03-w03-p03-060-continuity (closure at omega, Kolaitis p. 46).
- thm:p03-w03-p03-060-kv-systems: Kolaitis Thm. 8.2 for systems of positive EFO^k formulas.
  Decision: his second item prints EFO^k for the lfp components; stated with EL^k_infty-omega,
  and thm:p03-w03-p03-060-tc-not-fo (compactness) shows the printed reading fails.
- thm:p03-w03-p03-060-kdatalog-system: k-Datalog programs as systems of positive EFO^k formulas
  (Kolaitis p. 71 "refining Prop. 6.21"), using patterns mu: [r_i] -> T_k so head arities > k are
  handled; thm:p03-w03-p03-060-kdatalog: k-Datalog in EL^k, k-Datalog(neq) in EL^k(neq) (Thms.
  8.2 consequence and 8.3), goal arity r_i <= k (stated as the meaningful reading).
- thm:p03-w03-p03-060-datalog-systems: Kolaitis Prop. 6.21 and the p. 45 analogue, both directions,
  all structures; plus equality elimination for constant-free vocabularies (his rules have no
  equality literals). Decision: his statement asks each phi_i to be a single exists-conjunction;
  that version is false for programs with two rules per head; thm:p03-w03-p03-060-single-conjunction
  proves it (direct products; transitive closure), and the theorem uses finite disjunctions, as
  his own formulas for Exs. 6.20 and 6.24 do.
- def:p03-w03-p03-060-efp, thm:p03-w03-p03-060-efp-datalog: Graedel Prop. 3.3.64 both directions on
  all structures; converse by induction with lifting data (parameters of a system carried as extra
  arguments of the R_l); def:p03-w03-p03-060-efp-example.
- thm:p03-w03-p03-060-stage-comparison-positive: Graedel Thm. 3.3.49 second sentence, via
  thm:p03-w03-p03-059-immerman-normal-form (relational vocabularies; constants replaced by parameters).

Existing treatments found, not listed in the packet: handbook/parts/p03/...-w03-p03-061.tex
(section 39.8) has thm:p03-w03-p03-061-datalog (k-Datalog in EL^k for programs, with its own
substitution lemma thm:p03-w03-p03-061-substitution) and a second treatment of the existential
pebble game. The assessment for 39.7 required the system form here (061 covers programs only);
the overlap is reported as a proposed decision. 059's thm:p03-w03-p03-059-stage-comparison is
Immerman's stage comparison for monotone inductions (not the inflationary one) and is linked
through the normal form only.

## Continuation

State after w03a block 2: unit-compile ok (26 overfull boxes, cosmetic); fused-space check clean;
check.py shows no finding in these files. The four gaps of the block-2 list have text and annex
proofs. Open items still recorded:

1. Hard direction of Abiteboul-Vianu (statement owned by 059, cited=); unchanged.
2. Kreutzer IFP = LFP on infinite structures (cited=); unchanged.
3. Kolaitis p. 54 remarks: L^k-definability of transfinite stages of positive formulas, and
   LFP in L^omega on classes of bounded cardinality: stated as reported, not proved.
4. Nested LFP/IFP/PFP formulas: only the generous variable bound of fp-in-lomega is proved.
5. Overlap with w03-p03-061 (k-Datalog, existential games): needs a lead decision on which
   chapter keeps which statement.

## Author proof audit and correction, 2026-10-26

The inflationary stage-comparison proof now alpha-renames relation binders
and replaces only free occurrences of the distinguished relation. Without
this hygiene, a nested fixed point binding the same letter is changed by
the construction. For example, P(x) or exists y (E(x,y) and [lfp X z.X(z)](y))
defines the constant operator P; replacing the inner bound X by the current
comparison slice incorrectly adds predecessors. The semantic renaming and
replacement steps now exclude that case, including in the zero-ary collapse
argument.

The finite-variable stage theorem now fixes a supply of k >= 1 variables
containing every formula variable and every declared argument coordinate.
This makes m <= k explicit even if a coordinate never occurs in the body.
Previously a formula such as x_1 = x_1 for a binary operator could have fewer
occurring variables than argument coordinates, defeating the stated
coordinate-preserving renaming. Closed empty conjunction/disjunction supply
the initial truth and falsehood formulas, so the free-label assertion also
holds for zero-ary relations. The inflationary/greatest additions and unused
coordinate convention remain identified as editorial extensions of Kolaitis
Theorem 7.2, whose manuscript page 54 was checked.

The held dated Graedel author PDF was checked at running pages 176 and
181--182. Its stage-comparison references and the EFP converse left as an
exercise are distinguished from the manuscript's explicit finite and
lifting proofs. Printed-edition identity remains unestablished. The EFP
lifting/slice argument and finite-variable substitution construction were
reread. Kreutzer's infinite-structure collapse and the transfinite and
bounded-cardinality claims remain cited/reported, not proved here.

The final scoped four-pass TeX Live build succeeded: 51 pages, 26 overfull
warnings, and two external references unresolved in the isolated unit. No
new result label, proof-status upgrade, or source admission was introduced.

These are author corrections and bounded verification, not independent
review, source admission, complete-source coverage, or book completion.

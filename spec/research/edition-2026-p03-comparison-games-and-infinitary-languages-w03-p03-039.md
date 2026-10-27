# w03a-p03-039 (P3 ch. 35, sections 35.5-35.7): research note

Owned files:
- body `handbook/parts/p03/comparison-games-and-infinitary-languages-w03-p03-039.tex` (647 lines)
- annex `handbook/annex/p03/comparison-games-and-infinitary-languages-w03-p03-039.tex` (653 lines)
- bib intake `handbook/bib/intake-p03-comparison-games-and-infinitary-languages-w03-p03-039.bib` (Marker2014InfinitaryNotes, Marker2016Infinitary)
- symbol intake `handbook/registry/symbols-intake-p03-comparison-games-and-infinitary-languages-w03-p03-039.csv`

Placement (from the packet's insertion proposal): body `\input` after `parts/p03/presentations/n-a-004-02` in
`handbook/parts/p03/classification-theory.tex` (after line 206); annex `\input` after
`annex/p03/feferman-vaught-composition` in `handbook/annex/p03.tex` (after line 7). The drivers are lead-owned;
nothing was changed in them.

## Sources read in this session

- Marker, *Lectures on Infinitary Model Theory*, Math 512 lecture notes, UIC Fall 2013, PDF created
  10 January 2014, 163 pp., author-hosted at https://homepages.math.uic.edu/~marker/math512-F13/inf.pdf
  (linked as "Lecture notes (January 2014 version)" from https://homepages.math.uic.edu/~marker/math512-F13).
  This is an earlier version of the 2016 Cambridge book (Lecture Notes in Logic 46), not the version of record.
  Read: contents pp. 1-3; Part I ch. 1 pp. 4-12 (Defs. 1.3, 1.11, 1.16, 1.18; Exs. 1.1-1.32; Thms. 1.23, 1.31);
  ch. 2 pp. 13-22 through Ex. 2.34 (Defs. 2.1, 2.3, 2.9, 2.10, 2.18, 2.25, 2.33; Thm. 2.4, 2.13, 2.22, 2.32;
  Lemmas 2.15, 2.17; Cor. 2.23, 2.26); ch. 4.1 pp. 39-43 (Def. 4.1, Lemma 4.2, Exs. 4.3-4.5, 4.7, Thms. 4.6, 4.8).
  Page images of pp. 13, 16, 19, 39 rendered and checked for glyphs (the text layer drops several symbols,
  e.g. the \notin of C1 and the \ne of Ex. 1.5).
  Local copy: tmp/agent-scratch/w03a-w03a-p03-039-b1-author/marker/inf.pdf (+ inf.txt, infp.txt with page markers).

- Nadel, ch. VIII of Barwise-Feferman (eds.), *Model-Theoretic Logics*, Perspectives in Logic 8 (ASL; open-access
  Project Euclid copy reproducing the Springer 1985 pagination), read in block 2 (2026-10-12):
  Part I https://projecteuclid.org/euclid.pl/1235417273 (PDF via /ebook/Download?urlid=pl%2F1235417273&isFullBook=False,
  19 pp., book pp. 269-287) and Part II https://projecteuclid.org/euclid.pl/1235417274 (29 pp., book pp. 288-316).
  Read closely: pp. 271-290 (sec. 1-5.2, page images of pp. 273, 275-279, 288-289 checked for glyphs); text layer of
  pp. 290-305 skimmed; pp. 305-316 (rest of sec. 7 and sec. 8) not yet read.
  Local copy: tmp/agent-scratch/w03a-w03a-p03-039-b1-author/nadel/ (partI.pdf, partII.pdf, *.txt, page PNGs).
  Book page = Part I PDF page + 268; Part II PDF page + 287.

## Access attempts that failed (no copy read)

- (block 1, superseded in block 2) Nadel, ch. VIII, pp. 271-316 (ED26-SRC-049-0008):
  - held preview tmp/edition-2026-catalog-src038/tail-039-068/SRC-049-pageplace-preview-2026-09-09.pdf: contents
    only (reading text line 417-433 lists §§1-8 with start pages), no chapter body.
  - Project Euclid https://projecteuclid.org/euclid.pl/1235417273, .../euclid.pl/1235417274,
    https://projecteuclid.org/ebook/Download?urlid=pl/1235417273&isFullBook=false and the same for 1235417274:
    every request (curl and WebFetch) returned an Incapsula "Pardon Our Interruption" bot-check page
    (incident IDs 673000730020728939-75054201354392138, -22781911036400199). Not bypassed. The p03-022 packet
    recorded the same response for the sibling chapter pl/1235417272.
  - Cambridge Core chapter page (DOI 10.1017/9781316717158.013): paywalled ("Get access ...").
  - Web search for author preprint / institutional / other open version: none found.
- Karp 1964 (Karp1964): not held; web search found only catalogue records and reviews; no free copy.
- Scott 1965 (Scott1965): not held; Elsevier/North-Holland chapter, paywalled; PhilArchive record has no text.
- Keisler 1971 (Keisler1971Infinitary): not held; Keisler's publication page (people.math.wisc.edu/~hkeisler/papers.html,
  entry 36) lists the book with no download link.
- Marker 2016 printed book: Cambridge paywall; the 2014 notes were used instead (A3 version rule).

## Source-to-text decisions

- The notes' Ex. 1.19(a) needs |tau| < kappa; stated as a warning (def:p03-w03-p03-039-fragment-size).
- Def. 2.1 clause ii misprint ("for all g ... g ⊇ f") read symmetrically to clause i; said in reader text.
- Thm. 1.31 clause vi misprint (inner ∀v̄) dropped; said in reader text.
- Lemma 2.17 proof prints Γ_α ⊆ Γ_β and pairs in Γ_{α+1} \ Γ_α; corrected direction stated in reader text.
- Thm. 4.8 lacks "Σ nonempty"; counterexample given (def:p03-w03-p03-039-nonempty).
- Thm. 4.6 printed proof: Λ enlarged by atomic and negated atomic sentences; induction made on an explicit depth δ.
- Def. 2.18 assertion sr(M) = sup r(ā): only ≤ proved (thm:p03-w03-p03-039-tuple-rank-bound); equality recorded
  as an unproved source assertion (proofboundary def:p03-w03-p03-039-sr-equality). Superseded in block 4: the equality is
  refuted by thm:p03-w03-p03-039-sr-counterexample; the label is now an hbwarning.
- Exercises used as results are proved in the annex; the reader text says the notes pose them as exercises.

- (block 3) Ex. 2.21(a) prints "(M,a) ~_alpha (N,b)"; read as ~_beta within M (said in reader text).
- (block 3) Ex. 2.5 prints "M_0 ⊆ N" for the given substructure; read as M_0 ⊆ M (said in reader text).
- (block 3) Ex. 1.13(b) "kappa = beth_alpha for some limit ordinal alpha": true for infinite kappa when 0 counts as a limit
  (kappa = aleph_0 is a categoricity cardinal); stated as "alpha = 0 or a limit" with the reason in reader text.
- (block 3) p. 7 claims archimedean ordered fields are isomorphic to subfields of R; only the order-embedding needed for the
  cardinality bound is proved; reader text says so.
- (block 3) Ex. 2.27 needs tau countable; counterexample for uncountable tau given (def:p03-w03-p03-039-countable-vocabulary).
- (block 3) Ex. 1.12(e) "incomplete ordered fields" read as "not Dedekind complete"; stated in the theorem.

## Existing treatments found

Listed in the packet: handbook/parts/p02/variants.tex 344-417 (def:p02-lomega-one-omega,
thm:p02-lomega-one-omega-calibration cited=Scott1965, def:p02-infinitary-derivation, thm:p02-karp-completeness cited=Karp1964,
Scott-sentence prose); handbook/parts/p03/presentations/n-a-004-02.tex 126-237 (Morley-route Scott construction with annex proofs);
handbook/parts/p03/preservation-abstract-logic.tex. The new section links to these and gives an explicit bridge
(sec:p03-w03-p03-039-bridge). Not listed in the packet: handbook/parts/p02/many-sorted-and-alternative-first-order-w02-p02-039.tex
cites Karp1964/Scott1965 (pointer level; its note records Karp/Scott as not held); the w02c-p02-003 KPU admissible-set
definition (after Makkai), unrouted, noted by the assessment.

## Continuation

Block 4 (2026-10-13; scratch tmp/agent-scratch/w03a-w03a-p03-039-b2-author/): Marker 2014 notes pp. 21-27 re-read from the
local copy (text layer + page images of pp. 21-26 rendered to check glyphs: Def. 2.35 prints "union a_n in X", Lemma 2.36
proof prints an intersection for the union, Thm. 2.46 (ii) is "M not-equiv N iff M^a not-iso N^a a.e.", the game table of
Ex. 2.39 alternates single moves). Written, in the assessment order:
- sr = sup r: REFUTED. Proofboundary replaced by hbwarning def:p03-w03-p03-039-sr-equality + thm:p03-w03-p03-039-sr-counterexample
  (E an equivalence relation with one 3-class and one 2-class, plus an infinite P-part; sr = 2, sup r = 1, SR = 2;
  annex:p03-w03-p03-039-sr-counterexample). The pure infinite set shows SR != sr as well.
- new body subsection sec:p03-w03-p03-039-approximations (body 996-1299; annex from 1373): Ex. 1.28 (elementary chains),
  Ex. 2.31 (all three directions; Gao remark attributed, not proved), Thm. 2.32 (with the finite-model case added),
  Def. 2.33, Ex. 2.34 (printed hypothesis "M countable" makes it trivial; proved for M of any cardinality), all of
  sec. 2.3: Def. 2.35, Lemma 2.36, Ex. 2.37, Lemma 2.38, Ex. 2.39, Ex. 2.40, Def. 2.41 (indexed families convention),
  Ex. 2.42 (holds for every a with indexed families), Thm. 2.43 + Ex. 2.44, Cor. 2.45, Thm. 2.46 + Ex. 2.47 (forward
  direction of (ii) proved with the ranks ~_alpha, not via Thm. 2.43, because the notes' route needs X to approximate a
  distinguishing sentence), Cor. 2.48, and the abelian-group remark as thm:p03-w03-p03-039-kueker-free (needs "not free on
  finitely many generators"; Z is the counterexample to the unqualified form).
- bridge paragraph "Atomic models and countable approximations".
Source-to-text decisions this block: listed in reader text next to each item (Ex. 2.31 "phi" read as sigma; Def. 2.33 "T"
read as phi; Ex. 2.34 hypothesis; Def. 2.35/Lemma 2.36 misprints; Def. 2.41 fragment condition weakened to subformulas).
Remaining for S04, in order: sec. 2.4 (Exs. 2.49-2.53, Def. 2.54, Exs. 2.55-2.57; check Ex. 2.57 against Eklof's strongly
aleph_1-free condition before writing), exercises 1.14, 1.20, 1.21 (membership in the fragment), 1.22, 1.24(a), 1.25-1.27,
1.29, 1.30, 2.7, 2.8, 2.11, 2.12, 2.16, 2.19, 2.20, 4.4, 4.5, 4.7 (first grep the body for each: some may already be
present from block 1). Then Nadel C001-C008 as below (Nadel section now starts at body line 1372, annex line 1948).
check.py --tree handbook ran to completion in under 590 s this block (only bib-key findings on own intake keys).

### Block 3 continuation record

Block 3 (2026-10-12, this run; scratch tmp/agent-scratch/w03a-w03a-p03-039-b2-author/): Marker 2014 notes re-read
(local copy from block 1, pp. 4-27; page images of pp. 8 and 19 rendered to confirm beth_alpha in Ex. 1.13 and the
indices of Ex. 2.21). Written, in the order of the assessment list:
- body sec:p03-w03-p03-039-expressive (lines 246-463) and annex 655-~990: Ex. 1.2, Def. of ultraproducts + Ex. 1.6 a,b,
  Ex. 1.7 i-ix (ii, ix reuse Nadel's sentences), upward LS failure (p. 7: Z-order, f.g. groups, archimedean fields),
  Ex. 1.9 linked to thm:p03-w03-p03-039-nadel-ordinals (no second treatment), formula count + Ex. 1.10, Def. 1.11,
  Ex. 1.12 a-f, Ex. 1.13 (Silver) a,b, Ex. 1.15. The p. 7 remark that was left unproved in block 1 is now replaced by
  thm:p03-w03-p03-039-upward-ls-failure.
- body sec:p03-w03-p03-039-complete-sentences (lines 824-978) and annex ~990-1282: fragment-size lemma, Ex. 2.21 a,b,
  Ex. 2.5, Ex. 2.6 (with Dedekind's countable-subgroup lemma proved), Cor. 2.23, Ex. 2.24, finite-structure lemma,
  Ex. 2.27 (+ countable-tau warning), Ex. 2.28, Ex. 2.29, Ex. 2.30.
- bridge paragraph "Expressive power and complete sentences" in sec:p03-w03-p03-039-bridge.
Remaining for S04, in order: Ex. 2.31 (proof planned: (i)=>(ii) via countable L_{infty,omega}-elementary N_0 ⊊ N_1 inside an
uncountable model, built by closing under the Scott-formula system P; (iii)=>(i) via an omega_1-chain using the
A-elementary chain lemma, Ex. 1.28), Thm. 2.32 (finite-model case needs: elementary equivalence to a finite structure in a
countable vocabulary gives isomorphism, and finite models of complete theories are atomic), Def. 2.33 + Ex. 2.34,
sec. 2.3 (Kueker), sec. 2.4; sr = sup r (open: tried several structures (graphs, equivalence relations with classes of
sizes 2 and 3) and found sup r = sr each time; no proof found: the one-step condition defining r(a) is not upward closed in
alpha, e.g. a singleton in a 3-class of the 2/3-equivalence-relation example has r = 0 but fails the condition at 1).
Then Nadel C001-C008 as listed under "Remaining (next block, in order)" below.

### Block 2 continuation record


Block 1: Marker 2014 notes presentation (sec:p03-w03-p03-039-marker); see the block-1 list below.

Block 2 (2026-10-12): new section sec:p03-w03-p03-039-nadel appended to the body (lines 649-1125) and
sec:annex-p03-w03-p03-039-nadel appended to the annex (from line 655). Written from Nadel ch. VIII:
- sec. 1: Def. of the logics (p. 273), subformula free-variable lemma (p. 273), five L_{omega1 omega} expressibility
  claims (pp. 272-274), well-orderings in L_{omega1 omega1} under AC (p. 274), ordinal-characterizing sentences
  (exercise, p. 274).
- sec. 2.1: Def. of partial isomorphism / kappa-back-and-forth set / Karp property (p. 276); warning that F must be
  nonempty (printed definition admits F = empty); bridge lemma to Marker's partial embeddings and systems;
  Thm 2.1.1 via the bridge (different route from the source's induction, said in reader text); Cor 2.1.2;
  the four examples (DLO, ACF finite/infinite trdeg, ordinals) with the equal-characteristic correction.
- sec. 3.1: Def. 3.1.1, Def. 3.1.2 with corrections (C4 misprint "in C"; C7 basic terms must include C and constants,
  counterexample given), Thm 3.1.3 (i),(ii) with a direct Henkin proof.
- sec. 5.1-5.2: Delta_0/Sigma_1/Sigma, end extensions, persistence lemma, KP, admissible sets/structures, rudimentary,
  o(B), H(kappa), HF, HC, H(kappa) admissible for regular kappa (AC), o(HF) = omega.
Source-to-text decisions: Nadel's fragment/consistency property kept distinct from Marker's; field facts F1-F4
stated as a convention (algebra, not proved here).

Remaining (next block, in order):
- C001: sec. 1.3 claims (aleph_1-free abelian groups, free abelian groups, Ulm invariants, Lopez-Escobar non-
  definability of well-orderings and non-PC, Nadel 1974b scattered orders), Scott sentence in an arbitrary logic,
  sec. 1.4 reduction to omitting types, sec. 1.5 L*_{omega1 omega} with the substitution axiom (*) and its claims.
- C002: Remarks 2.1.3 (kappa analogue of Karp, Chang cf = omega, Morley aleph_1 example, Shelah n(M) results,
  embedding analogues), sec. 2.2 potential isomorphism Thm 2.2.1 (forcing), Remarks 2.2.2.
- C003: failure of model existence for uncountable fragments; sec. 3.2 Karp calculus and Thm 3.2.1, Remarks 3.2.2;
  sec. 3.3 interpolation (Lopez-Escobar; Keisler's consistency-property proof), Beth, Robinson failure and weak form,
  3.3.1-3.3.2 (Malitz preservation); sec. 3.4 Kueker; sec. 3.5 Thm 3.5.1 omitting types, 3.5.2; sec. 3.6 Loewenheim
  number, Thm 3.6.1 Hanf number beth_{omega1}, 3.6.2-3.6.3, Thm 3.6.5 Landraitis.
- C004: all of sec. 4 (Thm 4.1.1, Lemma 4.1.2, Def 4.1.3, Lemma 4.1.4, Scott height, Def 4.1.5, Thm 4.1.6, Thm 4.2.1,
  local definability, Thm 4.2.2); bridge to the Marker Scott material is the cheapest first step.
- C005: sec. 5.1 primitive recursive closure; ZF-minus claims for H(kappa); L(omega_1^CK); HYP(x); sec. 5.3 KP
  theorems and Lemmas 5.3.1-5.3.2, truncation lemma, 5.3.3, 5.3.4; sec. 5.4 KPU; sec. 5.5 Thms 5.5.1-5.5.4;
  sec. 5.6 Barwise compactness 5.6.1-5.6.2; sec. 5.7 application.
- C006, C007, C008: not started (C007 from p. 305 on and C008 not yet read).

### Block 1 continuation record

Block 1 (this block):
- N-a-059-S04-PRESENTATION/PROOF/BRIDGE: partial. Written from the 2014 notes: ch. 1 (language, ≡∞,ω, compactness failure,
  formal negation, fragments, countable fragments, downward LS, Chang's theorem), ch. 2.1-2.2 (Karp's theorem, ∼α,
  quantifier rank, Thm 2.13, Scott formulas, Scott rank, tuple ranks, Scott sentence, Scott's theorem, complete sentences,
  Cor. 2.26), ch. 4.1 (consistency properties, Lemma 4.2, model existence, extended model existence), bridge to the
  Morley route and to variants.tex. Remaining in Marker Part I chapters 1-2: Exs. 1.6-1.15, 1.20-1.22, 1.25-1.30, Def. 1.11
  (PC classes) and Ex. 1.12-1.14, Exs. 2.5-2.8, 2.16, 2.19-2.21, 2.24, 2.27-2.31, 2.34; Cor. 2.23; Def. 2.33; Thm. 2.32;
  §§2.3 (Kueker countable approximations) and 2.4; Exs. 4.4, 4.5; the equality sr = sup r. Also: whether the 2016 book
  differs from the 2014 notes cannot be checked (book not reachable).
- N-a-059-S01 (Karp 1964), S02 (Scott 1965), S03 (Keisler 1971): blocked_source (no legitimate copy reachable).
- ED26-SRC-049-0008-C001..C008 (Nadel ch. VIII): blocked_source (bot check on Project Euclid; Cambridge paywall;
  held preview lacks pp. 271-316). Needs a user-supplied copy of pp. 271-316.
- Next block: continue S04 remaining items above (Cor. 2.23 and Thm. 2.32 first, then §2.3), and re-try the Nadel
  acquisition only if a held copy appears in held-sources.json.

## Author correction on 26 October 2026

The field comparison now supplies the previously unproved F1--F4 dependencies
at `thm:p03-w03-p03-039-nadel-field-dependencies`, with its reciprocal annex
proof. This includes finite algebraic extensions, transitivity, relative
algebraic closure, extension of isomorphisms by Zorn's lemma and transcendental
adjunction. The proof also supplies the exchange argument and finite-generator
bound actually used to select a fresh transcendental element. The existing
back-and-forth proof now points to that dependency proof.

The definition of a kappa-back-and-forth set now requires nonemptiness directly;
the following warning explains the omitted-condition counterexample without
making the reader repair the active definition. Transcendence degree is stated
as a cardinal supremum, with the finite/infinite distinction needed here.

These are author corrections, not independent admission. The other source,
exercise, and integration obligations recorded above remain open.

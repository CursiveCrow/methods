# w03a-p03-042 (P3, sections 36.1, 36.3) - research note

## Sources read this session

- Mostowski 1957, "On a generalization of quantifiers", Fund. Math. 44, pp. 12-36. Held file
  source/references/acq-r1-ACQ-2026-10-0311/ACQ-2026-10-0311.pdf (published journal pages, archival scan,
  13 PDF pages of two-page spreads, image only). All of pp. 12-36 viewed; pp. 14-17 re-rendered at higher
  resolution (scratch tmp/agent-scratch/w03a-w03a-p03-042-b1-author/) to read the displays.
  Locators used: p. 12 (truth values, I*, propositional function), p. 13 (support, limited quantifier,
  invariance, Q_T, Theorem 1, dual, unlimited quantifier, note 4 notation), p. 14 (Boolean operations;
  examples (a)-(c)), pp. 14-15 (example (d)), p. 15 (2(e), note 6 Los; calculus (S)), p. 16 (valuations,
  val, true/satisfiable), p. 17 (definability; completeness problem; property (E); Theorem 2; A_0 from
  Tarski [9] p. 69; B_0), p. 18 (facts (a)-(e)), p. 19 (fact (f); proof of Theorem 2 with the "it is
  known" non-r.e. citation; Theorem 3), p. 20 (Theorem 4; open general case; Theorem 5).
- Keisler 1970, Ann. Math. Logic 1, held file source/references/acq-r1-ACQ-2026-10-0225/ACQ-2026-10-0225.pdf
  (publisher version, PDF page = printed page). Read pp. 26-27 this session: Corollary 2.9, definition of
  valid, Corollary 2.10 (provable iff valid; valid sentences r.e. in the set of symbols of L), Corollary
  2.11, Vaught/Fuhrken attribution, uncountable-constants example. Earlier locators (pp. 4-27) come from
  the existing route treatment sec:p02-w02c-p02-003-keisler and are only cross-referenced.

## Sources not reachable (tried this session)

- Barwise-Feferman (eds), Model-Theoretic Logics: Mundici ch. VI "Other quantifiers: an overview"
  (pp. 211-233/234) and Kaufmann ch. IV. Project Euclid TOC
  https://projecteuclid.org/ebooks/perspectives-in-logic/Model-Theoretic-Logics/toc/pl/1235417263 returned
  an Incapsula "Pardon Our Interruption" bot-check page to WebFetch (not bypassed); Cambridge Core
  https://www.cambridge.org/core/product/identifier/CBO9781316717158A045/type/book_part requires login or
  purchase; Mundici's home page https://people.dimai.unifi.it/mundici/index.html links only the Cambridge
  DOI. Held file is the contents-only preview. Earlier acquisition ACQ-2026-10-0471 failed for the same
  bot-check reason.
- Lindstrom 1966, Theoria 32 pp. 186-195: Wiley paywall; web search found no author or repository copy.
- Church, Introduction to Mathematical Logic (the list behind Keisler's Axiom 0): not held, not sought
  further.

## Decisions

1. Mostowski's p. 14 display for T_2 (S^0) has "= wedge" where the verbal gloss, 2(e) (X_3 = <N,N,wedge>)
   and the Theorem 3 formula all require "= vee". Corrected in the reader (hbwarning
   def:p03-w03-p03-042-misprint), with the evidence.
2. p. 16 quantifier clause prints "support {i}" with argument y_1; rendered as the set
   {x : val_{M(i,x)I}(Z_1) = vee}, stated in the reader.
3. A_0: Mostowski takes Tarski's axioms of non-densely ordered rings (Undecidable Theories p. 69, not
   read). The handbook fixes an explicit list (discretely ordered commutative ring with unit, unit least
   positive) and states that the proofs use only facts (a)-(d); stated in def:p03-w03-p03-042-ring-axioms.
4. Mostowski's "it is known" (true sentences about the integers not r.e., p. 19) is discharged via a
   computable translation from L_A into the ring language plus thm:tarski-undefinability and the last
   clause of thm:representability (cited theorem in the restoration capture).
5. Theorem 2 fact (e): Mostowski chooses x with |Z_x| minimal; the written proof notes it is not needed.
   Uses AC for p+1+p = p.
6. Theorem 4 sufficiency ("obvious" in the source) is proved via E_m formulas, downward LS
   (thm:downward-ls) and countable completeness (cor:fol-completeness-countable).
7. Off-route labels avoided: thm:p02-downward-ls, thm:p02-fol-completeness-countable,
   def:p05-language-arithmetic, thm:p05-truth-undefinable are not on the static route (check reports them
   dangling); restoration labels used instead.
8. Keisler Cor. 2.10 second half: Keisler gives no argument; proved via a presentation hypothesis
   (def:p03-w03-p03-042-presentation) and decision procedures, with the Church-Turing thesis
   (def:p04-church-turing) as the declared identification step.
9. Host thm:p03-keisler-q-one (readonly) tied to a proved version thm:p03-w03-p03-042-q-one-host-form
   through a patch request (insert_after), not by changing its status (would break annex pairing).
10. Lindstrom comparison and Mundici/Kaufmann content: nothing written (A13).

## Continuation

Session 1 (w03a block 1), written:
- Body handbook/parts/p03/generalized-game-and-dependence-quantification-w03-p03-042.tex (chapter, toc
  P3 36 36.1,36.3): Mostowski sections 1-4 (definitions, Theorem 1, examples (a)-(d), misprint warning,
  2(e) classification, calculus (S), val lemma, definability, property (E), ring axioms and lemma,
  Theorems 2-5); Keisler effectivity (presentation definition, effectivity theorem, Axiom 0 warning);
  bridge (Mostowski class form + correspondence theorem; Keisler bridge convention; host-form theorem;
  worked example).
- Annex handbook/annex/p03/generalized-game-and-dependence-quantification-w03-p03-042.tex: proofs for all
  14 body results.
- Patch requests work/waves/w03a/patches/w03a-p03-042.json (driver inputs; host cross-reference sentence).
- Checks: unit-compile ok (16 overfull); find_fused_spaces clean; check.py --tree: no findings in owned
  files after the label replacements.

Still owed (in order):
(A) Mostowski section 5 (pp. 20-27): definition "does not distinguish infinite powers", Theorem 6 with
    Lemmas (a), (b) and the construction of I_0, Theorem 7 (cases (a)-(c), formulas A), Theorem 8 with
    the remark on p. 27. Source held; writable.
(B) Mostowski section 6 (pp. 28-35): monadic calculus (S^M), Theorem 9 with Mycielski's lemma (note 10),
    Theorem 10 with lemmas (a)-(d) and property (T), Theorem 11 with lemmas (a)-(e) and (c_n), the Fermat
    prime example (p. 35). Source held; writable.
(C) Bridge: comparison with Lindstrom 1966 - blocked_source.
(D) Mundici ch. VI sec. 1-4 and Kaufmann ch. IV - blocked_source (Project Euclid bot check).
(E) Comparison of Keisler's Axiom 0 (Church's list) with (0a)-(0g) - blocked_source (Church not held).

Session 2 (w03a block 1, 2026-10-12):
- Mostowski section 5 (pp. 20-27) written: body sec:p03-w03-p03-042-skolem-lowenheim (def infinite-powers,
  lemma transfer, def improper, lemma-a, method hull, lemma-b, theorem-six, theorem-seven, warning
  limit-point, theorem-eight, example + theorem theorem-eight-boundary); annex proofs for all 7 results.
  Decisions: (11) I_{k+1} := I_k u U_j I_kj (Mostowski omits I_k; needed for directedness in Lemma (b)).
  (12) Theorem 7 case (c) formula: printed limit conjunct for y_1 is vacuous when y_1 is least; added
  (Er)G(r,y_1). (13) Minimality choices in Theorem 7 replaced by comparison with the aleph_0 value (not
  needed). (14) Theorem 8: Mostowski's (11)-(14) isolated as lemma transfer(3). (15) Remark p. 27:
  unsuperscripted Sigma_I, Pi_I read as exists_I, forall_I (stated in reader).
- Mundici ch. VI (1985 Springer printing, pp. 211-233) NOW READ ONLINE: WebFetch of
  https://projecteuclid.org/ebook/download?urlId=pl/1235417271&isFullBook=false returned the PDF
  (24 pp, Adobe Paper Capture scan, saved tmp/agent-scratch/w03a-w03a-p03-042-b1-author/dl/mundici-ch6.pdf).
  Direct curl to projecteuclid.org got the Incapsula page (not bypassed); WebFetch was served the file.
- Still owed: Mostowski section 6 (pp. 28-35); Mundici sec. 1-4; Kaufmann ch. IV; Lindstrom 1966
  (blocked_source); Church's Axiom 0 list (blocked_source).
- Mundici sec. 1 partly written (sec:p03-w03-p03-042-mundici-po): Def 1.1.1, (1)-(3), Theorem 1.1.2
  (annex adds one-element structures and Skolem constants, steps 1 and 3), Q_0 in L(Q^H) (p. 216).
  Next, in order: Walkoe observation; Thm 1.2.1 (needs a PA-provable pairing bijection, prove in annex);
  Thm 1.2.2 Claims 1-2 (need RPC / Delta-closure definitions of Ch. II: not read; state them locally);
  Cor 1.2.3; Remark 1.2.4 (Montague - cited by Mundici); Prop 1.3.1; Thm 1.3.2; then sec. 2-4; then
  Mostowski sec. 6 (pp. 28-35); Kaufmann ch. IV (try the same WebFetch download route, urlId of ch. IV).
- Checks session 2: unit-compile ok (29 overfull); find_fused_spaces clean; check.py --tree: only
  bib-key Mundici1985OtherQuantifiers (own intake key).

Session 3 (w03a block 2, 2026-10-12): Mostowski section 6 (pp. 28-35).
- Source read this session: held file source/references/acq-r1-ACQ-2026-10-0311/ACQ-2026-10-0311.pdf,
  PDF spreads 8-12 (printed pp. 28-35, spread i = pp. 2i+12, 2i+13), rendered at 3.2x and 6x in
  tmp/agent-scratch/w03a-w03a-p03-042-b2-author/; p. 15 re-read for "(with identity)".
- Written: body sec:p03-w03-p03-042-monadic (subsections Theorem 9, 10, 11; body lines 690-1219) and
  bridge additions def:p03-w03-p03-042-monadic-bridge, thm:p03-w03-p03-042-monadic-bridge,
  def:p03-w03-p03-042-monadic-worked (body 1551-1638). Annex items annex:...-monadic-identity through
  annex:...-fermat (annex 888-1455) and annex:...-monadic-bridge (annex 1741-1789).
- Locators used: p. 28 ((S^M), (S^M_n), Thm 9, H(A), Mycielski lemma + note 10, Q_I, constituents, S_1..S_n,
  W_n); p. 29 (W_n criterion, true-formula consequence, open characterization, Thm 10, note 11
  Lowenheim/Hilbert-Ackermann p. 101, Remark, Lemma (a), Lemma (b)); pp. 29-30 (proof of (b)); p. 30
  (A^j, R(x_1..x_m), Lemma (c) and proof); p. 31 (allowable valuations, (T), Lemma (d) and proof); p. 32
  (Thm 10 conclusion, Thm 11, canonical representation, A^j_W, A^j_0, Lemma (a), Sigma, Lemma (b));
  p. 33 (induction for (b), class R for Thm 11, (c_n), allowable for I, 1o 2o, (15), convention, Lemma (d));
  p. 34 (proof of (d), Lemma (e), (16)); p. 35 (proof of Thm 11, K_I and K, non-effectiveness, Fermat
  example, note 12). p. 15 for "(with identity)".
- Decisions:
  (16) Identity. (S) has identity (p. 15) and section 6 does not remove it. With identity, Lemma (c)'s
       base case fails (x_1 = x_2) and Theorem 11 is false (proved counterexample E_k with Q_I(X) = v iff
       |X| in A, A non-recursive). Section 6 is therefore read identity-free; stated in hbwarning
       def:p03-w03-p03-042-monadic-identity with lemma thm:p03-w03-p03-042-monadic-identity. Theorem 9 holds
       in both readings. OPEN (not claimed, not proved): whether Theorem 10's conclusion holds for monadic
       formulas with identity; Mostowski's argument does not cover it.
  (17) Lemma (d) of Theorem 10 is false as printed when m_1 = 1 (counterexample (Ex)F_1 v (Ex)~F_1; the
       constant-falsity allowable valuation is unrealizable since I must be nonempty). Corrected via
       "admissible" pairs; when m_1 is infinite, cells with no true a^j get one element, and the printed
       statement holds for closed formulas. hbwarning def:p03-w03-p03-042-lemma-d-correction.
  (18) Theorems 10 and 11 are stated for all true formulas, Mostowski's proofs treat closed ones (Lemma (d)
       on R, Theorem 11 "each closed formula", p. 35). Extended to free individual variables: variables
       b_{h,l}, cells c_l(beta), and for Thm 11 pairs (gamma, D) in K_I; marked in the reader as added.
  (19) p. 32 prints N_{i_{k_1}} in Sigma; read as N_{k_1} (stated in reader).
  (20) Mostowski's double bar for cardinals kept as the chapter's single \overline (def truth-values),
       noted in Theorem 10.
  (21) Theorem 9: Q_I(X) = v iff X finite and |X| in A, taken for every I (Mostowski fixes it on denumerable
       I only). Mycielski consequence (non-recursive H(A)) by counting; no choice used.
  (22) Lemma (b) of Thm 11: proved directly from the satisfaction clause; Mostowski's induction via (a)
       checked in the same annex item.
  (23) Off-route existing treatment found (not in packet's existing list): sec:p02-w02-p02-035-monadic
       (handbook/parts/p02/definitions-interpolation-and-decidable-fragments-w02-p02-035.tex, equality-free
       monadic FOL colour-collapse decision procedure). Not cross-referenced (not on the static route);
       crosslink requested.
- Checks session 3: unit-compile ok (46 overfull; new ones in section 6 are 3-21pt paragraph/heading
  boxes); find_fused_spaces clean; check.py --tree: only bib-key Mundici1985OtherQuantifiers (own intake).
- Still owed (unchanged from session 2): Mundici sec. 1 remainder, sec. 2-4 (C001-C004); Kaufmann ch. IV;
  Lindstrom 1966 (blocked_source); Church's Axiom 0 list (blocked_source).

Session 4 (w03a block 2 rerun, 2026-10-13): guard fixes and Mundici sections 1.2-1.4.
- G14: "admitted" (body 736, 754; annex 1011) replaced by "present"/"allowed"; workflow-word scan of both
  owned tex files now empty.
- G1 (spec/research/edition-2026-authoring-batch-intake-13.json): not modified by this packet in any session;
  git shows the file last changed by lead commit 6de06cc3 ("w02ca: authored state ... route of batch 13"),
  working tree clean for it. Nothing to undo here; reported to the lead in the return.
- Source: Mundici ch. VI, 1985 Springer printing, Project Euclid scan. WebFetch of the same download URL
  this session returned empty content (twice); pages 213-217 were re-read this session from the copy
  WebFetch delivered in session 2 (tmp/agent-scratch/w03a-w03a-p03-042-b1-author/dl/mundici-ch6.pdf,
  PDF pages 3-7 rendered at 150 dpi in tmp/agent-scratch/w03a-w03a-p03-042-b2-author/m/).
- Locators used: p. 213 (Walkoe observation), p. 214 (Vaananen remark, Thm 1.2.1 and proof with the
  n-row/2-row equivalence, Remark, Thm 1.2.2 statement), pp. 214-216 (1.2.2 claims, Cor 1.2.3, Rem 1.2.4:
  mentioned only), p. 216 (Prop 1.3.1 with proof, Thm 1.3.2 with proof sketch), p. 217 (1.4 notes).
- Written: body subsection sec:p03-w03-p03-042-mundici-compare (body 1347-1584): convention
  def:...-mundici-comparison (<=, ==, (omega,omega)-compact, axiomatizable, Q_alpha), thm:...-mundici-walkoe,
  thm:...-mundici-pairing (general form = Mundici's Remark), cor thm:...-mundici-peano (Thm 1.2.1),
  example def:...-mundici-pairing-example, thm:...-mundici-not-compact (Prop 1.3.1 parts compact/axiom.),
  thm:...-mundici-pure-identity, thm:...-mundici-q-alpha (Thm 1.3.2), warning def:...-mundici-limits,
  paragraph of 1.4 attributions. Annex items for all six results (annex 1588-1899).
- Decisions:
  (24) Walkoe's observation is stated and proved for Mundici's Q_pi (Def. 1.1.1): r = 1 gives L_omega-omega
       (AC), r >= 2 gives L(Q^H) <= L(Q_pi). Walkoe's own wider notion of p.o. prefix was not read.
  (25) Thm 1.2.1 proved in the Remark's generality (any T with a first-order definable pairing bijection);
       PA case via lem:p05-pa-pair-beta (pairing graph P provably a bijection).
  (26) sigma_N for Prop 1.3.1: Q axioms + commutativity of + + (forall x) not Q_0 y (exists z)(y+z=x).
       Commutativity is added because Q alone does not prove 0+x=x, needed to show nonstandard elements
       have infinitely many "predecessors". Mundici only says "there is a sentence".
  (27) Non-axiomatizability via Tarski undefinability + representability (Mundici cites Goedel).
  (28) Readings of <=, (omega,omega)-compact, axiomatizable and Q_alpha fixed locally in an hbconvention
       (Mundici takes them from ch. II, not read).
- Still owed: Thm 1.2.2 with Claims 1-2, Cor 1.2.3, Remark 1.2.4 (need ch. II notions <=_RPC, Delta-closure,
  RPC, Loewenheim and Hanf numbers; ch. II not read); weak Beth part of Prop 1.3.1 (needs ch. II weak Beth
  definition and the Makowsky-Shelah abstract theorem); the 1.4 results are reported, not proved
  (interpolation failure, Delta/Beth failure, Walkoe/Keisler-Walkoe prefix theorem). Then Mundici sec. 2-4
  (C002-C004), Kaufmann ch. IV, Lindstrom 1966 (blocked_source), Church Axiom 0 (blocked_source).
- Checks session 4: unit-compile ok (50 overfull; new ones: annexitem header lines only, body 1522-1529
  6.7pt); find_fused_spaces clean; check.py --tree: only bib-key Mundici1985OtherQuantifiers (own intake).

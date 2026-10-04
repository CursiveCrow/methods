# w02-p02-005 (P2 10.5) research note

## Provenance

- Packet: work/waves/w02/packets/w02-p02-005.json, block 1, label_tag p02-w02-p02-005.
- Active host of the inherited translation passage: handbook/restoration/inherited-01899-01945.tex
  (read-only; byte-identical to source/formal-logic-reference.tex lines 1899-1945, checked by reading both).
  The frozen v1.0 block has no neither/nor row; nothing in the new text claims a v1.0 neither error.
- Inactive existing treatment found and not reused as a host: tab:p02-controlled-english in
  handbook/parts/p02/propositional-syntax-semantics.tex (around line 288); it is not input by parts/p02.tex.
  Its neither and not-both rows agree with the new rows.
- Barwise source: source/references/acq-r1-ACQ-2026-10-0497/schwichtenberg-1977-proof-theory-applications-cut-elimination.pdf
  (sha 256 digest 0226941f...; whole HML, 8th impression 1993, 1977 pagination). Chapter A.1 = PDF pp. 21-62 = printed pp. 5-46.
  Opened this session: OCR text of PDF 21-62 read in full; page images of printed pp. 8, 9, 10, 11, 12, 13, 14, 15
  viewed to verify the displayed formulas (1)-(10), (9)', ring and ideal axioms, the c > r sentence of 2.7,
  the "order >= N" of 2.3, N_psi of 2.8, and the algebraically-closed schema.
- Sibling treatment of the same chapter: w02-p02-039 cites Barwise1977FirstOrder ch. A.1 sec. 5.4 pp. 43-44
  (handbook/parts/p02/many-sorted-and-alternative-first-order-w02-p02-039.tex 278, 283). Same bib key and fields
  are in this packet's intake; finalizer keeps one copy.
- Other packets carrying ED26-SRC-001-001: w02-p02-003, -006, -021, -022, -029, -030, -031, -032. Their owned
  files had no Barwise mapping when this block was written.

## Decisions

- Proof routes for Barwise 2.4 and 2.5 in the annex go through the active-route theorems thm:fol-compactness and
  thm:downward-ls (plus lem:reduct-invariance). Barwise's own route (Main Lemma 4.8 via Henkin constants and
  propositional compactness 4.2) is not yet mapped; see missing work.
- Barwise leaves 2.2, 2.8 and the principal-ideal-ring claim (p. 14) without written proofs; the annex supplies full
  proofs and the body says the source gives none.
- Maximal ideal (9) <-> (9)': annex proves it directly; the source's route via the lemma "I maximal iff R/I field" is
  described, and (9)' is noted to be the field condition on R/I.
- Algebraically closed schema: qualification added that only n >= 1 instances express the property (n = 0 instance is
  false in every field). The source prints the schema without the bound.
- "Only" outside "only if": stated explicitly that the propositional guide treats "only" solely through "only if"
  (postposed or fronted); noun-phrase "only" given a first-order translation as illustration.

## Missing work for ED26-SRC-001-001 (Barwise 1977, ch. A.1, printed pp. 5-46)

Hosted in this block: sec. 2 pp. 6-17 (all displayed notions (1)-(10), 2.1-2.8 with proofs, reals remarks, rings,
ideals, fields, algebraically closed, extensionality, properties-of-theories claims recorded as attributed claims with
their referrals); sec. 3 pp. 17-22 (Defs 3.1-3.8, FV, sentence, model, elementary equivalence, axiomatizability,
substitution proviso and its example).

Not yet hosted (each needs an actual host):
1. sec. 1 Foreword p. 6: intended reader, historical attribution (Leibniz; Boole, Frege, Peano, Russell and Whitehead,
   Hilbert, Skolem, Goedel, Tarski).
2. sec. 2: the Archimedean-axiom remark about weak second-order LS (p. 12) is summarized only; the statement that LS
   holds for weak second-order logic and fails for second-order logic (p. 10), and that compactness fails for weak
   second-order logic (p. 10), are not proved. Properties-of-theories claims (p. 16: decidability of abelian groups,
   undecidability of groups, completeness of ACF_p, decidability of C, undecidability of Z) are recorded as attributed
   claims; their proofs live in chapters C.1, C.3, D.1 of the same handbook and are not supplied.
3. sec. 3: term example a^2+2a+1 (p. 21), formula examples (p. 19), the two coincidence facts (term value and
   satisfaction depend only on occurring/free variables, pp. 21-22) - stated, not proved; "isomorphic implies
   elementarily equivalent" stated, not proved; EC / EC_Delta terminology (p. 22) not recorded.
4. sec. 4 pp. 22-40 entirely: propositional formulas over prime formulas P, truth assignments into {t,f}, the truth
   table (p. 24) and the two worked truth tables (pp. 24-25), Def 4.1 tautology/consistent, listed tautologies, the
   backward method (p. 26), Thm 4.2 propositional compactness with both proofs (maximal finitely consistent sets;
   Tychonoff), map-colouring application and Tychonoff-for-2^P remark (p. 28), first-order tautology examples and
   non-examples (p. 28), Lemma 4.3 and its counterexample set (p. 29), 4.4 equality axioms, witnessing expansion L(C),
   Def 4.5 Henkin axioms I/II, Def 4.6 T_Henkin and quantifier axioms III/IV, reduct/expansion, Lemma 4.7, canonical
   structures and Eq, Main Lemma 4.8 with its proof (pp. 31-33), Barwise's proofs of 2.4 and 2.5 from 4.8 (p. 33),
   Hilbert system H (axioms, MP, generalization rules), Thm 4.9, Soundness Lemma 4.10, Lemma 4.11, proof of 4.9
   (pp. 36-37), Gentzen propositional rules (displayed rule figure p. 37; OCR lost it, page image must be read), the
   derivation example (p. 38), Thm 4.12 with proof, equality axioms/rule, quantifier rules, cut, system G and G+,
   Thm 4.13 with claims (1)-(5) (pp. 39-40), Thm 4.14 cut elimination (Gentzen; referral to ch. D.2), the exercise
   on exists y [phi(y) -> forall x phi(x)] (p. 40).
5. sec. 5 pp. 41-45: Hilbert's Thesis and its two examples, 5.1 many-sorted logic and its reduction, 5.2 M-logic and
   omega-logic (compactness fails for infinite M), 5.3 weak second-order logic via HF(M), 5.4 L_{omega1 omega}
   (partly hosted by w02-p02-039), 5.5 Q_0 and Q_1 with Keisler's axioms (1)-(4), 5.6 abstract model theory,
   5.7 Lindstrom's theorem.
6. Apparatus: footnote (Sloan/NSF support, p. 5), the References list pp. 45-46 (Barwise 1974; Chang-Keisler 1973;
   Enderton 1972; Feferman 1974; Keisler 1970; Shoenfield 1967; Smullyan 1968), referrals to chapters A.2-A.7, C.1,
   C.3, D.1, D.2 beyond those recorded in sec. 2.

## Continuation

Block 1 written items: A-032 C01 and C03 rows (body 33-139), Barwise sec. 2 and sec. 3 (body 141-472; annex 47-378).
Unit compile ok. Next block: Barwise sec. 4 (items 4 above) - propositional part 4.1-4.2 first, then Henkin
reduction 4.3-4.8 with the source-route proofs of 2.4/2.5, then H (4.9-4.11), then G/G+ (4.12-4.14, read p. 37 image
for the rule figure); then sec. 5 and apparatus. Consider whether sec. 4 belongs instead to the 20.1-20.4 packet
(w02-p02-031), which also carries ED26-SRC-001-001; lead to decide host to avoid two treatments.

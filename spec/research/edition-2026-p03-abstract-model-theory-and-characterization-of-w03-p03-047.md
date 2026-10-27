# Research note: w03a-p03-047 (P3, ch. 37, section 37.1)

Files: handbook/parts/p03/abstract-model-theory-and-characterization-of-w03-p03-047.tex (body, 871 lines),
handbook/annex/p03/abstract-model-theory-and-characterization-of-w03-p03-047.tex (annex, 541 lines),
intake bib and symbol CSV of the same slug.

## Source read in this session

SRC-049 held preview, tmp/edition-2026-catalog-src038/tail-039-068/SRC-049-pageplace-preview-2026-09-09.pdf
(sha 256 1597918d...), with the reading derivative. Physical page = printed page + 20.
Rendered and read as images: printed pp. 11, 13, 14, 18, 19 (Barwise) and pp. 27-32, 60-61 (Ebbinghaus);
the remaining Barwise pages 3-23 and Ebbinghaus pp. 25-37 were read from the reading derivative.
Correction from the image: Ebbinghaus Definition 1.2.4(i) reads "of power <= kappa" (the text extraction shows "<").
Edition: 2017 Cambridge reissue (Perspectives in Logic 8) of the 1985 volume; locators are the printed pages of that reissue.

## Existing treatments found (not all listed in the packet)

- preservation-abstract-logic.tex: def:p03-q-one, thm:p03-keisler-q-one (cited), sec:p03-lindstrom, thm:p03-lindstrom, def:p03-potential-isomorphism (listed in packet).
- abstract-model-theory-and-lindstrom.tex (Kennedy-Vaananen model-class package) - linked via sec:p03-lindstrom.
- NOT LISTED: generalized-game-and-dependence-quantification-w03-p03-044.tex treats Ebbinghaus Ch. II section 2.5 (Henkin quantifier, pp. 38-39); linked, not duplicated.
- NOT LISTED: comparison-games-and-infinitary-languages-w03-p03-041.tex treats Ebbinghaus Definition 5.2.1, Proposition 5.2.4 (for sublogics of L_omega1omega), Example 5.2.3(c) lower bound, and Barwise 1.4 compactness. def:p03-w03-p03-041-pinning is used instead of a second pin-down definition.
- NOT LISTED: propositional-languages-valuations-and-truth-functions-w02-p02-005.tex thm:p02-w02-p02-005-bw-extended-ls (L(Q0)/L_omega1omega not countably compact, L(Q1) no countable model, LS for L_omega1omega and L(Q0)); linked instead of reproving.
- NOT LISTED: w02c-p02-003 interpolation and Beth for L_omega1omega (thm:p02-w02c-p02-003-interpolation, -beth); linked.
- NOT LISTED: w03-p03-029 Vaught two-cardinal (thm:p03-w03-p03-029-theory-form) cited Barwise 1.5; linked.
- Note: first-order-completeness.tex labels (thm:p02-fol-compactness, thm:p02-downward-ls, thm:p02-upward-ls) are off the static route (check reports dangling refs); on-route equivalents used: thm:p02-w02-p02-005-bw-compactness, thm:p02-w02-p02-005-bw-ls, thm:p02-w02-p02-033-upward-ls-inclusion.

## Bib keys

Barwise1985BackgroundAims (same entry as intake of w03-p03-041) and Ebbinghaus1985ExtendedLogics (same entry as intake of w03-p03-044) duplicated field-for-field in this unit's intake so that the keys resolve; finalizer should dedupe.

## Continuation

Run of 2026-10-12 (block 1 continuation). Read in this session from the held PDF (rendered pp. 34-36, physical 54-56) and the reading derivative (Barwise pp. 8-9; Ebbinghaus pp. 33-37).

Added (body lines 256-312 and 946-1193; annex lines 119-230 and 638-979):
- Barwise 1.5: thm q0-not-re (L(Q0) validity not r.e.; reduction of TA via chi_N, cites p02-040 clause 3); thm q1-mostowski-facts (L(Q1) validity r.e. via Keisler calculus, a content bridge replacing Vaught's two-cardinal route; L(Q1) does not define (omega,<), so does not include L(Q0); countably generated groups / uncountable structures). Fuhrken and Keisler linked to the proved p02 w02c theorems.
- Ebbinghaus 2.1: thm sol-ch (CH sentence, full proof); thm weak-sol (finiteness, L(Q0) translation, torsion groups, N characterization, not aleph0-compact, not r.e. for validity, translation into L_omega1omega and LS property).
- Ebbinghaus 2.2 Examples 1-3: thm q1-ls-consequence (LS down to aleph1 for <= aleph1 sentences; r.e. for consequence via Keisler); example keisler-entailment ((*) proved); thm q1-interpolants (Q_1^2 and pos interpolants); thm set-quantifier-failures (omega1 and omega characterizations, aleph0-compactness failure); thm pos-monotone (***), with polarity hypothesis made explicit; warning pos-polarity (counterexample without it).

Still owed, in the components' own terms:
- 0001-C001: L(Q0) definability of torsion groups, finitely generated groups, finite-dimensional vector spaces (no proof written; source gives none); Hanf's large-cardinal requirement for compact L_kappa lambda; Mostowski 1968 (finite syntax + definable finiteness -> Beth fails); Moschovakis/Svenonius; Keisler probability logic incomparability; Shelah's four second-order quantifiers; Rabin monadic tree; Erdos-Gillman-Henriksen and Dickmann partial-isomorphism form. Vaught's own two-cardinal derivation (only the Keisler-calculus bridge is proved).
- 0001-C002: as listed in the previous continuation (Robinson failure for L_omega1omega; Robinson <=> compactness + Craig; Delta(L) existence and Delta(L(Q0)) = hyperarithmetic fragment; boundedness values; Hanf number formulas; Shelah decomposition; large cardinals / Vopenka; interpolation failures for L(Q0), L(Q1)).
- 0002-C002: SOL regularity (2.1.1 "obviously regular"); bridge from finite-relation L^w2 to Barwise's HF formulation for Beth/interpolation failure (2.1.2); regularity criterion Theorem III.4.1 for monotone unary Q; Fuhrken/Vaught original proofs (Keisler route proved instead); omitting types; preservation; Keisler no-interpolant claim for (*) (Ebbinghaus refers to 4.2.7); Friedman Beth failure; Example 2 Magidor-Malitz compactness under V=L/diamond, Shelah consistency, Suslin trees, Badger, Garavaglia-Shelah; Example 3 Stavi (neg characterizes omega1), pos aleph0-compact and r.e. for consequence; Example 4 stationary logic and 2.3-2.6 incl. Theorem 2.6.1, Corollary 2.6.2 (pp. 36-41 not yet worked).
- 0002-C003..C007: not started (pp. 41-73). C005 overlaps w03-p03-041 (link). C007: printed pp. 73-76 reported outside the held preview; verify page extent before writing.

Run of 2026-10-12 (block 2). Read in this session: reading derivative Barwise pp. 8-13 and 22-23, Ebbinghaus pp. 40-45; rendered images of printed pp. 42-44 (physical 62-64). Image correction: p. 43 reads L_{infty G} <=_equiv L_{infty omega} and L_{infty omega} < L_{infty G} (extraction garbled); chains on p. 43 taken from the image.

Guard fixes: reworded six copied-prose runs (Barwise p. 4 logic definition, p. 21 Vopenka, Ebbinghaus pp. 31-32 regular logic, 1.2.4(i), (viii), 1.2.5(i)); 'admitted' -> 'permitted' in the omega-logic remark; the sha 256 spelling in this note.

Added:
- Body 355-398 / annex 214-317: thm q0-beth-failure (E = evens implicitly defined over theta, not explicitly definable in L(Q0); interpolation fails for L(Q0) via craig-beth). Proof: Q0 eliminated over (omega,<), proper elementary extension (thm:p02-w02-p02-033-upward-ls-inclusion), shift automorphism on the nonstandard part. This is the L(Q0) instance of Mostowski's 1968 result, not the general theorem.
- Body 637-660: Barwise Sec. 3 limitations (omission of work outside the abstract framework; static-object shortcoming and human languages).
- Body 1243-1417 / annex 1093-1206: Ebbinghaus Sec. 3.1: Def. 3.1.1 (def ec-pc-rpc), Remarks 3.1.2 (PC in RPC and infinite sets PC not EC proved in thm pc-basic; RPC one/many-sorted equivalence and the two strictness claims reported only), Prop. 3.1.3 linked to thm craig-separation part 1 (one-sorted case only), Defs. 3.1.4-3.1.6 (def strength), basic facts (thm strength-basic), Prop. 3.1.9 (thm rpc-descent, many-sorted reading), reduction scheme (method).

Still owed, in the components' own terms:
- 0001-C001: general Mostowski theorem (finitary syntax + definable finiteness) and its weak second-order and omega-logic instances; L(Q0) definability of torsion groups, finitely generated groups, finite-dimensional vector spaces (no source proof; correctness of the L(Q0) claims not verified - weak second-order versions exist); Hanf's large-cardinal requirement; Moschovakis/Svenonius; Vaught's own two-cardinal route; Keisler probability logic incomparability; Rabin and Shelah (Sec. 1.7); Erdos-Gillman-Henriksen and partial-isomorphism form.
- 0001-C002: everything listed before except interpolation failure for L(Q0), now proved. Still: Robinson failure for L_omega1omega; Robinson iff compactness + interpolation; L(Q1) interpolation failure; Delta(L) existence, strictness, Delta(L(Q0)) = hyperarithmetic fragment; boundedness values; LS + boundedness by omega characterization; h(L) = beth values; Sec. 2.7 large cardinals / Vopenka.
- 0002-C001: Beth property for function symbols and constants (definition and proof from interpolation) not yet written.
- 0002-C002: as in block 1 list (Example 4 aa, 2.3 Rescher/Hartig, 2.4 cofinality, 2.6 L(K) with Thm 2.6.1 and Cor 2.6.2, 2.7, and the reported-only claims).
- 0002-C003: Prop. 3.1.3 many-sorted (RPC) case; Remarks 3.1.2 one/many-sorted RPC equivalence and strictness claims; the p. 43 comparison chains (reported, not proved); Prop. 3.1.7 and Cor. 3.1.8 (need Thm 2.6.1); Sec. 3.2 (Thms 3.2.2, 3.2.3, Lemma 3.2.4, pp. 45-48) not read yet; Prop. 3.1.9 for the one-sorted relativized reading.
- 0002-C004..C007: not started.

Run of 2026-10-13 (block 2, second session). Read in this session: reading derivative Barwise pp. 8-10, 16-17, 22-23 and Ebbinghaus pp. 33-34, 68-71; rendered image of printed p. 69 (physical 89) for the notation of Counterexamples 7.1.3(a) (K_{aleph_0} subscript, K^{aleph_1} superscript). No policy record in blockers.jsonl governs SRC-049.

Added:
- Body ~632-680 (Barwise Sec. 3): unified framework claim, Austin speech-act and side-effects point, inference as activity, positive programme (logic of concepts mathematicians use, applications, new concepts) and Barwise's uncertainty about which particulars last.
- Body 301-345 / annex 214-300: thm q0-vector-spaces. Finite field: f.d. iff finite iff not Q0 x (x=x). Over Q (one-sorted tau_Q): Q0 eliminated over nonzero Q-vector spaces by QE, T complete, Q and Q^(omega) are L(Q0)-equivalent, so Barwise's f.d. example FAILS over Q in that vocabulary (proved limitation). Torsion and finitely generated groups: no L(Q0) definition or undefinability proof (open; the weak second-order torsion definition is in thm weak-sol).
- Body ~420-492 / annex 434-~600: def self-satisfaction (finite syntax coded in omega + implicitly defined satisfaction over N) and thm mostowski-general: part 1 diagonal argument (U implicitly but not explicitly definable; Beth and interpolation fail); part 2 L(Q0) and L^w2 satisfy the definition (coding, sigma, uniqueness by induction). Uses thm:p04-ce-sigma-one for Delta^0_1 definability of decidable relations. omega-logic not covered (renaming failure, thm omega-logic-renaming).
- Body 1546-1632 / annex 1480-1587: sec. robinson: Def 7.1.1 (interpolation for another logic), Examples 7.1.2 reported with link to p02 interpolation, Def 7.1.4 Robinson property, Prop 7.1.5 with proof (hypotheses: small, compact, atom + Boolean + particularization), thm infinite-sets (L_infty-omega equivalence of infinite sets; 7.1.3(a) proved; Robinson fails for L_omega1omega, Barwise p. 16).

Still owed, in the components' own terms:
- 0001-C001: L(Q0)-definability of torsion groups and finitely generated groups (neither definition nor refutation); omega-logic instance of Mostowski; Hanf large-cardinal requirement for compact L_kappa lambda; Moschovakis/Svenonius; Vaught's own route; Keisler probability logic; Rabin, Shelah (Sec. 1.7); Erdos-Gillman-Henriksen / partial-isomorphism form.
- 0001-C002: Robinson => compactness for small occurrence number (Ch. XIX, not held) hence the full "Robinson iff compactness + interpolation"; Delta-closure strictly weaker than interpolation and existence of Delta(L); Delta(L(Q0)) = hyperarithmetic fragment; L(Q1) interpolation failure; boundedness values; LS + boundedness by omega characterization of FO; Hanf numbers; Sec. 2.7.
- 0002-C001: verification that the basic logics are logics with relativization (pp. 29-30), constants remark (p. 30), unification of domains (p. 25), Historical Remarks (p. 32); Beth for function symbols.
- 0002-C002: as in earlier list (Example 4 aa, 2.3, 2.4, 2.6 Thm 2.6.1 / Cor 2.6.2, 2.7; Keisler no-interpolant; monotone-Q regularity; L(pos) aleph0-compactness and r.e. consequence). L^w2 Beth/interpolation failure for the finite-relation formulation now closed via thm mostowski-general part 2 (body weak-SOL paragraph).
- 0002-C003: Prop 3.1.7, Cor 3.1.8, Thm 3.1.10, Remarks 3.1.2 claims, p. 43 chains, Sec. 3.2.
- 0002-C004: not started (pp. 48-59).
- 0002-C005: not started (pp. 58-64); 5.2.1, 5.2.4, 5.2.3(c) in w03-p03-041.
- 0002-C006: not started (pp. 64-68).
- 0002-C007: Def 7.1.1, 7.1.4, Prop 7.1.5, 7.1.3(a) written; 7.1.2 reported; 7.1.3(b)-(d), Def 7.2.1, 7.2.3, 7.2.2, Thm 7.2.4, Prop 7.2.5 not written; pp. 73-76 not in the held preview.

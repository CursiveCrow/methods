# w02ca-p02-003 (P2 10.1, 10.2, 10.5, 10.6) research note

## Provenance

- Packet: work/waves/w02ca/packets/w02ca-p02-003.json, block 1, label_tag p02-w02c-p02-003.
- Gaps addressed (ED26-SRC-001-001-DEVELOPMENT, duty MP-0 and the reported-claims list):
  (a) Barwise 5.7 for general languages (function, relation, constant symbols, no size restriction);
  (b) the p. 16 and pp. 43-45 claims recorded in the w02-p02-005 host as reported claims.
- Held file opened in this session: source/references/acq-r1-ACQ-2026-10-0497/schwichtenberg-1977-proof-theory-applications-cut-elimination.pdf
  (whole-book scan of the Handbook of Mathematical Logic, 1977 pagination; listed in held-sources.json under
  Schwichtenberg1977). Text layer read for PDF pp. 31-62 (Barwise ch. A.1, printed p = PDF p - 16), PDF pp. 9-16
  (contents), PDF pp. 249-275 (Makkai ch. A.7, printed pp. 233-259).
  Locators used and seen: Barwise ch. A.1 p. 16 (properties of theories), p. 17 (languages, no size restriction,
  referrals A.2-A.4), p. 42 (5.1, 5.2 omega-logic), p. 43 (5.3 HF, admissibility remark, A.7 3.1 and 2.16),
  p. 44 (5.4 infinitary rule, translation, Beth; 5.5 L(Q_0) and L(Q)), p. 45 (Keisler axioms (2)-(4), 5.6, 5.7).
  Makkai ch. A.7: p. 238 (2.1 Delta_0 formulas), p. 239 (2.3 KPU, 2.4 admissible set), p. 243 (2.16, 2.17
  recursion), p. 244 (3.1 H_U(kappa) admissible; remark that HF sets form an admissible set).
- Session 2 (same held whole-book scan): Barwise ch. A.1 p. 16 (PDF 32: Goedel's Second Incompleteness Theorem
  "tells us how to go about finding" a true sentence not a consequence of an effective true T) and p. 44 (PDF 60:
  implicit-not-explicit in WSO; "cannot happen in first-order logic or L_omega1omega, by Beth's Theorem").
  Makkai ch. A.7 read in this session: p. 236 (S1, Beth true for single sentences of L_omega1omega, Lopez-Escobar
  1965), pp. 249-252 (S4: 4.1 Hintikka sets, 4.2 model of a Hintikka set with induction steps omitted, fragments,
  4.3 model existence with proof only "similar to 4.2", 4.4 Sigma-compactness), p. 256 (5.3 game-form theorem),
  p. 271 (8.1 Vaught covering theorem, proof via 7.3, 7.6, 5.4(iv)), p. 272 (8.2 Strong Craig-Lopez-Escobar
  interpolation; (i) for L_omega1omega), p. 274 (remarks on Lopez-Escobar's Gentzen route and consistency-property
  route (Keisler 1971); 8.6 Beth's theorem with proof from interpolation).
- Session 3 (same held whole-book scan): Barwise ch. A.1 pp. 8-9 (PDF 24-25: (6), (7), (8), term nx), p. 12 (PDF 28:
  n1, Archimedean axiom), p. 15 (PDF 31: (10) and (10)_p), p. 43 (PDF 59: recursion remark, section 2 sentences "weak
  second-order in this precise sense"); Makkai ch. A.7 p. 249 (n.n.f.), p. 250 (4.1, 4.2), p. 251 (4.3, 4.4), p. 252,
  p. 272 (8.2), p. 274 (consistency-property route, Keisler 1971; 8.6).
- Davis 1973 (tmp/davis-h10-1973.pdf, listed in held-sources.json under Davis1973): PDF p. 3 = printed p. 234,
  Lagrange's four-square theorem cited there as known.
- Session 11 (r6, block 1): same held whole-book scan (Schwichtenberg1977 entry), text layer: Barwise ch. A.1 PDF 50-53
  (pp. 34-37: system H, 4.9, 4.10, 4.11 (i)-(iv) with proofs of (iii), (iv), proof of 4.9, and the p. 37 remark that
  the proof used only 4.11 (iii), (iv), with the Smullyan referral) and PDF 60 (p. 44: completeness for countable
  L_omega1omega theories needs an infinitary rule; no rule named). Makkai ch. A.7 PDF 249-280 text layer, p. 236
  (Gentzen-type infinitary system; completeness attributed to Karp 1964 and Lopez-Escobar 1965) and pp. 262-263
  (6.2 abstract completeness, not the full Barwise completeness theorem). No new locator beyond these.
  Online attempt: Lopez-Escobar 1965, Fund. Math. 57, IMPAN page lists a CC-BY download that redirects to
  matwbn.icm.edu.pl/ksiazki/fm/fm57/fm57119.pdf; that URL returned HTTP 403, so nothing was read and nothing is
  attributed to it. Karp 1964 not held.
- Not held: Barwise 1974 "Axioms for abstract model theory" (ACQ-2026-10-0032); Keisler 1970 (Keisler1970 has no
  held-sources entry); Hodges 2001 (ACQ-2026-10-0433); Ebbinghaus-Flum-Thomas (cited by the host for the
  relational notion; no held entry).

## Existing treatment found (A9)

- Relational 5.7: thm:p02-w02b-p02-001-barwise-lindstrom (w02b-p02-001 body 803-816, annex 1007-1045), extended,
  not duplicated; def:p02-w02b-p02-001-lindstrom-limit item 2 now points to the new theorem.
- ACF_p: thm:p03-acfp-qe (cited Marker2002), thm:p03-acfp-uncountable-categorical (cited Steinitz1910) in
  handbook/parts/p03/qe-categoricity-games.tex; thm:p03-morley-field-example (handbook/parts/p03/presentations/
  n-a-006-01.tex). Used as the cited categoricity input, not re-proved. Not in the packet's existing list.
- TA not c.e.: thm:p02-w02b-p02-034-ta-not-ce and thm:p02-w02b-p02-034-ce-sigma-one; Tarski undefinability
  thm:tarski-undefinability (restoration inherited-09925-09992). Used, not in the packet's existing list.
- Interpretation transfer thm:p05-interpretation-transfer (cited TMR1953). Referenced in the boundary.
- Keisler L(Q_1) compactness: thm:p03-keisler-q-one (cited Keisler1970).
- Session 2: first-order Beth thm:p03-beth-definability (proved=annex:p3.abstract.2, via Robinson separation) and
  thm:p02-beth-definability / thm:p07-beth-definability (cited Beth1953); no L_omega1omega interpolation or Beth
  anywhere in the handbook. G2 on the live route is thm:godel-second (restoration inherited-09877-09924) with
  sec:second-incompleteness-01 (D1-D3; proved for the selected Prv^19 formula of PA), def:fixed-proof-predicate,
  lem:p05-numeralwise-d1 (D1 for the certified predicate), def:formal-consistency-sentence, thm:representability
  (cited Shoenfield1967). handbook/parts/p05/provability-truth.tex and diagonalization.tex (thm:p05-goedel-second,
  def:p05-proof-predicate, ...) are NOT on the live route (check.py reports their labels as dangling); not used.
- No existing proof found for: Lindstrom with function symbols; Los-Vaught test; WSO -> L_omega1omega;
  HF(M) admissibility; Szmielew; undecidability of groups; Th(Z) undecidable.

## Decisions

- The general-language reading (def:p02-w02c-p02-003-general-reading) adds an occurrence condition and a
  replacement condition to the relational notion; recorded in reader as def:p02-w02c-p02-003-general-limit.
  Whether 5.7 holds without the replacement condition is open; Barwise 1974 not held, so not compared.
- L* atomic formulas read as L-atomic, t in a, a in b, a = b (def:p02-w02c-p02-003-wso-reading); Barwise does
  not list them.
- Decidability in thm acf is in Barwise's informal sense; in thm integers it is formal (definability in N),
  under an explicit hypothesis on the coding of ring-language sentences.
- No new bib keys (Makkai1977, Davis1973, Keisler1970, Steinitz1910 in handbook.bib).
- Symbol overlap: \mathrm{Nat} vs P10 \operatorname{Nat}(F,G) (different glyph/role; noted in intake).

## Missing work (specific records)

1. Beth failure for WSO (Barwise p. 44): written in session 4 (thm wso-n, hf-arith, truth-clauses, wso-beth-failure).
2. L(Q_0) essentially equivalent to omega-logic and WSO (p. 44): written in session 4 under the reading
   def:p02-w02c-p02-003-rpc (thm q0-equivalence). The reading of "essentially equivalent" is ours.
3. Keisler's Completeness and Compactness for L(Q) (pp. 44-45): written in session 9 from the held Keisler 1970
   (sec:p02-w02c-p02-003-keisler); beyond-boundary item removed.
4. Szmielew decidability of abelian groups; undecidability of groups (p. 16): not written
   (def:p02-w02c-p02-003-theories-boundary items 1-2).
5. Session 5: written (thm steinitz, fta, lagrange, lemma ring-coding). Earlier record: inputs cited without handbook proof: Steinitz classification (via thm:p03-acfp-uncountable-categorical);
   fundamental theorem of algebra; existence of an algebraically closed field of characteristic 0; Lagrange's
   four-square theorem (Davis p. 234); a ring-language coding with the definability property of thm integers
   part 2 (boundary item 3).
6. Session 3: recursion along omega in HF(M) written (thm hf-recursion) and the section 2 sentences (6), (7), (8), (10)
   written as L*-sentences with proofs (thm wso-sentences). Makkai's Sigma-recursion on membership (2.16-2.17): written in session 5 for HF(M) (thm hf-sigma-recursion).
7. 5.7 exact hypotheses per Barwise 1974: session 6, Barwise 1974 held (ACQ-2026-10-0032); written as thm b74-lindstrom (Corollary 3.4) and cor b74-five-seven, with comparison warning b74-comparison.
8. SRC-007-001 (Hodges 2001): blocked_source ACQ-2026-10-0433.
9. Session 3: interpolation for L_omega1omega now written with annex proofs (n.n.f., Hintikka model, consistency property,
   model existence, interpolation for relational then general languages); earlier record follows. Beth for L_omega1omega
   (Barwise p. 44): thm:p02-w02c-p02-003-beth proved in annex from the interpolation
   theorem thm:p02-w02c-p02-003-interpolation (Makkai 8.2(i), p. 272). Missing: a proof of the interpolation theorem
   (model existence for countable fragments, Makkai 4.3 proof only "similar to 4.2"; interpolant construction; or
   Makkai's route via 5.3 and 8.1 with 7.3, 7.6, 5.4(iv)). Beth for an uncountable set of L_omega1omega sentences not
   treated (Makkai p. 236 states single sentences). Recorded in beyond-boundary item 4.
10. Barwise p. 16 G2 claim: session 10 made thm:p02-w02c-p02-003-integers-second unconditional: T c.e. (formal reading of
   Barwise's effective list), explicit p.r. enumeration En^sharp of T^sharp (thm sharp-enumeration), selected formula
   Prv^sharp (def sharp-formula: chi_19 with axiom factor sg(Ax_19 + Cr), Cr the Craig padded axiom set) with meaning
   and D1-D3 proved (thm sharp-provability). Remaining: the step partial recursive => Turing computable is the cited
   thm:p04-tm-partial-recursive (Kleene 1952, P4-owned) (theories-boundary item 3). D2/D3 for an arbitrary
   representative of def:fixed-proof-predicate are not provable in general (thm arbitrary-representative).
11. Session 11: Barwise p. 44 completeness with an infinitary rule: written for the handbook calculus H_infinity
    (def hinf; thm infinitary-completeness), since Barwise names no rule and the Karp / Lopez-Escobar systems are
    not held. Barwise p. 37 replacement claim: written as H-circ (def system-h-circ, thm h-circ-completeness) with the
    proviso y = v or (y not free in phi(v) and substitutable); open: completeness with the narrower 4.11 proviso
    (y not occurring in phi(v)), which needs an alphabetic-variant lemma not written (warning h-circ-proviso).
    Session 12: that open item is settled negatively for Barwise's p. 34 convention (unrenamed quantifier axioms):
    thm h-flat (sigma = not exists x exists x not x=x is not provable). Still open: the same system with instances
    of schema (3) formed after renaming bound variables (warning h-flat-limit).

## Continuation

Session 1 (w02ca block 1):
- Body handbook/parts/p02/propositional-languages-valuations-and-truth-functions-w02c-p02-003.tex: section
  sec:p02-w02c-p02-003-general-lindstrom with subsections functions / beyond / theories.
- Annex handbook/annex/p02/propositional-languages-valuations-and-truth-functions-w02c-p02-003.tex: annexitems
  translations, general-lindstrom, hf, infinitary-rule, wso-translation, los-vaught, acf, integers.
- Host edits: w02b-p02-001 body def lindstrom-limit item 2; w02-p02-005 body (p. 16 paragraph, 5.3 paragraph,
  5.4-5.5 claims paragraph, Keisler sentence) now cross-reference the new results and boundaries.
- Checks: unit-compile ok (3 small overfull boxes from long annex headings / tagline); fused-space check clean.
Next: items 1-6 of Missing work; insertion of the new files into the drivers (lead).

Session 2 (w02ca block 1, continuation after usage limit):
- Body: after thm wso-translation, paragraph + thm interpolation (cited=Makkai1977), thm beth (proved), example
  beth-example, remark that WSO implicit definitions become L_omega1omega implicit definitions via wso-translation;
  beyond-boundary item 4; after thm integers, paragraph + thm integers-second + paragraph; theories-boundary item 4;
  purpose/conclusions, relationships, sources updated.
- Annex: annexitems beth (before los-vaught) and integers-second (end).
- Host w02-p02-005 body: p. 16 paragraph (G2 sentence; cref integers-second); claims paragraph after
  thm bw-extended-ls (cref beth, interpolation).
- Symbol intake: rho-renaming/B_rho, chi^pi, chi[x/a], phi(P_i), T^+, T^sharp.
- Checks: unit-compile ok (3 overfull, pre-existing); check.py --tree: no finding in owned files; fused-space clean.
Next: items 1-6, 9 (interpolation proof), 10 (D2/D3 for T#) of Missing work; driver insertion (lead).

Session 3 (w02ca block 2, continuation after usage limit):
- Guard G1: spec/research/...-w02-p02-002.md shows no diff vs HEAD; not touched.
- Body: thm hf-recursion and thm wso-sentences (with Emp, Succ, Rec, Mul, Add, Times, Prime, Pos, (6)*-(10)*) replace the
  note on Makkai 2.16-2.17; interpolation route (def hintikka, lemma nnf, lemma hintikka-model, def consistency,
  thm model-existence, thm interpolation now proved=annex for general languages); thm wso-n (step (a)); beyond-boundary
  item 1 narrowed to steps (b), (c), item 4 removed; chi^- and translations part 1 extended to L_omega1omega; sources.
- Annex: annexitems hf-recursion, wso-sentences, nnf, hintikka-model, mex, interpolation, wso-n.
- Host w02-p02-005 body: paragraph after def bw-weak-so crefs hf-recursion and wso-sentences.
- Symbol intake: chi^+/chi^ominus, chi(c/x), S, C(Delta), theta-hat, Fn, Emp/Succ, Rec, Val*, Mul/Add/Times/Prime/Pos,
  (6)*-(10)*, alpha_N.
- Checks: unit-compile ok (7 small overfull); fused-space clean; check.py --tree: nothing in owned files.
Next: WSO Beth failure steps (b), (c); FTA and existence of ACF_0; Lagrange four-square; ring coding with the definability
property; D2/D3 for Prov_{T#} and a formal enumeration of T#; driver insertion (lead).

Session 4 (w02ca block 1, r4 continuation):
- Beth failure for WSO (Barwise p. 44), steps (b), (c), (d) written: body def hf-code (hc, chi_in, Odd, translation
  theta^ar), thm hf-arith (hc bijection, membership test primitive recursive, translation correct, definability
  transfer), def truth-clauses (Snt, sb, tv, arg_0/1, TC(T), alpha_TA), lemma truth-clauses (TA unique solution over N),
  thm wso-beth-failure (implicit definition, no explicit L* definition, via thm:tarski-undefinability). Annex items
  hf-arith, truth-clauses, wso-beth-failure. Inputs used from the live route: def:p05-pa-pr-graph,
  thm:p02-w02b-p02-034-pr-graph, sec:arithmetic-coding-04 (tree coding, numeral substitution, course-of-values),
  thm:fol-substitution, lem:fol-coincidence, lem:substitution-fv, lem:substitution-complexity.
- beyond-boundary item 1 removed (now items: L(Q_0) equivalence; Keisler L(Q)).
- Host w02-p02-005 body p. 44 claims paragraph updated (interpolation proved; cref wso-beth-failure).
- Symbol intake: pty, hc, chi_in, Odd, theta^ar, arg_0/1, Snt/sb/tv, TC/beta_k, alpha_TA, [f(r)=r]; repaired the
  malformed varphi^{k,bar h} row (quoting).
- L(Q_0) essential equivalence (Barwise p. 44) written: body convention def:p02-w02c-p02-003-rpc (RPC classes over the
  three logics; omega-logic read in the one-sorted form (M u N, M, N, ...) of def bw-many-sorted with number sort Nn and
  operations 0,S,+,x of N, a reading recorded in the convention since Barwise names no operations; "essentially
  equivalent" read as equality of RPC classes, since Barwise gives no precise sense) and thm q0-equivalence (1: sentence
  translation L(Q_0) -> L*; 2: L* -> RPC L(Q_0) via first-order axioms H1-H6 for HF(M) with Q_0 for finiteness of sets
  and of rank predecessors; 3: L(Q_0) -> RPC omega-logic via witness relations/functions (AC); 4: omega -> RPC WSO via
  hf-recursion and (M2), (M3)). Annex item q0-equivalence. beyond-boundary now has only the Keisler L(Q) item.
- Host w02-p02-005 claims paragraph crefs q0-equivalence and def rpc.
- Checks: unit-compile ok (15 small overfull, max 11.3pt); fused-space clean on owned body/annex and host;
  check.py --tree: no finding in owned files.
Next (still owed, in order): (3) Szmielew decidability of abelian groups and undecidability of groups; (4) Steinitz
classification, fundamental theorem of algebra, existence of ACF_0, Lagrange four-square theorem, ring-language coding
with the definability property of thm integers part 2; (5) D2/D3 for Prov_{T#}, representability theorem, Turing-machine
enumeration of T#; Keisler L(Q) (blocked_source Keisler 1970); Barwise 1974 (blocked_source); driver insertion (lead).

Session 5 (w02ca block 2, r4 continuation after usage limit):
- Held file opened this session: the HML whole-book scan (Schwichtenberg1977 entry). Read: contents (PDF 9-16; C.1 Enderton,
  C.3 Rabin, D.1 Smorynski); Rabin ch. C.3 printed pp. 595-629 text layer (PDF 600-650): p. 608 Theorem 4 (Vaught test),
  p. 609 (2.2 ACF; Steinitz structure theorem used without proof), p. 611 Theorem 7 (Szmielew, stated without proof);
  Davis ch. C.2 p. 585 (four-square remark; not cited); Makkai ch. A.7 pp. 238-243 (2.1, 2.5 Sigma formulas p. 239,
  2.8 Sigma_A p. 240, TC p. 242, 2.15-2.17 p. 243).
- New bib key Rabin1977Decidable (intake bib). No page range given (end page not verified).
- Written (body + annex): thm hf-sigma-recursion (Makkai 2.16-2.17 for A = M u HF(M): TC exists and is finite; unique F;
  Delta_0 auxiliaries Pr, Ap, Fun, Tr, Cl, Rs; Phi_gamma defines F; Sigma if gamma Sigma; one-sorted -> L* translation);
  lemma simple-extension; thm steinitz (transcendence bases, cardinality, isomorphism; kappa-categoricity of ACF_p for
  uncountable kappa); thm fta (C algebraically closed, d'Alembert-Argand route via extreme value theorem and polar k-th
  roots); thm acf now unconditional (parts 2-3 hypotheses removed; uses steinitz and fta, no longer the cited P3
  categoricity theorem); def ring-coding (phi-circ coding, fixed D(x_i) with bound x_{i+1..i+4}, translation chi^Z);
  thm lagrange (Euler identity, descent); lemma ring-coding (tr primitive recursive by course of values; relation defined by
  graph formula of thm:p02-w02b-p02-034-pr-graph); thm integers now without the Lagrange and coding hypotheses;
  thm integers-second without the Lagrange hypothesis. Boundary item 3 (Steinitz/FTA/ACF_0/Lagrange/coding) removed;
  item 1 now cites Rabin p. 611.
- Host w02-p02-005 body (p. 16 paragraph, last sentence) reworded to the remaining boundary items (CRLF preserved).
- Symbol intake: TC(a) (overlap with TC(T) noted), Pr/Ap/Fun/Tr/Cl/Rs, exists^f, F restricted to TC, Phi_gamma, phi^s,
  K[a], P(X), q^sigma, phi-circ, code', tr, d; D(x_i) row updated.
- Checks: unit-compile ok (21 overfull, max 12.5pt); fused-space clean; check.py --tree: only bib-key Rabin1977Decidable
  (own intake) in owned files.
Next (still owed): (a) Szmielew's theorem (Rabin states it without proof; full proof from elementary mathematics not
written); (b) undecidability of groups; (e) D2/D3 for Prov_{T#} and a Turing-machine enumeration of T#;
thm:representability (cited, owned outside the packet); Keisler L(Q) and Barwise 1974 (blocked_source); driver insertion.

Session 6 (w02ca r5, block 1):
- Held file opened this session: source/references/acq-r1-ACQ-2026-10-0032/ACQ-2026-10-0032.pdf (Barwise, "Axioms for
  abstract model theory", Ann. Math. Logic 7 (1974) 221-265; printed p = PDF p + 220). Text layer read in full (PDF 1-45).
  Locators used: Part I §1 p. 222 (L_omega omega), §3 p. 228 (languages with V, partial structures, no nonemptiness
  stated), §4 4.1-4.3 pp. 229-230 (k-term interpretations, C_inf, isomorphisms), §5 p. 231 and 5.1-5.4 pp. 231-232
  (pull-backs, invertibility, relativization, indexed union, identification), §6 6.2 pp. 233-234 (category of
  languages, "tentative"), §7 pp. 234-235 (Occurrence, Isomorphism, Translation axioms), §8 p. 237 (atomic
  sentences), §9 9.1 p. 238, 9.3 p. 239, 9.7 p. 241, 9.9-9.10 p. 242 (conj/neg; 9.10 "well known"), remark pp. 243-244
  on (not phi)^alpha vs not(phi^alpha), §10 p. 243 (proofs referred to survey [4]); Part II §1 p. 249 (1.2), §2
  p. 254 (finite occurrence standing assumption), p. 255 (Lowenheim property, 2.2), §3 3.1 p. 257, 3.2 p. 257,
  3.4 p. 259 (Lindstrom: Lowenheim + (a) upward LS or (b) countable compactness => L* equiv L_omega omega; remark on
  Lindstrom's notion and finite models), §4 4.1 p. 260 (Delta(L_w) = Delta(L(Q_0)) = L_HYP), pp. 260-262 (proof
  inputs: [11] Makowsky-Shelah-Stavi, Barwise [1]/[3] interpolation, facts (1)-(3) from the forthcoming book),
  §5 p. 264 (P5).
- Barwise 1977 (held whole-book scan, Schwichtenberg1977 entry) re-read this session: PDF 25 (p. 9: referral to 5.3,
  A.2, A.7 for infinitary formulas), PDF 26 (p. 10: 2.4, 2.5), PDF 30 (p. 14: referral to A.3, A.4 for first-order
  equivalents), PDF 33-34 (pp. 17-18: languages, 3.1, small set-theoretic model remark), PDF 56 (p. 40: historical
  note on cut-elimination, 4.14), PDF 60-61 (pp. 44-45: 5.4, 5.5 connectives from v and not, 5.6, 5.7).
- Written (body): sec:p02-w02c-p02-003-b74 (def b74-languages, def b74-logic, thm b74-lindstrom, cor b74-five-seven,
  warning b74-comparison, example b74-example); sec:p02-w02c-p02-003-or-not (thm or-not, thm small-model, warning
  small-model-limit); general-limit warning rewritten (comparison now made; open question restricted to logics meeting
  the general reading without Barwise's translation axiom); beyond-boundary item 2 (L_A claim: Barwise 1974 4.1 and the
  exact missing inputs); intro, relationships, sources updated.
- Written (annex): annexitems b74-lindstrom (Steps 1-8: axiom consequences; FO inside L*; rank types ~_m of relational
  images with defining formulas; back-and-forth families preserve phi via Lowenheim; bounded rank gives psi incl. empty
  structure; coding sentence Theta; (b) via chain sentences eta_k; (a) via indexed union Xi with only countable models),
  b74-five-seven, or-not, small-model.
- Host edits: w02-p02-005 body (CRLF on disk; HEAD is LF; kept CRLF): p. 18 remark crefs small-model; p. 44 connectives
  crefs or-not; L_A claim crefs beyond-boundary item 2; def bw-abstract-logic crefs b74-logic; 5.7 paragraph crefs
  b74-five-seven/b74-lindstrom; attributions add the p. 40 historical note; referral list adds p. 9 (5.3, A.2, A.7) and
  p. 14 (A.3, A.4). w02b-p02-001 body (CRLF): lindstrom-limit items 1 and 2 cref the b74 results.
- Decisions: Barwise 1974 structures read as allowing an empty universe (the text states no nonemptiness); theorem
  covers the empty structure, so nothing depends on it. Existential quantifier clause 9.7 read with c added to the
  language if absent. "Reasonable sense" (p. 18) read as soundness of the ND calculus; class-sized case recorded as not
  established (warning small-model-limit). Symbol renames to avoid intake overlaps: Sq (not Seq), chi^bullet (not
  circ), eta_k (not beta_k), J (not D).
- Missing work now: Barwise 1974 4.1 inputs (beyond-boundary item 2); Keisler L(Q) (item 1); p. 18 class-structure case;
  items (a), (b), (e) of session 5; Hodges 2001 (blocked_source ACQ-2026-10-0433); driver insertion (lead).

Session 7 (w02ca r5, block 2):
- Gap: Barwise 2.5 for weak second-order logic (p. 10) and the kappa = aleph_0 form for L_omega1omega and L(Q_0)
  (p. 45, 5.6) were hosted only for finite or countable languages.
- Held file opened this session: the HML whole-book scan (Schwichtenberg1977 entry), PDF 26 (Barwise p. 10, 2.5:
  "Let kappa be an infinite cardinal and let T be a set of at most kappa first-order axioms ... cardinality <= kappa";
  the "<=" checked on the page image, the text layer reads "="; the same page says the principle "also holds for weak
  second-order logic"), PDF 60-61 (pp. 44-45, 5.4 LS for L_omega1omega; 5.6 WSO, L_omega1omega, L(Q_0) satisfy 2.5
  with kappa = aleph_0). No new locator.
- Host w02-p02-005 body (CRLF kept): thm bw-weak-so-ls part 1 restated for any language, every infinite kappa, every
  set of at most kappa L*-sentences (model HF(A) with |A| <= kappa, |A u HF(A)| <= kappa); substructure form kept
  under |L| <= kappa; countable-language form kept as "in particular" (used by thm bw-countable-field). New paragraph
  after the theorem: hypotheses match 2.5; limitation of the substructure form (kappa^+ distinct constants).
  thm bw-extended-ls: "Let the language be finite or countable" replaced by any language; parts 1-2 are sets of at
  most aleph_0 sentences with models of cardinality at most aleph_0. 5.6 paragraph: "over a language of any
  cardinality (for WSO with every infinite kappa)".
- Host w02-p02-005 annex: annex bw-weak-so-ls rewritten (cardinalities: finite subsets, closures, HF(A), number of
  L'*-formulas; reducts; hull for a language of at most kappa symbols; part 1 via L_T reduct, hull, expansion; the
  substructure and countable cases). annex bw-extended-ls part 1: L_T countable (symbols in atomic subformulas), reduct,
  countable hull, expansion; part 2: translation keeps L and countability.
- Host w02b-p02-001 body (CRLF kept): sharpness remark now "L_omega1omega over a language of any cardinality".
- Symbol intake: L_T, M_T, A_T, L' row.
- Checks: unit-compile ok (28 overfull); find_fused_spaces clean on the three edited hosts.
Next: still-owed items of session 6 (Szmielew; undecidability of groups; D2/D3 and enumeration for T#; L_A claim
inputs; Keisler L(Q), blocked_source; p. 18 class case); Hodges 2001 blocked_source; driver insertion (lead).

Session 8 (w02ca r5, block 3):
- Gap: Barwise ch. A.1 items without host or missing-work record: (i) p. 12 "proof of 2.6 is misleading"
  (more reals than first-order definitions over countably many symbols; reason for 2.7 with names for all reals);
  (ii) pp. 12-13 most theorems of calculus first-order, hold in *R, basis of infinitesimal analysis, Leibniz;
  (iii) p. 8 effectively presented infinite list "practically as good as" a finite list.
- Held file opened this session: the HML whole-book scan (Schwichtenberg1977 entry), PDF 24 (p. 8), PDF 28 (p. 12),
  PDF 29 (p. 13), text layer and page images. Page-image check: the p. 12 sentence reads "Thus 2.5, far from being
  a negative result, ..." (printed numeral 2.5, not 2.7); recorded in reader as printed 2.5, read as referring to
  2.7 (decision below). p. 13: "For more on this, see Chapter A.6 and its 1.1 in particular." No new locator.
- Written, host w02-p02-005 body (CRLF kept): 335-344 paragraph with marked one-sentence quotation of the p. 8
  remark and its standing; 391-425 thm:p02-w02c-p02-003-effective-lists (1: consequences of an effectively listed T
  are effectively listed, via thm:fol-validity-enumerable and compactness; 2: complement-axiomatizability forces
  finite axiomatizability; 3: divisible abelian groups: complement among abelian groups not axiomatizable, using
  thm bw-divisible) + paragraph; 447-450 diagnosis sentence crefs transfer part 1; 452-461 paragraph on the p. 12
  "misleading" verdict (Barwise's assessment); thm:p02-w02c-p02-003-undefinable-reals (definable elements of a
  countable-language structure are countable; an undefinable real; with names for all reals still no categorical
  axioms); thm:p02-w02c-p02-003-transfer (c and 1/c; square roots transfer; R has no lub in *R; expansion by any
  set F of functions/relations); 539-558 standing paragraph (calculus claim not made precise by Barwise; what is
  proved; Leibniz assessment reported, with the marked phrase "only a mild exaggeration"; referral to A.6, 1.1).
- Written, host w02-p02-005 annex: annex:p02-w02c-p02-003-effective-lists (221-289), -undefinable-reals (364-413),
  -transfer (415-492).
- Existing treatment found: thm:p02-w02-p02-033-infinitesimal (w02-p02-033; elementary-diagram construction, positive
  infinitesimal) - cross-referenced, not duplicated; thm:fol-validity-enumerable (restoration 08248-08305) used.
- Decisions: the printed "2.5" in the p. 12 sentence read as referring to 2.7 (the sentence follows 2.7's proof and
  speaks of *R; 2.5 is Loewenheim-Skolem). "First-order theorem of calculus" read relative to L_R or L_F, since
  Barwise names no language; statements quantifying over all functions or subsets are not covered (stated).
- Symbol intake: L_R/R_R/*R_R, F/L_F/R_F/*R_F (overlap with P01/P03 \mathcal F rows, different roles), dot f/dot P,
  c/epsilon/delta, #phi/e/g/D, tau_i/upsilon_j.
- Checks: unit-compile ok (28 overfull); find_fused_spaces clean on both edited hosts; check.py --tree: only
  bib-key Rabin1977Decidable (own intake) among hard findings in owned/edited files.
Next: unchanged from session 7 (Szmielew; undecidability of groups; D2/D3 and enumeration for T#; L_A claim inputs;
Keisler L(Q) blocked_source; p. 18 class case); Hodges 2001 blocked_source; driver insertion (lead).

Session 9 (w02ca r5, block 1):
- Held file opened this session: source/references/acq-r1-ACQ-2026-10-0225/ACQ-2026-10-0225.pdf (Keisler, "Logic with the
  quantifier 'there exist uncountably many'", Ann. Math. Logic 1 (1970) 1-93, publisher version; manifest
  downloaded_verified; PDF page = printed page). Text layer read for pp. 1-28 (Introduction, sec. 1, sec. 2, start of sec. 3).
  Locators used: p. 4 (L countable, power <= omega; formulas; weak model), p. 5 (Q clause, 1.1, 1.2, standard model, omits),
  p. 6 (Axioms 0-4 with Church reference for Axiom 0; intuitive readings; 1.3), p. 7 (infinite-sets weak model; rules MP,
  Gen; deductions only from sentences; 1.4, 1.5; AC remark), p. 8 (1.6-1.8), pp. 9-12 (1.9), p. 13 (Completeness theorem
  statement; witnesses; 2.2), pp. 14-15 (2.2 proof, 2.3), p. 16 (uncountable L remark; 2.4; elementary extension, chain,
  union), pp. 17-18 (2.5, A*, 2.6), pp. 19-23 (2.7), pp. 23-24 (2.8), pp. 24-26 (proof of completeness; 2.9, 2.10),
  p. 27 (2.11; Fuhrken/Vaught attribution; uncountable-constants counterexample).
- Written (body, owned file): sec:p02-w02c-p02-003-keisler (lines ~1360-1665): def kq-language, def kq-calculus,
  lemma kq-soundness (1.1-1.5), lemma kq-proof-lemmas (1.6-1.8 plus derived rules, alphabetic variants, maximal sets),
  thm kq-weak-completeness (2.2-2.4), lemma kq-finite-unions (semantic form of 1.9(i),(iv)), lemma kq-chains (2.5, 2.6),
  lemma kq-main-lemma (2.7, 2.8), thm keisler-completeness (with 2.9 one direction and 2.10 first part),
  cor keisler-compactness (2.11), example kq-example (p. 27 counterexample), warning kq-axiom-zero. Intro list updated;
  beyond-boundary item 1 (Keisler) removed.
- Written (annex, owned file, lines ~2254-2911): annexitems kq-soundness, kq-proof-lemmas, kq-weak-completeness (with
  derived facts (E) equality substitution for all L(Q) formulas and (N)), kq-finite-unions, kq-chains, kq-main-lemma,
  keisler-completeness, keisler-compactness.
- Host w02-p02-005 body: Keisler paragraph now crefs the two theorems; "item 2 of beyond-boundary" -> "the item of";
  5.6 paragraph crefs keisler-compactness.
- Decisions: (1) Keisler's identity symbol (written with a triple bar) rendered as =, since \equiv has registered roles
  (formula equivalence, elementary equivalence); stated in the reader. (2) Axiom 0: Keisler cites Church's list (Church
  not held, not compared); the handbook fixes schemes (0a)-(0g) and records this in warning kq-axiom-zero. (3) Keisler's
  Lemma 1.9 is proved semantically (in weak models where all axioms hold) instead of syntactically; only the semantic form
  is used by the proof of 2.7. (4) Omitting-types step and Main Lemma follow Keisler; the Henkin model construction
  (Keisler cites Henkin) is written out in full with equality classes.
- Not written: Corollary 2.9 converse direction (a standard model of power omega_1 makes Sigma u {(Qx)(x=x)} consistent; it
  is immediate from soundness but not stated) and Corollary 2.10 second part (recursive enumerability of the valid
  sentences in the set of symbols of L). Recorded as open items.
- P3 thm:p03-keisler-q-one (cited=Keisler1970) could now point to these proofs: crosslink request to the P3 owner.
- Checks: unit-compile ok (35 overfull, max 13.8pt, none from the new text above 10pt after two fixes); find_fused_spaces
  clean on owned body, annex and host; check.py --tree: in owned files only bib-key Rabin1977Decidable (own intake).

Next (still owed, in order):
(A) D2/D3 for T# and a formal enumeration of T# (thm:p02-w02c-p02-003-integers-second, theories-boundary item 3).
    Planned route (not yet written): (i) formal hypothesis on T: its code set is computably enumerable in the sense of
    sec:arithmetic-coding-04; then T# = {sigma : exists w R(w, sigma)} with R primitive recursive, from the p.r. checker
    (thm:p05-standard-pa-numerical-proof / sec:arithmetic-coding-04), the p.r. translation tr of
    thm:p02-w02c-p02-003-ring-coding and the p.r. PA-axiom recognizer def:p05-direct-pa-axioms -- this is the formal
    enumeration. (ii) Craig's trick: A = {sigma and (w = w) padded : R(w, sigma)} is primitive recursive and has the same
    consequences as T#. (iii) New proof description d_# = d_19 of def:p05-selected-direct-pa-graph with the axiom factor
    Ax_19 replaced by max(Ax_19, Cr) (Cr the p.r. test for A); Prv^#(x) = exists p Gamma_{d_#}(p,x,1). Meaning: as
    thm:p05-selected-direct-pa-graph with axiom set PA u A (needs a check of annex:p5.checker-description that Ax_19 enters
    only as the open-leaf factor). D2: annex:p5.checker-internal-mp with chi_# for chi_19 (needs a check that the internal-mp
    proof uses no property of Ax_19). D3: thm:p05-original-sigma-evidence applied to the Sigma_1 sentence
    Prv^#(code phi) (coverage of Gamma_{d_#} by thm:p05-literal-graph-evidence) gives PA |- Prv^#(phi) -> Prv^19(Prv^#(phi));
    then PA |- forall x (Prv^19(x) -> Prv^#(x)) (Ax_19 <= Ax_#, internal bounded-product monotonicity) gives D3.
    (iv) Replace Prov_{T#} in thm integers-second by Prv^# and check thm:godel-second's hypotheses on the chosen formula.
(B) thm:representability (cited, restoration capture; blocked_policy for this packet).
(C) Szmielew; undecidability of groups (sources not held: Szmielew 1955; TMR 1953 ACQ-2026-10-0529).
(D) Barwise 1974 4.1 inputs (Makowsky-Shelah-Stavi 1976; Barwise L_HYP interpolation; Admissible Sets and Structures 1975;
    not held).
(E) Hodges 2001 blocked_source ACQ-2026-10-0433; driver insertion of the owned files (lead).

Session 10 (w02ca r5, block 2):
- Gap closed (in order given): Barwise p. 16 G2 claim, D2/D3 and computable enumerability of T^sharp.
- No new source opened; no new locator (p. 16 locator already verified in earlier sessions). Inputs read on the live route:
  sec:second-incompleteness-01 (inherited-09750-09816: specified formula, D1-D3, Con), thm:godel-second and thm:lob
  (inherited-09877-09924, 09817-09876), def:fixed-proof-predicate and lem:p05-numeralwise-d1 and the certified c.e.
  relation (inherited-09328-09438), thm:representability / def:p05-pa-pr-graph / thm:p05-pa-pr-graphs /
  thm:p05-pa-sigma-evidence (inherited-09262-09327), thm:bounded-verification (inherited-08710-08876), P5
  standard-pa-proof-predicate (def direct-pa-axioms, StdProof, annex standard-pa-checker), pa-checker-arithmetization
  (description language, Ax_19, chi_19, d_mp, internal mp and its annex), pa-positive-introspection
  (original-sigma-evidence, literal-graph-evidence, direct-pa-d3 and annexes), P4 def:p04-partial-recursive,
  thm:p04-tm-partial-recursive (cited Kleene1952), sec:turing-machines-02/-03, def:partial-computable.
- Written (body, owned): 1894-2185: intro paragraph; reading paragraph (Church-Turing thesis only for reading Barwise);
  def sharp-enumeration; lemma ring-transfer; lemma sharp-enumeration; def sharp-formula; thm sharp-provability;
  thm integers-second (restated: T c.e.; T^+ with PA^d; part 2 T^+ does not imply Con^sharp^Z); worked example T empty;
  lemma arbitrary-representative (failure case); theories-boundary item 3 rewritten (only the cited Kleene step);
  intro list and relationships updated.
- Written (annex, owned): 3325-3784: ring-transfer (structures M*, K'), sharp-enumeration (p.r., meaning, mu-recursive
  domain, Kleene), sharp-provability (Part 1 meaning via factor identification of annex:p5.checker-description and the row
  induction of annex:p5.standard-pa-checker; Part 2 D1; Part 3 joining with the axiom-free paragraphs of
  annex:p5.checker-internal-mp and a written axiom-product paragraph; Part 4 internal monotonicity by fold induction;
  Part 5 D3 via literal-graph-evidence + original-sigma-evidence + Part 4), integers-second (rewritten),
  arbitrary-representative (rho' = rho and not x = code of bottom_A).
- Host w02-p02-005 body 652-655 (CRLF kept): boundary reference reworded.
- Symbol intake: C_T, Lf, Pf^+, En^sharp, (T^+)^circ, pd, A^sharp, cr, Cr, Ax_sharp, chi_sharp, d_sharp, Prf^sharp,
  Prv^sharp, Con^sharp, mp_sharp/d^sharp_mp, M*/K', F_19/F_sharp, rho'; T^+ row updated (PA^d).
- Decisions: T^+ uses PA^d (literal presentation) so the enumeration needs no index for the source PA axiom set;
  ring/L_A transfer uses S interpreted as the constant 1 (no ring axioms needed); Craig padding by k conjuncts 0=0.
- Checks: unit-compile ok (39 overfull, max 13.8pt, pre-existing); find_fused_spaces clean (owned body, annex, host);
  check.py --tree: in owned files only bib-key Rabin1977Decidable (own intake).
Next (still owed): Szmielew; undecidability of groups (sources not held); Barwise 1974 4.1 inputs (not held); Keisler
2.10 second part and 2.9 converse (not stated); Hodges 2001 blocked_source; driver insertion (lead); the cited Kleene
equivalence (P4).

Session 11 (w02ca r6, block 1):
- Gaps (in order): (1) Barwise p. 44 positive half (completeness for countable L_omega1omega theories with an
  infinitary rule); (2) Barwise p. 37 (derived rules 4.11(iii),(iv) in place of the generalization rules of H).
- (1) Owned body: pointer paragraph after thm infinitary-rule; block before the WSO Beth-failure paragraph:
  def hinf (calculus on sentences of L u Par: A1 infinitary tautologies over prime sentences, A2/A3 for closed
  terms, R1 MP, R2 generalization with a fresh parameter, R3 countable-premise conjunction rule; theorems = least
  closed set), lemma hinf-soundness (soundness; countably many premises suffice, AC), lemma hinf-nnf (tautological
  consequence, derived disjunction rule, |- bigwedge T, syntactic n.n.f. for formulas with finitely many free
  variables and parameters), def term-consistency (T0-T6), thm term-model-existence (term Hintikka sets; chain over
  closed terms), thm infinitary-completeness (any L, T countable, AC), example hinf-example, thm hinf-uncountable
  (T with c_alpha, alpha < omega_1, and d_n: no model, no proof of not bigwedge empty). Annex items hinf-sound,
  hinf-nnf, term-mex, hinf-complete, hinf-uncount (inserted before annex wso-n). Intro list and relationships updated.
  Host w02-p02-005 body p. 44 claims paragraph crefs infinitary-completeness and def hinf (CRLF kept).
- Decision: parameters instead of free variables in H_infinity, because one L_omega1omega sentence can use every
  variable of a countable stock, leaving none to serve as a witness; stated in the reader.
- (2) Host w02-p02-005 body after the p. 37 remark (CRLF kept): def system-h-circ, thm h-circ-completeness,
  example h-circ-example, warning h-circ-proviso. Host annex (LF) before bw-g-prop-completeness: annex item
  h-circ-completeness (semantic soundness of the two rules; derivation of clause (v) from (iii), (iv) via
  D = not exists y not phi(y) -> forall y phi(y), obtained by (iv) with a fresh variable w; completeness by the
  host's 4.9 annex proof with the blocks removed by the two rules and derived (v)). Paragraph moved to keep
  \tfrac out of the 240-character window before \vdash (check.py rule-shape heuristic).
- Symbol intake rows: H_infinity, |-_infinity, Par, top, chi sigma, CT, varphi^*, H^circ, |-^circ, D.
- Checks: unit-compile ok (40 overfull; one new 2.5pt title box); find_fused_spaces clean on the four edited TeX
  files; check.py --tree: no new finding in these files (pre-existing mathfrak V row in host body; bib-key
  Rabin1977Decidable from own intake).
Next (still owed): narrower-proviso H-circ completeness (alphabetic variants); items (A)-(E) of session 9/10 that
remain (Szmielew; groups; Barwise 1974 4.1 inputs; Keisler 2.10 second part and 2.9 converse; Hodges 2001
blocked_source; driver insertion by the lead; Kleene equivalence (P4)).

Session 12 (w02ca r6, block 1, packet w02ca-p02-003.3):
- Gaps as given: (1) Barwise p. 44 completeness with an infinitary rule; (2) Barwise p. 37 replacement of the
  generalization rules. Both were already written in session 11 (the assessment quoted line ranges from before it);
  re-read and checked: H_infinity block (owned body 1110-1323, annex 1680-2156) and H-circ (host body, annex).
- Held source re-opened this session: HML whole-book scan (Schwichtenberg1977 entry), PDF 50-53 = Barwise pp. 34-37
  (convention on p. 34: phi(t/v) written only when the variables of t do not occur bound in phi; 4.11 (iii), (iv)
  with "v does not appear in psi"; proof of 4.9; p. 37 remark). No new locator.
- New result: host w02-p02-005 body 1217-1330 (paragraph; def system-h-flat; thm h-flat; example h-flat-example;
  warning h-flat-limit) and warning h-circ-proviso last sentence; host annex 1239-1419 annex h-flat. Method: an
  auxiliary satisfaction relation in which every doubled existential formula (exists x chi with x bound in chi)
  holds at every assignment; all axioms with unrenamed schema (3) instances and all rule instances under Barwise's
  convention preserve it; sigma = not exists x exists x not x=x fails under it but is valid and H-provable (H's
  reading lets y = v without condition).
- Symbol intake rows: H-flat, H-flat-g, |-flat, |=flat, H-flat-union, sigma/rho (local).
- Checks: unit-compile ok (40 overfull); find_fused_spaces clean on both hosts; check.py --tree: no new finding.
Next (still owed): H-flat with renamed schema (3) instances (open, warning h-flat-limit); items listed in session 11.

Session 13 (w02ca r6, block 2, packet w02ca-p02-003.3):
- Gap as given: guard G14 at host w02-p02-005 body line 1280 (workflow word in thm h-flat part 3). Replaced
  "rule instances admitted by" with "rule instances permitted by" (byte-level, CRLF kept). No other text changed.
- Content guards (G8, G9, G11, G12, G14, G15) via tools/waves.py: no item on owned body, owned annex and the three
  editable hosts. unit-compile ok (40 overfull, unchanged); find_fused_spaces clean; check.py --tree: no new finding.
- Hodges 2001 (ACQ-2026-10-0433): web search for a legitimate free copy of either edition or a preprint found only
  catalogue/bookseller records; wilfridhodges.co.uk refused the TLS handshake. Still blocked_source; nothing read.
Next (still owed): unchanged from session 12 (H-flat with renamed schema (3) instances; Szmielew; groups; Barwise 1974
4.1 inputs; Keisler 2.10 second part and 2.9 converse; Kleene equivalence (P4); driver insertion by the lead).

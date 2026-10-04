# w02-p02-028: Herbrand methods (P2 19.1-19.3), block 1

Packet: `work/waves/w02/packets/w02-p02-028.json`; label tag `p02-w02-p02-028`.

## Sources opened in this session

- **Statman 1977, Handbook of Mathematical Logic ch. D.3, printed pp.897-912.**
  Held file: `source/references/acq-r1-ACQ-2026-10-0497/schwichtenberg-1977-proof-theory-applications-cut-elimination.pdf`
  (SHA-256 hash 0226941f...2aba, listed in `spec/coverage/edition-2026/held-sources.json`).
  It is the whole-book scan of the eighth impression (1993) of the 1977 first edition, with 1977 pagination.
  The manifest's extent note says PDF p.913 begins D.3. Checked here: PDF p.913 is the chapter opener (printed p.897),
  and PDF pp.914-928 are printed pp.898-912, with running heads "STATMAN/DIRECT PROOFS [CH. D.3".
  PDF p.929 opens D.4 (Feferman). Every page was read from 150 dpi renders, and pp.905-906 also at 300 dpi.
  The packet's `units[].held_paths` is empty; the file was located through held-sources.json.
- **Schwichtenberg 1977 (same file), Theorem 2.9 "Herbrand's Theorem"**, printed p.876 (PDF p.892).
  Statman points to it at p.898 ("Theorem 2.9 of Chapter D.2").
- Not consulted: Kreisel-Krivine 1967 (Statman's referral to Exercise 8, p.48 is reproduced as his referral and flagged in reader text);
  Kreisel-Tait 1961; Lifšic 1968; Statman 1974. Their bib entries are transcribed from Statman's p.912 list only.

## Printed-text observations (source fidelity)

- The number 2.8 is printed twice (length, then singularity, p.902). The reader text says so.
- In the proof of 3.1(ii) (p.906), "M(s^q z_j)=(M(s^m z_i)" is printed. The argument needs, and the measure conditions give,
  M(s^q z_j) <= M(s^m z_i). The annex proves the inequality and notes the printed sign.
- The proof of 3.2 (p.907) says "apply proposition" with no number; it is 3.1.
- The proof of 4.1.1 (p.911) says "Proposition 3.3"; the result is numbered 3.3.2.
- Lifšic [1968] is in the reference list (p.912) but I found no citation of it in the chapter text.
- In 1.6(a), the constant k of 2^{kp} is left open; 3.2(i) gives k=9 for p = lh(S)+lh(a=b).

## Existing treatment found that the packet does not list

- `handbook/parts/p02/first-order-resolution.tex:213-252` has thm:p02-herbrand-clauses (cited=Robinson1965) and
  thm:p02-resolution-lifting (cited=BachmairGanzinger2001). This file is not on the current p02 driver route
  (first-order-logic.tex inputs only the -supplement files and first-order-depth).
- `handbook/parts/p02/first-order-normal-forms.tex:223-257` (Skolemization; off-route) duplicates the on-route
  inherited thm:skolem-equisatisfiable (`handbook/restoration/inherited-05132-05567.tex:316`). The latter is used.
- The on-route results used are lem:fol-coincidence, thm:prop-compactness, thm:prop-resolution-complete,
  thm:prenex-normal-form, lem:fol-nnf, thm:skolem-equisatisfiable, lem:clause-substitution, def:p02-matrix-clause-construction,
  thm:p02-matrix-clause-equivalence and thm:fol-validity-undecidable (the last only as context; the no-bound corollary is
  stated conditionally on equality-free undecidability).
- The first-order unification theorem in `inherited-05568-05923.tex` (unlabelled, proof marked "Proof sketch") is used by
  the lifting lemma for existence of an mgu of two unifiable atoms.

## Provenance of the Herbrand block

The proofs are my own, from the handbook's definitions. They do not reproduce AfshariEnqvistLeigh2025, Robinson 1965
or Bachmair-Ganzinger. Proof routes:
- validity form, via a Herbrand model built by propositional compactness after passing to the finite signature of sigma;
- general form, via the Herbrand form as negated Skolemization of the prenex dual (AC is used only in the Hf-valid to sigma-valid direction);
- clause theorem, via the same model lemma;
- duality, via nnf plus the inherited matrix clause construction;
- resolution, via a direct lifting proof (factoring by successive pairwise mgus, then one resolution on renamed-apart parents).

## Provenance of the Statman block

The full annex proofs of 3.1 and 3.2 reconstruct Statman's routes and fill in his steps:
- 3.1 (i)-(v): the properties of S_{n_0} that need no hypothesis;
- the explicit read-off interpretation with finite-support functions;
- height and size counts giving 2^{3k} and 2^{4k};
- M-directness through the measure conditions;
- the cycle bound p <= number of s-equations;
- for 3.2, the flattening with the transfer map rho.

The following are my own proofs of claims that Statman makes without proof or sketches, each under hypotheses stated in the reader text:
- completeness of K, both routes;
- the polytime decision;
- the 16p^2 sequence bound (Statman's "kp^2");
- the model-theoretic route;
- the semigroup claim;
- the Horn claim of 1.3(ii), via Herbrand plus forward chaining (kept as a second proof), and, from block 3, along the
  chapter's own cut-elimination route (thm:p02-w02-p02-028-st-horn-cut);
- the S_n example.

Hypotheses I made explicit:
- Horn claim: prime formulas are read as equality-free atoms.
- Route-1 general models: the function sort contains lambda x.c with beta behaviour, which is my reading of "closed under explicit definition".

The rule displays of K use `\frac` inside a definition. tools/check.py does not flag them, but CONVENTIONS asks for rule displays in registry/calculi. A sheet `registry/calculi/statman-k.tex` would be a lead decision.

## Continuation

State at return (block 2):
- Proved in the annex (proved=), all statuses now proved=: everything listed for block 1, plus
  - thm:p02-w02-p02-028-unification (mgu existence: termination measure (n1 variables, n2 total size, n3 misoriented),
    invariant "unifiers = theta.eta with eta solving E" per transformation; occurs check via size);
  - thm:p02-w02-p02-028-st-herbrand-eq ([1.1] with equality, conclusion "valid"; route: equality as a fresh relation,
    equality axioms as universal hypotheses, quotient structure, existential Herbrand, discard axiom instances);
  - thm:p02-w02-p02-028-st-methods ([1.2] general: decidability of quantifier-free validity with equality via ground
    equality-axiom instances over the subterm set and a quotient countermodel; partial recursive search; total on derivations;
    no total recursive method, via Herbrand form with equality and the cited Church-Turing theorem);
  - def:p02-w02-p02-028-st-positions (positions, replacements, spines, H fragments);
  - thm:p02-w02-p02-028-st-nesting ([2.11](ii),(iii));
  - thm:p02-w02-p02-028-st-normal-forms ([2.11](a),(b), [2.12]: leftness argument, T_R = spine positions pairwise disjoint,
    T_L = no rule-(1) side premise concluded by rule (1));
  - 3.3.2 (inversion count of ascending-over-non-ascending pairs; boundedness by top/bottom induction),
    3.4 (T_L, left-before-right switches, fragment replacement, deletion of b=b side premises),
    3.5 (innermost-first stages; count gives lh(T_W) <= n^2),
    1.7(b) (now <= p^2), 4.1.1 (projection-anticipating instances f_{l,J}), and
    thm:p02-w02-p02-028-st-optimality ([4.1], under the stated reading of "analytic rule").
- Caption of fig:p02-w02-p02-028-st-fragments corrected: in T_L each conclusion is the main (left) premise of the next
  inference (block 1 said "right premise", which contradicts p.903 and p.908).

Source-fidelity notes for block 2 (Statman 1977, held scan PDF pp.913-928):
- p.903: [2.11](i)-(iii),(a),(b) and the leftness description; [2.12] shapes.  p.907: [3.3.1], [3.3.2] with its proof;
  [3.4] statement and start of proof.  p.908: [3.4] fragment displays and deletion step; [3.5] statement, the 2p / p+2 /
  2p+2 description.  p.909-910: [3.5] stages, cases (i),(ii).  p.910: [4.1] efficiency claim ("We leave most of the details
  to the reader"), [4.1.1] statement.  p.911: [4.1.1] proof ("Proposition 3.3"), [4.2], [4.3].
- [3.5] length accounting: the annex reproduces the chapter's quantities as verified bounds (fragment <= 2p-1, chain passed on
  <= p+1, new equations of the K computation <= 2p+1) and adds the per-stage growth bound p+1, giving n^2 <= n^2+n+1.
- [3.5] case (i): the chapter displays only the step at the root of t_i (rule (2) on s r_i = s r_{i+1}); the annex also treats
  steps inside the argument of s, which need no rule (2).
- [4.1]: the chapter does not define "analytic rule".  The theorem reads a rule (S_rho, E_rho) as analytic when
  /\S_rho -> E_rho is analytic in the sense of [2.15], applied through substitution instances.  This reading is stated in the
  reader text; it is the handbook's, not the chapter's.
- [1.2] item 4 is proved for a coded signature with infinitely many function symbols of each arity (needed for the Herbrand
  form).  Without function symbols, existential validity is decidable (finite Herbrand universe), so the hypothesis is not
  idle; that remark is not written in reader text because it is not proved there.

Still open (not written): none for the components of this packet (see block 3 below).
- Patch requests in work/waves/w02/patches/w02-p02-028.json (3 ops, lead).
- Guard note: the G1 hits on spec/research/edition-2026-p02-completeness-choice-scope-w02-p02-054{,-return.json}.md and
  edition-2026-p02-unit-accounting-w02-p02-044/045 files are untracked files written at 04:01-04:08 by other packets running
  concurrently in this tree (this packet's files were last written at 03:32 before this block). This packet did not create,
  edit or revert them; reverting another agent's files is outside this packet's edit permission.
- p.899 checked in this block (the cut-elimination remark of [1.3(ii)]).

State at return (block 3):
- Statman p.899 re-read this session from the held scan (PDF p.915, 150 dpi), and p.898 (PDF p.914) for [1.3(i)]: the conclusion is
  "for each substitution theta" for both the axioms theta A_i and the rules; the cut-elimination remark is the only justification printed.
- Written: the [1.3(ii)] Horn claim along the chapter's route (Gentzen's cut elimination), body lines 1071-1264, annex lines 1661-2018:
  - def:p02-w02-p02-028-st-horn-cut-setting (hypotheses the route needs), def:p02-w02-p02-028-st-horn-system (left/right formulas,
    G-forms, H(Theta;Gamma), targets);
  - thm:p02-w02-p02-028-st-gform (instances of G-forms under the on-route capture-avoiding substitution, inherited-03240-03428.tex);
  - thm:p02-w02-p02-028-st-lk-translation (sheet:lk -> sheet:lk-defneg, rule by rule; the handbook's thm:p07-lk-presentation-equivalence
    is only sketched, so the needed forward half is proved here);
  - thm:p02-w02-p02-028-st-extraction (induction on cut-free LK_d derivations; Cut-free input from the proved
    thm:p07-classical-cut-elimination);
  - thm:p02-w02-p02-028-st-horn-cut ((1) from LK_d-derivability; (2) from validity via thm:p07-canonical-lk-completeness for the
    finite signature of G, so no Choice); example with two substitutions and a proof that one substitution does not suffice; limits warning.
- Route choice: the midsequent theorem (only cited in the handbook) is not needed. The extraction works directly on any cut-free
  derivation because the endsequent has no strong quantifiers, so no eigenvariable inference can occur.
- Why the equality-free reading is a hypothesis of this route: LK_d has no equality, and on sheet:lk-eq Cut is not admissible
  (thm:p07-eqlk-cut-failure, proved). The reader text says this.
- Differences from st-horn: no sentence requirement; theta terms may contain variables; Theta is read off the cut-free derivation
  (substitutions of the G-instances principal in ->R).
- Unit compile: sheet: anchors are written as plain \texttt because the unit compile's label scan does not see \calculussheet anchors.
- tau replaced by eta for the variable-to-term map (tau is a global sentence metavariable); facts in the gform proof are (S1)-(S3) to avoid
  clashing with (F1) of the unification proof.
- Guard note: the G1 hits named in this block's task (unit-accounting-w02-p02-042/044 .md and -return.json) are files of packets 042 and 044;
  this packet did not touch them.

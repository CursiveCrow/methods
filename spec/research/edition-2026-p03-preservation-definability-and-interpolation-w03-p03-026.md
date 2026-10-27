# w03a-p03-026 research note: preservation proofs (P3 ch. 30, sections 30.1-30.4)

## Sources read in this session

- Los1955: J. Łoś, On the extending of models (I), Fund. Math. 42 (1955) 38-54.
  Held file source/references/acq-r1-ACQ-2026-10-0269/ACQ-2026-10-0269.pdf
  (SHA-256 prefix 7a9b4453; image-only spreads). All nine spreads (pp. 38-54) read as
  rendered images. Locators used: p. 47 (groups with one operation: N as a
  submodel of the integers; open axioms only with an inverse operation;
  Theorems 4-5), p. 48 ((8.1), Section 9 persistent sentences, Theorem 6),
  p. 54 (method attributed to Mal'cev and Robinson; Henkin's related results).
- No Chang-Keisler 1990 or Hodges 1993 body is held; neither is cited with a
  locator.

## Provenance of the written proofs

Body handbook/parts/p03/preservation-definability-and-interpolation-w03-p03-026.tex,
annex handbook/annex/p03/preservation-definability-and-interpolation-w03-p03-026.tex.
Proofs are written from the handbook's own compactness (thm:fol-compactness),
diagram tests (thm:diagram-tests), isomorphism invariance
(lem:iso-invariance), reduct invariance (lem:reduct-invariance),
alpha-invariance (cor:alpha-invariance) and elementary chain theorem
(thm:elementary-chain). The relative Łoś-Tarski statement follows the
generality of Łoś's Theorems 5 and 6 (definable subclass of a definable class;
persistence relative to a definable class). The Chang-Łoś-Suszko proof is the
alternating-chain argument; the original chain papers (Chang 1959 Proc. AMS;
Łoś-Suszko 1957 Fund. Math. 44) are not held and are not cited with locators.

## Patch request for the read-only host

work/waves/w03a/patches/w03a-p03-026.json asks the lead to change the status of
thm:p03-los-tarski and thm:p03-chang-los-suszko in
handbook/parts/p03/preservation-abstract-logic.tex from cited=ChangKeisler1990
to a pointer to the new proofs (see the patch file), and to \input the new body
file after parts/p03/presentations/n-a-011-02 and the new annex file after
annex/p03/n-a-011-02 in handbook/annex/p03.tex.

## Session 2 (block 1, continuation run)

- Re-read Los1955 in full this session from the held scan
  source/references/acq-r1-ACQ-2026-10-0269/ACQ-2026-10-0269.pdf (sha256 7a9b4453...;
  nine two-page spreads rendered to tmp/agent-scratch/w03a-w03a-p03-026-b1-author/los2,
  pp. 38-54 all read). Every locator in the new subsection was seen on the page cited.
- Verified the existing MAP-01/MAP-02 proofs (annex items union, easy, prenex, embed,
  los-tarski-relative/-class/-sentence, step-up, step-back, chang-los-suszko,
  elementary-chains-differ, groups) step by step; no change needed. The assessment's
  "stated only at cited=ChangKeisler1990" finding concerns the host theorems, which stay
  cited until the lead applies work/waves/w03a/patches/w03a-p03-026.json (anchors re-checked
  this session: preservation-abstract-logic.tex lines 230, 242, 307; annex/p03.tex line 16).
- Wrote the Los 1955 source presentation (sec:p03-w03-p03-026-los1955, sections 1-17) with
  annex proofs (annex:p03-w03-p03-026-los55-*).
- Printed-text readings recorded in reader text: Theorem 9 display has an undefined C (read
  as B; equivalent under the hypothesis); section 14 prints M(A1+C2), O1 n Cn2(A) and
  Cn2(A1 n C2) (read as unions / A1 u C2), and sm(P)|1 (Theorem 8 covers sm(P|1)); section 15
  gamma as printed lacks the compatibility clause (so alpha holds in every group); a fourth
  open clause is supplied and proved in thm:...-los55-ordered.
- Section 16: the source only sketches the rebracketing argument (footnote 19, bracket-free
  notation). The annex proves the claim by a different route (explicit reducible extension
  S = T u (T x T)/~), stated as such in the reader text.
- Section 17: the source states the omega-complete theorem and its converse without proof.
  Proved here: converse; forward direction when the system is complete (Tarski-Vaught) or
  when A and the signs are countable (omitting types, thm:p03-vaught-partial-omission).
  Forward direction for a consistent omega-complete system that is neither complete nor
  countable: not proved (source gives no proof). Reader text says so. Consistency is
  needed (the inconsistent system E3 is omega-complete).
- Reported only (source gives no proof, results of others): Robinson's (9.1)/(9.2) and the
  commutative-ring analogue, Neumann's counterexample remark for arbitrary groups, Mal'cev's
  semigroup-to-group solution and infiniteness, Los [5] axioms for orderable groups and their
  infiniteness, Banach's non-reducibility result.

## Continuation

- In files (not accepted): MAP-01, MAP-02, GOAL-01..03 (unchanged from session 1); Los 1955
  presentation sections 1-17 with annex proofs (session 2); Lyndon 1959 historical items
  (session 1, editable host n-a-011-02.tex).
- Open for N-a-011-C01: (a) section 17 forward direction in the general (uncountable,
  incomplete) case; (b) Chang-Keisler 1990 named-result presentation, blocked_source;
  (c) Hodges 1993 secs 6.4-6.6 presentation, blocked_source (only contents/corrigenda held).
- Lead action needed: apply work/waves/w03a/patches/w03a-p03-026.json (routes both new files
  and switches host statuses to proved=).

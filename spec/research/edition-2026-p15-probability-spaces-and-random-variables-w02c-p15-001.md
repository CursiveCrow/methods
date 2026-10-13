# w02ca-p15-001 (P15 157.3-157.6): Lebesgue integral notation and the change of variables formula

Packet: work/waves/w02ca/packets/w02ca-p15-001.json. Label tag `p15-w02c-p15-001`.
Files: handbook/parts/p15/probability-spaces-and-random-variables-w02c-p15-001.tex,
handbook/annex/p15/probability-spaces-and-random-variables-w02c-p15-001.tex,
handbook/registry/symbols-intake-p15-probability-spaces-and-random-variables-w02c-p15-001.csv,
patch requests work/waves/w02ca/patches/w02ca-p15-001.json.
No new bibliography keys (DurrettPTEAuthor2019 is in handbook.bib); no intake bib written.

## Source reading (this session)

Held file: source/references/durrett-probability-2019-01-11/PTE5_011119.pdf (author version dated
11 January 2019), extracted with pdftotext -layout; printed page numbers taken from the running heads.

- p. 3: Durrett writes R^d (calligraphic) for the Borel sets of R^d, dropping the superscript for d = 1.
- p. 8: Example 1.1.12; with every F_i(x) = x the resulting measure is Lebesgue measure on R^d
  (Theorem 1.1.11 is on p. 7).
- sec. 1.4, pp. 23-24: "Notation for special cases" (a) Lebesgue measure on (R^d, R^d, lambda):
  int f(x) dx; (b) (R, R, lambda) with E = [a, b]: int_a^b f(x) dx for int_E f dlambda; (c) dG(x) for
  the measure with mu((a,b]) = G(b) - G(a) (all three on p. 23); (d) counting measure, sum_i f(i)
  (p. 24), mentioned mainly to show that results for sums follow from those for integrals.
- sec. 1.6.3, p. 32: Theorem 1.6.9 titled "Change of variables formula" (X random element of (S, S)
  with distribution mu; f measurable (S,S) -> (R,R) with f >= 0 or E|f(X)| < infinity; Ef(X) =
  int_S f(y) mu(dy)); Remark: to explain the name, write h for X and P o h^{-1} for mu to get
  int_Omega f(h(omega)) dP = int_S f(y) d(P o h^{-1}). Proof in four cases on pp. 32-33; on p. 33 the
  consequence that expected values of functions of random variables can be computed by integrals on
  the real line.

## Components

- ED26-P15-CH-integration-expectation-C006 (assessment gap: Durrett's notation (a) and (b) not
  defined on the route). Written: def:p15-w02c-p15-001-dx-notation (cases (a), (b), the bound
  variable and sections, mu(dy); pointers for (c) and (d) to def:p15-convolution-law and
  thm:p15-expectation-law-integral); thm:p15-w02c-p15-001-interval-integrals (endpoint independence,
  additivity, constants); thm:p15-w02c-p15-001-interval-limits with
  def:p15-w02c-p15-001-limit-not-integral (the limit of interval integrals versus the half-line
  integral, and a bounded step function whose limit exists while the half-line integral is undefined);
  worked example def:p15-w02c-p15-001-uniform-moments-as-integrals. Full annex proofs.
  thm:p15-w02c-p15-001-lebesgue-rectangles proves that rectangle volumes fix lambda^d (pi-system of
  half-open rectangles, generation of B(R^d) via thm:p15-borel-generators, exhaustion (-n,n]^d, and
  thm:p15-w02c-p15-002-sigma-finite-uniqueness from sibling packet w02ca-p15-002), so Durrett's
  Example 1.1.12 measure (p. 8) and the route's lambda^d coincide.
  Patch request 2 adds a pointer at the end of def:p15-integrable-functions.
- ED26-P15-CH-integration-expectation-C016 (assessment gap: Durrett's name "change of variables
  formula" and the Remark's explanation not recorded). Written: def:p15-w02c-p15-001-change-of-variables-name
  (name, Remark's renaming, reading as substitution y = h(omega) with transported measure, distinction
  from the Jacobian rule thm:p15-w02b-p15-042-diffeomorphism / thm:p15-affine-lebesgue),
  thm:p15-w02c-p15-001-change-of-variables (Durrett's statement in both forms, annex proof via
  thm:p15-expectation-law-integral), thm:p15-w02c-p15-001-uniform-integrals (E h(U) = int_0^1 h),
  warning def:p15-w02c-p15-001-change-of-variables-limits. Patch request 1 attaches the name to
  thm:p15-expectation-law-integral.
- Other integration-expectation and radon-nikodym components: no gap named in this packet; existing
  treatments in integration-expectation.tex / radon-nikodym.tex and their annexes, not modified.

## Readonly units (A14): gaps relayed, not written

The computed task listed gaps on units owned by other packets. Per A14 they were not written here.
Search of the current tree (this session) shows:
- Closed by w02c-p15-002 (157.7): measurable-probability C010 (thm:p15-w02c-p15-002-generator-variants),
  C016 (def:p15-w02c-p15-002-extended-line, thm:p15-w02c-p15-002-order-borel,
  thm:p15-w02c-p15-002-domain-extension), C021 theorem part (thm:p15-w02c-p15-002-sigma-finite-uniqueness);
  regular-conditional-laws C011 (def:p15-w02c-p15-002-borel-paradox), C005 (Dieudonne attribution and
  def:p15-w02c-p15-002-rcd-nonexistence). Not re-assessed here.
- Not found anywhere on the route (owner returns for w02c-p15-003, -006, -014 report these components
  as existing with no remaining gap): finite-probability C008 (odds ratio r:s, p = r/(r+s), betting
  reading), C013 (Grinstead and Snell Example 4.17 and the second-year medical students claim);
  measurable-probability C021 (Dynkin attribution of the pi-lambda theorem), C025 (measures on R^d,
  Durrett sec. 1.1 pp. 6-9); measure-extension C006 (name "Caratheodory's Extension Theorem"), C007
  (justification of the (a, b] endpoint convention), C012 (computer generation remark after Theorem 1.2.2).
  These go to the lead as crosslink requests in the return file.

## Round r3 additions (C012, C017 of integration-expectation; C018 of radon-nikodym)

Source re-read this session (same held PDF, pdftotext -layout, printed page from the running head):
- p. 25: Theorem 1.5.2 (Hoelder), proof via xy <= x^p/p + y^q/q.
- p. 26: Remark after Theorem 1.5.2: p = q = 2 is Cauchy-Schwarz; direct proof from
  0 <= int (f + theta g)^2 dmu = int f^2 + theta 2 int fg + theta^2 int g^2; the quadratic
  a theta^2 + b theta + c has at most one real root, so b^2 - 4ac <= 0.
- p. 29: Theorem 1.6.4 "Chebyshev's inequality" (phi >= 0, A subset R, i_A = inf phi over A,
  i_A P(X in A) <= E(phi(X); X in A) <= E phi(X)); E(X; A) notation on the same page.
- p. 30: Remark: some authors call this Markov's inequality and use Chebyshev's for phi(x) = x^2,
  A = {|x| >= a}: a^2 P(|X| >= a) <= EX^2 (1.6.1). No range for a is stated.

Written (body lines 349-560, annex lines 327-602):
- C012: sec:p15-w02c-p15-001-cauchy-schwarz, thm:p15-w02c-p15-001-cauchy-schwarz (+ annex), example
  and boundary warning (a = 0; infinite second moments, concrete case f(u) = u^{-1/2}).
- C017: sec:p15-w02c-p15-001-chebyshev, def:p15-w02c-p15-001-chebyshev-names,
  thm:p15-w02c-p15-001-chebyshev-square (+ annex; a >= 0, centred form, failure for a < 0), example.
- C018: sec:p15-w02c-p15-001-affine-integrals, thm:p15-w02c-p15-001-affine-integral (step-function
  squeeze, no antiderivative), thm:p15-w02c-p15-001-signed-density-values (the three integrals and
  the Jordan-mass integrals), thm:p15-w02c-p15-001-reciprocal-density (nu([1/n,1)) <= n - 1,
  nu((0,a)) = infinity by dyadic pieces). The host's "log n" value is not derived; finiteness is.
- Patches 3-6 in work/waves/w02ca/patches/w02ca-p15-001.json (two host-proof replacements in
  annex:p15.radon-nikodym-examples, two pointers in integration-expectation.tex).
- Duplicate found: w02ca-p15-005 is concurrently writing thm:p15-w02c-p15-005-cauchy-schwarz and
  thm:p15-w02c-p15-005-chebyshev-displays (same Durrett remarks) although it lists this unit as
  readonly; relayed to the lead in crosslink_requests.
- Readonly-unit gaps in the r3 task (measurable-probability, finite-probability,
  conditional-expectation, measure-extension, regular-conditional-laws) relayed, not written (A14).
- Helper scripts: scratchpad folder w02ca-p15-001-r3 (not in the project).

## Round r4 additions (C006, C009, C016 of integration-expectation)

Source re-read this session: same held PDF (source/references/durrett-probability-2019-01-11/PTE5_011119.pdf),
pdftotext -layout into the r4 scratch folder; printed pages from running heads.
- p. 18: sec. 1.4 opening; the integral is defined by a four-step procedure (simple, bounded, nonnegative,
  general); the sequence of steps is also useful for proving integration formulas, see proofs of thms. 1.6.9, 1.7.2.
- pp. 23-24: notation cases (a)-(c) on p. 23, (d) and the remark on sums on p. 24.
- p. 26: convergence in measure defined; on a finite measure space it is a weaker assumption than a.e. convergence.
- p. 32: sec. 1.6.3 opening (computations need a space where calculus can be done; mostly S = R^d); thm. 1.6.9;
  proof by four cases paralleling sec. 1.4, reader asked to note the method. pp. 32-33: cases 3, 4; consequence.
- p. 38: thm. 1.7.2 (Fubini); p. 39: proof by four increasingly general cases.

Written:
- C006: items (5) dG(x) and (6) counting measure / sum_i f(i) in def:p15-w02c-p15-001-dx-notation;
  thm:p15-w02c-p15-001-stieltjes-notation (+ annex), thm:p15-w02c-p15-001-counting-sums (+ annex), example
  def:p15-w02c-p15-001-stieltjes-counting-examples. Patch request 2 text widened to all four notations.
- C016: Durrett's motive added to def:p15-w02c-p15-001-change-of-variables-name; new sec:p15-w02c-p15-001-four-step
  with def:p15-w02c-p15-001-four-step-method (hbmethod) and thm:p15-w02c-p15-001-four-step (+ annex); second
  derivation of the change of variables formula from it in annex:p15-w02c-p15-001-change-of-variables.
  Patch request 1 text extended.
- C009: existing treatment thm:p15-w02c-p15-005-ae-measure (packet w02ca-p15-005, unrouted) found; not duplicated;
  linked in the Relationships paragraph and by new patch request 7 (after def:p15-lp-convergence).
- Symbol intake: 4 new rows (dG/mu_G, #/sum, (i_k)/delta_0, four-step locals).
- Readonly-unit gaps of the r4 task relayed in crosslink_requests (A14), not written.

## Round r5 (integration-expectation C004-C019 gaps; radon-nikodym C011)

Source re-read this session: same held PDF, pdftotext -layout into
tmp/agent-scratch/w02ca-r5-w02ca-p15-001-b1-author/; printed pages from running heads: Exercises 1.5.5 and
1.5.10 p. 28; Figure 1.6 p. 30; Theorem 1.6.8 p. 31; (1.6.3) p. 33; Exercises 1.6.1-1.6.3 p. 35; 1.6.5-1.6.7
p. 36; 1.6.12-1.6.13 p. 37.

Findings: every r5 integration-expectation item not already in this chapter (C004, C005, C009, C014, the rest of
C017, C019) is proved in sec:p15-w02c-p15-005-integration-supplements (packet w02ca-p15-005, with annex proofs and
its own routing and pointer patches). Not duplicated (A9); linked by a new paragraph at the end of the
Relationships paragraph of the body file (lines 824-858). C006, C012, C016 and the (1.6.1) part of C017 are in
this chapter; the assessment found them absent only because the chapter is not routed.

radon-nikodym C011: thm:p15-w02c-p15-003-block-integrals (packet w02ca-p15-003) is the needed trace-integral
lemma. Patch request 8 replaces the sigma-finite assembly paragraph of annex:p15.lebesgue-decomposition with a
version that applies it, sums the blocks by term-by-term integration of nonnegative series, and states the
measurability, measure and null-set steps.

Readonly-unit gaps relayed in crosslink_requests (A14), not written.

## Round r6 (integration-expectation X-IE-exercises; status of C006, C009, C012, C016, C017; radon-nikodym C011)

Source re-read this session: held PDF source/references/durrett-probability-2019-01-11/PTE5_011119.pdf, pdftotext
-layout of physical pages 32-46 into tmp/agent-scratch/w02ca-r6-w02ca-p15-001-b1-author/d.txt; printed pages from
running heads: Exercises 1.5.8-1.5.10 p. 28; Example 1.6.12 (Bernoulli: EX = p, X^2 = X, var = p(1-p)) p. 34;
Exercises 1.6.1-1.6.3 p. 35; 1.6.4-1.6.10 (first part) p. 36; rest of 1.6.10, 1.6.11 (E|X|^k < infinity gives
E|X|^j < infinity and E|X|^j <= (E|X|^k)^{j/k} for 0 < j < k), 1.6.12-1.6.16 p. 37.

Scope note opened (the assessment could not): spec/research/edition-2026-p15-u1-integration-expectation.md states
that the assigned extent pp. 18-37 includes the exercises and that unproved source exercises "retain their own
obligations". So the X-IE-exercises items are owed.

Search: sec:p15-w02c-p15-005-integration-supplements (packet w02ca-p15-005, unrouted) proves 1.5.5/1.6.13, 1.5.8,
1.5.10, 1.6.1-1.6.7, 1.6.9, 1.6.10, 1.6.12, 1.6.14. Not found anywhere: Exercise 1.6.11 and Example 1.6.12.

Written:
- sec:p15-w02c-p15-001-lower-moments (body 803-947): thm:p15-w02c-p15-001-lower-moments (Hoelder with g = 1,
  real orders), thm:p15-w02c-p15-001-lower-moments-limits (counting measure 1/i; X(n) = 2^n under masses 2^{-n}
  via thm:p15-countable-atomic and def:p15-countable-waiting; attainment), def:p15-w02c-p15-001-bernoulli,
  thm:p15-w02c-p15-001-bernoulli-moments (a.s. identities through thm:p15-nonnegative-integral-laws), example
  and warning. Annex 822-953.
- New heading sec:p15-w02c-p15-001-relationships before the chapter's Relationships paragraph; one sentence there
  now names Exercises 1.5.8, 1.6.4, 1.6.9, 1.6.10, 1.6.14 with their w02c-p15-005 theorems and points to the
  new results. Intro Conclusions sentence added (body line 50-52), so body line numbers after 50 moved by +2.
- Symbol intake: 3 rows (j,k,p,q; Bernoulli p,A,N; f,I,B_m,r).

Unchanged: C006, C012, C016 and the (1.6.1) part of C017 are in this chapter; C009 is in w02c-p15-005 (finite
measure spaces); radon-nikodym C011 is patch request 8 (host paragraph still unpatched). All need lead routing.

## Round r7 (integration-expectation C014: worked boundary of Jensen's hypotheses)

Source re-read this session: held PDF source/references/durrett-probability-2019-01-11/PTE5_011119.pdf,
pdftotext -layout of physical pages 33-38 into tmp/agent-scratch/w02ca-r6-w02ca-p15-001-b1-author/j.txt;
printed pages from running heads: Theorem 1.5.1 (Jensen for integrals; mu a probability measure, f and phi(f)
integrable) p. 25; Theorem 1.6.2 (E phi(X) >= phi(EX) provided both expectations exist, i.e. E|X| and
E|phi(X)| finite), the two-point direction check and the special cases |EX| <= E|X|, (EX)^2 <= E(X^2) p. 29;
Figure 1.6 p. 30.

Search: the two-point illustration, Figure 1.6 and the two special cases are in packet w02ca-p15-005
(def:p15-w02c-p15-005-jensen-direction, thm:p15-w02c-p15-005-jensen-special; unrouted). Not found anywhere: a worked
boundary of the probability-normalisation and integrability hypotheses of thm:p15-jensen-integral.

Written: sec:p15-w02c-p15-001-jensen-hypotheses (body 952-1118), annex 955-1123:
thm:p15-w02c-p15-001-jensen-normalization (on a finite measure space the conclusion for all admissible pairs holds iff
mu(Omega) = 1, constant witnesses), thm:p15-w02c-p15-001-jensen-infinite-mass (failure with 1 < mu(A) < infinity,
Lebesgue (0,2]; equality on {0, infinity}-valued measures), thm:p15-w02c-p15-001-jensen-extended (E phi(X) exists in
(-infinity, infinity] and the inequality holds without integrability of phi(X)),
thm:p15-w02c-p15-001-jensen-integrability-limits (masses 3*4^{-n}, X = 2^n: EX = 3, EX^2 = infinity; masses
2^{-|m|-1} on Z\{0}: EX undefined), example def:p15-w02c-p15-001-jensen-mass-example (Figure 1.6 law with masses
1/2, 1, 1/4), warning def:p15-w02c-p15-001-jensen-hypotheses-warning. Intro Conclusions sentence and a Relationships
sentence added. Two symbol-intake rows.

Readonly-unit gaps of the r7 task (finite-probability C001, C010, C013, C014, C016, C019; measurable-probability C006,
C010, C016, C021; measure-extension C005, C007; regular-conditional-laws C005, C011) relayed, not written (A14).

## Round r8, block 2 (integration-expectation C004-C020 gaps)

Source re-read this session: held PDF source/references/durrett-probability-2019-01-11/PTE5_011119.pdf, pdftotext
-layout of physical pages 26 and 30-47 into tmp/agent-scratch/w02ca-r6-w02ca-p15-001-b2-author/; printed pages from
running heads: four-step procedure and its use for integration formulas p. 18; notation cases p. 23, (d) and the
remark on sums p. 24; Exercises 1.5.5, 1.5.8, 1.5.10 p. 28; Theorem 1.6.9 with its title, the Remark on P o h^{-1}
and the four-case proof p. 32; Example 1.6.12 p. 34; Exercises 1.6.1-1.6.3 p. 35; 1.6.4-1.6.9 and the start of
1.6.10 p. 36; the rest of 1.6.10 and 1.6.11-1.6.16 p. 37.

Search: every item in the r8 assessment for integration-expectation is already proved, with annex proofs, either in
this chapter (C006 notation, C008 four-step method, C016 change of variables name and remark, Exercise 1.6.11,
Example 1.6.12) or in sec:p15-w02c-p15-005-integration-supplements (C004, C005, C009, C014, C017, C019 and the other
exercises of C020). Both chapters are still off the input route (p15.tex has no w02c input on 2026-10-12). Not
duplicated (A9).

Written: patch request 9 in work/waves/w02ca/patches/w02ca-p15-001.json, a paragraph for the on-route boundary entry
def:p15-integration-next-boundary that places each named exercise by number at its proving label (C020). C008 and
C020 are now reported as blocked_policy on routing instead of as existing on-route treatments.

Readonly-unit gaps in the r8 task (finite-probability C008, C010, C011, C019; measurable-probability C006, C010,
C011, C014, C016, C017, C018, C021, C024, C025; measure-extension C005, C007, C012; regular-conditional-laws C005,
C007, C011, C012) belong to w02ca-p15-006, -014, -003 and -008; not written (A14).

## Continuation

State after r9 (block 1): no body or annex change; patch request 10 added (pointer after thm:p15-jensen-integral for
C014); unit compile ok (5 overfull annex headers, unchanged); find_fused_spaces clean. Remaining: lead routing of this
chapter and w02c-p15-005 (w02ca-p15-005.json requests 1-2), patch requests 1-10, symbol-intake merge. Readonly-unit
gaps (finite-probability, measurable-probability, measure-extension, regular-conditional-laws) not written (A14).

State after r8 (block 2): no body or annex change; patch request 9 added; unit compile ok (5 overfull annex
headers, unchanged); find_fused_spaces clean; check.py --tree reports nothing in these files. Remaining: lead routing of
this chapter and w02c-p15-005 (w02ca-p15-005.json requests 1-2), patch requests 1-9, symbol-intake merge.

State after r7: sec:p15-w02c-p15-001-jensen-hypotheses written (C014 worked boundary); unit compile ok (5 overfull
annex headers, unchanged); find_fused_spaces clean; check.py --tree reports nothing in these files. Remaining: lead
routing (\input lines for this chapter and w02c-p15-005), patch requests 1-8, symbol-intake merge, readonly relays.

State after r6: Exercise 1.6.11 and Example 1.6.12 written with annex proofs; unit compile ok (5 overfull
annex headers); find_fused_spaces clean; check.py --tree reports nothing in these files. Remaining gaps of the units
this packet owns are lead actions: the \input lines for this chapter and for the w02c-p15-003 and w02c-p15-005
chapters, and patch requests 1-8.

State after r5: no new theorem written; Relationships links and patch request 8 added; unit compile ok
(4 overfull annex headers); find_fused_spaces clean; check.py --tree reports nothing in these files. Every
remaining gap of the units this packet owns is a lead action: the \input lines for this chapter and for the
w02c-p15-003 and w02c-p15-005 chapters, and patch requests 1-8.

State after r4: C006, C009 (by link), C016 addressed in body and annex; unit compile ok (4 overfull annex
headers of 1-4 pt from label length); find_fused_spaces clean; check.py --tree reports nothing in these files.
Open for the lead: the two \input lines (the chapter is still unrouted, which is why route-only assessment
reports C006/C016 as absent), patches 1-7, symbol-intake merge (12 earlier + 4 new rows), the w02ca-p15-005
duplicate, and the readonly-unit relays.


State after r3: C012, C017 (integration-expectation) and C018 (radon-nikodym) written in body and
annex; unit compile ok (4 overfull annex headers of 1-4 pt from label length); find_fused_spaces
clean; check.py --tree reports nothing in these files. Open for the lead: the two \input lines,
patches 1-6, symbol-intake merge (5 new rows), the w02ca-p15-005 duplicate, and the readonly-unit
relays.

State at r2 return: C006 and C016 of ED26-P15-CH-integration-expectation written (body + annex), unit
compile ok (two overfull annex header lines, 1.0 pt and 6.7 pt, from annex label length), find_fused_spaces
clean, check.py --tree shows no finding in these files. Nothing further is open for the units this
packet writes. Open for the lead: insertion of the two \input lines (placement in the return file),
the two patch requests, symbol-intake merge, and rerouting of the readonly-unit gaps listed above.

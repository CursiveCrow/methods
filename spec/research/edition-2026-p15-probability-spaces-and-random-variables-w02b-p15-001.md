# Edition 2026, P15, packet w02b-p15-001: explicit moments, L^p inequalities and integral approximations

Packet: work/waves/w02b/packets/w02b-p15-001.json (P15 chapter 157; sections 157.1-157.4).
Label tag: p15-w02b-p15-001.

## Gap addressed

ED26-P15-CH-integration-expectation-C020. The boundary entry
def:p15-integration-next-boundary (handbook/parts/p15/integration-expectation.tex
lines 424-435) said that Poisson and geometric calculations "retain their
additional statements and proofs" and named no destination.

## Source opened in this session

- source/references/durrett-probability-2019-01-11/PTE5_011119.pdf
  (Durrett, Probability: Theory and Examples, author version 5, 11 January 2019;
  bib key DurrettPTEAuthor2019).
  - PDF p. 42 = book p. 34: Example 1.6.13 (Poisson; factorial moments
    E(X(X-1)...(X-k+1)) = lambda^k for k >= 1; EX = lambda; var X = lambda).
  - PDF p. 43 = book p. 35: Example 1.6.14 (geometric, p in (0,1); EN = 1/p;
    EN(N-1) = 2(1-p)/p^2; var N = (1-p)/p^2; differentiation of the geometric
    series justified by reference to Example A.5.6).
  - PDF pp. 480-481 = book pp. 472-473: Example A.5.6 (statement on p. 472,
    proof on p. 473). It treats the first-derivative series only.
  Page offsets checked by the running heads (PDF 41 shows "33"; PDF 480 shows "472").

## Existing treatments found (A9)

Not in the packet's "existing" list:
- thm:p15-stirling-poisson-premises (handbook/parts/p15/de-moivre-laplace-and-stirling.tex
  lines 205-214; annex handbook/annex/p15/de-moivre-laplace-and-stirling.tex lines 456-493):
  Poisson normalization, mean, E[X(X-1)] and variance. The new chapter cites it for
  normalization and states that it adds every higher factorial order.
- annex:p15.coupon-collector-law (handbook/annex/p15/weak-laws-and-triangular-arrays.tex
  lines 161-186): the geometric mean, E[G(G-1)] and variance by a justified
  differentiation of finite geometric sums, embedded in the coupon-collector proof and
  citing Durrett p. 35. Not a stated body result. The new chapter cites
  thm:p15-coupon-collector-law and uses a different (non-differentiation) proof.
- def:p15-countable-waiting (measurable-probability.tex) is the geometric law with
  p = 1/2; used in the worked example.

## Design decisions

- Proofs avoid term-by-term differentiation: factorial moments reduce to the
  negative-binomial series sum_m C(m+r,r) q^m = p^{-(r+1)}, proved by induction on r
  with the hockey-stick identity and regrouping of a nonnegative double series
  (thm:p15-countable-atomic). Recorded in the reader text as a change from the source.
- Geometric factorial moments are stated for every order r (Durrett states r = 1, 2);
  marked in the reader text as an extension.
- Part (4) of the geometric theorem proves the first-occurrence realization that
  Durrett states informally.
- Notation follows Durrett (lambda, X, N, p, k); expectation and variance use the
  handbook's \mathbb E and \operatorname{Var} for Durrett's E and var, as in the
  integration chapter. q = 1-p is a handbook abbreviation.

## Open items

- The same boundary entry also declares "further approximation exercises" and
  "general L^p space results" with additional statements and proofs. No treatment or
  destination for either was found on the route (search of handbook/parts/p15 for
  Riesz, Minkowski and Durrett Exercises 1.4-1.6 found none). Not supplied here.
- The boundary entry text must be changed to name the new destination; host is
  read-only. Patch request: work/waves/w02b/patches/w02b-p15-001.json.
- Placement: packet proposal (after regular-conditional-laws). A reader would find
  the chapter more naturally directly after integration-expectation; lead's choice.

## Second pass (C018 and the rest of C020)

Gaps named by the assessment and addressed in this pass:
- C018: the induction behind the sums of integers and squares in
  def:p15-computed-expectations was asserted, not written.
- C020: the boundary entry's "further approximation exercises" and
  "general L^p space results" had no destination.

Source pages opened in this pass (same held PDF,
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf; book page =
PDF page - 8, checked by running heads PDF 26 = "18", PDF 32 = "24",
PDF 36 = "28"):
- p. 17 (PDF 25): Exercise 1.3.7, definition of a simple function.
- p. 18 (PDF 26): start of Sec. 1.4, standing assumption that mu is sigma-finite.
- p. 24 (PDF 32): Exercises 1.4.1-1.4.4 (rendered as an image and read).
- p. 28 (PDF 36): Exercises 1.5.1-1.5.10 (rendered as an image and read).

Which "approximation exercises" and "L^p results" were taken (reading of the
boundary promise against the source range pp. 18-37):
- L^p: Exercises 1.5.1, 1.5.2, 1.5.3 -> thm:p15-w02b-p15-001-lp-results parts
  (1)-(3); part (4) adds the vector-space/norm consequences on a general measure.
- Approximation: Exercise 1.4.2 (dyadic level sums), 1.5.7 (truncation; small
  sets), 1.5.9 (simple functions dense in L^p) -> thm:p15-w02b-p15-001-approximations.
- Already on the route, linked not repeated: Ex. 1.4.1
  (thm:p15-nonnegative-integral-laws (1)); Ex. 1.4.3-1.4.4
  (thm:p15-criteria-real-integration); the inequality of Ex. 1.5.1 is also the
  p = 1 case of thm:p15-holder-integral, whose annex proof contains the
  essential-bound argument (not a stated result before this pass).
- Not treated as approximation exercises: 1.5.4-1.5.6, 1.5.8, 1.5.10
  (countable additivity, monotone/series convergence, continuity of an
  indefinite integral). 1.5.4 and 1.5.6 are on the route in
  thm:p15-nonnegative-integral-laws and thm:p15-signed-integral-laws; 1.5.5,
  1.5.8 and 1.5.10 were not searched for in this pass. If the lead reads the
  boundary promise as covering them, they remain open.
- Completeness of L^p is not in the source range and is not asserted.

Variants recorded in reader text: Durrett's essential supremum has no M >= 0
restriction (differs only for the zero measure); his integration section
assumes sigma-finiteness (proofs here do not use it); Ex. 1.5.2 is stated for a
probability measure (extended here to 0 < mu(Omega) < infinity, marked); the
explicit approximants in Ex. 1.5.9 are a handbook choice (marked).

Notation: Lebesgue measure is named in words in the new sections, because
lambda is the Poisson parameter throughout this chapter.

Patch requests (work/waves/w02b/patches/w02b-p15-001.json): (1) the boundary
entry of integration-expectation.tex now names every destination; (2) the
sentence "The finite identities ... follow by induction" in
def:p15-computed-expectations points to thm:p15-w02b-p15-001-uniform-moments.

C022 (measurable-probability) belongs to the read-only unit of w02b-p15-013 and
was not written here. The assessment's needed change: a sentence at
def:p15-cumulative-distribution recording that Durrett calls F_X the
"distribution function" (locator PTE5 p. 10 as given by the assessment; not
reopened in this pass). Passed to the lead as a cross-link request.

## Continuation

- C018: written (thm:p15-w02b-p15-001-uniform-moments with annex proof).
- C020: Poisson/geometric (first pass), L^p results and approximations (this
  pass) written; destination patch requested. Open: the lead's reading of
  whether Exercises 1.5.5, 1.5.8, 1.5.10 fall under "approximation exercises";
  application of the two patches.
- unit-compile ok, overfull 0; fused-space check clean; check.py shows no
  finding in the owned files.
- Other components: existing treatments, not modified.

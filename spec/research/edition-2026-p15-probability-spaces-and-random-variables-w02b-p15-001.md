# Edition 2026, P15, packet w02b-p15-001: Poisson and geometric moment calculations

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

## Continuation

- C020 Poisson and geometric calculations: body and annex written; unit-compile ok,
  overfull 0; fused-space check clean; check.py shows no finding in the new files.
- Remaining for C020: the two other undestinated clauses of the boundary entry (see
  open items) and application of the boundary patch by the lead.
- All other components of the packet: existing treatments in finite-probability.tex,
  integration-expectation.tex and measurable-probability.tex (the last is the
  read-only unit of w02b-p15-013); not modified here.

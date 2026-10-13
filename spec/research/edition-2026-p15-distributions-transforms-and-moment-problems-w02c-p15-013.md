# w02ca-p15-013 (P15, section 160.9): second derivatives, sine product, Pitman attribution

## Provenance

- Packet: work/waves/w02ca/packets/w02ca-p15-013.json; label_tag p15-w02c-p15-013; toc_tag "%% toc: P15 160 160.9"; heading \chapter.
- Task (r2 continuation): close the assessment disputes on ED26-P15-CH-characteristic-functions-and-inversion-C019 and -C021.
  That unit is listed in readonly_units (owner w02c-p15-011). Its host files are read-only, so the owner's text is not edited.
  The missing content is written in this packet's own files, and the links into the hosts are patch requests
  (work/waves/w02ca/patches/w02ca-p15-013.json). This follows the precedent of w02c-p15-012 for C021.
  The lead should check that w02ca-p15-011 does not write a second treatment of the same three items in this wave.
- Held source opened this session: source/references/durrett-probability-2019-01-11/PTE5_011119.pdf (Durrett PTE 5th ed., 2019-01-11).
  Printed page = PDF page - 8. Locators seen: p. 133 (Exercise 3.3.10), p. 134 (Theorem 3.3.18, Lemma 3.3.19),
  p. 135 (Theorem 3.3.20), p. 136 (sentence introducing Theorem 3.3.21; Theorem 3.3.21; Exercises 3.3.13 and 3.3.14 with the
  Pitman/Walsh attribution), p. 481 (reference-list entry: Pitman (1956), On derivatives of characteristic functions at the origin,
  Ann. Math. Statist. 27, 1156-1160). Page 136 was rendered to an image: Exercise 3.3.14(iii) is printed with limit -ia.
  The correct value is ia, which the handbook already uses (thm:p15-criteria-pitman-law, "corrected sign").
- Pitman's paper is not held. It is named only as Durrett reports it, and no content is drawn from it.

## What was written

- C019: thm:p15-w02c-p15-013-second-derivative-moment (existence of phi''(0) gives E X^2 < infinity and phi''(0) = -E X^2,
  with Q(h) -> phi''(0) proved through lemma thm:p15-w02c-p15-013-quotient-limit by Cauchy's mean value step).
  Also: corollary thm:p15-w02c-p15-013-four-conditions ((D), (S), (U) and E X^2 < infinity are equivalent; |t| as the
  non-characteristic-function contrast); worked example def:p15-w02c-p15-013-uniform-second-moment; failure case
  thm:p15-w02c-p15-013-order-contrast (e^{-|t|^alpha}, 1<alpha<2); warning def:p15-w02c-p15-013-order-one.
- C021(b): thm:p15-w02c-p15-013-sine-product (trig derivation, quotient form, limit, non-uniformity on R), corollary
  thm:p15-w02c-p15-013-half-pi, corollary thm:p15-w02c-p15-013-binary-uniform (the identity read backwards).
- C021(a): sec:p15-w02c-p15-013-pitman (Durrett's Pitman 1956 attribution, Walsh's point about part (iii), the reference-list
  entry, where part (iii) sits in annex:p15.criteria-pitman-law, and the printed sign).

## Symbols

Q(h) retained from thm:p15-characteristic-second-moment; u(t) = Re phi(t); P_n(t); c_m. All local; see the intake CSV.
No known overlap needing a decision. P_n is local to sec:p15-w02c-p15-013-sine-product.

## Continuation

C019 and C021 text is written in the owned body (lines 1-270) and annex (lines 1-236). Checks run: find_fused_spaces is clean.
unit-compile reports ok, with 6 overfull boxes and no errors. check.py --tree shows no finding for these files.
Outstanding items for the lead: put the two new files on the input route (insertion proposal in the return file), and apply the
four patch requests. C020 (Hausdorff 1921 and 1923, Heyde 1963) is still blocked on the source. The packet's blocker_ref
ACQ-2026-10-0316 does not name these works, so an acquisition request is needed.

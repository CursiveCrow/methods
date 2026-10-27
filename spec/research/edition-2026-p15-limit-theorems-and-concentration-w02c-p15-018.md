# P15 161.6-161.8 (packet w02ca-p15-018): strong-law rate context and infinite-mean limits

Date: 10 October 2026. Packet w02ca-p15-018, label tag p15-w02c-p15-018.

## Sources opened in this session

- Durrett, Probability: Theory and Examples, Version 5 dated 11 January 2019,
  source/references/durrett-probability-2019-01-11/PTE5_011119.pdf
  (key DurrettPTEAuthor2019). Printed page = PDF page - 8.
  Read: pp. 65-66 (Example 2.2.16 complete, truncation principle, price
  paragraph with the Nicolas Bernoulli 1713 remark and the 2^40 count);
  p. 70 (Theorem 2.3.8 and the start of its proof, including the identity
  S_n/n - S_(n+1)/(n+1) = S_n/(n(n+1)) - X_(n+1)/(n+1));
  pp. 76-77 (Exercise 2.3.20; Theorem 2.4.1 with "Etemadi's (1981) proof";
  Lemmas 2.4.2-2.4.4; the paragraph calling Lemmas 2.4.2-2.4.3 standard and
  stating Etemadi's X_n^+ / X_n^- reduction); pp. 86-89 (Theorem 2.5.10 end,
  Section 2.5.1 opening, Theorem 2.5.11 and Remark citing Theorem 8.5.2,
  Theorem 2.5.12, Section 2.5.2 opening with the St. Petersburg illustration,
  Feller (1946) attribution, no-nonzero-limit sentence and the Theorem 2.3.8
  remark; Theorem 2.5.13 statement and start of proof on p. 89).
- Feller, An Introduction to Probability Theory and Its Applications,
  Vol. II, 2nd ed., source/references/feller-probability-volume2-second-edition/feller-volume2-second-edition.pdf
  (key Feller1971ProbabilityII). Printed p. 236 = PDF p. 251. The page
  image was rendered and read for the fair-game paragraph preceding
  Theorem 2 (reference to Volume 1, Chapter X; participant strongly on the
  losing side; fair entrance fee depending on the number of trials) and the
  sentence reading X_k as gains and a_n as total entrance fee for n trials.

## What was written

New chapter (owned): handbook/parts/p15/limit-theorems-and-concentration-w02c-p15-018.tex
with annex handbook/annex/p15/limit-theorems-and-concentration-w02c-p15-018.tex.

- sec:p15-w02c-p15-018-rate-comparison: Durrett's Section 2.5.1 claim that the
  random-series proof gives rate estimates; the Theorem 2.5.11 Remark (law of
  the iterated logarithm, Theorem 8.5.2) and its conclusion that the rate is
  not far from the best possible; the exact logarithmic gap factor and the
  conditional consequence for denominators bounded by a multiple of the
  iterated-logarithm scale. The law of the iterated logarithm is not proved in
  the handbook; the text says so and does not use it as a premise.
  (ED26-P15-CH-strong-law-rates-and-normalization-C003)
- thm:p15-w02c-p15-018-no-nonzero-limit, thm:p15-w02c-p15-018-linear-scale,
  thm:p15-w02c-p15-018-petersburg-almost-sure, def:p15-w02c-p15-018-dyadic-ranges,
  def:p15-w02c-p15-018-scope, with full annex proofs. Feller (1946)
  attribution as Durrett gives it; no finite nonzero almost-sure limit
  (including outcome-dependent limits); the case a_n = n as Durrett's
  Theorem 2.3.8 (both conclusions, also via the source identity);
  St. Petersburg limsup X_n/(n log_2 n) = limsup S_n/(n log_2 n) = infinity
  almost surely by the second Borel-Cantelli lemma, and again via Feller's
  dichotomy with a_1 = 1, a_n = n log_2 n.
  (ED26-P15-CH-strong-law-rates-and-normalization-C010)

Editable hosts:
- handbook/parts/p15/strong-laws-of-large-numbers.tex, thm:p15-etemadi-strong-law:
  Etemadi 1981 dating, "standard" characterization of Lemmas 2.4.2-2.4.3 with
  the remark on Lemma 2.4.3, and the X_n^+ / X_n^- inspiration.
  (ED26-P15-CH-strong-laws-of-large-numbers-C006)
- handbook/parts/p15/infinite-mean-weak-normalization.tex,
  thm:p15-petersburg-array-calculation: Durrett's truncation principle, plus a
  proved fact that the tail condition forces b_n/n -> infinity and that for
  dyadic levels both conditions hold exactly when K(n) -> infinity; proof added
  at the end of annex:p15.petersburg-array-calculation.
  (ED26-P15-CH-infinite-mean-weak-normalization-C012)
- same file, thm:p15-petersburg-normalizers-and-prices: Durrett's paradox,
  fair price log_2 n per play (10 dollars at n = 1024), Nicolas Bernoulli's
  1713 40-ducat remark (paraphrased, not quoted), 2^40 ~ 10^12 plays; Feller's
  fair-game framing and entrance-fee reading. The handbook's precise meaning of
  "fair" (relative weak limit) is kept beside the reported claims.
  (ED26-P15-CH-infinite-mean-weak-normalization-C013)

Patch requests for the read-only host handbook/parts/p15/strong-law-rates-and-normalization.tex
are in work/waves/w02ca/patches/w02ca-p15-018.json (three items: the C003
sentence in thm:p15-finite-variance-log-rate, the C010 attribution and links
in thm:p15-feller-infinite-mean, and the C003 sentence in
def:p15-rates-next-boundary). Each requires the new chapter on the input route.

Read-only unit ED26-P15-CH-de-moivre-laplace-and-stirling (owner
w02c-p15-011) was not written.

Existing treatments found and extended rather than duplicated:
thm:p15-feller-infinite-mean, thm:p15-rate-calculated-examples item 4 (same
dyadic law, a_n = n), thm:p15-rate-hypothesis-boundaries items 1, 4, 5,
thm:p15-feller-ratio-counterexample, thm:p15-power-rate-necessity (p = 1),
thm:p15-borel-cantelli-second. No prior handbook treatment of Durrett's
Theorem 2.3.8 or Exercise 2.3.20 was found (search for "2.3.8", "2.3.20",
"Petersburg", "iterated logarithm").

## Continuation

Run of 10 October 2026 (after the usage-limit restart). The assessment
items for this packet were C003 and C010 of
ED26-P15-CH-strong-law-rates-and-normalization (route pending) and four
items of the read-only unit ED26-P15-CH-de-moivre-laplace-and-stirling
(owner w02c-p15-011; not written here).

Re-verified this session in the held Durrett Version 5 PDF (text layer,
printed page = PDF page - 8): p. 65 (Example 2.2.16, truncation
principle), p. 66 (price paragraph, Nicolas Bernoulli 1713, 2^40 count),
p. 70 (Theorem 2.3.8 and the identity used in its proof), p. 76
(Exercise 2.3.20; Etemadi's (1981) proof; Lemma 2.4.3 remark), p. 77
("standard" sentence and X_n^+ / X_n^- inspiration), p. 87 (Section 2.5.1
opening, Theorem 2.5.11 and its Remark citing Theorem 8.5.2), p. 88
(Section 2.5.2 opening: St. Petersburg, Feller (1946), no nonzero limit,
Theorem 2.3.8 as a_n = n), p. 89 (Theorem 2.5.13 statement). Feller II
p. 236 (PDF p. 251) fair-game paragraph re-read from the text layer.
Every locator in the owned and edited files matches.

The C003 and C010 content is in the owned chapter, which is not yet on
the input route. The two driver insertions are now patch items 1-2 in
work/waves/w02ca/patches/w02ca-p15-018.json, followed by the three items
for handbook/parts/p15/strong-law-rates-and-normalization.tex (which need
the insertions first). Until the lead applies those driver and host
changes, C003 and C010 remain off the route.

Run r4 of 10 October 2026 (after the second usage-limit restart). The
assessment items routed to this packet were C004, C006 and C014 of
ED26-P15-CH-de-moivre-laplace-and-stirling. That unit is listed in this
packet's readonly_units (owner w02c-p15-011; packet w02ca-p15-011 runs in
the same wave), and its hosts de-moivre-laplace-and-stirling.tex are
read-only here, so nothing was written for it. The owner's file
handbook/parts/p15/distributions-transforms-and-moment-problems-w02c-p15-011.tex
already carries the three items: Feller's numerical record and the 120.01
reconciliation (lines 53-122), the footnote attributions to Stirling 1730,
Robbins 1955 and Wallis / Feller 1967 (lines 120-145), and Durrett's
special-case framing of Theorem 3.1.3 with a proof from the general CLT
(lines 161-216). The owner's return records C004 as partial (the constant of
Feller's printed percentage bound on p. 54 is illegible in its held scan).
Both that file and this packet's chapter still need the lead's driver
insertions to reach the input route. No owned file changed in this run;
unit-compile ok, find_fused_spaces clean, check.py shows no hard finding in
the owned or edited files.

Run r5 of 10 October 2026. Assessment items: C003, C010 and the new C014
of ED26-P15-CH-strong-law-rates-and-normalization (all route pending),
and C004, C006, C014 of the read-only de Moivre--Laplace unit (owner
w02c-p15-011; not written here). Re-read in the held Durrett Version 5
PDF this session: printed p. 70 (Theorem 2.3.8), p. 87 (Section 2.5.1
opening, Theorem 2.5.11 and Remark citing Theorem 8.5.2 with the
"not far from the best possible" conclusion), p. 88 (Section 2.5.2
opening: St. Petersburg, Feller (1946), no nonzero limit, a_n = n case),
p. 89 (Theorem 2.5.13). All locators in the owned chapter match. C014
(the boundary's missing sharpness conclusion) is patch item 5, whose
reason now names C014. All five patch anchors match the current hosts
exactly once. No reader text changed; everything waits on the lead's
driver insertions (patch items 1-2) and then host items 3-5.

Run r6 of 11 October 2026. Assessment items: C003, C010, C014 of
ED26-P15-CH-strong-law-rates-and-normalization (all route pending
because the owned chapter was never input), and C004, C006, C014, C015
of the read-only de Moivre--Laplace unit (owner w02c-p15-011; not
written here). Re-read in the held Durrett Version 5 PDF this session
(text layer, PDF page = printed page + 8): p. 70 (Theorem 2.3.8 and its
proof identity), p. 76 (Exercise 2.3.20), p. 87 (Section 2.5.1 opening,
Theorem 2.5.11, Remark with Theorem 8.5.2 and "not far from the best
possible"), p. 88 (Section 2.5.2 opening: St. Petersburg, Feller (1946),
no nonzero limit, a_n = n), p. 89 (Theorem 2.5.13).

Change of placement: instead of waiting for the driver insertions, the
content was moved, with unchanged labels, into hosts that are already on
the input route and editable by this packet:
- sec:p15-w02c-p15-018-rate-comparison (C003, C014 conclusion) at the end
  of handbook/parts/p15/strong-laws-of-large-numbers.tex (lines 317-365);
- sec:p15-w02c-p15-018-infinite-mean-limits (C010) before
  def:p15-positive-normalization-boundary in
  handbook/parts/p15/infinite-mean-weak-normalization.tex (lines 362-492),
  with the three annex items appended to
  handbook/annex/p15/infinite-mean-weak-normalization.tex (lines 594-740)
  and one pointer sentence in that annex's introduction.
The owned chapter files now carry only the toc tag and comments (the
body also a \nocite so that the scoped unit build has a citation for
biber); they should not be input. Patch items 1-2 (driver insertions)
were withdrawn; the three items for strong-law-rates-and-normalization.tex
remain (all anchors match once) and now need no driver change. C014
stays blocked_policy only for the read-only continuation entry
def:p15-rates-next-boundary (patch item 3).
Checks: unit-compile ok; scratch build of both hosts' bodies and annexes
without TeX errors (all undefined references are labels in other routed
P15 files); find_fused_spaces clean; check.py shows only pre-existing
notation-scope notes in the edited hosts.

Run r6 block 2 of 11 October 2026. Assessment items routed here: C004,
C006 and C014 of the read-only unit ED26-P15-CH-de-moivre-laplace-and-stirling
(owner w02c-p15-011). Under the packet's readonly_units rule nothing was
written for them, and the de Moivre hosts are read-only for this packet.
Checked the owner's file
handbook/parts/p15/distributions-transforms-and-moment-problems-w02c-p15-011.tex
against the three assessment texts:
- Present there: Stirling 1730 (p. 52 n. 14), Robbins 1955 for (9.6)-(9.10)
  and (9.14) (p. 53 n. 15), Wallis and Feller 1967 (p. 53 n. 16), the (9.15)
  ratio comparison with 1-(12n^2)^{-1}, 2.0007 at n = 2 and 120.01 at n = 5
  (lines 96-101, 104-145); the full p. 52 numerical record 0.9221, 1.919,
  8/4/2 per cent, 3,598,600 vs 3,628,800 at 0.8 per cent, 0.08 per cent for
  100! (lines 54-101); Durrett pp. 113, 115 special-case framing of
  Theorem 3.1.3 with a CLT proof (lines 161-216).
- Not present in the owner's file or the de Moivre host (grep this run):
  (a) Feller p. 53: the constant's proof is elementary, independent of
  chapters IV-VI, and postponed to VII.2 because it connects naturally with
  the normal approximation theorem; (b) Feller pp. 52-53: d_n motivated as
  comparing log n! with a quantity near the arithmetic mean of the extreme
  members of (9.5); (c) Feller p. 52 evaluative claims: invaluable for
  theory, excellent numerical approximations, the percentage error is what
  really matters, remarkably accurate even for small n (the owner text has
  only "the percentage error decreases steadily and is already small for
  small n"); (d) the numerical constant of Feller's printed n^{-2} per cent
  bound on p. 54 (the owner reports it illegible in its held scan).
- Route: the owner's file is still not input by handbook/parts/p15.tex or
  handbook/annex/p15.tex, so none of its content is on the route.
These are for the owner packet w02ca-p15-011 and the lead (driver
insertion of the owner's files). No owned or host file changed in this
run. unit-compile ok; find_fused_spaces clean on the owned and edited
files.

Run r6 block 3 of 11 October 2026. Assessment items routed here: C004
(items 1-4), C006, C014 and C015 of the read-only unit
ED26-P15-CH-de-moivre-laplace-and-stirling (owner w02c-p15-011,
classified lead_owned by the assessment). Under readonly_units nothing
was written for them; the de Moivre hosts are read-only here and a patch
request carrying that unit's content would be writing its components.
State rechecked this run: the owner's files
distributions-transforms-and-moment-problems-w02c-p15-011.tex (body and
annex) are unchanged since 10 October and still not input by
handbook/parts/p15.tex or handbook/annex/p15.tex; grep of the owner body
and the de Moivre body finds no text for C004 item 4 (Feller pp. 52-53:
d_n motivated by comparing log n! with a quantity near the arithmetic
mean of the extreme members of (9.5), simplest (n+1/2) log n - n) nor for
Feller's evaluative claims on p. 52 (invaluable; excellent numerical
approximations; percentage error is what matters; remarkably accurate
for small n). These remain for the owner packet w02ca-p15-011 and for
the lead's driver insertion of the owner's files; the C015
proof-boundary continuation sentence (CLT special-case relation) is in
the read-only de Moivre body and also belongs to the owner.
Own units: no change. All three patch anchors in
work/waves/w02ca/patches/w02ca-p15-018.json still match their host
exactly once; find_fused_spaces clean on the five edited .tex files;
unit-compile reports no errors.

Run r6-b1 of 12 October 2026. Assessment items routed here: C004
(items i-iv), C006 and C014 of the read-only unit
ED26-P15-CH-de-moivre-laplace-and-stirling (owner w02c-p15-011, packet
w02ca-p15-011; the assessment itself labels each item lead-owned).
Nothing written for them: the unit is in this packet's readonly_units and
its hosts parts/annex p15/de-moivre-laplace-and-stirling.tex are
read-only here; writing the items into this packet's owned chapter would
be a second treatment of a unit owned elsewhere.
State rechecked this run: the owner files
distributions-transforms-and-moment-problems-w02c-p15-011.tex (body
modified 10 October 15:29, annex 10 October 15:22) are unchanged and
still not input by handbook/parts/p15.tex or handbook/annex/p15.tex
(both drivers last modified 5 October). Owner body carries C004 (i)-(iii)
at lines 124-141 (Stirling 1730 n. 14; Robbins 1955 n. 15; Wallis and
Feller 1967 n. 16), C014 at lines 54-122 (0.9221, 1.919, 8/4/2 per cent,
3,598,600 vs 3,628,800 at 0.8 per cent, 0.08 per cent for 100!,
1-(12n^2)^{-1}, 2.0007, the 120.01 vs 120.003 reconciliation), C006 at
lines 161-186. Absent from every handbook file (grep for "VII",
"elementary", "postpon", "independent of"): C004 item (iv), Feller
p. 53's reason for postponing the constant to VII.2 (natural connection
with the normal approximation theorem) and his remark that the proof is
elementary and independent of Chapters IV-VI; the owner body line 137
says only that the constant is determined in VII.2 by a probabilistic
argument.
Exact changes needed (lead): input
parts/p15/distributions-transforms-and-moment-problems-w02c-p15-011 in
handbook/parts/p15.tex and annex/p15/distributions-transforms-and-moment-problems-w02c-p15-011
in handbook/annex/p15.tex (placement per the owner's return); owner
w02ca-p15-011: add C004 item (iv).
Own units: no change. unit-compile: no errors; find_fused_spaces clean on
the five edited .tex files; check.py shows only pre-existing
notation-scope notes for mathbb E / mathbb P in the edited hosts.

Run r6-b2 of 12 October 2026. Assessment items routed here: C004 (items
a-f), C006, C014 and C015 of the read-only unit
ED26-P15-CH-de-moivre-laplace-and-stirling (owner w02c-p15-011, packet
w02ca-p15-011). Nothing written for them: the unit is in this packet's
readonly_units, its hosts parts/annex p15/de-moivre-laplace-and-stirling.tex
are read-only here, and writing the items into an editable routed host
of this packet would be a second treatment of a unit owned elsewhere.
No POL- record in blockers.jsonl governs this unit.
State rechecked: owner files distributions-transforms-and-moment-problems-w02c-p15-011.tex
(body 10 October 15:29, annex 10 October 15:22) unchanged; drivers
handbook/parts/p15.tex and handbook/annex/p15.tex (5 October) still do
not input them. The owner's patch file work/waves/w02ca/patches/w02ca-p15-011.json
already requests the C006/C015 continuation sentence in the read-only
de Moivre body (anchor "remain the next distinct source presentations."),
pointing to thm:p15-w02c-p15-011-dml-from-clt and
sec:p15-w02c-p15-011-feller-record. Owner body carries C004 (a)-(c), (f),
C014 and C006; still absent from every handbook file: C004 (d) (Feller
p. 53: constant's proof elementary, independent of chapters IV-VI,
postponed to VII.2 for its link with the normal approximation) and (e)
(Feller pp. 52-53: why d_n is chosen); the numerical constant of the
p. 54 n^-2 per cent bound is reported illegible by the owner.
Exact changes needed (lead): input
parts/p15/distributions-transforms-and-moment-problems-w02c-p15-011 in
handbook/parts/p15.tex after parts/p15/distributions-transforms-and-moment-problems-w02b-p15-012
and annex/p15/distributions-transforms-and-moment-problems-w02c-p15-011 in
handbook/annex/p15.tex after annex/p15/distributions-transforms-and-moment-problems-w02b-p15-012
(owner's insertion proposal), then apply the owner's de Moivre host patch;
owner w02ca-p15-011: add C004 (d) and (e).
Own units: no change. unit-compile ok; find_fused_spaces clean on the five
edited .tex files; check.py shows only pre-existing notation-scope notes
for mathbb E / mathbb P in the edited hosts.

Run r6-b3 of 12 October 2026. Assessment items routed here: C004 (i)-(iv),
C014 and C015 of the read-only unit ED26-P15-CH-de-moivre-laplace-and-stirling
(owner w02c-p15-011, packet w02ca-p15-011, which is not in run r6).
Nothing written for them (readonly_units; de Moivre hosts read-only here;
no POL- record governs the unit). State: owner files unchanged since
10 October; handbook/parts/p15.tex and handbook/annex/p15.tex (5 October)
still do not input them.
Verified this run in held sources: Feller I third edition VII.2,
pp. 180-181 (PDF pp. 195-196): (2.3)-(2.5) with error below k^3/nu^2 for
0 < k < K_nu under (2.4), (2.7) "valid when nu -> infinity and k < K_nu",
footnote 3 on the constant; Durrett V5 p. 113 (PDF p. 121): chapter
opening on special cases by elementary computations, and S_n read as the
winnings from betting 1 dollar on a fair coin.
Present in the owner body: C004 (i) (lines 124-147), part of (iii)
(lines 96-101), all C014 figures (lines 53-122), C015 special-case
relation (lines 161-171).
Absent from every handbook file (owner w02ca-p15-011 to write):
C004 (ii) Feller pp. 52-53 justificatory claims (invaluable tool; d_n
choice from the arithmetic mean of the extreme members of (9.5); constant
proof elementary, independent of chapters IV-VI, postponed to VII.2);
C004 (iii) the numeric constant of the p. 54 n^-2 per cent bound
(obscured in the held scan per the owner); C004 (iv) the K_nu-range
version of (2.5)/(2.7) with its annex proof; C015 Durrett's winnings
reading of S_n.
Lead: input the owner chapter (owner patch entries 6-7) and apply the
owner's de Moivre host patch.
Own units: no change.

Run r6 block 1 of 13 October 2026. Assessment items routed here: C004
(i)-(iv), C006 and C014 of the read-only unit
ED26-P15-CH-de-moivre-laplace-and-stirling (owner w02c-p15-011; the
assessment labels each item lead-owned). Packet w02ca-p15-011 is not a
lane of args-r6.json, so the owner does not run in this round. Nothing
written for the unit: it is in this packet's readonly_units, its hosts
parts/annex p15/de-moivre-laplace-and-stirling.tex are read-only here,
and no POL- record in blockers.jsonl governs it.
State rechecked: owner files distributions-transforms-and-moment-problems-w02c-p15-011.tex
(body 10 October 15:29, annex 10 October 15:22) unchanged; drivers
handbook/parts/p15.tex and handbook/annex/p15.tex (5 October 02:08) still
do not input them; de Moivre body unchanged since 8 September.
Verified this run in the held Feller I third edition
(source/references/feller-probability-volume1-third-edition/feller-volume1-third-edition.pdf,
printed page = PDF page - 15): p. 52 (PDF 67) footnote 14 (Stirling,
Methodus differentialis, 1730), the numerical record 0.9221, 1.919,
118.019, 8/4/2 per cent, 3,598,600 against 3,628,800 at 0.8 per cent,
0.08 per cent for 100!; p. 53 (PDF 68) footnote 15 (Robbins, Amer. Math.
Monthly 62 (1955), pp. 26-29, for the argument and (9.14)), footnote 16
(usual proof via Wallis; Feller's direct proof, Amer. Math. Monthly
(1967)), and the sentence for C004 (iv): the identity e^C = sqrt(2 pi) is
proved in VII,2; the proof is elementary and independent of chapters
IV-VI, and it is postponed to chapter VII because of its natural
connection with the normal approximation theorem; p. 54 (PDF 69) the
(9.15) remarks (ratio near 1 - (12n^2)^-1, right member overestimates,
2.0007 at n = 2, 120.01 at n = 5; the constant in the n^-2 per cent bound
is garbled in the text layer).
Exact changes needed (lead): input
parts/p15/distributions-transforms-and-moment-problems-w02c-p15-011 in
handbook/parts/p15.tex and annex/p15/distributions-transforms-and-moment-problems-w02c-p15-011
in handbook/annex/p15.tex (owner's insertion proposal), apply the
owner's de Moivre host patch (work/waves/w02ca/patches/w02ca-p15-011.json),
and have the owner add C004 (iv) from Feller p. 53 as recorded above
(the owner body line 137 says only that the constant is determined in
VII.2 by a probabilistic argument).
Own units: no change. The three patch anchors in
work/waves/w02ca/patches/w02ca-p15-018.json still match their host once.

Run r6 block 2 of 13 October 2026. Assessment items routed here: C004
(Feller II.9 justificatory claims) and C014 (Feller's normative claim on
percentage error) of the read-only unit
ED26-P15-CH-de-moivre-laplace-and-stirling (owner w02c-p15-011, packet
w02ca-p15-011, closed as drafted in r5 and not running again in this
wave). Nothing written for them: the unit is in this packet's
readonly_units, its hosts and the owner's files are read-only here, and
no POL- record governs it.
Re-verified in the held Feller I third edition (text layer, PDF pp. 67-68
= printed pp. 52-53): p. 52, Feller's judgement that the absolute
difference in (9.1) is unbounded but the percentage error is what really
matters; pp. 52-53, (9.5) suggests comparing log n! with a quantity near
the arithmetic mean of its extreme members, the simplest being
(n+1/2) log n - n, hence d_n of (9.6); p. 53, e^C = sqrt(2 pi) is proved
in VII,2, the proof is elementary and independent of chapters IV-VI, and
is postponed to VII only for its natural tie to the normal approximation
theorem (footnote 16: Wallis; Feller, Amer. Math. Monthly 1967).
Still absent from every handbook file (grep this run): the d_n
motivation, the e^C independence claim and its reconciliation with the
handbook's use of the chapter VI tail estimate
(thm:p15-stirling-tail-premises), and Feller's percentage-error judgement
(owner body lines 88-92 and warning lines 149-159 give only the
distinction and the opposite caution).
Since the owner packet is closed, these need the lead: write them in the
owner's file during integration, or move the unit out of this packet's
readonly_units so it can write them in a later run.
Guard G1 (spec/research/edition-2026-authoring-batch-intake-13.json): the
only change to that file is lead commit 6de06cc3 (13 October 07:09); the
working tree is clean against HEAD for it and this packet never wrote it.
Own units: no change. unit-compile ok; find_fused_spaces clean on the
five edited .tex files.

Run r6 block 3 of 13 October 2026. Assessment items routed here: C004
(three items), C014 and C015 of the read-only unit
ED26-P15-CH-de-moivre-laplace-and-stirling (owner w02c-p15-011; packet
w02ca-p15-011 closed). Change of approach: since the owner will not run
again and its hosts parts/annex p15/de-moivre-laplace-and-stirling.tex are
in this packet's readonly_hosts, the missing text is now supplied through
the A8 channel as ready-to-apply patch items 4-9 in
work/waves/w02ca/patches/w02ca-p15-018.json (items 1-3, for
strong-law-rates-and-normalization.tex, unchanged). No host file was
edited; the lead decides whether to apply them.
- Item 4 (annex, insert after "The improper integral at zero ..."): Feller
  pp. 52-53 justification of (n+1/2) log n - n from (9.5), with a proof
  that it stays within distance one of the midpoint of an interval whose
  width log(n+1)+n log(1+1/n) is unbounded.
- Item 5 (annex, replace "We now discharge the constant referral ..."):
  Feller p. 53 (proof of e^C = sqrt(2 pi) elementary, independent of
  chapters IV-VI, deferred to VII for its connection with the normal
  approximation theorem); VII.2 p. 180 n. 3 (pi in (2.6) replaced by an
  unknown constant; tail estimate VI,(3.5) against VII,(1.8)); the
  independence claim is reconciled with that footnote's use of VI,(3.5),
  which thm:p15-stirling-tail-premises proves directly.
- Item 6 (annex, replace from "Fix \(0<M<\infty\)" to "to zero."): full
  range (2.4): |E_{n,k}| <= (2k^3+k)/(3n^2) <= k^3/n^2 for 0 <= k <= n/2;
  K_n <= n/2 eventually; (2.5) and (2.7) uniformly on |k| < K_n with the
  constant unknown; the bounded-x statement as the case K_n = M sqrt(n)+1.
- Item 7 (body, thm:p15-stirling-with-remainder route paragraph): states
  the three Feller points and the full-range ratios.
- Item 8 (body, after thm:p15-stirling-worked-boundaries): Feller p. 52
  normative claim (marked 8-word quotation), why every approximation in
  the chapter is relative (only n!/A_n = e^{r_n} enters).
- Item 9 (body, def:p15-stirling-continuation): the II.9 / VII.2 promise
  made specific.
Verified this run in the held Feller I third edition (PDF page = printed
page + 15): pp. 52-54 (PDF 67-69; text layer) and pp. 180-181 (PDF
195-196; rendered images): (2.3)-(2.7), footnote 3, the sentence after
(2.7) on the K_nu range and the order-sqrt(nu) use, (1.8) in VII.1 p. 179.
Checks: all six anchors match their host exactly once; the patched copies
of both hosts (tmp/agent-scratch/w02ca-r6-w02ca-p15-018-b3-author/) build
with the handbook preamble without TeX errors or undefined citations (one
undefined reference, thm:p15-weak-elementary-asymptotics, is a label in
another routed file and was already used by the host); no new overfull
box; find_fused_spaces clean on both patched copies; unit-compile ok;
check.py shows only the pre-existing notation-scope notes. Symbol intake:
row for K_n added (conditional on items 4-9 being applied).

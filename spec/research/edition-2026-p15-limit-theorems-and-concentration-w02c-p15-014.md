# w02ca-p15-014 — P15 161.1 (label tag `p15-w02c-p15-014`)

Heading level `\chapter`; toc tag `%% toc: P15 161 161.1`.

## Files

- Body: `handbook/parts/p15/limit-theorems-and-concentration-w02c-p15-014.tex`
- Annex: `handbook/annex/p15/limit-theorems-and-concentration-w02c-p15-014.tex`
- Symbol intake: `handbook/registry/symbols-intake-p15-limit-theorems-and-concentration-w02c-p15-014.csv`
- Patch requests: `work/waves/w02ca/patches/w02ca-p15-014.json` (item (6) of
  `thm:p15-w02b-p15-013-comparison`, the matching chapter summary and annex
  line in the w02b-p15-013 files; the two driver `\input` lines).
- No intake bib: only `DurrettPTEAuthor2019`, already in `handbook/bib/handbook.bib`.

## Source reading (this session)

Held file opened: `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`
(Durrett, *Probability: Theory and Examples*, author version 5, 11 January 2019),
extracted with pdftotext -layout; printed page numbers read from the running heads
and form-feed page breaks.

| Locator written | Content checked |
|---|---|
| sec. 1.1, p. 1 | sigma-field = (nonempty) collection closed under complements and countable unions; countable = finite or countably infinite; countable intersections via De Morgan; omitted from the definition to make it easier to check |
| sec. 1.3, p. 15 | results developed for random elements of an arbitrary (S,S) because most hold there with the same, sometimes easier, proofs |
| Exercise 1.4.3, p. 24 | simple-function, interval and continuous approximation of integrable g on R |
| Theorem 4.6.3, p. 245 | hypothesis E|X_n| < infinity for all n; with X_n -> X in probability, UI <=> L^1 <=> E|X_n| -> E|X| < infinity |
| Theorem 4.6.9 and continuation, pp. 247-248 | Chung's line (obvious or incredible), the two arguments, Kolmogorov 0-1 law, closing evaluation (very useful) |
| Exercise 4.6.3, p. 249 | step-function approximation from the dyadic martingale; remark: much simpler than Exercise 1.4.3's bare-hands approach but uses a lot of machinery |
| app. A.1, p. 456 | pi-system definition; example: rectangles (a1,b1]x...x(ad,bd] form a pi-system |

Durrett gives no bibliographic reference for the Chung line at p. 247 (his
bibliography lists Chung 1974, but the line is not tied to it); the text says
so and quotes only six words.

## Duty-to-text map

| Duty | Where | Labels |
|---|---|---|
| 161.1 MP-0 probability-to-mean comparison | body 36-187, annex 3-169 | def:p15-w02c-p15-014-reading, thm:p15-w02c-p15-014-probability-mean (annex:p15-w02c-p15-014-prob-mean), def:p15-w02c-p15-014-method, def:p15-w02c-p15-014-worked, def:p15-w02c-p15-014-limits |
| MP-C001 nonempty variant, equivalence, justification | body 189-223, annex 171-187 | thm:p15-w02c-p15-014-sigma-field-variant (annex:p15-w02c-p15-014-field) |
| MP-C011 generality justification | body 224-238 | def:p15-w02c-p15-014-target-generality |
| MP-C020 half-open rectangles pi-system | body 240-268, annex 189-237 | thm:p15-w02c-p15-014-half-open-rectangles (annex:p15-w02c-p15-014-rectangles) |
| UI-C011 Chung, obvious/incredible, evaluation | body 270-318 | def:p15-w02c-p15-014-levy-readings |
| UI-C015 Exercise 4.6.3 remark + pointer to Exercise 1.4.3 | body 320-343 | def:p15-w02c-p15-014-dyadic-price |
| MP-C006, C010, C014, C016, C017 | not written here: existing treatment in w02c-p15-002 files (see below) | linked in body 345-366 |
| WCL-C005 | readonly unit (owner w02c-p15-004) | not written |

MP-0 content: item (1) tail UI of |X_n-X|^p with no moment hypothesis (both
directions), item (2) with X_n in L^p for all n (both directions, X in L^p),
item (3) with X in L^p, item (4) sufficiency and the two models X_n=X=Y_p and
X_1=Y_p, X_n=0 (Y_p = Y^{1/p}, Y from model (5) of the w02b countermodels,
E Y = infinity proved there). The p = 1 case of (2) is Durrett Theorem 4.6.3,
which carries the E|X_n| < infinity hypothesis. Items (1), (3), (4) and p != 1
are handbook extensions with full annex proofs.

## Existing treatments found

- Listed and used: measurable-probability, uniform-integrability-and-conditional-limits,
  conditional-expectation, integration-expectation files (labels cited in the body).
- Not listed in the packet "existing" list:
  - `handbook/parts/p15/probability-spaces-and-random-variables-w02c-p15-002.tex`
    and its annex (sibling packet w02ca-p15-002, untracked, not on the P15 route):
    `def:p15-w02c-p15-002-astragali` (MP-C006), `thm:p15-w02c-p15-002-generator-variants`
    (MP-C010), `def:p15-w02c-p15-002-indicator-terminology` (MP-C014),
    `def:p15-w02c-p15-002-extended-line`, `thm:p15-w02c-p15-002-order-borel`,
    `thm:p15-w02c-p15-002-domain-extension` (MP-C016),
    `thm:p15-w02c-p15-002-convergence-set` (MP-C016/C017). Their content matches
    the assessed gaps; not duplicated here. Ownership tension: packet w02ca-p15-002
    lists ED26-P15-CH-measurable-probability as readonly with owner w02c-p15-014,
    yet wrote these; its research note asks the lead to check duplication. The lead
    must either input those files on the route or have this packet write the items.
  - `thm:p15-w02b-p15-013-vitali`, `thm:p15-w02b-p15-013-countermodels`,
    `thm:p15-w02b-p15-013-power`, `thm:p15-w02b-p15-013-as-probability`
    (w02b-p15-013 chapter; reused).
  - `thm:p15-criteria-real-integration` (characteristic-function-criteria-and-moments.tex):
    the handbook's proof of Exercise 1.4.3.
  - `thm:p15-extinction-or-escape` (Exercises 4.6.4-4.6.5), `thm:p15-levy-upward`,
    `thm:p15-conditional-basic`, `thm:p15-conditional-existence`.


## Run r3 additions (resumed session, 10 October 2026)

Additional pages opened in the held PDF this session (text extraction and rendered
page images): pp. 3, 4, 10, 13, 15, 16, 117, 248.

| Locator written | Content checked |
|---|---|
| sec. 1.1, p. 3 | bold R^d = real d-vectors; script R^d = Borel sets, smallest sigma-field containing the open sets; superscript dropped when d = 1 |
| sec. 1.1, p. 4; Example 1.1.6 | "algebra (or field)": A,B in A implies A^c and A union B in A (no nonemptiness stated); intersection via De Morgan; sigma-algebra is an algebra; Z finite/cofinite example |
| sec. 1.2, p. 10 | random variable: X^{-1}(B) in F for every B in script R |
| Example 1.2.8, p. 13 | "Point mass at 0": F(x)=1 for x>=0, 0 for x<0; discrete = countable S with P(S^c)=0; simplest discrete example |
| sec. 1.3, p. 15 | random vector into (R^d, script R^d), d>1 |
| p. 16 | Theorem 1.3.5 f:(R^n, script R^n) -> (R, script R); Theorem 1.3.6 open set {x: x1+...+xn<a} in script R^n |
| sec. 3.2, p. 117 | mu_n = a point mass at 1/n |
| Theorem 4.6.10, p. 248 | title "Dominated convergence theorem for conditional expectations"; hypotheses and a.s. conclusion |
| Exercise 4.6.1, p. 248 | Z_i i.i.d. E|Z_i|<inf, theta independent finite mean, Y_i=Z_i+theta; normal(0,1) reading; prior distribution, posterior distribution P(theta in . | Y_1..Y_n); show E(theta|Y_1..Y_n) -> theta a.s. |

| Gap | Where | Labels |
|---|---|---|
| MP-C001 field name (p. 4) | body lemma items (2)-(3) + paragraph; annex field proof (2)-(3) | thm:p15-w02c-p15-014-sigma-field-variant |
| MP-C009 script R^d | body | def:p15-w02c-p15-014-borel-notation |
| MP-C018 point mass as a law, Example 1.2.8, p. 117 usage | body + annex | def:p15-w02c-p15-014-point-mass-law, thm:p15-w02c-p15-014-point-mass-law (annex:p15-w02c-p15-014-point-mass) |
| UI-C012 source title of Thm 4.6.10 | body | def:p15-w02c-p15-014-conditional-dominated |
| UI-C016 Exercise 4.6.1 statistical reading, prior/posterior | body + annex | def:p15-w02c-p15-014-prior-posterior, thm:p15-w02c-p15-014-posterior-mean (annex:p15-w02c-p15-014-posterior-mean) |
| MP-C006, C010, C011 (X in F), C012 ({X<q} test), C014, C016, C017, C021 | existing text in the w02c-p15-002 chapter (off route); linked from the relationships section, not duplicated | see that chapter's labels |

Note on Durrett p. 4: his algebra definition omits nonemptiness; the empty collection
satisfies the closure conditions vacuously. Recorded in the lemma, item (3).

## Run r4 b1 additions (10 October 2026)

Held file reopened: `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`;
text extraction plus rendered images of PDF pages 10, 257, 464 (printed pp. 2, 249, 456);
text of printed pp. 250 and 457 read from the extraction.

| Locator written | Content checked |
|---|---|
| Theorem 1.1.1, p. 2 | (ii) **subadditivity**: A subset of union A_m implies mu(A) <= sum mu(A_m); all sets assumed in F; proof via A'_n = A_n cap A, B_n disjointed |
| sec. 4.7, p. 249 | **backwards martingale** (some authors call them reversed); indexed n <= 0, increasing F_n, E(X_{n+1}|F_n)=X_n for n <= -1; claim: sigma-fields decrease as n to -inf, so convergence theory particularly simple |
| Theorem 4.7.1, pp. 249-250 | proof: upcrossing inequality on X_{-n},...,X_0 bounded by E(X_0-a)^+; X_n = E(X_0|F_n) gives UI (Thm 4.6.1) and L^1 (Thm 4.6.3) |
| app. A.1, Theorem A.1.4, p. 456 | "Dynkin's pi-lambda theorem", key to uniqueness, used many times; lambda-system conditions; statement sigma(P) subset L; no reference to a Dynkin work at that point |

| Gap | Where | Labels |
|---|---|---|
| MP-C005 subadditivity, covering form | body 253-312, annex 220-265 | thm:p15-w02c-p15-014-covering-subadditivity (annex:p15-w02c-p15-014-covering), def:p15-w02c-p15-014-covering-example |
| MP-C021(a) Dynkin attribution | body 383-399 | paragraph after thm:p15-w02c-p15-014-half-open-rectangles |
| UI-C019 reversed name and justification | body 622-670 | def:p15-w02c-p15-014-reversed-martingales |
| MP-C018 =d notation | linked: def:p15-w02c-p15-002-equal-in-distribution (off route) | relationships section |

Symbol intake: rows 6 and 14 quoted (glyphs with commas); three rows added.

## Continuation

Status at return (r4 b1):

- Writable gaps from the r4 assessment written here: MP-C005, MP-C021(a), UI-C019.
- Route-pending items (MP-C001, C009, C018 point-mass part, C020, UI-C011, C012, C015, C016, and
  the new C005, C021(a), UI-C019 text) depend on the lead inputting this chapter and its annex
  (patch requests in work/waves/w02ca/patches/w02ca-p15-014.json).
- MP-C006, C010, C011 (X in F), C012, C014, C016, C017, C018 (=d), C021(b): only treatment is in
  handbook/parts/p15/probability-spaces-and-random-variables-w02c-p15-002.tex (off route); lead
  decision needed: input that chapter or assign the text here. Not duplicated.
- WCL components: readonly unit (owner w02c-p15-004); not written.
- Checks (r4 b1): unit-compile ok, 0 overfull; find_fused_spaces clean; check.py --tree handbook
  shows no finding mentioning the owned files.

## Run r5 b1 (11 October 2026)

The r5 assessment names only route items (MP-C001, C006, C009, C010, C011, C012, C014, C016,
C017, C018, C020, C021, C024; UI-C011, C012, C015, C016, C019; WCL-C005, C008, C022).
No body or annex text changed. Added patch request 6 in work/waves/w02ca/patches/w02ca-p15-014.json:
the routed sentence "a point mass is a number" (measurable-probability.tex lines 369-370) gets the
source usage and a pointer to def:p15-w02c-p15-014-point-mass-law (MP-C018); apply with the driver inputs.
MP-C024 (Example 1.2.8) is written in def:p15-w02c-p15-014-point-mass-law and its lemma (body 407-466,
annex 317-402); route only. WCL items: readonly unit (owner w02c-p15-004).

## Continuation (r5 b1)

- Own text needing only the route (driver patch requests 4-5): MP-C001, C005, C009, C018, C020, C021(a),
  C024; UI-C011, C012, C015, C016, C019.
- Needing the w02c-p15-002 chapter on the route (patches in w02ca-p15-002.json): MP-C006, C010,
  C011(c), C012, C014, C016, C017, C021(b). Not duplicated here.
- Checks r5 b1: unit-compile ok, 0 overfull; find_fused_spaces clean; check.py filtered clean.

## Run r5 b2 (11 October 2026)

- G14 fixed: body line 402 "admitted" replaced by "allowed".
- UI-C009, UI-C010: the two identification proofs in the read-only UI annex checked only Omega,
  complements and disjoint unions. Patch requests (indices 6-7 of work/waves/w02ca/patches/w02ca-p15-014.json)
  replace those sentences with direct checks of def:p15-pi-lambda (Omega in every F_n; proper
  differences by subtraction of finite integrals; increasing unions by dominated convergence).
- MP-C025 (1): patch request index 8 names thm:p15-premeasure-extension in the boundary; the
  w02ca-p15-002 request on the same boundary covers the other three theorems and (2) the R^d measures.
- No source reread needed this block (no new locators written).

## Continuation (r5 b2)

- Lead: apply patch indices 3-4 (driver inputs), 5-8 (routed hosts), and the w02ca-p15-002 driver
  requests. Everything else in the r5 assessment is route-only.
- Checks r5 b2: unit-compile ok, 0 overfull; find_fused_spaces clean; check.py filtered clean.

## Run r5 b3 (11 October 2026)

Held file reopened: `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`
(pdftotext -layout; printed page = PDF page - 8). Pages read: printed pp. 1, 15, 16, 17, 244, 245.

| Locator written | Content checked |
|---|---|
| sec. 1.1, p. 1 | without P, (Omega, F) is a measurable space, glossed as a space on which a measure can be put |
| Theorem 1.3.5, p. 16 | X_1..X_n random variables, f: (R^n, script R^n) -> (R, script R) measurable => f(X_1..X_n) random variable; proof via product sets A_1x...xA_n generating script R^n and Theorem 1.3.1 |
| p. 16 | sentence before 1.3.5: the next result shows why Theorem 1.3.4 was proved for measurable maps |
| Theorem 1.3.6, p. 16 | sums, via 1.3.5 |
| sec. 4.6, p. 244 | UI defined for a collection X_i, i in I, no integrability hypothesis; M with sup < 1 gives sup E|X_i| <= M+1 < infinity; remark used several times below |
| Theorem 4.6.2, p. 245 | phi >= 0 any function, phi(x)/x -> infinity; examples x^p (p>1), x log^+ x; E phi(|X_i|) <= C; proof eps_M = sup{x/phi(x): x >= M} |

| Gap | Where | Labels |
|---|---|---|
| MP-C001 gloss | body paragraph after the sigma-field lemma | (in source paragraph of thm:p15-w02c-p15-014-sigma-field-variant) |
| MP-C015 Theorem 1.3.5, remark on 1.3.4 | body corollary, paragraph, example; annex proof | thm:p15-w02c-p15-014-borel-functions (annex:p15-w02c-p15-014-borel-functions), def:p15-w02c-p15-014-ratio-example |
| UI-C001 arbitrary-collection definition, M+1 bound | new section sec:p15-w02c-p15-014-ui-source; annex | def:p15-w02c-p15-014-ui-arbitrary, thm:p15-w02c-p15-014-ui-arbitrary (annex:p15-w02c-p15-014-ui-arbitrary) |
| UI-C003 Theorem 4.6.2 integrability step | same section; annex; patch indices 9-10 for the read-only UI host | thm:p15-w02c-p15-014-ui-moment-source (annex:p15-w02c-p15-014-ui-moment), def:p15-w02c-p15-014-ui-moment-example, def:p15-w02c-p15-014-ui-moment-limits |

Lemma hypothesis note: Durrett's "any function" phi is kept; the lemma states that each phi(|X_i|)
is a random variable, which his hypothesis E phi(|X_i|) <= C presupposes (automatic for Borel phi).
Symbol intake: six rows added (V, P_n, pi_i, varphi, eps_M, M_0).

## Continuation (r5 b3)

- All gaps of the r5 b3 assessment in the packet's units are now written in the owned files or in
  the off-route w02c-p15-002 chapter; what remains is lead action: driver inputs (patch indices 3-4),
  routed-host patches (indices 5-10), and the w02c-p15-002 chapter route decision (MP-C006, C010,
  C011 X-in-F, C014, C016, C017, C021(b)).
- WCL items: readonly unit (owner w02c-p15-004); not written.
- Checks r5 b3: unit-compile ok, 0 overfull; find_fused_spaces clean; check.py filtered clean.

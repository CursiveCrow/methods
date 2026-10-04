# P7 circle encode–decode: exact June 2013 source

## Scope and saved packet

Authoring block started 2026-10-03 10:21:29 UTC. This packet addresses the
circle gap left open by the routed HoTT foundations and HIT packets, not an
independent correctness review or a coverage disposition update. It supplies
the declared main encode–decode construction: integer presentation,
univalent code, signed powers, actual decoder lift, both inverse homotopies
and based-loop equivalence. It does not close every alternative argument
or the full original HoTT source allocation.

Owned files:

- handbook/parts/p07/hott-circle-encode-decode.tex
- handbook/annex/p07/hott-circle-encode-decode.tex
- handbook/bib/intake-p07-hott-circle.bib
- handbook/registry/symbols-intake-p07-hott-circle.csv
- this research note.

Ten proved results have ten reciprocal full annexitems: integer
presentation; successor/addition interface; signed power coherence;
monodromy; decoder lift; signed winding; decode–encode; encode–decode;
loop equivalence/addition; total-cover contraction. Definitions and
assumptions are marked separately. No canonical, driver, map, coverage,
receipt or style file was edited. No child, independent review, test,
build or render was run.

## Source identity and reading extent

Primary release: HoTT/book, commit
e0aa8e9d16858fc0ce01aacd43b24da0bd765ae3, author timestamp
2013-06-19T19:21:50Z. Held commit metadata identifies author Andrej Bauer
and tree prefix 5655ddf. The exact release's main.tex includes homotopy
at line 201. This is the June public release used by the existing
HoTT2013PublicReleaseFoundations key. The May 2023 first-edition tag
(prefix 4715f712) and August 2013 arXiv manifestation were not substituted.

The exact homotopy.tex was fetched read-only into memory:

<https://raw.githubusercontent.com/HoTT/book/e0aa8e9d16858fc0ce01aacd43b24da0bd765ae3/homotopy.tex>

Whole file: 153,773 bytes, 2,870 lines; SHA-256
35e0bee48711893dccf860a7c29a938f7c3ac162ab1cf3661e0cc0b903ec5d19.
The complete native Section 8.1, lines 309–789, was read in consecutive
regions 309–490, 491–655 and 656–789. This is not a complete Chapter 8
or book read. No source download was added to an unowned directory.

Native regions:

- 309–348: goal, signed powers and failure of fixed-loop path induction.
- 349–404: classical universal cover and contractible total path space.
- 405–490: code by successor equivalence and both monodromy directions.
- 491–655: encoder, dependent decoder, predecessor-power function lift,
  both inverse homotopies, equivalence and homotopy-group consequences.
- 656–722: separate flattening route and integer-indexed cover HIT.
- 723–789: separate identity-system eliminator and pair-path coherence.

Line 633 repeats the first inverse lemma's reference where both inverses
are needed. The new exposition supplies two distinct reciprocal results;
the source is untouched. The source's abbreviated negative induction
and predecessor-power calculation are expanded in the new annex.

Exact-release prerequisites also read:

- Held hits-public-release-2013.tex, lines 1315–1454: source pair
  quotient, canonical integer fixed-point presentation, signed induction
  and powers. SHA-256
  cb605e5c917f8ee32ac79f10595148a1dd71e11f73e1d1659c967ac183d79095.
- Held basics.tex, lines 1911–1981 and immediately relevant
  zero/successor and injectivity material through 1992: natural-number
  identity codes. SHA-256
  e93982b549538de1c454cc72a84b817655f88dc1757b6ad727128d808fad15d7.
- Held release commit metadata SHA-256
  a6bc31b9e28656d0402b2e83480eb15b0003192f6209c0ede46efa5377c05159.

The prior research notes edition-2026-p07-hott-foundations.md and
edition-2026-p07-higher-inductives.md were read for source identity and
held acquisition location. The held README identifies CC BY-SA 3.0.
This is independently authored, attributed exposition, not a copied section.

## Actually routed prerequisites

At capture, handbook/parts/p07.tex lines 122–123 route the HoTT
path/equivalence and HIT packets; annex driver lines 18–19 route their
proofs. The new packet is not self-routed. Root owns integration.

The selected substantive definitions and full relevant proofs were read:

- Core Id/J, groupoid laws and cancellation.
- Transport composition/inverse, based-path and pullback transport:
  HoTT annex lines 169–202.
- Arrow transport and function paths: annex lines 58–85.
- Sigma paths and round trips: annex lines 31–56.
- Contractibility comparisons: annex lines 88–132.
- Adjointification with corrected triangle: annex lines 252–281.
- Fiber-equivalence characterization: annex lines 283–314.
- Homotopy-level closure: annex lines 390–422.
- Univalence and its particular transport comparison: annex 424–446.
- HIT dependent paths, circle recursion and universal property:
  HIT annex lines 4–67, plus the actual circle eliminator declaration.

Hashes of routed artifacts when read:

| artifact | SHA-256 |
|---|---|
| parts/p07/hott-paths-and-equivalences.tex | bd541de374e4e7522aedc767a3ce14caceb9015939fc0e6a976f3e40992ffce6 |
| annex/p07/hott-paths-and-equivalences.tex | cc0d672f359334922172efd460be5c1ad92dbc1237cf6ab344756e6a17e6d2a1 |
| parts/p07/higher-inductive-types.tex | b72a07bad3307da216ca4460f825ac5ebc71e15ad08f0201bab6258343d85649 |
| annex/p07/higher-inductive-types.tex | 02a31a30257acd6cc85823311ca0831b986c5b9929c50288f22d8d39b95ae604 |

These artifact paths are relative to handbook. The existing corrected
adjointification proof is used as actually authored; this does not replace
the circle argument with a 2023 source. The routed reader did not fully
expose ordinary natural numbers as an API. The new packet declares that
ordinary primitive former and proves the integer facts actually needed.

## Equality and dependency decisions

The signed carrier 1+N+N is a presentation interface. The actual integer
type is the source-style fixed-point Sigma of a pair canonicalizer. The
annex proves its quotient property for the original relation a+d=b+c,
comparison homotopies, setness, successor equivalence and addition descent.
It does not substitute an unrelated assumed integer type.

The fixed-point witness of E is defined by tag induction, with reflexivity
on constructors, not asserted judgmentally reflexive at a free variable.
Arbitrary presentation comparisons, circle loop computation, universe
transport, path laws and funext are propositional. Circle point
computation, zero power and reflexivity transport retain their judgmental
computations.

The decoder lift is constructed as a composite: arrow transport changes
the input by predecessor; based-path transport appends the loop; all
signed cases prove power(pred n)·loop=power(n); funext supplies the
required function path. This invokes neither an assumed decoder nor
setness of the unknown loop space.

The first inverse uses variable-endpoint based J. The second uses signed
winding at the base. Its transported higher lift compares transport_M(loop,H)
with H pointwise using integer setness, then funext. Loop-space setness
is concluded only afterward. The total-cover contraction is then the
Sigma path consisting of decode(c) and epsilon(c), not a circular premise.

## Intake and insertion seam

One new focused primary-source bibliography entry:
HoTT2013CircleSourcePublicRelease. Retain the existing edition key
HoTT2013PublicReleaseFoundations. Sixteen seven-column symbol-intake
records have typed roles and equality restrictions.

Suggested seam: root inputs the new body immediately after
parts/p07/higher-inductive-types.tex, and its reciprocal annex after
annex/p07/higher-inductive-types.tex. Root merges bib/symbol intakes.
No new inference-rule sheet or macro is required; the packet uses the
already routed eliminators and mathematical definition/transport displays.

## Residuals and next source-native seam

The main circle encode–decode route is authored, not independently reviewed
or compiled. Separate original-source obligations remain:

1. General Section 6.12 flattening lemma and its specialization equating
   the code total space with the integer-indexed cover HIT. A derived
   contraction after encode–decode does not provide that equivalence.
2. The identity-system alternative in lines 723–789: full dependent
   pair-path transport composition and coherence of the selected winding
   proof under an integer step. The main route is not counted as a
   reconstruction of that alternative eliminator.
3. Native homotopy-group, truncation and iterated-loop interfaces for
   the source's pi1 and higher pi_n conclusions. This packet proves
   the stronger based-loop equivalence and setness but does not invent
   a general homotopy-group interface.
4. Other Chapters 6/8 HIT, sphere and source-native allocations.
   Planned chapters 90/91 are not globally closed by this one packet.

Next useful seam: the general flattening lemma and specialized
code-total-space equivalence, retaining the source's integer-indexed
cover HIT and dependent loop coherence, instead of repeating the main
encode–decode argument.

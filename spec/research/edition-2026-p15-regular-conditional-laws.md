# Edition 2026 P15: regular conditional laws

Date: 8 September 2026. Author: /root. Scope: P15.12.
The body and full proof annex are written, read back and integrated after
conditional-expectation. All independent reviews remain deferred until the
complete manuscript change set has been made.

## Source and supplied scope

The exact held Durrett 2019-01-11 source and complete Section 4.1 reading
are recorded in edition-2026-p15-conditional-expectation.md. Root read all
of printed pp. 205–217, including Theorems 4.1.16–18, the sphere example
on p. 210 and the conditional Holder exercise on p. 216.
The new text retains the source's countable rational-CDF construction,
Stieltjes measure construction and generating-class argument. It supplies
all endpoint limits, the rational right-continuity conditions, the common
measurable good set, and the Borel-image concentration needed to transport
the measure to its original target space.

A probability kernel is required to be a measure at every argument in the
new definition. The text identifies the source's almost-everywhere variant;
the construction supplies the stronger convention by an explicit measurable
point-mass default. The observed-value theorem includes the source's
same-standard-Borel-space case and proves the additional arbitrary
measurable conditioning-space clause through the scalar factorization
already established. It makes no assertion for arbitrary target spaces.

## Written artifacts

| Artifact under handbook/ | Lines / bytes | SHA-256 |
| --- | --- | --- |
| parts/p15/regular-conditional-laws.tex | 254 / 11645 | 02F6E8689A8BBC8F63362EC0A76D652DD64000E155A400535C8CB9C4CA825C44 |
| annex/p15/regular-conditional-laws.tex | 435 / 19835 | 746593FBC2EFC998D62F49208EC33634A2DE9EB75B9113FF354A256496F0C4EB |

Eight reciprocal suffixes use thm:p15- and annex:p15.:

- kernel-expectation: measurable simple/monotone integration and the signed absolute-integrability exception.
- real-conditional-law: all countable good-set conditions, the full CDF proof, measurable Stieltjes family, event identities and simultaneous measure uniqueness.
- standard-conditional-law: the exact Borel image, full-measure concentration, point-mass completion and countable-generator uniqueness.
- density-conditional-kernel: complete joint-density kernel with positive finite marginal domain and a valid probability at every other argument.
- value-conditional-law: all scalar lifts, a good set on the conditioning space, the probability kernel, joint event identity and observation-law uniqueness.
- kernel-joint-measure: measurable sections, the complete induced product probability, uniqueness, nonnegative and signed integration and the conditional parameter formula.
- conditional-holder: the source's proof route through the joint regular distribution and the ordinary Holder inequality.
- conditioning-coordinate-examples: normalized spherical coordinate densities, all great-circle transformation branches, and two different positive-probability approaches to one null event.

The uniform-square example uses Z = Y/(1+X). Its joint density is derived
by the already proved affine substitution, and the conditional X means are
1/2 and 5/9 for the two observation choices. The same densities hold exactly
on their shrinking positive-probability events. The source sphere model's
new great-circle angle has density absolute cosine divided by four, with
longitude independent of that angle. No source figure is reproduced.

The current RN body hash after the forward-reference update is
00F66AA8BA8A4B65C17E2339324137C7785993C2CDD7401B3675F6B3A54EE2A0;
its full annex remains D3E282F6672E636E838F229D6D419523696045C0181AA6EA1D1D80EAD3EA23A7.
The existing bibliography key DurrettPTEAuthor2019 is reused. Canonical
notation and the predecessor forward references are integrated. No tests,
independent reviews or manuscript renders were introduced. The next local
probability work is martingale definitions, bounded strategies, upcrossings
and convergence, followed by the stronger-moment, uniform-integrability
and reverse-martingale results required by the general information theorem.


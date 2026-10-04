# Approximate quantitative inference: source and authoring record

Date: 9 September 2026. Author: historical_first_half.
Allocation: ED26-SCI-Mahajan2014-002, originating gap ED26-GAP-SCI-003.
Standing: the four assigned components are complete as authored work, with
15 reciprocal theorem/proof pairs and a complete author read-through.
Independent source, mathematical and publication acceptance remains later work.

## Exact primary presentation and acquisition

Sanjoy Mahajan, *The Art of Insight in Science and Engineering: Mastering
Complexity*, MIT Press, 2014, ISBN 9780262526548.

The exact approved [MIT OpenCourseWare PDF](https://ocw.mit.edu/courses/res-6-011-the-art-of-insight-in-science-and-engineering-mastering-complexity-fall-2014/3bca850386a3005c22134fa62fb3bad5_MITRES_6-011F14_art_insfin.pdf)
was acquired once for this and the parallel dimensional-reasoning unit:
source/references/mahajan-2014-insight/mahajan-2014-art-of-insight-ocw.pdf.

- 8,336,087 bytes; 410 physical pages.
- SHA-256: B4DEB8E42CFC079BAAA9B395366AFDDD775584F658C53720F8B15C00EF1942A6.
- Physical page 4 is the title; page 5 is the copyright/cataloging page.
- The PDF footer records 2014-09-02 10:51:35 UTC, revision 78ca0ee9dfae.
- Copyright identifies the author and MIT Press and states CC BY-NC-SA 4.0.
- Arabic printed page n corresponds to physical page n+19.
- This is the selected 2014 presentation, not the 2008 course draft.

Ordinary PowerShell acquisition failed before creating the target; the scoped
permission request and then an explicitly approved curl command obtained the
source with ordinary TLS verification. No certificate or access check was
disabled. The shared path/hash and identity were sent to the dimensional author.

Read the title, copyright and complete selected body: Sections 6.1–6.4, printed
199–228 (physical 218–247), and Sections 8.1–8.4, printed 279 through the end
of 8.4 on page 312 (physical 298–331, stopping before 8.5). All embedded source
exercise prompts within those extents were read as well. The original wave
diagram on printed 310/physical 329 was also read visually to verify its
nine regions, the two axes and its reduced-wavelength convention. The single
source-page image is tmp/pdfs/p15-approximation/source-wave-regimes.png.
The source renderer emitted missing display-font notices, but the diagram
and its formulas were legible. No manuscript page was rendered.

## Scope and manuscript destinations

Body: handbook/parts/p15/approximate-quantitative-inference.tex.
Annex: handbook/annex/p15/approximate-quantitative-inference.tex.
Root owns routing, canonical bibliography/symbol merging and final integration.

| Required component | Completed treatment |
| --- | --- |
| ED26-GAP-SCI-003-C01 | def:p15-approximation-relations distinguishes identity, explicit bound, ratio asymptotics and heuristic comparability; logarithmic factor bounds and model qualifications make the relation usable. |
| ED26-GAP-SCI-003-C02 | Logarithmic rounding; weighted characteristic values and nonlinear remainder; energy/momentum example; oscillator scale; rectangular graph error; exact cone model; shape models; all named easy-case method families, including two-parameter waves. |
| ED26-GAP-SCI-003-C03 | thm:p15-approximation-certificates and thm:p15-approximation-rational propagate explicit error into strict comparison; overlap preserves an unresolved decision. |
| ED26-GAP-SCI-003-C04 | The x=0.9 rational failure, the x=0.1 small-margin reversal, a moving-domain nonuniform limit, and families with identical endpoint limits but uncontrolled transition values. |

The lead read the exact current allocation and confirmed that its selected-case
success conditions do not create a separate quota of solutions to all 49
source exercise prompts. Every named method family and its needed worked
example/derivation is retained. The treatment does not claim to solve the
entire embedded exercise collection. Selected exercise calculations are
included when they complete the method: nonlinear springs, the cone ODE,
velocity equalization, Atwood tension, projectile prefactor, rolling dynamics
and drag-regime self-consistency.

### Source method and example families

- 6.1–6.2: approximate arithmetic and its motivation; logarithmic rather than
  linear distance; whole and half powers of ten; minutes/day, seconds/year,
  and the pi mnemonic's actual status.
- 6.3: representative state populations; mass-independent jump scaling only
  under fixed muscle/efficiency assumptions; linear and nonlinear oscillator
  periods; vector versus scalar velocity derivatives; characteristic-value
  scaling for a generic impulsive energy release.
- 6.4: atomic-cell density and spacing sensitivity; rectangular age profiles
  and historical US/UK examples; finite-time approach to terminal speed;
  momentum-preserving velocity equalization; mean-free-path tube models;
  localized weak deflection; localized elastic contact.
- 8.1–8.2: inclusive-month and birthday boundary checks; positive-term
  dominance; ellipse symmetry; Atwood symmetry and actual dynamics;
  projectile endpoint cases; the limit of weak-angle inference.
- 8.3: rolling-radius versus geometric-radius regimes; viscous/form drag and
  self-consistency; transition limits of the drag coefficient; atmosphere
  scale height; confinement/attraction energy competition and thermal-mean
  qualifications; stellar temperature scale and its model limits.
- 8.4: the four wave corners and all five intervening retained-effect regions;
  derivation from an explicit linear-wave model; finite corner-error factors;
  a dimensionless interpretation of the classical/quantum/relativistic map.

## Complete reciprocal proof list

For each suffix below the body label is thm:p15-approximation-SUFFIX and the
annex label is annex:p15.approximation.SUFFIX.

1. certificates: interval implications, overlapping-threshold countervalue,
   difference-error budget and relative-error denominator.
2. log-bound: nearest-logarithm factor bound, arbitrary fixed real powers,
   and the geometric-mean rounding boundary.
3. lumping: affine identity, full integral Taylor remainder, weighted-square
   identity and finite uniform-sampling expectation.
4. energy-average: exact weighted kinetic-energy difference and equality case.
5. oscillators: exact linear period, nonlinear energy quadrature, finite
   endpoint integral and amplitude exponent.
6. rectangle: bounded-height integral error, omitted tail and Lipschitz bound.
7. fall: exact quadratic-drag solution, uniqueness, distance and velocity
   errors, and the distance-based speed fraction.
8. easy-cases: finite-check polynomial perturbation and smooth functions
   sharing both endpoint limits but differing arbitrarily in the middle.
9. counting-cases: inclusive-index bijection and complete birthday-product
   derivation, including empty and pigeonhole cases.
10. mechanical-cases: ellipse area integral, both Atwood equations, projectile
    endpoint cases and rolling translation/torque/no-slip equations.
11. dominance: positive maximum approximation and signed cancellation bound.
12. competing-energies: unique minimum, scale-balance distinction, exact
    turning-point midpoint and an explicit midpoint/time-mean distinction.
13. water-regimes: all mode/boundary equations, dispersion relation, four
    corner limits, finite shallow/deep bounds and combined error budget.
14. rational: exact remainder, uniform finite bound and both threshold reversals.
15. nonuniform: pointwise limit, nonattained supremum, moving-input failure
    and the positive-distance uniform domain restriction.

These proofs are authored derivations. The physical model equations and
constitutive assumptions are stated as such; algebra inside a stipulated
model is not represented as proof that the physical world satisfies it.

## Corrections and qualifications applied directly to active prose

The new chapter uses an explicit estimate notation rather than conflating
Mahajan's comparable-scale sign with ratio asymptotics. Easy-case agreement
rejects candidates but does not establish uniqueness; the appropriate
counting, geometry or dynamics supplies the full conclusion.

The UK rectangular-model inversion is computed consistently from the same
50-million/65-year/17,000 inputs: about 2.21 percent, not an unrelated
participation percentage with another denominator. Historical source numbers
are marked as historical examples, not current demographic claims.

For E(r)=A/r^2-B/r, balancing the two magnitudes gives A/B, while minimization
gives 2A/B. The exact model calculation makes the missing coefficient visible.
A turning-point midpoint is distinguished from both time and thermal means;
universal thermal expansion is not inferred from a schematic curve.

Weak gravitational deflection establishes an estimated scale, not capture or
an event horizon. The stellar scale argument does not establish a supernova
criterion or a reaction rate. The physics map uses actual dimensionless
ratios with held-fixed data instead of treating dimensionful constants alone
as unrestricted comparison parameters.

The wave expression is identified as squared phase speed of a sinusoidal mode
in an explicit linear inviscid model, not all possible waves. Reduced
wavelength is lambda/(2pi), and the gamma=0 case has no capillary branch.
The claimed finite error budgets are derived independently of the source's
diagram. Drag coefficients retain their model/shape and transition caveats.

Author read-through additionally made integrability explicit in the rectangle
bound, A!=0 explicit in the signed relative-error bound, the oscillator's
continuous zero-force extension explicit for noninteger exponents, and
epsilon<=1 explicit so the moving input remains inside its stated domain.
The existing Laplace hypotheses are described as conditions for applying that
theorem, not claimed logically necessary for every Laplace-type conclusion.

## Interfaces, intakes and final standing

Actual existing manuscript source was read for the Stirling remainder,
Laplace approximation and nonlinear measurement remainder. Active links are:

- thm:p15-stirling-with-remainder;
- thm:p15-laplace-relative-error;
- sec:p15-dimensional-and-scaling-inference, confirmed by its current author.

The dimensional author owns the single Mahajan2014Insight record in
handbook/bib/intake-p15-dimensional-reasoning.bib. The approximation intake
is a comment-only coordination record, not a duplicate entry or bibliography
stub. The unique approximation symbol intake has 28 rows.

Before canonical merging, all 28 glyph cells were changed from ASCII names to
their actual existing display code enclosed in TeX inline-math delimiters.
The distinct epsilon and varepsilon choices, every role, scope and first-use
label were preserved. Formula-bearing notes now use the body spellings in
math mode, including the restoring force, drag denominator, energy function
and wavenumber relations. Root's correction of Q_h precedence to n/a is retained.
This bounded intake correction did not change the body, annex or canonical
registry, and did not run a build or review.

All of the final body and annex were read, and the modified hypotheses were
read again. A single bounded count of the actual files found 15 theorem/status
targets and 15 corresponding annex items. Mathematical examples were checked
by their displayed exact algebra and derived formulas. No new test suite,
manuscript build, manuscript rendering or independent review was performed.
The research and PDF skills supported exact-source identification and the
one necessary source-diagram reading.

Final artifact hashes:

- Body: 01B763271502DE093D4091EF01E15E18820B8C718E02AAF3AFB8FC6DDEE78FCF.
- Annex: 83632924648CE5AD066B330D166AA2733B0CF4D95F116ABDA607C93DAE2B7A13.
- Symbol intake: 867ACFBF5AE1BCD07B6CF812BFEFF9D103C8E7662BDD5B71B0E6FA8EE1951056.
- Bibliography coordination intake: B4E9FB511BB53DA85F1530E0EF04C55E1543398C496FB40A47BDC94A59B82A63.

No source or mathematical obstacle remains for the four assigned components.
Routing, canonical merging and later consolidated independent admission are
still required. This record does not claim completion of the whole Mahajan book.

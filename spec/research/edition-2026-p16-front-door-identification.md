# P16 finite front-door identification: author return

Date: 8 September 2026 UTC. Author block started 09:14:32 UTC;
deadline 09:59:32 UTC. This is manuscript authoring under the user's
all-changes-before-consolidated-reviews instruction. No review task was
started. The output paths were verified unused before creation.

## Complete written component

| File | Extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p16/front-door-identification.tex` | 248 lines; four definitions, five results, one method | `B2264C7088657DEDCC5DD8E119E69608FE50EC62DB19D9CFF154890B250CAA97` |
| `handbook/annex/p16/front-door-identification.tex` | 352 lines; five complete proofs | `89D2E3EEBD35888F1E65003A076F734D54F93F31AEC8BA2E72DE47E2E098948F` |

Both files were read back completely from disk, including every proof.
Only these new files and this note were authored. No older boundaries,
shared routes, canonical notation, bibliography, or review report was edited.

The five reciprocal suffixes have body prefix `thm:p16-` and annex prefix
`annex:p16.`:

| Suffix | Full content |
| --- | --- |
| `front-door-graph-steps` | Treatment cannot descend from mediator; fixing the mediator deletes every directed treatment-response path; fixing treatment leaves no active mediator-response back-door path. Each is proved directly from the three path conditions. |
| `front-door-composition` | Pointwise equality of joint-intervention and mediator-intervention responses; commutation of distinct equation replacements; back-door adjustment inside the treatment-intervened model; positive mediator strata and the full finite mixture. No observational positivity is needed for this model identity. |
| `finite-front-door-identification` | Empty-set adjustment for treatment-to-mediator, treatment adjustment for mediator-to-response, and the proved composition; exact positive denominators, partial observation, equality across models, and finite response means. |
| `front-door-binary-calculation` | All graph conditions, eight full assignments, observed marginal table, every conditional factor, both mixture stages, direct interventions, and absence of an observed back-door set in the stipulated graph. |
| `front-door-bypass-counterexample` | A direct treatment-response edge violates only the interception condition; all required treatment-mediator pairs remain positive; the front-door expression fails but empty-set back-door identification still works. |

The latent example independently verifies the supplied lead: observational
response probabilities are 2/5 and 19/20, while both direct equation
replacement and the front-door functional give 5/8 and 7/8. Its contrasts
are 11/20 and 1/4. The bypass example's true probabilities are 1/4 and 1,
while the unjustified front-door expression gives 5/8 and 7/8.

## Sources and actual dependencies

The research and PDF skills guided reading of the held Pearl overview:
`source/references/pearl-causal-overview-2009/pearl-2009-ucla-r350.pdf`,
593,923 bytes, SHA256
`1A5ECB7CB7C55A9B4F2C09AAC091BC01A3EABFC94FC55EE692EFBC013A8B7581`.
Official source: [UCLA R-350](https://ftp.cs.ucla.edu/pub/stat_ser/r350.pdf).
Printed pp. 114-117 were read as extracted text in this block; complete
pp. 116-117 were also read visually. Figure 4 and pp. 114-115 had been
read visually in the preceding author block. Source reading images for
116-117 are in the old task's `tmp/pdfs/p16-front-door-source` directory.

Section 3.3.2, p. 116, Eq. (26) gives the mediated composition example.
The overview does not present a named three-condition front-door definition
on these pages; the explicit sufficient graph schema and its complete
finite proof are supplied here as handbook deductions. The manuscript does
not misattribute this proof to an unread book or to the overview's cited
general do-calculus. Its existing `Pearl2009CausalOverview` key is used.
The distinction between identification and estimation on p. 117 is retained.

The preceding causal and separation files had been read completely during
authoring. Their exact current hashes were verified, and the actual
intervention definition/proof and complete back-door statement/proof were
reread for this construction:

| Dependency | SHA256 |
| --- | --- |
| `parts/p16/finite-causal-models.tex` | `331568E5FF2329B4498CA98DCA7DC8BE79D4EB77B8A2152DAB33F05F05BABA42` |
| `annex/p16/finite-causal-models.tex` | `1393539308C2668996B75AED30D47025F337944E0FC0270E863A153A00794096` |
| `parts/p16/graphical-separation-adjustment.tex` | `6F26941A0B9AF00CE5101771113732958EE1926CDFF2D3BAEC1E440ECED62E2F` |
| `annex/p16/graphical-separation-adjustment.tex` | `9B97C4938F35761CA336AE783562B6E02C7F194DCE44056880A33380FAE9FC2A` |

## Integration and notation

Input each file after its matching `graphical-separation-adjustment`
predecessor. Both belong to the existing finite causal model chapter,
expected scope P16.2. Root should update earlier boundary paragraphs to
point here for this finite single-mediator result while retaining the
separate general do-calculus, completeness and multiple-mediator obligations.

| Glyph family | Explicit role |
| --- | --- |
| `\mathcal M`, `t,h,r`, `X,M,Y`, `x,m,y,x'` | Whole structural model; distinct treatment/mediator/response vertices; finite coordinate variables and their typed values. The mediator M is distinguished from the model. |
| `G_{\overline J}`, `G_{\overline t}`, `G_{\overline h}` | Incoming-edge deletion for equation replacement, distinct from the preceding proof's outgoing-edge deletion. |
| `M^x,Y^x,Y^m,Y^{x,m}`, `Y^{X=x},Y^{M=m}` | Typed single and joint intervention coordinates, with singleton indexed assignments and named-variable aliases declared before use. |
| `\mathcal X_+`, `\mathcal H_x`, `g:S_r\to\mathbb R` | Positive observational treatment strata; mediator support at the chosen positive treatment value; specified finite response function. |
| `U,U_U,U_X,U_M,U_Y`, `q(u,a,b),\alpha(a),\beta(b)`, `q_m` | Latent endogenous root and independent disturbances; explicit outcome masses; computed mediator-intervention response probabilities q_m, distinguished from outcome mass q. |
| `(u,a,b)`, `(c,b)`, `\oplus` | Outcome coordinates in the two stipulated models and the existing bit exclusive-or operation. |

## Checks and next writing requirement

The existing editorial scanner reports no findings: 17 labels, five
statuses, five annex items, five reciprocal pairs, seven external references
resolved in the prior causal/separation bodies, and no label collisions
with those bodies. The existing citation key is present. These are author
source-structure checks, not independent acceptance. No tests or manuscript
renders were created.

The assigned finite front-door component is fully written. The next distinct
requirement is a complete soundness treatment of the general do-calculus
rules with their exact graph modifications, conditioning and intervention
hypotheses, followed separately by any claimed completeness or identification
algorithm. This component assumes none of those unproved general rules.

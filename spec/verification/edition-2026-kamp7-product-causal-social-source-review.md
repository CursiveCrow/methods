# Independent source review: Kamp 7, products, causal models and social choice

Reviewer: /root/kamp7_product_causal_social_source_review.
Started 2026-09-08 06:35:11 UTC. Block deadline 07:20:11 UTC.
This is an independent source-fidelity review. Other reviewers' reports were
not read. Only this report is owned; no manuscript or shared-record edits.

## Retrieved Content

### Kamp manuscript body, lines 200-211

Source: handbook/parts/p09/presentations/kamp-iii2-lemma7.tex.

```tex
Each fixed-side condition \(\Sigma_J^R\) is a finite conjunction
of members of \(\operatorname{Bp}(x,u)\), and each nonempty
\(\rho_J^R\) is a finite disjunction of members of
\(\operatorname{Bp}(u,v)\), with the declared empty cases.
Each residual disjunction has at most one disjunct of length
\(\ell(\phi)\), and no disjunct of greater length.

This is the handbook's corrected aggregate formulation of the orientation
in Kamp's Lemma~7(b). The source refers its proof to the analogous left case;
the annex supplies both directions for this orientation in full
\cite[ch.~III, lemma~7(b), p.~81]{Kamp1968}.
\end{hblemma}
```

### Kamp manuscript annex, lines 465-474

Source: handbook/annex/p09/kamp-iii2-lemma7.tex.

```tex
Every basic past pattern begins with a unary point atom at its initial
endpoint, both at stage one and in each higher-stage constructor.
That atom is false under this interpretation, so every basic pattern
at every ordered endpoint pair is false. A nonempty conjunction of
such patterns is false. This verifies why imposing one basic pattern
as the fixed-side condition would remove a valid case. The same
argument works on \(0<1<2<3\) with \(x=0,y=3,u=1\) in the
right orientation, where the tested interval contains 2 and its
truth comes from \(\psi_2\), rather than from vacuity.

```

### Causal manuscript body, lines 246-260

Source: handbook/parts/p16/finite-causal-models.tex.

```tex
\begin{hbdefinition}{def:p16-causal-identification}{Identification relative to a model class}
Let \(\mathcal C\) be a class of models with common observed coordinates
\(O\) and value sets \(S_O\), and let \(Q(M)\) be a specified
quantity associated with each model in the class. The quantity is
\emph{identified from the observational law on \(O\)} within
\(\mathcal C\) if, for every \(M_1,M_2\in\mathcal C\),
\[
 p_{M_1,O}=p_{M_2,O}\quad\Longrightarrow\quad Q(M_1)=Q(M_2).
\]
Equality of laws means equality at every assignment in \(S_O\).
A pair with equal observed laws and unequal values of \(Q\) proves
\emph{nonidentification} in that class. This is the two-model criterion
of the source's Definition~2 \cite[p.~109]{Pearl2009CausalOverview}.
Identification treats the observational law as given exactly; recovering
it or the target from finite sampled data is a separate estimation problem.
```

### Product manuscript body, lines 308-314

Source: handbook/parts/p15/product-measures.tex.

```tex
\item Assume additionally the axiom of choice and the continuum
 hypothesis, in the form that a bijection
 \(b:\omega_1\to(0,1)\) exists, where \(\omega_1\) is the set
 of countable ordinals with its usual order. Transport that order by
 \(b\), writing \(b(\alpha)<'b(\beta)\) when \(\alpha<\beta\).
 On two uniform Borel copies of \((0,1)\), with measures
 \(\mu_1,\mu_2\), set
```

### Social-choice manuscript body, lines 267-270

Source: handbook/parts/p17/social-choice.tex.

```tex
The permitted increases are \(-1\) to \(0\) and \(0\) to \(1\).
Symmetrically, a decrease by one with \(f(s)\leq0\) must give
\(f(s')=-1\). Under neutrality this second direction follows from the
first; it is included in the condition itself when discussing independence.
```

## Supplementary Notes

### Scope and evidence standing

Kamp Lemma 7: **PASS for the frozen source-based corrected treatment** below.
No defect remains in this reviewed scope. This conclusion concerns the exact
corrected aggregate formulation; it does not accept the false individual-Bp
statement printed in 7(b). Finite causal models, product measure and social
choice: **PASS for the respective frozen components**, assessed below.
All eight manuscript files and all 27 proof items were read completely.

| Kamp target | Complete read extent | SHA256 |
| --- | --- | --- |
| handbook/parts/p09/presentations/kamp-iii2-lemma7.tex | 1-278 | 3411BB4A552755CAFEF4675851A764A8605CBE36D402C6CFE022E397DE9F9778 |
| handbook/annex/p09/kamp-iii2-lemma7.tex | 1-489, all three proof items | 3E71146A7142A8A2BA26983A6A23634D9E7D3B52AA8A5F4FD2C9CC8793BD817F |
| spec/research/edition-2026-c7-kamp-iii2-lemma7.md | Complete intake, not treated as primary evidence | D9EB1685E62404234017C4DA66D209A50C9D6C8692A423E5658AEE2545C1F471 |

The contract C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3
and conventions 4293F514072179A5AC95E64FA8D8F37E23FFE2693814A1980E5801BABA5B7242
were read completely, as were the research and PDF skills. The reviewer is the
already delegated researcher; no further agents were launched. PDF instructions
were used for reading primary scans. No PDF authoring operation occurred.

### Exact source and actual reading

J. A. W. Kamp, *Tense Logic and the Theory of Linear Order*, UCLA thesis, 1968.
Held source: tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf, 128 pages, SHA256
C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA.
Institutional locator: https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf.
The local source was retrieved and read on 2026-09-08 at 06:35-06:38 UTC;
no new network acquisition was needed.

All complete printed pages 63-66 and 80-83 were visually read, including the
7(a) class line at additional resolution. Physical pages are respectively
72-75 and 89-92. The eight inspected images were independently regenerated
from the verified PDF, at 180 dpi for prerequisites and 240 dpi for Lemma 7;
all eight SHA256 values matched the already inspected images exactly. Thus
the source reading is tied to the actual held PDF, not merely to the intake.

Actual manuscript prerequisites read: Lemma 1 body lines 1-184 (in particular
the complete basic grammar and word definitions); Lemma 1 annex lines 1-133
(complete realization induction and guarded closure equivalences); Lemma 4
body lines 44-91 (explicit word-to-formula recursion). The Lemmas 2-6 results
are not premises of these three cut proofs. No Lemma 8 proof is accepted here.

### Source comparison and exact correction assessment

1. Printed p. 80 states 7(a) using conjunctions on the fixed side and
   disjunctions on the varying side. The manuscript preserves that structure,
   the strict outer witness, the left universal interval, arbitrary formulas
   psi_1 and psi_2, and Lin equivalence. Its basic residual formulas also lie
   in the elementary interval class; no additional expressiveness is assumed.

2. Printed p. 81 states the 7(b) input as Bp(x,v), with v as the second
   endpoint. Its output line really gives sigma_i as individual members of
   Bp(x,u) and rho_i as individual members of Bp(u,v). It is not a reading of
   a y glyph or an implicit conjunction/disjunction printed on that line.

3. The source grammar on p. 63 makes every Bp formula begin with a positive
   unary atom at the first endpoint. Interpret all unary predicates as empty
   on the finite order 0 < 1 < 2 < 3. Set psi_1 and psi_2 to the declared
   tautologies, x = 0, y = 3, and u = 1. The input to 7(b) is true, with a
   nonempty universally tested interval containing 2. Every individual Bp(x,u)
   fixed-side output is false for every possible u. This refutes every finite
   output list of the printed class, including lists using other predicate
   letters. The proposed correction is justified by the exact source claim.

4. The active correction retains finite conjunctions and disjunctions and
   explicitly supplies true/false empty aggregates. The four-point countermodel
   is handled by the empty subset. Those formula abbreviations do not introduce
   a stage-zero Bp pattern or change the original pattern length definition.

5. Printed pp. 81-82 split the occurrence sequence into a prefix and suffix,
   use the point-occurrence subsequence Se, and form starred words by retaining
   or duplicating the cut letter. The manuscript's n gap cuts and n-1 point
   cuts implement these operations with explicit interior ranges. Excluding
   an empty prefix is an explicit domain clarification needed to obtain a
   genuine positive-stage basic pattern; p. 81 separately requires a suffix
   of length at least two. The added realization proof justifies the ranges.
   The source's occurrence definition and repeated-letter example on p. 64
   support positional, rather than letter-identity, discrimination.

6. The point-cut and gap-cut proofs retain all labels and address the shared
   cut point itself. The gap reverse direction correctly uses its B_k label
   to join the adjoining open intervals. The finite maximum argument needs
   linearity only, not order completeness, density or absent endpoints.

7. The complete truth patterns, their positive parts, and the selected
   residual disjunctions implement pp. 82-83. The manuscript does not identify
   a complete truth pattern with its positive part in isolation. Its two
   quantified converses justify dropping negative tests in the full output,
   and retain one fixed subset while allowing the cut index to vary with v.

8. Printed p. 81's original bound is preserved. Point-cut lengths are
   2k+1 and 2(n-k)+1; gap-cut lengths are 2k+1 and 2(n-k+1)+1.
   The only equal-length left residual is the last gap, and the only
   equal-length right residual is the first. No residual is longer; the
   empty case has no basic disjunct. The length is the occurrence-sequence
   length defined explicitly at the beginning of Lemma 8 on printed p. 83.

9. Both worked examples were recomputed from their explicit predicate sets.
   In the two-interval example the two gap residuals are required at different
   quantified points, while the point-cut endpoint label fails. The n = 1,
   empty universal interval, missing outer witness, repeated letters and
   quantifier-capture cases are addressed without changing source hypotheses.

The correction is identified in the active reader text and its provenance
is kept in the author intake. The corrected theorem is not presented as the
literal unmodified historical statement. This review does not grant build,
visual-output, rights, formal admission, later-lemma or whole-book acceptance.

### Finite causal models: source fidelity and qualification

The complete body (418 lines, SHA256
331568E5FF2329B4498CA98DCA7DC8BE79D4EB77B8A2152DAB33F05F05BABA42) and
complete annex (377 lines, SHA256
1393539308C2668996B75AED30D47025F337944E0FC0270E863A153A00794096) were
read, including all eight proof items. The complete author intake
spec/research/edition-2026-p16-finite-causal-models.md was read as an intake.
Actual finite-probability prerequisites were read at body lines 24-158,
217-256 and 348-384: finite laws, conditioning, independence and expectation.
Its body hash remains 934D75E81BB2A465B43C5B4F04F3819167A957A692D7E46FE453D3504AE3FAA1.

Primary source: Judea Pearl, *Causal inference in statistics: An overview*,
Statistics Surveys 3 (2009), 96-146, DOI 10.1214/09-SS057. The held UCLA
R-350 September 2009 author copy in journal layout is
source/references/pearl-causal-overview-2009/pearl-2009-ucla-r350.pdf,
51 pages, 593,923 bytes, verified hash
1A5ECB7CB7C55A9B4F2C09AAC091BC01A3EABFC94FC55EE692EFBC013A8B7581.
Primary locator: https://ftp.cs.ucla.edu/pub/stat_ser/r350.pdf.
The title page and every complete printed page 103-113 (physical 8-18)
were visually read at approximately 06:40-06:41 UTC. All eleven relevant
pages were independently regenerated from this PDF at 115 dpi; their hashes
match the inspected images. The printed title, report number/date, journal,
pagination and DOI identify this exact presentation.

The source's directed assignments and potentially correlated exogenous
variables on pp. 104-105, autonomous functions on p. 107, and replacement
semantics on pp. 107-108 support the declared finite model. The chapter
explicitly separates dependency from independence, allowed inputs from actual
influence, and conditioning from equation replacement. Source p. 105 states
that an arrow permits an influence; it need not have nonzero strength. This
supports the inactive allowed input in the nonidentification constructions.

The p. 109 image of Eq. (10) really has P(M1)=P(M1) on its left, while the
surrounding definition compares two models and their observational laws.
The quoted active definition corrects this to equality across M1 and M2.
The source's actual typo is confirmed independently; no reflexive comparison
remains active and no inference from finite samples is substituted for
identification from a specified law.

Source Theorem 1 and Corollary 1 on pp. 110-111 supply the causal and truncated
factorizations. The manuscript's finite kernels are total sums over disturbance
values, including null observational parent inputs. The full product proof
uses a solution fiber and mutual independence without dividing by a probability.
The conditional-kernel equality explicitly requires a positive parent event.
Replacement preserves independence and changes exactly the intervened factors
to point masses. These are complete finite proofs of the source-based claims,
with simultaneous, empty and all-variable interventions addressed.

The source's local general identification prose does not specify positivity
on pp. 110-111. The chapter supplies sufficient full positive support for
identification from all observed endogenous coordinates, and makes no claim
of necessity for every target. The independent-disturbance pair X=0,Y=0 and
X=0,Y=X has equal observational point mass and unequal intervention results
at X=1, so the null-support qualification is mathematically necessary in the
stated general class. The first counterpair also keeps equal positive observed
laws on the same allowed graph, while one member permits dependent disturbances.
All table probabilities, conditional means, interventions, and common-cause
adjustment values were independently recomputed in the finite equations.

The chain example accurately specializes source Eqs. (5)-(7), (16)-(17), with
the positive event needed for an observational conditional made explicit.
Topological evaluation, full uniqueness, nondescendant invariance and the
binary examples are identified as handbook finite constructions. The chapter
does not claim the source's entire path-analysis, d-separation, five-variable
example, later identification or counterfactual theory has been supplied.
No empirical conclusion is imported from stipulated probabilities. No source
or mathematical defect was found in these eight frozen proof pairs.
Root's pending bibliography/notation integration is outside this source verdict.

### Product measures: full assigned source component

The full 391-line body has SHA256
9FFEDE5090864204636CEA69B317F2CEF9E82105A90A47DB8F75764FD23EE0AC;
the full 571-line annex has SHA256
E62A873EE1BC0B6435F19ABE71F9B121FD4EB53BA0B3322863BBF61186E1CAB4.
Both were read entirely, including all nine proof items, with the complete
intake spec/research/edition-2026-p15-u1-product-measures.md.
The actual prerequisite theorem statements were read in measurable-probability
at 216-264, 323-345 and 400-415; measure-extension at 24-85 and 141-156;
and integration-expectation at 54-142. These supply the generator criteria,
simple approximation, pi-lambda principle, unrestricted extension existence,
nonnegative series and monotone convergence, and signed-integral convention.

Primary source is Rick Durrett's *Probability: Theory and Examples*, author
Version 5, January 11, 2019, held as
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf,
490 pages, verified SHA256
AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886.
Primary locator: https://math.duke.edu/~rtd/PTE/PTE5_011119.pdf.
The title/contents were read as text; complete printed pages 37-41 were read
as text and complete page images at approximately 06:43-06:45 UTC. All five
images were independently regenerated at 120 dpi from the held PDF, and
matched the inspected image hashes. The source section heading, theorem
numbers, four examples, exercise statements and hypotheses were all inspected.

The rectangle premeasure proof retains the source's one-variable integration
argument before any product integration theorem. Unrestricted existence is
an explicitly identified consequence of the earlier extension theorem;
source Theorem 1.7.1's sigma-finite uniqueness is preserved. The finite-product
consequence, Euclidean Borel domain and rectangle volumes are supplied, with
parenthesization and coordinate permutations justified by the same uniqueness.

Both section lemmas and all four cases of source Theorem 1.7.2 are supplied.
The finite-box lambda-system proof avoids infinite subtraction. Indicator,
simple and monotone approximation cases establish Tonelli with infinite
values allowed. The signed proof separates positive/negative sections, gives
measurable null exceptional sets and finite representatives, and proves both
orders without an undefined infinity-minus-infinity operation. The source's
single Fubini naming is explicitly distinguished from the chapter's two names.

All four source counterexamples match their actual formulas, domains and
values. The discrete series, continuous exponential example and both infinite
part integrals were recomputed. The diagonal is proved product measurable,
while uncountable counting measure fails sigma-finiteness. The real p. 40
display in Example 1.7.7 interchanges the dx/dy arguments in its last iterated
expression; the active formulas attach each variable to its correct measure.
The fourth example retains both choice and CH and its countable initial
segments; it is not reported as unconditional. Its separately measurable
sections do not imply product measurability. Neither product sigma-algebra
nor factor domains are silently completed.

Exercises 1.7.1 and 1.7.2 are solved with measurable sequence encoding,
absolute convergence a.e., a defined exceptional-set representative, and
the measurable strict subgraph including zero and infinite heights.
The elementary one-variable calculus used for numerical evaluations is
declared and related to the constructed Lebesgue integral by simple bounds.
The null exceptional-section example and unit-square calculation check out.
Later exercises, infinite products, completion and further representation
theorems remain explicitly outside this component. No defect was found.

### Social choice: source domain, four-step Arrow proof and full binary exercise

The entire social-choice body and annex were read, each 321 lines, hashes
224340F36A0774478ED6CFD8713601190B23F97BE7950106DD4CD8F8B71E64FA and
C76738A8942F81BD5BF37E3701A30820AD24992E5B3805EC448CD9D883D69E6F.
All seven proof items were read and their profile calculations recomputed.
The actual finite-preferences body lines 21-74 were read for its weak/strict
relation and indifference conventions; the new chapter explicitly extends
the relation definitions to arbitrary alternative sets.

Primary source is Ariel Rubinstein's *Lecture Notes in Microeconomic Theory*,
second edition, author revision January 11, 2015, held as
source/references/rubinstein-microeconomic-theory-2015/rubinstein-second-edition-revision-2015-01-11.pdf,
verified SHA256 F7CEA2C4F48C77D93DD25C30BBDA83E051C6562A589256AAC8CBA1B5084A33F8.
Complete printed pages 122-128, physical 136-142, were read as text and
complete page images at approximately 06:45-06:47 UTC. All seven pages were
also independently regenerated from the verified PDF at 120 dpi and read.
Those fresh images are a different resolution from the author's earlier
images and are not asserted to match their file hashes.

The source model on p. 123 has finite voters, strict individual rankings and
possibly weak social rankings, on an unrestricted profile domain. The new
chapter preserves those types, keeps social choice functions distinct from
social welfare functions, and does not infer interpersonal intensity or an
ethical prescription from ordinal aggregation. The alternative set remains
arbitrary for Arrow; only rules using finite rank/count data restrict X.

All six source aggregation procedures on pp. 123-124 are specified. The
two-thirds procedure makes an explicit strict-output selection within the
source's incompletely specified weak-output example; it is identified as a
convention rather than a literal extra historical requirement. Fixed tie
priorities make both finite selection procedures well defined. The majority
cycle, victory scores, unanimous comparisons and rank-score counterprofiles
have the stated counts and scores.

The Pareto and IIA conditions match p. 124. IIA is applied to both ordered
pairs when transferring a strict or indifferent social comparison. Arrow's
four-step proof on pp. 125-126 is retained: extreme-alternative lemma, finite
pivot sequence, pairs avoiding the reference alternative, and the remaining
pairs. The new extreme lemma proves existence of distinct a,c even with weak
social ties. Its stronger arrangement allowing any set of top/bottom voters
is proved by the same valid source argument. The final step supplies both
orientations explicitly. The finite pivot is fixed across profiles through
IIA and no extra monotonicity axiom is assumed. Insertion constructions also
work for infinite ordered X; a possibly empty profile domain is addressed
explicitly in the annex. The source p. 127 attribution to Geanakopolos is
retained without claiming to have independently retrieved his separate paper.

The four displayed removed-premise examples are verified, with no claim that
they exhaust all domain restrictions. Source Problem 1 on p. 128 includes
individual indifference and quantifies positive responsiveness over both
ordered pairs. The signed encoding preserves those cases and both directions,
including when neutrality is omitted to check axiom independence. The balanced
profile proof gives uniqueness; the sign-of-sum rule verifies existence.
The weighted rule, constant-one rule and constant-zero rule preserve exactly
the two asserted conditions and violate the third. Problem 1(a)-(d) is supplied.
The chapter correctly leaves other related impossibility theorems and later
problems as distinct obligations. No source-fidelity defect was found.

### Completion check

At the 06:50 UTC checkpoint all four frozen pairs were fully assessed.
All eight target hashes were rechecked unchanged after the complete reading.
The report was read back completely. The 31 complete mathematical source
pages, the title/identity evidence and the stated prerequisite LaTeX extents
support these bounded source verdicts. Only the assigned review report and
disposable source-page images in the task workspace were written. No new
software tests, manuscript build/render, canonical records or admission
actions were performed. Final source-text verdict: PASS for each of the four
frozen components; zero unresolved findings in those reviewed scopes.

### Separate navigation addendum, 2026-09-08 07:07-07:11 UTC

Scope: the lead's final notation, bibliography and route snapshot only.
The earlier manuscript/source verdicts above remain unchanged. The preceding
report snapshot was 404 lines with SHA256
73655B7D94276154D122CC96DC28C49D4C8F76C15E6D43F64138058717F3DB2E.
No accepted proof reading was reopened and no other review report was read.

Navigation source-fidelity verdict: **PASS**, with no unresolved finding in
the supplied snapshot. All 49 new canonical entries at physical CSV rows
1142-1190 were read completely, together with every corresponding generated
table row and every generated index row. Their glyphs, roles, scope, first
use, notes, table anchors and index page-reference targets preserve the
source meanings assessed above. A read-only comparison found exactly one
table anchor and one index entry for each of the 49 identifiers, with the
same glyph, role, scope and notes and its matching page-reference target.

| New physical rows / generated identifiers | Count | Meaning and scope checked |
| --- | ---: | --- |
| 1142-1148 | 7 | P9.4 occurrence lengths, positional cuts, both word/formula directions, subsets, finite aggregates, complete truth patterns and realization points. Empty aggregates and the corrected 7(b) class remain explicit. |
| 1149-1165 | 17 | P15.5 product domains and measures, section types, projections, finite Borel products, Tonelli/Fubini functions and exceptional sets, exhaustions, proof versions, all counterexample parameters, series and subgraph notation. CH/choice and sigma-finite exchange premises remain explicit. |
| 1166-1178 | 13 | P16.2 graph and tuple types, finite structural data, observation and intervention laws, means, total kernels, two-model identification, named examples, binary masses and proof fibers. Inactive allowed edges, dependent disturbances, null parent inputs and do versus conditioning remain distinct. |
| 1179-1190 | 12 | P17.5 finite electorate, arbitrary Arrow alternative domain, finite-rule restrictions, input/output relations, vote counts, scores, candidate rankings, pivot and extreme witnesses, binary domain and sign/reversal operations. Weak social ties and both responsiveness directions remain explicit. |

Verified snapshot hashes:

- handbook/registry/symbols.csv: 1189 data rows,
  EDC2091C85B289ED4C105B12043307928E54A8A54CEAB51B343341B2ECE4B1F5.
- handbook/bib/handbook.bib: 640 entry headers,
  46C6D1BEA7541A50E028422CC5BA0C305B3EAE7C64C57B803B611E49DE2A8F63.
- tmp/edition-2026-bounded-kamp4-probability-decision/kamp7-product-causal-social/symbols-tables.tex:
  63C1B7CEAD23BEF48F4622996528200C05F5E690B0D310C29EB9FF15E16B88B2.
- The sibling symbol-index.tex:
  DD0E3F87596A6D876D4D3E7571C93A7BEB9E5448FA5F0CA6DEE995246664917E.
- spec/research/edition-2026-p17-social-choice.md, read completely:
  E7C9F8F4F2504DCB78BBFDFF96AA667BC437E241F43EB5E3FEB1DE7E4DE80082.

The actual Kamp1968, DurrettPTEAuthor2019, Rubinstein2015LectureNotes and
Pearl2009CausalOverview bibliography entries were read. Pearl's new entry
preserves the article title, author, Statistics Surveys volume 3, 2009,
pages 96-146, DOI and exact UCLA R-350 manifestation. The Durrett entry
distinguishes the January 11 author version from a printed manifestation,
and Rubinstein retains its January 11, 2015 revision of the second edition.

The four active body/annex insertions were checked in actual drivers:
Kamp Lemma 7 follows Lemma 6 in n-c-012 and the P9 annex; product measures
follows integration/expectation in P15; finite causal models follows finite
abduction in P16; social choice follows finite subjective probability in P17.
P15.5, P16.2 and P17.5 therefore match their actual chapter positions.
The P9 presentation route remains under its fourth numbered section,
Temporal logic and automata, so its existing P9.4 scope is preserved.
The main driver reaches all four bodies and annexes, including the P9
logic-in-computer-science route to n-c-012. Each insertion occurs once in
its owning route.

| Route | Verified SHA256 |
| --- | --- |
| handbook/parts/p09/presentations/n-c-012.tex | 1691955B87016E2395A1D6ECC484A0FB715FFEEE664ECECB878E6115D8F9D448 |
| handbook/annex/p09.tex | 3F4EA7CE118A8F6DA03A06A97241FADB1881682C284010E26B324AC78F11F338 |
| handbook/parts/p15.tex | 5691E6A7E7893B62A6B680CD437C43D2A97F4CC92DC3231E43C0E415F231A59C |
| handbook/annex/p15.tex | 3181728DB165FBC1280BA5CFA5F9B4E7BB04B8AC087F9E7CDDBC84C0966C6777 |
| handbook/parts/p16.tex | A7011837E2B58077855CBF622CA7A7BD65830A235784B61A307215E0A1AB94B1 |
| handbook/annex/p16.tex | 6304AE18A090051F30F997CB8F0782DAE457D73F34BCC45BD95C2FAF4D4EECAE |
| handbook/parts/p17.tex | E5F92190B9B7065864ED3FFCACB30A2E40B07E6614D6AB0C0733E5BCACBEF6C2 |
| handbook/annex/p17.tex | 56201E228234AC3BE12E5CCDBC5C845095263198527526DAAC4B360767E31088 |

All eight mathematical-file hashes were verified unchanged from the prior
full reading. This addendum accepts the supplied navigation source snapshot;
it does not claim compiled page numbers, rendered lookup legibility, formal
admission or whole-book publication acceptance. Only this report was edited.

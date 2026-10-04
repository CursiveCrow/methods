# Round 4 source-fidelity, language, and evidence review: `N-c-014.c`

## Result

The frozen Round 4 snapshot is not admissible.  The reader and both research
records describe (k+1) as the corrected homogeneous-degree bound for the
graph of a weight-(k) zero-anticipation finite-memory operator.  That bound is
false under the same artifacts' definition of finite memory, because their
state-transition function may inspect the whole future suffix.  A two-state
operator satisfying every stated hypothesis has four distinct graph portions.

The source note also states the covering-construction lemma without the
nonemptiness case distinction required by the printed proof.  For the empty
homogeneous set, the source's total operator has nonempty image and therefore
cannot have image equal to the empty closure.  The closed-homogeneous
definability theorem remains true, but the proof record must handle the empty
set separately.

## Review boundary and source-language disclosure

I read the board charter and no ledger, chair transcript, earlier-round report,
other Round 4 report, or other board.  Substantive review was limited to the
seven frozen objects, the charter-authorized visual page aids for the two
frozen PDFs, and the controlling Math-Net record/Terms pages needed to verify
identity and rights wording.  No OCR text controlled a word, formula, symbol,
or page number.

My competence is working reading competence in printed mathematical Russian:
I can read the definitions, theorem statements, proof-connective prose,
qualifiers, and Cyrillic/Latin symbol distinctions used in these two papers.  I
am not a credentialed Russian-language specialist and do not supply a
specialist certification of literary nuance.  The mandate is nevertheless
supported here because every used Russian passage was checked in the scan,
formula-by-formula and clause-by-clause, against the bounded English
reconstruction; official English titles came from Math-Net rather than my own
translation.

I used no test, test harness, automated checker, repository script, TeX
command, build, or handbook-PDF inspection.  The evidence was direct
source/manuscript reading, original-detail source-page inspection,
mathematical derivation, live provenance/rights inspection, and the permitted
SHA-256 identity labels.

## M01: frozen identities

All seven SHA-256 values were recomputed before substantive review and match
the Round 4 charter exactly.

| Frozen object | Recomputed SHA-256 | Identity result |
|---|---|---|
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1961.pdf` | `44213AEBE4DB2F1C389B812A7401138799C3DB4749C3605BA7211BBB4BAF96F9` | exact match |
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1962-expanded.pdf` | `EAB4438A7BBA2B6009374826A98A3A61FB6465C493F57B03D2C6C7385824096D` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `D3480007167E06CEDB9FB6ABF847F66F3113A4907B72FA92BE80BAF3378B349A` | exact match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD` | exact match |
| `handbook/bib/handbook.bib` | `75AB70009DF4AB8B2180CFFC6987EA244ADB2F978B1D889C87009EFF17066D5C` | exact match |
| `spec/research/p09-trakhtenbrot-1961-source-note.md` | `A1ED4C1AF0E173AFDEAE98FC7C49BD9BB1C0ED4D72BAF61D6E8AFC1B571D78BC` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `7024F2410F69BD0D4ADFF3B31E9ED316BDB23AE27704984D0691BE0F1A1CC63A` | exact match |

The two PDF byte sizes also agree with the frozen source note: 566,358 bytes
for the announcement and 1,884,181 bytes for the expansion.

## M02--M04: complete visual inspection, identity, access, rights, and language

### Physical-to-printed page maps

Every page was inspected at original detail.

- Announcement physical pages 1, 2, 3, 4 map respectively to printed
  pp. 326, 327, 328, 329.  The scan contains the `Doklady Akademii Nauk
  SSSR` header, volume 140, number 2, the complete body, receipt line,
  bibliography, and the correction concerning the earlier cited paper.
- Expansion physical page (n) maps to printed page (n+102) for every
  (1\leq n\leq29).  Physical page 1 is the opening p. 103 (the opening page
  does not display a page numeral in the visible scan); physical page 2 is
  visibly p. 104, and the remaining visible pagination continues without a
  gap through physical page 29, p. 131.  All five sections, receipt line, and
  bibliography are present.

### Identities and source order

The visual bodies, bibliography entries at `handbook/bib/handbook.bib:5991-6013`,
reader at `handbook/parts/p09/presentations/n-c-014.tex:487-510`, source note at
`spec/research/p09-trakhtenbrot-1961-source-note.md:20-69`, and compact record at
`spec/research/p09-source-presentations-lot2-3.md:646-648` agree on the
following:

- the registered announcement is B. A. Trakhtenbrot, the Russian title
  `Конечные автоматы и логика одноместных предикатов`, *Doklady Akademii Nauk
  SSSR* 140(2) (1961), pp. 326--329;
- the complete expansion has the same Russian title and is *Sibirskii
  Matematicheskii Zhurnal* 3(1) (1962), pp. 103--131;
- Math-Net's official English rendering is “Finite automata and the logic of
  single-place predicates” for 1961 and “Finite automata and the logic of
  one-place predicates” for 1962;
- the 1961 scan records presentation by P. S. Novikov on 16 May 1961 and
  receipt on 29 April 1961; the 1962 scan records receipt on 15 May 1961;
- the Math-Net routes `dan25511` and `smj4799` are live and agree with the
  journal, year, volume, issue, pagination, language, and official English
  titles; and
- the later AMS translation is recorded only as an unacquired bibliographic
  route and is not used as textual evidence.

No title, theorem number, pagination, or proof detail is transferred silently
between the announcement and expansion.

### Controlling rights wording

I checked the current controlling
[Math-Net Terms of Use](https://www.mathnet.ru/php/agreement.phtml?option_lang=eng)
directly.  The operative exception says that the named individuals “may print
copies ... for noncommercial use in teaching or research.”  The same Terms say
that reproduction or republication requires the copyright holder's written
permission and separately prohibit systematic downloading without written
permission.

The source note at lines 71--77 and compact record at line 648 paraphrase the
exception as permission for individual teachers, students, and researchers to
print copies “for noncommercial teaching or research.”  Although that is not a
verbatim quotation, it preserves the subject, permitted act, noncommercial-use
limit, and teaching/research purposes.  The records correctly infer neither an
open-content licence nor electronic-copy or redistribution permission, and
they treat the local PDFs only as research objects.  I find no rights
inflation.  I27 is checked clean against the controlling wording, not merely
against the charter's paraphrase.

## Blocking and must-fix findings

### R4-SF-01 — blocker — the (k+1) graph-degree “correction” is false under the frozen definition of weight

**Frozen locations.** The reader defines finite memory using state-update and
output maps on the entire future suffix and defines weight as the least state
cardinality at
`handbook/parts/p09/presentations/n-c-014.tex:538-551`; it then claims that a
weight-(k) zero-anticipation graph has at most (k) nonempty portions plus
the empty portion, hence degree at most (k+1), at lines 582--604.  The same
claim occurs at `spec/research/p09-trakhtenbrot-1961-source-note.md:154-169`
and 203--213 and at
`spec/research/p09-source-presentations-lot2-3.md:652`.  The controlling source
prints the whole-future finite-memory equations on expanded p. 110, defines
weight and finite operators on pp. 110--111, defines portions and homogeneity
on pp. 114--115, and prints the disputed (k)-homogeneous graph claim on
p. 115.

**Counterexample.** Let the input and output alphabets both be
({0,1}).  Define the zero-anticipation operator (T) by

\[
 T(x)(t)=
 \begin{cases}
   x(t),&x(1)=1,\\
   0,&x(1)=0.
 \end{cases}
\]

This is causal: the output at (t) uses only (x(1)) and (x(t)).  It has a
two-state realization of exactly the broad form printed on expanded p. 110.
With (Q=\{0,1\}), (q(1)=0), and, for a current suffix
(z=(z_0,z_1,\ldots)), put

\[
 \Phi(q,z)=(1-q)z_0,
 \qquad
 \Psi(q,z)=q\mathbin{\mathsf{xor}}z_0\mathbin{\mathsf{xor}}z_1.
\]

Induction gives (q(t)=x(1)\mathbin{\mathsf{xor}}x(t)).  Hence the displayed
output equation is (x(t)) when (x(1)=1) and (0) when (x(1)=0), exactly
as required.  The realization is permitted because the frozen definition
allows (Psi) to inspect (x(t+1)).

The weight is exactly two, not merely at most two.  With one state the output
would have the same suffix-functional form (F(x_{\geq t})) at every time.
At (t=1), the definition of (T) forces (F(z)=z_0) for every suffix (z).
For an input beginning (0,1), that would force output (1) at time 2,
whereas (T) outputs (0).

Let (Gamma_T) be the graph.  Four pairwise distinct portions occur already
at depth one:

\[
 \Gamma_T,
 \qquad
 (\Gamma_T)_{(0,0)}=\Gamma_{0},
 \qquad
 (\Gamma_T)_{(1,1)}=\Gamma_{\mathrm{id}},
 \qquad
 (\Gamma_T)_{(0,1)}=\varnothing,
\]

where (Gamma_0) is the graph of the constant-zero operator and
(Gamma_{\mathrm{id}}) is the identity graph.  Thus the graph has degree at
least four, while the frozen formula gives (k+1=3).

**Why the frozen derivation fails.** A state reached after a prefix need not be
determined by that prefix when (Psi) can inspect the future.  In this example
the two-state realization has three different compatible residual operators:
the initial operator, the constant-zero residual after input (0), and the
identity residual after input (1).  The statement “one nonempty residual per
reachable memory state” is therefore invalid for the stated notion of weight.
The handbook's empty-portion observation is correct but does not exhaust the
source defect.

**Required minimum repair.** Do not bound graph degree by broad finite-memory
weight without a new proof.  A safe exact statement is that if (r) is the
number of distinct compatible residual operators, then the all-prefix graph
degree is at most (r+1), the extra member being the possible empty portion.
Equivalently, the (k+1) bound may be retained only when (k) counts states
in a prefix-determined zero-lookahead canonical realization, not when (k) is
the weight defined at reader line 551.  The reader, source note, and compact
record must all use the same corrected standing and must label the full repair
as handbook-owned.

**Reader harm.** As frozen, the handbook advertises a mathematically false
numerical repair as an exact correction of the historical source.  This
violates I07--I09, I25, M07, M09, M24--M25, and M27 and blocks source-faithful
admission.

### R4-SF-02 — must-fix — the covering-construction record silently assumes the homogeneous set is nonempty

**Frozen locations.** The source note says without qualification that the
covering construction chooses a permitted next bit at every basis member and
that its image is exactly the closure of the original homogeneous set at
`spec/research/p09-trakhtenbrot-1961-source-note.md:220-223`.  The reader's
closed-homogeneous theorem statement is at
`handbook/parts/p09/presentations/n-c-014.tex:610-632`.  The controlling
construction and lemma are on expanded pp. 115--116; the resulting closed-
homogeneous definability theorem is on p. 118.

**Counterexample to the proof sentence.** Take (M=\varnothing).  It is
closed and homogeneous: its only portion is (arnothing).  Expanded p. 115
allows the output function (Phi) to take arbitrary values at an empty basis
member, on the assertion that such values will not be used.  But the initial
basis member is (M) itself.  The operator in equation (1') on p. 116 is
total, so it produces an output for every parameter stream (U); its image is
therefore nonempty and cannot equal
(\overline M=\varnothing).  The proof of the lemma on p. 116 begins by using
the nonemptiness of every prefix portion, which is false in this case.

**Required minimum repair.** Qualify the covering-operator construction and
its image/closure lemma by (M\ne\varnothing).  Handle (M=\varnothing)
separately in the converse theorem by a contradiction formula (which already
has the required recurrent syntactic shape).  The theorem “every closed
homogeneous set is (mathcal I)-definable” remains correct; only the frozen
proof record is overbroad.

**Reader harm.** The note presently records a universally quantified proof
move that fails on the smallest allowed homogeneous set, while elsewhere the
same reconstruction correctly insists that empty portions and the empty word
cannot be discarded.  This violates I09--I12, I25, M09, M11, M24--M25, and
M27 and must be repaired before admission.

## Clean source-fidelity determinations

### Formal system and normal form: M05--M06

Checked clean against announcement pp. 326--327 and expanded pp. 103--109.
The reader correctly identifies Cyrillic И as the interpreted formal language
rendered (mathcal I), not an automaton or theorem.  Individuals range over
(1,2,\ldots), predicate variables over arbitrary subsets, and immediate
successor is primitive.  Equality, order, bounded individual quantifiers,
constants, and (t+k) are eliminable conveniences.

“Fictitious outside” is correctly translated as semantic independence from
changes outside the stated interval.  Lower (t)-formulae have bounded-prefix
dependence through (t+s); upper (t)-formulae have tail dependence from
(t).  The reported proof architecture is present: predicate-prenexing,
inward movement and splitting of individual quantifiers at (t), then
distribution of predicate quantifiers across independent prefix and tail
parts.  Announcement Theorem 1 and the expanded unnumbered normal-form theorem
are not conflated.

### Operator definitions and negative boundary: M07--M08

Apart from the false degree consequence in R4-SF-01, the operator definitions
are source-faithful to expanded pp. 109--113.  The map is total and typed;
anticipation (p) is independence from positions after (t+p); zero
anticipation is the extension-independent prefix condition; finite-memory
equations retain the whole suffix; weight is least state cardinality; and a
finite operator adds bounded anticipation.  The announcement's Cyrillic
Л-class and expansion's Latin (A)-class are distinguished and the reader's
normalization is explicit.

The one-state example correctly retains unbounded, potentially noneffective
future dependence.  The two primitive-recursive negative arguments are kept
at their printed strength: deciding eventual periodicity and uniformly
extracting finite-state equations are not available in that overly broad
synthesis language.

### Homogeneity, definability, and effectiveness: M09--M12

The definitions of portion, coordinatewise extension, degree, basis, and
internal transition match expanded pp. 114--115 and have the correct standing
as properties/data of a stream set.  The singleton/ultimate-periodicity claim
and the uncountability-versus-countable-formula counterexample are correct.
The empty-portion objection to the source's printed (k) bound is also
correct, but R4-SF-01 shows that (k+1) is not the full repair when (k) is
broad finite-memory weight.

Independently, the normal form leaves only finitely many canonical lower-window
Boolean functions after a prefix, so only finitely many formula portions can
occur; appending one input column computes the internal transition
syntactically.  This verifies the definable-to-homogeneous direction and the
unconditional internal-transition construction on expanded pp. 116--118.

For a nonempty closed homogeneous set, a finite basis and permitted one-bit
extensions yield a finite recurrent system.  Every produced finite prefix is
compatible with the set, and Cantor closedness turns compatibility at every
length into membership.  Conversely, the recurrent existential-predicate form
is the projection of a closed local relation over a compact product and is
therefore closed; its finitely many Boolean state valuations give homogeneity.
The empty set requires the separate contradiction case identified in
R4-SF-02.  With that case distinction, the closed-homogeneous converse and the
closure characterization by complement, finite union, and predicate
projection are correct.

The internal transition is obtained without a truth oracle.  External output
selection requires nonemptiness/truth decisions, so the arbitrary
(mathcal I)-formula construction remains conditional.  Putnam removes that
condition only for the stated existential-predicate recurrent fragment.  No
later result is laundered into the source-time claim.

### Explicit synthesis and finite words: M19--M21

Checked clean against expanded pp. 124--131.  The explicit-definition
standing, finite-memory conclusion, anticipation criterion, zero-shift
residual-formula termination, canonical equations, and the two-formula/two-
table worked example on pp. 126--127 are accurately bounded.

The induced maps (T_t:A^t\to B^t) are well typed, extension-independent, and
prefix-compatible.  Automaton-enumerability is stated length by length, while
automaton-decidability uses the terminal recognizer output.  The forward
direction of expanded Section 5, Theorem 2 is correct.  The frozen reader also
correctly identifies the empty language as a counterexample to the printed
converse and adds the necessary nonemptiness hypothesis; prefix closure and a
proper longer extension then supply a word at every positive length, including
the seed required on p. 128.

The weak system (mathcal I'), eventual-zero predicate range, and “special
beginning” are correctly distinguished from an arbitrary prefix.  Expanded
Section 5, Theorem 3 is reported with existence for an arbitrary
(mathcal I)-formula and effective construction in the (mathcal I') case,
including the source's explicit attribution to Büchi.

### Theorem numbering, modern theorem, records, and terminology: M22--M28

Announcement Theorems 1--5 and (4') are kept at announcement pagination and
strength; expanded Sections 1--5 and Theorems 1--3/3' are kept at expanded
pagination and strength.  The finite-memory conclusion without continuity is
not turned into finite-operator standing; graph equality is not confused with
solution containment; the two quantifiers in “general solution” are present;
and fixed (p) is not inflated to one unbounded-lookahead parametrization.

The shared theorem at
`handbook/parts/p09/logic-in-computer-science.tex:811-825` explicitly labels
the regular/MSO sentence as modern and lists the distinct Büchi, Elgot, and
Trakhtenbrot packages.  The Thomas paragraph at
`handbook/parts/p09/presentations/n-c-014.tex:789-807` is a later proof route,
not wording attributed to either Russian body.  The source-navigation paragraph
at `handbook/parts/p09/logic-in-computer-science.tex:2341-2347` preserves the
announcement/expansion pair.  No compound-name folklore is laundered into a
literal Trakhtenbrot theorem.

Except for R4-SF-01 and R4-SF-02, the source note, compact record, reader,
shared theorem, bibliography, and consolidated acquisition status agree.  The
status text says body-sufficient and reconstructed, not admitted, built,
visually verified as handbook pages, human-accepted, or complete beyond
`N-c-014.c`.

The AGENTS terminology audit is otherwise clean.  Every reader-facing name
needed here is introduced with an exact definition or declared source
normalization, its standing is explicit, its distinction from neighboring
terms is used later, and no speculative “chain” object or unused named
machinery appears.  The topic boundary, translation boundary, rights boundary,
and no-test/no-build boundary are explicit.

## Mandatory-coverage disposition

| Point | Disposition |
|---|---|
| M01 | checked clean: all seven hashes exact |
| M02 | checked clean: all 4+29 pages at original detail; maps 1--4 to 326--329 and 1--29 to 103--131 |
| M03 | checked clean: identities, journals, years, volumes/issues, pages, titles, routes, source order, and controlling rights boundary |
| M04 | checked clean with the competence limitation stated above; no specialist certification implied |
| M05 | checked clean |
| M06 | checked clean |
| M07 | finding-linked to R4-SF-01 for the consequence drawn from the otherwise correct whole-suffix definition |
| M08 | checked clean |
| M09 | finding-linked to R4-SF-01; the empty-portion observation alone is insufficient |
| M10 | checked clean by independent finite-residual derivation |
| M11 | finding-linked to R4-SF-02; theorem true, empty-set proof case omitted |
| M12 | checked clean |
| M13--M18 | not allocated to this seat for independent proof verdict; their printed source statements and locators were nevertheless checked under M22/M25, with no additional source-fidelity finding |
| M19 | checked clean |
| M20 | checked clean, including both directions and the handbook-owned nonempty repair |
| M21 | checked clean |
| M22 | checked clean |
| M23 | checked clean |
| M24 | finding-linked to R4-SF-01 and R4-SF-02; otherwise reconciled |
| M25 | finding-linked to R4-SF-01 and R4-SF-02; all other locators, theorem numbers, formulas, citations, titles, and qualifiers checked clean |
| M26 | checked clean apart from the false standing attached to “weight” in R4-SF-01 |
| M27 | finding-linked to R4-SF-01 and R4-SF-02; no other laundering, collapse, hidden topology, or completion inflation found |
| M28 | checked clean |

## Invariant disposition

| Invariant(s) | Disposition |
|---|---|
| I01--I06 | checked clean |
| I07--I08 | definitions checked clean; R4-SF-01 shows that their broad whole-future state standing invalidates the later numerical inference |
| I09 | rejected by R4-SF-01; the asserted (k+1) bound is false for broad weight |
| I10 | checked clean |
| I11 | theorem/formula checked clean; R4-SF-02 requires the empty-set proof case |
| I12--I13 | checked clean |
| I14--I20 | source-statement fidelity checked clean at the distinct theorem strengths and locators |
| I21--I24 | checked clean |
| I25 | rejected to the extent of the two false/overbroad evidence claims |
| I26 | checked clean apart from the erroneous weight standing in R4-SF-01 |
| I27--I30 | checked clean |

VERDICT: REJECT — R4-SF-01, R4-SF-02

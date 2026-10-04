# Edition 2026 C6 / R-002: arithmetic verification preparation

Date: 7 September 2026. This is read-only mathematical preparation for the actual bespoke-numbering theorem. No manuscript, code, registry or provenance file was edited, and no test, build, render, acquisition or delegation was performed.

## Five-minute checkpoint

The two assigned files have been read in full, together with the actual machine/input/output convention and program numbering. The pairing and beta lemmas already have supplied proofs. The missing work is the literal h1–h4 verification formula and its two semantic directions.

One prerequisite is genuinely unspecified in the active text: the serialization of a normalized machine description is called a “table tuple” or “description tuple,” but the entry fields, direction codes and placement of state/tape/input-alphabet metadata are not fixed. The h2 text refers to fixed-depth row unpacking without supplying that depth or field order. Likewise, the history definition promises fixed family tags and configuration coding without choosing them. These conventions must be completed explicitly before an exact formula for this numbering can be proved; a generic standard T-predicate is not an adequate replacement.

The arithmetic language itself is sufficient. Finite histories can store the large base-expansion values as beta entries, so bounded checking uses addition and multiplication only. No exponentiation symbol or polynomial bound on the size of the witness s is needed.

## Current evidence and exact read scope

All locators are actual active files under handbook/restoration.

| File | Read scope and role | SHA-256 |
| --- | --- | --- |
| inherited-07506-07677.tex | 1–172: two-sided tape, total nonhalting transition function, input/output and tuple conventions | EB27FE6DE9A8FFBBE3EC6F317DFF66D97DDE72F22B1FA3FCB48A4304D85F3C7D |
| inherited-07851-08048.tex | 1–198: designated slots, table numbering, enumeration and simulation/compiler boundaries | 436DE76199BCD67D4E55252CA92D47A3046701AC028E79484395E5C0EDE6B7B8 |
| inherited-08306-08438.tex | 1–71: exact arithmetic language and marked-bounded syntax | 0B020970BE72999CD771566BA0D6CDB4E4668728362CBD3C0D1606059EE9D2B8 |
| inherited-08439-08709.tex | 1–271: pairing graph, beta, contraction, bounded collection and prefix normal form | 95EB4270559303FEFC5DE2D9BC804A04768EAD87D68D9E5D9CBF65079714806A |
| inherited-08710-08876.tex | 1–167: history definition, omitted verification and hierarchy consumers | 2B00900E80D8D0A97CD6779A632E8821F2A51937164F72238CFEF179FE18934C |
| inherited-09262-09327.tex | 1–66: numeralwise representation and cited representability theorem | 75A27E87080116A235A904DAEDABE2A70DFF472BA27CA8A454C448DFD4B58BB6 |
| inherited-09328-09438.tex | 1–111: syntax coding and fixed proof/provability predicates | F5A14F098311611F5942A7E0F9F5B348B52C1AADFCA2E1FF129E5F63A977F6A0 |

The P4 driver at lines 54–66 reaches the two assigned files; the P5 driver at 11–19 reaches representability and arithmetization. The derivability-condition interface at inherited-09750-09816.tex:1–43 was also read.

The local manuscript is the primary authority for this bespoke numbering: inherited-07851-08048.tex:148–152 says expressly that the external Kleene treatment is parallel reading and does not define these indices. The assigned passages cite Gödel1931, Shoenfield1967 and BoolosBurgessJeffrey2007, but no body of those external books/papers was newly read in this block. Their citations cannot fill the missing local row serialization by themselves.

## What is already supplied, and what is actually omitted

The quantifier-free pairing graph is

\[
 \mathsf P(a,b,z)\equiv(a+b)(a+b+1)+2b=2z.
\]

Its exact relation to the fixed numerical pairing and the bounds a,b <= z are proved at inherited-08439-08709.tex:1–25. The bounded beta formula, functionality, value <= s and finite-sequence existence are proved at 37–83. The existence proof uses the Chinese remainder theorem; that remains its explicit mathematical dependency. The prefix-form transfer is supplied at 164–269 and should not be reproved as a substitute for h1–h4.

The omission is explicit at inherited-08710-08876.tex:77–80. The definition at 3–34 does not yet provide:

- actual tag constants, header entries and a flattening convention for time/cell families;
- a fully determined normalized-description tuple and fixed-depth row layout;
- canonical-input conditions, including the zero input and no-leading-zero condition;
- a finite representation of the two-sided tape, its width/origin and expansion certificates;
- the complete initial/step/final formula and every symbol/state/direction range check;
- extraction bounds for composed family indices, as distinct from the entry values themselves;
- the detailed converse from a satisfying s to an actual accepting run.

## Bounded helper formulas to author first

The language is exactly {0,S,+,times}, with equality logical. Pairing, beta, sequence-entry notation and every relation below must be eliminable formula abbreviations, not added function symbols.

For fixed tag t, a usable entry relation is

\[
 E_t(s,j,v):=
 \exists i<(t+j+1)^2+1\,
       \bigl(\mathsf P(t,j,i)\land\mathsf B(s,i,v)\bigr).
\]

The square denotes the product of the displayed term with itself. Prove the upper bound pair(t,j) <= (t+j+1)^2; the existing pairing lemma gives lower bounds on components, not this upper bound. For two-dimensional arrays use j=pair(time,cell) through another bounded P graph. Fixed-depth nesting gives a fixed polynomial term bound. A pair/tag index need not be <= s even though every extracted beta value is <= s.

Use marked comparisons throughout:

\[
 \operatorname{LT}(u,v):=\exists z<v\,(u+Sz=v),\qquad
 \operatorname{LE}(u,v):=\exists z\le v\,(z+u=v).
\]

All inserted z variables must be fresh. Bare comparisons expand to unbounded existentials in the actual language convention. Every occurrence of a subscripted family value in the schemas below must be replaced by a value variable <= s with its E_t extraction conjunct. A source-level family such as d_j is not an arithmetic term.

## h1: canonical input and certified binary expansion

Store L >= 1, digits d_j and prefix values v_j for j<L. Use the following conditions:

\[
\begin{gathered}
 L=S\ell,\quad d_j=0\lor d_j=1,\quad v_0=d_0,\\
 \forall j<\ell\quad v_{j+1}=2v_j+d_{j+1},\qquad
 v_\ell=x,\qquad \forall j<L\ \operatorname{LE}(v_j,x),\\
 (x=0\land L=1\land d_0=0)\ \lor\
 (\operatorname{LT}(0,x)\land d_0=1).
\end{gathered}
\]

Bound L, ell and all extracted values by s; use successor terms for j+1. The final line enforces the earlier canonical bin(x), rather than allowing a leading-zero word that a machine might treat differently. Prove uniqueness of the word by positional binary evaluation. The numerical bits 0/1 must be translated to the tape-symbol numbers 1/2 by adding one in the initial-tape clause.

## h2: exact table extraction and validity

Retain the existing outer equation P(k,c0,e), the right-nested code_k convention, and the decoding chain P(r_i,c_{i+1},c_i), terminating with r_{k-1}=c_{k-1}. Handle k=0 and k=1 explicitly; valid numerical machines have a nonempty full table, while the tuple convention itself has zero- and one-arity clauses.

The author must first fix the missing machine-description serialization. It must record or uniquely recover the state count n, tape base b, input-alphabet membership, and the ordered row list. State and symbol counts must be at least three; designated state codes are 0/1/2 and designated blank/digit codes are 0/1/2.

A natural proposed row format is code_5(q,a,q',a',d), with d=0 for L and d=1 for R. This is a proposal, not a claim that the current text has already chosen it. Its fixed-depth pairing graph is explicit once those five fields are fixed.

Validity must say that every nonhalting key (q,a), q<n, q != 1,2, a<b occurs exactly once, rows occur in lexicographic key order, output states/symbols lie in range, and direction is one of its two codes. The input alphabet must exclude blank, be a subset of the tape alphabet, and contain symbol numbers 1 and 2. One cannot silently discard the input-alphabet component and call this the already fixed numbering.

Every tuple component is bounded by its containing pairing code. Counts and table-array values may alternatively be recorded in the history, but their agreement with the actual decoded description must be checked. Merely storing a guessed table in s without proving that it decodes e would verify a different relation.

## h3: finite two-sided tape and exact local transition

A concrete compatible layout is a single fixed window for the whole run. If T is the number of transitions and L the canonical input length, set

\[
 H=T,\qquad W=L+2T+1.
\]

Column j<W represents physical cell j-H. Store states q_t, shifted head positions h_t, tape digits a_{t,j} and base-b prefix values u_{t,j}, for t<=T and j<W. Store the complete tape code z_t=u_{t,W-1} if h3 retains its assertion that each tape is coded in base b.

Check a_{t,j}<b and

\[
 u_{t,0}=a_{t,0},\qquad
 u_{t,j+1}=b\,u_{t,j}+a_{t,j+1}.
\]

These witnesses may be very large, but they are finite and can be beta entries bounded by s. They avoid a nonexistent exponentiation symbol. Fixed width permits leading blank digits without ambiguity.

Initial conditions are q_0=0 and h_0=H. For every i<L require a_{0,H+i}=d_i+1; every other j<W is blank 0. Thus the input occupies the correct physical cells 0,...,L-1, most significant bit first.

For every t<T, require q_t != 1,2 and select the unique decoded row (q,a,q',a',d) with q=q_t and a=a_{t,h_t}. Require q_{t+1}=q' and

\[
 (d=0\land h_{t+1}+1=h_t)
 \ \lor\
 (d=1\land h_{t+1}=h_t+1).
\]

For every j<W require

\[
 (j=h_t\to a_{t+1,j}=a')
 \land
 (j\ne h_t\to a_{t+1,j}=a_{t,j}).
\]

Bound every shifted head by W and every row-selection index by the decoded table length. The arithmetic expression a_{t,h_t} is implemented by an E_t extraction, not variable subscripting in the arithmetic language.

Prove that an actual T-step run never moves its head outside physical [-T,T]. The width above contains the whole initial input and every changed cell; it also leaves an unchanged blank to the right. Extending every represented tape by blank outside the window yields an actual two-sided tape. Conversely, initial equality and the cellwise update clauses give exactly the source transition relation, not merely a sequence of plausible configurations.

## h4: accepting state and canonical output prefix

Require q_T=1. Store an output length m>=1 and a value y, both bounded by s, with H+m<W. Require a_{T,H+m}=0 and, for every i<m, a_{T,H+i}=o_i+1 with o_i=0 or 1. This makes m the first blank at a nonnegative physical cell. Use stored prefix values w_0,...,w_{m-1} with

\[
 w_0=o_0,\qquad w_{i+1}=2w_i+o_{i+1},\qquad w_{m-1}=y,
\]

and the same zero/no-leading-zero alternative as h1. Negative cells, cells beyond the first blank, and the final head position impose no further output restrictions, matching inherited-07506-07677.tex:111–123.

Acceptance without a valid output must fail this clause; rejection and divergence must have no successful certificate. Do not require the raw decoded machine to be the separately described output-cleaning wrapper: the indexed partial function already recognizes exactly valid raw accepting outputs.

## Assembly and full proof obligations

Once the serialization and tags are fixed, write

\[
 \mathsf{Comp}(e,x,s):=
 \exists(\text{header values}\le s)\,
 [\operatorname{Header}\land H_1\land H_2\land H_3\land H_4],
\]

where each H_i is the displayed finite formula obtained from the schemas above, all loops are bounded quantifiers, and every array lookup is expanded by E_t and P/B. This displayed schematic line is the authoring target, not the completed missing formula.

Prove two separate directions:

1. A satisfying s decodes a valid normalized program e, a canonical input, and an actual finite accepting run with a valid output. Prove each extraction/step direction, including width boundaries, invalid indices and halting states.
2. Any actual accepting numerical computation gives finitely many header, decoding, digit, prefix and configuration values at explicitly indexed positions. Fill unused positions up to the greatest used index with zero and apply the existing beta existence lemma. The chosen code automatically bounds all stored values by s. Indices depend on the finite run data, not on the eventual chosen s, so there is no circular certificate construction.

No uniform polynomial bound on s in e,x is claimed or needed. Do not invoke a generic c.e.-is-Sigma1 or representability theorem to establish this direction: the immediately following c.e. characterization uses Comp and would make that proof circular.

## Concrete authoring decomposition

| Package | Main active home | Required output and pass condition |
| --- | --- | --- |
| C6.0 Fix the exact serialization | 07851-08048:7–39 and 08710-08876:3–34 | Full description/row/tag layout and all zero conventions, compatible with the source tuple and machine semantics. No unchosen field order or guessed table remains. |
| C6.1 Bounded extraction | 08439-08709:1–83, then 08710 | Fixed-tag and paired-index formulas, explicit term bounds, and correctness/functionality. Preserve existing P/B proofs and mark any newly supplied bound. |
| C6.2 Input and table | 08710:10–22 | Literal H1/H2 and proofs of canonical bin(x), exact e decoding and all validity clauses. |
| C6.3 Tapes and steps | 08710:23–27 | Width/origin definition, certified base expansions, initialization, every changed/unchanged cell and both head moves, with both simulation directions. |
| C6.4 Output and assembly | 08710:28–80 | Literal H4 and assembled bounded Comp; actual-run-to-code and code-to-run proofs; reject malformed output and invalid program codes. |
| C6.5 Consumers | 08710:89–107 and P5 interfaces below | Update only statuses whose complete obligations are now met; give the c.e. witness-search direction explicitly and keep the cited/unfinished P5 internal representation work separate. |

## P5 dependency boundary

The completed C6 theorem would establish truth in the standard structure N. It does not by itself establish what Q proves about every code or what PA proves internally about proof transformations.

- inherited-09262-09327.tex:31–48 gives the distinct cited numeralwise-representability theorem and the Sigma1 definability clause.
- inherited-09328-09438.tex:46–63 still has a syntax-arithmetization sketch, including proof rules and c.e.-axiom enumeration certificates.
- Its definition at 65–84 chooses a primitive-recursive proof relation and a specific Sigma1 formula representing it, then defines Prov_T(x)=exists p Proof_T(p,x). The additional existential merges with the initial block. It explicitly links its sequence apparatus to the beta lemma.
- inherited-09750-09816.tex:7–43 uses that fixed predicate for D1–D3. Internal proof concatenation and internal verification remain additional obligations; they are not supplied merely by the standard-model Comp theorem.

The notation-sharing claim in P5 is defensible as reuse of the same beta extraction machinery, not as proof that the machine history code and the chosen syntax/proof numbering are literally identical. Any change to the still-unspecified program serialization must be reconciled with the enumeration, universal simulation and parameter-compilation interfaces at 07851-08048:85–197; it must not silently replace the promised numbering by another standard one.

## Final preparation status

The arithmetic language admits the proposed bounded checks, and the current pairing/beta lemmas provide the right substrate. The immediate obstruction to writing the exact promised formula is missing serialization and history-layout data, not insufficient arithmetic operations. This note supplies a concrete next decomposition and formulas, without installing a speculative numbering or claiming that the missing Comp formula has already been written.

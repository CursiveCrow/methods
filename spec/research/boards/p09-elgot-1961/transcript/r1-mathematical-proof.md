# Blind mathematical and proof-correctness review — Elgot 1961, N-c-014.b

## Seat, snapshot, and review boundary

I reviewed the frozen N-c-014.b snapshot as the mathematical and proof-correctness seat. I did not read the board ledger, the chair transcript, a Büchi board, another board transcript, or another verdict, and I did not contact another reviewer. I edited no frozen artifact. I ran no test, automated checker, repository script, TeX command, build, or handbook-PDF inspection. Evidence below is limited to direct reading, original-detail source-image inspection, mathematical derivation, provenance/citation inspection, and SHA-256 identity computation.

Before substantive judgment I independently recomputed all eight frozen SHA-256 identities. Every value matched the charter:

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| elgot-1961-trans-ams.pdf | DE2F9587F72075C94C7071A00002D1129AA8148C498F9A4D6F75968EB46ACD74 | match |
| elgot-1959-umr1342.pdf | 596A599A7DF12F122BB2D875255B050695EC84A5A22F3488844D5876F3211D74 | match |
| elgot-1962-errata.pdf | B13E422FC03DDA61B93A1B782F40882AE90DBC8886945B26A42376A96ED34EC1 | match |
| n-c-014.tex | C37C4F9F7D093D75DD33E90FBD6050C55F147B3C7A71933D8891D4DDF46AF20A | match |
| logic-in-computer-science.tex | 1690DED84FC257B50BC5B44E094E382D8A79B176E7BB9C21D0845DAEC59629B8 | match |
| handbook.bib | 6F98B6EB38B2B935DACC0C7E8373E1B12A5BB70FCAAC172D11BAFCDACA8C502F | match |
| p09-elgot-1961-source-note.md | 292B5EFD5972B27DC5043AF39FE20B1AB3ABE487290C3699031A79ED18472DA7 | match |
| p09-source-presentations-lot2-3.md | 12CAA5ADB48E78D809F3EE6C8EA6FFBF98C504E0F7920A555DD9C378824ACAC7 | match |

I visually inspected at original detail journal render pages 01–31 (printed pp. 21–51), report render pages 01–60, and both errata render pages. The source maps are complete. The report has cover/funding on physical pp. 1–2; acknowledgments, contents, and abstract on pp. 3–5 (printed iii, v, vi); numbered report pp. 1–50 on physical pp. 6–55; four distribution leaves on pp. 56–59; and a barcode endpoint on p. 60. The Elgot errata begins on printed p. 558 and continues on p. 559. The January 1961 Transactions article controls the body, the June 1959 UMR1342 report is a precursor, and the June 1962 Transactions errata controls correction. The frozen DOI, handle, access-route, and research-copy/no-open-licence qualifications agree with those identities.

## Findings

### MP-01 — Must-fix — the exact syntactic hypothesis of §8.6 is replaced by an undefined “local” condition

- Manuscript location: n-c-014.tex lines 403–410, especially line 410; the unexplained descriptor first appears at lines 301–311.
- Controlling source: journal p. 46, §8.6.2; report numbered p. 41; frozen source note lines 284–292.
- Invariant: I16 and I20; mandatory points M17, M19, and M25.
- Problem: The manuscript says only that M is “quantifier-free and local in the displayed variables.” Elgot's hypothesis is more exact: M has only the displayed variables free, may contain numerals, and contains neither equality nor order. Its relevant terms are successor iterates x^(h) and 0^(h), and n is one more than the greatest occurring offset. “Local” has no eliminable definition at first use, no stated metalinguistic standing, and no nonredundancy account. It therefore neither satisfies the supplied AGENTS rule nor preserves the theorem's literal domain.
- Derivation and harm: The finite-union proof expands M into finitely many truth patterns on a bounded window of characteristic columns. That step is licensed by the exact term and atom restrictions, not by quantifier-freeness alone. A graduate reader cannot recover from “local” which atoms and terms are allowed, whether equality and order are excluded, how numerals enter, or which occurrences contribute to the window length. The later reduction consequently hides a hypothesis on which it depends.
- Minimum repair: Replace the compression at lines 403–410 by the literal restrictions: M is quantifier-free; only a, b, s, x are free; numerals are allowed; equality and order are forbidden; and n = 1 + max h over occurrences of x^(h) and 0^(h). If “local” is retained, introduce it there as a metalinguistic abbreviation for exactly those clauses and state its use.

### MP-02 — Must-fix — the purported general tagging construction is only written as binary and does not handle the unary-window edge case

- Manuscript location: n-c-014.tex lines 420–435, especially lines 425–433 and the unrestricted conclusion at lines 434–435.
- Controlling source: journal p. 46 for the false printed third sentence; errata pp. 558–559, especially p. 559's qualification “if the R_j's are r-ary relations, r >= 2”; report numbered p. 41 shares the false sentence.
- Invariant: I14–I16; mandatory points M18, M19, and M25.
- Problem: The manuscript correctly says each S_j is governed by an n-ary R_j, but defines the tagged relation only in binary notation,

  <a,j> R'_j <b,j> iff a R_j b,

  and then claims without qualification that this reduces every finite union to one local sequence set. It gives neither the componentwise n-ary definition nor a treatment of n = 1. The erratum's displayed particular construction expressly assumes arity at least two.
- Derivation: For n >= 2, the valid definition is

  R'_j = {((a_0,j),...,(a_(n-1),j)) : (a_0,...,a_(n-1)) in R_j},

  with E'_j tagged componentwise. Consecutive length-n windows overlap, so a valid infinite tagged sequence has one constant tag, and its projection lies in exactly one S_j. For n = 1 that overlap argument disappears. Under the natural unary reading, take S_1 = {0^omega}, S_2 = {1^omega}, R_1 = {0}, R_2 = {1}, and the matching one-letter prefix sets. The union of tagged unary relations admits

  (0,1),(1,2),(0,1),(1,2),...

  whose projection 0101... lies in neither S_1 nor S_2. Thus the asserted projection equality is not proved for the smallest window allowed by n = 1 + max h.
- Harm: Lines 434–435 use the construction as the bridge to a regular finite-prefix language and Theorem 8.1. As written, the proof has an arity/edge-case gap exactly where the manuscript claims to repair the printed error.
- Minimum repair: Define R'_j and E'_j componentwise for all n >= 2, explain why overlap makes the tag constant, and handle n = 1 by first promoting every unary constraint to a binary constant-tag relation, or by an equivalent finite-state construction that carries j permanently. State the projection equality only after these cases, and only then invoke §8.5 and Theorem 8.1.

### MP-03 — Must-fix — the report comparison says one corrected occurrence rather than both

- Manuscript location: n-c-014.tex lines 455–462, especially line 457.
- Controlling source: report numbered p. 4; errata printed p. 558, which says “Lines 10, 11. Replace each f-hat by p-hat”; frozen source note lines 94–98.
- Invariant: I18–I19; mandatory point M25, including misleading singular/plural and version laundering.
- Problem: The manuscript says the report already prints the correct projection symbol p-hat “at one place” where the journal erratum replaces f-hat. Original-detail inspection of report p. 4 shows p-hat in the two corresponding occurrences, exactly as the source note states; the erratum likewise corrects two journal occurrences.
- Harm: This is a false count in the paragraph whose purpose is exact version comparison. It makes the reader disagree with its own frozen source record.
- Minimum repair: Change “at one place” to “at both places” or “at the two places,” while keeping ownership of the journal correction with the 1962 errata.

## Independent mathematical rederivation

### M04–M07: acceptors, regular operations, and finite-set encodings

The §2 acceptor is exactly A = (S,f,d,D), with finite nonempty input alphabet I, finite nonempty internal-state set S, f : I x S -> S, d in S, and D a subset of S (journal pp. 21–22; manuscript lines 238–256). Extending f to words gives delta(d,Lambda) = d and, for u = i_0...i_(n-1), states s_0 = d and s_(k+1) = f(i_k,s_k). Thus u is accepted exactly when s_n is in D, and Lambda is accepted exactly when d is in D. The reader's indexing is equivalent to Elgot's and keeps alphabet, states, transition, run, and accepted language distinct.

The regular-language arguments of §§3–4 check out. Coordinate projection is a homomorphic image. Right truncation removes the maximal terminal block of a chosen letter; Lemma 4.1's identities distribute it through union, concatenation, and star, so Lemma 4.2 gives an effective regular expression. On journal p. 23 both printed f-hats must be p-hats, and on p. 24 the pair in the second display must be (b,a) so that the word described begins with b. These corrections are owned by errata p. 558.

In L_1^1, individual variables range over N and monadic variables over finite subsets of N (journal pp. 25–26; manuscript lines 258–286). A formula, an assignment, its characteristic-column function, and the associated language are different objects. For r >= 0, standard empty-product conventions give U_r = {0,1}^r, U_0 = {()}, 0_r the all-zero tuple, and U_0^0 empty. A nonempty union of assigned finite sets is cut immediately after its last nonzero column; the all-empty assignment is Lambda. The admissible words are U_r* U_r^0 union {Lambda}. In particular, for r = 0 the unique assignment is Lambda, so T_0(A) is {Lambda} exactly when the closed sentence A is true and is empty otherwise. No canonical encoding has a terminal zero column.

### M08: Theorem 5.3(a), formula to regular language

The proof on journal pp. 27–30 is sound.

1. Lemma 5.4 prenexes and moves every finite-set quantifier to the left of every individual quantifier. Its commuting identities introduce a fresh finite set of witnesses or counter-witnesses. A singleton witness set proves one direction, and selecting a member of a nonempty finite witness set proves the converse, so the finite-set interpretation is essential.
2. Lemma 5.5 turns the remaining individual-quantified matrix into disjunctive normal form built from principal successor patterns and their negations. Equalities and order are already definable, and iterated successor tests reduce to consecutive-column tests after fresh variables are introduced.
3. The admissible universe is regular. Boolean connectives become union, intersection, and complement relative to that universe.
4. Existentially quantifying F_r deletes the r-th Boolean coordinate and then removes the newly exposed terminal string of 0_(r-1) columns. Projection alone is wrong, because different canonical r-coordinate words can expose different terminal-zero lengths after deletion. For r = 1 every nonempty projected word is a string over the sole U_0 letter and truncates to Lambda, yielding {Lambda} exactly when some finite F_1 is a witness.
5. The local principal expressions have three required cases. If b is nonzero, c_F(x)=a and c_F(x')=b is an internal a,b factor. If b is zero and a is nonzero, the occurrence can be an internal a,0 factor or a at the represented terminal column. If a and b are both zero, every finite assignment satisfies the existential pattern by taking x beyond its finite support. Each language is regular.

This proves closure under the actual constructors rather than importing a modern automata/MSO correspondence.

### M09: Theorem 5.3(b), regular language to formula

Let alpha be a regular admissible U_r-language and choose an acceptor for alpha minus {Lambda}. Inject its finite nonempty state set into U_s^0 for some s > 0. A completed nonempty word records after each input column x_i the state y_i reached after that column. The exact conditions are:

- first letter in B = {(x,f(x,d)) : x in U_r};
- last letter in E = U_r^0 x D, enforcing acceptance and canonical nonzero termination;
- adjacent letters satisfy ((x_1,y_1),(x_2,y_2)) in R iff f(x_2,y_1) = y_2.

Finite start and terminal sets are definable by column tests; adjacency is an x,x' principal condition. Elgot's zero-tail extension of the local relation makes the universal local formula remain true beyond the represented end. Conjunction and existential removal of the s state coordinates project exactly to alpha minus {Lambda}. A length-one word needs start and terminal constraints but no adjacency instance. Add a closed Lambda case iff Lambda belongs to alpha. This covers the empty language and {Lambda} as well.

### M10: decision and arithmetic consequences

For a closed L_1^1 sentence the r = 0 analysis reduces truth to whether the effectively computed language is {Lambda} or empty. This is Corollary 5.8, not a blanket arithmetic decision theorem.

The map tau(F) = sum of 2^k for k in F is a bijection from finite subsets of N to N. A finite carry set C, with no incoming carry at position zero, makes the output bit the parity of the two input bits and incoming carry, while the next carry occurs exactly when at least two of those three bits occur. The relation is monadically definable, giving addition, Presburger decidability, and effective translation. Singleton finite sets correspond to powers of two, yielding the strict power-of-two expansion. The integer and quasi-finite developments alter the canonical representative and truncation operation but retain finite regular encodings. Manuscript lines 331–343 keep those exact strengths.

### M11–M13: transducers, Lemma 6.1, and Theorem 7.1

The later A/B-automaton is (S,f,d,g), with f : A x S -> S, d in S, and total g : S -> B (journal pp. 41–42; manuscript lines 345–372). On input a_0...a_n it first computes s_0 = f(a_0,d), then s_i = f(a_i,s_(i-1)), and outputs b_i = g(s_i). Its behavior is synchronous and always contains the empty paired word. It is a deterministic Moore-style transducer, not the §2 acceptor and not a Büchi automaton.

For Lemma 6.1, take an acceptor for regular gamma. A complete state records the last paired input/output letter and current acceptor state. First keep complete states whose acceptor component is final, because every prefix of a strongly extendable word must be in gamma. Define a descending sequence M_i by keeping q in M_i at stage i+1 exactly when, for every a in A, some b in B and some q' in M_i give a transition q --(a,b)--> q'. The induced relations descend with M_i. Finiteness gives stabilization after at most the number of complete states proper deletions. The stable graph, restricted to viable start states, recognizes a regular language; if no start is viable the result is empty, and otherwise Lambda is included as required by prefix closure. Every survivor has every input continuation, so the language is strongly A-extendable. If beta is any strongly A-extendable sublanguage of gamma, induction on i shows all complete states used by beta survive M_i. Thus beta is contained in the stable language, proving maximality. The construction is effective.

For Theorem 7.1, necessity follows from the unique causal run: completed runs form a regular language; every run prefix is a run; one input has at most one output; and every input has an output. For sufficiency, inject B into a Boolean cube. For each output bit, project alpha to A x {0,1} and recognize the inputs whose last output bit is 0 or 1. Functionality makes the two languages disjoint; totality makes their union all inputs. Take the product of their acceptors. On every reachable product state, the final-state vector is the unique prescribed output letter. Restrict to reachable states, or define arbitrary B-values off the reachable part, to obtain a total output map. Prefix closure and functionality prove inductively that the constructed output equals alpha's unique output on every input. The construction is effective.

### M14: Theorem 7.3 and the non-Büchi boundary

Suppose alpha is a set of infinite paired sequences with regular finite-prefix language alpha^L, prefix functionality, and input totality. Alpha^L is prefix closed. Its functionality follows from infinite prefix functionality. Any finite input extends to an infinite input, whose required output supplies finite input totality. Theorem 7.1 therefore constructs a transducer with J(T) = alpha^L.

The essential equality is lim(alpha^L) = alpha. One inclusion is immediate. Conversely, let (f,g) be in lim(alpha^L). Input totality gives h with (f,h) in alpha. For every n, membership of (f,g) restricted to n in alpha^L supplies a member (f_n,g_n) of alpha having that prefix. Prefix functionality applied to (f_n,g_n) and (f,h) gives g restricted to n = h restricted to n. Hence g = h and (f,g) is in alpha. An actual transducer has the three properties, and every finite behavior extends along any infinite continuation of its input. No recurrent accepting set or omega-acceptance condition is involved.

### M15–M16: Theorem 8.1, Corollary 8.2, and §8.3

If J(T) is contained in gamma, then J(T) is strongly A-extendable: run prefixes remain behaviors and every next input has its determined output continuation. Lemma 6.1 gives J(T) contained in gamma_A, so gamma_A is nonempty.

Conversely, if gamma_A is nonempty, it contains Lambda and is total under every next input. Fix an order on B and retain, for each finite input, the lexicographically least compatible output in gamma_A. Lemma 6.5 preserves regularity. The selection is functional and input-total. It is prefix closed: if a selected extension had a nonselected prefix, a smaller compatible prefix could be strongly extended along the remaining input, producing a smaller full compatible output, contradiction. Theorem 7.1 constructs the required transducer.

If gamma_A is empty, there are no realizing transducers and Corollary 8.2's universal equality is vacuous. Otherwise compare the least selection for an order with the least selection for the reverse order, which is the greatest selection for the first order. If they differ, they give two behaviors. If they agree, every compatible output lies between the least and greatest and therefore equals them. Empty symmetric difference is thus the exact uniqueness-of-behavior criterion.

Section 8.3's formula has different standing from the transducer. Existential state coordinates enforce the state reached after the first input and each successor transition; output coordinates enforce b(x) = g(s(x)); terminal-zero clauses delimit the finite word. The satisfying encodings equal J(T). Given a separate specification formula G[a,b], behavior containment is the truth of the universally closed implication F_T[a,b] -> G[a,b]. Formula and machine are not identified.

### M17–M19: arbitrary sets, direct errata check, and repaired reduction

In L_1^5, individual variables still range over N but monadic variables range over arbitrary, not finite, subsets of N. The exact restricted syntax is stated in MP-01. The source note is correct; the reader is not complete at this point.

I directly checked all six Elgot errata items on printed pp. 558–559:

1. journal p. 23 lines 10–11: both f-hats become p-hats;
2. journal p. 23 §3.6(b): “by a finite number ...” begins a new line;
3. journal p. 24 second display: (a,b) becomes (b,a);
4. journal p. 46 §8.6.2: n is one more than the maximum offset;
5. the phrase becomes “some R which is n-ary”;
6. the false third sentence is replaced by the finite-union and tagged-projection repair.

The erratum's k = 2 example genuinely refutes the printed k = 1 claim. One disjunct yields sequences over {(1,0),(1,1)} beginning with (1,0); the other yields sequences over {(0,1),(1,1)} beginning with (0,1). The shared column (1,1) permits spurious switching if the untagged relations are merely unioned. Disjoint component tags are necessary. For arity at least two, componentwise tagged fields, tagged prefix sets, relation union, and projection give exactly the finite union. MP-02 records the missing general-arity statement and unary case.

After that repair, let delta be the unprojected tagged local-sequence set and beta its projection after existential removal of state/set coordinates. Section 8.5 effectively constructs the regular finite-prefix language beta^L and, by its finite-branching compactness argument, lim(beta^L) = beta. Therefore

lim J(T) is contained in beta iff J(T) is contained in beta^L.

The right side is exactly the finite-behavior synthesis problem decided by Theorem 8.1. Thus §8.6.3 is sound after, but only after, the full arity-safe finite-union repair.

### M20: Chapter IV's exact undecidability boundary

Lemma 10.1 encodes a Post-normal-system proof as a finite sequence of words separated by a finite monadic marker predicate. The formula verifies the initial axiom and that each successive pair of blocks is related by one of the finitely many productions. Its encoded language is exactly the proof set.

For a two-letter Post system generating a complete recursively enumerable set, F_n is satisfiable exactly for generated n. Satisfiable L_2^1 formulas are recursively enumerable using the Presburger part, but the reduction makes the set undecidable and of maximal recursively enumerable degree (Theorem 10.2, journal p. 49). Section 10.3 transfers undecidability to unrestricted predicates; §10.4 transfers the Post encoding to integers with finite predicates; §10.5 treats ultimately periodic predicates, retaining recursive enumerability, undecidability, and maximal r.e. degree, with an analogous integer result.

Corollary 10.6 does not contradict the positive results. A fixed input-free automaton has an ultimately periodic output, so satisfaction of the specified L_2^4 formula on that fixed output is decidable. Quantifying over the existence of some input-free automaton is different and is undecidable. Manuscript lines 440–453 preserve this fixed-object/existence boundary.

## Assigned mandatory-point disposition

| Point | Disposition | Basis |
|---|---|---|
| M04 | checked-clean | Exact acceptor types, recursion, final-state convention, and Lambda case derived. |
| M05 | checked-clean | §§3–4 closures and p. 23/p. 24 corrections checked visually and mathematically. |
| M06 | checked-clean | L_1^1 syntax, finite-set interpretation, and object standings verified. |
| M07 | checked-clean | U_r, U_r^0, 0_r, T_r, admissibility, canonical cut, all-empty and r = 0 cases derived. |
| M08 | checked-clean | Both normalization lemmas, Boolean/local bases, projection, and truncation independently derived. |
| M09 | checked-clean | State completion, boundary sets, adjacency, existential projection, length-one and Lambda cases checked. |
| M10 | checked-clean | Corollary 5.8, finite carry, Presburger/power-of-two, integer, and quasi-finite strengths checked. |
| M11 | checked-clean | A/B tuple and synchronous behavior distinguished from the acceptor and Büchi acceptance. |
| M12 | checked-clean | Deletion, stabilization, regularity, effectiveness, strong extendability, and maximality proved. |
| M13 | checked-clean | Every necessity/sufficiency clause and effective converse verified. |
| M14 | checked-clean | lim(alpha^L) = alpha proved and non-Büchi boundary preserved. |
| M15 | checked-clean | Theorem 8.1, lexicographic prefix proof, both Corollary 8.2 cases, and uniqueness checked. |
| M16 | checked-clean | Fixed-machine formula and containment truth reduction checked without conflation. |
| M17 | finding-linked: MP-01 | Reader hides the exact forbidden/allowed syntax and offset definition. |
| M18 | finding-linked: MP-02 | All six corrections and k = 2 checked; tagging paragraph lacks arity/unary completeness. |
| M19 | finding-linked: MP-01, MP-02 | Reduction is sound only after exact syntax and an arity-safe tagging construction. |
| M20 | checked-clean | Lemma 10.1 through Corollary 10.6 verified at exact strength. |
| M25 | finding-linked: MP-01, MP-02, MP-03 | Hidden hypothesis, edge-case gap, terminology defect, and misleading singular/plural found. |

The supplied AGENTS terminology rule was enforced. Apart from MP-01's undefined “local” shorthand, proof-relevant distinctions have exact standing and later use: acceptor versus transducer, assignment versus encoding language, extendable versus strongly extendable, and formula versus machine are defined and nonredundant. Topic-only scope, research-copy rights qualification, and the no-test/no-build boundary were respected; this review does not establish another presentation, a rendered handbook, human review, Part IX completion, or user acceptance.

VERDICT: REJECT — MP-01, MP-02, MP-03

# Edition 2026 C6.2: bounded input and serialized-table formulas

Date: 7 September 2026. Authoring block for the exact bespoke numbering in the active manuscript. This note records supplied formulas, author read-back and the next proof interfaces. Independent acceptance has not been claimed. No tests, builds, manuscript renders, source acquisitions or delegation were performed.

## Saved result and ownership

The only manuscript edit is in [inherited-08710-08876.tex](../../handbook/restoration/inherited-08710-08876.tex), after the existing history definition. The new formula definition and three complete supplied lemma proofs occupy lines 157–528. The existing computation theorem remains explicitly a **proof sketch**, and its proof plan at lines 570–578 now identifies H3, H4 and full Comp assembly as the remaining substantive work.

The active interfaces are:

| Label | Current lines | Supplied content |
| --- | --- | --- |
| `def:p04-input-table-formulas` | 157–318 | All bounded comparison, bit, input, description, bitmap, five-field row and complete-table formulas; explicit H1(x,s) and H2(e,s) |
| `lem:p04-input-formula` | 320–374 | H1 is bounded and equivalent in the standard natural-number structure to exact canonical-input clause h1 |
| `lem:p04-table-formula` | 376–495 | H2 is bounded and equivalent to exact serialized-program certificate clause h2; invalid indices have no such certificate |
| `lem:p04-input-table-packing` | 497–528 | Joint input/table certificates and every compatible finite extension can be packed in one beta code |
| `thm:bounded-verification` | 530–579, including its proof plan | Existing statement retained; status remains proof sketch |

The four ordinary theorem openings are still, in order: bounded verification, c.e./Sigma-1 characterization, hierarchy classifications, hierarchy strictness. Their current opening lines are 530, 587, 619 and 640. The driver’s third/fourth theorem ordinal interface is preserved: the insertion adds only a definition and lemmas.

## Frozen identities and retained root material

| Artifact | SHA-256 |
| --- | --- |
| History file before this block | `F133F82DF48E6E4556FF07B637452151362770CA0DB4396B3772BD4468EF49C1` |
| History file after author read-back | `076FFD24CBF5824234818704CABCEFF918D607EF61C36DC34314C3F47D3CABF5` |
| Unchanged serialization file | `DE01687B7F524F49D6B3E90C9ACD038550F7BE1551A1AABC771B8BBB3B4B0177` |
| Protected history prefix, original/current lines 1–156 | `7013B87D4AD110ABCC7A9ACDABE58AA5455FFB28D06E613E51BF306AAC40F551` |

The protected-prefix hash is SHA-256 of the UTF-8 encoding of the exact text before the first new definition. Before insertion it ended immediately before the original bounded-verification theorem; afterward it ends immediately before `Bounded input and table formulas`. Both computations gave the same hash. Thus the entire root-authored E/E2 definition, extraction/packing lemma and fourteen-tag history definition were retained exactly. No overlap correction was needed.

The first saved checkpoint was hash `2C323D2267116BF84A66EB7E69B18B47E0141F0058C26B87B11722F6A1F8C377`. Final read-back added only two interface clarifications: R5 alone does not assert table membership or field ranges, and a finite packing extension must agree with the certificates at overlapping tagged positions.

## Primary local evidence and actual reading scope

The precise source of this numbering is the book’s own serialization definition. The new formulas are explicitly attributed in their definition as the handbook’s construction for that numbering. No external book’s code numbers, transition format or T-predicate were substituted. The earlier preparation note’s missing-serialization observation was resolved by the root stage before this block and is not a current blocker.

| Actual local source | Read scope in this block and relevant locators | SHA-256 |
| --- | --- | --- |
| [inherited-07506-07677.tex](../../handbook/restoration/inherited-07506-07677.tex) | 1–145: total nonhalting transition function at 20–25; exact step and initial tape at 33–79; canonical binary word at 81–84; right-nested tuple coding at 91–105; first-blank output convention at 111–123 | `EB27FE6DE9A8FFBBE3EC6F317DFF66D97DDE72F22B1FA3FCB48A4304D85F3C7D` |
| [inherited-07851-08048.tex](../../handbook/restoration/inherited-07851-08048.tex) | Full 1–261: serialization at 22–63, exact decoding at 65–80, invalid-index/raw-output behavior at 82–109, bespoke-source boundary at 212–216 | `DE01687B7F524F49D6B3E90C9ACD038550F7BE1551A1AABC771B8BBB3B4B0177` |
| [inherited-08306-08438.tex](../../handbook/restoration/inherited-08306-08438.tex) | 1–70: actual language, numeral convention and marked bounded quantifiers, including the left-oriented witness for Le | `0B020970BE72999CD771566BA0D6CDB4E4668728362CBD3C0D1606059EE9D2B8` |
| [inherited-08439-08709.tex](../../handbook/restoration/inherited-08439-08709.tex) | 1–160: P graph and component bounds at 1–25; B formula, unique extracted value bound and finite packing at 37–83; later prefix-transfer material was not needed for the new proofs | `95EB4270559303FEFC5DE2D9BC804A04768EAD87D68D9E5D9CBF65079714806A` |
| History file before editing | Full 1–286, including exact E/E2 and fourteen-tag layout at 1–155 and all theorem-status boundaries | Predecessor hash above |
| History file after editing | Full new content read back in numbered, non-truncated ranges, plus unchanged-prefix hash and final clarification read-back; final freeze hash above | Final hash above |

The research skill was read and its primary-source attribution and single-note workflow used. The assignment explicitly prohibited delegation, so its default background-agent instruction was not applied. No external paper or book body was newly read. The manuscript’s existing Gödel, Shoenfield, Kleene and Boolos–Burgess–Jeffrey references remain their existing parallel/source dependencies, not sources claimed for these newly supplied literal formulas. The beta-packing lemma’s Chinese remainder theorem dependency is unchanged.

## What the actual formulas check

### H1: canonical input and its prefix certificate

Header tag 0, position 5 supplies L. The formula introduces a bounded last-position variable lambda with L = S lambda. Families 5 and 6 supply digits and prefix values. It checks:

- every digit is 0 or 1 and every prefix is at most x;
- first prefix equals first digit;
- each successor prefix is twice the preceding prefix plus the next digit;
- the last prefix is exactly x;
- x = 0 requires exactly one digit, namely 0;
- x > 0 requires first digit 1.

The full formula is displayed at manuscript lines 201–209 with I and J expanded immediately above it. The reverse proof bounds every stored witness by s and bounds lambda by L. The forward proof uses unique E extraction and Euclidean quotient/remainder uniqueness to establish the exact canonical word, including uniqueness of length. The compatibility lemma proves the prefix bounds for the actual binary word by monotonicity of its successive values.

These digits are numerical bits 0/1. The future H3 initial-tape formula must convert them to normalized tape-symbol numbers 1/2, namely S d, at shifted positions H+j. H1 does not silently identify bit 0 with the blank tape symbol 0.

### H2: exact program index and total ordered table

The outer witnesses are k,c,n,b,A,nu,m,lambda, each at most s. Header tags identify the first five. Arithmetic equations assert n = nu+2, nu != 0, b >= 3, m = nu*b, k = 3+m and k = S lambda. Consequently n,b >= 3 and k >= 6; zero-, one- and other short-length descriptions cannot pass.

P(k,c,e), the first stored tail c, the paired tail recurrence for i<lambda and the final equality between last tail and last entry check the exact length-k right-nested code. There is no invented terminal zero. The first three description entries equal n,b,A.

The bitmap check fixes B_0=A and B_b=0, every recurrence B_j=2B_(j+1)+eta_j, all digit ranges, and eta_0=0, eta_1=eta_2=1. The terminal zero proves absence of higher bitmap bits. Powers appear only in the metatheoretic proof of the recurrence’s meaning, never as arithmetic-language terms.

For each block u<nu and symbol a<b, row number u*b+a must have source state 0 if u=0, and u+2 otherwise. Four P equations decode its five fields in exactly the source order (q,a,q',a',direction). The next state is below n, written symbol below b, and direction is 0=L or 1=R. The current state is below n and is neither halting state. Euclidean division by b proves that the double loop covers every row below m exactly once and gives exactly the required lexicographic list. The n=3 case has only the state-0 block and is included.

R5(s,i,q,a,q',a',d) uses description position 3+i. Its code rho is an E-extracted value at most s; its three auxiliary pairing tails and every field are at most rho. R5 alone is merely the five-field lookup graph. Future transition formulas must combine it with H2 and a row bound i<m (or the proved equivalent bounded key enumeration) to use its validity and totality guarantee.

## Boundedness and author checks

The actual formulas contain only 0, S, addition, multiplication, equality, Boolean connectives and marked bounded quantifiers after the named abbreviations are expanded. Lt and Le explicitly bind the comparison witnesses. Every abbreviation expansion renames all bound variables fresh, including the internal E/B variables, before substituting argument terms. The separately bound lambda variables in H1 and H2 are renamed apart on conjunction.

Stored values are bounded by s, but a flattened tag/position index is not assumed to be at most s. E supplies the proved term bound S(t+j)*S(t+j) for that index. Five-field pairing witnesses are bounded by rho. The auxiliary differences n-2, k-3 and k-1 are defined metatheoretically only in the correctness proof; their formula witnesses are related by addition and successor, with bounds supplied by n or k. No exponentiation, division, subtraction, generic T-predicate or added array function occurs in the formula syntax.

The author read-back checked both semantic directions, fresh binding, zero input, one-bit positive input, positive no-leading-zero input, empty universal successor range at L=1, minimal state/symbol counts, arbitrary bitmap padding within width b, rejection of higher bitmap bits, both directions, halting-state row exclusion, all row positions including the terminal description entry, and simultaneous finite packing. This is a supplied-proof author check, not independent review or formal verification in Q/PA. The statements concern truth in the standard natural-number structure.

## Exact continuation point: C6.3–C6.5 remain open

1. Supply H3 for this same fourteen-tag layout: all header relationships, the base-b tape prefix checks, initial q=0 and shifted h=H, initial input symbols S d_j at H+j and blanks elsewhere, every source state/symbol/direction lookup through the certified R5 relation, the written cell and every unchanged cell, and correct shifted left/right head arithmetic. Prove that the finite window H=T, W=L+2T+1 represents the full two-sided run and that no boundary transition is lost. This requires a real bounded formula and both directions.
2. Supply H4: accepting state 1, the first-blank output boundary at H+ell, positive output length, normalized symbols S o_j, canonical output digits and prefixes, final value y, and all associated bounds. Retain the earlier convention that later cells, negative cells and final head position do not affect the output. Rejecting or numerically invalid halts must not satisfy the computation formula.
3. Display the full Comp conjunction and prove its equivalence to the exact history definition. Prove that each genuine finite accepting computation admits one simultaneous packed certificate, and that a satisfying certificate reconstructs the actual decoded run. H1 and H2 alone admit certificates for rejecting/diverging valid programs and cannot establish the existential Comp claim.
4. Reconcile downstream c.e./Sigma-1 and P5 proof/representation interfaces after that proof is supplied. No numeralwise representability theorem, proof-predicate primitive-recursive construction, or D1–D3 internal provability assertion was upgraded in this block. Those are different claims from standard-model bounded checking and remain for their assigned continuation.

The immediate authoring interface is H1(x,s), H2(e,s), E/E2 and R5 with i<m. The exact next missing manuscript argument is the H3 configuration/step formula now identified in the proof plan of `thm:bounded-verification`.

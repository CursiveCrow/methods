# Round 8 adversarial-publication-and-terminology report: Rabin 1969

## Decision and exact scope

I accept the frozen Round 8 reconstruction at manuscript-content level. I found
no blocker, must-fix, should-fix, consider, discard, or unresolved-user finding.
This verdict is deliberately narrow: it concerns only the frozen content for
`N-c-014.d`, including the consistency of that content with the frozen detailed
source note, compact source-presentation record, and relevant bibliography
entries. It does not admit another `N-c-014` presentation, all of `N-c-014`,
Part IX, a rendered handbook page, a build, another part, the book, human
review, user review, final typesetting, or publication.

## Independence, evidence boundary, and method

I conducted a fresh whole-snapshot review under the Round 8 evidence rule. I
read only:

1. `spec/research/boards/p09-rabin-1969/charter.md` in full;
2. the six objects in the charter's Frozen Round 8 table, each in full; and
3. the original-detail Rabin and Meyer render sets identified by the charter.

I did not read any earlier-round report, another Round 8 report, `ledger.md`,
`transcript/chair.md`, another board or board transcript, an unfiled Round 4
object, the staging draft, the layout extraction, a handbook PDF, conversation
history, or memory. I did not contact another reviewer and did not browse the
web. I ran no test, checker, repository script, TeX command, interim build, or
build. The only automated operation used on frozen evidence was native SHA-256
hashing for identity. All source formulae, symbols, source wording, and printed
pagination were checked visually against the original-detail renders rather
than inferred from OCR.

## Frozen identity

All six native SHA-256 computations matched the Frozen Round 8 table exactly.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | exact match |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695` | exact match |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | exact match |
| `spec/research/p09-rabin-1969-source-note.md` | `4C7FA2AFDCED52E1076F5604A826F5AC148707EE0A4AE1772B31F704259F104A` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `9B679F27B410F8FC65F0193AD0E85B4653C32B306002B9C0F19E2EFBACDC8DB2` | exact match |

## Source pages inspected

I individually opened and visually inspected every mandated source page at
original detail.

- **Rabin:** physical PDF pages **1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
  13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
  30, 31, 32, 33, 34, 35, and 36**. Physical p. 1 is the JSTOR/AMS
  custody-and-use cover. Physical pp. 2--36 are, respectively, printed article
  pp. 1--35.
- **Meyer:** physical PDF pages **485, 486, 487, 488, 489, and 490**. These
  are, respectively, printed article pp. 477, 478, 479, 480, 481, and 482.

The Rabin inspection included the title, abstract, introduction, all
definitions and numbered results, all of Chapters I--III, the complete
application chapter, the complete complementation and emptiness development,
and the references. The Meyer inspection included the title/copyright page,
the lower-bound theorem on printed p. 478, its listed theories and
Meyer--Stockmeyer attribution on printed p. 479, the explicit Rabin upper-bound
comparison on printed p. 480, the examples on pp. 480--481, and the references
on pp. 481--482.

The page evidence most material to this mandate was: Rabin printed pp. 1 and 4
for the historical elementary-recursive claim; pp. 3--7 for Definition 1.1,
valued trees, automaton tuples, and ordinary acceptance; pp. 7--10 for the two
logical translations and sentence reduction; pp. 17--19 for sequential
automata and Theorem 3.1; pp. 19--24 for marked trees, well-founded mappings,
and simultaneous runs; pp. 24--32 for dual acceptance, the half-steps, finite
trees, compactness, and complementation; pp. 32--34 for the actual emptiness
argument; and pp. 34--35 for its last base clause and references. Meyer printed
pp. 478--480 controlled the complexity correction.

## Adversarial stress-test result

I tried to falsify the reconstruction along every boundary singled out by the
charter. None yielded a surviving defect.

| Boundary attacked | Result and exact frozen evidence |
|---|---|
| Ordinary versus dual acceptance | The reader gives ordinary `\exists r\,\forall\pi` with `F\subseteq\mathcal P(S)` at `n-c-014.tex:974-1013`, then separately gives type/type-empty and dual `\forall r\,\exists\pi` at `1143-1188`, including no-run vacuity at `1182-1187`. Rabin printed pp. 6 and 24--25 control. The detailed note repeats the distinction at `p09-rabin-1969-source-note.md:203-249,359-416`; the compact record does so at `p09-source-presentations-lot2-3.md:664-668`. |
| Finite versus infinite trees | Infinite valued subtrees and whole-run path acceptance are typed at `n-c-014.tex:965-1014`. Finite predecessor-closed, frontiered witnesses, their restricted valuation, and the external frontier value are separately typed at `1259-1294`. The reader expressly denies that the finite machinery changes the infinite input at `1397-1400`. Rabin printed pp. 5--7 and 30--34 control. |
| Weak versus full monadic logic | Full `S2S` supplies the main sentence translation and decision at `n-c-014.tex:941-963,1027-1098`; weak monadic logic occurs only as the external finite-tree base dependency at `1381-1400`. This agrees with Rabin printed pp. 7--10 and 30--34 and with the detailed note at `523-557,591-620`. |
| Arbitrary root versus full root | `T_x`, arbitrary-root valued trees, and `V_\Sigma` are defined at `n-c-014.tex:965-1014`. The track bijection is expressly full-root at `1027-1046`. The distinction agrees with Rabin printed pp. 5--6 and Definition 1.7 on p. 7 and with the detailed note at `184-241,252-265`. |
| Source proof versus later route | The reader uses Rabin's nonemptiness reduction with no basis insertion at `n-c-014.tex:1093-1098` and reconstructs the one-letter/dual/weak-base emptiness route at `1305-1400`. Thomas's basis route is separately and later attributed at `1432-1437`. The compact record keeps the same boundary at `666,670,674-680`. |
| Source claim versus later correction | Rabin's elementary-recursive claim is reported but explicitly not retained at `n-c-014.tex:952-960,1392-1400`. Meyer supplies the later non-elementary tower lower bound and the two-successors-and-prefix attribution, and the sublanguage consequence is stated without weakening decidability or effectiveness. Rabin printed pp. 1 and 4 and Meyer printed pp. 478--480 control. |
| Decidability/effectivity versus complexity | Theorem 1.1, Theorems 1.5--1.6, and Theorem 1.12 remain effective decision results, while the false worst-case qualification is removed: `n-c-014.tex:952-963,1016-1023,1392-1400`. No complexity class or quantitative upper bound is invented. |
| Proof versus outline | The reader supplies exact definitions, reductions, repairs, and the proof architecture, then discloses that it does not reproduce every transition table or every induction in the fourteen-page development: `n-c-014.tex:1423-1430`. External McNaughton and weak-theory dependencies are labelled external at `1114-1139,1381-1384,1397-1400`. |
| Source text versus handbook repair | The zero-pair normalization is marked handbook-owned at `n-c-014.tex:1190-1213`; the empty-`H` branch is marked handbook-owned at `1361-1371`; the `m=0`/empty-`U_0` branch is marked handbook-owned at `1373-1389`. The printed nonempty clauses remain accurately reported rather than silently rewritten. Rabin printed pp. 25--26 and 34 control. |
| Rights/access versus republication | The detailed note distinguishes public/research access from an open-content or republication licence at `p09-rabin-1969-source-note.md:48-102`. Rabin physical p. 1 supplies the custody/use restriction; Meyer printed p. 477 and the proceedings object supply the later-source boundary. No frozen record licenses redistribution of PDFs or renders. |
| Reconstruction status versus admission/completion | The detailed note says a fresh Round 8 is required and disclaims terminal admission at `p09-rabin-1969-source-note.md:18-46,622-665`; the compact record says `N-c-014.d` is not admitted and Round 8 remains required at `p09-source-presentations-lot2-3.md:660-672`, then calls the review pending at `913`. No record promotes this topic to Part, rendered, build, human, user, or book completion. |

## Mandatory invariant audit, R01--R29

Every mandatory invariant passed. “Reader” below means the frozen
`handbook/parts/p09/presentations/n-c-014.tex`; “note” means the frozen detailed
Rabin source note; “compact” means the frozen lots 2--3 source-presentation
record.

| Invariant | Result | Precise manuscript/record locator and controlling printed source |
|---|---|---|
| **R01** | Pass | The reader retains `\Lambda` and expressly rejects a silent `\epsilon` substitution at `914-917`; `\Lambda` is then used in the predecessor definition at `932-939`. Note `146-182` states the same boundary. Rabin printed pp. 3--5 control. |
| **R02** | Pass | Reader `918-963` defines both editorially disambiguated orders, `r_a`, `T_n=n^*`, `\mathfrak N_n`, and `SnS` for every `0<n\le\omega`; it states the finite-`n` definability and `T_\omega` exception. Note `144-177` and compact `662-664` agree. Rabin printed pp. 3--5 control. |
| **R03** | Pass | Reader `965-1014` defines arbitrary-root `T_x`, paths, valued trees, the distinct table and automaton tuples, finite state set, possibly partial move table, run, `\operatorname{In}`, and ordinary `\exists r\,\forall\pi` acceptance with `F\subseteq\mathcal P(S)`. Note `184-249` and compact `664` agree. Rabin printed pp. 5--7 control. |
| **R04** | Pass | Reader `1143-1188` assigns `\Omega` only to dual acceptance, gives the exact `\forall r\,\exists\pi` condition, and states no-run vacuity and nonidentity with ordinary `F`. Note `359-416` and compact `664,668` agree. Rabin printed pp. 24--26 control. |
| **R05** | Pass | Reader `1016-1023` states Theorems 1.3--1.6 at the exact needed strengths. Theorem 1.4 is described directly as projection away from one coordinate and converse addition of an unconstrained coordinate; no invented operation name appears. Note `243-250` agrees. Rabin printed pp. 6--7 control. |
| **R06** | Pass | Reader `1027-1065` types `\chi_A`, `\Sigma_n`, `v_{\bar A}`, and `\tau`, states the full-root bijection, then separates principal-formula normalization, the finite-tree lift, Boolean closure, projection, and complement. Note `252-300` agrees. Rabin printed pp. 7--10 and 30--31 control. |
| **R07** | Pass | The concrete formula and its two-bit reading occur at reader `1067-1077`; the prose expressly identifies it as handbook-worked and not a Rabin-printed transition table. Note `302-327` says the same. Rabin's principal-formula method on printed pp. 8--9 and Corollary 3.13 on printed p. 31 control the fidelity boundary. |
| **R08** | Pass | Reader `1079-1098` gives Lemma 1.2's single-start normalization, finite run tracks, the move/path clauses, exact `\exists\bar B\,\forall C` set prefix, and the closed-sentence-to-nonemptiness reduction with no basis step. Note `289-300` agrees. Rabin printed pp. 9--10 control. |
| **R09** | Pass | Reader `1102-1139` types the path word, deterministic Muller tuple `\langle U,K,u_0,H\rangle`, `K:U\times S\to U`, product `U\times S`, start set, transition, projection `p_1`, and designated family. The one-position shift inherent in starting the first coordinate at `u_0` cannot affect an infinitely-recurring-state condition; no finite-position property is claimed. Note `329-357` and compact `668` agree. Rabin printed pp. 17--19 control. |
| **R10** | Pass | Reader `1143-1188` reproduces both type clauses: meeting some `U_i` while avoiding its `L_i`, and the additional whole-range avoidance of some `L_j` for type-empty. It then supplies the dual/complement role. Note `359-416` agrees. Rabin printed pp. 24--26 control. |
| **R11** | Pass | Reader `1215-1257` separately retains marked obligations, simultaneous copies, same-state merging, and Theorem 3.1's all-path check before the half-step induction. Note `418-446` and compact `668` agree. Rabin printed pp. 19--24 and 26--32 control. |
| **R12** | Pass | The reader's single local architecture at `1215-1247` gives the need (deferred marked obligations cannot continue endlessly), the standing as a mapping `h\mapsto H_h\subseteq H` on nonempty `H`, the exact no-infinite-chain condition at `1227-1230`, the lower-ordinal-stratum equivalence, and the Lemma 3.4/3.11 uses. It is separated from ordinary run/path acceptance at `1167-1188` and from same-state copy merging in the immediately preceding item `1219-1225`. Note `420-452` and compact `668` make the same nonredundancy explicit. Rabin printed pp. 19--24 and 27--30 control. |
| **R13** | Pass | Reader `1235-1256` preserves the same-length Lemma 3.7/3.8 transformations, the shorter `\Omega_{k-1}` half-step, arbitrary versus last-lower-empty cases, and positive-length induction after the explicit zero case. Note `436-452` agrees. Rabin printed pp. 25--32 control. |
| **R14** | Pass | Reader `1259-1287` gives finite predecessor closure, `\operatorname{Ft}(E)`, the both-children condition, the exact local definition and standing of `frontiered`, its nonredundancy with predecessor closure and later use, valuation off the frontier, exact transition codomain, and `f\notin S` as an external frontier value rather than a state. Note `302-324,523-550` and compact `670` agree. Rabin printed p. 30 controls. |
| **R15** | Pass | Reader `1284-1294` assigns the finite-tree lift to Lemma 3.12, the principal-formula application to Corollary 3.13, finite-obligation compactness to Lemma 3.14, and the resulting ordinary automaton to Corollary 3.15; `1397-1400` denies any weak/full or finite/infinite collapse. Note `551-557` and compact `670` agree. Rabin printed pp. 30--32 control. |
| **R16** | Pass | Reader `1305-1333` erases the alphabet to one letter, complements the one-tree language, uses Lemma 3.6 to obtain the dual question, and reduces emptiness to membership of the unique full tree. It expressly denies a basis theorem at `1307` and earlier at `1096-1098`. Note `454-489` agrees. Rabin printed pp. 32--34 control. |
| **R17** | Pass | Reader `1335-1351` binds the current table, current state set, current pair sequence, and current root state before recursion, notes that state sets may change, and defines `N_{R'}` while retaining formal state set `R`. It expressly permits the root outside `R'` because only nodes strictly below it are restricted. Note `468-478` agrees. Rabin printed p. 33 controls. |
| **R18** | Pass | Reader `1353-1371` gives finite disjoint strata and termination, ranges over every `H\subseteq U_k`, treats `H=\varnothing` as the direct shorter question, treats nonempty `H` via the restricted table and length `k-1`, and labels the empty branch handbook-owned. Note `468-478,491-512` includes a concrete falsification of the printed nonempty-only equivalence. Compact `670` agrees. Rabin printed pp. 33--34 control. |
| **R19** | Pass | Reader `1373-1389` permits `m\ge0`, empty `U_0`, and `E_0,\ldots,E_m`; it spells out the universal finite-run condition and the `m=0` no-run obstruction, invokes König exactly for finite/infinite equivalence, labels the repair, and keeps Doner/Thatcher--Wright external. Note `479-489,502-512` gives the same case and a concrete need witness. Rabin printed p. 34 controls. |
| **R20** | Pass | Reader `952-960,1392-1400` reports Rabin's historical claim but does not retain it. It states Meyer's tower lower bound, exact Meyer--Stockmeyer credit, the sublanguage argument, and survival of decidability/effectiveness. Note `71-109,155-177,514-521,613-617` and compact `662` agree. Rabin printed pp. 1 and 4; Meyer printed pp. 478--480 control. |
| **R21** | Pass | Reader `1404-1421` accounts separately for the countable-linear-order, unary-function, Cantor/`F_\sigma`, Boolean-algebra/ideal, and game applications at their class-level strengths. Note `559-589` agrees. Rabin printed pp. 10--17 control. |
| **R22** | Pass | Reader `1423-1437` states what is reconstructed, what remains in Rabin's fourteen-page development, McNaughton's external role, and Thomas's distinct later basis route. Note `329-357,418-452,514-521,622-651` and compact `668,672,674-680` agree. Rabin printed pp. 17--34 control Rabin's route; no later theorem is attributed to those pages. |
| **R23** | Pass | Numbering and roles are stable throughout: reader `941-963,1016-1023,1038-1065,1079-1098,1102-1139,1143-1188,1218-1256,1284-1303,1305-1400`. In particular, Lemma 3.12/Corollary 3.13/Lemma 3.14/Corollary 3.15 are not interchanged. The printed pages listed in the preceding rows confirm each locator. |
| **R24** | Pass | Reader, note, compact record, and bibliography agree on Rabin and Meyer identity and roles. Relevant bibliography entries are `handbook.bib:2290-2299` (McNaughton), `2346-2355` (Thomas), `5938-5947` (Meyer), `5973-5982` (Rabin, including the inspected scan URL and DOI), and `5993-6002` (Thatcher--Wright, pp. 57--81 and DOI). Pending Round 8 status agrees at note `18-46,622-665` and compact `672,913`. |
| **R25** | Pass | Note `48-102` states that neither public access nor local custody establishes an open-content or republication licence and that PDFs/renders are research objects, not handbook assets. This matches Rabin physical p. 1 and the inspected Meyer proceedings pages. No contrary licence claim occurs in reader, compact record, or bibliography. |
| **R26** | Pass | The complete five-part terminology audit appears in the next section. Every actual technical name is either a source-defined object replayed with exact standing and use, an eliminable editorial notation whose necessity/nonredundancy is stated, or an expressly external established result. No hypothetical named answer appears. |
| **R27** | Pass | The stress-test table above records the surviving separations. Particularly explicit anti-conflation sentences occur at reader `1007-1013,1182-1188,1211-1213,1281-1287,1296-1303,1305-1307,1392-1400,1423-1437`; note `591-620`; and compact `664-672`. |
| **R28** | Pass | Note `45-46,662-665` disclaims terminal admission; compact `672` says `N-c-014.d` is not admitted and `913-915` distinguishes body sufficiency from review/build/human completion. The reader makes a reconstruction/proof-boundary statement, not an admission statement, at `1423-1437`. This report's opening scope repeats the exact limitation. |
| **R29** | Pass | Reader `1190-1213` derives the empty sequence's no-run semantics, defines `\Omega^\dagger=((S,S))`, proves its path language empty over the finite nonempty state set available with named root state `s`, proves dual equality, and labels it an exact handbook-owned normalization rather than new semantics. It is actually used at `1249-1256,1340-1342`. Note `393-416,442-446,459-467` and compact `668` agree. Rabin printed pp. 25--26 and 31 show the source construction and positive-length induction boundary. |

## Five-part technical-name audit

I treated a “technical name” broadly: formal symbols newly introduced by the
reader, source terms replayed as terms of art, and editorial/metalinguistic
abbreviations all received review. Ordinary bound variables (`A`, `B`, `C`,
`D`, `E_i`, `F`, `H`, `L_i`, `R`, `S`, `U_i`, and so on), theorem numbers,
and bibliographic titles are not independent named concepts; their types are
nevertheless checked where bound. The five columns below are: **necessity**,
**definition**, **standing**, **nonredundancy**, and **later use**.

| Name or coherent name family | Five-part disposition at first local introduction |
|---|---|
| `\preccurlyeq_{\mathrm{is}}`, `\preccurlyeq_{\mathrm{lex}}` | **Necessity/nonredundancy:** reader `918-927` says the subscripts are required to distinguish Rabin's two printed order symbols and are not extra relations. **Definition/standing:** the initial-segment relation is given by an iff; lexicographic order is the order induced from the alphabet order. **Use:** both enter `\mathfrak N_n` at `941-951` and the formula normalization at `1048-1065`. Rabin printed pp. 3--5 control. |
| `r_a` and editorial `\operatorname{pd}` | **Necessity:** they expose successor and predecessor behavior without overloading the two orders. **Definition/standing:** typed maps and all cases are at reader `927-940`. **Nonredundancy:** `r_a` appends while `pd` fixes the root/removes the last symbol. **Use:** `r_i` enters `\mathfrak N_n`; `pd` types arbitrary-root paths at `969-971`. Rabin printed pp. 3--6 control. |
| `T_n`, `\mathfrak N_n`, and `SnS` | **Necessity:** they distinguish the word-tree domain, its full displayed structure, and the theory of that structure. **Definition/standing:** reader `941-952` defines all three and the domain/range of `n`. **Nonredundancy:** the finite/omega order-elimination distinction is stated locally. **Use:** Theorems 1.1/1.12 and later `S2S` translations use them at `952-963,1040-1046`. Rabin printed pp. 5 and 10--11 control. |
| `T`, `T_x`, path, full-root, and `V_\Sigma` | **Necessity:** these distinguish the binary ambient tree, one arbitrary rooted subtree, a branch, the root-`\Lambda` special case, and the universe relative to which complements are taken. **Definition/standing:** reader `965-973` gives exact set/path/map clauses. **Nonredundancy:** arbitrary-root versus full-root is expressly stated at `1011-1014,1027-1039`. **Use:** `T_x` types every run/dual language; full-root types `\tau`; `V_{\{\bullet\}}` is required in the double-complement identity at `1328-1331`. Rabin printed pp. 5--7, 18, and 33 control. |
| transition table, ordinary automaton, state set, move table, run, `\operatorname{In}`, and `T(\mathfrak A)` | **Necessity/nonredundancy:** reader `974-1013` explicitly separates table data from automaton data and ordinary `F` from the later pair sequence. **Definition/standing:** all tuples, maps, run constraints, and acceptance quantifiers are exact. **Use:** Theorems 1.3--1.7, Theorem 3.1, dualization, and emptiness all use the vocabulary. Rabin printed pp. 5--7 control. |
| `\chi_A`, `\Sigma_n`, `v_{\bar A}`, and `\tau(\bar A)` | **Necessity:** these distinguish individual membership tracks, their product alphabet, the node label, and the complete encoded tree. **Definition/standing:** typed at reader `1027-1037`; the bijection at `1038-1039` fixes their role. **Nonredundancy:** the components have different domains/codomains and are not called formulas or automata. **Use:** Theorem 1.7's equivalence at `1040-1046`. Rabin printed p. 7 controls. |
| principal formula | **Necessity:** it identifies the exact normal-form base whose automaton construction is deferred. **Definition/standing:** its quantified syntactic form and suffix/membership parameters are at reader `1048-1059`. **Nonredundancy:** the reader distinguishes it from its Boolean combinations and from the later finite-tree lift. **Use:** Corollary 3.13 closes it at `1060-1065,1284-1287`. Rabin printed pp. 8--9 and 31 control. |
| `P(A,B)` | **Necessity:** one named formula is needed to work the general track construction concretely. **Definition/standing:** it is exactly a two-free-set formula at reader `1067-1070`. **Nonredundancy:** `1071-1077` distinguishes the formula, its track condition, its finite witness, and a transition table, and marks the example handbook-owned. **Use:** the immediately following calculation and lift use it. |
| `(r\mathbin{\upharpoonright}\pi)_\omega` | **Necessity:** a path restriction is a node-indexed map until it is explicitly enumerated as the `S^\omega` word consumed by the sequential automaton. **Definition/standing:** reader `1102-1104`. **Nonredundancy:** the codomain `S^\omega` separates it from the tree run. **Use:** Theorem 3.1's premise and product proof at `1105-1138`. Rabin printed p. 18 controls. |
| deterministic Muller word automaton and `p_1` | **Necessity:** determinism is required for one coherent first-coordinate history across common branch prefixes, and `p_1` is required to pull the recurring product states back to the Muller family. **Definition/standing:** reader `1114-1135` types the tuple, transition, family, and projection. **Nonredundancy:** `1136-1138` states the deterministic role; the two product coordinates have separately typed jobs. **Use:** the designated family and later Theorem 3.1 path checks. Rabin printed pp. 17--19 control; McNaughton is expressly external. |
| `\Omega`, type `\Omega`, type `\Omega`-empty, `[\Omega]`, `[\Omega,e]`, and `D(\mathfrak A_0,\Omega,s)` | **Necessity:** these objects express the complement-side path obstruction that ordinary `F` does not. **Definition/standing:** reader `1143-1181` supplies the exact sequence, two predicates on maps, and dual language. **Nonredundancy:** `1182-1188` gives the quantifier reversal, vacuity, complement role, and nonidentity with ordinary acceptance. **Use:** every later half-step and emptiness recursion uses them. Rabin printed pp. 24--26 control. |
| `\Omega^\dagger` | **Necessity:** Lemma 3.6 can produce no pairs while the printed induction begins at one. **Definition/standing:** reader `1190-1203` introduces one exact pair sequence. **Nonredundancy:** `1203-1212` proves that it has the empty path type, is dual-equivalent to the zero sequence, and is not new semantics. **Use:** expressly promised at `1212-1213` and performed at `1249-1256,1340-1342`. |
| marked tree at `H` | **Necessity:** local automaton obligations must be activated and recorded at nodes. **Definition/standing:** reader `1218-1222` types finite marker set `Q`, marking relation `H\subseteq T_x\times Q`, and the enlarged label. **Nonredundancy:** it is a labelled tree construction, not an acceptance condition or a new tree domain. **Use:** simultaneous copies, merging, and Lemmas 3.2/3.4 immediately use it at `1222-1233`. Rabin printed pp. 19--20 control. |
| well-founded mapping `h\mapsto H_h` | **Necessity:** within the same enumerated introduction, reader `1244-1247` states that locally activated obligations may defer and that those deferrals must not continue endlessly. **Definition:** `1227-1230` gives exactly no infinite `h_{m+1}\in H_{h_m}` chain. **Standing:** it is a mapping on a nonempty obligation set, not a motive, state, path language, or new acceptance field. **Nonredundancy:** its dependency-chain role is separated from ordinary run/path acceptance at `1167-1188` and from simultaneous same-state merging at `1219-1225`; Lemma 3.4 adds this condition to, rather than renames, Lemma 3.2. **Use:** lower ordinal strata, Lemma 3.4, arbitrary-sequence Lemma 3.11, and the precise transfinite locus at `1230-1254,1296-1303`. Note `425-435` and compact `668` repeat all five locally. Rabin printed pp. 19--20 and 27--30 control. |
| `\Omega_{k-1}` and last-lower-set-empty | **Necessity:** these distinguish the shorter induction input from a same-length transformed input. **Definition/standing:** reader `1240-1247` gives the truncated sequence and exact `L_k=\varnothing` condition. **Nonredundancy:** same-length Lemmas 3.7--3.8 are separately stated at `1235-1238`. **Use:** the two positive-length half-steps at `1249-1256` and emptiness recursion at `1361-1371`. Rabin printed pp. 26--32 and 33--34 control. |
| `\operatorname{Ft}(E)`, terminal-node frontier, and `frontiered` | **Necessity:** the valuation and finite automaton need an exact separation between internal labelled nodes and terminal external-boundary nodes. **Definition/standing:** reader `1259-1267` gives the set and says `frontiered` is a property of `E`. **Nonredundancy:** `1268-1271` explains exactly that predecessor closure permits a one-child node while frontieredness does not. **Use:** finite-tree automata, Lemma 3.12, the complementation base, and `E_0,\ldots,E_m` at `1272-1294,1373-1389`. Note `311-324,523-550` and compact `670` replay all five. Rabin printed p. 30 controls. |
| external frontier value `f` | **Necessity:** a finite run must record that both successors have left the finite labelled interior. **Definition/standing:** reader `1272-1283` types `f\notin S`, its sole permitted transition pair, and its frontier assignment. **Nonredundancy:** the reader twice states that `f` is external and not an ordinary state. **Use:** finite-tree acceptance and the lift at `1281-1287`. Rabin printed p. 30 controls. |
| `M^\bullet` | **Necessity:** the emptiness question must forget input letters while preserving every possible transition choice. **Definition/standing:** reader `1307-1314` defines a one-letter table by coordinatewise union. **Nonredundancy:** it changes only labels/transitions, not the state set or acceptance family. **Use:** the exact two-way run equivalence and unique-tree reduction at `1315-1322`. Rabin printed pp. 32--33 control. |
| current table/current sequence and restricted table `N_{R'}` | **Necessity:** effective reductions can change the finite table/state set, and Definition 3.7 restricts descendants without disallowing the named root. **Definition/standing:** reader `1335-1348` binds `R`, `N`, `\Omega`, and defines `N_{R'}` as a table restriction with formal state set retained. **Nonredundancy:** `1349-1351` distinguishes descendant-state restriction from root-state membership. **Use:** the nonempty-`H` half-step at `1361-1371`. Rabin printed pp. 33--34 control. |
| `H_0,H_1,\ldots`, `U_0`, and `E_0,\ldots,E_m` | These are locally bound proof objects rather than names of new theoretical kinds. Their **necessity, standing, and use** are nonetheless immediate: disjoint strata make finite termination explicit at reader `1353-1359`; `U_0` and the trees type the finite base certificate at `1373-1386`. Their **definitions and nonredundancy** are the displayed subset/enumeration clauses and the distinction between a state witness set and finite tree witnesses. The `m=0` clause proves that neither name hides a nonempty assumption. Rabin printed pp. 33--34 control. |

The detailed note and compact record do not defeat these first uses through
their history passages. The detailed note's opening history at lines 18--43 is
generic until the objects receive their substantive definitions. In that note,
`frontiered` first receives its exact property standing, distinction from
predecessor closure, and uses at lines 311--324; the well-founded mapping first
receives necessity, standing, exact definition, nonredundancy, and use at
425--435; and `\Omega^\dagger` receives the zero-case need, exact definition,
standing, proof of nonredundancy, and later use at 393--416. In the compact
record, the corresponding first substantive introductions are lines 664--670;
its history follows those introductions at line 672. The status histories
therefore do not create premature technical names.

Established source or literature names such as “Muller automaton,” “König's
Infinity Lemma,” “weak monadic second-order theory of two successors,” and
“regular-tree basis theorem” are not repackaged as novel handbook objects. Each
is given its source standing and exact role, and each external dependency is
identified rather than silently assumed. I found no speculative name, unnamed
primitive, redundant new relation, or unused named distinction.

## Cross-record identity, attribution, rights, and status reconciliation

The four prose/bibliographic frozen records agree in all publication-sensitive
respects:

- Rabin is Michael O. Rabin, *Transactions of the American Mathematical
  Society* 141 (1969), pp. 1--35, DOI
  `10.1090/S0002-9947-1969-0246760-1`; the bibliography retains the inspected
  EPFL scan URL (`handbook.bib:5973-5982`).
- Meyer is Albert R. Meyer, the 1975 publication of the Vancouver 1974 ICM
  proceedings, vol. 2, pp. 477--482. The reader and both records use Meyer only
  for the later complexity correction, not for Rabin's definitions or proof
  architecture (`handbook.bib:5938-5947`; note `71-109`; compact `662`).
- McNaughton remains the external sequential-word dependency and is not
  credited with Rabin's tree construction (`handbook.bib:2290-2299`; reader
  `1114-1139`).
- Thatcher--Wright retains the full article identity, pp. 57--81 and DOI
  `10.1007/BF01691346`, while the prose accurately says only that Rabin cites
  Doner and Thatcher--Wright for the external weak-theory base
  (`handbook.bib:5993-6002`; reader `1381-1400`). No full source proof is
  laundered into Rabin.
- Thomas retains the 1997 chapter identity, pp. 389--455 and DOI
  `10.1007/978-3-642-59126-6_7`, and is confined to the expressly later survey
  route (`handbook.bib:2346-2355`; reader `1432-1437`; compact `674-680`).
- The detailed note's opening and closing histories agree: Rounds 1--3 and
  5--7 are closed/rejected, Round 4 was withdrawn before filing, no terminal
  admission is claimed, and a fresh Round 8 is required (`18-46,653-665`). The
  compact record gives the same pre-review state (`672,913`). Acceptance in
  this report therefore cannot be read as a whole-Part or final-book status.

## Limitations of this verdict

This was a manuscript-scholarship review, not a mechanical or visual
publication-production gate. I did not test compilation, inspect a rendered
handbook page, verify typography after TeX layout, inspect another part, assess
all of Part IX, or conduct human/user review. Those unperformed categories are
not evidence against the narrow content verdict, but neither are they silently
claimed by it.

VERDICT: ACCEPT

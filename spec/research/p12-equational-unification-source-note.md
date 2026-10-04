# Baader-Snyder equational-unification authoring block

2 October 2026, authoring block begun approximately 10:12 UTC. This is a
partial source-specific reconstruction with reciprocal editorial proofs,
not an admission record, manuscript review, or completion of the allocation.

## Scope and ownership

The complete candidate-3 record in `work/next-formal-authoring-units.md`
and exact queue row `ED26-REQ-N-c-035-05` were read before authoring.
Parent `N-c-035-C01` and allocated `N-c-035-MAP-05` require the identified
Baader-Snyder equational/AC methods and examples, including generality,
type, methods, proof hypotheses, constructions and limitations.
The queue's proposed body and annex paths exactly match the assignment:

- `handbook/parts/p12/presentations/n-c-035-05.tex`,
  `sec:p12-n-c-035-05`.
- `handbook/annex/p12/n-c-035-05.tex`.
- `handbook/registry/calculi/p12-equational-unification-narrowing.tex`
  (additional explicit ownership in the second block).
- `handbook/bib/intake-p12-equational-unification.bib` (reuses canonical
  `BaaderSnyder2001`; the third block adds the actual cross-referred
  `DershowitzPlaisted2001Rewriting` chapter entry, absent from canonical bib).
- `handbook/registry/symbols-intake-p12-equational-unification.csv`.
- `source/references/p12-equational-unification/manifest.json`.
- This source/construction note.

The named symbol scope **P12 Baader-Snyder equational unification** is the
union of that body section, all eighteen items in its matching annex,
and the source-specific narrowing sheet. The original seven proofs remain.
The lead owns route installation, shared hosts/style/drivers, canonical
bibliography/symbols, all generated surfaces, crosswalk and disposition.
No competing `har2001-c08.tex` was created. The overlaps with
`ED26-SRC-037-0008-C002` through `C005` must be bound by the lead and
must not be counted as another completed chapter.

The presentation parent did not yet exist. Exact scoped permissions were
requested. The normal shell still denied directory creation after the
grant, so exact escalated `New-Item` created only that presentation
directory. Subsequent normal shell calls developed helper setup-refresh
errors; read-only source commands used the scoped escalated alternative.
No shared file was written. All text artifacts were created by apply_patch.

## Governing instructions and actual prerequisite reading

The research and PDF skills were read completely. This author is the
already delegated investigator, so the explicit no-children instruction
precluded a further research agent. Research's primary-source/note workflow
is followed here. PDF use is source reading and glyph inspection, not
creation, editing or rendering of a manuscript PDF. No manuscript build,
render, prose test, review agent, paid acquisition, login or external
contact was performed.

The full `handbook/CONVENTIONS.md`, `spec/EDITION-2026-CONTRACT.md`, and
`spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md` were read. Current
`handbook/parts/p12/unification-extraction-adequacy.tex` and its matching
annex were read completely. The current `first-order-automation.tex`
unification host, especially lines 186-228, was read. The finite syntactic
termination/extraction/MGU block is present and is not reauthored as an
equational theorem here. Its reusable interface is finite-support
simultaneous substitution, first-then-second composition, and the proven
syntactic solver for the actual empty-theory variant problems.

Read-time current prerequisite SHA-256:

| File | SHA-256 |
| --- | --- |
| `handbook/parts/p12/first-order-automation.tex` | `154CE0329220F74D4FA5A845282293DA01AC23C4105C3C6FBB5B7F20156EEF9F` |
| `handbook/parts/p12/unification-extraction-adequacy.tex` | `E84D3FA2F3B0E3D9A3B105BCEAF56B7965AB67ED03D811B1A88EE91207EB2881` |
| `handbook/annex/p12/unification-extraction-adequacy.tex` | `C2C3252B309FACA24AEAAB7845779CD68CC3065E4070626CC50D23C06E7B127D` |

The host still says its retained-equation sheet has solved substitutions
"accumulated by Eliminate"; that is not the literal sheet state, whose
exact solution-set equality already has a proof. Its brief equational
sentence says "multiple incomparable MGUs". Under the source's singleton
definition, incomparable answers are members of a minimal complete set,
not each an MGU covering all solutions. Both observations were sent to
the lead; this writer did not change the host.

## Exact held manifestation and actual reading

Primary identity: Franz Baader and Wayne Snyder, *Unification Theory*,
Handbook of Automated Reasoning, 2001, DOI
`10.1016/B978-044450813-3/50010-2`. The canonical bibliography currently
uses published pp445-532. The held **89-page ICCL PS-derived manifestation**
has printed pp445-533; it is not independently compared final publisher
typography. The alternate 88-page pp439-526 manifestation remains distinct.

Held citation PDF:
`citations/Baader and Snyder - Unification Theory (2001, Handbook of Automated Reasoning chapter, PS-derived PDF).pdf`.
Its read-time SHA-256 is
`4197E9729D3DAFC0E889F64BB46940D71254F90EBDCF948138626F9D2865934B`.
The original derived-PDF hash retained by the handoff is
`84ebf4ddd5a041e09d3f757aea7e638b85f939d629b7d5fd7729ab3af3b99fc1`.
No new byte identity with that file or a publisher file is inferred.

Readable extraction:
`tmp/acquisition/src037/iccl-unification-ps-gz-retry-02.body.derived-decompressed.ps.derived-render.pdf.derived-layout.txt`.
Read-time SHA-256:
`C3ED63CD9E95B000B0EBC5D8339AC9BC100652A80AA5F4E0A702D0B557323BC2`.
Actual contiguous reading completed over lines1047-3351, all of sections
3 through 6, printed pp469-519 with shared boundary pages. This is
**not reading of the entire 89-page chapter**: sections1-2, full section7,
bibliography and index were not read. The continuation additionally read
extraction lines343-591, including complete subsections2.2.3-2.2.5 and
surrounding partial context, to ground the literal source U helper.
No whole-chapter source qualification
is asserted. Headings occur at extraction lines1047,1978,2640,3068,3352.

The citation PDF was opened with PDFium; 89 pages and page mapping
physical one-based = printed -444 were observed. Source pages470,471,506
were rendered and visually inspected. Page506 resolves a real extraction
defect: the AG generator is `(1,-2,0)`, not the extracted `(1,2,0)`.
Pages470-471 verify the source's dotted comparison, problem-variable
restriction, cardinality and strict type separation. A further source-only
detail render retained in the source-reference directory confirms an
interior dot in a less-than angle with a lower horizontal line; the draft
reconstructs that relation with underlined lessdot, and the symmetric
relation with dotted equality. Their manuscript typography remains a
visual/fidelity check. The mathematical roles are not replaced with
the global syntactic instance order.

## Retained first-block construction

The body has source-attributed definitions for E-congruence, finite E
problems, problem-variable generality, complete/minimal sets, four types,
signature regimes, output contracts, free-algebra and constant-restriction
interfaces, the three exact ACU/ACUI/AG theories, homogeneous and
inhomogeneous constructions, and the semiring criterion.

Seven body claims have full reciprocal **editorial proofs**; they are not
represented as transcribed source proof prose:

| Body result | Reciprocal annex | Scope established |
| --- | --- | --- |
| `thm:p12-eu-minimal-sets` | `annex:p12.n-c-035.5.minimal-sets` | Preorder, quotient, minimal classes, antichain characterization, existence and representative uniqueness, including empty solution set. |
| `thm:p12-eu-c-and-a` | `annex:p12.n-c-035.5.c-and-a` | C root-variant finite complete construction using an explicitly justified syntactic bridge; two incomparable ground C answers; infinite antichain complete A answers for the source word equation. Not the whole general associative procedure. |
| `thm:p12-eu-categorical-bridge` | `annex:p12.n-c-035.5.categorical-bridge` | Generator maps, quotient well-definedness, equation/composition bridge, problem-variable factorization; explicit failure of coequalizer uniqueness for the unused-generator example. |
| `thm:p12-eu-coordinate-models` | `annex:p12.n-c-035.5.coordinate-models` | ACU natural counts, ACUI supports, AG signed counts; both equality directions; inverse-law derivation; matrix composition; fixed free constants. |
| `thm:p12-eu-homogeneous-completeness` | `annex:p12.n-c-035.5.homogeneous-completeness` | Soundness, all-solution-column factorization, fresh-variable scope, full Dickson finiteness/generation argument and elementary subgroup-of-Z^n finite-generation proof. Computational normal-form and bounded basis algorithms remain separate. |
| `thm:p12-eu-constant-completeness` | `annex:p12.n-c-035.5.constant-completeness` | Particular/homogeneous factorization, empty-inhomogeneous failure, finite choices, ACU minimal particular argument, AG one-coset property, complete two-answer source ACU example and editorial three-answer ACUI witness. |
| `thm:p12-eu-semiring-criterion` | `annex:p12.n-c-035.5.semiring-criterion` | Both directions of finite homogeneous generation/MGU and finite particular translates/finite complete constants under the explicit semi-additive matrix interface; exact fixed-constant block multiplication. |

Worked source examples retain the ACU vectors `(1,1,1),(0,3,1),(3,0,2)`,
the three separate source answers and their combined answer, the further
`(1,4,2)` example and factor, ACUI Boolean generators, AG signed generators,
and the two ACU constant answers. Coordinate notation `coef` and the
general subgroup proof are explicitly editorial typed additions. Source
occurrence-count bars are retained and registered locally, not renamed
merely to evade house glyph policy. The general comparison remains the
source E/problem-variable comparison, not syntactic global factor equality.

## Exact remaining work: allocation remains partial

Reading the source is not completing its reconstruction. All of
`N-c-035-MAP-05` remains open as a source unit; the completed mathematical
subresults above must be retained when continuing, not redone or used to
discard the rest.

1. **Section3/C002:** full free-symbol abstraction bridge; systems versus
   single equations with its free-wrapper hypothesis and elementary
   countercases; full positive existential and positive AE Theorem3.14
   reductions and proofs; Theorem3.16's general-positive/LCR dependencies;
   source survey's distributivity, rings, endomorphism cases and exact
   decision/type/algorithm boundaries. AI type-zero nonexistence is
   source-attributed, not independently proved here; separate promised
   full-proof obligations must be resolved, not waived by this attribution.
2. **Section4/C003:** the continuation now supplies the U helper, G/B/N
   state/rule surfaces, G soundness and actual lifting, both critical-pair
   directions, and directed B/N lifting with its required grounding domain.
   The third block now supplies the actual cross-referred ordered-Cr
   interface, direct ordered-closure proof, and a genuine comparison with
   the separately labelled F_omega, plus Reduce/redex-ordered composites
   and eager/Propagation/Blocking/lower-index proof cases with literal
   and corrected variants kept distinct. Remaining source-specific work
   includes §4.2 hereditary overlap refinements and full reconstruction
   of the original RE/basic-rewrite and minimal-proof-length presentation
   in Lemmas4.7-4.9 alongside the independently proved alternative route.
   Ground-domain/basic-LP direction and refinement corrections below remain
   explicit source-fidelity and referred-version dependencies, not waivers.
3. **Section5/C004:** the source's complete monoidal/commutative equivalence
   and alternative AG presentation, Proposition5.3 and the precise implicit
   operation argument; full semiring/interface construction beyond the
   explicit matrix hypothesis; remaining four reported results at p512 and
   their external dependencies. Effective finite-basis/particular-solution
   algorithms are not implemented merely by proving finite generation.
   Pure AC's flat variable/constant construction is now supplied by the
   fifth-block fragments below. ACI proper and general free-symbol-input
   combination constructions remain; pure AC was not equated with ACU.
4. **Section6/C005:** full alien abstraction and reconstruction, partitions,
   labels and LCR orders with nonshared-variable convention, recursive
   sound assembly, complete-set cross product and normalized/layer-reduced
   completeness. The source's normalized-solution proof is a sketch with
   referred-source dependencies; the separate full-proof duty remains.
   No disjointness or algorithmic component hypothesis may be omitted.
5. **Whole chapter/C006-C007:** sections1-2 and7 and every distinct retained
   manifestation/final publisher-layout comparison are separate remaining
   obligations. This unit supplies no new credit for C001's complete
   source-specific finite syntactic chapter, no higher-order undecidability
   reduction, and no whole-chapter admission.

The short proofboundary paragraphs expose these dependencies to the reader;
they are not completed substitutes for their missing treatments.

## Verification standing and integration

Author reasoning checked the comparison domain, composition direction,
empty answer, finite support, constant fixing, nonnegative versus Boolean
versus signed coordinates, and the counterexamples to one-MGU and
coequalizer substitutions. Eighteen reciprocal proof pairs are present by
direct author inspection. No automated prose tests, checker build,
manuscript render, independent review, or admission is claimed. Source
rendering only was performed for ambiguous mathematical glyphs.

Lead should route the new source section after the syntactic interface and
its matching annex, bind the named symbol scope, merge comment-only/intake
records as appropriate, and preserve all component residuals above in the
shared crosswalk. Consolidated static/build/visual and independent source,
topic and adversarial gates remain later work. The author does not admit
their own unit.

## Second authoring block: 10:53 UTC onward

Current body/annex hashes were checked before editing and matched the
first return. The six new full editorial proof pairs, added without
removing the original seven, are:

| Body result | Reciprocal annex | Established scope |
| --- | --- | --- |
| `thm:p12-eu-u-bridge` | `annex:p12.n-c-035.5.u-bridge` | Literal source U removing-binding multiset state, solved-support invariant, all termination cases and global factorization. |
| `thm:p12-eu-gbn-soundness` | `annex:p12.n-c-035.5.gbn-soundness` | Backward implication for every G/B/N core transition; equational versus syntactic failure distinction. |
| `thm:p12-eu-cp-ground-closure` | `annex:p12.n-c-035.5.cp-ground-closure` | Explicit unrestricted critical closure; conservative congruence; all disjoint, critical and nested-variable peaks, including erasure/duplication and changed orientation. |
| `thm:p12-eu-cp-elimination` | `annex:p12.n-c-035.5.cp-elimination` | Both directions and root overlap; actual U MGU/fresh-variable interface; repaired mandatory first decomposition; depth-multiset elimination to E. |
| `thm:p12-eu-g-completeness` | `annex:p12.n-c-035.5.g-completeness` | Actual reduced ground witness and admissible innermost LP block; decreasing term-multiset induction; elimination and ungrounding back to original E. |
| `thm:p12-eu-bn-completeness` | `annex:p12.n-c-035.5.bn-completeness` | Grounding-domain equivalence and every C/Constrain/LP induction case; B/N skeleton differences and source multiset/lexicographic measure. |

The companion closure is explicitly unrestricted, not misattributed as
the source's exact ordered E_omega. Its identities are eliminated before
the original G result is returned. Existence of a decreasing successful
branch does not prove termination of the search tree or an effective
normal-form computation for an infinite closure.

Source PDF pages489,493,494,496,497,498,499 were rendered as source-only
evidence; pages489,494,496 were visually inspected directly. No manuscript
rendering was performed. They confirm two consequential qualifications:

1. Page489 requires first Decomposition of a new nonvariable LP match.
   Printed Case Two on p494 delays that decomposition while performing a
   nested LP. The repair decomposes first and moves the nested step into
   the corresponding child equation, preserving the earlier rule surface.
2. Directed Narrow uses forward R rules explicitly in §4.4.1, whereas
   the basic LP display refers back to G's restrictions without restating
   whether inverses are included. The new directed completeness theorem
   declares convergence after finite fresh-constant extensions. Its failing
   case R={f(x,y)->a, f(x,x)->g(x), g(a)->a} is terminating and ground-
   confluent on original closed {a,f,g} terms, has nontrivial E and
   g(x)=E a, but only x=a is returned by directed narrowing on g(x)=?a.
   Identity is not covered; fresh c exposes an unjoined peak. This does
   not refute an inverse-identity LP interpretation: G can first replace
   g(x) by f(x,x). The source wording is retained with this exact boundary,
   not silently relabeled as the strengthened theorem.

The concrete B/N example R={g(a)->b}, input h(x)=h(b), x=g(a), distinguishes
the prohibited basic substituted position and nonreduced solved image
from a successful alternate branch reducing g(a) first. Blocking rejects
a reduced-witness branch; it does not certify absence of all E-solutions.

The sheet is additional explicitly owned work. It registers all core
G/B/N transitions and the U helper failures, B-only Solve/Narrow composites,
and individual Problem Decomposition, Variable Abstraction, Propagation,
Blocking rules. Remaining full refinement constructions and proofs are
preserved in item2 above. No independent review, build, manuscript render,
prose test or self-admission was performed.

## Third block: ordered closure and refinements (12:38 UTC onward)

Starting body/annex hashes matched the second-block return. All thirteen
earlier proofs remain. The source's Definition4.10 leaves its ordered
Cr interface to the adjacent rewriting chapter. The actual primary
author-hosted chapter was freely acquired from
`https://www.cs.tau.ac.il/~nachum/papers/hand-final.pdf`, saved as
`source/references/p12-equational-unification/dershowitz-plaisted-2001-author-hand-final.pdf`.
SHA-256: `D755FC3B24D68721E6B8F3DAB6B9DC904CEE69FE23CA2E5319FF59C058C14D79`.
It has 76 physical pages, printed535-610; physical one-based = printed-534.
Complete §6 pp567-574 and the specific Definition4.5 passage on p547
were read. Page569 was rendered and visually inspected. No whole-chapter
reading or publisher-file comparison is asserted. The exact Snyder1991
Theorem6.1.7 body was not acquired/read and is not substituted by this file.

Definition6.2 actually admits an ordered overlap only if SOME substitution
witnesses both not-≤ tests of the common source against its two branches.
It is not unrestricted CP formation followed by orientation. The witness
may be nonground, so incomparability matters. The new ordered-closure proof
uses actual ground peaks to satisfy those tests, with variable-image and
trivial-theory cases proved explicitly. Its normal forms and F_omega's
normal forms are compared through the same least ground E-class member;
no set identity is claimed. Transport of the G simulation declares the
additional open proper-subterm ordering property, e.g. LPO, which excludes
inner variable-left overlaps in nontrivial theories and justifies common-
selector level inclusion. Ordered normalization is proved directly.

Five new full editorial reciprocal proof pairs bring the total to eighteen:

| Body result | Reciprocal annex | Established scope |
| --- | --- | --- |
| `thm:p12-eu-ordered-closure` | `annex:p12.n-c-035.5.ordered-closure` | Exact existential ordered filters, conservative closure, all ground peak cases, trivial theory, common least-class normal forms and qualified G-interface transport. |
| `thm:p12-eu-local-simplifications` | `annex:p12.n-c-035.5.local-simplifications` | Every local witness/descent check for constructor decomposition, corrected Propagation, cleaned Reduce and actual C rules; distinct N coordinate ordering. |
| `thm:p12-eu-eager-corrected` | `annex:p12.n-c-035.5.eager-corrected` | Finite eager simplification phase plus actual core lifting cases, output factorization and ungrounding; no completeness assumption hidden in a helper lemma. |
| `thm:p12-eu-eager-reduce-literal` | `annex:p12.n-c-035.5.eager-reduce-literal` | Literal Reduce alone with permanent isolated fresh domains, active reduced witnesses and original-variable coverage; no use of inactive images as certificates. |
| `thm:p12-eu-ordered-narrow-blocking` | `annex:p12.n-c-035.5.ordered-narrow-blocking` | Minimal-redex/protected-position cases, finite original-position abstraction, actual lowest-index matching test, intermediate C proper-normality and eager Blocking survival. |

The registry retains printed Propagation separately and adds its nonvariable-
skeleton correction, literal versus cleaned Reduce, B and N composites,
finite redex-ordered blocks and lower-index restrictions. Corrections have
explicit reader examples and proof boundaries:

- Printed Propagation permits u to be a variable even when u sigma_S is
  nonvariable. Repeated fresh aliases then leave the proposed skeleton
  size unchanged and prevent an eager strategy from reaching solving.
  The corrected variant removes only actual nonvariable skeleton terms.
- Literal Reduce can retain a fresh image g(y) which becomes reducible
  under a reduced old witness. With R={f(z)->a,g(b)->c}, input
  f(g(y))=a,h(g(y))=h(c), the solution y=b exposes the failure of using
  that match binding as a normality certificate for Propagation/Blocking.
  Cleaned Reduce discards only the now-isolated fresh matching domains.
  Literal Reduce alone remains complete by a separately proved active/
  inactive-variable invariant, not by pretending all its bindings normal.
- Reduce's displayed match target is u sigma_S; the source's abbreviated
  parenthetical l gamma=u cannot be read literally when S is nonempty.
- Redex-ordered abstraction is a finite pass on earlier retained context
  positions, not repeated abstraction of newly created variables. Removed
  positions inside the old redex are not positions of the new context.
- N Elimination can increase skeleton size, so the corrected N proof puts
  its constraint counters before i. The source B ordering is retained.
- Fresh-variable simplification must compare designated binding-satisfying
  extensions, not arbitrary fresh assignments; otherwise the unrestricted
  restriction biconditional cannot justify Propagation's new binding.

These are author constructions/corrections with primary mathematical
evidence, not independent acceptance. No children, reviews, builds,
manuscript renders, prose tests, shared/canonical/queue edits or blanket
allocation completion were performed. All remaining §3/§5/§6/chapter/version
obligations above remain owed.

## Fourth block: released-core freeze and new hereditary fragments

Started 14:44 UTC, 2 October 2026. The lead began integrating the released
core and expressly froze this writer's core body, annex, rule sheet and
intakes. They were read, not edited. New owned outputs are
`spec/fragments/p12-equational-hereditary-body.tex`, matching
`spec/fragments/p12-equational-hereditary-annex.tex`, and unique
`-hereditary` bibliography/symbol intakes. These are not yet routed by
this writer. The named scope **P12 equational hereditary fragments** is
their body subsection plus matching five annex items; the lead owns final
insertion and scope binding. The core eighteen pairs remain separate
from the five new unintegrated pairs.

Exact rereading covered source Definitions4.3-4.6, Lemmas4.7-4.9 and their
complete printed proofs, pp489-492, and complete §4.2 p495. Source pages
490,491,492,495 were rendered, and pp490-491 were directly visually
inspected. Current core G states, ground/ordered closure definitions,
arbitrary G and B/N witness proofs were also read. No new whole-chapter
or alternate-manifestation reading is asserted.

Five reader-ready reciprocal fragment proofs establish:

| Body result | Annex | Content |
| --- | --- | --- |
| `thm:p12-eu-h-minimal-instance` | `annex:p12.n-c-035.5.h-minimal-instance` | Lexicographically minimal applicable ground pair has genuinely reduced generating images, including right-only identity variables; R and R_E normal terms coincide. |
| `thm:p12-eu-h-basic-normalization` | `annex:p12.n-c-035.5.h-basic-normalization` | Actual fresh-skeleton construction at every step; finite R_E normalization; source4.7 endpoint and4.8 equivalence, not an assumed basic lifting lemma. |
| `thm:p12-eu-h-basic-transport` | `annex:p12.n-c-035.5.h-basic-transport` | Position-by-position transport through a finite literal solve preserving the ground witness; same ground steps and proof-length upper bound. |
| `thm:p12-eu-h-minimum-blocks` | `annex:p12.n-c-035.5.h-minimum-blocks` | Original four-tuple objects, explicit minimum over R_E proofs, all normal-equation cases, actual LP/full-U-matching blocks, strict length decrease, reachable solved-state invariant and fixed-domain final factorization. |
| `thm:p12-eu-h-convergent-hereditary` | `annex:p12.n-c-035.5.h-convergent-hereditary` | Whole common-nonvariable-head agreement and historical copied-occurrence eligibility for that precise ground-convergent/reduced-witness regime. |

Two independent repairs of the printed descent argument are retained
beside the source measure, with concrete finite examples:

- For E={f(a)=a}, f(a)=?a has minimum length1, but raw LP adds
  f(a)=f(a), whose two normal-form legs total2. Raw LP does not decrease m.
- With f(x)=x and f(f(x))=x, even the mandated first decomposition can
  leave f(a)=f(a), again of length2 after an original one-step proof.
  The repair solves the entire introduced literal matching problem.
- With E={f(x)=a,g(b)=c}, the shortest unrestricted basic proof of
  f(g(b))=a erases a nonnormal image. Its first instance is not reduced;
  the reduced-instance minimum instead uses g(b)->c then f(c)->a.
  The repaired minimum is explicitly m_R_E, not silently the unqualified
  source m. Removing the selected first reduced step and transporting
  every remaining basic path gives the strict decrease actually proved.

The original arbitrary-theory hereditary allocation remains OPEN.
The new theorem states its convergent hypotheses explicitly and does not
weaken that outstanding goal. Reusing the previous arbitrary G proof is
not enough: source CP simulation Case Two can introduce a matching
pattern with a deeper head mismatch, and nested MGU expansion can turn
primitive-template occurrences into substitution-history copies. Those
compatibility/mark transports were examined but not proved generally;
they are not asserted as helper lemmas or granted as assumptions.

Primary acquisition checks located the institutional DJ1992 URL, the
official MPI Socher report and the Springer Moser1993 chapter record.
The DJ URL now redirected in browsing to the Figshare home page and its
shell request timed out; no PDF file was saved. MPI body access returned
403; no bypass or alternative protected access was attempted. Moser's
publisher record exposed metadata/subscription access only. None of
DJ1992, Socher1994 or Moser1993 is called fully acquired or read. A
primary author publications page was found for DJ1992, but metadata is
not its mathematical body. No bibliography entry or credit is fabricated
for a read body. The separate 1990 conference manifestation is not used
as a substituted 1992 journal version.

Next decisive dependency is a complete identified arbitrary-theory
hereditary-refinement body/proof, or a successful independent proof of
the nested compatibility and occurrence-history transports. All original
§3/§5/§6/whole-chapter/version residuals remain owed. No children,
independent reviews, builds, manuscript renders, prose tests, canonical,
queue or released-core edits were performed. Source-image rendering only
was used. The fragments are author work, not self-admission.

## Fifth block: pure AC positive images (15:32 UTC onward)

Core body/annex/sheet and hereditary fragments remained frozen and were
not edited. New owned outputs are `spec/fragments/p12-equational-ac-body.tex`
and matching `spec/fragments/p12-equational-ac-annex.tex`, with unique
`handbook/bib/intake-p12-equational-ac.bib` and
`handbook/registry/symbols-intake-p12-equational-ac.csv`. The named scope
**P12 pure AC fragments** is this body subsection plus its six reciprocal
annex items. Root owns insertion, routes and canonical merges.

The full retained chapter §5, extraction lines2640-3067, was reread,
including its exact ACU/ACUI/AG constructions, constant columns and
explicit limitation to elementary/constant semantic methods. Current
ACU/ACUI/AG definitions and source examples were read without editing.
Pure AC's no-unit construction is attributed separately, not fabricated
as an unnoticed ACU case in the chapter's monoidal class.

The chapter-selected 1975 paper was actually acquired from the official
IJCAI proceedings URL `https://www.ijcai.org/Proceedings/75/Papers/011.pdf`.
Held file: `source/references/p12-equational-unification/stickel-1975-ijcai.pdf`.
SHA-256: `A44961390E79703845BEF9B7E24E477FC0DF3BFB94C56CEF04D21652BF221002`.
All six pages, printed71-76, were read; all were source-rendered and
directly visually inspected to recover equations/tables missing from OCR.
Physical one-based page = printed-70. The actual endpoint76 is retained
instead of the held chapter bibliography's71-82 range. The 1975 body is
not the distinct 1981 JACM article. Publisher PDF access for the latter
returned403 and a managed challenge; no login, challenge execution,
security bypass or body-reading claim was made.

The source's one-equation procedure retains its real bound
K=max(m,n) max(lcm(a_i,b_j)), positive-variable subset condition,
cancellation argument and coefficient-only-variable factoring proof.
The simultaneous-system extension is explicitly editorial: enumerate
positive one-dimensional rational kernel rays, form the coordinate box
bound from their sum, enumerate integer kernel remainders, and retain
actual global minima. Its cone splitting, finite remainder and integer
generation arguments are proved, not imported as a named Hilbert-basis
oracle. Constants use augmented homogeneous last-coordinate1 generators,
with a full proof of exact affine minimality and coverage.

Six full editorial reciprocal pairs are supplied:

| Body | Annex | Scope |
| --- | --- | --- |
| `thm:p12-ac-multisets` | `annex:p12.ac.multisets` | Nonempty free-commutative-semigroup coordinates, composition and genuine cancellation, including internal empty balances. |
| `thm:p12-ac-single-bound` | `annex:p12.ac.single-bound` | Source positive-coefficient lcm bound, finite search, exact minima and generation. |
| `thm:p12-ac-system-basis` | `annex:p12.ac.system-basis` | Rational support rays, constructive cone generation, proved finite integer remainder bound, exact homogeneous minima and generation. |
| `thm:p12-ac-particulars` | `annex:p12.ac.particulars` | Actual augmented-kernel computation; exact minimal affine columns and one-particular-plus-homogeneous representation. |
| `thm:p12-ac-coverage` | `annex:p12.ac.coverage` | Finite positive-support enumeration, legal term extraction, every target's nonempty factor, empty/ground/duplicate cases. |
| `thm:p12-ac-minimality` | `annex:p12.ac.minimality` | Indecomposable target columns and affine minima force identical comparable candidates; canonical deduplication is justified. |

Every selected parameter gets a nonempty AC term. Unused basis vectors
are omitted from the chosen subset, not assigned a nonexistent empty
product. Empty I is allowed only when constants already cover every
variable row. A constant named e remains an ordinary one-atom term;
no zero row receives an invented unit. Variables cancelled from a count
equation remain unconstrained original variables rather than empty images.

Direct finite arithmetic verification (not a manuscript/prose test)
enumerated the source equation 2*x1+x2+x3=2*y1+y2 within its proved
bound6. It reproduced the seven source minimal vectors and exactly69
positive-row subsets. The original constant example f(x,x,y,a)=f(b,b,z)
has the four extracted answers, reproduced independently through
H={(0,1,1),(1,0,2)}, P_a={(0,0,1)}, P_b={(1,0,0),(0,2,0)}.
The earlier chapter equation 2*x+y=3*z has five pure-AC answers versus
one ACU answer; zero-row singles are rejected. Divisibility, kernel-zero,
one-sided cancellation, duplicate rows, empty input and ground-only
equations have explicit boundaries/examples.

This supplies the complete stated flat f/variable/free-constant system
algorithm, including simultaneous equations. It does not waive the
general nested/free-function-input algorithm or the 1981 exact-version
body. Stickel1975's general extension invokes recursive reconciliation
and lesser-complexity calls; that unrestricted termination proof and
the source §6 combination obligation remain separate. The arbitrary-
theory hereditary gap from the fourth block remains OPEN. All other
§3/§5 monoidal/§6/chapter/version residuals remain allocated. No children,
reviews, builds, manuscript renders, prose tests, released-file/shared-
canonical/queue edits or self-admission were performed.

## Sixth block: disjoint-theory combination (17:42 UTC onward)

Owned new outputs are `spec/fragments/p12-equational-combination-body.tex`
and `spec/fragments/p12-equational-combination-annex.tex`, plus unique
`handbook/bib/intake-p12-equational-combination.bib` and
`handbook/registry/symbols-intake-p12-equational-combination.csv`.
Core body/annex/sheet, hereditary fragments and AC fragments remained
frozen and were not edited. Root retains insertion/routing/canonical
ownership. The named new scope **P12 combination fragments** is this
subsection and its seven reciprocal full editorial proofs.

The entire source section6 was reread: extraction lines3068-3351,
printed513-519. Its exact source construction remains purification,
shared-variable partition, labels, linear order/LCR, fresh ranges,
ordered merge, then normalization for the successful completeness
witness. Actual current LCR/general-instantiation definitions and
flat AC procedures were read before making their bridges. The old
core's combination proof boundary is frozen; root may replace or
route it only when integrating these fragments.

Primary dependence acquired from the author's openly linked manuscript:
`https://lat.inf.tu-dresden.de/research/papers/1998/BaaderSchulz-TCS-98.pdf`.
Held `source/references/p12-equational-unification/baader-schulz-1998-author-tcs.pdf`;
SHA-256 `69CBC9B48CC013212D90A2C739A0B6DB5946A79A8A18C0310BD96478F0E7F1DB`.
It has62 physical pages, internally numbered1-62. Actual contiguous
reading is pp26-44, including full §§4.2-4.5 and5.1; p44 also contains
the beginning of5.2. Source pages29 and43 were rendered and directly
visually inspected. No whole-paper or publisher-layout comparison
claim is made. The source fibering construction uses stabilizers,
extended quasi-free component structures, singleton/pair fibres,
transported operations and an ordering by fibering; its completeness
uses its Lemma3.30. Those are not silently asserted as proved by the
new equational tower, and that broader quasi-free primary is not
substituted for the chapter's exact1992/1996 ordered-completion route.

The new full proof route is explicitly editorial and equational.
Its free-product construction takes F_i(S), adds nongenerator classes
by colour, uses conservative free-algebra inclusions and finite birth
ranks, and transports each component reduct onto one carrier.
Injectivity is proved by generator retraction; an old nongenerator
cannot become a new generator because two retractions would identify
two distinct old generators. Universal-property existence and
uniqueness are then established by finite-rank induction, including
nonregular and collapsing identities. No minimum-support lemma,
ground representative, root-preservation premise or desired
normalization result is inserted as an assumption.
For the ground-only abstraction boundary, a ground term, when one
exists, supplies a retraction to the ground term quotient; when no
ground terms exist an empty atom list permits no equation. This
reflection case is supplied explicitly rather than assuming that
the empty-generated free algebra always exists as a nonempty algebra.

Seven full reciprocal proof pairs are supplied:

| Body result | Annex | Actual content |
| --- | --- | --- |
| `thm:p12-comb-purification` | `annex:p12.comb.purification` | Alien abstraction/definitions, variable identification, target extension/restriction and original-scope reconstruction; polynomial finite-node implementation. |
| `thm:p12-comb-soundness` | `annex:p12.comb.soundness` | Fresh-range equivalence, strictly earlier foreign dependencies, terminating actual merge, local-instance equality and all-block soundness. |
| `thm:p12-comb-free-product` | `annex:p12.comb.free-product` | Actual stage construction, generator/non-generator conservativity, limit carrier/bijections, finite representatives, model and free universal property, equality reflection. |
| `thm:p12-comb-projection` | `annex:p12.comb.projection` | Arbitrary-target partition, colour labels after true equality, birth-rank order, injective local abstraction, every local equation and LCR restriction. |
| `thm:p12-comb-completeness` | `annex:p12.comb.completeness` | Local factors evaluated in the proved combined algebra, one actual finite global factor, shared-order induction, identification/reconstruction and finite complete families. |
| `thm:p12-comb-decision` | `annex:p12.comb.decision` | Finite branch algorithm and component termination hypotheses, fixed-finite-theory NP certificate argument, finite-set generation, syntactic-MGU LCR bridge, general free-symbol extension and exact coverage tests by target-parameter freezing for effective finite minimalization. |
| `thm:p12-comb-ac-lcr` | `annex:p12.comb.ac-lcr` | Constant-multiplicity persistence, complete finite filtering of the supplied pure-AC algorithm, actual nested/multiple-AC plus free-symbol construction with no unit or empty image. |

The source cyclic example is retained: individual f/g solutions,
labels, the necessary x=z identification, then both incompatible
orders. The exact original normalized-solution/root/strict-subterm
choices and its ordered-completion/layer-reduced alternatives are
retained in a separate method with the source's sketch boundary.
Source applications, nondisjoint distributivity failure examples
(with their with-constants scope), collapse-free/regular definitions,
older constant-elimination interfaces and the ACUI/polynomial
optimization qualifications are retained as source-reported claims,
without inventing their missing proofs. A successful nested-AC merge
is worked explicitly. Collapsing
f(g(z))=g(z) and variable-independent h(x)=h(y) with no ground
terms test the proof's real boundary. An AG counterexample
x+c=y, ordinary answer x=p,y=p+c, order y<c<x and instance p=-c
shows why the positive-AC filtering argument cannot be imported to
signed counts. Unconstrained owner representatives absent from their
labelled block (n>2) and original representatives disappearing after
variable-equation elimination are retained explicitly by tautologies,
so coverage does not silently shrink its variable scope.

The general finite nested/multiple-AC/free-symbol algorithmic gap from
block5 is now addressed by a full AC-LCR bridge and the actual ordered
combination proof. This is not credit for Stickel1975's distinct
recursive-reconciliation/lesser-complexity algorithm or the unread1981
journal body. Those exact-version/presentation obligations remain.

Access checks for the original completion presentation were bounded:
the openly indexed1991 DFKI institutional PDF returned a managed
anti-bot challenge to direct retrieval (browser reported oversize);
no challenge execution/security bypass or retained report resulted.
The exact author-linked FTP file
`ftp://ftp.cis.uni-muenchen.de/pub/kepser/ccl/Combination.ps.Z`
failed host resolution, with no retained file. The1996 journal DOI
`10.1006/jsco.1996.0009` was unavailable through browser retrieval.
Metadata and abstracts are not counted as body reading. Its ordered-
completion route, the1992/1995a exact manifestations and the complete
1998 quasi-free presentation remain unclosed source-preservation
dependencies, even though chapter Proposition6.1/Theorems6.2-6.3 now
have independent full equational proofs in the new fragments.

Still allocated: arbitrary-theory hereditary compatibility/occurrence-
history transports; other remaining §3 logical and §5 monoidal exact
constructions/proofs, including signed LCR rather than the invalid
AC filter; §6 optimization/complexity/disunification qualifications;
unread whole-chapter portions; publisher layout and alternate88-page
manifestation comparisons. No source/whole-allocation completion,
admission or independent-review status is asserted. No children,
reviews, builds, manuscript renders, prose tests, shared/canonical or
queue edits were performed. Only primary source pages were rendered.

## Seventh block: author-side AC and combination manuscript adoption (18:44 UTC onward)

The complete current core body and core annex were read in bounded
chunks, including root's already adopted hereditary body input. All
four released AC/combination fragments were read completely before
placement. Exact destinations were resolved as absent before creation.
Copies were created using apply_patch, preserving the released originals:

- `handbook/parts/p12/presentations/n-c-035-05-ac.tex` from
  `spec/fragments/p12-equational-ac-body.tex`;
- `handbook/annex/p12/n-c-035-05-ac.tex` from the matching six-item annex;
- `handbook/parts/p12/presentations/n-c-035-05-combination.tex` from
  `spec/fragments/p12-equational-combination-body.tex`;
- `handbook/annex/p12/n-c-035-05-combination.tex` from the matching
  seven-item annex.

The owned parent `handbook/parts/p12/presentations/n-c-035-05.tex`
now inputs AC immediately after the AC-versus-ACU boundary and before
the semiring bridge. It inputs combination after the semiring criterion
and before the final method/source boundary. Thus the original-variable
preorder, LCR interface, source syntactic helper and pure-AC algorithm
are declared before the combination treatment uses them. Root's
existing hereditary input remains unchanged in its previous location.
The parent opening now accurately identifies its actual §§3-6 source
scope, not only §§3 and5.

Two active boundary passages were repaired coherently: the parent's
`def:p12-eu-ac-not-acu`/`def:p12-eu-method-boundaries`, and the adopted
AC body's `def:p12-ac-general-boundary`. They state that the actual
independent AC-LCR/ordered-combination route supplies finite complete
families for finite arbitrary nested/multiple AC symbols and free
symbols/constants, with effective minimalization under the declared
terminating local-algorithm hypotheses. They do not claim that a flat
matrix proof alone treats alien terms. Historical Stickel recursive
reconciliation/1981 and 1992/1996 completion/layer-reduction duties,
arbitrary-theory hereditary transport, signed LCR, other monoidal
presentations and whole-chapter/version gaps remain explicit.
The parent's hereditary reference uses the actual adopted label
`sec:p12-eu-hereditary-source`, not a guessed subsection label.

The AC annex, combination body and combination annex have hashes
identical to their released source fragments. The adopted AC body
differs only in its final source boundary, now pointing to the actually
supplied independent route. All six AC and seven combination result/
annex identities and full proof text are retained. The four original
spec/fragments files remain byte-for-byte unchanged.

Root still owns routing the annex driver with
`\input{annex/p12/n-c-035-05-ac}` and
`\input{annex/p12/n-c-035-05-combination}` in that dependency order,
as well as merging the existing unique AC/combination bibliography
and symbol intakes into canonical data. No shared driver, canonical
registry/bibliography, generated file, baseline/queue, existing core
annex, hereditary packet or released source fragment was edited.
No new source reading was claimed. File-digest observations verify
copy fidelity only; no tests, builds, renders, independent reviews,
source admission or full-allocation completion were performed.

## Eighth block: source B/N trace and composite-MGU dependencies (19:06 UTC onward)

This block owns only new `spec/fragments/p12-equational-narrowing-body.tex`
and `spec/fragments/p12-equational-narrowing-annex.tex`, unique
`handbook/bib/intake-p12-equational-narrowing.bib` and
`handbook/registry/symbols-intake-p12-equational-narrowing.csv`, and this
single note. Adopted core/AC/combination/hereditary bodies and annexes,
earlier intakes, canonical/shared files and source manifest were not
edited. Root was merging released intakes concurrently; those changes
were preserved.

The current core's actual B/N state, narrowing-domain and answer claims,
entire registered rule sheet, relevant B/N annex proof, and hereditary
proof boundary were read. Exact source rereading covered extraction
lines1991-2094 (the complete inherited LP restrictions and reduced/basic
definitions, printed488-490) and2241-2487 (complete §§4.3.1-4.3.2 and
4.4.1, printed495-499, plus surrounding text and the beginning of4.4.2).
Retained source pixels496 and499 were directly inspected; no new image
or manuscript rendering was performed. The reading confirms that
raw B refers back to G's LP restrictions without restating the
identity selector, whereas composite Narrow explicitly uses forward
l->r from R. These variants remain separate.

The named new scope **P12 narrowing transport fragments** contains six
full reciprocal editorial proof pairs:

| Body result | Annex | Supplied dependency |
| --- | --- | --- |
| `thm:p12-en-state-invariant` | `annex:p12.en.state-invariant` | Reachable six-rule solved/domain invariants, exact source-order accumulator A*delta, global literal-S factor even when an initial variable disappears, and P*A=P for ordinary N. |
| `thm:p12-en-trace-transport` | `annex:p12.en.trace-transport` | Actual every-rule B->N compilation P_N=P_B*sigma_S, equation occurrence multiplicity, same constraints/bindings, LP roots/freshness/mandatory first decomposition and identical terminal answer. Optional bare N-Constrain is proved equivalent on all reachable primitive N states. |
| `thm:p12-en-mgu-blocks` | `annex:p12.en.mgu-blocks` | Actual terminating source U run on the selected literal match, S*eta union[eta], sigma_new=A*eta globally, both directions of local literal-condition equivalence, factor equality and backward equation soundness. Source C-set duplicates differ only by solved literal identities/Trivial; C-empty intended composite boundaries agree exactly. |
| `thm:p12-en-actual-lift` | `annex:p12.en.actual-lift` | Chosen innermost forward redex at a real nonvariable skeleton address, fresh normal gamma, computed eta and explicit rho' factor, exact instantiated reduct/descent and its transported N block. Premise is an actual specified-signature reduced ground witness, not a newly assumed global completeness conclusion. |
| `thm:p12-en-terminal-normalization` | `annex:p12.en.terminal-normalization` | Actual finite image reductions, ordinary-rule variable preservation, normalized idempotence and identical equational coverage; distinct from active literal-S normalization. |
| `thm:p12-en-infinite-search` | `annex:p12.en.infinite-search` | R={f(s(x))->f(x),f(0)->a}: full termination and confluence proof, concrete composite B/N states/MGUs/answers y=s^k(0), a legal infinite branch in fresh replacement skeletons, and a proved infinite minimal complete family on the initial scope. |

These supply genuinely omitted source components: Corollary4.14's
"same sequence" now has an exact state/position proof for the original
six rules, without any new convergence restriction, and §4.4.1's
suppressed matching steps now have actual helper computations and
global factorization. They are not a repetition of the existing
stronger-convergence universal narrowing proof and are not credited
as a universal completeness theorem from weaker premises.
The arbitrary-trace compiler preserves the given scheduling of the
matching-first obligation: it transports operations elsewhere before
that Decomposition if the source trace delays it, rather than inserting
an earlier Decomposition and falsely claiming identical checkpoint
states. Immediate matching decomposition is used only for the actual
source composite blocks that choose it.

Precise unclosed dependency: the source Theorem4.13 proof begins by
grounding/reducing an arbitrary target. To read "ground convergent"
as only convergence of the original signature's closed terms, one
would need a lemma that this grounding preserves common normal forms
and protected-position lifting for all parameter witnesses. That
lemma was not supplied: the core's existing fresh-constant peak
counterexample refutes the directed unrestricted conclusion under
that weak reading. The tested ordinary-to-basic reversal also fails
locally when an ordinary step is inside an inserted solved image;
the concrete h(x)/g(a) compiler example exhibits the missing basic
address. Attempting to replace literal active solved bindings by
E-equal normal forms does not preserve the old literal witness;
the new reachable x=f(a),z=f(a) state exhibits that failure.
Terminal-only normalization is the valid separately proved operation.

For the raw inverse-identity interpretation of B, the weak-domain
counterexample is not treated as a disproof of that different tree.
The newly supplied actual basic inverse branch for that problem uses
g(v)=f(v,v), then f(p,q)=a, both at protected skeleton roots;
the matching equations first decompose and yield only fresh bindings
v=x,p=x,q=x. It returns identity on the original x. The ordinary
compiler supplies the same answer only in that same inverse family,
not in forward-only Narrow. Thus the direction distinction has an
actual successful source-state construction, not just an assertion.
The inverse variant's universal argument would still require actual normalization and
occurrence-history/critical-simulation transports, not the newly
proved one-way state compiler. Fay's distinct historical body,
arbitrary-theory hereditary refinements, other §3/§5/§6 whole-source
and version obligations remain allocated. This block neither waived
them nor promoted the source's sketch/general statement by repetition.

No children, independent reviews, tests, builds, manuscript renders,
shared/canonical edits or admission/whole-allocation completion claims
were made. The bibliography intake contains only explanatory comments
because the established BaaderSnyder2001 key suffices; no unread primary
is cited as though its body had been consulted.

Release artifact digests for this block (SHA-256):

- narrowing body: `702228561758591B0DF9CB7E0F3ACBA2D5E70FDBB78191387F8C1180B9748004`;
- narrowing annex: `1A29A65D8AC813C4052F3F581EBE9B9C8245693BBE3540BDDAFDEA4187C9B5AF`;
- narrowing bibliography intake: `088102F2AE0451FA6BFC3A1E3813828E1E8E57146D742CE78F74340F4236393F`;
- narrowing symbol intake: `8C0083376154F5902993D8ABC276B0B992C3B8ABEDC5571FCF6018B0AFE3906D`.

The fragments are released for root's inspection/integration; they are
not adopted manuscript files or source-admission records. No further
block is started by the author after this release.

## Ninth block: author-side narrowing manuscript adoption (20:00 UTC onward)

The latest complete parent body was read in three bounded portions.
Both frozen narrowing fragments were read completely and their exact
new manuscript destinations were resolved as absent before creation.
Using apply_patch, the complete body was copied to
`handbook/parts/p12/presentations/n-c-035-05-narrowing.tex`, and its
complete six-item proof annex to
`handbook/annex/p12/n-c-035-05-narrowing.tex`. Both originals under
spec/fragments remain byte-for-byte unchanged.

The owned parent `handbook/parts/p12/presentations/n-c-035-05.tex`
inputs the new narrowing body after its B/N standing/theorem and the
ground-domain/basic-skeleton examples, and before the strategy/refinement
material. Thus the actual six rules, removing-binding U helper,
composition convention, comparison scope, domain qualification and
counterexample used by the packet precede it. A source-appropriate
strategy subsection heading follows the packet, separating its primitive
reachable-state invariant from the later additional operations.
Existing hereditary/AC/combination inputs were preserved.

Only directly affected parent passages changed: the directed weak-domain
counterexample now points to the actual same-family inverse-basic
identity trace; the composite-rule paragraph points to concrete helper,
accumulator, factor and chosen-redex proofs; and the final methods
boundary points to the exact Corollary4.14 transport, preserved matching-
first scheduling, terminal-only normalization and infinite minimal
family. The weak original-ground directed universal claim remains
refuted rather than promoted. Source grounding and inverse-basic
normalization/path-history dependencies remain explicitly open in
`def:p12-en-completeness-boundary`. No hypothesis of the existing
`thm:p12-eu-bn-completeness` was changed.

All six reciprocal result/annex pairs and all source direction,
optional Constrain, constraint-context and scheduling variants are
retained. The adopted narrowing body and annex are exact copies of
the released fragments, not shortened summaries or substituted proofs.
Root owns adding `\input{annex/p12/n-c-035-05-narrowing}` to the
shared annex driver and canonical intake reconciliation. No shared
driver, canonical data, baseline/new snapshot, existing core annex,
other adopted packet, prior source fragment or other contributor's
edit was altered. No tests, reviews, builds, renders, new source-reading
claims or admission/full-allocation completion claims were made.

## Tenth block: original term/convergence scope and inverse-basic progress (20:27 UTC onward)

Only new `spec/fragments/p12-equational-basic-completeness-body.tex`
and matching annex, uniquely suffixed basic-completeness intakes,
and this existing note were edited. All adopted/released earlier
packets, intakes, shared/canonical files and source manifest remained
frozen and untouched.

The earlier held unification chapter's complete text-extraction extent
was actually read contiguously through lines1-1047: front matter and
§§1-2, printed445-469. Its graph illustrations were not newly rendered
or compared to the PDF pixels. Source§2.1 pp451-452 permits T(F,V), finite
or countable F, infinite V, and finite-support simultaneous substitutions;
it does not restrict targets to ground substitutions or declare an
infinite stock of free nullary symbols. Source§3.1 and its open-term/
comparison definitions were reread at lines1048-1252, printed469-473.
Combined with the previous actual contiguous §3-6 reading, the
cumulative text-read extent is now lines1-3351/§§1-6. Section7,
bibliography/index completion and manifestation comparisons are not
claimed; this is not whole-chapter reading or treatment completion.

The source explicitly imports the rewriting chapter's terminology at
p488. The held Dershowitz--Plaisted author chapter was read at complete
printed pages540-544,546-547,560-561 (physical6-10,12-13,26-27).
Its p542 contextual rewrite definition includes every substitution
instance, with no unequal-endpoint filter. Derivations at p543 do
not exclude equal-endpoint steps. Reduction Ordering Def4.5 p547
is well founded, monotone and fully invariant over the open term
domain. Ground Confluence Def5.5 p560 explicitly restricts confluence
to variable-free terms; Convergence Def5.6 p561 is termination plus
confluence of the whole relation. No implicit free-constant reserve
or automatic ground-confluence extension was found in these definitions.
An earlier broad filtered extraction exceeded its output bound;
only the selected complete pages subsequently read are counted.
No render or pixel-generation call was made in this block.

The new named scope **P12 original-scope basic completeness dependencies**
contains five full reciprocal editorial pairs:

| Body result | Annex | Supplied dependency |
| --- | --- | --- |
| `thm:p12-eb-ground-termination` | `annex:p12.eb.ground-termination` | One original ground term plus ground termination implies open termination under the actual unfiltered rewrite relation, including stutters. A termwise all-variable map is realized by finite restrictions for every step, even across infinitely many variable names. No infinite-support source substitution or new constants are smuggled in. |
| `thm:p12-eb-initial-normalization` | `annex:p12.eb.initial-normalization` | Source reduction ordering yields open termination, nonvariable left sides and no right-only variables. Finite initial open image normalization preserves all E-solutions pointwise, before any active S exists; no idempotence or unique open normal forms assumed. |
| `thm:p12-eb-open-history-lift` | `annex:p12.eb.open-history-lift` | Literal C steps retain the normal open witness; actual innermost forward match at eligible skeleton address gives normal fresh images, computed-U eta, explicit global factor, actual reduct/descent and original/template-versus-inserted-image marks. No global progress conclusion is asserted. |
| `thm:p12-eb-inverse-expansion` | `annex:p12.eb.inverse-expansion` | Given a genuinely eligible inverse match at a normal witness value, construct normal matched images and normal fresh right-only parameters, computed U factor and marked expanded template; prove that this block increases rather than decreases source M. |
| `thm:p12-eb-progress-countercase` | `annex:p12.eb.progress-countercase` | New left-linear, regular R={f(x)->g(x),f(g(x))->g(x),g(a)->a}, explicit ground-total reduction ordering, open termination and original ground confluence, distinct E-equal open normal endpoints, unique normal representative of identity's y-image, and actual successful raw inverse-basic trace with normal witnesses and complete singleton answer for that problem. |

The parent-suggested ground-termination lemma is verified at the printed
definitions. A hypothetical infinite open run is mapped termwise to one
original ground term. Each mapped step is a legal finite-substitution
instance. When endpoints coincide the step is retained, as the source
requires, so the run still contradicts ground termination. If there
is no original ground term, source R contained in a reduction ordering
already supplies open termination independently. The fragment includes
counterconventions/cases showing why deleting stutters or omitting
the ground-term existence guard changes that general lemma.

Consequential correction to the earlier residual description:
**initial finite-image normalization is now supplied at the original
open term/ordering scope and is not the outstanding step.** It can
be done before S exists without grounding or normalizing active
literal bindings. What remains is global progress/basic conversion
and inverse protected-history transport from R-equal but different
open normal endpoints. Grounding to one existing term proves only
termination; it is noninjective and cannot reflect generic equality
or recover parameter-level coverage. New constants would require a
separate confluence statement at the grounding vocabulary.

The new countercase removes nonlinearity, irregularity and dependence
on the old directed-only example. Its original closed terms all
normalize to a. But g(g(y)) and g(y) are distinct open R-normal
endpoints and are equal through the peak f(g(y)). Every R-normal
image E-equal to the identity's y-image is y itself, so an alternate
normalization choice cannot produce a forward redex. The raw B
inverse branch uses fresh g(v)=f(v) at the left root, then forward
f(g(w))->g(w), matching-first Decomposition each time, and returns
S={v=g(y),w=y}; its answer fixes original y. Fresh images g(y),y
are normal and every rewrite uses a genuine marked skeleton address.
The first block replaces g(g(y)) by the strictly greater f(g(y)),
so the source descending-M induction does not justify that inverse
strategy. Adding fresh c exposes the unjoined peak g(g(c))/g(c).

This is a countercase to exhaustion/descent of the source proof at
the literal fixed-signature ground-convergence reading, not a
counterexample to raw inverse-basic completeness itself. The actual
successful inverse branch prevents that incorrect transfer. The
next substantive action is a global finite equational-conversion/
basic-history construction permitting such inverse increases, or
primary evidence establishing an explicitly different source
convergence domain. The unchanged stronger-open-convergence proof
was not repeated or credited as this original-scope result. All
other chapter/source/version allocations remain owed.

No children, reviews, tests, builds, renders, source substitution,
shared/adopted/canonical edits or admission/whole-allocation completion
claims were made. The new bib intake refers only to the established
two source keys and does not mutate earlier/canonical entries.

## Eleventh block: original-scope five-proof manuscript adoption (21:31 UTC onward)

The latest complete parent and complete prerequisite narrowing
transport body were read, followed by both frozen original-scope
fragments in full. Exact target destinations were absent before
creation. Using apply_patch, full copies were created at
`handbook/parts/p12/presentations/n-c-035-05-basic-completeness.tex`
and `handbook/annex/p12/n-c-035-05-basic-completeness.tex`.
The parent inputs this new body immediately after the narrowing
package and before its strategy subsection. Thus the source state,
composition, actual helper, matched-block and basic-address interfaces
precede their use. All five reciprocal pairs and their complete
proof text, convergence distinctions and actual countercase are
preserved; the spec/fragments originals are unchanged.

Only directly obsolete normalization boundaries changed. The parent
narrowing standing/final methods boundary now distinguishes initial
open image normalization, supplied under the source ordering, from
the stronger common-normal-form/progress domain used by the existing
directed theorem. The adopted narrowing transport body's
`def:p12-en-completeness-boundary` now states that initial normalized
open witnesses and open termination need no new-constant reserve.
It retains the genuinely unclosed global raw inverse conversion,
protected history and progress argument for E-equal different open
normal endpoints. The successful countercase is not relabelled a
disproof of raw inverse-basic completeness. No universal theorem,
earlier proof status or convergence hypothesis was upgraded.

The adopted five-result body and annex are byte-identical to their
released fragments. The older six-proof narrowing annex and all
six result statements/proof text were not edited. Only its adopted
body's directly superseded initial-normalization boundary changed.
All other hereditary/AC/combination packets, earlier intakes,
source fragments, shared drivers, canonical data and baseline/new
snapshots were preserved. Root owns routing
`\input{annex/p12/n-c-035-05-basic-completeness}` and canonical
intake reconciliation. No tests, reviews, builds, renders, new source-
reading claims or admission/whole-allocation completion were made.

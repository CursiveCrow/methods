# P16 Jin Tian conditional identification: author return

Date: 8 September 2026 UTC. Block began 15:09:26 UTC; deadline
15:54:26 UTC. The assigned manuscript, intake and capture paths were
absent at intake. Only the new owned outputs and primary-reading
intermediates were created. No independent review, manuscript verification
scanner, test, build, acceptance check or manuscript render was run.

## Complete written extent

| File | Extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p16/tian-conditional-identification.tex` | 322 lines; original four phases, eleven results, source examples and corrected comparison | `26A2A34E807B4508F79366CEB63239B7B33F8A2FA03E4FB78C75DB655A442D5E` |
| `handbook/annex/p16/tian-conditional-identification.tex` | 496 lines; eleven complete proofs in body order | `AE44A25C04E85AEEC72ED64FBCBFB7F06C99953FBB658FDAD788DC235F2BE429` |
| `handbook/bib/intake-p16-tian-conditional-uai2004.bib` | 11 lines; original primary entry | `0C301404ADFCC5B31590D849527A0045D8D46BA0EFAF519C9A0E2BFF6557E94E` |

The complete actual body and annex were read back mathematically, including
all final corrections. The eleven reciprocal suffixes use body prefix
`thm:p16-` and annex prefix `annex:p16.`: `tcc-stochastic-bridge`,
`tcc-component-interface`, `tcc-quick-criteria`, `tcc-closure`,
`tcc-cancellation-soundness`, `tcc-complexity`, `tcc-moral-bridge`,
`tcc-idc-bridge`, `tcc-completeness`, `tcc-original-examples`, and
`tcc-corrected-comparison`. Counts and hashes are handoff identifiers.

## Verified original primary

Capture:
`source/references/jin-tian-conditional-causal-effects-uai2004/tian-uai-2004.pdf`.
It is 117,018 bytes, eight complete readable pages, SHA256
`332E38EA419D8714F5A54EA5F1A9A20D6CC39770EB6D3AC42F1F50ECBCD0A7E1`.

The actual first page names **Jin Tian**, not Jie Tian, and the exact title
**Identifying Conditional Causal Effects**, with Iowa State affiliation.
The author's research page links this exact PDF as his UAI 2004 paper:
<https://faculty.sites.iastate.edu/jtian/research>.
Download URL:
<https://faculty.sites.iastate.edu/jtian/files/inline-files/uai-04.pdf>.
The official conference program independently lists the same title and
author: <https://www.auai.org/uai2004/PosterSessions.htm>.
The proceedings page range 561-568 is recorded in the bibliographic
proceedings index <https://dblp.org/db/conf/uai/uai2004>.

The captured body is not date-stamped or numbered as a publisher facsimile;
its year/venue are verified through the author's linked publication record
and conference program. PDF metadata supplies only GNU Ghostscript 7.05 as
producer and no date. No creation/publication date was invented from file
timestamps. The later arXiv deposit 1207.4161 was identified as a distinct
record and was not substituted for this author-hosted version.

The initial default scoped write/TLS request failed; an escalated download
limited to the exact capture path succeeded. All eight source pages were
read as full extracted text and primary page images. The two source graph
figures were additionally read at higher resolution to preserve every edge.
Primary-reading images are in the old task's `tmp/pdfs/p16-tian2004-source/`.
Research and PDF skills guided this acquisition and reading.

The complete held 2007 addendum was reread as text:
`source/references/shpitser-pearl-conditional-identification-uai2006/r329-appendum-2007.pdf`,
SHA256 `16149F70F492FF7292F4E916B781112B1D2BBF621F053B6B17658CE2AB4EE8BC`.
Its complete page images had been read in the preceding IDC author block.
Its existing key is `Shpitser2007ConditionalIdentificationAppendum`.
The new intake key is `Tian2004ConditionalCausalEffects`.

## Exact original procedure retained

Tian's source letters T/S/C are retained as action/response/conditioning
sets. Definition 1 of the original paper explicitly assumes positive
observed distributions. The manuscript states the finite independent-input
model domain and all positive graph-uniform quantifiers. A private finite
response-table construction proves the stochastic-row/total-equation bridge
for this domain; no arbitrary latent projection or independence conversion
is assumed for a different hidden-variable model class.

The component subroutine is written on the connected component-call domain
used by every call in the conditional algorithm. All three branches and
the exact inclusions B subset H-prime subset A proper-subset H are explicit.
The source's 2004 use of “unidentifiable” to mean failure of that procedure
is explained historically, without attributing later completeness to 2004.

All four original phases are supplied: full Q decomposition; component
identification into failed/successful families; least closure through
marginalized variables; and conditional cancellation. Source Eqs. (28)-(30)
are proved as a product of two finite sums. The unknown common factor is
independent of responses, is positive, and cancels from the conditional.
Every computed denominator is positive. The polynomial bound is explicitly
for graph decisions and shared symbolic construction, not expanded tables
or unbounded-precision numerical arithmetic.

## The correction and full IDC bridge

The source explicitly defines Pa(B) to include B itself and its proper
parents. The body prints Pa-plus to keep that role distinct from the
handbook's proper-parent notation. This is the notation whose misreading
caused the later UAI comparison error.

The completeness bridge is fully proved:

1. A factor-scope incidence graph has district factor vertices and the
   unconditioned variable vertices S union F; inclusive scopes determine
   its edges. Phase 3 is exactly reachability from the failed factors
   through F, and Phase 4 fails iff a failed factor connects to S.
2. Each district's latent parents, retained outputs and external observed
   parents form a connected block in the ancestral moral graph after C
   is deleted. Conditioned outputs connect their co-parents by marriage.
   Private formal roots cover singleton blocks without changing observed
   separation. Every moral edge lies in such a block, proving the exact
   incidence/moral connectivity equivalence.
3. IDC eligibility is therefore equivalent to a conditioning vertex's
   district lying outside the response-connected factor family R. The
   maximal exchange set is C minus D_R. The terminal joint ancestor set
   is exactly D_R, proved by both ancestral closure and directed routes
   to the first response/conditioning target. Its districts are precisely R.
4. The same original component calls determine the terminal joint factors.
   Thus Tian fails iff a failed original factor belongs to R, exactly IDC's
   terminal failure. IDC completeness gives necessity, while Tian's own
   cancellation proof independently gives success soundness.

This retains the addendum's closure idea and supplies all its graph bridges
without assuming that other multi-vertex districts can be treated as single
observed variables. IDC is not substituted for Tian's distinct procedure.

## Original examples and corrected comparison

The full Figure 2 examples are reconstructed: P_x(Y given W) cancels its
unknown W factor, while adding B to the conditioning set brings the failed
A,Y district into the response scope. Every component call and partition
is supplied. The full Figure 4 four-phase example is also reconstructed,
including the Q[W,Y] marginal, failed A factor, empty closure and final
conditional expression. Coordinate-sum operators prevent inner dummy action
or evidence coordinates from capturing outer assigned values.

For the UAI comparison graph W -> Y -> Z, X -> Z, X <-> Z, the corrected
calculation has failed Z factor, F0={Y}, and moves the Y factor because
Pa-plus({Y})={W,Y}. Its scope reaches response W, so Phase 4 FAILS. Explicit
positive models with the same sixteen-cell observed law give conditional
response probabilities 1/2 in the first model and 3/8 or 5/8 in the second,
with conditioning masses 1/2. This confirms the corrected decision and
does not repeat the withdrawn unsoundness assertion.

## Integration and remaining boundaries

Input both files after their `conditional-interventional-identification.tex`
counterparts and merge the one bibliography intake. Root owns all shared
drivers, canonical notation and later review. New roles include inclusive
Pa-plus, the source action/response/conditioning letters, the two factor
families and their least-closure partitions, cancellation factors U/K,
factor-scope incidence vertices, response-connected family R and D_R.

No soundness/completeness proof for this stated positive graph-uniform
conditional procedure remains pending. Additional nonpositive-support
claims, separately prescribed small alphabets and a broader latent-model
translation are not asserted by this component. They do not alter the
completed finite independent-input theorem or the corrected source comparison.

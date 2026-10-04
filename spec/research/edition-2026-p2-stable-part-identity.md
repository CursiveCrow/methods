# Edition 2026 P2: stable part identity compatibility

Implementation checkpoint: 7 September 2026, 13:38 UTC. Authority: the approved mapping in [EDITION-2026-CONTRACT.md](C:/Dev/the-methods-of-reason/spec/EDITION-2026-CONTRACT.md). This is an implementation and verification record, not independent acceptance or completion of the nineteen-part reorganization.

## Implemented changes

The approved order is P1–P10, P15–P19, P11–P14. Stable part IDs now have an explicit identity independent of the printed ordinal.

- [handbook.sty:397–459](C:/Dev/the-methods-of-reason/handbook/handbook.sty:397) defines the approved nineteen-ID/ordinal/title map and the driver-boundary interface.
- Every existing driver p01.tex through p14.tex declares its own stable ID on line 2, before its public part heading or source-heading route.
- [Status output at line 473](C:/Dev/the-methods-of-reason/handbook/handbook.sty:473) and [card output at line 1136](C:/Dev/the-methods-of-reason/handbook/handbook.sty:1136) serialize the explicit stable identity. Neither derives ownership from the printed part counter.
- [Annex plumbing at line 1705](C:/Dev/the-methods-of-reason/handbook/handbook.sty:1705) preserves stable chapter numbering and hyperlink identities while mapping its displayed part ordinal and title.
- [The one-book checker](C:/Dev/the-methods-of-reason/tools/check_compendium_volume_manifest.py:25) uses explicit stable-ID/title pairs in approved printed order, checks each driver's one preceding identity declaration, rejects unapproved IDs, and reports missing new parts as edition migration requirements.
- [Symbol validation](C:/Dev/the-methods-of-reason/tools/symbols2tex.py:40) and [review-shard validation](C:/Dev/the-methods-of-reason/tools/merge_section_review_shards.py:21), together with the matching schema pattern, accept precisely the approved P1–P19 IDs. The symbol global interval now covers P19; generated group headings identify a stable part explicitly.

### Driver and annex interface

The new public driver declaration is \\hbpartidentity{pNN}. It must occur before that driver's single public part heading. It validates the ID, sets \\hbcurrentpartid, and records the actual next printed ordinal for this construction run. The existing one-public-heading-per-driver contract remains essential.

The mapping queries are:

- \\hbpartordinal{pNN}: approved edition ordinal as an integer.
- \\hbparttitle{pNN}: approved title.
- \\hbpartdisplayordinal{pNN}: Roman numeral for the recorded current body position, or the approved position when no body declaration has run.

This preserves transition behavior. In the current fourteen-part construction, P11 is still printed XI, and its annex therefore says Part XI. Once the five new parts precede it, the same stable ID is printed XVI and its annex says Part XVI.

The existing two-argument \\hbannexchapter{stable-number}{legacy-title} call remains accepted. The second argument is retained for driver compatibility; the approved title map now controls the displayed title. Annex chapter numbers remain P1, P2, ..., P19, and hyperlink identities remain annex.1, annex.2, ..., annex.19. No body/annex label was renamed.

Symbol scope ranges remain ranges of stable IDs, not intervals of printed positions. Thus P10–P11 does not silently acquire P15–P19 when the book is reordered. No canonical symbol data or generated view was edited.

## Separately authorized C4 routing contribution

The root additionally requested exactly one [PA2 definition input at p02.tex:52](C:/Dev/the-methods-of-reason/handbook/parts/p02.tex:52), after scope-SRC-12356-12414 and before scope-SRC-12415-12536. That input is present once at the requested seam, and the root confirmed the routing. Its corresponding required position was added to the checker's existing exact P2 input sequence at [line 779](C:/Dev/the-methods-of-reason/tools/check_compendium_volume_manifest.py:779).

This is a C4 routing contribution, separate from P2 identity compatibility. The PA2 chapter file and its mathematical contents belong to the root and were not edited here. The exact restoration-input subsequence remains unchanged.

## Meaningful verification

### Python checks

Thirteen focused cases passed in one run: all seven existing section-review shard tests, plus six bounded compatibility cases. Those six checked:

1. All nineteen style entries agree with the checker map and approved contract titles/ordinals.
2. All fourteen current drivers have exactly their own preceding declaration; C4 occurs once at the exact seam.
3. Runtime/schema part patterns accept p01–p19 and reject p00, p20, p1, P15, p015 and p15x.
4. Actual queued-section validation accepts p15 and p19 and rejects p20.
5. Symbol parsing accepts the new IDs, rejects invalid IDs, admits global first-use P19.1, and detects a global/P19 glyph collision.
6. In-memory nineteen-part fixtures validate the approved order; a reordered p15/p11 pair, an unapproved p20 input and a wrong p15 declaration fail. These fixtures did not create future manuscript drivers or content.

Nine existing publication-record shape tests also passed, covering the single-book record, title/path restrictions, internal-authority exclusion, release status and required release evidence. No test framework was added.

The first combined run also exercised the three existing registered-notation route tests: two passed and the old adjacency expectation in test_registered_notation_wrapper_precedes_editorial_aggregator failed. Its expected immediate aggregator placement contradicts the pre-existing P12 source sequence. Removing only this task's new non-input boundary line restores the exact pre-task P12 bytes, so this failure was not introduced by P2. That unrelated test or route policy was not modified.

### Scoped TeX compilation

Internal fixtures were compiled with MiKTeX pdfTeX and package auto-installation disabled. They exercised the actual theorem-status writer, card serializer and annex machinery. The second identity run resolved first-pass cross-references.

Observed metadata:

    thm:p15-probe|proved|annex:p15.probe|p15
    thm:p11-probe|proved|annex:p11.probe|p11
    CARD|entry:p15-probe|p15|P15 probe
    CARD|entry:p11-probe|p11|P11 probe

Observed checks:

| Case | Result |
|---|---|
| P15 at printed XI | stable p15; approved ordinal 11 |
| P11 at printed XVI | stable p11; approved ordinal 16 |
| P15 annex | chapter P15; displayed Part XI; approved uncertainty title; anchor chapter.annex.15 |
| P11 annex after reordering | chapter P11; displayed Part XVI; Philosophy of Logic; anchor chapter.annex.11 |
| P11 in the current fourteen-part construction | body XI and annex Part XI, both stable p11 |
| Standalone P19 annex fallback | chapter P19; displayed Part XV; approved empirical-reasoning title |
| Invalid p20 declaration | compilation exits 1 with the explicit invalid-stable-ID error |
| Metadata emission without an identity | compilation exits 1 with the missing-stable-ID error |

Temporary fixture directory: C:/Users/Crow/AppData/Local/Temp/edition-p2-d8bf5004f293457ab1ec5a3254d95eb9. These are internal verification artifacts, not the public handbook PDF or publication acceptance. No rendered-page inspection or full-book build/render was performed.

### Current guard failures and attribution

The checker implementation before this task was reconstructed in memory by reversing only the bounded P2/C4 code changes. Its SHA256 exactly matched the recorded original value:

    77802C3430114EEB8C3A70B695CD96EBDCA1E929BC8C568EA1C4E31D8CF9CBEC

Evaluating that original implementation against the pre-task routing view produced twelve existing guard failures. The P2 implementation produced those same twelve failures plus exactly five explicit missing P15–P19 migration requirements. The comparison therefore isolated the intended new requirements from implementation regressions.

The twelve prior failures concern old exact route/seam guards in P2/P3/P4 and old source-byte/provenance expectations in P6/P7/P8. They were not repaired or suppressed. The older fourteen-part synthetic fixtures and live-zero-failure expectations in the one-book test module also need migration before that whole historical suite can be advertised as passing.

After this comparison, the root reported its independent C5 correction to inherited-07295-07468.tex, SHA256 1958b3363dcac80b5c7af56f446e74591b4249d23c1c8543cc9ec7de7bb93a89. Any newly resulting P3 provenance/source-byte failure belongs to that subsequent authorized correction; it must not be relabelled as one of the pre-task failures above.

## Preservation and unresolved migration steps

Removing only the fourteen new identity lines and the C4 input restores every current driver's exact pre-task bytes and SHA256, including its original LF or CRLF endings. All existing driver labels, source inputs and other dirty edits are preserved.

The owned-file whitespace check passes with Git's explicit cr-at-eol option.
The default check flags the carriage returns on the five added lines in the
already-CRLF drivers p09, p10, p11, p13 and p14; there is no added space or tab
at those line endings. Their original encoding convention was retained rather
than normalizing unrelated lines. The saved public main.pdf still has SHA256
ee4c5324c1aac7fc3b0e13fba816b35ec6f39be059e807b01695fe1a9900851f.

Remaining work belongs to later assignments:

- Write substantive P15–P19 content and drivers, each declaring its stable ID; then change main.tex to the approved order.
- Route new annex content and reconcile reader-facing prose/table references to printed part ordinals.
- Reconcile the separately recorded historical source/provenance guards without undoing accepted corrections.
- Update the relevant old full-book fixtures to the approved mapping and declarations.
- Regenerate admitted lookup surfaces and obtain full-book static/build/visual and independent review evidence.

No blank new part or chapter was added to pass a gate. main.tex, contract files, canonical bibliography/symbol CSV, generated views and author-owned chapter texts were not edited.

## Before/after file hashes

These identify the nineteen owned files changed by this block, including the separately recorded C4 routing contribution.

| File | Before SHA256 | After SHA256 |
|---|---|---|
| handbook/handbook.sty | BB4D4E18B039B68E6C156BD900EA8AE028815198F90926D1550D3BD1EACC9C0D | 1B5C089594010DD517389CDF510CDFBF741E014EAAC877CC5BB44F3991412288 |
| tools/check_compendium_volume_manifest.py | 77802C3430114EEB8C3A70B695CD96EBDCA1E929BC8C568EA1C4E31D8CF9CBEC | 8DD16AC7EFA3A7E1C58C6F7A6A7CFADEB9D40F2984401A4361A0030DBCEC37C7 |
| tools/symbols2tex.py | AADF720A3390A5524E87C561C8A1E37AF593D95C159BC24FA841C40C9EC870E5 | 1107FA18828213D26FC7221B3D51A384F27A8CF8C1B136FF6DD15A2076A614D5 |
| tools/merge_section_review_shards.py | 5E87B161C05580D65C9B50C391D865A7350E702F75DF29B228A1AFED3B3890B4 | 8026234C9CA2B58D190DA3B05FD9E1EFD96F19251B5EC476FA15988197955B25 |
| spec/provenance/section-review-shard.schema.json | F0E4A7C6440BD786AD20C47E5134717F532E64F0708B931F5260E03E99B8365E | 11EFA6422A9A74683F6380402A00E1EB6CF088FEAC39316AC01793109F1E3C3F |
| handbook/parts/p01.tex | F9E914C3582F835E0A3066DBF7D6003AC435C1BB07F7A0CE847C797AEE0F44EF | 576196661B4198D6DA891EC6A777DCE8C832D7CF9DF81D458079877D561A8650 |
| handbook/parts/p02.tex | F0083D69ED260951B95DF228B6FA108CF62DF048F4874DA2E08A6D386C9F923F | BF76EB346924365E7D06EB3596CF22B266D61EA6FF24096B6C527FD9F8151E0C |
| handbook/parts/p03.tex | EECDBBBF6431C43B36F15D2334E5486E954B7962DC5B437A372A04F5506B1A48 | 3694A5CDE0762B4CF489AA640AECA2F00B9216BF16FE4BFA2A43E0FD4583BA69 |
| handbook/parts/p04.tex | 9E1CD4671FA9E1A5D5D951305116D1F728591F689FB66B83C3DC47585F50312D | 19C6CB01DE3F19F24430EDBFE623F466C55DDEA50AF006864B6B1B8EC964A509 |
| handbook/parts/p05.tex | CD29B788CE9F89E94AC527E88C662C6C6DF0CD666DFBD3295D2BD8AF03D2C300 | 068B90E56BFCF4538AFF14F0DBBF428A228A34B12736CA55484B1E3D5E64B326 |
| handbook/parts/p06.tex | E0A11AC4EDD4BFFA86FEA36953A20E11CA56FF54BF4A5727B54B84FBE92E444A | 586423629382AABF0D804C56B6458D8E8AFAA1BADCE5DB81D7C39CF19613EA86 |
| handbook/parts/p07.tex | 475798B19232A7FAD3D28DE5237304258B69F5ACAFB31C252CD4C6B601C93469 | C3CBD4AFB174E51B042A9A6B5CBF374B33428A47E69A66440660159100EADD31 |
| handbook/parts/p08.tex | F15EC253AC615AC688A17FC868B22932469D5FAD26D92C4F4D5443F26715786D | 18A9D459D89930DD02EC3E337ACB806E4A1EB307938E4CC4E699D42428B0AF27 |
| handbook/parts/p09.tex | A414F249CB2D46013D902176D09BBD11A176551775929F2837D62DAB4FC3B0D1 | 625DF74E50F822162949AA0B6E2826353FF7A520BD95002A5714AE8885A960BF |
| handbook/parts/p10.tex | BE19CCBE6FA0A3F89B8F36FEEFB8FBA24F714C1DA013F04E63C048D9C71157F2 | 640A1FA9E7932D81921EAB1E27FF767E39B676E1B8B3A22591E2FEBA4710AD8F |
| handbook/parts/p11.tex | C817EA468D980C30AB4EF17732588BD83326D7F06BDF1892CFD622281B6640F6 | 0E6B43B67D7FF31D548329CA337712A3A92D4B486ADE41861033163A4B82C15F |
| handbook/parts/p12.tex | A1DA5246AB90CCF1362F97FAFD1434771A9086DBF7C3B59A8E361ED5C2C35262 | 8CCFF3944DEDEFF8D6FFBEF93E5972A6BCE551F165C2F7EE2F535A2753BEE105 |
| handbook/parts/p13.tex | 2289CB177CE8AED8E4B8C3E73604BA80E5E5A70DE628F4EA4A6C12476A10968D | DF74F68133761521D8A4778C4E4DC56CCF46120402E1574C5B11907BF5C28CF7 |
| handbook/parts/p14.tex | 72098C2E2574DF676CFA21C0FC106AE7884BC85A81B2AA0012539EF2084E9DB4 | BFBD748160B1C751A50255C22B376476DB15F7297CCC4A5074FCBC7AE8A32D01 |

The note records author verification only. It does not assert source/text acceptance, packet admission, section lock or release readiness.

# Independent source evidence for the ten governed restorations

Date: 2026-08-13

## Scope and result

This is an independent, read-only audit of these ten provenance records against the frozen authority `source/formal-logic-reference.tex` and the live handbook files:

- `PRE-00035-00037`
- `PRE-00039-00047`
- `SRC-00171-00197`
- `SRC-00198-00234`
- `SRC-00235-00293`
- `SRC-00294-00320`
- `SRC-00321-00362`
- `SRC-00363-00372`
- `SRC-00373-00405`
- `SRC-09099-09111`

Overall audited-record result: **PASS: 10; FAIL: 0**.

The result separates as follows:

- frozen-authority file and corpus-manifest agreement: **PASS: 1; FAIL: 0**;
- record-level authority, source-locator, interval-hash, artifact-hash, physical-line, and normalized content-token checks: **PASS: 10; FAIL: 0**;
- exact wrapper-shape checks: **PASS: 10; FAIL: 0**;
- single-input reachability and recorded-destination checks: **PASS: 10; FAIL: 0**;
- nonempty recorded stable-label checks: **PASS: 8; FAIL: 0; not applicable: 2**;
- additional labels explicitly discussed by the records for `SRC-00321-00362` and `SRC-00363-00372`: **PASS: 3; FAIL: 0**;
- secondary existing-checker cross-check: **PASS: 10; FAIL: 0**.

## Independent method

The existing restoration checker was not used to obtain the primary results. The primary audit performed the following operations directly:

1. Read the frozen authority and every artifact and wrapper as raw bytes; calculate SHA-256 independently.
2. Decode the bytes as strict UTF-8, count physical CRLF, LF, and CR endings, and verify terminal line endings.
3. Select each inclusive source interval by its one-based physical line numbers and hash its raw bytes.
4. Normalize each terminal CRLF, LF, or CR to one LF byte, preserving physical-line order and every other byte; compare the normalized source interval and restoration artifact byte-for-byte and by SHA-256.
5. Construct the required wrapper bytes directly from the record identifier and artifact path, then compare the live wrapper byte-for-byte with the exact three-line, LF-terminated form.
6. Count every exact wrapper input and artifact input across the live `handbook/**/*.tex` files, check its occurrence in the recorded destination or wrapper, and follow the literal `\input{...}` route from `handbook/main.tex`.
7. Count each nonempty recorded stable label globally and in its recorded destination. For labels added by a driver, check that the live textual placement precedes the governed wrapper input; for an unchanged source label, verify its exact location in the governed artifact.
8. Only after those checks, run `python tools/check_inherited_restoration.py --record <record>` separately for all ten records as a secondary cross-check.

## Exact source result

### Frozen authority

The live authority agrees exactly with `spec/inherited-corpus-manifest.json` and with the authority object in every audited record:

- path: `source/formal-logic-reference.tex`;
- edition recorded by all ten records: `Version 1.0`;
- bytes: `762835`;
- physical lines: `17206`;
- SHA-256: `0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc`;
- line endings: `17206` CR bytes, `17206` LF bytes, and `17206` CRLF pairs; the file has a terminal CRLF and no UTF-8 BOM.

### Interval, artifact, and content-token comparison

The frozen source uses CRLF endings, while all ten restoration artifacts use LF endings, have no CR bytes, and end in LF. Consequently, the literal raw source-interval byte stream is not identical to the literal artifact byte stream for any record. This is not a failure of the governed comparison: the raw source-interval hash and raw artifact hash each match their separate recorded fields, and the only byte-count difference is one CR byte per physical line. After the record's stated terminal-line-ending normalization, every source interval is byte-for-byte identical to its artifact.

In the table, `lines` is source interval lines / artifact lines. `source bytes` and `source SHA-256` refer to the raw CRLF source interval. `artifact bytes` and `artifact/token SHA-256` refer to the raw LF artifact; its raw hash equals its normalized content-token hash.

| Record | Locator | Lines | Source bytes | Artifact bytes | Source interval SHA-256 | Artifact/content-token SHA-256 | Result |
|---|---:|---:|---:|---:|---|---|---|
| `PRE-00035-00037` | 35--37 | 3 / 3 | 116 | 113 | `513c48de22ce0c6b6d69a2d3669c4521ff5142dd01d861b34915784722e15bf0` | `c79d4da149a3220a247f2ae094fb3bdb18f0787c4d03e77b150a59fbd5603b96` | PASS |
| `PRE-00039-00047` | 39--47 | 9 / 9 | 329 | 320 | `63fee27bf0eed6e78b438e4a18dbbce576dc584d4fdc3bf7f39a82e8522f78f5` | `5b1bfe1c66425872e546cadc9f7913f09e45f5fc94e577d017b3d5880a4672ed` | PASS |
| `SRC-00171-00197` | 171--197 | 27 / 27 | 777 | 750 | `8e81caf2b8ead9a68301be75a101d143339146b7b16d97add9fb7a0d42f79e0a` | `2facc8e7a342b7cb4449fdf7f8f14239f18c6f32adfa949b1170744a0439da89` | PASS |
| `SRC-00198-00234` | 198--234 | 37 / 37 | 1946 | 1909 | `5c2ae5a52a339a2cf26bd093b0527d1ceb41de4b752d8034ca8155a4bca21d3e` | `1703bd79753e71c3175d4c5473bb56a6365a5e23e291aae955ee5c839f9dac81` | PASS |
| `SRC-00235-00293` | 235--293 | 59 / 59 | 3300 | 3241 | `cfb4fd3bc98b3f99aed3441910c5c5f10b57a3f6c7319daba58a470f8a8eff43` | `1ae4b4ee4e8d0cc3223f93ad3ae8a0699e47d7a378a22343495fa6d127888422` | PASS |
| `SRC-00294-00320` | 294--320 | 27 / 27 | 1416 | 1389 | `4572b3a5a7146066afb2307e416577e47b2d1cc1bdde04fda88de3b2b1bf4393` | `def6c511ed2634044d9de15803a3686d8108d381480f498c9a0b36ce2dac609e` | PASS |
| `SRC-00321-00362` | 321--362 | 42 / 42 | 1938 | 1896 | `efb3339e522a9f12e34fd2b974557c612a8a9c7eb40ec388e12d4424306de8c8` | `a532bf1693bbcaecc7b10f5730ab6e42748c080c77566bbaae28496fdd910cc2` | PASS |
| `SRC-00363-00372` | 363--372 | 10 / 10 | 414 | 404 | `c05aaa09bdb34a81b660ef53c84ae6e980081ce74194f827b921dab7c92c19c3` | `3add1c0d52f826dc01d85ae0dbc5027af35ac6735efe3bd7c954be3d39133743` | PASS |
| `SRC-00373-00405` | 373--405 | 33 / 33 | 1097 | 1064 | `6f97f4a54c9a9d608c6dcb76f3733d6ac76826f57c396beea491161f56193e65` | `286c93b9e007e33c9a2a453397b49cbe2a82c0649fca0cb4b6dc5cc725a40663` | PASS |
| `SRC-09099-09111` | 9099--9111 | 13 / 13 | 395 | 382 | `c56e4463144025ebeecdaec3ae1877d623ed84f7cb2c52a30e86539b1cd748e3` | `38534e090c35db78d99d045d19b3c7f34f1f1aaa8999cf118c7a416cd41d9d2b` | PASS |

Exact-source conclusion: **PASS: 10; FAIL: 0**. This is exact equality under the comparison declared in each record, with the raw CRLF/LF distinction retained rather than hidden.

## Wrapper and destination result

### Exact wrapper bytes

Each live wrapper is exactly 125 UTF-8 bytes, has three LF-terminated physical lines and no CR byte, and is byte-for-byte equal to this form with its own record identifier and artifact numeric range substituted:

```tex
\begin{inheritedrestorationscope}{<provenance-id>}
\input{restoration/inherited-<numeric-range>}
\end{inheritedrestorationscope}
```

| Record | Live wrapper SHA-256 | Exact three-line shape |
|---|---|---|
| `PRE-00035-00037` | `4b5b4e72d5a74492cf1b45ba782d7c24db7ba34d5b7644d9f094e03275e058c3` | PASS |
| `PRE-00039-00047` | `654fdf75f54e841391abc4e36d77bc84524fe265ec45a686d07c810f719cb4b1` | PASS |
| `SRC-00171-00197` | `c38f280b1597c7759b103cf3c1cd2afa84457eb33cb43ec1f4b47337761941d1` | PASS |
| `SRC-00198-00234` | `4f2003e7fc90a00d70db6e54a4ddb57d5d233e4d8f5de0d374e366b97014d83b` | PASS |
| `SRC-00235-00293` | `b93dc0a6bed0aa44c59cc5c283c053bf8c3453605061be4eb66581a74adef41a` | PASS |
| `SRC-00294-00320` | `21779c9d30ae6e86f3027640987f686678c12d44e1b1391cd79ec131cf0d7e6b` | PASS |
| `SRC-00321-00362` | `9c4104ac6863b9d101df4a9df5480537b42bd972473c45f1ca87e5fadbe81016` | PASS |
| `SRC-00363-00372` | `93abbe45538d5f997c297e40ce47419dd007987963a7e37565c16e30f95dab5b` | PASS |
| `SRC-00373-00405` | `b1b2c9c2c0e5c1df79327b62a895d9e4e65d242a2ece2de040dc03aadde9158b` | PASS |
| `SRC-09099-09111` | `56c8378d1d04f699b89eedc85851e8da68c675c414a62e1e17342ec042a4de9f` | PASS |

### Single input, destination, and label evidence

For every row below:

- the wrapper input occurs exactly once across live `handbook/**/*.tex` and exactly once at the stated integration point;
- the artifact input occurs exactly once across live `handbook/**/*.tex` and exactly once in its exact wrapper;
- every literal input edge shown in the route occurs exactly once, giving one literal `\input` route from `handbook/main.tex` to the wrapper and then the artifact;
- if a stable label is listed, it occurs exactly once across live `handbook/**/*.tex` and exactly once in the recorded destination; labels added at an integration point precede the wrapper input, while inherited labels remain inside their byte-exact artifacts.

| Record | Unique route from `handbook/main.tex` | Integration point | Stable label and recorded destination | Result |
|---|---|---|---|---|
| `PRE-00035-00037` | driver -> wrapper -> artifact | `handbook/main.tex:9` | not applicable: the record has an empty stable label | PASS |
| `PRE-00039-00047` | driver -> wrapper -> artifact | `handbook/main.tex:10` | not applicable: the record has an empty stable label | PASS |
| `SRC-00171-00197` | driver -> `frontmatter.tex` -> wrapper -> artifact | `handbook/frontmatter.tex:11` | `sec:inherited-title-page`, line 10 | PASS |
| `SRC-00198-00234` | driver -> `frontmatter.tex` -> wrapper -> artifact | `handbook/frontmatter.tex:15` | `sec:inherited-preface`, line 14 | PASS |
| `SRC-00235-00293` | driver -> `frontmatter.tex` -> wrapper -> artifact | `handbook/frontmatter.tex:19` | `sec:inherited-terminology-policy`, line 18 | PASS |
| `SRC-00294-00320` | driver -> `frontmatter.tex` -> wrapper -> artifact | `handbook/frontmatter.tex:23` | `sec:inherited-evidence-policy`, line 22 | PASS |
| `SRC-00321-00362` | driver -> `frontmatter.tex` -> wrapper -> artifact | `handbook/frontmatter.tex:36` | `sec:inherited-graduate-scope`, line 26 | PASS |
| `SRC-00363-00372` | driver -> `parts/p01.tex` -> wrapper -> artifact | `handbook/parts/p01.tex:6` | `sec:inherited-set-prerequisites`, line 5 | PASS |
| `SRC-00373-00405` | driver -> `parts/p01.tex` -> wrapper -> artifact | `handbook/parts/p01.tex:5` | `sec:set-prerequisites-01`, `handbook/restoration/inherited-00373-00405.tex:2` | PASS |
| `SRC-09099-09111` | driver -> `parts/p05.tex` -> `parts/p05/diagonalization.tex` -> wrapper -> artifact | `handbook/parts/p05/diagonalization.tex:46` | `def:p05-robinson-q`, line 45 | PASS |

The two additional front-matter labels associated by the `SRC-00321-00362` record are each present once globally and once in `handbook/frontmatter.tex`: `sec:inherited-prerequisites` at line 32 and `sec:inherited-learning-outcomes` at line 34. The unchanged inherited label associated by the `SRC-00363-00372` record, `ch:set-prerequisites`, is present once globally and once at line 4 of `handbook/restoration/inherited-00363-00372.tex`. These three additional label checks pass. The unchanged `sec:set-prerequisites-01` label is already the recorded stable label for `SRC-00373-00405` and is therefore counted in the primary stable-label result rather than duplicated here.

Wrapper/destination conclusion: **PASS: 10; FAIL: 0**.

## Secondary checker cross-check

After completing the independent checks, the existing checker was run once per record:

```text
python tools/check_inherited_restoration.py --record spec/provenance/PRE-00035-00037.json
python tools/check_inherited_restoration.py --record spec/provenance/PRE-00039-00047.json
python tools/check_inherited_restoration.py --record spec/provenance/SRC-00171-00197.json
python tools/check_inherited_restoration.py --record spec/provenance/SRC-00198-00234.json
python tools/check_inherited_restoration.py --record spec/provenance/SRC-00235-00293.json
python tools/check_inherited_restoration.py --record spec/provenance/SRC-00294-00320.json
python tools/check_inherited_restoration.py --record spec/provenance/SRC-00321-00362.json
python tools/check_inherited_restoration.py --record spec/provenance/SRC-00363-00372.json
python tools/check_inherited_restoration.py --record spec/provenance/SRC-00373-00405.json
python tools/check_inherited_restoration.py --record spec/provenance/SRC-09099-09111.json
```

Each command returned `RESTORATION CHECK OK` with exit status 0. Secondary checker result: **PASS: 10; FAIL: 0**.

## Limitations and claims not made

- This evidence establishes the frozen authority hash, the exact raw source locators and interval hashes, the recorded artifact bytes and hashes, exact normalized content-token equality, exact wrapper bytes, static destination and label presence, and single reachability in the live literal `\input` graph.
- This audit did not compile the handbook or PDF and makes no build claim.
- It did not inspect rendered pages and makes no visual claim.
- It is not human editorial review and makes no human-review claim.
- It does not establish mathematical or formal-logical correctness, completeness, proof validity, or adequacy of the restored content.
- The label findings are static source findings. Without a build, they do not claim successful TeX hook execution, reference resolution, page placement, or absence of runtime duplicate-label warnings.
- No provenance record, restoration artifact, wrapper, handbook source, tool, snapshot, manifest, ledger, PDF, or test was modified by this audit.

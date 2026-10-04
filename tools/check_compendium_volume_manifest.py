#!/usr/bin/env python3
"""Verify the single public handbook artifact and its internal authority evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path, PurePosixPath
from typing import Any

try:
    from tools import check_inherited_restoration as restoration_checker
except ModuleNotFoundError:  # direct ``python tools/...`` execution
    import check_inherited_restoration as restoration_checker  # type: ignore[no-redef]


BOOK_TITLE = "The Methods of Reason"
PUBLIC_PATH = "handbook/main.pdf"
INHERITED_MANIFEST_PATH = "spec/inherited-corpus-manifest.json"
# Stable identity is independent of printed position (EDITION-2026-CONTRACT.md).
FINAL_PARTS = (
    ("p01", "Foundations of Formal Work"),
    ("p02", "Classical Logic"),
    ("p03", "Model Theory"),
    ("p04", "Computability and Complexity"),
    ("p05", "Arithmetic and Incompleteness"),
    ("p06", "Axiomatic Set Theory"),
    ("p07", "Proof Theory, Lambda Calculi, and Higher-Order Logic"),
    ("p08", "Nonclassical Logics"),
    ("p09", "Logic in Computer Science"),
    ("p10", "Algebraic and Categorical Logic"),
    ("p15", "Uncertainty and Statistical Inference"),
    ("p16", "Explanation, Abduction and Causation"),
    ("p17", "Decision and Strategic Reasoning"),
    ("p18", "Argumentation and Informal Reasoning"),
    ("p19", "Empirical Science of Reasoning"),
    ("p11", "Philosophy of Logic"),
    ("p12", "Automation, Mechanization, and Formal Practice"),
    ("p13", "Chronology and Biography"),
    ("p14", "Apparatus"),
)
FINAL_PART_TITLES = tuple(title for _, title in FINAL_PARTS)
APPROVED_PART_ORDINALS = {part_id: ordinal for ordinal, (part_id, _) in enumerate(FINAL_PARTS, 1)}
EDITION_NEW_PART_IDS = frozenset(f"p{number:02d}" for number in range(15, 20))
SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
FROZEN_INHERITED_MANIFEST = {
    "schema_version": 1,
    "tex": {
        "path": "source/formal-logic-reference.tex",
        "bytes": 762835,
        "lines": 17206,
        "sha256": "0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc",
    },
    "pdf": {
        "path": "source/formal-logic-reference.pdf",
        "bytes": 2042303,
        "pages": 251,
        "sha256": "0a8fb84042175343e5ba8bbcf65d4804d8a4019367edb3d22473927a3399bb3f",
    },
}
PART2_RESTORATION_IDS = (
    "SRC-01649-01660",
    "SRC-01661-01816",
    "SRC-01817-01898",
    "SRC-01899-01945",
    "SRC-01946-02186",
    "SRC-02187-02192",
    "SRC-02193-02340",
    "SRC-02341-02450",
    "SRC-02451-02544",
    "SRC-02545-02664",
    "SRC-02665-02809",
    "SRC-02810-02914",
    "SRC-02915-02932",
    "SRC-02933-03021",
    "SRC-03022-03037",
    "SRC-03038-03104",
    "SRC-03105-03165",
    "SRC-03166-03239",
    "SRC-03240-03428",
    "SRC-03429-03518",
    "SRC-03519-03680",
    "SRC-03681-03728",
    "SRC-03729-03907",
    "SRC-03908-03926",
    "SRC-03927-04061",
    "SRC-04062-04108",
    "SRC-04109-04213",
    "SRC-04214-04234",
    "SRC-04235-04305",
    "SRC-04306-04575",
    "SRC-04576-04712",
    "SRC-04713-04920",
    "SRC-04921-04967",
    "SRC-04968-05042",
    "SRC-05043-05131",
    "SRC-05132-05567",
    "SRC-05568-05923",
    "SRC-05924-05959",
    "SRC-05960-06048",
    "SRC-12249-12261",
    "SRC-12262-12289",
    "SRC-12290-12355",
    "SRC-12356-12414",
    "SRC-12415-12536",
    "SRC-12537-12673",
    "SRC-12674-12720",
    "SRC-12721-12783",
    "SRC-12784-12923",
    "SRC-12924-12950",
    "SRC-12951-12969",
)
PART3_RESTORATION_IDS = (
    "SRC-06049-06069",
    "SRC-06070-06137",
    "SRC-06138-06242",
    "SRC-06243-06331",
    "SRC-06332-06421",
    "SRC-06422-06431",
    "SRC-06432-06493",
    "SRC-06494-06509",
    "SRC-06510-06629",
    "SRC-06630-06639",
    "SRC-06640-06693",
    "SRC-06694-06782",
    "SRC-06783-06791",
    "SRC-06792-06845",
    "SRC-06846-06854",
    "SRC-06855-06941",
    "SRC-06942-07134",
    "SRC-07135-07149",
    "SRC-07150-07294",
    "SRC-07295-07468",
    "SRC-07469-07493",
)
# Necessity: the generic transitive part scan cannot state the exact seventeen-wrapper
# Part IV route while distinguishing its governed subordinate source heading
# and the four explicitly OPEN supplement seams.
# Definition: PART4_RESTORATION_IDS is exactly the ordered provenance-ID tuple
# whose validated scope wrappers open public Part IV before its four separately
# bounded OPEN supplements.
# Standing: it is a metalinguistic checker abbreviation, not a source result or
# an audit, admission, build, visual, register, or acceptance status.
# Nonredundancy: the Part II and Part III tuples bind different public drivers,
# source headings, wrapper counts, and supplement seams, so neither determines it.
# Use: the p04 source validator below requires exact equality, order, scoped
# routing, and absence of direct raw-artifact inputs before accepting the surface.
PART4_RESTORATION_IDS = (
    "SRC-07494-07505",
    "SRC-07506-07677",
    "SRC-07678-07752",
    "SRC-07753-07843",
    "SRC-07844-07850",
    "SRC-07851-08048",
    "SRC-08049-08080",
    "SRC-08081-08143",
    "SRC-08144-08186",
    "SRC-08187-08238",
    "SRC-08239-08247",
    "SRC-08248-08305",
    "SRC-08306-08438",
    "SRC-08439-08709",
    "SRC-08710-08876",
    "SRC-08877-08897",
    "SRC-08898-09079",
)
# Necessity: the generic transitive part scan sees the exact Formal Arithmetic
# source title rather than the fixed public Part V title and cannot state the
# one permitted OPEN supplement seam or the preserved source island.
# Definition: PART5_RESTORATION_IDS is exactly the nineteen-entry source-order
# provenance tuple from the Part V opening through source line 10059, including
# the already governed SRC-09099-09111 island once.
# Standing: it is a metalinguistic checker abbreviation, not a source result,
# theorem family, audit, admission, build, visual, register, or acceptance
# status.
# Nonredundancy: the Part IV tuple has a different public-title relation,
# wrapper count, source interval, and supplement placement and cannot determine
# the Part V route.
# Use: the p05 validator requires this exact wrapper order, the one bounded
# model/interpretation supplement after the first source chapter, the governed
# public-title record, and absence of raw artifacts or driver part aliases.
PART5_RESTORATION_IDS = (
    "SRC-09080-09098",
    "SRC-09099-09111",
    "SRC-09112-09149",
    "SRC-09150-09174",
    "SRC-09175-09187",
    "SRC-09188-09261",
    "SRC-09262-09327",
    "SRC-09328-09438",
    "SRC-09439-09497",
    "SRC-09498-09538",
    "SRC-09539-09619",
    "SRC-09620-09728",
    "SRC-09729-09749",
    "SRC-09750-09816",
    "SRC-09817-09876",
    "SRC-09877-09924",
    "SRC-09925-09992",
    "SRC-09993-10027",
    "SRC-10028-10059",
)
# Necessity: the generic scan cannot distinguish the direct exact Part VI
# source binding from a driver alias or state its bounded OPEN addition seams.
# Definition: PART6_RESTORATION_IDS is exactly the ordered twenty-three-record
# source run of public Part VI through source line 11353.
# Standing: it is checker metadata, not a source result, audit, admission,
# build, visual, register, or acceptance result.
# Nonredundancy: Part V has a title mapping and nineteen wrappers; neither its
# tuple nor the generic part rule determines this direct-source route.
# Use: the p06 validator requires this tuple, exact source label, wrapper order,
# bounded OPEN addition seams, and absence of raw, historical, or driver aliases.
PART6_RESTORATION_IDS = (
    "SRC-10060-10088",
    "SRC-10089-10271",
    "SRC-10272-10352",
    "SRC-10353-10451",
    "SRC-10452-10520",
    "SRC-10521-10558",
    "SRC-10559-10674",
    "SRC-10675-10769",
    "SRC-10770-10825",
    "SRC-10826-10881",
    "SRC-10882-10899",
    "SRC-10900-10988",
    "SRC-10989-11011",
    "SRC-11012-11052",
    "SRC-11053-11103",
    "SRC-11104-11126",
    "SRC-11127-11199",
    "SRC-11200-11239",
    "SRC-11240-11279",
    "SRC-11280-11293",
    "SRC-11294-11314",
    "SRC-11315-11337",
    "SRC-11338-11353",
)
# Necessity: the generic transitive part scan cannot distinguish the fixed
# public Part VII heading from the exact subordinate source part, nor can it
# state the two bounded OPEN addition seams without admitting historical overlap.
# Definition: PART7_RESTORATION_IDS is exactly the ordered nineteen-record
# source run through the end of Part VII at source line 12248.
# Standing: it is checker metadata, not a source result, theorem family, audit,
# admission, build, visual, register, or acceptance result.
# Nonredundancy: the Part VI tuple is a direct-source public-part route with
# twenty-three wrappers and different addition seams, so it cannot determine
# this fixed-public/subordinate-source route.
# Use: the p07 validator requires this tuple, exact source part and label,
# wrapper order, two bounded OPEN additions, later-chapter order, and absence
# of raw artifacts, historical routes, or source-label aliases.
PART7_RESTORATION_IDS = (
    "SRC-11354-11413",
    "SRC-11414-11505",
    "SRC-11506-11519",
    "SRC-11520-11598",
    "SRC-11599-11627",
    "SRC-11628-11644",
    "SRC-11645-11695",
    "SRC-11696-11710",
    "SRC-11711-11740",
    "SRC-11741-11767",
    "SRC-11768-11823",
    "SRC-11824-11881",
    "SRC-11882-11913",
    "SRC-11914-11960",
    "SRC-11961-12029",
    "SRC-12030-12100",
    "SRC-12101-12132",
    "SRC-12133-12217",
    "SRC-12218-12248",
)
# Necessity: the generic transitive scan sees the singular exact source Part X
# title rather than the fixed plural public Part VIII title and cannot state the
# five bounded addition seams around four exact source chapters.
# Definition: PART8_RESTORATION_IDS is exactly the ordered forty-record source
# run from the Nonclassical opening through the relevance/linear chapter ending
# at line 14094.
# Standing: it is checker metadata, not a source result, theorem family, audit,
# admission, build, visual, register, or acceptance result.
# Nonredundancy: Part VII uses a fixed public driver plus a subordinate source
# part and nineteen wrappers; neither that tuple nor the generic rule determines
# this governed public-title mapping and its five supplement boundaries.
# Use: the p08 validator requires this tuple, exact source label, wrapper order,
# the five bounded OPEN additions, and absence of raw artifacts, historical
# routes, generated audit input, or driver label aliases.
PART8_RESTORATION_IDS = (
    "SRC-12970-12988",
    "SRC-12989-13045",
    "SRC-13046-13057",
    "SRC-13058-13099",
    "SRC-13100-13127",
    "SRC-13128-13140",
    "SRC-13141-13157",
    "SRC-13158-13179",
    "SRC-13180-13200",
    "SRC-13201-13213",
    "SRC-13214-13254",
    "SRC-13255-13284",
    "SRC-13285-13316",
    "SRC-13317-13339",
    "SRC-13340-13409",
    "SRC-13410-13439",
    "SRC-13440-13471",
    "SRC-13472-13478",
    "SRC-13479-13518",
    "SRC-13519-13551",
    "SRC-13552-13564",
    "SRC-13565-13583",
    "SRC-13584-13613",
    "SRC-13614-13640",
    "SRC-13641-13699",
    "SRC-13700-13730",
    "SRC-13731-13774",
    "SRC-13775-13788",
    "SRC-13789-13806",
    "SRC-13807-13861",
    "SRC-13862-13896",
    "SRC-13897-13918",
    "SRC-13919-13938",
    "SRC-13939-13971",
    "SRC-13972-14000",
    "SRC-14001-14015",
    "SRC-14016-14034",
    "SRC-14035-14051",
    "SRC-14052-14068",
    "SRC-14069-14094",
)
# Necessity: the generic Part XII scan cannot express the exact label-less
# source Part XI heading as a subordinate public Part XII chapter or bind the
# two bounded editorial-addition seams around the exact source chapters.
# Definition: PART12_RESTORATION_IDS is exactly the ordered forty-one-record
# source run from the Formal Practice part heading through the Writing and
# Typesetting and Research Workflow chapters, source Appendices A--F, and the
# D.6 section continuation, including all four literal blank separators,
# ending at line 16802.
# Standing: it is checker metadata, not a method, inference rule, theorem
# family, source-fidelity verdict, build, visual, admission, or acceptance.
# Nonredundancy: the generic part-title rule sees only a second raw part command;
# it cannot prove that the exact label-less source part leaves the public counter
# unchanged, that blank source lines remain ordered, or that the old combined
# workflow and generated audit are unrouted.
# Use: the p12 validator requires this tuple, the v2 no-label layout record,
# exact wrapper/workflow-addition/automation-addition order, and absence of raw
# or historical inputs; the staged mutation suite rejects every listed drift.
PART12_RESTORATION_IDS = (
    "SRC-14095-14146",
    "SRC-14147-14169",
    "SRC-14170-14202",
    "SRC-14203-14230",
    "SRC-14231-14270",
    "SRC-14271-14350",
    "SRC-14351-14400",
    "SRC-14401-14434",
    "SRC-14435-14479",
    "SRC-14480-14495",
    "SRC-14496-14521",
    "SRC-14522-14560",
    "SEP-14561-14561",
    "SRC-14562-14589",
    "SEP-14590-14590",
    "SRC-14591-14628",
    "SRC-14629-14660",
    "SRC-14661-14690",
    "SRC-14691-14728",
    "SRC-14729-14778",
    "SRC-14779-14814",
    "SRC-14815-14850",
    "SRC-14851-14870",
    "SRC-14871-14931",
    "SRC-14932-14945",
    "SRC-14946-14975",
    "SRC-14976-14990",
    "SRC-14991-15029",
    "SRC-15030-15050",
    "SRC-15051-15068",
    "SRC-15069-15077",
    "SRC-15078-15091",
    "SEP-15092-15092",
    "SRC-15093-15206",
    "SRC-15207-15239",
    "SRC-15240-15488",
    "SRC-15489-15619",
    "SRC-15620-15637",
    "SRC-15638-16742",
    "SRC-16743-16801",
    "SEP-16802-16802",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON value must be an object")
    return value


def is_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def is_sha256(value: Any) -> bool:
    return isinstance(value, str) and SHA256_PATTERN.fullmatch(value) is not None


def is_canonical_relative_path(value: Any) -> bool:
    if not isinstance(value, str) or not value or "\\" in value:
        return False
    pure = PurePosixPath(value)
    return (
        not pure.is_absolute()
        and pure.as_posix() == value
        and all(part not in {"", ".", ".."} for part in pure.parts)
    )


def resolve_inside(root: Path, recorded: str) -> Path:
    path = (root / recorded).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError as error:
        raise ValueError(f"path leaves repository root: {recorded}") from error
    return path


def exact_fields(
    failures: list[str], label: str, value: Any, expected: set[str]
) -> bool:
    if not isinstance(value, dict):
        failures.append(f"{label}: must be an object")
        return False
    if set(value) != expected:
        failures.append(
            f"{label}: fields differ from exact schema: "
            f"{sorted(set(value) ^ expected)}"
        )
        return False
    return True


def validate_manifest_structure(manifest: dict[str, Any]) -> list[str]:
    """Return exact-schema failures without reading repository files."""

    failures: list[str] = []
    top_fields = {
        "schema_version",
        "manifest_kind",
        "title",
        "public_artifact",
        "internal_authority_evidence",
        "final_release_evidence",
    }
    exact_fields(failures, "manifest", manifest, top_fields)

    if manifest.get("schema_version") != 2:
        failures.append("manifest: schema_version must be exactly 2")
    if manifest.get("manifest_kind") != "single-publication-handbook":
        failures.append(
            "manifest: manifest_kind must be 'single-publication-handbook'"
        )
    if manifest.get("title") != BOOK_TITLE:
        failures.append(f"manifest: title must be exactly {BOOK_TITLE!r}")

    public = manifest.get("public_artifact")
    public_fields = {
        "artifact_id",
        "title",
        "path",
        "artifact_kind",
        "publication_status",
        "release_ready",
        "observed",
    }
    if exact_fields(failures, "public_artifact", public, public_fields):
        assert isinstance(public, dict)
        if public.get("artifact_id") != "the-methods-of-reason":
            failures.append(
                "public_artifact: artifact_id must be 'the-methods-of-reason'"
            )
        if public.get("title") != BOOK_TITLE:
            failures.append(f"public_artifact: title must be exactly {BOOK_TITLE!r}")
        if public.get("path") != PUBLIC_PATH:
            failures.append(f"public_artifact: path must be exactly {PUBLIC_PATH!r}")
        if public.get("artifact_kind") != "pdf":
            failures.append("public_artifact: artifact_kind must be 'pdf'")
        status = public.get("publication_status")
        if status not in {"construction-draft", "release"}:
            failures.append(
                "public_artifact: publication_status must be 'construction-draft' "
                "or 'release'"
            )
        ready = public.get("release_ready")
        if not isinstance(ready, bool):
            failures.append("public_artifact: release_ready must be a boolean")
        elif ready != (status == "release"):
            failures.append(
                "public_artifact: release-ready must be true exactly for release status"
            )

        observed = public.get("observed")
        if exact_fields(
            failures, "public_artifact.observed", observed, {"bytes", "pages", "sha256"}
        ):
            assert isinstance(observed, dict)
            for field in ("bytes", "pages"):
                value = observed.get(field)
                if not is_int(value) or value < 1:
                    failures.append(
                        f"public_artifact.observed: {field} must be a positive integer"
                    )
            if not is_sha256(observed.get("sha256")):
                failures.append(
                    "public_artifact.observed: sha256 must be 64 lowercase hexadecimal digits"
                )

    authority = manifest.get("internal_authority_evidence")
    if exact_fields(
        failures,
        "internal_authority_evidence",
        authority,
        {"inherited_corpus_manifest", "published_with_book"},
    ):
        assert isinstance(authority, dict)
        if authority.get("inherited_corpus_manifest") != INHERITED_MANIFEST_PATH:
            failures.append(
                "internal authority: inherited_corpus_manifest must be exactly "
                f"{INHERITED_MANIFEST_PATH!r}"
            )
        if authority.get("published_with_book") is not False:
            failures.append(
                "internal authority: frozen source and PDF must not be published with the book"
            )

    release = manifest.get("final_release_evidence")
    public_status = public.get("publication_status") if isinstance(public, dict) else None
    if public_status == "construction-draft":
        if release is not None:
            failures.append(
                "final_release_evidence must be null while the public artifact is a draft"
            )
    elif public_status == "release":
        release_fields = {
            "readiness_manifest_path",
            "readiness_manifest_sha256",
            "user_final_acceptance_path",
            "user_final_acceptance_sha256",
            "public_pdf_sha256",
        }
        if exact_fields(failures, "final_release_evidence", release, release_fields):
            assert isinstance(release, dict)
            for field in ("readiness_manifest_path", "user_final_acceptance_path"):
                if not is_canonical_relative_path(release.get(field)):
                    failures.append(
                        f"final_release_evidence: {field} must be a canonical relative path"
                    )
            for field in (
                "readiness_manifest_sha256",
                "user_final_acceptance_sha256",
                "public_pdf_sha256",
            ):
                if not is_sha256(release.get(field)):
                    failures.append(
                        f"final_release_evidence: {field} must be a SHA-256 digest"
                    )
            observed_hash = (
                public.get("observed", {}).get("sha256")
                if isinstance(public, dict)
                and isinstance(public.get("observed"), dict)
                else None
            )
            if release.get("public_pdf_sha256") != observed_hash:
                failures.append(
                    "final_release_evidence: public_pdf_sha256 must equal the observed PDF digest"
                )
    return failures


def _strip_tex_comments(text: str) -> str:
    """Remove TeX comments while retaining executable escaped percent signs."""

    cleaned: list[str] = []
    for line in text.splitlines(keepends=True):
        cut = len(line)
        for index, character in enumerate(line):
            if character != "%":
                continue
            backslashes = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                backslashes += 1
                cursor -= 1
            if backslashes % 2 == 0:
                cut = index
                break
        suffix = "\n" if line.endswith(("\n", "\r")) else ""
        cleaned.append(line[:cut].rstrip("\r\n") + suffix)
    return "".join(cleaned)


def _part_surface(
    root: Path,
    relative_path: str,
    failures: list[str],
    active: tuple[str, ...] = (),
    provenance_id: str | None = None,
) -> list[tuple[str, str, str | None]]:
    """Return every source file reached from one part driver, with multiplicity."""

    canonical = relative_path.replace("\\", "/")
    pure = PurePosixPath(canonical)
    if (
        pure.is_absolute()
        or any(part in ("", ".", "..") for part in pure.parts)
        or not canonical.endswith(".tex")
    ):
        failures.append(f"book source: noncanonical TeX input {relative_path!r}")
        return []
    if canonical in active:
        failures.append(f"book source: cyclic TeX input at {canonical}")
        return []
    path = root / "handbook" / Path(*pure.parts)
    try:
        source = _strip_tex_comments(path.read_text(encoding="utf-8"))
    except OSError as error:
        failures.append(f"book source: unable to read {path}: {error}")
        return []

    wrapper_match = re.fullmatch(
        r"restoration/scope-((?:PRE|SRC|CTL|SEP)-\d{5}-\d{5})\.tex",
        canonical,
    )
    child_provenance = provenance_id
    if wrapper_match:
        wrapper_id = wrapper_match.group(1)
        if provenance_id is not None:
            failures.append(
                f"book source: nested provenance wrapper at {canonical}"
            )
        child_provenance = wrapper_id

    surface = [(canonical, source, provenance_id)]
    next_active = active + (canonical,)
    for match in re.finditer(r"\\input\s*\{([^{}]+)\}", source):
        target = match.group(1).strip().replace("\\", "/")
        if not target.endswith(".tex"):
            target += ".tex"
        surface.extend(
            _part_surface(root, target, failures, next_active, child_provenance)
        )
    return surface


def validate_book_sources(root: Path) -> list[str]:
    """Verify the public title and the approved stable-ID/printed-order mapping.

    Missing future drivers are explicit migration requirements, not permission
    to publish placeholders or to accept the old fourteen-part layout as final.
    """

    failures: list[str] = []
    main_path = root / "handbook/main.tex"
    title_path = root / "handbook/publication-title.tex"
    try:
        main = main_path.read_text(encoding="utf-8")
    except OSError as error:
        return [f"book source: unable to read handbook/main.tex: {error}"]
    try:
        title_page = title_path.read_text(encoding="utf-8")
    except OSError as error:
        return [f"book source: unable to read handbook/publication-title.tex: {error}"]

    metadata_line = rf"\hypersetup{{pdftitle={{{BOOK_TITLE}}}}}"
    if main.count(metadata_line) != 1:
        failures.append(
            "book source: handbook/main.tex must set the exact public PDF title once"
        )
    if title_page.count(BOOK_TITLE) != 1:
        failures.append(
            "book source: publication-title.tex must display the exact public title once"
        )

    main = _strip_tex_comments(main)
    approved_ids = {part_id for part_id, _ in FINAL_PARTS}
    for part_id in re.findall(r"\\input\s*\{parts/(p[0-9]+)\}", main):
        if part_id not in approved_ids:
            failures.append(f"book source: unapproved stable part ID {part_id}")
    cursor = -1
    for part_id, title in FINAL_PARTS:
        input_line = rf"\input{{parts/{part_id}}}"
        if part_id in EDITION_NEW_PART_IDS and main.count(input_line) == 0:
            failures.append(
                f"edition migration: required stable part {part_id} is not yet routed"
            )
            continue
        if main.count(input_line) != 1:
            failures.append(
                f"book source: handbook/main.tex must input {part_id} exactly once"
            )
        else:
            position = main.index(input_line)
            if position <= cursor:
                failures.append("book source: approved stable part inputs are out of printed order")
            cursor = position

        part_relative = f"parts/{part_id}.tex"
        surface = _part_surface(root, part_relative, failures)
        if not surface:
            continue
        declaration = rf"\hbpartidentity{{{part_id}}}"
        declaration_matches = list(re.finditer(r"\\hbpartidentity\s*\{([^{}]+)\}", surface[0][1]))
        declarations = [match.group(1) for match in declaration_matches]
        if declarations != [part_id]:
            failures.append(
                f"book source: {part_relative} must declare {declaration} exactly once"
            )
        elif declaration_matches[0].start() > min(
            (match.start() for match in re.finditer(r"\\(?:part|input)\b", surface[0][1])),
            default=len(surface[0][1]),
        ):
            failures.append(f"book source: {part_relative} stable identity must precede its content")
        part_titles: list[str] = []
        part_locations: list[str] = []
        label_count = 0
        direct_binding = False
        part_occurrences: list[tuple[str, str, str | None]] = []
        for relative, source, provenance_id in surface:
            for match in re.finditer(r"\\part(?!\*)\s*\{([^{}]+)\}", source):
                part_titles.append(match.group(1))
                part_locations.append(relative)
                part_occurrences.append((match.group(1), relative, provenance_id))
            label_count += len(
                re.findall(rf"\\label\s*\{{part:{part_id}\}}", source)
            )
            if re.search(
                rf"\\part\s*\{{{re.escape(title)}\}}\s*"
                rf"\\label\s*\{{part:{part_id}\}}",
                source,
            ):
                direct_binding = True

        source_exact_binding = (
            part_id == "p01"
            and part_locations == ["restoration/inherited-00363-00372.tex"]
            and label_count == 0
        )
        if part_id == "p02":
            driver_source = surface[0][1]
            public_binding = r"\part{Classical Logic}\label{part:p02}"
            expected_inputs = [
                f"restoration/scope-{provenance_id}"
                for provenance_id in PART2_RESTORATION_IDS
            ]
            higher_supplement = "parts/p02/second-and-higher-order-logic-supplement"
            expected_driver = (
                expected_inputs[:8]
                + ["parts/p02/propositional-hilbert-tableaux"]
                + expected_inputs[8:14]
                + ["parts/p02/propositional-metatheory-supplement"]
                + expected_inputs[14:39]
                + [
                    "parts/p02/first-order-calculi-supplement",
                    "parts/p02/first-order-completeness-remainder",
                    "parts/p02/first-order-logic",
                ]
                + expected_inputs[39:]
                + [higher_supplement, "parts/p02/variants"]
            )
            # C4 is a separate authored PA2 definition between its two source
            # neighbors; the exact restoration subsequence remains unchanged.
            expected_driver.insert(
                expected_driver.index("restoration/scope-SRC-12415-12536"),
                "parts/p02/pa2-definition",
            )
            # D-P2-010 follows the actual CPL valuation/equivalence clauses.
            expected_driver.insert(
                expected_driver.index("restoration/scope-SRC-01899-01945"),
                "parts/p02/propositional-substitution",
            )
            # D-P2-007 follows the inherited CNF construction and its forward link.
            expected_driver.insert(
                expected_driver.index("restoration/scope-SRC-02187-02192"),
                "parts/p02/tseitin-transformation",
            )
            direct_inputs = [
                match.group(1).strip().removesuffix(".tex")
                for match in re.finditer(r"\\input\s*\{([^{}]+)\}", driver_source)
            ]
            restoration_inputs = [
                value for value in direct_inputs
                if value.startswith("restoration/scope-")
            ]
            raw_inputs = [
                value for value in direct_inputs
                if value.startswith("restoration/inherited-")
            ]
            expected_occurrences = [
                ("Classical Logic", "parts/p02.tex", None),
                (
                    "Classical Propositional Logic",
                    "restoration/inherited-01649-01660.tex",
                    "SRC-01649-01660",
                ),
                (
                    "Classical First-Order Logic",
                    "restoration/inherited-03022-03037.tex",
                    "SRC-03022-03037",
                ),
                (
                    "Second-Order and Higher-Order Logic",
                    "restoration/inherited-12249-12261.tex",
                    "SRC-12249-12261",
                ),
            ]
            source_labels = {
                (
                    "restoration/inherited-01649-01660.tex",
                    "SRC-01649-01660",
                    "part:classical-propositional",
                ),
                (
                    "restoration/inherited-03022-03037.tex",
                    "SRC-03022-03037",
                    "part:classical-first-order",
                ),
                (
                    "restoration/inherited-12249-12261.tex",
                    "SRC-12249-12261",
                    "part:higher-order",
                ),
            }
            source_labels_exact = all(
                sum(
                    source.count(rf"\label{{{source_label}}}")
                    for relative, source, occurrence_id in surface
                    if relative == artifact and occurrence_id == provenance_id
                ) == 1
                for artifact, provenance_id, source_label in source_labels
            )
            records_valid = True
            for provenance_id in PART2_RESTORATION_IDS:
                layout_record_path = root / f"spec/provenance/{provenance_id}.json"
                try:
                    layout_record = restoration_checker.load_json(layout_record_path)
                    restoration_checker.validate_record(
                        layout_record, layout_record_path, root
                    )
                except (OSError, restoration_checker.CheckFailure) as error:
                    records_valid = False
                    failures.append(
                        "book source: p02 governed source-part record failed: "
                        f"{error}"
                    )
            ordered_after_public = (
                driver_source.count(public_binding) == 1
                and all(
                    driver_source.count(rf"\input{{restoration/scope-{provenance_id}}}")
                    == 1
                    and driver_source.index(public_binding)
                    < driver_source.index(
                        rf"\input{{restoration/scope-{provenance_id}}}"
                    )
                    for provenance_id in (
                        "SRC-01649-01660",
                        "SRC-03022-03037",
                        "SRC-12249-12261",
                    )
                )
            )
            if raw_inputs:
                failures.append("book source: p02 raw inherited input is forbidden")
            if not (
                part_occurrences == expected_occurrences
                and direct_binding
                and label_count == 1
                and source_labels_exact
                and restoration_inputs == expected_inputs
                and not raw_inputs
                and direct_inputs == expected_driver
                and direct_inputs.count(higher_supplement) == 1
                and ordered_after_public
                and records_valid
            ):
                failures.append(
                    "book source: p02 must classify exactly one public Part II "
                    "and the three governed subordinate source parts, with exact "
                    "titles, labels, routes, fifty-wrapper order, and bounded "
                    "higher-order supplement seam"
                )
            continue
        if part_id == "p03":
            driver_source = surface[0][1]
            expected_inputs = [
                f"restoration/scope-{provenance_id}"
                for provenance_id in PART3_RESTORATION_IDS
            ]
            maps_supplement = "parts/p03/maps-elementarity-supplement"
            types_supplement = "parts/p03/types-ultraproducts-supplement"
            qe_supplement = "parts/p03/qe-categoricity-games-supplement"
            expected_driver_prefix = (
                expected_inputs[:8]
                + [maps_supplement]
                + expected_inputs[8:18]
                + [types_supplement]
                + expected_inputs[18:]
                + [qe_supplement]
            )
            direct_inputs = [
                match.group(1).strip().removesuffix(".tex")
                for match in re.finditer(r"\\input\s*\{([^{}]+)\}", driver_source)
            ]
            restoration_inputs = [
                value for value in direct_inputs
                if value.startswith("restoration/scope-")
            ]
            expected_occurrences = [
                (
                    "Model Theory",
                    "restoration/inherited-06049-06069.tex",
                    "SRC-06049-06069",
                )
            ]
            source_label_exact = sum(
                source.count(r"\label{part:model-theory}")
                for relative, source, provenance_id in surface
                if relative == "restoration/inherited-06049-06069.tex"
                and provenance_id == "SRC-06049-06069"
            ) == 1
            source_label_total = sum(
                source.count(r"\label{part:model-theory}")
                for _relative, source, _provenance_id in surface
            )
            layout_record_path = root / "spec/provenance/SRC-06049-06069.json"
            layout_record_valid = True
            try:
                layout_record = restoration_checker.load_json(layout_record_path)
                restoration_checker.validate_record(
                    layout_record, layout_record_path, root
                )
            except (OSError, restoration_checker.CheckFailure) as error:
                layout_record_valid = False
                failures.append(
                    "book source: p03 governed direct source-part record failed: "
                    f"{error}"
                )
            if not (
                part_occurrences == expected_occurrences
                and label_count == 0
                and source_label_exact
                and source_label_total == 1
                and restoration_inputs == expected_inputs
                and direct_inputs[: len(expected_driver_prefix)]
                == expected_driver_prefix
                and direct_inputs.count(maps_supplement) == 1
                and direct_inputs.count(types_supplement) == 1
                and direct_inputs.count(qe_supplement) == 1
                and layout_record_valid
            ):
                failures.append(
                    "book source: p03 must classify exactly the direct public "
                    "source Part III SRC-06049-06069, with its exact title, "
                    "source label, direct route, governed supplement seams, "
                    "and twenty-one-wrapper order"
                )
            continue
        if part_id == "p04":
            driver_source = surface[0][1]
            public_binding = (
                r"\part{Computability and Complexity}\label{part:p04}"
            )
            expected_inputs = [
                f"restoration/scope-{provenance_id}"
                for provenance_id in PART4_RESTORATION_IDS
            ]
            machine_supplement = "parts/p04/machines-effective-procedures-supplement"
            universal_supplement = "parts/p04/universal-reductions-supplement"
            decision_supplement = "parts/p04/decision-hierarchy-apparatus-supplement"
            degrees_continuation = "parts/p04/degrees-and-priority-continuation"
            expected_driver_prefix = expected_inputs + [
                machine_supplement,
                universal_supplement,
                decision_supplement,
                degrees_continuation,
            ]
            direct_inputs = [
                match.group(1).strip().removesuffix(".tex")
                for match in re.finditer(r"\\input\s*\{([^{}]+)\}", driver_source)
            ]
            restoration_inputs = [
                value
                for value in direct_inputs
                if value.startswith("restoration/scope-")
            ]
            raw_inherited_inputs = [
                value
                for value in direct_inputs
                if value.startswith("restoration/inherited-")
            ]
            if raw_inherited_inputs:
                failures.append(
                    "book source: p04 raw inherited input is forbidden; "
                    "exact source artifacts must be reached only through their "
                    "validated provenance scope wrappers"
                )
            expected_occurrences = [
                ("Computability and Complexity", "parts/p04.tex", None),
                (
                    "Computability",
                    "restoration/inherited-07494-07505.tex",
                    "SRC-07494-07505",
                ),
            ]
            source_label_exact = sum(
                source.count(r"\label{part:computability}")
                for relative, source, provenance_id in surface
                if relative == "restoration/inherited-07494-07505.tex"
                and provenance_id == "SRC-07494-07505"
            ) == 1
            source_label_total = sum(
                source.count(r"\label{part:computability}")
                for _relative, source, _provenance_id in surface
            )
            layout_record_path = root / "spec/provenance/SRC-07494-07505.json"
            layout_record_valid = True
            try:
                layout_record = restoration_checker.load_json(layout_record_path)
                restoration_checker.validate_record(
                    layout_record, layout_record_path, root
                )
            except (OSError, restoration_checker.CheckFailure) as error:
                layout_record_valid = False
                failures.append(
                    "book source: p04 governed subordinate source-part record failed: "
                    f"{error}"
                )
            if not (
                part_occurrences == expected_occurrences
                and direct_binding
                and driver_source.count(public_binding) == 1
                and label_count == 1
                and source_label_exact
                and source_label_total == 1
                and restoration_inputs == expected_inputs
                and not raw_inherited_inputs
                and direct_inputs[: len(expected_driver_prefix)]
                == expected_driver_prefix
                and direct_inputs.count(machine_supplement) == 1
                and direct_inputs.count(universal_supplement) == 1
                and direct_inputs.count(decision_supplement) == 1
                and direct_inputs.count(degrees_continuation) == 1
                and layout_record_valid
            ):
                failures.append(
                    "book source: p04 must classify exactly one public Part IV "
                    "and the governed subordinate source part SRC-07494-07505, "
                    "with exact titles, labels, routes, seventeen-wrapper order, "
                    "and governed supplement seams"
                )
            continue
        if part_id == "p05":
            driver_source = surface[0][1]
            expected_inputs = [
                f"restoration/scope-{provenance_id}"
                for provenance_id in PART5_RESTORATION_IDS
            ]
            model_supplement = "parts/p05/models-and-interpretability-supplement"
            expected_driver_prefix = (
                expected_inputs[:8] + [model_supplement] + expected_inputs[8:]
            )
            direct_inputs = [
                match.group(1).strip().removesuffix(".tex")
                for match in re.finditer(r"\\input\s*\{([^{}]+)\}", driver_source)
            ]
            restoration_inputs = [
                value
                for value in direct_inputs
                if value.startswith("restoration/scope-")
            ]
            raw_inherited_inputs = [
                value
                for value in direct_inputs
                if value.startswith("restoration/inherited-")
            ]
            if raw_inherited_inputs:
                failures.append(
                    "book source: p05 raw inherited input is forbidden; exact "
                    "source artifacts must be reached only through validated "
                    "provenance scope wrappers"
                )
            expected_occurrences = [
                (
                    "Formal Arithmetic and Incompleteness",
                    "restoration/inherited-09080-09098.tex",
                    "SRC-09080-09098",
                )
            ]
            source_label_exact = sum(
                source.count(r"\label{part:incompleteness}")
                for relative, source, provenance_id in surface
                if relative == "restoration/inherited-09080-09098.tex"
                and provenance_id == "SRC-09080-09098"
            ) == 1
            source_label_total = sum(
                source.count(r"\label{part:incompleteness}")
                for _relative, source, _provenance_id in surface
            )
            layout_record_path = root / "spec/provenance/SRC-09080-09098.json"
            layout_record_valid = True
            try:
                layout_record = restoration_checker.load_json(layout_record_path)
                restoration_checker.validate_record(
                    layout_record, layout_record_path, root
                )
            except (OSError, restoration_checker.CheckFailure) as error:
                layout_record_valid = False
                failures.append(
                    "book source: p05 governed public-title record failed: "
                    f"{error}"
                )
            if not (
                part_occurrences == expected_occurrences
                and label_count == 0
                and source_label_exact
                and source_label_total == 1
                and restoration_inputs == expected_inputs
                and not raw_inherited_inputs
                and direct_inputs[: len(expected_driver_prefix)]
                == expected_driver_prefix
                and direct_inputs.count(model_supplement) == 1
                and layout_record_valid
            ):
                failures.append(
                    "book source: p05 must classify exactly the governed source "
                    "part SRC-09080-09098 as public Part V, with its exact source "
                    "label, fixed public title, nineteen-wrapper order, and one "
                    "bounded OPEN supplement seam"
                )
            continue
        if part_id == "p06":
            driver_source = surface[0][1]
            expected_inputs = [
                f"restoration/scope-{provenance_id}"
                for provenance_id in PART6_RESTORATION_IDS
            ]
            table_supplement = "parts/p06/zfc-axiom-table-supplement"
            ordinal_supplement = "parts/p06/ordinal-rank-supplement"
            choice_supplement = "parts/p06/cardinals-choice-supplement"
            forcing_vocabulary = "parts/p06/forcing-vocabulary"
            constructibility_supplement = "parts/p06/constructibility-forcing-supplement"
            variants_supplement = "parts/p06/forcing-variants-supplement"
            arithmetic_supplement = "parts/p06/cardinal-arithmetic-supplement"
            expected_driver = [
                expected_inputs[0],
                expected_inputs[1],
                table_supplement,
                expected_inputs[2],
                expected_inputs[3],
                expected_inputs[4],
                expected_inputs[5],
                expected_inputs[6],
                ordinal_supplement,
                choice_supplement,
                *expected_inputs[7:],
                forcing_vocabulary,
                constructibility_supplement,
                variants_supplement,
                "parts/p06/infinitary-combinatorics",
                arithmetic_supplement,
                "parts/p06/large-cardinals-absoluteness",
                "parts/p06/descriptive-set-theory",
                "parts/p06/determinacy",
            ]
            direct_inputs = [
                match.group(1).strip().removesuffix(".tex")
                for match in re.finditer(r"\\input\s*\{([^{}]+)\}", driver_source)
            ]
            restoration_inputs = [
                value for value in direct_inputs if value.startswith("restoration/scope-")
            ]
            raw_inputs = [
                value for value in direct_inputs if value.startswith("restoration/inherited-")
            ]
            expected_occurrences = [
                (
                    "Axiomatic Set Theory",
                    "restoration/inherited-10060-10088.tex",
                    "SRC-10060-10088",
                )
            ]
            source_label_exact = sum(
                source.count(r"\label{part:set-theory}")
                for relative, source, provenance_id in surface
                if relative == "restoration/inherited-10060-10088.tex"
                and provenance_id == "SRC-10060-10088"
            ) == 1
            source_label_total = sum(
                source.count(r"\label{part:set-theory}")
                for _relative, source, _provenance_id in surface
            )
            records_valid = True
            for provenance_id in PART6_RESTORATION_IDS:
                record_path = root / f"spec/provenance/{provenance_id}.json"
                try:
                    record = restoration_checker.load_json(record_path)
                    restoration_checker.validate_record(record, record_path, root)
                except (OSError, restoration_checker.CheckFailure) as error:
                    records_valid = False
                    failures.append(
                        f"book source: p06 restoration record failed: {error}"
                    )
            if raw_inputs:
                failures.append("book source: p06 raw inherited input is forbidden")
            if not (
                part_occurrences == expected_occurrences
                and label_count == 0
                and source_label_exact
                and source_label_total == 1
                and restoration_inputs == expected_inputs
                and not raw_inputs
                and direct_inputs == expected_driver
                and direct_inputs.count(table_supplement) == 1
                and direct_inputs.count(ordinal_supplement) == 1
                and direct_inputs.count(choice_supplement) == 1
                and direct_inputs.count(forcing_vocabulary) == 1
                and direct_inputs.count(constructibility_supplement) == 1
                and direct_inputs.count(variants_supplement) == 1
                and direct_inputs.count(arithmetic_supplement) == 1
                and records_valid
            ):
                failures.append(
                    "book source: p06 must classify the exact direct public Part VI "
                    "with twenty-three-wrapper order and governed OPEN addition seams"
                )
            continue
        if part_id == "p07":
            driver_source = surface[0][1]
            public_binding = (
                r"\part{Proof Theory, Lambda Calculi, and Higher-Order Logic}"
                r"\label{part:p07}"
            )
            expected_inputs = [
                f"restoration/scope-{provenance_id}"
                for provenance_id in PART7_RESTORATION_IDS
            ]
            calculus_supplement = "parts/p07/calculi-and-derivability-supplement"
            cut_supplement = "parts/p07/cut-elimination-and-interpolation-supplement"
            normalization_supplement = "parts/p07/normalization-and-curry-howard-supplement"
            arithmetic_supplement = "parts/p07/arithmetic-proof-theory-supplement"
            expected_driver = (
                expected_inputs[:8]
                + [calculus_supplement]
                + expected_inputs[8:14]
                + [
                    cut_supplement,
                    *expected_inputs[14:],
                    normalization_supplement,
                    "parts/p07/lambda-calculi-and-type-theories",
                    arithmetic_supplement,
                    "parts/p07/functional-interpretations",
                    "parts/p07/structural-extensions",
                    "parts/p07/proof-complexity",
                ]
            )
            direct_inputs = [
                match.group(1).strip().removesuffix(".tex")
                for match in re.finditer(r"\\input\s*\{([^{}]+)\}", driver_source)
            ]
            restoration_inputs = [
                value for value in direct_inputs
                if value.startswith("restoration/scope-")
            ]
            raw_inputs = [
                value for value in direct_inputs
                if value.startswith("restoration/inherited-")
            ]
            expected_occurrences = [
                (
                    "Proof Theory, Lambda Calculi, and Higher-Order Logic",
                    "parts/p07.tex",
                    None,
                ),
                (
                    "Proof Theory",
                    "restoration/inherited-11354-11413.tex",
                    "SRC-11354-11413",
                ),
            ]
            source_label_exact = sum(
                source.count(r"\label{part:proof-theory}")
                for relative, source, provenance_id in surface
                if relative == "restoration/inherited-11354-11413.tex"
                and provenance_id == "SRC-11354-11413"
            ) == 1
            source_label_total = sum(
                source.count(r"\label{part:proof-theory}")
                for _relative, source, _provenance_id in surface
            )
            records_valid = True
            for provenance_id in PART7_RESTORATION_IDS:
                record_path = root / f"spec/provenance/{provenance_id}.json"
                try:
                    record = restoration_checker.load_json(record_path)
                    restoration_checker.validate_record(record, record_path, root)
                except (OSError, restoration_checker.CheckFailure) as error:
                    records_valid = False
                    failures.append(
                        f"book source: p07 restoration record failed: {error}"
                    )
            if raw_inputs:
                failures.append("book source: p07 raw inherited input is forbidden")
            if not (
                part_occurrences == expected_occurrences
                and driver_source.count(public_binding) == 1
                and direct_binding
                and label_count == 1
                and source_label_exact
                and source_label_total == 1
                and restoration_inputs == expected_inputs
                and not raw_inputs
                and direct_inputs == expected_driver
                and direct_inputs.count(calculus_supplement) == 1
                and direct_inputs.count(cut_supplement) == 1
                and direct_inputs.count(normalization_supplement) == 1
                and direct_inputs.count(arithmetic_supplement) == 1
                and records_valid
            ):
                failures.append(
                    "book source: p07 must classify exactly one public Part VII "
                    "and the governed subordinate source Part SRC-11354-11413, "
                    "with nineteen-wrapper order and four bounded OPEN addition seams"
                )
            continue
        if part_id == "p08":
            driver_source = surface[0][1]
            expected_inputs = [
                f"restoration/scope-{provenance_id}"
                for provenance_id in PART8_RESTORATION_IDS
            ]
            intuitionistic_supplement = "parts/p08/intuitionistic-supplement"
            modal_supplement = "parts/p08/modal-logics-supplement"
            temporal_supplement = "parts/p08/temporal-epistemic-supplement"
            many_supplement = "parts/p08/many-valued-supplement"
            relevance_supplement = "parts/p08/relevance-linear-supplement"
            expected_driver = (
                expected_inputs[:9]
                + [intuitionistic_supplement]
                + expected_inputs[9:22]
                + [modal_supplement, temporal_supplement]
                + ["parts/p08/conditionals-deontic-free"]
                + expected_inputs[22:28]
                + [many_supplement]
                + expected_inputs[28:]
                + [
                    relevance_supplement,
                    "parts/p08/paraconsistent-and-nonmonotonic",
                    "parts/p08/further-reading",
                ]
            )
            direct_inputs = [
                match.group(1).strip().removesuffix(".tex")
                for match in re.finditer(r"\\input\s*\{([^{}]+)\}", driver_source)
            ]
            restoration_inputs = [
                value for value in direct_inputs
                if value.startswith("restoration/scope-")
            ]
            raw_inputs = [
                value for value in direct_inputs
                if value.startswith("restoration/inherited-")
            ]
            expected_occurrences = [
                (
                    "Nonclassical Logic",
                    "restoration/inherited-12970-12988.tex",
                    "SRC-12970-12988",
                ),
            ]
            source_label_exact = sum(
                source.count(r"\label{part:nonclassical}")
                for relative, source, provenance_id in surface
                if relative == "restoration/inherited-12970-12988.tex"
                and provenance_id == "SRC-12970-12988"
            ) == 1
            source_label_total = sum(
                source.count(r"\label{part:nonclassical}")
                for _relative, source, _provenance_id in surface
            )
            records_valid = True
            for provenance_id in PART8_RESTORATION_IDS:
                record_path = root / f"spec/provenance/{provenance_id}.json"
                try:
                    record = restoration_checker.load_json(record_path)
                    restoration_checker.validate_record(record, record_path, root)
                except (OSError, restoration_checker.CheckFailure) as error:
                    records_valid = False
                    failures.append(
                        f"book source: p08 restoration record failed: {error}"
                    )
            if raw_inputs:
                failures.append("book source: p08 raw inherited input is forbidden")
            if not (
                part_occurrences == expected_occurrences
                and label_count == 0
                and not direct_binding
                and source_label_exact
                and source_label_total == 1
                and restoration_inputs == expected_inputs
                and not raw_inputs
                and direct_inputs == expected_driver
                and direct_inputs.count(intuitionistic_supplement) == 1
                and direct_inputs.count(modal_supplement) == 1
                and direct_inputs.count(temporal_supplement) == 1
                and direct_inputs.count(many_supplement) == 1
                and direct_inputs.count(relevance_supplement) == 1
                and "parts/p08/intuitionistic-and-intermediate" not in direct_inputs
                and "parts/p08/modal-logics" not in direct_inputs
                and "parts/p08/temporal-dynamic-epistemic" not in direct_inputs
                and "parts/p08/many-valued-and-fuzzy" not in direct_inputs
                and "parts/p08/substructural" not in direct_inputs
                and "generated/audit-p08" not in direct_inputs
                and records_valid
            ):
                failures.append(
                    "book source: p08 must classify the governed public Part VIII "
                    "with exact source label, forty-wrapper order, and five "
                    "bounded OPEN addition seams"
                )
            continue
        if part_id == "p12":
            driver_source = surface[0][1]
            public_binding = (
                r"\part{Automation, Mechanization, and Formal Practice}"
                r"\label{part:p12}"
            )
            expected_inputs = [
                f"restoration/scope-{provenance_id}"
                for provenance_id in PART12_RESTORATION_IDS
            ]
            supplement = "parts/p12/formal-practice-supplement"
            aggregator = "parts/p12/automation-and-mechanization"
            expected_driver = (
                expected_inputs[:5]
                + [supplement]
                + expected_inputs[5:]
                + [aggregator]
            )
            direct_inputs = [
                match.group(1).strip().removesuffix(".tex")
                for match in re.finditer(r"\\input\s*\{([^{}]+)\}", driver_source)
            ]
            restoration_inputs = [
                value for value in direct_inputs
                if value.startswith("restoration/scope-")
            ]
            raw_inputs = [
                value for value in direct_inputs
                if value.startswith("restoration/inherited-")
            ]
            expected_occurrences = [
                (
                    "Automation, Mechanization, and Formal Practice",
                    "parts/p12.tex",
                    None,
                ),
                (
                    "Formal Practice, Automation, and Verification",
                    "restoration/inherited-14095-14146.tex",
                    "SRC-14095-14146",
                ),
            ]
            surface_paths = {relative for relative, _source, _provenance in surface}
            records_valid = True
            for provenance_id in PART12_RESTORATION_IDS:
                record_path = root / f"spec/provenance/{provenance_id}.json"
                try:
                    record = restoration_checker.load_json(record_path)
                    restoration_checker.validate_record(record, record_path, root)
                except (OSError, restoration_checker.CheckFailure) as error:
                    records_valid = False
                    failures.append(
                        f"book source: p12 restoration record failed: {error}"
                    )
            if raw_inputs:
                failures.append("book source: p12 raw inherited input is forbidden")
            if not (
                part_occurrences == expected_occurrences
                and driver_source.count(public_binding) == 1
                and direct_binding
                and label_count == 1
                and restoration_inputs == expected_inputs
                and direct_inputs == expected_driver
                and not raw_inputs
                and direct_inputs.count(supplement) == 1
                and direct_inputs.count(aggregator) == 1
                and "parts/p12/formal-workflow.tex" not in surface_paths
                and "generated/audit-p12.tex" not in surface_paths
                and records_valid
            ):
                failures.append(
                    "book source: p12 must classify exactly one public Part XII "
                    "and the label-less governed subordinate source Part "
                    "SRC-14095-14146, with forty-one-wrapper order, all four "
                    "literal blank separators, local source Appendices A--F/D.6, and two "
                    "bounded OPEN addition seams"
                )
            continue
        if (
            part_titles != [title]
            or not (
                (direct_binding and label_count == 1)
                or source_exact_binding
            )
        ):
            failures.append(
                f"book source: {part_id} transitive surface must contain exactly "
                f"one part titled {title!r}; direct headings require exactly one "
                f"bound label part:{part_id}, while the exact inherited Part I "
                "heading remains byte-unaltered"
            )
    return failures


def pdf_details(path: Path) -> tuple[int, str | None]:
    try:
        from pypdf import PdfReader
    except ImportError:
        bundled = (
            Path.home()
            / ".cache/codex-runtimes/codex-primary-runtime/dependencies/native"
            / "poppler/Library/bin/pdfinfo.exe"
        )
        pdfinfo = str(bundled) if bundled.is_file() else shutil.which("pdfinfo")
        if pdfinfo is None:
            raise RuntimeError("PDF inspection requires pypdf or pdfinfo")
        completed = subprocess.run(
            [pdfinfo, str(path)],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        if completed.returncode != 0:
            raise RuntimeError(completed.stderr.strip() or "pdfinfo failed")
        pages = re.search(r"^Pages:\s*(\d+)\s*$", completed.stdout, re.MULTILINE)
        title = re.search(r"^Title:\s*(.*?)\s*$", completed.stdout, re.MULTILINE)
        if pages is None:
            raise RuntimeError("pdfinfo output has no page count")
        return int(pages.group(1)), title.group(1) if title and title.group(1) else None
    reader = PdfReader(str(path))
    metadata = reader.metadata
    return len(reader.pages), metadata.title if metadata is not None else None


def validate_live_files(manifest: dict[str, Any], root: Path) -> list[str]:
    failures: list[str] = []
    authority_record = manifest.get("internal_authority_evidence")
    if not isinstance(authority_record, dict):
        return ["internal authority: record is unavailable"]
    inherited_recorded = authority_record.get("inherited_corpus_manifest")
    if not isinstance(inherited_recorded, str) or not is_canonical_relative_path(
        inherited_recorded
    ):
        return ["internal authority: manifest path is invalid"]
    try:
        inherited_path = resolve_inside(root, inherited_recorded)
        inherited = load_json(inherited_path)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        failures.append(f"internal authority: {error}")
        inherited = {}
    if inherited != FROZEN_INHERITED_MANIFEST:
        failures.append("internal authority: frozen corpus manifest values have drifted")
    else:
        for kind in ("tex", "pdf"):
            record = inherited[kind]
            path = resolve_inside(root, record["path"])
            if not path.is_file():
                failures.append(f"internal authority: missing {record['path']}")
                continue
            if path.stat().st_size != record["bytes"]:
                failures.append(f"internal authority: byte count drifted for {record['path']}")
            if sha256(path) != record["sha256"]:
                failures.append(f"internal authority: digest drifted for {record['path']}")
            if kind == "tex":
                line_count = len(path.read_bytes().splitlines())
                if line_count != record["lines"]:
                    failures.append(f"internal authority: line count drifted for {record['path']}")
            else:
                try:
                    pages, _ = pdf_details(path)
                except Exception as error:
                    failures.append(f"internal authority: unable to inspect PDF: {error}")
                else:
                    if pages != record["pages"]:
                        failures.append("internal authority: inherited PDF page count drifted")

    public = manifest.get("public_artifact")
    if not isinstance(public, dict):
        return failures + ["public artifact: record is unavailable"]
    try:
        public_path = resolve_inside(root, str(public.get("path")))
    except ValueError as error:
        return failures + [f"public artifact: {error}"]
    if not public_path.is_file():
        failures.append(f"public artifact: missing {PUBLIC_PATH}")
        return failures
    observed = public.get("observed")
    if not isinstance(observed, dict):
        return failures + ["public artifact: observed record is unavailable"]
    try:
        pages, title = pdf_details(public_path)
    except Exception as error:
        failures.append(f"public artifact: unable to inspect PDF: {error}")
        return failures
    actual = {
        "bytes": public_path.stat().st_size,
        "pages": pages,
        "sha256": sha256(public_path),
    }
    for field, value in actual.items():
        if observed.get(field) != value:
            failures.append(
                f"public artifact: observed {field} {observed.get(field)!r}, actual {value!r}"
            )
    if title != BOOK_TITLE:
        failures.append(
            f"public artifact: PDF metadata title {title!r}, expected {BOOK_TITLE!r}"
        )

    release = manifest.get("final_release_evidence")
    if isinstance(release, dict):
        for path_field, hash_field in (
            ("readiness_manifest_path", "readiness_manifest_sha256"),
            ("user_final_acceptance_path", "user_final_acceptance_sha256"),
        ):
            recorded_path = release.get(path_field)
            if not isinstance(recorded_path, str):
                continue
            path = resolve_inside(root, recorded_path)
            if not path.is_file():
                failures.append(f"final release: missing {recorded_path}")
            elif sha256(path) != release.get(hash_field):
                failures.append(f"final release: digest drifted for {recorded_path}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest", type=Path, default=Path("spec/compendium-volume-manifest.json")
    )
    parser.add_argument("--repo-root", type=Path)
    parser.add_argument("--require-release-ready", action="store_true")
    parser.add_argument(
        "--require-expansions-ready",
        action="store_true",
        help="deprecated alias for --require-release-ready",
    )
    args = parser.parse_args()

    manifest_path = args.manifest.resolve()
    root = (
        args.repo_root.resolve()
        if args.repo_root is not None
        else manifest_path.parent.parent.resolve()
    )
    try:
        manifest = load_json(manifest_path)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print("publication manifest: FAIL")
        print(f"  {error}")
        return 1

    failures = validate_manifest_structure(manifest)
    if not failures:
        failures.extend(validate_live_files(manifest, root))
        failures.extend(validate_book_sources(root))
    public = manifest.get("public_artifact")
    ready = isinstance(public, dict) and public.get("release_ready") is True
    if (args.require_release_ready or args.require_expansions_ready) and not ready:
        failures.append("release gate: public artifact is still a construction draft")

    if failures:
        print("publication manifest: FAIL")
        for failure in failures:
            print(f"  {failure}")
        return 1
    print("publication manifest: PASS")
    print(f"public artifact: {BOOK_TITLE} at {PUBLIC_PATH}")
    print(f"publication status: {'RELEASE READY' if ready else 'CONSTRUCTION DRAFT'}")
    print("internal authority evidence: VERIFIED; NOT PART OF THE PUBLICATION")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Build the full-compendium coverage manifest from the acquired baseline.

The baseline is an attributed transcription of publisher, project, and
institutional taxonomies.  This generator performs no subject classification
and infers no handbook mapping.  It preserves source order, displayed titles,
hierarchy, repetitions, metadata, and URL order while assigning deterministic
administrative identifiers.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import sys
import tempfile
from collections import Counter
from dataclasses import dataclass, replace
from itertools import groupby
from pathlib import Path
from typing import Iterable, Iterator, TextIO


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = (
    REPO_ROOT / "spec" / "research" / "full-compendium-coverage-baseline.md"
)
DEFAULT_CSV = REPO_ROOT / "spec" / "full-compendium-coverage-manifest.csv"
DEFAULT_MARKDOWN = REPO_ROOT / "spec" / "full-compendium-coverage-manifest.md"

EXPECTED_SOURCE_COUNT = 68
EXPECTED_HIERARCHY_COUNT = 27979
EXPECTED_TOPIC_COUNT = 9134103
EXPECTED_ROW_COUNT = 9162150
EXPECTED_UNIQUE_URL_COUNT = 23765
EXPECTED_UNIQUE_NON_HTTPS_URL_COUNT = 5511
EXPECTED_UNIQUE_SCHEME_LESS_IDENTIFIER_COUNT = 20071
MAPPING_STATUS = "open/unmapped"
FROZEN_BASELINE_SHA256 = "b44701e82b987d03476652fc8aba987705221973a149d4439ad130de0484838f"

SOURCE_HEADING_RE = re.compile(
    r"^### (?P<source_id>SRC-\d{3}) — (?P<source_title>.+)$"
)
HIERARCHY_HEADING_RE = re.compile(
    r"^(?P<marks>#{4,6}) (?P<displayed_title>.+)$"
)
RETRIEVAL_DATE_RE = re.compile(
    r"^Retrieval date for every URL below: (?P<date>\d{4}-\d{2}-\d{2})\.$"
)
URL_RE = re.compile(r"https://[^\s]+")
ADMITTED_NON_HTTPS_SCHEME_RE = re.compile(
    r"^(?:https?|ftp|git|ssh|urn|mailto|doi|ark):", re.IGNORECASE
)
# Necessity: HTTPS-only extraction cannot preserve source-displayed HTTP and
# scheme-less locator forms. Definition: a non-HTTPS locator is the literal
# value in an explicitly numbered baseline metadata field whose displayed URI
# scheme is not HTTPS; currently retained schemes are HTTP, FTP, Git, SSH,
# URN, mailto, DOI, and ARK. A scheme-less identifier is the literal value in
# its explicitly named field.
# Standing: both are administrative source locators, not logical terms.
# Nonredundancy: neither is an HTTPS URL, and a scheme-less identifier is not a
# URL.  Use: both are emitted as ordered JSON fields and counted independently
# so generation fails if a recorded form disappears.
HTTPS_URL_RE = re.compile(
    r"^Exact HTTPS locator (?P<number>\d+): (?P<url>https://.+)$"
)
NON_HTTPS_URL_RE = re.compile(
    r"^Exact non-HTTPS locator (?P<number>\d+): (?P<url>.+)$"
)
SCHEME_LESS_IDENTIFIER_RE = re.compile(
    r"^Exact scheme-less identifier (?P<number>\d+): (?P<identifier>.+)$"
)

FIELDNAMES = (
    "stable_id",
    "record_type",
    "source_id",
    "source_title",
    "source_metadata",
    "retrieved_granularity",
    "hierarchy_path",
    "parent_stable_id",
    "displayed_title",
    "source_https_urls",
    "source_non_https_urls",
    "source_scheme_less_identifiers",
    "retrieval_date",
    "mapping_status",
)

# These source-level fields are stored once on the source row.  An empty child
# cell means "resolve through source_id"; it is intentionally distinct from a
# source row's literal JSON empty list, ``[]``.
SOURCE_JSON_FIELDS = (
    "source_metadata",
    "source_https_urls",
    "source_non_https_urls",
    "source_scheme_less_identifiers",
)
SOURCE_ONLY_FIELDS = (
    "source_metadata",
    "retrieved_granularity",
    "source_https_urls",
    "source_non_https_urls",
    "source_scheme_less_identifiers",
)


def canonical_json(values: tuple[str, ...]) -> str:
    return json.dumps(values, ensure_ascii=False, separators=(",", ":"))


@dataclass(frozen=True)
class SourceBlock:
    source_id: str
    source_title: str
    metadata: tuple[str, ...]
    retrieved_granularity: str
    https_urls: tuple[str, ...]
    non_https_urls: tuple[str, ...]
    scheme_less_identifiers: tuple[str, ...]
    content_lines: tuple[tuple[int, str], ...]


@dataclass(frozen=True)
class ManifestRecord:
    stable_id: str
    record_type: str
    source_id: str
    source_title: str
    source_metadata: tuple[str, ...]
    retrieved_granularity: str
    hierarchy_path: tuple[str, ...]
    parent_stable_id: str
    displayed_title: str
    source_https_urls: tuple[str, ...]
    source_non_https_urls: tuple[str, ...]
    source_scheme_less_identifiers: tuple[str, ...]
    retrieval_date: str
    mapping_status: str = MAPPING_STATUS

    def csv_row(self) -> dict[str, str]:
        # Source-level metadata and locator lists are emitted on the source row
        # once. Child rows point to that source through ``source_id``. Repeating
        # the same large ordered lists on every child row is not additional
        # source evidence and became non-generable as exact acquisition grew.
        source_only = self.record_type == "source"
        return {
            "stable_id": self.stable_id,
            "record_type": self.record_type,
            "source_id": self.source_id,
            "source_title": self.source_title,
            "source_metadata": canonical_json(self.source_metadata) if source_only else "",
            "retrieved_granularity": self.retrieved_granularity if source_only else "",
            "hierarchy_path": canonical_json(self.hierarchy_path),
            "parent_stable_id": self.parent_stable_id,
            "displayed_title": self.displayed_title,
            "source_https_urls": canonical_json(self.source_https_urls) if source_only else "",
            "source_non_https_urls": (
                canonical_json(self.source_non_https_urls) if source_only else ""
            ),
            "source_scheme_less_identifiers": (
                canonical_json(self.source_scheme_less_identifiers) if source_only else ""
            ),
            "retrieval_date": self.retrieval_date,
            "mapping_status": self.mapping_status,
        }


def relative_display(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return resolved.as_posix()


def read_utf8(path: Path) -> str:
    raw = path.read_bytes()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"{path}: input is not UTF-8: {exc}") from exc


def retrieval_date(lines: list[str], path: Path) -> str:
    dates = [
        match.group("date")
        for line in lines
        if (match := RETRIEVAL_DATE_RE.fullmatch(line)) is not None
    ]
    if len(dates) != 1:
        raise ValueError(
            f"{path}: expected exactly one global retrieval date, found {len(dates)}"
        )
    return dates[0]


def source_ranges(lines: list[str], path: Path) -> list[tuple[int, int]]:
    starts = [
        index
        for index, line in enumerate(lines)
        if SOURCE_HEADING_RE.fullmatch(line) is not None
    ]
    if not starts:
        raise ValueError(f"{path}: no source headings found")

    terminators = [
        index for index, line in enumerate(lines) if line == "---" and index > starts[-1]
    ]
    if len(terminators) != 1:
        raise ValueError(
            f"{path}: expected one post-source terminator, found {len(terminators)}"
        )

    boundaries = starts[1:] + [terminators[0]]
    return list(zip(starts, boundaries, strict=True))


def ordered_https_occurrences(
    metadata: Iterable[str], path: Path, source_line: int
) -> tuple[str, ...]:
    """Return every HTTPS occurrence in its physical metadata order.

    Both source parsers need one rule that preserves interleaving between
    ordinary metadata URLs and explicitly numbered HTTPS rows.  Each numbered
    row contributes its URL at that row's position, while an ordinary row
    contributes every displayed HTTPS URL from left to right.  Numbering is an
    independent canonical-form check on the numbered subset and remains dense
    from 1 through N; it does not determine output order or remove repetitions.
    """

    numbered_https: list[tuple[int, str]] = []
    https_urls: list[str] = []
    for item in metadata:
        match = HTTPS_URL_RE.fullmatch(item)
        if match is not None:
            url = match.group("url")
            numbered_https.append((int(match.group("number")), url))
            https_urls.append(url)
            continue
        https_urls.extend(URL_RE.findall(item))

    expected_numbers = list(range(1, len(numbered_https) + 1))
    actual_numbers = [number for number, _ in numbered_https]
    if actual_numbers != expected_numbers:
        raise ValueError(
            f"{path}:{source_line}: HTTPS locator numbering is not exact and sequential"
        )
    if not https_urls:
        raise ValueError(f"{path}:{source_line}: source record has no HTTPS URL")
    return tuple(https_urls)


def parse_source_block(
    lines: list[str], start: int, end: int, path: Path
) -> SourceBlock:
    heading = SOURCE_HEADING_RE.fullmatch(lines[start])
    if heading is None:  # Defensive: source_ranges already checked this line.
        raise ValueError(f"{path}:{start + 1}: invalid source heading")

    source_id = heading.group("source_id")
    source_title = heading.group("source_title")
    metadata: list[str] = []
    content_lines: list[tuple[int, str]] = []
    retrieved_seen = False
    content_started = False

    for index in range(start + 1, end):
        line = lines[index]
        if not content_started:
            if line.startswith("- Retrieved granularity:"):
                if retrieved_seen:
                    raise ValueError(
                        f"{path}:{index + 1}: duplicate retrieved-granularity field"
                    )
                retrieved_seen = True

            if retrieved_seen and line == "":
                content_started = True
                continue

            if line == "":
                continue
            if not line.startswith("- "):
                raise ValueError(
                    f"{path}:{index + 1}: unexpected source-metadata line {line!r}"
                )
            metadata.append(line[2:])
            continue

        if line == "":
            continue
        if HIERARCHY_HEADING_RE.fullmatch(line) is not None or line.startswith("- "):
            content_lines.append((index + 1, line))
            continue
        raise ValueError(f"{path}:{index + 1}: unexpected source-content line {line!r}")

    if not retrieved_seen:
        raise ValueError(f"{path}:{start + 1}: missing retrieved-granularity field")
    if not content_started:
        raise ValueError(
            f"{path}:{start + 1}: source metadata is not separated from content"
        )

    granularity_fields = [
        item.removeprefix("Retrieved granularity:").strip()
        for item in metadata
        if item.startswith("Retrieved granularity:")
    ]
    if len(granularity_fields) != 1 or not granularity_fields[0]:
        raise ValueError(
            f"{path}:{start + 1}: expected one nonempty retrieved granularity"
        )

    https_urls = ordered_https_occurrences(metadata, path, start + 1)

    numbered_non_https = [
        (int(match.group("number")), match.group("url"))
        for item in metadata
        if (match := NON_HTTPS_URL_RE.fullmatch(item)) is not None
    ]
    expected_numbers = list(range(1, len(numbered_non_https) + 1))
    actual_numbers = [number for number, _ in numbered_non_https]
    if actual_numbers != expected_numbers:
        raise ValueError(
            f"{path}:{start + 1}: non-HTTPS locator numbering is not exact and sequential"
        )
    non_https_urls = tuple(url for _, url in numbered_non_https)
    numbered_scheme_less = [
        (int(match.group("number")), match.group("identifier"))
        for item in metadata
        if (match := SCHEME_LESS_IDENTIFIER_RE.fullmatch(item)) is not None
    ]
    expected_scheme_less_numbers = list(range(1, len(numbered_scheme_less) + 1))
    actual_scheme_less_numbers = [number for number, _ in numbered_scheme_less]
    if actual_scheme_less_numbers != expected_scheme_less_numbers:
        raise ValueError(
            f"{path}:{start + 1}: scheme-less locator numbering is not exact and sequential"
        )
    scheme_less_identifiers = tuple(
        identifier for _, identifier in numbered_scheme_less
    )
    return SourceBlock(
        source_id=source_id,
        source_title=source_title,
        metadata=tuple(metadata),
        retrieved_granularity=granularity_fields[0],
        https_urls=https_urls,
        non_https_urls=non_https_urls,
        scheme_less_identifiers=scheme_less_identifiers,
        content_lines=tuple(content_lines),
    )


def parse_blocks(lines: list[str], path: Path) -> list[SourceBlock]:
    blocks = [
        parse_source_block(lines, start, end, path)
        for start, end in source_ranges(lines, path)
    ]
    expected_ids = [f"SRC-{number:03d}" for number in range(1, len(blocks) + 1)]
    actual_ids = [block.source_id for block in blocks]
    if actual_ids != expected_ids:
        raise ValueError(
            f"{path}: source IDs are not exactly sequential: {actual_ids!r}"
        )
    return blocks


def records_for_block(block: SourceBlock, date: str) -> list[ManifestRecord]:
    source_path = (block.source_title,)
    records = [
        ManifestRecord(
            stable_id=block.source_id,
            record_type="source",
            source_id=block.source_id,
            source_title=block.source_title,
            source_metadata=block.metadata,
            retrieved_granularity=block.retrieved_granularity,
            hierarchy_path=source_path,
            parent_stable_id="",
            displayed_title=block.source_title,
            source_https_urls=block.https_urls,
            source_non_https_urls=block.non_https_urls,
            source_scheme_less_identifiers=block.scheme_less_identifiers,
            retrieval_date=date,
        )
    ]

    hierarchy_count = 0
    topic_count = 0
    # Stack entries are (Markdown heading level, stable ID, displayed title).
    hierarchy_stack: list[tuple[int, str, str]] = []

    for line_number, line in block.content_lines:
        heading = HIERARCHY_HEADING_RE.fullmatch(line)
        if heading is not None:
            level = len(heading.group("marks"))
            title = heading.group("displayed_title")
            while hierarchy_stack and hierarchy_stack[-1][0] >= level:
                hierarchy_stack.pop()
            if hierarchy_stack and level > hierarchy_stack[-1][0] + 1:
                raise ValueError(
                    f"{block.source_id}:{line_number}: hierarchy level jumps from "
                    f"{hierarchy_stack[-1][0]} to {level}"
                )
            if not hierarchy_stack and level != 4:
                raise ValueError(
                    f"{block.source_id}:{line_number}: top hierarchy heading is level {level}"
                )

            hierarchy_count += 1
            stable_id = f"{block.source_id}-H{hierarchy_count:03d}"
            parent_id = hierarchy_stack[-1][1] if hierarchy_stack else block.source_id
            hierarchy_stack.append((level, stable_id, title))
            records.append(
                ManifestRecord(
                    stable_id=stable_id,
                    record_type="hierarchy",
                    source_id=block.source_id,
                    source_title=block.source_title,
                    source_metadata=block.metadata,
                    retrieved_granularity=block.retrieved_granularity,
                    hierarchy_path=source_path
                    + tuple(item[2] for item in hierarchy_stack),
                    parent_stable_id=parent_id,
                    displayed_title=title,
                    source_https_urls=block.https_urls,
                    source_non_https_urls=block.non_https_urls,
                    source_scheme_less_identifiers=block.scheme_less_identifiers,
                    retrieval_date=date,
                )
            )
            continue

        if not line.startswith("- "):
            raise ValueError(
                f"{block.source_id}:{line_number}: unrecognized content line {line!r}"
            )
        title = line[2:]
        if not title:
            raise ValueError(f"{block.source_id}:{line_number}: empty topic title")
        topic_count += 1
        stable_id = f"{block.source_id}-T{topic_count:03d}"
        parent_id = hierarchy_stack[-1][1] if hierarchy_stack else block.source_id
        records.append(
            ManifestRecord(
                stable_id=stable_id,
                record_type="topic",
                source_id=block.source_id,
                source_title=block.source_title,
                source_metadata=block.metadata,
                retrieved_granularity=block.retrieved_granularity,
                hierarchy_path=source_path
                + tuple(item[2] for item in hierarchy_stack)
                + (title,),
                parent_stable_id=parent_id,
                displayed_title=title,
                source_https_urls=block.https_urls,
                source_non_https_urls=block.non_https_urls,
                source_scheme_less_identifiers=block.scheme_less_identifiers,
                retrieval_date=date,
            )
        )

    return records


def validate_records(records: list[ManifestRecord]) -> None:
    counts = Counter(record.record_type for record in records)
    expected_counts = {
        "source": EXPECTED_SOURCE_COUNT,
        "hierarchy": EXPECTED_HIERARCHY_COUNT,
        "topic": EXPECTED_TOPIC_COUNT,
    }
    if dict(counts) != expected_counts:
        raise ValueError(f"record-type counts {dict(counts)!r}, expected {expected_counts!r}")
    if len(records) != EXPECTED_ROW_COUNT:
        raise ValueError(
            f"manifest has {len(records)} rows, expected {EXPECTED_ROW_COUNT}"
        )

    by_id = {record.stable_id: record for record in records}
    if len(by_id) != len(records):
        duplicates = [
            stable_id
            for stable_id, count in Counter(
                record.stable_id for record in records
            ).items()
            if count > 1
        ]
        raise ValueError(f"duplicate stable IDs: {duplicates!r}")

    source_records = {
        record.source_id: record for record in records if record.record_type == "source"
    }
    for record in records:
        if record.mapping_status != MAPPING_STATUS:
            raise ValueError(
                f"{record.stable_id}: mapping status is {record.mapping_status!r}"
            )
        if not record.hierarchy_path:
            raise ValueError(f"{record.stable_id}: empty hierarchy path")
        if record.hierarchy_path[-1] != record.displayed_title:
            raise ValueError(
                f"{record.stable_id}: hierarchy path does not end in displayed title"
            )
        source = source_records.get(record.source_id)
        if source is None:
            raise ValueError(f"{record.stable_id}: missing source {record.source_id}")
        if record.source_title != source.source_title:
            raise ValueError(f"{record.stable_id}: source-title mismatch")
        if record.source_metadata != source.source_metadata:
            raise ValueError(f"{record.stable_id}: source-metadata mismatch")
        if record.retrieved_granularity != source.retrieved_granularity:
            raise ValueError(f"{record.stable_id}: granularity mismatch")
        if record.source_https_urls != source.source_https_urls:
            raise ValueError(f"{record.stable_id}: source-HTTPS-URL mismatch")
        if record.source_non_https_urls != source.source_non_https_urls:
            raise ValueError(f"{record.stable_id}: source-non-HTTPS-URL mismatch")
        if (
            record.source_scheme_less_identifiers
            != source.source_scheme_less_identifiers
        ):
            raise ValueError(f"{record.stable_id}: scheme-less-identifier mismatch")
        if record.retrieval_date != source.retrieval_date:
            raise ValueError(f"{record.stable_id}: retrieval-date mismatch")

        if record.record_type == "source":
            if record.stable_id != record.source_id:
                raise ValueError(f"{record.stable_id}: source stable ID mismatch")
            if record.parent_stable_id:
                raise ValueError(f"{record.stable_id}: source has a parent")
            if record.hierarchy_path != (record.source_title,):
                raise ValueError(f"{record.stable_id}: source path is not canonical")
            continue

        if not record.parent_stable_id:
            raise ValueError(f"{record.stable_id}: non-source record has no parent")
        parent = by_id.get(record.parent_stable_id)
        if parent is None:
            raise ValueError(
                f"{record.stable_id}: missing parent {record.parent_stable_id}"
            )
        if parent.source_id != record.source_id:
            raise ValueError(f"{record.stable_id}: parent belongs to another source")
        if parent.record_type == "topic":
            raise ValueError(f"{record.stable_id}: topic cannot be a parent")
        if record.hierarchy_path[:-1] != parent.hierarchy_path:
            raise ValueError(f"{record.stable_id}: hierarchy path disagrees with parent")

    unique_urls = {
        url
        for record in records
        if record.record_type == "source"
        for url in record.source_https_urls
    }
    if len(unique_urls) != EXPECTED_UNIQUE_URL_COUNT:
        raise ValueError(
            f"manifest has {len(unique_urls)} unique HTTPS URLs, "
            f"expected {EXPECTED_UNIQUE_URL_COUNT}"
        )
    if any(not url.startswith("https://") for url in unique_urls):
        raise ValueError("source URL set contains a non-HTTPS URL")

    unique_non_https_urls = {
        url
        for record in records
        if record.record_type == "source"
        for url in record.source_non_https_urls
    }
    if len(unique_non_https_urls) != EXPECTED_UNIQUE_NON_HTTPS_URL_COUNT:
        raise ValueError(
            f"manifest has {len(unique_non_https_urls)} unique non-HTTPS URLs, "
            f"expected {EXPECTED_UNIQUE_NON_HTTPS_URL_COUNT}"
        )
    if any(
        ADMITTED_NON_HTTPS_SCHEME_RE.match(url) is None
        or url.lower().startswith("https:")
        for url in unique_non_https_urls
    ):
        raise ValueError("non-HTTPS source locator set contains an unsupported scheme")

    unique_scheme_less_identifiers = {
        identifier
        for record in records
        if record.record_type == "source"
        for identifier in record.source_scheme_less_identifiers
    }
    if (
        len(unique_scheme_less_identifiers)
        != EXPECTED_UNIQUE_SCHEME_LESS_IDENTIFIER_COUNT
    ):
        raise ValueError(
            "manifest has "
            f"{len(unique_scheme_less_identifiers)} unique scheme-less identifiers, "
            f"expected {EXPECTED_UNIQUE_SCHEME_LESS_IDENTIFIER_COUNT}"
        )
    # The acquisition ledger's explicit scheme-less field controls standing.
    # Some literal archival identifiers begin with characters such as ``urn:``
    # or ``ark:`` without the source assigning them locator standing.  Moving
    # those values to the URI field here would normalize the source record.


def expected_source_only_values(record: ManifestRecord) -> dict[str, str]:
    """Return the exact source-row serialization for inherited source fields."""

    return {
        "source_metadata": canonical_json(record.source_metadata),
        "retrieved_granularity": record.retrieved_granularity,
        "source_https_urls": canonical_json(record.source_https_urls),
        "source_non_https_urls": canonical_json(record.source_non_https_urls),
        "source_scheme_less_identifiers": canonical_json(
            record.source_scheme_less_identifiers
        ),
    }


def validate_sparse_projection_declarations() -> None:
    if tuple(SOURCE_ONLY_FIELDS) != (
        "source_metadata",
        "retrieved_granularity",
        "source_https_urls",
        "source_non_https_urls",
        "source_scheme_less_identifiers",
    ):
        raise ValueError("source-only field declaration drifted")
    if not set(SOURCE_JSON_FIELDS).issubset(SOURCE_ONLY_FIELDS):
        raise ValueError("source JSON fields are not all declared source-only")
    if not set(SOURCE_ONLY_FIELDS).issubset(FIELDNAMES):
        raise ValueError("source-only fields are not all CSV fields")


def validate_sparse_projection(records: list[ManifestRecord]) -> None:
    """Prove that the CSV projection retains source data through an exact join."""

    validate_sparse_projection_declarations()
    if records and tuple(expected_source_only_values(records[0])) != SOURCE_ONLY_FIELDS:
        raise ValueError("source-only field declaration disagrees with serialization order")

    source_groups: dict[str, list[ManifestRecord]] = {}
    for record in records:
        if record.record_type == "source":
            source_groups.setdefault(record.source_id, []).append(record)

    for source_id, group in source_groups.items():
        if len(group) != 1:
            raise ValueError(
                f"{source_id}: sparse projection requires exactly one source row, "
                f"found {len(group)}"
            )
        if group[0].stable_id != source_id:
            raise ValueError(
                f"{group[0].stable_id}: source stable ID does not equal {source_id}"
            )

    join_attributes = (
        "source_title",
        "source_metadata",
        "retrieved_granularity",
        "source_https_urls",
        "source_non_https_urls",
        "source_scheme_less_identifiers",
        "retrieval_date",
    )
    for record in records:
        row = record.csv_row()
        if tuple(row) != FIELDNAMES:
            raise ValueError(f"{record.stable_id}: CSV fields or field order drifted")

        if record.record_type == "source":
            expected = expected_source_only_values(record)
            for field in SOURCE_ONLY_FIELDS:
                if row[field] != expected[field]:
                    raise ValueError(
                        f"{record.stable_id}: {field} source-row serialization drifted"
                    )
            if not row["retrieved_granularity"]:
                raise ValueError(
                    f"{record.stable_id}: source row has empty retrieved granularity"
                )
            if any(not row[field] for field in SOURCE_JSON_FIELDS):
                raise ValueError(
                    f"{record.stable_id}: source row has an empty source JSON field"
                )
            continue

        nonblank = [field for field in SOURCE_ONLY_FIELDS if row[field] != ""]
        if nonblank:
            raise ValueError(
                f"{record.stable_id}: child row repeats source-only fields {nonblank!r}"
            )

        group = source_groups.get(record.source_id, [])
        if len(group) != 1:
            raise ValueError(
                f"{record.stable_id}: source_id {record.source_id!r} resolves to "
                f"{len(group)} source rows"
            )
        source = group[0]
        for attribute in join_attributes:
            if getattr(record, attribute) != getattr(source, attribute):
                raise ValueError(
                    f"{record.stable_id}: {attribute} is not exactly recoverable "
                    f"through source_id {record.source_id}"
                )


def validate_sparse_projection_record(
    record: ManifestRecord, source: ManifestRecord
) -> None:
    """Validate one streamed row and its exact source-row resolution."""

    row = record.csv_row()
    if tuple(row) != FIELDNAMES:
        raise ValueError(f"{record.stable_id}: CSV fields or field order drifted")
    if source.record_type != "source" or source.stable_id != source.source_id:
        raise ValueError(
            f"{source.stable_id}: streamed source row does not key itself exactly"
        )
    if record.source_id != source.source_id:
        raise ValueError(
            f"{record.stable_id}: source_id {record.source_id!r} does not resolve "
            f"to streamed source row {source.source_id!r}"
        )

    if record.record_type == "source":
        if record is not source and record != source:
            raise ValueError(f"{record.stable_id}: source row resolution is ambiguous")
        expected = expected_source_only_values(source)
        for field in SOURCE_ONLY_FIELDS:
            if row[field] != expected[field]:
                raise ValueError(
                    f"{record.stable_id}: {field} source-row serialization drifted"
                )
        if not row["retrieved_granularity"]:
            raise ValueError(
                f"{record.stable_id}: source row has empty retrieved granularity"
            )
        if any(not row[field] for field in SOURCE_JSON_FIELDS):
            raise ValueError(
                f"{record.stable_id}: source row has an empty source JSON field"
            )
        return

    nonblank = [field for field in SOURCE_ONLY_FIELDS if row[field] != ""]
    if nonblank:
        raise ValueError(
            f"{record.stable_id}: child row repeats source-only fields {nonblank!r}"
        )
    for attribute in (
        "source_title",
        "source_metadata",
        "retrieved_granularity",
        "source_https_urls",
        "source_non_https_urls",
        "source_scheme_less_identifiers",
        "retrieval_date",
    ):
        if getattr(record, attribute) != getattr(source, attribute):
            raise ValueError(
                f"{record.stable_id}: {attribute} is not exactly recoverable "
                f"through source_id {record.source_id}"
            )


def streamed_lines(path: Path) -> Iterator[tuple[int, str]]:
    with path.open("r", encoding="utf-8", newline=None) as handle:
        for line_number, line in enumerate(handle, start=1):
            if line.endswith("\n"):
                line = line[:-1]
            yield line_number, line


def streamed_retrieval_date(path: Path) -> str:
    dates = [
        match.group("date")
        for _, line in streamed_lines(path)
        if (match := RETRIEVAL_DATE_RE.fullmatch(line)) is not None
    ]
    if len(dates) != 1:
        raise ValueError(
            f"{path}: expected exactly one global retrieval date, found {len(dates)}"
        )
    return dates[0]


def source_block_from_metadata(
    source_id: str,
    source_title: str,
    metadata: list[str],
    path: Path,
    source_line: int,
) -> SourceBlock:
    granularity_fields = [
        item.removeprefix("Retrieved granularity:").strip()
        for item in metadata
        if item.startswith("Retrieved granularity:")
    ]
    if len(granularity_fields) != 1 or not granularity_fields[0]:
        raise ValueError(
            f"{path}:{source_line}: expected one nonempty retrieved granularity"
        )

    https_urls = ordered_https_occurrences(metadata, path, source_line)

    numbered_non_https = [
        (int(match.group("number")), match.group("url"))
        for item in metadata
        if (match := NON_HTTPS_URL_RE.fullmatch(item)) is not None
    ]
    expected_numbers = list(range(1, len(numbered_non_https) + 1))
    actual_numbers = [number for number, _ in numbered_non_https]
    if actual_numbers != expected_numbers:
        raise ValueError(
            f"{path}:{source_line}: non-HTTPS locator numbering is not exact and sequential"
        )
    non_https_urls = tuple(url for _, url in numbered_non_https)
    numbered_scheme_less = [
        (int(match.group("number")), match.group("identifier"))
        for item in metadata
        if (match := SCHEME_LESS_IDENTIFIER_RE.fullmatch(item)) is not None
    ]
    expected_scheme_less_numbers = list(range(1, len(numbered_scheme_less) + 1))
    actual_scheme_less_numbers = [number for number, _ in numbered_scheme_less]
    if actual_scheme_less_numbers != expected_scheme_less_numbers:
        raise ValueError(
            f"{path}:{source_line}: scheme-less locator numbering is not exact and sequential"
        )
    scheme_less_identifiers = tuple(
        identifier for _, identifier in numbered_scheme_less
    )
    return SourceBlock(
        source_id=source_id,
        source_title=source_title,
        metadata=tuple(metadata),
        retrieved_granularity=granularity_fields[0],
        https_urls=https_urls,
        non_https_urls=non_https_urls,
        scheme_less_identifiers=scheme_less_identifiers,
        content_lines=(),
    )


def source_manifest_record(block: SourceBlock, date: str) -> ManifestRecord:
    return ManifestRecord(
        stable_id=block.source_id,
        record_type="source",
        source_id=block.source_id,
        source_title=block.source_title,
        source_metadata=block.metadata,
        retrieved_granularity=block.retrieved_granularity,
        hierarchy_path=(block.source_title,),
        parent_stable_id="",
        displayed_title=block.source_title,
        source_https_urls=block.https_urls,
        source_non_https_urls=block.non_https_urls,
        source_scheme_less_identifiers=block.scheme_less_identifiers,
        retrieval_date=date,
    )


def iter_manifest_records(path: Path, date: str) -> Iterator[ManifestRecord]:
    """Parse and emit one manifest row at a time in exact baseline order."""

    source_id = ""
    source_title = ""
    source_line = 0
    source_number = 0
    metadata: list[str] = []
    retrieved_seen = False
    content_started = False
    block: SourceBlock | None = None
    source_record: ManifestRecord | None = None
    hierarchy_stack: list[tuple[int, str, str]] = []
    hierarchy_count = 0
    topic_count = 0
    terminator_count = 0
    retrieval_count = 0

    for line_number, line in streamed_lines(path):
        retrieval_match = RETRIEVAL_DATE_RE.fullmatch(line)
        if retrieval_match is not None:
            retrieval_count += 1
            if retrieval_match.group("date") != date:
                raise ValueError(
                    f"{path}:{line_number}: retrieval date changed during generation"
                )

        heading = SOURCE_HEADING_RE.fullmatch(line)
        if heading is not None:
            if terminator_count:
                raise ValueError(
                    f"{path}:{line_number}: source heading occurs after post-source terminator"
                )
            if source_id and not content_started:
                raise ValueError(
                    f"{path}:{source_line}: source metadata is not separated from content"
                )

            source_number += 1
            expected_id = f"SRC-{source_number:03d}"
            actual_id = heading.group("source_id")
            if actual_id != expected_id:
                raise ValueError(
                    f"{path}:{line_number}: source ID is {actual_id}, expected {expected_id}"
                )
            source_id = actual_id
            source_title = heading.group("source_title")
            source_line = line_number
            metadata = []
            retrieved_seen = False
            content_started = False
            block = None
            source_record = None
            hierarchy_stack = []
            hierarchy_count = 0
            topic_count = 0
            continue

        if not source_id:
            if terminator_count and line == "---":
                terminator_count += 1
            continue

        if not content_started:
            if line.startswith("- Retrieved granularity:"):
                if retrieved_seen:
                    raise ValueError(
                        f"{path}:{line_number}: duplicate retrieved-granularity field"
                    )
                retrieved_seen = True

            if retrieved_seen and line == "":
                content_started = True
                block = source_block_from_metadata(
                    source_id, source_title, metadata, path, source_line
                )
                source_record = source_manifest_record(block, date)
                validate_sparse_projection_record(source_record, source_record)
                yield source_record
                continue

            if line == "":
                continue
            if not line.startswith("- "):
                raise ValueError(
                    f"{path}:{line_number}: unexpected source-metadata line {line!r}"
                )
            metadata.append(line[2:])
            continue

        if line == "---":
            terminator_count += 1
            source_id = ""
            continue
        if line == "":
            continue
        if block is None or source_record is None:
            raise ValueError(f"{path}:{line_number}: source record was not initialized")

        hierarchy = HIERARCHY_HEADING_RE.fullmatch(line)
        if hierarchy is not None:
            level = len(hierarchy.group("marks"))
            title = hierarchy.group("displayed_title")
            while hierarchy_stack and hierarchy_stack[-1][0] >= level:
                hierarchy_stack.pop()
            if hierarchy_stack and level > hierarchy_stack[-1][0] + 1:
                raise ValueError(
                    f"{block.source_id}:{line_number}: hierarchy level jumps from "
                    f"{hierarchy_stack[-1][0]} to {level}"
                )
            if not hierarchy_stack and level != 4:
                raise ValueError(
                    f"{block.source_id}:{line_number}: top hierarchy heading is level {level}"
                )

            hierarchy_count += 1
            stable_id = f"{block.source_id}-H{hierarchy_count:03d}"
            parent_id = hierarchy_stack[-1][1] if hierarchy_stack else block.source_id
            hierarchy_stack.append((level, stable_id, title))
            record = ManifestRecord(
                stable_id=stable_id,
                record_type="hierarchy",
                source_id=block.source_id,
                source_title=block.source_title,
                source_metadata=block.metadata,
                retrieved_granularity=block.retrieved_granularity,
                hierarchy_path=(block.source_title,)
                + tuple(item[2] for item in hierarchy_stack),
                parent_stable_id=parent_id,
                displayed_title=title,
                source_https_urls=block.https_urls,
                source_non_https_urls=block.non_https_urls,
                source_scheme_less_identifiers=block.scheme_less_identifiers,
                retrieval_date=date,
            )
            validate_sparse_projection_record(record, source_record)
            yield record
            continue

        if not line.startswith("- "):
            raise ValueError(
                f"{block.source_id}:{line_number}: unrecognized content line {line!r}"
            )
        title = line[2:]
        if not title:
            raise ValueError(f"{block.source_id}:{line_number}: empty topic title")
        topic_count += 1
        stable_id = f"{block.source_id}-T{topic_count:03d}"
        parent_id = hierarchy_stack[-1][1] if hierarchy_stack else block.source_id
        record = ManifestRecord(
            stable_id=stable_id,
            record_type="topic",
            source_id=block.source_id,
            source_title=block.source_title,
            source_metadata=block.metadata,
            retrieved_granularity=block.retrieved_granularity,
            hierarchy_path=(block.source_title,)
            + tuple(item[2] for item in hierarchy_stack)
            + (title,),
            parent_stable_id=parent_id,
            displayed_title=title,
            source_https_urls=block.https_urls,
            source_non_https_urls=block.non_https_urls,
            source_scheme_less_identifiers=block.scheme_less_identifiers,
            retrieval_date=date,
        )
        validate_sparse_projection_record(record, source_record)
        yield record

    if not source_number:
        raise ValueError(f"{path}: no source headings found")
    if source_id:
        raise ValueError(f"{path}: expected one post-source terminator, found 0")
    if terminator_count != 1:
        raise ValueError(
            f"{path}: expected one post-source terminator, found {terminator_count}"
        )
    if retrieval_count != 1:
        raise ValueError(
            f"{path}: expected exactly one global retrieval date, found {retrieval_count}"
        )


@dataclass(frozen=True)
class ManifestStats:
    source_count: int
    hierarchy_count: int
    topic_count: int
    row_count: int
    unique_https_count: int
    unique_non_https_count: int
    unique_scheme_less_count: int


def scan_manifest(path: Path, date: str) -> ManifestStats:
    validate_sparse_projection_declarations()
    counts: Counter[str] = Counter()
    https_urls: set[str] = set()
    non_https_urls: set[str] = set()
    scheme_less_identifiers: set[str] = set()

    for record in iter_manifest_records(path, date):
        counts[record.record_type] += 1
        if record.mapping_status != MAPPING_STATUS:
            raise ValueError(
                f"{record.stable_id}: mapping status is {record.mapping_status!r}"
            )
        if record.record_type == "source":
            https_urls.update(record.source_https_urls)
            non_https_urls.update(record.source_non_https_urls)
            scheme_less_identifiers.update(record.source_scheme_less_identifiers)

    expected_counts = {
        "source": EXPECTED_SOURCE_COUNT,
        "hierarchy": EXPECTED_HIERARCHY_COUNT,
        "topic": EXPECTED_TOPIC_COUNT,
    }
    if dict(counts) != expected_counts:
        raise ValueError(f"record-type counts {dict(counts)!r}, expected {expected_counts!r}")
    row_count = sum(counts.values())
    if row_count != EXPECTED_ROW_COUNT:
        raise ValueError(f"manifest has {row_count} rows, expected {EXPECTED_ROW_COUNT}")
    if len(https_urls) != EXPECTED_UNIQUE_URL_COUNT:
        raise ValueError(
            f"manifest has {len(https_urls)} unique HTTPS URLs, "
            f"expected {EXPECTED_UNIQUE_URL_COUNT}"
        )
    if any(not url.startswith("https://") for url in https_urls):
        raise ValueError("source URL set contains a non-HTTPS URL")
    if len(non_https_urls) != EXPECTED_UNIQUE_NON_HTTPS_URL_COUNT:
        raise ValueError(
            f"manifest has {len(non_https_urls)} unique non-HTTPS URLs, "
            f"expected {EXPECTED_UNIQUE_NON_HTTPS_URL_COUNT}"
        )
    if any(
        ADMITTED_NON_HTTPS_SCHEME_RE.match(url) is None
        or url.lower().startswith("https:")
        for url in non_https_urls
    ):
        raise ValueError("non-HTTPS source locator set contains an unsupported scheme")
    if len(scheme_less_identifiers) != EXPECTED_UNIQUE_SCHEME_LESS_IDENTIFIER_COUNT:
        raise ValueError(
            f"manifest has {len(scheme_less_identifiers)} unique scheme-less identifiers, "
            f"expected {EXPECTED_UNIQUE_SCHEME_LESS_IDENTIFIER_COUNT}"
        )
    # Preserve the source-declared scheme-less field even when a literal value
    # lexically resembles a URI; field standing is not inferred or corrected.

    return ManifestStats(
        source_count=counts["source"],
        hierarchy_count=counts["hierarchy"],
        topic_count=counts["topic"],
        row_count=row_count,
        unique_https_count=len(https_urls),
        unique_non_https_count=len(non_https_urls),
        unique_scheme_less_count=len(scheme_less_identifiers),
    )


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def build_manifest(path: Path) -> list[ManifestRecord]:
    actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    if path.resolve() == DEFAULT_INPUT.resolve() and actual_hash != FROZEN_BASELINE_SHA256:
        raise ValueError(
            f"{path}: acquisition baseline drifted "
            f"({actual_hash}, expected {FROZEN_BASELINE_SHA256})"
        )
    lines = read_utf8(path).splitlines()
    date = retrieval_date(lines, path)
    blocks = parse_blocks(lines, path)
    records = [record for block in blocks for record in records_for_block(block, date)]
    validate_records(records)
    return records


def write_csv(records: list[ManifestRecord], output: TextIO) -> None:
    validate_sparse_projection(records)
    writer = csv.DictWriter(output, fieldnames=FIELDNAMES, lineterminator="\n")
    writer.writeheader()
    for record in records:
        writer.writerow(record.csv_row())


def run_projection_self_tests() -> None:
    """Exercise exact source serialization, sparse children, and failed joins."""

    duplicate_https = (
        "https://example.test/one",
        "https://example.test/two",
        "https://example.test/one",
    )
    duplicate_non_https = (
        "http://example.test/legacy",
        "urn:self-test:locator",
        "http://example.test/legacy",
    )
    duplicate_scheme_less = (
        "identifier with internal spaces and final spaces  ",
        "ISBN-TEST",
        "ISBN-TEST",
    )
    source = ManifestRecord(
        stable_id="SRC-999",
        record_type="source",
        source_id="SRC-999",
        source_title="Self-test source",
        source_metadata=('Exact comma, quote " and Unicode Ω', "Second item"),
        retrieved_granularity="Self-test exact granularity",
        hierarchy_path=("Self-test source",),
        parent_stable_id="",
        displayed_title="Self-test source",
        source_https_urls=duplicate_https,
        source_non_https_urls=duplicate_non_https,
        source_scheme_less_identifiers=duplicate_scheme_less,
        retrieval_date="2026-08-12",
    )
    child = ManifestRecord(
        stable_id="SRC-999-T001",
        record_type="topic",
        source_id=source.source_id,
        source_title=source.source_title,
        source_metadata=source.source_metadata,
        retrieved_granularity=source.retrieved_granularity,
        hierarchy_path=(source.source_title, "Self-test topic"),
        parent_stable_id=source.stable_id,
        displayed_title="Self-test topic",
        source_https_urls=source.source_https_urls,
        source_non_https_urls=source.source_non_https_urls,
        source_scheme_less_identifiers=source.source_scheme_less_identifiers,
        retrieval_date=source.retrieval_date,
    )

    validate_sparse_projection([source, child])
    spaced_identifier = (
        "Exact scheme-less identifier 1: identifier with internal spaces and final spaces  "
    )
    identifier_match = SCHEME_LESS_IDENTIFIER_RE.fullmatch(spaced_identifier)
    if (
        identifier_match is None
        or identifier_match.group("identifier")
        != "identifier with internal spaces and final spaces  "
    ):
        raise AssertionError("scheme-less identifier whitespace was not preserved exactly")
    try:
        ordered_https_occurrences(
            ("Exact HTTPS locator 2: https://example.test/noncanonical",),
            Path("self-test-baseline.md"),
            1,
        )
    except ValueError as exc:
        if "HTTPS locator numbering is not exact and sequential" not in str(exc):
            raise AssertionError(
                "non-dense HTTPS self-test produced the wrong failure"
            ) from exc
    else:
        raise AssertionError("non-dense HTTPS locator numbering was accepted")
    csv_buffer = io.StringIO(newline="")
    write_csv([source, child], csv_buffer)
    rows = list(csv.DictReader(io.StringIO(csv_buffer.getvalue())))
    if len(rows) != 2:
        raise AssertionError("projection self-test did not emit exactly two rows")
    source_row, child_row = rows
    expected = expected_source_only_values(source)
    if any(source_row[field] != expected[field] for field in SOURCE_ONLY_FIELDS):
        raise AssertionError("source-only fields did not survive CSV quoting exactly")
    if tuple(json.loads(source_row["source_https_urls"])) != duplicate_https:
        raise AssertionError("duplicate HTTPS occurrences changed in source-row JSON")
    if tuple(json.loads(source_row["source_non_https_urls"])) != duplicate_non_https:
        raise AssertionError("duplicate non-HTTPS occurrences changed in source-row JSON")
    if (
        tuple(json.loads(source_row["source_scheme_less_identifiers"]))
        != duplicate_scheme_less
    ):
        raise AssertionError(
            "duplicate scheme-less occurrences changed in source-row JSON"
        )
    empty_non_https_row = replace(source, source_non_https_urls=()).csv_row()
    if empty_non_https_row["source_non_https_urls"] != "[]":
        raise AssertionError("source empty list is not represented by literal []")
    if any(child_row[field] != "" for field in SOURCE_ONLY_FIELDS):
        raise AssertionError("child source-only fields are not sparse")

    json_attributes = {
        "source_metadata": "source_metadata",
        "source_https_urls": "source_https_urls",
        "source_non_https_urls": "source_non_https_urls",
        "source_scheme_less_identifiers": "source_scheme_less_identifiers",
    }
    for field, attribute in json_attributes.items():
        recovered = tuple(json.loads(source_row[field]))
        if recovered != getattr(child, attribute):
            raise AssertionError(f"child {field} was not recovered exactly")
    if source_row["retrieved_granularity"] != child.retrieved_granularity:
        raise AssertionError("child retrieved granularity was not recovered exactly")

    def require_failure(
        label: str, candidate_records: list[ManifestRecord], expected_text: str
    ) -> None:
        try:
            validate_sparse_projection(candidate_records)
        except ValueError as exc:
            if expected_text not in str(exc):
                raise AssertionError(
                    f"{label}: wrong failure {exc!s}; expected {expected_text!r}"
                ) from exc
        else:
            raise AssertionError(f"{label}: invalid projection was accepted")

    require_failure(
        "child mismatch",
        [source, replace(child, source_metadata=("altered",))],
        "not exactly recoverable",
    )
    require_failure(
        "orphan child",
        [source, replace(child, source_id="SRC-998")],
        "resolves to 0 source rows",
    )
    require_failure(
        "duplicate source",
        [source, replace(source), child],
        "requires exactly one source row",
    )
    require_failure(
        "miskeyed source",
        [replace(source, stable_id="SRC-998"), child],
        "source stable ID does not equal",
    )

    with tempfile.TemporaryDirectory(prefix="coverage-stream-self-test-") as temp_dir:
        baseline = Path(temp_dir) / "baseline.md"
        baseline.write_text(
            "Retrieval date for every URL below: 2026-08-12.\n"
            "\n"
            "### SRC-001 — Stream self-test\n"
            "- Official source: https://example.test/source\n"
            "- Exact HTTPS locator 1: https://example.test/exact\n"
            "- Repeated official source: https://example.test/source\n"
            "- Exact HTTPS locator 2: https://example.test/exact\n"
            "- Exact non-HTTPS locator 1: http://example.test/legacy\n"
            "- Exact non-HTTPS locator 2: urn:self-test:locator\n"
            "- Exact non-HTTPS locator 3: http://example.test/legacy\n"
            "- Exact scheme-less identifier 1: identifier with internal and final spaces  \n"
            "- Exact scheme-less identifier 2: DUPLICATE-ID\n"
            "- Exact scheme-less identifier 3: DUPLICATE-ID\n"
            "- Retrieved granularity: every exact self-test row\n"
            "\n"
            "#### Exact hierarchy\n"
            "- Exact topic\n"
            "\n"
            "---\n",
            encoding="utf-8",
            newline="",
        )
        streamed_records = list(iter_manifest_records(baseline, "2026-08-12"))
        reference_lines = read_utf8(baseline).splitlines()
        reference_records = [
            record
            for block in parse_blocks(reference_lines, baseline)
            for record in records_for_block(block, "2026-08-12")
        ]
        if streamed_records != reference_records:
            raise AssertionError("stream parser rows differ from the exact reference parser")
        if len(streamed_records) != 3:
            raise AssertionError("stream parser did not emit source, hierarchy, and topic")
        streamed_source = streamed_records[0]
        if streamed_source.source_https_urls != (
            "https://example.test/source",
            "https://example.test/exact",
            "https://example.test/source",
            "https://example.test/exact",
        ):
            raise AssertionError(
                "stream parser changed interleaved duplicate HTTPS occurrence order"
            )
        if streamed_source.source_non_https_urls != (
            "http://example.test/legacy",
            "urn:self-test:locator",
            "http://example.test/legacy",
        ):
            raise AssertionError(
                "stream parser changed duplicate non-HTTPS occurrence order"
            )
        if streamed_source.source_scheme_less_identifiers != (
            "identifier with internal and final spaces  ",
            "DUPLICATE-ID",
            "DUPLICATE-ID",
        ):
            raise AssertionError(
                "stream parser changed duplicate scheme-less occurrence order"
            )

        self_test_pins = {
            "EXPECTED_SOURCE_COUNT": 1,
            "EXPECTED_HIERARCHY_COUNT": 1,
            "EXPECTED_TOPIC_COUNT": 1,
            "EXPECTED_ROW_COUNT": 3,
            "EXPECTED_UNIQUE_URL_COUNT": 2,
            "EXPECTED_UNIQUE_NON_HTTPS_URL_COUNT": 2,
            "EXPECTED_UNIQUE_SCHEME_LESS_IDENTIFIER_COUNT": 2,
        }
        original_pins = {name: globals()[name] for name in self_test_pins}
        try:
            globals().update(self_test_pins)
            stats = scan_manifest(baseline, "2026-08-12")
        finally:
            globals().update(original_pins)
        if (
            stats.unique_https_count,
            stats.unique_non_https_count,
            stats.unique_scheme_less_count,
        ) != (2, 2, 2):
            raise AssertionError("unique locator summaries did not remain set-based")
        streamed_csv = io.StringIO(newline="")
        streamed_markdown = io.StringIO(newline="")
        write_streamed_outputs(
            iter_manifest_records(baseline, "2026-08-12"),
            stats,
            "2026-08-12",
            baseline,
            streamed_csv,
            streamed_markdown,
        )
        legacy_csv = io.StringIO(newline="")
        legacy_markdown = io.StringIO(newline="")
        write_csv(streamed_records, legacy_csv)
        write_markdown(streamed_records, baseline, legacy_markdown)
        if streamed_csv.getvalue() != legacy_csv.getvalue():
            raise AssertionError("streamed CSV bytes differ from the exact row writer")
        if streamed_markdown.getvalue() != legacy_markdown.getvalue():
            raise AssertionError("streamed Markdown bytes differ from the exact row writer")


def markdown_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("|", r"\|").replace("\n", "<br>")


class MarkdownLineWriter:
    """Stream joined lines while discarding only final blank lines."""

    def __init__(self, output: TextIO) -> None:
        self.output = output
        self.started = False
        self.pending_blank_lines = 0

    def append(self, line: str) -> None:
        if line == "":
            self.pending_blank_lines += 1
            return
        if self.started:
            self.output.write("\n" * (self.pending_blank_lines + 1))
        elif self.pending_blank_lines:
            self.output.write("\n" * self.pending_blank_lines)
        self.output.write(line)
        self.started = True
        self.pending_blank_lines = 0

    def extend(self, lines: Iterable[str]) -> None:
        for line in lines:
            self.append(line)

    def finish(self) -> None:
        if self.started:
            self.output.write("\n")


def write_markdown(
    records: list[ManifestRecord], input_path: Path, output: TextIO
) -> None:
    counts = Counter(record.record_type for record in records)
    source_rows = [record for record in records if record.record_type == "source"]
    unique_urls = {url for record in source_rows for url in record.source_https_urls}
    unique_non_https_urls = {
        url for record in source_rows for url in record.source_non_https_urls
    }
    unique_scheme_less_identifiers = {
        identifier
        for record in source_rows
        for identifier in record.source_scheme_less_identifiers
    }
    lines = [
        "# Full-compendium coverage manifest",
        "",
        "Generated mechanically from "
        f"`{relative_display(input_path)}`. This manifest preserves the acquired "
        "source records, displayed hierarchy, topic titles, repetitions, metadata, "
        "URL order, and acquisition order. This is an acquisition-only manifest: "
        "it does not classify topics, select a house syntax, infer any handbook "
        "mapping, or serve as a completion ledger. A separate keyed mapping and "
        "packet-status ledger remains owed.",
        "",
        "## Validation",
        "",
        f"- Retrieval date: `{source_rows[0].retrieval_date}`.",
        f"- Source records: {counts['source']:,}.",
        f"- Hierarchy records: {counts['hierarchy']:,}.",
        f"- Topic records: {counts['topic']:,}.",
        f"- Total records: {len(records):,}.",
        f"- Unique HTTPS source URLs: {len(unique_urls):,}.",
        f"- Unique non-HTTPS source URLs: {len(unique_non_https_urls):,}.",
        "- Unique scheme-less source identifiers: "
        f"{len(unique_scheme_less_identifiers):,}.",
        f"- Mapping status on every record: `{MAPPING_STATUS}`.",
        "",
        "The CSV is the complete machine-readable ledger. Source rows carry the "
        "source-level JSON-valued fields and `retrieved_granularity` once; hierarchy "
        "and topic rows join to them through `source_id`, without duplicating those "
        "same source values. On each source row, `source_metadata` is the ordered "
        "list of source metadata bullets, `retrieved_granularity` is the exact "
        "source-level acquisition-granularity field, "
        "`source_https_urls` and `source_non_https_urls` are the two ordered URL "
        "lists, `source_scheme_less_identifiers` is the ordered list of literal "
        "source identifiers that supply no URI scheme, and `hierarchy_path` is "
        "the ordered displayed-title path from the source through the current "
        "record. These locator fields are administrative source evidence, not "
        "logical classifications; they remain separate because neither an HTTP "
        "locator nor a scheme-less identifier is replaceable by an HTTPS URL.",
        "",
        "## Record ledger",
        "",
    ]

    line_writer = MarkdownLineWriter(output)
    line_writer.extend(lines)
    record_groups = iter(groupby(records, key=lambda record: record.source_id))
    for source in source_rows:
        try:
            grouped_source_id, source_records = next(record_groups)
        except StopIteration as exc:
            raise ValueError(
                f"markdown output has no record group for {source.source_id}"
            ) from exc
        if grouped_source_id != source.source_id:
            raise ValueError(
                f"markdown source order drifted: found {grouped_source_id}, "
                f"expected {source.source_id}"
            )
        line_writer.extend(
            [
                f"### {source.source_id} — {source.source_title}",
                "",
                f"- Stable ID: `{source.stable_id}`",
                f"- Retrieved granularity: {source.retrieved_granularity}",
                f"- Mapping status: `{source.mapping_status}`",
                "- Source metadata, in displayed order:",
            ]
        )
        for item in source.source_metadata:
            line_writer.append(f"  - {item}")
        line_writer.extend(
            [
                "",
                "| Stable ID | Type | Parent | Hierarchy path | Displayed title | Mapping status |",
                "|---|---|---|---|---|---|",
            ]
        )
        for record in source_records:
            path = json.dumps(
                record.hierarchy_path, ensure_ascii=False, separators=(",", ":")
            )
            parent = record.parent_stable_id or "—"
            line_writer.append(
                f"| `{record.stable_id}` | {record.record_type} | "
                f"`{parent}` | `{markdown_escape(path)}` | "
                f"{markdown_escape(record.displayed_title)} | "
                f"`{record.mapping_status}` |"
            )
        line_writer.append("")

    try:
        extra_source_id, _ = next(record_groups)
    except StopIteration:
        pass
    else:
        raise ValueError(f"markdown output has unexpected group {extra_source_id}")
    line_writer.finish()


def streamed_markdown_header(
    stats: ManifestStats, date: str, input_path: Path
) -> tuple[str, ...]:
    return (
        "# Full-compendium coverage manifest",
        "",
        "Generated mechanically from "
        f"`{relative_display(input_path)}`. This manifest preserves the acquired "
        "source records, displayed hierarchy, topic titles, repetitions, metadata, "
        "URL order, and acquisition order. This is an acquisition-only manifest: "
        "it does not classify topics, select a house syntax, infer any handbook "
        "mapping, or serve as a completion ledger. A separate keyed mapping and "
        "packet-status ledger remains owed.",
        "",
        "## Validation",
        "",
        f"- Retrieval date: `{date}`.",
        f"- Source records: {stats.source_count:,}.",
        f"- Hierarchy records: {stats.hierarchy_count:,}.",
        f"- Topic records: {stats.topic_count:,}.",
        f"- Total records: {stats.row_count:,}.",
        f"- Unique HTTPS source URLs: {stats.unique_https_count:,}.",
        f"- Unique non-HTTPS source URLs: {stats.unique_non_https_count:,}.",
        "- Unique scheme-less source identifiers: "
        f"{stats.unique_scheme_less_count:,}.",
        f"- Mapping status on every record: `{MAPPING_STATUS}`.",
        "",
        "The CSV is the complete machine-readable ledger. Source rows carry the "
        "source-level JSON-valued fields and `retrieved_granularity` once; hierarchy "
        "and topic rows join to them through `source_id`, without duplicating those "
        "same source values. On each source row, `source_metadata` is the ordered "
        "list of source metadata bullets, `retrieved_granularity` is the exact "
        "source-level acquisition-granularity field, "
        "`source_https_urls` and `source_non_https_urls` are the two ordered URL "
        "lists, `source_scheme_less_identifiers` is the ordered list of literal "
        "source identifiers that supply no URI scheme, and `hierarchy_path` is "
        "the ordered displayed-title path from the source through the current "
        "record. These locator fields are administrative source evidence, not "
        "logical classifications; they remain separate because neither an HTTP "
        "locator nor a scheme-less identifier is replaceable by an HTTPS URL.",
        "",
        "## Record ledger",
        "",
    )


def write_streamed_outputs(
    records: Iterable[ManifestRecord],
    stats: ManifestStats,
    date: str,
    input_path: Path,
    csv_output: TextIO,
    markdown_output: TextIO,
) -> None:
    csv_writer = csv.DictWriter(
        csv_output, fieldnames=FIELDNAMES, lineterminator="\n"
    )
    csv_writer.writeheader()
    markdown = MarkdownLineWriter(markdown_output)
    markdown.extend(streamed_markdown_header(stats, date, input_path))

    current_source: ManifestRecord | None = None
    counts: Counter[str] = Counter()
    for record in records:
        counts[record.record_type] += 1
        csv_writer.writerow(record.csv_row())

        if record.record_type == "source":
            if current_source is not None:
                markdown.append("")
            current_source = record
            markdown.extend(
                (
                    f"### {record.source_id} — {record.source_title}",
                    "",
                    f"- Stable ID: `{record.stable_id}`",
                    f"- Retrieved granularity: {record.retrieved_granularity}",
                    f"- Mapping status: `{record.mapping_status}`",
                    "- Source metadata, in displayed order:",
                )
            )
            for item in record.source_metadata:
                markdown.append(f"  - {item}")
            markdown.extend(
                (
                    "",
                    "| Stable ID | Type | Parent | Hierarchy path | Displayed title | Mapping status |",
                    "|---|---|---|---|---|---|",
                )
            )
        elif current_source is None or record.source_id != current_source.source_id:
            raise ValueError(
                f"{record.stable_id}: output row does not follow its exact source row"
            )

        path = canonical_json(record.hierarchy_path)
        parent = record.parent_stable_id or "—"
        markdown.append(
            f"| `{record.stable_id}` | {record.record_type} | "
            f"`{parent}` | `{markdown_escape(path)}` | "
            f"{markdown_escape(record.displayed_title)} | "
            f"`{record.mapping_status}` |"
        )

    actual = (
        counts["source"],
        counts["hierarchy"],
        counts["topic"],
        sum(counts.values()),
    )
    expected = (
        stats.source_count,
        stats.hierarchy_count,
        stats.topic_count,
        stats.row_count,
    )
    if actual != expected:
        raise ValueError(
            f"streamed output counts changed between scans: {actual!r}, expected {expected!r}"
        )
    markdown.finish()


def create_adjacent_temp(path: Path, *, create_parent: bool) -> tuple[Path, TextIO]:
    """Create a named temporary file beside its eventual target."""

    if create_parent:
        path.parent.mkdir(parents=True, exist_ok=True)
    if not path.parent.is_dir():
        raise FileNotFoundError(f"output parent does not exist: {path.parent}")
    handle = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        newline="",
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
        delete=False,
    )
    return Path(handle.name), handle


def files_equal(left: Path, right: Path, chunk_size: int = 1024 * 1024) -> bool:
    if left.stat().st_size != right.stat().st_size:
        return False
    with left.open("rb") as left_handle, right.open("rb") as right_handle:
        while True:
            left_chunk = left_handle.read(chunk_size)
            right_chunk = right_handle.read(chunk_size)
            if left_chunk != right_chunk:
                return False
            if not left_chunk:
                return True


def check_generated_file(path: Path, temporary_path: Path | None) -> bool:
    if not path.exists():
        print(f"missing generated file: {relative_display(path)}", file=sys.stderr)
        return False
    if temporary_path is None or not files_equal(path, temporary_path):
        print(f"stale generated file: {relative_display(path)}", file=sys.stderr)
        return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MARKDOWN)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify that generated files are current without rewriting them",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="run sparse-projection self-tests without reading or writing manifests",
    )
    args = parser.parse_args()

    if args.self_test:
        try:
            run_projection_self_tests()
        except (AssertionError, ValueError) as exc:
            print(f"coverage-manifest self-test failed: {exc}", file=sys.stderr)
            return 1
        print("coverage-manifest sparse-projection self-tests: PASS")
        return 0

    if args.csv.resolve() == args.markdown.resolve():
        print(
            "coverage-manifest generation failed: CSV and Markdown targets are identical",
            file=sys.stderr,
        )
        return 1

    if args.check:
        missing_parent = False
        for target in (args.csv, args.markdown):
            if not target.parent.is_dir():
                missing_parent = True
                print(
                    f"missing generated file: {relative_display(target)}",
                    file=sys.stderr,
                )
        if missing_parent:
            return 1

    temporary_paths: list[Path] = []
    handles: list[TextIO] = []
    try:
        initial_hash = sha256_file(args.input)
        if (
            args.input.resolve() == DEFAULT_INPUT.resolve()
            and initial_hash != FROZEN_BASELINE_SHA256
        ):
            raise ValueError(
                f"{args.input}: acquisition baseline drifted "
                f"({initial_hash}, expected {FROZEN_BASELINE_SHA256})"
            )
        date = streamed_retrieval_date(args.input)
        stats = scan_manifest(args.input, date)

        csv_temp, csv_handle = create_adjacent_temp(
            args.csv, create_parent=not args.check
        )
        temporary_paths.append(csv_temp)
        handles.append(csv_handle)
        markdown_temp, markdown_handle = create_adjacent_temp(
            args.markdown, create_parent=not args.check
        )
        temporary_paths.append(markdown_temp)
        handles.append(markdown_handle)

        write_streamed_outputs(
            iter_manifest_records(args.input, date),
            stats,
            date,
            args.input,
            csv_handle,
            markdown_handle,
        )
        for handle in handles:
            handle.flush()
            os.fsync(handle.fileno())
            handle.close()

        final_hash = sha256_file(args.input)
        if final_hash != initial_hash:
            raise ValueError(
                f"{args.input}: acquisition baseline changed during generation "
                f"({initial_hash} -> {final_hash})"
            )

        if args.check:
            current = check_generated_file(args.csv, csv_temp)
            current &= check_generated_file(args.markdown, markdown_temp)
            if not current:
                return 1
        else:
            csv_temp.replace(args.csv)
            temporary_paths.remove(csv_temp)
            markdown_temp.replace(args.markdown)
            temporary_paths.remove(markdown_temp)
    except (OSError, UnicodeError, ValueError, csv.Error) as exc:
        print(f"coverage-manifest generation failed: {exc}", file=sys.stderr)
        return 1
    finally:
        for handle in handles:
            if not handle.closed:
                handle.close()
        for temporary_path in temporary_paths:
            temporary_path.unlink(missing_ok=True)

    mode = "verified" if args.check else "wrote"
    print(
        f"{mode} {stats.row_count:,} rows: {stats.source_count} sources, "
        f"{stats.hierarchy_count} hierarchy headings, {stats.topic_count} topics, "
        f"{stats.unique_https_count} unique HTTPS URLs, "
        f"{stats.unique_non_https_count} unique non-HTTPS URLs, "
        f"{stats.unique_scheme_less_count} unique scheme-less identifiers"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

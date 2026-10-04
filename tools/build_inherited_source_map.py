#!/usr/bin/env python3
"""Build the inherited-source audit-interval baseline from the audit ledgers.

This generator does not classify or rewrite handbook content.  It copies the
five cells of each frozen-source restoration row, records the row's audit
location, and gives every physical source interval a deterministic identifier.

The printed corpus is the text strictly between ``\\begin{document}`` and
``\\end{document}``.  The audit tables occasionally omit a blank separator
line between consecutive units.  Such a gap is admitted only when every line
in it is blank or comment-only; the generator then emits an explicitly typed,
unclassified continuity interval.  Any content-bearing gap, any overlap, or
any final coverage count other than exactly one is a hard failure.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = REPO_ROOT / "source" / "formal-logic-reference.tex"
DEFAULT_AUDITS = (
    REPO_ROOT / "spec" / "research" / "full-transcription-audit-p01-p04.md",
    REPO_ROOT / "spec" / "research" / "full-transcription-audit-p05-p08.md",
    REPO_ROOT / "spec" / "research" / "full-transcription-audit-p09-p14.md",
)
DEFAULT_CSV = REPO_ROOT / "spec" / "inherited-source-map.csv"
DEFAULT_MARKDOWN = REPO_ROOT / "spec" / "inherited-source-map.md"
FROZEN_AUDIT_SHA256 = {
    "spec/research/full-transcription-audit-p01-p04.md": "7e81084f677f93d4aa2e30989b8fe7c04221abc9ae909cd477bb5ee579b7770f",
    "spec/research/full-transcription-audit-p05-p08.md": "ea47ea6f1c3be0026f099db958a31da763eb1df31e388e72d891409891c67356",
    "spec/research/full-transcription-audit-p09-p14.md": "06ab9d4fdf20d7ea67c2bc080eacb4c00a2350484ab70219be5828a10c59686f",
}

CONTRACT_CLASS_ORDER = (
    "full-and-accurate",
    "layout-only relocation",
    "altered",
    "abridged",
    "omitted",
    "hybridized",
    "unsupported addition",
)

TABLE_FIRST_HEADERS = {"frozen source", "frozen source locator"}
RANGE_RE = re.compile(r"^(?P<start>\d+)(?:\s*--\s*(?P<end>\d+))?$")


@dataclass(frozen=True)
class SourceFile:
    path: Path
    raw: bytes
    line_bytes: tuple[bytes, ...]
    line_text: tuple[str, ...]
    printed_first: int
    printed_last: int
    sha256: str


@dataclass(frozen=True)
class AuditRow:
    audit_file: str
    audit_line: int
    audit_heading: str
    audit_source_locator: str
    source_spans: tuple[tuple[int, int], ...]
    source_surface_description: str
    current_live_locator_evidence: str
    class_original: str
    class_normalized: tuple[str, ...]
    restoration_obligation: str


@dataclass(frozen=True)
class MapInterval:
    stable_id: str
    record_type: str
    source_start: int
    source_end: int
    audit_source_locator: str
    audit_file: str
    audit_line_start: int
    audit_line_end: int
    audit_heading: str
    source_surface_description: str
    current_live_locator_evidence: str
    class_original: str
    class_normalized: tuple[str, ...]
    restoration_obligation: str
    source_sha256: str

    @property
    def line_count(self) -> int:
        return self.source_end - self.source_start + 1

    @property
    def audit_locator(self) -> str:
        suffix = str(self.audit_line_start)
        if self.audit_line_end != self.audit_line_start:
            suffix += f"--{self.audit_line_end}"
        return f"{self.audit_file}:{suffix}"


def source_file(path: Path) -> SourceFile:
    raw = path.read_bytes()
    line_bytes = tuple(raw.splitlines(keepends=True))
    try:
        line_text = tuple(line.decode("utf-8") for line in line_bytes)
    except UnicodeDecodeError as exc:
        raise ValueError(f"{path}: source is not UTF-8: {exc}") from exc

    begin_lines = [
        number
        for number, line in enumerate(line_text, start=1)
        if line.strip() == r"\begin{document}"
    ]
    end_lines = [
        number
        for number, line in enumerate(line_text, start=1)
        if line.strip() == r"\end{document}"
    ]
    if len(begin_lines) != 1 or len(end_lines) != 1:
        raise ValueError(
            f"{path}: expected one document begin and end; found "
            f"{len(begin_lines)} and {len(end_lines)}"
        )
    begin = begin_lines[0]
    end = end_lines[0]
    if begin >= end:
        raise ValueError(f"{path}: document boundary order is invalid")

    return SourceFile(
        path=path,
        raw=raw,
        line_bytes=line_bytes,
        line_text=line_text,
        printed_first=begin + 1,
        printed_last=end - 1,
        sha256=hashlib.sha256(raw).hexdigest(),
    )


def relative_display(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return resolved.as_posix()


def split_markdown_row(line: str) -> list[str]:
    """Split a pipe table row without treating pipes in code spans as cells."""

    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []

    cells: list[str] = []
    cell: list[str] = []
    in_code = False
    code_fence = 0
    index = 1
    stop = len(stripped) - 1

    while index < stop:
        char = stripped[index]
        if char == "`":
            run_end = index + 1
            while run_end < stop and stripped[run_end] == "`":
                run_end += 1
            run_length = run_end - index
            if not in_code:
                in_code = True
                code_fence = run_length
            elif run_length == code_fence:
                in_code = False
                code_fence = 0
            cell.append(stripped[index:run_end])
            index = run_end
            continue

        escaped = index > 0 and stripped[index - 1] == "\\"
        if char == "|" and not in_code and not escaped:
            cells.append("".join(cell).strip())
            cell = []
        else:
            cell.append(char)
        index += 1

    cells.append("".join(cell).strip())
    return cells


def normalized_header(cell: str) -> str:
    value = re.sub(r"[`*_]", "", cell).strip().lower()
    return re.sub(r"\s+", " ", value)


def is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def parse_source_locator(cell: str, *, where: str) -> tuple[tuple[int, int], ...]:
    value = cell.strip()
    while len(value) >= 2 and (
        (value.startswith("**") and value.endswith("**"))
        or (value.startswith("__") and value.endswith("__"))
    ):
        value = value[2:-2].strip()
    if value.startswith("`") and value.endswith("`"):
        value = value[1:-1].strip()

    spans: list[tuple[int, int]] = []
    for item in value.split(","):
        match = RANGE_RE.fullmatch(item.strip())
        if not match:
            raise ValueError(f"{where}: invalid frozen-source locator {cell!r}")
        start = int(match.group("start"))
        end = int(match.group("end") or match.group("start"))
        if start < 1 or end < start:
            raise ValueError(f"{where}: reversed/out-of-range locator {item!r}")
        spans.append((start, end))
    return tuple(spans)


def normalize_classes(original: str, *, where: str) -> tuple[str, ...]:
    text = re.sub(r"[`*_]", "", original).strip().lower()
    aliases = {
        "full and accurate": "full-and-accurate",
        "full-and-accurate": "full-and-accurate",
        "layout-only": "layout-only relocation",
        "layout only": "layout-only relocation",
        "layout-only relocation": "layout-only relocation",
        "altered": "altered",
        "abridged": "abridged",
        "shortened": "abridged",
        "omitted": "omitted",
        "hybrid": "hybridized",
        "hybridized": "hybridized",
        "unsupported addition": "unsupported addition",
    }
    if text in aliases:
        tokens = [text]
    else:
        tokens = [
            token.strip()
            for token in re.split(r"\s*(?:,|;|/|\band\b)\s*", text)
            if token.strip()
        ]
    unknown = [token for token in tokens if token not in aliases]
    if unknown:
        raise ValueError(f"{where}: unknown contract class token(s) {unknown!r}")
    found = {aliases[token] for token in tokens}
    if original.strip() and not found:
        raise ValueError(f"{where}: no recognized contract class in {original!r}")
    passing = {"full-and-accurate", "layout-only relocation"} & found
    defects = {
        "altered",
        "abridged",
        "omitted",
        "hybridized",
        "unsupported addition",
    } & found
    if len(passing) > 1:
        raise ValueError(f"{where}: mutually exclusive passing classes in {original!r}")
    if passing and defects:
        raise ValueError(
            f"{where}: a passing class cannot co-occur with defects in {original!r}"
        )
    return tuple(item for item in CONTRACT_CLASS_ORDER if item in found)


def validate_class_parser() -> None:
    expected = {
        "full and accurate": ("full-and-accurate",),
        "layout-only": ("layout-only relocation",),
        "abridged and altered": ("altered", "abridged"),
        "altered, hybrid": ("altered", "hybridized"),
    }
    for value, result in expected.items():
        if normalize_classes(value, where="class-parser self-test") != result:
            raise ValueError(f"class-parser self-test failed for {value!r}")
    for value in ("altered, nonsense", "not altered", "abridged-ish"):
        try:
            normalize_classes(value, where="class-parser self-test")
        except ValueError:
            continue
        raise ValueError(f"class-parser accepted invalid value {value!r}")


def parse_audit(path: Path) -> list[AuditRow]:
    lines = path.read_text(encoding="utf-8").splitlines()
    rows: list[AuditRow] = []
    heading = ""
    index = 0

    while index < len(lines):
        line = lines[index]
        heading_match = re.match(r"^#{1,6}\s+(?P<title>.+?)\s*$", line)
        if heading_match:
            heading = heading_match.group("title")

        header = split_markdown_row(line)
        header_names = [normalized_header(cell) for cell in header]
        is_ledger = (
            len(header_names) == 5
            and header_names[0] in TABLE_FIRST_HEADERS
            and (
                "source" in header_names[1]
                or "function" in header_names[1]
            )
            and header_names[3].startswith("class")
            and (
                "restoration" in header_names[4]
                or "obligation" in header_names[4]
            )
        )
        if not is_ledger:
            index += 1
            continue

        if index + 1 >= len(lines):
            raise ValueError(f"{path}:{index + 1}: unterminated ledger table")
        separator = split_markdown_row(lines[index + 1])
        if len(separator) != 5 or not is_separator(separator):
            raise ValueError(f"{path}:{index + 2}: malformed ledger separator")

        index += 2
        table_rows = 0
        while index < len(lines):
            cells = split_markdown_row(lines[index])
            if not cells:
                break
            if len(cells) != 5:
                raise ValueError(
                    f"{path}:{index + 1}: ledger row has {len(cells)} cells, not 5"
                )
            where = f"{path}:{index + 1}"
            spans = parse_source_locator(cells[0], where=where)
            classes = normalize_classes(cells[3], where=where)
            rows.append(
                AuditRow(
                    audit_file=relative_display(path),
                    audit_line=index + 1,
                    audit_heading=heading,
                    audit_source_locator=cells[0],
                    source_spans=spans,
                    source_surface_description=cells[1],
                    current_live_locator_evidence=cells[2],
                    class_original=cells[3],
                    class_normalized=classes,
                    restoration_obligation=cells[4],
                )
            )
            table_rows += 1
            index += 1
        if table_rows == 0:
            raise ValueError(f"{path}: ledger under {heading!r} has no data rows")

    if not rows:
        raise ValueError(f"{path}: found no five-column frozen-source ledger rows")
    return rows


def digest_interval(source: SourceFile, start: int, end: int) -> str:
    literal = b"".join(source.line_bytes[start - 1 : end])
    return hashlib.sha256(literal).hexdigest()


def stable_id(record_type: str, start: int, end: int) -> str:
    prefixes = {
        "preamble_obligation": "PRE",
        "document_control": "CTL",
        "printed_body": "SRC",
        "printed_continuity": "SEP",
    }
    return f"{prefixes[record_type]}-{start:05d}-{end:05d}"


def interval_from_row(
    row: AuditRow,
    source: SourceFile,
    record_type: str,
    start: int,
    end: int,
) -> MapInterval:
    return MapInterval(
        stable_id=stable_id(record_type, start, end),
        record_type=record_type,
        source_start=start,
        source_end=end,
        audit_source_locator=row.audit_source_locator,
        audit_file=row.audit_file,
        audit_line_start=row.audit_line,
        audit_line_end=row.audit_line,
        audit_heading=row.audit_heading,
        source_surface_description=row.source_surface_description,
        current_live_locator_evidence=row.current_live_locator_evidence,
        class_original=row.class_original,
        class_normalized=row.class_normalized,
        restoration_obligation=row.restoration_obligation,
        source_sha256=digest_interval(source, start, end),
    )


def expand_rows(rows: list[AuditRow], source: SourceFile) -> list[MapInterval]:
    intervals: list[MapInterval] = []
    last_line = len(source.line_bytes)
    first = source.printed_first
    last = source.printed_last

    for row in rows:
        for start, end in row.source_spans:
            if end > last_line:
                raise ValueError(
                    f"{row.audit_file}:{row.audit_line}: {start}--{end} exceeds "
                    f"the {last_line}-line source"
                )
            if end < first:
                if start <= first - 2:
                    preamble_end = min(end, first - 2)
                    intervals.append(
                        interval_from_row(
                            row,
                            source,
                            "preamble_obligation",
                            start,
                            preamble_end,
                        )
                    )
                if end >= first - 1:
                    intervals.append(
                        interval_from_row(
                            row,
                            source,
                            "document_control",
                            max(start, first - 1),
                            end,
                        )
                    )
                continue
            if start > last:
                intervals.append(
                    interval_from_row(row, source, "document_control", start, end)
                )
                continue

            if start < first:
                intervals.append(
                    interval_from_row(
                        row, source, "document_control", start, first - 1
                    )
                )
            body_start = max(start, first)
            body_end = min(end, last)
            intervals.append(
                interval_from_row(row, source, "printed_body", body_start, body_end)
            )
            if end > last:
                intervals.append(
                    interval_from_row(row, source, "document_control", last + 1, end)
                )

    return intervals


def collapse(numbers: list[int]) -> list[tuple[int, int]]:
    if not numbers:
        return []
    spans: list[tuple[int, int]] = []
    start = previous = numbers[0]
    for number in numbers[1:]:
        if number == previous + 1:
            previous = number
            continue
        spans.append((start, previous))
        start = previous = number
    spans.append((start, previous))
    return spans


def format_spans(spans: list[tuple[int, int]]) -> str:
    return ", ".join(
        str(start) if start == end else f"{start}--{end}" for start, end in spans
    )


def is_blank_or_comment(line: str) -> bool:
    stripped = line.strip()
    return not stripped or stripped.startswith("%")


def continuity_interval(
    source: SourceFile,
    start: int,
    end: int,
    left: MapInterval | None,
    right: MapInterval | None,
) -> MapInterval:
    adjacent = [item for item in (left, right) if item is not None]
    if not adjacent:
        raise ValueError(f"cannot attribute continuity interval {start}--{end}")
    audit_file = adjacent[0].audit_file
    if any(item.audit_file != audit_file for item in adjacent):
        audit_file = " + ".join(dict.fromkeys(item.audit_file for item in adjacent))
    audit_line_start = min(item.audit_line_start for item in adjacent)
    audit_line_end = max(item.audit_line_end for item in adjacent)
    locators = " and ".join(item.audit_source_locator for item in adjacent)
    heading = adjacent[0].audit_heading
    if any(item.audit_heading != heading for item in adjacent):
        heading = " / ".join(dict.fromkeys(item.audit_heading for item in adjacent))

    return MapInterval(
        stable_id=stable_id("printed_continuity", start, end),
        record_type="printed_continuity",
        source_start=start,
        source_end=end,
        audit_source_locator=f"between {locators}",
        audit_file=audit_file,
        audit_line_start=audit_line_start,
        audit_line_end=audit_line_end,
        audit_heading=heading,
        source_surface_description=(
            "Blank/comment separator between adjacent audited source intervals."
        ),
        current_live_locator_evidence=(
            "No separate audit classification; continuity is bracketed by the "
            f"adjacent ledger rows {locators}."
        ),
        class_original="",
        class_normalized=(),
        restoration_obligation=(
            "Preserve these literal separator lines with the adjacent frozen "
            "source. No content classification is inferred."
        ),
        source_sha256=digest_interval(source, start, end),
    )


def complete_and_validate_body(
    intervals: list[MapInterval], source: SourceFile
) -> list[MapInterval]:
    body = sorted(
        (item for item in intervals if item.record_type == "printed_body"),
        key=lambda item: (item.source_start, item.source_end),
    )
    if not body:
        raise ValueError("no printed-body audit intervals were parsed")

    coverage = [0] * (source.printed_last + 1)
    for item in body:
        for number in range(item.source_start, item.source_end + 1):
            coverage[number] += 1

    overlaps = [
        number
        for number in range(source.printed_first, source.printed_last + 1)
        if coverage[number] > 1
    ]
    if overlaps:
        raise ValueError(
            "overlapping printed-body audit intervals at "
            + format_spans(collapse(overlaps))
        )

    missing = [
        number
        for number in range(source.printed_first, source.printed_last + 1)
        if coverage[number] == 0
    ]
    content_missing = [
        number
        for number in missing
        if not is_blank_or_comment(source.line_text[number - 1])
    ]
    if content_missing:
        raise ValueError(
            "content-bearing printed lines absent from the audit ledgers: "
            + format_spans(collapse(content_missing))
        )

    continuity: list[MapInterval] = []
    for start, end in collapse(missing):
        left_candidates = [item for item in body if item.source_end < start]
        right_candidates = [item for item in body if item.source_start > end]
        left = max(left_candidates, key=lambda item: item.source_end, default=None)
        right = min(right_candidates, key=lambda item: item.source_start, default=None)
        continuity.append(continuity_interval(source, start, end, left, right))

    complete_body = sorted(
        body + continuity, key=lambda item: (item.source_start, item.source_end)
    )
    exact = [0] * (source.printed_last + 1)
    for item in complete_body:
        for number in range(item.source_start, item.source_end + 1):
            exact[number] += 1
    failures = [
        number
        for number in range(source.printed_first, source.printed_last + 1)
        if exact[number] != 1
    ]
    if failures:
        raise ValueError(
            "final printed coverage is not exactly one at "
            + format_spans(collapse(failures))
        )

    nonbody = [item for item in intervals if item.record_type != "printed_body"]
    result = sorted(
        nonbody + complete_body,
        key=lambda item: (item.source_start, item.source_end, item.record_type),
    )
    identifiers = [item.stable_id for item in result]
    if len(identifiers) != len(set(identifiers)):
        duplicates = sorted(
            item for item, count in Counter(identifiers).items() if count > 1
        )
        raise ValueError(f"duplicate stable identifiers: {', '.join(duplicates)}")
    return result


def csv_text(intervals: list[MapInterval]) -> str:
    output = io.StringIO(newline="")
    fieldnames = (
        "stable_id",
        "record_type",
        "source_start",
        "source_end",
        "source_line_count",
        "source_sha256",
        "audit_source_locator",
        "audit_file",
        "audit_line_start",
        "audit_line_end",
        "audit_locator",
        "audit_heading",
        "source_surface_description",
        "audited_snapshot_locator_evidence",
        "class_original",
        "class_normalized",
        "restoration_obligation",
    )
    writer = csv.DictWriter(output, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    for item in intervals:
        writer.writerow(
            {
                "stable_id": item.stable_id,
                "record_type": item.record_type,
                "source_start": item.source_start,
                "source_end": item.source_end,
                "source_line_count": item.line_count,
                "source_sha256": item.source_sha256,
                "audit_source_locator": item.audit_source_locator,
                "audit_file": item.audit_file,
                "audit_line_start": item.audit_line_start,
                "audit_line_end": item.audit_line_end,
                "audit_locator": item.audit_locator,
                "audit_heading": item.audit_heading,
                "source_surface_description": item.source_surface_description,
                "audited_snapshot_locator_evidence": item.current_live_locator_evidence,
                "class_original": item.class_original,
                "class_normalized": "; ".join(item.class_normalized),
                "restoration_obligation": item.restoration_obligation,
            }
        )
    return output.getvalue()


def markdown_escape(text: str) -> str:
    return text.replace("|", r"\|").replace("\n", " ")


def markdown_text(
    intervals: list[MapInterval],
    rows: list[AuditRow],
    source: SourceFile,
    audit_paths: list[Path],
) -> str:
    body_audit = [item for item in intervals if item.record_type == "printed_body"]
    continuity = [
        item for item in intervals if item.record_type == "printed_continuity"
    ]
    preamble = [
        item for item in intervals if item.record_type == "preamble_obligation"
    ]
    controls = [
        item for item in intervals if item.record_type == "document_control"
    ]

    class_interval_counts: Counter[str] = Counter()
    class_line_counts: Counter[str] = Counter()
    for item in body_audit:
        for classification in item.class_normalized:
            class_interval_counts[classification] += 1
            class_line_counts[classification] += item.line_count

    audit_row_counts: Counter[str] = Counter(row.audit_file for row in rows)
    audit_body_intervals: Counter[str] = Counter(
        item.audit_file for item in body_audit
    )
    audit_body_lines: Counter[str] = Counter()
    for item in body_audit:
        audit_body_lines[item.audit_file] += item.line_count

    lines = [
        "# Inherited-source audit-interval baseline",
        "",
        "Generated mechanically from the five-column frozen-source restoration "
        "ledgers. The CSV is the complete ordered interval-audit baseline; this "
        "file records the "
        "coverage proof, normalized counts, and non-body obligations without "
        "changing any audit wording or class string.",
        "",
        "## Validation",
        "",
        f"- Frozen source: `{relative_display(source.path)}`.",
        f"- Frozen-source SHA-256: `{source.sha256}`.",
        "- Audited handbook-source snapshot: `spec/handbook-audit-snapshot.csv`, "
        "SHA-256 `63b405b2b9d1384ee32ae963e053d5c971b90dfe34d186fde0d1b2a0b3cec2ba`.",
        "- All locator evidence and classes are historical evidence for that exact "
        "snapshot; any handbook-source drift invalidates them until re-audited.",
        f"- Physical source lines: {len(source.line_bytes):,}.",
        f"- Printed-source bounds: {source.printed_first}--{source.printed_last} "
        f"({source.printed_last - source.printed_first + 1:,} physical lines).",
        f"- Five-column audit rows parsed: {len(rows):,}.",
        f"- Printed audit intervals: {len(body_audit):,}.",
        f"- Blank/comment continuity intervals inserted: {len(continuity):,} "
        f"({sum(item.line_count for item in continuity):,} physical lines).",
        f"- Coverage verdict: every printed line {source.printed_first}--"
        f"{source.printed_last} is covered exactly once; no overlap remains.",
        "",
        "Continuity rows have no inherited class. They exist only where the "
        "audit ledger omitted a blank or comment-only separator; a nonblank "
        "omission causes generation to fail.",
        "",
        "## Ledger intake by audit",
        "",
        "| Audit note | Five-column rows | Printed intervals | Printed lines |",
        "|---|---:|---:|---:|",
    ]
    for path in audit_paths:
        display = relative_display(path)
        lines.append(
            f"| `{display}` | {audit_row_counts[display]:,} | "
            f"{audit_body_intervals[display]:,} | {audit_body_lines[display]:,} |"
        )

    lines.extend(
        [
            "",
            "## Normalized contract-class counts",
            "",
            "Synonyms in the audit notes are normalized only for counting: "
            "`shortened` maps to `abridged`, `hybrid` to `hybridized`, and "
            "`layout-only` to `layout-only relocation`. Every original single- "
            "or multi-class string remains unchanged in the CSV. A multi-class "
            "interval is counted once in each applicable row, so these rows are "
            "not mutually exclusive.",
            "The `unsupported addition` count below includes only that class when "
            "attached to an inherited source interval. This one-way baseline does "
            "not inventory live-handbook-only material; the reverse live-handbook "
            "provenance audit remains OPEN, so zero is not evidence that no "
            "unsupported addition exists.",
            "",
            "| Normalized contract class | Printed intervals | Lines in those intervals |",
            "|---|---:|---:|",
        ]
    )
    for classification in CONTRACT_CLASS_ORDER:
        lines.append(
            f"| {classification} | {class_interval_counts[classification]:,} | "
            f"{class_line_counts[classification]:,} |"
        )

    lines.extend(
        [
            "",
            "## Content-bearing preamble obligations",
            "",
            "These intervals are preserved from the audit's preamble inventory "
            "but are excluded from printed-body coverage and class counts. The "
            "first audit row includes implementation/layout data because the "
            "audit itself recorded that obligation; its original class and "
            "wording remain unchanged.",
            "",
            "| Stable ID | Source lines | Audit | Controlling function | Original class |",
            "|---|---:|---|---|---|",
        ]
    )
    for item in preamble:
        lines.append(
            f"| `{item.stable_id}` | {item.source_start}--{item.source_end} | "
            f"`{item.audit_locator}` | "
            f"{markdown_escape(item.source_surface_description)} | "
            f"{markdown_escape(item.class_original)} |"
        )

    lines.extend(
        [
            "",
            "## Nonprinted document controls",
            "",
            "These controls came from five-column audit rows but lie outside the "
            "printed bounds and therefore do not contribute to printed-body "
            "coverage or classification counts.",
            "",
            "| Stable ID | Source lines | Audit source locator | Audit |",
            "|---|---:|---|---|",
        ]
    )
    for item in controls:
        span = (
            str(item.source_start)
            if item.source_start == item.source_end
            else f"{item.source_start}--{item.source_end}"
        )
        lines.append(
            f"| `{item.stable_id}` | {span} | "
            f"{markdown_escape(item.audit_source_locator)} | "
            f"`{item.audit_locator}` |"
        )

    lines.extend(
        [
            "",
            "## Complete interval-audit baseline",
            "",
            "See `spec/inherited-source-map.csv`. This is not yet the complete "
            "contract provenance map: typed handbook destinations, stable labels, "
            "per-dimension completion evidence, and independent verification remain "
            "open. Each row currently supplies the stable "
            "interval ID, literal inclusive source bounds and digest, audit "
            "file/line, source-surface description, audited-snapshot locator/evidence, exact "
            "original class string, normalized count classes, and exact "
            "restoration obligation.",
            "",
        ]
    )
    return "\n".join(lines)


def write_or_check(path: Path, content: str, *, check: bool) -> bool:
    if check:
        if not path.exists():
            print(f"missing generated file: {relative_display(path)}", file=sys.stderr)
            return False
        existing = path.read_text(encoding="utf-8")
        if existing != content:
            print(f"stale generated file: {relative_display(path)}", file=sys.stderr)
            return False
        return True
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument(
        "--audit",
        type=Path,
        action="append",
        help="five-column audit note; repeat for each note (defaults to all three)",
    )
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MARKDOWN)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify that generated files are current without rewriting them",
    )
    args = parser.parse_args()

    validate_class_parser()
    audit_paths = args.audit or list(DEFAULT_AUDITS)
    if not args.audit:
        for path in audit_paths:
            relative = path.resolve().relative_to(REPO_ROOT).as_posix()
            expected = FROZEN_AUDIT_SHA256[relative]
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
            if actual != expected:
                raise ValueError(
                    f"{relative}: audit authority drifted ({actual}, expected {expected})"
                )
    source = source_file(args.source)
    rows = [row for path in audit_paths for row in parse_audit(path)]
    intervals = complete_and_validate_body(expand_rows(rows, source), source)

    csv_output = csv_text(intervals)
    markdown_output = markdown_text(intervals, rows, source, audit_paths)
    current = write_or_check(args.csv, csv_output, check=args.check)
    current &= write_or_check(args.markdown, markdown_output, check=args.check)
    if not current:
        return 1

    mode = "verified" if args.check else "wrote"
    print(
        f"{mode} {len(intervals):,} intervals; printed source "
        f"{source.printed_first}--{source.printed_last} is covered exactly once"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

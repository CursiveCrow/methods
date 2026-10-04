#!/usr/bin/env python3
"""Validate and render the lossless SRC-023 integration ledger.

The note contains three authoritative Markdown tables and one pre-existing
90-line topic list.  This focused checker maps only mechanically explicit
numbering depths to Markdown hierarchy levels, serializes every other row as
an OPEN topic, and proves exact table-to-ledger equality.  It does not read or
write the acquisition baseline.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_NOTE = ROOT / "spec/research/acquisition-src-023.md"

OUTER_HEADING = "## Source hierarchy and printed units"
PUBLISHER_HEADING = "## Complete acquired Chapter 2 printed heading hierarchy"
AUTHOR_HEADING = "## Complete author-hosted Chapter 2 contents hierarchy"
HTTPS_HEADING = "## Patch-ready HTTPS locator ledger"
NON_HTTPS_HEADING = "## Non-HTTPS locators preserved from source displays"
OLD_TOPIC_HEADING = "## Patch-ready topic ledger"
LEDGER_HEADING = "## Patch-ready hierarchy-and-topic ledger"
COUNTS_HEADING = "## Exact integration counts and deltas"
AFTER_OLD_LEDGER_HEADING = "## Acquisition and verification counts"

OUTER_COLUMNS = (
    "No.",
    "Source level",
    "Exact source display or printed unit",
    "Author/editor display",
    "Printed span or delivered extent",
    "Identifier / locator",
    "Acquisition state",
)
PUBLISHER_COLUMNS = ("PDF page", "Exact detected printed heading")
AUTHOR_COLUMNS = ("No.", "Exact contents title", "Author-manifestation page")

ORIGINAL_TOPIC_COUNT = 90
ORIGINAL_TOPIC_SHA256 = "95cac18ae5b900e5c8c8c4ec522e276bf59d0a15632dbf95e87a4bc5cb69193e"
HTTPS_COUNT = 61
HTTPS_SHA256 = "a12bf9aeb3e40ef3628fd05e4549d9c213112bbf41ef3a5cb5718e817399979a"
NON_HTTPS_COUNT = 8
NON_HTTPS_SHA256 = "b6228c875ce570d7e4f5fc65aca05fbeffa1ed219fa8d448b5b84c7edbaa8e55"

OPEN_SUFFIX = " — **OPEN**"
HEADING_RE = re.compile(r"^(?P<marks>#{4,6}) .+$")
NUMBERED_TOPIC_RE = re.compile(r"^(?P<number>\d+)\. .+$")
RETAINED_TOPIC_RE = re.compile(
    r"^- Retained original topic (?P<record>\d{3}) — "
    r"(?P<topic>\d+\. .+) — \*\*OPEN\*\*$"
)


def fail(message: str) -> "NoReturn":
    raise ValueError(message)


def read_note(path: Path) -> tuple[bytes, list[str]]:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        fail("UTF-8 BOM is not allowed")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        fail(f"not valid UTF-8: {error}")
    if "\r" in text:
        fail("CR characters are not allowed; LF line endings are required")
    if not text.endswith("\n"):
        fail("the note must end with one LF")
    if text.endswith("\n\n"):
        fail("the note must end with exactly one LF")
    lines = text.splitlines()
    for number, line in enumerate(lines, start=1):
        if line != line.rstrip(" \t"):
            fail(f"line {number} has trailing whitespace")
    return raw, lines


def unique_index(lines: list[str], value: str) -> int:
    matches = [index for index, line in enumerate(lines) if line == value]
    if len(matches) != 1:
        fail(f"expected one {value!r}, found {len(matches)}")
    return matches[0]


def split_table_row(line: str, line_number: int) -> tuple[str, ...]:
    if not line.startswith("|") or not line.endswith("|"):
        fail(f"line {line_number} is not a complete Markdown table row")
    return tuple(cell.strip() for cell in line[1:-1].split("|"))


def table_after(
    lines: list[str], heading: str, columns: tuple[str, ...]
) -> list[tuple[str, ...]]:
    heading_index = unique_index(lines, heading)
    try:
        header_index = next(
            index
            for index in range(heading_index + 1, len(lines))
            if lines[index].startswith("|")
        )
    except StopIteration:
        fail(f"{heading}: table is missing")
    header = split_table_row(lines[header_index], header_index + 1)
    if header != columns:
        fail(f"{heading}: header mismatch: {header!r}")
    if header_index + 1 >= len(lines) or not lines[header_index + 1].startswith("|"):
        fail(f"{heading}: separator row is missing")
    rows: list[tuple[str, ...]] = []
    index = header_index + 2
    while index < len(lines) and lines[index].startswith("|"):
        row = split_table_row(lines[index], index + 1)
        if len(row) != len(columns):
            fail(f"{heading}: line {index + 1} has {len(row)} cells")
        rows.append(row)
        index += 1
    if not rows:
        fail(f"{heading}: table has no data rows")
    return rows


def numbered_rows_in_h2_section(lines: list[str], heading: str) -> list[str]:
    start = unique_index(lines, heading)
    end = next(
        (index for index in range(start + 1, len(lines)) if lines[index].startswith("## ")),
        len(lines),
    )
    rows = [line for line in lines[start + 1 : end] if NUMBERED_TOPIC_RE.fullmatch(line)]
    return rows


def rows_sha256(rows: list[str]) -> str:
    return hashlib.sha256(("\n".join(rows) + "\n").encode("utf-8")).hexdigest()


def original_topics(lines: list[str]) -> list[str]:
    if OLD_TOPIC_HEADING in lines:
        topics = numbered_rows_in_h2_section(lines, OLD_TOPIC_HEADING)
    else:
        start = unique_index(lines, LEDGER_HEADING)
        end = unique_index(lines, COUNTS_HEADING)
        topics = []
        records = []
        for line in lines[start + 1 : end]:
            match = RETAINED_TOPIC_RE.fullmatch(line)
            if match is not None:
                records.append(int(match.group("record")))
                topics.append(match.group("topic"))
        if records != list(range(1, ORIGINAL_TOPIC_COUNT + 1)):
            fail("retained original-topic record IDs are not unique and dense 001-090")
    topic_numbers = []
    for topic in topics:
        match = NUMBERED_TOPIC_RE.fullmatch(topic)
        if match is None:
            fail(f"malformed original topic: {topic!r}")
        topic_numbers.append(int(match.group("number")))
    if topic_numbers != list(range(1, ORIGINAL_TOPIC_COUNT + 1)):
        fail("original topic numbers are not unique and dense 1-90")
    if rows_sha256(topics) != ORIGINAL_TOPIC_SHA256:
        fail("the original 90 topic strings changed or were reordered")
    return topics


def unquote_single_code_span(value: str) -> str:
    if value.startswith("`") and value.endswith("`") and value.count("`") == 2:
        return value[1:-1]
    fail(f"expected one exact code-span cell, found {value!r}")


def publisher_level(title_cell: str) -> int | None:
    title = unquote_single_code_span(title_cell)
    numeric = re.match(r"^(?P<number>\d+(?:\.\d+)*)\s", title)
    if numeric is not None:
        # The first component is the printed chapter number.  The remainder is
        # the mechanically explicit chapter-internal level.
        return len(numeric.group("number").split(".")) - 1
    appendix = re.match(r"^(?P<number>A(?:\.\d+)?)\s", title)
    if appendix is not None:
        return len(appendix.group("number").split("."))
    return None


def author_level(number_cell: str) -> int | None:
    if re.fullmatch(r"\d+", number_cell) or number_cell == "A":
        return 1
    if re.fullmatch(r"\d+\.\d+", number_cell):
        return 2
    return None


def outer_record(number: int, row: tuple[str, ...]) -> str:
    labels = OUTER_COLUMNS
    fields = " — ".join(f"{label}: {value}" for label, value in zip(labels, row))
    return f"- Source hierarchy table row {number:03d} — {fields}{OPEN_SUFFIX}"


def publisher_record(number: int, row: tuple[str, ...]) -> str:
    body = (
        f"Publisher printed-heading table row {number:03d} — "
        f"PDF page: {row[0]} — Exact detected printed heading: {row[1]}"
    )
    level = publisher_level(row[1])
    if level == 1:
        return f"##### {body}"
    if level == 2:
        return f"###### {body}"
    return f"- {body}{OPEN_SUFFIX}"


def publisher_records(rows: list[tuple[str, ...]]) -> list[str]:
    records: list[str] = []
    for number, row in enumerate(rows, start=1):
        if publisher_level(row[1]) is None and number in {68, 80}:
            exact_title = unquote_single_code_span(row[1])
            records.extend(
                [
                    "",
                    f"#### Publisher printed presentation — {exact_title}",
                    "",
                ]
            )
        records.append(publisher_record(number, row))
    return records


def author_record(number: int, row: tuple[str, ...]) -> str:
    body = (
        f"Author contents table row {number:03d} — No.: {row[0]} — "
        f"Exact contents title: {row[1]} — Author-manifestation page: {row[2]}"
    )
    level = author_level(row[0])
    if level == 1:
        return f"##### {body}"
    if level == 2:
        return f"###### {body}"
    return f"- {body}{OPEN_SUFFIX}"


def author_records(rows: list[tuple[str, ...]]) -> list[str]:
    records: list[str] = []
    for number, row in enumerate(rows, start=1):
        if author_level(row[0]) is None and number == 68:
            exact_title = unquote_single_code_span(row[1])
            records.extend(
                [
                    "",
                    f"#### Author contents presentation — {exact_title}",
                    "",
                ]
            )
        records.append(author_record(number, row))
    return records


def ledger_lines(
    outer: list[tuple[str, ...]],
    publisher: list[tuple[str, ...]],
    author: list[tuple[str, ...]],
    topics: list[str],
) -> list[str]:
    lines = [
        LEDGER_HEADING,
        "",
        "Every row below is separately OPEN. No row selects, merges, normalizes, corrects,",
        "reconciles, or substitutes for another presentation.",
        "",
        "#### Source hierarchy and printed units",
        "",
    ]
    lines.extend(outer_record(number, row) for number, row in enumerate(outer, start=1))
    lines.extend(["", "#### Complete acquired Chapter 2 printed heading hierarchy", ""])
    lines.extend(publisher_records(publisher))
    lines.extend(["", "#### Complete author-hosted Chapter 2 contents hierarchy", ""])
    lines.extend(author_records(author))
    lines.extend(["", "#### Patch-ready topic ledger", ""])
    lines.extend(
        f"- Retained original topic {number:03d} — {topic}{OPEN_SUFFIX}"
        for number, topic in enumerate(topics, start=1)
    )
    return lines


def observed_counts(ledger: list[str]) -> dict[str, int]:
    counts = {"h4": 0, "h5": 0, "h6": 0, "topics": 0}
    for line in ledger:
        match = HEADING_RE.fullmatch(line)
        if match is not None:
            counts[f"h{len(match.group('marks'))}"] += 1
        elif line.startswith("- "):
            if not line.endswith(OPEN_SUFFIX):
                fail(f"ledger topic lacks exact OPEN suffix: {line!r}")
            counts["topics"] += 1
    return counts


def count_lines() -> list[str]:
    return [
        COUNTS_HEADING,
        "",
        "- Exact HTTPS locators: 61.",
        "- Exact non-HTTPS locators: 8.",
        "- Exact hierarchy headings: 98.",
        "- Displayed hierarchy headings: 7 H4 + 18 H5 + 73 H6 = 98; 14 outer/book, 80 publisher internal, and 68 author contents table rows are each represented exactly once.",
        "- Separate OPEN topics: 161; 90 retained originals + 14 outer-table rows + 54 publisher rows without an admissible H5/H6 level + 3 author rows without an admissible H5/H6 level.",
        "- These are acquisition-ledger counts, not evidence of content completeness.",
    ]


def inputs(lines: list[str]) -> tuple[
    list[tuple[str, ...]],
    list[tuple[str, ...]],
    list[tuple[str, ...]],
    list[str],
]:
    outer = table_after(lines, OUTER_HEADING, OUTER_COLUMNS)
    publisher = table_after(lines, PUBLISHER_HEADING, PUBLISHER_COLUMNS)
    author = table_after(lines, AUTHOR_HEADING, AUTHOR_COLUMNS)
    topics = original_topics(lines)
    if len(outer) != 14:
        fail(f"outer/book table has {len(outer)} rows, expected 14")
    if len(publisher) != 80:
        fail(f"publisher heading table has {len(publisher)} rows, expected 80")
    if len(author) != 68:
        fail(f"author contents table has {len(author)} rows, expected 68")
    return outer, publisher, author, topics


def verify_locator_ledgers(lines: list[str]) -> None:
    https = numbered_rows_in_h2_section(lines, HTTPS_HEADING)
    non_https = numbered_rows_in_h2_section(lines, NON_HTTPS_HEADING)
    if len(https) != HTTPS_COUNT or rows_sha256(https) != HTTPS_SHA256:
        fail("the 61-row HTTPS locator ledger changed or was reordered")
    if len(non_https) != NON_HTTPS_COUNT or rows_sha256(non_https) != NON_HTTPS_SHA256:
        fail("the 8-row non-HTTPS locator ledger changed or was reordered")


def validate(path: Path) -> None:
    raw, lines = read_note(path)
    verify_locator_ledgers(lines)
    outer, publisher, author, topics = inputs(lines)
    expected = ledger_lines(outer, publisher, author, topics) + [""]
    start = unique_index(lines, LEDGER_HEADING)
    end = unique_index(lines, COUNTS_HEADING)
    actual = lines[start:end]
    if actual != expected:
        mismatch = next(
            (
                number
                for number, (left, right) in enumerate(zip(actual, expected), start=1)
                if left != right
            ),
            min(len(actual), len(expected)) + 1,
        )
        fail(
            f"ledger differs from the exact table/topic projection at ledger line {mismatch}; "
            f"actual {len(actual)} lines, expected {len(expected)}"
        )
    if lines[end:] != count_lines():
        fail("the final count block is not exact or is not the final note content")
    counts = observed_counts(actual)
    expected_counts = {"h4": 7, "h5": 18, "h6": 73, "topics": 161}
    if counts != expected_counts:
        fail(f"count mismatch: observed {counts}, expected {expected_counts}")
    record_lines = [
        line
        for line in actual
        if " table row " in line or "Retained original topic " in line
    ]
    if len(record_lines) != 14 + 80 + 68 + 90:
        fail("one or more table/topic records are missing")
    if len(record_lines) != len(set(record_lines)):
        fail("table/topic records are not unique")
    print("SRC-023 acquisition ledger: PASS")
    print(f"note_sha256={hashlib.sha256(raw).hexdigest()}")
    print("outer_rows=14")
    print("publisher_rows=80")
    print("author_rows=68")
    print("retained_original_topics=90")
    print("h4=7")
    print("h5=18")
    print("h6=73")
    print("hierarchy_total=98")
    print("topics=161")
    print("https_locators=61")
    print("non_https_locators=8")
    print("encoding=utf-8")
    print("line_endings=LF")
    print("trailing_whitespace=none")


def emit_patch(path: Path) -> None:
    _, lines = read_note(path)
    verify_locator_ledgers(lines)
    outer, publisher, author, topics = inputs(lines)
    expected_ledger = ledger_lines(outer, publisher, author, topics) + [""]
    if LEDGER_HEADING in lines:
        ledger_start = unique_index(lines, LEDGER_HEADING)
        ledger_end = unique_index(lines, COUNTS_HEADING)
        actual_ledger = lines[ledger_start:ledger_end]
        prefix = 0
        while (
            prefix < len(actual_ledger)
            and prefix < len(expected_ledger)
            and actual_ledger[prefix] == expected_ledger[prefix]
        ):
            prefix += 1
        suffix = 0
        while (
            suffix < len(actual_ledger) - prefix
            and suffix < len(expected_ledger) - prefix
            and actual_ledger[-1 - suffix] == expected_ledger[-1 - suffix]
        ):
            suffix += 1
        if prefix == len(actual_ledger) == len(expected_ledger):
            fail("the ledger already matches; no repair patch is needed")
        old_middle = actual_ledger[prefix : len(actual_ledger) - suffix]
        new_middle = expected_ledger[prefix : len(expected_ledger) - suffix]
        if prefix == 0 or suffix == 0:
            fail("ledger drift has no safe unchanged patch context")
        print("*** Begin Patch")
        print(f"*** Update File: {path}")
        print("@@")
        print(f" {actual_ledger[prefix - 1]}")
        for line in old_middle:
            print(f"-{line}")
        for line in new_middle:
            print(f"+{line}")
        print(f" {actual_ledger[len(actual_ledger) - suffix]}")
        print("*** End Patch")
        return
    old_start = unique_index(lines, OLD_TOPIC_HEADING)
    old_end = unique_index(lines, AFTER_OLD_LEDGER_HEADING)
    old_block = lines[old_start:old_end]
    if not old_block:
        fail("old topic block is empty")
    if lines[-1] != "10. No independent verification against a second lawful complete source was obtained.":
        fail("unexpected note tail; refusing to emit a patch")
    replacement = expected_ledger + count_lines()
    print("*** Begin Patch")
    print(f"*** Update File: {path}")
    print("@@")
    for line in old_block:
        print(f"-{line}")
    print(f" {AFTER_OLD_LEDGER_HEADING}")
    print("@@")
    print(f" {lines[-1]}")
    print("+")
    for line in replacement:
        print(f"+{line}")
    print("*** End Patch")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--note", type=Path, default=DEFAULT_NOTE)
    parser.add_argument("--emit-patch", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = args.note.resolve()
    if args.emit_patch:
        emit_patch(path)
    else:
        validate(path)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, UnicodeError, ValueError) as error:
        print(f"SRC-023 acquisition ledger: FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)

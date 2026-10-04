#!/usr/bin/env python3
"""Replace one acquisition-baseline source block from its exact note ledger.

Necessity: the acquired ledgers can contain hundreds of separately owed rows,
so manually copying them risks silent omission.  Definition: this utility
reads explicitly named locator and hierarchy/topic sections from one
acquisition note, preserves the admitted bounded ledger lines byte-for-byte,
and replaces exactly one matching ``SRC-NNN`` block in the acquisition baseline.
Standing: it is an administrative file transformation, not a content or
logical classification.  Nonredundancy: the coverage generator reads the
baseline but cannot populate it from an acquisition note.  Use: each acquired
source is integrated only after its note supplies exact sections and expected
counts; the normal generators then independently validate the result.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASELINE = ROOT / "spec/research/full-compendium-coverage-baseline.md"
SOURCE_RE = re.compile(r"^### (?P<source_id>SRC-\d{3}) — .+$")
HEADING_RE = re.compile(r"^(?P<marks>#{4,6}) .+$")
NUMBERED_URL_RE = re.compile(
    r"^\d+\. `(?P<url>(?:(?:https?|ftp)://|urn:|mailto:|doi:|ark:/)[^`]+)`$"
)
NUMBERED_LITERAL_RE = re.compile(r"^\d+\. `(?P<value>[^`]+)`$")
ADMITTED_NON_HTTPS_SCHEME_RE = re.compile(
    r"^(?:https?|ftp|git|ssh|urn|mailto|doi|ark):", re.IGNORECASE
)
OPEN_TOPIC_SUFFIX = "— **OPEN**"

# These are exact administrative blocks already used before contiguous source
# ledgers.  They are enumerated as whole one- or two-line blocks so a wrapped,
# edited, duplicated, or newly invented sentence cannot be normalized away.
LEDGER_PREAMBLE_BLOCKS: tuple[tuple[str, ...], ...] = (
    (
        "Every topic row below remains **OPEN**. The hierarchy labels reproduce "
        "the acquisition-note presentation hierarchy. Exact source displays remain "
        "separate; repeated or divergent manifestations are not merged.",
    ),
    (
        "Every bullet is a separate OPEN record. No row stands for the content of",
        "another row, and no difference is resolved by preference.",
    ),
    (
        "Every topic and hierarchy entry below remains **OPEN**. The hierarchy labels",
        "and source forms are retained without replacement or normalization.",
    ),
    (
        "Every heading and bullet below is one separately countable baseline entry. "
        "The internal Contents rows already transcribed above are repeated here because "
        "this ledger is the patch-ready integration source; none is summarized by a count.",
    ),
    ("Every bullet is a separate OPEN record. No row stands for another row.",),
    (
        "Every bullet is one separate OPEN record. No row stands for, corrects,",
        "compresses, merges, or replaces another row.",
    ),
    (
        "Every bullet is one separate OPEN record. No bullet stands for another bullet.",
    ),
    (
        "Every bullet is one separate OPEN record. No bullet supplies another bullet's content.",
    ),
    (
        "Every bullet is one separate OPEN record. No row stands for, corrects, compresses,",
        "merges, summarizes, normalizes, or replaces another row.",
    ),
    (
        "Every bullet below is one separate OPEN record. No bullet substitutes for another bullet.",
    ),
    ("Every bullet is one independently OPEN record.",),
    (
        "Every bullet is one independently OPEN record; no aggregate row substitutes "
        "for any retained source row.",
    ),
    ("Every bullet is one separately OPEN record.",),
    ("Every bullet in this ledger is one separately OPEN record.",),
    (
        "Every generated topic below is a separate OPEN record. No record substitutes "
        "for another record.",
    ),
    (
        "Every row below is separately OPEN. No row is a pointer to, aggregate replacement "
        "for, normalization of, or substitute for another row.",
    ),
    ("Every bullet below is one separately OPEN record.",),
    (
        "Every bullet below is one separately OPEN record. No bullet is a pointer to, "
        "aggregate replacement for, normalization of, or substitute for another record.",
    ),
    (
        "Every row below is separately OPEN. No row selects, merges, normalizes, corrects, "
        "reconciles, or substitutes for another presentation.",
    ),
    (
        "Every topic row below is separately OPEN. No topic selects, merges, normalizes, "
        "corrects, reconciles, compresses, or substitutes for another presentation.",
    ),
)

# Lines after the declared ledger end are administrative count/gate statements,
# not silently discarded source records.  Exact field labels give these lines
# their administrative standing; a lexical prefix such as ``Exact`` or
# ``Source`` is deliberately insufficient.
POST_LEDGER_COUNT_FIELD_LABELS = frozenset(
    {
        "Acquired PDF manifestations",
        "Acquired PDF pages",
        "Acquired PDF physical pages",
        "Acquired PDF presentations",
        "Acquired or renderer-derived PDF physical pages visually inspected",
        "Acquired public image-asset manifestations",
        "Acquired repository checkouts",
        "Acquired source bodies",
        "Cambridge Contents rows",
        "Crossref ISBN-query items retained in returned order",
        "Direct lawful-source acquisition requests",
        "Direct primary acquisition requests",
        "Displayed hierarchy headings",
        "Distinct acquired PDF manifestations",
        "Distinct locally acquired PDF manifestations",
        "Distinct official PDF manifestations",
        "Duplicate PDF audit sheets proven byte-identical to an opened presentation",
        "Exact DBLP keyed-body and keyed-export gap rows represented separately",
        "Exact HTTPS locators",
        "Exact citation-export body gap rows represented separately",
        "Exact coexistence and conflict rows represented separately",
        "Exact exposed asset rows represented separately",
        "Exact exposed export rows represented separately",
        "Exact hierarchy headings",
        "Exact indexed access-response rows represented separately",
        "Exact indexed source rows represented separately",
        "Exact institutional contents items represented separately",
        "Exact locator and identifier occurrences represented separately",
        "Exact non-HTTPS locators",
        "Exact retained scratch bytes",
        "Exact retained scratch files",
        "Exact scheme-less identifiers",
        "Exact scheme-less locators",
        "Exact separately retained coexistence rows represented separately",
        "Exact versioned HTML and indexed PDF source rows represented separately",
        "Exact versioned manual indexed source rows represented separately",
        "Hierarchy headings",
        "Indexed application/pdf renderer manifestations with reported page counts",
        "Literal OCR lines",
        "Locally rendered and visually inspected PDF pages",
        "Markdown table presentations",
        "Mechanically extracted PDF table cells retained",
        "Mechanically extracted PDF table rows retained",
        "Mechanically extracted PDF tables retained",
        "OCR page presentations",
        "Opened and inspected PDF contact-sheet visual presentations",
        "Patch-ledger top-level file manifestations",
        "PDF render audit",
        "Replacement delta",
        "Rendered PDF pages",
        "Rendered acquired PDF pages",
        "Rendered acquired PDF physical pages",
        "Rendered and visually inspected PDF pages",
        "Retained PDF audit sheets",
        "Retained PDF contact sheets",
        "Retained physical-page PNG renders",
        "Retained scratch artifacts represented",
        "Retained visually inspected contact sheets",
        "Scratch inventory",
        "Separate OPEN topics",
        "Separate copied SRC-045 provenance-bearing artifacts",
        "Separate direct-response stderr artifacts",
        "Separate indexed renderer or indexed access-response artifacts",
        "Separate zero-byte direct-response header artifacts",
        "Separately retained public web-discovery presentation groups",
        "Separately retained repository-clone access-failure presentations",
        "Separately retained sandbox HTTP access-failure presentations",
        "Separately retained sandbox access-failure presentations",
        "Separately retained web-discovery access-response presentations",
        "Source-hierarchy headings",
        "Unique PDF audit-sheet visual presentations opened and inspected",
        "Visually inspected PDF JPEG contact sheets",
        "Visually inspected PDF contact sheets",
        "Visually inspected PDF pages",
        "Visually inspected acquired PDF pages",
        "Visually inspected acquired PDF physical pages",
        "Visually inspected public image presentations",
        "Visually inspected public image-asset manifestations",
    }
)
POST_LEDGER_GATE_FIELD_LABELS = frozenset(
    {
        "Acquisition gate",
        "Build gate",
        "Human-content gate",
        "Reproduction gate",
        "Rights gate",
        "Source gate",
        "Static gate",
        "Visual gate",
    }
)
POST_LEDGER_EXACT_PROSE = frozenset(
    {
        "- All acquisition, rights, source, static, build, visual, human, and reproduction gates remain OPEN.",
        "- All acquisition, rights, source, static, build, visual, human-content, reproduction, and completeness gates remain OPEN.",
        "- Source, static, build, visual, human-content, and reproduction gates remain separately **OPEN**.",
        "- These are acquisition-ledger counts, not evidence of content completeness.",
        "- These are acquisition-ledger counts, not evidence of content completeness or reproduction authority.",
    }
)
POST_LEDGER_FIELD_RE = re.compile(
    r"^- (?P<label>[^:\n]+): (?P<value>\S.*[.:])$"
)
POST_LEDGER_COUNT_VALUE_RE = re.compile(r"^[+]?\d[\d,]*.*\.$")
POST_LEDGER_LIVE_FIELD_RE = re.compile(
    r"^Live SRC-\d{3} baseline (?:HTTPS locators|non-HTTPS locators|"
    r"scheme-less identifiers|hierarchy headings|topics) before integration$"
)
POST_LEDGER_PRIOR_FIELD_RE = re.compile(r"^Prior SRC-\d{3} baseline$")
POST_LEDGER_DIGEST_RE = re.compile(r"^`[0-9A-Fa-f]{64}`\.$")
POST_LEDGER_DESCRIPTIVE_FIELD_LABELS = frozenset(
    {"Acquired PDF manifestations", "Acquired PDF presentations"}
)
FINAL_OPEN_ADMIN_RE = re.compile(
    r"^(?:SRC-\d{3}|No |All |Every ).*(?:gate|gates|record|presentation|body|"
    r"source|content|acquisition|rights|static|build|visual|human|reproduction)"
    r".*\*\*OPEN\*\*\.$",
    re.IGNORECASE,
)


def read_lines(path: Path) -> list[str]:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ValueError(f"{path}: UTF-8 BOM is not allowed")
    text = raw.decode("utf-8")
    if "\r" in text:
        raise ValueError(f"{path}: CR characters are not allowed")
    return text.splitlines()


def unique_heading_index(lines: list[str], heading: str, path: Path) -> int:
    matches = [index for index, line in enumerate(lines) if line == heading]
    if len(matches) != 1:
        raise ValueError(
            f"{path}: expected one {heading!r} heading, found {len(matches)}"
        )
    return matches[0]


def numbered_urls(
    lines: list[str], start_heading: str, end_heading: str, path: Path
) -> list[str]:
    start = unique_heading_index(lines, start_heading, path)
    end = unique_heading_index(lines, end_heading, path)
    if end <= start:
        raise ValueError(f"{path}: locator section boundaries are reversed")
    urls: list[str] = []
    expected_number = 1
    for line_number, line in enumerate(lines[start + 1 : end], start=start + 2):
        if not line:
            continue
        match = NUMBERED_URL_RE.fullmatch(line)
        if match is None:
            raise ValueError(f"{path}:{line_number}: malformed locator row {line!r}")
        actual_number = int(line.split(".", 1)[0])
        if actual_number != expected_number:
            raise ValueError(f"{path}:{line_number}: expected locator {expected_number}")
        urls.append(match.group("url"))
        expected_number += 1
    return urls


def numbered_exact_values(
    lines: list[str], start_heading: str, end_heading: str, path: Path
) -> list[str]:
    """Read a numbered ledger whose rows may carry provenance after the value."""

    start = unique_heading_index(lines, start_heading, path)
    end = unique_heading_index(lines, end_heading, path)
    if end <= start:
        raise ValueError(f"{path}: locator section boundaries are reversed")
    values: list[str] = []
    pattern = re.compile(r"^\d+\. `(?P<value>[^`]+)`(?: .*)?$")
    expected_number = 1
    for line_number, line in enumerate(lines[start + 1 : end], start=start + 2):
        if not line:
            continue
        match = pattern.fullmatch(line)
        if match is None:
            raise ValueError(f"{path}:{line_number}: malformed exact-value row {line!r}")
        actual_number = int(line.split(".", 1)[0])
        if actual_number != expected_number:
            raise ValueError(f"{path}:{line_number}: expected locator {expected_number}")
        values.append(match.group("value"))
        expected_number += 1
    return values


def numbered_literals(
    lines: list[str], start_heading: str, end_heading: str, path: Path
) -> list[str]:
    """Read an exact numbered literal ledger without assigning URI semantics."""

    start = unique_heading_index(lines, start_heading, path)
    end = unique_heading_index(lines, end_heading, path)
    if end <= start:
        raise ValueError(f"{path}: literal-ledger boundaries are reversed")
    values: list[str] = []
    expected_number = 1
    for line_number, line in enumerate(lines[start + 1 : end], start=start + 2):
        if not line:
            continue
        match = NUMBERED_LITERAL_RE.fullmatch(line)
        if match is None:
            raise ValueError(f"{path}:{line_number}: malformed literal row {line!r}")
        actual_number = int(line.split(".", 1)[0])
        if actual_number != expected_number:
            raise ValueError(f"{path}:{line_number}: expected literal {expected_number}")
        values.append(match.group("value"))
        expected_number += 1
    return values


def ledger_rows_without_preamble(
    rows: list[tuple[int, str]], path: Path
) -> list[tuple[int, str]]:
    """Remove at most one exact, contiguous pre-content administrative block."""

    first_content = next(
        (
            index
            for index, (_, line) in enumerate(rows)
            if HEADING_RE.fullmatch(line) is not None or line.startswith("- ")
        ),
        len(rows),
    )
    prefix = rows[:first_content]
    nonblank = [index for index, (_, line) in enumerate(prefix) if line]
    if not nonblank:
        return rows

    block_start, block_end = nonblank[0], nonblank[-1] + 1
    block_rows = prefix[block_start:block_end]
    block = tuple(line for _, line in block_rows)
    if any(not line for line in block) or block not in LEDGER_PREAMBLE_BLOCKS:
        line_number = block_rows[0][0]
        raise ValueError(
            f"{path}:{line_number}: untyped or inexact pre-content ledger block {block!r}"
        )
    return rows[:block_start] + rows[block_end:]


def is_typed_post_ledger_admin(line: str) -> bool:
    """Recognize only exact administrative labels with their admitted value type."""

    if line in POST_LEDGER_EXACT_PROSE:
        return True
    match = POST_LEDGER_FIELD_RE.fullmatch(line)
    if match is None:
        return False
    label, value = match.group("label"), match.group("value")
    if label in POST_LEDGER_GATE_FIELD_LABELS:
        return value == "OPEN."
    if label == "Exact scratch inventory row serialization SHA-256":
        return POST_LEDGER_DIGEST_RE.fullmatch(value) is not None
    if label in POST_LEDGER_DESCRIPTIVE_FIELD_LABELS and re.fullmatch(
        r"(?:one|five)\b.*\.", value
    ):
        return True
    return (
        label in POST_LEDGER_COUNT_FIELD_LABELS
        or POST_LEDGER_LIVE_FIELD_RE.fullmatch(label) is not None
        or POST_LEDGER_PRIOR_FIELD_RE.fullmatch(label) is not None
    ) and POST_LEDGER_COUNT_VALUE_RE.fullmatch(value) is not None


def validate_post_ledger(
    lines: list[str], end: int, end_heading: str, path: Path
) -> None:
    """Reject source rows or untyped prose after the declared ledger boundary."""

    for line_number, line in enumerate(lines[end + 1 :], start=end + 2):
        if not line:
            continue
        if HEADING_RE.fullmatch(line) is not None or line.endswith(OPEN_TOPIC_SUFFIX):
            raise ValueError(
                f"{path}:{line_number}: source record occurs after the declared ledger end: {line!r}"
            )
        if is_typed_post_ledger_admin(line):
            continue
        if (
            end_heading == "## Final OPEN statement"
            and FINAL_OPEN_ADMIN_RE.fullmatch(line) is not None
        ):
            continue
        raise ValueError(
            f"{path}:{line_number}: untyped content occurs after the declared ledger end: {line!r}"
        )


def exact_ledger(
    lines: list[str], start_heading: str, end_heading: str, path: Path
) -> tuple[list[str], int, int]:
    start = unique_heading_index(lines, start_heading, path)
    end = unique_heading_index(lines, end_heading, path)
    if end <= start:
        raise ValueError(f"{path}: ledger section boundaries are reversed")

    rows = list(enumerate(lines[start + 1 : end], start=start + 2))
    admitted_rows = ledger_rows_without_preamble(rows, path)
    output: list[str] = []
    for line_number, line in admitted_rows:
        if HEADING_RE.fullmatch(line) is not None:
            output.append(line)
            continue
        if not line:
            output.append(line)
            continue
        if line.startswith("- "):
            if not line.endswith(OPEN_TOPIC_SUFFIX):
                raise ValueError(f"{path}:{line_number}: topic lacks exact OPEN suffix")
            output.append(line)
            continue
        raise ValueError(f"{path}:{line_number}: untyped ledger line {line!r}")

    validate_post_ledger(lines, end, end_heading, path)
    hierarchy_count = sum(HEADING_RE.fullmatch(line) is not None for line in output)
    topics = [line for line in output if line.startswith("- ")]
    return output, hierarchy_count, len(topics)


def source_range(lines: list[str], source_id: str, path: Path) -> tuple[int, int]:
    starts = [
        index
        for index, line in enumerate(lines)
        if (match := SOURCE_RE.fullmatch(line)) is not None
        and match.group("source_id") == source_id
    ]
    if len(starts) != 1:
        raise ValueError(
            f"{path}: expected one {source_id} source block, found {len(starts)}"
        )
    start = starts[0]
    later = [
        index
        for index in range(start + 1, len(lines))
        if SOURCE_RE.fullmatch(lines[index]) is not None or lines[index] == "---"
    ]
    if not later:
        raise ValueError(f"{path}: {source_id} has no closing boundary")
    return start, later[0]


def base_metadata(block: list[str], path: Path, source_id: str) -> list[str]:
    try:
        retrieval_index = next(
            index
            for index, line in enumerate(block)
            if line.startswith("- Retrieved granularity:")
        )
    except StopIteration as error:
        raise ValueError(f"{path}: {source_id} has no retrieved-granularity field") from error

    excluded = (
        "- Exact HTTPS locator ",
        "- Exact non-HTTPS locator ",
        "- Exact scheme-less identifier ",
        "- Exact scheme-less identifier:",
    )
    retained = [
        line
        for line in block[1:retrieval_index]
        if line.startswith("- ") and not line.startswith(excluded)
    ]
    if not retained:
        raise ValueError(f"{path}: {source_id} has no retained source metadata")
    return retained


def replacement_source_block(
    old_block: list[str], note_lines: list[str], args: argparse.Namespace
) -> list[str]:
    expected_level_total = args.expected_h4 + args.expected_h5 + args.expected_h6
    if args.expected_hierarchy != expected_level_total:
        raise ValueError(
            "expected hierarchy aggregate does not equal its level pins: "
            f"{args.expected_hierarchy} != {args.expected_h4} + "
            f"{args.expected_h5} + {args.expected_h6}"
        )
    metadata = base_metadata(old_block, args.baseline, args.source_id)

    value_reader = numbered_exact_values if args.locator_rows_have_provenance else numbered_urls
    https_urls = value_reader(
        note_lines,
        args.https_heading,
        args.https_end_heading or args.non_https_heading,
        args.note,
    )
    non_https_urls = value_reader(
        note_lines,
        args.non_https_heading,
        args.non_https_end_heading or args.ledger_heading,
        args.note,
    )
    if any(not value.startswith("https://") for value in https_urls):
        raise ValueError(f"{args.note}: HTTPS ledger contains a non-HTTPS value")
    if any(
        not ADMITTED_NON_HTTPS_SCHEME_RE.match(value)
        or value.lower().startswith("https:")
        for value in non_https_urls
    ):
        raise ValueError(f"{args.note}: non-HTTPS ledger has a missing or HTTPS scheme")
    ledger, hierarchy_count, topic_count = exact_ledger(
        note_lines, args.ledger_heading, args.ledger_end_heading, args.note
    )
    hierarchy_levels = {"h4": 0, "h5": 0, "h6": 0}
    for line in ledger:
        if heading_match := HEADING_RE.fullmatch(line):
            hierarchy_levels[f"h{len(heading_match.group('marks'))}"] += 1
    scheme_less_identifiers = list(args.scheme_less_identifier)
    if args.scheme_less_heading:
        if scheme_less_identifiers:
            raise ValueError(
                "use either --scheme-less-heading or --scheme-less-identifier, not both"
            )
        scheme_less_identifiers = numbered_literals(
            note_lines,
            args.scheme_less_heading,
            args.scheme_less_end_heading or args.ledger_heading,
            args.note,
        )
    observed = {
        "https": len(https_urls),
        "non_https": len(non_https_urls),
        "scheme_less": len(scheme_less_identifiers),
        "hierarchy": hierarchy_count,
        **hierarchy_levels,
        "topics": topic_count,
    }
    expected = {
        "https": args.expected_https,
        "non_https": args.expected_non_https,
        "scheme_less": args.expected_scheme_less,
        "hierarchy": args.expected_hierarchy,
        "h4": args.expected_h4,
        "h5": args.expected_h5,
        "h6": args.expected_h6,
        "topics": args.expected_topics,
    }
    if observed != expected:
        raise ValueError(f"count mismatch: observed {observed}, expected {expected}")

    output = [old_block[0], "", *metadata]
    for number, url in enumerate(https_urls, start=1):
        output.append(f"- Exact HTTPS locator {number}: {url}")
    for number, url in enumerate(non_https_urls, start=1):
        output.append(f"- Exact non-HTTPS locator {number}: {url}")
    for number, identifier in enumerate(scheme_less_identifiers, start=1):
        output.append(f"- Exact scheme-less identifier {number}: {identifier}")
    output.append(
        "- Retrieved granularity: exact acquisition-note ledger containing "
        f"{len(https_urls)} HTTPS locators, {len(non_https_urls)} non-HTTPS "
        f"locators, {len(scheme_less_identifiers)} scheme-less identifiers, "
        f"{hierarchy_count} displayed hierarchy headings, and {topic_count} "
        "separate topics; every presentation remains OPEN"
    )
    output.append("")
    output.extend(ledger)
    output.append("")
    return output


def build_source_block(args: argparse.Namespace) -> list[str]:
    baseline_lines = read_lines(args.baseline)
    note_lines = read_lines(args.note)
    start, end = source_range(baseline_lines, args.source_id, args.baseline)
    replacement = replacement_source_block(
        baseline_lines[start:end], note_lines, args
    )
    if replacement_source_block(replacement, note_lines, args) != replacement:
        raise ValueError(f"{args.source_id}: replacement block is not a fixed point")
    return replacement


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE)
    parser.add_argument("--note", type=Path, required=True)
    parser.add_argument("--source-id", required=True)
    parser.add_argument(
        "--https-heading", default="## Patch-ready exact HTTPS locator ledger"
    )
    parser.add_argument(
        "--https-end-heading",
        help="end boundary when another section intervenes before the non-HTTPS ledger",
    )
    parser.add_argument(
        "--non-https-heading", default="## Exact non-HTTPS locator ledger"
    )
    parser.add_argument(
        "--non-https-end-heading",
        help="end boundary when the non-HTTPS ledger follows the content ledger",
    )
    parser.add_argument(
        "--ledger-heading", default="## Patch-ready hierarchy-and-topic ledger"
    )
    parser.add_argument(
        "--ledger-end-heading", default="## Exact integration counts and deltas"
    )
    parser.add_argument("--scheme-less-identifier", action="append", default=[])
    parser.add_argument(
        "--locator-rows-have-provenance",
        action="store_true",
        help="allow exact numbered locator values followed by retained provenance text",
    )
    parser.add_argument("--scheme-less-heading")
    parser.add_argument("--scheme-less-end-heading")
    parser.add_argument("--expected-https", type=int, required=True)
    parser.add_argument("--expected-non-https", type=int, required=True)
    parser.add_argument("--expected-scheme-less", type=int, required=True)
    parser.add_argument("--expected-hierarchy", type=int, required=True)
    parser.add_argument("--expected-h4", type=int, required=True)
    parser.add_argument("--expected-h5", type=int, required=True)
    parser.add_argument("--expected-h6", type=int, required=True)
    parser.add_argument("--expected-topics", type=int, required=True)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    args.baseline = args.baseline.resolve()
    args.note = args.note.resolve()
    baseline_lines = read_lines(args.baseline)
    start, end = source_range(baseline_lines, args.source_id, args.baseline)
    replacement = build_source_block(args)
    desired_lines = baseline_lines[:start] + replacement + baseline_lines[end:]
    desired_text = "\n".join(desired_lines) + "\n"
    current_text = args.baseline.read_text(encoding="utf-8")

    if args.check:
        if current_text != desired_text:
            print(f"{args.source_id}: baseline source block is stale", file=sys.stderr)
            return 1
        print(f"{args.source_id}: acquisition-note block matches exactly")
        return 0

    args.baseline.write_text(desired_text, encoding="utf-8", newline="\n")
    print(f"{args.source_id}: acquisition-note block replaced exactly")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, UnicodeError, ValueError) as error:
        print(f"baseline replacement failed: {error}", file=sys.stderr)
        raise SystemExit(1)

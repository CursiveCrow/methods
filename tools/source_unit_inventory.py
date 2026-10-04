#!/usr/bin/env python3
"""Generate a literal structural inventory of the frozen source corpus.

The inventory is evidence, not a summary. Every listed unit carries its exact
inclusive source-line range and a SHA-256 digest of the literal UTF-8 bytes in
that range. A separate whole-file digest covers every byte, including prose,
displays, list items, front matter, bibliography text, and other material that
does not begin an inventoried unit.

TeX written *inside* an opaque listing is data, not an active TeX structure.
The scanner therefore inventories the listing itself while excluding command-
looking strings in its body from active theorem/proof/etc. counts.
"""

from __future__ import annotations

import argparse
import bisect
import csv
import hashlib
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path


HEADING_KINDS = (
    "part",
    "chapter",
    "section",
    "subsection",
    "subsubsection",
)

ENVIRONMENT_KINDS = (
    "definition",
    "theorem",
    "lemma",
    "corollary",
    "proof",
    "proofplan",
    "example",
    "exercise",
    "method",
    "convention",
    "warning",
    "remark",
    "solution",
    "table",
    "figure",
    "longtable",
    "lstlisting",
)

# TeX commands in these bodies are literal data. Only lstlisting occurs in the
# frozen source, but recognizing the other standard verbatim-like environments
# prevents a future source refresh from silently creating false active units.
OPAQUE_ENVIRONMENT_KINDS = (
    "lstlisting",
    "verbatim",
    "verbatim*",
    "Verbatim",
    "BVerbatim",
    "LVerbatim",
    "SaveVerbatim",
    "minted",
)

HEADING_TOKEN_RE = re.compile(
    rf"(?m)^[ \t]*\\(?P<kind>{'|'.join(HEADING_KINDS)})"
    r"(?P<star>\*)?\s*(?P<open>\{)"
)
ENVIRONMENT_TOKEN_RE = re.compile(
    r"\\(?P<command>begin|end)\s*\{\s*(?P<kind>[^{}\s]+)\s*\}"
)
TARGET_BEGIN_RE = re.compile(
    rf"\\begin\s*\{{\s*(?P<kind>{'|'.join(ENVIRONMENT_KINDS)})\s*\}}"
)
LABEL_AT_START_RE = re.compile(r"^[ \t]*\\label\{(?P<label>[^}]+)\}")


@dataclass(frozen=True)
class Unit:
    ordinal: int
    kind: str
    title: str
    label: str
    start_line: int
    end_line: int
    part: str
    chapter: str
    section: str
    sha256: str


@dataclass(frozen=True)
class EnvironmentSpan:
    kind: str
    start_offset: int
    opening_end_offset: int
    end_offset: int
    start_line: int
    end_line: int
    title: str


@dataclass(frozen=True)
class HeadingSpan:
    kind: str
    start_offset: int
    command_end_offset: int
    start_line: int
    end_line: int
    title: str


@dataclass(frozen=True)
class OpaqueSpan:
    kind: str
    start_line: int
    end_line: int


@dataclass(frozen=True)
class IgnoredCommand:
    kind: str
    line: int
    opaque_kind: str


def line_starts(lines: list[str]) -> list[int]:
    starts: list[int] = []
    offset = 0
    for line in lines:
        starts.append(offset)
        offset += len(line)
    return starts


def line_number(starts: list[int], offset: int) -> int:
    """Return the one-based physical line containing ``offset``."""

    return bisect.bisect_right(starts, offset)


def line_without_ending(line: str) -> str:
    return line.rstrip("\r\n")


def spaces_preserving_line_end(line: str) -> str:
    body = line_without_ending(line)
    return " " * len(body) + line[len(body) :]


def mask_range_preserving_line_end(line: str, start: int, end: int) -> str:
    body = line_without_ending(line)
    chars = list(line)
    for index in range(max(0, start), min(end, len(body))):
        chars[index] = " "
    return "".join(chars)


def is_escaped(text: str, position: int) -> bool:
    slashes = 0
    position -= 1
    while position >= 0 and text[position] == "\\":
        slashes += 1
        position -= 1
    return slashes % 2 == 1


def mask_inline_verbatim_and_comments(line: str) -> str:
    """Mask line-local ``\verb`` bodies and TeX comments without reflow."""

    body = line_without_ending(line)
    chars = list(line)
    index = 0
    while index < len(body):
        if (
            body.startswith(r"\verb", index)
            and not is_escaped(body, index)
            and (index + 5 == len(body) or not body[index + 5].isalpha())
        ):
            delimiter_at = index + 5
            if delimiter_at < len(body) and body[delimiter_at] == "*":
                delimiter_at += 1
            if delimiter_at < len(body) and not body[delimiter_at].isspace():
                delimiter = body[delimiter_at]
                close_at = body.find(delimiter, delimiter_at + 1)
                if close_at < 0:
                    raise ValueError(
                        "unterminated inline verbatim command in source line: "
                        + body
                    )
                for masked in range(index, close_at + 1):
                    chars[masked] = " "
                index = close_at + 1
                continue
        if body[index] == "%" and not is_escaped(body, index):
            for masked in range(index, len(body)):
                chars[masked] = " "
            break
        index += 1
    return "".join(chars)


def comment_masked_lines(lines: list[str]) -> list[str]:
    return [mask_inline_verbatim_and_comments(line) for line in lines]


def opaque_patterns() -> tuple[re.Pattern[str], dict[str, re.Pattern[str]]]:
    alternatives = "|".join(re.escape(kind) for kind in OPAQUE_ENVIRONMENT_KINDS)
    begin = re.compile(
        rf"^[ \t]*\\begin\s*\{{\s*(?P<kind>{alternatives})\s*\}}"
    )
    ends = {
        kind: re.compile(rf"^[ \t]*\\end\s*\{{\s*{re.escape(kind)}\s*\}}")
        for kind in OPAQUE_ENVIRONMENT_KINDS
    }
    return begin, ends


def mask_opaque_bodies(lines: list[str]) -> tuple[list[str], list[OpaqueSpan]]:
    """Leave opaque begin/end tokens visible and blank their literal bodies."""

    begin_re, end_res = opaque_patterns()
    masked: list[str] = []
    spans: list[OpaqueSpan] = []
    open_kind = ""
    open_line = 0

    for number, line in enumerate(lines, start=1):
        if open_kind:
            ended = end_res[open_kind].match(line)
            if ended:
                masked.append(mask_range_preserving_line_end(line, ended.end(), len(line)))
                spans.append(OpaqueSpan(open_kind, open_line, number))
                open_kind = ""
                open_line = 0
            else:
                masked.append(spaces_preserving_line_end(line))
            continue

        begun = begin_re.match(line)
        if not begun:
            masked.append(line)
            continue

        kind = begun.group("kind")
        same_line_end = end_res[kind].search(line, begun.end())
        if same_line_end:
            chars = list(spaces_preserving_line_end(line))
            for position in range(begun.start(), begun.end()):
                chars[position] = line[position]
            for position in range(same_line_end.start(), same_line_end.end()):
                chars[position] = line[position]
            masked.append("".join(chars))
            spans.append(OpaqueSpan(kind, number, number))
        else:
            masked.append(mask_range_preserving_line_end(line, begun.end(), len(line)))
            open_kind = kind
            open_line = number

    if open_kind:
        raise ValueError(
            f"unterminated opaque {open_kind} environment beginning at line {open_line}"
        )
    return masked, spans


def matching_group_end(
    text: str, open_offset: int, opening: str, closing: str
) -> int:
    """Return the offset of a balanced closing delimiter."""

    if text[open_offset] != opening:
        raise ValueError(f"expected {opening!r} at source offset {open_offset}")
    depth = 0
    for offset in range(open_offset, len(text)):
        character = text[offset]
        if character == opening and not is_escaped(text, offset):
            depth += 1
        elif character == closing and not is_escaped(text, offset):
            depth -= 1
            if depth == 0:
                return offset
    raise ValueError(f"unterminated {opening}{closing} group at source offset {open_offset}")


def clean_title(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def optional_title(text: str, after_begin: int) -> tuple[str, int]:
    """Read a possibly multiline, balanced optional environment argument."""

    offset = after_begin
    while offset < len(text) and text[offset].isspace():
        offset += 1
    if offset >= len(text) or text[offset] != "[":
        return "", after_begin
    close = matching_group_end(text, offset, "[", "]")
    return clean_title(text[offset + 1 : close]), close + 1


def collect_environment_spans(
    active_text: str,
    lexical_text: str,
    starts: list[int],
) -> list[EnvironmentSpan]:
    stack: list[tuple[str, re.Match[str]]] = []
    spans: list[EnvironmentSpan] = []

    for token in ENVIRONMENT_TOKEN_RE.finditer(active_text):
        command = token.group("command")
        kind = token.group("kind")
        if command == "begin":
            stack.append((kind, token))
            continue

        if not stack:
            raise ValueError(
                f"unmatched \\end{{{kind}}} at line {line_number(starts, token.start())}"
            )
        begun_kind, begun = stack.pop()
        if begun_kind != kind:
            raise ValueError(
                "environment nesting mismatch: "
                f"\\begin{{{begun_kind}}} at line "
                f"{line_number(starts, begun.start())} closed by \\end{{{kind}}} "
                f"at line {line_number(starts, token.start())}"
            )

        if kind not in ENVIRONMENT_KINDS:
            continue
        title, opening_end = optional_title(lexical_text, begun.end())
        spans.append(
            EnvironmentSpan(
                kind=kind,
                start_offset=begun.start(),
                opening_end_offset=opening_end,
                end_offset=token.end(),
                start_line=line_number(starts, begun.start()),
                end_line=line_number(starts, token.start()),
                title=title,
            )
        )

    if stack:
        kind, begun = stack[-1]
        raise ValueError(
            f"unterminated {kind} environment beginning at line "
            f"{line_number(starts, begun.start())}"
        )
    return spans


def collect_heading_spans(active_text: str, starts: list[int]) -> list[HeadingSpan]:
    spans: list[HeadingSpan] = []
    for heading in HEADING_TOKEN_RE.finditer(active_text):
        open_offset = heading.start("open")
        close_offset = matching_group_end(active_text, open_offset, "{", "}")
        kind = heading.group("kind") + ("*" if heading.group("star") else "")
        spans.append(
            HeadingSpan(
                kind=kind,
                start_offset=heading.start(),
                command_end_offset=close_offset + 1,
                start_line=line_number(starts, heading.start()),
                end_line=line_number(starts, close_offset),
                title=clean_title(active_text[open_offset + 1 : close_offset]),
            )
        )
    return spans


def associated_label(
    active_lines: list[str],
    starts: list[int],
    anchor_offset: int,
    maximum_line: int | None,
) -> str:
    """Return only a label syntactically adjacent to a unit's opening.

    A label may follow on the command line or on the first later nonblank,
    noncomment line. Encountering any other token stops the search, so a label
    belonging to a later heading or nested item cannot leak backward.
    """

    anchor_line = line_number(starts, anchor_offset)
    line_start = starts[anchor_line - 1]
    column = anchor_offset - line_start
    tail = line_without_ending(active_lines[anchor_line - 1])[column:]
    same_line = LABEL_AT_START_RE.match(tail)
    if same_line:
        return same_line.group("label")
    if tail.strip():
        return ""

    last = maximum_line if maximum_line is not None else len(active_lines)
    for number in range(anchor_line + 1, last + 1):
        candidate = line_without_ending(active_lines[number - 1])
        if not candidate.strip():
            continue
        labelled = LABEL_AT_START_RE.match(candidate)
        return labelled.group("label") if labelled else ""
    return ""


def digest(lines: list[str], start: int, end: int) -> str:
    literal_bytes = "".join(lines[start - 1 : end]).encode("utf-8")
    return hashlib.sha256(literal_bytes).hexdigest()


def collect(
    lines: list[str],
) -> tuple[list[Unit], list[OpaqueSpan], list[IgnoredCommand]]:
    lexical_lines = comment_masked_lines(lines)
    active_lines, opaque_spans = mask_opaque_bodies(lexical_lines)
    lexical_text = "".join(lexical_lines)
    active_text = "".join(active_lines)
    starts = line_starts(lines)

    environments = collect_environment_spans(active_text, lexical_text, starts)
    headings = collect_heading_spans(active_text, starts)

    active_target_offsets = {span.start_offset for span in environments}
    ignored: list[IgnoredCommand] = []
    for token in TARGET_BEGIN_RE.finditer(lexical_text):
        if token.start() in active_target_offsets:
            continue
        number = line_number(starts, token.start())
        container = next(
            (
                span.kind
                for span in opaque_spans
                if span.start_line <= number <= span.end_line
            ),
            "",
        )
        if not container:
            raise ValueError(
                f"active-looking \\begin{{{token.group('kind')}}} at line {number} "
                "was not inventoried"
            )
        ignored.append(IgnoredCommand(token.group("kind"), number, container))

    events: list[tuple[int, str, HeadingSpan | EnvironmentSpan]] = []
    events.extend((span.start_offset, "heading", span) for span in headings)
    events.extend((span.start_offset, "environment", span) for span in environments)
    events.sort(key=lambda event: event[0])

    context = {"part": "", "chapter": "", "section": ""}
    raw: list[dict[str, object]] = []
    for _, event_type, event in events:
        if event_type == "heading":
            assert isinstance(event, HeadingSpan)
            base_kind = event.kind.removesuffix("*")
            if base_kind == "part":
                context.update(part=event.title, chapter="", section="")
            elif base_kind == "chapter":
                context.update(chapter=event.title, section="")
            elif base_kind == "section":
                context["section"] = event.title
            raw.append(
                {
                    "kind": event.kind,
                    "title": event.title,
                    "label": associated_label(
                        active_lines,
                        starts,
                        event.command_end_offset,
                        None,
                    ),
                    "start_line": event.start_line,
                    "end_line": event.end_line,
                    **context,
                }
            )
            continue

        assert isinstance(event, EnvironmentSpan)
        raw.append(
            {
                "kind": event.kind,
                "title": event.title,
                "label": associated_label(
                    active_lines,
                    starts,
                    event.opening_end_offset,
                    event.end_line,
                ),
                "start_line": event.start_line,
                "end_line": event.end_line,
                **context,
            }
        )

    units: list[Unit] = []
    for ordinal, item in enumerate(raw, start=1):
        start = int(item["start_line"])
        end = int(item["end_line"])
        units.append(
            Unit(
                ordinal=ordinal,
                kind=str(item["kind"]),
                title=str(item["title"]),
                label=str(item["label"]),
                start_line=start,
                end_line=end,
                part=str(item["part"]),
                chapter=str(item["chapter"]),
                section=str(item["section"]),
                sha256=digest(lines, start, end),
            )
        )
    validate(lines, units, headings, environments, ignored)
    return units, opaque_spans, ignored


def validate(
    lines: list[str],
    units: list[Unit],
    headings: list[HeadingSpan],
    environments: list[EnvironmentSpan],
    ignored: list[IgnoredCommand],
) -> None:
    if "".join(lines).encode("utf-8").decode("utf-8") != "".join(lines):
        raise ValueError("source text is not a lossless UTF-8 round trip")
    expected_count = len(headings) + len(environments)
    if len(units) != expected_count:
        raise ValueError(
            f"unit count mismatch: {len(units)} rows for {expected_count} spans"
        )

    previous_key = (0, 0)
    seen: set[tuple[str, int, int]] = set()
    for expected_ordinal, unit in enumerate(units, start=1):
        if unit.ordinal != expected_ordinal:
            raise ValueError(f"nonconsecutive ordinal at row {expected_ordinal}")
        if not (1 <= unit.start_line <= unit.end_line <= len(lines)):
            raise ValueError(f"invalid line range for unit {unit.ordinal}: {unit}")
        key = (unit.start_line, unit.end_line)
        if key < previous_key:
            raise ValueError(f"source-order regression at unit {unit.ordinal}")
        previous_key = key
        identity = (unit.kind, unit.start_line, unit.end_line)
        if identity in seen:
            raise ValueError(f"duplicate inventory unit: {identity}")
        seen.add(identity)
        if unit.sha256 != digest(lines, unit.start_line, unit.end_line):
            raise ValueError(f"digest mismatch for unit {unit.ordinal}")

    active_counts: dict[str, int] = {}
    for span in environments:
        active_counts[span.kind] = active_counts.get(span.kind, 0) + 1
    row_counts: dict[str, int] = {}
    for unit in units:
        if unit.kind in ENVIRONMENT_KINDS:
            row_counts[unit.kind] = row_counts.get(unit.kind, 0) + 1
    if active_counts != row_counts:
        raise ValueError(
            f"active environment counts do not match inventory: "
            f"{active_counts!r} != {row_counts!r}"
        )

    # An ignored command-looking string is valid only as literal content of an
    # opaque environment; collect() establishes that containment.
    for command in ignored:
        if command.opaque_kind not in OPAQUE_ENVIRONMENT_KINDS:
            raise ValueError(f"unsafe ignored command: {command}")


def counts_by_kind(units: list[Unit]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for unit in units:
        counts[unit.kind] = counts.get(unit.kind, 0) + 1
    return counts


def write_csv(path: Path, units: list[Unit]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(Unit.__annotations__),
            lineterminator="\n",
        )
        writer.writeheader()
        for unit in units:
            writer.writerow(unit.__dict__)


def write_summary(
    path: Path,
    source: Path,
    source_bytes: bytes,
    lines: list[str],
    units: list[Unit],
    ignored: list[IgnoredCommand],
) -> None:
    counts = counts_by_kind(units)
    source_hash = hashlib.sha256(source_bytes).hexdigest()
    ignored_by_kind: dict[str, list[IgnoredCommand]] = {}
    for command in ignored:
        ignored_by_kind.setdefault(command.kind, []).append(command)

    body = [
        "# Frozen-source unit inventory",
        "",
        "This file is generated by `tools/source_unit_inventory.py`. It is an",
        "inventory and integrity record, not a summary or migration disposition.",
        "",
        f"- Source: `{source.as_posix()}`",
        f"- Bytes: {len(source_bytes)}",
        f"- Lines: {len(lines)}",
        f"- Whole-file SHA-256: `{source_hash}`",
        f"- Named structural/content units: {len(units)}",
        "- Generator self-checks: **PASS**",
        "",
        "## Counts",
        "",
        "| Kind | Count |",
        "|---|---:|",
    ]
    body.extend(f"| `{kind}` | {counts[kind]} |" for kind in sorted(counts))

    body.extend(
        [
            "",
            "## Opaque-listing exclusions",
            "",
            "TeX commands printed inside `lstlisting` are literal example data,",
            "not active environments. The listing row hash and whole-file hash",
            "still cover those bytes. The following are the only command-looking",
            "target begins excluded from active unit counts:",
            "",
            "| Kind | Lexical occurrences | Active units | Excluded literal lines |",
            "|---|---:|---:|---|",
        ]
    )
    lexical_kinds = sorted(set(counts) | set(ignored_by_kind))
    difference_rows = 0
    for kind in lexical_kinds:
        exclusions = ignored_by_kind.get(kind, [])
        if not exclusions:
            continue
        difference_rows += 1
        active = counts.get(kind, 0)
        literal_lines = ", ".join(
            f"{item.line} (`{item.opaque_kind}`)" for item in exclusions
        )
        body.append(
            f"| `{kind}` | {active + len(exclusions)} | {active} | {literal_lines} |"
        )
    if difference_rows == 0:
        body.append("| _none_ | 0 | 0 | -- |")

    body.extend(
        [
            "",
            "The apparent theorem count of 113 is therefore 112 active theorem",
            "environments plus the literal `\\begin{theorem}` printed at source",
            "line 14882. Likewise, the 126 lexical proof begins comprise 125",
            "active proof environments plus the literal begin at line 14889.",
            "",
            "## Coverage boundary",
            "",
            "Rows are emitted for part/chapter/section headings and the named",
            "block environments listed in the counts above. The byte-preserving",
            "whole-file digest covers all material that is not separately rowed,",
            "including the preamble, title page, connective prose, unnamed math",
            "displays, lists, bibliography entries, index commands, and wrappers.",
            "This mechanical boundary assigns no migration or content disposition.",
            "",
            "## Acceptance use",
            "",
            "Every row in the companion CSV must receive a book locator and a",
            "full-transcription verdict. The row hash makes literal source drift",
            "detectable; the whole-file hash covers all connective prose and",
            "unnamed displays as well as the named units.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(body))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--csv", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify that both generated files are current without rewriting them",
    )
    args = parser.parse_args()

    source_bytes = args.source.read_bytes()
    source_text = source_bytes.decode("utf-8")
    lines = source_text.splitlines(keepends=True)
    if "".join(lines).encode("utf-8") != source_bytes:
        raise ValueError("source bytes are not a lossless UTF-8 line split")

    units, _opaque_spans, ignored = collect(lines)
    if args.check:
        with tempfile.TemporaryDirectory(prefix="source-unit-inventory-") as temp:
            temp_root = Path(temp)
            csv_candidate = temp_root / "inventory.csv"
            summary_candidate = temp_root / "inventory.md"
            write_csv(csv_candidate, units)
            write_summary(
                summary_candidate,
                args.source,
                source_bytes,
                lines,
                units,
                ignored,
            )
            for tracked, candidate in (
                (args.csv, csv_candidate),
                (args.summary, summary_candidate),
            ):
                if not tracked.is_file() or tracked.read_bytes() != candidate.read_bytes():
                    raise SystemExit(f"stale generated artifact: {tracked}")
    else:
        write_csv(args.csv, units)
        write_summary(
            args.summary,
            args.source,
            source_bytes,
            lines,
            units,
            ignored,
        )
    print(f"source bytes: {len(source_bytes)}")
    print(f"source lines: {len(lines)}")
    print(f"source SHA-256: {hashlib.sha256(source_bytes).hexdigest()}")
    print(f"inventory units: {len(units)}")
    print(f"opaque command-looking exclusions: {len(ignored)}")
    print("self-checks: PASS")
    if args.check:
        print(f"verified current: {args.csv}")
        print(f"verified current: {args.summary}")
    else:
        print(f"wrote {args.csv}")
        print(f"wrote {args.summary}")


if __name__ == "__main__":
    main()

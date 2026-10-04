#!/usr/bin/env python3
"""Check that full-transcription ledgers cover every printed source line.

The checker reads the first cell of Markdown table rows whose locator has the
form ``N--M``. It does not decide whether an audit verdict is correct; it only
detects source text that has escaped the interval ledgers.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


RANGE_RE = re.compile(
    r"^\|\s*(?:`|\*\*)?(?P<start>\d+)\s*--\s*(?P<end>\d+)(?:`|\*\*)?\s*\|"
)


@dataclass(frozen=True)
class Interval:
    start: int
    end: int
    audit: Path
    audit_line: int


def printed_bounds(lines: list[str]) -> tuple[int, int]:
    begin = next(
        number
        for number, line in enumerate(lines, start=1)
        if line.strip() == r"\begin{document}"
    )
    end = next(
        number
        for number, line in enumerate(lines, start=1)
        if line.strip() == r"\end{document}"
    )
    return begin + 1, end - 1


def read_intervals(paths: list[Path]) -> list[Interval]:
    intervals: list[Interval] = []
    for path in paths:
        for number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            # Restoration ledgers have at least five columns. Ignore compact
            # summary/count tables whose broad ranges intentionally repeat the
            # detailed partitions.
            if line.count("|") < 6:
                continue
            match = RANGE_RE.match(line)
            if not match:
                continue
            start = int(match.group("start"))
            end = int(match.group("end"))
            if end < start:
                raise ValueError(f"{path}:{number}: reversed range {start}--{end}")
            intervals.append(Interval(start, end, path, number))
    return intervals


def collapse(numbers: list[int]) -> list[tuple[int, int]]:
    if not numbers:
        return []
    result: list[tuple[int, int]] = []
    start = previous = numbers[0]
    for number in numbers[1:]:
        if number == previous + 1:
            previous = number
            continue
        result.append((start, previous))
        start = previous = number
    result.append((start, previous))
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--audit", type=Path, action="append", required=True)
    args = parser.parse_args()

    source_lines = args.source.read_text(encoding="utf-8").splitlines()
    first, last = printed_bounds(source_lines)
    intervals = read_intervals(args.audit)

    wholly_outside = [item for item in intervals if item.end < first or item.start > last]
    invalid = [
        item for item in intervals if item.start < 1 or item.end > len(source_lines)
    ]
    if invalid:
        for item in invalid:
            print(
                f"range outside source file {item.start}--{item.end} "
                f"at {item.audit}:{item.audit_line}"
            )
        return 2

    coverage = [0] * (len(source_lines) + 1)
    for item in intervals:
        for number in range(max(item.start, first), min(item.end, last) + 1):
            coverage[number] += 1

    content_lines = [
        number
        for number in range(first, last + 1)
        if source_lines[number - 1].strip()
        and not source_lines[number - 1].lstrip().startswith("%")
    ]
    missing = [number for number in content_lines if coverage[number] == 0]
    overlaps = [number for number in content_lines if coverage[number] > 1]

    print(f"printed source bounds: {first}--{last}")
    print(f"nonblank noncomment printed lines: {len(content_lines)}")
    print(f"audit intervals: {len(intervals)}")
    print(f"preamble/postamble audit intervals ignored: {len(wholly_outside)}")
    print(f"uncovered content lines: {len(missing)}")
    for start, end in collapse(missing):
        print(f"  missing {start}--{end}")
    print(f"multiply covered content lines: {len(overlaps)}")
    for start, end in collapse(overlaps):
        print(f"  overlap {start}--{end}")

    return 1 if missing or overlaps else 0


if __name__ == "__main__":
    raise SystemExit(main())

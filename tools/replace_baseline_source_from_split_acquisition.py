#!/usr/bin/env python3
"""Replace SRC-025 from its frozen, physically split exact source ledger.

Necessity: SRC-025 preserves source topics on both sides of its locator
metadata, so the contiguous-ledger transformer cannot reproduce its order.
Definition: this transformer admits one SHA-256-pinned note whose two exact
ledger ranges contain source H3 headings and exact OPEN topic rows; it projects
only those H3 occurrences to baseline H4 and inserts the eight intervening
non-HTTPS source-presentation rows at their physical split point. Standing: it
is an administrative byte transformation, not a logical classification.
Nonredundancy: the general transformer assumes one contiguous ledger and does
not type SRC-025's provenance-bearing non-HTTPS presentation grammar. Use: a
write or check is admitted only after exact counts, schemes, punctuation,
administrative blocks, boundaries, note digest, and replacement-block fixed
point have all been proved mechanically. Baseline traversal is streaming, so
its memory use is bounded by the one source block rather than the corpus size.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
import tempfile
import time
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASELINE = ROOT / "spec/research/full-compendium-coverage-baseline.md"

SOURCE_RE = re.compile(r"^### (?P<source_id>SRC-\d{3}) — .+$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
HIERARCHY_RE = re.compile(r"^### (?P<title>.+)$")
BASELINE_HIERARCHY_RE = re.compile(r"^#{4,6} .+$")
NUMBERED_HTTPS_RE = re.compile(
    r"^(?P<number>[1-9]\d*)\. (?P<value>https://\S+)$"
)
NON_HTTPS_PRESENTATION_RE = re.compile(
    r"^- `(?P<value>[^`\n]+)` — (?P<provenance>\S.*)\.$"
)
NON_HTTPS_URI_RE = re.compile(
    r"^(?:http://|ftp://|urn:|mailto:|doi:|ark:/)", re.IGNORECASE
)
TOPIC_OPEN_SUFFIX = "**OPEN**."
OLD_OPEN_SUFFIXES = ("**OPEN**", "**OPEN**.")
DERIVED_LOCATOR_RE = re.compile(
    r"^- Exact (?P<kind>HTTPS locator|non-HTTPS locator|scheme-less identifier) "
    r"(?P<number>[1-9]\d*): (?P<value>\S.*)$"
)

FROZEN_SOURCE_ID = "SRC-025"
FROZEN_SOURCE_HEADING = "### SRC-025 — Handbook of Modal Logic"
FROZEN_NOTE_SHA256 = (
    "618cc1a68ed00929fbd50a4a086748a2eb70c45b15e03f3035e255b64af216f1"
)
FROZEN_COUNTS = {
    "https": 282,
    "non_https": 8,
    "scheme_less": 0,
    "hierarchy": 39,
    "h4": 39,
    "h5": 0,
    "h6": 0,
    "topics": 1257,
}
FROZEN_IDENTITY_METADATA = (
    "- Exact work title: *Handbook of Modal Logic*",
    "- Editors: Patrick Blackburn; Johan van Benthem; Frank Wolter",
    "- Publisher metadata: 1st Edition; Volume 3; November 3, 2006",
    "- Official publisher source: https://shop.elsevier.com/books/handbook-of-modal-logic/blackburn/978-0-444-51690-9",
)

HTTPS_HEADING = "## Ordered exact HTTPS locator ledger"
NON_HTTPS_HEADING = (
    "## Non-HTTPS locators exposed by acquired source presentations"
)
NON_HTTPS_END_HEADING = "## Count premises for integration"
FIRST_LEDGER_HEADING = "## Patch-ready hierarchy-and-topic ledger"
SECOND_LEDGER_HEADING = "## Patch-ready hierarchy-and-topic ledger continued"
LEDGER_END_HEADING = "## Exact integration counts and deltas"

# Each block is exact acquisition-note administration. Enumerating its physical
# lines makes a rewrap, omission, duplication, or edited claim fail closed.
HTTPS_PREAMBLE = (
    "The current baseline locator is item 1. Items 2–282 are additions. Every item is an exact locator; no locator template is counted.",
)
FIRST_LEDGER_PREAMBLE = (
    "Every bullet below is one source-displayed unit, artifact, internal hierarchy",
    "entry, variant, conflict, access gap, or OPEN obligation. No aggregate line",
    "stands in for the editor PDFs' 584 source-contents hierarchy entries. The 19",
    "regex false positives remain separately typed extraction evidence and are not",
    "source hierarchy.",
)
FIRST_LEDGER_INTERLUDE = (
    "All 82 ILLC Chapter 1 pages, 65 Manchester Chapter 4 pages, 81 Darmstadt",
    "Chapter 5 pages, 86 STOQ Chapter 6 pages, 38 author-hosted Chapter 10 pages,",
    "63 ICCL Chapter 13 converted pages, 45 author-hosted Chapter 14 pages, 21 Rice",
    "Chapter 17 converted pages, and 49 Indiana Chapter 19 pages were rendered and",
    "visually inspected. The ICCL and Rice PDF files are local inspection",
    "derivatives of the acquired `.ps.gz` sources, not independent source",
    "presentations. The STOQ Chapter 6 PDF visibly contains colored link or markup",
    "annotations. No derivative or visual inspection changes any **OPEN** standing.",
)
NON_HTTPS_POSTAMBLE = (
    "`mailto:` locators are not HTTP locators and are not included in either URL",
    "count. The editor project nevertheless displays the exact mailto forms",
    "`mailto:%20patrick.blackburn@loria.fr`,",
    "`mailto:%20%20johan@science.uva.nl`, and",
    "`mailto:%20frank@csc.liv.ac.uk`.",
)
SECOND_LEDGER_PREAMBLE = (
    "The eight non-HTTPS source-presentation rows above remain topics in this",
    "continued ledger; only their locator values are also copied to the baseline's",
    "separate non-HTTPS metadata fields.",
)
SECOND_LEDGER_INTERLUDE = (
    "The first acquisition pass counted every line matching repeated spaced full",
    "stops across every extracted PDF page and reported 603. Source-position audit",
    "shows that 584 are contents-block hierarchy lines. The following nineteen",
    "matches occur after the contents blocks in chapter prose or formulas and are",
    "therefore retained as extraction-evidence rows, not hierarchy entries:",
)
GLOBAL_OPEN_STANDING = "All content and reproduction standings remain **OPEN**."
COUNT_PREMISES_BODY = (
    "",
    "The current baseline has 4 part hierarchy headings, 21 chapter topics, and 1",
    "HTTPS locator. The following source counts are mechanical premises for the",
    "parent integration pass; none is a substitute for a literal row above or",
    "below:",
    "",
    "| Mechanical premise | Exact count |",
    "|---|---:|",
    "| Publisher/printed source hierarchy | 11 outer/part headings plus 21 chapter headings |",
    "| Editor-PDF internal hierarchy | 584 entries; per-chapter counts `39, 39, 22, 29, 45, 33, 25, 35, 37, 20, 39, 35, 22, 18, 11, 33, 16, 15, 19, 36, 16` |",
    "| Separately typed extraction false positives | 19 body/prose/formula lines; none is hierarchy |",
    "| Independently hosted complete-presentation hierarchies | 233 entries; per-presentation counts `39, 29, 45, 19, 21, 22, 21, 16, 21` |",
    "| HTTPS locators | 282 total; delta `+281` |",
    "| Non-HTTPS locators | 8; excluded from the HTTPS count |",
    "",
    "The exact patch-ready Markdown-heading and topic totals are recorded after the",
    "literal ledger. Distinct source hierarchy entries remain unmerged; these",
    "mechanical premises do not convert them into a synthetic hierarchy.",
    "",
    GLOBAL_OPEN_STANDING,
    "",
)


def file_sha256(path: Path) -> str:
    """Return the SHA-256 of one file using bounded reads."""

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def frozen_note_lines(
    path: Path, expected_sha256: str
) -> tuple[list[str], str]:
    """Read one immutable note payload and enforce its caller-supplied digest."""

    if SHA256_RE.fullmatch(expected_sha256) is None:
        raise ValueError("--expected-note-sha256 must be 64 lowercase hex digits")
    raw = path.read_bytes()
    observed = hashlib.sha256(raw).hexdigest()
    if observed != expected_sha256:
        raise ValueError(
            f"{path}: SHA-256 mismatch: observed {observed}, expected {expected_sha256}"
        )
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ValueError(f"{path}: UTF-8 BOM is not allowed")
    text = raw.decode("utf-8")
    if "\r" in text:
        raise ValueError(f"{path}: CR characters are not allowed")
    return text.splitlines(), observed


def unique_heading_index(lines: list[str], heading: str, path: Path) -> int:
    """Return the sole physical occurrence of an exact section heading."""

    matches = [index for index, line in enumerate(lines) if line == heading]
    if len(matches) != 1:
        raise ValueError(
            f"{path}: expected one {heading!r} heading, found {len(matches)}"
        )
    return matches[0]


def bounded(
    lines: list[str], start: str, end: str, path: Path
) -> list[tuple[int, str]]:
    """Return exact line-numbered content between two unique headings."""

    first = unique_heading_index(lines, start, path)
    last = unique_heading_index(lines, end, path)
    if last <= first:
        raise ValueError(f"{path}: reversed section bounds {start!r}, {end!r}")
    return [(index + 1, lines[index]) for index in range(first + 1, last)]


def without_exact_preamble(
    section: list[tuple[int, str]], preamble: tuple[str, ...], path: Path
) -> list[tuple[int, str]]:
    """Remove one exact leading administrative block and no source row."""

    cursor = 0
    while cursor < len(section) and not section[cursor][1]:
        cursor += 1
    for expected in preamble:
        if cursor >= len(section) or section[cursor][1] != expected:
            line_number = section[cursor][0] if cursor < len(section) else "EOF"
            actual = section[cursor][1] if cursor < len(section) else None
            raise ValueError(
                f"{path}:{line_number}: exact preamble expected {expected!r}, got {actual!r}"
            )
        cursor += 1
    if cursor < len(section) and section[cursor][1] in preamble:
        raise ValueError(f"{path}:{section[cursor][0]}: duplicated exact preamble")
    return section[cursor:]


def without_one_exact_block(
    section: list[tuple[int, str]],
    block: tuple[str, ...],
    path: Path,
    label: str,
) -> list[tuple[int, str]]:
    """Remove exactly one enumerated internal administrative block."""

    starts = [
        index
        for index in range(0, len(section) - len(block) + 1)
        if tuple(line for _, line in section[index : index + len(block)]) == block
    ]
    if len(starts) != 1:
        raise ValueError(
            f"{path}: untyped ledger line: expected one exact {label}, found {len(starts)}"
        )
    first = starts[0]
    return section[:first] + section[first + len(block) :]


def numbered_https_rows(lines: list[str], path: Path) -> list[tuple[int, str]]:
    """Parse every numbered HTTPS locator without normalizing its value."""

    section = without_exact_preamble(
        bounded(lines, HTTPS_HEADING, NON_HTTPS_HEADING, path),
        HTTPS_PREAMBLE,
        path,
    )
    rows: list[tuple[int, str]] = []
    expected = 1
    for line_number, line in section:
        if not line:
            continue
        match = NUMBERED_HTTPS_RE.fullmatch(line)
        if match is None:
            raise ValueError(f"{path}:{line_number}: malformed HTTPS row {line!r}")
        number = int(match.group("number"))
        if number != expected:
            raise ValueError(
                f"{path}:{line_number}: HTTPS locator sequence expected {expected}, got {number}"
            )
        rows.append((number, match.group("value")))
        expected += 1
    return rows


def non_https_rows(
    lines: list[str], path: Path
) -> tuple[list[tuple[int, str]], list[str]]:
    """Parse each typed locator and preserve its full source-presentation row."""

    section = without_one_exact_block(
        bounded(lines, NON_HTTPS_HEADING, NON_HTTPS_END_HEADING, path),
        NON_HTTPS_POSTAMBLE,
        path,
        "non-HTTPS postamble",
    )
    rows: list[tuple[int, str]] = []
    topics: list[str] = []
    for line_number, line in section:
        if not line:
            continue
        match = NON_HTTPS_PRESENTATION_RE.fullmatch(line)
        if match is None:
            raise ValueError(
                f"{path}:{line_number}: malformed non-HTTPS source-presentation row {line!r}"
            )
        value = match.group("value")
        if NON_HTTPS_URI_RE.match(value) is None or value.lower().startswith("https:"):
            raise ValueError(
                f"{path}:{line_number}: non-HTTPS row lacks a non-HTTPS URI scheme"
            )
        rows.append((len(rows) + 1, value))
        topics.append(line)
    return rows, topics


def projected_ledger(
    lines: list[str],
    start: str,
    end: str,
    preamble: tuple[str, ...],
    interlude: tuple[str, ...],
    path: Path,
) -> tuple[list[str], int, int]:
    """Project only exact source H3 rows and copy exact OPEN topics in order."""

    section = without_exact_preamble(bounded(lines, start, end, path), preamble, path)
    section = without_one_exact_block(
        section, interlude, path, f"{start} administrative interlude"
    )
    output: list[str] = []
    headings = 0
    topics = 0
    for line_number, line in section:
        if not line:
            output.append(line)
            continue
        if HIERARCHY_RE.fullmatch(line) is not None:
            output.append(f"#{line}")
            headings += 1
            continue
        if line.startswith("- "):
            if not line.endswith(TOPIC_OPEN_SUFFIX):
                raise ValueError(
                    f"{path}:{line_number}: topic lacks exact {TOPIC_OPEN_SUFFIX!r} suffix"
                )
            output.append(line)
            topics += 1
            continue
        raise ValueError(f"{path}:{line_number}: untyped ledger line {line!r}")
    return output, headings, topics


def exact_note_payload(
    note: list[str], args: argparse.Namespace
) -> tuple[
    list[tuple[int, str]],
    list[tuple[int, str]],
    list[tuple[int, str]],
    list[str],
    int,
    int,
]:
    """Assemble the split ledger only after every aggregate and level pin agrees."""

    if args.expected_scheme_less != 0:
        raise ValueError("SRC-025 requires --expected-scheme-less 0")
    if args.scheme_less_heading or args.scheme_less_end_heading:
        raise ValueError("SRC-025 has no scheme-less locator section")
    if args.expected_hierarchy != (
        args.expected_h4 + args.expected_h5 + args.expected_h6
    ):
        raise ValueError(
            "expected hierarchy aggregate does not equal its level pins"
        )

    count_premises = tuple(
        line
        for _, line in bounded(
            note, NON_HTTPS_END_HEADING, SECOND_LEDGER_HEADING, args.note
        )
    )
    if count_premises != COUNT_PREMISES_BODY:
        raise ValueError(
            f"{args.note}: exact count-premises and global-OPEN bridge changed"
        )

    https = numbered_https_rows(note, args.note)
    non_https, non_https_topics = non_https_rows(note, args.note)
    scheme_less: list[tuple[int, str]] = []
    first, first_headings, first_topics = projected_ledger(
        note,
        FIRST_LEDGER_HEADING,
        HTTPS_HEADING,
        FIRST_LEDGER_PREAMBLE,
        FIRST_LEDGER_INTERLUDE,
        args.note,
    )
    second, second_headings, second_topics = projected_ledger(
        note,
        SECOND_LEDGER_HEADING,
        LEDGER_END_HEADING,
        SECOND_LEDGER_PREAMBLE,
        SECOND_LEDGER_INTERLUDE,
        args.note,
    )

    ledger = [*first, *non_https_topics, "", *second]
    headings = first_headings + second_headings
    topics = first_topics + len(non_https_topics) + second_topics
    observed = {
        "https": len(https),
        "non_https": len(non_https),
        "scheme_less": 0,
        "hierarchy": headings,
        "h4": headings,
        "h5": 0,
        "h6": 0,
        "topics": topics,
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
    return https, non_https, scheme_less, ledger, headings, topics


def retained_metadata(block: list[str], path: Path, source_id: str) -> list[str]:
    """Retain typed metadata and reject any silently discardable stale-block row."""

    retrieval_indices = [
        index
        for index, line in enumerate(block)
        if line.startswith("- Retrieved granularity:")
    ]
    if len(retrieval_indices) != 1:
        raise ValueError(
            f"{path}: {source_id} must have exactly one retrieved-granularity field; "
            f"found {len(retrieval_indices)}"
        )
    retrieval_index = retrieval_indices[0]
    retained: list[str] = []
    locator_sequences: dict[str, int] = {
        "HTTPS locator": 0,
        "non-HTTPS locator": 0,
        "scheme-less identifier": 0,
    }
    for index, line in enumerate(block[1:retrieval_index], start=2):
        if not line:
            continue
        if not line.startswith("- "):
            raise ValueError(
                f"{path}: {source_id} metadata line {index} is untyped: {line!r}"
            )
        locator = DERIVED_LOCATOR_RE.fullmatch(line)
        if locator is None:
            if line.startswith(
                (
                    "- Exact HTTPS locator ",
                    "- Exact non-HTTPS locator ",
                    "- Exact scheme-less identifier ",
                    "- Exact scheme-less identifier:",
                )
            ):
                raise ValueError(
                    f"{path}: {source_id} malformed derived locator at block line {index}"
                )
            retained.append(line)
            continue
        kind = locator.group("kind")
        expected = locator_sequences[kind] + 1
        observed = int(locator.group("number"))
        if observed != expected:
            raise ValueError(
                f"{path}: {source_id} {kind} sequence expected {expected}, got {observed}"
            )
        locator_sequences[kind] = observed

    for index, line in enumerate(block[retrieval_index + 1 :], start=retrieval_index + 2):
        if not line or BASELINE_HIERARCHY_RE.fullmatch(line) is not None:
            continue
        if line.startswith("- ") and (
            line.endswith(OLD_OPEN_SUFFIXES)
            or NON_HTTPS_PRESENTATION_RE.fullmatch(line) is not None
        ):
            continue
        raise ValueError(
            f"{path}: {source_id} replaceable ledger line {index} is untyped: {line!r}"
        )
    if not retained:
        raise ValueError(f"{path}: {source_id} has no retained source metadata")
    return retained


def validate_frozen_contract(args: argparse.Namespace) -> None:
    """Refuse caller-controlled substitutions for the one named source contract."""

    if args.source_id != FROZEN_SOURCE_ID:
        raise ValueError(
            f"this adapter is pinned to {FROZEN_SOURCE_ID}, got {args.source_id}"
        )
    if args.expected_note_sha256 != FROZEN_NOTE_SHA256:
        raise ValueError(
            f"{FROZEN_SOURCE_ID} requires frozen note SHA-256 {FROZEN_NOTE_SHA256}"
        )
    observed = {
        "https": args.expected_https,
        "non_https": args.expected_non_https,
        "scheme_less": args.expected_scheme_less,
        "hierarchy": args.expected_hierarchy,
        "h4": args.expected_h4,
        "h5": args.expected_h5,
        "h6": args.expected_h6,
        "topics": args.expected_topics,
    }
    if observed != FROZEN_COUNTS:
        raise ValueError(
            f"{FROZEN_SOURCE_ID} frozen count pins are {FROZEN_COUNTS}, got {observed}"
        )


def replacement_block(
    old: list[str], note: list[str], args: argparse.Namespace
) -> list[str]:
    """Build one complete canonical source block from the validated payload."""

    if not old or old[0] != FROZEN_SOURCE_HEADING:
        actual = old[0] if old else None
        raise ValueError(
            f"{args.baseline}: frozen source heading changed: {actual!r}"
        )
    metadata = retained_metadata(old, args.baseline, args.source_id)
    missing_identity = [
        line for line in FROZEN_IDENTITY_METADATA if metadata.count(line) != 1
    ]
    if missing_identity:
        raise ValueError(
            f"{args.baseline}: {args.source_id} identity metadata changed or duplicated: "
            f"{missing_identity}"
        )
    https, non_https, scheme_less, ledger, headings, topics = exact_note_payload(
        note, args
    )
    output = [old[0], "", *metadata]
    for number, value in https:
        output.append(f"- Exact HTTPS locator {number}: {value}")
    for number, value in non_https:
        output.append(f"- Exact non-HTTPS locator {number}: {value}")
    for number, value in scheme_less:
        output.append(f"- Exact scheme-less identifier {number}: {value}")
    output.append(
        "- Retrieved granularity: exact split acquisition-note ledger containing "
        f"{len(https)} HTTPS locators, {len(non_https)} non-HTTPS locators, "
        f"{len(scheme_less)} scheme-less identifiers, {headings} displayed "
        f"hierarchy headings, and {topics} separate OPEN topics; no source "
        "presentation is merged or closed"
    )
    output.extend(("", *ledger, ""))
    validate_old_derived_conservation(old, output, args)
    return output


def validate_old_derived_conservation(
    old: list[str], replacement: list[str], args: argparse.Namespace
) -> None:
    """Prove every old typed derived occurrence survives in the frozen payload.

    The source note, rather than stale baseline placement, fixes output order.
    Therefore conservation is multiplicity-preserving rather than an old-order
    subsequence test: the prior adapter placed the eight intervening rows at the
    end, while the frozen split presentation requires them between ledger parts.
    """

    old_retrieval = next(
        index
        for index, line in enumerate(old)
        if line.startswith("- Retrieved granularity:")
    )
    new_retrieval = next(
        index
        for index, line in enumerate(replacement)
        if line.startswith("- Retrieved granularity:")
    )
    old_locators = Counter(
        line for line in old[1:old_retrieval] if DERIVED_LOCATOR_RE.fullmatch(line)
    )
    new_locators = Counter(
        line
        for line in replacement[1:new_retrieval]
        if DERIVED_LOCATOR_RE.fullmatch(line)
    )
    old_records = Counter(
        line
        for line in old[old_retrieval + 1 :]
        if BASELINE_HIERARCHY_RE.fullmatch(line) is not None
        or line.startswith("- ")
    )
    new_records = Counter(
        line
        for line in replacement[new_retrieval + 1 :]
        if BASELINE_HIERARCHY_RE.fullmatch(line) is not None
        or line.startswith("- ")
    )
    missing_locators = old_locators - new_locators
    missing_records = old_records - new_records
    if missing_locators or missing_records:
        def display(counter: Counter[str]) -> list[tuple[str, int]]:
            return sorted(counter.items())[:5]

        raise ValueError(
            f"{args.baseline}: {args.source_id} replacement would discard typed "
            f"occurrences; locators={display(missing_locators)}, "
            f"ledger={display(missing_records)}"
        )


def decoded_line(raw: bytes, path: Path, line_number: int) -> str:
    """Decode one baseline line while enforcing the repository's LF/UTF-8 form."""

    if line_number == 1 and raw.startswith(b"\xef\xbb\xbf"):
        raise ValueError(f"{path}: UTF-8 BOM is not allowed")
    if b"\r" in raw:
        raise ValueError(f"{path}:{line_number}: CR characters are not allowed")
    return raw.rstrip(b"\n").decode("utf-8")


def source_block_and_digest(
    baseline: Path, source_id: str
) -> tuple[list[str], str]:
    """Stream the corpus, retaining exactly one complete target source block."""

    digest = hashlib.sha256()
    block: list[str] = []
    capturing = False
    complete = False
    found = 0
    with baseline.open("rb") as handle:
        for line_number, raw in enumerate(handle, start=1):
            digest.update(raw)
            line = decoded_line(raw, baseline, line_number)
            match = SOURCE_RE.fullmatch(line)
            boundary = match is not None or line == "---"
            if capturing and boundary:
                capturing = False
                complete = True
            if match is not None and match.group("source_id") == source_id:
                found += 1
                if found != 1:
                    raise ValueError(
                        f"{baseline}: expected one {source_id} source block, found at least {found}"
                    )
                capturing = True
                complete = False
                block = [line]
                continue
            if capturing:
                block.append(line)
    if found != 1:
        raise ValueError(
            f"{baseline}: expected one {source_id} source block, found {found}"
        )
    if not complete:
        raise ValueError(f"{baseline}: {source_id} has no closing boundary")
    return block, digest.hexdigest()


def stream_candidate(
    baseline: Path,
    candidate: Path,
    source_id: str,
    replacement: list[str],
    expected_baseline_digest: str,
) -> None:
    """Copy the corpus byte-for-byte while replacing exactly one source block."""

    digest = hashlib.sha256()
    state = "before"
    found = 0
    with baseline.open("rb") as source, candidate.open("wb") as output:
        for line_number, raw in enumerate(source, start=1):
            digest.update(raw)
            line = decoded_line(raw, baseline, line_number)
            match = SOURCE_RE.fullmatch(line)
            if match is not None and match.group("source_id") == source_id:
                found += 1
                if found != 1 or state != "before":
                    raise ValueError(
                        f"{baseline}: duplicate or misplaced {source_id} source block"
                    )
                output.write(("\n".join(replacement) + "\n").encode("utf-8"))
                state = "skip"
                continue
            if state == "skip":
                if match is not None or line == "---":
                    output.write(raw)
                    state = "after"
                continue
            output.write(raw)
    if found != 1 or state == "skip":
        raise ValueError(f"{baseline}: expected one complete {source_id} block")
    if digest.hexdigest() != expected_baseline_digest:
        raise ValueError(f"{baseline}: baseline changed during replacement")


def atomic_replace_after_digest_check(
    candidate: Path, baseline: Path, expected_baseline_digest: str
) -> None:
    """Install atomically, retrying only while the old corpus digest is unchanged."""

    for attempt in range(10):
        if file_sha256(baseline) != expected_baseline_digest:
            raise ValueError(f"{baseline}: baseline changed before atomic replacement")
        try:
            os.replace(candidate, baseline)
            return
        except PermissionError:
            if attempt == 9:
                raise
            time.sleep(0.2 * (attempt + 1))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE)
    parser.add_argument("--note", type=Path, required=True)
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--expected-note-sha256", required=True)
    parser.add_argument("--expected-https", type=int, required=True)
    parser.add_argument("--expected-non-https", type=int, required=True)
    parser.add_argument("--expected-scheme-less", type=int, required=True)
    parser.add_argument("--expected-hierarchy", type=int, required=True)
    parser.add_argument("--expected-h4", type=int, required=True)
    parser.add_argument("--expected-h5", type=int, required=True)
    parser.add_argument("--expected-h6", type=int, required=True)
    parser.add_argument("--expected-topics", type=int, required=True)
    parser.add_argument("--scheme-less-heading")
    parser.add_argument("--scheme-less-end-heading")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    args.baseline = args.baseline.resolve()
    args.note = args.note.resolve()
    validate_frozen_contract(args)

    note, note_digest = frozen_note_lines(args.note, args.expected_note_sha256)
    old_block, baseline_digest = source_block_and_digest(
        args.baseline, args.source_id
    )
    replacement = replacement_block(old_block, note, args)
    if replacement_block(replacement, note, args) != replacement:
        raise ValueError(f"{args.source_id}: replacement block is not a fixed point")

    if args.check:
        if old_block != replacement:
            print(f"{args.source_id}: baseline source block is stale", file=sys.stderr)
            return 1
        if file_sha256(args.note) != note_digest:
            raise ValueError(f"{args.note}: note changed after digest validation")
        if file_sha256(args.baseline) != baseline_digest:
            raise ValueError(f"{args.baseline}: baseline changed during exact check")
        print(f"{args.source_id}: split acquisition-note block matches exactly")
        return 0

    fd, name = tempfile.mkstemp(
        prefix=args.baseline.name + ".", suffix=".tmp", dir=args.baseline.parent
    )
    os.close(fd)
    candidate = Path(name)
    try:
        stream_candidate(
            args.baseline,
            candidate,
            args.source_id,
            replacement,
            baseline_digest,
        )
        if file_sha256(args.note) != note_digest:
            raise ValueError(f"{args.note}: note changed after digest validation")
        atomic_replace_after_digest_check(candidate, args.baseline, baseline_digest)
        print(f"{args.source_id}: split acquisition-note block replaced exactly")
        return 0
    finally:
        candidate.unlink(missing_ok=True)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, UnicodeError, ValueError) as error:
        print(f"split baseline replacement failed: {error}", file=sys.stderr)
        raise SystemExit(1)

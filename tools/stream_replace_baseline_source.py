#!/usr/bin/env python3
"""Bounded-memory replacement/check for one baseline source from a literal note.

Necessity: some exact acquisition ledgers are hundreds of megabytes, so the
existing list-based administrative transformer can require multiple gigabytes.
Definition: this utility streams one explicitly bounded locator/ledger shape,
streams the baseline around exactly one matching source block, and either
atomically installs or byte-compares the result. Standing: it is an
administrative byte transformation, not a logical/content classification.
Nonredundancy: the existing transformer materializes both input documents and
the output simultaneously. Use: only notes with three explicitly bounded
locator sections and one contiguous hierarchy/topic ledger are accepted; every
count, scheme, OPEN suffix, and source boundary is checked before installation.
One exact administrative ledger preamble and explicitly typed post-ledger
count/gate statements are outside the source-record projection; every other
nonblank line in those positions is rejected rather than silently omitted.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
import tempfile
import time
from pathlib import Path
from typing import Iterable, TextIO


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASELINE = ROOT / "spec/research/full-compendium-coverage-baseline.md"
SOURCE_RE = re.compile(r"^### (?P<id>SRC-\d{3}) — .+$")
LOCATOR_RE = re.compile(r"^(?P<number>\d+)\. `(?P<value>[^`]+)`$")
PROVENANCE_LOCATOR_RE = re.compile(
    r"^(?P<number>\d+)\. `(?P<value>[^`]+)` (?P<provenance>.+)$"
)
OPEN_LOCATOR_RE = re.compile(
    r"^- (?:\[TOPIC-\d+\] )?"
    r"\[(?P<kind>HTTPS|NONHTTPS|SCHEMELESS)-(?P<number>\d+)\] "
    r"(?P<value>.+) (?:\u2014|â€”) \*\*OPEN\*\*$"
)
OPEN_SUFFIXES = ("\u2014 **OPEN**", "â€” **OPEN**")
URI_SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
QUALIFIED_OPEN_TOPIC_RE = re.compile(r"^- .+\*\*OPEN\*\*; [^;]+$")
# These are the URI schemes admitted by the manifest's non-HTTPS locator field.
# A colon alone is insufficient: literal source identifiers such as
# ``sha256:...``, ``arXiv:...``, host-and-port forms, and archival compound IDs
# remain scheme-less unless the note explicitly types them as URI locators.
ADMITTED_NON_HTTPS_SCHEME_RE = re.compile(
    r"^(?:https?|ftp|git|ssh|urn|mailto|doi|ark):", re.IGNORECASE
)
HEADING_RE = re.compile(r"^(?P<marks>#{4,6}) .+$")
LEDGER_PREAMBLE_RE = re.compile(
    r"^Every (?:(?:bullet(?: below| in this ledger)? is one|generated topic below is a) "
    r"(?:independently |separately |separate )?OPEN record|row below is separately OPEN)"
    r"(?:[.;].*)?$|^Every topic row below is separately OPEN\. "
    r"No topic selects, merges, normalizes, corrects, reconciles, compresses, "
    r"or substitutes for another presentation\.$"
)
LEDGER_PREAMBLE_BLOCKS = {
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
        "Every bullet is one separate OPEN record. No row stands for, corrects, compresses,",
        "merges, summarizes, normalizes, or replaces another row.",
    ),
    (
        "Every bullet is a separate OPEN record. No row stands for the content of",
        "another row, and no difference is resolved by preference.",
    ),
}


def admitted_ledger_preamble_block(lines: list[str]) -> bool:
    """Accept one complete, exact administrative preamble block."""

    block = tuple(lines)
    return block in LEDGER_PREAMBLE_BLOCKS or (
        len(block) == 1 and LEDGER_PREAMBLE_RE.fullmatch(block[0]) is not None
    )


def exact_configured_block(lines: list[str], configured: list[str]) -> bool:
    """Return whether physical lines equal one explicitly configured block."""

    return bool(configured) and lines == configured
FINAL_OPEN_ADMIN_RE = re.compile(
    r"^(?:SRC-\d{3}|No |All |Every ).*(?:gate|gates|record|presentation|body|"
    r"source|content|acquisition|rights|static|build|visual|human|reproduction)"
    r".*\*\*OPEN\*\*\.$",
    re.IGNORECASE,
)
POST_LEDGER_ADMIN_BULLET_RE = re.compile(
    r"^- (?:Acquired|Acquisition|All|Build|Cornell|Czech|Direct|Distinct|Exact|"
    r"Cambridge Contents rows|Crossref ISBN-query items|Displayed|Duplicate|"
    r"Full|Hierarchy|Human-content|Independent|Indexed|Institutional|Literal|"
    r"Live|Locally|Markdown|Nonzero|OCR|Official|Opened|Page-specific|Patch-ready|"
    r"PDF|Printed-Contents|Public-PDF|Public-renderer|Public-web|Rendered|"
    r"Mechanically extracted PDF tables|Mechanically extracted PDF table cells|"
    r"Mechanically extracted PDF table rows|Patch-ledger top-level file manifestations|"
    r"Prior SRC-\d{3} baseline|Raster|Replacement delta|Reproduction|Request|"
    r"Retained|Rights|Scratch|Separate|Separately|Source|Static|These|Unique|"
    r"The complete|Visual|Visually|ZIP(?:/DOCX)?|Zero-byte)\b.*[.:]$"
)

HTTPS_START = "## Patch-ready exact HTTPS locator ledger"
NON_HTTPS_START = "## Exact non-HTTPS locator ledger"
SCHEMELESS_START = "## Exact scheme-less identifier ledger"
LEDGER_START = "## Patch-ready hierarchy-and-topic ledger"
LEDGER_END = "## Exact integration counts and deltas"


def parse_locator_row(
    line: str, section: str, allow_provenance: bool = False
) -> tuple[int, str] | None:
    """Return the exact row number/value for either admitted literal grammar.

    Necessity: acquisition notes already contain two exact row surfaces, and
    rewriting one surface merely to run this administrative transformer would
    alter the retained note. Definition: an admitted row is either
    ``N. `value``` or ``- [KIND-N] value â€” **OPEN**``, where KIND is fixed by
    the active HTTPS, non-HTTPS, or scheme-less subsection. Standing: these are
    metalinguistic serialization grammars only. Nonredundancy: the second form
    carries the note's explicit OPEN status and typed identifier, which the
    first form does not. Use: scanning and value emission below both call this
    function, so neither grammar is normalized into the other inside the note.
    """

    match = LOCATOR_RE.fullmatch(line)
    if match is not None:
        return int(match.group("number")), match.group("value")
    if allow_provenance:
        match = PROVENANCE_LOCATOR_RE.fullmatch(line)
        if match is not None:
            return int(match.group("number")), match.group("value")
    match = OPEN_LOCATOR_RE.fullmatch(line)
    if match is None:
        return None
    expected_kind = {
        "https": "HTTPS",
        "non_https": "NONHTTPS",
        "bare": "SCHEMELESS",
    }[section]
    if match.group("kind") != expected_kind:
        return None
    return int(match.group("number")), match.group("value")


def source_metadata(baseline: Path, source_id: str) -> tuple[str, list[str]]:
    heading = ""
    metadata: list[str] = []
    state = "before"
    with baseline.open("r", encoding="utf-8", newline="") as handle:
        for raw in handle:
            line = raw.rstrip("\n")
            if line.endswith("\r"):
                raise ValueError(f"{baseline}: CR is not allowed")
            match = SOURCE_RE.fullmatch(line)
            if state == "before":
                if match and match.group("id") == source_id:
                    heading = line
                    state = "metadata"
                continue
            if state == "metadata":
                if line.startswith("- Retrieved granularity:"):
                    return heading, [
                        item
                        for item in metadata
                        if not item.startswith(
                            (
                                "- Exact HTTPS locator ",
                                "- Exact non-HTTPS locator ",
                                "- Exact scheme-less identifier ",
                                "- Exact scheme-less identifier:",
                            )
                        )
                    ]
                if line.startswith("- "):
                    metadata.append(line)
                if match or line == "---":
                    break
    raise ValueError(f"{baseline}: {source_id} metadata boundary not found")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def stable_note_snapshot(note: Path) -> tuple[Path, str]:
    """Copy one immutable parse/emission snapshot and prove source stability.

    Necessity: count validation and bounded-memory emission require multiple
    passes, while a note could otherwise change between those passes.
    Definition: the snapshot is a byte-for-byte temporary copy whose SHA-256
    equals the source note both during the copy and in an immediate independent
    reread. Standing: this is an administrative integrity check, not source
    verification. Nonredundancy: a size or timestamp alone cannot establish
    byte identity. Use: every scan and emitted value below is read only from
    this one snapshot, and installation is refused if the live note later
    differs from its digest.
    """

    before = note.stat()
    fd, name = tempfile.mkstemp(
        prefix=note.name + ".", suffix=".snapshot", dir=note.parent
    )
    os.close(fd)
    snapshot = Path(name)
    digest = hashlib.sha256()
    try:
        with note.open("rb") as source, snapshot.open("wb") as target:
            while chunk := source.read(1024 * 1024):
                digest.update(chunk)
                target.write(chunk)
        copied_digest = digest.hexdigest()
        after = note.stat()
        if (
            before.st_size != after.st_size
            or before.st_mtime_ns != after.st_mtime_ns
            or copied_digest != file_sha256(note)
        ):
            raise ValueError(f"{note}: note changed while its snapshot was created")
        return snapshot, copied_digest
    except BaseException:
        snapshot.unlink(missing_ok=True)
        raise


def scan_note(note: Path, args: argparse.Namespace) -> dict[str, int]:
    if bool(args.quarantine_https_heading) != bool(args.expected_quarantine_https):
        raise ValueError(
            "a quarantined HTTPS ledger heading and positive expected count are required together"
        )
    if args.combined_non_https_bare and (
        args.non_https_heading != args.scheme_less_heading
        or args.non_https_end_heading != args.scheme_less_end_heading
    ):
        raise ValueError(
            "combined non-HTTPS/bare mode requires identical configured bounds"
        )
    if args.combined_non_https_bare:
        ordinals = args.combined_scheme_less_ordinal
        if len(ordinals) != args.expected_scheme_less or len(set(ordinals)) != len(ordinals):
            raise ValueError(
                "combined scheme-less ordinals must be unique and match the expected count"
            )
        if any(number < 1 for number in ordinals):
            raise ValueError("combined scheme-less ordinals must be positive")
    elif args.combined_scheme_less_ordinal:
        raise ValueError(
            "combined scheme-less ordinals require --combined-non-https-bare"
        )
    if args.ignore_post_ledger and args.ledger_end_heading not in {
        "## Exact integration counts and deltas",
        "## Exact acquisition counts and integration deltas",
        "## Acquisition and verification counts",
        "This patch-ready ledger contains ten hierarchy headings and 121 separate topic",
    }:
        raise ValueError(
            "--ignore-post-ledger is allowed only for an exact administrative counts heading"
        )
    if (
        args.no_scheme_less_section
        and args.expected_scheme_less != 0
        and not args.scheme_less_identifier
    ):
        raise ValueError(
            "a nonzero absent scheme-less section requires exact inline identifiers"
        )
    if args.scheme_less_identifier and not args.no_scheme_less_section:
        raise ValueError(
            "--scheme-less-identifier requires --no-scheme-less-section"
        )
    if len(args.scheme_less_identifier) != args.expected_scheme_less:
        if args.no_scheme_less_section:
            raise ValueError(
                "inline scheme-less identifiers do not equal expected scheme-less count"
            )
    expected_level_total = args.expected_h4 + args.expected_h5 + args.expected_h6
    if args.expected_hierarchy != expected_level_total:
        raise ValueError(
            "expected hierarchy aggregate does not equal its level pins: "
            f"{args.expected_hierarchy} != {args.expected_h4} + "
            f"{args.expected_h5} + {args.expected_h6}"
        )
    boundary_targets = {
        "https_start": args.https_heading,
        "non_https_start": args.non_https_heading,
        "ledger_start": args.ledger_heading,
        "ledger_end": args.ledger_end_heading,
    }
    if args.quarantine_https_heading:
        boundary_targets["quarantine_https_start"] = args.quarantine_https_heading
    if not args.no_scheme_less_section and not args.combined_non_https_bare:
        boundary_targets["bare_start"] = args.scheme_less_heading
    if args.https_end_heading:
        boundary_targets["https_end"] = args.https_end_heading
    if args.non_https_end_heading:
        boundary_targets["non_https_end"] = args.non_https_end_heading
    if args.scheme_less_end_heading:
        boundary_targets["bare_end"] = args.scheme_less_end_heading
    positions = {label: [] for label in boundary_targets}
    postamble_hits = {line: 0 for line in args.locator_postamble}
    admin_line_hits = {line: 0 for line in args.locator_admin_line}
    inline_identifier_hits = {value: 0 for value in args.scheme_less_identifier}
    interlude_line_hits = {line: 0 for line in args.ledger_interlude_line}
    with note.open("r", encoding="utf-8", newline="") as handle:
        for line_number, raw in enumerate(handle, start=1):
            line = raw.rstrip("\n")
            if line.endswith("\r"):
                raise ValueError(f"{note}: CR is not allowed")
            for label, heading in boundary_targets.items():
                if line == heading:
                    positions[label].append(line_number)
            if line in postamble_hits:
                postamble_hits[line] += 1
            if line in admin_line_hits:
                admin_line_hits[line] += 1
            for value in inline_identifier_hits:
                inline_identifier_hits[value] += line.count(f"`{value}`")
            if line in interlude_line_hits:
                interlude_line_hits[line] += 1
    malformed = {label: found for label, found in positions.items() if len(found) != 1}
    if malformed:
        raise ValueError(f"{note}: every configured boundary must occur once: {malformed}")
    malformed_postambles = {
        line: count for line, count in postamble_hits.items() if count != 1
    }
    if malformed_postambles:
        raise ValueError(
            f"{note}: every configured locator postamble must occur once: "
            f"{malformed_postambles}"
        )
    malformed_admin_lines = {
        line: count for line, count in admin_line_hits.items() if count != 1
    }
    if malformed_admin_lines:
        raise ValueError(
            f"{note}: every configured locator administrative line must occur once: "
            f"{malformed_admin_lines}"
        )
    malformed_inline_identifiers = {
        value: count
        for value, count in inline_identifier_hits.items()
        if count < 1
    }
    if malformed_inline_identifiers:
        raise ValueError(
            f"{note}: every inline scheme-less identifier must occur: "
            f"{malformed_inline_identifiers}"
        )
    malformed_interlude_lines = {
        line: count for line, count in interlude_line_hits.items() if count != 1
    }
    if malformed_interlude_lines:
        raise ValueError(
            f"{note}: every configured ledger interlude line must occur once: "
            f"{malformed_interlude_lines}"
        )
    if positions["ledger_start"][0] >= positions["ledger_end"][0]:
        raise ValueError(f"{note}: ledger boundaries are reversed")
    if args.ledger_admin_start:
        admin_positions: list[int] = []
        with note.open("r", encoding="utf-8", newline="") as handle:
            for line_number, raw in enumerate(handle, start=1):
                if raw.rstrip("\n") == args.ledger_admin_start:
                    admin_positions.append(line_number)
        if len(admin_positions) != 1 or not (
            positions["ledger_start"][0]
            < admin_positions[0]
            <= positions["ledger_end"][0]
        ):
            raise ValueError(
                f"{note}: configured ledger administrative start must occur once inside ledger bounds"
            )
    implicit_ends = {
        "https_start": (
            "quarantine_https_start"
            if args.quarantine_https_heading
            else "non_https_start"
        ),
        "non_https_start": (
            "ledger_start" if args.no_scheme_less_section else "bare_start"
        ),
    }
    if args.quarantine_https_heading:
        implicit_ends["quarantine_https_start"] = "non_https_start"
    if args.combined_non_https_bare:
        implicit_ends["non_https_start"] = "ledger_start"
    if not args.no_scheme_less_section and not args.combined_non_https_bare:
        implicit_ends["bare_start"] = "ledger_start"
    explicit_ends = {
        "https_start": "https_end",
        "non_https_start": "non_https_end",
        "bare_start": "bare_end",
    }
    for start_label, implicit_end in implicit_ends.items():
        end_label = explicit_ends.get(start_label)
        selected_end = (
            end_label if end_label is not None and end_label in positions else implicit_end
        )
        if positions[start_label][0] >= positions[selected_end][0]:
            raise ValueError(
                f"{note}: {start_label} does not precede its configured end"
            )
    section = "before"
    in_ledger = False
    ledger_content_seen = False
    ledger_preamble_seen = False
    counters = {
        "https": 0,
        "quarantine_https": 0,
        "non_https": 0,
        "bare": 0,
        "hierarchy": 0,
        "h4": 0,
        "h5": 0,
        "h6": 0,
        "topics": 0,
    }
    counters["bare"] = len(args.scheme_less_identifier)
    expected_number = 1
    pending_preamble: list[str] = []
    with note.open("r", encoding="utf-8", newline="") as handle:
        for raw in handle:
            line = raw.rstrip("\n")
            if line.endswith("\r"):
                raise ValueError(f"{note}: CR is not allowed")
            if line == args.ledger_heading:
                in_ledger = True
                section = "between"
                continue
            if line == args.ledger_end_heading:
                if not in_ledger and not (
                    args.ledger_admin_start and section == "after"
                ):
                    raise ValueError(f"{note}: unmatched or duplicate ledger end")
                if pending_preamble:
                    raise ValueError(
                        f"{note}: ledger ends inside preamble block {tuple(pending_preamble)!r}"
                    )
                in_ledger = False
                section = "after"
                if line == args.https_heading:
                    section, expected_number = "https", 1
                continue
            if in_ledger:
                if line in args.ledger_interlude_line:
                    continue
                if heading_match := HEADING_RE.fullmatch(line):
                    if pending_preamble:
                        block = tuple(pending_preamble)
                        if not (
                            admitted_ledger_preamble_block(pending_preamble)
                            or exact_configured_block(
                                pending_preamble, args.ledger_preamble_line
                            )
                        ):
                            raise ValueError(f"{note}: untyped ledger preamble block {block!r}")
                        ledger_preamble_seen = True
                        pending_preamble.clear()
                    counters["hierarchy"] += 1
                    counters[f"h{len(heading_match.group('marks'))}"] += 1
                    ledger_content_seen = True
                elif args.ledger_admin_start and line == args.ledger_admin_start:
                    in_ledger = False
                    section = "after"
                    continue
                elif line.startswith("- "):
                    if pending_preamble:
                        block = tuple(pending_preamble)
                        if not (
                            admitted_ledger_preamble_block(pending_preamble)
                            or exact_configured_block(
                                pending_preamble, args.ledger_preamble_line
                            )
                        ):
                            raise ValueError(f"{note}: untyped ledger preamble block {block!r}")
                        ledger_preamble_seen = True
                        pending_preamble.clear()
                    if not (
                        line.endswith(OPEN_SUFFIXES)
                        or QUALIFIED_OPEN_TOPIC_RE.fullmatch(line) is not None
                    ):
                        raise ValueError(f"{note}: topic is not explicitly OPEN: {line!r}")
                    counters["topics"] += 1
                    ledger_content_seen = True
                elif line:
                    if ledger_preamble_seen or ledger_content_seen:
                        raise ValueError(
                            f"{note}: administrative ledger preamble is duplicated or misplaced"
                        )
                    pending_preamble.append(line)
            elif section == "after" and line:
                if args.ignore_post_ledger:
                    continue
                if HEADING_RE.fullmatch(line) or line.endswith(OPEN_SUFFIXES):
                    raise ValueError(
                        f"{note}: source record occurs after the declared ledger end: {line!r}"
                    )
                if POST_LEDGER_ADMIN_BULLET_RE.fullmatch(line) is not None:
                    # The allowlist is the current exact administrative
                    # count/gate vocabulary; an unknown bullet fails closed.
                    continue
                if (
                    args.ledger_end_heading == "## Final OPEN statement"
                    and FINAL_OPEN_ADMIN_RE.fullmatch(line) is not None
                ):
                    continue
                raise ValueError(
                    f"{note}: untyped content occurs after the declared ledger end: {line!r}"
                )
            if line == args.https_heading:
                section, expected_number = "https", 1
                continue
            if args.quarantine_https_heading and line == args.quarantine_https_heading:
                section, expected_number = "quarantine_https", 1
                continue
            if line == args.non_https_heading:
                section, expected_number = (
                    "combined" if args.combined_non_https_bare else "non_https"
                ), 1
                continue
            if line == args.scheme_less_heading and not args.combined_non_https_bare:
                section, expected_number = "bare", 1
                continue
            if section == "https" and args.https_end_heading and line == args.https_end_heading:
                section = "between"
                continue
            if section in {"non_https", "combined"} and args.non_https_end_heading and line == args.non_https_end_heading:
                section = "between"
                continue
            if section == "bare" and args.scheme_less_end_heading and line == args.scheme_less_end_heading:
                section = "between"
                continue
            if section in {
                "https",
                "quarantine_https",
                "non_https",
                "bare",
                "combined",
            }:
                if not line:
                    continue
                parsed = parse_locator_row(
                    line,
                    (
                        "https"
                        if section == "quarantine_https"
                        else "non_https" if section == "combined" else section
                    ),
                    args.locator_rows_have_provenance,
                )
                if parsed is None:
                    if line in args.locator_postamble or line in args.locator_admin_line:
                        continue
                    raise ValueError(f"{note}: malformed {section} locator row {line!r}")
                number, value = parsed
                if number != expected_number:
                    raise ValueError(f"{note}: {section} locator sequence expected {expected_number}")
                if section in {"https", "quarantine_https"} and not value.startswith(
                    "https://"
                ):
                    raise ValueError(f"{note}: HTTPS row has wrong scheme")
                if section == "non_https" and (
                    not ADMITTED_NON_HTTPS_SCHEME_RE.match(value)
                    or value.lower().startswith("https:")
                ):
                    raise ValueError(f"{note}: non-HTTPS row lacks a non-HTTPS URI scheme")
                # The explicitly named scheme-less section controls standing.
                # A source-displayed identifier can begin with characters that
                # resemble a URI scheme (for example ``urn:`` or ``ark:``)
                # without the acquisition record assigning it URI standing.
                # Reclassifying it here would be an editorial normalization.
                if section == "combined":
                    if number in args.combined_scheme_less_ordinal:
                        counters["bare"] += 1
                    else:
                        if (
                            not ADMITTED_NON_HTTPS_SCHEME_RE.match(value)
                            or value.lower().startswith("https:")
                        ):
                            raise ValueError(
                                f"{note}: combined non-HTTPS ordinal lacks admitted URI scheme"
                            )
                        counters["non_https"] += 1
                else:
                    counters[section] += 1
                expected_number += 1
    if pending_preamble:
        raise ValueError(f"{note}: unclosed ledger preamble block {tuple(pending_preamble)!r}")
    if in_ledger or section in {
        "https",
        "quarantine_https",
        "non_https",
        "bare",
        "combined",
    }:
        raise ValueError(f"{note}: an admitted section is not closed")
    expected = {
        "https": args.expected_https,
        "quarantine_https": args.expected_quarantine_https,
        "non_https": args.expected_non_https,
        "bare": args.expected_scheme_less,
        "hierarchy": args.expected_hierarchy,
        "h4": args.expected_h4,
        "h5": args.expected_h5,
        "h6": args.expected_h6,
        "topics": args.expected_topics,
    }
    if counters != expected:
        raise ValueError(f"count mismatch: observed {counters}, expected {expected}")
    return counters


def iter_note_values(
    note: Path, target: str, args: argparse.Namespace
) -> Iterable[str]:
    if target == "bare" and args.no_scheme_less_section:
        yield from args.scheme_less_identifier
        return
    section = "before"
    seen_target = False
    with note.open("r", encoding="utf-8", newline="") as handle:
        for raw in handle:
            line = raw.rstrip("\n")
            if line == args.https_heading:
                section = "https"
                seen_target = seen_target or target == "https"
                continue
            if args.quarantine_https_heading and line == args.quarantine_https_heading:
                if seen_target and target == "https":
                    break
                section = "quarantine_https"
                continue
            if line == args.non_https_heading:
                section = "combined" if args.combined_non_https_bare else "non_https"
                if args.combined_non_https_bare:
                    seen_target = seen_target or target in {"non_https", "bare"}
                else:
                    seen_target = seen_target or target == "non_https"
                continue
            if line == args.scheme_less_heading and not args.combined_non_https_bare:
                section = "bare"
                seen_target = seen_target or target == "bare"
                continue
            if line == args.ledger_heading:
                if seen_target:
                    break
                continue
            if line == args.ledger_end_heading:
                if seen_target:
                    break
                continue
            if section == "https" and args.https_end_heading and line == args.https_end_heading:
                section = "between"
                continue
            if section in {"non_https", "combined"} and args.non_https_end_heading and line == args.non_https_end_heading:
                section = "between"
                continue
            if section == "bare" and args.scheme_less_end_heading and line == args.scheme_less_end_heading:
                section = "between"
                continue
            if (section == target or section == "combined") and line:
                parsed = parse_locator_row(
                    line,
                    "non_https" if section == "combined" else section,
                    args.locator_rows_have_provenance,
                )
                if parsed is None:
                    if line in args.locator_postamble or line in args.locator_admin_line:
                        continue
                    raise ValueError(f"{note}: malformed {target} row")
                value = parsed[1]
                if section == "combined":
                    is_non_https = parsed[0] not in args.combined_scheme_less_ordinal
                    if (target == "non_https") != is_non_https:
                        continue
                yield value


def write_replacement(
    output: TextIO,
    heading: str,
    metadata: list[str],
    note: Path,
    counts: dict[str, int],
    args: argparse.Namespace,
) -> None:
    output.write(heading + "\n\n")
    for line in metadata:
        output.write(line + "\n")
    for number, value in enumerate(iter_note_values(note, "https", args), start=1):
        output.write(f"- Exact HTTPS locator {number}: {value}\n")
    for number, value in enumerate(
        iter_note_values(note, "non_https", args), start=1
    ):
        output.write(f"- Exact non-HTTPS locator {number}: {value}\n")
    for number, value in enumerate(iter_note_values(note, "bare", args), start=1):
        output.write(f"- Exact scheme-less identifier {number}: {value}\n")
    output.write(
        "- Retrieved granularity: exact acquisition-note ledger containing "
        f"{counts['https']} HTTPS locators, {counts['non_https']} non-HTTPS locators, "
        f"{counts['bare']} scheme-less identifiers, {counts['hierarchy']} displayed "
        f"hierarchy headings, and {counts['topics']} separate topics; every presentation remains OPEN\n\n"
    )
    copying = False
    at_ledger_content_start = False
    with note.open("r", encoding="utf-8", newline="") as handle:
        for raw in handle:
            line = raw.rstrip("\n")
            if line == args.ledger_heading:
                copying = True
                at_ledger_content_start = True
                continue
            if line == args.ledger_end_heading:
                break
            if not copying:
                continue
            if args.ledger_admin_start and line == args.ledger_admin_start:
                break
            if line in args.ledger_interlude_line:
                continue
            if at_ledger_content_start:
                if not line:
                    continue
                if args.ledger_preamble_line:
                    if line == args.ledger_preamble_line[0]:
                        for expected in args.ledger_preamble_line[1:]:
                            following = next(handle, None)
                            if following is None or following.rstrip("\n") != expected:
                                raise ValueError(
                                    f"{note}: configured ledger preamble changed during emission"
                                )
                        continue
                elif LEDGER_PREAMBLE_RE.fullmatch(line):
                    continue
                else:
                    matched_preamble = False
                    for block in LEDGER_PREAMBLE_BLOCKS:
                        if line != block[0]:
                            continue
                        matched_preamble = True
                        for expected in block[1:]:
                            following = next(handle, None)
                            if following is None or following.rstrip("\n") != expected:
                                raise ValueError(
                                    f"{note}: admitted ledger preamble changed during emission"
                                )
                        break
                    if matched_preamble:
                        continue
                at_ledger_content_start = False
            output.write(line + "\n")
    output.write("\n")


def stream_transform(
    baseline: Path,
    output: TextIO,
    source_id: str,
    replacement_writer,
) -> None:
    state = "before"
    found = 0
    with baseline.open("r", encoding="utf-8", newline="") as handle:
        for raw in handle:
            line = raw.rstrip("\n")
            match = SOURCE_RE.fullmatch(line)
            if match and match.group("id") == source_id:
                found += 1
                if found != 1 or state != "before":
                    raise ValueError(
                        f"{baseline}: duplicate or misplaced {source_id} source block"
                    )
                replacement_writer(output)
                state = "skip"
                continue
            if state == "skip":
                if (match and match.group("id") != source_id) or line == "---":
                    output.write(raw)
                    state = "after"
                continue
            output.write(raw)
    if found != 1 or state == "skip":
        raise ValueError(f"{baseline}: expected one complete {source_id} block, found {found}")


def files_equal(left: Path, right: Path) -> bool:
    if left.stat().st_size != right.stat().st_size:
        return False
    with left.open("rb") as a, right.open("rb") as b:
        while True:
            ca, cb = a.read(1024 * 1024), b.read(1024 * 1024)
            if ca != cb:
                return False
            if not ca:
                return True


def replace_after_stability_check(
    temporary: Path, target: Path, expected_digest: str
) -> None:
    """Atomically replace after each bounded Windows reader-lock retry.

    Necessity: antivirus/indexing readers can transiently deny ``os.replace``
    on Windows even though neither input changed. Definition: retry at most ten
    times, verifying the target's expected SHA-256 immediately before every
    replacement attempt. Standing: this is an administrative installation
    guard. Nonredundancy: retrying without the digest check could overwrite a
    genuine concurrent edit. Use: write mode installs only through this guard.
    """

    for attempt in range(10):
        if file_sha256(target) != expected_digest:
            raise ValueError(f"{target}: baseline changed before atomic replacement")
        try:
            temporary.replace(target)
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
    parser.add_argument("--expected-https", type=int, required=True)
    parser.add_argument("--expected-quarantine-https", type=int, default=0)
    parser.add_argument("--expected-non-https", type=int, required=True)
    parser.add_argument("--expected-scheme-less", type=int, required=True)
    parser.add_argument("--expected-hierarchy", type=int, required=True)
    parser.add_argument("--expected-h4", type=int, required=True)
    parser.add_argument("--expected-h5", type=int, required=True)
    parser.add_argument("--expected-h6", type=int, required=True)
    parser.add_argument("--expected-topics", type=int, required=True)
    parser.add_argument("--https-heading", default=HTTPS_START)
    parser.add_argument("--quarantine-https-heading")
    parser.add_argument("--https-end-heading")
    parser.add_argument("--non-https-heading", default=NON_HTTPS_START)
    parser.add_argument("--non-https-end-heading")
    parser.add_argument(
        "--locator-postamble",
        action="append",
        default=[],
        help="exact nonblank administrative line admitted inside a locator bound",
    )
    parser.add_argument(
        "--locator-admin-line",
        action="append",
        default=[],
        help="exact nonblank administrative line admitted inside locator sections",
    )
    parser.add_argument("--locator-rows-have-provenance", action="store_true")
    parser.add_argument("--combined-non-https-bare", action="store_true")
    parser.add_argument(
        "--combined-scheme-less-ordinal", action="append", type=int, default=[]
    )
    parser.add_argument("--scheme-less-heading", default=SCHEMELESS_START)
    parser.add_argument("--scheme-less-end-heading")
    parser.add_argument("--no-scheme-less-section", action="store_true")
    parser.add_argument("--scheme-less-identifier", action="append", default=[])
    parser.add_argument("--ledger-heading", default=LEDGER_START)
    parser.add_argument("--ledger-end-heading", default=LEDGER_END)
    parser.add_argument("--ledger-preamble-line", action="append", default=[])
    parser.add_argument("--ledger-interlude-line", action="append", default=[])
    parser.add_argument("--ledger-admin-start")
    parser.add_argument("--ignore-post-ledger", action="store_true")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    args.baseline = args.baseline.resolve()
    args.note = args.note.resolve()
    original_note = args.note
    original_baseline = args.baseline
    snapshot, snapshot_digest = stable_note_snapshot(original_note)
    baseline_snapshot, baseline_snapshot_digest = stable_note_snapshot(original_baseline)
    args.note = snapshot
    args.baseline = baseline_snapshot
    fd, name = tempfile.mkstemp(
        prefix=original_baseline.name + ".", suffix=".tmp", dir=original_baseline.parent
    )
    os.close(fd)
    temporary = Path(name)
    try:
        counts = scan_note(args.note, args)
        heading, metadata = source_metadata(args.baseline, args.source_id)
        with temporary.open("w", encoding="utf-8", newline="\n") as output:
            stream_transform(
                args.baseline,
                output,
                args.source_id,
                lambda handle: write_replacement(
                    handle, heading, metadata, args.note, counts, args
                ),
            )
        if file_sha256(original_note) != snapshot_digest:
            raise ValueError(f"{original_note}: note changed after snapshot validation")
        if file_sha256(original_baseline) != baseline_snapshot_digest:
            raise ValueError(
                f"{original_baseline}: baseline changed after snapshot validation"
            )
        if args.check:
            if not files_equal(baseline_snapshot, temporary):
                print(f"{args.source_id}: baseline source block is stale", file=sys.stderr)
                return 1
            print(f"{args.source_id}: streamed acquisition-note block matches exactly")
            return 0
        replace_after_stability_check(
            temporary, original_baseline, baseline_snapshot_digest
        )
        print(f"{args.source_id}: streamed acquisition-note block replaced exactly")
        return 0
    finally:
        temporary.unlink(missing_ok=True)
        snapshot.unlink(missing_ok=True)
        baseline_snapshot.unlink(missing_ok=True)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, UnicodeError, ValueError) as error:
        print(f"streamed baseline replacement failed: {error}", file=sys.stderr)
        raise SystemExit(1)

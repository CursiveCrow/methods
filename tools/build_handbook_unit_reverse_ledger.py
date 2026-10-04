#!/usr/bin/env python3
"""Build the exhaustive current-handbook unit inventory and reverse join.

The parser partitions physical lines; it does not decide mathematical meaning,
source fidelity, or completion.  Reviewer-supplied records are optional and
fail closed.  A terminal row is admitted only after exact unit identity, live
links, and five separately recorded verification artifacts have been checked.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SNAPSHOT = ROOT / "spec/handbook-construction-snapshot.csv"
DEFAULT_PHYSICAL_INVENTORY = (
    ROOT / "spec/handbook-construction-source-inventory.csv"
)
DEFAULT_UNIT_CSV = ROOT / "spec/handbook-unit-inventory.csv"
DEFAULT_UNIT_MD = ROOT / "spec/handbook-unit-inventory.md"
DEFAULT_REVERSE_CSV = ROOT / "spec/handbook-unit-reverse-ledger.csv"
DEFAULT_REVERSE_MD = ROOT / "spec/handbook-unit-reverse-ledger.md"
DEFAULT_REVIEWED = ROOT / "spec/provenance/reviewed-handbook-unit-records.json"
DEFAULT_REGISTER_MANIFEST = ROOT / "spec/register-obligation-manifest.csv"
DEFAULT_PRESENTATION_ROOT = ROOT / "spec/presentations"

SCHEMA_VERSION = 2
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
LABEL_RE = re.compile(r"^[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9][A-Za-z0-9._:-]*$")
SNAPSHOT_FIELDS = ("path", "bytes", "sha256")
PHYSICAL_FIELDS = (
    "record_id",
    "record_type",
    "path",
    "line_number",
    "bytes",
    "sha256",
    "provenance_status",
    "source_authority_ids",
)
INVENTORY_FIELDS = (
    "unit_id",
    "record_type",
    "path",
    "start_line",
    "end_line",
    "bytes",
    "sha256",
    "unit_kind",
    "named_owner_key",
    "named_title",
    "stable_labels",
    "line_standing",
    "parser_basis",
    "parser_status",
    "mapping_status",
    "semantic_review_status",
    "source_authority_ids",
    "presentation_packet_ids",
    "register_obligation_ids",
)
VERIFICATION_FIELDS = (
    "source_fidelity_ai",
    "topic_specialist_ai",
    "adversarial_publication_ai",
    "static",
    "build",
    "visual",
)
AI_REVIEW_FIELDS = VERIFICATION_FIELDS[:3]
REVERSE_FIELDS = INVENTORY_FIELDS + tuple(
    f"{name}_verification" for name in VERIFICATION_FIELDS
) + ("verification_evidence", "review_record_sha256")
REVIEW_IDENTITY_FIELDS = (
    "unit_id",
    "record_type",
    "path",
    "start_line",
    "end_line",
    "bytes",
    "sha256",
    "unit_kind",
    "named_owner_key",
    "named_title",
    "stable_labels",
    "line_standing",
    "parser_basis",
    "parser_status",
)
REVIEW_RECORD_FIELDS = set(REVIEW_IDENTITY_FIELDS) | {
    "mapping_status",
    "semantic_review_status",
    "source_authority_ids",
    "presentation_packet_ids",
    "register_obligation_ids",
    "verification",
    "verification_evidence",
}
EVIDENCE_FIELDS = {
    "category",
    "recorded_result",
    "artifact_path",
    "sha256",
    "producer_identity",
    "recorded_scope",
}
AI_EVIDENCE_FIELDS = EVIDENCE_FIELDS | {
    "model",
    "model_version",
    "instructions",
    "consulted_authorities",
    "findings",
    "other_review_outputs_consulted",
}
CONSULTED_AUTHORITY_FIELDS = {"path", "locator", "sha256"}

READER_STANDING = "reader-facing candidate"
CONTROL_STANDING = "nonprinting control candidate"
COMMENT_STANDING = "comment"
BLANK_STANDING = "blank material"
BINARY_STANDING = "binary artifact"
EMPTY_STANDING = "empty text artifact"

TEX_ENVIRONMENTS = {
    "hbtheorem": ("theorem", 40),
    "hblemma": ("lemma", 40),
    "hbcorollary": ("corollary", 40),
    "hbdefinition": ("definition", 40),
    "hbconvention": ("convention", 40),
    "hbmethod": ("method", 40),
    "hbexample": ("example", 40),
    "hbwarning": ("warning", 40),
    "proofboundary": ("proof-boundary", 40),
    "systementry": ("system-entry", 40),
    "annexitem": ("annex-item", 40),
    "inheritedrestorationscope": ("restoration-scope", 35),
    "definition": ("definition", 25),
    "theorem": ("theorem", 25),
    "lemma": ("lemma", 25),
    "proposition": ("proposition", 25),
    "corollary": ("corollary", 25),
    "example": ("example", 25),
    "exercise": ("exercise", 25),
    "solution": ("solution", 25),
    "remark": ("remark", 25),
    "warning": ("warning", 25),
    "proof": ("proof", 20),
    "figure": ("figure", 20),
    "table": ("table", 20),
}
TEX_BEGIN_END_RE = re.compile(r"\\(begin|end)\s*\{([A-Za-z*@]+)\}")
TEX_HEADING_RE = re.compile(
    r"\\(part|chapter|section|subsection|subsubsection|paragraph)\*?\s*\{([^{}]*)\}"
)
TEX_NAMED_COMMAND_RE = re.compile(
    r"\\(calculussheet|hbrule)\s*\{([^{}]+)\}\s*\{([^{}]*)\}"
)
TEX_EXPLICIT_LABEL_RE = re.compile(r"\\label\s*\{\s*([^{}\s]+)\s*\}")
TEX_TYPED_ENV_LABEL_RE = re.compile(
    r"\\begin\s*\{(?:hbtheorem|hblemma|hbcorollary|hbdefinition|hbconvention|"
    r"hbmethod|hbexample|hbwarning|proofboundary|systementry|annexitem)\}"
    r"\s*\{\s*([^{}\s]+)\s*\}"
)
NONPRINTING_COMMAND_RE = re.compile(
    r"^\s*(?:\{|\}|\\(?:documentclass|usepackage|RequirePackage|ProvidesPackage|"
    r"input|include|label|index|phantomsection|addcontentsline|setcounter|"
    r"newcommand|renewcommand|providecommand|DeclareMathOperator|newenvironment|"
    r"NewDocumentCommand|NewDocumentEnvironment|def|let|makeatletter|makeatother|"
    r"frontmatter|mainmatter|backmatter|clearpage|newpage|pagebreak|nopagebreak|"
    r"medskip|smallskip|bigskip|vspace|hspace|pagestyle|thispagestyle|hypersetup|"
    r"geometry|setlength|addtolength|bibliographystyle|bibliography)\b[^\n]*|"
    r"\\(?:begin|end)\s*\{(?:document|center|titlepage|itemize|enumerate|description|"
    r"landscape|minipage|longtable|tabular|tikzpicture|align\*?|gathered|aligned|"
    r"array|cases)\}[^\n]*|\\end\s*\{[^{}]+\}\s*)$"
)


class DuplicateJsonFieldError(ValueError):
    """A repeated JSON name makes the governed input ambiguous."""


@dataclass(frozen=True)
class Owner:
    start: int
    end: int
    kind: str
    key: str
    title: str
    labels: tuple[str, ...]
    basis: str
    priority: int


@dataclass(frozen=True)
class PhysicalFile:
    file_id: str
    path: str
    raw: bytes
    lines: tuple[bytes, ...] | None


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def json_compact(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def duplicate_rejecting_object(
    pairs: list[tuple[str, object]],
) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateJsonFieldError(f"duplicate JSON field {key!r}")
        result[key] = value
    return result


def require_exact_fields(
    value: object, expected: set[str], location: str
) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"{location}: expected object")
    missing = sorted(expected - set(value))
    extra = sorted(set(value) - expected)
    if missing or extra:
        details: list[str] = []
        if missing:
            details.append(f"missing {missing}")
        if extra:
            details.append(f"unexpected {extra}")
        raise ValueError(f"{location}: exact field set required ({'; '.join(details)})")
    return value


def repository_path(root: Path, value: object, location: str) -> tuple[str, Path]:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{location}: expected nonempty canonical path")
    if "\\" in value:
        raise ValueError(f"{location}: use repository-relative POSIX path syntax")
    pure = PurePosixPath(value)
    if pure.is_absolute() or any(part in ("", ".", "..") for part in pure.parts):
        raise ValueError(f"{location}: path traversal is forbidden")
    if pure.parts and re.fullmatch(r"[A-Za-z]:", pure.parts[0]) is not None:
        raise ValueError(f"{location}: drive-qualified path is forbidden")
    if pure.as_posix() != value:
        raise ValueError(f"{location}: path is not canonical")
    resolved_root = root.resolve()
    resolved = (resolved_root / Path(*pure.parts)).resolve()
    try:
        resolved.relative_to(resolved_root)
    except ValueError as exc:
        raise ValueError(f"{location}: path escapes repository") from exc
    return value, resolved


def parse_csv_exact(path: Path, fields: tuple[str, ...], label: str) -> list[dict[str, str]]:
    try:
        text = path.read_bytes().decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"{label} is not UTF-8") from exc
    with io.StringIO(text, newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != fields:
            raise ValueError(f"{label} has an unexpected schema")
        rows = list(reader)
    return rows


def canonical_decimal(value: str, location: str, *, minimum: int = 0) -> int:
    if not value.isascii() or not value.isdecimal() or str(int(value)) != value:
        raise ValueError(f"{location}: expected canonical decimal")
    result = int(value)
    if result < minimum:
        raise ValueError(f"{location}: value must be at least {minimum}")
    return result


def load_physical_files(
    snapshot_path: Path,
    physical_inventory_path: Path,
    root: Path,
    expected_snapshot_sha256: str | None = None,
) -> tuple[list[PhysicalFile], str]:
    snapshot_raw = snapshot_path.read_bytes()
    snapshot_sha = sha256_bytes(snapshot_raw)
    if expected_snapshot_sha256 is not None and snapshot_sha != expected_snapshot_sha256:
        raise ValueError("construction snapshot is not the pinned current record")
    snapshot_rows = parse_csv_exact(snapshot_path, SNAPSHOT_FIELDS, "construction snapshot")
    if not snapshot_rows:
        raise ValueError("construction snapshot is empty")
    if [row["path"] for row in snapshot_rows] != sorted(row["path"] for row in snapshot_rows):
        raise ValueError("construction snapshot paths are not in canonical order")
    if len({row["path"] for row in snapshot_rows}) != len(snapshot_rows):
        raise ValueError("construction snapshot contains duplicate paths")

    physical_rows = parse_csv_exact(
        physical_inventory_path, PHYSICAL_FIELDS, "construction physical inventory"
    )
    cursor = 0
    result: list[PhysicalFile] = []
    for file_index, snapshot in enumerate(snapshot_rows, start=1):
        location = f"construction snapshot row {file_index}"
        path_value, live_path = repository_path(root, snapshot["path"], f"{location}.path")
        if not path_value.startswith("handbook/") or not live_path.is_file():
            raise ValueError(f"{location}: handbook file does not exist")
        byte_count = canonical_decimal(snapshot["bytes"], f"{location}.bytes")
        if SHA256_RE.fullmatch(snapshot["sha256"]) is None:
            raise ValueError(f"{location}.sha256: malformed digest")
        raw = live_path.read_bytes()
        if len(raw) != byte_count or sha256_bytes(raw) != snapshot["sha256"]:
            raise ValueError(f"snapshot source drifted: {path_value}")

        expected_file_id = f"HB-F{file_index:04d}"
        if cursor >= len(physical_rows):
            raise ValueError(f"physical inventory lacks {expected_file_id}")
        expected_file_row = {
            "record_id": expected_file_id,
            "record_type": "file",
            "path": path_value,
            "line_number": "",
            "bytes": str(len(raw)),
            "sha256": sha256_bytes(raw),
            "provenance_status": "open/unmapped",
            "source_authority_ids": "[]",
        }
        if physical_rows[cursor] != expected_file_row:
            raise ValueError(f"physical inventory file row differs: {expected_file_id}")
        cursor += 1

        try:
            raw.decode("utf-8")
            lines: tuple[bytes, ...] | None = tuple(raw.splitlines(keepends=True))
        except UnicodeDecodeError:
            lines = None
        if lines is not None:
            for line_number, line in enumerate(lines, start=1):
                expected_id = f"{expected_file_id}-L{line_number:06d}"
                if cursor >= len(physical_rows):
                    raise ValueError(f"physical inventory lacks {expected_id}")
                expected_line_row = {
                    "record_id": expected_id,
                    "record_type": "physical_line",
                    "path": path_value,
                    "line_number": str(line_number),
                    "bytes": str(len(line)),
                    "sha256": sha256_bytes(line),
                    "provenance_status": "open/unmapped",
                    "source_authority_ids": "[]",
                }
                if physical_rows[cursor] != expected_line_row:
                    raise ValueError(f"physical inventory line row differs: {expected_id}")
                cursor += 1
        if cursor < len(physical_rows) and physical_rows[cursor]["record_type"] != "file":
            raise ValueError(f"physical inventory has excess lines for {expected_file_id}")
        result.append(PhysicalFile(expected_file_id, path_value, raw, lines))
    if cursor != len(physical_rows):
        raise ValueError("physical inventory has records beyond the snapshot")
    return result, snapshot_sha


def tex_active(line: str) -> str:
    for index, char in enumerate(line):
        if char != "%":
            continue
        slash_count = 0
        cursor = index - 1
        while cursor >= 0 and line[cursor] == "\\":
            slash_count += 1
            cursor -= 1
        if slash_count % 2 == 0:
            return line[:index]
    return line


def normalized_title(value: str) -> str:
    return " ".join(value.split())


def labels_in_tex(value: str) -> tuple[str, ...]:
    active = "\n".join(tex_active(line) for line in value.splitlines())
    labels = set(TEX_EXPLICIT_LABEL_RE.findall(active))
    labels.update(TEX_TYPED_ENV_LABEL_RE.findall(active))
    labels.update(match.group(2) for match in TEX_NAMED_COMMAND_RE.finditer(active))
    return tuple(sorted(label for label in labels if LABEL_RE.fullmatch(label)))


def tex_owners(path: str, lines: tuple[str, ...]) -> list[Owner]:
    owners: list[Owner] = []
    stacks: dict[str, list[int]] = {name: [] for name in TEX_ENVIRONMENTS}
    active_lines = tuple(tex_active(line) for line in lines)
    for line_number, active in enumerate(active_lines, start=1):
        for token in TEX_BEGIN_END_RE.finditer(active):
            action, environment = token.groups()
            if environment not in TEX_ENVIRONMENTS:
                continue
            if action == "begin":
                stacks[environment].append(line_number)
                continue
            if not stacks[environment]:
                continue
            start = stacks[environment].pop()
            kind, priority = TEX_ENVIRONMENTS[environment]
            span_text = "".join(lines[start - 1 : line_number])
            labels = labels_in_tex(span_text)
            begin_match = re.search(
                r"\\begin\s*\{" + re.escape(environment) + r"\}"
                r"(?:\s*\{[^{}]*\}){0,2}\s*\{([^{}]*)\}",
                tex_active(lines[start - 1]),
            )
            title = normalized_title(begin_match.group(1)) if begin_match else ""
            key = f"N::{path}::tex-env::{environment}::{start:06d}"
            owners.append(
                Owner(
                    start,
                    line_number,
                    kind,
                    key,
                    title,
                    labels,
                    f"recognized TeX environment {environment}",
                    priority,
                )
            )
    for environment, starts in stacks.items():
        kind, priority = TEX_ENVIRONMENTS[environment]
        for start in starts:
            span_text = "".join(lines[start - 1 :])
            owners.append(
                Owner(
                    start,
                    len(lines),
                    kind,
                    f"N::{path}::tex-env-open::{environment}::{start:06d}",
                    "",
                    labels_in_tex(span_text),
                    f"recognized open TeX environment {environment}",
                    priority - 1,
                )
            )

    for line_number, active in enumerate(active_lines, start=1):
        for match in TEX_HEADING_RE.finditer(active):
            command, title = match.groups()
            labels = labels_in_tex(active)
            owners.append(
                Owner(
                    line_number,
                    line_number,
                    f"{command}-heading",
                    f"N::{path}::tex-heading::{command}::{line_number:06d}",
                    normalized_title(title),
                    labels,
                    f"recognized TeX {command} heading",
                    50,
                )
            )
        for match in TEX_NAMED_COMMAND_RE.finditer(active):
            command, label, title = match.groups()
            labels = tuple(sorted(set(labels_in_tex(active)) | {label}))
            owners.append(
                Owner(
                    line_number,
                    line_number,
                    "calculus-sheet" if command == "calculussheet" else "rule",
                    f"N::{path}::tex-command::{command}::{line_number:06d}",
                    normalized_title(title),
                    labels,
                    f"recognized TeX {command} command",
                    50,
                )
            )
    return owners


def markdown_owners(path: str, lines: tuple[str, ...]) -> list[Owner]:
    owners: list[Owner] = []
    for line_number, line in enumerate(lines, start=1):
        match = re.match(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$", line.rstrip("\r\n"))
        if match:
            level, title = match.groups()
            owners.append(
                Owner(
                    line_number,
                    line_number,
                    f"markdown-heading-{len(level)}",
                    f"N::{path}::markdown-heading::{line_number:06d}",
                    normalized_title(title),
                    (),
                    "recognized Markdown ATX heading",
                    50,
                )
            )
    return owners


def bibliography_owners(path: str, lines: tuple[str, ...]) -> list[Owner]:
    starts: list[tuple[int, str, str]] = []
    for line_number, line in enumerate(lines, start=1):
        match = re.match(r"^\s*@([A-Za-z]+)\s*[({]\s*([^,\s]+)", line)
        if match:
            starts.append((line_number, match.group(1).lower(), match.group(2)))
    owners: list[Owner] = []
    for index, (start, entry_type, key_value) in enumerate(starts):
        end = starts[index + 1][0] - 1 if index + 1 < len(starts) else len(lines)
        owners.append(
            Owner(
                start,
                end,
                f"bibliography-{entry_type}",
                f"N::{path}::bib::{key_value}::{start:06d}",
                key_value,
                (),
                "recognized BibTeX entry",
                35,
            )
        )
    return owners


def csv_owners(path: str, text: str) -> list[Owner]:
    owners: list[Owner] = []
    with io.StringIO(text, newline="") as handle:
        reader = csv.reader(handle)
        previous_end = 0
        for row_index, row in enumerate(reader, start=1):
            end = reader.line_num
            start = previous_end + 1
            previous_end = end
            if row_index == 1:
                continue
            title = row[0] if row else ""
            owners.append(
                Owner(
                    start,
                    end,
                    "csv-record",
                    f"N::{path}::csv-record::{row_index:06d}",
                    normalized_title(title),
                    (),
                    "recognized CSV data record",
                    35,
                )
            )
    return owners


def select_owners(owners: Iterable[Owner], line_count: int) -> list[Owner | None]:
    selected: list[Owner | None] = [None] * line_count
    for line_number in range(1, line_count + 1):
        candidates = [owner for owner in owners if owner.start <= line_number <= owner.end]
        if candidates:
            selected[line_number - 1] = max(
                candidates,
                key=lambda owner: (
                    owner.priority,
                    -(owner.end - owner.start),
                    owner.start,
                    owner.key,
                ),
            )
    return selected


def tex_control_only(active: str) -> bool:
    stripped = active.strip()
    if not stripped:
        return True
    return NONPRINTING_COMMAND_RE.fullmatch(active.rstrip("\r\n")) is not None


def line_classification(
    suffix: str,
    line_number: int,
    line: str,
    owner: Owner | None,
) -> tuple[str, str, str]:
    without_break = line.rstrip("\r\n")
    if not without_break.strip():
        return "blank", BLANK_STANDING, "lexical blank line"
    if suffix in {".tex", ".sty"}:
        if without_break.lstrip().startswith("%"):
            return "comment", COMMENT_STANDING, "TeX comment line"
        active = tex_active(without_break)
        if not active.strip():
            return "comment", COMMENT_STANDING, "TeX comment line"
        if owner is not None:
            if tex_control_only(active):
                return "control", CONTROL_STANDING, f"{owner.basis}; lexical control line"
            return owner.kind, READER_STANDING, owner.basis
        if suffix == ".sty" or tex_control_only(active):
            return "control", CONTROL_STANDING, "lexical TeX control line"
        return "reader-facing-residual", READER_STANDING, "unowned active TeX line"
    if suffix == ".md":
        if without_break.lstrip().startswith("<!--"):
            return "comment", COMMENT_STANDING, "Markdown comment line"
        if owner is not None:
            return owner.kind, READER_STANDING, owner.basis
        return "reader-facing-residual", READER_STANDING, "unowned Markdown line"
    if suffix == ".bib":
        if without_break.lstrip().startswith("%"):
            return "comment", COMMENT_STANDING, "BibTeX comment line"
        if owner is not None:
            return owner.kind, READER_STANDING, owner.basis
        return "control", CONTROL_STANDING, "BibTeX material outside a recognized entry"
    if suffix == ".csv":
        if line_number == 1:
            return "control", CONTROL_STANDING, "CSV header record"
        if owner is not None:
            return owner.kind, READER_STANDING, owner.basis
        return "reader-facing-residual", READER_STANDING, "unowned CSV physical line"
    if owner is not None:
        return owner.kind, READER_STANDING, owner.basis
    return "reader-facing-residual", READER_STANDING, "unowned UTF-8 text line"


def unit_id_for(row: dict[str, str]) -> str:
    identity = {field: row[field] for field in INVENTORY_FIELDS[:14] if field != "unit_id"}
    return "HBU-" + sha256_bytes(json_compact(identity).encode("utf-8"))[:24]


def build_file_rows(file: PhysicalFile) -> list[dict[str, str]]:
    if file.lines is None:
        row = {
            "unit_id": "",
            "record_type": "binary_file",
            "path": file.path,
            "start_line": "",
            "end_line": "",
            "bytes": str(len(file.raw)),
            "sha256": sha256_bytes(file.raw),
            "unit_kind": "binary-file",
            "named_owner_key": "",
            "named_title": "",
            "stable_labels": "[]",
            "line_standing": BINARY_STANDING,
            "parser_basis": "whole file is not valid UTF-8",
            "parser_status": "parsed/unchecked",
            "mapping_status": "open/unmapped",
            "semantic_review_status": "pending",
            "source_authority_ids": "[]",
            "presentation_packet_ids": "[]",
            "register_obligation_ids": "[]",
        }
        row["unit_id"] = unit_id_for(row)
        return [row]
    if not file.lines:
        row = {
            "unit_id": "",
            "record_type": "empty_text_file",
            "path": file.path,
            "start_line": "",
            "end_line": "",
            "bytes": "0",
            "sha256": sha256_bytes(b""),
            "unit_kind": "empty-text-file",
            "named_owner_key": "",
            "named_title": "",
            "stable_labels": "[]",
            "line_standing": EMPTY_STANDING,
            "parser_basis": "valid UTF-8 file with no physical lines",
            "parser_status": "parsed/unchecked",
            "mapping_status": "open/unmapped",
            "semantic_review_status": "pending",
            "source_authority_ids": "[]",
            "presentation_packet_ids": "[]",
            "register_obligation_ids": "[]",
        }
        row["unit_id"] = unit_id_for(row)
        return [row]

    text_lines = tuple(line.decode("utf-8") for line in file.lines)
    suffix = PurePosixPath(file.path).suffix.lower()
    if suffix == ".tex":
        owners = tex_owners(file.path, text_lines)
    elif suffix == ".md":
        owners = markdown_owners(file.path, text_lines)
    elif suffix == ".bib":
        owners = bibliography_owners(file.path, text_lines)
    elif suffix == ".csv":
        owners = csv_owners(file.path, file.raw.decode("utf-8"))
    else:
        owners = []
    selected = select_owners(owners, len(text_lines))

    atoms: list[dict[str, object]] = []
    for index, (raw_line, line, owner) in enumerate(
        zip(file.lines, text_lines, selected, strict=True), start=1
    ):
        unit_kind, standing, basis = line_classification(suffix, index, line, owner)
        labels = owner.labels if owner is not None else labels_in_tex(line) if suffix == ".tex" else ()
        atoms.append(
            {
                "line": index,
                "raw": raw_line,
                "unit_kind": unit_kind,
                "standing": standing,
                "basis": basis,
                "owner_key": owner.key if owner is not None else "",
                "owner_title": owner.title if owner is not None else "",
                "labels": labels,
            }
        )

    rows: list[dict[str, str]] = []
    start_index = 0
    while start_index < len(atoms):
        atom = atoms[start_index]
        grouping_key = (
            atom["unit_kind"],
            atom["standing"],
            atom["basis"],
            atom["owner_key"],
            atom["owner_title"],
            atom["labels"],
        )
        end_index = start_index + 1
        while end_index < len(atoms):
            candidate = atoms[end_index]
            candidate_key = (
                candidate["unit_kind"],
                candidate["standing"],
                candidate["basis"],
                candidate["owner_key"],
                candidate["owner_title"],
                candidate["labels"],
            )
            if candidate_key != grouping_key:
                break
            end_index += 1
        interval_raw = b"".join(
            item["raw"] for item in atoms[start_index:end_index]  # type: ignore[arg-type]
        )
        row = {
            "unit_id": "",
            "record_type": "physical_interval",
            "path": file.path,
            "start_line": str(atoms[start_index]["line"]),
            "end_line": str(atoms[end_index - 1]["line"]),
            "bytes": str(len(interval_raw)),
            "sha256": sha256_bytes(interval_raw),
            "unit_kind": str(atom["unit_kind"]),
            "named_owner_key": str(atom["owner_key"]),
            "named_title": str(atom["owner_title"]),
            "stable_labels": json_compact(list(atom["labels"])),
            "line_standing": str(atom["standing"]),
            "parser_basis": str(atom["basis"]),
            "parser_status": "parsed/unchecked",
            "mapping_status": "open/unmapped",
            "semantic_review_status": "pending",
            "source_authority_ids": "[]",
            "presentation_packet_ids": "[]",
            "register_obligation_ids": "[]",
        }
        row["unit_id"] = unit_id_for(row)
        rows.append(row)
        start_index = end_index
    return rows


def validate_partition(rows: list[dict[str, str]], files: list[PhysicalFile]) -> None:
    if any(set(row) != set(INVENTORY_FIELDS) for row in rows):
        raise ValueError("unit inventory row has an unexpected field set")
    by_path: dict[str, list[dict[str, str]]] = {}
    seen_ids: set[str] = set()
    for row in rows:
        if row["unit_id"] in seen_ids:
            raise ValueError(f"duplicate handbook unit ID: {row['unit_id']}")
        seen_ids.add(row["unit_id"])
        if row["unit_id"] != unit_id_for(row):
            raise ValueError(f"stale handbook unit identity: {row['unit_id']}")
        by_path.setdefault(row["path"], []).append(row)
    if set(by_path) != {file.path for file in files}:
        raise ValueError("unit inventory file set differs from construction snapshot")

    for file in files:
        file_rows = by_path[file.path]
        if file.lines is None:
            if len(file_rows) != 1 or file_rows[0]["record_type"] != "binary_file":
                raise ValueError(f"binary file is not one exact whole-file row: {file.path}")
            row = file_rows[0]
            if row["start_line"] or row["end_line"]:
                raise ValueError(f"binary file row has a line range: {file.path}")
            if int(row["bytes"]) != len(file.raw) or row["sha256"] != sha256_bytes(file.raw):
                raise ValueError(f"binary whole-file identity differs: {file.path}")
            continue
        if not file.lines:
            if len(file_rows) != 1 or file_rows[0]["record_type"] != "empty_text_file":
                raise ValueError(f"empty text file is not one exact row: {file.path}")
            continue
        expected_line = 1
        for row in file_rows:
            if row["record_type"] != "physical_interval":
                raise ValueError(f"text file has a non-interval row: {file.path}")
            start = canonical_decimal(row["start_line"], "unit.start_line", minimum=1)
            end = canonical_decimal(row["end_line"], "unit.end_line", minimum=1)
            if start != expected_line:
                problem = "overlap" if start < expected_line else "gap"
                raise ValueError(f"physical-line partition {problem}: {file.path}:{start}")
            if end < start or end > len(file.lines):
                raise ValueError(f"invalid physical-line interval: {file.path}:{start}-{end}")
            raw = b"".join(file.lines[start - 1 : end])
            if int(row["bytes"]) != len(raw) or row["sha256"] != sha256_bytes(raw):
                raise ValueError(f"stale interval digest: {file.path}:{start}-{end}")
            expected_line = end + 1
        if expected_line != len(file.lines) + 1:
            raise ValueError(f"physical-line partition dropped trailing lines: {file.path}")


def build_inventory(
    snapshot_path: Path,
    physical_inventory_path: Path,
    root: Path,
    expected_snapshot_sha256: str | None = None,
) -> tuple[list[dict[str, str]], str]:
    files, snapshot_sha = load_physical_files(
        snapshot_path, physical_inventory_path, root, expected_snapshot_sha256
    )
    rows = [row for file in files for row in build_file_rows(file)]
    validate_partition(rows, files)
    return rows, snapshot_sha


def csv_bytes(rows: list[dict[str, str]], fields: tuple[str, ...]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def inventory_markdown(rows: list[dict[str, str]], snapshot_sha: str) -> bytes:
    paths = {row["path"] for row in rows}
    physical_lines = sum(
        int(row["end_line"]) - int(row["start_line"]) + 1
        for row in rows
        if row["record_type"] == "physical_interval"
    )
    kinds: dict[str, int] = {}
    for row in rows:
        kinds[row["unit_kind"]] = kinds.get(row["unit_kind"], 0) + 1
    kind_lines = [f"- `{kind}` intervals: {count:,}." for kind, count in sorted(kinds.items())]
    return (
        "\n".join(
            [
                "# Current handbook-unit inventory",
                "",
                "This generated artifact uses the existing contract wording \"handbook unit\"",
                "and the existing construction inventory's owed semantic inventory. The",
                "following five statements fix the administrative use at this location:",
                "",
                "- Necessity: the physical inventory cannot state which contiguous lines a",
                "  deterministic parser associated with a named construction or explicit",
                "  residual, control, comment, blank, empty, or binary interval.",
                "- Definition: this inventory is exactly the canonical CSV partition generated",
                "  from every file and physical-line row in the pinned construction records,",
                "  with one stable digest-derived ID per interval or exact whole-file row.",
                "- Standing: it is a metalinguistic parsing and accounting artifact, not a",
                "  logic, presentation, authority, semantic verdict, or completion claim.",
                "- Nonredundancy: the physical inventory proves byte and line presence; this",
                "  artifact adds only a deterministic interval partition and parser basis.",
                "- Use: the reverse projection keys reviewer-supplied provenance, packet, and",
                "  register links to these exact interval identities without changing this",
                "  immutable parser projection.",
                "",
                f"- Construction snapshot SHA-256: `{snapshot_sha}`.",
                f"- Snapshot files represented: {len(paths):,}.",
                f"- Physical lines partitioned exactly once: {physical_lines:,}.",
                f"- Inventory rows: {len(rows):,}.",
                *kind_lines,
                "- Parser status on every row: `parsed/unchecked`.",
                "- Mapping status on every row: `open/unmapped`.",
                "- Semantic-review status on every row: `pending`.",
                "",
                "`reader-facing candidate` and `nonprinting control candidate` are lexical",
                "parser classifications only. They do not establish the semantic standing or",
                "correctness of any line. The companion reverse ledger remains fail-closed",
                "until separately supplied review evidence is accepted.",
                "",
            ]
        )
    ).encode("utf-8")


def empty_review_document(snapshot_sha: str, inventory_sha: str) -> dict[str, object]:
    return {
        "schema_version": SCHEMA_VERSION,
        "construction_snapshot_sha256": snapshot_sha,
        "handbook_unit_inventory_sha256": inventory_sha,
        "records": [],
    }


def review_document_bytes(document: dict[str, object]) -> bytes:
    return (json.dumps(document, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def load_json_strict(path: Path) -> object:
    try:
        return json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=duplicate_rejecting_object,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, DuplicateJsonFieldError) as exc:
        raise ValueError(f"invalid reviewed-record JSON: {exc}") from exc


def exact_string_array(value: object, location: str) -> list[str]:
    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item or item != item.strip() for item in value
    ):
        raise ValueError(f"{location}: expected array of nonempty strings")
    if value != sorted(set(value)):
        raise ValueError(f"{location}: values must be unique and lexically sorted")
    return list(value)


def load_register_ids(path: Path) -> set[str]:
    if not path.is_file():
        return set()
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if "obligation_id" not in (reader.fieldnames or []):
            raise ValueError("register manifest lacks obligation_id")
        values = [row["obligation_id"] for row in reader]
    if len(values) != len(set(values)):
        raise ValueError("register manifest has duplicate obligation IDs")
    return set(values)


def load_source_authority_ids(root: Path) -> set[str]:
    result: set[str] = set()
    provenance_root = root / "spec/provenance"
    if not provenance_root.is_dir():
        return result
    for path in sorted(provenance_root.glob("*.json")):
        if path.name.startswith("reviewed-") or path.name.endswith(".schema.json"):
            continue
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            continue
        identifier = value.get("provenance_id") if isinstance(value, dict) else None
        if isinstance(identifier, str) and identifier:
            if identifier in result:
                raise ValueError(f"duplicate provenance ID: {identifier}")
            result.add(identifier)
    return result


def load_packet_statuses(root: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    if not root.is_dir():
        return result
    for path in sorted(root.rglob("*.json")):
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError(f"invalid presentation packet {path}: {exc}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"presentation packet root is not an object: {path}")
        identifier, status = value.get("packet_id"), value.get("overall_status")
        if not isinstance(identifier, str) or not identifier:
            raise ValueError(f"presentation packet lacks packet_id: {path}")
        if identifier in result:
            raise ValueError(f"duplicate presentation packet ID: {identifier}")
        result[identifier] = status if isinstance(status, str) else ""
    return result


def record_identity(row: dict[str, str]) -> dict[str, object]:
    result: dict[str, object] = {}
    for field in REVIEW_IDENTITY_FIELDS:
        value: object = row[field]
        if field in {"start_line", "end_line"}:
            value = int(row[field]) if row[field] else None
        elif field == "bytes":
            value = int(row[field])
        elif field == "stable_labels":
            value = json.loads(row[field])
        result[field] = value
    return result


def normalized_identity(value: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def evidence_array(
    value: object,
    verification: dict[str, str],
    root: Path,
    forbidden_paths: set[Path],
    location: str,
) -> list[dict[str, object]]:
    if not isinstance(value, list) or len(value) != len(VERIFICATION_FIELDS):
        raise ValueError(f"{location}: exactly six evidence records are required")
    result: list[dict[str, object]] = []
    categories: list[str] = []
    artifact_paths: list[Path] = []
    producer_keys: list[str] = []
    for index, untyped in enumerate(value):
        item_location = f"{location}[{index}]"
        if not isinstance(untyped, dict):
            raise ValueError(f"{item_location}: expected object")
        category = untyped.get("category")
        if not isinstance(category, str) or category not in VERIFICATION_FIELDS:
            raise ValueError(f"{item_location}.category: unknown evidence category")
        item = require_exact_fields(
            untyped,
            AI_EVIDENCE_FIELDS if category in AI_REVIEW_FIELDS else EVIDENCE_FIELDS,
            item_location,
        )
        categories.append(category)
        if item["recorded_result"] != verification[category] or item["recorded_result"] != "pass":
            raise ValueError(f"{item_location}: evidence result must match terminal pass")
        path_value, artifact = repository_path(root, item["artifact_path"], f"{item_location}.artifact_path")
        if not artifact.is_file():
            raise ValueError(f"{item_location}: evidence artifact does not exist")
        if artifact.resolve() in forbidden_paths:
            raise ValueError(f"{item_location}: governed inputs cannot evidence themselves")
        digest = item["sha256"]
        if not isinstance(digest, str) or SHA256_RE.fullmatch(digest) is None:
            raise ValueError(f"{item_location}.sha256: malformed digest")
        if sha256_bytes(artifact.read_bytes()) != digest:
            raise ValueError(f"{item_location}: stale evidence digest")
        producer = item["producer_identity"]
        scope = item["recorded_scope"]
        if not isinstance(producer, str) or not producer.strip() or producer != producer.strip():
            raise ValueError(f"{item_location}.producer_identity: expected nonempty string")
        if not isinstance(scope, str) or not scope.strip() or scope != scope.strip():
            raise ValueError(f"{item_location}.recorded_scope: expected nonempty string")
        artifact_paths.append(artifact.resolve())
        producer_keys.append(normalized_identity(producer))
        canonical_item: dict[str, object] = {
            "category": category,
            "recorded_result": "pass",
            "artifact_path": path_value,
            "sha256": digest,
            "producer_identity": producer,
            "recorded_scope": scope,
        }
        if category in AI_REVIEW_FIELDS:
            for field in ("model", "model_version", "instructions"):
                field_value = item[field]
                if (
                    not isinstance(field_value, str)
                    or not field_value.strip()
                    or field_value != field_value.strip()
                ):
                    raise ValueError(f"{item_location}.{field}: expected nonempty string")
                canonical_item[field] = field_value
            if item["other_review_outputs_consulted"] is not False:
                raise ValueError(
                    f"{item_location}.other_review_outputs_consulted: expected false"
                )
            canonical_item["other_review_outputs_consulted"] = False
            findings = item["findings"]
            if not isinstance(findings, list) or not findings:
                raise ValueError(f"{item_location}.findings: expected nonempty list")
            for finding_index, finding in enumerate(findings):
                if not isinstance(finding, str) or not finding.strip():
                    raise ValueError(
                        f"{item_location}.findings[{finding_index}]: "
                        "expected nonempty string"
                    )
            canonical_item["findings"] = findings
            consulted = item["consulted_authorities"]
            if not isinstance(consulted, list) or not consulted:
                raise ValueError(
                    f"{item_location}.consulted_authorities: expected nonempty list"
                )
            canonical_consulted: list[dict[str, str]] = []
            seen_consulted: set[tuple[str, str]] = set()
            for authority_index, untyped_authority in enumerate(consulted):
                authority_location = (
                    f"{item_location}.consulted_authorities[{authority_index}]"
                )
                authority = require_exact_fields(
                    untyped_authority,
                    CONSULTED_AUTHORITY_FIELDS,
                    authority_location,
                )
                authority_path, authority_file = repository_path(
                    root, authority["path"], f"{authority_location}.path"
                )
                locator = authority["locator"]
                if not isinstance(locator, str) or not locator.strip():
                    raise ValueError(
                        f"{authority_location}.locator: expected nonempty string"
                    )
                authority_digest = authority["sha256"]
                if (
                    not isinstance(authority_digest, str)
                    or SHA256_RE.fullmatch(authority_digest) is None
                ):
                    raise ValueError(f"{authority_location}.sha256: malformed digest")
                if not authority_file.is_file() or sha256_bytes(
                    authority_file.read_bytes()
                ) != authority_digest:
                    raise ValueError(f"{authority_location}: stale authority digest")
                key = (authority_path, locator)
                if key in seen_consulted:
                    raise ValueError(f"{authority_location}: duplicate authority")
                seen_consulted.add(key)
                canonical_consulted.append(
                    {"path": authority_path, "locator": locator, "sha256": authority_digest}
                )
            canonical_item["consulted_authorities"] = canonical_consulted
        result.append(canonical_item)
    if categories != list(VERIFICATION_FIELDS):
        raise ValueError(f"{location}: evidence categories must have canonical order")
    if len(set(artifact_paths)) != len(artifact_paths):
        raise ValueError(f"{location}: evidence artifacts must be distinct files")
    if len(set(producer_keys)) != len(producer_keys):
        raise ValueError(f"{location}: evidence producer identities must be distinct")
    return result


def apply_reviewed_records(
    rows: list[dict[str, str]],
    reviewed_path: Path,
    snapshot_sha: str,
    inventory_sha: str,
    root: Path,
    register_manifest: Path,
    presentation_root: Path,
) -> list[dict[str, str]]:
    if not reviewed_path.is_file():
        raise ValueError(f"reviewed-record input does not exist: {reviewed_path}")
    document = require_exact_fields(
        load_json_strict(reviewed_path),
        {
            "schema_version",
            "construction_snapshot_sha256",
            "handbook_unit_inventory_sha256",
            "records",
        },
        "reviewed-record document",
    )
    if document["schema_version"] != SCHEMA_VERSION or isinstance(document["schema_version"], bool):
        raise ValueError(f"reviewed-record document.schema_version must be {SCHEMA_VERSION}")
    if document["construction_snapshot_sha256"] != snapshot_sha:
        raise ValueError("reviewed-record document: construction snapshot digest drift")
    if document["handbook_unit_inventory_sha256"] != inventory_sha:
        raise ValueError("reviewed-record document: handbook-unit inventory digest drift")
    records = document["records"]
    if not isinstance(records, list):
        raise ValueError("reviewed-record document.records: expected array")

    by_id = {row["unit_id"]: row for row in rows}
    authority_ids = load_source_authority_ids(root)
    packet_statuses = load_packet_statuses(presentation_root)
    register_ids = load_register_ids(register_manifest)
    seen_ids: set[str] = set()
    overlays: dict[str, dict[str, str]] = {}
    forbidden = {
        reviewed_path.resolve(),
        (root / "spec/handbook-unit-inventory.csv").resolve(),
        (root / "spec/handbook-construction-snapshot.csv").resolve(),
        (root / "spec/handbook-construction-source-inventory.csv").resolve(),
    }

    for index, untyped in enumerate(records):
        location = f"reviewed-record document.records[{index}]"
        record = require_exact_fields(untyped, REVIEW_RECORD_FIELDS, location)
        unit_id = record["unit_id"]
        if not isinstance(unit_id, str) or unit_id not in by_id:
            raise ValueError(f"{location}: unknown handbook unit ID {unit_id!r}")
        if unit_id in seen_ids:
            raise ValueError(f"{location}: duplicate handbook unit ID {unit_id}")
        seen_ids.add(unit_id)
        base = by_id[unit_id]
        expected_identity = record_identity(base)
        for field, expected in expected_identity.items():
            if record[field] != expected or (
                field in {"start_line", "end_line", "bytes"}
                and isinstance(record[field], bool)
            ):
                raise ValueError(f"{location}.{field}: exact unit identity differs")
        if record["mapping_status"] != "mapped/reviewed":
            raise ValueError(f"{location}.mapping_status: terminal value required")
        expected_semantic = (
            "pass" if base["line_standing"] == READER_STANDING else "not-applicable"
        )
        if record["semantic_review_status"] != expected_semantic:
            raise ValueError(
                f"{location}.semantic_review_status: expected {expected_semantic!r}"
            )
        source_ids = exact_string_array(record["source_authority_ids"], f"{location}.source_authority_ids")
        packet_ids = exact_string_array(record["presentation_packet_ids"], f"{location}.presentation_packet_ids")
        obligation_ids = exact_string_array(record["register_obligation_ids"], f"{location}.register_obligation_ids")
        unknown_sources = sorted(set(source_ids) - authority_ids)
        if unknown_sources:
            raise ValueError(f"{location}: unknown source-authority IDs {unknown_sources}")
        unknown_packets = sorted(set(packet_ids) - set(packet_statuses))
        if unknown_packets:
            raise ValueError(f"{location}: unknown presentation-packet IDs {unknown_packets}")
        unverified_packets = sorted(
            identifier for identifier in packet_ids if packet_statuses[identifier] != "verified"
        )
        if unverified_packets:
            raise ValueError(f"{location}: presentation packets are not verified {unverified_packets}")
        unknown_obligations = sorted(set(obligation_ids) - register_ids)
        if unknown_obligations:
            raise ValueError(f"{location}: unknown register-obligation IDs {unknown_obligations}")
        if base["line_standing"] == READER_STANDING and not (source_ids or packet_ids):
            raise ValueError(f"{location}: reader-facing unit requires source or packet link")
        labels = json.loads(base["stable_labels"])
        if base["line_standing"] == READER_STANDING and not labels:
            raise ValueError(f"{location}: reader-facing unit lacks a stable label")

        verification = require_exact_fields(
            record["verification"], set(VERIFICATION_FIELDS), f"{location}.verification"
        )
        typed_verification: dict[str, str] = {}
        for category in VERIFICATION_FIELDS:
            if verification[category] != "pass":
                raise ValueError(f"{location}.verification.{category}: terminal pass required")
            typed_verification[category] = "pass"
        evidence = evidence_array(
            record["verification_evidence"],
            typed_verification,
            root,
            forbidden,
            f"{location}.verification_evidence",
        )
        canonical_record = json_compact(record)
        overlay = {
            "mapping_status": "mapped/reviewed",
            "semantic_review_status": expected_semantic,
            "source_authority_ids": json_compact(source_ids),
            "presentation_packet_ids": json_compact(packet_ids),
            "register_obligation_ids": json_compact(obligation_ids),
            "verification_evidence": json_compact(evidence),
            "review_record_sha256": sha256_bytes(canonical_record.encode("utf-8")),
        }
        for category in VERIFICATION_FIELDS:
            overlay[f"{category}_verification"] = "pass"
        overlays[unit_id] = overlay

    result: list[dict[str, str]] = []
    for base in rows:
        joined = dict(base)
        for category in VERIFICATION_FIELDS:
            joined[f"{category}_verification"] = "pending"
        joined["verification_evidence"] = "[]"
        joined["review_record_sha256"] = ""
        joined.update(overlays.get(base["unit_id"], {}))
        result.append(joined)
    return result


def reverse_markdown(
    rows: list[dict[str, str]], snapshot_sha: str, inventory_sha: str
) -> bytes:
    mapped = sum(row["mapping_status"] == "mapped/reviewed" for row in rows)
    semantic_pass = sum(row["semantic_review_status"] == "pass" for row in rows)
    return (
        "\n".join(
            [
                "# Current handbook-unit reverse ledger",
                "",
                "This generated projection joins optional reviewer-supplied records to the",
                "immutable parser inventory by exact stable unit ID. It does not alter the",
                "inventory and does not infer source identity or correctness from syntax.",
                "",
                f"- Construction snapshot SHA-256: `{snapshot_sha}`.",
                f"- Handbook-unit inventory SHA-256: `{inventory_sha}`.",
                f"- Joined unit rows: {len(rows):,}.",
                f"- Rows admitted as `mapped/reviewed`: {mapped:,}.",
                f"- Reader-facing rows with semantic review `pass`: {semantic_pass:,}.",
                f"- Rows retaining `open/unmapped`: {len(rows) - mapped:,}.",
                "",
                "An admitted row must repeat its complete parsed identity, resolve every",
                "source-authority, verified-presentation-packet, and register-obligation",
                "link, and supply separate passing source-fidelity AI, topic-specialist AI,",
                "adversarial-publication AI, static, build, and visual evidence.",
                "Evidence paths and normalized producer strings must be pairwise",
                "distinct. Those checks establish only that the recorded files and strings",
                "exist and match; they do not authenticate identities or prove that the",
                "recorded review was correctly performed.",
                "",
            ]
        )
    ).encode("utf-8")


def write_or_check(path: Path, raw: bytes, check: bool) -> None:
    if check:
        if not path.is_file() or path.read_bytes() != raw:
            raise ValueError(f"stale generated artifact: {path}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)


def default_snapshot_pin() -> str:
    import check_handbook_construction_snapshot as construction

    return construction.MANIFEST_SHA256


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    parser.add_argument("--snapshot", type=Path, default=DEFAULT_SNAPSHOT)
    parser.add_argument("--physical-inventory", type=Path, default=DEFAULT_PHYSICAL_INVENTORY)
    parser.add_argument("--inventory-csv", type=Path, default=DEFAULT_UNIT_CSV)
    parser.add_argument("--inventory-markdown", type=Path, default=DEFAULT_UNIT_MD)
    parser.add_argument("--reverse-csv", type=Path, default=DEFAULT_REVERSE_CSV)
    parser.add_argument("--reverse-markdown", type=Path, default=DEFAULT_REVERSE_MD)
    parser.add_argument("--reviewed-records", type=Path, default=DEFAULT_REVIEWED)
    parser.add_argument("--register-manifest", type=Path, default=DEFAULT_REGISTER_MANIFEST)
    parser.add_argument("--presentation-root", type=Path, default=DEFAULT_PRESENTATION_ROOT)
    parser.add_argument(
        "--expected-snapshot-sha256",
        default=None,
        help="exact snapshot pin; the repository checker's pin is used by default",
    )
    args = parser.parse_args(argv)

    try:
        pin = args.expected_snapshot_sha256 or default_snapshot_pin()
        rows, snapshot_sha = build_inventory(
            args.snapshot, args.physical_inventory, args.repository_root, pin
        )
        inventory_raw = csv_bytes(rows, INVENTORY_FIELDS)
        inventory_sha = sha256_bytes(inventory_raw)
        inventory_md_raw = inventory_markdown(rows, snapshot_sha)

        if args.write:
            if args.reviewed_records.is_file():
                existing = load_json_strict(args.reviewed_records)
                existing_object = require_exact_fields(
                    existing,
                    {
                        "schema_version",
                        "construction_snapshot_sha256",
                        "handbook_unit_inventory_sha256",
                        "records",
                    },
                    "reviewed-record document",
                )
                if existing_object["records"] == []:
                    args.reviewed_records.write_bytes(
                        review_document_bytes(empty_review_document(snapshot_sha, inventory_sha))
                    )
            else:
                args.reviewed_records.parent.mkdir(parents=True, exist_ok=True)
                args.reviewed_records.write_bytes(
                    review_document_bytes(empty_review_document(snapshot_sha, inventory_sha))
                )

        reverse_rows = apply_reviewed_records(
            rows,
            args.reviewed_records,
            snapshot_sha,
            inventory_sha,
            args.repository_root,
            args.register_manifest,
            args.presentation_root,
        )
        reverse_raw = csv_bytes(reverse_rows, REVERSE_FIELDS)
        reverse_md_raw = reverse_markdown(reverse_rows, snapshot_sha, inventory_sha)
        write_or_check(args.inventory_csv, inventory_raw, args.check)
        write_or_check(args.inventory_markdown, inventory_md_raw, args.check)
        write_or_check(args.reverse_csv, reverse_raw, args.check)
        write_or_check(args.reverse_markdown, reverse_md_raw, args.check)
    except (OSError, ValueError) as exc:
        print(f"handbook-unit reverse ledger: FAIL ({exc})")
        return 1

    action = "verified" if args.check else "wrote"
    mapped = sum(row["mapping_status"] == "mapped/reviewed" for row in reverse_rows)
    physical_lines = sum(
        int(row["end_line"]) - int(row["start_line"]) + 1
        for row in rows
        if row["record_type"] == "physical_interval"
    )
    print(
        f"{action} handbook-unit inventory/reverse ledger: {len(rows)} units, "
        f"{physical_lines} physical lines, {mapped} mapped/reviewed"
    )
    print(f"inventory SHA-256 {inventory_sha}")
    print("Parser standing is separate from semantic correctness and release status.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

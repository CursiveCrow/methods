#!/usr/bin/env python3
"""Patch and audit the edition-2026 fulfillment ledger."""

from __future__ import annotations

import argparse
import collections
import contextlib
import datetime as _dt
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parent.parent
EDITION_DIR = Path("spec/coverage/edition-2026")
LEDGER_DIR = EDITION_DIR / "current-fulfillment"
TOC_PATH = Path("spec/proposed-table-of-contents.json")
QUEUE_PATH = EDITION_DIR / "completion-work-queue.jsonl"
ASSESSMENTS_DIR = EDITION_DIR / "assessments"
RESIDUALS_PATH = EDITION_DIR / "unit-residuals.jsonl"
ACQUISITION_PATH = EDITION_DIR / "acquisition-requests.jsonl"
BLOCKERS_PATH = EDITION_DIR / "blockers.jsonl"

ALLOWED_STATUSES = {
    "authored_unreviewed",
    "partial",
    "missing",
    "unassessed",
}
STATUS_ORDER = {
    "unassessed": 0,
    "missing": 1,
    "partial": 2,
    "authored_unreviewed": 3,
}
EDITABLE_SET_FIELDS = {
    "status",
    "missing_pieces",
    "unassessed_scope",
}
# The tool owns these: observed_utc is always "now"; evidence is appended and
# the revision is written by apply itself.
AUTO_EDITABLE_FIELDS = {"observed_utc", "reader_evidence", "fulfillment_revision"}
PROPOSAL_KEYS = frozenset(
    {"section_id", "original_row_sha256", "set", "append_reader_evidence", "assessment_ids", "reason"}
)
# Environments whose first mandatory argument is a label (anchor search).
LABEL_ARG_ENVIRONMENTS = frozenset(
    {
        "hbtheorem",
        "hblemma",
        "hbcorollary",
        "hbdefinition",
        "hbconvention",
        "hbmethod",
        "hbexample",
        "hbwarning",
        "proofboundary",
        "annexitem",
        "systementry",
    }
)
ALL_EDITABLE_FIELDS = EDITABLE_SET_FIELDS | AUTO_EDITABLE_FIELDS
BLOCKER_PREFIXES = ("ACQ-", "MATH-", "POL-")
NON_ACCEPTANCE_SENTENCE = (
    "This report is bookkeeping evidence only; it is not independent source, "
    "proof, manuscript, or publication acceptance."
)
BASELINE_ROW_KEYS = frozenset(
    {
        "absence_evidence",
        "annex_read_evidence",
        "assessment_kind",
        "authored_scope",
        "authoring_scope_assessment",
        "chapter_id",
        "chapter_title",
        "fulfillment_basis",
        "fulfillment_revision",
        "independent_admission",
        "integration_qualification",
        "missing_pieces",
        "observed_utc",
        "part",
        "previous_authoring_scope_assessment",
        "reader_adoption_qualification",
        "reader_evidence",
        "reader_interface_candidates",
        "remaining_authoring_work",
        "schema_version",
        "section_id",
        "section_title",
        "source_facets",
        "source_note_evidence",
        "source_obligations_preserved",
        "status",
        "unassessed_scope",
    }
)
# Keys that hold identifiers rather than prose, skipped by the fused-number
# scan only at the evidence-entry level and at the revision levels.
EVIDENCE_ID_KEYS = frozenset(
    {"anchor", "assessment_ids", "components", "path", "route_state", "sha256"}
)
REVISION_ID_KEYS = frozenset(
    {"assessment_ids", "observed_utc", "patch_id", "row_sha256", "status"}
)
MISSING_PIECE_KINDS = frozenset(
    {"writable", "blocked_source", "blocked_math", "blocked_policy", "assessment_dispute"}
)
ASSESSMENT_ID_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]*")


class LedgerError(Exception):
    """Base class for user-visible ledger errors."""


class UsageError(LedgerError):
    """The command-line input or proposal shape is invalid."""


class Refusal(LedgerError):
    """A requested ledger change violates a rule."""


@dataclass
class LedgerRow:
    shard: Path
    index: int
    body: bytes
    newline: bytes
    obj: dict[str, Any]

    @property
    def row_sha256(self) -> str:
        return hashlib.sha256(self.body).hexdigest()


@dataclass
class LedgerState:
    rows: list[LedgerRow]
    by_section: dict[str, LedgerRow]
    duplicate_sections: dict[str, int]


@dataclass
class CheckResult:
    hard: list[str]
    warnings: list[str]
    metrics: dict[str, Any]

    @property
    def ok(self) -> bool:
        return not self.hard


def _rooted(root: Path, relative: Path | str) -> Path:
    return (root / relative).resolve()


def _rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return str(path)


def _now_utc() -> str:
    return _dt.datetime.now(_dt.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def _sha256_bytes(data: bytes, *, upper: bool = False) -> str:
    value = hashlib.sha256(data).hexdigest()
    return value.upper() if upper else value


def _sha256_file(path: Path, *, upper: bool = False) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    value = digest.hexdigest()
    return value.upper() if upper else value


def _line_parts(raw_line: bytes) -> tuple[bytes, bytes]:
    if raw_line.endswith(b"\r\n"):
        return raw_line[:-2], b"\r\n"
    if raw_line.endswith(b"\n"):
        return raw_line[:-1], b"\n"
    return raw_line, b""


def _read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return json.load(handle)


def _write_atomic_text(path: Path, text: str) -> None:
    temp_name = ""
    try:
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            newline="\n",
            dir=path.parent,
            delete=False,
        ) as handle:
            temp_name = handle.name
            handle.write(text)
        os.replace(temp_name, path)
    finally:
        if temp_name:
            try:
                os.unlink(temp_name)
            except FileNotFoundError:
                pass


def _write_atomic_bytes(path: Path, data: bytes) -> None:
    temp_name = ""
    try:
        with tempfile.NamedTemporaryFile("wb", dir=path.parent, delete=False) as handle:
            temp_name = handle.name
            handle.write(data)
        os.replace(temp_name, path)
    finally:
        if temp_name:
            try:
                os.unlink(temp_name)
            except FileNotFoundError:
                pass


def _json_compact(obj: dict[str, Any]) -> bytes:
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def _json_pretty(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=False)


def _ledger_shards(root: Path) -> list[Path]:
    directory = _rooted(root, LEDGER_DIR)
    return sorted(
        path
        for path in directory.glob("*.jsonl")
        if path.is_file()
        and not path.name.endswith("-receipt.jsonl")
        and not path.name.endswith("-history.jsonl")
    )


def load_ledger(root: Path = ROOT) -> LedgerState:
    rows: list[LedgerRow] = []
    counts: collections.Counter[str] = collections.Counter()
    by_section: dict[str, LedgerRow] = {}
    duplicate_sections: dict[str, int] = {}
    for shard in _ledger_shards(root):
        with shard.open("rb") as handle:
            raw_lines = handle.readlines()
        for index, raw_line in enumerate(raw_lines):
            body, newline = _line_parts(raw_line)
            if not body.strip():
                continue
            try:
                obj = json.loads(body.decode("utf-8-sig"))
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                raise UsageError(f"{_rel(shard, root)}:{index + 1}: malformed JSONL: {exc}") from exc
            if not isinstance(obj, dict):
                raise UsageError(f"{_rel(shard, root)}:{index + 1}: row is not a JSON object")
            row = LedgerRow(shard=shard, index=index, body=body, newline=newline, obj=obj)
            section_id = str(obj.get("section_id", ""))
            counts[section_id] += 1
            if section_id and section_id not in by_section:
                by_section[section_id] = row
            rows.append(row)
    duplicate_sections = {section: count for section, count in counts.items() if count > 1}
    return LedgerState(rows=rows, by_section=by_section, duplicate_sections=duplicate_sections)


def _toc_section_ids(root: Path) -> set[str]:
    data = _read_json(_rooted(root, TOC_PATH))
    ids: set[str] = set()
    for part in data.get("parts", []):
        for chapter in part.get("chapters", []):
            for section in chapter.get("numbered_sections", []):
                number = section.get("number")
                if number is not None:
                    ids.add(str(number))
    return ids


def _status_counts(rows: Iterable[LedgerRow]) -> dict[str, int]:
    counts: collections.Counter[str] = collections.Counter(
        str(row.obj.get("status", "")) for row in rows
    )
    return {status: counts.get(status, 0) for status in sorted(ALLOWED_STATUSES)}


def _by_part(rows: Iterable[LedgerRow]) -> list[dict[str, Any]]:
    by_part: dict[str, list[LedgerRow]] = collections.defaultdict(list)
    for row in rows:
        by_part[str(row.obj.get("part", ""))].append(row)
    result = []
    for part in sorted(by_part, key=_part_sort_key):
        part_rows = by_part[part]
        result.append(
            {
                "part": part,
                "rows": len(part_rows),
                "status_counts": _status_counts(part_rows),
            }
        )
    return result


def _part_sort_key(part: str) -> tuple[int, str]:
    match = re.fullmatch(r"P(\d+)", part)
    if match:
        return int(match.group(1)), part
    return 10_000, part


def _load_proposals(path: Path) -> list[dict[str, Any]]:
    proposals: list[dict[str, Any]] = []
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            for line_number, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                try:
                    item = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise UsageError(f"{path}:{line_number}: malformed proposal JSON: {exc}") from exc
                if not isinstance(item, dict):
                    raise UsageError(f"{path}:{line_number}: proposal is not an object")
                proposals.append(item)
    except OSError as exc:
        raise UsageError(f"cannot read proposals file {path}: {exc}") from exc
    return proposals


def _validate_unique_proposals(proposals: list[dict[str, Any]]) -> None:
    seen: set[str] = set()
    for index, proposal in enumerate(proposals, start=1):
        section_id = proposal.get("section_id")
        if not isinstance(section_id, str) or not section_id:
            raise UsageError(f"proposal {index}: section_id must be a non-empty string")
        if section_id in seen:
            raise Refusal(f"{section_id}: two proposals in one run")
        seen.add(section_id)


def _proposal_assessment_ids(proposal: dict[str, Any]) -> list[str]:
    raw = proposal.get("assessment_ids", [])
    if raw is None:
        raw = []
    if not isinstance(raw, list) or not all(isinstance(item, str) and item for item in raw):
        raise UsageError(f"{proposal.get('section_id', '<unknown>')}: assessment_ids must be a list of strings")
    return list(dict.fromkeys(raw))


def _proposal_reason(proposal: dict[str, Any]) -> str:
    reason = proposal.get("reason", "")
    if not isinstance(reason, str):
        raise UsageError(f"{proposal.get('section_id', '<unknown>')}: reason must be a string")
    return reason


def _set_payload(proposal: dict[str, Any]) -> dict[str, Any]:
    raw = proposal.get("set", {})
    if raw is None:
        raw = {}
    if not isinstance(raw, dict):
        raise UsageError(f"{proposal.get('section_id', '<unknown>')}: set must be an object")
    if "observed_utc" in raw:
        raise Refusal(
            f"{proposal.get('section_id', '<unknown>')}: observed_utc cannot be set; "
            "apply sets it to the current time"
        )
    extra = sorted(set(raw) - EDITABLE_SET_FIELDS)
    if extra:
        raise Refusal(
            f"{proposal.get('section_id', '<unknown>')}: immutable key(s) in set: "
            + ", ".join(extra)
        )
    return raw


def _append_evidence_payload(proposal: dict[str, Any]) -> list[dict[str, Any]]:
    raw = proposal.get("append_reader_evidence", [])
    if raw is None:
        raw = []
    if not isinstance(raw, list):
        raise UsageError(
            f"{proposal.get('section_id', '<unknown>')}: append_reader_evidence must be a list"
        )
    result: list[dict[str, Any]] = []
    for index, item in enumerate(raw, start=1):
        if not isinstance(item, dict):
            raise UsageError(
                f"{proposal.get('section_id', '<unknown>')}: evidence {index} is not an object"
            )
        result.append(dict(item))
    return result


def _evidence_assessment_ids(entries: list[dict[str, Any]]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for index, entry in enumerate(entries, start=1):
        raw = entry.get("assessment_ids", [])
        if raw is None:
            raw = []
        if not isinstance(raw, list) or not all(isinstance(item, str) and item for item in raw):
            raise UsageError(
                f"append_reader_evidence entry {index}: assessment_ids must be a list of strings"
            )
        for assessment_id in raw:
            if assessment_id not in seen:
                result.append(assessment_id)
                seen.add(assessment_id)
    return result


def _all_strings(value: Any) -> Iterable[str]:
    """Every string in a JSON value, dict keys included."""
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from _all_strings(item)
    elif isinstance(value, dict):
        for key, item in value.items():
            yield str(key)
            yield from _all_strings(item)


def _revision_strings(value: Any) -> Iterable[str]:
    if not isinstance(value, dict):
        yield from _all_strings(value)
        return
    for key, item in value.items():
        if key in REVISION_ID_KEYS:
            continue
        yield key
        if key in ("previous_observation", "prior_revision"):
            yield from _revision_strings(item)
        else:
            yield from _all_strings(item)


def _field_prose_strings(field: str, value: Any) -> Iterable[str]:
    """Strings of an editable field that the fused-number scan must see."""
    if field == "reader_evidence" and isinstance(value, list):
        for entry in value:
            if not isinstance(entry, dict):
                yield from _all_strings(entry)
                continue
            for key, item in entry.items():
                if key in EVIDENCE_ID_KEYS:
                    continue
                yield key
                yield from _all_strings(item)
    elif field == "fulfillment_revision":
        yield from _revision_strings(value)
    else:
        yield from _all_strings(value)


def _fused_hits(strings: Iterable[str]) -> list[str]:
    """Classes A-C of find_fused_spaces in plain-text mode (no masking)."""
    try:
        from find_fused_spaces import _scan
    except ImportError as exc:
        raise UsageError(f"cannot import tools/find_fused_spaces.py: {exc}") from exc
    hits: list[str] = []
    for text in strings:
        for hit in _scan(text, text, tex=False):
            if hit.cls in {"A", "B", "C"}:
                hits.append(f"{hit.match!r} at line {hit.line}, col {hit.col}")
    return hits


def _validate_no_fused_hits(section_id: str, field: str, strings: Iterable[str]) -> None:
    hits = _fused_hits(strings)
    if hits:
        raise Refusal(
            f"{section_id}: fused-number hit(s) in {field}: {', '.join(hits[:5])}"
        )


def _validate_missing_pieces(section_id: str, items: list[Any], known_refs: set[str]) -> None:
    for index, item in enumerate(items, start=1):
        label = f"{section_id}: missing_pieces item {index}"
        if isinstance(item, str):
            tag = MISSING_TAG_RE.match(item.strip())
            if tag is None or tag.group("kind") == "component":
                continue
            kind, ref = tag.group("kind"), tag.group("ref")
            # "[x](link) prose" is not a tag; "[kind:REF]", "[blocked_math]" are.
            if ref is None and "_" not in kind and kind not in MISSING_PIECE_KINDS:
                continue
            if kind not in MISSING_PIECE_KINDS:
                raise Refusal(f"{label}: unknown kind tag [{kind}]")
            if ref is None:
                raise Refusal(f"{label}: a kind tag must have the form [{kind}:REF]")
            if kind.startswith("blocked_") and not ref.startswith(BLOCKER_PREFIXES):
                raise Refusal(
                    f"{label}: {kind} requires a blocker ref starting with "
                    + ", ".join(BLOCKER_PREFIXES)
                )
            if ref.startswith(BLOCKER_PREFIXES) and ref not in known_refs:
                raise Refusal(f"{label}: blocker_ref {ref} does not resolve")
            continue
        if not isinstance(item, dict):
            raise Refusal(f"{label}: must be a string or an object")
        kind = item.get("kind")
        if not isinstance(kind, str) or kind not in MISSING_PIECE_KINDS:
            raise Refusal(f"{label}: invalid kind {kind!r}")
        if not isinstance(item.get("duty"), str) or not item["duty"].strip():
            raise Refusal(f"{label}: duty must be a non-empty string")
        component_ids = item.get("component_ids")
        if not isinstance(component_ids, list) or not all(
            isinstance(value, str) and value for value in component_ids
        ):
            raise Refusal(f"{label}: component_ids must be a list of strings")
        ref = item.get("blocker_ref")
        if ref is not None and not isinstance(ref, str):
            raise Refusal(f"{label}: blocker_ref must be a string or null")
        if "since" in item and not isinstance(item["since"], str):
            raise Refusal(f"{label}: since must be a string")
        if kind.startswith("blocked_"):
            if not ref or not ref.startswith(BLOCKER_PREFIXES):
                raise Refusal(
                    f"{label}: {kind} requires a blocker_ref starting with "
                    + ", ".join(BLOCKER_PREFIXES)
                )
        if ref and ref.startswith(BLOCKER_PREFIXES) and ref not in known_refs:
            raise Refusal(f"{label}: blocker_ref {ref} does not resolve")


def _validate_set_payload(
    section_id: str, payload: dict[str, Any], known_refs: set[str]
) -> None:
    if "status" in payload:
        status = payload["status"]
        if status not in ALLOWED_STATUSES:
            raise Refusal(f"{section_id}: invalid status {status!r}")
    for key in ("missing_pieces", "unassessed_scope"):
        if key in payload and not isinstance(payload[key], list):
            raise UsageError(f"{section_id}: {key} must be a list")
    if "missing_pieces" in payload:
        _validate_missing_pieces(section_id, payload["missing_pieces"], known_refs)
    _validate_no_fused_hits(section_id, "set strings", _all_strings(payload))


def _line_count(path: Path) -> int:
    data = path.read_bytes()
    if not data:
        return 0
    count = data.count(b"\n")
    if not data.endswith(b"\n"):
        count += 1
    return count


def _skip_spaces(text: str, index: int) -> int:
    while index < len(text) and text[index] in " \t\r\n":
        index += 1
    return index


def _balanced_bracket_end(text: str, index: int, open_char: str, close_char: str) -> int | None:
    index = _skip_spaces(text, index)
    if index >= len(text) or text[index] != open_char:
        return None
    depth = 1
    pos = index + 1
    while pos < len(text):
        char = text[pos]
        if char == "\\" and pos + 1 < len(text):
            pos += 2
            continue
        if char == open_char:
            depth += 1
        elif char == close_char:
            depth -= 1
            if depth == 0:
                return pos + 1
        pos += 1
    return None


def _first_braced_arg(text: str, index: int) -> tuple[str, int] | None:
    start = _skip_spaces(text, index)
    if start >= len(text) or text[start] != "{":
        return None
    end = _balanced_bracket_end(text, start, "{", "}")
    if end is None:
        return None
    return text[start + 1 : end - 1], end


def _tex_search_text(text: str) -> str:
    try:
        import check  # type: ignore
    except ImportError as exc:
        raise UsageError(f"cannot import tools/check.py for TeX anchor search: {exc}") from exc
    strip_comments = getattr(check, "strip_comments", None)
    strip_verbatims = getattr(check, "strip_verbatims", None)
    if not callable(strip_comments) or not callable(strip_verbatims):
        raise UsageError("tools/check.py lacks strip_comments/strip_verbatims")
    return strip_verbatims(strip_comments(text))


def _anchor_found(text: str, anchor: str) -> bool:
    text = _tex_search_text(text)
    label_re = re.compile(r"\\label\s*\{\s*" + re.escape(anchor) + r"\s*\}")
    if label_re.search(text):
        return True
    begin_re = re.compile(r"\\begin\s*\{\s*([A-Za-z*]+)\s*\}")
    for match in begin_re.finditer(text):
        if match.group(1) not in LABEL_ARG_ENVIRONMENTS:
            continue
        pos = match.end()
        while True:
            optional_end = _balanced_bracket_end(text, pos, "[", "]")
            if optional_end is None:
                break
            pos = optional_end
        first = _first_braced_arg(text, pos)
        if first is not None and first[0].strip() == anchor:
            return True
    return False


def _handbook_reached_files(root: Path) -> set[str]:
    handbook = _rooted(root, "handbook")
    if not handbook.is_dir():
        return set()
    bodies: dict[str, str] = {}
    for path in sorted(handbook.rglob("*.tex")):
        rel = path.relative_to(handbook).as_posix()
        try:
            # Undecodable bytes cannot hide an \input; keep the file in the closure.
            raw = path.read_text(encoding="utf-8-sig", errors="replace")
        except OSError:
            continue
        bodies[rel] = raw
    try:
        import check  # type: ignore

        stripped: dict[str, str] = {}
        strip_comments = getattr(check, "strip_comments", None)
        strip_verbatims = getattr(check, "strip_verbatims", None)
        for rel, raw in bodies.items():
            text = raw
            if callable(strip_comments):
                text = strip_comments(text)
            if callable(strip_verbatims):
                text = strip_verbatims(text)
            stripped[rel] = text
        reachability = getattr(check, "_hb_static_input_reachability", None)
        if callable(reachability):
            reached = reachability(stripped)
            if isinstance(reached, set):
                return set(str(item) for item in reached)
    except Exception:
        pass
    try:
        from symbol_registry import ReaderIndex  # type: ignore

        index = ReaderIndex(handbook)
        if getattr(index, "files", None):
            return set(index.files)
    except Exception:
        pass
    return set()


def _route_state(relative: str, reached: set[str]) -> str:
    """Repo-relative path -> route_state; only handbook/ files can be on route."""
    if relative.startswith("handbook/") and relative.removeprefix("handbook/") in reached:
        return "on_current_recursive_input_route"
    return "off_route"


def _normalize_repo_path(path_value: str, root: Path) -> tuple[Path, str]:
    raw = Path(path_value.replace("\\", "/"))
    if raw.is_absolute():
        resolved = raw.resolve()
    else:
        resolved = _rooted(root, raw)
    try:
        relative = resolved.relative_to(root.resolve()).as_posix()
    except ValueError as exc:
        raise Refusal(f"evidence path is outside the repository root: {path_value}") from exc
    return resolved, relative


def _prepare_evidence_entries(
    entries: list[dict[str, Any]], root: Path, reached: set[str]
) -> list[dict[str, Any]]:
    prepared: list[dict[str, Any]] = []
    for entry in entries:
        path_value = entry.get("path")
        anchor = entry.get("anchor")
        line_start = entry.get("line_start")
        line_end = entry.get("line_end")
        if not isinstance(path_value, str) or not path_value:
            raise UsageError("append_reader_evidence entry has invalid path")
        if not isinstance(anchor, str) or not anchor:
            raise UsageError(f"{path_value}: append_reader_evidence entry has invalid anchor")
        if (
            isinstance(line_start, bool)
            or isinstance(line_end, bool)
            or not isinstance(line_start, int)
            or not isinstance(line_end, int)
        ):
            raise UsageError(f"{path_value}: line_start and line_end must be integers")
        if line_start < 1 or line_end < line_start:
            raise Refusal(f"{path_value}: invalid line range {line_start}-{line_end}")
        path, relative = _normalize_repo_path(path_value, root)
        if not path.is_file():
            raise Refusal(f"{relative}: evidence path is missing")
        count = _line_count(path)
        if line_end > count:
            raise Refusal(f"{relative}: line_end {line_end} exceeds file length {count}")
        try:
            text = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError as exc:
            raise Refusal(f"{relative}: evidence file is not UTF-8: {exc}") from exc
        if not _anchor_found(text, anchor):
            raise Refusal(f"{relative}: anchor {anchor!r} not found")
        new_entry = dict(entry)
        new_entry["path"] = relative
        new_entry["sha256"] = _sha256_file(path, upper=True)
        new_entry["route_state"] = _route_state(relative, reached)
        prepared.append(new_entry)
    return prepared


def _assessment_files_for_ids(root: Path, assessment_ids: list[str]) -> dict[str, Path]:
    result: dict[str, Path] = {}
    base = _rooted(root, ASSESSMENTS_DIR)
    files_by_name: dict[str, list[Path]] = collections.defaultdict(list)
    if base.is_dir():
        for path in base.rglob("*.json"):
            if path.is_file():
                files_by_name[path.name].append(path)
    for assessment_id in assessment_ids:
        if not ASSESSMENT_ID_RE.fullmatch(assessment_id):
            raise Refusal(f"{assessment_id!r}: invalid assessment id")
        matches = files_by_name.get(f"{assessment_id}.json", [])
        if not matches:
            raise Refusal(
                f"{assessment_id}: assessment file not found under "
                f"{ASSESSMENTS_DIR.as_posix()}/**/{assessment_id}.json"
            )
        if len(matches) > 1:
            raise Refusal(f"{assessment_id}: assessment id resolves to multiple files")
        result[assessment_id] = matches[0]
    return result


def _load_assessments(root: Path, assessment_ids: list[str]) -> list[dict[str, Any]]:
    files = _assessment_files_for_ids(root, assessment_ids)
    assessments: list[dict[str, Any]] = []
    for assessment_id in assessment_ids:
        path = files[assessment_id]
        try:
            data = _read_json(path)
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise Refusal(f"{_rel(path, root)}: unreadable assessment: {exc}") from exc
        if not isinstance(data, dict):
            raise Refusal(f"{_rel(path, root)}: assessment is not an object")
        recorded_id = data.get("assessment_id")
        if not isinstance(recorded_id, str) or not recorded_id:
            raise Refusal(f"{_rel(path, root)}: assessment_id is missing")
        if recorded_id != assessment_id:
            raise Refusal(f"{_rel(path, root)}: assessment_id does not match {assessment_id}")
        assessments.append(data)
    return assessments


def _assessor_role_context(assessment: dict[str, Any]) -> tuple[str | None, str | None]:
    assessor = assessment.get("assessor")
    if not isinstance(assessor, dict):
        return None, None
    role = assessor.get("role")
    context_id = assessor.get("context_id")
    return (
        role if isinstance(role, str) else None,
        # casefolded: "ctx-A" and "CTX-a" name the same context
        context_id.strip().casefold() if isinstance(context_id, str) and context_id.strip() else None,
    )


def _has_first_confirm_pair(assessments: list[dict[str, Any]]) -> bool:
    """A role "first" and a role "confirm" assessment from different context_ids."""
    firsts = set()
    confirms = set()
    for assessment in assessments:
        role, context_id = _assessor_role_context(assessment)
        if context_id is None:
            continue
        if role == "first":
            firsts.add(context_id)
        elif role == "confirm":
            confirms.add(context_id)
    return any(first != confirm for first in firsts for confirm in confirms)


def _covered_component_ids(assessment: dict[str, Any]) -> set[str]:
    components = assessment.get("components")
    if not isinstance(components, list):
        return set()
    return {
        item["component_id"]
        for item in components
        if isinstance(item, dict)
        and item.get("verdict") == "covered"
        and isinstance(item.get("component_id"), str)
    }


def _evidence_components(entry: dict[str, Any]) -> list[str]:
    raw = entry.get("components", [])
    if raw is None:
        return []
    if not isinstance(raw, list) or not all(isinstance(item, str) and item for item in raw):
        raise UsageError(
            f"{entry.get('path', '<evidence>')}: evidence components must be a list of strings"
        )
    return raw


def _assessment_label(assessment: dict[str, Any]) -> str:
    assessment_id = assessment.get("assessment_id")
    return assessment_id if isinstance(assessment_id, str) and assessment_id else "<assessment>"


def _validate_assessment_section_ids(
    section_id: str, assessments: list[dict[str, Any]]
) -> None:
    for assessment in assessments:
        label = _assessment_label(assessment)
        if assessment.get("section_id") != section_id:
            raise Refusal(f"{label}: section_id does not match {section_id}")


def _validate_assessment_inputs_current(root: Path, assessment: dict[str, Any]) -> set[str]:
    label = _assessment_label(assessment)
    inputs = assessment.get("inputs")
    if not isinstance(inputs, dict):
        raise Refusal(f"{label}: inputs must be an object")
    tex_inputs = inputs.get("tex")
    if not isinstance(tex_inputs, list):
        raise Refusal(f"{label}: inputs.tex must be a list")
    if not tex_inputs:
        raise Refusal(f"{label}: inputs.tex must be a non-empty list")
    input_paths: set[str] = set()
    for item in tex_inputs:
        if not isinstance(item, dict):
            raise Refusal(f"{label}: inputs.tex item is not an object")
        path_value = item.get("path")
        recorded = item.get("sha256")
        if not isinstance(path_value, str) or not isinstance(recorded, str):
            raise Refusal(f"{label}: inputs.tex path/sha256 missing")
        path, relative = _normalize_repo_path(path_value, root)
        if not path.is_file():
            raise Refusal(f"{relative}: assessment input path is missing")
        actual = _sha256_file(path, upper=True)
        if actual.lower() != recorded.lower():
            raise Refusal(f"{label}: input {relative} sha256 is stale")
        input_paths.add(relative)
    return input_paths


def _live_on_route_evidence_paths(
    root: Path, evidence: Any, reached: set[str]
) -> set[str]:
    result: set[str] = set()
    for item in _latest_evidence_entries(evidence):
        path_value = item.get("path")
        recorded = item.get("sha256")
        if not isinstance(path_value, str) or not isinstance(recorded, str):
            continue
        try:
            path, relative = _normalize_repo_path(path_value, root)
        except Refusal:
            continue
        if not path.is_file():
            continue
        actual = _sha256_file(path, upper=True)
        if actual.lower() != recorded.lower():
            continue
        if _route_state(relative, reached) == "on_current_recursive_input_route":
            result.add(relative)
    return result


def _latest_evidence_entries(evidence: Any) -> list[dict[str, Any]]:
    if not isinstance(evidence, list):
        return []
    latest: dict[tuple[str, str], dict[str, Any]] = {}
    unkeyed: list[dict[str, Any]] = []
    for item in evidence:
        if not isinstance(item, dict):
            continue
        path_value = item.get("path")
        anchor = item.get("anchor")
        if isinstance(path_value, str) and isinstance(anchor, str):
            latest[(path_value, anchor)] = item
        else:
            unkeyed.append(item)
    return list(latest.values()) + unkeyed


def _au_shape_ok(row: dict[str, Any]) -> bool:
    evidence = row.get("reader_evidence")
    return (
        row.get("missing_pieces") == []
        and row.get("unassessed_scope") == []
        and isinstance(evidence, list)
        and bool(evidence)
    )


def _claimed_components(row: dict[str, Any]) -> set[str]:
    """Components claimed by a row's latest evidence entry per (path, anchor)."""
    claims: set[str] = set()
    for entry in _latest_evidence_entries(row.get("reader_evidence", [])):
        raw = entry.get("components", [])
        if isinstance(raw, list):
            claims.update(item for item in raw if isinstance(item, str) and item)
    return claims


def _is_upgrade(old_row: dict[str, Any], new_row: dict[str, Any]) -> bool:
    """The upgrade rule applies to any change that ends in an AU row, unless the
    old row was already a well-formed AU row and the change claims no component
    that row did not already claim (I7 counts AU claims as covered)."""
    if new_row.get("status") != "authored_unreviewed":
        return False
    if old_row.get("status") != "authored_unreviewed" or not _au_shape_ok(old_row):
        return True
    return not _claimed_components(new_row) <= _claimed_components(old_row)


def _validate_verdicts_covered(assessment: dict[str, Any]) -> None:
    label = _assessment_label(assessment)
    components = assessment.get("components")
    if not isinstance(components, list) or not components:
        raise Refusal(f"{label}: components must be a non-empty list")
    duties = assessment.get("duties", [])
    if not isinstance(duties, list):
        raise Refusal(f"{label}: duties must be a list")
    for kind, items in (("component", components), ("duty", duties)):
        for item in items:
            if not isinstance(item, dict) or item.get("verdict") != "covered":
                raise Refusal(f"{label}: every {kind} verdict must be covered")


def _validate_upgrade(
    root: Path,
    section_id: str,
    new_row: dict[str, Any],
    assessment_ids: list[str],
    assessments: list[dict[str, Any]],
    reached: set[str],
) -> None:
    if len(set(assessment_ids)) < 2:
        raise Refusal(f"{section_id}: authored_unreviewed upgrade requires at least two assessments")
    if not _has_first_confirm_pair(assessments):
        raise Refusal(
            f"{section_id}: authored_unreviewed upgrade requires a role first and a role "
            "confirm assessment with different assessor.context_id values"
        )
    _validate_assessment_section_ids(section_id, assessments)
    live_evidence_paths = _live_on_route_evidence_paths(
        root,
        new_row.get("reader_evidence", []),
        reached,
    )
    if not live_evidence_paths:
        raise Refusal(f"{section_id}: authored_unreviewed upgrade requires at least one live on-route evidence path")
    for assessment in assessments:
        label = _assessment_label(assessment)
        _validate_verdicts_covered(assessment)
        input_paths = _validate_assessment_inputs_current(root, assessment)
        if input_paths.isdisjoint(live_evidence_paths):
            raise Refusal(
                f"{label}: inputs.tex does not include a live on-route evidence path"
            )
    if new_row.get("missing_pieces") != [] or new_row.get("unassessed_scope") != []:
        raise Refusal(
            f"{section_id}: authored_unreviewed upgrade requires empty missing_pieces and unassessed_scope"
        )
    # Every component the AU row will claim (I7 counts them) must be covered in
    # every cited assessment.
    for entry in _latest_evidence_entries(new_row.get("reader_evidence", [])):
        for component in _evidence_components(entry):
            for assessment in assessments:
                if component not in _covered_component_ids(assessment):
                    raise Refusal(
                        f"{section_id}: evidence component {component} is not covered "
                        f"in assessment {_assessment_label(assessment)}"
                    )


def _validate_appended_components(
    section_id: str,
    old_row: dict[str, Any],
    append_entries: list[dict[str, Any]],
    proposal_assessment_ids: list[str],
    assessments_by_id: dict[str, dict[str, Any]],
) -> None:
    """Appended evidence may claim only components a cited assessment covers, or,
    without proposal-level assessment ids, only components that entry's key
    already claimed. Entry-level ids alone authorize nothing: a lead: refresh
    may only keep or narrow existing claims."""
    existing = {
        (entry.get("path"), entry.get("anchor")): entry
        for entry in _latest_evidence_entries(old_row.get("reader_evidence", []))
    }
    for entry in append_entries:
        components = _evidence_components(entry)
        cited = (
            list(dict.fromkeys(_evidence_assessment_ids([entry]) + proposal_assessment_ids))
            if proposal_assessment_ids
            else []
        )
        if cited:
            covered: set[str] = set()
            for assessment_id in cited:
                covered |= _covered_component_ids(assessments_by_id[assessment_id])
            unassessed = [item for item in components if item not in covered]
            if unassessed:
                raise Refusal(
                    f"{section_id}: evidence component(s) {', '.join(unassessed)} are not "
                    "covered in any cited assessment"
                )
            continue
        previous = existing.get((entry["path"], entry["anchor"]))
        claimed = set(_evidence_components(previous)) if previous else set()
        new_claims = [item for item in components if item not in claimed]
        if new_claims:
            raise Refusal(
                f"{section_id}: evidence without assessment ids may not claim new "
                f"component(s) {', '.join(new_claims)} for {entry['path']}#{entry['anchor']}"
            )


def _validate_assessment_or_lead_reason(
    section_id: str,
    old_row: dict[str, Any],
    new_row: dict[str, Any],
    set_payload: dict[str, Any],
    assessment_ids: list[str],
    reason: str,
) -> None:
    if assessment_ids:
        return
    if not reason.startswith("lead:"):
        raise Refusal(
            f"{section_id}: change requires at least one assessment id or a lead: reason"
        )
    if not reason.removeprefix("lead:").strip():
        raise Refusal(f"{section_id}: lead: reason requires text after the prefix")
    old_status = str(old_row.get("status", ""))
    if str(new_row.get("status", old_status)) != old_status:
        raise Refusal(
            f"{section_id}: lead: reason without assessment ids is only for "
            "unchanged-status evidence refreshes"
        )
    if set_payload:
        raise Refusal(
            f"{section_id}: lead: reason without assessment ids may not use set; "
            f"refused set key(s): {', '.join(sorted(set_payload))}"
        )


def _validate_row_shape_for_status(section_id: str, row: dict[str, Any]) -> None:
    status = str(row.get("status", ""))
    if status == "authored_unreviewed":
        if not _au_shape_ok(row):
            raise Refusal(
                f"{section_id}: authored_unreviewed requires empty residual scope and non-empty evidence"
            )
    elif status in {"partial", "missing"}:
        if not row.get("missing_pieces"):
            raise Refusal(f"{section_id}: {status} requires non-empty missing_pieces")
    elif status == "unassessed" and not row.get("unassessed_scope"):
        raise Refusal(f"{section_id}: unassessed requires non-empty unassessed_scope")


def _patch_id(section_id: str, observed_utc: str) -> str:
    safe_section = re.sub(r"[^A-Za-z0-9_.-]+", "-", section_id)
    stamp = observed_utc.replace("-", "").replace(":", "")
    return f"ledger_patch-{stamp}-{safe_section}"


def _apply_one_proposal(
    root: Path,
    row: LedgerRow,
    proposal: dict[str, Any],
    reached: set[str],
    observed_utc: str,
    known_refs: set[str],
) -> dict[str, Any]:
    section_id = str(row.obj.get("section_id", ""))
    unknown = sorted(set(proposal) - PROPOSAL_KEYS)
    if unknown:
        raise Refusal(f"{section_id}: unknown proposal key(s): {', '.join(unknown)}")
    original_pin = proposal.get("original_row_sha256")
    if not isinstance(original_pin, str) or not original_pin:
        raise UsageError(f"{section_id}: original_row_sha256 must be a non-empty string")
    if original_pin.lower() != row.row_sha256.lower():
        raise Refusal(
            f"{section_id}: pin mismatch (proposal {original_pin}, current {row.row_sha256})"
        )
    set_payload = _set_payload(proposal)
    _validate_set_payload(section_id, set_payload, known_refs)
    assessment_ids = _proposal_assessment_ids(proposal)
    reason = _proposal_reason(proposal)
    _validate_no_fused_hits(section_id, "reason", [reason])
    append_payload = _append_evidence_payload(proposal)
    _validate_no_fused_hits(
        section_id,
        "append_reader_evidence",
        _field_prose_strings("reader_evidence", append_payload),
    )
    cited_assessment_ids = list(
        dict.fromkeys(assessment_ids + _evidence_assessment_ids(append_payload))
    )
    cited_assessments = (
        _load_assessments(root, cited_assessment_ids) if cited_assessment_ids else []
    )
    _validate_assessment_section_ids(section_id, cited_assessments)
    assessments_by_id = dict(zip(cited_assessment_ids, cited_assessments))
    assessments = [assessments_by_id[assessment_id] for assessment_id in assessment_ids]
    append_entries = _prepare_evidence_entries(append_payload, root, reached)

    new_row = json.loads(json.dumps(row.obj, ensure_ascii=False))
    for key, value in set_payload.items():
        if key in ("reader_evidence", "fulfillment_revision"):
            raise Refusal(f"{section_id}: {key} cannot be set directly")
        new_row[key] = value
    if append_entries:
        old_evidence = new_row.get("reader_evidence", [])
        if not isinstance(old_evidence, list):
            raise Refusal(f"{section_id}: existing reader_evidence is not a list")
        new_row["reader_evidence"] = old_evidence + append_entries
    old_status = str(row.obj.get("status", ""))
    new_status = str(new_row.get("status", old_status))
    if new_status not in ALLOWED_STATUSES:
        raise Refusal(f"{section_id}: invalid status {new_status!r}")
    if _is_upgrade(row.obj, new_row):
        _validate_upgrade(root, section_id, new_row, assessment_ids, assessments, reached)
    _validate_appended_components(
        section_id, row.obj, append_entries, assessment_ids, assessments_by_id
    )
    _validate_assessment_or_lead_reason(
        section_id,
        row.obj,
        new_row,
        set_payload,
        assessment_ids,
        reason,
    )
    _validate_row_shape_for_status(section_id, new_row)
    new_row["observed_utc"] = observed_utc
    new_row["fulfillment_revision"] = {
        "reason": reason,
        "patch_id": _patch_id(section_id, observed_utc),
        "assessment_ids": assessment_ids,
        "previous_observation": {
            "status": row.obj.get("status"),
            "missing_pieces": row.obj.get("missing_pieces"),
            "unassessed_scope": row.obj.get("unassessed_scope"),
            "observed_utc": row.obj.get("observed_utc"),
            "row_sha256": row.row_sha256,
            "prior_revision": row.obj.get("fulfillment_revision"),
        },
    }
    for key, value in row.obj.items():
        if key not in ALL_EDITABLE_FIELDS and new_row.get(key) != value:
            raise Refusal(f"{section_id}: immutable key {key!r} would change")
    return new_row


def _old_new_table(changes: list[tuple[LedgerRow, dict[str, Any]]], root: Path) -> str:
    lines = ["section_id | shard | old_status | new_status | old_sha256 | new_sha256"]
    lines.append("--- | --- | --- | --- | --- | ---")
    for row, new_obj in changes:
        new_body = _json_compact(new_obj)
        lines.append(
            " | ".join(
                [
                    str(row.obj.get("section_id", "")),
                    _rel(row.shard, root),
                    str(row.obj.get("status", "")),
                    str(new_obj.get("status", "")),
                    row.row_sha256,
                    _sha256_bytes(new_body),
                ]
            )
        )
    return "\n".join(lines)


def _rewrite_shards(
    changes: list[tuple[LedgerRow, dict[str, Any]]], root: Path, observed_utc: str
) -> None:
    by_shard: dict[Path, dict[int, tuple[LedgerRow, bytes]]] = collections.defaultdict(dict)
    for row, new_obj in changes:
        by_shard[row.shard][row.index] = (
            row,
            _json_compact(new_obj) + (row.newline or b"\n"),
        )
    for shard in by_shard:
        _read_receipt(_receipt_path_for_shard(shard), root)  # refuse before any write
    for shard, replacements in by_shard.items():
        with shard.open("rb") as handle:
            raw_lines = handle.readlines()
        for index, (row, replacement) in replacements.items():
            if index >= len(raw_lines):
                raise Refusal(f"{_rel(shard, root)}:{index + 1}: target line disappeared before write")
            current_body, _current_newline = _line_parts(raw_lines[index])
            current_hash = _sha256_bytes(current_body)
            if current_hash.lower() != row.row_sha256.lower():
                raise Refusal(
                    f"{_rel(shard, root)}:{index + 1}: line changed since pin "
                    f"(expected {row.row_sha256}, current {current_hash})"
                )
            raw_lines[index] = replacement
        _write_atomic_bytes(shard, b"".join(raw_lines))
        _refresh_receipt(root, shard, observed_utc)


def _receipt_path_for_shard(shard: Path) -> Path:
    return shard.with_name(f"{shard.stem}-receipt.json")


def _top_level_json_members(text: str) -> tuple[list[tuple[str, int, int, int]], int]:
    """Parse a JSON object's top-level members as (key, key_start, value_start,
    value_end) offsets; also return the offset of the closing brace."""
    decoder = json.JSONDecoder()
    length = len(text)

    def skip_ws(position: int) -> int:
        while position < length and text[position] in " \t\r\n":
            position += 1
        return position

    pos = skip_ws(0)
    if pos >= length or text[pos] != "{":
        raise ValueError("receipt is not a JSON object")
    pos += 1
    members: list[tuple[str, int, int, int]] = []
    while True:
        pos = skip_ws(pos)
        if pos < length and text[pos] == "}" and not members:
            return members, pos
        key_start = pos
        key, pos = decoder.raw_decode(text, pos)
        if not isinstance(key, str):
            raise ValueError("top-level JSON object key is not a string")
        pos = skip_ws(pos)
        if pos >= length or text[pos] != ":":
            raise ValueError("missing colon after top-level key")
        pos = skip_ws(pos + 1)
        value_start = pos
        _value, pos = decoder.raw_decode(text, pos)
        members.append((key, key_start, value_start, pos))
        pos = skip_ws(pos)
        if pos < length and text[pos] == ",":
            pos += 1
            continue
        if pos < length and text[pos] == "}":
            return members, pos
        raise ValueError("missing comma or closing brace in receipt")


def _splice_receipt_text(
    original: str,
    current: dict[str, Any],
    history: list[Any] | None,
) -> str:
    """Replace only the value spans of `current` (and `history`); every other
    byte of the receipt is copied verbatim. Absent keys go before the final }."""
    members, close = _top_level_json_members(original)
    indent = "  "
    if members:
        line_start = original.rfind("\n", 0, members[0][1]) + 1
        indent = original[line_start : members[0][1]]
        if indent.strip():  # first key shares its line with "{": compact receipt
            indent = ""

    def render(value: Any) -> str:
        return json.dumps(value, ensure_ascii=False, indent=2).replace("\n", "\n" + indent)

    values: dict[str, Any] = {"current": current}
    if history is not None:
        values["history"] = history
    edits: list[tuple[int, int, str]] = []
    present: set[str] = set()
    for key, _key_start, value_start, value_end in members:
        if key in values:
            edits.append((value_start, value_end, render(values[key])))
            present.add(key)
    absent = [key for key in ("history", "current") if key in values and key not in present]
    if absent:
        insertion = ",".join(
            "\n" + indent + json.dumps(key) + ": " + render(values[key]) for key in absent
        )
        if members:
            edits.append((members[-1][3], members[-1][3], "," + insertion))
        else:
            edits.append((close, close, insertion + "\n"))
    text = original
    for start, end, replacement in sorted(edits, reverse=True):
        text = text[:start] + replacement + text[end:]
    return text


def _read_receipt(receipt_path: Path, root: Path) -> tuple[str, dict[str, Any]] | None:
    """Return (text, parsed object) of an existing receipt, refusing anything
    that cannot be spliced safely."""
    if not receipt_path.exists():
        return None
    try:
        text = receipt_path.read_text(encoding="utf-8-sig", newline="")
        data = json.loads(text)
        _top_level_json_members(text)
    except (OSError, UnicodeDecodeError, ValueError) as exc:
        raise Refusal(f"{_rel(receipt_path, root)}: receipt cannot be refreshed: {exc}") from exc
    if not isinstance(data, dict):
        raise Refusal(f"{_rel(receipt_path, root)}: receipt is not a JSON object")
    if "history" in data and not isinstance(data["history"], list):
        raise Refusal(f"{_rel(receipt_path, root)}: receipt history is not a list")
    return text, data


def _refresh_receipt(root: Path, shard: Path, observed_utc: str) -> None:
    receipt_path = _receipt_path_for_shard(shard)
    existing = _read_receipt(receipt_path, root)
    original_text, data = existing if existing is not None else (None, {})
    state = load_ledger(root)
    shard_rows = [row for row in state.rows if row.shard == shard]
    current = {
        "ledger_sha256": _sha256_file(shard),
        "rows": len(shard_rows),
        "unique_section_ids": len({str(row.obj.get("section_id", "")) for row in shard_rows}),
        "status_counts": _status_counts(shard_rows),
        "by_part": _by_part(shard_rows),
        "observed_utc": observed_utc,
    }
    old_current = data.get("current")
    history_for_write: list[Any] | None = None
    if old_current is not None:
        history_for_write = data.get("history", []) + [old_current]
    if original_text is None:
        text = _json_pretty({"current": current}) + "\n"
    else:
        text = _splice_receipt_text(original_text, current, history_for_write)
    _write_atomic_text(receipt_path, text)


def apply_proposals(root: Path, proposals_path: Path, *, apply: bool) -> int:
    proposals = _load_proposals(proposals_path)
    _validate_unique_proposals(proposals)
    state = load_ledger(root)
    if state.duplicate_sections:
        raise Refusal(f"ledger has duplicate section ids: {state.duplicate_sections}")
    reached = _handbook_reached_files(root)
    known_refs = _load_blocker_refs(root)
    observed_utc = _now_utc()
    changes: list[tuple[LedgerRow, dict[str, Any]]] = []
    for proposal in proposals:
        section_id = str(proposal["section_id"])
        row = state.by_section.get(section_id)
        if row is None:
            raise Refusal(f"{section_id}: section_id not found in ledger")
        new_obj = _apply_one_proposal(root, row, proposal, reached, observed_utc, known_refs)
        changes.append((row, new_obj))
    if not changes:
        print("No proposals.")
        return 0
    print(_old_new_table(changes, root))
    if apply:
        _rewrite_shards(changes, root, observed_utc)
        print(f"applied {len(changes)} proposal(s)")
    else:
        print("dry run: no files written")
    return 0


def _evidence_sha_stale(root: Path, evidence: dict[str, Any]) -> bool:
    path_value = evidence.get("path")
    recorded = evidence.get("sha256")
    if not isinstance(path_value, str) or not isinstance(recorded, str):
        return True
    try:
        path, _relative = _normalize_repo_path(path_value, root)
    except Refusal:
        return True
    if not path.is_file():
        return True
    return _sha256_file(path).lower() != recorded.lower()


def _au_stale_count(root: Path, rows: Iterable[LedgerRow]) -> int:
    count = 0
    for row in rows:
        if row.obj.get("status") != "authored_unreviewed":
            continue
        evidence = row.obj.get("reader_evidence", [])
        if not isinstance(evidence, list):
            count += 1
            continue
        if any(_evidence_sha_stale(root, item) for item in _latest_evidence_entries(evidence)):
            count += 1
    return count


def _collect_au_evidence_components(rows: Iterable[LedgerRow]) -> set[str]:
    components: set[str] = set()
    for row in rows:
        if row.obj.get("status") != "authored_unreviewed":
            continue
        # A later entry for the same (path, anchor) supersedes the earlier claim.
        components |= _claimed_components(row.obj)
    return components


COMPONENT_TAG_RE = re.compile(r"\[component:([^\]\s]+)\]")
# A leading [word] or [word:REF] tag; only [kind:REF] with a known kind classifies.
MISSING_TAG_RE = re.compile(r"^\[(?P<kind>[A-Za-z_]+)(?::(?P<ref>[^\]\s]+))?\]")


def _missing_item_kind_and_ref(item: Any) -> tuple[str, str | None]:
    if isinstance(item, dict):
        kind = item.get("kind")
        ref = item.get("blocker_ref")
        return (
            kind if isinstance(kind, str) and kind else "unclassified",
            ref if isinstance(ref, str) and ref else None,
        )
    if isinstance(item, str):
        match = MISSING_TAG_RE.match(item.strip())
        if match and match.group("kind") in MISSING_PIECE_KINDS and match.group("ref"):
            return match.group("kind"), match.group("ref")
    return "unclassified", None


def _collect_open_missing_components(rows: Iterable[LedgerRow]) -> set[str]:
    components: set[str] = set()
    for row in rows:
        if row.obj.get("status") == "authored_unreviewed":
            continue
        for item in row.obj.get("missing_pieces", []):
            if isinstance(item, dict):
                raw = item.get("component_ids", [])
                if isinstance(raw, list):
                    components.update(str(value) for value in raw if isinstance(value, str) and value)
                duty = item.get("duty")
                if isinstance(duty, str):
                    components.update(COMPONENT_TAG_RE.findall(duty))
            elif isinstance(item, str):
                components.update(COMPONENT_TAG_RE.findall(item))
    return components


def _residual_component_ids(root: Path) -> set[str]:
    path = _rooted(root, RESIDUALS_PATH)
    if not path.is_file():
        return set()
    result: set[str] = set()
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        for line in handle:
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(item, dict):
                continue
            for key in ("component_id", "component_ids"):
                value = item.get(key)
                if isinstance(value, str):
                    result.add(value)
                elif isinstance(value, list):
                    result.update(str(part) for part in value if isinstance(part, str) and part)
    return result


def _component_ids_from_unit(unit: dict[str, Any]) -> list[str]:
    result: list[str] = []
    raw = unit.get("required_components", [])
    if isinstance(raw, list):
        for item in raw:
            if isinstance(item, dict) and isinstance(item.get("component_id"), str):
                result.append(item["component_id"])
    return result


def _duty_conservation_unaccounted(root: Path, rows: Iterable[LedgerRow]) -> dict[str, int]:
    accounted = (
        _collect_au_evidence_components(rows)
        | _collect_open_missing_components(rows)
        | _residual_component_ids(root)
    )
    queue = _rooted(root, QUEUE_PATH)
    unaccounted: dict[str, int] = {}
    if not queue.is_file():
        return unaccounted
    with queue.open("r", encoding="utf-8-sig", newline="") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                unit = json.loads(line)
            except json.JSONDecodeError:
                unaccounted[f"<malformed line {line_number}>"] = 1
                continue
            if not isinstance(unit, dict):
                continue
            missing = [component for component in _component_ids_from_unit(unit) if component not in accounted]
            if missing:
                unit_id = str(unit.get("unit_id", f"<line {line_number}>"))
                unaccounted[unit_id] = len(missing)
    return unaccounted


def _blocker_references_in_rows(rows: Iterable[LedgerRow]) -> list[tuple[str, str]]:
    refs: list[tuple[str, str]] = []
    for row in rows:
        section_id = str(row.obj.get("section_id", ""))
        for item in row.obj.get("missing_pieces", []):
            _kind, ref = _missing_item_kind_and_ref(item)
            if ref and ref.startswith(BLOCKER_PREFIXES):
                refs.append((section_id, ref))
    return refs


def _load_blocker_refs(root: Path) -> set[str]:
    refs: set[str] = set()
    for relative in (ACQUISITION_PATH, BLOCKERS_PATH):
        path = _rooted(root, relative)
        if not path.is_file():
            continue
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            for line in handle:
                if not line.strip():
                    continue
                try:
                    item = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if not isinstance(item, dict):
                    continue
                for key in ("id", "acq_id", "blocker_ref", "request_id", "ref"):
                    value = item.get(key)
                    if isinstance(value, str):
                        refs.add(value)
    return refs


def _editable_field_string_hits(root: Path, rows: Iterable[LedgerRow]) -> list[str]:
    hits: list[str] = []
    for row in rows:
        section_id = str(row.obj.get("section_id", ""))
        for key in ("reader_evidence", "missing_pieces", "unassessed_scope", "fulfillment_revision"):
            if key not in row.obj:
                continue
            field_hits = _fused_hits(_field_prose_strings(key, row.obj[key]))
            for hit in field_hits:
                hits.append(f"{section_id}.{key}: {hit}")
    return hits


def _au_upgrade_revision(revision: Any) -> dict[str, Any] | None:
    """The revision that made the row a well-formed AU row (mirrors _is_upgrade)."""
    while isinstance(revision, dict):
        previous = revision.get("previous_observation")
        if not isinstance(previous, dict):
            return None
        if (
            previous.get("status") != "authored_unreviewed"
            or previous.get("missing_pieces") != []
            or previous.get("unassessed_scope") != []
        ):
            return revision
        revision = previous.get("prior_revision")
    return None


def _validate_au_revision_assessments(root: Path, rows: Iterable[LedgerRow]) -> list[str]:
    failures: list[str] = []
    for row in rows:
        if row.obj.get("status") != "authored_unreviewed":
            continue
        revision = _au_upgrade_revision(row.obj.get("fulfillment_revision"))
        if not isinstance(revision, dict):
            continue
        patch_id = revision.get("patch_id")
        if not isinstance(patch_id, str) or not patch_id.startswith("ledger_patch-"):
            continue
        assessment_ids = revision.get("assessment_ids", [])
        if not isinstance(assessment_ids, list) or not all(isinstance(item, str) for item in assessment_ids):
            failures.append(f"{row.obj.get('section_id')}: upgrade patch_id revision lacks assessment ids")
            continue
        try:
            assessments = _load_assessments(root, assessment_ids)
            if not _has_first_confirm_pair(assessments):
                failures.append(
                    f"{row.obj.get('section_id')}: upgrade patch_id revision lacks a first and a "
                    "confirm assessment from distinct contexts"
                )
        except Refusal as exc:
            failures.append(f"{row.obj.get('section_id')}: {exc}")
    return failures


def _receipt_hash_warnings_and_failures(root: Path) -> tuple[list[str], list[str]]:
    warnings: list[str] = []
    failures: list[str] = []
    for shard in _ledger_shards(root):
        receipt = _receipt_path_for_shard(shard)
        actual = _sha256_file(shard)
        if not receipt.is_file():
            failures.append(f"{_rel(receipt, root)} missing")
            continue
        try:
            data = _read_json(receipt)
        except (OSError, json.JSONDecodeError) as exc:
            failures.append(f"{_rel(receipt, root)} unreadable: {exc}")
            continue
        if not isinstance(data, dict):
            failures.append(f"{_rel(receipt, root)} is not a JSON object")
            continue
        current = data.get("current")
        if current is None:
            failures.append(f"{_rel(receipt, root)} has no current object")
            continue
        if not isinstance(current, dict):
            failures.append(f"{_rel(receipt, root)} current is not an object")
            continue
        recorded = current.get("ledger_sha256")
        if not isinstance(recorded, str) or recorded.lower() != actual.lower():
            failures.append(f"{_rel(receipt, root)} current.ledger_sha256 mismatch")
    return warnings, failures


def run_check(root: Path = ROOT, *, final: bool = False) -> CheckResult:
    state = load_ledger(root)
    rows = state.rows
    hard: list[str] = []
    warnings: list[str] = []
    metrics: dict[str, Any] = {}

    ids = [str(row.obj.get("section_id", "")) for row in rows]
    toc_ids = _toc_section_ids(root)
    ledger_ids = set(ids)
    if len(rows) != 2475 or len(ledger_ids) != 2475 or ledger_ids != toc_ids:
        hard.append(
            "I1 section-id set mismatch: "
            f"rows={len(rows)} unique={len(ledger_ids)} toc={len(toc_ids)}"
        )
    if state.duplicate_sections:
        hard.append(f"I1 duplicate section ids: {state.duplicate_sections}")
    bad_statuses = sorted(
        {str(row.obj.get("status", "")) for row in rows if row.obj.get("status") not in ALLOWED_STATUSES}
    )
    if bad_statuses:
        hard.append(f"I2 invalid statuses: {', '.join(bad_statuses)}")

    au_bad_shape = [
        str(row.obj.get("section_id"))
        for row in rows
        if row.obj.get("status") == "authored_unreviewed"
        and not _au_shape_ok(row.obj)
    ]
    metrics["AU-shape"] = len(au_bad_shape)
    metrics["AU-stale"] = _au_stale_count(root, rows)
    if au_bad_shape:
        target = hard if final else warnings
        target.append(f"I3 AU rows with residual scope/evidence shape issue: {len(au_bad_shape)}")
    if final and metrics["AU-stale"]:
        hard.append(f"I3 AU-stale: {metrics['AU-stale']}")
    elif metrics["AU-stale"]:
        warnings.append(f"I3 AU-stale: {metrics['AU-stale']}")

    open_without_missing = [
        str(row.obj.get("section_id"))
        for row in rows
        if row.obj.get("status") in {"partial", "missing"} and not row.obj.get("missing_pieces")
    ]
    metrics["partial_or_missing_without_missing_pieces"] = len(open_without_missing)
    if open_without_missing:
        target = hard if final else warnings
        target.append(f"I4 partial/missing rows without missing_pieces: {len(open_without_missing)}")

    unassessed_without_scope = [
        str(row.obj.get("section_id"))
        for row in rows
        if row.obj.get("status") == "unassessed" and not row.obj.get("unassessed_scope")
    ]
    unassessed_count = sum(1 for row in rows if row.obj.get("status") == "unassessed")
    metrics["unassessed"] = unassessed_count
    metrics["unassessed_without_scope"] = len(unassessed_without_scope)
    if unassessed_without_scope:
        target = hard if final else warnings
        target.append(f"I5 unassessed rows without unassessed_scope: {len(unassessed_without_scope)}")
    if final and unassessed_count:
        hard.append(f"I5 unassessed rows remain: {unassessed_count}")

    revision_failures = _validate_au_revision_assessments(root, rows)
    if revision_failures:
        hard.append("I6 AU patch assessment failure(s): " + "; ".join(revision_failures[:10]))

    unaccounted = _duty_conservation_unaccounted(root, rows)
    metrics["I7-unaccounted-units"] = len(unaccounted)
    metrics["I7-unaccounted-by-unit"] = unaccounted
    metrics["I7-unaccounted-components"] = sum(unaccounted.values())
    if unaccounted:
        message = (
            "I7 unaccounted components: "
            f"{metrics['I7-unaccounted-components']} across {len(unaccounted)} unit(s)"
        )
        (hard if final else warnings).append(message)

    known_refs = _load_blocker_refs(root)
    blocker_refs = _blocker_references_in_rows(rows)
    unresolved = sorted({ref for _section, ref in blocker_refs if ref not in known_refs})
    metrics["unresolved_blocker_refs"] = len(unresolved)
    if unresolved:
        hard.append(f"I8 unresolved blocker refs: {', '.join(unresolved[:20])}")

    receipt_warnings, receipt_failures = _receipt_hash_warnings_and_failures(root)
    warnings.extend(f"I9 {item}" for item in receipt_warnings)
    hard.extend(f"I9 {item}" for item in receipt_failures)

    fused_hits = _editable_field_string_hits(root, rows)
    metrics["I10-fused-number-hits"] = len(fused_hits)
    if fused_hits:
        (hard if final else warnings).append(f"I10 fused-number hits in editable string fields: {len(fused_hits)}")

    outside_baseline = [
        (
            str(row.obj.get("section_id")),
            sorted(set(row.obj) - BASELINE_ROW_KEYS),
        )
        for row in rows
        if set(row.obj) - BASELINE_ROW_KEYS
    ]
    metrics["I11-row-key-union-size"] = len(BASELINE_ROW_KEYS)
    if outside_baseline:
        details = "; ".join(
            f"{section}: {', '.join(keys)}" for section, keys in outside_baseline
        )
        hard.append(f"I11 row keys outside baseline: {details}")

    metrics["status_counts"] = _status_counts(rows)
    metrics["rows"] = len(rows)
    metrics["unique_section_ids"] = len(ledger_ids)
    return CheckResult(hard=hard, warnings=warnings, metrics=metrics)


def print_check(result: CheckResult, *, i7_limit: int | None = 50) -> None:
    print(f"rows: {result.metrics.get('rows', 0)}")
    print(f"unique_section_ids: {result.metrics.get('unique_section_ids', 0)}")
    print("status_counts:")
    for status, count in result.metrics.get("status_counts", {}).items():
        print(f"  {status}: {count}")
    print(f"AU-stale: {result.metrics.get('AU-stale', 0)}")
    print(
        "I7 unaccounted: "
        f"{result.metrics.get('I7-unaccounted-components', 0)} component(s) "
        f"across {result.metrics.get('I7-unaccounted-units', 0)} unit(s)"
    )
    by_unit = sorted(
        result.metrics.get("I7-unaccounted-by-unit", {}).items(),
        # natural order: re.split with a group alternates text and digit runs
        key=lambda item: [
            int(part) if index % 2 else part
            for index, part in enumerate(re.split(r"(\d+)", item[0]))
        ],
    )
    shown = by_unit if i7_limit is None else by_unit[:i7_limit]
    for unit_id, count in shown:
        print(f"  {unit_id}: {count}")
    if len(shown) < len(by_unit):
        print(f"  plus {len(by_unit) - len(shown)} more unit(s) (use check --i7-detail for all)")
    print(f"I10 fused-number hits: {result.metrics.get('I10-fused-number-hits', 0)}")
    if result.warnings:
        print("\nwarnings:")
        for item in result.warnings:
            print(f"  - {item}")
    if result.hard:
        print("\nhard failures:")
        for item in result.hard:
            print(f"  - {item}")
    else:
        print("\nno hard failures")


def show_section(root: Path, section_id: str) -> int:
    state = load_ledger(root)
    row = state.by_section.get(section_id)
    if row is None:
        print(f"{section_id}: not found", file=sys.stderr)
        return 1
    print(f"shard: {_rel(row.shard, root)}")
    print(f"row_sha256: {row.row_sha256}")
    print(_json_pretty(row.obj))
    return 0


def _counts_from_rows(rows: Iterable[dict[str, Any]]) -> dict[str, int]:
    counts: collections.Counter[str] = collections.Counter(str(row.get("status", "")) for row in rows)
    return {status: counts.get(status, 0) for status in sorted(ALLOWED_STATUSES)}


def _previous_rows_from_tag(root: Path, tag: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for shard in _ledger_shards(root):
        relative = _rel(shard, root)
        proc = subprocess.run(
            ["git", "show", f"{tag}:{relative}"],
            cwd=root,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if proc.returncode != 0:
            detail = proc.stderr.strip() or f"git show exited {proc.returncode}"
            raise UsageError(f"{tag}: cannot read {relative}: {detail}")
        for line in proc.stdout.splitlines():
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(row, dict) and isinstance(row.get("section_id"), str):
                result[row["section_id"]] = row
    return result


def _section_sort_key(section_id: str) -> tuple[tuple[int, int | str], ...]:
    parts: list[tuple[int, int | str]] = []
    for part in section_id.split("."):
        if part.isdigit():
            parts.append((0, int(part)))
        else:
            parts.append((1, part))
    return tuple(parts)


def _format_delta(value: int | None) -> str:
    if value is None:
        return "n/a"
    if value > 0:
        return f"+{value}"
    return str(value)


def _current_rows_as_dicts(root: Path) -> list[dict[str, Any]]:
    return [row.obj for row in load_ledger(root).rows]


def _downgrades(rows: list[dict[str, Any]], previous: dict[str, dict[str, Any]] | None) -> list[str]:
    result: list[str] = []
    if previous is not None:
        for row in rows:
            section_id = str(row.get("section_id", ""))
            old = previous.get(section_id, {}).get("status")
            new = row.get("status")
            if old in STATUS_ORDER and new in STATUS_ORDER and STATUS_ORDER[str(new)] < STATUS_ORDER[str(old)]:
                result.append(f"{section_id}: {old} -> {new}")
        return sorted(result)
    for row in rows:
        revision = row.get("fulfillment_revision")
        if not isinstance(revision, dict):
            continue
        previous_observation = revision.get("previous_observation")
        if not isinstance(previous_observation, dict):
            continue
        old = previous_observation.get("status")
        new = row.get("status")
        if old in STATUS_ORDER and new in STATUS_ORDER and STATUS_ORDER[str(new)] < STATUS_ORDER[str(old)]:
            result.append(f"{row.get('section_id')}: {old} -> {new}")
    return sorted(result)


def _report_missing_piece_buckets(rows: list[dict[str, Any]]) -> tuple[list[str], dict[str, list[str]], int]:
    writable: list[str] = []
    blocked: dict[str, list[str]] = {
        "blocked_source": [],
        "blocked_math": [],
        "blocked_policy": [],
    }
    unclassified = 0
    for row in rows:
        if row.get("status") == "authored_unreviewed":
            continue
        section_id = str(row.get("section_id", ""))
        for item in row.get("missing_pieces", []):
            kind, ref = _missing_item_kind_and_ref(item)
            if kind == "writable" and row.get("status") == "partial":
                writable.append(section_id)
            elif kind in blocked:
                blocked[kind].append(f"{section_id}" + (f" ({ref})" if ref else ""))
            elif kind == "unclassified":
                unclassified += 1
    return sorted(set(writable)), {key: sorted(values) for key, values in blocked.items()}, unclassified


def _acquisition_summary(root: Path) -> dict[str, int] | None:
    path = _rooted(root, ACQUISITION_PATH)
    if not path.is_file():
        return None
    counts: collections.Counter[str] = collections.Counter()
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        for line in handle:
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                counts["malformed"] += 1
                continue
            if not isinstance(item, dict):
                counts["malformed"] += 1
                continue
            key = item.get("status") or item.get("state") or item.get("standing") or "unspecified"
            counts[str(key)] += 1
    return dict(sorted(counts.items()))


def report(root: Path, wave: str, prev_tag: str | None) -> int:
    rows = _current_rows_as_dicts(root)
    previous = _previous_rows_from_tag(root, prev_tag) if prev_tag else None
    current_counts = _counts_from_rows(rows)
    previous_counts = _counts_from_rows(previous.values()) if previous is not None else None
    check_result = run_check(root, final=False)
    writable, blocked, unclassified = _report_missing_piece_buckets(rows)
    unassessed = sorted(
        (str(row.get("section_id")) for row in rows if row.get("status") == "unassessed"),
        key=_section_sort_key,
    )
    downgrades = _downgrades(rows, previous)

    print(f"# Ledger Wave {wave} Report")
    print()
    print("## Downgrades")
    if downgrades:
        for item in downgrades[:100]:
            print(f"- {item}")
        if len(downgrades) > 100:
            print(f"- plus {len(downgrades) - 100} more")
    else:
        print("- none recorded")
    print()
    print("## Section Status Counts")
    print("| status | count | delta |")
    print("|---|---:|---:|")
    for status in sorted(ALLOWED_STATUSES):
        old_count = previous_counts.get(status, 0) if previous_counts is not None else None
        delta = current_counts.get(status, 0) - old_count if old_count is not None else None
        print(f"| {status} | {current_counts.get(status, 0)} | {_format_delta(delta)} |")
    print()
    print(f"AU-stale: {check_result.metrics.get('AU-stale', 0)}")
    print()
    print("## Partial With Writable Duties")
    if writable:
        print(f"- sections: {len(writable)}")
        print(f"- sample: {', '.join(writable[:40])}")
    else:
        print("- none classified")
    print()
    print("## Blocked Duties")
    labels = {
        "blocked_source": "source",
        "blocked_math": "math",
        "blocked_policy": "policy",
    }
    for key in ("blocked_source", "blocked_math", "blocked_policy"):
        values = blocked[key]
        print(f"- {labels[key]}: {len(values)}" + (f" ({', '.join(values[:20])})" if values else ""))
    print(f"- unclassified missing-piece items: {unclassified}")
    print()
    print("## Unassessed")
    print(f"- rows: {len(unassessed)}")
    if unassessed:
        print(f"- sample: {', '.join(unassessed[:60])}")
    print()
    print("## Duty Conservation")
    print(
        "- unaccounted: "
        f"{check_result.metrics.get('I7-unaccounted-components', 0)} component(s) "
        f"across {check_result.metrics.get('I7-unaccounted-units', 0)} unit(s)"
    )
    acquisition = _acquisition_summary(root)
    if acquisition is not None:
        print()
        print("## Acquisition Summary")
        for key, value in acquisition.items():
            print(f"- {key}: {value}")
    print()
    print(NON_ACCEPTANCE_SENTENCE)
    return 0


def _selftest() -> None:
    scratch = ROOT / "tmp" / "tooling-scratch" / "ledger"
    scratch.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=scratch) as tmp_name:
        root = Path(tmp_name)
        ledger_dir = _rooted(root, LEDGER_DIR)
        ledger_dir.mkdir(parents=True)
        (root / "spec").mkdir(exist_ok=True)
        handbook = root / "handbook"
        handbook.mkdir()
        body = handbook / "body.tex"
        body.write_text(
            "\\section{One}\\label{sec:test-one}\nText.\n",
            encoding="utf-8",
            newline="\n",
        )
        orphan = handbook / "orphan.tex"
        orphan.write_text(
            "\\section{Orphan}\\label{sec:orphan}\n",
            encoding="utf-8",
            newline="\n",
        )
        commented = handbook / "commented.tex"
        commented.write_text(
            "% \\label{sec:commented}\n",
            encoding="utf-8",
            newline="\n",
        )
        main = handbook / "main.tex"
        main.write_text("\\input{body}\n", encoding="utf-8", newline="\n")
        body_hash = _sha256_file(body, upper=True)
        orphan_hash = _sha256_file(orphan, upper=True)
        toc = {
            "parts": [
                {
                    "chapters": [
                        {
                            "numbered_sections": [
                                {"number": "1.1", "title": "One"},
                                {"number": "1.2", "title": "Two"},
                            ]
                        }
                    ]
                }
            ]
        }
        _rooted(root, TOC_PATH).parent.mkdir(parents=True, exist_ok=True)
        _rooted(root, TOC_PATH).write_text(
            json.dumps(toc, ensure_ascii=False, indent=2),
            encoding="utf-8",
            newline="\n",
        )
        queue = _rooted(root, QUEUE_PATH)
        queue.parent.mkdir(parents=True, exist_ok=True)
        queue.write_text(
            json.dumps(
                        {
                            "unit_id": "U1",
                            "required_components": [
                                {"component_id": "C1"},
                            ],
                        },
                separators=(",", ":"),
            )
            + "\n"
            + json.dumps({"unit_id": "U2", "required_components": [{"component_id": "C7"}]})
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        row1 = {
            "part": "P1",
            "chapter_id": "1",
            "chapter_title": "Ch",
            "section_id": "1.1",
            "section_title": "One",
            "status": "partial",
            "reader_evidence": [
                {
                    "path": "handbook/orphan.tex",
                    "anchor": "sec:orphan",
                    "line_start": 1,
                    "line_end": 1,
                    "read_extent": "old stale evidence",
                    "route_state": "on_current_recursive_input_route",
                    "sha256": "00",
                    "components": ["C-old"],
                }
            ],
            "source_facets": [],
            "missing_pieces": [{"duty": "C2", "component_ids": ["C2"], "kind": "writable", "blocker_ref": None, "since": "test"}],
            "unassessed_scope": [],
            "observed_utc": "2026-01-01T00:00:00Z",
        }
        row2 = {
            "part": "P1",
            "chapter_id": "1",
            "chapter_title": "Ch",
            "section_id": "1.2",
            "section_title": "Two",
            "status": "authored_unreviewed",
            "reader_evidence": [
                {
                    "path": "handbook/body.tex",
                    "anchor": "sec:test-one",
                    "line_start": 1,
                    "line_end": 2,
                    "read_extent": "read",
                    "route_state": "on_current_recursive_input_route",
                    "sha256": body_hash,
                    "components": ["C1"],
                }
            ],
            "source_facets": [],
            "missing_pieces": [],
            "unassessed_scope": [],
            "observed_utc": "2026-01-01T00:00:00Z",
        }
        row3 = json.loads(json.dumps(row2, ensure_ascii=False))
        row3["section_id"] = "1.3"
        row3["section_title"] = "Three"
        row3["missing_pieces"] = [
            {
                "duty": "residual [component:C9]",
                "component_ids": ["C9"],
                "kind": "writable",
                "blocker_ref": None,
                "since": "test",
            }
        ]
        shard = ledger_dir / "p01.jsonl"
        shard.write_text(
            _json_compact(row1).decode("utf-8")
            + "\n"
            + _json_compact(row2).decode("utf-8")
            + "\n"
            + _json_compact(row3).decode("utf-8")
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        receipt = ledger_dir / "p01-receipt.json"
        receipt.write_text('{"schema_version":1}\n', encoding="utf-8", newline="\n")
        state = load_ledger(root)
        old_line = shard.read_bytes().splitlines()[1]
        row = state.by_section["1.1"]
        assessments = _rooted(root, ASSESSMENTS_DIR) / "w00"
        assessments.mkdir(parents=True)

        def write_assessment(
            assessment_id: str,
            role: str,
            *,
            context_id: str | None = None,
            section_id: str = "1.1",
            verdict: str = "covered",
            duty_verdict: str = "covered",
            tex_path: str = "handbook/body.tex",
            tex_sha: str = body_hash,
            components: tuple[str, ...] = ("C1",),
            inputs: Any | None = None,
            include_assessment_id: bool = True,
        ) -> None:
            payload = {
                "schema": "coverage-assessment/1",
                "section_id": section_id,
                "assessor": {
                    "family": "anthropic",
                    "model": "opus",
                    "role": role,
                    "context_id": context_id or f"ctx-{assessment_id}",
                },
                "inputs": {"tex": [{"path": tex_path, "sha256": tex_sha}]}
                if inputs is None
                else inputs,
                "components": [
                    {"component_id": component, "verdict": verdict} for component in components
                ],
                "duties": [{"duty": "d1", "verdict": duty_verdict}],
            }
            if include_assessment_id:
                payload["assessment_id"] = assessment_id
            (assessments / f"{assessment_id}.json").write_text(
                json.dumps(payload, ensure_ascii=False, indent=2),
                encoding="utf-8",
                newline="\n",
            )

        write_assessment("CA-one", "first")
        write_assessment("CA-two", "confirm")
        write_assessment("CA-first-again", "first")
        write_assessment("CA-same-context", "confirm", context_id="ctx-CA-one")
        write_assessment("CA-uncovered", "confirm", verdict="partial")
        write_assessment("CA-duty-partial", "confirm", duty_verdict="partial")
        write_assessment("CA-stale", "confirm", tex_sha="0" * 64)
        write_assessment("CA-wrong-one", "first", section_id="9.9")
        write_assessment("CA-wrong-two", "confirm", section_id="9.9")
        write_assessment("CA-row2-one", "first", section_id="1.2")
        write_assessment("CA-row3-one", "first", section_id="1.3")
        write_assessment("CA-row2-c5-first", "first", section_id="1.2", components=("C1", "C5"))
        write_assessment(
            "CA-row2-c5-confirm", "confirm", section_id="1.2", components=("C1", "C5")
        )
        write_assessment("CA-case-confirm", "confirm", context_id="CTX-CA-ONE")
        write_assessment("CA-missing-field", "confirm", include_assessment_id=False)
        write_assessment("CA-inputs-list", "confirm", inputs=[])
        write_assessment("CA-inputs-empty", "confirm", inputs={"tex": []})
        write_assessment(
            "CA-orphan-one", "first", tex_path="handbook/orphan.tex", tex_sha=orphan_hash
        )
        write_assessment(
            "CA-orphan-two", "confirm", tex_path="handbook/orphan.tex", tex_sha=orphan_hash
        )
        (assessments / "CA-malformed.json").write_text("{not json", encoding="utf-8")

        good_upgrade = {
            "section_id": "1.1",
            "original_row_sha256": row.row_sha256,
            "set": {
                "status": "authored_unreviewed",
                "missing_pieces": [],
                "unassessed_scope": [],
            },
            "append_reader_evidence": [
                {
                    "path": "handbook/body.tex",
                    "anchor": "sec:test-one",
                    "line_start": 1,
                    "line_end": 2,
                    "read_extent": "read",
                    "components": ["C1"],
                    "assessment_ids": ["CA-one", "CA-two"],
                },
                {
                    # supersedes the old orphan entry's unassessed "C-old" claim
                    "path": "handbook/orphan.tex",
                    "anchor": "sec:orphan",
                    "line_start": 1,
                    "line_end": 1,
                    "read_extent": "re-read; claims nothing",
                    "components": [],
                },
            ],
            "assessment_ids": ["CA-one", "CA-two"],
            "reason": "test upgrade",
        }

        def clone(value: Any) -> Any:
            return json.loads(json.dumps(value, ensure_ascii=False))

        def write_proposals(path: Path, proposals: list[dict[str, Any]]) -> None:
            path.write_text(
                "".join(
                    json.dumps(item, separators=(",", ":")) + "\n"
                    for item in proposals
                ),
                encoding="utf-8",
                newline="\n",
            )

        case_number = 0

        def expect_error(
            proposals: list[dict[str, Any]],
            message: str,
            error_type: type[Exception] = Refusal,
        ) -> None:
            nonlocal case_number
            case_number += 1
            path = root / f"bad-{case_number}.jsonl"
            write_proposals(path, proposals)
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    apply_proposals(root, path, apply=False)
            except error_type as exc:
                assert message in str(exc), str(exc)
            else:
                raise AssertionError(f"expected {error_type.__name__}: {message}")

        bad = clone(good_upgrade)
        bad["original_row_sha256"] = "0" * 64
        expect_error([bad], "pin mismatch")

        expect_error([clone(good_upgrade), clone(good_upgrade)], "two proposals")

        bad = clone(good_upgrade)
        bad["set"]["status"] = "complete"
        expect_error([bad], "invalid status")

        bad = clone(good_upgrade)
        bad["set"]["chapter_title"] = "Changed"
        expect_error([bad], "immutable key")

        bad = clone(good_upgrade)
        bad["append_reader_evidence"][0]["path"] = "handbook/missing.tex"
        expect_error([bad], "evidence path is missing")

        bad = clone(good_upgrade)
        bad["append_reader_evidence"][0]["line_end"] = 99
        expect_error([bad], "exceeds file length")

        bad = clone(good_upgrade)
        bad["append_reader_evidence"][0]["anchor"] = "sec:nope"
        expect_error([bad], "anchor")

        bad = clone(good_upgrade)
        bad["append_reader_evidence"][0]["path"] = "handbook/commented.tex"
        bad["append_reader_evidence"][0]["anchor"] = "sec:commented"
        bad["append_reader_evidence"][0]["line_end"] = 1
        expect_error([bad], "anchor")

        bad = clone(good_upgrade)
        bad["append_reader_evidence"][0]["line_start"] = True
        expect_error([bad], "integers", UsageError)

        bad = clone(good_upgrade)
        bad["append_reader_evidence"][0]["read_extent"] = "around1115"
        expect_error([bad], "append_reader_evidence")

        bad = clone(good_upgrade)
        bad["reason"] = "in1348"
        expect_error([bad], "reason")

        bad = {
            "section_id": "1.1",
            "original_row_sha256": row.row_sha256,
            "set": {
                "missing_pieces": [
                    {"duty": "x", "component_ids": [], "kind": "writable", "around1115": "key"}
                ]
            },
            "assessment_ids": [],
            "reason": "lead: mechanical evidence refresh",
        }
        expect_error([bad], "set strings")

        # Plain-text mode: no Markdown masking, and identifier-named keys inside
        # missing_pieces items are still prose.
        for fused in (
            "`around1115` todo",
            "<in1348> todo",
            "[x](in1348 rest) todo",
            {"duty": "x", "component_ids": [], "kind": "writable", "status": "around1115 more"},
            {"duty": "x", "component_ids": [], "kind": "writable", "path": "in1348 prose"},
        ):
            bad = {
                "section_id": "1.1",
                "original_row_sha256": row.row_sha256,
                "set": {"missing_pieces": [fused]},
                "assessment_ids": ["CA-one"],
                "reason": "",
            }
            expect_error([bad], "fused-number")

        # missing_pieces item format
        for item, message in (
            ({"duty": "x", "component_ids": ["C2"], "kind": "whatever"}, "invalid kind"),
            ({"component_ids": ["C2"], "kind": "writable"}, "duty"),
            ({"duty": "x", "kind": "writable"}, "component_ids"),
            ({"duty": "x", "component_ids": [], "kind": "blocked_math"}, "blocker_ref"),
            (
                {"duty": "x", "component_ids": [], "kind": "blocked_source", "blocker_ref": "ZZZ-1"},
                "blocker_ref",
            ),
            (
                {"duty": "x", "component_ids": [], "kind": "blocked_policy", "blocker_ref": "POL-9"},
                "does not resolve",
            ),
            ("[blocked_math:MATH-404] legacy tagged string", "does not resolve"),
            (7, "string or an object"),
        ):
            bad = {
                "section_id": "1.1",
                "original_row_sha256": row.row_sha256,
                "set": {"missing_pieces": [item]},
                "assessment_ids": ["CA-one"],
                "reason": "",
            }
            expect_error([bad], message)

        bad = clone(good_upgrade)
        bad["assessment_ids"] = ["CA-one", "CA-first-again"]
        bad["append_reader_evidence"][0]["assessment_ids"] = []
        expect_error([bad], "role first and a role confirm")

        bad = clone(good_upgrade)
        bad["assessment_ids"] = ["CA-one", "CA-same-context"]
        bad["append_reader_evidence"][0]["assessment_ids"] = []
        expect_error([bad], "different assessor.context_id")

        bad = clone(good_upgrade)
        bad["assessment_ids"] = ["CA-one", "CA-one"]
        bad["append_reader_evidence"][0]["assessment_ids"] = []
        expect_error([bad], "at least two assessments")

        bad = clone(good_upgrade)
        bad["assessment_ids"] = ["CA-one", "CA-duty-partial"]
        bad["append_reader_evidence"][0]["assessment_ids"] = []
        expect_error([bad], "every duty verdict")

        for bad_id in ("CA-[o]ne", "../w00/CA-one", "CA-?"):
            bad = clone(good_upgrade)
            bad["assessment_ids"] = [bad_id, "CA-two"]
            bad["append_reader_evidence"][0]["assessment_ids"] = []
            expect_error([bad], "invalid assessment id")

        bad = clone(good_upgrade)
        bad["assessment_ids"] = ["CA-one", "CA-malformed"]
        bad["append_reader_evidence"][0]["assessment_ids"] = []
        expect_error([bad], "unreadable assessment")

        # Upgrade: evidence may claim only components both assessments cover.
        bad = clone(good_upgrade)
        bad["append_reader_evidence"][0]["components"] = ["C1", "C2"]
        expect_error([bad], "C2")

        # Upgrade: an older, unsuperseded evidence claim must be covered too.
        bad = clone(good_upgrade)
        del bad["append_reader_evidence"][1]
        expect_error([bad], "C-old")

        bad = clone(good_upgrade)
        bad["assessment_ids"] = ["CA-one", "CA-uncovered"]
        bad["append_reader_evidence"][0]["assessment_ids"] = ["CA-one", "CA-uncovered"]
        expect_error([bad], "verdict")

        bad = clone(good_upgrade)
        bad["assessment_ids"] = ["CA-one", "CA-stale"]
        bad["append_reader_evidence"][0]["assessment_ids"] = ["CA-one", "CA-stale"]
        expect_error([bad], "stale")

        bad = clone(good_upgrade)
        bad["assessment_ids"] = ["CA-wrong-one", "CA-wrong-two"]
        bad["append_reader_evidence"][0]["assessment_ids"] = ["CA-wrong-one", "CA-wrong-two"]
        expect_error([bad], "section_id")

        bad = clone(good_upgrade)
        bad["assessment_ids"] = ["CA-one", "CA-missing-field"]
        bad["append_reader_evidence"][0]["assessment_ids"] = ["CA-one", "CA-missing-field"]
        expect_error([bad], "assessment_id is missing")

        bad = clone(good_upgrade)
        bad["assessment_ids"] = ["CA-one", "CA-inputs-list"]
        bad["append_reader_evidence"][0]["assessment_ids"] = ["CA-one", "CA-inputs-list"]
        expect_error([bad], "inputs must be an object")

        bad = clone(good_upgrade)
        bad["assessment_ids"] = ["CA-one", "CA-inputs-empty"]
        bad["append_reader_evidence"][0]["assessment_ids"] = ["CA-one", "CA-inputs-empty"]
        expect_error([bad], "non-empty")

        bad = clone(good_upgrade)
        bad["append_reader_evidence"] = []
        expect_error([bad], "live on-route")

        bad = clone(good_upgrade)
        bad["append_reader_evidence"][0].update(
            {
                "path": "handbook/orphan.tex",
                "anchor": "sec:orphan",
                "line_end": 1,
                "assessment_ids": ["CA-orphan-one", "CA-orphan-two"],
            }
        )
        bad["assessment_ids"] = ["CA-orphan-one", "CA-orphan-two"]
        expect_error([bad], "live on-route")

        row2_initial = state.by_section["1.2"]
        row3_initial = state.by_section["1.3"]
        bad = {
            "section_id": "1.3",
            "original_row_sha256": row3_initial.row_sha256,
            "set": {"missing_pieces": []},
            "assessment_ids": ["CA-row3-one"],
            "reason": "",
        }
        expect_error([bad], "at least two assessments")

        downgrade = {
            "section_id": "1.2",
            "original_row_sha256": row2_initial.row_sha256,
            "set": {"status": "partial", "missing_pieces": ["needs review"]},
            "assessment_ids": ["CA-does-not-exist"],
            "reason": "",
        }
        expect_error([downgrade], "assessment file not found")

        bad = clone(downgrade)
        bad["assessment_ids"] = ["CA-one"]
        expect_error([bad], "section_id does not match 1.2")

        bad = clone(downgrade)
        bad["assessment_ids"] = []
        bad["reason"] = "lead: mechanical status change"
        expect_error([bad], "unchanged-status")

        def expect_ok(proposals: list[dict[str, Any]]) -> None:
            nonlocal case_number
            case_number += 1
            path = root / f"ok-{case_number}.jsonl"
            write_proposals(path, proposals)
            with contextlib.redirect_stdout(io.StringIO()):
                assert apply_proposals(root, path, apply=False) == 0

        # S1/S2: an AU row taking on a new component claim is an upgrade for it.
        s1 = {
            "section_id": "1.2",
            "original_row_sha256": row2_initial.row_sha256,
            "append_reader_evidence": [
                {
                    "path": "handbook/body.tex",
                    "anchor": "sec:test-one",
                    "line_start": 1,
                    "line_end": 2,
                    "read_extent": "read",
                    "components": ["C1", "C5"],
                }
            ],
            "assessment_ids": ["CA-row2-c5-first"],
            "reason": "",
        }
        expect_error([s1], "at least two assessments")
        bad = clone(s1)
        bad["assessment_ids"] = []
        bad["reason"] = "lead: refresh"
        bad["append_reader_evidence"][0]["assessment_ids"] = ["CA-row2-c5-first"]
        expect_error([bad], "at least two assessments")
        good = clone(s1)
        good["assessment_ids"] = ["CA-row2-c5-first", "CA-row2-c5-confirm"]
        expect_ok([good])

        # S3a: legacy string tags classify only as a full [kind:REF].
        for item, message in (
            ("[blocked_math] needs a proof source", "[blocked_math:REF]"),
            ("[bogus_kind] x", "unknown kind tag"),
            ("[bogus_kind:ACQ-1] x", "unknown kind tag"),
            ("[blocked_source:FOO-1] x", "blocker ref starting with"),
        ):
            bad = {
                "section_id": "1.1",
                "original_row_sha256": row.row_sha256,
                "set": {"missing_pieces": [item]},
                "assessment_ids": ["CA-one"],
                "reason": "",
            }
            expect_error([bad], message)
        assert _missing_item_kind_and_ref("[blocked_math] x") == ("unclassified", None)
        assert _missing_item_kind_and_ref("[bogus_kind:ACQ-1] x") == ("unclassified", None)
        assert _missing_item_kind_and_ref("[writable:W-1] x") == ("writable", "W-1")
        expect_ok(
            [
                {
                    "section_id": "1.1",
                    "original_row_sha256": row.row_sha256,
                    "set": {"missing_pieces": ["[component:C2] still to write"]},
                    "assessment_ids": ["CA-one"],
                    "reason": "",
                }
            ]
        )

        # S4: unknown top-level proposal keys are refused.
        bad = {
            "section_id": "1.1",
            "original_row_sha256": row.row_sha256,
            "set": {"missing_pieces": ["still open"]},
            "append_reader_evidence_": [{"path": "handbook/body.tex"}],
            "assessment_ids": ["CA-one"],
            "reason": "",
        }
        expect_error([bad], "unknown proposal key(s): append_reader_evidence_")

        # S5: only label-argument environments match an anchor.
        table_text = (
            "\\begin{tabular}{ll}\na & b\n\\end{tabular}\n"
            "\\begin{hbtheorem}{thm:x}{proved=x}{T}\nBody.\n\\end{hbtheorem}\n"
        )
        assert not _anchor_found(table_text, "ll")
        assert _anchor_found(table_text, "thm:x")

        # S6: context ids differing only in case are one context.
        bad = clone(good_upgrade)
        bad["assessment_ids"] = ["CA-one", "CA-case-confirm"]
        bad["append_reader_evidence"][0]["assessment_ids"] = []
        expect_error([bad], "different assessor.context_id")

        # S9: observed_utc is owned by the tool.
        bad = {
            "section_id": "1.1",
            "original_row_sha256": row.row_sha256,
            "set": {"observed_utc": "1999-01-01T00:00:00Z"},
            "assessment_ids": ["CA-one"],
            "reason": "",
        }
        expect_error([bad], "observed_utc cannot be set")

        # S22: with an assessment id, a lead: reason may change status.
        expect_ok(
            [
                {
                    "section_id": "1.1",
                    "original_row_sha256": row.row_sha256,
                    "set": {"status": "missing"},
                    "assessment_ids": ["CA-one"],
                    "reason": "lead: reclassify",
                }
            ]
        )

        # I6: a malformed-AU -> AU revision is the upgrade revision.
        def forged_au(previous_status: str, previous_missing: list[Any]) -> LedgerRow:
            obj = clone(row2)
            obj["fulfillment_revision"] = {
                "reason": "forged",
                "patch_id": "ledger_patch-20260101T000000Z-1.2",
                "assessment_ids": ["CA-row2-one"],
                "previous_observation": {
                    "status": previous_status,
                    "missing_pieces": previous_missing,
                    "unassessed_scope": [],
                    "observed_utc": "2026-01-01T00:00:00Z",
                    "row_sha256": "0" * 64,
                    "prior_revision": None,
                },
            }
            return LedgerRow(shard=shard, index=0, body=b"{}", newline=b"\n", obj=obj)

        assert _validate_au_revision_assessments(root, [forged_au("authored_unreviewed", ["x"])])
        assert _validate_au_revision_assessments(root, [forged_au("partial", ["x"])])
        assert not _validate_au_revision_assessments(root, [forged_au("authored_unreviewed", [])])

        # Report: "Partial With Writable Duties" counts partial rows only.
        writable_rows, _blocked, _unclassified = _report_missing_piece_buckets(
            [
                {"section_id": "8.1", "status": "partial", "missing_pieces": [{"kind": "writable"}]},
                {"section_id": "8.2", "status": "missing", "missing_pieces": [{"kind": "writable"}]},
            ]
        )
        assert writable_rows == ["8.1"], writable_rows

        bad = {
            "section_id": "1.2",
            "original_row_sha256": row2_initial.row_sha256,
            "append_reader_evidence": [
                {
                    "path": "handbook/body.tex",
                    "anchor": "sec:test-one",
                    "line_start": 1,
                    "line_end": 2,
                    "read_extent": "read again",
                    "components": ["C1"],
                }
            ],
            "assessment_ids": [],
            "reason": "lead:",
        }
        expect_error([bad], "requires text")

        bad = {
            "section_id": "1.1",
            "original_row_sha256": row.row_sha256,
            "set": {"missing_pieces": ["trivial"]},
            "assessment_ids": [],
            "reason": "lead: mechanical evidence refresh",
        }
        expect_error([bad], "may not use set")

        bad = {
            "section_id": "1.3",
            "original_row_sha256": row3_initial.row_sha256,
            "set": {"missing_pieces": []},
            "assessment_ids": [],
            "reason": "lead: mechanical evidence refresh",
        }
        expect_error([bad], "at least two assessments")

        bad = {
            "section_id": "1.2",
            "original_row_sha256": row2_initial.row_sha256,
            "set": {"missing_pieces": ["now missing"]},
            "assessment_ids": [],
            "reason": "lead: mechanical evidence refresh",
        }
        expect_error([bad], "may not use set")

        bad = {
            "section_id": "1.1",
            "original_row_sha256": row.row_sha256,
            "set": {"missing_pieces": []},
            "assessment_ids": [],
            "reason": "lead: mechanical evidence refresh",
        }
        expect_error([bad], "may not use set")

        bad = {
            "section_id": "1.1",
            "original_row_sha256": row.row_sha256,
            "set": {"status": "unassessed", "unassessed_scope": []},
            "assessment_ids": ["CA-one"],
            "reason": "",
        }
        expect_error([bad], "unassessed requires")

        # route_state: only handbook/ paths can be on route, even when a
        # repo-root file shares a reached handbook-relative name.
        (root / "body.tex").write_text(
            "\\section{Root}\\label{sec:root-body}\n", encoding="utf-8", newline="\n"
        )
        reached = _handbook_reached_files(root)
        assert "body.tex" in reached
        entries = _prepare_evidence_entries(
            [{"path": "body.tex", "anchor": "sec:root-body", "line_start": 1, "line_end": 1}],
            root,
            reached,
        )
        assert entries[0]["route_state"] == "off_route"
        assert not _live_on_route_evidence_paths(root, entries, reached)

        # Undecodable files: a clean refusal for evidence, no crash in the closure.
        (handbook / "binary.tex").write_bytes(b"\xff\xfe\x00garbage\n")
        assert "body.tex" in _handbook_reached_files(root)
        bad = clone(good_upgrade)
        bad["append_reader_evidence"][0].update(
            {"path": "handbook/binary.tex", "anchor": "x", "line_end": 1}
        )
        expect_error([bad], "not UTF-8")

        # Non-AU row with an assessment: claims limited to covered components.
        bad = {
            "section_id": "1.1",
            "original_row_sha256": row.row_sha256,
            "append_reader_evidence": [
                {
                    "path": "handbook/body.tex",
                    "anchor": "sec:test-one",
                    "line_start": 1,
                    "line_end": 2,
                    "read_extent": "read",
                    "components": ["C1", "C2"],
                }
            ],
            "assessment_ids": ["CA-one"],
            "reason": "",
        }
        expect_error([bad], "C2 are not covered")
        # AU row: a new claim (C2) is an upgrade; keeping C1 is not.
        row2_claim = {
            "section_id": "1.2",
            "original_row_sha256": row2_initial.row_sha256,
            "append_reader_evidence": [
                {
                    "path": "handbook/body.tex",
                    "anchor": "sec:test-one",
                    "line_start": 1,
                    "line_end": 2,
                    "read_extent": "read",
                    "components": ["C1", "C2"],
                }
            ],
            "assessment_ids": ["CA-row2-one"],
            "reason": "",
        }
        expect_error([row2_claim], "at least two assessments")
        row2_claim["append_reader_evidence"][0]["components"] = ["C1"]
        claim_path = root / "row2-claim.jsonl"
        write_proposals(claim_path, [row2_claim])
        with contextlib.redirect_stdout(io.StringIO()):
            assert apply_proposals(root, claim_path, apply=False) == 0

        proposal_path = root / "proposal.jsonl"
        write_proposals(proposal_path, [good_upgrade])
        with contextlib.redirect_stdout(io.StringIO()):
            assert apply_proposals(root, proposal_path, apply=False) == 0
        assert shard.read_bytes().splitlines()[1] == old_line
        with contextlib.redirect_stdout(io.StringIO()):
            assert apply_proposals(root, proposal_path, apply=True) == 0
        new_state = load_ledger(root)
        assert new_state.by_section["1.1"].obj["status"] == "authored_unreviewed"
        evidence = new_state.by_section["1.1"].obj["reader_evidence"][-2]
        assert evidence["sha256"] == body_hash
        assert evidence["route_state"] == "on_current_recursive_input_route"
        assert new_state.by_section["1.1"].obj["reader_evidence"][-1]["route_state"] == "off_route"
        assert shard.read_bytes().splitlines()[1] == old_line
        receipt_data = _read_json(receipt)
        assert receipt_data["current"]["ledger_sha256"] == _sha256_file(shard)
        assert '"schema_version":1' in receipt.read_text(encoding="utf-8-sig")

        result = run_check(root, final=False)
        assert result.metrics["I7-unaccounted-components"] == 1
        assert result.metrics["I7-unaccounted-by-unit"] == {"U2": 1}
        printed = io.StringIO()
        with contextlib.redirect_stdout(printed):
            print_check(result)
        assert "  U2: 1" in printed.getvalue()
        assert all(item.startswith("I1 ") for item in result.hard)

        # Receipt refresh splices only current/history; all other bytes stay.
        receipt.write_text(
            '{\n  "schema_version": 1,\n  "nested": {\n    "a": [\n      1,\n      2\n    ]\n  },\n'
            '  "current": {"ledger_sha256": "old"},\n  "trailing": {"x":   "y"}\n}\n',
            encoding="utf-8",
            newline="\n",
        )

        def outside_current_history(text: str) -> str:
            members, _close = _top_level_json_members(text)
            for key, _start, value_start, value_end in sorted(members, key=lambda m: -m[2]):
                if key in ("current", "history"):
                    text = text[:value_start] + text[value_end:]
            return text

        receipt_frame = outside_current_history(receipt.read_text(encoding="utf-8"))

        lead_refresh = {
            "section_id": "1.1",
            "original_row_sha256": new_state.by_section["1.1"].row_sha256,
            "append_reader_evidence": [
                {
                    "path": "handbook/body.tex",
                    "anchor": "sec:test-one",
                    "line_start": 1,
                    "line_end": 2,
                    "read_extent": "mechanical refresh",
                    "components": ["C1"],
                }
            ],
            "assessment_ids": [],
            "reason": "lead: mechanical evidence refresh",
        }
        lead_refresh_path = root / "lead-refresh.jsonl"
        # A lead: refresh without assessments may not claim new components,
        # neither on an existing (path, anchor) nor on a new one.
        bad = clone(lead_refresh)
        bad["append_reader_evidence"][0]["components"] = ["C1", "C7"]
        expect_error([bad], "at least two assessments")
        bad = clone(lead_refresh)
        bad["append_reader_evidence"][0].update(
            {"path": "handbook/orphan.tex", "anchor": "sec:orphan", "line_end": 1}
        )
        expect_error([bad], "may not claim new component(s) C1")
        write_proposals(lead_refresh_path, [lead_refresh])
        with contextlib.redirect_stdout(io.StringIO()):
            assert apply_proposals(root, lead_refresh_path, apply=True) == 0
        first_receipt = receipt.read_text(encoding="utf-8")
        # the only non-value bytes added are the inserted history key
        first_frame = outside_current_history(first_receipt)
        assert first_frame.replace(',\n  "history": ', "", 1) == receipt_frame, first_frame
        assert len(_read_json(receipt)["history"]) == 1
        i6_result = run_check(root, final=False)
        assert not any(item.startswith("I6 ") for item in i6_result.hard)

        body.write_text(
            "\\section{One}\\label{sec:test-one}\nText.\nFresh line.\n",
            encoding="utf-8",
            newline="\n",
        )
        row2_stale = load_ledger(root).by_section["1.2"]
        assert _au_stale_count(root, [row2_stale]) == 1
        stale_refresh = {
            "section_id": "1.2",
            "original_row_sha256": row2_stale.row_sha256,
            "append_reader_evidence": [
                {
                    "path": "handbook/body.tex",
                    "anchor": "sec:test-one",
                    "line_start": 1,
                    "line_end": 3,
                    "read_extent": "mechanical refresh after source edit",
                    "components": ["C1"],
                }
            ],
            "assessment_ids": [],
            "reason": "lead: mechanical evidence refresh",
        }
        stale_refresh_path = root / "stale-refresh.jsonl"
        write_proposals(stale_refresh_path, [stale_refresh])
        with contextlib.redirect_stdout(io.StringIO()):
            assert apply_proposals(root, stale_refresh_path, apply=True) == 0
        row2_refreshed = load_ledger(root).by_section["1.2"]
        assert _au_stale_count(root, [row2_refreshed]) == 0
        second_receipt = receipt.read_text(encoding="utf-8")
        assert outside_current_history(second_receipt) == first_frame
        assert len(_read_json(receipt)["history"]) == 2
        # history's first element was copied, not re-indented again
        assert second_receipt.count('"ledger_sha256": "old"') == 1

        # S8: a non-list history is refused before any write, never replaced.
        bad_receipt = '{"current": {"ledger_sha256": "x"}, "history": {"note": "keep"}}\n'
        receipt.write_text(bad_receipt, encoding="utf-8", newline="\n")
        shard_before = shard.read_bytes()
        s8 = clone(stale_refresh)
        s8["original_row_sha256"] = row2_refreshed.row_sha256
        write_proposals(stale_refresh_path, [s8])
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                apply_proposals(root, stale_refresh_path, apply=True)
            raise AssertionError("non-list receipt history should be refused")
        except Refusal as exc:
            assert "history is not a list" in str(exc), str(exc)
        assert shard.read_bytes() == shard_before
        assert receipt.read_text(encoding="utf-8") == bad_receipt
        receipt.write_text(second_receipt, encoding="utf-8", newline="\n")
        new_state = load_ledger(root)

        refs = _blocker_references_in_rows(
            [
                LedgerRow(
                    shard=shard,
                    index=0,
                    body=b"{}",
                    newline=b"\n",
                    obj={
                        "section_id": "x",
                        "missing_pieces": [
                            "needs MATH-heavy rewrite",
                            "[blocked_math:MATH-123] exact blocker",
                            {"kind": "blocked_source", "blocker_ref": "ACQ-456"},
                        ],
                    },
                )
            ]
        )
        assert ("x", "MATH-heavy") not in refs
        assert ("x", "MATH-123") in refs
        assert ("x", "ACQ-456") in refs
        evidence_hits = _fused_hits(
            _field_prose_strings(
                "reader_evidence", [{"sha256": "ecbcf3119", "read_extent": "around1115"}]
            )
        )
        assert any("around1115" in item for item in evidence_hits)
        assert not any("ecbcf3119" in item for item in evidence_hits)
        revision_hits = _fused_hits(
            _field_prose_strings(
                "fulfillment_revision",
                {"patch_id": "x-in1348", "reason": "in1348", "previous_observation": {
                    "row_sha256": "ab12cdef", "missing_pieces": [{"status": "around1115"}]}},
            )
        )
        assert len(revision_hits) == 2, revision_hits

        bad_proposal = root / "bad.jsonl"
        bad = {
            "section_id": "1.2",
            "original_row_sha256": new_state.by_section["1.2"].row_sha256,
            "set": {"missing_pieces": ["around1115"]},
            "assessment_ids": [],
            "reason": "lead: mechanical evidence refresh",
        }
        bad_proposal.write_text(json.dumps(bad) + "\n", encoding="utf-8", newline="\n")
        try:
            apply_proposals(root, bad_proposal, apply=False)
            raise AssertionError("fused-number proposal should be refused")
        except Refusal:
            pass

        lines = shard.read_text(encoding="utf-8-sig").splitlines()
        rogue = json.loads(lines[1])
        rogue["totally_new_key"] = "bad"
        lines[1] = _json_compact(rogue).decode("utf-8")
        shard.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        result = run_check(root, final=False)
        assert any(item.startswith("I11 ") and "totally_new_key" in item for item in result.hard)
        assert any(
            item.startswith("I9 ") and "current.ledger_sha256 mismatch" in item
            for item in result.hard
        )

        receipt.write_text('{"schema_version":1}\n', encoding="utf-8", newline="\n")
        dropped_current = run_check(root, final=True)
        assert any(
            item.startswith("I9 ") and "has no current object" in item
            for item in dropped_current.hard
        )

        receipt.unlink()
        missing_receipt = run_check(root, final=False)
        assert any(
            item.startswith("I9 ") and item.endswith("p01-receipt.json missing")
            for item in missing_receipt.hard
        )

        lines.append(lines[0])
        shard.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                apply_proposals(root, bad_proposal, apply=False)
            raise AssertionError("duplicate section ids should refuse apply")
        except Refusal as exc:
            assert "duplicate section ids" in str(exc)


def _configure_stdio() -> None:
    stdout_reconfigure = getattr(sys.stdout, "reconfigure", None)
    if callable(stdout_reconfigure):
        stdout_reconfigure(encoding="utf-8", newline="\n")
    stderr_reconfigure = getattr(sys.stderr, "reconfigure", None)
    if callable(stderr_reconfigure):
        stderr_reconfigure(
            encoding="utf-8",
            errors="backslashreplace",
            newline="\n",
        )


def main(argv: list[str] | None = None) -> int:
    _configure_stdio()
    parser = argparse.ArgumentParser(description="Patch and audit the edition-2026 fulfillment ledger.")
    parser.add_argument("--selftest", action="store_true", help="run internal tests")
    subparsers = parser.add_subparsers(dest="command")

    apply_parser = subparsers.add_parser("apply", help="apply or dry-run ledger proposals")
    apply_parser.add_argument("--proposals", required=True, help="proposal JSONL file")
    apply_parser.add_argument("--apply", action="store_true", help="write changed ledger rows and receipts")

    check_parser = subparsers.add_parser("check", help="check ledger invariants")
    check_parser.add_argument("--final", action="store_true", help="treat terminal warnings as hard failures")
    check_parser.add_argument("--i7-detail", action="store_true", help="list every unit with unaccounted components")

    report_parser = subparsers.add_parser("report", help="write a Markdown ledger report")
    report_parser.add_argument("--wave", required=True, help="wave id such as 00")
    report_parser.add_argument("--prev-tag", help="optional git tag for status deltas")

    show_parser = subparsers.add_parser("show", help="show one section row")
    show_parser.add_argument("section_id")

    refresh_parser = subparsers.add_parser(
        "refresh-receipts", help="write each shard receipt's current block from the live shard (no row changes)")
    refresh_parser.add_argument("--apply", action="store_true", help="write the receipts")

    args = parser.parse_args(argv)
    if args.selftest:
        _selftest()
        return 0
    if args.command is None:
        parser.print_usage(sys.stderr)
        return 2
    try:
        if args.command == "apply":
            return apply_proposals(ROOT, Path(args.proposals), apply=args.apply)
        if args.command == "check":
            result = run_check(ROOT, final=args.final)
            print_check(result, i7_limit=None if args.i7_detail else 50)
            return 0 if result.ok else 1
        if args.command == "report":
            return report(ROOT, args.wave, args.prev_tag)
        if args.command == "refresh-receipts":
            shards = _ledger_shards(ROOT)
            for shard in shards:
                print(("refresh " if args.apply else "would refresh ") + str(_receipt_path_for_shard(shard)))
                if args.apply:
                    _refresh_receipt(ROOT, shard, _now_utc())
            return 0
        return show_section(ROOT, args.section_id)
    except Refusal as exc:
        print(str(exc), file=sys.stderr)
        return 1
    except LedgerError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    except Exception as exc:  # one line, not a traceback, for any unexpected failure
        print(f"error: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

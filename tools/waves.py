#!/usr/bin/env python3
"""Authoring-wave packet, ownership, and scoped-build tooling.

The commands in this file are intentionally plain: the wave files are planning
artifacts, while integration and ledger mutation are handled by neighboring
tools.  Mutating subcommands default to dry-run and write atomically only with
``--apply``.
"""

from __future__ import annotations

import argparse
import contextlib
import copy
import csv
import hashlib
import importlib.util
import io
import json
import math
import os
import posixpath
import re
import subprocess
import sys
import tempfile
import time
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parent.parent
COVERAGE = Path("spec/coverage/edition-2026")
FULFILLMENT = COVERAGE / "current-fulfillment"
QUEUE = COVERAGE / "completion-work-queue.jsonl"
TOC = Path("spec/proposed-table-of-contents.json")
HELD_SOURCES = COVERAGE / "held-sources.json"
WAVES_ROOT = Path("work/waves")
UNIT_BUILDS = Path("tmp/unit-builds")

AU = "authored_unreviewed"
MAX_CONCURRENT = 12
AGENT_BUDGET = 940

CHECK_CATEGORIES = {
    "annex-bidir",
    "status-spec",
    "duplicate-label",
    "dangling-ref",
    "label-prefix",
    "bib-key",
}
SYMBOL_HEADER = [
    "glyph",
    "macro",
    "role",
    "scope",
    "precedence",
    "first_use",
    "notes",
]
FROZEN_EXPLICIT = {
    "handbook/handbook.sty",
    "handbook/main.tex",
    "handbook/frontmatter.tex",
    "handbook/bib/handbook.bib",
    "handbook/registry/symbols.csv",
    "handbook/registry/symbol-scopes.json",
}
WORKFLOW_WORDS = (
    "review",
    "admission",
    "admitted",
    "ledger",
    "assessor",
    "intake",
    "wave",
    "this record",
    "author block",
)
PRESCRIPTIVE_WORDS = (
    "must",
    "should",
    "shall",
    "ought",
    "required",
    "requires",
    "require",
    "always",
    "never",
)


class UsageError(Exception):
    """A command-line or input-file problem."""


class Refusal(Exception):
    """The repository state does not allow the requested result (exit 1)."""


def _root(path: Path | str = ".") -> Path:
    return ROOT / Path(path)


def _rel(path: Path | str) -> str:
    p = Path(path)
    try:
        return p.resolve().relative_to(ROOT).as_posix()
    except (OSError, ValueError):
        return p.as_posix().replace("\\", "/")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def _write_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = ""
    try:
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            newline="\n",
            dir=path.parent,
            delete=False,
        ) as handle:
            tmp = handle.name
            handle.write(text)
        os.replace(tmp, path)
    finally:
        if tmp:
            try:
                os.unlink(tmp)
            except FileNotFoundError:
                pass


def _write_json_atomic(path: Path, data: Any) -> None:
    _write_atomic(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def _json_line(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _path_exists_rel(rel: str) -> bool:
    return _root(rel).is_file()


def _try_normalize_repo_path(value: str) -> str | None:
    text = str(value).strip().replace("\\", "/")
    if not text:
        return None
    try:
        if re.match(r"^[A-Za-z]:/", text) or text.startswith("/"):
            root_resolved = ROOT.resolve(strict=False)
            rel = Path(text).resolve(strict=False).relative_to(root_resolved)
            text = rel.as_posix()
        else:
            while text.startswith("./"):
                text = text[2:]
            text = posixpath.normpath(text)
            if text in {"", "."}:
                return None
            if text == ".." or text.startswith("../") or "/../" in text:
                return None
        parts = text.split("/")
        if any(part in {"", "."} for part in parts):
            return None
        if any(part == ".." for part in parts):
            return None
        return text
    except (OSError, ValueError):
        return None


def _normalize_repo_path(value: str) -> str:
    normalized = _try_normalize_repo_path(value)
    if normalized is None:
        raise UsageError(f"path escapes repository or is not normalizable: {value!r}")
    return normalized


def _path_has_prefix(path: str, prefix: str) -> bool:
    path_cmp = path.casefold() if os.name == "nt" else path
    prefix_cmp = prefix.casefold() if os.name == "nt" else prefix
    return path_cmp == prefix_cmp.rstrip("/") or path_cmp.startswith(prefix_cmp.rstrip("/") + "/")


def _handbook_rel(path: str) -> str:
    rel = _normalize_repo_path(path)
    if rel.startswith("handbook/"):
        return rel[len("handbook/") :]
    return rel


def _part_dir(part: str) -> str:
    return f"p{int(part[1:]):02d}"


def _natural_section_key(section_id: str) -> tuple[int, ...]:
    pieces: list[int] = []
    for item in re.findall(r"\d+", section_id):
        pieces.append(int(item))
    return tuple(pieces)


def _part_key(part: str) -> int:
    try:
        return int(part[1:])
    except (ValueError, IndexError):
        return 999


def _section_title(row: dict[str, Any]) -> str:
    return str(row.get("section_title") or row.get("title") or "")


def _section_id(row: dict[str, Any]) -> str:
    return str(row.get("section_id") or row.get("number") or "")


def _chapter_id(row: dict[str, Any]) -> str:
    return str(row.get("chapter_id") or row.get("chapter") or "")


def _chapter_title(row: dict[str, Any]) -> str:
    return str(row.get("chapter_title") or row.get("chapter") or "")


def _iter_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    if not path.is_file():
        return
    with path.open("r", encoding="utf-8-sig") as handle:
        for number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                raise UsageError(f"{_rel(path)}:{number}: malformed JSONL: {exc}") from exc
            if isinstance(item, dict):
                yield item


def _load_json(path: Path, default: Any = None) -> Any:
    if not path.is_file():
        return default
    try:
        return json.loads(_read_text(path))
    except json.JSONDecodeError as exc:
        raise UsageError(f"{_rel(path)}: malformed JSON: {exc}") from exc


def _load_ledger_rows() -> list[dict[str, Any]]:
    base = _root(FULFILLMENT)
    if not base.is_dir():
        raise UsageError(f"{FULFILLMENT.as_posix()} is missing")
    rows: list[dict[str, Any]] = []
    for path in sorted(base.glob("*.jsonl")):
        for row in _iter_jsonl(path):
            row = dict(row)
            row["_ledger_path"] = path.relative_to(ROOT).as_posix()
            rows.append(row)
    return rows


def _load_toc_order() -> dict[str, dict[str, Any]]:
    toc = _load_json(_root(TOC), {})
    order: dict[str, dict[str, Any]] = {}
    ordinal = 0
    for part in toc.get("parts", []) if isinstance(toc, dict) else []:
        part_id = str(part.get("stable_part_id") or "")
        for chapter in part.get("chapters", []) or []:
            chapter_number = str(chapter.get("number") or "")
            chapter_title = str(chapter.get("title") or "")
            for section in chapter.get("numbered_sections", []) or []:
                ordinal += 1
                number = str(section.get("number") or "")
                order[number] = {
                    "order": ordinal,
                    "part": part_id,
                    "chapter": chapter_number,
                    "chapter_title": chapter_title,
                    "title": section.get("title"),
                }
    return order


def _row_order(row: dict[str, Any], toc_order: dict[str, dict[str, Any]]) -> tuple[int, tuple[int, ...]]:
    section = _section_id(row)
    if section in toc_order:
        return int(toc_order[section]["order"]), _natural_section_key(section)
    return 10_000_000, _natural_section_key(section)


def _unit_ids_for_row(row: dict[str, Any]) -> list[str]:
    result: list[str] = []
    for facet in row.get("source_facets", []) or []:
        if isinstance(facet, dict) and facet.get("unit_id"):
            result.append(str(facet["unit_id"]))
    return result


def _component_id(component: dict[str, Any]) -> str:
    return str(component.get("component_id") or component.get("id") or "")


def _text_items(value: Any) -> list[str]:
    items: list[str] = []
    if isinstance(value, str):
        if value.strip():
            items.append(value.strip())
    elif isinstance(value, list):
        for item in value:
            items.extend(_text_items(item))
    elif isinstance(value, dict):
        for item in value.values():
            items.extend(_text_items(item))
    return items


def _row_open_texts(row: dict[str, Any]) -> list[str]:
    texts: list[str] = []
    texts.extend(_text_items(row.get("missing_pieces")))
    texts.extend(_text_items(row.get("unassessed_scope")))
    return texts


def _component_tokens(component: dict[str, Any]) -> list[str]:
    tokens: list[str] = []
    for key in (
        "component_id",
        "id",
        "body_label",
        "annex_label",
        "description",
        "success_condition",
        "failure_condition",
        "exact_current_text",
    ):
        tokens.extend(_text_items(component.get(key)))
    return tokens


def _component_matches_open_text(component: dict[str, Any], open_texts: list[str]) -> bool:
    if not open_texts:
        return False
    haystacks = [text.casefold() for text in open_texts]
    for token in _component_tokens(component):
        folded = token.casefold()
        if folded and any(folded in haystack for haystack in haystacks):
            return True
    component_text = json.dumps(component, ensure_ascii=False).casefold()
    return any(text.casefold() in component_text for text in open_texts if len(text) >= 24)


def _explicit_open_component_ids(row: dict[str, Any]) -> list[str]:
    # The ledger's own open-component notation (ledger_patch I7): dict items
    # with component_ids, or [component:ID] tags in legacy strings.
    ids: list[str] = []
    for key in ("missing_pieces", "unassessed_scope"):
        for item in row.get(key) or []:
            if isinstance(item, dict):
                ids.extend(_identity_strings_from_value(item.get("component_ids")))
            elif isinstance(item, str):
                ids.extend(m.strip() for m in re.findall(r"\[component:([^\]]+)\]", item))
    return _dedupe(ids)


def _facet_state(row: dict[str, Any], unit_id: str, unit: dict[str, Any] | None) -> str:
    for facet in row.get("source_facets") or []:
        if isinstance(facet, dict) and str(facet.get("unit_id") or "") == unit_id:
            state = facet.get("baseline_content_state")
            if isinstance(state, str) and state:
                return state
    if unit:
        state = unit.get("content_state")
        if isinstance(state, str) and state:
            return state
    return ""


def _open_components_for_row(
    row: dict[str, Any],
    units: dict[str, dict[str, Any]],
) -> tuple[set[str], int]:
    # Packet sizing counts only work still open in this row. A component is open
    # when the row's missing/unassessed note names that component's id, label or
    # text, or when the facet itself is marked missing. Unmapped open work counts
    # as one fallback component for the section instead of reopening every
    # already-authored component in every facet unit.
    open_texts = _row_open_texts(row)
    status = str(row.get("status") or "").casefold()
    has_open_note = bool(open_texts) or status in {"missing", "unassessed"}
    component_ids: set[str] = set(_explicit_open_component_ids(row))
    fallback = 0
    for unit_id in _unit_ids_for_row(row):
        unit = units.get(unit_id)
        components = [
            c for c in (unit or {}).get("required_components") or []
            if isinstance(c, dict)
        ]
        state = _facet_state(row, unit_id, unit).casefold()
        missing_unit = state in {"missing", "identified_missing", "not_started"}
        if missing_unit or (not open_texts and status == "missing"):
            for component in components:
                cid = _component_id(component)
                if cid:
                    component_ids.add(cid)
            if not components:
                fallback += 1
            continue
        matched = False
        for component in components:
            if _component_matches_open_text(component, open_texts):
                cid = _component_id(component)
                if cid:
                    component_ids.add(cid)
                    matched = True
        if unit is None and has_open_note:
            fallback += 1
        elif matched:
            continue
    if has_open_note and not component_ids and fallback == 0:
        fallback = 1
    return component_ids, fallback


def _load_queue_units(unit_ids: set[str]) -> dict[str, dict[str, Any]]:
    if not unit_ids:
        return {}
    path = _root(QUEUE)
    found: dict[str, dict[str, Any]] = {}
    if not path.is_file():
        return found
    with path.open("r", encoding="utf-8-sig") as handle:
        for number, line in enumerate(handle, 1):
            if len(found) == len(unit_ids):
                break
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise UsageError(f"{QUEUE.as_posix()}:{number}: malformed JSONL: {exc}") from exc
            unit_id = row.get("unit_id")
            if unit_id in unit_ids:
                found[str(unit_id)] = _normalize_unit_paths(row)
    return found


# Lead ruling 2026-10-03: the frozen queue (hash-pinned by receipts) keeps its bytes, but
# destination paths corrupted by a fused space ("p 08") or unpadded ("p8") are read with
# their evident part ("p08"). Part-less units take the lead's assignment file.
_MALFORMED_DIR_RE = re.compile(r"(handbook/(?:parts|annex)/)p(?:\s+(\d{1,2})|(\d))(?=/|\.tex|-route\.tex)")
UNIT_PART_ASSIGNMENTS = Path("work/waves/unit-part-assignments.json")


def _normalize_unit_paths(unit: dict[str, Any]) -> dict[str, Any]:
    def fix(value: Any) -> Any:
        if isinstance(value, str):
            return _MALFORMED_DIR_RE.sub(lambda m: f"{m.group(1)}p{int(m.group(2) or m.group(3)):02d}", value)
        if isinstance(value, list):
            return [fix(v) for v in value]
        if isinstance(value, dict):
            return {k: fix(v) for k, v in value.items()}
        return value
    if "destination" not in unit:
        return unit
    fixed = dict(unit)
    fixed["destination"] = fix(unit["destination"])
    return fixed


def _assigned_part(unit_id: str) -> str | None:
    path = _root(UNIT_PART_ASSIGNMENTS)
    if not path.is_file():
        return None
    value = json.loads(path.read_text(encoding="utf-8")).get(unit_id)
    return value if isinstance(value, str) and re.fullmatch(r"P(?:[1-9]|1[0-9])", value) else None


def _scan_queue(needed: set[str], linked: set[str]) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    """One pass over the queue: the needed units, and every unit that no
    ledger row links (no source_facets reference)."""
    found: dict[str, dict[str, Any]] = {}
    unlinked: dict[str, dict[str, Any]] = {}
    for row in _iter_jsonl(_root(QUEUE)):
        unit_id = row.get("unit_id")
        if not isinstance(unit_id, str) or not unit_id:
            continue
        row = _normalize_unit_paths(row)
        if unit_id in needed:
            found[unit_id] = row
        if unit_id not in linked:
            unlinked[unit_id] = row
    return found, unlinked


ACCOUNTING_MODES = {"accounting", "unit_accounting"}


def _unit_component_ids(unit: dict[str, Any]) -> list[str]:
    return _dedupe(
        cid
        for component in unit.get("required_components") or []
        if isinstance(component, dict)
        for cid in [_component_id(component)]
        if cid
    )


def _evidence_stale(row: dict[str, Any]) -> bool:
    """Some file's latest reader_evidence entry has no sha256 or one that differs from the
    current file (a missing file differs), or an entry is not an object (no sha256: fail
    closed). reader_evidence is append-only, so an older entry for a file is superseded by a
    later one for the same file (e.g. a post-routing re-assessment pair)."""
    latest: dict[str, Any] = {}
    for evidence in row.get("reader_evidence") or []:
        if not isinstance(evidence, dict):
            return True
        rel = _try_normalize_repo_path(evidence["path"]) if isinstance(evidence.get("path"), str) else None
        if rel is None:
            return True
        latest[_path_key(rel)] = (rel, evidence.get("sha256"))
    for rel, recorded in latest.values():
        current = _cached_sha256(rel)
        if not isinstance(recorded, str) or current is None or recorded.strip().lower() != current:
            return True
    return False


def _lacks_component_accounting(row: dict[str, Any], queue_units: dict[str, dict[str, Any]]) -> bool:
    """No single reader_evidence entry carries a non-empty components list
    covering all component ids of the row's facet units (section 10 (c),
    read per entry). A facet unit missing from the queue has unknown
    components, so it cannot be covered (fail closed)."""
    wanted: set[str] = set()
    facets = row.get("source_facets", []) or []
    if any(not isinstance(facet, dict) or not facet.get("unit_id") for facet in facets):
        return True  # malformed facet: fail closed
    for unit_id in _unit_ids_for_row(row):
        unit = queue_units.get(unit_id)
        if unit is None:
            return True
        wanted.update(_unit_component_ids(unit))
    # Entries backed by the same assessment ids (one first+confirm pair split per file, e.g. body
    # and annex) count together; an entry without assessment ids counts alone.
    groups: dict[Any, set[str]] = {}
    for index, evidence in enumerate(row.get("reader_evidence") or []):
        if not isinstance(evidence, dict) or not isinstance(evidence.get("components"), list):
            continue  # components must be a list (a bare string does not count as accounting)
        claimed = set(_identity_strings_from_value(evidence.get("components")))
        claimed.update(
            _component_id(item) for item in evidence.get("components") or [] if isinstance(item, dict)
        )
        claimed.discard("")
        ids = evidence.get("assessment_ids")
        key = tuple(sorted(ids)) if isinstance(ids, list) and ids else ("entry", index)
        groups.setdefault(key, set()).update(claimed)
    return not any(claimed and wanted <= claimed for claimed in groups.values())


def _au_accounting_reasons(row: dict[str, Any], queue_units: dict[str, dict[str, Any]]) -> list[str]:
    """Why an authored_unreviewed row still needs accounting (empty: it does not)."""
    reasons: list[str] = []
    if row.get("unassessed_scope"):
        reasons.append("parked_scope")
    if row.get("missing_pieces"):
        reasons.append("au_with_missing_pieces")
    if _evidence_stale(row):
        reasons.append("stale_evidence")
    if _lacks_component_accounting(row, queue_units):
        reasons.append("no_component_accounting")
    return reasons


DESTINATION_PROPOSAL_KEYS = (
    "proposed_path",
    "proposed_source_presentation",
    "proposed_source_proof_destination",
    "proposed_body",
    "proposed_annex",
)


DESTINATION_WRITE_KEYS = ("body", "annex", "completion")
# The completion dict form {"body": path, "annex": path} names proposals too.
COMPLETION_PROPOSAL_KEYS = ("body", "annex")
# Reference destinations: they give a unit's part and hosts, never owned files
# (no ruling makes a lookup proposal a writable destination).
DESTINATION_LOOKUP_KEYS = ("lookup", "historical_navigation")


def _unit_destinations(
    unit: dict[str, Any], keys: tuple[str, ...] = DESTINATION_WRITE_KEYS
) -> tuple[list[str], list[str]]:
    """(proposed, existing) destination paths of a queue unit, in order:
    proposals from destination.body/annex/completion (or the given keys),
    including string values under body/annex of the completion dict form,
    and the paths the destination records (existing anchors). A proposal
    that exists on disk counts as existing."""
    proposed: list[str] = []
    existing: list[str] = []

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if isinstance(child, str):
                    rel = _try_normalize_repo_path(child) if child.startswith("handbook/") else None
                    if rel is None:
                        continue
                    if key in DESTINATION_PROPOSAL_KEYS or key in COMPLETION_PROPOSAL_KEYS:
                        (existing if _path_exists_rel(rel) else proposed).append(rel)
                    elif key == "path":
                        existing.append(rel)
                else:
                    walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    destination = unit.get("destination")
    if isinstance(destination, dict):
        for key in keys:
            walk(destination.get(key))
    return _dedupe(proposed), _dedupe(existing)


def _unit_lookup_paths(unit: dict[str, Any]) -> list[str]:
    """destination.lookup (and historical_navigation) paths, proposed or existing."""
    proposed, existing = _unit_destinations(unit, DESTINATION_LOOKUP_KEYS)
    return _dedupe(proposed + existing)


PART_PATH_RE = re.compile(r"handbook/(?:parts|annex)/p(\d{2})(?:/|\.tex$|-route\.tex$)")


def _part_of_number(number: str) -> str | None:
    n = int(number)
    return f"P{n}" if 1 <= n <= 19 else None


def _unit_part(unit: dict[str, Any], parents: dict[str, list["InputEdge"]]) -> str | None:
    """A queue unit's part: destination.primary_part, else the first
    body/annex/completion path under handbook/parts|annex/pNN, else the first
    such lookup path, else the P<n> in prerequisite_allocation_prefix, else
    the part driver on the input route of the first routed destination or
    lookup path. None when nothing names a part."""
    assigned = _assigned_part(str(unit.get("unit_id", "")))
    if assigned:
        return assigned
    destination = unit.get("destination")
    primary = destination.get("primary_part") if isinstance(destination, dict) else None
    if isinstance(primary, str) and re.fullmatch(r"P(?:[1-9]|1[0-9])", primary.strip()):
        return primary.strip()
    proposed, existing = _unit_destinations(unit)
    lookup = _unit_lookup_paths(unit)
    for rel in proposed + existing + lookup:
        match = PART_PATH_RE.match(rel)
        if match and _part_of_number(match.group(1)):
            return _part_of_number(match.group(1))
    prefix = unit.get("prerequisite_allocation_prefix")
    match = re.search(r"-P(\d{1,2})-", prefix) if isinstance(prefix, str) else None
    if match and _part_of_number(match.group(1)):
        return _part_of_number(match.group(1))
    for rel in existing + lookup:
        found = sorted(
            {
                _part_of_number(m.group(1))
                for chain in _route_chains(rel, parents)
                for edge in chain
                for m in [PART_PATH_RE.match(edge.host)]
                if m and _part_of_number(m.group(1))
            },
            key=lambda part: _part_key(part or ""),
        )
        if found:
            return found[0]
    return None


# A part directory written with a fused space (p 15) or unpadded (p8): the
# part is evident but the queue path is malformed, so no part is derived from
# it (never guessed); the unplaced record names the evident part instead.
MALFORMED_PART_PATH_RE = re.compile(r"handbook/(?:parts|annex)/p(?:\s+(\d{1,2})|(\d))(?=/|\.tex|-route\.tex)")
UNPLACED_MALFORMED = "malformed part path (fused space / unpadded pNN)"
UNPLACED_NO_PART = "no part named"


def _unplaced_reason(unit: dict[str, Any]) -> tuple[str, list[str]]:
    """Why an unlinked unit has no derivable part, and the parts its
    malformed destination paths evidently name (in part order)."""
    text = json.dumps(unit.get("destination"), ensure_ascii=False)
    evident = {
        part
        for match in MALFORMED_PART_PATH_RE.finditer(text)
        for part in [_part_of_number(match.group(1) or match.group(2))]
        if part
    }
    if evident:
        return UNPLACED_MALFORMED, sorted(evident, key=_part_key)
    return UNPLACED_NO_PART, []


def _pack_units(
    unit_ids: list[str],
    units: dict[str, dict[str, Any]],
    ignore: set[str] | frozenset[str] = frozenset(),
    cap: int = 6,
) -> list[list[str]]:
    """Units sharing a destination .tex file cluster together (union-find;
    files in `ignore`, such as drivers and frozen files, link nothing); the
    clusters are packed, in order of their first destination path, up to
    `cap` units per packet. A larger cluster is split in that order."""
    uf = UnionFind()
    owner: dict[str, str] = {}
    keys: dict[str, tuple[str, str]] = {}
    for unit_id in unit_ids:
        uf.find(unit_id)
        proposed, existing = _unit_destinations(units[unit_id])
        paths = _dedupe(proposed + existing + _unit_lookup_paths(units[unit_id]))
        keys[unit_id] = (paths[0] if paths else "~", unit_id)
        for rel in paths:
            if not rel.endswith(".tex") or rel in ignore:
                continue
            if rel in owner:
                uf.union(owner[rel], unit_id)
            else:
                owner[rel] = unit_id
    groups: dict[str, list[str]] = defaultdict(list)
    for unit_id in unit_ids:
        groups[uf.find(unit_id)].append(unit_id)
    clusters = sorted((sorted(group, key=keys.__getitem__) for group in groups.values()), key=lambda g: keys[g[0]])
    packets: list[list[str]] = []
    current: list[str] = []
    for cluster in clusters:
        if current and len(current) + len(cluster) > cap:
            packets.append(current)
            current = []
        for start in range(0, len(cluster), cap):
            piece = cluster[start : start + cap]
            if len(piece) == cap:
                packets.append(piece)
            else:
                current.extend(piece)
    if current:
        packets.append(current)
    return packets


@dataclass
class HeldIndex:
    entries: list[dict[str, Any]] = field(default_factory=list)
    identity_to_paths: dict[str, list[str]] = field(default_factory=dict)
    bibkey_to_entries: dict[str, list[dict[str, Any]]] = field(default_factory=dict)
    path_to_entry: dict[str, dict[str, Any]] = field(default_factory=dict)
    path: str = ""
    available: bool = False
    unavailable_reason: str = ""

    def paths_for_identities(self, identities: Iterable[str]) -> list[str]:
        paths: list[str] = []
        seen: set[str] = set()
        for identity in identities:
            for path in self.identity_to_paths.get(_identity_key(identity), []):
                if path not in seen:
                    seen.add(path)
                    paths.append(path)
            for entry in self.bibkey_to_entries.get(identity, []):
                raw_path = entry.get("path")
                normalized = _try_normalize_repo_path(raw_path) if isinstance(raw_path, str) else None
                if normalized and normalized not in seen:
                    seen.add(normalized)
                    paths.append(normalized)
        return paths

    def paths_for_presentations(self, presentations: Any) -> list[str]:
        # Held paths: files the index maps to the presentation's identities,
        # plus source files the presentation records with a matching hash.
        # Handbook files are presentations of the book itself, not held
        # sources to compare prose against.
        paths: list[str] = []
        for presentation in _presentation_dicts(presentations):
            paths.extend(self.paths_for_identities(_presentation_identities(presentation)))
            paths.extend(
                path for path in _verified_recorded_files(presentation)
                if not _path_has_prefix(path, "handbook")
            )
        return _dedupe(paths)


def _identity_key(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip()).casefold()


def _dedupe(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def _held_entry_strings(entry: dict[str, Any], key: str) -> Iterable[str]:
    value = entry.get(key)
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            if isinstance(item, str):
                yield item


def _add_identity_path(index: HeldIndex, identity: Any, path: str) -> None:
    if not isinstance(identity, str) or not identity.strip() or not path:
        return
    key = _identity_key(identity)
    index.identity_to_paths.setdefault(key, [])
    if path not in index.identity_to_paths[key]:
        index.identity_to_paths[key].append(path)


def _held_index_from_data(data: Any, path_label: str) -> HeldIndex:
    entries: list[dict[str, Any]]
    if isinstance(data, dict) and isinstance(data.get("entries"), list):
        entries = [e for e in data["entries"] if isinstance(e, dict)]
    elif isinstance(data, list):
        entries = [e for e in data if isinstance(e, dict)]
    else:
        entries = []
    index = HeldIndex(
        entries=entries,
        path=path_label,
        available=bool(entries),
        unavailable_reason="" if entries else f"{path_label} has no held-source entries",
    )
    source_index = data.get("source_index", {}) if isinstance(data, dict) else {}
    if isinstance(source_index, dict):
        for source_id, paths in source_index.items():
            if not isinstance(paths, list):
                continue
            for p in paths:
                normalized = _try_normalize_repo_path(p) if isinstance(p, str) else None
                if normalized:
                    _add_identity_path(index, str(source_id), normalized)
    for entry in entries:
        raw_path = entry.get("path")
        path_text = _try_normalize_repo_path(raw_path) if isinstance(raw_path, str) else None
        if path_text:
            index.path_to_entry[path_text] = entry
            _add_identity_path(index, path_text, path_text)
            _add_identity_path(index, entry.get("sha256"), path_text)
        else:
            path_text = ""
        for source_id in _held_entry_strings(entry, "source_ids"):
            if path_text:
                _add_identity_path(index, source_id, path_text)
        for key in _held_entry_strings(entry, "bibkeys"):
            index.bibkey_to_entries.setdefault(key, []).append(entry)
            if path_text:
                _add_identity_path(index, key, path_text)
        for key in (
            "titles",
            "doi",
            "dois",
            "benchmark_ids",
            "benchmark_id",
            "source_keys",
            "source_key",
        ):
            for value in _held_entry_strings(entry, key):
                if path_text:
                    _add_identity_path(index, value, path_text)
    return index


def _build_held_sources_in_memory(path: Path) -> HeldIndex | None:
    if path.resolve() != _root(HELD_SOURCES).resolve():
        return None
    held_script = _root("tools/held_sources.py")
    if not held_script.is_file():
        return None
    try:
        spec = importlib.util.spec_from_file_location("_waves_held_sources", held_script)
        if spec is None or spec.loader is None:
            return None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)  # type: ignore[union-attr]
        data, _stats = module.build_index(ROOT)  # type: ignore[attr-defined]
    except Exception as exc:
        return HeldIndex(
            path=f"{HELD_SOURCES.as_posix()} (in-memory dry-run)",
            available=False,
            unavailable_reason=f"{HELD_SOURCES.as_posix()} is missing and in-memory build failed: {exc}",
        )
    return _held_index_from_data(
        data,
        f"{HELD_SOURCES.as_posix()} (in-memory dry-run)",
    )


def _load_held_sources(path: Path | None = None) -> HeldIndex:
    path = path or _root(HELD_SOURCES)
    if not path.is_file():
        built = _build_held_sources_in_memory(path)
        if built is not None:
            return built
        return HeldIndex(
            path=_rel(path),
            available=False,
            unavailable_reason=f"{_rel(path)} is missing",
        )
    data = _load_json(path, {})
    return _held_index_from_data(data, _rel(path))


def _presentation_dicts(presentations: Any) -> list[dict[str, Any]]:
    if isinstance(presentations, dict):
        return [presentations]
    if isinstance(presentations, list):
        return [item for item in presentations if isinstance(item, dict)]
    return []


def _identity_strings_from_value(value: Any) -> Iterable[str]:
    if isinstance(value, str) and value.strip():
        yield value.strip()
    elif isinstance(value, list):
        for item in value:
            yield from _identity_strings_from_value(item)


# Identity fields of one presentation. Titles count only at the presentation's
# top level or in its own bibliographic record, never from nested containers,
# and keys such as identified_citation_keys_within_block (works cited inside
# the source) are not identities of the presentation itself.
PRESENTATION_IDENTITY_KEYS = (
    "source_id",
    "source_ids",
    "source_key",
    "key",
    "citation_key",
    "bibliography_key",
    "bibliographic_key",
    "bibkey",
    "bibkeys",
    "dblp_key",
    "benchmark_id",
    "benchmark_ids",
    "doi",
    "container_doi",
    "work_doi",
    "title",
    "local_path",
    "local_artifact",
    "local_capture",
    "artifact",
    "sha256",
)
RECORD_IDENTITY_KEYS = ("key", "citation_key", "source_id", "doi", "title")
RECORD_KEYS = ("bibliographic_record", "bibliographic_records", "bibliographic_identity")
ARTIFACT_KEYS = ("artifacts", "local_artifacts")


def _pathlike_identity(value: str) -> str | None:
    if "/" not in value and "\\" not in value:
        return None
    if not re.search(r"\.[A-Za-z0-9]{2,5}$", value):
        return None
    return _try_normalize_repo_path(value)


def _presentation_identities(presentations: Any) -> list[str]:
    identities: list[str] = []
    titles: set[str] = set()
    for presentation in _presentation_dicts(presentations):
        titles.update(_identity_strings_from_value(presentation.get("title")))
        for key in PRESENTATION_IDENTITY_KEYS:
            identities.extend(_identity_strings_from_value(presentation.get(key)))
        for key in RECORD_KEYS:
            for record in _presentation_dicts(presentation.get(key)):
                titles.update(_identity_strings_from_value(record.get("title")))
                for record_key in RECORD_IDENTITY_KEYS:
                    identities.extend(_identity_strings_from_value(record.get(record_key)))
        for key in ARTIFACT_KEYS:
            artifacts = presentation.get(key)
            for artifact in artifacts if isinstance(artifacts, list) else [artifacts]:
                if isinstance(artifact, str):
                    # Free-text notes in local_artifacts identify nothing.
                    if _pathlike_identity(artifact):
                        identities.append(artifact)
                elif isinstance(artifact, dict):
                    for artifact_key in ("path", "local_path", "sha256"):
                        identities.extend(_identity_strings_from_value(artifact.get(artifact_key)))
    expanded: list[str] = []
    for identity in identities:
        if " " not in identity.strip() and identity in titles:
            # A one-word title ("Introduction") identifies nothing.
            continue
        expanded.append(identity)
        normalized = _pathlike_identity(identity)
        if normalized:
            expanded.append(normalized)
    return _dedupe(expanded)


def _presentation_recorded_missing(presentation: dict[str, Any]) -> bool:
    state = str(presentation.get("body_state") or "").casefold()
    return "missing" in state or state in {"absent", "not_held", "unavailable"}


_SHA_CACHE: dict[tuple[str, int, int], str] = {}


def _cached_sha256(rel: str) -> str | None:
    path = _root(rel)
    try:
        if not path.is_file():
            return None
        stat = path.stat()
    except OSError:
        return None
    key = (str(path), stat.st_size, stat.st_mtime_ns)
    if key not in _SHA_CACHE:
        _SHA_CACHE[key] = _sha256_file(path)
    return _SHA_CACHE[key]


# A repo path named in an author's scope record ("Local original: <path>").
RECORD_PATH_RE = re.compile(r"(?<![\w./-])((?:source|citations|spec|handbook|tmp)/[^\s`'\"<>\[\]{}(),;*]+)")


def _author_scope_record_paths(value: Any) -> list[str]:
    """Paths of the author scope records a presentation links, at any depth."""
    paths: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "author_scope_records":
                for item in child if isinstance(child, list) else [child]:
                    raw = item.get("path") if isinstance(item, dict) else item
                    if isinstance(raw, str):
                        normalized = _try_normalize_repo_path(raw)
                        if normalized:
                            paths.append(normalized)
            else:
                paths.extend(_author_scope_record_paths(child))
    elif isinstance(value, list):
        for child in value:
            paths.extend(_author_scope_record_paths(child))
    return paths


def _recorded_artifacts(presentation: dict[str, Any]) -> list[tuple[str, str]]:
    """(path, sha256) pairs a presentation records for its local files.

    Sources: artifacts/local_artifacts entries with a path and hash, top-level
    local_path/local_artifact/local_capture with the presentation's sha256, and
    files that a linked author scope record names together with their hash.
    """
    pairs: list[tuple[str, str]] = []
    top_sha = presentation.get("sha256")
    if isinstance(top_sha, str):
        for key in ("local_path", "local_artifact", "local_capture"):
            for value in _identity_strings_from_value(presentation.get(key)):
                pairs.append((value, top_sha))
    for key in ARTIFACT_KEYS:
        artifacts = presentation.get(key)
        for artifact in artifacts if isinstance(artifacts, list) else [artifacts]:
            if not isinstance(artifact, dict) or not isinstance(artifact.get("sha256"), str):
                continue
            for path_key in ("path", "local_path"):
                value = artifact.get(path_key)
                if isinstance(value, str):
                    pairs.append((value, artifact["sha256"]))
    for record in _dedupe(_author_scope_record_paths(presentation)):
        if not _root(record).is_file():
            continue
        try:
            text = _read_text(_root(record))
        except (OSError, UnicodeDecodeError):
            continue
        lowered = text.lower()
        for match in RECORD_PATH_RE.finditer(text):
            rel = _try_normalize_repo_path(match.group(1).rstrip(".:"))
            sha = _cached_sha256(rel) if rel else None
            if rel and sha and sha in lowered:
                pairs.append((rel, sha))
    return pairs


def _verified_recorded_files(presentation: dict[str, Any]) -> list[str]:
    """Recorded local files that exist now with the recorded sha256."""
    files: list[str] = []
    for raw, sha in _recorded_artifacts(presentation):
        rel = _try_normalize_repo_path(raw)
        if rel and _cached_sha256(rel) == sha.strip().lower():
            files.append(rel)
    return _dedupe(files)


def _presentation_available(
    presentation: dict[str, Any],
    held: HeldIndex,
    census: dict[str, str],
) -> bool:
    # Fail closed: a presentation with no resolvable identity is absent, and a
    # presentation whose own record says its body is missing stays absent even
    # if a looser identity (for example a shared series source_id) matches a
    # held file. Only a census verdict of full or partial overrides that.
    # A recorded local file whose current hash equals the recorded hash is
    # held (source/formal-logic-reference.tex, handbook presentations, and
    # files an author scope record pins by hash).
    identities = _presentation_identities(presentation)
    if any(census.get(identity) in {"full", "partial"} for identity in identities):
        return True
    if _presentation_recorded_missing(presentation):
        return False
    if _verified_recorded_files(presentation):
        return True
    return bool(identities) and bool(held.paths_for_identities(identities))


CENSUS_VERDICTS = {"full", "partial", "missing", "absent", "none"}


def _load_census(path: Path | None) -> dict[str, str]:
    if path is None:
        return {}
    if not path.is_file():
        raise UsageError(f"--census file does not exist: {path}")
    data = _load_json(path, {})
    result: dict[str, str] = {}

    def verdict_of(record: dict[str, Any]) -> str | None:
        # Exact tokens only: "full text not held" or "not full" is not full.
        # Any other value is unknown, which the source gate treats as neither
        # full nor partial (fail closed).
        for key in ("verdict", "source_verdict", "held_verdict", "extent_verdict", "coverage"):
            value = record.get(key)
            if isinstance(value, str):
                lowered = value.strip().lower()
                if lowered in CENSUS_VERDICTS:
                    return lowered
        return None

    def bind(record: dict[str, Any]) -> None:
        verdict = verdict_of(record)
        if not verdict:
            return
        for key in ("unit_id", "source_id", "id", "source_key", "bibkey"):
            value = record.get(key)
            if isinstance(value, str) and value:
                result[value] = verdict

    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                bind(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                v = verdict_of(value)
                if v:
                    result[str(key)] = v
                bind(value)
            elif isinstance(value, str):
                lowered = value.strip().lower()
                if lowered in CENSUS_VERDICTS:
                    result[str(key)] = lowered
        for name in ("sources", "units", "records", "entries"):
            seq = data.get(name)
            if isinstance(seq, list):
                for item in seq:
                    if isinstance(item, dict):
                        bind(item)
    return result


def _read_blockers() -> dict[str, dict[str, Any]]:
    blockers: dict[str, dict[str, Any]] = {}
    for rel in (COVERAGE / "blockers.jsonl", COVERAGE / "acquisition-requests.jsonl"):
        path = _root(rel)
        if not path.is_file():
            continue
        for row in _iter_jsonl(path):
            ident = row.get("id") or row.get("blocker_ref") or row.get("request_id")
            if isinstance(ident, str):
                blockers[ident] = row
    return blockers


def _open_blocker_sections(blockers: dict[str, dict[str, Any]]) -> dict[str, str]:
    result: dict[str, str] = {}
    closed = {"closed", "resolved", "retired", "cancelled", "canceled"}
    for ident, row in blockers.items():
        status = str(row.get("status") or row.get("state") or "open").lower()
        if status in closed:
            continue
        raw_sections = row.get("sections")
        sections: list[Any]
        if isinstance(raw_sections, list):
            sections = raw_sections
        else:
            sections = [row.get("section_id"), row.get("section")]
        for section in sections:
            if isinstance(section, str) and section:
                result.setdefault(section, ident)
    return result


class UnionFind:
    def __init__(self) -> None:
        self.parent: dict[Any, Any] = {}

    def find(self, item: Any) -> Any:
        if item not in self.parent:
            self.parent[item] = item
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, a: Any, b: Any) -> None:
        ra = self.find(a)
        rb = self.find(b)
        if ra != rb:
            self.parent[rb] = ra


def _clusters_for_chapter(rows: list[dict[str, Any]]) -> list[list[dict[str, Any]]]:
    uf = UnionFind()
    unit_owner: dict[str, int] = {}
    for i, row in enumerate(rows):
        uf.find(i)
        for unit_id in _unit_ids_for_row(row):
            if unit_id in unit_owner:
                uf.union(i, unit_owner[unit_id])
            else:
                unit_owner[unit_id] = i
    groups: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for i, row in enumerate(rows):
        groups[uf.find(i)].append(row)
    return list(groups.values())


def _cluster_component_count(cluster: list[dict[str, Any]], units: dict[str, dict[str, Any]]) -> int:
    component_ids: set[str] = set()
    fallback = 0
    for row in cluster:
        row_components, row_fallback = _open_components_for_row(row, units)
        component_ids.update(row_components)
        fallback += row_fallback
    return len(component_ids) + fallback


def _split_rows_for_caps(
    rows: list[dict[str, Any]],
    units: dict[str, dict[str, Any]],
    toc_order: dict[str, dict[str, Any]],
) -> list[list[dict[str, Any]]]:
    packets: list[list[dict[str, Any]]] = []
    current: list[dict[str, Any]] = []

    def flush() -> None:
        nonlocal current
        if current:
            packets.append(current)
        current = []

    for row in sorted(rows, key=lambda item: _row_order(item, toc_order)):
        candidate = current + [row]
        if current and (
            len(candidate) > 4 or _cluster_component_count(candidate, units) > 8
        ):
            flush()
            candidate = [row]
        current = candidate
        if len(current) >= 4:
            flush()
    flush()
    return packets


def _bin_pack_chapter(
    chapter_clusters: list[list[dict[str, Any]]],
    units: dict[str, dict[str, Any]],
    toc_order: dict[str, dict[str, Any]],
) -> list[list[dict[str, Any]]]:
    packets: list[list[dict[str, Any]]] = []
    current: list[dict[str, Any]] = []
    current_components = 0

    def flush() -> None:
        nonlocal current, current_components
        if current:
            packets.append(current)
        current = []
        current_components = 0

    for cluster in sorted(
        chapter_clusters,
        key=lambda c: min(_row_order(row, toc_order) for row in c),
    ):
        section_count = len(cluster)
        component_count = _cluster_component_count(cluster, units)
        if (
            current
            and (len(current) + section_count > 4 or current_components + component_count > 8)
        ):
            flush()
        if section_count > 4 or component_count > 8:
            flush()
            packets.extend(_split_rows_for_caps(cluster, units, toc_order))
            continue
        current.extend(cluster)
        current_components += component_count
    flush()
    return packets


def _slugify(text: str) -> str:
    normalized = text.lower()
    replacements = {
        "&": " and ",
        "+": " plus ",
        "\\": " ",
        "/": " ",
    }
    for old, new in replacements.items():
        normalized = normalized.replace(old, new)
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized)
    normalized = re.sub(r"-+", "-", normalized).strip("-")
    if not normalized:
        normalized = "packet"
    pieces = normalized.split("-")
    return "-".join(pieces[:6])[:60].strip("-") or "packet"


def _label_files() -> dict[str, set[str]]:
    """Label -> the handbook .tex files that define it."""
    labels: dict[str, set[str]] = defaultdict(set)
    base = _root("handbook")
    if not base.is_dir():
        return labels
    pattern = re.compile(r"\\label\{([^{}]+)\}|\\begin\{(?:hbtheorem|hblemma|hbcorollary|hbdefinition|hbconvention|hbmethod|hbexample|hbwarning|proofboundary|systementry|annexitem)\}\s*\{([^{}]+)\}")
    for path in base.rglob("*.tex"):
        try:
            text = _read_text(path)
        except OSError:
            continue
        rel = path.relative_to(ROOT).as_posix()
        for match in pattern.finditer(text):
            labels[match.group(1) or match.group(2)].add(rel)
    return labels


def _labels_outside(label_files: dict[str, set[str]], exclude_files: set[str]) -> set[str]:
    return {label for label, files in label_files.items() if files - exclude_files}


def _existing_labels(exclude_files: set[str] | None = None) -> set[str]:
    return _labels_outside(_label_files(), exclude_files or set())


def _make_unique_slug(
    part: str,
    chapter_title: str,
    packet_base: str,
    existing_files: set[str],
    used_slugs: set[str],
    used_owned_files: set[str],
) -> str:
    base = f"{_slugify(chapter_title)}-{packet_base}"
    slug = base
    n = 2
    while (
        slug in used_slugs
        or any(
            path in existing_files or path in used_owned_files
            for path in _owned_files(part, slug)
        )
    ):
        slug = f"{base}-{n}"
        n += 1
    used_slugs.add(slug)
    used_owned_files.update(_owned_files(part, slug))
    return slug


def _label_tag_taken(tag: str, labels: set[str], used_tags: set[str]) -> bool:
    if tag in used_tags:
        return True
    for label in labels:
        suffix = label.split(":", 1)[1] if ":" in label else label
        if suffix == tag or suffix.startswith(tag + "-"):
            return True
    return False


def _make_label_tag(part: str, short: str, labels: set[str], used_tags: set[str]) -> str:
    part_lower = _part_dir(part)
    base = f"{part_lower}-{short}"
    label = base
    n = 2
    while _label_tag_taken(label, labels, used_tags):
        label = f"{base}-{n}"
        n += 1
    used_tags.add(label)
    return label


def _owned_files(part: str, slug: str) -> list[str]:
    part_lower = _part_dir(part)
    if part == "P13":
        body = f"handbook/parts/{part_lower}/presentations/{slug}.tex"
    else:
        body = f"handbook/parts/{part_lower}/{slug}.tex"
    return [
        body,
        f"handbook/annex/{part_lower}/{slug}.tex",
        f"handbook/bib/intake-{part_lower}-{slug}.bib",
        f"handbook/registry/symbols-intake-{part_lower}-{slug}.csv",
        f"spec/research/edition-2026-{part_lower}-{slug}.md",
        f"spec/research/edition-2026-{part_lower}-{slug}-return.json",
    ]


def _own_waves(wave: str, keep: str | None = None) -> set[str]:
    """The wave and its a/b sub-waves, minus any member already integrated (its directory holds an
    INTEGRATED marker) other than `keep` (default: `wave`): an integrated wave's packets no longer
    own their files."""
    keep = wave if keep is None else keep
    family = {wave, f"{wave}a", f"{wave}b"}
    return {w for w in family if w == keep or not (_root(WAVES_ROOT) / w / "INTEGRATED").is_file()}


def _packet_owned_files_and_tags(
    *,
    only_waves: set[str] | None = None,
    skip_waves: set[str] | None = None,
) -> tuple[set[str], set[str]]:
    owned: set[str] = set()
    tags: set[str] = set()
    base = _root(WAVES_ROOT)
    if not base.is_dir():
        return owned, tags
    for path in sorted(base.glob("*/packets/*.json")):
        wave_dir = path.parent.parent.name
        if only_waves is not None and wave_dir not in only_waves:
            continue
        if skip_waves is not None and wave_dir in skip_waves:
            continue
        data = _load_json(path, None)
        if not isinstance(data, dict):
            continue
        for item in data.get("owned_files") or []:
            if isinstance(item, str):
                normalized = _try_normalize_repo_path(item)
                if normalized:
                    owned.add(normalized)
        tag = data.get("label_tag")
        if isinstance(tag, str) and tag:
            tags.add(tag)
    return owned, tags


def _driver_paths() -> set[str]:
    result = set(FROZEN_EXPLICIT)
    for prefix in ("handbook/parts", "handbook/annex"):
        base = _root(prefix)
        if not base.is_dir():
            continue
        for path in base.glob("p*.tex"):
            result.add(path.relative_to(ROOT).as_posix())
        for path in base.glob("p*-route.tex"):
            result.add(path.relative_to(ROOT).as_posix())
    return result


def _retained_reader_files() -> set[str]:
    tools_dir = str(_root("tools"))
    inserted = False
    try:
        if tools_dir not in sys.path:
            sys.path.insert(0, tools_dir)
            inserted = True
        import check  # type: ignore
    except Exception as exc:
        check_path = _root("tools/check.py")
        if check_path.is_file():
            raise UsageError(f"cannot import tools/check.py for retained-file refusal: {exc}") from exc
        fallback = Path(__file__).resolve().with_name("check.py")
        try:
            spec = importlib.util.spec_from_file_location("_waves_check_fallback", fallback)
            if spec is None or spec.loader is None:
                raise ImportError(f"cannot load {fallback}")
            check = importlib.util.module_from_spec(spec)  # type: ignore[assignment]
            spec.loader.exec_module(check)  # type: ignore[union-attr]
        except Exception as fallback_exc:
            raise UsageError(
                f"cannot import tools/check.py for retained-file refusal: {fallback_exc}"
            ) from fallback_exc
    finally:
        if inserted:
            try:
                sys.path.remove(tools_dir)
            except ValueError:
                pass
    retained = getattr(check, "HB_RETAINED_UNREACHABLE_READER_FILES", {})
    if isinstance(retained, dict):
        return {f"handbook/{_normalize_repo_path(key)}" for key in retained}
    raise UsageError("tools/check.py lacks HB_RETAINED_UNREACHABLE_READER_FILES")


def _host_ref_counts(packets: list[list[dict[str, Any]]]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for packet_rows in packets:
        hosts: set[str] = set()
        for row in packet_rows:
            for evidence in row.get("reader_evidence") or []:
                if isinstance(evidence, dict) and isinstance(evidence.get("path"), str):
                    normalized = _try_normalize_repo_path(evidence["path"])
                    if normalized:
                        hosts.add(normalized)
        counts.update(hosts)
    return counts


def _is_editable_host(path: str, counts: Counter[str], drivers: set[str], retained: set[str]) -> bool:
    rel = _try_normalize_repo_path(path)
    if rel is None:
        return False
    comparable = rel.casefold() if os.name == "nt" else rel
    count = sum(
        value for key, value in counts.items()
        if (key.casefold() if os.name == "nt" else key) == comparable
    )
    if count > 1:
        return False
    driver_set = {item.casefold() if os.name == "nt" else item for item in drivers}
    retained_set = {item.casefold() if os.name == "nt" else item for item in retained}
    if comparable in driver_set or comparable in retained_set:
        return False
    if _path_has_prefix(rel, "handbook/restoration") or _path_has_prefix(rel, "handbook/generated"):
        return False
    name = Path(rel).name
    name_cmp = name.casefold() if os.name == "nt" else name
    if name_cmp in {"main.tex", "handbook.sty", "frontmatter.tex"}:
        return False
    if re.fullmatch(r"p\d{2}(?:-route)?\.tex", name_cmp) and (
        _path_has_prefix(rel, "handbook/parts") or _path_has_prefix(rel, "handbook/annex")
    ):
        return False
    return _path_has_prefix(rel, "handbook") and rel.casefold().endswith(".tex")


URL_COMMAND_RE = re.compile(r"\\(?:url|path|nolinkurl|href)(?![A-Za-z@])\s*")


def _strip_tex_comments(line: str) -> str:
    """The line up to its first unescaped %. A % inside the argument of
    \\url, \\path, \\nolinkurl or \\href ({..} or |..| delimited, on this
    line) is part of the URL, not a comment."""
    out: list[str] = []
    i = 0
    while i < len(line):
        char = line[i]
        if char == "\\":
            match = URL_COMMAND_RE.match(line, i)
            if match and match.end() < len(line) and line[match.end()] not in "%\\":
                delimiter = line[match.end()]
                close = line.find("}" if delimiter == "{" else delimiter, match.end() + 1)
                if close != -1:
                    out.append(line[i : close + 1])
                    i = close + 1
                    continue
            out.append(line[i : i + 2])
            i += 2
            continue
        if char == "%":
            break
        out.append(char)
        i += 1
    return "".join(out)


def _input_target(raw: str) -> str | None:
    value = raw.strip().replace("\\", "/")
    if not value or value.startswith("/") or re.match(r"[A-Za-z]:", value):
        return None
    if any(part in {"", ".", ".."} for part in value.split("/")):
        return None
    if not value.endswith(".tex"):
        value += ".tex"
    return value


def _skip_ws(text: str, pos: int) -> int:
    while pos < len(text) and text[pos] in " \t\r\n":
        pos += 1
    return pos


def _group_end(text: str, pos: int) -> int | None:
    """End index after the group that opens at text[pos] with {, [ or (.

    Braces nest; a ] or ) closes only at brace depth zero; escaped characters
    are skipped. Returns None when the group is not closed.
    """
    if pos >= len(text) or text[pos] not in "{[(":
        return None
    close = {"{": "}", "[": "]", "(": ")"}[text[pos]]
    depth = 0
    i = pos
    while i < len(text):
        char = text[i]
        if char == "\\":
            i += 2
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if close == "}" and depth == 0:
                return i + 1
        elif char == close and depth == 0 and i > pos:
            return i + 1
        i += 1
    return None


def _line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


# Hook commands and what they do: "add" and "remove" open and close a
# bracket; "next" (AddToHookNext) leaves code pending for the next use.
HOOK_PRIMITIVES = {
    "AddToHook": "add",
    "RemoveFromHook": "remove",
    "AddToHookNext": "next",
    "hook_gput_code:nnn": "add",
    "hook_put_code:nnn": "add",
    "hook_gremove_code:nn": "remove",
    "hook_remove_code:nn": "remove",
    "hook_gput_next_code:nn": "next",
    "hook_put_next_code:nn": "next",
    "AddToHookWithArguments": "add",
    "AddToHookNextWithArguments": "next",
    "hook_gput_code_with_args:nnn": "add",
    "hook_put_code_with_args:nnn": "add",
    "hook_gput_next_code_with_args:nn": "next",
    "hook_put_next_code_with_args:nn": "next",
}
# \let\a\b, \let\a=\b, \NewCommandCopy\a\b and \cs_set_eq:NN \a \b.
ALIAS_RE = re.compile(
    r"\\(?:let|(?:New|Renew|Declare)CommandCopy|cs_(?:new|set|gset)_eq:NN)\s*"
    r"\{?\s*\\([A-Za-z@_:]+)\s*\}?\s*=?\s*\{?\s*\\([A-Za-z@_:]+)"
)
MACRO_DEF_RE = re.compile(
    r"\\(?P<xparse>(?:New|Renew|Provide|Declare)(?:Expandable)?DocumentCommand)?"
    r"(?(xparse)|(?:newcommand|renewcommand|providecommand|DeclareRobustCommand)\*?)\s*"
    r"(?:\{\s*\\(?P<n1>[A-Za-z@]+)\s*\}|\\(?P<n2>[A-Za-z@]+))"
    r"|\\[gex]?def\s*\\(?P<n3>[A-Za-z@]+)"
    # etoolbox \csdef{name}, and expl3 \cs_new:Npn \name (and set/gset,
    # protected, nopar, :Nn forms).
    r"|\\cs[gex]?def\s*\{\s*(?P<n4>[A-Za-z@]+)\s*\}"
    r"|\\cs_(?:new|set|gset)(?:_protected)?(?:_nopar)?:N[pn]*\s*\\(?P<n5>[A-Za-z@_:]+)"
)


def _macro_definitions(text: str) -> list[tuple[str, int, int, str]]:
    """(name, start, end, body) of macro definitions that have a brace body."""
    definitions: list[tuple[str, int, int, str]] = []
    for match in MACRO_DEF_RE.finditer(text):
        name = match.group("n1") or match.group("n2") or match.group("n3") or match.group("n4") or match.group("n5")
        pos = _skip_ws(text, match.end())
        if match.group("xparse"):
            # xparse: one brace group of argument specifiers, then the body.
            end = _group_end(text, pos) if pos < len(text) and text[pos] == "{" else None
            if end is None:
                continue
            pos = _skip_ws(text, end)
        while pos < len(text) and text[pos] == "[":
            end = _group_end(text, pos)
            if end is None:
                break
            pos = _skip_ws(text, end)
        if match.group("n3") or match.group("n5"):
            # TeX parameter text, delimited parameters included (\def\x#1.{..}),
            # runs to the first brace.
            while pos < len(text) and text[pos] != "{":
                pos += 2 if text[pos] == "\\" else 1
        while pos + 1 < len(text) and text[pos] == "#":
            pos = _skip_ws(text, pos + 2)
        end = _group_end(text, pos) if pos < len(text) and text[pos] == "{" else None
        if end is not None:
            definitions.append((name, match.start(), end, text[pos + 1 : end - 1]))
    return definitions


_HOOK_MACRO_CACHE: dict[str, Any] = {}

HookEvent = tuple[str, tuple[str, str]]


def _hook_events_in(text: str, effects: dict[str, list[HookEvent]]) -> list[tuple[int, str, tuple[str, str]]]:
    """(position, kind, key) of hook commands and of calls to hook macros in
    `text`, outside macro definitions and \\let-style alias definitions."""
    spans = [(start, end) for _name, start, end, _body in _macro_definitions(text)]
    spans += [(match.start(), match.end()) for match in ALIAS_RE.finditer(text)]

    def in_definition(pos: int) -> bool:
        return any(start <= pos < end for start, end in spans)

    commands = _hook_commands()
    name_re = _hook_name_re()
    token_re = re.compile(name_re.pattern + r"\s*\{([^{}]+)\}\s*(?:\[([^\]]*)\])?\s*(?:\{([^{}]*)\})?")
    events: list[tuple[int, str, tuple[str, str]]] = []
    for occurrence in name_re.finditer(text):
        if in_definition(occurrence.start()):
            continue
        primitive = commands[occurrence.group(1)]
        kind = HOOK_PRIMITIVES[primitive]
        match = token_re.match(text, occurrence.start())
        if match is None:
            # A hook key the parser cannot read (nested braces, no group):
            # added or pending code opens a bracket nothing closes, and such a
            # remove closes nothing (fail closed).
            if kind != "remove":
                events.append((occurrence.start(), "add", (f"\0unreadable-{occurrence.start()}", "")))
            continue
        # LaTeX commands take the label as [..]; expl3 ones as the second {..}.
        if primitive.startswith("hook_"):
            label = match.group(4) if kind != "next" else ""
        else:
            label = match.group(3)
        events.append((match.start(), kind, (match.group(2).strip(), (label or "").strip())))
    if effects:
        call_re = re.compile(
            r"\\(" + "|".join(re.escape(name) for name in sorted(effects, key=len, reverse=True)) + r")(?![A-Za-z@])"
        )
        for match in call_re.finditer(text):
            if in_definition(match.start()):
                continue
            arguments = _call_arguments(text, match.end())
            for kind, key in effects[match.group(1)]:
                if "#" in key[0] + key[1]:
                    resolved = _substitute_parameters(key, arguments)
                    if resolved is None:
                        # Unknown arguments: such a remove closes nothing and
                        # such an add is never closed (fail closed).
                        if kind == "remove":
                            continue
                        resolved = (f"{key[0]}\0unresolved-{match.start()}-{len(events)}", key[1])
                    key = resolved
                events.append((match.start(), kind, key))
    return sorted(events, key=lambda item: item[0])


def _call_arguments(text: str, pos: int) -> list[str]:
    """The brace-group arguments that follow a macro call. A following [..]
    (an optional argument) makes them unknown: an empty list."""
    arguments: list[str] = []
    while True:
        start = _skip_ws(text, pos)
        if start >= len(text) or text[start] != "{" or len(arguments) == 9:
            break
        end = _group_end(text, start)
        if end is None:
            break
        arguments.append(text[start + 1 : end - 1].strip())
        pos = end
    if start < len(text) and text[start] == "[":
        return []
    return arguments


def _substitute_parameters(key: tuple[str, str], arguments: list[str]) -> tuple[str, str] | None:
    """A hook key with #1..#9 replaced by the call's arguments, or None when
    an argument is missing."""
    missing = False

    def replace(match: re.Match[str]) -> str:
        nonlocal missing
        index = int(match.group(1))
        if index > len(arguments):
            missing = True
            return match.group(0)
        return arguments[index - 1]

    resolved = (re.sub(r"#([1-9])", replace, key[0]), re.sub(r"#([1-9])", replace, key[1]))
    return None if missing else resolved


def _handbook_hook_texts() -> list[str]:
    """Comment-stripped text of every .tex and .sty file under handbook/."""
    cache_key = f"texts:{ROOT}"
    if cache_key not in _HOOK_MACRO_CACHE:
        base = _root("handbook")
        paths = sorted(base.rglob("*.tex")) + sorted(base.glob("*.sty")) if base.is_dir() else []
        texts: list[str] = []
        for path in paths:
            try:
                texts.append(_tex_text_without_comments(_read_text(path)))
            except (OSError, UnicodeDecodeError):
                continue
        _HOOK_MACRO_CACHE[cache_key] = texts
    return _HOOK_MACRO_CACHE[cache_key]


def _hook_aliases() -> dict[str, str]:
    """alias -> target of every \\let-style copy under handbook/."""
    cache_key = f"aliases:{ROOT}"
    if cache_key not in _HOOK_MACRO_CACHE:
        aliases: dict[str, str] = {}
        for text in _handbook_hook_texts():
            for match in ALIAS_RE.finditer(text):
                if match.group(1) != match.group(2):
                    aliases[match.group(1)] = match.group(2)
        _HOOK_MACRO_CACHE[cache_key] = aliases
    return _HOOK_MACRO_CACHE[cache_key]


def _resolve_aliases(known: dict[str, Any]) -> dict[str, Any]:
    """`known` extended with every alias (or alias of an alias) of its names."""
    result = dict(known)
    changed = True
    while changed:
        changed = False
        for alias, target in _hook_aliases().items():
            if target in result and alias not in result:
                result[alias] = result[target]
                changed = True
    return result


def _hook_name_re() -> re.Pattern[str]:
    """A hook command name (a primitive or an alias of one)."""
    names = sorted(_hook_commands(), key=len, reverse=True)
    return re.compile(r"\\(" + "|".join(re.escape(name) for name in names) + r")(?![A-Za-z@_:])")


def _hook_commands() -> dict[str, str]:
    """Hook command name -> the primitive it is (itself, or via aliases)."""
    cache_key = f"commands:{ROOT}"
    if cache_key not in _HOOK_MACRO_CACHE:
        _HOOK_MACRO_CACHE[cache_key] = _resolve_aliases({name: name for name in HOOK_PRIMITIVES})
    return _HOOK_MACRO_CACHE[cache_key]


def _hook_macro_effects() -> dict[str, list[HookEvent]]:
    """Macros anywhere in handbook/ whose expansion adds or removes hook code.

    Drivers switch hook brackets on and off through such macros (for example
    \\hbsourcepSevenHooksOn and \\hbsourcepSevenHooksOff), so a call counts as
    the AddToHook / RemoveFromHook commands it expands to, including those of
    macros it calls in turn.
    """
    cache_key = f"macros:{ROOT}"
    if cache_key in _HOOK_MACRO_CACHE:
        return _HOOK_MACRO_CACHE[cache_key]
    bodies: dict[str, str] = {}
    # Definitions the parser cannot read (no brace body found) with a hook
    # command after them, before the next definition: their effect is unknown,
    # so a call opens a bracket nothing closes (fail closed).
    unreadable: set[str] = set()
    name_re = _hook_name_re()
    for text in _handbook_hook_texts():
        definitions = _macro_definitions(text)
        parsed = {start for _name, start, _end, _body in definitions}
        for name, _start, _end, body in definitions:
            bodies[name] = body
        matches = list(MACRO_DEF_RE.finditer(text))
        for index, match in enumerate(matches):
            if match.start() in parsed:
                continue
            stop = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            if name_re.search(text, match.end(), stop):
                unreadable.add(next(name for name in match.group("n1", "n2", "n3", "n4", "n5") if name))
    effects: dict[str, list[HookEvent]] = {}
    resolving: set[str] = set()
    # expl3 names may contain _ and :; outside expl3 a name ends at its letters.
    call_re = re.compile(r"\\([A-Za-z@]+)([A-Za-z@_:]*)")

    def resolve(name: str) -> list[HookEvent]:
        if name in effects:
            return effects[name]
        if name in resolving:
            return []  # a recursive macro: its own hook commands are counted once
        resolving.add(name)
        body = bodies[name]
        callees = {
            callee
            for m in call_re.finditer(body)
            for callee in [m.group(1) + m.group(2) if m.group(1) + m.group(2) in bodies else m.group(1)]
            if callee in bodies and callee != name
        }
        inner = {callee: resolve(callee) for callee in sorted(callees)}
        resolving.discard(name)
        result = [(kind, key) for _pos, kind, key in _hook_events_in(body, {k: v for k, v in inner.items() if v})]
        effects[name] = result
        return result

    for name in sorted(unreadable):
        effects[name] = [("add", (f"\0unreadable-definition-{name}", ""))]
    for name in sorted(bodies):
        resolve(name)
    effects = _resolve_aliases({name: items for name, items in effects.items() if items})
    _HOOK_MACRO_CACHE[cache_key] = effects
    return effects


def _end_line(text: str) -> int:
    return text.count("\n") + 2


def _file_hook_events(path: str, active: frozenset[str] = frozenset()) -> list[HookEvent]:
    """Net hook commands a file issues at top level when it is input, in order,
    including those of the files it inputs."""
    cache_key = f"file:{ROOT}:{path}"
    if cache_key in _HOOK_MACRO_CACHE:
        return _HOOK_MACRO_CACHE[cache_key]
    if path in active:
        raise Refusal(f"{path}: \\input cycle while resolving hook brackets")
    full = _root(path)
    if not full.is_file():
        return []
    text = _tex_text_without_comments(_read_text(full))
    events = [(pos, kind, key) for pos, kind, key in _hook_events_in(text, _hook_macro_effects())]
    inputs = _input_positions(text)
    for pos, target in inputs:
        for kind, key in _file_hook_events(f"handbook/{target}.tex", active | {path}):
            events.append((pos, kind, key))
    events.sort(key=lambda item: item[0])
    # Pending AddToHookNext code reaches the including file only when no later
    # input of this file can consume it.
    last_input = max((pos for pos, _target in inputs), default=-1)
    result = [(kind, key) for pos, kind, key in events if kind != "next" or pos >= last_input]
    _HOOK_MACRO_CACHE[cache_key] = result
    return result


def _input_positions(text: str) -> list[tuple[int, str]]:
    """(position, target without .tex) of each \\input or \\include outside
    macro definitions."""
    definitions = _macro_definitions(text)
    result: list[tuple[int, str]] = []
    for match in INPUT_RE.finditer(text):
        if any(start <= match.start() < end for _name, start, end, _body in definitions):
            continue
        target = _input_target(match.group(1) or match.group(2) or "")
        if target:
            result.append((match.start(), target.removesuffix(".tex")))
    return result


def _hook_ranges(path: str) -> list[tuple[int, int]]:
    """Line ranges (open, close) of AddToHook...RemoveFromHook brackets, and
    of pending AddToHookNext code up to and including the next input, which
    may consume it.

    Hook commands count when written directly (LaTeX or expl3 forms), through
    \\let aliases, when issued by a macro call, and when issued at top level
    by an input file. A bracket left open, or pending code with no later
    input, runs to the end of the file (fail closed).
    """
    full = _root(path)
    if not full.is_file():
        return []
    text = _tex_text_without_comments(_read_text(full))
    events = _hook_events_in(text, _hook_macro_effects())
    inputs = _input_positions(text)
    for pos, target in inputs:
        for kind, key in _file_hook_events(f"handbook/{target}.tex", frozenset({path})):
            events.append((pos, kind, key))
    events.sort(key=lambda item: item[0])
    open_hooks: dict[tuple[str, str], list[int]] = defaultdict(list)
    ranges: list[tuple[int, int]] = []
    last = _end_line(text)
    for pos, kind, key in events:
        line = _line_of(text, pos)
        if kind == "next":
            following = [input_pos for input_pos, _target in inputs if input_pos > pos]
            ranges.append((line, _line_of(text, following[0]) + 1 if following else last))
        elif kind == "add":
            open_hooks[key].append(line)
        elif open_hooks.get(key):
            ranges.append((open_hooks[key].pop(), line))
    for starts in open_hooks.values():
        ranges.extend((start, last) for start in starts)
    return ranges


def _group_ranges(path: str) -> list[tuple[int, int]]:
    """Line ranges of \\begingroup...\\endgroup, of environments and of
    outermost brace groups.

    An unmatched closer means the file starts inside the group; an unclosed
    opener runs to the end of the file (both fail closed).
    """
    full = _root(path)
    if not full.is_file():
        return []
    text = _tex_text_without_comments(_read_text(full))
    ranges: list[tuple[int, int]] = []
    groups: list[int] = []
    envs: list[tuple[str, int]] = []
    token_re = re.compile(r"\\(begingroup|endgroup)(?![A-Za-z@])|\\(begin|end)\s*\{([^{}]+)\}")
    for match in token_re.finditer(text):
        line = _line_of(text, match.start())
        if match.group(1) == "begingroup":
            groups.append(line)
        elif match.group(1) == "endgroup":
            ranges.append((groups.pop() if groups else 0, line))
        elif match.group(3).strip() == "document":
            continue  # the document body is where content goes, not a bracket
        elif match.group(2) == "begin":
            envs.append((match.group(3).strip(), line))
        else:
            name = match.group(3).strip()
            start = 0
            while envs:
                env, env_start = envs.pop()
                if env == name:
                    start = env_start
                    break
            ranges.append((start, line))
    last = _end_line(text)
    ranges.extend((start, last) for start in groups)
    ranges.extend((start, last) for _env, start in envs)
    ranges.extend(_brace_group_ranges(text))
    return [(start, end) for start, end in ranges if end > start]


def _brace_group_ranges(text: str) -> list[tuple[int, int]]:
    """Line ranges of outermost {..} groups (escaped braces skipped)."""
    ranges: list[tuple[int, int]] = []
    depth = 0
    line = 1
    open_line = 0
    i = 0
    while i < len(text):
        char = text[i]
        if char == "\\":
            if text[i + 1 : i + 2] == "\n":
                line += 1
            i += 2
            continue
        if char == "\n":
            line += 1
        elif char == "{":
            if depth == 0:
                open_line = line
            depth += 1
        elif char == "}":
            if depth == 0:
                ranges.append((0, line))
            else:
                depth -= 1
                if depth == 0:
                    ranges.append((open_line, line))
        i += 1
    if depth > 0:
        ranges.append((open_line, _end_line(text)))
    return ranges


def _protected_ranges(path: str) -> list[tuple[int, int]]:
    return sorted(_hook_ranges(path) + _group_ranges(path))


def _line_inside_ranges(path: str, line: int) -> bool:
    """True if content inserted after `line` would sit inside a bracket."""
    return any(start <= line < end for start, end in _protected_ranges(path))


INPUT_RE = re.compile(r"\\(?:input|include)\s*(?:\{([^{}]+)\}|([^\s%{}]+))")


def _host_inputs(path: str) -> list[tuple[int, str]]:
    """(line, target without .tex) for every \\input or \\include in a file."""
    full = _root(path)
    if not full.is_file():
        return []
    result: list[tuple[int, str]] = []
    for line_no, line in enumerate(_read_text(full).splitlines(), 1):
        for match in INPUT_RE.finditer(_strip_tex_comments(line)):
            target = _input_target(match.group(1) or match.group(2) or "")
            if target:
                result.append((line_no, target.removesuffix(".tex")))
    return result


def _anchor_after(host: str, line: int) -> dict[str, Any]:
    """The insertion anchor at or after `line` in `host`.

    The anchor is an input line that is unique in the host and outside every
    hook bracket, group and environment. If `line` is inside one, the anchor
    moves to the first input after it; when there is none, refuse.
    """
    ranges = _protected_ranges(host)
    inputs = _host_inputs(host)
    counts = Counter(raw for _line, raw in inputs)
    for input_line, raw in inputs:
        if input_line < line:
            continue
        if any(start <= input_line < end for start, end in ranges):
            continue
        if counts[raw] != 1:
            raise Refusal(f"{host}: anchor \\input{{{raw}}} is not unique")
        return {"host": host, "after_line": input_line, "after_input": raw}
    raise Refusal(f"{host}: no \\input at or after line {line} lies outside a hook bracket or group")


def _last_anchor_in(host: str) -> dict[str, Any]:
    ranges = _protected_ranges(host)
    inputs = _host_inputs(host)
    counts = Counter(raw for _line, raw in inputs)
    for input_line, raw in reversed(inputs):
        if any(start <= input_line < end for start, end in ranges):
            continue
        if counts[raw] != 1:
            raise Refusal(f"{host}: anchor \\input{{{raw}}} is not unique")
        return {"host": host, "after_line": input_line, "after_input": raw}
    raise Refusal(f"{host}: no \\input lies outside a hook bracket or group")


@dataclass
class InputEdge:
    host: str
    target: str
    line: int
    raw: str


def _build_input_edges() -> tuple[dict[str, list[InputEdge]], dict[str, int]]:
    base = _root("handbook")
    parents: dict[str, list[InputEdge]] = defaultdict(list)
    route_order: dict[str, int] = {}
    active: set[str] = set()

    def visit(rel: str) -> None:
        if rel in route_order or rel in active:
            return
        active.add(rel)
        route_order[rel] = len(route_order)
        if (base / rel).is_file():
            for line_number, raw in _host_inputs(f"handbook/{rel}"):
                target = f"{raw}.tex"
                parents[f"handbook/{target}"].append(
                    InputEdge(host=f"handbook/{rel}", target=f"handbook/{target}", line=line_number, raw=raw)
                )
                visit(target)
        active.remove(rel)

    if (base / "main.tex").is_file():
        visit("main.tex")
    return parents, {f"handbook/{key}": value for key, value in route_order.items()}


def _part_drivers(part: str, *, annex: bool) -> list[str]:
    part_lower = _part_dir(part)
    if annex:
        return [f"handbook/annex/{part_lower}-route.tex", f"handbook/annex/{part_lower}.tex"]
    return [f"handbook/parts/{part_lower}.tex"]


def _routed_driver(part: str, route_order: dict[str, int], *, annex: bool) -> str:
    for driver in _part_drivers(part, annex=annex):
        if driver in route_order and _root(driver).is_file():
            return driver
    raise Refusal(f"no routed {'annex' if annex else 'body'} driver for {part}")


def _protected_reader_path(path: str) -> bool:
    return _path_has_prefix(path, "handbook/restoration") or _path_has_prefix(path, "handbook/generated")


def _in_part_zone(path: str, part: str, *, annex: bool) -> bool:
    zone = "annex" if annex else "parts"
    return path in _part_drivers(part, annex=annex) or path.startswith(f"handbook/{zone}/{_part_dir(part)}/")


def _edge_in_packet_part(edge: InputEdge, part: str, *, annex: bool) -> bool:
    if not _in_part_zone(edge.host, part, annex=annex):
        return False
    return _in_part_zone(edge.target, part, annex=annex) or _protected_reader_path(edge.target)


def _route_chains(rel: str, parents: dict[str, list[InputEdge]]) -> list[list[InputEdge]]:
    """Every complete input chain from `rel` up to handbook/main.tex."""
    chains: list[list[InputEdge]] = []

    def walk(node: str, chain: list[InputEdge], seen: set[str]) -> None:
        if node == "handbook/main.tex":
            if chain:
                chains.append(chain)
            return
        for edge in parents.get(node, []):
            if edge.host not in seen:
                walk(edge.host, chain + [edge], seen | {edge.host})

    walk(rel, [], {rel})
    return chains


def _anchor_from_chain(chain: list[InputEdge], part: str, *, annex: bool) -> dict[str, Any] | None:
    """Anchor for an evidence file reached by `chain` (evidence end first).

    The anchor is the lowest input edge of the packet's own part whose host is
    outside restoration/ and generated/. If any higher edge of the part sits
    inside a hook bracket or group, everything below it does too, so the anchor
    moves up to that edge and then out of the bracket in that host.
    """
    selected: InputEdge | None = None
    for edge in chain:
        in_part = _edge_in_packet_part(edge, part, annex=annex)
        if selected is None:
            if in_part and not _protected_reader_path(edge.host):
                selected = edge
            continue
        if in_part and _protected_reader_path(edge.host):
            raise Refusal(f"input of {edge.target} sits inside protected host {edge.host}")
        if _line_inside_ranges(edge.host, edge.line):
            if not in_part:
                # Every edge up to main.tex counts: a bracket outside the part
                # encloses the whole part, and no anchor in it can escape.
                raise Refusal(f"{edge.host}:{edge.line}: \\input{{{edge.raw}}} lies inside a hook bracket or group")
            selected = edge
    if selected is None:
        return None
    return _anchor_after(selected.host, selected.line)


def _evidence_paths(rows: list[dict[str, Any]]) -> list[str]:
    paths: list[str] = []
    for row in rows:
        for evidence in row.get("reader_evidence") or []:
            if isinstance(evidence, dict) and isinstance(evidence.get("path"), str):
                rel = _try_normalize_repo_path(evidence["path"])
                if rel is not None:
                    paths.append(rel)
    return _dedupe(paths)


def _candidate_anchors(
    rows: list[dict[str, Any]],
    parents: dict[str, list[InputEdge]],
    route_order: dict[str, int],
    *,
    part: str,
    annex: bool,
) -> list[dict[str, Any]]:
    evidence = _evidence_paths(rows)
    if annex:
        # Annex order follows body order: the annex counterpart of each body
        # evidence file is an annex anchor candidate too.
        prefix = f"handbook/parts/{_part_dir(part)}/"
        counterparts = [
            f"handbook/annex/{_part_dir(part)}/{rel[len(prefix):]}"
            for rel in evidence
            if rel.startswith(prefix)
        ]
        evidence = _dedupe(
            [rel for rel in evidence if _path_has_prefix(rel, "handbook/annex")]
            + [rel for rel in counterparts if rel in route_order]
        )
    else:
        evidence = [
            rel for rel in evidence
            if _path_has_prefix(rel, "handbook/parts")
            or _protected_reader_path(rel)
        ]
    anchors: dict[tuple[str, int], dict[str, Any]] = {}
    for rel in evidence:
        found = False
        chains = _route_chains(rel, parents)
        for chain in chains:
            anchor = _anchor_from_chain(chain, part, annex=annex)
            if anchor is not None:
                found = True
                anchors[(anchor["host"], anchor["after_line"])] = anchor
        touches_part = any(
            _in_part_zone(edge.host, part, annex=annex) for chain in chains for edge in chain
        )
        if not found and touches_part and _protected_reader_path(rel):
            raise Refusal(f"no insertion ancestor outside restoration/generated for {rel}")

    return sorted(anchors.values(), key=lambda anchor: _anchor_route_key(anchor, route_order))


def _anchor_route_key(anchor: dict[str, Any], route_order: dict[str, int]) -> tuple[int, int]:
    target = f"handbook/{anchor['after_input']}.tex"
    return route_order.get(target, -1), int(anchor["after_line"])


def _chapter_sort_key(chapter_rows: list[dict[str, Any]], toc_order: dict[str, dict[str, Any]]) -> tuple[int, tuple[int, ...]]:
    if not chapter_rows:
        return 10_000_000, ()
    return min(_row_order(row, toc_order) for row in chapter_rows)


def _chapter_rows_for(
    rows: list[dict[str, Any]],
    part: str,
    all_rows: list[dict[str, Any]],
    toc_order: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    chapter = _chapter_id(min(rows, key=lambda row: _row_order(row, toc_order)))
    same = [row for row in all_rows if row.get("part") == part and _chapter_id(row) == chapter]
    return same or rows


def _route_subtree_end(rel: str, parents: dict[str, list[InputEdge]], route_order: dict[str, int]) -> int:
    """Largest route position among `rel` and the files it inputs."""
    children: dict[str, list[str]] = defaultdict(list)
    for target, edges in parents.items():
        for edge in edges:
            children[edge.host].append(target)
    end = route_order.get(rel, -1)
    stack = [rel]
    seen: set[str] = set()
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        end = max(end, route_order.get(node, -1))
        stack.extend(children.get(node, []))
    return end


def _body_counterpart(annex_input: str) -> str:
    """handbook/parts/... path of an annex input's same-named body file."""
    return "handbook/parts/" + annex_input.removeprefix("annex/") + ".tex"


def _annex_anchor_by_body_order(
    part: str,
    body_anchor: dict[str, Any],
    parents: dict[str, list[InputEdge]],
    route_order: dict[str, int],
) -> dict[str, Any] | None:
    """Anchor after the last routed annex file of the part whose body
    counterpart (same path under parts/) is routed at or before the body
    anchor's input (including the files that input pulls in)."""
    limit = _route_subtree_end(f"handbook/{body_anchor['after_input']}.tex", parents, route_order)
    annex_prefix = f"handbook/annex/{_part_dir(part)}/"
    body_prefix = f"handbook/parts/{_part_dir(part)}/"
    candidates = sorted(
        (
            rel for rel in route_order
            if rel.startswith(annex_prefix)
            and route_order.get(body_prefix + rel[len(annex_prefix):], limit + 1) <= limit
        ),
        key=lambda rel: route_order[rel],
        reverse=True,
    )
    for rel in candidates:
        anchors = _candidate_anchors(
            [{"reader_evidence": [{"path": rel}]}], parents, route_order, part=part, annex=True
        )
        if anchors:
            return anchors[-1]
    return None


def _annex_anchor_before_following(
    part: str,
    limit: int,
    parents: dict[str, list[InputEdge]],
    route_order: dict[str, int],
) -> dict[str, Any] | None:
    """When no annex file is known to precede the body anchor, the new annex
    goes before the first routed annex file whose body counterpart is known
    to follow it: after the annex file just before that one, or, when it is
    the part's first annex file, before it. No input precedes it then, so the
    anchor names the line before that input and the input it must precede
    (after_input is null). Returns None when no annex file has a known
    counterpart after the body anchor."""
    annex_prefix = f"handbook/annex/{_part_dir(part)}/"
    ordered = sorted((rel for rel in route_order if rel.startswith(annex_prefix)), key=route_order.__getitem__)

    def anchors_for(rel: str) -> list[dict[str, Any]]:
        return _candidate_anchors([{"reader_evidence": [{"path": rel}]}], parents, route_order, part=part, annex=True)

    for index, rel in enumerate(ordered):
        counterpart = "handbook/parts/" + rel.removeprefix("handbook/annex/")
        if route_order.get(counterpart, -1) <= limit:
            continue
        if index > 0:
            previous = anchors_for(ordered[index - 1])
            if previous:
                return previous[-1]
        own = anchors_for(rel)
        if not own:
            return None
        first = own[0]
        line = int(first["after_line"]) - 1
        if _line_inside_ranges(first["host"], line):
            raise Refusal(
                f"{first['host']}: the line before \\input{{{first['after_input']}}} lies inside a hook bracket or group"
            )
        return {"host": first["host"], "after_line": line, "after_input": None, "before_input": first["after_input"]}
    return None


def _insertion_for_rows(
    rows: list[dict[str, Any]],
    part: str,
    all_rows: list[dict[str, Any]],
    toc_order: dict[str, dict[str, Any]],
    parents: dict[str, list[InputEdge]],
    route_order: dict[str, int],
    *,
    annex: bool,
    body_anchor: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """After the last routed input among the chapter's evidence files, else the
    previous chapter's, else the part driver's last input.

    Without direct annex evidence in the chapter, the annex anchor follows body
    order: after the last annex input whose body counterpart precedes the body
    anchor in route order."""
    if annex and body_anchor is not None:
        # Annex order follows body order: never before the annex of a file
        # whose body precedes the body anchor, and never after chapter
        # evidence whose body counterpart comes after the body anchor.
        limit = _route_subtree_end(f"handbook/{body_anchor['after_input']}.tex", parents, route_order)
        chapter_rows = _chapter_rows_for(rows, part, all_rows, toc_order)
        options = [
            anchor
            for anchor in _candidate_anchors(chapter_rows, parents, route_order, part=part, annex=True)
            if route_order.get(_body_counterpart(anchor["after_input"]), -1) <= limit
        ]
        by_body = _annex_anchor_by_body_order(part, body_anchor, parents, route_order)
        if by_body is not None:
            options.append(by_body)
        if options:
            return max(options, key=lambda anchor: _anchor_route_key(anchor, route_order))
        before = _annex_anchor_before_following(part, limit, parents, route_order)
        if before is not None:
            return before
    first = min(rows, key=lambda row: _row_order(row, toc_order))
    chapter = _chapter_id(first)
    by_chapter: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in all_rows:
        if row.get("part") == part:
            by_chapter[_chapter_id(row)].append(row)
    current_key = _chapter_sort_key(by_chapter.get(chapter) or rows, toc_order)
    previous = sorted(
        (
            chapter_rows for other, chapter_rows in by_chapter.items()
            if other != chapter and _chapter_sort_key(chapter_rows, toc_order) < current_key
        ),
        key=lambda chapter_rows: _chapter_sort_key(chapter_rows, toc_order),
        reverse=True,
    )
    for chapter_rows in [by_chapter.get(chapter) or rows] + previous:
        anchors = _candidate_anchors(chapter_rows, parents, route_order, part=part, annex=annex)
        if anchors:
            return anchors[-1]
    driver = _routed_driver(part, route_order, annex=annex)
    for chain in _route_chains(driver, parents):
        for edge in chain:
            if _line_inside_ranges(edge.host, edge.line):
                raise Refusal(f"{edge.host}:{edge.line}: \\input{{{edge.raw}}} lies inside a hook bracket or group")
    return _last_anchor_in(driver)


def _first_heading(path: str, seen: set[str] | None = None) -> str | None:
    seen = set() if seen is None else seen
    full = _root(path)
    if not full.is_file():
        return None
    rel = _rel(full)
    if rel in seen:
        return None
    seen.add(rel)
    try:
        lines = _read_text(full).splitlines()
    except OSError:
        return None
    token_re = re.compile(
        r"\\(?:(chapter|section|subsection)\*?\s*[\[{]|(?:input|include)\s*(?:\{([^{}]+)\}|([^\s%{}]+)))"
    )
    for line in lines:
        stripped = _strip_tex_comments(line)
        for match in token_re.finditer(stripped):
            if match.group(1):
                return f"\\{match.group(1)}"
            target = _input_target(match.group(2) or match.group(3) or "")
            if target is None:
                continue
            heading = _first_heading(f"handbook/{target}", seen)
            if heading:
                return heading
    return None


def _heading_level(part: str, insertion: dict[str, Any]) -> str:
    host = _handbook_rel(str(insertion.get("body", {}).get("host", "")))
    after_input = insertion.get("body", {}).get("after_input")
    flat = {
        "parts/p11.tex",
        "parts/p13.tex",
        "parts/p15.tex",
        "parts/p16.tex",
        "parts/p17.tex",
        "parts/p18.tex",
        "parts/p19.tex",
        "parts/p12/automation-and-mechanization.tex",
    }
    section_hosts = {
        "parts/p02/first-order-logic.tex",
        "parts/p03/classification-theory.tex",
        "parts/p03/preservation-abstract-logic.tex",
        "parts/p07/lambda-calculi-and-type-theories.tex",
        "parts/p12/rewriting.tex",
    }
    subsection_hosts = {
        "parts/p09/logic-in-computer-science.tex",
        "parts/p10/algebraic-and-categorical-logic.tex",
        "parts/p04/frontiers-of-computability.tex",
    }
    if host in flat:
        return "\\chapter"
    if host in section_hosts:
        return "\\section"
    if host in subsection_hosts:
        return "\\subsection"
    if re.fullmatch(r"parts/p\d{2}\.tex", host):
        # Mixed drivers (p01-p08, p12, p14, and any other non-flat driver):
        # match the neighbouring sibling's first heading, through its inputs.
        # The sibling before the anchor comes first, then the one after it;
        # a sibling without a heading continues the nearest earlier one.
        siblings = [raw for _line, raw in _host_inputs(f"handbook/{host}")]
        if after_input in siblings:
            idx = siblings.index(after_input)
            order = [idx, idx + 1] + list(range(idx - 1, -1, -1))
            for position in order:
                if 0 <= position < len(siblings):
                    heading = _first_heading(f"handbook/{siblings[position]}.tex")
                    if heading:
                        return heading
        raise Refusal(f"cannot determine heading level from the siblings of {after_input!r} in {host}")
    host_heading = _first_heading(f"handbook/{host}")
    if host_heading == "\\chapter":
        return "\\section"
    if host_heading == "\\section":
        return "\\subsection"
    if host_heading:
        return host_heading
    raise Refusal(f"cannot determine heading level from host {host!r}")


def _destination_paths(unit: dict[str, Any]) -> list[str]:
    result: list[str] = []

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            for key in ("path", "proposed_path", "body_path", "local_path"):
                raw = value.get(key)
                if isinstance(raw, str) and raw.endswith((".tex", ".md", ".bib", ".csv")):
                    result.append(_normalize_repo_path(raw))
            for child in value.values():
                if isinstance(child, (dict, list)):
                    walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(unit.get("destination"))
    seen: set[str] = set()
    out: list[str] = []
    for path in result:
        if path not in seen:
            seen.add(path)
            out.append(path)
    return out


def _labels_from_unit(unit: dict[str, Any]) -> list[str]:
    labels: list[str] = []

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            for key in ("label", "proposed_label", "entry_label", "anchor"):
                raw = value.get(key)
                if isinstance(raw, str) and ":" in raw:
                    labels.append(raw)
            for child in value.values():
                if isinstance(child, (dict, list)):
                    walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(unit.get("destination"))
    return sorted(set(labels))


LABEL_CONTEXT_RE = re.compile(r"(?<=[{,\[=])\s*([^\s{},\[\]=%\\]+)\s*(?=[},\]])")


def _label_context_index() -> dict[str, list[tuple[str, int]]]:
    """Every token in a label context ({L}, [L], {a,L}, =L}) of the handbook
    tree outside generated/, mapped to its (path, line) sites."""
    index: dict[str, list[tuple[str, int]]] = defaultdict(list)
    base = _root("handbook")
    if not base.is_dir():
        return index
    for path in sorted(base.rglob("*.tex")):
        rel = path.relative_to(ROOT).as_posix()
        if _path_has_prefix(rel, "handbook/generated"):
            continue
        try:
            text = _read_text(path)
        except (OSError, UnicodeDecodeError):
            continue
        for match in LABEL_CONTEXT_RE.finditer(text):
            index[match.group(1)].append((rel, text.count("\n", 0, match.start()) + 1))
    return index


def _grep_existing(
    labels: Iterable[str],
    files: Iterable[str],
    index: dict[str, list[tuple[str, int]]] | None = None,
) -> list[dict[str, Any]]:
    """Existing files, and whole-label occurrences in label contexts (\\label,
    \\ref, \\cref lists, \\hyperref[...], environment label arguments, status
    specs) outside handbook/generated/."""
    wanted = sorted({item for item in labels if item})
    wanted_files = sorted({_normalize_repo_path(item) for item in files if item})
    found: list[dict[str, Any]] = []
    for file in wanted_files:
        if _path_exists_rel(file):
            found.append({"kind": "file", "path": file})
    if not wanted:
        return found
    if index is None:
        index = _label_context_index()
    for label in wanted:
        for rel, line in dict.fromkeys(index.get(label, [])):
            found.append({"kind": "label-or-anchor", "label": label, "path": rel, "line": line})
    return found


def _packet_units(
    rows: list[dict[str, Any]],
    queue_units: dict[str, dict[str, Any]],
    held: HeldIndex,
    *,
    unit_ids: Iterable[str] | None = None,
) -> list[dict[str, Any]]:
    """Unit records of a packet. required_components lists every component
    with its conditions (assessors account each component id); `open` marks
    the ones the packet's rows name as open work, or every component of a
    unit no row links (unit-only packets: nothing accounts them yet)."""
    if unit_ids is None:
        unit_ids = [unit_id for row in rows for unit_id in _unit_ids_for_row(row)]
    result: list[dict[str, Any]] = []
    for unit_id in sorted(set(unit_ids)):
        unit = queue_units.get(unit_id, {"unit_id": unit_id})
        presentations = unit.get("source_presentations") or []
        open_ids: set[str] = set()
        for row in rows:
            if unit_id not in _unit_ids_for_row(row):
                continue
            row_open_ids, _row_fallback = _open_components_for_row(row, queue_units)
            open_ids.update(row_open_ids)
        linked = any(unit_id in _unit_ids_for_row(row) for row in rows)
        components = []
        for component in unit.get("required_components") or []:
            if isinstance(component, dict) and _component_id(component):
                components.append(
                    {
                        "id": _component_id(component),
                        "description": component.get("description"),
                        "success_condition": component.get("success_condition"),
                        "failure_condition": component.get("failure_condition"),
                        "open": _component_id(component) in open_ids or not linked,
                    }
                )
        result.append(
            {
                "unit_id": unit_id,
                "title": unit.get("title"),
                "required_components": components,
                "source_presentations": presentations,
                "held_paths": held.paths_for_presentations(presentations),
            }
        )
    return result


def _is_source_blocked(
    rows: list[dict[str, Any]],
    queue_units: dict[str, dict[str, Any]],
    held: HeldIndex,
    census: dict[str, str],
) -> bool:
    unit_ids = _dedupe(unit_id for row in rows for unit_id in _unit_ids_for_row(row))
    if not unit_ids:
        return False
    # Absent sources block a packet only when nothing else is owed: every open row has been
    # assessed (no unassessed scope) and every recorded duty is itself blocked_source. A
    # writable duty (e.g. a wrong locator in a held source), an assessment dispute or an
    # untyped legacy duty still needs an author or an assessor.
    for row in rows:
        if row.get("status") == AU:
            continue
        duties = row.get("missing_pieces") or []
        if row.get("status") == "unassessed" or row.get("unassessed_scope") or not duties:
            return False
        if any(not (isinstance(d, dict) and d.get("kind") == "blocked_source") for d in duties):
            return False
    for unit_id in unit_ids:
        # A facet unit missing from the queue has unknown sources: treat it as
        # absent (fail closed) unless the census says otherwise.
        unit = queue_units.get(unit_id)
        if unit is None:
            if census.get(unit_id) in {"full", "partial"}:
                return False
            continue
        if _unit_source_available(unit, held, census):
            return False
    return True


SOURCE_ID_KEYS = (
    "source_id",
    "source_ids",
    "source_key",
    "citation_key",
    "bibliography_key",
    "bibliographic_key",
    "bibkey",
    "bibkeys",
    "dblp_key",
    "benchmark_id",
    "benchmark_ids",
    "doi",
    "work_doi",
    "container_doi",
)


def _presentation_source_ids(presentation: dict[str, Any]) -> list[str]:
    """Real identifiers of a presentation (ids, citation keys, DOIs) for
    blocker and acquisition records; never titles, hashes, paths or notes."""
    ids: list[str] = []
    for key in SOURCE_ID_KEYS:
        ids.extend(_identity_strings_from_value(presentation.get(key)))
    for key in RECORD_KEYS:
        for record in _presentation_dicts(presentation.get(key)):
            for record_key in ("key", "citation_key", "source_id", "doi"):
                ids.extend(_identity_strings_from_value(record.get(record_key)))
    return _dedupe(ids)


def _unit_source_available(unit: dict[str, Any], held: HeldIndex, census: dict[str, str]) -> bool:
    if census.get(str(unit.get("unit_id"))) in {"full", "partial"}:
        return True
    presentations = _presentation_dicts(unit.get("source_presentations") or [])
    if not presentations:
        # No required source presentation: nothing can be absent or acquired.
        return True
    for presentation in presentations:
        if _presentation_available(presentation, held, census):
            return True
    return False


def _blocker_record(wave: str, rows: list[dict[str, Any]], queue_units: dict[str, dict[str, Any]]) -> dict[str, Any]:
    unit_ids = sorted({unit_id for row in rows for unit_id in _unit_ids_for_row(row)})
    sections = sorted({_section_id(row) for row in rows}, key=_natural_section_key)
    # Content-derived id: a rerun gives the same blocker the same id and can
    # never overwrite an unrelated record.
    digest = hashlib.sha256(",".join(sections).encode("utf-8")).hexdigest()[:12].upper()
    source_ids: set[str] = set()
    titles: set[str] = set()
    for unit_id in unit_ids:
        for presentation in _presentation_dicts(queue_units.get(unit_id, {}).get("source_presentations")):
            source_ids.update(_presentation_source_ids(presentation))
            titles.update(_identity_strings_from_value(presentation.get("title")))
    return {
        "id": f"ACQ-{wave.upper()}-{digest}",
        "wave": wave,
        "kind": "blocked_source",
        "status": "open",
        "sections": sections,
        "units": unit_ids,
        "source_ids": sorted(source_ids),
        "titles": sorted(titles),
        "reason": "required source presentations absent from held-sources and census is not full or partial",
    }


def _assessment_keys(row: dict[str, Any], queue_units: dict[str, dict[str, Any]]) -> dict[str, Any]:
    """The items both assessors must judge for a section: every required component of the row's
    facet units, and each recorded duty (MP-i = missing_pieces[i], US-i = unassessed_scope[i])."""
    components: list[str] = []
    for facet in row.get("source_facets") or []:
        unit = queue_units.get(facet.get("unit_id"), {}) if isinstance(facet, dict) else {}
        for comp in unit.get("required_components") or []:
            cid = comp.get("component_id") if isinstance(comp, dict) else None
            if cid and cid not in components:
                components.append(cid)
    text = lambda x: x.get("duty") if isinstance(x, dict) else str(x)  # noqa: E731
    duties = [{"duty_id": f"MP-{i}", "duty": text(x)} for i, x in enumerate(row.get("missing_pieces") or [])]
    duties += [{"duty_id": f"US-{i}", "duty": text(x)} for i, x in enumerate(row.get("unassessed_scope") or [])]
    return {"components": components, "duties": duties}


def _packet_summary_sections(rows: list[dict[str, Any]], queue_units: dict[str, dict[str, Any]] | None = None) -> list[dict[str, Any]]:
    return [
        {
            "section_id": _section_id(row),
            "title": _section_title(row),
            "status": row.get("status"),
            "missing_pieces": row.get("missing_pieces", []),
            "unassessed_scope": row.get("unassessed_scope", []),
            "reader_evidence": row.get("reader_evidence", []),
            "assessment_keys": _assessment_keys(row, queue_units or {}),
        }
        for row in sorted(rows, key=lambda r: _natural_section_key(_section_id(r)))
    ]


def _assign_lanes(packet_records: list[dict[str, Any]]) -> None:
    uf = UnionFind()
    # A unit shared by several packets has one writer: the first author packet listing it (else
    # the first packet). The others get it as a readonly unit (they cross-reference the owner's
    # treatment and do not write its components), so a broad unit no longer chains every packet
    # that touches it into one serial lane.
    unit_owner: dict[str, int] = {}
    for idx, packet in enumerate(packet_records):
        for unit in packet.get("units", []):
            unit_id = unit.get("unit_id")
            if unit_id and (unit_id not in unit_owner or (
                    packet.get("mode") == "author" and packet_records[unit_owner[unit_id]].get("mode") != "author")):
                unit_owner[unit_id] = idx
    host_owner: dict[str, int] = {}
    for idx, packet in enumerate(packet_records):
        uf.find(idx)
        readonly = {u.get("unit_id"): packet_records[unit_owner[u.get("unit_id")]]["id"]
                    for u in packet.get("units", []) if u.get("unit_id") and unit_owner[u.get("unit_id")] != idx}
        if readonly:
            packet["readonly_units"] = dict(sorted(readonly.items()))
        else:
            packet.pop("readonly_units", None)
        for host in packet.get("editable_hosts", []):
            if host in host_owner:
                uf.union(idx, host_owner[host])
            else:
                host_owner[host] = idx
    # A packet listing another packet's owned file or editable host (read-only,
    # for example a proposed destination shared by a split unit cluster) runs
    # in that packet's lane, never beside it.
    writable: dict[str, int] = {}
    for idx, packet in enumerate(packet_records):
        for rel in list(packet.get("owned_files") or []) + list(packet.get("editable_hosts") or []):
            if isinstance(rel, str):
                writable.setdefault(_path_key(rel), idx)
    for idx, packet in enumerate(packet_records):
        for rel in packet.get("readonly_hosts") or []:
            owner_idx = writable.get(_path_key(rel)) if isinstance(rel, str) else None
            if owner_idx is not None:
                uf.union(idx, owner_idx)
    group_order: dict[Any, int] = {}
    next_lane = 1
    for idx, packet in enumerate(packet_records):
        root = uf.find(idx)
        if root not in group_order:
            group_order[root] = next_lane
            next_lane += 1
        packet["lane"] = group_order[root]


def _packet_mode(packet: dict[str, Any]) -> str:
    return str(packet.get("mode") or "author")


def _packet_cost(packet: dict[str, Any]) -> int:
    """Worst-case agents: an accounting packet runs 2; an author packet runs
    one initial assessment block plus 2 per author block."""
    if _packet_mode(packet) in ACCOUNTING_MODES:
        return 2
    return 2 * int(packet.get("max_blocks") or 0) + 2


def _cap_violations(packet_records: list[dict[str, Any]], counts: dict[str, int]) -> list[str]:
    violations: list[str] = []
    for packet in packet_records:
        section_count = len(packet.get("sections") or [])
        component_total = counts[packet["id"]]
        if section_count > 4 or (component_total > 8 and section_count > 1):
            violations.append(
                f"{packet.get('id')}: sections={section_count} open_components={component_total}"
            )
    return violations


def _oversize_indivisible_packets(packet_records: list[dict[str, Any]], counts: dict[str, int]) -> list[str]:
    oversize: list[str] = []
    for packet in packet_records:
        section_count = len(packet.get("sections") or [])
        component_total = counts[packet["id"]]
        if section_count == 1 and component_total > 8:
            section = (packet.get("sections") or [{}])[0].get("section_id", "<unknown>")
            oversize.append(
                f"{packet.get('id')}: section={section} open_components={component_total}"
            )
    return oversize


def _lane_map(packet_records: list[dict[str, Any]]) -> dict[int, list[dict[str, Any]]]:
    lane_map: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for packet in packet_records:
        lane_map[int(packet["lane"])].append(packet)
    return lane_map


def _args_json_for_wave(wave: str, lane_map: dict[int, list[dict[str, Any]]]) -> dict[str, Any]:
    return {
        "wave": wave,
        "root": str(ROOT).replace("\\", "/"),
        "maxConcurrent": MAX_CONCURRENT,
        "agentBudget": AGENT_BUDGET,
        "lanes": [
            {
                "packets": [
                    {
                        "id": packet["id"],
                        "path": (WAVES_ROOT / wave / "packets" / f"{packet['id']}.json").as_posix(),
                        "part": packet["part"],
                        "mode": _packet_mode(packet),
                        "sections": [section["section_id"] for section in packet["sections"]],
                        "max_blocks": packet["max_blocks"],
                        # The workflow names a unit-only packet's work by these
                        # (and reads p.units only for unit_accounting packets).
                        **(
                            {"units": [str(unit.get("unit_id")) for unit in packet.get("units") or []]}
                            if _packet_mode(packet) == "unit_accounting"
                            else {}
                        ),
                    }
                    for packet in packets
                ]
            }
            for _, packets in sorted(lane_map.items())
        ],
    }


def _merge_records(
    existing: list[dict[str, Any]],
    incoming: list[dict[str, Any]],
    wave: str,
) -> list[dict[str, Any]]:
    """Merge sidecar records without losing any.

    An incoming record updates the existing record with the same id: the
    tool's fields are refreshed, fields only the existing record has (for
    example a human note) are kept, and a status other than open or
    superseded (for example acquired) is kept. Existing records without an id
    are kept as they are. Earlier open records of this wave that the current
    run no longer produces are kept and marked superseded.
    """
    incoming_by_id = {item["id"]: item for item in incoming}
    merged: list[dict[str, Any]] = []
    for item in existing:
        ident = item.get("id")
        if isinstance(ident, str) and ident in incoming_by_id:
            update = incoming_by_id.pop(ident)
            status = item.get("status", "open")
            item = {**item, **update}
            if status not in {"open", "superseded"}:
                item["status"] = status
        elif isinstance(ident, str) and item.get("wave") == wave and item.get("status", "open") == "open":
            item = {**item, "status": "superseded"}
        merged.append(item)
    merged.extend(item for item in incoming if item["id"] in incoming_by_id)
    return merged


def _read_jsonl_records(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    return [dict(item) for item in _iter_jsonl(path)]


def _packet_match_key(packet: dict[str, Any]) -> frozenset[str]:
    """What a rerun matches a packet by: its section ids, or for a packet
    without sections (unit_accounting) its unit ids."""
    sections = frozenset(str(s.get("section_id")) for s in packet.get("sections") or [] if isinstance(s, dict))
    if sections:
        return sections
    return frozenset(
        f"unit:{unit.get('unit_id')}" for unit in packet.get("units") or [] if isinstance(unit, dict)
    )


def _packet_base_id(packet_id: str, wave: str) -> str:
    """The id of a packet without a split-wave suffix (w02a-p01-001 -> w02-p01-001)."""
    match = re.fullmatch(re.escape(wave) + r"[ab]?(-p\d{2}-\d{3})", packet_id)
    return wave + match.group(1) if match else packet_id


def _packet_in_flight(packet_path: Path, packet_id: str) -> bool:
    """A packet is in flight once it has a snapshot (or a recorded snapshot
    digest) or a verdict."""
    wave_dir = packet_path.parent.parent
    if any((wave_dir / sub / f"{packet_id}.json").is_file() for sub in ("snapshots", "verdicts")):
        return True
    digests = _load_json(wave_dir / "snapshots" / "digests.json", {})
    return isinstance(digests, dict) and packet_id in digests


def _existing_wave_packets(wave: str) -> list[tuple[Path, dict[str, Any]]]:
    """Packet files already written for this wave and its split halves."""
    found: list[tuple[Path, dict[str, Any]]] = []
    for own in sorted(_own_waves(wave)):
        for path in sorted(_root(WAVES_ROOT / own / "packets").glob("*.json")):
            data = _load_json(path, None)
            if isinstance(data, dict) and isinstance(data.get("id"), str):
                found.append((path, data))
    return found


def _used_packet_numbers(wave: str) -> defaultdict[str, int]:
    """Highest packet number per part directory that any packet, snapshot or
    verdict of this wave (or its split halves) has used."""
    highest: defaultdict[str, int] = defaultdict(int)
    for own in _own_waves(wave):
        for sub in ("packets", "snapshots", "verdicts"):
            for path in _root(WAVES_ROOT / own / sub).glob("*.json"):
                match = re.fullmatch(re.escape(own) + r"-(p\d{2})-(\d{3})", path.stem)
                if match:
                    highest[match.group(1)] = max(highest[match.group(1)], int(match.group(2)))
    return highest


def _refuse_in_flight_changes(wave: str, plan: dict[str, set[str]], *, force: bool) -> None:
    """Refuse a write plan (wave directory -> packet ids it will hold) that
    would remove, move or renumber a packet with a snapshot or verdict."""
    if force:
        return
    displaced = [
        f"{path.parent.parent.name}/{data['id']}"
        for path, data in _existing_wave_packets(wave)
        if _packet_in_flight(path, str(data["id"]))
        and str(data["id"]) not in plan.get(path.parent.parent.name, set())
    ]
    if displaced:
        raise Refusal(
            "packets with a snapshot or verdict would be removed or reassigned: "
            + ", ".join(displaced)
            + " (pass --force to discard them)"
        )


def _write_wave_outputs(
    wave: str,
    packet_records: list[dict[str, Any]],
    blocked: list[dict[str, Any]],
    *,
    force: bool = False,
    write_args: bool = True,
) -> None:
    """Write a wave's packets, args.json and blocker sidecars. With
    write_args=False the wave keeps no args.json, so it is not runnable (the
    parent of a split wave, or the halves of an earlier split)."""
    wave_root = _root(WAVES_ROOT / wave)
    packet_dir = wave_root / "packets"
    packet_dir.mkdir(parents=True, exist_ok=True)
    expected = {f"{packet['id']}.json" for packet in packet_records}
    stale = [path for path in sorted(packet_dir.glob("*.json")) if path.name not in expected]
    in_flight = [path.stem for path in stale if _packet_in_flight(path, path.stem)]
    if in_flight and not force:
        raise Refusal(f"would remove packets with a snapshot or verdict: {', '.join(in_flight)} (pass --force)")
    for path in stale:
        path.unlink()
        print(f"removed stale: {_rel(path)}")
    for packet in packet_records:
        out = packet_dir / f"{packet['id']}.json"
        if out.is_file() and _packet_in_flight(out, str(packet["id"])) and not force:
            continue  # in flight: the packet stays exactly as snapshotted
        _write_json_atomic(out, packet)
    args_path = wave_root / "args.json"
    if write_args:
        _write_json_atomic(args_path, _args_json_for_wave(wave, _lane_map(packet_records)))
    elif args_path.is_file():
        args_path.unlink()
        print(f"removed: {_rel(args_path)}")
    blockers_path = wave_root / "blockers.jsonl"
    needs_path = wave_root / "acquisition-needs.json"
    existing_blockers = _read_jsonl_records(blockers_path)
    existing_needs_data = _load_json(needs_path, {}) if needs_path.is_file() else {}
    existing_needs = existing_needs_data.get("needs", []) if isinstance(existing_needs_data, dict) else []
    existing_needs = [item for item in existing_needs if isinstance(item, dict)]
    print(f"wrote: {(WAVES_ROOT / wave / 'packets').as_posix()} ({len(packet_records)} packet files)")
    if write_args:
        print(f"wrote: {(WAVES_ROOT / wave / 'args.json').as_posix()}")
    merged_blockers = _merge_records(existing_blockers, blocked, wave)
    if blocked or existing_blockers:
        _write_atomic(blockers_path, "".join(_json_line(item) + "\n" for item in merged_blockers))
        print(f"wrote: {(WAVES_ROOT / wave / 'blockers.jsonl').as_posix()}")
    if blocked or existing_needs:
        # A need carries its blocker's merged status (an acquired blocker
        # stays acquired).
        status_by_id = {item.get("id"): item.get("status") for item in merged_blockers}
        needs = [
            {
                "id": item["id"],
                "blocker_ref": item["id"],
                "wave": wave,
                "status": status_by_id.get(item["id"], item["status"]),
                "source_ids": item["source_ids"],
                "titles": item.get("titles", []),
                "units": item["units"],
                "sections": item["sections"],
            }
            for item in blocked
        ]
        _write_json_atomic(needs_path, {"wave": wave, "needs": _merge_records(existing_needs, needs, wave)})
        print(f"wrote: {(WAVES_ROOT / wave / 'acquisition-needs.json').as_posix()}")


def _retarget_packet_wave(packet: dict[str, Any], old_wave: str, new_wave: str) -> dict[str, Any]:
    updated = json.loads(json.dumps(packet))
    old_id = str(updated.get("id") or "")
    if old_id.startswith(old_wave):
        updated["id"] = new_wave + old_id[len(old_wave):]
    updated["wave"] = new_wave
    return updated


def _split_lanes_for_budget(lane_map: dict[int, list[dict[str, Any]]]) -> tuple[set[int], set[int]] | None:
    lane_items = [(lane, packets, sum(_packet_cost(packet) for packet in packets)) for lane, packets in sorted(lane_map.items())]
    if not lane_items:
        return set(), set()
    total = sum(item[2] for item in lane_items)
    if total > AGENT_BUDGET * 2:
        return None
    best: tuple[int, int] | None = None
    prefix = 0
    for idx in range(1, len(lane_items)):
        prefix += lane_items[idx - 1][2]
        suffix = total - prefix
        if prefix <= AGENT_BUDGET and suffix <= AGENT_BUDGET:
            score = abs(prefix - suffix)
            if best is None or score < best[0]:
                best = (score, idx)
    if best is None:
        return None
    split_at = best[1]
    first = {lane for lane, _, _ in lane_items[:split_at]}
    second = {lane for lane, _, _ in lane_items[split_at:]}
    return first, second


def _write_split_waves(
    wave: str,
    packet_records: list[dict[str, Any]],
    blocked: list[dict[str, Any]],
    *,
    apply: bool,
    force: bool = False,
) -> int:
    lane_map = _lane_map(packet_records)
    split = _split_lanes_for_budget(lane_map)
    if split is None:
        print(
            f"refusal: worst-case agent count cannot be split into two {AGENT_BUDGET}-agent halves",
            file=sys.stderr,
        )
        return 1
    first_lanes, second_lanes = split
    wave_a = f"{wave}a"
    wave_b = f"{wave}b"
    parts = [
        (wave_a, [packet for packet in packet_records if int(packet["lane"]) in first_lanes]),
        (wave_b, [packet for packet in packet_records if int(packet["lane"]) in second_lanes]),
    ]
    for child_wave, packets in parts:
        cost = sum(_packet_cost(packet) for packet in packets)
        print(f"split: {child_wave} packets={len(packets)} worst-case agents={cost}")
        if cost > AGENT_BUDGET:
            print(
                f"refusal: {child_wave} worst-case agent count {cost} exceeds {AGENT_BUDGET}",
                file=sys.stderr,
            )
            return 1
    children = [
        (child_wave, [_retarget_packet_wave(packet, wave, child_wave) for packet in packets])
        for child_wave, packets in parts
    ]
    plan = {child_wave: {str(packet["id"]) for packet in packets} for child_wave, packets in children}
    plan[wave] = set()
    _refuse_in_flight_changes(wave, plan, force=force)
    if not apply:
        print(f"dry-run: would write split waves {wave_a} and {wave_b}")
        return 0
    for child_wave, child_packets in children:
        _write_wave_outputs(child_wave, child_packets, [], force=force)
    # The parent keeps only its blocker sidecars: packets and args.json from
    # an earlier unsplit run must not stay runnable.
    _write_wave_outputs(wave, [], blocked, force=force, write_args=False)
    return 0


def _write_unplaced_units(wave: str, records: list[dict[str, Any]]) -> None:
    """Unlinked queue units whose part cannot be derived: no wave packetizes
    them, so I7 cannot close for them until the lead assigns a part or
    records residuals. Rewritten on every applied run (an empty list clears it)."""
    rel = WAVES_ROOT / wave / "unplaced-units.json"
    _write_json_atomic(
        _root(rel),
        {
            "wave": wave,
            "note": (
                "unlinked queue units with no derivable part; not packetized in any wave. "
                f"reason '{UNPLACED_MALFORMED}': the destination paths evidently name evident_parts "
                "but are malformed (repair the queue paths, e.g. with tools/find_fused_spaces.py); "
                f"reason '{UNPLACED_NO_PART}': nothing names a part"
            ),
            "units": records,
        },
    )
    print(f"wrote: {rel.as_posix()} ({len(records)} units)")


def _carry_section_ids(path: Path | None) -> list[str]:
    """Section ids carried over: a JSON list (or a rows/sections/carry/carry_over
    list) of section ids or of objects with a section_id."""
    if path is None:
        return []
    if not path.is_file():
        raise UsageError(f"--carry file does not exist: {path}")
    data = _load_json(path, None)
    items: list[Any] = []
    if isinstance(data, list):
        items = data
    elif isinstance(data, dict):
        for key in ("rows", "sections", "carry", "carry_over"):
            seq = data.get(key)
            if isinstance(seq, list):
                items.extend(seq)
    else:
        raise UsageError(f"--carry file is not a JSON list or object: {path}")
    ids: list[str] = []
    for item in items:
        section = item if isinstance(item, str) else _section_id(item) if isinstance(item, dict) else ""
        if not section:
            raise UsageError(f"--carry item without a section id: {item!r}")
        ids.append(section)
    return _dedupe(ids)


def packetize(args: argparse.Namespace) -> int:
    wave = args.wave
    if not re.fullmatch(r"w\d{2}[a-z]?", wave):
        raise UsageError("wave must look like w02 or w02a")
    parts = [part.strip().upper() for part in args.parts.split(",") if part.strip()]
    if not parts or any(not re.fullmatch(r"P(?:[1-9]|1[0-9])", part) for part in parts):
        raise UsageError("--parts must be a comma-separated list like P1,P2,P15")
    if args.apply and args.dry_run:
        raise UsageError("--apply and --dry-run are mutually exclusive")

    toc_order = _load_toc_order()
    rows = _load_ledger_rows()
    rows_by_section = {_section_id(row): row for row in rows}
    carried_rows: list[dict[str, Any]] = []
    for section in _carry_section_ids(Path(args.carry) if args.carry else None):
        row = rows_by_section.get(section)
        if row is None:
            raise UsageError(f"--carry section {section} is not in the ledger")
        carried_rows.append(row)
    part_rows = [row for row in rows if row.get("part") in parts]
    needed_units = {unit_id for row in part_rows + carried_rows for unit_id in _unit_ids_for_row(row)}
    linked_units = {unit_id for row in rows for unit_id in _unit_ids_for_row(row)}
    queue_units, unlinked_units = _scan_queue(needed_units, linked_units)
    # Open rows, plus authored_unreviewed rows that still need accounting
    # (parked scope, stale evidence hash, or no component accounting).
    selected: dict[str, dict[str, Any]] = {}
    for row in part_rows:
        if row.get("status") != AU or _au_accounting_reasons(row, queue_units):
            selected[_section_id(row)] = row
    carried_au: list[str] = []
    for row in carried_rows:
        section = _section_id(row)
        if row.get("status") == AU and section not in selected:
            reasons = _au_accounting_reasons(row, queue_units)
            if not reasons:
                carried_au.append(section)
                continue
        selected[section] = row
    open_rows = sorted(selected.values(), key=lambda row: _row_order(row, toc_order))
    if args.apply and not _root(HELD_SOURCES).is_file():
        # An in-memory index is a dry-run convenience only: applied packets and
        # blockers must rest on a recorded held-sources.json.
        raise Refusal(f"--apply needs {HELD_SOURCES.as_posix()}; build it with tools/held_sources.py build --apply")
    held = _load_held_sources()
    if not held.available:
        raise Refusal(f"held-sources index unavailable: {held.unavailable_reason}")
    census = _load_census(Path(args.census) if args.census else None)
    open_blocker_sections = _open_blocker_sections(_read_blockers())
    # An open blocker holds back authoring, not accounting: an
    # authored_unreviewed row it names still goes to an accounting packet of
    # its own (sources_held false), never into an author packet.
    skipped_for_blockers = [
        row for row in open_rows if _section_id(row) in open_blocker_sections and row.get("status") != AU
    ]
    blocker_au_rows = [row for row in open_rows if _section_id(row) in open_blocker_sections and row.get("status") == AU]
    open_rows = [row for row in open_rows if _section_id(row) not in open_blocker_sections]

    def chapters_of(chapter_source: list[dict[str, Any]]) -> list[list[dict[str, Any]]]:
        """The rows grouped by (part, chapter), chapters in TOC order."""
        grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
        for row in chapter_source:
            grouped[(str(row.get("part")), _chapter_id(row))].append(row)
        return [
            sorted(grouped[key], key=lambda row: _row_order(row, toc_order))
            for key in sorted(grouped, key=lambda k: min(_row_order(row, toc_order) for row in grouped[k]))
        ]

    raw_packets: list[list[dict[str, Any]]] = []
    for chapter_rows in chapters_of(open_rows):
        clusters = _clusters_for_chapter(chapter_rows)
        # Clusters of only authored_unreviewed rows pack apart (accounting
        # packets); a cluster with any open row is an author cluster.
        au_only = [c for c in clusters if all(row.get("status") == AU for row in c)]
        with_open = [c for c in clusters if not all(row.get("status") == AU for row in c)]
        raw_packets.extend(_bin_pack_chapter(with_open, queue_units, toc_order))
        raw_packets.extend(_bin_pack_chapter(au_only, queue_units, toc_order))

    blocked: list[dict[str, Any]] = []
    unblocked_packets: list[list[dict[str, Any]]] = []
    sources_absent: set[int] = set()
    for packet_rows in raw_packets:
        if all(row.get("status") == AU for row in packet_rows):
            # Accounting assesses text already present: the source gate does
            # not hold it back, but the packet records that its sources are
            # absent, so a downgrade cannot be authored without them.
            if _is_source_blocked(packet_rows, queue_units, held, census):
                sources_absent.add(id(packet_rows))
            unblocked_packets.append(packet_rows)
        elif _is_source_blocked(packet_rows, queue_units, held, census):
            # Only the open rows are blocked; the packet's authored_unreviewed
            # rows still go to accounting (sources absent).
            blocked.append(_blocker_record(wave, [r for r in packet_rows if r.get("status") != AU], queue_units))
            au_rows = [r for r in packet_rows if r.get("status") == AU]
            if au_rows:
                sources_absent.add(id(au_rows))
                unblocked_packets.append(au_rows)
        else:
            unblocked_packets.append(packet_rows)
    for chapter_rows in chapters_of(blocker_au_rows):
        for packet_rows in _bin_pack_chapter(_clusters_for_chapter(chapter_rows), queue_units, toc_order):
            sources_absent.add(id(packet_rows))
            unblocked_packets.append(packet_rows)

    # Packet ids are stable across reruns: a packet whose section set matches
    # an existing packet of this wave (or its split halves) keeps that packet's
    # id, owned files and label tag; a new packet gets the next unused number
    # of its part, never a number an earlier packet, snapshot or verdict used.
    existing_packets = _existing_wave_packets(wave)
    by_sections = {_packet_match_key(data): (path, data) for path, data in existing_packets}
    next_number = _used_packet_numbers(wave)
    own_owned_files, own_tags = _packet_owned_files_and_tags(only_waves=_own_waves(wave))
    wave_owned_files, wave_label_tags = _packet_owned_files_and_tags(skip_waves=_own_waves(wave))
    existing_files = {
        path.relative_to(ROOT).as_posix()
        for base in ("handbook", "spec/research")
        if _root(base).exists()
        for path in _root(base).rglob("*")
        if path.is_file()
    }
    used_owned_files = wave_owned_files | own_owned_files
    used_tags = wave_label_tags | own_tags
    used_slugs: set[str] = set()
    label_files = _label_files()
    labels = set(label_files)
    drivers = _driver_paths()
    retained = _retained_reader_files()
    parents, route_order = _build_input_edges()
    label_index = _label_context_index()

    # Unit-only packets: queue units of these parts that no ledger row links.
    unit_part: dict[str, str] = {}
    unplaced_units: list[str] = []
    for unit_id, unit in sorted(unlinked_units.items()):
        found_part = _unit_part(unit, parents)
        if found_part is None:
            unplaced_units.append(unit_id)
        elif found_part in parts:
            unit_part[unit_id] = found_part
    unit_packets = [
        (part, ids)
        for part in parts
        for ids in _pack_units([u for u in sorted(unit_part) if unit_part[u] == part], unlinked_units, drivers)
    ]
    unit_destinations = {unit_id: _unit_destinations(unlinked_units[unit_id]) for unit_id in unit_part}
    unit_lookups = {unit_id: _unit_lookup_paths(unlinked_units[unit_id]) for unit_id in unit_part}

    host_counts = _host_ref_counts(unblocked_packets)
    for _part, ids in unit_packets:
        host_counts.update({rel for unit_id in ids for rel in unit_destinations[unit_id][1] + unit_lookups[unit_id]})
    # A packet's owned file is never another packet's editable host.
    host_counts.update(own_owned_files)

    other_wave_owned_keys = {_path_key(item) for item in wave_owned_files}
    claimed_new: set[str] = set()

    def unit_new_files(part: str, ids: list[str]) -> list[str]:
        """Proposed destinations that do not exist yet and that no other
        packet owns: .tex files under handbook/parts|annex/<the packet's
        pNN>/, never under restoration/ or generated/ or a driver. A path
        proposed by units of two packets goes to the first; the others list
        it read-only (and share its lane)."""
        owned_new: list[str] = []
        for unit_id in ids:
            for rel in unit_destinations[unit_id][0]:
                key = _path_key(rel)
                if (
                    rel.endswith(".tex")
                    and re.fullmatch(rf"handbook/(?:parts|annex)/{_part_dir(part)}/.+", rel)
                    and not _path_has_prefix(rel, "handbook/restoration")
                    and not _path_has_prefix(rel, "handbook/generated")
                    and rel not in drivers
                    and rel not in existing_files
                    and key not in other_wave_owned_keys
                    and key not in claimed_new
                ):
                    claimed_new.add(key)
                    owned_new.append(rel)
        return owned_new

    plans: list[tuple[list[dict[str, Any]], str | None, list[str] | None]] = [
        (packet_rows, None, None) for packet_rows in unblocked_packets
    ] + [([], part, ids) for part, ids in unit_packets]

    def plan_match_key(packet_rows: list[dict[str, Any]], unit_ids: list[str] | None) -> frozenset[str]:
        if unit_ids is not None:
            return frozenset(f"unit:{unit_id}" for unit_id in unit_ids)
        return frozenset(_section_id(row) for row in packet_rows)

    # A reused packet keeps its owned files: claim them before any new unit
    # packet proposes the same new file (a later proposer lists it read-only).
    for packet_rows, _unit_only_part, unit_ids in plans:
        reused = by_sections.get(plan_match_key(packet_rows, unit_ids))
        if reused is not None:
            claimed_new.update(_path_key(rel) for rel in _packet_paths(reused[1], "owned_files"))

    packet_records: list[dict[str, Any]] = []
    component_counts: dict[str, int] = {}
    anchor_refusals: list[str] = []
    ownership_refusals: list[str] = []
    reused_ids: set[str] = set()
    kept_in_flight: list[str] = []
    for packet_rows, unit_only_part, unit_ids in plans:
        chapter: dict[str, Any] | None
        if unit_ids is not None:
            part = str(unit_only_part)
            chapter = None
            section_ids: list[str] = []
            mode = "unit_accounting"
            packet_unit_ids = sorted(unit_ids)
            unit_source = unlinked_units
            component_ids = _dedupe(cid for u in packet_unit_ids for cid in _unit_component_ids(unit_source[u]))
            component_total = len(component_ids)
            sources_held = any(_unit_source_available(unit_source[u], held, census) for u in packet_unit_ids)
        else:
            first = min(packet_rows, key=lambda row: _row_order(row, toc_order))
            part = str(first.get("part"))
            chapter = {
                "id": _chapter_id(first),
                "title": _chapter_title(first),
            }
            section_ids = [_section_id(row) for row in sorted(packet_rows, key=lambda r: _row_order(r, toc_order))]
            mode = "accounting" if all(row.get("status") == AU for row in packet_rows) else "author"
            packet_unit_ids = sorted({u for row in packet_rows for u in _unit_ids_for_row(row)})
            unit_source = queue_units
            component_ids = _dedupe(
                cid for u in packet_unit_ids for cid in _unit_component_ids(unit_source.get(u, {}))
            )
            component_total = _cluster_component_count(packet_rows, queue_units)
            sources_held = id(packet_rows) not in sources_absent
        match = by_sections.get(plan_match_key(packet_rows, unit_ids))
        if match is not None:
            match_path, match_data = match
            packet_id = _packet_base_id(str(match_data["id"]), wave)
            # Reused from a packet JSON (outside the G1 scan): check it again.
            reuse_problems = _owned_form_problems(part, packet_id, wave, match_data.get("owned_files"), mode)
            if reuse_problems:
                ownership_refusals.extend(f"{match_data['id']}: {item}" for item in reuse_problems)
                continue
            owned = [_normalize_repo_path(item) for item in match_data.get("owned_files") or []]
            label_tag = str(match_data.get("label_tag") or "")
            reused_ids.add(packet_id)
            component_counts[packet_id] = component_total
            if _packet_in_flight(match_path, str(match_data["id"])) and not getattr(args, "force", False):
                # In flight (snapshot or verdict): keep the packet as written.
                kept_in_flight.append(str(match_data["id"]))
                packet_records.append({**match_data, "id": packet_id, "wave": wave})
                continue
        else:
            part_dir = _part_dir(part)
            next_number[part_dir] += 1
            packet_id = f"{wave}-{part_dir}-{next_number[part_dir]:03d}"
            label_tag = _make_label_tag(part, packet_id, labels, used_tags)
            if unit_ids is not None:
                owned = unit_new_files(part, packet_unit_ids)
            else:
                slug = _make_unique_slug(
                    part,
                    chapter["title"] if chapter else "",
                    packet_id,
                    existing_files,
                    used_slugs,
                    used_owned_files,
                )
                owned = _owned_files(part, slug)

        if unit_ids is not None:
            # Existing and lookup destinations are hosts; a proposed path this
            # packet does not own (another packet's, another part's, or not a
            # writable destination) is read-only, as is any host not on disk.
            owned_keys = {_path_key(rel) for rel in owned}

            def unit_hosts(unit_id: str) -> list[str]:
                return [
                    rel
                    for rel in unit_destinations[unit_id][0] + unit_destinations[unit_id][1] + unit_lookups[unit_id]
                    if _path_key(rel) not in owned_keys
                ]

            host_paths = {rel for u in packet_unit_ids for rel in unit_hosts(u)}
        else:
            host_paths = {
                normalized
                for row in packet_rows
                for evidence in row.get("reader_evidence") or []
                if isinstance(evidence, dict)
                and isinstance(evidence.get("path"), str)
                for normalized in [_try_normalize_repo_path(evidence["path"])]
                if normalized is not None
            }
        evidence_hosts = sorted(host_paths)
        # Only hosts on disk are editable (a missing evidence path is read-only).
        editable_hosts = [
            host
            for host in evidence_hosts
            if _is_editable_host(host, host_counts, drivers, retained) and _path_exists_rel(host)
        ]
        readonly_hosts = [host for host in evidence_hosts if host not in editable_hosts]

        def anchor_for(
            anchor_rows: list[dict[str, Any]], anchor_all: list[dict[str, Any]], what: str
        ) -> tuple[dict[str, Any], str | None]:
            try:
                body_anchor = _insertion_for_rows(anchor_rows, part, anchor_all, toc_order, parents, route_order, annex=False)
                found = {
                    "body": body_anchor,
                    "annex": _insertion_for_rows(
                        anchor_rows, part, anchor_all, toc_order, parents, route_order, annex=True, body_anchor=body_anchor
                    ),
                }
                return found, _heading_level(part, found)
            except (Refusal, UsageError) as exc:
                anchor_refusals.append(f"{what}: {exc}")
                return {"body": None, "annex": None}, None

        insertions: list[dict[str, Any]] | None = None
        if unit_ids is None:
            insertion, heading_level = anchor_for(packet_rows, rows, packet_id)
        else:
            # Each new file goes beside the existing destinations of the units
            # that propose it (else at the end of the part driver), never
            # beside a co-packed unit's hosts: one insertion and heading level
            # per set of proposing units. No new files: no insertion.
            by_owners: dict[tuple[str, ...], list[str]] = {}
            for rel in owned:
                owners = tuple(
                    u for u in packet_unit_ids
                    if _path_key(rel) in {_path_key(item) for item in unit_destinations[u][0]}
                )
                by_owners.setdefault(owners, []).append(rel)
            insertions = []
            for owners, files in by_owners.items():
                own_rows = [
                    {
                        "part": part,
                        "chapter_id": "",
                        "section_id": "",
                        "reader_evidence": [{"path": rel} for rel in sorted({h for u in owners for h in unit_hosts(u)})],
                    }
                ]
                found, level = anchor_for(own_rows, own_rows, f"{packet_id} ({','.join(owners) or 'no proposing unit'})")
                insertions.append({"units": list(owners), "owned_files": files, "insertion": found, "heading_level": level})
            # The packet-level insertion is that of its first owned body file
            # (the body unit-compile builds).
            first_body = next((rel for rel in owned if rel.startswith("handbook/parts/")), None)
            primary = next(
                (item for item in insertions if first_body in item["owned_files"]),
                insertions[0] if insertions else None,
            )
            insertion = primary["insertion"] if primary else {"body": None, "annex": None}
            heading_level = primary["heading_level"] if primary else None
        units = _packet_units(
            packet_rows,
            unit_source,
            held,
            unit_ids=packet_unit_ids,
        )
        labels_to_find: set[str] = set()
        files_to_find: set[str] = set()
        for row in packet_rows:
            for evidence in row.get("reader_evidence") or []:
                if isinstance(evidence, dict):
                    if isinstance(evidence.get("anchor"), str):
                        labels_to_find.add(evidence["anchor"])
                    if isinstance(evidence.get("path"), str):
                        files_to_find.add(evidence["path"])
        for unit_id in packet_unit_ids:
            unit = unit_source.get(unit_id, {})
            files_to_find.update(_destination_paths(unit))
            labels_to_find.update(_labels_from_unit(unit))
            if unit_ids is not None:
                files_to_find.update(unit_destinations[unit_id][1] + unit_lookups[unit_id])
        component_counts[packet_id] = component_total
        max_blocks = min(4, 1 + math.ceil(max(component_total, 0) / 3))
        packet_records.append(
            {
                "id": packet_id,
                "wave": wave,
                "part": part,
                "mode": mode,
                "chapter": chapter,
                "sections": _packet_summary_sections(packet_rows, queue_units),
                "accounting_reasons": {
                    _section_id(row): _au_accounting_reasons(row, queue_units)
                    for row in packet_rows
                    if row.get("status") == AU
                },
                "units": units,
                "component_ids": component_ids,
                "sources_held": sources_held,
                # Open blocker records naming this packet's sections (only
                # authored_unreviewed sections, sent to accounting).
                "open_blockers": {
                    _section_id(row): open_blocker_sections[_section_id(row)]
                    for row in packet_rows
                    if _section_id(row) in open_blocker_sections
                },
                "owned_files": owned,
                "editable_hosts": editable_hosts,
                "readonly_hosts": readonly_hosts,
                "existing": _grep_existing(labels_to_find, files_to_find, label_index),
                "label_tag": label_tag,
                "heading_level": heading_level,
                "insertion": insertion,
                # Unit-only packets: one insertion and heading level per set
                # of units proposing owned files (None for section packets).
                "insertions": insertions,
                "toc_tag": f"%% toc: {part} {chapter['id']} {','.join(section_ids)}" if chapter else None,
                "max_blocks": max_blocks,
                "lane": None,
            }
        )

    # Owned files and label tags are disjoint between packets and from other
    # waves' packets; a reused tag is not used by labels outside its files.
    other_wave_owned = {_path_key(item) for item in wave_owned_files}
    owners: dict[str, str] = {}
    tag_owners: dict[str, str] = {}
    for record in packet_records:
        record_id = str(record["id"])
        owned_set = _packet_paths(record, "owned_files")
        for rel in sorted(owned_set):
            if owners.setdefault(_path_key(rel), record_id) != record_id or _path_key(rel) in other_wave_owned:
                ownership_refusals.append(f"{record_id}: owned file {rel} is another packet's")
        tag = record.get("label_tag")
        if not isinstance(tag, str) or not re.fullmatch(rf"{_part_dir(str(record['part']))}-{SLUG_RE}", tag):
            ownership_refusals.append(f"{record_id}: label_tag {tag!r} is not pNN-<short>")
            continue
        if tag_owners.setdefault(tag, record_id) != record_id or tag in wave_label_tags:
            ownership_refusals.append(f"{record_id}: label_tag {tag} is another packet's")
        if _packet_base_id(record_id, wave) in reused_ids and _label_tag_taken(
            tag, _labels_outside(label_files, owned_set), set()
        ):
            ownership_refusals.append(f"{record_id}: label_tag {tag} is used by labels outside its files")

    _assign_lanes(packet_records)
    # Within a lane, packets run in TOC order (printed part order, not part number).
    # Unit-only packets (no sections) follow, in part then unit order.
    packet_records.sort(
        key=lambda p: (
            int(p["lane"]),
            min(
                (_row_order({"section_id": s["section_id"]}, toc_order) for s in p["sections"]),
                default=(10_000_000, ()),
            ),
            sorted(str(u.get("unit_id")) for u in p.get("units") or []),
        )
    )
    lane_map = _lane_map(packet_records)
    worst_case = sum(_packet_cost(packet) for packet in packet_records)
    blocked_sections = sum(len(item.get("sections", [])) for item in blocked)
    total_sections = sum(len(packet["sections"]) for packet in packet_records) + blocked_sections
    cap_violations = _cap_violations(packet_records, component_counts)
    oversize_indivisible = _oversize_indivisible_packets(packet_records, component_counts)
    mode_counts = Counter(_packet_mode(packet) for packet in packet_records)
    # Reasons of the authored_unreviewed rows actually packetized.
    packetized_au = [row for packet_rows in unblocked_packets for row in packet_rows if row.get("status") == AU]
    accounting_reasons: Counter[str] = Counter(
        reason for row in packetized_au for reason in _au_accounting_reasons(row, queue_units)
    )
    mode_costs: Counter[str] = Counter()
    for packet in packet_records:
        mode_costs[_packet_mode(packet)] += _packet_cost(packet)
    print(f"wave: {wave}")
    print(f"parts: {','.join(parts)}")
    print(f"packets: {len(packet_records)}")
    for mode in ("author", "accounting", "unit_accounting"):
        print(f"  {mode} packets: {mode_counts.get(mode, 0)} (worst-case agents {mode_costs.get(mode, 0)})")
    print(f"lanes: {len(lane_map)}")
    print(f"sections: {total_sections}")
    print(
        f"  {AU} sections selected for accounting: "
        f"{len(packetized_au)} "
        f"(parked scope {accounting_reasons.get('parked_scope', 0)}, "
        f"stale evidence {accounting_reasons.get('stale_evidence', 0)}, "
        f"no component accounting {accounting_reasons.get('no_component_accounting', 0)})"
    )
    print(f"blocked sections: {blocked_sections}")
    print(f"unit-only units: {sum(len(u.get('units') or []) for u in packet_records if _packet_mode(u) == 'unit_accounting')}")
    no_sources = [p["id"] for p in packet_records if _packet_mode(p) in ACCOUNTING_MODES and p.get("sources_held") is False]
    if no_sources:
        print(f"accounting packets whose sources are absent (assess only; no authoring without sources): {len(no_sources)}")
    unplaced_reasons = {unit_id: _unplaced_reason(unlinked_units[unit_id]) for unit_id in unplaced_units}
    if unplaced_units:
        print(
            f"unlinked queue units with no derivable part (not packetized in any wave): {len(unplaced_units)} "
            f"(ids {'written to' if args.apply else 'would be written to'} "
            f"{(WAVES_ROOT / wave / 'unplaced-units.json').as_posix()}; open item for the lead)"
        )
        reason_counts = Counter(reason for reason, _evident in unplaced_reasons.values())
        for reason in (UNPLACED_MALFORMED, UNPLACED_NO_PART):
            print(f"  {reason}: {reason_counts.get(reason, 0)}")
        in_wave = [unit_id for unit_id, (_r, evident) in unplaced_reasons.items() if set(evident) & set(parts)]
        if in_wave:
            print(
                f"  malformed part path naming a part of this wave (left out; repair the queue paths): "
                f"{','.join(in_wave)}"
            )
    print(f"worst-case agents: {worst_case} (author 2*max_blocks+2, accounting 2, unit_accounting 2)")
    if skipped_for_blockers:
        print(f"skipped sections with open blockers: {len(skipped_for_blockers)}")
    if blocker_au_rows:
        print(
            f"{AU} sections with open blockers sent to accounting (sources_held false): "
            f"{','.join(_section_id(row) for row in blocker_au_rows)}"
        )
    if carried_au:
        print(f"carry-over sections already {AU} (not packetized): {','.join(carried_au)}")
    if anchor_refusals or cap_violations or ownership_refusals:
        if ownership_refusals:
            print("refusal: packet ownership breaks the rules for:", file=sys.stderr)
            for item in ownership_refusals:
                print(f"  - {item}", file=sys.stderr)
        if anchor_refusals:
            print("refusal: no valid insertion anchor or heading level for:", file=sys.stderr)
            for item in anchor_refusals:
                print(f"  - {item}", file=sys.stderr)
        if cap_violations:
            print("refusal: packet cap cannot be met for:", file=sys.stderr)
            for item in cap_violations:
                print(f"  - {item}", file=sys.stderr)
        return 1
    if oversize_indivisible:
        print("oversize indivisible sections:", file=sys.stderr)
        for item in oversize_indivisible:
            print(f"  - {item}", file=sys.stderr)
    if kept_in_flight:
        print(f"in-flight packets kept as written: {','.join(kept_in_flight)}")
    force = bool(getattr(args, "force", False))
    unplaced_records = [
        {
            "unit_id": unit_id,
            "reason": unplaced_reasons[unit_id][0],
            "evident_parts": unplaced_reasons[unit_id][1],
            "component_ids": _unit_component_ids(unlinked_units[unit_id]),
            "prerequisite_allocation_prefix": unlinked_units[unit_id].get("prerequisite_allocation_prefix"),
            "destination": unlinked_units[unit_id].get("destination"),
        }
        for unit_id in unplaced_units
    ]
    if worst_case > AGENT_BUDGET:
        result = _write_split_waves(wave, packet_records, blocked, apply=args.apply, force=force)
        if result == 0 and args.apply:
            _write_unplaced_units(wave, unplaced_records)
        return result
    _refuse_in_flight_changes(wave, {wave: {str(packet["id"]) for packet in packet_records}}, force=force)
    if not args.apply:
        return 0

    _write_wave_outputs(wave, packet_records, blocked, force=force)
    _write_unplaced_units(wave, unplaced_records)
    # Halves of an earlier split must not stay runnable beside the whole wave.
    for half in (f"{wave}a", f"{wave}b"):
        if _root(WAVES_ROOT / half).is_dir():
            _write_wave_outputs(half, [], [], force=force, write_args=False)
    return 0


def _resolve_packet(value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = ROOT / path
    if path.is_file():
        return path.resolve()
    matches = sorted(_root(WAVES_ROOT).glob(f"*/packets/{value}.json"))
    if len(matches) == 1:
        return matches[0].resolve()
    if not matches:
        raise UsageError(f"packet not found: {value}")
    raise UsageError(f"packet id is ambiguous: {value}")


def _load_packet(value: str) -> tuple[Path, dict[str, Any]]:
    path = _resolve_packet(value)
    data = _load_json(path, None)
    if not isinstance(data, dict):
        raise UsageError(f"{_rel(path)} is not a packet JSON object")
    return path, data


def _scan_tree_state() -> dict[str, dict[str, Any]]:
    state: dict[str, dict[str, Any]] = {}
    for base_rel in ("handbook", "spec/research", "spec/coverage"):
        base = _root(base_rel)
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not path.is_file():
                continue
            rel = path.relative_to(ROOT).as_posix()
            try:
                stat = path.stat()
            except OSError:
                continue
            state[rel] = {"size": stat.st_size, "mtime_ns": stat.st_mtime_ns}
    return state


def _hash_state(state: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    result = {}
    for rel, meta in state.items():
        path = _root(rel)
        if path.is_file():
            result[rel] = {**meta, "sha256": _sha256_file(path)}
    return result


def _frozen_files() -> list[str]:
    frozen = set(FROZEN_EXPLICIT)
    for glob in ("handbook/parts/p*.tex", "handbook/annex/p*.tex", "handbook/annex/p*-route.tex"):
        frozen.update(path.relative_to(ROOT).as_posix() for path in ROOT.glob(glob) if path.is_file())
    return sorted(frozen)


def _run_check_findings() -> list[str]:
    """All check.py findings over the whole handbook tree ("category: text")."""
    cmd = [
        sys.executable,
        "-B",
        str(_root("tools/check.py")),
        "--tree",
        "handbook",
        "--root",
        str(ROOT),
    ]
    try:
        proc = subprocess.run(
            cmd,
            cwd=ROOT,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=180,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return [f"__check_error__: check.py unavailable: {exc}"]
    summary_seen = any(
        "[check] all hard checks passed" in line
        or "[check]" in line and "hard failure(s)" in line
        for line in proc.stdout.splitlines()
    )
    if proc.returncode not in {0, 1}:
        return [f"__check_error__: check.py exited {proc.returncode}"]
    if not summary_seen:
        return ["__check_error__: check.py output did not include a summary line"]
    findings: list[str] = []
    for line in proc.stdout.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            findings.append(stripped[2:])
    return sorted(findings)


def _decoded_text(rel: str) -> str:
    """File text for the content guards; undecodable bytes become U+FFFD."""
    return _root(rel).read_bytes().decode("utf-8", errors="replace")


def _snapshot_path(packet_path: Path, packet: dict[str, Any]) -> Path:
    return packet_path.parent.parent / "snapshots" / f"{packet.get('id')}.json"


def _snapshot_digest_index(snapshot_path: Path) -> Path:
    return snapshot_path.parent / "digests.json"


def _record_snapshot_digest(snapshot_path: Path) -> None:
    """Record the snapshot's sha256 in the wave's digest index, which verify
    checks, so an edited or silently replaced snapshot is detected."""
    index_path = _snapshot_digest_index(snapshot_path)
    data = _load_json(index_path, {})
    if not isinstance(data, dict):
        raise UsageError(f"{_rel(index_path)} is not a JSON object")
    data[snapshot_path.stem] = _sha256_file(snapshot_path)
    _write_json_atomic(index_path, data)


def _packet_held_paths(packet: dict[str, Any]) -> list[str]:
    return sorted(
        {
            path
            for unit in packet.get("units") or []
            if isinstance(unit, dict)
            for path in unit.get("held_paths") or []
            if isinstance(path, str)
        }
    )


def _path_key(path: str) -> str:
    return path.casefold() if os.name == "nt" else path


def _packet_paths(data: dict[str, Any], *keys: str) -> set[str]:
    return {
        normalized
        for key in keys
        for item in data.get(key) or []
        if isinstance(item, str)
        for normalized in [_try_normalize_repo_path(item)]
        if normalized
    }


SLUG_RE = r"[a-z0-9]+(?:-[a-z0-9]+)*"


def _owned_form_problems(part: Any, packet_id: str, wave: str, owned: Any, mode: Any = None) -> list[str]:
    """owned_files must be exactly _owned_files(part, slug) for one slug, and
    the slug must end with the packet's short id (as packetize makes it), so
    the six files are new files of this packet only. A unit_accounting
    packet owns only its units' proposed body/annex destinations: each a
    .tex file under handbook/parts|annex/<its part dir>/ (possibly none)."""
    if not isinstance(part, str) or not re.fullmatch(r"P(?:[1-9]|1[0-9])", part):
        return [f"packet part {part!r} is not P1..P19"]
    if not isinstance(owned, list) or not all(isinstance(item, str) for item in owned):
        return ["owned_files is not a list of paths"]
    normalized = [_try_normalize_repo_path(item) for item in owned]
    if mode == "unit_accounting":
        bad = [
            raw for raw, rel in zip(owned, normalized)
            if rel is None
            or not rel.endswith(".tex")
            or not re.fullmatch(rf"handbook/(?:parts|annex)/{_part_dir(part)}/.+", rel)
            or _path_has_prefix(rel, "handbook/restoration")
            or _path_has_prefix(rel, "handbook/generated")
        ]
        if bad or len(set(normalized)) != len(normalized):
            return [
                f"unit_accounting owned_files {owned!r} must be distinct .tex destinations under "
                f"handbook/parts|annex/{_part_dir(part)}/"
            ]
        return []
    annex_re = re.compile(rf"handbook/annex/{_part_dir(part)}/({SLUG_RE})\.tex")
    slugs = {match.group(1) for item in normalized if item for match in [annex_re.fullmatch(item)] if match}
    shorts = {packet_id, _packet_base_id(packet_id, re.sub(r"[ab]$", "", wave))}
    short_re = "|".join(re.escape(item) for item in sorted(shorts))
    if (
        len(slugs) != 1
        or sorted(item or "" for item in normalized) != sorted(_owned_files(part, next(iter(slugs))))
        or not re.fullmatch(rf"{SLUG_RE}-(?:{short_re})(?:-\d+)?", next(iter(slugs)))
    ):
        return [
            f"owned_files {owned!r} are not exactly the six files of one slug ending with the packet id "
            f"(handbook/parts/{_part_dir(part)}/<slug>.tex, annex, intake bib, symbol CSV, research note, return JSON)"
        ]
    return []


def _ownership_problems(packet_path: Path, packet: dict[str, Any], *, check_labels: bool) -> list[str]:
    """Owned files, editable hosts and the label tag checked against the
    ownership rules.

    Owned files: the six files of one slug bound to the packet id; none under
    restoration/ or generated/, a driver, frozen or retained; none listed by
    another packet (owned files of any wave; owned, editable or read-only of
    this wave and its split halves, except read-only in the same lane).
    Editable hosts: not under restoration/ or generated/, not a driver or retained file, a handbook .tex file, and not
    listed by another packet of the wave. Label tag: pNN-..., not another
    packet's tag, and (with check_labels) not used by labels outside this
    packet's files."""
    drivers = _driver_paths()
    retained = _retained_reader_files()
    frozen = {_path_key(item) for item in set(_frozen_files()) | drivers | retained}
    wave_dir = packet_path.parent.parent.name
    family = _own_waves(re.sub(r"[ab]$", "", wave_dir), keep=wave_dir)
    family_paths: Counter[str] = Counter()
    conflict_keys: set[str] = set()
    other_owned: set[str] = set()
    other_tags: set[str] = set()
    for path in sorted(_root(WAVES_ROOT).glob("*/packets/*.json")):
        if path.resolve() == packet_path.resolve():
            continue
        data = _load_json(path, None)
        if not isinstance(data, dict):
            continue
        owned_other = _packet_paths(data, "owned_files")
        other_owned.update(_path_key(item) for item in owned_other)
        if path.parent.parent.name in family:
            family_paths.update(_packet_paths(data, "owned_files", "editable_hosts", "readonly_hosts"))
            # Read-only listing of this packet's owned file by a packet of the
            # same lane (a proposed destination shared by a split unit
            # cluster) is serialized by the lane, so it is no conflict.
            same_lane = (
                path.parent.parent.name == wave_dir
                and packet.get("lane") is not None
                and data.get("lane") == packet.get("lane")
            )
            conflict_keys.update(
                _path_key(item)
                for item in _packet_paths(data, "owned_files", "editable_hosts")
                | (set() if same_lane else _packet_paths(data, "readonly_hosts"))
            )
        if isinstance(data.get("label_tag"), str):
            other_tags.add(data["label_tag"])

    problems = _owned_form_problems(
        packet.get("part"), str(packet.get("id") or ""), wave_dir, packet.get("owned_files"), packet.get("mode")
    )
    if packet.get("mode") == "unit_accounting" and packet.get("sections"):
        problems.append("a unit_accounting packet has no sections")
    owned = _packet_paths(packet, "owned_files")
    for rel in sorted(owned):
        key = _path_key(rel)
        if (
            _path_has_prefix(rel, "handbook/restoration")
            or _path_has_prefix(rel, "handbook/generated")
            or key in frozen
        ):
            problems.append(f"owned file {rel!r} is under restoration/ or generated/, a driver, frozen or retained")
        if key in other_owned or key in conflict_keys:
            problems.append(f"owned file {rel!r} is listed by another packet")
    for raw in packet.get("editable_hosts") or []:
        rel = _try_normalize_repo_path(raw) if isinstance(raw, str) else None
        if rel is None or not _is_editable_host(rel, family_paths + Counter({rel: 1}), drivers, retained):
            problems.append(f"editable host {raw!r} breaks the ownership rules (restoration/generated, driver, retained, non-.tex, or shared with another packet)")

    tag = packet.get("label_tag")
    part = packet.get("part")
    part_dir = _part_dir(part) if isinstance(part, str) and re.fullmatch(r"P\d+", part) else "p??"
    if not isinstance(tag, str) or not re.fullmatch(rf"{part_dir}-{SLUG_RE}", tag):
        problems.append(f"label_tag {tag!r} is not {part_dir}-<short>")
    elif tag in other_tags:
        problems.append(f"label_tag {tag!r} is another packet's label tag")
    elif check_labels:
        mine = owned | _packet_paths(packet, "editable_hosts")
        if _label_tag_taken(tag, _existing_labels(exclude_files=mine), set()):
            problems.append(f"label_tag {tag!r} is already used by labels outside this packet's files")
    return problems


def _wave_packet_paths(packet_path: Path) -> dict[str, list[str]]:
    """Packet id -> owned files and editable hosts, for every other packet in
    this packet's wave directory."""
    result: dict[str, list[str]] = {}
    for path in sorted((packet_path.parent).glob("*.json")):
        if path.resolve() == packet_path.resolve():
            continue
        data = _load_json(path, None)
        if isinstance(data, dict):
            result[str(data.get("id") or path.stem)] = sorted(_packet_paths(data, "owned_files", "editable_hosts"))
    return result


@contextlib.contextmanager
def _snapshot_batch_cache():
    """Within one batch snapshot run the lead changes nothing, so the whole-tree
    state, the check.py baseline and the frozen-file list are computed once."""
    global _scan_tree_state, _run_check_findings, _frozen_files
    originals = (_scan_tree_state, _run_check_findings, _frozen_files)
    cache: dict[str, Any] = {}

    def memo(name, fn):
        def wrapper():
            if name not in cache:
                cache[name] = fn()
            return copy.deepcopy(cache[name])
        return wrapper

    _scan_tree_state = memo("tree", originals[0])
    _run_check_findings = memo("check", originals[1])
    _frozen_files = memo("frozen", originals[2])
    try:
        yield
    finally:
        _scan_tree_state, _run_check_findings, _frozen_files = originals


def snapshot(args: argparse.Namespace) -> int:
    packet_path, packet = _load_packet(args.packet)
    if args.apply and args.dry_run:
        raise UsageError("--apply and --dry-run are mutually exclusive")
    out = _snapshot_path(packet_path, packet)
    digests = _load_json(_snapshot_digest_index(out), {})
    taken = out.is_file() or (isinstance(digests, dict) and out.stem in digests)
    if taken and not getattr(args, "force", False):
        raise Refusal(f"a snapshot of {packet.get('id')} was already taken ({_rel(out)}); pass --force to replace the baseline")
    host_problems = _ownership_problems(packet_path, packet, check_labels=True)
    if host_problems:
        raise Refusal("; ".join(host_problems))
    owned = [_normalize_repo_path(path) for path in packet.get("owned_files", [])]
    editable = [_normalize_repo_path(path) for path in packet.get("editable_hosts", [])]
    frozen = _frozen_files()
    tree = _hash_state(_scan_tree_state())
    record = {
        "packet": packet.get("id"),
        "packet_path": _rel(packet_path),
        "packet_sha256": _sha256_file(packet_path),
        "wave": packet.get("wave"),
        "created_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "owned_files": {path: (_sha256_file(_root(path)) if _root(path).is_file() else None) for path in owned},
        "editable_hosts": {path: (_sha256_file(_root(path)) if _root(path).is_file() else None) for path in editable},
        # Host text at the snapshot: verify reports only guard hits that are new.
        "editable_host_text": {path: _decoded_text(path) for path in editable if _root(path).is_file()},
        "frozen_files": {path: (_sha256_file(_root(path)) if _root(path).is_file() else None) for path in frozen},
        # Held sources the copy guard compares against (they lie outside the
        # G1 scan, so verify checks them against these hashes).
        "held_paths": {
            path: (_sha256_file(_root(path)) if _root(path).is_file() else None)
            for path in _packet_held_paths(packet)
        },
        # Owned files and editable hosts of the wave's other packets: lanes run
        # concurrently, so G1 attributes their changes instead of failing.
        "wave_packet_paths": _wave_packet_paths(packet_path),
        "tree": tree,
        # Whole-tree baseline: verify diffs against it.
        "check_findings": _run_check_findings(),
    }
    if args.apply:
        _write_json_atomic(out, record)
        _record_snapshot_digest(out)
        print(f"wrote: {_rel(out)}")
        # verify reads the snapshot from the wave-base commit only: commit the
        # wave's snapshots and record that commit as base_sha in args.json.
        print(f"snapshot-sha256: {_sha256_file(out)}")
        print(f"next: commit {_rel(out.parent)}/ and set base_sha in {_rel(out.parent.parent / 'args.json')}")
    else:
        print(f"dry-run: would write {_rel(out)}")
        print(json.dumps({"packet": record["packet"], "owned_files": len(owned), "editable_hosts": len(editable), "frozen_files": len(frozen)}, ensure_ascii=False))
    return 0


def _git_blobs(sha: str, rels: list[str]) -> dict[str, bytes | None]:
    """Raw bytes of each path at commit `sha` (None when absent there)."""
    if not rels:
        return {}
    proc = subprocess.run(
        ["git", "-C", str(ROOT), "cat-file", "--batch"],
        input="".join(f"{sha}:{rel}\n" for rel in rels).encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=300,
    )
    if proc.returncode != 0:
        raise UsageError(f"git cat-file failed: {proc.stderr.decode('utf-8', 'replace').strip()}")
    out = proc.stdout
    pos = 0
    result: dict[str, bytes | None] = {}
    for rel in rels:
        newline = out.index(b"\n", pos)
        header = out[pos:newline].split(b" ")
        pos = newline + 1
        result[rel] = None
        if len(header) == 3 and header[2].isdigit():
            size = int(header[2])
            if header[1] == b"blob":
                result[rel] = out[pos : pos + size]
            pos += size + 1
    return result


def _wave_base_sha(wave_dir: Path) -> tuple[str | None, str]:
    """The wave-base commit recorded as base_sha in the wave's args.json,
    resolved to a full SHA; it must be a commit that HEAD contains. Returns
    (sha, "") or (None, problem)."""
    args_path = wave_dir / "args.json"
    data = _load_json(args_path, None)
    raw = data.get("base_sha") if isinstance(data, dict) else None
    if not isinstance(raw, str) or not re.fullmatch(r"[0-9a-fA-F]{7,64}", raw.strip()):
        return None, f"base_sha missing from {_rel(args_path)}: the lead must commit the wave snapshots and record that commit"
    proc = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "--verify", "--quiet", f"{raw.strip()}^{{commit}}"],
        capture_output=True,
        text=True,
        timeout=60,
    )
    sha = proc.stdout.strip()
    if proc.returncode != 0 or not sha:
        return None, f"base_sha {raw!r} in {_rel(args_path)} is not a commit"
    ancestor = subprocess.run(
        ["git", "-C", str(ROOT), "merge-base", "--is-ancestor", sha, "HEAD"], capture_output=True, timeout=60
    )
    if ancestor.returncode != 0:
        return None, f"base_sha {sha} is not an ancestor of HEAD"
    return sha, ""


def _parse_intake_bib(path: Path) -> list[str]:
    if not path.is_file():
        return []
    text = _read_text(path)
    keys: list[str] = []
    depth = 0
    for i, char in enumerate(text):
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth < 0:
                raise UsageError(f"{_rel(path)}: unbalanced BibTeX braces near byte {i}")
    if depth != 0:
        raise UsageError(f"{_rel(path)}: unbalanced BibTeX braces")
    for match in re.finditer(r"@[A-Za-z]+\s*\{\s*([^,\s{}]+)", text):
        keys.append(match.group(1))
    return keys


def _read_csv_header(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        return next(reader, [])


# Numeric scopes (section 8 of the tooling spec): PNN.k anywhere in the value,
# or a value that is only a part or a range of parts/chapters (P5, P5-P19,
# P4.2-P4.5).
NUMERIC_POINT = r"P\d{1,2}(?:\.\d+)?"
NUMERIC_SCOPE_RE = re.compile(rf"\s*{NUMERIC_POINT}(?:\s*(?:--|-|–|—|to)\s*P?\d{{1,2}}(?:\.\d+)?)?\s*")


def _numeric_scope_problems(path: Path) -> list[str]:
    """Numeric values in the scope and first_use columns of an intake CSV."""
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
    except (OSError, csv.Error, UnicodeDecodeError) as exc:
        return [f"unreadable CSV: {exc}"]
    problems: list[str] = []
    for line, row in enumerate(rows, 2):
        for column in ("scope", "first_use"):
            value = row.get(column)
            if isinstance(value, str) and (
                NUMERIC_SCOPE_RE.fullmatch(value) or re.search(r"\bP\d{1,2}\.\d+\b", value)
            ):
                problems.append(f"row {line}: numeric {column} {value!r}")
    return problems


def _tex_text_without_comments(text: str) -> str:
    return "\n".join(_strip_tex_comments(line) for line in text.splitlines())


def _file_text(path: str, text: str | None) -> str:
    return _read_text(_root(path)) if text is None else text


def _check_fused(path: str, text: str | None = None) -> list[str]:
    try:
        sys.path.insert(0, str(_root("tools")))
        import find_fused_spaces  # type: ignore
    finally:
        try:
            sys.path.remove(str(_root("tools")))
        except ValueError:
            pass
    if path.endswith(".tex"):
        scan = find_fused_spaces.scan_tex
    elif path.endswith(".md"):
        scan = find_fused_spaces.scan_md
    else:
        return []
    return [
        f"{path}:{hit.line}:{hit.col}: {hit.cls} {hit.match!r} -> {hit.suggestion!r}"
        for hit in scan(_file_text(path, text))
        if hit.cls in {"A", "B", "C"}
    ]


# Commands whose mandatory argument is a label, and environments whose first
# arguments are a label and (for results and annex items) a status or backref.
REFERENCE_COMMANDS = {
    "label",
    "ref",
    "cref",
    "Cref",
    "vref",
    "eqref",
    "pageref",
    "autoref",
    "nameref",
    "labelcref",
}
LABEL_ENV_ARGUMENTS = {
    "hbtheorem": 2,
    "hblemma": 2,
    "hbcorollary": 2,
    "hbdefinition": 1,
    "hbconvention": 1,
    "hbmethod": 1,
    "hbexample": 1,
    "hbwarning": 1,
    "proofboundary": 1,
    "systementry": 1,
    "annexitem": 2,
}


def _mandatory_group_spans(text: str, pos: int, count: int) -> list[tuple[int, int]]:
    """Spans of the first `count` brace groups after a command, skipping a
    star and leading optional [..] arguments (which stay visible)."""
    if pos < len(text) and text[pos] == "*":
        pos += 1
    start = _skip_ws(text, pos)
    while start < len(text) and text[start] == "[":
        end = _group_end(text, start)
        if end is None:
            return []
        start = _skip_ws(text, end)
    spans: list[tuple[int, int]] = []
    for _ in range(count):
        end = _group_end(text, start) if start < len(text) and text[start] == "{" else None
        if end is None:
            break
        spans.append((start, end))
        start = _skip_ws(text, end)
    return spans


def _mask_reference_arguments(text: str) -> str:
    """Blank (keeping newlines) the keys and labels in \\cite-family, \\label
    and \\ref-family arguments and in label arguments of labelled
    environments, so word guards do not read keys and labels as prose.
    Cite pre- and postnotes and other optional arguments stay visible."""
    chars = list(text)

    def blank(start: int, end: int) -> None:
        for i in range(start, min(end, len(chars))):
            if chars[i] != "\n":
                chars[i] = " "

    for match in re.finditer(r"\\([A-Za-z@]+)", text):
        name = match.group(1)
        pos = match.end()
        if _is_cite_command(name):
            _end, _groups, spans = _cite_arguments(text, pos, name)
        elif name in REFERENCE_COMMANDS:
            spans = _mandatory_group_spans(text, pos, 1)
        elif name == "hyperref":
            # \hyperref[label]{text}: the label is the optional argument.
            start = _skip_ws(text, pos)
            end = _group_end(text, start) if start < len(text) and text[start] == "[" else None
            spans = [(start, end)] if end else []
        elif name == "begin":
            start = _skip_ws(text, pos)
            end = _group_end(text, start) if start < len(text) and text[start] == "{" else None
            count = LABEL_ENV_ARGUMENTS.get(text[start + 1 : end - 1].strip()) if end else None
            spans = _mandatory_group_spans(text, end, count) if end and count else []
        else:
            continue
        for start, end in spans:
            blank(start, end)
    return "".join(chars)


STUB_PHRASES = (
    "left to the reader",
    "omitted for brevity",
    "standard argument",
    "routine verification",
    "similarly for the remaining cases",
    "the remaining cases are similar",
    "details omitted",
)
# Phrase words may be separated by any whitespace, line breaks included.
STUB_MARKER_RE = re.compile(
    r"\\hbstub(?![A-Za-z@])|\b(?:TODO|FIXME|TBD)\b"
    r"|(?i:\b(?:" + "|".join(r"\s+".join(phrase.split()) for phrase in STUB_PHRASES) + r")\b)"
)


def _hit_context(text: str, start: int, end: int) -> str:
    """A guard hit with up to three words on each side on its line, so a
    baseline comparison tells a changed or new hit from an old one (a line
    moved intact keeps its context)."""
    line_start = text.rfind("\n", 0, start) + 1
    line_end = text.find("\n", end)
    before = text[max(line_start, start - 60) : start].split()[-3:]
    after = text[end : min(end + 60, line_end if line_end != -1 else len(text))].split()[:3]
    return " ".join(before + text[start:end].split() + after)


def _stub_markers(path: str, text: str | None = None) -> list[str]:
    text = _mask_reference_arguments(_tex_text_without_comments(_file_text(path, text)))
    return [
        f"{path}:{text.count(chr(10), 0, m.start()) + 1}: stub marker {m.group(0)!r} in {_hit_context(text, m.start(), m.end())!r}"
        for m in STUB_MARKER_RE.finditer(text)
    ]


NEW_DEFINITION_RE = re.compile(
    r"\\(?:(?:new|renew|provide)commandx?|DeclareRobustCommand|[gex]?def|cs[gex]?def|let|futurelet|"
    r"cs_(?:new|set|gset)(?:_protected)?(?:_nopar)?:[Nc][npwTF]*|cs_(?:new|set|gset)_eq:[Nc][Nc]|"
    r"(?:new|renew|provide)robustcmd|@namedef|(?:math)?chardef|countdef|dimendef|skipdef|toksdef|"
    r"DeclareMathOperator|DeclareMathSymbol|newif|newcounter|newlength|"
    r"(?:New|Renew|Provide|Declare)Document(?:Command|Environment)|"
    r"(?:New|Renew|Provide|Declare)ExpandableDocumentCommand|NewCommandCopy|"
    r"newenvironment|renewenvironment|newtheorem|declaretheorem|"
    r"DeclarePairedDelimiter(?:X|XPP)?)(?![A-Za-z@])"
)


def _new_macro_defs(path: str, text: str | None = None) -> list[str]:
    text = _tex_text_without_comments(_file_text(path, text))
    findings: list[str] = []
    for m in NEW_DEFINITION_RE.finditer(text):
        # The definition as written on its line names the defined macro.
        line_end = text.find("\n", m.start())
        written = " ".join(text[m.start() : line_end if line_end != -1 else len(text)].split())[:200]
        findings.append(f"{path}:{text.count(chr(10), 0, m.start()) + 1}: content macro definition {written}")
    return findings


def _env_balance(path: str, text: str | None = None) -> list[str]:
    text = _tex_text_without_comments(_file_text(path, text))
    stack: list[tuple[str, int]] = []
    findings: list[str] = []
    for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", text):
        kind, env = match.group(1), match.group(2).strip()
        line = text.count("\n", 0, match.start()) + 1
        if kind == "begin":
            stack.append((env, line))
        elif not stack:
            findings.append(f"{path}:{line}: unmatched \\end{{{env}}}")
        else:
            last_env, last_line = stack.pop()
            if last_env != env:
                findings.append(
                    f"{path}:{line}: \\end{{{env}}} closes \\begin{{{last_env}}} from line {last_line}"
                )
    for env, line in stack:
        findings.append(f"{path}:{line}: unclosed \\begin{{{env}}}")
    return findings


def _encoding_guard(path: str) -> list[str]:
    raw = _root(path).read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        return [f"{path}: non-UTF-8 bytes: {exc}"]
    if "\ufffd" in text:
        return [f"{path}: contains U+FFFD replacement character"]
    return []


WORKFLOW_PATTERNS = {
    "review": r"review(?:s|ed|ing|er|ers)?",
    "admission": r"admissions?",
    "admitted": r"admitted",
    "ledger": r"ledgers?",
    "assessor": r"assessors?",
    "intake": r"intakes?",
    "wave": r"waves?",
    "this record": r"this\s+record",
    "author block": r"author\s+blocks?",
}


def _workflow_words(path: str, text: str | None = None) -> list[str]:
    if not path.startswith("handbook/parts/"):
        return []
    text = _mask_reference_arguments(_tex_text_without_comments(_file_text(path, text)))
    findings: list[str] = []
    for word, body in WORKFLOW_PATTERNS.items():
        pattern = re.compile(rf"\b{body}\b", re.IGNORECASE)
        for match in pattern.finditer(text):
            findings.append(
                f"{path}:{text.count(chr(10), 0, match.start()) + 1}: workflow word {word!r} "
                f"in {_hit_context(text, match.start(), match.end())!r}"
            )
    return findings


def _prescriptive_words(path: str, text: str | None = None) -> list[str]:
    if "/p19/" not in path and "/p19." not in path:
        return []
    text = _mask_reference_arguments(_tex_text_without_comments(_file_text(path, text)))
    findings: list[str] = []
    for word in PRESCRIPTIVE_WORDS:
        pattern = re.compile(rf"(?<![A-Za-z]){word}(?![A-Za-z])", re.IGNORECASE)
        for match in pattern.finditer(text):
            findings.append(
                f"{path}:{text.count(chr(10), 0, match.start()) + 1}: prescriptive word {word!r} "
                f"in {_hit_context(text, match.start(), match.end())!r}"
            )
    return findings


def _content_guard_items(path: str, text: str) -> list[tuple[str, str, bool]]:
    """(guard, message, hard) for the per-file content guards G8, G9, G11,
    G12, G14 and G15."""
    items = [("G8", item, True) for item in _check_fused(path, text)]
    if path.endswith(".tex"):
        items += [("G9", item, True) for item in _stub_markers(path, text)]
        items += [("G11", item, True) for item in _new_macro_defs(path, text)]
        items += [("G12", item, True) for item in _env_balance(path, text)]
        items += [("G14", item, True) for item in _workflow_words(path, text)]
        items += [("G15", item, False) for item in _prescriptive_words(path, text)]
    return items


def _finding_key(guard: str, message: str) -> tuple[str, str]:
    """A guard message without its location (path, line, column and "from
    line N"), for comparing against a baseline. The message keeps what was hit
    (the defined macro, a word with its context), so a changed hit is new."""
    body = re.sub(r"^[^\n]*?:\d+(?::\d+)?: ", "", message, count=1)
    return guard, re.sub(r"\bfrom line \d+", "from line #", body)


def _new_guard_items(path: str, current: str, baseline: str) -> list[tuple[str, str, bool]]:
    """Content-guard hits in `current` beyond those already in `baseline`."""
    remaining = Counter(_finding_key(guard, message) for guard, message, _hard in _content_guard_items(path, baseline))
    new: list[tuple[str, str, bool]] = []
    for guard, message, hard in _content_guard_items(path, current):
        key = _finding_key(guard, message)
        if remaining[key] > 0:
            remaining[key] -= 1
        else:
            new.append((guard, message, hard))
    return new


def _is_cite_command(name: str) -> bool:
    lowered = name.lower()
    return lowered.startswith("cite") or lowered.endswith(("cite", "cites"))


def _cite_arguments(
    text: str, pos: int, name: str
) -> tuple[int, list[tuple[str | None, str]], list[tuple[int, int]]]:
    """Parse the arguments of a cite command whose name ends at `pos`.

    Returns the end position, one (postnote, keys) pair per key group, and
    the (start, end) span of each key group's braces.
    Single cites take up to two optional arguments (the last one is the
    postnote) and one key group. The *cites forms take optional global notes
    in parentheses and then repeated [pre][post]{keys} groups.
    """
    multi = name.lower().endswith("cites")
    if pos < len(text) and text[pos] == "*":
        pos += 1
    if multi:
        for _ in range(2):
            start = _skip_ws(text, pos)
            end = _group_end(text, start) if start < len(text) and text[start] == "(" else None
            if end is None:
                break
            pos = end
    groups: list[tuple[str | None, str]] = []
    spans: list[tuple[int, int]] = []
    while True:
        start = _skip_ws(text, pos)
        options: list[str] = []
        while start < len(text) and text[start] == "[" and len(options) < 2:
            end = _group_end(text, start)
            if end is None:
                break
            options.append(text[start + 1 : end - 1])
            start = _skip_ws(text, end)
        if start >= len(text) or text[start] != "{":
            break
        end = _group_end(text, start)
        if end is None:
            break
        groups.append((options[-1] if options else None, text[start + 1 : end - 1]))
        spans.append((start, end))
        pos = end
        if not multi:
            break
    return pos, groups, spans


def _skip_command_arguments(text: str, pos: int, mandatory: int) -> int:
    """Skip optional [..] arguments and `mandatory` brace groups after a command."""
    if pos < len(text) and text[pos] == "*":
        pos += 1
    while True:
        start = _skip_ws(text, pos)
        if start < len(text) and text[start] == "[":
            end = _group_end(text, start)
            if end is None:
                return pos
            pos = end
            continue
        break
    for _ in range(mandatory):
        start = _skip_ws(text, pos)
        end = _group_end(text, start) if start < len(text) and text[start] == "{" else None
        if end is None:
            return pos
        pos = end
    return pos


COPY_MATH_ENVS = r"(?:equation|align|alignat|flalign|gather|multline|eqnarray|displaymath|math|array)\*?"
# Commands whose arguments are labels, keys or locations, not prose; the value
# is how many mandatory brace groups to drop.
COPY_STRIP_ARGUMENTS = {
    "label": 1,
    "ref": 1,
    "cref": 1,
    "Cref": 1,
    "eqref": 1,
    "pageref": 1,
    "autoref": 1,
    "nameref": 1,
    "hyperref": 0,
    "url": 1,
    "nolinkurl": 1,
    "href": 1,
    "input": 1,
    "include": 1,
    "index": 1,
}


# Commands that carry prose inside math, and how many mandatory arguments
# they take (the prose is the last one).
MATH_TEXT_COMMANDS = {
    **{
        name: 1
        for name in (
            "text", "textrm", "textup", "textnormal", "textit", "textsl", "textbf", "textsf", "texttt",
            "textsc", "textmd", "mbox", "hbox", "emph", "intertext", "shortintertext", "makebox",
            "framebox", "fbox", "mathrm", "operatorname",
        )
    },
    "parbox": 2,
}
MATH_TEXT_RE = re.compile(
    r"\\(" + "|".join(sorted(MATH_TEXT_COMMANDS, key=len, reverse=True)) + r")(?![A-Za-z@])"
)
# An unescaped TeX character: preceded by an even run of backslashes (\\[2pt]
# is a line break, not display math; \$ is a dollar sign).
UNESCAPED = r"(?<!\\)(?:\\\\)*"


def _math_prose(math: str) -> str:
    """The prose a math region carries in \\text, \\mbox, \\intertext,
    \\parbox and similar arguments; the copy guard keeps it when it drops the
    math."""
    pieces: list[str] = []
    covered = 0
    for match in MATH_TEXT_RE.finditer(math):
        if match.start() < covered:
            continue  # nested inside prose already kept
        count = MATH_TEXT_COMMANDS[match.group(1)]
        spans = _mandatory_group_spans(math, match.end(), count)
        if len(spans) == count:
            start, end = spans[-1]
            pieces.append(math[start + 1 : end - 1])
            covered = end
    return " " + " ".join(pieces) + " "


def _strip_for_copy(text: str) -> str:
    """Prose of a TeX file for the copy guard: comments, math (except its
    \\text-like arguments), cite key groups (pre- and postnotes print and
    stay), label-like arguments and command names removed."""
    text = _tex_text_without_comments(text)

    def keep_prose(match: re.Match[str]) -> str:
        return _math_prose(match.group(0))

    text = re.sub(
        rf"\\begin\s*\{{({COPY_MATH_ENVS})\}}.*?\\end\s*\{{\1\}}",
        keep_prose,
        text,
        flags=re.S,
    )
    text = re.sub(
        rf"{UNESCAPED}\\\((?s:.*?){UNESCAPED}\\\)|{UNESCAPED}\\\[(?s:.*?){UNESCAPED}\\\]", keep_prose, text
    )
    text = re.sub(rf"{UNESCAPED}\$\$(?s:.*?){UNESCAPED}\$\$", keep_prose, text)
    text = re.sub(rf"{UNESCAPED}\$(?s:.*?){UNESCAPED}\$", keep_prose, text)
    command_re = re.compile(r"\\([A-Za-z@]+)")
    pieces: list[str] = []
    last = 0
    pos = 0
    while True:
        match = command_re.search(text, pos)
        if match is None:
            break
        name = match.group(1)
        pieces.append(text[last : match.start()])
        end = match.end()
        if _is_cite_command(name):
            # Pre- and postnotes print, so they stay prose; only the key
            # groups go (blanked in place, so positions hold).
            _end, _groups, spans = _cite_arguments(text, end, name)
            for start, stop in spans:
                text = text[:start] + " " * (stop - start) + text[stop:]
        elif name in COPY_STRIP_ARGUMENTS:
            end = _skip_command_arguments(text, end, COPY_STRIP_ARGUMENTS[name])
        pieces.append(" ")
        last = pos = end
    pieces.append(text[last:])
    return "".join(pieces)


def _tokens(text: str) -> list[str]:
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"([A-Za-z])-\s*\n\s*([A-Za-z])", r"\1\2", text)
    text = text.translate(
        str.maketrans(
            {
                "\u2018": "'",
                "\u2019": "'",
                "\u201c": '"',
                "\u201d": '"',
            }
        )
    )
    text = text.replace("``", " ").replace("''", " ")
    # Hyphenated compounds split into their words, so joining copied words
    # with hyphens does not hide a run.
    return re.findall(r"[A-Za-z][A-Za-z0-9']*", text.lower())


def _extract_source_text(path: str) -> str:
    """Text of a held source, cached by the sha256 of its current bytes.
    An empty extraction is not cached, so a failure is retried next time."""
    source = _root(path)
    if not source.is_file():
        return ""
    cache_dir = _root(UNIT_BUILDS / "_srctext")
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache = cache_dir / f"{_sha256_file(source)}.txt"
    if cache.is_file():
        return _read_text(cache)
    text = ""
    suffix = source.suffix.lower()
    if suffix == ".pdf":
        try:
            import fitz  # type: ignore

            doc = fitz.open(source)
            text = "\n".join(page.get_text() for page in doc)
            doc.close()
        except Exception:
            text = ""
    else:
        try:
            text = source.read_text(encoding="utf-8-sig", errors="replace")
        except OSError:
            text = ""
    if text.strip():
        _write_atomic(cache, text)
    return text


CopyIndex = tuple[str, dict[tuple[str, ...], list[int]], list[str]]


def _copy_source_indexes(packet: dict[str, Any]) -> tuple[list[CopyIndex], list[str]]:
    """12-word indexes of the packet's held sources, and findings for sources
    with no extractable text."""
    source_paths = _packet_held_paths(packet)
    findings: list[str] = []
    indexes: list[CopyIndex] = []
    for path in source_paths:
        toks = _tokens(_extract_source_text(path))
        if len(toks) < 12:
            findings.append(f"{path}: held source has no extractable text to compare against")
            continue
        index: dict[tuple[str, ...], list[int]] = defaultdict(list)
        for i in range(len(toks) - 11):
            index[tuple(toks[i : i + 12])].append(i)
        indexes.append((path, index, toks))
    return indexes, findings


CopyRun = tuple[int, str, str]


def _text_copy_runs(text: str, indexes: list[CopyIndex]) -> list[CopyRun]:
    """(length, source, words) of each maximal run of 12 or more words of the
    TeX text's prose that also occurs in a held source."""
    toks = _tokens(_strip_for_copy(text))
    runs: list[CopyRun] = []
    i = 0
    while i <= len(toks) - 12:
        gram = tuple(toks[i : i + 12])
        best_run: tuple[int, str] | None = None
        for source_path, index, source_tokens in indexes:
            if gram not in index:
                continue
            best = 12
            for j in index[gram][:8]:
                k = 12
                while i + k < len(toks) and j + k < len(source_tokens) and toks[i + k] == source_tokens[j + k]:
                    k += 1
                best = max(best, k)
            if best_run is None or best > best_run[0]:
                best_run = (best, source_path)
        if best_run is not None:
            runs.append((best_run[0], best_run[1], " ".join(toks[i : i + best_run[0]])))
            i += best_run[0]
        else:
            i += 1
    return runs


def _classify_copy_runs(path: str, runs: list[CopyRun]) -> tuple[list[str], list[str]]:
    if not runs:
        return [], []
    longest = max(run[0] for run in runs)
    message = f"{path}: copied-prose run longest={longest} count_ge_12={len(runs)}"
    if longest >= 25 or len(runs) >= 3:
        return [message], []
    return [], [message]


def _copy_runs(packet: dict[str, Any], owned: list[str]) -> tuple[list[str], list[str]]:
    indexes, findings = _copy_source_indexes(packet)
    if not indexes and not findings:
        return [], []
    hard: list[str] = []
    for owned_path in owned:
        if not owned_path.endswith(".tex"):
            continue
        runs = _text_copy_runs(_read_text(_root(owned_path)), indexes)
        run_hard, run_findings = _classify_copy_runs(owned_path, runs)
        hard.extend(run_hard)
        findings.extend(run_findings)
    return hard, findings


def _new_copy_runs(packet: dict[str, Any], path: str, current: str, baseline: str) -> tuple[list[str], list[str]]:
    """Copy-guard result for runs in an editable host beyond those already in
    its snapshot text (compared by their words, not only their length)."""
    indexes, _findings = _copy_source_indexes(packet)
    if not indexes or not path.endswith(".tex"):
        return [], []
    remaining = Counter(_text_copy_runs(baseline, indexes))
    new: list[CopyRun] = []
    for run in _text_copy_runs(current, indexes):
        if remaining[run] > 0:
            remaining[run] -= 1
        else:
            new.append(run)
    return _classify_copy_runs(path, new)


PAGE_RANGE = r"(\d{1,5})(?:\s*(?:--|-|–|—|to)\s*(\d{1,5}))?"


def _range_numbers(first: str, second: str | None) -> list[int]:
    """Page numbers of a range; an abbreviated end (545--48) takes the start's
    leading digits."""
    if not second:
        return [int(first)]
    end = int(second)
    if end < int(first) and len(second) < len(first):
        end = int(first[: len(first) - len(second)] + second)
    return [int(first), end]


def _locator_page_numbers(locator: str) -> list[int]:
    """Page numbers in a cite postnote.

    Explicit page markers (p., pp., page, pages) count. A postnote that is only
    numbers, ranges or a list of them is a page locator too, as in biblatex.
    Theorem, section and similar numbers are not pages. Braces, TeX spaces and
    f./ff. suffixes are ignored.
    """
    clean = locator.replace("~", " ").replace("\\,", " ").replace("\\ ", " ")
    clean = clean.replace("{", "").replace("}", "")
    clean = re.sub(r"(\d)\s*ff?\.?(?![A-Za-z])", r"\1", clean)
    clean = re.sub(
        r"\b(?:Thm|Theorem|Lemma|Lem|Prop|Proposition|Cor|Corollary|Def|Definition|"
        r"Sec|Section|Eq|Equation|Ch|Chapter|Ex|Exercise|Fig|Figure|Table|Note|n)\.?\s*\d+(?:\.\d+)*"
        r"|(?:\\S|§)+\s*\d+(?:\.\d+)*",
        " ",
        clean,
        flags=re.IGNORECASE,
    )
    numbers: list[int] = []
    # A page marker covers the whole list after it: "pp. 3, 5--7 and 999".
    separator = r"\s*(?:,|;|\band\b|\\?&)\s*"
    page_list = rf"{PAGE_RANGE}(?:{separator}{PAGE_RANGE})*"
    for match in re.finditer(rf"\b(?:pp?\.?|pages?)\s*{page_list}", clean, re.IGNORECASE):
        for item in re.finditer(PAGE_RANGE, match.group(0)):
            numbers.extend(_range_numbers(item.group(1), item.group(2)))
    if numbers:
        return numbers
    if re.fullmatch(rf"\s*{page_list}\s*", clean):
        for match in re.finditer(PAGE_RANGE, clean):
            numbers.extend(_range_numbers(match.group(1), match.group(2)))
    return numbers


def _int_or_none(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str) and re.fullmatch(r"\s*-?\d+\s*", value):
        return int(value)
    return None


def _entry_page_offset(entry: dict[str, Any]) -> int | None:
    for key in ("printed_offset", "page_offset"):
        value = _int_or_none(entry.get(key))
        if value is not None:
            return value
    return None


def _presentation_start_page(presentation: dict[str, Any]) -> int | None:
    """First printed page of a presentation, from its queue record."""
    records = [presentation] + [
        record for key in RECORD_KEYS for record in _presentation_dicts(presentation.get(key))
    ]
    for record in records:
        for key in ("page_start", "start_page", "contents_start_page", "first_page"):
            value = _int_or_none(record.get(key))
            if value is not None:
                return value
    for record in records:
        pages = record.get("pages")
        if isinstance(pages, str):
            match = re.match(rf"\s*{PAGE_RANGE}", pages)
            if match and match.group(2):
                return int(match.group(1))
    return None


def _printed_offsets(packet: dict[str, Any], held: HeldIndex) -> dict[str, int]:
    """Held path -> printed offset (first printed page - 1), from the packet's
    queue presentations (their recorded start page)."""
    offsets: dict[str, int] = {}
    for unit in packet.get("units") or []:
        for presentation in _presentation_dicts(unit.get("source_presentations") if isinstance(unit, dict) else None):
            start = _presentation_start_page(presentation)
            if start is None:
                continue
            for path in held.paths_for_presentations([presentation]):
                offsets.setdefault(path, start - 1)
    return offsets


def _key_pdf_entries(key: str, held: HeldIndex, packet: dict[str, Any]) -> list[tuple[str | None, dict[str, Any]]]:
    """Held entries (path, entry) for a cite key: by the index's bibkeys, else
    through the packet units' presentations that carry the key (their held
    paths and the index entries of those paths)."""
    found: list[tuple[str | None, dict[str, Any]]] = []
    for entry in held.bibkey_to_entries.get(key, []):
        raw_path = entry.get("path")
        found.append((_try_normalize_repo_path(raw_path) if isinstance(raw_path, str) else None, entry))
    if found:
        return found
    seen: set[str] = set()
    for unit in packet.get("units") or []:
        if not isinstance(unit, dict):
            continue
        for presentation in _presentation_dicts(unit.get("source_presentations")):
            if key not in _presentation_source_ids(presentation):
                continue
            for path in held.paths_for_presentations([presentation]):
                entry = held.path_to_entry.get(path)
                if entry is not None and path not in seen:
                    seen.add(path)
                    found.append((path, entry))
    return found


def _cite_page_findings(owned: list[str], held: HeldIndex, packet: dict[str, Any] | None = None) -> list[str]:
    """G6: numeric page locators for keys mapped to held PDFs must lie within
    printed offset + 1 .. printed offset + PDF page count of some held PDF of
    the key. The offset comes from the held entry, else from the queue
    presentation's start page; when neither records one, 0 is assumed and the
    finding says so."""
    packet = packet or {}
    offsets = _printed_offsets(packet, held)
    findings: list[str] = []
    command_re = re.compile(r"\\([A-Za-z]+)")
    for rel in owned:
        if not rel.endswith(".tex") or not _root(rel).is_file():
            continue
        text = _tex_text_without_comments(_read_text(_root(rel)))
        for match in command_re.finditer(text):
            if not _is_cite_command(match.group(1)):
                continue
            _end, groups, _spans = _cite_arguments(text, match.end(), match.group(1))
            line = _line_of(text, match.start())
            for postnote, keys in groups:
                nums = _locator_page_numbers(postnote or "")
                if not nums:
                    continue
                for key in [k.strip() for k in keys.split(",") if k.strip()]:
                    ranges: list[tuple[int, int, str]] = []
                    for path, entry in _key_pdf_entries(key, held, packet):
                        pages = entry.get("pdf_pages")
                        if not isinstance(pages, int) or isinstance(pages, bool) or pages <= 0:
                            continue
                        offset = _entry_page_offset(entry)
                        note = ""
                        if offset is None and path in offsets:
                            offset = offsets[path]
                        if offset is None:
                            offset = 0
                            note = " (printed offset unknown, 0 assumed)"
                        ranges.append((offset + 1, offset + pages, f"{path or '<unknown>'} printed pages {offset + 1}-{offset + pages}{note}"))
                    for num in nums:
                        if ranges and not any(low <= num <= high for low, high, _label in ranges):
                            findings.append(
                                f"{rel}:{line}: cite locator {num} for {key} lies outside held PDF "
                                + "; ".join(label for _low, _high, label in ranges)
                            )
    return findings


BIB_KEY_FINDING_RE = re.compile(r"bib-key: '([^']*)' not in ")


def _suppress_packet_bib_findings(findings: list[str], intake_keys: set[str]) -> list[str]:
    """Drop bib-key findings whose quoted key is exactly a key of the packet's
    intake bib."""
    result: list[str] = []
    for item in findings:
        match = BIB_KEY_FINDING_RE.match(item)
        if match and match.group(1) in intake_keys:
            continue
        result.append(item)
    return result


LABEL_DEF_RE = re.compile(
    r"\\label\{([^{}]+)\}|\\begin\{(?:hbtheorem|hblemma|hbcorollary|hbdefinition|hbconvention|hbmethod|"
    r"hbexample|hbwarning|proofboundary|systementry|annexitem)\}\s*\{([^{}]+)\}"
)


def _attribution_patterns(
    packet: dict[str, Any],
    paths: Iterable[str],
    texts: Iterable[str],
) -> list[re.Pattern[str]]:
    """Patterns that tie a check.py finding to this packet: its owned and
    editable paths, labels defined in those files (now or at the snapshot),
    and its label tag."""
    # check.py names a location as "rel:line", so a path token may be followed
    # by ":<digits>"; labels and keys may not be followed by ":" or "." and a
    # word character (sec:a is not sec:a:b).
    path_tokens: set[str] = set()
    for rel in paths:
        path_tokens.add(rel)
        if rel.startswith("handbook/"):
            path_tokens.add(rel[len("handbook/") :])
    patterns = [
        re.compile(r"(?<![\w:./-])" + re.escape(token) + r"(?![\w-]|[:.][A-Za-z_])")
        for token in sorted(path_tokens)
    ]
    tokens: set[str] = set()
    for text in texts:
        for match in LABEL_DEF_RE.finditer(text):
            tokens.add((match.group(1) or match.group(2)).strip())
        for match in re.finditer(r"\\([A-Za-z]+)", text):
            if _is_cite_command(match.group(1)):
                _end, groups, _spans = _cite_arguments(text, match.end(), match.group(1))
                tokens.update(key.strip() for _note, keys in groups for key in keys.split(","))
    patterns += [
        re.compile(r"(?<![\w:./-])" + re.escape(token) + r"(?![\w-]|[:.]\w)")
        for token in sorted(tokens)
        if token
    ]
    tag = packet.get("label_tag")
    if isinstance(tag, str) and tag:
        patterns.append(re.compile(r"(?<![\w-])" + re.escape(tag) + r"(?![\w])"))
    return patterns


def _held_path_problems(packet: dict[str, Any], snapshot_data: dict[str, Any], held: HeldIndex) -> list[str]:
    """Held sources whose bytes differ from the hash the snapshot pinned or
    the held index records, or that have no recorded hash at all."""
    pinned = snapshot_data.get("held_paths")
    pinned = pinned if isinstance(pinned, dict) else {}
    problems: list[str] = []
    for path in _packet_held_paths(packet):
        current = _sha256_file(_root(path)) if _root(path).is_file() else None
        expected: list[tuple[str, Any]] = []
        if path in pinned:
            expected.append(("snapshot", pinned[path]))
        entry_sha = held.path_to_entry.get(path, {}).get("sha256")
        if isinstance(entry_sha, str):
            expected.append(("held index", entry_sha.strip().lower()))
        if not expected:
            problems.append(f"{path}: held source has no recorded sha256 to check against")
        for where, sha in expected:
            if sha != current:
                problems.append(f"{path}: held source bytes differ from the {where} sha256 (replaced or edited)")
    return problems


def verify(args: argparse.Namespace) -> int:
    packet_path, packet = _load_packet(args.packet)
    wave_dir = packet_path.parent.parent
    wave = wave_dir.name

    def refuse(problem: str) -> int:
        print(json.dumps({"hard": [problem], "findings": []}, ensure_ascii=False, indent=2))
        return 1

    # The snapshot comes from the wave-base commit, never the working tree.
    base_sha, problem = _wave_base_sha(wave_dir)
    if base_sha is None:
        return refuse(f"G1 {problem}")
    snapshot_rel = _rel(_snapshot_path(packet_path, packet))
    snapshot_bytes = _git_blobs(base_sha, [snapshot_rel])[snapshot_rel]
    if snapshot_bytes is None:
        return refuse(f"G1 snapshot {snapshot_rel} is not in the wave-base commit {base_sha}")
    expected_digest = getattr(args, "snapshot_sha256", None)
    if expected_digest and expected_digest.strip().lower() != hashlib.sha256(snapshot_bytes).hexdigest():
        return refuse(f"G1 snapshot at {base_sha} does not match --snapshot-sha256")
    try:
        snapshot_data = json.loads(snapshot_bytes.decode("utf-8-sig"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        return refuse(f"G1 snapshot {snapshot_rel} at {base_sha} is not JSON: {exc}")
    if not isinstance(snapshot_data, dict):
        return refuse(f"G1 snapshot {snapshot_rel} at {base_sha} is not a JSON object")
    hard: list[str] = []
    findings: list[str] = []
    snapshot_owned_raw = snapshot_data.get("owned_files")
    snapshot_editable_raw = snapshot_data.get("editable_hosts")
    if not isinstance(snapshot_owned_raw, dict):
        hard.append("G1 snapshot lacks owned_files map")
        snapshot_owned_raw = {}
    if not isinstance(snapshot_editable_raw, dict):
        hard.append("G1 snapshot lacks editable_hosts map")
        snapshot_editable_raw = {}
    host_baselines = snapshot_data.get("editable_host_text")
    if not isinstance(host_baselines, dict):
        hard.append("G1 snapshot lacks editable_host_text map")
        host_baselines = {}
    snapshot_owned = {_normalize_repo_path(p) for p in snapshot_owned_raw}
    snapshot_editable = {_normalize_repo_path(p) for p in snapshot_editable_raw}
    packet_owned = {_normalize_repo_path(p) for p in packet.get("owned_files", [])}
    packet_editable = {_normalize_repo_path(p) for p in packet.get("editable_hosts", [])}
    # Every guard input that comes from the packet (owned files, editable hosts,
    # held_paths) is pinned by the snapshot.
    if snapshot_data.get("packet_sha256") != _sha256_file(packet_path):
        hard.append("G1 packet JSON changed since the snapshot (or the snapshot lacks packet_sha256)")
    if packet_owned != snapshot_owned:
        hard.append("G1 packet owned_files differ from snapshot")
    if packet_editable != snapshot_editable:
        hard.append("G1 packet editable_hosts differ from snapshot")
    hard.extend(
        f"G1 {problem}"
        for problem in _ownership_problems(
            packet_path,
            {**packet, "owned_files": sorted(snapshot_owned), "editable_hosts": sorted(snapshot_editable)},
            check_labels=False,
        )
    )
    owned = [path for path in sorted(snapshot_owned) if _root(path).is_file()]
    editable = [path for path in sorted(snapshot_editable) if _root(path).is_file()]
    allowed = {_path_key(rel) for rel in snapshot_owned | snapshot_editable}
    # Other packets of the wave (recorded at the snapshot): their owned files
    # and editable hosts change concurrently. The wave's assessment files are
    # written by the workflow.
    other_packets: dict[str, list[str]] = defaultdict(list)
    wave_paths = snapshot_data.get("wave_packet_paths")
    for other_id, paths in (wave_paths.items() if isinstance(wave_paths, dict) else []):
        for item in paths if isinstance(paths, list) else []:
            normalized = _try_normalize_repo_path(item) if isinstance(item, str) else None
            if normalized:
                other_packets[_path_key(normalized)].append(str(other_id))
    assessments = f"{COVERAGE.as_posix()}/assessments/{wave}"

    baseline_tree = snapshot_data.get("tree")
    baseline_tree = baseline_tree if isinstance(baseline_tree, dict) else {}
    current_prefilter = _scan_tree_state()
    changed_candidates = set(current_prefilter) | set(baseline_tree)
    for rel in sorted(changed_candidates):
        old = baseline_tree.get(rel)
        new_meta = current_prefilter.get(rel)
        changed = not isinstance(old, dict) or new_meta is None
        if isinstance(old, dict) and new_meta is not None:
            changed = old.get("size") != new_meta.get("size") or old.get("mtime_ns") != new_meta.get("mtime_ns")
            if changed:
                new_sha = _sha256_file(_root(rel))
                changed = new_sha != old.get("sha256")
        if not changed or _path_key(rel) in allowed or _path_has_prefix(rel, assessments):
            continue
        owners = other_packets.get(_path_key(rel))
        if owners:
            findings.append(
                f"G1 {rel} changed: a file of packet {', '.join(sorted(set(owners)))}, not of {packet.get('id')} "
                "(a cross-packet edit if this packet made it)"
            )
        else:
            hard.append(f"G1 changed outside owned/editable set: {rel}")

    # G2 against the wave-base commit.
    frozen_snapshot = snapshot_data.get("frozen_files")
    frozen_rels = sorted(set(frozen_snapshot if isinstance(frozen_snapshot, dict) else {}) | set(_frozen_files()))
    for rel, base_bytes in _git_blobs(base_sha, frozen_rels).items():
        path = _root(rel)
        current = _sha256_file(path) if path.is_file() else None
        if current != (hashlib.sha256(base_bytes).hexdigest() if base_bytes is not None else None):
            hard.append(f"G2 frozen file changed since the wave-base commit {base_sha[:12]}: {rel}")

    intake_keys: set[str] = set()
    for rel in packet.get("owned_files", []):
        rel = _normalize_repo_path(rel)
        path = _root(rel)
        if rel.endswith(".bib") and path.is_file():
            try:
                intake_keys.update(_parse_intake_bib(path))
            except UsageError as exc:
                hard.append(f"G5 {exc}")
        if rel.endswith(".csv") and path.is_file():
            try:
                header = _read_csv_header(path)
            except (OSError, csv.Error, UnicodeDecodeError) as exc:
                hard.append(f"G5 {_rel(path)}: unreadable CSV: {exc}")
                continue
            if header != SYMBOL_HEADER:
                hard.append(f"G5 {rel}: bad CSV header {header!r}")
            hard.extend(f"G5 {rel}: {item}" for item in _numeric_scope_problems(path))

    # G3/G4: whole-tree check.py findings new since the snapshot. A new finding
    # that names this packet's files, labels or label tag is hard; any other
    # new finding (for example from a concurrent packet) is reported.
    baseline_findings = set(snapshot_data.get("check_findings") or [])
    current_check_items = _run_check_findings()
    for item in current_check_items:
        if item.startswith("__check_error__:"):
            hard.append(f"G3/G4 {item.split(':', 1)[1].strip()}")
    current_findings = {item for item in current_check_items if not item.startswith("__check_error__:")}
    new_findings = sorted(current_findings - baseline_findings)
    texts = [_decoded_text(rel) for rel in owned + editable if rel.endswith(".tex")]
    texts.extend(text for text in host_baselines.values() if isinstance(text, str))
    patterns = _attribution_patterns(packet, sorted(snapshot_owned | snapshot_editable), texts)
    for item in _suppress_packet_bib_findings(new_findings, intake_keys):
        category = item.split(":", 1)[0]
        if category not in CHECK_CATEGORIES:
            continue
        if any(pattern.search(item) for pattern in patterns):
            hard.append(f"G3/G4 {item}")
        else:
            findings.append(f"G3/G4 new finding not tied to this packet: {item}")

    held = _load_held_sources()
    if not held.available:
        hard.append(f"G13 held index unavailable: {held.unavailable_reason}")
    else:
        findings.extend(f"G6 {item}" for item in _cite_page_findings(owned, held, packet))
    hard.extend(f"G13 {item}" for item in _held_path_problems(packet, snapshot_data, held))

    for rel in owned:
        encoding_problems = _encoding_guard(rel)
        hard.extend(f"G16 {item}" for item in encoding_problems)
        if encoding_problems:
            continue
        for guard, item, is_hard in _content_guard_items(rel, _read_text(_root(rel))):
            (hard if is_hard else findings).append(f"{guard} {item}")

    # Editable hosts: the same content guards, counting only hits that are new
    # relative to the host text recorded at the snapshot.
    for rel in editable:
        current = _decoded_text(rel)
        baseline = host_baselines.get(rel)
        if not isinstance(baseline, str):
            baseline = ""
        if current.count("\ufffd") > baseline.count("\ufffd"):
            hard.append(f"G16 {rel}: new non-UTF-8 bytes or U+FFFD")
        for guard, item, is_hard in _new_guard_items(rel, current, baseline):
            (hard if is_hard else findings).append(f"{guard} {item}")
        if held.available:
            copy_hard, copy_findings = _new_copy_runs(packet, rel, current, baseline)
            hard.extend(f"G13 {item}" for item in copy_hard)
            findings.extend(f"G13 {item}" for item in copy_findings)

    # G10 needs owned body/annex files to build; a unit_accounting packet may
    # own none, or none an author has written yet.
    if any(_unit_compile_files(packet)):
        compile_result = unit_compile_packet(packet, run_build=True)
        if not compile_result.get("ok"):
            hard.append(f"G10 unit compile failed: {compile_result}")
    else:
        findings.append("G10 not applicable: the packet owns no body or annex .tex file to compile")

    if held.available:
        copy_hard, copy_findings = _copy_runs(packet, owned)
        hard.extend(f"G13 {item}" for item in copy_hard)
        findings.extend(f"G13 {item}" for item in copy_findings)

    verdict = {"hard": hard, "findings": findings}
    print(json.dumps(verdict, ensure_ascii=False, indent=2))
    return 1 if hard else 0


def _printed_ordinal(part: str) -> int:
    n = int(part[1:])
    if 1 <= n <= 10:
        return n
    if 15 <= n <= 19:
        return n - 4
    if 11 <= n <= 14:
        return n + 5
    raise UsageError(f"unsupported part {part}")


def _input_without_tex(path: str) -> str:
    rel = _handbook_rel(path)
    return rel[:-4] if rel.endswith(".tex") else rel


def _unit_compile_files(packet: dict[str, Any]) -> tuple[list[str], list[str]]:
    """(bodies, annexes) the unit compile builds. A section packet: its owned
    body and annex .tex pair (both or nothing). A unit_accounting packet owns
    some, one or none of its units' proposed destinations and an author may
    write only some of them: every owned body and annex .tex file on disk."""
    part_lower = _part_dir(str(packet.get("part")))
    owned = [_normalize_repo_path(path) for path in packet.get("owned_files", [])]
    bodies = [p for p in owned if p.startswith(f"handbook/parts/{part_lower}/") and p.endswith(".tex")]
    annexes = [p for p in owned if p.startswith(f"handbook/annex/{part_lower}/") and p.endswith(".tex")]
    if _packet_mode(packet) == "unit_accounting":
        return [p for p in bodies if _root(p).is_file()], [p for p in annexes if _root(p).is_file()]
    if not bodies or not annexes:
        return [], []
    return bodies[:1], annexes[:1]


def _unit_template(packet: dict[str, Any]) -> str:
    part = str(packet.get("part"))
    part_lower = _part_dir(part)
    owned = [_normalize_repo_path(path) for path in packet.get("owned_files", [])]
    bodies, annexes = _unit_compile_files(packet)
    if not bodies and not annexes:
        raise UsageError("packet lacks owned body and annex .tex files to compile")
    intake_bib = next((path for path in owned if path.startswith("handbook/bib/intake-") and path.endswith(".bib")), None)
    # A unit packet records a heading level per set of proposing units.
    body_levels = {
        _normalize_repo_path(rel): item.get("heading_level")
        for item in packet.get("insertions") or []
        if isinstance(item, dict)
        for rel in item.get("owned_files") or []
        if isinstance(rel, str)
    }
    body_lines = ""
    for body in bodies:
        heading = body_levels.get(body) or packet.get("heading_level") or "\\chapter"
        if heading == "\\section":
            body_lines += "\\chapter{Scoped host}\n"
        elif heading == "\\subsection":
            body_lines += "\\chapter{Scoped host}\n\\section{Scoped section host}\n"
        body_lines += f"\\input{{{_input_without_tex(body)}}}\n"
    annex_lines = ""
    if annexes:
        annex_lines = "\\hbannexsetup\n" f"\\hbannexchapter{{{int(part[1:])}}}{{Scoped annex}}\n"
        for annex in annexes:
            if _first_heading(annex) == "\\subsection":
                annex_lines += "\\section{Scoped annex host}\n"
            annex_lines += f"\\input{{{_input_without_tex(annex)}}}\n"
        annex_lines += "\\hbannexfinish\n"
    bib_line = ""
    if intake_bib and _root(intake_bib).is_file():
        bib_line = f"\\addbibresource{{{_handbook_rel(intake_bib)}}}\n"
    return (
        "\\documentclass[11pt]{book}\n"
        "\\usepackage{handbook}\n"
        "\\usepackage[backend=biber,style=alphabetic]{biblatex}\n"
        "\\addbibresource{bib/handbook.bib}\n"
        f"{bib_line}"
        "\\input{bib/inherited-keys}\n"
        "\\begin{document}\n"
        f"\\setcounter{{part}}{{{_printed_ordinal(part) - 1}}}\n"
        f"\\hbpartidentity{{{part_lower}}}\\part{{Scoped unit check}}\n"
        f"{body_lines}"
        f"{annex_lines}"
        "\\backmatter\\printbibliography\n"
        "\\end{document}\n"
    )


def _texlive_command(name: str) -> str | None:
    candidate = Path("C:/texlive/2025/bin/windows") / f"{name}.exe"
    if candidate.is_file():
        return str(candidate)
    return None


# -file-line-error reports errors as "<file>:<line>: <message>".
FILE_LINE_ERROR_RE = re.compile(r"^(?:[A-Za-z]:)?[^:\s][^:]*:\d+: ")


UNDEFINED_WARNING_RE = re.compile(
    r"\b(citation|reference)\s+[`']([^'`\n]+(?:\n[^'`\n]+)?)'\s+on\s+page\s+\S+\s+undefined",
    re.IGNORECASE,
)
TEX_LOG_LINE_BYTES = 79  # TeX Live max_print_line


def _unwrap_tex_log(raw: bytes) -> str:
    """Log text with TeX's hard wraps undone: a line exactly max_print_line
    bytes long continues on the next line."""
    pieces: list[bytes] = []
    for line in raw.replace(b"\r\n", b"\n").split(b"\n"):
        pieces.append(line)
        pieces.append(b"" if len(line) == TEX_LOG_LINE_BYTES else b"\n")
    return b"".join(pieces).decode("utf-8", errors="replace")


def _parse_unit_log(out_dir: Path) -> dict[str, Any]:
    log = out_dir / "unit.log"
    blg = out_dir / "unit.blg"
    errors: list[str] = []
    undefined_citations: list[str] = []
    undefined_refs: list[str] = []
    overfull = 0
    if log.is_file():
        text = _unwrap_tex_log(log.read_bytes())
        for line in text.splitlines():
            if (
                line.startswith("! ")
                or FILE_LINE_ERROR_RE.match(line)
                or "Undefined control sequence" in line
                or "multiply defined" in line
                or "Missing character" in line
            ):
                errors.append(line)
            if line.startswith("Overfull \\"):
                overfull += 1
        # "Citation `k' ...", "Reference `l' ...", "Hyper reference `l' ...";
        # a name may still span a line break that the unwrapping missed.
        for match in UNDEFINED_WARNING_RE.finditer(text):
            name = re.sub(r"\s*\n\s*", "", match.group(2))
            if match.group(1).lower() == "citation":
                undefined_citations.append(name)
            else:
                undefined_refs.append(name)
        # biblatex reports undefined citations under "There were undefined
        # references" too, so the summary is a signal only when no name parsed.
        summary = re.search(r"There were undefined (?:references|citations)", text, re.IGNORECASE)
        if summary and not undefined_citations and not undefined_refs:
            errors.append(f"{summary.group(0)} reported, but no undefined name could be parsed from the log")
    else:
        errors.append(f"{_rel(log)} was not written")
    if blg.is_file():
        for line in blg.read_text(encoding="utf-8", errors="replace").splitlines():
            if re.search(r"\b(?:WARN|ERROR)\b", line):
                errors.append(line)
    known_labels = _existing_labels()
    unknown_refs = sorted({ref for ref in undefined_refs if ref not in known_labels})
    return {
        "ok": not errors and not undefined_citations and not unknown_refs,
        "errors": errors,
        "undefined_citations": sorted(set(undefined_citations)),
        "undefined_refs_unknown": unknown_refs,
        "overfull": overfull,
    }


def unit_compile_packet(packet: dict[str, Any], *, run_build: bool) -> dict[str, Any]:
    stem = str(packet.get("id") or "packet")
    out_dir = _root(UNIT_BUILDS / stem)
    unit_tex = out_dir / "unit.tex"
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_atomic(unit_tex, _unit_template(packet))
    if not run_build:
        return {"ok": True, "unit_tex": _rel(unit_tex), "errors": [], "undefined_citations": [], "undefined_refs_unknown": [], "overfull": 0}
    pdflatex = _texlive_command("pdflatex")
    biber = _texlive_command("biber")
    missing = [
        name for name, command in (("pdflatex", pdflatex), ("biber", biber))
        if command is None
    ]
    if missing:
        return {
            "ok": False,
            "errors": [
                f"TeX Live 2025 executable missing: C:/texlive/2025/bin/windows/{name}.exe"
                for name in missing
            ],
            "undefined_citations": [],
            "undefined_refs_unknown": [],
            "overfull": 0,
        }
    commands = [
        [
            pdflatex,
            "-no-shell-escape",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-file-line-error",
            f"-output-directory={out_dir.resolve()}",
            str(unit_tex.resolve()),
        ],
        [biber, "--input-directory", str(out_dir.resolve()), "--output-directory", str(out_dir.resolve()), "unit"],
        [
            pdflatex,
            "-no-shell-escape",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-file-line-error",
            f"-output-directory={out_dir.resolve()}",
            str(unit_tex.resolve()),
        ],
        [
            pdflatex,
            "-no-shell-escape",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-file-line-error",
            f"-output-directory={out_dir.resolve()}",
            str(unit_tex.resolve()),
        ],
    ]
    exit_errors: list[str] = []
    for command in commands:
        try:
            proc = subprocess.run(
                command,
                cwd=_root("handbook"),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=600,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            return {
                "ok": False,
                "errors": [f"failed to run {command[0]}: {exc}"],
                "undefined_citations": [],
                "undefined_refs_unknown": [],
                "overfull": 0,
            }
        if proc.returncode != 0:
            exit_errors.append(f"{Path(command[0]).name} exited {proc.returncode}")
    result = _parse_unit_log(out_dir)
    if exit_errors:
        result["errors"] = exit_errors + result["errors"]
        result["ok"] = False
    return result


def unit_compile(args: argparse.Namespace) -> int:
    _, packet = _load_packet(args.packet)
    result = unit_compile_packet(packet, run_build=True)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("ok") else 1


def report(args: argparse.Namespace) -> int:
    wave = args.wave
    root = _root(WAVES_ROOT / wave)
    results = _load_json(root / "results.json", {}) if (root / "results.json").is_file() else {}
    verdicts: list[dict[str, Any]] = []
    for path in sorted((root / "verdicts").glob("*.json")) if (root / "verdicts").is_dir() else []:
        data = _load_json(path, None)
        if isinstance(data, dict):
            verdicts.append({"path": path.relative_to(ROOT).as_posix(), **data})
    hard = sum(len(v.get("hard", [])) for v in verdicts)
    findings = sum(len(v.get("findings", [])) for v in verdicts)
    print(f"# Wave {wave} report")
    print()
    if results:
        print("## Results")
        for key in sorted(results):
            value = results[key]
            if isinstance(value, (str, int, float, bool)) or value is None:
                print(f"- {key}: {value}")
        print()
    print("## Verdicts")
    print(f"- verdict files: {len(verdicts)}")
    print(f"- hard guard items: {hard}")
    print(f"- non-hard findings: {findings}")
    for verdict in verdicts:
        name = verdict.pop("path")
        h = len(verdict.get("hard", []))
        f = len(verdict.get("findings", []))
        print(f"- {name}: hard={h} findings={f}")
    return 1 if hard else 0


def _build_fixture(root: Path) -> None:
    for rel in (
        "spec/coverage/edition-2026/current-fulfillment",
        "spec/coverage/edition-2026",
        "spec",
        "handbook/parts/p01",
        "handbook/annex/p01",
        "handbook/bib",
        "handbook/registry",
    ):
        (root / rel).mkdir(parents=True, exist_ok=True)
    (root / "handbook/main.tex").write_text("\\input{parts/p01}\n\\input{annex/p01-route}\n", encoding="utf-8", newline="\n")
    (root / "handbook/annex/p01-route.tex").write_text(
        "\\hbannexchapter{1}{P1}\\label{annex:p01}\n\\input{annex/p01/kept}\n", encoding="utf-8", newline="\n"
    )
    (root / "handbook/annex/p01/kept.tex").write_text("\\section{Kept}\n", encoding="utf-8", newline="\n")
    (root / "handbook/parts/p01.tex").write_text("\\hbpartidentity{p01}\n\\part{P1}\n\\input{parts/p01/existing}\n", encoding="utf-8", newline="\n")
    (root / "handbook/parts/p01/existing.tex").write_text("\\chapter{Existing}\\label{sec:existing}\n", encoding="utf-8", newline="\n")
    (root / "handbook/annex/p01.tex").write_text("\\hbannexchapter{1}{P1}\\label{annex:p01}\n", encoding="utf-8", newline="\n")
    (root / "handbook/handbook.sty").write_text("", encoding="utf-8", newline="\n")
    (root / "handbook/bib/handbook.bib").write_text("", encoding="utf-8", newline="\n")
    (root / "handbook/registry/symbols.csv").write_text(",".join(SYMBOL_HEADER) + "\n", encoding="utf-8", newline="\n")
    (root / "handbook/registry/symbol-scopes.json").write_text('{"schema_version":1,"scopes":{}}\n', encoding="utf-8", newline="\n")
    toc = {
        "parts": [
            {
                "stable_part_id": "P1",
                "chapters": [
                    {
                        "number": 1,
                        "title": "Alpha Chapter",
                        "numbered_sections": [
                            {"number": "1.1", "title": "A"},
                            {"number": "1.2", "title": "B"},
                        ],
                    }
                ],
            }
        ]
    }
    (root / "spec/proposed-table-of-contents.json").write_text(json.dumps(toc), encoding="utf-8", newline="\n")
    rows = [
        {
            "part": "P1",
            "chapter_id": "1",
            "chapter_title": "Alpha Chapter",
            "section_id": "1.1",
            "section_title": "A",
            "status": "partial",
            "reader_evidence": [{"path": "handbook/parts/p01/existing.tex", "anchor": "sec:existing"}],
            "source_facets": [{"unit_id": "U1"}],
            "missing_pieces": ["x"],
            "unassessed_scope": [],
        },
        {
            "part": "P1",
            "chapter_id": "1",
            "chapter_title": "Alpha Chapter",
            "section_id": "1.2",
            "section_title": "B",
            "status": "missing",
            "reader_evidence": [],
            "source_facets": [{"unit_id": "U1"}],
            "missing_pieces": ["y"],
            "unassessed_scope": [],
        },
    ]
    with (root / "spec/coverage/edition-2026/current-fulfillment/p01-p03.jsonl").open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row) + "\n")
    unit = {
        "unit_id": "U1",
        "title": "Unit One",
        "required_components": [
            {"component_id": "C1", "description": "d", "success_condition": "s", "failure_condition": "f"}
        ],
        "source_presentations": [{"source_id": "S1"}],
        "destination": {"body": {"proposed_path": "handbook/parts/p01/u1.tex", "proposed_label": "sec:u1"}},
    }
    (root / "spec/coverage/edition-2026/completion-work-queue.jsonl").write_text(json.dumps(unit) + "\n", encoding="utf-8", newline="\n")
    held = {"entries": [{"path": "source/s1.txt", "source_ids": ["S1"], "bibkeys": [], "sha256": "abc"}], "source_index": {"S1": ["source/s1.txt"]}}
    (root / "spec/coverage/edition-2026/held-sources.json").write_text(json.dumps(held), encoding="utf-8", newline="\n")


def assert_refusal(action: Any) -> str:
    try:
        action()
    except Refusal as exc:
        return str(exc)
    raise AssertionError("expected a refusal")


def _fixture_write(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _fixture_commit_base(wave: str) -> str:
    """Commit the whole fixture tree (its own git repository under the
    selftest's temp directory) and record the commit as the wave's base_sha."""
    git = ["git", "-C", str(ROOT), "-c", "user.name=waves-selftest", "-c", "user.email=selftest@invalid"]
    if not (ROOT / ".git").exists():
        subprocess.run(git + ["init", "-q"], check=True)
    subprocess.run(git + ["add", "-A"], check=True)
    subprocess.run(git + ["commit", "-q", "--allow-empty", "-m", "wave base"], check=True)
    sha = subprocess.run(git + ["rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip()
    args_path = ROOT / WAVES_ROOT / wave / "args.json"
    data = _load_json(args_path, {}) if args_path.is_file() else {}
    _write_json_atomic(args_path, {**data, "base_sha": sha})
    return sha


def _selftest_integrity(base: Path) -> None:
    """Source gate, guards on editable hosts, G3/G4 attribution, snapshot
    protection, word and definition guards, G6 locators, G13 math prose."""
    global ROOT
    ROOT = base
    write = _fixture_write

    # Source gate: a recorded file with a matching hash is held; a stale hash,
    # a free-text note or a bare key with no record is not.
    write("source/formal-logic-reference.tex", "frozen reference text\n")
    write("handbook/parts/p01/presentation.tex", "\\section{Presented}\n")
    write("source/references/kr/kr-1995.pdf", "pdf bytes\n")
    flr_sha = _sha256_file(ROOT / "source/formal-logic-reference.tex").upper()
    pres_sha = _sha256_file(ROOT / "handbook/parts/p01/presentation.tex")
    kr_sha = _sha256_file(ROOT / "source/references/kr/kr-1995.pdf").upper()
    write(
        "spec/research/edition-2026-p15-kr.md",
        f"Local original:\nsource/references/kr/kr-1995.pdf\nSHA: {kr_sha}.\nsource/references/kr/other.pdf has no hash.\n",
    )
    kr_presentation = {
        "citation_key": "KR1995",
        "bibliographic_records": [{"path": "handbook/bib/handbook.bib", "page_start": 545}],
        "required_extent": {"author_scope_records": ["spec/research/edition-2026-p15-kr.md"]},
    }
    units = {
        "UF": {"unit_id": "UF", "source_presentations": [{"source_id": "FLRV1", "title": "Frozen formal-logic reference", "artifacts": [{"path": "source/formal-logic-reference.tex", "exists": True, "sha256": flr_sha}]}]},
        "US": {"unit_id": "US", "source_presentations": [{"source_id": "FLRV1", "artifacts": [{"path": "source/formal-logic-reference.tex", "sha256": "0" * 64}]}]},
        "UH": {"unit_id": "UH", "source_presentations": [{"source_id": "handbook-mathematical-presentation:X", "artifacts": [{"path": "handbook/parts/p01/presentation.tex", "sha256": pres_sha}]}]},
        "UK": {"unit_id": "UK", "source_presentations": [kr_presentation]},
        "UN": {"unit_id": "UN", "source_presentations": [{"citation_key": "Nope", "doi": "10.1/x", "local_artifacts": ["Exact held previews still require locating/acquisition."]}]},
    }
    empty = HeldIndex(available=True)

    def gate_rows(*unit_ids: str) -> list[dict[str, Any]]:
        return [{"section_id": "9.1", "status": "partial",
                 "missing_pieces": [{"kind": "blocked_source", "duty": "source not held"}],
                 "source_facets": [{"unit_id": unit_id} for unit_id in unit_ids]}]

    for unit_id in ("UF", "UH", "UK"):
        assert not _is_source_blocked(gate_rows(unit_id), units, empty, {}), unit_id
    for unit_id in ("US", "UN"):
        assert _is_source_blocked(gate_rows(unit_id), units, empty, {}), unit_id
    held_paths = {unit["unit_id"]: unit["held_paths"] for unit in _packet_units(gate_rows("UF", "UH", "UK"), units, empty)}
    assert held_paths == {"UF": ["source/formal-logic-reference.tex"], "UH": [], "UK": ["source/references/kr/kr-1995.pdf"]}, held_paths
    record = _blocker_record("wt", gate_rows("UN", "US"), units)
    assert record["source_ids"] == ["10.1/x", "FLRV1", "Nope"], record
    assert "Exact held previews still require locating/acquisition." not in _presentation_identities(units["UN"]["source_presentations"])

    # Word and definition guards.
    owned_rel = "handbook/parts/p01/new-wt-p01-001.tex"
    write(owned_rel, "\\cite{Todorcevic1984Trees} A mastodon. \\label{sec:TODO-later} Todo lists.\n")
    assert _stub_markers(owned_rel) == []
    write(owned_rel, "TODO\nFIXME and TBD. Details omitted.\n")
    assert len(_stub_markers(owned_rel)) == 4
    write(owned_rel, "It was reviewed; reviews, ledgers, assessors and intakes.\n")
    assert len(_workflow_words(owned_rel)) == 5
    write(owned_rel, "\\label{sec:review-of-x} \\ref{sec:review-of-x} \\cite[p.~2]{Wave2001} "
          "\\begin{hbtheorem}{thm:ledger}{proved=annex:intake}{Main}x\\end{hbtheorem}\n")
    assert _workflow_words(owned_rel) == []
    for definition in ("\\newif\\ifdone", "\\newcounter{c}", "\\newlength{\\l}", "\\DeclareMathSymbol{\\x}{\\mathord}{a}{1}", "\\csdef{x}{y}",
                       "\\newrobustcmd{\\x}{y}", "\\renewrobustcmd*{\\x}{y}", "\\providerobustcmd{\\x}{y}",
                       "\\@namedef{x}{y}", "\\chardef\\x=1", "\\mathchardef\\x=1", "\\countdef\\x=1",
                       "\\newcommandx{\\x}{y}", "\\renewcommandx\\x{y}", "\\providecommandx{\\x}{y}",
                       "\\cs_new:Npn \\x {y}", "\\cs_set_protected:Npn \\x #1 {y}", "\\cs_gset_nopar:Npn \\x {y}",
                       "\\cs_new_eq:NN \\x \\y", "\\futurelet\\x\\y\\z"):
        write(owned_rel, definition + "\n")
        assert _new_macro_defs(owned_rel), definition
    # Stub phrases match across any whitespace, line breaks and comments
    # included.
    for text in ("is left to the\nreader.", "Details % a comment\n   omitted.", "The remaining\tcases\n are similar.",
                 "Omitted\nfor\nbrevity."):
        assert len(_stub_markers("x.tex", text + "\n")) == 1, text
    # G5: numeric scopes and first uses, as PNN.k anywhere or a bare part or
    # part range; named scopes and the notes column pass.
    csv_rel = "handbook/registry/symbols-intake-p01-x.csv"
    write(csv_rel, ",".join(SYMBOL_HEADER) + "\n"
          "A,\\A,r,P5-P19,,sec:x,see P13.2\n"
          "B,\\B,r,P5,,P3.1,\n"
          "C,\\C,r,Legacy P4.2-P4.5 meaning,,sec:y,\n"
          "D,\\D,r,P17 arithmetic-coding,,sec:z,\n"
          "E,\\E,r,global,,sec:z,\n")
    assert _numeric_scope_problems(ROOT / csv_rel) == [
        "row 2: numeric scope 'P5-P19'",
        "row 3: numeric scope 'P5'",
        "row 3: numeric first_use 'P3.1'",
        "row 4: numeric scope 'Legacy P4.2-P4.5 meaning'",
    ], _numeric_scope_problems(ROOT / csv_rel)
    # G6: a page marker covers every number in the list after it.
    assert _locator_page_numbers("pages 3 and 999") == [3, 999]
    assert _locator_page_numbers("pp.~3, 5--7 \\& 12") == [3, 5, 7, 12]
    assert _locator_page_numbers("3 and 5") == [3, 5]
    assert _locator_page_numbers("Thm.~4.2 and p.~7") == [7]
    # Cite pre- and postnotes are prose; only key groups are masked. A % in a
    # URL starts no comment.
    for text, guard in (
        ("\\cite[TODO: find page]{K}", _stub_markers),
        ("\\cite[details omitted]{K}", _stub_markers),
        ("\\cite[the wave ledger review]{K}", _workflow_words),
        ("\\cite[reviewed in][3]{K}", _workflow_words),
        ("\\parencites[see][the intake]{A}[2]{B}", _workflow_words),
        ("\\url{http://x/a%b} TODO", _stub_markers),
        ("\\url|http://x/a%b| TODO", _stub_markers),
    ):
        write(owned_rel, text + "\n")
        assert guard(owned_rel), text
    write(owned_rel, "\\cite[p.~2]{Review1999,Wave2001} \\label{sec:wave} \\autocites(see)[3]{Ledger}[4]{Intake}\n")
    assert _workflow_words(owned_rel) == [] and _stub_markers(owned_rel) == []

    # Census verdicts: exact tokens only; negated or compound text is unknown,
    # which never unblocks a source.
    census_path = ROOT / "census.json"
    census_path.write_text(json.dumps({
        "sources": [
            {"source_id": "Nope", "verdict": "full text not held"},
            {"source_id": "B", "verdict": "not full"},
            {"source_id": "C", "verdict": "missing (full copy unavailable)"},
            {"source_id": "D", "verdict": " Partial "},
            {"source_id": "E", "verdict": "partial/full"},
        ],
        "F": "full",
        "G": "fully held? no",
    }), encoding="utf-8", newline="\n")
    census = _load_census(census_path)
    assert census == {"D": "partial", "F": "full"}, census
    assert _is_source_blocked(gate_rows("UN"), units, empty, census)

    # Intake-key suppression of bib-key findings is exact.
    bib_items = [
        "bib-key: 'Smith2001a' not in bib/handbook.bib (parts/p01/x.tex:1 [cite])",
        "bib-key: 'Other' not in bib/handbook.bib (parts/p01/handbook-a.tex:2 [cite])",
        "bib-key: 'Smith2001' not in bib/handbook.bib (parts/p01/x.tex:3 [cite])",
        "dangling-ref: Smith2001 (parts/p01/x.tex:4)",
    ]
    assert _suppress_packet_bib_findings(bib_items, {"Smith2001", "a"}) == [bib_items[0], bib_items[1], bib_items[3]]

    # G6: locator forms, abbreviated ranges, and lookup through the packet's
    # presentations when the index has no bibkey for the cite key.
    kr_held = _held_index_from_data(
        {"entries": [{"path": "source/references/kr/kr-1995.pdf", "sha256": "x", "pdf_pages": 4}]}, "fixture"
    )
    kr_packet = {"units": [{"source_presentations": [kr_presentation]}]}
    for cite in ("\\cite[p.\\ 549]{KR1995}", "\\cite[549f.]{KR1995}", "\\cite[549ff]{KR1995}", "\\cite[{549}]{KR1995}", "\\cite[545--49]{KR1995}"):
        write(owned_rel, cite + "\n")
        assert len(_cite_page_findings([owned_rel], kr_held, kr_packet)) == 1, cite
    write(owned_rel, "\\cite[545--48]{KR1995} \\cite[pp.~546f.]{KR1995} \\cite[Thm.~549]{KR1995}\n")
    assert _cite_page_findings([owned_rel], kr_held, kr_packet) == []
    assert _locator_page_numbers("545--48") == [545, 548]

    # G13: prose inside \text in math is still compared.
    words = [f"word{i}" for i in range(1, 41)]
    write("source/references/kr/words.txt", " ".join(words) + "\n")
    write(owned_rel, "$\\text{" + " ".join(words[:38]) + "}$\n")
    words_packet = {"units": [{"held_paths": ["source/references/kr/words.txt"]}]}
    copy_hard, _copy_findings = _copy_runs(words_packet, [owned_rel])
    assert copy_hard
    # Prose carried by \intertext, \textsc, \parbox, \makebox or \fbox in
    # math counts; \\[2pt] and \\$ are a line break, not math; \$ is a dollar.
    copied = " ".join(words[:30])
    for text in (
        f"Intro line\\\\[2pt] {copied} end. Later \\[ x \\]",
        f"Intro line\\\\(2) {copied} end. Later \\( x \\)",
        f"Intro line\\\\$y$ {copied} and $x$",
        f"\\begin{{align}} a &= b \\intertext{{{copied}}} c &= d \\end{{align}}",
        f"\\begin{{align*}} a &= b \\shortintertext{{{copied}}} c \\end{{align*}}",
        f"$\\textsc{{{copied}}}$",
        f"$\\textmd{{{copied}}}$",
        f"\\[ \\parbox[t]{{5cm}}{{{copied}}} \\]",
        f"\\[ \\makebox[3cm][l]{{{copied}}} \\]",
        f"$\\fbox{{{copied}}}$",
        f"$\\text{{a \\textbf{{b}} {copied}}}$",
        f"Costs \\$5. {copied} and \\$6.",
        # Cite pre- and postnotes print; \mathrm and \operatorname carry
        # words; hyphens do not join copied words into one token.
        f"\\cite[{copied}]{{K}}",
        f"\\parencite[see][{copied}]{{K}}",
        f"$\\mathrm{{{copied}}}$",
        f"$\\operatorname*{{{copied}}}$",
        "-".join(words[:30]),
    ):
        write(owned_rel, text + "\n")
        copy_hard, _copy_findings = _copy_runs(words_packet, [owned_rel])
        assert copy_hard, text
    write(owned_rel, f"\\[ {copied} \\]\n")
    assert _copy_runs(words_packet, [owned_rel]) == ([], [])
    # Editable hosts: a different copied run of the same length is new.
    first_run, other_run = " ".join(words[:14]), " ".join(words[20:34])
    host_rel_name = "handbook/parts/p01/h.tex"
    assert _new_copy_runs(words_packet, host_rel_name, first_run, first_run) == ([], [])
    assert _new_copy_runs(words_packet, host_rel_name, other_run, first_run)[1]
    # Editable hosts: a new definition or a moved stub marker is new although
    # the counts are unchanged; the same text moved is not.
    baseline = "\\newcommand{\\a}{x}\nSome prose. TODO here.\n"
    changed = "Some prose.\n\\newcommand{\\evil}{y}\nTODO moved here.\n"
    assert {guard for guard, _item, _hard in _new_guard_items(host_rel_name, changed, baseline)} == {"G9", "G11"}
    moved = "\n\nSome prose. TODO here.\n\\newcommand{\\a}{x}\n"
    assert _new_guard_items(host_rel_name, moved, baseline) == []

    # Existing-treatment grep: whole labels only, generated/ excluded.
    write("handbook/parts/p01/a.tex", "\\label{annex:p15}\n\\ref{annex:p15-foo}\n")
    write("handbook/generated/x.tex", "\\label{annex:p15}\n")
    hits = [item for item in _grep_existing(["annex:p15"], []) if item["kind"] == "label-or-anchor"]
    assert [(item["path"], item["line"]) for item in hits] == [("handbook/parts/p01/a.tex", 1)], hits

    # verify: editable-host guards, G3/G4 attribution, snapshot protection.
    annex_rel = "handbook/annex/p01/new-wt-p01-001.tex"
    host_rel = "handbook/parts/p01/host.tex"
    host_text = "Existing prose with a review of \\cite{K}.\n\\begin{proof}x\\end{proof}\n"
    write(owned_rel, "\\chapter{New}\\label{sec:p01-w99-p01-001-intro}\n")
    write(annex_rel, "\\section{Annex}\n")
    write(host_rel, host_text)
    write(HELD_SOURCES.as_posix(), json.dumps({"entries": [{"path": "source/references/kr/kr-1995.pdf", "sha256": "x"}]}))
    packet = {
        "id": "wt-p01-001",
        "wave": "wt",
        "part": "P1",
        "label_tag": "p01-w99-p01-001",
        "owned_files": _owned_files("P1", "new-wt-p01-001"),
        "editable_hosts": [host_rel],
        "units": [],
    }
    write("work/waves/wt/packets/wt-p01-001.json", json.dumps(packet))
    packet_arg = str(ROOT / "work/waves/wt/packets/wt-p01-001.json")
    check_output: list[str] = []
    globals()["_run_check_findings"] = lambda: list(check_output)
    globals()["unit_compile_packet"] = lambda packet, run_build: {
        "ok": True, "errors": [], "undefined_citations": [], "undefined_refs_unknown": [], "overfull": 0
    }

    def take_snapshot(force: bool, path_arg: str | None = None) -> None:
        with contextlib.redirect_stdout(io.StringIO()):
            assert snapshot(argparse.Namespace(packet=path_arg or packet_arg, apply=True, dry_run=False, force=force)) == 0

    def run_verify(digest: str | None = None, path_arg: str | None = None) -> tuple[int, dict[str, Any]]:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            rc = verify(argparse.Namespace(packet=path_arg or packet_arg, snapshot_sha256=digest))
        return rc, json.loads(buffer.getvalue())

    def rebase() -> None:
        """A fresh snapshot, committed as the wave base."""
        take_snapshot(True)
        _fixture_commit_base("wt")

    outside_rel = "handbook/parts/p01/outside.tex"
    write(outside_rel, "outside\n")
    snap_args = argparse.Namespace(packet=packet_arg, apply=True, dry_run=False, force=False)
    snap_path = ROOT / "work/waves/wt/snapshots/wt-p01-001.json"
    args_path = ROOT / "work/waves/wt/args.json"
    take_snapshot(False)
    assert_refusal(lambda: snapshot(snap_args))
    # verify reads the snapshot only from the wave-base commit: without
    # base_sha it refuses (hard).
    rc, verdict = run_verify()
    assert rc == 1 and "base_sha missing" in verdict["hard"][0], verdict
    base_sha = _fixture_commit_base("wt")
    assert run_verify() == (0, {"hard": [], "findings": []})
    assert run_verify(_sha256_file(snap_path))[0] == 0
    assert run_verify("0" * 64)[0] == 1
    # A base_sha that is no commit, or a commit HEAD does not contain, is
    # refused.
    git = ["git", "-C", str(ROOT), "-c", "user.name=waves-selftest", "-c", "user.email=selftest@invalid"]
    dangling = subprocess.run(
        git + ["commit-tree", "HEAD^{tree}", "-m", "forged"], check=True, capture_output=True, text=True
    ).stdout.strip()
    for bad, reason in (("f" * 40, "not a commit"), (dangling, "not an ancestor"), (None, "base_sha missing")):
        _write_json_atomic(args_path, {} if bad is None else {"base_sha": bad})
        rc, verdict = run_verify()
        assert rc == 1 and reason in verdict["hard"][0], (bad, verdict)
    _write_json_atomic(args_path, {"base_sha": base_sha})
    # The working-tree snapshot and digests.json are never read: an author who
    # edits a non-owned file and rewrites both to match is still caught.
    write(outside_rel, "edited outside\n")
    forged = json.loads(snap_path.read_text(encoding="utf-8"))
    forged["tree"].update(_hash_state({outside_rel: _scan_tree_state()[outside_rel]}))
    snap_path.write_text(json.dumps(forged), encoding="utf-8", newline="\n")
    _record_snapshot_digest(snap_path)
    rc, verdict = run_verify()
    assert rc == 1 and f"G1 changed outside owned/editable set: {outside_rel}" in verdict["hard"], verdict
    write(outside_rel, "outside\n")
    # G2 compares frozen files with the wave-base commit.
    write("handbook/main.tex", "edited driver\n")
    rc, verdict = run_verify()
    assert rc == 1 and any(item.startswith("G2 ") and "handbook/main.tex" in item for item in verdict["hard"]), verdict
    (ROOT / "handbook/main.tex").unlink()
    rebase()
    assert run_verify()[0] == 0

    # G1 concurrency: another packet of the wave edits its own files and the
    # workflow writes the wave's assessments; this packet's verify reports
    # that (naming both packets) without failing. Another packet's read-only
    # host, or any other file, is still hard.
    other_rel = "work/waves/wt/packets/wt-p01-002.json"
    other = {
        **packet,
        "id": "wt-p01-002",
        "label_tag": "p01-w99-p01-002",
        "owned_files": _owned_files("P1", "new-wt-p01-002"),
        "editable_hosts": [],
        "readonly_hosts": [outside_rel],
    }
    write(other_rel, json.dumps(other))
    take_snapshot(True)
    take_snapshot(False, str(ROOT / other_rel))
    rc, verdict = run_verify(path_arg=str(ROOT / other_rel))
    assert rc == 1 and "is not in the wave-base commit" in verdict["hard"][0], verdict
    _fixture_commit_base("wt")
    write(other["owned_files"][0], "\\chapter{Other}\n")
    write("spec/coverage/edition-2026/assessments/wt/CA-wt-wt-p01-002-b1-1.1-first.json", "{}\n")
    rc, verdict = run_verify()
    assert rc == 0 and verdict["hard"] == [], verdict
    assert any("packet wt-p01-002, not of wt-p01-001" in item for item in verdict["findings"]), verdict
    assert run_verify(path_arg=str(ROOT / other_rel))[0] == 0
    write("spec/coverage/edition-2026/assessments/w77/CA-x.json", "{}\n")
    write(outside_rel, "edited outside\n")
    rc, verdict = run_verify()
    hard_g1 = {item for item in verdict["hard"] if item.startswith("G1 ")}
    assert rc == 1 and hard_g1 == {
        f"G1 changed outside owned/editable set: {outside_rel}",
        "G1 changed outside owned/editable set: spec/coverage/edition-2026/assessments/w77/CA-x.json",
    }, verdict
    write(outside_rel, "outside\n")
    for rel in (other_rel, other["owned_files"][0], "work/waves/wt/snapshots/wt-p01-002.json",
                "spec/coverage/edition-2026/assessments/w77/CA-x.json",
                "spec/coverage/edition-2026/assessments/wt/CA-wt-wt-p01-002-b1-1.1-first.json"):
        (ROOT / rel).unlink()
    rebase()
    assert run_verify()[0] == 0

    write(host_rel, host_text + "\\newcommand{\\foo}{bar} TODO this was reviewed in the wave ledger. \\begin{proof}\n")
    rc, verdict = run_verify()
    guards = {item.split(" ", 1)[0] for item in verdict["hard"]}
    assert rc == 1 and {"G9", "G11", "G12", "G14"} <= guards, verdict
    assert not any("review of" in item for item in verdict["hard"])
    write(host_rel, host_text)
    assert run_verify()[0] == 0

    write(owned_rel, "\\begin{hbtheorem}{thm:p01-w99-p01-001-new}{proved=annex:p01-x}{T}x\\end{hbtheorem}\n")
    check_output.append("annex-bidir: annex:p01-x targeted by 2 results: thm:old, thm:p01-w99-p01-001-new")
    rc, verdict = run_verify()
    assert rc == 1 and any(item.startswith("G3/G4 annex-bidir") for item in verdict["hard"]), verdict
    check_output[:] = ["dangling-ref: thm:zzz (parts/p03/other.tex:4)"]
    rc, verdict = run_verify()
    assert rc == 0 and any("not tied to this packet" in item for item in verdict["findings"]), verdict
    # Findings named only by a "rel:line" location in the owned file or an
    # editable host are this packet's.
    for item in (
        f"dangling-ref: sec:nowhere ({owned_rel.removeprefix('handbook/')}:1)",
        f"label-prefix: hbtheorem label 'bad' must be 'thm:<id>' ({owned_rel.removeprefix('handbook/')}:3)",
        f"dangling-ref: sec:nowhere ({host_rel.removeprefix('handbook/')}:2)",
        f"label-prefix: hbtheorem label 'bad' must be 'thm:<id>' ({host_rel.removeprefix('handbook/')}:7)",
    ):
        check_output[:] = [item]
        rc, verdict = run_verify()
        assert rc == 1 and verdict["hard"] == [f"G3/G4 {item}"], verdict
    check_output[:] = [f"dangling-ref: sec:nowhere ({host_rel.removeprefix('handbook/')}.bak:2)"]
    assert run_verify()[0] == 0
    write(owned_rel, "See \\cite{MissingKey}.\n")
    check_output[:] = ["bib-key: 'MissingKey' not in bib/handbook.bib (parts/p03/a.tex:1 [cite], +1 more)"]
    rc, verdict = run_verify()
    assert rc == 1 and any(item.startswith("G3/G4 bib-key") for item in verdict["hard"]), verdict
    write(owned_rel, "\\chapter{New}\\label{sec:p01-w99-p01-001-intro}\n")
    check_output.clear()

    # Held sources are pinned: a replaced or edited source is hard, and so is
    # one whose bytes differ from the held index.
    words_rel = "source/references/kr/words.txt"
    packet["units"] = [{"held_paths": [words_rel]}]
    write("work/waves/wt/packets/wt-p01-001.json", json.dumps(packet))
    rebase()
    assert run_verify()[0] == 0
    write(words_rel, "tampered\n")
    rc, verdict = run_verify()
    assert rc == 1 and any(item.startswith("G13") and "snapshot sha256" in item for item in verdict["hard"]), verdict
    write(words_rel, " ".join(words) + "\n")
    assert run_verify()[0] == 0
    write(HELD_SOURCES.as_posix(), json.dumps({"entries": [{"path": words_rel, "sha256": "0" * 64}]}))
    rc, verdict = run_verify()
    assert rc == 1 and any("held index sha256" in item for item in verdict["hard"]), verdict
    write(HELD_SOURCES.as_posix(), json.dumps({"entries": [{"path": "source/references/kr/kr-1995.pdf", "sha256": "x"}]}))
    packet["units"] = []
    write("work/waves/wt/packets/wt-p01-001.json", json.dumps(packet))
    rebase()
    assert run_verify()[0] == 0

    # Editable hosts must satisfy the ownership rules at snapshot and verify.
    restoration_rel = "handbook/restoration/r.tex"
    write(restoration_rel, "restored\n")
    for bad_host in (restoration_rel, "handbook/parts/p01.tex", "handbook/parts/p01/notes.md"):
        write("work/waves/wt/packets/wt-p01-001.json", json.dumps({**packet, "editable_hosts": [host_rel, bad_host]}))
        assert_refusal(lambda: snapshot(argparse.Namespace(packet=packet_arg, apply=True, dry_run=False, force=True)))
    write("work/waves/wt/packets/wt-p01-002.json", json.dumps({"id": "wt-p01-002", "readonly_hosts": [host_rel]}))
    write("work/waves/wt/packets/wt-p01-001.json", json.dumps(packet))
    assert_refusal(lambda: snapshot(argparse.Namespace(packet=packet_arg, apply=True, dry_run=False, force=True)))
    (ROOT / "work/waves/wt/packets/wt-p01-002.json").unlink()
    # A packet and snapshot rewritten together to widen the hosts, even when
    # that baseline is committed: verify repeats the ownership check.
    rebase()
    write("work/waves/wt/packets/wt-p01-001.json", json.dumps({**packet, "editable_hosts": [host_rel, restoration_rel]}))
    forged = json.loads(snap_path.read_text(encoding="utf-8"))
    forged["packet_sha256"] = _sha256_file(ROOT / "work/waves/wt/packets/wt-p01-001.json")
    forged["editable_hosts"][restoration_rel] = _sha256_file(ROOT / restoration_rel)
    forged["editable_host_text"][restoration_rel] = "restored\n"
    snap_path.write_text(json.dumps(forged), encoding="utf-8", newline="\n")
    _fixture_commit_base("wt")
    write(restoration_rel, "edited restoration\n")
    rc, verdict = run_verify()
    assert rc == 1 and any(item.startswith("G1 editable host") for item in verdict["hard"]), verdict
    write("work/waves/wt/packets/wt-p01-001.json", json.dumps(packet))
    rebase()
    assert run_verify()[0] == 0

    # Owned files are exactly the six files of one slug bound to the packet
    # id, none under restoration/ or generated/, a driver or frozen, and none
    # another packet's; the label tag is the packet's own.
    owned_files = packet["owned_files"]
    generated_rel = "handbook/generated/g.tex"
    write(generated_rel, "generated\n")
    packet_rel = "work/waves/wt/packets/wt-p01-001.json"
    force_args = argparse.Namespace(packet=packet_arg, apply=True, dry_run=False, force=True)
    for changes in (
        {"owned_files": owned_files + [restoration_rel]},
        {"owned_files": owned_files[:2] + [generated_rel] + owned_files[3:]},
        {"owned_files": owned_files[:-1]},
        {"owned_files": owned_files + [owned_files[0]]},
        {"owned_files": _owned_files("P1", "existing")},
        {"owned_files": ["handbook/parts/p01.tex"] + owned_files[1:]},
        {"owned_files": ["handbook/main.tex"] + owned_files[1:]},
        {"label_tag": "p02-w99-p01-001"},
        {"label_tag": None},
    ):
        write(packet_rel, json.dumps({**packet, **changes}))
        reason = assert_refusal(lambda: snapshot(force_args))
        assert ("owned" if "owned_files" in changes else "label_tag") in reason, (changes, reason)
    write(packet_rel, json.dumps(packet))
    for other_wave, other in (
        ("wt", {"id": "wt-p01-002", "editable_hosts": [owned_files[0]]}),
        ("wt", {"id": "wt-p01-002", "readonly_hosts": [owned_files[1]]}),
        ("w77", {"id": "w77-p01-001", "owned_files": [owned_files[2]]}),
        ("w77", {"id": "w77-p01-001", "label_tag": packet["label_tag"]}),
    ):
        other_rel = f"work/waves/{other_wave}/packets/{other['id']}.json"
        write(other_rel, json.dumps(other))
        reason = assert_refusal(lambda: snapshot(force_args))
        assert "another packet" in reason, (other, reason)
        (ROOT / other_rel).unlink()
    write("handbook/parts/p01/elsewhere.tex", "\\label{sec:p01-w99-p01-001-x}\n")
    assert "outside this packet" in assert_refusal(lambda: snapshot(force_args))
    (ROOT / "handbook/parts/p01/elsewhere.tex").unlink()
    # A packet and snapshot rewritten together to widen the owned files, even
    # when that baseline is committed: verify repeats the check.
    rebase()
    write(packet_rel, json.dumps({**packet, "owned_files": owned_files + [restoration_rel]}))
    forged = json.loads(snap_path.read_text(encoding="utf-8"))
    forged["packet_sha256"] = _sha256_file(ROOT / packet_rel)
    forged["owned_files"][restoration_rel] = _sha256_file(ROOT / restoration_rel)
    snap_path.write_text(json.dumps(forged), encoding="utf-8", newline="\n")
    _fixture_commit_base("wt")
    write(restoration_rel, "edited again\n")
    rc, verdict = run_verify()
    assert rc == 1 and any(item.startswith("G1 owned") for item in verdict["hard"]), verdict
    write(packet_rel, json.dumps(packet))
    rebase()
    assert run_verify()[0] == 0

    # Deleting the snapshot does not reopen the baseline either.
    snap_path.unlink()
    assert_refusal(lambda: snapshot(snap_args))

    # A unit_accounting packet owning no files still gets the full verdict: a
    # write outside its set is hard G1, and G10 is not applicable (no build).
    unit_rel = "work/waves/wu/packets/wu-p01-001.json"
    unit_packet = {
        "id": "wu-p01-001", "wave": "wu", "part": "P1", "mode": "unit_accounting", "label_tag": "p01-wu-p01-001",
        "sections": [], "units": [{"unit_id": "UL"}], "owned_files": [], "editable_hosts": [], "readonly_hosts": [],
    }
    write(unit_rel, json.dumps(unit_packet))

    def no_build(packet: dict[str, Any], run_build: bool) -> dict[str, Any]:
        raise AssertionError("unit compile must not run without owned body/annex files")

    globals()["unit_compile_packet"] = no_build
    take_snapshot(False, str(ROOT / unit_rel))
    _fixture_commit_base("wu")
    rogue_rel = "handbook/parts/p01/rogue.tex"
    write(rogue_rel, "rogue\n")
    rc, verdict = run_verify(path_arg=str(ROOT / unit_rel))
    assert rc == 1 and f"G1 changed outside owned/editable set: {rogue_rel}" in verdict["hard"], verdict
    assert any(item.startswith("G10 not applicable") for item in verdict["findings"]), verdict
    (ROOT / rogue_rel).unlink()
    # Owning proposed destinations an author has not written: still no build;
    # with only the body written, the template builds the body alone.
    unit_body, unit_annex = "handbook/parts/p01/ul.tex", "handbook/annex/p01/ul.tex"
    unit_owned = {**unit_packet, "owned_files": [unit_body, unit_annex],
                  "insertions": [{"units": ["UL"], "owned_files": [unit_body, unit_annex], "heading_level": "\\section"}]}
    assert _unit_compile_files(unit_owned) == ([], [])
    write(unit_body, "\\section{UL}\n")
    assert _unit_compile_files(unit_owned) == ([unit_body], [])
    template = _unit_template(unit_owned)
    assert "\\chapter{Scoped host}\n\\input{parts/p01/ul}\n" in template and "hbannexsetup" not in template, template
    (ROOT / unit_body).unlink()
    globals()["unit_compile_packet"] = lambda packet, run_build: {
        "ok": True, "errors": [], "undefined_citations": [], "undefined_refs_unknown": [], "overfull": 0
    }


def _selftest_packet_ids(base: Path) -> None:
    """Packet ids, owned files and label tags survive a ledger change; packets
    with a snapshot are never removed or renumbered without --force."""
    global ROOT
    ROOT = base
    _build_fixture(ROOT)
    globals()["_run_check_findings"] = lambda: []
    chapters = [("1", "Alpha Chapter", "1.1"), ("2", "Beta Chapter", "2.1"), ("3", "Gamma Chapter", "3.1")]
    toc = {
        "parts": [
            {
                "stable_part_id": "P1",
                "chapters": [
                    {"number": int(number), "title": title, "numbered_sections": [{"number": section, "title": title}]}
                    for number, title, section in chapters
                ],
            }
        ]
    }
    _fixture_write("spec/proposed-table-of-contents.json", json.dumps(toc))
    _fixture_write(
        "spec/coverage/edition-2026/completion-work-queue.jsonl",
        "".join(
            json.dumps(
                {
                    "unit_id": f"U{number}",
                    "required_components": [{"component_id": f"C{number}"}],
                    "source_presentations": [{"source_id": "S1"}],
                }
            )
            + "\n"
            for number, _title, _section in chapters
        ),
    )

    existing_sha = _sha256_file(ROOT / "handbook/parts/p01/existing.tex").upper()

    def write_rows(statuses: dict[str, str], note: str = "x") -> None:
        # An authored_unreviewed row here is fully accounted (live evidence
        # hash, components covering its unit, no parked scope): not selected.
        rows = [
            {
                "part": "P1",
                "chapter_id": number,
                "chapter_title": title,
                "section_id": section,
                "section_title": title,
                "status": statuses[section],
                "reader_evidence": (
                    [{"path": "handbook/parts/p01/existing.tex", "sha256": existing_sha, "components": [f"C{number}"]}]
                    if statuses[section] == AU
                    else [{"path": "handbook/parts/p01/existing.tex"}] if number == "1" else []
                ),
                "source_facets": [{"unit_id": f"U{number}"}],
                "missing_pieces": [] if statuses[section] == AU else [note],
                "unassessed_scope": [],
            }
            for number, title, section in chapters
            if section in statuses
        ]
        _fixture_write(
            "spec/coverage/edition-2026/current-fulfillment/p01-p03.jsonl",
            "".join(json.dumps(row) + "\n" for row in rows),
        )

    packet_dir = ROOT / "work/waves/w05/packets"

    def run(force: bool = False) -> int:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return packetize(argparse.Namespace(wave="w05", parts="P1", carry=None, census=None, apply=True, dry_run=False, force=force))

    def packets() -> dict[str, dict[str, Any]]:
        return {path.stem: json.loads(path.read_text(encoding="utf-8")) for path in sorted(packet_dir.glob("*.json"))}

    write_rows({"1.1": "partial", "2.1": "partial"})
    assert run() == 0
    first = packets()
    assert sorted(first) == ["w05-p01-001", "w05-p01-002"]
    beta = first["w05-p01-002"]
    assert [s["section_id"] for s in beta["sections"]] == ["2.1"]

    # No snapshots: Alpha's packet goes stale, Beta keeps its identity.
    write_rows({"1.1": AU, "2.1": "partial"})
    assert run() == 0
    second = packets()
    assert sorted(second) == ["w05-p01-002"]
    assert second["w05-p01-002"]["owned_files"] == beta["owned_files"]
    assert second["w05-p01-002"]["label_tag"] == beta["label_tag"]

    # New packets take fresh numbers.
    write_rows({"1.1": "partial", "2.1": "partial", "3.1": "partial"})
    assert run() == 0
    third = packets()
    assert sorted(third) == ["w05-p01-002", "w05-p01-003", "w05-p01-004"]
    assert [s["section_id"] for s in third["w05-p01-003"]["sections"]] == ["1.1"]
    assert third["w05-p01-002"]["owned_files"] == beta["owned_files"]

    # Packet JSONs lie outside the G1 scan: a rerun checks the owned files and
    # label tag it reuses.
    beta_path = packet_dir / "w05-p01-002.json"
    beta_text = beta_path.read_text(encoding="utf-8")
    _fixture_write("handbook/parts/p01/taken.tex", "\\label{sec:p01-taken-x}\n")
    for changes in (
        {"owned_files": beta["owned_files"] + ["handbook/restoration/r.tex"]},
        {"owned_files": ["handbook/generated/g.tex"] + beta["owned_files"][1:]},
        {"owned_files": third["w05-p01-003"]["owned_files"]},
        {"label_tag": third["w05-p01-003"]["label_tag"]},
        {"label_tag": "p01-taken"},
        {"label_tag": "../x"},
    ):
        beta_path.write_text(json.dumps({**json.loads(beta_text), **changes}), encoding="utf-8", newline="\n")
        assert run() == 1, changes
    beta_path.write_text(beta_text, encoding="utf-8", newline="\n")
    _fixture_write("work/waves/w06/packets/w06-p01-001.json", json.dumps({"id": "w06-p01-001", "owned_files": beta["owned_files"][:1]}))
    assert run() == 1
    (ROOT / "work/waves/w06/packets/w06-p01-001.json").unlink()
    (ROOT / "handbook/parts/p01/taken.tex").unlink()
    assert run() == 0 and packets() == third

    # Snapshotted packets stay exactly as written, and are never removed
    # without --force.
    for packet_id in ("w05-p01-002", "w05-p01-003"):
        with contextlib.redirect_stdout(io.StringIO()):
            assert snapshot(argparse.Namespace(packet=str(packet_dir / f"{packet_id}.json"), apply=True, dry_run=False, force=False)) == 0
    beta_bytes = (packet_dir / "w05-p01-002.json").read_bytes()
    write_rows({"1.1": "partial", "2.1": "partial", "3.1": "partial"}, note="changed note")
    assert run() == 0
    assert (packet_dir / "w05-p01-002.json").read_bytes() == beta_bytes
    write_rows({"1.1": AU, "2.1": "partial", "3.1": "partial"})
    assert_refusal(run)
    assert sorted(packets()) == ["w05-p01-002", "w05-p01-003", "w05-p01-004"]
    assert run(force=True) == 0
    final = packets()
    assert sorted(final) == ["w05-p01-002", "w05-p01-004"]
    assert final["w05-p01-002"]["owned_files"] == beta["owned_files"]

    # An unsplit run clears the halves of an earlier split.
    stale_half = ROOT / "work/waves/w05a"
    _fixture_write("work/waves/w05a/packets/w05a-p01-001.json", '{"id": "w05a-p01-001"}\n')
    _fixture_write("work/waves/w05a/args.json", "{}\n")
    assert run() == 0
    assert not (stale_half / "args.json").exists() and list((stale_half / "packets").glob("*.json")) == []


def _selftest_accounting(base: Path) -> None:
    """Section 10: authored_unreviewed rows with parked scope, a stale
    evidence hash or no component accounting become accounting packets (an
    accounted one is not selected; a mixed cluster is an author packet), and
    unlinked queue units of the part become unit_accounting packets."""
    global ROOT
    ROOT = base
    _build_fixture(ROOT)
    globals()["_run_check_findings"] = lambda: []
    sha = _sha256_file(ROOT / "handbook/parts/p01/existing.tex").upper()
    chapters = ["1", "2", "3", "4", "5"]
    toc = {
        "parts": [
            {
                "stable_part_id": "P1",
                "chapters": [
                    {
                        "number": int(number),
                        "title": f"Chapter {number}",
                        "numbered_sections": [
                            {"number": f"{number}.1", "title": "A"},
                            {"number": f"{number}.2", "title": "B"},
                        ],
                    }
                    for number in chapters
                ],
            }
        ]
    }
    _fixture_write("spec/proposed-table-of-contents.json", json.dumps(toc))

    def evidence(sha256: str, components: list[str]) -> list[dict[str, Any]]:
        return [{"path": "handbook/parts/p01/existing.tex", "anchor": "sec:existing", "sha256": sha256, "components": components}]

    def row(section: str, status: str, unit: str, ev: list[dict[str, Any]], **extra: Any) -> dict[str, Any]:
        return {
            "part": "P1",
            "chapter_id": section.split(".")[0],
            "chapter_title": f"Chapter {section.split('.')[0]}",
            "section_id": section,
            "section_title": section,
            "status": status,
            "reader_evidence": ev,
            "source_facets": [{"unit_id": unit}],
            "missing_pieces": extra.get("missing_pieces", []),
            "unassessed_scope": extra.get("unassessed_scope", []),
        }

    rows = [
        row("1.1", AU, "U1", evidence(sha, ["C1"]), unassessed_scope=["parked duty"]),
        row("2.1", AU, "U2", evidence("00" * 32, ["C2"])),
        row("3.1", AU, "U3", evidence(sha, ["C9"])),
        row("4.1", AU, "U4", evidence(sha, ["C4"])),
        row("5.1", "partial", "U5", [], missing_pieces=["x"]),
        row("5.2", AU, "U5", evidence(sha, [])),
    ]
    _fixture_write(
        "spec/coverage/edition-2026/current-fulfillment/p01-p03.jsonl",
        "".join(json.dumps(item) + "\n" for item in rows),
    )
    linked = [
        {"unit_id": f"U{n}", "required_components": [{"component_id": f"C{n}"}],
         "source_presentations": [{"source_id": "SMISSING" if n == 3 else "S1"}]}
        for n in range(1, 6)
    ]
    unlinked = [
        {"unit_id": "UL", "required_components": [{"component_id": "CL1"}, {"component_id": "CL2"}],
         "source_presentations": [{"source_id": "S1"}],
         "destination": {"body": [{"path": "handbook/parts/p01/existing.tex", "line": 1},
                                  {"proposed_path": "handbook/parts/p01/ul.tex"}],
                         "annex": {"proposed_path": "handbook/annex/p01/ul.tex"}}},
        {"unit_id": "UL2", "required_components": [{"component_id": "CM"}],
         "source_presentations": [{"source_id": "S1"}],
         "destination": {"body": [{"path": "handbook/parts/p01/existing.tex", "line": 2}], "annex": []}},
        {"unit_id": "UX", "required_components": [{"component_id": "CX"}],
         "destination": {"body": {"proposed_path": "handbook/parts/p02/ux.tex"}, "annex": None}},
        {"unit_id": "UZ", "required_components": [{"component_id": "CZ"}],
         "destination": {"body": [{"path": "handbook/handbook.sty"}], "annex": []}},
    ]
    _fixture_write(
        "spec/coverage/edition-2026/completion-work-queue.jsonl",
        "".join(json.dumps(item) + "\n" for item in linked + unlinked),
    )
    assert _au_accounting_reasons(rows[0], {"U1": linked[0]}) == ["parked_scope"]
    assert _au_accounting_reasons(rows[1], {"U2": linked[1]}) == ["stale_evidence"]
    # A later entry for the same file supersedes a stale one; a stale latest entry still counts.
    superseded = dict(rows[1], reader_evidence=evidence("00" * 32, ["C2"]) + evidence(sha, ["C2"]))
    assert _au_accounting_reasons(superseded, {"U2": linked[1]}) == []
    regressed = dict(rows[1], reader_evidence=evidence(sha, ["C2"]) + evidence("00" * 32, ["C2"]))
    assert _au_accounting_reasons(regressed, {"U2": linked[1]}) == ["stale_evidence"]
    assert _au_accounting_reasons(rows[2], {"U3": linked[2]}) == ["no_component_accounting"]
    assert _au_accounting_reasons(rows[3], {"U4": linked[3]}) == []
    # A non-dict evidence entry carries no sha256: stale (fail closed).
    assert _evidence_stale({**rows[3], "reader_evidence": evidence(sha, ["C4"]) + ["handbook/parts/p01/existing.tex"]})
    # Evidence split over two entries is not accounting (read per entry), and
    # a facet unit absent from the queue cannot be covered.
    split = {**rows[3], "reader_evidence": evidence(sha, ["C4"]) + evidence(sha, ["C5"])}
    assert not _lacks_component_accounting(split, {"U4": linked[3]})
    two = {"unit_id": "U4", "required_components": [{"component_id": "C4"}, {"component_id": "C5"}]}
    assert _lacks_component_accounting(split, {"U4": two})
    assert _lacks_component_accounting(rows[3], {})
    parents, _route = _build_input_edges()
    assert _unit_part(unlinked[0], parents) == "P1" and _unit_part(unlinked[2], parents) == "P2"
    assert _unit_part(unlinked[3], parents) is None
    assert _unit_part({"prerequisite_allocation_prefix": "ED26-REQ-D-P12-015-01/PRE-"}, parents) == "P12"

    # An open blocker naming an authored_unreviewed section holds back
    # authoring only: the row still goes to accounting, sources_held false.
    _fixture_write(
        "spec/coverage/edition-2026/blockers.jsonl",
        json.dumps({"id": "ACQ-X-1", "status": "open", "sections": ["2.1"]}) + "\n",
    )
    packet_dir = ROOT / "work/waves/w07/packets"

    def run() -> str:
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            ns = argparse.Namespace(wave="w07", parts="P1", carry=None, census=None, apply=True, dry_run=False, force=False)
            assert packetize(ns) == 0
        return out.getvalue()

    summary = run()
    packets = {path.stem: json.loads(path.read_text(encoding="utf-8")) for path in sorted(packet_dir.glob("*.json"))}
    by_sections = {tuple(s["section_id"] for s in p["sections"]): p for p in packets.values()}
    assert {key: p["mode"] for key, p in by_sections.items()} == {
        ("1.1",): "accounting",
        ("2.1",): "accounting",
        ("3.1",): "accounting",
        ("5.1", "5.2"): "author",
        (): "unit_accounting",
    }, {key: p["mode"] for key, p in by_sections.items()}
    assert by_sections[("1.1",)]["accounting_reasons"] == {"1.1": ["parked_scope"]}
    assert by_sections[("2.1",)]["accounting_reasons"] == {"2.1": ["stale_evidence"]}
    assert by_sections[("2.1",)]["sources_held"] is False
    assert by_sections[("2.1",)]["open_blockers"] == {"2.1": "ACQ-X-1"}
    assert by_sections[("1.1",)]["open_blockers"] == {}
    assert "skipped sections with open blockers" not in summary, summary
    assert "open blockers sent to accounting (sources_held false): 2.1" in summary, summary
    # Reasons are counted for packetized rows only (1.1, 2.1, 3.1, 5.2).
    assert (
        f"{AU} sections selected for accounting: 4 "
        "(parked scope 1, stale evidence 1, no component accounting 2)"
    ) in summary, summary
    assert by_sections[("1.1",)]["component_ids"] == ["C1"]
    assert [c["id"] for c in by_sections[("1.1",)]["units"][0]["required_components"]] == ["C1"]
    # Sources absent: an accounting packet is not held back by the gate.
    assert by_sections[("3.1",)]["sources_held"] is False
    assert by_sections[("5.1", "5.2")]["component_ids"] == ["C5"]
    # Every component id carries its record and conditions; `open` marks the
    # open subset (none named open here; all of an unlinked unit's).
    assert [
        (c["id"], c["open"], "success_condition" in c)
        for c in by_sections[("5.1", "5.2")]["units"][0]["required_components"]
    ] == [("C5", False, True)]
    assert all(
        c["open"] for u in by_sections[()]["units"] for c in u["required_components"]
    ), by_sections[()]["units"]
    unit_packet = by_sections[()]
    assert [u["unit_id"] for u in unit_packet["units"]] == ["UL", "UL2"]
    assert unit_packet["component_ids"] == ["CL1", "CL2", "CM"]
    assert unit_packet["owned_files"] == ["handbook/parts/p01/ul.tex", "handbook/annex/p01/ul.tex"]
    assert "handbook/parts/p01/existing.tex" in unit_packet["readonly_hosts"]
    assert unit_packet["insertion"]["body"]["after_input"] == "parts/p01/existing"
    assert unit_packet["toc_tag"] is None and unit_packet["chapter"] is None
    assert not any(u["unit_id"] in {"UX", "UZ"} for p in packets.values() for u in p["units"])
    assert "no derivable part (not packetized in any wave): 1" in summary, summary
    author = by_sections[("5.1", "5.2")]
    expected = 3 * 2 + 2 + 2 * author["max_blocks"] + 2
    assert f"worst-case agents: {expected} " in summary, summary
    assert "  accounting packets: 3 (worst-case agents 6)" in summary, summary
    args_data = _load_json(ROOT / "work/waves/w07/args.json", {})
    modes = sorted(p["mode"] for lane in args_data["lanes"] for p in lane["packets"])
    assert modes == ["accounting", "accounting", "accounting", "author", "unit_accounting"], modes
    # Lane entries of unit-only packets name their units.
    lane_units = {p["id"]: p.get("units") for lane in args_data["lanes"] for p in lane["packets"]}
    assert lane_units[unit_packet["id"]] == ["UL", "UL2"], lane_units
    assert all(units is None for pid, units in lane_units.items() if pid != unit_packet["id"]), lane_units
    # A rerun keeps every id (the unit packet matches by its units), and the
    # unit packet's ownership passes the snapshot rules.
    run()
    assert {path.stem for path in packet_dir.glob("*.json")} == set(packets)
    unit_path = packet_dir / f"{unit_packet['id']}.json"
    assert _ownership_problems(unit_path, unit_packet, check_labels=True) == []
    assert _owned_form_problems("P1", unit_packet["id"], "w07", ["handbook/restoration/r.tex"], "unit_accounting")
    assert _ownership_problems(unit_path, {**unit_packet, "sections": [{"section_id": "1.1"}]}, check_labels=False)
    unplaced = _load_json(ROOT / "work/waves/w07/unplaced-units.json", {})
    assert [u["unit_id"] for u in unplaced["units"]] == ["UZ"], unplaced
    assert unplaced["units"][0]["component_ids"] == ["CZ"]

    # A lookup-only unit takes its part from destination.lookup and lists the
    # lookup path read-only (lookup proposals are not owned). A unit whose
    # primary_part disagrees with its proposed path's part owns nothing outside
    # its part. Seven units sharing one new file split into two packets: the
    # second lists the file read-only and runs in the owner's lane.
    extra = [
        {"unit_id": "ULOOK", "required_components": [{"component_id": "CK"}],
         "destination": {"body": None, "annex": None,
                         "lookup": {"proposed_path": "handbook/parts/p01/sources/look-guide.tex"}}},
        {"unit_id": "UPRIM", "required_components": [{"component_id": "CP"}],
         "destination": {"primary_part": "P1", "body": {"proposed_path": "handbook/parts/p02/prim.tex"}, "annex": []}},
    ] + [
        {"unit_id": f"US{n}", "required_components": [{"component_id": f"CS{n}"}],
         "destination": {"body": {"proposed_path": "handbook/parts/p01/shared-new.tex"}, "annex": []}}
        for n in range(1, 8)
    ] + [
        # The completion dict form names the unit's body and annex proposals.
        {"unit_id": "UL4", "required_components": [{"component_id": "C4L"}],
         "destination": {"body": [], "annex": [],
                         "completion": {"body": "handbook/parts/p01/ul4-completion.tex",
                                        "annex": "handbook/annex/p01/ul4-completion.tex"}}},
        # A fused-space part directory: the part is evident, never derived.
        {"unit_id": "UFUSED", "required_components": [{"component_id": "CF"}],
         "destination": {"body": {"proposed_path": "handbook/parts/p 01/sources/fused.tex"}, "annex": []}},
    ]
    ul4_files = ["handbook/parts/p01/ul4-completion.tex", "handbook/annex/p01/ul4-completion.tex"]
    assert _unit_destinations(extra[-2]) == (ul4_files, []), _unit_destinations(extra[-2])
    assert _unit_part(extra[-2], parents) == "P1"
    assert _unit_part(extra[-1], parents) is None
    assert _unplaced_reason(extra[-1]) == (UNPLACED_MALFORMED, ["P1"])
    assert _unplaced_reason({"destination": {"body": [{"path": "handbook/parts/p8/x.tex"}]}}) == (
        UNPLACED_MALFORMED,
        ["P8"],
    )
    assert _unplaced_reason(unlinked[3]) == (UNPLACED_NO_PART, [])
    assert _unit_part(extra[0], parents) == "P1" and _unit_part(extra[1], parents) == "P1"
    assert _unit_lookup_paths(extra[0]) == ["handbook/parts/p01/sources/look-guide.tex"]
    _fixture_write(
        "spec/coverage/edition-2026/completion-work-queue.jsonl",
        "".join(json.dumps(item) + "\n" for item in linked + unlinked + extra),
    )
    out = io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
        ns = argparse.Namespace(wave="w09", parts="P1", carry=None, census=None, apply=True, dry_run=False, force=False)
        assert packetize(ns) == 0
    w09_dir = ROOT / "work/waves/w09/packets"
    w09 = [json.loads(path.read_text(encoding="utf-8")) for path in sorted(w09_dir.glob("*.json"))]
    unit_of = {u["unit_id"]: p for p in w09 for u in p["units"]}
    look = unit_of["ULOOK"]
    assert look["mode"] == "unit_accounting" and "CK" in look["component_ids"]
    assert "handbook/parts/p01/sources/look-guide.tex" in look["readonly_hosts"]
    assert "handbook/parts/p01/sources/look-guide.tex" not in look["owned_files"] + look["editable_hosts"]
    prim = unit_of["UPRIM"]
    assert prim["part"] == "P1" and "handbook/parts/p02/prim.tex" not in prim["owned_files"]
    assert "handbook/parts/p02/prim.tex" in prim["readonly_hosts"]
    assert _owned_form_problems("P1", prim["id"], "w09", ["handbook/parts/p02/prim.tex"], "unit_accounting")
    shared = "handbook/parts/p01/shared-new.tex"
    first_us, last_us = unit_of["US1"], unit_of["US7"]
    assert first_us["id"] != last_us["id"]
    assert shared in first_us["owned_files"] and shared not in last_us["owned_files"]
    assert shared in last_us["readonly_hosts"] and first_us["lane"] == last_us["lane"]
    for packet in w09:
        assert _ownership_problems(w09_dir / f"{packet['id']}.json", packet, check_labels=False) == [], packet["id"]
    # Absent completion-form proposals are owned, with their own insertion.
    ul4 = unit_of["UL4"]
    assert all(rel in ul4["owned_files"] for rel in ul4_files), ul4["owned_files"]
    ul4_insertion = next(item for item in ul4["insertions"] if "UL4" in item["units"])
    assert ul4_insertion["owned_files"] == ul4_files, ul4_insertion
    assert ul4_insertion["insertion"]["body"] is not None and ul4_insertion["heading_level"]
    # Unplaced units are classified by reason; an evident part of this wave is named.
    w09_summary = out.getvalue()
    # Lead ruling: a fused/unpadded part path is read with its evident part, so UFUSED is placed.
    assert "UFUSED" in unit_of, unit_of
    assert f"  {UNPLACED_MALFORMED}: 0" in w09_summary and f"  {UNPLACED_NO_PART}: 1" in w09_summary, w09_summary
    unplaced_w09 = {u["unit_id"]: u for u in _load_json(ROOT / "work/waves/w09/unplaced-units.json", {})["units"]}
    assert "UFUSED" not in unplaced_w09
    assert (unplaced_w09["UZ"]["reason"], unplaced_w09["UZ"]["evident_parts"]) == (UNPLACED_NO_PART, [])
    assert _normalize_unit_paths({"destination": {"body": "handbook/parts/p 8/x.tex", "annex": "handbook/annex/p9/y.tex"}})["destination"] == {
        "body": "handbook/parts/p08/x.tex", "annex": "handbook/annex/p09/y.tex"}
    # In another lane, the read-only listing of an owned file is a conflict.
    owner_path = w09_dir / f"{first_us['id']}.json"
    _write_json_atomic(w09_dir / f"{last_us['id']}.json", {**last_us, "lane": 999})
    assert _ownership_problems(owner_path, first_us, check_labels=False)

    # A reused packet's owned new file stays claimed: six units sharing a new
    # file make one packet that owns it; a seventh proposer added on a rerun
    # lists it read-only in the owner's lane (no ownership refusal).
    reuse = [
        {"unit_id": f"UR{n}", "required_components": [{"component_id": f"CR{n}"}],
         "destination": {"body": {"proposed_path": "handbook/parts/p01/reuse-shared.tex"}, "annex": []}}
        for n in range(1, 8)
    ]
    w10_dir = ROOT / "work/waves/w10/packets"
    reuse_shared = "handbook/parts/p01/reuse-shared.tex"
    for count in (6, 7):
        _fixture_write(
            "spec/coverage/edition-2026/completion-work-queue.jsonl",
            "".join(json.dumps(item) + "\n" for item in linked + unlinked + reuse[:count]),
        )
        err = io.StringIO()
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
            ns = argparse.Namespace(wave="w10", parts="P1", carry=None, census=None, apply=True, dry_run=False, force=False)
            assert packetize(ns) == 0, err.getvalue()
        w10 = [json.loads(path.read_text(encoding="utf-8")) for path in sorted(w10_dir.glob("*.json"))]
        unit_of = {u["unit_id"]: p for p in w10 for u in p["units"]}
        if count == 6:
            owner_id = unit_of["UR1"]["id"]
            assert reuse_shared in unit_of["UR1"]["owned_files"]
    assert unit_of["UR1"]["id"] == owner_id and reuse_shared in unit_of["UR1"]["owned_files"]
    assert unit_of["UR7"]["id"] != owner_id and reuse_shared not in unit_of["UR7"]["owned_files"]
    assert reuse_shared in unit_of["UR7"]["readonly_hosts"] and unit_of["UR7"]["lane"] == unit_of["UR1"]["lane"]


def _selftest_unit_insertions(base: Path) -> None:
    """A proposal-only unit co-packed with a unit that has an existing host
    is anchored at the end of the part driver, not beside that host; each
    set of proposing units gets its own insertion and heading level. A
    section packet's evidence path that is not on disk is read-only."""
    global ROOT
    ROOT = base
    _build_fixture(ROOT)
    globals()["_run_check_findings"] = lambda: []
    _fixture_write(
        "handbook/parts/p01.tex",
        "\\hbpartidentity{p01}\n\\part{P1}\n\\input{parts/p01/existing}\n\\input{parts/p01/tail}\n",
    )
    _fixture_write("handbook/parts/p01/tail.tex", "\\chapter{Tail}\n")
    ledger = ROOT / "spec/coverage/edition-2026/current-fulfillment/p01-p03.jsonl"
    rows = [json.loads(line) for line in ledger.read_text(encoding="utf-8").splitlines() if line.strip()]
    rows[0]["reader_evidence"].append({"path": "handbook/parts/p01/gone.tex"})
    _fixture_write(ledger.relative_to(ROOT).as_posix(), "".join(json.dumps(row) + "\n" for row in rows))
    queue = ROOT / "spec/coverage/edition-2026/completion-work-queue.jsonl"
    units = [
        {"unit_id": "UL5", "required_components": [{"component_id": "C5"}],
         "destination": {"body": [{"path": "handbook/parts/p01/existing.tex"},
                                  {"proposed_path": "handbook/parts/p01/ul5.tex"}],
                         "annex": {"proposed_path": "handbook/annex/p01/ul5.tex"}}},
        {"unit_id": "UL7", "required_components": [{"component_id": "C7"}],
         "destination": {"body": {"proposed_path": "handbook/parts/p01/presentations/far.tex"}, "annex": []}},
    ]
    _fixture_write(
        queue.relative_to(ROOT).as_posix(),
        queue.read_text(encoding="utf-8") + "".join(json.dumps(item) + "\n" for item in units),
    )
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        ns = argparse.Namespace(wave="w03", parts="P1", carry=None, census=None, apply=True, dry_run=False, force=False)
        assert packetize(ns) == 0
    packets = [json.loads(p.read_text(encoding="utf-8")) for p in sorted((ROOT / "work/waves/w03/packets").glob("*.json"))]
    unit_packet = next(p for p in packets if p["mode"] == "unit_accounting")
    assert [u["unit_id"] for u in unit_packet["units"]] == ["UL5", "UL7"], unit_packet["units"]
    by_units = {tuple(item["units"]): item for item in unit_packet["insertions"]}
    assert sorted(by_units) == [("UL5",), ("UL7",)], by_units
    assert by_units[("UL5",)]["owned_files"] == ["handbook/parts/p01/ul5.tex", "handbook/annex/p01/ul5.tex"]
    assert by_units[("UL5",)]["insertion"]["body"]["after_input"] == "parts/p01/existing"
    far = by_units[("UL7",)]
    assert far["owned_files"] == ["handbook/parts/p01/presentations/far.tex"]
    assert far["insertion"]["body"]["host"] == "handbook/parts/p01.tex", far
    assert far["insertion"]["body"]["after_input"] == "parts/p01/tail", far
    assert far["heading_level"] == "\\chapter"
    assert unit_packet["insertion"] == by_units[("UL5",)]["insertion"]
    section_packet = next(p for p in packets if p["mode"] == "author")
    assert "handbook/parts/p01/gone.tex" in section_packet["readonly_hosts"]
    assert "handbook/parts/p01/gone.tex" not in section_packet["editable_hosts"]
    assert section_packet["insertions"] is None


def _selftest_anchors(base: Path) -> None:
    """Hook brackets through xparse macros, nested macros and input files;
    annex anchors that follow body order."""
    global ROOT
    ROOT = base
    write = _fixture_write
    _HOOK_MACRO_CACHE.clear()
    write("handbook/parts/p07/anchors.tex",
          "\\NewDocumentCommand{\\hbOn}{}{\\AddToHook{env/theorem/begin}[k]{\\x}}\n"
          "\\NewDocumentCommand\\hbOff{}{\\RemoveFromHook{env/theorem/begin}[k]}\n"
          "\\newcommand{\\inner}{\\AddToHook{env/lemma/begin}[n]{y}}\n"
          "\\newcommand{\\outer}{\\inner}\n"
          "\\newcommand{\\close}{\\RemoveFromHook{env/lemma/begin}[n]}\n")
    write("handbook/parts/p07.tex", "\\hbOn\n\\input{restoration/a}\n\\hbOff\n\\input{parts/p07/x}\n")
    write("handbook/parts/p08.tex", "\\outer\n\\input{restoration/b}\n\\close\n\\input{parts/p08/y}\n")
    write("handbook/parts/p09.tex", "\\input{parts/p09/on}\n\\input{restoration/c}\n\\input{parts/p09/off}\n\\input{parts/p09/z}\n")
    write("handbook/parts/p09/on.tex", "\\AddToHook{env/example/begin}[i]{z}\n")
    write("handbook/parts/p09/off.tex", "\\RemoveFromHook{env/example/begin}[i]\n")
    write("handbook/parts/p10.tex", "\\input{parts/p10/both}\n\\input{parts/p10/w}\n")
    write("handbook/parts/p10/both.tex", "\\AddToHook{env/example/begin}[j]{z}\n\\RemoveFromHook{env/example/begin}[j]\n")
    for host, after in (("handbook/parts/p07.tex", "parts/p07/x"), ("handbook/parts/p08.tex", "parts/p08/y")):
        assert _line_inside_ranges(host, 2) and not _line_inside_ranges(host, 4), host
        assert _anchor_after(host, 2)["after_input"] == after, host
    assert _line_inside_ranges("handbook/parts/p09.tex", 2)
    assert _anchor_after("handbook/parts/p09.tex", 2)["after_line"] == 3
    assert not _line_inside_ranges("handbook/parts/p10.tex", 1)
    write("handbook/parts/p11.tex",
          "\\input{parts/p11/a}\n\\AddToHookNext{env/definition/end}{\\label{x}}\n"
          "\\input{restoration/q}\n\\input{parts/p11/b}\n")
    write("handbook/parts/p12.tex",
          "\\let\\hbadd\\AddToHook\n\\let\\hbrem=\\RemoveFromHook\n\\hbadd{env/x/begin}[k]{y}\n"
          "\\input{restoration/a}\n\\hbrem{env/x/begin}[k]\n\\input{parts/p12/z}\n")
    write("handbook/parts/p13.tex",
          "\\newcommand{\\on}{\\AddToHook{env/y/begin}[k]{y}}\n\\newcommand{\\off}{\\RemoveFromHook{env/y/begin}[k]}\n"
          "\\let\\On\\on\n\\On\n\\input{restoration/a}\n\\off\n\\input{parts/p13/z}\n")
    write("handbook/parts/p14.tex",
          "\\hook_gput_code:nnn {env/z/begin} {k} {y}\n\\input{restoration/a}\n"
          "\\hook_gremove_code:nn {env/z/begin} {k}\n\\input{parts/p14/z}\n")
    write("handbook/parts/p15.tex", "{\n\\input{restoration/a}\n}\n\\input{parts/p15/z}\n")
    write("handbook/parts/p16.tex", "\\input{parts/p16/pending}\n\\input{parts/p16/z}\n\\input{parts/p16/w}\n")
    write("handbook/parts/p16/pending.tex", "\\AddToHookNext{env/definition/end}{\\label{y}}\n")
    _HOOK_MACRO_CACHE.clear()
    assert [_line_inside_ranges("handbook/parts/p11.tex", line) for line in (1, 2, 3, 4)] == [False, True, True, False]
    assert _anchor_after("handbook/parts/p11.tex", 2)["after_line"] == 4
    for host, inside, outside in (
        ("handbook/parts/p12.tex", 4, 6),
        ("handbook/parts/p13.tex", 5, 7),
        ("handbook/parts/p14.tex", 2, 4),
        ("handbook/parts/p15.tex", 2, 4),
    ):
        assert _line_inside_ranges(host, inside) and not _line_inside_ranges(host, outside), host
    # Pending code left at the end of an input file reaches the next input.
    assert [_line_inside_ranges("handbook/parts/p16.tex", line) for line in (1, 2, 3)] == [True, True, False]
    # Hook macros defined with \csdef or expl3 \cs_new:Npn; parameterised
    # hook macros close only the hook their arguments name.
    write("handbook/parts/p17.tex",
          "\\csdef{csOn}{\\AddToHook{env/theorem/begin}[k]{x}}\n\\csdef{csOff}{\\RemoveFromHook{env/theorem/begin}[k]}\n"
          "\\csOn\n\\input{parts/p17/a}\n\\csOff\n\\input{parts/p17/b}\n")
    write("handbook/parts/p18.tex",
          "\\cs_new:Npn \\hb_x_on: {\\AddToHook{env/theorem/begin}[k]{x}}\n"
          "\\cs_new_protected:Npn \\hb_x_off: {\\RemoveFromHook{env/theorem/begin}[k]}\n"
          "\\hb_x_on:\n\\input{parts/p18/a}\n\\hb_x_off:\n\\input{parts/p18/b}\n")
    write("handbook/parts/p19.tex",
          "\\newcommand{\\pOn}[1]{\\AddToHook{env/#1/begin}[k]{x}}\n\\newcommand{\\pOff}[1]{\\RemoveFromHook{env/#1/begin}[k]}\n"
          "\\pOn{theorem}\n\\input{parts/p19/a}\n\\pOff{lemma}\n\\input{parts/p19/b}\n")
    write("handbook/parts/p03.tex",
          "\\pOn{theorem}\n\\input{parts/p03/a}\n\\pOff{theorem}\n\\input{parts/p03/b}\n\\pOn\n\\input{parts/p03/c}\n")
    _HOOK_MACRO_CACHE.clear()
    for host in ("handbook/parts/p17.tex", "handbook/parts/p18.tex"):
        assert _line_inside_ranges(host, 4) and not _line_inside_ranges(host, 6), host
        assert _anchor_after(host, 4)["after_line"] == 6, host
    assert _line_inside_ranges("handbook/parts/p19.tex", 4) and _line_inside_ranges("handbook/parts/p19.tex", 6)
    assert_refusal(lambda: _anchor_after("handbook/parts/p19.tex", 4))
    # \pOn without its argument opens a bracket nothing closes (fail closed).
    assert [_line_inside_ranges("handbook/parts/p03.tex", line) for line in (2, 4, 6)] == [True, False, True]
    _HOOK_MACRO_CACHE.clear()

    # Annex order follows body order: with no annex evidence for the chapter,
    # the annex anchor follows the last annex file whose body counterpart is
    # routed before the body anchor.
    write("handbook/main.tex", "\\input{parts/p02}\n\\input{annex/p02}\n")
    write("handbook/parts/p02.tex", "\\input{parts/p02/a}\n\\input{parts/p02/b}\n\\input{parts/p02/c}\n")
    write("handbook/annex/p02.tex", "\\input{annex/p02/a}\n\\input{annex/p02/c}\n")
    for name in ("a", "b", "c"):
        write(f"handbook/parts/p02/{name}.tex", f"\\chapter{{{name}}}\n")
    for name in ("a", "c"):
        write(f"handbook/annex/p02/{name}.tex", f"\\section{{{name}}}\n")
    parents, route = _build_input_edges()
    rows = [{"part": "P2", "chapter_id": "14", "section_id": "14.7", "reader_evidence": [{"path": "handbook/parts/p02/b.tex"}]}]
    body = _insertion_for_rows(rows, "P2", rows, {}, parents, route, annex=False)
    assert body["after_input"] == "parts/p02/b"
    annex = _insertion_for_rows(rows, "P2", rows, {}, parents, route, annex=True, body_anchor=body)
    assert annex == {"host": "handbook/annex/p02.tex", "after_line": 1, "after_input": "annex/p02/a"}, annex
    # Chapter evidence whose body follows the body anchor does not pull the
    # annex later; with no annex file before the body anchor, the annex goes
    # before the first annex file.
    write("handbook/annex/p02.tex", "\\chapter{Annex}\n\\input{annex/p02/c}\n")
    parents, route = _build_input_edges()
    rows = [{"part": "P2", "chapter_id": "14", "section_id": "14.1", "reader_evidence": [
        {"path": "handbook/parts/p02/a.tex"}, {"path": "handbook/annex/p02/c.tex"}]}]
    body = _insertion_for_rows(rows, "P2", rows, {}, parents, route, annex=False)
    assert body["after_input"] == "parts/p02/a"
    annex = _insertion_for_rows(rows, "P2", rows, {}, parents, route, annex=True, body_anchor=body)
    assert annex == {"host": "handbook/annex/p02.tex", "after_line": 1, "after_input": None, "before_input": "annex/p02/c"}, annex


def _selftest() -> None:
    global ROOT
    old_root = ROOT
    old_unit_compile = unit_compile_packet
    old_run_check = _run_check_findings
    old_texlive_command = _texlive_command
    try:
        scratch_root = ROOT / "tmp/tooling-scratch/waves"
        scratch_root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=scratch_root) as td:
            ROOT = Path(td)
            _build_fixture(ROOT)
            assert _slugify("Alpha, Beta & Gamma!") == "alpha-beta-and-gamma"
            assert _printed_ordinal("P15") == 11
            assert _printed_ordinal("P11") == 16
            assert _input_target("parts/p01") == "parts/p01.tex"
            parents, route = _build_input_edges()
            assert "handbook/parts/p01/existing.tex" in parents
            assert "handbook/main.tex" in route

            p04_hook = ROOT / "handbook/parts/p04.tex"
            p04_hook.parent.mkdir(parents=True, exist_ok=True)
            p04_hook.write_text(
                "\\AddToHook{env/lemma/begin}[a]{x}\n"
                "\\AddToHook{env/theorem/begin}[b]{x}\n"
                "\\input{restoration/a}\n"
                "\\RemoveFromHook{env/lemma/begin}[a]\n"
                "\\RemoveFromHook{env/theorem/begin}[b]\n",
                encoding="utf-8",
                newline="\n",
            )
            assert _line_inside_ranges("handbook/parts/p04.tex", 3)
            assert_refusal(lambda: _anchor_after("handbook/parts/p04.tex", 3))
            p06_hook = ROOT / "handbook/parts/p06.tex"
            p06_hook.write_text(
                "\\AddToHookNext{env/x/begin}{ignored}\n"
                "\\AddToHook{env/definition/begin}[hb-p6-source-unit]{x}\n"
                "\\AddToHook{env/convention/begin}[hb-p6-source-unit]{x}\n"
                "\\AddToHook{env/example/begin}[hb-p6-source-unit]{x}\n"
                "\\input{restoration/a}\n"
                "\\input{restoration/b}\n"
                "\\RemoveFromHook{env/definition/begin}[hb-p6-source-unit]\n"
                "\\RemoveFromHook{env/convention/begin}[hb-p6-source-unit]\n"
                "\\RemoveFromHook{env/example/begin}[hb-p6-source-unit]\n"
                "\\input{restoration/c}\n",
                encoding="utf-8",
                newline="\n",
            )
            assert _line_inside_ranges("handbook/parts/p06.tex", 6)
            # Pending AddToHookNext code protects up to the input that may
            # consume it, and opens no bracket.
            assert _line_inside_ranges("handbook/parts/p06.tex", 1)
            assert not _line_inside_ranges("handbook/parts/p06.tex", 10)
            assert _anchor_after("handbook/parts/p06.tex", 6) == {
                "host": "handbook/parts/p06.tex",
                "after_line": 10,
                "after_input": "restoration/c",
            }
            p06_hook.write_text(
                "\\AddToHook{env/example/begin}[open]{x}\n\\input{x}\n",
                encoding="utf-8",
                newline="\n",
            )
            assert _line_inside_ranges("handbook/parts/p06.tex", 2)
            assert_refusal(lambda: _anchor_after("handbook/parts/p06.tex", 2))
            # Hook brackets switched by macros, defined in another file (as in
            # parts/p08/source-anchors.tex and parts/p07.tex); the definitions
            # themselves are not brackets.
            (ROOT / "handbook/parts/p07").mkdir(parents=True, exist_ok=True)
            (ROOT / "handbook/parts/p07/anchors.tex").write_text(
                "\\newcommand{\\hbHooksOn}{%\n"
                "  \\AddToHook{env/theorem/begin}[k]{\\x}%\n"
                "  \\AddToHook{env/lemma/begin}[k]{\\x}}\n"
                "\\newcommand{\\hbHooksOff}{%\n"
                "  \\RemoveFromHook{env/theorem/begin}[k]%\n"
                "  \\RemoveFromHook{env/lemma/begin}[k]}\n",
                encoding="utf-8",
                newline="\n",
            )
            (ROOT / "handbook/parts/p07.tex").write_text(
                "\\hbHooksOn\n\\input{restoration/a}\n\\hbHooksOff\n\\input{parts/p07/x}\n"
                "\\hbHooksOn\n\\input{restoration/b}\n",
                encoding="utf-8",
                newline="\n",
            )
            _HOOK_MACRO_CACHE.clear()
            assert _line_inside_ranges("handbook/parts/p07.tex", 2)
            assert not _line_inside_ranges("handbook/parts/p07.tex", 4)
            assert _line_inside_ranges("handbook/parts/p07.tex", 6)
            assert _hook_ranges("handbook/parts/p07/anchors.tex") == []
            # Inside a multi-line definition body is inside a brace group.
            assert _line_inside_ranges("handbook/parts/p07/anchors.tex", 2)
            assert _anchor_after("handbook/parts/p07.tex", 2)["after_input"] == "parts/p07/x"
            assert_refusal(lambda: _anchor_after("handbook/parts/p07.tex", 6))
            (ROOT / "handbook/parts/p07.tex").write_text(
                "\\input{parts/p07/x}\n\\input{parts/p07/x}\n", encoding="utf-8", newline="\n"
            )
            assert_refusal(lambda: _anchor_after("handbook/parts/p07.tex", 1))
            (ROOT / "handbook/parts/p07.tex").unlink()
            (ROOT / "handbook/parts/p07/anchors.tex").unlink()
            _HOOK_MACRO_CACHE.clear()

            # With-arguments hook forms count; a hook key the parser cannot
            # read opens a bracket nothing closes (fail closed).
            for opener, closer, closed in (
                ("\\AddToHookWithArguments{env/x/begin}[k]{\\x}", "\\RemoveFromHook{env/x/begin}[k]", True),
                ("\\hook_gput_code_with_args:nnn {env/x/begin}{k}{\\x}", "\\hook_gremove_code:nn {env/x/begin}{k}", True),
                ("\\AddToHookNextWithArguments{env/x/begin}{\\x}", "", True),
                ("\\AddToHook{env/{theorem}/begin}[k]{\\x}", "\\RemoveFromHook{env/{theorem}/begin}[k]", False),
            ):
                p06_hook.write_text(
                    f"\\input{{a}}\n{opener}\n\\input{{b}}\n{closer}\n\\input{{c}}\n", encoding="utf-8", newline="\n"
                )
                _HOOK_MACRO_CACHE.clear()
                assert _line_inside_ranges("handbook/parts/p06.tex", 3), opener
                assert _line_inside_ranges("handbook/parts/p06.tex", 5) != closed, opener
            # Hook macros with delimited parameters resolve; a definition the
            # parser cannot read, followed by a hook command, makes its calls
            # open a bracket nothing closes.
            anchors = ROOT / "handbook/parts/p07/anchors.tex"
            p07_driver = ROOT / "handbook/parts/p07.tex"
            for definitions, closed in (
                ("\\def\\hbOn#1.{\\AddToHook{env/theorem/begin}[k]{#1}}\n"
                 "\\def\\hbOff{\\RemoveFromHook{env/theorem/begin}[k]}\n", True),
                ("\\newcommand{\\hbOn}{\\AddToHook{env/theorem/begin}[k]{x}\n"
                 "\\def\\hbOff{\\RemoveFromHook{env/theorem/begin}[k]}\n", False),
            ):
                anchors.write_text(definitions, encoding="utf-8", newline="\n")
                p07_driver.write_text(
                    "\\hbOn x.\n\\input{restoration/a}\n\\hbOff\n\\input{parts/p07/x}\n", encoding="utf-8", newline="\n"
                )
                _HOOK_MACRO_CACHE.clear()
                assert _line_inside_ranges("handbook/parts/p07.tex", 2), definitions
                assert _line_inside_ranges("handbook/parts/p07.tex", 4) != closed, definitions
            # Every edge up to main.tex counts: a bracket in a host outside the
            # part around the part's driver refuses the anchor; the document
            # environment is no bracket.
            p07_driver.write_text("\\input{parts/p07/x}\n", encoding="utf-8", newline="\n")
            (ROOT / "handbook/parts/p09.tex").write_text(
                "\\begin{document}\n\\input{parts/p07}\n\\end{document}\n", encoding="utf-8", newline="\n"
            )
            (ROOT / "handbook/parts/p08.tex").write_text(
                "\\AddToHook{env/x/begin}[k]{y}\n\\input{parts/p07}\n\\RemoveFromHook{env/x/begin}[k]\n",
                encoding="utf-8",
                newline="\n",
            )
            _HOOK_MACRO_CACHE.clear()
            lower = InputEdge("handbook/parts/p07.tex", "handbook/parts/p07/x.tex", 1, "parts/p07/x")
            assert _anchor_from_chain(
                [lower, InputEdge("handbook/parts/p09.tex", "handbook/parts/p07.tex", 2, "parts/p07")], "P7", annex=False
            ) == {"host": "handbook/parts/p07.tex", "after_line": 1, "after_input": "parts/p07/x"}
            assert_refusal(lambda: _anchor_from_chain(
                [lower, InputEdge("handbook/parts/p08.tex", "handbook/parts/p07.tex", 2, "parts/p07")], "P7", annex=False
            ))
            for path in (p07_driver, anchors, ROOT / "handbook/parts/p08.tex", ROOT / "handbook/parts/p09.tex"):
                path.unlink()
            p06_hook.write_text("\\AddToHook{env/example/begin}[open]{x}\n\\input{x}\n", encoding="utf-8", newline="\n")
            _HOOK_MACRO_CACHE.clear()

            rows_for_insert = [
                {
                    "part": "P1",
                    "chapter_id": "1",
                    "section_id": "1.1",
                    "status": AU,
                    "reader_evidence": [{"path": "handbook/parts/p01/existing.tex"}],
                },
                {
                    "part": "P1",
                    "chapter_id": "1",
                    "section_id": "1.2",
                    "status": "missing",
                    "reader_evidence": [],
                },
            ]
            toc_order = _load_toc_order()
            insertion = _insertion_for_rows(
                [rows_for_insert[1]],
                "P1",
                rows_for_insert,
                toc_order,
                parents,
                route,
                annex=False,
            )
            assert insertion["after_input"] == "parts/p01/existing"

            (ROOT / "handbook/restoration").mkdir(parents=True, exist_ok=True)
            with (ROOT / "handbook/main.tex").open("a", encoding="utf-8", newline="\n") as handle:
                handle.write("\\input{parts/p02}\n\\input{parts/p06}\n\\input{parts/p15}\n\\input{parts/p16}\n")
            (ROOT / "handbook/parts/p02.tex").write_text(
                "\\input{restoration/scope-SRC-02665-02809}\n",
                encoding="utf-8",
                newline="\n",
            )
            (ROOT / "handbook/restoration/scope-SRC-02665-02809.tex").write_text(
                "\\begin{inheritedrestorationscope}{SRC-02665-02809}\n"
                "\\input{restoration/inherited-02665-02809}\n"
                "\\end{inheritedrestorationscope}\n",
                encoding="utf-8",
                newline="\n",
            )
            (ROOT / "handbook/restoration/inherited-02665-02809.tex").write_text(
                "\\section{Inherited}\\label{sec:inherited}\n",
                encoding="utf-8",
                newline="\n",
            )
            parents, route = _build_input_edges()
            restoration_rows = [
                {
                    "part": "P2",
                    "chapter_id": "13",
                    "section_id": "13.6",
                    "reader_evidence": [
                        {"path": "handbook/restoration/inherited-02665-02809.tex"}
                    ],
                }
            ]
            restoration_insert = _insertion_for_rows(
                restoration_rows,
                "P2",
                restoration_rows,
                toc_order,
                parents,
                route,
                annex=False,
            )
            assert restoration_insert["host"] == "handbook/parts/p02.tex"
            assert restoration_insert["after_input"] == "restoration/scope-SRC-02665-02809"
            assert _heading_level("P2", {"body": restoration_insert}) == "\\section"

            (ROOT / "handbook/parts/p06").mkdir(parents=True, exist_ok=True)
            (ROOT / "handbook/parts/p06.tex").write_text(
                "\\AddToHook{env/example/begin}[wrap]{x}\n"
                "\\input{parts/p06/host}\n"
                "\\RemoveFromHook{env/example/begin}[wrap]\n"
                "\\input{parts/p06/after}\n",
                encoding="utf-8",
                newline="\n",
            )
            (ROOT / "handbook/parts/p06/after.tex").write_text("\\section{After}\n", encoding="utf-8", newline="\n")
            (ROOT / "handbook/parts/p06/host.tex").write_text(
                "\\section{Host}\n\\input{parts/p06/ev}\n",
                encoding="utf-8",
                newline="\n",
            )
            (ROOT / "handbook/parts/p06/ev.tex").write_text("\\section{Evidence}\n", encoding="utf-8", newline="\n")
            _HOOK_MACRO_CACHE.clear()
            parents, route = _build_input_edges()
            hook_rows = [
                {
                    "part": "P6",
                    "chapter_id": "1",
                    "section_id": "1.1",
                    "reader_evidence": [{"path": "handbook/parts/p06/ev.tex"}],
                }
            ]
            hook_insert = _insertion_for_rows(hook_rows, "P6", hook_rows, toc_order, parents, route, annex=False)
            # ev.tex sits in host.tex, whose own input in p06.tex is inside a
            # hook bracket: the anchor moves up to p06.tex and out of the bracket.
            assert hook_insert["host"] == "handbook/parts/p06.tex"
            assert hook_insert["after_line"] == 4
            assert hook_insert["after_input"] == "parts/p06/after"
            assert _heading_level("P6", {"body": hook_insert}) == "\\section"

            (ROOT / "handbook/parts/p15").mkdir(parents=True, exist_ok=True)
            (ROOT / "handbook/parts/p16").mkdir(parents=True, exist_ok=True)
            (ROOT / "handbook/parts/p15.tex").write_text(
                "\\input{parts/p15/hume-and-the-problem-of-induction}\n",
                encoding="utf-8",
                newline="\n",
            )
            (ROOT / "handbook/parts/p15/hume-and-the-problem-of-induction.tex").write_text(
                "\\chapter{Hume}\n",
                encoding="utf-8",
                newline="\n",
            )
            (ROOT / "handbook/parts/p16.tex").write_text(
                "\\chapter{P16}\n"
                "\\begingroup\n"
                "\\input{parts/p16/finite-abduction}\n"
                "\\endgroup\n",
                encoding="utf-8",
                newline="\n",
            )
            (ROOT / "handbook/parts/p16/finite-abduction.tex").write_text(
                "\\chapter{Finite Abduction}\n",
                encoding="utf-8",
                newline="\n",
            )
            parents, route = _build_input_edges()
            cross_rows = [
                {
                    "part": "P15",
                    "chapter_id": "164",
                    "section_id": "164.1",
                    "reader_evidence": [
                        {"path": "handbook/parts/p15/hume-and-the-problem-of-induction.tex"},
                        {"path": "handbook/parts/p16/finite-abduction.tex"},
                    ],
                }
            ]
            cross_insert = _insertion_for_rows(cross_rows, "P15", cross_rows, toc_order, parents, route, annex=False)
            assert cross_insert["host"] == "handbook/parts/p15.tex"
            assert cross_insert["after_input"] == "parts/p15/hume-and-the-problem-of-induction"

            # Annex order follows body order through annex counterparts.
            (ROOT / "handbook/annex/p15").mkdir(parents=True, exist_ok=True)
            with (ROOT / "handbook/main.tex").open("a", encoding="utf-8", newline="\n") as handle:
                handle.write("\\input{annex/p15}\n")
            (ROOT / "handbook/annex/p15.tex").write_text(
                "\\input{annex/p15/fisher}\n\\input{annex/p15/huber}\n\\input{annex/p15/later}\n",
                encoding="utf-8",
                newline="\n",
            )
            for name in ("fisher", "huber", "later"):
                (ROOT / f"handbook/annex/p15/{name}.tex").write_text("x\n", encoding="utf-8", newline="\n")
            (ROOT / "handbook/parts/p15/huber.tex").write_text("\\chapter{Huber}\n", encoding="utf-8", newline="\n")
            parents, route = _build_input_edges()
            annex_rows = [
                {
                    "part": "P15",
                    "chapter_id": "169",
                    "section_id": "169.1",
                    "reader_evidence": [
                        {"path": "handbook/parts/p15/huber.tex"},
                        {"path": "handbook/annex/p15/fisher.tex"},
                    ],
                }
            ]
            annex_insert = _insertion_for_rows(annex_rows, "P15", annex_rows, toc_order, parents, route, annex=True)
            assert annex_insert == {"host": "handbook/annex/p15.tex", "after_line": 2, "after_input": "annex/p15/huber"}

            ns = argparse.Namespace(wave="w02", parts="P1", carry=None, census=None, apply=False, dry_run=True)
            rc = packetize(ns)
            assert rc == 0
            held_path = ROOT / HELD_SOURCES
            held_text = held_path.read_text(encoding="utf-8")
            held_path.unlink()
            assert_refusal(lambda: packetize(ns))
            ns.apply = True
            ns.dry_run = False
            assert_refusal(lambda: packetize(ns))
            assert not (ROOT / "work/waves/w02").exists()
            held_path.write_text(held_text, encoding="utf-8", newline="\n")

            rc = packetize(ns)
            assert rc == 0
            packet_files = sorted((ROOT / "work/waves/w02/packets").glob("*.json"))
            assert len(packet_files) == 1
            packet = json.loads(packet_files[0].read_text(encoding="utf-8"))
            # A rerun of the same wave keeps ids, slugs and label tags, even
            # after the packet's author has created its files and labels.
            first_run = packet_files[0].read_text(encoding="utf-8")
            (ROOT / packet["owned_files"][0]).write_text(
                f"\\chapter{{New}}\\label{{sec:{packet['label_tag']}-intro}}\n", encoding="utf-8", newline="\n"
            )
            assert packetize(ns) == 0
            assert packet_files[0].read_text(encoding="utf-8") == first_run
            (ROOT / packet["owned_files"][0]).unlink()
            assert packet["insertion"]["annex"]["host"] == "handbook/annex/p01-route.tex"
            assert packet["insertion"]["annex"]["after_input"] == "annex/p01/kept"
            assert packet["sections"][0]["section_id"] == "1.1"
            assert packet["max_blocks"] == 2
            assert packet["heading_level"] == "\\chapter"
            snap_args = argparse.Namespace(packet=str(packet_files[0]), apply=True, dry_run=False)
            assert snapshot(snap_args) == 0
            snap = ROOT / "work/waves/w02/snapshots" / f"{packet['id']}.json"
            assert snap.is_file()
            body = ROOT / packet["owned_files"][0]
            body.parent.mkdir(parents=True, exist_ok=True)
            body.write_text("\\chapter{New}\\label{sec:new}\n", encoding="utf-8", newline="\n")
            assert _env_balance(packet["owned_files"][0]) == []
            assert _encoding_guard(packet["owned_files"][0]) == []

            cluster_rows = [
                {"section_id": f"1.{idx}", "source_facets": [{"unit_id": "UBIG"}]}
                for idx in range(1, 8)
            ]
            big_packets = _bin_pack_chapter(
                [cluster_rows],
                {"UBIG": {"required_components": [{"component_id": "C1"}]}},
                {f"1.{idx}": {"order": idx} for idx in range(1, 8)},
            )
            assert [len(item) for item in big_packets] == [4, 3]
            partial_row = {
                "section_id": "1.9",
                "status": "partial",
                "source_facets": [
                    {"unit_id": "UA", "baseline_content_state": "authored"},
                    {"unit_id": "UB", "baseline_content_state": "authored"},
                ],
                "missing_pieces": ["The label def:open-piece remains unsupplied."],
            }
            partial_units = {
                "UA": {
                    "required_components": [
                        {"component_id": "A1", "body_label": "def:open-piece"},
                        {"component_id": "A2", "body_label": "def:closed-piece"},
                    ]
                },
                "UB": {"required_components": [{"component_id": "B1"}]},
            }
            assert _cluster_component_count([partial_row], partial_units) == 1

            collision_slug = "alpha-chapter-w02-p01-001"
            (ROOT / f"handbook/bib/intake-p01-{collision_slug}.bib").write_text(
                "", encoding="utf-8", newline="\n"
            )
            existing_files = {
                path.relative_to(ROOT).as_posix()
                for path in ROOT.rglob("*")
                if path.is_file()
            }
            slug = _make_unique_slug("P1", "Alpha Chapter", "w02-p01-001", existing_files, set(), set())
            assert slug == "alpha-chapter-w02-p01-001-2"
            label = _make_label_tag(
                "P1",
                "w02-p01-001",
                {"sec:p01-w02-p01-001", "thm:p01-w02-p01-001-main"},
                set(),
            )
            assert label == "p01-w02-p01-001-2"
            packet_record_path = ROOT / "work/waves/w01/packets/x.json"
            packet_record_path.parent.mkdir(parents=True, exist_ok=True)
            packet_record_path.write_text(
                json.dumps(
                    {
                        "owned_files": _owned_files("P1", "beta-w02-p01-002"),
                        "label_tag": "p01-w02-p01-002",
                    }
                ),
                encoding="utf-8",
                newline="\n",
            )
            owned_taken, tags_taken = _packet_owned_files_and_tags()
            assert "handbook/parts/p01/beta-w02-p01-002.tex" in owned_taken
            assert "p01-w02-p01-002" in tags_taken

            assert _try_normalize_repo_path("handbook/parts/../restoration/r.tex") == "handbook/restoration/r.tex"
            assert _try_normalize_repo_path("../outside.tex") is None
            assert not _is_editable_host(
                "handbook/parts/../restoration/r.tex",
                Counter(),
                set(),
                set(),
            )
            assert not _is_editable_host(
                "handbook/Restoration/r.tex",
                Counter(),
                set(),
                set(),
            )

            verify_root = ROOT / "verify"
            verify_root.mkdir()
            ROOT = verify_root
            (ROOT / "handbook/parts/p01").mkdir(parents=True)
            (ROOT / "handbook/annex/p01").mkdir(parents=True)
            (ROOT / "handbook/bib").mkdir(parents=True)
            (ROOT / "handbook/registry").mkdir(parents=True)
            (ROOT / "work/waves/wt/packets").mkdir(parents=True)
            (ROOT / "work/waves/wt/snapshots").mkdir(parents=True)
            (ROOT / "spec/coverage/edition-2026").mkdir(parents=True)
            (ROOT / "source").mkdir()
            good_body = ROOT / "handbook/parts/p01/owned-wt-p01-001.tex"
            good_body.write_text("\\chapter{Owned}\\label{sec:owned}\n", encoding="utf-8", newline="\n")
            good_annex = ROOT / "handbook/annex/p01/owned-wt-p01-001.tex"
            good_annex.write_text("\\chapter{Annex}\\label{annex:owned}\n", encoding="utf-8", newline="\n")
            packet_path = ROOT / "work/waves/wt/packets/wt-p01-001.json"
            guard_packet = {
                "id": "wt-p01-001",
                "wave": "wt",
                "part": "P1",
                "label_tag": "p01-wt-p01-001",
                "owned_files": _owned_files("P1", "owned-wt-p01-001"),
                "editable_hosts": [],
                "units": [],
            }
            packet_path.write_text(json.dumps(guard_packet), encoding="utf-8", newline="\n")
            snapshot_path = ROOT / "work/waves/wt/snapshots/wt-p01-001.json"

            def write_guard_snapshot(frozen_files: dict[str, str | None] | None = None) -> None:
                current_packet = json.loads(packet_path.read_text(encoding="utf-8"))
                owned_map = {
                    rel: (_sha256_file(_root(rel)) if _root(rel).is_file() else None)
                    for rel in current_packet["owned_files"]
                }
                hosts = current_packet.get("editable_hosts") or []
                snapshot_path.write_text(
                    json.dumps(
                        {
                            "tree": _hash_state(_scan_tree_state()),
                            "packet_sha256": _sha256_file(packet_path),
                            "owned_files": owned_map,
                            "editable_hosts": {rel: _sha256_file(_root(rel)) for rel in hosts},
                            "editable_host_text": {rel: _decoded_text(rel) for rel in hosts},
                            "frozen_files": frozen_files or {},
                            "check_findings": [],
                        }
                    ),
                    encoding="utf-8",
                    newline="\n",
                )
                _fixture_commit_base("wt")

            write_guard_snapshot()
            globals()["unit_compile_packet"] = lambda packet, run_build: {
                "ok": True,
                "errors": [],
                "undefined_citations": [],
                "undefined_refs_unknown": [],
                "overfull": 0,
            }
            globals()["_run_check_findings"] = lambda: []
            held_path = ROOT / HELD_SOURCES
            held_path.write_text(
                json.dumps({"entries": [{"path": "source/s.txt", "source_ids": ["S"], "bibkeys": [], "sha256": "s"}]}),
                encoding="utf-8",
                newline="\n",
            )
            write_guard_snapshot()
            assert verify(argparse.Namespace(packet=str(packet_path))) == 0
            outside = ROOT / "handbook/parts/p01/outside.tex"
            outside.write_text("old\n", encoding="utf-8", newline="\n")
            write_guard_snapshot()
            outside.write_text("new\n", encoding="utf-8", newline="\n")
            assert verify(argparse.Namespace(packet=str(packet_path))) == 1
            widened_packet = dict(guard_packet)
            widened_packet["editable_hosts"] = ["handbook/parts/p01/outside.tex"]
            packet_path.write_text(json.dumps(widened_packet), encoding="utf-8", newline="\n")
            assert verify(argparse.Namespace(packet=str(packet_path))) == 1
            outside.unlink()
            packet_path.write_text(json.dumps(guard_packet), encoding="utf-8", newline="\n")
            write_guard_snapshot()
            assert verify(argparse.Namespace(packet=str(packet_path))) == 0
            packet_path.write_text(json.dumps({**guard_packet, "units": [{"held_paths": []}]}), encoding="utf-8", newline="\n")
            assert verify(argparse.Namespace(packet=str(packet_path))) == 1
            packet_path.write_text(json.dumps(guard_packet), encoding="utf-8", newline="\n")
            frozen = ROOT / "handbook/main.tex"
            frozen.write_text("old\n", encoding="utf-8", newline="\n")
            write_guard_snapshot({"handbook/main.tex": _sha256_file(frozen)})
            frozen.write_text("new\n", encoding="utf-8", newline="\n")
            assert verify(argparse.Namespace(packet=str(packet_path))) == 1
            frozen.unlink()
            write_guard_snapshot()
            globals()["unit_compile_packet"] = lambda packet, run_build: {
                "ok": False,
                "errors": ["stubbed compile failure"],
                "undefined_citations": [],
                "undefined_refs_unknown": [],
                "overfull": 0,
            }
            assert verify(argparse.Namespace(packet=str(packet_path))) == 1
            globals()["unit_compile_packet"] = old_unit_compile
            globals()["_run_check_findings"] = old_run_check

            class FakeProc:
                def __init__(self, stdout: str, returncode: int = 0) -> None:
                    self.stdout = stdout
                    self.returncode = returncode

            old_subprocess_run = subprocess.run
            try:
                subprocess.run = lambda *a, **k: FakeProc(
                    "[check] all hard checks passed\n"
                    "  - duplicate-label: bad (parts/p01/owned-wt-p01-001.tex:1)\n"
                )  # type: ignore[assignment]
                assert _run_check_findings() == ["duplicate-label: bad (parts/p01/owned-wt-p01-001.tex:1)"]
                subprocess.run = lambda *a, **k: FakeProc("traceback\n", 2)  # type: ignore[assignment]
                assert _run_check_findings()[0].startswith("__check_error__:")
            finally:
                subprocess.run = old_subprocess_run  # type: ignore[assignment]

            bib = ROOT / "handbook/bib/intake-p01-owned-wt-p01-001.bib"
            bib.write_text("@book{K,\n title={T}\n}\n", encoding="utf-8", newline="\n")
            assert _parse_intake_bib(bib) == ["K"]
            bib.write_text("@book{K,\n title={T}\n", encoding="utf-8", newline="\n")
            try:
                _parse_intake_bib(bib)
                raise AssertionError("bad bib should fail")
            except UsageError:
                pass
            csv_path = ROOT / "handbook/registry/symbols-intake-p01-owned-wt-p01-001.csv"
            csv_path.write_text(",".join(SYMBOL_HEADER) + "\n", encoding="utf-8", newline="\n")
            assert _read_csv_header(csv_path) == SYMBOL_HEADER
            csv_path.write_text("glyph,macro\nP1.2,x\n", encoding="utf-8", newline="\n")
            assert _read_csv_header(csv_path) != SYMBOL_HEADER

            held = HeldIndex(
                entries=[
                    {
                        "path": "source/s.txt",
                        "source_ids": ["S"],
                        "bibkeys": ["K"],
                        "pdf_pages": 4,
                        "page_offset": 544,
                    }
                ],
                bibkey_to_entries={
                    "K": [{"bibkeys": ["K"], "pdf_pages": 4, "page_offset": 544}],
                    "U": [{"bibkeys": ["U"], "pdf_pages": 4}],
                },
                available=True,
            )
            gate_held = _held_index_from_data(
                {
                    "entries": [
                        {
                            "path": "source/s.txt",
                            "source_ids": ["S"],
                            "bibkeys": ["K"],
                            "titles": ["Benchmark Chapter"],
                            "sha256": "abc123",
                        }
                    ],
                    "source_index": {"S": ["source/s.txt"]},
                },
                "fixture-held",
            )
            citation_unit = {"unit_id": "UC", "source_presentations": [{"citation_key": "K"}]}
            benchmark_unit = {
                "unit_id": "UBM",
                "source_presentations": [{"benchmark_id": "B1", "title": "Benchmark Chapter"}],
            }
            missing_unit = {"unit_id": "UM", "source_presentations": [{"title": "Missing Chapter"}]}
            GATE_DUTY = {"kind": "blocked_source", "duty": "d"}
            # Absent sources block only rows whose every duty is blocked_source and that have no
            # unassessed scope: a writable duty, an untyped duty or an unassessed row is not blocked.
            for row in ({"status": "partial", "missing_pieces": [GATE_DUTY, {"kind": "writable", "duty": "w"}]},
                        {"status": "partial", "missing_pieces": ["legacy untyped duty"]},
                        {"status": "partial", "missing_pieces": []},
                        {"status": "unassessed", "missing_pieces": [GATE_DUTY]},
                        {"status": "partial", "missing_pieces": [GATE_DUTY], "unassessed_scope": ["u"]}):
                assert not _is_source_blocked([{**row, "section_id": "1.8", "source_facets": [{"unit_id": "UM"}]}],
                                              {"UM": missing_unit}, gate_held, {}), row
            gate_row = {"section_id": "1.8", "status": "partial", "missing_pieces": [GATE_DUTY], "source_facets": [{"unit_id": "UC"}]}
            assert not _is_source_blocked([gate_row], {"UC": citation_unit}, gate_held, {})
            assert _packet_units([gate_row], {"UC": citation_unit}, gate_held)[0]["held_paths"] == ["source/s.txt"]
            gate_row = {"section_id": "1.8", "status": "partial", "missing_pieces": [GATE_DUTY], "source_facets": [{"unit_id": "UBM"}]}
            assert not _is_source_blocked([gate_row], {"UBM": benchmark_unit}, gate_held, {})
            gate_row = {"section_id": "1.8", "status": "partial", "missing_pieces": [GATE_DUTY], "source_facets": [{"unit_id": "UM"}]}
            assert _is_source_blocked([gate_row], {"UM": missing_unit}, gate_held, {})
            assert not _is_source_blocked([gate_row], {"UM": missing_unit}, gate_held, {"UM": "partial"})
            # A presentation recorded as missing stays absent although its
            # shared source id is held; a census verdict still unblocks it.
            recorded_missing = {
                "unit_id": "URM",
                "source_presentations": [{"source_id": "S", "body_state": "identified_missing"}],
            }
            gate_row = {"section_id": "1.8", "status": "partial", "missing_pieces": [GATE_DUTY], "source_facets": [{"unit_id": "URM"}]}
            assert _is_source_blocked([gate_row], {"URM": recorded_missing}, gate_held, {})
            assert not _is_source_blocked([gate_row], {"URM": recorded_missing}, gate_held, {"S": "full"})
            # A facet unit absent from the queue is unknown, hence absent.
            gate_row = {"section_id": "1.8", "status": "partial", "missing_pieces": [GATE_DUTY], "source_facets": [{"unit_id": "UNOTQUEUED"}]}
            assert _is_source_blocked([gate_row], {}, gate_held, {})
            # Unresolvable identities fail closed; an artifact hash or a
            # bibliographic-record key resolves.
            unresolvable = {"unit_id": "UX", "source_presentations": [{"version": "1957", "extent": "all"}]}
            gate_row = {"section_id": "1.8", "status": "partial", "missing_pieces": [GATE_DUTY], "source_facets": [{"unit_id": "UX"}]}
            assert _is_source_blocked([gate_row], {"UX": unresolvable}, gate_held, {})
            by_hash = {"unit_id": "UH", "source_presentations": [{"artifacts": [{"path": "elsewhere.pdf", "sha256": "ABC123"}]}]}
            gate_row = {"section_id": "1.8", "status": "partial", "missing_pieces": [GATE_DUTY], "source_facets": [{"unit_id": "UH"}]}
            assert not _is_source_blocked([gate_row], {"UH": by_hash}, gate_held, {})
            by_record = {"unit_id": "UR", "source_presentations": [{"bibliographic_record": {"key": "K"}}]}
            gate_row = {"section_id": "1.8", "status": "partial", "missing_pieces": [GATE_DUTY], "source_facets": [{"unit_id": "UR"}]}
            assert not _is_source_blocked([gate_row], {"UR": by_record}, gate_held, {})
            nested_title = {
                "unit_id": "UT",
                "source_presentations": [{"container_record": {"title": "Benchmark Chapter"}}],
            }
            gate_row = {"section_id": "1.8", "status": "partial", "missing_pieces": [GATE_DUTY], "source_facets": [{"unit_id": "UT"}]}
            assert _is_source_blocked([gate_row], {"UT": nested_title}, gate_held, {})

            # Open components: the ledger's explicit notation, plus fallbacks.
            explicit_row = {
                "section_id": "1.9",
                "status": "partial",
                "source_facets": [{"unit_id": "UA", "baseline_content_state": "authored"}],
                "missing_pieces": [
                    {"duty": "d", "component_ids": ["A2"], "kind": "writable"},
                    "[component:A9] still open",
                ],
            }
            explicit_units = {"UA": {"required_components": [{"component_id": "A1"}, {"component_id": "A2"}]}}
            assert _open_components_for_row(explicit_row, explicit_units) == ({"A2", "A9"}, 0)
            fallback_row = {"section_id": "1.10", "status": "partial", "missing_pieces": ["unmapped"], "source_facets": []}
            assert _cluster_component_count([explicit_row, fallback_row], explicit_units) == 3

            good_body.write_text("\\cite[pp.~545--548]{K} \\cite[Thm. 3.2]{K}\n", encoding="utf-8", newline="\n")
            assert _cite_page_findings(["handbook/parts/p01/owned-wt-p01-001.tex"], held) == []
            good_body.write_text("\\cite[p.~549]{K} \\cite[p.~99]{U}\n", encoding="utf-8", newline="\n")
            assert _cite_page_findings(["handbook/parts/p01/owned-wt-p01-001.tex"], held)
            for cite in (
                "\\footcite[549]{K}",
                "\\Textcite[p.~549]{K}",
                "\\Parencite[see][550--551]{K}",
                "\\parencites[12]{X}[549]{K}",
                "\\autocites(see)(and)[pp.~1--2]{X}[549]{K}",
                "\\cite[see {\\S}~3, p.~549]{K}",
                "\\cite[544]{K}",
            ):
                good_body.write_text(cite + "\n", encoding="utf-8", newline="\n")
                assert len(_cite_page_findings(["handbook/parts/p01/owned-wt-p01-001.tex"], held)) >= 1, cite
            good_body.write_text("\\parencites[12]{X}[546]{K} \\cite[\\S~3.2]{K} \\cite[Thm.~9]{K}\n", encoding="utf-8", newline="\n")
            assert _cite_page_findings(["handbook/parts/p01/owned-wt-p01-001.tex"], held) == []
            # Printed offset from the queue presentation's start page.
            offset_held = _held_index_from_data(
                {"entries": [{"path": "source/g.pdf", "bibkeys": ["G"], "pdf_pages": 51, "sha256": "g"}]},
                "fixture-held",
            )
            offset_packet = {
                "units": [
                    {"source_presentations": [{"citation_key": "G", "bibliographic_record": {"page_start": 153, "pages": "153-203"}}]}
                ]
            }
            good_body.write_text("\\cite[p.~160]{G} \\cite[203]{G}\n", encoding="utf-8", newline="\n")
            assert _cite_page_findings(["handbook/parts/p01/owned-wt-p01-001.tex"], offset_held, offset_packet) == []
            good_body.write_text("\\cite[p.~12]{G} \\cite[p.~204]{G}\n", encoding="utf-8", newline="\n")
            assert len(_cite_page_findings(["handbook/parts/p01/owned-wt-p01-001.tex"], offset_held, offset_packet)) == 2
            unknown = _cite_page_findings(["handbook/parts/p01/owned-wt-p01-001.tex"], offset_held, {})
            assert len(unknown) == 1 and "offset unknown" in unknown[0]

            good_body.write_text("around1115\n", encoding="utf-8", newline="\n")
            assert _check_fused("handbook/parts/p01/owned-wt-p01-001.tex")
            good_body.write_text("around 1115\n", encoding="utf-8", newline="\n")
            assert _check_fused("handbook/parts/p01/owned-wt-p01-001.tex") == []

            good_body.write_text("Routine verification.\n", encoding="utf-8", newline="\n")
            assert _stub_markers("handbook/parts/p01/owned-wt-p01-001.tex")
            good_body.write_text("A direct verification.\n", encoding="utf-8", newline="\n")
            assert _stub_markers("handbook/parts/p01/owned-wt-p01-001.tex") == []

            good_body.write_text("\\renewcommand{\\x}{y}\n", encoding="utf-8", newline="\n")
            assert _new_macro_defs("handbook/parts/p01/owned-wt-p01-001.tex")
            good_body.write_text("\\emph{not a definition}\n", encoding="utf-8", newline="\n")
            assert _new_macro_defs("handbook/parts/p01/owned-wt-p01-001.tex") == []
            for definition in (
                "\\DeclareRobustCommand{\\x}{y}",
                "\\newtheorem{claim}{Claim}",
                "\\DeclarePairedDelimiter\\abs{\\lvert}{\\rvert}",
                "\\NewDocumentEnvironment{e}{}{}{}",
                "\\def\\x{y}",
            ):
                good_body.write_text(definition + "\n", encoding="utf-8", newline="\n")
                assert _new_macro_defs("handbook/parts/p01/owned-wt-p01-001.tex"), definition
            good_body.write_text("\\left( \\letter \\default \\undefined \\right)\n", encoding="utf-8", newline="\n")
            assert _new_macro_defs("handbook/parts/p01/owned-wt-p01-001.tex") == []

            good_body.write_text("\\begin{proof}\n", encoding="utf-8", newline="\n")
            assert _env_balance("handbook/parts/p01/owned-wt-p01-001.tex")
            good_body.write_text("\\begin {proof}\n", encoding="utf-8", newline="\n")
            assert _env_balance("handbook/parts/p01/owned-wt-p01-001.tex")
            good_body.write_text("\\begin{proof}\\end{proof}\n", encoding="utf-8", newline="\n")
            assert _env_balance("handbook/parts/p01/owned-wt-p01-001.tex") == []
            good_body.write_text("\\begin {proof}\\end{ proof }\n", encoding="utf-8", newline="\n")
            assert _env_balance("handbook/parts/p01/owned-wt-p01-001.tex") == []

            stripped = _strip_for_copy(
                "Keep one \\cite[see {\\S}~3]{K} two \\parencites[a]{A}[b]{B} three "
                "\\label{x:y} \\begin{eqnarray}lost\\end{eqnarray} \\begin{alignat*}{2}gone\\end{alignat*} "
                "\\begin{math}away\\end{math} \\href{http://u}{shown} four"
            )
            # Cite notes print and stay; keys, labels and math go.
            assert _tokens(stripped) == ["keep", "one", "see", "two", "a", "b", "three", "shown", "four"], _tokens(stripped)

            source_words = " ".join(f"word{i}" for i in range(1, 30))
            (ROOT / "source/s.txt").write_text(source_words, encoding="utf-8", newline="\n")
            copy_packet = {"units": [{"held_paths": ["source/s.txt"]}]}
            good_body.write_text("Plain prose.\n", encoding="utf-8", newline="\n")
            hard, copied = _copy_runs({"units": [{"held_paths": ["source/absent.pdf"]}]}, ["handbook/parts/p01/owned-wt-p01-001.tex"])
            assert hard == [] and copied and "no extractable text" in copied[0]
            good_body.write_text("\\emph{" + " ".join(f"word{i}" for i in range(1, 15)) + "}\n", encoding="utf-8", newline="\n")
            hard, copied = _copy_runs(copy_packet, ["handbook/parts/p01/owned-wt-p01-001.tex"])
            assert hard == [] and copied
            good_body.write_text(" ".join(f"word{i}" for i in range(1, 27)) + "\n", encoding="utf-8", newline="\n")
            hard, copied = _copy_runs(copy_packet, ["handbook/parts/p01/owned-wt-p01-001.tex"])
            assert hard and copied == []
            good_body.write_text("\\[ " + source_words + " \\]\n", encoding="utf-8", newline="\n")
            hard, copied = _copy_runs(copy_packet, ["handbook/parts/p01/owned-wt-p01-001.tex"])
            assert hard == [] and copied == []

            normalized_source = (
                "alpha beta \ufb01nancial delta epsilon zeta eta theta iota kappa lambda mu "
                "nu xi omicron pi rho sigma tau upsilon phi chi psi omega cri-\n"
                "terion final quoted words"
            )
            normalized_owned = (
                "alpha beta financial delta epsilon zeta eta theta iota kappa lambda mu "
                "nu xi omicron pi rho sigma tau upsilon phi chi psi omega criterion final quoted words"
            )
            (ROOT / "source/s.txt").write_text(normalized_source, encoding="utf-8", newline="\n")
            good_body.write_text("``" + normalized_owned + "''\n", encoding="utf-8", newline="\n")
            hard, copied = _copy_runs(copy_packet, ["handbook/parts/p01/owned-wt-p01-001.tex"])
            assert hard and copied == []

            good_body.write_text(
                "This\nrecord has review ledger assessor intake wave waves "
                "admission admissions admitted author block.\n",
                encoding="utf-8",
                newline="\n",
            )
            assert len(_workflow_words("handbook/parts/p01/owned-wt-p01-001.tex")) >= 9
            good_body.write_text("The theory admits quantifier elimination. Each wavelet is ordinary prose.\n", encoding="utf-8", newline="\n")
            assert _workflow_words("handbook/parts/p01/owned-wt-p01-001.tex") == []

            p19 = ROOT / "handbook/parts/p19/owned.tex"
            p19.parent.mkdir(parents=True, exist_ok=True)
            p19.write_text("This must hold.\n", encoding="utf-8", newline="\n")
            assert _prescriptive_words("handbook/parts/p19/owned.tex")
            p19.write_text("This holds.\n", encoding="utf-8", newline="\n")
            assert _prescriptive_words("handbook/parts/p19/owned.tex") == []

            bad_encoding = ROOT / "handbook/parts/p01/bad-encoding.tex"
            bad_encoding.write_bytes(b"\xff")
            assert _encoding_guard("handbook/parts/p01/bad-encoding.tex")
            bad_encoding.unlink()
            good_body.write_text("utf-8\n", encoding="utf-8", newline="\n")
            assert _encoding_guard("handbook/parts/p01/owned-wt-p01-001.tex") == []

            log_dir = ROOT / "tmp-log"
            log_dir.mkdir()
            (log_dir / "unit.log").write_text(
                "LaTeX Warning: Reference `thm:nowhere' on page 1 undefined on input line 7.\n"
                "LaTeX Warning: Citation `MissingKey' on page 1 undefined on input line 8.\n",
                encoding="utf-8",
                newline="\n",
            )
            parsed_log = _parse_unit_log(log_dir)
            assert parsed_log["undefined_refs_unknown"] == ["thm:nowhere"]
            assert parsed_log["undefined_citations"] == ["MissingKey"]
            assert not parsed_log["ok"]
            (log_dir / "unit.log").write_text(
                "./parts/p01/owned-wt-p01-001.tex:12: LaTeX Error: Environment foo undefined.\n"
                "Overfull \\hbox (1.0pt too wide) in paragraph at lines 3--4\n"
                "Overfull \\vbox (2.0pt too high) has occurred while \\output is active\n",
                encoding="utf-8",
                newline="\n",
            )
            parsed_log = _parse_unit_log(log_dir)
            assert not parsed_log["ok"] and parsed_log["overfull"] == 2
            assert parsed_log["errors"][0].startswith("./parts/p01/owned-wt-p01-001.tex:12:")
            wrapped_cite = "LaTeX Warning: Citation `VeryLongCitationKeyForWrapping2001' on page 1 undefined on input line 9."
            wrapped_ref = "LaTeX Warning: Reference `sec:an-unusually-long-label-name-that-wraps-in-the-log' on page 2 undefined on input line 3."
            for line in (wrapped_cite, wrapped_ref):
                assert len(line) > 79 and "undefined" not in line[:79]
            (log_dir / "unit.log").write_text(
                "LaTeX Warning: Hyper reference `sec:nowhere' on page 1 undefined on input line 5.\n"
                + wrapped_cite[:79] + "\n" + wrapped_cite[79:] + "\n"
                + wrapped_ref[:79] + "\n" + wrapped_ref[79:] + "\n",
                encoding="utf-8",
                newline="\n",
            )
            parsed_log = _parse_unit_log(log_dir)
            assert parsed_log["undefined_refs_unknown"] == [
                "sec:an-unusually-long-label-name-that-wraps-in-the-log", "sec:nowhere"
            ], parsed_log
            assert parsed_log["undefined_citations"] == ["VeryLongCitationKeyForWrapping2001"], parsed_log
            (log_dir / "unit.log").write_text(
                "LaTeX Warning: There were undefined references.\n", encoding="utf-8", newline="\n"
            )
            assert not _parse_unit_log(log_dir)["ok"]
            (log_dir / "unit.log").write_text(
                "LaTeX Warning: Reference `sec:owned' on page 1 undefined on input line 2.\n"
                "LaTeX Warning: There were undefined references.\n",
                encoding="utf-8",
                newline="\n",
            )
            good_body.write_text("\\label{sec:owned}\n", encoding="utf-8", newline="\n")
            assert _parse_unit_log(log_dir)["ok"]
            (log_dir / "unit.log").unlink()
            assert not _parse_unit_log(log_dir)["ok"]

            # Sidecars: content-derived blocker ids, nothing lost on merge.
            blocker_rows = [{"section_id": "2.1", "source_facets": [{"unit_id": "UM"}]}]
            first_blocker = _blocker_record("ws", blocker_rows, {"UM": missing_unit})
            assert first_blocker == _blocker_record("ws", list(blocker_rows), {"UM": missing_unit})
            other_blocker = _blocker_record("ws", [{"section_id": "2.2"}], {})
            assert first_blocker["id"] != other_blocker["id"]
            _write_wave_outputs("ws", [], [first_blocker])
            blockers_file = ROOT / WAVES_ROOT / "ws/blockers.jsonl"
            with blockers_file.open("a", encoding="utf-8", newline="\n") as handle:
                handle.write(_json_line({"note": "hand-written record without an id"}) + "\n")
            _write_wave_outputs("ws", [], [other_blocker])
            records = _read_jsonl_records(blockers_file)
            assert {"note": "hand-written record without an id"} in records
            by_id = {item.get("id"): item for item in records}
            assert by_id[first_blocker["id"]]["status"] == "superseded"
            assert by_id[other_blocker["id"]]["status"] == "open"
            _write_wave_outputs("ws", [], [])
            needs = _load_json(ROOT / WAVES_ROOT / "ws/acquisition-needs.json", {})["needs"]
            assert {item["id"] for item in needs} == {first_blocker["id"], other_blocker["id"]}
            assert len(_read_jsonl_records(blockers_file)) == 3
            records = _read_jsonl_records(blockers_file)
            for item in records:
                if item.get("id") == first_blocker["id"]:
                    item.update({"status": "acquired", "note": "bought a copy"})
            _write_atomic(blockers_file, "".join(_json_line(item) + "\n" for item in records))
            _write_wave_outputs("ws", [], [first_blocker])
            by_id = {item.get("id"): item for item in _read_jsonl_records(blockers_file)}
            assert by_id[first_blocker["id"]]["status"] == "acquired", by_id
            assert by_id[first_blocker["id"]]["note"] == "bought a copy", by_id
            assert by_id[other_blocker["id"]]["status"] == "superseded", by_id
            needs = {item["id"]: item for item in _load_json(ROOT / WAVES_ROOT / "ws/acquisition-needs.json", {})["needs"]}
            assert needs[first_blocker["id"]]["status"] == "acquired", needs
            assert len(_read_jsonl_records(blockers_file)) == 3

            # A split leaves the parent wave with no runnable packets or args.
            split_root = ROOT / WAVES_ROOT / "wsp"
            (split_root / "packets").mkdir(parents=True)
            (split_root / "packets/wsp-p01-999.json").write_text('{"id": "wsp-p01-999"}\n', encoding="utf-8", newline="\n")
            (split_root / "args.json").write_text("{}\n", encoding="utf-8", newline="\n")
            split_packets = [
                {"id": f"wsp-p01-{i:03d}", "wave": "wsp", "part": "P1", "sections": [{"section_id": f"1.{i}"}],
                 "max_blocks": 4, "lane": i}
                for i in range(1, 107)
            ]
            with contextlib.redirect_stdout(io.StringIO()):
                assert _write_split_waves("wsp", split_packets, [], apply=True) == 0
            assert not (split_root / "args.json").exists()
            assert list((split_root / "packets").glob("*.json")) == []
            for half in ("wspa", "wspb"):
                assert (ROOT / WAVES_ROOT / half / "args.json").is_file(), half

            carry_file = ROOT / "carry.json"
            carry_file.write_text(json.dumps({"carry": ["1.1", {"section_id": "1.2"}]}), encoding="utf-8", newline="\n")
            assert _carry_section_ids(carry_file) == ["1.1", "1.2"]
            carry_file.write_text(json.dumps([{"title": "no id"}]), encoding="utf-8", newline="\n")
            try:
                _carry_section_ids(carry_file)
                raise AssertionError("carry item without a section id should fail")
            except UsageError:
                pass

            assert "Scoped annex host" not in _unit_template(guard_packet)
            good_annex.write_text("\\subsection{Annex item}\n", encoding="utf-8", newline="\n")
            assert "\\section{Scoped annex host}\n\\input{annex/p01/owned-wt-p01-001}" in _unit_template(guard_packet)
            # The intake bib is named with its .bib extension exactly once.
            bib.write_text("@book{K,\n title={T}\n}\n", encoding="utf-8", newline="\n")
            bib_lines = [line for line in _unit_template(guard_packet).splitlines() if "intake-" in line]
            assert bib_lines == ["\\addbibresource{bib/intake-p01-owned-wt-p01-001.bib}"], bib_lines
            bib.unlink()
            assert "intake-" not in _unit_template(guard_packet)

            globals()["_texlive_command"] = lambda name: None
            texlive_result = unit_compile_packet(guard_packet, run_build=True)
            assert not texlive_result["ok"]
            globals()["_texlive_command"] = old_texlive_command

            _selftest_integrity(Path(td) / "integrity")
            _selftest_packet_ids(Path(td) / "packet-ids")
            _selftest_accounting(Path(td) / "accounting")
            _selftest_unit_insertions(Path(td) / "unit-insertions")
            _selftest_anchors(Path(td) / "anchors")
    finally:
        globals()["unit_compile_packet"] = old_unit_compile
        globals()["_run_check_findings"] = old_run_check
        globals()["_texlive_command"] = old_texlive_command
        ROOT = old_root


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Authoring wave packet and verification tools.")
    parser.add_argument("--selftest", action="store_true", help="run internal tests")
    sub = parser.add_subparsers(dest="command")

    p_packetize = sub.add_parser("packetize", help="build wave packet JSONs")
    p_packetize.add_argument("wave")
    p_packetize.add_argument("--parts", required=True)
    p_packetize.add_argument("--carry")
    p_packetize.add_argument("--census")
    p_packetize.add_argument("--dry-run", action="store_true")
    p_packetize.add_argument("--apply", action="store_true")
    p_packetize.add_argument(
        "--force",
        action="store_true",
        help="rewrite, renumber or remove packets that already have a snapshot or verdict",
    )

    p_snapshot = sub.add_parser("snapshot", help="record a packet ownership snapshot")
    p_snapshot.add_argument("packet", nargs="+", help="one or more packet JSON paths (batch: tree/check computed once)")
    p_snapshot.add_argument("--dry-run", action="store_true")
    p_snapshot.add_argument("--apply", action="store_true")
    p_snapshot.add_argument("--force", action="store_true", help="replace an existing snapshot")

    p_verify = sub.add_parser("verify", help="verify a packet against its snapshot")
    p_verify.add_argument("packet")
    p_verify.add_argument(
        "--snapshot-sha256",
        help="optional: the digest snapshot --apply printed; the snapshot read from base_sha must match it",
    )

    p_compile = sub.add_parser("unit-compile", help="run a scoped packet build")
    p_compile.add_argument("packet")

    p_report = sub.add_parser("report", help="summarize a wave results file and verdicts")
    p_report.add_argument("wave")

    args = parser.parse_args(argv)
    if args.selftest:
        _selftest()
        return 0
    if args.command is None:
        parser.print_usage(sys.stderr)
        return 2
    try:
        if args.command == "packetize":
            return packetize(args)
        if args.command == "snapshot":
            packets = args.packet if isinstance(args.packet, list) else [args.packet]
            rc = 0
            with _snapshot_batch_cache():
                for packet in packets:
                    one = argparse.Namespace(**{**vars(args), "packet": packet})
                    rc = max(rc, snapshot(one))
            return rc
        if args.command == "verify":
            return verify(args)
        if args.command == "unit-compile":
            return unit_compile(args)
        if args.command == "report":
            return report(args)
    except UsageError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    except Refusal as exc:
        print(f"refusal: {exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

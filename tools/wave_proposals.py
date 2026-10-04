#!/usr/bin/env python3
"""Wave results + coverage assessment files -> ledger proposals and unit residuals.

TOOLING-SPEC section 11. Dry run by default; --apply writes
work/waves/<wave>/proposals.jsonl and appends to
spec/coverage/edition-2026/unit-residuals.jsonl. The lead then runs
`python -B tools/ledger_patch.py apply --proposals work/waves/<wave>/proposals.jsonl [--apply]`.

Rules beyond the literal text of section 11 (each one keeps a proposal inside what
`ledger_patch.py apply` accepts; see the selftest):
- authored_unreviewed needs a result with status authored_unreviewed and no gaps or
  blocked items, a valid first/confirm pair (a != c, roles first/confirm, distinct
  casefolded context_ids), identical component and duty sets in a and c, every raw
  component and duty entry of both files an object with verdict covered (the
  ledger_patch rule), every covered component in an emitted evidence entry, every
  inputs.tex sha256 of a and c current, and an on-route evidence path among each
  file's inputs (ledger_patch's own stale-input and route checks).
  A result that asks for AU and fails this is downgraded to partial; each component
  or duty that is not established gets an `assessment_dispute` missing piece. A
  partial/missing result is never upgraded.
- Duplicate component ids / duty keys with conflicting verdicts, and entries that
  are not objects, are not established: `assessment_dispute` pieces on every open row.
- Every open-gap piece has kind "writable" (section 11).
- Section missing pieces never carry kind lead_owned (ledger_patch has no such
  kind): not_assessable / lead_owned map to `assessment_dispute`. Unit residuals
  keep lead_owned.
- A blocked_* item needs an ACQ-/MATH-/POL- ref that ledger_patch can resolve:
  the assessment's own blocker.ref when it is on record, else a record in
  acquisition-requests.jsonl / blockers.jsonl matching the kind and the section or
  its facet units. Without one the section is an error (ledger_patch would refuse it).
- Evidence outside the repository root or with a line range outside its file, and
  labels containing a macro parameter (`#`), are skipped.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import re
import sys
import tempfile
import unicodedata
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ledger_patch as lp  # noqa: E402
from find_fused_spaces import _fixed_text, _scan  # noqa: E402

ROOT = lp.ROOT
SCRATCH = ROOT / "tmp" / "tooling-scratch" / "wave-proposals"

# Assessment verdicts / blocker kinds / result kinds -> residual kinds.
KIND_ALIASES = {
    "writable": "writable",
    "partial": "writable",
    "absent": "writable",
    "missing": "writable",
    "not_covered": "writable",
    "blocked_source": "blocked_source",
    "source_not_held": "blocked_source",
    "blocked_math": "blocked_math",
    "blocked_policy": "blocked_policy",
    "lead_owned": "lead_owned",
    "not_assessable": "lead_owned",
}
# Residual kind -> ledger missing_pieces kind (ledger_patch MISSING_PIECE_KINDS).
SECTION_KIND = {"lead_owned": "assessment_dispute"}
DISPUTE = "assessment_dispute"
OPEN_STATUSES = {"partial", "missing"}
REF_KEYS = ("acq_id", "id", "blocker_ref", "request_id", "ref")
LABEL_TOKEN_RE = re.compile(r"(?<![\w.\\/-])[A-Za-z][A-Za-z0-9]*:[A-Za-z0-9][\w.:-]*")
LABEL_RE = re.compile(r"\\label\s*\{\s*([^{}]+?)\s*\}")
BEGIN_RE = re.compile(r"\\begin\s*\{\s*([A-Za-z*]+)\s*\}")
WAVE_RE = re.compile(r"w\d+[a-z0-9]*")


class WaveError(Exception):
    """A result or assessment cannot be turned into a proposal or residual."""


def _jdump(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def fix_fused(text: str) -> str:
    """Insert spaces until classes A-C of find_fused_spaces (plain text) are clean."""
    for _ in range(5):
        hits = [hit for hit in _scan(text, text, tex=False) if hit.cls in {"A", "B", "C"}]
        if not hits:
            return text
        text = _fixed_text(text, hits)
    raise WaveError(f"fused-number hits persist after repair: {text[:80]!r}")


def normalize_kind(raw: Any) -> str:
    kind = KIND_ALIASES.get(str(raw or "").strip().lower())
    if kind is None:
        raise WaveError(f"unknown open-component kind {raw!r}")
    return kind


def component_kind(comp: dict[str, Any]) -> str:
    """A non-covered component's kind: its blocker kind when it names one, else its verdict."""
    blocker = comp.get("blocker")
    if isinstance(blocker, dict) and blocker.get("kind"):
        kind = normalize_kind(blocker["kind"])
        if kind != "writable":
            return kind
    return normalize_kind(comp.get("verdict"))


def _components(assessment: dict[str, Any]) -> list[dict[str, Any]]:
    raw = assessment.get("components")
    return [item for item in raw if isinstance(item, dict)] if isinstance(raw, list) else []


def _norm(text: Any) -> str:
    return " ".join(str(text or "").split()).casefold()


def audit(assessment: dict[str, Any] | None) -> tuple[dict[str, dict[str, Any]], dict[str, str], list[str]]:
    """-> (items, conflicts, malformed). items: component id, or "duty:<duty_id or normalised
    duty text>" -> its object; a duplicate key keeps a non-covered entry over a covered one.
    conflicts: key -> the disagreeing verdicts. malformed: entries that are not objects."""
    items: dict[str, dict[str, Any]] = {}
    verdicts: dict[str, set[str]] = {}
    malformed: list[str] = []
    for kind, raw in (("component", (assessment or {}).get("components")), ("duty", (assessment or {}).get("duties"))):
        for entry in raw if isinstance(raw, list) else []:
            if not isinstance(entry, dict):
                malformed.append(f"{kind} entry {entry!r} is not an object")
                continue
            key = (str(entry.get("component_id")) if kind == "component"
                   else "duty:" + _norm(entry.get("duty_id") or entry.get("duty")))
            verdicts.setdefault(key, set()).add(str(entry.get("verdict")))
            if items.get(key, {}).get("verdict", "covered") == "covered":
                items[key] = entry
    conflicts = {key: ", ".join(sorted(v)) for key, v in verdicts.items() if len(v) > 1}
    return items, conflicts, malformed


def all_covered(assessment: dict[str, Any] | None) -> bool:
    """ledger_patch's raw rule: every component and duty entry is an object with verdict covered."""
    try:
        lp._validate_verdicts_covered(assessment or {})
    except lp.Refusal:
        return False
    return True


def confirm_problem(a: Any, first: dict[str, Any], c: Any, confirm: dict[str, Any] | None) -> str | None:
    """Why (a, c) is not an independent first/confirm pair; None when it is.
    Same rule as ledger_patch._has_first_confirm_pair, plus a != c."""
    if confirm is None:
        return "no confirm assessment"
    if a == c:
        return "the confirm assessment id equals the first"
    (role_a, ctx_a), (role_c, ctx_c) = lp._assessor_role_context(first), lp._assessor_role_context(confirm)
    if (role_a, role_c) != ("first", "confirm"):
        return f"assessor roles are {role_a!r} and {role_c!r}, not 'first' and 'confirm'"
    if ctx_a is None or ctx_c is None or ctx_a == ctx_c:
        return "first and confirm lack distinct assessor.context_id values"
    return None


_UNIT_COMPONENTS: dict[Path, dict[str, set[str]]] = {}


def unit_components(root: Path) -> dict[str, set[str]]:
    """queue unit_id -> its required component ids (cached per root)."""
    if root not in _UNIT_COMPONENTS:
        found: dict[str, set[str]] = {}
        path = root / lp.QUEUE_PATH
        for line in path.read_text(encoding="utf-8").splitlines() if path.is_file() else []:
            if line.strip():
                unit = json.loads(line)
                found[str(unit.get("unit_id"))] = {str(c.get("component_id")) for c in unit.get("required_components") or []
                                                   if isinstance(c, dict)}
        _UNIT_COMPONENTS[root] = found
    return _UNIT_COMPONENTS[root]


def load_assessments(root: Path, wave: str) -> dict[str, dict[str, Any]]:
    base = root / lp.ASSESSMENTS_DIR / wave
    found: dict[str, dict[str, Any]] = {}
    for path in sorted(base.glob("*.json")) if base.is_dir() else []:
        data = lp._read_json(path)
        if isinstance(data, dict) and data.get("assessment_id") == path.stem:
            found[path.stem] = data
    return found


def _need(assessments: dict[str, dict[str, Any]], assessment_id: Any, wave: str) -> dict[str, Any]:
    if not isinstance(assessment_id, str) or assessment_id not in assessments:
        raise WaveError(f"assessment {assessment_id!r} not found under assessments/{wave}/")
    return assessments[assessment_id]


def load_blockers(root: Path) -> list[dict[str, Any]]:
    """Blocker records ledger_patch resolves: acquisition requests (blocked_source) and blockers.jsonl."""
    records: list[dict[str, Any]] = []
    for relative, default_kind in ((lp.ACQUISITION_PATH, "blocked_source"), (lp.BLOCKERS_PATH, None)):
        path = root / relative
        if not path.is_file():
            continue
        with path.open("r", encoding="utf-8-sig") as handle:
            for line in handle:
                item = json.loads(line) if line.strip() else None
                if not isinstance(item, dict):
                    continue
                ref = next((item[key] for key in REF_KEYS if isinstance(item.get(key), str)
                            and item[key].startswith(lp.BLOCKER_PREFIXES)), None)
                if ref is None:
                    continue
                strings = lambda key: {v for v in item.get(key) or [] if isinstance(v, str)}  # noqa: E731
                records.append({"ref": ref, "kind": KIND_ALIASES.get(str(item.get("kind") or default_kind).lower()),
                                "units": strings("units"), "sections": strings("sections"),
                                "cite": cite_tokens(item.get("key"))})
    return records


def _fold(text: str) -> str:
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().casefold()


def cite_tokens(key: Any) -> tuple[str, str] | None:
    """(first author surname, year) from a citation key such as Craig1957 or BaazEglyLeitsch2001;
    ("src-059", "") for a source-series key such as SRC-059 (matched by its id in the duty)."""
    s = str(key or "")
    if re.fullmatch(r"SRC-\d{3}", s):
        return (s.casefold(), "")
    m = re.match(r"([A-Z][a-z]+)[A-Za-z]*?(\d{4})", s)
    return (_fold(m.group(1)), m.group(2)) if m else None


def _cited_at(rec: dict[str, Any], duty: str) -> tuple[int, int] | None:
    """(position, gap to the year) where the duty names the record's work (surname, then its year
    within 200 characters), else None. A mention the duty itself marks as held ("Kleene 1952
    (held, ...") names no blocker; a downloaded file is not proof, since it may be another version."""
    tok = rec.get("cite")
    if not tok:
        return None
    folded = _fold(duty)
    for m in re.finditer(re.escape(tok[0]), folded):
        gap = folded.find(tok[1], m.end(), m.end() + 200)
        if gap < 0:
            continue
        after = folded[gap + len(tok[1]):gap + len(tok[1]) + 12]
        if re.match(r"\W{0,3}\(held", after):
            continue
        return m.start(), gap - m.end()
    return None


def resolve_ref(kind: str, comps: list[dict[str, Any]], units: list[str], section_id: str | None,
                blockers: list[dict[str, Any]], duty: str = "") -> str | None:
    """The assessment's own blocker.ref when on record; else the record whose work the duty names
    first (surname and year); else the most specific matching record."""
    known = {rec["ref"] for rec in blockers}
    for comp in comps:
        blocker = comp.get("blocker")
        ref = blocker.get("ref") if isinstance(blocker, dict) else None
        if isinstance(ref, str) and ref.strip() in known:
            return ref.strip()
    # A named work (surname + year) beats a source-series id; then first named; then order.
    named = [(not (rec.get("cite") or ("", ""))[1], pos, order, rec["ref"]) for order, rec in enumerate(blockers)
             if rec["kind"] == kind and (pos := _cited_at(rec, duty)) is not None]
    if named:
        return min(named)[3]
    unit_set = set(units)
    # A record naming this section beats one that only shares a unit; then fewer units; then order.
    candidates = [(section_id not in rec["sections"], len(rec["units"]), order, rec["ref"])
                  for order, rec in enumerate(blockers)
                  if rec["kind"] == kind and (rec["units"] & unit_set or section_id in rec["sections"])]
    return min(candidates)[3] if candidates else None


# ---------------------------------------------------------------- evidence


def declared_labels(text: str) -> list[tuple[int, str]]:
    """(line, label) for every \\label{..} and label-argument environment, comments/verbatim
    stripped; macro-parameter labels (\\label{#1}) are not labels."""
    search = lp._tex_search_text(text)  # keeps newlines, so line numbers stay valid
    found: list[tuple[int, int, str]] = []
    for match in LABEL_RE.finditer(search):
        found.append((match.start(), search.count("\n", 0, match.start()) + 1, match.group(1)))
    for match in BEGIN_RE.finditer(search):
        if match.group(1) not in lp.LABEL_ARG_ENVIRONMENTS:
            continue
        pos = match.end()
        while (end := lp._balanced_bracket_end(search, pos, "[", "]")) is not None:
            pos = end
        first = lp._first_braced_arg(search, pos)
        if first is not None and first[0].strip():
            found.append((match.start(), search.count("\n", 0, match.start()) + 1, first[0].strip()))
    return [(line, label) for _, line, label in sorted(found) if "#" not in label]


def pick_anchor(text: str, label_strings: list[str], line_start: int) -> str | None:
    declared = declared_labels(text)
    names = {label for _, label in declared}
    for raw in label_strings:
        for match in LABEL_TOKEN_RE.finditer(raw or ""):
            token = match.group(0).rstrip(".:-")
            if token in names:
                return token
    before = [label for line, label in declared if line <= line_start]
    return before[-1] if before else None


def au_input_problems(root: Path, row: lp.LedgerRow, evidence: list[dict[str, Any]],
                      pair: list[tuple[str, dict[str, Any]]], reached: set[str]) -> list[str]:
    """TOOLING-SPEC 4 upgrade rules 4-5, through ledger_patch's own checks: why an AU
    proposal would be refused for stale inputs or off-route evidence; [] when it would not."""
    live = {e["path"] for e in evidence if lp._route_state(e["path"], reached) == "on_current_recursive_input_route"}
    live |= lp._live_on_route_evidence_paths(root, row.obj.get("reader_evidence", []), reached)
    problems = [] if live else [
        "no evidence path is on the current recursive input route ("
        + ", ".join(sorted({e["path"] for e in evidence})) + ")"]
    for aid, data in pair:
        try:
            inputs = lp._validate_assessment_inputs_current(root, data)
        except lp.Refusal as exc:
            problems.append(str(exc).replace(" sha256 ", " hash "))  # "sha256" would be split by fix_fused
            continue
        if live and inputs.isdisjoint(live):
            problems.append(f"{aid}: inputs.tex ({', '.join(sorted(inputs))}) includes no on-route evidence path")
    return problems


def build_evidence(root: Path, first: dict[str, Any], a: str, warnings: list[str],
                   skip: set[str] = frozenset()) -> list[dict[str, Any]]:
    """One entry per path over the first assessment's covered components (except `skip`);
    assessment_ids=[a]."""
    groups: dict[str, list[tuple[str, int, int, str]]] = {}
    for comp in _components(first):
        if comp.get("verdict") != "covered" or str(comp.get("component_id")) in skip:
            continue
        for ev in comp.get("evidence") or []:
            path = ev.get("path") if isinstance(ev, dict) else None
            start, end = (ev.get("line_start"), ev.get("line_end")) if isinstance(ev, dict) else (None, None)
            if not isinstance(path, str) or not all(isinstance(v, int) and not isinstance(v, bool) for v in (start, end)):
                continue
            try:
                path = (root / path.replace("\\", "/")).resolve().relative_to(root.resolve()).as_posix()
            except ValueError:
                warnings.append(f"evidence path skipped (outside the repository): {path}")
                continue
            groups.setdefault(path, []).append((str(comp["component_id"]), start, end, str(ev.get("label") or "")))
    entries: list[dict[str, Any]] = []
    for path, items in groups.items():
        file = root / path
        if not file.is_file():
            warnings.append(f"evidence path skipped (missing): {path}")
            continue
        try:
            text = file.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            warnings.append(f"evidence path skipped (not UTF-8): {path}")
            continue
        count = lp._line_count(file)
        good = []
        for cid, start, end, label in items:
            if start < 1 or end < start or end > count:
                warnings.append(f"evidence skipped (lines {start}-{end} outside 1-{count}): {path} for {cid}")
            else:
                good.append((cid, start, end, label))
        if not good:
            continue
        line_start, line_end = min(g[1] for g in good), max(g[2] for g in good)
        anchor = pick_anchor(text, [g[3] for g in good], line_start)
        if anchor is None:
            warnings.append(f"evidence path skipped (no declared label at or before line {line_start}): {path}")
            continue
        entries.append(
            {
                "path": path,
                "anchor": anchor,
                "line_start": line_start,
                "line_end": line_end,
                "read_extent": fix_fused(f"coverage assessment {a}"),
                "components": list(dict.fromkeys(g[0] for g in good)),
                "assessment_ids": [a],
            }
        )
    return entries


# ---------------------------------------------------------------- sections


def _id_mentioned(component_id: str, text: str) -> bool:
    return re.search(r"(?<![\w-])" + re.escape(component_id) + r"(?![\w-])", text) is not None


def _range_ids(text: str, component_ids: list[str]) -> set[str]:
    """'X-SECTION-1..5' names X-SECTION-1 .. X-SECTION-5."""
    hits: set[str] = set()
    for match in re.finditer(r"([\w-]*?)(\d+)\.\.(\d+)", text):
        prefix, low, high = match.group(1), int(match.group(2)), int(match.group(3))
        hits.update(f"{prefix}{n}" for n in range(low, high + 1) if f"{prefix}{n}" in component_ids)
    return hits


def match_gap(gap: str, open_comps: list[dict[str, Any]]) -> list[dict[str, Any]]:
    ids = [c["component_id"] for c in open_comps]
    named = {cid for cid in ids if _id_mentioned(cid, gap)} | _range_ids(gap, ids)
    if not named:
        body = _norm(gap.split(": ", 1)[1] if ": " in gap else gap)
        named = {
            c["component_id"]
            for c in open_comps
            if _norm(c.get("gap")) and (_norm(c.get("gap")) in _norm(gap) or body in _norm(c.get("gap")))
        }
    return [c for c in open_comps if c["component_id"] in named] or list(open_comps)


def _since(old_row: dict[str, Any], kind: str, component_ids: list[str], wave: str) -> str:
    for item in old_row.get("missing_pieces") or []:
        if (
            isinstance(item, dict)
            and item.get("kind") == kind
            and sorted(item.get("component_ids") or []) == sorted(component_ids)
            and isinstance(item.get("since"), str)
        ):
            return item["since"]
    return wave


def section_proposal(
    root: Path,
    wave: str,
    packet_id: str,
    sec: dict[str, Any],
    row: lp.LedgerRow,
    assessments: dict[str, dict[str, Any]],
    blockers: list[dict[str, Any]],
    warnings: list[str],
    reached: set[str],
) -> dict[str, Any]:
    section_id = sec["section_id"]
    a, c = sec.get("a"), sec.get("c")
    first = _need(assessments, a, wave)
    confirm = _need(assessments, c, wave) if c else None
    for label, data in (("a", first), ("c", confirm)):
        if data is not None and data.get("section_id") != section_id:
            raise WaveError(f"assessment {label}={data.get('assessment_id')} is for section {data.get('section_id')!r}")
    problem = confirm_problem(a, first, c, confirm)
    if c and problem:
        warnings.append(f"{section_id}: confirm {c} not used: {problem}")
    first_items, first_conflicts, first_bad = audit(first)
    confirm_items, confirm_conflicts, confirm_bad = audit(confirm) if problem is None else ({}, {}, [])
    # Duplicate keys with disagreeing verdicts, and non-object entries: never established.
    flawed: dict[str, str] = {}
    for aid, conflicts in ((a, first_conflicts), (c, confirm_conflicts)):
        for key, verdicts in conflicts.items():
            flawed.setdefault(key, f"conflicting verdicts in {aid}: {verdicts}")
    malformed = [f"{aid}: {m}" for aid, bad in ((a, first_bad), (c, confirm_bad)) for m in bad]
    evidence = build_evidence(root, first, a, warnings, skip=set(flawed))
    evidenced = {cid for entry in evidence for cid in entry["components"]}
    # Covered in a, but not established by an independent confirm plus a usable evidence entry.
    unestablished: dict[str, tuple[dict[str, Any], str]] = {}
    for key, obj in first_items.items():
        if obj.get("verdict") != "covered" or key in flawed:
            continue
        other = confirm_items.get(key)
        if problem:
            why = problem
        elif other is None:
            why = f"not assessed in confirm {c}"
        elif other.get("verdict") != "covered":
            why = f"confirm {c} verdict {other.get('verdict')}" + (f": {other['gap']}" if other.get("gap") else "")
        elif not key.startswith("duty:") and key not in evidenced:
            why = "no usable evidence entry"
        else:
            continue
        unestablished[key] = (obj, why)
    for key in confirm_items.keys() - first_items.keys() - flawed.keys():
        unestablished[key] = (confirm_items[key], f"assessed in confirm {c} but not in first {a}")
    # Owed components: every required component of the row's facet units (judged anywhere on the
    # route). An assessor's covered extra outside that set is not owed here; an owed one neither
    # assessor judged is not established.
    owed = set().union(*(unit_components(root).get(f.get("unit_id"), set())
                         for f in row.obj.get("source_facets") or [] if isinstance(f, dict)))
    if owed:
        for key in [k for k, (obj, _) in unestablished.items()
                    if not k.startswith("duty:") and k not in owed and obj.get("verdict") == "covered"]:
            del unestablished[key]
        if sec.get("status") == "authored_unreviewed" and problem is None:
            for key in sorted(owed - first_items.keys() - confirm_items.keys()):
                unestablished[key] = ({"component_id": key}, f"assessed in neither {a} nor {c}")
    # A covered duty entry that is the assessor's own extra scope check (keyed "X-", or any duty when
    # the row records none) was not owed by the other assessor. A non-covered one stays (a dissent
    # downgrades on one vote).
    no_recorded = not row.obj.get("missing_pieces") and not row.obj.get("unassessed_scope")
    for key in [k for k, (obj, _) in unestablished.items()
                if k.startswith("duty:") and obj.get("verdict") == "covered"
                and (no_recorded or k.startswith("duty:x-"))]:
        del unestablished[key]
    proposal: dict[str, Any] = {"section_id": section_id, "original_row_sha256": row.row_sha256}
    status = sec.get("status")
    au_problems = (au_input_problems(root, row, evidence, [(a, first), (c, confirm)], reached)
                   if status == "authored_unreviewed" and problem is None and evidence else [])
    if (
        status == "authored_unreviewed"
        and not sec.get("gaps")
        and not sec.get("blocked")
        and problem is None
        and evidence
        and not unestablished
        and not au_problems
        and all_covered(first)
        and all_covered(confirm)
    ):
        for entry in evidence:
            entry["assessment_ids"] = [a, c]
        proposal["set"] = {"status": "authored_unreviewed", "missing_pieces": [], "unassessed_scope": []}
        proposal["append_reader_evidence"] = evidence
        proposal["assessment_ids"] = [a, c]
        proposal["reason"] = fix_fused(f"wave {wave} packet {packet_id}")
        return proposal

    downgraded = status == "authored_unreviewed"
    if status not in OPEN_STATUSES:
        if not downgraded:
            raise WaveError(f"result status {status!r} is not authored_unreviewed, partial or missing")
        warnings.append(f"{section_id}: result status authored_unreviewed downgraded to partial")
        status = "partial"
    facet_units = [f.get("unit_id") for f in row.obj.get("source_facets") or [] if isinstance(f, dict)]
    open_comps = [obj for key, obj in first_items.items()
                  if not key.startswith("duty:") and key not in flawed and obj.get("verdict") != "covered"]
    disputed = [obj for key, (obj, _) in unestablished.items() if not key.startswith("duty:")]

    def item(duty: str, comps: list[dict[str, Any]], kind: str) -> dict[str, Any]:
        kind = SECTION_KIND.get(kind, kind)
        ids = [str(comp["component_id"]) for comp in comps]
        ref = None
        if kind.startswith("blocked_"):
            ref = resolve_ref(kind, comps, facet_units, section_id, blockers, duty)
            if ref is None:
                own = sorted({str(comp["blocker"].get("ref")) for comp in comps
                              if isinstance(comp.get("blocker"), dict) and comp["blocker"].get("ref")})
                raise WaveError(
                    f"{kind} item for {ids} has no ACQ-/MATH-/POL- record in acquisition-requests.jsonl or "
                    f"blockers.jsonl (assessment refs: {own or 'none'}); ledger_patch refuses a blocked kind without one"
                )
        return {"duty": fix_fused(duty), "component_ids": ids, "kind": kind, "blocker_ref": ref,
                "since": _since(row.obj, kind, ids, wave)}

    items: list[dict[str, Any]] = []
    for gap in sec.get("gaps") or []:
        gap = str(gap)
        if gap.casefold().startswith(DISPUTE + ":"):  # the workflow's failed-confirmation gaps
            items.append(item(gap, match_gap(gap, disputed) if disputed else [], DISPUTE))
        else:
            items.append(item(gap, match_gap(gap, open_comps), "writable"))  # section 11: open gaps are writable
    for blocked in sec.get("blocked") or []:
        kind = normalize_kind(blocked.get("kind") if isinstance(blocked, dict) else None)
        comps = [comp for comp in open_comps if component_kind(comp) == kind] or open_comps
        detail = (blocked.get("detail") or blocked.get("kind")) if isinstance(blocked, dict) else blocked
        items.append(item(str(detail), comps, kind))
    for key, why in flawed.items():
        if key.startswith("duty:"):
            duty = (first_items.get(key) or confirm_items.get(key) or {}).get("duty") or key.removeprefix("duty:")
            items.append(item(f"Duty not established ({why}): {duty}", [], DISPUTE))
        else:
            items.append(item(f"{key}: not established ({why})", [{"component_id": key}], DISPUTE))
    for text in malformed:
        items.append(item(f"Assessment entry not established: {text}", [], DISPUTE))
    accounted = {cid for it in items for cid in it["component_ids"]}
    if downgraded:
        for text in au_problems:
            items.append(item(f"Authored-unreviewed upgrade not established: {text}", [], DISPUTE))
        for key, (obj, why) in unestablished.items():
            if key.startswith("duty:"):
                items.append(item(f"Duty not established ({why}): {obj.get('duty')}", [], DISPUTE))
            elif key not in accounted:
                items.append(item(f"{key}: covered in {a} but not established: {why}", [obj], DISPUTE))
        for key, obj in first_items.items():  # duties a does not cover
            if key.startswith("duty:") and key not in flawed and obj.get("verdict") != "covered":
                items.append(item(f"Duty {obj.get('verdict')} in {a}: {obj.get('gap') or obj.get('duty')}",
                                  [], component_kind(obj)))
    for comp in open_comps:  # every open component of a lands in some missing piece
        if comp["component_id"] not in accounted:
            items.append(item(str(comp.get("gap") or comp["component_id"]), [comp], component_kind(comp)))
    if not items:
        raise WaveError(f"status {status} but no gap, blocked item or open component to record")
    proposal["set"] = {"status": status, "missing_pieces": items, "unassessed_scope": []}
    proposal["append_reader_evidence"] = evidence
    proposal["assessment_ids"] = [a]
    proposal["reason"] = fix_fused(f"wave {wave} packet {packet_id}")
    return proposal


# ---------------------------------------------------------------- units

RANK = {"covered": 0, "covered_unconfirmed": 1}  # any open kind ranks 2


def load_residuals(root: Path) -> dict[tuple[str, str], dict[str, Any]]:
    path = root / lp.RESIDUALS_PATH
    latest: dict[tuple[str, str], dict[str, Any]] = {}
    if path.is_file():
        with path.open("r", encoding="utf-8-sig") as handle:
            for line in handle:
                if line.strip():
                    rec = json.loads(line)
                    latest[(rec.get("unit_id"), rec.get("component_id"))] = rec
    return latest


def unit_residuals(
    wave: str,
    unit: dict[str, Any],
    assessments: dict[str, dict[str, Any]],
    blockers: list[dict[str, Any]],
    previous: dict[tuple[str, str], dict[str, Any]],
    warnings: list[str],
) -> list[dict[str, Any]]:
    unit_id = unit["unit_id"]
    first_id, confirm_id = unit.get("assessment_id"), unit.get("confirm_assessment_id")
    first = _need(assessments, first_id, wave)
    confirm = _need(assessments, confirm_id, wave) if confirm_id else None
    for data in (first, confirm):
        if data is not None and data.get("unit_id") != unit_id:
            raise WaveError(f"assessment {data.get('assessment_id')} is for unit {data.get('unit_id')!r}, not {unit_id}")
    if not _components(first):
        raise WaveError(f"assessment {first_id} has no components")
    problem = confirm_problem(first_id, first, confirm_id, confirm)
    if confirm_id and problem:
        warnings.append(f"unit {unit_id}: confirm {confirm_id} not used: {problem}")
    first_items = audit(first)[0]
    confirm_items = audit(confirm)[0] if confirm is not None and confirm_id != first_id else {}
    ids = [first_id] + ([confirm_id] if problem is None else [])
    # Components only the confirm file assesses: at most covered_unconfirmed (a never covered them).
    entries = [(comp, ids, problem is None and confirm_items.get(key, {}).get("verdict") == "covered")
               for key, comp in first_items.items() if not key.startswith("duty:")]
    entries += [(comp, [confirm_id], False) for key, comp in confirm_items.items()
                if not key.startswith("duty:") and key not in first_items]
    records = []
    for comp, comp_ids, confirmed in entries:
        cid = comp.get("component_id")
        if comp.get("verdict") == "covered":
            kind = "covered" if confirmed else "covered_unconfirmed"
            records.append({"unit_id": unit_id, "component_id": cid, "kind": kind, "assessment_ids": comp_ids,
                            "evidence": comp.get("evidence") or [], "wave": wave})
            continue
        kind = component_kind(comp)
        prior = previous.get((unit_id, cid))
        since = prior.get("since") if prior and prior.get("kind") == kind and prior.get("since") else wave
        ref = resolve_ref(kind, [comp], [unit_id], None, blockers) if kind.startswith("blocked_") else None
        records.append({"unit_id": unit_id, "component_id": cid, "kind": kind,
                        "duty": fix_fused(str(comp.get("gap") or cid)),
                        "blocker_ref": ref, "assessment_ids": comp_ids, "wave": wave, "since": since})
    return records


# ---------------------------------------------------------------- driver


def build(root: Path, wave: str, results_doc: Any) -> tuple[list[dict], list[dict], list[str], list[str]]:
    """-> (proposals, new residual records, warnings, errors)."""
    doc = results_doc.get("result", results_doc) if isinstance(results_doc, dict) else None
    if not isinstance(doc, dict) or not isinstance(doc.get("results"), list):
        raise WaveError("results file has no results list")
    if doc.get("wave") not in (None, wave):
        raise WaveError(f"results file is for wave {doc.get('wave')!r}, not {wave}")
    assessments = load_assessments(root, wave)
    blockers = load_blockers(root)
    ledger = lp.load_ledger(root)
    previous = load_residuals(root)
    reached = lp._handbook_reached_files(root)
    proposals: list[dict] = []
    merged: dict[tuple[str, str], dict] = {}
    warnings: list[str] = []
    errors: list[str] = []
    seen_sections: dict[str, str] = {}
    for result in doc["results"]:
        packet_id = str(result.get("id"))
        for sec in result.get("sections") or []:
            section_id = str(sec.get("section_id"))
            try:
                if section_id in seen_sections:
                    raise WaveError(f"also reported by packet {seen_sections[section_id]}")
                seen_sections[section_id] = packet_id
                row = ledger.by_section.get(section_id)
                if row is None:
                    raise WaveError("section not in ledger")
                proposals.append(
                    section_proposal(root, wave, packet_id, sec, row, assessments, blockers, warnings, reached)
                )
            except WaveError as exc:
                errors.append(f"{packet_id} section {section_id}: {exc}")
        for unit in result.get("units") or []:
            try:
                for rec in unit_residuals(wave, unit, assessments, blockers, previous, warnings):
                    key = (rec["unit_id"], rec["component_id"])
                    old = merged.get(key)
                    # Within one run the more conservative record wins; ties go to the later packet.
                    if old is None or RANK.get(rec["kind"], 2) >= RANK.get(old["kind"], 2):
                        merged[key] = rec
            except WaveError as exc:
                errors.append(f"{packet_id} unit {unit.get('unit_id')}: {exc}")
    new_records = [rec for key, rec in merged.items() if previous.get(key) != rec]
    return proposals, new_records, warnings, errors


def write_outputs(root: Path, wave: str, proposals: list[dict], records: list[dict], out_dir: Path | None = None) -> tuple[Path, Path]:
    """Real targets when out_dir is None (--apply); otherwise preview copies under out_dir."""
    if out_dir is None:
        proposals_path = root / "work" / "waves" / wave / "proposals.jsonl"
        residuals_path = root / lp.RESIDUALS_PATH
        existing = residuals_path.read_text(encoding="utf-8-sig") if residuals_path.is_file() else ""
    else:
        proposals_path = out_dir / "proposals.jsonl"
        residuals_path = out_dir / "unit-residuals.new.jsonl"
        existing = ""
    if existing and not existing.endswith("\n"):
        existing += "\n"
    for path in (proposals_path, residuals_path):
        path.parent.mkdir(parents=True, exist_ok=True)
    lp._write_atomic_text(proposals_path, "".join(_jdump(p) + "\n" for p in proposals))
    lp._write_atomic_text(residuals_path, existing + "".join(_jdump(r) + "\n" for r in records))
    return proposals_path, residuals_path


def summarize(root: Path, proposals: list[dict], records: list[dict], warnings: list[str], errors: list[str]) -> None:
    ledger = lp.load_ledger(root)
    print("section_id | old_status | new_status | evidence_entries | missing_pieces (kind:blocker_ref)")
    print("--- | --- | --- | --- | ---")
    for p in proposals:
        old = ledger.by_section[p["section_id"]].obj.get("status")
        pieces = ", ".join(f"{m['kind']}:{m['blocker_ref']}" for m in p["set"]["missing_pieces"]) or "-"
        print(f"{p['section_id']} | {old} | {p['set']['status']} | {len(p['append_reader_evidence'])} | {pieces}")
    counts: dict[str, int] = {}
    for rec in records:
        counts[rec["kind"]] = counts.get(rec["kind"], 0) + 1
    print(f"unit residual records to append: {len(records)} {json.dumps(counts, sort_keys=True)}")
    for line in warnings:
        print(f"warning: {line}")
    for line in errors:
        print(f"error: {line}", file=sys.stderr)


# ---------------------------------------------------------------- selftest


def _selftest() -> None:
    SCRATCH.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp_name:
        root = Path(tmp_name) / "repo"
        (Path(tmp_name) / "outside.tex").write_text("\\section{O}\\label{sec:o}\n", encoding="utf-8", newline="\n")

        def write(rel: str | Path, text: str) -> Path:
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8", newline="\n")
            return path

        write("handbook/main.tex", "\\input{parts/x}\n")
        body = write(
            "handbook/parts/x.tex",
            "\\section{X}\\label{sec:x}\nText.\n\\begin{hbtheorem}{thm:x}{proved}\nBody.\n"
            "More.\n\\end{hbtheorem}\n% \\label{sec:ghost}\n\\newcommand{\\mk}[1]{\\label{#1}}\nTail.\n",
        )
        write("handbook/parts/y.tex", "\\section{Y}\\label{sec:y}\nY body.\n")
        write("handbook/parts/nolabel.tex", "no labels here\nline2\n")
        orphan = write("handbook/parts/orphan.tex", "\\section{O}\\label{sec:orphan}\nNot input.\n")
        sha = lp._sha256_file(body)
        base_row = {"part": "P1", "chapter_id": "1", "chapter_title": "Ch", "reader_evidence": [],
                    "unassessed_scope": [], "observed_utc": "2026-01-01T00:00:00Z"}

        def row(section_id: str, units: list[str] | None = None, **extra: Any) -> dict:
            return dict(base_row, section_id=section_id, section_title="T", status="partial",
                        source_facets=[{"unit_id": u} for u in units or []], missing_pieces=["old"], **extra)

        extra_ids = ["2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9", "3.2", "3.3",
                     "4.2", "4.3", "4.4", "4.5", "4.6", "4.8", "5.1", "5.2"]
        rows = [
            row("1.1", ["U1"]),
            row("1.2", ["U2"]),
            row("1.3"),
            *[row(s) for s in extra_ids],
            row("3.1", ["U7"]),
            row("4.1", ["U2"]),
            dict(row("4.7"), status="authored_unreviewed", missing_pieces=[]),
        ]
        rows[1]["missing_pieces"] = [{"duty": "d", "component_ids": ["C4"], "kind": "blocked_source",
                                      "blocker_ref": "ACQ-T-2", "since": "w01"}]
        write(lp.LEDGER_DIR / "p01.jsonl", "".join(_jdump(r) + "\n" for r in rows))
        # Real acquisition records are keyed acq_id only.
        write(lp.ACQUISITION_PATH,
              _jdump({"acq_id": "ACQ-T-1", "units": ["U2", "U9"]}) + "\n"
              + _jdump({"acq_id": "ACQ-T-2", "units": ["U2"]}) + "\n")
        write(lp.BLOCKERS_PATH,
              _jdump({"id": "ACQ-T-9", "kind": "blocked_source", "units": ["U7"]}) + "\n"
              + _jdump({"id": "MATH-1", "kind": "blocked_math"}) + "\n"
              + _jdump({"id": "POL-1", "kind": "blocked_policy", "sections": ["3.1"]}) + "\n")

        def assessment(aid: str, role: str, ctx: str, comps: list, **extra: Any) -> None:
            data = {"schema": "coverage-assessment/1", "assessment_id": aid,
                    "assessor": {"family": "anthropic", "model": "opus", "role": role, "context_id": ctx},
                    "inputs": {"tex": [{"path": "handbook/parts/x.tex", "sha256": sha}]},
                    "components": comps, "duties": [], **extra}
            write(lp.ASSESSMENTS_DIR / "w99" / f"{aid}.json", json.dumps(data))

        def cov(cid: str, start: int, end: int, label: str, path: str = "handbook/parts/x.tex") -> dict:
            return {"component_id": cid, "verdict": "covered", "gap": "", "blocker": None,
                    "evidence": [{"path": path, "line_start": start, "line_end": end, "label": label}]}

        def pair(sid: str, first: list, confirm: list | None, role_c: str = "confirm", ctx_c: str = "c",
                 role_a: str = "first", **extra: Any) -> None:
            assessment(f"CA-{sid}a", role_a, f"a-{sid}", first, section_id=sid, **extra)
            if confirm is not None:
                assessment(f"CA-{sid}c", role_c, f"{ctx_c}-{sid}", confirm, section_id=sid, **extra)

        def au_sec(sid: str, c: str | None = None) -> dict:
            return {"section_id": sid, "status": "authored_unreviewed", "gaps": [], "blocked": [],
                    "a": f"CA-{sid}a", "c": c if c is not None else f"CA-{sid}c"}

        blocked_c4 = {"component_id": "C4", "verdict": "blocked_source", "gap": "Supply the proof of C4.",
                      "blocker": {"kind": "source_not_held", "ref": "book"}, "evidence": []}
        assessment("CA-a11", "first", "ctx-1", [cov("C1", 1, 2, "within sec:ghost and sec:x;"),
                                               cov("C2", 3, 5, "\\label{thm:x}")], section_id="1.1")
        assessment("CA-c11", "confirm", "ctx-2", [cov("C1", 1, 2, "sec:x"), cov("C2", 3, 5, "thm:x")],
                   section_id="1.1")
        assessment("CA-a12", "first", "ctx-3", [cov("C3", 5, 5, "no label here"), blocked_c4,
                                               {"component_id": "C5", "verdict": "partial",
                                                "gap": "State lemma five around1115.", "evidence": []},
                                               cov("C9", 1, 1, "x", "handbook/missing.tex")],
                   section_id="1.2")
        assessment("CA-a13", "first", "ctx-4", [cov("C6", 1, 1, "sec:x")], section_id="1.3")
        # F1 c == a; F2 confirm with role first; F8 roles swapped; F2b same context.
        pair("2.1", [cov("C1", 1, 2, "sec:x")], None)
        pair("2.2", [cov("C1", 1, 2, "sec:x")], [cov("C1", 1, 2, "sec:x")], role_c="first")
        pair("2.3", [cov("C1", 1, 2, "sec:x")], [cov("C1", 1, 2, "sec:x")], role_a="confirm", role_c="first")
        pair("2.4", [cov("C1", 1, 2, "sec:x")], [cov("C1", 1, 2, "sec:x")], ctx_c="a")
        # F3 confirm covers a subset, C2's evidence unanchorable; F3b subset with usable evidence.
        pair("2.5", [cov("C1", 1, 2, "sec:x"), cov("C2", 1, 2, "z", "handbook/parts/nolabel.tex")],
             [cov("C1", 1, 2, "sec:x")])
        pair("2.6", [cov("C1", 1, 2, "sec:x"), cov("C2", 3, 5, "thm:x")], [cov("C1", 1, 2, "sec:x")])
        # F3c both cover C1, C2 but C2 has no usable evidence; F5 range past EOF; F5b line 0.
        pair("2.7", [cov("C1", 1, 2, "sec:x"), cov("C2", 1, 2, "z", "handbook/parts/nolabel.tex")],
             [cov("C1", 1, 2, "sec:x"), cov("C2", 1, 2, "z")])
        pair("2.8", [cov("C1", 1, 500, "sec:x"), cov("C2", 0, 0, "sec:y", "handbook/parts/y.tex"),
                     cov("C3", 3, 4, "thm:x")],
             [cov("C1", 1, 2, "sec:x"), cov("C2", 1, 1, "sec:y"), cov("C3", 3, 4, "thm:x")])
        # F4c: the nearest label before line 9 is the macro parameter #1, which is not a label.
        pair("2.9", [cov("C1", 9, 9, "tail")], [cov("C1", 9, 9, "tail")])
        # A7 / A7b: partial result, or AU result with a gap, while a and c both cover C1 -> never AU.
        pair("4.1", [cov("C1", 1, 2, "sec:x")], [cov("C1", 1, 2, "sec:x")])
        pair("4.8", [cov("C1", 1, 2, "sec:x")], [cov("C1", 1, 2, "sec:x")])
        # A4 / A5: C1 listed twice with conflicting verdicts in a, in c; A13 the same on an AU row.
        pair("4.2", [{"component_id": "C1", "verdict": "partial", "gap": "g"}, cov("C1", 1, 2, "sec:x")],
             [cov("C1", 1, 2, "sec:x")])
        pair("4.3", [cov("C1", 1, 2, "sec:x"), cov("C2", 3, 5, "thm:x")],
             [cov("C1", 1, 2, "sec:x"), {"component_id": "C1", "verdict": "partial", "gap": "g"}, cov("C2", 3, 5, "thm:x")])
        pair("4.7", [cov("C1", 1, 2, "sec:x")], [cov("C1", 1, 2, "sec:x"), {"component_id": "C1", "verdict": "partial"}])
        # A6: two duties with the same text, one partial; A10: a string component entry.
        duty_ok = {"duty": "Prove it.", "verdict": "covered"}
        assessment("CA-4.4a", "first", "a-4.4", [cov("C1", 1, 2, "sec:x")], section_id="4.4",
                   duties=[duty_ok, {"duty": "prove  it.", "verdict": "partial"}])
        assessment("CA-4.4c", "confirm", "c-4.4", [cov("C1", 1, 2, "sec:x")], section_id="4.4", duties=[duty_ok])
        pair("4.5", [cov("C1", 1, 2, "sec:x"), "C9"], [cov("C1", 1, 2, "sec:x")])
        # A11: evidence outside the repository root.
        pair("4.6", [cov("C1", 1, 2, "sec:x"), cov("C2", 1, 1, "sec:o", "../outside.tex")],
             [cov("C1", 1, 2, "sec:x"), cov("C2", 1, 1, "sec:o", "../outside.tex")])
        # R4: stale inputs.tex hash; R5: evidence only in a file the handbook never inputs.
        pair("5.1", [cov("C1", 1, 2, "sec:x")], [cov("C1", 1, 2, "sec:x")],
             inputs={"tex": [{"path": "handbook/parts/x.tex", "sha256": "0" * 64}]})
        pair("5.2", [cov("C1", 1, 1, "sec:orphan", "handbook/parts/orphan.tex")],
             [cov("C1", 1, 1, "sec:orphan", "handbook/parts/orphan.tex")],
             inputs={"tex": [{"path": "handbook/parts/orphan.tex", "sha256": lp._sha256_file(orphan)}]})
        # F6: every kind wave_proposals emits; refs from assessment, unit record, section record.
        assessment("CA-3.1a", "first", "a-3.1", [
            cov("C1", 1, 2, "sec:x"),
            {"component_id": "C2", "verdict": "blocked_math", "gap": "open problem",
             "blocker": {"kind": "blocked_math", "ref": "MATH-1"}},
            {"component_id": "C3", "verdict": "not_assessable", "gap": "no render"},
            {"component_id": "C4", "verdict": "blocked_source", "gap": "no book", "blocker": {"kind": "source_not_held"}},
            {"component_id": "C5", "verdict": "blocked_policy", "gap": "policy", "blocker": {"kind": "blocked_policy"}},
            {"component_id": "C6", "verdict": "partial", "gap": "write it"}], section_id="3.1")
        # F6b: blocked_math whose ref is on no record -> error; F6c not_assessable only.
        assessment("CA-3.2a", "first", "a-3.2", [{"component_id": "C2", "verdict": "blocked_math", "gap": "g",
                                                  "blocker": {"kind": "blocked_math", "ref": "MATH-404"}}],
                   section_id="3.2")
        assessment("CA-3.3a", "first", "a-3.3", [cov("C1", 1, 2, "sec:x"),
                                                {"component_id": "C3", "verdict": "not_assessable", "gap": "no render"}],
                   section_id="3.3")
        assessment("CA-u1", "first", "ctx-5", [cov("K1", 1, 1, "sec:x"),
                                              {"component_id": "K2", "verdict": "partial", "gap": "K2 gap"}],
                   unit_id="U1")
        assessment("CA-u1c", "confirm", "ctx-6", [cov("K1", 1, 1, "sec:x")], unit_id="U1")
        assessment("CA-u2", "first", "ctx-7", [cov("K3", 1, 1, "sec:x"), dict(blocked_c4, component_id="K4"),
                                              {"component_id": "K5", "verdict": "not_assessable", "gap": "no render"},
                                              {"component_id": "K6", "verdict": "blocked_math", "gap": "m",
                                               "blocker": {"kind": "blocked_math", "ref": "MATH-1"}}],
                   unit_id="U2")
        # F7: unit confirm == first; confirm with role first; same context; valid pair.
        assessment("CA-u3", "first", "x3", [cov("K7", 1, 1, "sec:x")], unit_id="U3")
        assessment("CA-u4", "first", "x4", [cov("K8", 1, 1, "sec:x")], unit_id="U4")
        assessment("CA-u4c", "first", "y4", [cov("K8", 1, 1, "sec:x")], unit_id="U4")
        assessment("CA-u5", "first", "x5", [cov("K9", 1, 1, "sec:x")], unit_id="U5")
        assessment("CA-u5c", "confirm", "X5", [cov("K9", 1, 1, "sec:x")], unit_id="U5")
        assessment("CA-u6", "first", "x6", [cov("K10", 1, 1, "sec:x")], unit_id="U6")
        assessment("CA-u6c", "confirm", "y6", [cov("K10", 1, 1, "sec:x"), cov("K11", 1, 1, "sec:x"),
                                              {"component_id": "K12", "verdict": "partial", "gap": "K12 gap"}],
                   unit_id="U6")
        results = {"result": {"wave": "w99", "results": [
            {"id": "w99-p01-001", "outcome": "accounted",
             "sections": [{"section_id": "1.1", "status": "authored_unreviewed", "gaps": [], "blocked": [],
                           "a": "CA-a11", "c": "CA-c11"},
                          {"section_id": "1.3", "status": "authored_unreviewed", "gaps": [], "blocked": [],
                           "a": "CA-a13"},
                          au_sec("2.1", c="CA-2.1a"), au_sec("2.2"), au_sec("2.3"), au_sec("2.4"),
                          au_sec("2.5"), au_sec("2.6"), au_sec("2.7"), au_sec("2.8"), au_sec("2.9"),
                          dict(au_sec("4.1"), status="partial", gaps=["Writer note: C1 proof still lacks case 3."],
                               blocked=[{"kind": "source_not_held", "detail": "book"}]),
                          dict(au_sec("4.8"), gaps=["C1 needs case 3."]),
                          au_sec("4.2"), au_sec("4.3"), au_sec("4.4"), au_sec("4.5"), au_sec("4.6"), au_sec("4.7"),
                          au_sec("5.1"), au_sec("5.2")],
             "units": [{"unit_id": "U1", "open_components": [], "assessment_id": "CA-u1",
                        "confirm_assessment_id": "CA-u1c"},
                       {"unit_id": "U3", "assessment_id": "CA-u3", "confirm_assessment_id": "CA-u3"},
                       {"unit_id": "U4", "assessment_id": "CA-u4", "confirm_assessment_id": "CA-u4c"},
                       {"unit_id": "U5", "assessment_id": "CA-u5", "confirm_assessment_id": "CA-u5c"},
                       {"unit_id": "U6", "assessment_id": "CA-u6", "confirm_assessment_id": "CA-u6c"}]},
            {"id": "w99-p01-002", "outcome": "carry_over",
             "sections": [{"section_id": "1.2", "status": "partial",
                           "gaps": ["C5: State lemma five.", "Duty: the proof of C4 is not supplied."],
                           "blocked": [{"kind": "source_not_held", "detail": "Book held since2020 only as contents"}],
                           "a": "CA-a12"},
                          {"section_id": "3.1", "status": "partial", "gaps": ["C6: write it"],
                           "blocked": [{"kind": "blocked_math", "detail": "m"}, {"kind": "not_assessable", "detail": "n"},
                                       {"kind": "source_not_held", "detail": "s"}, {"kind": "blocked_policy", "detail": "p"}],
                           "a": "CA-3.1a"},
                          {"section_id": "3.2", "status": "partial", "gaps": [], "blocked": [], "a": "CA-3.2a"},
                          {"section_id": "3.3", "status": "partial", "gaps": ["C3: no render"], "blocked": [],
                           "a": "CA-3.3a"}],
             "units": [{"unit_id": "U2", "open_components": [], "assessment_id": "CA-u2"}]},
        ]}}
        proposals, records, warnings, errors = build(root, "w99", results)
        assert len(errors) == 1 and "section 3.2" in errors[0] and "MATH-404" in errors[0], errors
        by_id = {p["section_id"]: p for p in proposals}
        assert set(by_id) == {"1.1", "1.2", "1.3", "3.1", "3.3", "4.1", "4.7", *extra_ids} - {"3.2"}, sorted(by_id)

        def ledger_ok(proposal: dict) -> None:
            props_file = write("tmp/p.jsonl", _jdump(proposal) + "\n")
            out = io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
                code = lp.apply_proposals(root, props_file, apply=False)
            assert code == 0, (proposal["section_id"], out.getvalue()[-600:])

        def pieces(sid: str) -> list[tuple[str, list[str], Any]]:
            return [(m["kind"], m["component_ids"], m["blocker_ref"]) for m in by_id[sid]["set"]["missing_pieces"]]

        au = by_id["1.1"]
        assert au["set"] == {"status": "authored_unreviewed", "missing_pieces": [], "unassessed_scope": []}, au
        assert au["assessment_ids"] == ["CA-a11", "CA-c11"]
        assert au["reason"] == "wave w99 packet w99-p01-001"
        assert au["original_row_sha256"] == lp.load_ledger(root).by_section["1.1"].row_sha256
        [ev] = au["append_reader_evidence"]
        assert ev["anchor"] == "sec:x" and (ev["line_start"], ev["line_end"]) == (1, 5), ev
        assert ev["components"] == ["C1", "C2"] and ev["assessment_ids"] == ["CA-a11", "CA-c11"], ev
        assert ev["read_extent"] == "coverage assessment CA-a11"
        ledger_ok(au)
        # 1.3: AU result without a confirm -> partial with a dispute piece for the unconfirmed component.
        assert by_id["1.3"]["set"]["status"] == "partial" and pieces("1.3") == [(DISPUTE, ["C6"], None)]
        assert "no confirm assessment" in by_id["1.3"]["set"]["missing_pieces"][0]["duty"]
        ledger_ok(by_id["1.3"])
        part = by_id["1.2"]
        assert part["set"]["status"] == "partial" and part["assessment_ids"] == ["CA-a12"], part
        [ev2] = part["append_reader_evidence"]  # missing.tex skipped, never invented
        assert ev2["anchor"] == "thm:x" and ev2["components"] == ["C3"], ev2  # nearest label at/before line 5
        assert ev2["assessment_ids"] == ["CA-a12"]
        assert any("missing.tex" in w for w in warnings), warnings
        gap5, gap4, blk = part["set"]["missing_pieces"]
        assert gap5["kind"] == "writable" and gap5["component_ids"] == ["C5"] and gap5["blocker_ref"] is None
        assert gap5["since"] == "w99"
        # Section 11: every open-gap piece is writable, even when it names a blocked component.
        assert gap4["kind"] == "writable" and gap4["component_ids"] == ["C4"] and gap4["blocker_ref"] is None, gap4
        assert blk["kind"] == "blocked_source" and blk["component_ids"] == ["C4"] and blk["blocker_ref"] == "ACQ-T-2"
        assert blk["since"] == "w01", blk  # acq_id-keyed record; since kept from the old row's piece
        assert blk["duty"] == "Book held since 2020 only as contents", blk  # fused number repaired
        ledger_ok(part)  # needs ledger_patch to resolve acq_id-keyed acquisition records
        # F1, F2, F8, same context: no independent confirm -> partial, every component disputed.
        for sid in ("2.1", "2.2", "2.3", "2.4"):
            assert by_id[sid]["set"]["status"] == "partial" and pieces(sid) == [(DISPUTE, ["C1"], None)], by_id[sid]
            assert by_id[sid]["assessment_ids"] == [f"CA-{sid}a"]
            assert by_id[sid]["append_reader_evidence"][0]["assessment_ids"] == [f"CA-{sid}a"]
            ledger_ok(by_id[sid])
        assert any("2.1: confirm CA-2.1a not used" in w for w in warnings), warnings
        # F3 / F3b: C2 not assessed by the confirm; F3c: C2 confirmed but unevidenced.
        for sid, why in (("2.5", "not assessed in confirm"), ("2.6", "not assessed in confirm"),
                         ("2.7", "no usable evidence entry")):
            assert pieces(sid) == [(DISPUTE, ["C2"], None)], (sid, by_id[sid])
            assert why in by_id[sid]["set"]["missing_pieces"][0]["duty"], by_id[sid]
            ledger_ok(by_id[sid])
        # F5 / F5b: out-of-file ranges skipped, so C1 and C2 lack evidence -> partial.
        assert pieces("2.8") == [(DISPUTE, ["C1"], None), (DISPUTE, ["C2"], None)], by_id["2.8"]
        [ev8] = by_id["2.8"]["append_reader_evidence"]
        assert (ev8["line_start"], ev8["line_end"], ev8["components"]) == (3, 4, ["C3"]), ev8
        assert any("lines 1-500 outside 1-9" in w for w in warnings) and any("lines 0-0" in w for w in warnings)
        ledger_ok(by_id["2.8"])
        # F4c: AU, anchored at thm:x, not at the macro parameter #1.
        assert by_id["2.9"]["set"]["status"] == "authored_unreviewed"
        assert by_id["2.9"]["append_reader_evidence"][0]["anchor"] == "thm:x"
        ledger_ok(by_id["2.9"])
        # F6: every emitted kind is one ledger_patch accepts, with a resolvable ref.
        assert pieces("3.1") == [("writable", ["C6"], None), ("blocked_math", ["C2"], "MATH-1"),
                                 (DISPUTE, ["C3"], None), ("blocked_source", ["C4"], "ACQ-T-9"),
                                 ("blocked_policy", ["C5"], "POL-1")], pieces("3.1")
        ledger_ok(by_id["3.1"])
        assert pieces("3.3") == [("writable", ["C3"], None)]  # F6c: a gap is writable (section 11)
        ledger_ok(by_id["3.3"])
        # A7: a partial result is never upgraded; its gap and blocked item are kept.
        assert by_id["4.1"]["set"]["status"] == "partial", by_id["4.1"]
        assert pieces("4.1") == [("writable", [], None), ("blocked_source", [], "ACQ-T-2")], pieces("4.1")
        assert by_id["4.1"]["assessment_ids"] == ["CA-4.1a"]
        ledger_ok(by_id["4.1"])
        assert by_id["4.8"]["set"]["status"] == "partial" and pieces("4.8") == [("writable", [], None)]
        ledger_ok(by_id["4.8"])
        # A4, A5, A13: conflicting duplicate verdicts -> assessment_dispute, never AU.
        for sid, aid in (("4.2", "CA-4.2a"), ("4.3", "CA-4.3c"), ("4.7", "CA-4.7c")):
            assert by_id[sid]["set"]["status"] == "partial" and pieces(sid) == [(DISPUTE, ["C1"], None)], by_id[sid]
            assert f"conflicting verdicts in {aid}" in by_id[sid]["set"]["missing_pieces"][0]["duty"], by_id[sid]
            assert all("C1" not in e["components"] for e in by_id[sid]["append_reader_evidence"]), by_id[sid]
            ledger_ok(by_id[sid])
        # A6: duplicate duty with a partial verdict; A10: non-object component entry.
        assert pieces("4.4") == [(DISPUTE, [], None)] and "conflicting verdicts in CA-4.4a" in by_id["4.4"]["set"]["missing_pieces"][0]["duty"]
        assert pieces("4.5") == [(DISPUTE, [], None)] and "is not an object" in by_id["4.5"]["set"]["missing_pieces"][0]["duty"]
        for sid in ("4.4", "4.5"):
            assert by_id[sid]["set"]["status"] == "partial", by_id[sid]
            ledger_ok(by_id[sid])
        # A11: the outside path is skipped, so C2 has no usable evidence.
        assert pieces("4.6") == [(DISPUTE, ["C2"], None)], by_id["4.6"]
        assert [e["path"] for e in by_id["4.6"]["append_reader_evidence"]] == ["handbook/parts/x.tex"]
        assert any("outside the repository" in w for w in warnings), warnings
        ledger_ok(by_id["4.6"])
        # R4 / R5: downgraded to partial with a dispute naming the stale input / off-route path.
        for sid, why in (("5.1", "CA-5.1a: input handbook/parts/x.tex hash is stale"),
                         ("5.2", "no evidence path is on the current recursive input route (handbook/parts/orphan.tex)")):
            assert by_id[sid]["set"]["status"] == "partial", by_id[sid]
            assert [(k, ids) for k, ids, _ in pieces(sid)][0] == (DISPUTE, []), pieces(sid)
            assert any(why in m["duty"] for m in by_id[sid]["set"]["missing_pieces"]), by_id[sid]
            ledger_ok(by_id[sid])
        kinds = {(r["unit_id"], r["component_id"]): r for r in records}
        assert kinds[("U1", "K1")]["kind"] == "covered" and kinds[("U1", "K1")]["assessment_ids"] == ["CA-u1", "CA-u1c"]
        assert kinds[("U1", "K2")]["kind"] == "writable" and kinds[("U1", "K2")]["duty"] == "K2 gap"
        assert kinds[("U2", "K3")]["kind"] == "covered_unconfirmed" and kinds[("U2", "K3")]["assessment_ids"] == ["CA-u2"]
        assert kinds[("U2", "K4")]["kind"] == "blocked_source" and kinds[("U2", "K4")]["blocker_ref"] == "ACQ-T-2"
        assert kinds[("U2", "K5")]["kind"] == "lead_owned" and kinds[("U2", "K5")]["blocker_ref"] is None
        assert kinds[("U2", "K6")]["kind"] == "blocked_math" and kinds[("U2", "K6")]["blocker_ref"] == "MATH-1"
        # F7: a unit is "covered" only with a valid, independent confirm.
        for uid, cid in (("U3", "K7"), ("U4", "K8"), ("U5", "K9")):
            assert kinds[(uid, cid)]["kind"] == "covered_unconfirmed", kinds[(uid, cid)]
            assert kinds[(uid, cid)]["assessment_ids"] == [f"CA-{uid.lower()}"], kinds[(uid, cid)]
        assert kinds[("U6", "K10")]["kind"] == "covered" and kinds[("U6", "K10")]["assessment_ids"] == ["CA-u6", "CA-u6c"]
        # Components only the confirm file assesses still get residual records.
        assert kinds[("U6", "K11")]["kind"] == "covered_unconfirmed" and kinds[("U6", "K11")]["assessment_ids"] == ["CA-u6c"]
        assert kinds[("U6", "K12")]["kind"] == "writable" and kinds[("U6", "K12")]["duty"] == "K12 gap"
        assert all(r["wave"] == "w99" for r in records) and len(records) == 12, len(records)
        # helpers
        assert fix_fused("between0 and1") == "between 0 and 1"
        assert match_gap("X-S-1..3: all", [{"component_id": f"X-S-{n}"} for n in range(1, 5)]) == [
            {"component_id": "X-S-1"}, {"component_id": "X-S-2"}, {"component_id": "X-S-3"}]
        assert [label for _, label in declared_labels(body.read_text(encoding="utf-8"))] == ["sec:x", "thm:x"]
        try:
            normalize_kind("mystery")
            raise AssertionError("unknown kind accepted")
        except WaveError:
            pass

        # --apply writes, and a rerun appends no duplicate residuals.
        proposals_path, residuals_path = write_outputs(root, "w99", proposals, records)
        assert proposals_path.read_text(encoding="utf-8").count("\n") == len(proposals)
        assert residuals_path.read_text(encoding="utf-8").count("\n") == 12
        _, again, _, _ = build(root, "w99", results)
        assert again == [], again
        # A later wave with a changed verdict appends a newer record (latest wins, history kept).
        assessment("CA-u2", "first", "ctx-7", [cov("K3", 1, 1, "sec:x"), cov("K4", 1, 1, "sec:x"),
                                              {"component_id": "K5", "verdict": "not_assessable", "gap": "no render"},
                                              {"component_id": "K6", "verdict": "blocked_math", "gap": "m",
                                               "blocker": {"kind": "blocked_math", "ref": "MATH-1"}}],
                   unit_id="U2")
        _, newer, _, _ = build(root, "w99", results)
        assert [(r["component_id"], r["kind"]) for r in newer] == [("K4", "covered_unconfirmed")], newer
    print("wave_proposals selftest: OK")


def main(argv: list[str] | None = None) -> int:
    lp._configure_stdio()
    parser = argparse.ArgumentParser(description="Turn wave results and assessments into ledger proposals and unit residuals.")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--wave", help="wave id such as w02")
    parser.add_argument("--results", help="workflow results JSON (work/waves/<wave>/results-<n>.json)")
    parser.add_argument("--apply", action="store_true", help="write proposals.jsonl and append unit residuals")
    parser.add_argument("--preview-dir", help="dry run only: also write the would-be outputs into this directory")
    args = parser.parse_args(argv)
    if args.selftest:
        _selftest()
        return 0
    if not args.wave or not args.results or not WAVE_RE.fullmatch(args.wave):
        parser.print_usage(sys.stderr)
        print("error: --wave wNN and --results FILE are required", file=sys.stderr)
        return 2
    if args.apply and args.preview_dir:
        print("error: --preview-dir is for dry runs only", file=sys.stderr)
        return 2
    try:
        proposals, records, warnings, errors = build(ROOT, args.wave, lp._read_json(Path(args.results)))
    except (WaveError, OSError, json.JSONDecodeError, lp.LedgerError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    summarize(ROOT, proposals, records, warnings, errors)
    if args.apply:
        if errors:
            print("refused: errors above; nothing written", file=sys.stderr)
            return 1
        paths = write_outputs(ROOT, args.wave, proposals, records)
        print(f"wrote {paths[0]} ({len(proposals)} proposals); appended {len(records)} records to {paths[1]}")
    elif args.preview_dir:
        paths = write_outputs(ROOT, args.wave, proposals, records, Path(args.preview_dir))
        print(f"dry run: preview written to {paths[0]} and {paths[1]}")
    else:
        print("dry run: no files written")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

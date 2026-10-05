"""Integrate wave author returns into handbook routes and canonical intakes."""
from __future__ import annotations

import argparse
from bisect import bisect_right
from collections import Counter
import contextlib
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from datetime import datetime, timezone

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "handbook"
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import check as grammar  # noqa: E402
import symbol_registry as registry  # noqa: E402
import symbols2tex  # noqa: E402


class Refusal(RuntimeError):
    """A checked refusal or finding; command exits 1."""


class UsageError(RuntimeError):
    """A command-line usage error; command exits 2."""


FIELDS = registry.HEADER
TEX_EXTENSIONS = {".aux", ".bbl", ".bcf", ".blg", ".fdb_latexmk", ".fls", ".idx",
                  ".ilg", ".ind", ".log", ".out", ".run.xml", ".synctex.gz", ".toc"}
PDF_OR_BUILD = {".pdf", ".djvu", ".epub"} | TEX_EXTENSIONS
NUMERIC_SCOPE_TOKEN_RE = re.compile(r"(?i)\bP[^A-Za-z0-9\s]?\s*\d{1,2}\s*\.\s*\d")
FORBIDDEN_REPO_PREFIXES = (
    "handbook/restoration/",
    "handbook/generated/",
    "citations/",
    "source/references/",
)
FORBIDDEN_REPO_FILES = {"source/formal-logic-reference.tex"}
TEXLIVE_BIN = Path("C:/texlive/2025/bin/windows")
# handbook.sty for the compile gate when the adopt base (a bare test tree) lacks one.
TOOL_HANDBOOK = Path(__file__).resolve().parents[1] / "handbook"


def is_build_artifact(name: str) -> bool:
    name = name.lower()
    return any(name.endswith(ext) for ext in PDF_OR_BUILD)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def read_log_text(path: Path) -> str:
    """TeX logs and .blg files carry raw font-encoding bytes (e.g. T1 0xf6)."""
    return path.read_bytes().decode("utf-8-sig", errors="replace")


def write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(text)
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def json_text(data: object) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def configure_stdout() -> None:
    reconfigure = getattr(sys.stdout, "reconfigure", None)
    if reconfigure is None:
        return
    try:
        reconfigure(encoding="utf-8", newline="\n")
    except (TypeError, ValueError):
        pass


def write_json_atomic(path: Path, data: object) -> None:
    write_text_atomic(path, json_text(data))


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def public(row: dict) -> dict:
    return {k: v for k, v in row.items() if not k.startswith("_")}


def row_tuple(row: dict) -> tuple[str, ...]:
    return tuple(row.get(k, "") for k in FIELDS)


def row_id(row: dict) -> str:
    return str(row.get("_uid", row.get("_line", "")))


def rel_posix(path: str | Path) -> str:
    return str(path).replace("\\", "/").strip()


def strip_handbook_prefix(rel: str) -> str:
    rel = rel_posix(rel)
    if rel.startswith("handbook/"):
        rel = rel[len("handbook/"):]
    return rel


def tex_rel(rel: str) -> str:
    rel = strip_handbook_prefix(rel)
    if rel.endswith(".tex"):
        return rel
    return rel + ".tex"


def input_arg(rel: str) -> str:
    rel = strip_handbook_prefix(rel)
    return rel[:-4] if rel.endswith(".tex") else rel


def handbook_file(base: Path, rel: str) -> Path:
    return resolve_handbook_path(base, rel, tex=True)[0]


def repo_file(rel: str) -> Path:
    rel = rel_posix(rel)
    raw = Path(rel)
    path = raw.resolve() if raw.is_absolute() else (ROOT / rel).resolve()
    root = ROOT.resolve()
    if not path.is_relative_to(root):
        raise Refusal(f"repository path outside root: {rel}")
    repo_rel = path.relative_to(root).as_posix()
    if forbidden_repo_path(repo_rel):
        raise Refusal(f"forbidden repository path: {repo_rel}")
    return path


def forbidden_repo_path(repo_rel: str) -> bool:
    repo_rel = rel_posix(repo_rel)
    return repo_rel in FORBIDDEN_REPO_FILES or any(
        repo_rel.startswith(prefix) for prefix in FORBIDDEN_REPO_PREFIXES
    )


def resolve_handbook_path(base: Path, rel: str, *, tex: bool = False,
                          allow_forbidden: bool = False) -> tuple[Path, str]:
    rel = tex_rel(rel) if tex else strip_handbook_prefix(rel_posix(rel))
    raw = Path(rel)
    if raw.is_absolute() or re.match(r"^[A-Za-z]:/", rel):
        raise Refusal(f"absolute handbook path refused: {rel}")
    base_resolved = base.resolve()
    path = (base / rel).resolve()
    if not path.is_relative_to(base_resolved):
        raise Refusal(f"handbook path outside base: {rel}")
    rel_norm = path.relative_to(base_resolved).as_posix()
    repo_rel = "handbook/" + rel_norm
    if not allow_forbidden and forbidden_repo_path(repo_rel):
        raise Refusal(f"forbidden handbook path: {repo_rel}")
    return path, rel_norm


def as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def load_json(path: Path) -> object:
    try:
        return json.loads(read_text(path))
    except OSError as exc:
        raise Refusal(f"unreadable JSON {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise Refusal(f"invalid JSON {path}: {exc}") from exc


def read_manifest(path: Path) -> tuple[dict, str]:
    """A manifest's parsed object and the exact text it was parsed from."""
    try:
        text = read_text(path)
    except OSError as exc:
        raise Refusal(f"unreadable JSON {path}: {exc}") from exc
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise Refusal(f"invalid JSON {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise Refusal(f"manifest {path} must be a JSON object")
    problems = manifest_shape_errors(data)
    if problems:
        raise Refusal(f"malformed manifest {path}: " + "; ".join(problems))
    return data, text


GROUP_LIST_FIELDS = ("bodies", "annexes", "rule_sheets", "symbol_intakes", "bibliography_intakes")
PLACEMENT_FIELDS = ("host", "after", "before", "input")
# A placement names its point by after (the \input line it follows), before (the line it
# precedes), or both (the point must satisfy both).
PLACEMENT_ANCHORS = ("after", "before")
# The packet insertion spelling of after / before (normalized_placement reads both).
PLACEMENT_KEYS = PLACEMENT_FIELDS + ("after_input", "before_input")


def is_string_list(value) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value)


def placement_shape_errors(value, where: str) -> list[str]:
    """Shape problems in a placement value: a placement object (or a list or object of
    them) with string host and input, at least one of after/before, and string
    supplement_of. Scalar members of a container object (a note, say) are ignored, as
    manifest_placements does; a null after or before counts as absent."""
    if value is None:
        return []
    if isinstance(value, list):
        return [p for i, item in enumerate(value) for p in placement_shape_errors(item, f"{where}[{i}]")]
    if not isinstance(value, dict):
        return [f"{where} must be a placement object or a list of them"]
    if not any(key in value for key in PLACEMENT_KEYS):
        return [p for key, item in value.items() if isinstance(item, (dict, list))
                for p in placement_shape_errors(item, f"{where}.{key}")]
    try:
        value = normalized_placement(value, where)
    except Refusal as exc:
        return [str(exc)]
    present = [key for key in PLACEMENT_FIELDS if key in value
               and not (key in PLACEMENT_ANCHORS and value[key] is None)]
    problems = [f"{where} lacks {key}" for key in ("host", "input") if key not in value]
    if not any(key in present for key in PLACEMENT_ANCHORS):
        problems.append(f"{where} lacks after or before")
    problems += [f"{where}.{key} must be a non-empty string" for key in present
                 if not isinstance(value[key], str) or not value[key].strip()]
    if value.get("supplement_of") is not None and not isinstance(value["supplement_of"], str):
        problems.append(f"{where}.supplement_of must be a string")
    return problems


def manifest_shape_errors(manifest: dict) -> list[str]:
    """Schema problems that would otherwise surface as crashes deep in a command."""
    problems = placement_shape_errors(manifest.get("placements"), "placements")
    if manifest.get("prior_manifest") is not None and not isinstance(manifest["prior_manifest"], str):
        problems.append("prior_manifest must be a string")
    groups = manifest.get("groups", [])
    if not isinstance(groups, list):
        return problems + ["groups must be a list of objects"]
    for i, group in enumerate(groups):
        where = f"groups[{i}]"
        if not isinstance(group, dict):
            problems.append(f"{where} must be an object")
            continue
        if not isinstance(group.get("stem"), str) or not group["stem"].strip():
            problems.append(f"{where}.stem must be a non-empty string")
        for key in ("integration_status", "part", "note"):
            if group.get(key) is not None and not isinstance(group[key], str):
                problems.append(f"{where}.{key} must be a string")
        for key in GROUP_LIST_FIELDS:
            if key in group and not is_string_list(group[key]):
                problems.append(f"{where}.{key} must be a list of strings")
        for key in ("placement", "placements"):
            problems += placement_shape_errors(group.get(key), f"{where}.{key}")
    return problems


DECISION_LIST_KEYS = ("row_edits", "drop_rows", "canonical_row_edits", "extend_scopes",
                      "overrides", "allow_shared_owned_files")


def decisions_shape_errors(decisions: dict) -> list[str]:
    """Schema problems in a decisions file that would otherwise crash adopt."""
    problems = [f"{key} must be a list" for key in DECISION_LIST_KEYS
                if key in decisions and not isinstance(decisions[key], list)]
    if problems:
        return problems
    for key in ("extend_scopes", "overrides"):
        for i, item in enumerate(decisions.get(key, [])):
            where = f"{key}[{i}]"
            if not isinstance(item, dict):
                problems.append(f"{where} must be an object")
                continue
            for name in ("scope", "name", "presentation"):
                if item.get(name) is not None and not isinstance(item[name], str):
                    problems.append(f"{where}.{name} must be a string")
            regions = item.get("regions", [])
            if not isinstance(regions, list) or not all(isinstance(r, dict) for r in regions):
                problems.append(f"{where}.regions must be a list of objects")
    if not is_string_list(decisions.get("allow_shared_owned_files", [])):
        problems.append("allow_shared_owned_files must be a list of strings")
    keep = decisions.get("bib_keep_canonical", {})
    if isinstance(keep, list) and not is_string_list(keep):
        problems.append("bib_keep_canonical list must hold strings")
    return problems


def refuse_changed_since_read(expected: dict[Path, str]) -> None:
    """Refuse when another writer changed a file after it was read; its edits would be lost."""
    changed = sorted(relative_output_path(path) for path, text in expected.items()
                     if not path.is_file() or read_text(path) != text)
    if changed:
        raise Refusal("files changed on disk since they were read: " + ", ".join(changed))


def pinned_reader_files() -> set[str]:
    """Handbook-relative files check.py pins byte-for-byte; no tool may edit them."""
    return set(grammar.HB_RETAINED_UNREACHABLE_READER_FILES)


def print_json(data: object) -> None:
    sys.stdout.write(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def contains_numeric_scope_token(scope: str) -> bool:
    return bool(NUMERIC_SCOPE_TOKEN_RE.search(scope or ""))


NUMERIC_SCOPE_FORM_RE = re.compile(r"P\d+(?:\.\d+)?(?:(?:-|TO)P\d+(?:\.\d+)?)?")
P_LOOKALIKES = str.maketrans({"Р": "P", "р": "p", "Ρ": "P", "ρ": "p"})


def numeric_scope_forbidden(scope: str) -> bool:
    """True for any legacy numeric scope however spelled (dashes, spacing, case, 'to',
    full-width forms, or any non-alphanumeric separator in place of the ordinal dot,
    so 'P1-3', 'P6–3', 'P6·3' and 'P1 3' are numeric too; a four-digit year as in
    'P8 1946 Brouwerian algebra' is not an ordinal). Invisible format characters
    (U+200B, U+2060, U+FEFF, ...), combining marks and Greek/Cyrillic look-alikes of P
    are ignored, and 'Part 6.3' counts as numeric."""
    scope = scope or ""
    if scope == "global":
        return False
    scope = "".join(ch for ch in unicodedata.normalize("NFKD", scope)
                    if unicodedata.category(ch) not in {"Cf", "Mn", "Me"})
    scope = scope.translate(P_LOOKALIKES)
    # Any non-alphanumeric run may also sit between P and the part ('P-6.3', 'P_6.3').
    if re.match(r"\s*P[^A-Za-z0-9]*\d+[^A-Za-z0-9]+\d{1,3}(?!\d)", scope, re.I):
        return True
    if re.match(r"\s*Parts?\s*\d+\s*[^\w\s‐-―−-]\s*\d", scope, re.I):
        return True
    normalized = scope
    normalized = re.sub("[‐-―−]", "-", normalized)  # hyphens, en/em dash, minus
    normalized = re.sub(r"\s+", "", normalized).upper()
    normalized = re.sub(r"(?<=\d)[,_/:](?=\d)", ".", normalized)
    normalized = re.sub(r"(?<![A-Z0-9])P[^A-Z0-9]+(?=\d)", "P", normalized)
    return bool(
        registry.parse_scope(scope)
        or registry.parse_scope(normalized.replace("TO", "-"))
        or NUMERIC_SCOPE_FORM_RE.fullmatch(normalized)
        or contains_numeric_scope_token(scope)
        or contains_numeric_scope_token(normalized)
    )


def numeric_row_errors(row: dict, existing_scope_names: set[str]) -> list[dict]:
    """Numeric scope / first_use errors shared by incoming rows and canonical edits."""
    errors: list[dict] = []
    where = {"group": row.get("_group", "canonical"), "intake": row.get("_intake"),
             "line": row.get("_line")}
    scope = row.get("scope", "")
    if scope not in existing_scope_names and numeric_scope_forbidden(scope):
        errors.append(dict(where, error="numeric scope forbidden", scope=scope))
    if registry.FIRST_RE.fullmatch(row.get("first_use", "")):
        errors.append(dict(where, error="numeric first_use forbidden", first_use=row["first_use"]))
    return errors


def strip_line_comment(line: str) -> str:
    out = []
    backslashes = 0
    for ch in line:
        if ch == "\\":
            backslashes += 1
            out.append(ch)
            continue
        if ch == "%" and backslashes % 2 == 0:
            break
        backslashes = 0
        out.append(ch)
    return "".join(out)


# Braced \input{x} / \include{x}, or the primitive braceless form `\input x`.
INPUT_RE = re.compile(
    r"\\(?:input|include)(?:\s*\{\s*([A-Za-z0-9_./-]+?)(?:\.tex)?\s*\}"
    r"|\s+([A-Za-z0-9_./-]+?)(?:\.tex)?(?![A-Za-z0-9_./-]))"
)
HEADING_COMMAND_RE = re.compile(r"\\(chapter|section|subsection)(?![A-Za-z@])\*?")
DISABLED_TOKEN_RE = re.compile(
    r"\\(iffalse|if[A-Za-z@]*|fi)(?![A-Za-z@])|\\(begin|end)\s*\{\s*comment\s*\}"
)


def blank_disabled(text: str) -> str:
    r"""Blank \iffalse...\fi and comment-environment spans, keeping newlines.

    Expects comment-stripped text. Inside \iffalse, nested conditionals are
    counted so their \fi does not end the skipped span early.
    """
    spans: list[tuple[int, int]] = []
    depth = 0
    start = 0
    in_comment_env = False
    for match in DISABLED_TOKEN_RE.finditer(text):
        word, env = match.group(1), match.group(2)
        if in_comment_env:
            if env == "end":
                spans.append((start, match.end()))
                in_comment_env = False
            continue
        if depth == 0:
            if word == "iffalse":
                depth, start = 1, match.start()
            elif env == "begin":
                in_comment_env, start = True, match.start()
            continue
        if word == "fi":
            depth -= 1
            if depth == 0:
                spans.append((start, match.end()))
        elif word and word != "ifthenelse":
            depth += 1
    if depth or in_comment_env:
        spans.append((start, len(text)))
    chars = list(text)
    for begin, end in spans:
        for i in range(begin, end):
            if chars[i] != "\n":
                chars[i] = " "
    return "".join(chars)


def active_tex(text: str) -> str:
    r"""Text TeX actually reads: comments, \verb/verbatim spans and disabled blocks blanked.

    Every offset and newline is kept, so line numbers and in-line offsets stay valid.
    """
    return blank_disabled(mask_inactive(text))


def iter_headings(text: str, regex: re.Pattern = HEADING_COMMAND_RE) -> list[tuple[int, str]]:
    r"""(offset, kind) of each heading command of regex (default \chapter/\section/\subsection)
    that has its mandatory '{'.

    The optional argument is scanned brace-aware, so [{a]b}] does not end early.
    """
    found: list[tuple[int, str]] = []
    for match in regex.finditer(text):
        cursor = match.end()
        while cursor < len(text) and text[cursor].isspace():
            cursor += 1
        if cursor < len(text) and text[cursor] == "[":
            cursor = delimited_end(text, cursor, "]")
            if cursor < 0:
                continue
            while cursor < len(text) and text[cursor].isspace():
                cursor += 1
        if cursor < len(text) and text[cursor] == "{":
            found.append((match.start(), match.group(1)))
    return found


DEFINITION_RE = re.compile(
    r"\\(?:(newcommand|renewcommand|providecommand|DeclareRobustCommand)\*?"
    r"|(NewDocumentCommand|RenewDocumentCommand|ProvideDocumentCommand|DeclareDocumentCommand)"
    r"|(def|gdef|edef|xdef))(?![A-Za-z@])"
)


def blank_definition_bodies(text: str) -> str:
    r"""Blank macro-definition bodies (\newcommand, \def, ...), keeping newlines.

    A \section inside a definition body is not typeset where it is written, so it is
    not a file's first heading. An unparseable definition is refused.
    """
    chars = list(text)
    done = 0
    for match in DEFINITION_RE.finditer(text):
        if match.start() < done:
            continue  # nested in a body already blanked
        cursor = match.end()
        while cursor < len(text) and text[cursor].isspace():
            cursor += 1
        if match.group(3):  # \def\name<parameter text>{body}
            body = text.find("{", cursor)
        else:
            if cursor < len(text) and text[cursor] == "{":
                _args, cursor = grammar.scan_braced_args(text, cursor, 1)
            else:
                name = re.compile(r"\\(?:[A-Za-z@]+|.)").match(text, cursor)
                cursor = name.end() if name else cursor
            if match.group(2):  # argument specification
                _args, cursor = grammar.scan_braced_args(text, cursor, 1)
            while True:  # [n] [default]
                while cursor < len(text) and text[cursor].isspace():
                    cursor += 1
                if cursor >= len(text) or text[cursor] != "[":
                    break
                cursor = delimited_end(text, cursor, "]")
                if cursor < 0:
                    break
            body = cursor
        if body < 0 or body >= len(text) or text[body] != "{":
            raise Refusal("cannot parse macro definition near offset " + str(match.start()))
        args, end = grammar.scan_braced_args(text, body, 1)
        if not args:
            raise Refusal("unbalanced macro definition body near offset " + str(match.start()))
        for i in range(body, end):
            if chars[i] != "\n":
                chars[i] = " "
        done = end
    return "".join(chars)


def input_target(match: re.Match) -> str:
    return tex_rel(match.group(1) or match.group(2))


def iter_inputs(text: str) -> list[str]:
    return [input_target(match) for match in INPUT_RE.finditer(active_tex(text))]


def normalized_input(base: Path, target: str) -> str | None:
    """Handbook-relative .tex path an input target names ('./a' and 'x/../a' give 'a.tex');
    None when it does not resolve inside the handbook."""
    try:
        return resolve_handbook_path(base, target, tex=True, allow_forbidden=True)[1]
    except Refusal:
        return None


def input_occurrences(base: Path, text: str, rel: str) -> list[tuple[int, re.Match]]:
    r"""(line index, match) of each \input in text whose target resolves to rel.

    Targets are compared after normalization, so every spelling of a path counts.
    """
    rel = normalized_input(base, rel)
    return [(number, match) for number, line in enumerate(text.split("\n"))
            for match in INPUT_RE.finditer(line)
            if match.group(0).startswith("\\input")
            and normalized_input(base, input_target(match)) == rel]


def handbook_text(base: Path, rel: str, virtual: dict[str, str] | None = None) -> str | None:
    """Text of a handbook file (virtual edits first); None when missing or unresolvable."""
    try:
        path, rel = resolve_handbook_path(base, rel, tex=True, allow_forbidden=True)
    except Refusal:
        return None
    if virtual and rel in virtual:
        return virtual[rel]
    return read_text(path) if path.is_file() else None


def first_heading_kind(base: Path, rel: str, virtual: dict[str, str] | None = None,
                       seen: set[str] | None = None) -> str | None:
    r"""First \chapter/\section/\subsection reached from rel, following static \input order."""
    seen = set() if seen is None else seen
    rel = normalized_input(base, rel) or tex_rel(rel)
    if rel in seen:
        return None
    seen.add(rel)
    text = handbook_text(base, rel, virtual)
    if text is None:
        return None
    text = blank_definition_bodies(active_tex(text))
    events = [(start, "heading", kind) for start, kind in iter_headings(text)]
    events += [(m.start(), "input", input_target(m)) for m in INPUT_RE.finditer(text)]
    for _pos, kind, value in sorted(events):
        if kind == "heading":
            return value
        found = first_heading_kind(base, value, virtual, seen)
        if found:
            return found
    return None


def closure_matches(base: Path, rel: str, regex: re.Pattern,
                    virtual: dict[str, str] | None = None, seen: set[str] | None = None) -> bool:
    """True when rel or any file it statically inputs matches regex in active text."""
    seen = set() if seen is None else seen
    rel = normalized_input(base, rel) or tex_rel(rel)
    if rel in seen:
        return False
    seen.add(rel)
    text = handbook_text(base, rel, virtual)
    if text is None:
        return False
    text = active_tex(text)
    return bool(regex.search(text)) or any(
        closure_matches(base, target, regex, virtual, seen)
        for target in (input_target(m) for m in INPUT_RE.finditer(text))
    )


def static_input_counts(base: Path, virtual: dict[str, str] | None = None,
                        start: str = "main.tex") -> tuple[dict[str, int], list[str]]:
    virtual = virtual or {}
    counts: dict[str, int] = {}
    errors: list[str] = []
    active: list[str] = []

    def read_rel(rel: str) -> str | None:
        try:
            path, rel = resolve_handbook_path(base, rel, tex=True, allow_forbidden=True)
        except Refusal as exc:
            errors.append(str(exc))
            return None
        if rel in virtual:
            return virtual[rel]
        if not path.is_file():
            errors.append("missing input target " + rel)
            return None
        return read_text(path)

    def visit(rel: str) -> None:
        # Keyed by the normalized path, so './a' and 'x/../a' count as 'a'.
        rel = normalized_input(base, rel) or tex_rel(rel)
        if rel in active:
            errors.append("cyclic input route: " + " -> ".join(active + [rel]))
            return
        text = read_rel(rel)
        if text is None:
            return
        active.append(rel)
        for target in iter_inputs(text):
            target = normalized_input(base, target) or target
            counts[target] = counts.get(target, 0) + 1
            visit(target)
        active.pop()

    visit(start)
    return counts, errors


def parse_hook_command(text: str, command_end: int,
                       is_add: bool) -> tuple[str, str, int] | None:
    r"""Return (hook, label, end offset) for an \AddToHook/\RemoveFromHook call."""
    args, cursor = grammar.scan_braced_args(text, command_end, 1)
    if not args:
        return None
    while cursor < len(text) and text[cursor].isspace():
        cursor += 1
    label = ""
    if cursor < len(text) and text[cursor] == "[":
        close = delimited_end(text, cursor, "]")
        if close < 0:
            return None
        label = strip_outer_braces(text[cursor + 1:close - 1])
        cursor = close
    if is_add:
        rest = cursor
        while rest < len(text) and text[rest].isspace():
            rest += 1
        if rest < len(text) and text[rest] == "{":
            code, end = grammar.scan_braced_args(text, rest, 1)
            if not code:
                return None
            cursor = end
    return strip_outer_braces(args[0]), label, cursor


def strip_outer_braces(value: str) -> str:
    """Strip whitespace and one level of enclosing braces, as ltcmd does for an argument."""
    value = value.strip()
    if value.startswith("{"):
        args, end = grammar.scan_braced_args(value, 0, 1)
        if args and end == len(value):
            return args[0].strip()
    return value


def normalized_hook_label(label: str) -> str:
    """At document level an omitted label and '.' both name the default label 'top-level'."""
    if label in {"", "."}:
        return "top-level"
    if label.startswith("./"):
        return "top-level/" + label[2:]
    return label


def hook_events(lines: list[str]) -> tuple[dict[tuple[str, str], list[tuple[int, int, int]]],
                                           dict[tuple[str, str], list[tuple[int, int]]],
                                           set[tuple[str, str]]]:
    r"""Map (hook, normalized label) to adds (offset, first line, last line) and removes
    (offset, line), plus the keys of deferred removes.

    Neither text is ever read as code when it is in a % comment, \verb or a
    verbatim-like/comment environment. Beyond that, an \AddToHook counts even inside
    \iffalse, while a \RemoveFromHook counts only in active text, so a disabled one
    never closes a bracket early. A \RemoveFromHook in a macro definition body runs
    wherever the macro is used, which is not known here: its key is returned as
    deferred instead. Offsets agree because every mask keeps every position.
    """
    adds: dict[tuple[str, str], list[tuple[int, int, int]]] = {}
    removes: dict[tuple[str, str], list[tuple[int, int]]] = {}
    deferred: set[tuple[str, str]] = set()
    text = mask_inactive("\n".join(lines))
    active = blank_disabled(text)
    if re.search(r"\\(?:PushDefaultHookLabel|PopDefaultHookLabel|SetDefaultHookLabel)(?![A-Za-z@])",
                 text):
        raise Refusal("host changes the default hook label; hook brackets cannot be paired")
    if re.search(r"\\csname\s*(?:AddToHook|RemoveFromHook)|\\hook_[A-Za-z_]+:", text):
        raise Refusal("host uses \\csname AddToHook/RemoveFromHook or expl3 \\hook_... code; "
                      "hook brackets cannot be paired")
    outside_definitions = blank_definition_bodies(active)
    starts = [0]
    starts.extend(match.end() for match in re.finditer("\n", text))

    def line_of(offset: int) -> int:
        return max(0, bisect_right(starts, offset) - 1)

    for match in re.finditer(r"\\(AddToHook|AddToHookWithArguments|RemoveFromHook)(?![A-Za-z@])",
                             text):
        is_add = match.group(1) != "RemoveFromHook"
        if not is_add and active[match.start()] != "\\":
            continue  # a disabled \RemoveFromHook: TeX never runs it
        parsed = parse_hook_command(text if is_add else active, match.end(), is_add)
        if parsed is None:
            raise Refusal(
                "cannot parse \\" + match.group(1) + " hook command near line "
                + str(line_of(match.start()) + 1)
            )
        hook, label, end = parsed
        key = (hook, normalized_hook_label(label))
        if is_add:
            adds.setdefault(key, []).append(
                (match.start(), line_of(match.start()), line_of(max(match.start(), end - 1)))
            )
        elif outside_definitions[match.start()] != "\\":
            deferred.add(key)
        else:
            removes.setdefault(key, []).append((match.start(), line_of(match.start())))
    return adds, removes, deferred


def insertion_inside_hook(lines: list[str], insert_index: int) -> bool:
    r"""True when a line inserted before lines[insert_index] lands inside a hook bracket.

    A bracket runs from an \AddToHook to the end of its code argument and, when
    a later matching \RemoveFromHook exists (same label, or label '*'), on to it.
    With no such remove but a matching remove in a macro definition body (run at an
    unknown later point), it runs to the end of the host.
    """
    adds, removes, deferred = hook_events(lines)
    for key, add_events in adds.items():
        hook, _label = key
        remaining = sorted(removes.get(key, []) + removes.get((hook, "*"), []))
        for offset, start, last in sorted(add_events):
            end = last
            later = [item for item in remaining if item[0] > offset]
            if later:
                remaining.remove(later[0])
                end = max(end, later[0][1])
            elif key in deferred or (hook, "*") in deferred:
                end = len(lines)
            if start < insert_index <= end:
                return True
    return False


def hook_next_consumer_regex(hook: str) -> re.Pattern | None:
    r"""The command that fires a one-shot cmd/NAME/... or env/NAME/... hook."""
    match = re.fullmatch(r"cmd/([A-Za-z@]+)/(?:before|after)", hook)
    if match:
        return re.compile(r"\\" + re.escape(match.group(1)) + r"(?![A-Za-z@])")
    match = re.fullmatch(r"env/([A-Za-z@*]+)/(begin|end|before|after)", hook)
    if match:
        verb = "begin" if match.group(2) in {"begin", "before"} else "end"
        return re.compile(r"\\" + verb + r"\s*\{\s*" + re.escape(match.group(1)) + r"\s*\}")
    return None


def insertion_before_hook_next_consumer(lines: list[str], insert_index: int,
                                        base: Path | None = None,
                                        virtual: dict[str, str] | None = None) -> bool:
    r"""True when an insertion lands between an \AddToHookNext and the command it fires on.

    The consumer may sit in the host or in a file the host inputs (followed through
    the static \input closure when base is given). With no consumer found, or an
    unknown hook kind, the pending hook runs to the end of the host.
    """
    text = mask_inactive("\n".join(lines))
    active_lines = blank_disabled(text).split("\n")
    starts = [0]
    starts.extend(match.end() for match in re.finditer("\n", text))

    def line_of(offset: int) -> int:
        return max(0, bisect_right(starts, offset) - 1)

    # Like hook_events: the hook counts even inside \iffalse; its consumer only when active.
    for match in re.finditer(r"\\AddToHookNext(?![A-Za-z@])", text):
        parsed = parse_hook_command(text, match.end(), True)
        if parsed is None:
            raise Refusal("cannot parse \\AddToHookNext near line " + str(line_of(match.start()) + 1))
        hook, _label, end = parsed
        first = line_of(match.start())
        consumer = hook_next_consumer_regex(hook)
        stop = len(lines)
        if consumer is not None:
            for number in range(line_of(end), len(active_lines)):
                portion = active_lines[number]
                if number == line_of(end):
                    portion = portion[end - starts[number]:]
                if consumer.search(portion) or (base is not None and any(
                    closure_matches(base, input_target(m), consumer, virtual)
                    for m in INPUT_RE.finditer(portion)
                )):
                    stop = number
                    break
        if first < insert_index <= stop:
            return True
    return False


def iter_placements_in_value(value, stem: str | None = None) -> list[dict]:
    placements: list[dict] = []
    if value is None:
        return placements
    if isinstance(value, list):
        for item in value:
            placements.extend(iter_placements_in_value(item, stem))
        return placements
    if not isinstance(value, dict):
        return placements
    if any(key in value for key in PLACEMENT_KEYS):
        item = normalized_placement(value, "placement")
        if stem and "stem" not in item:
            item["stem"] = stem
        placements.append(item)
        return placements
    for nested in value.values():
        placements.extend(iter_placements_in_value(nested, stem))
    return placements


def manifest_placements(manifest: dict) -> list[dict]:
    placements: list[dict] = []
    placements.extend(iter_placements_in_value(manifest.get("placements")))
    for group in manifest.get("groups", []):
        stem = group.get("stem")
        placements.extend(iter_placements_in_value(group.get("placement"), stem))
        placements.extend(iter_placements_in_value(group.get("placements"), stem))
    return placements


TOC_LINE_RE = re.compile(r"^%%\s*toc:\s*P(\d+)\s+(\S+)\s+(\S+)", re.M)


def toc_order(base: Path, rel: str) -> tuple | None:
    """Reading-order key from the '%% toc: P<part> <chapter> <sections>' line a wave file
    opens with (its first section number when several are listed); None without one."""
    text = handbook_text(base, rel)
    match = TOC_LINE_RE.search("\n".join((text or "").split("\n")[:5]))
    if not match:
        return None

    def number(value: str) -> tuple:
        return tuple((0, int(x)) if x.isdigit() else (1, x) for x in value.split("."))

    sections = [number(x) for x in match.group(3).split(",") if x]
    return (int(match.group(1)), number(match.group(2)), min(sections) if sections else ())


def placement_order(base: Path, placement: dict, index: int) -> tuple:
    """Order of placements that share one anchor: the input's toc line, then the packet
    id in its stem, then manifest order (a placement without a toc line sorts after)."""
    toc = toc_order(base, placement["input"])
    packet = PACKET_ID_RE.search(placement.get("stem") or "")
    packet_key = tuple(int(x) for x in re.findall(r"\d+", packet.group(0))) if packet else ()
    return ((0, toc) if toc else (1,), packet_key, index)


def placement_anchor(base: Path, placement: dict) -> tuple[str, str] | None:
    r"""('after', rel) or ('before', rel): the \input line a placement's sibling run hangs
    from (after when both are given); None when it names neither."""
    for side in PLACEMENT_ANCHORS:
        if placement.get(side):
            return side, resolve_handbook_path(base, placement[side], tex=True, allow_forbidden=True)[1]
    return None


def anchor_siblings(base: Path, placements: list[dict]) -> dict[tuple[str, str, str], dict[str, tuple]]:
    """(host, side, anchor) -> {input: order key} over every placement that names that anchor."""
    found: dict[tuple[str, str, str], dict[str, tuple]] = {}
    for index, placement in enumerate(placements):
        try:
            host = resolve_handbook_path(base, placement["host"], tex=True, allow_forbidden=True)[1]
            anchor = placement_anchor(base, placement)
            new = resolve_handbook_path(base, placement["input"], tex=True, allow_forbidden=True)[1]
        except (Refusal, KeyError, TypeError):
            continue
        if anchor is not None:
            found.setdefault((host, *anchor), {}).setdefault(new, placement_order(base, placement, index))
    return found


def placement_befores(base: Path, placements: list[dict]) -> dict[tuple[str, str], str]:
    """(host, input) -> the input it must precede, over every placement naming before."""
    found: dict[tuple[str, str], str] = {}
    for placement in placements:
        try:
            if placement.get("before"):
                host = resolve_handbook_path(base, placement["host"], tex=True, allow_forbidden=True)[1]
                new = resolve_handbook_path(base, placement["input"], tex=True, allow_forbidden=True)[1]
                found.setdefault((host, new), resolve_handbook_path(
                    base, placement["before"], tex=True, allow_forbidden=True)[1])
        except (Refusal, KeyError, TypeError):
            continue
    return found


def before_dependency_order(base: Path, placements: list[dict]) -> list[dict]:
    """placements, each one naming before after the placement (in this run) of that input,
    so the line it must precede is in the host when it is inserted; otherwise in order."""
    def rel_of(value) -> str | None:
        return normalized_input(base, value) if isinstance(value, str) and value else None

    index_of: dict[str, int] = {}
    for i, placement in enumerate(placements):
        rel = rel_of(placement.get("input"))
        if rel:
            index_of.setdefault(rel, i)
    order: list[int] = []
    pending = list(range(len(placements)))
    while pending:
        done = set(order)
        ready = [i for i in pending
                 if index_of.get(rel_of(placements[i].get("before")), i) in done | {i}]
        nxt = ready[0] if ready else pending[0]  # a cycle: in order; the missing line is refused
        order.append(nxt)
        pending.remove(nxt)
    return [placements[i] for i in order]


def sibling_line(base: Path, line: str, siblings: dict[str, tuple]) -> tuple[str, tuple] | None:
    r"""(input, order key) when an active line holds just one \input of a placement sharing
    the anchor (one the manifest places there) or of a wave file (it opens with a toc
    line, routed there by an earlier run of any manifest); else None."""
    match = INPUT_RE.fullmatch(line.strip())
    target = normalized_input(base, input_target(match)) if match else None
    if not target:
        return None
    key = siblings.get(target)
    if key is None:
        toc = toc_order(base, target)
        key = ((0, toc), (), sys.maxsize) if toc else None
    return (target, key) if key is not None else None


def sibling_run(base: Path, active_lines: list[str], anchor: int,
                siblings: dict[str, tuple], *, before: bool = False) -> list[tuple[int, str, tuple]]:
    r"""(line index, input, order key), in reading order, of the consecutive sibling lines
    (sibling_line) after the anchor line, or before it when before is set."""
    run: list[tuple[int, str, tuple]] = []
    numbers = range(anchor - 1, -1, -1) if before else range(anchor + 1, len(active_lines))
    for number in numbers:
        found = sibling_line(base, active_lines[number], siblings)
        if found is None:
            break
        run.append((number, *found))
    return run[::-1] if before else run


# Heading depth; \hbannexchapter opens a proof-annex chapter.
HEADING_DEPTH = {"part": -1, "chapter": 0, "hbannexchapter": 0, "section": 1, "subsection": 2}
LEVEL_COMMAND_RE = re.compile(r"\\(part|chapter|section|subsection|hbannexchapter)(?![A-Za-z@])\*?")


def heading_in_force(base: Path, host_rel: str, insert_index: int,
                     virtual: dict[str, str] | None = None, cache: dict | None = None) -> str | None:
    r"""The last \part/\chapter/\section/\subsection (or \hbannexchapter) typeset before
    line insert_index of host_rel, in static \input reading order from main.tex (from
    the host alone when main.tex does not reach it); None when there is none."""
    cache = {} if cache is None else cache
    virtual = virtual or {}

    def events(rel: str):
        if rel not in virtual and rel in cache:
            return cache[rel]
        text = handbook_text(base, rel, virtual)
        if text is None:
            return None
        text = blank_definition_bodies(active_tex(text))
        items = sorted([(pos, "heading", kind) for pos, kind in iter_headings(text, LEVEL_COMMAND_RE)]
                       + [(m.start(), "input", input_target(m)) for m in INPUT_RE.finditer(text)])
        if rel not in virtual:
            cache[rel] = (text, items)
        return text, items

    last: list[str | None] = [None]
    active: list[str] = []

    def visit(rel: str) -> bool:
        """Walk rel; True once the insertion point is reached."""
        rel = normalized_input(base, rel) or tex_rel(rel)
        found = None if rel in active else events(rel)
        if found is None:
            return False
        text, items = found
        limit = (sum(len(line) + 1 for line in text.split("\n")[:insert_index])
                 if rel == host_rel else None)
        active.append(rel)
        try:
            for pos, kind, value in items:
                if limit is not None and pos >= limit:
                    return True
                if kind == "heading":
                    last[0] = value
                elif visit(value):
                    return True
            return limit is not None
        finally:
            active.pop()

    if not visit("main.tex"):
        last[0] = None
        visit(host_rel)
    return last[0]


def heading_skip(new_heading: str | None, in_force: str | None) -> bool:
    r"""True when a file opening with new_heading would skip a level below in_force (a
    \subsection where a \chapter is in force, a \section right after a \part). A file
    without a heading continues what is in force; nothing in force accepts any level."""
    return bool(new_heading and in_force) and HEADING_DEPTH[new_heading] > HEADING_DEPTH[in_force] + 1


def simulate_route(base: Path, placements: list[dict], *, apply: bool,
                   also_write=None, siblings: list[dict] | None = None) -> dict:
    r"""Route placements into their hosts (dry run unless apply).

    A placement names the unique \input line it follows (after), the unique line it
    precedes (before), or both; with both, the point must satisfy both. Placements
    sharing an anchor keep reading order: a new \input goes into the run of sibling
    \input lines after the after-anchor (or before the before-anchor), routed earlier
    in this run or an earlier one, before the first sibling that sorts after it
    (placement_order). A placement naming before is routed after the placement of that
    input in this run. siblings is every placement that may already be routed (default:
    placements).

    The new file's first heading may not skip a level below the heading in force at
    the insertion point (heading_skip), unless supplement_of is set.

    also_write is {path: (text read, new text)}, or a function of the post-route
    static input counts returning one; it is built and checked before any write.
    """
    virtual: dict[str, str] = {}
    originals: dict[Path, str] = {}
    writes: dict[Path, str] = {}
    actions: list[dict] = []
    errors: list[dict] = []
    requested_inputs: list[str] = []
    every_sibling = siblings if siblings is not None else placements
    shared = anchor_siblings(base, every_sibling)
    befores = placement_befores(base, every_sibling)
    touched_anchors: set[tuple[str, str, str]] = set()
    heading_cache: dict = {}

    for placement in before_dependency_order(base, placements):
        try:
            host_path, host_rel = resolve_handbook_path(base, placement["host"], tex=True)
            new_path, new_rel = resolve_handbook_path(base, placement["input"], tex=True)
            after_rel, before_rel = (
                resolve_handbook_path(base, placement[side], tex=True, allow_forbidden=True)[1]
                if placement.get(side) else None for side in PLACEMENT_ANCHORS)
        except Refusal as exc:
            errors.append({"placement": placement, "error": str(exc)})
            continue
        if after_rel is None and before_rel is None:
            errors.append({"placement": placement, "error": "placement names neither after nor before"})
            continue
        new_arg = input_arg(new_rel)
        requested_inputs.append(new_rel)
        if not host_path.is_file():
            errors.append({"placement": placement, "error": "host file missing"})
            continue
        if not new_path.is_file():
            errors.append({"placement": placement, "error": "input file missing"})
            continue
        pinned_reached = sorted(({new_rel} | set(static_input_counts(base, virtual, new_rel)[0]))
                                & pinned_reader_files())
        if pinned_reached:
            errors.append({"placement": placement, "pinned": pinned_reached,
                           "error": "input routes a check.py byte-pinned retained-unreachable "
                                    "file (HB_RETAINED_UNREACHABLE_READER_FILES); refused"})
            continue
        if host_path not in originals:
            originals[host_path] = read_text(host_path)
        text = virtual.get(host_rel, originals[host_path])
        # split("\n") everywhere: splitlines() also breaks at \f, \v, U+2028, ...,
        # which would shift line indices against active_tex and rewrite those characters.
        lines = text.split("\n")
        active_lines = active_tex(text).split("\n")
        # Occurrences, not lines: one line may carry several \input commands. Targets
        # are normalized, so './x' or 'y/../x' spellings of the path count too.
        existing = [i for i, _m in input_occurrences(base, "\n".join(active_lines), new_rel)]
        uncommented = "\n".join(strip_line_comment(line) for line in lines)
        disabled = sorted({i for i, _m in input_occurrences(base, uncommented, new_rel)
                           if i not in existing})
        if disabled:
            errors.append({"placement": placement, "host": host_rel,
                           "lines": [i + 1 for i in disabled],
                           "error": "input already present inside an \\iffalse, comment "
                                    "or verbatim block (not typeset); needs a decision"})
            continue
        if len(existing) > 1:
            errors.append({"placement": placement, "error": "input already occurs more than once"})
            continue
        if len(existing) == 1:
            actions.append({"placement": placement, "action": "noop-already-present",
                            "host": host_rel, "line": existing[0] + 1})
            virtual[host_rel] = text
            continue

        active_text = "\n".join(active_lines)
        blanked: list[str] = []

        def unique_line(rel: str, what: str) -> tuple[int | None, dict | None]:
            r"""The line of the one active \input of rel, or a refusal."""
            hits = input_occurrences(base, active_text, rel)
            if len(hits) != 1:
                return None, {"error": f"{what} occurs {len(hits)} times", "count": len(hits)}
            number, match = hits[0]
            # An anchor inside a \newcommand/\def body is typeset where the macro is used,
            # not at the line of the definition.
            if not blanked:
                blanked.append(blank_definition_bodies(active_text))
            offset = sum(len(item) + 1 for item in active_lines[:number]) + match.start()
            if blanked[0][offset] != "\\":
                return None, {"host": host_rel, "line": number + 1,
                              "error": f"{what} \\input lies inside a macro definition body; "
                                       "needs a decision"}
            return number, None

        try:
            anchor, problem = unique_line(after_rel, "anchor") if after_rel else (None, None)
            before_line, before_problem = (unique_line(before_rel, "before anchor")
                                           if before_rel else (None, None))
        except Refusal as exc:
            errors.append({"placement": placement, "error": str(exc)})
            continue
        if problem:
            errors.append({"placement": placement, **{k: v for k, v in problem.items() if k != "count"}})
            continue
        # With after, a before input not routed yet (placed at the same anchor, or an unrouted
        # wave file: another packet's new file) is an order among the siblings: kept here by
        # sort order, and when it is routed by the floor below.
        if before_problem and not (
                after_rel and before_problem.get("count") == 0
                and (before_rel in shared.get((host_rel, "after", after_rel), {})
                     or (toc_order(base, before_rel) is not None
                         and not static_input_counts(base, virtual)[0].get(before_rel)))):
            errors.append({"placement": placement,
                           **{k: v for k, v in before_problem.items() if k != "count"}})
            continue
        if host_rel in pinned_reader_files():
            errors.append({"placement": placement, "host": host_rel,
                           "error": "route host is a check.py byte-pinned retained file "
                                    "(HB_RETAINED_UNREACHABLE_READER_FILES); edit refused"})
            continue
        if anchor is not None:
            side_key = (host_rel, "after", after_rel)
            siblings_here = shared.get(side_key, {})
            mine = siblings_here.get(new_rel) or placement_order(base, placement, sys.maxsize)
            run = sibling_run(base, active_lines, anchor, siblings_here)
            insert_index = anchor + 1
            for number, _target, key in run:
                if key > mine:
                    break
                insert_index = number + 1
            if before_line is not None:
                # Only sibling inputs (the run after the anchor) may lie between the two.
                run_end = run[-1][0] + 1 if run else anchor + 1
                if not anchor < before_line <= run_end:
                    errors.append({"placement": placement, "host": host_rel,
                                   "after_line": anchor + 1, "before_line": before_line + 1,
                                   "error": "after and before name different insertion points"})
                    continue
                insert_index = min(insert_index, before_line)
        else:
            side_key = (host_rel, "before", before_rel)
            siblings_here = shared.get(side_key, {})
            mine = siblings_here.get(new_rel) or placement_order(base, placement, sys.maxsize)
            run = sibling_run(base, active_lines, before_line, siblings_here, before=True)
            insert_index = before_line
            for number, _target, key in run:
                if key > mine:
                    insert_index = number
                    break
        # A routed sibling whose before names this input stays before it.
        floor = max((number + 1 for number, target, _key in run
                     if befores.get((host_rel, target)) == new_rel), default=insert_index)
        if floor > insert_index:
            if before_line is not None and floor > before_line:
                errors.append({"placement": placement, "host": host_rel,
                               "error": "a sibling that must precede this input lies after its "
                                        "before anchor"})
                continue
            insert_index = floor
        if run:
            touched_anchors.add(side_key)
        try:
            inside_hook = insertion_inside_hook(lines, insert_index)
            before_next_hook = insertion_before_hook_next_consumer(lines, insert_index, base, virtual)
        except Refusal as exc:
            errors.append({"placement": placement, "error": str(exc)})
            continue
        if inside_hook:
            errors.append({"placement": placement, "error": "insertion point is inside AddToHook bracket"})
            continue
        if before_next_hook:
            errors.append({"placement": placement,
                           "error": "insertion point lies between an \\AddToHookNext and the "
                                    "command it fires on; needs a decision"})
            continue
        if not placement.get("supplement_of"):
            try:
                new_heading = first_heading_kind(base, new_rel, virtual)
                in_force = heading_in_force(base, host_rel, insert_index, virtual, heading_cache)
            except Refusal as exc:
                errors.append({"placement": placement, "error": str(exc)})
                continue
            if heading_skip(new_heading, in_force):
                errors.append({"placement": placement, "host": host_rel,
                               "insert_line": insert_index + 1,
                               "error": "heading level skip: the input's first heading is more "
                                        "than one level below the heading in force there",
                               "input_heading": new_heading, "heading_in_force": in_force})
                continue
        line = r"\input{" + new_arg + "}"
        new_text = "\n".join(lines[:insert_index] + [line] + lines[insert_index:])
        virtual[host_rel] = new_text
        writes[host_path] = new_text
        actions.append({"placement": placement, "action": "insert", "host": host_rel,
                        **({"after_line": anchor + 1} if anchor is not None else {}),
                        **({"before_line": before_line + 1} if before_line is not None else {}),
                        "insert_line": insert_index + 1, "line": line})

    counts: dict[str, int] = {}
    if not errors and requested_inputs:
        counts, closure_errors = static_input_counts(base, virtual)
        for err in closure_errors:
            errors.append({"error": err})
        for rel in requested_inputs:
            count = counts.get(rel, 0)
            if count != 1:
                errors.append({"input": rel, "error": f"route reaches input {count} times"})

    order_report = []
    for host_rel, side, anchor_rel in sorted(touched_anchors):
        text = virtual.get(host_rel)
        active_lines = active_tex(text).split("\n") if text is not None else []
        anchor = [i for i, _m in input_occurrences(base, "\n".join(active_lines), anchor_rel)]
        if len(anchor) == 1:
            order_report.append({"host": host_rel, side: anchor_rel, "inputs": [
                target for _n, target, _key in sibling_run(
                    base, active_lines, anchor[0], shared.get((host_rel, side, anchor_rel), {}),
                    before=side == "before")]})
    if errors:
        return {"ok": False, "errors": errors, "actions": actions, "dry_run": not apply,
                "shared_anchor_order": order_report}

    also_write = also_write(counts) if callable(also_write) else (also_write or {})
    if apply:
        # also_write (path -> (text read, new text)) is prepared and checked before any write.
        refuse_changed_since_read({**{path: originals[path] for path in writes},
                                   **{path: old for path, (old, _new) in also_write.items()}})
        for path, text in writes.items():
            write_text_atomic(path, text)
        for path, (_old, text) in also_write.items():
            write_text_atomic(path, text)
    return {"ok": True, "errors": [], "actions": actions, "dry_run": not apply,
            "shared_anchor_order": order_report,
            "writes": [p.relative_to(ROOT).as_posix() if p.is_relative_to(ROOT) else p.as_posix()
                       for p in writes]}


def count_annexitems(path: Path) -> int:
    if not path.is_file():
        return 0
    return len(re.findall(r"\\begin\s*\{\s*annexitem\s*\}", active_tex(read_text(path))))


def conventional_intakes(stem: str, kind: str) -> list[str]:
    prefix = "symbols-intake-" if kind == "symbol" else "intake-"
    suffix = ".csv" if kind == "symbol" else ".bib"
    folder = "registry" if kind == "symbol" else "bib"
    rel = f"{folder}/{prefix}{stem}{suffix}"
    return [rel] if (BASE / rel).is_file() else []


OWNED_KINDS = (("bodies", "parts/", ".tex"), ("annexes", "annex/", ".tex"),
               ("bibliography_intakes", "bib/", ".bib"), ("symbol_intakes", "registry/", ".csv"))
PACKET_ID_RE = re.compile(r"w\d{2}[a-z]?-p\d{2}-\d{3}(?:\.\d+)*")


def owned_kind(rel: str) -> str | None:
    """The group list a handbook file belongs in (repository paths need the handbook/ prefix)."""
    rel = rel_posix(rel)
    if not rel.startswith("handbook/"):
        return None
    rel = rel[len("handbook/"):]
    return next((kind for kind, folder, suffix in OWNED_KINDS
                 if rel.startswith(folder) and rel.endswith(suffix)), None)


def normalized_placement(value, where: str):
    """A return's placement with the packet insertion keys after_input / before_input read
    as after / before (a null one is absent)."""
    if isinstance(value, list):
        return [normalized_placement(item, f"{where}[{i}]") for i, item in enumerate(value)]
    if not isinstance(value, dict):
        return value
    if "host" not in value and "input" not in value:
        return {key: normalized_placement(item, f"{where}.{key}") for key, item in value.items()}
    item = dict(value)
    for key in PLACEMENT_ANCHORS:
        packet_value = item.pop(key + "_input", None)
        if packet_value is not None:
            if item.get(key) not in (None, packet_value):
                raise Refusal(f"{where}: {key} and {key}_input differ")
            item[key] = packet_value
        if key in item and item[key] is None:
            del item[key]
    return item


def packet_for_return(path: Path, data: dict, stem: str) -> dict:
    """The wave packet a return answers: the packet JSON the return names (a path or a
    packet id), else the one whose id ends the stem; {} when there is none."""
    ref = data.get("packet_path") or data.get("packet")
    if ref is not None and not isinstance(ref, str):
        raise Refusal(f"{path}: packet must be a string")
    if ref and ref.endswith(".json"):
        packet_path = repo_file(ref)
    else:
        match = PACKET_ID_RE.fullmatch(ref) if ref else PACKET_ID_RE.search(stem)
        if ref and not match:
            raise Refusal(f"{path}: packet {ref!r} is not a packet id or .json path")
        if not match:
            return {}
        packet_id = match.group(0)
        packet_path = ROOT / "work" / "waves" / packet_id.split("-")[0] / "packets" / f"{packet_id}.json"
    if not packet_path.is_file():
        # The return's own files_written still apply; an unowned placement input is refused.
        return {}
    packet = load_json(packet_path)
    if not isinstance(packet, dict):
        raise Refusal(f"{packet_path}: packet must be a JSON object")
    return packet


def group_from_return(path: Path, data: dict, report: list | None = None) -> dict:
    """A batch group from an author return.

    Reads both the batch-group shape and the wave author return: placement
    {body, annex} objects with packet-style after_input, notes, files_written. Owned
    files, part and label_tag come from the return or, where it lacks them, from its
    packet (named by the return, or found by the packet id ending the stem). With a
    packet, owned files come only from its owned_files; files_written entries outside
    them (editable hosts included) are appended to report, not adopted. Without one,
    files_written is the list. Such files are kept when they exist (or a placement
    routes them).
    """
    source = data.get("group") if isinstance(data.get("group"), dict) else data
    stem = (source.get("stem") or data.get("stem")
            or path.stem.removeprefix("edition-2026-").removesuffix("-return"))
    placement = normalized_placement(
        source.get("placement") or data.get("placement") or source.get("placements")
        or data.get("placements"), f"{path}: placement")
    placement_inputs = {tex_rel(rel_posix(p["input"])) for p in iter_placements_in_value(placement)
                        if isinstance(p.get("input"), str)}
    owned_lists: dict[str, list] = {kind: [] for kind, _folder, _suffix in OWNED_KINDS}
    for kind, alias in (("bodies", "body"), ("annexes", "annex"),
                        ("symbol_intakes", "symbols"), ("bibliography_intakes", "bibliography")):
        owned_lists[kind] += as_list(source.get(kind) or source.get(alias))
    owned = source.get("owned_files") or data.get("owned_files") or {}
    if isinstance(owned, dict):
        owned_lists["bodies"] += as_list(owned.get("bodies") or owned.get("body"))
        owned_lists["annexes"] += as_list(owned.get("annexes") or owned.get("annex"))
    # Authors also use these keys for prose ("symbols": "none new; ..."): a value holding
    # whitespace is not a path, so it is reported, never read as an owned file.
    for kind, items in owned_lists.items():
        prose = [item for item in items if isinstance(item, str) and re.search(r"\s", item.strip())]
        if prose and report is not None:
            report.extend({"return": rel_posix(str(path)), "field": kind, "value": item,
                           "reason": "not a path (holds whitespace); ignored"} for item in prose)
        owned_lists[kind] = [item for item in items if item not in prose]
    packet: dict = {}
    if (not any(owned_lists.values()) or not (source.get("part") or data.get("part"))
            or not (source.get("label_tag") or data.get("label_tag"))):
        packet = packet_for_return(path, data, stem)
    if not any(owned_lists.values()):
        # With a packet, only its owned_files are the group's: files_written may also name
        # the packet's editable hosts (canonical files) or anything else the author touched,
        # which are reported, never adopted as the group's bodies.
        packet_owned = [rel for rel in as_list(packet.get("owned_files")) if isinstance(rel, str)]
        editable = {rel_posix(rel) for rel in as_list(packet.get("editable_hosts"))
                    if isinstance(rel, str)}
        listed = [rel for rel in (owned if isinstance(owned, list) else [])
                  if not (isinstance(rel, str) and rel_posix(rel) in editable)] + packet_owned
        known = {rel_posix(rel) for rel in listed if isinstance(rel, str)}
        for rel in as_list(data.get("files_written")):
            if not isinstance(rel, str) or rel_posix(rel) in known:
                continue
            if packet_owned or rel_posix(rel) in editable:
                if report is not None:
                    report.append({"return": rel_posix(str(path)), "file": rel_posix(rel),
                                   "reason": "editable host of the packet" if rel_posix(rel) in editable
                                   else "not among the packet's owned_files"})
            else:
                listed.append(rel)
        for rel in listed:
            kind = owned_kind(rel) if isinstance(rel, str) else None
            if kind is None:
                continue
            tex = kind in {"bodies", "annexes"}
            target = resolve_handbook_path(BASE, rel, tex=tex)[0]
            if target.is_file() or (tex and tex_rel(rel_posix(rel)) in placement_inputs):
                owned_lists[kind].append(rel)
    bodies, annexes = owned_lists["bodies"], owned_lists["annexes"]
    part = source.get("part") or data.get("part") or packet.get("part")
    if not part:
        for rel in bodies + annexes:
            match = re.search(r"/p(\d{2})(?:/|\.|-)", rel_posix(rel))
            if match:
                part = "P" + str(int(match.group(1)))
                break
    if not part:
        raise Refusal(f"{path}: cannot determine part")
    symbol_intakes = owned_lists["symbol_intakes"] or conventional_intakes(stem, "symbol")
    bibliography_intakes = owned_lists["bibliography_intakes"] or conventional_intakes(stem, "bib")
    notes = source.get("notes") if isinstance(source.get("notes"), str) else None
    note = source.get("note") or data.get("note") or notes or f"spec/research/edition-2026-{stem}.md"
    annexitem_count = sum(count_annexitems(resolve_handbook_path(BASE, rel, tex=True)[0])
                          for rel in annexes)
    declared = source.get("declared_proof_pairs")
    if declared is not None:
        try:
            declared_int = int(declared)
        except (TypeError, ValueError) as exc:
            raise Refusal(f"{path}: declared_proof_pairs is not an integer: {declared!r}") from exc
        if declared_int != annexitem_count:
            raise Refusal(
                f"{path}: declared_proof_pairs {declared_int} does not match "
                f"annexitem count {annexitem_count}"
            )
    declared = annexitem_count
    group = {
        "stem": stem,
        "part": part,
        "bodies": sorted(dict.fromkeys(tex_rel(rel_posix(x)) for x in bodies)),
        "annexes": sorted(dict.fromkeys(tex_rel(rel_posix(x)) for x in annexes)),
        "symbol_intakes": sorted(dict.fromkeys(strip_handbook_prefix(rel_posix(x)) for x in symbol_intakes)),
        "bibliography_intakes": sorted(dict.fromkeys(strip_handbook_prefix(rel_posix(x)) for x in bibliography_intakes)),
        **({"rule_sheets": sheets} if (sheets := sorted(dict.fromkeys(
            strip_handbook_prefix(rel_posix(x)) for x in as_list(source.get("rule_sheets") or data.get("rule_sheets"))
            if isinstance(x, str) and not re.search(r"\s", x.strip())))) else {}),
        "note": rel_posix(note),
        "declared_proof_pairs": declared,
        "integration_status": "returned",
        "placement": placement,
        "label_tag": source.get("label_tag") or data.get("label_tag") or packet.get("label_tag"),
        "proposed_decisions": source.get("proposed_decisions") or data.get("proposed_decisions") or [],
    }
    problems = manifest_shape_errors({"groups": [group]})
    if problems:
        raise Refusal(f"{path}: malformed return: " + "; ".join(problems))
    owned_tex = set(group["bodies"]) | set(group["annexes"])
    if placement_inputs and not owned_tex:
        raise Refusal(f"{path}: placements route inputs but the group owns no body or annex file "
                      "(neither the return nor its packet lists one)")
    stray = sorted(placement_inputs - owned_tex)
    if stray:
        raise Refusal(f"{path}: placement inputs not owned by the group: " + ", ".join(stray))
    return group


def accounting_only(group: dict) -> bool:
    """True for a group that owns no body, annex, rule sheet or intake and has no
    placement: an accounting or unit-accounting return (null insertion), with nothing to
    route or adopt."""
    return (not any(group.get(key) for key in GROUP_LIST_FIELDS)
            and not iter_placements_in_value(group.get("placement"))
            and not iter_placements_in_value(group.get("placements")))


def validate_group_files(group: dict) -> list[str]:
    missing: list[str] = []
    for key in ("bodies", "annexes", "symbol_intakes", "bibliography_intakes"):
        for rel in group.get(key, []):
            path = resolve_handbook_path(BASE, rel, tex=key in {"bodies", "annexes"})[0]
            if not path.is_file():
                missing.append(path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else path.as_posix())
    note = group.get("note")
    if note and not repo_file(note).is_file():
        missing.append(note)
    return missing


def command_collect(args: argparse.Namespace) -> int:
    groups = []
    missing: list[str] = []
    seen_stems: set[str] = set()
    not_adopted: list[dict] = []
    accounting: list[dict] = []
    for return_path in args.return_json:
        path = Path(return_path)
        data = load_json(path)
        if not isinstance(data, dict):
            raise Refusal(f"{path}: return JSON must be an object")
        group = group_from_return(path, data, not_adopted)
        if accounting_only(group):
            # Nothing to route or adopt: listed, not made a batch group (route and adopt
            # would otherwise wait on it for the whole manifest).
            accounting.append({"return": rel_posix(str(path)), "stem": group["stem"],
                               "reason": "owns no body, annex or intake and has no placement "
                                         "(accounting return); not a batch group"})
            continue
        if group["stem"] in seen_stems:
            raise Refusal(f"{path}: duplicate stem {group['stem']!r} in one collect run")
        seen_stems.add(group["stem"])
        groups.append(group)
        missing.extend(validate_group_files(group))
    if missing:
        print_json({"ok": False, "command": "collect", "missing": missing})
        return 1
    out = ROOT / "spec" / "research" / f"edition-2026-authoring-batch-intake-{args.wave}.json"
    manifest = {
        "standing": "Collected wave author returns; integration, source admission and independent acceptance remain separate.",
        "wave": args.wave,
        "groups": groups,
        "book_complete": False,
        "catalog_admission_complete": False,
    }
    if args.apply:
        if out.exists() and not getattr(args, "force", False):
            raise Refusal(f"{out.relative_to(ROOT).as_posix()} already exists; use --force to overwrite")
        write_json_atomic(out, manifest)
    print_json({"ok": True, "command": "collect", "dry_run": not args.apply,
                "out": out.relative_to(ROOT).as_posix(), "groups": len(groups),
                "accounting_only": accounting,
                "files_written_not_adopted": not_adopted})
    return 0


def command_route(args: argparse.Namespace) -> int:
    manifest_path = Path(args.manifest)
    manifest, manifest_text = read_manifest(manifest_path)
    groups = manifest.get("groups", [])
    # Groups deliberately kept off the route are never routed, whatever placement they carry.
    held = {group.get("stem") for group in groups
            if (group.get("integration_status") or "") in ADOPT_SKIPPED_STATUSES}
    all_placements = manifest_placements(manifest)
    placements = [p for p in all_placements if p.get("stem") not in held]
    placed = {placement.get("stem") for placement in placements}
    unplaced = [group for group in groups if group.get("stem") not in placed]
    # A freshly collected group ("returned") cannot be routed without a placement; one with
    # nothing to route or adopt (accounting_only) is skipped.
    blocked = [{"stem": group.get("stem"), "error": "returned group has no placement"}
               for group in unplaced if group.get("integration_status") == "returned"
               and not accounting_only(group)]
    # A placed group must have a status route knows: promotable, already routed or merged
    # (its placement is then an idempotent no-op), or held (skipped above).
    blocked += [{"stem": group.get("stem"), "integration_status": group.get("integration_status"),
                 "error": "unknown integration_status for a placed group; route promotes only "
                          + " or ".join(sorted(ROUTE_PROMOTABLE_STATUSES)) + " groups"}
                for group in groups if group.get("stem") in placed
                and group.get("integration_status") not in ROUTE_PROMOTABLE_STATUSES
                and group.get("integration_status") != ADOPT_ROUTED_STATUS
                and not (group.get("integration_status") or "").startswith("merged")]
    # A placed group becomes routed only when the post-route static closure reaches each
    # of its owned bodies and annexes exactly once; the status edit is built (and may
    # refuse) from those counts before any host is written.
    candidates = [group for group in groups
                  if group.get("stem") in placed
                  and group.get("integration_status") in ROUTE_PROMOTABLE_STATUSES]
    status_report: dict[str, list] = {"routed": [], "not_fully_routed": []}

    def status_edit(counts: dict[str, int]) -> dict[Path, tuple[str, str]]:
        for group in candidates:
            reach: dict[str, int] = {}
            for rel in owned_rels(group):
                try:
                    rel = resolve_handbook_path(BASE, rel, tex=True)[1]
                except Refusal:
                    pass
                reach[rel] = counts.get(rel, 0)
            off = {rel: count for rel, count in reach.items() if count != 1}
            if reach and not off:
                status_report["routed"].append(group.get("stem"))
            else:
                status_report["not_fully_routed"].append({
                    "stem": group.get("stem"), "reach_counts": off,
                    "error": ("owned bodies/annexes not reached exactly once after routing; "
                              "status left unchanged") if reach else
                             "group owns no body or annex; status left unchanged"})
        routed = set(status_report["routed"])
        return ({manifest_path: (manifest_text, manifest_text_with_status(
            manifest_text, routed, ADOPT_ROUTED_STATUS))} if routed else {})

    result = simulate_route(BASE, placements, apply=args.apply and not blocked,
                            also_write=status_edit, siblings=all_placements)
    routed = set(status_report["routed"])
    result["command"] = "route"
    result["placements"] = len(placements)
    result["skipped_held_placements"] = [
        {"stem": p.get("stem"), "input": p.get("input")} for p in all_placements
        if p.get("stem") in held]
    result["groups_without_placement"] = [
        {"stem": group.get("stem"), "integration_status": group.get("integration_status")}
        for group in unplaced
    ]
    if blocked:
        result["ok"] = False
        result["dry_run"] = True
        result["errors"].extend(blocked)
    if args.apply and result["ok"] and routed:
        result["status_set_routed"] = sorted(routed)
    result["groups_not_fully_routed"] = status_report["not_fully_routed"]
    print_json(result)
    return 0 if result["ok"] and not status_report["not_fully_routed"] else 1


def located_route_inputs(base: Path, group: dict,
                         host_lines: dict[str, list[str]]) -> tuple[list[tuple[str, str]], list[dict]]:
    r"""Find the \input lines that route a group's owned files, for groups without placements.

    host_lines maps every file of the static closure from main.tex to its lines.
    Lines inside the group's own files are ignored (removing the outer input already
    disconnects them).
    """
    owned = {tex_rel(rel) for key in ("bodies", "annexes", "rule_sheets")
             for rel in group.get(key, [])}
    errors: list[dict] = []
    found: list[tuple[str, str]] = []
    active_hosts = {host: active_tex("\n".join(lines)) for host, lines in host_lines.items()
                    if host not in owned}
    for rel in sorted(owned):
        hits = [host for host, text in active_hosts.items()
                for _hit in input_occurrences(base, text, rel)]
        if len(hits) > 1:
            errors.append({"stem": group.get("stem"), "input": rel,
                           "error": f"input occurs {len(hits)} times in route hosts"})
        elif hits:
            found.append((hits[0], rel))
    if not found and not errors:
        errors.append({"stem": group.get("stem"),
                       "error": "no placement and no routed input line found for group"})
    return found, errors


def closure_host_lines(base: Path) -> tuple[dict[str, list[str]], list[str]]:
    counts, errors = static_input_counts(base)
    host_lines: dict[str, list[str]] = {}
    for rel in sorted(set(counts) | {"main.tex"}):
        path = resolve_handbook_path(base, rel, tex=True, allow_forbidden=True)[0]
        if path.is_file():
            host_lines[rel] = read_text(path).split("\n")
    return host_lines, errors


def command_unroute(args: argparse.Namespace) -> int:
    manifest_path = Path(args.manifest)
    manifest, manifest_text = read_manifest(manifest_path)
    stems = {x.strip() for x in args.stems.split(",") if x.strip()}
    if not stems:
        raise UsageError("--stems must name at least one stem")
    groups = [g for g in manifest.get("groups", []) if g.get("stem") in stems]
    unknown = sorted(stems - {g.get("stem") for g in groups})
    if unknown:
        raise Refusal("unknown stems: " + ", ".join(unknown))
    # A merged group's rows are in the canonical registry with first_use labels on the
    # route: unrouting it would strand them (read_rows fails, the book build breaks). A
    # held group is not on the route at all; route skips it, so unroute refuses it too.
    not_unroutable = [{"stem": g.get("stem"), "integration_status": g.get("integration_status"),
                       "error": ("merged group: its canonical symbol rows would lose their "
                                 "first_use on the reader route; unroute refused")
                                if (g.get("integration_status") or "").startswith("merged") else
                                "held group (kept off the route); unroute refused"}
                      for g in groups
                      if (g.get("integration_status") or "").startswith("merged")
                      or g.get("integration_status") in ADOPT_SKIPPED_STATUSES]
    if not_unroutable:
        print_json({"ok": False, "command": "unroute", "errors": not_unroutable, "actions": [],
                    "dry_run": True})
        return 1
    errors: list[dict] = []
    actions: list[dict] = []
    originals: dict[Path, str] = {}
    writes: dict[Path, str] = {}
    by_stem: dict[str, list[dict]] = {}
    for placement in manifest_placements(manifest):
        by_stem.setdefault(placement.get("stem"), []).append(placement)
    targets: list[tuple[str, str, str]] = []
    host_lines: dict[str, list[str]] | None = None
    for group in groups:
        stem = group.get("stem")
        if by_stem.get(stem):
            targets.extend((stem, p["host"], p["input"]) for p in by_stem[stem])
        else:
            if host_lines is None:
                host_lines, closure_errors = closure_host_lines(BASE)
                errors.extend({"error": err} for err in closure_errors)
            found, located_errors = located_route_inputs(BASE, group, host_lines)
            errors.extend(located_errors)
            targets.extend((stem, host, rel) for host, rel in found)
    for stem, host_name, input_name in targets:
        try:
            host, host_rel = resolve_handbook_path(BASE, host_name, tex=True)
            _input_path, input_rel = resolve_handbook_path(BASE, input_name, tex=True)
        except Refusal as exc:
            errors.append({"stem": stem, "host": host_name, "input": input_name, "error": str(exc)})
            continue
        if not host.is_file():
            errors.append({"stem": stem, "host": host_rel, "error": "host file missing"})
            continue
        if host_rel in pinned_reader_files():
            errors.append({"stem": stem, "host": host_rel,
                           "error": "route host is a check.py byte-pinned retained file "
                                    "(HB_RETAINED_UNREACHABLE_READER_FILES); edit refused"})
            continue
        if host not in originals:
            originals[host] = read_text(host)
        text = writes.get(host, originals[host])
        lines = text.split("\n")
        active_lines = active_tex(text).split("\n")
        hits = input_occurrences(BASE, "\n".join(active_lines), input_rel)
        if len(hits) != 1:
            errors.append({"stem": stem, "host": host_rel, "input": input_rel,
                           "error": f"input occurs {len(hits)} times"})
            continue
        # Remove only the \input span; the line goes only when nothing active remains.
        number, match = hits[0]
        rest = lines[number][:match.start()] + lines[number][match.end():]
        line_dropped = not strip_line_comment(rest).strip()
        if line_dropped:
            lines.pop(number)
        else:
            lines[number] = rest
        writes[host] = "\n".join(lines)
        actions.append({"stem": stem, "host": host_rel, "line": number + 1,
                        "removed": match.group(0), "line_dropped": line_dropped})
    if errors or len(actions) != len(targets):
        print_json({"ok": False, "command": "unroute", "errors": errors, "actions": actions,
                    "dry_run": True})
        return 1
    new_manifest_text = manifest_text_with_status(manifest_text, stems, "returned-for-fix")
    if args.apply:
        refuse_changed_since_read({manifest_path: manifest_text,
                                   **{path: originals[path] for path in writes}})
        for path, text in writes.items():
            write_text_atomic(path, text)
        write_text_atomic(manifest_path, new_manifest_text)
    print_json({"ok": True, "command": "unroute", "actions": actions,
                "status_updates": sorted(stems), "dry_run": not args.apply})
    return 0


BIB_COMMENT_BLOCK_RE = re.compile(r"@comment\s*([{(])", re.I)


def mask_bib_comments(text: str) -> str:
    r"""Blank % comments outside field values (brace depth <= 1, not quoted) and the
    delimited body of each top-level @comment{...} / @comment(...) block; offsets and
    newlines kept.

    Biber reads such a % as a comment to the end of the line; inside a braced or
    quoted value (a URL's %20, say) it is literal text. It ignores an @comment body,
    records written inside it included. As in BibTeX, a backslash escapes nothing: \{ and
    \} count as braces and \" ends a quoted value at brace depth 0.
    """
    chars = list(text)
    depth = 0
    quoted = False
    i = 0
    while i < len(text):
        ch = text[i]
        block =BIB_COMMENT_BLOCK_RE.match(text, i) if ch == "@" and depth == 0 else None
        if block:
            opener = block.group(1)
            closer = "}" if opener == "{" else ")"
            level = 0
            end = block.start(1)
            while end < len(text):
                if text[end] == opener:
                    level += 1
                elif text[end] == closer:
                    level -= 1
                    if level == 0:
                        break
                end += 1
            if end >= len(text):
                raise Refusal("unterminated @comment block near offset " + str(i))
            for j in range(block.start(1), end + 1):
                if chars[j] != "\n":
                    chars[j] = " "
            i = end + 1
            continue
        if ch == "%" and depth <= 1 and not quoted:
            end = text.find("\n", i)
            end = len(text) if end < 0 else end
            for j in range(i, end):
                chars[j] = " "
            i = end
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth = max(0, depth - 1)
        elif ch == '"' and depth == 1:
            quoted = not quoted
        i += 1
    return "".join(chars)


def bib_brace_end(text: str, start: int) -> int:
    """Offset after the } matching the { at start, counting braces as BibTeX does (a
    backslash escapes nothing); -1 when unbalanced."""
    depth = 0
    for index in range(start, len(text)):
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
            if depth == 0:
                return index + 1
    return -1


def bib_quote_end(text: str, start: int, end: int) -> int:
    """Offset of the " closing the quoted value opened at start: the next " at brace depth
    0, as in BibTeX (\\" ends the value; {\\"o} does not). -1 when none before end."""
    depth = 0
    for index in range(start + 1, end):
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
        elif text[index] == '"' and depth == 0:
            return index
    return -1


def bib_records(text: str) -> list[dict]:
    """@type{key, ...} records of live (not commented-out) bibliography text."""
    masked = mask_bib_comments(text)
    records: list[dict] = []
    previous_end = 0
    for match in re.finditer(r"@([A-Za-z]+)\s*\{\s*([^,\s{}]+)\s*,", masked):
        if match.group(1).lower() in {"comment", "string", "preamble"}:
            continue
        if match.start() < previous_end:
            raise Refusal("bibliography record " + match.group(2) + " starts inside record "
                          + records[-1]["key"] + " (unterminated entry)")
        end = bib_brace_end(masked, masked.find("{", match.start()))
        if end < 0:
            raise Refusal("unbalanced bibliography record " + match.group(2))
        raw = text[match.start():end]
        previous_end = end
        records.append({
            "key": match.group(2),
            "type": match.group(1).lower(),
            "raw": raw,
            "sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
            "comparison": re.sub(r"\s+", " ", masked[match.start():end]).strip(),
        })
    return records


BIB_ENTRY_START_RE = re.compile(r"@([A-Za-z]+)\s*[({]")


def unparsed_bib_entries(text: str) -> list[str]:
    """Live entry openings bib_records cannot read (e.g. parenthesis-delimited @book(...))."""
    masked = mask_bib_comments(text)
    found: list[str] = []
    for match in BIB_ENTRY_START_RE.finditer(masked):
        if match.group(1).lower() in {"comment", "string", "preamble"}:
            continue
        if not re.match(r"@[A-Za-z]+\s*\{\s*[^,\s{}]+\s*,", masked[match.start():]):
            found.append(masked[match.start():match.start() + 60].split("\n")[0])
    return found


def commented_bib_entries(text: str) -> list[str]:
    """Entry openings that sit in % comments (skipped by biber and by adopt)."""
    masked = mask_bib_comments(text)
    return [text[m.start():m.start() + 60].split("\n")[0]
            for m in BIB_ENTRY_START_RE.finditer(text) if masked[m.start()] != "@"]


BIB_MACRO_RECORD_RE = re.compile(r"@(string|preamble)\s*[({]", re.I)
BIB_PREDEFINED_MACROS = {"jan", "feb", "mar", "apr", "may", "jun",
                         "jul", "aug", "sep", "oct", "nov", "dec"}


def bib_macro_records(text: str) -> list[str]:
    """Live @string / @preamble openings (biber macros a record may depend on)."""
    masked = mask_bib_comments(text)
    return [masked[m.start():m.start() + 60].split("\n")[0]
            for m in BIB_MACRO_RECORD_RE.finditer(masked)]


def bib_string_names(text: str) -> set[str]:
    """Macro names that live @string records define (case-insensitive, as biber reads them)."""
    masked = mask_bib_comments(text)
    return {m.group(1).casefold()
            for m in re.finditer(r"@string\s*[({]\s*([^\s=,{}()\"#]+)\s*=", masked, re.I)}


def bib_value_macros(record: dict) -> set[str]:
    """Bare (unbraced, unquoted, non-numeric) value parts: macro names biber must resolve."""
    raw = mask_bib_comments(record["raw"])
    end = len(raw) - 1  # the record's closing brace
    cursor = raw.index(",") + 1
    found: set[str] = set()
    field_re = re.compile(r"\s*,?\s*([^\s=,{}\"#]+)\s*=\s*")
    while True:
        match = field_re.match(raw, cursor, end)
        if not match:
            return found
        cursor = match.end()
        while True:  # value parts joined by '#'
            while cursor < end and raw[cursor].isspace():
                cursor += 1
            if cursor >= end:
                return found
            if raw[cursor] == "{":
                cursor = bib_brace_end(raw, cursor)
                if cursor < 0:
                    raise Refusal("unbalanced bibliography field in " + record["key"])
            elif raw[cursor] == '"':
                close = bib_quote_end(raw, cursor, end)
                if close < 0:
                    raise Refusal("unterminated quoted bibliography field in " + record["key"])
                cursor = close + 1
            else:
                token = re.compile(r"[^\s,#{}\"]+").match(raw, cursor, end)
                if not token:
                    return found
                if not token.group(0).isdigit():
                    found.add(token.group(0).casefold())
                cursor = token.end()
            while cursor < end and raw[cursor].isspace():
                cursor += 1
            if cursor < end and raw[cursor] == "#":
                cursor += 1
                continue
            break


BIB_FIELD_NAME_RE = re.compile(r"[^\s\"#%'(),={}0-9][^\s\"#%'(),={}]*")
BIB_NUMBER_RE = re.compile(r"[0-9]+")


def bib_record_syntax_error(raw: str) -> str | None:
    r"""Why a record (as bib_records cuts it) breaks the BibTeX entry grammar, or None.

    Grammar: @type{key, then name = part (# part)* items separated by commas (a trailing
    comma allowed), up to the record's own closing brace and nothing else. A part is a
    {braced} value, a "quoted" value (ended by the first " at brace depth 0; its braces
    balance), a number or a macro name. Braces count as in BibTeX: a backslash escapes
    nothing, so \} closes a brace and \" ends a quoted value.
    """
    text = mask_bib_comments(raw)
    head = re.match(r"@[A-Za-z]+\s*\{\s*[^,\s{}]+\s*,", text)
    if not head:
        return "entry does not open with @type{key,"
    end = len(text) - 1
    if text[end] != "}":
        return "entry does not end at its own closing brace"

    def where(cursor: int) -> str:
        return repr(text[cursor:cursor + 30].split("\n")[0])

    cursor = head.end()
    while True:
        while cursor < end and text[cursor].isspace():
            cursor += 1
        if cursor == end:
            return None
        field = BIB_FIELD_NAME_RE.match(text, cursor, end)
        if not field:
            return "expected a field name at " + where(cursor)
        name = field.group(0)
        cursor = field.end()
        while cursor < end and text[cursor].isspace():
            cursor += 1
        if cursor >= end or text[cursor] != "=":
            return "field " + name + " lacks '=' (found " + where(cursor) + ")"
        cursor += 1
        while True:  # value parts joined by '#'
            while cursor < end and text[cursor].isspace():
                cursor += 1
            if cursor >= end:
                return "field " + name + " has no value"
            if text[cursor] == "{":
                close = bib_brace_end(text, cursor)
                if close < 0 or close > end:
                    return "field " + name + " has unbalanced braces"
                cursor = close
            elif text[cursor] == '"':
                depth, close = 0, -1
                for index in range(cursor + 1, end):
                    if text[index] == "{":
                        depth += 1
                    elif text[index] == "}":
                        depth -= 1
                        if depth < 0:
                            return "quoted field " + name + " has an unbalanced }"
                    elif text[index] == '"' and depth == 0:
                        close = index
                        break
                if close < 0:
                    return "quoted field " + name + " is not closed inside the entry"
                cursor = close + 1
            else:
                token = (BIB_NUMBER_RE.match(text, cursor, end)
                         or BIB_FIELD_NAME_RE.match(text, cursor, end))
                if not token:
                    return "field " + name + " has no valid value at " + where(cursor)
                cursor = token.end()
            while cursor < end and text[cursor].isspace():
                cursor += 1
            if cursor < end and text[cursor] == "#":
                cursor += 1
                continue
            break
        if cursor == end:
            return None
        if text[cursor] != ",":
            return ("expected ',' or the end of the entry after field " + name + ", found "
                    + where(cursor))
        cursor += 1


def bib_text_errors(text: str, expected_keys: list[str],
                    syntax_keys: set[str] | frozenset = frozenset()) -> list[str]:
    """Problems that would make a bibliography text unreadable or lose an expected record;
    the records named in syntax_keys (the appended ones) must also follow the grammar."""
    try:
        records = bib_records(text)
    except Refusal as exc:
        return [str(exc)]
    errors = ["unparsed entry: " + entry for entry in unparsed_bib_entries(text)]
    if [record["key"] for record in records] != expected_keys:
        errors.append("record keys differ from the expected canonical+appended sequence")
    for record in records:
        problem = bib_record_syntax_error(record["raw"]) if record["key"] in syntax_keys else None
        if problem:
            errors.append("record " + record["key"] + ": " + problem)
    return errors


def isbn13(digits: str) -> str:
    """ISBN-10 to ISBN-13 (978 prefix); other values unchanged."""
    if len(digits) != 10 or not digits[:9].isdigit():
        return digits
    core = "978" + digits[:9]
    check = (10 - sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(core)) % 10) % 10
    return core + str(check)


def bib_fields(record: dict) -> dict:
    raw = mask_bib_comments(record["raw"])
    cursor = raw.index(",") + 1
    found: dict[str, str] = {}
    while cursor < len(raw) - 1:
        match = re.match(r"\s*,?\s*([A-Za-z]+)\s*=\s*", raw[cursor:])
        if not match:
            break
        key = match.group(1).lower()
        cursor += match.end()
        if cursor >= len(raw):
            break
        if raw[cursor] == "{":
            end = bib_brace_end(raw, cursor)
            if end < 0:
                raise Refusal("unbalanced bibliography field " + key)
            value = raw[cursor + 1:end - 1]
            cursor = end
        elif raw[cursor] == '"':
            end = bib_quote_end(raw, cursor, len(raw))
            if end < 0:
                raise Refusal("unterminated quoted bibliography field " + key)
            value = raw[cursor + 1:end]
            cursor = end + 1
        else:
            end = raw.find(",", cursor)
            if end < 0:
                end = len(raw) - 1
            value = raw[cursor:end].strip()
            cursor = end
        found[key] = re.sub(r"\s+", " ", value).strip()
    return found


def normalize_identity(value: str | None) -> str:
    """Author/title text for duplicate detection: braces, case and punctuation ignored."""
    value = value or ""
    value = re.sub(r"[{}\\]", "", value)
    value = re.sub(r"[^\w\s]", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip().casefold()


def publication_year(fields: dict) -> str:
    return (fields.get("year") or fields.get("date") or "")[:4]


def unescape_tex_identifier(value: str) -> str:
    r"""A DOI/URL as written in TeX source: \_ \% \& \# unescaped, braces dropped."""
    return re.sub(r"\\([_%&#])", r"\1", value).replace("{", "").replace("}", "")


def normalize_doi(value: str) -> str | None:
    value = unescape_tex_identifier(value).strip()
    value = re.sub(r"^doi:\s*", "", value, flags=re.I)
    value = re.sub(r"^https?://(?:www\.)?(?:dx\.)?doi\.org/", "", value, flags=re.I)
    value = value.strip().strip("<>")
    value = re.sub(r"[\s,.;]+$", "", value)
    return value.casefold() if value else None


def dois_in_text(value: str) -> set[str]:
    found: set[str] = set()
    for match in re.finditer(
        r"(?:doi:\s*|https?://(?:www\.)?(?:dx\.)?doi\.org/)?"
        r"(10\.[^\s{}<>\"\\]+/[^\s{}<>\"\\]+)",
        unescape_tex_identifier(value),
        flags=re.I,
    ):
        doi = normalize_doi(match.group(1))
        if doi:
            found.add(doi)
    return found


def bib_locators(record: dict) -> list[str]:
    fields = bib_fields(record)
    found: set[str] = set()
    doi = fields.get("doi")
    if doi:
        normalized = normalize_doi(doi)
        if normalized:
            found.add("doi:" + normalized)
    for field in ("eprint", "url", "note"):
        value = fields.get(field, "")
        for item in dois_in_text(value):
            found.add("doi:" + item)
        # The version suffix (v2) names a revision of the same work.
        for item in re.findall(r"\b(\d{4}\.\d{4,5})(?:v\d+)?\b", value):
            found.add("arxiv:" + item.casefold())
        for item in re.findall(r"\b([A-Za-z][A-Za-z.-]*/[0-9]{7})(?:v[0-9]+)?\b", value):
            found.add("arxiv:" + item.casefold())
    found.update("isbn:" + item for item in isbn_values(fields.get("isbn", "")))
    return sorted(found)


def isbn_values(value: str) -> list[str]:
    """Each ISBN listed in an isbn field, normalized to ISBN-13.

    Items split on ';' and ','. An item whose characters do not form one ISBN-10/13
    is split again on whitespace (spaces may also separate groups inside one ISBN).
    """
    found: list[str] = []
    for item in re.split(r"[;,]", value):
        digits = re.sub(r"[^0-9Xx]", "", item).upper()
        pieces = [digits] if len(digits) in {10, 13} else [
            re.sub(r"[^0-9Xx]", "", piece).upper() for piece in item.split()]
        found.extend(isbn13(piece) for piece in pieces if piece)
    return found


def same_publication_identity(a: dict, b: dict) -> bool:
    af = bib_fields(a)
    bf = bib_fields(b)
    return bool(publication_year(af)) and publication_year(af) == publication_year(bf) and all(
        af.get(k) and bf.get(k) and normalize_identity(af[k]) == normalize_identity(bf[k])
        for k in ("author", "title")
    )


class IntakeRowError(ValueError):
    """An intake row that cannot be normalized safely; it is reported and never written."""


# Paired TeX delimiters a top-level comma inside them does not separate family members.
OPEN_DELIMITERS = {r"\langle": "angle", r"\lvert": "vert", r"\lVert": "Vert", r"\{": "set",
                   r"\lbrace": "set", r"\lbrack": "paren", r"\lceil": "ceil", r"\lfloor": "floor"}
CLOSE_DELIMITERS = {r"\rangle": "angle", r"\rvert": "vert", r"\rVert": "Vert", r"\}": "set",
                    r"\rbrace": "set", r"\rbrack": "paren", r"\rceil": "ceil", r"\rfloor": "floor"}
TEX_TOKEN_RE = re.compile(r"\\(?:[A-Za-z]+|.)")


def split_top(value: str) -> tuple[list[str], bool]:
    r"""Split a TeX glyph at commas outside every delimiter pair; (parts, balanced).

    Pairs: {..}, (..) and [..] (either closer, for half-open intervals), \left..\right,
    \langle..\rangle, \lvert..\rvert, \lVert..\rVert, \{..\}, \lceil, \lfloor, and the
    self-closing |..| and \|..\|. balanced is False when a closer does not match its
    opener or an opener is left open.
    """
    parts: list[str] = []
    stack: list[str] = []
    balanced = True
    start = 0
    index = 0

    def push_or_pop(kind: str, opens: bool, closes: bool) -> None:
        nonlocal balanced
        if closes and stack and stack[-1] == kind:
            stack.pop()
        elif opens:
            stack.append(kind)
        else:
            balanced = False

    def skip_delimiter_token(cursor: int) -> int:
        while cursor < len(value) and value[cursor].isspace():
            cursor += 1
        token = TEX_TOKEN_RE.match(value, cursor)
        return token.end() if token else min(cursor + 1, len(value))

    while index < len(value):
        ch = value[index]
        if ch == "\\":
            token = TEX_TOKEN_RE.match(value, index)
            word = token.group(0) if token else "\\"
            index = token.end() if token else index + 1
            if word == r"\left":
                push_or_pop("left", True, False)
                index = skip_delimiter_token(index)
            elif word == r"\right":
                push_or_pop("left", False, True)
                index = skip_delimiter_token(index)
            elif word in OPEN_DELIMITERS:
                push_or_pop(OPEN_DELIMITERS[word], True, False)
            elif word in CLOSE_DELIMITERS:
                push_or_pop(CLOSE_DELIMITERS[word], False, True)
            elif word == r"\|":
                push_or_pop("dbar", True, True)
            continue
        if ch in "([":
            push_or_pop("paren", True, False)
        elif ch in ")]":
            push_or_pop("paren", False, True)
        elif ch == "{":
            push_or_pop("brace", True, False)
        elif ch == "}":
            push_or_pop("brace", False, True)
        elif ch == "|":
            push_or_pop("bar", True, True)
        elif ch == "," and not stack:
            parts.append(value[start:index].strip())
            start = index + 1
        index += 1
    parts.append(value[start:].strip())
    return parts, balanced and not stack


ELLIPSIS_MEMBERS = {r"\ldots", r"\dots", r"\cdots", r"\dotsc", "..."}


def is_sequence_glyph(glyph: str) -> bool:
    r"""True for a comma list with an ellipsis member (T_0,\ldots,T_k): one sequence glyph,
    kept as one row like the canonical \(R_1,\ldots,R_{q+1}\), never split into members."""
    parts, balanced = split_top(glyph)
    return balanced and len(parts) > 1 and any(part in ELLIPSIS_MEMBERS for part in parts)


def family_members(glyph: str) -> list[str]:
    """The glyphs a comma-listed family names: [glyph] for one glyph or a sequence glyph.

    Raises IntakeRowError when a comma cannot be read safely: the glyph has unbalanced
    delimiters, or a resulting member is empty or not a balanced glyph of its own.
    """
    parts, balanced = split_top(glyph)
    if not balanced:
        if "," in glyph:
            raise IntakeRowError("glyph " + repr(glyph) + " has a comma and unbalanced delimiters; "
                                 "cannot tell a symbol family from one glyph (declare it explicitly)")
        return [glyph]
    for part in parts if len(parts) > 1 else []:
        sub_parts, sub_balanced = split_top(part)
        if not part or not sub_balanced or len(sub_parts) != 1:
            raise IntakeRowError("glyph " + repr(glyph) + " splits into the unbalanced member "
                                 + repr(part) + " (declare the family explicitly)")
    return [glyph] if is_sequence_glyph(glyph) else parts


def unwrap_glyph(glyph: str) -> str:
    glyph = glyph.strip()
    if glyph.startswith(r"\(") and glyph.endswith(r"\)"):
        return glyph[2:-2]
    if glyph.startswith("$") and glyph.endswith("$") and len(glyph) >= 2:
        return glyph[1:-1]
    return glyph


def intake_glyph_body(raw: str) -> str:
    r"""The TeX body of an intake glyph cell, checked before unwrapping.

    A leading $$ (display math, or an empty $$) is refused: unwrapping one dollar pair
    from $$x$$ would leave $x$ and hide the display delimiters inside the body.
    """
    g = raw.strip()
    if g.startswith("$$"):
        raise IntakeRowError("glyph " + repr(raw) + " starts with $$ (display math or an empty "
                             "glyph); give the bare TeX form")
    body = unwrap_glyph(g)
    if body != g and any(d in body for d in (r"\(", r"\)")):
        raise IntakeRowError("glyph " + repr(raw) + " holds several separately wrapped math "
                             r"spans (e.g. \(A\), \(B\)); give one bare TeX form (A,B for a "
                             "family) or one row per glyph")
    return body


TEXT_ARG_RE = re.compile(r"\\(?:text[A-Za-z]*|mbox)(?![A-Za-z@])\s*(?=\{)")


def text_argument_spans(g: str) -> list[tuple[int, int]]:
    r"""(start, end) of each \text...{...} / \mbox{...} argument (text mode inside math)."""
    spans: list[tuple[int, int]] = []
    for match in TEXT_ARG_RE.finditer(g):
        args, end = grammar.scan_braced_args(g, match.end(), 1)
        if args:
            spans.append((match.end(), end))
    return spans


def nonascii_math_characters(body: str) -> list[str]:
    r"""Non-ASCII characters of a glyph body outside \text{...}: math fonts lack them."""
    spans = text_argument_spans(body)
    return sorted({ch for i, ch in enumerate(body) if ord(ch) > 127
                   and not any(start <= i < end for start, end in spans)})


# Definitions, assignments, file and catcode primitives, and commands that act outside the
# table cell (labels and anchors, index/citation/TOC/mark entries, notes, page styles,
# global font parameters, interaction modes): a cell holding one would act on the rest of
# the book after the symbol table, and still compile (so the gate passes). Every citation
# command (\cite, \parencite, \nocite, ...) counts too (side_effect_token).
SIDE_EFFECT_TOKENS = {"\\" + name for name in (
    "def gdef edef xdef let futurelet global long outer protected catcode lccode uccode "
    "mathcode delcode sfcode chardef mathchardef countdef dimendef skipdef muskipdef toksdef "
    "newcommand renewcommand providecommand DeclareRobustCommand NewDocumentCommand "
    "RenewDocumentCommand ProvideDocumentCommand DeclareDocumentCommand NewCommandCopy "
    "DeclareMathOperator DeclareMathSymbol DeclareMathAlphabet DeclareSymbolFont "
    "newcount newdimen newskip newtoks newif newlength newcounter newenvironment "
    "renewenvironment setcounter addtocounter stepcounter refstepcounter setlength "
    "addtolength settowidth input include InputIfFileExists endinput makeatletter "
    "makeatother csname expandafter write immediate openout openin closeout closein "
    "read special afterassignment aftergroup everymath everydisplay everypar everyhbox "
    "everyvbox everycr usepackage RequirePackage documentclass ExplSyntaxOn "
    "AtBeginDocument AtEndDocument AddToHook AddToHookNext ProcessOptions "
    "scantokens uppercase lowercase "
    "label index glossary hypertarget hyperlink hyperdef phantomsection addcontentsline "
    "addtocontents markboth markright footnote footnotemark footnotetext marginpar "
    "pagestyle thispagestyle fontdimen hyphenchar skewchar globaldefs interactionmode "
    "batchmode nonstopmode scrollmode errorstopmode").split()}


def side_effect_token(value: str) -> str | None:
    """The first SIDE_EFFECT_TOKENS or citation-command token in value, or None."""
    return next((token for token in TEX_TOKEN_RE.findall(value)
                 if token in SIDE_EFFECT_TOKENS or ANY_CITE_COMMAND_RE.fullmatch(token)), None)


# Commands whose braced argument stacks rows: a \\ there breaks a row of the argument.
ROW_STACK_COMMANDS = {r"\substack", r"\shortstack", r"\Shortstack"}


def math_glyph(glyph: str) -> str:
    r"""The glyph body made safe to wrap in \(...\), or IntakeRowError.

    A glyph that is only $ % # & or _ becomes its escaped form; nothing else is ever
    rewritten. Refused: an empty body, a blank line, math delimiters inside the body (no
    nesting), an unescaped $ (inside \text{...} too), an unescaped % or # anywhere, an
    unescaped & outside an environment (inside \begin{..}..\end{..} it is alignment
    syntax), ^^ (TeX's character-code notation), a trailing odd backslash run (it would
    consume the closing \)), \\ outside an environment or a \substack/\shortstack
    argument and \par (both end the table row the glyph is typeset in), ^ or _ with no
    operand, a second ^ or _ on one base (TeX's double sub/superscript error), unbalanced
    braces or \left/\right, a bare ^ or ~ glyph, and definition, assignment or file
    primitives (SIDE_EFFECT_TOKENS: \gdef, \let, \catcode, \input, ...). What syntax cannot see (a command's arity, say) is left to adopt's
    compile gate.
    """
    g = glyph.strip()

    def refuse(reason: str) -> IntakeRowError:
        return IntakeRowError("glyph " + repr(glyph) + " " + reason)

    if not g:
        raise refuse("is empty")
    if g in ("$", "%", "#", "&", "_"):
        return "\\" + g
    if g in ("^", "~"):
        raise refuse("is a bare " + g + "; give its TeX form (e.g. \\hat{}, \\sim)")
    if re.search(r"\n[ \t\r]*\n", g):
        raise refuse("contains a blank line (a paragraph break is not valid in math)")
    if g.startswith("$$") or any(d in g for d in (r"\(", r"\)", r"\[", r"\]")):
        raise refuse("contains math delimiters; give the bare TeX form")
    if "^^" in g:
        raise refuse("contains ^^ (TeX character-code notation); give the TeX command")
    side_effect = side_effect_token(g)
    if side_effect:
        raise refuse("has " + side_effect + " (a definition, assignment, file primitive or "
                     "command acting outside the table cell would act on the rest of the book); "
                     "give the bare TeX form")
    text_spans = text_argument_spans(g)
    # One entry per brace level: the scripts already attached to the current base, whether
    # the next atom is the operand of a ^ or _ (it then keeps that base), and whether the
    # level is (inside) a \substack-like argument, where \\ breaks a row of the stack.
    levels: list[dict] = [{"seen": set(), "operand": False, "stack": False}]
    environments = 0
    stack_pending = False

    def atom() -> None:
        level = levels[-1]
        if level["operand"]:
            level["operand"] = False
        else:
            level["seen"] = set()

    i = 0
    while i < len(g):
        ch = g[i]
        if ch == "\\":
            if i + 1 >= len(g):
                raise refuse("ends in an odd backslash run, which would consume the closing \\)")
            match = TEX_TOKEN_RE.match(g, i)
            token = match.group(0) if match else g[i:i + 2]
            i += len(token)
            if token in ROW_STACK_COMMANDS:
                stack_pending = True
            if token == "\\\\" and not environments and not levels[-1]["stack"]:
                raise refuse(r"has \\ outside an environment (a row break ends the table "
                             "row the glyph is typeset in)")
            if token == r"\par":
                raise refuse(r"has \par (a paragraph break is not valid in math)")
            if token == r"\begin":
                environments += 1
            elif token == r"\end":
                environments -= 1
            if token not in (r"\limits", r"\nolimits", r"\displaylimits"):
                atom()
            continue
        if ch == "$":
            if any(start <= i < end for start, end in text_spans):
                raise refuse(r"has $ inside \text{...}; give the intended TeX form explicitly")
            raise refuse("has an unescaped $ (math delimiter) in its body; give the bare TeX form")
        if ch == "%":
            raise refuse(r"has an unescaped % (it starts a TeX comment); write \% for the sign")
        if ch == "#":
            raise refuse(r"has an unescaped # (TeX's macro parameter character); write \#")
        if ch == "&" and not environments:
            raise refuse(r"has an unescaped & outside an environment (an alignment tab); "
                         r"write \& for the sign")
        if ch in "^_":
            rest = g[i + 1:].lstrip()
            if not rest or rest[0] == "}":
                raise refuse("has " + ch + " with no operand")
            level = levels[-1]
            if ch in level["seen"]:
                raise refuse("has a double " + ("superscript" if ch == "^" else "subscript")
                             + " on one base; brace the base (e.g. {a_b}_c)")
            level["seen"].add(ch)
            level["operand"] = True
        elif ch == "{":
            levels.append({"seen": set(), "operand": False,
                           "stack": stack_pending or levels[-1]["stack"]})
            stack_pending = False
        elif ch == "}":
            levels.pop()
            if not levels:
                raise refuse("has unbalanced braces")
            atom()
        elif not ch.isspace():
            atom()
        i += 1
    if len(levels) != 1:
        raise refuse("has unbalanced braces")
    fences = 0
    for token in TEX_TOKEN_RE.findall(g):
        if token == r"\left":
            fences += 1
        elif token == r"\right":
            fences -= 1
            if fences < 0:
                break
    if fences:
        raise refuse(r"has unbalanced \left/\right")
    return g


def macro_problem(value: str) -> str | None:
    r"""Why a macro cell would break \texttt{\detokenize{...}} in the symbol table, or None.

    \detokenize reads its argument as TeX tokens: \{ \} \% are control symbols, a bare
    % starts a comment, braces must balance, a trailing odd backslash run swallows the
    closing brace, ^^ is character-code notation and a blank line is \par.
    """
    if "^^" in value:
        return "contains ^^ (TeX character-code notation)"
    side_effect = side_effect_token(value)
    if side_effect:
        return ("has " + side_effect + " (a definition, assignment, file primitive or command "
                "acting outside the table cell)")
    if re.search(r"\n[ \t\r]*\n", value):
        return "contains a blank line (a paragraph break)"
    depth = 0
    i = 0
    while i < len(value):
        ch = value[i]
        if ch == "\\":
            if i + 1 >= len(value):
                return ("ends in an odd backslash run, which would consume the closing brace "
                        "of \\detokenize{...}")
            i += 2
            continue
        if ch == "%":
            return r"has an unescaped % (it starts a TeX comment); write \%"
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                return "has unbalanced braces"
        i += 1
    return "has unbalanced braces" if depth else None


def visible_glyph(glyph: str) -> str:
    return re.sub(r"\s+", "", unwrap_glyph(glyph))


MACRO_FILL_NOTE = "Blank macro filled with the glyph's TeX spelling."


def append_note(row: dict, note: str) -> None:
    row["notes"] = (row.get("notes", "") + (" " if row.get("notes") else "") + note).strip()


P09_MODELS = "registry/symbols-intake-p09-recombination-models.csv"
P09_NATIVE = "registry/symbols-intake-p09-recombination-native.csv"
P09_ITERATION = "registry/symbols-intake-p09-recombination-iteration.csv"
P18_SEARCH = "registry/symbols-intake-p18-erotetic-search.csv"
P18_NATIVE = "registry/symbols-intake-p18-erotetic-search-native.csv"
P10_ADEQUACY = "registry/symbols-intake-p10-operational-adequacy.csv"


def displayed_form(original: str, role: str, glyph: str) -> dict:
    return {"expect": (original, role), "glyph": glyph}


# Ported B7/B8 per-line normalizations (prepare_remaining_inventory.py), keyed by
# (stem, intake) and physical CSV line. Each applies only while the line still holds the
# recorded original glyph and role ("expect"); an edited intake is refused, never guessed.
# "requires": the native supplement that supersedes the row must be among the adopted intakes.
INTAKE_SPECIALS: dict[tuple[str, str], dict[int, dict]] = {
    ("p09-recombination-models", P09_MODELS): {
        2: displayed_form("V", "finite module or splicing alphabet", "V"),
        3: displayed_form("#", "first and second recognition-cut separator", r"\#"),
        4: displayed_form("$", "separator between the two splicing sites", r"\$"),
        5: displayed_form("u_i", "four rule handles", "u_i"),
        6: displayed_form("sigma", "H scheme and its language operation", r"\sigma"),
        7: displayed_form("vdash_r", "oriented splicing relation", r"\vdash_r"),
        8: {"expect": ("epsilon", "literal empty word"), "requires": P09_NATIVE,
            "inactive": "raw epsilon superseded by the restored native lambda record"},
        9: displayed_form("A/B", "right language quotient", "A/B"),
        10: displayed_form("B backslash A", "left language quotient", r"B\backslash A"),
        11: displayed_form("sigma star", "iterated least H-scheme closure", r"\sigma^*"),
        12: displayed_form("V_B", "module alphabet extended by branch brackets", "V_B"),
        13: {"expect": ("P H L U", "turtle position and orthonormal heading-left-up frame"),
             "glyph": "P,H,L,U",
             "role": "turtle position and orthonormal-frame symbol family",
             "members": [("P", "turtle position vector"), ("H", "orthonormal heading vector"),
                         ("L", "orthonormal left vector"), ("U", "orthonormal up vector")]},
        14: displayed_form("M", "parametric module set V times R star", "M"),
        15: displayed_form("G", "parametric OL-system tuple", "G"),
        16: displayed_form("E", "set of formal parameter names", "E"),
        17: displayed_form("omega", "nonempty parametric axiom", r"\omega"),
        18: displayed_form("P", "finite production set", "P"),
        19: displayed_form("h", "morphism induced by nonparametric DOL successors", "h"),
        20: displayed_form("pi", "stochastic production-factor map", r"\pi"),
        21: {"expect": ("N_k p_k",
                        "current apex count and conditional binary-branching probability"),
             "glyph": "N_k,p_k",
             "role": "apex-count and conditional-branching symbol family",
             "members": [("N_k", "current apex count"),
                         ("p_k", "conditional binary branching probability")]},
        22: displayed_form("sigma_min", "minimum exposed leaf area per viable shoot",
                           r"\sigma_{\min}"),
    },
    ("p09-recombination-iteration", P09_ITERATION): {
        13: {"expect": ("O_r C_r Q_r D_r", "explicit aliases for the four displayed bracket tokens"),
             "inactive": "old ASCII aliases superseded by native bracket records"},
        27: {"expect": ("L_k W_1 W_2 W",
                        "source radius witness and specific wrapper-separation languages"),
             "glyph": "L_k,W_1,W_2,W",
             "role": "radius-witness and wrapper-language symbol family", "family": True},
    },
    ("p18-erotetic-search", P18_SEARCH): {
        3: {"expect": (r"e \varphi_k", "Sequence and indexed occurrence"),
            "glyph": r"e,\varphi_k",
            "role": "Sequence and indexed occurrence symbol family", "family": True},
        4: {"expect": ("Q X", "Principal question and initial basis"), "glyph": "Q,X",
            "role": "Principal question and initial basis symbol family", "family": True},
        7: {"expect": (r"\mathcal B(A,B)", "Binary conjunctive question"), "requires": P18_NATIVE,
            "inactive": "editorial binary-question alias superseded by native supplement"},
        11: {"expect": ("Z Y", "Retained grounds and replaced basis"), "glyph": "Z,Y",
             "role": "Retained grounds and replaced basis symbol family", "family": True},
        13: {"expect": ("x_1 x_2 x_3", "Departure premise formula names"),
             "glyph": "x_1,x_2,x_3",
             "role": "Departure premise formula names symbol family", "family": True},
    },
    ("p10-operational-adequacy", P10_ADEQUACY): {
        29: {"expect": (r"\(\operatorname{succ}\)", "Gunter PCF numerical successor term constructor"),
             "same_as_previous": True,
             "inactive": "byte-identical repeated successor record after the preceding record"},
    },
}


def member_role(role: str, member: str) -> str:
    """A family member's role: the role is a text cell, so the member's TeX goes in math."""
    return role + r" member \(" + math_glyph(member) + r"\)"


def actual_row(row: dict, group: dict, rel: str, number: int,
               previous: dict | None = None,
               adopted_intakes: set[str] | None = None) -> tuple[dict, str | None]:
    """Ported B7/B8 intake normalizations from remaining inventory preparation.

    rel is the handbook-relative intake path; previous is the preceding line's original
    cells. Raises IntakeRowError when a recorded special no longer matches its line or a
    glyph's commas cannot be read safely.
    """
    row = copy.deepcopy(row)
    stem = group.get("stem", "")
    glyph = intake_glyph_body(row["glyph"])
    inactive = None
    members: list[tuple[str, str]] = []
    reasons: list[str] = []
    special = INTAKE_SPECIALS.get((stem, rel), {}).get(number)
    if special:
        expected_glyph, expected_role = special["expect"]
        if (row["glyph"], row["role"]) != (expected_glyph, expected_role) or (
                special.get("same_as_previous") and row != previous):
            raise IntakeRowError(
                f"line {number} no longer holds the row its recorded normalization was written "
                f"for (expected glyph {expected_glyph!r}, role {expected_role!r}"
                + (", identical to the previous line" if special.get("same_as_previous") else "")
                + "); the intake changed, so nothing is applied: update the special or the intake")
        required = special.get("requires")
        if required and required not in (adopted_intakes or set()):
            raise IntakeRowError(f"line {number} is superseded by the native intake {required}, "
                                 "which is not among the group's adopted intakes")
        inactive = special.get("inactive")
        glyph = special.get("glyph", glyph)
        row["role"] = special.get("role", row["role"])
        if special.get("members"):
            members = list(special["members"])
        elif special.get("family"):
            members = [(x, member_role(row["role"], x)) for x in family_members(glyph)]
        elif "glyph" in special:
            reasons.append("Actual displayed reader TeX form, not the raw ASCII alias.")
    if stem == "p09-recombination-iteration" and rel == P09_ITERATION and glyph == "$":
        glyph = r"\$"
    if inactive:
        return row, inactive
    parts = family_members(glyph)
    if not members and len(parts) > 1:
        row["role"] += " symbol family"
        members = [(x, member_role(row["role"], x)) for x in parts]
        reasons.append("Explicit displayed family; member types and common actual first-use exposed, not one atomic glyph.")
    # A family's glyph is its members' bodies, each checked on its own (a lone # or &
    # member is escaped like a lone-character glyph).
    body = ",".join(math_glyph(part) for part in parts) if len(parts) > 1 else math_glyph(glyph)
    row["glyph"] = r"\(" + body + r"\)"
    row["_macro_filled"] = not row.get("macro")
    if row["_macro_filled"]:
        row["macro"] = body
        reasons.append(MACRO_FILL_NOTE)
    elif macro_problem(row["macro"]):
        raise IntakeRowError("macro " + repr(row["macro"]) + " " + macro_problem(row["macro"]))
    if not registry.PREC_RE.fullmatch(row.get("precedence", "")):
        old = row.get("precedence", "")
        row["precedence"] = "n/a"
        append_note(row, "Original precedence descriptor " + repr(old) + " retained; no rank inferred.")
    if is_sequence_glyph(glyph):
        reasons.append("Sequence glyph kept as one row; the ellipsis is not a member symbol.")
    if reasons:
        append_note(row, " ".join(reasons))
    if members:
        append_note(row, "Family listing, not one atomic glyph.")
        if not row["_macro_filled"]:
            # Each member takes its own TeX spelling; the author's macro is not lost silently.
            # Shown literally, as the macro column is (it may be undefined in handbook.sty).
            shown = (" " + symbols2tex.macro_code(row["macro"])
                     if row["macro"].isascii() and not macro_problem(row["macro"]) else "")
            append_note(row, "Author macro" + shown + " not carried to the members.")
        # Members take every other field (scope, first_use, ...) from the row at expansion.
        row["_members"] = [{"glyph": r"\(" + math_glyph(g) + r"\)", "macro": math_glyph(g),
                            "role": role} for g, role in members]
    return row, inactive


def repair_csv_text(text: str) -> str:
    fixed: list[str] = []
    for line in io.StringIO(text, newline="\n").readlines():
        match = re.match(r"^(\\\(.*?\\\)),", line)
        if match and "," in match.group(1):
            line = '"' + match.group(1).replace('"', '""') + '",' + line[match.end():]
        fixed.append(line)
    return "".join(fixed)


def tex_balanced(value: str) -> bool:
    depth = 0
    escaped = False
    for ch in value:
        if escaped:
            escaped = False
            continue
        if ch == "\\":
            escaped = True
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


def repair_csv_cells(cells: list[str]) -> list[str] | None:
    """Rejoin cells split at an unquoted comma inside TeX braces; None (a CSV parse
    failure) when the row still does not have exactly one cell per column."""
    if len(cells) == len(FIELDS):
        return cells
    result: list[str] = []
    index = 0
    while index < len(cells):
        field = cells[index]
        index += 1
        while not tex_balanced(field) and index < len(cells):
            field += "," + cells[index]
            index += 1
        result.append(field)
    return result if len(result) == len(FIELDS) else None


SELECTOR_ROW_KEYS = {"glyph", "macro", "role", "scope", "first_use"}
SELECTOR_CONTROL_KEYS = {"row", "fields", "set", "reason", "multi_match"}
SELECTOR_KEYS = {
    "group", "stem", "line", "record_number", "intake",
    *SELECTOR_ROW_KEYS, *SELECTOR_CONTROL_KEYS,
}


def selector_unknown_keys(selector: dict) -> set[str]:
    return set(selector) - SELECTOR_KEYS


def selector_allows_multi_match(selector) -> bool:
    return isinstance(selector, dict) and selector.get("multi_match") is True


def selector_value_matches(key: str, expected, actual) -> bool:
    if key in {"line", "record_number"}:
        return str(expected) == str(actual)
    return expected == actual


def row_matches_selector(row: dict, selector) -> bool:
    if selector is None:
        return False
    if isinstance(selector, str):
        return selector in {row.get("_group", "") + ":" + str(row.get("_line", "")),
                            row.get("_group", "") + ":" + row_id(row)}
    if not isinstance(selector, dict):
        return False
    if selector_unknown_keys(selector):
        return False
    nested = selector.get("row")
    if nested is not None:
        if not isinstance(nested, dict) or any(key not in FIELDS for key in nested):
            return False
        if any(row.get(k) != v for k, v in nested.items()):
            return False
    checks = {
        "group": row.get("_group"),
        "stem": row.get("_group"),
        "line": row.get("_line"),
        "record_number": row.get("_line"),
        "intake": row.get("_intake"),
        "glyph": row.get("glyph"),
        "macro": row.get("macro"),
        "role": row.get("role"),
        "scope": row.get("scope"),
        "first_use": row.get("first_use"),
    }
    for key, actual in checks.items():
        if key in selector and not selector_value_matches(key, selector[key], actual):
            return False
    return True


def selector_shape_error(selector, context: str) -> str | None:
    if isinstance(selector, str):
        if context != "incoming":
            return "string selectors are only valid for incoming rows"
        if not selector.strip():
            return "empty selector string"
        return None
    if not isinstance(selector, dict):
        return "selector must be an object or incoming group:line string"
    unknown = selector_unknown_keys(selector)
    if unknown:
        return "unknown selector key(s): " + ", ".join(sorted(unknown))
    nested = selector.get("row")
    if nested is not None:
        if not isinstance(nested, dict):
            return "row selector must be an object"
        unknown_nested = set(nested) - set(FIELDS)
        if unknown_nested:
            return "unknown row selector key(s): " + ", ".join(sorted(unknown_nested))
    for field_key in ("fields", "set"):
        if field_key not in selector:
            continue
        fields = selector[field_key]
        if not isinstance(fields, dict):
            return f"{field_key} must be an object"
        unknown_fields = set(fields) - set(FIELDS)
        if unknown_fields:
            return f"unknown {field_key} field(s): " + ", ".join(sorted(unknown_fields))
        if not all(isinstance(value, str) for value in fields.values()):
            return f"{field_key} values must be strings"
    nested_keys = set(nested or {})
    has_line = "line" in selector or "record_number" in selector
    if context == "incoming":
        has_group = "group" in selector or "stem" in selector
        if not (has_group and has_line):
            return "incoming selectors must identify one row by group/stem and line/record_number"
    elif context == "canonical":
        exact = all(key in selector or key in nested_keys for key in ("glyph", "role", "scope"))
        if not has_line and not exact:
            return "canonical selectors must identify by line/record_number or exact glyph+role+scope"
    else:
        return "unknown selector context " + context
    return None


def selector_match_errors(name: str, selectors: list, rows: list[dict],
                          context: str) -> list[dict]:
    errors: list[dict] = []
    for index, selector in enumerate(selectors):
        shape_error = selector_shape_error(selector, context)
        if shape_error:
            errors.append({
                "kind": "invalid-selector",
                "decision": name,
                "index": index,
                "selector": selector,
                "error": shape_error,
            })
            continue
        matches = [row for row in rows if row_matches_selector(row, selector)]
        if not matches:
            errors.append({
                "kind": "selector-match-count",
                "decision": name,
                "index": index,
                "selector": selector,
                "matches": 0,
                "error": "selector matched no rows",
            })
        elif len(matches) > 1 and not selector_allows_multi_match(selector):
            errors.append({
                "kind": "selector-match-count",
                "decision": name,
                "index": index,
                "selector": selector,
                "matches": len(matches),
                "error": "selector matched more than one row",
            })
    return errors


def validate_decision_selectors(decisions: dict, incoming_rows: list[dict],
                                canonical_rows: list[dict]) -> list[dict]:
    errors: list[dict] = []
    errors.extend(selector_match_errors(
        "row_edits", decisions.get("row_edits", []), incoming_rows, "incoming"
    ))
    errors.extend(selector_match_errors(
        "drop_rows", decisions.get("drop_rows", []), incoming_rows, "incoming"
    ))
    canonical_for_matching = []
    for line, row in enumerate(canonical_rows, 2):
        item = copy.deepcopy(row)
        item["_line"] = line
        canonical_for_matching.append(item)
    errors.extend(selector_match_errors(
        "canonical_row_edits", decisions.get("canonical_row_edits", []),
        canonical_for_matching, "canonical"
    ))
    return errors


def apply_row_edits(row: dict, decisions: dict, edited: set[str] | None = None) -> list[str]:
    """Apply matching row_edits to row; their reasons. edited collects the fields set."""
    changes: list[str] = []
    for edit in decisions.get("row_edits", []):
        if not row_matches_selector(row, edit):
            continue
        fields = edit.get("fields") or edit.get("set") or {}
        for key, value in fields.items():
            if key in FIELDS:
                row[key] = value
                if edited is not None:
                    edited.add(key)
        reason = edit.get("reason", "decision row edit")
        changes.append(reason)
    return changes


def row_is_dropped(row: dict, decisions: dict) -> bool:
    return any(row_matches_selector(row, selector) for selector in decisions.get("drop_rows", []))


FAMILY_FIELDS = ("glyph", "macro", "role")


def apply_incoming_row_decisions(rows: list[dict], decisions: dict) -> list[dict]:
    """Apply row_edits and drop_rows to incoming rows.

    A family row (one intake line listing several glyphs) expands into member rows
    that inherit the edited row's other fields. An edit of its glyph, macro or role
    cannot say which member it means, so it is an error; a glyph edit that would
    turn a single row into a family is an error too.
    """
    errors: list[dict] = []
    for row in rows:
        if row.get("_pre_edited"):
            continue  # a refused intake row already re-read with its row_edits
        before = {key: row.get(key) for key in FAMILY_FIELDS}
        edited: set[str] = set()
        for reason in apply_row_edits(row, decisions, edited):
            row["_changes"].append(reason)
            append_note(row, reason)
        if "macro" in edited and row.get("_macro_filled"):
            # An edit sets the macro itself: the fill note no longer describes it.
            row["_macro_filled"] = False
            row["notes"] = " ".join(row.get("notes", "").replace(MACRO_FILL_NOTE, "").split())
        becomes_family = False
        if row.get("glyph") != before["glyph"]:
            # An edited glyph takes the same path as an intake glyph: wrap + math_glyph.
            try:
                body = intake_glyph_body(row["glyph"])
                becomes_family = len(family_members(body)) > 1
                if not becomes_family:
                    row["glyph"] = r"\(" + math_glyph(body) + r"\)"
                    if row.get("_macro_filled"):
                        # The macro was filled from the old glyph: fill it from the new one.
                        row["macro"] = math_glyph(body)
            except IntakeRowError as exc:
                errors.append({"group": row.get("_group"), "intake": row.get("_intake"),
                               "line": row.get("_line"), "kind": "row-edit-glyph",
                               "error": str(exc)})
        if row.get("macro") != before["macro"] and macro_problem(row.get("macro") or ""):
            errors.append({"group": row.get("_group"), "intake": row.get("_intake"),
                           "line": row.get("_line"), "kind": "row-edit-macro",
                           "error": "macro " + repr(row["macro"]) + " "
                                    + macro_problem(row["macro"])})
        changed = [key for key in FAMILY_FIELDS if row.get(key) != before[key]]
        if changed and (row.get("_members") or becomes_family):
            errors.append({"group": row.get("_group"), "intake": row.get("_intake"),
                           "line": row.get("_line"), "kind": "family-row-edit",
                           "fields": changed,
                           "error": "row_edits may not change glyph, macro or role of a symbol "
                                    "family row; its members are derived from the intake line"})
        if row_is_dropped(row, decisions):
            row["_dropped"] = True
    return errors


def finalize_incoming_rows(rows: list[dict], index: registry.ReaderIndex,
                           old_tuples: set[tuple[str, ...]],
                           existing_scope_names: set[str] | None = None) -> list[dict]:
    errors: list[dict] = []
    existing_scope_names = existing_scope_names or set()
    for row in rows:
        if not row.get("_inactive") and not row.get("_dropped"):
            errors.extend(numeric_row_errors(row, existing_scope_names))
            if not registry.FIRST_RE.fullmatch(row["first_use"]):
                try:
                    index.unique(row["first_use"])
                except registry.RegistryError as exc:
                    errors.append({"group": row.get("_group"), "intake": row.get("_intake"),
                                   "line": row.get("_line"), "error": str(exc),
                                   "first_use": row["first_use"]})
        if row.get("_members"):
            # A family is written as its member rows: each is compared with canonical.
            for member in row["_members"]:
                member["_already_merged"] = row_tuple({**row, **member}) in old_tuples
            row["_already_merged"] = (all(m["_already_merged"] for m in row["_members"])
                                      or row_tuple(row.get("_original", {})) in old_tuples)
        else:
            row["_already_merged"] = (
                row_tuple(row) in old_tuples or row_tuple(row.get("_original", {})) in old_tuples
            )
    return errors


def nonascii_glyph_decisions(rows: list[dict]) -> list[dict]:
    r"""Rows to be merged whose glyph (or a family member's) has non-ASCII characters outside
    \text{...}; math fonts may lack them. A row_edits glyph fix or drop_rows covers it."""
    needed: list[dict] = []
    for row in rows:
        if row.get("_inactive") or row.get("_dropped") or row.get("_already_merged"):
            continue
        members = [m for m in row.get("_members", []) if not m.get("_already_merged")]
        glyphs = [member["glyph"] for member in members] or [row["glyph"]]
        found = sorted({ch for glyph in glyphs for ch in nonascii_math_characters(unwrap_glyph(glyph))})
        if found:
            needed.append({"kind": "glyph-non-ascii-math", "group": row.get("_group"),
                           "intake": row.get("_intake"), "line": row.get("_line"),
                           "glyph": row["glyph"], "characters": found,
                           "error": "non-ASCII character in math outside \\text{...}; give its "
                                    "TeX command (row_edits) or drop the row"})
        # A filled macro is the glyph's own spelling: the glyph decision above covers it
        # (a row_edits glyph fix re-fills it), and so do family members' macros.
        macros = [] if members or row.get("_macro_filled") else [row.get("macro", "")]
        found = sorted({ch for macro in macros for ch in macro if not ch.isascii()})
        if found:
            needed.append(dict(nonascii_macro_decision(row.get("macro", ""), found),
                               group=row.get("_group"), intake=row.get("_intake"),
                               line=row.get("_line")))
    return needed


def nonascii_macro_decision(macro: str, found: list[str]) -> dict:
    r"""A non-ASCII macro cell renders as mojibake in the table's \texttt{\detokenize{...}}."""
    return {"kind": "macro-non-ascii", "macro": macro, "characters": found,
            "error": "non-ASCII character in the macro cell (\\detokenize shows its raw bytes); "
                     "give its TeX command (row_edits / canonical_row_edits) or drop the row"}


def heading_label_for(index: registry.ReaderIndex, heading) -> str | None:
    candidates = []
    for label, sites in index.labels.items():
        for site in sites:
            if site.path == heading.path and site.start == heading.start and site.kind == heading.kind:
                candidates.append(label)
    if candidates:
        return sorted(candidates)[0]
    return None


def local_regions_for_first_use(index: registry.ReaderIndex, first: str,
                                group: dict) -> tuple[list[dict], list[dict]]:
    """Binding regions for a first_use in a group's own files, and items needing a decision.

    A body first_use binds its innermost heading region plus every annex item in the
    group's own annexes whose owner result lies in that region. An annex first_use binds
    its item and the item's owner result when the group owns the owner's file.

    Not bound, returned as {kind, anchor or selector, path, ...} for a decision (covered
    by an extend_scopes entry listing that selector): an owned item sitting in another
    annex file, an annex first_use's owner in a file the group does not own, an item
    whose owner label is ambiguous, and a heading region that runs on into a following
    file the group does not own.
    """
    declaration = index.unique(first)
    owned = {tex_rel(rel) for rel in owned_rels(group)}
    if not owned:
        raise registry.RegistryError("group owns no files; cannot synthesize binding")
    if declaration.path not in owned:
        raise registry.RegistryError("first_use outside group-owned files: " + declaration.path)
    if declaration.path.startswith("annex/"):
        selectors = [{"anchor": declaration.label}]
        if not declaration.owner:
            return selectors, []
        owners = index.labels.get(declaration.owner, [])
        if len(owners) != 1:
            return selectors, [{"kind": "binding-annexitem-owner-ambiguous",
                                "anchor": declaration.owner, "item": declaration.label,
                                "owner_sites": [site.path for site in owners]}]
        if owners[0].path not in owned:
            return selectors, [{"kind": "binding-foreign-owner", "anchor": declaration.owner,
                                "path": owners[0].path, "item": declaration.label}]
        return selectors + [{"anchor": declaration.owner}], []
    if declaration.path.startswith("registry/"):
        # A \calculussheet / \hbrule in an owned rule sheet binds the whole sheet file.
        return [{"file": declaration.path}], []
    headings = [h for h in index.heading_records
                if h.path == declaration.path and h.start <= declaration.start < h.end]
    heading = max(headings, key=lambda h: h.start) if headings else None
    if heading:
        label = heading_label_for(index, heading) or first
        selectors = [{"heading_of": label, "level": heading.kind}]
    else:
        selectors = [{"anchor": first}]
    region = index.region(selectors[0])
    owned_annexes = {tex_rel(rel) for rel in group.get("annexes", [])}
    foreign: list[dict] = []
    if heading:
        # A heading region closes only at the next heading of its level or above, so it
        # may run on over files that follow the group's own. A following file adds nothing
        # when the closing heading (at position region.end) is its own first heading:
        # only commands before it, such as a wrapper environment, fall in the region.
        heading_starts = sorted(h.start for h in index.heading_records)

        def runs_on(fr) -> bool:
            if not heading.start < fr.start < region.end - 1:
                return False
            later = heading_starts[bisect_right(heading_starts, fr.start):]
            return not (later and later[0] == region.end < fr.end)

        spill = sorted({rel for rel, file_regions in index.files.items() if rel not in owned
                        for fr in file_regions if runs_on(fr)})
        if spill:
            foreign.append({"kind": "binding-heading-spill", "selector": selectors[0],
                            "paths": spill})
    for sites in index.labels.values():
        for annex in sites:
            if annex.kind != "annexitem" or not annex.owner:
                continue
            owners = index.labels.get(annex.owner, [])
            if not any(region.start <= owner.start < region.end for owner in owners):
                continue
            selector = {"anchor": annex.label}
            if len(owners) != 1:
                item = {"kind": "binding-annexitem-owner-ambiguous", **selector,
                        "path": annex.path, "owner": annex.owner,
                        "owner_sites": [site.path for site in owners]}
            elif annex.path not in owned_annexes:
                item = {"kind": "binding-foreign-annexitem", **selector, "path": annex.path}
            else:
                if selector not in selectors:
                    selectors.append(selector)
                continue
            if item not in foreign:
                foreign.append(item)
    return selectors, foreign


def selector_key(selector: dict) -> str:
    return json.dumps(selector, sort_keys=True, ensure_ascii=False)


def decided_selectors(decisions: dict, scope: str) -> set[str]:
    """selector_key of every region an extend_scopes decision lists for scope."""
    return {selector_key(s) for item in decisions.get("extend_scopes", [])
            if isinstance(item, dict) and item.get("scope") == scope
            for s in item.get("regions", []) if isinstance(s, dict)}


def merge_decision_scope_extensions(scopes: dict, decisions: dict,
                                    canonical: dict) -> tuple[dict, list[dict]]:
    """Apply extend_scopes and overrides. A scope already in canonical keeps its
    presentation: a differing one is an error (extending only adds regions or rules)."""
    result = copy.deepcopy(scopes)
    errors: list[dict] = []

    def set_presentation(kind: str, name: str, binding: dict, item: dict) -> None:
        wanted = item.get("presentation")
        if not wanted or wanted == binding.get("presentation"):
            return
        if name in canonical:
            errors.append({"kind": "decision-scope-presentation", "decision": kind,
                           "scope": name, "error": "decision would rewrite the presentation "
                                                   "of an existing canonical scope"})
            return
        binding["presentation"] = wanted
    for item in decisions.get("extend_scopes", []):
        name = item.get("scope")
        if not name:
            continue
        binding = result.setdefault(name, {
            "presentation": item.get("presentation", "Decision-supplied scope extension."),
            "regions": [],
        })
        set_presentation("extend_scopes", name, binding, item)
        seen = {selector_key(s) for s in binding.get("regions", [])}
        for selector in item.get("regions", []):
            key = selector_key(selector)
            if key not in seen:
                binding.setdefault("regions", []).append(selector)
                seen.add(key)
    for item in decisions.get("overrides", []):
        name = item.get("scope") or item.get("name")
        rule = item.get("rule")
        if not name or not rule:
            continue
        binding = result.setdefault(name, {
            "presentation": item.get("presentation", "Decision-supplied override scope."),
            "regions": item.get("regions", []),
        })
        set_presentation("overrides", name, binding, item)
        if item.get("regions") and not binding.get("regions"):
            binding["regions"] = item["regions"]
        rules = binding.setdefault("overrides", [])
        if rule not in rules:
            rules.append(rule)
    return result, errors


def apply_canonical_row_edits(rows: list[dict], decisions: dict) -> tuple[list[dict], list[dict]]:
    """Canonical rows with canonical_row_edits applied, and errors. An edited glyph is
    normalized like an intake glyph (one glyph, wrapped, math_glyph-checked)."""
    edited = []
    errors: list[dict] = []
    for number, original in enumerate(rows, 2):
        row = copy.deepcopy(original)
        row["_line"] = number
        for edit in decisions.get("canonical_row_edits", []):
            if row_matches_selector(row, edit):
                for key, value in (edit.get("fields") or edit.get("set") or {}).items():
                    if key in FIELDS:
                        row[key] = value
        if row.get("glyph") != original.get("glyph"):
            try:
                body = intake_glyph_body(row["glyph"])
                if len(family_members(body)) > 1:
                    raise IntakeRowError("canonical_row_edits may not turn a row into a symbol "
                                         "family: " + repr(row["glyph"]))
                row["glyph"] = r"\(" + math_glyph(body) + r"\)"
            except IntakeRowError as exc:
                errors.append({"kind": "canonical-row-edit-glyph", "line": number,
                               "error": str(exc)})
        if row.get("macro") != original.get("macro") and macro_problem(row.get("macro") or ""):
            errors.append({"kind": "canonical-row-edit-macro", "line": number,
                           "error": "macro " + repr(row["macro"]) + " "
                                    + macro_problem(row["macro"])})
        edited.append(row)
    return edited, errors


def csv_rows_text(rows: list[dict], *, header: bool = False) -> str:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=FIELDS, lineterminator="\n")
    if header:
        writer.writeheader()
    for row in rows:
        writer.writerow({key: row.get(key, "") for key in FIELDS})
    return stream.getvalue()


def symbols_csv_text_preserving(original_text: str, original_rows: list[dict],
                                edited_rows: list[dict],
                                appended_rows: list[dict]) -> str | None:
    lines = io.StringIO(original_text, newline="\n").readlines()  # breaks at "\n" only, like csv
    expected_lines = len(original_rows) + 1
    if len(lines) != expected_lines:
        raise Refusal(
            "symbols.csv physical line count does not match parsed row count; "
            "refusing whole-file rewrite"
        )
    changed = False
    for offset, (original, edited) in enumerate(zip(original_rows, edited_rows), 1):
        if row_tuple(original) == row_tuple(edited):
            continue
        lines[offset] = csv_rows_text([edited], header=False)
        changed = True
    text = "".join(lines)
    if appended_rows:
        if text and not text.endswith("\n"):
            text += "\n"
        text += csv_rows_text(appended_rows, header=False)
        changed = True
    return text if changed else None


def matching_json_object_end(text: str, start: int) -> int:
    if start >= len(text) or text[start] != "{":
        raise Refusal("expected JSON object")
    depth = 0
    in_string = False
    escaped = False
    for index in range(start, len(text)):
        ch = text[index]
        if in_string:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return index
    raise Refusal("unbalanced JSON object")


def scopes_object_bounds(text: str) -> tuple[int, int]:
    match = re.search(r'"scopes"\s*:', text)
    if not match:
        raise Refusal("symbol-scopes.json has no scopes object")
    start = text.find("{", match.end())
    if start < 0:
        raise Refusal("symbol-scopes.json scopes value is not an object")
    return start, matching_json_object_end(text, start)


def skip_json_space(text: str, index: int, end: int) -> int:
    while index < end and text[index].isspace():
        index += 1
    return index


def json_object_members(text: str, object_start: int, object_end: int) -> dict[str, dict]:
    decoder = json.JSONDecoder()
    members: dict[str, dict] = {}
    index = object_start + 1
    while True:
        index = skip_json_space(text, index, object_end)
        if index >= object_end:
            break
        if text[index] == ",":
            index += 1
            continue
        if text[index] != '"':
            raise Refusal("invalid JSON object member in symbol-scopes.json")
        key_start = index
        key, offset = decoder.raw_decode(text[index:])
        if not isinstance(key, str):
            raise Refusal("non-string scope key in symbol-scopes.json")
        index += offset
        index = skip_json_space(text, index, object_end)
        if index >= object_end or text[index] != ":":
            raise Refusal("missing colon after scope key in symbol-scopes.json")
        index += 1
        index = skip_json_space(text, index, object_end)
        _value, offset = decoder.raw_decode(text[index:])
        value_end = index + offset
        if key in members:
            raise Refusal("duplicate scope key in symbol-scopes.json: " + key)
        members[key] = {"start": key_start, "end": value_end,
                        "raw": text[key_start:value_end]}
        index = value_end
    return members


def line_indent_before(text: str, index: int) -> str:
    """Leading whitespace of the line containing index."""
    start = text.rfind("\n", 0, index) + 1
    return re.match(r"[ \t]*", text[start:index]).group(0)


def compact_scope_member(key: str, value: dict, indent: str) -> str:
    return (
        indent
        + json.dumps(key, ensure_ascii=False)
        + ": "
        + json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    )


def scopes_json_text_preserving(original_text: str, old_doc: dict,
                                new_doc: dict) -> str | None:
    old_scopes = old_doc.get("scopes", {})
    new_scopes_doc = new_doc.get("scopes", {})
    removed = set(old_scopes) - set(new_scopes_doc)
    if removed:
        raise Refusal("scope deletion refused: " + ", ".join(sorted(removed)))
    object_start, object_end = scopes_object_bounds(original_text)
    members = json_object_members(original_text, object_start, object_end)
    if set(members) != set(old_scopes):
        raise Refusal("symbol-scopes.json parsed keys differ from canonical JSON")
    if members:
        first_start = min(item["start"] for item in members.values())
        member_indent = line_indent_before(original_text, first_start)
    else:
        object_indent = line_indent_before(original_text, object_start)
        member_indent = object_indent + "  "
    operations: list[tuple[int, int, str]] = []
    for key, value in new_scopes_doc.items():
        if key not in old_scopes or old_scopes[key] == value:
            continue
        member = members.get(key)
        if member is None:
            raise Refusal("changed scope member not found in canonical text: " + key)
        operations.append((member["start"], member["end"],
                           compact_scope_member(key, value, "")))
    appended = [
        compact_scope_member(key, value, member_indent)
        for key, value in new_scopes_doc.items()
        if key not in old_scopes
    ]
    if appended:
        if members:
            last_end = max(item["end"] for item in members.values())
            operations.append((last_end, last_end, ",\n" + ",\n".join(appended)))
        else:
            object_indent = line_indent_before(original_text, object_start)
            operations.append((object_start + 1, object_start + 1,
                               "\n" + ",\n".join(appended) + "\n" + object_indent))
    if not operations:
        return None
    result = original_text
    for start, end, replacement in sorted(operations, key=lambda item: item[0], reverse=True):
        result = result[:start] + replacement + result[end:]
    try:
        parsed = json.loads(result)
    except json.JSONDecodeError as exc:
        raise Refusal("scope text merge produced invalid JSON: " + str(exc)) from exc
    if parsed != new_doc:
        raise Refusal("scope text merge did not produce the requested JSON document")
    return result


def read_symbol_intake(path: Path, rel: str, group: dict,
                       adopted_intakes: set[str]) -> tuple[list[dict], list[dict], list[dict]]:
    """Rows, errors and inactive dispositions of one intake (rel is handbook-relative)."""
    errors: list[dict] = []
    inactive: list[dict] = []
    rows: list[dict] = []
    try:
        text = repair_csv_text(read_text(path))
        reader = csv.reader(io.StringIO(text))
        header = next(reader, None)
    except csv.Error as exc:
        return [], [{"group": group.get("stem"), "intake": rel, "error": str(exc)}], []
    if header != FIELDS:
        return [], [{"group": group.get("stem"), "intake": rel, "error": "bad CSV header",
                     "header": header}], []
    previous = None
    for line, cells in enumerate(reader, 2):
        repaired = repair_csv_cells(cells)
        if repaired is None:
            errors.append({"group": group.get("stem"), "intake": rel, "line": line,
                           "error": "CSV parse failure"})
            previous = None
            continue
        raw = dict(zip(FIELDS, repaired))
        original = {key: (raw.get(key) or "").strip() for key in FIELDS}
        try:
            row, disposition = actual_row(original, group, rel, line, previous, adopted_intakes)
        except IntakeRowError as exc:
            # Kept as a raw-cell placeholder, so drop_rows and row_edits can select it by
            # group+line; resolve_refused_rows drops, re-reads or reports it.
            rows.append(dict(original, _group=group.get("stem"), _intake=rel, _line=line,
                             _original=copy.deepcopy(original), _changes=[], _refused=str(exc),
                             _previous=previous, _adopted_intakes=adopted_intakes))
            previous = original
            continue
        previous = original
        row.update(_group=group.get("stem"), _intake=rel, _line=line,
                   _original=copy.deepcopy(original), _changes=[])
        if disposition:
            inactive.append({"group": group.get("stem"), "intake": rel, "line": line,
                             "row": original, "reason": disposition})
            row["_inactive"] = True
        rows.append(row)
    return rows, errors, inactive


def refused_row_error(row: dict, cells: dict, reason: str) -> dict:
    return {"group": row.get("_group"), "intake": row.get("_intake"), "line": row.get("_line"),
            "kind": "intake-row-refused", "row": cells,
            "error": f"intake row refused (raw glyph cell {cells.get('glyph', '')!r}, macro cell "
                     f"{cells.get('macro', '')!r}): {reason}. Remedy: a row_edits entry for group "
                     f"{row.get('_group')} line {row.get('_line')} (its glyph replaces the raw "
                     "cell and is then normalized), drop_rows for that row, or return the group "
                     "for fix (unroute)"}


def resolve_refused_rows(rows: list[dict], decisions: dict) -> tuple[list[dict], list[dict], list[dict]]:
    """Refused intake rows: dropped by drop_rows, re-read from the raw cells with their
    row_edits applied, or reported. Returns (rows, errors, inactive dispositions)."""
    kept: list[dict] = []
    errors: list[dict] = []
    inactive: list[dict] = []
    for row in rows:
        if not row.get("_refused"):
            kept.append(row)
            continue
        if row_is_dropped(row, decisions):
            row["_dropped"] = True  # skipped by every later step, like any dropped row
            kept.append(row)
            continue
        probe = copy.deepcopy(row)
        reasons = apply_row_edits(probe, decisions)
        cells = {key: probe.get(key, "") for key in FIELDS}
        if not reasons:
            errors.append(refused_row_error(row, cells, row["_refused"]))
            continue
        try:
            new, disposition = actual_row(cells, {"stem": row.get("_group")}, row.get("_intake", ""),
                                          row.get("_line"), row.get("_previous"),
                                          row.get("_adopted_intakes"))
        except IntakeRowError as exc:
            errors.append(refused_row_error(row, cells, str(exc) + " (after its row_edits)"))
            continue
        new.update(_group=row.get("_group"), _intake=row.get("_intake"), _line=row.get("_line"),
                   _original=copy.deepcopy(row["_original"]), _changes=list(reasons),
                   _pre_edited=True)
        for reason in reasons:
            append_note(new, reason)
        if disposition:
            new["_inactive"] = True
            inactive.append({"group": row.get("_group"), "intake": row.get("_intake"),
                             "line": row.get("_line"), "row": cells, "reason": disposition})
        kept.append(new)
    return kept, errors, inactive


def copy_group_for_adopt(group: dict, owner: Path) -> dict:
    copied = copy.deepcopy(group)
    copied["_manifest_path"] = owner.resolve().as_posix()
    return copied


def owned_rels(group: dict) -> list[str]:
    return group.get("bodies", []) + group.get("annexes", []) + group.get("rule_sheets", [])


def ownership_decisions(groups: list[dict], base: Path, allowed: set[str]) -> list[dict]:
    r"""Owned files must be disjoint across groups, and an owned file may \input only
    files its own group owns. A file claimed twice, or a shared route host such as
    parts/pNN.tex, would put one group's citation rewrites and bindings over text that
    is not its own. allowed lists handbook-relative paths a decision lets through."""
    owners: dict[str, list[str]] = {}
    for group in groups:
        for rel in owned_rels(group):
            try:
                rel_norm = resolve_handbook_path(base, rel, tex=True)[1]
            except Refusal:
                continue  # reported by the owned-file checks
            stems = owners.setdefault(rel_norm, [])
            if group.get("stem") not in stems:
                stems.append(group.get("stem"))
    needed: list[dict] = []
    for rel, stems in sorted(owners.items()):
        if rel in allowed:
            continue
        if len(stems) > 1:
            needed.append({"kind": "owned-file-shared-across-groups", "path": rel, "groups": stems,
                           "error": "several selected groups own this file; each group's citation "
                                    "rewrites and bindings would apply to the others' text "
                                    "(allow_shared_owned_files covers a deliberate share)"})
        path = base / rel
        if not path.is_file():
            continue
        own = {r for r, s in owners.items() if set(s) & set(stems)}
        foreign = sorted({target for target in (normalized_input(base, item)
                                                for item in iter_inputs(read_text(path)))
                          if target and target not in own})
        if foreign:
            needed.append({"kind": "owned-file-is-shared-route-host", "path": rel, "groups": stems,
                           "routes": foreign,
                           "error": "an owned file routes files its group does not own; a route "
                                    "host such as parts/pNN.tex is shared, not group-owned "
                                    "(allow_shared_owned_files covers a deliberate claim)"})
    return needed


ADOPT_ROUTED_STATUS = "routed-awaiting-canonical-merge"
ADOPT_SKIPPED_STATUSES = {"saved-off-route", "frozen-unrouted", "active-authoring"}
# Only a collected or returned-for-fix group is promoted to routed by route --apply.
ROUTE_PROMOTABLE_STATUSES = {"returned", "returned-for-fix"}


def groups_for_adopt(manifest_path: Path, manifest: dict) -> tuple[list[dict], list[dict], dict[Path, str]]:
    """Select routed groups from the manifest and its declared prior_manifest only.

    Returns the selected groups, an error for every manifest group that is neither
    routed nor skipped (merged*, saved-off-route, frozen-unrouted, active-authoring),
    and the exact text of each prior manifest read. The manifest's own status for a
    stem wins over the prior manifest's (an unroute quarantine there stays in force).
    The prior manifest contributes only its routed groups.

    Each source_native_repairs[].supplement (of either manifest) is added to its
    group's symbol_intakes, as prepare_remaining_inventory.py did.
    """
    groups: list[dict] = []
    errors: list[dict] = []
    texts: dict[Path, str] = {}
    own_stems = {group.get("stem") for group in manifest.get("groups", [])}
    seen: set[str] = set()
    prior_manifest: dict = {}
    prior = manifest.get("prior_manifest")
    if prior:
        prior_path = repo_file(prior)
        if not prior_path.is_file():
            raise Refusal(f"prior_manifest {prior} does not exist")
        prior_manifest, texts[prior_path.resolve()] = read_manifest(prior_path)
        for group in prior_manifest.get("groups", []):
            stem = group.get("stem")
            if (group.get("integration_status") == ADOPT_ROUTED_STATUS
                    and stem not in own_stems and stem not in seen):
                groups.append(copy_group_for_adopt(group, prior_path))
                seen.add(stem)
    for group in manifest.get("groups", []):
        stem = group.get("stem")
        status = group.get("integration_status") or ""
        if stem in seen or status.startswith("merged") or status in ADOPT_SKIPPED_STATUSES:
            continue
        seen.add(stem)
        if status != ADOPT_ROUTED_STATUS and accounting_only(group):
            continue  # nothing to adopt
        if status != ADOPT_ROUTED_STATUS:
            errors.append({"group": stem, "kind": "group-not-routed", "integration_status": status,
                           "error": "Not confirmed actual incoming route: only "
                                    + ADOPT_ROUTED_STATUS + " groups are adopted"})
            continue
        groups.append(copy_group_for_adopt(group, manifest_path))
    errors.extend(add_native_supplements(groups, [manifest, prior_manifest]))
    return groups, errors, texts


def add_native_supplements(groups: list[dict], manifests: list[dict]) -> list[dict]:
    """Add each source_native_repairs supplement to its selected group's symbol_intakes."""
    errors: list[dict] = []
    by_stem = {group.get("stem"): group for group in groups}
    known = {group.get("stem") for manifest in manifests for group in manifest.get("groups", [])}
    for manifest in manifests:
        repairs = manifest.get("source_native_repairs", [])
        if not isinstance(repairs, list) or not all(isinstance(item, dict) for item in repairs):
            errors.append({"kind": "invalid-source-native-repairs",
                           "error": "source_native_repairs must be a list of objects"})
            continue
        for repair in repairs:
            stem, supplement = repair.get("stem"), repair.get("supplement")
            if not supplement:
                continue
            if stem not in known:
                errors.append({"kind": "source-native-repair-unknown-stem", "group": stem,
                               "supplement": supplement,
                               "error": "source_native_repairs names a stem no manifest group has"})
                continue
            group = by_stem.get(stem)
            if group is None:
                continue  # merged or skipped group: nothing is adopted for it
            intakes = group.setdefault("symbol_intakes", [])
            if strip_handbook_prefix(rel_posix(supplement)) not in {
                    strip_handbook_prefix(rel_posix(rel)) for rel in intakes}:
                intakes.append(supplement)
    return errors


JSON_KEY_COLON_RE = re.compile(r'"(?:[^"\\]|\\.)*"\s*:\s*')


def manifest_text_with_status(text: str, stems: set[str], status: str) -> str:
    """The manifest text with only the named groups' integration_status values replaced.

    Every other byte is kept. The result must parse to the manifest with exactly those
    statuses changed; a group without an integration_status member is refused.
    """
    expected = json.loads(text)
    top = len(text) - len(text.lstrip())
    members = json_object_members(text, top, matching_json_object_end(text, top))
    if "groups" not in members:
        raise Refusal("manifest has no groups member")
    cursor = JSON_KEY_COLON_RE.match(text, members["groups"]["start"]).end()
    if text[cursor] != "[":
        raise Refusal("manifest groups member is not a list")
    decoder = json.JSONDecoder()
    operations: list[tuple[int, int, str]] = []
    cursor += 1
    while True:
        while text[cursor].isspace() or text[cursor] == ",":
            cursor += 1
        if text[cursor] == "]":
            break
        _value, length = decoder.raw_decode(text[cursor:])
        end = cursor + length
        if text[cursor] == "{" and _value.get("stem") in stems:
            fields = json_object_members(text, cursor, end - 1)
            if "integration_status" not in fields:
                raise Refusal("manifest group " + str(_value.get("stem"))
                              + " has no integration_status member to edit in place")
            field = fields["integration_status"]
            value_start = JSON_KEY_COLON_RE.match(text, field["start"]).end()
            operations.append((value_start, field["end"], json.dumps(status, ensure_ascii=False)))
        cursor = end
    for group in expected.get("groups", []):
        if group.get("stem") in stems:
            group["integration_status"] = status
    result = text
    for start, end, replacement in sorted(operations, reverse=True):
        result = result[:start] + replacement + result[end:]
    if json.loads(result) != expected:
        raise Refusal("in-place manifest status edit did not produce the expected manifest")
    return result


def manifest_status_updates(groups: list[dict], manifest_texts: dict[Path, str]) -> dict[Path, str]:
    """Manifest texts with the selected stems set to merged, edited in place from the
    texts read at startup."""
    stems_by_path: dict[Path, set[str]] = {}
    for group in groups:
        stem = group.get("stem")
        if not stem:
            continue
        owner = Path(group["_manifest_path"]).resolve()
        stems_by_path.setdefault(owner, set()).add(stem)
    updates: dict[Path, str] = {}
    for path, stems in stems_by_path.items():
        if path not in manifest_texts:
            raise Refusal(f"manifest {path} was not read at startup")
        updated = manifest_text_with_status(manifest_texts[path], stems, "merged")
        if updated != manifest_texts[path]:
            updates[path] = updated
    return updates


def resolve_incoming_rows(rows: list[dict], resolver: registry.Resolver) -> tuple[list[dict], list[dict]]:
    incoming: list[dict] = []
    errors: list[dict] = []
    for row in rows:
        if row.get("_inactive") or row.get("_dropped") or row.get("_already_merged"):
            continue
        expanded = []
        if row.get("_members"):
            for member in row["_members"]:
                if member.get("_already_merged"):
                    continue
                child = copy.deepcopy(row)
                child.update(member)
                child["_family_parent"] = row["glyph"]
                child["_uid"] = row_id(row) + ":" + child["glyph"] + ":" + child["role"]
                expanded.append(child)
        else:
            expanded.append(row)
        for item in expanded:
            item["_resolver"] = resolver
            try:
                item["_scope"] = resolver.resolve(item["scope"])
                if not resolver.contains(item["_scope"], item["first_use"]):
                    raise registry.RegistryError("first_use outside scope")
                incoming.append(item)
            except registry.RegistryError as exc:
                errors.append({"group": item.get("_group"), "intake": item.get("_intake"),
                               "line": item.get("_line"), "row": public(item), "error": str(exc)})
    return incoming, errors


def collision_decisions(canonical: list[dict], incoming: list[dict]) -> list[dict]:
    decisions: list[dict] = []
    buckets: dict[str, list[dict]] = {}
    for row in canonical + incoming:
        buckets.setdefault(re.sub(r"\s+", "", row["glyph"]), []).append(row)
    for entries in buckets.values():
        for i, a in enumerate(entries):
            for b in entries[i + 1:]:
                if not (a.get("_group") or b.get("_group")):
                    continue
                try:
                    if not a["_resolver"].overlaps(a["_scope"], b["_scope"]):
                        continue
                    if a["role"] != b["role"] and (
                        a["_resolver"].authorized_override(a, b) or a["_resolver"].authorized_override(b, a)
                    ):
                        continue
                except registry.RegistryError as exc:
                    decisions.append({"kind": "collision-check-error", "error": str(exc),
                                      "a": public(a), "b": public(b),
                                      "a_group": a.get("_group", "canonical"),
                                      "b_group": b.get("_group", "canonical")})
                    continue
                decisions.append({
                    "kind": "duplicate-glyph-role" if a["role"] == b["role"] else "typed-role-overlap",
                    "glyph": a["glyph"],
                    "visible_glyph": visible_glyph(a["glyph"]),
                    "a": public(a),
                    "b": public(b),
                    "a_group": a.get("_group", "canonical"),
                    "b_group": b.get("_group", "canonical"),
                    "standing": "Exact overlapping reader regions require an explicit decision.",
                })
    return decisions


def analyze_bibliography(groups: list[dict], decisions: dict, canonical_text: str,
                         base: Path) -> tuple[list[dict], list[dict], list[dict]]:
    old = bib_records(canonical_text)
    defined_macros = BIB_PREDEFINED_MACROS | bib_string_names(canonical_text)
    by_key: dict[str, list[dict]] = {}
    by_locator: dict[str, list[dict]] = {}
    for record in old:
        by_key.setdefault(record["key"], []).append(record)
        for locator in bib_locators(record):
            by_locator.setdefault(locator, []).append(record)
    citation_aliases_raw = decisions.get("citation_aliases", {})
    citation_aliases = citation_aliases_raw if isinstance(citation_aliases_raw, dict) else {}
    keep_raw = decisions.get("bib_keep_canonical", {})
    if isinstance(keep_raw, list):
        keep = {key: None for key in keep_raw}
    elif isinstance(keep_raw, dict):
        keep = keep_raw
    else:
        keep = {}
    actions_raw = decisions.get("bib_actions", {})
    actions: dict[str, dict] = {}
    append_records: list[dict] = []
    decisions_needed: list[dict] = []
    comparisons: list[dict] = []
    reuse_requests: list[dict] = []
    if not isinstance(actions_raw, dict):
        decisions_needed.append({"kind": "invalid-bib-actions",
                                 "error": "bib_actions must be an object"})
    else:
        for key, action in actions_raw.items():
            if not isinstance(action, dict) or action.get("action") not in {"reuse", "append"}:
                decisions_needed.append({"kind": "invalid-bib-action", "key": key,
                                         "action": action,
                                         "error": "unknown bib_actions value"})
                continue
            actions[key] = action
    if not isinstance(keep_raw, (dict, list)):
        decisions_needed.append({"kind": "invalid-bib-keep-canonical",
                                 "error": "bib_keep_canonical must be an object or list"})

    def reuse_target_for(key: str) -> tuple[str | None, str | None]:
        if key in citation_aliases:
            return citation_aliases[key], "citation_aliases"
        if key in keep:
            return keep[key] or key, "bib_keep_canonical"
        action = actions.get(key, {})
        if action.get("action") == "reuse":
            return action.get("canonical_key") or key, "bib_actions"
        return None, None

    def record_reuse(group: dict, key: str, target: str | None, source: str | None) -> None:
        comparisons.append({"group": group.get("stem"), "key": key,
                            "decision": "reuse-canonical-key",
                            "canonical_key": target, "source": source})
        reuse_requests.append({"group": group.get("stem"), "key": key,
                               "target": target, "source": source})

    for group in groups:
        for rel in group.get("bibliography_intakes", []):
            path = resolve_handbook_path(base, rel)[0]
            if not path.is_file():
                continue
            intake_text = read_text(path)
            for entry in commented_bib_entries(intake_text):
                comparisons.append({"group": group.get("stem"), "intake": rel, "entry": entry,
                                    "decision": "skip-commented-out-entry"})
            for entry in bib_macro_records(intake_text):
                decisions_needed.append({"kind": "bib-string-or-preamble", "group": group.get("stem"),
                                         "intake": rel, "entry": entry,
                                         "error": "@string/@preamble records are not merged; "
                                                  "the canonical bibliography must define what "
                                                  "appended records use"})
            for entry in unparsed_bib_entries(intake_text):
                decisions_needed.append({"kind": "bib-unparsed-record", "group": group.get("stem"),
                                         "intake": rel, "entry": entry,
                                         "error": "bibliography entry not in @type{key, ...} form; "
                                                  "it would be silently lost"})
            for record in bib_records(intake_text):
                key = record["key"]
                problem = bib_record_syntax_error(record["raw"])
                if problem:
                    # An error, not a decision: command_adopt moves this kind to errors.
                    decisions_needed.append({"kind": "bib-record-syntax", "group": group.get("stem"),
                                             "intake": rel, "key": key, "error": problem,
                                             "raw": record["raw"]})
                    continue
                existing = by_key.get(key, [])
                if existing:
                    identical = any(record["comparison"] == old_record["comparison"] for old_record in existing)
                    if identical:
                        comparisons.append({"group": group.get("stem"), "key": key,
                                            "decision": "skip-identical-record"})
                        continue
                    canonical_key, source = reuse_target_for(key)
                    if source:
                        comparisons.append({"group": group.get("stem"), "key": key,
                                            "decision": "keep-canonical-record"})
                        reuse_requests.append({"group": group.get("stem"), "key": key,
                                               "target": canonical_key, "source": source})
                        continue
                    decisions_needed.append({"kind": "bib-key-conflict", "group": group.get("stem"),
                                             "incoming": record, "existing": existing})
                    continue
                candidates: dict[str, dict] = {}
                for locator in bib_locators(record):
                    for candidate in by_locator.get(locator, []):
                        candidates[candidate["key"]] = candidate
                # Records appended earlier in this run count too: two intakes (or two
                # records of one intake) may bring the same work under different keys.
                for old_record in old + append_records:
                    if same_publication_identity(record, old_record):
                        candidates[old_record["key"]] = old_record
                action = actions.get(key, {})
                canonical_key, source = reuse_target_for(key)
                if canonical_key or source:
                    record_reuse(group, key, canonical_key, source)
                    continue
                # Biber reports keys differing only in case as likely typos.
                case_variants = sorted(k for k in by_key if k != key and k.casefold() == key.casefold())
                if case_variants and action.get("action") != "append":
                    decisions_needed.append({"kind": "bib-key-case-conflict", "group": group.get("stem"),
                                             "incoming": record, "existing_keys": case_variants})
                    continue
                if candidates and action.get("action") != "append":
                    decisions_needed.append({"kind": "bib-duplicate-work", "group": group.get("stem"),
                                             "incoming": record,
                                             "candidates": list(candidates.values()),
                                             "shared_locators": bib_locators(record)})
                    continue
                undefined = sorted(bib_value_macros(record) - defined_macros)
                if undefined:
                    decisions_needed.append({"kind": "bib-undefined-macro", "group": group.get("stem"),
                                             "incoming": record, "macros": undefined,
                                             "error": "record uses bare macro values the canonical "
                                                      "bibliography does not define"})
                    continue
                append_records.append(record)
                by_key[key] = [record]
                for locator in bib_locators(record):
                    by_locator.setdefault(locator, []).append(record)
    final_keys = set(by_key)
    for request in reuse_requests:
        target = request.get("target")
        if not isinstance(target, str) or target not in final_keys:
            decisions_needed.append({"kind": "unknown-bib-reuse-target",
                                     "group": request.get("group"),
                                     "key": request.get("key"),
                                     "target": target,
                                     "source": request.get("source"),
                                     "error": "Unknown bib reuse target"})
            continue
        key = request.get("key")
        if key != target and citation_aliases.get(key) != target:
            decisions_needed.append({"kind": "bib-reuse-needs-citation-alias",
                                     "group": request.get("group"),
                                     "key": key,
                                     "target": target,
                                     "source": request.get("source"),
                                     "error": "reuse target differs from incoming key but citation_aliases does not cover it"})
    return append_records, decisions_needed, comparisons


def cite_alias_text(text: str, aliases: dict[str, str]) -> str:
    """Rewrite alias keys at citation sites only, keeping separators."""
    if not aliases:
        return text
    return map_cite_keys(text, lambda key: aliases.get(key, key))


def cite_site_keys(text: str, *, any_cite_command: bool = False) -> set[str]:
    r"""Every bibliography key at a citation site of text.

    any_cite_command: fail closed, reading every braced argument of every
    \...cite... command (known or not) as a key list.
    """
    keys: set[str] = set()

    def collect(key: str) -> str:
        keys.add(key)
        return key

    map_cite_keys(text, collect, any_cite_command=any_cite_command)
    return keys


# handbook.sty status specs (cited=<key> is passed to \cite): the second argument of
# hbtheorem/hblemma/hbcorollary and the argument of \entryadequacy/\entrydecidability.
STATUS_SITE_RE = re.compile(r"\\begin\s*\{(hbtheorem|hblemma|hbcorollary)\}"
                            r"|\\(?:entryadequacy|entrydecidability)(?![A-Za-z@])")
STATUS_CITED_RE = re.compile(r"\s*cited\s*=")


def status_cited_spans(active: str) -> list[tuple[int, int]]:
    """(start, end) of the key list of each cited= status spec in active text."""
    spans: list[tuple[int, int]] = []
    for match in STATUS_SITE_RE.finditer(active):
        _label, cursor = grammar.scan_braced_args(active, match.end(), 1 if match.group(1) else 0)
        while cursor < len(active) and active[cursor].isspace():
            cursor += 1
        args, end = grammar.scan_braced_args(active, cursor, 1)
        if not args:
            continue
        cited = STATUS_CITED_RE.match(active, cursor + 1, end - 1)
        if cited:
            spans.append((cited.end(), end - 1))
    return spans


def map_cite_keys(text: str, fn, *, any_cite_command: bool = False) -> str:
    r"""Apply fn to each key at a citation site, keeping separators.

    Sites: cite-family commands (\cite, \Cite, \citeauthor, \textcite,
    \parencites(..)[..]{..}{..}, \volcite[..]{<volume>}[..]{<key>}, ...), handbook.sty's
    \entrysources{<keys>}, and the status-spec argument {cited=<keys>} of result
    environments and status fields. With any_cite_command, every braced argument of
    any command whose name contains "cite" counts.

    Only active text counts: sites are found in mask_inactive(text), so keys in
    comments, \verb and verbatim-like environments are never read or rewritten.
    Argument scanning stops at a blank line (\par), as biblatex's does.
    """
    active = mask_inactive(text)
    edits: dict[int, tuple[int, str]] = {}

    def keys(start: int, end: int) -> None:
        for key in re.finditer(r"[^,\s]+", active[start:end]):
            edits[start + key.start()] = (start + key.end(), fn(key.group(0)))

    done = 0
    for match in (ANY_CITE_COMMAND_RE if any_cite_command else CITE_COMMAND_RE).finditer(active):
        if match.start() < done:
            continue
        name = match.group(1)
        multi = any_cite_command or name in MULTI_CITE_COMMANDS or name in MULTI_VOLCITE_COMMANDS
        # volcite forms alternate {volume}{keys}; the others read {keys} (once unless multi).
        volume = not any_cite_command and (name in VOLCITE_COMMANDS
                                           or name in MULTI_VOLCITE_COMMANDS)
        pos = match.end()
        key_args = 0
        while True:
            cursor = pos
            while cursor < len(active) and active[cursor].isspace():
                cursor += 1
            # A blank line in the source (comment lines are not blank) is \par.
            if cursor >= len(active) or re.search(r"\n[ \t]*\n", text[pos:cursor]):
                break
            ch = active[cursor]
            if ch in "[(":
                end = delimited_end(active, cursor, "]" if ch == "[" else ")")
                if end < 0:
                    break
            elif ch == "{" and (multi or key_args < (2 if volume else 1)):
                args, end = grammar.scan_braced_args(active, cursor, 1)
                if not args:
                    break
                if not volume or key_args % 2 == 1:
                    keys(cursor + 1, end - 1)
                key_args += 1
            else:
                break
            pos = end
        done = pos
    for start, end in status_cited_spans(active):
        keys(start, end)
    out: list[str] = []
    done = 0
    for start in sorted(edits):
        end, new = edits[start]
        out.append(text[done:start] + new)
        done = end
    out.append(text[done:])
    return "".join(out)


VERBATIM_ENV_RE = re.compile(r"\\begin\s*\{(verbatim\*?|Verbatim\*?|lstlisting|minted|comment)\}")
VERB_RE = re.compile(r"\\verb(?![A-Za-z@])\*?")
INLINE_CODE_RE = re.compile(r"\\(lstinline|mintinline)(?![A-Za-z@])\s*(?:\[[^\]\n]*\]\s*)?")


def inline_code_end(text: str, match: re.Match) -> int:
    r"""End of a \lstinline / \mintinline span: {code} or a delimiter pair on one line."""
    cursor = match.end()
    if match.group(1) == "mintinline":  # the language argument comes first
        _args, cursor = grammar.scan_braced_args(text, cursor, 1)
    line_end = text.find("\n", cursor)
    line_end = len(text) if line_end < 0 else line_end
    if cursor >= line_end:
        return line_end
    if text[cursor] == "{":
        args, end = grammar.scan_braced_args(text, cursor, 1)
        return end if args else line_end
    close = text.find(text[cursor], cursor + 1, line_end)
    return close + 1 if close >= 0 else line_end


def mask_inactive(text: str) -> str:
    r"""Blank % comments, \verb / \lstinline / \mintinline spans and verbatim-like
    environments; offsets and newlines kept."""
    chars = list(text)

    def blank(start: int, end: int) -> None:
        for i in range(start, end):
            if chars[i] != "\n":
                chars[i] = " "

    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "%":
            end = text.find("\n", i)
            end = len(text) if end < 0 else end
        elif ch != "\\":
            i += 1
            continue
        elif env := VERBATIM_ENV_RE.match(text, i):
            close = re.compile(r"\\end\s*\{" + re.escape(env.group(1)) + r"\}").search(text, env.end())
            end = close.end() if close else len(text)
        elif (verb := VERB_RE.match(text, i)) and verb.end() < len(text):
            line_end = text.find("\n", verb.end())
            line_end = len(text) if line_end < 0 else line_end
            close = text.find(text[verb.end()], verb.end() + 1, line_end)
            end = close + 1 if close >= 0 else line_end
        elif inline := INLINE_CODE_RE.match(text, i):
            end = inline_code_end(text, inline)
        else:
            i += 2  # a control symbol such as \% or \\ is not a comment start
            continue
        blank(i, end)
        i = end
    return "".join(chars)


# biblatex and natbib citation commands whose braced arguments are entry keys, plus
# handbook.sty's \entrysources{<keys>} (expands to \cite{<keys>} via \hb@sourcesrow).
CITE_COMMANDS = {
    "entrysources",
    "cite", "Cite", "parencite", "Parencite", "footcite", "footcitetext", "textcite", "Textcite",
    "smartcite", "Smartcite", "supercite", "autocite", "Autocite", "citeauthor", "Citeauthor",
    "citetitle", "Citetitle", "citeyear", "citedate", "citeurl", "nocite", "fullcite",
    "footfullcite", "notecite", "Notecite", "pnotecite", "Pnotecite", "fnotecite",
    "citename", "citelist", "citefield", "citet", "citep", "citealt", "citealp", "citenum",
    "Citet", "Citep", "Citealt", "Citealp", "citeyearpar", "citefullauthor", "Citefullauthor",
}
MULTI_CITE_COMMANDS = {
    "cites", "Cites", "parencites", "Parencites", "footcites", "footcitetexts", "smartcites",
    "Smartcites", "textcites", "Textcites", "supercites", "autocites", "Autocites",
}
VOLCITE_COMMANDS = {"volcite", "Volcite", "pvolcite", "Pvolcite", "fvolcite", "Fvolcite",
                    "ftvolcite", "svolcite", "Svolcite", "tvolcite", "Tvolcite",
                    "avolcite", "Avolcite"}
MULTI_VOLCITE_COMMANDS = {name + "s" for name in VOLCITE_COMMANDS}
CITE_COMMAND_RE = re.compile(
    r"\\(" + "|".join(sorted(CITE_COMMANDS | MULTI_CITE_COMMANDS | VOLCITE_COMMANDS
                              | MULTI_VOLCITE_COMMANDS, key=len, reverse=True))
    + r")(?![A-Za-z@])\*?"
)
ANY_CITE_COMMAND_RE = re.compile(r"\\([A-Za-z]*[Cc]ite[A-Za-z]*)(?![A-Za-z@])\*?")


def delimited_end(text: str, start: int, close: str) -> int:
    """End offset after the `close` matching text[start], skipping braced groups; -1 if none."""
    depth = 0
    index = start + 1
    while index < len(text):
        ch = text[index]
        if ch == "\\":
            index += 2
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        elif ch == close and depth == 0:
            return index + 1
        index += 1
    return -1


def bibliography_intake_keys(groups: list[dict], base: Path) -> dict[str, set[str]]:
    by_group: dict[str, set[str]] = {}
    for group in groups:
        stem = group.get("stem")
        if not stem:
            continue
        keys = by_group.setdefault(stem, set())
        for rel in group.get("bibliography_intakes", []):
            path = resolve_handbook_path(base, rel)[0]
            if not path.is_file():
                continue
            keys.update(record["key"] for record in bib_records(read_text(path)))
    return by_group


def validate_citation_aliases(groups: list[dict], base: Path, aliases: dict,
                              canonical_keys: set[str]) -> tuple[dict[str, dict[str, str]], list[dict]]:
    if not isinstance(aliases, dict):
        return {}, [{"kind": "invalid-citation-aliases", "error": "citation_aliases must be an object"}]
    keys_by_group = bibliography_intake_keys(groups, base)
    source_groups: dict[str, set[str]] = {}
    for stem, keys in keys_by_group.items():
        for key in keys:
            source_groups.setdefault(key, set()).add(stem)
    aliases_by_group: dict[str, dict[str, str]] = {}
    decisions: list[dict] = []
    for source, target in aliases.items():
        if not isinstance(source, str) or not isinstance(target, str):
            decisions.append({"kind": "invalid-citation-alias", "source": source, "target": target,
                              "error": "alias source and target must be strings"})
            continue
        groups_for_source = source_groups.get(source, set())
        if not groups_for_source:
            decisions.append({"kind": "invalid-citation-alias-source", "source": source, "target": target,
                              "error": "alias source is not a key from a selected group's bibliography intakes"})
            continue
        if target not in canonical_keys:
            decisions.append({"kind": "invalid-citation-alias-target", "source": source, "target": target,
                              "error": "alias target is not present in the canonical bibliography after append"})
            continue
        for stem in groups_for_source:
            aliases_by_group.setdefault(stem, {})[source] = target
    return aliases_by_group, decisions


def symbol_validation_failures(path: Path, *, base: Path) -> set[str]:
    rows, errors = registry.read_rows(path, base=base)
    return set(errors) | {"collision: " + item for item in registry.collision_check(rows)}


def symbol_validation_failures_from_text(text: str, *, base: Path,
                                         resolver: registry.Resolver) -> set[str]:
    scratch_root = ROOT / "tmp" / "tooling-scratch" / "integrate"
    scratch_root.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix="symbols-", suffix=".csv", dir=scratch_root)
    temp = Path(name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(text)
        rows, errors = registry.read_rows(temp, resolver=resolver, base=base)
        return set(errors) | {"collision: " + item for item in registry.collision_check(rows)}
    finally:
        try:
            temp.unlink()
        except OSError:
            pass


def gate_scratch_dir() -> tempfile.TemporaryDirectory:
    scratch_root = ROOT / "tmp" / "tooling-scratch" / "integrate"
    scratch_root.mkdir(parents=True, exist_ok=True)
    return tempfile.TemporaryDirectory(prefix="gate-", dir=scratch_root)


def symbol_compile_errors(rows: list[dict], base: Path) -> list[dict]:
    r"""Compile gate: the rows typeset as symbols2tex types them, under handbook.sty.

    Syntax checks cannot see a command's arity (\hat, \frac{a}); pdflatex can. Every
    row becomes a symbol-table row (glyph, \texttt{\detokenize{macro}}, role, scope,
    first use, notes) in one longtable; any '! ' error refuses, attributed to its row.
    """
    if not rows:
        return []
    pdflatex = TEXLIVE_BIN / "pdflatex.exe"
    if not pdflatex.is_file():
        return [{"kind": "symbol-compile-gate", "error": "TeX Live pdflatex not found at "
                 + pdflatex.as_posix() + "; the symbol compile gate cannot run"}]
    sty_dir = base if (base / "handbook.sty").is_file() else TOOL_HANDBOOK
    lines = [rf"\phantomsection\label{{entry:symbol-gate-{n:05d}}}{symbols2tex.glyph_cell(row['glyph'])}"
             + " & " + " & ".join([symbols2tex.macro_code(row["macro"]),
                                   symbols2tex.text_cell(row["role"]), registry.scope_tex(row),
                                   row["precedence"], registry.first_use_tex(row), r"\thepage",
                                   symbols2tex.text_cell(row["notes"])]) + r" \\"
             for n, row in enumerate(rows)]
    table = symbols2tex.longtable(
        r"@{}p{0.9in}p{1.3in}p{1.0in}p{0.5in}p{0.3in}p{0.4in}p{0.35in}p{1.65in}@{}",
        ["Glyph", "Macro", "Role", "Scope", "Prec./form", "First", "Reg. page", "Notes"], [])
    head, tail = table.split(r"\end{longtable}", 1)
    prefix = ("\\documentclass[11pt]{book}\n\\usepackage{handbook}\n\\begin{document}\n"
              "\\begin{landscape}\n" + head)
    starts: list[int] = []  # first TeX line of each row
    line_no = prefix.count("\n") + 1
    for text in lines:
        starts.append(line_no)
        line_no += text.count("\n") + 1
    document = (prefix + "\n".join(lines) + "\n\\end{longtable}" + tail
                + "\\end{landscape}\n\\end{document}\n")
    env = os.environ.copy()
    env["PATH"] = str(TEXLIVE_BIN) + os.pathsep + env.get("PATH", "")
    env["TEXINPUTS"] = str(sty_dir) + os.pathsep
    with gate_scratch_dir() as temp_name:
        temp = Path(temp_name)
        write_text_atomic(temp / "gate.tex", document)
        try:
            proc = subprocess.run([str(pdflatex), "-no-shell-escape", "-interaction=nonstopmode",
                                   "-halt-on-error", "gate.tex"], cwd=temp, env=env,
                                  capture_output=True, timeout=600)
        except subprocess.TimeoutExpired:
            return [{"kind": "symbol-compile-gate", "error": "pdflatex timed out"}]
        log = read_log_text(temp / "gate.log").splitlines() if (temp / "gate.log").is_file() else []
    found: list[dict] = []
    for index, line in enumerate(log):
        if not line.startswith("! "):
            continue
        context = next((m for m in (re.match(r"l\.(\d+)", item) for item in log[index + 1:index + 12])
                        if m), None)
        item = {"kind": "symbol-compile", "error": line}
        if context:
            row_index = bisect_right(starts, int(context.group(1))) - 1
            if 0 <= row_index < len(rows):
                row = rows[row_index]
                item.update(row=public(row), group=row.get("_group", "canonical"),
                            intake=row.get("_intake"), line=row.get("_line"))
        found.append(item)
    if not found and proc.returncode != 0:
        found.append({"kind": "symbol-compile-gate",
                      "error": "pdflatex exited " + str(proc.returncode) + " without a '! ' error"})
    return found


BIBER_TEMP_PATH_RE = re.compile(r"\S*biber_tmp\S*")


def biber_messages(text: str, folder: Path, biber: Path) -> tuple[int, list[str]]:
    """Exit code and the normalized WARN/ERROR lines of biber --tool on text."""
    write_text_atomic(folder / "handbook.bib", text)
    proc = subprocess.run([str(biber), "--tool", "--output-file", "tool-out.bib", "handbook.bib"],
                          cwd=folder, capture_output=True, encoding="utf-8", errors="replace",
                          timeout=600)
    lines = [BIBER_TEMP_PATH_RE.sub("<tmp>", line).strip()
             for line in (proc.stdout + proc.stderr).splitlines()
             if "WARN - " in line or "ERROR - " in line]
    return proc.returncode, lines


def biber_new_problems(old_text: str, new_text: str) -> list[str]:
    """biber --tool gate: every ERROR, and each WARN the merged bibliography has beyond the
    canonical one, as TeX Live biber reports them (section 0)."""
    biber = TEXLIVE_BIN / "biber.exe"
    if not biber.is_file():
        return ["TeX Live biber not found at " + biber.as_posix() + "; the bibliography gate cannot run"]
    with gate_scratch_dir() as temp_name:
        temp = Path(temp_name)
        try:
            with ThreadPoolExecutor(max_workers=2) as pool:
                old_job = pool.submit(biber_messages, old_text, temp / "old", biber)
                new_job = pool.submit(biber_messages, new_text, temp / "new", biber)
                _old_code, old_lines = old_job.result()
                new_code, new_lines = new_job.result()
        except subprocess.TimeoutExpired:
            return ["biber timed out"]
    problems = [line for line in new_lines if "ERROR - " in line]
    problems += list((Counter(line for line in new_lines if "WARN - " in line)
                      - Counter(line for line in old_lines if "WARN - " in line)).elements())
    if new_code != 0 and not problems:
        problems.append("biber exited " + str(new_code))
    return problems


def relative_output_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def apply_adoption(result: dict, context: dict) -> list[Path]:
    original_paths = set(context["canonical_paths"])
    original_paths.update(context["citation_writes"])
    original_paths.update(context["manifest_updates"])
    refuse_changed_since_read(context.get("expected_texts", {}))
    originals = {path: read_text(path) for path in original_paths}
    written: list[Path] = []

    def write_if_changed(path: Path, text: str) -> None:
        if read_text(path) != text:
            write_text_atomic(path, text)
            written.append(path)

    try:
        if context["new_bib_text"] is not None:
            write_if_changed(context["bib_path"], context["new_bib_text"])
            problems = bib_text_errors(read_text(context["bib_path"]),
                                       context.get("expected_bib_keys", []),
                                       context.get("appended_bib_keys", frozenset()))
            if problems:
                raise Refusal("post-apply bibliography check failed: " + repr(problems[:5]))
        if context["new_scopes_text"] is not None:
            write_if_changed(context["scopes_path"], context["new_scopes_text"])
        if context["new_symbols_text"] is not None:
            write_if_changed(context["symbols_path"], context["new_symbols_text"])
        for path, text in context["citation_writes"].items():
            write_if_changed(path, text)
        rows, errors = registry.read_rows(context["symbols_path"], base=context["base"])
        collision_errors = registry.collision_check(rows)
        failures = set(errors) | {"collision: " + item for item in collision_errors}
        new_failures = sorted(failures - context.get("baseline_validation_failures", set()))
        if new_failures:
            raise Refusal("post-apply symbol validation introduced failures: " + repr(new_failures[:10]))
        for path, manifest_text in context["manifest_updates"].items():
            write_if_changed(path, manifest_text)
    except Exception:
        for path, text in originals.items():
            if path.is_file() and read_text(path) != text:
                write_text_atomic(path, text)
        raise
    return written


def command_adopt(args: argparse.Namespace) -> int:
    if bool(args.return_json) != bool(args.virtual_route):
        raise UsageError("--return and --virtual-route must be used together")
    manifest_path = Path(args.manifest)
    manifest, manifest_text = read_manifest(manifest_path)
    decisions = load_json(Path(args.decisions)) if args.decisions else {}
    if not isinstance(decisions, dict):
        raise Refusal("decisions must be a JSON object")
    problems = decisions_shape_errors(decisions)
    if problems:
        raise Refusal("malformed decisions: " + "; ".join(problems))

    base = BASE
    virtual_group = None
    if args.return_json and args.virtual_route:
        return_data = load_json(Path(args.return_json))
        temp_group = group_from_return(Path(args.return_json), return_data)
        stem = temp_group.get("stem", "")
        if not re.fullmatch(r"[a-z0-9-]+", stem):
            raise Refusal(f"invalid return stem: {stem!r}")
        unit_root = (ROOT / "tmp" / "unit-builds").resolve()
        tree = (unit_root / stem / "tree").resolve()
        if not tree.is_relative_to(unit_root):
            raise Refusal(f"virtual-route tree outside tmp/unit-builds: {tree}")
        source = BASE
        if tree.exists():
            shutil.rmtree(tree)
        shutil.copytree(source, tree / "handbook",
                        ignore=lambda _dir, names: {n for n in names if is_build_artifact(n)})
        base = tree / "handbook"
        own_placements = iter_placements_in_value(temp_group.get("placement"), temp_group.get("stem"))
        route_result = simulate_route(base, own_placements, apply=True,
                                      siblings=manifest_placements(manifest) + own_placements)
        if not route_result["ok"]:
            raise Refusal("virtual route failed: " + json.dumps(route_result["errors"], ensure_ascii=False))
        virtual_group = temp_group

    groups, status_errors, manifest_texts = groups_for_adopt(manifest_path, manifest)
    manifest_texts[manifest_path.resolve()] = manifest_text
    group_source = manifest_path.as_posix()
    if virtual_group is not None:
        # The returned group's placement was applied in the copy; the reach check below
        # still has to confirm it is on the route there.
        virtual_group = copy_group_for_adopt(virtual_group, manifest_path)
        groups = [group for group in groups if group.get("stem") != virtual_group.get("stem")]
        status_errors = [item for item in status_errors
                         if item.get("group") != virtual_group.get("stem")]
        groups.append(virtual_group)
        group_source += "+return"
    allowed_shared = {resolve_handbook_path(base, rel, tex=True)[1]
                      for rel in decisions.get("allow_shared_owned_files", [])}
    ownership_needed = ownership_decisions(groups, base, allowed_shared)
    symbols_path = base / "registry/symbols.csv"
    scopes_path = base / "registry/symbol-scopes.json"
    bib_path = base / "bib/handbook.bib"
    canonical_text = {
        "symbols": read_text(symbols_path),
        "scopes": read_text(scopes_path),
        "bib": read_text(bib_path),
    }
    old_rows_raw = list(csv.DictReader(io.StringIO(canonical_text["symbols"])))
    old_tuples = {row_tuple(row) for row in old_rows_raw}
    try:
        old_scopes_doc = json.loads(canonical_text["scopes"])
    except json.JSONDecodeError as exc:
        raise Refusal("invalid symbol-scopes.json: " + str(exc)) from exc
    if not isinstance(old_scopes_doc, dict) or old_scopes_doc.get("schema_version") != 1 or not isinstance(old_scopes_doc.get("scopes"), dict):
        raise Refusal("invalid symbol-scopes.json schema")
    index = registry.ReaderIndex(base)

    all_rows: list[dict] = []
    errors: list[dict] = list(status_errors)
    inactive: list[dict] = []
    missing_inputs: list[dict] = []
    route_counts, _closure_errors = static_input_counts(base)
    for group in groups:
        for rel in owned_rels(group):
            try:
                path, rel_norm = resolve_handbook_path(base, rel, tex=True)
            except Refusal as exc:
                errors.append({"group": group.get("stem"), "path": rel, "error": str(exc)})
                continue
            if not path.is_file():
                missing_inputs.append({"group": group.get("stem"), "path": rel})
            elif not route_counts.get(rel_norm):
                errors.append({"group": group.get("stem"), "path": rel_norm, "kind": "not-on-route",
                               "error": "Not literally reached: owned file is not reached by the "
                                        "static \\input closure from main.tex"})
        intakes: list[tuple[Path, str]] = []
        for rel in group.get("symbol_intakes", []):
            try:
                path, rel_norm = resolve_handbook_path(base, rel)
            except Refusal as exc:
                errors.append({"group": group.get("stem"), "path": rel, "error": str(exc)})
                continue
            if not path.is_file():
                missing_inputs.append({"group": group.get("stem"), "path": rel})
                continue
            intakes.append((path, rel_norm))
        adopted_intakes = {rel_norm for _path, rel_norm in intakes}
        for path, rel in intakes:
            rows, row_errors, row_inactive = read_symbol_intake(path, rel, group, adopted_intakes)
            all_rows.extend(rows)
            errors.extend(row_errors)
            inactive.extend(row_inactive)
    errors.extend({"error": "missing input", **item} for item in missing_inputs)
    selector_errors = validate_decision_selectors(decisions, all_rows, old_rows_raw)
    errors.extend(selector_errors)
    all_rows, refused_errors, refused_inactive = resolve_refused_rows(
        all_rows, {} if selector_errors else decisions)
    errors.extend(refused_errors)
    inactive.extend(refused_inactive)
    if not selector_errors:
        errors.extend(apply_incoming_row_decisions(all_rows, decisions))
    errors.extend(finalize_incoming_rows(
        all_rows, index, old_tuples, set(old_scopes_doc["scopes"])
    ))
    canonical_edited = copy.deepcopy(old_rows_raw)
    if not selector_errors:
        canonical_edited, canonical_edit_errors = apply_canonical_row_edits(old_rows_raw, decisions)
        errors.extend(canonical_edit_errors)
    for old_row, new_row in zip(old_rows_raw, canonical_edited):
        for item in numeric_row_errors(new_row, set(old_scopes_doc["scopes"])):
            field = "scope" if "scope" in item else "first_use"
            if new_row.get(field) != old_row.get(field):
                errors.append(dict(item, kind="canonical-row-edit"))

    # Each synthesized binding comes from one group's rows; scope name -> group -> regions.
    synthesized: dict[str, dict[str, list[dict]]] = {}
    foreign_annexitems: list[dict] = []
    for row in all_rows:
        if row.get("_inactive") or row.get("_dropped") or row.get("_already_merged"):
            continue
        name = row["scope"]
        if name == "global" or registry.LABEL_RE.fullmatch(name) or " through " in name:
            continue
        if name in old_scopes_doc["scopes"]:
            continue
        if numeric_scope_forbidden(name):
            continue
        group = next((g for g in groups if g.get("stem") == row.get("_group")), {})
        try:
            selectors, foreign = local_regions_for_first_use(index, row["first_use"], group)
        except registry.RegistryError as exc:
            errors.append({"group": row.get("_group"), "line": row.get("_line"),
                           "kind": "binding-unresolved", "scope": name, "error": str(exc)})
            continue
        foreign_annexitems.extend({"group": row.get("_group"), "scope": name, **item}
                                  for item in foreign)
        regions = synthesized.setdefault(name, {}).setdefault(str(row.get("_group")), [])
        for selector in selectors:
            if selector not in regions:
                regions.append(selector)
    new_scopes: dict[str, dict] = {}
    shared_scope_decisions: list[dict] = []
    for name, by_group in synthesized.items():
        union = [s for regions in by_group.values() for s in regions]
        union = [s for i, s in enumerate(union) if s not in union[:i]]
        new_scopes[name] = {
            "presentation": "Source-labelled wave intake regions for " + ", ".join(by_group),
            "regions": union,
        }
        if len(by_group) == 1:
            continue
        # One name used by several groups: merging would put each group's symbol in
        # force over the other's regions. Only an extend_scopes decision listing every
        # region covers that.
        if not {selector_key(s) for s in union} <= decided_selectors(decisions, name):
            shared_scope_decisions.append({
                "kind": "scope-name-shared-across-groups", "scope": name,
                "groups": {group: regions for group, regions in by_group.items()},
                "error": "groups use the same new scope name; merging their regions needs an "
                         "extend_scopes decision listing every region (or rename the scope)"})
    combined_scopes = copy.deepcopy(old_scopes_doc)
    combined_scopes["scopes"].update(new_scopes)
    combined_scopes["scopes"], scope_decision_errors = merge_decision_scope_extensions(
        combined_scopes["scopes"], decisions, old_scopes_doc["scopes"])
    errors.extend(scope_decision_errors)
    foreign_errors = {
        "binding-foreign-annexitem": "an annex item owned by a result in this scope's region lies "
                                     "outside the group's own annexes; it is not bound (add it "
                                     "with extend_scopes to include it)",
        "binding-foreign-owner": "the annex first_use's owner result lies in a file the group "
                                 "does not own; it is not bound (add it with extend_scopes to "
                                 "include it)",
        "binding-annexitem-owner-ambiguous": "the annex item's owner label resolves more than once "
                                             "on the route; it is not bound (extend_scopes listing "
                                             "the anchor binds it, or fix the duplicate label)",
        "binding-heading-spill": "the synthesized heading region runs on over files the group does "
                                 "not own (extend_scopes listing this selector accepts it; or give "
                                 "the row a label scope)",
    }
    foreign_decisions: list[dict] = []
    for item in foreign_annexitems:
        selector = item.get("selector") or {"anchor": item["anchor"]}
        if selector_key(selector) in decided_selectors(decisions, item["scope"]):
            continue  # a decision lists it explicitly
        decision = {**item, "error": foreign_errors[item["kind"]]}
        if decision not in foreign_decisions:
            foreign_decisions.append(decision)
    for name in sorted(set(combined_scopes["scopes"]) - set(old_scopes_doc["scopes"])):
        if numeric_scope_forbidden(name):
            errors.append({"kind": "decision-scope", "scope": name,
                           "error": "numeric scope forbidden"})

    baseline_validation_failures = symbol_validation_failures(symbols_path, base=base)
    append_bib, bib_decisions, bib_comparisons = analyze_bibliography(groups, decisions,
                                                                       canonical_text["bib"], base)
    errors.extend(item for item in bib_decisions if item["kind"] == "bib-record-syntax")
    bib_decisions = [item for item in bib_decisions if item["kind"] != "bib-record-syntax"]
    resolver = registry.Resolver(base, bindings=combined_scopes, index=index)
    resolver.source_keys.update(record["key"] for record in append_bib)
    parsed_old: list[dict] = []
    canonical_errors: list[str] = []
    for line, row in enumerate(canonical_edited, 2):
        row = copy.deepcopy(row)
        row.update(_line=line, _resolver=resolver)
        try:
            row["_scope"] = resolver.resolve(row["scope"])
        except registry.RegistryError as exc:
            canonical_errors.append(f"line {line}: {exc}")
            continue
        # Like registry.read_rows: a resolved row stays in the collision set even
        # when its first_use check fails.
        parsed_old.append(row)
        try:
            if not resolver.contains(row["_scope"], row["first_use"]):
                canonical_errors.append(f"line {line}: first_use outside scope")
        except registry.RegistryError as exc:
            canonical_errors.append(f"line {line}: {exc}")
    incoming, incoming_errors = resolve_incoming_rows(all_rows, resolver)
    errors.extend(incoming_errors)
    decisions_needed = ownership_needed + collision_decisions(parsed_old, incoming)
    decisions_needed.extend(shared_scope_decisions)
    decisions_needed.extend(foreign_decisions)
    decisions_needed.extend(nonascii_glyph_decisions(all_rows))
    for line, (old_row, new_row) in enumerate(zip(old_rows_raw, canonical_edited), 2):
        found = (nonascii_math_characters(unwrap_glyph(new_row["glyph"]))
                 if new_row.get("glyph") != old_row.get("glyph") else [])
        if found:
            decisions_needed.append({
                "kind": "glyph-non-ascii-math", "group": "canonical", "line": line,
                "glyph": new_row["glyph"], "characters": found,
                "error": "canonical_row_edits sets a glyph with a non-ASCII character in math "
                         "outside \\text{...}; give its TeX command instead"})
        found = (sorted({ch for ch in new_row.get("macro", "") if not ch.isascii()})
                 if new_row.get("macro") != old_row.get("macro") else [])
        if found:
            decisions_needed.append(dict(nonascii_macro_decision(new_row["macro"], found),
                                         group="canonical", line=line))
    decisions_needed.extend(bib_decisions)

    appended_bib_keys = {record["key"] for record in append_bib}
    expected_bib_keys = ([record["key"] for record in bib_records(canonical_text["bib"])]
                         + [record["key"] for record in append_bib])
    canonical_keys_after_append = set(expected_bib_keys)
    aliases_by_group, alias_decisions = validate_citation_aliases(
        groups, base, decisions.get("citation_aliases", {}), canonical_keys_after_append
    )
    decisions_needed.extend(alias_decisions)

    edited_tuples = {row_tuple(row) for row in canonical_edited}
    safe_rows = [row for row in incoming if row_tuple(row) not in edited_tuples]
    new_bib_text = None
    new_symbols_text = None
    new_scopes_text = None
    citation_writes: dict[Path, str] = {}
    citation_originals: dict[Path, str] = {}
    manifest_updates: dict[Path, str] = {}
    validation_new_failures: list[str] = []
    prospective_validation_failures: set[str] = set()
    ready_for_writes = not decisions_needed and not errors
    if ready_for_writes:
        if append_bib:
            sep = "\n\n" if canonical_text["bib"].rstrip() else ""
            new_bib_text = canonical_text["bib"].rstrip() + sep + "\n\n".join(r["raw"].strip() for r in append_bib) + "\n"
            errors.extend({"kind": "bib-merge-unreadable", "error": problem}
                          for problem in bib_text_errors(new_bib_text, expected_bib_keys,
                                                         appended_bib_keys))
            errors.extend({"kind": "bib-biber-check", "error": problem}
                          for problem in biber_new_problems(canonical_text["bib"], new_bib_text))
        # Compile gate over every row this adopt adds or edits.
        errors.extend(symbol_compile_errors(
            safe_rows + [row for old_row, row in zip(old_rows_raw, canonical_edited)
                         if row_tuple(old_row) != row_tuple(row)], base))
        if new_scopes or decisions.get("extend_scopes") or decisions.get("overrides"):
            new_scopes_doc = copy.deepcopy(old_scopes_doc)
            new_scopes_doc["scopes"] = combined_scopes["scopes"]
            new_scopes_text = scopes_json_text_preserving(
                canonical_text["scopes"], old_scopes_doc, new_scopes_doc
            )
        canonical_edits_present = bool(decisions.get("canonical_row_edits"))
        if canonical_edits_present or safe_rows:
            new_symbols_text = symbols_csv_text_preserving(
                canonical_text["symbols"], old_rows_raw, canonical_edited, safe_rows
            )
        final_scopes_doc = copy.deepcopy(old_scopes_doc)
        final_scopes_doc["scopes"] = combined_scopes["scopes"]
        final_resolver = registry.Resolver(base, bindings=final_scopes_doc, index=index)
        final_resolver.source_keys.update(record["key"] for record in append_bib)
        prospective_validation_failures = symbol_validation_failures_from_text(
            new_symbols_text if new_symbols_text is not None else canonical_text["symbols"],
            base=base,
            resolver=final_resolver,
        )
        validation_new_failures = sorted(
            prospective_validation_failures - baseline_validation_failures,
            key=lambda value: value.encode("utf-8"),
        )
        # Alias sources that leave no record of their own in the final bibliography.
        dangling_sources = {source for aliases in aliases_by_group.values() for source in aliases
                            if source not in canonical_keys_after_append}
        pinned = pinned_reader_files()
        checked: list[tuple[dict, Path, str, dict]] = []
        read_texts: dict[Path, str] = {}
        for group in groups:
            aliases = aliases_by_group.get(group.get("stem"), {})
            for rel in owned_rels(group):
                path, rel_norm = resolve_handbook_path(base, rel, tex=True)
                if not path.is_file():
                    continue
                if path not in read_texts:
                    read_texts[path] = read_text(path)
                # A file shared by decision gets every owner's rewrite, applied in turn.
                text = citation_writes.get(path, read_texts[path])
                changed = cite_alias_text(text, aliases)
                if changed != text:
                    if rel_norm in pinned:
                        errors.append({"group": group.get("stem"), "path": rel_norm,
                                       "kind": "pinned-file-rewrite",
                                       "error": "citation rewrite target is a check.py byte-pinned "
                                                "retained file (HB_RETAINED_UNREACHABLE_READER_FILES); "
                                                "edit refused"})
                        continue
                    citation_writes[path] = changed
                checked.append((group, path, rel_norm, aliases))
        citation_originals = {path: read_texts[path] for path in citation_writes}
        for group, path, rel_norm, aliases in checked:
            final = citation_writes.get(path, read_texts[path])
            renamed = {source for source, target in aliases.items() if source != target}
            cited = cite_site_keys(final) | cite_site_keys(final, any_cite_command=True)
            left = sorted(cited & (renamed | dangling_sources))
            if left:
                errors.append({"group": group.get("stem"), "path": rel_norm, "keys": left,
                               "kind": "alias-left-at-citation-site",
                               "error": "aliased source key still cited after the rewrite"})
        manifest_updates = manifest_status_updates(groups, manifest_texts)

    ok = ready_for_writes and not errors and not validation_new_failures

    result = {
        "ok": ok,
        "command": "adopt",
        "dry_run": not args.apply or bool(args.virtual_route),
        "group_source": group_source,
        "groups": [g.get("stem") for g in groups],
        "input_symbol_rows": len(all_rows),
        "inactive_rows": inactive,
        "new_symbol_rows": len(safe_rows),
        "new_scope_bindings": sorted(new_scopes),
        "new_bib_records": [r["key"] for r in append_bib],
        "bib_comparisons": bib_comparisons,
        "errors": errors,
        "canonical_errors_count": len(canonical_errors),
        "canonical_errors_sample": canonical_errors[:20],
        "baseline_symbol_validation_failures_count": len(baseline_validation_failures),
        # Not computed when decisions or errors block the merge.
        "prospective_symbol_validation_failures_count": (
            len(prospective_validation_failures) if ready_for_writes else None),
        "new_symbol_validation_failures": validation_new_failures[:20],
        "decisions-needed": decisions_needed,
        "known_overlap_visible_glyphs": sorted({d.get("visible_glyph") for d in decisions_needed
                                                if d.get("visible_glyph")}),
    }
    if args.apply and result["ok"] and not args.virtual_route:
        context = {
            "base": base,
            "canonical_paths": [symbols_path, scopes_path, bib_path],
            "symbols_path": symbols_path,
            "scopes_path": scopes_path,
            "bib_path": bib_path,
            "new_bib_text": new_bib_text,
            "expected_bib_keys": expected_bib_keys,
            "appended_bib_keys": appended_bib_keys,
            "new_scopes_text": new_scopes_text,
            "new_symbols_text": new_symbols_text,
            "citation_writes": citation_writes,
            "manifest_updates": manifest_updates,
            "baseline_validation_failures": baseline_validation_failures,
            "expected_texts": {symbols_path: canonical_text["symbols"],
                               scopes_path: canonical_text["scopes"],
                               bib_path: canonical_text["bib"],
                               **citation_originals,
                               **manifest_texts},
        }
        written = apply_adoption(result, context)
        result["dry_run"] = False
        result["files_written"] = [relative_output_path(path) for path in written]
    print_json(result)
    return 0 if result["ok"] else 1


def normalize_check_output(text: str) -> list[str]:
    lines: list[str] = []
    for line in text.splitlines():
        if not line.startswith("  - "):
            continue
        line = re.sub(r":\d+\)", ")", line)
        line = re.sub(r":\d+(:\d+)?", "", line)
        # symbols-csv / glyph-collision findings: 'line 6053: ...', 'lines 79/6052: ...'.
        line = re.sub(r"\b(lines?) \d+(?:/\d+)*", r"\1", line)
        lines.append(line)
    return sorted(lines, key=lambda s: s.encode("utf-8"))


def finding_category(line: str) -> str:
    match = re.match(r"\s*-\s*([^:]+):", line)
    return match.group(1).strip() if match else "uncategorized"


def manifest_paths(manifest_path: str | None) -> set[str]:
    if not manifest_path:
        return set()
    data, _text = read_manifest(Path(manifest_path))
    paths: set[str] = set()
    for group in data.get("groups", []):
        for key in GROUP_LIST_FIELDS:
            for rel in group.get(key, []):
                if key in {"bodies", "annexes", "rule_sheets"}:
                    rel_norm = tex_rel(rel)
                else:
                    rel_norm = strip_handbook_prefix(rel)
                paths.add("handbook/" + rel_norm)
    return paths


def git_untracked_paths() -> set[str]:
    proc = subprocess.run(["git", "ls-files", "--others", "--exclude-standard"],
                          cwd=ROOT, text=True, capture_output=True)
    if proc.returncode != 0:
        return set()
    return {rel_posix(line) for line in proc.stdout.splitlines() if line.strip()}


def finding_paths(line: str) -> set[str]:
    found: set[str] = set()
    pattern = re.compile(
        r"(?<![A-Za-z0-9_./-])"
        r"((?:handbook/)?(?:parts|annex|bib|registry)/[A-Za-z0-9_./-]+"
        r"(?:\.(?:tex|bib|csv|json))?)"
    )
    for match in pattern.finditer(line):
        rel = match.group(1)
        if rel.startswith("handbook/"):
            found.add(rel)
        else:
            found.add("handbook/" + rel)
    return found


def line_mentions_only_untracked(line: str, manifest_tracked: set[str],
                                 untracked: set[str]) -> bool:
    if not untracked:
        return False
    mentions = finding_paths(line)
    return bool(mentions) and all(
        path in untracked and path not in manifest_tracked for path in mentions
    )


def multiset_delta(current: list[str], previous: list[str]) -> tuple[list[str], list[str]]:
    current_counter = Counter(current)
    previous_counter = Counter(previous)
    new = list((current_counter - previous_counter).elements())
    fixed = list((previous_counter - current_counter).elements())
    return (
        sorted(new, key=lambda s: s.encode("utf-8")),
        sorted(fixed, key=lambda s: s.encode("utf-8")),
    )


def check_run_failure(returncode: int, output: str) -> str | None:
    if returncode not in {0, 1}:
        return "check.py exited with " + str(returncode)
    if "Traceback" in output:
        return "check.py output contains Traceback"
    has_marker = (
        "[check] all hard checks passed" in output
        or re.search(r"\[check\]\s+\d+\s+(?:hard\s+)?(?:failure|finding)\(s\)", output)
    )
    if not has_marker:
        return "check.py output lacks summary marker"
    return None


CHECK_NAME_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")


def check_store_name(value: str, option: str) -> str:
    if not CHECK_NAME_RE.fullmatch(value or "") or ".." in value:
        raise UsageError(f"{option} must be a plain name ([A-Za-z0-9._-]): {value!r}")
    return value


def latest_check_store(exclude: str) -> str | None:
    """Name of the most recently written tmp/integration/<name>/check-norm.txt."""
    stores = [path for path in (ROOT / "tmp/integration").glob("*/check-norm.txt")
              if path.parent.name != exclude]
    if not stores:
        return None
    return max(stores, key=lambda path: path.stat().st_mtime).parent.name


def command_check_delta(args: argparse.Namespace) -> int:
    # Validate every argument before the (slow) check.py run.
    integration = ROOT / "tmp/integration"
    previous_store = None
    previous_name = None
    name = None
    if args.init:
        # The store lives at tmp/integration/<name>; a path may only spell that location.
        if CHECK_NAME_RE.fullmatch(args.init) and ".." not in args.init:
            out = integration / args.init
        else:
            raw = Path(args.init)
            out = (raw if raw.is_absolute() else ROOT / raw).resolve()
            if (out.parent != integration.resolve()
                    or not CHECK_NAME_RE.fullmatch(out.name) or ".." in out.name):
                raise UsageError("--init must name tmp/integration/<name>: " + repr(args.init))
    else:
        name = check_store_name(args.stage or args.tag, "--stage" if args.stage else "--tag")
        if args.stage:
            previous_name = (check_store_name(args.prev, "--prev") if args.prev
                             else latest_check_store(exclude=name))
            if previous_name is None:
                raise Refusal("no stored check baseline under tmp/integration; run --init first")
        else:
            if args.prev:
                raise UsageError("--prev is only valid with --stage")
            previous_name = name
        previous_store = integration / previous_name / "check-norm.txt"
        if not previous_store.is_file():
            raise Refusal(f"check baseline not found: {relative_output_path(previous_store)}")
    if args.manifest:
        manifest_paths(args.manifest)

    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    proc = subprocess.run([sys.executable, "-B", "tools/check.py", "--tree", "handbook"],
                          cwd=ROOT, capture_output=True, env=env,
                          encoding="utf-8", errors="replace")
    check_output = proc.stdout + proc.stderr
    check_failure = check_run_failure(proc.returncode, check_output)
    if check_failure:
        print_json({"ok": False, "command": "check-delta",
                    "error": check_failure, "check_exit": proc.returncode,
                    "output_sample": check_output.splitlines()[:20]})
        return 1
    current = normalize_check_output(check_output)
    if args.init:
        out.mkdir(parents=True, exist_ok=True)
        write_text_atomic(out / "check-norm.txt", "\n".join(current) + ("\n" if current else ""))
        print_json({"ok": True, "command": "check-delta", "init": out.as_posix(),
                    "findings": len(current), "check_exit": proc.returncode})
        return 0
    previous = read_text(previous_store).splitlines()
    new, fixed = multiset_delta(current, previous)
    manifest_tracked = manifest_paths(args.manifest)
    untracked = git_untracked_paths()
    effective_new = [line for line in new
                     if not line_mentions_only_untracked(line, manifest_tracked, untracked)]
    by_category: dict[str, dict[str, int]] = {}
    for label, lines in (("new", new), ("fixed", fixed)):
        for line in lines:
            cat = finding_category(line)
            by_category.setdefault(cat, {"new": 0, "fixed": 0})[label] += 1
    if args.stage and not effective_new:
        store = ROOT / "tmp/integration" / name / "check-norm.txt"
        store.parent.mkdir(parents=True, exist_ok=True)
        write_text_atomic(store, "\n".join(current) + ("\n" if current else ""))
        write_json_atomic(store.parent / "check-meta.json", {
            "stage": name,
            "previous": previous_name,
            "observed_utc": utc_now(),
        })
    print_json({"ok": not effective_new, "command": "check-delta", "name": name,
                "previous": previous_name,
                "new": len(new), "fixed": len(fixed),
                "new_after_manifest_filter": len(effective_new),
                "by_category": by_category, "check_exit": proc.returncode})
    return 0 if not effective_new else 1


def printed_part_ordinal(part: int) -> int:
    if 1 <= part <= 10:
        return part
    if 15 <= part <= 19:
        return part - 4
    if 11 <= part <= 14:
        return part + 5
    return part


def scoped_driver_text(part: int) -> str:
    p = f"p{part:02d}"
    annex = {"p01": "annex/p01-route", "p05": "annex/p05-route", "p06": "annex/p06-route"}.get(p, f"annex/{p}")
    lines = [
        r"\documentclass[11pt]{book}",
        r"\usepackage{handbook}",
        r"\usepackage[backend=biber,style=alphabetic]{biblatex}",
        r"\addbibresource{bib/handbook.bib}",
        r"\input{bib/inherited-keys}",
        r"\begin{document}",
        rf"\setcounter{{part}}{{{printed_part_ordinal(part) - 1}}}",
    ]
    if part == 8:
        lines.append(r"\input{parts/p08/source-anchors}")
    lines += [
        rf"\input{{parts/{p}}}",
        r"\hbannexsetup",
        rf"\input{{{annex}}}",
        r"\hbannexfinish",
        r"\backmatter\printbibliography",
        r"\end{document}",
    ]
    return "\n".join(lines) + "\n"


def run_scoped_part(snapshot: Path, part: int) -> dict:
    snapshot = snapshot.resolve()
    out_dir = snapshot / "scoped" / f"p{part:02d}"
    out_dir.mkdir(parents=True, exist_ok=True)
    driver = out_dir / "scoped.tex"
    write_text_atomic(driver, scoped_driver_text(part))
    texlive = TEXLIVE_BIN
    pdflatex = texlive / "pdflatex.exe"
    biber = texlive / "biber.exe"
    if not pdflatex.is_file() or not biber.is_file():
        missing = [path.as_posix() for path in (pdflatex, biber) if not path.is_file()]
        return {"part": f"P{part}", "ok": False,
                "errors": ["missing TeX Live 2025 executable: " + item for item in missing],
                "driver": driver.as_posix(), "out": out_dir.as_posix()}
    pdflatex_cmd = str(pdflatex)
    biber_cmd = str(biber)
    env = os.environ.copy()
    env["PATH"] = str(texlive) + os.pathsep + env.get("PATH", "")
    errors: list[str] = []
    commands = [
        [pdflatex_cmd, "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error",
         "-file-line-error", "-output-directory", str(out_dir), str(driver)],
        [biber_cmd, "--input-directory", str(out_dir), "--output-directory", str(out_dir), "scoped"],
        [pdflatex_cmd, "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error",
         "-file-line-error", "-output-directory", str(out_dir), str(driver)],
        [pdflatex_cmd, "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error",
         "-file-line-error", "-output-directory", str(out_dir), str(driver)],
    ]
    for command in commands:
        try:
            # TeX console output carries raw font-encoding bytes too.
            proc = subprocess.run(command, cwd=snapshot / "handbook", encoding="utf-8",
                                  errors="replace", capture_output=True, timeout=600, env=env)
        except subprocess.TimeoutExpired:
            errors.append("timeout: " + " ".join(command[:2]))
            break
        if proc.returncode != 0:
            errors.append("exit " + str(proc.returncode) + ": " + " ".join(command[:2]))
            break
    log = out_dir / "scoped.log"
    if log.is_file():
        for line in read_log_text(log).splitlines():
            if line.startswith("! ") or "Undefined control sequence" in line:
                errors.append(line)
    return {"part": f"P{part}", "ok": not errors, "errors": errors,
            "driver": driver.as_posix(), "out": out_dir.as_posix()}


def command_scoped_build(args: argparse.Namespace) -> int:
    snapshot = Path(args.snapshot).resolve()
    try:
        parts = sorted({int(item.strip()) for item in args.parts.split(",") if item.strip()})
    except ValueError as exc:
        raise UsageError("--parts must be comma-separated part numbers") from exc
    if not parts or any(not 1 <= part <= 19 for part in parts):
        raise UsageError("--parts must name parts 1..19")
    if not (snapshot / "handbook").is_dir():
        raise Refusal(f"snapshot has no handbook directory: {snapshot.as_posix()}")
    results = []
    with ThreadPoolExecutor(max_workers=min(len(parts), os.cpu_count() or 1)) as pool:
        futures = [pool.submit(run_scoped_part, snapshot, part) for part in parts]
        for future in as_completed(futures):
            results.append(future.result())
    results.sort(key=lambda item: item["part"])
    ok = all(item["ok"] for item in results)
    print_json({"ok": ok, "command": "scoped-build", "results": results})
    return 0 if ok else 1


def unwrap_latex_log_lines(text: str) -> str:
    pieces: list[str] = []
    for line in text.splitlines():
        pieces.append(line)
        if len(line) != 79:
            pieces.append("\n")
    return "".join(pieces)


LOG_FILE_OPEN_RE = re.compile(r'\("?((?:[A-Za-z]:)?[^\s()"]*\.[A-Za-z][A-Za-z0-9]*)"?')
BOX_WARNING_RE = re.compile(r"(Overfull|Underfull) \\[hv]box")


def overfull_by_file(unwrapped: str) -> dict[str, int]:
    r"""Overfull box count per source file, following TeX's open-file stack.

    '(' + file name opens a file and its matching ')' closes it; any other '(' is
    pushed too, so a parenthesised message closes itself. The box display TeX prints
    after an Overfull/Underfull warning (up to the next blank line) is skipped, since
    it quotes paragraph text whose parentheses need not balance.
    """
    counts: dict[str, int] = {}
    stack: list[str | None] = []
    in_box_display = False
    for line in unwrapped.split("\n"):
        if in_box_display:
            in_box_display = bool(line.strip())
            continue
        warning = BOX_WARNING_RE.search(line)
        scan = line[:warning.start()] if warning else line
        i = 0
        while i < len(scan):
            if scan[i] == "(":
                opened = LOG_FILE_OPEN_RE.match(scan, i)
                stack.append(opened.group(1).replace("\\", "/").removeprefix("./")
                             if opened else None)
                if opened:
                    i = opened.end()
                    continue
            elif scan[i] == ")" and stack:
                stack.pop()
            i += 1
        if warning:
            if warning.group(1) == "Overfull":
                current = next((name for name in reversed(stack) if name), "unknown")
                counts[current] = counts.get(current, 0) + 1
            in_box_display = True
    return counts


def parse_build_summary(log_path: Path) -> dict:
    text = read_log_text(log_path)
    unwrapped = unwrap_latex_log_lines(text)
    pages = None
    match = re.search(r"Output written on .+ \((\d+) pages?", text)
    if match:
        pages = int(match.group(1))
    refs = sorted(set(re.findall(r"Reference [`']([^`']+)'[^\n]*undefined", unwrapped)))
    citations = sorted(set(re.findall(r"Citation [`']([^`']+)'[^\n]*undefined", unwrapped)))
    multiply = sorted(set(re.findall(r"Label [`']([^`']+)'[^\n]*multiply defined", unwrapped)))
    missing = [line for line in text.splitlines() if "Missing character:" in line]
    overfull = overfull_by_file(unwrapped)
    blg = log_path.with_suffix(".blg")
    biber = []
    if blg.is_file():
        biber = [line for line in read_log_text(blg).splitlines()
                 if "WARN" in line or "ERROR" in line]
    return {
        "log": log_path.as_posix(),
        "page_count": pages,
        "undefined_refs": refs,
        "undefined_citations": citations,
        "multiply_defined_labels": multiply,
        "overfull": overfull,
        "missing_character_lines": missing,
        "biber": biber,
    }


def command_build_summary(args: argparse.Namespace) -> int:
    if not Path(args.log).is_file():
        raise Refusal(f"log not found: {args.log}")
    summary = parse_build_summary(Path(args.log))
    new_items = {}
    if args.prev:
        prev = load_json(Path(args.prev))
        for key in ("undefined_refs", "undefined_citations", "multiply_defined_labels",
                    "missing_character_lines"):
            new_items[key] = sorted(set(summary[key]) - set(prev.get(key, [])))
        old_biber = set(prev.get("biber", []))
        new_items["biber"] = [line for line in summary["biber"] if line not in old_biber]
        summary["new_items"] = new_items
    print_json(summary)
    if args.prev and any(new_items.get(key) for key in (
        "undefined_refs", "undefined_citations", "multiply_defined_labels", "missing_character_lines"
    )):
        return 1
    return 0


def run_selftest() -> None:
    # math_glyph: escape bare specials, refuse nesting/unbalanced/bare ^ ~
    assert math_glyph("%") == r"\%" and math_glyph("#") == r"\#" and math_glyph("&") == r"\&"
    assert math_glyph("$") == r"\$" and math_glyph("_") == r"\_" and math_glyph("H_q") == "H_q"
    assert math_glyph(r"\{x\}") == r"\{x\}" and math_glyph(r"a\%b") == r"a\%b"
    for bad in ("$$x$$", r"\[x\]", r"\(x\)", "^", "~", "{", "}", "a}b{"):
        try:
            math_glyph(bad)
        except IntakeRowError:
            pass
        else:
            raise AssertionError("math_glyph accepted " + repr(bad))
    scratch_root = ROOT / "tmp" / "tooling-scratch" / "integrate"
    scratch_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="selftest-", dir=scratch_root) as temp_name:
        temp = Path(temp_name)
        hb = temp / "handbook"
        (hb / "registry").mkdir(parents=True)
        (hb / "bib").mkdir(parents=True)
        (hb / "parts/p01").mkdir(parents=True)
        write_text_atomic(hb / "main.tex", "\\input{parts/p01}\n")
        write_text_atomic(hb / "parts/p01.tex",
                          "\\chapter{One}\\label{ch:p01}\n"
                          "\\input{parts/p01/a}\n"
                          "\\input{restoration/scope-old}\n")
        write_text_atomic(hb / "parts/p01/a.tex", "\\section{A}\\label{sec:p01-a}\n")
        write_text_atomic(hb / "parts/p01/b.tex", "\\section{B}\\label{sec:p01-b}\n")
        (hb / "restoration").mkdir(parents=True)
        write_text_atomic(hb / "restoration/scope-old.tex",
                          "\\section{Old}\\label{sec:p01-old}\n")
        write_text_atomic(hb / "parts/p01/c.tex", "\\section{C}\\label{sec:p01-c}\n")
        placement = {"host": "parts/p01.tex", "after": "parts/p01/a", "input": "parts/p01/b"}
        routed = simulate_route(hb, [placement], apply=False)
        assert routed["ok"], routed
        assert routed["actions"][0]["action"] == "insert"
        restoration_anchor = {
            "host": "parts/p01.tex",
            "after": "restoration/scope-old",
            "input": "parts/p01/c",
        }
        restored = simulate_route(hb, [restoration_anchor], apply=False)
        assert restored["ok"], restored
        bad = {"host": "parts/p01.tex", "after": "parts/p01/missing", "input": "parts/p01/b"}
        assert not simulate_route(hb, [bad], apply=False)["ok"]
        bad_path = {"host": "../outside", "after": "parts/p01/a", "input": "parts/p01/b"}
        assert not simulate_route(hb, [bad_path], apply=False)["ok"]
        assert not insertion_inside_hook([r"\AddToHookNext{cmd/chapter/before}{\relax}",
                                          r"\input{parts/p01/a}"], 1)
        # ...but the one-shot hook stays pending until its \chapter fires.
        assert insertion_before_hook_next_consumer(
            [r"\AddToHookNext{cmd/chapter/before}{\relax}", r"\input{parts/p01/a}"], 1)
        assert not insertion_inside_hook([r"\AddToHook{env/x/begin}[n]{\relax}",
                                          r"\input{parts/p01/a}"], 1)
        paired = [
            r"\AddToHook{env/x/begin}[n]{\relax}",
            r"\input{parts/p01/a}",
            r"\RemoveFromHook{env/x/begin}[n]",
            r"\input{parts/p01/b}",
        ]
        assert insertion_inside_hook(paired, 1)
        assert insertion_inside_hook(paired, 2)
        assert not insertion_inside_hook(paired, 3)
        wildcard_remove = [
            r"\AddToHook{env/x/begin}[n]{\relax}",
            r"\input{parts/p01/a}",
            r"\RemoveFromHook{env/x/begin}[*]",
        ]
        assert insertion_inside_hook(wildcard_remove, 1)
        assert insertion_inside_hook(wildcard_remove, 2)
        multiline_hook = [
            r"\AddToHook",
            r"  {env/x/begin}[n]{\relax}",
            r"\input{parts/p01/a}",
            r"\RemoveFromHook{env/x/begin}[n]",
        ]
        assert insertion_inside_hook(multiline_hook, 2)
        try:
            insertion_inside_hook([r"\AddToHook", r"\input{parts/p01/a}"], 1)
            assert False, "unparseable hook command should be refused"
        except Refusal:
            pass
        csv_text = "glyph,macro,role,scope,precedence,first_use,notes\n\\(a,b\\),,role,scope,operator,def:x,n\n"
        repaired = repair_csv_text(csv_text)
        parsed = list(csv.DictReader(io.StringIO(repaired)))
        assert parsed[0]["glyph"] == r"\(a,b\)"
        doi_records = bib_records(
            "@article{A,\n title={T},\n year={2020},\n doi={doi:10.1/X}\n}\n"
            "@article{B,\n title={T},\n year={2020},\n url={https://www.doi.org/10.1/X}\n}\n"
            "@article{C,\n title={T},\n year={2020},\n note={See https://doi.org/10.1/X.}\n}\n"
        )
        for record in doi_records:
            assert "doi:10.1/x" in bib_locators(record)
        assert normalize_check_output(
            "x\n  - cat: path:12) bad\n  - cat: path:14) bad\n"
        ) == ["  - cat: path) bad", "  - cat: path) bad"]
        assert multiset_delta(["a", "a", "b"], ["a", "c"]) == (["a", "b"], ["c"])
        assert check_run_failure(0, "[check] all hard checks passed\n") is None
        assert check_run_failure(1, "\n[check] 2 hard failure(s):\n  - x\n") is None
        assert check_run_failure(1, "Traceback (most recent call last):\n") is not None
        assert check_run_failure(1, "  - vanished marker\n") is not None
        assert check_run_failure(2, "[check] no handbook tree\n") is not None

        index = registry.ReaderIndex(hb)
        numeric_variants = ["P1.1 - P1", "P1.1–P1", "p1.1", "P1-P1.0x",
                            "P1–P1", "P1 - P1", "p1-p1", "P1—P1", "P5 to P19",
                            "p5", "P1 – p2", "P-6.3", "P.6.3", "P#6.3", "P_6.3"]
        numeric_rows = [
            {"_group": "g", "_line": line, "glyph": r"\(n\)", "macro": "n",
             "role": "role", "scope": scope, "precedence": "n/a",
             "first_use": "sec:p01-a", "notes": ""}
            for line, scope in enumerate(numeric_variants, 2)
        ]
        numeric_errors = finalize_incoming_rows(numeric_rows, index, set(), set())
        assert [item["error"] for item in numeric_errors] == (
            ["numeric scope forbidden"] * len(numeric_variants)), numeric_errors
        assert not numeric_scope_forbidden("P13 consequence operations")
        assert not numeric_scope_forbidden("global")
        try:
            local_regions_for_first_use(index, "sec:p01-a",
                                        {"stem": "empty", "bodies": [], "annexes": []})
            assert False, "empty owned file set should not synthesize a binding"
        except registry.RegistryError as exc:
            assert "group owns no files" in str(exc)

        bad_selector_row = {"_group": "g", "_line": 2, "glyph": r"\(x\)",
                            "macro": "x", "role": "role", "scope": "global",
                            "first_use": "sec:p01-a", "precedence": "n/a", "notes": ""}
        selector_errors = validate_decision_selectors(
            {"drop_rows": [{"glyf": r"\(x\)"}],
             "canonical_row_edits": [{"lin": 2, "set": {"notes": "bad"}}]},
            [bad_selector_row],
            [public(bad_selector_row)],
        )
        assert {item["kind"] for item in selector_errors} == {"invalid-selector"}
        assert not row_is_dropped(bad_selector_row, {"drop_rows": [{"glyf": r"\(x\)"}]})
        assert validate_decision_selectors(
            {"canonical_row_edits": [{"glyph": r"\(x\)", "role": "role",
                                      "scope": "global", "set": {"notes": "ok"}}]},
            [],
            [public(bad_selector_row)],
        ) == []

        original_symbols = (
            "glyph,macro,role,scope,precedence,first_use,notes\n"
            r"\(a\),a,role a,global,n/a,sec:p01-a,keep" + "\n"
            r"\(b\),b,role b,global,n/a,sec:p01-a,old" + "\n"
        )
        original_rows = list(csv.DictReader(io.StringIO(original_symbols)))
        edited_rows = copy.deepcopy(original_rows)
        edited_rows[1]["notes"] = "new"
        preserved_symbols = symbols_csv_text_preserving(
            original_symbols, original_rows, edited_rows,
            [{"glyph": r"\(c\)", "macro": "c", "role": "role c", "scope": "global",
              "precedence": "n/a", "first_use": "sec:p01-a", "notes": "append"}],
        )
        unchanged_prefix = original_symbols.index(r"\(b\)")
        assert preserved_symbols is not None
        assert preserved_symbols.encode("utf-8")[:unchanged_prefix] == (
            original_symbols.encode("utf-8")[:unchanged_prefix]
        )
        original_scopes = (
            "{\n"
            "  \"schema_version\": 1,\n"
            "  \"scopes\": {\n"
            "    \"alpha\": {\n"
            "      \"presentation\": \"A\",\n"
            "      \"regions\": [\n"
            "        {\"anchor\":\"sec:a\"}\n"
            "      ]\n"
            "    }\n"
            "  }\n"
            "}\n"
        )
        old_scope_doc = json.loads(original_scopes)
        new_scope_doc = copy.deepcopy(old_scope_doc)
        new_scope_doc["scopes"]["beta"] = {"presentation": "B",
                                           "regions": [{"anchor": "sec:b"}]}
        preserved_scopes = scopes_json_text_preserving(
            original_scopes, old_scope_doc, new_scope_doc
        )
        assert preserved_scopes is not None
        old_bounds = scopes_object_bounds(original_scopes)
        old_members = json_object_members(original_scopes, *old_bounds)
        alpha_end = old_members["alpha"]["end"]
        assert preserved_scopes.encode("utf-8")[:alpha_end] == (
            original_scopes.encode("utf-8")[:alpha_end]
        )
        assert json.loads(preserved_scopes) == new_scope_doc

        log_path = temp / "unit.log"
        prev_path = temp / "prev-summary.json"
        ref_key = "FrozenFormalLogicFoundationsClosure"
        ref_prefix = f"LaTeX Warning: Reference `{ref_key}' "
        wrapped_ref = ref_prefix + ("x" * (79 - len(ref_prefix) - len("undefi"))) + "undefi"
        assert len(wrapped_ref) == 79
        write_text_atomic(
            log_path,
            "LaTeX Warning: Citation 'Brouwer1908' on page 461 undefined on input line 481.\n"
            + wrapped_ref + "\n"
            "ned on input line 10.\n",
        )
        write_json_atomic(prev_path, {"undefined_refs": [], "undefined_citations": [],
                                      "multiply_defined_labels": [],
                                      "missing_character_lines": []})
        summary = parse_build_summary(log_path)
        assert summary["undefined_citations"] == ["Brouwer1908"]
        assert summary["undefined_refs"] == [ref_key]
        with contextlib.redirect_stdout(io.StringIO()):
            assert command_build_summary(argparse.Namespace(
                log=str(log_path), prev=str(prev_path)
            )) == 1
        unicode_log_path = temp / "unicode-build.log"
        write_text_atomic(
            unicode_log_path,
            "Missing character: There is no ≤ in font cmr10!\n",
        )
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "cp1252"
        env["PYTHONUTF8"] = "0"
        proc = subprocess.run(
            [sys.executable, "-B", str(Path(__file__).resolve()),
             "build-summary", str(unicode_log_path)],
            cwd=ROOT, capture_output=True, env=env, timeout=30,
        )
        assert proc.returncode == 0, proc.stderr.decode("utf-8", "replace")
        decoded_stdout = proc.stdout.decode("utf-8")
        assert "≤" in decoded_stdout
        assert "Traceback" not in proc.stderr.decode("utf-8", "replace")

        manifest = {"groups": [{"stem": "s", "integration_status": "routed-awaiting-canonical-merge",
                                "placements": [placement]}]}
        manifest_path = temp / "manifest-unroute.json"
        write_json_atomic(manifest_path, manifest)
        write_text_atomic(hb / "parts/p01.tex",
                          "\\chapter{One}\\label{ch:p01}\n"
                          "\\input{parts/p01/a}\n"
                          "\\input{parts/p01/b}\n")
        old_root, old_base = ROOT, BASE
        try:
            globals()["ROOT"] = temp
            globals()["BASE"] = hb
            with contextlib.redirect_stdout(io.StringIO()):
                code = command_unroute(argparse.Namespace(
                    manifest=str(manifest_path), stems="s", apply=True
                ))
            assert code == 0
            assert r"\input{parts/p01/b}" not in read_text(hb / "parts/p01.tex")
            assert load_json(manifest_path)["groups"][0]["integration_status"] == "returned-for-fix"

            (hb / "annex/p01").mkdir(parents=True)
            write_text_atomic(hb / "annex/p01/a.tex",
                              "\\begin{annexitem}{annex:p01.a}{sec:p01-a}\nX\n\\end{annexitem}\n")
            try:
                group_from_return(temp / "bad-return.json", {
                    "stem": "bad",
                    "part": "P1",
                    "annexes": ["annex/p01/a"],
                    "declared_proof_pairs": 2,
                })
                assert False, "declared_proof_pairs mismatch should be refused"
            except Refusal:
                pass

            write_text_atomic(hb / "parts/p01.tex",
                              "\\chapter{One}\\label{ch:p01}\n\\input{parts/p01/a}\n")
            write_text_atomic(hb / "registry/symbol-scopes.json",
                              json_text({"schema_version": 1, "scopes": {}}))
            write_text_atomic(hb / "registry/symbols.csv",
                              "glyph,macro,role,scope,precedence,first_use,notes\n"
                              r"\(x\),x,old role,global,n/a,sec:p01-a," + "\n")
            write_text_atomic(hb / "bib/handbook.bib", "")
            adopt_manifest = temp / "manifest-adopt.json"
            decisions_path = temp / "decisions-adopt.json"
            write_json_atomic(adopt_manifest, {"groups": []})
            write_json_atomic(decisions_path, {
                "canonical_row_edits": [{"line": 2, "set": {"role": "new role"}}]
            })
            with contextlib.redirect_stdout(io.StringIO()):
                code = command_adopt(argparse.Namespace(
                    manifest=str(adopt_manifest),
                    decisions=str(decisions_path),
                    apply=True,
                    return_json=None,
                    virtual_route=False,
                ))
            assert code == 0
            assert "new role" in read_text(hb / "registry/symbols.csv")

            write_text_atomic(hb / "bib/intake-s.bib",
                              "@article{NewKey,\n title={N},\n author={A},\n year={2024}\n}\n")
            aliases_by_group, alias_errors = validate_citation_aliases(
                [{"stem": "s", "bibliography_intakes": ["bib/intake-s.bib"]}],
                hb,
                {"NewKey": "Ghost", "OldKey": "Ghost"},
                {"OldKey"},
            )
            assert aliases_by_group == {}
            assert {item["kind"] for item in alias_errors} == {
                "invalid-citation-alias-target",
                "invalid-citation-alias-source",
            }

            canonical_bib = (
                "@article{OldKey,\n"
                "  title={T},\n"
                "  author={A},\n"
                "  year={2024},\n"
                "  doi={10.1000/example}\n"
                "}\n"
            )
            write_text_atomic(hb / "bib/intake-s.bib",
                              "@article{Other,\n title={O},\n author={A},\n year={2024}\n}\n")
            _append, bib_needed, _comparisons = analyze_bibliography(
                [{"stem": "s", "bibliography_intakes": ["bib/intake-s.bib"]}],
                {"bib_actions": {"Other": {"action": "reuse", "canonical_key": "Ghost"}}},
                canonical_bib,
                hb,
            )
            assert any(item["kind"] == "unknown-bib-reuse-target" for item in bib_needed)
            write_text_atomic(hb / "bib/intake-s.bib",
                              "@article{NewKey,\n"
                              "  title={T},\n"
                              "  author={A},\n"
                              "  year={2024},\n"
                              "  doi={10.1000/example}\n"
                              "}\n")
            _append, bib_needed, _comparisons = analyze_bibliography(
                [{"stem": "s", "bibliography_intakes": ["bib/intake-s.bib"]}],
                {"bib_keep_canonical": {"NewKey": "OldKey"}},
                canonical_bib,
                hb,
            )
            assert any(item["kind"] == "bib-reuse-needs-citation-alias" for item in bib_needed)
            _append, bib_needed, _comparisons = analyze_bibliography(
                [{"stem": "s", "bibliography_intakes": ["bib/intake-s.bib"]}],
                {"bib_keep_canonical": {"NewKey": "OldKey"},
                 "citation_aliases": {"NewKey": "OldKey"}},
                canonical_bib,
                hb,
            )
            assert not any(item["kind"] in {
                "unknown-bib-reuse-target",
                "bib-reuse-needs-citation-alias",
            } for item in bib_needed)
            _append, bib_needed, _comparisons = analyze_bibliography(
                [{"stem": "s", "bibliography_intakes": ["bib/intake-s.bib"]}],
                {"bib_actions": {"NewKey": {"action": "mystery"}}},
                canonical_bib,
                hb,
            )
            assert any(item["kind"] == "invalid-bib-action" for item in bib_needed)
        finally:
            globals()["ROOT"] = old_root
            globals()["BASE"] = old_base

        rollback = temp / "rollback"
        rb = rollback / "handbook"
        (rb / "registry").mkdir(parents=True)
        (rb / "bib").mkdir(parents=True)
        (rb / "parts/p01").mkdir(parents=True)
        write_text_atomic(rb / "main.tex", "\\input{parts/p01}\n")
        write_text_atomic(rb / "parts/p01.tex", "\\chapter{One}\\label{ch:p01}\n\\input{parts/p01/a}\n")
        write_text_atomic(rb / "parts/p01/a.tex", "\\section{A}\\label{sec:p01-a}\n\\cite{OldKey}\n")
        write_text_atomic(rb / "registry/symbol-scopes.json", json_text({"schema_version": 1, "scopes": {}}))
        good_symbols = ("glyph,macro,role,scope,precedence,first_use,notes\n"
                        r"\(x\),x,role,global,n/a,sec:p01-a," + "\n")
        bad_symbols = ("glyph,macro,role,scope,precedence,first_use,notes\n"
                       r"\(x\),x,role,global,n/a,sec:nope," + "\n")
        write_text_atomic(rb / "registry/symbols.csv", good_symbols)
        write_text_atomic(rb / "bib/handbook.bib", "")
        rollback_manifest = rollback / "manifest.json"
        original_manifest = {"groups": [{"stem": "s", "integration_status": "routed"}]}
        write_json_atomic(rollback_manifest, original_manifest)
        try:
            apply_adoption({}, {
                "base": rb,
                "canonical_paths": [rb / "registry/symbols.csv",
                                    rb / "registry/symbol-scopes.json",
                                    rb / "bib/handbook.bib"],
                "symbols_path": rb / "registry/symbols.csv",
                "scopes_path": rb / "registry/symbol-scopes.json",
                "bib_path": rb / "bib/handbook.bib",
                "new_bib_text": None,
                "new_scopes_text": None,
                "new_symbols_text": bad_symbols,
                "citation_writes": {rb / "parts/p01/a.tex":
                                    "\\section{A}\\label{sec:p01-a}\n\\cite{NewKey}\n"},
                "manifest_updates": {rollback_manifest: json_text(
                    {"groups": [{"stem": "s", "integration_status": "merged"}]})},
                "baseline_validation_failures": set(),
            })
            assert False, "apply_adoption should have refused bad symbols"
        except Refusal:
            pass
        assert read_text(rb / "registry/symbols.csv") == good_symbols
        assert "\\cite{OldKey}" in read_text(rb / "parts/p01/a.tex")
        assert load_json(rollback_manifest) == original_manifest
        selftest_route_and_bib(temp)
        selftest_commands(temp)
        selftest_repairs(temp)
        selftest_round4(temp)
        selftest_round5(temp)
        selftest_round6(temp)
        selftest_round7(temp)
        selftest_round8(temp)
        selftest_round9(temp)
        selftest_round10(temp)
        selftest_round11(temp)
        selftest_round12(temp)
        selftest_round13(temp)


def selftest_route_and_bib(temp: Path) -> None:
    """Route refusals, apply/idempotence, hook arguments, bib detection and text helpers."""
    hb = temp / "route" / "handbook"
    (hb / "parts/p01").mkdir(parents=True)
    write_text_atomic(hb / "main.tex", "\\input{parts/p01}\n")
    write_text_atomic(hb / "parts/p01.tex", "\\chapter{One}\n\\input{parts/p01/a}\n")
    write_text_atomic(hb / "parts/p01/a.tex", "\\section{A}\\label{sec:p01-a}\n")
    write_text_atomic(hb / "parts/p01/b.tex", "\\section{B}\\label{sec:p01-b}\n")
    write_text_atomic(hb / "parts/p01/sub.tex", "\\subsection{S}\\label{sec:p01-s}\n")
    write_text_atomic(hb / "parts/p01/orphan.tex", "\\input{parts/p01/a}\n")

    # Right after \chapter{One} (before a), a \subsection would skip the section level.
    sub = {"host": "parts/p01", "before": "parts/p01/a", "input": "parts/p01/sub"}
    result = simulate_route(hb, [sub], apply=False)
    assert not result["ok"] and result["errors"][0]["error"].startswith("heading level skip"), result
    assert result["errors"][0]["heading_in_force"] == "chapter", result
    # After a (a \section is in force there) it continues that section.
    assert simulate_route(hb, [dict(sub, before=None, after="parts/p01/a")], apply=False)["ok"]
    assert simulate_route(hb, [dict(sub, supplement_of="parts/p01/a")], apply=False)["ok"]

    orphan = {"host": "parts/p01/orphan", "after": "parts/p01/a", "input": "parts/p01/b"}
    result = simulate_route(hb, [orphan], apply=False)
    assert not result["ok"] and "reaches input 0 times" in result["errors"][0]["error"], result

    twice = {"host": "parts/p01", "after": "parts/p01/a", "input": "parts/p01/b"}
    write_text_atomic(hb / "main.tex", "\\input{parts/p01}\n\\input{parts/p01/b}\n")
    result = simulate_route(hb, [twice], apply=False)
    assert not result["ok"] and "reaches input 2 times" in result["errors"][0]["error"], result
    write_text_atomic(hb / "main.tex", "\\input{parts/p01}\n")

    before = read_text(hb / "parts/p01.tex")
    assert simulate_route(hb, [twice], apply=False)["ok"]
    assert read_text(hb / "parts/p01.tex") == before, "dry run must not write"
    applied = simulate_route(hb, [twice], apply=True)
    assert applied["ok"] and applied["actions"][0]["action"] == "insert", applied
    routed_text = read_text(hb / "parts/p01.tex")
    assert routed_text == "\\chapter{One}\n\\input{parts/p01/a}\n\\input{parts/p01/b}\n"
    again = simulate_route(hb, [twice], apply=True)
    assert again["ok"] and again["actions"][0]["action"] == "noop-already-present", again
    assert read_text(hb / "parts/p01.tex") == routed_text

    hooked = [r"\AddToHook{env/x/begin}[n]{%", r"  \input{parts/p01/a}", r"}", r"\input{z}"]
    assert insertion_inside_hook(hooked, 2)
    assert not insertion_inside_hook(hooked, 3)
    try:
        insertion_inside_hook([r"\AddToHook{env/x/begin}[n]{%", r"\input{parts/p01/a}"], 1)
        assert False, "unbalanced hook code should be refused"
    except Refusal:
        pass

    index = registry.ReaderIndex(hb)
    base_row = {"_group": "g", "glyph": r"\(n\)", "macro": "n", "role": "role",
                "scope": "global", "precedence": "n/a", "notes": ""}
    errors = finalize_incoming_rows([dict(base_row, _line=2, first_use="P1.1"),
                                     dict(base_row, _line=3, first_use="sec:nope"),
                                     dict(base_row, _line=4, first_use="sec:p01-a")],
                                    index, set(), set())
    assert [item["line"] for item in errors] == [2, 3], errors
    assert errors[0]["error"] == "numeric first_use forbidden"

    (hb / "bib").mkdir(parents=True)
    canonical = "@article{OldKey,\n  title={T},\n  author={A},\n  year={2024},\n  doi={10.1000/x}\n}\n"
    group = {"stem": "s", "bibliography_intakes": ["bib/intake-s.bib"]}

    def bib_kinds(intake: str, decisions: dict) -> tuple[list[str], set[str]]:
        write_text_atomic(hb / "bib/intake-s.bib", intake)
        append, needed, _comparisons = analyze_bibliography([group], decisions, canonical, hb)
        return [record["key"] for record in append], {item["kind"] for item in needed}

    assert bib_kinds(canonical, {}) == ([], set())
    conflict = canonical.replace("title={T}", "title={Other}")
    assert bib_kinds(conflict, {}) == ([], {"bib-key-conflict"})
    assert bib_kinds(conflict, {"bib_keep_canonical": ["OldKey"]}) == ([], set())
    duplicate = canonical.replace("OldKey", "NewKey")
    assert bib_kinds(duplicate, {}) == ([], {"bib-duplicate-work"})
    same_work = ("@book{Third,\n  title={T},\n  author={A},\n  year={2024}\n}\n")
    assert bib_kinds(same_work, {}) == ([], {"bib-duplicate-work"})
    assert bib_kinds(duplicate, {"bib_actions": {"NewKey": {"action": "append"}}}) == (["NewKey"], set())
    fresh = "@book{Fresh,\n  title={F},\n  author={B},\n  year={1999}\n}\n"
    assert bib_kinds(fresh, {}) == (["Fresh"], set())

    aliases = {"X": "Y"}
    assert cite_alias_text(r"\cite{K1, K2} X", aliases) == r"\cite{K1, K2} X"
    assert cite_alias_text(r"\cite[p.~3]{K1, X}", aliases) == r"\cite[p.~3]{K1, Y}"
    assert cite_alias_text(r"\parencites(g)[see]{X}[p]{K, X}", aliases) == r"\parencites(g)[see]{Y}[p]{K, Y}"
    assert cite_alias_text(r"\citeauthor{X} \Cite*{X} \textcite{XX}", aliases) == r"\citeauthor{Y} \Cite*{Y} \textcite{XX}"
    assert cite_alias_text(r"\ref{X}", aliases) == r"\ref{X}"

    empty_scopes = '{\n  "schema_version": 1,\n  "scopes": {}\n}\n'
    old_doc = json.loads(empty_scopes)
    new_doc = copy.deepcopy(old_doc)
    new_doc["scopes"]["beta"] = {"presentation": "B", "regions": [{"anchor": "sec:b"}]}
    merged = scopes_json_text_preserving(empty_scopes, old_doc, new_doc)
    assert merged is not None and json.loads(merged) == new_doc
    assert '\n    "beta": ' in merged, merged
    changed_doc = copy.deepcopy(new_doc)
    changed_doc["scopes"]["beta"]["regions"].append({"anchor": "sec:c"})
    changed = scopes_json_text_preserving(merged, new_doc, changed_doc)
    assert changed is not None and json.loads(changed) == changed_doc
    assert '\n    "beta": ' in changed and '\n        "beta"' not in changed, changed

    assert is_build_artifact("x.run.xml") and is_build_artifact("X.SYNCTEX.GZ")
    assert is_build_artifact("main.pdf") and not is_build_artifact("main.tex")


def selftest_commands(temp: Path) -> None:
    """route/unroute/check-delta/adopt commands against a temp ROOT."""
    root = temp / "commands"
    hb = root / "handbook"
    (hb / "parts/p01").mkdir(parents=True)
    (hb / "registry").mkdir(parents=True)
    (hb / "bib").mkdir(parents=True)
    write_text_atomic(hb / "main.tex", "\\input{parts/p01}\n")
    write_text_atomic(hb / "parts/p01.tex",
                      "\\chapter{One}\n\\input{parts/p01/a}\n\\input{parts/p01/b}\n")
    write_text_atomic(hb / "parts/p01/a.tex", "\\section{A}\\label{sec:p01-a}\n\\cite{K1, X}\n")
    write_text_atomic(hb / "parts/p01/b.tex",
                      "\\section{B}\\label{sec:p01-b}\n\\input{parts/p01/b-inner}\n")
    write_text_atomic(hb / "parts/p01/b-inner.tex", "Inner text.\n")
    old_root, old_base = ROOT, BASE
    try:
        globals()["ROOT"] = root
        globals()["BASE"] = hb

        def run(func, **kwargs) -> tuple[int, dict]:
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                try:
                    code = func(argparse.Namespace(**kwargs))
                except UsageError:
                    return 2, {}
                except Refusal as exc:
                    return 1, {"error": str(exc)}
            return code, json.loads(stream.getvalue())

        manifest_path = root / "manifest.json"
        write_json_atomic(manifest_path, {"groups": [
            {"stem": "fresh", "integration_status": "returned", "bodies": ["parts/p01/a"]},
        ]})
        code, out = run(command_route, manifest=str(manifest_path), apply=True)
        assert code == 1 and out["groups_without_placement"][0]["stem"] == "fresh", out
        write_json_atomic(manifest_path, {"groups": [
            {"stem": "old", "integration_status": "routed-awaiting-canonical-merge",
             "bodies": ["parts/p01/b", "parts/p01/b-inner"], "annexes": []},
        ]})
        code, out = run(command_route, manifest=str(manifest_path), apply=False)
        assert code == 0 and out["groups_without_placement"][0]["stem"] == "old", out

        code, out = run(command_unroute, manifest=str(manifest_path), stems="old", apply=False)
        assert code == 0 and [a["removed"] for a in out["actions"]] == ["\\input{parts/p01/b}"], out
        assert "\\input{parts/p01/b}" in read_text(hb / "parts/p01.tex")
        code, out = run(command_unroute, manifest=str(manifest_path), stems="old", apply=True)
        assert code == 0, out
        assert read_text(hb / "parts/p01.tex") == "\\chapter{One}\n\\input{parts/p01/a}\n"
        assert "b-inner" in read_text(hb / "parts/p01/b.tex")
        assert load_json(manifest_path)["groups"][0]["integration_status"] == "returned-for-fix"
        code, out = run(command_unroute, manifest=str(manifest_path), stems="old", apply=False)
        assert code == 1, out

        delta = {"tag": None, "init": None, "stage": None, "manifest": None, "prev": None}
        assert run(command_check_delta, **dict(delta, stage="../up"))[0] == 2
        assert run(command_check_delta, **dict(delta, tag="t", prev="x"))[0] == 2
        code, out = run(command_check_delta, **dict(delta, stage="s1"))
        assert code == 1 and "run --init first" in out["error"], out
        (root / "tmp/integration/base").mkdir(parents=True)
        write_text_atomic(root / "tmp/integration/base/check-norm.txt", "")
        assert latest_check_store(exclude="s1") == "base"
        assert latest_check_store(exclude="base") is None

        write_text_atomic(hb / "registry/symbol-scopes.json",
                          json_text({"schema_version": 1, "scopes": {}}))
        write_text_atomic(hb / "registry/symbols.csv",
                          "glyph,macro,role,scope,precedence,first_use,notes\n")
        write_text_atomic(hb / "bib/handbook.bib",
                          "@book{Y,\n  title={Y},\n  author={C},\n  year={2001}\n}\n")
        write_text_atomic(hb / "bib/intake-g.bib",
                          "@book{X,\n  title={X},\n  author={D},\n  year={2002}\n}\n")
        write_text_atomic(hb / "registry/symbols-intake-g.csv",
                          "glyph,macro,role,scope,precedence,first_use,notes\n"
                          "\\(q\\),,query role,g local region,operator,sec:p01-a,\n")
        adopt_manifest = root / "manifest-adopt.json"
        decisions_path = root / "decisions.json"
        group = {"stem": "g", "part": "P1", "integration_status": "routed-awaiting-canonical-merge",
                 "bodies": ["parts/p01/a"], "annexes": [],
                 "symbol_intakes": ["registry/symbols-intake-g.csv"],
                 "bibliography_intakes": ["bib/intake-g.bib"]}
        write_json_atomic(adopt_manifest, {"groups": [group]})
        write_json_atomic(decisions_path, {})
        adopt_args = {"manifest": str(adopt_manifest), "decisions": str(decisions_path),
                      "return_json": None, "virtual_route": False}
        code, out = run(command_adopt, apply=False, **adopt_args)
        assert code == 0, out
        assert out["new_scope_bindings"] == ["g local region"], out
        assert out["new_bib_records"] == ["X"], out
        write_json_atomic(decisions_path, {"citation_aliases": {"X": "Y"},
                                           "bib_keep_canonical": {"X": "Y"}})
        code, out = run(command_adopt, apply=True, **adopt_args)
        assert code == 0 and not out["dry_run"], out
        scopes = load_json(hb / "registry/symbol-scopes.json")
        assert scopes["scopes"]["g local region"]["regions"] == [
            {"heading_of": "sec:p01-a", "level": "section"}
        ], scopes
        rows = list(csv.DictReader(io.StringIO(read_text(hb / "registry/symbols.csv"))))
        assert [(r["glyph"], r["macro"], r["precedence"]) for r in rows] == [
            (r"\(q\)", "q", "n/a")
        ], rows
        assert "@book{X" not in read_text(hb / "bib/handbook.bib")
        assert "\\cite{K1, Y}" in read_text(hb / "parts/p01/a.tex")
        assert load_json(adopt_manifest)["groups"][0]["integration_status"] == "merged"
        write_text_atomic(hb / "registry/symbols-intake-g.csv",
                          "glyph,macro,role,scope,precedence,first_use,notes\n"
                          "\\(r\\),r,role,P1.2 local,n/a,sec:p01-a,\n")
        write_json_atomic(adopt_manifest, {"groups": [group]})
        code, out = run(command_adopt, apply=False, **adopt_args)
        assert code == 1 and out["errors"][0]["error"] == "numeric scope forbidden", out
    finally:
        globals()["ROOT"] = old_root
        globals()["BASE"] = old_base


def selftest_repairs(temp: Path) -> None:
    """Fixtures for the repair-round defects (logs, numeric edits, hooks, routes, bib, cite)."""
    root = temp / "repairs"
    hb = root / "handbook"
    for folder in ("parts/p01", "registry/calculi", "bib"):
        (hb / folder).mkdir(parents=True)

    def run(func, **kwargs) -> tuple[int, dict]:
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            try:
                code = func(argparse.Namespace(**kwargs))
            except UsageError:
                return 2, {}
            except Refusal as exc:
                return 1, {"error": str(exc)}
        return code, json.loads(stream.getvalue())

    # Raw T1 byte 0xf6 in a TeX log and .blg: build-summary and scoped-build still give JSON.
    log = root / "t1.log"
    log.write_bytes(b"Overfull \\hbox (1.0pt too wide) in paragraph: H\xf6lder\n"
                    b"Output written on t1.pdf (3 pages, 10 bytes).\n")
    log.with_suffix(".blg").write_bytes(b"WARN - H\xf6lder\n")
    code, out = run(command_build_summary, log=str(log), prev=None)
    assert code == 0 and out["page_count"] == 3 and len(out["biber"]) == 1, out
    texlive = root / "texlive"
    texlive.mkdir()
    for exe in ("pdflatex.exe", "biber.exe"):
        (texlive / exe).write_bytes(b"")
    scoped_log = root / "snap/scoped/p15/scoped.log"
    scoped_log.parent.mkdir(parents=True)
    (root / "snap/handbook").mkdir(parents=True)
    old_bin, old_run = TEXLIVE_BIN, subprocess.run
    try:
        globals()["TEXLIVE_BIN"] = texlive
        subprocess.run = lambda command, **_kw: subprocess.CompletedProcess(command, 0, "", "")
        scoped_log.write_bytes(b"Overfull \\hbox in paragraph: H\xf6lder\n")
        code, out = run(command_scoped_build, snapshot=str(root / "snap"), parts="15")
        assert code == 0 and out["ok"], out
        scoped_log.write_bytes(b"! Undefined control sequence H\xf6lder.\n")
        code, out = run(command_scoped_build, snapshot=str(root / "snap"), parts="15")
        assert code == 1 and not out["ok"] and out["results"][0]["errors"], out
    finally:
        globals()["TEXLIVE_BIN"] = old_bin
        subprocess.run = old_run

    # Hooks: \AddToHookWithArguments brackets; \AddToHookNext pending until its command.
    assert insertion_inside_hook([r"\AddToHookWithArguments{env/x/begin}[n]{\relax}",
                                  r"\input{a}", r"\RemoveFromHook{env/x/begin}[n]"], 1)
    write_text_atomic(hb / "main.tex", "\\input{parts/p01}\n")
    write_text_atomic(hb / "parts/p01/a.tex", "\\chapter{A}\\label{sec:p01-a}\n")
    write_text_atomic(hb / "parts/p01/b.tex", "\\chapter{B}\\label{sec:p01-b}\n")
    write_text_atomic(hb / "parts/p01/n.tex", "\\chapter{N}\\label{sec:p01-n}\n")
    hooked = [r"\AddToHookNext{cmd/chapter/before}{%", r"  \label{sec:x}}",
              r"\input{parts/p01/a}", r"\input{parts/p01/b}"]
    assert insertion_before_hook_next_consumer(hooked, 1, hb)
    assert insertion_before_hook_next_consumer(hooked, 2, hb)
    assert not insertion_before_hook_next_consumer(hooked, 3, hb)
    assert insertion_before_hook_next_consumer(hooked, 3)  # no base: cannot see a.tex
    assert not insertion_before_hook_next_consumer(
        [r"\AddToHookNext{env/definition/end}{\relax}", r"\begin{definition}x\end{definition}",
         r"\input{parts/p01/a}"], 2)
    write_text_atomic(hb / "parts/p01.tex", "\n".join(hooked[:3]) + "\n")
    result = simulate_route(hb, [{"host": "parts/p01", "after": "parts/p01/a",
                                  "input": "parts/p01/n"}], apply=False)
    assert result["ok"], result
    write_text_atomic(hb / "parts/p01.tex",
                      "\\input{parts/p01/a}\n\\AddToHookNext{cmd/chapter/before}{\\relax}\n"
                      "\\input{parts/p01/b}\n")
    result = simulate_route(hb, [{"host": "parts/p01", "after": "parts/p01/a",
                                  "input": "parts/p01/n"}], apply=False)
    assert result["ok"], result  # inserted before the hook, not after it
    write_text_atomic(hb / "parts/p01.tex",
                      "\\AddToHookNext{cmd/chapter/before}{\\relax}\n\\input{parts/p01/x}\n"
                      "\\input{parts/p01/a}\n")
    write_text_atomic(hb / "parts/p01/x.tex", "No heading.\n")
    result = simulate_route(hb, [{"host": "parts/p01", "after": "parts/p01/x",
                                  "input": "parts/p01/n", "supplement_of": "parts/p01/x"}],
                            apply=False)
    assert not result["ok"] and "AddToHookNext" in result["errors"][0]["error"], result

    # Headings through wrapper files: the new file's first heading may not skip a level
    # below the heading in force at the insertion point (through wrappers and heading-less
    # continuation files; a commented-out heading does not count); a file without a
    # heading continues what is in force.
    write_text_atomic(hb / "parts/p01/w1.tex", "\\input{parts/p01/w1-inner}\n")
    write_text_atomic(hb / "parts/p01/w1-inner.tex", "\\section{W1}\n")
    write_text_atomic(hb / "parts/p01/w2.tex", "% \\section{fake}\n\\input{parts/p01/w2-inner}\n")
    write_text_atomic(hb / "parts/p01/w2-inner.tex", "\\chapter{W2}\n")
    write_text_atomic(hb / "parts/p01/w3.tex", "\\input{parts/p01/w1-inner}\n")
    write_text_atomic(hb / "parts/p01/plain1.tex", "Text.\n")
    write_text_atomic(hb / "parts/p01/plain2.tex", "More text.\n")
    write_text_atomic(hb / "parts/p01/w4.tex", "\\input{parts/p01/w4-inner}\n")
    write_text_atomic(hb / "parts/p01/w4-inner.tex", "\\subsection{W4}\n")
    write_text_atomic(hb / "parts/p01/w5.tex", "\\chapter{W5}\n")
    assert first_heading_kind(hb, "parts/p01/w2") == "chapter"
    write_text_atomic(hb / "parts/p01.tex", "\\input{parts/p01/w2}\n\\input{parts/p01/plain1}\n")
    after_plain = {"host": "parts/p01", "after": "parts/p01/plain1"}
    result = simulate_route(hb, [dict(after_plain, input="parts/p01/w4")], apply=False)
    assert not result["ok"] and result["errors"][0]["error"].startswith("heading level skip"), result
    assert (result["errors"][0]["input_heading"], result["errors"][0]["heading_in_force"]) == (
        "subsection", "chapter"), result
    for ok_input in ("parts/p01/w3", "parts/p01/plain2", "parts/p01/w5"):
        assert simulate_route(hb, [dict(after_plain, input=ok_input)], apply=False)["ok"], ok_input
    assert simulate_route(hb, [dict(after_plain, input="parts/p01/w4",
                                    supplement_of="parts/p01/plain1")], apply=False)["ok"]

    # Braceless \input already routes the file: no second \input.
    write_text_atomic(hb / "parts/p01.tex", "\\input{parts/p01/a}\n\\input parts/p01/b\n")
    result = simulate_route(hb, [{"host": "parts/p01", "after": "parts/p01/a",
                                  "input": "parts/p01/b"}], apply=False)
    assert result["ok"] and result["actions"][0]["action"] == "noop-already-present", result
    for disabled in ("\\iffalse\n\\ifx a b\\fi\n\\input{parts/p01/b}\n\\fi\n",
                     "\\begin{comment}\n\\input{parts/p01/b}\n\\end{comment}\n"):
        write_text_atomic(hb / "parts/p01.tex", "\\input{parts/p01/a}\n" + disabled)
        result = simulate_route(hb, [{"host": "parts/p01", "after": "parts/p01/a",
                                      "input": "parts/p01/b"}], apply=False)
        assert not result["ok"] and "iffalse" in result["errors"][0]["error"], result
        assert "parts/p01/b.tex" not in static_input_counts(hb)[0]

    # \calculussheet first_use in an owned rule sheet binds the whole sheet file.
    write_text_atomic(hb / "main.tex", "\\input{parts/p01}\n")
    write_text_atomic(hb / "parts/p01.tex", "\\input{parts/p01/a}\n\\input{registry/calculi/s}\n")
    write_text_atomic(hb / "registry/calculi/s.tex",
                      "\\calculussheet{sheet:p01-s}{S}\n\\hbrule{rule:p01-r}{R}\n")
    index = registry.ReaderIndex(hb)
    sheet_group = {"stem": "s", "rule_sheets": ["registry/calculi/s"]}
    for first in ("sheet:p01-s", "rule:p01-r"):
        selectors, foreign = local_regions_for_first_use(index, first, sheet_group)
        assert selectors == [{"file": "registry/calculi/s.tex"}] and foreign == [], selectors
        sheet_region = index.region(selectors[0])
        assert sheet_region.end - sheet_region.start >= 2

    # Adopt: canonical edits cannot introduce numeric scope/first_use; an unresolved
    # canonical first_use still takes part in collision decisions.
    write_text_atomic(hb / "registry/symbol-scopes.json",
                      json_text({"schema_version": 1, "scopes": {}}))
    symbols = ("glyph,macro,role,scope,precedence,first_use,notes\n"
               "\\(x\\),x,role,global,n/a,sec:p01-a,\n")
    write_text_atomic(hb / "registry/symbols.csv", symbols)
    write_text_atomic(hb / "bib/handbook.bib", "")
    manifest = root / "manifest.json"
    decisions = root / "decisions.json"
    write_json_atomic(manifest, {"groups": []})
    adopt_args = {"manifest": str(manifest), "decisions": str(decisions),
                  "return_json": None, "virtual_route": False}
    old_root, old_base = ROOT, BASE
    try:
        globals()["ROOT"] = root
        globals()["BASE"] = hb
        for edit in ({"scope": "P1.1"}, {"scope": "P1 \u2013 P1"}, {"first_use": "P1.1"}):
            write_json_atomic(decisions, {"canonical_row_edits": [{"line": 2, "set": edit}]})
            code, out = run(command_adopt, apply=True, **adopt_args)
            assert code == 1 and any(item.get("kind") == "canonical-row-edit"
                                     for item in out["errors"]), out
            assert read_text(hb / "registry/symbols.csv") == symbols
        write_text_atomic(hb / "registry/symbols.csv",
                          "glyph,macro,role,scope,precedence,first_use,notes\n"
                          "\\(q\\),q,other role,global,n/a,sec:missing,\n")
        write_text_atomic(hb / "registry/symbols-intake-g.csv",
                          "glyph,macro,role,scope,precedence,first_use,notes\n"
                          "\\(q\\),q,query role,g local region,n/a,sec:p01-a,\n")
        write_json_atomic(manifest, {"groups": [{
            "stem": "g", "integration_status": "routed-awaiting-canonical-merge",
            "bodies": ["parts/p01/a"], "annexes": [],
            "symbol_intakes": ["registry/symbols-intake-g.csv"], "bibliography_intakes": []}]})
        write_json_atomic(decisions, {})
        code, out = run(command_adopt, apply=False, **adopt_args)
        assert code == 1 and any(item.get("a_group") == "canonical"
                                 for item in out["decisions-needed"]), out

        # collect refuses duplicate stems; check-delta --init stays in tmp/integration.
        returns = []
        for name in ("r1.json", "r2.json"):
            write_json_atomic(root / name, {"stem": "n", "part": "P1", "bodies": ["parts/p01/a"]})
            returns.append(str(root / name))
        code, out = run(command_collect, wave=99, apply=False, return_json=returns)
        assert code == 1 and "duplicate stem" in out["error"], out
        delta = {"tag": None, "stage": None, "manifest": None, "prev": None}
        for bad in (str(root / "citations/x"), "citations/x", "tmp/integration/../x",
                    str(root / "tmp/integration/a/b")):
            assert run(command_check_delta, **dict(delta, init=bad))[0] == 2, bad
    finally:
        globals()["ROOT"] = old_root
        globals()["BASE"] = old_base

    # apply_adoption refuses when a canonical file changed after adopt read it.
    bib = hb / "bib/handbook.bib"
    write_text_atomic(bib, "@book{A,\n  title={A}\n}\n")
    try:
        apply_adoption({}, {"base": hb, "canonical_paths": [bib], "symbols_path": hb / "registry/symbols.csv",
                            "scopes_path": hb / "registry/symbol-scopes.json", "bib_path": bib,
                            "new_bib_text": "overwritten\n", "new_scopes_text": None,
                            "new_symbols_text": None, "citation_writes": {}, "manifest_updates": {},
                            "expected_texts": {bib: "@book{A,\n  title={old}\n}\n"}})
        assert False, "a concurrent canonical change must be refused"
    except Refusal as exc:
        assert "changed on disk" in str(exc)
    assert read_text(bib) == "@book{A,\n  title={A}\n}\n"

    # Bibliography: parenthesis entries are reported; arXiv versions and ISBN-10/13 match.
    canonical = ("@article{Arx,\n  title={One},\n  author={A},\n  year={2021},\n"
                 "  eprint={2101.00001}\n}\n"
                 "@book{Isbn,\n  title={Two},\n  author={B},\n  year={1990},\n"
                 "  isbn={978-0-306-40615-7}\n}\n")
    group = {"stem": "s", "bibliography_intakes": ["bib/intake-s.bib"]}
    for intake, kind in (
        ("@book(Fresh,\n  title={F},\n  author={C},\n  year={1999}\n)\n", "bib-unparsed-record"),
        ("@article{Arx2,\n  title={Other},\n  author={D},\n  year={2022},\n"
         "  eprint={2101.00001v2}\n}\n", "bib-duplicate-work"),
        ("@book{Isbn2,\n  title={Else},\n  author={E},\n  year={1991},\n"
         "  isbn={0-306-40615-2}\n}\n", "bib-duplicate-work"),
    ):
        write_text_atomic(hb / "bib/intake-s.bib", intake)
        append, needed, _comparisons = analyze_bibliography([group], {}, canonical, hb)
        assert append == [] and [item["kind"] for item in needed] == [kind], (intake, needed)

    # Cite rewriting: explicit command names; brace-aware optional arguments.
    aliases = {"X": "Y"}
    assert cite_alias_text(r"\excite{X} \citex{X}", aliases) == r"\excite{X} \citex{X}"
    assert cite_alias_text(r"\cite[{a]b}]{X}", aliases) == r"\cite[{a]b}]{Y}"
    assert cite_alias_text(r"\citep[see][{p]2}]{X, K} {X}", aliases) == r"\citep[see][{p]2}]{Y, K} {X}"
    assert cite_alias_text(r"\autocites(a)(b)[c]{X}{X}", aliases) == r"\autocites(a)(b)[c]{Y}{Y}"
    selftest_round3(temp)


def selftest_round3(temp: Path) -> None:
    """Fixtures for repair round 3: routed-only adopt, handbook cite sites, races, pins."""
    root = temp / "round3"
    hb = root / "handbook"
    for folder in ("parts/p01", "registry", "bib"):
        (hb / folder).mkdir(parents=True)
    pinned_rel = sorted(rel for rel in pinned_reader_files() if rel.startswith("parts/"))[0]
    pinned_path = hb / pinned_rel
    pinned_path.parent.mkdir(parents=True, exist_ok=True)
    main_text = "\\input{parts/p01}\n\\input{" + input_arg(pinned_rel) + "}\n"
    p01_text = "\\chapter{One}\n\\input{parts/p01/a}\n"
    a_text = ("\\section{A}\\label{sec:p01-a}\n\\cite{K1}\n"
              "\\begin{hbtheorem}{thm:p01-x}{cited=X}{T}\nBody.\n\\end{hbtheorem}\n"
              "\\entrysources{X,K1}\n")
    pinned_text = "\\section{P}\\label{sec:p01-pin}\n\\input{parts/p01/c}\n\\cite{X}\n"
    canonical_bib = "@book{K1,\n  title={Kept},\n  author={K},\n  year={2001}\n}\n"
    for rel, text in (("main.tex", main_text), ("parts/p01.tex", p01_text),
                      ("parts/p01/a.tex", a_text), ("parts/p01/b.tex", "\\section{B}\n"),
                      ("parts/p01/c.tex", "\\section{C}\n"),
                      ("parts/p01/off.tex", "\\section{Off}\\label{sec:p01-off}\n"),
                      ("parts/p01/h.tex", "\\section{H}\\label{sec:p01-h}\n\\cite{X}\n"),
                      (pinned_rel, pinned_text),
                      ("registry/symbol-scopes.json", json_text({"schema_version": 1, "scopes": {}})),
                      ("registry/symbols.csv", "glyph,macro,role,scope,precedence,first_use,notes\n"),
                      ("bib/handbook.bib", canonical_bib),
                      ("bib/intake-g.bib", "@book{X,\n  title={Alias},\n  author={D},\n  year={2002}\n}\n"),
                      ("bib/intake-n.bib", "@book{NewK,\n  title={New},\n  author={N},\n  year={2003}\n}\n")):
        write_text_atomic(hb / rel, text)

    # Citation sites: cite commands, \entrysources and {cited=...} status specs.
    assert cite_site_keys(a_text) == {"K1", "X"}
    assert cite_alias_text(a_text, {"X": "K1"}).count("K1") == 4
    status_text = (r"\entrysources{A, X} \begin{hblemma}{thm:a}{cited=X}{T} "
                   r"\begin{hbtheorem}{thm:b}{cited=XX}{T} \entryadequacy{ cited = X} "
                   r"\texttt{cited=X} {cited=X}")
    assert cite_alias_text(status_text, {"X": "Y"}) == status_text.replace(
        "{A, X}", "{A, Y}").replace("{thm:a}{cited=X}", "{thm:a}{cited=Y}").replace(
        "cited = X}", "cited = Y}")

    # Hook labels: omitted, '.' and 'top-level' name the same document-level chunk.
    assert insertion_inside_hook([r"\AddToHook{h}{\relax}", r"\input{a}",
                                  r"\RemoveFromHook{h}[top-level]"], 1)
    assert insertion_inside_hook([r"\AddToHook{h}[.]{\relax}", r"\input{a}",
                                  r"\RemoveFromHook{h}"], 2)
    assert not insertion_inside_hook([r"\AddToHook{h}[pkg]{\relax}", r"\input{a}",
                                      r"\RemoveFromHook{h}"], 1)
    try:
        insertion_inside_hook([r"\PushDefaultHookLabel{x}", r"\AddToHook{h}{\relax}"], 1)
        assert False, "a changed default hook label should be refused"
    except Refusal:
        pass

    # Anchor occurrences are counted, not anchor lines; pinned hosts are never edited.
    write_text_atomic(hb / "parts/p01.tex", "\\input{parts/p01/a}\\input{parts/p01/a}\n")
    result = simulate_route(hb, [{"host": "parts/p01", "after": "parts/p01/a",
                                  "input": "parts/p01/b"}], apply=False)
    assert not result["ok"] and result["errors"][0]["error"] == "anchor occurs 2 times", result
    write_text_atomic(hb / "parts/p01.tex", p01_text)
    result = simulate_route(hb, [{"host": pinned_rel, "after": "parts/p01/c",
                                  "input": "parts/p01/b"}], apply=True)
    assert not result["ok"] and "byte-pinned" in result["errors"][0]["error"], result
    assert read_text(pinned_path) == pinned_text

    def run(func, **kwargs) -> tuple[int, dict]:
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            try:
                code = func(argparse.Namespace(**kwargs))
            except Refusal as exc:
                return 1, {"error": str(exc)}
        return code, json.loads(stream.getvalue())

    manifest = root / "manifest.json"
    decisions = root / "decisions.json"
    adopt_args = {"manifest": str(manifest), "decisions": str(decisions),
                  "return_json": None, "virtual_route": False}
    routed = "routed-awaiting-canonical-merge"
    group_g = {"stem": "g", "integration_status": routed, "bodies": ["parts/p01/a"],
               "annexes": [], "symbol_intakes": [], "bibliography_intakes": ["bib/intake-g.bib"]}
    old_root, old_base, old_validate = ROOT, BASE, symbol_validation_failures_from_text
    try:
        globals()["ROOT"] = root
        globals()["BASE"] = hb
        write_json_atomic(decisions, {})
        # Unrouted statuses and off-route bodies are refused; nothing is written.
        for status, body in (("returned", "parts/p01/off"), ("returned-for-fix", "parts/p01/off"),
                             (routed, "parts/p01/off")):
            write_json_atomic(manifest, {"groups": [{
                "stem": "n", "integration_status": status, "bodies": [body], "annexes": [],
                "symbol_intakes": [], "bibliography_intakes": ["bib/intake-n.bib"]}]})
            before = read_text(manifest)
            code, out = run(command_adopt, apply=True, **adopt_args)
            kind = "not-on-route" if status == routed else "group-not-routed"
            assert code == 1 and [item.get("kind") for item in out["errors"]] == [kind], out
            assert read_text(hb / "bib/handbook.bib") == canonical_bib
            assert read_text(manifest) == before

        # A manifest-level unroute quarantine wins over the prior manifest's routed copy.
        prior = root / "prior.json"
        write_json_atomic(prior, {"groups": [dict(group_g, stem="n")]})
        write_json_atomic(manifest, {"prior_manifest": str(prior), "groups": [{
            "stem": "n", "integration_status": "returned-for-fix", "bodies": ["parts/p01/a"]}]})
        code, out = run(command_adopt, apply=False, **adopt_args)
        assert code == 1 and out["groups"] == [] and out["errors"][0]["kind"] == "group-not-routed", out

        # A concurrent manifest edit after adopt read it is refused, not overwritten.
        write_json_atomic(decisions, {"citation_aliases": {"X": "K1"}})
        write_json_atomic(manifest, {"groups": [group_g, {"stem": "other",
                                                          "integration_status": "saved-off-route"}]})
        concurrent = json_text({"groups": [group_g, {"stem": "other", "integration_status": "routed",
                                                     "note_kept": True}]})

        def racing_validate(*a, **kw):
            write_text_atomic(manifest, concurrent)
            return old_validate(*a, **kw)

        globals()["symbol_validation_failures_from_text"] = racing_validate
        code, out = run(command_adopt, apply=True, **adopt_args)
        globals()["symbol_validation_failures_from_text"] = old_validate
        assert code == 1 and "changed on disk" in out["error"], out
        assert read_text(manifest) == concurrent and read_text(hb / "parts/p01/a.tex") == a_text

        # Aliases are rewritten at every handbook citation site and none is left behind.
        write_json_atomic(manifest, {"groups": [group_g]})
        code, out = run(command_adopt, apply=True, **adopt_args)
        assert code == 0 and out["ok"], out
        rewritten = read_text(hb / "parts/p01/a.tex")
        assert "{cited=K1}" in rewritten and "\\entrysources{K1,K1}" in rewritten, rewritten
        assert cite_site_keys(rewritten) == {"K1"}
        assert "@book{X" not in read_text(hb / "bib/handbook.bib")
        assert load_json(manifest)["groups"][0]["integration_status"] == "merged"

        # Another routed group still citing the aliased-away key is an error.
        write_text_atomic(hb / "parts/p01.tex", p01_text + "\\input{parts/p01/h}\n")
        write_text_atomic(hb / "parts/p01/a.tex", a_text)
        group_h = {"stem": "h", "integration_status": routed, "bodies": ["parts/p01/h"]}
        write_json_atomic(manifest, {"groups": [group_g, group_h]})
        code, out = run(command_adopt, apply=False, **adopt_args)
        assert code == 1 and [(item["group"], item["kind"], item["keys"]) for item in out["errors"]] == [
            ("h", "alias-left-at-citation-site", ["X"])], out

        # A citation rewrite never edits a check.py-pinned file.
        # (The group owns c too: the pinned file routes it, so it is no shared route host.)
        write_json_atomic(manifest, {"groups": [dict(group_g, bodies=[pinned_rel, "parts/p01/c"])]})
        code, out = run(command_adopt, apply=True, **adopt_args)
        assert code == 1 and out["errors"][0]["kind"] == "pinned-file-rewrite", out
        assert read_text(pinned_path) == pinned_text

        # Unroute removes only the \input span; a line left with no active content goes.
        write_text_atomic(hb / "parts/p01.tex",
                          "\\chapter{One}\n\\input{parts/p01/a}\n"
                          "\\clearpage\\input{parts/p01/b}\\input{parts/p01/c}\n"
                          "\\input{parts/p01/h} % routes h\n")
        write_json_atomic(manifest, {"groups": [
            {"stem": "b", "integration_status": routed, "placements": [
                {"host": "parts/p01", "after": "parts/p01/a", "input": "parts/p01/b"},
                {"host": "parts/p01", "after": "parts/p01/a", "input": "parts/p01/h"}]}]})
        code, out = run(command_unroute, manifest=str(manifest), stems="b", apply=True)
        assert code == 0, out
        assert read_text(hb / "parts/p01.tex") == (
            "\\chapter{One}\n\\input{parts/p01/a}\n\\clearpage\\input{parts/p01/c}\n"), out
    finally:
        globals()["ROOT"] = old_root
        globals()["BASE"] = old_base
        globals()["symbol_validation_failures_from_text"] = old_validate


def selftest_round4(temp: Path) -> None:
    """Fixtures for repair round 4: disabled hook removes, active-only cite sites, log stack."""
    hb = temp / "round4" / "handbook"
    (hb / "parts/p01").mkdir(parents=True)
    write_text_atomic(hb / "main.tex", "\\input{parts/p01}\n")
    for name in ("a", "c", "n"):
        write_text_atomic(hb / f"parts/p01/{name}.tex", f"\\section{{{name}}}\n")

    # A disabled \RemoveFromHook never closes the bracket of a live \AddToHook.
    add = r"\AddToHook{env/x/begin}[n]{\relax}"
    remove = r"\RemoveFromHook{env/x/begin}[n]"
    for disabled in ([r"\iffalse " + remove + r" \fi"],
                     [r"\begin{comment}", remove, r"\end{comment}"]):
        lines = [add, r"\input{parts/p01/a}", *disabled, r"\input{parts/p01/c}", remove]
        assert insertion_inside_hook(lines, len(lines) - 1), lines
        write_text_atomic(hb / "parts/p01.tex", "\n".join(lines) + "\n")
        result = simulate_route(hb, [{"host": "parts/p01", "after": "parts/p01/c",
                                      "input": "parts/p01/n"}], apply=False)
        assert not result["ok"] and "AddToHook" in result["errors"][0]["error"], result
    # A live remove still closes it; a disabled add still opens one (wider, never narrower).
    assert not insertion_inside_hook([add, r"\input{a}", remove, r"\input{c}"], 3)
    assert insertion_inside_hook([r"\iffalse " + add + r" \fi", r"\input{a}", remove], 1)

    # Unroute without placements counts only live \input lines.
    host_lines = {"parts/p01.tex": [r"\input{parts/p01/c}", r"\iffalse", r"\input{parts/p01/c}",
                                    r"\fi"]}
    group = {"stem": "s", "bodies": ["parts/p01/c"]}
    assert located_route_inputs(hb, group, host_lines) == ([("parts/p01.tex", "parts/p01/c.tex")], [])
    host_lines["parts/p01.tex"].append(r"\input{parts/p01/c}")
    assert "2 times" in located_route_inputs(hb, group, host_lines)[1][0]["error"]

    # Headings: a ']' inside braces does not end the optional argument.
    assert iter_headings(r"\subsection[{a]b}]{B}") == [(0, "subsection")]
    assert iter_headings(r"\section[x] {B} \sectionmark{x} \section[{a]") == [(0, "section")]
    write_text_atomic(hb / "parts/p01/n.tex", "\\subsection[{a]b}]{N}\n")
    write_text_atomic(hb / "parts/p01/c.tex", "\\subsection{C}\n")
    write_text_atomic(hb / "parts/p01.tex", "\\input{parts/p01/c}\n")
    assert simulate_route(hb, [{"host": "parts/p01", "after": "parts/p01/c",
                                "input": "parts/p01/n"}], apply=False)["ok"]

    # Citation aliases: only active text; multicite arguments stop at a blank line.
    aliases = {"X": "Y"}
    assert cite_alias_text("\\cite{A,% X here\n X}", aliases) == "\\cite{A,% X here\n Y}"
    assert cite_alias_text(r"\verb|\cite{X}| \cite{X}", aliases) == r"\verb|\cite{X}| \cite{Y}"
    assert cite_alias_text("\\cites{X}\n\n{X marks}", aliases) == "\\cites{Y}\n\n{X marks}"
    assert cite_alias_text("\\cites{X}\n% c\n{X}", aliases) == "\\cites{Y}\n% c\n{Y}"
    verbatim = "\\begin{verbatim}\n\\cite{X}\n\\end{verbatim}\n\\cite{X}\\%\\cite{X}"
    assert cite_alias_text(verbatim, aliases) == (
        "\\begin{verbatim}\n\\cite{X}\n\\end{verbatim}\n\\cite{Y}\\%\\cite{Y}")
    assert cite_site_keys("\\cite{A}% \\cite{X}\n\\verb+\\cite{X}+") == {"A"}

    # Overfull boxes go to the file open at that point, not the last file named.
    log = temp / "round4" / "stack.log"
    write_text_atomic(log, "(./main.tex\n(./parts/p01.tex\n"
                           "Overfull \\hbox (1.0pt too wide) in paragraph at lines 1--2\n"
                           "[]\\T1/cmr/m/n/10 (unbalanced\n\n"
                           ") (./parts/p02.tex\n)\n"
                           "Overfull \\hbox (2.0pt too wide) in paragraph at lines 9--9\n[]\n\n)\n")
    assert parse_build_summary(log)["overfull"] == {"parts/p01.tex": 1, "main.tex": 1}

    # ISBN fields listing several ISBNs give one locator each.
    assert isbn_values("978-0-306-40615-7; 0-306-40615-2") == ["9780306406157"] * 2
    assert isbn_values("978 0 306 40615 7") == ["9780306406157"]
    assert isbn_values("9780306406157 0198537793") == ["9780306406157", "9780198537793"]
    (hb / "bib").mkdir()
    canonical = ("@book{Multi,\n  title={Three},\n  author={F},\n  year={1980},\n"
                 "  isbn={0-19-853779-3; 978-0-306-40615-7}\n}\n")
    write_text_atomic(hb / "bib/intake-s.bib", "@book{Single,\n  title={Other},\n  author={G},\n"
                                               "  year={1981},\n  isbn={9780306406157}\n}\n")
    append, needed, _comparisons = analyze_bibliography(
        [{"stem": "s", "bibliography_intakes": ["bib/intake-s.bib"]}], {}, canonical, hb)
    assert append == [] and [item["kind"] for item in needed] == ["bib-duplicate-work"], needed


def selftest_round5(temp: Path) -> None:
    """Fixtures for repair round 5: family edits, cross-group annex items, commented bib
    entries, canonical presentations, pinned route inputs, verbatim masking, CSV."""
    root = temp / "round5"
    hb = root / "handbook"
    pinned_rel = sorted(rel for rel in pinned_reader_files() if rel.startswith("parts/"))[0]
    files = {
        "main.tex": "\\input{parts/p01}\n\\input{annex/p01}\n",
        "parts/p01.tex": "\\chapter{One}\n\\input{parts/p01/a}\n",
        "parts/p01/a.tex": ("\\section{A}\\label{sec:p01-a}\n\\subsection{S}\\label{sec:p01-s}\n"
                            "\\begin{hbtheorem}{thm:p01-t}{proved=annex:p01.t}{T}\nx\n"
                            "\\end{hbtheorem}\n\\begin{hbdefinition}{def:p01-d}{D}\nx\n"
                            "\\end{hbdefinition}\n"),
        "parts/p01/b.tex": "\\section{B}\n",
        "parts/p01/v.tex": "\\section{V}\n",
        "parts/p01/wrap.tex": "\\section{W}\n\\input{" + input_arg(pinned_rel) + "}\n",
        pinned_rel: "\\section{Pinned}\n",
        "annex/p01.tex": "\\input{annex/p01/other}\n",
        "annex/p01/other.tex": ("\\begin{annexitem}{annex:p01.t}{thm:p01-t}{T}\nProof.\n"
                                "\\end{annexitem}\n"),
        "registry/symbol-scopes.json": json_text({"schema_version": 1, "scopes": {
            "keep": {"presentation": "Original", "regions": [{"anchor": "sec:p01-a"}]}}}),
        "registry/symbols.csv": "glyph,macro,role,scope,precedence,first_use,notes\n",
        "bib/handbook.bib": "@book{K1,\n  title={Kept},\n  author={K},\n  year={2001}\n}\n",
        "registry/symbols-intake-g.csv": ("glyph,macro,role,scope,precedence,first_use,notes\n"
                                          '"\\(a,b\\)",,pair,g region,n/a,sec:p01-a,\n'),
    }
    for rel, text in files.items():
        write_text_atomic(hb / rel, text)
    index = registry.ReaderIndex(hb)

    # Only the group's own annex items join the binding of their owner's region; an item
    # in another annex file is returned for a decision instead.
    selectors, foreign = local_regions_for_first_use(
        index, "sec:p01-a", {"stem": "g", "bodies": ["parts/p01/a"]})
    assert selectors == [{"heading_of": "sec:p01-a", "level": "section"}], selectors
    assert foreign == [{"kind": "binding-foreign-annexitem", "anchor": "annex:p01.t",
                        "path": "annex/p01/other.tex"}], foreign
    selectors, foreign = local_regions_for_first_use(
        index, "sec:p01-a", {"stem": "g", "bodies": ["parts/p01/a"], "annexes": ["annex/p01/other"]})
    assert selectors == [{"heading_of": "sec:p01-a", "level": "section"},
                         {"anchor": "annex:p01.t"}] and foreign == [], selectors

    def run(func, **kwargs) -> tuple[int, dict]:
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            try:
                code = func(argparse.Namespace(**kwargs))
            except Refusal as exc:
                return 1, {"error": str(exc)}
        return code, json.loads(stream.getvalue())

    manifest = root / "manifest.json"
    decisions = root / "decisions.json"
    adopt_args = {"manifest": str(manifest), "decisions": str(decisions),
                  "return_json": None, "virtual_route": False}
    group = {"stem": "g", "integration_status": "routed-awaiting-canonical-merge",
             "bodies": ["parts/p01/a"], "annexes": ["annex/p01/other"],
             "symbol_intakes": ["registry/symbols-intake-g.csv"], "bibliography_intakes": []}
    old_root, old_base = ROOT, BASE
    try:
        globals()["ROOT"] = root
        globals()["BASE"] = hb
        write_json_atomic(manifest, {"groups": [group]})
        symbols_before = read_text(hb / "registry/symbols.csv")
        # A role/macro edit of a family row is refused; nothing is written.
        write_json_atomic(decisions, {"row_edits": [
            {"group": "g", "line": 2, "set": {"role": "edited", "macro": "E"}, "reason": "d"}]})
        code, out = run(command_adopt, apply=True, **adopt_args)
        assert code == 1 and [e.get("kind") for e in out["errors"]] == ["family-row-edit"], out
        assert out["prospective_symbol_validation_failures_count"] is None, out
        assert read_text(hb / "registry/symbols.csv") == symbols_before
        # A first_use edit reaches every member row and its synthesized binding.
        write_json_atomic(decisions, {"row_edits": [
            {"group": "g", "line": 2, "set": {"first_use": "sec:p01-s"}, "reason": "d"}]})
        code, out = run(command_adopt, apply=True, **adopt_args)
        assert code == 0 and out["new_symbol_rows"] == 2, out
        rows = list(csv.DictReader(io.StringIO(read_text(hb / "registry/symbols.csv"))))
        assert [(r["glyph"], r["first_use"]) for r in rows] == [
            (r"\(a\)", "sec:p01-s"), (r"\(b\)", "sec:p01-s")], rows
        scopes = load_json(hb / "registry/symbol-scopes.json")["scopes"]
        assert scopes["g region"]["regions"][0] == {"heading_of": "sec:p01-s", "level": "subsection"}

        # Decisions may not rewrite an existing canonical scope's presentation.
        write_json_atomic(manifest, {"groups": []})
        for kind, item in (("extend_scopes", {"scope": "keep", "presentation": "Hijacked",
                                              "regions": []}),
                           ("overrides", {"scope": "keep", "presentation": "Hijacked",
                                          "rule": {"glyph": "x"}})):
            write_json_atomic(decisions, {kind: [item]})
            code, out = run(command_adopt, apply=True, **adopt_args)
            assert code == 1 and out["errors"][0]["kind"] == "decision-scope-presentation", out
        assert load_json(hb / "registry/symbol-scopes.json")["scopes"]["keep"]["presentation"] == "Original"

        # An extra unquoted comma outside braces is a CSV parse failure, not a realignment.
        write_text_atomic(hb / "registry/symbols-intake-g.csv",
                          "glyph,macro,role,scope,precedence,first_use,notes\n"
                          "\\(c\\),c,role a, b,h region,n/a,sec:p01-a,\n"
                          "\\(d\\),{x,y},role,h region,n/a,sec:p01-a,\n")
        write_json_atomic(manifest, {"groups": [group]})
        write_json_atomic(decisions, {})
        code, out = run(command_adopt, apply=False, **adopt_args)
        assert code == 1 and [(e.get("line"), e["error"]) for e in out["errors"]] == [
            (2, "CSV parse failure")], out
        assert out["input_symbol_rows"] == 1, out
    finally:
        globals()["ROOT"] = old_root
        globals()["BASE"] = old_base

    # Bibliography: commented-out entries are skipped and reported; an entry left
    # unterminated once comments are masked is refused; apply rolls back a bad merge.
    commented = "% @book{Old,\n%  title={Old},\n% }\n@book{New,\n  title={N}, % a {note\n  year={1}\n}\n"
    assert [r["key"] for r in bib_records(commented)] == ["New"]
    assert commented_bib_entries(commented) == ["% @book{Old,"[2:]] and unparsed_bib_entries(commented) == []
    assert bib_records("@misc{U,\n  url={http://x.org/a%20b}\n}\n")[0]["key"] == "U"
    assert [r["key"] for r in bib_records("@book{A,\n  note={x\n% }\n}\n@book{B,\n}\n")] == ["A", "B"]
    for broken in ("@book{Half,\n  title={T}\n% }\n", "@book{A,\n  title={x}\n% }\n@book{B,\n}\n}\n"):
        try:
            bib_records(broken)
            assert False, broken
        except Refusal:
            pass
    write_text_atomic(hb / "bib/intake-s.bib", commented)
    append, needed, comparisons = analyze_bibliography(
        [{"stem": "s", "bibliography_intakes": ["bib/intake-s.bib"]}], {},
        read_text(hb / "bib/handbook.bib"), hb)
    assert [r["key"] for r in append] == ["New"] and needed == [], needed
    assert [c["decision"] for c in comparisons] == ["skip-commented-out-entry"], comparisons
    assert bib_text_errors("@book{K1,\n}\n@book{X,\n % }\n", ["K1", "X"])
    for intake, kind in (("@book{k1,\n  title={Other},\n  author={Z},\n  year={1999}\n}\n",
                          "bib-key-case-conflict"),
                         ("@book{K2,\n  title={Kept.},\n  author={{K}},\n  year={2001}\n}\n",
                          "bib-duplicate-work")):
        write_text_atomic(hb / "bib/intake-s.bib", intake)
        append, needed, _comparisons = analyze_bibliography(
            [{"stem": "s", "bibliography_intakes": ["bib/intake-s.bib"]}], {},
            read_text(hb / "bib/handbook.bib"), hb)
        assert append == [] and [item["kind"] for item in needed] == [kind], needed
    for scope in ("P10,1", "P10_1", "P10/1", "P10:1", "Ｐ10.1", "P１０.1"):
        assert numeric_scope_forbidden(scope), scope
    bib = hb / "bib/handbook.bib"
    bib_before = read_text(bib)
    try:
        apply_adoption({}, {"base": hb, "canonical_paths": [bib],
                            "symbols_path": hb / "registry/symbols.csv",
                            "scopes_path": hb / "registry/symbol-scopes.json", "bib_path": bib,
                            "new_bib_text": bib_before + "@book{X,\n % }\n",
                            "expected_bib_keys": ["K1", "X"],
                            "new_scopes_text": None, "new_symbols_text": None,
                            "citation_writes": {}, "manifest_updates": {}})
        assert False, "an unreadable merged bibliography must be refused"
    except Refusal as exc:
        assert "bibliography" in str(exc)
    assert read_text(bib) == bib_before

    # Route: inputs that are, or input, pinned retained files are refused.
    for target in (pinned_rel, "parts/p01/wrap"):
        result = simulate_route(hb, [{"host": "parts/p01", "after": "parts/p01/a", "input": target,
                                      "supplement_of": "parts/p01/a"}], apply=False)
        assert not result["ok"] and "byte-pinned" in result["errors"][0]["error"], result

    # Verbatim, \lstinline and \mintinline spans are not live TeX.
    write_text_atomic(hb / "parts/p01.tex", "\\chapter{One}\n\\input{parts/p01/a}\n"
                      "\\begin{verbatim}\n\\input{parts/p01/v}\n\\end{verbatim}\n")
    result = simulate_route(hb, [{"host": "parts/p01", "after": "parts/p01/v",
                                  "input": "parts/p01/b"}], apply=False)
    assert not result["ok"] and result["errors"][0]["error"] == "anchor occurs 0 times", result
    assert "parts/p01/v.tex" not in static_input_counts(hb)[0]
    write_text_atomic(hb / "parts/p01/v.tex",
                      "\\begin{verbatim}\n\\chapter{Fake}\n\\end{verbatim}\n\\section{V}\n")
    assert first_heading_kind(hb, "parts/p01/v") == "section"
    aliases = {"X": "Y"}
    for text in (r"\lstinline|\cite{X}|", r"\lstinline[language=TeX]{\cite{X}}",
                 r"\mintinline{latex}|\cite{X}|", r"\mintinline{latex}{\cite{X}}"):
        assert cite_alias_text(text + r" \cite{X}", aliases) == text + r" \cite{Y}", text


def selftest_round6(temp: Path) -> None:
    """Fixtures for repair round 6: native supplements, guarded specials, delimiter-aware
    families, owned annex bindings, line separators, volcite, @string, numeric scopes,
    hook spellings, definition bodies, in-place manifest edits, invalid scopes JSON."""
    # Native supplements are added to their group; an unknown stem is an error.
    groups = [{"stem": "p09-recombination-models", "symbol_intakes": [P09_MODELS]}]
    errors = add_native_supplements(groups, [
        {"groups": [{"stem": "p09-recombination-models"}],
         "source_native_repairs": [{"stem": "p09-recombination-models", "supplement": P09_NATIVE},
                                   {"stem": "p09-recombination-iteration"}]}, {}])
    assert errors == [] and groups[0]["symbol_intakes"] == [P09_MODELS, P09_NATIVE], groups
    errors = add_native_supplements([], [{"groups": [], "source_native_repairs": [
        {"stem": "ghost", "supplement": "registry/x.csv"}]}])
    assert [e["kind"] for e in errors] == ["source-native-repair-unknown-stem"], errors

    def cells(glyph: str, role: str) -> dict:
        return {"glyph": glyph, "macro": "", "role": role, "scope": "s", "precedence": "n/a",
                "first_use": "sec:x", "notes": ""}

    def refused(*args) -> bool:
        try:
            actual_row(*args)
        except IntakeRowError:
            return True
        return False

    # A row superseded by a native record stays active-blocking unless that intake is adopted.
    models = {"stem": "p09-recombination-models"}
    epsilon = cells("epsilon", "literal empty word")
    assert refused(epsilon, models, P09_MODELS, 8, None, {P09_MODELS})
    assert actual_row(epsilon, models, P09_MODELS, 8, None, {P09_MODELS, P09_NATIVE})[1]
    # Specials apply only to the recorded content of the recorded intake.
    search = {"stem": "p18-erotetic-search"}
    assert refused(cells("z", "unrelated z"), search, P18_SEARCH, 4, None, {P18_SEARCH})
    row, inactive = actual_row(cells("Q X", "Principal question and initial basis"), search,
                               P18_SEARCH, 4, None, {P18_SEARCH})
    assert inactive is None and [m["glyph"] for m in row["_members"]] == [r"\(Q\)", r"\(X\)"]
    adequacy = {"stem": "p10-operational-adequacy"}
    succ = cells(r"\(\operatorname{succ}\)", "Gunter PCF numerical successor term constructor")
    assert actual_row(succ, adequacy, P10_ADEQUACY, 29, dict(succ), {P10_ADEQUACY})[1]
    assert refused(succ, adequacy, P10_ADEQUACY, 29, cells("x", "y"), {P10_ADEQUACY})
    assert actual_row(succ, adequacy, "registry/other.csv", 29, None, set())[1] is None

    # Commas inside paired delimiters do not split a glyph; ambiguous commas are refused.
    for glyph in (r"?\pm|A,B|", r"\langle a,b\rangle", r"\left( a,b \right)", r"\{a,b\}",
                  "[0,1)", r"\lVert a,b\rVert", "F_r(s,t)"):
        assert family_members(glyph) == [glyph], glyph
    assert family_members("a,b") == ["a", "b"]
    assert family_members("|w|,|v|") == ["|w|", "|v|"]
    assert family_members(r"\mathopen{(\!(}_r") == [r"\mathopen{(\!(}_r"]
    for glyph in ("a|b,c", r"\langle a,b", "a,", r"\rangle a,b"):
        try:
            family_members(glyph)
            assert False, glyph
        except IntakeRowError:
            pass
    native = {"stem": "p18-erotetic-search"}
    row, _inactive = actual_row(cells(r"\(?\pm|A,B|\)", "native"), native, P18_NATIVE, 4,
                                None, {P18_NATIVE})
    assert row["glyph"] == r"\(?\pm|A,B|\)" and not row.get("_members"), row
    assert refused(cells(r"\(\langle a,b\)", "r"), {"stem": "g"}, "registry/g.csv", 2, None, set())

    # Route and unroute split host lines at "\n" only: \f and U+2028 stay in their lines.
    hb = temp / "round6" / "handbook"
    (hb / "parts/p01").mkdir(parents=True)
    write_text_atomic(hb / "main.tex", "\\input{parts/p01}\n")
    for name in ("a", "c"):
        write_text_atomic(hb / f"parts/p01/{name}.tex", f"\\section{{{name}}}\n")
    host = "\\chapter{One}\n\f x\u2028y\x1c\n\\input{parts/p01/a}\n% end\n"
    write_text_atomic(hb / "parts/p01.tex", host)
    result = simulate_route(hb, [{"host": "parts/p01", "after": "parts/p01/a",
                                  "input": "parts/p01/c"}], apply=True)
    assert result["ok"], result
    assert read_text(hb / "parts/p01.tex") == host.replace(
        "\\input{parts/p01/a}\n", "\\input{parts/p01/a}\n\\input{parts/p01/c}\n")
    manifest_text = ('{\n "groups": [\n  {\n   "stem": "s",\n   "integration_status": "routed",\n'
                     '   "placement": {"host": "parts/p01", "after": "parts/p01/a", '
                     '"input": "parts/p01/c"}\n  },\n  {"stem": "t", "integration_status": "x"}\n'
                     ' ]\n}\n')
    manifest_path = temp / "round6" / "manifest.json"
    write_text_atomic(manifest_path, manifest_text)
    old_root, old_base = ROOT, BASE
    try:
        globals()["ROOT"] = temp / "round6"
        globals()["BASE"] = hb
        with contextlib.redirect_stdout(io.StringIO()):
            code = command_unroute(argparse.Namespace(manifest=str(manifest_path), stems="s",
                                                      apply=True))
        assert code == 0
        assert read_text(hb / "parts/p01.tex") == host
        # Only the status value changed; the indent=1 layout is kept byte for byte.
        assert read_text(manifest_path) == manifest_text.replace(
            '"integration_status": "routed"', '"integration_status": "returned-for-fix"')

        # Adopt refuses an unparseable symbol-scopes.json with a checked refusal.
        (hb / "registry").mkdir()
        (hb / "bib").mkdir()
        write_text_atomic(hb / "registry/symbols.csv", ",".join(FIELDS) + "\n")
        write_text_atomic(hb / "registry/symbol-scopes.json", "{not json")
        write_text_atomic(hb / "bib/handbook.bib", "")
        write_json_atomic(temp / "round6" / "decisions.json", {})
        write_json_atomic(temp / "round6" / "adopt.json", {"groups": []})
        try:
            command_adopt(argparse.Namespace(
                manifest=str(temp / "round6" / "adopt.json"),
                decisions=str(temp / "round6" / "decisions.json"),
                apply=False, return_json=None, virtual_route=False))
            assert False, "invalid symbol-scopes.json must be refused"
        except Refusal as exc:
            assert "invalid symbol-scopes.json" in str(exc)
    finally:
        globals()["ROOT"] = old_root
        globals()["BASE"] = old_base
    status_text = manifest_text_with_status(manifest_text, {"t"}, "merged")
    assert status_text == manifest_text.replace('"x"', '"merged"'), status_text

    # volcite forms are rewritten; any other *cite* command is read fail-closed.
    aliases = {"NewKey": "Old"}
    assert cite_alias_text(r"\volcite[see]{2}[12]{NewKey}", aliases) == r"\volcite[see]{2}[12]{Old}"
    assert cite_alias_text(r"\volcites{1}{NewKey}{2}{NewKey}", aliases) == (
        r"\volcites{1}{Old}{2}{Old}")
    assert cite_alias_text(r"\volcite{NewKey}{x}", aliases) == r"\volcite{NewKey}{x}"
    assert "NewKey" in cite_site_keys(r"\mycustomcite[p]{NewKey}", any_cite_command=True)
    assert "NewKey" not in cite_site_keys(r"\mycustomcite[p]{NewKey}")

    # @string/@preamble in an intake and undefined bare macros are decisions, not appends.
    write_text_atomic(hb / "bib/intake-s.bib",
                      '@string{jx = "Journal X"}\n'
                      "@article{Other,\n title={O},\n author={A},\n year={2024},\n journal=jx\n}\n"
                      "@article{Month,\n title={M},\n author={B},\n year={2024},\n month=jan\n}\n")
    append, needed, _comparisons = analyze_bibliography(
        [{"stem": "s", "bibliography_intakes": ["bib/intake-s.bib"]}], {}, "", hb)
    assert [r["key"] for r in append] == ["Month"], append
    assert [item["kind"] for item in needed] == ["bib-string-or-preamble", "bib-undefined-macro"], needed
    append, needed, _comparisons = analyze_bibliography(
        [{"stem": "s", "bibliography_intakes": ["bib/intake-s.bib"]}], {},
        '@STRING{JX = "Journal X"}\n', hb)
    assert [r["key"] for r in append] == ["Other", "Month"], append
    assert [item["kind"] for item in needed] == ["bib-string-or-preamble"], needed

    # Numeric scopes with any separator between part and ordinal; a year is not an ordinal.
    for scope in ("P1-3", "P6–3", "P6·3", "P1 3", "P6 — 12 forcing"):
        assert numeric_scope_forbidden(scope), scope
    for scope in ("P8 1946 Brouwerian algebra", "P13 consequence operations",
                  "P9 recombination development native words"):
        assert not numeric_scope_forbidden(scope), scope

    # Hook spellings that cannot be paired are refused.
    for hook in (r"\csname AddToHook\endcsname{env/x/begin}{\relax}",
                 r"\ExplSyntaxOn \hook_gput_code:nnn {env/x/begin} {n} {\relax}"):
        try:
            insertion_inside_hook([hook, r"\input{parts/p01/a}"], 1)
            assert False, hook
        except Refusal:
            pass
    # A heading inside a macro definition body is not the file's first heading.
    write_text_atomic(hb / "parts/p01/d.tex",
                      "\\newcommand{\\x}[1][a]{\\section{#1}}\n\\def\\y#1{\\chapter{#1}}\n"
                      "\\renewcommand*\\z{\\section{Z}}\n\\subsection{Real}\n")
    assert first_heading_kind(hb, "parts/p01/d") == "subsection"
    result = simulate_route(hb, [{"host": "parts/p01", "before": "parts/p01/a",
                                  "input": "parts/p01/d"}], apply=False)
    assert not result["ok"] and result["errors"][0]["error"].startswith("heading level skip"), result
    # Nor is one in a definition body before the insertion point the heading in force.
    write_text_atomic(hb / "parts/p01/e.tex", "\\newcommand{\\w}{\\section{W}}\n")
    write_text_atomic(hb / "parts/p01.tex", "\\chapter{One}\n\\input{parts/p01/e}\n"
                      "\\input{parts/p01/a}\n")
    assert heading_in_force(hb, "parts/p01.tex", 2) == "chapter"
    assert heading_in_force(hb, "parts/p01.tex", 3) == "section"
    write_text_atomic(hb / "parts/p01.tex", host)


def selftest_round7(temp: Path) -> None:
    """Fixtures for repair round 7: scope names shared across groups, braced hook labels,
    anchors in definition bodies, hidden numeric scopes, TeX-escaped DOIs."""
    root = temp / "round7"
    hb = root / "handbook"
    files = {
        "main.tex": "\\input{parts/p01}\n",
        "parts/p01.tex": "\\chapter{One}\n\\input{parts/p01/a}\n\\input{parts/p01/c}\n",
        "parts/p01/a.tex": "\\section{A}\\label{sec:p01-a}\n",
        "parts/p01/b.tex": "\\section{B}\\label{sec:p01-b}\n",
        "parts/p01/c.tex": "\\section{C}\\label{sec:p01-c}\n",
        "registry/symbol-scopes.json": json_text({"schema_version": 1, "scopes": {}}),
        "registry/symbols.csv": ",".join(FIELDS) + "\n",
        "bib/handbook.bib": "",
        "registry/symbols-intake-g.csv": (",".join(FIELDS) + "\n"
                                          "\\(q\\),q,query,local region,n/a,sec:p01-a,\n"),
        "registry/symbols-intake-h.csv": (",".join(FIELDS) + "\n"
                                          "\\(r\\),r,rule,local region,n/a,sec:p01-c,\n"),
    }
    for rel, text in files.items():
        write_text_atomic(hb / rel, text)

    def run(func, **kwargs) -> tuple[int, dict]:
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            code = func(argparse.Namespace(**kwargs))
        return code, json.loads(stream.getvalue())

    routed = "routed-awaiting-canonical-merge"
    manifest = root / "manifest.json"
    decisions = root / "decisions.json"
    write_json_atomic(manifest, {"groups": [
        {"stem": stem, "integration_status": routed, "bodies": [body], "annexes": [],
         "symbol_intakes": [f"registry/symbols-intake-{stem}.csv"], "bibliography_intakes": []}
        for stem, body in (("g", "parts/p01/a"), ("h", "parts/p01/c"))]})
    adopt_args = {"manifest": str(manifest), "decisions": str(decisions),
                  "return_json": None, "virtual_route": False}
    region_g = {"heading_of": "sec:p01-a", "level": "section"}
    region_h = {"heading_of": "sec:p01-c", "level": "section"}
    old_root, old_base = ROOT, BASE
    try:
        globals()["ROOT"] = root
        globals()["BASE"] = hb
        # Two groups using one new scope name are not merged silently.
        write_json_atomic(decisions, {})
        scopes_before = read_text(hb / "registry/symbol-scopes.json")
        code, out = run(command_adopt, apply=True, **adopt_args)
        shared = [d for d in out["decisions-needed"]
                  if d["kind"] == "scope-name-shared-across-groups"]
        assert code == 1 and shared and shared[0]["groups"] == {"g": [region_g], "h": [region_h]}, out
        assert read_text(hb / "registry/symbol-scopes.json") == scopes_before
        # An extend_scopes decision naming only one group's region does not cover it.
        write_json_atomic(decisions, {"extend_scopes": [{"scope": "local region",
                                                         "regions": [region_g]}]})
        code, out = run(command_adopt, apply=False, **adopt_args)
        assert code == 1 and any(d["kind"] == "scope-name-shared-across-groups"
                                 for d in out["decisions-needed"]), out
        # A decision listing every region covers the merge.
        write_json_atomic(decisions, {"extend_scopes": [{"scope": "local region",
                                                         "regions": [region_g, region_h]}]})
        code, out = run(command_adopt, apply=True, **adopt_args)
        assert code == 0 and out["ok"], out
        scopes = load_json(hb / "registry/symbol-scopes.json")["scopes"]
        assert scopes["local region"]["regions"] == [region_g, region_h], scopes
    finally:
        globals()["ROOT"] = old_root
        globals()["BASE"] = old_base

    # A braced optional label (or hook name) pairs with its unbraced spelling.
    for add, remove in ((r"\AddToHook{env/x/begin}[{n}]{\relax}", r"\RemoveFromHook{env/x/begin}[n]"),
                        (r"\AddToHook{{env/x/begin}}[n]{\relax}", r"\RemoveFromHook{env/x/begin}[ {n} ]"),
                        (r"\AddToHook{env/x/begin}[{a]b}]{\relax}", r"\RemoveFromHook{env/x/begin}[{a]b}]")):
        lines = [add, r"\input{a}", remove, r"\input{b}"]
        assert insertion_inside_hook(lines, 1) and insertion_inside_hook(lines, 2), lines
        assert not insertion_inside_hook(lines, 3), lines

    # An anchor \input inside a macro definition body is refused.
    write_text_atomic(hb / "parts/p01.tex",
                      "\\newcommand\\foo{\\input{parts/p01/a}}\n\\chapter{One}\n\\foo\n"
                      "\\input{parts/p01/c}\n")
    result = simulate_route(hb, [{"host": "parts/p01", "after": "parts/p01/a",
                                  "input": "parts/p01/b"}], apply=False)
    assert not result["ok"] and "definition body" in result["errors"][0]["error"], result
    write_text_atomic(hb / "parts/p01.tex", files["parts/p01.tex"])
    assert simulate_route(hb, [{"host": "parts/p01", "after": "parts/p01/a",
                                "input": "parts/p01/b"}], apply=False)["ok"]

    # Hidden or spelled-out numeric scopes.
    for scope in ("P\u200b1.1", "P\u20601.1 x", "\ufeffP1.1", "Part 6.3", "Parts 6.3 x",
                  "\u04201.1", "P\u03011.1", "P1\u00ad.1"):
        assert numeric_scope_forbidden(scope), scope
    for scope in ("Parts 5\u201319 from first-incompleteness", "Part one", "P13 consequence operations"):
        assert not numeric_scope_forbidden(scope), scope

    # A TeX-escaped DOI is the same work as the plain one.
    canonical = "@incollection{Plain,\n  title={T},\n  author={A},\n  year={2004},\n" \
                "  doi={10.1007/978-3-662-07675-0_7}\n}\n"
    for field in ("doi={10.1007/978-3-662-07675-0\\_7}",
                  "doi={{10.1007/978-3-662-07675-0\\_7}}",
                  "note={https://doi.org/10.1007/978-3-662-07675-0\\_7}"):
        write_text_atomic(hb / "bib/intake-s.bib",
                          "@incollection{Escaped,\n  title={U},\n  author={B},\n  year={2005},\n  "
                          + field + "\n}\n")
        append, needed, _comparisons = analyze_bibliography(
            [{"stem": "s", "bibliography_intakes": ["bib/intake-s.bib"]}], {}, canonical, hb)
        assert append == [] and [item["kind"] for item in needed] == ["bib-duplicate-work"], field


def selftest_round8(temp: Path) -> None:
    """Fixtures for repair round 8: path spellings in route checks, hook removes in
    definition bodies, @comment blocks, commented annex items, check line tokens."""
    hb = temp / "round8" / "handbook"
    (hb / "parts/p01").mkdir(parents=True)
    write_text_atomic(hb / "main.tex", "\\input{parts/p01}\n")
    for name in ("a", "b", "c", "n"):
        write_text_atomic(hb / f"parts/p01/{name}.tex", f"\\section{{{name}}}\n")
    place = {"host": "parts/p01", "after": "parts/p01/a", "input": "parts/p01/b"}

    # Another file already routes b under a different spelling: b would be reached twice.
    for spelling in ("./parts/p01/b", "parts/p01/../p01/b", "./parts/p01/b.tex"):
        write_text_atomic(hb / "parts/p01.tex",
                          "\\chapter{One}\n\\input{parts/p01/a}\n\\input{parts/p01/c}\n")
        write_text_atomic(hb / "parts/p01/c.tex", "\\section{c}\n\\input{" + spelling + "}\n")
        assert static_input_counts(hb)[0].get("parts/p01/b.tex") == 1, spelling
        result = simulate_route(hb, [place], apply=False)
        assert not result["ok"] and "reaches input 2 times" in result["errors"][0]["error"], result
    write_text_atomic(hb / "parts/p01/c.tex", "\\section{c}\n")
    # The host already holds b under another spelling: a no-op, not a second copy.
    for spelling in ("./parts/p01/b", "parts/p01/../p01/b.tex"):
        write_text_atomic(hb / "parts/p01.tex",
                          "\\chapter{One}\n\\input{parts/p01/a}\n\\input{" + spelling + "}\n")
        result = simulate_route(hb, [place], apply=False)
        assert result["ok"] and result["actions"][0]["action"] == "noop-already-present", result
        found, errors = located_route_inputs(
            hb, {"stem": "s", "bodies": ["parts/p01/b"]},
            {"parts/p01.tex": read_text(hb / "parts/p01.tex").split("\n")})
        assert found == [("parts/p01.tex", "parts/p01/b.tex")] and errors == [], (found, errors)
    # The anchor counted under every spelling.
    write_text_atomic(hb / "parts/p01.tex",
                      "\\chapter{One}\n\\input{parts/p01/a}\n\\input{./parts/p01/a.tex}\n")
    result = simulate_route(hb, [place], apply=False)
    assert not result["ok"] and result["errors"][0]["error"] == "anchor occurs 2 times", result
    write_text_atomic(hb / "parts/p01.tex", "\\chapter{One}\n\\input{parts/p01/../p01/a}\n")
    result = simulate_route(hb, [place], apply=False)
    assert result["ok"] and result["actions"][0]["action"] == "insert", result

    # A \RemoveFromHook in a definition body runs where the macro is used: the bracket
    # stays open to the end of the host.
    add = r"\AddToHook{env/x/begin}[n]{\relax}"
    for define in (r"\newcommand\stop{\RemoveFromHook{env/x/begin}[n]}",
                   r"\def\stop{\RemoveFromHook{env/x/begin}[*]}"):
        for lines in ([define, add, r"\input{parts/p01/a}", r"\stop", r"\input{parts/p01/c}"],
                      [add, define, r"\input{parts/p01/a}", r"\stop", r"\input{parts/p01/c}"]):
            assert insertion_inside_hook(lines, 3) and insertion_inside_hook(lines, 5), lines
            write_text_atomic(hb / "parts/p01.tex", "\n".join(lines) + "\n")
            result = simulate_route(hb, [{"host": "parts/p01", "after": "parts/p01/a",
                                          "input": "parts/p01/n"}], apply=False)
            assert not result["ok"] and "AddToHook" in result["errors"][0]["error"], result
    # A live remove after a deferred one still closes the bracket.
    assert not insertion_inside_hook([r"\newcommand\stop{\RemoveFromHook{env/x/begin}[n]}", add,
                                      r"\input{a}", r"\RemoveFromHook{env/x/begin}[n]",
                                      r"\input{c}"], 4)

    # A record inside an @comment block is not live; it is reported, never appended.
    (hb / "bib").mkdir()
    hidden = ("@comment{ @article{Hidden,\n  title={H},\n  author={A},\n  year={2020}\n} }\n"
              "@Comment(note (with) parens @book{Hidden2, title={X}})\n"
              "@book{Live,\n  title={L},\n  author={B},\n  year={2021}\n}\n")
    assert [r["key"] for r in bib_records(hidden)] == ["Live"] and unparsed_bib_entries(hidden) == []
    write_text_atomic(hb / "bib/intake-s.bib", hidden)
    append, needed, comparisons = analyze_bibliography(
        [{"stem": "s", "bibliography_intakes": ["bib/intake-s.bib"]}], {}, "", hb)
    assert [r["key"] for r in append] == ["Live"] and needed == [], needed
    assert [c["entry"][:15] for c in comparisons] == ["@article{Hidden", "@book{Hidden2, "], comparisons
    try:
        bib_records("@comment{ open\n@book{K,\n}\n")
        assert False, "an unterminated @comment must be refused"
    except Refusal:
        pass

    # declared_proof_pairs counts only live annexitem environments.
    (hb / "annex/p01").mkdir(parents=True)
    write_text_atomic(hb / "annex/p01/a.tex",
                      "% \\begin{annexitem}{annex:p01.old}{sec:p01-a}\n"
                      "\\begin{annexitem}{annex:p01.a}{sec:p01-a}\nX\n\\end{annexitem}\n")
    assert count_annexitems(hb / "annex/p01/a.tex") == 1
    old_base = BASE
    try:
        globals()["BASE"] = hb
        group = group_from_return(temp / "r.json", {"stem": "r", "part": "P1",
                                                    "annexes": ["annex/p01/a"],
                                                    "declared_proof_pairs": 1})
        assert group["declared_proof_pairs"] == 1, group
    finally:
        globals()["BASE"] = old_base

    # check-delta: 'line N' and 'lines N/M' tokens do not make a moved finding new.
    before = normalize_check_output("  - symbols-csv: line 6053: bad\n"
                                    "  - glyph-collision: lines 79/6052: clash\n")
    after = normalize_check_output("  - symbols-csv: line 6060: bad\n"
                                   "  - glyph-collision: lines 79/6059: clash\n")
    assert before == after == ["  - glyph-collision: lines: clash", "  - symbols-csv: line: bad"], before


def selftest_round9(temp: Path) -> None:
    """Fixtures for repair round 9: author+title+year duplicates within one run, file
    ownership across groups, malformed manifests and decisions."""
    root = temp / "round9"
    hb = root / "handbook"
    same = "author={Zed},\n  title={Same Work},\n  year={1999}\n}\n"
    files = {
        "main.tex": "\\input{parts/p01}\n",
        "parts/p01.tex": "\\chapter{One}\n\\input{parts/p01/a}\n\\input{parts/p01/c}\n",
        "parts/p01/a.tex": "\\section{A}\\label{sec:p01-a}\nSee \\cite{GAlias,HAlias}.\n",
        "parts/p01/c.tex": "\\section{C}\\label{sec:p01-c}\n",
        "registry/symbol-scopes.json": json_text({"schema_version": 1, "scopes": {}}),
        "registry/symbols.csv": ",".join(FIELDS) + "\n",
        "bib/handbook.bib": ("@book{CanonG,\n  author={Gee},\n  title={G},\n  year={2000}\n}\n\n"
                             "@book{CanonH,\n  author={Aitch},\n  title={H},\n  year={2001}\n}\n"),
        "bib/intake-g.bib": "@book{KeyG,\n  " + same,
        "bib/intake-h.bib": "@book{KeyH,\n  " + same,
        "bib/intake-two.bib": "@book{NewA,\n  " + same + "\n@book{NewB,\n  " + same,
        "bib/intake-ga.bib": "@book{GAlias,\n  author={Gee},\n  title={G},\n  year={2000}\n}\n",
        "bib/intake-ha.bib": "@book{HAlias,\n  author={Aitch},\n  title={H},\n  year={2001}\n}\n",
    }
    for rel, text in files.items():
        write_text_atomic(hb / rel, text)

    # The same work under two keys, no identifiers: across groups and inside one intake.
    groups = [{"stem": "g", "bibliography_intakes": ["bib/intake-g.bib"]},
              {"stem": "h", "bibliography_intakes": ["bib/intake-h.bib"]}]
    for case in (groups, [{"stem": "t", "bibliography_intakes": ["bib/intake-two.bib"]}]):
        append, needed, _comparisons = analyze_bibliography(case, {}, files["bib/handbook.bib"], hb)
        assert len(append) == 1 and [d["kind"] for d in needed] == ["bib-duplicate-work"], needed
        assert needed[0]["candidates"][0]["key"] == append[0]["key"], needed

    def run(argv: list[str]) -> tuple[int, dict]:
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            code = main(argv)
        return code, json.loads(stream.getvalue())

    routed = "routed-awaiting-canonical-merge"
    manifest = root / "manifest.json"
    decisions = root / "decisions.json"

    def group(stem: str, bodies: list[str], bib: str) -> dict:
        return {"stem": stem, "integration_status": routed, "bodies": bodies, "annexes": [],
                "symbol_intakes": [], "bibliography_intakes": [bib]}

    aliases = {"citation_aliases": {"GAlias": "CanonG", "HAlias": "CanonH"}}
    adopt = ["adopt", "--manifest", str(manifest), "--decisions", str(decisions)]
    old_root, old_base = ROOT, BASE
    try:
        globals()["ROOT"] = root
        globals()["BASE"] = hb
        # Two groups claiming one file, and a group claiming the part host, need a decision.
        write_json_atomic(manifest, {"groups": [
            group("g", ["parts/p01/a", "parts/p01"], "bib/intake-ga.bib"),
            group("h", ["parts/p01/a"], "bib/intake-ha.bib")]})
        write_json_atomic(decisions, aliases)
        before = read_text(hb / "parts/p01/a.tex")
        code, out = run(adopt + ["--apply"])
        kinds = sorted(d["kind"] for d in out["decisions-needed"])
        assert code == 1 and kinds == ["owned-file-is-shared-route-host",
                                       "owned-file-shared-across-groups"], out
        assert read_text(hb / "parts/p01/a.tex") == before
        # A decided share gets both groups' rewrites; neither is lost.
        write_json_atomic(manifest, {"groups": [group("g", ["parts/p01/a"], "bib/intake-ga.bib"),
                                                group("h", ["parts/p01/a"], "bib/intake-ha.bib")]})
        write_json_atomic(decisions, dict(aliases, allow_shared_owned_files=["parts/p01/a.tex"]))
        code, out = run(adopt + ["--apply"])
        assert code == 0 and out["ok"], out
        assert "\\cite{CanonG,CanonH}" in read_text(hb / "parts/p01/a.tex")

        # Malformed manifests and decisions are refused cleanly (JSON, exit 1).
        malformed = ({"groups": "g"},
                     {"groups": [dict(group("g", [], "bib/intake-g.bib"), bodies="parts/p01/a")]},
                     {"groups": [dict(group("g", [], "bib/intake-g.bib"), annexes=[1])]},
                     {"groups": ["g"]},
                     {"groups": [dict(group("g", [], "bib/intake-g.bib"),
                                      placement={"host": 1, "after": "a", "input": "b"})]},
                     {"groups": [dict(group("g", [], "bib/intake-g.bib"), placement="parts/p01")]},
                     {"placements": [{"host": "parts/p01", "input": "parts/p01/c"}], "groups": []})
        write_json_atomic(decisions, {})
        for data in malformed:
            write_json_atomic(manifest, data)
            for argv in (["route", "--manifest", str(manifest)], adopt,
                         ["unroute", "--manifest", str(manifest), "--stems", "g"]):
                code, out = run(argv)
                assert code == 1 and not out["ok"] and "malformed manifest" in out["error"], (argv, out)
        write_json_atomic(manifest, {"groups": []})
        for data in ({"extend_scopes": [1]}, {"overrides": {"scope": "x"}},
                     {"extend_scopes": [{"scope": "x", "regions": "sec:p01-a"}]},
                     {"bib_keep_canonical": [{"k": 1}]}, {"allow_shared_owned_files": "a"}):
            write_json_atomic(decisions, data)
            code, out = run(adopt)
            assert code == 1 and "malformed decisions" in out["error"], (data, out)
        write_json_atomic(decisions, {"row_edits": [{"group": "g", "line": 2,
                                                     "fields": {"role": 3}}]})
        code, out = run(adopt)
        assert code == 1 and out["errors"][0]["kind"] == "invalid-selector", out
    finally:
        globals()["ROOT"] = old_root
        globals()["BASE"] = old_base


def selftest_round10(temp: Path) -> None:
    """Fixtures for repair round 10 (verifier defects M1-M6, m1-m8)."""
    def refused(raw: str) -> bool:
        row = dict.fromkeys(FIELDS, "")
        row.update(glyph=raw, role="r", scope="s", precedence="n/a", first_use="sec:x")
        try:
            actual_row(row, {"stem": "g"}, "registry/x.csv", 2)
        except IntakeRowError:
            return True
        return False

    # M1 $$ and dollar-wrapped families; M3 trailing backslash and ^^; m2; m8 empty bodies.
    for raw in ("$$x$$", r"$\alpha$, $\beta$", "$x", "x\\", "\\", "x\\\\\\", "^^", "x^^41",
                "x^", "x_", "{x^}", r"\left(x", r"x\right)", "a\n\nb", r"\text{$x$}",
                "$$", r"\(\)", "", " ", r"x\\y"):
        assert refused(raw), raw
    for raw in ("$", r"\$", "_", "a_b", r"\left(x\right)", r"\begin{array}{c}x\\y\end{array}",
                r"\text{a b}", "x_{}"):
        assert not refused(raw), raw
    # M2: a blank macro takes the TeX spelling, never a raw % # &.
    row = dict.fromkeys(FIELDS, "")
    row.update(glyph="#,&", role="r", scope="s", precedence="n/a", first_use="sec:x")
    out, _inactive = actual_row(row, {"stem": "g"}, "registry/x.csv", 2)
    assert [(m["glyph"], m["macro"]) for m in out["_members"]] == [(r"\(\#\)", r"\#"),
                                                                  (r"\(\&\)", r"\&")], out
    row.update(glyph="%")
    out, _inactive = actual_row(row, {"stem": "g"}, "registry/x.csv", 2)
    assert (out["glyph"], out["macro"]) == (r"\(\%\)", r"\%"), out
    assert nonascii_math_characters("≤") == ["≤"] and nonascii_math_characters(r"\text{≤}") == []

    # m7: BibTeX brace/quote rules (a backslash escapes nothing).
    records = bib_records("@book{A,\n  title={a\\}b},\n  year={2000}\n}\n")
    assert records[0]["raw"] == "@book{A,\n  title={a\\}b}", records
    assert bib_fields({"raw": '@book{Q,\n  title="G\\"odel",\n  year={1}\n}'})["title"] == "G\\"
    assert bib_fields({"raw": '@book{Q,\n  title="G{\\"o}del",\n  year={1}\n}'})["title"] == 'G{\\"o}del'
    try:
        bib_records("@book{B,\n  title={x\\{y},\n  year={2000}\n}\n")
        assert False, "\\{ opens a brace in BibTeX; the record is unbalanced"
    except Refusal:
        pass

    root = temp / "round10"
    hb = root / "handbook"
    routed = ADOPT_ROUTED_STATUS

    def make(files: dict) -> None:
        if root.exists():
            shutil.rmtree(root)
        base_files = {
            "main.tex": "\\input{parts/p01}\n\\input{annex/p01}\n",
            "annex/p01.tex": "",
            "registry/symbol-scopes.json": json_text({"schema_version": 1, "scopes": {}}),
            "registry/symbols.csv": ",".join(FIELDS) + "\n",
            "bib/handbook.bib": "@book{Canon,\n  author={C},\n  title={Canon},\n  year={2000}\n}\n",
        }
        for rel, text in {**base_files, **files}.items():
            write_text_atomic(hb / rel, text)

    def run(argv: list[str]) -> tuple[int, dict]:
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            code = main(argv)
        return code, json.loads(stream.getvalue())

    def adopt(groups: list[dict], decisions: dict, apply: bool = False) -> tuple[int, dict]:
        write_json_atomic(root / "manifest.json", {"groups": groups})
        write_json_atomic(root / "decisions.json", decisions)
        return run(["adopt", "--manifest", str(root / "manifest.json"), "--decisions",
                    str(root / "decisions.json")] + (["--apply"] if apply else []))

    def group(stem: str, bodies=(), annexes=(), intakes=(), bibs=()) -> dict:
        return {"stem": stem, "integration_status": routed, "bodies": list(bodies),
                "annexes": list(annexes), "symbol_intakes": list(intakes),
                "bibliography_intakes": list(bibs)}

    def kinds(out: dict) -> list[str]:
        return sorted(d["kind"] for d in out["decisions-needed"])

    header = ",".join(FIELDS) + "\n"
    one_body = {"parts/p01.tex": "\\chapter{One}\n\\input{parts/p01/a}\n",
                "parts/p01/a.tex": "\\section{A}\\label{sec:p01-a}\nText.\n"}
    old_root, old_base = ROOT, BASE
    try:
        globals()["ROOT"] = root
        globals()["BASE"] = hb

        # m2 non-ASCII math glyph: decisions-needed; a row_edits glyph fix covers it, and
        # the edited glyph is normalized like an intake glyph (m1).
        make({**one_body, "registry/symbols-intake-g.csv": header + "≤,,le role,g region,n/a,sec:p01-a,\n"})
        grp = [group("g", ["parts/p01/a"], intakes=["registry/symbols-intake-g.csv"])]
        code, out = adopt(grp, {})
        assert code == 1 and kinds(out) == ["glyph-non-ascii-math"], out
        code, out = adopt(grp, {"row_edits": [{"group": "g", "line": 2, "set": {"glyph": "\\leq"}}]},
                          apply=True)
        assert code == 0 and out["ok"], out
        # The macro filled from the old glyph is re-filled from the edited one (round 12).
        assert "\\(\\leq\\),\\leq,le role," in read_text(hb / "registry/symbols.csv")
        code, out = adopt(grp, {"row_edits": [{"group": "g", "line": 2, "set": {"glyph": "50%$x$"}}]})
        assert code == 1 and out["errors"][0]["kind"] == "row-edit-glyph", out
        code, out = adopt([], {"canonical_row_edits": [{"line": 2, "set": {"glyph": "$z"}}]})
        assert code == 1 and out["errors"][0]["kind"] == "canonical-row-edit-glyph", out
        code, out = adopt([], {"canonical_row_edits": [{"line": 2, "set": {"glyph": "%"}}]}, apply=True)
        assert code == 0 and "\n\\(\\%\\),\\leq,le role," in read_text(hb / "registry/symbols.csv"), out

        # M4: an annex first_use whose owner result lives in another group's body binds only
        # the item; the owner needs an extend_scopes decision.
        make({"parts/p01.tex": "\\chapter{One}\n\\input{parts/p01/b}\n",
              "annex/p01.tex": "\\input{annex/p01/a}\n",
              "parts/p01/b.tex": ("\\section{B}\\label{sec:p01-b}\n\\begin{hbtheorem}{thm:p01-b}"
                                  "{proved=annex:p01.a}{B}\nX.\n\\end{hbtheorem}\n"),
              "annex/p01/a.tex": "\\begin{annexitem}{annex:p01.a}{thm:p01-b}{A}\nP.\n\\end{annexitem}\n",
              "registry/symbols-intake-a.csv": header + "\\(\\alpha\\),\\alpha,a,a region,n/a,annex:p01.a,\n"})
        grp = [group("a", annexes=["annex/p01/a"], intakes=["registry/symbols-intake-a.csv"])]
        code, out = adopt(grp, {})
        assert code == 1 and kinds(out) == ["binding-foreign-owner"], out
        code, out = adopt(grp, {"extend_scopes": [{"scope": "a region",
                                                   "regions": [{"anchor": "thm:p01-b"}]}]}, apply=True)
        assert code == 0, out
        assert load_json(hb / "registry/symbol-scopes.json")["scopes"]["a region"]["regions"] == [
            {"anchor": "annex:p01.a"}, {"anchor": "thm:p01-b"}]
        index = registry.ReaderIndex(hb)
        selectors, foreign = local_regions_for_first_use(
            index, "annex:p01.a", {"bodies": ["parts/p01/b"], "annexes": ["annex/p01/a"]})
        assert selectors == [{"anchor": "annex:p01.a"}, {"anchor": "thm:p01-b"}] and not foreign

        # m3: a section region running on over a following file the group does not own.
        spill = {"parts/p01.tex": "\\chapter{One}\n\\input{parts/p01/a}\n\\input{parts/p01/b}\n",
                 "parts/p01/a.tex": ("\\section{A}\\label{sec:p01-a}\n\\begin{hbdefinition}"
                                     "{def:p01-a}{A}\nX.\n\\end{hbdefinition}\n"),
                 "parts/p01/b.tex": "\\subsection{B}\\label{sec:p01-b}\n",
                 "registry/symbols-intake-a.csv": header + "\\(\\beta\\),\\beta,b,a region,n/a,def:p01-a,\n"}
        make(spill)
        grp = [group("a", ["parts/p01/a"], intakes=["registry/symbols-intake-a.csv"])]
        code, out = adopt(grp, {})
        assert code == 1 and kinds(out) == ["binding-heading-spill"], out
        assert out["decisions-needed"][0]["paths"] == ["parts/p01/b.tex"], out
        code, out = adopt(grp, {"extend_scopes": [{"scope": "a region", "regions": [
            {"heading_of": "sec:p01-a", "level": "section"}]}]})
        assert code == 0, out
        make(dict(spill, **{"parts/p01/b.tex": "\\section{B}\\label{sec:p01-b}\n"}))
        code, out = adopt(grp, {})
        assert code == 0, out  # b opens with its own section: nothing runs on
        # A wrapper file whose first heading closes the region adds nothing to it either; a
        # following file of prose only does run on.
        make(dict(spill, **{"parts/p01/b.tex": ("\\begin{inheritedrestorationscope}{SRC-1}\n"
                                                "\\input{parts/p01/c}\n"
                                                "\\end{inheritedrestorationscope}\n"),
                            "parts/p01/c.tex": "\\section{C}\\label{sec:p01-c}\n"}))
        code, out = adopt(grp, {})
        assert code == 0, out
        make(dict(spill, **{"parts/p01/b.tex": "Prose with \\(x\\) only.\n"}))
        code, out = adopt(grp, {})
        assert code == 1 and kinds(out) == ["binding-heading-spill"], out

        # m4: an annex item whose owner label is declared twice is reported, not dropped.
        make({"parts/p01.tex": "\\chapter{One}\n\\input{parts/p01/a}\n",
              "annex/p01.tex": "\\input{annex/p01/a}\n",
              "parts/p01/a.tex": ("\\section{A}\\label{sec:p01-a}\n"
                                  "\\begin{hbtheorem}{thm:p01-t}{x}{T}\nX.\n\\end{hbtheorem}\n"
                                  "\\begin{hbtheorem}{thm:p01-t}{x}{Dup}\nY.\n\\end{hbtheorem}\n"),
              "annex/p01/a.tex": "\\begin{annexitem}{annex:p01.t}{thm:p01-t}{T}\nP.\n\\end{annexitem}\n",
              "registry/symbols-intake-a.csv": header + "\\(\\gamma\\),\\gamma,g,a region,n/a,sec:p01-a,\n"})
        code, out = adopt([group("a", ["parts/p01/a"], ["annex/p01/a"],
                                 ["registry/symbols-intake-a.csv"])], {})
        assert code == 1 and kinds(out) == ["binding-annexitem-owner-ambiguous"], out

        # M5 annex placement with no heading on either side; m5 held groups are never
        # routed; m6 a refused status edit leaves every host unwritten.
        make({**one_body, "parts/p01/s.tex": "\\section{S}\\label{sec:p01-s}\n",
              "annex/p01.tex": "\\input{annex/p01/a}\n",
              "annex/p01/a.tex": "\\begin{annexitem}{annex:p01.a}{sec:p01-a}{A}\nP.\n\\end{annexitem}\n",
              "annex/p01/n.tex": "\\begin{annexitem}{annex:p01.n}{sec:p01-a}{N}\nP.\n\\end{annexitem}\n"})
        manifest = root / "manifest.json"
        route = ["route", "--manifest", str(manifest), "--apply"]
        host = read_text(hb / "parts/p01.tex")
        body_place = {"host": "parts/p01", "after": "parts/p01/a", "input": "parts/p01/s"}
        write_json_atomic(manifest, {"groups": [{"stem": "s", "integration_status": "saved-off-route",
                                                 "bodies": ["parts/p01/s"], "placement": body_place}]})
        code, out = run(route)
        assert code == 0 and out["skipped_held_placements"] and "status_set_routed" not in out, out
        assert read_text(hb / "parts/p01.tex") == host
        assert load_json(manifest)["groups"][0]["integration_status"] == "saved-off-route"
        write_json_atomic(manifest, {"groups": [{"stem": "s", "bodies": ["parts/p01/s"],
                                                 "placement": body_place}]})
        code, out = run(route)
        # A placed group without a status is refused before any write (round 12: unknown status).
        assert code == 1 and "integration_status" in json.dumps(out["errors"]), out
        assert read_text(hb / "parts/p01.tex") == host
        write_json_atomic(manifest, {"groups": [{"stem": "n", "integration_status": "returned",
                                                 "annexes": ["annex/p01/n"], "placement": {
                                                     "host": "annex/p01", "after": "annex/p01/a",
                                                     "input": "annex/p01/n"}}]})
        code, out = run(route)
        assert code == 0 and out["status_set_routed"] == ["n"], out
        assert "\\input{annex/p01/n}" in read_text(hb / "annex/p01.tex")

        # M6: collect -> route -> adopt on an author return in the wave shape (a trimmed copy
        # of edition-2026-p01-languages-logical-systems-and-levels-of-w02-p01-002-return.json):
        # placement {body, annex} with after_input, notes, files_written; no part and no
        # body or annex in files_written, so both come from the packet.
        stem = "p01-languages-logical-systems-and-levels-of-w02-p01-002"
        body, annex = f"parts/p01/languages-logical-systems-and-levels-of-w02-p01-002", \
            f"annex/p01/languages-logical-systems-and-levels-of-w02-p01-002"
        make({"main.tex": "\\input{parts/p01}\n\\input{annex/p01-route}\n",
              "parts/p01.tex": ("\\chapter{One}\n\\input{parts/p01/boolean-prime-ideal-and-ultrafilters}\n"
                                "\\input{restoration/scope-SRC-00853-00906}\n"),
              "parts/p01/boolean-prime-ideal-and-ultrafilters.tex": "\\section{BPI}\\label{sec:p01-bpi}\n",
              "restoration/scope-SRC-00853-00906.tex": "\\section{Old}\\label{sec:p01-old}\n",
              "annex/p01-route.tex": "\\input{annex/p01/boolean-prime-ideal-and-ultrafilters}\n",
              "annex/p01/boolean-prime-ideal-and-ultrafilters.tex": "",
              body + ".tex": ("%% toc: P1 1 1.2\n\\section{Valuation systems}"
                              "\\label{sec:p01-w02-p01-002-valuation-systems}\n"
                              "\\cite[1--78]{RyanSadler1992}\n"),
              annex + ".tex": "",
              f"bib/intake-{stem}.bib": ("@incollection{RyanSadler1992,\n  author={Ryan, Mark and "
                                         "Sadler, Martin},\n  title={Valuation Systems and "
                                         "Consequence Relations},\n  year={1992}\n}\n"),
              f"registry/symbols-intake-{stem}.csv": (
                  header + "\\(\\models_V\\),,valuation consequence,P1 valuation systems,relation,"
                  "sec:p01-w02-p01-002-valuation-systems,\n")})
        note = f"spec/research/edition-2026-{stem}.md"
        write_text_atomic(root / note, "## Continuation\n")
        packet = {"id": "w02-p01-002", "part": "P1", "label_tag": "p01-w02-p01-002",
                  "owned_files": ["handbook/" + body + ".tex", "handbook/" + annex + ".tex",
                                  f"handbook/bib/intake-{stem}.bib",
                                  f"handbook/registry/symbols-intake-{stem}.csv",
                                  note, f"spec/research/edition-2026-{stem}-return.json"],
                  "insertion": {"body": {"host": "handbook/parts/p01.tex", "after_line": 3,
                                         "after_input": "restoration/scope-SRC-00853-00906"}}}
        write_json_atomic(root / "work/waves/w02/packets/w02-p01-002.json", packet)
        returned = {
            "packet": "w02-p01-002", "label_tag": "p01-w02-p01-002",
            "placement": {
                "body": {"host": "handbook/parts/p01.tex",
                         "after_input": "restoration/scope-SRC-00853-00906", "input": body},
                "annex": {"host": "handbook/annex/p01-route.tex",
                          "after_input": "annex/p01/boolean-prime-ideal-and-ultrafilters",
                          "input": annex},
                "reason": "follows the packet's insertion proposal"},
            "components": [{"component_id": "ED26-SRC-026-001-DOMAIN", "state": "blocked_source",
                            "blocker": "chapter body not held"}],
            "proposed_decisions": [], "unit_compile": "ok", "notes": note,
            "files_written": [f"handbook/bib/intake-{stem}.bib", note,
                              f"spec/research/edition-2026-{stem}-return.json"],
            "files_owned_unchanged_this_session": ["handbook/" + body + ".tex",
                                                   "handbook/" + annex + ".tex"]}
        return_path = root / f"spec/research/edition-2026-{stem}-return.json"
        write_json_atomic(return_path, returned)
        code, out = run(["collect", "--wave", "97", str(return_path), "--apply"])
        assert code == 0, out
        manifest = root / "spec/research/edition-2026-authoring-batch-intake-97.json"
        collected = load_json(manifest)["groups"][0]
        assert (collected["stem"], collected["part"], collected["label_tag"], collected["note"]) == (
            stem, "P1", "p01-w02-p01-002", note), collected
        assert (collected["bodies"], collected["annexes"]) == ([body + ".tex"], [annex + ".tex"])
        assert collected["bibliography_intakes"] == [f"bib/intake-{stem}.bib"]
        assert collected["symbol_intakes"] == [f"registry/symbols-intake-{stem}.csv"]
        assert collected["placement"]["body"]["after"] == "restoration/scope-SRC-00853-00906"
        code, out = run(["route", "--manifest", str(manifest), "--apply"])
        assert code == 0 and out["status_set_routed"] == [stem], out
        assert read_text(hb / "parts/p01.tex").split("\n")[3] == "\\input{" + body + "}"
        assert "\\input{" + annex + "}" in read_text(hb / "annex/p01-route.tex")
        write_json_atomic(root / "decisions.json", {})
        code, out = run(["adopt", "--manifest", str(manifest), "--decisions",
                         str(root / "decisions.json"), "--apply"])
        assert code == 0 and out["new_bib_records"] == ["RyanSadler1992"], out
        assert "\\(\\models_V\\),\\models_V," in read_text(hb / "registry/symbols.csv")
        assert load_json(manifest)["groups"][0]["integration_status"] == "merged"

        # The same return without its packet: files_written lacks the routed body, so that
        # placement input is not owned; with no owned file at all, a placement is refused.
        (root / "work/waves/w02/packets/w02-p01-002.json").unlink()
        annex_only = returned["files_written"] + ["handbook/" + annex + ".tex"]
        for data, message in ((dict(returned, part="P1", files_written=annex_only),
                               "not owned by the group"),
                              (dict(returned, part="P1"), "owns no body or annex")):
            write_json_atomic(return_path, data)
            code, out = run(["collect", "--wave", "96", str(return_path)])
            assert code == 1 and message in out["error"], out
    finally:
        globals()["ROOT"] = old_root
        globals()["BASE"] = old_base


def selftest_round11(temp: Path) -> None:
    """Fixtures for repair round 11: bib grammar and biber gate, macro checks, glyph
    refusals and the compile gate, shared-anchor route order, canonical non-ASCII
    glyph edits, packet-owned collect, partial routes."""
    # Bib grammar: the three records biber rejects although braces balance BibTeX's way.
    def record(text: str) -> str:
        return bib_records(text)[0]["raw"]

    assert bib_record_syntax_error(record('@book{Q1, author={Aa}, title="Schr\\"odinger", year={2001}}\n'))
    assert bib_record_syntax_error(record("@book{A4, author={Dd}, title={Has \\} escaped brace}, year={2004}}\n"))
    assert bib_record_syntax_error(record("@book{K1, author={A} title={T}, year={2001}}\n"))
    assert bib_record_syntax_error(record('@book{K1, author={A}, title="a } b", year={2001}}\n'))
    for good in ('@book{G, author={A} # " and " # {B}, title="T{\\"o}", year=2001, month=jan,}\n',
                 "@book{G,\n  title={x % y},\n  url={a%20b}\n}\n"):
        assert bib_record_syntax_error(record(good)) is None, good

    # Macros: what would break \texttt{\detokenize{...}}.
    for bad in ("50%", "{a", "a}", "\\", "x\\\\\\", "^^41", "a\n\nb"):
        assert macro_problem(bad), bad
    for good in (r"\alpha", r"a\%b", r"\{", r"x\\", "#", "≤", r"\mathcal{A}"):
        assert macro_problem(good) is None, good
    # Glyphs: double scripts, row breaks, \par, stray specials; nothing is rewritten.
    for bad in ("a_b_c", "a^b^c", "a_{b}_c", "x\\\\", r"x\par y", "a&b", "50%", "x#y",
                r"\begin{pmatrix}a&b\end{pmatrix}&"):
        try:
            math_glyph(bad)
            assert False, "math_glyph accepted " + repr(bad)
        except IntakeRowError:
            pass
    for good in ("{a_b}_c", "a_b^c", r"\sum\limits_a^b", "a^{b^c}", "a_b c_d",
                 r"\begin{pmatrix}a&b\end{pmatrix}", r"\begin{array}{c}x\\y\end{array}"):
        assert math_glyph(good) == good, good
    assert [math_glyph(c) for c in "%#&$_"] == [r"\%", r"\#", r"\&", r"\$", r"\_"]

    root = temp / "round11"
    hb = root / "handbook"
    routed = ADOPT_ROUTED_STATUS
    header = ",".join(FIELDS) + "\n"
    canonical_bib = "@book{Canon,\n  author={C},\n  title={Canon},\n  year={2000}\n}\n"

    def make(files: dict) -> None:
        if root.exists():
            shutil.rmtree(root)
        base_files = {
            "main.tex": "\\input{parts/p01}\n\\input{annex/p01}\n",
            "annex/p01.tex": "",
            "parts/p01.tex": "\\chapter{One}\n\\input{parts/p01/a}\n",
            "parts/p01/a.tex": "\\section{A}\\label{sec:p01-a}\nText.\n",
            "registry/symbol-scopes.json": json_text({"schema_version": 1, "scopes": {}}),
            "registry/symbols.csv": header + "\\(c\\),c,canon role,global,n/a,sec:p01-a,\n",
            "bib/handbook.bib": canonical_bib,
        }
        for rel, text in {**base_files, **files}.items():
            write_text_atomic(hb / rel, text)

    def run(argv: list[str]) -> tuple[int, dict]:
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            code = main(argv)
        return code, json.loads(stream.getvalue())

    def adopt(groups: list[dict], decisions: dict, apply: bool = False) -> tuple[int, dict]:
        write_json_atomic(root / "manifest.json", {"groups": groups})
        write_json_atomic(root / "decisions.json", decisions)
        return run(["adopt", "--manifest", str(root / "manifest.json"), "--decisions",
                    str(root / "decisions.json")] + (["--apply"] if apply else []))

    def group(intakes=(), bibs=()) -> dict:
        return {"stem": "g", "integration_status": routed, "bodies": ["parts/p01/a"],
                "annexes": [], "symbol_intakes": list(intakes), "bibliography_intakes": list(bibs)}

    def intake(glyph: str, macro: str = "") -> dict:
        cell = lambda value: '"' + value.replace('"', '""') + '"'  # noqa: E731
        return {"registry/symbols-intake-g.csv":
                header + cell(glyph) + "," + cell(macro) + ",probe role,g region,n/a,sec:p01-a,\n"}

    def kinds(items: list[dict]) -> list[str]:
        return sorted(item.get("kind", "") for item in items)

    old_root, old_base = ROOT, BASE
    try:
        globals()["ROOT"] = root
        globals()["BASE"] = hb
        # Malformed intake records are errors; nothing is appended.
        for bib in ('@book{Q1, author={Aa}, title="Schr\\"odinger", year={2001}}\n',
                    "@book{A4, author={Dd}, title={Has \\} escaped brace}, year={2004}}\n",
                    "@book{K1, author={A} title={T}, year={2001}}\n"):
            make({"bib/intake-g.bib": bib})
            code, out = adopt([group(bibs=["bib/intake-g.bib"])], {}, apply=True)
            assert code == 1 and kinds(out["errors"]) == ["bib-record-syntax"], out
            assert read_text(hb / "bib/handbook.bib") == canonical_bib
        # A well-formed record biber still warns about is refused by the biber gate.
        make({"bib/intake-g.bib": "@book{M1,\n  author={M},\n  title={Monthly},\n  year={2001},\n"
                                  "  month={September}\n}\n"})
        code, out = adopt([group(bibs=["bib/intake-g.bib"])], {}, apply=True)
        assert code == 1 and kinds(out["errors"]) == ["bib-biber-check"], out
        assert "legacy month" in out["errors"][0]["error"], out
        assert read_text(hb / "bib/handbook.bib") == canonical_bib

        # Macros from intake cells, row_edits and canonical_row_edits are checked.
        make(intake("q", "50%"))
        code, out = adopt([group(["registry/symbols-intake-g.csv"])], {})
        assert code == 1 and kinds(out["errors"]) == ["intake-row-refused"], out
        make(intake("q"))
        grp = [group(["registry/symbols-intake-g.csv"])]
        code, out = adopt(grp, {"row_edits": [{"group": "g", "line": 2, "set": {"macro": "a}"}}]})
        assert code == 1 and kinds(out["errors"]) == ["row-edit-macro"], out
        code, out = adopt(grp, {"canonical_row_edits": [{"line": 2, "set": {"macro": "50%"}}]})
        assert code == 1 and kinds(out["errors"]) == ["canonical-row-edit-macro"], out
        # A canonical glyph edited to a bare non-ASCII math character needs a decision.
        code, out = adopt(grp, {"canonical_row_edits": [{"line": 2, "set": {"glyph": "≤"}}]})
        assert code == 1 and kinds(out["decisions-needed"]) == ["glyph-non-ascii-math"], out

        # Compile gate: command arity is only visible to pdflatex; the row is named.
        for glyph in (r"\hat", r"\frac{a}"):
            make(intake(glyph))
            code, out = adopt([group(["registry/symbols-intake-g.csv"])], {}, apply=True)
            assert code == 1 and out["errors"] and out["errors"][0]["kind"] == "symbol-compile", out
            assert out["errors"][0]["line"] == 2 and out["errors"][0]["error"].startswith("! "), out
            assert "probe role" not in read_text(hb / "registry/symbols.csv")
        make(intake(r"\begin{pmatrix}a&b\end{pmatrix}", "M"))
        code, out = adopt([group(["registry/symbols-intake-g.csv"])], {}, apply=True)
        assert code == 0, out
        assert "\\(\\begin{pmatrix}a&b\\end{pmatrix}\\)" in read_text(hb / "registry/symbols.csv")

        # Shared anchors keep reading order: toc lines first, then manifest order; across
        # runs, a later-routed earlier section goes above the one routed before it.
        def body(name: str, toc: str | None) -> str:
            return (f"%% toc: {toc}\n" if toc else "") + f"\\section{{{name}}}\\label{{sec:p01-{name}}}\n"

        make({"parts/p01.tex": "\\chapter{One}\n\\input{parts/p01/a}\n\\input{parts/p01/z}\n",
              "parts/p01/z.tex": body("z", None),
              "parts/p01/x2.tex": body("xb", "P1 1 1.5"), "parts/p01/x3.tex": body("xc", "P1 1 1.3,1.4"),
              "parts/p01/y1.tex": body("ya", None), "parts/p01/y2.tex": body("yb", None)})

        def placed(stem: str, name: str, status: str = "returned") -> dict:
            return {"stem": stem, "integration_status": status, "bodies": [f"parts/p01/{name}"],
                    "placement": {"body": {"host": "parts/p01", "after": "parts/p01/a",
                                           "input": f"parts/p01/{name}"}}}

        manifest = root / "manifest.json"
        write_json_atomic(manifest, {"groups": [placed("s2", "x2"), placed("s3", "x3")]})
        code, out = run(["route", "--manifest", str(manifest), "--apply"])
        assert code == 0 and out["shared_anchor_order"][0]["inputs"] == [
            "parts/p01/x3.tex", "parts/p01/x2.tex"], out
        write_json_atomic(manifest, {"groups": [placed("s2", "x2", routed), placed("s3", "x3", routed),
                                                placed("t1", "y1", "saved-off-route"),
                                                placed("t2", "y2")]})
        code, out = run(["route", "--manifest", str(manifest), "--apply"])
        assert code == 0, out
        write_json_atomic(manifest, {"groups": [placed("s2", "x2", routed), placed("s3", "x3", routed),
                                                placed("t1", "y1"), placed("t2", "y2", routed)]})
        code, out = run(["route", "--manifest", str(manifest), "--apply"])
        assert code == 0 and out["status_set_routed"] == ["t1"], out
        assert read_text(hb / "parts/p01.tex") == (
            "\\chapter{One}\n\\input{parts/p01/a}\n\\input{parts/p01/x3}\n\\input{parts/p01/x2}\n"
            "\\input{parts/p01/y1}\n\\input{parts/p01/y2}\n\\input{parts/p01/z}\n")
        # Wave files routed there by another manifest are ordered by their toc lines.
        write_text_atomic(hb / "parts/p01/x0.tex", body("xa", "P1 1 1.4"))
        write_json_atomic(manifest, {"groups": [placed("s0", "x0")]})
        code, out = run(["route", "--manifest", str(manifest), "--apply"])
        assert code == 0 and out["shared_anchor_order"][0]["inputs"] == [
            "parts/p01/x3.tex", "parts/p01/x0.tex", "parts/p01/x2.tex"], out

        # A group with an unplaced owned body is reported and keeps its status.
        make({"parts/p01/s.tex": body("s", None), "parts/p01/t.tex": body("t", None)})
        write_json_atomic(manifest, {"groups": [dict(placed("s", "s"),
                                                     bodies=["parts/p01/s", "parts/p01/t"])]})
        code, out = run(["route", "--manifest", str(manifest), "--apply"])
        assert code == 1 and "status_set_routed" not in out, out
        assert out["groups_not_fully_routed"][0]["reach_counts"] == {"parts/p01/t.tex": 0}, out
        assert load_json(manifest)["groups"][0]["integration_status"] == "returned"

        # collect: with a packet, files_written outside its owned_files (an editable host
        # here) is reported, never adopted as a body.
        make({"parts/p01/host.tex": body("host", None), "parts/p01/x-w99-p01-004.tex": body("x", None)})
        write_json_atomic(root / "work/waves/w99/packets/w99-p01-004.json", {
            "id": "w99-p01-004", "part": "P1", "label_tag": "p01-w99-p01-004",
            "owned_files": ["handbook/parts/p01/x-w99-p01-004.tex"],
            "editable_hosts": ["handbook/parts/p01/host.tex"]})
        note = "spec/research/edition-2026-p01-x-w99-p01-004.md"
        write_text_atomic(root / note, "n\n")
        return_path = root / "spec/research/edition-2026-p01-x-w99-p01-004-return.json"
        write_json_atomic(return_path, {
            "packet": "w99-p01-004", "notes": note,
            "placement": {"body": {"host": "handbook/parts/p01.tex", "after_input": "parts/p01/a",
                                   "input": "parts/p01/x-w99-p01-004"}},
            "files_written": ["handbook/parts/p01/host.tex", "handbook/parts/p01/x-w99-p01-004.tex"]})
        code, out = run(["collect", "--wave", "99", "--apply", str(return_path)])
        assert code == 0 and out["files_written_not_adopted"] == [{
            "return": rel_posix(str(return_path)), "file": "handbook/parts/p01/host.tex",
            "reason": "editable host of the packet"}], out
        collected = load_json(root / "spec/research/edition-2026-authoring-batch-intake-99.json")
        assert collected["groups"][0]["bodies"] == ["parts/p01/x-w99-p01-004.tex"], collected
    finally:
        globals()["ROOT"] = old_root
        globals()["BASE"] = old_base


def selftest_round12(temp: Path) -> None:
    """Fixtures for repair round 12: status-aware unroute and route, re-filled macros after
    glyph edits, non-ASCII macros, sequence glyphs, refused rows selectable by decisions,
    per-member already-merged, side-effect tokens, \\substack row breaks."""
    for bad in (r"\gdef\alpha{Z}\alpha", r"\let\x\y", r"\catcode`\a=13 a", r"\input{x}",
                r"x\\", r"{a\\b}", r"\global\def\q{}"):
        try:
            math_glyph(bad)
            assert False, "math_glyph accepted " + repr(bad)
        except IntakeRowError:
            pass
    for good in (r"\sum_{\substack{i<n\\j<m}}", r"\shortstack[l]{a\\b}", r"\delta", r"\letter"):
        assert math_glyph(good) == good, good
    assert macro_problem(r"\gdef\x{y}") and macro_problem(r"\makeatletter") and not macro_problem(r"\leq")
    assert family_members(r"T_0,\ldots,T_k") == [r"T_0,\ldots,T_k"]
    assert family_members("p,q_0,q_1,...") == ["p,q_0,q_1,..."] and family_members("a,b") == ["a", "b"]

    root = temp / "round12"
    hb = root / "handbook"
    routed = ADOPT_ROUTED_STATUS
    header = ",".join(FIELDS) + "\n"

    def make(files: dict) -> None:
        if root.exists():
            shutil.rmtree(root)
        base_files = {
            "main.tex": "\\input{parts/p01}\n\\input{annex/p01}\n",
            "annex/p01.tex": "",
            "parts/p01.tex": "\\chapter{One}\n\\input{parts/p01/a}\n",
            "parts/p01/a.tex": "\\section{A}\\label{sec:p01-a}\nText.\n",
            "registry/symbol-scopes.json": json_text({"schema_version": 1, "scopes": {}}),
            "registry/symbols.csv": header + "\\(c\\),c,canon role,global,n/a,sec:p01-a,\n",
            "bib/handbook.bib": "@book{Canon,\n  author={C},\n  title={Canon},\n  year={2000}\n}\n",
        }
        for rel, text in {**base_files, **files}.items():
            write_text_atomic(hb / rel, text)

    def run(argv: list[str]) -> tuple[int, dict]:
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            code = main(argv)
        return code, json.loads(stream.getvalue())

    def adopt(decisions: dict, apply: bool = False) -> tuple[int, dict]:
        write_json_atomic(root / "manifest.json", {"groups": [{
            "stem": "g", "integration_status": routed, "bodies": ["parts/p01/a"], "annexes": [],
            "symbol_intakes": ["registry/symbols-intake-g.csv"], "bibliography_intakes": []}]})
        write_json_atomic(root / "decisions.json", decisions)
        return run(["adopt", "--manifest", str(root / "manifest.json"), "--decisions",
                    str(root / "decisions.json")] + (["--apply"] if apply else []))

    def intake(*cells: tuple[str, str]) -> dict:
        cell = lambda value: '"' + value.replace('"', '""') + '"'  # noqa: E731
        return {"registry/symbols-intake-g.csv": header + "".join(
            cell(glyph) + "," + cell(macro) + ",probe role " + str(i) + ",g region,n/a,sec:p01-a,\n"
            for i, (glyph, macro) in enumerate(cells))}

    def kinds(items: list[dict]) -> list[str]:
        return sorted(item.get("kind", "") for item in items)

    def canonical_rows() -> list[dict]:
        return list(csv.DictReader(io.StringIO(read_text(hb / "registry/symbols.csv"))))[1:]

    edit = lambda line, **fields: {"group": "g", "line": line, "set": fields}  # noqa: E731
    old_root, old_base = ROOT, BASE
    try:
        globals()["ROOT"] = root
        globals()["BASE"] = hb
        # Unroute refuses a merged group (its canonical rows would lose their first_use)
        # and a held one; nothing is written.
        make({"parts/p01.tex": "\\chapter{One}\n\\input{parts/p01/a}\n\\input{parts/p01/s}\n",
              "parts/p01/s.tex": "\\section{S}\\label{sec:p01-s}\n"})
        manifest = root / "manifest.json"
        host = read_text(hb / "parts/p01.tex")
        for status in ("merged", "merged-ready10", "saved-off-route", "frozen-unrouted"):
            write_json_atomic(manifest, {"groups": [{
                "stem": "s", "integration_status": status, "bodies": ["parts/p01/s"],
                "placement": {"host": "parts/p01", "after": "parts/p01/a", "input": "parts/p01/s"}}]})
            code, out = run(["unroute", "--manifest", str(manifest), "--stems", "s", "--apply"])
            assert code == 1 and not out["ok"] and out["errors"][0]["stem"] == "s", (status, out)
            assert read_text(hb / "parts/p01.tex") == host
            assert load_json(manifest)["groups"][0]["integration_status"] == status
        # Route promotes only returned / returned-for-fix; an unknown status is an error.
        make({"parts/p01/s.tex": "\\section{S}\\label{sec:p01-s}\n"})
        host = read_text(hb / "parts/p01.tex")
        write_json_atomic(manifest, {"groups": [{
            "stem": "s", "integration_status": "bogus-status", "bodies": ["parts/p01/s"],
            "placement": {"host": "parts/p01", "after": "parts/p01/a", "input": "parts/p01/s"}}]})
        code, out = run(["route", "--manifest", str(manifest), "--apply"])
        assert code == 1 and "unknown integration_status" in out["errors"][0]["error"], out
        assert read_text(hb / "parts/p01.tex") == host
        assert load_json(manifest)["groups"][0]["integration_status"] == "bogus-status"

        # A glyph-only row edit re-fills a blank-filled macro; an edit that sets the macro
        # keeps it and drops the fill note.
        make(intake(("≤", ""), ("x", ""), ("≥", "")))
        code, out = adopt({"row_edits": [edit(2, glyph="\\leq"), edit(3, glyph="\\xi"),
                                         edit(4, glyph="\\geq", macro="GE")]}, apply=True)
        assert code == 0, out
        rows = {row["glyph"]: row for row in canonical_rows()}
        assert rows["\\(\\leq\\)"]["macro"] == "\\leq" and MACRO_FILL_NOTE in rows["\\(\\leq\\)"]["notes"]
        assert rows["\\(\\xi\\)"]["macro"] == "\\xi", rows
        assert rows["\\(\\geq\\)"]["macro"] == "GE" and MACRO_FILL_NOTE not in rows["\\(\\geq\\)"]["notes"]

        # A non-ASCII macro cell needs a decision (incoming, row_edits, canonical_row_edits).
        make(intake(("\\leq", "≤")))
        code, out = adopt({})
        assert code == 1 and kinds(out["decisions-needed"]) == ["macro-non-ascii"], out
        code, out = adopt({"row_edits": [edit(2, macro="\\leq")]})
        assert code == 0, out
        make(intake(("\\leq", "\\leq")))
        code, out = adopt({"row_edits": [edit(2, macro="≤")]})
        assert code == 1 and kinds(out["decisions-needed"]) == ["macro-non-ascii"], out
        code, out = adopt({"canonical_row_edits": [{"line": 2, "set": {"macro": "ĉ"}}]})
        assert code == 1 and kinds(out["decisions-needed"]) == ["macro-non-ascii"], out
        assert out["decisions-needed"][0]["group"] == "canonical", out

        # A sequence glyph stays one row with the author's macro; a true family notes the
        # author macro it does not carry to its members.
        make(intake(("T_0,\\ldots,T_k", "T_j"), ("a,b", "ab")))
        code, out = adopt({}, apply=True)
        assert code == 0, out
        rows = {row["glyph"]: row for row in canonical_rows()}
        assert rows["\\(T_0,\\ldots,T_k\\)"]["macro"] == "T_j", rows
        assert "\\(\\ldots\\)" not in rows and set(rows) == {
            "\\(T_0,\\ldots,T_k\\)", "\\(a\\)", "\\(b\\)"}, rows
        assert r"Author macro \texttt{\detokenize{ab}} not carried" in rows[r"\(a\)"]["notes"], rows
        # Re-adopting the merged family is a no-op: each member is matched with canonical.
        code, out = adopt({}, apply=True)
        assert code == 0 and out["new_symbol_rows"] == 0 and not out["decisions-needed"], out

        # A refused row is reported with its raw cell and remedy; drop_rows and row_edits
        # select it by group+line (an edited glyph replaces the raw cell).
        make(intake(("\\(A\\), \\(B\\)", ""), ("\\kappa", "")))
        code, out = adopt({})
        assert code == 1 and kinds(out["errors"]) == ["intake-row-refused"], out
        assert "raw glyph cell '\\\\(A\\\\), \\\\(B\\\\)'" in out["errors"][0]["error"], out
        assert "row_edits" in out["errors"][0]["error"], out
        code, out = adopt({"drop_rows": [{"group": "g", "line": 2}]})
        assert code == 0 and out["new_symbol_rows"] == 1, out
        code, out = adopt({"row_edits": [edit(2, glyph="A,B")]}, apply=True)
        assert code == 0 and out["new_symbol_rows"] == 3, out
        assert {"\\(A\\)", "\\(B\\)", "\\(\\kappa\\)"} <= {row["glyph"] for row in canonical_rows()}
        code, out = adopt({"row_edits": [edit(2, glyph="\\(C")]})
        assert code == 1 and "after its row_edits" in out["errors"][0]["error"], out

        # Side-effect tokens are refused in glyph and macro cells.
        make(intake(("\\gdef\\alpha{Z}\\alpha", "")))
        code, out = adopt({})
        assert code == 1 and "\\gdef" in out["errors"][0]["error"], out
        make(intake(("\\alpha", "\\let\\a\\b")))
        code, out = adopt({})
        assert code == 1 and "\\let" in out["errors"][0]["error"], out
    finally:
        globals()["ROOT"] = old_root
        globals()["BASE"] = old_base


def selftest_round13(temp: Path) -> None:
    """Fixtures for repair round 13: the heading in force at the insertion point (annex
    files after heading-less annex siblings, after a heading-less restoration continuation,
    after a chapter-opening sibling), before_input placements, accounting returns, glyph
    commands acting outside the table cell, and an undefined author macro on a family."""
    hb = temp / "round13" / "handbook"
    files = {
        "main.tex": "\\input{parts/p01}\n\\input{parts/p02}\n\\hbannexsetup\n\\input{annex/p01-route}\n",
        # p01: restoration scopes wrap the inherited text; the second is a heading-less
        # continuation of the first one's section.
        "parts/p01.tex": "\\input{restoration/scope-1}\n\\input{restoration/scope-2}\n",
        "restoration/scope-1.tex": "\\begin{x}\n\\input{restoration/inherited-1}\n\\end{x}\n",
        "restoration/inherited-1.tex": "\\chapter{Strings}\n\\section{Concatenation}\nText.\n",
        "restoration/scope-2.tex": "\\begin{x}\n\\input{restoration/inherited-2}\n\\end{x}\n",
        "restoration/inherited-2.tex": "Continuation text, no heading.\n",
        # p02: a host whose inputs each open with \chapter and hold sections; a \part before.
        "parts/p02.tex": "\\part{Classical}\n\\input{parts/p02/first-order-logic}\n",
        "parts/p02/first-order-logic.tex": "\\input{parts/p02/depth}\n\\input{parts/p02/variants}\n",
        "parts/p02/depth.tex": "\\chapter{Depth}\n\\section{D1}\n",
        "parts/p02/variants.tex": "\\chapter{Variants}\n\\section{V1}\n\\section{V2}\n",
        # The annex host: a chapter opened by \hbannexchapter and heading-less annex items.
        "annex/p01-route.tex": ("%% Active annex.\n\\hbannexchapter{1}{Foundations}\\label{annex:p01}\n"
                                "\\input{annex/p01/bpi}\n\\input{annex/p01/eq}\n"),
        "annex/p01/bpi.tex": "\\begin{annexitem}{annex:p01.bpi}{thm:x}{BPI}\nProof.\n\\end{annexitem}\n",
        "annex/p01/eq.tex": "No heading.\n",
        "annex/p01/new-w99-p01-001.tex": "%% toc: P1 1 1.2\n\\section{Proofs for 1.2}\n",
        "annex/p01/sub.tex": "\\subsection{Too deep}\n",
        "parts/p01/new-w99-p01-011.tex": "%% toc: P1 4 4.5\n\\section{Grammars}\n",
        "parts/p02/new-w99-p02-036.tex": "%% toc: P2 30 30.4\n\\section{Interpolation}\n",
        "parts/p02/new-chapter.tex": "\\chapter{Another}\n",
        "parts/p02/new-section.tex": "\\section{Right after the part}\n",
    }
    for rel, text in files.items():
        write_text_atomic(hb / rel, text)

    def route(*placements: dict, siblings: list[dict] | None = None, apply: bool = False) -> dict:
        return simulate_route(hb, list(placements), apply=apply, siblings=siblings)

    # Heading in force (M5 class): a \section annex file after a heading-less annex sibling
    # (the \hbannexchapter chapter is in force), a \section after a heading-less restoration
    # continuation, and a \section or \chapter after a chapter-opening sibling with sections.
    annex = {"host": "annex/p01-route", "after": "annex/p01/bpi", "input": "annex/p01/new-w99-p01-001"}
    assert heading_in_force(hb, "annex/p01-route.tex", 3) == "hbannexchapter"
    assert route(annex)["ok"], route(annex)
    assert route(dict(annex, after="annex/p01/eq"))["ok"]
    result = route({"host": "annex/p01-route", "before": "annex/p01/bpi", "input": "annex/p01/sub"})
    assert not result["ok"] and result["errors"][0]["heading_in_force"] == "hbannexchapter", result
    body = {"host": "parts/p01", "after": "restoration/scope-2", "input": "parts/p01/new-w99-p01-011"}
    assert heading_in_force(hb, "parts/p01.tex", 2) == "section"
    assert route(body)["ok"], route(body)
    fol = {"host": "parts/p02/first-order-logic", "after": "parts/p02/depth"}
    assert heading_in_force(hb, "parts/p02/first-order-logic.tex", 1) == "section"
    for new in ("parts/p02/new-w99-p02-036", "parts/p02/new-chapter"):
        assert route(dict(fol, input=new))["ok"], new
    assert route(dict(fol, after="parts/p02/variants", input="parts/p02/new-w99-p02-036"))["ok"]
    # Right after \part, a \section skips the chapter level; a \chapter does not.
    part = {"host": "parts/p02/first-order-logic", "before": "parts/p02/depth"}
    result = route(dict(part, input="parts/p02/new-section"))
    assert not result["ok"] and result["errors"][0]["heading_in_force"] == "part", result
    assert route(dict(part, input="parts/p02/new-chapter"))["ok"]
    assert heading_skip("subsection", "chapter") and not heading_skip("section", "chapter")
    assert not heading_skip(None, "part") and not heading_skip("subsection", None)

    # before placements: insert before the unique \input line, in reading order among
    # siblings that share it; after+before must name one point; refusals as for after.
    host = "\\chapter{One}\n\\input{parts/p01/a}\n\\input{parts/p01/m}\n\\input{parts/p01/z}\n"
    write_text_atomic(hb / "parts/p01.tex", host)
    for name, toc in (("a", ""), ("m", ""), ("z", ""), ("s3", "%% toc: P1 1 1.5\n"),
                      ("s4", "%% toc: P1 1 1.4\n"), ("b1", "%% toc: P1 1 1.7\n"),
                      ("b2", "%% toc: P1 1 1.8\n")):
        write_text_atomic(hb / f"parts/p01/{name}.tex", toc + f"\\section{{{name}}}\n")
    write_text_atomic(hb / "parts/p01/m.tex", "Heading-less text.\n")
    p01 = {"host": "parts/p01"}
    b1 = dict(p01, before="parts/p01/z", input="parts/p01/b1")
    b2 = dict(p01, before="parts/p01/z", input="parts/p01/b2")
    result = route(b2, b1)
    assert result["ok"] and [a["insert_line"] for a in result["actions"]] == [4, 4], result
    assert result["shared_anchor_order"] == [{"host": "parts/p01.tex", "before": "parts/p01/z.tex",
                                              "inputs": ["parts/p01/b1.tex", "parts/p01/b2.tex"]}], result
    # after a + before s3, where s3 is placed after a in the same run (return 004's shape):
    # s4 lands between them whichever comes first in the manifest.
    s3 = dict(p01, after="parts/p01/a", input="parts/p01/s3")
    s4 = dict(p01, after="parts/p01/a", before="parts/p01/s3", input="parts/p01/s4")
    for order in ((s3, s4), (s4, s3)):
        write_text_atomic(hb / "parts/p01.tex", host)
        assert route(*order, apply=True)["ok"]
        assert read_text(hb / "parts/p01.tex") == host.replace(
            "\\input{parts/p01/a}\n", "\\input{parts/p01/a}\n\\input{parts/p01/s4}\n\\input{parts/p01/s3}\n")
        again = route(*order, apply=True)
        assert again["ok"] and {a["action"] for a in again["actions"]} == {"noop-already-present"}
    # s4 alone, before the unrouted wave file s3 (the author self-check); s3 routed later
    # stays after s4 although its toc line sorts it first.
    write_text_atomic(hb / "parts/p01/s3.tex", "%% toc: P1 1 1.1\n\\section{s3}\n")
    write_text_atomic(hb / "parts/p01.tex", host)
    assert route(s4, apply=True)["ok"]
    assert route(s3, siblings=[s3, s4], apply=True)["ok"]
    assert "\\input{parts/p01/a}\n\\input{parts/p01/s4}\n\\input{parts/p01/s3}\n" in read_text(
        hb / "parts/p01.tex")
    write_text_atomic(hb / "parts/p01.tex", host)
    # after and before that name different points, or a before line that is missing,
    # repeated, or follows a non-sibling line: refused, nothing inserted.
    for placement, error in (
            (dict(p01, after="parts/p01/a", before="parts/p01/z", input="parts/p01/b1"),
             "after and before name different insertion points"),
            (dict(p01, after="parts/p01/z", before="parts/p01/a", input="parts/p01/b1"),
             "after and before name different insertion points"),
            (dict(p01, before="parts/p01/missing", input="parts/p01/b1"), "before anchor occurs 0 times"),
            (dict(p01, after="parts/p01/a", before="parts/p01/missing", input="parts/p01/b1"),
             "before anchor occurs 0 times")):
        result = route(placement)
        assert not result["ok"] and result["errors"][0]["error"] == error, (placement, result)
    write_text_atomic(hb / "parts/p01.tex", host + "\\input{parts/p01/z}\n")
    result = route(b1)
    assert not result["ok"] and result["errors"][0]["error"] == "before anchor occurs 2 times", result
    write_text_atomic(hb / "parts/p01.tex", "\\chapter{One}\n\\AddToHook{env/x/begin}{\n"
                      "\\input{parts/p01/z}\n}\n")
    result = route(b1)
    assert not result["ok"] and "AddToHook bracket" in result["errors"][0]["error"], result
    write_text_atomic(hb / "parts/p01.tex", host)
    # Shapes: before alone is a placement; neither after nor before is malformed; the
    # packet keys after_input / before_input (null = absent) normalize to after / before.
    assert not placement_shape_errors(b1, "p") and iter_placements_in_value({"annex": b1})
    assert placement_shape_errors({"host": "h", "input": "i"}, "p") == ["p lacks after or before"]
    assert placement_shape_errors({"host": "h", "input": "i", "after": None, "before": "b"}, "p") == []
    assert normalized_placement({"host": "h", "after_input": None, "before_input": "b", "input": "i",
                                 "after_line": 2}, "p") == {"host": "h", "before": "b", "input": "i",
                                                            "after_line": 2}
    try:
        normalized_placement({"host": "h", "before": "x", "before_input": "b", "input": "i"}, "p")
        assert False, "before and before_input that differ must be refused"
    except Refusal:
        pass

    # Glyph and macro cells refuse commands that act outside the table cell.
    for bad in (r"\label{sym:x}", r"\phantomsection\label{entry:symbol-gate-00000}x", r"\index{x}x",
                r"\cite{Canon}", r"\parencite[2]{Canon}", r"\nocite{*}", r"\Citeauthor{C}",
                r"\hypertarget{h}{x}", r"\hyperlink{h}{x}", r"\fontdimen2\font=0pt",
                r"\hyphenchar\font=-1", r"\skewchar\font=1", r"\globaldefs=1 x", r"\batchmode x",
                r"\nonstopmode x", r"\scrollmode x", r"\errorstopmode x", r"\interactionmode=0 x",
                r"x\footnote{y}", r"\addcontentsline{toc}{section}{x}", r"\markboth{a}{b}x"):
        try:
            math_glyph(bad)
            assert False, "math_glyph accepted " + repr(bad)
        except IntakeRowError:
            pass
        assert macro_problem(bad), bad
    for good in (r"\mathrm{cite}", r"\operatorname{label}", r"\ref{sec:x}"):
        assert math_glyph(good) == good and not macro_problem(good), good

    # A family row with an author macro undefined in handbook.sty: the note shows the macro
    # literally, so the compile gate (adopt --apply) passes.
    row, _ = actual_row({"glyph": "p,q", "macro": "\\pq", "role": "pair", "scope": "s",
                         "precedence": "n/a", "first_use": "sec:x", "notes": ""},
                        {"stem": "g"}, "registry/x.csv", 2)
    assert r"Author macro \texttt{\detokenize{\pq}} not carried" in row["notes"], row
    assert "\\(\\pq" not in row["notes"], row

    # Accounting returns: collected with a normal return, they are listed, not made batch
    # groups; route --apply and adopt --apply then succeed for the normal group. A manifest
    # that already holds one (status returned, nothing owned) is skipped by both too.
    root = temp / "round13-collect"
    hb2 = root / "handbook"
    header = ",".join(FIELDS) + "\n"
    for rel, text in {
            "main.tex": "\\input{parts/p01}\n\\input{annex/p01}\n",
            "annex/p01.tex": "\\input{annex/p01/a}\n",
            "annex/p01/a.tex": "",
            "parts/p01.tex": "\\chapter{One}\n\\input{parts/p01/a}\n",
            "parts/p01/a.tex": "\\section{A}\\label{sec:p01-a}\n",
            "parts/p01/x-w99-p01-001.tex": "%% toc: P1 1 1.2\n\\section{X}\\label{sec:p01-x}\nUses \\(\\pq\\).\n",
            "annex/p01/x-w99-p01-001.tex": "%% toc: P1 1 1.2\n\\section{Proofs for X}\n",
            "registry/symbols-intake-p01-x-w99-p01-001.csv":
                header + "\"p,q\",\\pq,probe pair,x region,n/a,sec:p01-x,\n",
            "registry/symbol-scopes.json": json_text({"schema_version": 1, "scopes": {}}),
            "registry/symbols.csv": header,
            "bib/handbook.bib": "@book{Canon,\n  author={C},\n  title={Canon},\n  year={2000}\n}\n",
    }.items():
        write_text_atomic(hb2 / rel, text)
    packets = root / "work/waves/w99/packets"
    write_json_atomic(packets / "w99-p01-001.json", {
        "id": "w99-p01-001", "part": "P1", "label_tag": "p01-w99-p01-001", "editable_hosts": [],
        "owned_files": ["handbook/parts/p01/x-w99-p01-001.tex", "handbook/annex/p01/x-w99-p01-001.tex",
                        "handbook/registry/symbols-intake-p01-x-w99-p01-001.csv"]})
    write_json_atomic(packets / "w99-p01-002.json", {
        "id": "w99-p01-002", "part": "P1", "mode": "unit_accounting", "label_tag": "p01-w99-p01-002",
        "owned_files": [], "editable_hosts": [], "insertion": {"body": None, "annex": None}})
    research = root / "spec/research"
    for n in ("001", "002"):
        write_text_atomic(research / f"edition-2026-p01-x-w99-p01-{n}.md", "note\n")
    returns = [research / "edition-2026-p01-x-w99-p01-001-return.json",
               research / "edition-2026-p01-x-w99-p01-002-return.json"]
    write_json_atomic(returns[0], {
        "packet": "w99-p01-001", "notes": "spec/research/edition-2026-p01-x-w99-p01-001.md",
        "placement": {"body": {"host": "handbook/parts/p01.tex", "after_input": "parts/p01/a",
                               "input": "parts/p01/x-w99-p01-001"},
                      "annex": {"host": "handbook/annex/p01.tex", "after_input": None,
                                "before_input": "annex/p01/a", "input": "annex/p01/x-w99-p01-001"}},
        "files_written": ["handbook/parts/p01/x-w99-p01-001.tex"]})
    write_json_atomic(returns[1], {
        "packet": "w99-p01-002", "notes": "spec/research/edition-2026-p01-x-w99-p01-002.md",
        "placement": {"body": None, "annex": None, "reason": "accounting only"},
        "symbols": "none new; all symbols already appear in sec:p01-a", "files_written": []})
    manifest = research / "edition-2026-authoring-batch-intake-99.json"
    decisions = root / "decisions.json"
    write_json_atomic(decisions, {})

    def run(argv: list[str]) -> tuple[int, dict]:
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            code = main(argv)
        return code, json.loads(stream.getvalue())

    old_root, old_base = ROOT, BASE
    try:
        globals()["ROOT"] = root
        globals()["BASE"] = hb2
        code, out = run(["collect", "--wave", "99", "--apply", *map(str, returns)])
        assert code == 0 and out["groups"] == 1, out
        assert [item["stem"] for item in out["accounting_only"]] == ["p01-x-w99-p01-002"], out
        assert any(item.get("field") == "symbol_intakes" for item in out["files_written_not_adopted"]), out
        groups = load_json(manifest)["groups"]
        assert [g["stem"] for g in groups] == ["p01-x-w99-p01-001"], groups
        assert groups[0]["placement"]["annex"]["before"] == "annex/p01/a", groups
        # The same accounting return as a legacy group in the manifest: skipped, not blocking.
        data = load_json(manifest)
        data["groups"].append({"stem": "p01-x-w99-p01-002", "part": "P1", "bodies": [], "annexes": [],
                               "symbol_intakes": [], "bibliography_intakes": [],
                               "integration_status": "returned",
                               "placement": {"body": None, "annex": None, "reason": "accounting only"}})
        write_json_atomic(manifest, data)
        code, out = run(["route", "--manifest", str(manifest), "--apply"])
        assert code == 0 and out["ok"] and out["status_set_routed"] == ["p01-x-w99-p01-001"], out
        assert read_text(hb2 / "annex/p01.tex") == ("\\input{annex/p01/x-w99-p01-001}\n"
                                                    "\\input{annex/p01/a}\n")
        code, out = run(["adopt", "--manifest", str(manifest), "--decisions", str(decisions), "--apply"])
        assert code == 0 and out["ok"], out
        statuses = {g["stem"]: g["integration_status"] for g in load_json(manifest)["groups"]}
        assert statuses == {"p01-x-w99-p01-001": "merged", "p01-x-w99-p01-002": "returned"}, statuses
        rows = list(csv.DictReader(io.StringIO(read_text(hb2 / "registry/symbols.csv"))))
        assert {row["glyph"] for row in rows} == {r"\(p\)", r"\(q\)"}, rows
    finally:
        globals()["ROOT"] = old_root
        globals()["BASE"] = old_base


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selftest", action="store_true", help="run internal selftests")
    sub = parser.add_subparsers(dest="command")

    collect = sub.add_parser("collect")
    collect.add_argument("--wave", required=True, type=int)
    collect.add_argument("--apply", action="store_true")
    collect.add_argument("--force", action="store_true")
    collect.add_argument("return_json", nargs="+")
    collect.set_defaults(func=command_collect)

    route = sub.add_parser("route")
    route.add_argument("--manifest", required=True)
    route.add_argument("--apply", action="store_true")
    route.set_defaults(func=command_route)

    unroute = sub.add_parser("unroute")
    unroute.add_argument("--manifest", required=True)
    unroute.add_argument("--stems", required=True)
    unroute.add_argument("--apply", action="store_true")
    unroute.set_defaults(func=command_unroute)

    adopt = sub.add_parser("adopt")
    adopt.add_argument("--manifest", required=True)
    adopt.add_argument("--decisions", required=True)
    adopt.add_argument("--apply", action="store_true")
    adopt.add_argument("--return", dest="return_json")
    adopt.add_argument("--virtual-route", action="store_true")
    adopt.set_defaults(func=command_adopt)

    delta = sub.add_parser("check-delta")
    group = delta.add_mutually_exclusive_group(required=True)
    group.add_argument("--tag")
    group.add_argument("--init")
    group.add_argument("--stage")
    delta.add_argument("--manifest")
    delta.add_argument("--prev")
    delta.set_defaults(func=command_check_delta)

    scoped = sub.add_parser("scoped-build")
    scoped.add_argument("--snapshot", required=True)
    scoped.add_argument("--parts", required=True)
    scoped.set_defaults(func=command_scoped_build)

    summary = sub.add_parser("build-summary")
    summary.add_argument("log")
    summary.add_argument("--prev")
    summary.set_defaults(func=command_build_summary)
    return parser


def main(argv: list[str] | None = None) -> int:
    configure_stdout()
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.selftest:
        run_selftest()
        print_json({"ok": True, "command": "selftest"})
        return 0
    if not hasattr(args, "func"):
        parser.error("a command or --selftest is required")
    try:
        return args.func(args)
    except UsageError as exc:
        print_json({"ok": False, "error": str(exc)})
        return 2
    except Refusal as exc:
        print_json({"ok": False, "error": str(exc)})
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

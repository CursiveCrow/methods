#!/usr/bin/env python3
"""Find prose tokens where an expected space was fused away."""

from __future__ import annotations

import argparse
import bisect
import json
import os
import re
import sys
import tempfile
from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent.parent
ALLOWLIST_PATH = Path(__file__).resolve().with_name("fused_allowlist.txt")

LOWER_A_WORDS = {
    "to",
    "and",
    "or",
    "both",
    "between",
    "than",
    "of",
    "at",
    "is",
    "be",
    "are",
    "from",
    "through",
    "with",
    "by",
    "in",
    "on",
    "for",
    "as",
    "value",
    "stage",
    "rank",
    "input",
    "step",
    "level",
    "length",
    "size",
    "degree",
    "arity",
    "distance",
    "around",
    "about",
    "planned",
    "page",
    "pages",
    "pp",
    "line",
    "lines",
    "exactly",
    "least",
    "most",
    "only",
    "every",
    "each",
    "returned",
    "printed",
    "contains",
    "has",
    "gives",
    "yields",
    "circa",
    "until",
    "after",
    "before",
    "since",
    "during",
}

STRUCTURAL_A_WORDS = {
    "Axioms",
    "Theorem",
    "Theorems",
    "Lemma",
    "Lemmas",
    "Proposition",
    "Propositions",
    "Corollary",
    "Corollaries",
    "Definition",
    "Definitions",
    "Section",
    "Sections",
    "Chapter",
    "Chapters",
    "Example",
    "Examples",
    "Table",
    "Tables",
    "Figure",
    "Figures",
    "Remark",
    "Remarks",
    "Exercise",
    "Exercises",
    "Appendix",
    "Appendices",
    "Appendixes",
    "Volume",
    "Volumes",
    "Case",
    "Cases",
    "Axiom",
    "Equation",
    "Equations",
    "Rule",
    "Rules",
}

TEX_TIE_WORDS = {
    "Theorem",
    "Lemma",
    "Proposition",
    "Corollary",
    "Definition",
    "Section",
    "Chapter",
    "Example",
    "Table",
    "Figure",
    "Remark",
    "Exercise",
    "Appendix",
    "Equation",
    "Axiom",
}

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)

B_EXACT_ALLOWLIST = {"2EXPTIME", "2SAT", "3SAT", "2NEXPTIME"}
B_UNIT_ALLOWLIST = {"pt", "em", "ex", "cm", "mm", "in", "bp", "sp", "pc"}

MATH_ENVS = (
    "equation",
    "align",
    "gather",
    "multline",
    "eqnarray",
    "array",
    "tabular",
    "displaymath",
    "math",
)

ARG_COMMANDS = {
    "label": 1,
    "ref": 1,
    "cref": 1,
    "Cref": 1,
    "eqref": 1,
    "pageref": 1,
    "autoref": 1,
    "url": 1,
    "input": 1,
    "include": 1,
    "entrysources": 1,
    "showcalculus": 1,
    "entrycalculus": 1,
    "hbrule": 5,
    "calculussheet": 3,
    "begin": 1,
    "end": 1,
    "index": 1,
    "texttt": 1,
    "nolinkurl": 1,
    "href": 1,
}

# Leading non-prose arguments per handbook.sty signature: {label}{status}{Title}
# and {label}{backref}{Title} mask two; {label}{Title} masks only the label.
LABEL_ARG_COUNTS = {
    "hbtheorem": 2,
    "hblemma": 2,
    "hbcorollary": 2,
    "annexitem": 2,
    "hbdefinition": 1,
    "hbconvention": 1,
    "hbmethod": 1,
    "hbexample": 1,
    "hbwarning": 1,
    "proofboundary": 1,
    "systementry": 1,
}

URL_COMMAND_RE = re.compile(r"\\(?:url|nolinkurl|href)(?![A-Za-z@])")
CITE_KEYS_RE = re.compile(r"\s*[^\s,{}\\\[\]]+(?:\s*,\s*[^\s,{}\\\[\]]+)*\s*,?\s*")

BARE_LABEL_RE = re.compile(
    r"(?<![\w\\])(?:part|sec|entry|def|thm|tab|fig|sheet|rule|annex|ch):"
    r"[A-Za-z0-9_.-]+"
)
PREFIX_GUARD = r"(?<![\w/.\\-])"
VERB_RE = re.compile(r"\\verb\*?([^A-Za-z\s*])[^\n]*?\1")
TIKZ_RE = re.compile(
    r"\\begin\s*\{\s*tikzpicture\s*\}(?s:.*?)\\end\s*\{\s*tikzpicture\s*\}"
)


@dataclass(frozen=True)
class Hit:
    line: int
    col: int
    cls: str
    match: str
    suggestion: str
    start: int = field(repr=False, compare=False)
    end: int = field(repr=False, compare=False)
    fixes: tuple[tuple[int, str], ...] = field(
        default_factory=tuple, repr=False, compare=False
    )


class UsageError(Exception):
    """A command-line input is invalid."""


def _is_escaped(text: str, index: int) -> bool:
    slash_count = 0
    pos = index - 1
    while pos >= 0 and text[pos] == "\\":
        slash_count += 1
        pos -= 1
    return slash_count % 2 == 1


def _mask_range(chars: list[str], start: int, end: int) -> None:
    start = max(0, start)
    end = min(len(chars), end)
    for index in range(start, end):
        if chars[index] != "\n":
            chars[index] = " "


def _mask_verb_and_comments(text: str, chars: list[str]) -> None:
    for match in VERB_RE.finditer(text):
        if not _is_escaped(text, match.start()):
            _mask_range(chars, match.start(), match.end())
    # URL arguments are read verbatim, so a "%" inside them is not a comment.
    # Braces stay so the later argument pass still finds this argument.
    for match in URL_COMMAND_RE.finditer(text):
        if _is_escaped(text, match.start()):
            continue
        url_start = _skip_optional_arguments(text, match.end())
        url = _balanced_range(text, url_start, "{", "}")
        if url is not None and "\n" not in text[url[0] : url[1]]:
            _mask_range(chars, url[0] + 1, url[1] - 1)
    staged = "".join(chars)
    line_start = 0
    for line in staged.split("\n"):
        limit = line_start + len(line)
        for offset, char in enumerate(line):
            absolute = line_start + offset
            if char == "%" and not _is_escaped(staged, absolute):
                _mask_range(chars, absolute, limit)
                break
        line_start = limit + 1


def _mask_tikz_code(text: str, chars: list[str]) -> None:
    # TikZ code outside brace groups (options, node names, coordinates) is not
    # prose; brace groups keep node text visible to the scan.
    for match in TIKZ_RE.finditer(text):
        depth = 0
        for index in range(match.start(), match.end()):
            char = text[index]
            if char == "{" and not _is_escaped(text, index):
                depth += 1
            elif char == "}" and not _is_escaped(text, index):
                depth = max(0, depth - 1)
            elif depth == 0:
                _mask_range(chars, index, index + 1)


def _mask_regex(text: str, chars: list[str], pattern: re.Pattern[str]) -> None:
    for match in pattern.finditer(text):
        _mask_range(chars, match.start(), match.end())


def _mask_delimited_math(text: str, chars: list[str]) -> None:
    # Delimiters count only with an unescaped backslash, so a line break such
    # as "\\[2pt]" or "\\(" does not open a math span.
    for opener, closer in (("\\(", "\\)"), ("\\[", "\\]")):
        start = _find_unescaped(text, opener, 0)
        while start != -1:
            end = _find_unescaped(text, closer, start + 2)
            if end == -1:
                break
            _mask_range(chars, start, end + 2)
            start = _find_unescaped(text, opener, end + 2)

    index = 0
    while index < len(text):
        if text[index] != "$" or _is_escaped(text, index):
            index += 1
            continue
        if index + 1 < len(text) and text[index + 1] == "$":
            end = _find_unescaped(text, "$$", index + 2)
            if end == -1:
                index += 2
                continue
            _mask_range(chars, index, end + 2)
            index = end + 2
            continue
        end = _find_single_dollar(text, index + 1)
        if end == -1:
            index += 1
            continue
        _mask_range(chars, index, end + 1)
        index = end + 1


def _find_unescaped(text: str, needle: str, start: int) -> int:
    index = text.find(needle, start)
    while index != -1:
        if not _is_escaped(text, index):
            return index
        index = text.find(needle, index + 1)
    return -1


def _find_single_dollar(text: str, start: int) -> int:
    index = text.find("$", start)
    while index != -1:
        if not _is_escaped(text, index):
            if index + 1 >= len(text) or text[index + 1] != "$":
                return index
        index = text.find("$", index + 1)
    return -1


def _skip_spaces(text: str, index: int) -> int:
    while index < len(text) and text[index].isspace():
        index += 1
    return index


def _balanced_range(text: str, index: int, open_char: str, close_char: str) -> tuple[int, int] | None:
    index = _skip_spaces(text, index)
    if index >= len(text) or text[index] != open_char:
        return None
    depth = 0
    # An optional [..] argument closes only on a "]" outside any {} group.
    brace_depth = 0
    pos = index
    while pos < len(text):
        char = text[pos]
        if _is_escaped(text, pos):
            pass
        elif open_char == "[" and char == "{":
            brace_depth += 1
        elif open_char == "[" and char == "}":
            brace_depth = max(0, brace_depth - 1)
        elif brace_depth > 0:
            pass
        elif char == open_char:
            depth += 1
        elif char == close_char:
            depth -= 1
            if depth == 0:
                return index, pos + 1
        pos += 1
    return None


def _mask_optional_and_mandatory(
    text: str, chars: list[str], index: int, mandatory_count: int
) -> None:
    pos = _skip_spaces(text, index)
    while True:
        optional = _balanced_range(text, pos, "[", "]")
        if optional is None:
            break
        _mask_range(chars, optional[0], optional[1])
        pos = _skip_spaces(text, optional[1])
    for _ in range(mandatory_count):
        mandatory = _balanced_range(text, pos, "{", "}")
        if mandatory is None:
            return
        _mask_range(chars, mandatory[0], mandatory[1])
        pos = _skip_spaces(text, mandatory[1])


def _skip_optional_arguments(text: str, index: int) -> int:
    pos = _skip_spaces(text, index)
    while True:
        optional = _balanced_range(text, pos, "[", "]")
        if optional is None:
            return pos
        pos = _skip_spaces(text, optional[1])


def _mask_mandatory_after_optional(
    text: str, chars: list[str], index: int, mandatory_count: int
) -> None:
    pos = _skip_optional_arguments(text, index)
    for _ in range(mandatory_count):
        mandatory = _balanced_range(text, pos, "{", "}")
        if mandatory is None:
            return
        _mask_range(chars, mandatory[0], mandatory[1])
        pos = _skip_spaces(text, mandatory[1])


def _mask_first_optional(text: str, chars: list[str], index: int) -> None:
    optional = _balanced_range(text, index, "[", "]")
    if optional is not None:
        _mask_range(chars, optional[0], optional[1])


def _mask_multicite_groups(text: str, chars: list[str], index: int) -> None:
    # Mask ([pre][post]{keys})+ and stop at the first unit that is not a
    # complete citation unit whose braces hold a key list.
    pos = index
    while True:
        unit = []
        for _ in range(2):
            optional = _balanced_range(text, pos, "[", "]")
            if optional is None:
                break
            unit.append(optional)
            pos = optional[1]
        keys = _balanced_range(text, pos, "{", "}")
        if keys is None or not CITE_KEYS_RE.fullmatch(text[keys[0] + 1 : keys[1] - 1]):
            return
        unit.append(keys)
        for start, end in unit:
            _mask_range(chars, start, end)
        pos = keys[1]


def _is_cite_command(name: str) -> bool:
    lowered = name.lower()
    return lowered.startswith("cite") or lowered.endswith(("cite", "cites"))


def _mask_macro_arguments(text: str, chars: list[str]) -> None:
    command_re = re.compile(r"\\([A-Za-z@]+)\*?")
    for match in command_re.finditer(text):
        if _is_escaped(text, match.start()):
            continue
        name = match.group(1)
        mandatory_count = ARG_COMMANDS.get(name)
        if mandatory_count is not None:
            _mask_optional_and_mandatory(text, chars, match.end(), mandatory_count)
        elif name == "hyperref":
            _mask_first_optional(text, chars, match.end())
        elif _is_cite_command(name):
            if name.lower().endswith("cites"):
                _mask_multicite_groups(text, chars, match.end())
            else:
                _mask_optional_and_mandatory(text, chars, match.end(), 1)
        elif name in LABEL_ARG_COUNTS:
            _mask_mandatory_after_optional(
                text, chars, match.end(), LABEL_ARG_COUNTS[name]
            )


def _mask_environment_label_args(text: str, chars: list[str]) -> None:
    names = "|".join(re.escape(name) for name in sorted(LABEL_ARG_COUNTS))
    pattern = re.compile(r"\\begin\s*\{\s*(" + names + r")\s*\}")
    for match in pattern.finditer(text):
        if _is_escaped(text, match.start()):
            continue
        _mask_mandatory_after_optional(
            text, chars, match.end(), LABEL_ARG_COUNTS[match.group(1)]
        )


def _mask_tex(text: str) -> str:
    chars = list(text)
    _mask_verb_and_comments(text, chars)

    staged = "".join(chars)
    _mask_regex(
        staged,
        chars,
        re.compile(
            r"\\begin\s*\{\s*verbatim\*?\s*\}"
            r"(?s:.*?)"
            r"\\end\s*\{\s*verbatim\*?\s*\}"
        ),
    )
    staged = "".join(chars)
    _mask_tikz_code(staged, chars)

    envs = []
    for name in MATH_ENVS:
        envs.append(re.escape(name))
        envs.append(re.escape(name + "*"))
    math_env_re = re.compile(
        r"\\begin\s*\{\s*(" + "|".join(envs) + r")\s*\}"
        r"(?s:.*?)"
        r"\\end\s*\{\s*\1\s*\}"
    )
    staged = "".join(chars)
    _mask_regex(staged, chars, math_env_re)
    _mask_delimited_math(staged, chars)
    staged = "".join(chars)
    _mask_environment_label_args(staged, chars)
    _mask_macro_arguments(staged, chars)

    staged = "".join(chars)
    _mask_regex(staged, chars, re.compile(r"\b(?:proved|cited|sketched)=[^\s,\]}]+"))
    _mask_regex(staged, chars, BARE_LABEL_RE)
    staged = "".join(chars)
    _mask_regex(staged, chars, re.compile(r"\\[A-Za-z@]+\*?|\\."))
    return "".join(chars)


def _mask_md_link_targets(text: str, chars: list[str]) -> None:
    index = 0
    while True:
        start = text.find("](", index)
        if start == -1:
            return
        pos = start + 2
        depth = 1
        while pos < len(text):
            char = text[pos]
            if char == "\n":
                break
            if char == "(" and not _is_escaped(text, pos):
                depth += 1
            elif char == ")" and not _is_escaped(text, pos):
                depth -= 1
                if depth == 0:
                    _mask_range(chars, start + 1, pos + 1)
                    pos += 1
                    break
            pos += 1
        index = max(pos, start + 2)


def _mask_md(text: str) -> str:
    chars = list(text)
    _mask_regex(text, chars, re.compile(r"(?m)^```.*(?:\n(?:.*\n)*?)?^```[ \t]*$"))
    staged = "".join(chars)
    _mask_regex(staged, chars, re.compile(r"`[^`\n]*`"))
    staged = "".join(chars)
    _mask_md_link_targets(staged, chars)
    staged = "".join(chars)
    _mask_regex(staged, chars, re.compile(r"<[^<>\n]+>"))
    staged = "".join(chars)
    _mask_regex(staged, chars, re.compile(r"https?://[^\s<>\]]+"))
    return "".join(chars)


def _line_starts(text: str) -> list[int]:
    starts = [0]
    for match in re.finditer("\n", text):
        starts.append(match.end())
    return starts


def _line_col(starts: list[int], index: int) -> tuple[int, int]:
    line_index = bisect.bisect_right(starts, index) - 1
    return line_index + 1, index - starts[line_index] + 1


def _make_hit(
    original: str,
    starts: list[int],
    cls: str,
    start: int,
    end: int,
    suggestion: str,
    fixes: tuple[tuple[int, str], ...],
) -> Hit:
    line, col = _line_col(starts, start)
    return Hit(
        line=line,
        col=col,
        cls=cls,
        match=original[start:end],
        suggestion=suggestion,
        start=start,
        end=end,
        fixes=fixes,
    )


def _a_word_pattern() -> re.Pattern[str]:
    capitalized_lower = {word[:1].upper() + word[1:] for word in LOWER_A_WORDS}
    words = sorted(
        LOWER_A_WORDS | capitalized_lower | STRUCTURAL_A_WORDS,
        key=len,
        reverse=True,
    )
    return re.compile(
        PREFIX_GUARD
        + r"("
        + "|".join(re.escape(word) for word in words)
        + r")(\d{1,4}(?:\.\d+)?)(?!\d)"
    )


A_WORD_RE = _a_word_pattern()
A_YEAR_RE = re.compile(PREFIX_GUARD + r"([a-z]{3,})(\d{3,4})(?!\d)")
B_RE = re.compile(PREFIX_GUARD + r"(\d{1,4})([A-Za-z]{3,})")
B_MONTH_RE = re.compile(r"(\d+)(" + "|".join(MONTHS) + r")(\d+)")
C_PUNCT_RE = re.compile(r"(?<=\w)([:;])\d(?=[A-Za-z])")
C_COMMA_RE = re.compile(r"(?<=[a-z]),(?=\d{4}\b)")
D_RE = re.compile(r"\b[A-Z][a-z]{2,}[A-Z][a-z]{2,}\b")


def _load_d_allowlist() -> set[str]:
    default = {
        "PostScript",
        "JavaScript",
        "LaTeX",
        "BibTeX",
        "MiniSat",
        "PageRank",
        "NetLogo",
        "MathSciNet",
        "DeepMind",
        "OpenAI",
        "GitHub",
        "YouTube",
    }
    try:
        with ALLOWLIST_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
            for line in handle:
                stripped = line.strip()
                if stripped and not stripped.startswith("#"):
                    default.add(stripped)
    except OSError:
        pass
    return default


def _is_b_allowed(token: str, letters: str) -> bool:
    if token in B_EXACT_ALLOWLIST:
        return True
    if re.fullmatch(r"\d+(?:st|nd|rd|th)", token, re.IGNORECASE):
        return True
    return letters.lower() in B_UNIT_ALLOWLIST


def _overlaps(existing: Iterable[Hit], start: int, end: int) -> bool:
    return any(start < hit.end and end > hit.start for hit in existing)


def _scan(original: str, masked: str, *, tex: bool) -> list[Hit]:
    starts = _line_starts(original)
    hits: list[Hit] = []

    for match in A_WORD_RE.finditer(masked):
        word = match.group(1)
        number = match.group(2)
        separator = "~" if tex and word in TEX_TIE_WORDS else " "
        hits.append(
            _make_hit(
                original,
                starts,
                "A",
                match.start(),
                match.end(),
                f"{word}{separator}{number}",
                ((match.start(2), separator),),
            )
        )

    for match in A_YEAR_RE.finditer(masked):
        if _overlaps(hits, match.start(), match.end()):
            continue
        word = match.group(1)
        number = match.group(2)
        hits.append(
            _make_hit(
                original,
                starts,
                "A",
                match.start(),
                match.end(),
                f"{word} {number}",
                ((match.start(2), " "),),
            )
        )

    for match in B_MONTH_RE.finditer(masked):
        fixes = [(match.start(2), " "), (match.start(3), " ")]
        if (
            match.start() >= 2
            and original[match.start() - 1] in ":;"
            and original[match.start() - 2].isalnum()
        ):
            fixes.insert(0, (match.start(), " "))
        month = match.group(2)
        year = match.group(3)
        hits.append(
            _make_hit(
                original,
                starts,
                "B",
                match.start(),
                match.end(),
                f"{match.group(1)} {month} {year}",
                tuple(fixes),
            )
        )

    for match in B_RE.finditer(masked):
        if _overlaps(hits, match.start(), match.end()):
            continue
        token = match.group(0)
        letters = match.group(2)
        if _is_b_allowed(token, letters):
            continue
        hits.append(
            _make_hit(
                original,
                starts,
                "B",
                match.start(),
                match.end(),
                f"{match.group(1)} {letters}",
                ((match.start(2), " "),),
            )
        )

    for match in C_PUNCT_RE.finditer(masked):
        punct = match.group(1)
        hits.append(
            _make_hit(
                original,
                starts,
                "C",
                match.start(),
                match.end(),
                f"{punct} {original[match.start() + 1]}",
                ((match.start() + 1, " "),),
            )
        )

    for match in C_COMMA_RE.finditer(masked):
        hits.append(
            _make_hit(
                original,
                starts,
                "C",
                match.start(),
                match.end(),
                ", ",
                ((match.end(), " "),),
            )
        )

    allowlist = _load_d_allowlist()
    for match in D_RE.finditer(masked):
        token = match.group(0)
        if token in allowlist:
            continue
        if re.match(r"Mc[A-Z]|Mac[A-Z]", token):
            continue
        hits.append(
            _make_hit(
                original,
                starts,
                "D",
                match.start(),
                match.end(),
                token,
                (),
            )
        )

    return sorted(hits, key=lambda hit: (hit.line, hit.col, hit.cls, hit.match))


def scan_tex(text: str) -> list[Hit]:
    return _scan(text, _mask_tex(text), tex=True)


def scan_md(text: str) -> list[Hit]:
    return _scan(text, _mask_md(text), tex=False)


def _selected_classes(raw: str, include_d: bool) -> set[str]:
    classes = {part.strip().upper() for part in raw.split(",") if part.strip()}
    valid = {"A", "B", "C", "D"}
    if not classes or not classes <= valid:
        raise ValueError("--classes must be a comma-separated subset of A,B,C,D")
    if include_d:
        classes.add("D")
    return classes


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def _resolve_manifest_entry(value: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path.resolve()
    if path.parts[:1] == ("handbook",):
        return (ROOT / path).resolve()
    return (ROOT / "handbook" / path).resolve()


def _iter_manifest_paths(manifest: Path) -> list[Path]:
    data = json.loads(_read_text(manifest))
    found: list[Path] = []

    def collect_from_value(value: object) -> None:
        if value is None:
            return
        if isinstance(value, str):
            found.append(_resolve_manifest_entry(value))
        elif isinstance(value, list):
            for item in value:
                collect_from_value(item)
        elif isinstance(value, dict):
            for key in ("path", "file", "body", "annex"):
                if key in value:
                    collect_from_value(value[key])

    def walk(value: object) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if key in {"bodies", "annexes", "body", "annex", "source_files"}:
                    collect_from_value(child)
                else:
                    walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(data)
    paths = _dedupe_paths(found)
    if not paths:
        raise UsageError(f"{manifest}: manifest yielded no paths")
    missing = [path for path in paths if not path.is_file()]
    if missing:
        raise UsageError(
            "\n".join(
                f"{manifest}: manifest path does not exist: {_path_for_output(path)}"
                for path in missing
            )
        )
    return paths


def _dedupe_paths(paths: Iterable[Path]) -> list[Path]:
    seen: set[Path] = set()
    result: list[Path] = []
    for path in paths:
        resolved = path.resolve()
        if resolved not in seen:
            seen.add(resolved)
            result.append(resolved)
    return result


def _iter_paths(paths: list[str], *, md: bool, manifest: str | None) -> list[Path]:
    result: list[Path] = []
    suffix = ".md" if md else ".tex"
    if manifest:
        result.extend(_iter_manifest_paths(Path(manifest)))
    for raw in paths:
        path = Path(raw)
        if not path.is_absolute():
            path = ROOT / path
        path = path.resolve()
        if path.is_dir():
            result.extend(sorted(path.rglob(f"*{suffix}")))
        elif path.is_file():
            result.append(path)
        else:
            raise UsageError(f"{raw}: path does not exist")
    return _dedupe_paths(result)


def _path_for_output(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def _scan_file(path: Path, *, md: bool) -> tuple[str, list[Hit]]:
    text = _read_text(path)
    return text, scan_md(text) if md else scan_tex(text)


def _hit_to_json(path: Path, hit: Hit) -> dict[str, object]:
    return {
        "path": _path_for_output(path),
        "line": hit.line,
        "col": hit.col,
        "cls": hit.cls,
        "match": hit.match,
        "suggestion": hit.suggestion,
    }


def _print_human(path: Path, hits: list[Hit]) -> None:
    for hit in hits:
        print(
            f"{_path_for_output(path)}:{hit.line}:{hit.col}: "
            f"{hit.cls} {hit.match!r} -> {hit.suggestion!r}"
        )


def _under(relative: Path, prefix: str) -> bool:
    parts = relative.parts
    prefix_parts = tuple(Path(prefix).parts)
    return len(parts) >= len(prefix_parts) and parts[: len(prefix_parts)] == prefix_parts


def _refusal_reason(path: Path) -> str | None:
    try:
        relative = path.resolve().relative_to(ROOT)
    except ValueError:
        return "outside repository root"

    if _under(relative, "handbook/restoration"):
        return "under handbook/restoration"
    if _under(relative, "handbook/generated"):
        return "under handbook/generated"
    if _under(relative, "citations"):
        return "under citations"
    if _under(relative, "source"):
        return "under source"

    try:
        import check  # type: ignore
    except Exception as exc:  # pragma: no cover - import should work in the repo
        return f"cannot import tools/check.py for retained-file refusal: {exc}"

    retained = getattr(check, "HB_RETAINED_UNREACHABLE_READER_FILES", None)
    if not isinstance(retained, Mapping):
        return "cannot read retained-file refusal list from tools/check.py"
    handbook_prefix = ("handbook",)
    if relative.parts[:1] == handbook_prefix:
        handbook_relative = Path(*relative.parts[1:]).as_posix()
        if handbook_relative in retained:
            return "digest-pinned retained file"
    return None


def _fixed_text(text: str, hits: list[Hit]) -> str:
    fixes: dict[int, str] = {}
    for hit in hits:
        for index, inserted in hit.fixes:
            fixes.setdefault(index, inserted)
    pieces = list(text)
    for index, inserted in sorted(fixes.items(), reverse=True):
        pieces.insert(index, inserted)
    return "".join(pieces)


def _write_atomic(path: Path, text: str) -> None:
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


def _selftest() -> None:
    global ROOT

    positive = (
        "around1115 in1348 Theorem4.13 between0 and1 "
        "Date:3October2026 300seconds Date:12October2026 "
        "Rules1 Theorems9 In1348"
    )
    hits = [hit for hit in scan_tex(positive) if hit.cls in {"A", "B", "C"}]
    matched = {hit.match for hit in hits}
    assert "around1115" in matched
    assert "in1348" in matched
    assert "Theorem4.13" in matched
    assert "between0" in matched
    assert "and1" in matched
    assert "300seconds" in matched
    assert "12October2026" in matched
    assert "Rules1" in matched
    assert "Theorems9" in matched
    assert "In1348" in matched
    assert any(hit.cls == "C" and hit.match == ":3" for hit in hits)
    assert any(hit.cls == "B" and hit.match == "3October2026" for hit in hits)
    theorem = next(hit for hit in hits if hit.match == "Theorem4.13")
    assert theorem.suggestion == "Theorem~4.13"

    negative = r"""
\cite[p.~97]{Rubinstein2015LectureNotes}
\label{thm:p04-wc-basic}
$x_1+x2$ and \(ET5 + CF3\)
2EXPTIME
annex:p15.x
Lemma~4.4
"""
    negative_hits = [
        hit for hit in scan_tex(negative) if hit.cls in {"A", "B", "C"}
    ]
    assert negative_hits == []

    fixed = _fixed_text(positive, hits)
    assert "around 1115" in fixed
    assert "in 1348" in fixed
    assert "Theorem~4.13" in fixed
    assert "between 0 and 1" in fixed
    assert "Date: 3 October 2026" in fixed
    assert "Date: 12 October 2026" in fixed
    assert "300 seconds" in fixed

    trailing = "in1340s and2x Theorem4a of2nd 300seconds5 x3October20265"
    trailing_hits = {hit.match: hit for hit in scan_tex(trailing)}
    assert trailing_hits["in1340"].suggestion == "in 1340"
    assert trailing_hits["and2"].cls == "A"
    assert trailing_hits["Theorem4"].suggestion == "Theorem~4"
    assert trailing_hits["of2"].cls == "A"
    assert trailing_hits["300seconds"].cls == "B"
    assert trailing_hits["3October20265"].cls == "B"
    fixed_trailing = _fixed_text(trailing, list(trailing_hits.values()))
    assert fixed_trailing == (
        "in 1340s and 2x Theorem~4a of 2nd 300 seconds5 x3 October 20265"
    )

    verb_and_comment = "\\verb|%| in1348 \\verb+in1349+\n% a\x0cin1350\n"
    assert [hit.match for hit in scan_tex(verb_and_comment)] == ["in1348"]
    tikz = (
        "\\begin{tikzpicture}[node distance=of is2]\n"
        "\\node (is1) at (0,0) {};\n\\draw (is1) -- (is2);\n"
        "\\node at (1,1) {around1115};\n\\end{tikzpicture}"
    )
    assert [hit.match for hit in scan_tex(tikz)] == ["around1115"]

    masked_negatives = [
        "% costs in $ here\nWe have $x + in2$",
        "\\begin{verbatim}\necho $HOME\n\\end{verbatim}\nThen $y = in3$",
        "\\begin{equation}\nx % \\end{equation}\n in2\n\\end{equation}",
        "\\cite{a,% see }\n kleene1952intro}",
    ]
    for text in masked_negatives:
        assert [hit for hit in scan_tex(text) if hit.cls in {"A", "B", "C"}] == []

    cite_negatives = r"""
\citeyear{gentzen1935untersuchungen}
\citeauthor{kleene1952introduction}
\cites{kleene1952introduction}{tarski1936concept}
"""
    assert [
        hit for hit in scan_tex(cite_negatives) if hit.cls in {"A", "B", "C"}
    ] == []

    theorem_title = r"\begin{hbtheorem}[Title around1115]{thm:x}{proved}"
    assert any(hit.match == "around1115" for hit in scan_tex(theorem_title))
    hyperref_text = r"\hyperref[sec:x]{around1115}"
    assert any(hit.match == "around1115" for hit in scan_tex(hyperref_text))
    def abc_matches(text: str) -> list[str]:
        return [hit.match for hit in scan_tex(text) if hit.cls in {"A", "B", "C"}]

    # {label}{Title} environments mask only the label; titles stay prose.
    assert abc_matches(r"\begin{hbdefinition}{def:x}{Title Theorem4.4}") == [
        "Theorem4.4"
    ]
    assert abc_matches(r"\hbwarning{def:x}{Title in1348}") == ["in1348"]
    assert abc_matches(
        r"\begin{annexitem}{annex:x}{thm:in1349}{Title around1115}"
    ) == ["around1115"]
    assert abc_matches(r"\begin{hblemma}{thm:x}{cited=in1349}{T in1348}") == [
        "in1348"
    ]
    # An escaped backslash does not open \[..\], \(..\) or a macro.
    assert abc_matches(r"x\\[2pt] in1348 \[a\]") == ["in1348"]
    assert abc_matches(r"x\\(a) in1348 \(b\)") == ["in1348"]
    assert abc_matches(r"x\\label{in1348}") == ["in1348"]
    # Optional-argument brackets inside braces do not close the argument.
    assert abc_matches(r"\cite[{p.~3]x}]{kleene1952intro}") == []
    # \href hides only its URL; multicite hides only citation units.
    assert abc_matches(r"\href{https://x}{around1115}") == ["around1115"]
    assert abc_matches(r"\cites{a}{b} {\em around1115}") == ["around1115"]
    assert abc_matches(r"\cites{a}{in1348 years}") == ["in1348"]
    assert abc_matches(
        r"\cites[see][p.~3]{kleene1952intro}[]{tarski1936concept, gentzen1935}"
    ) == []
    # A "%" inside a URL argument is not a comment.
    assert abc_matches(r"\url{a%20b} in1348") == ["in1348"]
    assert abc_matches(r"\href{a%20b}{t} in1348") == ["in1348"]
    assert abc_matches(r"\nolinkurl{a%20b} in1348") == ["in1348"]

    protected_rule = r"\hbrule{rule:x}{Rule1}{..}{..}{..}"
    assert [
        hit for hit in scan_tex(protected_rule) if hit.cls in {"A", "B", "C"}
    ] == []
    protected_rule_side = r"\hbrule{rule:x}{Rule1}{\(A\)}{\(B\)}{side in1348}"
    assert [
        hit for hit in scan_tex(protected_rule_side) if hit.cls in {"A", "B", "C"}
    ] == []
    protected_sheet = r"\calculussheet{sheet:x}{Name1999 around1115}{ident}"
    assert [
        hit for hit in scan_tex(protected_sheet) if hit.cls in {"A", "B", "C"}
    ] == []

    md_hits = scan_md("PostScript and NotreDame")
    assert any(hit.cls == "D" and hit.match == "NotreDame" for hit in md_hits)
    assert not any(hit.match == "PostScript" for hit in md_hits)
    md_negative = "[x](a%20Jung.pdf) <https://e.test/a%20Jung.pdf> https://e.test/a%20Jung.pdf"
    assert [hit for hit in scan_md(md_negative) if hit.cls in {"A", "B", "C"}] == []

    assert _refusal_reason(ROOT / "handbook/restoration/x.tex") is not None
    assert _refusal_reason(ROOT / "handbook/generated/x.tex") is not None
    assert _refusal_reason(ROOT / "source/formal-logic-reference.tex") is not None
    assert _refusal_reason(ROOT / "citations/x.md") is not None
    assert (
        _refusal_reason(
            ROOT / "handbook/parts/p02/propositional-syntax-semantics.tex"
        )
        is not None
    )

    scratch_root = ROOT / "tmp" / "tooling-scratch" / "fused"
    scratch_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=scratch_root) as temp_dir:
        temp_path = Path(temp_dir)
        target = temp_path / "atomic.txt"
        _write_atomic(target, "alpha\nbeta\n")
        assert target.read_bytes() == b"alpha\nbeta\n"
        assert [path for path in temp_path.iterdir() if path != target] == []

    original_root = ROOT
    with tempfile.TemporaryDirectory(dir=scratch_root) as temp_dir:
        fake_root = Path(temp_dir)
        body = fake_root / "handbook" / "parts" / "p09" / "body.tex"
        annex = fake_root / "handbook" / "annex" / "p09" / "annex.tex"
        prefixed = fake_root / "handbook" / "parts" / "p09" / "prefixed.tex"
        source_file = fake_root / "handbook" / "parts" / "p09" / "source-file.tex"
        manifest = fake_root / "spec" / "research" / "intake.json"
        for path, text in (
            (body, "around1115\n"),
            (annex, "300seconds\n"),
            (prefixed, "in1348\n"),
            (source_file, "Date:3October2026\n"),
        ):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8", newline="\n")
        manifest.parent.mkdir(parents=True, exist_ok=True)
        manifest.write_text(
            json.dumps(
                {
                    "groups": [
                        {
                            "bodies": [
                                "parts/p09/body.tex",
                                "handbook/parts/p09/prefixed.tex",
                            ],
                            "annex": "annex/p09/annex.tex",
                        }
                    ],
                    "source_files": [{"path": "handbook/parts/p09/source-file.tex"}],
                }
            ),
            encoding="utf-8",
            newline="\n",
        )
        try:
            ROOT = fake_root
            paths = _iter_manifest_paths(manifest)
            assert paths == [
                body.resolve(),
                prefixed.resolve(),
                annex.resolve(),
                source_file.resolve(),
            ]
            scanned = []
            for path in paths:
                scanned.extend(hit.match for hit in _scan_file(path, md=False)[1])
            assert {"around1115", "in1348", "300seconds", ":3"} <= set(scanned)

            empty_manifest = fake_root / "spec" / "research" / "empty.json"
            empty_manifest.write_text(
                json.dumps({"groups": []}), encoding="utf-8", newline="\n"
            )
            try:
                _iter_manifest_paths(empty_manifest)
                raise AssertionError("empty manifest should be a usage error")
            except UsageError as exc:
                assert "manifest yielded no paths" in str(exc)

            missing_manifest = fake_root / "spec" / "research" / "missing.json"
            missing_manifest.write_text(
                json.dumps({"groups": [{"body": "parts/p09/missing.tex"}]}),
                encoding="utf-8",
                newline="\n",
            )
            try:
                _iter_manifest_paths(missing_manifest)
                raise AssertionError("missing manifest path should be a usage error")
            except UsageError as exc:
                assert "manifest path does not exist" in str(exc)
        finally:
            ROOT = original_root


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Find fused spaces next to numbers or CamelCase prose tokens."
    )
    parser.add_argument("paths", nargs="*", metavar="PATH")
    parser.add_argument("--md", action="store_true", help="scan Markdown instead of TeX")
    parser.add_argument("--json", action="store_true", help="write JSON findings")
    parser.add_argument("--classes", default="A,B,C", help="comma-separated classes")
    parser.add_argument("--include-d", action="store_true", help="include class D")
    parser.add_argument("--fix", action="store_true", help="prepare fixes for classes A-C")
    parser.add_argument("--apply", action="store_true", help="write fixes")
    parser.add_argument("--manifest", help="batch-intake JSON manifest")
    parser.add_argument("--selftest", action="store_true", help="run internal tests")
    args = parser.parse_args(argv)

    if args.selftest:
        _selftest()
        return 0

    try:
        selected = _selected_classes(args.classes, args.include_d)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if not args.paths and not args.manifest:
        parser.print_usage(sys.stderr)
        return 2

    if args.apply and not args.fix:
        print("--apply requires --fix", file=sys.stderr)
        return 2

    try:
        paths = _iter_paths(args.paths, md=args.md, manifest=args.manifest)
    except UsageError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"{args.manifest}: malformed manifest JSON: {exc}", file=sys.stderr)
        return 2
    except UnicodeDecodeError as exc:
        print(f"{args.manifest}: cannot read manifest as UTF-8: {exc}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"{args.manifest}: cannot read manifest: {exc}", file=sys.stderr)
        return 2

    all_json: list[dict[str, object]] = []
    any_remaining_abc = False
    suppressed_abc_count = 0
    refused = False

    for path in paths:
        try:
            text, all_hits = _scan_file(path, md=args.md)
        except (OSError, UnicodeDecodeError) as exc:
            print(f"{_path_for_output(path)}: cannot read: {exc}", file=sys.stderr)
            refused = True
            continue

        hits = [hit for hit in all_hits if hit.cls in selected]
        fixable_hits = [hit for hit in hits if hit.cls in {"A", "B", "C"}]

        if args.fix and fixable_hits:
            reason = _refusal_reason(path)
            if reason is not None:
                print(f"{_path_for_output(path)}: refusing --fix: {reason}", file=sys.stderr)
                refused = True
            elif args.apply:
                new_text = _fixed_text(text, fixable_hits)
                if new_text != text:
                    _write_atomic(path, new_text)
                _, all_hits = _scan_file(path, md=args.md)
                hits = [hit for hit in all_hits if hit.cls in selected]
                fixable_hits = [hit for hit in hits if hit.cls in {"A", "B", "C"}]

        if args.json:
            all_json.extend(_hit_to_json(path, hit) for hit in hits)
        else:
            _print_human(path, hits)

        remaining_abc = [hit for hit in all_hits if hit.cls in {"A", "B", "C"}]
        if remaining_abc:
            any_remaining_abc = True
            suppressed_abc_count += sum(
                1 for hit in remaining_abc if hit.cls not in selected
            )

    if args.json:
        print(json.dumps(all_json, ensure_ascii=False, indent=2))

    if suppressed_abc_count:
        print(
            f"{suppressed_abc_count} class A-C finding(s) remain outside --classes",
            file=sys.stderr,
        )

    if refused or any_remaining_abc:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

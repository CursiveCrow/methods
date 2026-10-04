#!/usr/bin/env python3
"""Generate the Part-1 symbol tables from the symbol registry.

Usage: python tools/symbols2tex.py [csv_path [out_path]]

Reads handbook/registry/symbols.csv (the single source of truth; header
``glyph,macro,role,scope,precedence,first_use,notes``) and writes
handbook/generated/symbols-tables.tex: one booktabs longtable per scope
group (Global first, then by part), with the same longtable head/foot
discipline as tools/csv2tex.py.  Cells are LaTeX-valued by convention (the
registry escapes its own specials), so no escaping happens here except that
the macro column is displayed through \\detokenize.

Exits nonzero on: duplicate glyph-role in overlapping scope (the same
glyph twice in overlapping scopes, whatever the roles -- same role means a
duplicate row, different roles a collision), malformed rows (wrong field
count, bad scope/precedence/first_use grammar, first_use outside scope),
and empty required cells (all columns but notes are required).

Scope, first-use, role-collision and descriptor validation is shared with the
handbook checker in symbol_registry.py. Legacy numeric scopes coexist with
uniquely resolved declaration regions and explicit named presentation bindings.
"""

import re
import sys
from pathlib import Path

try:
    from . import symbol_registry as registry
except ImportError:
    import symbol_registry as registry

ROOT = Path(__file__).resolve().parent.parent
CSV_DEFAULT = ROOT / "handbook" / "registry" / "symbols.csv"
OUT_DEFAULT = ROOT / "handbook" / "generated" / "symbols-tables.tex"
INDEX_OUT_DEFAULT = ROOT / "handbook" / "generated" / "symbol-index.tex"

HEADER = registry.HEADER
REQUIRED = registry.REQUIRED
POINT_RE = registry.POINT_RE
PREC_RE = registry.PREC_RE
FIRST_RE = registry.FIRST_RE
GLOBAL = registry.GLOBAL
point_interval = registry.point_interval
parse_scope = registry.parse_scope
overlap = registry.overlap
read_rows = registry.read_rows
collision_check = registry.collision_check


# Text cells are LaTeX-valued by convention, but registry rows written by authoring
# agents sometimes carry bare specials (u_i, ND_CPL, 2^h) outside math. Escape only
# bare _ # & % ^ outside \(..\), $..$ and \[..\] so data (and override role matching)
# stays unchanged while the generated tables stay valid LaTeX.
_MATH_RE = re.compile(r"\\\(.*?\\\)|\$[^$]*\$|\\\[.*?\\\]", re.S)
_SPECIAL_RE = re.compile(r"(?<!\\)([_#&%^])")


def text_cell(cell: str) -> str:
    def esc(chunk: str) -> str:
        return _SPECIAL_RE.sub(lambda m: "\\" + m.group(1) + ("{}" if m.group(1) == "^" else ""), chunk)
    out, pos = [], 0
    for m in _MATH_RE.finditer(cell):
        out.append(esc(cell[pos:m.start()]))
        out.append(m.group())
        pos = m.end()
    out.append(esc(cell[pos:]))
    return unicode_math("".join(out))


# Unicode math characters that pdflatex cannot typeset in text cells.
_UNICODE_MATH = {"Π": r"\ensuremath{\Pi}", "Σ": r"\ensuremath{\Sigma}",
                 "↦": r"\ensuremath{\mapsto}", "≃": r"\ensuremath{\simeq}",
                 "→": r"\ensuremath{\to}"}


def unicode_math(cell: str) -> str:
    return "".join(_UNICODE_MATH.get(ch, ch) for ch in cell)


def glyph_cell(glyph: str) -> str:
    """Glyphs are math-delimited by convention; render nonconforming rows safely."""
    if "\\(" in glyph or "$" in glyph or "\\[" in glyph:
        out = glyph
    elif "\\" in glyph or "_" in glyph or "^" in glyph:
        out = "\\ensuremath{" + glyph + "}"
    else:
        out = text_cell(glyph)
    # a cell starting with [ after a table row end would be read as \\[<dimen>]
    return "{}" + out if out.startswith("[") else out


def longtable(colspec: str, header: list[str], body_rows: list[list[str]],
              size: str = r"\scriptsize") -> str:
    # Same head/foot discipline as tools/csv2tex.py.
    head = " & ".join(rf"\textbf{{{h}}}" for h in header) + r" \\"
    lines = [
        r"\begingroup" + size + r"\setlength{\tabcolsep}{3pt}",
        rf"\begin{{longtable}}{{{colspec}}}",
        r"\toprule", head, r"\midrule", r"\endfirsthead",
        r"\toprule", head, r"\midrule", r"\endhead",
        r"\midrule\multicolumn{" + str(len(header)) +
        r"}{r}{\emph{continued}}\\\endfoot",
        r"\bottomrule\endlastfoot",
    ]
    for r in body_rows:
        lines.append(" & ".join(r) + r" \\")
    lines += [r"\end{longtable}", r"\endgroup"]
    return "\n".join(lines) + "\n"


def group_key(row):
    """Scope group: 'global' or the part number of the scope's lower end."""
    return row["_scope"].part


def group_title(key) -> str:
    return "Global scope" if key == "global" else f"Stable part P{key} scopes"


def macro_code(s: str) -> str:
    """Render registry macro text literally, with safe top-level breakpoints."""
    chunks = []
    current = []
    depth = 0
    for char in s:
        current.append(char)
        if char == "{":
            depth += 1
        elif char == "}":
            depth = max(0, depth - 1)
        if depth == 0 and char in ",/":
            chunks.append("".join(current))
            current = []
    if current:
        chunks.append("".join(current))
    rendered = r"\allowbreak".join(
        rf"\detokenize{{{chunk}}}" for chunk in chunks)
    return rf"\texttt{{{rendered}}}"


def render(rows) -> str:
    order = {"global": 0}
    groups: dict = {}
    for row in rows:
        groups.setdefault(group_key(row), []).append(row)
    keys = sorted(groups, key=lambda k: 0 if k == "global" else k)
    chunks = ["% GENERATED by tools/symbols2tex.py from "
              "handbook/registry/symbols.csv -- do not hand-edit.\n",
              r"\begin{landscape}" + "\n"]
    for key in keys:
        body = [[rf"\phantomsection\label{{entry:symbol-registry-{r['_line']:05d}}}{glyph_cell(r['glyph'])}",
                 macro_code(r["macro"]),
                 text_cell(r["role"]), registry.scope_tex(r), r["precedence"], registry.first_use_tex(r),
                 r"\thepage", text_cell(r["notes"])]
                for r in groups[key]]
        # Keep a scope heading with the first rows of its generated table.
        chunks.append(r"\Needspace{.4\textheight}" + "\n")
        chunks.append(rf"\subsection*{{{group_title(key)}}}" + "\n")
        chunks.append(longtable(
            r"@{}p{0.9in}p{1.3in}p{1.0in}p{0.5in}p{0.3in}p{0.4in}p{0.35in}p{1.65in}@{}",
            ["Glyph", "Macro", "Role", "Scope", "Prec./form", "First", "Reg. page", "Principal uses / notes"],
            body))
    chunks.append(r"\end{landscape}" + "\n")
    return "".join(chunks)


def render_index(rows) -> str:
    lines = [
        "% GENERATED by tools/symbols2tex.py -- do not hand-edit.\n",
    ]
    ordered = sorted(
        rows,
        key=lambda r: (re.sub(r"\\[A-Za-z]+|[^A-Za-z0-9]+", " ", r["glyph"]).casefold(), r["role"]),
    )
    for row in ordered:
        label = f"entry:symbol-registry-{row['_line']:05d}"
        lines.append(
            f"{glyph_cell(row['glyph'])} & {text_cell(row['role'])} & {registry.scope_tex(row)} & "
            rf"\hyperref[{label}]{{p.~\pageref{{{label}}}}} & "
            f"{registry.first_use_tex(row)} & {text_cell(row['notes'])} " + r" \\" + "\n"
        )
    return "".join(lines)


def main() -> None:
    csv_path = Path(sys.argv[1]) if len(sys.argv) > 1 else CSV_DEFAULT
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else OUT_DEFAULT
    rows, errors = read_rows(csv_path)
    errors += collision_check(rows)
    if errors:
        for e in errors:
            print(f"[symbols2tex] {e}", file=sys.stderr)
        print(f"[symbols2tex] FAILED: {len(errors)} error(s) in {csv_path}",
              file=sys.stderr)
        sys.exit(1)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write(render(rows))
    index_path = INDEX_OUT_DEFAULT if out_path == OUT_DEFAULT else out_path.with_name("symbol-index.tex")
    with index_path.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write(render_index(rows))
    groups = sorted({group_key(r) for r in rows},
                    key=lambda k: 0 if k == "global" else k)
    print(f"[symbols2tex] {len(rows)} rows -> {out_path} and {index_path} "
          f"({len(groups)} scope groups: "
          + ", ".join(group_title(k) for k in groups) + ")")


if __name__ == "__main__":
    main()

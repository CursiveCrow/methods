#!/usr/bin/env python3
"""Generate the Part-1 symbol tables from the symbol registry.

Usage: python tools/symbols2tex.py [--check | --selftest] [csv_path [out_path]]

Reads handbook/registry/symbols.csv (the single source of truth; header
``glyph,macro,role,scope,precedence,first_use,notes``) and writes
handbook/generated/symbols-tables.tex: one captioned booktabs longtable per
scope group (Global first, then by part), with the same longtable head/foot
discipline as tools/csv2tex.py plus a continued caption on every
continuation head.  It also writes symbol-index.tex, symbols-precedence.tex
(every row with a numeric rank, ordered by rank) and
symbols-letter-families.tex (rows and scopes per letter family) beside it.
--check writes nothing and exits nonzero when any of these files is missing
or differs from its rendering of the registry.  Cells are LaTeX-valued by convention (the
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
              size: str = r"\scriptsize", caption: str = "", label: str = "") -> str:
    # Same head/foot discipline as tools/csv2tex.py, plus a caption on the
    # first head and a continued caption on every continuation head.
    head = " & ".join(rf"\textbf{{{h}}}" for h in header) + r" \\"
    first_cap = ([rf"\caption{{{caption}}}" + (rf"\label{{{label}}}" if label else "") + r"\\"]
                 if caption else [])
    cont_cap = [rf"\caption[]{{{caption} (continued)}}\\"] if caption else []
    lines = [
        r"\begingroup" + size + r"\setlength{\tabcolsep}{3pt}",
        rf"\begin{{longtable}}{{{colspec}}}",
        *first_cap, r"\toprule", head, r"\midrule", r"\endfirsthead",
        *cont_cap, r"\toprule", head, r"\midrule", r"\endhead",
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


def table_label(key) -> str:
    return "tab:p01-classical-symbols" if key == "global" else f"tab:p01-w02-p01-026-symbols-p{key}"


def rank_key(prec: str):
    """Numeric operator ranks only; descriptors such as meta or n/a are not ranks."""
    try:
        return float(prec)
    except ValueError:
        return None


GENERATED = "% GENERATED by tools/symbols2tex.py from handbook/registry/symbols.csv -- do not hand-edit.\n"


def render_precedence(rows) -> str:
    """Every registry row carrying a numeric rank, ordered by rank then row."""
    ranked = sorted((r for r in rows if rank_key(r["precedence"]) is not None),
                    key=lambda r: (rank_key(r["precedence"]), r["_line"]))
    body = [[r["precedence"], glyph_cell(r["glyph"]), text_cell(r["role"]),
             registry.scope_tex(r)] for r in ranked]
    return GENERATED + longtable(
        r"@{}p{0.07\textwidth}p{0.30\textwidth}p{0.30\textwidth}p{0.27\textwidth}@{}",
        ["Rank", "Glyph", "Role", "Scope"], body, size=r"\small",
        caption=r"Registered operator ranks, generated from \texttt{registry/symbols.csv}",
        label="tab:p01-precedence")


# Letter families, matched on the glyph's TeX source; a glyph using several
# families is counted in each.
_GREEK_UP = r"Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega"
_GREEK_LOW = (r"alpha|beta|gamma|delta|epsilon|varepsilon|zeta|eta|theta|vartheta|iota|kappa|"
              r"lambda|mu|nu|xi|pi|varpi|rho|varrho|sigma|varsigma|tau|upsilon|phi|varphi|chi|psi|omega")
FAMILIES = [
    ("Greek lowercase", re.compile(rf"\\(?:{_GREEK_LOW})(?![A-Za-z])")),
    ("Greek uppercase", re.compile(rf"\\(?:{_GREEK_UP})(?![A-Za-z])")),
    ("Calligraphic", re.compile(r"\\mathcal(?![A-Za-z])")),
    ("Blackboard bold", re.compile(r"\\mathbb(?![A-Za-z])")),
    ("Fraktur", re.compile(r"\\mathfrak(?![A-Za-z])")),
    ("Sans serif", re.compile(r"\\mathsf(?![A-Za-z])")),
    ("Roman operator", re.compile(r"\\(?:operatorname|mathrm)(?![A-Za-z])")),
]


def render_families(rows) -> str:
    body = []
    for name, pattern in FAMILIES:
        members = [r for r in rows if pattern.search(r["glyph"])]
        examples = []
        for r in members:
            if r["glyph"] not in examples and len(examples) < 4:
                examples.append(r["glyph"])
        body.append([name, str(len(members)), str(len({r["scope"] for r in members})),
                     "; ".join(glyph_cell(g) for g in examples) or "none registered"])
    return GENERATED + longtable(
        r"@{}p{0.16\textwidth}p{0.08\textwidth}p{0.08\textwidth}p{0.58\textwidth}@{}",
        ["Family", "Rows", "Scopes", "First registered glyphs"], body, size=r"\small",
        caption=r"Letter families in the registry, generated from \texttt{registry/symbols.csv}",
        label="tab:p01-letter-families")


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
    chunks = [GENERATED, r"\begin{landscape}" + "\n"]
    for key in keys:
        body = [[rf"\phantomsection\label{{entry:symbol-registry-{r['_line']:05d}}}{glyph_cell(r['glyph'])}",
                 macro_code(r["macro"]),
                 text_cell(r["role"]), registry.scope_tex(r), r["precedence"], registry.first_use_tex(r),
                 r"\thepage", text_cell(r["notes"])]
                for r in groups[key]]
        # Keep a scope heading with the first rows of its generated table.
        chunks.append(r"\Needspace{.4\textheight}" + "\n")
        chunks.append(rf"\subsection*{{{group_title(key)}}}" + "\n")
        title = group_title(key)
        chunks.append(longtable(
            # Landscape line width is 541.4pt; these columns use 6.8in
            # (491.4pt) plus seven 6pt gaps, 533.4pt in all, so no header or
            # scope cell runs into its neighbour.
            r"@{}p{0.9in}p{1.2in}p{1.0in}p{0.75in}p{0.5in}p{0.45in}p{0.35in}p{1.65in}@{}",
            ["Glyph", "Macro", "Role", "Scope", "Prec. / form", "First", "Reg. page", "Principal uses / notes"],
            body, caption=f"Symbol register: {title[0].lower()}{title[1:]}",
            label=table_label(key)))
    chunks.append(r"\end{landscape}" + "\n")
    return "".join(chunks)


def expected_outputs(rows, out_path=OUT_DEFAULT) -> dict:
    """Every generated file and the text the registry renders for it."""
    index_path = INDEX_OUT_DEFAULT if out_path == OUT_DEFAULT else out_path.with_name("symbol-index.tex")
    return {out_path: render(rows), index_path: render_index(rows),
            out_path.with_name("symbols-precedence.tex"): render_precedence(rows),
            out_path.with_name("symbols-letter-families.tex"): render_families(rows)}


def stale_outputs(rows, out_path=OUT_DEFAULT) -> list:
    """Generated files that are missing or differ from the registry rendering."""
    stale = []
    for path, text in expected_outputs(rows, out_path).items():
        current = path.read_text(encoding="utf-8") if path.is_file() else None
        if current != text:
            stale.append(path)
    return stale


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


def _selftest() -> None:
    import tempfile
    scope = registry.Scope("global", interval=GLOBAL)
    rows = [
        {"glyph": r"\(\lor\)", "macro": r"\lor", "role": "disjunction", "scope": "global",
         "precedence": "5", "first_use": "P1.1", "notes": "", "_line": 2, "_scope": scope},
        {"glyph": r"\(\mathfrak A\)", "macro": r"\mathfrak A", "role": "algebra", "scope": "global",
         "precedence": "object", "first_use": "P1.1", "notes": "", "_line": 3, "_scope": scope},
        {"glyph": r"\(\neg\)", "macro": r"\neg", "role": "negation", "scope": "global",
         "precedence": "3", "first_use": "P1.1", "notes": "", "_line": 4, "_scope": scope},
    ]
    table = render(rows)
    assert r"\caption{Symbol register: global scope}\label{tab:p01-classical-symbols}\\" in table
    assert r"\caption[]{Symbol register: global scope (continued)}\\" in table
    assert table.index(r"\endfirsthead") < table.index("(continued)") < table.index(r"\endhead")
    prec = render_precedence(rows)
    assert r"\label{tab:p01-precedence}" in prec and "object" not in prec
    assert prec.index(r"\neg") < prec.index(r"\lor")
    fams = render_families(rows)
    assert r"Fraktur & 1 & 1 & \(\mathfrak A\)" in fams and "Sans serif & 0 & 0 & none registered" in fams
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "symbols-tables.tex"
        assert len(stale_outputs(rows, out)) == 4
        for path, text in expected_outputs(rows, out).items():
            path.write_text(text, encoding="utf-8", newline="\n")
        assert stale_outputs(rows, out) == []
        out.with_name("symbols-precedence.tex").write_text("% hand edit\n", encoding="utf-8")
        assert stale_outputs(rows, out) == [out.with_name("symbols-precedence.tex")]


def main() -> None:
    if "--selftest" in sys.argv[1:]:
        _selftest()
        print("[symbols2tex] selftest passed")
        return
    check = "--check" in sys.argv[1:]
    args = [a for a in sys.argv[1:] if a != "--check"]
    csv_path = Path(args[0]) if len(args) > 0 else CSV_DEFAULT
    out_path = Path(args[1]) if len(args) > 1 else OUT_DEFAULT
    rows, errors = read_rows(csv_path)
    errors += collision_check(rows)
    if errors:
        for e in errors:
            print(f"[symbols2tex] {e}", file=sys.stderr)
        print(f"[symbols2tex] FAILED: {len(errors)} error(s) in {csv_path}",
              file=sys.stderr)
        sys.exit(1)
    if check:
        stale = stale_outputs(rows, out_path)
        for path in stale:
            print(f"[symbols2tex] {path} diverges from {csv_path}; "
                  "rerun python -B tools/symbols2tex.py", file=sys.stderr)
        sys.exit(1 if stale else 0)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    outputs = expected_outputs(rows, out_path)
    for path, text in outputs.items():
        with path.open("w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    groups = sorted({group_key(r) for r in rows},
                    key=lambda k: 0 if k == "global" else k)
    print(f"[symbols2tex] {len(rows)} rows -> "
          + ", ".join(str(p) for p in outputs) + f" ({len(groups)} scope groups: "
          + ", ".join(group_title(k) for k in groups) + ")")


if __name__ == "__main__":
    main()

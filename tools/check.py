#!/usr/bin/env python3
"""Mechanical check suite for the formal-logic handbook campaign.

Usage:  python tools/check.py [--tree source|handbook] [--strict] [--root PATH]

--tree source (default) -- the v1.x manuscript checks, unchanged from Phase 0:
duplicate labels, dangling references, cite/bibitem mismatches, and -- in
--strict mode -- status-coverage below 100%, rule displays outside the
calculus registry, and zero-citation chapters.

--tree handbook -- the Phase-3 tree grammar per handbook/CONVENTIONS.md
("Checks" section), implemented by STATIC PARSING of handbook/**/*.tex plus
registry/symbols.csv and bib/handbook.bib.  No compile is required and the
tree may be half-built; every check degrades to a finding, never a crash.

Handbook failure categories (ALL hard under --strict; the three structural
ones -- duplicate-label, dangling-ref, bib-key -- fail even without --strict,
mirroring the source-tree behaviour; the rest print as findings):

  status-spec            malformed/missing status specs in hbtheorem/hblemma/
                         hbcorollary and \\entryadequacy/\\entrydecidability
  body-proof             proof environments under parts/
  rule-outside-registry  \\hbrule or \\frac-based rule shapes outside
                         registry/calculi/
  restoration-scope      inherited proof/rule exemption is not backed by an
                         exact, current provenance record and artifact
  annex-bidir            annex<->body bidirectionality (112=112 discipline)
  label-prefix           label-prefix taxonomy violations
  duplicate-label        duplicate labels (incl. environment-argument labels)
  dangling-ref           dangling \\ref/\\cref/\\pageref/\\hyperref/
                         \\entrycalculus/\\showcalculus targets
  glyph-collision        glyph with two roles in overlapping scopes
                         (registry/symbols.csv)
  entry-fields           system entry missing one or more required card fields
  zero-cite-chapter      non-stub chapters with zero citations
  bib-key                \\cite-family, \\entrysources, and cited= keys
                         missing from bib/handbook.bib
  fused-number           likely missing spaces next to numbers in handbook prose
  stub-marker            stub and TODO-style markers in body/proof content
  env-grammar            unparseable environment/macro argument lists
  symbols-csv            registry/symbols.csv structural problems
  missing-infra          registry/symbols.csv or bib/handbook.bib absent

Handbook metrics (always printed): stub count per part, status-form
distribution, entry-card field coverage, bib entry/stub counts.

Exit codes: 0 all hard checks passed; 1 hard failures; 2 usage/tree errors.
"""

import argparse
import csv
import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

RESULT_ENVS = ("theorem", "lemma", "corollary")
STATUS_MARKERS = (
    r"Status:\s*(complete proof|proof sketch|cited theorem)",
    r"\\begin\{proofplan\}",
    r"\\paragraph\{Proof sketch",
    r"\\paragraph\{Cited theorem",
)


def read_tree(tree: str) -> dict[Path, str]:
    base = ROOT / tree
    files = sorted(base.rglob("*.tex"))
    if not files:
        print(f"[check] no .tex files under {base}", file=sys.stderr)
        sys.exit(2)
    return {p: p.read_text(encoding="utf-8", errors="replace") for p in files}


def strip_comments(text: str) -> str:
    # Remove LaTeX comments (unescaped %) so commented-out code is not scanned.
    return re.sub(r"(?<!\\)%.*", "", text)


def strip_listings(text: str) -> str:
    # lstlisting bodies are verbatim; labels/cites inside them are not real.
    return re.sub(r"\\begin\{lstlisting\}.*?\\end\{lstlisting\}", "", text, flags=re.S)


def check_labels(texts: dict[Path, str]) -> tuple[list[str], set[str]]:
    errors: list[str] = []
    labels: Counter[str] = Counter()
    for path, raw in texts.items():
        body = strip_listings(strip_comments(raw))
        for m in re.finditer(r"\\label\{([^}]+)\}", body):
            labels[m.group(1)] += 1
    for name, n in labels.items():
        if n > 1:
            errors.append(f"duplicate label: {name} ({n} occurrences)")
    return errors, set(labels)


def check_refs(texts: dict[Path, str], labels: set[str]) -> list[str]:
    errors = []
    ref_cmds = r"\\(?:cref|Cref|ref|pageref|hyperref)\s*(?:\[([^\]]+)\]|\{([^}]+)\})"
    for path, raw in texts.items():
        body = strip_listings(strip_comments(raw))
        for m in re.finditer(ref_cmds, body):
            arg = m.group(1) or m.group(2)
            for target in arg.split(","):
                target = target.strip()
                if target and target not in labels:
                    errors.append(f"dangling reference: {target} ({path.name})")
    return errors


def check_bib(texts: dict[Path, str]) -> list[str]:
    errors = []
    cites: set[str] = set()
    bibitems: set[str] = set()
    for path, raw in texts.items():
        body = strip_listings(strip_comments(raw))
        for m in re.finditer(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}", body):
            cites.update(k.strip() for k in m.group(1).split(","))
        for m in re.finditer(r"\\bibitem\{([^}]+)\}", body):
            bibitems.add(m.group(1))
    if bibitems:
        for k in sorted(cites - bibitems):
            errors.append(f"cite key with no bibitem: {k}")
        for k in sorted(bibitems - cites):
            errors.append(f"uncited bibitem: {k}")
    return errors


def status_coverage(texts: dict[Path, str]) -> tuple[int, int]:
    """Count result environments and how many carry a status marker nearby."""
    total = covered = 0
    marker = re.compile("|".join(STATUS_MARKERS))
    for path, raw in texts.items():
        body = strip_listings(strip_comments(raw))
        for env in RESULT_ENVS:
            for m in re.finditer(rf"\\begin\{{{env}\}}", body):
                total += 1
                # A status marker within the following 2,500 characters is
                # treated as attached to this result (heuristic; the handbook
                # tree replaces this with a mandatory key on the environment).
                window = body[m.start() : m.start() + 2500]
                if marker.search(window):
                    covered += 1
    return covered, total


def rule_display_ban(texts: dict[Path, str]) -> list[str]:
    """Handbook tree only: inference-rule fractions belong in registry/calculi."""
    errors = []
    for path, raw in texts.items():
        rel = path.relative_to(ROOT).as_posix()
        if "registry/calculi" in rel:
            continue
        body = strip_listings(strip_comments(raw))
        if re.search(r"\\Rule\b|\\dfrac\{.*\\vdots", body):
            errors.append(f"rule display outside registry: {rel}")
    return errors


def zero_cite_chapters(texts: dict[Path, str]) -> list[str]:
    errors = []
    for path, raw in texts.items():
        body = strip_listings(strip_comments(raw))
        body_without_audit_wrapper = re.sub(
            r"\\chapter\*\s*\{Part\s+\d+\s+Audit Register\}",
            "",
            body,
        )
        if (re.search(r"\\chapter\b", body_without_audit_wrapper)
                and not re.search(r"\\cite", body)):
            errors.append(f"chapter file with zero citations: {path.name}")
    return errors


# =========================================================================
# Handbook tree (Phase 3): static grammar checks per handbook/CONVENTIONS.md
# =========================================================================

HB_LABEL_PREFIXES = ("part:", "sec:", "entry:", "def:", "thm:", "tab:",
                     "fig:", "sheet:", "rule:", "annex:")
HB_ID_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\Z")

# Theorem-class environments and the label prefix each one owns.
HB_STATUS_ENVS = {"hbtheorem": "thm:", "hblemma": "thm:", "hbcorollary": "thm:"}
HB_PLAIN_ENVS = {"hbdefinition": "def:", "hbconvention": "def:",
                 "hbmethod": "def:", "hbexample": "def:",
                 "hbwarning": "def:", "proofboundary": "def:"}
HB_THEOREM_CLASS = {**HB_STATUS_ENVS, **HB_PLAIN_ENVS}

HB_ENTRY_FIELDS_REQUIRED = ("entrylanguage", "entrysemantics", "entrycalculus",
                            "entryadequacy", "entrydecidability",
                            "entrycharacteristic", "entrysources")
HB_ENTRY_FIELDS_ALL = HB_ENTRY_FIELDS_REQUIRED + (
    "entryaliases", "entrytranslations", "entryalgebra")

HB_ENV_RE = re.compile(
    r"\\begin\{(" + "|".join(list(HB_THEOREM_CLASS) + ["systementry", "annexitem"]) + r")\}")
HB_REF_RE = re.compile(
    r"\\(?:cref|Cref|ref|pageref|hyperref)\*?\s*(?:\[([^\]]+)\]|\{([^}]+)\})")
HB_CITE_RE = re.compile(
    r"\\(?:cite|Cite|autocite|Autocite|textcite|Textcite|parencite|Parencite)\*?"
    r"(?:\[[^\]]*\]){0,2}\{([^{}]+)\}")
# Proof-tree commands that draw inference rules (banned outside the registry).
HB_RULECMD_RE = re.compile(
    r"\\(Rule|infer(?:rule)?\*?|prftree|AxiomC|UnaryInfC|BinaryInfC|TrinaryInfC)\b")
HB_FRAC_RE = re.compile(r"\\[dtc]?frac\b")
HB_SEQ_MARK_RE = re.compile(r"\\(?:vdash|Vdash|vdots|Rightarrow|Longrightarrow)\b")
HB_RESTORATION_SCOPE = "inheritedrestorationscope"
HB_RESTORATION_ID_RE = re.compile(r"(?:PRE|SRC|CTL|SEP)-\d{5}-\d{5}\Z")
HB_RESTORATION_SCOPE_TOKEN_RE = re.compile(
    rf"\\(begin|end)\{{{HB_RESTORATION_SCOPE}\}}"
)
HB_INPUT_RE = re.compile(
    r"\\(?:input|include)\s*(?:\{([^{}]+)\}|([^\s%{}]+))"
)
HB_RESTORATION_ARTIFACT_RE = re.compile(
    r"restoration/inherited-\d{5}-\d{5}\.tex\Z"
)
# Necessity: exact source lines 6061, 7267, 7722, 7821, and 15506--15618 use
# convention, proofplan, and solution, and no existing guarded source
# environment states those forms exactly.  Definition: convention is the
# optional-title shared-counter source form; proofplan is the paragraph headed
# ``Proof sketch.''; solution is the paragraph headed ``Solution.'' and closed
# by a right-aligned square.  Standing: all three are source-rendering control
# syntax, not mathematical statement families or review results.
# Nonredundancy: editorial conventions and proof apparatus carry different
# headings, labels, counters, ownership, or standing.  Use: this scan rejects
# all three spellings outside validated restoration artifacts, including the
# two Part IV proofplans and five qualifying-examination solutions;
# handbook.sty supplies the matching TeX guards.
HB_SOURCE_ENV_RE = re.compile(
    r"\\begin\s*\{\s*"
    r"(definition|warning|remark|lemma|method|theorem|corollary|example|exercise|convention|proofplan|solution|lstlisting)"
    r"\s*\}"
)
# Necessity: exact source chapters use guarded command spellings that cannot be
# byte-rewritten to editorial notation.  Definition: this expression enumerates
# exactly the source-only command tokens whose meanings handbook.sty supplies
# inside validated inherited scopes.  Standing: it is metalinguistic scanner
# control, not a mathematical vocabulary or admission result.  Nonredundancy:
# the TeX guards fail at compile time, while this independent source scan also
# catches unrouted editorial files before a build; globally registered \topv is
# deliberately excluded.  Use: restoration-scope tests exercise every listed
# token, including the modal \K, \Sfour, and \Sfive spellings, inside and outside
# scope and reject omissions or unguarded additions.
HB_SOURCE_COMMAND_RE = re.compile(
    r"(?<!\\)(?:\\\\)*\\(Pow|set|tuple|rng|Mod|Fm|length|restr|rank|side|UNSAT|SAT|NP|ZFC|ZF|Z|"
    r"Prop|CPL|IPL|Sfour|Sfive|K|Sub|True|False|ND|LK|LJ|notentails|Var|Term|Sent|arity|Meta|Th|Cn|FOL|Q|R)(?![A-Za-z@])"
)
HB_STUB_MARKER_RE = re.compile(
    r"\\hbstub\b|\b(?:TODO|FIXME|TBD)\b|"
    r"\bleft\s+to\s+the\s+reader\b|"
    r"\bomitted\s+for\s+brevity\b|"
    r"\bstandard\s+argument\b|"
    r"\broutine\s+verification\b|"
    r"\bsimilarly\s+for\s+the\s+remaining\s+cases\b|"
    r"\bthe\s+remaining\s+cases\s+are\s+similar\b|"
    r"\bdetails\s+omitted\b",
    re.I,
)

HB_CATEGORY_ORDER = (
    "status-spec", "body-proof", "rule-outside-registry", "annex-bidir",
    "restoration-scope",
    "label-prefix", "duplicate-label", "dangling-ref", "pending-inherited-ref",
    "glyph-collision",
    "entry-fields", "zero-cite-chapter", "bib-key", "fused-number",
    "stub-marker", "env-grammar", "symbols-csv", "missing-infra",
)
HB_ALWAYS_HARD = {
    "duplicate-label", "dangling-ref", "pending-inherited-ref", "bib-key"
}


def strip_verbatims(text: str) -> str:
    """Blank verbatim-like bodies while retaining environment markers."""
    def repl(m: re.Match) -> str:
        name = m.group(1)
        return (
            rf"\begin{{{name}}}"
            + "\n" * m.group(0).count("\n")
            + rf"\end{{{name}}}"
        )
    return re.sub(r"\\begin\{(lstlisting|verbatim)\}.*?\\end\{\1\}",
                  repl, text, flags=re.S)


def scan_braced_args(text: str, pos: int, count: int) -> tuple[list[str], int]:
    """Read up to `count` {...} groups (nesting-aware) starting at `pos`.

    Skips intervening whitespace.  Returns (args, end_pos); fewer than
    `count` args means the source is malformed at that point.
    """
    args: list[str] = []
    n = len(text)
    while len(args) < count:
        while pos < n and text[pos] in " \t\r\n":
            pos += 1
        if pos >= n or text[pos] != "{":
            return args, pos
        depth = 1
        i = pos + 1
        start = i
        while i < n and depth:
            c = text[i]
            if c == "\\" and i + 1 < n:
                i += 2
                continue
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            i += 1
        if depth:                       # unbalanced braces: bail out
            return args, pos
        args.append(text[start:i - 1])
        pos = i
    return args, pos


def _normalized_tex_input(raw: str) -> str | None:
    """Return a repository-style TeX input path, or None for a dynamic path."""
    value = raw.strip().replace("\\", "/")
    while value.startswith("./"):
        value = value[2:]
    if (not value or value.startswith("/") or re.match(r"[A-Za-z]:", value)
            or any(part in ("", ".", "..") for part in value.split("/"))):
        return None
    if not value.endswith(".tex"):
        value += ".tex"
    return value


# Necessity: the tree-wide identity scan cannot distinguish an unrouted file
# retained as migration evidence from a live reader definition without an
# explicit, mutation-sensitive classification.
# Definition: HB_RETAINED_UNREACHABLE_READER_FILES maps exactly sixty-five retained
# repository-relative TeX paths to their exact byte digests.  The check is
# activated only when either exact-source split or one of its live successors
# exists; a mapped path is then omitted from reader identity
# harvesting only when its digest matches and no static input route from
# main.tex reaches it.
# Standing: this is a metalinguistic checker abbreviation, not a TeX construct,
# logical relation, source disposition, or publication-review result.
# Nonredundancy: ordinary route reachability proves only that a file is not
# currently included, while this classification additionally pins which exact
# bytes may receive that treatment and fails closed on either content or route
# drift.
# Use: check_handbook consumes the result before harvesting labels, references,
# result statuses, annex links, citations, and chapter metrics, preventing the
# sixty-five preserved combined drafts and drivers from duplicating their split live successors.
HB_RETAINED_UNREACHABLE_READER_FILES = {
    "parts/p02/propositional-syntax-semantics.tex":
        "94338430c4e87cf1b9228274b15adbac052c704eb0b4e81a48b4587a59217b56",
    "annex/p02/propositional-syntax-semantics.tex":
        "6f6546466de5950df28e1f1450fd6087608a60d9ddccf2f1d16f2563616d69fb",
    "parts/p02/propositional-calculi.tex":
        "b8acd5d657b2718252ce31cd892c1aac68200a271ecd103af8989e2d66fc73ab",
    "annex/p02/propositional-calculi.tex":
        "9ea96bfc0d8d5acf8895fcf2dcfcf21ad12150641ed122c65bc1bb06304cc5c0",
    "parts/p02/propositional-metatheory.tex":
        "db4e2b81d8c319e42df4c82768f95d91818488360194ed892e9e8f2640170e62",
    "annex/p02/propositional-metatheory.tex":
        "a958662006df1cf3956731ca63e1c5d9f327eb85596415ec1f7e64efdae1c71e",
    "parts/p02/first-order-syntax-semantics.tex":
        "5a737c791bf8e24a98f8bdc97c75b7257ac33cd9596d535e3fa5dffd96bd83d4",
    "annex/p02/first-order-syntax-semantics.tex":
        "8f0cf70d498925661e03430b12a611836f80f9a31550cc34022a11fbfcd8492e",
    "parts/p02/first-order-calculi.tex":
        "ac38cba6e24cc9adcc6d95b1ddc8f4e45ea803fa486b7d642accdba2b5f52c1f",
    "annex/p02/first-order-calculi.tex":
        "8268564a38345e1299de69d5ac8226cb5d13b8e663f26b342099bcf29d830356",
    "parts/p02/first-order-completeness.tex":
        "fa0f9c6075cb85bb79dd280f254355ac297d415eddfc21d8c70e3e14de94ab95",
    "annex/p02/first-order-completeness.tex":
        "f7b25a11112feebfd04a88a670ffbc6267e61d9adcec4d07498668ec692eaef0",
    "parts/p02/first-order-normal-forms.tex":
        "4e4594b277c315f658a0f2e586dc3139aed3d0abedfe29132de168ab5c54a8ba",
    "annex/p02/first-order-normal-forms.tex":
        "d300a9a54a76d21abb5c5300198ab1404a2d26e5148059f51ef85154b9e8e237",
    "parts/p02/first-order-resolution.tex":
        "f0d6c96e4215241247595e03432166017b9605b900fe14e2b78f0f3ab8c466c0",
    "annex/p02/first-order-resolution.tex":
        "2fabb80918d495f4f419b479d319bd90875ab77996d4a53fe82293e7f091f19c",
    "parts/p03/maps-elementarity.tex":
        "2c3b31b2905b6ba4c11ecdea119edce02960e8fa3e85525cbe2d6b93a069c7ac",
    "annex/p03/maps-elementarity.tex":
        "81a912fb519d811c1a517b764e4e716b6687e16c2e1986218e6b6b7f6ebd67b4",
    "parts/p03/types-ultraproducts.tex":
        "fd8eb5788fd460ef6555df01692597c9649badabbb17f366d43ef1575e263ecf",
    "annex/p03/types-ultraproducts.tex":
        "7363e0df7e9afdccdb557de9c1eed7702c854083aba6b21b5c90f5c17523d385",
    "parts/p03/qe-categoricity-games.tex":
        "59b274b3d0f0f40f9d9f7c138d173044150082d222a30829587702caee2cd551",
    "annex/p03/qe-categoricity-games.tex":
        "89a7bac0248d521eba8c8c321ed79c1dc587b40f1d50bd1b628342f7a8a5392d",
    "parts/p04/machines-effective-procedures.tex":
        "745c470a05c7fde4f66670f6c81ae69bf6674e1c40f269a6de5fa169795d959b",
    "annex/p04/machines-effective-procedures.tex":
        "1fa574674deb89dcc7fa9b4976c928298f39921a6aa6117a4ad79edbd91988bd",
    "parts/p04/universal-reductions.tex":
        "46ebae43bd661d65951dd4a5c55960d36d586146ab6c758b21672ed0b6c84c0c",
    "annex/p04/universal-reductions.tex":
        "c9b4dbe85da7ac62efc36def8cdce445ac5a20a8c10d1cbd492e78f0f4621880",
    "parts/p04/decision-problems-and-arithmetical-hierarchy.tex":
        "7e7a5082c59955a9b539173fdaf105197aaef9eedbeb9f4bcceeea250df7eb4e",
    "annex/p04/decision-problems-and-arithmetical-hierarchy.tex":
        "e897b6d4357d7d421a886fc5274d90a6c6801d8ef3b8a67e93dc40bf9b5e968f",
    "parts/p04/degrees-and-priority.tex":
        "cc4d58a3fcac3cf80232c40612ba0b408ec962a7cd112444b210b92fcc8cca82",
    "annex/p04/degrees-and-priority.tex":
        "4f314dcfacd1b097a88b63f1207382b4f3bb69e18b32b4a7dd949267304b16e5",
    "parts/p05/diagonalization.tex":
        "63dc7704391e0cfd6c9bfa07465b0dfa905112f612f57a0b35932f2810c9dfb4",
    "parts/p05/models-and-interpretability.tex":
        "dce02758d3950e0eeb3a1b5e621baec58eb7552294ed5ec5a843d9f0ab907a9e",
    "parts/p05/provability-truth.tex":
        "1ce4fca01f2e371d78c6b41a8e6dcf909c700ad959a0c0de0d2f932ccc697ac6",
    "annex/p05.tex":
        "aba296def30934f250036c7f2ea10c1b6cf36090ea698788a06df22423c8c4ae",
    "annex/p05/depth-completion.tex":
        "4325b14b8ed8f7487eef9d51e887b862619bfbcc7059fd7dd546619c2d2524c8",
    "parts/p06/axioms-hierarchy.tex":
        "a6c38c9617f69a66076f56050b19d8ee04ec16ebe38cb92fe202a2dd53982fb2",
    "annex/p06/axioms-hierarchy.tex":
        "9d78bdea96c760449b5986dfe69aadafb48ceea3483b82e59b82c592715d8f1b",
    "parts/p06/cardinals-choice.tex":
        "c8fd192939632620a7665044e32fdf781928d31f70f478e94705259011613c7b",
    "parts/p06/cardinal-arithmetic.tex":
        "9b0f95b04f9054cf877f874dbb6714bf811539375025e70db0e80749985e3c49",
    "annex/p06/cardinals-choice.tex":
        "0a41cef98a376cd6dbe377771c4a173f7153fb229dbc14fcb2307a231d00e584",
    "parts/p06/constructibility-forcing.tex":
        "aa07af766e41f5e34a76385ff3118110caf6ab5204ba4e1add8bf1179f315d03",
    "annex/p06/constructibility-forcing.tex":
        "53a353652500bf77b24ec0f4a1c99d9946a47cc65c8a5be5a03f53684e414ff6",
    "parts/p06/forcing-variants.tex":
        "5aea34290ea15571ef42051696c1d2c1e29bca4bbdc9c9a03762f7cce98932aa",
    "annex/p06.tex":
        "8facb6cf86dd63b60febce1d33d35f10db2e430603e3baf6d889df20410d1927",
    "parts/p07/calculi-and-derivability.tex":
        "a9a44a5b20aed82c412894750808c363c588d5b18b3695e3f7f4cf0af23c2ffd",
    "parts/p07/cut-elimination-and-interpolation.tex":
        "02d5b4791bb9392f0e86095559a7539d4ad75c05abad5729f0f3e36a078fc8f1",
    "annex/p07/calculi-and-cut-elimination.tex":
        "ec9cbe318f783a3dbf343bf065dd56a8a39ab51b87b0f11b1fae11f777923fd7",
    "annex/p07/interpolation.tex":
        "257a3c6df73e5f7011c119fc1ffbbb4d4312ce03dd119bb06eb7bdf6272fd97f",
    "parts/p07/normalization-and-curry-howard.tex":
        "6aca2a57c14b65dce494f358ffd9116b19a765536e5a7f70bc2ce640fd120be0",
    "annex/p07/normalization.tex":
        "1f2d4449f7afb5d79e3551464cb050d9c396df1b9e561730221b3511e7a4f951",
    "parts/p07/arithmetic-proof-theory.tex":
        "f25320abf78d1ee9465126b4a81ee261af2cabfc1e05ad9325119e1b593992f7",
    "annex/p07/arithmetic-proof-theory.tex":
        "db6ec58dda1c4b887595fda70fe5f9c51b27147a338bf185a63061bc9cae6149",
    "parts/p02/second-and-higher-order-logic.tex":
        "72551e0b9ef0b8051f15a5efbde7107b147607f314a1f411641157134cc60ca0",
    "annex/p02/higher-order.tex":
        "456ee135aa668118cd9184deabdb02ba02947a4ef9451045823138cb96303dc9",
    "parts/p08/intuitionistic-and-intermediate.tex":
        "aac30a07b44a9564662848fa39b8880ee4dad77673761a4402b2e1aa0fb30dd3",
    "annex/p08/intuitionistic-and-intermediate.tex":
        "e758da33c6f167e8eab621b2e151fd003269a1c9e54e41ca7c624e06bc9aed8a",
    "parts/p08/modal-logics.tex":
        "b2f93697504b9b494fd015783683e0de970cc77fbfa3767590da6cb8594acf46",
    "annex/p08/modal-logics.tex":
        "115fa5aaf61cf3e4c89e86d6cfe25a188f9740c36d2d17d3651899063397ce8d",
    "parts/p08/temporal-dynamic-epistemic.tex":
        "14403d7c48bc1569d2505ad031abb4ff2f923d0b284fd62375c154a714fd32e4",
    "annex/p08/temporal-dynamic-epistemic.tex":
        "933b2a29ecc9a0b851abd20d9b4245158cc6f6ef9ed578ce5be01da2c3c5ed79",
    "parts/p08/many-valued-and-fuzzy.tex":
        "717904583f7f888fc716f7fc29f88c411211a5c2fd333184c70235c0dd76f1da",
    "annex/p08/many-valued-and-fuzzy.tex":
        "c15c354b5ee52ae0fa55acceb61b2a314bca9509d871120aacb54e194eb11bfc",
    "parts/p08/substructural.tex":
        "2217b18d6e9c84748a94952a6b9d9977a1bbe3d7dbbf3a9851e7f87c02673a61",
    "annex/p08/substructural.tex":
        "3d86ce418247e23de00a07aa3bb6257b74e239dd397c374268ef75dd8b565126",
    "parts/p12/formal-workflow.tex":
        "b5d74d38ca0fa5756e3f36a6cd10200a5b4d082c01eb0dce9052e628a8d1af36",
}


def _hb_static_input_reachability(bodies: dict[str, str]) -> set[str]:
    """Return exact TeX files reached by literal inputs from main.tex."""
    reached: set[str] = set()
    active: set[str] = set()

    def visit(relative: str) -> None:
        if relative in reached or relative in active:
            return
        active.add(relative)
        reached.add(relative)
        for match in HB_INPUT_RE.finditer(bodies.get(relative, "")):
            target = _normalized_tex_input(match.group(1) or match.group(2))
            if target in bodies:
                visit(target)
        active.remove(relative)

    if "main.tex" in bodies:
        visit("main.tex")
    return reached


def _hb_retained_unreachable_reader_files(
    base: Path, bodies: dict[str, str], data: "_HBData"
) -> set[str]:
    """Verify and return the exact retained files excluded from reader data."""
    activation_paths = {
        "restoration/scope-SRC-01649-01660.tex",
        "restoration/scope-SRC-02187-02192.tex",
        "parts/p02/propositional-hilbert-tableaux.tex",
        "annex/p02/propositional-hilbert.tex",
        "restoration/scope-SRC-02451-02544.tex",
        "parts/p02/propositional-metatheory-supplement.tex",
        "annex/p02/propositional-metatheory-supplement.tex",
        "restoration/scope-SRC-03022-03037.tex",
        "restoration/scope-SRC-06049-06069.tex",
        "restoration/scope-SRC-07494-07505.tex",
        "restoration/scope-SRC-09080-09098.tex",
        "restoration/scope-SRC-10060-10088.tex",
        "restoration/scope-SRC-11354-11413.tex",
        "restoration/scope-SRC-12249-12261.tex",
        "restoration/scope-SRC-12970-12988.tex",
        "restoration/scope-SRC-13201-13213.tex",
        "restoration/scope-SRC-13584-13613.tex",
        "restoration/scope-SRC-14095-14146.tex",
    }
    if not activation_paths.intersection(bodies):
        return set()
    reached = _hb_static_input_reachability(bodies)
    verified: set[str] = set()
    for relative, expected_hash in HB_RETAINED_UNREACHABLE_READER_FILES.items():
        path = base / relative
        if relative not in bodies or not path.is_file():
            data.flag(
                "duplicate-label",
                f"retained reader-history file is missing; no identity exclusion "
                f"is authorized ({relative})",
            )
            continue
        if relative in reached:
            data.flag(
                "duplicate-label",
                f"retained reader-history file is reachable from main.tex; no "
                f"identity exclusion is authorized ({relative})",
            )
            continue
        try:
            actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        except OSError as exc:
            data.flag(
                "duplicate-label",
                f"retained reader-history file is unreadable; no identity "
                f"exclusion is authorized ({relative}: {exc})",
            )
            continue
        if actual_hash != expected_hash:
            data.flag(
                "duplicate-label",
                f"retained reader-history file bytes changed; no identity "
                f"exclusion is authorized ({relative})",
            )
            continue
        verified.add(relative)
    return verified


def _has_restricted_restoration_construct(body: str) -> bool:
    """Whether exact material needs the proof/rule restoration scope."""
    if re.search(r"\\begin\{proof\}", body):
        return True
    if HB_SOURCE_ENV_RE.search(body):
        return True
    if re.search(r"\\hbrule\b", body) or HB_RULECMD_RE.search(body):
        return True
    for match in HB_FRAC_RE.finditer(body):
        if HB_SEQ_MARK_RE.search(body[match.end():match.end() + 240]):
            return True
    return False


def _hb_detokenize_argument_spans(body: str) -> list[tuple[int, int]]:
    r"""Return content spans of balanced, braced ``\detokenize`` arguments.

    Commands inside those exact argument tokens are displayed as characters,
    not executed.  An unbraced or unbalanced occurrence authorizes nothing.
    """
    spans: list[tuple[int, int]] = []
    for match in re.finditer(r"\\detokenize(?![A-Za-z@])", body):
        pos = match.end()
        while pos < len(body) and body[pos] in " \t\r\n":
            pos += 1
        if pos >= len(body) or body[pos] != "{":
            continue
        depth = 1
        index = pos + 1
        while index < len(body) and depth:
            if body[index] == "\\" and index + 1 < len(body):
                index += 2
                continue
            if body[index] == "{":
                depth += 1
            elif body[index] == "}":
                depth -= 1
            index += 1
        if depth == 0:
            spans.append((pos + 1, index - 1))
    return spans


def _hb_validate_restoration_scopes(
    base: Path, bodies: dict[str, str], data: "_HBData"
) -> set[str]:
    """Validate provenance-gated wrappers and return authorized artifacts.

    A wrapper is deliberately incapable of carrying editorial material: its
    single scope body must be exactly one input of the artifact named by the
    validated inherited-restoration record. Versions 1--3 retain exact source
    equality; version 4 authorizes only the recorded corrected-reader candidate.
    This mechanical syntax authorization is not any independent admission gate.
    """
    try:
        import check_inherited_restoration as exact_checker
    except ImportError as exc:  # pragma: no cover - a broken installation
        data.flag("restoration-scope",
                  f"cannot import exact restoration checker: {exc}")
        return set()

    repo_root = base.parent
    provenance_root = repo_root / "spec" / "provenance"
    authorized: set[str] = set()
    authorized_ids: set[str] = set()
    authorized_wrappers: set[str] = set()
    wrapper_artifacts: dict[str, str] = {}

    for rel, body in sorted(bodies.items()):
        tokens = list(HB_RESTORATION_SCOPE_TOKEN_RE.finditer(body))
        is_scope_wrapper = rel.startswith("restoration/scope-")
        if not tokens:
            if is_scope_wrapper:
                data.flag("restoration-scope",
                          f"scope wrapper has no {HB_RESTORATION_SCOPE} "
                          f"environment ({rel})")
            continue
        if not rel.startswith("restoration/"):
            for token in tokens:
                data.flag(
                    "restoration-scope",
                    f"{HB_RESTORATION_SCOPE} may occur only under "
                    f"handbook/restoration ({rel}:{_line(body, token.start())})",
                )
            continue

        stack: list[tuple[re.Match[str], str, int]] = []
        pairs: list[tuple[re.Match[str], str, int, re.Match[str]]] = []
        structurally_valid = True
        for token in tokens:
            if token.group(1) == "begin":
                args, args_end = scan_braced_args(body, token.end(), 1)
                provenance_id = args[0].strip() if args else ""
                if len(args) != 1 or not HB_RESTORATION_ID_RE.fullmatch(
                        provenance_id):
                    data.flag(
                        "restoration-scope",
                        f"scope requires one exact provenance id "
                        f"({rel}:{_line(body, token.start())})",
                    )
                    structurally_valid = False
                if stack:
                    data.flag(
                        "restoration-scope",
                        f"nested restoration scope "
                        f"({rel}:{_line(body, token.start())})",
                    )
                    structurally_valid = False
                stack.append((token, provenance_id, args_end))
            elif not stack:
                data.flag(
                    "restoration-scope",
                    f"unbalanced restoration scope end "
                    f"({rel}:{_line(body, token.start())})",
                )
                structurally_valid = False
            else:
                begin, provenance_id, args_end = stack.pop()
                pairs.append((begin, provenance_id, args_end, token))
        for begin, _provenance_id, _args_end in stack:
            data.flag(
                "restoration-scope",
                f"unbalanced restoration scope begin "
                f"({rel}:{_line(body, begin.start())})",
            )
            structurally_valid = False
        if not structurally_valid:
            continue
        if len(pairs) != 1:
            data.flag("restoration-scope",
                      f"wrapper must contain exactly one restoration scope "
                      f"({rel})")
            continue

        begin, provenance_id, args_end, end = pairs[0]
        expected_wrapper = f"restoration/scope-{provenance_id}.tex"
        if rel != expected_wrapper:
            data.flag(
                "restoration-scope",
                f"scope {provenance_id} must be in {expected_wrapper}, not {rel}",
            )
            continue
        if (body[:begin.start()] + body[end.end():]).strip():
            data.flag(
                "restoration-scope",
                f"wrapper contains material outside its scope ({rel})",
            )
            continue
        scope_body = body[args_end:end.start()]
        input_match = re.fullmatch(
            r"\s*\\input\s*\{([^{}]+)\}\s*", scope_body
        )
        if not input_match:
            data.flag(
                "restoration-scope",
                f"scope body must be exactly one braced artifact input ({rel})",
            )
            continue
        artifact_input = _normalized_tex_input(input_match.group(1))
        if artifact_input is None or not HB_RESTORATION_ARTIFACT_RE.fullmatch(
                artifact_input):
            data.flag(
                "restoration-scope",
                f"scope input is not a locator-bound restoration artifact "
                f"({rel})",
            )
            continue

        record_path = provenance_root / f"{provenance_id}.json"
        try:
            record = exact_checker.load_json(record_path)
            verified_id = exact_checker.validate_record(
                record, record_path, repo_root
            )
        except Exception as exc:  # checker exceptions become closed findings
            data.flag(
                "restoration-scope",
                f"{provenance_id} record/artifact is missing or stale: {exc} "
                f"({rel})",
            )
            continue
        record_artifact = _normalized_tex_input(
            record["restoration_artifact"]["path"]
        )
        if record_artifact and record_artifact.startswith("handbook/"):
            record_artifact = record_artifact.removeprefix("handbook/")
        if verified_id != provenance_id or record_artifact != artifact_input:
            data.flag(
                "restoration-scope",
                f"{provenance_id} record artifact {record_artifact!r} does not "
                f"match wrapper input {artifact_input!r} ({rel})",
            )
            continue
        if record["schema_version"] == 4:
            candidate_raw = (repo_root / record["restoration_artifact"]["path"]).read_bytes()
            candidate_text = candidate_raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
            if (exact_checker.sha256(candidate_raw) != record["restoration_artifact"]["sha256"]
                    or bodies.get(artifact_input) != strip_verbatims(strip_comments(candidate_text))):
                data.flag("restoration-scope", f"corrected reader changed during scope validation ({artifact_input})")
                continue
        if provenance_id in authorized_ids or artifact_input in authorized:
            data.flag(
                "restoration-scope",
                f"duplicate scope authorization for {provenance_id} "
                f"({rel})",
            )
            continue
        authorized_ids.add(provenance_id)
        authorized.add(artifact_input)
        authorized_wrappers.add(rel)
        wrapper_artifacts[rel] = artifact_input
        data.authorized_restorations[artifact_input] = {
            "provenance_id": provenance_id,
            "governed_end_line": int(record["source_locator"]["end_line"]),
            "reachable_once": False,
            "authorization_kind": "corrected-reader" if record["schema_version"] == 4 else "exact-capture",
            "source_line_map": exact_checker.reader_source_line_map(record),
        }

    # Necessity: source preamble and backmatter controls must remain byte-exact
    # authority evidence, but executing them in the integrated driver would
    # duplicate the document preamble, bibliography, index, or terminator.
    # Definition: a reconstruction evidence artifact is an exact
    # restoration/inherited-*.tex file whose validated record has disposition
    # full reconstruction and names a different integrated destination.
    # Standing: this is checker authorization for retained non-executable
    # evidence, not source admission, reader content, or a review result.
    # Nonredundancy: a routed wrapper proves direct execution; this case instead
    # proves exact retention plus an explicit reconstructed destination.
    # Use: the preamble and final backmatter records use this branch, while any
    # unrecorded artifact or direct input remains rejected below.
    for rel in sorted(bodies):
        if rel in authorized or not HB_RESTORATION_ARTIFACT_RE.fullmatch(rel):
            continue
        locator = rel.removeprefix("restoration/inherited-").removesuffix(".tex")
        records = list(provenance_root.glob(f"*-{locator}.json"))
        if len(records) != 1:
            continue
        record_path = records[0]
        try:
            record = exact_checker.load_json(record_path)
            provenance_id = exact_checker.validate_record(
                record, record_path, repo_root
            )
        except Exception:
            continue
        record_artifact = _normalized_tex_input(
            record["restoration_artifact"]["path"]
        )
        if record_artifact and record_artifact.startswith("handbook/"):
            record_artifact = record_artifact.removeprefix("handbook/")
        destination = _normalized_tex_input(record["handbook_destination"]["file"])
        if destination and destination.startswith("handbook/"):
            destination = destination.removeprefix("handbook/")
        if (
            record["disposition"] == "full reconstruction"
            and record_artifact == rel
            and destination != rel
        ):
            authorized.add(rel)
            data.authorized_restorations[rel] = {
                "provenance_id": provenance_id,
                "governed_end_line": int(record["source_locator"]["end_line"]),
                "reachable_once": False,
            }
    # Every inherited artifact requires one exact provenance record and one
    # validated wrapper.  Content shape cannot substitute for source identity:
    # an unrecorded prose, formula, example, or control-syntax fragment is as
    # unauthorized as an unrecorded proof or rule display.
    for rel, body in sorted(bodies.items()):
        for match in HB_INPUT_RE.finditer(body):
            target = _normalized_tex_input(match.group(1) or match.group(2))
            if target is None or not HB_RESTORATION_ARTIFACT_RE.fullmatch(target):
                continue
            # The validated wrapper's input has already been checked exactly.
            if rel.startswith("restoration/scope-") and target in authorized:
                continue
            locator = target.removeprefix("restoration/inherited-").removesuffix(
                ".tex"
            )
            records = list(provenance_root.glob(f"*-{locator}.json"))
            if records:
                data.flag(
                    "restoration-scope",
                    f"provenance-recorded artifact {target} is included outside "
                    f"its validated scope wrapper "
                    f"({rel}:{_line(body, match.start())})",
                )
                continue
            data.flag(
                "restoration-scope",
                f"unrecorded restoration artifact {target} is included outside "
                f"a validated provenance scope "
                f"({rel}:{_line(body, match.start())})",
            )

    # A valid wrapper that is never reached by the handbook driver is not an
    # integrated restoration.  Count literal static input paths from main.tex;
    # zero routes and duplicate routes both fail closed.  Cycles contribute no
    # route and cannot make an unreachable wrapper appear integrated.
    graph: dict[str, list[str]] = {}
    for rel, body in bodies.items():
        graph[rel] = []
        for match in HB_INPUT_RE.finditer(body):
            target = _normalized_tex_input(match.group(1) or match.group(2))
            if target in bodies:
                graph[rel].append(target)

    def route_count(node: str, target: str, active: frozenset[str]) -> int:
        if node == target:
            return 1
        if node in active:
            return 0
        count = 0
        next_active = active | {node}
        for child in graph.get(node, []):
            count += route_count(child, target, next_active)
            if count > 1:
                return count
        return count

    for wrapper in sorted(authorized_wrappers):
        count = route_count("main.tex", wrapper, frozenset())
        artifact = wrapper_artifacts[wrapper]
        data.authorized_restorations[artifact]["reachable_once"] = count == 1
        if count != 1:
            data.flag(
                "restoration-scope",
                "validated scope wrapper is not reachable exactly once from "
                f"main.tex: {wrapper} has {count} static route(s)",
            )
    return authorized


def hb_valid_label(label: str, prefix: str = "") -> bool:
    prefixes = (prefix,) if prefix else HB_LABEL_PREFIXES
    for p in prefixes:
        if label.startswith(p) and HB_ID_RE.match(label[len(p):]):
            return True
    return False


def hb_parse_status(spec: str):
    """Return (form, target) for a well-formed status spec, else None."""
    s = spec.strip()
    m = re.fullmatch(r"(proved|sketched)=(annex:[A-Za-z0-9][A-Za-z0-9._-]*)", s)
    if m:
        return m.group(1), m.group(2)
    m = re.fullmatch(r"cited=([A-Za-z0-9][A-Za-z0-9._:+-]*)", s)
    if m:
        return "cited", m.group(1)
    return None


def _line(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


class _HBData:
    """Everything harvested from the tree in one pass."""

    def __init__(self) -> None:
        self.labels: dict[str, list[str]] = {}   # label -> [locations]
        self.refs: list[tuple[str, str, str]] = []  # (target, location, source file)
        self.cites: list[tuple[str, str, str]] = []  # (key, location, context)
        self.statuses: list[dict] = []           # owner/owner_kind/form/target/raw/loc
        self.annexitems: list[dict] = []         # label/backref/loc
        self.entries: list[dict] = []            # label/loc/fields
        self.stub_parts: Counter = Counter()
        self.chapters: list[tuple[str, bool, bool]] = []  # (rel, is_stub, has_cite)
        self.findings: dict[str, list[str]] = {}
        self.authorized_restorations: dict[str, dict[str, object]] = {}
        self.pending_inherited_refs: list[dict[str, object]] = []
        # Necessity: an exact inherited theorem cannot gain an editorial
        # proved=/sketched= field without changing its source bytes, yet an OPEN
        # annex derivative may need to point structurally to that genuine result.
        # Definition: source_result_labels maps a literal label to theorem,
        # lemma, or corollary only when the label occurs inside that environment
        # in a provenance-validated artifact whose wrapper is reachable exactly
        # once.  Standing: this is an administrative structural classification,
        # not proof status, admission, audit PASS, or register closure.
        # Nonredundancy: statuses records editorial proof claims; this mapping
        # records only the environment-to-label association already present in
        # unchanged source.  Use: annex bidirectionality accepts such a backref
        # without manufacturing a reciprocal status and rejects all other cases.
        self.source_result_labels: dict[str, str] = {}

    def flag(self, category: str, msg: str) -> None:
        self.findings.setdefault(category, []).append(msg)

    def add_label(self, label: str, loc: str) -> None:
        self.labels.setdefault(label, []).append(loc)


def _hb_scan_fused_numbers(
    rel: str,
    raw: str,
    data: _HBData,
    retained_reader_files: set[str] | frozenset[str] = frozenset(),
) -> None:
    """Flag fused-space classes A-C in reader TeX."""
    # generated/ views are tool output (fusions there originate in registry/bib notes)
    if rel.startswith(("restoration/", "generated/")) or rel in retained_reader_files:
        return
    try:
        from .find_fused_spaces import scan_tex
    except ImportError:
        from find_fused_spaces import scan_tex
    for hit in scan_tex(raw):
        if hit.cls not in {"A", "B", "C"}:
            continue
        data.flag(
            "fused-number",
            f"{hit.cls} {hit.match!r} -> {hit.suggestion!r} "
            f"({rel}:{hit.line}:{hit.col})",
        )


def _hb_marker_text(match: re.Match[str]) -> str:
    return re.sub(r"\s+", " ", match.group(0)).strip()


def _hb_annex_marker_spans(body: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    for match in re.finditer(r"\\begin\{annexitem\}", body):
        _args, args_end = scan_braced_args(body, match.end(), 3)
        end = body.find(r"\end{annexitem}", args_end)
        spans.append((args_end, len(body) if end == -1 else end))
    for match in re.finditer(r"\\begin\{proof\}", body):
        end = body.find(r"\end{proof}", match.end())
        spans.append((match.end(), len(body) if end == -1 else end))
    return spans


def _hb_scan_stub_markers(rel: str, body: str, zone: str, data: _HBData) -> None:
    """Flag stub/TODO wording where the handbook spec treats it as content."""
    if zone == "parts":
        spans = [(0, len(body))]
    elif zone == "annex":
        spans = _hb_annex_marker_spans(body)
    else:
        return

    seen: set[tuple[int, int]] = set()
    for start, end in sorted(spans):
        for match in HB_STUB_MARKER_RE.finditer(body, start, end):
            key = (match.start(), match.end())
            if key in seen:
                continue
            seen.add(key)
            data.flag(
                "stub-marker",
                f"{_hb_marker_text(match)!r} ({rel}:{_line(body, match.start())})",
            )


def _register_env_label(data: _HBData, env: str, label: str,
                        expected_prefix: str, loc: str) -> str:
    label = label.strip()
    if not label:
        data.flag("env-grammar", f"{env} with empty label argument ({loc})")
        return ""
    data.add_label(label, loc)
    if not hb_valid_label(label, expected_prefix):
        data.flag("label-prefix",
                  f"{env} label '{label}' must be '{expected_prefix}<id>' ({loc})")
    return label


def _hb_scan_status_arg(data: _HBData, owner: str, owner_kind: str,
                        spec: str, loc: str) -> None:
    parsed = hb_parse_status(spec)
    if parsed is None:
        shown = spec.strip() or "<empty>"
        data.flag("status-spec",
                  f"{owner_kind} {owner or '<unlabeled>'}: malformed status "
                  f"spec '{shown}' ({loc})")
        data.statuses.append({"owner": owner, "owner_kind": owner_kind,
                              "form": None, "target": None,
                              "raw": spec.strip(), "loc": loc})
    else:
        form, target = parsed
        data.statuses.append({"owner": owner, "owner_kind": owner_kind,
                              "form": form, "target": target,
                              "raw": spec.strip(), "loc": loc})


def _hb_scan_systementry(data: _HBData, rel: str, body: str,
                         args_end: int, entry_label: str, loc: str) -> tuple[int, bool]:
    """Scan one systementry body; returns (span_end, saw_sources)."""
    end = body.find(r"\end{systementry}", args_end)
    if end == -1:
        data.flag("env-grammar",
                  f"systementry {entry_label or '<unlabeled>'} missing "
                  f"\\end{{systementry}} ({loc})")
        end = len(body)
    fields: set[str] = set()
    field_counts: Counter = Counter()
    valid_required: set[str] = set()
    saw_sources = False
    field_re = re.compile(r"\\(" + "|".join(HB_ENTRY_FIELDS_ALL) + r")\b")
    for fm in field_re.finditer(body, args_end, end):
        name = fm.group(1)
        floc = f"{rel}:{_line(body, fm.start())}"
        fields.add(name)
        field_counts[name] += 1
        if name in HB_ENTRY_FIELDS_REQUIRED and field_counts[name] > 1:
            data.flag(
                "entry-fields",
                f"systementry {entry_label or '<unlabeled>'} duplicates "
                f"required field \\{name} ({floc})",
            )
        if name in ("entryadequacy", "entrydecidability"):
            fargs, _ = scan_braced_args(body, fm.end(), 2)
            if not fargs:
                data.flag("status-spec",
                          f"\\{name} in {entry_label or '<unlabeled>'}: missing "
                          f"status argument ({floc})")
                continue
            if len(fargs) < 2:
                data.flag("env-grammar",
                          f"\\{name} in {entry_label or '<unlabeled>'} with "
                          f"1/2 arguments ({floc})")
            elif not fargs[1].strip():
                data.flag(
                    "entry-fields",
                    f"systementry {entry_label or '<unlabeled>'} has empty "
                    f"required field \\{name} ({floc})",
                )
            else:
                valid_required.add(name)
            _hb_scan_status_arg(data, entry_label, name, fargs[0], floc)
        elif name == "entrycalculus":
            fargs, _ = scan_braced_args(body, fm.end(), 1)
            if not fargs or not fargs[0].strip():
                data.flag(
                    "entry-fields",
                    f"systementry {entry_label or '<unlabeled>'} has empty "
                    f"required field \\{name} ({floc})",
                )
                data.flag("env-grammar",
                          f"\\entrycalculus with empty/missing argument ({floc})")
            else:
                valid_required.add(name)
                target = fargs[0].strip()
                data.refs.append((target, floc, rel))
                if not target.startswith("sheet:"):
                    data.flag("label-prefix",
                              f"\\entrycalculus target '{target}' must be "
                              f"'sheet:<id>' ({floc})")
        elif name == "entrysources":
            fargs, _ = scan_braced_args(body, fm.end(), 1)
            if not fargs or not fargs[0].strip():
                data.flag(
                    "entry-fields",
                    f"systementry {entry_label or '<unlabeled>'} has empty "
                    f"required field \\{name} ({floc})",
                )
            else:
                valid_required.add(name)
                for k in fargs[0].split(","):
                    k = k.strip()
                    if k:
                        data.cites.append((k, floc, "entrysources"))
                        saw_sources = True
        else:
            fargs, _ = scan_braced_args(body, fm.end(), 1)
            if name in HB_ENTRY_FIELDS_REQUIRED:
                if not fargs or not fargs[0].strip():
                    data.flag(
                        "entry-fields",
                        f"systementry {entry_label or '<unlabeled>'} has "
                        f"empty required field \\{name} ({floc})",
                    )
                else:
                    valid_required.add(name)
    missing = [name for name in HB_ENTRY_FIELDS_REQUIRED if name not in fields]
    if missing:
        data.flag(
            "entry-fields",
            f"systementry {entry_label or '<unlabeled>'} missing required "
            f"field(s): {', '.join(missing)} ({loc})",
        )
    valid_required = {
        name for name in valid_required if field_counts[name] == 1
    }
    if entry_label:
        data.entries.append({"label": entry_label, "loc": loc,
                             "fields": fields,
                             "valid_required": valid_required})
    return end, saw_sources


def _hb_scan_file(
    rel: str,
    body: str,
    data: _HBData,
    *,
    restoration_authorized: bool = False,
    source_result_authorized: bool = False,
) -> None:
    if rel.startswith("parts/"):
        zone = "parts"
    elif rel.startswith("annex/"):
        zone = "annex"
    elif rel.startswith("registry/calculi/"):
        zone = "registry/calculi"
    elif rel.startswith("restoration/"):
        zone = "restoration"
    else:
        zone = "other"
    pm = re.match(r"(?:parts|annex)/p(\d{2})", rel)
    part = f"p{pm.group(1)}" if pm else "other"

    has_cite = False
    entry_spans: list[tuple[int, int]] = []

    _hb_scan_stub_markers(rel, body, zone, data)

    if source_result_authorized:
        for source_result in re.finditer(
            r"\\begin\s*\{(theorem|lemma|corollary)\}"
            r"(?:\s*\[[^\]]*\])?(.*?)"
            r"\\end\s*\{\1\}",
            body,
            flags=re.S,
        ):
            environment = source_result.group(1)
            for label_match in re.finditer(
                r"\\label\s*\{([^{}]+)\}", source_result.group(2)
            ):
                label = label_match.group(1).strip()
                if label:
                    data.source_result_labels[label] = environment

    # --- environments -----------------------------------------------------
    for m in HB_ENV_RE.finditer(body):
        env = m.group(1)
        loc = f"{rel}:{_line(body, m.start())}"
        if env in HB_STATUS_ENVS:
            args, _ = scan_braced_args(body, m.end(), 3)
            if len(args) < 3:
                data.flag("env-grammar",
                          f"{env} with {len(args)}/3 arguments ({loc})")
            label = _register_env_label(
                data, env, args[0] if args else "", HB_STATUS_ENVS[env], loc)
            if len(args) >= 2:
                _hb_scan_status_arg(data, label, env, args[1], loc)
            else:
                data.flag("status-spec",
                          f"{env} {label or '<unlabeled>'}: missing status "
                          f"argument ({loc})")
                data.statuses.append({"owner": label, "owner_kind": env,
                                      "form": None, "target": None,
                                      "raw": "", "loc": loc})
        elif env in HB_PLAIN_ENVS:
            args, _ = scan_braced_args(body, m.end(), 2)
            if len(args) < 2:
                data.flag("env-grammar",
                          f"{env} with {len(args)}/2 arguments ({loc})")
            _register_env_label(
                data, env, args[0] if args else "", HB_PLAIN_ENVS[env], loc)
        elif env == "systementry":
            args, args_end = scan_braced_args(body, m.end(), 2)
            if len(args) < 2:
                data.flag("env-grammar",
                          f"systementry with {len(args)}/2 arguments ({loc})")
            label = _register_env_label(
                data, env, args[0] if args else "", "entry:", loc)
            span_end, saw_sources = _hb_scan_systementry(
                data, rel, body, args_end, label, loc)
            entry_spans.append((m.start(), span_end))
            has_cite = has_cite or saw_sources
        elif env == "annexitem":
            args, _ = scan_braced_args(body, m.end(), 3)
            if len(args) < 3:
                data.flag("env-grammar",
                          f"annexitem with {len(args)}/3 arguments ({loc})")
            label = _register_env_label(
                data, env, args[0] if args else "", "annex:", loc)
            backref = args[1].strip() if len(args) >= 2 else ""
            if backref and not (
                hb_valid_label(backref, "thm:")
                or hb_valid_label(backref, "entry:")
                or hb_valid_label(backref, "lem:")
                or hb_valid_label(backref, "cor:")
            ):
                data.flag("label-prefix",
                          f"annexitem backref '{backref}' must be "
                          f"'thm:<id>' (or a validated reachable source "
                          f"'lem:<id>'/'cor:<id>', or 'entry:<id>' for "
                          f"entry-card statuses) ({loc})")
            if label or backref:
                data.annexitems.append(
                    {"label": label, "backref": backref, "loc": loc})

    # --- entry fields outside any systementry (harvest would miss them) ---
    stray_re = re.compile(r"\\(entryadequacy|entrydecidability)\b")
    for sm in stray_re.finditer(body):
        if any(a <= sm.start() < b for a, b in entry_spans):
            continue
        floc = f"{rel}:{_line(body, sm.start())}"
        data.flag("env-grammar",
                  f"\\{sm.group(1)} outside a systementry ({floc})")
        fargs, _ = scan_braced_args(body, sm.end(), 1)
        if fargs and hb_parse_status(fargs[0]) is None:
            data.flag("status-spec",
                      f"{sm.group(1)} <stray>: malformed status spec "
                      f"'{fargs[0].strip() or '<empty>'}' ({floc})")

    # --- registry macros --------------------------------------------------
    for m in re.finditer(r"\\calculussheet\b", body):
        loc = f"{rel}:{_line(body, m.start())}"
        args, _ = scan_braced_args(body, m.end(), 3)
        if len(args) < 3:
            data.flag("env-grammar",
                      f"\\calculussheet with {len(args)}/3 arguments ({loc})")
        _register_env_label(
            data, "calculussheet", args[0] if args else "", "sheet:", loc)
    for m in re.finditer(r"\\hbrule\b", body):
        loc = f"{rel}:{_line(body, m.start())}"
        if zone != "registry/calculi" and not restoration_authorized:
            data.flag("rule-outside-registry", f"\\hbrule ({loc})")
        args, _ = scan_braced_args(body, m.end(), 5)
        if len(args) < 5:
            data.flag("env-grammar",
                      f"\\hbrule with {len(args)}/5 arguments ({loc})")
        _register_env_label(
            data, "hbrule", args[0] if args else "", "rule:", loc)

    # --- plain labels, refs, cites ---------------------------------------
    for m in re.finditer(r"\\label\{([^{}]+)\}", body):
        label = m.group(1).strip()
        loc = f"{rel}:{_line(body, m.start())}"
        data.add_label(label, loc)
        # A provenance-validated restoration keeps the source presentation's
        # published label syntax byte-for-byte.  House-prefix validation is
        # therefore inapplicable there; duplicate-label and dangling-reference
        # checks still consume the literal label through data.add_label above.
        if not restoration_authorized and not hb_valid_label(label):
            data.flag("label-prefix",
                      f"\\label '{label}' outside the prefix taxonomy "
                      f"{'/'.join(p[:-1] for p in HB_LABEL_PREFIXES)} ({loc})")
    for m in HB_REF_RE.finditer(body):
        arg = m.group(1) or m.group(2)
        loc = f"{rel}:{_line(body, m.start())}"
        for t in arg.split(","):
            t = t.strip()
            if t:
                data.refs.append((t, loc, rel))
    for m in re.finditer(r"\\showcalculus\s*\{([^{}]+)\}", body):
        slug = m.group(1).strip()
        target = slug if slug.startswith("sheet:") else f"sheet:{slug}"
        data.refs.append((target, f"{rel}:{_line(body, m.start())}", rel))
    for m in HB_CITE_RE.finditer(body):
        loc = f"{rel}:{_line(body, m.start())}"
        for k in m.group(1).split(","):
            k = k.strip()
            if k and k != "*":
                data.cites.append((k, loc, "cite"))
                has_cite = True

    # --- zone bans --------------------------------------------------------
    if zone == "parts":
        for m in re.finditer(r"\\begin\{proof\}", body):
            data.flag("body-proof",
                      f"proof environment under parts/ "
                      f"({rel}:{_line(body, m.start())})")
    if zone == "restoration" and not restoration_authorized:
        for m in re.finditer(r"\\begin\{proof\}", body):
            data.flag(
                "restoration-scope",
                f"unscoped inherited proof "
                f"({rel}:{_line(body, m.start())})",
            )
    if not restoration_authorized:
        for m in HB_SOURCE_ENV_RE.finditer(body):
            data.flag(
                "restoration-scope",
                f"source environment {m.group(1)} outside a validated "
                f"restoration scope ({rel}:{_line(body, m.start())})",
            )
        detokenized = _hb_detokenize_argument_spans(body)
        for m in HB_SOURCE_COMMAND_RE.finditer(body):
            if any(start <= m.start() < end for start, end in detokenized):
                continue
            data.flag(
                "restoration-scope",
                f"source command \\{m.group(1)} outside a validated "
                f"restoration scope ({rel}:{_line(body, m.start())})",
            )
    if zone != "registry/calculi" and not restoration_authorized:
        for m in HB_RULECMD_RE.finditer(body):
            data.flag("rule-outside-registry",
                      f"\\{m.group(1)} rule display "
                      f"({rel}:{_line(body, m.start())})")
        for m in HB_FRAC_RE.finditer(body):
            window = body[m.end():m.end() + 240]
            if HB_SEQ_MARK_RE.search(window):
                data.flag("rule-outside-registry",
                          f"\\frac-based rule shape "
                          f"({rel}:{_line(body, m.start())})")

    # --- stubs and chapters ----------------------------------------------
    n_stub = len(re.findall(r"\\hbstub\b", body))
    if n_stub:
        data.stub_parts[part] += n_stub
    body_without_audit_wrapper = re.sub(
        r"\\chapter\*\s*\{Part\s+\d+\s+Audit Register\}",
        "",
        body,
    )
    if zone == "parts" and re.search(r"\\chapter\b", body_without_audit_wrapper):
        data.chapters.append((rel, n_stub > 0, has_cite))


def _hb_source_inventory_labels(root: Path, data: _HBData) -> dict[str, int]:
    """Load unique exact source labels and their governed start lines."""
    path = root / "spec" / "source-unit-inventory.csv"
    try:
        with path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
            fieldnames = set(reader.fieldnames or [])
    except (OSError, UnicodeError, csv.Error) as exc:
        data.flag("missing-infra", f"source-unit inventory is unreadable: {exc}")
        return {}
    required = {"label", "start_line"}
    if not required.issubset(fieldnames):
        data.flag(
            "missing-infra",
            "spec/source-unit-inventory.csv lacks label/start_line columns",
        )
        return {}
    labels: dict[str, int] = {}
    unusable: set[str] = set()
    for row_number, row in enumerate(rows, start=2):
        label = (row.get("label") or "").strip()
        if not label:
            continue
        try:
            start_line = int(row.get("start_line") or "")
        except ValueError:
            data.flag(
                "restoration-scope",
                f"source-unit inventory label {label!r} has an invalid start line "
                f"(spec/source-unit-inventory.csv:{row_number})",
            )
            unusable.add(label)
            labels.pop(label, None)
            continue
        if start_line < 1 or label in labels or label in unusable:
            data.flag(
                "restoration-scope",
                f"source-unit inventory label {label!r} is not uniquely bound to "
                f"one positive start line (spec/source-unit-inventory.csv:{row_number})",
            )
            unusable.add(label)
            labels.pop(label, None)
            continue
        labels[label] = start_line
    return labels


def _hb_cross_checks(data: _HBData, source_labels: dict[str, int]) -> None:
    # Duplicate labels (plain \label and environment-argument labels alike).
    for label, sites in sorted(data.labels.items()):
        if len(sites) > 1:
            data.flag("duplicate-label",
                      f"{label} defined {len(sites)}x ({', '.join(sites)})")

    # Dangling references.
    known = set(data.labels)
    for target, loc, rel in data.refs:
        if target in known:
            continue
        authorization = data.authorized_restorations.get(rel)
        target_start = source_labels.get(target)
        governed_end = (
            int(authorization["governed_end_line"]) if authorization else None
        )
        mapped_original_occurrence = True
        if authorization and authorization.get("authorization_kind") == "corrected-reader":
            try:
                reader_line = int(loc.rsplit(":", 1)[1])
            except (ValueError, IndexError):
                mapped_original_occurrence = False
            else:
                mapped_original_occurrence = authorization["source_line_map"].get(reader_line) is not None
        if (authorization and mapped_original_occurrence
                and target_start is not None and target_start > governed_end):
            data.pending_inherited_refs.append(
                {
                    "target": target,
                    "loc": loc,
                    "provenance_id": authorization["provenance_id"],
                    "governed_end_line": governed_end,
                    "target_start_line": target_start,
                }
            )
            continue
        data.flag("dangling-ref", f"{target} ({loc})")

    # Annex <-> body bidirectionality.
    annex_by_label: dict[str, list[dict]] = {}
    for it in data.annexitems:
        if it["label"]:
            annex_by_label.setdefault(it["label"], []).append(it)
    status_by_target: dict[str, list[dict]] = {}
    for st in data.statuses:
        if st["form"] in ("proved", "sketched") and st["owner"]:
            status_by_target.setdefault(st["target"], []).append(st)
    resolvable = ({st["owner"] for st in data.statuses if st["owner"]}
                  | {e["label"] for e in data.entries})

    for target, sts in sorted(status_by_target.items()):
        if len(sts) > 1:
            data.flag("annex-bidir",
                      f"{target} targeted by {len(sts)} results: "
                      f"{', '.join(s['owner'] for s in sts)}")
        items = annex_by_label.get(target, [])
        if not items:
            for s in sts:
                data.flag("annex-bidir",
                          f"{s['owner']} {s['form']}={target}: no annexitem "
                          f"{target} exists ({s['loc']})")
        elif len(items) == 1:
            it = items[0]
            for s in sts:
                if it["backref"] != s["owner"]:
                    data.flag("annex-bidir",
                              f"annexitem {target} backref '{it['backref']}' "
                              f"does not point back to {s['owner']} "
                              f"({it['loc']})")
        else:
            data.flag("annex-bidir",
                      f"{target}: {len(items)} annexitems share the label")

    for it in data.annexitems:
        back, label = it["backref"], it["label"]
        if not label or not back:
            continue
        if (back.startswith("lem:") or back.startswith("cor:")) and (
            back not in data.source_result_labels
        ):
            data.flag(
                "label-prefix",
                f"annexitem backref '{back}' is permitted only for a literal "
                f"label in a validated reachable source result ({it['loc']})",
            )
        if any(s["owner"] == back for s in status_by_target.get(label, [])):
            continue
        if back in data.source_result_labels:
            continue
        if back not in resolvable:
            data.flag("annex-bidir",
                      f"annexitem {label} backref '{back}' does not resolve "
                      f"to a body result ({it['loc']})")
        else:
            data.flag("annex-bidir",
                      f"annexitem {label}: backref '{back}' has no "
                      f"proved=/sketched= status pointing at {label} "
                      f"({it['loc']})")

    # Zero-citation non-stub chapters.
    for rel, is_stub, has_cite in data.chapters:
        if not is_stub and not has_cite:
            data.flag("zero-cite-chapter", rel)


def _hb_scope_parts(scope: str) -> set[int]:
    """Compatibility helper for strict legacy scopes; no numeric guessing.

    Declaration scopes require the shared reader resolver used below. Unknown
    scopes are errors, rather than globally visible or silently disjoint.
    """
    try:
        from . import symbol_registry
    except ImportError:
        import symbol_registry
    interval = symbol_registry.parse_scope(scope)
    if interval is None:
        raise ValueError(f"unknown legacy symbol scope {scope!r}")
    return {part * 100 + chapter for part in range(1, 20)
            for chapter in range(100)
            if interval[0] <= part * 1000 + chapter <= interval[1]}


def _hb_check_symbols(path: Path, data: _HBData) -> None:
    if not path.is_file():
        data.flag("missing-infra", f"registry/symbols.csv not found ({path})")
        return
    try:
        from . import symbol_registry
    except ImportError:
        import symbol_registry
    rows, errors = symbol_registry.read_rows(path)
    for error in errors:
        data.flag("symbols-csv", error)
    for error in symbol_registry.collision_check(rows):
        data.flag("glyph-collision" if "glyph-role collision" in error
                  else "symbols-csv", error)
    by_glyph = {re.sub(r"\s+", "", row["glyph"]) for row in rows}
    print(f"[metric] symbol registry: {len(rows)} rows, "
          f"{len(by_glyph)} distinct glyphs")


def _hb_check_bib(path: Path, data: _HBData) -> None:
    wanted = list(data.cites) + [
        (s["target"], s["loc"], f"cited= on {s['owner'] or '<unlabeled>'}")
        for s in data.statuses if s["form"] == "cited"]
    if not path.is_file():
        data.flag("missing-infra",
                  f"bib/handbook.bib not found ({path}); "
                  f"{len(set(k for k, _, _ in wanted))} cite key(s) unchecked")
        return
    text = path.read_text(encoding="utf-8", errors="replace")
    keys: set[str] = set()
    n_stub = 0
    for m in re.finditer(r"@([A-Za-z]+)\s*\{\s*([^,\s{}]+)\s*,", text):
        if m.group(1).lower() in ("comment", "preamble", "string"):
            continue
        keys.add(m.group(2))
    for chunk in re.split(r"(?=@[A-Za-z]+\s*\{)", text):
        if re.match(r"@(comment|preamble|string)\b", chunk, re.I):
            continue
        if re.search(r"keywords\s*=\s*[{\"][^}\"]*\bstub\b", chunk):
            n_stub += 1
    print(f"[metric] bibliography: {len(keys)} entries ({n_stub} intake stubs)")
    missing: dict[str, list[str]] = {}
    for key, loc, ctx in wanted:
        if key not in keys:
            missing.setdefault(key, []).append(f"{loc} [{ctx}]")
    for key in sorted(missing):
        sites = missing[key]
        shown = ", ".join(sites[:3]) + (f", +{len(sites) - 3} more"
                                        if len(sites) > 3 else "")
        data.flag("bib-key", f"'{key}' not in bib/handbook.bib ({shown})")


def _hb_metrics(data: _HBData) -> None:
    print(f"[metric] pending inherited references: {len(data.pending_inherited_refs)}")
    for item in data.pending_inherited_refs:
        print(
            "[pending] inherited reference: "
            f"{item['target']} ({item['loc']}; {item['provenance_id']} ends at "
            f"source line {item['governed_end_line']}, target starts at "
            f"{item['target_start_line']})"
        )
    forms = Counter((s["form"] or "malformed") for s in data.statuses)
    print(f"[metric] status forms: proved={forms.get('proved', 0)} "
          f"sketched={forms.get('sketched', 0)} cited={forms.get('cited', 0)} "
          f"malformed={forms.get('malformed', 0)}")
    if data.stub_parts:
        per = " ".join(f"{p}={n}" for p, n in sorted(data.stub_parts.items()))
        print(f"[metric] stubs per part: {per} | total={sum(data.stub_parts.values())}")
    else:
        print("[metric] stubs per part: none")
    n = len(data.entries)
    if n:
        cov = " ".join(
            f"{f.removeprefix('entry')}="
            f"{sum(1 for e in data.entries if f in e['valid_required'])}/{n}"
            for f in HB_ENTRY_FIELDS_REQUIRED)
        print(f"[metric] entry cards: {n}; required-field coverage: {cov}")
    else:
        print("[metric] entry cards: 0")


def check_handbook(
    root: Path, strict: bool, require_no_pending_inherited_refs: bool = False
) -> int:
    base = root / "handbook"
    if not base.is_dir():
        print(f"[check] no handbook tree at {base}", file=sys.stderr)
        return 2
    files = sorted(base.rglob("*.tex"))
    if not files:
        print(f"[check] warning: no .tex files under {base} yet (half-built tree)")
    data = _HBData()
    raw_bodies: dict[str, str] = {}
    bodies: dict[str, str] = {}
    for p in files:
        rel = p.relative_to(base).as_posix()
        raw = p.read_text(encoding="utf-8", errors="replace")
        raw_bodies[rel] = raw
        bodies[rel] = strip_verbatims(strip_comments(raw))
    authorized_restorations = _hb_validate_restoration_scopes(
        base, bodies, data
    )
    retained_unreachable_reader_files = _hb_retained_unreachable_reader_files(
        base, bodies, data
    )
    for rel, body in bodies.items():
        if rel in retained_unreachable_reader_files:
            continue
        _hb_scan_fused_numbers(
            rel,
            raw_bodies[rel],
            data,
            retained_unreachable_reader_files,
        )
        _hb_scan_file(
            rel,
            body,
            data,
            restoration_authorized=rel in authorized_restorations,
            source_result_authorized=(
                rel in authorized_restorations
                and bool(
                    data.authorized_restorations.get(rel, {}).get(
                        "reachable_once", False
                    )
                )
            ),
        )
    source_labels = _hb_source_inventory_labels(root, data)
    _hb_cross_checks(data, source_labels)
    if require_no_pending_inherited_refs:
        for item in data.pending_inherited_refs:
            data.flag(
                "pending-inherited-ref",
                f"{item['target']} ({item['loc']}; authorized by "
                f"{item['provenance_id']}, target source line "
                f"{item['target_start_line']} is not integrated)",
            )
    _hb_check_symbols(base / "registry" / "symbols.csv", data)
    _hb_check_bib(base / "bib" / "handbook.bib", data)
    _hb_metrics(data)

    hard: list[str] = []
    soft: list[str] = []
    extra = tuple(sorted(set(data.findings) - set(HB_CATEGORY_ORDER)))
    for cat in HB_CATEGORY_ORDER + extra:
        for msg in data.findings.get(cat, []):
            (hard if strict or cat in HB_ALWAYS_HARD else soft).append(
                f"{cat}: {msg}")
    if soft:
        print(f"\n[check] {len(soft)} finding(s) (hard under --strict):")
        for e in soft:
            print(f"  - {e}")
    if hard:
        print(f"\n[check] {len(hard)} hard failure(s):")
        for e in hard:
            print(f"  - {e}")
        return 1
    print("[check] all hard checks passed")
    return 0


def _selftest() -> None:
    assert HB_CATEGORY_ORDER.index("fused-number") < HB_CATEGORY_ORDER.index(
        "env-grammar"
    )
    assert HB_CATEGORY_ORDER.index("stub-marker") < HB_CATEGORY_ORDER.index(
        "env-grammar"
    )
    assert "fused-number" not in HB_ALWAYS_HARD
    assert "stub-marker" not in HB_ALWAYS_HARD

    data = _HBData()
    _hb_scan_fused_numbers(
        "parts/p01/body.tex",
        "around1115 NotreDame\n",
        data,
    )
    fused = data.findings.get("fused-number", [])
    assert len(fused) == 1
    assert "around1115" in fused[0]
    assert "NotreDame" not in fused[0]

    data = _HBData()
    _hb_scan_fused_numbers(
        "restoration/inherited-00001-00002.tex",
        "around1115\n",
        data,
    )
    assert "fused-number" not in data.findings

    data = _HBData()
    _hb_scan_fused_numbers(
        "parts/p01/body.tex",
        "around1115\n",
        data,
        {"parts/p01/body.tex"},
    )
    assert "fused-number" not in data.findings

    data = _HBData()
    _hb_scan_file(
        "parts/p01/body.tex",
        r"\chapter{Stub}\hbstub TODO left to the reader.",
        data,
    )
    part_markers = "\n".join(data.findings.get("stub-marker", [])).lower()
    assert "\\hbstub" in part_markers
    assert "todo" in part_markers
    assert "left to the reader" in part_markers

    data = _HBData()
    _hb_scan_file(
        "annex/p01/demo.tex",
        r"""
TODO outside.
\begin{annexitem}{annex:p01.demo}{thm:p01.demo}{proved}
Routine verification.
\begin{proof}
Details omitted.
\end{proof}
\end{annexitem}
TBD outside.
\begin{proof}
Similarly for the remaining cases.
\end{proof}
""",
        data,
    )
    annex_markers = "\n".join(data.findings.get("stub-marker", [])).lower()
    assert "routine verification" in annex_markers
    assert "details omitted" in annex_markers
    assert "similarly for the remaining cases" in annex_markers
    assert "todo" not in annex_markers
    assert "tbd" not in annex_markers


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tree", choices=("source", "handbook"), default="source")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--selftest", action="store_true",
                    help="run internal assert-based checks")
    ap.add_argument(
        "--require-no-pending-inherited-refs",
        action="store_true",
        help="fail even provenance-authorized inherited references whose exact "
             "later source targets are not integrated yet",
    )
    ap.add_argument("--root", type=Path, default=ROOT,
                    help="repo root override (handbook tree only; used by the "
                         "check suite's own fixture tests)")
    args = ap.parse_args()

    if args.selftest:
        _selftest()
        return 0

    if args.tree == "handbook":
        return check_handbook(
            Path(args.root).resolve(),
            strict=args.strict,
            require_no_pending_inherited_refs=args.require_no_pending_inherited_refs,
        )

    texts = read_tree(args.tree)
    hard: list[str] = []

    label_errors, labels = check_labels(texts)
    hard += label_errors
    hard += check_refs(texts, labels)
    hard += check_bib(texts)

    covered, total = status_coverage(texts)
    pct = 100.0 * covered / total if total else 100.0
    print(f"[metric] result environments: {total}; with status marker: {covered} ({pct:.1f}%)")

    if args.strict:
        if total and covered < total:
            hard.append(f"status coverage {pct:.1f}% < 100% (strict)")
        hard += rule_display_ban(texts)
        hard += zero_cite_chapters(texts)

    if hard:
        print(f"\n[check] {len(hard)} hard failure(s):")
        for e in hard:
            print(f"  - {e}")
        return 1
    print("[check] all hard checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

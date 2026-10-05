"""Shared, strict symbol-row validation and reader-region resolution.

The CSV keeps its seven public fields. Numeric scopes retain their old meaning;
labels resolve on the literal reader input route. Named source scopes and any
exception to a broader role require explicit bindings in symbol-scopes.json.
Unknown text is never interpreted as global or as a disjoint namespace.
"""
from __future__ import annotations

import bisect
import csv
from dataclasses import dataclass, field
import json
from pathlib import Path
import re

HEADER = ['glyph', 'macro', 'role', 'scope', 'precedence', 'first_use', 'notes']
REQUIRED = HEADER[:-1]
POINT_RE = re.compile(r'^P([1-9]|1[0-9])(?:\.([0-9]{1,2}))?$')
FIRST_RE = re.compile(r'^P([1-9]|1[0-9])\.([0-9]{1,2})$')
LABEL_RE = re.compile(r'^(?:part|sec|entry|def|thm|tab|fig|sheet|rule|annex):[A-Za-z0-9][A-Za-z0-9_.:-]*$')
# The last three are declared form/category descriptors, not invented ranks.
PREC_RE = re.compile(r'^(?:[0-9]+(?:\.[0-9]+)?|meta|n/a|object|relation|infix)$')
GLOBAL = (0, 20000)


def point_interval(token):
    match = POINT_RE.fullmatch(token)
    if not match:
        return None
    part = int(match[1])
    return ((part * 1000, part * 1000 + 999) if match[2] is None
            else (part * 1000 + int(match[2]),) * 2)


def parse_scope(text):
    """Legacy numeric scope only; unknown and out-of-range tokens return None."""
    if text == 'global':
        return GLOBAL
    interval = point_interval(text)
    if interval:
        return interval
    match = re.fullmatch(r'(P\d+(?:\.\d+)?)-(P\d+(?:\.\d+)?)', text)
    if match:
        left, right = point_interval(match[1]), point_interval(match[2])
        if left and right and left[0] <= right[1]:
            return left[0], right[1]
    return None


def overlap(a, b):
    return max(a[0], b[0]) <= min(a[1], b[1])


@dataclass
class Declaration:
    label: str
    path: str
    line: int
    part: int | None
    chapter: int | None
    start: int
    end: int
    kind: str
    owner: str | None = None


@dataclass
class Region:
    start: int
    end: int
    part: int | None
    chapter: int | None
    description: str


@dataclass
class Scope:
    raw: str
    interval: tuple[int, int] | None = None
    regions: list[Region] = field(default_factory=list)
    presentation: str | None = None
    overrides: list[dict] = field(default_factory=list)

    @property
    def part(self):
        if self.interval:
            return 'global' if self.interval == GLOBAL else self.interval[0] // 1000
        parts = {r.part for r in self.regions if r.part is not None}
        return min(parts) if parts else None


class RegistryError(ValueError):
    pass


def _grammar():
    # Imported lazily: check.py calls this module only in its symbol phase.
    try:
        from . import check
    except ImportError:
        import check
    return check


class ReaderIndex:
    """Declaration regions from actual input order, with source-file locations.

    This is a static reader index, not a TeX engine. Named bindings may only use
    files reached through main.tex. It ignores generated tables to avoid making
    registry validity depend on the registry's previous generated output.
    """
    COMMAND = re.compile(r'\\(input|include|label|chapter|section|subsection|subsubsection|paragraph|subparagraph|begin|end|calculussheet|hbrule)\b')
    LEVELS = {'chapter':0, 'section':1, 'subsection':2, 'subsubsection':3, 'paragraph':4, 'subparagraph':5}
    NAMED = {'hbdefinition','hbconvention','hbmethod','hbexample','hbwarning','proofboundary','hbtheorem','hblemma','hbcorollary','systementry','annexitem'}
    ORDINARY = {'theorem','lemma','corollary','definition','proposition','example','remark','claim'}

    def __init__(self, base: Path):
        self.base = base.resolve()
        self.labels: dict[str, list[Declaration]] = {}
        self.files: dict[str, list[Region]] = {}
        self.errors: list[str] = []
        self.position = 0
        self.counts: dict[int,int] = {}
        self.headings: list[tuple[int,str,int,list[Declaration]]] = []
        self.heading_records: list[Declaration] = []
        self.environment: list[tuple[str,int,list[Declaration]]] = []
        self.active: list[str] = []
        self.current_part = None
        self.current_zone = ''
        # One record per routed file visit: stripped text plus (offset,
        # position, chapter) marks, used by notation_lint to place a use.
        self.visits: list[dict] = []
        if (self.base/'main.tex').is_file():
            self._visit('main.tex', None)
            self._close_headings(0)

    def _close_headings(self, level):
        while self.headings and self.headings[-1][0] >= level:
            _, _, _, declarations = self.headings.pop()
            for declaration in declarations:
                declaration.end = self.position

    def _add(self, label, rel, line, part, chapter, kind, start, owner=None):
        declaration = Declaration(label,rel,line,part,chapter,start,start+1,kind,owner)
        self.labels.setdefault(label,[]).append(declaration)
        return declaration

    def _visit(self, rel, inherited_part):
        path=(self.base/rel).resolve()
        if not path.is_relative_to(self.base):
            self.errors.append('reader input outside handbook: '+rel);return
        rel=path.relative_to(self.base).as_posix()
        if rel.startswith('generated/'):
            return
        if not path.is_file():
            # Existing generators may not yet have written all apparatus files.
            # They contain no source declarations that can resolve a first use.
            return
        if rel in self.active:
            self.errors.append('cyclic reader input: '+' -> '.join(self.active+[rel]));return
        grammar=_grammar()
        text=grammar.strip_verbatims(grammar.strip_comments(path.read_text(encoding='utf-8-sig')))
        pm=re.match(r'(parts|annex)/p(\d{2})(?:[/.\-]|$)',rel)
        part=int(pm[2]) if pm else inherited_part
        zone=pm[1] if pm else self.current_zone
        if part != self.current_part or zone != self.current_zone:
            self._close_headings(0)
            self.current_part,self.current_zone=part,zone
        file_start=self.position
        self.active.append(rel)
        consumed=0;marks=[]
        for match in self.COMMAND.finditer(text):
            if match.start()<consumed:
                continue
            # State in effect for the text before this command.
            marks.append((match.start(),self.position,self.counts.get(part) if zone=='parts' else None))
            command=match[1];cursor=match.end()
            if cursor<len(text) and text[cursor]=='*':cursor+=1
            if cursor<len(text) and text[cursor]=='[':
                close=text.find(']',cursor)
                if close>=0:cursor=close+1
            args,end=grammar.scan_braced_args(text,cursor,1)
            if not args:continue
            consumed=end; value=args[0]
            self.position+=1
            line=text.count('\n',0,match.start())+1
            chapter=self.counts.get(part) if zone=='parts' else None
            if command in {'input','include'}:
                if re.fullmatch(r'[A-Za-z0-9_./\-]+',value):
                    target=value if value.endswith('.tex') else value+'.tex'
                    self._visit(target,part)
                continue
            if command in self.LEVELS:
                level=self.LEVELS[command];self._close_headings(level)
                if command=='chapter' and zone=='parts' and part is not None:
                    self.counts[part]=self.counts.get(part,0)+1
                    chapter=self.counts[part]
                heading=Declaration('',rel,line,part,chapter,self.position,self.position+1,command)
                self.heading_records.append(heading)
                self.headings.append((level,zone,self.position,[heading]))
            elif command=='begin' and value in self.NAMED|self.ORDINARY:
                declarations=[]
                if value in self.NAMED:
                    ea,ee=grammar.scan_braced_args(text,end,2 if value=='annexitem' else 1)
                    if ea:
                        declarations.append(self._add(ea[0],rel,line,part,chapter,value,self.position,ea[1] if value=='annexitem' and len(ea)>1 else None))
                        consumed=ee
                self.environment.append((value,self.position,declarations))
            elif command=='end' and self.environment and self.environment[-1][0]==value:
                _,_,declarations=self.environment.pop()
                for declaration in declarations:declaration.end=self.position+1
            elif command=='label':
                if self.environment:
                    env,start,declarations=self.environment[-1]
                    declaration=self._add(value,rel,line,part,chapter,env,start)
                    declarations.append(declaration)
                elif self.headings:
                    level,_,start,declarations=self.headings[-1]
                    declaration=self._add(value,rel,line,part,chapter,list(self.LEVELS)[level],start)
                    declarations.append(declaration)
                else:
                    self._add(value,rel,line,part,chapter,'label',self.position)
            elif command in {'calculussheet','hbrule'}:
                self._add(value,rel,line,part,chapter,command,self.position)
        marks.append((len(text),self.position,self.counts.get(part) if zone=='parts' else None))
        self.visits.append({'path':rel,'text':text,'marks':marks,'part':part,'zone':zone})
        self.position+=1
        self.files.setdefault(rel,[]).append(Region(file_start,self.position,part,self.counts.get(part) if zone=='parts' else None,rel))
        self.active.pop()

    def unique(self, label):
        sites=self.labels.get(label,[])
        if len(sites)!=1:
            raise RegistryError(f'declaration {label!r} resolves {len(sites)} times on the reader route')
        return sites[0]

    def numeric_location(self, declaration, seen=None):
        if declaration.owner:
            seen=set() if seen is None else seen
            if declaration.label in seen:raise RegistryError('cyclic annex association: '+declaration.label)
            seen.add(declaration.label)
            return self.numeric_location(self.unique(declaration.owner),seen)
        if declaration.part is None or declaration.chapter is None:
            raise RegistryError(f'no body chapter association for {declaration.label!r}')
        return declaration.part*1000+declaration.chapter

    def region(self, spec):
        if set(spec)=={'file'}:
            sites=self.files.get(spec['file'],[])
            if len(sites)!=1:raise RegistryError(f'region file {spec["file"]!r} resolves {len(sites)} times')
            return sites[0]
        if set(spec)=={'heading_of','level'}:
            target=self.unique(spec['heading_of'])
            candidates=[h for h in self.heading_records if h.kind==spec['level'] and h.start<=target.start<h.end and h.part==target.part]
            if not candidates:raise RegistryError('no declared containing heading for '+repr(spec))
            heading=max(candidates,key=lambda h:h.start)
            return Region(heading.start,heading.end,heading.part,heading.chapter,str(spec))
        if set(spec) not in ({'anchor'},{'from','through'}):
            raise RegistryError('invalid region binding '+repr(spec))
        first=self.unique(spec.get('anchor',spec.get('from')))
        last=self.unique(spec['through']) if 'through' in spec else first
        if first.start>last.start or first.part!=last.part or first.path.split('/')[0]!=last.path.split('/')[0]:
            raise RegistryError('unordered or cross-part declaration range '+repr(spec))
        return Region(first.start,last.end,first.part,first.chapter,str(spec))


class Resolver:
    def __init__(self, base=None, bindings=None, index=None):
        self.index=index or (ReaderIndex(base) if base and (base/'main.tex').is_file() else None)
        if bindings is None and base and (base/'registry/symbol-scopes.json').is_file():
            bindings=json.loads((base/'registry/symbol-scopes.json').read_text(encoding='utf-8-sig'))
        self.bindings=bindings or {'schema_version':1,'scopes':{}}
        if self.bindings.get('schema_version')!=1 or not isinstance(self.bindings.get('scopes'),dict):
            raise RegistryError('invalid symbol-scopes.json schema')
        self.cache={}
        bibpath=(self.index.base/'bib/handbook.bib') if self.index else None
        self.source_keys=set(re.findall(r'@[A-Za-z]+\s*\{\s*([^,\s]+)',bibpath.read_text(encoding='utf-8-sig'))) if bibpath and bibpath.is_file() else set()

    def resolve(self, raw):
        if raw in self.cache:return self.cache[raw]
        numeric=parse_scope(raw)
        named_part=re.match(r'^P(\d+)(?:[.\s-]|$)',raw)
        if named_part and not 1<=int(named_part[1])<=19:
            raise RegistryError('stable part outside P1-P19 in '+raw)
        if numeric is None and re.match(r'^P\d+\.\d+(?:$|-)',raw):
            raise RegistryError('malformed numeric chapter scope '+raw)
        if numeric:
            result=Scope(raw,interval=numeric)
        else:
            if self.index is None:raise RegistryError(f'scope {raw!r} needs a reader declaration index')
            binding=self.bindings['scopes'].get(raw)
            if binding is not None:
                if not isinstance(binding,dict) or not binding.get('presentation') or not binding.get('regions'):
                    raise RegistryError('named scope lacks presentation/regions: '+raw)
                result=Scope(raw,regions=[self.index.region(s) for s in binding['regions']],presentation=binding['presentation'],overrides=binding.get('overrides',[]))
                if named_part and any(r.part!=int(named_part[1]) for r in result.regions):
                    raise RegistryError('named scope part differs from its declared reader regions: '+raw)
                if not isinstance(result.overrides,list):raise RegistryError('overrides must be a list in '+raw)
                for item in result.overrides:
                    required={'glyph','local_role','first_use','broader_scope','broader_role','reason','source'}
                    if not isinstance(item,dict) or set(item)!=required or not all(isinstance(v,str) and v.strip() for v in item.values()):
                        raise RegistryError('override requires exact row selectors, source and reason in '+raw)
                    if item['source'] not in self.source_keys:raise RegistryError('unidentified override source '+item['source'])
                    declaration=self.index.unique(item['first_use'])
                    if not any(r.start<=declaration.start<r.end for r in result.regions):
                        raise RegistryError('override declaration lies outside its scope in '+raw)
            elif LABEL_RE.fullmatch(raw):
                result=Scope(raw,regions=[self.index.region({'anchor':raw})])
            elif ' through ' in raw:
                ends=raw.split(' through ')
                if len(ends)!=2 or not all(LABEL_RE.fullmatch(s) for s in ends):
                    raise RegistryError('malformed declaration range '+raw)
                result=Scope(raw,regions=[self.index.region({'from':ends[0],'through':ends[1]})])
            else:raise RegistryError(f'unknown scope {raw!r}; an explicit declaration/region binding is required')
        if result.part is None:raise RegistryError('scope has no stable part binding: '+raw)
        self.cache[raw]=result
        return result

    def contains(self, scope, first):
        numeric=FIRST_RE.fullmatch(first)
        if numeric:
            point=int(numeric[1])*1000+int(numeric[2])
            if scope.interval:return scope.interval[0]<=point<=scope.interval[1]
            # A chapter number does not locate a point inside a smaller region.
            raise RegistryError('a local declaration scope requires a declaration first_use')
        if not LABEL_RE.fullmatch(first):raise RegistryError(f'malformed first_use {first!r}')
        if self.index is None:raise RegistryError(f'first_use {first!r} requires a reader declaration index')
        declaration=self.index.unique(first)
        if scope.interval:
            if scope.interval==GLOBAL:return True
            point=self.index.numeric_location(declaration)
            return scope.interval[0]<=point<=scope.interval[1]
        return any(r.start<=declaration.start<r.end for r in scope.regions)

    def overlaps(self,a,b):
        if a.interval and b.interval:return overlap(a.interval,b.interval)
        if a.interval==GLOBAL or b.interval==GLOBAL:return True
        if a.regions and b.regions:
            return any(max(x.start,y.start)<min(x.end,y.end) for x in a.regions for y in b.regions)
        numeric,local=(a,b) if a.interval else (b,a)
        for region in local.regions:
            if region.part is None:return True
            # A region's occupied declarations can span multiple chapters or
            # annex owners. Match every one, rather than its first number only.
            declarations=[d for ds in self.index.labels.values() for d in ds if region.start<=d.start<region.end]
            if not declarations:raise RegistryError('scope region contains no reader declarations: '+region.description)
            for declaration in declarations:
                try:point=self.index.numeric_location(declaration)
                except RegistryError:
                    if numeric.interval[0]//1000<=region.part<=numeric.interval[1]//1000:return True
                else:
                    if numeric.interval[0]<=point<=numeric.interval[1]:return True
        return False

    def authorized_override(self,local,broad):
        scope=local['_scope']
        if not scope.presentation or not scope.regions:return False
        # Exact row selectors prevent a whole presentation from suppressing
        # all global collisions. The bound first-use declaration must lie here.
        for item in scope.overrides:
            if not isinstance(item,dict) or not item.get('reason') or not item.get('source'):
                raise RegistryError('override lacks source/reason in '+scope.raw)
            if item.get('glyph')!=local['glyph'] or item.get('local_role')!=local['role'] or item.get('first_use')!=local['first_use']:
                continue
            if item.get('broader_scope')!=broad['scope'] or item.get('broader_role')!=broad['role']:
                continue
            if not self.contains(scope,item['first_use']):raise RegistryError('override declaration lies outside its scope')
            broader=broad['_scope']
            if broader.interval==GLOBAL:return True
            if broader.interval:
                for region in scope.regions:
                    for ds in self.index.labels.values():
                        for d in ds:
                            if region.start<=d.start<region.end:
                                point=self.index.numeric_location(d)
                                if not broader.interval[0]<=point<=broader.interval[1]:return False
                return True
            return all(any(b.start<=r.start and r.end<=b.end for b in broader.regions) for r in scope.regions)
        return False


def read_rows(path: Path, *, resolver=None, base=None):
    path=Path(path); errors=[]; rows=[]
    if base is None and path.parent.name=='registry':base=path.parent.parent
    try:resolver=resolver or Resolver(base)
    except (OSError,ValueError) as exc:return [],[str(exc)]
    try:
        with path.open(encoding='utf-8-sig',newline='') as stream:
            reader=csv.reader(stream);header=next(reader,None)
            if header!=HEADER:return [],[f'bad header {header!r}; expected {HEADER!r}']
            for line,cells in enumerate(reader,2):
                if not cells or len(cells)==1 and not cells[0].strip():continue
                if len(cells)!=len(HEADER):
                    errors.append(f'line {line}: malformed row ({len(cells)} fields, expected {len(HEADER)})');continue
                row=dict(zip(HEADER,(s.strip() for s in cells)));row['_line']=line
                row['_resolver']=resolver;row['_interval']=parse_scope(row['scope'])
                for col in REQUIRED:
                    if not row[col]:errors.append(f'line {line}: empty required cell {col!r}')
                if not PREC_RE.fullmatch(row['precedence']):errors.append(f'line {line}: malformed precedence {row["precedence"]!r}')
                try:
                    row['_scope']=resolver.resolve(row['scope'])
                    if not resolver.contains(row['_scope'],row['first_use']):
                        errors.append(f'line {line}: first_use {row["first_use"]!r} outside scope {row["scope"]!r}')
                except RegistryError as exc:errors.append(f'line {line}: {exc}')
                rows.append(row)
    except (OSError,csv.Error) as exc:errors.append(f'unreadable registry {path}: {exc}')
    if resolver.index:errors.extend(resolver.index.errors)
    return rows,errors


def collision_check(rows):
    errors=[];groups={}
    for row in rows:groups.setdefault(re.sub(r'\s+','',row['glyph']),[]).append(row)
    for entries in groups.values():
        for i,a in enumerate(entries):
            for b in entries[i+1:]:
                if '_scope' not in a or '_scope' not in b:continue
                resolver=a['_resolver']
                try:
                    if not resolver.overlaps(a['_scope'],b['_scope']):continue
                    if a['role']!=b['role'] and (resolver.authorized_override(a,b) or resolver.authorized_override(b,a)):continue
                    kind='duplicate glyph-role' if a['role']==b['role'] else 'glyph-role collision'
                    errors.append(f'lines {a["_line"]}/{b["_line"]}: {kind} for glyph {a["glyph"]!r} in overlapping scopes {a["scope"]!r}/{b["scope"]!r} (roles {a["role"]!r} vs {b["role"]!r})')
                except RegistryError as exc:errors.append(f'lines {a["_line"]}/{b["_line"]}: {exc}')
    return errors


def first_use_tex(row):
    value=row['first_use']
    if LABEL_RE.fullmatch(value):
        return rf'\hyperref[{value}]{{\ref*{{{value}}}}}'
    return value


def scope_tex(row):
    value=row['scope']
    if LABEL_RE.fullmatch(value):return rf'\hyperref[{value}]{{\ref*{{{value}}}}}'
    if ' through ' in value:
        parts=value.split(' through ')
        if len(parts)==2 and all(LABEL_RE.fullmatch(p) for p in parts):
            return '--'.join(rf'\hyperref[{p}]{{\ref*{{{p}}}}}' for p in parts)
    if parse_scope(value):return value
    # Alias names are data, not trusted TeX. Braces and backslashes cannot be
    # allowed to break the literal wrapper; the explicit binding owns the name.
    escapes={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','_':r'\_','%':r'\%','&':r'\&','#':r'\#','$':r'\$','^':r'\textasciicircum{}','~':r'\textasciitilde{}'}
    return ''.join(escapes.get(c,c) for c in value)


# Body notation lint.  The reader index records, for every routed file, the
# reader position and chapter in effect between consecutive commands, so a
# notation use inside a file is located in the same order as the declarations
# that bound registry scopes.  Coverage is stated by the two atom classes the
# lint checks: typeface letters (\mathcal, \mathfrak, \mathbb, \mathscr, with
# \Meta read as \mathcal M) against the registry's macro column, and bar
# expressions against the roles of the in-scope bar rows.
FONT_ATOM = re.compile(r'\\(mathcal|mathfrak|mathbb|mathscr)\s*(?:\{\s*([A-Za-z])\s*\}|([A-Za-z]))')
META_ATOM = re.compile(r'\\Meta(?![A-Za-z])')
MATH_SPAN = re.compile(
    r'\\\((?P<a>.*?)\\\)|\\\[(?P<b>.*?)\\\]|\$\$(?P<c>.*?)\$\$|(?<![\\$])\$(?P<d>[^$]+?)\$'
    r'|\\begin\{(?P<env>equation|align|alignat|gather|multline|flalign|eqnarray|displaymath|math)(?P<star>\*?)\}'
    r'(?P<e>.*?)\\end\{(?P=env)(?P=star)\}', re.S)
STRUCTURE_ROLE = re.compile(r'\bstructures?\b', re.I)
# A bar row records a domain role when its role names the value of the bars
# as a domain, universe or carrier (for example 'universe of a parameter
# system'); a role that merely mentions a domain elsewhere does not.
DOMAIN_ROLE = re.compile(r'^\s*(?:the\s+)?(?:domains?|universes?|carriers?)\b', re.I)
OPEN_BAR = re.compile(r'\\abs\s*\{|\\left\s*(?:\\lvert(?![A-Za-z])|\\vert(?![A-Za-z])|\|)|\\lvert(?![A-Za-z])')
RAW_BAR_ATOM = re.compile(
    r'(?<![\\|])\|\s*((?:\\Meta(?![A-Za-z])|\\(?:mathcal|mathfrak|mathbb|mathscr)\s*(?:\{\s*[A-Za-z]\s*\}|[A-Za-z]))'
    r'(?:\s*[_^]\s*(?:\{[^{}]*\}|\\?[A-Za-z0-9]))*)\s*\|(?!\|)')


def notation_atoms(text):
    """(offset, atom) for every typeface-letter atom in text."""
    for match in FONT_ATOM.finditer(text):
        yield match.start(), '\\%s{%s}' % (match[1], match[2] or match[3])
    for match in META_ATOM.finditer(text):
        yield match.start(), '\\mathcal{M}'


def math_spans(text):
    for match in MATH_SPAN.finditer(text):
        for group in 'abcde':
            if match.group(group) is not None:
                yield match.start(group), match.group(group)
                break


def _bar_operands(math):
    """(offset, operand, form) for bar expressions whose extent is certain."""
    for match in OPEN_BAR.finditer(math):
        if match[0].startswith('\\abs'):
            args, _ = _grammar().scan_braced_args(math, match.end() - 1, 1)
            if args:
                yield match.start(), args[0], '\\abs'
            continue
        left = match[0].startswith('\\left')
        closer = re.compile(r'\\right\s*(?:\\rvert(?![A-Za-z])|\\vert(?![A-Za-z])|\|)' if left else r'\\rvert(?![A-Za-z])')
        opener = re.compile(r'\\left\s*(?:\\lvert(?![A-Za-z])|\\vert(?![A-Za-z])|\|)' if left else r'\\lvert(?![A-Za-z])')
        depth, cursor = 1, match.end()
        while depth:
            o, c = opener.search(math, cursor), closer.search(math, cursor)
            if c is None:
                break
            if o is not None and o.start() < c.start():
                depth, cursor = depth + 1, o.end()
            else:
                depth, cursor = depth - 1, c.end()
                if not depth:
                    yield match.start(), math[match.end():c.start()], '\\left|' if left else '\\lvert'
    for match in RAW_BAR_ATOM.finditer(math):
        yield match.start(), match[1], '|'


def _locate(marks, offset):
    keys = [m[0] for m in marks]
    return marks[min(bisect.bisect_left(keys, offset), len(marks) - 1)]


def _in_scope(row, visit, mark):
    scope = row.get('_scope')
    if scope is None:
        return False
    _, position, chapter = mark
    if scope.interval:
        if scope.interval == GLOBAL:
            return True
        part = visit['part']
        if part is None:
            return False
        if chapter is None:
            # Annex and apparatus files carry no body chapter number; a part
            # interval is matched at part level.
            return scope.interval[0] // 1000 <= part <= scope.interval[1] // 1000
        return scope.interval[0] <= part * 1000 + chapter <= scope.interval[1]
    return any(r.start <= position < r.end for r in scope.regions)


def notation_lint(rows):
    """Check routed body and annex notation against the registry.

    Returns (kind, message) pairs.  Kinds: notation-unregistered (a typeface
    letter no row registers), notation-scope (registered only in scopes that
    do not contain the use), notation-role (bars around a structure or around
    bars where no in-scope bar row records a domain role).
    """
    if not rows:
        return []
    index = rows[0]['_resolver'].index
    if index is None:
        return [('notation-scope', 'no reader index; the notation lint did not run')]
    by_atom, bar_rows = {}, []
    for row in rows:
        # The macro column names the symbol; a row whose macro is a handbook
        # command (such as the natural-number macro) is indexed by the
        # typeface letters of its glyph.
        atoms = {a for _, a in notation_atoms(row['macro'])} or {a for _, a in notation_atoms(row['glyph'])}
        for atom in atoms:
            by_atom.setdefault(atom, []).append(row)
        if '\\abs' in row['macro'] or '\\lvert' in row['glyph'] or re.search(r'(?<!\\)\|', row['glyph']):
            bar_rows.append(row)
    found = {}

    def note(kind, visit, offset, key, message):
        line = visit['text'].count('\n', 0, offset) + 1
        slot = found.setdefault((kind, visit['path'], key), [line, 0, message])
        slot[1] += 1

    for visit in index.visits:
        text, marks = visit['text'], visit['marks']
        for start, math in math_spans(text):
            for offset, atom in notation_atoms(math):
                mark = _locate(marks, start + offset)
                candidates = by_atom.get(atom, [])
                if not candidates:
                    note('notation-unregistered', visit, start + offset, atom,
                         f'{atom} has no registry row')
                elif not any(_in_scope(r, visit, mark) for r in candidates):
                    note('notation-scope', visit, start + offset, atom,
                         f'{atom} is registered only in scopes '
                         + ', '.join(sorted({r["scope"] for r in candidates})[:4])
                         + ' (lines ' + ','.join(str(r['_line']) for r in candidates[:4]) + ')')
            for offset, operand, form in _bar_operands(math):
                mark = _locate(marks, start + offset)
                in_scope = [r for r in bar_rows if _in_scope(r, visit, mark)]
                if any(DOMAIN_ROLE.search(r['role']) for r in in_scope):
                    continue
                roles = '; '.join(sorted({f'{r["role"]} (line {r["_line"]})' for r in in_scope})[:3]) or 'none'
                nested = OPEN_BAR.search(operand) or RAW_BAR_ATOM.search(operand)
                core = re.sub(r'(?:\s*[_^]\s*(?:\{[^{}]*\}|\\?[A-Za-z0-9]))+$', '', operand.strip().strip('{}').strip())
                atoms = list(notation_atoms(core))
                structure = (len(atoms) == 1 and re.fullmatch(r'\\Meta|\\(?:mathcal|mathfrak|mathbb|mathscr)\s*(?:\{\s*[A-Za-z]\s*\}|[A-Za-z])', core)
                             and any(STRUCTURE_ROLE.search(r['role']) and _in_scope(r, visit, mark) for r in by_atom.get(atoms[0][1], [])))
                if nested:
                    note('notation-role', visit, start + offset, 'nested:' + operand.strip(),
                         f'nested bars {form}{{{operand.strip()}}}; in-scope bar roles: {roles}')
                elif structure:
                    note('notation-role', visit, start + offset, 'structure:' + core,
                         f'bars {form} enclose the structure {core}; in-scope bar roles: {roles}; write \\dom{core} or register a typed scoped domain role')
    return [(kind, f'{path}:{line}: {message}' + (f' ({count} uses)' if count > 1 else ''))
            for (kind, path, _), (line, count, message) in sorted(found.items(), key=lambda item: (item[0][1], item[1][0]))]


def _notation_lint_selftest():
    class _Res:
        index = None
    visit = {'path': 'parts/p02/x.tex', 'part': 2, 'zone': 'parts',
             'text': r'a \(\abs{\Meta}\) and \(\abs{\abs{\mathcal N}}\) and \(\abs{\dom\mathcal M}\) and \(\mathfrak Q\)',
             'marks': [(10 ** 6, 5, 1)]}

    class _Index:
        visits = [visit]
    res = _Res(); res.index = _Index()
    glob = Scope('global', interval=GLOBAL)
    rows = [
        {'glyph': r'\(|X|\)', 'macro': r'\abs', 'role': 'cardinality', 'scope': 'global', '_scope': glob, '_line': 41, '_resolver': res},
        {'glyph': r'\(\mathcal M,\mathcal N\)', 'macro': r'\mathcal M,\mathcal N', 'role': 'structures', 'scope': 'global', '_scope': glob, '_line': 22, '_resolver': res},
    ]
    out = notation_lint(rows)
    kinds = sorted(k for k, _ in out)
    assert kinds == ['notation-role'] * 3 + ['notation-unregistered'], out
    rows.append({'glyph': r'\(|A|\)', 'macro': r'|A|', 'role': 'universe of a structure', 'scope': 'global', '_scope': glob, '_line': 99, '_resolver': res})
    assert sorted(k for k, _ in notation_lint(rows)) == ['notation-unregistered']


# First-use check.  A row's first_use anchor is genuine when no routed use of
# the row's symbol inside the row's scope comes before the anchor's
# declaration in reader order.  A use is attributed to a row only when that
# row is the single in-scope row for the atom, so uses that a more local row
# could own are not read as uses of the broader one.  Atoms: the typeface
# letters of the row (as in notation_lint) and the handbook-defined commands
# named in its macro column.
HANDBOOK_COMMAND = re.compile(
    r'\\(?:newcommand|renewcommand|providecommand|DeclareMathOperator|NewDocumentCommand|DeclareDocumentCommand)\*?\s*\{?\s*\\([A-Za-z]+)')
CONTROL_WORD = re.compile(r'\\([A-Za-z]+)')


def handbook_commands(base):
    """Handbook-defined command names, each with the typeface atom its body
    consists of (for example the natural-number macro), or None."""
    names = {}
    for path in sorted(Path(base).glob('*.sty')):
        text = path.read_text(encoding='utf-8-sig')
        for match in HANDBOOK_COMMAND.finditer(text):
            args, _ = _grammar().scan_braced_args(text, match.end() + (1 if text[match.end():match.end() + 1] == '}' else 0), 1)
            # A restoration-only spelling (an error outside inherited scopes)
            # spells the letter that follows its guard.
            body = re.sub(r'(?<!\\)%[^\n]*', '', args[0] if args else '')
            body = re.sub(r'\\ifhb@inheritedrestoration.*?\\fi', '', body, flags=re.S).strip()
            atoms = [a for _, a in notation_atoms(body)]
            letter = atoms[0] if len(atoms) == 1 and FONT_ATOM.fullmatch(body) else None
            names.setdefault(match[1], letter)
    return names


def _row_atoms(row, commands):
    """The row's own symbol: typeface letters of its macro column, else the
    handbook commands it names (with the letter such a command spells)."""
    # Only bare letters name the row's symbol: a decorated letter such as a
    # letter with a superscript, or a quotient of letters, is another symbol.
    items = [item.strip() for item in row['macro'].split(',')]
    atoms = {a for item in items if FONT_ATOM.fullmatch(item) for _, a in notation_atoms(item)}
    if atoms or any(notation_atoms(row['macro'])):
        return atoms
    for name in CONTROL_WORD.findall(row['macro']):
        if name in commands and name != 'Meta':
            atoms.add('\\' + name)
            if commands[name]:
                atoms.add(commands[name])
    return atoms


def _span_atoms(math, commands):
    yield from notation_atoms(math)
    for match in CONTROL_WORD.finditer(math):
        if match[1] in commands and match[1] != 'Meta':
            yield match.start(), '\\' + match[1]
            if commands[match[1]]:
                # A command whose body is one typeface letter spells that letter.
                yield match.start(), commands[match[1]]


def _innermost_label(index, position):
    """Label of the innermost labelled heading or environment containing a
    reader position, or None."""
    best = None
    for label, sites in index.labels.items():
        if len(sites) == 1 and sites[0].kind != 'label' and sites[0].start <= position < sites[0].end:
            if best is None or sites[0].start > best[1].start:
                best = (label, sites[0])
    return best[0] if best else None


def first_use_lint(rows, commands=None):
    """(kind, message) pairs: first-use-late when a row's symbol is used in its
    scope before its first_use declaration; the message names the earliest use
    and the innermost labelled declaration containing it."""
    if not rows:
        return []
    index = rows[0]['_resolver'].index
    if index is None:
        return [('first-use-late', 'no reader index; the first-use check did not run')]
    commands = handbook_commands(index.base) if commands is None else commands
    by_atom = {}
    for row in rows:
        for atom in _row_atoms(row, commands):
            by_atom.setdefault(atom, []).append(row)
    earliest = {}
    for visit in index.visits:
        text, marks = visit['text'], visit['marks']
        for start, math in math_spans(text):
            for offset, atom in _span_atoms(math, commands):
                candidates = by_atom.get(atom)
                if not candidates:
                    continue
                mark = _locate(marks, start + offset)
                in_scope = [r for r in candidates if _in_scope(r, visit, mark)]
                if len(in_scope) != 1:
                    continue
                key = in_scope[0]['_line']
                if key not in earliest or mark[1] < earliest[key][0]:
                    earliest[key] = (mark[1], visit['path'], text.count('\n', 0, start + offset) + 1, atom, in_scope[0])
    out = []
    for key in sorted(earliest):
        position, path, line, atom, row = earliest[key]
        if not LABEL_RE.fullmatch(row['first_use']):
            continue
        try:
            anchor = index.unique(row['first_use'])
        except RegistryError:
            continue  # read_rows reports an unresolved first_use
        if position >= anchor.start:
            continue
        target = _innermost_label(index, position)
        try:
            ok = target is not None and row['_resolver'].contains(row['_scope'], target)
        except RegistryError:
            ok = False
        hint = f'; earliest containing declaration {target}' if ok else '; no labelled declaration in scope contains it'
        out.append(('first-use-late', f'registry line {key}: {atom} is used at {path}:{line} '
                    f'before first_use {row["first_use"]} ({anchor.path}:{anchor.line}){hint}'))
    return out


def _first_use_selftest():
    early = Declaration('sec:early', 'parts/p01/x.tex', 1, 1, 1, 5, 9, 'section')
    late = Declaration('sec:late', 'parts/p01/x.tex', 9, 1, 1, 20, 30, 'section')

    class _Index:
        base = Path('first-use-selftest-has-no-files')
        labels = {'sec:early': [early], 'sec:late': [late]}
        visits = [{'path': 'parts/p01/x.tex', 'part': 1, 'zone': 'parts',
                   'text': r'a \(\dom\mathcal M\) b', 'marks': [(10 ** 6, 6, 1)]}]

        def unique(self, label):
            return ReaderIndex.unique(self, label)
    res = Resolver(index=_Index())
    glob = Scope('global', interval=GLOBAL)
    dom = {'glyph': r'\(\operatorname{dom}X\)', 'macro': r'\dom', 'role': 'domain operator', 'scope': 'global',
           'first_use': 'sec:late', '_scope': glob, '_line': 23, '_resolver': res}
    out = first_use_lint([dom], commands={'dom': None})
    assert [k for k, _ in out] == ['first-use-late'] and 'sec:early' in out[0][1], out
    assert first_use_lint([dict(dom, first_use='sec:early')], commands={'dom': None}) == []
    # Two in-scope rows for one letter: the use is attributed to neither.
    structures = {'glyph': r'\(\mathcal M\)', 'macro': r'\mathcal M', 'role': 'structures', 'scope': 'global',
                  'first_use': 'sec:late', '_scope': glob, '_line': 22, '_resolver': res}
    other = dict(structures, role='another role', _line=99)
    assert first_use_lint([structures, other], commands={}) == []
    assert [k for k, _ in first_use_lint([structures], commands={})] == ['first-use-late']


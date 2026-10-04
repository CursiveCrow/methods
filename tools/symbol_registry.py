"""Shared, strict symbol-row validation and reader-region resolution.

The CSV keeps its seven public fields. Numeric scopes retain their old meaning;
labels resolve on the literal reader input route. Named source scopes and any
exception to a broader role require explicit bindings in symbol-scopes.json.
Unknown text is never interpreted as global or as a disjoint namespace.
"""
from __future__ import annotations

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
        consumed=0
        for match in self.COMMAND.finditer(text):
            if match.start()<consumed:
                continue
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

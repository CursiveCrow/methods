"""Prepare NEW batch5 only; read canonical files, write only adjacent proposals.

No driver/manuscript/canonical/ledger modifications. Existing batch3 helper
parsers are reused without calling its main or regenerating old proposals.
Root supplies decisions through an adjacent JSON file; original intakes stay
immutable. Default proposals hold actual overlaps and record alias candidates.
"""
from __future__ import annotations
import argparse, copy, csv, hashlib, importlib.util, io, json, re, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
BASE=ROOT/'handbook'
PREFIX='oct3-batch5-proposal-'
sys.path.insert(0,str(ROOT/'tools'))
import symbol_registry as registry
import check as grammar
spec=importlib.util.spec_from_file_location('previous_intake_preparation',OUT/'prepare_oct3_intakes.py')
previous=importlib.util.module_from_spec(spec)
spec.loader.exec_module(previous)
FIELDS=registry.HEADER
sha=previous.sha
read=previous.read
def bib_records(text):
    records=previous.bib_records(text)
    for record in records:
        # Percent-encoded URL bytes are data, not TeX comment boundaries.
        # Compare the complete raw record after whitespace normalization.
        record['comparison']=re.sub(r'\s+',' ',record['raw']).strip()
    return records
csv_lines=previous.csv_lines
tuple_row=previous.tuple_row
public=previous.public
rid=previous.rid

def save(name,data):
    path=OUT/(PREFIX+name+'.json')
    assert path.parent==OUT and path.name.startswith(PREFIX)
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return path.name

def replacement_chunks(kind,target,pairs):
    names=[];sizes={};units=[]
    for old,new in pairs:
        if old==new:continue
        units.append('@@\n'+'\n'.join('-'+x for x in old.splitlines())+'\n'+'\n'.join('+'+x for x in new.splitlines())+'\n')
    batch=[]
    def flush():
        nonlocal batch
        if not batch:return
        text='*** Begin Patch\n*** Update File: '+target.as_posix()+'\n'+''.join(batch)+'*** End Patch\n'
        if len(text)>=8000:raise ValueError((kind,'replacement exceeds limit',len(text)))
        name=PREFIX+kind+'-%02d.patch'%(len(names)+1);(OUT/name).write_text(text,encoding='utf-8');names.append(name);sizes[name]=len(text);batch=[]
    for unit in units:
        if batch and sum(map(len,batch))+len(unit)+200>=7800:flush()
        batch.append(unit)
    flush();return names,sizes

def update_record(rec,updates):
    raw=rec['raw'];replacements=[];missing={}
    for field,value in updates.items():
        match=re.search(r'(?m)\b'+re.escape(field)+r'\s*=\s*',raw)
        if match:
            start=match.end();args,end=grammar.scan_braced_args(raw,start,1)
            if not args:raise ValueError('Metadata field is not braced: '+field)
            replacements.append((start,end,'{'+value+'}'))
        else:missing[field]=value
    for start,end,value in sorted(replacements,reverse=True):raw=raw[:start]+value+raw[end:]
    if missing:
        head=raw[:-1].rstrip();head+=('\n' if head.endswith(',') else ',\n')
        raw=head+''.join('  '+key+' = {'+value+'},\n' for key,value in missing.items())+'}'
    return bib_records(raw)[0]

def fields(record):
    raw=record['raw']; cursor=raw.index(',')+1; found={}
    while cursor<len(raw)-1:
        m=re.match(r'\s*,?\s*([A-Za-z]+)\s*=\s*',raw[cursor:])
        if not m: break
        key=m[1].lower(); cursor+=m.end()
        if raw[cursor]=='{':
            args,end=grammar.scan_braced_args(raw,cursor,1)
            if not args:raise ValueError('Unbalanced field '+key)
            value=args[0];cursor=end
        elif raw[cursor]=='"':
            end=cursor+1
            while end<len(raw) and (raw[end]!='"' or raw[end-1]=='\\'):end+=1
            value=raw[cursor+1:end];cursor=end+1
        else:
            end=raw.find(',',cursor)
            if end<0:end=len(raw)-1
            value=raw[cursor:end].strip();cursor=end
        found[key]=re.sub(r'\s+',' ',value).strip()
    return found

def locators(record):
    f=fields(record); result=[]
    if f.get('doi'):result.append('doi:'+f['doi'].lower())
    for k in ('eprint','url'):
        for x in re.findall(r'\b\d{4}\.\d{4,5}v\d+\b',f.get(k,'')):result.append('arxiv:'+x)
        for x in re.findall(r'\b[a-f0-9]{40}\b',f.get(k,'')):result.append('commit:'+x)
    return sorted(set(result))

def visible_glyph(text):
    text=text.strip()
    if text.startswith(r'\(') and text.endswith(r'\)'):text=text[2:-2]
    if text.startswith('$') and text.endswith('$'):text=text[1:-1]
    return re.sub(r'\s+','',text)

def chunks(kind,target,anchor,units,json_members=False):
    names=[];sizes={};current=anchor;batch=[]
    def render(old,chosen):
        if json_members:
            new=old+',\n'+',\n'.join(chosen)
            hunk='\n'.join('-'+x for x in old.splitlines())+'\n'+'\n'.join('+'+x for x in new.splitlines())
        else:hunk='\n'.join(' '+x for x in old.splitlines())+'\n'+'\n'.join('+'+x for x in '\n'.join(chosen).splitlines())
        return '*** Begin Patch\n*** Update File: '+target.as_posix()+'\n@@\n'+hunk+'\n*** End Patch\n'
    def flush():
        nonlocal current,batch
        if not batch:return
        text=render(current,batch)
        if len(text)>=8000:raise ValueError((kind,'unit exceeds chunk limit',len(text)))
        name=PREFIX+'cumulative-'+kind+'-%02d.patch'%(len(names)+1)
        (OUT/name).write_text(text,encoding='utf-8');names.append(name);sizes[name]=len(text)
        current=batch[-1] if kind in {'bib','scopes'} else batch[-1].splitlines()[-1]
        batch=[]
    for unit in units:
        if batch and len(render(current,batch+[unit]))>=7800:flush()
        batch.append(unit)
    flush();return names,sizes

def capture_pre_route():
    path=OUT/(PREFIX+'pre-route-numeric-bindings.json')
    if path.exists():return json.loads(read(path))
    idx=registry.ReaderIndex(BASE)
    rows=list(csv.DictReader(io.StringIO(read(BASE/'registry/symbols.csv'))))
    chapters=[]
    for h in idx.heading_records:
        if h.kind!='chapter' or h.chapter is None or h.part is None:continue
        labels=[d for ds in idx.labels.values() for d in ds if d.path==h.path and d.start==h.start and d.kind=='chapter']
        inside=sorted([d for ds in idx.labels.values() for d in ds if h.start<=d.start<h.end],key=lambda d:d.start)
        selectors=[{'anchor':labels[0].label}] if labels else ([{'heading_of':inside[0].label,'level':'chapter'}] if inside else [])
        valid=[d for d in inside if registry.LABEL_RE.fullmatch(d.label) and len(idx.labels.get(d.label,[]))==1]
        first=labels[0].label if labels and registry.LABEL_RE.fullmatch(labels[0].label) else (valid[0].label if valid else None)
        chapters.append({'part':h.part,'chapter':h.chapter,'path':h.path,'line':h.line,'start':h.start,'end':h.end,'selectors':selectors,'valid_first_use':first})
    numeric=[]
    for line,r in enumerate(rows,2):
        interval=registry.parse_scope(r['scope'])
        if not interval or interval==registry.GLOBAL:continue
        occupied=[c for c in chapters if interval[0]<=c['part']*1000+c['chapter']<=interval[1]]
        m=registry.FIRST_RE.fullmatch(r['first_use']);first=r['first_use'] if not m else None
        if m:
            at=[c for c in chapters if c['part']==int(m[1]) and c['chapter']==int(m[2])]
            if len(at)==1:first=at[0]['valid_first_use']
        numeric.append({'canonical_line':line,'original':r,'interval':list(interval),'old_chapters':occupied,'proposed_first_use':first,'standing':'Actual postB4/preB5 chapter-level meaning; valid descendant locators do not assert a new exact first glyph occurrence.'})
    canonical=[BASE/'registry/symbols.csv',BASE/'registry/symbol-scopes.json',BASE/'bib/handbook.bib']
    payload={'utc':datetime.now(timezone.utc).isoformat(),'canonical_symbols_sha256':sha(canonical[0]),'canonical_scopes_sha256':sha(canonical[1]),'canonical_bib_sha256':sha(canonical[2]),'canonical_row_count':len(rows),'canonical_text':{p.relative_to(ROOT).as_posix():read(p) for p in canonical},'route_sha256':{p:sha(BASE/p) for p in sorted(idx.files) if (BASE/p).is_file()},'reader_index_errors':idx.errors,'chapters':chapters,'numeric_rows':numeric,'standing':'Frozen actual postB4 graph BEFORE any B5 routes. Includes fragment-hosted body chapters. Existing named and global scopes are not retargeted. Original intakes/source bytes untouched.'}
    save('pre-route-numeric-bindings',payload)
    return payload

def propose_numeric_migrations(frozen,current_index):
    """Compare old numeric occupancy to current actual anchors, no rank guesses."""
    proposals=[];unresolved=[];same=0
    for item in frozen['numeric_rows']:
        original=item['original'];interval=item['interval']
        # A whole-part range retains its scope, but a numeric first-use point
        # can still need its actual old anchor after chapter insertion.
        shifted=False;first_shifted=False;regions=[];identities=[]
        for chapter in item['old_chapters']:
            if not chapter['selectors']:
                unresolved.append({'line':item['canonical_line'],'scope':original['scope'],'old_chapter':chapter,'error':'No old literal anchor'});continue
            selector=chapter['selectors'][0];label=selector.get('anchor',selector.get('heading_of'))
            try:
                d=current_index.unique(label);now=current_index.numeric_location(d)
                old=chapter['part']*1000+chapter['chapter']
                # Interior chapter movement does not alter an open whole-part
                # numeric range. Only a finite endpoint's identity can shift
                # its numeric meaning (plus an independently numeric first-use).
                if now!=old and old in interval:shifted=True
                identities.append({'anchor':label,'old_part':chapter['part'],'old_chapter':chapter['chapter'],'current_part':now//1000,'current_chapter':now%1000,'path':chapter['path']})
                regions.append(selector)
                for ds in current_index.labels.values():
                    for a in ds:
                        if a.kind=='annexitem' and a.owner:
                            owner=current_index.unique(a.owner)
                            if owner.part==d.part and current_index.numeric_location(owner)==now:regions.append({'anchor':a.label})
            except registry.RegistryError as e:unresolved.append({'line':item['canonical_line'],'scope':original['scope'],'error':str(e)})
        numeric_first=registry.FIRST_RE.fullmatch(original['first_use'])
        if numeric_first and item['proposed_first_use']:
            try:
                first_now=current_index.numeric_location(current_index.unique(item['proposed_first_use']))
                first_old=int(numeric_first[1])*1000+int(numeric_first[2])
                if first_now!=first_old:first_shifted=True
            except registry.RegistryError as e:unresolved.append({'line':item['canonical_line'],'error':str(e)})
        if not shifted and not first_shifted:same+=1;continue
        # Compress genuinely whole-part portions using their real driver files,
        # retaining individually anchored chapter-boundary portions. This does
        # not invent a disjoint namespace or suppress any typed overlap.
        for part in {c['part'] for c in item['old_chapters']}:
            all_part=[c for c in frozen['chapters'] if c['part']==part]
            chosen=[c for c in item['old_chapters'] if c['part']==part]
            if len(all_part)!=len(chosen) or not all_part:continue
            wrappers=[]
            for zone in ('parts/','annex/'):
                options=[(sites[0].end-sites[0].start,rel,sites[0]) for rel,sites in current_index.files.items() if rel.startswith(zone) and len(sites)==1 and sites[0].part==part]
                if options:wrappers.append(max(options,key=lambda x:x[0]))
            if not wrappers:continue
            kept=[]
            for selector in regions:
                try:reg=current_index.region(selector)
                except registry.RegistryError:kept.append(selector);continue
                if reg.part!=part:kept.append(selector)
            regions=kept+[{'file':x[1]} for x in wrappers]
        # An entire reciprocal annex file can replace its individual items
        # only when EVERY owner in that actual file belongs to the selected
        # old chapter identities. No source family gets a fabricated region.
        positions={(x['current_part'],x['current_chapter']) for x in identities}
        paths={d.path for r in regions if set(r)=={'anchor'} for d in current_index.labels.get(r['anchor'],[]) if d.path.startswith('annex/')}
        compressible=set()
        for path in paths:
            items=[a for ds in current_index.labels.values() for a in ds if a.kind=='annexitem' and a.path==path]
            if not items or any(not a.owner for a in items) or len(current_index.files.get(path,[]))!=1:continue
            if not all((current_index.numeric_location(a)//1000,current_index.numeric_location(a)%1000) in positions for a in items):continue
            compressible.add(path)
        kept=[]
        for selector in regions:
            sites=current_index.labels.get(selector.get('anchor'),[])
            if set(selector)=={'anchor'} and sites and all(d.path in compressible for d in sites):continue
            kept.append(selector)
        regions=kept+[{'file':path} for path in sorted(compressible)]
        name='Legacy pre-batch5 '+original['scope']+' reader meaning'
        proposed=copy.deepcopy(original)
        if shifted:proposed['scope']=name
        if numeric_first and (shifted or first_shifted):
            if not item['proposed_first_use']:
                unresolved.append({'line':item['canonical_line'],'error':'Cannot migrate numeric first use to unique actual old anchor'});continue
            proposed['first_use']=item['proposed_first_use']
        proposed['notes']+=(' ' if proposed['notes'] else '')+' Numeric chapter scope migrated to its frozen pre-batch5 source-labelled reader regions; glyph, role and precedence unchanged.'
        regions=list({json.dumps(r,sort_keys=True):r for r in regions}.values())
        proposals.append({'canonical_line':item['canonical_line'],'original':original,'proposed':proposed,'chapter_identity_changes':identities,'binding':({'presentation':'Exact frozen reader meaning of '+original['scope']+' before batch5 chapter insertion; not a fresh source or role admission','regions':regions} if shifted else None),'standing':'Scope rebound only when a finite endpoint moved; first-use-only changes preserve the existing scope.'})
    result={'utc':datetime.now(timezone.utc).isoformat(),'frozen_snapshot_utc':frozen['utc'],'frozen_symbols_sha256':frozen['canonical_symbols_sha256'],'current_symbols_sha256':sha(BASE/'registry/symbols.csv'),'proposed_migration_rows':proposals,'unchanged_numeric_rows_examined':same,'unresolved':unresolved,'standing':'ROOT DECISION REQUIRED. Only actual old chapter identities that moved are proposed for rebinding; whole-part/global/existing named scopes untouched. This is not a canonical patch or proof review.'}
    save('numeric-migrations',result)
    return result

def complete_frozen_numeric_meanings(frozen,groups):
    """B5 snapshot already captures fragment-hosted chapters; no reconstruction."""
    return frozen


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--decisions',type=Path,help='Root-owned decision JSON; only explicit exact-row reuse/override and bib actions')
    ap.add_argument('--diagnostics-only',action='store_true')
    ap.add_argument('--capture-pre-route-only',action='store_true')
    args=ap.parse_args()
    pre_route=capture_pre_route()
    if args.capture_pre_route_only:
        print(json.dumps({'utc':pre_route['utc'],'numeric_row_count':len(pre_route['numeric_rows']),'chapter_count':len(pre_route['chapters']),'canonical_symbols_sha256':pre_route['canonical_symbols_sha256'],'canonical_scopes_sha256':pre_route['canonical_scopes_sha256']}));return
    decisions=json.loads(read(args.decisions)) if args.decisions else {}
    manifest=ROOT/'spec/research/edition-2026-authoring-batch-intake-5.json'
    groups=json.loads(read(manifest))['groups']
    assert len(groups)==11 and sum(len(g['bodies']) for g in groups)==11
    apparatus=json.loads(read(manifest))['root_apparatus']
    groups.append({'stem':apparatus['stem'],'part':apparatus['part'],'bodies':[],'annexes':[],'symbols':False,'note':apparatus['note']})
    pre_route=complete_frozen_numeric_meanings(pre_route,groups)
    canonical=[BASE/'registry/symbols.csv',BASE/'registry/symbol-scopes.json',BASE/'bib/handbook.bib']
    snapshot={p.relative_to(ROOT).as_posix():{'sha256':sha(p),'text':read(p)} for p in canonical}
    old_rows=list(csv.DictReader(io.StringIO(snapshot['handbook/registry/symbols.csv']['text'])))
    old_tuple={tuple_row(r) for r in old_rows}
    bindings=json.loads(snapshot['handbook/registry/symbol-scopes.json']['text'])
    if any(name in bindings['scopes'] for name in ('P3 FV products','P6 cardinal characteristics','P4 represented spaces','P15 Reichenbach')):
        raise ValueError('Batch5 is already partly/fully merged. Do not regenerate or reapply this frozen proposal packet; root must inspect its recorded snapshot/application order.')
    old_bib=bib_records(snapshot['handbook/bib/handbook.bib']['text'])
    index=registry.ReaderIndex(BASE);pending=[];missing=[];issues=[];datasets={};new_scopes={}
    migrations=propose_numeric_migrations(pre_route,index)
    for g in groups:
        for rel in g['bodies']+g['annexes']+g.get('rule_sheets',[]):
            if not (BASE/rel).is_file():missing.append(rel);continue
            if not index.files.get(rel):
                index._close_headings(0);index._visit(rel,int(g['part'][1:]));index._close_headings(0);pending.append(rel)
                for ds in index.labels.values():
                    for d in ds:
                        if d.path==rel:d.chapter=None
                for h in index.heading_records:
                    if h.path==rel:h.chapter=None
                for region in index.files.get(rel,[]):region.chapter=None
    def regions(first,g):
        d=index.unique(first)
        if d.path not in g['bodies']+g['annexes']+g.get('rule_sheets',[]):raise registry.RegistryError('first_use outside owned batch group '+d.path)
        if d.path.startswith('annex/'):
            return [{'anchor':d.label}]+([{'anchor':d.owner}] if d.owner else [])
        hs=[h for h in index.heading_records if h.path==d.path and h.start<=d.start<h.end]
        h=max(hs,key=lambda h:h.start) if hs else None
        result=[{'heading_of':first,'level':h.kind}] if h else [{'anchor':first}]
        region=index.region(result[0])
        for ds in index.labels.values():
            for a in ds:
                if a.kind=='annexitem' and a.owner and a.path in g['annexes']:
                    owner=index.unique(a.owner)
                    if region.start<=owner.start<region.end:result.append({'anchor':a.label})
        return result
    reuse_selectors={(x['group'],x['line']):x for x in decisions.get('reuse_rows',[])}
    for g in groups:
        stem=g['stem'];sp=BASE/('registry/symbols-intake-'+stem+'.csv');bp=BASE/('bib/intake-'+stem+'.bib')
        if (g.get('symbols') is not False and not sp.is_file()) or not bp.is_file():raise ValueError('Missing intake '+stem)
        with (sp.open(encoding='utf-8-sig',newline='') if g.get('symbols') is not False else io.StringIO(','.join(FIELDS)+'\n')) as f:
            reader=csv.DictReader(f)
            if reader.fieldnames!=FIELDS:raise ValueError((sp,'bad header',reader.fieldnames))
            rows=[]
            for line,raw in enumerate(reader,2):
                if None in raw:raise ValueError((sp,line,'malformed field count'))
                r={k:(raw[k] or '').strip() for k in FIELDS};r.update(_group=stem,_line=line,_original=copy.deepcopy(r),_changes=[])
                label_aliases=decisions.get('first_use_aliases',{})
                if r['first_use'] in label_aliases:
                    previous_first=r['first_use'];r['first_use']=label_aliases[previous_first]
                    r['_changes'].append('Root source-label reconciliation '+previous_first+' -> '+r['first_use']+'; original intake preserved.')
                for update in decisions.get('row_updates',[]):
                    if update['group']==stem and update['line']==line:
                        r.update(update['fields'])
                        r['_changes'].append('Root actual declaration-region reconciliation: '+update['reason'])
                if not r['macro']:
                    r['macro']=r['glyph'][2:-2] if r['glyph'].startswith(r'\(') and r['glyph'].endswith(r'\)') else r['glyph']
                    r['_changes'].append('Blank macro filled with exact unchanged glyph spelling; registry data only, not a new TeX command.')
                if not registry.PREC_RE.fullmatch(r['precedence']):
                    r['_changes'].append('Original precedence '+repr(r['precedence'])+' retained as semantic descriptor; n/a is not an invented rank.')
                    r['precedence']='n/a'
                if r['_changes']:r['notes']+=(' ' if r['notes'] else '')+' '.join(r['_changes'])
                r['_already_merged']=tuple_row(r) in old_tuple or tuple_row(raw) in old_tuple
                r['_reuse']=False
                if (stem,line) in reuse_selectors:
                    decision=reuse_selectors[(stem,line)]
                    if decision['incoming']!=r['_original']:raise ValueError('Stale reuse selector '+stem+':'+str(line))
                    matches=[o for o in old_rows if all(o[k]==v for k,v in decision['canonical'].items())]
                    if len(matches)!=1:raise ValueError('Nonunique canonical reuse')
                    r['_reuse']=True
                rows.append(r)
        datasets[stem]={'group':g,'rows':rows,'original_row_count':len(rows),'bib':bib_records(read(bp)),'sp':sp,'bp':bp}
        def child(parent,glyph,macro,role,scope=None,first=None):
            c=copy.deepcopy(parent);c.update(glyph=glyph,macro=macro,role=role)
            c['scope']=scope or parent['scope'];c['first_use']=first or parent['first_use']
            c['_uid']=str(parent['_line'])+':'+glyph+':'+role
            c['notes']+=' Root-authorized typed decomposition; original grouped intake row remains unchanged as evidence.'
            c['_already_merged']=tuple_row(c) in old_tuple
            return c
        transforms=decisions.get('typed_transforms',[])
        if stem=='p06-cardinal-characteristics' and 'cardinal-source-restoration' in transforms:
            changed=[];superseded=[]
            for r in rows:
                if r['_line']==2:
                    for glyph,role in [(r'\(\mathcal N\)','null ideal of arbitrary real subsets'),(r'\(\mathcal M\)','meager ideal of arbitrary real subsets')]:
                        c=child(r,glyph,glyph[2:-2],role,first='def:p06-cc-standing')
                        c['notes']='Root restored actual Fremlin source glyph. Ideal of arbitrary real subsets, explicitly not a structure or ground model. Original I_null/I_meager row is superseded evidence, not active notation.'
                        changed.append(c)
                    superseded.append({'original_line':r['_line'],'original':r['_original'],'decision':'Replace house-renamed ideal family by actual source cal-N and cal-M typed rows.'})
                elif r['_line']==12:
                    superseded.append({'original_line':r['_line'],'original':r['_original'],'decision':'Obsolete plain N/M display aliases removed by root from actual body/annex/diagram; do not append as active glyphs.'})
                else:changed.append(r)
            base=next(r for r in rows if r['_line']==3)
            c=child(base,r'\(\operatorname{cf}(I)\)',r'\operatorname{cf}','Fremlin ideal cofinal-base minimum','P6 cardinal characteristics','def:p06-cc-ideal-four')
            c['notes']='Actual cf(I) source spelling restored beside cof(I); equality uses the SAME ideal and cofinal-base minimum. Ideal argument type differs from ordinal cf(alpha). Original grouped invariant row remains unchanged as evidence.'
            changed.append(c);rows=changed;datasets[stem]['rows']=rows
            save('cardinal-supersessions',{'root_authorization':'Actual source glyph and label corrections supplied by root; frozen raw intake unchanged','superseded':superseded,'active_rows':[public(r) for r in rows]})
        if stem=='p15-carnap-relevance' and 'carnap-four-scalar-cells-and-confirmation-function' in transforms:
            changed=[]
            for r in rows:
                if r['glyph']=='a b c d':
                    for glyph,role in [('a','scalar mass m(eih)'),('b','scalar mass m(ei not-h)'),('c','scalar mass m(e not-i h)'),('d','scalar mass m(e not-i not-h)')]:changed.append(child(r,glyph,glyph,role))
                    function=child(r,'c','c','binary confirmation function','P15 Carnap continuation','sec:p15-carnap-confirmation-relevance-and-reliability')
                    function['notes']='Binary c(h,e)=m(e and h)/m(e), distinct from the scalar c cell by argument type in the SAME theorem. Root-authorized continuation role; source Carnap1950Probability.'
                    changed.append(function)
                else:changed.append(r)
            rows=changed;datasets[stem]['rows']=rows
        if stem=='p13-arabic-originals' and 'street-mode-and-predicate-types' in transforms:
            changed=[]
            for r in rows:
                changed.append(r)
                if r['glyph']==r'\(A\)' and r['role']=='source perpetual mode symbol':
                    for glyph in ('A','B'):
                        c=child(r,r'\('+glyph+r'\)',glyph,'predicate in the source temporal-modal rendition')
                        c['notes']='Actual body426-434 declares A,B predicates while the SAME modal-table region retains A as a mode. Argument/position type distinguishes readings; no artificial disjoint scope.'
                        changed.append(c)
            rows=changed;datasets[stem]['rows']=rows
        if stem=='p07-cchm2016' and 'cchm-glue-operations-and-two-equiv-uses' in transforms:
            changed=[]
            for r in rows:
                if r['glyph']=='Glue glue unglue':
                    for glyph,role in [('Glue','gluing type formation operation'),('glue','gluing term introduction operation'),('unglue','gluing term elimination operation')]:changed.append(child(r,glyph,r'\mathsf{'+glyph+'}',role))
                elif r['glyph']=='equiv':
                    changed.append(child(r,'equiv',r'\mathsf{equiv}','uniform partial-fiber extension operation','P07 CCHM2016 v1 partial fiber extension'))
                    changed.append(child(r,'equiv^i',r'\mathsf{equiv}^{i}','superscripted type-line equivalence construction','P07 CCHM2016 v1 type-line equivalence','sec:p07-cchm2016-universe'))
                else:changed.append(r)
            rows=changed;datasets[stem]['rows']=rows
        by_scope={}
        for r in rows:
            if not r['_already_merged'] and not r['_reuse']:by_scope.setdefault(r['scope'],[]).append(r)
        for name,rs in by_scope.items():
            if registry.parse_scope(name) or registry.LABEL_RE.fullmatch(name) or ' through ' in name or name in bindings['scopes']:continue
            specs=[]
            for r in rs:
                try:specs+=regions(r['first_use'],g)
                except registry.RegistryError as e:issues.append({'group':stem,'line':r['_line'],'kind':'binding-unresolved','error':str(e)})
            specs=list({json.dumps(x,sort_keys=True):x for x in specs}.values())
            if specs:new_scopes[name]={'presentation':'Source-labelled local regions of new batch5 '+stem+'; version and proof admission remain separate','regions':specs}
    # A composed name uses the real constituent union only when both exist.
    pool={**bindings['scopes'],**new_scopes}
    for name,b in new_scopes.items():
        parts=name.split(' and ')
        if len(parts)==2 and all(p in pool for p in parts):b['regions']=list({json.dumps(x,sort_keys=True):x for p in parts for x in pool[p]['regions']}.values())
    for item in decisions.get('scope_bindings',[]):
        if item['scope'] in bindings['scopes']:raise ValueError('Existing scope replacement forbidden')
        new_scopes[item['scope']]=item['binding']
    def exact_override(name,row,broader_scope,broader_role,source,reason):
        rule={'glyph':row['glyph'],'local_role':row['role'],'first_use':row['first_use'],'broader_scope':broader_scope,'broader_role':broader_role,'source':source,'reason':reason}
        new_scopes[name].setdefault('overrides',[]).append(rule)
    if 'carnap-four-scalar-cells-and-confirmation-function' in decisions.get('typed_transforms',[]):
        row=next(r for r in datasets['p15-carnap-relevance']['rows'] if r['glyph']=='c' and r['role']=='scalar mass m(e not-i h)')
        exact_override(row['scope'],row,'P15 Carnap continuation','binary confirmation function','Carnap1950Probability','The SAME four-cell theorem declares scalar c=m(e not-i h) and writes binary confirmation c(h,ei). The scalar-versus-binary function argument type is explicit; root preserves both genuine source uses without fake disjoint regions.')
    if 'street-mode-and-predicate-types' in decisions.get('typed_transforms',[]):
        row=next(r for r in datasets['p13-arabic-originals']['rows'] if r['glyph']==r'\(A\)' and r['role']=='predicate in the source temporal-modal rendition')
        exact_override(row['scope'],row,row['scope'],'source perpetual mode symbol','Street2004ArabicLogicHHL','The SAME modal-table section explicitly uses A as perpetual mode and declares A,B predicates in the 26 temporal renditions. Position and argument type distinguish these readings; root preserves both in this actual region.')
    if 'cchm-glue-operations-and-two-equiv-uses' in decisions.get('typed_transforms',[]):
        name='P07 CCHM2016 v1 partial fiber extension'
        new_scopes[name]['regions']=[{'heading_of':'sec:p07-cchm2016-equivalence','level':'subsection'},{'heading_of':'sec:p07-cchm2016-glue','level':'subsection'},{'anchor':'annex:p07.cchm2016.extension'},{'anchor':'annex:p07.cchm2016.glue-composition'},{'anchor':'annex:p07.cchm2016.unglue'}]
    if 'cardinal-source-restoration' in decisions.get('typed_transforms',[]):
        for row in datasets['p06-cardinal-characteristics']['rows']:
            if row['glyph'] in (r'\(\mathcal N\)',r'\(\mathcal M\)'):
                exact_override(row['scope'],row,'global','structures','Fremlin522Author2023','The actual source/body explicitly types cal-N and cal-M as real null/meager ideals, not models. Global grouped structure glyphs remain unchanged; this exact local ideal role is root-authorized and argument-typed.')
    for item in decisions.get('overrides',[]):
        name=item['scope']; rule=item['rule']
        if name not in new_scopes:
            if name in bindings['scopes']:raise ValueError('Existing scope update held for root')
            new_scopes[name]={'presentation':item['presentation'],'regions':item['regions']}
        new_scopes[name].setdefault('overrides',[]).append(rule)
    combined=copy.deepcopy(bindings);combined['scopes'].update(new_scopes)
    migration_rows={}
    if decisions.get('numeric_migrations'):
        for p in migrations['proposed_migration_rows']:
            migration_rows[p['canonical_line']]=p['proposed']
            if p['binding']:new_scopes.setdefault(p['proposed']['scope'],p['binding'])
        combined['scopes'].update(new_scopes)
    resolver=registry.Resolver(BASE,bindings=combined,index=index)
    resolver.source_keys.update(r['key'] for d in datasets.values() for r in d['bib'])
    parsed_old,canonical_errors=registry.read_rows(BASE/'registry/symbols.csv',resolver=resolver)
    virtual_canonical_errors=[]
    if migration_rows:
        parsed_old=[]
        for line,original in enumerate(old_rows,2):
            r=copy.deepcopy(migration_rows.get(line,original));r.update(_line=line,_resolver=resolver)
            try:
                r['_scope']=resolver.resolve(r['scope'])
                if not resolver.contains(r['_scope'],r['first_use']):raise registry.RegistryError('first_use outside migrated scope')
                parsed_old.append(r)
            except registry.RegistryError as e:virtual_canonical_errors.append('line '+str(line)+': '+str(e))
    all_new=[]
    for stem,d in datasets.items():
        for r in d['rows']:
            if r['_already_merged'] or r['_reuse']:continue
            r['_resolver']=resolver
            try:
                r['_scope']=resolver.resolve(r['scope'])
                if not resolver.contains(r['_scope'],r['first_use']):raise registry.RegistryError('first_use outside scope')
                all_new.append(r)
            except registry.RegistryError as e:issues.append({'group':stem,'line':r['_line'],'kind':'row-unresolved','row':public(r),'error':str(e)})
    glyphs={};collisions=[];held=set()
    for r in parsed_old+all_new:glyphs.setdefault(re.sub(r'\s+','',r['glyph']),[]).append(r)
    for entries in glyphs.values():
        for i,a in enumerate(entries):
            for b in entries[i+1:]:
                if not (a.get('_group') or b.get('_group')) or not resolver.overlaps(a['_scope'],b['_scope']):continue
                if a['role']!=b['role'] and (resolver.authorized_override(a,b) or resolver.authorized_override(b,a)):continue
                for r in (a,b):
                    if r.get('_group'):held.add((r['_group'],rid(r)))
                collisions.append({'glyph':a['glyph'],'kind':'duplicate-role' if a['role']==b['role'] else 'typed-role-overlap','a':{**public(a),'group':a.get('_group','canonical'),'line':a['_line']},'b':{**public(b),'group':b.get('_group','canonical'),'line':b['_line']},'decision':'HELD: actual overlapping regions; root must decide exact typed exception or reuse. No renamed glyph/fake scope.'})
    visible={};wrapper_overlaps=[]
    for r in parsed_old+all_new:visible.setdefault(visible_glyph(r['glyph']),[]).append(r)
    for entries in visible.values():
        for i,a in enumerate(entries):
            for b in entries[i+1:]:
                if not (a.get('_group') or b.get('_group')) or a['glyph']==b['glyph'] or a['role']==b['role']:continue
                if not resolver.overlaps(a['_scope'],b['_scope']):continue
                wrapper_overlaps.append({'a':{**public(a),'group':a.get('_group','canonical'),'line':a['_line']},'b':{**public(b),'group':b.get('_group','canonical'),'line':b['_line']},'standing':'Same visible token with differing math wrappers; strict checker does not compare these spellings. Root decision needed; original glyphs remain unchanged.'})
    grouped=[{'group':r['_group'],'line':r['_line'],'row':public(r),'standing':'Grouped notation-family record, not a single semantic identity. Component roles and any same-region retyping require explicit root decisions; not certified disjoint by the combined glyph string.'} for d in datasets.values() for r in d['rows'] if (',' in visible_glyph(r['glyph']) or ';' in r['macro'] or (re.search(r'\s',r['glyph']) and not r['glyph'].startswith('95%')))]
    save('typed-family-warnings',{'wrapper_overlaps':wrapper_overlaps,'grouped_rows':grouped})
    bykey={};byloc={};bib_decisions=[];aliases=[];new_bib=[]
    for rec in old_bib:
        bykey.setdefault(rec['key'],[]).append(rec)
        for loc in locators(rec):byloc.setdefault(loc,[]).append(rec)
    actions=decisions.get('bib_actions',{});metadata_updates=[]
    metadata=decisions.get('bibliography_metadata',{})
    for rec in old_bib:
        if rec['key'] in metadata:metadata_updates.append((rec['raw'],update_record(rec,metadata[rec['key']])['raw']))
    for stem,d in datasets.items():
        for rec in d['bib']:
            if rec['key'] in metadata:rec=update_record(rec,metadata[rec['key']])
            existing=bykey.get(rec['key'],[])
            if existing:
                identical=any(rec['comparison']==x['comparison'] for x in existing)
                approved=actions.get(rec['key'],{}).get('action')=='reuse'
                bib_decisions.append({'group':stem,'incoming':rec,'existing':existing,'decision':'reuse-root-identified-publication' if approved else ('skip-identical-record' if identical else 'hold-conflicting-key'),'field_comparison':[{'key':x['key'],'existing_fields':fields(x),'incoming_fields':fields(rec)} for x in existing]})
                continue
            candidates={x['key']:x for loc in locators(rec) for x in byloc.get(loc,[])}
            # Exact publication identity tuple supplements missing DOI fields;
            # it is reported for root, never automatic manifestation equivalence.
            incoming_fields=fields(rec)
            identity_names=('author','title','year','pages','booktitle','volume','publisher')
            if all(incoming_fields.get(k) for k in identity_names):
                for previous_record in old_bib:
                    pf=fields(previous_record)
                    if all(pf.get(k)==incoming_fields[k] for k in identity_names):candidates[previous_record['key']]=previous_record
            if candidates:
                aliases.append({'group':stem,'incoming':rec,'incoming_fields':fields(rec),'shared_exact_locators':locators(rec),'candidates':[{'record':x,'fields':fields(x)} for x in candidates.values()],'decision':'CANDIDATE ONLY: matching exact locator or full publication identity tuple; differing notes/manifests need root choice'})
            action=actions.get(rec['key'])
            if action:
                if action['action']=='reuse':
                    if action['canonical_key'] not in bykey:raise ValueError('Unknown bib reuse target')
                    continue
                if action['action']!='append':raise ValueError('Unknown bib action')
            elif candidates:continue
            new_bib.append(rec);bykey[rec['key']]=[rec]
            for loc in locators(rec):byloc.setdefault(loc,[]).append(rec)
    safe=[r for r in all_new if (r['_group'],rid(r)) not in held]
    normalizations=[{'group':r['_group'],'line':r['_line'],'original':r['_original'],'proposed':public(r),'changes':r['_changes']} for d in datasets.values() for r in d['rows'] if r['_changes']]
    files=[]
    for stem,d in datasets.items():
        files.append(save(stem,{'group':d['group'],'inputs':[{'path':p.relative_to(ROOT).as_posix(),'sha256':sha(p)} for p in [d['sp'],d['bp'],ROOT/d['group']['note']] if p.is_file()],'source_region_files':[{'path':'handbook/'+p,'sha256':sha(BASE/p),'route_pending':p in pending} for p in d['group']['bodies']+d['group']['annexes'] if (BASE/p).is_file()],'proposed_rows':[public(r) for r in safe if r['_group']==stem],'held_rows':[public(r) for r in d['rows'] if (stem,rid(r)) in held],'reused_rows':[public(r) for r in d['rows'] if r['_reuse']],'already_merged_lines':[r['_line'] for r in d['rows'] if r['_already_merged']],'total_intake_rows':d['original_row_count'],'transformed_row_count':len(d['rows']),'total_intake_bib_records':len(d['bib'])}))
    files.append(save('scopes',{'append_only_scopes':new_scopes,'pending_routes':pending}))
    files.append(save('normalizations',normalizations))
    files.append(save('bibliography-decisions',{'exact_key_comparisons':bib_decisions,'exact_locator_alias_candidates':aliases,'append_records':new_bib}))
    application_order={};sizes={};replay_errors=[]
    if not args.diagnostics_only:
        names,ss=replacement_chunks('bibliography-metadata',BASE/'bib/handbook.bib',metadata_updates);application_order['bibliography_metadata']=names;sizes.update(ss)
        names,ss=chunks('bib',BASE/'bib/handbook.bib',old_bib[-1]['raw'],[r['raw'] for r in new_bib]);application_order['bib']=names;sizes.update(ss)
        scope_text=snapshot['handbook/registry/symbol-scopes.json']['text'];last=next(reversed(bindings['scopes']));token=json.dumps(last,ensure_ascii=False)
        sites=list(re.finditer(r'(?m)^([ \t]*)'+re.escape(token)+r'\s*:',scope_text))
        if len(sites)!=1:raise ValueError('Canonical tail scope member not unique')
        site=sites[0];start=site.start();at=start+len(site[1]);value=scope_text.index(':',at+len(token))+1
        while scope_text[value].isspace():value+=1
        _,extent=json.JSONDecoder().raw_decode(scope_text[value:]);anchor=scope_text[start:value+extent];prefix=scope_text[start:at]
        members=[prefix+json.dumps(k,ensure_ascii=False)+': '+json.dumps(v,ensure_ascii=False,separators=(',',':')) for k,v in new_scopes.items()]
        names,ss=chunks('scopes',BASE/'registry/symbol-scopes.json',anchor,members,True);application_order['scopes']=names;sizes.update(ss)
        names,ss=chunks('rows',BASE/'registry/symbols.csv',snapshot['handbook/registry/symbols.csv']['text'].rstrip().splitlines()[-1],[csv_lines([r]) for r in safe]);application_order['rows']=names;sizes.update(ss)
        raw_lines=snapshot['handbook/registry/symbols.csv']['text'].splitlines()
        pairs=[(raw_lines[line-1],csv_lines([proposed])) for line,proposed in migration_rows.items()]
        names,ss=replacement_chunks('numeric-row-migration',BASE/'registry/symbols.csv',pairs);application_order['numeric_migrations']=names;sizes.update(ss)
        citation_files=[]
        citation_aliases=decisions.get('citation_aliases',{})
        for g in groups:
            for rel in g['bodies']+g['annexes']:
                text=read(BASE/rel);lines=text.splitlines();new_lines=[];intervals=[]
                for n,line in enumerate(lines):
                    new=line
                    for incoming,canonical_key in citation_aliases.items():new=re.sub(r'\b'+re.escape(incoming)+r'\b',canonical_key,new)
                    new_lines.append(new)
                    if new==line:continue
                    radius=1
                    while True:
                        left=max(0,n-radius);right=min(len(lines),n+radius+1)
                        if text.count('\n'.join(lines[left:right]))==1:break
                        radius+=1
                    if intervals and left<=intervals[-1][1]:intervals[-1][1]=max(right,intervals[-1][1])
                    else:intervals.append([left,right])
                pairs=[('\n'.join(lines[left:right]),'\n'.join(new_lines[left:right])) for left,right in intervals]
                if pairs:
                    names,ss=replacement_chunks('citation-'+g['stem']+'-'+Path(rel).stem+'-'+Path(rel).parent.name,BASE/rel,pairs);citation_files+=names;sizes.update(ss)
        application_order['citation_aliases']=citation_files
        virtual_files={str((ROOT/k).as_posix()):v['text'] for k,v in snapshot.items()}
        for kind,names in application_order.items():
            for name in names:
                patch=read(OUT/name);target=patch.split('*** Update File: ',1)[1].split('\n',1)[0]
                if target not in virtual_files:virtual_files[target]=read(Path(target))
                for block in patch.split('@@\n')[1:]:
                    hunk=block.split('*** End Patch',1)[0].rstrip('\n').splitlines();old='\n'.join(x[1:] for x in hunk if x[:1] in {' ','-'});new='\n'.join(x[1:] for x in hunk if x[:1] in {' ','+'})
                    if virtual_files[target].count(old)!=1:replay_errors.append(name+': ambiguous/missing anchor')
                    else:virtual_files[target]=virtual_files[target].replace(old,new,1)
        try:
            json.loads(virtual_files[(BASE/'registry/symbol-scopes.json').as_posix()]);vr=list(csv.DictReader(io.StringIO(virtual_files[(BASE/'registry/symbols.csv').as_posix()])));vb=bib_records(virtual_files[(BASE/'bib/handbook.bib').as_posix()])
            if len(vr)!=len(old_rows)+len(safe):replay_errors.append('CSV count mismatch')
            if len(vb)!=len(old_bib)+len(new_bib):replay_errors.append('Bib count mismatch')
        except (ValueError,csv.Error) as e:replay_errors.append(str(e))
    after={p.relative_to(ROOT).as_posix():sha(p) for p in canonical}
    summary={'utc':datetime.now(timezone.utc).isoformat(),'manifest_sha256':sha(manifest),'canonical_before':{k:v['sha256'] for k,v in snapshot.items()},'canonical_after':after,'canonical_changed_during_read':[k for k,v in snapshot.items() if v['sha256']!=after[k]],'canonical_row_count':len(old_rows),'canonical_bib_count':len(old_bib),'group_count':len(groups),'body_count':11,'author_group_count':11,'root_apparatus_group_count':1,'intake_row_count':sum(d['original_row_count'] for d in datasets.values()),'transformed_row_count':sum(len(d['rows']) for d in datasets.values()),'intake_bib_count':sum(len(d['bib']) for d in datasets.values()),'proposed_row_count':len(safe),'held_row_count':len(held),'reused_row_count':sum(r['_reuse'] for d in datasets.values() for r in d['rows']),'normalization_count':len(normalizations),'normalized_original_row_count':len({(x['group'],x['line']) for x in normalizations}),'new_scope_count':len(new_scopes),'proposed_bib_count':len(new_bib),'canonical_read_errors':canonical_errors,'virtual_migrated_canonical_errors':virtual_canonical_errors,'virtual_full_collision_errors':registry.collision_check(parsed_old+all_new),'numeric_migration_row_count':len(migration_rows),'reader_index_errors':index.errors,'route_pending_files':pending,'missing_source_region_files':missing,'issues':issues,'collisions':collisions,'wrapper_overlap_count':len(wrapper_overlaps),'grouped_family_count':len(grouped),'bib_duplicate_decisions':bib_decisions,'bib_alias_candidates':aliases,'application_order':application_order,'chunk_characters':sizes,'in_memory_patch_parsing_errors':replay_errors,'files':files,'standing':'New batch5 preparation only. Prospective routes are labelled; no canonical/manuscript writes, source equivalence or proof/admission certification. Only ordered cumulative patch files are applicable; hashes are snapshot-specific.'}
    save('summary',summary)
    print(json.dumps({k:summary[k] for k in ['utc','canonical_row_count','canonical_bib_count','group_count','body_count','intake_row_count','intake_bib_count','proposed_row_count','held_row_count','normalization_count','new_scope_count','proposed_bib_count','route_pending_files','missing_source_region_files','canonical_changed_during_read','in_memory_patch_parsing_errors']},ensure_ascii=False))

if __name__=='__main__':main()

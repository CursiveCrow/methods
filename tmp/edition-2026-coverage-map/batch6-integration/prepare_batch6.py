"""Batch6 integration preparation only; never write canonical/manuscript."""
from __future__ import annotations
import argparse,copy,csv,hashlib,importlib.util,io,json,re,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
BASE=ROOT/'handbook'
sys.path.insert(0,str(ROOT/'tools'))
import symbol_registry as registry
sys.path.insert(0,str(OUT.parent))
import prepare_oct3_batch5_intakes as grounded
grounded.OUT=OUT
grounded.PREFIX='batch6-proposal-'
FIELDS=registry.HEADER
ARTIFACT_PREFIX=''
def read(path):return Path(path).read_text(encoding='utf-8-sig')
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def save(name,data):
    path=OUT/(ARTIFACT_PREFIX+name+'.json')
    assert path.parent==OUT
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def capture_numeric_meanings(filename='pre-batch6-numeric-meanings',standing=None):
    path=OUT/(filename+'.json')
    if path.exists():return json.loads(read(path))
    index=registry.ReaderIndex(BASE)
    canonical=[BASE/'registry/symbols.csv',BASE/'registry/symbol-scopes.json',BASE/'bib/handbook.bib']
    rows=list(csv.DictReader(io.StringIO(read(canonical[0]))))
    chapters=[]
    for h in index.heading_records:
        if h.kind!='chapter' or h.chapter is None or h.part is None:continue
        inside=sorted([d for ds in index.labels.values() for d in ds if h.start<=d.start<h.end],key=lambda d:d.start)
        exact=[d for d in inside if d.path==h.path and d.start==h.start and d.kind=='chapter']
        selector={'anchor':exact[0].label} if exact else ({'heading_of':inside[0].label,'level':'chapter'} if inside else None)
        valid=[d for d in inside if registry.LABEL_RE.fullmatch(d.label) and len(index.labels.get(d.label,[]))==1]
        first=exact[0].label if exact and registry.LABEL_RE.fullmatch(exact[0].label) else (valid[0].label if valid else None)
        chapters.append({'part':h.part,'chapter':h.chapter,'path':h.path,'line':h.line,'start':h.start,'end':h.end,'selectors':[selector] if selector else [],'valid_first_use':first})
    numeric=[]
    for line,row in enumerate(rows,2):
        interval=registry.parse_scope(row['scope'])
        if not interval or interval==registry.GLOBAL:continue
        occupied=[c for c in chapters if interval[0]<=c['part']*1000+c['chapter']<=interval[1]]
        match=registry.FIRST_RE.fullmatch(row['first_use']);first=row['first_use'] if not match else None
        if match:
            at=[c for c in chapters if c['part']==int(match[1]) and c['chapter']==int(match[2])]
            if len(at)==1:first=at[0]['valid_first_use']
        numeric.append({'canonical_line':line,'original':row,'interval':list(interval),'old_chapters':occupied,'proposed_first_use':first,'standing':'Frozen chapter-level meaning, not a new assertion of exact first glyph occurrence.'})
    scopes=json.loads(read(canonical[1]))
    payload={'utc':datetime.now(timezone.utc).isoformat(),'canonical_row_count':len(rows),'canonical_symbols_sha256':sha(canonical[0]),'canonical_scopes_sha256':sha(canonical[1]),'canonical_bib_sha256':sha(canonical[2]),'canonical_text':{p.relative_to(ROOT).as_posix():read(p) for p in canonical},'route_sha256':{p:sha(BASE/p) for p in sorted(index.files) if (BASE/p).is_file()},'chapters':chapters,'numeric_rows':numeric,'existing_named_scopes':scopes['scopes'],'reader_index_errors':index.errors,'standing':'Actual postB5/preB6 meaning captured once BEFORE routing changes. Includes fragment-hosted body chapters. Named/global meanings remain unchanged; original intakes/history preserved.'}
    if filename!='pre-batch6-numeric-meanings':payload['standing']='Actual current canonical baseline AFTER initial two B6 groups, BEFORE later returned-author chapter insertion. Original preB6 capture retained unchanged; named/global meanings preserved.'
    if standing:payload['standing']=standing
    payload['canonical_bib_count']=len(grounded.bib_records(read(canonical[2])))
    save(filename,payload)
    return payload
def public(row):return {k:v for k,v in row.items() if not k.startswith('_')}
def main():
    global ARTIFACT_PREFIX
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--capture-only',action='store_true')
    ap.add_argument('--capture-post-initial',action='store_true')
    ap.add_argument('--later',action='store_true',help='Prepare only nonmerged later returns against the actual post-initial baseline')
    ap.add_argument('--numeric-baseline',type=Path,help='Frozen actual later-stage numeric meanings; never silently replay an earlier baseline')
    ap.add_argument('--decisions',type=Path)
    ap.add_argument('--include',action='append',help='Explicitly selected current-stage group; repeat for each')
    ap.add_argument('--stage',default='later',help='Separate proposal/history namespace for this stage')
    ap.add_argument('--require-actual',action='store_true',help='Do not index any off-route candidate; fail readiness explicitly')
    ap.add_argument('--patches',action='store_true',help='Emit proposed patches only after root decisions; never apply')
    args=ap.parse_args()
    if args.capture_post_initial:
        summary=json.loads(read(OUT/'summary.json'))
        history_path=OUT/'initial-two-merged-history.json'
        if not history_path.exists():
            save('initial-two-merged-history',{'utc':datetime.now(timezone.utc).isoformat(),'root_confirmation':'Initial four patches actually applied; no reapply. Canonical now6083rows/1250keys; body and annex routes reached once.','summary':summary,'manifest':json.loads(read(ROOT/'spec/research/edition-2026-authoring-batch-intake-6.json')),'patches':{name:{'sha256':sha(OUT/name),'text':read(OUT/name)} for names in summary['application_order'].values() for name in names},'original_numeric_capture_sha256':sha(OUT/'pre-batch6-numeric-meanings.json')})
        current=capture_numeric_meanings('post-initial-two-numeric-baseline')
        print(json.dumps({'utc':current['utc'],'rows':current['canonical_row_count'],'actual_chapters':len(current['chapters']),'numeric_rows':len(current['numeric_rows']),'symbols_sha256':current['canonical_symbols_sha256'],'scopes_sha256':current['canonical_scopes_sha256'],'bib_sha256':current['canonical_bib_sha256']}));return
    if (OUT/'initial-two-merged-history.json').exists() and not args.later and not args.capture_only:
        raise ValueError('Initial two groups already merged. Do not regenerate/reapply them; use --later for newly frozen returns only.')
    frozen=json.loads(read(args.numeric_baseline or OUT/'post-initial-two-numeric-baseline.json')) if args.later else capture_numeric_meanings()
    if args.later:
        if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,40}',args.stage):raise ValueError('Invalid stage namespace')
        ARTIFACT_PREFIX=args.stage+'-';grounded.PREFIX='batch6-'+args.stage+'-proposal-'
    if args.capture_only:
        print(json.dumps({'utc':frozen['utc'],'rows':frozen['canonical_row_count'],'actual_chapters':len(frozen['chapters']),'numeric_rows':len(frozen['numeric_rows']),'symbols_sha256':frozen['canonical_symbols_sha256'],'scopes_sha256':frozen['canonical_scopes_sha256'],'bib_sha256':frozen['canonical_bib_sha256']}));return
    manifest=ROOT/'spec/research/edition-2026-authoring-batch-intake-6.json'
    all_groups=json.loads(read(manifest))['groups']
    groups=[g for g in all_groups if not g.get('integration_status','').startswith('merged')] if args.later else all_groups
    if args.include:
        unknown=set(args.include)-{g['stem'] for g in groups}
        if unknown:raise ValueError('Unknown/unavailable included group '+repr(unknown))
        groups=[g for g in groups if g['stem'] in args.include]
    excluded_groups=[g for g in all_groups if g not in groups]
    if not groups:raise ValueError('No new frozen later groups supplied; initial two remain merged and untouched')
    decisions=json.loads(read(args.decisions)) if args.decisions else {}
    paths=[BASE/'registry/symbols.csv',BASE/'registry/symbol-scopes.json',BASE/'bib/handbook.bib']
    snapshot={p.relative_to(ROOT).as_posix():{'text':read(p),'sha256':sha(p)} for p in paths}
    old_rows=list(csv.DictReader(io.StringIO(snapshot['handbook/registry/symbols.csv']['text'])))
    old_tuple={tuple(r[k] for k in FIELDS) for r in old_rows}
    original_scopes=json.loads(snapshot['handbook/registry/symbol-scopes.json']['text'])
    index=registry.ReaderIndex(BASE);pending=[];sheet_pending=[];issues=[];datasets={};new_scopes={}
    for group in groups:
        for rel in group['bodies']+group['annexes']:
            if not (BASE/rel).is_file():raise ValueError('Missing frozen region file '+rel)
            if not index.files.get(rel):
                if args.require_actual:
                    pending.append(rel);issues.append({'group':group['stem'],'kind':'selected-group-not-actually-routed','path':rel});continue
                index._close_headings(0);index._visit(rel,int(group['part'][1:]));index._close_headings(0);pending.append(rel)
                for ds in index.labels.values():
                    for d in ds:
                        if d.path==rel:d.chapter=None
                for h in index.heading_records:
                    if h.path==rel:h.chapter=None
                for r in index.files.get(rel,[]):r.chapter=None
        # Do not fabricate a reachable rule first_use through showcalculus.
        for rel in group.get('rule_sheets',[]):
            if not index.files.get(rel):sheet_pending.append(rel)
    actual_index=registry.ReaderIndex(BASE)
    migrations=grounded.propose_numeric_migrations(frozen,actual_index)
    for change in migrations['proposed_migration_rows']:
        if change['binding']:
            new_name=change['proposed']['scope'].replace('pre-batch5','pre-batch6')
            change['proposed']['scope']=new_name
            change['proposed']['notes']=change['proposed']['notes'].replace('pre-batch5','pre-batch6')
            change['binding']['presentation']=change['binding']['presentation'].replace('batch5','batch6')
            positions={(d['current_part'],d['current_chapter']) for d in change['chapter_identity_changes']}
            repaired=[]
            for selector in change['binding']['regions']:
                if set(selector)=={'file'} and selector['file'].startswith('annex/'):
                    region=actual_index.region(selector)
                    ds=[d for items in actual_index.labels.values() for d in items if region.start<=d.start<region.end]
                    opaque=[]
                    for d in ds:
                        try:actual_index.numeric_location(d)
                        except registry.RegistryError:opaque.append(d)
                    if opaque:
                        proof_items=[d for d in ds if d.kind=='annexitem' and d.owner]
                        if proof_items and all((actual_index.numeric_location(d)//1000,actual_index.numeric_location(d)%1000) in positions for d in proof_items):
                            repaired.extend({'anchor':d.label} for d in proof_items);continue
                        issues.append({'kind':'numeric-wrapper-association-unresolved','scope':new_name,'selector':selector,'unowned_labels':[d.label for d in opaque]})
                repaired.append(selector)
            change['binding']['regions']=list({json.dumps(s,sort_keys=True):s for s in repaired}.values())
            if new_name in original_scopes['scopes']:raise ValueError('Never replace an existing named meaning '+new_name)
            new_scopes[new_name]=change['binding']
    save('numeric-migration-proposals',migrations)
    def local_regions(first,group):
        d=index.unique(first)
        if d.path not in group['bodies']+group['annexes']+group.get('rule_sheets',[]):raise registry.RegistryError('first_use outside candidate source group')
        if d.path.startswith('annex/'):
            return [{'anchor':d.label}]+([{'anchor':d.owner}] if d.owner else [])
        if d.path.startswith('registry/calculi/'):
            return [{'file':d.path}]
        headings=[h for h in index.heading_records if h.path==d.path and h.start<=d.start<h.end]
        h=max(headings,key=lambda h:h.start) if headings else None
        selectors=[{'heading_of':first,'level':h.kind}] if h else [{'anchor':first}]
        region=index.region(selectors[0])
        for ds in index.labels.values():
            for a in ds:
                if a.kind=='annexitem' and a.owner and a.path in group['annexes']:
                    owner=index.unique(a.owner)
                    if region.start<=owner.start<region.end:selectors.append({'anchor':a.label})
        return selectors
    normalizations=[]
    reuse_records=[];supersessions=[]
    for group in groups:
        stem=group['stem'];sp=BASE/('registry/symbols-intake-'+stem+'.csv');bp=BASE/('bib/intake-'+stem+'.bib')
        sps=[BASE/p for p in group.get('symbol_intakes',[sp.relative_to(BASE).as_posix()])]
        rows=[];raw_entries=[]
        for intake in sps:
            with intake.open(encoding='utf-8-sig',newline='') as handle:
                reader=csv.DictReader(handle)
                if reader.fieldnames!=FIELDS:raise ValueError('Bad intake header '+str(intake))
                raw_entries.extend((line,raw,intake) for line,raw in enumerate(reader,2))
        for line,raw,intake in raw_entries:
            if None in raw:raise ValueError('Malformed row '+str(sp)+':'+str(line))
            row={k:(raw[k] or '').strip() for k in FIELDS};row.update(_group=stem,_line=line,_intake=intake.relative_to(BASE).as_posix(),_uid=intake.name+':'+str(line),_original=copy.deepcopy(row),_changes=[])
            row['_inactive']=False
            for action in decisions.get('row_dispositions',[]):
                if action['group']==stem and action['line']==line and action.get('intake',row['_intake'])==row['_intake']:
                    row['_inactive']=True
                    if action['action']=='reuse':
                        matches=[old for old in old_rows if all(old.get(k)==v for k,v in action['canonical'].items())]
                        if len(matches)!=1:raise ValueError('Nonunique canonical reuse '+row['_uid'])
                        reuse_records.append({'group':stem,'intake':row['_intake'],'line':line,'original':row['_original'],'canonical':matches[0],'reason':action['reason']})
                    elif action['action'] in ('superseded','reuse-proposed'):supersessions.append({'group':stem,'intake':row['_intake'],'line':line,'original':row['_original'],'action':action['action'],'target':action.get('target'),'reason':action['reason']})
                    else:raise ValueError('Unknown row disposition')
            for update in decisions.get('row_updates',[]):
                if update['group']==stem and update['line']==line and (not update.get('intake') or update['intake']==row['_intake']):
                    row.update(update['fields']);row['_changes'].append('Root-authorized declaration/type reconciliation: '+update['reason'])
            if not row['macro']:
                row['macro']=row['glyph'][2:-2] if row['glyph'].startswith(r'\(') and row['glyph'].endswith(r'\)') else row['glyph']
                row['_changes'].append('Blank macro filled with unchanged glyph spelling; registry data only, no new TeX command.')
            if not registry.PREC_RE.fullmatch(row['precedence']):
                row['_changes'].append('Original precedence descriptor '+repr(row['precedence'])+' preserved; n/a is not an invented rank.');row['precedence']='n/a'
            if row['_changes']:row['notes']+=(' ' if row['notes'] else '')+' '.join(row['_changes'])
            row['_merged']=tuple(row[k] for k in FIELDS) in old_tuple
            rows.append(row)
            if row['_changes']:normalizations.append({'group':stem,'line':line,'original':row['_original'],'proposed':public(row),'changes':row['_changes']})
        if stem=='p13-ganeri' and decisions.get('split_ganeri_negation'):
            revised=[]
            for row in rows:
                if row['_line']==16 and row['glyph']=='neg':
                    for tag,role in [('object','object-level absence constructor'),('external','external classical denial of location truth')]:
                        child=copy.deepcopy(row);child['role']=role;child['_uid']+=':'+tag
                        child['notes']+=' Root-authorized typed split in the SAME actual Navya declaration/rule/proof regions; original combined row remains evidence.'
                        revised.append(child)
                else:revised.append(row)
            rows=revised
        datasets[stem]={'group':group,'rows':rows,'original_raw_count':len(raw_entries),'bib':grounded.bib_records(read(bp)),'sp':sp,'sps':sps,'bp':bp}
        scope_rows={}
        for row in rows:
            if not row['_merged'] and not row['_inactive']:scope_rows.setdefault(row['scope'],[]).append(row)
        for name,entries in scope_rows.items():
            if registry.parse_scope(name) or registry.LABEL_RE.fullmatch(name) or ' through ' in name or name in original_scopes['scopes']:continue
            specs=[]
            for row in entries:
                try:specs.extend(local_regions(row['first_use'],group))
                except registry.RegistryError as exc:issues.append({'group':stem,'line':row['_line'],'kind':'binding-unresolved','error':str(exc)})
            if specs:new_scopes[name]={'presentation':'Actual batch6 source-labelled regions of '+stem+'; not source/version/proof admission','regions':list({json.dumps(x,sort_keys=True):x for x in specs}.values())}
    for item in decisions.get('scope_bindings',[]):
        if item['scope'] in original_scopes['scopes']:raise ValueError('Existing scope updates require root-owned separate patch')
        new_scopes[item['scope']]=item['binding']
    for item in decisions.get('overrides',[]):
        if item['scope'] not in new_scopes:new_scopes[item['scope']]={'presentation':item['presentation'],'regions':item['regions']}
        new_scopes[item['scope']].setdefault('overrides',[]).append(item['rule'])
    scope_updates={}
    for addition in decisions.get('existing_scope_usage_additions',[]):
        name=addition['scope']
        if name not in original_scopes['scopes']:raise ValueError('Unknown existing host scope '+name)
        new=copy.deepcopy(original_scopes['scopes'][name])
        for selector in addition['regions']:
            if selector not in new['regions']:new['regions'].append(selector)
        scope_updates[name]={'original':original_scopes['scopes'][name],'proposed':new,'reason':addition['reason']}
    save('existing-scope-usage-updates',scope_updates)
    combined=copy.deepcopy(original_scopes);combined['scopes'].update(new_scopes);combined['scopes'].update({k:v['proposed'] for k,v in scope_updates.items()})
    resolver=registry.Resolver(BASE,bindings=combined,index=index)
    for data in datasets.values():resolver.source_keys.update(r['key'] for r in data['bib'])
    migration_rows={x['canonical_line']:x['proposed'] for x in migrations['proposed_migration_rows']}
    parsed=[];canonical_errors=[]
    for line,original in enumerate(old_rows,2):
        row=copy.deepcopy(migration_rows.get(line,original));row.update(_line=line,_resolver=resolver)
        try:
            row['_scope']=resolver.resolve(row['scope'])
            if not resolver.contains(row['_scope'],row['first_use']):raise registry.RegistryError('first_use outside scope')
            parsed.append(row)
        except registry.RegistryError as exc:canonical_errors.append({'line':line,'error':str(exc)})
    incoming=[]
    for stem,data in datasets.items():
        for row in data['rows']:
            if row['_merged'] or row['_inactive']:continue
            row['_resolver']=resolver
            try:
                row['_scope']=resolver.resolve(row['scope'])
                if not resolver.contains(row['_scope'],row['first_use']):raise registry.RegistryError('first_use outside scope')
                incoming.append(row)
            except registry.RegistryError as exc:issues.append({'group':stem,'line':row['_line'],'kind':'row-unresolved','error':str(exc),'row':public(row)})
    glyphs={};collisions=[];held=set()
    for row in parsed+incoming:glyphs.setdefault(re.sub(r'\s+','',row['glyph']),[]).append(row)
    for entries in glyphs.values():
        for i,a in enumerate(entries):
            for b in entries[i+1:]:
                if not (a.get('_group') or b.get('_group')) or not resolver.overlaps(a['_scope'],b['_scope']):continue
                if a['role']!=b['role'] and (resolver.authorized_override(a,b) or resolver.authorized_override(b,a)):continue
                for row in (a,b):
                    if row.get('_group'):held.add((row['_group'],row['_uid']))
                collisions.append({'glyph':a['glyph'],'a':{**public(a),'group':a.get('_group','canonical'),'line':a['_line']},'b':{**public(b),'group':b.get('_group','canonical'),'line':b['_line']},'standing':'Held for exact root decision; no glyph rename/fake disjoint source scopes.'})
    safe=[r for r in incoming if (r['_group'],r['_uid']) not in held]
    old_bib=grounded.bib_records(snapshot['handbook/bib/handbook.bib']['text']);bykey={r['key']:r for r in old_bib};new_bib=[];bib_decisions=[];bib_actions=decisions.get('bib_actions',{})
    for stem,data in datasets.items():
        for record in data['bib']:
            existing=bykey.get(record['key'])
            if existing:
                a,b=grounded.fields(record),grounded.fields(existing)
                identity=('author','title','booktitle','series','volume','editor','publisher','year','pages','isbn')
                approved_johnson=record['key']=='Johnson2004ModalSyllogisms' and all(a.get(k)==b.get(k) for k in identity)
                action=bib_actions.get(record['key'],{}).get('action')
                decision='reuse-exact-Johnson-publication-identity' if approved_johnson else ('reuse-root-identified-record' if action=='reuse' else ('skip-identical-record' if record['comparison']==existing['comparison'] else 'HELD differing exact key'))
                bib_decisions.append({'group':stem,'key':record['key'],'incoming':record,'existing':existing,'incoming_fields':a,'existing_fields':b,'decision':decision})
                if decision.startswith('HELD'):issues.append({'group':stem,'kind':'bibliography-key-conflict','key':record['key']})
            else:
                action=bib_actions.get(record['key'],{})
                if action.get('action')=='reuse':
                    if action['canonical_key'] not in bykey:raise ValueError('Unknown root bibliography reuse target')
                    bib_decisions.append({'group':stem,'key':record['key'],'incoming':record,'existing':bykey[action['canonical_key']],'decision':'reuse-root-identified-record'})
                else:new_bib.append(record);bykey[record['key']]=record
    for stem,data in datasets.items():
        save('group-'+stem,{'group':data['group'],'inputs':[{'path':p.relative_to(ROOT).as_posix(),'sha256':sha(p)} for p in data['sps']+[data['bp'],ROOT/data['group']['note']]],'source_regions':[{'path':rel,'sha256':sha(BASE/rel),'actual_route':rel not in pending} for rel in data['group']['bodies']+data['group']['annexes']],'proposed_rows':[public(r) for r in safe if r['_group']==stem],'held_rows':[public(r) for r in data['rows'] if (stem,r['_uid']) in held],'raw_row_count':data['original_raw_count'],'transformed_row_count':len(data['rows']),'bib_records':data['bib']})
    save('scopes',{'append_only_scopes':new_scopes});save('normalizations',normalizations);save('bibliography',{'append_records':new_bib,'decisions':bib_decisions})
    save('row-reuses-and-supersessions',{'reused':reuse_records,'superseded':supersessions,'standing':'Original raw intakes unchanged; exact root-approved semantic reuse/supersession, not glyph renaming.'})
    order={};sizes={};replay_errors=[]
    if args.patches:
        if pending or sheet_pending or issues or collisions or canonical_errors:raise ValueError('Current reader/decision diagnostics unresolved; JSON saved but no applicable final patches emitted')
        metadata_pairs=[]
        for old_record in old_bib:
            updates=decisions.get('bibliography_metadata',{}).get(old_record['key'])
            if updates:metadata_pairs.append((old_record['raw'],grounded.update_record(old_record,updates)['raw']))
        names,ss=grounded.replacement_chunks('bibliography-metadata',BASE/'bib/handbook.bib',metadata_pairs);order['bibliography_metadata']=names;sizes.update(ss)
        names,ss=grounded.chunks('bib',BASE/'bib/handbook.bib',old_bib[-1]['raw'],[x['raw'] for x in new_bib]);order['bib']=names;sizes.update(ss)
        text=snapshot['handbook/registry/symbol-scopes.json']['text'];last=next(reversed(original_scopes['scopes']));token=json.dumps(last,ensure_ascii=False);sites=list(re.finditer(r'(?m)^([ \t]*)'+re.escape(token)+r'\s*:',text))
        if len(sites)!=1:raise ValueError('Nonunique canonical scope tail')
        site=sites[0];start=site.start();at=start+len(site[1]);value=text.index(':',at+len(token))+1
        while text[value].isspace():value+=1
        _,extent=json.JSONDecoder().raw_decode(text[value:]);anchor=text[start:value+extent];prefix=text[start:at]
        members=[prefix+json.dumps(k,ensure_ascii=False)+': '+json.dumps(v,ensure_ascii=False,separators=(',',':')) for k,v in new_scopes.items()]
        names,ss=grounded.chunks('scopes',BASE/'registry/symbol-scopes.json',anchor,members,True);order['scopes']=names;sizes.update(ss)
        scope_pairs=[]
        for name,update in scope_updates.items():
            key=json.dumps(name,ensure_ascii=False);matches=list(re.finditer(r'(?m)^([ \t]*)'+re.escape(key)+r'\s*:',text))
            if len(matches)!=1:raise ValueError('Nonunique existing scope member')
            match=matches[0];begin=match.start();keypos=begin+len(match[1]);val=text.index(':',keypos+len(key))+1
            while text[val].isspace():val+=1
            _,extent=json.JSONDecoder().raw_decode(text[val:]);tail=',' if text[val+extent:val+extent+1]==',' else '';old=text[begin:val+extent]+tail
            new=match[1]+key+': '+json.dumps(update['proposed'],ensure_ascii=False,separators=(',',':'))
            new+=tail
            scope_pairs.append((old,new))
        names,ss=grounded.replacement_chunks('existing-scope-usage',BASE/'registry/symbol-scopes.json',scope_pairs);order['existing_scope_usage']=names;sizes.update(ss)
        names,ss=grounded.chunks('rows',BASE/'registry/symbols.csv',snapshot['handbook/registry/symbols.csv']['text'].rstrip().splitlines()[-1],[grounded.csv_lines([r]) for r in safe]);order['rows']=names;sizes.update(ss)
        raw_lines=snapshot['handbook/registry/symbols.csv']['text'].splitlines();pairs=[(raw_lines[line-1],grounded.csv_lines([r])) for line,r in migration_rows.items()]
        names,ss=grounded.replacement_chunks('numeric-migrations',BASE/'registry/symbols.csv',pairs);order['numeric_migrations']=names;sizes.update(ss)
        aliases=decisions.get('citation_aliases',{});citation_names=[]
        for group in groups:
            for rel in group['bodies']+group['annexes']:
                source=read(BASE/rel);lines=source.splitlines();new_lines=[];intervals=[]
                for n,line in enumerate(lines):
                    new=line
                    for incoming_key,current_key in aliases.items():new=re.sub(r'\b'+re.escape(incoming_key)+r'\b',current_key,new)
                    new_lines.append(new)
                    if new==line:continue
                    radius=1
                    while True:
                        left=max(0,n-radius);right=min(len(lines),n+radius+1)
                        if source.count('\n'.join(lines[left:right]))==1:break
                        radius+=1
                    if intervals and left<=intervals[-1][1]:intervals[-1][1]=max(right,intervals[-1][1])
                    else:intervals.append([left,right])
                pairs=[('\n'.join(lines[l:r]),'\n'.join(new_lines[l:r])) for l,r in intervals]
                if pairs:
                    names,ss=grounded.replacement_chunks('citation-'+group['stem']+'-'+Path(rel).stem+'-'+Path(rel).parent.name,BASE/rel,pairs);citation_names+=names;sizes.update(ss)
        order['citation_aliases']=citation_names
        virtual={p.as_posix():read(p) for p in paths}
        for names in order.values():
            for patch_name in names:
                patch=read(OUT/patch_name);target=patch.split('*** Update File: ',1)[1].split('\n',1)[0]
                if target not in virtual:virtual[target]=read(Path(target))
                for block in patch.split('@@\n')[1:]:
                    lines=block.split('*** End Patch',1)[0].rstrip('\n').splitlines();old='\n'.join(x[1:] for x in lines if x[:1] in {' ','-'});new='\n'.join(x[1:] for x in lines if x[:1] in {' ','+'})
                    if virtual[target].count(old)!=1:replay_errors.append(patch_name+': missing/nonunique anchor')
                    else:virtual[target]=virtual[target].replace(old,new,1)
        json.loads(virtual[(BASE/'registry/symbol-scopes.json').as_posix()])
        if len(list(csv.DictReader(io.StringIO(virtual[(BASE/'registry/symbols.csv').as_posix()]))))!=len(old_rows)+len(safe):replay_errors.append('CSV count mismatch')
        if len(grounded.bib_records(virtual[(BASE/'bib/handbook.bib').as_posix()]))!=len(old_bib)+len(new_bib):replay_errors.append('Bibliography count mismatch')
    after={p.relative_to(ROOT).as_posix():sha(p) for p in paths}
    result={'utc':datetime.now(timezone.utc).isoformat(),'manifest_sha256':sha(manifest),'canonical_before':{k:v['sha256'] for k,v in snapshot.items()},'canonical_after':after,'canonical_changed_during_read':[k for k,v in snapshot.items() if v['sha256']!=after[k]],'canonical_row_count':len(old_rows),'canonical_bib_count':len(old_bib),'groups':[g['stem'] for g in groups],'raw_intake_rows':sum(d['original_raw_count'] for d in datasets.values()),'transformed_intake_rows':sum(len(d['rows']) for d in datasets.values()),'stage':args.stage,'excluded_groups':[{'stem':g['stem'],'integration_status':g.get('integration_status',''),'standing':'Retained in full manifest; not part of this current-stage semantic/patch assessment'} for g in excluded_groups],'full_manifest_group_count':len(all_groups),'proposed_rows':len(safe),'held_rows':len(held),'new_bib_records':len(new_bib),'new_scopes':len(new_scopes),'numeric_migration_rows':len(migration_rows),'pending_body_annex_routes':pending,'pending_literal_sheet_routes':sheet_pending,'issues':issues,'collisions':collisions,'canonical_resolution_errors':canonical_errors,'full_virtual_collision_errors':registry.collision_check(parsed+incoming),'bibliography_decisions':bib_decisions,'application_order':order,'patch_characters':sizes,'patch_replay_errors':replay_errors,'standing':'Only batch6 preparation. Never runs merged B4/B5 main functions; preserves all original intakes and prior meanings. Actual rule locators require literal reachable input. No source/proof/admission review.'}
    save('summary',result)
    print(json.dumps({k:result[k] for k in ['utc','groups','canonical_row_count','canonical_bib_count','raw_intake_rows','proposed_rows','held_rows','new_bib_records','new_scopes','numeric_migration_rows','pending_body_annex_routes','pending_literal_sheet_routes','canonical_changed_during_read','patch_replay_errors']}))
if __name__=='__main__':main()

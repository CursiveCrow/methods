"""Root-approved exact selector repair; no canonical/manuscript writes."""
from __future__ import annotations
import copy,csv,io,json,sys,re
from datetime import datetime,timezone
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import prepare_oct3_batch5_intakes as prep
R=prep.registry
OUT,BASE,ROOT=prep.OUT,prep.BASE,prep.ROOT
name='oct3-batch5-ordering-diagnostics'
def save(suffix,data):
    (OUT/(name+suffix+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def pub(d):return {k:v for k,v in d.items() if not k.startswith('_')}

summary_path=OUT/(prep.PREFIX+'summary.json')
scopes_path=OUT/(prep.PREFIX+'scopes.json')
old_summary=json.loads(prep.read(summary_path))
old_scope_data=json.loads(prep.read(scopes_path))
old_scope_patches={p:{'sha256':prep.sha(OUT/p),'text':prep.read(OUT/p)} for p in old_summary['application_order']['scopes']}
history={'utc':datetime.now(timezone.utc).isoformat(),'summary_sha256':prep.sha(summary_path),'scope_data_sha256':prep.sha(scopes_path),'summary':old_summary,'scope_data':old_scope_data,'scope_patches':old_scope_patches,'standing':'Original B5 packet/error history preserved before root-approved ordering selector repair.'}
history_path=OUT/(name+'-before-repair.json')
if not history_path.exists():save('-before-repair',history)
else:history=json.loads(prep.read(history_path));old_summary=history['summary'];old_scope_data=history['scope_data']

frozen=json.loads(prep.read(OUT/(prep.PREFIX+'pre-route-numeric-bindings.json')))
index=R.ReaderIndex(BASE)
manifest=json.loads(prep.read(ROOT/'spec/research/edition-2026-authoring-batch-intake-5.json'))
sheet_visits=[]
for group in manifest['groups']:
    for rel in group.get('rule_sheets',[]):
        if not index.files.get(rel):
            index._close_headings(0);index._visit(rel,int(group['part'][1:]));index._close_headings(0)
            sheet_visits.append(rel)
            for ds in index.labels.values():
                for d in ds:
                    if d.path==rel:d.chapter=None
            for h in index.heading_records:
                if h.path==rel:h.chapter=None
            for region in index.files.get(rel,[]):region.chapter=None

scope_name='Legacy pre-batch5 P4.4-P4.6 reader meaning'
offending={'file':'annex/p04/decision-problem-hardness.tex'}
before_binding=old_scope_data['append_only_scopes'][scope_name]
items=sorted([d for ds in index.labels.values() for d in ds if d.kind=='annexitem' and d.path==offending['file']],key=lambda d:d.start)
if not items or any(not d.owner or index.numeric_location(d)!=4007 for d in items):raise ValueError('Associated proof identity changed; root decision required')
replacement=[{'anchor':d.label} for d in items]
after_binding=copy.deepcopy(before_binding)
after_binding['regions']=[p for s in before_binding['regions'] for p in (replacement if s==offending else [s])]

canonical_scopes=json.loads(prep.read(BASE/'registry/symbol-scopes.json'))
before_scopes=copy.deepcopy(canonical_scopes);before_scopes['scopes'].update(old_scope_data['append_only_scopes'])
after_scopes=copy.deepcopy(before_scopes);after_scopes['scopes'][scope_name]=after_binding
before=R.Resolver(BASE,bindings=before_scopes,index=index)
after=R.Resolver(BASE,bindings=after_scopes,index=index)
for g in manifest['groups']:
    path=BASE/('bib/intake-'+g['stem']+'.bib')
    for record in prep.bib_records(prep.read(path)):before.source_keys.add(record['key']);after.source_keys.add(record['key'])
for record in prep.bib_records(prep.read(BASE/manifest['root_apparatus']['bib_intake'])):before.source_keys.add(record['key']);after.source_keys.add(record['key'])

declarations=[d for ds in index.labels.values() for d in ds]
def witness(selector,interval):
    region=index.region(selector);matches=[];fallbacks=[];locations=[]
    for d in declarations:
        if not region.start<=d.start<region.end:continue
        try:
            loc=index.numeric_location(d);locations.append(loc)
            if interval[0]<=loc<=interval[1]:matches.append({'label':d.label,'path':d.path,'line':d.line,'location':loc,'owner':d.owner,'event':d.start})
        except R.RegistryError as exc:
            if interval[0]//1000<=region.part<=interval[1]//1000:
                fallbacks.append({'label':d.label,'path':d.path,'line':d.line,'kind':d.kind,'owner':d.owner,'chapter':d.chapter,'event':d.start,'end':d.end,'error':str(exc),'mechanism':'Resolver.overlaps numeric/local fallback returns true for any numeric interval spanning this part.'})
    return {'selector':selector,'region':vars(region),'owned_numeric_locations':sorted(set(locations)),'actual_numeric_intersection_declarations':matches,'conservative_fallback_witnesses':fallbacks}
trace=[]
for line,raw in [(79,'P1-P4.2'),(80,'P4.3')]:
    interval=R.parse_scope(raw)
    trace.append({'canonical_line':line,'scope':raw,'numeric_interval':list(interval),'before_overlap':before.overlaps(before.resolve(raw),before.resolve(scope_name)),'after_overlap':after.overlaps(after.resolve(raw),after.resolve(scope_name)),'before_selector_witnesses':[witness(s,interval) for s in before_binding['regions']],'after_selector_witnesses':[witness(s,interval) for s in after_binding['regions']]})

migrations=json.loads(prep.read(OUT/(prep.PREFIX+'numeric-migrations.json')))
updates={x['canonical_line']:x['proposed'] for x in migrations['proposed_migration_rows']}
rows=list(csv.DictReader(io.StringIO(prep.read(BASE/'registry/symbols.csv'))))
virtual=[];errors=[]
for line,original in enumerate(rows,2):
    row=copy.deepcopy(updates.get(line,original));row.update(_line=line,_resolver=after)
    try:
        row['_scope']=after.resolve(row['scope'])
        if not after.contains(row['_scope'],row['first_use']):raise R.RegistryError('first_use outside scope')
        virtual.append(row)
    except R.RegistryError as exc:errors.append({'line':line,'error':str(exc)})
for g in manifest['groups']:
    data=json.loads(prep.read(OUT/(prep.PREFIX+g['stem']+'.json')))
    for incoming in data['proposed_rows']:
        row=copy.deepcopy(incoming);row.update(_line=len(virtual)+2,_resolver=after)
        try:
            row['_scope']=after.resolve(row['scope'])
            if not after.contains(row['_scope'],row['first_use']):raise R.RegistryError('first_use outside scope')
            virtual.append(row)
        except R.RegistryError as exc:errors.append({'group':g['stem'],'error':str(exc)})
collisions=R.collision_check(virtual)
result={'utc':datetime.now(timezone.utc).isoformat(),'root_authorization':'Exclude ONLY unowned annex wrapper by replacing whole-file selector with exact associated proof items; no notation/role changes or resolver weakening.','original_rows':[x for x in frozen['numeric_rows'] if x['canonical_line'] in [79,80,81]],'before_binding':before_binding,'after_binding':after_binding,'associated_proof_items':[vars(d) for d in items],'overlap_traces':trace,'full_virtual_row_resolution_errors':errors,'full_virtual_collision_errors':collisions,'full_virtual_row_count':len(virtual),'sheet_index_limitation':{'extra_visits':sheet_visits,'reason':'ReaderIndex does not expand actual showcalculus display; only displayed source sheets visited for declaration resolution, no body ordinal invented.'},'standing':'Mechanical source-region preservation diagnostic, not proof/source/admission review.'}
save('',result)
if errors or collisions:raise ValueError('Corrected selector still has unresolved diagnostics; packet not changed')

# Rewrite only scope proposal data/chunks and application-order/diagnostics.
corrected_data=copy.deepcopy(old_scope_data);corrected_data['append_only_scopes'][scope_name]=after_binding
scope_text=prep.read(BASE/'registry/symbol-scopes.json');last=next(reversed(canonical_scopes['scopes']));token=json.dumps(last,ensure_ascii=False)
sites=list(re.finditer(r'(?m)^([ \t]*)'+re.escape(token)+r'\s*:',scope_text))
if len(sites)!=1:raise ValueError('Canonical scope tail changed')
site=sites[0];start=site.start();at=start+len(site[1]);value=scope_text.index(':',at+len(token))+1
while scope_text[value].isspace():value+=1
_,extent=json.JSONDecoder().raw_decode(scope_text[value:]);anchor=scope_text[start:value+extent];prefix=scope_text[start:at]
members=[prefix+json.dumps(k,ensure_ascii=False)+': '+json.dumps(v,ensure_ascii=False,separators=(',',':')) for k,v in corrected_data['append_only_scopes'].items()]
scope_names,scope_sizes=prep.chunks('scopes',BASE/'registry/symbol-scopes.json',anchor,members,True)
new_summary=copy.deepcopy(old_summary);new_summary['application_order']['scopes']=scope_names
for old in old_summary['application_order']['scopes']:new_summary['chunk_characters'].pop(old,None)
new_summary['chunk_characters'].update(scope_sizes)
files={};patch_errors=[]
for kind,names in new_summary['application_order'].items():
    for patch_name in names:
        patch=prep.read(OUT/patch_name);target=patch.split('*** Update File: ',1)[1].split('\n',1)[0]
        if target not in files:files[target]=prep.read(Path(target))
        for block in patch.split('@@\n')[1:]:
            lines=block.split('*** End Patch',1)[0].rstrip('\n').splitlines();old='\n'.join(x[1:] for x in lines if x[:1] in {' ','-'});new='\n'.join(x[1:] for x in lines if x[:1] in {' ','+'})
            if files[target].count(old)!=1:patch_errors.append(patch_name+': missing/nonunique anchor')
            else:files[target]=files[target].replace(old,new,1)
for path,text in files.items():
    if path.endswith('symbol-scopes.json'):json.loads(text)
    elif path.endswith('symbols.csv'):
        if len(list(csv.DictReader(io.StringIO(text))))!=6050:patch_errors.append('Final CSV count mismatch')
    elif path.endswith('handbook.bib'):
        if len(prep.bib_records(text))!=1247:patch_errors.append('Final bibliography count mismatch')
if patch_errors:raise ValueError(patch_errors)
new_summary['original_packet_utc']=old_summary['utc'];new_summary['utc']=datetime.now(timezone.utc).isoformat()
new_summary['virtual_full_collision_errors']=collisions;new_summary['in_memory_patch_parsing_errors']=patch_errors
new_summary['ordering_selector_repair']={'diagnostic_file':name+'.json','preserved_error_history_file':name+'-before-repair.json','changed_scope':scope_name,'old_selector':offending,'new_selectors':replacement,'full_virtual_row_resolution_errors':errors,'all_other_scopes_rows_bib_citations_unchanged':True}
scopes_path.write_text(json.dumps(corrected_data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
summary_path.write_text(json.dumps(new_summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
result['updated_scope_patch_order']=scope_names;result['updated_summary_sha256']=prep.sha(summary_path);result['updated_scope_data_sha256']=prep.sha(scopes_path);result['scope_patch_sha256']={n:prep.sha(OUT/n) for n in scope_names};result['full_ordered_patch_replay_errors']=patch_errors
save('',result)
print(json.dumps({'utc':new_summary['utc'],'before_overlap_pairs':[x['before_overlap'] for x in trace],'after_overlap_pairs':[x['after_overlap'] for x in trace],'replaced_file_selector_with_proof_items':len(replacement),'full_virtual_row_count':len(virtual),'full_virtual_row_resolution_errors':errors,'full_virtual_collision_errors':collisions,'patch_replay_errors':patch_errors,'scope_patch_order':scope_names,'scope_patch_hashes':result['scope_patch_sha256'],'summary_sha256':result['updated_summary_sha256']},indent=2))

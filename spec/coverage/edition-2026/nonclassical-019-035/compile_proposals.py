"""Compile the manual17-row coverage allocation, preserving canonical identities."""
from pathlib import Path
import copy, csv, hashlib, json, re, sys
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
SUFFIX = ('-' + sys.argv[1]) if len(sys.argv) > 1 else ''
if SUFFIX and not re.fullmatch(r'-v[1-9][0-9]*', SUFFIX):
    raise SystemExit('Optional revision must be v2, v3, ...')
ROOT = HERE.parents[3]
BASE = HERE.parent
sys.path.insert(0, str(HERE))
from goal_profiles import PROFILES
sys.path.insert(0, str(ROOT/'tools'))
import check as grammar

def readrows(name):
    return [json.loads(s) for s in (BASE/name).read_text(encoding='utf-8-sig').splitlines() if s.strip()]
req = {r['original_requirement_id']:r for r in readrows('requirements-crosswalk.jsonl')}
units = {r['unit_id']:r for r in readrows('requirements-units.jsonl')}
with (HERE/'source_allocations.tsv').open(encoding='utf-8-sig',newline='') as f:
    allocations = list(csv.DictReader(f, delimiter='\t'))
assert len(PROFILES) == 17 and len(allocations) == 59
assert {p['id'] for p in PROFILES} == {f'N-b-{i:03}' for i in range(19,36)}

bibtext = (ROOT/'handbook/bib/handbook.bib').read_text(encoding='utf-8-sig')
bib = {}
for m in re.finditer(r'@[A-Za-z]+\s*\{', bibtext):
    args,end=grammar.scan_braced_args(bibtext,m.end()-1,1)
    if args and ',' in args[0]:
        key=args[0].split(',',1)[0].strip()
        bib[key] = dict(key=key,path='handbook/bib/handbook.bib',line=bibtext.count('\n',0,m.start())+1,literal_record=bibtext[m.start():end])
extra=json.loads((BASE/'nonclassical-additional-identities.json').read_text(encoding='utf-8'))
identities={s['key']:s for s in extra['sources']}
local_extra={
 'Priest2002BeyondLimits':dict(key='Priest2002BeyondLimits',author='Graham Priest',title='Beyond the Limits of Thought',edition='Second extended edition',year=2002,doi='10.1093/acprof:oso/9780199254057.001.0001',isbn='9780199254057',url='https://academic.oup.com/book/8368',author_confirmation='https://grahampriest.net/publications/books/'),
 'Herzberger1982Erratum':dict(key='Herzberger1982Erratum',title='Erratum',journal='Journal of Philosophical Logic',volume=11,issue=3,pages='371',year=1982,doi='10.1007/BF00293435',publisher_issue='https://link.springer.com/journal/10992/volumes-and-issues/11-3',publisher_article='https://link.springer.com/article/10.1007/BF00293435',standing='Exact publisher item identity resolved; full body and applicability to Herzberger remain a bounded acquisition/reading task, not an invented correction.'),
 'McCarthy1986Circumscription':dict(key='McCarthy1986Circumscription',author='John McCarthy',title='Applications of Circumscription to Formalizing Common-Sense Knowledge',year=1986,journal='Artificial Intelligence',volume=28,pages='89–116',doi='10.1016/0004-3702(86)90032-9',url='https://www-formal.stanford.edu/jmc/applications.html',publisher_url='https://www.sciencedirect.com/science/article/pii/0004370286900329',standing='Author index and publisher identity/abstract verified. This separate later source supports the varying/prioritized interface; complete body qualification and presentation still required.'),
 'BehounekCintula2022Corrigenda':dict(key='BehounekCintula2022Corrigenda',authors='Libor Běhounek and Petr Cintula',title='Corrigenda to Chapter1 Introduction to Mathematical Fuzzy Logic',version='25 October2022',doi='10.13140/RG.2.2.14956.44166',author_index='https://www.behounek.online/logic/',standing='Author-linked corrected item; indexed author text read. Direct DOI fetch failed. Three corrections explicitly allocated, no local body-acquisition credit.')}
identities.update(local_extra)
def identity(key):
    if key in identities:return identities[key]
    if key in bib:return bib[key]
    raise ValueError('Unidentified bibliography key: '+key)

fuzzy_constituents=[
 dict(presentation_id='CintulaHajekNoguera2011-I',authors='Libor Běhounek;Petr Cintula;Petr Hájek',title='Introduction to Mathematical Fuzzy Logic',volume=1,chapter='I',extent='Sections1–4, starts2,26,55,68; section4.1 Completeness theorems starts69; source chapter body1–101; include required preceding definitions and2022corrections',role='Survey; all but one theorem proof expressly omitted by the authors',url='https://www.behounek.online/logic/papers/handbook-mfl-ch1.pdf'),
 dict(presentation_id='CintulaHajekNoguera2011-II',authors='Petr Cintula;Carles Noguera',title='A General Framework for Mathematical Fuzzy Logic',volume=1,chapter='II',extent='Sections2–3 starts105,153; §§2.1–2.6 and3.1–3.4 supply the selected implicative/semilinear/completeness framework and its native proof dependencies; full chapter103–207',role='General formal framework'),
 dict(presentation_id='CintulaHajekNoguera2011-IV',authors='Rostislav Horčík',title='Algebraic Semantics:Semilinear FL-Algebras',volume=1,chapter='IV',extent='Sections2–4 starts287,293,318, especially4.1 Integral semilinear varieties(start320), and every internal dependency of the MTL/standard-completeness construction',role='Algebraic proof support'),
 dict(presentation_id='CintulaHajekNoguera2011-V',authors='Manuela Busaniche;Franco Montagna',title='Hájek’s Logic BL and BL-Algebras',volume=1,chapter='V',extent='Sections2–4 starts357,368,381; especially2.4 BL-chains and completeness(start363),4.3 Generation by t-norm BL-algebras(start384),4.6 Generating classes and completeness theorems(start390),with full internal proof dependencies',role='BL source presentation'),
 dict(presentation_id='CintulaHajekNoguera2011-VI',authors='Antonio Di Nola;Ioana Leuștean',title='Łukasiewicz Logic and MV-Algebras',volume=2,chapter='VI',extent='Sections2–3 starts470,493;5.3 Chang completeness(start536);6 Łukasiewicz infinite-valued logic(start547),including6.1–6.4 and their exact algebraic proof dependencies',role='MV/Łukasiewicz source presentation'),
 dict(presentation_id='CintulaHajekNoguera2011-VII',authors='Matthias Baaz;Norbert Preining',title='Gödel–Dummett Logics',volume=2,chapter='VII',extent='Propositional syntax/semantics/axiomatization and completeness treatment in chapter585–626, including1.3(start587),1.5(start590)and its native propositional proof dependencies; quantified developments beyond a used dependency remain separately catalogued',role='Gödel source presentation',url='https://dspace.jaist.ac.jp/dspace/handle/10119/10903')]
for c in fuzzy_constituents:
    c['contents_evidence']='https://www.collegepublications.co.uk/downloads/mlf00020.pdf'
    c['extent_standing']='Named source sections and displayed starts, not inferred end pages; selected source bodies remain to be qualified/read.'

dependencies={
 'N-b-021':[('Herzberger1982Erratum','Entire exact one-page erratum; establish applicability and implement any actual correction','source_correction')],
 'N-b-026':[('Priest2002BeyondLimits','Chapter9 Vicious Circles: native inclosure schema and argument, with required preceding schema definitions only','external_result')],
 'N-b-029':[('CignoliEstevaGodoTorrens2000','Basic fuzzy logic is the logic of continuous t-norms and their residua: complete standard-BL completeness proof','external_result'),('JeneiMontagna2002','A proof of standard completeness for Esteva and Godo logic MTL: complete original proof and its exact cardinality/consequence scope','external_result'),('BehounekCintula2022Corrigenda','All three original chapterI corrections, with applicability and date of any subsequent status change','source_correction')],
 'N-b-032':[('KatsunoMendelzon1991','Finite faithful-preorder revision versus update presentation used in the current comparison; no replacement for original AGM','comparison_source')],
 'N-b-033':[('McCarthy1986Circumscription','The varying-predicate and prioritized circumscription constructions, examples and supporting results needed for the current generalized interface','external_result')]}

# Current LaTeX is evidence about authored coverage, not source/native proof acceptance.
paths=[ROOT/'handbook/parts/p11/philosophy-of-logic.tex']
paths += [ROOT/'handbook/parts/p08'/n for n in ['many-valued-supplement.tex','paraconsistent-and-nonmonotonic.tex','relevance-linear-supplement.tex','intuitionistic-supplement.tex']]
anchors={}
read_receipts=[]
for path in paths:
    literal=path.read_text(encoding='utf-8-sig')
    text=grammar.strip_verbatims(grammar.strip_comments(literal))
    rel=path.relative_to(ROOT).as_posix(); digest=hashlib.sha256(path.read_bytes()).hexdigest()
    read_receipts.append(dict(path=rel,sha256=digest,read_extent='Full P11 philosophy file; named P8 content sections/entries used in the profiles. No full-book read or review claimed.'))
    for m in grammar.HB_ENV_RE.finditer(text):
        env=m.group(1); arity=3 if env in grammar.HB_STATUS_ENVS or env=='annexitem' else 2
        args,end=grammar.scan_braced_args(text,m.end(),arity)
        if len(args)!=arity:continue
        close=text.find('\\end{'+env+'}',end)
        anchors.setdefault(args[0],[]).append(dict(path=rel,label=args[0],line=text.count('\n',0,m.start())+1,sha256=digest,kind=env,title=args[-1],declared_status=args[1] if env in grammar.HB_STATUS_ENVS else None,declaration_text=text[end:close] if close>=0 else None))
    for m in re.finditer(r'\\label\{([^}]+)\}',text):
        anchors.setdefault(m.group(1),[]).append(dict(path=rel,label=m.group(1),line=text.count('\n',0,m.start())+1,sha256=digest,kind='explicit_label'))

def spaced(s):
    # Mechanical prose spacing, leaving source keys and mathematical L0/K3 labels intact.
    s=re.sub(r'(?<=[A-Za-z])(?=(?:18|19|20)\d{2})',' ',s)
    s=re.sub(r'(?<=(?:18|19|20)\d{2})(?=[A-Za-z])',' ',s)
    s=re.sub(r'\b(chapter|chapters|Theorem|section|sections|volume|volumes|appendices)(?=\d)',r'\1 ',s)
    s=re.sub(r'(?<=\d)(?=(?:October|publisher|hardback|first|second|standard|page))',' ',s)
    return s

out=[]
for p in PROFILES:
    original=req[p['id']]; rid=p['id']
    assigned=[a for a in allocations if a['id']==rid]
    assert len(assigned)==len(original['unit_ids'])
    for i,a in enumerate(assigned,1):assert int(a['ordinal'])==i
    parent_ids=sorted({c['component_id'] for uid in original['unit_ids'] for c in units[uid]['required_components']})
    present=[]
    for label in p['anchors']:
        if len(anchors.get(label,[]))!=1:raise ValueError(f'{rid}: {label} has {len(anchors.get(label,[]))} bindings')
        present += anchors[label]
    subs=[]
    for n,c in enumerate(p['components'],1):
        assert c['sources'] and all(1<=i<=len(assigned) for i in c['sources'])
        subs.append(dict(component_id=f'{rid}-MAP-{n:02}',parent_component_ids=parent_ids,description=spaced(c['text']),source_ordinals=c['sources'],success_condition='Supply the exact mapped goal with its source-specific hypotheses and evidence: '+spaced(c['text']),failure_condition=spaced(p['failure']),required_source_extent=[dict(source_key=assigned[i-1]['key'],extent=spaced(assigned[i-1]['required_extent']),conditions=spaced(assigned[i-1]['conditions'])) for i in c['sources']]))
    additional=[dict(source_key=key,extent=spaced(extent),role=role,bibliographic_identity=identity(key)) for key,extent,role in dependencies.get(rid,[])]
    related=[dict(original_requirement_id=k,unit_ids=req[k]['unit_ids'],role='reader_interface',relation='Shared topic/proof comparison; not automatically an external premise or an alias.') for k in p['related']]
    patches=[]
    for ordinal,a in enumerate(assigned,1):
        uid=original['unit_ids'][ordinal-1]
        assert uid==f'ED26-REQ-{rid}-{ordinal:02}'
        old=units[uid]; patch=copy.deepcopy(old)
        selected=[c for c in subs if ordinal in c['source_ordinals']]; assert selected
        primary=dict(source_id=a['key'],original_source_literal=old['source_presentations'][0]['source_id'],bibliographic_identity=identity(a['key']),precise_extent=spaced(a['required_extent']),source_role=spaced(a['source_role']),conditions=spaced(a['conditions']),version='Exact original publication/edition recorded in the literal bibliography or additional identity record; reprints/errata retain explicit roles.',allocated_subcomponent_ids=[c['component_id'] for c in selected],body_acquisition_standing='Complete local body acquisition, all required extents and source-native proofs have not been qualified by this mapping task.')
        if a['key']=='CintulaHajekNoguera2011':primary['constituent_presentations']=fuzzy_constituents
        if a['key']=='Martin1984':primary['constituent_presentations']=[dict(authors='Robert L.Martin;Peter W.Woodruff',title='On Representing True-in-L in L',pages='47–51',version='1984 reprint'),dict(author='Saul A.Kripke',title='Outline of a Theory of Truth',pages='53–81',version='1984 reprint'),dict(author='Robert L.Martin',title='Editor introduction',extent='Direct comparison of the two selected fixed-point presentations',version='1984')]
        patch['source_presentations']=[primary]
        for c in patch['required_components']:
            c['required_source_extent']=dict(original_scope=original['original_register_row'],source_key=a['key'],precise_extent=spaced(a['required_extent']),conditions=spaced(a['conditions']),standing='Resolved finite source allocation; future body reading/writing remains owed.')
            c['allocated_subcomponent_ids']=[s['component_id'] for s in selected]
            c['success_condition']='Complete this exact original source allocation and its mapped subcomponents: '+spaced(a['required_extent'])
            c['failure_condition']=spaced(p['failure'])+' '+spaced(a['conditions'])
        patch['required_subcomponents']=selected
        patch['prerequisites']=[dict(named_premise=s,role='internal_setup',supply_rule='Define and prove the exact needed setup before use, or bind an already completed matching treatment; no unidentified import assumed.') for s in p['setup']]
        patch['prerequisites'] += [dict(named_premise=d['extent'],role=d['role'],source_key=d['source_key'],required_source_extent=d['extent'],bibliographic_identity=d['bibliographic_identity']) for d in additional]
        body=f"handbook/parts/{p['part']}/presentations/{rid.lower()}-{ordinal:02}.tex"
        annex=f"handbook/annex/{p['part']}/{rid.lower()}-{ordinal:02}.tex"
        label=f"sec:{p['part']}-{rid.lower()}-{ordinal:02}"
        patch['destination']=dict(body=dict(existing_common_goal_anchors=present,proposed_source_presentation=body,proposed_label=label),annex=dict(proposed_source_proof_destination=annex,label_prefix=f"annex:{p['part']}.{rid.lower()}.{ordinal}",applicability='Formal definitions/results receive full supporting derivations; philosophical claims receive explicit arguments. Do not invent a mathematical proof for a normative position.'),lookup=dict(body_path=body,entry_label=label,keys=[rid,a['key'],original['original_wording']]))
        patch['destination_rule']='Reuse an actually identical source treatment where it exists; proposed paths are precise assignments, not newly created or routed chapters.'
        patch['reader_interfaces']=related
        patch['source_state']='identified_missing'
        patch['source_state_explanation']='This proposal identifies exact sources but does not establish qualified complete local body availability. Existing held artifacts may satisfy later qualification; their existence is not denied.'
        patch['scope_state']='resolved';patch['unresolved_questions']=[]
        patch['mapping_stage']='explicit_nonclassical_goal_and_separate_source_allocation'
        patch['remaining_work']=original['current_assessment'].get('remaining_book_work',[]) + ['Acquire/qualify and read each exact original source/version extent and correction companion.','Complete every allocated source-native presentation, unsupplied proof, formal diagnosis and philosophical argument.','Integrate existing/proposed body, annex and source/task lookup entries with accurate statuses.','Run consolidated independent checks only after the complete requested change set is written.']
        patch['evidence'] += ['spec/coverage/edition-2026/nonclassical-019-035/goal_profiles.py','spec/coverage/edition-2026/nonclassical-019-035/source_allocations.tsv','spec/coverage/edition-2026/nonclassical-additional-identities.json','spec/research/edition-2026-map-nonclassical-019-035.md','spec/research/edition-2026-truth-source-extent-evidence.md']
        patch['current_declaration_bindings']=present
        patches.append(patch)
    out.append(dict(original_requirement_id=rid,original_wording=original['original_wording'],original_register_row=original['original_register_row'],unit_ids=original['unit_ids'],parent_component_ids_preserved=parent_ids,required_subcomponents=subs,unit_patches=patches,present_destinations=present,original_inventory_destinations_preserved=original['present_destinations'],additional_bounded_dependencies=additional,reader_interfaces=related,mapping_state='resolved',scope_state='resolved',unresolved_questions=[],current_assessment=original['current_assessment'],preserve_current_assessment=True,remaining_work=original['current_assessment'].get('remaining_book_work',[])+['Complete each explicit source allocation and exact mapped subcomponent; source/proof/publication acceptance is not established by the map.']))

outfile=HERE/('proposals'+SUFFIX+'.jsonl')
if outfile.exists():raise SystemExit('Refusing to overwrite the published proposal batch')
outfile.write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in out),encoding='utf-8')
(HERE/('local-additional-identities'+SUFFIX+'.json')).write_text(json.dumps(local_extra,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(HERE/('fuzzy-constituents'+SUFFIX+'.json')).write_text(json.dumps(fuzzy_constituents,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
receipt=dict(requirements=len(out),source_unit_patches=sum(len(r['unit_patches']) for r in out),mathematical_or_argument_subcomponents=sum(len(r['required_subcomponents']) for r in out),original_source_ordinals_preserved=True,original_wording_register_assessment_preserved=True,parent_component_ids_preserved=True,all_selected_current_anchors_unique=True,manuscript_content_acceptance=False,sha256=hashlib.sha256(outfile.read_bytes()).hexdigest(),files_read=read_receipts,standing='Finite coverage proposal, not canonical integration or manuscript completion.')
receipt['revision']=SUFFIX or 'initial'
receipt['supersedes']='proposals.jsonl' if SUFFIX else None
(HERE/('receipt'+SUFFIX+'.json')).write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False))

"""Compile the finite N-c decisions without changing canonical map ownership."""
from pathlib import Path
from datetime import datetime, timezone
import copy, csv, hashlib, json, re, sys

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
BASE = ROOT / 'spec/coverage/edition-2026'
sys.path.insert(0, str(ROOT / 'tools'))
import check as grammar

def read_jsonl(path):
    return [json.loads(s) for s in path.read_text(encoding='utf-8-sig').splitlines() if s.strip()]

requirements = {r['original_requirement_id']: r for r in read_jsonl(BASE/'requirements-crosswalk.jsonl')}
units = {u['unit_id']: u for u in read_jsonl(BASE/'requirements-units.jsonl')}
candidates = {(r['requirement_id'], r['source_ordinal']): r for r in json.loads((ROOT/'tmp/edition-2026-map-requirements/source-identity-candidates.json').read_text(encoding='utf-8-sig'))}
with (OUT/'goal-profiles.tsv').open(encoding='utf-8', newline='') as stream:
    profiles = list(csv.DictReader(stream, delimiter='\t'))
assert len(profiles) == 40
assert {p['id'] for p in profiles} == {f'N-c-{i:03}' for i in range(1,41)}

bibtext = (ROOT/'handbook/bib/handbook.bib').read_text(encoding='utf-8-sig')
bib = {}
for match in re.finditer(r'@[A-Za-z]+\s*\{', bibtext):
    args, end = grammar.scan_braced_args(bibtext, match.end()-1, 1)
    if not args or ',' not in args[0]:
        continue
    key = args[0].split(',',1)[0].strip()
    literal = bibtext[match.start():end]
    fields = {}
    for field in ['author','title','year','edition','pages','doi','url','booktitle','journaltitle','publisher','volume']:
        fm = re.search(r'\b'+field+r'\s*=\s*\{', literal, re.I)
        if fm:
            fa, _ = grammar.scan_braced_args(literal, fm.end()-1, 1)
            if fa: fields[field] = fa[0]
    bib[key] = {'key':key, **fields, 'path':'handbook/bib/handbook.bib', 'line':bibtext.count('\n',0,match.start())+1, 'literal_record':literal}
extra = {r['key']:r for r in json.loads((OUT/'identity-additions.json').read_text(encoding='utf-8'))['sources']}
def identity(key):
    if key in extra: return extra[key]
    if key in bib: return bib[key]
    raise ValueError('Unidentified citation key '+key)

key_overrides = {('N-c-039',1):'PaulinMohring1989Extraction',('N-c-039',2):'Letouzey2003Extraction',('N-c-040',1):'PaulsonBlanchette2010Sledgehammer'}
source_notes = {
    1:'p09-source-presentations-lot1.md',2:'p09-source-presentations-lot1.md',3:'p09-source-presentations-lot1.md',4:'p09-source-presentations-lot1.md',5:'p09-source-presentations-lot1.md',6:'p09-source-presentations-lot1.md',7:'p09-source-presentations-lot1.md',8:'p09-source-presentations-lot1.md',
    **{n:'p09-source-presentations-lot2-3.md' for n in range(9,19)},
    **{n:'p09-source-presentations-lot4.md' for n in [19,20,21,22,23,24,25,26,28]},
    **{n:'p12-new-content.md' for n in range(31,41)}
}
note_texts = {name:(ROOT/'spec/research'/name).read_text(encoding='utf-8-sig') for name in set(source_notes.values())}

def note_locator(number, rid, ordinal):
    name = source_notes.get(number)
    if not name:
        return {'path':'spec/research/edition-2026-map-computational-requirements.md','section':rid,'standing':'Actual current LaTeX and exact canonical bibliography supply the mapped goal; no new source-body qualification.'}
    text = note_texts[name]
    heads = list(re.finditer(r'^## .*$',text,re.M))
    selected = next((h for h in heads if rid in h.group()),None)
    if selected:
        next_head = next((h for h in heads if h.start()>selected.start()),None)
        end = next_head.start() if next_head else len(text)
        subheads = list(re.finditer(r'^### .*$',text[selected.end():end],re.M))
        start = selected.start()
        if ordinal <= len(subheads):
            start = selected.end()+subheads[ordinal-1].start()
            if ordinal < len(subheads): end = selected.end()+subheads[ordinal].start()
        return {'path':'spec/research/'+name,'start_line':text.count('\n',0,start)+1,'end_line':text.count('\n',0,end)+1,'extent_basis':'The exact requirement/source subsection records existing source locators, held-body evidence and unequal proof standing. Its historical acceptance statements are not renewed here.'}
    return {'path':'spec/research/'+name,'section':'Source accounting and construction-method packages','extent_basis':'Existing P12 source note; original row and explicit allocated subgoals govern, not its superseded phase ceilings.'}

additional = {
    'N-c-010': [('BaaderBrandtLutz2005TR','external_proof_dependency','LTCS-05-01 normalization/completion and countermodel lemmas supporting the 2005 conference results; corrected handbook method retains separate attribution.'),('W3COWL2Profiles2012','normative_definition_dependency','2012 OWL 2 EL/QL/RL profile grammars, permitted restrictions and exact reasoning/task complexity qualifications.'),('W3COWL2Syntax2012','normative_definition_dependency','2012 OWL 2 structural syntax and global restrictions used in the family/profile map.'),('W3COWL2DirectSemantics2012','normative_definition_dependency','2012 OWL 2 direct semantics for the displayed expressive-language reasoning tasks.')],
    'N-c-012':[('AlpernSchneider1985','external_proof_dependency','The exact safety/liveness definitions and decomposition theorem for infinite behaviors; provide the decomposition construction and topology/prefix prerequisites used by this requirement.')],
    'N-c-018':[('Walukiewicz2000','external_proof_dependency','The full equational weak-completeness bridge actually cited by the current Kozen entry, with exact calculus translation and hypotheses.'),('Safra1995Extended','external_proof_dependency','The expanded determinization construction actually used in the current monitor/nondeterminization chain; not a substitute for registered Safra 1988 or 2007 survey identity.')],
    'N-c-029':[('Wells1999','external_proof_dependency','The exact Curry-style checking/typability undecidability result cited by the current comparison; preserve Church/Curry input distinctions.')],
    'N-c-030':[('AbelCoquandDybjer2007','external_proof_dependency','Functions-and-one-Russell-universe normalization-by-evaluation and typed equality theorem actually cited by the current entry; does not cover the full selected MLTT sheet.')],
    'N-c-036':[('BachmairGanzinger2001','external_proof_dependency','The exact ordering/selection/saturation completeness presentation cited by the live sheet and theorem, in addition to the separately registered 1994 article.')]
}

version_decisions = {
    'ComonEtAl2007':'Fixed online monograph release 18 November 2008, already selected in the active text; the original 2007 attribution denotes the evolving work. Retain exact release artifact and date.',
    'ClarkeEmerson1981':'1981 workshop contribution published 1982, 52-71. Authorized 2008 reprint and longer manuscript retain separate manifestation/proof extents.',
    'EenSorensson2003':'SAT 2003 contribution published in LNCS proceedings in 2004, 502-518; preserve conference and publication dates.',
    'Thomas1997':'Final 1997 Handbook of Formal Languages chapter, 389-455. The held May 1996 Kiel report is a separate precursor and not source completion.',
    'McMillan1993':'Revised Kluwer 1993 book, xvii+194 pages; May 1992 CMU thesis is separate.',
    'EbbinghausFlum1995':'1995 first edition, not the 1999 second edition or another finite-model text.',
    'BaaderEtAl2003':'2003 first edition, not a later edition of the Description Logic Handbook.',
    'BradfieldStirling2007':'Final 2007 Handbook of Modal Logic chapter 721-756; held 2005 preprint internal locators remain separate.',
    'AndrekaVanBenthemNemeti1998':'1998 Journal of Philosophical Logic article 217-274; 1996 ILLC preprint is distinct.',
    'Buchi1960':'1960 journal article 66-92; held 1959 report is a separate version.',
    'Trakhtenbrot1961':'1961 announcement 326-329; 1962 expansion remains separate in date, title, pages and theorem scope.',
    'Safra1988':'1988 FOCS article 319-327; 1995 expanded work is separate.',
    'ThatcherWright1968':'1968 Mathematical Systems Theory 2(1), 57-81, DOI 10.1007/BF01691346; no abstract, report lead or dissertation substitute.',
    'SistlaClarke1985':'1985 corrected JACM article 733-749; 1982 STOC predecessor does not control the repaired regular-operator chain.'
}

body_receipts = {}
def bind_current(row):
    bindings = []
    originals=[]
    for old in row['present_destinations']:
        if old.get('label')=='annex:p9.alc.1–.3':
            # This inventory shorthand is not a literal label and its first
            # item is in a different file. Resolve the actual declarations.
            for label in ['annex:p9.alc.1','annex:p9.alc.2','annex:p9.alc.3']:
                locations=[]
                for path in (ROOT/'handbook/annex/p09').glob('*.tex'):
                    raw=path.read_text(encoding='utf-8-sig')
                    if re.search(r'\\begin\{annexitem\}\s*\{'+re.escape(label)+r'\}',raw):
                        locations.append(path)
                assert len(locations)==1,(label,locations)
                d=copy.deepcopy(old);d['path']=locations[0].relative_to(ROOT).as_posix();d['label']=label
                d['original_inventory_shorthand']=copy.deepcopy(old)
                originals.append(d)
        else:
            originals.append(old)
    for old in originals:
        d = copy.deepcopy(old)
        path = ROOT / d['path']
        assert path.is_file(),d
        raw = path.read_text(encoding='utf-8-sig')
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        body_receipts[d['path']] = {'path':d['path'],'sha256':sha,'line_count':len(raw.splitlines()),'reading_standing':'Structural destination/source-reference extraction; selected substantive passages read as recorded in the mapper note, not a new full-text proof review.'}
        label = d.get('label')
        if label:
            pattern = r'\\label\s*\{'+re.escape(label)+r'\}|\\begin\s*\{(?:hb\w+|proofboundary|annexitem)\}\s*\{'+re.escape(label)+r'\}'
            matches = list(re.finditer(pattern,raw))
            assert len(matches)==1,(row['original_requirement_id'],label,len(matches))
            d['line'] = raw.count('\n',0,matches[0].start())+1
            d['binding']='unique active literal label in preserved path'
        else:
            assert 1 <= d['line'] <= len(raw.splitlines())
            d['binding']='preserved actual file interval; no invented label'
        d['sha256']=sha
        d['declared_evidence_only']=True
        bindings.append(d)
    return bindings

output = []
source_allocations = []
for profile in profiles:
    rid=profile['id']; number=int(rid[-3:]); original=requirements[rid]
    original_ids=original['unit_ids']
    count=len(original_ids)
    parent_ids=sorted({c['component_id'] for uid in original_ids for c in units[uid]['required_components']})
    components=[]
    for i,item in enumerate(profile['components'].split('||'),1):
        sources,desc=item.split('#',1); ords=[int(s) for s in sources.split(',')]
        assert all(1<=s<=count for s in ords)
        components.append({'component_id':f'{rid}-MAP-{i:02}','parent_component_ids':parent_ids,'description':desc,'source_ordinals':ords,
            'success_condition':'Supply this exact named mathematical/source subgoal, with all hypotheses, defined objects, claimed proof or method steps and a retrievable body/annex entry: '+desc,
            'failure_condition':'A required case, hypothesis, source presentation or promised proof step is absent or is supplied only by a different version. '+profile['conditions'],
            'required_source_extent':{'original_requirement_id':rid,'allocated_goal':desc,'scope_conditions':profile['conditions']}})
    assert set(range(1,count+1))=={s for c in components for s in c['source_ordinals']}
    present=bind_current(original)
    deps=[{'source_key':key,'role':role,'named_premise':extent,'required_source_extent':extent,'bibliographic_identity':identity(key)} for key,role,extent in additional.get(rid,[])]
    part_num=int(original['original_register_row']['target_part'][1:]); part=f'p{part_num:02}'
    patches=[]
    for ordinal,uid in enumerate(original_ids,1):
        assert uid==f'ED26-REQ-{rid}-{ordinal:02}'
        old=units[uid]; candidate=candidates[(rid,ordinal)]
        if (rid,ordinal) in key_overrides: key=key_overrides[(rid,ordinal)]
        else:
            assert len(candidate['candidates'])==1,(rid,ordinal,candidate)
            key=candidate['candidates'][0]['key']
        ident=identity(key)
        assert ident.get('title'),key
        selected=[c for c in components if ordinal in c['source_ordinals']]
        extent={'source_key':key,'original_source_ordinal':ordinal,'allocated_subgoals':[c['description'] for c in selected],
            'source_extent_rule':'Complete the exact named treatment in this identified source, including definitions, statements, proofs, constructions, examples and limitations supporting the allocated goals; the original whole requirement and inherited source obligations are retained. This is not a whole unrelated book expansion.',
            'source_locator_evidence':note_locator(number,rid,ordinal),'scope_conditions':profile['conditions'],
            'proof_obligation_rule':'A source-sketched/external step keeps its attributed source standing. Supply every separate full-proof obligation; old S/P labels or historical completion assertions cannot erase it.'}
        version=version_decisions.get(key,ident.get('version','Exact publication/edition identified by the literal bibliographic record; variants and later corrected copies require explicit separate identification.'))
        source={'source_id':key,'original_source_literal':candidate['source_literal'],'bibliographic_identity':ident,'version':version,'precise_extent':extent,
            'allocated_subcomponent_ids':[c['component_id'] for c in selected],'identification_evidence':[note_locator(number,rid,ordinal),{'path':'spec/coverage/edition-2026/computational-requirements/identity-additions.json' if key in extra else 'handbook/bib/handbook.bib','key':key}],
            'body_acquisition_standing':'This mapping identifies the exact required body/extent; it does not newly certify completeness of source acquisition. Existing qualified captures stay preserved and missing exact-version bodies remain writing dependencies.'}
        patch=copy.deepcopy(old)
        patch['source_presentations']=[source]
        for c in patch['required_components']:
            c['required_source_extent']=copy.deepcopy(extent)
            c['allocated_subcomponent_ids']=[s['component_id'] for s in selected]
            c['success_condition']='Complete this exact separately identified source allocation: '+'; '.join(s['description'] for s in selected)
            c['failure_condition']=profile['conditions']+' Any unfilled allocated case or promised proof leaves the source treatment incomplete.'
        patch['required_subcomponents']=copy.deepcopy(selected)
        patch['prerequisites']=[{'named_premise':p.strip(),'role':'internal_setup','supply_rule':'Define and prove the required setup within this treatment or bind an exact completed theorem before use; no unspecified mathematical result is silently assumed.'} for p in profile['setup'].split(';')]
        patch['prerequisites']+=copy.deepcopy(deps)
        if rid in ['N-c-031','N-c-038']:
            patch['prerequisites'].append({'named_premise':'The exact assistant/kernel versions already declared in the live cross-part entries, with matching official syntax, kernel and trusted-base documentation frozen at the edition cutoff.','role':'versioned_documentation_dependency','supply_rule':'Preserve current pinned version identifiers; verify their matching official documentation before accepting implementation claims. Historical papers are not current-version evidence.'})
        proposed_body=f'handbook/parts/{part}/presentations/{rid.lower()}-{ordinal:02}.tex'
        proposed_annex=f'handbook/annex/{part}/{rid.lower()}-{ordinal:02}.tex'
        proposed_label=f'sec:{part}-{rid.lower()}-{ordinal:02}'
        patch['destination']={'body':{'existing_common_goal_anchors':present,'proposed_source_presentation':proposed_body,'proposed_label':proposed_label},'annex':{'proposed_source_proof_destination':proposed_annex,'label_prefix':f'annex:p{part_num}.{rid.lower()}.{ordinal}'},'lookup':{'body_path':proposed_body,'entry_label':proposed_label,'keys':[rid,key,original['original_wording']]}}
        patch['destination_rule']='Reuse and bind existing exact source treatment when present; these disjoint proposed destinations identify missing material and do not authorize duplicate authoring or create files.'
        patch['source_state']='identified_missing' if key in ['ThatcherWright1968','Thomas1997','McMillan1993','EbbinghausFlum1995','ClarkeGrumbergPeled1999','PaulinMohring1989Extraction','Letouzey2003Extraction','PaulsonBlanchette2010Sledgehammer'] else 'mixed'
        patch['source_state_explanation']='Existing source notes/bibliography identify the work. Complete exact-version body qualification is retained as an explicit outstanding task where not established; this conservative map grants no new acquisition credit.'
        patch['scope_state']='resolved';patch['unresolved_questions']=[]
        patch['mapping_stage']='computational_finite_goal_and_separate_source_allocation'
        patch['current_declaration_bindings']=present
        patch['remaining_work']=list(original['current_assessment'].get('remaining_book_work',[]))+['Apply the later mapping delta before reusing stale inventory conclusions; preserve the original assessment as history.','Qualify every exact required source body/extent and correction companion; complete all unsupplied allocated components and promised proofs.','Integrate exact body, proof annex and lookup targets, then include the completed changes in consolidated independent checks.']
        patch['evidence'] += ['spec/coverage/edition-2026/computational-requirements/goal-profiles.tsv','spec/research/edition-2026-map-computational-requirements.md']
        patch['later_mapping_delta']={'scope_only':True,'conditions':profile['conditions'],'content_acceptance':False}
        if rid=='N-c-010':
            patch['later_mapping_delta']['current_correction']='Current n-c-010.tex lines 8-24, 470-526 and 779-817 define three corrections, CR8 feature support, marked decision criterion, complete soundness/countermodel derivation and polynomial marked-run classification. The inventory statements that these are only proposed are stale; independent correctness is not renewed by this map.'
        if rid=='N-c-036':
            patch['later_mapping_delta']['source_citation_boundary']='The live completeness entry cites BachmairGanzinger2001. Preserve this additional presentation; it does not discharge the original BachmairGanzinger1994 unit.'
        if rid=='N-c-037':
            patch['later_mapping_delta']['source_correction_task']='The live critical-pair definition cites Huet1973, whose exact canonical identity is third-order unification undecidability. Correct this inappropriate source citation in the later authorized writing batch while retaining Huet1980 and the registered 1973 unification presentation separately.'
        patches.append(patch)
        source_allocations.append({'unit_id':uid,'requirement_id':rid,'source_ordinal':ordinal,'original_source_literal':candidate['source_literal'],'source_key':key,'version':version,'precise_extent':extent})
    output.append({'original_requirement_id':rid,'original_wording':original['original_wording'],'original_register_row':original['original_register_row'],'unit_ids':original_ids,'parent_component_ids_preserved':parent_ids,'required_subcomponents':components,'unit_patches':patches,'present_destinations':present,'original_inventory_destinations_preserved':original['present_destinations'],'additional_bounded_dependencies':deps,'reader_interfaces':[],'mapping_state':'resolved','scope_state':'resolved','unresolved_questions':[],'current_assessment':original['current_assessment'],'preserve_current_assessment':True,'remaining_work':original['current_assessment'].get('remaining_book_work',[])+['Apply source-specific later deltas, then supply every exact allocated source presentation and component. Map completion supplies no proof/source/publication acceptance.']})

proposal=OUT/'proposals.jsonl'
assert not proposal.exists(),'Refusing to overwrite published proposal'
proposal.write_text(''.join(json.dumps(p,ensure_ascii=False,separators=(',',':'))+'\n' for p in output),encoding='utf-8')
(OUT/'source-allocations.jsonl').write_text(''.join(json.dumps(p,ensure_ascii=False,separators=(',',':'))+'\n' for p in source_allocations),encoding='utf-8')
(OUT/'current-destination-receipts.json').write_text(json.dumps(list(body_receipts.values()),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
receipt={'created_utc':datetime.now(timezone.utc).isoformat(),'requirements':len(output),'source_unit_patches':sum(len(p['unit_patches']) for p in output),'subcomponents':sum(len(p['required_subcomponents']) for p in output),'original_wording_assessment_and_unit_ids_preserved':True,'original_component_ids_preserved':True,'all_source_ordinals_allocated':True,'all_selected_current_labels_unique':True,'sha256':hashlib.sha256(proposal.read_bytes()).hexdigest(),'scope_state':'resolved','source_or_mathematical_acceptance':False,'input_sha256':{n:hashlib.sha256((OUT/n).read_bytes()).hexdigest() for n in ['goal-profiles.tsv','identity-additions.json']}}
(OUT/'receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False))

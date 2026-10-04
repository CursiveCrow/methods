"""Freeze root-confirmed applied batch6 state; write only owned preparation outputs."""
from pathlib import Path
import copy,csv,difflib,hashlib,io,json,subprocess,sys
from datetime import datetime,timezone
import prepare_batch6 as prep

ROOT=prep.ROOT
OUT=prep.OUT
BASE=prep.BASE
EXPECTED={
    'handbook/registry/symbols.csv':'50c1dc7a64aedeaa0ed158c6b0387fe61f1ee351c5e0a7ac51e1686c4546ef7f',
    'handbook/registry/symbol-scopes.json':'3206b04c7f88a93c53ad4469db584593ac0a37d7c6ab48cf913e7d6974003167',
    'handbook/bib/handbook.bib':'bf45ec432d08faf4adf3d8440977b0370874aa9d30858ebd586b4fc9e56b6075',
}

def main():
    now=datetime.now(timezone.utc).isoformat()
    before={p:prep.sha(ROOT/p) for p in EXPECTED}
    if before!=EXPECTED:raise ValueError('Actual canonical state differs from root-confirmed ready10 hashes; do not freeze or prepare against a stale state')
    original=json.loads(prep.read(OUT/'ready10-summary.json'))
    manifest=json.loads(prep.read(ROOT/'spec/research/edition-2026-authoring-batch-intake-6.json'))
    names=[name for group in original['application_order'].values() for name in group]
    proposals={name:{'sha256':prep.sha(OUT/name),'text':prep.read(OUT/name)} for name in names}
    baseline=prep.capture_numeric_meanings('post-ready10-numeric-baseline',standing='Actual root-confirmed canonical state after initial two and ready10 applied. Captured BEFORE pending Hintikka/Abelian routing. Original preB6/post-initial captures and source roles remain preserved; no source/proof/publication admission.')
    if baseline['canonical_row_count']!=6276 or baseline['canonical_bib_count']!=1262:raise ValueError('Wrong applied counts')
    patched={p:prep.read(ROOT/p) for p in EXPECTED}
    applied_usage=proposals['batch6-ready10-proposal-existing-scope-usage-01.patch']['text']
    applied_usage='\n'.join(line+',' if line[:1] in {'-','+'} and line.endswith('}') else line for line in applied_usage.splitlines())+'\n'
    prep.save('ready10-root-corrected-scope-usage',{'standing':'Actual correction reported applied by root; original proposal retained unchanged','original_proposal_sha256':proposals['batch6-ready10-proposal-existing-scope-usage-01.patch']['sha256'],'root_applied_correction':applied_usage})
    evidence=[]
    for n,row in enumerate(csv.DictReader(io.StringIO(patched['handbook/registry/symbols.csv'])),2):
        if row['macro'] in {'gamma_pair','x_b'} or row['glyph'].find('gamma')>=0 and 'pairwise' in row['role']:
            evidence.append({'canonical_line':n,'row':row})
    citation=BASE/'parts/p07/hott-circle-encode-decode.tex'
    cite_lines=[{'line':n,'text':line} for n,line in enumerate(prep.read(citation).splitlines(),1) if 'HoTT2013PublicReleaseFoundations' in line]
    history={'utc':now,'root_confirmation':'All22 ready10 ordered patches actually applied; canonical6276 symbol rows/1262 bibliography keys. Initial2 merge history remains immutable; no replay.',
        'original_summary':original,'original_summary_sha256':prep.sha(OUT/'ready10-summary.json'),'original_proposals':proposals,
        'original_manifest_sha256':original['manifest_sha256'],'current_manifest':manifest,'actual_canonical_sha256':before,
        'actual_canonical_text':patched,'numeric_control_baseline':'post-ready10-numeric-baseline.json','numeric_control_baseline_sha256':prep.sha(OUT/'post-ready10-numeric-baseline.json'),
        'root_applied_corrections':[
            {'kind':'patch-syntax','detail':'existing-host scope usage01 required trailing commas on four minus/plus lines; corrected applied text separately preserved'},
            {'kind':'provenance-notes','detail':'New numeric migration notes use pre-batch6, not pre-batch5; prior existing B5 notes are not retroactively rewritten'},
            {'kind':'reader-citation','path':citation.relative_to(ROOT).as_posix(),'sha256':prep.sha(citation),'actual_citation_lines':cite_lines,'detail':'Root collapsed duplicated HoTT alias citation'},
            {'kind':'semantic-row','detail':'gamma_pair is the host strict pairwise role, not the1995 source; x_b fixed-parameter note states native x_a equiv a','actual_rows':evidence}],
        'standing':'Factual merge history only. Original raw intakes/source versions preserved. No mathematical proof/source/publication acceptance.'}
    if (OUT/'ready10-merged-history.json').exists():raise ValueError('Do not overwrite applied merge history')
    prep.save('ready10-merged-history',history)
    selected=[g for g in manifest['groups'] if g['integration_status'].startswith('merged')]
    if len(selected)!=12:raise ValueError('Need exactly12 merged groups for incoming verification; keep pending2 outside current graph')
    verification={'standing':'Actual12 merged batch6 groups only; pending Hintikka/Abelian retained in full intake manifest and excluded from this route-only incoming check. No source/proof/admission review.','scope':manifest['scope'],'groups':selected,'pending_groups':[g['stem'] for g in manifest['groups'] if not g['integration_status'].startswith('merged')],'canonical_sha256':before}
    prep.save('applied12-wiring-manifest',verification)
    if (OUT/'applied12-wiring-result.json').exists():raise ValueError('Existing once-only incoming result: do not run another wave')
    command=[sys.executable,str(OUT.parent/'inspect_oct3_author_wiring.py'),'--manifest',(OUT/'applied12-wiring-manifest.json').relative_to(ROOT).as_posix()]
    run=subprocess.run(command,text=True,encoding='utf-8',capture_output=True,check=True)
    result=json.loads(run.stdout)
    result['utc']=datetime.now(timezone.utc).isoformat()
    result['command']=command
    result['manifest_sha256']=prep.sha(OUT/'applied12-wiring-manifest.json')
    result['canonical_before']=before
    result['canonical_after']={p:prep.sha(ROOT/p) for p in EXPECTED}
    result['canonical_changed_during_read']=[p for p in EXPECTED if result['canonical_after'][p]!=before[p]]
    prep.save('applied12-wiring-result',result)
    print(json.dumps({'utc':result['utc'],'groups':len(result['groups']),'pairs':sum(g['proved_pairs'] for g in result['groups']),'rows':result['canonical_symbol_rows'],'bib':result['canonical_bib_keys'],'errors':result['errors'],'canonical_changed':result['canonical_changed_during_read'],'history_sha256':prep.sha(OUT/'ready10-merged-history.json'),'baseline_sha256':prep.sha(OUT/'post-ready10-numeric-baseline.json'),'baseline_chapters':len(baseline['chapters']),'numeric_rows':len(baseline['numeric_rows'])}))

if __name__=='__main__':main()

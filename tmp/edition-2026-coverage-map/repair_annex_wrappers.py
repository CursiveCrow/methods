"""One bounded mechanical repair of four unsupported annex wrappers."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"tools"))
import check as grammar
targets=[("p15","huber-information-game"),("p15","huber-joint-endpoints"),("p15","huber-remaining-methods"),("p19","mental-rotation-and-spatial-reasoning")]
planned=[]
for part,slug in targets:
    bodypath=ROOT/f"handbook/parts/{part}/{slug}.tex"
    annexpath=ROOT/f"handbook/annex/{part}/{slug}.tex"
    body=grammar.strip_verbatims(grammar.strip_comments(bodypath.read_text(encoding="utf-8-sig")))
    declarations={}
    for m in grammar.HB_ENV_RE.finditer(body):
        if m.group(1) not in grammar.HB_STATUS_ENVS: continue
        args,_=grammar.scan_braced_args(body,m.end(),3)
        if len(args)==3:
            if args[0] in declarations:raise SystemExit("Duplicate body label "+args[0])
            declarations[args[0]]={"status":args[1],"title":args[2]}
    original=annexpath.read_text(encoding="utf-8-sig")
    pattern=re.compile(r"\\begin\{hbproof\}\{([^{}]+)\}\{([^{}]+)\}([\s\S]*?)\\end\{hbproof\}")
    blocks=list(pattern.finditer(original))
    if not blocks:raise SystemExit("No unrepaired wrappers in "+str(annexpath))
    assert len(blocks)==original.count(r"\begin{hbproof}")==original.count(r"\end{hbproof}")
    expected=[]
    def replace(m):
        label,backref,payload=m.groups()
        if r"\begin{proof}" in payload or r"\begin{annexitem}" in payload:raise ValueError("Unexpected nested proof wrapper")
        declaration=declarations[backref]
        if declaration["status"]!="proved="+label:raise ValueError("Nonreciprocal body target "+backref)
        expected.append({"annex_label":label,"body_label":backref,"title":declaration["title"],"payload_sha256":hashlib.sha256(payload.encode()).hexdigest()})
        return r"\begin{annexitem}{"+label+"}{"+backref+"}{"+declaration["title"]+"}\n"+r"\begin{proof}"+payload+r"\end{proof}"+"\n"+r"\end{annexitem}"
    rewritten=pattern.sub(replace,original)
    assert "hbproof" not in rewritten
    planned.append({"annexpath":annexpath,"bodypath":bodypath,"old":original,"new":rewritten,"old_sha256":hashlib.sha256(annexpath.read_bytes()).hexdigest(),"blocks":expected})
assert sum(len(x["blocks"]) for x in planned)==39
receipt_path=ROOT/"spec/research/edition-2026-annex-wrapper-repair.json"
if receipt_path.exists():raise SystemExit("Preserve prior repair receipt")
records=[]
for item in planned:
    item["annexpath"].write_text(item["new"],encoding="utf-8")
    actual=item["annexpath"].read_text(encoding="utf-8")
    restored=actual
    for block in item["blocks"]:
        start=r"\begin{annexitem}{"+block["annex_label"]+"}{"+block["body_label"]+"}{"+block["title"]+"}\n"+r"\begin{proof}"
        oldstart=r"\begin{hbproof}{"+block["annex_label"]+"}{"+block["body_label"]+"}"
        assert restored.count(start)==1
        restored=restored.replace(start,oldstart,1)
    restored=restored.replace(r"\end{proof}"+"\n"+r"\end{annexitem}",r"\end{hbproof}")
    assert restored==item["old"],"Unexpected mathematical/text change"
    records.append({"annex_path":item["annexpath"].relative_to(ROOT).as_posix(),"body_path":item["bodypath"].relative_to(ROOT).as_posix(),"before_sha256":item["old_sha256"],"after_sha256":hashlib.sha256(item["annexpath"].read_bytes()).hexdigest(),"all_original_proof_payloads_preserved":True,"reciprocal_entries":item["blocks"]})
receipt={"date_utc":datetime.now(timezone.utc).isoformat(),"files":records,"entries":39,"scope":"Mechanical integration repair only. Existing derivation payloads and labels are unchanged; no new mathematical or independent acceptance is claimed.","consolidated_production_checks":"pending the complete writing/integration batch"}
receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"files":len(records),"entries":39,"all_payloads_preserved":True,"all_body_targets_reciprocal":True,"receipt":str(receipt_path)}))

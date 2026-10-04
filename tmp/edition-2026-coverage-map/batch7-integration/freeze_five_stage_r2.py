"""Freeze corrected R2 proposals and raw input bytes. No application/replay."""
from __future__ import annotations
import hashlib,json
from datetime import datetime,timezone
from pathlib import Path
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    stage_path=OUT/"five-r2-stage.json"
    stage=json.loads(stage_path.read_text(encoding="utf-8"))
    if stage["preparation_guards"] or stage["root_decisions_required"]:
        raise RuntimeError("Cannot freeze unresolved corrected preparation")
    changed=[name for name,expected in stage["input_hashes"].items()
             if sha(ROOT/name)!=expected]
    if changed:
        raise RuntimeError("Selected inputs changed before freezing; refresh preparation: "+repr(changed))
    stamp=datetime.fromisoformat(stage["utc"]).strftime("%Y%m%dT%H%M%SZ")
    dest=OUT/("five-r2-frozen-"+stamp)
    dest.mkdir(exist_ok=True)
    names=["five-r2-stage.json","five-r2-root-decisions.json",
           "five-r2-transformed-rows.json","five-r2-scope-bindings.json",
           "five-r2-transformations.json","five-r2-family-members.json",
           "five-r2-decisions-required.json","five-r2-dq-binding-proposal.json",
           "batch7-proposal-numeric-migrations.json",
           "prepare_five_stage_r2.py","prepare_numeric_watch.py"]
    names += [name for phase in stage["application_order"].values() for name in phase]
    artifacts=[]
    for name in names:
        original=OUT/name;target=dest/name;data=original.read_bytes()
        if target.exists() and target.read_bytes()!=data:
            raise RuntimeError("Immutable R2 proposal conflict: "+name)
        if not target.exists():target.write_bytes(data)
        artifacts.append({"name":name,"sha256":sha(target),"bytes":len(data)})
    raw_inputs=[]
    for name,expected in stage["input_hashes"].items():
        if not name.startswith(("handbook/registry/symbols-intake-","handbook/bib/intake-")):
            continue
        original=ROOT/name;data=original.read_bytes()
        evidence_name="raw-"+original.name+"-"+expected+original.suffix
        target=dest/evidence_name
        if target.exists() and target.read_bytes()!=data:
            raise RuntimeError("Immutable raw intake conflict")
        if not target.exists():target.write_bytes(data)
        raw_inputs.append({"original":name,"evidence":evidence_name,"sha256":expected,"bytes":len(data)})
    receipt={
        "freeze_utc":datetime.now(timezone.utc).isoformat(),"proposal_utc":stage["utc"],
        "directory":dest.name,"stage_sha256":sha(dest/"five-r2-stage.json"),
        "baseline_sha256":stage["baseline_sha256"],"selected_groups":stage["selected_groups"],
        "retained_other_groups":stage["retained_other_groups"],
        "canonical_before":{"symbols":stage["canonical_symbols_before"],"bibliography":stage["canonical_bib_before"]},
        "raw_selected_symbol_records":stage["raw_selected_symbol_rows"],
        "proposed_delta":{"symbols":stage["proposed_symbol_rows_count"],
                          "bibliography":len(stage["append_bib_records"]),
                          "scopes":len(stage["append_only_scopes"])},
        "source_scopes":stage["new_symbol_source_scopes"],
        "numeric_meaning_scopes":len(stage["append_only_scopes"])-stage["new_symbol_source_scopes"],
        "numeric_row_replacements":stage["numeric_migration_rows"],
        "actual_chapter_headings":stage["numeric_identity_proposals"]["actual_chapter_headings"],
        "proposed_counts_if_applied":{"symbols":stage["canonical_symbols_before"]+stage["proposed_symbol_rows_count"],
                                     "bibliography":stage["canonical_bib_before"]+len(stage["append_bib_records"])},
        "application_order":stage["application_order"],"input_hashes":stage["input_hashes"],
        "artifacts":artifacts,"raw_intake_evidence":raw_inputs,
        "scope":stage["scope"],"root_decisions_required":stage["root_decisions_required"],
        "standing":"Corrected actual-five PROPOSAL bytes only. No applying, replay, independent review/check/build/render. Old eleven-patch frozen packet and interrupted R2 draft remain historical/unapplied; old raw bytes, baseline and B6 pending2 preserved. dQ is declaration-local as root adopted, with all later selected body/annex/sheet usage exposed separately."
    }
    receipt_path=dest/"frozen-receipt.json"
    if receipt_path.exists():
        existing=json.loads(receipt_path.read_text(encoding="utf-8"))
    else:
        receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        existing=receipt
    print(json.dumps({"directory":dest.name,"proposal_utc":existing["proposal_utc"],
        "freeze_utc":existing["freeze_utc"],"stage_sha256":existing["stage_sha256"],
        "receipt_sha256":sha(receipt_path),"patches":sum(map(len,existing["application_order"].values())),
        "proposed_delta":existing["proposed_delta"],"numeric_replacements":existing["numeric_row_replacements"],
        "actual_chapters":existing["actual_chapter_headings"],
        "proposed_counts_if_applied":existing["proposed_counts_if_applied"]}))

if __name__=="__main__":main()

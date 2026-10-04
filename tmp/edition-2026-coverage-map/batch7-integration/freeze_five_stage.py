"""Freeze successful five-stage preparation bytes; no replay/check/application."""
from __future__ import annotations
import hashlib,json
from datetime import datetime,timezone
from pathlib import Path
OUT=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    stage_path=OUT/"five-stage.json"
    stage=json.loads(stage_path.read_text(encoding="utf-8"))
    if stage["preparation_guards"] or stage["root_decisions_required"]:
        raise RuntimeError("Cannot freeze a stage with unresolved preparation data")
    timestamp=datetime.fromisoformat(stage["utc"]).strftime("%Y%m%dT%H%M%SZ")
    destination=OUT/("five-frozen-"+timestamp)
    destination.mkdir(exist_ok=True)
    names=["five-stage.json","five-root-decisions.json","five-transformed-rows.json",
           "five-scope-bindings.json","five-transformations.json",
           "five-decisions-required.json"]
    names += [n for group in stage["application_order"].values() for n in group]
    records=[]
    for name in names:
        original=OUT/name;target=destination/name;data=original.read_bytes()
        if target.exists() and target.read_bytes()!=data:
            raise RuntimeError("Immutable five-stage artifact conflict: "+name)
        if not target.exists():target.write_bytes(data)
        records.append({"name":name,"sha256":sha(target),"bytes":len(data)})
    receipt={
        "freeze_utc":datetime.now(timezone.utc).isoformat(),
        "proposal_utc":stage["utc"],"directory":destination.name,
        "stage_sha256":sha(destination/"five-stage.json"),
        "baseline_sha256":stage["baseline_sha256"],
        "selected_groups":stage["selected_groups"],
        "retained_other_groups":stage["retained_offroute_groups"],
        "canonical_before":{"symbols":stage["canonical_symbols_before"],
                            "bibliography":stage["canonical_bib_before"]},
        "proposed_delta":{"symbols":stage["raw_selected_symbol_rows"],
                          "bibliography":len(stage["append_bib_records"]),
                          "named_scopes":len(stage["append_only_scopes"])},
        "proposed_counts_if_applied":{"symbols":stage["canonical_symbols_before"]+stage["raw_selected_symbol_rows"],
                                     "bibliography":stage["canonical_bib_before"]+len(stage["append_bib_records"])},
        "application_order":stage["application_order"],
        "input_hashes":stage["input_hashes"],"artifacts":records,
        "root_decisions_required":stage["root_decisions_required"],
        "scope":stage["scope"],
        "standing":"Frozen PROPOSAL bytes only. Root reads/applies in listed order against matching canonical/source inputs. No replay/check/review/build/render or target mutation performed. Original intakes, pre-B7 baseline, B6 pending2 preserved."
    }
    receipt_path=destination/"frozen-receipt.json"
    if not receipt_path.exists():
        receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    existing=json.loads(receipt_path.read_text(encoding="utf-8"))
    print(json.dumps({"directory":destination.name,"stage_sha256":existing["stage_sha256"],
        "receipt_sha256":sha(receipt_path),"proposal_utc":existing["proposal_utc"],
        "freeze_utc":existing["freeze_utc"],"patches":sum(map(len,existing["application_order"].values())),
        "proposed_delta":existing["proposed_delta"],"proposed_counts_if_applied":existing["proposed_counts_if_applied"]}))

if __name__=="__main__":main()

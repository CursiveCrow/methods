#!/usr/bin/env python3
"""CLI-level tests for exact inherited-interval restoration records."""

from __future__ import annotations

import copy
import csv
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools import check_inherited_restoration as validator


REPO_ROOT = Path(__file__).resolve().parents[1]
CHECKER = REPO_ROOT / "tools" / "check_inherited_restoration.py"


class InheritedRestorationCliTests(unittest.TestCase):
    def stage_repository(self, destination: Path) -> Path:
        files = (
            "source/formal-logic-reference.tex",
            "spec/inherited-corpus-manifest.json",
            "spec/inherited-source-map.csv",
            "spec/source-unit-inventory.csv",
            "spec/provenance/SRC-09099-09111.json",
            "handbook/restoration/inherited-09099-09111.tex",
            "handbook/restoration/inherited-00039-00047.tex",
            "handbook/parts/p05/diagonalization.tex",
        )
        for relative in files:
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO_ROOT / relative, target)
        return destination

    def stage_reader_layout_repository(
        self, destination: Path, provenance_id: str = "SRC-01649-01660"
    ) -> Path:
        record = json.loads(
            (REPO_ROOT / f"spec/provenance/{provenance_id}.json").read_text(
                encoding="utf-8"
            )
        )
        files = (
            "source/formal-logic-reference.tex",
            "spec/inherited-corpus-manifest.json",
            "spec/inherited-source-map.csv",
            "spec/source-unit-inventory.csv",
            f"spec/provenance/{provenance_id}.json",
            record["restoration_artifact"]["path"],
            record["reader_layout"]["wrapper_path"],
            record["reader_layout"]["public_part_file"],
        )
        for relative in files:
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO_ROOT / relative, target)
        return destination

    def stage_reader_appendix_layout_repository(
        self, destination: Path, provenance_id: str = "SRC-15093-15206"
    ) -> Path:
        record = json.loads(
            (REPO_ROOT / f"spec/provenance/{provenance_id}.json").read_text(
                encoding="utf-8"
            )
        )
        files = (
            "source/formal-logic-reference.tex",
            "spec/inherited-corpus-manifest.json",
            "spec/inherited-source-map.csv",
            "spec/source-unit-inventory.csv",
            f"spec/provenance/{provenance_id}.json",
            record["restoration_artifact"]["path"],
            record["reader_appendix_layout"]["wrapper_path"],
            record["reader_appendix_layout"]["public_part_file"],
        )
        for relative in files:
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO_ROOT / relative, target)
        return destination

    @staticmethod
    def write_record(path: Path, record: dict[str, object]) -> None:
        path.write_text(
            json.dumps(record, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )

    def run_checker(
        self,
        repo_root: Path = REPO_ROOT,
        record: str | list[str] | None = "spec/provenance/SRC-09099-09111.json",
    ) -> subprocess.CompletedProcess[str]:
        command = [
            sys.executable,
            str(CHECKER),
            "--repo-root",
            str(repo_root),
        ]
        records = [record] if isinstance(record, str) else record or []
        for item in records:
            command.extend(["--record", item])
        return subprocess.run(
            command,
            cwd=repo_root,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_pristine_repository_interval_passes(self) -> None:
        completed = self.run_checker()

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("RESTORATION CHECK OK: SRC-09099-09111", completed.stdout)

    def test_default_discovery_ignores_other_provenance_json(self) -> None:
        completed = self.run_checker(record=None)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 267", completed.stdout)

    def test_requested_repository_records_pass_together(self) -> None:
        records = [
            "spec/provenance/PRE-00039-00047.json",
            "spec/provenance/SRC-00171-00197.json",
            "spec/provenance/SRC-00198-00234.json",
            "spec/provenance/SRC-00235-00293.json",
            "spec/provenance/SRC-00294-00320.json",
            "spec/provenance/SRC-00321-00362.json",
            "spec/provenance/SRC-09099-09111.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 7", completed.stdout)

    def test_first_chapter_pilot_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-00406-00443.json",
            "spec/provenance/SRC-00444-00506.json",
            "spec/provenance/SRC-00507-00532.json",
            "spec/provenance/SRC-00533-00602.json",
            "spec/provenance/SRC-00603-00647.json",
            "spec/provenance/SRC-00648-00744.json",
            "spec/provenance/SRC-00745-00772.json",
            "spec/provenance/SRC-00773-00789.json",
            "spec/provenance/SRC-00790-00797.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 9", completed.stdout)

    def test_levels_chapter_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-00798-00852.json",
            "spec/provenance/SRC-00853-00906.json",
            "spec/provenance/SRC-00907-00984.json",
            "spec/provenance/SRC-00985-01023.json",
            "spec/provenance/SRC-01024-01084.json",
            "spec/provenance/SRC-01085-01100.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 6", completed.stdout)

    def test_strings_chapter_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-01101-01147.json",
            "spec/provenance/SRC-01148-01163.json",
            "spec/provenance/SRC-01164-01223.json",
            "spec/provenance/SRC-01224-01263.json",
            "spec/provenance/SRC-01264-01308.json",
            "spec/provenance/SRC-01309-01319.json",
            "spec/provenance/SRC-01320-01342.json",
            "spec/provenance/SRC-01343-01397.json",
            "spec/provenance/SRC-01398-01410.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 9", completed.stdout)

    def test_writing_chapter_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-01411-01504.json",
            "spec/provenance/SRC-01505-01553.json",
            "spec/provenance/SRC-01554-01579.json",
            "spec/provenance/SRC-01580-01591.json",
            "spec/provenance/SRC-01592-01631.json",
            "spec/provenance/SRC-01632-01648.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 6", completed.stdout)

    def test_classical_propositional_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-01649-01660.json",
            "spec/provenance/SRC-01661-01816.json",
            "spec/provenance/SRC-01817-01898.json",
            "spec/provenance/SRC-01899-01945.json",
            "spec/provenance/SRC-01946-02186.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 5", completed.stdout)

    def test_natural_deduction_and_sequents_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-02187-02192.json",
            "spec/provenance/SRC-02193-02340.json",
            "spec/provenance/SRC-02341-02450.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 3", completed.stdout)

    def test_propositional_metatheory_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-02451-02544.json",
            "spec/provenance/SRC-02545-02664.json",
            "spec/provenance/SRC-02665-02809.json",
            "spec/provenance/SRC-02810-02914.json",
            "spec/provenance/SRC-02915-02932.json",
            "spec/provenance/SRC-02933-03021.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 6", completed.stdout)

    def test_first_order_syntax_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-03022-03037.json",
            "spec/provenance/SRC-03038-03104.json",
            "spec/provenance/SRC-03105-03165.json",
            "spec/provenance/SRC-03166-03239.json",
            "spec/provenance/SRC-03240-03428.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 5", completed.stdout)

    def test_first_order_semantics_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-03429-03518.json",
            "spec/provenance/SRC-03519-03680.json",
            "spec/provenance/SRC-03681-03728.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 3", completed.stdout)

    def test_first_order_theories_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-03729-03907.json",
            "spec/provenance/SRC-03908-03926.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 2", completed.stdout)

    def test_first_order_deduction_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-03927-04061.json",
            "spec/provenance/SRC-04062-04108.json",
            "spec/provenance/SRC-04109-04213.json",
            "spec/provenance/SRC-04214-04234.json",
            "spec/provenance/SRC-04235-04305.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 5", completed.stdout)

    def test_first_order_completeness_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-04306-04575.json",
            "spec/provenance/SRC-04576-04712.json",
            "spec/provenance/SRC-04713-04920.json",
            "spec/provenance/SRC-04921-04967.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 4", completed.stdout)

    def test_first_order_cardinality_normal_forms_and_resolution_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-04968-05042.json",
            "spec/provenance/SRC-05043-05131.json",
            "spec/provenance/SRC-05132-05567.json",
            "spec/provenance/SRC-05568-05923.json",
            "spec/provenance/SRC-05924-05959.json",
            "spec/provenance/SRC-05960-06048.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 6", completed.stdout)

    def test_model_theory_opening_record_passes_with_direct_public_part_layout(self) -> None:
        completed = self.run_checker(
            record="spec/provenance/SRC-06049-06069.json"
        )

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("RESTORATION CHECK OK: SRC-06049-06069", completed.stdout)

    def test_maps_substructures_and_elementarity_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-06049-06069.json",
            "spec/provenance/SRC-06070-06137.json",
            "spec/provenance/SRC-06138-06242.json",
            "spec/provenance/SRC-06243-06331.json",
            "spec/provenance/SRC-06332-06421.json",
            "spec/provenance/SRC-06422-06431.json",
            "spec/provenance/SRC-06432-06493.json",
            "spec/provenance/SRC-06494-06509.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 8", completed.stdout)

    def test_types_saturation_and_ultraproducts_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-06510-06629.json",
            "spec/provenance/SRC-06630-06639.json",
            "spec/provenance/SRC-06640-06693.json",
            "spec/provenance/SRC-06694-06782.json",
            "spec/provenance/SRC-06783-06791.json",
            "spec/provenance/SRC-06792-06845.json",
            "spec/provenance/SRC-06846-06854.json",
            "spec/provenance/SRC-06855-06941.json",
            "spec/provenance/SRC-06942-07134.json",
            "spec/provenance/SRC-07135-07149.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 10", completed.stdout)

    def test_quantifier_elimination_and_categoricity_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-07150-07294.json",
            "spec/provenance/SRC-07295-07468.json",
            "spec/provenance/SRC-07469-07493.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 3", completed.stdout)

    def test_machines_and_effective_procedures_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-07494-07505.json",
            "spec/provenance/SRC-07506-07677.json",
            "spec/provenance/SRC-07678-07752.json",
            "spec/provenance/SRC-07753-07843.json",
            "spec/provenance/SRC-07844-07850.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 5", completed.stdout)

    def test_universal_computation_reductions_and_fixed_points_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-07851-08048.json",
            "spec/provenance/SRC-08049-08080.json",
            "spec/provenance/SRC-08081-08143.json",
            "spec/provenance/SRC-08144-08186.json",
            "spec/provenance/SRC-08187-08238.json",
            "spec/provenance/SRC-08239-08247.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 6", completed.stdout)

    def test_decision_problems_and_arithmetical_hierarchy_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-08248-08305.json",
            "spec/provenance/SRC-08306-08438.json",
            "spec/provenance/SRC-08439-08709.json",
            "spec/provenance/SRC-08710-08876.json",
            "spec/provenance/SRC-08877-08897.json",
            "spec/provenance/SRC-08898-09079.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 6", completed.stdout)

    def test_complete_part5_source_run_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-09080-09098.json",
            "spec/provenance/SRC-09099-09111.json",
            "spec/provenance/SRC-09112-09149.json",
            "spec/provenance/SRC-09150-09174.json",
            "spec/provenance/SRC-09175-09187.json",
            "spec/provenance/SRC-09188-09261.json",
            "spec/provenance/SRC-09262-09327.json",
            "spec/provenance/SRC-09328-09438.json",
            "spec/provenance/SRC-09439-09497.json",
            "spec/provenance/SRC-09498-09538.json",
            "spec/provenance/SRC-09539-09619.json",
            "spec/provenance/SRC-09620-09728.json",
            "spec/provenance/SRC-09729-09749.json",
            "spec/provenance/SRC-09750-09816.json",
            "spec/provenance/SRC-09817-09876.json",
            "spec/provenance/SRC-09877-09924.json",
            "spec/provenance/SRC-09925-09992.json",
            "spec/provenance/SRC-09993-10027.json",
            "spec/provenance/SRC-10028-10059.json",
        ]

        completed = self.run_checker(record=records)

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 19", completed.stdout)

    def test_zf_zfc_opening_chapter_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-10060-10088.json",
            "spec/provenance/SRC-10089-10271.json",
            "spec/provenance/SRC-10272-10352.json",
        ]
        completed = self.run_checker(record=records)
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 3", completed.stdout)

    def test_cumulative_hierarchy_chapter_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-10353-10451.json",
            "spec/provenance/SRC-10452-10520.json",
            "spec/provenance/SRC-10521-10558.json",
            "spec/provenance/SRC-10559-10674.json",
        ]
        completed = self.run_checker(record=records)
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 4", completed.stdout)

    def test_constructibility_forcing_chapter_records_pass_together(self) -> None:
        records = [
            f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
            for start, end in (
                (10675, 10769),
                (10770, 10825),
                (10826, 10881),
                (10882, 10899),
                (10900, 10988),
                (10989, 11011),
                (11012, 11052),
                (11053, 11103),
                (11104, 11126),
                (11127, 11199),
                (11200, 11239),
                (11240, 11279),
                (11280, 11293),
                (11294, 11314),
                (11315, 11337),
                (11338, 11353),
            )
        ]
        completed = self.run_checker(record=records)
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 16", completed.stdout)

    def test_proof_theory_calculi_and_cut_elimination_records_pass_together(self) -> None:
        records = [
            f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
            for start, end in (
                (11354, 11413),
                (11414, 11505),
                (11506, 11519),
                (11520, 11598),
                (11599, 11627),
                (11628, 11644),
                (11645, 11695),
                (11696, 11710),
                (11711, 11740),
                (11741, 11767),
                (11768, 11823),
                (11824, 11881),
                (11882, 11913),
                (11914, 11960),
            )
        ]
        completed = self.run_checker(record=records)
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 14", completed.stdout)

    def test_normalization_and_ordinal_analysis_records_pass_together(self) -> None:
        records = [
            f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
            for start, end in (
                (11961, 12029),
                (12030, 12100),
                (12101, 12132),
                (12133, 12217),
                (12218, 12248),
            )
        ]
        completed = self.run_checker(record=records)
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 5", completed.stdout)

    def test_second_and_higher_order_logic_records_pass_together(self) -> None:
        records = [
            f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
            for start, end in (
                (12249, 12261), (12262, 12289), (12290, 12355),
                (12356, 12414), (12415, 12536), (12537, 12673),
                (12674, 12720), (12721, 12783), (12784, 12923),
                (12924, 12950), (12951, 12969),
            )
        ]
        completed = self.run_checker(record=records)
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 11", completed.stdout)

    def test_intuitionistic_logic_records_pass_together(self) -> None:
        records = [
            f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
            for start, end in (
                (12970, 12988), (12989, 13045), (13046, 13057),
                (13058, 13099), (13100, 13127), (13128, 13140),
                (13141, 13157), (13158, 13179), (13180, 13200),
            )
        ]
        completed = self.run_checker(record=records)
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 9", completed.stdout)

    def test_modal_temporal_epistemic_records_pass_together(self) -> None:
        records = [
            f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
            for start, end in (
                (13201, 13213), (13214, 13254), (13255, 13284),
                (13285, 13316), (13317, 13339), (13340, 13409),
                (13410, 13439), (13440, 13471), (13472, 13478),
                (13479, 13518), (13519, 13551), (13552, 13564),
                (13565, 13583),
            )
        ]
        completed = self.run_checker(record=records)
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 13", completed.stdout)

    def test_many_valued_relevance_linear_records_pass_together(self) -> None:
        records = [
            f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
            for start, end in (
                (13584, 13613), (13614, 13640), (13641, 13699),
                (13700, 13730), (13731, 13774), (13775, 13788),
                (13789, 13806), (13807, 13861), (13862, 13896),
                (13897, 13918), (13919, 13938), (13939, 13971),
                (13972, 14000), (14001, 14015), (14016, 14034),
                (14035, 14051), (14052, 14068), (14069, 14094),
            )
        ]
        completed = self.run_checker(record=records)
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 18", completed.stdout)

    def test_formal_practice_records_pass_together(self) -> None:
        records = [
            f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
            for start, end in (
                (14095, 14146), (14147, 14169), (14170, 14202),
                (14203, 14230), (14231, 14270),
            )
        ]
        completed = self.run_checker(record=records)
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 5", completed.stdout)

    def test_automated_reasoning_and_continuity_records_pass_together(self) -> None:
        records = [
            "spec/provenance/SRC-14271-14350.json",
            "spec/provenance/SRC-14351-14400.json",
            "spec/provenance/SRC-14401-14434.json",
            "spec/provenance/SRC-14435-14479.json",
            "spec/provenance/SRC-14480-14495.json",
            "spec/provenance/SRC-14496-14521.json",
            "spec/provenance/SRC-14522-14560.json",
            "spec/provenance/SEP-14561-14561.json",
            "spec/provenance/SRC-14562-14589.json",
            "spec/provenance/SEP-14590-14590.json",
        ]
        completed = self.run_checker(record=records)
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 10", completed.stdout)

    def test_blank_continuity_has_exactly_no_content_classification(self) -> None:
        path = REPO_ROOT / "spec/provenance/SEP-14561-14561.json"
        record = validator.load_json(path)
        self.assertEqual(record["audit_evidence"]["classifications"], [])
        validator.validate_record(record, path, REPO_ROOT)

        mutated = copy.deepcopy(record)
        mutated["audit_evidence"]["classifications"] = ["altered"]
        with self.assertRaisesRegex(
            validator.CheckFailure,
            "audit classifications do not exactly match",
        ):
            validator.validate_record(mutated, path, REPO_ROOT)

    def test_mechanized_proof_checking_records_pass_together(self) -> None:
        records = [
            f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
            for start, end in (
                (14591, 14628),
                (14629, 14660),
                (14661, 14690),
                (14691, 14728),
            )
        ]
        completed = self.run_checker(record=records)
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 4", completed.stdout)

    def test_writing_and_typesetting_records_pass_together(self) -> None:
        records = [
            f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
            for start, end in (
                (14729, 14778),
                (14779, 14814),
                (14815, 14850),
                (14851, 14870),
                (14871, 14931),
                (14932, 14945),
                (14946, 14975),
                (14976, 14990),
                (14991, 15029),
            )
        ]
        completed = self.run_checker(record=records)
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 9", completed.stdout)

    def test_research_workflow_records_pass_together(self) -> None:
        records = [
            f"spec/provenance/{provenance_id}.json"
            for provenance_id in (
                "SRC-15030-15050",
                "SRC-15051-15068",
                "SRC-15069-15077",
                "SRC-15078-15091",
                "SEP-15092-15092",
            )
        ]
        completed = self.run_checker(record=records)
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("verified restoration records: 5", completed.stdout)

    def test_registered_notation_appendix_record_passes(self) -> None:
        completed = self.run_checker(
            record="spec/provenance/SRC-15093-15206.json"
        )
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("RESTORATION CHECK OK: SRC-15093-15206", completed.stdout)

    def test_binding_precedence_appendix_record_passes(self) -> None:
        completed = self.run_checker(
            record="spec/provenance/SRC-15207-15239.json"
        )
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("RESTORATION CHECK OK: SRC-15207-15239", completed.stdout)

    def test_binding_precedence_is_appendix_b_without_second_transition(self) -> None:
        provenance_id = "SRC-15207-15239"
        record_relative = f"spec/provenance/{provenance_id}.json"
        with tempfile.TemporaryDirectory(prefix="reader-appendix-b-") as raw:
            root = self.stage_reader_appendix_layout_repository(
                Path(raw), provenance_id
            )
            path = root / record_relative
            record = validator.load_json(path)
            validator.validate_reader_appendix_layout(record, root)
            layout = record["reader_appendix_layout"]
            self.assertEqual(layout["source_appendix_line"], 0)
            self.assertEqual(layout["source_appendix_command"], "")
            self.assertEqual(layout["appendix_ordinal"], "B")

            layout["appendix_ordinal"] = "A"
            self.write_record(path, record)
            completed = self.run_checker(root, record_relative)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn(
            "does not match the exact governed reader appendix layout",
            completed.stderr,
        )

        with tempfile.TemporaryDirectory(prefix="reader-appendix-b-token-") as raw:
            root = self.stage_reader_appendix_layout_repository(
                Path(raw), provenance_id
            )
            path = root / record_relative
            record = validator.load_json(path)
            artifact = root / record["restoration_artifact"]["path"]
            artifact.write_text(
                "\\appendix\n" + artifact.read_text(encoding="utf-8"),
                encoding="utf-8",
                newline="\n",
            )
            with self.assertRaisesRegex(
                validator.CheckFailure, "continuation must use line 0"
            ):
                validator.validate_reader_appendix_layout(record, root)

    def test_rule_sheets_appendix_record_passes(self) -> None:
        completed = self.run_checker(
            record="spec/provenance/SRC-15240-15488.json"
        )
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("RESTORATION CHECK OK: SRC-15240-15488", completed.stdout)

    def test_rule_sheets_is_appendix_c_without_second_transition(self) -> None:
        provenance_id = "SRC-15240-15488"
        record_relative = f"spec/provenance/{provenance_id}.json"
        with tempfile.TemporaryDirectory(prefix="reader-appendix-c-") as raw:
            root = self.stage_reader_appendix_layout_repository(
                Path(raw), provenance_id
            )
            path = root / record_relative
            record = validator.load_json(path)
            validator.validate_reader_appendix_layout(record, root)
            layout = record["reader_appendix_layout"]
            self.assertEqual(layout["source_appendix_line"], 0)
            self.assertEqual(layout["source_appendix_command"], "")
            self.assertEqual(layout["appendix_ordinal"], "C")
            self.assertEqual(
                layout["source_labels"],
                [
                    "ch:rule-sheets",
                    "app:rules",
                    "sec:rule-sheets-01",
                    "sec:rule-sheets-02",
                    "sec:rule-sheets-03",
                ],
            )

        with tempfile.TemporaryDirectory(prefix="reader-appendix-c-token-") as raw:
            root = self.stage_reader_appendix_layout_repository(
                Path(raw), provenance_id
            )
            path = root / record_relative
            record = validator.load_json(path)
            artifact = root / record["restoration_artifact"]["path"]
            artifact.write_text(
                r"\appendix" + "\n" + artifact.read_text(encoding="utf-8"),
                encoding="utf-8",
                newline="\n",
            )
            with self.assertRaisesRegex(
                validator.CheckFailure, "continuation must use line 0"
            ):
                validator.validate_reader_appendix_layout(record, root)

    def test_qualifying_problems_appendix_record_passes(self) -> None:
        completed = self.run_checker(
            record="spec/provenance/SRC-15489-15619.json"
        )
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("RESTORATION CHECK OK: SRC-15489-15619", completed.stdout)

    def test_qualifying_problems_is_appendix_d_without_second_transition(self) -> None:
        provenance_id = "SRC-15489-15619"
        record_relative = f"spec/provenance/{provenance_id}.json"
        with tempfile.TemporaryDirectory(prefix="reader-appendix-d-") as raw:
            root = self.stage_reader_appendix_layout_repository(
                Path(raw), provenance_id
            )
            path = root / record_relative
            record = validator.load_json(path)
            validator.validate_reader_appendix_layout(record, root)
            layout = record["reader_appendix_layout"]
            self.assertEqual(layout["source_appendix_line"], 0)
            self.assertEqual(layout["source_appendix_command"], "")
            self.assertEqual(layout["appendix_ordinal"], "D")
            self.assertEqual(len(layout["source_labels"]), 12)
            self.assertEqual(layout["source_labels"][0:2], [
                "ch:qualifying-problems",
                "app:qualifying",
            ])

        with tempfile.TemporaryDirectory(prefix="reader-appendix-d-token-") as raw:
            root = self.stage_reader_appendix_layout_repository(
                Path(raw), provenance_id
            )
            path = root / record_relative
            record = validator.load_json(path)
            artifact = root / record["restoration_artifact"]["path"]
            artifact.write_text(
                r"\appendix" + "\n" + artifact.read_text(encoding="utf-8"),
                encoding="utf-8",
                newline="\n",
            )
            with self.assertRaisesRegex(
                validator.CheckFailure, "continuation must use line 0"
            ):
                validator.validate_reader_appendix_layout(record, root)

    def test_additional_qualifying_problems_record_passes(self) -> None:
        completed = self.run_checker(
            record="spec/provenance/SRC-15620-15637.json"
        )
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("RESTORATION CHECK OK: SRC-15620-15637", completed.stdout)

    def test_additional_problems_is_chapterless_appendix_d6_continuation(self) -> None:
        provenance_id = "SRC-15620-15637"
        record_relative = f"spec/provenance/{provenance_id}.json"
        with tempfile.TemporaryDirectory(prefix="reader-appendix-d6-") as raw:
            root = self.stage_reader_appendix_layout_repository(
                Path(raw), provenance_id
            )
            path = root / record_relative
            record = validator.load_json(path)
            validator.validate_reader_appendix_layout(record, root)
            layout = record["reader_appendix_layout"]
            self.assertEqual(layout["source_chapter_line"], 0)
            self.assertEqual(layout["source_chapter_command"], "")
            self.assertEqual(layout["appendix_ordinal"], "D")
            self.assertEqual(layout["reader_heading_level"], "appendix section continuation")
            self.assertEqual(layout["toc_level"], "section")
            self.assertEqual(layout["bookmark_level"], 1)

        with tempfile.TemporaryDirectory(prefix="reader-appendix-d6-chapter-") as raw:
            root = self.stage_reader_appendix_layout_repository(
                Path(raw), provenance_id
            )
            path = root / record_relative
            record = validator.load_json(path)
            artifact = root / record["restoration_artifact"]["path"]
            artifact.write_text(
                r"\chapter{Invented}" + "\n" + artifact.read_text(encoding="utf-8"),
                encoding="utf-8",
                newline="\n",
            )
            with self.assertRaisesRegex(
                validator.CheckFailure,
                "section continuation must use chapter line 0",
            ):
                validator.validate_reader_appendix_layout(record, root)

    def test_exercise_feedback_appendix_record_passes(self) -> None:
        completed = self.run_checker(
            record="spec/provenance/SRC-15638-16742.json"
        )
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("RESTORATION CHECK OK: SRC-15638-16742", completed.stdout)

    def test_exercise_feedback_is_appendix_e_without_second_transition(self) -> None:
        provenance_id = "SRC-15638-16742"
        record_relative = f"spec/provenance/{provenance_id}.json"
        with tempfile.TemporaryDirectory(prefix="reader-appendix-e-") as raw:
            root = self.stage_reader_appendix_layout_repository(
                Path(raw), provenance_id
            )
            path = root / record_relative
            record = validator.load_json(path)
            validator.validate_reader_appendix_layout(record, root)
            layout = record["reader_appendix_layout"]
            self.assertEqual(layout["source_appendix_line"], 0)
            self.assertEqual(layout["source_appendix_command"], "")
            self.assertEqual(layout["appendix_ordinal"], "E")
            self.assertEqual(
                layout["source_labels"],
                ["ch:exercise-feedback", "app:exercise-feedback"],
            )

        with tempfile.TemporaryDirectory(prefix="reader-appendix-e-token-") as raw:
            root = self.stage_reader_appendix_layout_repository(
                Path(raw), provenance_id
            )
            path = root / record_relative
            record = validator.load_json(path)
            artifact = root / record["restoration_artifact"]["path"]
            artifact.write_text(
                r"\appendix" + "\n" + artifact.read_text(encoding="utf-8"),
                encoding="utf-8",
                newline="\n",
            )
            with self.assertRaisesRegex(
                validator.CheckFailure, "continuation must use line 0"
            ):
                validator.validate_reader_appendix_layout(record, root)

    def test_reader_appendix_layout_is_schema_v3_and_provenance_specific(self) -> None:
        provenance_id = "SRC-15093-15206"
        record_relative = f"spec/provenance/{provenance_id}.json"
        with tempfile.TemporaryDirectory(prefix="reader-appendix-layout-") as raw:
            root = self.stage_reader_appendix_layout_repository(Path(raw))
            path = root / record_relative
            record = validator.load_json(path)
            self.assertEqual(record["schema_version"], 3)
            validator.validate_reader_appendix_layout(record, root)

            record["provenance_id"] = "SRC-15094-15206"
            moved = path.with_name("SRC-15094-15206.json")
            self.write_record(moved, record)
            path.unlink()
            completed = self.run_checker(
                root, "spec/provenance/SRC-15094-15206.json"
            )
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("schema_version 3 is reserved", completed.stderr)

    def test_reader_appendix_layout_fields_and_source_tokens_fail_closed(self) -> None:
        field_cases = (
            (
                "missing",
                lambda layout: layout.pop("appendix_ordinal"),
                "missing=['appendix_ordinal']",
            ),
            (
                "extra",
                lambda layout: layout.__setitem__("ignore", True),
                "extra=['ignore']",
            ),
            (
                "mutated",
                lambda layout: layout.__setitem__("appendix_ordinal", "B"),
                "does not match the exact governed reader appendix layout",
            ),
        )
        for name, mutate, expected in field_cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory(
                prefix=f"reader-appendix-field-{name}-"
            ) as raw:
                root = self.stage_reader_appendix_layout_repository(Path(raw))
                path = root / "spec/provenance/SRC-15093-15206.json"
                record = validator.load_json(path)
                mutate(record["reader_appendix_layout"])
                self.write_record(path, record)
                completed = self.run_checker(
                    root, "spec/provenance/SRC-15093-15206.json"
                )
                self.assertNotEqual(completed.returncode, 0)
                self.assertIn(expected, completed.stderr)

        source_cases = (
            ("missing appendix", lambda text: text.replace("\\appendix", ""), "appendix command"),
            ("duplicate appendix", lambda text: text.replace("\\appendix", "\\appendix\n\\appendix"), "appendix command"),
            ("wrong chapter", lambda text: text.replace("\\chapter{Registered Notation}", "\\chapter{Wrong}"), "chapter command"),
            ("missing label", lambda text: text.replace("\\label{app:notation}", ""), "source labels"),
        )
        for name, mutate, expected in source_cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory(
                prefix=f"reader-appendix-source-{name}-"
            ) as raw:
                root = self.stage_reader_appendix_layout_repository(Path(raw))
                path = root / "spec/provenance/SRC-15093-15206.json"
                record = validator.load_json(path)
                artifact = root / record["restoration_artifact"]["path"]
                artifact.write_text(
                    mutate(artifact.read_text(encoding="utf-8")),
                    encoding="utf-8",
                    newline="\n",
                )
                with self.assertRaisesRegex(validator.CheckFailure, expected):
                    validator.validate_reader_appendix_layout(record, root)

    def test_reader_appendix_layout_rejects_public_binding_and_order_drift(self) -> None:
        cases = (
            (
                "binding",
                lambda text: text.replace(
                    r"\part{Automation, Mechanization, and Formal Practice}\label{part:p12}",
                    r"\part{Automation, Mechanization, and Formal Practice}",
                ),
                "exact public Part XII binding",
            ),
            (
                "after aggregator",
                lambda text: text.replace(
                    r"\input{restoration/scope-SRC-15093-15206}" + "\n"
                    + r"\input{restoration/scope-SRC-15207-15239}" + "\n"
                    + r"\input{restoration/scope-SRC-15240-15488}" + "\n"
                    + r"\input{restoration/scope-SRC-15489-15619}" + "\n"
                    + r"\input{restoration/scope-SRC-15620-15637}" + "\n"
                    + r"\input{restoration/scope-SRC-15638-16742}" + "\n"
                    + r"\input{parts/p12/automation-and-mechanization}",
                    r"\input{restoration/scope-SRC-15207-15239}" + "\n"
                    + r"\input{restoration/scope-SRC-15240-15488}" + "\n"
                    + r"\input{restoration/scope-SRC-15489-15619}" + "\n"
                    + r"\input{restoration/scope-SRC-15620-15637}" + "\n"
                    + r"\input{restoration/scope-SRC-15638-16742}" + "\n"
                    + r"\input{parts/p12/automation-and-mechanization}" + "\n"
                    + r"\input{restoration/scope-SRC-15093-15206}",
                ),
                "must precede the editorial aggregator",
            ),
        )
        for name, mutate, expected in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory(
                prefix=f"reader-appendix-public-{name}-"
            ) as raw:
                root = self.stage_reader_appendix_layout_repository(Path(raw))
                path = root / "spec/provenance/SRC-15093-15206.json"
                record = validator.load_json(path)
                driver = root / record["reader_appendix_layout"]["public_part_file"]
                driver.write_text(
                    mutate(driver.read_text(encoding="utf-8")),
                    encoding="utf-8",
                    newline="\n",
                )
                with self.assertRaisesRegex(validator.CheckFailure, expected):
                    validator.validate_reader_appendix_layout(record, root)

    def test_part5_opening_record_uses_the_governed_public_title_layout(self) -> None:
        record = validator.load_json(
            REPO_ROOT / "spec/provenance/SRC-09080-09098.json"
        )
        validator.validate_reader_layout(record, REPO_ROOT)

    def test_part8_opening_record_uses_the_governed_public_title_layout(self) -> None:
        record = validator.load_json(
            REPO_ROOT / "spec/provenance/SRC-12970-12988.json"
        )
        validator.validate_reader_layout(record, REPO_ROOT)

    def test_part8_public_title_layout_is_independently_fail_closed(self) -> None:
        provenance_id = "SRC-12970-12988"
        record_relative = f"spec/provenance/{provenance_id}.json"
        with tempfile.TemporaryDirectory(prefix="part8-layout-field-") as raw:
            root = self.stage_reader_layout_repository(Path(raw), provenance_id)
            record_path = root / record_relative
            record = validator.load_json(record_path)
            record["reader_layout"]["public_part_title"] = "Nonclassical Logic"
            self.write_record(record_path, record)
            completed = self.run_checker(root, record_relative)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("does not match the exact governed reader layout", completed.stderr)

    def test_part5_public_title_layout_is_independently_fail_closed(self) -> None:
        provenance_id = "SRC-09080-09098"
        record_relative = f"spec/provenance/{provenance_id}.json"

        with tempfile.TemporaryDirectory(prefix="part5-layout-field-") as raw:
            root = self.stage_reader_layout_repository(Path(raw), provenance_id)
            record_path = root / record_relative
            record = validator.load_json(record_path)
            record["reader_layout"]["public_part_title"] = "Formal Arithmetic and Incompleteness"
            self.write_record(record_path, record)
            completed = self.run_checker(root, record_relative)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("does not match the exact governed reader layout", completed.stderr)

        for name, token, replacement, expected in (
            (
                "missing-part",
                r"\part{Formal Arithmetic and Incompleteness}",
                "",
                "part command",
            ),
            (
                "duplicate-part",
                r"\part{Formal Arithmetic and Incompleteness}",
                r"\part{Formal Arithmetic and Incompleteness}"
                + "\n"
                + r"\part{Formal Arithmetic and Incompleteness}",
                "part command",
            ),
            (
                "starred-part",
                r"\part{Formal Arithmetic and Incompleteness}",
                r"\part*{Formal Arithmetic and Incompleteness}",
                "part command",
            ),
            (
                "wrong-title",
                r"\part{Formal Arithmetic and Incompleteness}",
                r"\part{Wrong}",
                "part command",
            ),
            ("missing-label", r"\label{part:incompleteness}", "", "part label"),
            (
                "duplicate-label",
                r"\label{part:incompleteness}",
                r"\label{part:incompleteness}"
                + "\n"
                + r"\label{part:incompleteness}",
                "part label",
            ),
        ):
            with self.subTest(name=name), tempfile.TemporaryDirectory(
                prefix=f"part5-layout-{name}-"
            ) as raw:
                root = self.stage_reader_layout_repository(Path(raw), provenance_id)
                record = validator.load_json(root / record_relative)
                artifact = root / record["restoration_artifact"]["path"]
                artifact.write_text(
                    artifact.read_text(encoding="utf-8").replace(token, replacement),
                    encoding="utf-8",
                    newline="\n",
                )
                with self.assertRaisesRegex(validator.CheckFailure, expected):
                    validator.validate_reader_layout(record, root)

        for name, prefix, expected in (
            ("wrong-order", r"\input{parts/p05/other}" + "\n", "first direct input"),
            (
                "driver-part",
                r"\part{Arithmetic and Incompleteness}" + "\n",
                "exact artifact",
            ),
            ("driver-label", r"\label{part:p05}" + "\n", "driver label alias"),
        ):
            with self.subTest(name=name), tempfile.TemporaryDirectory(
                prefix=f"part5-driver-{name}-"
            ) as raw:
                root = self.stage_reader_layout_repository(Path(raw), provenance_id)
                record = validator.load_json(root / record_relative)
                driver = root / record["reader_layout"]["public_part_file"]
                driver.write_text(
                    prefix + driver.read_text(encoding="utf-8"),
                    encoding="utf-8",
                    newline="\n",
                )
                with self.assertRaisesRegex(validator.CheckFailure, expected):
                    validator.validate_reader_layout(record, root)

    def test_computability_subordinate_reader_layout_is_provenance_specific(self) -> None:
        provenance_id = "SRC-07494-07505"
        record_relative = f"spec/provenance/{provenance_id}.json"

        with tempfile.TemporaryDirectory(prefix="computability-layout-field-") as raw:
            root = self.stage_reader_layout_repository(Path(raw), provenance_id)
            record_path = root / record_relative
            record = validator.load_json(record_path)
            record["reader_layout"]["part_counter_effect"] = "increment once"
            self.write_record(record_path, record)
            completed = self.run_checker(root, record_relative)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("does not match the exact governed reader layout", completed.stderr)

        for name, token, replacement, expected in (
            ("missing-part", r"\part{Computability}", "", "part command"),
            (
                "duplicate-part",
                r"\part{Computability}",
                r"\part{Computability}" + "\n" + r"\part{Computability}",
                "part command",
            ),
            (
                "starred-part",
                r"\part{Computability}",
                r"\part*{Computability}",
                "part command",
            ),
            (
                "wrong-title",
                r"\part{Computability}",
                r"\part{Wrong}",
                "part command",
            ),
            ("missing-label", r"\label{part:computability}", "", "part label"),
            (
                "duplicate-label",
                r"\label{part:computability}",
                r"\label{part:computability}" + "\n"
                + r"\label{part:computability}",
                "part label",
            ),
        ):
            with self.subTest(name=name), tempfile.TemporaryDirectory(
                prefix=f"computability-layout-{name}-"
            ) as raw:
                root = self.stage_reader_layout_repository(Path(raw), provenance_id)
                record = validator.load_json(root / record_relative)
                artifact = root / record["restoration_artifact"]["path"]
                artifact.write_text(
                    artifact.read_text(encoding="utf-8").replace(token, replacement),
                    encoding="utf-8",
                    newline="\n",
                )
                with self.assertRaisesRegex(validator.CheckFailure, expected):
                    validator.validate_reader_layout(record, root)

        with tempfile.TemporaryDirectory(prefix="computability-layout-wrapper-") as raw:
            root = self.stage_reader_layout_repository(Path(raw), provenance_id)
            record = validator.load_json(root / record_relative)
            wrapper = root / record["reader_layout"]["wrapper_path"]
            wrapper.write_text(
                wrapper.read_text(encoding="utf-8") + "% drift\n",
                encoding="utf-8",
                newline="\n",
            )
            with self.assertRaisesRegex(validator.CheckFailure, "exact three-line form"):
                validator.validate_reader_layout(record, root)

        for name, mutate, expected in (
            (
                "missing-public-part",
                lambda text: text.replace(
                    r"\part{Computability and Complexity}\label{part:p04}", ""
                ),
                "exact public Part IV binding",
            ),
            (
                "wrapper-before-public-part",
                lambda text: text.replace(
                    r"\part{Computability and Complexity}\label{part:p04}" + "\n"
                    + r"\input{restoration/scope-SRC-07494-07505}",
                    r"\input{restoration/scope-SRC-07494-07505}" + "\n"
                    + r"\part{Computability and Complexity}\label{part:p04}",
                ),
                "must follow the public Part IV binding",
            ),
            (
                "driver-alias",
                lambda text: text
                + "\n"
                + r"\label{part:computability}"
                + "\n",
                "cannot acquire a source part label alias",
            ),
        ):
            with self.subTest(name=name), tempfile.TemporaryDirectory(
                prefix=f"computability-driver-{name}-"
            ) as raw:
                root = self.stage_reader_layout_repository(Path(raw), provenance_id)
                record = validator.load_json(root / record_relative)
                driver = root / record["reader_layout"]["public_part_file"]
                driver.write_text(
                    mutate(driver.read_text(encoding="utf-8")),
                    encoding="utf-8",
                    newline="\n",
                )
                with self.assertRaisesRegex(validator.CheckFailure, expected):
                    validator.validate_reader_layout(record, root)

    def test_model_theory_direct_public_layout_rejects_extra_part_surface(self) -> None:
        provenance_id = "SRC-06049-06069"
        for suffix, expected in (
            ("\\part{Extra Model Theory Part}\n", "part command"),
            ("\\label{part:extra-model-theory}\n", "part label"),
        ):
            with self.subTest(suffix=suffix), tempfile.TemporaryDirectory(
                prefix="model-theory-layout-extra-"
            ) as raw:
                root = self.stage_reader_layout_repository(Path(raw), provenance_id)
                record_path = root / f"spec/provenance/{provenance_id}.json"
                record = json.loads(record_path.read_text(encoding="utf-8"))
                artifact = root / record["restoration_artifact"]["path"]
                artifact.write_text(
                    artifact.read_text(encoding="utf-8") + suffix,
                    encoding="utf-8",
                    newline="\n",
                )
                with self.assertRaisesRegex(validator.CheckFailure, expected):
                    validator.validate_reader_layout(record, root)

    def test_model_theory_direct_public_layout_is_independently_fail_closed(self) -> None:
        provenance_id = "SRC-06049-06069"
        record_relative = f"spec/provenance/{provenance_id}.json"

        with tempfile.TemporaryDirectory(prefix="model-theory-layout-field-") as raw:
            root = self.stage_reader_layout_repository(Path(raw), provenance_id)
            record_path = root / record_relative
            record = validator.load_json(record_path)
            record["reader_layout"]["part_counter_effect"] = "no increment"
            self.write_record(record_path, record)
            completed = self.run_checker(root, record_relative)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("does not match the exact governed reader layout", completed.stderr)

        for name, token, replacement, expected in (
            ("missing-part", r"\part{Model Theory}", "", "part command"),
            (
                "duplicate-part",
                r"\part{Model Theory}",
                r"\part{Model Theory}" + "\n" + r"\part{Model Theory}",
                "part command",
            ),
            (
                "missing-label",
                r"\label{part:model-theory}",
                "",
                "part label",
            ),
            (
                "duplicate-label",
                r"\label{part:model-theory}",
                r"\label{part:model-theory}" + "\n"
                + r"\label{part:model-theory}",
                "part label",
            ),
        ):
            with self.subTest(name=name), tempfile.TemporaryDirectory(
                prefix=f"model-theory-layout-{name}-"
            ) as raw:
                root = self.stage_reader_layout_repository(Path(raw), provenance_id)
                record = validator.load_json(root / record_relative)
                artifact = root / record["restoration_artifact"]["path"]
                artifact.write_text(
                    artifact.read_text(encoding="utf-8").replace(token, replacement),
                    encoding="utf-8",
                    newline="\n",
                )
                with self.assertRaisesRegex(validator.CheckFailure, expected):
                    validator.validate_reader_layout(record, root)

        with tempfile.TemporaryDirectory(prefix="model-theory-layout-wrapper-") as raw:
            root = self.stage_reader_layout_repository(Path(raw), provenance_id)
            record = validator.load_json(root / record_relative)
            wrapper = root / record["reader_layout"]["wrapper_path"]
            wrapper.write_text(
                wrapper.read_text(encoding="utf-8") + "% drift\n",
                encoding="utf-8",
                newline="\n",
            )
            with self.assertRaisesRegex(validator.CheckFailure, "exact three-line form"):
                validator.validate_reader_layout(record, root)

        for name, prefix, expected in (
            ("wrong-order", r"\input{parts/p03/other}" + "\n", "first direct input"),
            ("driver-part", r"\part{Model Theory}" + "\n", "exact artifact"),
            (
                "driver-label",
                r"\label{part:model-theory}" + "\n",
                "driver label alias",
            ),
        ):
            with self.subTest(name=name), tempfile.TemporaryDirectory(
                prefix=f"model-theory-driver-{name}-"
            ) as raw:
                root = self.stage_reader_layout_repository(Path(raw), provenance_id)
                record = validator.load_json(root / record_relative)
                driver = root / record["reader_layout"]["public_part_file"]
                driver.write_text(
                    prefix + driver.read_text(encoding="utf-8"),
                    encoding="utf-8",
                    newline="\n",
                )
                with self.assertRaisesRegex(validator.CheckFailure, expected):
                    validator.validate_reader_layout(record, root)

    def test_reader_layout_schema_v2_is_provenance_specific(self) -> None:
        with tempfile.TemporaryDirectory(prefix="reader-layout-id-") as raw:
            root = self.stage_reader_layout_repository(Path(raw))
            old_path = root / "spec/provenance/SRC-01649-01660.json"
            record = json.loads(old_path.read_text(encoding="utf-8"))
            record["provenance_id"] = "SRC-01650-01660"
            new_path = old_path.with_name("SRC-01650-01660.json")
            self.write_record(new_path, record)
            old_path.unlink()
            completed = self.run_checker(root, "spec/provenance/SRC-01650-01660.json")
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("schema_version 2 is reserved", completed.stderr)

        with tempfile.TemporaryDirectory(prefix="reader-layout-v1-") as raw:
            root = self.stage_reader_layout_repository(Path(raw))
            path = root / "spec/provenance/SRC-01649-01660.json"
            record = json.loads(path.read_text(encoding="utf-8"))
            record["schema_version"] = 1
            self.write_record(path, record)
            completed = self.run_checker(root, "spec/provenance/SRC-01649-01660.json")
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("extra=['reader_layout']", completed.stderr)

    def test_reader_layout_fields_are_closed_and_exact(self) -> None:
        cases = (
            ("missing", lambda layout: layout.pop("toc_level"), "missing=['toc_level']"),
            ("extra", lambda layout: layout.__setitem__("ignore", True), "extra=['ignore']"),
            (
                "mutated",
                lambda layout: layout.__setitem__("reader_heading_title", "Wrong"),
                "does not match the exact governed reader layout",
            ),
        )
        for name, mutate, expected in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory(
                prefix=f"reader-layout-{name}-"
            ) as raw:
                root = self.stage_reader_layout_repository(Path(raw))
                path = root / "spec/provenance/SRC-01649-01660.json"
                record = json.loads(path.read_text(encoding="utf-8"))
                mutate(record["reader_layout"])
                self.write_record(path, record)
                completed = self.run_checker(
                    root, "spec/provenance/SRC-01649-01660.json"
                )
                self.assertNotEqual(completed.returncode, 0)
                self.assertIn(expected, completed.stderr)

    def test_reader_layout_rejects_altered_missing_and_duplicate_source_tokens(self) -> None:
        command = r"\part{Classical Propositional Logic}"
        label = r"\label{part:classical-propositional}"
        cases = (
            ("missing part", lambda text: text.replace(command, ""), "part command"),
            ("altered part", lambda text: text.replace(command, r"\part{Wrong}"), "part command"),
            ("duplicate part", lambda text: text.replace(command, command + "\n" + command), "part command"),
            ("missing label", lambda text: text.replace(label, ""), "part label"),
            ("altered label", lambda text: text.replace(label, r"\label{part:wrong}"), "part label"),
            ("duplicate label", lambda text: text.replace(label, label + "\n" + label), "part label"),
        )
        for name, mutate, expected in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory(
                prefix="reader-layout-source-"
            ) as raw:
                root = self.stage_reader_layout_repository(Path(raw))
                record_path = root / "spec/provenance/SRC-01649-01660.json"
                record = validator.load_json(record_path)
                artifact = root / "handbook/restoration/inherited-01649-01660.tex"
                artifact.write_text(
                    mutate(artifact.read_text(encoding="utf-8")),
                    encoding="utf-8",
                    newline="\n",
                )
                with self.assertRaisesRegex(validator.CheckFailure, expected):
                    validator.validate_reader_layout(record, root)

    def test_reader_layout_rejects_wrapper_drift(self) -> None:
        with tempfile.TemporaryDirectory(prefix="reader-layout-wrapper-") as raw:
            root = self.stage_reader_layout_repository(Path(raw))
            wrapper = root / "handbook/restoration/scope-SRC-01649-01660.tex"
            wrapper.write_text(
                wrapper.read_text(encoding="utf-8") + "% drift\n",
                encoding="utf-8",
                newline="\n",
            )
            completed = self.run_checker(
                root, "spec/provenance/SRC-01649-01660.json"
            )
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("exact three-line form", completed.stderr)

    def test_reader_layout_rejects_public_binding_and_order_drift(self) -> None:
        cases = (
            (
                "binding",
                lambda text: text.replace(
                    r"\part{Classical Logic}\label{part:p02}",
                    r"\part{Classical Logic}",
                ),
                "exact public Part II binding",
            ),
            (
                "order",
                lambda text: text.replace(
                    r"\part{Classical Logic}\label{part:p02}" + "\n"
                    + r"\input{restoration/scope-SRC-01649-01660}",
                    r"\input{restoration/scope-SRC-01649-01660}" + "\n"
                    + r"\part{Classical Logic}\label{part:p02}",
                ),
                "must follow the public Part II binding",
            ),
        )
        for name, mutate, expected in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory(
                prefix=f"reader-layout-public-{name}-"
            ) as raw:
                root = self.stage_reader_layout_repository(Path(raw))
                driver = root / "handbook/parts/p02.tex"
                driver.write_text(
                    mutate(driver.read_text(encoding="utf-8")),
                    encoding="utf-8",
                    newline="\n",
                )
                completed = self.run_checker(
                    root, "spec/provenance/SRC-01649-01660.json"
                )
                self.assertNotEqual(completed.returncode, 0)
                self.assertIn(expected, completed.stderr)

    def test_first_order_reader_layout_is_independently_fail_closed(self) -> None:
        provenance_id = "SRC-03022-03037"
        record_relative = f"spec/provenance/{provenance_id}.json"

        with tempfile.TemporaryDirectory(prefix="fol-reader-layout-field-") as raw:
            root = self.stage_reader_layout_repository(Path(raw), provenance_id)
            path = root / record_relative
            record = validator.load_json(path)
            record["reader_layout"]["reader_heading_title"] = "Wrong"
            self.write_record(path, record)
            completed = self.run_checker(root, record_relative)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("does not match the exact governed reader layout", completed.stderr)

        with tempfile.TemporaryDirectory(prefix="fol-reader-layout-source-") as raw:
            root = self.stage_reader_layout_repository(Path(raw), provenance_id)
            path = root / record_relative
            record = validator.load_json(path)
            artifact = root / record["restoration_artifact"]["path"]
            command = record["reader_layout"]["source_part_command"]
            artifact.write_text(
                artifact.read_text(encoding="utf-8").replace(
                    command, command + "\n" + command
                ),
                encoding="utf-8",
                newline="\n",
            )
            with self.assertRaisesRegex(validator.CheckFailure, "part command"):
                validator.validate_reader_layout(record, root)

        with tempfile.TemporaryDirectory(prefix="fol-reader-layout-wrapper-") as raw:
            root = self.stage_reader_layout_repository(Path(raw), provenance_id)
            path = root / record_relative
            record = validator.load_json(path)
            wrapper = root / record["reader_layout"]["wrapper_path"]
            wrapper.write_text(
                wrapper.read_text(encoding="utf-8") + "% drift\n",
                encoding="utf-8",
                newline="\n",
            )
            completed = self.run_checker(root, record_relative)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("exact three-line form", completed.stderr)

        with tempfile.TemporaryDirectory(prefix="fol-reader-layout-order-") as raw:
            root = self.stage_reader_layout_repository(Path(raw), provenance_id)
            driver = root / "handbook/parts/p02.tex"
            public = r"\part{Classical Logic}\label{part:p02}"
            wrapper_input = r"\input{restoration/scope-SRC-03022-03037}"
            text = driver.read_text(encoding="utf-8")
            text = text.replace(wrapper_input + "\n", "", 1)
            driver.write_text(
                wrapper_input + "\n" + text,
                encoding="utf-8",
                newline="\n",
            )
            self.assertIn(public, text)
            completed = self.run_checker(root, record_relative)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("must follow the public Part II binding", completed.stderr)

    def test_changed_restoration_content_byte_fails(self) -> None:
        with tempfile.TemporaryDirectory(prefix="inherited-restoration-test-") as raw:
            root = self.stage_repository(Path(raw))
            artifact = root / "handbook/restoration/inherited-09099-09111.tex"
            artifact.write_bytes(
                artifact.read_bytes().replace(b"Robinson arithmetic", b"Rxbinsxn arithmetic", 1)
            )

            completed = self.run_checker(root)

        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("restoration artifact digest mismatch", completed.stderr)

    def test_changed_content_with_rewritten_artifact_hash_still_fails(self) -> None:
        with tempfile.TemporaryDirectory(prefix="inherited-restoration-test-") as raw:
            root = self.stage_repository(Path(raw))
            artifact_path = root / "handbook/restoration/inherited-09099-09111.tex"
            record_path = root / "spec/provenance/SRC-09099-09111.json"
            artifact = artifact_path.read_bytes().replace(
                b"Robinson arithmetic", b"Rxbinsxn arithmetic", 1
            )
            artifact_path.write_bytes(artifact)
            record = json.loads(record_path.read_text(encoding="utf-8"))
            record["restoration_artifact"]["sha256"] = hashlib.sha256(artifact).hexdigest()
            record["restoration_artifact"]["content_token_sha256"] = hashlib.sha256(
                artifact
            ).hexdigest()
            record_path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")

            completed = self.run_checker(root)

        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("source content-token digest", completed.stderr)

    def test_coordinated_authority_and_metadata_drift_still_fails(self) -> None:
        with tempfile.TemporaryDirectory(prefix="inherited-restoration-test-") as raw:
            root = self.stage_repository(Path(raw))
            source_path = root / "source/formal-logic-reference.tex"
            artifact_path = root / "handbook/restoration/inherited-09099-09111.tex"
            record_path = root / "spec/provenance/SRC-09099-09111.json"
            manifest_path = root / "spec/inherited-corpus-manifest.json"
            map_path = root / "spec/inherited-source-map.csv"

            source_bytes = source_path.read_bytes().replace(
                b"Robinson arithmetic", b"Rxbinsxn arithmetic", 1
            )
            source_path.write_bytes(source_bytes)
            source_lines = source_bytes.splitlines(keepends=True)
            interval = b"".join(source_lines[9098:9111])
            artifact = b"\n".join(
                line.rstrip(b"\r\n") for line in source_lines[9098:9111]
            ) + b"\n"
            artifact_path.write_bytes(artifact)

            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["tex"]["bytes"] = len(source_bytes)
            manifest["tex"]["sha256"] = hashlib.sha256(source_bytes).hexdigest()
            manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

            record = json.loads(record_path.read_text(encoding="utf-8"))
            record["authority"]["bytes"] = len(source_bytes)
            record["authority"]["sha256"] = hashlib.sha256(source_bytes).hexdigest()
            record["source_locator"]["interval_sha256"] = hashlib.sha256(interval).hexdigest()
            record["restoration_artifact"]["bytes"] = len(artifact)
            record["restoration_artifact"]["sha256"] = hashlib.sha256(artifact).hexdigest()
            record["restoration_artifact"]["content_token_sha256"] = hashlib.sha256(
                artifact
            ).hexdigest()
            record_path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")

            rows: list[dict[str, str]]
            with map_path.open("r", encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                fieldnames = list(reader.fieldnames or [])
                rows = list(reader)
            for row in rows:
                if row["stable_id"] == "SRC-09099-09111":
                    row["source_sha256"] = hashlib.sha256(interval).hexdigest()
            with map_path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
                writer.writeheader()
                writer.writerows(rows)

            completed = self.run_checker(root)

        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("frozen authority", completed.stderr)

    def test_locator_that_truncates_the_identified_source_unit_fails(self) -> None:
        with tempfile.TemporaryDirectory(prefix="inherited-restoration-test-") as raw:
            root = self.stage_repository(Path(raw))
            old_record = root / "spec/provenance/SRC-09099-09111.json"
            new_record = root / "spec/provenance/SRC-09100-09111.json"
            old_artifact = root / "handbook/restoration/inherited-09099-09111.tex"
            new_artifact = root / "handbook/restoration/inherited-09100-09111.tex"
            source_lines = (
                root / "source/formal-logic-reference.tex"
            ).read_bytes().splitlines(keepends=True)
            interval = b"".join(source_lines[9099:9111])
            artifact = b"\n".join(
                line.rstrip(b"\r\n") for line in source_lines[9099:9111]
            ) + b"\n"
            new_artifact.write_bytes(artifact)
            old_artifact.unlink()

            record = json.loads(old_record.read_text(encoding="utf-8"))
            record["provenance_id"] = "SRC-09100-09111"
            record["source_locator"] = {
                "start_line": 9100,
                "end_line": 9111,
                "line_count": 12,
                "interval_sha256": hashlib.sha256(interval).hexdigest(),
            }
            record["restoration_artifact"].update(
                {
                    "path": "handbook/restoration/inherited-09100-09111.tex",
                    "bytes": len(artifact),
                    "physical_lines": 12,
                    "sha256": hashlib.sha256(artifact).hexdigest(),
                    "content_token_sha256": hashlib.sha256(artifact).hexdigest(),
                }
            )
            record["audit_evidence"]["interval_ids"] = ["SRC-09100-09111"]
            new_record.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
            old_record.unlink()

            map_path = root / "spec/inherited-source-map.csv"
            with map_path.open("r", encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                fieldnames = list(reader.fieldnames or [])
                rows = list(reader)
            for row in rows:
                if row["stable_id"] == "SRC-09099-09111":
                    row["stable_id"] = "SRC-09100-09111"
                    row["source_start"] = "9100"
                    row["source_line_count"] = "12"
                    row["source_sha256"] = hashlib.sha256(interval).hexdigest()
            with map_path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
                writer.writeheader()
                writer.writerows(rows)

            completed = self.run_checker(
                root, "spec/provenance/SRC-09100-09111.json"
            )

        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("source-unit locator mismatch", completed.stderr)

    def test_nonprinting_interval_can_leave_destination_open(self) -> None:
        with tempfile.TemporaryDirectory(prefix="inherited-restoration-test-") as raw:
            root = self.stage_repository(Path(raw))
            source_lines = (
                root / "source/formal-logic-reference.tex"
            ).read_bytes().splitlines(keepends=True)
            interval = b"".join(source_lines[38:47])
            artifact_path = root / "handbook/restoration/inherited-00039-00047.tex"
            artifact = artifact_path.read_bytes()
            record = json.loads(
                (root / "spec/provenance/SRC-09099-09111.json").read_text(
                    encoding="utf-8"
                )
            )
            record["provenance_id"] = "PRE-00039-00047"
            record["source_locator"] = {
                "start_line": 39,
                "end_line": 47,
                "line_count": 9,
                "interval_sha256": hashlib.sha256(interval).hexdigest(),
            }
            record["source_unit_evidence"]["unit_ordinals"] = []
            record["artifact_line_standing"] = "nonprinting control syntax"
            record["presentation_identity"] = {
                "kind": "PDF metadata",
                "source_title": "Formal Logic: Language, Semantics, Deduction, and Metatheory",
                "description": "The exact PDF metadata declarations at source lines 39--47.",
            }
            record["restoration_artifact"].update(
                {
                    "path": "handbook/restoration/inherited-00039-00047.tex",
                    "bytes": len(artifact),
                    "physical_lines": 9,
                    "sha256": hashlib.sha256(artifact).hexdigest(),
                    "content_token_sha256": hashlib.sha256(artifact).hexdigest(),
                }
            )
            record["handbook_destination"] = {
                "status": "open/missing",
                "file": "",
                "stable_label": "",
                "reason": "Nonprinting control syntax has no final integrated-layout destination yet.",
            }
            record["audit_evidence"]["interval_ids"] = ["PRE-00039-00047"]
            record["audit_evidence"]["classifications"] = ["altered"]
            record_path = root / "spec/provenance/PRE-00039-00047.json"
            record_path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")

            completed = self.run_checker(
                root, "spec/provenance/PRE-00039-00047.json"
            )

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )

    def test_audit_interval_digest_drift_fails(self) -> None:
        with tempfile.TemporaryDirectory(prefix="inherited-restoration-test-") as raw:
            root = self.stage_repository(Path(raw))
            map_path = root / "spec/inherited-source-map.csv"
            with map_path.open("r", encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                fieldnames = list(reader.fieldnames or [])
                rows = list(reader)
            for row in rows:
                if row["stable_id"] == "SRC-09099-09111":
                    row["source_sha256"] = "0" * 64
            with map_path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
                writer.writeheader()
                writer.writerows(rows)

            completed = self.run_checker(root)

        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("audit interval digest mismatch", completed.stderr)


def make_corrected_reader_fixture(root: Path, record_path: Path, replacements: list[tuple[int, int, bytes]]) -> dict[str, object]:
    """Build an isolated cumulative edit map from an existing exact fixture."""
    original_record_bytes = record_path.read_bytes()
    record = json.loads(original_record_bytes)
    artifact_path = root / record["restoration_artifact"]["path"]
    original = artifact_path.read_bytes().splitlines(keepends=True)
    history = root / "spec/provenance/history" / record_path.name
    history.parent.mkdir(parents=True, exist_ok=True)
    history.write_bytes(original_record_bytes)
    policy_path = root / validator.CORRECTION_POLICY_PATH
    policy_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(REPO_ROOT / validator.CORRECTION_POLICY_PATH, policy_path)
    rationale = root / "spec/research/candidate-correction.md"
    rationale.parent.mkdir(parents=True, exist_ok=True)
    rationale.write_text("Isolated mechanical correction fixture; no mathematical admission.\n", encoding="utf-8")
    output: list[bytes] = []
    edits = []
    cursor = 0
    for start, end, replacement in replacements:
        output.extend(original[cursor:start])
        new_lines = replacement.splitlines(keepends=True)
        reader_start = len(output)
        output.extend(new_lines)
        edits.append({
            "source_range": [start, end], "reader_range": [reader_start, len(output)],
            "source_sha256": validator.sha256(validator.correction_slice_bytes(original[start:end], "fixture")),
            "reader_sha256": validator.sha256(validator.correction_slice_bytes(new_lines, "fixture")),
            "reason": "Exercise the recorded edit in an isolated fixture.",
        })
        cursor = end
    output.extend(original[cursor:])
    raw = b"".join(output)
    artifact_path.write_bytes(raw)
    record["schema_version"] = 4
    record["disposition"] = "full reconstruction"
    record["restoration_artifact"].update({
        "bytes": len(raw), "physical_lines": len(output),
        "sha256": validator.sha256(raw),
        "content_token_sha256": validator.sha256(validator.correction_slice_bytes(output, "fixture")),
        "content_token_comparison": validator.CORRECTED_CONTENT_COMPARISON,
    })
    record["handbook_destination"].update({
        "file": record["restoration_artifact"]["path"], "stable_label": "",
        "reason": "Candidate corrected reader; all independent admission gates remain pending.",
    })
    record["reader_correction"] = {
        "kind": "candidate corrected reader interval", "correction_id": "fixture.correction",
        "policy_authority": {"path": validator.CORRECTION_POLICY_PATH,
            "sha256": validator.sha256(policy_path.read_bytes()), "locator": validator.CORRECTION_POLICY_LOCATOR},
        "rationale": {"path": rationale.relative_to(root).as_posix(),
            "sha256": validator.sha256(rationale.read_bytes()), "locator": "complete fixture note"},
        "predecessor_record": {"path": history.relative_to(root).as_posix(),
            "sha256": validator.sha256(original_record_bytes)},
        "affected_ids": [record["provenance_id"]],
        "source_content_token_sha256": validator.sha256(validator.correction_slice_bytes(original, "fixture")),
        "edits": edits,
    }
    for evidence in record["verification_evidence"]:
        evidence["scope"] = validator.CORRECTION_VERIFICATION_SCOPES[evidence["kind"]]
        evidence["command"] = (
            "python tools/check_inherited_restoration.py --record "
            f"spec/provenance/{record['provenance_id']}.json"
        )
    InheritedRestorationCliTests.write_record(record_path, record)
    return record


class CorrectedReaderCandidateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="corrected-reader-")
        self.addCleanup(self.temp.cleanup)
        self.root = InheritedRestorationCliTests().stage_repository(Path(self.temp.name))
        self.path = self.root / "spec/provenance/SRC-09099-09111.json"

    def validate(self, record: dict[str, object]) -> None:
        validator.validate_record(record, self.path, self.root)

    def test_insertion_deletion_and_same_line_edits_map_only_unchanged_lines(self):
        record = make_corrected_reader_fixture(self.root, self.path,
            [(1, 1, b"Inserted reader explanation.\n"), (3, 4, b""), (6, 7, b"Corrected reader line.\n")])
        self.validate(record)
        mapping = validator.reader_source_line_map(record)
        self.assertEqual(mapping[1], 9099)
        self.assertIsNone(mapping[2])
        self.assertEqual(mapping[3], 9100)
        self.assertIsNone(mapping[7])
        self.assertEqual(record["verification"]["build"], "pending")
        self.assertEqual(record["verification"]["visual"], "pending")
        self.assertTrue(all(v == "pending" for v in record["completeness"].values()))

    def test_stale_reader_hash_is_rejected(self):
        record = make_corrected_reader_fixture(self.root, self.path, [(0, 1, b"Correction.\n")])
        (self.root / record["restoration_artifact"]["path"]).write_bytes(b"Unrecorded.\n")
        with self.assertRaises(validator.CheckFailure):
            self.validate(record)

    def test_each_edit_shape_accepts_its_actual_reader_length(self):
        for edit, length in (((1, 1, b"Inserted.\n"), 14),
                             ((1, 2, b""), 12),
                             ((1, 2, b"Replacement.\n"), 13)):
            with self.subTest(edit=edit), tempfile.TemporaryDirectory() as raw:
                root = InheritedRestorationCliTests().stage_repository(Path(raw))
                path = root / "spec/provenance/SRC-09099-09111.json"
                record = make_corrected_reader_fixture(root, path, [edit])
                validator.validate_record(record, path, root)
                self.assertEqual(record["restoration_artifact"]["physical_lines"], length)

    def test_rehashed_wrong_policy_and_predecessor_source_are_rejected(self):
        record = make_corrected_reader_fixture(self.root, self.path, [(1, 2, b"Correction.\n")])
        predecessor = self.root / record["reader_correction"]["predecessor_record"]["path"]
        old = predecessor.read_bytes()
        modified = json.loads(old); modified["provenance_id"] = "SRC-00001-00002"
        predecessor.write_text(json.dumps(modified), encoding="utf-8")
        bad = copy.deepcopy(record)
        bad["reader_correction"]["predecessor_record"]["sha256"] = validator.sha256(predecessor.read_bytes())
        with self.assertRaisesRegex(validator.CheckFailure, "wrong provenance_id"):
            self.validate(bad)
        predecessor.write_bytes(old)
        policy = self.root / validator.CORRECTION_POLICY_PATH
        policy.write_text("Unrelated policy; no correction authority.\n", encoding="utf-8")
        record["reader_correction"]["policy_authority"]["sha256"] = validator.sha256(policy.read_bytes())
        with self.assertRaisesRegex(validator.CheckFailure, "authorization absent"):
            self.validate(record)

    def test_incomplete_map_rejects_rehashed_unexplained_change(self):
        record = make_corrected_reader_fixture(self.root, self.path, [(0, 1, b"Correction.\n")])
        path = self.root / record["restoration_artifact"]["path"]
        raw = path.read_bytes() + b"Unrecorded extra line.\n"
        path.write_bytes(raw)
        record["restoration_artifact"].update(bytes=len(raw), physical_lines=len(raw.splitlines()),
            sha256=validator.sha256(raw), content_token_sha256=validator.sha256(raw))
        with self.assertRaisesRegex(validator.CheckFailure, "unchanged tail"):
            self.validate(record)

    def test_overlapping_and_wrong_slice_hashes_are_rejected(self):
        record = make_corrected_reader_fixture(self.root, self.path, [(1, 2, b"Correction.\n")])
        bad = copy.deepcopy(record); bad["reader_correction"]["edits"].append(copy.deepcopy(bad["reader_correction"]["edits"][0]))
        with self.assertRaisesRegex(validator.CheckFailure, "overlapping"):
            self.validate(bad)
        bad = copy.deepcopy(record); bad["reader_correction"]["edits"][0]["reader_sha256"] = "0" * 64
        with self.assertRaisesRegex(validator.CheckFailure, "slice digest"):
            self.validate(bad)

    def test_wrong_source_policy_and_predecessor_are_rejected(self):
        record = make_corrected_reader_fixture(self.root, self.path, [(1, 2, b"Correction.\n")])
        for group, field in (("authority", "sha256"), ("source_locator", "interval_sha256")):
            bad = copy.deepcopy(record); bad[group][field] = "0" * 64
            with self.assertRaises(validator.CheckFailure):
                self.validate(bad)
        bad = copy.deepcopy(record); bad["reader_correction"]["policy_authority"]["locator"] = "Unrelated policy"
        with self.assertRaisesRegex(validator.CheckFailure, "wrong correction policy"):
            self.validate(bad)
        bad = copy.deepcopy(record); bad["reader_correction"]["predecessor_record"]["sha256"] = "0" * 64
        with self.assertRaisesRegex(validator.CheckFailure, "digest mismatch"):
            self.validate(bad)
        bad = copy.deepcopy(record); bad["reader_correction"]["affected_ids"] = ["R-999", record["provenance_id"]]
        with self.assertRaisesRegex(validator.CheckFailure, "unknown affected"):
            self.validate(bad)

    def test_false_disposition_and_faked_acceptance_are_rejected(self):
        record = make_corrected_reader_fixture(self.root, self.path, [(1, 2, b"Correction.\n")])
        for disposition in ("full transcription", "layout-only relocation", "open/missing"):
            bad = copy.deepcopy(record); bad["disposition"] = disposition
            with self.assertRaises(validator.CheckFailure):
                self.validate(bad)
        bad = copy.deepcopy(record); bad["verification"]["build"] = "pass"
        with self.assertRaisesRegex(validator.CheckFailure, "must remain pending"):
            self.validate(bad)
        bad = copy.deepcopy(record); bad["verification_evidence"][0]["scope"] = "Exact unchanged transcription accepted."
        with self.assertRaisesRegex(validator.CheckFailure, "candidate validation"):
            self.validate(bad)

    def test_version4_requires_the_closed_correction_object(self):
        record = make_corrected_reader_fixture(self.root, self.path, [(1, 2, b"Correction.\n")])
        del record["reader_correction"]
        with self.assertRaisesRegex(validator.CheckFailure, "field mismatch"):
            self.validate(record)

    def test_same_changed_bytes_cannot_be_laundered_as_version1(self):
        record = make_corrected_reader_fixture(self.root, self.path, [(1, 2, b"Correction.\n")])
        record["schema_version"] = 1; record["disposition"] = "full transcription"
        del record["reader_correction"]
        record["restoration_artifact"]["content_token_comparison"] = validator.CONTENT_TOKEN_COMPARISON
        with self.assertRaisesRegex(validator.CheckFailure, "source content-token"):
            self.validate(record)


if __name__ == "__main__":
    unittest.main()

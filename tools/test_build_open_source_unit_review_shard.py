#!/usr/bin/env python3
"""Focused tests for mechanical OPEN source-unit shard construction."""

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from tools import build_open_source_unit_review_shard as builder


ROOT = Path(__file__).resolve().parents[1]
PILOT_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (406, 443),
        (444, 506),
        (507, 532),
        (533, 602),
        (603, 647),
        (648, 744),
        (745, 772),
        (773, 789),
        (790, 797),
    )
]
CLASSICAL_PROPOSITIONAL_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (1649, 1660),
        (1661, 1816),
        (1817, 1898),
        (1899, 1945),
        (1946, 2186),
    )
]
NATURAL_DEDUCTION_AND_SEQUENT_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (2187, 2192),
        (2193, 2340),
        (2341, 2450),
    )
]
PROPOSITIONAL_METATHEORY_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (2451, 2544),
        (2545, 2664),
        (2665, 2809),
        (2810, 2914),
        (2915, 2932),
        (2933, 3021),
    )
]
FIRST_ORDER_SYNTAX_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (3022, 3037),
        (3038, 3104),
        (3105, 3165),
        (3166, 3239),
        (3240, 3428),
    )
]
FIRST_ORDER_SEMANTICS_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (3429, 3518),
        (3519, 3680),
        (3681, 3728),
    )
]
FIRST_ORDER_THEORIES_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (3729, 3907),
        (3908, 3926),
    )
]
FIRST_ORDER_DEDUCTION_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (3927, 4061),
        (4062, 4108),
        (4109, 4213),
        (4214, 4234),
        (4235, 4305),
    )
]
FIRST_ORDER_COMPLETENESS_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (4306, 4575),
        (4576, 4712),
        (4713, 4920),
        (4921, 4967),
    )
]
FIRST_ORDER_CARDINALITY_NORMAL_FORMS_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (4968, 5042),
        (5043, 5131),
        (5132, 5567),
        (5568, 5923),
        (5924, 5959),
        (5960, 6048),
    )
]
MAPS_SUBSTRUCTURES_ELEMENTARITY_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (6049, 6069),
        (6070, 6137),
        (6138, 6242),
        (6243, 6331),
        (6332, 6421),
        (6422, 6431),
        (6432, 6493),
        (6494, 6509),
    )
]
TYPES_SATURATION_ULTRAPRODUCTS_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (6510, 6629),
        (6630, 6639),
        (6640, 6693),
        (6694, 6782),
        (6783, 6791),
        (6792, 6845),
        (6846, 6854),
        (6855, 6941),
        (6942, 7134),
        (7135, 7149),
    )
]
QE_CATEGORICITY_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (7150, 7294),
        (7295, 7468),
        (7469, 7493),
    )
]
MACHINES_EFFECTIVE_PROCEDURES_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (7494, 7505),
        (7506, 7677),
        (7678, 7752),
        (7753, 7843),
        (7844, 7850),
    )
]
UNIVERSAL_COMPUTATION_REDUCTIONS_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (7851, 8048),
        (8049, 8080),
        (8081, 8143),
        (8144, 8186),
        (8187, 8238),
        (8239, 8247),
    )
]
DECISION_HIERARCHY_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (8248, 8305),
        (8306, 8438),
        (8439, 8709),
        (8710, 8876),
        (8877, 8897),
        (8898, 9079),
    )
]
PART5_EXACT_RECORDS_EXCLUDING_ISLAND = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (9080, 9098),
        (9112, 9149),
        (9150, 9174),
        (9175, 9187),
        (9188, 9261),
        (9262, 9327),
        (9328, 9438),
        (9439, 9497),
        (9498, 9538),
        (9539, 9619),
        (9620, 9728),
        (9729, 9749),
        (9750, 9816),
        (9817, 9876),
        (9877, 9924),
        (9925, 9992),
        (9993, 10027),
        (10028, 10059),
    )
]
ZF_ZFC_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in ((10060, 10088), (10089, 10271), (10272, 10352))
]
CUMULATIVE_HIERARCHY_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (10353, 10451),
        (10452, 10520),
        (10521, 10558),
        (10559, 10674),
    )
]
CONSTRUCTIBILITY_FORCING_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (10675, 10769), (10770, 10825), (10826, 10881), (10882, 10899),
        (10900, 10988), (10989, 11011), (11012, 11052), (11053, 11103),
        (11104, 11126), (11127, 11199), (11200, 11239), (11240, 11279),
        (11280, 11293), (11294, 11314), (11315, 11337), (11338, 11353),
    )
]
PROOF_THEORY_CALCULI_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (11354, 11413), (11414, 11505), (11506, 11519), (11520, 11598),
        (11599, 11627), (11628, 11644), (11645, 11695), (11696, 11710),
        (11711, 11740), (11741, 11767), (11768, 11823), (11824, 11881),
        (11882, 11913), (11914, 11960),
    )
]
NORMALIZATION_ORDINAL_ANALYSIS_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (11961, 12029),
        (12030, 12100),
        (12101, 12132),
        (12133, 12217),
        (12218, 12248),
    )
]
SECOND_HIGHER_ORDER_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (12249, 12261), (12262, 12289), (12290, 12355), (12356, 12414),
        (12415, 12536), (12537, 12673), (12674, 12720), (12721, 12783),
        (12784, 12923), (12924, 12950), (12951, 12969),
    )
]
INTUITIONISTIC_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (12970, 12988), (12989, 13045), (13046, 13057),
        (13058, 13099), (13100, 13127), (13128, 13140),
        (13141, 13157), (13158, 13179), (13180, 13200),
    )
]
MODAL_TEMPORAL_EPISTEMIC_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (13201, 13213), (13214, 13254), (13255, 13284),
        (13285, 13316), (13317, 13339), (13340, 13409),
        (13410, 13439), (13440, 13471), (13472, 13478),
        (13479, 13518), (13519, 13551), (13552, 13564),
        (13565, 13583),
    )
]
MANY_VALUED_RELEVANCE_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (13584, 13613), (13614, 13640), (13641, 13699),
        (13700, 13730), (13731, 13774), (13775, 13788),
        (13789, 13806), (13807, 13861), (13862, 13896),
        (13897, 13918), (13919, 13938), (13939, 13971),
        (13972, 14000), (14001, 14015), (14016, 14034),
        (14035, 14051), (14052, 14068), (14069, 14094),
    )
]
FORMAL_PRACTICE_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (14095, 14146), (14147, 14169), (14170, 14202),
        (14203, 14230), (14231, 14270),
    )
]
RESEARCH_WORKFLOW_RECORDS = [
    ROOT / f"spec/provenance/SRC-{start:05d}-{end:05d}.json"
    for start, end in (
        (15030, 15050),
        (15051, 15068),
        (15069, 15077),
        (15078, 15091),
    )
]
REGISTERED_NOTATION_RECORDS = [
    ROOT / "spec/provenance/SRC-15093-15206.json"
]
BINDING_PRECEDENCE_RECORDS = [
    ROOT / "spec/provenance/SRC-15207-15239.json"
]
RULE_SHEETS_RECORDS = [ROOT / "spec/provenance/SRC-15240-15488.json"]
QUALIFYING_PROBLEMS_RECORDS = [ROOT / "spec/provenance/SRC-15489-15619.json"]
ADDITIONAL_PROBLEMS_RECORDS = [ROOT / "spec/provenance/SRC-15620-15637.json"]
EXERCISE_FEEDBACK_RECORDS = [ROOT / "spec/provenance/SRC-15638-16742.json"]


class OpenSourceUnitShardTests(unittest.TestCase):
    def test_pilot_builds_exactly_units_14_through_52_without_promotion(self) -> None:
        document = builder.build_document(PILOT_RECORDS, ROOT)
        records = document["records"]
        self.assertEqual([record["unit_ordinal"] for record in records], list(range(14, 53)))
        self.assertTrue(all(record["provenance_disposition"] == "open/missing" for record in records))
        self.assertTrue(all(record["audit_result"] == "pending/unclassified" for record in records))
        self.assertTrue(
            all(
                record["verification"]
                == {
                    "source_fidelity_ai": "pending",
                    "topic_specialist_ai": "pending",
                    "adversarial_publication_ai": "pending",
                    "static": "pass",
                    "build": "pending",
                    "visual": "pending",
                }
                for record in records
            )
        )

    def test_duplicate_provenance_input_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "duplicate unit ordinal"):
            builder.build_document([PILOT_RECORDS[0], PILOT_RECORDS[0]], ROOT)

    def test_classical_propositional_shard_keeps_units_135_through_166_open(self) -> None:
        document = builder.build_document(CLASSICAL_PROPOSITIONAL_RECORDS, ROOT)
        records = document["records"]
        self.assertEqual(
            [record["unit_ordinal"] for record in records], list(range(135, 167))
        )
        self.assertTrue(
            all(record["provenance_disposition"] == "open/missing" for record in records)
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in records)
        )
        self.assertTrue(
            all(record["layout_changes"] == [] for record in records)
        )
        self.assertTrue(
            all(record["defect_exclusions"] == [] for record in records)
        )
        self.assertTrue(
            all(
                record["verification"]
                == {
                    "source_fidelity_ai": "pending",
                    "topic_specialist_ai": "pending",
                    "adversarial_publication_ai": "pending",
                    "static": "pass",
                    "build": "pending",
                    "visual": "pending",
                }
                for record in records
            )
        )

    def test_zero_unit_interval_does_not_invent_a_record(self) -> None:
        document = builder.build_document(
            [ROOT / "spec/provenance/SRC-00171-00197.json"], ROOT
        )
        self.assertEqual(document["records"], [])

    def test_natural_deduction_shard_keeps_units_167_through_177_open(self) -> None:
        expected = builder.build_document(NATURAL_DEDUCTION_AND_SEQUENT_RECORDS, ROOT)
        shard_path = (
            ROOT
            / "spec/provenance/reviewed-source-unit-shards/00167-00177.json"
        )
        stored = json.loads(shard_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)

        records = stored["records"]
        self.assertEqual(
            [record["unit_ordinal"] for record in records], list(range(167, 178))
        )
        self.assertTrue(
            all(record["provenance_disposition"] == "open/missing" for record in records)
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in records)
        )
        self.assertTrue(all(record["layout_changes"] == [] for record in records))
        self.assertTrue(all(record["defect_exclusions"] == [] for record in records))
        self.assertTrue(
            all(
                record["verification"]
                == {
                    "source_fidelity_ai": "pending",
                    "topic_specialist_ai": "pending",
                    "adversarial_publication_ai": "pending",
                    "static": "pass",
                    "build": "pending",
                    "visual": "pending",
                }
                for record in records
            )
        )

    def test_propositional_metatheory_shard_keeps_units_178_through_221_open(self) -> None:
        expected = builder.build_document(PROPOSITIONAL_METATHEORY_RECORDS, ROOT)
        shard_path = (
            ROOT
            / "spec/provenance/reviewed-source-unit-shards/00178-00221.json"
        )
        stored = json.loads(shard_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)

        records = stored["records"]
        self.assertEqual(
            [record["unit_ordinal"] for record in records], list(range(178, 222))
        )
        self.assertTrue(
            all(record["provenance_disposition"] == "open/missing" for record in records)
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in records)
        )
        self.assertTrue(all(record["layout_changes"] == [] for record in records))
        self.assertTrue(all(record["defect_exclusions"] == [] for record in records))
        self.assertTrue(
            all(
                record["verification"]
                == {
                    "source_fidelity_ai": "pending",
                    "topic_specialist_ai": "pending",
                    "adversarial_publication_ai": "pending",
                    "static": "pass",
                    "build": "pending",
                    "visual": "pending",
                }
                for record in records
            )
        )

    def test_first_order_syntax_shard_keeps_units_222_through_246_open(self) -> None:
        expected = builder.build_document(FIRST_ORDER_SYNTAX_RECORDS, ROOT)
        shard_path = (
            ROOT
            / "spec/provenance/reviewed-source-unit-shards/00222-00246.json"
        )
        stored = json.loads(shard_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)

        records = stored["records"]
        self.assertEqual(
            [record["unit_ordinal"] for record in records], list(range(222, 247))
        )
        self.assertTrue(
            all(record["provenance_disposition"] == "open/missing" for record in records)
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in records)
        )
        self.assertTrue(all(record["layout_changes"] == [] for record in records))
        self.assertTrue(all(record["defect_exclusions"] == [] for record in records))
        self.assertTrue(
            all(
                record["verification"]
                == {
                    "source_fidelity_ai": "pending",
                    "topic_specialist_ai": "pending",
                    "adversarial_publication_ai": "pending",
                    "static": "pass",
                    "build": "pending",
                    "visual": "pending",
                }
                for record in records
            )
        )

    def test_first_order_semantics_shard_keeps_units_247_through_270_open(self) -> None:
        expected = builder.build_document(FIRST_ORDER_SEMANTICS_RECORDS, ROOT)
        shard_path = (
            ROOT
            / "spec/provenance/reviewed-source-unit-shards/00247-00270.json"
        )
        stored = json.loads(shard_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)

        records = stored["records"]
        self.assertEqual(
            [record["unit_ordinal"] for record in records], list(range(247, 271))
        )
        self.assertTrue(
            all(record["provenance_disposition"] == "open/missing" for record in records)
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in records)
        )
        self.assertTrue(all(record["layout_changes"] == [] for record in records))
        self.assertTrue(all(record["defect_exclusions"] == [] for record in records))
        self.assertTrue(
            all(
                record["verification"]
                == {
                    "source_fidelity_ai": "pending",
                    "topic_specialist_ai": "pending",
                    "adversarial_publication_ai": "pending",
                    "static": "pass",
                    "build": "pending",
                    "visual": "pending",
                }
                for record in records
            )
        )

    def test_first_order_theories_shard_keeps_units_271_through_281_open(self) -> None:
        expected = builder.build_document(FIRST_ORDER_THEORIES_RECORDS, ROOT)
        shard_path = (
            ROOT
            / "spec/provenance/reviewed-source-unit-shards/00271-00281.json"
        )
        stored = json.loads(shard_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)

        records = stored["records"]
        self.assertEqual(
            [record["unit_ordinal"] for record in records], list(range(271, 282))
        )
        self.assertTrue(
            all(record["provenance_disposition"] == "open/missing" for record in records)
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in records)
        )
        self.assertTrue(all(record["layout_changes"] == [] for record in records))
        self.assertTrue(all(record["defect_exclusions"] == [] for record in records))
        self.assertTrue(
            all(
                record["verification"]
                == {
                    "source_fidelity_ai": "pending",
                    "topic_specialist_ai": "pending",
                    "adversarial_publication_ai": "pending",
                    "static": "pass",
                    "build": "pending",
                    "visual": "pending",
                }
                for record in records
            )
        )

    def test_first_order_deduction_shard_keeps_units_282_through_307_open(self) -> None:
        expected = builder.build_document(FIRST_ORDER_DEDUCTION_RECORDS, ROOT)
        shard_path = (
            ROOT
            / "spec/provenance/reviewed-source-unit-shards/00282-00307.json"
        )
        stored = json.loads(shard_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)

        records = stored["records"]
        self.assertEqual(
            [record["unit_ordinal"] for record in records], list(range(282, 308))
        )
        self.assertTrue(
            all(record["provenance_disposition"] == "open/missing" for record in records)
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in records)
        )
        self.assertTrue(all(record["layout_changes"] == [] for record in records))
        self.assertTrue(all(record["defect_exclusions"] == [] for record in records))
        self.assertTrue(
            all(
                record["verification"]
                == {
                    "source_fidelity_ai": "pending",
                    "topic_specialist_ai": "pending",
                    "adversarial_publication_ai": "pending",
                    "static": "pass",
                    "build": "pending",
                    "visual": "pending",
                }
                for record in records
            )
        )

    def test_first_order_completeness_shard_keeps_units_308_through_345_open(self) -> None:
        expected = builder.build_document(FIRST_ORDER_COMPLETENESS_RECORDS, ROOT)
        shard_path = (
            ROOT
            / "spec/provenance/reviewed-source-unit-shards/00308-00345.json"
        )
        stored = json.loads(shard_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)

        records = stored["records"]
        self.assertEqual(
            [record["unit_ordinal"] for record in records], list(range(308, 346))
        )
        self.assertTrue(
            all(record["provenance_disposition"] == "open/missing" for record in records)
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in records)
        )
        self.assertTrue(all(record["layout_changes"] == [] for record in records))
        self.assertTrue(all(record["defect_exclusions"] == [] for record in records))
        self.assertTrue(
            all(
                record["verification"]
                == {
                    "source_fidelity_ai": "pending",
                    "topic_specialist_ai": "pending",
                    "adversarial_publication_ai": "pending",
                    "static": "pass",
                    "build": "pending",
                    "visual": "pending",
                }
                for record in records
            )
        )

    def test_first_order_cardinality_normal_forms_shard_keeps_units_346_through_405_open(self) -> None:
        expected = builder.build_document(FIRST_ORDER_CARDINALITY_NORMAL_FORMS_RECORDS, ROOT)
        shard_path = (
            ROOT
            / "spec/provenance/reviewed-source-unit-shards/00346-00405.json"
        )
        stored = json.loads(shard_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)

        records = stored["records"]
        self.assertEqual(
            [record["unit_ordinal"] for record in records], list(range(346, 406))
        )
        self.assertTrue(
            all(record["provenance_disposition"] == "open/missing" for record in records)
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in records)
        )
        self.assertTrue(all(record["layout_changes"] == [] for record in records))
        self.assertTrue(all(record["defect_exclusions"] == [] for record in records))
        self.assertTrue(
            all(
                record["verification"]
                == {
                    "source_fidelity_ai": "pending",
                    "topic_specialist_ai": "pending",
                    "adversarial_publication_ai": "pending",
                    "static": "pass",
                    "build": "pending",
                    "visual": "pending",
                }
                for record in records
            )
        )

    def test_maps_substructures_elementarity_shard_keeps_units_406_through_443_open(self) -> None:
        expected = builder.build_document(MAPS_SUBSTRUCTURES_ELEMENTARITY_RECORDS, ROOT)
        shard_path = (
            ROOT
            / "spec/provenance/reviewed-source-unit-shards/00406-00443.json"
        )
        stored = json.loads(shard_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)

        records = stored["records"]
        self.assertEqual(
            [record["unit_ordinal"] for record in records], list(range(406, 444))
        )
        self.assertTrue(
            all(record["provenance_disposition"] == "open/missing" for record in records)
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in records)
        )
        self.assertTrue(all(record["layout_changes"] == [] for record in records))
        self.assertTrue(all(record["defect_exclusions"] == [] for record in records))
        self.assertTrue(
            all(
                record["verification"]
                == {
                    "source_fidelity_ai": "pending",
                    "topic_specialist_ai": "pending",
                    "adversarial_publication_ai": "pending",
                    "static": "pass",
                    "build": "pending",
                    "visual": "pending",
                }
                for record in records
            )
        )
        by_ordinal = {record["unit_ordinal"]: record for record in records}
        self.assertEqual(
            by_ordinal[436]["stable_labels"],
            ["ex:maps-elementarity-01", "ex:diagram-test"],
        )

    def test_types_saturation_ultraproducts_shard_keeps_units_444_through_485_open(self) -> None:
        expected = builder.build_document(TYPES_SATURATION_ULTRAPRODUCTS_RECORDS, ROOT)
        shard_path = (
            ROOT
            / "spec/provenance/reviewed-source-unit-shards/00444-00485.json"
        )
        stored = json.loads(shard_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)

        records = stored["records"]
        self.assertEqual(
            [record["unit_ordinal"] for record in records], list(range(444, 486))
        )
        self.assertTrue(
            all(record["provenance_disposition"] == "open/missing" for record in records)
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in records)
        )
        self.assertTrue(all(record["layout_changes"] == [] for record in records))
        self.assertTrue(all(record["defect_exclusions"] == [] for record in records))
        self.assertTrue(
            all(
                record["verification"]
                == {
                    "source_fidelity_ai": "pending",
                    "topic_specialist_ai": "pending",
                    "adversarial_publication_ai": "pending",
                    "static": "pass",
                    "build": "pending",
                    "visual": "pending",
                }
                for record in records
            )
        )
        by_ordinal = {record["unit_ordinal"]: record for record in records}
        self.assertEqual(
            by_ordinal[451]["stable_labels"],
            ["ex:types-ultraproducts-01", "ex:type-space-basis"],
        )
        self.assertEqual(
            by_ordinal[462]["stable_labels"],
            ["ex:types-ultraproducts-02", "ex:homogeneity-back-step"],
        )
        self.assertEqual(
            by_ordinal[467]["stable_labels"],
            ["ex:types-ultraproducts-03", "ex:omit-constant-type"],
        )

    def test_qe_shard_keeps_all_source_declared_unit_labels_in_order(self) -> None:
        expected = builder.build_document(QE_CATEGORICITY_RECORDS, ROOT)
        shard_path = (
            ROOT
            / "spec/provenance/reviewed-source-unit-shards/00486-00516.json"
        )
        stored = json.loads(shard_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        records = stored["records"]
        self.assertEqual(
            [record["unit_ordinal"] for record in records], list(range(486, 517))
        )
        by_ordinal = {record["unit_ordinal"]: record for record in records}
        self.assertEqual(
            by_ordinal[514]["stable_labels"], ["ex:qe-categoricity-01"]
        )
        self.assertEqual(
            by_ordinal[515]["stable_labels"], ["ex:qe-categoricity-02"]
        )
        self.assertEqual(
            by_ordinal[516]["stable_labels"],
            ["ex:qe-categoricity-03", "ex:back-and-forth-equivalence"],
        )
        self.assertTrue(
            all(record["provenance_disposition"] == "open/missing" for record in records)
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in records)
        )
        self.assertTrue(all(record["layout_changes"] == [] for record in records))
        self.assertTrue(all(record["defect_exclusions"] == [] for record in records))
        self.assertTrue(
            all(
                record["verification"]
                == {
                    "source_fidelity_ai": "pending",
                    "topic_specialist_ai": "pending",
                    "adversarial_publication_ai": "pending",
                    "static": "pass",
                    "build": "pending",
                    "visual": "pending",
                }
                for record in records
            )
        )

    def test_machines_shard_keeps_units_517_through_543_open(self) -> None:
        expected = builder.build_document(MACHINES_EFFECTIVE_PROCEDURES_RECORDS, ROOT)
        shard_path = (
            ROOT
            / "spec/provenance/reviewed-source-unit-shards/00517-00543.json"
        )
        stored = json.loads(shard_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        records = stored["records"]
        self.assertEqual(
            [record["unit_ordinal"] for record in records], list(range(517, 544))
        )
        self.assertTrue(
            all(record["provenance_disposition"] == "open/missing" for record in records)
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in records)
        )
        self.assertTrue(all(record["layout_changes"] == [] for record in records))
        self.assertTrue(all(record["defect_exclusions"] == [] for record in records))
        self.assertTrue(
            all(
                record["verification"]
                == {
                    "source_fidelity_ai": "pending",
                    "topic_specialist_ai": "pending",
                    "adversarial_publication_ai": "pending",
                    "static": "pass",
                    "build": "pending",
                    "visual": "pending",
                }
                for record in records
            )
        )
        by_ordinal = {record["unit_ordinal"]: record for record in records}
        self.assertEqual(by_ordinal[517]["stable_labels"], ["part:computability"])
        self.assertEqual(
            by_ordinal[543]["stable_labels"], ["ex:turing-machines-01"]
        )

    def test_universal_computation_shard_keeps_units_544_through_573_open(self) -> None:
        expected = builder.build_document(
            UNIVERSAL_COMPUTATION_REDUCTIONS_RECORDS, ROOT
        )
        shard_path = (
            ROOT
            / "spec/provenance/reviewed-source-unit-shards/00544-00573.json"
        )
        stored = json.loads(shard_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        records = stored["records"]
        self.assertEqual(
            [record["unit_ordinal"] for record in records], list(range(544, 574))
        )
        self.assertTrue(
            all(record["provenance_disposition"] == "open/missing" for record in records)
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in records)
        )
        self.assertTrue(
            all(
                record["verification"]
                == {
                    "source_fidelity_ai": "pending",
                    "topic_specialist_ai": "pending",
                    "adversarial_publication_ai": "pending",
                    "static": "pass",
                    "build": "pending",
                    "visual": "pending",
                }
                for record in records
            )
        )
        by_ordinal = {record["unit_ordinal"]: record for record in records}
        self.assertEqual(by_ordinal[544]["stable_labels"], ["ch:universal-reductions"])
        self.assertEqual(
            by_ordinal[573]["stable_labels"], ["ex:universal-reductions-01"]
        )

    def test_decision_hierarchy_shard_keeps_units_574_through_615_open(self) -> None:
        expected = builder.build_document(DECISION_HIERARCHY_RECORDS, ROOT)
        shard_path = (
            ROOT
            / "spec/provenance/reviewed-source-unit-shards/00574-00615.json"
        )
        stored = json.loads(shard_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        records = stored["records"]
        self.assertEqual(
            [record["unit_ordinal"] for record in records], list(range(574, 616))
        )
        self.assertTrue(
            all(record["provenance_disposition"] == "open/missing" for record in records)
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in records)
        )
        self.assertTrue(
            all(
                record["verification"]
                == {
                    "source_fidelity_ai": "pending",
                    "topic_specialist_ai": "pending",
                    "adversarial_publication_ai": "pending",
                    "static": "pass",
                    "build": "pending",
                    "visual": "pending",
                }
                for record in records
            )
        )
        by_ordinal = {record["unit_ordinal"]: record for record in records}
        self.assertEqual(by_ordinal[574]["stable_labels"], ["ch:decision-hierarchy"])
        self.assertEqual(
            by_ordinal[604]["stable_labels"], ["ex:decision-hierarchy-01"]
        )
        self.assertEqual(
            by_ordinal[606]["stable_labels"], ["ex:decision-hierarchy-03"]
        )
        self.assertEqual(by_ordinal[615]["stable_labels"], ["rem:jump-convention"])

    def test_part5_shard_keeps_units_616_through_693_except_existing_island_open(self) -> None:
        expected = builder.build_document(PART5_EXACT_RECORDS_EXCLUDING_ISLAND, ROOT)
        shard_path = (
            ROOT
            / "spec/provenance/reviewed-source-unit-shards/00616-00693-excluding-00619.json"
        )
        stored = json.loads(shard_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        records = stored["records"]
        ordinals = [*range(616, 619), *range(620, 694)]
        self.assertEqual([record["unit_ordinal"] for record in records], ordinals)
        self.assertTrue(
            all(record["provenance_disposition"] == "open/missing" for record in records)
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in records)
        )
        self.assertTrue(
            all(
                record["verification"]
                == {
                    "source_fidelity_ai": "pending",
                    "topic_specialist_ai": "pending",
                    "adversarial_publication_ai": "pending",
                    "static": "pass",
                    "build": "pending",
                    "visual": "pending",
                }
                for record in records
            )
        )
        by_ordinal = {record["unit_ordinal"]: record for record in records}
        self.assertEqual(by_ordinal[616]["stable_labels"], ["part:incompleteness"])
        self.assertEqual(by_ordinal[646]["stable_labels"], ["ex:arithmetic-coding-03"])
        self.assertEqual(by_ordinal[693]["stable_labels"], ["ex:second-incompleteness-04"])

    def test_zf_zfc_shard_keeps_units_694_through_716_open(self) -> None:
        expected = builder.build_document(ZF_ZFC_RECORDS, ROOT)
        path = ROOT / "spec/provenance/reviewed-source-unit-shards/00694-00716.json"
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        self.assertEqual(
            [record["unit_ordinal"] for record in stored["records"]],
            list(range(694, 717)),
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in stored["records"])
        )

    def test_cumulative_hierarchy_shard_keeps_units_717_through_739_open(self) -> None:
        expected = builder.build_document(CUMULATIVE_HIERARCHY_RECORDS, ROOT)
        path = ROOT / "spec/provenance/reviewed-source-unit-shards/00717-00739.json"
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        self.assertEqual(
            [record["unit_ordinal"] for record in stored["records"]],
            list(range(717, 740)),
        )
        by_ordinal = {record["unit_ordinal"]: record for record in stored["records"]}
        self.assertEqual(by_ordinal[717]["stable_labels"], ["sec:cumulative-hierarchy-01"])
        self.assertEqual(by_ordinal[737]["stable_labels"], ["ex:cumulative-hierarchy-01"])
        self.assertEqual(by_ordinal[738]["stable_labels"], ["ex:cumulative-hierarchy-02"])
        self.assertEqual(by_ordinal[739]["stable_labels"], ["ex:cumulative-hierarchy-03"])
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in stored["records"])
        )

    def test_constructibility_forcing_shard_keeps_units_740_through_766_open(self) -> None:
        expected = builder.build_document(CONSTRUCTIBILITY_FORCING_RECORDS, ROOT)
        path = ROOT / "spec/provenance/reviewed-source-unit-shards/00740-00766.json"
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        self.assertEqual(
            [record["unit_ordinal"] for record in stored["records"]],
            list(range(740, 767)),
        )
        by_ordinal = {record["unit_ordinal"]: record for record in stored["records"]}
        self.assertEqual(by_ordinal[740]["stable_labels"], ["sec:constructibility-forcing-01"])
        self.assertEqual(by_ordinal[756]["stable_labels"], ["lem:relativization-derivations"])
        self.assertEqual(by_ordinal[758]["stable_labels"], ["thm:ch-relative-consistency"])
        self.assertEqual(by_ordinal[761]["stable_labels"], ["thm:ch-nonderivability"])
        self.assertEqual(by_ordinal[765]["stable_labels"], ["ex:constructibility-forcing-01"])
        self.assertEqual(by_ordinal[766]["stable_labels"], ["ex:constructibility-forcing-02"])
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in stored["records"])
        )

    def test_proof_theory_calculi_shard_keeps_units_767_through_807_open(self) -> None:
        expected = builder.build_document(PROOF_THEORY_CALCULI_RECORDS, ROOT)
        path = ROOT / "spec/provenance/reviewed-source-unit-shards/00767-00807.json"
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        self.assertEqual(
            [record["unit_ordinal"] for record in stored["records"]],
            list(range(767, 808)),
        )
        by_ordinal = {record["unit_ordinal"]: record for record in stored["records"]}
        self.assertEqual(by_ordinal[767]["stable_labels"], ["part:proof-theory"])
        self.assertEqual(by_ordinal[785]["stable_labels"], ["ex:lk-lj-01"])
        self.assertEqual(by_ordinal[787]["stable_labels"], ["ch:cut-elimination"])
        self.assertEqual(by_ordinal[790]["stable_labels"], ["lem:cut-mix-equipollence"])
        self.assertEqual(by_ordinal[794]["stable_labels"], ["lem:cutfree-subformula"])
        self.assertEqual(by_ordinal[806]["stable_labels"], ["thm:craig-interpolation"])
        self.assertEqual(by_ordinal[807]["stable_labels"], ["thm:beth"])
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in stored["records"])
        )

    def test_normalization_ordinal_shard_keeps_units_808_through_821_open(self) -> None:
        expected = builder.build_document(NORMALIZATION_ORDINAL_ANALYSIS_RECORDS, ROOT)
        path = ROOT / "spec/provenance/reviewed-source-unit-shards/00808-00821.json"
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        self.assertEqual(
            [record["unit_ordinal"] for record in stored["records"]],
            list(range(808, 822)),
        )
        by_ordinal = {record["unit_ordinal"]: record for record in stored["records"]}
        self.assertEqual(
            by_ordinal[808]["stable_labels"],
            ["sec:normalization-curry-howard-01"],
        )
        self.assertEqual(
            by_ordinal[811]["stable_labels"],
            ["sec:normalization-curry-howard-02"],
        )
        self.assertEqual(
            by_ordinal[818]["stable_labels"],
            ["ex:normalization-curry-howard-01"],
        )
        self.assertEqual(
            by_ordinal[821]["stable_labels"],
            ["ex:normalization-curry-howard-03"],
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in stored["records"])
        )

    def test_second_higher_order_shard_keeps_units_822_through_860_open(self) -> None:
        expected = builder.build_document(SECOND_HIGHER_ORDER_RECORDS, ROOT)
        path = ROOT / "spec/provenance/reviewed-source-unit-shards/00822-00860.json"
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        self.assertEqual(
            [record["unit_ordinal"] for record in stored["records"]],
            list(range(822, 861)),
        )
        by_ordinal = {record["unit_ordinal"]: record for record in stored["records"]}
        self.assertEqual(by_ordinal[822]["stable_labels"], ["part:higher-order"])
        self.assertEqual(by_ordinal[823]["stable_labels"], ["ch:second-order-logic"])
        self.assertEqual(
            by_ordinal[839]["stable_labels"],
            ["thm:second-order-reals-categorical"],
        )
        self.assertEqual(by_ordinal[840]["stable_labels"], ["thm:lindstrom"])
        self.assertEqual(
            by_ordinal[846]["stable_labels"],
            ["ex:second-order-logic-01"],
        )
        self.assertEqual(
            by_ordinal[858]["stable_labels"],
            ["ex:simple-type-theory-01"],
        )
        self.assertEqual(
            by_ordinal[860]["stable_labels"],
            ["ex:simple-type-theory-03"],
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in stored["records"])
        )

    def test_intuitionistic_shard_keeps_units_861_through_879_open(self) -> None:
        expected = builder.build_document(INTUITIONISTIC_RECORDS, ROOT)
        path = ROOT / "spec/provenance/reviewed-source-unit-shards/00861-00879.json"
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        self.assertEqual(
            [record["unit_ordinal"] for record in stored["records"]],
            list(range(861, 880)),
        )
        by_ordinal = {record["unit_ordinal"]: record for record in stored["records"]}
        self.assertEqual(by_ordinal[861]["stable_labels"], ["part:nonclassical"])
        self.assertEqual(by_ordinal[862]["stable_labels"], ["ch:intuitionistic-logic"])
        self.assertEqual(
            by_ordinal[864]["stable_labels"], ["sec:intuitionistic-logic-01"]
        )
        self.assertEqual(
            by_ordinal[873]["stable_labels"], ["ex:intuitionistic-logic-01"]
        )
        self.assertEqual(
            by_ordinal[879]["stable_labels"], []
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in stored["records"])
        )

    def test_modal_temporal_shard_keeps_units_880_through_896_open(self) -> None:
        expected = builder.build_document(MODAL_TEMPORAL_EPISTEMIC_RECORDS, ROOT)
        path = ROOT / "spec/provenance/reviewed-source-unit-shards/00880-00896.json"
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        self.assertEqual(
            [record["unit_ordinal"] for record in stored["records"]],
            list(range(880, 897)),
        )
        by_ordinal = {record["unit_ordinal"]: record for record in stored["records"]}
        self.assertEqual(
            by_ordinal[880]["stable_labels"], ["ch:modal-temporal-epistemic"]
        )
        self.assertEqual(
            by_ordinal[881]["stable_labels"],
            ["sec:modal-temporal-epistemic-01"],
        )
        self.assertEqual(
            by_ordinal[887]["stable_labels"],
            ["sec:modal-temporal-epistemic-02"],
        )
        self.assertEqual(
            by_ordinal[890]["stable_labels"],
            ["sec:modal-temporal-epistemic-03"],
        )
        self.assertEqual(
            by_ordinal[896]["stable_labels"],
            ["ex:modal-temporal-epistemic-03"],
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in stored["records"])
        )

    def test_many_relevance_shard_keeps_units_897_through_926_open(self) -> None:
        expected = builder.build_document(MANY_VALUED_RELEVANCE_RECORDS, ROOT)
        path = ROOT / "spec/provenance/reviewed-source-unit-shards/00897-00926.json"
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        self.assertEqual(
            [record["unit_ordinal"] for record in stored["records"]],
            list(range(897, 927)),
        )
        by_ordinal = {record["unit_ordinal"]: record for record in stored["records"]}
        self.assertEqual(
            by_ordinal[897]["stable_labels"], ["ch:many-valued-paraconsistent"]
        )
        self.assertEqual(
            by_ordinal[898]["stable_labels"],
            ["sec:many-valued-paraconsistent-01"],
        )
        self.assertEqual(
            by_ordinal[911]["stable_labels"],
            ["ex:many-valued-paraconsistent-01"],
        )
        self.assertEqual(
            by_ordinal[913]["stable_labels"], ["sec:relevance-linear-01"]
        )
        self.assertEqual(
            by_ordinal[926]["stable_labels"], ["ex:relevance-linear-04"]
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in stored["records"])
        )

    def test_formal_practice_shard_keeps_units_927_through_943_open(self) -> None:
        expected = builder.build_document(FORMAL_PRACTICE_RECORDS, ROOT)
        path = ROOT / "spec/provenance/reviewed-source-unit-shards/00927-00943.json"
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        self.assertEqual(
            [record["unit_ordinal"] for record in stored["records"]],
            list(range(927, 944)),
        )
        by_ordinal = {record["unit_ordinal"]: record for record in stored["records"]}
        self.assertEqual(by_ordinal[927]["stable_labels"], [])
        self.assertEqual(
            by_ordinal[928]["stable_labels"], ["ch:formal-practice"]
        )
        self.assertEqual(
            by_ordinal[929]["stable_labels"], ["sec:formal-practice-01"]
        )
        self.assertEqual(
            by_ordinal[942]["stable_labels"], ["ex:formal-practice-01"]
        )
        self.assertEqual(
            by_ordinal[943]["stable_labels"], ["ex:formal-practice-02"]
        )
        self.assertTrue(
            all(record["audit_result"] == "pending/unclassified" for record in stored["records"])
        )

    def test_research_workflow_shard_keeps_units_999_through_1005_open(self) -> None:
        expected = builder.build_document(RESEARCH_WORKFLOW_RECORDS, ROOT)
        path = ROOT / "spec/provenance/reviewed-source-unit-shards/00999-01005.json"
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        self.assertEqual(
            [record["unit_ordinal"] for record in stored["records"]],
            list(range(999, 1006)),
        )
        by_ordinal = {record["unit_ordinal"]: record for record in stored["records"]}
        self.assertEqual(
            by_ordinal[999]["stable_labels"], ["ch:research-workflow"]
        )
        self.assertEqual(
            by_ordinal[1000]["stable_labels"], ["sec:research-workflow-01"]
        )
        self.assertEqual(by_ordinal[1001]["stable_labels"], [])
        self.assertEqual(
            by_ordinal[1002]["stable_labels"], ["sec:research-workflow-02"]
        )
        self.assertEqual(
            by_ordinal[1003]["stable_labels"], ["sec:research-workflow-03"]
        )
        self.assertEqual(
            by_ordinal[1004]["stable_labels"], ["sec:research-workflow-04"]
        )
        self.assertEqual(by_ordinal[1005]["stable_labels"], [])
        self.assertTrue(
            all(
                record["audit_result"] == "pending/unclassified"
                for record in stored["records"]
            )
        )

    def test_registered_notation_shard_keeps_units_1006_through_1009_open(self) -> None:
        expected = builder.build_document(REGISTERED_NOTATION_RECORDS, ROOT)
        path = ROOT / "spec/provenance/reviewed-source-unit-shards/01006-01009.json"
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        self.assertEqual(
            [record["unit_ordinal"] for record in stored["records"]],
            list(range(1006, 1010)),
        )
        by_ordinal = {record["unit_ordinal"]: record for record in stored["records"]}
        self.assertEqual(
            by_ordinal[1006]["stable_labels"],
            ["ch:registered-notation", "app:notation"],
        )
        self.assertEqual(by_ordinal[1007]["stable_labels"], [])
        self.assertEqual(
            by_ordinal[1008]["stable_labels"], ["sec:registered-notation-01"]
        )
        self.assertEqual(
            by_ordinal[1009]["stable_labels"], ["sec:registered-notation-02"]
        )
        self.assertTrue(
            all(
                record["audit_result"] == "pending/unclassified"
                for record in stored["records"]
            )
        )

    def test_binding_precedence_shard_keeps_unit_1010_open(self) -> None:
        expected = builder.build_document(BINDING_PRECEDENCE_RECORDS, ROOT)
        path = ROOT / "spec/provenance/reviewed-source-unit-shards/01010-01010.json"
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        self.assertEqual(
            [record["unit_ordinal"] for record in stored["records"]], [1010]
        )
        self.assertEqual(
            stored["records"][0]["stable_labels"],
            ["ch:binding-precedence", "app:precedence"],
        )

    def test_rule_sheets_shard_keeps_units_1011_through_1025_open(self) -> None:
        expected = builder.build_document(RULE_SHEETS_RECORDS, ROOT)
        path = ROOT / "spec/provenance/reviewed-source-unit-shards/01011-01025.json"
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        self.assertEqual(
            [record["unit_ordinal"] for record in stored["records"]],
            list(range(1011, 1026)),
        )
        by_ordinal = {record["unit_ordinal"]: record for record in stored["records"]}
        self.assertEqual(
            by_ordinal[1011]["stable_labels"],
            ["ch:rule-sheets", "app:rules"],
        )
        self.assertEqual(by_ordinal[1012]["stable_labels"], ["sec:rule-sheets-01"])
        self.assertEqual(by_ordinal[1020]["stable_labels"], ["sec:rule-sheets-02"])
        # The frozen 1,055-row inventory has no separate row for the
        # optional-title section at line 15470.  Do not fabricate a unit or
        # attach its label to the preceding Logical identity unit; the exact
        # restoration/layout record governs sec:rule-sheets-03 independently.
        self.assertEqual(by_ordinal[1025]["stable_labels"], [])
        provenance = json.loads(
            RULE_SHEETS_RECORDS[0].read_text(encoding="utf-8")
        )
        self.assertIn(
            "sec:rule-sheets-03",
            provenance["reader_appendix_layout"]["source_labels"],
        )
        self.assertTrue(
            all(
                record["provenance_disposition"] == "open/missing"
                and record["audit_result"] == "pending/unclassified"
                for record in stored["records"]
            )
        )

    def test_qualifying_problems_shard_keeps_units_1026_through_1036_open(self) -> None:
        expected = builder.build_document(QUALIFYING_PROBLEMS_RECORDS, ROOT)
        path = ROOT / "spec/provenance/reviewed-source-unit-shards/01026-01036.json"
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        self.assertEqual(
            [record["unit_ordinal"] for record in stored["records"]],
            list(range(1026, 1037)),
        )
        by_ordinal = {record["unit_ordinal"]: record for record in stored["records"]}
        expected_labels = {
            1026: ["ch:qualifying-problems", "app:qualifying"],
            1027: ["sec:qualifying-problems-01", "prob:substitution"],
            1029: ["sec:qualifying-problems-02", "prob:compactness"],
            1031: ["sec:qualifying-problems-03", "prob:incompleteness"],
            1033: ["sec:qualifying-problems-04", "prob:modal-frame"],
            1035: ["sec:qualifying-problems-05", "prob:cut-subformula"],
        }
        for ordinal, labels in expected_labels.items():
            self.assertEqual(by_ordinal[ordinal]["stable_labels"], labels)
        for ordinal in (1028, 1030, 1032, 1034, 1036):
            self.assertEqual(by_ordinal[ordinal]["stable_labels"], [])
        self.assertTrue(
            all(
                record["provenance_disposition"] == "open/missing"
                and record["audit_result"] == "pending/unclassified"
                for record in stored["records"]
            )
        )

    def test_additional_problems_shard_keeps_unit_1037_open(self) -> None:
        expected = builder.build_document(ADDITIONAL_PROBLEMS_RECORDS, ROOT)
        path = ROOT / "spec/provenance/reviewed-source-unit-shards/01037-01037.json"
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        self.assertEqual(
            [record["unit_ordinal"] for record in stored["records"]], [1037]
        )
        self.assertEqual(
            stored["records"][0]["stable_labels"],
            ["sec:qualifying-problems-06"],
        )
        self.assertEqual(
            stored["records"][0]["provenance_disposition"], "open/missing"
        )
        self.assertEqual(
            stored["records"][0]["audit_result"], "pending/unclassified"
        )

    def test_exercise_feedback_shard_keeps_units_1038_through_1050_open(self) -> None:
        expected = builder.build_document(EXERCISE_FEEDBACK_RECORDS, ROOT)
        path = ROOT / "spec/provenance/reviewed-source-unit-shards/01038-01050.json"
        stored = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(stored, expected)
        self.assertEqual(
            [record["unit_ordinal"] for record in stored["records"]],
            list(range(1038, 1051)),
        )
        by_ordinal = {record["unit_ordinal"]: record for record in stored["records"]}
        self.assertEqual(
            by_ordinal[1038]["stable_labels"],
            ["ch:exercise-feedback", "app:exercise-feedback"],
        )
        for ordinal in range(1039, 1051):
            self.assertEqual(by_ordinal[ordinal]["stable_labels"], [])
        self.assertTrue(
            all(
                record["provenance_disposition"] == "open/missing"
                and record["audit_result"] == "pending/unclassified"
                for record in stored["records"]
            )
        )
        self.assertEqual(
            stored["records"][0]["audit_result"], "pending/unclassified"
        )

    def test_source_declared_unit_labels_fail_closed_on_mutation(self) -> None:
        document = builder.build_document(QE_CATEGORICITY_RECORDS, ROOT)
        by_ordinal = {record["unit_ordinal"]: record for record in document["records"]}
        self.assertEqual(len(by_ordinal[514]["stable_labels"]), 1)
        self.assertEqual(len(by_ordinal[516]["stable_labels"]), 2)
        cases = (
            ("single omission", 514, []),
            ("secondary omission", 516, ["ex:qe-categoricity-03"]),
            (
                "duplication",
                516,
                [
                    "ex:qe-categoricity-03",
                    "ex:back-and-forth-equivalence",
                    "ex:back-and-forth-equivalence",
                ],
            ),
            (
                "substitution",
                516,
                ["ex:qe-categoricity-03", "ex:qe-categoricity-02"],
            ),
            (
                "out-of-slice addition",
                516,
                [
                    "ex:qe-categoricity-03",
                    "ex:back-and-forth-equivalence",
                    "ex:qe-categoricity-02",
                ],
            ),
        )
        for name, ordinal, labels in cases:
            with self.subTest(name=name):
                mutated = copy.deepcopy(document)
                mutated_target = next(
                    record
                    for record in mutated["records"]
                    if record["unit_ordinal"] == ordinal
                )
                mutated_target["stable_labels"] = labels
                with self.assertRaisesRegex(
                    ValueError, "source-declared stable labels differ"
                ):
                    builder.validate_document(mutated, ROOT)

    def test_every_reviewed_source_label_is_stable_and_slice_exact(self) -> None:
        merged = json.loads(
            (ROOT / "spec/provenance/reviewed-source-unit-records.json").read_text(
                encoding="utf-8"
            )
        )
        inventory = builder.load_inventory(ROOT / "spec/source-unit-inventory.csv")
        authority_lines = (ROOT / builder.crosswalk.AUTHORITY_PATH).read_text(
            encoding="utf-8"
        ).splitlines()
        prefixes: set[str] = set()
        for record in merged["records"]:
            ordinal = record["unit_ordinal"]
            expected = builder.stable_labels_from_exact_slice(
                inventory[ordinal], authority_lines
            )
            self.assertEqual(record["stable_labels"], expected)
            primary = inventory[ordinal]["label"]
            if primary:
                self.assertIn(primary, record["stable_labels"])
                prefixes.add(primary.split(":", 1)[0])
        expected_prefixes = {
            inventory[record["unit_ordinal"]]["label"].split(":", 1)[0]
            for record in merged["records"]
            if inventory[record["unit_ordinal"]]["label"]
        }
        self.assertEqual(prefixes, expected_prefixes)


if __name__ == "__main__":
    unittest.main()

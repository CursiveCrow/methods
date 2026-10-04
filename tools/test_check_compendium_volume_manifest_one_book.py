#!/usr/bin/env python3
"""Focused tests for the single-publication handbook manifest."""

from __future__ import annotations

import copy
import shutil
import tempfile
import unittest
from pathlib import Path

from tools import check_compendium_volume_manifest as checker


HASH = "a" * 64
REPO_ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PART2_HIGHER_ORDER_IDS = (
    "SRC-12249-12261", "SRC-12262-12289", "SRC-12290-12355",
    "SRC-12356-12414", "SRC-12415-12536", "SRC-12537-12673",
    "SRC-12674-12720", "SRC-12721-12783", "SRC-12784-12923",
    "SRC-12924-12950", "SRC-12951-12969",
)
EXPECTED_PART3_RESTORATION_IDS = (
    "SRC-06049-06069",
    "SRC-06070-06137",
    "SRC-06138-06242",
    "SRC-06243-06331",
    "SRC-06332-06421",
    "SRC-06422-06431",
    "SRC-06432-06493",
    "SRC-06494-06509",
    "SRC-06510-06629",
    "SRC-06630-06639",
    "SRC-06640-06693",
    "SRC-06694-06782",
    "SRC-06783-06791",
    "SRC-06792-06845",
    "SRC-06846-06854",
    "SRC-06855-06941",
    "SRC-06942-07134",
    "SRC-07135-07149",
    "SRC-07150-07294",
    "SRC-07295-07468",
    "SRC-07469-07493",
)
EXPECTED_PART4_RESTORATION_IDS = (
    "SRC-07494-07505",
    "SRC-07506-07677",
    "SRC-07678-07752",
    "SRC-07753-07843",
    "SRC-07844-07850",
    "SRC-07851-08048",
    "SRC-08049-08080",
    "SRC-08081-08143",
    "SRC-08144-08186",
    "SRC-08187-08238",
    "SRC-08239-08247",
    "SRC-08248-08305",
    "SRC-08306-08438",
    "SRC-08439-08709",
    "SRC-08710-08876",
    "SRC-08877-08897",
    "SRC-08898-09079",
)
EXPECTED_PART5_RESTORATION_IDS = (
    "SRC-09080-09098",
    "SRC-09099-09111",
    "SRC-09112-09149",
    "SRC-09150-09174",
    "SRC-09175-09187",
    "SRC-09188-09261",
    "SRC-09262-09327",
    "SRC-09328-09438",
    "SRC-09439-09497",
    "SRC-09498-09538",
    "SRC-09539-09619",
    "SRC-09620-09728",
    "SRC-09729-09749",
    "SRC-09750-09816",
    "SRC-09817-09876",
    "SRC-09877-09924",
    "SRC-09925-09992",
    "SRC-09993-10027",
    "SRC-10028-10059",
)
EXPECTED_PART6_RESTORATION_IDS = (
    "SRC-10060-10088",
    "SRC-10089-10271",
    "SRC-10272-10352",
    "SRC-10353-10451",
    "SRC-10452-10520",
    "SRC-10521-10558",
    "SRC-10559-10674",
    "SRC-10675-10769",
    "SRC-10770-10825",
    "SRC-10826-10881",
    "SRC-10882-10899",
    "SRC-10900-10988",
    "SRC-10989-11011",
    "SRC-11012-11052",
    "SRC-11053-11103",
    "SRC-11104-11126",
    "SRC-11127-11199",
    "SRC-11200-11239",
    "SRC-11240-11279",
    "SRC-11280-11293",
    "SRC-11294-11314",
    "SRC-11315-11337",
    "SRC-11338-11353",
)
EXPECTED_PART7_RESTORATION_IDS = (
    "SRC-11354-11413",
    "SRC-11414-11505",
    "SRC-11506-11519",
    "SRC-11520-11598",
    "SRC-11599-11627",
    "SRC-11628-11644",
    "SRC-11645-11695",
    "SRC-11696-11710",
    "SRC-11711-11740",
    "SRC-11741-11767",
    "SRC-11768-11823",
    "SRC-11824-11881",
    "SRC-11882-11913",
    "SRC-11914-11960",
    "SRC-11961-12029",
    "SRC-12030-12100",
    "SRC-12101-12132",
    "SRC-12133-12217",
    "SRC-12218-12248",
)
EXPECTED_PART8_RESTORATION_IDS = (
    "SRC-12970-12988",
    "SRC-12989-13045",
    "SRC-13046-13057",
    "SRC-13058-13099",
    "SRC-13100-13127",
    "SRC-13128-13140",
    "SRC-13141-13157",
    "SRC-13158-13179",
    "SRC-13180-13200",
    "SRC-13201-13213",
    "SRC-13214-13254",
    "SRC-13255-13284",
    "SRC-13285-13316",
    "SRC-13317-13339",
    "SRC-13340-13409",
    "SRC-13410-13439",
    "SRC-13440-13471",
    "SRC-13472-13478",
    "SRC-13479-13518",
    "SRC-13519-13551",
    "SRC-13552-13564",
    "SRC-13565-13583",
    "SRC-13584-13613",
    "SRC-13614-13640",
    "SRC-13641-13699",
    "SRC-13700-13730",
    "SRC-13731-13774",
    "SRC-13775-13788",
    "SRC-13789-13806",
    "SRC-13807-13861",
    "SRC-13862-13896",
    "SRC-13897-13918",
    "SRC-13919-13938",
    "SRC-13939-13971",
    "SRC-13972-14000",
    "SRC-14001-14015",
    "SRC-14016-14034",
    "SRC-14035-14051",
    "SRC-14052-14068",
    "SRC-14069-14094",
)
EXPECTED_PART12_RESTORATION_IDS = (
    "SRC-14095-14146",
    "SRC-14147-14169",
    "SRC-14170-14202",
    "SRC-14203-14230",
    "SRC-14231-14270",
    "SRC-14271-14350",
    "SRC-14351-14400",
    "SRC-14401-14434",
    "SRC-14435-14479",
    "SRC-14480-14495",
    "SRC-14496-14521",
    "SRC-14522-14560",
    "SEP-14561-14561",
    "SRC-14562-14589",
    "SEP-14590-14590",
    "SRC-14591-14628",
    "SRC-14629-14660",
    "SRC-14661-14690",
    "SRC-14691-14728",
    "SRC-14729-14778",
    "SRC-14779-14814",
    "SRC-14815-14850",
    "SRC-14851-14870",
    "SRC-14871-14931",
    "SRC-14932-14945",
    "SRC-14946-14975",
    "SRC-14976-14990",
    "SRC-14991-15029",
    "SRC-15030-15050",
    "SRC-15051-15068",
    "SRC-15069-15077",
    "SRC-15078-15091",
    "SEP-15092-15092",
    "SRC-15093-15206",
    "SRC-15207-15239",
    "SRC-15240-15488",
    "SRC-15489-15619",
    "SRC-15620-15637",
    "SRC-15638-16742",
)


def valid_manifest() -> dict[str, object]:
    return {
        "schema_version": 2,
        "manifest_kind": "single-publication-handbook",
        "title": "The Methods of Reason",
        "public_artifact": {
            "artifact_id": "the-methods-of-reason",
            "title": "The Methods of Reason",
            "path": "handbook/main.pdf",
            "artifact_kind": "pdf",
            "publication_status": "construction-draft",
            "release_ready": False,
            "observed": {"bytes": 1, "pages": 1, "sha256": HASH},
        },
        "internal_authority_evidence": {
            "inherited_corpus_manifest": "spec/inherited-corpus-manifest.json",
            "published_with_book": False,
        },
        "final_release_evidence": None,
    }


class SinglePublicationManifestTests(unittest.TestCase):
    def test_live_part2_higher_order_source_contract_has_exact_suffix_and_route(self) -> None:
        self.assertEqual(
            checker.PART2_RESTORATION_IDS[-11:],
            EXPECTED_PART2_HIGHER_ORDER_IDS,
        )
        self.assertEqual(checker.validate_book_sources(REPO_ROOT), [])

    def test_live_part7_source_contract_has_exact_wrapper_tuple_and_route(self) -> None:
        self.assertEqual(
            checker.PART7_RESTORATION_IDS,
            EXPECTED_PART7_RESTORATION_IDS,
        )
        self.assertEqual(checker.validate_book_sources(REPO_ROOT), [])

    def test_live_part8_source_contract_has_exact_wrapper_tuple_and_route(self) -> None:
        self.assertEqual(
            checker.PART8_RESTORATION_IDS,
            EXPECTED_PART8_RESTORATION_IDS,
        )
        self.assertEqual(checker.validate_book_sources(REPO_ROOT), [])

    def test_live_part12_source_contract_has_exact_wrapper_tuple_and_route(self) -> None:
        self.assertEqual(
            checker.PART12_RESTORATION_IDS,
            EXPECTED_PART12_RESTORATION_IDS,
        )
        self.assertEqual(checker.validate_book_sources(REPO_ROOT), [])

    def assert_valid(self, manifest: dict[str, object]) -> None:
        self.assertEqual(checker.validate_manifest_structure(manifest), [])

    def assert_invalid(self, manifest: dict[str, object], fragment: str) -> None:
        failures = checker.validate_manifest_structure(manifest)
        self.assertTrue(
            any(fragment in failure for failure in failures),
            msg=f"missing {fragment!r} in {failures!r}",
        )

    def test_accepts_exact_one_book_construction_record(self) -> None:
        self.assert_valid(valid_manifest())

    def test_rejects_wrong_public_title(self) -> None:
        manifest = valid_manifest()
        manifest["public_artifact"]["title"] = "Formal Logic"  # type: ignore[index]
        self.assert_invalid(manifest, "title")

    def test_rejects_wrong_public_path(self) -> None:
        manifest = valid_manifest()
        manifest["public_artifact"]["path"] = "source/formal-logic-reference.pdf"  # type: ignore[index]
        self.assert_invalid(manifest, "handbook/main.pdf")

    def test_rejects_publishing_the_internal_authority(self) -> None:
        manifest = valid_manifest()
        manifest["internal_authority_evidence"]["published_with_book"] = True  # type: ignore[index]
        self.assert_invalid(manifest, "internal authority")

    def test_rejects_extra_publication_surfaces(self) -> None:
        manifest = valid_manifest()
        manifest["volumes"] = []
        self.assert_invalid(manifest, "fields differ")

    def test_rejects_release_ready_without_release_status(self) -> None:
        manifest = valid_manifest()
        manifest["public_artifact"]["release_ready"] = True  # type: ignore[index]
        self.assert_invalid(manifest, "release-ready")

    def test_accepts_terminal_release_shape(self) -> None:
        manifest = copy.deepcopy(valid_manifest())
        manifest["public_artifact"]["publication_status"] = "release"  # type: ignore[index]
        manifest["public_artifact"]["release_ready"] = True  # type: ignore[index]
        manifest["final_release_evidence"] = {
            "readiness_manifest_path": "spec/verification/final-readiness.json",
            "readiness_manifest_sha256": HASH,
            "user_final_acceptance_path": "spec/verification/user-final-acceptance.json",
            "user_final_acceptance_sha256": HASH,
            "public_pdf_sha256": HASH,
        }
        self.assert_valid(manifest)

    def test_rejects_release_without_terminal_evidence(self) -> None:
        manifest = valid_manifest()
        manifest["public_artifact"]["publication_status"] = "release"  # type: ignore[index]
        manifest["public_artifact"]["release_ready"] = True  # type: ignore[index]
        self.assert_invalid(manifest, "final_release_evidence")

    def test_rejects_unknown_publication_status(self) -> None:
        manifest = valid_manifest()
        manifest["public_artifact"]["publication_status"] = "provisional"  # type: ignore[index]
        self.assert_invalid(manifest, "publication_status")

    def test_book_source_contract_requires_exact_title_and_fourteen_parts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "handbook/parts").mkdir(parents=True)
            (root / "handbook/restoration").mkdir(parents=True)
            (root / "handbook/main.tex").write_text(
                "\\hypersetup{pdftitle={The Methods of Reason}}\n"
                + "".join(
                    f"\\input{{parts/p{number:02d}}}\n" for number in range(1, 15)
                ),
                encoding="utf-8",
            )
            (root / "handbook/publication-title.tex").write_text(
                "{\\Huge\\bfseries The Methods of Reason\\par}\n",
                encoding="utf-8",
            )
            (root / "handbook/parts/p01.tex").write_text(
                "\\input{restoration/scope-SRC-00363-00372}\n",
                encoding="utf-8",
            )
            (root / "handbook/restoration/scope-SRC-00363-00372.tex").write_text(
                "\\begin{inheritedrestorationscope}{SRC-00363-00372}\n"
                "\\input{restoration/inherited-00363-00372}\n"
                "\\end{inheritedrestorationscope}\n",
                encoding="utf-8",
            )
            (root / "handbook/restoration/inherited-00363-00372.tex").write_text(
                "\\part{Foundations of Formal Work}\n",
                encoding="utf-8",
            )
            for relative in (
                "source/formal-logic-reference.tex",
                "spec/inherited-corpus-manifest.json",
                "spec/inherited-source-map.csv",
                "spec/source-unit-inventory.csv",
                "spec/provenance/SRC-01649-01660.json",
                "spec/provenance/SRC-03022-03037.json",
                "spec/provenance/SRC-06049-06069.json",
                "spec/provenance/SRC-07494-07505.json",
                "handbook/restoration/scope-SRC-01649-01660.tex",
                "handbook/restoration/scope-SRC-01661-01816.tex",
                "handbook/restoration/scope-SRC-01817-01898.tex",
                "handbook/restoration/scope-SRC-01899-01945.tex",
                "handbook/restoration/scope-SRC-01946-02186.tex",
                "handbook/restoration/scope-SRC-02187-02192.tex",
                "handbook/restoration/scope-SRC-02193-02340.tex",
                "handbook/restoration/scope-SRC-02341-02450.tex",
                "handbook/restoration/scope-SRC-02451-02544.tex",
                "handbook/restoration/scope-SRC-02545-02664.tex",
                "handbook/restoration/scope-SRC-02665-02809.tex",
                "handbook/restoration/scope-SRC-02810-02914.tex",
                "handbook/restoration/scope-SRC-02915-02932.tex",
                "handbook/restoration/scope-SRC-02933-03021.tex",
                "handbook/restoration/scope-SRC-03022-03037.tex",
                "handbook/restoration/scope-SRC-03038-03104.tex",
                "handbook/restoration/scope-SRC-03105-03165.tex",
                "handbook/restoration/scope-SRC-03166-03239.tex",
                "handbook/restoration/scope-SRC-03240-03428.tex",
                "handbook/restoration/scope-SRC-03429-03518.tex",
                "handbook/restoration/scope-SRC-03519-03680.tex",
                "handbook/restoration/scope-SRC-03681-03728.tex",
                "handbook/restoration/scope-SRC-03729-03907.tex",
                "handbook/restoration/scope-SRC-03908-03926.tex",
                "handbook/restoration/scope-SRC-03927-04061.tex",
                "handbook/restoration/scope-SRC-04062-04108.tex",
                "handbook/restoration/scope-SRC-04109-04213.tex",
                "handbook/restoration/scope-SRC-04214-04234.tex",
                "handbook/restoration/scope-SRC-04235-04305.tex",
                "handbook/restoration/scope-SRC-04306-04575.tex",
                "handbook/restoration/scope-SRC-04576-04712.tex",
                "handbook/restoration/scope-SRC-04713-04920.tex",
                "handbook/restoration/scope-SRC-04921-04967.tex",
                "handbook/restoration/scope-SRC-04968-05042.tex",
                "handbook/restoration/scope-SRC-05043-05131.tex",
                "handbook/restoration/scope-SRC-05132-05567.tex",
                "handbook/restoration/scope-SRC-05568-05923.tex",
                "handbook/restoration/scope-SRC-05924-05959.tex",
                "handbook/restoration/scope-SRC-05960-06048.tex",
                "handbook/restoration/scope-SRC-06049-06069.tex",
                "handbook/restoration/scope-SRC-06070-06137.tex",
                "handbook/restoration/scope-SRC-06138-06242.tex",
                "handbook/restoration/scope-SRC-06243-06331.tex",
                "handbook/restoration/scope-SRC-06332-06421.tex",
                "handbook/restoration/scope-SRC-06422-06431.tex",
                "handbook/restoration/scope-SRC-06432-06493.tex",
                "handbook/restoration/scope-SRC-06494-06509.tex",
                "handbook/restoration/scope-SRC-06510-06629.tex",
                "handbook/restoration/scope-SRC-06630-06639.tex",
                "handbook/restoration/scope-SRC-06640-06693.tex",
                "handbook/restoration/scope-SRC-06694-06782.tex",
                "handbook/restoration/scope-SRC-06783-06791.tex",
                "handbook/restoration/scope-SRC-06792-06845.tex",
                "handbook/restoration/scope-SRC-06846-06854.tex",
                "handbook/restoration/scope-SRC-06855-06941.tex",
                "handbook/restoration/scope-SRC-06942-07134.tex",
                "handbook/restoration/scope-SRC-07135-07149.tex",
                "handbook/restoration/scope-SRC-07150-07294.tex",
                "handbook/restoration/scope-SRC-07295-07468.tex",
                "handbook/restoration/scope-SRC-07469-07493.tex",
                "handbook/restoration/scope-SRC-07494-07505.tex",
                "handbook/restoration/scope-SRC-07506-07677.tex",
                "handbook/restoration/scope-SRC-07678-07752.tex",
                "handbook/restoration/scope-SRC-07753-07843.tex",
                "handbook/restoration/scope-SRC-07844-07850.tex",
                "handbook/restoration/scope-SRC-07851-08048.tex",
                "handbook/restoration/scope-SRC-08049-08080.tex",
                "handbook/restoration/scope-SRC-08081-08143.tex",
                "handbook/restoration/scope-SRC-08144-08186.tex",
                "handbook/restoration/scope-SRC-08187-08238.tex",
                "handbook/restoration/scope-SRC-08239-08247.tex",
                "handbook/restoration/scope-SRC-08248-08305.tex",
                "handbook/restoration/scope-SRC-08306-08438.tex",
                "handbook/restoration/scope-SRC-08439-08709.tex",
                "handbook/restoration/scope-SRC-08710-08876.tex",
                "handbook/restoration/scope-SRC-08877-08897.tex",
                "handbook/restoration/scope-SRC-08898-09079.tex",
                "handbook/restoration/inherited-01649-01660.tex",
                "handbook/restoration/inherited-01661-01816.tex",
                "handbook/restoration/inherited-01817-01898.tex",
                "handbook/restoration/inherited-01899-01945.tex",
                "handbook/restoration/inherited-01946-02186.tex",
                "handbook/restoration/inherited-02187-02192.tex",
                "handbook/restoration/inherited-02193-02340.tex",
                "handbook/restoration/inherited-02341-02450.tex",
                "handbook/restoration/inherited-02451-02544.tex",
                "handbook/restoration/inherited-02545-02664.tex",
                "handbook/restoration/inherited-02665-02809.tex",
                "handbook/restoration/inherited-02810-02914.tex",
                "handbook/restoration/inherited-02915-02932.tex",
                "handbook/restoration/inherited-02933-03021.tex",
                "handbook/restoration/inherited-03022-03037.tex",
                "handbook/restoration/inherited-03038-03104.tex",
                "handbook/restoration/inherited-03105-03165.tex",
                "handbook/restoration/inherited-03166-03239.tex",
                "handbook/restoration/inherited-03240-03428.tex",
                "handbook/restoration/inherited-03429-03518.tex",
                "handbook/restoration/inherited-03519-03680.tex",
                "handbook/restoration/inherited-03681-03728.tex",
                "handbook/restoration/inherited-03729-03907.tex",
                "handbook/restoration/inherited-03908-03926.tex",
                "handbook/restoration/inherited-03927-04061.tex",
                "handbook/restoration/inherited-04062-04108.tex",
                "handbook/restoration/inherited-04109-04213.tex",
                "handbook/restoration/inherited-04214-04234.tex",
                "handbook/restoration/inherited-04235-04305.tex",
                "handbook/restoration/inherited-04306-04575.tex",
                "handbook/restoration/inherited-04576-04712.tex",
                "handbook/restoration/inherited-04713-04920.tex",
                "handbook/restoration/inherited-04921-04967.tex",
                "handbook/restoration/inherited-04968-05042.tex",
                "handbook/restoration/inherited-05043-05131.tex",
                "handbook/restoration/inherited-05132-05567.tex",
                "handbook/restoration/inherited-05568-05923.tex",
                "handbook/restoration/inherited-05924-05959.tex",
                "handbook/restoration/inherited-05960-06048.tex",
                "handbook/restoration/inherited-06049-06069.tex",
                "handbook/restoration/inherited-06070-06137.tex",
                "handbook/restoration/inherited-06138-06242.tex",
                "handbook/restoration/inherited-06243-06331.tex",
                "handbook/restoration/inherited-06332-06421.tex",
                "handbook/restoration/inherited-06422-06431.tex",
                "handbook/restoration/inherited-06432-06493.tex",
                "handbook/restoration/inherited-06494-06509.tex",
                "handbook/restoration/inherited-06510-06629.tex",
                "handbook/restoration/inherited-06630-06639.tex",
                "handbook/restoration/inherited-06640-06693.tex",
                "handbook/restoration/inherited-06694-06782.tex",
                "handbook/restoration/inherited-06783-06791.tex",
                "handbook/restoration/inherited-06792-06845.tex",
                "handbook/restoration/inherited-06846-06854.tex",
                "handbook/restoration/inherited-06855-06941.tex",
                "handbook/restoration/inherited-06942-07134.tex",
                "handbook/restoration/inherited-07135-07149.tex",
                "handbook/restoration/inherited-07150-07294.tex",
                "handbook/restoration/inherited-07295-07468.tex",
                "handbook/restoration/inherited-07469-07493.tex",
                "handbook/restoration/inherited-07494-07505.tex",
                "handbook/restoration/inherited-07506-07677.tex",
                "handbook/restoration/inherited-07678-07752.tex",
                "handbook/restoration/inherited-07753-07843.tex",
                "handbook/restoration/inherited-07844-07850.tex",
                "handbook/restoration/inherited-07851-08048.tex",
                "handbook/restoration/inherited-08049-08080.tex",
                "handbook/restoration/inherited-08081-08143.tex",
                "handbook/restoration/inherited-08144-08186.tex",
                "handbook/restoration/inherited-08187-08238.tex",
                "handbook/restoration/inherited-08239-08247.tex",
                "handbook/restoration/inherited-08248-08305.tex",
                "handbook/restoration/inherited-08306-08438.tex",
                "handbook/restoration/inherited-08439-08709.tex",
                "handbook/restoration/inherited-08710-08876.tex",
                "handbook/restoration/inherited-08877-08897.tex",
                "handbook/restoration/inherited-08898-09079.tex",
            ):
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(REPO_ROOT / relative, target)
            for provenance_id in EXPECTED_PART5_RESTORATION_IDS:
                suffix = provenance_id.removeprefix("SRC-")
                for relative in (
                    f"spec/provenance/{provenance_id}.json",
                    f"handbook/restoration/scope-{provenance_id}.tex",
                    f"handbook/restoration/inherited-{suffix}.tex",
                ):
                    target = root / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(REPO_ROOT / relative, target)
            for provenance_id in EXPECTED_PART6_RESTORATION_IDS:
                suffix = provenance_id.removeprefix("SRC-")
                for relative in (
                    f"spec/provenance/{provenance_id}.json",
                    f"handbook/restoration/scope-{provenance_id}.tex",
                    f"handbook/restoration/inherited-{suffix}.tex",
                ):
                    target = root / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(REPO_ROOT / relative, target)
            for provenance_id in EXPECTED_PART7_RESTORATION_IDS:
                suffix = provenance_id.removeprefix("SRC-")
                for relative in (
                    f"spec/provenance/{provenance_id}.json",
                    f"handbook/restoration/scope-{provenance_id}.tex",
                    f"handbook/restoration/inherited-{suffix}.tex",
                ):
                    target = root / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(REPO_ROOT / relative, target)
            for provenance_id in EXPECTED_PART8_RESTORATION_IDS:
                suffix = provenance_id.removeprefix("SRC-")
                for relative in (
                    f"spec/provenance/{provenance_id}.json",
                    f"handbook/restoration/scope-{provenance_id}.tex",
                    f"handbook/restoration/inherited-{suffix}.tex",
                ):
                    target = root / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(REPO_ROOT / relative, target)
            for provenance_id in EXPECTED_PART12_RESTORATION_IDS:
                suffix = provenance_id.split("-", 1)[1]
                for relative in (
                    f"spec/provenance/{provenance_id}.json",
                    f"handbook/restoration/scope-{provenance_id}.tex",
                    f"handbook/restoration/inherited-{suffix}.tex",
                ):
                    target = root / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(REPO_ROOT / relative, target)
            for provenance_id in checker.PART2_RESTORATION_IDS:
                suffix = provenance_id.removeprefix("SRC-")
                for relative in (
                    f"spec/provenance/{provenance_id}.json",
                    f"handbook/restoration/scope-{provenance_id}.tex",
                    f"handbook/restoration/inherited-{suffix}.tex",
                ):
                    target = root / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(REPO_ROOT / relative, target)
            for relative in (
                "handbook/parts/p02/propositional-hilbert-tableaux.tex",
                "handbook/parts/p02/propositional-metatheory-supplement.tex",
            ):
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("", encoding="utf-8")
            (root / "handbook/parts/p02.tex").write_text(
                "\\part{Classical Logic}\\label{part:p02}\n"
                "\\input{restoration/scope-SRC-01649-01660}\n"
                "\\input{restoration/scope-SRC-01661-01816}\n"
                "\\input{restoration/scope-SRC-01817-01898}\n"
                "\\input{restoration/scope-SRC-01899-01945}\n"
                "\\input{restoration/scope-SRC-01946-02186}\n"
                "\\input{restoration/scope-SRC-02187-02192}\n"
                "\\input{restoration/scope-SRC-02193-02340}\n"
                "\\input{restoration/scope-SRC-02341-02450}\n"
                "\\input{parts/p02/propositional-hilbert-tableaux}\n"
                "\\input{restoration/scope-SRC-02451-02544}\n"
                "\\input{restoration/scope-SRC-02545-02664}\n"
                "\\input{restoration/scope-SRC-02665-02809}\n"
                "\\input{restoration/scope-SRC-02810-02914}\n"
                "\\input{restoration/scope-SRC-02915-02932}\n"
                "\\input{restoration/scope-SRC-02933-03021}\n"
                "\\input{parts/p02/propositional-metatheory-supplement}\n"
                "\\input{restoration/scope-SRC-03022-03037}\n"
                "\\input{restoration/scope-SRC-03038-03104}\n"
                "\\input{restoration/scope-SRC-03105-03165}\n"
                "\\input{restoration/scope-SRC-03166-03239}\n"
                "\\input{restoration/scope-SRC-03240-03428}\n"
                "\\input{restoration/scope-SRC-03429-03518}\n"
                "\\input{restoration/scope-SRC-03519-03680}\n"
                "\\input{restoration/scope-SRC-03681-03728}\n"
                "\\input{restoration/scope-SRC-03729-03907}\n"
                "\\input{restoration/scope-SRC-03908-03926}\n"
                "\\input{restoration/scope-SRC-03927-04061}\n"
                "\\input{restoration/scope-SRC-04062-04108}\n"
                "\\input{restoration/scope-SRC-04109-04213}\n"
                "\\input{restoration/scope-SRC-04214-04234}\n"
                "\\input{restoration/scope-SRC-04235-04305}\n"
                "\\input{restoration/scope-SRC-04306-04575}\n"
                "\\input{restoration/scope-SRC-04576-04712}\n"
                "\\input{restoration/scope-SRC-04713-04920}\n"
                "\\input{restoration/scope-SRC-04921-04967}\n"
                "\\input{restoration/scope-SRC-04968-05042}\n"
                "\\input{restoration/scope-SRC-05043-05131}\n"
                "\\input{restoration/scope-SRC-05132-05567}\n"
                "\\input{restoration/scope-SRC-05568-05923}\n"
                "\\input{restoration/scope-SRC-05924-05959}\n"
                "\\input{restoration/scope-SRC-05960-06048}\n",
                encoding="utf-8",
            )
            p02_fixture_tail = (
                "parts/p02/first-order-calculi-supplement",
                "parts/p02/first-order-completeness-remainder",
                "parts/p02/first-order-logic",
            )
            p02_higher_supplement = "parts/p02/second-and-higher-order-logic-supplement"
            p02_variants = "parts/p02/variants"
            (root / "handbook/parts/p02").mkdir(parents=True, exist_ok=True)
            for item in (*p02_fixture_tail, p02_higher_supplement, p02_variants):
                (root / f"handbook/{item}.tex").write_text(
                    "% governed Part II fixture\n", encoding="utf-8"
                )
            p02_fixture = root / "handbook/parts/p02.tex"
            p02_fixture.write_text(
                p02_fixture.read_text(encoding="utf-8")
                + "".join(f"\\input{{{item}}}\n" for item in p02_fixture_tail)
                + "".join(
                    f"\\input{{restoration/scope-{item}}}\n"
                    for item in EXPECTED_PART2_HIGHER_ORDER_IDS
                )
                + f"\\input{{{p02_higher_supplement}}}\n"
                + f"\\input{{{p02_variants}}}\n",
                encoding="utf-8",
            )
            for number, title in enumerate(checker.FINAL_PART_TITLES[2:], start=3):
                (root / f"handbook/parts/p{number:02d}.tex").write_text(
                    f"\\part{{{title}}}\\label{{part:p{number:02d}}}\n",
                    encoding="utf-8",
                )
            p03_path = root / "handbook/parts/p03.tex"
            maps_supplement = "parts/p03/maps-elementarity-supplement"
            types_supplement = "parts/p03/types-ultraproducts-supplement"
            qe_supplement = "parts/p03/qe-categoricity-games-supplement"
            (root / "handbook/parts/p03").mkdir(parents=True, exist_ok=True)
            (root / f"handbook/{maps_supplement}.tex").write_text(
                "% governed OPEN maps supplement fixture\n", encoding="utf-8"
            )
            (root / f"handbook/{types_supplement}.tex").write_text(
                "% governed OPEN types supplement fixture\n", encoding="utf-8"
            )
            (root / f"handbook/{qe_supplement}.tex").write_text(
                "% governed OPEN QE supplement fixture\n", encoding="utf-8"
            )
            expected_p03_inputs = (
                EXPECTED_PART3_RESTORATION_IDS[:8]
                + (maps_supplement,)
                + EXPECTED_PART3_RESTORATION_IDS[8:18]
                + (types_supplement,)
                + EXPECTED_PART3_RESTORATION_IDS[18:]
                + (qe_supplement,)
            )
            p03_path.write_text(
                "".join(
                    (
                        f"\\input{{restoration/scope-{value}}}\n"
                        if value.startswith("SRC-")
                        else f"\\input{{{value}}}\n"
                    )
                    for value in expected_p03_inputs
                ),
                encoding="utf-8",
            )
            self.assertEqual(
                checker.PART3_RESTORATION_IDS,
                EXPECTED_PART3_RESTORATION_IDS,
            )
            p04_path = root / "handbook/parts/p04.tex"
            p04_supplement = "parts/p04/machines-effective-procedures-supplement"
            p04_universal_supplement = "parts/p04/universal-reductions-supplement"
            p04_decision_supplement = "parts/p04/decision-hierarchy-apparatus-supplement"
            p04_degrees_continuation = "parts/p04/degrees-and-priority-continuation"
            (root / "handbook/parts/p04").mkdir(parents=True, exist_ok=True)
            (root / f"handbook/{p04_supplement}.tex").write_text(
                "% governed OPEN machines supplement fixture\n", encoding="utf-8"
            )
            (root / f"handbook/{p04_universal_supplement}.tex").write_text(
                "% governed OPEN universal supplement fixture\n", encoding="utf-8"
            )
            (root / f"handbook/{p04_decision_supplement}.tex").write_text(
                "% governed OPEN decision apparatus fixture\n", encoding="utf-8"
            )
            (root / f"handbook/{p04_degrees_continuation}.tex").write_text(
                "% governed OPEN degree continuation fixture\n", encoding="utf-8"
            )
            p04_path.write_text(
                "\\part{Computability and Complexity}\\label{part:p04}\n"
                + "".join(
                    f"\\input{{restoration/scope-{value}}}\n"
                    for value in EXPECTED_PART4_RESTORATION_IDS
                )
                + f"\\input{{{p04_supplement}}}\n"
                + f"\\input{{{p04_universal_supplement}}}\n"
                + f"\\input{{{p04_decision_supplement}}}\n"
                + f"\\input{{{p04_degrees_continuation}}}\n",
                encoding="utf-8",
            )
            self.assertEqual(
                checker.PART4_RESTORATION_IDS,
                EXPECTED_PART4_RESTORATION_IDS,
            )
            p05_path = root / "handbook/parts/p05.tex"
            p05_supplement = "parts/p05/models-and-interpretability-supplement"
            (root / "handbook/parts/p05").mkdir(parents=True, exist_ok=True)
            (root / f"handbook/{p05_supplement}.tex").write_text(
                "% governed OPEN Part V supplement fixture\n", encoding="utf-8"
            )
            expected_p05_inputs = (
                EXPECTED_PART5_RESTORATION_IDS[:8]
                + (p05_supplement,)
                + EXPECTED_PART5_RESTORATION_IDS[8:]
            )
            p05_path.write_text(
                "".join(
                    (
                        f"\\input{{restoration/scope-{value}}}\n"
                        if value.startswith("SRC-")
                        else f"\\input{{{value}}}\n"
                    )
                    for value in expected_p05_inputs
                ),
                encoding="utf-8",
            )
            self.assertEqual(
                checker.PART5_RESTORATION_IDS,
                EXPECTED_PART5_RESTORATION_IDS,
            )
            p06_path = root / "handbook/parts/p06.tex"
            p06_table = "parts/p06/zfc-axiom-table-supplement"
            p06_ordinal = "parts/p06/ordinal-rank-supplement"
            p06_choice = "parts/p06/cardinals-choice-supplement"
            p06_vocabulary = "parts/p06/forcing-vocabulary"
            p06_constructibility = "parts/p06/constructibility-forcing-supplement"
            p06_variants = "parts/p06/forcing-variants-supplement"
            p06_arithmetic = "parts/p06/cardinal-arithmetic-supplement"
            p06_later = (
                "parts/p06/infinitary-combinatorics",
                p06_arithmetic,
                "parts/p06/large-cardinals-absoluteness",
                "parts/p06/descriptive-set-theory",
                "parts/p06/determinacy",
            )
            (root / "handbook/parts/p06").mkdir(parents=True, exist_ok=True)
            for item in (
                p06_table,
                p06_ordinal,
                p06_choice,
                p06_vocabulary,
                p06_constructibility,
                p06_variants,
                *p06_later,
            ):
                (root / f"handbook/{item}.tex").write_text(
                    "% governed OPEN Part VI fixture\n", encoding="utf-8"
                )
            expected_p06_inputs = (
                EXPECTED_PART6_RESTORATION_IDS[:2]
                + (p06_table,)
                + EXPECTED_PART6_RESTORATION_IDS[2:7]
                + (p06_ordinal, p06_choice)
                + EXPECTED_PART6_RESTORATION_IDS[7:]
                + (p06_vocabulary, p06_constructibility, p06_variants)
                + p06_later
            )
            p06_path.write_text(
                "".join(
                    (
                        f"\\input{{restoration/scope-{value}}}\n"
                        if value.startswith("SRC-")
                        else f"\\input{{{value}}}\n"
                    )
                    for value in expected_p06_inputs
                ),
                encoding="utf-8",
            )
            self.assertEqual(
                checker.PART6_RESTORATION_IDS,
                EXPECTED_PART6_RESTORATION_IDS,
            )
            p07_path = root / "handbook/parts/p07.tex"
            p07_calculus = "parts/p07/calculi-and-derivability-supplement"
            p07_cut = "parts/p07/cut-elimination-and-interpolation-supplement"
            p07_normalization = "parts/p07/normalization-and-curry-howard-supplement"
            p07_arithmetic = "parts/p07/arithmetic-proof-theory-supplement"
            p07_later = (
                "parts/p07/lambda-calculi-and-type-theories",
                p07_arithmetic,
                "parts/p07/functional-interpretations",
                "parts/p07/structural-extensions",
                "parts/p07/proof-complexity",
            )
            (root / "handbook/parts/p07").mkdir(parents=True, exist_ok=True)
            for item in (p07_calculus, p07_cut, p07_normalization, *p07_later):
                (root / f"handbook/{item}.tex").write_text(
                    "% governed OPEN Part VII fixture\n", encoding="utf-8"
                )
            expected_p07_inputs = (
                EXPECTED_PART7_RESTORATION_IDS[:8]
                + (p07_calculus,)
                + EXPECTED_PART7_RESTORATION_IDS[8:14]
                + (p07_cut,)
                + EXPECTED_PART7_RESTORATION_IDS[14:]
                + (p07_normalization,)
                + p07_later
            )
            p07_path.write_text(
                "\\part{Proof Theory, Lambda Calculi, and Higher-Order Logic}"
                "\\label{part:p07}\n"
                + "".join(
                    (
                        f"\\input{{restoration/scope-{value}}}\n"
                        if value.startswith("SRC-")
                        else f"\\input{{{value}}}\n"
                    )
                    for value in expected_p07_inputs
                ),
                encoding="utf-8",
            )
            self.assertEqual(
                checker.PART7_RESTORATION_IDS,
                EXPECTED_PART7_RESTORATION_IDS,
            )
            p08_path = root / "handbook/parts/p08.tex"
            p08_supplement = "parts/p08/intuitionistic-supplement"
            p08_modal_supplement = "parts/p08/modal-logics-supplement"
            p08_temporal_supplement = "parts/p08/temporal-epistemic-supplement"
            p08_many_supplement = "parts/p08/many-valued-supplement"
            p08_relevance_supplement = "parts/p08/relevance-linear-supplement"
            p08_later = (
                "parts/p08/conditionals-deontic-free",
                "parts/p08/paraconsistent-and-nonmonotonic",
                "parts/p08/further-reading",
            )
            (root / "handbook/parts/p08").mkdir(parents=True, exist_ok=True)
            for item in (
                p08_supplement,
                p08_modal_supplement,
                p08_temporal_supplement,
                p08_many_supplement,
                p08_relevance_supplement,
                *p08_later,
            ):
                (root / f"handbook/{item}.tex").write_text(
                    "% governed OPEN Part VIII fixture\n", encoding="utf-8"
                )
            p08_path.write_text(
                "".join(
                    f"\\input{{restoration/scope-{value}}}\n"
                    for value in EXPECTED_PART8_RESTORATION_IDS[:9]
                )
                + f"\\input{{{p08_supplement}}}\n"
                + "".join(
                    f"\\input{{restoration/scope-{value}}}\n"
                    for value in EXPECTED_PART8_RESTORATION_IDS[9:22]
                )
                + f"\\input{{{p08_modal_supplement}}}\n"
                + f"\\input{{{p08_temporal_supplement}}}\n"
                + f"\\input{{{p08_later[0]}}}\n"
                + "".join(
                    f"\\input{{restoration/scope-{value}}}\n"
                    for value in EXPECTED_PART8_RESTORATION_IDS[22:28]
                )
                + f"\\input{{{p08_many_supplement}}}\n"
                + "".join(
                    f"\\input{{restoration/scope-{value}}}\n"
                    for value in EXPECTED_PART8_RESTORATION_IDS[28:]
                )
                + f"\\input{{{p08_relevance_supplement}}}\n"
                + "".join(f"\\input{{{item}}}\n" for item in p08_later[1:]),
                encoding="utf-8",
            )
            self.assertEqual(
                checker.PART8_RESTORATION_IDS,
                EXPECTED_PART8_RESTORATION_IDS,
            )
            exact_p04 = p04_path.read_text(encoding="utf-8")
            exact_p03 = p03_path.read_text(encoding="utf-8")
            exact_p05 = p05_path.read_text(encoding="utf-8")
            exact_p06 = p06_path.read_text(encoding="utf-8")
            exact_p07 = p07_path.read_text(encoding="utf-8")
            exact_p08 = p08_path.read_text(encoding="utf-8")
            p12_path = root / "handbook/parts/p12.tex"
            p12_supplement = "parts/p12/formal-practice-supplement"
            p12_aggregator = "parts/p12/automation-and-mechanization"
            (root / "handbook/parts/p12").mkdir(parents=True, exist_ok=True)
            for item in (p12_supplement, p12_aggregator):
                (root / f"handbook/{item}.tex").write_text(
                    "% governed OPEN Part XII fixture\n", encoding="utf-8"
                )
            p12_path.write_text(
                "\\part{Automation, Mechanization, and Formal Practice}"
                "\\label{part:p12}\n"
                + "".join(
                    f"\\input{{restoration/scope-{value}}}\n"
                    for value in EXPECTED_PART12_RESTORATION_IDS[:5]
                )
                + f"\\input{{{p12_supplement}}}\n"
                + "".join(
                    f"\\input{{restoration/scope-{value}}}\n"
                    for value in EXPECTED_PART12_RESTORATION_IDS[5:]
                )
                + f"\\input{{{p12_aggregator}}}\n",
                encoding="utf-8",
            )
            exact_p12 = p12_path.read_text(encoding="utf-8")
            self.assertEqual(checker.validate_book_sources(root), [])

            p05_path.write_text(
                exact_p05.replace(
                    "\\input{restoration/scope-SRC-09112-09149}\n"
                    "\\input{restoration/scope-SRC-09150-09174}\n",
                    "\\input{restoration/scope-SRC-09150-09174}\n"
                    "\\input{restoration/scope-SRC-09112-09149}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("nineteen-wrapper order" in failure for failure in failures), failures)

            p05_path.write_text(
                exact_p05.replace(f"\\input{{{p05_supplement}}}\n", ""),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("supplement seam" in failure for failure in failures), failures)

            p05_path.write_text(
                exact_p05
                + "\\input{restoration/inherited-09112-09149}\n",
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("p05 raw inherited input" in failure for failure in failures), failures)

            p05_path.write_text(
                "\\part{Arithmetic and Incompleteness}\\label{part:p05}\n"
                + exact_p05,
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("p05 must classify" in failure for failure in failures), failures)
            p05_path.write_text(exact_p05, encoding="utf-8")

            p06_path.write_text(
                exact_p06.replace(
                    "\\input{restoration/scope-SRC-10452-10520}\n"
                    "\\input{restoration/scope-SRC-10521-10558}\n",
                    "\\input{restoration/scope-SRC-10521-10558}\n"
                    "\\input{restoration/scope-SRC-10452-10520}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("twenty-three-wrapper order" in failure for failure in failures), failures)

            p06_path.write_text(
                exact_p06.replace(f"\\input{{{p06_ordinal}}}\n", ""),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("addition seams" in failure for failure in failures), failures)

            p06_path.write_text(
                exact_p06 + "\\input{restoration/inherited-10452-10520}\n",
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("p06 raw inherited input" in failure for failure in failures), failures)

            p06_path.write_text(exact_p06, encoding="utf-8")

            p07_path.write_text(
                exact_p07.replace(
                    "\\input{restoration/scope-SRC-11741-11767}\n"
                    "\\input{restoration/scope-SRC-11768-11823}\n",
                    "\\input{restoration/scope-SRC-11768-11823}\n"
                    "\\input{restoration/scope-SRC-11741-11767}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("nineteen-wrapper order" in failure for failure in failures), failures)

            p07_path.write_text(
                exact_p07.replace(f"\\input{{{p07_calculus}}}\n", ""),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("addition seams" in failure for failure in failures), failures)

            p07_path.write_text(
                exact_p07 + "\\input{restoration/inherited-11741-11767}\n",
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("p07 raw inherited input" in failure for failure in failures), failures)

            p07_path.write_text(
                exact_p07 + "\\label{part:proof-theory}\n",
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("p07 must classify" in failure for failure in failures), failures)
            p07_path.write_text(exact_p07, encoding="utf-8")

            p08_path.write_text(
                exact_p08.replace(
                    "\\input{restoration/scope-SRC-12970-12988}\n"
                    "\\input{restoration/scope-SRC-12989-13045}\n",
                    "\\input{restoration/scope-SRC-12989-13045}\n"
                    "\\input{restoration/scope-SRC-12970-12988}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("forty-wrapper order" in failure for failure in failures), failures)

            p08_path.write_text(
                exact_p08.replace(f"\\input{{{p08_supplement}}}\n", ""),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("addition seams" in failure for failure in failures), failures)

            p08_path.write_text(
                exact_p08.replace(f"\\input{{{p08_many_supplement}}}\n", ""),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("addition seams" in failure for failure in failures), failures)

            p08_path.write_text(
                exact_p08.replace(f"\\input{{{p08_relevance_supplement}}}\n", ""),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("addition seams" in failure for failure in failures), failures)

            p08_path.write_text(
                exact_p08.replace(f"\\input{{{p08_modal_supplement}}}\n", ""),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("addition seams" in failure for failure in failures), failures)

            p08_path.write_text(
                exact_p08.replace(f"\\input{{{p08_temporal_supplement}}}\n", ""),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("addition seams" in failure for failure in failures), failures)

            p08_path.write_text(
                exact_p08 + "\\input{restoration/inherited-12989-13045}\n",
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("p08 raw inherited input" in failure for failure in failures), failures)

            p08_path.write_text(
                "\\part{Nonclassical Logics}\\label{part:p08}\n" + exact_p08,
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("p08 must classify" in failure for failure in failures), failures)
            p08_path.write_text(exact_p08, encoding="utf-8")

            p12_path.write_text(
                exact_p12.replace(
                    "\\input{restoration/scope-SRC-14095-14146}\n"
                    "\\input{restoration/scope-SRC-14147-14169}\n",
                    "\\input{restoration/scope-SRC-14147-14169}\n"
                    "\\input{restoration/scope-SRC-14095-14146}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("thirty-nine-wrapper order" in failure for failure in failures), failures)

            p12_path.write_text(
                exact_p12.replace(
                    "\\input{restoration/scope-SRC-15240-15488}\n", ""
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(
                any("thirty-nine-wrapper order" in failure for failure in failures),
                failures,
            )

            p12_path.write_text(
                exact_p12.replace(
                    "\\input{restoration/scope-SRC-15489-15619}\n", ""
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(
                any("thirty-nine-wrapper order" in failure for failure in failures),
                failures,
            )

            p12_path.write_text(
                exact_p12.replace(
                    "\\input{restoration/scope-SRC-15620-15637}\n", ""
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(
                any("thirty-nine-wrapper order" in failure for failure in failures),
                failures,
            )

            p12_path.write_text(
                exact_p12.replace(
                    "\\input{restoration/scope-SRC-15638-16742}\n", ""
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(
                any("thirty-nine-wrapper order" in failure for failure in failures),
                failures,
            )

            p12_path.write_text(
                exact_p12.replace(f"\\input{{{p12_supplement}}}\n", ""),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("addition seam" in failure for failure in failures), failures)

            p12_path.write_text(
                exact_p12 + "\\input{restoration/inherited-14147-14169}\n",
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("p12 raw inherited input" in failure for failure in failures), failures)

            historical = root / "handbook/parts/p12/formal-workflow.tex"
            historical.write_text("% retired historical workflow\n", encoding="utf-8")
            p12_path.write_text(
                exact_p12 + "\\input{parts/p12/formal-workflow}\n",
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("p12 must classify" in failure for failure in failures), failures)

            audit = root / "handbook/generated/audit-p12.tex"
            audit.parent.mkdir(parents=True, exist_ok=True)
            audit.write_text("% stale audit fixture\n", encoding="utf-8")
            p12_path.write_text(
                exact_p12 + "\\input{generated/audit-p12}\n",
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("p12 must classify" in failure for failure in failures), failures)
            p12_path.write_text(exact_p12, encoding="utf-8")

            p02_path = root / "handbook/parts/p02.tex"
            exact_p02 = p02_path.read_text(encoding="utf-8")
            p02_path.write_text(
                exact_p02 + "\\part{Arbitrary extra part}\n", encoding="utf-8"
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("p02 must classify" in failure for failure in failures), failures)

            p02_path.write_text(
                exact_p02.replace(
                    "\\input{restoration/scope-SRC-01649-01660}\n"
                    "\\input{restoration/scope-SRC-01661-01816}\n",
                    "\\input{restoration/scope-SRC-01661-01816}\n"
                    "\\input{restoration/scope-SRC-01649-01660}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("fifty-wrapper order" in failure for failure in failures), failures)

            p02_path.write_text(
                exact_p02.replace(
                    "\\input{restoration/scope-SRC-04713-04920}\n"
                    "\\input{restoration/scope-SRC-04921-04967}\n",
                    "\\input{restoration/scope-SRC-04921-04967}\n"
                    "\\input{restoration/scope-SRC-04713-04920}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("fifty-wrapper order" in failure for failure in failures), failures)

            p02_path.write_text(
                exact_p02.replace(
                    "\\input{restoration/scope-SRC-02915-02932}\n"
                    "\\input{restoration/scope-SRC-02933-03021}\n",
                    "\\input{restoration/scope-SRC-02933-03021}\n"
                    "\\input{restoration/scope-SRC-02915-02932}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("fifty-wrapper order" in failure for failure in failures), failures)

            p02_path.write_text(
                exact_p02.replace(
                    "\\input{restoration/scope-SRC-03166-03239}\n"
                    "\\input{restoration/scope-SRC-03240-03428}\n",
                    "\\input{restoration/scope-SRC-03240-03428}\n"
                    "\\input{restoration/scope-SRC-03166-03239}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("fifty-wrapper order" in failure for failure in failures), failures)

            p02_path.write_text(
                exact_p02.replace(
                    "\\input{restoration/scope-SRC-03519-03680}\n"
                    "\\input{restoration/scope-SRC-03681-03728}\n",
                    "\\input{restoration/scope-SRC-03681-03728}\n"
                    "\\input{restoration/scope-SRC-03519-03680}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("fifty-wrapper order" in failure for failure in failures), failures)

            p02_path.write_text(
                exact_p02.replace(
                    "\\input{restoration/scope-SRC-03729-03907}\n"
                    "\\input{restoration/scope-SRC-03908-03926}\n",
                    "\\input{restoration/scope-SRC-03908-03926}\n"
                    "\\input{restoration/scope-SRC-03729-03907}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("fifty-wrapper order" in failure for failure in failures), failures)

            p02_path.write_text(
                exact_p02.replace(
                    "\\input{restoration/scope-SRC-04214-04234}\n"
                    "\\input{restoration/scope-SRC-04235-04305}\n",
                    "\\input{restoration/scope-SRC-04235-04305}\n"
                    "\\input{restoration/scope-SRC-04214-04234}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("fifty-wrapper order" in failure for failure in failures), failures)

            p02_path.write_text(
                exact_p02.replace(
                    "\\input{restoration/scope-SRC-05924-05959}\n"
                    "\\input{restoration/scope-SRC-05960-06048}\n",
                    "\\input{restoration/scope-SRC-05960-06048}\n"
                    "\\input{restoration/scope-SRC-05924-05959}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("fifty-wrapper order" in failure for failure in failures), failures)

            p02_path.write_text(
                exact_p02.replace(
                    "\\input{restoration/scope-SRC-02933-03021}\n", ""
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("fifty-wrapper order" in failure for failure in failures), failures)

            p02_path.write_text(
                exact_p02 + "\\input{restoration/scope-SRC-02933-03021}\n",
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("fifty-wrapper order" in failure for failure in failures), failures)

            p02_path.write_text(
                exact_p02.replace(
                    "\\input{restoration/scope-SRC-01649-01660}",
                    "\\input{restoration/inherited-01649-01660}",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("titles, labels, routes" in failure for failure in failures), failures)

            p02_path.write_text(
                exact_p02.replace(
                    "\\input{restoration/scope-SRC-12249-12261}\n"
                    "\\input{restoration/scope-SRC-12262-12289}\n",
                    "\\input{restoration/scope-SRC-12262-12289}\n"
                    "\\input{restoration/scope-SRC-12249-12261}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("fifty-wrapper order" in failure for failure in failures), failures)

            p02_path.write_text(
                exact_p02.replace(f"\\input{{{p02_higher_supplement}}}\n", ""),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("higher-order supplement seam" in failure for failure in failures), failures)

            p02_path.write_text(
                exact_p02 + "\\label{part:higher-order}\n",
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("titles, labels, routes" in failure for failure in failures), failures)
            p02_path.write_text(exact_p02, encoding="utf-8")

            p03_path.write_text(
                exact_p03.replace(
                    "\\input{restoration/scope-SRC-06049-06069}\n"
                    "\\input{restoration/scope-SRC-06070-06137}\n",
                    "\\input{restoration/scope-SRC-06070-06137}\n"
                    "\\input{restoration/scope-SRC-06049-06069}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("twenty-one-wrapper order" in failure for failure in failures), failures)

            p03_path.write_text(
                exact_p03.replace(
                    "\\input{restoration/scope-SRC-07469-07493}\n", ""
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("twenty-one-wrapper order" in failure for failure in failures), failures)

            p03_path.write_text(
                exact_p03 + "\\input{restoration/scope-SRC-07469-07493}\n",
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("twenty-one-wrapper order" in failure for failure in failures), failures)

            p03_path.write_text(
                exact_p03.replace(f"\\input{{{maps_supplement}}}\n", "")
                + f"\\input{{{maps_supplement}}}\n",
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("governed supplement seams" in failure for failure in failures), failures)

            p03_path.write_text(
                exact_p03.replace(f"\\input{{{qe_supplement}}}\n", "")
                .replace(
                    "\\input{restoration/scope-SRC-07150-07294}\n",
                    f"\\input{{{qe_supplement}}}\n"
                    "\\input{restoration/scope-SRC-07150-07294}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("governed supplement seams" in failure for failure in failures), failures)

            p03_path.write_text(
                exact_p03.replace(f"\\input{{{types_supplement}}}\n", "")
                .replace(
                    "\\input{restoration/scope-SRC-06510-06629}\n",
                    f"\\input{{{types_supplement}}}\n"
                    "\\input{restoration/scope-SRC-06510-06629}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("governed supplement seams" in failure for failure in failures), failures)

            for injected in (
                "\\part{Model Theory}\n",
                "\\label{part:model-theory}\n",
                "\\part{Arbitrary extra part}\n",
            ):
                with self.subTest(p03_injected=injected):
                    p03_path.write_text(injected + exact_p03, encoding="utf-8")
                    failures = checker.validate_book_sources(root)
                    self.assertTrue(any("p03 must classify" in failure for failure in failures), failures)
            p03_path.write_text(exact_p03, encoding="utf-8")

            p03_artifact = root / "handbook/restoration/inherited-06049-06069.tex"
            exact_p03_artifact = p03_artifact.read_text(encoding="utf-8")
            p03_artifact.write_text(
                exact_p03_artifact.replace(
                    "\\part{Model Theory}", "\\part{Wrong Model Theory}"
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("p03" in failure for failure in failures), failures)
            p03_artifact.write_text(exact_p03_artifact, encoding="utf-8")

            p04_path.write_text(
                exact_p04.replace(
                    "\\input{restoration/scope-SRC-07494-07505}\n"
                    "\\input{restoration/scope-SRC-07506-07677}\n",
                    "\\input{restoration/scope-SRC-07506-07677}\n"
                    "\\input{restoration/scope-SRC-07494-07505}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("seventeen-wrapper order" in failure for failure in failures), failures)

            p04_path.write_text(
                exact_p04.replace(
                    "\\input{restoration/scope-SRC-07844-07850}\n", ""
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("seventeen-wrapper order" in failure for failure in failures), failures)

            p04_path.write_text(
                exact_p04 + "\\input{restoration/scope-SRC-07844-07850}\n",
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("seventeen-wrapper order" in failure for failure in failures), failures)

            p04_path.write_text(
                exact_p04.replace(f"\\input{{{p04_supplement}}}\n", "")
                .replace(
                    "\\input{restoration/scope-SRC-07494-07505}\n",
                    f"\\input{{{p04_supplement}}}\n"
                    "\\input{restoration/scope-SRC-07494-07505}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("governed supplement seam" in failure for failure in failures), failures)

            for supplemental in (
                p04_decision_supplement,
                p04_degrees_continuation,
            ):
                with self.subTest(p04_supplemental=supplemental):
                    p04_path.write_text(
                        exact_p04.replace(
                            f"\\input{{{supplemental}}}\n", ""
                        )
                        + f"\\input{{{supplemental}}}\n",
                        encoding="utf-8",
                    )
                    failures = checker.validate_book_sources(root)
                    self.assertTrue(
                        any("governed supplement seam" in failure for failure in failures),
                        failures,
                    )

            p04_path.write_text(
                exact_p04.replace(
                    f"\\input{{{p04_universal_supplement}}}\n", ""
                ).replace(
                    f"\\input{{{p04_supplement}}}\n",
                    f"\\input{{{p04_universal_supplement}}}\n"
                    f"\\input{{{p04_supplement}}}\n",
                ),
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("governed supplement seam" in failure for failure in failures), failures)

            p04_path.write_text(
                exact_p04
                + "\\input{restoration/inherited-07506-07677}\n",
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("raw inherited input" in failure for failure in failures), failures)

            for injected in (
                "\\part{Computability}\n",
                "\\label{part:computability}\n",
                "\\part{Arbitrary extra part}\n",
            ):
                with self.subTest(p04_injected=injected):
                    p04_path.write_text(injected + exact_p04, encoding="utf-8")
                    failures = checker.validate_book_sources(root)
                    self.assertTrue(any("p04 must classify" in failure for failure in failures), failures)
            p04_path.write_text(exact_p04, encoding="utf-8")

            (root / "handbook/parts/p01.tex").write_text(
                "\\input{restoration/scope-SRC-00363-00372}\n"
                "\\part{Foundations of Formal Work}\\label{part:p01-copy}\n",
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("p01" in failure for failure in failures), failures)

            (root / "handbook/parts/p01.tex").write_text(
                "\\input{restoration/scope-SRC-00363-00372}\n",
                encoding="utf-8",
            )
            (root / "handbook/parts/p02.tex").write_text(
                "\\part{Classical Logic}\n",
                encoding="utf-8",
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("p02" in failure for failure in failures), failures)

            (root / "handbook/parts/p06.tex").write_text(
                "\\part{Set Theory}\\label{part:p06}\n", encoding="utf-8"
            )
            failures = checker.validate_book_sources(root)
            self.assertTrue(any("p06" in failure for failure in failures), failures)

    def test_part2_source_part_cannot_be_generically_ignored(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "handbook/parts").mkdir(parents=True)
            (root / "handbook/restoration").mkdir(parents=True)
            (root / "handbook/main.tex").write_text(
                "\\hypersetup{pdftitle={The Methods of Reason}}\n"
                + "".join(f"\\input{{parts/p{n:02d}}}\n" for n in range(1, 15)),
                encoding="utf-8",
            )
            (root / "handbook/publication-title.tex").write_text(
                "The Methods of Reason\n", encoding="utf-8"
            )
            (root / "handbook/parts/p01.tex").write_text(
                "\\part{Foundations of Formal Work}\\label{part:p01}\n",
                encoding="utf-8",
            )
            for number, title in enumerate(checker.FINAL_PART_TITLES[1:], start=2):
                (root / f"handbook/parts/p{number:02d}.tex").write_text(
                    f"\\part{{{title}}}\\label{{part:p{number:02d}}}\n",
                    encoding="utf-8",
                )
            (root / "handbook/parts/p02-extra.tex").write_text(
                "\\part{Arbitrary suppressed content}\n", encoding="utf-8"
            )
            with (root / "handbook/parts/p02.tex").open("a", encoding="utf-8") as handle:
                handle.write("\\input{parts/p02-extra}\n")

            failures = checker.validate_book_sources(root)
            self.assertTrue(any("p02" in failure for failure in failures), failures)


if __name__ == "__main__":
    unittest.main()

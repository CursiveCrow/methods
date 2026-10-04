#!/usr/bin/env python3
"""Report exact bounded-memory statistics for the acquisition baseline.

This administrative reporter deliberately delegates record classification to
the coverage-manifest parser.  A second, approximate bullet classifier would
create a redundant content decision and could disagree about what constitutes
a source topic.
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path

from build_coverage_manifest import (
    DEFAULT_INPUT,
    MAPPING_STATUS,
    iter_manifest_records,
    sha256_file,
    streamed_retrieval_date,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    args = parser.parse_args()

    date = streamed_retrieval_date(args.input)
    counts: Counter[str] = Counter()
    https_urls: set[str] = set()
    non_https_urls: set[str] = set()
    scheme_less_identifiers: set[str] = set()
    for record in iter_manifest_records(args.input, date):
        if record.mapping_status != MAPPING_STATUS:
            raise ValueError(
                f"{record.stable_id}: unexpected mapping status "
                f"{record.mapping_status!r}"
            )
        counts[record.record_type] += 1
        if record.record_type == "source":
            https_urls.update(record.source_https_urls)
            non_https_urls.update(record.source_non_https_urls)
            scheme_less_identifiers.update(record.source_scheme_less_identifiers)
    rows = sum(counts.values())
    print(
        json.dumps(
            {
                "sha256": sha256_file(args.input),
                "sources": counts["source"],
                "hierarchy": counts["hierarchy"],
                "topics": counts["topic"],
                "rows": rows,
                "unique_https": len(https_urls),
                "unique_non_https": len(non_https_urls),
                "unique_scheme_less": len(scheme_less_identifiers),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

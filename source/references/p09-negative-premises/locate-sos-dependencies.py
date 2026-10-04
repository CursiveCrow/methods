"""Locate selected primary sections; no manuscript or prose tests."""
from pathlib import Path
import sys
from pypdf import PdfReader
sys.stdout.reconfigure(encoding="utf-8")
root = Path(__file__).parent
for name in sys.argv[1:]:
    reader = PdfReader(root / name)
    print(name, "physical extent", len(reader.pages))
    for number, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        if any(word in text.lower() for word in ("source-depend", "conservativity theorem", "gsos rule", "congruence")):
            print("PHYSICAL", number, text[:60].replace("\n", " "))

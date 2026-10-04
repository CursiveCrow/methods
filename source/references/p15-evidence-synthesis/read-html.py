"""Inspect the captured primary HTML without changing it."""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

class Reader(HTMLParser):
    def __init__(self):
        super().__init__()
        self.chunks = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.skip += 1
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "tr"}:
            self.chunks.append("\n")
        if tag == "img":
            a = dict(attrs)
            self.chunks.append(" [IMAGE " + (a.get("alt") or "") + " " + (a.get("src") or "") + "] ")
    def handle_endtag(self, tag):
        if tag in {"script", "style"}:
            self.skip -= 1
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "tr"}:
            self.chunks.append("\n")
    def handle_data(self, data):
        if not self.skip:
            self.chunks.append(data)

r = Reader()
r.feed(Path(__file__).with_name("cochrane-ch10-v6.5-2024-11.html").read_text(encoding="utf-8"))
text = re.sub(r"[ \t\r\f\v]+", " ", "".join(r.chunks))
text = re.sub(r"\n\s*\n+", "\n", text)
text = text[text.index("Cite this chapter as:"):]
sections = re.split(r"\n(?=10\.\d+ )", text)
lo, hi = map(int, sys.argv[1:3])
for section in sections:
    m = re.match(r"10\.(\d+) ", section)
    if m and lo <= int(m.group(1)) <= hi:
        print(section)

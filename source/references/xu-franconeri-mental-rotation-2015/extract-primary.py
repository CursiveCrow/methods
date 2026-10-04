from html.parser import HTMLParser
from pathlib import Path


class PrimaryArticle(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.article_depth = 0
        self.text = []
        self.images = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "article":
            self.article_depth += 1
        if not self.article_depth:
            return
        if tag in {"p", "h1", "h2", "h3", "h4", "li", "figcaption", "tr"}:
            self.text.append("\n")
        if tag == "img":
            self.images.append(attributes)
        if tag == "a":
            self.links.append(attributes.get("href", ""))

    def handle_endtag(self, tag):
        if self.article_depth and tag in {"p", "h1", "h2", "h3", "h4", "li", "figcaption", "tr"}:
            self.text.append("\n")
        if tag == "article":
            self.article_depth -= 1

    def handle_data(self, data):
        if self.article_depth:
            self.text.append(data)


parser = PrimaryArticle()
parser.feed(Path(__file__).with_name("pmc-source.html").read_text(encoding="utf-8"))
lines = [" ".join(line.split()) for line in "".join(parser.text).splitlines()]
print("\n".join(line for line in lines if line))
print("\nFIGURE FILE REFERENCES")
for item in parser.images:
    print(item)
print("\nSUPPLEMENT AND PDF LINKS")
for link in parser.links:
    if any(term in link.lower() for term in ("supp", ".pdf", "bin/", "attachment")):
        print(link)

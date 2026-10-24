"""Regression tests for Habo's ten consistent landing pages and archive growth."""
import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE="https://skaraborgmaskin.se/"
SOURCES=["data/habo-services-part1.json","data/habo-services-part2.json"]

class Inspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags=[]
        self.hrefs=[]
        self.ids=[]
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        self.tags.append((tag,attrs))
        if "href" in attrs:self.hrefs.append(attrs["href"])
        if "id" in attrs:self.ids.append(attrs["id"])

class LandingPages(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records=sum((json.loads((ROOT/p).read_text(encoding="utf-8")) for p in SOURCES),[])
        cls.slugs=[r["slug"] for r in cls.records]

    def test_all_ten_use_shared_design_and_have_valid_links(self):
        self.assertEqual(len(self.records),10)
        self.assertEqual(len(set(self.slugs)),10)
        self.assertTrue((ROOT/"habo-service.css").is_file())
        for record in self.records:
            slug=record["slug"]
            with self.subTest(slug=slug):
                html=(ROOT/(slug+".html")).read_text(encoding="utf-8")
                parser=Inspector()
                parser.feed(html)
                self.assertEqual(sum(tag=="h1" for tag,_ in parser.tags),1)
                self.assertIn('href="/habo-service.css"',html)
                self.assertIn('rel="canonical" href="'+BASE+slug+'.html"',html)
                self.assertIn('name="robots" content="index,follow',html)
                self.assertIn('href="/habo.html"',html)
                self.assertIn("partials1/header.html",html)
                self.assertIn("partials1/footer.html",html)
                self.assertIn("Jönköpings",html)
                self.assertEqual(len([t for t in parser.tags if t[0]=="details"]),3)
                self.assertEqual(len([t for t in parser.tags if t[0]=="article"]),3)
                self.assertEqual(len(parser.ids),len(set(parser.ids)))
                self.assertNotIn("924620407412160",html)
                self.assertNotIn("{{",html)
                for link in parser.hrefs:
                    if not link.startswith("/") or link.startswith("//"):
                        continue
                    path=link.split("#",1)[0].split("?",1)[0].lstrip("/")
                    if path:self.assertTrue((ROOT/path).exists(),slug+" missing "+path)

    def test_archive_is_scalable_and_truthful(self):
        html=(ROOT/"maskinarkivet.html").read_text(encoding="utf-8")
        self.assertIn("Under uppbyggnad",html)
        self.assertIn('id="model-search"',html)
        self.assertIn('id="type-filter"',html)
        self.assertIn('id="more-models"',html)
        self.assertIn("visibleLimit=4",html)
        self.assertIn("visibleLimit+=4",html)
        self.assertIn('data-category="akgrasklippare"',html)
        self.assertEqual(len(re.findall(r'<article class="machine"\s',html)),6)
        for term in ("grasklippare","motorsagar","motorer","redskap"):
            self.assertIn(term,html)
        self.assertIn(".machine[hidden]{display:none",html)
        self.assertIn('aria-live="polite"',html)
        self.assertEqual(len(re.findall(r'<h1\b',html)),1)

if __name__=="__main__":unittest.main()

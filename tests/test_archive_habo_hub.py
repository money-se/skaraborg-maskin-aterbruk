"""Kontrollera att Habo-satsningen och Maskinarkivets nav fungerar ihop."""
from pathlib import Path
from html.parser import HTMLParser
import re
import unittest
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
BASE="https://skaraborgmaskin.se/"
HABO_SERVICES=[
 "salja-maskin-habo.html",
 "salja-grasklippare-habo.html",
 "salja-akgrasklippare-habo.html",
 "dodsbo-utrensning-habo.html",
 "skrot-hamtning-habo.html",
 "aterbruk-habo.html",
 "verkstad-maskiner-habo.html",
 "dack-hamtning-habo.html",
 "gratis-aterbrukshamtning-habo.html",
 "skank-maskin-manadens-maskin-habo.html",
]
MACHINES=["stiga-villa-12-hst","husqvarna-rider-13","husqvarna-lth151","stiga-park-16","jonsered-lt2115","stiga-park-2000"]

def content(path):
    return (ROOT/path).read_text(encoding="utf-8")

def sitemap():
    tree=ET.parse(ROOT/"sitemap.xml")
    return [n.text for n in tree.iter() if n.tag.endswith("}loc") or n.tag=="loc"]

class SitemapTests(unittest.TestCase):
    def test_habo_complete_and_unique(self):
        urls=sitemap()
        for path in ["habo.html",*HABO_SERVICES]:
            with self.subTest(path=path):
                self.assertTrue((ROOT/path).is_file())
                self.assertEqual(urls.count(BASE+path),1)
                html=content(path)
                self.assertEqual(len(re.findall(r'<h1\b',html,re.I)),1)
                self.assertIn("name=\"robots\" content=\"index,follow",html)
                self.assertIn(BASE+path,html)

    def test_habo_hub_links_all_services_and_shared_menu(self):
        html=content("habo.html")
        for path in HABO_SERVICES:
            self.assertIn('href="'+path+'"',html)
        self.assertIn('inject("site-header"',html)
        self.assertIn('inject("site-footer"',html)
        self.assertIn("Jönköpings län",html)
        self.assertNotIn("Habo ligger i Skaraborg",html)
        self.assertIn('href="habo.html"',content("kop-maskiner.html"))
        self.assertIn('href="habo.html"',content("partials1/footer.html"))

    def test_old_habo_service_pages_link_to_hub(self):
        for path in HABO_SERVICES[:7]:
            with self.subTest(path=path):
                self.assertIn('href="/habo.html"',content(path))
                self.assertNotIn('924620407412160',content(path))

    def test_archive_index_links_only_existing_articles(self):
        html=content("maskinarkivet.html")
        self.assertEqual(len(re.findall(r'<h1\b',html,re.I)),1)
        self.assertIn('id="model-search"',html)
        self.assertIn('.machine[hidden]{display:none}',html)
        for slug in MACHINES:
            path="maskinarkiv/"+slug+".html"
            self.assertTrue((ROOT/path).is_file())
            self.assertIn('href="/'+path+'"',html)
        self.assertEqual(sitemap().count(BASE+"maskinarkiv/stiga-park-2000.html"),1)

    def test_project_is_unlisted_and_unindexed(self):
        self.assertIn('name="robots" content="noindex,follow"',content("projekt.html"))
        self.assertNotIn(BASE+"projekt.html",sitemap())

if __name__=="__main__":unittest.main()

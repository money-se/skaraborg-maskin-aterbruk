"""Regression checks for legacy public canonical URLs (standard library only)."""
import json
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://skaraborgmaskin.se/"
LEGACY = [
    "metallskrot-hjo-skovde.html",
    "maskinskrot-skaraborg.html",
    "tomma-verkstad-maskiner.html",
    "trasig-grasklippare-varde.html",
    "akgrasklippare-startar-inte.html",
    "kop-trasiga-maskiner-skaraborg.html",
    "salja-grasklippare-skaraborg.html",
    "bli-av-med-maskiner-skaraborg.html",
    "salja-akgrasklippare-skaraborg.html",
    "salja-tradgardsmaskiner-skaraborg.html",
    "dodsbo-glom-inte-garaget.html",
]
GUIDE = "dodsbo-glom-inte-garaget.html"


def head_tags(filename):
    text = (ROOT / filename).read_text(encoding="utf-8")
    head = re.split(r"</head\s*>", text, maxsplit=1, flags=re.I)[0]
    canonical = re.findall(r'<link\s+rel="canonical"\s+href="([^"]+)"', head, re.I)
    return text, head, canonical


class LegacyCanonicalTests(unittest.TestCase):
    def test_legacy_pages_have_one_self_canonical_on_our_domain(self):
        for filename in LEGACY:
            with self.subTest(filename=filename):
                full, head, canonicals = head_tags(filename)
                self.assertEqual(canonicals, [SITE + filename])
                self.assertNotIn("money-se.github.io/skaraborg-maskin-aterbruk/", head)
                self.assertNotIn("https://skaraborgmaskin.se/e-garaget.html", full)

    def test_guide_metadata_and_structured_data_agree(self):
        _, head, canonicals = head_tags(GUIDE)
        self.assertEqual(canonicals, [SITE + GUIDE])
        self.assertIn('property="og:url" content="' + SITE + GUIDE + '"', head)
        scripts = re.findall(r'<script type="application/ld\+json">([\s\S]*?)</script>', head)
        ld_data = [json.loads(raw) for raw in scripts]
        articles = [entry for entry in ld_data if entry.get("@type") == "Article"]
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0].get("mainEntityOfPage"), SITE + GUIDE)

    def test_guide_is_discoverable_without_mirroring_old_thin_pages(self):
        tree = ET.parse(ROOT / "sitemap.xml")
        urls = [el.text for el in tree.iter() if el.tag.endswith("}loc") or el.tag == "loc"]
        self.assertEqual(urls.count(SITE + GUIDE), 1)
        for filename in LEGACY:
            if filename != GUIDE:
                self.assertNotIn(SITE + filename, urls)
        self.assertIn('href="' + GUIDE + '"', (ROOT / "dodsbo-utrensning.html").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()

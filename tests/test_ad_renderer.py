"""Regression tests for the public, static ad detail renderer."""
import importlib.util
import os
from pathlib import Path
import re
import unittest
from html.parser import HTMLParser

os.environ.setdefault("SUPABASE_PUBLISHABLE_KEY", "fixture-only-not-a-real-secret")
SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "generate_ad_seo.py"
spec = importlib.util.spec_from_file_location("adseo", SCRIPT)
adseo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adseo)

AD_ID = "cc6a351d-29b5-4754-af16-9040c25bfd35"
URL = "https://skaraborgmaskin.se/annonser/provobjekt-cc6a351d.html"


def fixture(status="sale", title="Provobjekt"):
    return {
        "id": AD_ID,
        "title": title,
        "description": "En begagnad maskin.\nKänd brist: saknar drivrem.",
        "price_sek": 3000,
        "location_name": "Hjo",
        "status": status,
        "marketplace_url": "https://www.facebook.com/marketplace/item/12345",
        "image_paths": ["a/photo-1.webp", "a/photo-2.webp"],
    }


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = 0
        self.buttons = {}
        self.images = []
        self.canonical = []
        self.robots = []
        self.links = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "h1":
            self.h1 += 1
        if tag == "button" and "id" in d:
            self.buttons[d["id"]] = d
        if tag == "img":
            self.images.append(d)
        if tag == "link" and d.get("rel") == "canonical":
            self.canonical.append(d.get("href"))
        if tag == "meta" and d.get("name") == "robots":
            self.robots.append(d.get("content"))
        if tag == "a":
            self.links.append(d.get("href"))


class TestAdSeo(unittest.TestCase):
    def test_live_ad_is_accessible_and_contactable(self):
        content = adseo.render(fixture(), URL)
        parser = Parser()
        parser.feed(content)
        self.assertEqual(parser.h1, 1)
        self.assertEqual(parser.canonical, [URL])
        self.assertIn("index,follow", parser.robots[0])
        self.assertIn("3 000 kr", content)
        self.assertIn("Till salu", content)
        self.assertIn("sms:+46727483256", parser.links)
        self.assertIn("https://www.facebook.com/profile.php?id=61588383880828", parser.links)
        self.assertEqual(content.count('data-image='), 2)
        self.assertIn("ad-primary-image", parser.images[0].get("id", ""))
        self.assertIn("photo-open", parser.buttons)
        self.assertIn("photo-close", parser.buttons)
        self.assertIn('data-page="annons:' + AD_ID + '"', content)
        self.assertIn('id="site-header"', content)
        self.assertIn('id="site-footer"', content)

    def test_pending_and_sold_are_not_buyable(self):
        for status, text in [("pending", "Reserverad"), ("sold", "Såld")]:
            content = adseo.render(fixture(status=status), URL)
            self.assertIn(text, content)
            self.assertNotIn('href="sms:+46727483256"', content)
            parser = Parser()
            parser.feed(content)
            self.assertEqual(parser.robots[0].startswith("noindex"), status == "sold")

    def test_missing_images_no_gallery_crash(self):
        ad = fixture()
        ad["image_paths"] = []
        content = adseo.render(ad, URL)
        self.assertIn("Ingen produktbild tillgänglig", content)
        self.assertNotIn('id="photo-open"', content)

    def test_html_escaping(self):
        payload = "<script>alert('x')</script>"
        content = adseo.render(fixture(title=payload), URL)
        self.assertNotIn(payload, content)
        self.assertIn("&lt;script&gt;", content)

    def test_external_marketplace_url_is_allowlisted(self):
        ad = fixture()
        ad["marketplace_url"] = "https://example.invalid/bad"
        self.assertNotIn("example.invalid", adseo.render(ad, URL))
        ad["marketplace_url"] = "javascript:alert(1)"
        self.assertNotIn("javascript:alert", adseo.render(ad, URL))

    def test_slug_is_stable(self):
        self.assertEqual(adseo.slugify("VÄGSKRAPA VRETEN 2 M"), "vagskrapa-vreten-2-m")


if __name__ == "__main__":
    unittest.main()

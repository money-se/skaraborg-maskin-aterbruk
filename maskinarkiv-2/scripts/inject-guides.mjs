import fs from "node:fs";
import path from "node:path";
import assert from "node:assert/strict";

const root = process.cwd();
const catalog = JSON.parse(fs.readFileSync(path.join(root, "src/_data/digital-guides.json"), "utf8"));
const placements = JSON.parse(fs.readFileSync(path.join(root, "src/_data/digital-guide-placements.json"), "utf8"));
const escapeHtml = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
const allowed = url => /^https:\/\/(?:skaraborgmerch\.se|cdn\.shopify\.com)\//.test(url);
const card = p => {
  for (const key of ["url", "image"]) assert.ok(allowed(p[key]), "Guide has unsafe or unexpected URL: " + key);
  assert.ok(Number.isInteger(p.priceSek) && p.priceSek > 0, "Invalid guide price");
  return '<aside class="guide-promo" aria-label="Digital guide från Skaraborg Merch" style="display:flex;gap:16px;align-items:center;flex-wrap:wrap;padding:20px;margin:24px 0;border:1px solid #b8d0bf;border-radius:14px;background:#f4f8f3">' +
    '<a href="' + escapeHtml(p.url) + '" target="_blank" rel="noopener noreferrer"><img src="' + escapeHtml(p.image) + '" alt="Omslag till ' + escapeHtml(p.title) + '" loading="lazy" width="110" style="width:110px;height:auto;border-radius:6px"></a>' +
    '<div style="flex:1 1 230px"><p style="margin:0;font-size:12px;font-weight:700;color:#3c6743">DIGITAL GUIDE · SKARABORG MERCH</p><h3 style="margin:8px 0">' + escapeHtml(p.title) + '</h3>' +
    '<p>' + escapeHtml(p.description) + '</p><p><strong>' + p.priceSek + ' kr</strong> · PDF, digital leverans</p>' +
    '<a href="' + escapeHtml(p.url) + '" target="_blank" rel="noopener noreferrer" style="display:inline-block;padding:10px 14px;border-radius:8px;background:#225c36;color:white;text-decoration:none">Se guiden hos Skaraborg Merch ↗</a></div></aside>';
};
let updated = 0;
for (const [slug, spots] of Object.entries(placements)) {
  assert.match(slug, /^[a-z0-9-]+$/, "Invalid machine slug");
  const target = path.join(root, "..", "_maskinarkiv-preview", "maskinarkiv", slug + ".html");
  assert.ok(fs.existsSync(target), "Generated machine page missing: " + slug);
  let html = fs.readFileSync(target, "utf8");
  assert.ok(!html.includes('class="guide-promo"'), "Legacy hardcoded guide card remains: " + slug);
  const chapters = new Set();
  for (const spot of spots) {
    assert.ok(!chapters.has(spot.chapter), "Duplicate guide placement in one chapter: " + spot.chapter);
    chapters.add(spot.chapter);
    const p = catalog.products[spot.product];
    assert.ok(p && p.active, "Missing/inactive guide: " + spot.product);
    assert.match(spot.chapter, /^[a-z0-9-]+$/);
    const token = '<section id="' + spot.chapter + '"';
    const start = html.indexOf(token);
    assert.ok(start >= 0, "Missing destination chapter: " + spot.chapter);
    const stop = html.indexOf("</section>", start);
    assert.ok(stop > start, "Unclosed chapter: " + spot.chapter);
    html = html.slice(0, stop) + card(p) + html.slice(stop);
  }
  fs.writeFileSync(target, html);
  updated++;
}
console.log("MASKINARKIV_GUIDES=PASS; pages=" + updated);

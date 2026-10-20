import fs from "node:fs";
import assert from "node:assert/strict";
const source=JSON.parse(fs.readFileSync("src/_data/machines/stiga-park-16.json","utf8"));
const target="../_maskinarkiv-preview/maskinarkiv/stiga-park-16.html";
assert.ok(fs.existsSync(target),"Kör npm run build före npm run check");
const html=fs.readFileSync(target,"utf8");
assert.equal(source.chapters.length,16);
const allowed = new Set(["html","facts","note","warning","check","table-scroll","steps","answer","faq","cta","tradera-follow"]);
for (const chapter of source.chapters) { assert.ok(chapter.blocks.length > 0, "Empty chapter: "+chapter.id); for (const block of chapter.blocks) assert.ok(allowed.has(block.type), "Unknown block: "+block.type); }
const typed = source.chapters.flatMap(c => c.blocks).filter(b => b.type !== "html");
assert.equal(typed.length, 23, "Unexpected component count inside chapters");
assert.equal(source.traderaBlock.type,"tradera-follow");
assert.ok(source.afterChaptersMetaHtml.includes("Källprincip"));
assert.equal((html.match(/class="tradera-section"/g)||[]).length,1);
assert.equal((html.match(/<section\b/g)||[]).length,(html.match(/<\/section>/g)||[]).length,"Section tags unbalanced");
assert.equal(typed.filter(b => b.type === "facts").length,2);
assert.equal(typed.filter(b => b.type === "table-scroll").length,4);
assert.equal(source.sources.length,6);
for(const chapter of source.chapters) assert.ok(html.includes('id="'+chapter.id+'"'),"Saknar kapitel: "+chapter.id);
assert.ok(html.includes('href="/tradera.html"'));
assert.ok(html.includes('class="source-disclosure"'));
assert.ok(html.includes('maskinarkiv-v6.css'));
assert.equal((html.match(/<section id="kallor"/g)||[]).length,1);
assert.equal((html.match(/class="source-record"/g)||[]).length,source.sources.length);
const ids=[...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
assert.equal(new Set(ids).size,ids.length,"Dubblett-ID");
for(const [,anchor] of html.matchAll(/href="#([^"]+)"/g)) assert.ok(ids.includes(anchor),"Trasigt ankare: "+anchor);
console.log("MASKINARKIV_2_COMPONENTS=PASS; articles="+source.chapters.length+"; sources="+source.sources.length);


const rider = JSON.parse(fs.readFileSync("src/_data/machines/husqvarna-rider-13.json","utf8"));
const riderPath="../_maskinarkiv-preview/maskinarkiv/husqvarna-rider-13.html";
assert.ok(fs.existsSync(riderPath), "Rider 13 HTML must be generated");
const riderHtml=fs.readFileSync(riderPath,"utf8");
assert.equal(rider.chapters.length,14);
assert.equal(rider.sources.length,8);
for(const ch of rider.chapters) assert.ok(riderHtml.includes('id="'+ch.id+'"'), "Rider chapter missing: "+ch.id);
assert.ok(riderHtml.includes('class="source-disclosure"'));
assert.ok(riderHtml.includes("Husqvarna Rider 13"));
const riderIds=[...riderHtml.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
assert.equal(new Set(riderIds).size,riderIds.length,"Rider duplicate IDs");
for(const [,anchor] of riderHtml.matchAll(/href="#([^"]+)"/g)) assert.ok(riderIds.includes(anchor),"Rider broken anchor: "+anchor);
assert.equal((riderHtml.match(/<section\b/g)||[]).length,(riderHtml.match(/<\/section>/g)||[]).length,"Rider section tags unbalanced");
console.log("MASKINARKIV_2_RIDER=PASS; chapters="+rider.chapters.length+"; sources="+rider.sources.length);


const lth=JSON.parse(fs.readFileSync("src/_data/machines/husqvarna-lth151.json","utf8"));
const lthPath="../_maskinarkiv-preview/maskinarkiv/husqvarna-lth151.html";
assert.ok(fs.existsSync(lthPath),"LTH151 output missing");
const lthHtml=fs.readFileSync(lthPath,"utf8");
assert.equal(lth.chapters.length,14);
assert.equal(lth.sources.length,4);
for(const chapter of lth.chapters)assert.ok(lthHtml.includes('id="'+chapter.id+'"'),"LTH151 chapter missing: "+chapter.id);
const lthIds=[...lthHtml.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
assert.equal(new Set(lthIds).size,lthIds.length,"LTH151 duplicate IDs");
for(const [,anchor] of lthHtml.matchAll(/href="#([^"]+)"/g))assert.ok(lthIds.includes(anchor),"LTH151 broken anchor: "+anchor);
assert.equal((lthHtml.match(/<section\b/g)||[]).length,(lthHtml.match(/<\/section>/g)||[]).length,"LTH151 section tags unbalanced");
assert.ok(lthHtml.includes('href="/tradera.html"'));
assert.equal((lthHtml.match(/class="source-record"/g)||[]).length,lth.sources.length);
console.log("MASKINARKIV_2_LTH151=PASS");

for(const page of [html,riderHtml,lthHtml]) {
  assert.equal((page.match(/class="archive-contact"/g)||[]).length,1,"Missing or duplicate shared contact block");
  assert.ok(page.includes('Kontakta oss på Facebook'),"Shared Facebook CTA missing");
  assert.ok(page.includes('class="footer-bottom"'),"Shared footer missing");
  assert.ok(page.includes('class="smar-'),"Shared header missing");
  assert.ok(!page.includes('inject("site-header"'),"Runtime header injection must be removed");
}
console.log("MASKINARKIV_2_SHARED_CHROME=PASS");

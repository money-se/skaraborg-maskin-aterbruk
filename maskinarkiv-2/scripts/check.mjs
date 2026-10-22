import fs from "node:fs";
import assert from "node:assert/strict";
const source=JSON.parse(fs.readFileSync("src/_data/machines/stiga-park-16.json","utf8"));
const target="../_maskinarkiv-preview/maskinarkiv/stiga-park-16.html";
assert.ok(fs.existsSync(target),"Kör npm run build före npm run check");
const html=fs.readFileSync(target,"utf8");
assert.equal(source.chapters.length,15);
const allowed = new Set(["html","facts","note","warning","check","table-scroll","steps","answer","faq","cta","tradera-follow"]);
for (const chapter of source.chapters) { assert.ok(chapter.blocks.length > 0, "Empty chapter: "+chapter.id); for (const block of chapter.blocks) assert.ok(allowed.has(block.type), "Unknown block: "+block.type); }
const typed = source.chapters.flatMap(c => c.blocks).filter(b => b.type !== "html");
assert.equal(typed.length, 22, "Unexpected component count inside chapters");
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
assert.equal(rider.chapters.length,17);
assert.deepEqual(rider.chapters.slice(0,5).map(c=>c.id),["hitta-hjalp","oversikt","identifiering","felsokning","reservdelar"]);
assert.equal(rider.sources.length,18);
for(const ch of rider.chapters) assert.ok(riderHtml.includes('id="'+ch.id+'"'), "Rider chapter missing: "+ch.id);
assert.ok(riderHtml.includes('class="source-disclosure"'));
assert.ok(riderHtml.includes("Husqvarna Rider 13"));
for(const phrase of ["Provkörningsprotokoll för köpare","Varför blir drivningen svag när den är varm?","Så hittar du rätt originalmanual","Ojämn klippning"])assert.ok(riderHtml.includes(phrase),"Rider enrichment missing: "+phrase);
const riderIds=[...riderHtml.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
assert.equal(new Set(riderIds).size,riderIds.length,"Rider duplicate IDs");
for(const [,anchor] of riderHtml.matchAll(/href="#([^"]+)"/g)) assert.ok(riderIds.includes(anchor),"Rider broken anchor: "+anchor);
assert.equal((riderHtml.match(/<section\b/g)||[]).length,(riderHtml.match(/<\/section>/g)||[]).length,"Rider section tags unbalanced");
const guideCatalog=JSON.parse(fs.readFileSync("src/_data/digital-guides.json","utf8"));
const guidePlacements=JSON.parse(fs.readFileSync("src/_data/digital-guide-placements.json","utf8"));
assert.equal(Object.keys(guideCatalog.products).length,4,"Expected all four actual Shopify guides");
assert.equal(guidePlacements["husqvarna-rider-13"].length,4,"Four guide placements required");
assert.equal((riderHtml.match(/class="guide-promo"/g)||[]).length,4,"Exactly four centrally injected Rider guide cards");
for(const p of Object.values(guideCatalog.products)) {
  assert.ok(riderHtml.includes(p.image),"Missing actual Shopify cover: "+p.title);
  assert.ok(riderHtml.includes(p.url),"Missing Shopify product link: "+p.title);
}
assert.equal(rider.chapters.flatMap(ch=>ch.blocks).filter(b=>b.html?.includes('class="guide-promo"')).length,0,"Cards must not be duplicated in model source");
const villaGuideHtml=fs.readFileSync("../_maskinarkiv-preview/maskinarkiv/stiga-villa-12-hst.html","utf8");
assert.equal(guidePlacements["stiga-villa-12-hst"].length,4,"Villa must have exactly four relevant guide placements");
assert.equal((villaGuideHtml.match(/class="guide-promo"/g)||[]).length,4,"Villa should render four central guide cards");
for(const name of ["start","verkstad","ordbok","kopguide"]){
  const product=guideCatalog.products[name];
  assert.ok(villaGuideHtml.includes(product.image),"Villa missing image "+name);
  assert.ok(villaGuideHtml.includes(product.url),"Villa missing product URL "+name);
}
assert.ok(guidePlacements["stiga-villa-12-hst"].some(p=>p.chapter==="reservdelar"&&p.product==="ordbok"),"Villa dictionary belongs in spare-parts chapter");
console.log("MASKINARKIV_CENTRAL_GUIDES=PASS");
console.log("MASKINARKIV_2_RIDER=PASS; chapters="+rider.chapters.length+"; sources="+rider.sources.length);


const lth=JSON.parse(fs.readFileSync("src/_data/machines/husqvarna-lth151.json","utf8"));
const lthPath="../_maskinarkiv-preview/maskinarkiv/husqvarna-lth151.html";
assert.ok(fs.existsSync(lthPath),"LTH151 output missing");
const lthHtml=fs.readFileSync(lthPath,"utf8");
assert.equal(lth.chapters.length,13);
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
  assert.equal((page.match(/class="archive-reuse"/g)||[]).length,1,"Missing or duplicate shared reuse block");
  assert.ok(page.includes('Kontakta oss på Facebook'),"Reuse Facebook CTA missing");
  assert.ok(page.includes('class="footer-bottom"'),"Shared footer missing");
  assert.ok(page.includes('class="smar-'),"Shared header missing");
  assert.ok(!page.includes('inject("site-header"'),"Runtime header injection must be removed");
}
console.log("MASKINARKIV_2_SHARED_CHROME=PASS");

for(const page of [html,riderHtml,lthHtml]){assert.equal((page.match(/id="aterbruk"/g)||[]).length,1,"Exactly one shared reuse section required");assert.ok(page.includes("Så köper vi maskiner"),"Missing buying CTA");}
console.log("MASKINARKIV_2_REUSE_UNIFIED=PASS");

for(const page of [html,riderHtml,lthHtml]) {
  const reuseAt=page.indexOf('id="aterbruk"');
  const traderaAt=page.indexOf('class="tradera-section"');
  const sourcesAt=page.indexOf('id="kallor"');
  assert.ok(reuseAt>=0 && traderaAt>reuseAt && sourcesAt>traderaAt,"Wrong reusable section ordering");
  assert.ok(!page.includes("Har du en Husqvarna Rider som blivit stående?"),"Legacy Rider Återbruk remains");
  assert.equal((page.match(/Kontakta oss på Facebook/g)||[]).length,1,"One Facebook CTA expected");
}
console.log("MASKINARKIV_2_SECTION_ORDER=PASS");


for(const [slug,chapters,sources] of [["stiga-villa-12-hst",12,14],["jonsered-lt2115",21,10]]) {
 const data=JSON.parse(fs.readFileSync("src/_data/machines/"+slug+".json","utf8"));
 const file="../_maskinarkiv-preview/maskinarkiv/"+slug+".html";
 assert.ok(fs.existsSync(file),"Missing generated "+slug);
 const page=fs.readFileSync(file,"utf8");
 assert.equal(data.chapters.length,chapters);
 assert.equal(data.sources.length,sources);
 if(slug==="stiga-villa-12-hst"){
   assert.ok(!page.includes("[Källspår:"),"Villa internal research IDs leaked into public HTML");
   assert.ok(page.includes("Reglagen enligt manualens figurer"),"Villa control table missing");
   assert.ok(page.includes("Symtomguide: fem olika problem"),"Villa diagnostic table missing");
   assert.equal((page.match(/Beställ rätt del i fem steg/g)||[]).length,1,"Villa spare-parts ordering guide duplicated");
   assert.equal((page.match(/Utökad kontroll före köp/g)||[]).length,1,"Villa buyer checklist duplicated");
   assert.ok(page.includes("Gör en servicejournal som går att använda nästa år"),"Villa service journal missing");
 }

 const ids=[...page.matchAll(/\bid="([^"]+)"/g)].map(x=>x[1]);
 assert.equal(ids.length,new Set(ids).size,slug+" duplicate IDs");
 for(const [,anchor] of page.matchAll(/href="#([^"]+)"/g)) assert.ok(ids.includes(anchor),slug+" bad anchor "+anchor);
 for(const chapter of data.chapters){
   assert.ok(ids.includes(chapter.id),slug+" missing "+chapter.id);
   for(const block of chapter.blocks){if(slug==="stiga-villa-12-hst" && block.type==="html") assert.ok(!/<\/?section\b/i.test(block.html||""),slug+" section tags must be owned by the chapter template: "+chapter.id);}
 }

 assert.equal((page.match(/<section\b/g)||[]).length,(page.match(/<\/section>/g)||[]).length,slug+" unbalanced sections");
 const reuse=page.indexOf('id="aterbruk"'),tradera=page.indexOf('id="tradera"'),source=page.indexOf('id="kallor"');
 assert.ok(reuse>=0&&reuse<tradera&&tradera<source,slug+" bad CTA order");
 assert.ok(page.includes('Kontakta oss på Facebook'));
 assert.ok(page.includes('class="footer-bottom"'));
 assert.equal([...page.matchAll(/<\/(?:b|strong)>(?=[\p{L}\d])/gu)].length,0,slug+" missing whitespace after labels");
 console.log("MASKINARKIV_2_"+slug+"=PASS");
}

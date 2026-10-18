import fs from "node:fs";
import assert from "node:assert/strict";
const source=JSON.parse(fs.readFileSync("src/_data/machines/stiga-park-16.json","utf8"));
const target="../_maskinarkiv-preview/maskinarkiv/stiga-park-16.html";
assert.ok(fs.existsSync(target), "Kör npm run build före npm run check");
const html=fs.readFileSync(target,"utf8");
assert.equal(source.chapters.length,17);
for(const chapter of source.chapters){assert.ok(html.includes('id="'+chapter.id+'"'),"Saknar kapitel: "+chapter.id);}
assert.ok(html.includes('href="/tradera.html"'));
assert.ok(html.includes('class="source-disclosure"'));
assert.ok(html.includes('maskinarkiv-v6.css'));
const ids=[...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
assert.equal(new Set(ids).size,ids.length,"Dubblett-ID");
for(const [,anchor] of html.matchAll(/href="#([^"]+)"/g)) assert.ok(ids.includes(anchor),"Trasigt ankare: "+anchor);
console.log("MASKINARKIV_2_PILOT=PASS; kapitel="+source.chapters.length);

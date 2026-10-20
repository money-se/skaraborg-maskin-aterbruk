import fs from "node:fs";
import path from "node:path";
import assert from "node:assert/strict";
const root=path.resolve(process.cwd(),"..");
const output=path.join(root,"_maskinarkiv-preview","maskinarkiv");
const slugs=["stiga-park-16","husqvarna-rider-13","husqvarna-lth151","stiga-villa-12-hst","jonsered-lt2115","husqvarna-rider-850"];
for(const slug of slugs){
 const file=path.join(output,slug+".html");
 const html=fs.readFileSync(file,"utf8");
 const canonical="https://skaraborgmaskin.se/maskinarkiv/"+slug+".html";
 const count=fragment=>(html.match(fragment)||[]).length;
 assert.equal(count(/<title>/gi),1,slug+" title count");
 assert.equal(count(/<meta name="description"/gi),1,slug+" description count");
 assert.equal(count(/<link rel="canonical"/gi),1,slug+" canonical count");
 assert.ok(html.includes('href="'+canonical+'"'),slug+" canonical mismatch");
 assert.ok(html.includes('content="index,follow,max-image-preview:large"'),slug+" unexpected robots");
 assert.ok(!/noindex|nofollow/i.test((html.match(/<meta name="robots"[^>]*>/i)||[""])[0]),slug+" accidental noindex");
 assert.equal(count(/id="aterbruk"/g),1,slug+" reuse");
 assert.equal(count(/id="tradera"/g),1,slug+" tradera");
 assert.equal(count(/id="kallor"/g),1,slug+" sources");
 assert.equal(count(/class="footer-bottom"/g),1,slug+" footer");
 assert.ok(html.includes('href="/maskinarkiv/maskinarkiv-v6.css"'),slug+" CSS");
 assert.ok(!html.includes('inject("site-header"')&&!html.includes('inject("site-footer"'),slug+" old partial loader");
 for(const [,link] of html.matchAll(/(?:href|src)="([^"]+)"/g)){
  if(!link.startsWith("/")||link.startsWith("//"))continue;
  const pathname=link.split(/[?#]/)[0];
  if(pathname==="/maskinarkiv/maskinarkiv-v6.css")continue;
  if(pathname==="/")continue;
  const target=path.join(root,pathname.slice(1));
  assert.ok(fs.existsSync(target),slug+" missing local link target: "+pathname);
 }
 console.log("PRODUCTION_AUDIT_"+slug+"=PASS");
}
console.log("MASKINARKIV_2_PRODUCTION_AUDIT=PASS");

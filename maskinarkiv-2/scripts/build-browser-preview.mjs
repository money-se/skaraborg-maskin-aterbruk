import fs from "node:fs";
import path from "node:path";
import assert from "node:assert/strict";

const repoRoot=path.resolve(process.cwd(),"..");
const built=path.join(repoRoot,"_maskinarkiv-preview");
const destination=path.join(process.cwd(),"preview");
const slugs=["stiga-park-16","husqvarna-rider-13","husqvarna-lth151","stiga-villa-12-hst","jonsered-lt2115","husqvarna-rider-850"];
const domain="https://skaraborgmaskin.se";
fs.mkdirSync(destination,{recursive:true});
function publicHref(url){
  if(url.startsWith("#")||url.startsWith("?")||/^[a-z][a-z0-9+.-]*:/i.test(url))return url;
  if(url.startsWith("//"))return "https:"+url;
  if(url.startsWith("/"))return domain+url;
  return domain+"/"+url.replace(/^(?:\.\.\/)+/,"").replace(/^\.\//,"");
}
function prepare(html){
  html=html.replace(/<link rel="canonical"[^>]*>/gi,"");
  html=html.replace(/<meta name="robots"[^>]*>/gi,"");
  html=html.replace(/<\/head>/i,'<meta name="robots" content="noindex,nofollow"></head>');
  html=html.replace(/(href|src)=(["'])([^"']+)\2/gi,(all,attr,quote,value)=>attr+"="+quote+publicHref(value)+quote);
  return html;
}
const entries=[];
for(const slug of slugs){
  const src=path.join(built,"maskinarkiv",slug+".html");
  assert.ok(fs.existsSync(src),"Missing generated HTML for "+slug);
  let html=prepare(fs.readFileSync(src,"utf8"));
  const ids=[...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
  assert.equal(ids.length,new Set(ids).size,slug+" duplicate id");
  for(const [,anchor] of html.matchAll(/href="#([^"]+)"/g))
    assert.ok(ids.includes(anchor),slug+" missing anchor "+anchor);
  assert.ok(html.includes('class="footer-bottom"'),slug+" footer missing");
  assert.ok(html.includes('id="aterbruk"'),slug+" reuse missing");
  assert.ok(html.includes('id="tradera"'),slug+" Tradera missing");
  assert.ok(html.includes('id="kallor"'),slug+" sources missing");
  assert.ok(html.includes('name="robots" content="noindex,nofollow"'));
  assert.ok(html.includes(domain+"/maskinarkiv/maskinarkiv-v6.css"));
  const output=path.join(destination,slug+".html");
  fs.writeFileSync(output,html);
  const data=JSON.parse(fs.readFileSync(path.join("src","_data","machines",slug+".json"),"utf8"));
  entries.push({slug,name:data.model});
}
let index=fs.readFileSync(path.join(built,"index.html"),"utf8");
assert.ok(index.includes('noindex,nofollow'));
fs.writeFileSync(path.join(destination,"index.html"),index);
for(const item of entries)assert.ok(index.includes('maskinarkiv/'+item.slug+'.html'),"Index link missing: "+item.slug);
index=index.replace(/href="maskinarkiv\//g,'href="');
fs.writeFileSync(path.join(destination,"index.html"),index);
console.log("MASKINARKIV_2_BROWSER_PREVIEW=PASS, pages="+entries.length);

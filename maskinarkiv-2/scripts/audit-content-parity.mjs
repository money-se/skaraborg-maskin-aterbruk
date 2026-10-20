import fs from "node:fs";
import path from "node:path";
import assert from "node:assert/strict";
const root=path.resolve(process.cwd(),"..");
const slugs=["stiga-park-16","husqvarna-rider-13","husqvarna-lth151","stiga-villa-12-hst","jonsered-lt2115"];
const normalize=s=>s.replace(/<[^>]*>/g," ").replace(/&(?:amp|nbsp|lt|gt|quot);/g," ").replace(/\s+/g," ").trim();
const article=s=>(s.match(/<article class="article">([\s\S]*?)<\/article>/)||[])[1]||"";
const paragraphs=s=>[...article(s).matchAll(/<(p|li|td|th|summary|h[2-4])\b[^>]*>([\s\S]*?)<\/\1>/gi)].map(m=>normalize(m[2])).filter(x=>x.length>15);
const expectedOmissions={
 "stiga-park-16":["Har du en Park 16 stående?","Skaraborg Maskin Återbruk arbetar med begagnade maskiner","Vi gör en individuell bedömning och kan diskutera hämtning"],
 "husqvarna-rider-13":["Har du en Husqvarna Rider som blivit stående?","Vi är intresserade av åkgräsklippare och Riders","Äldre dokument och artikelnummer kan skilja sig mellan produktversioner."],
 "husqvarna-lth151":["Har du en LTH151 som blivit stående?","Skaraborg Maskin Återbruk är intresserade av äldre trädgårdsmaskiner","Faktaunderlag sammanställt: 18 oktober 2026.",""],
 "stiga-villa-12-hst":["Har du en Villa 12 HST som blivit stående?","Även en maskin som inte längre startar","Välj gärna dokument som hör till just din maskins produktnummer."],
 "jonsered-lt2115":["Har du en Jonsered stående?","Vi är intresserade av åkgräsklippare i olika skick.","Välj dokument efter produktnumret på din maskin."]
};
const result=[];
for(const slug of slugs){
 const old=fs.readFileSync(path.join(root,"maskinarkiv",slug+".html"),"utf8");
 const made=fs.readFileSync(path.join(root,"_maskinarkiv-preview","maskinarkiv",slug+".html"),"utf8");
 const list=paragraphs(old),newList=new Set(paragraphs(made));
 const missing=list.filter(x=>!newList.has(x));
 const unexpected=missing.filter(text=>!expectedOmissions[slug].some(begin=>begin&&text.startsWith(begin)));
 assert.deepEqual(unexpected,[],slug+" lost unsanctioned article content");
 for(const [kind,re] of Object.entries({source:/class="source-record"/g,table:/<table\b/g,faq:/<details\b/g})){
  const tally=s=>(s.match(re)||[]).length;
  assert.equal(tally(made),tally(old),slug+" changed "+kind+" count");
 }
 const oldHead=(old.match(/<head>([\s\S]*?)<\/head>/i)||[])[1]||"";
 const newHead=(made.match(/<head>([\s\S]*?)<\/head>/i)||[])[1]||"";
 const important=[
  /<title>[\s\S]*?<\/title>/i,
  /<meta name="description"[^>]*>/i,
  /<link rel="canonical"[^>]*>/i
 ];
 for(const re of important)assert.equal(oldHead.match(re)?.[0],newHead.match(re)?.[0],slug+" SEO metadata changed");
 result.push({slug,originalParagraphs:list.length,preservedParagraphs:list.length-missing.length,intentionalChanges:missing});
 console.log("CONTENT_PARITY_"+slug+"=PASS");
}
fs.writeFileSync(path.join(root,"_maskinarkiv-release-review","content-parity-report.json"),JSON.stringify({status:"PASS_WITH_DOCUMENTED_SHARED_REUSE_CHANGES",results:result},null,2)+"\n");
console.log("MASKINARKIV_2_CONTENT_PARITY=PASS");

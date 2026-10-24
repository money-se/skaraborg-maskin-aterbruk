// Shared Habo service renderer. From repository root: node scripts/build-habo-services.mjs [--check]
import fs from "node:fs";
import path from "node:path";
const root=process.cwd();
const template=fs.readFileSync(path.join(root,"data/habo-service-template.html.txt"),"utf8");
const records=["data/habo-services-part1.json","data/habo-services-part2.json"].flatMap(file=>JSON.parse(fs.readFileSync(path.join(root,file),"utf8")));
const escapeHtml=v=>String(v).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#39;");
const paragraph=s=>"<p>"+escapeHtml(s)+"</p>";
const list=values=>values.map(v=>"<li>"+escapeHtml(v)+"</li>").join("\n");
const items=values=>values.map(([title,description],i)=>'<article class="hb-card"><span class="hb-card-index">'+String(i+1).padStart(2,"0")+'</span><h3>'+escapeHtml(title)+'</h3><p>'+escapeHtml(description)+'</p></article>').join("\n");
function render(data){
  if(!/^[a-z0-9-]+$/.test(data.slug))throw new Error("Unsafe slug "+data.slug);
  const url="https://skaraborgmaskin.se/"+data.slug+".html";
  for(const [k,expected] of [["steps",3],["faq",3]])if(data[k]?.length!==expected)throw new Error(data.slug+" requires "+expected+" "+k);
  const schema=JSON.stringify({"@context":"https://schema.org","@type":"WebPage","name":data.h1,"url":url,"inLanguage":"sv-SE","isPartOf":{"@type":"WebSite","name":"Skaraborg Maskin & Återbruk","url":"https://skaraborgmaskin.se/"}}).replace(/</g,"\\u003c");
  const replacements={
    META_TITLE:escapeHtml(data.h1+" | Skaraborg Maskin & Återbruk"),
    META_DESCRIPTION:escapeHtml(data.lead.slice(0,158)),
    CANONICAL:escapeHtml(url),
    OG_TITLE:escapeHtml(data.h1),
    SCHEMA:schema,
    SHORT:escapeHtml(data.short),
    KICKER:escapeHtml(data.kicker),
    H1:escapeHtml(data.h1),
    LEAD:escapeHtml(data.lead),
    HERO_PANEL_TITLE:escapeHtml(data.panelTitle),
    HERO_POINTS:list(data.panelPoints),
    HERO_NOTE:escapeHtml(data.heroNote),
    STEP_TITLE:escapeHtml(data.stepTitle),
    STEP_LEAD:escapeHtml(data.stepLead),
    STEPS:items(data.steps),
    DETAIL_TITLE:escapeHtml(data.detailTitle),
    DETAIL_PARAS:data.details.map(paragraph).join("\n"),
    ADVICE:escapeHtml(data.advice),
    NOTE_TITLE:escapeHtml(data.noteTitle),
    NOTE_PARAS:data.noteParas.map(paragraph).join("\n"),
    CHECKS:list(data.checks),
    FAQS:data.faq.map(([q,a])=>"<details><summary>"+escapeHtml(q)+"</summary><p>"+escapeHtml(a)+"</p></details>").join("\n"),
    RELATED:data.related.map(([text,url])=>{
      if(!/^\/[a-z0-9/-]+\.html$/.test(url))throw new Error("Bad related link "+url);
      return '<a href="'+escapeHtml(url)+'">'+escapeHtml(text)+' →</a>';
    }).join("\n"),
    CTA_TITLE:escapeHtml(data.ctaTitle),
    CTA_TEXT:escapeHtml(data.ctaText),
  };
  const used=new Set();
  const html=template.replace(/\{\{([A-Z_]+)\}\}/g,(_,key)=>{
    used.add(key);
    if(!(key in replacements))throw new Error(data.slug+" unknown placeholder "+key);
    return replacements[key];
  });
  if(used.size!==Object.keys(replacements).length)throw new Error(data.slug+" missing template placeholders");
  if((html.match(/<h1\b/g)||[]).length!==1||!html.includes('rel="canonical" href="'+url+'"'))throw new Error("HTML validation failed "+data.slug);
  return html;
}
const check=process.argv.includes("--check");
const slugs=new Set();
let failed=0;
for(const data of records){
  if(slugs.has(data.slug))throw new Error("Duplicate slug "+data.slug);
  slugs.add(data.slug);
  const dest=path.join(root,data.slug+".html");
  const desired=render(data);
  if(check){
    const current=fs.existsSync(dest)?fs.readFileSync(dest,"utf8"):null;
    if(current!==desired){console.error("HABO_CHECK_FAIL="+data.slug);failed++}
    else console.log("HABO_CHECK_OK="+data.slug);
  }else{fs.writeFileSync(dest,desired,"utf8");console.log("HABO_BUILD_OK="+data.slug)}
}
if(records.length!==10)throw new Error("Expected 10 Habo service records");
if(failed)process.exitCode=1;
if(check&&!failed)console.log("HABO_ALL_10_PAGES_PASS");

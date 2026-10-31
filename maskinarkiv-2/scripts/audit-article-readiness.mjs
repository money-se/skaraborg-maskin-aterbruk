#!/usr/bin/env node
// Offline, read-only publication readiness audit. Run: node scripts/audit-article-readiness.mjs [--strict]
import fs from "node:fs";
import path from "node:path";
const strict=process.argv.includes("--strict");
const dir="src/_data/machines", evidence="research/machines";
const rows=[];
for(const file of fs.readdirSync(dir).filter(f=>f.endsWith(".json"))){
 const slug=path.basename(file,".json"), article=JSON.parse(fs.readFileSync(path.join(dir,file),"utf8"));
 const blocking=[], warnings=[];
 const row={slug,chapters:article.chapters?.length||0,articleSources:article.sources?.length||0,research:false,status:null,claims:0,sources:0,openGaps:0,blocking,warnings};
 if(article.slug!==slug)blocking.push("article slug mismatch");
 if(!row.chapters)blocking.push("article has no chapters");
 const ids=(article.chapters||[]).map(x=>x.id);
 if(new Set(ids).size!==ids.length)blocking.push("duplicate chapter IDs");
 const source=path.join(evidence,file);
 if(!fs.existsSync(source)){blocking.push("missing canonical research register for exact article slug");rows.push(row);continue}
 row.research=true;
 const research=JSON.parse(fs.readFileSync(source,"utf8"));
 row.status=research.status;row.claims=research.claims?.length||0;row.sources=research.sources?.length||0;row.openGaps=research.gaps?.length||0;
 if(research.slug!==slug)blocking.push("research slug mismatch");
 if(!["ready","scoped_ready"].includes(research.status))blocking.push("research not released");
 const sourceIds=(research.sources||[]).map(s=>s.id),claimIds=(research.claims||[]).map(c=>c.id);
 if(new Set(sourceIds).size!==sourceIds.length)blocking.push("duplicate research source IDs");
 if(new Set(claimIds).size!==claimIds.length)blocking.push("duplicate claim IDs");
 if((research.claims||[]).some(c=>!sourceIds.includes(c.sourceId)))blocking.push("claim references missing source");
 if(research.status==="scoped_ready"){
  const s=research.scopedRelease||{};
  if(!s.reviewedAt||!s.reviewedBy)blocking.push("missing scoped review");
  if(!Array.isArray(s.exclusions)||!s.exclusions.length)blocking.push("scope exclusions missing");
  if((s.publishedClaims||[]).some(id=>!claimIds.includes(id)))blocking.push("published claim not in research register");
  if(row.openGaps)warnings.push("scoped publication only; "+row.openGaps+" research gaps unresolved");
 }else if(row.openGaps)warnings.push(row.openGaps+" unresolved gaps");
 rows.push(row);
}
const summary={articleCount:rows.length,readyForFurtherReview:rows.filter(r=>!r.blocking.length).map(r=>r.slug),missingResearch:rows.filter(r=>!r.research).map(r=>r.slug),rows};
console.log(JSON.stringify(summary,null,2));
if(strict&&rows.some(r=>r.blocking.length))process.exitCode=1;

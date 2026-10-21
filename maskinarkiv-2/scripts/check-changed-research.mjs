import {execFileSync} from "node:child_process";
import {existsSync} from "node:fs";
import assert from "node:assert/strict";
const base=process.env.GITHUB_BASE_REF;
const event=process.env.GITHUB_EVENT_NAME;
let changes=[];
if(event==="pull_request" && base){
  const common=execFileSync("git",["merge-base","HEAD","origin/"+base],{encoding:"utf8"}).trim();
  changes=execFileSync("git",["diff","--name-only",common,"HEAD"],{encoding:"utf8"}).trim().split("\n");
}else if(event==="push"){
  changes=execFileSync("git",["diff","--name-only","HEAD^","HEAD"],{encoding:"utf8"}).trim().split("\n");
}else{
  console.log("RESEARCH_CHANGED_MODELS=SKIP; event="+event);
  process.exit(0);
}
const slugs=[...new Set(changes.map(x=>x.match(/^maskinarkiv-2\/src\/_data\/machines\/([a-z0-9-]+)\.json$/)?.[1]).filter(Boolean))];
for(const slug of slugs){
  const file="research/machines/"+slug+".json";
  assert.ok(existsSync(file),"Research record missing for changed model "+slug);
  execFileSync("node",["scripts/check-research.mjs","--release",slug],{stdio:"inherit"});
}
console.log("RESEARCH_CHANGED_MODELS=PASS; checked="+slugs.length);

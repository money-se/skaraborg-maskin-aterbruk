import fs from "node:fs";
import path from "node:path";
import assert from "node:assert/strict";
const dir="research/machines";
const keys="ABCDEFGHIJKLM".split("");
const args=process.argv.slice(2);
const release=args[0]==="--release";
const target=release?args[1]:null;
const files=fs.readdirSync(dir).filter(f=>f.endsWith(".json"));
assert.ok(files.length>0,"No research records present");
let ready=0, incomplete=0;
for(const file of files){
  const d=JSON.parse(fs.readFileSync(path.join(dir,file),"utf8"));
  assert.equal(d.schemaVersion,1,file+" schema version");
  assert.equal(file,d.slug+".json","Filename must match machine slug");
  assert.ok(["needs_research","ready","scoped_ready"].includes(d.status),d.slug+" invalid status");
  assert.ok(d.reviewDate && /^\d{4}-\d{2}-\d{2}$/.test(d.reviewDate),d.slug+" review date");
  assert.deepEqual(Object.keys(d.topics).sort(),keys,d.slug+" must cover research topics A-M");
  for(const k of keys){
    const t=d.topics[k];
    assert.ok(["verified","gap"].includes(t.state),d.slug+" topic "+k+" missing state");
    assert.ok(t.note && t.note.length>18,d.slug+" topic "+k+" missing explanation");
  }
  assert.ok(d.sources.length>0 && d.claims.length>0,d.slug+" requires sources and claims");
  const sourceIds=new Set();
  for(const s of d.sources){
    assert.ok(s.id && s.document && s.title, d.slug+" incomplete source");
    assert.ok([1,2,3].includes(s.tier),d.slug+" invalid source tier");
    assert.ok(/^https:\/\//.test(s.url),d.slug+" invalid source URL");
    assert.ok(!sourceIds.has(s.id),d.slug+" duplicate source");
    sourceIds.add(s.id);
  }
  const ids=new Set(), claimTopics=new Set();
  for(const c of d.claims){
    assert.ok(c.id && c.statement && c.variant && c.locator,d.slug+" incomplete claim");
    assert.ok(["A","B","C","D"].includes(c.grade),d.slug+" invalid claim grade");
    assert.ok(sourceIds.has(c.sourceId),d.slug+" unsupported source reference");
    assert.ok(keys.includes(c.topic),d.slug+" claim must identify topic A-M");
    if(c.grade==="A")assert.equal(d.sources.find(x=>x.id===c.sourceId).tier,1,d.slug+" grade A requires primary source");
    if(c.grade==="B")assert.ok(d.sources.find(x=>x.id===c.sourceId).tier<=2,d.slug+" grade B requires strong source");
    assert.ok(!ids.has(c.id),d.slug+" duplicate claim ID");ids.add(c.id);
    if(["A","B"].includes(c.grade))claimTopics.add(c.topic);
  }
  if(d.status==="scoped_ready"){
    assert.ok(d.scopedRelease && d.scopedRelease.reviewedBy && d.scopedRelease.reviewedAt, d.slug+" scoped review missing");
    assert.ok(d.scopedRelease.scope && d.scopedRelease.scope.length>80, d.slug+" scoped content policy missing");
    assert.ok(Array.isArray(d.scopedRelease.exclusions) && d.scopedRelease.exclusions.length>=3,d.slug+" scoped exclusions missing");
    assert.ok(Array.isArray(d.scopedRelease.publishedClaims) && d.scopedRelease.publishedClaims.length>=10,d.slug+" published claims missing");
    for(const id of d.scopedRelease.publishedClaims){
      const c=d.claims.find(x=>x.id===id);
      assert.ok(c && ["A","B"].includes(c.grade),d.slug+" unverified published claim "+id);
    }
    for(const k of keys) assert.ok(claimTopics.has(k),d.slug+" topic "+k+" has no A/B evidence");
    assert.ok(d.gaps.length>0,d.slug+" scoped publication must preserve unresolved research questions");
    const modelFile=d.scopedRelease.articleFile;
    assert.ok(modelFile && fs.existsSync(modelFile),d.slug+" scoped article missing");
    const article=JSON.parse(fs.readFileSync(modelFile,"utf8"));
    assert.equal(article.slug,d.slug,d.slug+" article identity mismatch");
    const articleText=article.chapters.flatMap(x=>(x.blocks||[]).map(b=>b.html||"")).join("\\n");
    for(const phrase of d.scopedRelease.forbiddenArticleFragments||[]) assert.ok(!articleText.includes(phrase),d.slug+" forbidden unverified specification: "+phrase);
    assert.ok(articleText.includes("13-2729-35"),d.slug+" missing FR variant");
    ready++;
  }else if(d.status==="ready"){
    assert.equal(d.gaps.length,0,d.slug+" cannot be ready with open gaps");
    assert.ok(d.reviewedBy && d.reviewedAt,d.slug+" requires human research review");
    for(const k of keys){
      assert.equal(d.topics[k].state,"verified",d.slug+" topic "+k+" not verified");
      assert.ok(claimTopics.has(k),d.slug+" topic "+k+" has no A/B evidence");
    }
    ready++;
  }else incomplete++;
  if(release && d.slug===target)assert.ok(["ready","scoped_ready"].includes(d.status),d.slug+" RESEARCH_NOT_READY");
  console.log("RESEARCH_RECORD="+d.slug+"; status="+d.status+"; claims="+d.claims.length+"; gaps="+d.gaps.length);
}
if(release)assert.ok(files.includes(target+".json"),"No research record for "+target);
console.log("RESEARCH_GATE=PASS; releasable="+ready+"; needs_research="+incomplete);

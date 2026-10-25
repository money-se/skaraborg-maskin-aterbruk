import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import assert from "node:assert/strict";
const root=path.resolve(process.cwd(),"..");
const built=path.join(root,"_maskinarkiv-preview","maskinarkiv");
const dest=path.join(root,"_maskinarkiv-release-review","maskinarkiv");
const slugs=["stiga-park-16","husqvarna-rider-13","husqvarna-lth151","stiga-villa-12-hst","jonsered-lt2115"];
fs.rmSync(path.dirname(dest),{recursive:true,force:true});
fs.mkdirSync(dest,{recursive:true});
function useSharedSiteShell(html) {
  html = html.replace(/<header\b(?=[^>]*class\s*=\s*["'][^"']*\bsmar-site-header\b)[^>]*>[\s\S]*?<\/header>/gi, "");
  html = html.replace(/<footer\b(?=[^>]*class\s*=\s*["'][^"']*\bsite-footer\b)[^>]*>[\s\S]*?<\/footer>/gi, "");
  if (!html.includes('id="site-header"')) html = html.replace(/<body\b[^>]*>/i, x => x + '<div id="site-header"></div>');
  if (!html.includes('id="site-footer"')) html = html.replace(/<\/body>/i, '<div id="site-footer"></div></body>');
  if (!html.includes('data-shared-site-shell')) html = html.replace(/<\/head>/i, '<script defer src="/partials1/site-shell.js" data-shared-site-shell></script></head>');
  return html;
}

const files=[];
for(const slug of slugs){
 const name=slug+".html";
 const source=path.join(built,name);
 const existing=path.join(root,"maskinarkiv",name);
 assert.ok(fs.existsSync(source)&&fs.existsSync(existing),"Missing release file: "+name);
 const updated=Buffer.from(useSharedSiteShell(fs.readFileSync(source,"utf8")),"utf8");
 const original=fs.readFileSync(existing);
 const sha=b=>crypto.createHash("sha256").update(b).digest("hex");
 assert.ok(updated.includes(Buffer.from('rel="canonical"')),"Missing SEO canonical: "+name);
 fs.writeFileSync(path.join(dest,name),updated);
 files.push({path:"maskinarkiv/"+name,original_sha256:sha(original),new_sha256:sha(updated),old_bytes:original.length,new_bytes:updated.length,changed:sha(original)!==sha(updated)});
}
const report={mode:"REVIEW_ONLY_DO_NOT_DEPLOY",releaseFiles:files,filesChanged:files.filter(f=>f.changed).length,allowedPaths:files.map(f=>f.path),notes:"Only these 5 HTML files may be proposed for an independently approved production PR. Never copy preview/index.html or noindex preview versions to production."};
fs.writeFileSync(path.join(root,"_maskinarkiv-release-review","manifest.json"),JSON.stringify(report,null,2)+"\n");
console.log("MASKINARKIV_2_RELEASE_STAGE=PASS; files="+files.length+"; changed="+report.filesChanged);

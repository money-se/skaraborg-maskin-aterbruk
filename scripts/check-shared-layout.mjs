// Read-only audit of public HTML pages that should use the shared site shell.
import fs from "node:fs";
import { execFileSync } from "node:child_process";

const files = execFileSync("git", ["ls-files", "-z", "--", "*.html"], { encoding:"utf8" }).split("\0").filter(Boolean);
const sitemap = fs.readFileSync("sitemap.xml", "utf8");
const inSitemap = new Set([...sitemap.matchAll(/<loc>(.*?)<\/loc>/g)].map(m => m[1].replace("https://skaraborgmaskin.se/","") || "index.html"));
const isExcluded = p => /forhandsvisning|forhandsgranskning|experiment|preview|test|granskning|backup|archiv|utkast|demo|\/_/i.test(p) ||
  /(^|\/)(admin|personal|inkorg|statistik-admin|tavling-admin|veckoblogg-admin|annonskontakt|.*-admin|partials1\/)/i.test(p);
const publicPages = files.filter(p => inSitemap.has(p) || !isExcluded(p));
const errors = [];
for (const page of publicPages) {
  const html = fs.readFileSync(page, "utf8");
  const requirements = [
    ["shared script", /<script[^>]*src=["']\/partials1\/site-shell\.js["']/i],
    ["header mount", /id=["']site-header["']/i],
    ["footer mount", /id=["']site-footer["']/i],
  ];
  for (const [label, rule] of requirements) if (!rule.test(html)) errors.push(page + ": missing " + label);
  if (/<header\b(?=[^>]*class\s*=\s*["'][^"']*\bsmar-site-header\b)[^>]*>/i.test(html))
    errors.push(page + ": inlined shared header remains");
  if (/<footer\b(?=[^>]*class\s*=\s*["'][^"']*\bsite-footer\b)[^>]*>/i.test(html))
    errors.push(page + ": inlined shared footer remains");
}
const required = ["partials1/header.html","partials1/footer.html","partials1/site-shell.js",
  "data/habo-service-template.html.txt","scripts/generate_ad_seo.py","scripts/generate_competition_seo.py","scripts/generate_weekly_blog_seo.py","maskinarkiv-2/scripts/stage-production.mjs"];
for (const file of required) {
  if (!fs.readFileSync(file,"utf8").includes("site-shell")) {
    // Header/footer are the actual content sources, not shell consumers.
    if (!file.endsWith("header.html") && !file.endsWith("footer.html") && !file.endsWith("site-shell.js"))
      errors.push(file + ": does not use the shared shell");
  }
}
if (!fs.readFileSync("partials1/header.html","utf8").includes("data-metricool-tracker"))
  errors.push("partials1/header.html: tracker tag missing");
if (errors.length) {
  console.error(errors.join("\n"));
  process.exit(1);
}
console.log("SHARED_SITE_SHELL_OK=" + publicPages.length);

#!/usr/bin/env python3
"""Conservative, offline manufacturer PDF indexer; pip install pymupdf."""
import argparse,csv,hashlib,json,re
from pathlib import Path
from collections import defaultdict
import fitz
TOPICS={"troubleshooting":r"troubleshooting|felsökning","maintenance":r"service and maintenance|maintenance schedule|underhåll","fluids":r"oil change|fluid change|fluids","parts":r"parts list|parts catalogue|spare parts|reservdelskatalog","torques":r"torques|åtdragningsmoment"}
def scan(folder,out):
 out.mkdir(parents=True,exist_ok=True)
 docs=[];pages=[];review=[];errors=[]
 for path in sorted(folder.glob("*.pdf")):
  try:
   h=hashlib.sha256(path.read_bytes()).hexdigest()
   with fitz.open(path) as pdf:
    if pdf.needs_pass: raise ValueError("encrypted PDF")
    cover=" ".join(" ".join(pdf[i].get_text().split()) for i in range(min(3,len(pdf))))
    m=re.search(r"\bBLN\s*[-–]\s*(\d{4,6})\b",cover,re.I)
    docid="BLN-"+m.group(1) if m else "UNKNOWN:"+path.name
    d=re.search(r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s*,?\s*(?:19|20)\d{2}\b",cover,re.I)
    textpages=0
    for i,page in enumerate(pdf):
     text=" ".join(page.get_text().split())[:12000]
     if text:textpages+=1
     for topic,pattern in TOPICS.items():
      if re.search(pattern,text,re.I):pages.append([path.name,docid,i+1,topic,text[:150]])
     if text and len([r for r in review if r[0]==path.name])<20:
      m2=re.search(r"\b(?:\d+(?:[.,]\d+)?\s*(?:ml|cc|fl oz|Nm|psi)|20W[- ]?50)\b",text,re.I)
      if m2: review.append([path.name,docid,i+1,text[max(0,m2.start()-70):m2.end()+90],"needs_human_review"])
    docs.append([path.name,docid,d.group(0) if d else "",h,len(pdf),textpages,cover[:220]])
  except Exception as e:errors.append({"file":path.name,"error":str(e)[:200]})
 def save(name,header,rows):
  with (out/name).open("w",newline="",encoding="utf-8-sig") as f:
   w=csv.writer(f);w.writerow(header);w.writerows(rows)
 save("manuals.csv",["filename","document_id","edition","sha256","pdf_pages","text_pages","cover_excerpt"],docs)
 save("sections.csv",["filename","document_id","pdf_page","topic","excerpt"],pages)
 save("review_candidates.csv",["filename","document_id","pdf_page","candidate_text","status"],review)
 ids=defaultdict(list);hashes=defaultdict(list)
 for r in docs:
  if not r[1].startswith("UNKNOWN:"):ids[r[1]].append(r)
  hashes[r[3]].append(r[0])
 report={"documents":len(docs),"pages":sum(x[4] for x in docs),"errors":errors,"identical_files":[v for v in hashes.values() if len(v)>1],"revision_candidates":{k:[{"filename":r[0],"edition":r[2]} for r in v] for k,v in ids.items() if len({r[3] for r in v})>1},"caution":"Index and snippets are not verified facts. Image-only pages require manual inspection. Verify exact BOM/model, printed page, revision and OEM."}
 (out/"report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 return report
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("pdf_dir",type=Path);p.add_argument("--output",required=True,type=Path);a=p.parse_args()
 print(json.dumps(scan(a.pdf_dir,a.output),ensure_ascii=False))

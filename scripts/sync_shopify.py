#!/usr/bin/env python3
"""Read published Shopify product JSON, never copy admin-only data to the website."""
import datetime as dt
import json
import pathlib
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "data/shopify-items.json"
SHOP = "https://skaraborgmerch.se"
MAX_PAGES = 30

def clean(item):
    if not isinstance(item, dict): return None
    handle = item.get("handle")
    title = item.get("title")
    if not isinstance(handle, str) or not handle or not all(c.isalnum() or c == "-" for c in handle): return None
    if not isinstance(title, str) or not title.strip(): return None
    variants = item.get("variants") or []
    options = []
    for v in variants:
        if not isinstance(v, dict): continue
        try: price = float(v.get("price"))
        except (ValueError, TypeError): continue
        if price < 0 or price > 10000000: continue
        if v.get("available", True) is False: continue
        options.append(price)
    if not options: return None
    images = item.get("images") or []
    image = None
    for img in images:
        candidate = img.get("src") if isinstance(img, dict) else img
        if isinstance(candidate, str) and candidate.startswith("https://"):
            image = candidate
            break
    return {"title":title.strip()[:200], "url":f"{SHOP}/products/{handle}", "image":image,
            "price":min(options), "category":str(item.get("product_type") or "Övrigt")[:80],
            "handle":handle}

def child_handles():
    handles = set()
    for collection in ("barnklader", "baby"):
        for page in range(1, MAX_PAGES + 1):
            url = SHOP + "/collections/" + collection + "/products.json?" + urllib.parse.urlencode({"limit":250,"page":page})
            req = urllib.request.Request(url, headers={"User-Agent":"SkaraborgMaskinShopifyCatalog/1.0","Accept":"application/json"})
            with urllib.request.urlopen(req, timeout=30) as response:
                if response.status != 200 or "json" not in response.headers.get("Content-Type","").lower():
                    raise ValueError("Cannot verify child collections")
                data = json.load(response)
            rows = data.get("products") if isinstance(data,dict) else None
            if not isinstance(rows,list): raise ValueError("Unexpected child collection response")
            handles.update(x.get("handle") for x in rows if isinstance(x,dict) and isinstance(x.get("handle"),str))
            if len(rows) < 250: break
        else: raise ValueError("Child collection pagination limit reached")
    if not handles: raise ValueError("Child collection list was unexpectedly empty")
    return handles

def main():
    result = []
    seen = set()
    # Shopify public products endpoint uses a page parameter for classic JSON catalog.
    for page in range(1, MAX_PAGES + 1):
        url = SHOP + "/products.json?" + urllib.parse.urlencode({"limit":250,"page":page})
        request = urllib.request.Request(url, headers={"User-Agent":"SkaraborgMaskinShopifyCatalog/1.0","Accept":"application/json"})
        with urllib.request.urlopen(request, timeout=30) as response:
            if response.status != 200 or "json" not in response.headers.get("Content-Type","").lower():
                raise ValueError("Shopify public JSON endpoint not available")
            data = json.load(response)
        rows = data.get("products") if isinstance(data, dict) else None
        if not isinstance(rows,list): raise ValueError("Unexpected Shopify response; feed not modified")
        for item in rows:
            normalized = clean(item)
            if normalized and normalized["handle"] not in seen:
                seen.add(normalized["handle"])
                result.append(normalized)
        if len(rows) < 250: break
    else:
        raise ValueError("Pagination limit reached; feed not modified")
    if not result: raise ValueError("No public products available; feed not modified")
    children = child_handles()
    for item in result:
        item["audience"] = "barn" if item["handle"] in children else "vuxna"
    result.sort(key=lambda x:x["title"].casefold())
    payload = {"status":"ready","updated_at":dt.datetime.now(dt.timezone.utc).isoformat(),"items":result}
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("SHOPIFY_PUBLIC_CATALOG_PRODUCTS=",len(result))
if __name__ == "__main__":
    main()

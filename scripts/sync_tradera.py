#!/usr/bin/env python3
"""Read-only Tradera seller feed. Never sends credentials to the public website."""
import datetime as dt
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEST = ROOT / "data/tradera-items.json"
API = "https://api.tradera.com/v4/items/seller/"
TRADERA_LINK = re.compile(r"^https://(?:www\.)?tradera\.com/", re.I)

def first(d, *keys):
    for key in keys:
        if key in d and d[key] is not None:
            return d[key]
    return None

def iso(value):
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        date = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        if date.tzinfo is None:
            date = date.replace(tzinfo=dt.timezone.utc)
        return date.isoformat()
    except ValueError:
        return None

def normalize(item, now):
    if not isinstance(item, dict):
        return None
    ident = first(item, "id", "itemId")
    title = first(item, "shortDescription", "title", "name")
    if not isinstance(title, str) or not title.strip() or not isinstance(ident, (int,str)):
        return None
    end = iso(first(item, "endDate", "endTime", "endAt"))
    if not end or dt.datetime.fromisoformat(end) <= now:
        return None
    if first(item, "isEnded", "ended", "isSold", "sold") is True:
        return None
    status = first(item, "status", "itemStatus")
    # Tradera REST v4: status is an object containing ended, gotBidders and gotWinner.
    if not isinstance(status, dict) or status.get("ended") is not False or status.get("gotWinner") is not False:
        return None
    quantity = first(item, "remainingQuantity")
    if not isinstance(quantity, int) or quantity <= 0:
        return None
    url = first(item, "itemLink", "itemUrl", "url", "link")
    if not isinstance(url,str) or not TRADERA_LINK.match(url):
        category = first(item, "categoryId")
        if not isinstance(category, int):
            return None
        url = f"https://www.tradera.com/item/{category}/{ident}"
    image = first(item, "thumbnailImage", "thumbnailUrl", "imageUrl", "image", "imageLinks")
    if isinstance(image, list):
        image = image[0] if image else None
    if isinstance(image, dict):
        image = first(image, "url", "href", "imageUrl", "link")
    if isinstance(image, str) and image.startswith("http://"):
        image = "https://" + image[len("http://"):]
    if not (isinstance(image, str) and image.startswith("https://")):
        image = None
    item_type = item.get("itemType")
    if item_type == 3:
        value = item.get("buyItNowPrice")
        price_kind = "buy_now"
    elif item_type == 1:
        value = item.get("openingBid") if status.get("gotBidders") is False else item.get("maxBid")
        price_kind = "starting_bid" if status.get("gotBidders") is False else "current_bid"
    else:
        return None
    if isinstance(value, dict):
        value = first(value, "amount", "value")
    try:
        price = float(value) if value is not None else None
        if price is None or price <= 0 or price > 1e9:
            return None
    except (ValueError,TypeError):
        return None
    return {"id":str(ident),"title":title.strip()[:180],"url":url,"image":image,"price":price,"price_kind":price_kind,"end_at":end}

def main():
    app_id=os.environ["TRADERA_APP_ID"]
    app_key=os.environ["TRADERA_APP_KEY"]
    seller=os.getenv("TRADERA_SELLER_ID","5896660")
    if not seller.isdigit():
        raise ValueError("TRADERA_SELLER_ID must be numeric")
    request=urllib.request.Request(API+seller,headers={"X-App-Id":app_id,"X-App-Key":app_key,"Accept":"application/json","User-Agent":"SkaraborgMaskinTraderaCatalog/1.0"})
    with urllib.request.urlopen(request,timeout=25) as response:
        result=json.load(response)
    if isinstance(result,list):
        raw=result
    elif isinstance(result,dict) and isinstance(result.get("items"),list):
        raw=result["items"]
    else:
        raise ValueError("Unexpected Tradera response schema; refusing to overwrite current feed")
    now=dt.datetime.now(dt.timezone.utc)
    normalized=[n for r in raw if (n:=normalize(r,now)) is not None]
    if raw and not normalized:
        raise ValueError("Tradera returned listings but none could be parsed; refusing to overwrite feed")
    payload={"status":"ready","updated_at":now.isoformat(),"items":normalized}
    DEST.parent.mkdir(exist_ok=True)
    DEST.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"Tradera sync validated: {len(normalized)} active listings")
if __name__=="__main__":
    try:main()
    except (KeyError,ValueError,urllib.error.HTTPError,urllib.error.URLError,TimeoutError) as err:
        print(f"Tradera sync failed ({type(err).__name__}); existing feed preserved",file=sys.stderr)
        sys.exit(1)

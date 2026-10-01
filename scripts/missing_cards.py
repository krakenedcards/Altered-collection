#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
cards=json.loads((root/"data/cards.json").read_text(encoding="utf-8"))["cards"]
owned=json.loads((root/"data/collection.json").read_text(encoding="utf-8"))["cards"]
rows=[]
for c in cards:
    o=owned.get(c["ref"], {"count":0,"has_french":False})
    count=max(0,int(o.get("count",0)))
    fr=bool(o.get("has_french",False))
    if count < 4 or not fr:
        rows.append({**c,"count":count,"has_french":fr,
                     "missing_total":max(0,4-count),
                     "missing_french":0 if fr else 1})
rows.sort(key=lambda x:(x["set"],str(x["collector_number"] or ""),x["rarity"],x["ref"]))
print("Incomplete cards:",len(rows))
print("Total copies still needed:",sum(x["missing_total"] for x in rows))
print("French copies still needed:",sum(x["missing_french"] for x in rows))
for x in rows:
    print(f'{x["ref"]}\t{x["set"]}\t{x["collector_number"]}\t{x["name_fr"]}\t{x["rarity"]}\t{x["faction"]}\t{x["count"]}/4\tFR={"yes" if x["has_french"] else "no"}\tneed={x["missing_total"]}')

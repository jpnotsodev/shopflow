import shutil
import sys
import json
from pathlib import Path

from api.app import fetch_page


SOURCES = Path(__file__).parent / "sources"
RAW = Path(__file__).parent / "data" / "raw"
ORDERS = RAW / "orders"
ORDERS.mkdir(parents=True, exist_ok=True)


def ingest():

    for file in SOURCES.iterdir():
        shutil.copy(file, (RAW / file.name))

    args = sys.argv[1:]

    for arg in args:
        out = ORDERS / f"dt={arg}"
        out.mkdir(parents=True, exist_ok=True)
        orders = out / "orders.jsonl"
        page, count = 1, 0
        with open(orders, "w", encoding="utf-8") as f:
            while page:
                data = fetch_page(arg, page)
                for order in data["orders"]:
                    f.write(f"{json.dumps(order)}\n")
                count += len(data["orders"])
                page = data["next_page"]


        manifest = {"day": arg, "orders": count, "path": f"{orders}"}
        (out / "_manifest.json").write_text(json.dumps(manifest))

        # print(manifest) 

    return manifest


ingest()
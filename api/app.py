import os
import random
from pathlib import Path


PAGE_SIZE = 500
STATE = Path(__file__).parent / "data" / "state"


def total_orders(day):
    return 6000 + random.Random(day).randint(1, 2000)

def make_order(day, n):
    r = random.Random(f"{day}-{n}")
    items = [{"sku": f"SKU-00{r.randint(1, 41):02d}",
             "qty": r.choice([1] * 12 + [2] * 5 + [3] * 2 + [0])} for _ in range(r.randint(1, 4))]
    return {"order_id": f"{day}-{n:05d}", 
            "customer_id": r.randint(1, 2010), 
            "ordered_at": f"{day} {r.randint(1, 23):02d}:{r.randint(0, 59):02d}:00",
            "items": items,
            "status": r.choice(["paid"] * 10 + ["refunded", "cancelled"])}

def fetch_page(day, page):
    outage = STATE / f"outage_{day}"
    if os.environ.get("API_FLAKY") == "1" and page == 3 and not outage.exists():
        STATE.mkdir(parents=True, exist_ok=True)
        outage.touch()
        raise ConnectionError("API timed out on page {page}")

    total = total_orders(day)
    start = (page - 1) * PAGE_SIZE
    orders = [make_order(day, n) for n in range(start + 1, min(start + PAGE_SIZE, total) + 1)]

    if page > 1:
        orders.append(make_order(day, start))

    next_page = page + 1 if start + PAGE_SIZE < total else None

    return {"day": day, "page": page, "orders": orders, "next_page": next_page}
import random
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

random.seed(42)

LOCATIONS = ["LOC-01", "LOC-02", "LOC-03", "LOC-04", "LOC-05"]
NUM_SKUS = 100
BASE_DATE = date(2026, 11, 19)
INACTIVE_REASONS = ["Out of stock", "Brand approval pending", "Price issue"]
CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

listing_rows = []
stock_rows = []

for i in range(1, NUM_SKUS + 1):
    sku = f"SKU-{i:04d}"
    asin = "B0" + "".join(random.choices(CHARS, k=8))
    mrp = round(random.uniform(50, 2000), 2)

    for loc in LOCATIONS:
        status = random.choices(
            ["Active", "Inactive", "Incomplete"], weights=[70, 20, 10]
        )[0]

        if status == "Inactive":
            reason = random.choice(INACTIVE_REASONS)
        elif status == "Incomplete":
            reason = "Missing attributes"
        else:
            reason = None

        if reason == "Out of stock":
            qty = 0
        else:
            qty = random.randint(5, 200)

        listed_date = BASE_DATE - timedelta(days=random.randint(0, 365))

        listing_rows.append({
            "asin": asin,
            "sku": sku,
            "location": loc,
            "status": status,
            "reason": reason,
            "listed_date": listed_date,
        })
        stock_rows.append({
            "sku": sku,
            "location": loc,
            "erp_qty": qty,
            "mrp": mrp,
        })

out = Path("data")
out.mkdir(exist_ok=True)

listings = pd.DataFrame(listing_rows)
erp_stock = pd.DataFrame(stock_rows)

listings.to_csv(out / "listings.csv", index=False)
erp_stock.to_csv(out / "erp_stock.csv", index=False)

print("listings rows:", len(listings))
print("erp_stock rows:", len(erp_stock))
print(listings["status"].value_counts())
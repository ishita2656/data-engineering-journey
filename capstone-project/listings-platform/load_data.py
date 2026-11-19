import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

DATA = Path("data")

listings = pd.read_csv(DATA / "listings.csv")
listings["listed_date"] = pd.to_datetime(listings["listed_date"]).dt.date
erp_stock = pd.read_csv(DATA / "erp_stock.csv")

print("Rows read from CSV -> listings:", len(listings), "| erp_stock:", len(erp_stock))

with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE listings, erp_stock"))
    listings.to_sql("listings", conn, if_exists="append", index=False)
    erp_stock.to_sql("erp_stock", conn, if_exists="append", index=False)
    n_listings = conn.execute(text("SELECT COUNT(*) FROM listings")).scalar()
    n_stock = conn.execute(text("SELECT COUNT(*) FROM erp_stock")).scalar()

print("Rows now in Neon -> listings:", n_listings, "| erp_stock:", n_stock)
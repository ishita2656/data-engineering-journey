\# Listings Data Platform



A data pipeline that loads marketplace listing and stock data into a Postgres database.



\## What it does

\- Generates fake listings and ERP stock data (500 rows each) as CSV files

\- Loads them into Neon Postgres using Python

\- Safe to run twice: running it again replaces the data and never creates duplicates



\## Tools used

Python, pandas, SQLAlchemy, Neon Postgres, Git



\## How to run

1\. Create a .env file with your DATABASE\_URL

2\. pip install -r requirements.txt

3\. python generate\_data.py

4\. python load\_data.py



\## Notes

All data is fake. Each SKU appears once per location, so the primary key is (sku, location).


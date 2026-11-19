import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

db_url = os.getenv("DATABASE_URL")

engine = create_engine(db_url)

with engine.connect() as conn:
    count = conn.execute(text("SELECT COUNT(*) FROM listings")).scalar()
    print("Rows in listings:", count)
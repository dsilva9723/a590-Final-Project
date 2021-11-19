import sqlite3
import pandas as pd 

db = sqlite3.connect("flight.db")
flights_df = pd.read_sql("select * from flights", db)

with open("flights.json", "w", encoding="utf-8") as f:
    flights_df.to_json(f, orient="records")

db.close()

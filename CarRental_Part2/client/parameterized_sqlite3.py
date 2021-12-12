"""Two ways of binding parameters in SQLite3
"""
import pandas as pd
import sys, os, sqlite3
from sqlalchemy import create_engine, types

engine, db = None, None
# make db connection
engine = create_engine(r"sqlite:///C:\Users\trww3\Desktop\CarRental\redesign\Rental.db")

# qmark style 
if engine is not None:
    db = engine.connect()
    params = ['Wrangler', 'xB'] 
    sql = "select * from specs where vehiclemodel like ? or vehiclemodel like ?"
    specs = pd.read_sql(sql=sql, con=db, params=params)
    print(f"qmark style:\n {specs}")


if engine is not None:
    db = engine.connect()
    params = ['Corolla', 'Civic'] 
    sql = "select * from specs where vehiclemodel like ? or vehiclemodel like ?"
    specs = pd.read_sql(sql=sql, con=db, params=params)
    print(f"qmark style:\n {specs}")


if engine is not None:
    db = engine.connect()
    params = ['Atlanta', 'Oakland'] 
    sql = "select * from carrental where airportcity like ? or airportcity like ?"
    specs = pd.read_sql(sql=sql, con=db, params=params)
    print(f"qmark style:\n {specs}")




"""Two ways of binding parameters in SQLite3
"""
import pandas as pd
import sys, os, sqlite3
from sqlalchemy import create_engine, types

engine, db = None, None
# make db connection
engine = create_engine("sqlite:///flight.db")

# qmark style 
if engine is not None:
    db = engine.connect()
    params = ['DFW', 'JFK'] 
    sql = "select * from flights where origin like ? or origin like ?"
    flights = pd.read_sql(sql=sql, con=db, params=params)
    print(f"qmark style:\n {flights}")


# named style
if engine is not None:
    db = engine.connect()
    params = {
        'value1': 'DFW',
        'value2': 'JFK'
    }
    sql = "select * from flights where origin like :value1 or origin like :value2"
    print(f'named style:\n {pd.read_sql(sql=sql, con=db, params=params)}')

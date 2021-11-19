"""MySQL binding parameters
"""
import pandas as pd
import sys, os
from sqlalchemy import create_engine, types
# import module from function directory
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from function import config

engine, db = None, None
# make db connection
engine = config.sqlalchemy_mysql("flight2")

# %s style
if engine is not None:
    db = engine.connect()
    params = ('DFW','JFK') #tuple
    sql = "select * from flight where origin like %s or origin like %s"
    df = pd.read_sql(sql=sql, con=db, params=params)
    print(f'{df}')
 
